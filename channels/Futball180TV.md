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
<img src="https://cdn5.telesco.pe/file/s8SpB_CmshFs-nxdSTGTlUtibTgEGp6YFOcJpmP1o4qdKfImRNTy7T3IgbK1GHtfZxil2oCx34oWUnNhUsJzYD-SxEMdyTmh2Vjqseoy29tjsXtDRMA3aYjQiAXa6ctKkEn5jaKUThwZQ0lzYlZktxVyZoGOCaQ49NJq4fSrRfv8HIXtDZxvkmoRdtWmw0c4iHYjFZDCRcar0IVwZAc3Ak_llMIk6gMTKk3UR4c5KWFug2S8yUFO5-eiBzawdDNVtWhDusO27vReKX_ztbfhEyHzeoaWLTUk4DyopGmjds5SQoSCgKUOn1FNI4GDWryX9ixllNN3aH2oZVV9iIomDA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 416K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 01:20:48</div>
<hr>

<div class="tg-post" id="msg-106324">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🦖
2 چالش، 2 کد مخفی، 2 جایزه 1$ در سایت بین‌المللی TREXBET !   فردا در دو زمان مشخص، عکس‌های چالشی داخل استوری کانال منتشر میشه؛ اما کدها همین‌طوری به دستت نمی‌رسن…
👀
🔎
باید با دقت بگردی، Promo Code یک‌دلاری رو پیدا کنی و قبل از بقیه داخل سایت ثبتش کنی! …</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/Futball180TV/106324" target="_blank">📅 01:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106323">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKh0Y1eNh9pf8Znx6OQj2XOM_6qNEc2SfI2q3eTeHTCSI6uhHfAgwav9VD4W4cGMO_gvYaHFNPvqaykxsuf_9cawJLY95iNq698c_k_c4Ix39tfgrV-NpRqg99xKINJHpx_uKxPYDFZHRf2rHDSbOhCOjVFmGBKsoYlLMScKDS2mUTWznJde9lRZSuMwOSLilzoWjl9mPYZCwEvnVosLyDXAX5zi3H0flUrTdIcEsvR69EAu9DhWYTWyQHCJnJP2EjU_AwjEdlRPnVNXKphMZg2vdnCIJiq036uib8hpoHWYEvEkKUTxkAHUdvmO1Fz4Ymk6Kg13c2ODpfJr9rOncw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
2 چالش، 2 کد مخفی، 2 جایزه 1$ در سایت بین‌المللی
TREXBET
!
فردا در دو زمان مشخص، عکس‌های چالشی داخل استوری کانال منتشر میشه؛
اما کدها همین‌طوری به دستت نمی‌رسن…
👀
🔎
باید با دقت بگردی،
Promo Code یک‌دلاری
رو پیدا کنی و قبل از بقیه داخل سایت ثبتش کنی!
⏰
چالش اول → 18:30
⏰
چالش دوم → 20:00
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/Futball180TV/106323" target="_blank">📅 01:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106322">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/Futball180TV/106322" target="_blank">📅 01:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106321">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pj8-yzh08oWchO3F9RIQWFPNSfMVnBjA5GgG8ExYqTjt5-afhDTtH4uRv4xumzVYXd1n8P4MWEQNjsFQ6U5LAiaLgF-Rv_938pJq5oqHFA72cS3X04_gAq_VKGpWH9Ro6V_JDhPkHm5yJ7zcpIjWrvHtqPCLyOK8T09JINOExMFzviooUAK06r9VbTJIWhM9b4WqE-brf-1dvuRFtBwx6uvXCcKzYh7m5FeECWzd3SpMsQuRG-Q4r6l85ZHM2YWnldON1dAUXxFS_gFAJDebpowz5sQrugJQHOgxHDiPrfF3se3MeOzmw9B3ykzZ1-od6K5xDZ4eoBi98eo3QiNHaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌چهارم پریمیرلیگ؛ آرسنال همچنان درحال یکه‌تازی؛ ساندرلند هم مقابل تیم آرتتا زانو زد
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
😀
-
😏
ساندرلند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/Futball180TV/106321" target="_blank">📅 00:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106320">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fir6rL8COZSpg9jBsE_dCqG00c_u923dgnLr2hIoTaD7L8g51OQHmzzSP9b1tr4vNxFjmqKf1wZOi5tNPVPcFtmQO6zWP5ZepdtZ9ZqpOtVpPxgyBkeyFnt6umqF9nRAOJ_vENZ1u2DOQRyUq55TPFtru-YNmRR6AXuAoghkN6r_dgRf4RNnflqm9I1PiEzy_XrRU2Sjw0bl7ivCjxrQWLjc7Z8ZDNkrJhJ_MY0HojeQ5jn0XQJgO10Yb0i9AYZVpp2wCX-2RB3n-HZeHlAXOueISj9bCNLZumv5ks7aZ9S-egxp3qzfDSX9YfvRkwVDpyYVUgvgKFxtPvpdBYmrgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
کیلیان امباپه با رئال‌مادرید در تمامی مسابقات:
🔺
۱۰۹ بازی؛ ۹۳ گل و ۱۲ پاس‌گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/Futball180TV/106320" target="_blank">📅 00:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106319">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTFtzg1lQleQuioZbcXCMZEu5ViBWD-JnaAGXKf7-xJhOJHW6HdZSHGx0jbbB422DF1ocgNdy-_8kbKZu0yW8sA9ivbXZzAn7PeYbNSvnvYXrkYz1gqjXBF_-NrKu3TrIjYH-JF-CSSiLGoIeH2fgOlpNLUXguC--6SIIm69u0wYi7OGpPn7YbGnFJIHHjqy4Fz0takm7nwXUs4kfbWX62pBHDEFm6y2Mh8BxKBTfJiUp28EzlGoRwLm6CepkH1Gx8bq28xP6iAnGXNnXHNI9-IBxHif9-hKV3xDp3QSbIokbUon878ps9yOfunA-wpNxDLTiY56MFHCAT8NNRaxnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
گلگلگگلگلگلگلگگلگل برنده واقعی توپ‌طلا</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/Futball180TV/106319" target="_blank">📅 00:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106318">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aiU8Lrck6PZxOyHMXk23uI63J1GTBw4qMh_oq_tbyChPaIAQtTP_qeq1ckEl51BPvfD2cir9QMJG9-k7v__De5zW-xAVWMY06DJCJdeKE9PrWntVcgmUEK994B4iOY77xFnzQ3_NjAkWwmz1f5mYKTvfUTu9Zfgrn_oZiMG70JhgXimeMMbdwP2wTeOXdwM2yDmsdkLG7nCpEGXbSM9LZlYuOVMOgahnn6KG1T1g9LI8BYStttcgtwFRJp2G_n74fY9uAYAhwoySmbgwDndkc5mJjuUmasHZQDinXH2y7qoAvAp8q9ujmZhcugcrPFVoudSM5j1fde6-nbLvkDsOZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌چهارم پریمیرلیگ؛ آرسنال همچنان درحال یکه‌تازی؛ ساندرلند هم مقابل تیم آرتتا زانو زد
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
😀
-
😏
ساندرلند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/Futball180TV/106318" target="_blank">📅 00:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106317">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0f6e034671.mp4?token=idX_bdgY_iKW6y-WsDyY2CXXGxVyVLyBQ-bVIpDrrEAOnLBQuXajQQxhOnucP5vf6Jli7KeP3iaQTPnWljfyR8g-hB4HcEIpUFyp9Z898rZ6ioiNORl0tTH8hk97or-dpWGatt3WA1HMNFw14wonmSlwaloVO145Ml8udNF9hby4t1Lb7YelOfIjeXISQETqTbGAb_u_7oI276uvpwcN3GCBzzi-HUl9e2JOK4sD6m6AVwz7np9OIIcEYrMAo2Y90SeGDiPAlCZPxSDIQlA5UfvY5UCZQJHebUxk9xmiGWQ1rjWcFIq70DCOjkvGPPLjuLeZ6ru-yrxJCzqFxSGhzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0f6e034671.mp4?token=idX_bdgY_iKW6y-WsDyY2CXXGxVyVLyBQ-bVIpDrrEAOnLBQuXajQQxhOnucP5vf6Jli7KeP3iaQTPnWljfyR8g-hB4HcEIpUFyp9Z898rZ6ioiNORl0tTH8hk97or-dpWGatt3WA1HMNFw14wonmSlwaloVO145Ml8udNF9hby4t1Lb7YelOfIjeXISQETqTbGAb_u_7oI276uvpwcN3GCBzzi-HUl9e2JOK4sD6m6AVwz7np9OIIcEYrMAo2Y90SeGDiPAlCZPxSDIQlA5UfvY5UCZQJHebUxk9xmiGWQ1rjWcFIq70DCOjkvGPPLjuLeZ6ru-yrxJCzqFxSGhzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
گلگلگگلگلگلگلگگلگل برنده واقعی توپ‌طلا</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/Futball180TV/106317" target="_blank">📅 00:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106316">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اونور آرسنال دومی رو زددددد</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/Futball180TV/106316" target="_blank">📅 00:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106315">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">برنده واقعی توپ‌طلا دبل کرددددددد
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/Futball180TV/106315" target="_blank">📅 00:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106314">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">رئال چهارمی رو زدددددد</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/Futball180TV/106314" target="_blank">📅 00:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106313">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jizIo77QJYHP1uClSeFu27dvjUJBpiGFD64Wb-cBBQiIcWtqOGbQEhxRNWMFzEP0tA_lfBnoqgs63moqpYRHQA0oSrqx4wTqOh-7RJite6gOazKZbkzd8FkUJmBV7eQPdBcmhYWbC45otrjhnRFAtYa0k2mPaKgSUC57ZEAL8oFxecupGbvRcLjOgrrODyOskcOQCZJz78jyABnls4QBFnv1IE28EdfOWjaowStu-FcYrNp1B89zyB7l5GgyDR7KgvaEi1vaDhngLZEM4cXkWJT8EtkVb3LOT-41HmDb3xrjPKFfse51Sko5lRBOZgmKJgDTRGcb04ElFkC7ib1_hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇶🇦
استقلالی خبر جدید براتون اومد؛ مارسلو بروزوویچ از النصر به السد پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/Futball180TV/106313" target="_blank">📅 00:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106312">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q42ODp1aPT_e5Vu4SWmoE2AGWtw78SXVDWlRu399mfAILLD2aVrbr3Yvs6wAJjaIn0xXS6IunMqR4HXn5A5yWWFPsScsDzYLHdBEpW0AOKk2BSAjI4mXazIlZN-v86jWXmUhOI5rrx_flyGDHZrl8nG6zxCWYb8-AcpHIvkmFwcttLUbdiY_VkslKCWGioclQqXlOpeNdS-10aMF3XghEqH_zaawHG3DaFisYSHDMChYTGtsLaggcofvgNkVYfUJrR50H4UiZTT-Why0pnp9yodQwEoiK0ZlrEJHjPjTdCtMtbTm-JH1X6hyoVdV_01_n8bDBdfrtkLck5YvgP-4Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صالح‌حردانی چه دلبری از سهراب میکنه
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/Futball180TV/106312" target="_blank">📅 23:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106311">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d53729e95b.mp4?token=DIvcKXLxXzSbMF85eBHzNBZVywD5shVa0Q-WgeEA3vSYKYt_f6WPTbW4bfWQ0L1LPWkuxYnqNyxoc8HPR6qX3ZsRyypQNdvN_YevExPwie3WEM0MGKADCi35oHJJzThGxu7DSgvmFjSyVMVA1fEjDLuamJ8V63GUcQHQaHbZ74wkAmA6bnitiozqaIRPoh9z-C88WmoOIExcQ-FDMXq2i_AEXLsuZm7psDAdOYTZsieRWOFyotuuoB3iLFTvfN8iDL7kABprutzp9HSdOA937SjOxy8u1Yp-YZmtPTCDTd0_tYka76XeD6HozTUkx4Amk7IOCvZHololcTl7_7DHDA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d53729e95b.mp4?token=DIvcKXLxXzSbMF85eBHzNBZVywD5shVa0Q-WgeEA3vSYKYt_f6WPTbW4bfWQ0L1LPWkuxYnqNyxoc8HPR6qX3ZsRyypQNdvN_YevExPwie3WEM0MGKADCi35oHJJzThGxu7DSgvmFjSyVMVA1fEjDLuamJ8V63GUcQHQaHbZ74wkAmA6bnitiozqaIRPoh9z-C88WmoOIExcQ-FDMXq2i_AEXLsuZm7psDAdOYTZsieRWOFyotuuoB3iLFTvfN8iDL7kABprutzp9HSdOA937SjOxy8u1Yp-YZmtPTCDTd0_tYka76XeD6HozTUkx4Amk7IOCvZHololcTl7_7DHDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل اول رایووایکانو به رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/Futball180TV/106311" target="_blank">📅 23:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106310">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/152a6c453c.mp4?token=VDDwg45HJ1d8ZM1M7fEqY9TYbSkQGrVBEGJu0FA6YQWTTnIbkvvvk5y6mjfR6UcOf2eNa-pkRx6pygqRXrrgTUECgY3keREwIhhjgZb3RccSkgXozOKg06sZ7O_RsPQzoOpARngmbKi7Go-b8JRXIZAET7o1Jd2qGlnHm6C9p8ATngCLiWYGrbp4hUjB1FjHXoyqjXVpqqE5uEpMVm3YUxk6gJFoG_fSET62cDbItzSuMiBYonUMQ0D8XGHqkVXWm4qAHT8AYXhOpFzdG-HZteHmIKt25-I3WJIJOGFVOYmuXRP1cDtUDRkpBtBAjlK_CJXU4RR_QHo_PthbpoUelw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/152a6c453c.mp4?token=VDDwg45HJ1d8ZM1M7fEqY9TYbSkQGrVBEGJu0FA6YQWTTnIbkvvvk5y6mjfR6UcOf2eNa-pkRx6pygqRXrrgTUECgY3keREwIhhjgZb3RccSkgXozOKg06sZ7O_RsPQzoOpARngmbKi7Go-b8JRXIZAET7o1Jd2qGlnHm6C9p8ATngCLiWYGrbp4hUjB1FjHXoyqjXVpqqE5uEpMVm3YUxk6gJFoG_fSET62cDbItzSuMiBYonUMQ0D8XGHqkVXWm4qAHT8AYXhOpFzdG-HZteHmIKt25-I3WJIJOGFVOYmuXRP1cDtUDRkpBtBAjlK_CJXU4RR_QHo_PthbpoUelw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌سوم رئال‌مادرید توسط جود بِلینگهام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/106310" target="_blank">📅 23:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106308">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بلینگهام هم سومیو زد</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/106308" target="_blank">📅 23:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106307">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a23278bfb7.mp4?token=p5GVtIN_eovMtiTUNHRCA8xN5SQHnRxZY4gJD2w2em8ipaDNB55k9dnDybfCSAu6m_zkv--5UarKDMmfQyALBOIj3voS-dQMGy6gl37LoRdZB33yqq0aEb0zBguoMNkcXzzwk6pY0-xz5ZTssHMLCSqDXPVH02bQO8YK8-2ZioYi4rJPya3G5t2p_78ren8mzFZtpgZSvX46fkcxkWLetcTpSQxYSFs-d83e2rBQSNW619MI2pszNxMSTvmCkppE33klA_FsMKcMMJzLv3iJnu_XjcxrD3ZZmt8HgxRgEWqDbeaSbunKhgx0DMuEdPa_WbdJ-A1aFDpeww5D3lgKUIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a23278bfb7.mp4?token=p5GVtIN_eovMtiTUNHRCA8xN5SQHnRxZY4gJD2w2em8ipaDNB55k9dnDybfCSAu6m_zkv--5UarKDMmfQyALBOIj3voS-dQMGy6gl37LoRdZB33yqq0aEb0zBguoMNkcXzzwk6pY0-xz5ZTssHMLCSqDXPVH02bQO8YK8-2ZioYi4rJPya3G5t2p_78ren8mzFZtpgZSvX46fkcxkWLetcTpSQxYSFs-d83e2rBQSNW619MI2pszNxMSTvmCkppE33klA_FsMKcMMJzLv3iJnu_XjcxrD3ZZmt8HgxRgEWqDbeaSbunKhgx0DMuEdPa_WbdJ-A1aFDpeww5D3lgKUIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم رئال‌مادرید توسط کارراس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/106307" target="_blank">📅 23:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106306">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2689afdf46.mp4?token=LppqXmVlAxUgh1z0gMHNxaxYsuFKtFP8TMnhraLBUH_G5myz3Im4NBfM0UdtBGWFxZM0Foy0S4F9vA201X7XCYAHlWi-96M2Rk9wXa7WgP3Iy8bDOeeaSVOfov48HvSwF_YQSfxSvzp4fH0AxwEMefMcJMk4AkZ-sYHdw7w8hqCf7XM4GiROVcU8OYRHcPRaF1FyGYYwxumeYm1C453Bf9svKpcNpYSmrNu2ay4UmekBAsCfPVnlhVP7Xu991_AvbwzgakCbIGeNJOGZ_od7ZCUBWTqACGGPuR-g1MCZSLr57_OlZhC08_h84BVmG-SfBnihUfkJhI7xGT2YX3oqdg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2689afdf46.mp4?token=LppqXmVlAxUgh1z0gMHNxaxYsuFKtFP8TMnhraLBUH_G5myz3Im4NBfM0UdtBGWFxZM0Foy0S4F9vA201X7XCYAHlWi-96M2Rk9wXa7WgP3Iy8bDOeeaSVOfov48HvSwF_YQSfxSvzp4fH0AxwEMefMcJMk4AkZ-sYHdw7w8hqCf7XM4GiROVcU8OYRHcPRaF1FyGYYwxumeYm1C453Bf9svKpcNpYSmrNu2ay4UmekBAsCfPVnlhVP7Xu991_AvbwzgakCbIGeNJOGZ_od7ZCUBWTqACGGPuR-g1MCZSLr57_OlZhC08_h84BVmG-SfBnihUfkJhI7xGT2YX3oqdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پنالتی امشب اسطوره توپ‌طلا امباپه
😍
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/106306" target="_blank">📅 22:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106305">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ریال امشب حشریههههههههه
😍
😍
😍
🔥</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/106305" target="_blank">📅 22:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106304">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کاررررررااااااااس زددددددددد
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/106304" target="_blank">📅 22:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106303">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گلگلگلگلگگلگلگلگل دوم رئال‌مادرید</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/106303" target="_blank">📅 22:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106302">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9x1sACUpSGZ4qqngw9dAPtCj4MFhOmlsCnOO96viR5E8OHf7NFCn8H62mrJKBnF3SpWPx8QKbLYWJGwEWhZVMf2jJwz3RrlKx-AEQXDwNgqgOwjFkhFwVpDsNH9a0nYfVzOgcx0UVO8PdgzT9-CW1fY5k2fooThp-48mq1_ZgE-FZhF-czZCkoOUIMNAoTeRROgN10ITgT_sKX6tYlK7OfdDBh14HTQgPgK3yV4QAqf3A8BiaOAtwz7Sc3kig7D_pf0WWsZbLhT8bkElKV3JgKxxSx9bp7A7hIcToLLUrcDF-TTv202p1kVO2yYHyk_ONEiN5JPTgQmismdy8L1Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده واقعی توپ‌طلا
🔥
🔥
🔥
🔥
🏆</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/106302" target="_blank">📅 22:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106301">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رئال‌مادرید زددددددد کیلیان‌امباپه
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/106301" target="_blank">📅 22:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106300">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گلگلگلگلگگلگلگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/106300" target="_blank">📅 22:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106299">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پنالتی برای رئال‌مادرید</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/106299" target="_blank">📅 22:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106298">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTSbbV5KFDvWNQarFKZVo2NOQ6ewZCTYdI3otUZIgOBMA_eV8Ft5wo_Gv9UvcMnlhVtRGTWpUVTLjXpTFIcLvBhvaa8-UNxWnkSqg88SbmbyNe6kRQ1YqOSvnzpbhVqDnFJFZE67sPbuEp7LrCZCi6t2RnR_m_CKjBtZdyfIndT8EJBnclbR57MBv4ip_9wBKFTxOK8psCeqgXF2nH7wUCUyKweU1bcb3BvUtzUIs8bnSfQV6stbk4vGazP9y0JH8Wsj7IfWqukD8pj2BV7WaGsfYeHSCK2a0BnXhuCK8E52M8-jHYWKdH3K-JjExqM5Q0vxptou270dmk0k7HL3MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
شماتیک ترکیب رئال‌مادرید مقابل رایووایکانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/106298" target="_blank">📅 22:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106297">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇪🇸
🇪🇸
🇪🇸
یادی‌کنیم از فینال سوپرکاپ جذاب اسپانیا در سال ۲۰۲۵ در قلب عربستان شهر ریاض!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/106297" target="_blank">📅 21:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106296">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBo172705bT2zbV0Sj3F0KKht0mre5b3H_I_9HrGxMff-qh45L5GCMDQA1h_kzQyeYJIIZ9DyVGttkE6RXORYWUu7fG5kkVtdoriE8tVbiwZHzpnvHxuOVfdi9IP25rFRvcoHheZK0N3e6iSgfBEsBHbtQZyz36FQut_g7lRoJe52rTIdRBVAYuVVDttXDbfCrYiUantaILz50d50_k88UflA9emDiuDvBE0F1PubWHDiz8MZ4Xb9qUowB3IjYzhcC7EFVxIWzHCuBh2M7x4lIbRI_xqBEWEUjh7Y-jN2irorCQme3SQAzGbz5zTHN9KIxTgB3Hgxxua2DQEXaqBWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇮🇷
🇶🇦
پوستر السد برا بازی مقابل استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/106296" target="_blank">📅 20:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106295">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOz2XwwmDJ3RUsTlnoJA0sFDpuSwjCpne0vR7WALwLZ7f4_J3H6mvt-rDbF7a9N9BuJP0zzIYr7AxD1IPn7CIyMNoE3-bkPy_-o_0z758IP63hMj1MfnV9zrOlB786PoL4AlA85Co94dp9zcNo_1JhQk6mvbBRBkjtq-gyJtV0hp2i_e1qATNpNZ1sSCO-_j_qBYpfB5CFMcM49kS_-Qm4ns0RIQqKnkkzz8X7lC0Q6vT-4s_YWPQQ9bBTUq66MIQAzDkz7IGeaMVgMO0wp5fMMxvuPMWK_NMgVPwJX5EoLmt_3amb7MCOhQy5WSos3D9FPdlLt9MmAaFqOelFPI0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
😱
قیمت PS5 Pro در ایران به حدود ۳۰۰ میلیون تومان رسید
🔻
قیمت کنسول PS5 Pro در بازار ایران به حدود ۳۰۰ میلیون تومان رسیده؛ در حالی که این کنسول هنگام عرضه در ایران حدود ۷۵ میلیون تومان قیمت داشت.
🔻
یعنی قیمت PS5 Pro در مدت نه‌چندان طولانی تقریباً ۴ برابر شده و حدود ۲۲۵ میلیون تومان افزایش یافته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106295" target="_blank">📅 20:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106294">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReveQs77sKCxVIKZ3fpffNtNJNlu53is-4qP1c_wymw6R8gKmY3eubVAocIu275wk9Ie9BWqHG5aMuTVd1vI02Hp4W75vecp4NPQEjoBdGqUwvZjXFP-HwADNDO4zYfob67irFioBy-uaBos2ntYKLWoGaMY1jDWG9WXIwf332YC58yFxcgELqX1W-MwhU7c02CX6E6nbeZA8xowGskgwgGlJKbMA6xIZhlw7V0Vrs1DwQjF7aOxup6aK9sxWnc_5yD1uGw3o7kLuGy1HgY9MM7Ecc9GztvyCbVzXI5zwsrEqxHTz0YqyFUrZob-IQphfu2Cj7Xpzip1yfyJbc4HzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
ترکیب النصر مقابل الخلیج با حضور GOAT
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/106294" target="_blank">📅 20:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106293">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMUmauHOnW9KsuTduB6N_khWFkDVx8OMEpLcT-V69UiaDaGoEI1FRMLJC_bV8zhfl2vjU8g1NTKmnAuMwo4qbw2ZPaAjfvSwwf5K60WA7ILThBa6kUrBME2a0Pzt2ED49xu3CcOr1104LxNv-gLOYzmoD8sgweEGie0glwVIaV28pymOWFOX4-Al_v1_-1TpiuAsl0EJEZngVxePtoJbRRQGJdBke9sHyhmHU36fBrqSAc0wpDuWqvjgQmrEO-bB1USuUou8x7TqWVoK-x3hUO4Vw5Hak--zsc93ne4jrvfoBdBPrRLcjEiKV1Jc8PP4H2Lr5JrDrT5rH-q_OaZtSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇶🇦
استقلالی خبر جدید براتون اومد؛ مارسلو بروزوویچ از النصر به السد پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/106293" target="_blank">📅 20:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106292">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
▶️
صحبت‌های‌جالب یک‌بانوی ایرانی شاغل در آکادمی باشگاه چارلتون انگلیس که بسیار شنیدنی و جذابه. حتما ببینید از دستش ندید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/106292" target="_blank">📅 20:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106291">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/045726ccbe.mp4?token=BTfYLBLNZZ3nzqTmxR7M5KeBrIL6zjJcCs2NhDkInU4-_8wDLjD6AnaalIwUEV6HmIbqzWfBd0D9kd48kJLEe1CWNVZI-lGClirusRIG61XhpM8m5tyoAFXSY3gGSbTcoExecpW5vAPwtiYJUUgF4Cp1bOsD8_YhJf_PcGB6tfvoSJSeg3c2_2kVpAJ1VWqStWL6UvnDTnikYWw4rHbQSYJYZMpqpPnocfDijBm7mf2R-DSepvds99PgrpH6D8gQ3tKuxgShyb2To_l7Q8O41QKo-o4TLnBtw-cmQin7G36uS8Lj_barmWgAFrunilSk7tzNwxmSPafOzH9gGEe-Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/045726ccbe.mp4?token=BTfYLBLNZZ3nzqTmxR7M5KeBrIL6zjJcCs2NhDkInU4-_8wDLjD6AnaalIwUEV6HmIbqzWfBd0D9kd48kJLEe1CWNVZI-lGClirusRIG61XhpM8m5tyoAFXSY3gGSbTcoExecpW5vAPwtiYJUUgF4Cp1bOsD8_YhJf_PcGB6tfvoSJSeg3c2_2kVpAJ1VWqStWL6UvnDTnikYWw4rHbQSYJYZMpqpPnocfDijBm7mf2R-DSepvds99PgrpH6D8gQ3tKuxgShyb2To_l7Q8O41QKo-o4TLnBtw-cmQin7G36uS8Lj_barmWgAFrunilSk7tzNwxmSPafOzH9gGEe-Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔵
گلزنی گابریل‌مارتینلی در بازی امشب الهلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/106291" target="_blank">📅 19:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106290">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMAjTQC1cmkn4DC5eoeKRDFfYLy2o7vkCwSOYV9P7TeSPnpuh_yH8zHnok8FWhpr2-Z0Yypn-dmGbVD7u7fKTVrrYZZTLT9SR_tCkwdzYoT87f0NC1sAk4Gcc6di8BZ6Wcy1zs4GBQPqjwwsrqDKscrc0kH66TsnsjLO_mM3g8GXCi3jbS0YCzZ2naFL0ipwIut3r1HcZacvKSiijreXz7tV6Yzc3D4ofCswVtfou9IbX4sCxh0mjVCLoK42oPg-SxWvLlNLd5Fgvt0UXSaKjuOrXR5RSfAkOw7eFWks4zzoYX06Nvvuq8CCksSpzrphopBqyEtr-N3TjaH8eh9zEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست بارسلونا برای دیدار فرداشب مقابل لوانته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/106290" target="_blank">📅 19:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106289">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106289" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/106289" target="_blank">📅 19:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106288">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSyi0BYqJr-o5XSkc0q2A4fk_K6e7zhdA6dtKtjnPC_klnrUK13FxKlZ8_N_Pt8T6sDhSFEfiBtjgOKdXdyb7yYQyGHoNfwKV08NQ762vOxA72wGwLewMBht45v3lnWWCyLhcvmnNipdO8tmjcwk4L4VilKU-yCSQaCW7vs1g3xkVZeFnl0MUxGgx4rKLdy0ayVWsqTwSDXHjBoLCFY7XzBfRWQX8XVwsdCwJlrNfPoeIjsQbMg-HIlWalbe3reZ3ltnFfG0KIqgyeR5b4J_2XdvSQ9Ouy8eMzPcSHtKtPLXQQyY5dsFq8iBLwdfr5vY_vH9cM_xS72SY-lU3MXHiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
میلان
🆚
لاتزیو
⚽️
را در
TrexBet
پیش‌بینی کنید.
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
میلان: ۳ برد، ۱ تساوی و ۱ شکست و ۹ گل زده
⚽️
لاتزیو: ۴ برد، ۱ شکست و ۶ گل زده
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/106288" target="_blank">📅 19:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106287">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41e5692356.mp4?token=AFzTt0uq5r5N_10CAnhZPCTqHMUxq2Ay6_XJwUItAll0HrsgDd_rWj-MKZXYzAwk5Avuc35mAme0siR_WB4DxEm5Izg_nLGiWkZkPLfX08j_3bKeifN9tvOqhBOsQWtWizHTtB5oFbTlqtAQlOo_JEhQhrHQEvIdVGmhCbAH3IigG5pR_ws8PcwpkDaf8wqNw7715PSJPh42t4hDa0AgOD3VFfRr40u8CJyJ48hKNo5v9NfJTphe-zlfuQ5BsxrzcNU1TLvoCEpBtfWkYziD6uAHQ9OOZMdUwQ0xnWQwPgJg6cwbpEAKreR4jCg320ostk1wnkI8t8xLmZMPuNc8XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41e5692356.mp4?token=AFzTt0uq5r5N_10CAnhZPCTqHMUxq2Ay6_XJwUItAll0HrsgDd_rWj-MKZXYzAwk5Avuc35mAme0siR_WB4DxEm5Izg_nLGiWkZkPLfX08j_3bKeifN9tvOqhBOsQWtWizHTtB5oFbTlqtAQlOo_JEhQhrHQEvIdVGmhCbAH3IigG5pR_ws8PcwpkDaf8wqNw7715PSJPh42t4hDa0AgOD3VFfRr40u8CJyJ48hKNo5v9NfJTphe-zlfuQ5BsxrzcNU1TLvoCEpBtfWkYziD6uAHQ9OOZMdUwQ0xnWQwPgJg6cwbpEAKreR4jCg320ostk1wnkI8t8xLmZMPuNc8XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
تفاوت صحبت‌های چوپان قبل و بعد جدایی از هانی‌رامبد! نمک نشناس هم که هست ظاهرا!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/106287" target="_blank">📅 19:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106286">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gt2ObcPcNbvoBiVjsNnx7-CMPSp3XFPPve-x6pIvnWuU_Gxi1ibvrsw0N9ORmXC21PsMyNlpAaZR1FrN_m4z3Ka3IA3OrlUNT0LULDaVgRJGO6fVs250l8d-0rQGBm4fbaqT9pgSPu8xoTELF8XwOYVXvG2sl_p0Scx0LrvG9-FNrAjfcyVmgONrF4esknjoY-bZYON3zJSnLFBOxuueu6i5weOBT0vSvmGaoI_jSH5KWqbZ_iAqLHkY5pi3T4rLJjssjCQnc1Exo54FDBRPWrG5acPkMy7yxna0RVBen_dvdjf200mfMJKQ9-F2inH6T4T14w6paZXjUf7Hes2_Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇺
جدول بهترین‌گلزنان تاریخ لیگ‌قهرمانان اروپا؛ هالند و امباپه با همین فرمون پیش برن به راحتی رکورد رونالدو و مسی رو میزنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/106286" target="_blank">📅 19:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106285">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90c64420bb.mp4?token=OYJmeJ2HPSb5aefobaE1Z0VKEIlNQYVzcO5-NnUwOa8R3GDk-8_XQmGY_2NpS0q_7HPLzdIiZvl6kEV_Xo484TRJEo57JgcCAKfadp2j-81vSTzrMoWYfhnqQ8Ovkx7asfN0sUBAyZbYaO4C3ZgburoMLuXnHtydGCLUGAcb-4Yg4oPgcH5V9MdNUQ4A2Ssfwd0F9TePSVbnQS1sra7pKPK-39lCXW2H9t5MUfbxZ9jxg2a4bLbTgH7qKJeHHfQN1t7Rm-Ju95IQiYUliYN-Iha1R5Fk16gJetQtPge6rSUmwPoOE5GTUOtndlLOMO1vdQN1jqmbooxoygIp4GQbjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90c64420bb.mp4?token=OYJmeJ2HPSb5aefobaE1Z0VKEIlNQYVzcO5-NnUwOa8R3GDk-8_XQmGY_2NpS0q_7HPLzdIiZvl6kEV_Xo484TRJEo57JgcCAKfadp2j-81vSTzrMoWYfhnqQ8Ovkx7asfN0sUBAyZbYaO4C3ZgburoMLuXnHtydGCLUGAcb-4Yg4oPgcH5V9MdNUQ4A2Ssfwd0F9TePSVbnQS1sra7pKPK-39lCXW2H9t5MUfbxZ9jxg2a4bLbTgH7qKJeHHfQN1t7Rm-Ju95IQiYUliYN-Iha1R5Fk16gJetQtPge6rSUmwPoOE5GTUOtndlLOMO1vdQN1jqmbooxoygIp4GQbjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🫣
🥲
دردسر‌های کیلیان امباپه هنگام دیدن سکانس‌های فیلم زیدش اکسپوزیتو :)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/106285" target="_blank">📅 18:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106284">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/833fb28b6e.mp4?token=NpE7eJ2DmY052v2JTsFFfYHjIKd9gCNsGNMq45mSu6Cgw0FqRB4fSx50i4p1ciCcijGKUdz2dlB-jwpJ-Bsq5vTK10NiXD7O1GWjAYfGw6sX9mgd1RpffJAFOQky81284FRinH5DWJjx3EeTAvSnJYOXBvFJclfz-2h41bJPWnnAXR9i3qZdOFBKiV2cUbMyoecp34WhvZDn1sZ6itzuRRpfhQLPxsDkJmDSM1O_IQIwdtj8s2Qqz3PcNEUc_BEWVb7L77EFBP46nx3NeGfjZVhz5JWTg7crM6QZAFyXED8uT1IAGfiQ9t1VatwzP6qjawVhSkZte3U1HXza6j-BGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/833fb28b6e.mp4?token=NpE7eJ2DmY052v2JTsFFfYHjIKd9gCNsGNMq45mSu6Cgw0FqRB4fSx50i4p1ciCcijGKUdz2dlB-jwpJ-Bsq5vTK10NiXD7O1GWjAYfGw6sX9mgd1RpffJAFOQky81284FRinH5DWJjx3EeTAvSnJYOXBvFJclfz-2h41bJPWnnAXR9i3qZdOFBKiV2cUbMyoecp34WhvZDn1sZ6itzuRRpfhQLPxsDkJmDSM1O_IQIwdtj8s2Qqz3PcNEUc_BEWVb7L77EFBP46nx3NeGfjZVhz5JWTg7crM6QZAFyXED8uT1IAGfiQ9t1VatwzP6qjawVhSkZte3U1HXza6j-BGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
ریدمان دیشب داور اسپانیایی بازی لیگ عربستان که بجای کارت زرد اشتباه کارت قرمز نشون داد
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106284" target="_blank">📅 17:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106283">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9242df0ef5.mp4?token=c0MpQQP4OptSRX9aFwJkYzd3WvutngxANuvaxIOchhEenwvr87L0dW4zm0MJm9i3EFCJ6zxunUfguNoN0cjy2mMhLqzMquD7lTEBEmd4MPGCVJKvr_YjCVQg1ieFacNyts_yGg29karF68IwhXE50iesplFh3LaPycrC-wao3Rf0kRZIbFxzdHPCuIxD4cIk1Adg9q_jF2ARqVxUWo7ZjBOhxDojjSx3tG93-9zRZ7sRQ7IwYaMKZ1pX3c0jYcXC73iRvCrC22YpXqgR8W9X6iMOV3LITTa-IBEGbJgJe7ugTCZ9jVy6gHzeSsT4hVS7UUN0v9fThZPxhx8Bw4RwhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9242df0ef5.mp4?token=c0MpQQP4OptSRX9aFwJkYzd3WvutngxANuvaxIOchhEenwvr87L0dW4zm0MJm9i3EFCJ6zxunUfguNoN0cjy2mMhLqzMquD7lTEBEmd4MPGCVJKvr_YjCVQg1ieFacNyts_yGg29karF68IwhXE50iesplFh3LaPycrC-wao3Rf0kRZIbFxzdHPCuIxD4cIk1Adg9q_jF2ARqVxUWo7ZjBOhxDojjSx3tG93-9zRZ7sRQ7IwYaMKZ1pX3c0jYcXC73iRvCrC22YpXqgR8W9X6iMOV3LITTa-IBEGbJgJe7ugTCZ9jVy6gHzeSsT4hVS7UUN0v9fThZPxhx8Bw4RwhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
افشاگری جنجالی محمد سيانكى: برخی تیم‌ها در سفره خانه هاى تهران بازيكن جابجا ميکنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106283" target="_blank">📅 17:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106282">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iM1Bvv3HZKf9s4skskgwM2Eh5vmnTB7pberyOuFWejmNvMMHfG0TQdFXQniMrpNzlp9DJbX6NSNfyiIZpD9x6ZGkhExqxLBDBEH_DMc2i91_sdZpf7R6-ms0_6SQMVOL9gcWr-FbayNUGHipPm1rwyMOfbNZNVHTnjtMAtzYzrQrtGZ2AsuMB0RDt8HHKbeszpu2Ops2JuNvcYlwR37ZglXtiymmSf1UHl1wYAps9UmTjEr7MD8o9W-GTIsNHKt4Z0joEUbCQ8OFFoXAEDeMY8idswQpBU8cE7h7So86FaOl2wTHvuk4SLVwT4X6YBNyDU2suzeDBx2xnSZuttkbZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
🔥
🇪🇺
عملکرد تیم‌های انگلیسی در هفته‌اول UCL
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106282" target="_blank">📅 16:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106281">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc8b60637a.mp4?token=C32jIRSNGbzE7dkPygxVXuLsb9L_GE1ixIH_UD4rCP2z8eoQ5UxTqAwCrMgYpwQ5vG-KAan7S9297IyKWfpV84EzefTFbWSeA5S86IhEIbFj_-DW-69qWQbGqHrylS0Q_ekI5ssRwBwMUGGi_Cq2kEk1PGdFkgo5z_SWbGoUhlGHctKU1P05jJMWxLE_kaXWGUpEL2x274YpKInOK_1a3d9l8rXvNVMkI68tpuE4ot22WEw84k2Ma2gXLyI_iZZpJgW42GD7Ky2-7FnSbpcF06Ry2TEtQan31fENfCfUEsMyM-P0KuVAYTmBFIKwhgK--t6omCAJPy6Akv4mBAB4OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc8b60637a.mp4?token=C32jIRSNGbzE7dkPygxVXuLsb9L_GE1ixIH_UD4rCP2z8eoQ5UxTqAwCrMgYpwQ5vG-KAan7S9297IyKWfpV84EzefTFbWSeA5S86IhEIbFj_-DW-69qWQbGqHrylS0Q_ekI5ssRwBwMUGGi_Cq2kEk1PGdFkgo5z_SWbGoUhlGHctKU1P05jJMWxLE_kaXWGUpEL2x274YpKInOK_1a3d9l8rXvNVMkI68tpuE4ot22WEw84k2Ma2gXLyI_iZZpJgW42GD7Ky2-7FnSbpcF06Ry2TEtQan31fENfCfUEsMyM-P0KuVAYTmBFIKwhgK--t6omCAJPy6Akv4mBAB4OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولی تو تاریخ لیگ‌برتر ایران هیچ‌شادی گلی مثل این نبوده و نخواهد اومد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106281" target="_blank">📅 16:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106280">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5318ea7807.mp4?token=I8lc3rFASqQ5IUBZUTbAIqjM1EYjGMGALHXBQnHCkDmsbaKS0IOOIRjn5CEtMx2WMUnsM2su-aXXo5tBgesLimUbOksPimybxg2d0QTojmjKBW1D0Qffg8ZXI_KsAHvwPv4RxOuFtuc4-MNMS0-N_uN0ydhlrA7So9DXrJGzK2tYmBkMHhcX2jApam6cEbyuslAVDeq3YYk85rJ_p5tYN7neBigTL3_xzKA9_8DzIFvT47sy3zN3skzCIz85V4mEUzLiKib29Tr6UE22fXvF7Rwfy1hP-0lz7_Bm6n31a_-zMgJf9y8dPgaP-xi1Q0qU_Yosge0p1DqC3QPaoUj15w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5318ea7807.mp4?token=I8lc3rFASqQ5IUBZUTbAIqjM1EYjGMGALHXBQnHCkDmsbaKS0IOOIRjn5CEtMx2WMUnsM2su-aXXo5tBgesLimUbOksPimybxg2d0QTojmjKBW1D0Qffg8ZXI_KsAHvwPv4RxOuFtuc4-MNMS0-N_uN0ydhlrA7So9DXrJGzK2tYmBkMHhcX2jApam6cEbyuslAVDeq3YYk85rJ_p5tYN7neBigTL3_xzKA9_8DzIFvT47sy3zN3skzCIz85V4mEUzLiKib29Tr6UE22fXvF7Rwfy1hP-0lz7_Bm6n31a_-zMgJf9y8dPgaP-xi1Q0qU_Yosge0p1DqC3QPaoUj15w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🥶
باریک‌ترین خودرو جهان با عرض ۵۰ سانتی‌متر ثبت گینس شد! وزن خودرو ۲۶۴ کیلو هست و حداکثر سرعتش ۱۵ کیلومتر بر ساعت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106280" target="_blank">📅 16:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106279">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76c27ec481.mp4?token=lwR-M-2h0OBNO6BvP4hqRpvMx-K4dyS4li2_FTKZXDA4rP69ZbBO2C5NTjzmKt6VLVGeKw_gkm8s03HYXghH3wQhOrU09OlUcJJ5rXaQlOPVtrkmamWZyz51q2yhmMMEaQl6reqm6xIUq6gO_PECfFO2QHVvq7m9y2Qx_9uSYjXxzkjM0M4_YIppmloXFiyBvipRhqJf44_3pKr0J7xa1YVc-qM4KFrP9MPUSA3xTaLBC9Zc5UeE2e49_hVS7xn2kjSRA-2-ql1xr-p7mTKXGW3cj7TCXvQ0p9QYBXQFOJIFpllYwipc5rVRe9BX4Wk52I574FwyFIamgff-79MYBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76c27ec481.mp4?token=lwR-M-2h0OBNO6BvP4hqRpvMx-K4dyS4li2_FTKZXDA4rP69ZbBO2C5NTjzmKt6VLVGeKw_gkm8s03HYXghH3wQhOrU09OlUcJJ5rXaQlOPVtrkmamWZyz51q2yhmMMEaQl6reqm6xIUq6gO_PECfFO2QHVvq7m9y2Qx_9uSYjXxzkjM0M4_YIppmloXFiyBvipRhqJf44_3pKr0J7xa1YVc-qM4KFrP9MPUSA3xTaLBC9Zc5UeE2e49_hVS7xn2kjSRA-2-ql1xr-p7mTKXGW3cj7TCXvQ0p9QYBXQFOJIFpllYwipc5rVRe9BX4Wk52I574FwyFIamgff-79MYBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚫
🎙
هادی چوپان درباره کلیپ رقصی که در دی ماه از او در صداوسیما منتشر شده، توضیح داد این برنامه دو ماه پیش از اتفاقات دی‌ماه ضبط شده و ارتباطی با حوادث آن روزها ندارد
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106279" target="_blank">📅 15:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106278">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f692d60102.mp4?token=v9S7HksaqP4IbkizNXG4cJp4PFyI28n9P4gGsCoONHUNw_FeeVeaePkXgT9JwdNVJyRut4Xz0yku_V3_ZPN6QuME4bFfZbMV27PvdtilbzgmVYFwhZUyQFllzHYKJlBRi15v33xp9gD8fS8bZPrwIo72dn9IgJdM7fEsBOSr7WeeKE4Gz0115ovhtuQLrNHtYFRbxiChoqWNDmHWimAH62EU1jFv_mVgscK2f1M1jUfDppj7mXsBhoo2B7YUnX-Pv61ToaSLEbxswD6XfwrtTOLtAHcUlL_TbPWaIjGeUufn8MepQCdWy9oceyWJoUCAYTLpq_94EP1WA8Y_Ez-OUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f692d60102.mp4?token=v9S7HksaqP4IbkizNXG4cJp4PFyI28n9P4gGsCoONHUNw_FeeVeaePkXgT9JwdNVJyRut4Xz0yku_V3_ZPN6QuME4bFfZbMV27PvdtilbzgmVYFwhZUyQFllzHYKJlBRi15v33xp9gD8fS8bZPrwIo72dn9IgJdM7fEsBOSr7WeeKE4Gz0115ovhtuQLrNHtYFRbxiChoqWNDmHWimAH62EU1jFv_mVgscK2f1M1jUfDppj7mXsBhoo2B7YUnX-Pv61ToaSLEbxswD6XfwrtTOLtAHcUlL_TbPWaIjGeUufn8MepQCdWy9oceyWJoUCAYTLpq_94EP1WA8Y_Ez-OUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✅
تو این شرایط اگر از اینترنت زیاد استفاده میکنین برای مدیریت هزینه‌های خرید بسته، این ترفند راه خوبیه. برای دوستانتون هم بفرستید
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106278" target="_blank">📅 15:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106277">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb9d15a53b.mp4?token=PwFbODS4N48IHuz9wOOcwXh_VaYRQk9ABDLo-lmlAECtToYpFjygoL75J-2CncaYI53JlyeScCAn3rgcm6jgH0N78_ihpvt_OlbMZLAsY73WuAWn_uxI0grFqqvW9DS2OYOv1hCnntpm3zA8Xtd-oMIOmNaUTz7X-tlNhr5QWyxKEN2fxvfmyh7Mflh-6SMtV0LQOrPlgQ7ebb64u9lJW_nl7me8JSaXycGH5ngs7CbyMVMu0M_hfrwsHvNCb-NVM8rVwPHeLZ8MoFUEMSx6EvbqnxPU-lKN_cO_0K2k-1Uwy7DJKAxlTtzD6lgBu1FA0jCJ7jB3HX43Lf5XtfbG9IisgzfCu5pKq7wK7U4ykuYcLY4_PXUMo51bObHhGhm-A8XjCCPjawABAPiKhTbH3NNuiJ3v8Tw2VZp83mqG1IKWBGrSbt7tPpG5NcgWlr8ESYac0dOKazNdYb5Kd8T5SNRU_Vcfknr7r3Q0hEWQGjJfj1I-DGwwhF9KyEmSrm9LOyBvSckYtkvvwjlqLKuDbci-1wDhPtPynT7_HGCTs3DvpvMIUBntHTz_BSzdocePZeRo-WisVhKrY0NS9IxLE5TMmfuqYGOpXlbER6lb-Vy6V3VieXJvS1gW3oa5L4lKbM9DTQZ5-fB0Dmi7sxX7TMti9ZG5uNmIgzwP6FPgChY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb9d15a53b.mp4?token=PwFbODS4N48IHuz9wOOcwXh_VaYRQk9ABDLo-lmlAECtToYpFjygoL75J-2CncaYI53JlyeScCAn3rgcm6jgH0N78_ihpvt_OlbMZLAsY73WuAWn_uxI0grFqqvW9DS2OYOv1hCnntpm3zA8Xtd-oMIOmNaUTz7X-tlNhr5QWyxKEN2fxvfmyh7Mflh-6SMtV0LQOrPlgQ7ebb64u9lJW_nl7me8JSaXycGH5ngs7CbyMVMu0M_hfrwsHvNCb-NVM8rVwPHeLZ8MoFUEMSx6EvbqnxPU-lKN_cO_0K2k-1Uwy7DJKAxlTtzD6lgBu1FA0jCJ7jB3HX43Lf5XtfbG9IisgzfCu5pKq7wK7U4ykuYcLY4_PXUMo51bObHhGhm-A8XjCCPjawABAPiKhTbH3NNuiJ3v8Tw2VZp83mqG1IKWBGrSbt7tPpG5NcgWlr8ESYac0dOKazNdYb5Kd8T5SNRU_Vcfknr7r3Q0hEWQGjJfj1I-DGwwhF9KyEmSrm9LOyBvSckYtkvvwjlqLKuDbci-1wDhPtPynT7_HGCTs3DvpvMIUBntHTz_BSzdocePZeRo-WisVhKrY0NS9IxLE5TMmfuqYGOpXlbER6lb-Vy6V3VieXJvS1gW3oa5L4lKbM9DTQZ5-fB0Dmi7sxX7TMti9ZG5uNmIgzwP6FPgChY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
داش‌علیرضا منصوریان درحال یاد دادن ترفند سرمربیگری به اسطوره سندروم‌داون استاد علیرضا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106277" target="_blank">📅 14:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106276">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aa2c3aa1e.mp4?token=tmfodG9LIKfSl4s8ZgOtrqlphyRANXAaXPxxkfMqgz68c0rO2Aln7TTxxKUkTVL3gz5FIS4kfeSrL25sX53wUWDkIqJxtvM0aO3jXTnb6aDAfmgTQaTnAP2EV5stt5Af8ibGI2MGVUT22z5-gRr_eEpyAG2kpzH8Wl77w9u5GU1_CCY6MuEXEN3t-6cPiU5S_5Rhjpskk0UNyMrszYuUBxfFU2tLU1P1nq8ut-tqxtXarkSIcVeaC6KHpsl0VPA8rOnQ08TgyMEeoqVqH_Cd67pRaB4aFPziBySO_zKYbUerGzjOOzL4xPvshdjJshE30-dZqBQVxxU_53MaoxkU6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aa2c3aa1e.mp4?token=tmfodG9LIKfSl4s8ZgOtrqlphyRANXAaXPxxkfMqgz68c0rO2Aln7TTxxKUkTVL3gz5FIS4kfeSrL25sX53wUWDkIqJxtvM0aO3jXTnb6aDAfmgTQaTnAP2EV5stt5Af8ibGI2MGVUT22z5-gRr_eEpyAG2kpzH8Wl77w9u5GU1_CCY6MuEXEN3t-6cPiU5S_5Rhjpskk0UNyMrszYuUBxfFU2tLU1P1nq8ut-tqxtXarkSIcVeaC6KHpsl0VPA8rOnQ08TgyMEeoqVqH_Cd67pRaB4aFPziBySO_zKYbUerGzjOOzL4xPvshdjJshE30-dZqBQVxxU_53MaoxkU6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
دلیل جدایی هانی رامبد از هادی چوپان: اون مثل برادر بزرگترم بود ولی یه زمانی از من خواست پشت جمهوری اسلامی نباشم که من قبول نکردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106276" target="_blank">📅 14:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106275">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NkdtYwK23yGjgok9GeJpU2rYRHV0U8ZERIeiQKsS6OpPLZII4kAFXfRg9fgGBipBMK_DxBYnvJ9zsuOor3A_SxW1MNUWLbyyOTJd3peKBHg-sG78eLGShfgrAyfuRmFrluCi2AFg9Je-EloejLMhJxQs67UMSWvn8RcxWbtel27sO1ek1PoBQs2Egx8ySCG0rn78GaFk7rAJ-0p16a7bedqPsuzYi49zDJ8HHjpjSubQkCsUCQqJKJ4eAmwIr6VNVt4xYNze2hs45i73dlWHA4A55Rz46rzdx47wzx_tc1M_el6D8vTi-2Ck63oApL74eybPzEo3QuDyRZ6OqPxrWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات لواندوفسکی و دی‌پائول که درگیری‌شان در هفته‌اخیر جنجالی شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106275" target="_blank">📅 14:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106274">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4SuPig6yK8t3LszTfZMWGmiQ8bO-Ac0Qxh9ycVwPjGVb1QvHIGjgkqME4cgSDfbWTRBa2Gsd8owFQ6NZ9QLoDZNQ1dVLek3_k6Zay1Y8qG8aVGYkGdlnfBNEqpNQF5fOmz0206Aje6G1oqkTVQRtxmEGhi5-kqI-2e31sVEEys2sn5f02Obxjz4kk5UDMm31mzMJmPBUFTpWkYs8lN5NRv3wiIYxzzcvjGt2rNY4KJGXgdGs2Y3xaoTNiAIaENSaIhAiUU827cxzMnFnhSdymNB1VGkXhBjgPAIC-upq7KYLd0754cK5U_Jz13eGqLjzQrqWe3piQ_J6wMo1K_JOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
درخواست تاجرنیا از هواداران عراقی برای حمایت از استقلال در بازی مقابل السد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106274" target="_blank">📅 13:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106273">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bcc13d5f9.mp4?token=SovcbNbqfFUlyQMJrAypRhWb8q9FEGQfaA7PwvTL9-BbP2Zydhfgerc-aT3FsNKlpbT1oC4XVNOiW3lOL3HbMt_yxksueMQGaMUZzUZjX87kF5BgGVZd7r6siO18uf-PbVSpcO6KuHoQviwCD8xOVADBSwA3mslvuXv5xCk5R0TM_numMssSaCIsJS262FYlZY6s18_C3AMCPaAkulP2LrOpNM01vJaFjLW9Pah_Go9i4xPmlwurKO7tZjJV-xkc1BpdsjaN0Hccx-jZgzEutxoeAuRtUpeg1bbVryJSLQjbO_89cj4FJWerbF1MV0JXdfsqUzBqebwZf2yYsWy_34WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bcc13d5f9.mp4?token=SovcbNbqfFUlyQMJrAypRhWb8q9FEGQfaA7PwvTL9-BbP2Zydhfgerc-aT3FsNKlpbT1oC4XVNOiW3lOL3HbMt_yxksueMQGaMUZzUZjX87kF5BgGVZd7r6siO18uf-PbVSpcO6KuHoQviwCD8xOVADBSwA3mslvuXv5xCk5R0TM_numMssSaCIsJS262FYlZY6s18_C3AMCPaAkulP2LrOpNM01vJaFjLW9Pah_Go9i4xPmlwurKO7tZjJV-xkc1BpdsjaN0Hccx-jZgzEutxoeAuRtUpeg1bbVryJSLQjbO_89cj4FJWerbF1MV0JXdfsqUzBqebwZf2yYsWy_34WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
محمود فکری: سهراب بختیاری‌زاده از دست صالح حردانی حالش بد شده بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106273" target="_blank">📅 13:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106272">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFpeiqMFsZn1Q6zKBcKGqV_HpdP4St75VNstKAP77OsGYuIW2a3eRf4xGILiCT5OvdArEM4gU2O574zyDx9kHom3J-LD8_FHMcfPwGlgoPm9sn8L22vvHvlHWw5r3jq8BhyItKu-Tx38qK6Z1tpMQgtWjChiofYV1CXmnNUamDGU1hRBjUDPBUVb2JxhjOGMUxVeyPlmDthmeJgms763A_8dFR7ltMIN4xRfbL0Ligly3qWMRb8RrI5Plx_3o2SDTuwNhC6sIpkJF4LMCobuMgtXUKnSyVeTaMk0lud6BiOmimmRnUT7ANdnBpOzopPTqVaX94cY8XUh0cQ_KbBgpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
کیلیان‌امباپه: اگر عدالتی وجود داشته باشه بدون‌شک توپ‌طلا امسال باید به من برسه. درسته جام باشگاهی نبردم اما در جام‌جهانی تاریخ‌سازی کردم و این جایزه هم برای عناوین فردی هست نه صرفا تیمی. پس مطمئن باشید به خودم رای خواهم داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106272" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106271">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_LYZMWXQOJ0mTG_13JQDUpK4DXOS_NZsV7I1fKY8cWViyD0jqitdmQwRSP_Zw_g8ygLtIh0KHBUe9d5-d5zS7ngncV1Dhisihm_5M4FNQNR_fTu4sAG8ZUlhKhjMbkOWGzU7Je-GWEkU2vMneN-Q80wUjwpj_bLXit1-ysCf-bbNyt1Bb66smnW24t0rb4s6bhfSvOY-71M_NYi7xAfpt9KR0EIogCAxmjZbUgjepZe0iLpkzCoGtVM5NjuBhyySO7sPA63wIodNCqaGzWbuxCgPYYsU2Ar716-5n5VqRRvckTkMs7L7s-9dtrpTk84lQP_XudrtS9v9eIDNUPj_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇮🇷
با رایزنی صورت گرفته مشکل پرواز استقلال به بصره حل شد و کاروان آبی‌ها تا ساعاتی دیگر عازم این شهر میشوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106271" target="_blank">📅 12:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106270">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92b41d0adb.mp4?token=M6E0zArPVsU7a5AMoyZu1VCfzdeoWFRloHyP8NM7POUYWtgD4FDbOXtRKkEjmjfI-OE0MoC1vdQrc6GHgBwJw-ZMHGO54b_2TV6b5KoliwQH-ZkxBIw-NFJ0eKCCn7rJcCEV1SBZLZdS5sFvW60Lc_fOEkhFl73835eFzi6JLYP36VeWSl8fc5nyKzXiy1vlFlUcamtkaMRb3B5s3qnXxyXoWSPtz8BSkZ-wvosP7WVcXv0L549Y4dLAGy1B6g0nIHXeec4QrnITgm_njUYclG-foA2eloE3l27hVK9S-AhsVObk5aXDDW6cixYiVH8wWJ_b3L5K3eSZbOC0jbGRVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92b41d0adb.mp4?token=M6E0zArPVsU7a5AMoyZu1VCfzdeoWFRloHyP8NM7POUYWtgD4FDbOXtRKkEjmjfI-OE0MoC1vdQrc6GHgBwJw-ZMHGO54b_2TV6b5KoliwQH-ZkxBIw-NFJ0eKCCn7rJcCEV1SBZLZdS5sFvW60Lc_fOEkhFl73835eFzi6JLYP36VeWSl8fc5nyKzXiy1vlFlUcamtkaMRb3B5s3qnXxyXoWSPtz8BSkZ-wvosP7WVcXv0L549Y4dLAGy1B6g0nIHXeec4QrnITgm_njUYclG-foA2eloE3l27hVK9S-AhsVObk5aXDDW6cixYiVH8wWJ_b3L5K3eSZbOC0jbGRVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
پاسخ جواد نکونام به سرمربی پرسپولیس!
جواد نکونام سرمربی تیم تراکتور در پاسخ به صحبتهای مهدی تارتار در کنفرانس مطبوعاتی پس از بازی با استقلال خوزستان صحبت کرد و گفت که «آنها از آب گل آلود ماهی گرفتند!» تارتار هفته گذشته خواستار برخورد شدید با خداداد عزیزی شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106270" target="_blank">📅 12:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106269">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106269" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106269" target="_blank">📅 12:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106268">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuduDRXHbcq8OJ3t8orneNXx0i3a3OudymKNucIP_5Ve4JnF6v0C_iW2haNUQFrLg5NBTaB7Cv8PSUKjttJ2NI2KRy8WtNvHnq6b93yZQRHIu4E4XB-lzKrWveddcx7x76x2fBbGjJrhMNB1Syi1oWwVMGhcPZC3wDP89FNvmgtrKiMuOcuTTTWB81IpO_3LSqbvZsu_yBHy7h52LvdWlwvXBcSRN0MuAJtHPX713xDzLVk1S_H5S0dL8G4__J0yLdHYZd3VVg5p84jKslD2ztIcm8axRBROiRQsu9l-mX5GBa_HunMWFqZsf6lSJ34bRKwKE5IAian-KPug1VCK1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت‌بین‌المللی
TrexBet
پیش ‌بینی کنید.
چلسی
🆚
لیدز یونایتد
فولام
🆚
لیورپول
اورتون
🆚
تاتنهام
ساندرلند
🆚
آرسنال
رایو وایکانو
🆚
رئال مادرید
میلان
🆚
لاتزیو
کالیاری
🆚
آتالانتا
پادربورن
🆚
دورتموند
🦖
🦖
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب برای بازی‌های امروز
🦖
واریز آسان و امن از طریق کارت به کارت و ارز های دیجیتال
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106268" target="_blank">📅 12:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106267">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
⭕️
🇮🇷
درحالی‌که مدیر سازمان فوتبال استقلال دیشب گفته بود که اعضای این تیم امروز ساعت ۱۴ تهران را به‌مقصد بصره ترک می‌کنند، فرودگاه بین‌المللی این شهر تمام پروازهای با مبدأ و به‌مقصد ایران را تا اطلاع ثانوی تعلیق کرد
‼️
‼️
‼️
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106267" target="_blank">📅 11:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106266">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d37095ed52.mp4?token=B51X6yx_tUt5ruRSlf7G_QZpc6ERVlnMRASwwyQN2QygjEVgFicuP27t_cGO5JKBQybV8vhz1dpv60p5A-rUayq3pWDOcKx5MlopD_UmAOHglfDoEaCU0UK80WJ2fBtEnqOhYFlnmRQrE3I0Rnt8k7jxE83QsnktsllcJzjHeRFwStHTlAeLa-9763lkLmjLgOG_WvU6MMPa-nSbX40FSqq1z2TCtLVqwiS1lt38Bzv5CHjSRLk4Mhee98sRcXDrEChdyDDBdveoVQBsRwkxfLPPcApF5KGMHbQrabrK0IA-V7PnEDb4yCzBpH7x6zZu9mp8y2brOiuAg4g55Xv6IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d37095ed52.mp4?token=B51X6yx_tUt5ruRSlf7G_QZpc6ERVlnMRASwwyQN2QygjEVgFicuP27t_cGO5JKBQybV8vhz1dpv60p5A-rUayq3pWDOcKx5MlopD_UmAOHglfDoEaCU0UK80WJ2fBtEnqOhYFlnmRQrE3I0Rnt8k7jxE83QsnktsllcJzjHeRFwStHTlAeLa-9763lkLmjLgOG_WvU6MMPa-nSbX40FSqq1z2TCtLVqwiS1lt38Bzv5CHjSRLk4Mhee98sRcXDrEChdyDDBdveoVQBsRwkxfLPPcApF5KGMHbQrabrK0IA-V7PnEDb4yCzBpH7x6zZu9mp8y2brOiuAg4g55Xv6IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚠️
بختیاری نویسنده و کارشناس اقتصادی: چند سال قبل من رو به سمینار دعوت میکردم تا اقتصاد رو با انیمیشن به رئیسی یاد بدم؛ گفتند ۳ دقیقه بیشتر نشه چون ذهنش می‌پره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106266" target="_blank">📅 11:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106265">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe7ae3e84.mp4?token=cnOPxv9he67PXJBCZo-nJhU2jgYE_Xbn04nzfmtRJB6-kU1uwKME8OF_-_P-mvgeNhsMLiNtXzVZtoOAEodhaEpM0NCBe7ZNKSSdgTq8H5Ku5wyLQ7ByyQIdA5fzm3Ab6bvc5-FVGPrxv0RLtKs2rLv1sK1WBfh0VeYHqt7EMCuWUmxtFb8gqIvGtVQuB8QetTFT3T9tHwrOXESP86gqTUZXFxBNBRvsOvuYUk4TCCcG6V1gxeyRzEL-jT09GS2Y7WPpwj_-RvkEHIyw5y30A22fDkkPgMTCjPytknAk8r-t-eHWlY8Yh_zWZqY3-ZI2eNwwWs9czic5iwexiWkAbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe7ae3e84.mp4?token=cnOPxv9he67PXJBCZo-nJhU2jgYE_Xbn04nzfmtRJB6-kU1uwKME8OF_-_P-mvgeNhsMLiNtXzVZtoOAEodhaEpM0NCBe7ZNKSSdgTq8H5Ku5wyLQ7ByyQIdA5fzm3Ab6bvc5-FVGPrxv0RLtKs2rLv1sK1WBfh0VeYHqt7EMCuWUmxtFb8gqIvGtVQuB8QetTFT3T9tHwrOXESP86gqTUZXFxBNBRvsOvuYUk4TCCcG6V1gxeyRzEL-jT09GS2Y7WPpwj_-RvkEHIyw5y30A22fDkkPgMTCjPytknAk8r-t-eHWlY8Yh_zWZqY3-ZI2eNwwWs9czic5iwexiWkAbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
🇪🇺
🇪🇸
کارشناس چمپیونزلیگ: امسال نوبت بارساست که قهرمان این مسابقات بشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106265" target="_blank">📅 11:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106264">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecba46a4ad.mp4?token=gca8CczkEJXf7zoL-Q8jxzXyfYi-NrjEZjbRmqBi_PEw4enCdXGMwj5vK4fj-hte8LAfspWtk43tMZC1l5_Vt-FsCOfjmilFCq073RFTiURDIFHqgHZQsJTWli5zq5-4CnPCdbGvB9UcUe_63ODnCwyYY7qN6JyFwpzyr7S6h7zow2G-5eSwRPAG1_wW6PlYnMy_1aeHSXVUf7AZXl8YWiGVlCif0LxTcu3wPin8WtszOLvjDpWZIZZLtNwzJhn4S5shuPokzPuHQN7A-V5AriAKZa8IuWigUlywurSkAtiB7y1A3-GJBXJUcwzgTgB9SgKM8nbkBIZbipBPCMAjhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecba46a4ad.mp4?token=gca8CczkEJXf7zoL-Q8jxzXyfYi-NrjEZjbRmqBi_PEw4enCdXGMwj5vK4fj-hte8LAfspWtk43tMZC1l5_Vt-FsCOfjmilFCq073RFTiURDIFHqgHZQsJTWli5zq5-4CnPCdbGvB9UcUe_63ODnCwyYY7qN6JyFwpzyr7S6h7zow2G-5eSwRPAG1_wW6PlYnMy_1aeHSXVUf7AZXl8YWiGVlCif0LxTcu3wPin8WtszOLvjDpWZIZZLtNwzJhn4S5shuPokzPuHQN7A-V5AriAKZa8IuWigUlywurSkAtiB7y1A3-GJBXJUcwzgTgB9SgKM8nbkBIZbipBPCMAjhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هیچوقت این دوراهی سخت فراموش نمیشه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106264" target="_blank">📅 11:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106263">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84d171b8e1.mp4?token=NRyP4eiA6LyIIHn002Rmuiu3EIInsibuycaSF9kheseo6pOKx-EhX4if9tHS-l98hVM9eUsCe34rViFoEVZs2MZHO4o6ZeGz2ny3IxxJwbSnHRCVBva8AZnOMlct37c-5E1w11sEHGo1WXkGPj813H-oXgmnHzD1sLODGfu__tprVCfV_Qy8STnCcanMk3S_dGv99ma4J_STgy0VXCU8aLXukSAQ6953UZv-vQ9nbprwPl_tXSMgXnhxZAMXX3EYEg2LxN4EdRXDolrvATlguIXQ0byInxaSDgd0WvlnTB18m8EDwjhRNeozR206y2loZUFT3LW0siTC_sl1jZV5dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84d171b8e1.mp4?token=NRyP4eiA6LyIIHn002Rmuiu3EIInsibuycaSF9kheseo6pOKx-EhX4if9tHS-l98hVM9eUsCe34rViFoEVZs2MZHO4o6ZeGz2ny3IxxJwbSnHRCVBva8AZnOMlct37c-5E1w11sEHGo1WXkGPj813H-oXgmnHzD1sLODGfu__tprVCfV_Qy8STnCcanMk3S_dGv99ma4J_STgy0VXCU8aLXukSAQ6953UZv-vQ9nbprwPl_tXSMgXnhxZAMXX3EYEg2LxN4EdRXDolrvATlguIXQ0byInxaSDgd0WvlnTB18m8EDwjhRNeozR206y2loZUFT3LW0siTC_sl1jZV5dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اعتراف جیمی کرگر به اشتباهش درباره لیساندرو مارتینز مدافع منچستریونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106263" target="_blank">📅 10:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106262">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d19807ddf.mp4?token=mAkSq1Zl6lqKELOEFm7ydEa64RIsCB9d4TP1XlISTZm6tmV0ZY5NzE4_fwJqUnqC6Fxo6f1ddZXfuh9ROEaLuSUfvQVBQLZbB_B3EX0NCTHFS9uWjPbpDuahccs2aPuEGnDVcyyzV6IgQSQU30nt4QiGxYqz_032L10VJlg7zuMCWYEdU5Tztuk_PA04TCs729Th993FWHVL8EETDQP29uem-QBPNn384bRGID9vNHDq1sfWaggw6ohbTsN6eKnjflAAkNlj7JR1BRqRV7QfbVMA8G3tAZGsWAoXLxaJrSiqvmcj8ft2DDB944sZUOxBuHvil-BnSH0H4YCxoy17Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d19807ddf.mp4?token=mAkSq1Zl6lqKELOEFm7ydEa64RIsCB9d4TP1XlISTZm6tmV0ZY5NzE4_fwJqUnqC6Fxo6f1ddZXfuh9ROEaLuSUfvQVBQLZbB_B3EX0NCTHFS9uWjPbpDuahccs2aPuEGnDVcyyzV6IgQSQU30nt4QiGxYqz_032L10VJlg7zuMCWYEdU5Tztuk_PA04TCs729Th993FWHVL8EETDQP29uem-QBPNn384bRGID9vNHDq1sfWaggw6ohbTsN6eKnjflAAkNlj7JR1BRqRV7QfbVMA8G3tAZGsWAoXLxaJrSiqvmcj8ft2DDB944sZUOxBuHvil-BnSH0H4YCxoy17Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🙂
جدیدا تو صداوسیما دیدن که مخاطب زیادی ندارن دیگه خیلی احساس راحتی میکنن
🎙
مهمون شبکه دو: زیر کونشون میزاشتن
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106262" target="_blank">📅 10:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106261">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
⭕️
🇮🇷
درحالی‌که مدیر سازمان فوتبال استقلال دیشب گفته بود که اعضای این تیم امروز ساعت ۱۴ تهران را به‌مقصد بصره ترک می‌کنند، فرودگاه بین‌المللی این شهر تمام پروازهای با مبدأ و به‌مقصد ایران را تا اطلاع ثانوی تعلیق کرد
‼️
‼️
‼️
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106261" target="_blank">📅 10:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106260">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31134b7828.mp4?token=YhEZlrh5jXHJPzV69QJZ_bHpTLYOjtpcztMzToOiZQQobsnBZ6YHi64Ea3ryfnk2IQWgwi0AdmYZrc6eyJFoDiFlu8dQKU2Dro7Ro9s0hm56u7KxpmNdxbvfISNJU9LFdJzgYvyoE7wad9Cs9vEEb4rWY9TT5kLN2z4nU5iSkbGsE5fGh5naekZKMeR6hfQwAOcfCIACZYoA_FpYMKWUN5i2Eof6tWsi-wAFjOxPYwxNqCgLido6_erAVm_Cpxz4e3uu8DssEQmS7xKROzxl_ge-QPGw3fPlXq1Xfx-ozcH1sh3RaQY6dZ61aXJfsjOqI-PnoDkSuNs7vwXOwXm8-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31134b7828.mp4?token=YhEZlrh5jXHJPzV69QJZ_bHpTLYOjtpcztMzToOiZQQobsnBZ6YHi64Ea3ryfnk2IQWgwi0AdmYZrc6eyJFoDiFlu8dQKU2Dro7Ro9s0hm56u7KxpmNdxbvfISNJU9LFdJzgYvyoE7wad9Cs9vEEb4rWY9TT5kLN2z4nU5iSkbGsE5fGh5naekZKMeR6hfQwAOcfCIACZYoA_FpYMKWUN5i2Eof6tWsi-wAFjOxPYwxNqCgLido6_erAVm_Cpxz4e3uu8DssEQmS7xKROzxl_ge-QPGw3fPlXq1Xfx-ozcH1sh3RaQY6dZ61aXJfsjOqI-PnoDkSuNs7vwXOwXm8-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇮🇹
اولین‌حضور کومو دوست‌داشتنی در UCL
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106260" target="_blank">📅 09:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106259">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f0128cf1a.mp4?token=OkknDrP8ssSh7FzfoJToJxRK85HqgRi_rtHe_dvbeK9UgEz87Q0z14Wb_6bUe8fDEHAmYg3DHV2i9nMMUYUNSVfvZf5UU-Ix8rYuZZE93MFrG30bwxwW9OE6d6B3q0blTOYjwstaHKOluPWlNGMDOqpqauHIY-vvY2QPZgrbYkQJr5rPGgOGKh4uS1RcZsdMg5KjamtqSqibdw0axtdxCXrE_9E6p6bO1NCubMKVaXnHdHpERqpyhWzPxGw8CjGhuAZeg7-3Kkt27nXB6D7M09OJ1Ub3aH5NI8JserQWAQtM4EF5JbKUSgfJChqhSMf1dqdDVuCJMz0N5nzYZGJoroJZFLc62HQaB0vEphgZr-ucimz42i_VReVFJsexXb3w7opMflKTNBNBrJvUcJQ8PqjGBe1FH6qVIm7_Fm5JlkElxgmEN4PFPHmFtlrMMnTq80IOdW-hwp7K2cx4ocSA8KUYcvw6W36sPwULMPB-FYPXwXaqbthN0iPey8egStO5uMZ3hC5FlwRKDXNIQKxp31rISQBQJq1LOHV5qIhlI3NK8aFbhqFMm0qpFerQvWxt0wqp1kfwwnJQIbRoFX6CrM1TAPr5avPlpg7uZEF97Y3qUqvY122gqy77noU28EcEDPwnaG54UvNJD7syZ7Av9Q9-bEis-fXUDDmHfUDQsFs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f0128cf1a.mp4?token=OkknDrP8ssSh7FzfoJToJxRK85HqgRi_rtHe_dvbeK9UgEz87Q0z14Wb_6bUe8fDEHAmYg3DHV2i9nMMUYUNSVfvZf5UU-Ix8rYuZZE93MFrG30bwxwW9OE6d6B3q0blTOYjwstaHKOluPWlNGMDOqpqauHIY-vvY2QPZgrbYkQJr5rPGgOGKh4uS1RcZsdMg5KjamtqSqibdw0axtdxCXrE_9E6p6bO1NCubMKVaXnHdHpERqpyhWzPxGw8CjGhuAZeg7-3Kkt27nXB6D7M09OJ1Ub3aH5NI8JserQWAQtM4EF5JbKUSgfJChqhSMf1dqdDVuCJMz0N5nzYZGJoroJZFLc62HQaB0vEphgZr-ucimz42i_VReVFJsexXb3w7opMflKTNBNBrJvUcJQ8PqjGBe1FH6qVIm7_Fm5JlkElxgmEN4PFPHmFtlrMMnTq80IOdW-hwp7K2cx4ocSA8KUYcvw6W36sPwULMPB-FYPXwXaqbthN0iPey8egStO5uMZ3hC5FlwRKDXNIQKxp31rISQBQJq1LOHV5qIhlI3NK8aFbhqFMm0qpFerQvWxt0wqp1kfwwnJQIbRoFX6CrM1TAPr5avPlpg7uZEF97Y3qUqvY122gqy77noU28EcEDPwnaG54UvNJD7syZ7Av9Q9-bEis-fXUDDmHfUDQsFs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇩🇪
عملکرد درخشان اولیسه مقابل بودگلیمت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106259" target="_blank">📅 09:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106258">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a312ae120.mp4?token=YsQlkjLJYzzHeT77BLywY775j6wbCwSDFsyzhz2rcue8U4WOzfFHDYv0Us7ZSjLosZG3IjPheMhNtEMfX2SwBIPYquj3Is1ZZAMMXRhQ_QA6ytCiKuAVxUgWl4hnGJBdxXB2biGcjjzeaedAJjsi_SeCugf0n9XHaEDqtQTop8863w5nWu4ZMT5bl2zBtf8IG3t5Kw36YzVhiRz8bSnNDOBzdeQz31yL1RDoo_PEMJLCbYu9InuaaTOFMcMVdBA7ddeG9dnYy9kW3qh9nWq1lw62LiyTobaka63D6rxe7HxMuY3-birYBZ2eek6d8bVTT-wHRJBrvYhQ2Nnm3rMQVX4EfGwE_cV3TsRs4bt_p98EPLHittqEvP-4yPbACG8PbcCMqltS4IF88Iz2SWnfc5vY4OTl6LKG9QLcAWjLxtMxSGuI4XiGOactnYkWOIBcAJs6fiBTvURj5dzfZDJG7-zFNhhJjafHOLCHb47Pn0ef480uRbo-yqt-SaERsbkKpAQ1wq9-sVz2zgMVn7tJTDU_L_jTXLNNC8s-lC9CXqKR9SSHaKe82-Og5D6Fh-FmEPxQn23uBqg7F_z2O6rYhOhhSbwJH7v-mFhpdoCQmCfC0W5iTfGPGUqytBhbnUGwooW2mbaDkQGoVDV3HEDaCpfVMzxuWpfavFi9xW9I4dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a312ae120.mp4?token=YsQlkjLJYzzHeT77BLywY775j6wbCwSDFsyzhz2rcue8U4WOzfFHDYv0Us7ZSjLosZG3IjPheMhNtEMfX2SwBIPYquj3Is1ZZAMMXRhQ_QA6ytCiKuAVxUgWl4hnGJBdxXB2biGcjjzeaedAJjsi_SeCugf0n9XHaEDqtQTop8863w5nWu4ZMT5bl2zBtf8IG3t5Kw36YzVhiRz8bSnNDOBzdeQz31yL1RDoo_PEMJLCbYu9InuaaTOFMcMVdBA7ddeG9dnYy9kW3qh9nWq1lw62LiyTobaka63D6rxe7HxMuY3-birYBZ2eek6d8bVTT-wHRJBrvYhQ2Nnm3rMQVX4EfGwE_cV3TsRs4bt_p98EPLHittqEvP-4yPbACG8PbcCMqltS4IF88Iz2SWnfc5vY4OTl6LKG9QLcAWjLxtMxSGuI4XiGOactnYkWOIBcAJs6fiBTvURj5dzfZDJG7-zFNhhJjafHOLCHb47Pn0ef480uRbo-yqt-SaERsbkKpAQ1wq9-sVz2zgMVn7tJTDU_L_jTXLNNC8s-lC9CXqKR9SSHaKe82-Og5D6Fh-FmEPxQn23uBqg7F_z2O6rYhOhhSbwJH7v-mFhpdoCQmCfC0W5iTfGPGUqytBhbnUGwooW2mbaDkQGoVDV3HEDaCpfVMzxuWpfavFi9xW9I4dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
داستان جالب منیجر ایرانی مسعود اوزیل؛ مهدی کیا: پدر مسعود اوزیل باعث پایان فوتبالش شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106258" target="_blank">📅 09:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106254">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUNeNTa_o6nx98HUYh4VkqOGWl9E2J6gMUAX_0OAZwT_o0ojwkUVYAy_hdjyO8WIeSC_vMzHq36e1-qXS4nxuBwOCqd2V2gf79KL-9g6wLIOJSBdNJxT6Rkff7zv8GQQ-9NG-0D4NgJfIkLiM1CcYl91sTmi9xD7dU84v-A-XaFRdzo2asZpXFIaq_cHUYCtZzQEQYk_nvukdt3IPgwhAOZaJTDo3j7Oo88Des3JgufUj-Zp_LzNNzMQPshj1rspma3AEbI2SebfAhzqq3Qq4iMXuPti7r2gM4bJcQBo3wF1xsWT6vSuZ0AytiX9AAlaHm0A9MMKehUqWZiIhQgi2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
✅
🚨
کیلیان‌امباپه:
🔻
من سال‌هاست که خودم را بهترین بازیکن جهان می‌دانم اما اگر در مراسمی توپ‌طلا به مسی یا رونالدو می‌رسید، اصلا ناراحت نمی‌شدم چون می‌دانستم آنها چه بازیکنانی هستند. اما درباره سایر بازیکنان و کسب جوایز کمی تعجب میکردم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106254" target="_blank">📅 01:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106253">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIqCSKoDjNSLIm8SQGFtXYuF3JLRVBY84Su4pVLVjB8Lrfdert9jEizGeJxqKCg0AO1mR9EsFdBC3DWXiG7TsCbWQu_wZxUSTnfb14BotKW73QqoIsk9DnJXEOocZJ4w5YIWFnmzWPuIhEOLwqhcF3GpxaKOD07JBZ1JrWbfEkIasE2PPlW7bYPZ-ZlBFbD4gqve3eg1coySnebPRk-1oYsuaW0o9ZxTowJADp6GO1j_24cnNvqpk5PWnJEt5BPEI-HzAtbQyg-S0Of42ZJqCwjXRO1_5y1BVIYXNChmSTch9UmDnBcRgGKjIf7jN4BQdVpdaAunRx8NyUuqfaU-jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
آیا فکر می‌کنید می‌توانید مانند لیونل مسی تا سن 39 سالگی بازی کنید؟
🚨
🎙
کیلیان امباپه:  اگر لازم باشد، تا صد سال هم بازی می‌کنم! (می‌خندد).
🔻
آیا کیفیت من هم به همین اندازه خواهد بود؟ این به هوش بستگی دارد: اینکه بدانید چه زمانی دیگر نمی‌توانید ادامه دهید.…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106253" target="_blank">📅 01:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106252">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHzYnYISgxVda6iUtDEA2Imbngy1jxWaDNR-2Mm_GPxpOx5Phq0JXcW6G1BDjwdsX11qQtc7PqRSO6ctbxSM_ieIdBNwrOvoJduaOoEnwc70L1ywJG0xvVjFVwpJI0HZl6xt2jbXhjutG7oO4pwpjAWYieYBDvYGx2dzxq_d-AZhzsU9no282rBf_LZpq4qHrlS4t2w5YX3TkthlRir47QkSgl0Annfm_uLHMWNhGSWGYlPLJOrjWMsj8UkcdoW8urcNs7INW50RTymp4wX91xePDlfjGJ5P1IkcTjr9FpovgSTWOO9nW1xRH8_rcWjLR9q6-iE6hUK9f106QvNtgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
آیا فکر می‌کنید می‌توانید مانند لیونل مسی تا سن 39 سالگی بازی کنید؟
🚨
🎙
کیلیان امباپه:
اگر لازم باشد، تا صد سال هم بازی می‌کنم! (می‌خندد).
🔻
آیا کیفیت من هم به همین اندازه خواهد بود؟ این به هوش بستگی دارد: اینکه بدانید چه زمانی دیگر نمی‌توانید ادامه دهید.
🔻
او نیازی به فکر کردن در این مورد ندارد، چون هنوز می‌تواند این کار را انجام دهد. ضمن اینکه، مسی خودش یک بازیکن فوق‌العاده‌ خاص است.
🔻
من خودم را یک بازیکن متفاوت می‌دانم. اما او هم یک بازیکن متفاوت، در بین نسل‌های مختلف بازیکنان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106252" target="_blank">📅 01:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106251">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srEFAHbRULGeVzipz7jQlElqsFUQXhP9vtbYEzFxtDIL2Adqerl-UfJb6EFQFUaPiT_kBcErmRGNcgmtcwbwKhVbukCNykEaxq9-apjrxIwUnc5cJd95OVtecxAkjWtgIPvSNPZTZ_-X9IbvlUtH4YLderJxp7PLpLNjyG0EgCHy7jwHE0Jfn74Ook74mF7hRAd3h1Z425xW4MIo5eLEsOSf28E_lMR80IgSM-GzeNdIGC7-Cia3zTZpKF5ApOU8ZL1S7zy3v9XxvgDQ6oeLwwxnM2FYUhPKdAXJ1i_tew9A8BBL00qpm7I7OmXsSxoSpXqFLUuzhRBzWvB9ynlK6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😆
📱
استوری ابوطالب‌حسینی: ما نبودیم دیگه تو فوتبال حاشیه نبود و همه پاها موازی بود دیگه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/106251" target="_blank">📅 00:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106250">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b4f3dd673.mp4?token=F9YpUyH3AFc-Uh1Pm3qrcW5ZpY9OWN1rYK5qGr-_rIH0pemqQqg0WwZuEKjguGrYPG0yDzENuqOH60986Dd1ZQozjTkyIw0HMXH281uJMMvtktZynmWFihdM5NRLoEnga3lX-DKcLlX24NTG0-4qdsLB706s4XGtmyphlQTTcR3CUFTxcpznhw6cfa3Ox8slcidVsD-DkAeiSRUeLTx8rbK_BXO7AFNIGdLAEyOotm1EUPePTNqyrXf1tS489ySg_TKKSWd8tz180E_9lVB1DMDX4Nbwi0A3CF52RpGrQ-GgnSB2wRfX_8541k4mRa2K6sZS3ayrlEwtKmXJ0wejrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b4f3dd673.mp4?token=F9YpUyH3AFc-Uh1Pm3qrcW5ZpY9OWN1rYK5qGr-_rIH0pemqQqg0WwZuEKjguGrYPG0yDzENuqOH60986Dd1ZQozjTkyIw0HMXH281uJMMvtktZynmWFihdM5NRLoEnga3lX-DKcLlX24NTG0-4qdsLB706s4XGtmyphlQTTcR3CUFTxcpznhw6cfa3Ox8slcidVsD-DkAeiSRUeLTx8rbK_BXO7AFNIGdLAEyOotm1EUPePTNqyrXf1tS489ySg_TKKSWd8tz180E_9lVB1DMDX4Nbwi0A3CF52RpGrQ-GgnSB2wRfX_8541k4mRa2K6sZS3ayrlEwtKmXJ0wejrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇮🇷
🇮🇷
آنالیز بازی استقلال و پیکان توسط تقوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/106250" target="_blank">📅 00:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106249">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdncZ63OEvZ7vZQ7ZVjwrfXP6DGtUTUgQNcwy4kyfIlYwXe4SP9z9MbuDSo32n416BqpwFYb3Qca8CoUL2MpyUnwImOoviRA-LL4ja007jHgseL7-xnm60Ew7piyj_T7PJDCxGHRPy10k1BwAj3Mij5bYKJo0ry40kI9DCp8vGDCt7LNe0vOwNKuurfKdG1ON5Q6h_WnDqbW2Oy0ACeo_g3F-TCw30Wr7NwukSO2sYRR50xV-cJ9AtDFVn0Y6OVZbgqxWSiQzOJueUe8p1tO2Dy_m0Mhv54ABsnWxIsV0CmJvR91L9XStyjpoEDulWs_FLiCvZU_LM_XPTothTmyDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
⭕️
🇮🇷
با اعلام باشگاه استقلال، مشکل مصدومیت یاسر‌آسانی جدی نیست و این بازیکن برای بازی روز دوشنبه مقابل السد در دسترس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/106249" target="_blank">📅 23:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106248">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4uLcSTi_uOuMpYb-hUTpJ57E9QYrJeuHsToeXALFQvSoQISSAa-lyumVvl__G6Y3piT_JvdqvDhqfeZRvw8PnH598xqCnz-Jy2dtbJ19-35nYXmcxZiWxgnfuSyuqPEmst9dTCxsTMFfAJ6-JFp9viGh3i_bRvGtx0CayoPpijfLPz-fPwTCnT6-KXXu7VRfnrGGjhG-NDCkzxR1n1MsesjTgfOzrtNKNnOdzQPmJSdmmF82TUosW7WsarBUw9Vs0Rye-79CdjYjwAIHY1KGtSy6M_xF3su1EhYCafLdzM3Z2tMheSJn11kVWFrEpJhM0FdXkVqsWLAPvpfRaoDwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🙂
🇮🇷
نحوه برخورد شجاع خلیل‌زاده با مدافعان تراکتور: حمال‌های بی‌خاصیت
❗️
❗️
❗️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/106248" target="_blank">📅 23:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106247">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63b0b11397.mp4?token=IP2rb4Ba5Qk6pjXXN2xN2cGb_TkuzSOo4wkqYLfHRsBe3onNeGCFPofkmIanCtxioPNSvZVKnIPCCVw-SiV5wKDkDDn4rZcsXQBRIs4BNf6yJQNkCRp-NyI34-l59u_xiQsRulU8jo_koG2eFy4pdij8EqG1RnFLSftsvlYR5hA7hdnk0MrNDIwgmXdpkzmZUu8Me8JiDZwrJVO-wQl0UxvM0yZkiM7ml9PBCf0rExxZhnkHjivPEVFQdPBxdNahVLYQfctjTZaPl-8RwG322f4IsUloc_9GdquDR7SnlM_VnxKIumHNWqyQYGAvH0Dx-c8vnE7M4Gukmi5I1V3IuJASbDw-rYSytj6bdJg0TxKNrkpmDihMHa740vGn-cTVF7GShFvOHYIZ9AK3pr40ztftzVmY2rLF37olaKnijQJNd8vvFiS4gkyikOrCMHGhoZRyx2IspqX6k6xwZiY5O8qGgixqljWvIVQuOrUC5aEdQJMQ47qjScPPDfZ1czq3FHabV8o5ELFkiEwYPgG40ez1-xCZDFw4aMqZVvoL_i9PeQqpcgHB6x6VlUm2u6UvqqTAjjZnawd_QRWBq_ftHxIkmXJ5XZqCOCqyOqSIDOoUGbCrH3wYyJOkz2oG7JQaGnEMxIDJW2oOrLHHA6gi8aeadCFnBh7xukQRUS44bvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63b0b11397.mp4?token=IP2rb4Ba5Qk6pjXXN2xN2cGb_TkuzSOo4wkqYLfHRsBe3onNeGCFPofkmIanCtxioPNSvZVKnIPCCVw-SiV5wKDkDDn4rZcsXQBRIs4BNf6yJQNkCRp-NyI34-l59u_xiQsRulU8jo_koG2eFy4pdij8EqG1RnFLSftsvlYR5hA7hdnk0MrNDIwgmXdpkzmZUu8Me8JiDZwrJVO-wQl0UxvM0yZkiM7ml9PBCf0rExxZhnkHjivPEVFQdPBxdNahVLYQfctjTZaPl-8RwG322f4IsUloc_9GdquDR7SnlM_VnxKIumHNWqyQYGAvH0Dx-c8vnE7M4Gukmi5I1V3IuJASbDw-rYSytj6bdJg0TxKNrkpmDihMHa740vGn-cTVF7GShFvOHYIZ9AK3pr40ztftzVmY2rLF37olaKnijQJNd8vvFiS4gkyikOrCMHGhoZRyx2IspqX6k6xwZiY5O8qGgixqljWvIVQuOrUC5aEdQJMQ47qjScPPDfZ1czq3FHabV8o5ELFkiEwYPgG40ez1-xCZDFw4aMqZVvoL_i9PeQqpcgHB6x6VlUm2u6UvqqTAjjZnawd_QRWBq_ftHxIkmXJ5XZqCOCqyOqSIDOoUGbCrH3wYyJOkz2oG7JQaGnEMxIDJW2oOrLHHA6gi8aeadCFnBh7xukQRUS44bvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
کنایه‌های تند وحید هاشمیان به حدادی:
🔻
حداقل درویش از مدیریت الان مرام بیشتری داشت و به نظرم برکنار شد چون من را برکنار نکرد. چطور برای اوسمار این چنین مراسم بدرقه ای انجام دادید ولی با من این گونه برخورد شد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/106247" target="_blank">📅 23:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106246">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1d2ea919.mp4?token=Q62Z05LQw18oQVpy39yCyQ_y8kwjGweWfpr15Avp62vyENwIY4Eb2sCLXpf2xiCnYSJvBJVfwBoIGbr6Rcf8Im5SeWJI9ehs4fARsur3-EOgrfaPgc6tClH5FlvEFD-69zPb7snmK-SCuecWlBUHO_QBCfgvO1E8zdFjrHCb5-X0cnSFNrOCzJISnhjcZ2yVjyi0bKE7mmaV3vO08wr1XmXB1uWz5EmBWy5WxQX1pVR3Ktd6iZNFi5Una-AOxuakC6QWCdfCANM65xHkrjzGM2anPE3MWXzqNhAtZSJwg5sxcwRs7UCp6rnRdY4vXFEA5Uk9l90kDSZpCN63gFJkMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1d2ea919.mp4?token=Q62Z05LQw18oQVpy39yCyQ_y8kwjGweWfpr15Avp62vyENwIY4Eb2sCLXpf2xiCnYSJvBJVfwBoIGbr6Rcf8Im5SeWJI9ehs4fARsur3-EOgrfaPgc6tClH5FlvEFD-69zPb7snmK-SCuecWlBUHO_QBCfgvO1E8zdFjrHCb5-X0cnSFNrOCzJISnhjcZ2yVjyi0bKE7mmaV3vO08wr1XmXB1uWz5EmBWy5WxQX1pVR3Ktd6iZNFi5Una-AOxuakC6QWCdfCANM65xHkrjzGM2anPE3MWXzqNhAtZSJwg5sxcwRs7UCp6rnRdY4vXFEA5Uk9l90kDSZpCN63gFJkMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
محمد تقوی، درباره پیروزی استقلال برابر پیکان در هفته هفتم لیگ برتر گفت: «استقلال نمایش خوبی در این بازی نداشت اما باید این بازی را می‌برد. خط دفاعی استقلال آشفته است و با این شرایط در بازی‌های آسیایی مشکل بزرگی خواهند داشت.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/106246" target="_blank">📅 23:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106245">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/657c84dea6.mp4?token=BRpeiL3-zrpwMGAo92VFKwfBdSZ4phZcs2_LEEDN1s0JjsuM1SW8rrZvNC_95W6h6IblauA6DcDfdbv2pdwNv6OnnoAaIl-nqj3lwLPPzebcm7FACURYpEWGDXg1lndy3jib1dlozCX0W_hGW0tCQJ8gOh_kgfb39xW2ZKgr2Gw7IC_jpZB6Ws8-pWSDu_BKVIF5Hc5Zts_UMtWCwImxZa1Ib7TmLpvx8GLJIXQVZ9QEA4l_g1VMiXwxF6nhIOgrLTxEIcu-HaUP0PBjJ4s8YdfPoQ-M8mH4ehtAqE5qlC2w5GT3ZwhXze9pJe5cszuv8raWvAqKsf6sR3uVzW3wXZOYDsMb6EL7ZR1-W0UVjdoYYGLt6EpcafdXAf9f15tvOYL6NBtYKeHbSxdqGFPQxxKbM_a14chbEEzdNmZ63jptsxnYsh76oYhsVijuJ8ny2NvWIdNYQgjt6aOAhUCr13Pc4yWNmUfKHoZpuxEJsf1pBFmg3HUQiy3_JwISo_ybVQB0tkaPB8vRnvNyZFOlKe0UTPyDiisDOewg1NSL4hlTfD-RO9rdJksKSgqITPQo6lHgTxK6LVlTFeCAEmaWKnhV8_05xMe4qlJZKPlipqwVkqEEHsUcO4uvV-L4SKA3XagQOttJEltbg5q82DCuTt99or2RICD9kHs6alnhEeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/657c84dea6.mp4?token=BRpeiL3-zrpwMGAo92VFKwfBdSZ4phZcs2_LEEDN1s0JjsuM1SW8rrZvNC_95W6h6IblauA6DcDfdbv2pdwNv6OnnoAaIl-nqj3lwLPPzebcm7FACURYpEWGDXg1lndy3jib1dlozCX0W_hGW0tCQJ8gOh_kgfb39xW2ZKgr2Gw7IC_jpZB6Ws8-pWSDu_BKVIF5Hc5Zts_UMtWCwImxZa1Ib7TmLpvx8GLJIXQVZ9QEA4l_g1VMiXwxF6nhIOgrLTxEIcu-HaUP0PBjJ4s8YdfPoQ-M8mH4ehtAqE5qlC2w5GT3ZwhXze9pJe5cszuv8raWvAqKsf6sR3uVzW3wXZOYDsMb6EL7ZR1-W0UVjdoYYGLt6EpcafdXAf9f15tvOYL6NBtYKeHbSxdqGFPQxxKbM_a14chbEEzdNmZ63jptsxnYsh76oYhsVijuJ8ny2NvWIdNYQgjt6aOAhUCr13Pc4yWNmUfKHoZpuxEJsf1pBFmg3HUQiy3_JwISo_ybVQB0tkaPB8vRnvNyZFOlKe0UTPyDiisDOewg1NSL4hlTfD-RO9rdJksKSgqITPQo6lHgTxK6LVlTFeCAEmaWKnhV8_05xMe4qlJZKPlipqwVkqEEHsUcO4uvV-L4SKA3XagQOttJEltbg5q82DCuTt99or2RICD9kHs6alnhEeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇶🇦
کامنت‌ هواداران پرسپولیس زیر پست‌های السد: قرارداد آسانی غیرقانونی است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/106245" target="_blank">📅 22:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106244">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9444ed9ae1.mp4?token=nTbvjl8hGomVijSuCSGAtlMwu51K6UCB_H3umt74snJSzSD5QQ98YmDOyiUKjn3g5K23SbYTxQAsvOSpV7P5xn49p70K_gF4Ie8OEmglRQPklIDsMyHKBhhfPZ0bX6CEFMjbPtLXvVYRAENbdWKpXQRDK2T4gpzVcxpTuKIlssmLzFS57-oaZkO3IE6d0V2qE7LUhagi8hWZs6gpigPxBkrQqJ7ArwkY0RNWfmHKRhgnOkFvZbX_VJWWOeqootigzCgnMLY5dWQ3wWSkvr6FGvgu3zjCUws8r4LMBqy5WrskmgyfEPcKtP4AJJw4Fw7QTkn37Ht0GHIVMPYSIiQ9kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9444ed9ae1.mp4?token=nTbvjl8hGomVijSuCSGAtlMwu51K6UCB_H3umt74snJSzSD5QQ98YmDOyiUKjn3g5K23SbYTxQAsvOSpV7P5xn49p70K_gF4Ie8OEmglRQPklIDsMyHKBhhfPZ0bX6CEFMjbPtLXvVYRAENbdWKpXQRDK2T4gpzVcxpTuKIlssmLzFS57-oaZkO3IE6d0V2qE7LUhagi8hWZs6gpigPxBkrQqJ7ArwkY0RNWfmHKRhgnOkFvZbX_VJWWOeqootigzCgnMLY5dWQ3wWSkvr6FGvgu3zjCUws8r4LMBqy5WrskmgyfEPcKtP4AJJw4Fw7QTkn37Ht0GHIVMPYSIiQ9kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💙
سعید فتاحی رئیس سازمان فوتبال استقلال: به غیر از خلیفه و گودرزی در نیم فصل هربازیکنی سهراب بختیاری زاده بخواهد باشگاه استقلال جذب خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/106244" target="_blank">📅 22:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106243">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dab1b117ec.mp4?token=sZ-RYR3qLdjbnxs8y-GFEnIrv9vi_SbJnrVYLL9CR4-HKeKgREQ_kGFTggFwGqrQ6yiTtBLE2AHhykG4rpIj-b1Z1L1RU610H2u9LxETLd4qzTbAsx8kUnIwdys_dm5tGw_qWkiou9QIelctLJ2NRSksl9p9MhTrK6ijq5zVRtY92cHmCEG35RW_yY8mlqeWJa60M_SdCMdoXCzidLMor-at6iBHSuZfLf_kQ1mZZCBXSQXkXsNYRdHI7cR-yo04RgqPlZVqYOWPTNt1PZ4shS2FomMy_M9o3ixZix-wfnnDUQNbgUtkZjEtJvs-F5DeSb1Ujs6cEG29GwlYsnxEWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dab1b117ec.mp4?token=sZ-RYR3qLdjbnxs8y-GFEnIrv9vi_SbJnrVYLL9CR4-HKeKgREQ_kGFTggFwGqrQ6yiTtBLE2AHhykG4rpIj-b1Z1L1RU610H2u9LxETLd4qzTbAsx8kUnIwdys_dm5tGw_qWkiou9QIelctLJ2NRSksl9p9MhTrK6ijq5zVRtY92cHmCEG35RW_yY8mlqeWJa60M_SdCMdoXCzidLMor-at6iBHSuZfLf_kQ1mZZCBXSQXkXsNYRdHI7cR-yo04RgqPlZVqYOWPTNt1PZ4shS2FomMy_M9o3ixZix-wfnnDUQNbgUtkZjEtJvs-F5DeSb1Ujs6cEG29GwlYsnxEWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
🎙
نادر محمدی منجنیق: به صورت اتفاقی این نوع پرتاب رو یاد گرفتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/106243" target="_blank">📅 22:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106242">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
⭕️
⭕️
🇮🇷
با اعلام باشگاه استقلال، مشکل مصدومیت یاسر‌آسانی جدی نیست و این بازیکن برای بازی روز دوشنبه مقابل السد در دسترس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/106242" target="_blank">📅 22:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106241">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3e40e30b.mp4?token=OVVtILAo4QEtrJCqwrPZB05AMDh1j7PMDTgstb9ymGtyUgYmK4qyJ53VxrjTizWEofShOBioFo2YUawS_72WrjVJiBGoLRnKOEa5viIrj0EC2YmW3eVz3NDjLlURLn9GMFDqNIpiov19T0_BY9jn4h714OgfomWUGdOmpSq3odAGqXiib2ts8MIzsE8YBGhYZ-R5WcN7AqAS51eM3xRNo5-ilCFseMs-sRw1HH2V-z-apnEhz3VtmqSssZlwYL5yWdM39MODbX9sXmyweL14wNeEQ3dLvvBY75C4gk1MWZcJCFdT-gvW161ksSn-OejpkugfWfPa0cz7XY0Wxph19C-fpifuv3jVD7qpNwlZpXVHVqqxeNLN4y_-gkXZTveNWpKDZEAUM1VqBqLXm_Bof-6V6aDFiEEiiNERWToZ7qqsZmDjgaf9qykf3vDndGkFlwaDqQ7c6LtRFmgHJVAZAx2KezVKrxDKv2ZSIjHmtHYNZFnH6PtuRppcmy8qWLM4IPOLydPw1tYzGrZX3jNti7H4h2j12807ANAHD7IGPkfZbxYCD3KzGbg-YBY9verKKIeDP0CV9XoD3USr8D4N0yr1sO5BnI0IipyM-qIPHaIJLsPEf48oK3rbTajX_sEf2d6nbXFrU26BJ2KYfZbfl8UqZk8ioWezLBUF59ODG40" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3e40e30b.mp4?token=OVVtILAo4QEtrJCqwrPZB05AMDh1j7PMDTgstb9ymGtyUgYmK4qyJ53VxrjTizWEofShOBioFo2YUawS_72WrjVJiBGoLRnKOEa5viIrj0EC2YmW3eVz3NDjLlURLn9GMFDqNIpiov19T0_BY9jn4h714OgfomWUGdOmpSq3odAGqXiib2ts8MIzsE8YBGhYZ-R5WcN7AqAS51eM3xRNo5-ilCFseMs-sRw1HH2V-z-apnEhz3VtmqSssZlwYL5yWdM39MODbX9sXmyweL14wNeEQ3dLvvBY75C4gk1MWZcJCFdT-gvW161ksSn-OejpkugfWfPa0cz7XY0Wxph19C-fpifuv3jVD7qpNwlZpXVHVqqxeNLN4y_-gkXZTveNWpKDZEAUM1VqBqLXm_Bof-6V6aDFiEEiiNERWToZ7qqsZmDjgaf9qykf3vDndGkFlwaDqQ7c6LtRFmgHJVAZAx2KezVKrxDKv2ZSIjHmtHYNZFnH6PtuRppcmy8qWLM4IPOLydPw1tYzGrZX3jNti7H4h2j12807ANAHD7IGPkfZbxYCD3KzGbg-YBY9verKKIeDP0CV9XoD3USr8D4N0yr1sO5BnI0IipyM-qIPHaIJLsPEf48oK3rbTajX_sEf2d6nbXFrU26BJ2KYfZbfl8UqZk8ioWezLBUF59ODG40" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
✅
🇺🇲
بررسی حادثه ۱۱ سپتامبر از این زاویه؛ برای دوستانی که اطلاعات کمی دارن دیدنش توصیه میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/106241" target="_blank">📅 22:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106240">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16ebf2050a.mp4?token=YPyK8tgttyeuhytC45sS-K-_-iHMmLC7e1Z-D7aGxEGzW14yms3Z3dGdFEI0EJl164EJG_elc9ZGmpB_-Qq9PtMmMQ7-pjUf4aJKtyx89QIIfg84DuOLianGoXc40VRpMAxszCfwwxmfs3j0TVuM40a34uGowB2i8A4Ok4yud32WmBYtc4YpFC_OZoFj985WsLhZutYM0FkG_NOhOyW1LsbWX_-CpiavgBEk8IqsVpQA8NLxyhU7oqQ5cKlGuwbhl9475LuJTygvwz2eYZjq6TD7yGdthJDUjz7fEl78JDkq4Vlhx0SprTfC7sDbL9p72PRAtLLgsdjBh23xwCUaxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16ebf2050a.mp4?token=YPyK8tgttyeuhytC45sS-K-_-iHMmLC7e1Z-D7aGxEGzW14yms3Z3dGdFEI0EJl164EJG_elc9ZGmpB_-Qq9PtMmMQ7-pjUf4aJKtyx89QIIfg84DuOLianGoXc40VRpMAxszCfwwxmfs3j0TVuM40a34uGowB2i8A4Ok4yud32WmBYtc4YpFC_OZoFj985WsLhZutYM0FkG_NOhOyW1LsbWX_-CpiavgBEk8IqsVpQA8NLxyhU7oqQ5cKlGuwbhl9475LuJTygvwz2eYZjq6TD7yGdthJDUjz7fEl78JDkq4Vlhx0SprTfC7sDbL9p72PRAtLLgsdjBh23xwCUaxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❤️
محسن خلیلی مدیر پرسپولیس: چرا می خواهند ترمز پرسپولیس را بکشند؟ چرا می خواهند حق پرسپولیس را بخورند واقعا این شائبه برانگیز است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/106240" target="_blank">📅 22:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106239">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/febf5e7a8e.mp4?token=M2QzXdom2z3ZdA2ZVPTnuUNxJjgb549xxUg1MX1K-kChaRBJ77hppdT8JaXQ-vkHVFYCP7BG-3U-nXJNtzN3YFxM60U9i1ReLwrgQqDt1Mhq7AUnO5N8u2McbCAnx-Spj0Cm1p9nOL3i0MDeAWXP_LcSXiHW9vp2Wyf_bKhx_gey2jL41TFPMvJtgdWYEue_ImfJitI9rFfgr93ujYWbFBFdRgVNcvbLHP2p2ZH15AX-gvbUJa8VV9jrmJ6nSAZ2-zKm1NM87_-ydZOA_TdWc4_5AsjvphxKaN5BALhe6zOGfLXSK2kjepAzrWhC2jUre_LeMyaQ347AIixnR2LX6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/febf5e7a8e.mp4?token=M2QzXdom2z3ZdA2ZVPTnuUNxJjgb549xxUg1MX1K-kChaRBJ77hppdT8JaXQ-vkHVFYCP7BG-3U-nXJNtzN3YFxM60U9i1ReLwrgQqDt1Mhq7AUnO5N8u2McbCAnx-Spj0Cm1p9nOL3i0MDeAWXP_LcSXiHW9vp2Wyf_bKhx_gey2jL41TFPMvJtgdWYEue_ImfJitI9rFfgr93ujYWbFBFdRgVNcvbLHP2p2ZH15AX-gvbUJa8VV9jrmJ6nSAZ2-zKm1NM87_-ydZOA_TdWc4_5AsjvphxKaN5BALhe6zOGfLXSK2kjepAzrWhC2jUre_LeMyaQ347AIixnR2LX6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❤️
محسن خلیلی مدیر پرسپولیس:  2 تیم ( استقلال و تراکتور) با تیم ملی امید همکاری نکردند و بازیکن ندادند چرا کمیته انضباطی با آنها برخورد نکرد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/106239" target="_blank">📅 21:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106238">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a557a62450.mp4?token=nxZD7UR81-XAQhyxjKtknhhEF1FEY6kIBhaZUT_nEKK-655PUEda3rxJiMQILbUUwn6zuAsaJs9vWZH7bqAaKscACHm4gcQ1DZuXEpQUpJnL3LACnPVDp5uT7c6aRiI5q7ZV1K8FEnGFjchCuDseGzn9u9lPyXOkDrlE_UifENAc0OA_e5YFcrtOAiklDkPtLAmVBPEYHZdzWfzyeWqrKY4id2phJ9egOOsxIrRNeTx8rF7PO3N-1pJo8Wy-LAtb0h3Nt_0YmiT62QHxC1ISxGOcWY7dSOpCxhdqqlgBD2k2NRY3l4hHrnishTqyIF26I9i36hS1vDH1LIOzXB3eyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a557a62450.mp4?token=nxZD7UR81-XAQhyxjKtknhhEF1FEY6kIBhaZUT_nEKK-655PUEda3rxJiMQILbUUwn6zuAsaJs9vWZH7bqAaKscACHm4gcQ1DZuXEpQUpJnL3LACnPVDp5uT7c6aRiI5q7ZV1K8FEnGFjchCuDseGzn9u9lPyXOkDrlE_UifENAc0OA_e5YFcrtOAiklDkPtLAmVBPEYHZdzWfzyeWqrKY4id2phJ9egOOsxIrRNeTx8rF7PO3N-1pJo8Wy-LAtb0h3Nt_0YmiT62QHxC1ISxGOcWY7dSOpCxhdqqlgBD2k2NRY3l4hHrnishTqyIF26I9i36hS1vDH1LIOzXB3eyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببینیم دیشب در لیگ قهرمانان چه خبر بوده.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/106238" target="_blank">📅 21:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106237">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiX2lyfD0bIUMpxHjjSnHrzdStHy0IQ2HQH-9PQJ3XApsw3viT_ipiIb9XYbJCRbythmL6f_NB6bfxl_TobCbd-A39GDorAHt8qaDYFw9wzClqRCGy_LD--z-jZOX7sFnrQfYHImg-0YgGFrPR8Cvpm185v7xp3Dmc3DzwwtaV8ki6McQCC0I6ZJYRUC-QBZ9ahdiSaTokUAuFjz2GLF2Ek9qllYvRzt1louSVR-xDKmpYSRsB_DwO93Wq8L1VRF3Q6hZ5zPNS8PtPb5WWl-oEynEfmrxSv-2jwsdwE-0Vw5QT3smW6h-3GlL2aHzqk1zAYWhFrU4MlOksderUPFLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇮🇹
🇪🇸
سسک فابرگاس، سرمربی کومو:
🔻
«بارسلونا ترسناک شده. سطحی که تیم در حال حاضر داره واقعا ترسناکه. بازی دیشب رو دیدم. فاینورد تیم خیلی خوبیه، ولی بارسلونا کاری می‌کنه که حریف ضعیف به نظر برسه، چون در هر لحظه راه‌حل پیدا می‌کنن.»
🔻
«می‌تونی مقابلشون نفر به نفر دفاع کنی؛ همون‌طور که فاینورد سعی کرد این کار رو مقابل رودری یا پدری انجام بده، اما بارسا از هر نقطه‌ای راه‌حل پیدا می‌کنه. فرقی نمی‌کنه چه بازیکنی وارد زمین بشه؛ سطح تیم همچنان خیلی بالاست.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/106237" target="_blank">📅 21:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106236">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/525ed46310.mp4?token=kp2d6r1VD3CXV84tzpv97mtMZSCszXtbVudrqDObZtTX_jAHROH3VwQTzXjN0xax0r5RY_Na-JikmVP76DzuA2sGfKyHd7gcglNfG3lf-vy2d3rAp2lEKmumA8bNZaUdq_LMyp1zu2o_85frVBTskqfvcCmF3xie7ZB95u8XaVCh4D_z2DElG3OBQ5Pg8Z6MxGNbPH2TsIaETVFYijnUXXc_D7ODGMsJOcykbBYxeldtzmFvXgHa5sT4geXZAfQH0fp2Pm8ixxB2WBvvH7LPYlKpXVoKTO8Zt4AjluXsf1Qtfl2CbI9jBVjHpRuYh0jSSnOyVhCjjWD5XWK2Xps52A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/525ed46310.mp4?token=kp2d6r1VD3CXV84tzpv97mtMZSCszXtbVudrqDObZtTX_jAHROH3VwQTzXjN0xax0r5RY_Na-JikmVP76DzuA2sGfKyHd7gcglNfG3lf-vy2d3rAp2lEKmumA8bNZaUdq_LMyp1zu2o_85frVBTskqfvcCmF3xie7ZB95u8XaVCh4D_z2DElG3OBQ5Pg8Z6MxGNbPH2TsIaETVFYijnUXXc_D7ODGMsJOcykbBYxeldtzmFvXgHa5sT4geXZAfQH0fp2Pm8ixxB2WBvvH7LPYlKpXVoKTO8Zt4AjluXsf1Qtfl2CbI9jBVjHpRuYh0jSSnOyVhCjjWD5XWK2Xps52A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😳
😳
😳
اینارو از کجا پیدا می‌کنن
😂
- کارشناس صداوسیما می‌گوید ذخایر طلای بانک مرکزی ایران ۵۰۰ میلیون تن است!
یک ۵۰۰ میلیون تن و یک ۸۰۰ میلیون تن دیگه هم گفت تازه
😂
حالا جالبه بدونید که کل طلای کشف شده توسط بشر در طول تاریخ ۲۲۲ هزار تن بوده
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/106236" target="_blank">📅 20:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106235">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e059f4f8a8.mp4?token=fsrb27Lr2QnyzviOXdfDPl6l_ncGvma9LbzcMtZpdh8TL36OPSx5mv9hP3BpdnDMvbhEzhJaBiOiZlYczHjcWiXr6Brzb0aiXSI7_78qANJ-f0Yj9REAX9HFLCtqnBjg9YOf-Cwl7lBiobAgCmW4KKL1rOL1lzeb22__zPU_tkIaDHyhccPw4wv_79Ewv0prm9FHu3pCiNNgsdpzUCSuGn2rRNjh0VsxTTbvzbNFAOwZtPqECQyJ64_NGvzmU0W5NCGum8_j8Nb-I5BNObNihfv4dgwHhZfIKoCVsvvNLyt6IM7rC-QNWHHBqrjekuZj5p3VzadjWQFzNH1H1XWFCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e059f4f8a8.mp4?token=fsrb27Lr2QnyzviOXdfDPl6l_ncGvma9LbzcMtZpdh8TL36OPSx5mv9hP3BpdnDMvbhEzhJaBiOiZlYczHjcWiXr6Brzb0aiXSI7_78qANJ-f0Yj9REAX9HFLCtqnBjg9YOf-Cwl7lBiobAgCmW4KKL1rOL1lzeb22__zPU_tkIaDHyhccPw4wv_79Ewv0prm9FHu3pCiNNgsdpzUCSuGn2rRNjh0VsxTTbvzbNFAOwZtPqECQyJ64_NGvzmU0W5NCGum8_j8Nb-I5BNObNihfv4dgwHhZfIKoCVsvvNLyt6IM7rC-QNWHHBqrjekuZj5p3VzadjWQFzNH1H1XWFCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
فراز کمالوند سرمربی خیبر: الان که پرسپولیسی‌ها مخالف هستند 3 ماه پیش هم که پرسپولیس اصرار داشت تورنمنت 3 جانبه برگزار شود همه مخالف بودند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/106235" target="_blank">📅 20:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106234">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzVlwYLhImNUOi8zTLITxaTkc4FnbNCrWUq0RcFcnaGm3NWUGiK50ocG5WcOuUxBSBP0NNVoojZRtM1UZa_WXKsUC_3kJiuSx2hJjJS18YFIQ5T85Mi97R5-WEl1fhhU1-SN5JMsM8j2bA4-fwzU6zWcM8Ykzn-26OONb5V4BvXUlReVur6I3JyhJ2djTJ8YFYGoY9qGYC5tRFhNpM04HhZHcFuwAClFawaAuchDuM9gu4EkT_s5EbZQjMszo45rVzhlNahNnlbQsQv20OfBWfNFlZ8ae2DQz8ORQ3N0VseR5IUYbAiYB793OvlpVuDtLH66H77Q9Zka0KqpL7wzOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین‌ماهینی عزیز و همسرش
✅
🔥
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/106234" target="_blank">📅 20:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106233">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d8215d3c.mp4?token=AeT7glE21iOVuPKAh5gX_gtQsfyFVsh2WFc3wv728zdZw6PFNfR98WDgvr_QH-Xs9pOCRkXp8_qp7I81Yh6pC4xGZ4OgkaVJZAQVsvRREn63lXaSI3JfNBxHUlhUGciCCKbArua5L-nFGfAPy_43jWXEBz1YODpYoefTeqKYnNHxgOIjxUZmbkPSVt1jOApYkSTOMJAq6gVXtZ06o2eLgjQFlR6eZe1ofo6gYUTQOXgu7nvVur44Ej8KfutnuUDitpPcCFiuEesN9UrJEgE8Ikbofos4b0Ds44QmSO4plX44DeHwX1SIDPN2Fk9etLwlvWEkJx0ahyXTNV1Yq7pMW1DrTNmYPZIlHUCAniUPMFQtuP_OL2_BwT8dtXRoTObVCunRjWi_e4G9hqp4kyZpZ3bUqr6X8P6R4aZhKjygeMRLF2JUIX6fIXy5URjVJEDaVa0JxZwbp0bbZ9lchC4fGp6gQhvO-_FELBWDlpA2F0aLZhvAoArX5KDLAPP8m-n0aHYQUe8K_t4wT5ZRKkQfli9Nr0aqHyIUlqIQB5onxHdi0aAunVO-z4brCYdvhwK1h4Lb6B7hapr_CtN0oREKF93BAA1T4ATWJepi0pnygBX5xdC11E8OLsZRayGCBHAAfX68eaY3NsOl1Q1x_iH3LEtPwNx2BGZWJ72m_leVahw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d8215d3c.mp4?token=AeT7glE21iOVuPKAh5gX_gtQsfyFVsh2WFc3wv728zdZw6PFNfR98WDgvr_QH-Xs9pOCRkXp8_qp7I81Yh6pC4xGZ4OgkaVJZAQVsvRREn63lXaSI3JfNBxHUlhUGciCCKbArua5L-nFGfAPy_43jWXEBz1YODpYoefTeqKYnNHxgOIjxUZmbkPSVt1jOApYkSTOMJAq6gVXtZ06o2eLgjQFlR6eZe1ofo6gYUTQOXgu7nvVur44Ej8KfutnuUDitpPcCFiuEesN9UrJEgE8Ikbofos4b0Ds44QmSO4plX44DeHwX1SIDPN2Fk9etLwlvWEkJx0ahyXTNV1Yq7pMW1DrTNmYPZIlHUCAniUPMFQtuP_OL2_BwT8dtXRoTObVCunRjWi_e4G9hqp4kyZpZ3bUqr6X8P6R4aZhKjygeMRLF2JUIX6fIXy5URjVJEDaVa0JxZwbp0bbZ9lchC4fGp6gQhvO-_FELBWDlpA2F0aLZhvAoArX5KDLAPP8m-n0aHYQUe8K_t4wT5ZRKkQfli9Nr0aqHyIUlqIQB5onxHdi0aAunVO-z4brCYdvhwK1h4Lb6B7hapr_CtN0oREKF93BAA1T4ATWJepi0pnygBX5xdC11E8OLsZRayGCBHAAfX68eaY3NsOl1Q1x_iH3LEtPwNx2BGZWJ72m_leVahw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
آشتی جالب هواداران نساجی با مجتبی حسینی سرمربی تیمشون بعد از فحاشی اخیر به وی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/106233" target="_blank">📅 19:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106232">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLOlg9ubryCsFJt2jpjfbD75DzTvibLeH4xBsf7rMgNTT-qZzU5MjFtVd-LjUxbrF2KM-svCKlzFq6K2-utWxQVRPIj0Rp2CTwXXRoaAlyN725hLKBK-7wu6nlQa_GSRVh3wW22Ps_yn6oFmIxiOrZKCyw_RNLAdX-HAoxAktUHO2sS6j2tEzEQIK470ouDsqBy80ymreCzWPxsie0-MeWpSa-DkGkDc94oGQzOL_A-fNK9gvS5SKpUHkAdbcNkbSRv8gYL--8jf3HMXeHV36W_bdl84FAcAcS9UScET2VwBTw8EwJjHjmZgehOxcdymFXP6SWsY6AbJYqcZ9_LANA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🇮🇷
طبق پیش‌بینی‌ها، یکی از پربارش‌ترین پاییزها برای ایران در راه است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/106232" target="_blank">📅 19:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106231">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be84e2f3d7.mp4?token=E36FXk79Lre-2jniGlE_FNSRkd8QASL9dpiKJqMSzm-FsElvpam0Dk4hGFSuduv_SYJR5r1idxfHuWDq2X-HwCRRwh92PcQ2lPTJ_U63Mn0dpR9A1k2cc2X2Seee9UOEMqDchADR3aRyAn_Adcufw4Fre_9_oMxGZCNRVFF0lMD32xZIg2GvNt_Wd0DQByMmJgQwx2m3CXrFIjQyPH0tJHUl7pU3i6hmok0o7mX-UULL3G1NsnUKScyhTAea7PKt27Ik0-DG4L9glt7puuzcWWm-E-BA6CVQDfh2awI3aqF1KzOFn8-H2vZXUW8XETxPdEPB2dEHpGGCVR_L_AqSRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be84e2f3d7.mp4?token=E36FXk79Lre-2jniGlE_FNSRkd8QASL9dpiKJqMSzm-FsElvpam0Dk4hGFSuduv_SYJR5r1idxfHuWDq2X-HwCRRwh92PcQ2lPTJ_U63Mn0dpR9A1k2cc2X2Seee9UOEMqDchADR3aRyAn_Adcufw4Fre_9_oMxGZCNRVFF0lMD32xZIg2GvNt_Wd0DQByMmJgQwx2m3CXrFIjQyPH0tJHUl7pU3i6hmok0o7mX-UULL3G1NsnUKScyhTAea7PKt27Ik0-DG4L9glt7puuzcWWm-E-BA6CVQDfh2awI3aqF1KzOFn8-H2vZXUW8XETxPdEPB2dEHpGGCVR_L_AqSRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
به مناسبت سالروز واقعه ۱۱ سپتامبر یادی کنیم از همدردی مردم شریف ایران با آمریکایی‌ها؛ این درحالیه که کشورهایی نظیر عراق جشن و سرور به پا کرده بودن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/106231" target="_blank">📅 19:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106230">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHu4-z-WekZ6lHDHuTGziqg-uPu14Qy_FYF6zvUiAkEz5jQ8m1nTUwMwsywujGj-5rAryGNofs4ELtXKcGjKwcsQnYsbj8DOpi5CgCisF4B9fbuuMMlQSKijIPbRdoA0i3bGEVh7GLEaG2nBW7Va8wfxVcNhL4P8tJ6HtZsip87__5w6clTz4lvAlzzX5r-4AjBFfyWQsvs4E7sVMyheOaJtRN1YQHeRRymKDrHhumn3npMdlVWCde-x0qUe5U9ltz0r9TmCvvVRPgufvkGbF9t3o5d0XXO5R59mp8_YH_JAgjehxe2EuZFFUPke775fhiWQRe6tQvCLIAG8BwcGEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
👋
گئورگی گولسیانی مدافع سابق پرسپولیس ‌و سپاهان از فوتبال خداحافظی کرد. گولسیانی زننده گل قهرمانی پرسپولیس در لیگ بیست‌وسوم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106230" target="_blank">📅 19:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106229">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuUTXTUYDgSMymbGt2n71v5T_mqTF_ZGfO0Ku1MMIW9NCzPb7vyGOnnR9kmuEkMTu_sH3SjTaRvjjNiScllclPMQZvW8oSjwXRu_u8hu6LNbw2RxwW8lOLPypy8K5jtq_3F3_BKJ-c_l6yKOI-P8Zyn1eWkhYSLHPTYEF89rAIlwWwJ2n8jdfT1cR55E_E5r-oKK2pAJVUfGddlf91SxghV8x1iGaUZyAAMCiY9prOD35P3MDpfarpi85sguZkuO6-GgDH5x7dkzrKB-gCQLWCUOk0t4aCc3bD-GX0DxIiAPki_mT-M3Jg572Gq4ozLp3xIgapoHQDApLsVPA0XDyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🔥
🔥
🔥
اکتبر خونین که در پیش‌داریم!
🗓
🇪🇸
🇫🇷
20 اکتبر/بارسلونا - پاری‌سن‌ژرمن
🗓
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇩🇪
21اکتبر/آرسنال - بایرن‌مونیخ
🗓
🇪🇸
🇪🇸
25اکتبر/بارسلونا - رئال‌مادرید
🗓
🏆
26 اکتبر/اعلام رسمی برنده توپ‌طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106229" target="_blank">📅 18:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106228">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106228" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106228" target="_blank">📅 18:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106227">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etluqX3rtz-VByTurDxcfE_1FNHZBf0rgjE5sGClXSitj_64ZYriJW0S2w_K74T-fqjfOu9xs7uNMLTVTdFzUvMLw1yGH-mOPHxQGsTo0Jne0bDsv5XLBsf5NjG2hmd_5E8AecJ0Tkw__SCVyLVWGv_4q5y02-nwKYsBWuFFHwGMEYiGsy8ncTES_i1ntkfjq6WFUWIELziTVfbooYBN6Dw0nPrmS_nPW0q_lsRLxhBGqBd1DkSZtpoD4XJkqbP_weZh_l3C8OoEJ-Oyd5uXFHezXp-tAiMyafmKhTWid6TAOg8jDpXMfff-gUfzcbWTGj-b3Fqvm1rJuJN7eHmUlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106227" target="_blank">📅 18:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106226">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2_-bqN7Xwk7H9qeAJIzwMTFyHoxc-Zpp_sH_HnSHLhrkAAkTVljc_4p5HUeBw04LBStn1wN7UP5O2SU_zUEABxkKwJVtQFZdBjagWdDuvokbog0psNxvzCJwSLYdmOLx62IVnimKVuGGGM7wBM7zgFHFmOsNieCG1d4WNst92YUqt3GOb8-j7f_3QR6ukF1y7nFJGtVVe8bPBqADYln1UVcSSviS4_CNEzADv25spV92e7-1UG_ij42OT_P3I8QeeVrbnjmrpypJbT4w10BY5bKcediDL_hzQsVZ6wHenoIa_0cZoyOnXAO3MBCKHHTO62K6atIG4eSYigulM2J1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇺
تیم‌منتخب هفته‌اول لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106226" target="_blank">📅 18:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106225">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e1c6bb479.mp4?token=YNhtPmeRO7-j8VbFLGYEATOODf8CEh-9XYh3-5XBACaq0NgNojZRitB7OOvKSMmRyThRDy4f-vr2ATKKbrrAEnTGT6ORd2b4u_5HNmXWcIKKQ-8nho9MnmozUCjS1kTYUkxC09Opd9Pi3xTRXUsKXsRJzrCgRcsM2CNM9Lcz70i-NDBoiC0gjfBU0ogEsn4zdOJv35EMlymu8EUwobNuCj0bbqxOC10JOJSQTvdfUFNoQFUA0KIbymngruYmnzkAJD2yvEYPsS-Sj76hR_DzVMpM9RCyDa6DMyfoIlPp-EXB6IBEj8mBVM-p1dc_srLwdh3YuLQ24bd6aKHWKEKC0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e1c6bb479.mp4?token=YNhtPmeRO7-j8VbFLGYEATOODf8CEh-9XYh3-5XBACaq0NgNojZRitB7OOvKSMmRyThRDy4f-vr2ATKKbrrAEnTGT6ORd2b4u_5HNmXWcIKKQ-8nho9MnmozUCjS1kTYUkxC09Opd9Pi3xTRXUsKXsRJzrCgRcsM2CNM9Lcz70i-NDBoiC0gjfBU0ogEsn4zdOJv35EMlymu8EUwobNuCj0bbqxOC10JOJSQTvdfUFNoQFUA0KIbymngruYmnzkAJD2yvEYPsS-Sj76hR_DzVMpM9RCyDa6DMyfoIlPp-EXB6IBEj8mBVM-p1dc_srLwdh3YuLQ24bd6aKHWKEKC0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
پخش‌صدای بانو هایده در مراسم هفته‌مد در نیویورک آمریکا؛ روحش شاد اسطوره
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106225" target="_blank">📅 18:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106224">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8904bfcc25.mp4?token=SzHtPVpkEzf61ser45eRtq5gxktnwz_3NOcnTXor85jAzSvtqtcTc9U297z9rNv5wrODbzmkp8RuzodLqqSB1sMU--iV6Frtbpheu84zZsdZo4rD-wkds7k4vtCYionmFp-4KlxwVd2Qq_LwANU5amZQ6Zi4nWzY29US_upXSZEZ8d9mj2FBNLrUX8RTWKd9qc3vkt6vk-w9O-a42o9DJLJMLu230vYrletVaPf4lXH93MHSVSdPsOna_x56HYoVWubrmZ10CmLvNKpLvndVwDiPIf0mHoV270gTEeL0-C5zUd_qvwd5s0pnzyMn5DAEvJLWj3wyYkNy_vXUpiHxbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8904bfcc25.mp4?token=SzHtPVpkEzf61ser45eRtq5gxktnwz_3NOcnTXor85jAzSvtqtcTc9U297z9rNv5wrODbzmkp8RuzodLqqSB1sMU--iV6Frtbpheu84zZsdZo4rD-wkds7k4vtCYionmFp-4KlxwVd2Qq_LwANU5amZQ6Zi4nWzY29US_upXSZEZ8d9mj2FBNLrUX8RTWKd9qc3vkt6vk-w9O-a42o9DJLJMLu230vYrletVaPf4lXH93MHSVSdPsOna_x56HYoVWubrmZ10CmLvNKpLvndVwDiPIf0mHoV270gTEeL0-C5zUd_qvwd5s0pnzyMn5DAEvJLWj3wyYkNy_vXUpiHxbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇺
برخی از اتفاقات هفته‌اول لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106224" target="_blank">📅 17:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106223">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3be86e9eb1.mp4?token=lKzV40NMviHwNi6harihnD-s8iBt6Ud673FrE7ZsRM1nKTAmCymWvtgpDy-keM2wV8MzMpgfnBExbEqvYq3rhB4L_JcHAXjpbuy7hm1FuvLlEECSxvITuD1C1kBXTYX1oQrnbJcCmo52trS2x8k9Y2SqxcyYAYmvQDo7p7dS2YZBcyynlxDw4q_DubNQ1UQYjwI148hMdm5O3b850ggK7fVnd_c0PVXfU3PIpOE9OkLXMYOB-BKDFAkfeN7b-ewjMGrU5IlQFoQbgWYMTKili5bQnZt-Q-y1KOpyJ0qtpJREClXH6J5fecN-c4dl774m8pTpJ8NQhld-OsPHhJ65JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3be86e9eb1.mp4?token=lKzV40NMviHwNi6harihnD-s8iBt6Ud673FrE7ZsRM1nKTAmCymWvtgpDy-keM2wV8MzMpgfnBExbEqvYq3rhB4L_JcHAXjpbuy7hm1FuvLlEECSxvITuD1C1kBXTYX1oQrnbJcCmo52trS2x8k9Y2SqxcyYAYmvQDo7p7dS2YZBcyynlxDw4q_DubNQ1UQYjwI148hMdm5O3b850ggK7fVnd_c0PVXfU3PIpOE9OkLXMYOB-BKDFAkfeN7b-ewjMGrU5IlQFoQbgWYMTKili5bQnZt-Q-y1KOpyJ0qtpJREClXH6J5fecN-c4dl774m8pTpJ8NQhld-OsPHhJ65JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم تشیع جنازه بابای مسی با علی‌آقا دایی
😂
🚫
با صدای کم‌گوش بدید فقط
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106223" target="_blank">📅 17:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106222">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2Oxn6FplpIHOdblfQO82h_NPdn2VleQhNZG9X2kFHkA5BjMHzeDFvhQvzRD98T5SKIqH7TN0cIEuVZc9fEWmBguSkQHk2oCO-fw4FhTxdmknrldVqMn1WaGp2nW1XONhnS78UqYJRLGLPATCqGGTdOesnyJr2B179STFgqba-hA-4-9U3yMdx2aqfxOBnM3ykrXo2oxZdK1ZygsplB-fNf4tdAxRuRLB7WGcXTViqY7LbVWtE4PNT0EHEane_obIQw_bxa6KxARJAMky7Xwd0yZsgXKmBo9QA2cbKNnJjNKT6Zqb5o-KMw-EChmj4zzQbN7heCfJVA4zhrEBvrp6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
واکنش علی تاجرنیا به بخشیده شدن صالح‌حردانی توسط بختیاری‌زاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106222" target="_blank">📅 17:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106221">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d24125c19.mp4?token=eqTTkVuU2-CV1kOWW-gkFRaNrXSnx6alJr5VlNNGEzntiXopN1TOGAfcSAlXITiy02P9VpYYaIW6lqeLJmhD3ginND5KARlTtzwV4bfqB6K4tBwbwn46JfoAD9uE2oU_goyrHyca9J5yxCSGB7LJK3otiLwfedue9aBMmpG_eqVpfkpO-CYti7Zgxr_K23qRa7H3aYUi3Yom3HQ6TTNEFV6x3e-DOxiT4solFGl-5E4rnuosU0PzdkS0l8J_SQVtk8xtyOJqV_dDX1Ky-css_QpPjeQ3CsMmhUAaJooOMHVyrJ-F88l0ftHtGzasBm_cMcXKW-pBjBOMyZysazyatw8WmThx4caxFvH20OpsewUWxOfKdC1TozmXiYgfJ296lZwTaz8ekXjieJH0Uog-WweDBXgekeilzvYi1Y96biUCpufatx4ODFEvhqS477kXwp6_3ENxLK8qzNMiBYoKWD0Odk4gn1-ZhN2Vhn2pBMj39FzBSTcKGL3MC4NbS4G9G2PCmHZI3s0Si8rBbxRnW_F-punV1oaL1exmegN6Y7srH3HujBPH-RmF5PldZT0zADVxy0119Mlv4KG8qd74MJj4HODNfbEn260FWr11WLvyq3gqfUBfWjzrLZFu8X7bvdnNyB2ww_2uAts689n4CQc2_YaeoVBSDgXaklvz18I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d24125c19.mp4?token=eqTTkVuU2-CV1kOWW-gkFRaNrXSnx6alJr5VlNNGEzntiXopN1TOGAfcSAlXITiy02P9VpYYaIW6lqeLJmhD3ginND5KARlTtzwV4bfqB6K4tBwbwn46JfoAD9uE2oU_goyrHyca9J5yxCSGB7LJK3otiLwfedue9aBMmpG_eqVpfkpO-CYti7Zgxr_K23qRa7H3aYUi3Yom3HQ6TTNEFV6x3e-DOxiT4solFGl-5E4rnuosU0PzdkS0l8J_SQVtk8xtyOJqV_dDX1Ky-css_QpPjeQ3CsMmhUAaJooOMHVyrJ-F88l0ftHtGzasBm_cMcXKW-pBjBOMyZysazyatw8WmThx4caxFvH20OpsewUWxOfKdC1TozmXiYgfJ296lZwTaz8ekXjieJH0Uog-WweDBXgekeilzvYi1Y96biUCpufatx4ODFEvhqS477kXwp6_3ENxLK8qzNMiBYoKWD0Odk4gn1-ZhN2Vhn2pBMj39FzBSTcKGL3MC4NbS4G9G2PCmHZI3s0Si8rBbxRnW_F-punV1oaL1exmegN6Y7srH3HujBPH-RmF5PldZT0zADVxy0119Mlv4KG8qd74MJj4HODNfbEn260FWr11WLvyq3gqfUBfWjzrLZFu8X7bvdnNyB2ww_2uAts689n4CQc2_YaeoVBSDgXaklvz18I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
یک‌دقیقه با کورتوا بهترین گلر فعلی اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106221" target="_blank">📅 16:55 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
