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
<img src="https://cdn4.telesco.pe/file/dxjWttm1eoD7zvH2Mb2Uw7FZ-8PkdNfpiViSv_GRNxSYrbP3suAn01wluDKPcu7rJ0hGvSwteZGH1xjXW1Kfm-2QI4q00AN9vUC-MItuVyXFhda0DE59wXlQwG1IHHMy3NDWdfwRFfBacrr6mxrQCGcy8jcjxURnFqZBdRlQ9EZcrl57kYXveMEkGne0mSAmR-Z0EnryxOGI8ti4GBLUK1CeUv-kuwnPQIznEU3WqLjsnh3BU_LR5EG9x1oKN0yIm6fma-vSDmfDR__fSOfFIg3BqCKTsju9tuk39dnvcKqdKNNWLCBdIJy6wWfqSY4LYtHRhzR7KUl8OR-tbUOUdw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 625K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 20:20:57</div>
<hr>

<div class="tg-post" id="msg-26957">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsnaj5aszU3Qv6imQztKtUejr7ZOLkHmVq7Z5zQ1E8n_Nr-z8W9mP3gVnPq2u6wspR1lP0_4ZjE2UGt3wt0aqF6jl0EsnRZjo08UVxrC8U59fBISdE_1SSOHjwNvuzFZOChBFYoQLeC_EiJWFo6CpZAJWq9o3BhvSXkpJ5zFVur_HMtXurq3LDA0GXaFrZS1R32qUkHdEN6lKD7KxEGV-gQG4-AkE0XF5Q8AFn9QRzj_4KALz9pMn_WxplHxWMZkJ61GLJsmXFLhIcPS06a4hXUQAkSQcFpSiZL_h9HaYgdX8r6RICNCum37HQ1ZLPHN_WYzosWOnw-xTYxHbGhEzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
هایلایتی از عملکرد خیره کننده فابیو آبرئو مهاجم 33 ساله انگولایی مدنطر استقلال در سال 2025.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/persiana_Soccer/26957" target="_blank">📅 20:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26955">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZfDErY7x4m8eplMUlbzvYbhkuHilawZnr1pGjNkeXpGu0BG_tfPIObaewToDkbNSKIu4m2meL1WUBIlqEKdSxZbAA9kVPqVU1iAclnIsHv9rUF-rrzN8H6WJYfcbH22vJy-U3akdSkmwN3Xr1jp_P_3ik1LSNUa6Kggbwvqt5yhGh1Y9BVwDL72TMUGupN-2JFkMgwoZaLgC2b1VD8bi0CwaQxNYxVfkku2TtrkeOH4rZZEhLkcZfsoyaX4Z162tv8dPXtH_pJ2SOicsdeQBhjlT-DN-lZ9drmSOzR39Jh0k9ZWFq3cSVJR5x3BftuHO6j5LS-wxisYmUIyqy06eNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NCnLKJ6dzrNWYcaYIG5q2nYcUiOS46An4ktx-25VYySRf4SlsEZr4yn95uHgnF-GH9k0bXHzFS4l6YCzj9Vx51ogxBVGQws-C-5AAyMB7dS-jTEAH8xKA3W8-HqtJWOo5aguIpreMaCPteAHWWusN0JlVCG_9hayqcBkhygX5HzgY9XZqwINLOBTE_sCoS-T9Hk0HFxTqRBt5sxkgts6_8jPjPQVz8TkqPWlTuLpnZK3hweRHTH_WxJ3xK05Dqs8VCFUsOiHnvdrrYypV3IdVHniCQWfsczFKL0QHfQJhUCA-Tzg2ef-XN3rsQ1zDA_nPDTLVA0uLPu3l5H_RrTC2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📍
برسی تموم اپراتور های اینترنت در ایران. این‌‌ پست‌رو ذخیره‌کن و برای دوستات بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/26955" target="_blank">📅 19:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26954">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-dEmR23PYm_wC-hGhFGDTVa3ovmMQKrLTznYxRCjETZL4lauEMyT8W6aePt9yT-TzyzNw6cZYBVaVp4Xs6c6NqHYChjR3es_EdMiuK3wAVstL2rDRJTiUGzPqUUGKh0fJWt_57vmoepiBGqTAjpDrEAA1V0hHYlhmSsBEt1Khn2rh8GqtHD97v8WgGpGMsQDa-UALKnOa30HnWHe7D-KfRoarYFAT_MzR3E6R6qP5Z1ZnnQ9O7bcscuf_adCu_NmXNRw5ARYyxkqK4OmfHqW4lxlePW4XFGloTymMYPSiKEYsPJL7s5M8LWQ-HVquAB43VyfC4NXOKM06PjfI4PFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌ ملی‌والیبال‌ آمریکا در نیمه نهایی لیگ ملت‌ ها بابرتری‌سخت و نفسگیر سه بر دو مقابل ژاپن به فینال رقابت‌ها راه پیدا کرد؛ ژاپن بالاخره باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/26954" target="_blank">📅 19:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26953">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMD5MdQ7XIuCJrBrlLFagx76psu_i9F7Rap1Z7uRGfyQYyFlfe5MA-ByjX1XjXN5aB12XmAig_sErkNspN9Q59c0UOcHjmzt3ack-96pMYGbuGLhX_IHx7oxSe4kGuUkCMAaJXPm2WMEHaSlp5ZmtxUtTTqtNDH2ogQgSO14VaqoL_2b-XoCgvIT-gg_sA7AsMBv61pvktarRgPTY3R_P-OarJqdrXP99pfz7VCakAnJY0nAP8OJY2FMARPSteaLemcdXPExunSczTUP85GEVTamAifbX8aWIEPE2dpcV7TJh6fYWwe7EKzbJtcgh3safbNLzU08zYuKNEpjBlo4Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ مهران احمدی هافبک تهاجمی تیم استقلال به دلیل مصدومیت دیدار هفته اول با مس شهر بابک رو از دست داد. باتوجه به این رقابت های این فصل بسیار فشرده‌تر از فصل قبل برگزار میشه‌. اگه‌دوره‌بدنسازی‌خوب انجام‌نشده‌باشه دهن بازیکنان لیگ‌برتری سرویسه‌. هرسه روز…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/26953" target="_blank">📅 18:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26952">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf02af4598.mp4?token=M-CX7UuEGKZIkDbWi0-ciAZ0cEJwCkOhr5ME2Hv5NgAOasA7Y6Ru6vkLj5-OhAl6T9QgWT_TpJET8IhXKOuxN2ZaNpyLdHwNGMHwnSEIFE3KxgY0ejJ16TMv0sJ6G5Imnjv4NQVQjq8MNzfQxiQirzUeZxfzeysJyAxUCskYAM228lYQ1ksY6HkuBBNtPIQUFsgZhZ7As0KyZxHU1Z-acqXN0YSbJxhxCsJxI4ew1GXZms20VBt3VajK44KN3SLoGu7FGyqjgZ0EvMEIBBbX6j1htmc_HE1RCN_XnoIKzoi6GdZpL4NRVKnZNNRmemsdCOAAYYyvvyzxii95uotKkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf02af4598.mp4?token=M-CX7UuEGKZIkDbWi0-ciAZ0cEJwCkOhr5ME2Hv5NgAOasA7Y6Ru6vkLj5-OhAl6T9QgWT_TpJET8IhXKOuxN2ZaNpyLdHwNGMHwnSEIFE3KxgY0ejJ16TMv0sJ6G5Imnjv4NQVQjq8MNzfQxiQirzUeZxfzeysJyAxUCskYAM228lYQ1ksY6HkuBBNtPIQUFsgZhZ7As0KyZxHU1Z-acqXN0YSbJxhxCsJxI4ew1GXZms20VBt3VajK44KN3SLoGu7FGyqjgZ0EvMEIBBbX6j1htmc_HE1RCN_XnoIKzoi6GdZpL4NRVKnZNNRmemsdCOAAYYyvvyzxii95uotKkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌ ملی‌والیبال‌ آمریکا در نیمه نهایی لیگ ملت‌ ها بابرتری‌سخت و نفسگیر سه بر دو مقابل ژاپن به فینال رقابت‌ها راه پیدا کرد؛ ژاپن بالاخره باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/26952" target="_blank">📅 18:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26951">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbUwnAscmcO_b8ea0OXyH0-xnoQK-llRi4FmK8yoPeeA0oZdplN2UcBSgqFGEBmgBj1HMuG7irczTukl95DKUoYSIqJORBZe82sQWUYoKjFqgP3rBpzqO_fUREpY04Cm4h_nfpRFUr6tV9KywLqdQvklcNFJLi8lLi-fa6V-srCnBlHpjj-A5gQNckzS4ceyeh_5Qz5VHiLCKkskQEozceeA4071INcHL4KCWAoAB6zpf3OeX5xAw4csOdALbzuYkIde-qbN_tbNgvLSigJ_dAXxPzYvaTPu70Fl3Z4o91QswZNANTC-0o691rqt3P8yOKzWLcLy-ApGKFKXbp7HeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/26951" target="_blank">📅 17:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26950">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ab908f0eb.mp4?token=ASTE1FasX188jkZiuyTs-F0FK0BsO_cVFKCQQIB2JUIt_tQfVUTPu3Gt47d7Zb3549furKNZtGxGY60m51wBVdhZMb45vWW2In5pVY539PLV8PiSKxyeHSfM7ViCbxwLM4aAmYjfyJd0bULmZHqDwqGd-c0n48ICABV5XpcJKiEfRGxz_zpT5K49NjFIeQlBqp3r0goPyuxPHfg1bfxa-S6MClOcOG-WfV2LOuY7Pt0vIo4zUTW1OLox4LjJzozUJKbq4rbMqZK7rZHC_FVCEhXiii1DNa3NKaFviq5-_ycqvD7DxJspg1BGEhV5htD4HCpBC9v1_-8Ax765pVlMAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ab908f0eb.mp4?token=ASTE1FasX188jkZiuyTs-F0FK0BsO_cVFKCQQIB2JUIt_tQfVUTPu3Gt47d7Zb3549furKNZtGxGY60m51wBVdhZMb45vWW2In5pVY539PLV8PiSKxyeHSfM7ViCbxwLM4aAmYjfyJd0bULmZHqDwqGd-c0n48ICABV5XpcJKiEfRGxz_zpT5K49NjFIeQlBqp3r0goPyuxPHfg1bfxa-S6MClOcOG-WfV2LOuY7Pt0vIo4zUTW1OLox4LjJzozUJKbq4rbMqZK7rZHC_FVCEhXiii1DNa3NKaFviq5-_ycqvD7DxJspg1BGEhV5htD4HCpBC9v1_-8Ax765pVlMAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آمادگی بدنی خیره کننده احمدرضا عابدزاده گلر سابق تیم ملی و سرخابی‌ها در سن 60 سالگی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/26950" target="_blank">📅 17:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26949">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVNPF5ylIfHw6rRcCHblYkuAx1f4tdqALGOwWz-Pv8SmhtVYmHrggrtcwbx6ag1zMuxZFoYVIL3mvHjH5X9IUDKRNqrqwxrq_GZX_jMeyZUYvfQzmATi2X0F4FtToT09G4D5oDzyKehXww3uV5ogHFU2q77wD_gHMACMXveVaNkAZMKNVFbkdDC_lf6GTghalY2qdVSD_ZWjfJnnHgE1VaNEnelZPD1ggXC324BxqiilGr7dGz_aS_pv4shgdxEZQLAHlmfDyB5hiUpfy6Jc-LBz-3ezjuV3XjostusFuISOYqS-whsTfL9mSysDzopvqaUigoZLCBrpvxVQkFajBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛ از مصاف شاگردان ژابی با تاتنهام در استرالیا تا بازی رئال مادرید برابر فیورنتینا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/26949" target="_blank">📅 17:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26948">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQNhnn6_P5sCQli5uZytMLWxgVap_1t5pt9xfVrUR2OqV3LhONyrXtZT0WvnaJDEqVLb3EVcAvJ3f2WUd2flwP156YvYyGEDj2x8Wmp41dL_CDscDPx6uP3Cfl2a9lg9xD5487lbNfTyl2fxkja0YEbKKo2neOAhpuQ2f_jyfqRpouQJfIJplZwFApVTnQNeICwM3pVit02yFYtKVqB9N4WysFYI_2-Ew5WnzUF05FA_1EL79toJfGJTkFqFQqnKNVvS1wl9Pq9vbtbgwWGqhG4ZWwe_dll3JOOux86l0dIkk6n37aIlpZtPkPrakRjxvogks4dNzWRJnefRPGgvRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌تارتارسرمربی‌پرسپولیس باردیگر در تماس تلفنی به مدیریت باشگاه اعلام کرده نیازی به حضور تیوی بیفوما و دنیل گرا ندارد و این دو بازیکن رو در لیست مازاد سرخ‌ها قرار داده. اورونوف، سرگیف و باکیچ 3 خارجیکه تارتار سبک‌بازیشون رو پذیرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/26948" target="_blank">📅 17:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26947">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3XPZChWv2TYjxTnrvlhhZuuRH4m1HTX_CuZw12ZFwobKCO41195qaQDpYSiMFPYt0g2fHwQP-QRvTrZlXfy9kVU7wSajBvMRTqTr-HYGdYY_B8AzITX0JsuQ-EvOYYjy5bYSedcPSe0pr5csG8WOjT8NnxskyIoMkBwN4IRZfbFFW16jzHji-fOQXRTEIh6FU8AtTc9rTH7b1d9lZEwGLyL_AGz0tghN0zxSwAyTXgDL-XqW8cLaZtAqOW2kdu1Xh7r5R3UEkezwCoPdmoejbD1Uc9h_U2n-_3dL7L705pM_NZI6g8nK58CcSzaE4vr4kIcJaaI7Cc_ZiMbBrEN2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#تکمیلی؛ اسپورت: PSG این هفته از فران تورس خریدجدیدخود رونمایی خواهد کرد. تورس به لاپورتا اعلام کرده هیچ علاقه‌ای برای موندن در بارسا نداره و میخواد شاگرد پدر زنش در تیم PSG بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/26947" target="_blank">📅 16:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26946">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HytOmBI9-yN24uC31VcJrrFrGH0GQp9D206okleJ2jW8lffkB45ODCMMezOf7bDpRxTbKracbp1yv5oA_NqdyDFQ-GptZDkBGI_AFYbBYSxa2KoS0rC3PWYQUSxlFiB5eGzRq0skqGqm_ThPK0w8GEBB6lXhpGoGO8oTV5ai-yYgk-inhQTD_aVdozwmd-6X8nVP221mEiderNRjDYYrtdTmnjCaldgSUEJS4ifE7dhPqHW3d0PCWiXv4q_Y-iISowIX8-kReKUzCeDBfveXUQiofPiwvIE_r953ri_xz2C0B4A8kBGbDPFiamjh3VUuwI-OdKKUauXkYuKOEyi8xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/26946" target="_blank">📅 16:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26945">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vev9AcsSR_XTbQoOUH02RttiuAVPsvEikWkpVai-QUIV-4diZEHXMlI82RwofTZfO-5XqcFPZlKuSEstPuNePXfkKhB_6nMPRYM4hVCIKcMLe2vuVqGAeo_n2V3eV3wM__EiieOFm6A8D0LTheZMQ9sm9VMHDuJVqqTj54wgJ0Tm82CHWecbkHBWvmJPXFbFbvuEK5e5rYKwJqgnZXjxDbMp7jur6irm-4PApAZSfKw0h3ns0I9xfvxkrAo6xMOijtIBvVs1-8cAN8lh2uIlPl5v9UooyYolrZ0b1uBPKNGU0IyvYbjYfDmikFZ2inx6PyT9sdP-TmOqXrMKQ5JM1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/26945" target="_blank">📅 16:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26944">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSCyDKaxOarI0GZaK4-PJx9Rz-xiuQ4BSqsi9lks1TefYoPqXKimRKuRyYvOcQu__5LAsoJ5jpI1ZKPi3OPr2OUKbCncY0ZvsXvo-GFqlU67-Z1sttEoHANHhwjx_M5swY8IFoiDVGikyfjIHyMdctw2DTjhSPsL6yHNcuuNt1wowTWe42FplNGWEuMxs0FRmV7i8LiHxthOwO8GYWvnjJCaw8NmC-GfQUEAg3ZWVm7qMYwn59mBbfMbI6rJIAN19im7UNFWz24Rj8R47xcnu4lwQhmLFaj_cXtpVMhwJmPm7rPdfBi5WO0Jq-hQP48uUclMtgNcBP3fH5bCvMcydw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
طبق شنیده‌های‌رسانه پرشیانا؛ فردا جلسه‌ای مهم بین‌مدیران‌دوباشگاه خیبر خرم آباد و استقلال بر سرانتقال‌مهدی‌گودرزی و مسعود محبی برگزار خواهد شد. مدیریت استقلال به این بازیکن اعلام کرده که با ماقرارداد ببندید و تا نیم فصل در تیم خیبر بمونید. قراره فردا تکلیف…</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/26944" target="_blank">📅 15:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26942">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSbXVg47Al8IkjRVuX64CUtBIT_UmUi1Y6v4lRA3KsdyCvg5LbdPOichGJhVK4G1kwovVb-3TdFV3GKwea0sHMyGJO2hDEVZjSaY_bKj5RUZGYWtki5wzsGhHi9ic85U58arGBuIFguwvQgC27M49W8ckzDg5YrvNlKhApY5N4r1GIGz-h0-MNOECYn1cA3cpjb2nzIwKdDbFSHijcrxc9uYl6hDbY0jM6cPyBa-HePahHbx8dwfmjQAnyxIanbuPO2zxkHyiX3moahfhFN6SXNR9-AL5UtJ20ipHagGtjas6cozYoodkiO4SeZgYYxEcL_57aRHoxejW_YX3j4NYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c22a2b9700.mp4?token=F4unTLIl0ln5En4Ekxn0QEBS2iSa8gtcmZ8rHDMtG0gFYAyywVRuk1UGrfxHKUTTvyj5tm55AeG2zNg1J3LThHEREzO2wHPYipzEau-ow-gD7Zzhcn-thE6-n6OcKfRNbRbSDBfm9jcZyYUP4MFK47xYZ7c7puxh4r8nBr-Fc0B8PWeU_WNGkL12qN6O7DfnA9lUAiKJYuPiqOAtZe81S1B2kLAR_VCMiSvhiKX4Y1fOALRjhcBGAaH3O0S91aVAeaDsCdEwSNOCjg-rOjd1ULcjvMwxV_4Kq_sXETX1q0tP3mcpTBYl7Co84XsDzdM5I4QV81inVLfVT9kFI-DWxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c22a2b9700.mp4?token=F4unTLIl0ln5En4Ekxn0QEBS2iSa8gtcmZ8rHDMtG0gFYAyywVRuk1UGrfxHKUTTvyj5tm55AeG2zNg1J3LThHEREzO2wHPYipzEau-ow-gD7Zzhcn-thE6-n6OcKfRNbRbSDBfm9jcZyYUP4MFK47xYZ7c7puxh4r8nBr-Fc0B8PWeU_WNGkL12qN6O7DfnA9lUAiKJYuPiqOAtZe81S1B2kLAR_VCMiSvhiKX4Y1fOALRjhcBGAaH3O0S91aVAeaDsCdEwSNOCjg-rOjd1ULcjvMwxV_4Kq_sXETX1q0tP3mcpTBYl7Co84XsDzdM5I4QV81inVLfVT9kFI-DWxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ ماخاچ‌قلعه دو روز به جواد حسین نژاد فرصت داده‌ که‌پاسخ‌نهایی خود رو نسبت به آفر باشگاه‌پرسپولیس‌بدهد. ظرف 48 ساعت آینده تکلیف فوق ستاره فوتبال ایران مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/26942" target="_blank">📅 15:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26941">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1f8c0281.mp4?token=qLWzZbkSKUdw4yo-IQv72wWYvFIf-v1kVnmOyKtWpmryMRb1iT-jRSUMHiSAvmd-LXh4969sJYoHL_aILbdYwgJrknai-DL7eiYB-P2CfvZnrOooOZPtl2ciBzKytibs9Bkj-K2LOo3T0UtG51b7c_QSDk8MmlXzaAwBAo9E6POl29MkRt6mrnabQyuRi_vtWUb-cMgfC9FYEsNwV7uzJuMot4yxZ6G_YlK0xXB4aFp0i5bY4Lwt2fnbIgjswxyaOm2H8yhAvcqMj0c1Vji2pFKe8M-iQj4rKRbHKtTLtz4lXkgqKO4pcwFL8afsn1FsLSvB30xkcmClACIwDkwU1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1f8c0281.mp4?token=qLWzZbkSKUdw4yo-IQv72wWYvFIf-v1kVnmOyKtWpmryMRb1iT-jRSUMHiSAvmd-LXh4969sJYoHL_aILbdYwgJrknai-DL7eiYB-P2CfvZnrOooOZPtl2ciBzKytibs9Bkj-K2LOo3T0UtG51b7c_QSDk8MmlXzaAwBAo9E6POl29MkRt6mrnabQyuRi_vtWUb-cMgfC9FYEsNwV7uzJuMot4yxZ6G_YlK0xXB4aFp0i5bY4Lwt2fnbIgjswxyaOm2H8yhAvcqMj0c1Vji2pFKe8M-iQj4rKRbHKtTLtz4lXkgqKO4pcwFL8afsn1FsLSvB30xkcmClACIwDkwU1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپ بسیار سمی که صداسینا پخش کرد اینقدر سطح ریدمان بالا بود که از آرشیوم حذفش کردند.
🔴
از سر راه کنار برید ایرانیا رسیدن...
🔴
علی بیرو توی دروازه یا که نیازمند
🔴
کنارش شجاع و کنعانی میشن پدافند
🔴
تنگه ی هرمز ما تو دستای سعیده
🔴
شوتای قدوس و رامین مثل خیبر شکن…</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/26941" target="_blank">📅 15:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26939">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g5Kye87fZZaI48VlwD6ZHR2zbbQjH0rOZCI4xs549sG7AkwhnHMj7eJcaMOaKruKheYo2VZj_kRIi0SWRTCBFoVbxWEuihDoi7EFHF1TfLfOEuz0iV1781NgptsqYu9eu2jyZL1RNEbTtG9-SBEj007ZzTa-EG3eTGCEHB4nMpR4uKbsYeq4VNYOR_NzHS7GX2On6kg_Sz7_5LvOa4E3WWsWbsOfhFMKKovXFVnqimJRAJudMEq8AO48jRGH-AyB7-9GD1x5nGUenZCYXoRXdNzshYouvX2B4PEN-vdRXeXaY3PGtQWdLK_odKygrtcpQ87b59SFsyezBo7AHfDsZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kojPwKPGswjunlkauR1LyJpQSHY859fod9vDP5utZPb4jsSGEGdPSEf0ylJuFIqkXzet87s17JbV0_vNGzl6beWAkrMYFsaqJf6fXx6hfHhurnBTxxK7Fh1WYJiJWHaEU_eWg6-uV_t2wyh6pwi8K-E2DEUUNqVcrge3CKUBzpOY5b03plUYUg6fO7QXz9pOY1Vx03pBdvtXovTWQxQPGux1fh4ema3x5uvosmUugoE7vkX5vY2p938CkKuDKmFikpvELhFdPJ4Nxb-uaMBYd78aaLHbAStHIUjgBdKiffPnst6tCts1oDETLxzY8W0NQkuwaQRmY_n-iiaKmjSpww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
افزایش 12 سانتی متری قد لامین یامال ستاره جوان تیم ملی اسپانیا و باشگاه بارسلونا در 3 سال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/26939" target="_blank">📅 14:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26938">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5mbmXMmvWGHxKi0E1RKzwlktpyCZUVOnHytEF4ToBD3jHUsi-IjCnKvYz3Pi5ysD4xruDieD29fTXKIwKGyJ-NKWBkn9nFtWXGvBs7XchA8alvlV_GihrON545R229R4H8otF7zxBCIt11HakJeXRo-r-D1VgD3m9_GfGufuir81VyZfsAQ7mlY98T8kLkSTtEiQdu0dE5UzjAX15cAy3t1ZyEx_3TRGp-oC4R0xwS5JTzUbulArT8AD2KD94kWuR-MLHg0kS8lFMOnVBqu3xrji4g-XXAxoDMZzWh-Hrr7nn1AYwA_783fW79YALlmLcmmMfFOA4CnizlmU6ReGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
پست معنادار و تامل‌برانگیز رسانه رسمی باشگاه خیبر خرم آباد با استفاده از اعداد تاریخی 18 و 19
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26938" target="_blank">📅 14:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26937">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cdcb5398e.mp4?token=m0wOZXNkusOQ06wI-mqHhdXgqx68Q70Mi_Yf-7ugZXsUbybJWfxyTcWE9hi98D3HkFoYu_KByvMdBb6KxIsSe1T9l2cl8vbOxQ4w-RgNtURB8J_D26ZwM_gVvah_q9HYyzudWcevJqxAf0OVavzr-eJe30LIPVI1Otgla4bjltyuvpckl5SvL_muw7qSBpQIY3YLZk2omByFMHorY859BQTfj-eunK4NjxegF1VFGCbboboVzAvQYdHr8C6BbTCqNzlyBV3zqs6OHNwQG5aINYtx4KPWfqW3pnmBFrZKTyyl9UOckstyrU_krjq07QOsg-BenmqPg_txL0gS8kkozg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cdcb5398e.mp4?token=m0wOZXNkusOQ06wI-mqHhdXgqx68Q70Mi_Yf-7ugZXsUbybJWfxyTcWE9hi98D3HkFoYu_KByvMdBb6KxIsSe1T9l2cl8vbOxQ4w-RgNtURB8J_D26ZwM_gVvah_q9HYyzudWcevJqxAf0OVavzr-eJe30LIPVI1Otgla4bjltyuvpckl5SvL_muw7qSBpQIY3YLZk2omByFMHorY859BQTfj-eunK4NjxegF1VFGCbboboVzAvQYdHr8C6BbTCqNzlyBV3zqs6OHNwQG5aINYtx4KPWfqW3pnmBFrZKTyyl9UOckstyrU_krjq07QOsg-BenmqPg_txL0gS8kkozg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خیلیامیپرسن‌دارایی محمدرضا زنوزی چقدره که هرچی خرج میکنه تموم نمیشه. این ویدیو رو ببینید متوجه میشید. امکان کز خوردن پشماتونم هست.
‼️
طبق‌گفته‌خطیبی؛ زنوزی قبل از تراکتور خواسته بود استقلال رو بخره که سلطانی‌فر بهش نداده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26937" target="_blank">📅 14:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26936">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eezm3_wEa5GiZ-Uosk4dh8Ymk-tN4y2sAOhlVpe6Kyo6hs-byj9DyeFjPA8CeW9lqbC1emk2W0uTktiox5AQlvQgPj0kpB4O9_9g5O24tVB51pDFRrZP9NukewHzQk-DmCC4eEcRAtfKIMOpFq2CYATvwkPVslz9s_6p2bUtZrLJf3kQZFFJpdsyA3iWK9C9g1-ngfzFUhSstI8VuBCWAy03qJTDWHmcbewgUOsYxvPy5jvVyBN0aXxK-LvAvyOt9z3yr4Gd0rkEkTq8-damWQghTI82eBEAUxBWijb9udrc1FLcIeKeZB_QxYM35maLnnHIT9FGFbVu381DiL2Gyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی تارتار سرمربی تیم پرسپولیس درجدید ترین اقدام خود تیوی بیفوما و دنیل گرا رو درلیست مازاد سرخوشان قرار داده است و این دو بازیکن نیز بزودی از جمع سرخ‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26936" target="_blank">📅 13:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26935">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYgq0drOC_FPZJudLX6tn36gsb5_-G0t5uCaog-BbzngD2_XI2Nwm7m-LaHhe8B4B7vKZCZjVWWkaW_4IRH-4VQy6rzSuusccKx_3DH_3ExHCUChiLHQ3nYb_Pm3ARAEsNTB6TWNbKJnh98jqv1wc4GX0IB42-bhc_xbRh6P-poe0TNb_qh2u0lEvGEa4VV_0A5XOHcbbiJBo92oMrIY4ZvOvqYzEJlTFAFTVOIfi1_9MASysw4oM2M7Yx-lGLq1CHxLRJ5kRJcjFjST05GxTmvQLyTkAebQRiWpe7jhsKmATvc9B5202tLnh3uV44_1aEhlGL0CRD8rX2eeprxWQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ ماخاچ‌قلعه دو روز به جواد حسین نژاد فرصت داده‌ که‌پاسخ‌نهایی خود رو نسبت به آفر باشگاه‌پرسپولیس‌بدهد. ظرف 48 ساعت آینده تکلیف فوق ستاره فوتبال ایران مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26935" target="_blank">📅 13:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26934">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0a57Uya4TlkNos1NqnnG8B4RzA68Wy-hYRMk68jgtwVhd-2ggs9CN7EKBC41UbDrKVsHK_hkeW6SF82lc6MFzM0V91Gd3QXdV8ljhMaMfz1tuXrMfl19UQe_GObNzxR6ZmG_CAhp6DkcwO34e102bBkjvSHmdyXne2SBeJ-mxJQtmXSChDNuPhUnVKpaVyLk2ZszdXPFyZqX8ROVRWEf6BKHslaEo0vtopoi8oHXE1HfZDZvxnZMuCIf4A7uTUwiENnhl_1XmaeRdr8R8kQwPNE7gnOeQOoe-70KRDcJkFa-UlMWUNMe61__EgOQR4OgyR1b4VHdMg24_tZLllmYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی‌پرشیانا #فوری؛ تلاش پرسپولیس برای سرخپوش‌کردن‌فوق‌ستاره‌ایرانی ماخاچ قلعه‌.
🔴
طبق اخبار دریافتی پرشیانا؛ مدیریت پرسپولیس ساعتی‌قبل‌باارسال‌ایمیلی‌رسمی به باشگاه‌ماخاچ قلعه آمادگی خود را برای پرداخت رضایت نامه دو میلیون یورویی محمد جواد حسین نژاد…</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/persiana_Soccer/26934" target="_blank">📅 13:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26933">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5gxYw8DFPf-pLB3RwsV6zCQB6qLhgEKgAbmcGjg_go-7jW6SFs7qZf7T0_spHQci6UvEY5VlfOxwB_yzOCAoTcBVAMQf7wl8MbDoInOcuM4tN2VzgnyED2_OaHZ1wDBpqzNHca5feUi2ACw_qal2lC8LTVvvuDfNkw5EWf_Ira7jTWllFrjn9mv30eXvUBXCHaW-fwPEsSJVLp1DAOrkPPwNtN9N4eJje8TpZlXTSIN4jtZ4ge7GvgYsKPliT0J7wd5dZvqgVrdCQ5Srb4kS6mSZ6kXu1FnD6V_dFTEJhbjXFKhU2JAMv3FCTk3Sm2yuKRJgTd2-taARYN69mbRkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی‌پرشیانا #فوری؛ تلاش پرسپولیس برای سرخپوش‌کردن‌فوق‌ستاره‌ایرانی ماخاچ قلعه‌.
🔴
طبق اخبار دریافتی پرشیانا؛ مدیریت پرسپولیس ساعتی‌قبل‌باارسال‌ایمیلی‌رسمی به باشگاه‌ماخاچ قلعه آمادگی خود را برای پرداخت رضایت نامه دو میلیون یورویی محمد جواد حسین نژاد…</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/persiana_Soccer/26933" target="_blank">📅 13:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26932">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rq_nTPtigzcTF_Bi5BBoJmb5YAxWL2oxitJmcvbO8uKOnqkj_ArYicPox6wdmeOVOkq2c3SUXZw4uEPqgG5wD8kMF8KWCz9P7pUa3Hin9wxSkig12D0oHSoWPq_a_M1NRENgS4INfMWRrLmKQM2U-XX7i3bheztSHv1j6v2XK8sQ58xQync4GDYBicYcWIGTqg5TDgV6YB_NezUXgcWX0ladpoFoi4U5jofXriB2ApMtHSqSuSrnSMBFh7-5XNG2oIFEI2qFNDBjUE-2pYWgnMgdb7eAacULc7AjcD9AXlzXaxcw3fnQaVgimHZlPqT0DiZnJ34EFY2y57TNJjmJOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره 22 ساله تیم ماخاچ قلعه روسیه پیشنهاد تراکتور رو در رورهای اخیر رد کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/persiana_Soccer/26932" target="_blank">📅 12:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26931">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcHQeIfzsaOA4DvJ5B1u4jFbcBzezLahXc8BsAImFHIvbFufNN1A7fMEqMXb5lz14P8nEm7p9yxvLza96DKegLhncBIEzxmPETNj16A_n6eO9b_NcximpyDl7du659B2-WmjJZdoqWCQ7WeWox9Er_ymy4MzAZeeh4b2QiQQHRBYQLhKJ2V7Ro6bICBVwHJWJkljY67znirQd3rd-KXA407uunrYogSU4i7mixxHvuLx4N5iu2Iwy40qA3hTUXM-UKlBZbWG7O6s23S97pyUE2BSnOJwOdVw0LAC2mcMp5ND5hc2NamA2YdYvPHxUgS7mdMzsZO-M5JcZ6TN9cbghA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
نشریهESPN:فلورنتینو پرز قصدداره درآمد باشگاه رئال مادرید در این پنجره رو به 400 میلیون یورو برسونه. تا حالا 200 میلیون یورو بابت فروش بازیکنان‌آکادمی درآمد داشته و به‌سران آرسنال گفته اگه‌وینیسیوس‌جونیور رو میخوایدباید 200 میلیون یورو هزینه کنید. اگه توپچی…</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/persiana_Soccer/26931" target="_blank">📅 12:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26929">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cupPuKfqFkJNNGTPDruIv9JkNCa3Plg199XF9_ukvZVsHsR94p8Uwra-p_j8j81RCDhdQi3G46BnUvzeLJ8wUojBmwTiVdS618XuvnATy0MY6FBkPqbv4M9CbLO5kUlQwmMPkhZOfnKpqDnvz4GNuO2y-2tzKnRBS9nIkSR91YgbB-MGImq6L3XyHSg-77B3URjyR_4kx1fBtMp_vUqcBKweDuUmTXYTmn41vg9MpBbLS_emG-tAyftiT9geEICwCjafmV7ycChuqYpsKNyaj1wONLzUbjOvQXej-1WgU-AdcuFx-Y2TT8D3iULPyV7AyK8bvgBG84alKzqZdMwMKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UFcKyEByPvrUGAXrqyA-f2Hhg9dFyC8lVTVv2Sv9UbJ3JgnFaTooHZdRkjLI6d5zRabv0AP0HAUQJydoaUdfb7ztBXBAabPgsC8bOVy-Uqi4osxsEHXmGNQmiW8DGML3Mf87Ms2UjTzheDbIyTaFpdxI1MraYw-K1iwCaWLHXAcnEigId1aqFLq2eJbZNDvJaoW3ReBLKu67UNNO8rg2RU_Q_AE-fhCQw5s2pl8M81HIHXKwZ_ySrG_L8BslKD3G0GrQk0GfAGrR2Xm3WVejjn4aVVP7FosxAfQa0vLDsCnZ4so_Ts0xhSBucb9f06nqmoGxKlfW6wGcmdt1o_edGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لیست کامل ورودی‌وخروجی‌های دو تیم رئال مادرید و بارسلونا دراین پنجره تا به امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26929" target="_blank">📅 12:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26928">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0eEmL5r0qCN8Ne4WHQGj8utcTq19IyqEJqUX4E5pxcC4dqh7bOGGdHkd_4nGTlf9JVq9W2QjBDT-AknBtn7Wrs7TKSgKbxGSulXvh26X9oHbw_X60q_8yC04oK_PA-PM8NOjQypyluTYCQ9m2GOWEbMyLYgAkYCA0egTmx1Jh-Dh12S4wrgNrFcGBUAevT1A9DhNGgGk-6bGA2Eti7JlBHZWwEagEiwbqaavKqNNtuFAH4Uslu5JVyDvqtlwdRY25JdleSMi7eLnmJmD_GpD80MVFY_ZRxUlRFoTmbSMMeCso-uOkWsm3CiUQjAS_VnR9kLfiHanpfH_LVEbfPLxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
در فاصله دو هفته تا شروع لیگ برتر؛ مهران احمدی هافبک‌تهاجمی‌استقلال دربازی دوستانه امروز آبی‌ها مقابل فولاد از ناحیه کشاله ران مصدوم شد و ممکن است دو الی چهار هفته دور از میادین باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26928" target="_blank">📅 11:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26927">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">📹
هایلایتی از عملکرد خیره کننده فابیو آبرئو مهاجم 33 ساله انگولایی مدنطر استقلال در سال 2025.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26927" target="_blank">📅 11:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26926">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuHov7D0WEAGWpEhUiPyoNp6zInXC03SapYCuZs_1aZlgK5WN-sasRle8bVZkXdI9XS4drR8Q-vSsSJfJJVsPjfBAWTsoSYPPfUhYMnL0Mt-q7K1iWkY8NNIoFOmuXiXFTmGLtSWGg8FYZ9IenaX2UTSVRSIvSi8WaEEGvG-DIrhrbzG866GSBLfqL7d4ZaSekp0dsmJ8H0pLaFhKX0CfZ75AJXqiFzGNV77hZIRcui_v_Q8YEq9x2wRiOacSpYVC082emngI3-xq5MaWZHjWpoSO080_1O5FwMOGl2xtPuN8vJWSUaCUVNHx1KHarySO0XSmvrR7Uw36Osv1DbWHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
زندگی رو لامین یامال 19 ساله میکنه که تو این‌سن جام جهانی برده، تو تیم بارسلونا بازی میکنه، حقوق بالا داره و صبح تا شب با دوست دخترشه نه جوون بدبخت ایرانی که از بعد هجده سالگی باید به فکر سربازی و کار و قسط و کوفت و زهرمار باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26926" target="_blank">📅 11:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26925">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIeqjoGiiFEnmJWtXrp0KbBmMTGNcClGTzlvKskxvERDEaaF37u-q-4kBYTy9IZkWl-06YMM5CcCi-pKll2F4w-aFcrjt1DIj3B13oJEdOcaL4yZp3i9gQFfbevjbHK-VgU0w4D2Ls7i16tUyxrevz1dRUAmrw6IklfTO1L5g7k4arr4zQjpUcz2Clj7BdfjNIoumHQIzZIupkPIlYuY-2bxPm8LeSYzUvdKf77ghmitd2t0KYEwc4aWbQuGFTnGGn07dGzLnlejdH3H2xCB0LogqZRjwHGubLGqN16KtGM6E7xJIoMcGya-XqsTnZ-Fzc5If64bz0pwntVZZ2tQ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔹
👤
طبق‌شنیده‌های رسانه پرشیانا؛
با دستور مسعود پزشکیان؛ مجوزفعالیت فرهاد مجیدی در لیگ برتر صادر شده و حالا به‌خودِ مجیدی بستگی دارد به رقابت‌های لیگ‌برتر فوتبال ایران بازگردد یا که خیر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26925" target="_blank">📅 11:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26924">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEvWIc3lWZkVj49QDVIn1MxBHbtamWfaRWsFQdOrm4Pt86HKhkaOOkCgb_Llf5LLqDWpsN9ohJcI1hvialhFoaU7xELB2RLB3NOspS1MccV6OW1pjqAamjcPaI7EG8wBEmia2eBS9F_Ec4R7tsv9oQhb8ISl8dRmZCNN7rcrO1RCSfMwAshR1sC0yG3XDKZtGl8klud8_cr1XcTJVGrDeuy26fdvI26mihQiTaZyEMpAHCkwS4USHmOS0eXKskv05HgGsxOcSgoyuWisR3zNVksNEmpfSZ2I-Yom9UUvr5ZVrqy_q5KEQE_OyoET2ILJ2NDLLc41N7y-bIVKNRiKqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26924" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26923">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99893fb77f.mp4?token=P0j4PAXLECrNwg1spxznVecbK4h-eAaVPevB-9iti-atFAUP7dehXMd1W9kDWmMB0Yos5FE-lbKFmdV879CFAcCAW11Qiji-BJCa5EB-MA_Xq6mm0cdm8FVOdLCKfM13y_JRV1rhOTGxjFdwCz2WDJikyHhONxodyvZasHJdRKPy5_jxJFb3hou3HM7vACel34juJpzrmVRqxKV8MMp_OG9fGCQQ5Gd4RLSWonJfcls4XRHoWMVyV86lnqfaEsSjIqVPhgCAt049u2ICb9d5AzQ6HwF3Z82rENTu5_Lz69_FKjs3n_3zgqIToWbHH9fsSGoC2GNKaJxeWm9h8OhRB05TqVfC_Au7z2uzprRfIrZiGmt2MCXSOAgO9Q0Ll0y8gbttKH3bjY0qRfKTDI167O_qZbH9o55pSeNhr_Z16mrAEwO0KfAEeSZlyj7k7wTmFvPKq_E9XDl1CTYhJhExebbPzqvBTRgpAQSmFtyRBkJUO0HpVvOSUHsFPIRbk9KfJhOl_qqL5_AqfoJ3F6IE-vS6uGT5Q1H6f0ma66cU_JqpCkMlMWKLwwA_jE9A3XyGa0Hr1gJyPQ62DC8dISqD9WXnswmMB3pZAA9KE_Dr3SciBkJuvITCUgRFPBg4pvuNmH22wTAD7InRM9dIIar-lDL3Wc_H7DzXkgZdTXVdWFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99893fb77f.mp4?token=P0j4PAXLECrNwg1spxznVecbK4h-eAaVPevB-9iti-atFAUP7dehXMd1W9kDWmMB0Yos5FE-lbKFmdV879CFAcCAW11Qiji-BJCa5EB-MA_Xq6mm0cdm8FVOdLCKfM13y_JRV1rhOTGxjFdwCz2WDJikyHhONxodyvZasHJdRKPy5_jxJFb3hou3HM7vACel34juJpzrmVRqxKV8MMp_OG9fGCQQ5Gd4RLSWonJfcls4XRHoWMVyV86lnqfaEsSjIqVPhgCAt049u2ICb9d5AzQ6HwF3Z82rENTu5_Lz69_FKjs3n_3zgqIToWbHH9fsSGoC2GNKaJxeWm9h8OhRB05TqVfC_Au7z2uzprRfIrZiGmt2MCXSOAgO9Q0Ll0y8gbttKH3bjY0qRfKTDI167O_qZbH9o55pSeNhr_Z16mrAEwO0KfAEeSZlyj7k7wTmFvPKq_E9XDl1CTYhJhExebbPzqvBTRgpAQSmFtyRBkJUO0HpVvOSUHsFPIRbk9KfJhOl_qqL5_AqfoJ3F6IE-vS6uGT5Q1H6f0ma66cU_JqpCkMlMWKLwwA_jE9A3XyGa0Hr1gJyPQ62DC8dISqD9WXnswmMB3pZAA9KE_Dr3SciBkJuvITCUgRFPBg4pvuNmH22wTAD7InRM9dIIar-lDL3Wc_H7DzXkgZdTXVdWFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
چند تا از شوت های روبرتو کارلوس رو ببینید، زمانی که فوتبال از کسب و کار و پول دور بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/26923" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26922">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ja3SMauFUpFAw7hPyiHz2Cpmu9H4dCvmsxnea7-GRCFnw3oGxKmfk8XJVP5ckWuY4wk3_d4iSsTq5miEZDbew3IrGOp6FH0nZe34ezQOf7JmwWcU_oGLd8elgSWrEivjbY4shLSU20nY1ZrFs4iqKWOOSyTzKIzCRMSxx4KdkuiMBOMTtouYE2f62I-aWgmQ3GuHrWcr-DUhzxM9jjujDt6B9YlBKXjnEVDgQYvLmzVNF69EJq9zQeMh2VfuaBFXrC1BvyNb1phJ1JS2OGGqLZghkZM77Ugiw0WVMKaBIf1y7FjbWq_esvnSdkjcrZY048Nlbg2obprneAlCwm-smQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
🎰
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26922" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26921">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EM1dyE_y1egN25fxHERYoeDPy0Us2WUEFvcGY3gnd1Ly0DW7UjDUgZ2p10YxlrbuX7VJ3Og_MeB3XQzABApnvKGX5U7C5P7Ouku-FNgWf9SAc-ACrSq4Ssxsxg574SPlFweWGzpdiL5gm9c8VjHyGXagJbAb6OGkKjMnsleQplwVXqk5js755QEk6QyEcIoz4e0sls60AkYZFU805EeOcmnU5P9j_OtWxeRwnnMozRVxaNeLP65FIUkXwY2Sohp2C2zS7jtDk5YR66jwaTK7At_3M1Cvsl7fPIzrdjdkgQzOmKOpBtuaowNYXGsFZT9blcFHkei-YQu7SK--63inlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
ماتیس یایسله سرمربی 38 ساله الاهلی‌که فصل گذشته این‌تیم به‌دومین قهرمانی آسیایی خود رساند باعقد قراردادی چهار ساله به تیم نیوکاسل پیوست.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26921" target="_blank">📅 10:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26920">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_Zpg8pOV5TqamFwASssBaZddOD6FZi6KzghcTclNIPPCm4NTA8Xbpr_x_Qi25Q5j1nypx9MNrI1GXKTfhqJ7bP_aUdZIrA5w34kh6wH0YWOh-82NuT35RL3AUU-41WO6c9AYPGIL0HJvDaizCu7QBweOT-PlpkkBh3XWV92xr0ItDiA846nkOMjbh1dwDV_0l7CRWICI59f2wzlkeTSU7Sm8p9yHyYU1EOkfsmsi-eGmVCRDjdSne5Nugde9ccScmtg84JJ7TznB0K2lXg3olyJ7lXLlGunEw_eiQyqAJF-6iqIlyfgNuHAbN5vJ9S8r4nhyIFwg6khFAhjTYZ4RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26920" target="_blank">📅 09:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26918">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3px4QhoCn0NQgV0lL113tmyxG8A5PidvKfcyiRUTsPg9rfOQclGEfmRKk82S5gsNzfqv54eeEpez5IeeByRGQP6A18EeTiA9POXeXEv4MW9suqPoK4tQpi-rZceT5_qRv0AbBRelyEE5JMAl879Wh3HWKld3TVez9LWZTxhy3mGsVKIrxJpjXhEpA4yaNkBS9LTZ1KPgP-So-lRL_49omyfdac-fgROH09zKI7kPyohm66vDAzs1eYx46e3ZeDi8MpT-FmhlxI2LLIMLXQlmcNX2bRkufyHE560xuA6WKr_P4yKu7MHtho4ktGgBuP_UbDBeOT7ollGiq4SC0lGMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇷
👤
رسانه‌های‌یونانی: تصمیم‌باشگاه المپیاکوس برای فروش مهدی طارمی قطعیه. سران المپیاکوس برای فروش مهاجم 34 ساله خود رقمی بین 1 الی 1.5 میلیون یورو تقاضا خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/26918" target="_blank">📅 09:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26917">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrOCSKCUq5AwRswTPzHaLW9TfISO1e1JekS3JLEnLUqFYaqlNKnU3qrTCV3Mky9wCHWCBUI-j4cdO2RzJ127XvrTvsiT27wiFBOdpAu-iDn0oJ8OgrXPk-c69MsILzBL0Ax5uqQcW4YJo2HODary93lEoxI0g0EjhOWG1sRW6DvCplpTRt7QvDhPYu7ObtxWlLAq6b4Cc0957Z3rZ9P29evclREt_BaGiT8tKcWVjwM0qLP0jD2p2cu13z1o3IfMFsjQ1zgTp73hN4OebmM7stE6MxS_rQ87QDc1XZ-IdKOuj0Ep3mxwOVAhV4U0FI-lXPblaxvIEwxUdLdU2beLaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شامیل گازیزوف مدیرعامل‌باشگاه دینامو ماخاچ‌ قلعه در گفت‌وگو با RB Sport: سه پیشنهاد خارجی برای حسین نژاد به‌دست ما رسیده اما ارقام پیشنهاد شده کمتر از رقم مدنظر باشگاه ماست. سیاست تیم ماخاچ قلعه فروش این‌ستاره‌جوان با بالاترین رقمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26917" target="_blank">📅 01:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26915">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZy_KKv8_xTw48R1cIjrXtzEuP-D4lX7UttWyPh25-FpSyLCJCOwK4d0as905NQ2_ZQNAHqOgmTuhv7cLcn_Hf5gsXtEDHPqrH_JRzTiZCeqTneWw6h0c58vJzBHo9a7tT7kJWz4zCRaqWNoWyWCYuWt6vdx0GN2_tYcmEVbNGeXxXuuQssYGTxsInyR3eBjgqtAEPM9l6bfUMPWm6_O_8-phGjVjWVHDGCz0uYlG4nuh1YcF-w6RwjvsrB5-lOPFjm94tdT-o2f44RnSjULqB2iDs0JvarXocHVQCNGWFzu7AEv2FagWt8KZq5-cts7R332pPWcyqxYcXqTbJVOIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛
از مصاف شاگردان ژابی با تاتنهام در استرالیا تا بازی رئال مادرید برابر فیورنتینا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26915" target="_blank">📅 01:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26914">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzqIoAI6tyQboPiUED7uksTaKPagHrKbkP0ky3Of4lmlNQCx1yXGE1cev9cb40Zp0fw_Nqqwe8rarPw-uUbSnrozhyZ4lm6yTyVYofveOZFvkFyvNH5VhYHUKImdP0z9C_QXYkMSZpuUJtZvHB-9fswmS8FmUFruilCWay6VQi9iuJDSGOcgjK910BsPEjzf_CbamEqIj-puHGGqQvw5J08iNzSHRGt0O2IL-DnlYhgspiO-pvQVWkaO7ohftQ8-OvhYmBggJTY3QAyrAmPoCpmpv0WV8rejI3gvO4QFd52KFZ5HsNiI7izsJ-f0xk3iARxEa-l-T1ypXIt1THAFeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
بردشاگردان اسپالتی مقابل تیم فرانسوی و شکست کاتالان‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26914" target="_blank">📅 01:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26913">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucd-goZn5RzXxjI0NNznZHLTTcwaHqaAkNmnlVmVLASUZ5ODX1TVB9w8HITFOgpzPnm90Sob96fnC2U1hTu413-rm8kPwuuPn4ZORMjPr6_P8Pmo2uMJGiJpyrY5kJhLgBHma-zllwgyJU0CbGEpnn-ouqQXx1fEH8rsxAJQk4XTNZT9fxX1YVflm3ykKd9tvNhlQ0CEUVcT5soxxofE-Dq2sR7JHvR0FF1jWcuAu3jr4GlDi5PjWBay8etjOskIzLWvwKMLaE8Cd-1FOeBHI7K0X4_KZh96LZHibSUDK4N3haM68GueZgORGOarx27Iwe6s_jP-Q_LmvlLngx3CLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه آمریکا و اسرائیل در حال برنامه‌ریزی برای اجرای یکی از شدیدترین حملات هوایی تاکنون علیه زیر ساخت‌ های بخش انرژی ایران هستند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26913" target="_blank">📅 01:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26912">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NouTR0r7ByTgxyBm-WcwnOhMC0YCwXAfSLYYckEGuJohr9W4pGdOPnM9xL3VIvbw3q6gGrozAt3c_0JlOnpDmA_4FxQsyAcaZw7wRjmzQ7zAcoqB6DVn0TmoWowANmFyIE-D97RqsADK_HiKEZz139Wsx5A6mJc5ydSrK9GQ4eBa2LO5wmh_TRvGXzOmPh33dQKi_5stvnnvj_BjBicOrXomY2hItjmMtzD5c6Cn1FiS8tL9jnyR3gQ0cpaeiSbDbko7Z0mLTRI9KOFc8EiqyVZycFuKIRosdTKCXxxOkX-Yg7vdsXB3HOeeI4NaEqA6jR4xfF-abR7CMRggJPPLXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
رسانه‌های مراکشی: منیر الحدادی ستاره سابق بارسلونا پیشنهاد باشگاه الاتحاد طنجه مراکش رو به دلیل پایین‌ بودن رقم‌‌قرارداد رد کرد. باشگاه استقلال به‌منیر گفته‌برگرد سالی 1.5 میلیون دلار بهت میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26912" target="_blank">📅 00:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26911">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJ289LDBcVYwlRrHWE6AId7dZ8G21U2BRfPCl1I4FXi_NtFNTmMuaDu5I684qsMudleH21uZjGh0MZ7QqlTPhdneKf-iddRBYnoYXMCwJ5cEEooV4oPAQOKeWv9y6to-W3eBjNLaKFT6NqNVh-6tDUn8tLuT0_tHPMCinph0ZhmouTgDjWsf5sBjr0Myf9s--QQ9HGkq5mn2mz4YaUvHcUq4lafdzYWDFnkhhTomqdDP9f4XoVvCMTyE_VsIlrgZVrGUdikvn6AlKEGlVWM_yR-hSH05MB9teB_sNiRZylVjr2xON2zSA8M4X_8PpERR1ct0UXXNG7OhJJxa0EEOMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛رئال‌مادرید بابت‌فروش‌بازیکنان آکادمیش درشش‌فصل‌اخیر 440 میلیون‌یورو درآمد داشته. تو همین پنجره هم 196 میلیون یورو درآمد داشته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26911" target="_blank">📅 00:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26910">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDx_Zpevxb_8Bv0V4ASR_ZzADf-5v7GdRZ_2QBvjecruRdkjsJ2onDDxyIleT5IdYGwnZVaJVed6OuBcIRJavyqXY8OhI3T3ceJbHStY7klYU4MflKRzBLSzpJiOhyxXFOGtb28Wl7zVuepbbb6YBR47k1j4m-E4Y3XGmwfoOZ0BuNd0Yi-pSJqTQ1iQgph4VT2EX4LtEmljaQuSOX8KBGDSCNg6GYktmVLrZuTigVQDCgthW6QdlWbjjQEPVf-9K027_mkZqluTu_l0nyeGT6lvNjkFQII-MoDB5pQSFgnvmahJIKyzHqyaSkGTFTAhooPeHr26GXYGRWvvssbDxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه فلیکس دیاز: با درخشش در این دوره جام جهانی؛ فلورنتینو پرز تصمیمش برای جذب انزو فرناندز ستاره خط‌هافبک تیم آرژانتین قطعی شده و قصد داره انزو و اولیسه رو باهم جذب کنه. انزو به سران چلسی گفته نمیخواد در این تیم بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26910" target="_blank">📅 00:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26909">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEUuvoJ1Fdup5--MeaLoqZaYzxQJc0Bpyz5wc3Duu4tc0RUJDIF8KLRxmiRpJnIKpXXf3G-futK7cRyaHYh0V1LTmdMtxOeZzMZiIIVkUXjTmKJHLr85UR6H8cNoKGe_vGzQxS4sDQC-A5769yODlKpnTPVL1DC3gb6mM6B2GkO42mrOpb88MqHVlJdcVIKWsxdS63aYYbR9obcEdNpaGzsejdnzVcXN1XtQRKxolSkv9w3gOw_ffpllJY15R3snmyRZO3BiKCxPkxZb01YT-_P6xwQ5YlWg4knnvKcqqiPzLxCPAJi_V6JAb66SVVRXp2PxHBzCuLZj6StF5K16MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد..بااعلام‌مدیربرنامه‌های مرتضی پورعلی گنجی، امیدعالیشاه و میلادسرلک در ترانسفرمارکت؛ این 3 بازیکن رسما از باشگاه پرسپولیس جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26909" target="_blank">📅 23:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26908">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0s1tkeCDAbK-m2UnwkwVzlKGraclPm2xmy4XQ_AWF4eLP_U_YIXCvk0MFt5L1tyEymkDXiNXrqwb0khXrW2697V9QBCIXzK_dex0t4xEhmTgvPXmBjNeNkwqXVHgmJEIpLoxURi9Y52w9KMcEot0q2jHzk79CxFW0aFi6OnjLwBsdUu44rtCBLw65lax0g8E0suzPqRuFsHhQniS5ovHPUqwzDdJigRf9TOKyDv1NGyemjbSE3Y0AJm2vznErOO666otUjUukfINTLcanHMjcRz-QQn5-5d8toZ0BtWWoPMiCeTmjphDtrKPPpg_ZjGYoHmlc_4l5PszH5Izocdpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26908" target="_blank">📅 23:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26907">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTTFL_qMPsGH_SYzaC0-CCveInn5_VYZep-FG0qMQ6nRLpKXCu8y80KTpP0TIuTsxW3virwf1o6uAnOeZPzoID4RhlJk8t6RUWzGC7C4jChNKGdYH_56oUIhJdSCm3BoNzvPeuykLKdgHuuhWoFyX1bq8JoECmEwszdT76t3aYDdk55ff3C2v2Q4avnVN6XQIOi6nnk9tbaL1pUDbPyxVjJoHN1ibup3RGgwJXQCNWVqPEfoGLWs8IE2E-tC5pbIFfZtNpxhOFCg0y0t01qgVTTcOR4QdRV5skaIroKbkOT-2qT57I5z9PenR-5ob6ZEqNuFlmt-fHE6q5qhGOqAig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26907" target="_blank">📅 23:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26906">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇪🇸
خب گویا سرخیو راموس اسطوره رئال مادرید هم‌تحت‌تاثیراستوری‌های‌رامین‌رضاییان قرار گرفته و دویدن تو خیابان‌های شهر مادرید رو شروع کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26906" target="_blank">📅 22:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26904">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzaSgXURvHXPryyZOZiUtuAY3kL48yxZXGxVCOubklz1IaQTD9Pg-C_wQkv6sTlBVbyOm7k2mRmPJQI3fwdtBrlNIxDDYBPJuDRIivn5MSqeJlyOENbEiQDuQWVhMl1scE9aYzKxLIxyiPBiqS1DQu6TVY7w4bFLMAdRDZU3U_F_VHVSyl3v7zv_KHTkKFRqvUIgpmd8XYhukL6KxhbZQccavrJ3iK4qlY8j6E9zKigfYGIXa3hYyJxuWNUY166GQBp9qPqvxAhCckLdPXMpYOodbxN3Iibl6dxCKF663lxlMGbxmO9iBM2MVN_rHCKEXBJ5WgbsV5APJ0FynSEF8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26904" target="_blank">📅 22:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26903">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eO00DuBbVGSHOxHJdYEESgN2jtrPIGz19NyKAABFyqrpoPjS46IEj_Lb7thEicEKcKTTly8Iy-PWvaMtE72VRzQ_vvIbSH9FX9nLiDrZK3PHRQT7DcAX9jUL7f_8pMVomDo7ZrFQA3AQQhYZ49vumj5mZws3agC0OdTIDueH3dDuEOXLM9iUFHz-uivNd-5r72RPE9xL4oq8gvdkkxeAUUBhO37yLC1k1iEg46H-OWlAM4MikBSQ75PIq_I15S52FF1pgYcBV-vO3SmS5GvRW8YfPxjW33fUKTfrVhP4WJtzqZ3QPXAghkavCub1A4HXcReXMdj9K6S4Y7UtbnjQNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
شش‌خرید قطعی تیم رئال مادرید در نقل و اتتقالات تابستونی؛ به این لیست رودری و الساندرو باستونی هم اضافه کنید که در نهایی شدن هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26903" target="_blank">📅 22:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26901">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsQ5sdjd18NNaZTZ4YKwyqPvRpjQ9wE9auKtL7oDW1jZLA9r-M2NARLIakFRxobjpKdTxnuduY9cmuEj10X8wXDoHYIWvp09zmRL-X4rxmTNdyBLNrkzLu6ousXRRKejrj-hJp4ZdRx7uqiGWz2vlqLqOl8UBV47qbY_1FkbsQ9ef3E2RKOsxysKu5U5qvVYFiiyg4RVwiEszJfBjoxol2LUZffHflH6Bag668r0uxFJnyzvpxQBQE91FbvsITGkBJLv2ba9m89b5gufO-0TnsMwJ08-__viu5tKq5X7_13444Z194PuAGmLyzJ7tL263ottwLWch9xOa4Fe3NWxpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
جسی بیسیوو وینگر 18 ساله کلوب‌بروژ با عقد قراردادی 5 ساله‌رسما بارسلونا پیوست. آبی اناری‌ها برای این انتقال 8.5 میلیون یورو هزینه کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26901" target="_blank">📅 22:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26900">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgsttXFs6rDcWaS4PHnq2H6aC_dlp4WPf5BGAHa3Iknnn3Q48qOM-Iy2RpKR3PGdGB2uT1A4gu-zbOSKCy8KKte1LP8WPX4mRRsJvwdhIgYBbo7epF6hA69vcwdlqy_z0rNmFf3psw89UJwtAswsfM5naPRunTKRDtl3GYKruzRcgmP5aBElOVPZ7rkRJprRn2DVcmxBhfOp04CTb1HnYfYcYdyDHqBOJkYcxoBPRPb4Iiy93BwOawdEVykYWNOqbom9ySWniber899f2SJFK55QrKkQFAnrcQ7itMtOb5XUTO8OjGdPAdYcpTiMiN0nn7Zfs3PP_9LAJbjzAmRx0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفامیشود با بازیکنی که 6 ماه از قراردادش‌باقی‌مانده‌مذاکره‌کرد و حتی قرار داد بست مثل‌ همون‌‌قضیه یاسر آسانی با این تفاوت که در حال‌ حاضر پنجره استقلال‌ بسته و مدیریت آبی‌ها میتونه الان‌ باهاش‌ قرارداد ببنده و تا نیم‌فصل در همون تیم فعلیش بمونه و زمستون به عنوان بازیکن آزاد جذب بشه و نیازی هم به پرداخت رضایت نامه نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26900" target="_blank">📅 22:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26899">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtgoXKMPGQr8PEIfh78TJaUupbsDX6A_WAGfC4ZS2z6TtJ9D8LOswycQNNjh74GaMBuvRfNFpykaFnYYF9UNTp1tKpQlZ2QZ6bXY_SoEHZq-WOBJcA65ydMJ97Ol6wIIeaVAM6HCv04hhsDdGblbpIQo_X-mKF4kTPP-PLZM6lYkI5zgvIDEcONFIACdsRXVq0AfDxjuGy0pLe2c8uh--rToMTtiiJpDLTJ0-3bol6wX7i5kxD85V4m3OPgmiN4V0zs48Kskcft7fN7RO0GO56PwCwzKwFhcwP5M9Tjx6V71ix975UYYxLzpbPyMXZ9swEHKyOb6DKfuhxm0UsDhDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
براساس‌اطلاعات‌ترانسفرمارکت؛ تنها 6 ماه از قرار داد فابیو آبرئو مهاجم‌ آنگولایی بیجینگ گوان چین باقی‌مانده و طبق قانون فیفا میتوان با این بازیکن مذاکره و قرارداد بست. در فصلی که گذشت بااختلاف‌آقای‌گل سوپرلیگ چین شد هر باشگاهی بتونه بگیرتش ضرر نکرده است.…</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26899" target="_blank">📅 21:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26898">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0YyhutR_UxACInCdaHeMcS2NRfM18Vk92TC06EEoyWeoOnadDn9ZbcSsNicFYFBI1uMu7WLhpaBbrLSmNQi7JzMOl1ZZx6vGAZnhy9OLmehuwEDTMXVcXEJGV3bEsSzyghu59Ok2BqcWIZ_f3apl5hcDjC6FBZrLTx4ZgSc7GQWX4j76xLAWJBLl2pSZrEWpVAoPwY-FKMFdPDMuRiheLmJvlEROGd3WepnMN9mAxA70TETYY-6GxaDlZ2B_5t00B-w81SmqxDaHt9YtLer9kP6v7_L22LbTyyxnE8WAEtHaYZLl_8SmViGt-bWbEfn199iZ3m_ycDFU4acg2lDxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
در فاصله دو هفته تا شروع لیگ برتر؛ مهران احمدی هافبک‌تهاجمی‌استقلال دربازی دوستانه امروز آبی‌ها مقابل فولاد از ناحیه کشاله ران مصدوم شد و ممکن است دو الی چهار هفته دور از میادین باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26898" target="_blank">📅 20:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26897">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ovjz_qiznazx-xucGWUEYzMMqbO8dA_6jo41iRBSGCdsKqlRKfOxHWA_AZRePpezItY0o_0wgVY2vMTR_mGhufRDZaGeYrUR6dvodce5PgKyRn46BKWun6Uq7M0lGrFpToGB4f5jm76Qq9SS529RUH_8BFMPwoP-YLkqWMpm8GXZKxw6GS4LgSSgtnOjJvlpHDemapS_YF8gXLeJltSe_nPm_HUnbOodacmUOc8ZDTq_ZtE_TRsQtKyGlPG-6WJEAKJo7pQ4C3NSSTM_1r6WWAmp2lLes6iDjo6TKAKvriqPuLlolpFaxSOE8Fg3C2_ocSdvizqDawFf8vwXfEelnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
افزایش 12 سانتی متری قد لامین یامال ستاره جوان تیم ملی اسپانیا و باشگاه بارسلونا در 3 سال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26897" target="_blank">📅 20:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26896">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92aea27557.mp4?token=M0JQsTRqfLLaCXao78cSdHxkgtXbR9IIyrE2MY7sqVrA5d24R3-PB3N9maNuVbewaG8tqvzQtRwY4KEfT7VP6qyWDwzLLonbMZJT4ouAFxjDg5jv0HxEQ25FJJW7OqJoMY49JpkvkpUWJzgDJKmg3Mp-u5wSXtM2jpUpsvj7ByHaVxjqc_gMeMaQzEL9ShzmbEHbs_fDORtzeWB2X7oe6OQvZjvjBBN4VWcjeMuuRAb9CgPHO2m41VKbEPnhMg4nNsa5NRBCyYK1_qtttvNi688eX7yxR1kz8dWG3v2h7_214zDV1Fq0XShQhcVgdDYusGcVLkU-BUut18tYin-RQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92aea27557.mp4?token=M0JQsTRqfLLaCXao78cSdHxkgtXbR9IIyrE2MY7sqVrA5d24R3-PB3N9maNuVbewaG8tqvzQtRwY4KEfT7VP6qyWDwzLLonbMZJT4ouAFxjDg5jv0HxEQ25FJJW7OqJoMY49JpkvkpUWJzgDJKmg3Mp-u5wSXtM2jpUpsvj7ByHaVxjqc_gMeMaQzEL9ShzmbEHbs_fDORtzeWB2X7oe6OQvZjvjBBN4VWcjeMuuRAb9CgPHO2m41VKbEPnhMg4nNsa5NRBCyYK1_qtttvNi688eX7yxR1kz8dWG3v2h7_214zDV1Fq0XShQhcVgdDYusGcVLkU-BUut18tYin-RQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی از عروسی نادیا خمز دختر خانم پاکو خمز سرمربی اسپانیایی سابق تراکتور به پارتنرش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26896" target="_blank">📅 20:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26895">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1QXRQWwulELw6onmNwPfoEsPhToYHHEt1FxGA8K_JspQFAFvz7KqxT9Z2GrrmgTUulzHVlaDFUoPf2Paw__h3-peF5UCGfiSjATnmzQn32RmdfkkK8JyRvyAPPWllPAqJeHadWEVidtj52Wp6zHt6jnpIdmgGKpSXSX3vw3nhaslBGBaKtTFKxAsUKq9aviHFtAd4SSPep5zaD2P8W-kU2rrYw21osnfeUML7rAAUZi4xxYuUGTXo02wzeZDkWk-bMjNjLbOho5wDmu_QKT1gFiO0J9kNsEoeIP7fwRknEtwAxXDkT45APeJwxVjkRwhM7jcJEcFc4A_FR3tGUrlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛ بازی دوستانه آبی‌اناری‌ ها برابر تیم سابق جود بلینگهام در لیگ برتر انگلیس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26895" target="_blank">📅 20:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26894">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-1u3KAXlm_4Z-HNSXI71zCth71edR8LjP3Jl7sgWwkUBIOWoCMZpfcWfw0E2CIflKVKkWDEY6OTuEgcyf9kcdIpHMUdpaiyVrkXnZGHa_XzPRmy2p4CWHPGWDbC9w6ETCHlgJ9_ZM853vGD_l7XL-jALID3DgJ4TT6Mw-sSXKYZ4eI7wHzYd-QjA6tMN27mMbP-4X83XABxsY-Wlslxqo6Ar2Rd3wjRFBrKMyA656k58LmG8yxj2DcnfchcUP3eCyMNdL-NMxJCUu6uNLpPqlv7mJyrpQRwQ31NIQV3pVCsRAW_yDtI8ojrMht--ro0qzLn0FkD3cCZ_iHd5uSMtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شمارش‌معکوس‌تاآغاز5+1لیگ‌های‌معتر اروپایی درفصل جدید؛ تنها چهارده روز تا پریمیرلیگ ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26894" target="_blank">📅 20:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26893">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCMQuNkeQQKO6W9hTye5S4AQwlYXSzlZhtMJP69zby03DFbIywhB1-QOoMDuM0WiKsQwQyT9leJpxZldWdpYReG2SXy2LFCVieEnsp0N4MbjduyZc2UK1nD2KAeX5mWwp_kXhkXrjII7wspaX2YI8qewdtNyBw6IAoxxnOoSYRb-XgIK7TFU5bbBI3JSbGbcnlPqAGyxkwFnNPi0zlch7iJgYey2nX0wjHtdWY4dlnPhlN2Vb8scsM80i1x1be8Jh8gWmKMeL3ftREsCEHagbc3ln-fxDIrEJ38MZ3U22pGo071gNechv9k-NUip1fPOsnbjrNjSdtQAQqNSsEYZCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌عملکرد اشرف‌حکیمی،ژائو کانسلو، ریس جیمز و آرنولد 4 مدافع‌راست‌برتر حال حاضر فوتبال جهان؛ رئال مادرید حکیمی رو مفت از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26893" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26892">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9ttpZAGKLIGNe9qgpa2wX1vdX_AN9s24D_ijf7SNeDQ0AayGNUdMZfDQiHv-T4ma9TVj8yVjWKnvN8uF2EfBMxL6bvUiRNOh2AK1Ow9UIyk8nXNys27TKUC8upQ0EO3BYteGbi3twdIglxwQA8r2cdFYKbKMBI9o0r52d2fxsMaDzEZSN2sl0Fhw420MbN4Ku9xuON_1pMoTY6ju-WBu1nJGjgwil0tayxGOFhYAmIrxh3yNcpZaHoT2M6-pgrklJUjOs_j7wRg0kxNhhj4HqF3K-ePxmUgLY1XLcxgkGMIlsZXiA_6lvbtGtYJN4bwijq_kwFs2QWcl44j-faVCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیربرنامه آنتونیو آدان؛ این دروازه بان اسپانیایی از تیم استقلال جدا شد و درصورت بسته بودن پنجره نیز قرار نیست قراردادش تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26892" target="_blank">📅 19:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26891">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgTNY3TN4UnLEekNI7ioV473V5ACcqePVq2leiMHot4fOTY3sPXaUiQyna3el4xjd5w4lqX7lFJfIeJ58r8MeDH1ttjS0y7b9C73O-ZkWNOqGkPZwnNqvbZ0Qg4H5J4HIE-tWQg_ZIx89p7h0PXn4ds26uukB20lRMlwZVLvT4CDl0DUBtYYp6uhCljRm7j3jITP7udNeBbUsxGIy35DztbiI1PIrKCNpDI4fkOF5m14yfJhkLqqiLVCLYt2pJXzxcoDSe3FIiXJi2XBgtD9PoKrvxVRjpv6aXBaC4alMW-9xty76pZiiesXTNK8zkiKVH_Z70XoIWd8f0sZ8qSjLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26891" target="_blank">📅 19:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26889">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZG452ExeN1Bwxw7EB0_-FR2j4KOm62btjm_Rs2aGO7-MwuziK7l_Ep7aLzzQlUiLQUr9xrEsDLOiksZlgnLLN1R6yzGrzcYxQ8NGyjrngdYNkI9Hko6b8urAM26xba9pvrlTyLoLrFsfH6mLPRY_lNP57Tgp1ZCjcCqE0xmfkJpu701ZdUcdb8KNLvPSRvprvIshbuZcbe6Pjpn05XRbkDhzJSW4C3wiHS91tvxyNZPf08WZeN0UmhosqzAJXHIo_r09Z8Md1q4ZpX_OCp_f7t0Ymjy0AxEm1mYoN0EDAYydmZHhRJuJfSQHdrewqfj7pJJr7GpTyBnWTwlM7SrZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
همسرایرانی‌خوزه"ممد"مورایس هستند سرمربی پرتغالی سابق باشگاه سپاهان اصفهان.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26889" target="_blank">📅 19:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26888">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoUnjk0TQDOoYSzrkfqimVgg4U1DG2N52xkNRVgL0H3j3700cfMCfyy_6Fpip7b-PXJU8c58A1Axjt4c0W1bk_TfAXjZattnwGIav9HB02MgZWqR5OptCFFvw-hHDbtmd37o3G90fnT3eTa4wXNMj0wVGtscb9QkMLnH8YXWAALdrxfr2BVQtDSJYEILSGNR97dJdMohZ_DQlUlNYEwSI6k0dHzAP3V_wXeJrwvn9n2_VgMIWCqn7jPGNPB9vDRktYGF6CU_3PWMX12g9sJSfImrX8IL878_ySk7R9OC2wSPqpCD9ZDtnohxkrc_vrF_kX3mRjZM35740o_LScKjoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇺🇦
مارکا: میخائیلو مودریک‌ ستاره‌ محروم‌ چلسی تصمیم گرفته که در رشته دو میدانی فعالیت کنه و هدف او نمایندگی اوکراین در بازی‌های‌ المپیک ۲۰۲۸ لس‌آنجلس است. او تصمیم‌ گرفته‌ که کفش‌ های فوتبال خود را با کفش‌های دو و میدانی عوض کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26888" target="_blank">📅 18:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26887">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیویی از مراسم عروسی کریس رونالدو و جورجینا  که‌توسط AI ساخته شده؛ عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26887" target="_blank">📅 18:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26886">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wb7lw_3D7aG-JWYl9KQFAIQSwErqfJ4aPF9q5bd8dGyI5IsqeOgFMWYn5QIgSKbc4WvnHWPz6uTtc6JwOQ128lJWoglR5HECwODkYLJSD9-CtJo6kYZdRZ1xaeBFi52CVquRDpJ68oe1DK83N2TAWBc0hZPwW7Ndh_12XB8ZV3YVWME8Ilf8I2pvITVTcJDewFLfFhE00SS5oIFCvN8fJ4nn3xgTTzGH7YdZBmMeZ18wtddDouhiY_jmtGIDH-cATmcG8sn1snPVnauBYtHisbfhWXixI43ZDCw6S6CVvHlDhvsyiF7pY70k0G0Zw9BUGQhCNYKwI87CRYDCk4DzHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ESPN: رودری به سران من سیتی اعلام کرده که به‌هیچ‌عنوان دیگر علاقه‌ای به ماندن در این تیم ندارد و قصدداره‌راهی رئال مادرید شود. شماره رودری بعد از عقد قرارداد به رئال 18 خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26886" target="_blank">📅 18:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26885">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVvgecPM9Pbe2l1tWTmEaakKRpwmUCrNaMTNrmMLpdpnd-YqdxS6x4CZn4CvyRdB-goJS00LtVKelZBIhhEPkM-lij55M5xmDH0koycWQUO-8Efozcm9jHUXERM00jlNZSdWlBmFqppCGz_V9EV_pdI8JsQ4TWpL5SoxJ_WluBRrhWcU9EOs0sIM55OA-BgQydM2YVe7iM_JKmhLJsJgKf9Q6v5--gIl7M8A4ag7t0Me8TRmcf9slNntl2L-lfyTTblRpqWmqu_RAMjmhbt7eOpWwgl8H6p-REcHmcWcMQme4IiH3FDvm1SL8gXPR73b7ajiN77R8_j9cSqf6ImWyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمارمعکوس تاشروع‌رقابت‌های داغ فوتبال اروپا؛ تنها 27 روز تاشروع‌جذاب‌ترین‌لیگ‌دنیا "لیگ‌جزیره"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26885" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26884">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9Q-qcn3AbfvE5-sR92o_4qIv1LlhXlssI2TuWPh8C_1U2OZ4vyyACgFfr_SWFteha7KF3tqKDMw48h1IQGHgDTDo7w7C1SaNi0g0sD7nunZ7H4g3aa3eO3gWmgunZLSPdj984dYEEzRvxK4-VNNg6Flb8py1hiPUTp4-sZlGt2oJ-vBww99YLOOQBuOEHajHA0SBO4xZnKllEunPqGa3AP0RSyEukEwBejqaJhMlx7vujefALQKbwrYbphK6iq3039Pw7lbIPn_VnJnBMKgv4YGENsJD-lNychGDf5u8C9B2Ir3O8Z4c0YJ3w0mY8XRZGKmoK3gyAl3my6V3VTgtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه دیدارهای هفته اول و دوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26884" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26882">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MW76QjjtJ7BvKjnIBnGsbcu02TQt4fMHE7WkkHjfYaP_IAebIeSCUCzpewPLsuC3Kg-ngvpxgKlC48LbtytX-XJKyG7p5-S5u493-Oy5Br3IFu8TttONTJFZ26k-bGI_rQSGuWz_7z75u4MhqTZy3wJzlGVwFm9tRt5H-AhDbFRaA2QFnmSU9RIyrjgoYvuYCGodyTqsJiGCtZLZn9KNaHfmxUA9TB4FKA5QXuIBovesCDgSiY6vWA3IM6ADI_W2IV5cXmrNRIfGhcTQHx_Gw8Iw1vEPY2dKbQUWVDBv1BHjN_M_-d8GTa41Ne0r_uP_vzlA-UCDOC7CP7lnmc-vvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
وحید امیری کاپیتان سابق پرسپولیس برای عقدقرارداد یک ساله با فولاد خوزستان به ارزش 25 میلیارد تومان بامدیریت این باشگاه به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26882" target="_blank">📅 17:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26881">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjtgxK13gKUC6xdecphGLpuQ-7-TDvmAMpPVysvDcIQ-Y6w1ilDMMOlwZRl56tw6GRTMGBWbRCFJM1qN9ICDoPbdS-qTBBbu4AA_dKkJpIJR32ZHWMk1_jvho_tKXx72j7ni6xWbCGsND8fqVTSVvO0CC5kTccQwqgD5yN5IBnIuHpmDUOG3I5bo_XgfRAtbW3dyYghEcPXD0E-XuzxWP3UJPRhHiJWrE6jmdjFFhMSszvkQJvUnDhnP4NU7o-KjLIn-zbnDySjW6VZAZ6fiULUAQSmWFs3qNIJ4SOYaFFSmDumhkmYRHHgcZki_QrllPJzW6cfWcetfetdtNi_B0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوتامندی‌ مدافع‌آرژانتین:
دخترای‌خوشگلِ زیادی بودن که عاشقِ دیبالابودن‌ میدونستم‌ که اونا از دیبالا خوششون میاد، گاهی دخترها میان دایرکتم میپرسن "دیبالا پیشته؟ رفیقِ نزدیکته؟" سرِکارشون میزاشتم و میگفتم:«آره بابا اتفاقا الان خونم مهمونمه! میگفتن میشه ببینیمش؟ توروخدا، میگفتم آره آدرس میدادم و تا میومدن خونم میگفتن:"کو دیبالا؟" میگفتم رفته بیرون مغازه خریدکنه الان میاد، بعد از یک ساعت باز میگفتن پس کو دیبالا؟ چرا نمیاد؟ میگفتم کار براش پیش‌اومده‌رفت‌متاسفانه دیگه خودم مخشونو میزدم و باهاشون دوست میشدم. دیبالا واقعا رفیق خوبیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26881" target="_blank">📅 17:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26880">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alxeQO4koALfRshbVxw-HTlu0DD8GfjK1bty9IGEZ8aALD-1Kcoj5SBF6pp7vNUlfyfm2ErAvl8ly-kRfoktAS-KWgqS5ssEnN3fNpBvOpxZDWHNYkJys4VQLmLWc3KzdoTaCb57tQ-Ae7W7pFhIgAN22NnFtWnSFESqyNqDhtgl9M9fGFOgGk4USHT-T-wP1kdUWyBmZgwQm-isBynkYM1OsSRV6hE3GjUM3f2MwRxznKZizhbKVcXci0L2_8jeQArQ2FWPwnLsUWLTAGyhsBBMeQo-UV8EufuXUePqLQUHbWITW-JbiYQPV9R1czzt5Y-kaKZ0v8pJpH3gPqDSbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
👤
#اختصاصی_پرشیانا #فوری؛ امیر رضا رفیعی دروازه‌بان جوان پرسپولیس که در آستانه عقد قرار داد با تیم‌ گل‌گهر قرار داشت با باشگاه شمس آذر قزوین واردمذاکره‌شد و به توافقاتی نیز رسیده که به احتمال فراوان بزودی پوسترش منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26880" target="_blank">📅 16:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26879">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e6b766e58.mp4?token=FF_SYqdhaYeOHpR_mWW2_m7Y7i-4SuxngzcrsXhoYxYfA7HgWMwF8sAio0cdCoPOQ2h-8PNQrV3ApLLngLEIbGLdpfQPWA2GdINTO5yEunt1isdTC8lqad6oWoIqdpL1Bd1GlLt8OqqPXcz5jhD4RfSXlBZ5XqPJobHUvQUPCgBwCP9HRNJqs-U-51jOX9-NgzBSBzLnRp00DIcofgjYBZa5vC0Gd3y8tRGXaiF3AITbQbz4wkVoDXNqD3qjT3Ci_4Mnbu6tnxjnnBMxIG-Es5nTR4U0zyMzwUjBuJtZ75RWi5Y7qDvdyVU0J_yzW6HtuToSPGB7ro-3e3xT9Ns5Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e6b766e58.mp4?token=FF_SYqdhaYeOHpR_mWW2_m7Y7i-4SuxngzcrsXhoYxYfA7HgWMwF8sAio0cdCoPOQ2h-8PNQrV3ApLLngLEIbGLdpfQPWA2GdINTO5yEunt1isdTC8lqad6oWoIqdpL1Bd1GlLt8OqqPXcz5jhD4RfSXlBZ5XqPJobHUvQUPCgBwCP9HRNJqs-U-51jOX9-NgzBSBzLnRp00DIcofgjYBZa5vC0Gd3y8tRGXaiF3AITbQbz4wkVoDXNqD3qjT3Ci_4Mnbu6tnxjnnBMxIG-Es5nTR4U0zyMzwUjBuJtZ75RWi5Y7qDvdyVU0J_yzW6HtuToSPGB7ro-3e3xT9Ns5Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بااعلام‌‌باشگاه‌‌آث‌میلان؛ فرانکو بارسی اسطوره و کاپیتان‌سابق‌روسونری‌صبح‌امروز درسن ۶۶ سالگی درگذشت. این در شرایطی است که در روزهای پیش خبر فوت این اسطوره منتشر و رد شده بود.
📊
بارزسی افسانه‌ ای ۷۱۶ بازی رسمی برای باشگاه میلان انجام‌داد و ۳۳گل و ۲۴پاس‌گل…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26879" target="_blank">📅 16:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26878">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de98c1f92f.mp4?token=il84t1ER6CScFCipB43jX6JXDH_mNCjTG9xVENH4Dku8l5LXUBKkfBbqGSC12OOEk_z0gqcMya1E14XAV-WKaLawQ4Jv5n4R1C8gW9yhzSJ53IDEdvu9fecDZbqSmFmL8-DWGGL1dFxPZ_9Zb7jVx9mYaG3Vn9hgkfNzsIROxJjZpas82OTyfMglgVTpkzrDs1mBNWNDlr8mgI7QtgFN7ccUhF8yCnkvFlP9A4Hkyvs2V_aWe1beK8zSuOvbiiKywJlE4W4xH5CdwkaDymKElnOy7bmaItaVMjBVUuRgK1KmkciFR6RbZXO9CA8X6DNz-7CW2dUsgy_Of1EyVsnNJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de98c1f92f.mp4?token=il84t1ER6CScFCipB43jX6JXDH_mNCjTG9xVENH4Dku8l5LXUBKkfBbqGSC12OOEk_z0gqcMya1E14XAV-WKaLawQ4Jv5n4R1C8gW9yhzSJ53IDEdvu9fecDZbqSmFmL8-DWGGL1dFxPZ_9Zb7jVx9mYaG3Vn9hgkfNzsIROxJjZpas82OTyfMglgVTpkzrDs1mBNWNDlr8mgI7QtgFN7ccUhF8yCnkvFlP9A4Hkyvs2V_aWe1beK8zSuOvbiiKywJlE4W4xH5CdwkaDymKElnOy7bmaItaVMjBVUuRgK1KmkciFR6RbZXO9CA8X6DNz-7CW2dUsgy_Of1EyVsnNJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی کوتاه از یه مسابقه والیبال محله ای در زمین‌های خاکی؛ جدا از بازی‌خوبشون و اون دریافت خیره‌کننده‌بازیکنه به‌وضعیت داورای بازی نگاه کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26878" target="_blank">📅 16:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26877">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCLv9Q0zmTwBMBEYXNKXT191mxhsUzWykOl3BEr1a6GrH8P_onKnaSyvtRSddZ50YSbc--JHNu5PCWB4NaNbyUqylAM_4vI_Ubyld_oHaMGkHIjpa5xU-Id6klfZ06kXNs9Gcar0T-KZ1YVFxo2XysTHqPvlyLPOXr8cYnqshqTK2WQm01p0CRfUU1yQzaKsSW4Y7-FrTYTjg5vryl766Tlzftk_fqZcUoLcaratzGcRV6flYBG8A_iokMgD6F-8eHxTDlRU9ADW1wPJb1ph2vax2b-1NyjpcOOx6pEdwimURgao8x1UmEHx27ezPTvDriIPgNof5tURsDcekZDzyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات|وحدت هنانوف، برایان دابو و ابوبکر کامارا ۳ خارجی سپاهان از این تیم جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26877" target="_blank">📅 15:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26876">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGg2h3K2cgs9hhvjQW8mbhdX9k3EfYEd6Y9IAKiZaofcYpgGhw44NeU8zYd2uM5_EOrnIiny21R5MomRw96FSEOA28qAdgjfbUgFTcZ0jaC6rg99XTk6IQdQ0gsQ1ixIGl4GR8aU1MoBjiJ_npZDpqNKIs2-DLFROp65bMSDEc3myTAYNncrN2uERJbh9iOjbFwLsgvLVq8SPRY4BUBD8NNVhKpMaIEle40_WUCWCQd_YoPG9DdAAsfbuDkg_K8Ukxxlcu7bm8rICyOxq85-VBuJWRn-wWoJoSlr_L1Pup5v5ePVCr8mjeW7rHUIxazlspLmGeDIqXnDFrwVHoHdPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه تراکتور ظرف 48 ساعت‌آینده‌از محمد قربانی خرید جدید خود رونمایی میکنه. رضایت نامه این بازیکن دقایقی پیش از سوی الوحده امارات صادر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26876" target="_blank">📅 15:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26875">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f12e49800d.mp4?token=q7MIt50OXO3O3jHWKXaiHZ6s9oLwSm892le9bLyYEI6kSkWRVZ1EQpqrSLUyZfcK02t6K2c55XPXhmqHlYeziwb8PzI8gD2kR4ZboaGO1SgGcrzjLLZBzpA5eOzbTRXzwyKYBD03uBdZzj9UoT1yFXVlynFAnr-vcpVHcw7kIm76d9LYMTw9b1upJeElUc8YIBfifNtS8W3ltPBfMYnlmhSn6Lsu69HXsW_hdCVjfgwJFmxeBo8te6gfZw2IYxgk73toiyCopxnYN6kI3mvS0tTApjwFD5_QFtct9vdH_YO_Fb-XCQ39L14vhf9hcPBjnPsZYtoigXlJXtVE_YXcvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f12e49800d.mp4?token=q7MIt50OXO3O3jHWKXaiHZ6s9oLwSm892le9bLyYEI6kSkWRVZ1EQpqrSLUyZfcK02t6K2c55XPXhmqHlYeziwb8PzI8gD2kR4ZboaGO1SgGcrzjLLZBzpA5eOzbTRXzwyKYBD03uBdZzj9UoT1yFXVlynFAnr-vcpVHcw7kIm76d9LYMTw9b1upJeElUc8YIBfifNtS8W3ltPBfMYnlmhSn6Lsu69HXsW_hdCVjfgwJFmxeBo8te6gfZw2IYxgk73toiyCopxnYN6kI3mvS0tTApjwFD5_QFtct9vdH_YO_Fb-XCQ39L14vhf9hcPBjnPsZYtoigXlJXtVE_YXcvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇧🇷
پوستررونمایی‌رسمی‌باشگاه اینترمیامی برای کاسمیرو خرید جدید خود؛ قرارداد یک ساله همراه با تمدید خودکار به مدت دو فصل امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26875" target="_blank">📅 15:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26874">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_lFaag-4KI2W8_SnO3yvGYhOaeFGe4dfaH4p7eRVwMwKFsQhX-H-mlLFQZIO546CfcT1o5kP4E7WHbZNNdFDcgFUOOCTxMWHpEGyr-9v_-fP5-9rC-II7LQpU1CNuX5R9OegZ4phmxY3C52bNm0TEu3yXTmflFLgNlim-Dp_LQEU4wBavHDS9-x37bTwid4xlHmBxAGOlLlS_MqjV4NgMQGeW9h0YxSPDHE3bbbD1LzK64iYLmleBF9ERAkeNHe0S9RcNFCF-PpUJ_2lTDuPxwf_iGqDUHxze8ij1CNuHIeHX7Rv7MdLCSWP724BBikF0CbFJmtdWVGl1kLiyXjyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استارلینک توکشورعراق‌فعال‌شده. قیمت‌ها هم با دلار ۱۹۳۰۰۰ تومانی: ۹ میلیون‌برای‌سرعت ۱۰۰ مگابیتی و دانلودنامحدود.۱۵ میلیون‌برای سرعت ۴۰۰ مگابیتی و دانلود نامحدود. میانگین درآمد ماهانه مردم عراق: حدود ۵۰۰ دلار که میشه تقریبا ۹۵ میلیون تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26874" target="_blank">📅 14:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26873">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbKahN4EYlk_2yoGzIeCPRfSbtqEVy6f7Cuj8jfRF7Lfveo4oKTA1eGUIolah_fG4yw-XmRn7yOQ9az8enQdm2kpZrJjovCBg4bO64O9dYivMQN7nnYS9AHsc6d_F1uRxkP40w3xWWjKjeh5Ji_j4Frtr05MJpRmtJUbplg8TdXkZb5nqbm28y02LuVMwiMgfUBF5rsCFXzA2ef2v7M7naTwYdJnnWjS8706He-XlMxa8o2XYJjWo7lrRIS1LvnK1ufvBMiNwoHTNBLdSTJlNEVZCQPKfXodwsHdFW9Td_Ht2md1QE2fLlWgt0iXEXmaPPbmFJlV5caiuGjnOrmKOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
باشگاه آرسنال بزودی بندفسخ قرارداد برونو گیمارش روفعال‌میکنه و از خرید جدید خود به شکل رسمی رونمایی میکنه. تمام توافقات‌انجام‌شده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26873" target="_blank">📅 14:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26872">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a91beb718e.mp4?token=ssrYmWwwhFU6f2LF_p6_4JpdzhsZLNLQgkHJSv9HaR5h3vmo-B7ul2OFPo5FZx_DsMSjlFMCMDODFyIXNTshIYsnWSXMVUN8VWKxXYM5y-he5lY3udIKGv710YB2smcrZvFWi9-mskaR1OD4QD5vB8bDRKWaz9hgbk9E5Gk5wGMK_SLJF7N1d3XQcgg04AeUpkXJX4F_x4XMpLoCz4LHzsVGRuxU5cFCDJO8_GTQYuox3uh51cAAwHio5qn_bIItSRh7DejZ_qzxKm7KYBq2hEmXtxgHFTI2oyq0Ae8Ybu7gh9o0ZANnz6fiV2HUkut5teioirLnMztU7cj22ktJXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a91beb718e.mp4?token=ssrYmWwwhFU6f2LF_p6_4JpdzhsZLNLQgkHJSv9HaR5h3vmo-B7ul2OFPo5FZx_DsMSjlFMCMDODFyIXNTshIYsnWSXMVUN8VWKxXYM5y-he5lY3udIKGv710YB2smcrZvFWi9-mskaR1OD4QD5vB8bDRKWaz9hgbk9E5Gk5wGMK_SLJF7N1d3XQcgg04AeUpkXJX4F_x4XMpLoCz4LHzsVGRuxU5cFCDJO8_GTQYuox3uh51cAAwHio5qn_bIItSRh7DejZ_qzxKm7KYBq2hEmXtxgHFTI2oyq0Ae8Ybu7gh9o0ZANnz6fiV2HUkut5teioirLnMztU7cj22ktJXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
برنامه دیدارهای هفته اول و دوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26872" target="_blank">📅 13:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26871">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAMYA9yOCopiR3rPa_HgzNfytbQut7BRuf6s6EVBY4gJqdClLnY51o1K68AtHPOlvb53aMwW4JrSbv8xixkOZS9GyvTqJgXvCWdRMuawN_vMUedI2ca1wVgEPtfX0N9vQI4umZsR0UtvWo6ZwV7ThNBV-nrcHuiPZVb1Hdx0QJB_wlcsC91CCk-fHibiJHAtmq0Y5QyL5Ss3vK-f1BkcWWzse65XTE9Bg0UubOZYRd8w5lPx8sIj6bKO_JHR8uWKVMumBjqPlRBM0W-ScdoL3XCYI91Z7EOGIbPL2-1WcGTFB7QO53mVhG7lHwAXV-Tcv3qapSU2b4aojV0Xuak_IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مایکل اولیسه که علاقه زیادی به پیوستن به رئال مادرید دراین‌پنجره داشت تو تعطیلات در حال خوش گذرونیه. ویدیو مثبت 18 بود تو کانال دوم گذاشتیم. بزنید روی پست ریپلای‌شده کانال‌دومم‌داشته باشید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26871" target="_blank">📅 13:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26870">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2b1c64c36.mp4?token=BtJ_-XHOk2GMw-mOAxvWyvtjI9qCVnC3bTa50O8KjAfE4C32DiDe1zEXPqK37FCnrgyFbRuhYqsIPEteWXnYLpE38piRBbPZNjjMkz3tpFYbeND7GCaVajxYqLlKFm48mAy5K8rp08jvb9VE3NT8iVRhsAg1we7JLN838H5K9gqrEywdJH7REjcJ6LP-u0nLKSmOO0qHBkyB5W6pfF7ZiXSIdGgDj27hWScKegA0zdxocSD1axQbDomsKOghXWLvyH-wpnR8yGy7_Fu0ZIchcoxvn5HvWtIOBU9iwvyyO9qcIpGIt5iYUynI3kGyP8GFzy1kM5LJ2e_XJeOcYU2VBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2b1c64c36.mp4?token=BtJ_-XHOk2GMw-mOAxvWyvtjI9qCVnC3bTa50O8KjAfE4C32DiDe1zEXPqK37FCnrgyFbRuhYqsIPEteWXnYLpE38piRBbPZNjjMkz3tpFYbeND7GCaVajxYqLlKFm48mAy5K8rp08jvb9VE3NT8iVRhsAg1we7JLN838H5K9gqrEywdJH7REjcJ6LP-u0nLKSmOO0qHBkyB5W6pfF7ZiXSIdGgDj27hWScKegA0zdxocSD1axQbDomsKOghXWLvyH-wpnR8yGy7_Fu0ZIchcoxvn5HvWtIOBU9iwvyyO9qcIpGIt5iYUynI3kGyP8GFzy1kM5LJ2e_XJeOcYU2VBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
توضیحات و عذرخواهی میلاد کرمی ملقب به وضعتان چونه درباره تبلیغ مرز ایران اربعین:
‼️
یک بلاگر معروف در فیلمش گفته بود در مهران ماشینش دزدیدن از این مرز بد گفته بود خیلی هم وایرال شده بود خیلیا دیگه برای رفتن به کربلا مرز مهران انتخاب‌نمیکردن؛خیلی از مردم ایلام…</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26870" target="_blank">📅 12:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26869">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VomH1XNzDYQMoN6tNTs_p1NN9Il7_yalhM02GoskCrE653_cwEF-zA60LU-F9pELLXe0Q2pvpxB1zQ9y_g3xrH2fzvvBBHvr4cEmy6Nq-lOtLx5215K1rZRxncdzT5sZ3Fk2cNGCuam4QZRTBqIgbkPWVK-nOBF8bo_jkO1s-HNhAh2IEbCxBv48du1lLwiIXaIr_kEbwTM9h9paAaB9D5aVxaEWvceaMjDbVNuang15bw5ywmVYpNUOje0FmAIc1yB4AG7WNGxom-7h8RzbASWBAr9ib7lgEtEliOXZf5lQhor6eS3IRetJA0Rs4z5Wn4EKzqZf5EwePae7YVOvmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
نشریه‌کوپه: باشگاه‌فولام به‌درخواست آلوارو آربلوا سرمربی‌جدید خود؛ باپرداخت 70 میلیون یورو به‌ رئال مادرید گونزالو گارسیا مهاجم جوان کهکشانی ها رو با قراردادی سه ساله به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26869" target="_blank">📅 12:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26868">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lsml0B_zFBAeicFpS2bAOfVFsUxj-ebLw3vaKf4oEV6pOi94zDcEGOuw30gXODn5-RZWhPJsWx-yv5HTFp3kSnkUPURsHxVfD1LHwodRPWzpc0dQMU1JRTXjhU6exnajCAbYE_rMn9x847B6R6BpITJNiRi0PQ2-64ZxDmPoH14bewKgftgbsqHrtYlscWjYWVfuGDLCQNMveJ9M-k6c6g4QV5jDQrqIy8iVeEbtSlh9OvSfPzhT5QuoEpnMj3UVkUe_2_KRMG8KJ-83HowruPlvrssrw609o6z4-ngiCh_3LPSSpA8cqc7A-P4tg9hxi2exQW2bvjjPX_OP6rPSLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شکیرا خواننده کلمبیایی: جدایی من از جرارد پیکه بهترین تصمیم زندگیم بود. اون با خیانت‌ هاش بارها به من‌ ثابت‌ کرد که لیاقتش رو هم نداره حتی باهاش هم صحبت بشم چه برسه به زندگی کردند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26868" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26867">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CD2RQpM9OCIx2gLOkuyYX4H00AxTQiG7KsJRmEdDFht-_CPebHWhPAAafCDtD-OVvmeMW7IXikYKaKT3lQc8KwFbsPYIQikbX9_kJ_2lGcRPTlaz5pimJN_3T57p85Wmc_CagZNlQb589AAkKk2ffYMjeA9KZcp5UQLmquAkzVf_JZl1l2lNJPK0Y_VtHb3BPzjcxPenRwkS45iXKdKv23uvl7Py4b69k6lhszCLfj3tXsbwjHpTg-sNkZ5DSKBXHWfvjmM1v09Hbo52z5Fe0Mdaz8TeKTfbvh-F_xmJdkWdzSMKxx_zvqswkW2qIAHaR6-C7BdwZuSSSJ-BqAGFRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیمار داخل یه ویدیو به محله‌ای که توش بزرگ شده‌بود برگشت. یه پسربچه بهش گفت: «من پادشاه این محله‌ام» نیمارم‌گفت: «یه زمانی منم همین‌جا به همین اسم صدام می‌کردند بیا باهم عکس بگیریم.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26867" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26864">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a5naXaHI_AogS7Pck_FWUSQl35VThRTdyVdMNnC2WWBFdHgO_FhPK82xKYPntEH3F11mOBg5bMNMECgqiXWoxzrfwUu8fjdCx-Jz7vSJC9q0VHIgV8WJuESmC-DsiqdTtxdFFHeMR-tbWnCXv5xHtJbCLbO5cqOf02qQfh2h-T-GbwtlDXfgk9YFbxXgWzl0ibg8QY98SlX2RgDw-e1Ezm-7KOlJAwwsVYSY43Th3EXp6oUPA3A3Whe6ln2Dlijyrnz6wODCsM9GAUpShl3QJKo8ITyeijQO85fBD9Wp_QRjwuYsLRM4pekazvoaFRZ7v47AK4TtwoDC_8k-qWR_JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QerTzT_FkV6Ie3JVLHOGVy6dBCPoiNWl7rra_EdAEJJCvdOtIjSD41HG_8uvcQxNL4haRRxDxRxU67URRgalvkB7j-8tuZK0i0YozXO4ylR_pwXWgbSN84b32Ae1dHsRI8sBOsgkMzFFqC2wk8kXMCygKSRmTe9359guGOaa9pNmYlWzK6MJhqU8Exbhj1aV3JbWEittSSCjPeeYH88Ic64bWcXZ2FRyqQSeEHbUF8rnwmWnN3wQqU6exvJMxYWx-KUjYhsgzFCSEa_KFTQQPfnMhokywPhIC1IgXoydYigrnKRDSDJkhWrOwJj71W-FklWBKHjFD-VaqnC-T3PknQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رنکینگ بندی جدید فیفا برای تیم‌های ملی و باشگاهی؛ لاروخا و PSG در صدر قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26864" target="_blank">📅 11:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26863">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSi2MPGk1uXBTBOSad7aNBPUQKfD--it6rc6xM8E7zRkhn30Dx-RJZDBROW7L5ivc1BU6UT0DMR2LVtW3Pq_2Q6O47q_q49eF_MkVwA564KMfxX4Z-yCwDBRUg4eO3Gx6HfQk-Vl_qbjDNGnz6pWJV-GFZ6m2ChHv1kSPehOrZimh8sZwnN8Vz7W0hNFMcFUHKhEjR6uOO1gKaK6aXy8kHAgYupvYDI1JWq5Aysb1ING3AFV4HIVQ9DGcblB4TzZvpiLqbC9ZL1l0_2Tf-viXqQRdW-qBwbPPLP8FBf2h-Bp-hQabkkI47i648OGax31RB0qFayVYDp8XlbtSgttQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سعیدمهری هافبک‌میانی‌سابق‌تراکتور، استقلال و پرسپولیس با مدیریت باشگاه پیکان برای پیوستن به این تیم به توافق رسیده است. رقم قرارداد مهری در پیکان برای دو فصل 25 میلیارد تومان توافق شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26863" target="_blank">📅 11:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26862">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPl5WnndoQaT4SnMUiuk-2p19nP0H4X0OB5hPRUj7VMXCprMzRUXr5BVtc9MyXYGE0JOKxv92mvE3lgpL371IXNfnbOPudt4LKxU4zQiOChxQ46Bt2vmaolhUZeR8um_DppSZxc82hDztsvuWczI8UOARM7F8bna2bCFaJVp1EJ9XCmCwhDkdFwCDg-4mIRrxmfJ2BAdt7gcGFrI8bbF8x4R8FluEIFQqh223yOXBA4gBJl1DPZaBVdwxpTD130cl4N__1xkao-u9QnOufQNh1q8O-PJENUUqUGKXSlugNRcSR5YLct92gz5mohHIm2cqLGsRsfeXkvjy60b-FlZbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عیسی آلکثیر: به خاطر دلخوری از بعضی مدیران و بازیکنان در پرسپولیس، به استقلال رفتم. با خسرو حیدری و ریکاردوساپینتو مستقیما صحبت‌کردم‌ و هر دو هم موافق اومدن من به باشگاه استقلال بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26862" target="_blank">📅 11:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26861">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5b33a46ab.mp4?token=nfykxJs5vMh6dD90GCmmScRrcZkzbl3arIoyVQZju1xou7zUk8UoexuXXw3foukd5_gBYfpwZXNPkclI9cQBIbtSW1s7BZPVY7nUg3zyxXPtgIRga_kHhf0PgbdcDqxyesHBlitTDJILwFXjgWNGmvjM4hU93bokxC-Qnlu3dIbA-ET4wqYHRyXKRn8cvRrOqhuasm6R92CxSQkpxlrr3G-_WO8kNwNvnounYqPSpdg7FCa_jf7xeMjUVWu16HtrCvFTVQJa-Tt74P3Kmvqk5x66zbCrzG2FbDHD-3L9d-tfKMGWmVMZKsralmF2bVipJjVGZrJk_pGp-hxym6GcBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5b33a46ab.mp4?token=nfykxJs5vMh6dD90GCmmScRrcZkzbl3arIoyVQZju1xou7zUk8UoexuXXw3foukd5_gBYfpwZXNPkclI9cQBIbtSW1s7BZPVY7nUg3zyxXPtgIRga_kHhf0PgbdcDqxyesHBlitTDJILwFXjgWNGmvjM4hU93bokxC-Qnlu3dIbA-ET4wqYHRyXKRn8cvRrOqhuasm6R92CxSQkpxlrr3G-_WO8kNwNvnounYqPSpdg7FCa_jf7xeMjUVWu16HtrCvFTVQJa-Tt74P3Kmvqk5x66zbCrzG2FbDHD-3L9d-tfKMGWmVMZKsralmF2bVipJjVGZrJk_pGp-hxym6GcBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26861" target="_blank">📅 11:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26860">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNyYcVmPiApW9onsOBhwQW7gWXCzPJ6v0UhjH5EnUK11msEurklWyPwa7jt-cmHMQXRTNXXnTHH_sAJzRCqt55G_Qq42qLGGy37OQt7U3bNfp4ttdfAGT4mtk3CKL4UwZKP_K-TN-pGuAzL7dZrSq8cJ0v_fMPYhD8nxcWuU8iyQjBMcoKyqzdBkuj0R-G63ov502-26LY_4ZX02Q6FKbJluOzyn8JojNY8x-h6FQll31PFeXGypbDVT7TchtmM4nSPNn6hKzIPvmReGxk_ud_mvRaXfV10IDzu2544lrHQq7tQpYGy7in2ZaVLKrhmAITVYdmxJO8QdbQ5ORugD5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
باشگاه خیبر خرم‌آباد رقم نهایی رضایت نامه و فروش مهدی‌گودرزی و مسعود محبی دوستاره 22 ساله خود را 150 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26860" target="_blank">📅 10:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26859">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsAx3beA8N17mhosxu2lu03BRNnyahAkA7CejtsG8e4XEc0airZbnM6N2uYxlo367QnE1KnhPIYuu4XFR8cj9sCHMNuvHNduYTWddD1fDRWfdEZ79LBqS8Cmw4oj-LwTLL1IVwl1nWUXtE0iAVm7SgmFusKNbfHpDDL4-XZw65kZeoHkU7IbwGsXy8pzMpoxTJtQGeV47IaM9ixTyzdIz8HBooVyRRUXOnk1mf389xkyq6fMUcIDxc9T3EbnKECxbUuwdLsuPSFix6L-LAFMLys4k-XQ3IvQv6NGoLTarmwgVIddjc5DBH-CNZNKIxarPT_55Oue6FLQ7va9VoFkvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ عثمان اندونگ مدافع‌سنگالی 26 ساله سابق گل گهر از طریق ایجنت ایرانی نزدیک به خود آمادگی‌اش روبرای‌پیوستن‌به پرسپولیس اعلام کرده است. تارتار به‌مدیریت سرخ‌هااعلام‌کرده که قرارداد دنیل گرا رو فسخ کنند و اندونگ رو جایگزین کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26859" target="_blank">📅 10:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26858">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOAyh12P0s1v_cKjhiVJ9y4v6fQcD_lQnGdXBOFtALBkyhxPJoomDJYjk8tgimHiZTnl1i_SZWLZLvZph5xhdo1QbQaYYj9agcpxtHV2pH8TZfxv0J_tWmIB1X4IbonSJPANzp887ecn70NPYfDUERM7VU9sPG1idwfRxd80-_INYanBAJC3uKyV35sD9xBJ85Y3wUwtZkA8RrIU3t9aWvh2uZoV2p1vQ0EFowUCZVWP39uqVySIxWU3bVHLw4FBOZJeaFg1sMG9A2pJv-0WB9xMuqePAr-EW5PqzC_N_BgkWatcOg3TEDbNRy7eyT0lfrf_hqPwetgzfx8CP8qjzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌فابریزیو رومانو؛ باشگاه رئال مادرید 25 میلیون‌یورو به لوانته پرداخت و باعقدقراردادی پنج ساله کارلوس اسپی ستاره تیم لوانته رو جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26858" target="_blank">📅 10:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26857">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhaMJ0XvrQsQBNrwUSK0lcm48RedbwQM-jIDR2WmBoVtd2d6SzhcGcjXFL0O9noTnFi4tJ89ydvB7F63h_ifrKnetPkJ8pv0tW7i2W1PsZmADOUpF5XYkloy_BjLH4W4FZu4YaRXgi1e2-vyHWL0z5sRjmOT-NwVhy7eTXSQ6LcHW2TWc-5xrQDI0FRal7nErfX_s8KdTqUggP5lVra7KknZBFFfLgMgOi8T_DTmmw8qNVfoWE7aRgt0vZ3lZF8H3KZCtaq3ZRJAB5Phf_D8YDXgmvZ9oiusfSRFo1Dxls3U5g5Hzm6lfwA0BTHopk_MlS1-JoR5nLmox9Ba8PDFLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بااعلام‌‌باشگاه‌‌آث‌میلان؛
فرانکو بارسی اسطوره و کاپیتان‌سابق‌روسونری‌صبح‌امروز درسن ۶۶ سالگی درگذشت. این در شرایطی است که در روزهای پیش خبر فوت این اسطوره منتشر و رد شده بود.
📊
بارزسی افسانه‌ ای ۷۱۶ بازی رسمی برای باشگاه میلان انجام‌داد و ۳۳گل و ۲۴پاس‌گل به ثبت رساند. سه قهرمانی لیگ قهرمانان اروپا، شش قهرمانی سری آ، دو جام‌بین‌قاره‌ای،سه سوپرجام‌اروپا و ۴ سوپرجام ایتالیا از افتخارات این اسطوره محسوب می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26857" target="_blank">📅 09:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26856">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNJMBuqEYCByopEXlQgfh6EWeAYTjJstykQm6mxa9KYdeyiJlfxcmxgJ0U_G_fKWrV_gKk1ynLCmUg8hgcg4J6NuVC_mqTw93dPjZjPLqkUExuYUmhNseDSVrbRqKPI6b2zSHbg-ZjWCV4CZyR_Le3ZC_3oqPZ6jDJ_2ka7i_dMlzkikfaQbqD97Ao2JY0pt1aLB6gIf5On33WSdzwwsx-2aQMwV8eutmreBCaH_pIxIEIc-Q7xbMeENeAR9EX60P7QlYsDNN16yV_8WWNv9kFpOiDCf7WEQcDL5V-KFR6L85Q6otB2fF1oBI11RZcW5yk8kJr7TwAtNHPF57nlJEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ریکاردو ساپینتو سرمربی‌سابق‌استقلال‌که در روز های اخیر با عقد قراردادی به پافوس قبرس پیوست با این باشگاه قهرمان‌جام‌حدفی شد. از معروف ترین بازیکنان این تیم میتوان به داوید لوئیز مدافع سابق چلسی و آرسنال با اون موهای خوشکلش یاد کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/26856" target="_blank">📅 01:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26854">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UJVeainn-FWmKC8I-O4tMR_Tl9jPj6qedQUm-xcTHW2AyJ43dNCy8E6jxVsh8E797pMWFfS6IBma8aws2ezSpQkBFA2Q1aMNwyB3KmHhaS2TyLuMu4K2cDVcaYMY1HsaT3YCIx39EA5R5UeVxOvZpNpQULgJgWEe9NpVlI8FzdfPpkNR1n53W7nkgPgJ6Xdj8abkBD-8v_h6tIyimMxSqjk10ax40GxGB7LgWlsiPyU8CDeDyvGyvb1Sxs5HDoSg808_Hn3KN4x-liJegH5rHiYvTe9j3YU8AMn5_dq4REBQwi6OJ1pYKEd_9XuqjGMAlwktMwdWCRTTNNSX5YJ_WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D2FJO8gTyAtpUDhKl6weu9h-pHYMQXlzu0KgaZYh9aIDO_CT3HP3xbzx8m0FXWypJhJv6MmTNZRNxpr0bEDupDj7lqQkRg9fCXkMEzAQd7GF3h-fpWozfjxS8j1eApVjgFg-8kFbv9w_pDYJ87095lIvJ0P2M_UtDVS2QO1slQSkhLCEDqahYIB9sOpT5VG3ogkM3BsB_m32T8gMXn5LJcctqhUAkCDH60e9WUCv6kcfRq6BmLelA_MZggcyFJEK3Zm8ZsgToMMND3ezKkrwGRFlKD7_kUDKe9waxQOLuV74pMYH_TENtHNjDT5-ileiYu6q5JNXK62IpzFgnYTa2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌وتاریخ‌برگزاری‌دیدارهای‌ سه‌ هفته ابتدایی فصل جدید رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26854" target="_blank">📅 01:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26853">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ek2NR4ppQNePbmWhMcxlnUOa6uOd3iR8fsnp0_U7gCh6aNfpdTq1dzDPeR9DNSG_ZTFuTxJCeMy5yn8XMnk1Fh_ZgVcdPglH7qPH1OGAeyQoOk5IRlTJoaduPrkygmc6QEWSkR0rLsagmiQq7ZDstSLS1t2r3RCWlpCWsURUpqn_BhZi_tQN_sSYkle_JpsG2hFEhk8Cy9g0luJ_OPh8X8r11Jt4SoFUic1F4L1zVFHrp21Z8bbkvkJUVCjGJKzwCjUcXyWne7WBdrj4-k0k2hCl6Din5Tv_pfkuZAn9BbarQqpCmRw9XrShBjEo22vBFShvCP9DmiP_GpD9jvmd2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه‌استقلال امروز پیشنهادمالی جدیدی به رامین‌ رضاییان داده‌که 15 میلیارد بالاتر قراردادیه که درنیم‌فصل امضا شده‌است. باشگاه به رضاییان گفته ظرف 48 ساعت آینده پاسخ نهایی خود را بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26853" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26852">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mehzp8FUMbaY2Ar6FSU0f6AWvYZrrmbx7MifV8uu91gA0ut8CW7k5CaI0_i_m2El2dk87BcyG0dvAiq9R2TqRNxdmBdWzSRK-xODB2g9sytjIgHKb9pE7dAoo7LMt_vOSAohyvpFD-BlmlCsAM0VziTmQEPsFqvoffPTUaX1eGa1w37P2uqxXr3H-OtMQ3y6LG7Q2AdfVPYRytLnb3JWZkwRQT-rB8Jh8BawnvSWvJxbb2hPNhxr9rqqQXjenJ4xnagCL2bMEsClPNaiMAgsPoReFkPTYOAADpRirZ2oTm3J2idHneSb8rmRx9sY5NLkSEhV03zU-bfLjUaVph5OJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل…</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26852" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26850">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S35F67D3gVR7poj2ORU_0uQeMuX4dhYoy_bX2BcGGCpVmuWENmGa58ABVbKUrvebB0catB7twatiroj_uI3ERCqy6zdUZRCkrY1ond32N80VFSi3s56FXDK69SUjPJQkNghLAH6K7Vlz1m-uUorIcaPvt5qGHvG43dcr-_L_kLC0muHModhjvn_uLye1xFnXV39WHeB9GmaEgh0KnV6MtiimoGXIpt_hC0WctX8lGKr_7u3Yj3vYfS32V1kVZOlTV5RrWIwfonkVvwF1h2iuXChBqidtQVBJZU3SmF0dikotPkFFGxLGn-ppSPM93-ZxJDWneaGaQWt4QiAXm3da7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی پرسپولیس درتماس با مدیریت باشگاه پرسپولیس‌خواستارجذب عثمان اندونگ مدافع میانی 26 ساله‌باشگاه‌اخمت گروژنی‌روسیه شد. مهدی تارتار از بین ایری و اندونگ یکی رو حتما میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26850" target="_blank">📅 00:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26849">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=aKQXajZAZqCw-7m1wX_a2TCSWQHTlxBlahjpwWrCv-nLSqz35AYBpjVCi1wn85d-ZrwRGx6Lpp1agP2PGwMbJYCGCmUrsUiHihtWq0P4jEgtNYWnZmEPfOL7HZuekMfTWFkCQr7a8E2xFwnkQ1XvPXS6QA5m9NZClQpcsqDH4yFpaNCpn18E0_1xz1YoHL6LTGqf4AhfrsKW_6dDecsUNIi_H4He8pQ-r9BqC8qdkI2fiG6zijWIGqqkDSsddO2EYOLi2b-KbndmWCeZELzwY3SH1IAyfT8qafjTn58YKHWwzlpLcgTHAw2qUZDXlf7ouJhJjc43_CYWW5xpzaHHWYpk3vZzBfgY0lV8UOK0Gy0ABmiNcXNvXbk6wIN4w2nAG0DHz27HZFmXe9YysHW9JxFFADZoozXjjy28IgVFyg0_Yl_QXCw2ALBUMW-Lgl3lUnw_ySCjXyes1brH3ILgXyR7xx09m7IdNV_8zxxDT8sM9JF6fX4286EMufCsKZonYC026oMa9jLrsHCgbGHklvlRk6fElC3rslN8DUaOkD4HF6YnnoAochxSlIH0WvyM1u9ykjnLRFxBDxuu9_rwYEb-T_qm5KkUmBoAzxtAJ5WsDtcVCp4mWykAeMnwxv0pTuJcLUx8KT_M9mnzbQhSm8jsbzkmrnj1abNH8GRD5Ec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=aKQXajZAZqCw-7m1wX_a2TCSWQHTlxBlahjpwWrCv-nLSqz35AYBpjVCi1wn85d-ZrwRGx6Lpp1agP2PGwMbJYCGCmUrsUiHihtWq0P4jEgtNYWnZmEPfOL7HZuekMfTWFkCQr7a8E2xFwnkQ1XvPXS6QA5m9NZClQpcsqDH4yFpaNCpn18E0_1xz1YoHL6LTGqf4AhfrsKW_6dDecsUNIi_H4He8pQ-r9BqC8qdkI2fiG6zijWIGqqkDSsddO2EYOLi2b-KbndmWCeZELzwY3SH1IAyfT8qafjTn58YKHWwzlpLcgTHAw2qUZDXlf7ouJhJjc43_CYWW5xpzaHHWYpk3vZzBfgY0lV8UOK0Gy0ABmiNcXNvXbk6wIN4w2nAG0DHz27HZFmXe9YysHW9JxFFADZoozXjjy28IgVFyg0_Yl_QXCw2ALBUMW-Lgl3lUnw_ySCjXyes1brH3ILgXyR7xx09m7IdNV_8zxxDT8sM9JF6fX4286EMufCsKZonYC026oMa9jLrsHCgbGHklvlRk6fElC3rslN8DUaOkD4HF6YnnoAochxSlIH0WvyM1u9ykjnLRFxBDxuu9_rwYEb-T_qm5KkUmBoAzxtAJ5WsDtcVCp4mWykAeMnwxv0pTuJcLUx8KT_M9mnzbQhSm8jsbzkmrnj1abNH8GRD5Ec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل فردوسی‌پور:
🔴
اگه قرار بود که من چاپلوس و دست‌ بوس باشم الان‌صداوسیمابودم‌و نود روداشتم. چراباید دست یه مسئول رو درمقابل‌جمعیت ببوسم؟ چراچنین چیزی روباید باور کنید؟ دست کسی رو نمیبوسم. هجمه عجیبی علیه اومده. همیشه کنار مردم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26849" target="_blank">📅 00:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26847">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gM8BAU5L3GCNHV1sUIKuRHw0miFNqYmsmCSYDb5BCsS0x8BZgr9Y6-dbCVw0LuAeqAlC--1hGusHxIXwgSW_E8UMdTEPtvAaUR3V6W78tgnoRThxnebf6z1F4zpBPQie4o14sQbBwIk2qaac43aVUBrlmb04ZjTtaDar6wpAz79PsrTevPvjxjSnqN5awS1JtJ-ZviuYL6GB79F6F1m6HWNcbZ19l0rgPJOvK5B9XbwLI9s0UiItaJIqK_wUSM737bgizNZQiBcCBKQCwdjQNzokjen4Xa0Un7Nx2ih7vbuDr1uNHjeE7xHoTGTAJgzIJjVXYuaBXy1mtrr0qOzNSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
بازی دوستانه آبی‌اناری‌ ها برابر تیم سابق جود بلینگهام در لیگ برتر انگلیس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26847" target="_blank">📅 00:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26846">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9gZyBsWbUVPRMU95CduZIA1LEnYzN1HLtQnsLdXIg07TBb4xKe9AWb9m68AKszf95m0ST_nLQEilSKTEVUbYq65-X6QF76hpj15aCegxcULayOjuPmbiwk3eyQqPf11YT1J0coCBzDI_YnD4yMluetFzcXE-Sd4r39BG7y1XlBKtmjQO8xuLeslpxB75Gyou5ggXLVB5rRY2k1knEAxF1nTSBVvAzkgVv0z6ixJDO61-EhPbUMaDCVF6j0ih3qkpPulFgO9KwCMNAxaSTKzyD_NNmS6WOhfCdc-fqrbSMj3foE14nCa0N3BnJ63xb9EdINxS9DM9-N6XSATqFbZ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ کارلوس اسپی مهاجم 21 ساله لوانته بزودی با قراردادی 4 ساله به رئال خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26846" target="_blank">📅 00:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26845">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfpdDeyaIekp_S8ucHIGXJswRnmttTI0-rDbLHQE2BQsjYQB3hd1lTx5NI7nh8Tc8ZusRtzIUQa8BSsBNZm-5ijQM-M1EdFOE6B_y8h9vgP2oV_rbBXmlHH7_vubSf7LaV-rNyXOJtu37Q3lXrHOKVLUu0yFdyDEtzm_Q4h-7F4Yh_Bt9dVT0IKVdZ0SV8SwubsFpCMjtQeC9_v0jDb0FpdCbsofkql9wyRQwoFsvbF_ugC1CFUFNb_4slwvkKcboDyDxbXc-15iL9BLPo7vBMqK30lWSoWBu4U-RIaOJ36PDSsoFzPmmJYWs_OX2mBcPEWTQX3jfGpnkGP6vPpA5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دو گزینه نهایی تیم‌پرسپولیس برای جانشینی میلاد محمدی؛ اولویت مهدی تاتار مدافع جوان گل گهری‌ها شد.
🔴
باشگاه پرسپولیس بعد از توافق شخصی با امیر جعفری مدافع چپ 25 ساله گل گهر سیرجان؛ امروز صبح با ارسال نامه‌ ای به این باشگاه خواستار…</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26845" target="_blank">📅 23:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26844">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPvUUPOg3vwDJVe0T3jnyji167PyjpYHT8uYU7o8_8kmNIo5S9Jn4MtG5Cs_sDK4n2Hfvsjjbab4wVyouLs32xzYt2DU7Pny9W5GDwQpiTt4RBGAD6c0OGqhqoX25P36dqo8RplL0W1VwU2KGxvuHWyD0eMfWUtqrtTiZ9R_6de7pnYqXdHBf2hx37JIips3B9d4vGcfKTTm9qGEzc4Mjmu2ONF6VFcjG9VsF7B2KtGviNopv_cGM8fgDpZgd-FfnJ9NfkvB53qQCbXUvSGbnaX0QtjR2tVWfOJVjbSSyTwq2dfsqOspij4tVOcH0GI2AtW8d4UYt0fuvkxgjronkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل…</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26844" target="_blank">📅 23:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26843">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/io9JgQRuAuewO8DHc275LbNiBhueLWmwD36V_yqWvyABPxAhpHWNIetyLWC_-h7Ox8HNWztXN_F4RDCHpFtPGWU8cmOK1RnRVzGJZACy-EO1ze5bpFpYmwN6Do_yOuX3KV7U4cZW-0NWDBk9Cz5Kscmn1B65fKG1SHjqtKVDSbyR2GPre9ZhudegdHTSMDbcZ_qnFw0lGBCtAlQPQEcHloKiveEBlO94e0pIMJi8mGypAH3fcSVxvQ26yrK3s5PCVgLrUPvfykf_h_qEr3j0pnEvOcs1Uq715UP0ec618jBSFZI3L_oq3Ohh00DVGyfo932c52y5BahwzratklY3WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی رسانه پرشیانا؛
سعید دقیقی سرمربی جوان سابق پیکان مذاکرات مثبتی با باشگاه‌صنعت‌نفت‌آبادان داشته و احتمال اینکه بزودی قرارداد دو ساله‌ای با این تیم امضا کند زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26843" target="_blank">📅 22:49 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
