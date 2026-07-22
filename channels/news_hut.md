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
<img src="https://cdn4.telesco.pe/file/L_VAiYb43UDuISIPCzrI39F4AVys2QzoZm7apbs3tVBm7C1w3qk4KlDmbgWgIsJpJof5Aljf1UaxjvloHUg_ew5xB44OFqkVYohS65317mPuyu1phmVb_510ke6iCVLBfdtQmuTKPIexfW4uERORtp7lXUPi1M29njeiqt7YWt_DR4DhLPui4hhAFRpCUlihEImOCZrr8leDR4udRBdkSZGGMOBxwRNRR7I1eKr_3_WvrMyvzt5mVRQDxJmE3meG9_RkLC-Y6KlVi2f_CW15Jm3tlVsKnA720RntwIi9CYB5JH5CYh8w38rj98NwXredkKBmaL_TPC6IdeTbr6BZ-g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 154K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 13:46:19</div>
<hr>

<div class="tg-post" id="msg-68795">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44a650cd04.mp4?token=OjPUPP9WJpYLzmhs8jZhrTf7hB2LMFWPY8ckJtqCgfMDdm99eObJ5zRwfEX_F0E7PBetDSKyfurJL3LPXZbGxS2LDfB4ZIv5UFzj965MSxhKVuBa-xCsrnm3QQvCkhr85eRcOgKT9RXis17-ai_99waVxxNz-rO7C6SeMV4KrBa3UiqzJhElTXAVwpcFKJKnANI6JWDkvFaBGjzfLvUqWJwAaPgIiKrP1G2V6p6jNhr-pheyYSGC0xTTBzzyG2MktvwMGbrp2kQX_e70AEFwgVeMAfoVwm1ZAq1CKoCbQ_MXWUBt65djZhDh0nTWvedbzGp-EmZZd2SPt6DJ7HbtJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44a650cd04.mp4?token=OjPUPP9WJpYLzmhs8jZhrTf7hB2LMFWPY8ckJtqCgfMDdm99eObJ5zRwfEX_F0E7PBetDSKyfurJL3LPXZbGxS2LDfB4ZIv5UFzj965MSxhKVuBa-xCsrnm3QQvCkhr85eRcOgKT9RXis17-ai_99waVxxNz-rO7C6SeMV4KrBa3UiqzJhElTXAVwpcFKJKnANI6JWDkvFaBGjzfLvUqWJwAaPgIiKrP1G2V6p6jNhr-pheyYSGC0xTTBzzyG2MktvwMGbrp2kQX_e70AEFwgVeMAfoVwm1ZAq1CKoCbQ_MXWUBt65djZhDh0nTWvedbzGp-EmZZd2SPt6DJ7HbtJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
مراد ویسی:
دیدم مردم به من گفتن عراقچی رو فالو کردی رفتم توییتر نگاه کنم ، دیدم نه تو توییتر ندارمش و رفتم تو اینستا دیدم اره عراقچی رو فالو دارم که احتمالا دستم خورده بود و انفالو کردم.
مرسی که بهم تذکر دادید.
@News_Hut</div>
<div class="tg-footer">👁️ 619 · <a href="https://t.me/news_hut/68795" target="_blank">📅 13:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68794">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
فارس:
دقایقی قبل صدای سه انفجار حوالی سیریک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/news_hut/68794" target="_blank">📅 13:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68789">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd690bdc0.mp4?token=kH8Rjewd4tqZeOPqUhEzYsIeOH67hnZl246a0WIMT72IQb3vMPqBv0yTM4FWly4x3vXZ1Qkb1ULUuJKzCRXFEq1dI26pFTbw3BiWg-CKz9lRTO8HZi1YoWqCLBtzCEYa0bwEJ5u_UP7nymHYuTtkvJQLstcGnDcKqYhj2-3mfGURyzic7K2ld1CWGcoen6r-bj4O55DEFDNDyNs4720PGy_AH7E6GV6uQoxNIOFsbn28NgkdpQCb1uI3oUMfMoTTZsb58fLauQ-4eWqD8VSfA8_DbNXDtEluJbalpOBUsoCj_BPGUPxr79wmATk_AyXmFw6vFxaShcoBH4jqUA5VVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd690bdc0.mp4?token=kH8Rjewd4tqZeOPqUhEzYsIeOH67hnZl246a0WIMT72IQb3vMPqBv0yTM4FWly4x3vXZ1Qkb1ULUuJKzCRXFEq1dI26pFTbw3BiWg-CKz9lRTO8HZi1YoWqCLBtzCEYa0bwEJ5u_UP7nymHYuTtkvJQLstcGnDcKqYhj2-3mfGURyzic7K2ld1CWGcoen6r-bj4O55DEFDNDyNs4720PGy_AH7E6GV6uQoxNIOFsbn28NgkdpQCb1uI3oUMfMoTTZsb58fLauQ-4eWqD8VSfA8_DbNXDtEluJbalpOBUsoCj_BPGUPxr79wmATk_AyXmFw6vFxaShcoBH4jqUA5VVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
🚀
حملات شدید پهبادی اوکراین به روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/news_hut/68789" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68788">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/348d732189.mp4?token=HO7eIVlIvYyysHnhb0fzHOLHe98X-H5ffnaVLIgTpWrUWqZdKRrvSnP1P4v6TfTp2YuPJargybb1hciFEHCVwyHv2wwtlbOX8N-c7NvZY2B8Vo3S3U6n0KpySGWAYvG8XgtPmM1YhJL5XEdVFoKQHGOf8T9yD-QOe5k9nYqbhDR_WAMzc4KJGvgRvMGoK1RiAUPfJMWd0yQzhlFJClzgA3vnPuYwpRJaQ-WVHDdfj6mKli5U1PFBQ5HFoxigkyG-kfyJK5BuSEcLRaY_DydBcIxF8aQMrjXbUYEUKW-jyQkEzpo4z2Fghf0Tcvrv3EdaPeABlytzkuEPHXgmrNDnHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/348d732189.mp4?token=HO7eIVlIvYyysHnhb0fzHOLHe98X-H5ffnaVLIgTpWrUWqZdKRrvSnP1P4v6TfTp2YuPJargybb1hciFEHCVwyHv2wwtlbOX8N-c7NvZY2B8Vo3S3U6n0KpySGWAYvG8XgtPmM1YhJL5XEdVFoKQHGOf8T9yD-QOe5k9nYqbhDR_WAMzc4KJGvgRvMGoK1RiAUPfJMWd0yQzhlFJClzgA3vnPuYwpRJaQ-WVHDdfj6mKli5U1PFBQ5HFoxigkyG-kfyJK5BuSEcLRaY_DydBcIxF8aQMrjXbUYEUKW-jyQkEzpo4z2Fghf0Tcvrv3EdaPeABlytzkuEPHXgmrNDnHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی وزارت کشور :
عباس چرت میگه مشهد سقوط کرده بود، تو دی ماه من خودم مشهد بودم خبری نبود اون شب.
@News_Hut</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/news_hut/68788" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68787">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
💵
پرداخت آسان و سریع با تمامی روش‌های پرداختی
📣
30% فریبت ورزشی برای واریزهای کریپتوباکس (ارز دیجیتال اتوماتیک)
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/news_hut/68787" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68786">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kA-RRtN9TwBOVJgKDXGyPG0jeDcz6XTBjKSeknden88zlzA66LtuAkcrdQH1TxGZC-rbdVAETqH9SjrseGXyaf4VV8MKZ1ej3tALsdu9jsPaY4LfOAV_i8KrqQMSOV5GUt9v4b-nInb1MNGPsA-LFDtbuA7pZTQfTgOf5vB_3nHBcFBD9xBLxQtTOiF3XvlTq01d6Jz3tWkdjd9QVxadUwJGTnjoWCPyKU0Ay39Nz0k-vweSQjr6H4C8u_mhIF309QiCh7ImzwPUikT9c0zxloWCHPCoWT9ZcSYOPHd404FN9D24eYFkiNQ4gKko1Uv_w21SHYQfZUWpzQGxIBYSFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBET
💎
🇪🇺
لیگ قهرمانان اروپا
⏰
شروع بازی ساعت 20:30
🎁
100% هدیه ورزشی ویژه اولین واریز
💰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/news_hut/68786" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68785">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/22ed6173e8.mp4?token=i0AV0-S0J-vSm65yGhoC4Wm4b0zdl1tfmBfeOa1JnyGSjE9T8noxAvHxF3OkrUZzDtx-vZOCB-cH6vpSru17Gd6ccKsKhFtF7UaP0yQljXg6V1X0PZfjb1ZvP3G_-lGQkPTzhTLOxRQLb8rl8ZF4CWuX55R6z6sXpgZBBkaCKqzVEbhb475yhBESoxysjdAm5Aja2YbbPZVcn0NJt_Rglkj3yq1YXhkjRSrzAPBkBNM8Ig-vckf7-8bNEC2UhV8CBLeLpCVseicM60WSsKkirnN1tOhDQZfekW_4iKDR6xOGe4Qy0lf4lRShkeWUeqHncDUEFc7WlcsucBs6QWuHNg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/22ed6173e8.mp4?token=i0AV0-S0J-vSm65yGhoC4Wm4b0zdl1tfmBfeOa1JnyGSjE9T8noxAvHxF3OkrUZzDtx-vZOCB-cH6vpSru17Gd6ccKsKhFtF7UaP0yQljXg6V1X0PZfjb1ZvP3G_-lGQkPTzhTLOxRQLb8rl8ZF4CWuX55R6z6sXpgZBBkaCKqzVEbhb475yhBESoxysjdAm5Aja2YbbPZVcn0NJt_Rglkj3yq1YXhkjRSrzAPBkBNM8Ig-vckf7-8bNEC2UhV8CBLeLpCVseicM60WSsKkirnN1tOhDQZfekW_4iKDR6xOGe4Qy0lf4lRShkeWUeqHncDUEFc7WlcsucBs6QWuHNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
این ویدیو از اینکه نشونه آدم پولدار چیه، اخیرا خیلی وایرال شده!
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/68785" target="_blank">📅 12:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68784">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxCw4tMQs0tT0yuoDn7xuMCG1w1uPoQbqre3ZN2-z0vrat87QBW6IQgK4DAi-W13WKv5zZ4O-IJ5Uy3V3U5e8W6l8m5GXzy3lCS__Io3mQFP2iql_wX2w6vlj8IsjZpvFyby_zazFsQ1q91AFg9zV0r2d3Si65nX49H2_5WY-ILuCvQLZBDN4AYUEnIf1JHoJwlBYReZz-5OSKsLMOoCuV3IvsJnUtSB-280DZMOl5CeXfGpEC2ucC6fTR-l8_HrQ0Hm7pSegCi6BCMi_m0Fm6Ojk0Ea5t4V55tSOdYsPZjJnjcZSDPFYPGo_0pNL4wbtcRdzZf8uT_MtmFd8vWPLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
شلیک موشک از کرمانشاه به سمت پایگاه های آمریکا در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/68784" target="_blank">📅 11:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68783">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d576bfeb8.mp4?token=YqyB11VYmahFrOK_qdEeX85KC-2tiAh7_Tiwj098J80Hb8dt3CrV9kWd5tAkcZvnn6MKfHg8wxKD18ZCb5WpROEnc6TW56lDUbUU2vR4IhkLZacZ7X1r0aPfP_f20XQ_DHWIDyhvGmUdrEHivXsckEeeuEEMpSVDV5hYOgm4A6uzIDaH6LGeAZOXdtHjFyI-K5tCItggSjYZzPPcZdLHPrrbpP0MlqVYjX0AuNV8nQuW_k4uC7s8Z4IgEntwCwoGu1Y9wjnef05XshkBPZ-FWuKchTmZJuWS0nslp1etltBqvt3l4CTW9Jlw7XZJITdjMhh1ac1jOf6Gfi3T-Tn2fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d576bfeb8.mp4?token=YqyB11VYmahFrOK_qdEeX85KC-2tiAh7_Tiwj098J80Hb8dt3CrV9kWd5tAkcZvnn6MKfHg8wxKD18ZCb5WpROEnc6TW56lDUbUU2vR4IhkLZacZ7X1r0aPfP_f20XQ_DHWIDyhvGmUdrEHivXsckEeeuEEMpSVDV5hYOgm4A6uzIDaH6LGeAZOXdtHjFyI-K5tCItggSjYZzPPcZdLHPrrbpP0MlqVYjX0AuNV8nQuW_k4uC7s8Z4IgEntwCwoGu1Y9wjnef05XshkBPZ-FWuKchTmZJuWS0nslp1etltBqvt3l4CTW9Jlw7XZJITdjMhh1ac1jOf6Gfi3T-Tn2fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
‌علی‌اکبر رائفی‌پور، ازحامیان جمهوری اسلامی:
با شناختی که از سپاه دارم اگر نظام سقوط کند، سپاه پاسداران موشک‌های خود را بر سر شهرهایی خالی خواهد کرد که به کنترل طرف مقابل درآمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/68783" target="_blank">📅 11:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68782">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c11f67944.mp4?token=Luq85FXg4cYS_D0eT-3upc-sgoeIeAonpIcd82nj-n9el8ITJfTB5lVAT1Yhlok92OTcvgqUOAUSApj2EZLAFK6YrGipbnJzefeMnpddIcCFLH09w6HMlvUk671bQ2b0vcYVeYRBInaKbkR1O700Wd7s1I30lNMpnEYumgHC8kNV0uTmylJSTeuNhzq7YFiYpbrW-H96RVwzODlFbQN6huYi6TIcLTuZNQ1g2-4rhKVfPTJbhwkLYGoOwaa6rsVBpip9e73E0TuAIJ7wPzhJ-buFIKBiUx7EqiIm8h5RaezqWjFM6lX73N5zRPTVZSYFpBmkrNWEP3fpVLkCIKDr5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c11f67944.mp4?token=Luq85FXg4cYS_D0eT-3upc-sgoeIeAonpIcd82nj-n9el8ITJfTB5lVAT1Yhlok92OTcvgqUOAUSApj2EZLAFK6YrGipbnJzefeMnpddIcCFLH09w6HMlvUk671bQ2b0vcYVeYRBInaKbkR1O700Wd7s1I30lNMpnEYumgHC8kNV0uTmylJSTeuNhzq7YFiYpbrW-H96RVwzODlFbQN6huYi6TIcLTuZNQ1g2-4rhKVfPTJbhwkLYGoOwaa6rsVBpip9e73E0TuAIJ7wPzhJ-buFIKBiUx7EqiIm8h5RaezqWjFM6lX73N5zRPTVZSYFpBmkrNWEP3fpVLkCIKDr5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
⭕️
گفته میشه دیشب با وجود اینکه پدافندا توی تهران خیلی فعال بودن اما انفجاری گزارش نشده.
احتمالا دیشب بیشتر پهپادهای شناسایی آمریکا، مثل MQ-1C Gray Eagle و... تو آسمون تهران بودن و پدافندا هم سعی می‌کردن اونا رو بزنن.
احتمالاً مأموریت اصلی این پهپادا دیشب شناسایی بعضی مکان‌ها، مراکز نظامی، محل استقرار پدافندا، و... بوده و ممکنه که آمریکا درحال آماده کردن خودش برای دور جدیدی از جنگ باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/68782" target="_blank">📅 10:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68781">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e535968cb3.mp4?token=bBEjoyVgl39rVCr6UX9m6MwD7IWPFCT2Z7kHEauEr02BWA0gP9JNI2MfSAPWlgq_fU7uE65wiKhqGX8LYjqx2sRV_pTSjeQ8MOG57091fw12qPhfSISmN2WLujOKaghdjwwnHrpFmIyN-YzB5L7HioSRxxXdjuIBzkI7ebJ_i8vaVakQkqEJIsqz3uoCz2jFf78fWmd-_ZgMr5JGAP9ut9MdxKQ663uP8sPwFi2fawhvooVVOh3bLekrR5EJoaByS5LVLCaCGwoQjiFJo2yQPm-_ULw5e0A-H3ve5Qgb48GhqD5IbAwvTuuGWBSwu7VXYyLbpdZcby3GOkwkROHBUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e535968cb3.mp4?token=bBEjoyVgl39rVCr6UX9m6MwD7IWPFCT2Z7kHEauEr02BWA0gP9JNI2MfSAPWlgq_fU7uE65wiKhqGX8LYjqx2sRV_pTSjeQ8MOG57091fw12qPhfSISmN2WLujOKaghdjwwnHrpFmIyN-YzB5L7HioSRxxXdjuIBzkI7ebJ_i8vaVakQkqEJIsqz3uoCz2jFf78fWmd-_ZgMr5JGAP9ut9MdxKQ663uP8sPwFi2fawhvooVVOh3bLekrR5EJoaByS5LVLCaCGwoQjiFJo2yQPm-_ULw5e0A-H3ve5Qgb48GhqD5IbAwvTuuGWBSwu7VXYyLbpdZcby3GOkwkROHBUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی دو روز قبل یه گونی آدم از مجری‌های صداوسیما ، اعضای پایداری و بعضی ورزشکارها در واکنش به کارزاری که راه افتاده بود، پا شدن رفتن جنوب که بگن ما از جنگ ترسی نداریم و این حرف‌ها؛
حالا کجا رفته باشن خوبه؟
بهمنشیر که تو نزدیکی کویته و 14 ساعت [1125 کیلومتر] با بندرعباس فاصله داره
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/68781" target="_blank">📅 10:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68780">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/822c8aa150.mp4?token=P50h4jODfNPQ_VIEnG00HPx8EP8rBH3hXxWj5pe1YbnbwHaTTkzfCWqrcyZ8ZDlhxJ21yImcovTijuRmEQELvQjt6EYplGq9YU1gW6brDjNuorsag0o3vkAddo1PitxsdhcDZZ3uAKswjFyAFAQ6SO4o6FA0Tjmk7Rpjz6NnMt7coJdsWhY_fSQEKTItt-T0nPJ1Nm_tuJ7AOiKWnhqOugOYnkayoCtsyz1pe2gZcqqlDvKGlUy-X0boM0hT3F-ciDgoXpiF9oeE-0D7j3nH7IXtm46gvtA8bhG94uBDW_Sd10EFiZC1wnRefvk1yXQC4moxgBipy17qS6BjhCci0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/822c8aa150.mp4?token=P50h4jODfNPQ_VIEnG00HPx8EP8rBH3hXxWj5pe1YbnbwHaTTkzfCWqrcyZ8ZDlhxJ21yImcovTijuRmEQELvQjt6EYplGq9YU1gW6brDjNuorsag0o3vkAddo1PitxsdhcDZZ3uAKswjFyAFAQ6SO4o6FA0Tjmk7Rpjz6NnMt7coJdsWhY_fSQEKTItt-T0nPJ1Nm_tuJ7AOiKWnhqOugOYnkayoCtsyz1pe2gZcqqlDvKGlUy-X0boM0hT3F-ciDgoXpiF9oeE-0D7j3nH7IXtm46gvtA8bhG94uBDW_Sd10EFiZC1wnRefvk1yXQC4moxgBipy17qS6BjhCci0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
لحظه‌ای که عادل فردوسی‌پور تو لایو فوتبال 360 بغض و گریه کرد...
اپلیکیشن‌ و سایت فوتبال 360 به علت اینکه عادل و مهمون‌هاش از تیم ملی انتقاد کرده بودن، به درخواست قلعه نویی و باندش فیلتر و از دسترس خارج شده و مجبور شدن برنامه رو تو لایو اینستاگرام و یوتیوب اجرا کنن!
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/68780" target="_blank">📅 10:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68779">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087e2855d3.mp4?token=Ep7gUnmikgfoFcSEQt59hm5ZJOP9SE9PUVDpOw6Ho0MUoI16Tn6-WB1YRQNOELGrhFhJt0p1434CjMODJ42T1CcAn1tXD9QP46XOXC2EonrRiKPRhpOANAhXc5CATtnScNineK2SthUgVWKGh6zLdDM6Dm2nxipAkUuS_0dw12rsSfH9hdSpGtIX7Fo_LbgjwCfBRUnOGZGWlShFCPpB9RRQAXvvlGL_ZK04Keja4LA63eoRzA_RUKHkl9Ye96QtUWViHL1SUgKTavLbZ5je6Gpj22J8cYeZe98aN8dHRlDnR9FHFrlVpa56gRl_lKCObNa85YXHLgLzUyfaXaWjxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087e2855d3.mp4?token=Ep7gUnmikgfoFcSEQt59hm5ZJOP9SE9PUVDpOw6Ho0MUoI16Tn6-WB1YRQNOELGrhFhJt0p1434CjMODJ42T1CcAn1tXD9QP46XOXC2EonrRiKPRhpOANAhXc5CATtnScNineK2SthUgVWKGh6zLdDM6Dm2nxipAkUuS_0dw12rsSfH9hdSpGtIX7Fo_LbgjwCfBRUnOGZGWlShFCPpB9RRQAXvvlGL_ZK04Keja4LA63eoRzA_RUKHkl9Ye96QtUWViHL1SUgKTavLbZ5je6Gpj22J8cYeZe98aN8dHRlDnR9FHFrlVpa56gRl_lKCObNa85YXHLgLzUyfaXaWjxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
نظر مارکو روبیو درباره برجام (سپتامبر 2015)
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/68779" target="_blank">📅 09:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68778">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
سنتکام: حملات امشب به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68778" target="_blank">📅 04:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68777">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68777" target="_blank">📅 03:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68775">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c46837f26.mp4?token=CRzvE_Sk52fj7U_6yTp1wlSmVjGqbTrNi2gffbveLzhSY2nCrTnn5_A3DcBxa7xiWSakAmXY-cSypmmuvfJf4jQqZe3IbKuVVnwgb0sXPkc1-UYiTplJss0itzc3eI176evCwsUgIt6Kpt4Py1DbVJx676g0Lx_6NgCU-ftKQUrydKSR-9cHaO1E7Dwxwd5bMvEiyLcetpiJpYCIDIOUvdfLl3-NU6RrnfR5DGxf9SvSqZkAtJwexeMbdPZgDav-Pk8wCysr6oztoZ0ZnK6VpQFzsrH0FxCl-1qm_HMghyyc8Ty6wcSr4Ifhtu9UsPgVeVAg_CMP_IOzVWQejgkJ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c46837f26.mp4?token=CRzvE_Sk52fj7U_6yTp1wlSmVjGqbTrNi2gffbveLzhSY2nCrTnn5_A3DcBxa7xiWSakAmXY-cSypmmuvfJf4jQqZe3IbKuVVnwgb0sXPkc1-UYiTplJss0itzc3eI176evCwsUgIt6Kpt4Py1DbVJx676g0Lx_6NgCU-ftKQUrydKSR-9cHaO1E7Dwxwd5bMvEiyLcetpiJpYCIDIOUvdfLl3-NU6RrnfR5DGxf9SvSqZkAtJwexeMbdPZgDav-Pk8wCysr6oztoZ0ZnK6VpQFzsrH0FxCl-1qm_HMghyyc8Ty6wcSr4Ifhtu9UsPgVeVAg_CMP_IOzVWQejgkJ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68775" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68774">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
❌
🌐
امشب ریزپرنده ها در تهران فعالیت داشتند، احتمال اختلالِ بیشتر در اینترنت وجود داره؛ پروکسی های پرسرعت زیر رو داشته باشید
https://t.me/proxy?server=nab.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68774" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68773">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در زنجان!
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68773" target="_blank">📅 03:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68772">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6Mil3TL9-pE2GufdC0RrUDNnIz1FNQdS4Ior7s0TmCBv3I9byN2KOerT42Mc-lFIEcL2P_I534wcZAZLOW0a1yfaiSspQFddnTSM7bDqwNEcO_vBMkrJhrjWmqYIWd3A6BE6_JtyDr9KHJ4U_ueKwT9FtONjOnNBGHJqRaKscJLkUNYPIImxz1tCAVXCH7Cf2100kTGsPrNUzFe0ssOU3rW-eYgg0erHe7bpM5EYFPOMb9Ho4gjlJKdXUlgQX_aIVcGjSBjgqEPPJHZnPkvSzdgjLJv_gJzoj6LlxJmnb5_HCddGw3N9BVwZlFUWo14k70XpE7pHqJMQUbo-vEM1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جالبه هنوزم سنتکام چیزی نگفته!!! #hjAly‌</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68772" target="_blank">📅 03:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68771">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
فعالیت پدافند شرق تهران
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68771" target="_blank">📅 03:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68770">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🇺🇸
هم‌اکنون حملات شدید آمریکا به</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68770" target="_blank">📅 03:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68769">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">جالبه هنوزم سنتکام چیزی نگفته!!! #hjAly‌</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68769" target="_blank">📅 02:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68768">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تا این لحظه سنتکام هیچ خبری مبنی بر آغاز حملات رو اعلام نکرده! #hjAly‌</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68768" target="_blank">📅 02:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68767">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بابت گزارش های لحظه‌ایتون عمیقاً سپاسگزارم، ولی حتما سعی کنید بعدش چنین گزارش هایی رو پاک کنید خدای‌نکرده جایی تو بازرسی گوشی توسط مزدوران ج.ا، مشکلی پیش نیاد
❤️
#hjAly‌
‌</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68767" target="_blank">📅 02:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68766">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
هشت انفجار در تبریز  @News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68766" target="_blank">📅 02:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68765">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68765" target="_blank">📅 02:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68764">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مثل اینکه تو غرب تبریز صدا های شدیدی اومده، مشخص نیست حمله‌ست یا شلیک موشک های سپاه #hjAly‌</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68764" target="_blank">📅 02:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68763">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مثل اینکه تو غرب تبریز صدا های شدیدی اومده، مشخص نیست حمله‌ست یا شلیک موشک های سپاه
#hjAly‌</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68763" target="_blank">📅 02:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68762">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس  @News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68762" target="_blank">📅 02:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68761">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68761" target="_blank">📅 02:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68760">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
انفجار در ماهشهر و بهبان  @News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68760" target="_blank">📅 02:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68759">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
انفجار در ماهشهر و بهبان
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68759" target="_blank">📅 02:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68758">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
صدای انفجار در نارمک!!
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68758" target="_blank">📅 02:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68757">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
💥
ارائه مهیج‌ ترین اسلات‌ های جهان
💲
شروعی هیجان‌انگیز با 100% هدیه خوش‌ آمدگویی ورزشی و کازینو تا سقف 100 میلیون ریال
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68757" target="_blank">📅 01:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68756">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbYGnF-q4bgMd3NeOV1unJoHkNrYOoILXELuF0epnUpxyPXu1LF8HH2Nk5NE10NuSR8nsHI8KIxyvcoAp3pGJeVI8B5Y-HjcbaNMP2-0h1Ftnib7zrI321134JfDfRPkClbI1SvKCMsw8zdvKhrVcepAH--jBRdM7HoiTgkQV1jsIrRkYpksdmATjco2-AvX3H-nlHVy-VH7oTCilsN3eXQC9xX7b6fVENoqGok6NnYJ77bSQzBfH48oN5jCyOuu6bFd2TuCYNz32RB9b8ewhRPlx1NfmF5BWUE8LKeppDmWat_5G1cmRiMlKD2doNq0Y8z0WtUAnYQNX6rUr_0fnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🍾
شب‌های بی‌پایان در یک بت!
🎁
35%
بانس جبران باخت ورزشی و کازینو، شبی پر از هیجان و فرصت‌های جدید
⏰
مختص واریزی‌های ساعت 00 تا 8
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68756" target="_blank">📅 01:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68755">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f9fa164a6.mp4?token=MVTTISVb6ukBd-tTg_LHXcXWjzd0FAJwRCzo6lhIK5DfwSw-grEL4SwJFbAYvj0TNYCXn9YBQlYvp_fNal8CR3mtP5QN5s4KwaSD6fz618co46vcNoZYp9xeVocsMBlng8BCixCMTr-ucrz8sL7-WU7PNiNehXGahAUTaMW8O_zk4gx7-UulqVhIH6ZFeftFyMHCaCVTKeLBSFvPPCrM9JcXq6-3wFR6ZGmE5ub9e8Rn5xqs3FADKNfpB8_bhZmdHbgEo55TzQKHTBgJiP994PkBQI6smFOQl4O-lmGzMJogJCVU6mxmafyYSc6a7jet7vtPbrffVyWA6IK2B8edFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f9fa164a6.mp4?token=MVTTISVb6ukBd-tTg_LHXcXWjzd0FAJwRCzo6lhIK5DfwSw-grEL4SwJFbAYvj0TNYCXn9YBQlYvp_fNal8CR3mtP5QN5s4KwaSD6fz618co46vcNoZYp9xeVocsMBlng8BCixCMTr-ucrz8sL7-WU7PNiNehXGahAUTaMW8O_zk4gx7-UulqVhIH6ZFeftFyMHCaCVTKeLBSFvPPCrM9JcXq6-3wFR6ZGmE5ub9e8Rn5xqs3FADKNfpB8_bhZmdHbgEo55TzQKHTBgJiP994PkBQI6smFOQl4O-lmGzMJogJCVU6mxmafyYSc6a7jet7vtPbrffVyWA6IK2B8edFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🚀
پهباد‌های انتحاری در آسمان کویت
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68755" target="_blank">📅 01:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68754">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
جمهوری اسلامی به کویت حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68754" target="_blank">📅 01:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68753">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7d96b014.mp4?token=k3G5Zge5OYkKF11NphkAzwjVLl5m1a-nwlEddum_vDP4JUZJ0FTkLDitGOs29gmPAbNBLtI4niwUKjO5s_JstV7nQtrt68h2HmP1qTKNchpxPpbOX1wQTNvVDIFVdqio9pbdDbJohjLHnogIgwem-oa5DcDrrVmYpngVjIi3FvKn_xXCgpk3rYn1GIfC-UJFgY2Sn8xvSyNU_xrnbEAAbeecVLhecccosBSty2GKA6gFUMd7cRlGLJaLjSHVukMXJH6mYKqVdxupeD8K4KNYDm-txv8-rHcTVyfQrnW7VLgt-j8T3Xo2remQIpNrDTXRvdV1eQhXT_mpYjPIFs85gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7d96b014.mp4?token=k3G5Zge5OYkKF11NphkAzwjVLl5m1a-nwlEddum_vDP4JUZJ0FTkLDitGOs29gmPAbNBLtI4niwUKjO5s_JstV7nQtrt68h2HmP1qTKNchpxPpbOX1wQTNvVDIFVdqio9pbdDbJohjLHnogIgwem-oa5DcDrrVmYpngVjIi3FvKn_xXCgpk3rYn1GIfC-UJFgY2Sn8xvSyNU_xrnbEAAbeecVLhecccosBSty2GKA6gFUMd7cRlGLJaLjSHVukMXJH6mYKqVdxupeD8K4KNYDm-txv8-rHcTVyfQrnW7VLgt-j8T3Xo2remQIpNrDTXRvdV1eQhXT_mpYjPIFs85gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هگست وزیر جنگ آمریکا:
«رئیس‌جمهور ترامپ گفت که ما دوباره درگیر جنگ‌های احمقانه‌ای مانند [عراق و افغانستان] نمی‌شویم، و او این کار را نکرده است.
به همین دلیل است که ما سعی نکرده‌ایم جامعه ایران را از نو بسازیم، بلکه صرفاً، به شیوه‌ای واقع‌گرایانه و با شعار «اول آمریکا»، اطمینان حاصل کنیم که آنها هرگز به بمب هسته‌ای راه پیدا نمی‌کنند - کاملاً متوقف می‌شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68753" target="_blank">📅 01:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68752">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8503f1809.mp4?token=lKhvFp-CqzYVpv1dMzv59CvUTEfsOhZR1kY-AEbsE-ifcbV1AWD01PGxTnlCYLNpqlfi9IQe7e4S9ZTXp7BZfuTjotkvPoFKwbjGYG2euPFPArViyH9CcWxjRNhdSvvLLSYLPTLJm5Rv-DWBa4T6FAkkTDJI41eINWyPxyl73P1YeE2Im9Q5AD0Zdhod4hkmoK8LalrdVVn0v9zxD7Hrsmwyy9v8dhyCQayR-oUCS-OSAhWjUAVqLPbbGfLLzA7E0UFQEOvRNlwYU_qRIWBUf3_rh0Y7L9dFTojAebzZ7071tB_xlVcqm6D5ZAQtHLbryuJifazyZDWFkTk0eEYOSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8503f1809.mp4?token=lKhvFp-CqzYVpv1dMzv59CvUTEfsOhZR1kY-AEbsE-ifcbV1AWD01PGxTnlCYLNpqlfi9IQe7e4S9ZTXp7BZfuTjotkvPoFKwbjGYG2euPFPArViyH9CcWxjRNhdSvvLLSYLPTLJm5Rv-DWBa4T6FAkkTDJI41eINWyPxyl73P1YeE2Im9Q5AD0Zdhod4hkmoK8LalrdVVn0v9zxD7Hrsmwyy9v8dhyCQayR-oUCS-OSAhWjUAVqLPbbGfLLzA7E0UFQEOvRNlwYU_qRIWBUf3_rh0Y7L9dFTojAebzZ7071tB_xlVcqm6D5ZAQtHLbryuJifazyZDWFkTk0eEYOSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاورمیانه هرشب
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68752" target="_blank">📅 00:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68751">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXysGOYIFMAyxxmzUNyVy4VWneo-FCljmLz-KyEwhwVoA-GVXHQytCZxtOw2omj504HrBj6iGcpQJzFAItpbnwiE9--0dZqd06O0kqYNCPDfwCobPcDiWN3PCFqjM-EawhOvEQ_JCbea8LybgYxgQFth8arOKhnCOWtOtHEdNyb8MJFMEtkfL-tvLX_po9iqx2RFZKyMgiq8LoAwK8_5Kw5uy6s-r0Ugf-KCV7w9s6oHhkUoqnnSz6-NSUOpVhMQJ8i9J1C0vNa7kz0gtjI16vTRBmATAi8dt6UPRrR4QZZxk3Hw_BC1AvSeLQ8tuJ-6a9tV73R8k50kbTQPbUoVdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قرارگاه مرکزی خاتم‌الانبیا:
آمریکای جنایتکار مراکز هسته‌ای و تأسیسات حساس ایران رو تهدید کرده که ممکنه بهشون حمله کنه.
اعلام می‌کنیم اگه ارتش متجاوز و تروریست آمریکا چنین اقدامی انجام بده، این کار رو به‌عنوان گسترش جنگ در منطقه تلقی می‌کنیم و همه منافع آمریکا، همچنین منافع متحدها و حامیان این کشور یاغی و شرور، هدف حملات قدرتمند نیروهای مسلح جمهوری اسلامی ایران قرار می‌گیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68751" target="_blank">📅 00:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68750">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e35b34fa8d.mp4?token=rjIhX4yLU50Dt3on5LC0w9xdCd4148FY-9q7RCb-l_-4rG5vopqnjM9wv-geLM7iDqPNvZ17lNn3EcYHbMKksmOnfA0VFRIFKXQ0eZUsrLXt_CIczh_Ez4n15OLgXqWoflRbMANAvV1o8iIj8iFZf0qX8wOyTaQ_2YzNoVMNNVfv5tYDvmiRUviKl1Y60Lwj8x7xqh9kOHUjHQq0fXbPeK-my39ZXWZB-KIe8LEP0tILiFg9ki54KFwdK0HYKCN1iiIlnuUuz16CRPyPgruH-d8pVQSJghAkiv83AdIDAJFar-1ZUPomgjgXwfZWcDq-WydGDJgZEbfi9wYxFhGl0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e35b34fa8d.mp4?token=rjIhX4yLU50Dt3on5LC0w9xdCd4148FY-9q7RCb-l_-4rG5vopqnjM9wv-geLM7iDqPNvZ17lNn3EcYHbMKksmOnfA0VFRIFKXQ0eZUsrLXt_CIczh_Ez4n15OLgXqWoflRbMANAvV1o8iIj8iFZf0qX8wOyTaQ_2YzNoVMNNVfv5tYDvmiRUviKl1Y60Lwj8x7xqh9kOHUjHQq0fXbPeK-my39ZXWZB-KIe8LEP0tILiFg9ki54KFwdK0HYKCN1iiIlnuUuz16CRPyPgruH-d8pVQSJghAkiv83AdIDAJFar-1ZUPomgjgXwfZWcDq-WydGDJgZEbfi9wYxFhGl0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🎙
سناتور:
آیا ما توانایی نابود کردن هر آنچه را که در زیر «کوه پیک‌اکس» (Pickaxe Mountain) ایران قرار دارد، داریم؟
⏺
🇺🇸
هگست:
بسیاری از توانمندی‌های ما طبقه‌بندی‌شده (محرمانه) هستند، سناتور. اما اگر کسی در جهان بتواند به هر نقطه‌ای از این کره خاکی دسترسی پیدا کند، آن ارتش ایالات متحده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68750" target="_blank">📅 00:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68749">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2ac98ac4.mp4?token=Cs0zZkoOXSU1cpjqXvF4QK7SsD0y7091ZNVNHp-3S96wXQ7mLFY8JPupbg7Zfxn_4VcooEZSOhNTup3GKwGvBN_svo3dIhwVMcmeTatFte8MyNXLmEuNyN8mtdqmRhiERxyKb8ieLd6kIM5MmKinJRtCd6CecEkXFLcE4eBxQ0nwFLOansdynvdENFaArikVcHZCfYWi5SSWQU9zc-0OmUY2XX5j7szq9VDbxWhv6MFAkmQrr4gQTnePE05TDd6-UNNsRBxrQ38FO_GheuwKjK65nyMxpWiXMzRlXvpsBdUDziPPrNTjkaSwg9qJih2Ul2BlJYqZ9jXEqQUHy9qlkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2ac98ac4.mp4?token=Cs0zZkoOXSU1cpjqXvF4QK7SsD0y7091ZNVNHp-3S96wXQ7mLFY8JPupbg7Zfxn_4VcooEZSOhNTup3GKwGvBN_svo3dIhwVMcmeTatFte8MyNXLmEuNyN8mtdqmRhiERxyKb8ieLd6kIM5MmKinJRtCd6CecEkXFLcE4eBxQ0nwFLOansdynvdENFaArikVcHZCfYWi5SSWQU9zc-0OmUY2XX5j7szq9VDbxWhv6MFAkmQrr4gQTnePE05TDd6-UNNsRBxrQ38FO_GheuwKjK65nyMxpWiXMzRlXvpsBdUDziPPrNTjkaSwg9qJih2Ul2BlJYqZ9jXEqQUHy9qlkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هگست:
محاصره ما دوباره اعمال شده و عملاً غیرقابل‌نفوذ است...
بسیاری از حملاتی که دریاسالار کوپر و سنتکام (CENTCOM) انجام می‌دهند، توانایی ایران برای رصد و پایش در تنگه هرمز را از بین می‌برد.
سناتور جان هوون: « هدف از این بودجه‌گذاری همین است... اطمینان از اینکه ما و متحدانمان می‌توانیم در تنگه هرمز عملیات انجام دهیم... و اینکه ایران را وادار کنیم تا در راستای اهداف ما عمل کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68749" target="_blank">📅 00:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68748">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f962f6335.mp4?token=ZAcqjQ5fo7FxegJbLAN5HPFeXlP5TEdWGYb_YLGqQ8bhxUy8AHeI21R8WtNo51E6f-sm6Tg6l-_PLp2P7EanOcnlzywsUA6-duytj_1M1JBrrAq1sXKkJE64QIdnlShTrKJiDaQwC-plMPwNrBosmlH5KuH6NiLvEkINkNIOZvtMHABjX5PUj4_JIOFHQO09VXQE86495__u4Furirjpzwxyln9gwlg5Auu17Q5-8_NzCawDKiT4aIF2rspKKn1MEAyAFzhluvazO7HpkqA7C6D9tHvWsUSK4w6eIHhKMnEKoTszxp_QiNmoz4f87SwXWRwGSvACEw2VxS9P7AmjpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f962f6335.mp4?token=ZAcqjQ5fo7FxegJbLAN5HPFeXlP5TEdWGYb_YLGqQ8bhxUy8AHeI21R8WtNo51E6f-sm6Tg6l-_PLp2P7EanOcnlzywsUA6-duytj_1M1JBrrAq1sXKkJE64QIdnlShTrKJiDaQwC-plMPwNrBosmlH5KuH6NiLvEkINkNIOZvtMHABjX5PUj4_JIOFHQO09VXQE86495__u4Furirjpzwxyln9gwlg5Auu17Q5-8_NzCawDKiT4aIF2rspKKn1MEAyAFzhluvazO7HpkqA7C6D9tHvWsUSK4w6eIHhKMnEKoTszxp_QiNmoz4f87SwXWRwGSvACEw2VxS9P7AmjpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست:
من در مقابل یک کمیته نشسته‌ام که می‌خواهد درباره پیروزی در جنگی صحبت کند که چهار سال است ادامه دارد، و درباره شکست استراتژیک درگیری‌ای صحبت می‌کند که چهار ماه است ادامه دارد، تا از دستیابی ایران به بمب هسته‌ای جلوگیری شود.
امیدوارم که در این شهر، دیدگاهی وجود داشته باشد نسبت به اهمیت تاریخی اقداماتی که رئیس‌جمهور ترامپ در حال انجام آن‌ها است.
آیا شما می‌خواهید که گروه‌های افراطی اسلامی به بمب هسته‌ای دست پیدا کنند...؟"
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68748" target="_blank">📅 00:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68747">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/912fcd0888.mp4?token=iZEmxzq00LYw7jYKDO9z6EijCLbwUePJRS4F8lW3vw01P9UAhe7sAlhtevzd2xJdnLyshEtWxG4J0g80cXVT_QRUC2fPcdQ4KkUBa5ZyCfopCBy4zQO6eS-dhfIvzvGaCTfC33xD9GK1IVL28PTGzLtl6fCrTLAQHT5lCcl4g_XZVfVcLs5R4FbupYIGWWzYzTnOTzRGhZ_QMTW_ITjNt-vzGyrzitFEMN1dDpd5Iq2UhfR5-PL3sh6RgzYZL64lLzVSs09b5F68SlHsfFjVqF2Fsciyde48nzoytYczhgMdGxf8GmmnzPXhdoSQsnipiUj7cVbA7Fy8ykdcZqCBgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/912fcd0888.mp4?token=iZEmxzq00LYw7jYKDO9z6EijCLbwUePJRS4F8lW3vw01P9UAhe7sAlhtevzd2xJdnLyshEtWxG4J0g80cXVT_QRUC2fPcdQ4KkUBa5ZyCfopCBy4zQO6eS-dhfIvzvGaCTfC33xD9GK1IVL28PTGzLtl6fCrTLAQHT5lCcl4g_XZVfVcLs5R4FbupYIGWWzYzTnOTzRGhZ_QMTW_ITjNt-vzGyrzitFEMN1dDpd5Iq2UhfR5-PL3sh6RgzYZL64lLzVSs09b5F68SlHsfFjVqF2Fsciyde48nzoytYczhgMdGxf8GmmnzPXhdoSQsnipiUj7cVbA7Fy8ykdcZqCBgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست درباره ایران:
ایران از نظر نظامی در ضعیف‌ترین وضعیت تاریخ خود قرار دارد...
بی‌شک اذعان می‌کنم که آن‌ها همچنان از توانمندی‌هایی برخوردارند، اما حجم خساراتی که ما طی این رشته عملیات به آن‌ها وارد کرده‌ایم، آن‌ها را در بدترین موقعیت تاریخشان قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68747" target="_blank">📅 00:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68746">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f9adfe1f.mp4?token=SughTg2qq-_iqr9VuxaOrRRCBXukDP-8nGNsTJgpHEJPrYiFQybXVsRe25WJPaCVKvKok7at5pjPCk3B4u1wWHEgg4NCzOmsxhLwR8R4WyzW0J9Ce2yydqvV2vlR5tRFyJcUS7wUWyfsrOL7KgO6E2IVyKqDMYPEEydFpXmIdSmO9rOv8UktlytJQQdkpxrPSHgSh0xAIydyuod-Q14dS5GYrtb64oq-axlZf6qa_bx446_chaIBKvL_Pi37SMD4fQZa9AJEz3C0eMOIFxViXlXaTmaArVCZoAJA_TZH88SOENvGwAq1A6ZZY_2vBj6-EDwRLdZsA882Kf9mVsMm0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f9adfe1f.mp4?token=SughTg2qq-_iqr9VuxaOrRRCBXukDP-8nGNsTJgpHEJPrYiFQybXVsRe25WJPaCVKvKok7at5pjPCk3B4u1wWHEgg4NCzOmsxhLwR8R4WyzW0J9Ce2yydqvV2vlR5tRFyJcUS7wUWyfsrOL7KgO6E2IVyKqDMYPEEydFpXmIdSmO9rOv8UktlytJQQdkpxrPSHgSh0xAIydyuod-Q14dS5GYrtb64oq-axlZf6qa_bx446_chaIBKvL_Pi37SMD4fQZa9AJEz3C0eMOIFxViXlXaTmaArVCZoAJA_TZH88SOENvGwAq1A6ZZY_2vBj6-EDwRLdZsA882Kf9mVsMm0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت
هگست:
این درخواست تکمیلی دو هدف را دنبال می‌کند: حفظ آمادگی نظامی ما برای پاسخگویی به نیازهای جدید امسال؛ و تسریع قابلیت‌های حیاتی برای جایگزینی و تقویت قابلیت‌هایی که در شرایط اضطراری استفاده کرده‌ایم...
در حوزه آمادگی، ما ۲۱ میلیارد دلار درخواست کردیم. این مبلغ برای تأمین حقوق نظامیان، جایگزینی تجهیزات مورد استفاده در عملیات‌های اخیر، حفظ نیروهای مستقر در خط مقدم و افزایش قدرت نهایی پرسنل در عین تثبیت کمبود سوخت حیاتی ماموریت و پشتیبانی از گارد ملی هزینه خواهد شد.
در حوزه قابلیت‌ها، ما ۴۶ میلیارد دلار درخواست کردیم. این بودجه خطوط تولید را گسترش داده و تحویل مهمات مورد نیاز را تسریع می‌کند. ما در مورد موتورهای موشک سوخت جامد، JADM، موشک‌های مافوق صوت و قابلیت‌های ضد پهپاد صحبت می‌کنیم. علاوه بر این، ما از این سرمایه‌گذاری برای تضمین تسلط دیجیتال و فضایی، از جمله شبکه‌های ماهواره‌ای انعطاف‌پذیر، استفاده خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68746" target="_blank">📅 00:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68745">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1b34a86e2.mp4?token=IS4Dhc8YSpcidRTRdJ37-fhNcrYOMNxqXJIAECrF6MaIc3PQU-wjUQBz33A9fqkNmIO2WWCPQoegiiIlAI9Yd95tPMQCfOSPf0RIK39THkwusxQ8E7BzZn5zUByYbkRMFgc4QPjSt0NnRdkvQBF8--MbLyph6KijLQiBzNu6WqtPjsABZptQCqbVs33XXClTs1I1vL6wtBge5qt-DdrnMnzzjf0xSuKzbkWpEPmv81wKBCNz2CTAmCd-F6lSyHeH9xomBuHIVFvbhRivMXIOQyzuoxBN6PfPA8d3457rdgWy729hP5ZJuCP7nVEQZb9L2j21X3_IMc48nIblBVFCxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1b34a86e2.mp4?token=IS4Dhc8YSpcidRTRdJ37-fhNcrYOMNxqXJIAECrF6MaIc3PQU-wjUQBz33A9fqkNmIO2WWCPQoegiiIlAI9Yd95tPMQCfOSPf0RIK39THkwusxQ8E7BzZn5zUByYbkRMFgc4QPjSt0NnRdkvQBF8--MbLyph6KijLQiBzNu6WqtPjsABZptQCqbVs33XXClTs1I1vL6wtBge5qt-DdrnMnzzjf0xSuKzbkWpEPmv81wKBCNz2CTAmCd-F6lSyHeH9xomBuHIVFvbhRivMXIOQyzuoxBN6PfPA8d3457rdgWy729hP5ZJuCP7nVEQZb9L2j21X3_IMc48nIblBVFCxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست وزیر جنگ آمریکا:
«رئیس جمهور ترامپ از یک منطق ساده پیروی می‌کند - ارتش برای تحقق صلح از طریق قدرت به یک سرمایه‌گذاری نسلی نیاز دارد.
ما می‌دانیم که بهترین راه برای ایجاد صلح، آماده شدن برای جنگ است - برای جلوگیری از آن و این دقیقاً همان کاری است که وزارت جنگ انجام می‌دهد - ایجاد نیرویی چنان توانمند که به چالش کشیدن آن برای هر کسی پوچ و بی‌معنی باشد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68745" target="_blank">📅 00:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68744">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAE8dcUSDGHw_cMbv9ZoQgyTG6YEQiBo7tUfbm5D4upUe1vY9jSHael9JIk3mLS5jt-NQfCCXjGryd2Bu2RtGG-A33uIAVva9pcbo0Uqc0jinHEune1Luo5vS-Zx0YNqn0uTAqtzinrysdBZAQ7ZRFuIZxiXuMZX24OgyXl81OllJEhLTlveq2NgkjsEBBurvNRJrteY5B-Zrh3o7dY3TvTeD5nvIsXbFRapeB62wO5r_9ACq0928x1tmoNgTdf5dNGO2hHIa82DkvZ6_jXSISvL3xSUqgDBdvpyY1J0JK4X0pK3tolucAY4tYbFRBn2D09DTdr-dVH_576cQmLIiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
چند سوخت‌رسان از فرودگاه بن‌گوریون اسرائیل بلند شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68744" target="_blank">📅 23:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68743">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تاسیسات جدید هسته‌ای ج.ا: ۲۰۰ متر زیر کوه کلنگ
پرنفوذ ترین بمب غیرهسته‌ای آمریکا: GBU-57 با ۶۰ متر نفوذ
#hjAly‌</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68743" target="_blank">📅 23:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68742">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVePTy3Xslh0_4Sf4FU-MvGfTqWhMHkArPh-vvYhobQR8hYOhMy25W4IZlLiLn7RGIo-CGVPSH6hfmGO0jw9OQ-bf1fE4YrotLRsVOur_cK09-vGeUZh2mtTjAUvDN-FZP6PnwscbT8wTrg7w2zT56L4dOJrHx-hZqFdGC96J4SeuObymJOiO9oT6peU6EDDRbaTONrMisDpodvSbU7gqk8hn7yzATUR1dwyJ0mUQxyuB9yu9TLuBTcZbV3VUJqJ3UnbN6HwxVJKyqoyY-9t08xwsog9FrHfGQMtz8UecQpvcAW7miZ3-vJejxCXm5zj6Pw52smdtNW1FDift3qYmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ در تروث سوشال:
جنگ افغانستان: ۲۰ سال، ۲ هزار کشته.
جنگ عراق: ۹ سال، ۴۶۰۰ کشته.
جنگ ویتنام: ۱۹ سال و ۵ ماه، ۵۸۲۲۰ کشته.
جنگ کره: ۳ سال و ۱ ماه، ۳۶۵۷۴ کشته.
درگیری‌ها در ونزوئلا: ۱ روز، ۰ کشته.
درگیری‌های نظامی با ایران: ۴ ماه، ۱۸ کشته.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68742" target="_blank">📅 23:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68741">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab2e49c2e.mp4?token=Sj94_05FAZMoRAOV4NlugonSR8cTsEg9vA7LTtXR1TWWy3d3k3PY-vyWAkxabYFuTULN6BfNqbRl9qzmxrBxGsxM5v2SoDw9felv_lE9fzS09tvMYxVfXfTCuZW19i4jl-fo7UtaqGzZfmbtOgIByThGRJRA5ayKZCh03Fo_Pt17UqF8mHmCnbNuOgmK-NHgNEBUChLQG7SzlsC8yGgUeyrwWffhdMkkB3MPbG5tPKzDN5EjR2y4UhdTLMJjgq1hyn8z1OrCWUl5Ko3Q_EjQ_PZsfZcRo5rO1l6jN6vkdXJ7ByriW8_iPNOmbib_T0fpjSSSnhgJQWT1kXXnI9DiSnWSj0fvIbdo_im7H-nMPGMMDPFYlNxO65mI4-l0lQRnPyqc7qbT8SMOLzj__iS0z7XaFYZ5p5H2xz5XyOzjryrTXGgcqeCHMygjtHb5rOE_P6wBZJjZN8TdBKVuUrgT5qCG_SqxkwNBt6EJnnI-gJNAYVRu-h9TJY9taAiz8bCxlx8SRlqBx2cOFwu-VOcLaphmQbDS2fg0uFaJBMHXdRZZocwztJ9_zcfUW-Uwp2i91fRMfUdk1pp1tJLCEXtq5wCLu9tTuVBaWgUeeynQU_E2NCFmTQvbNPKpYfbYgsf32vnUTJJsJtU0bGvF4IGy76k0GYJa1VLNZCjXddpudMk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab2e49c2e.mp4?token=Sj94_05FAZMoRAOV4NlugonSR8cTsEg9vA7LTtXR1TWWy3d3k3PY-vyWAkxabYFuTULN6BfNqbRl9qzmxrBxGsxM5v2SoDw9felv_lE9fzS09tvMYxVfXfTCuZW19i4jl-fo7UtaqGzZfmbtOgIByThGRJRA5ayKZCh03Fo_Pt17UqF8mHmCnbNuOgmK-NHgNEBUChLQG7SzlsC8yGgUeyrwWffhdMkkB3MPbG5tPKzDN5EjR2y4UhdTLMJjgq1hyn8z1OrCWUl5Ko3Q_EjQ_PZsfZcRo5rO1l6jN6vkdXJ7ByriW8_iPNOmbib_T0fpjSSSnhgJQWT1kXXnI9DiSnWSj0fvIbdo_im7H-nMPGMMDPFYlNxO65mI4-l0lQRnPyqc7qbT8SMOLzj__iS0z7XaFYZ5p5H2xz5XyOzjryrTXGgcqeCHMygjtHb5rOE_P6wBZJjZN8TdBKVuUrgT5qCG_SqxkwNBt6EJnnI-gJNAYVRu-h9TJY9taAiz8bCxlx8SRlqBx2cOFwu-VOcLaphmQbDS2fg0uFaJBMHXdRZZocwztJ9_zcfUW-Uwp2i91fRMfUdk1pp1tJLCEXtq5wCLu9tTuVBaWgUeeynQU_E2NCFmTQvbNPKpYfbYgsf32vnUTJJsJtU0bGvF4IGy76k0GYJa1VLNZCjXddpudMk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام:
هرگونه موفقیت عملیاتی در خاورمیانه، از جمله در زمینه محاصره ایران توسط ایالات متحده، با عملکرد نیروهای نظامی متمرکز بر مأموریت‌هایشان آغاز و تکمیل می‌شود. تا تاریخ ۲۱ ژوئیه، نیروهای آمریکایی برای اجرای کامل این محاصره، مسیر ۸ کشتی تجاری را تغییر داده و یک کشتی را از کار انداخته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68741" target="_blank">📅 23:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68740">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d66a861bfb.mp4?token=ZDOMDmSrfK07GAqGUVQwXrZPU-SivPQEmY_1C8LV_MHa0IUdpOB5acWQVr8EG_MqlJN661W-xOJ7v2WcbXzSg_CSE1-W2LPPQAkMS68GJhl3UBVt97jZsncNf5DRLCLlD7eSdDt5dkKqu3R7hbPy8CTvfNy_dF9y9zfw9yKmucdUL8OvV9GKwCjg_Fe2nBdIMGcwrtfufh_0of_YQ_ECFhNaZ6C1FKty1eo3nQbq0KxxBgx7HoIALB1uMdVn5uRaA5cmwBCD-3VprOa06sauAc8gy2NkqrZSLMG2H2FJhJiAmulNrfrE2-Oubimq5L5ZmhD4yh5d3PZ2w7o1yyaPfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d66a861bfb.mp4?token=ZDOMDmSrfK07GAqGUVQwXrZPU-SivPQEmY_1C8LV_MHa0IUdpOB5acWQVr8EG_MqlJN661W-xOJ7v2WcbXzSg_CSE1-W2LPPQAkMS68GJhl3UBVt97jZsncNf5DRLCLlD7eSdDt5dkKqu3R7hbPy8CTvfNy_dF9y9zfw9yKmucdUL8OvV9GKwCjg_Fe2nBdIMGcwrtfufh_0of_YQ_ECFhNaZ6C1FKty1eo3nQbq0KxxBgx7HoIALB1uMdVn5uRaA5cmwBCD-3VprOa06sauAc8gy2NkqrZSLMG2H2FJhJiAmulNrfrE2-Oubimq5L5ZmhD4yh5d3PZ2w7o1yyaPfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
جوزف، رئیس جمهور لبنان:
شما رئیس جمهور بزرگی هستید.
🇺🇸
ترامپ:
ببینید این خیلی خوب بلده خایمالی کنه، الان منم هر چی بخواد بهش میدم!
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68740" target="_blank">📅 23:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68739">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🇮🇱
کانال 14 اسرائیل:
سپاه سفارت اسرائیل رو تو بحرین زده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68739" target="_blank">📅 22:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68738">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d3140239a.mp4?token=LGvOOIJ0c8wNHupuDqKwk1s9ia3T_C61kMBm2Xc3_FOHcL9Pbd9UufMYfrZeqz4xIOJlaoMB8agqRvUoJAnjPsePakUo7H4nPsgqVpQ4Ow6HRQjxbh_reeio60vv8ngS8lOsdXP7wAHEzP45nszjxYis-K_ARQnA6UBIx79DZPHKnh3BDcPhZDp9r9U-zLhNzkK2BaehzHOad3Ifx2qI1LkB-POtwVJg5X6st1dPsmpv2RyCfSZOUNF2UGyE5ySic6n_UybJVz06v749_3WLjp2WbSwZEYRM7XrAwdpWudk7TGHY0rESY-Jdw2a9rvUB0HiObwddkS4mtIJ7-ZR0hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d3140239a.mp4?token=LGvOOIJ0c8wNHupuDqKwk1s9ia3T_C61kMBm2Xc3_FOHcL9Pbd9UufMYfrZeqz4xIOJlaoMB8agqRvUoJAnjPsePakUo7H4nPsgqVpQ4Ow6HRQjxbh_reeio60vv8ngS8lOsdXP7wAHEzP45nszjxYis-K_ARQnA6UBIx79DZPHKnh3BDcPhZDp9r9U-zLhNzkK2BaehzHOad3Ifx2qI1LkB-POtwVJg5X6st1dPsmpv2RyCfSZOUNF2UGyE5ySic6n_UybJVz06v749_3WLjp2WbSwZEYRM7XrAwdpWudk7TGHY0rESY-Jdw2a9rvUB0HiObwddkS4mtIJ7-ZR0hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
انهدام پهپاد جمهوری اسلامی توسط سامانه آمریکایی برفراز اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68738" target="_blank">📅 22:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68737">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cacafc700.mp4?token=t0ktm0m6fvtd-5PmRwiJnJUSZftoKqipLFQcU3pEj6TCxVa6YCOHvG6ZOro7ZRlT6gIB19V6NocNPdeHfbKog3UshOCaS9RSas_0WQN8EtyBxOJmBV0sTYK1X5f7ZPcrKnQQoEiIUlKJH9LR0Z1BWaNxStXKjlMd81g93TB8KSgdbFMo9Tp_aCI8t5eA1oipHVCeZY5sa4YC-WGsyRudDYE7PV0zZXWSWXkM886uH-elatHFSkER5BsoH3nzlr93oyykg799viygqlFbFA8AdsREcV8eBAz6oRsGCRJ4Sq18bEg5AIFHS-Xr6axMLb8rGjBJvdTeTu8APEAebMIsUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cacafc700.mp4?token=t0ktm0m6fvtd-5PmRwiJnJUSZftoKqipLFQcU3pEj6TCxVa6YCOHvG6ZOro7ZRlT6gIB19V6NocNPdeHfbKog3UshOCaS9RSas_0WQN8EtyBxOJmBV0sTYK1X5f7ZPcrKnQQoEiIUlKJH9LR0Z1BWaNxStXKjlMd81g93TB8KSgdbFMo9Tp_aCI8t5eA1oipHVCeZY5sa4YC-WGsyRudDYE7PV0zZXWSWXkM886uH-elatHFSkER5BsoH3nzlr93oyykg799viygqlFbFA8AdsREcV8eBAz6oRsGCRJ4Sq18bEg5AIFHS-Xr6axMLb8rGjBJvdTeTu8APEAebMIsUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دانش آموزی که ۱۹/۷۵ گرفته دانش آموزی که ۰/۷۵ گرفته
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68737" target="_blank">📅 22:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68736">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MymRzv7WHEaCRqEYhtQXCKstsicAv40bJZM-0rXLlY3x-cjhgET4WKTs4gUIAChRzr7bO1MnO9cGhgLJRLcMDbfFXpwX4WE-AJAKgLrU-xh8eFw6Xn_EoI5Z-hYufnnfGaUW1tAOBdabb7eAqyu8xWY8NS3S4rxVQB_oASl90Gf-lNVhviptF-2vLnPbkhcreYuN8Djq3keiZzrIm-9VPRkquM0N4gxuBIgH5-VFsHP284cmTNsc6CidvsxeId0R70JQjHweZRldFy2NRjrS-HqK7ZoOv69hDxWKgs6WFiP5bLFfdcRwVXzotydlUJ0rFwFmXi3L_66LKMxSD6oPvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به گفته بعضی از کاربران شیرازی، این اولین بار نیست که چنین اتفاقی می‌افته. ظاهراً چند بار هم دیده شده یه نفر میاد اینجا آتیش روشن می‌کنه و بعد میره؛ اما هنوز معلوم نیست هدفش از این کار چیه...
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68736" target="_blank">📅 21:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68734">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QnSRi9pPPIkagvreezPsXe7Ciyv8CkCy48xMkOmUlbNbyY-9PB6W746iypNzqj-o8G1xF-wX1MCHr7PznLU39yTJQzFs82M81yOEezEOSSOt8_A0FpP7bdUHJf1BRMX_2ks5srzmkWEd1yeQKctACGhCK4PioQS1wnr6KH-wP7N7UhEa1_OUznclJ03pWA8kqHEsWvkFWX1_1U3WoTsjKJ4YLU_x6ykOxi1r3i-M9n7AcaDFsjwQPcByqib8bIze5S6zoYeG4j_zgqfdYCmZr2PH2AqGZSJhWdiuVVf1T9zk_9fb-q-K2J-6TIg0kceU9A5dRSxIIieA6QPRo0yPlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KItroriZfeuOzfXUFLOg_NP3da2eBJ9e1fZNLM-x78lrSIP2GRfpBpfOgFhgGQXjftxRK3h32ANRnE6XQUX4wmFAHEADg3RzKAfTijtQBWYTS6EavYVSwLgq5ucVn6o5eFlb4XKfuu5LogKw1B6d85JkCA5wiGOJkpGbt_GqsJzLZfR8JHav9D2Mp3ZHuUBw5wFuQvvOdJLAhDEW_IRq-RhycpwKNOKGwiMwtxlXecjf8eC0o0VEnEzjAAxrRWErzg9CvsyJ3yw42ce_C5I7OF9NYVsWbmwQwzYTGHzQ050ueNgjcW2U9wnTrX9HkaZCF-nIecZe4_R5b13vfPqqlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
کوه دراک شیراز در حال آتش‌سوزی به دلایل نامعلوم
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68734" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68733">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZuGw3Hr4lEsPLW3R23-HkriAk3EjiKv4yYwP7n958pDHyCWtnSsnKF2GMwGFn2N5ddtkBpXR3u6TTXRzCkTp_tC_EbedEjPj5_upngwsbuv_hBFRUyMvOR48Ke7NwfCZOx1aLDEoIGGyR4_y61XkEYLZLr-jGHsysA1z7PHJ0nVnikgBhF8KbibqZNIcmgMC4ooCZzJ0S5hOEUHEWv_rhzcku-eUol6z8PEW8EwNEVZDsfs6Gb631ZC8vpz7DtyBNCHA2O42qHHh8oE3gddJ7VQdwKVyxn2IBP_8okDUuLa6BJR8OX4gYuY6mkZSX1zQ85x3ezKCCi5K8YWme4gdPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
گزارش های تایید نشده از آتش‌سوزی در کوه دراک شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68733" target="_blank">📅 20:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68732">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba9bba21a8.mp4?token=uwpNJHfWHD2h4zP5_QO9KDCce6s_cG99jaUWpdbaQMtWI1r_EKtmK3ZX8gV05N7RcJF3_sZ-21OT_h0qjewl-7Na9FyEqTKK-XAChKAS64-uhcm50quu2cU6ZsskFPy3aHFDo6-NgrvK0WMoL4CjK32_NpwGbg8TtXbfe_yHCysqufRxUaolSl92CNjhfZFkUIjkk0pRtIOEmV3hjZmD0BRCahpc3VTtRpfVdxbQKlc5-9K1gbQVACOC6h20y2kWpE-kC49SzbenCPoTZBCNlQg9BXFPdRfesaFpHm3728KvOwATxJoNIkcUwAksWIDamdYU18egT5_yWnJURaY_uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba9bba21a8.mp4?token=uwpNJHfWHD2h4zP5_QO9KDCce6s_cG99jaUWpdbaQMtWI1r_EKtmK3ZX8gV05N7RcJF3_sZ-21OT_h0qjewl-7Na9FyEqTKK-XAChKAS64-uhcm50quu2cU6ZsskFPy3aHFDo6-NgrvK0WMoL4CjK32_NpwGbg8TtXbfe_yHCysqufRxUaolSl92CNjhfZFkUIjkk0pRtIOEmV3hjZmD0BRCahpc3VTtRpfVdxbQKlc5-9K1gbQVACOC6h20y2kWpE-kC49SzbenCPoTZBCNlQg9BXFPdRfesaFpHm3728KvOwATxJoNIkcUwAksWIDamdYU18egT5_yWnJURaY_uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
چندی پیش، همزمان با تهدید رئیس جمهور ترامپ به حمله به «کوه کلنگ» مستحکم ایران، چندین بمب‌افکن سنگین B-1 Lancer نیروی هوایی ایالات متحده، خاک بریتانیا را ترک کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68732" target="_blank">📅 20:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68731">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cdd4a3d5a.mp4?token=puhyTutwqEv4YTcemJrvMYAdJx2yz2eIqWALouALPqqbVDjMrsnyW3H4z5cJGrH8jFOmB03s9SJyciGppjr8co50E9S_np4zG-Y4QtnrhLgT2LnIjsfcgODielpLdSPiNzDSnf6GEF7DjEyTpNOHS4zal65sVvjFns-S-HA5YmwaqsgApjAxPEY4RNVYO58hSZ-GHLObQ6IS_cQYPGWIW3aBpnq1pPyEYSPwzgkdnU3fK9qq5CkIisfIDhHh6crZm6VyRFkmIcJFwLo5IYrK6cP8llr2ZtHYAIUhm7S0Lcjchzbc3i0mYd_2TIirpUqP3U_fZpDp4XqGLg368xgvrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cdd4a3d5a.mp4?token=puhyTutwqEv4YTcemJrvMYAdJx2yz2eIqWALouALPqqbVDjMrsnyW3H4z5cJGrH8jFOmB03s9SJyciGppjr8co50E9S_np4zG-Y4QtnrhLgT2LnIjsfcgODielpLdSPiNzDSnf6GEF7DjEyTpNOHS4zal65sVvjFns-S-HA5YmwaqsgApjAxPEY4RNVYO58hSZ-GHLObQ6IS_cQYPGWIW3aBpnq1pPyEYSPwzgkdnU3fK9qq5CkIisfIDhHh6crZm6VyRFkmIcJFwLo5IYrK6cP8llr2ZtHYAIUhm7S0Lcjchzbc3i0mYd_2TIirpUqP3U_fZpDp4XqGLg368xgvrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست، وزیر جنگ:
به ایران فرصت‌های فراوانی داده شده است تا مذاکره کند و نشان دهد که در قبال تنگه هرمز رفتاری معقول دارد. اما اگر آن‌ها بخواهند به کشتی‌های تجاری شلیک کنند، آن‌گاه ما — همان‌طور که رئیس‌جمهور گفته است — ضربه‌ای ده برابر سنگین‌تر به آن‌ها وارد خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68731" target="_blank">📅 19:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68730">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46342c6e91.mp4?token=S2o2x3x0K19Uy97TVG7yaETCEmJ4IBRLPo0IHyPKQO9vnskL7FCVdEZwRYtZ9vlpDOwE6-b5hEkef_dBwMr267lBFIyzRqTJWaenDW_3lWo0LHLS5Fpa_gNhAJ7khcWax9n_FXMFNOsqkF1x7wgQYLoCjS39UnLKBAT1W1LU3_gFOPoJl6jgupahoURyUkzwZAGedGufUm-kwqITJz_oylRFQUEr0efFriiWeXLBN3KhPNDSD8OxPVDOo8sjQlu14v1q9oTSFloG_O5jMXwsZ5_TfNmgRXSYzq0O2WxmBGBH73uCAM91oZWlxu0T-UvuXvLMvHxiP1iH_qYCbmGJRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46342c6e91.mp4?token=S2o2x3x0K19Uy97TVG7yaETCEmJ4IBRLPo0IHyPKQO9vnskL7FCVdEZwRYtZ9vlpDOwE6-b5hEkef_dBwMr267lBFIyzRqTJWaenDW_3lWo0LHLS5Fpa_gNhAJ7khcWax9n_FXMFNOsqkF1x7wgQYLoCjS39UnLKBAT1W1LU3_gFOPoJl6jgupahoURyUkzwZAGedGufUm-kwqITJz_oylRFQUEr0efFriiWeXLBN3KhPNDSD8OxPVDOo8sjQlu14v1q9oTSFloG_O5jMXwsZ5_TfNmgRXSYzq0O2WxmBGBH73uCAM91oZWlxu0T-UvuXvLMvHxiP1iH_qYCbmGJRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره حمله سپاه که باعث کشته شدن دوتا امریکایی شد:
«داریم توانشون رو در حدی از بین می‌بریم که هیچ‌کس فکرش رو هم نمی‌کرد ممکن باشه. واقعاً ضربات سنگینی خوردن.
البته تونستن یک مورد رو از اردن رد کنن و اگر افراد دیگه‌ای مسئول عملیات بودن، چنین اتفاقی نمی‌افتاد؛ چون ما بهترین تجهیزات دنیا رو داریم.
ما تقریباً جلوی همه‌چیز رو گرفتیم. اما وقتی کار آمریکا رو می‌سپری به آدم‌های دیگه، بعضی وقت‌ها اون‌طور که باید پیش نمیره.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68730" target="_blank">📅 19:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68729">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3516843a5c.mp4?token=hkWXvvdHja1ZFrzWAkrARO6iesLnPCKCjf62_xgw7e9Qe_KFDxzCGIp1W3YKvhla-DDu_Y0MuhDcieXDK43AsJSBAqonLo4jYY0x-3kD1ySCmXHTsuuedxLdtH4_NzhNDc9cWFlEgp-kjewsJ0K6R4MyxxTGJa-RmPUqQzpjPipiV9LWaLIQF9QKNSt6-eLwp9lgnFKAyH2UXaq--Ci2nrqiCB9eqZX2dGxzkzjpQlHMQ3uXNBdPnS_Pf3AvUlLg193rCHj1UBKduZJHVVR0ivwl6q1sQ0O_5WOe2LKs2TKSmg5_sOdQKrUEPuqeO1rJGD2_wJ8nonmTZGf39TmYHggiCz6wwfPM7uHb5F55zA0zez_x5m70SnmaBVlLBwRhT0qG-pDSQ1Zh6xoDozRhV_XFBu1M-n0dK0aJSZyW-1nlp7_8NeIPDTTLX0KCfnxujEv9bpjE6ykFsmSJ23ukhKXAc1zShgf4SV4Zzb9-RJO_JGConajCT_MPYbuoCepTuaEwG1QKR1R8qo5WwpRZlqOeA_CfIaLRbeRp-EUrBHDIa9U3fR72BRZJW2Z0tszRtRpJepJbzF440JQZmYDFMKqEk1KAVyAQf3tj9if4FVhjiCqEqApvE9I12OeIkcXfx1TwVM_w-dinsMrxnx08NRG4WkTtEJ_drk9_ob_AEF0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3516843a5c.mp4?token=hkWXvvdHja1ZFrzWAkrARO6iesLnPCKCjf62_xgw7e9Qe_KFDxzCGIp1W3YKvhla-DDu_Y0MuhDcieXDK43AsJSBAqonLo4jYY0x-3kD1ySCmXHTsuuedxLdtH4_NzhNDc9cWFlEgp-kjewsJ0K6R4MyxxTGJa-RmPUqQzpjPipiV9LWaLIQF9QKNSt6-eLwp9lgnFKAyH2UXaq--Ci2nrqiCB9eqZX2dGxzkzjpQlHMQ3uXNBdPnS_Pf3AvUlLg193rCHj1UBKduZJHVVR0ivwl6q1sQ0O_5WOe2LKs2TKSmg5_sOdQKrUEPuqeO1rJGD2_wJ8nonmTZGf39TmYHggiCz6wwfPM7uHb5F55zA0zez_x5m70SnmaBVlLBwRhT0qG-pDSQ1Zh6xoDozRhV_XFBu1M-n0dK0aJSZyW-1nlp7_8NeIPDTTLX0KCfnxujEv9bpjE6ykFsmSJ23ukhKXAc1zShgf4SV4Zzb9-RJO_JGConajCT_MPYbuoCepTuaEwG1QKR1R8qo5WwpRZlqOeA_CfIaLRbeRp-EUrBHDIa9U3fR72BRZJW2Z0tszRtRpJepJbzF440JQZmYDFMKqEk1KAVyAQf3tj9if4FVhjiCqEqApvE9I12OeIkcXfx1TwVM_w-dinsMrxnx08NRG4WkTtEJ_drk9_ob_AEF0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ:
«قطعاً به سایت جدیدی که درباره‌اش حرف می‌زنن حمله می‌کنیم. کل این ماجرا به خاطر سلاح هسته‌ایه و اون‌ها دارن تلاش می‌کنن دوباره یک سایت هسته‌ای راه بندازن.
ما اون سایت رو هدف قرار می‌دیم. هر جایی که حتی فکر ساخت سلاح هسته‌ای توش باشه، با قدرت خیلی خیلی زیادی بهش حمله می‌کنیم.
هیچ‌کس، جز خود ایرانی‌ها، نمی‌دونه چه میزان خسارت بهشون وارد کردیم.
اگر همین فردا هم از اونجا خارج بشیم، باز هم یک موفقیت بزرگ به دست آوردیم. ولی ما فردا نمیریم.
راستش رو بخواید، هنوز هیچی ندیدن. ما تا الان باهاشون مدارا کردیم.
من اصلاً باور ندارم که بتونن دوباره خودشون رو بازسازی کنن.»
🎙
خبرنگار: «فکر می‌کنید ایران سانتریفیوژهای هسته‌ای رو جابه‌جا کرده؟»
🇺🇸
ترامپ: «ما مواد هسته‌ای رو ردیابی می‌کنیم. اصل ماجرا هم همونجاست و به احتمال خیلی زیاد، خیلی زود اون منطقه رو هدف قرار میدیم.
کار زیادی هم از دستشون برنمیاد. معمولاً همچین چیزی رو علنی نمیگم.
اگر فکر می‌کردم می‌تونن کاری انجام بدن، هیچ‌وقت این حرف رو نمی‌زدم. ولی خیلی زود اون منطقه رو هدف قرار میدیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68729" target="_blank">📅 19:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68728">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0f808d08.mp4?token=RyyijjSQ5rI51rHKBZ-dikfowGJ_uy1T0VZG6nGasV_N3fHy1MXs4vN8wlTDKcg9rPjJfb5gvvwdtChlFbXuls0JS_knS6VLqi-ZmA1PB7tc3Uu7N8ANxyhO-pzqISmfAuAv8B0cJyPlAFH5wAYuKXQ7cya2tDAmgmMrQIfWb1WqbQBeRpkk2OmtJN6DjrrsGbNk6Jlwa7DUnj0s955s14uJhZdNzkuOVgySCYRZ2x7ssnm8IgNd2XDKBKwCRqEEjsBM7LQ9Fmx-o9dBy6RYXHNIz341syXtkCGzWNdjRuzsZCJJKH2ky8gBzMPeA1n3h5d0kKXWiSXf12rpbNYsEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0f808d08.mp4?token=RyyijjSQ5rI51rHKBZ-dikfowGJ_uy1T0VZG6nGasV_N3fHy1MXs4vN8wlTDKcg9rPjJfb5gvvwdtChlFbXuls0JS_knS6VLqi-ZmA1PB7tc3Uu7N8ANxyhO-pzqISmfAuAv8B0cJyPlAFH5wAYuKXQ7cya2tDAmgmMrQIfWb1WqbQBeRpkk2OmtJN6DjrrsGbNk6Jlwa7DUnj0s955s14uJhZdNzkuOVgySCYRZ2x7ssnm8IgNd2XDKBKwCRqEEjsBM7LQ9Fmx-o9dBy6RYXHNIz341syXtkCGzWNdjRuzsZCJJKH2ky8gBzMPeA1n3h5d0kKXWiSXf12rpbNYsEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ :
«جوون‌ها رو می‌کشن؛ انگار هیچ ارزشی ندارن، انگار آب‌نباتن. واقعاً آدم از کاراشون شوکه می‌شه.
همین‌جوری الکی مردم رو می‌کشن؛ بیش از
52 هزار نفر
کشته شدن و هیچ‌کس هم درباره‌ش حرفی نمی‌زنه.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68728" target="_blank">📅 19:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68727">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18745bb1ea.mp4?token=irMGIltKPLRZ621CqSKsT66-3PjyGzdUyE30S7f3bVw7pc0aT7_KNtOYtvx09s1Fw5bm-n22UDmqDNGUmt7XWJrN_7GxSplFmzC18DS3p8Zsb81Rvk3PsEBABTr7A9kU3Fd6k4rgEylxcQyOxMuRiOSeuj7kf3IjsCzszP87xFPhgnMx6YYcV8SYR5xd1VwP10gUBrJ2TakWVoS92YMHLks5csI1ln_OhU3aSB6LUxW6sip7buBbO1BYy_XRaXf9sJs0Ne7ahIet6a0UNo3RPKptitzsOFvYS_OLAZlWXogyT-QvznK1h3p9PmGspnscGWCVyeOH0RwixPZ0qr_vvZPIzUMyI6KsSWgxJkiA4L1fKACvdF2hq6ETP6WSEYEU_biZwDry0AMtgay3W2JhHBTV1wne13Ekp6Y22kuZI0NfQizEeUiakGv7gAocDoGfa6FGj4GlFar_IRbboiqYyhMOvOTZGB03BVIVZ70fUZ8Q4Mt21IyCRElfD-5rf1av6rGkSf_-MOXCh8lmUjaBYPFcq5ZyAea8jJjhc7SCWe5CLAKvzmmc8NQBXw7fo3yS2ZQ7zb9IZYUUKvB9hp6QR-uDXJ-Pi2xyJV88r0Z_vuj4joiinE_floT6LYq0SpZmu6ag70GyPsf8eFs2mriC0OzhgE_ZjkS9G9TmlZEZ8OM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18745bb1ea.mp4?token=irMGIltKPLRZ621CqSKsT66-3PjyGzdUyE30S7f3bVw7pc0aT7_KNtOYtvx09s1Fw5bm-n22UDmqDNGUmt7XWJrN_7GxSplFmzC18DS3p8Zsb81Rvk3PsEBABTr7A9kU3Fd6k4rgEylxcQyOxMuRiOSeuj7kf3IjsCzszP87xFPhgnMx6YYcV8SYR5xd1VwP10gUBrJ2TakWVoS92YMHLks5csI1ln_OhU3aSB6LUxW6sip7buBbO1BYy_XRaXf9sJs0Ne7ahIet6a0UNo3RPKptitzsOFvYS_OLAZlWXogyT-QvznK1h3p9PmGspnscGWCVyeOH0RwixPZ0qr_vvZPIzUMyI6KsSWgxJkiA4L1fKACvdF2hq6ETP6WSEYEU_biZwDry0AMtgay3W2JhHBTV1wne13Ekp6Y22kuZI0NfQizEeUiakGv7gAocDoGfa6FGj4GlFar_IRbboiqYyhMOvOTZGB03BVIVZ70fUZ8Q4Mt21IyCRElfD-5rf1av6rGkSf_-MOXCh8lmUjaBYPFcq5ZyAea8jJjhc7SCWe5CLAKvzmmc8NQBXw7fo3yS2ZQ7zb9IZYUUKvB9hp6QR-uDXJ-Pi2xyJV88r0Z_vuj4joiinE_floT6LYq0SpZmu6ag70GyPsf8eFs2mriC0OzhgE_ZjkS9G9TmlZEZ8OM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار: هیچ نشونه‌ای نیست که ایران بخواد جنگ رو تموم کنه. پس برنامه‌تون چیه؟
🇺🇸
ترامپ: تو از کجا می‌دونی؟ چطوری می‌دونی که نشونه‌ای وجود نداره؟
چرا تو چیزی رو می‌دونی که من نمی‌دونم؟
تو نمی‌دونی چه گفت‌وگوهایی پشت صحنه در حال انجامه. اون‌ها به شدت می‌خوان ملاقات کنن تا بتونن این قضیه رو تموم کنن.
اون‌ها به شدت می‌خوان ملاقات کنن.
تا وقتی که آماده نباشن به شکل معناداری ملاقات کنن، ما هیچ علاقه‌ای به ملاقات نداریم.
ما دارم اون‌ها رو به سطحی پایین میاریم که هیچ‌کس فکرش رو هم نمی‌کرد. واقعاً دارن به شدت ضعیف می‌شن.
البته یه چیزی رو تو اردن رد کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/68727" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68726">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/68726" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68725">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ik7DdpP88EufKgjlExDX_HYaA0KL7pjXGVXjmUFlMUbrijvAqJmGL8aoAM1c0eSF9Yw3lUAIWJMhghSE8_1Y_Ig37exx-MYpUETMrogHhwwQE7ZMCC_3HJiGYDra2AmSMJcxigClBQVeMd19IK5zDHgR9kHk_WCp4MPgDq1QFzMxbY3x1dBQsyMk5ixcUSs_oA4KrHhWWKgJA8p8GH5LTg3G926wUJhyniQf-247bawQDDspERD5ngiGP-WxOtbISp3BPJC2ZDIM5Wr5xH7fj5QXOgukvPjJSEHiILixkbNMkrMK_7FJ5teNdeXNSfYGYfFuYyXNdENcWplf07ugHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68725" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68724">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d3d23d787.mp4?token=No9D8tPOyxEDhygXj-GlIt1QxTAE4vr8xue1OkqE5gYS-MmJdaEPHjQXui3-0g_WhFTCFQKTJks_5C25NDWIb0lPAFeqMZWoBMjJ3tw-luLw2jMS-v9f5xUvLKCWK8tu6ZnkHn6gVPuUx7ruInJac20E-zFayyS1fze0nE8XjJszCxtO2DVT6h_1AUHJJ_fXPLgxHLy1nE8x6-W7mhCW7X6E6-dkNlxreJq8KY1NOnNtgZL7aEP-gfz4jnWHpn8yr-F40956_xheW1e_ul_jl1HO16Oj4hfsW_xXINbmrMh8Lg_GcZFfm1Wyy1UWgyHo7P9hKBdeNZBm2Ns6U06DFxwRNBwUXpVI5nUOK_V_C4T_JWPkxl4P4W23kHQ95TFQj4lHWSyQ5fElDzQe4StbTEmH4N-WOMs6y0__NNVRvgnrds_Vht56PFQR3GZ-iWJLVvuTLx3n0kcaQhPs60CzMsiF_So1o9vInlxJRjMnduivAJfqaFAXlGmNGIBKInvyK5y1Y6Qk7RYf-q-LtSLaGY-OTqpD7gWvLl_3tap9CTxxm42xFujHjeuJ79bIZp-6aRZ6Bg_p4DNlt_i0G8ThOLX8CGBByjnJSmwMlNP5KETb_BvFCUnFp_ODAlxM0ST4cMZPVEhRLk3D7eI2uky0x3bd5m9XANt2NTGjzzq685g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d3d23d787.mp4?token=No9D8tPOyxEDhygXj-GlIt1QxTAE4vr8xue1OkqE5gYS-MmJdaEPHjQXui3-0g_WhFTCFQKTJks_5C25NDWIb0lPAFeqMZWoBMjJ3tw-luLw2jMS-v9f5xUvLKCWK8tu6ZnkHn6gVPuUx7ruInJac20E-zFayyS1fze0nE8XjJszCxtO2DVT6h_1AUHJJ_fXPLgxHLy1nE8x6-W7mhCW7X6E6-dkNlxreJq8KY1NOnNtgZL7aEP-gfz4jnWHpn8yr-F40956_xheW1e_ul_jl1HO16Oj4hfsW_xXINbmrMh8Lg_GcZFfm1Wyy1UWgyHo7P9hKBdeNZBm2Ns6U06DFxwRNBwUXpVI5nUOK_V_C4T_JWPkxl4P4W23kHQ95TFQj4lHWSyQ5fElDzQe4StbTEmH4N-WOMs6y0__NNVRvgnrds_Vht56PFQR3GZ-iWJLVvuTLx3n0kcaQhPs60CzMsiF_So1o9vInlxJRjMnduivAJfqaFAXlGmNGIBKInvyK5y1Y6Qk7RYf-q-LtSLaGY-OTqpD7gWvLl_3tap9CTxxm42xFujHjeuJ79bIZp-6aRZ6Bg_p4DNlt_i0G8ThOLX8CGBByjnJSmwMlNP5KETb_BvFCUnFp_ODAlxM0ST4cMZPVEhRLk3D7eI2uky0x3bd5m9XANt2NTGjzzq685g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه‌ای، (خرداد1384):
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68724" target="_blank">📅 19:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68723">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇷
ابوالفضل بازرگان تحلیلگر سیاسی وابسته به حکومت :
⏺
بی تعارف نشستن منتظرن جزیره بوموسی و خارک و لاوان بگیرن
دارن ماه ها روش تمرین میکنن برای اشغال این جزایر
برای اینکه یک هفته دو هفته نگهش دارن و یک کارت جدید بزارن رو میز دیگه برای گرفتن ذخایر هیچ مشکلی ندارن
🎙
مجری : یعنی پی تلفات انسانی به خودشون میمالن؟
🔵
بازرگان : اره!
اولن که تو جزایر ما هلی بورن بشن ما متاسفانه باید از خاک خودمون جزایر خودمونو بزنیم
به ویژه بوموسی که فاصلش دوره
اگر صبر کنیم اونقدر که برسیم به جایی که یکی از جزایر گرفته بشه ، بگن حالا اگه میخوایی جزیره پس بگیری باید تنگه باز بشه ، تنگه هم باید تحت مدیریت من باشه یعنی مثلا من باید بیام تو بندرعباس پایگاه نظامی بزنم و ذخایر اورانیوم هم باید بدی
الان میگن تنگه نگهدار ، ذخایر بده حالا اون موقع فک کنید میگن خارک یا ذخایر ؛ دیگه اون موقع مگه میشه ذخایر ندی ؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68723" target="_blank">📅 18:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68722">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2ErqBP6OpVr5hFtNjLLDTkyzQPsV-FMnYVaaf_3HKFGFheB6ZjSFs69XtvD_ns4zCBg7DxrHpFJ7fC_e_vhv5JH8IYS2fzgHuwT6C8rwXeqSt9bR4FCQBQpX0K1s4QfB12h3HkuzgXnaZDquC6T6fOdql-rEXpQydIFPKUg-rZgFXscXu1DR7V8C6tBOzmUXZjbrgR7Wc3tZOSKc3xJ51M7NYpyHRWJ3aZu0dVNjj1i1E-I8y6m_MEY6FwiV-cR5PdyKyR1g3khg91XRPaYEXDay7p7x-12pj2KQBHZ4zQq_DO7WZP6LxM4vi1Ht7iEGpPx3mRqiqqEGl939Sc0gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پست جدید ترامپ در تروث:  این آخرین نفر از بین بیش از 52 هزار معترض بی‌گناهه. وحشی‌ان!!! دموکرات‌ها کی می‌خوان بالاخره بیدار بشن؟؟؟ این گل‌محمد محمدی، 23 ساله هس. امروز صبح توسط حکومت جمهوری اسلامی اعدام شد. تنها. بی‌گناه.  @News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68722" target="_blank">📅 17:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68720">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/Igk8VSXCIaob-PPuN-C_mMTmSDUtqQt_nz5iqWLzcGNWmz_9dOXUGpcnfc-rnuzirVz0NrVfR7W0fnevnSU1lUgl9vof80Yi4YjXTCal4Ec9Nj5_pQW9-2kLAUwNDHeKiVClUW5KPEJfyWXIHVBA0G_A4nrrtNzkHEfkA_mMffVFIKWX2sBoQhztg86N6iJJpFcnUuvh783NVqsE2Msthg1X8_vHy9H1aIyrfWcR0iaIqfMQ_L55Mtyazbe05ClWnMxkYM-YVo-IRagL-8IkCIFxlnADY6nma7oPjLJSgRVme4oqYlInNTDukcQZgmsL_B7Mis8rzeBhBREEnEwqkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/seNDF-_CuODg-nwypiXyAB_0WwY3WijdmIrZmehgqg38QF403TmxJ7DjTb11xnAjH596bLUwJ2QOlrA0iSN0oD_OPOtEy_3SYbpKBpPrdBuWF0Zym9oOqqutlM3npTG1qz6dHT4W5cCAmT6AwRmLK8DrdGfUprJj7_nATN256arIg7qkAYneC03_0tnjCcab_vtyG5UXgNz9uUshhtv9hMZVNTqkSBiC1ayE5AD7PCv_oWouQzeTa5K5jSaHyDfk-NgwWQBbuVC6baNpaEjqdCICUVSbjYQ_14a1orm1dPSmY1ve4c1m2TdwipQlATQpY5nN-4SjCfPvo2EiP0kPFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پست جدید ترامپ در تروث:
این آخرین نفر از بین بیش از 52 هزار معترض بی‌گناهه. وحشی‌ان!!! دموکرات‌ها کی می‌خوان بالاخره بیدار بشن؟؟؟
این گل‌محمد محمدی، 23 ساله هس.
امروز صبح توسط حکومت جمهوری اسلامی اعدام شد.
تنها. بی‌گناه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68720" target="_blank">📅 17:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68719">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c7e1427c7.mp4?token=KtKTJ7EPAoKCpT3J3P7kK3Qvb1XhevkaIgKKwOGZ-Hz-qNQURivKqGAw2xXnA2-WaVB-UFNokhsmpEczXpzZEtNMnHeWpWYnqioSSyF7U_0ola8NmiR6fgKtDvCcE9D7RFF6CnSBtgoLNeC9wRPvhmK18ZJsEzzfbxWKy9KYSftJ-vRJJKzgVYmz3_n3xFTr3ZBw5UWc2IuvdyfR9S6-RwK46ZTQnUr2s7BL6fV1RUpYmntMkgbBiQRWccfIc21pfPIJ1ANmLSUqWjr78A3aAGVIBLyJ6NBQiTcTQW7CfV_ijLH04scFYeN0w9q2kG7KTGyATewaHiUgz3VlXQFv3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c7e1427c7.mp4?token=KtKTJ7EPAoKCpT3J3P7kK3Qvb1XhevkaIgKKwOGZ-Hz-qNQURivKqGAw2xXnA2-WaVB-UFNokhsmpEczXpzZEtNMnHeWpWYnqioSSyF7U_0ola8NmiR6fgKtDvCcE9D7RFF6CnSBtgoLNeC9wRPvhmK18ZJsEzzfbxWKy9KYSftJ-vRJJKzgVYmz3_n3xFTr3ZBw5UWc2IuvdyfR9S6-RwK46ZTQnUr2s7BL6fV1RUpYmntMkgbBiQRWccfIc21pfPIJ1ANmLSUqWjr78A3aAGVIBLyJ6NBQiTcTQW7CfV_ijLH04scFYeN0w9q2kG7KTGyATewaHiUgz3VlXQFv3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمعات شبانه
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68719" target="_blank">📅 17:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68718">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVqaBkM1W662aenl95Dpr8DCj4uvTJqtmTkuM3YHtNAyh03vyELWtFkZNYH62hjFxGwJUkbxBGsGJj5F6qGjUjyFfXIXHAWVSioZOUS2pnXOxGOJubCrYCqfvUson_UxodF0fn1qoEbE16Db_o2MfQLYKmGfDhsu9H_a6oBi1er_FJlFRy-4yVcs1x8qvRquqcyiG7L9NuJXv97doyZAv4m31M0D6MooEHEKgRv0rRKtNlmnl8vGTQ7duXpmP78SiEc8XabHa1kqznZ-pTVqN_mRJEBct1a-SbO9R5snTue-D6_FcZDal-JNkuViQ5M0Hs-4qBKqxqz54gMc8U950w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
هویت نظامی آمریکایی که در جریان انهدام کنترل‌شدۀ یک پهپاد تهاجمی ایرانی در پایگاه هوایی اربیل در تاریخ ۱۹ ژوئیه کشته شد، گروهبان «مایکل سوینتون»، ۳۰ ساله و اهل فایت‌ویل در ایالت کارولینای شمالی، اعلام شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68718" target="_blank">📅 16:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68717">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da37587eed.mp4?token=TxbUODW69um_X-oHpr9Ri9X7G3XTuvqIBuZcYVBOMyhlhhsvO7pTkfUjHY-rzakaeiYxsBiIzAzKnTQI8dh5Zpl0s1LjHg7AXq6L3J54pdqR4rDiIRnIUlw5WtdZrwXDaf2BmQw3SBGALE-HeJGkE2PyAa-z62g-lFWe6795rNNQ3SJUmZByohABuSr1Lm_077aAC8qVaoyv3EIA5QiqKCYVdxomuHQMFlpb2z0yn0SEttv5qm43k5tJdhrH23Ts50F78P6MrLcUgk-gYLPisJ3ANUYWOxi5uYFATZlnyZTNZJpHsZYxU-j0imx0rDoKI-UuxJXo-dZjNEMUX9oftg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da37587eed.mp4?token=TxbUODW69um_X-oHpr9Ri9X7G3XTuvqIBuZcYVBOMyhlhhsvO7pTkfUjHY-rzakaeiYxsBiIzAzKnTQI8dh5Zpl0s1LjHg7AXq6L3J54pdqR4rDiIRnIUlw5WtdZrwXDaf2BmQw3SBGALE-HeJGkE2PyAa-z62g-lFWe6795rNNQ3SJUmZByohABuSr1Lm_077aAC8qVaoyv3EIA5QiqKCYVdxomuHQMFlpb2z0yn0SEttv5qm43k5tJdhrH23Ts50F78P6MrLcUgk-gYLPisJ3ANUYWOxi5uYFATZlnyZTNZJpHsZYxU-j0imx0rDoKI-UuxJXo-dZjNEMUX9oftg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شاهزاده رضا پهلوی در گفتگو با رویترز:
«دخالت خارجی در ایران لازمه. این مداخله در واقع می‌تونه باعث بشه جان آدم‌های بیشتری نجات پیدا کنه؛ آدم‌هایی که در غیر این صورت ممکنه کشته بشن.
جایگاه من به‌عنوان رهبر دوره انتقال اینه که مقصد نهایی نیستم؛ من فقط پلی هستم برای رسیدن به اون مقصد.
برای اینکه بتونم نقش یه داور بی‌طرف رو داشته باشم، خودم رو وارد هیچ جناحی نمی‌کنم. نه طرفدار پادشاهی هستم، نه جمهوری.
وظیفه من اینه که مطمئن بشم یه بحث سالم شکل می‌گیره و در نهایت، این مردم هستن که تصمیم می‌گیرن چه نوع حکومتی رو برای آینده‌شون می‌خوان.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68717" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68716">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🎁
بهترین اسلات‌ها با چرخش‌های رایگان یک بت
💥
تسویه سریع و آنی جوایز شما
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💯
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68716" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68715">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BR9oKWYCiUqjPZN3srbQjCxXyFN1x0iUNqNQts8Q4ZZUDo29s76MpMhWbMJB9agnB9b7IZYF1XEtZsncpR9BF7wBOO_qsV2D3URQZFp9tt-mKkZRaaqieD9x2QlxrfoSk7JrD88q5PCHezcYWX-QXKOL0C0kMn8fQhOInPszWHp2AhBt22rOCtQ0CtJaU4BhCVse-hMJ6qCfcpGUJ1FlQS0Dvm186WeBGNZMV9biSx_tQ01hQ2LUMCmSpJJPrAIeoYEJORK3Z2B_QcISxR5dG1GmeD5RJHFDHfr-KXyJPfidMW3iwmfVL62P_ywR8cr7E2Z1uBTxPx19jImqYNCDwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
فری اسپین‌های بیشتر، هیجان بیشتر!
🎰
با واریز از طریق کریپتو، ووچر پریمیوم، ووچر اتوپیا و اتوپیا، بیشترین پاداش را دریافت کنید!
✨
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68715" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68714">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpvTNT8JrNyk7tD8ff3CkI6C7QoYNCaekvLirnmHQH6khkxlpfP7D9Vfk_vtqdQF8L0WItjH925mZSeAcPMqmXjJzRwXDi9Me0WWaY6UoYZhsZT5SE7SXu3pHGHsCHGLRXCrNzegid7c91e3y2Z_D26AmY3I4EsRExL1IWZVvXvY45GPp0w9VtlIU8TqG5_sGiqMC5ZHd8ix9WuJCnqwTOND1LC9PaNfgv64hl-sozBbnfVHwGZmz_qgl8-QiMF70ucVKtqLErAwXE7eSD6XSNt-y1Nuyzx-ekmfSbXA1fiM4N5m3hVt38qegptoqUuuPh6Xk94MLWruhJySBwIyig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مراد ویسی، عباس عراقچی رو فالو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68714" target="_blank">📅 15:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68713">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‼️
🤩
عکس یامال و تیم ملی اسپانیا روی پهباد شاهد چسبوندن که بفرستنش سمت مواضع آمریکا تو منطقه  @News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68713" target="_blank">📅 15:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68712">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b6161f8d4.mp4?token=r5EG4HNFbt59rNdU8hwvtR7CJ0BcMsjx8IpddzRczbELCTV-xKGXfTelzSY34pJSTlRD9GE3qqkiTx6pRxwVlVeC_76IUzecklWMdCcA4IABk1ezMCzr3ZORlqnVF4DC78tyAh7R7DBAUdEL3sBT359TlVFShzegPofBj76hRjmCJo3cKjccuEn1J2V6z4FG3XHtmHjGe9c2gOpH2WlUYOKdDRb0Zpd_YI_XZcbfdxHbOE_GHLcSmxiggHMcO0HomPwTiUmg2QImWbJnC8QFlsBbGp_Ue70yvCMKSB_pZioEyKEPkb1dVerCq1Jqe0J-V3mtEFBVf0qd1LoYV7iPPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b6161f8d4.mp4?token=r5EG4HNFbt59rNdU8hwvtR7CJ0BcMsjx8IpddzRczbELCTV-xKGXfTelzSY34pJSTlRD9GE3qqkiTx6pRxwVlVeC_76IUzecklWMdCcA4IABk1ezMCzr3ZORlqnVF4DC78tyAh7R7DBAUdEL3sBT359TlVFShzegPofBj76hRjmCJo3cKjccuEn1J2V6z4FG3XHtmHjGe9c2gOpH2WlUYOKdDRb0Zpd_YI_XZcbfdxHbOE_GHLcSmxiggHMcO0HomPwTiUmg2QImWbJnC8QFlsBbGp_Ue70yvCMKSB_pZioEyKEPkb1dVerCq1Jqe0J-V3mtEFBVf0qd1LoYV7iPPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤩
عکس یامال و تیم ملی اسپانیا روی پهباد شاهد چسبوندن که بفرستنش سمت مواضع آمریکا تو منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68712" target="_blank">📅 15:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68711">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICXCjZeWzRM-3kC5eKYeSOvMNknhFM4CmFt5atQYFCQQyG2EMcuMAmSfZk8oxrYFLffZLsrNQDgbxzseUnijw3KXba-3HhOX1qEGUkPeBFPfpOkFEQ7X-vef0of_KM9uChiaMjwL98MpzWTobUDDSkBO1s9OrAL9Qsh4Hy4aGOagN0AcycYYuFmP3ttuwBVVeM0C8RqB_iRUgw1MSDCmt3SBYVmPBAi1KvBS8GBroIJNg4rpNq8se8g37v8BAF6L30YX9ci_hGHyytdIAp88EU0HQsJsOvmICEEgkjCaDBedwNnn2R2Mij2Z0tKhEyhwbtFXAkqMuVEAQMe1H-kNjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
با اعلام مقام‌های کویتی ،  چندین نیروگاه برق و تأسیسات آب‌شیرین‌کن این کشور در جریان حملات روز دوشنبه جمهوری اسلامی هدف قرار گرفته‌اند و دچار خسارات عمده‌ایی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68711" target="_blank">📅 15:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68710">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acd31fc49e.mp4?token=fi6KqNulC9ZSPr8CG_jdha-L0nvh-FV7li9roy2zTnufS5yucJUfdpzoWEpOjzVPToMZdbKg9LFQu9bANPZEqYB_fd3l21IoZnXaNvdzPs6j1fA9AFeG2aEDYr9XVqbPda_lq-RmjwQ_9oPkvCsn9yDe9Qr1a3MVnoYxpnjWuKt3syl0bFORBBXw2s7AV8eBGSVfRsCsCPtT_1bQxNK827Bl0yQzC3HlV6h5pPEZwjDefQudWNoM-GeOJOjCIrn4V2UuAB2RPIjI9flpuhU_vRD6sE3OMK91h9306gaE2-ryt6lgx0oaI8aEvDgfQuDToJWqH1CavzlZlqw_-TU2Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acd31fc49e.mp4?token=fi6KqNulC9ZSPr8CG_jdha-L0nvh-FV7li9roy2zTnufS5yucJUfdpzoWEpOjzVPToMZdbKg9LFQu9bANPZEqYB_fd3l21IoZnXaNvdzPs6j1fA9AFeG2aEDYr9XVqbPda_lq-RmjwQ_9oPkvCsn9yDe9Qr1a3MVnoYxpnjWuKt3syl0bFORBBXw2s7AV8eBGSVfRsCsCPtT_1bQxNK827Bl0yQzC3HlV6h5pPEZwjDefQudWNoM-GeOJOjCIrn4V2UuAB2RPIjI9flpuhU_vRD6sE3OMK91h9306gaE2-ryt6lgx0oaI8aEvDgfQuDToJWqH1CavzlZlqw_-TU2Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ها؟
درست شنیدم؟
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68710" target="_blank">📅 14:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68709">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
صداوسیما:
دقایقی قبل نقطه‌ای در ارتفاعات خرم‌آباد هدف حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68709" target="_blank">📅 14:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68708">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🇮🇱
وای‌نت:
مقامات ارشد اسرائیلی مدعی‌اند که تیم «جی‌دی ونس» مانع از برگزاری دیدار میان نتانیاهو و ترامپ می‌شود تا از اتخاذ مواضع تند و جنگ‌طلبانه علیه ایران توسط ترامپ جلوگیری کند.
نخست‌وزیر اسرائیل قصد دارد این سفر را با مراسم خاکسپاری سناتور گراهام در ۲۷ ژوئیه هماهنگ کند، اما تا زمانی که از قطعی شدن دیدار با ترامپ اطمینان حاصل نکند، به این سفر نخواهد رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68708" target="_blank">📅 13:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68707">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f5cc929c.mp4?token=HNHiT6xV54umBs-7L9-zc1VUQYtd37bEB-2CYhyNqXhebh9SQdxJYMD4jZ4PKAImH9fLosruH6-z4G6tOLC5euvZRno3hOy0sIeaEoUA9W4A-v1Pn50DXb0GleXhqJ0Le38S75zP0W_WSuX5kInvsxYWRI8MVClecHe7lFj3Wa6vmg2pVcdn8JQ1MbzQgxdBIXY5r-OcVeliTrH1rHX7_mgbrALBzWvGNG8sinak7HjJe49PvTdwaxgPUeZFvBklWRT2CFPDfCE7VwsRieKyh_sPmlkRXBGgsKg2YoHnPgTE0MyOkbY_IwzErrPvPAhwaSdnWCKxhk88PW-G-f6aPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f5cc929c.mp4?token=HNHiT6xV54umBs-7L9-zc1VUQYtd37bEB-2CYhyNqXhebh9SQdxJYMD4jZ4PKAImH9fLosruH6-z4G6tOLC5euvZRno3hOy0sIeaEoUA9W4A-v1Pn50DXb0GleXhqJ0Le38S75zP0W_WSuX5kInvsxYWRI8MVClecHe7lFj3Wa6vmg2pVcdn8JQ1MbzQgxdBIXY5r-OcVeliTrH1rHX7_mgbrALBzWvGNG8sinak7HjJe49PvTdwaxgPUeZFvBklWRT2CFPDfCE7VwsRieKyh_sPmlkRXBGgsKg2YoHnPgTE0MyOkbY_IwzErrPvPAhwaSdnWCKxhk88PW-G-f6aPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پاسخ دفتر شاهزاده رضا پهلوی به صحبت‌های عباس عراقچی درمورد توافق پهلوی با اسرائیل برای تجزیه ایران:
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68707" target="_blank">📅 13:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68706">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427c084f6e.mp4?token=HRIODftLBUO0PdBGO98cRvU1x5sqgkyzpDC54exCGOJ3bR_xPHVgc3CNssScIf78lGRK8tcjDvZ-Q42eGEojYwxPq_wJ6B1m0Uh7TPr8V1iPwAdqw1OF-wsARLbeXYADQQFQDUijo4NTWEthaLe6_H4p8WtQhjd4ofVVIZUu0pQRPc40w-F7K8B5lK1j0lufOsjx1GdXar817irOFDNhAcNKRwx_CRoeKO81g8-qXXPftIhOq_3_xGd_b7FoCo5G0Rrym0sTUQ297GhiyURM3qIWxMFxW8uw74AdoK11fGzgCpxzNknYsmPVvHeIUJkZL08TmRQzIA-xkJ3DTUTFdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427c084f6e.mp4?token=HRIODftLBUO0PdBGO98cRvU1x5sqgkyzpDC54exCGOJ3bR_xPHVgc3CNssScIf78lGRK8tcjDvZ-Q42eGEojYwxPq_wJ6B1m0Uh7TPr8V1iPwAdqw1OF-wsARLbeXYADQQFQDUijo4NTWEthaLe6_H4p8WtQhjd4ofVVIZUu0pQRPc40w-F7K8B5lK1j0lufOsjx1GdXar817irOFDNhAcNKRwx_CRoeKO81g8-qXXPftIhOq_3_xGd_b7FoCo5G0Rrym0sTUQ297GhiyURM3qIWxMFxW8uw74AdoK11fGzgCpxzNknYsmPVvHeIUJkZL08TmRQzIA-xkJ3DTUTFdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حملات دیشب سنتکام به مراکز فرماندهی نظامی، توانایی‌های دریایی، سایت‌های پرتاب موشک و پهپاد و سیستم‌های دفاع هوایی جمهوری اسلامی.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68706" target="_blank">📅 12:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68704">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OSIw5nvOb1Ix1L1th6fYmj7WnSP_KuVfADDODJgOSzyPv-IP12g34WwtQoxfVrI1ZOBDP3SeGyZdq0fOoAe6SH9wHd0C0qxXHMOc7aRWe9FFe6r0dc_1tfu8Z5v2Z2YDM1lWLf7sLz-WSkzMKjC570QpKg6NYdV2vFlNjKNQZAeFHERn8QjFZivWXKo6qRCDg3peDtTiRUzjVbJMVQO0tio0BhKLbnvYhS--fJCH8-A0t33O5jJ4oIArQCfYar9X27Jv_aFOcvyluDwXA6QejOedZHfyTEViJP6_00rT-vJ-o93fv6rw-oJCBuMnq1EztEGgMY47dFwLgzHltNKyiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YtaKj5TN5ZqR-7zbC0OomVylQfSH4_kPBC9duk-fvlFTSjfJ-i4C68lB8KhSwB9r4XDiI-mZ4m9pRm57E8khOQcVYpBeE5pYIFEbfX63UALLmb58WFrxIMkm64I7J-lTZtNG_YkKSY29nD5o01BzBBlhoO_AFTGw9Eln1eK8NUNq7Kj7BcVYC3MsAv2SdFQwvDCnxmzRVm8LGQAmfWE5atHuRFz34Ukhaq6BbykjqbkSc-mxLq7tYx-S5Y9wCIeWr62OwO_gabC2dfYZ_ND4DNDf4kmwBHv_7H_ok3g5SZxE4BNVMysPLOlwUXIGCSdEWtYWob6ieX8j6u4Qcg3DWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
دقایقی قبل سپاه از زنجان و همدان به سمت پایگاه آمریکا در اردن موشک شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68704" target="_blank">📅 12:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68703">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1QtHjcruwrxBsi4HkBtJPUyNz6umun8mC9v_OyQ0KeIlA2YMHxiNHsDObvAWUNXAonuZHEfb9-Dpz6z71iDX61Rbz-LjXUW_v851GM6jwnc8zlCqb0quWve7vJgK-oSQkFfTCO81LOh4AVOz_YMBQOePuHt2yEC_RqCYHRj8mk6a9AL1J6_Nr_XWe2odvVP-OqtcVEE6XQHDH-kXyDdbqgrfSuledxEWiNxE0YdONkXDrAW0JZ91eIkuzB1ZAPs_4wbBTd45fuCX3pWSd42NNXujIh6pKL4W4yLPshpdfVZBq6qMlDydclg_uFLQv6oTOSGLRjGnLr5u7koFqt3Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
در خصوص مناقشه با ایران، مقامات ارشد آمریکایی و اسرائیلی استدلال می‌کنند که تنها دو گزینه واقع‌بینانه پیش روی ترامپ وجود دارد:
پیگیری یک آتش‌بس ۱۰ روزه جدید با هدف بازگشایی تنگه هرمز
آغاز یک عملیات نظامی گسترده و جدید به همراه اسرائیل برای وادار کردن تهران به تسلیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68703" target="_blank">📅 11:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68702">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⁉️
مقایسه ایران و نروژ:
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68702" target="_blank">📅 11:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68701">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b4d07166.mp4?token=MFaFKYY7sX6uHVLT25AsAZ3ukmz3fr6zzKQHA8SIKJ4Q9EjvEjQfX40PFgpm_PaIpWTIHDp1_jwYm3znne7-iNhkMRMTWp3WCWXnevs9FhTk2FoeU0L2b_OpEiZJhqew2NGM7BtOXpr0e-EmVUhWbZUpZWzxWN_KdNSBBuq8w_buPqGH7io0X9ofs4ihiaTkWaDn9bmIJVs50VqBQgBtJo6cNHvhjDdSd347OaQlaZM9FS2mXFo_p3zpoJhfGs9J5g4iFjldypubB6hQedhVayUQu49Nno0KYgKmlhiWQFUcU8xSuQqHKZDbzARIaU_9xUVhW1UjZlyS0eGtRZN80w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b4d07166.mp4?token=MFaFKYY7sX6uHVLT25AsAZ3ukmz3fr6zzKQHA8SIKJ4Q9EjvEjQfX40PFgpm_PaIpWTIHDp1_jwYm3znne7-iNhkMRMTWp3WCWXnevs9FhTk2FoeU0L2b_OpEiZJhqew2NGM7BtOXpr0e-EmVUhWbZUpZWzxWN_KdNSBBuq8w_buPqGH7io0X9ofs4ihiaTkWaDn9bmIJVs50VqBQgBtJo6cNHvhjDdSd347OaQlaZM9FS2mXFo_p3zpoJhfGs9J5g4iFjldypubB6hQedhVayUQu49Nno0KYgKmlhiWQFUcU8xSuQqHKZDbzARIaU_9xUVhW1UjZlyS0eGtRZN80w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
اکرمی‌نیا، سخنگوی ارتش:
اگه پای آمریکا به بخشی از خاک کشور برسه، منطقِ جنگ اینه‌ که اون منطقه رو هم بزنیم و هدف قرار بدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68701" target="_blank">📅 10:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68700">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c2573b8c6.mp4?token=pdK2uDnLueLQpk4dOvdbZoQ3YPbY9YgBucKZlgdIGo9V-_UY-JDmE4qIAmgx_7fisfv10bRVHwuewagfyTkXxL7rEec3t0jHrSV2mUqgjZkKIarkd9Hkug1Uh5-aVl0GCm5-Jmz2Mt7kJHiCW_5u6vjE8FO8o18zwgcxFVCFitNpnmIVw3BRdrA0o22eNGV3WQ1Xq9G5ZYUdQbWM0j_Yeth3f-rNNTIsr5DAKRIJQ4Zl5lj7_zZOXWPHct4Pf8yLxaD8AGOij_RW6UcWknzFwfL6k_AOTBoONUf3EdzTR2S7uQtkMMWF0KkXP6-m_InaM_brZGLaq0rP5EizhZDGqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c2573b8c6.mp4?token=pdK2uDnLueLQpk4dOvdbZoQ3YPbY9YgBucKZlgdIGo9V-_UY-JDmE4qIAmgx_7fisfv10bRVHwuewagfyTkXxL7rEec3t0jHrSV2mUqgjZkKIarkd9Hkug1Uh5-aVl0GCm5-Jmz2Mt7kJHiCW_5u6vjE8FO8o18zwgcxFVCFitNpnmIVw3BRdrA0o22eNGV3WQ1Xq9G5ZYUdQbWM0j_Yeth3f-rNNTIsr5DAKRIJQ4Zl5lj7_zZOXWPHct4Pf8yLxaD8AGOij_RW6UcWknzFwfL6k_AOTBoONUf3EdzTR2S7uQtkMMWF0KkXP6-m_InaM_brZGLaq0rP5EizhZDGqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در سال ۲۰۰۵، نیروی دریایی آمریکا ناو هواپیمابر USS America را هفته‌ها زیر شدیدترین آزمایش‌های انفجاری قرار داد؛ انفجارهایی که حملات اژدر، مین دریایی و آسیب‌های واقعی میدان نبرد را شبیه‌سازی می‌کردند.
هدف یک چیز بود:
فهمیدن اینکه یک ناو هواپیمابر تا کجا مقاومت می‌کند، چگونه آسیب می‌بیند و در نهایت چگونه غرق می‌شود.
این ناو بعد از حدود 4هفته آزمایش با انفجار های کنترل‌شده و بررسی مقاومت سازه در14مه2005 عمدا در اقیانوس اطلس غرق شد.
نتایج این آزمایش بعدها در طراحی و افزایش مقاومت نسل جدید ناوهای هواپیمابر آمریکا به کار گرفته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68700" target="_blank">📅 10:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68699">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9ecf589fd.mp4?token=gWq93rrVMRxYgvx3MeaBmX8NU52xf5nVqzUnwdF92_qBjRkp3k5u44ZcZPWF3eAqZ3WmQWcBf4xYYndrtmu7Ib-NO_o1w0_UdTmzXWZG4O2f5Vn6mGuuoACzdxNfxdkg4Z1xArlHqmxV2zpuH8h3m95gIcR17RGIdAgiByQBfE7hQym7VBEbq07EvaGL87LsgW5mWRK5GidEQ3CXzmRnTcJi8bc7GSqYPlej7_61p3XLlA1LZ_PaxhS2eRfOOIRSo9jZPPANWlwHnkPGKTrMaCgVOciuFxtyPdS3RmQ0mqUaQQ3PpSzzqiJmemrh6ke8zkxQ2ugzMeLg_01bl6dxww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9ecf589fd.mp4?token=gWq93rrVMRxYgvx3MeaBmX8NU52xf5nVqzUnwdF92_qBjRkp3k5u44ZcZPWF3eAqZ3WmQWcBf4xYYndrtmu7Ib-NO_o1w0_UdTmzXWZG4O2f5Vn6mGuuoACzdxNfxdkg4Z1xArlHqmxV2zpuH8h3m95gIcR17RGIdAgiByQBfE7hQym7VBEbq07EvaGL87LsgW5mWRK5GidEQ3CXzmRnTcJi8bc7GSqYPlej7_61p3XLlA1LZ_PaxhS2eRfOOIRSo9jZPPANWlwHnkPGKTrMaCgVOciuFxtyPdS3RmQ0mqUaQQ3PpSzzqiJmemrh6ke8zkxQ2ugzMeLg_01bl6dxww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
موگویی:
تونل رفتی؟یه تونل تهِ پیروزیه ، اون یکی هم بالای دربنده ، فرمانده‌ها توی این دوتا تونل زیاد میرن میان!
🇮🇷
عراقچی :
حالا
کونده‌‌خان
انقدر دقیق نگو شاید دوباره جنگ شد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68699" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68698">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68698" target="_blank">📅 04:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68697">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOIFl4IQAIvAZm5zhH-FHjgpxJXj2-IxKSDbuKsIItbScPFIh2NWM7n7IbhwKMsCA2_vCMavn06Z5iGeIl25V5I1uaiazBxCCOTGN2lRwsd_yxarlX8p4zvATDmuXz9YwoVNDy7sNhyeCJaNv1VgbYunNg-sFhd61LjOrF9IXuycdjvkt8rPCmd8_JQhcRHurb9kWEieuUoXjJdvYvGXBL81LNUtQTGdRmSYA4xDcbRuf6FpjqUalE1vyXlPKEkIxVoJl-qcxY5rRk6A_h5xa3fUgRQgh_lyP6ocQt1SyZ4odcMkSjaGXmQxm0fE9II_ZoxZliC-c97qFFeq_wtGOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68697" target="_blank">📅 04:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68696">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jY0I9TVyGN8a4oLi9gJUdupV8UYe6o0Etu4QLEf5xDN26JCrDfsDMVg1UaphkHSUswiXNsAqf4d5f9cy7fIQwMw8gzS1j04ITSn1WP3rqdofmAHxueeyi4aakwBkMEDgc6t1E7iqBEU5VVJkxKMDbz3hh1vr1njY73xW9zVQLoRYb6m5d5aH7BRihjHV92K7V2VK1muvde8owqbr7YFIepMdiaxC3kk9rLdCoXS8-wMYJDtqcenJkYViZ6p2tzBeNXVyygbWG3Vq4T7f-WJ3YYaRwpta4xH_lUe78rTPx2d_wDCJz-7XpUYusRmKw9kckDLPcubowNJGYyDL_nz6FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68696" target="_blank">📅 02:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68694">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trnaJkQdF1jlFVA2g92rilE_HMptzqwaaGNceQNGBKew0j0NIJS10V_IbdrN5Iwx8_UgKDReBjm194Q1uBVYBdju1zKP6bBMqR5FC3MCtf0WIcfzKaEo6QiywQhwj-RqFJJx8LnSH3hR97Xc419FJea0meMckEPWMC5wOQ3hvYpmvo8SDrAaVkg14bnI-JcpaqmWMcwlJslgndIWIAl7Cb8e0He65sg72R3hvFocXtcMFrKWgUISXQQn_jXGoZjRuzZm6EUMJ07ftVxpYdXDpn4bxH-3Sy6wzXPimuOxpk6p_fhJ05UPHfcc7s6wAsUdgeRvxRHOlAlC2lcfTssJmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ:
"من گفتگوی بسیار خوبی با نخست وزیر جدید بریتانیا، اندی برنهام، داشتم.
ما در مورد موضوعات زیادی از جمله روابط برجسته‌ای که با بریتانیا داشته‌ایم، بحث کردیم.
ما در آینده‌ای نه چندان دور برای موضوعات مورد علاقه مشترک دیدار خواهیم کرد.
نخست وزیر کار بزرگی پیش رو دارد، اما او قادر به انجام آن خواهد بود و البته ایالات متحده آمریکا برای کمک آنجا خواهد بود!
ما در مورد نفت دریای شمال، تجارت، ائتلاف نظامی، مین‌زدایی تنگه هرمز و بسیاری از موضوعات دیگر صحبت کردیم.
تماس تلفنی جالب بود و خیلی خوب پیش رفت. من برای نخست وزیر برنهام آرزوی موفقیت و پیروزی دارم! رئیس جمهور دونالد جی. ترامپ"
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68694" target="_blank">📅 01:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68693">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
پایگاه هوایی بندرعباس رو زدن
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68693" target="_blank">📅 01:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68692">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
دو انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68692" target="_blank">📅 01:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68691">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8Xh95rUms6ia9f8iUKBlkZs3HSX8cVvrEu0qh-dguiANTPH2REMSiIOBD-ffRE5U2vYn7QMLR1qwUd9LQj8Eca5b6llEnb3vcKJyFY0jxt0od_RzvKvChNKw0awEZuoJB2mfuSsChH6-H8ZqfW2UZ-AzkXo2PdkS_o8CaFlSz7Rlon2B-AyBcvpJOImIWLOBI5Xd6OOxNbS-trOEq6ULQgjJY3P1vTASuxwnNRC8dAx02SV-9dnyYpWA_E9lumIdGE-GotAEF8r_f833tnzNFyfjlrrAtmmZ0uAi_7mnQIjBaR4nrYYnIpQ6WXZ9qbGo0ogbbZqXMo_U95c9drhBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سازمان تجارت دریایی بریتانیا (UKMTO):
یک حادثه در ۸ مایل دریایی شمال شرق LIMAH، عمان گزارش شده است. UKMTO گزارش‌های متعددی دریافت کرده است مبنی بر اینکه یک نفتکش از طریق کانال ۱۶ رادیویی VHF اعلام کرده که مورد اصابت یک شیء ناشناس قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68691" target="_blank">📅 01:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68690">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
مجدد انفجار در بندرلنگه
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68690" target="_blank">📅 01:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68686">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aMaqm2MQYN0uCzIu2Km0h-8V3n6hyKuU6bgn_iyuwUfrL8pu-0gbKAWNBH2wUlPnwuy5HG8MY6iQIAecZRTD1IwFeXaLUdG_IWHBZZwmvCC72dATVIAdMTjkEmMBPRVZtO2wZi8Kh-GSuLNYqt-t9M0w_UWY1wkJQb1v0GmZPD0MxPbI9yESqxYCAWT5LnRdnSmIAyUIT7Y5vWXblX7iu91SUPx-2UUKimv1QnIgqhuLCwWEiL9RQOg3sXc88o1tGUxLbsHzUs4v4y1jmFyGqMg9upT9pokeN84trTej3AqXUINTtwFriuahN_bLIgXSzpyYKRj_7Ne8DXX9J6ShSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LKsrQYXGZuxsV_wyk2WkkTC0heEOqU_hK9dh2FYUunHWm5Pg5JCTWi20barYwejlet8asVMrRDVdMrEFM1cMnDPtZPH-Rqj1afZ69lj-EmSZsloWbaIAQbATndTLQlP3pceuwSv-VyJPv6XEa0qLN8tJ9lKSI5UVpihgu_lkafd5xnluX70jfuAI_VboUL3NYK7x4DUuLboZY-TdYGxVu3P1IQlEOLdMXG2cbmqG1ehtNHuufdYmZd7Wx8fCpdZ7VgAUzr_vXGnCxHjL_KP0ZTymmIpn6AkNiksY_EsFktxlCYFjGr8BdRXUB6oa6IwhhdBYHPbHcwQVYApHF2uhUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sUfYsy1psmJ5HXprl63Fur7EW7o33K9tX2zvveVHVg_7ColPEJWhsYIr_192Vm99eOuEJ8QYX-vv7DVywU9EDAqHm7ywr3v3lal2Qgm6kRWOXE_YoTxvDjJ6KIZY6XBGCgrWMVDtO5C8QwBaVfkcmouInGLx3ZTanDyJJYFuHFPhcpjCKblswsTjk2NUfnbIiEl506aSDY9W90hOpsZ7138pHTDfjhgCkIIEtdFVkWxQHZKgr-HjxoJckwlQ3cIYvxA2cSDjHi7_3_lK2cSNLmgj8kcerMorts0L9HNjJvmaW46KZs9hgGOT4psE7fFMewpylGn7wjJ03UyvT5bzpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/myoRN_xwE_gqnvYFYHWbw6IywH6T5lIYk-2ChbHNMtwM39FdFXz2myY8bUyfNwazBVjZMVT94dvo700V8dEz0iuhwZodcJ7ebcvRS_xb3EWRqgI2p9dRqxEvQVV3Hw07GFPZ3C4umrMCDoSXVWJI9StvrRZii5P-4JvuuupXTND4ArH1-anzxfIy0P_MGNTXET-ipo4X9DzgawMtiEiPbXjGp7xA6yxHtde7My4DAFMp_NxrjXIiZSp9sUr4hYRdLf0JXOH54dqO6TwxKgKUW4pE0HtZ3af_iqgMYXDYNN1gSycCZk2GPX5Ggq2ofau2ZvFEbTm9GOeMNPthcOa5Pw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
کوه دراک شیراز زدن
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68686" target="_blank">📅 01:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68685">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6bdf4b6292.mp4?token=RLor8AlYmycncSaVbhJ6-xiVE21-IslB5Y0yUtv6k4C06HyCwmGAOTYju5QJ07mlOVhRJB49pZvXzBbHv8wO6GVr0iep3bp8QxYG6yzsWXD5UGsL8THsHcegcM0EiOBBSWJWpqOu8M1cbRJfs7PNyaUCPofXNmsfKhWaf7s61rh6R0H3A_B-qdCYCMPhIl6I_4sCmUmmX2Qxss_zCW9ExErmsSi0BzwXpx-reTw3FJx_NjJqd55RPOwDy1FckT92x9JfruuyUdIAZaMVNJg97ufSOVgZ6-zj-mfBOkjvo8Tg6K5SkZvUmat8-qhRLv2H92rOZlrhnbpkn5uXO1SsvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6bdf4b6292.mp4?token=RLor8AlYmycncSaVbhJ6-xiVE21-IslB5Y0yUtv6k4C06HyCwmGAOTYju5QJ07mlOVhRJB49pZvXzBbHv8wO6GVr0iep3bp8QxYG6yzsWXD5UGsL8THsHcegcM0EiOBBSWJWpqOu8M1cbRJfs7PNyaUCPofXNmsfKhWaf7s61rh6R0H3A_B-qdCYCMPhIl6I_4sCmUmmX2Qxss_zCW9ExErmsSi0BzwXpx-reTw3FJx_NjJqd55RPOwDy1FckT92x9JfruuyUdIAZaMVNJg97ufSOVgZ6-zj-mfBOkjvo8Tg6K5SkZvUmat8-qhRLv2H92rOZlrhnbpkn5uXO1SsvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فعالیت پدافند در کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68685" target="_blank">📅 00:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68684">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiMAVb2fz1TlJ82kmPOU6hL-SIBxgek1uwk8pGppl43Z_8HVuwbi9FxlfCkIyd3Kgu4ItEozFktOZGxKE27gIs8PwrFa9R321wnWFA5GJ0corUL9gB8ODW7eiionjC9cEMX2SfywOQVXI-N4Tny_XlJMhpFQIwBcIR4pIlBO_kx0tKSftiOm4Beuaa7CTEzTkwZWQ_nDSR4rQKw_rMT_EfFj-rcqtex5vxX3wi6kGhObQRgRYSnOgdDREs0G_2IL6-4kHKyhV_vfu7qIunpfSMyH7XuEsVsrprC_R1PGNDLN9IfJowXIo0RbwX9xQi8bosUiZjd-S5GwlDTQEqvCNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آژیر ها در کویت به صدا درآمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68684" target="_blank">📅 00:54 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
