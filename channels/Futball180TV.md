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
<img src="https://cdn5.telesco.pe/file/n4rxAIpbi3a270GR_k1zoKXdIz3ujaV0dzUoEYW-anVbR6QjJl65uVGEdk6LbzkoLfEbYRdxKFxHUa_IcuhfNVflWoLbLu2rUNyfabDQMPaPRAOI6ej8tNVELaZe7s24YyMwkzUvFBxooNWFCsFQwI4JjhZHYJWlo9G1VnT1HRVDh-G-nLg7xjsizSY_cu7tMcdOpNCE9TropFn59btkKN69_L7eu0HeeXBQOTx3PDlDru8ke-wlr0QfJQh593kYGt_L0LqStJ_mJulKQipr7zTzpkmgIDRAsZo8h8gQ1cSWS8P5ypM9SkSZhhsDWlE0GCu3dgX4tVj4ACtnIaFALw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 390K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 17:18:01</div>
<hr>

<div class="tg-post" id="msg-107925">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2cHJtsOZeYz1cTsBytC4GTRmC-Z0ioPjWdL9wTvWZOm9bMfsux3JJ4o5NRtEyE_VWLHxSdbuG-YAhcGUvlofRRxOOL9jRVd8vp4gcRQAFoEoYsgbsSnj0b4nSAlXmLSDX1jrjZc_ACF7AorKrRt56Uh3kHWJmy43cHjqtrVopxCWzF0DMDOyImXZJpuda06BwhYE9JKTn4p4MfK3CQzTIR-HastPTibfeSDRk1cdp8PF2I86QgiyjfcA7qt6_OsZMEhHkV0EIV4XHF3_L1hyLE5CHezcFsZNAoqNVXTeBIYyvb3slPRHoZ4dQu_uqsmaMDkL-vzqyEBMVDWd9D9bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎤
آندره ویلاش-بواش، رئیس پورتو:
🔻
برای مورینیو واقعا حیفه که بارسلونا تا این حد قدرتمند باشه. درست مثل زمانی که اینتر را ترک کرد ، بارسلونا در بهترین دوران خودش به سر میبره.
🔻
اما این دقیقا همان چالش‌هایه که مورینیو بیشتر از هر چیز دیگری از آن‌ها لذت می‌برد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/Futball180TV/107925" target="_blank">📅 16:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107924">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مهدوی‌کیا: وقتی شکست می‌خورید باید پاسخگو باشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/Futball180TV/107924" target="_blank">📅 16:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107923">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf4e21ea3.mp4?token=rUzSTvASbqA5FdiKVYO8frpcDJmSATsCcb36eUtmYVF6LZB85Bdq_Gh3ebeHYShv3sT_augZ0dJL2TzSGUGC7uYKVQItXknsxOHggsvXSLn3cOzWZ7xDXKvTKwLg2T-iOfjvK7t5z7DhoTReh9b4n2aUJOc4k0wAVZJ6IOrBGIilhj6iEhCAmuzP-_d0IafFtDhuhAbZZhG9drt9aDPzajOQxZIhxneUI7GXHLB6MIT-HTRiXsDqmIlDwangnpJxpPjjQE-PzErvsgyAQDSwjZJ2cnSXB8_UIQIMSKvvMdAEBVy6kDk6VLZEMcr1fFF4sDcAVhqcym7QBPWg4s5BlBdJcFaAnz7H5sOQacP4B8HGim3LXqsm6I-I3My2B2O4tF9vWhpVH37-TpMeZS-l8DPkIlGoz1_QENCZGOWnt9Dpy7RSMxvZJoqs0pUUBZMM4eChfn16VCeTbivdP-O9qIXdXjg-VsQwXjgbTIP3n5alKDkR5AGKiOVwKYYQsYkXZWDTdMV4INIYz2B9891CCJe-gnJJejpefWevO__IvC0-EegnPdqQdFZYxWfXxRoUZ3KNLhAR5x3UzYk6tncfDK-sGM8Z29MJMjpAsoGDpQH4ZSZbEb-vRmJwIhSbg9zHgYklUnje08VzFpjuLxUGeXqpfeTrzZhNWJYc-jH50jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf4e21ea3.mp4?token=rUzSTvASbqA5FdiKVYO8frpcDJmSATsCcb36eUtmYVF6LZB85Bdq_Gh3ebeHYShv3sT_augZ0dJL2TzSGUGC7uYKVQItXknsxOHggsvXSLn3cOzWZ7xDXKvTKwLg2T-iOfjvK7t5z7DhoTReh9b4n2aUJOc4k0wAVZJ6IOrBGIilhj6iEhCAmuzP-_d0IafFtDhuhAbZZhG9drt9aDPzajOQxZIhxneUI7GXHLB6MIT-HTRiXsDqmIlDwangnpJxpPjjQE-PzErvsgyAQDSwjZJ2cnSXB8_UIQIMSKvvMdAEBVy6kDk6VLZEMcr1fFF4sDcAVhqcym7QBPWg4s5BlBdJcFaAnz7H5sOQacP4B8HGim3LXqsm6I-I3My2B2O4tF9vWhpVH37-TpMeZS-l8DPkIlGoz1_QENCZGOWnt9Dpy7RSMxvZJoqs0pUUBZMM4eChfn16VCeTbivdP-O9qIXdXjg-VsQwXjgbTIP3n5alKDkR5AGKiOVwKYYQsYkXZWDTdMV4INIYz2B9891CCJe-gnJJejpefWevO__IvC0-EegnPdqQdFZYxWfXxRoUZ3KNLhAR5x3UzYk6tncfDK-sGM8Z29MJMjpAsoGDpQH4ZSZbEb-vRmJwIhSbg9zHgYklUnje08VzFpjuLxUGeXqpfeTrzZhNWJYc-jH50jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پروژه‌ای که هر روز یک شاهکار تازه رو می‌کند!
قرار بود با عایق‌بندی سکوها مشکل نفوذ رطوبت و آب برطرف شود، اما هنوز هم آب از سقف ورزشگاه آزادی چکه می‌کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/Futball180TV/107923" target="_blank">📅 16:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107922">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4700a47c7a.mp4?token=e82XIz53V7baFY_yuupBGND5IhYXM4PK7NVOmHD2B12pCNq98nIxazKeS59qKzRCyZD3G3Oi8DjDOiDVM9tRZ97TmlzuPEe9jLh-q_9VKAbe7kwIOPCX0hH4-31BXac-MwO82O2h6fbg95q37dpozoCTKUtsOmKXU2eL-iAMhjyJncyKuXG85vSBWrZjvnkQwcoJ6Se9Ee56Xr1_h02mB6083-vE90NynAk8Rm_maCmajcbrMJrWaPinHd-ICy_tn8s61fj0merI9mg17ncwHuq46qv8KQ5ik9QEmYReBgMrYTbBMuddnd_8WJ6mZOJgQDCXnXZXtQ50zclDMKwYRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4700a47c7a.mp4?token=e82XIz53V7baFY_yuupBGND5IhYXM4PK7NVOmHD2B12pCNq98nIxazKeS59qKzRCyZD3G3Oi8DjDOiDVM9tRZ97TmlzuPEe9jLh-q_9VKAbe7kwIOPCX0hH4-31BXac-MwO82O2h6fbg95q37dpozoCTKUtsOmKXU2eL-iAMhjyJncyKuXG85vSBWrZjvnkQwcoJ6Se9Ee56Xr1_h02mB6083-vE90NynAk8Rm_maCmajcbrMJrWaPinHd-ICy_tn8s61fj0merI9mg17ncwHuq46qv8KQ5ik9QEmYReBgMrYTbBMuddnd_8WJ6mZOJgQDCXnXZXtQ50zclDMKwYRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🎙
✔️
صحبت‌های جالب یاسر‌آسانی پیرامون فرهاد مجیدی اسطوره باشگاه‌استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/Futball180TV/107922" target="_blank">📅 15:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107921">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27cad11c0b.mp4?token=q1FptjrgZVUsoEcQJdbmLru3qHIAIFHv2-_7gFy_ElrGEP6Bp3eNmYD-iSTEIQ2tx_jxeWbLXc7LsSSxJ5KHfrAS14GglhzxxJq3trc6QP6S7_TSXfgthUmq10CxcVwuwdMOcnrzO_eQlMpTk-t0fiOnfTtrtV14sY0SndJ5P20uoYBt3ICrM2wNAJ_TbVAD5ByjlHuskUk8ycZkhDw97AhtvJmeepPL8PW1PR2DLdeDly9i5IsqRFFEw8oRnnXwDbo549PJUMtd7dBEbn9V8Y8TRaiWicBAjNhuJmYw6CpPwIess8GMgj_jaMwUe6i3I4Vz3oMHIakI1XYsB6ZFXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27cad11c0b.mp4?token=q1FptjrgZVUsoEcQJdbmLru3qHIAIFHv2-_7gFy_ElrGEP6Bp3eNmYD-iSTEIQ2tx_jxeWbLXc7LsSSxJ5KHfrAS14GglhzxxJq3trc6QP6S7_TSXfgthUmq10CxcVwuwdMOcnrzO_eQlMpTk-t0fiOnfTtrtV14sY0SndJ5P20uoYBt3ICrM2wNAJ_TbVAD5ByjlHuskUk8ycZkhDw97AhtvJmeepPL8PW1PR2DLdeDly9i5IsqRFFEw8oRnnXwDbo549PJUMtd7dBEbn9V8Y8TRaiWicBAjNhuJmYw6CpPwIess8GMgj_jaMwUe6i3I4Vz3oMHIakI1XYsB6ZFXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
پشیمانی بزرگ رجب‌زاده؛ باید به پرسپولیس یا استقلال می‌رفتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/Futball180TV/107921" target="_blank">📅 15:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107920">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f6fed1c3.mp4?token=WJ6Fp5yKa9w6MbDrEWOrYEEy3PrQ1zzQO-ndtXt8ATOvK4zm-SfHbSIGG3AGk5tuk42eezl5TI2As4GV0oVCdiURPBh_ws_C-pN2Ksa638y3upBhFMX7p9LQ-i3v3rKTlnJoHZMU198iUXNGqNXJJZA6M04RI_RSEa6tSOMtL326iu33zIh4DR1fICXFfkCiNr1CVkqZE7sm1DPRoZDTXifOMUSq3PwgfwnXIZ45iNgvhdxvHk7RlwWTUnwVGFpu5QVT_AxE4UEuubCBxWu3Nv7E0xaPbpzw4JxStif0jzX5DhKjuMwklSwiBI3YbpHbzMnUKRDhAUTh5GnB36knYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f6fed1c3.mp4?token=WJ6Fp5yKa9w6MbDrEWOrYEEy3PrQ1zzQO-ndtXt8ATOvK4zm-SfHbSIGG3AGk5tuk42eezl5TI2As4GV0oVCdiURPBh_ws_C-pN2Ksa638y3upBhFMX7p9LQ-i3v3rKTlnJoHZMU198iUXNGqNXJJZA6M04RI_RSEa6tSOMtL326iu33zIh4DR1fICXFfkCiNr1CVkqZE7sm1DPRoZDTXifOMUSq3PwgfwnXIZ45iNgvhdxvHk7RlwWTUnwVGFpu5QVT_AxE4UEuubCBxWu3Nv7E0xaPbpzw4JxStif0jzX5DhKjuMwklSwiBI3YbpHbzMnUKRDhAUTh5GnB36knYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر قلعه‌نویی سال ۱۴۰۰ در برابر قلعه‌نویی سال ۱۴۰۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/Futball180TV/107920" target="_blank">📅 14:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107919">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dw_Ng7pqnLLpmQMJIlyqtYlX6L9ujJj26cAVjeEaMkDS7AsUJrS11MAa0JRiz6GY-2AKRykHa_4uBdFmlMazU6aKp14xbRm8n-WYH9UIjQFTG3pbedzhiQo4nRfNuSNSyD5Bdu1ROdw2vdJHx3rB4wvAVGS1wqUheSgokYzdy-lP4ZFN-9sbiKeDrCo8bxuF2yFfJ2oSdLypACCsiLB2LUtPX2xQ9mDrd_VsvmXX4Wswtok-b7PHNo4jck8rrrijs8Rea0A6wq2albp1w2BdjqSNUasSHamTut26RUX31tlheL3UcZ6TF31bZ2HZ1tCHG8OjhtDtwLBFNyzhKlzMHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
🙂
رسانه‌های برزیلی با انتشار این تصویر معتقدن که وینیسیوس به قتل رسیده و بدلش داره برای رئال‌مادرید و برزیل بازی میکنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/107919" target="_blank">📅 14:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107918">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0504ebd98.mp4?token=T1E8yikv0ey1vs-kCdBab5OtltsteXFdwD76mcQci_S7cRqedazIumf0elakMzgaoPmP6usT1Fa4krs5R5-VfSQLGD11lNYPsnbUHbJELnUuGF7r085_mywvCckZztn34f-Tiag9DMt7hM7GgjLFKHsVp25eYStRTspGsjNln0S3VULExQdb0LpYAqPGeTTm8lVVUg9EGj9Sgtq46nd4OiULB7UM09p6-rrjJswss2m8WLXwIO3Px7n72YYyVmB7XEJD8anV0yob9hFD1abHMzNdyLif8n-mLuUfEDsc_9H8NzGZ-8m3bqczcDOq3QnTxLA85Mlby2wOCddVjpvyTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0504ebd98.mp4?token=T1E8yikv0ey1vs-kCdBab5OtltsteXFdwD76mcQci_S7cRqedazIumf0elakMzgaoPmP6usT1Fa4krs5R5-VfSQLGD11lNYPsnbUHbJELnUuGF7r085_mywvCckZztn34f-Tiag9DMt7hM7GgjLFKHsVp25eYStRTspGsjNln0S3VULExQdb0LpYAqPGeTTm8lVVUg9EGj9Sgtq46nd4OiULB7UM09p6-rrjJswss2m8WLXwIO3Px7n72YYyVmB7XEJD8anV0yob9hFD1abHMzNdyLif8n-mLuUfEDsc_9H8NzGZ-8m3bqczcDOq3QnTxLA85Mlby2wOCddVjpvyTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
فتح‌الله‌زاده: از استقلال که بیرون آمدم برای مدیریت پرسپولیس هم پیشنهاد داشتم/ تاجرنیا نه مدیرعامل میشه نه میذاره کس دیگه‌ای بیاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/107918" target="_blank">📅 14:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107917">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8beb00264c.mp4?token=pnwKxvS8WDX17znnM5-YIeSdQaCu_4bs26BTPNz5aPHv2-Yn3BEVdJv_H8qFMfyeG3c8wCI2-jDbCdFCtlqyk63-bRYIGPlMvtcLo7jBHvqtIpZ_DOW3zEPRGzd33NP3ZBH2TQOBOpXJp1FnDjtrkge8qFyqgDRbHirAtUk-3oKDRNrAGMWbO9zHGbdRqHVKdx7QOdw5EdGQ9xgpIQ-Pjcyr5-PDSuefk-8xUj9Fj29s1fYgKVLQfvTCV4YTVcqfyidmrWXoqMxZVwnC59ndOV4WUV8ZXk6ycIAg1BqAuD25_yyMbHhItbqjisbYE9M9nq6bC8Qz3Io_WmTeqLePlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8beb00264c.mp4?token=pnwKxvS8WDX17znnM5-YIeSdQaCu_4bs26BTPNz5aPHv2-Yn3BEVdJv_H8qFMfyeG3c8wCI2-jDbCdFCtlqyk63-bRYIGPlMvtcLo7jBHvqtIpZ_DOW3zEPRGzd33NP3ZBH2TQOBOpXJp1FnDjtrkge8qFyqgDRbHirAtUk-3oKDRNrAGMWbO9zHGbdRqHVKdx7QOdw5EdGQ9xgpIQ-Pjcyr5-PDSuefk-8xUj9Fj29s1fYgKVLQfvTCV4YTVcqfyidmrWXoqMxZVwnC59ndOV4WUV8ZXk6ycIAg1BqAuD25_yyMbHhItbqjisbYE9M9nq6bC8Qz3Io_WmTeqLePlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
▶️
👍
تسسترون خالص!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/107917" target="_blank">📅 13:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107916">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اعتراف جدید کلثوم: آمار دقیق افرادی که به قتل رسوندم، ۱۱ نفره. یک نفر هم پیش‌از کشته شدن متوجه میشه و نمیذاره اینکارو انجام بدم
😐
⚽️
Channel: @futball180tv</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/107916" target="_blank">📅 13:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107915">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8324686f63.mp4?token=hOzo-Tu1pp-WCiRNFcyNLUDug4aI-ICbi_zNgMTCPMT5c8rRLiOiGHrdWVGmLrxx3T-TWffWGRwr4EjgMhN8spj8XjKzhMy5obsA-r6L3pe91TrJpv8gzd9jUZfOOtuzR8VShABDXHsCN2wd3t84fbWXqdcNUbCSee7GCMFrZP_k1anEtUiGAMhyUO_k5tyip1Goo_xviHrIqBbrldmdqQYr70-ye0Mtie3kLW8jUkruoslW5MjxyZHxhsEn_ASaMoV-B-Om20TL48aSvHqNuy1OgEhH-fHYjtESv7BtsYl1S0snTnm7SSXJMZC2cPsy_GiBTn93yYuHZVNn_WzoMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8324686f63.mp4?token=hOzo-Tu1pp-WCiRNFcyNLUDug4aI-ICbi_zNgMTCPMT5c8rRLiOiGHrdWVGmLrxx3T-TWffWGRwr4EjgMhN8spj8XjKzhMy5obsA-r6L3pe91TrJpv8gzd9jUZfOOtuzR8VShABDXHsCN2wd3t84fbWXqdcNUbCSee7GCMFrZP_k1anEtUiGAMhyUO_k5tyip1Goo_xviHrIqBbrldmdqQYr70-ye0Mtie3kLW8jUkruoslW5MjxyZHxhsEn_ASaMoV-B-Om20TL48aSvHqNuy1OgEhH-fHYjtESv7BtsYl1S0snTnm7SSXJMZC2cPsy_GiBTn93yYuHZVNn_WzoMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
دیس سنگین ابوطالب به هادی چوپان!
هانی رامبد بهت برنامه نمیده؟ خب تو نیازی نداری به برنامه بزرگ‌تر از این نمیشی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/107915" target="_blank">📅 13:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107914">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05980d89a2.mp4?token=n_EZCrFOLaETF6qRgeixXOEnTu5WYyMEoq1i7hZ8r8pbr4PN4X4rF8CWHIMZlnCW0uyRHcyFbQt4d7tcjHtnjqCiuTQj1kQJZaEY3uIyve0CjYvOXXxZv0I3wEf9Z7pW3yFDx4HswQxCq3und72qudmmSdRBtPG1os4Ojbgv8gWabNxyNFzT9PNsUhfC0_RYgohe7lrKqYnJCj2lqxDX9L-jETVjvjPXEI7FaVhL3Zvonk4s0uSKHT3sSqqq7TcY5TIUS1edyDuD-H2z0CDkGYKOnUgTBTZvPUoS_-Er1EVnJ5P3HJD0J3IwqH1kvkMz_m4a_Vzp_KbacOezRyPsjKohLYmwPT3UfvodUwFIutlWf1CVgi1SkqwMDgOUSJ4y2Ar2qgKDPYPkNna2vYAjDH6nNriuj-a6SvjNvqh9dlld2_teuVrpwE3BvY352zbmkjglOLeXvdK1KnVgyl-7niOkejT4-vZjCT2w9OzoXbfMgVZZgHRr5X2ttGSP7qguo-_kc9Cv2NQGeHuS_ABMBWz1T1c6xZi_p44B0qn8Va3tsASzj5iSwZzXIIev_uE8hI8NV7agVOpryd9I2ogQDLmQ4B5s4p3gU6aXpebMk3eqP6mfloVKlgU51oHPn1PbcFrfeg0eqV0vsV3xOaTzdEkqXYy93X527iIlYPvaJ28" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05980d89a2.mp4?token=n_EZCrFOLaETF6qRgeixXOEnTu5WYyMEoq1i7hZ8r8pbr4PN4X4rF8CWHIMZlnCW0uyRHcyFbQt4d7tcjHtnjqCiuTQj1kQJZaEY3uIyve0CjYvOXXxZv0I3wEf9Z7pW3yFDx4HswQxCq3und72qudmmSdRBtPG1os4Ojbgv8gWabNxyNFzT9PNsUhfC0_RYgohe7lrKqYnJCj2lqxDX9L-jETVjvjPXEI7FaVhL3Zvonk4s0uSKHT3sSqqq7TcY5TIUS1edyDuD-H2z0CDkGYKOnUgTBTZvPUoS_-Er1EVnJ5P3HJD0J3IwqH1kvkMz_m4a_Vzp_KbacOezRyPsjKohLYmwPT3UfvodUwFIutlWf1CVgi1SkqwMDgOUSJ4y2Ar2qgKDPYPkNna2vYAjDH6nNriuj-a6SvjNvqh9dlld2_teuVrpwE3BvY352zbmkjglOLeXvdK1KnVgyl-7niOkejT4-vZjCT2w9OzoXbfMgVZZgHRr5X2ttGSP7qguo-_kc9Cv2NQGeHuS_ABMBWz1T1c6xZi_p44B0qn8Va3tsASzj5iSwZzXIIev_uE8hI8NV7agVOpryd9I2ogQDLmQ4B5s4p3gU6aXpebMk3eqP6mfloVKlgU51oHPn1PbcFrfeg0eqV0vsV3xOaTzdEkqXYy93X527iIlYPvaJ28" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🐐
حالا محکم بشینید؛ این دور آخره …
چهارشنبه؛ ۲:۳۰ صبح - پایان ۲۱ سال سرمستی در لباس آرژانتین؛ رقص آخر، قدم‌های آخر، قرار آخر
🎬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/107914" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107913">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-Tf39QShKdgvZB7QbIEfDJGgvwDk-UwVbQP1RmJWdHhYUqmqOqeC60ekl_XbS-ppJFFNn7QS6513mCh--tVDv_wcnRdG6r7lJxo18ZHxhu6HaLYtTKeXJRY7exoS9dytOFRKaREaH3PJzYzk-wr2Lqu9EXZxmxHprcSUN40-39P9AYHs9J8ltqwKDc4l1eccU01P-9mEWK0Iq58AsZLSI4PcIZYEC2tIufScS8PrPXx2tnpOyY488p5XPEe3ll5sWINXyRbzyI5Cn8C9t4fQSwjzTqiDSZ99Ex8iQY0KfPVykQDoUkxGc8Rifv8MdtdMH1ZYfdRNmXOFFv2DHFVuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
👤
۱۰ رکورد اسطوره مسی، با تیم ملی آرژانتین:
1️⃣
بیشترین حضور در فینال‌ها: ۱۱ فینال در رقابت‌های قاره‌ای و جام جهانی.
2️⃣
پرافتخارترین بازیکن آرژانتین: ۴ عنوان قهرمانی با تیم ملی بزرگسالان.
3️⃣
طولانی‌ترین حضور متوالی در تیم ملی: ۲۱ سال.
4️⃣
بیشترین بازی ملی: ۲۰۷ بازی.
5️⃣
بیشترین پیروزی با پیراهن آرژانتین: ۱۳۴ برد.
6️⃣
بیشترین بازی با بازوبند کاپیتانی: ۱۴۷ بازی.
7️⃣
بهترین گلزن تاریخ تیم ملی: ۱۲۵ گل ملی
8️⃣
حضور در ۶ دوره جام جهانی و گلزنی در ۵ دوره از آن‌ها.
9️⃣
حضور در ۶ دوره جام جهانی و ۳ فینال؛ تنها بازیکن تاریخ که به این رکورد رسیده.
🔟
اسطوره جام جهانی: رکورد بیشترین بازی (۳۴) و بیشترین پاس گل (۱۳) و بیشترین تاثیر مستقیم روی گل در تاریخ جام جهانی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/107913" target="_blank">📅 12:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107912">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e79f527d7d.mp4?token=fo7OGBEhZBJDrCyVAqAVFl7wzsteRkNfqn8ByowohI_G51AI5S0u-Xih2LE_QdlZNqCAmF2rxzqDIOinXFrjmDDbGRtWXND4UqMykjJdmqMUYUs5Dzf7GTrociyQLjn_bEY6fjq3iZtUz7MhOu9S3PfsMyT1p6kYop85GyplGLWOqXG2IaL7LEFmcTVIS5boAeaZQgRPjNQJ8EAAJ1q4NZQg5fertMtlvbeLf4KUwtJKfgQmK4omjIz25AHTtsWMWmpCGNm3iJ3pdSC2mkghcHt_tdgZVKCZLo28CkxT7Er8JcudtNwZ9wrcUhC5SznyFF6rKKaXgAQeAFQgERq3cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e79f527d7d.mp4?token=fo7OGBEhZBJDrCyVAqAVFl7wzsteRkNfqn8ByowohI_G51AI5S0u-Xih2LE_QdlZNqCAmF2rxzqDIOinXFrjmDDbGRtWXND4UqMykjJdmqMUYUs5Dzf7GTrociyQLjn_bEY6fjq3iZtUz7MhOu9S3PfsMyT1p6kYop85GyplGLWOqXG2IaL7LEFmcTVIS5boAeaZQgRPjNQJ8EAAJ1q4NZQg5fertMtlvbeLf4KUwtJKfgQmK4omjIz25AHTtsWMWmpCGNm3iJ3pdSC2mkghcHt_tdgZVKCZLo28CkxT7Er8JcudtNwZ9wrcUhC5SznyFF6rKKaXgAQeAFQgERq3cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇹
ولی این رسمش نبود ...
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/107912" target="_blank">📅 12:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107911">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f83cf644f9.mp4?token=nXboGkXzTqqq7ZZP4JrSG9DwqPpDXgPXB7XZccRYnprKnHQ--dPnwCFDLsDOejShIclOCXbkB4DRTZJi5V_EWpRdgwLGWjCAbgmw1RT1H-nS2iLGq6bDLqCEU1w7F09W2Dmfh8N2zDZ1MUf22sO8o1tQ0sUDguADrSPc8dGm2IoZIOi1m_KQ0IL9cBPZ5Q5za_4yYuZtHdBlUa5HdVoJ7fX8-T0V3Ygy3RVoWhPSl7Pfpj_bnoPPcut_x-gtJZ_ELkB90uVBL1qaajecbH2H-dH00KiJ5DM4HXtxbGeIYxjGuOZf5TVi9TBEC3lesaGE8jU2zpYjVimcZSFPb4mz4BF59jXOiAkAmphJ07QZBm-etElV5kvrNOquho5mVIWHtVCwmtrfRgQbZEVPgxQyHCoiyDZaON6RMbHR-UL-QS8u6p3WE9kvqfKXmRZiTgpJ23nH7siGud_gPbDpWT42gTPUhk25Q-qYXqQeWsvUvfUX9mAp8OQ13aq3sYEwidoniw8-qWgMy0GAkNYDrog5a6Jdr5kxvy9z6yWc-VbIJ6boKQ7v9Y8gbViSNCfMPTJqgGAm2hA6ragqoEHD7svFNml2USSvXs9rZRusDZyOKEIrug29fis9PIiZhOo7mfTHIK3reqpNctHflIhbwWt_4R8OEYIVLZbyeCXewvK_fVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f83cf644f9.mp4?token=nXboGkXzTqqq7ZZP4JrSG9DwqPpDXgPXB7XZccRYnprKnHQ--dPnwCFDLsDOejShIclOCXbkB4DRTZJi5V_EWpRdgwLGWjCAbgmw1RT1H-nS2iLGq6bDLqCEU1w7F09W2Dmfh8N2zDZ1MUf22sO8o1tQ0sUDguADrSPc8dGm2IoZIOi1m_KQ0IL9cBPZ5Q5za_4yYuZtHdBlUa5HdVoJ7fX8-T0V3Ygy3RVoWhPSl7Pfpj_bnoPPcut_x-gtJZ_ELkB90uVBL1qaajecbH2H-dH00KiJ5DM4HXtxbGeIYxjGuOZf5TVi9TBEC3lesaGE8jU2zpYjVimcZSFPb4mz4BF59jXOiAkAmphJ07QZBm-etElV5kvrNOquho5mVIWHtVCwmtrfRgQbZEVPgxQyHCoiyDZaON6RMbHR-UL-QS8u6p3WE9kvqfKXmRZiTgpJ23nH7siGud_gPbDpWT42gTPUhk25Q-qYXqQeWsvUvfUX9mAp8OQ13aq3sYEwidoniw8-qWgMy0GAkNYDrog5a6Jdr5kxvy9z6yWc-VbIJ6boKQ7v9Y8gbViSNCfMPTJqgGAm2hA6ragqoEHD7svFNml2USSvXs9rZRusDZyOKEIrug29fis9PIiZhOo7mfTHIK3reqpNctHflIhbwWt_4R8OEYIVLZbyeCXewvK_fVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
آخرین پیش‌بینی خوش‌چشم، کارشناس صداوسیما، از تاریخ وقوع جنگ بعدی ایران و آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/107911" target="_blank">📅 11:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107910">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pM9UVWhD63VyGhP5bi49aiD4MOL7NhgGnI5cpyWz03RjXKH33rk1TUHxkoZOpUiQ3uhdPwTd63PgZ-cBR67NmbsoU7nWEffPbZLIFgDMJfv0bDMq1_FlM_gakcAjddcDxvcpDzefmn_YINQjsyCDWPBwGPbSgWaiWYT0FUxoE-pq5FK7NHWKYk-tbHufUd0xSJwEA8JW6RXL6HRDLAK-2XZRMJDRAH0WqaTa3HN2XK54k1sxibZEaWSbkJoBSi64Q2nEw3_zijT6arrImTUkCpuVu9cQ8XuEWIsb55McPbukWkRkQHRe2IE2Zd5rJLxDsyGFRuveMScLyaPCCP0-BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
✅
مصدومیت حبیب فرعباسی سنگربان استقلال جدی نیست و این بازیکن به دیدار روز ۱۶ مهر مقابل تراکتور تبریز خواهد رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/107910" target="_blank">📅 11:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107909">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/477e1b7cf7.mp4?token=PjiXNfa2AFy8uslS1qTRi44FdoYMlRRCnexP0dMS2IkH_U7UdCOwfPJyHDR_eEi-PB-6SFxe-kGf3GMNj1DUTquCvQ412pHjUTOB8lka-63H6zVZkL021wwzhtP6CJLpirZSrqDvy41PlM3FBZkQTBJEevYNHSoD7lJ-m6u7fJPdeftI80UtHkZEGUJcXg16GX_hagA067kKfEwPH05cQi3SugsbF7DhnmM2gYgXaZP7SVsYfZjORPC2Y6Nyau40TzzbN_EPR9Ekvpzw79igD5OL3p7ZXVxe4lNqIHeYZG_S7ukHktC9XFwYIc-4V-FnC1yrVyfem87kd-8fht1EoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/477e1b7cf7.mp4?token=PjiXNfa2AFy8uslS1qTRi44FdoYMlRRCnexP0dMS2IkH_U7UdCOwfPJyHDR_eEi-PB-6SFxe-kGf3GMNj1DUTquCvQ412pHjUTOB8lka-63H6zVZkL021wwzhtP6CJLpirZSrqDvy41PlM3FBZkQTBJEevYNHSoD7lJ-m6u7fJPdeftI80UtHkZEGUJcXg16GX_hagA067kKfEwPH05cQi3SugsbF7DhnmM2gYgXaZP7SVsYfZjORPC2Y6Nyau40TzzbN_EPR9Ekvpzw79igD5OL3p7ZXVxe4lNqIHeYZG_S7ukHktC9XFwYIc-4V-FnC1yrVyfem87kd-8fht1EoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⁉️
ادامه‌دهنده مطمئن برای راه پدر؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/107909" target="_blank">📅 11:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107908">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eeed962e7.mp4?token=VGS3XCtTIDq4QLKgBF89xjXu7gSH1vWv82_nqs7aF9t8vvdACNR9Npvy_eKMXyezyE3PqhBijqSZRbb-fX9MeoT1NqVGo-6nkM69bYdUyPL1G1e0x5GqaXC_QoZOYvoaU8Tv25SkBRQAOXvMFJTdq2iuMhr1DrHa_nHnsywVdOpzHHUvhakXDygqJfuDB6Oym6KvpMWDgrXSww-Z0HlcKUa3wOUnJ73VCQN87Mx52inU3U_4ixIw7rE4HgMwgPsB4o4wc427sTykGcpkFKhPaZ8ig2fJhFZiWUuUoISgvO63zcrQfH4AWGHfxk9cFRE6s-2ZtHnW3iG8EjUdspn-9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eeed962e7.mp4?token=VGS3XCtTIDq4QLKgBF89xjXu7gSH1vWv82_nqs7aF9t8vvdACNR9Npvy_eKMXyezyE3PqhBijqSZRbb-fX9MeoT1NqVGo-6nkM69bYdUyPL1G1e0x5GqaXC_QoZOYvoaU8Tv25SkBRQAOXvMFJTdq2iuMhr1DrHa_nHnsywVdOpzHHUvhakXDygqJfuDB6Oym6KvpMWDgrXSww-Z0HlcKUa3wOUnJ73VCQN87Mx52inU3U_4ixIw7rE4HgMwgPsB4o4wc427sTykGcpkFKhPaZ8ig2fJhFZiWUuUoISgvO63zcrQfH4AWGHfxk9cFRE6s-2ZtHnW3iG8EjUdspn-9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
تعجب علی‌ضیا از تغییرات باورنکردنی دختر بهداد سلیمی؛ تو ده سالگی هم قد خودش شده!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/107908" target="_blank">📅 11:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107907">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107907" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/107907" target="_blank">📅 11:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107906">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VN726xGy9XJB9TccY9hmR6MyjrbzT8otAyqWn81xEDPbG44YOBzMsl1nkgcpL9wC4dLmJTmk83vSMBZ7Cjru2TUXFFKB8BKeQP0SrzQhdyxH-f3LE3Pxl6whzVDq7EJx9PuAV0bqB4wn0fVLkwUxa6OIsaSih_yFh433hIcbZ4ks8iFZBDunvirnpT7jLTtyrROAPlP7U7Gx7Dr3DKu1FNzSX2G5DF34ulr00TJpq1rl2vSFuYbWGpHtxstfA9t2oTm6LGMeSPeUetBd_wlChnqX3IOAJMmR-39TlQ941bTPHggiILefBVVJyei7ZCADNCQMIqQEL4E7T03HeZRkng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
اسپانیا
🆚
کرواسی
چک
🆚
انگلیس
اسلوونی
🆚
اسکاتلند
مقدونیه شمالی
🆚
سوئیس
ازبکستان
🆚
کره‌ جنوبی
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
https://TrexBet.com</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/107906" target="_blank">📅 11:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107905">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/906a8b3b0f.mp4?token=n5wameh9fzDvwm8NkAmHKWWso6pNKRwC18LttVNCi_KyTq37xF1mujAWIcCokCD0MWWAVJCDH39K_oNGBWKev2QTSrGx_h46kpkwORYe0HqoCMrAgnNY_nWtssN-6uH8pFoMofAkQcij6x8hmh5lBkqWo47jzQIlngbtmFe5ShzOib2gChgnh-26Ndr5efCuJm1dfb8ASVcsgqn8_zRmdcWrPS53gOQM4mW6RBoA7zX9XZKndLuJFXTFmXQRfMM5HSCgRQU8HoBIzRSjrhx2l86mL6Z9KqWoEKXIB0-1tez-OPshAkidzJ7KZ-0g3PyuaUr785JVM6UAx4YLmTs4rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/906a8b3b0f.mp4?token=n5wameh9fzDvwm8NkAmHKWWso6pNKRwC18LttVNCi_KyTq37xF1mujAWIcCokCD0MWWAVJCDH39K_oNGBWKev2QTSrGx_h46kpkwORYe0HqoCMrAgnNY_nWtssN-6uH8pFoMofAkQcij6x8hmh5lBkqWo47jzQIlngbtmFe5ShzOib2gChgnh-26Ndr5efCuJm1dfb8ASVcsgqn8_zRmdcWrPS53gOQM4mW6RBoA7zX9XZKndLuJFXTFmXQRfMM5HSCgRQU8HoBIzRSjrhx2l86mL6Z9KqWoEKXIB0-1tez-OPshAkidzJ7KZ-0g3PyuaUr785JVM6UAx4YLmTs4rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
محاسبه افت قیمت خودرو :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/107905" target="_blank">📅 11:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107904">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BT8nldbMS4_vfVVJjII5dcoxEqi2L1QtR_E8-TJ4xy_jxxohbPdgg_Es3KI8V0PZxqJGHMm9oWnDhH6HtsT6JthFTkZ2lJOR_KIkl4HYpvJGbSh19hWiSk4u7KROpQro8tNjmsDQYqh-olbzhDzihuB30X5LM3i461Wnl-UaV319XakC10XmVayx5mBGfneEV29VqLhDRbStNxHTjAUN74lmpXddoMn8ehCZMgCTW7TFSNOGfZiyoSoRyvJjDvPFSo8smtGIa2N_R6K1R0RejUBvO9-DFWkfXGO20E_uMXkWcjVT_nCZl6fLqxvg2-OhJo8U-XhF4O6sRqLKjhHy0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
بیشترین تاثیر‌گذاری روی گل‌ها در این‌فصل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/107904" target="_blank">📅 10:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107903">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXw7-dEawiG8ChC8jIF8_ucO4nKuC3XuvehHGp4rBTWgGq4F-OrYaRfpXZw-nsJOK98sYgdZfvy31oCkjDoEUKV53HlV1bU7TWLky-90AT5hUfsV4LEcKFZGuuXif12lbLwLkNY6ekqCd5-UlmBc5OlRawAOPkGLNQTztzQH3CE7h-ZUZBz68LH_pJ8bwebcfkQPv5ezy_3-kyniDGs-ihogqH_mag9vaRTW94Cf61YwuTDhhEm7eP25NeaRrPM3NKYer-gV89-fctq1b4rafliMqSKVNm1uWNVOu_-zeuLFgbtAADVO5OrNrEs7--CKaprBXZ-RNA5UCs5dAYBgBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
#فوری
؛ رومانو: قرارداد رافینیا با بارسلونا تا ژوئن سال 2030 تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/107903" target="_blank">📅 10:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107902">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQ2mBzcnz0S_7QwueEzm-fJppzxZJdLSr08y7XNjI9xUn_CTFRpSQ0MBwQy-CJ1puYX6CyOOXBZcnTPcEkK4F5by60l19oQ-XAHEpSr1cb08MzJBXH3bvEa7vMYYqyeXzHsfz8IyhTxKvXLu0WqlK0UY2mULVRUjfw8Tw1K3Q5xpucxIjpuARuGSWDbU-DG6enBVQyrUqtN-aDKZ4IhT4R3yQIsyvWGUqd-LzT9DxFvyqcEYWgUzoSoihxf7XGwsnrwJqc6ni1qddOxx0zSnj9Z0Tmi-hc7EMs1VRzxHBaWCyo-V2n7cQ3P_RREJl8e51ceDtItuBsyDFads2Au1kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
معرفی داوران دیدارهای هفته ۸ لیگ برتر
🔸
🔸
تراکتور - استقلال؛ داور وسط: سیدوحید کاظمی، داور VAR: امیر عرب‌براقی
🔸
🔸
پرسپولیس - صنعت‌نفت آبادان؛ داور وسط: احمد محمدی، داور VAR: میثم حیدری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/107902" target="_blank">📅 10:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107901">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff702b8d86.mp4?token=h6IyTZyFCpBtFndmbiH3mOBc4kcVmU_FfDUw7q430DpNkvVh0dITl8LjdTcLdxu9wzHTzhhplfeIPKJLjOquAP80GpkW0l7lJoM1h_1PxqPnOiVS1MgmY4N9_O0nON-3oZ8KAc38rR9Pnkg7Edr_8l_fyXC2SF4I1-FstfkJwEh_UWmvKYvJD8TKWrmbUJUmjeLgJp3xWJzip6YXRlEwvG5XM_QeeHIbnP8F_C8gmofXm8ce7X-D_Tk01wp_Zq7TsnithB_7bTG4Sx7W_BeNobAZEmyoHNEArG0K52Al6VdpTs9QFmIi046QP6bf7SRpcgseXWxoEKasRGwcRrmejX_yfXDdp-TND5JogzibVpEwfhMO9Me4O0X-lqRIbbvCEaZC7xsZIaDHPmQSqMZm5I8uG_BoTPPkI7S2M7OvPb4_vOmNzIO2CqraMd-b1mXbPrZXmncSk9TEXvAuKZ095HAPpAyYWI87cErl_U7SMoENOSt2GRnaMCIAxDteHsAZuNyYZIoP3pvFaSDD0FJgismNwa9WXmLBnSjcWvECG4m-4p0H4apaE9MdgjhHbyW9oDvejENXJOrwFn9ibAluUnd-B-53NyMogmuTR6plVVYMw_787ZVhKHWuuI9OuFe5HCwz4LsHAiQBefHvH8Hkl_tzm-LBKOaaIopIwH6v6pk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff702b8d86.mp4?token=h6IyTZyFCpBtFndmbiH3mOBc4kcVmU_FfDUw7q430DpNkvVh0dITl8LjdTcLdxu9wzHTzhhplfeIPKJLjOquAP80GpkW0l7lJoM1h_1PxqPnOiVS1MgmY4N9_O0nON-3oZ8KAc38rR9Pnkg7Edr_8l_fyXC2SF4I1-FstfkJwEh_UWmvKYvJD8TKWrmbUJUmjeLgJp3xWJzip6YXRlEwvG5XM_QeeHIbnP8F_C8gmofXm8ce7X-D_Tk01wp_Zq7TsnithB_7bTG4Sx7W_BeNobAZEmyoHNEArG0K52Al6VdpTs9QFmIi046QP6bf7SRpcgseXWxoEKasRGwcRrmejX_yfXDdp-TND5JogzibVpEwfhMO9Me4O0X-lqRIbbvCEaZC7xsZIaDHPmQSqMZm5I8uG_BoTPPkI7S2M7OvPb4_vOmNzIO2CqraMd-b1mXbPrZXmncSk9TEXvAuKZ095HAPpAyYWI87cErl_U7SMoENOSt2GRnaMCIAxDteHsAZuNyYZIoP3pvFaSDD0FJgismNwa9WXmLBnSjcWvECG4m-4p0H4apaE9MdgjhHbyW9oDvejENXJOrwFn9ibAluUnd-B-53NyMogmuTR6plVVYMw_787ZVhKHWuuI9OuFe5HCwz4LsHAiQBefHvH8Hkl_tzm-LBKOaaIopIwH6v6pk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇮🇹
آنالیز بسیار جذاب از تقابل تاکتیکی ایتالیا و فرانسه در فیفادی اخیر با هدایت زیدان و مانچینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/107901" target="_blank">📅 10:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107900">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02c435695d.mp4?token=PMlvyyTPtyHZurgcR8uYC4yeqiudOs91pP0nxZuziqU0Oa7zTz4OFBpbp11ww-cjWW4Q2KgbBCbGVB0kEUXAxyzXIOnCoSbRkAFV4TA-b6y8lbejyoTlIEQYcSgEooTCLUzyyiqCmGSuH53HeIA2miV57lrAXE5qTzCGwpEKy1vjVuDDiKYBVA-qXkMZrlP-Ce6jS0QN5ByiWTaSh25NV68X8zcfskJTMjqTfNSnVP4aErF9oH6JTc2tfCOw-JfYQUgJkPFzPJtiBUvhmf5GqjdZ7_rsl0YME-K9tQSrzuTIcnsC8qiwSqxOLoerlFMPEufwYvR0qKNMDBD6RVK3dLNObOrVlMXYlHz615kquDK0BwCpKYAUEihi4muxevO8HnkGt8tjDdGspPA-hEXc1VoOTPYvHnJb5AKm0z8RkdmsAVDJe-p8CfRnsWFvjBNgoGIrXtIDPwLk3JaclewURtROoJWnWNt-eVygg99a4yIMVjidl9Vy0BCKBN87GdQQxSXKI6unr2Tjc6ET-T4GQPpj_88MykFKe2jCQsyplvAOTdV6JuwW-ZrE0DGw2NZLpPRHjl68hDFMmsJJKRX_14hhPMDTGGFoQVhlPmPM9TzISVd5EEaxTO7WoTrv0NuhRRL0XgtrRaacx7n19IQJVmp0QqnEEVKrLTa09VPBKeM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02c435695d.mp4?token=PMlvyyTPtyHZurgcR8uYC4yeqiudOs91pP0nxZuziqU0Oa7zTz4OFBpbp11ww-cjWW4Q2KgbBCbGVB0kEUXAxyzXIOnCoSbRkAFV4TA-b6y8lbejyoTlIEQYcSgEooTCLUzyyiqCmGSuH53HeIA2miV57lrAXE5qTzCGwpEKy1vjVuDDiKYBVA-qXkMZrlP-Ce6jS0QN5ByiWTaSh25NV68X8zcfskJTMjqTfNSnVP4aErF9oH6JTc2tfCOw-JfYQUgJkPFzPJtiBUvhmf5GqjdZ7_rsl0YME-K9tQSrzuTIcnsC8qiwSqxOLoerlFMPEufwYvR0qKNMDBD6RVK3dLNObOrVlMXYlHz615kquDK0BwCpKYAUEihi4muxevO8HnkGt8tjDdGspPA-hEXc1VoOTPYvHnJb5AKm0z8RkdmsAVDJe-p8CfRnsWFvjBNgoGIrXtIDPwLk3JaclewURtROoJWnWNt-eVygg99a4yIMVjidl9Vy0BCKBN87GdQQxSXKI6unr2Tjc6ET-T4GQPpj_88MykFKe2jCQsyplvAOTdV6JuwW-ZrE0DGw2NZLpPRHjl68hDFMmsJJKRX_14hhPMDTGGFoQVhlPmPM9TzISVd5EEaxTO7WoTrv0NuhRRL0XgtrRaacx7n19IQJVmp0QqnEEVKrLTa09VPBKeM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تضاد قابل توجه صحبت‌های مورینیو در مصاحبه اخیر خود با رفتار دیروز کیلیان امباپه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/107900" target="_blank">📅 09:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107899">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6256aac96.mp4?token=CgEmKc-gt3MGVGe-EmkN9TWYHT1xga1TFfV-Akgv87CQK2y9Zr3abTTD-PkJhkPSJYQe3Ik8gVfmToWNY0-L-1awIFeyO1FwugivfJ5_Ok7IkMsRl_WP88B2cOhk4Sd0kJtEhc9QrSXxwknoUDCEpUuqIvVkrjF1TCdV3spmoYosos3-Y3jmoGHbtYD00PNKq8z6O1OzWfR_brLt176pGJCdhJ8FFPxRFzHBvK1zYW3rk7W4tHPgfMSnUwo6MPVp6EdslfrooiRke-G0Oass6-IpMMmjV9ZwkgmGhqCWjLwDKdS92ZDRZb-Smm-5g2xMMjSd-py9e-bnVb1Qbz0PqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6256aac96.mp4?token=CgEmKc-gt3MGVGe-EmkN9TWYHT1xga1TFfV-Akgv87CQK2y9Zr3abTTD-PkJhkPSJYQe3Ik8gVfmToWNY0-L-1awIFeyO1FwugivfJ5_Ok7IkMsRl_WP88B2cOhk4Sd0kJtEhc9QrSXxwknoUDCEpUuqIvVkrjF1TCdV3spmoYosos3-Y3jmoGHbtYD00PNKq8z6O1OzWfR_brLt176pGJCdhJ8FFPxRFzHBvK1zYW3rk7W4tHPgfMSnUwo6MPVp6EdslfrooiRke-G0Oass6-IpMMmjV9ZwkgmGhqCWjLwDKdS92ZDRZb-Smm-5g2xMMjSd-py9e-bnVb1Qbz0PqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
پرتغال بدون حضور رونالدو همچنان می‌برد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/107899" target="_blank">📅 09:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107898">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/522303d3e9.mp4?token=ujeTc3m7zZa4wqUGmQEhQrfg5GCSjSRoZ8_r4G_ZAj9AW3sbEN8qzfVxe0iafCxLixiN-6Q1m2sAo4lYs-rh4j_2pLMZ5X07ciygS3nXj0dnPvQ0vCvJ7kblZXWTs8vq_zz_lpSDaDGntVcXyjsu537-FV05yZS6o_oXLiwmctWRdRv5aAzIjjD04ZrGZBLNsA7e1_cvn_HF-m0nHk8MIng2Kb8ESQVwHS__Jmt8YkFXbQ2gIPGPSWDCMF-iZB7Mpft5ANjF5K3vCIU0N6XtEIHGuNciVoCiNdKVQY9cc_mRk_YnRY2yBdKpDZ001PR3uU33Q7_mIN8uN2lMcOHOXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/522303d3e9.mp4?token=ujeTc3m7zZa4wqUGmQEhQrfg5GCSjSRoZ8_r4G_ZAj9AW3sbEN8qzfVxe0iafCxLixiN-6Q1m2sAo4lYs-rh4j_2pLMZ5X07ciygS3nXj0dnPvQ0vCvJ7kblZXWTs8vq_zz_lpSDaDGntVcXyjsu537-FV05yZS6o_oXLiwmctWRdRv5aAzIjjD04ZrGZBLNsA7e1_cvn_HF-m0nHk8MIng2Kb8ESQVwHS__Jmt8YkFXbQ2gIPGPSWDCMF-iZB7Mpft5ANjF5K3vCIU0N6XtEIHGuNciVoCiNdKVQY9cc_mRk_YnRY2yBdKpDZ001PR3uU33Q7_mIN8uN2lMcOHOXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
تماس‌ژوله با آناهیتا درگاهی عمه مهاجم تیم‌ملی وسط برنامش؛ بهش میگه فوتبال ما عمه‌ای شده
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/107898" target="_blank">📅 09:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107897">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25bf4f2e86.mp4?token=BM27WSmj_iyI7yybEg88Q0Y2iJELs6Tj0HDDoGqpI5tTNsMHigUcjRz_m6O7_P3gKjagoYcSBTQP0_xkMHayPXt9XOq0pFu7p7S2EGJbyONB4iOOQwBGplpEaukuXw9SkPLubuAULdWT_5Rv7CX0C30weMrIDAdNKdEUUkCAXlEIr4JDljpZcCSaTO89n0FNFgh-ytE_9WGKfv6Vjk8memJz8lNB6yNzmH5drIiFvetEUwR94DE5fzO7xT-Z3kvt1W96o8GVRSzu74zld1KJUctyX8wX_wWyikFglAq6tlA2qjTTOtb3gnkQcGjdNIsR7hnT4PKunBez17lod12_5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25bf4f2e86.mp4?token=BM27WSmj_iyI7yybEg88Q0Y2iJELs6Tj0HDDoGqpI5tTNsMHigUcjRz_m6O7_P3gKjagoYcSBTQP0_xkMHayPXt9XOq0pFu7p7S2EGJbyONB4iOOQwBGplpEaukuXw9SkPLubuAULdWT_5Rv7CX0C30weMrIDAdNKdEUUkCAXlEIr4JDljpZcCSaTO89n0FNFgh-ytE_9WGKfv6Vjk8memJz8lNB6yNzmH5drIiFvetEUwR94DE5fzO7xT-Z3kvt1W96o8GVRSzu74zld1KJUctyX8wX_wWyikFglAq6tlA2qjTTOtb3gnkQcGjdNIsR7hnT4PKunBez17lod12_5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
حجت کریمی توهین کرد، علی خطیر تهدید؛ کریمی: تو دلالی، خطیر: دادگاه می بینمت!
❌
درگیری شدید دو عضو هیات رییسه پیش چشم سخنگوی فدراسیون فوتبال در برنامه زنده تلویزیونی...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107897" target="_blank">📅 08:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107896">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4798a06f34.mp4?token=vu9dNXQiVmfqZv5jroLotiAiwzhEzpACwcVTb-0k-fpjUHWOjM3t2lXAb_q27kRshZo0eeR33N4gXXBAEXhq7t9QrJAVbSMJZViuxUtT6k4G_7qOanxBM4B5KMqt-3KQHX2OvzEgB8s-89ahdPjmxL2gOo4rTbGNuCiE0dQRsZz5JmkZDPf4SOKAvXPRMPSpYx-PUCVKdhDEsBXmYShiJkMkLlOxiTcWQEuWmzv8-gOCjFwUMGINka42yEZsEiQSPkT3DxlRDLrqzbb6CmdrYdlM-mvMGmGiw00DulAbVZ5v9ja9oQSvWW-RYZmK3eOueAqlYvBL3Iw7a580hlTFMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4798a06f34.mp4?token=vu9dNXQiVmfqZv5jroLotiAiwzhEzpACwcVTb-0k-fpjUHWOjM3t2lXAb_q27kRshZo0eeR33N4gXXBAEXhq7t9QrJAVbSMJZViuxUtT6k4G_7qOanxBM4B5KMqt-3KQHX2OvzEgB8s-89ahdPjmxL2gOo4rTbGNuCiE0dQRsZz5JmkZDPf4SOKAvXPRMPSpYx-PUCVKdhDEsBXmYShiJkMkLlOxiTcWQEuWmzv8-gOCjFwUMGINka42yEZsEiQSPkT3DxlRDLrqzbb6CmdrYdlM-mvMGmGiw00DulAbVZ5v9ja9oQSvWW-RYZmK3eOueAqlYvBL3Iw7a580hlTFMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
خطیر: اگر آقای گل‌محمدی قبول کنند من همین فردا کل هیئت رئیسه را متقاعد خواهم کرد
خطیر: هیچ مربی ایرانی با ماهی 500 میلیون تومان سرمربی تیم ملی امید نمی شود! کمترین دستمزد مربی در ایران 70 میلیار است کدام مربی سرمربیگری تیم امید را قبول می کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/107896" target="_blank">📅 08:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107895">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107895" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107895" target="_blank">📅 01:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107894">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwX-JNmSqlWItURMzCM03reFTp8zdM-Z3RMZm3JuRGCCZzg1I_n0WV98EDE9XUM45LSTiPealPd_2uHM_fx3-rCYH47V6ATlo1K-F7X8C_r-1RKoY1WMHCWnLx49R2Dr8NEb8P3HDojXFAIegoxde3Xdi2JH9sgldaCBrmhd1UUGezB26tdKznAc_8rO58Up4MRXTdHDcm4mpoTLedJ1Gegby3z3E5duTgGrtcH7JtTwk9xgYUj1gpBF7XJ7mj5V03t8OZIB7roojdWDJ6il1c81GLGp76HkShGyFcRSK6R-Bq-d4ZzmvWjtpwGKHKX13YANiJthrK4i_2UAEistQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107894" target="_blank">📅 01:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107893">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107893" target="_blank">📅 01:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107892">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3867ed322d.mp4?token=rTS-PA0lAbZtxj_1CNlkUt3fxMxO-uXOxXEQWnDFmzRJ-9C-Nkl7qvaZgnJ87AqQAYOEPUHnJVGRTLuyh1jFy1_Hcm6a3p9jQrbSDZIrpcfJDEjguET41s0fdoHd5AxphosYzZlJI_NQ87Kt_eUJJyNMmuUVOW2G4rFUlwOtWLx8wLvvg39CDFS8OhWOnsdmKZvac-C9vRVPbyxU5t7S9H1KhBexp8RAEbUI4cOI7DJoA7dIXrVJc7_v4oBys5sIy8LDa6RDgILC6hjO4iaChM4SbdjmnhAPrZPiZbzo1t1IpkumhkqADkTxhGXV4eDyTP_5uNuIsG5i5vseK6fJ7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3867ed322d.mp4?token=rTS-PA0lAbZtxj_1CNlkUt3fxMxO-uXOxXEQWnDFmzRJ-9C-Nkl7qvaZgnJ87AqQAYOEPUHnJVGRTLuyh1jFy1_Hcm6a3p9jQrbSDZIrpcfJDEjguET41s0fdoHd5AxphosYzZlJI_NQ87Kt_eUJJyNMmuUVOW2G4rFUlwOtWLx8wLvvg39CDFS8OhWOnsdmKZvac-C9vRVPbyxU5t7S9H1KhBexp8RAEbUI4cOI7DJoA7dIXrVJc7_v4oBys5sIy8LDa6RDgILC6hjO4iaChM4SbdjmnhAPrZPiZbzo1t1IpkumhkqADkTxhGXV4eDyTP_5uNuIsG5i5vseK6fJ7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
لحظاتی رمانتیک و شبه هندی در شبکه سه
روبوسی های واعظ آشتیانی و علی خطیر در پخش زنده
😂
پی نوشت: گفتنی‌ست در لحظاتی از این برنامه واعظ آشتیانی و علی خطیر با یکدیگر درگیری های لفظی داشتند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107892" target="_blank">📅 00:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107890">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DA2_TcVh-61UP4cIUWpTIAC-keAgFJ_TBbRdbayX1XHGGa0k94spVT9WDl3UDdU-OOnb5KvBYY2N_23HQRn0FF8060hmwrg4tg35vdkVUYix9YfHyIKnrqE2r6usohuWIwtdSKtR0q2Ntaj5T08y60u2h0MykDg-57N_ADwrUgNWClf4kaeGekWqX-QTU_cDbcS07QtgAvwGpjZwtAQbELj_MHRLzOzHjThWSqnsaforuRFpN6ZYyUhZRiLsi1iMHup5GxwAiOuKuW41Q2uBxbLKB6IQ5XRRIjSrzusmaS3oFzQP3rSBLLInPR_2uES8vYfXAiOJT0qTslJWkdxOgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U4ap1yhleLVGXQ9uUkidsIdweikdzNSAEUyV5CmVVllLg1AjA9RPUc7A7hbxPqEmRlGi119MXofYxt3h5HCCl-7UjfDwY12jifllwT2nF-IxWGWAhoe1AneqzZO-_ZUiJ9dBjv-Yw9W9GpmWd2QzF3rILkaFiFHjtcloJODXw2lz0HQTdaq_uEZIYAz4uvrHtsdiOsBf7htBqJXSy7fYFNW0o2CwSxIzkpUGvX1WUZuZ7rwYrMFhmbBDVPy9vJr5xGn9x-AJl9ROrrtZhVrlgubHwW6r_F5Vp_5W6QDvgtrNNdnUL7mY0dnuU4OyFaEJp9tI7RjGV8Lj3W8TptbBjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
‼️
ترامپ: نمی‌تونیم جلوی شیوع طاعون از روسیه رو بگیریم!  این ویروس بسیار کشنده و خطرناک‌تر از قبل شده و مثل یه ارتش شدن! حتی با پیشرفت چشمگیر پزشکی هم نمیشه جلوشو گرفت، با این حال ما به روسیه کمک میکنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107890" target="_blank">📅 00:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107889">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7gjzl6XiwoHfqx4yWaaLnvltGBzQBE9zieu6EqSXNFRkZJedtLGnY5LKwFO3DmHCpSyzoMVs1Mril9R8DPOoqE4b5mJSM_TJ0DlgKDHNIUfddKXynjkwWu5oej8gz7hvLh-P21NdlCwQBAPXcbzGIMDVVQdvNeN-aUr38c_DbAtB9DbAryy-OFKL8Dzb_X2MFw4v4CkT4pHObfZ-D3UwKP0ayAUAo_KsoZl875k_A22xJ4lIDTNuDOZBWzkvWUGBSU_p1wRb-HjP15MPnyk7g4ekdimJhd56R6Z089LIQ06R61Gxc4gsHqnD_an1fsxgkknQBUN-BVcrowZIs9akg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
✔️
لیگ‌ملت‌های اروپا؛ ایتالیا رفت و برگشت مقابل ترکیه پیروز شد؛ تیم مانچینی سرحال نشان می‌دهد!
🇮🇹
ایتالیا
3️⃣
-
1️⃣
ترکیه
🇹🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107889" target="_blank">📅 00:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107888">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3c5cdf08.mp4?token=UaVnv1t33bObEJ2Emdk7oyzaXOOMg7F533hfb9iOiolQ4zpyUBcs-mqtYJ3Pr8e9zuPfI-1DwZsJ6LjeZbJQP0QvTx4Wc_6CLRRqJMPxb4GwaQGE6xHYEYBtpo7gEpQhpt9ftpmX_5GQO_QSO5TBoT_tFGJt8U0z9stZa1kGZLwKieGTId1SOsQI6ZlzW4Yj8PvlX7Dy938nrnZjw2VZvPIAYhAoyCjNBIEhi4weyxIbLmXpvk_PeCSXXXvEBVR2ofldBSoSKNOplJNFrQp_EowfqQPASKdGeZqFqDzbv7-V6TCahA-XiuFHrTeFKRDQwhGZxqeYEEgTkS3IWfqxD4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3c5cdf08.mp4?token=UaVnv1t33bObEJ2Emdk7oyzaXOOMg7F533hfb9iOiolQ4zpyUBcs-mqtYJ3Pr8e9zuPfI-1DwZsJ6LjeZbJQP0QvTx4Wc_6CLRRqJMPxb4GwaQGE6xHYEYBtpo7gEpQhpt9ftpmX_5GQO_QSO5TBoT_tFGJt8U0z9stZa1kGZLwKieGTId1SOsQI6ZlzW4Yj8PvlX7Dy938nrnZjw2VZvPIAYhAoyCjNBIEhi4weyxIbLmXpvk_PeCSXXXvEBVR2ofldBSoSKNOplJNFrQp_EowfqQPASKdGeZqFqDzbv7-V6TCahA-XiuFHrTeFKRDQwhGZxqeYEEgTkS3IWfqxD4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
درگیری لفظی واعظ آشتیانی و علی خطیر روی آنتن زنده
🔹
آشتیانی: من فکر می کردم نفرات اول و دوم فدراسیون برای پاسخگویی حضور دارند
🔻
خطیر: من هم انتظار داشتم با نفری صحبت کنم به مسائل روز فوتبال دنیا آگاه باشد
🔹
آشتیانی: همه آقای خطیر را به عنوان ایجنت می شناسند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107888" target="_blank">📅 00:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107887">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff62591c17.mp4?token=aGN4iEz8qESQi_ZgpH6tki6PJFTXxCb6JP8UX3IYO8n8eQndxFZ50eGoPUY69pxPV_8OQjMrL0yiOlmElC6ADaW0bK6LbWGjzFUgqU58Lxgaz2xWcw8w3zkyMUZqKQjGozdP-VKZlES0bATVmZzOtWD93El3zwPRGZ31yqSkgmaKxjVb1vhJacwfvpKVInjOV_NsIEOHVs6LgKjnHnwI2dqNkuP81tfH6w0VryNeX8yuQi8-v703ol9XMtduLiuUEXxKcLm-Tzv7B7AWG5zgx6MwEULdwzty6NJ9E65R8Zl62WyZjNiNkkkM0jvTpFTFhVXyOaOV_a0ReY4CCVYuKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff62591c17.mp4?token=aGN4iEz8qESQi_ZgpH6tki6PJFTXxCb6JP8UX3IYO8n8eQndxFZ50eGoPUY69pxPV_8OQjMrL0yiOlmElC6ADaW0bK6LbWGjzFUgqU58Lxgaz2xWcw8w3zkyMUZqKQjGozdP-VKZlES0bATVmZzOtWD93El3zwPRGZ31yqSkgmaKxjVb1vhJacwfvpKVInjOV_NsIEOHVs6LgKjnHnwI2dqNkuP81tfH6w0VryNeX8yuQi8-v703ol9XMtduLiuUEXxKcLm-Tzv7B7AWG5zgx6MwEULdwzty6NJ9E65R8Zl62WyZjNiNkkkM0jvTpFTFhVXyOaOV_a0ReY4CCVYuKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🚨
‼️
میثاقی
: فیفادی واسه تیم ملی ایران بعد از بازی دوم تموم شد، درحالیکه ژاپن همین امروز بازی داشت و خیلی از تیمای جهان 4 تا بازی انجام دادن. قرار بود تیم ملی با گینه بیسائو بازی کنه، دیدن تیمه 3 تا به نیجریه زده، بازی رو کنسل کردن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107887" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107886">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WywV-WEJW33r2J3F6xhtmRWz8NCT_EK16fAb8KFTPH_H5Qg1HaD2JycHjI89p-tiw4zt6bZD7-NSIt30USCealOJDYAPJWa9Kh2XBNiVZf1n6G6g-oPPSyOHcb1ev0SXbumqyGa8mytZ35AZtqBbDBqsewr2p-unnU-2Qxr5700Psijou-GiIH2-QySD305toutBsE2vamFKtkEyndN1CzqsViTKlHYia4d9ukxXMdypyBGizHrAy7qRw1IWqEiyUTBI03HP_Vu1-APmXsr6NtLGQwf_u52su9e0Wl5YSCd0xEqfL-VHdZi4zWhy8mBBDEYQJxC9CdPLHLTM-M81wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇪🇺
لیگ‌ملت‌های اروپا؛ زیدان نیازی به امباپه نداشت؛ اولیسه و چرکی ستاره‌های خروس‌ها شدند
🇫🇷
فرانسه
4️⃣
-
1️⃣
بلژیک
🇧🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107886" target="_blank">📅 00:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107885">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZJwGVq8OvyqlHJUStYuDL-DpREOmAjF4XGQIquzhaL-hXh5hVHqSEi25CJQvC7I5Y-g-xK6KD4ZIX6XWjhO7CfoHxiCmkjRqc2noJ86oNSTzDy9tG-NkmnqgBtENe2ce1NpPW6xvzV3kc7s7wuOp7jvxPYRjcoiA9k12xNsW0bwhtj-1NiJnhUqFclTvmiXQMpCmgiK1KjPiMTKb-J3S8RfR_4ToMRjVVKRTMmYU_nIyJjK4aDJ4K29NqlORpQqhXMnitGmJ10mF_jUfeYydvB1swyvW0q1wSzfuE9rHf4Ff1TBHAuavPDDZx0_ue6Ga6w-apo-UYGrdIrYIaibcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇪🇺
لیگ‌ملت‌های اروپا؛ زیدان نیازی به امباپه نداشت؛ اولیسه و چرکی ستاره‌های خروس‌ها شدند
🇫🇷
فرانسه
4️⃣
-
1️⃣
بلژیک
🇧🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107885" target="_blank">📅 00:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107884">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tra_vJ-vL2E9EF2hsgdPznU9rSE640xrSVMya9s0es0Lcl9ssof5VivFbQJxu67CVidbdYmFe0CE1VtSIdDfBGLVTmdBHG9Og-buUEe-IOTceRDhwQq1uSIaFv0Q5IvW839E8rS-FOS5hMp8TkfK-XjXVh83gN9M4L2YZijs-VxFQO3rfL3NBdDRBznGPhsESabAUxg0_8LYsST_GDRjsEPEMoelWyPhO_y1ndg7cybbECPnCLKNlfC8rrLj90778cc8n_WME9l3XHbVLCKp9kC2H2Xm15N2gY6Z3LsHlifCcr7NJThQcza_QqZ2O7UD0xNsJrT5sWXJRHQIuLqcew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
✔️
لیگ‌ملت‌های اروپا؛ ایتالیا رفت و برگشت مقابل ترکیه پیروز شد؛ تیم مانچینی سرحال نشان می‌دهد!
🇮🇹
ایتالیا
3️⃣
-
1️⃣
ترکیه
🇹🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107884" target="_blank">📅 00:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107883">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25f8a10c9e.mp4?token=B11xSgLavZXr4Y1RrL6SEXDKfziAtbzPKNaKlHyjOCoKyZt_tZ2LvoeAnYLEiNdYQjSMRtYuWEaX34iseXbp_yPDZq3aNG_yOC97lBy833wyuae6E5wJ4A2005zJkdrBj5YPfNawGNe9bwnYWqxrQpvyJRBP5Y5DD8ALAwLm2-DUfbOkUIfunMIvzN7I8Lk4D7r0JtTjQf9JcjUEu5WIWgzR0_xrDCscO6miD6zmG7dT7n-TtC5ACSaqssk5LfxuLG9Lz6TLKmxCTeA0UjPwJ1Em_kl1nVXoSX65jTVCGnyBc7QhdK5l2YJ8XzMXye8WJm58Jc3UH8-iKxH6Y5yS7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25f8a10c9e.mp4?token=B11xSgLavZXr4Y1RrL6SEXDKfziAtbzPKNaKlHyjOCoKyZt_tZ2LvoeAnYLEiNdYQjSMRtYuWEaX34iseXbp_yPDZq3aNG_yOC97lBy833wyuae6E5wJ4A2005zJkdrBj5YPfNawGNe9bwnYWqxrQpvyJRBP5Y5DD8ALAwLm2-DUfbOkUIfunMIvzN7I8Lk4D7r0JtTjQf9JcjUEu5WIWgzR0_xrDCscO6miD6zmG7dT7n-TtC5ACSaqssk5LfxuLG9Lz6TLKmxCTeA0UjPwJ1Em_kl1nVXoSX65jTVCGnyBc7QhdK5l2YJ8XzMXye8WJm58Jc3UH8-iKxH6Y5yS7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ترامپ: نمی‌تونیم جلوی شیوع طاعون از روسیه رو بگیریم!
این ویروس بسیار کشنده و خطرناک‌تر از قبل شده و مثل یه ارتش شدن!
حتی با پیشرفت چشمگیر پزشکی هم نمیشه جلوشو گرفت، با این حال ما به روسیه کمک میکنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107883" target="_blank">📅 00:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107882">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01bb309807.mp4?token=RRllumQrhebaAjfWapq2Dk6TUAcVnVQgj9cRrhSdxBczp8qv6oIct4ggoBMa2-6aNJ4O1kkGgjiYhfu7i7Ugch3ybQEE_bhG4Im4b1oa8qJpzobUwjsAyx-tSVcMXLbAomhaPt4ijgT22sKaq9eBE3ilLz08fjP3Q8suF70XR_ZcbN5EkOMg-XmJUCl--jRQubJMIOt5yZ-vgQIIBc67D1EWTmiR0Ze4doqDKCMKZiVeK-WiE1rbDWyJ8pUntVTdCGLuSirtIXv0_F8UrTJewJgb38PQrz_iwkgbvfZ6Xoc02GDWt-RrlaaQTXPr-122rlo3-P2tf8Y_s3VRSoHSog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01bb309807.mp4?token=RRllumQrhebaAjfWapq2Dk6TUAcVnVQgj9cRrhSdxBczp8qv6oIct4ggoBMa2-6aNJ4O1kkGgjiYhfu7i7Ugch3ybQEE_bhG4Im4b1oa8qJpzobUwjsAyx-tSVcMXLbAomhaPt4ijgT22sKaq9eBE3ilLz08fjP3Q8suF70XR_ZcbN5EkOMg-XmJUCl--jRQubJMIOt5yZ-vgQIIBc67D1EWTmiR0Ze4doqDKCMKZiVeK-WiE1rbDWyJ8pUntVTdCGLuSirtIXv0_F8UrTJewJgb38PQrz_iwkgbvfZ6Xoc02GDWt-RrlaaQTXPr-122rlo3-P2tf8Y_s3VRSoHSog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
خاطره امیرمحمد رزاقی‌نیا از هم‌اتاقی بودن با رامین رضاییان: سنش را بگویم ناراحت می‌شود ولی مثل یک جوان 24 ساله تمرین می‌کند و در دویدن باهم کل‌کل داشتیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107882" target="_blank">📅 23:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107881">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4d63f949c.mp4?token=NazhgcjfXkvU5cLHJ9gJaGAb-1Ff7EF9XiDHHvqmjExxiExM_H3PidTzZVLy4PVITS8kvMOIpSiAQo70kMGjcOmo3auRm_qf4mJPhWdPpxOD6O0WifCr0oUPNAGiuOw3D48n0wImXJu7kunG9KxpAMoDCJUgArE03kCnnVV-Vq1vkYB3iNlbVLhuzfTL1_0A3T2-9mdaYuFxJ2GUvxfpNmjztQu4tnQ1Senyo6a_IDnXhb8P4x8zA0eoZ8AuHpqqg2-6g3VfIhGAcDttAhlQMVNqNCADILvmlLjqt6cBrdKRUPK-lz4JzDG7L0miYssLpL3r72RXSulZJNlV06av8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4d63f949c.mp4?token=NazhgcjfXkvU5cLHJ9gJaGAb-1Ff7EF9XiDHHvqmjExxiExM_H3PidTzZVLy4PVITS8kvMOIpSiAQo70kMGjcOmo3auRm_qf4mJPhWdPpxOD6O0WifCr0oUPNAGiuOw3D48n0wImXJu7kunG9KxpAMoDCJUgArE03kCnnVV-Vq1vkYB3iNlbVLhuzfTL1_0A3T2-9mdaYuFxJ2GUvxfpNmjztQu4tnQ1Senyo6a_IDnXhb8P4x8zA0eoZ8AuHpqqg2-6g3VfIhGAcDttAhlQMVNqNCADILvmlLjqt6cBrdKRUPK-lz4JzDG7L0miYssLpL3r72RXSulZJNlV06av8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
سنگین ترین پرونده مهریه ایران اعلام شد:
اقای جراح ۶۳۶۰ سکه مهریه برای خانم با وفاش زده بوده و الانم تو زندانه
+ تا چند نسل قبل و بعدش هم جمع بشن نمیتونن اینو پرداخت کنن
😕
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/107881" target="_blank">📅 22:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107880">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
‼️
🇮🇷
بعد از پیمان حدادی، موبایل همراه مهدی تارتار سرمربی پرسپولیس پس از تمرین امروز سرخپوشان به سرقت رفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/107880" target="_blank">📅 22:18 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107879">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1743ee1f5a.mp4?token=O2E3tnn701r5kInk7SA7OBrPBdBaoFnSeJHMa5dYsJ2IV1aGxpQK8zJiOgLYNbl9WCHLFzqQ0j8q6gvM8OYgf149wz6MSOtuW_saSRLBPeUTqYgIVla8okrRK2fYMUNipGDIumvYbV1nGzYlDvU_wCgtY2TyujYks5vR6cTk3-g5bhETdjdHWg5yEkLRcXT4BSerH1mYWktjS2sNkW6n4kwdGOn7SoLz-CvCWfdLLJ_EQNrFvYBSf2CUgHZDx8nKo-IlK0eRwd42fnauGtcAwvG9JdGem1b4MnYFPsQNiNQVaVI_8-iq6LOv4xyhb0UEShZJjU-yRfjaKhUJ8-hmkFUmAhOS9FPUVaFTnxMKOJu28gI_yHtoVlHS-lf35S8uel_0Eo6-YknEZUlv5HbRIHvbIVtHDbaC9fwpW20-q7flCG99qNQqC9HNTNnoaGApBAGjePzScijyWutMxTjJN2geXhupv_8S8swStnLzx3CK1Hvr85IgKhlhR54UluBCgyZdULoB79vNsP_HXGeGoG0EmOqGVg-dTkgKvplcfoaSFYOELwnUyWI1ZCahDNF1O1BfgzUzWdAjM8bP2EAogfNEZDDXUhaMTwcwgP2h0pFQurXZg77_J0cGOOVfBylXBxL8GhJtUUgKj-NdbVzfMpMmE_zENOzqHh0ZxLXXprU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1743ee1f5a.mp4?token=O2E3tnn701r5kInk7SA7OBrPBdBaoFnSeJHMa5dYsJ2IV1aGxpQK8zJiOgLYNbl9WCHLFzqQ0j8q6gvM8OYgf149wz6MSOtuW_saSRLBPeUTqYgIVla8okrRK2fYMUNipGDIumvYbV1nGzYlDvU_wCgtY2TyujYks5vR6cTk3-g5bhETdjdHWg5yEkLRcXT4BSerH1mYWktjS2sNkW6n4kwdGOn7SoLz-CvCWfdLLJ_EQNrFvYBSf2CUgHZDx8nKo-IlK0eRwd42fnauGtcAwvG9JdGem1b4MnYFPsQNiNQVaVI_8-iq6LOv4xyhb0UEShZJjU-yRfjaKhUJ8-hmkFUmAhOS9FPUVaFTnxMKOJu28gI_yHtoVlHS-lf35S8uel_0Eo6-YknEZUlv5HbRIHvbIVtHDbaC9fwpW20-q7flCG99qNQqC9HNTNnoaGApBAGjePzScijyWutMxTjJN2geXhupv_8S8swStnLzx3CK1Hvr85IgKhlhR54UluBCgyZdULoB79vNsP_HXGeGoG0EmOqGVg-dTkgKvplcfoaSFYOELwnUyWI1ZCahDNF1O1BfgzUzWdAjM8bP2EAogfNEZDDXUhaMTwcwgP2h0pFQurXZg77_J0cGOOVfBylXBxL8GhJtUUgKj-NdbVzfMpMmE_zENOzqHh0ZxLXXprU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚽️
کلید واژه‌های تکراری قلعه‌نویی؛
همه مقصرند جز ژنرال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/107879" target="_blank">📅 21:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107878">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
‼️
💵
عادل فردوسی‌پور: دیگر حوصله شوخی‌کردن با قیمت دلار را هم نداریم
روزگار سخت و تلخی که سپری می‌کنیم/ شروع فصل لیگ برتر، با دلار ۱۸۷ هزار تومانی، بازگشتش از فیفادی، با دلار ۲۷۰ هزار تومانی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/107878" target="_blank">📅 21:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107877">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc2122fb81.mp4?token=NbR-NU4RKx8pRMW8ABlLF5kq6IjOYJp5Awbj0WTz1u0imGmKFtQ21MDonIsac-ADH6TSeCmZDVvAP-qvgovf6XrTKKXg-QLVoSd0l-8LqICR4Iig4Ljgw83trJKMxaulK0NDWUZIzi2p1BEPAJK9m4UhKlaSEzQUembJg_GRGNC75-kbYEdibQk8CbsZy7Oz-mxwO3D-zb098HzNMRDf_5R1Ghx3bPR4wVb7z0xQJ0Gk1WVDaepGrjWf1OQb4hvrAWTS7qHfATX7P21kSVhojIbofMjKDf2Xe2gVVFGjk8Cd1EV6DE5CKUDm3bDRk2jP6_MVbOD5Y3bidp3rt5XOZHCdXNc6f3m5I80Rk7SKf4FTbX88x0F5YG1pNxDhfBwA9TiaRZfImEeZu0-boib8Jn280cNTXfLl_igFCOLnRxxl75Hrc-_p5dSlDZaeNf0x_KuawKLOychYDUetbgbEjZUEgZRmSilc3WjAWMNmMs6Ygflj4Yrirgogx7xIVApPCqZTNjaXRAfWyui-9CcF82hYQeWX3GlBFOYPo7jc6-O9UtNWKGFcP2mImBS8fqOsnxOk_5SctzV4sSqMUQAT5Qt_H8_Clu3Ve3a1TvCThLJM6xcZuZ-cSUTO3_PZ-qQY26tcF17qGA_7Du4n6h0DmpVSQkvcGsayiGAgjjHcZFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc2122fb81.mp4?token=NbR-NU4RKx8pRMW8ABlLF5kq6IjOYJp5Awbj0WTz1u0imGmKFtQ21MDonIsac-ADH6TSeCmZDVvAP-qvgovf6XrTKKXg-QLVoSd0l-8LqICR4Iig4Ljgw83trJKMxaulK0NDWUZIzi2p1BEPAJK9m4UhKlaSEzQUembJg_GRGNC75-kbYEdibQk8CbsZy7Oz-mxwO3D-zb098HzNMRDf_5R1Ghx3bPR4wVb7z0xQJ0Gk1WVDaepGrjWf1OQb4hvrAWTS7qHfATX7P21kSVhojIbofMjKDf2Xe2gVVFGjk8Cd1EV6DE5CKUDm3bDRk2jP6_MVbOD5Y3bidp3rt5XOZHCdXNc6f3m5I80Rk7SKf4FTbX88x0F5YG1pNxDhfBwA9TiaRZfImEeZu0-boib8Jn280cNTXfLl_igFCOLnRxxl75Hrc-_p5dSlDZaeNf0x_KuawKLOychYDUetbgbEjZUEgZRmSilc3WjAWMNmMs6Ygflj4Yrirgogx7xIVApPCqZTNjaXRAfWyui-9CcF82hYQeWX3GlBFOYPo7jc6-O9UtNWKGFcP2mImBS8fqOsnxOk_5SctzV4sSqMUQAT5Qt_H8_Clu3Ve3a1TvCThLJM6xcZuZ-cSUTO3_PZ-qQY26tcF17qGA_7Du4n6h0DmpVSQkvcGsayiGAgjjHcZFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
تصویر تکراری تیم ملی
بازنده اما طلبکار و با اعتماد به نفس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107877" target="_blank">📅 21:22 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107876">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ohiolu2y4bDdP9bY0Mj6IGLrUPKLgRQndZhmCaT6gFmn3URGusOIZfHjsB5z_aRvHAS71hTBlPYWBlA8dyYoR02-wjrYbMVTGGZ31y7IRAPr2QqKnPPqZRL1gRkpiP2xxwfCelbIWBE_-wTwAFd0YFRpO5bs-1Tp-nGL0E174dr4dCFmQiDRvzQvyVRQLLXIAFS7ysHodlSbCZh0vPg8C4DFeSMY3DGtHk5iBqD304Z0uMDmr_jIcPkWUUPQh2oZU5urrJbphzCPeqtWSo3hgffnTu_tcubzojRNbQaomOzI_U0mekPICXy92TMmAJgo4uS9IalaDoxhT9ysEmps8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇫🇷
ترکیب تیم‌ملی فرانسه مقابل بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/107876" target="_blank">📅 20:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107875">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71f2c09e35.mp4?token=rrGVBZAZerXnn6mozoJnmxLG3fjsLv6J3W9bu8sbKpW70QSMyaOwItG6sCoHuWBTl8S0MUlDahJ8xbCkEkoTkAHyTzZxt0i6NDhGa4k_dAldnl4m2uQuVCYL8Vicx2_KIGDI3eO7Tl9Um7WXBjAUOXo7Q_ZD4tTnQjrTOsXQ1_Kph41ONy34-PsFy2k97kTnuYKku7Uys6WGdh681VlUwR383ogRm2Q26Fzb3PMX_xxHLeFKNvk__MbvPdLsOSj8uvkGMirMInpqTlBGp0ewt2XMvAU60v5KtNq1gbZ5BXB9S7ntGjUknp-8Khrx0BP_ZbC_DAotHObHQ4y1BYwuO2oGtErO8NwIdHTcI32Vin1_yaB4VejT9mCIKjK9TsSK7ZPyUMM_XmCMSAdioZGMEfNtABEQTwCZ6OEu8ikb3o-H2EOPPaicFvcqpVUC2idQZfXk5aKVJvfU9mrxG27n3MnWENr7vGpO4HbmvHjzXsLR1Yi3FzC_1nl5Vk3p82uX6AtMwflIN_6T9uF107WnQpwvNAUzig4RJ6vizfVnMQp0WNdNsSL5zSJNOlUpMkY8szPt12GJ0zGx0kbzFLASV6891kFkQFdJ-VoCXyLGwwSYhq4RmlFdTw0nhMM51laQhP9ivp-5GcuwJ0U63h12pFYXs1Ke_66glF0Ycm5qFJ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71f2c09e35.mp4?token=rrGVBZAZerXnn6mozoJnmxLG3fjsLv6J3W9bu8sbKpW70QSMyaOwItG6sCoHuWBTl8S0MUlDahJ8xbCkEkoTkAHyTzZxt0i6NDhGa4k_dAldnl4m2uQuVCYL8Vicx2_KIGDI3eO7Tl9Um7WXBjAUOXo7Q_ZD4tTnQjrTOsXQ1_Kph41ONy34-PsFy2k97kTnuYKku7Uys6WGdh681VlUwR383ogRm2Q26Fzb3PMX_xxHLeFKNvk__MbvPdLsOSj8uvkGMirMInpqTlBGp0ewt2XMvAU60v5KtNq1gbZ5BXB9S7ntGjUknp-8Khrx0BP_ZbC_DAotHObHQ4y1BYwuO2oGtErO8NwIdHTcI32Vin1_yaB4VejT9mCIKjK9TsSK7ZPyUMM_XmCMSAdioZGMEfNtABEQTwCZ6OEu8ikb3o-H2EOPPaicFvcqpVUC2idQZfXk5aKVJvfU9mrxG27n3MnWENr7vGpO4HbmvHjzXsLR1Yi3FzC_1nl5Vk3p82uX6AtMwflIN_6T9uF107WnQpwvNAUzig4RJ6vizfVnMQp0WNdNsSL5zSJNOlUpMkY8szPt12GJ0zGx0kbzFLASV6891kFkQFdJ-VoCXyLGwwSYhq4RmlFdTw0nhMM51laQhP9ivp-5GcuwJ0U63h12pFYXs1Ke_66glF0Ycm5qFJ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
بررسی ۵ نکته مهم در جدیدترین نسل‌آیفون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107875" target="_blank">📅 20:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107874">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dce1470830.mp4?token=d4siQusuQYbSkYkAbrr3i6lKEOx_J3f7KloYjJaYc49WR3Mclm4CIwBBDU2bbS2Rf_-uPwYpT83exbhpwSj7dlbxQdI24oLANqm_RIz5cu5cpyhOQYpm5xLMcL9iDF8GNVDSYGFhK_9OLIfyVgceX8n2hrV4X1PdVuT6L5miKGYXHZfI3fUr7vW4B_ZFmjRB_jJYFhAJ0xJPrVS52wjjfBSDd_WTDb6OqFHR6rT7XVmtpGLg1LKKIkVOTCGTHHCLrczaOMQihgiIHeJ7Wbvkbh5q8dgo_g-OyQspzC4GXx9hVxhT5BQQSW4nwhNov1LWbOOGgtErVo5uPRwSkewwMSKC7MrdttHiDQB7boi42ydJLHVgfE7m2eFQaQlmFTiKZOT-_7jaV_8OqJFvIeYR9gN4tAQicw7B_YBxlp3zu0qY1oJoFThAGOP9o0aiI4TLVKbxL-VadesvfjN72z8VPpIrkFmdH4eVoi9Wwpop0s6B916219QwtLiB_DnkFilmGYmRw1SGC84n6vU3oOil31qH6bS_uyxuzx-_jLs98FP9rPAdvwn1KL_A8JvjptVfOR3DueyPMFRVjW8oVJ-ylBIwsgAvBNIBrhRSuxEwCEQj2Brl9Rwvl7vmDo4lLMEtEL4w2-szoq2d2NoysglxWasenFKNY9NmzAOB7WWAi2E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dce1470830.mp4?token=d4siQusuQYbSkYkAbrr3i6lKEOx_J3f7KloYjJaYc49WR3Mclm4CIwBBDU2bbS2Rf_-uPwYpT83exbhpwSj7dlbxQdI24oLANqm_RIz5cu5cpyhOQYpm5xLMcL9iDF8GNVDSYGFhK_9OLIfyVgceX8n2hrV4X1PdVuT6L5miKGYXHZfI3fUr7vW4B_ZFmjRB_jJYFhAJ0xJPrVS52wjjfBSDd_WTDb6OqFHR6rT7XVmtpGLg1LKKIkVOTCGTHHCLrczaOMQihgiIHeJ7Wbvkbh5q8dgo_g-OyQspzC4GXx9hVxhT5BQQSW4nwhNov1LWbOOGgtErVo5uPRwSkewwMSKC7MrdttHiDQB7boi42ydJLHVgfE7m2eFQaQlmFTiKZOT-_7jaV_8OqJFvIeYR9gN4tAQicw7B_YBxlp3zu0qY1oJoFThAGOP9o0aiI4TLVKbxL-VadesvfjN72z8VPpIrkFmdH4eVoi9Wwpop0s6B916219QwtLiB_DnkFilmGYmRw1SGC84n6vU3oOil31qH6bS_uyxuzx-_jLs98FP9rPAdvwn1KL_A8JvjptVfOR3DueyPMFRVjW8oVJ-ylBIwsgAvBNIBrhRSuxEwCEQj2Brl9Rwvl7vmDo4lLMEtEL4w2-szoq2d2NoysglxWasenFKNY9NmzAOB7WWAi2E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
کنایه‌های ژوله به داستان سربازی دکتر بیرانوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107874" target="_blank">📅 19:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107873">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d2ddbc7f1.mp4?token=YL6SmoPT_gdrl-eNn-eV742zZ6-A2zipMyKrEiPvbGaEFVaRToUl58eaFB5DNcgTb1V5HiBCtSyTP4Q1qJwwA-7JQ7hYAhKbWVY4aWNLQcl-9n2rldjUGv_7jWlTGA-GqrlaESTtVl9QZPsz_3b3wFo_5e0YpeRPQoVGOjAYN2FBFBaPCxKPe4FKf0S3rsj9IWUhZ5H4Y6P38YEvn8Z-rp9ZQ7lX24I7TGv09sjI5efU1yNsi_Z7NbMhIOGfan4DFALUia8AYHy_kshp-rwRNFoCTuleE1rvCFB0LicfeO77Mo5SNFmoZmShpU6gea3cTCE1oJJIVwTwZqoAKniSTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d2ddbc7f1.mp4?token=YL6SmoPT_gdrl-eNn-eV742zZ6-A2zipMyKrEiPvbGaEFVaRToUl58eaFB5DNcgTb1V5HiBCtSyTP4Q1qJwwA-7JQ7hYAhKbWVY4aWNLQcl-9n2rldjUGv_7jWlTGA-GqrlaESTtVl9QZPsz_3b3wFo_5e0YpeRPQoVGOjAYN2FBFBaPCxKPe4FKf0S3rsj9IWUhZ5H4Y6P38YEvn8Z-rp9ZQ7lX24I7TGv09sjI5efU1yNsi_Z7NbMhIOGfan4DFALUia8AYHy_kshp-rwRNFoCTuleE1rvCFB0LicfeO77Mo5SNFmoZmShpU6gea3cTCE1oJJIVwTwZqoAKniSTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ممکنه دفتر نُت موسیقی دیده باشید ولی ندونید چیه
این ویدیو کمک میکنه تا کشش زمانی نُت‌ها یا مدت زمانی که یک صدا یا نت ادامه می‌ یابد رو راحت متوجه شید
و به هر کدوم از این نت ها چنگ، دولاچنگ، سه‌لاچنگ و ... میگن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107873" target="_blank">📅 19:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107872">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd348ccf0b.mp4?token=urxNideumVJQMcN10EkERasEkZ9OYCop01pusJWIPIdq_poaHgi5zFGcTL1_bG4NFAYYE69CHtvAv8YKmvvvhURzH7FZ4zlYSGxUjTjSke7J6dPr6P9x3JN5jN9hmxnkL2FQvGQ1Bip2Z0yzYp-cvAkFJq2Snq1O6BR3Eb8w52Rb2GGqUSqP46DC2AlCh5L9LITyqfEq7tuTc9OwPIqg3uhNQ3tgRMET2YyUZGIo3tnaOC9_E_ttQETniitK0kwaZiOS2o27lLQVOR7BFcdf2HoCxdLD1iKa4RxnlWdKRr24tk7fo2iKGziK2zUklm3kZvAxFyUEnoU-wd-KkfvZEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd348ccf0b.mp4?token=urxNideumVJQMcN10EkERasEkZ9OYCop01pusJWIPIdq_poaHgi5zFGcTL1_bG4NFAYYE69CHtvAv8YKmvvvhURzH7FZ4zlYSGxUjTjSke7J6dPr6P9x3JN5jN9hmxnkL2FQvGQ1Bip2Z0yzYp-cvAkFJq2Snq1O6BR3Eb8w52Rb2GGqUSqP46DC2AlCh5L9LITyqfEq7tuTc9OwPIqg3uhNQ3tgRMET2YyUZGIo3tnaOC9_E_ttQETniitK0kwaZiOS2o27lLQVOR7BFcdf2HoCxdLD1iKa4RxnlWdKRr24tk7fo2iKGziK2zUklm3kZvAxFyUEnoU-wd-KkfvZEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
وضعیت پسران و دختران پس از نتایج کنکور:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107872" target="_blank">📅 18:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107871">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTApijoh8WlPHPT4zpHQYZmGDQnjP06qZ4kcbwtcCCUAwyK9FE_6nBBJrpbweg_b0fwIay3nY8f-OQgvnaqXZTegVHMFuZ5VSwv4tDbRU0KD5JNlkl0c4szPDfY2H63wCeze-F-e1kPaoq5IfpA_mWHJw7W8o-HHHnwh8bqSJ6pRtXMwzvoX0b1OyT3_SY1Zst1nWjYYq8K84yFl3h75RXASdGL9S9yrflUN_82vYbGamntmmm4qwjgAK6Su5qwWdO606SrXa9s2chV4KmBDw5db5oFV5LXh6k5I-vBp1jVlOKZFo2Rxf0CuGeqHxnuVoIG6o7jzjGsNOdzGJ34AJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
فهرست نامزدهای جایزه گلدن بوی بعد از کاهش از ۱۰۰ به ۲۵ نامزد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107871" target="_blank">📅 18:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107870">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6601bb6094.mp4?token=V4-vSbpzu2cRiPoTX0mfgVagrMuvKhvj0LRhOZx1vVUD6HS2IAD8A34lNYNe9t6aUJidsCRHxPF3fPPtI45pTekNDGidh507r1okFAucFOCgHUaCejY4KH1Z73d2gxY8BQ3Ju7vPshyKfBDQWbzvJhWMLA4IESiT-HV3-l1jovydFIbv8VjnuY5PQ1I_6JCZqR5hgMz5JQRmyNDPiBdaMoPxub14DcJFCDuPEPJYGukin-B87gJS_WJOLSyAcPZu9mwZqU_oMjpsJPyyg84YGx88xJ_BqfL4ObKduTTGHx7lR4YYSsoTHJO-8FzxUtECdo5DbdxW5hCt6extJE7CEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6601bb6094.mp4?token=V4-vSbpzu2cRiPoTX0mfgVagrMuvKhvj0LRhOZx1vVUD6HS2IAD8A34lNYNe9t6aUJidsCRHxPF3fPPtI45pTekNDGidh507r1okFAucFOCgHUaCejY4KH1Z73d2gxY8BQ3Ju7vPshyKfBDQWbzvJhWMLA4IESiT-HV3-l1jovydFIbv8VjnuY5PQ1I_6JCZqR5hgMz5JQRmyNDPiBdaMoPxub14DcJFCDuPEPJYGukin-B87gJS_WJOLSyAcPZu9mwZqU_oMjpsJPyyg84YGx88xJ_BqfL4ObKduTTGHx7lR4YYSsoTHJO-8FzxUtECdo5DbdxW5hCt6extJE7CEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
میگل آلبوکرکه، رئیس دولت منطقه‌ای مادیرا، زادگاه کریستیانو رونالدو:⁣ ۳۰ سال دیگه کسی یادش نمیاد کی سرمربی بوده، کی رئیس فدراسیون بوده یا کی کارشناس بازی‌های فوتبال بوده؛ اما همه می‌دونن رونالدو کیه.⁣ این تفاوت بزرگی و معمولی بودنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107870" target="_blank">📅 18:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107869">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107869" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107869" target="_blank">📅 18:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107868">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yutcyd07fVQB7jyc4dHWOx-t7POlmEfGa_-3V3ULa-4XOV-BZuIZLSB_EYU9Rc-nknhNmH6Vlt9DKGETwN00S79993MBxCAS4ByQ7nPsqQBiF_tYhjoZuQUIV1azsrqI5vaq8BN6er2C03ewR9HkhMuwnX2PgHZ3La-Wc75mq8OoT2yZGq4236tnHSmnDrYRt251ZNgr0EFAvFomLsopXVAT0Er9Vnr61cYHBhKTRfKUoxfe70pZ3rv50vYdwMX6Drkx7gUEf6SBLLhSCEhIHiuGSnbQrULKJhvJnHoMkaXeWHf_LGicZmLdgwMctfeeKCXM-Rq1w5KTpk2AVvyJYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز بلژیک
🆚
فرانسه را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
بلژیک: ۳ برد، ۲ شکست و ۱۰ گل زده
فرانسه: ۲ برد، ۱ تساوی، ۲ شکست و ۷ گل زده
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107868" target="_blank">📅 18:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107867">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8rau3Z2RqwmY4A74lBIB1jcnUsuT99uocxE1Je63P_Dt3CUF3PMedUtIYFeOZ8g8M3rlAWCAd4XtK7pZ0WKHaY8qSwSE-nocKFzv7uX3hrjUkp7q5C-ff-u_IHc2v060s7NQiCoJ0MJmSIpmxcm4yNmJke5JsqjFhmZ9vofIu8VnmENnE22rN_kjPuSNZwSOepmeoPngBMAejiJw8S4_F8NW4e-CLFmqVJL7fZLgAB_4gfPNPYZ6aB_KcBdPVaOjIg6-57ONhtaNpeNbGK_xQlgY431znERy__JLTWkB5BLGZvnMG4hOTHiU_pgeXBnY14csOl8UnHSNJDLpvMsmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
گونزالو راموس در هر سه بازی اخیر خود با تیم ملی پرتغال که به عنوان بازیکن اصلی در آن حضور داشته، گلزنی کرده است.
🇵🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107867" target="_blank">📅 18:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107866">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1c39a914.mp4?token=twZRFECtns4wdDC3mxZX7yJPa8WV3LntjdAbNSmbXr9Bhm9DiM_meZfMFFrW7lc9ptiDHXoZblLycLdhABjWIgbSVa_jDpn9L9dyOYkLAJ3yw30klm6M6Uz28i7iKxQswWSgXw1nPRxLOmPIpHtx4H-FiPSQRSjLdoQMD53Z9vmLhvJU6hHdqfMa98L0mRwzqvADmuz1WQejwGj_Zugh_x1pAN18AS-PRdb-V8hXSsi5fSC4cXfvq2WzkO-XznrYLjZFcCDMY_h1KIBFM1_yR3RamPsV5uGVn4PWfdorBKIa1zdLvaqdfSn4VDiYY9w16ywgttr6uFhawwahJwaeRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1c39a914.mp4?token=twZRFECtns4wdDC3mxZX7yJPa8WV3LntjdAbNSmbXr9Bhm9DiM_meZfMFFrW7lc9ptiDHXoZblLycLdhABjWIgbSVa_jDpn9L9dyOYkLAJ3yw30klm6M6Uz28i7iKxQswWSgXw1nPRxLOmPIpHtx4H-FiPSQRSjLdoQMD53Z9vmLhvJU6hHdqfMa98L0mRwzqvADmuz1WQejwGj_Zugh_x1pAN18AS-PRdb-V8hXSsi5fSC4cXfvq2WzkO-XznrYLjZFcCDMY_h1KIBFM1_yR3RamPsV5uGVn4PWfdorBKIa1zdLvaqdfSn4VDiYY9w16ywgttr6uFhawwahJwaeRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤡
آخرشم نفهمیدیم بارسا چجوری تونست 8 تا بخوره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107866" target="_blank">📅 17:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107865">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7PHq4dtgHaHzQemcCK7480XESlXGoOrVHhw7Qpa6s1y8kDmkBx_LcHSyBrmzlRH_-r1aPsL2kJx6eK-WxPgq2bmPb1xOtuOEIuGuYsvZvrOwued8OESP8bXMn8LKPX-gawM_mjchZ8EXvEv38MlFafFHvSmnZm_gKkB5uUAP31NgzHzN-sUVB2eBHcXuxxFBrQgxuJW38ow9zDvC_NoHh1TlKesBzAomDCzsgdQk3EpZlHnlf9X3GZSMoxKMoqampsPP_X4Y2_vv-fkC6MjAvtRq47vmvLiRIaMeT5LDyW-6O1rxKTHHNlqRu9w74g8hlJ1VG2El7TNo0mYQadPMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
عکس جدید نیکی کریمی در 54 سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107865" target="_blank">📅 16:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107864">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d579a3c3bc.mp4?token=MWPQzpp-zObM9e1NDzZq6c5ZGI65R0g4GkL-o_OS8R7jxHxFrR7Y8QiSS2KfX69mZa_fbDBAJtlSEzXgIZ1CnjKjJ_E_O_xVUwfLSaVRCzfsdPgUjkBbsSjienJGxigFPm-GxJtGoO1SkHIGYQsMXAs0fsIxMfhpNWOT3P7bQ2wD7cgwCtS0n5BKc4rFM0MB1m5hcH2XlhRQYjcnV--LP853Ry_aA9UUmHPqKOsT7qPvaNIT5iVC8d-qbK-spABFgW7Jz2UrqjpZOo2XU_Epdp19kelPoLSvSUJfHKEAZWe-orNroGsdxmnPf4M7oWVip3YSZj4b9hrEEdsAGL4f6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d579a3c3bc.mp4?token=MWPQzpp-zObM9e1NDzZq6c5ZGI65R0g4GkL-o_OS8R7jxHxFrR7Y8QiSS2KfX69mZa_fbDBAJtlSEzXgIZ1CnjKjJ_E_O_xVUwfLSaVRCzfsdPgUjkBbsSjienJGxigFPm-GxJtGoO1SkHIGYQsMXAs0fsIxMfhpNWOT3P7bQ2wD7cgwCtS0n5BKc4rFM0MB1m5hcH2XlhRQYjcnV--LP853Ry_aA9UUmHPqKOsT7qPvaNIT5iVC8d-qbK-spABFgW7Jz2UrqjpZOo2XU_Epdp19kelPoLSvSUJfHKEAZWe-orNroGsdxmnPf4M7oWVip3YSZj4b9hrEEdsAGL4f6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
صحبت‌های رسول‌مجیدی درباره سختی مربیان تیم‌های ملی بدلیل زمان کم آماده‌سازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107864" target="_blank">📅 16:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107863">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ea1e2bc4.mp4?token=nLDbpnPOcD16VrEB-dWwY-2N3-jqNUV3bBltL9OdEyMZcc7RoVYc2FAMqVGScllzqOvRARllE9tlCpLBQt-ZM0Vax6Hw65EXzbO5szpPQr5_4tv9PHCeoPE1A4MVBXDTF5g_8AqSLiwz_2oFbPblIK2c5B8r4a9ZGleFtkzy9tSQRpm9kPq7mtOQu0H3EzvID2aZYqsCiqnHm66Xfdt1lkdtNf_zpxcWj9STaqcitr6O8adU_PcU1Fif-p6DxbGPkdBxPI-3edEKMduSXxjgEfp_ffgyRs46aVT-5hHTQKzU39I31QL_CaOikOdGDSAxP3Z_cWHkREyv5XmOR3tzTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ea1e2bc4.mp4?token=nLDbpnPOcD16VrEB-dWwY-2N3-jqNUV3bBltL9OdEyMZcc7RoVYc2FAMqVGScllzqOvRARllE9tlCpLBQt-ZM0Vax6Hw65EXzbO5szpPQr5_4tv9PHCeoPE1A4MVBXDTF5g_8AqSLiwz_2oFbPblIK2c5B8r4a9ZGleFtkzy9tSQRpm9kPq7mtOQu0H3EzvID2aZYqsCiqnHm66Xfdt1lkdtNf_zpxcWj9STaqcitr6O8adU_PcU1Fif-p6DxbGPkdBxPI-3edEKMduSXxjgEfp_ffgyRs46aVT-5hHTQKzU39I31QL_CaOikOdGDSAxP3Z_cWHkREyv5XmOR3tzTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
بیرانوند تو سربازی اسلحه بازو بست کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107863" target="_blank">📅 16:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107862">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/367af750e7.mp4?token=FzUl-Cu9tDZG6umv0X9sPr31gqKehHm0_x32mlRZzS9Wxyeb5O4mmT5W4efdzm8fXuBl_AVZsNSl0rtaWFiY3SiylVhRXds9nr7ew4P7_rFraO_FvHthJjX63mtOk2WG55F3RGpydCg4tEpQ2-nfz4JadDxMKxRb1BWvOlZy5pdhszBGfGhFsC2mXZNNz7vjTb6bdYeNM-8cQfaFwoSXA5r36HLSIBtxfCVn--rrGowv4b7M8XGgkaDETZ6sEk3Qy2gnwp6ECCXGTe5JRgubHg7-rv0Ce9exoQ6qQQmMWtJxLtwvLHVayUUUPj6eJPGouqdAmCLTRAApy-whqlBiTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/367af750e7.mp4?token=FzUl-Cu9tDZG6umv0X9sPr31gqKehHm0_x32mlRZzS9Wxyeb5O4mmT5W4efdzm8fXuBl_AVZsNSl0rtaWFiY3SiylVhRXds9nr7ew4P7_rFraO_FvHthJjX63mtOk2WG55F3RGpydCg4tEpQ2-nfz4JadDxMKxRb1BWvOlZy5pdhszBGfGhFsC2mXZNNz7vjTb6bdYeNM-8cQfaFwoSXA5r36HLSIBtxfCVn--rrGowv4b7M8XGgkaDETZ6sEk3Qy2gnwp6ECCXGTe5JRgubHg7-rv0Ce9exoQ6qQQmMWtJxLtwvLHVayUUUPj6eJPGouqdAmCLTRAApy-whqlBiTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
▶️
با توصیه‌های هانی‌رامبد، اینجوری شانه های پهن تری میسازی؛ ذخیره کن و بفرست برای دوستت
❤️
👌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107862" target="_blank">📅 15:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107861">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfjdeznCl5Zew1LBZivFyT6bY9nSbFlxnvFETvAso8vdbX7HHtEIlJ00twYGhr2td3eUFWOej5Vxcd7rxDijlUnCZnp03zd3DYSs4JfIDtNIerRf36lcav0-VO3NnPlsavSCkmLCIQtWmr4JXEq26qGPp-RL6-KGYgCTcz81QQIxrhgX-9spNmK-eIvbZQXl_tvsBeMUfk6rBWJCmOr-4dCyATb_FoUFz5dd2xogx07TuY3UniwpmuaE3kU61rOSZ_DiSfJiuuwU6RUflCt-esYLRtqzg_u3sL_0vMV87i5LbovoAzK5Yyj6IlDFp7UCn6nYiyFOm_4jhhK251pVlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
اسپانیا اولین تیم ملی مردان در تاریخ فوتبال است که 41 بازی متوالی را بدون شکست به پایان رسانده است.
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107861" target="_blank">📅 15:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107860">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c6f99cc68.mp4?token=EVK09rHl0bLN0Fjm6ONKQ7N-kZ1_xf-rtjWWtggAhoXHTXbEtdRHTTAhhmBU8QAUdYWOKCwhygY5mFSuFSDLutDfhJHU4nqn0Wz0BYxL1Byta7rrNElQ1txzE9JSqvMFk5IoJnHVzsfUfxbXdz-dmkAVVOvvCOmoa6R7D3wHYaV8jGdHNZIiMwd0cWXWVpkoE5_ke3-PVF5dWFkurEbUWH8VNpBv3mEVTituwSKCjoz4ZK3PI6Y19Eg4h5d0Vt6kWHM3NW_xY0ZaB_jU5Xi61gH7J0Xn2eGlMXD0C0pyu4xmdm7zuoBg-ERVD3kpVaxCiLtaUt4RT26Zh8Rc6qco7jolpo8LxitqJKJDXDl7_U68lRnJjcY6EZGShKFJvehZd1NTYI2lXfuJBZE0lHNyISVQ2eyJpzd77o49w-8vi49yAAJYfmzUzcvlACUa0WEvF2Uj-VW_G5Jx5Y2Fc08SjfyL9RVl1NUUjfbwoW94x4Ncj1eqpFM_AcmPRs5Au4OJ-hN8VzJgxTo7Ndt_AX8MI01slmYfz2rU4NepbjvPd8c0gIAxrxKWXLy4Ad_JAWj5NZ86EZGgDpz5SyBQxvDxoQw2V6uN0A4LU6JQ4z_CDl0tsCPxVBcLi3CeNzJR1CYBfvHedE7b5-qQKKlq-z21RaT1yLTzEEsIlF9_frF4l5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c6f99cc68.mp4?token=EVK09rHl0bLN0Fjm6ONKQ7N-kZ1_xf-rtjWWtggAhoXHTXbEtdRHTTAhhmBU8QAUdYWOKCwhygY5mFSuFSDLutDfhJHU4nqn0Wz0BYxL1Byta7rrNElQ1txzE9JSqvMFk5IoJnHVzsfUfxbXdz-dmkAVVOvvCOmoa6R7D3wHYaV8jGdHNZIiMwd0cWXWVpkoE5_ke3-PVF5dWFkurEbUWH8VNpBv3mEVTituwSKCjoz4ZK3PI6Y19Eg4h5d0Vt6kWHM3NW_xY0ZaB_jU5Xi61gH7J0Xn2eGlMXD0C0pyu4xmdm7zuoBg-ERVD3kpVaxCiLtaUt4RT26Zh8Rc6qco7jolpo8LxitqJKJDXDl7_U68lRnJjcY6EZGShKFJvehZd1NTYI2lXfuJBZE0lHNyISVQ2eyJpzd77o49w-8vi49yAAJYfmzUzcvlACUa0WEvF2Uj-VW_G5Jx5Y2Fc08SjfyL9RVl1NUUjfbwoW94x4Ncj1eqpFM_AcmPRs5Au4OJ-hN8VzJgxTo7Ndt_AX8MI01slmYfz2rU4NepbjvPd8c0gIAxrxKWXLy4Ad_JAWj5NZ86EZGgDpz5SyBQxvDxoQw2V6uN0A4LU6JQ4z_CDl0tsCPxVBcLi3CeNzJR1CYBfvHedE7b5-qQKKlq-z21RaT1yLTzEEsIlF9_frF4l5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💥
پیت هگست در سالن «کلون آرنا» در آکادمی نیروی هوایی آمریکا، در یک نوبت ۹ شوت از ۱۰ شوت سه‌امتیازی خود را به ثمر رسانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107860" target="_blank">📅 14:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107859">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/969710a175.mp4?token=Ly4D8iu_B8Mh4j7LPt5POCpDu-FXp0IqWqK8TQMGK2eojTgRMC7CpzsVOrtMQOIqNWwP1kwXWAedv7QSRW3qi6ZZI4orIYONGDf307wWihTT0g3rRUp8jznmTOWlpcrKGctDCOY0TOBG8Lo2Wc1AXSjaQeeg5m0-FwiXsIo0V-6UZ8-XesFy_c1EHLioXo5UVrumO8YkwAPS_ZouUa766yMSOJVGijt8XugL4gFNTP6Q7OO3RajJRcn4zBrlWfg_YkvV_NxPSo_XbwodAkQlV1Umr-WreTln0u9ppOLtK3IH_NL0ws90DxX9z09l43u--BYVhzwxS7YlIMhsqRyCt17ysfhvq-uvX4oCDiRPnBOY5sTg7_MNS2GMzZm--jlyhrtwxKyKM19hdQVAInCmuYO116p7aC6W2lfgwfBpjuJ24pm1LU1zactwJ_NVTs-2gLZc85rvmXhYwgJ0vq6GgXlSjCyXKFLQDpojLK-JaGjiJnMOXwCfObTxcaNbEns4i4CxhHc4xyHQ9egFCmi2M2Y-qN9_Z9F1CiTKBtZ6F475AW83QapyasHBcHOGDDRYhZNKr1aFJ1nqCulfRCGOG5wBV0c9nEA7za3TNQY_pAhVsjHVZDPcVjlSUp1Fg5POuAkG7t8K24DFvb25cJtoQnjrU_1v6f5fy5i8uYTe7eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/969710a175.mp4?token=Ly4D8iu_B8Mh4j7LPt5POCpDu-FXp0IqWqK8TQMGK2eojTgRMC7CpzsVOrtMQOIqNWwP1kwXWAedv7QSRW3qi6ZZI4orIYONGDf307wWihTT0g3rRUp8jznmTOWlpcrKGctDCOY0TOBG8Lo2Wc1AXSjaQeeg5m0-FwiXsIo0V-6UZ8-XesFy_c1EHLioXo5UVrumO8YkwAPS_ZouUa766yMSOJVGijt8XugL4gFNTP6Q7OO3RajJRcn4zBrlWfg_YkvV_NxPSo_XbwodAkQlV1Umr-WreTln0u9ppOLtK3IH_NL0ws90DxX9z09l43u--BYVhzwxS7YlIMhsqRyCt17ysfhvq-uvX4oCDiRPnBOY5sTg7_MNS2GMzZm--jlyhrtwxKyKM19hdQVAInCmuYO116p7aC6W2lfgwfBpjuJ24pm1LU1zactwJ_NVTs-2gLZc85rvmXhYwgJ0vq6GgXlSjCyXKFLQDpojLK-JaGjiJnMOXwCfObTxcaNbEns4i4CxhHc4xyHQ9egFCmi2M2Y-qN9_Z9F1CiTKBtZ6F475AW83QapyasHBcHOGDDRYhZNKr1aFJ1nqCulfRCGOG5wBV0c9nEA7za3TNQY_pAhVsjHVZDPcVjlSUp1Fg5POuAkG7t8K24DFvb25cJtoQnjrU_1v6f5fy5i8uYTe7eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فوتبال معلولان عجب صحنه‌های فوق‌العاده‌ای داره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107859" target="_blank">📅 14:25 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107858">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81e41c5067.mp4?token=EFkYPUunMUaFg_LRkmmWO68uMa-jPkYFauqyl83gpmYr5EmwVhjV3CNf2Gjg6En95Qcd7kXpcAo3hnIjPs4o8alZQGD_uBuMKnIh1WFX-oHncB8gRXjE7Q0gGUW4wPTCGrWWlr-LoDmRJM7PBGegyko_wk-cVlaGhZ4v6ChAx4bQIbRJ6Q1jJ2epkqv1orJKqdu5u9comDtXfo4twnLZu0SQzaGRAWt5wMCZ6XnXNOmIOB9g-wE8xbvTk_D5CnyQ8TnloOvXgmTVtSLpI4wPgI19AxQAItma3Y1IWo7VQHQGbZ5mKpw4nYP7E24c7zn54MAeoFGCbxH7Ir6MSwXVDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81e41c5067.mp4?token=EFkYPUunMUaFg_LRkmmWO68uMa-jPkYFauqyl83gpmYr5EmwVhjV3CNf2Gjg6En95Qcd7kXpcAo3hnIjPs4o8alZQGD_uBuMKnIh1WFX-oHncB8gRXjE7Q0gGUW4wPTCGrWWlr-LoDmRJM7PBGegyko_wk-cVlaGhZ4v6ChAx4bQIbRJ6Q1jJ2epkqv1orJKqdu5u9comDtXfo4twnLZu0SQzaGRAWt5wMCZ6XnXNOmIOB9g-wE8xbvTk_D5CnyQ8TnloOvXgmTVtSLpI4wPgI19AxQAItma3Y1IWo7VQHQGbZ5mKpw4nYP7E24c7zn54MAeoFGCbxH7Ir6MSwXVDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سمفونی خیابانی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107858" target="_blank">📅 14:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107857">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5554fbfbba.mp4?token=KnDT8AGDA2sl7I3ZRxM6vSz8COKgfLWMg-0s5QTu6ywjgRAEtwVGBQVWnKhsOxb7Xl_OjVn4S_OBuTTLNTvswjJTOwziGoj0VUBxHSw0873xyG3GLTfKfmpkSflTysDykNQGH9Mb5ypbbs4baseFXfX43Fm6PNzVJxbJKjOaBKubmfbCcC1dP1VJVFSlOejHx0oQcM5FUjYteLGCC5zWY0ZtmPUuYEyUxtNF40ISCaUpMDM0EutNwgIV9vAWK4Dbvigga8R7j1LAoSehhs1Za1whO9P_d61T1Ze9qQxeJvFMVwQhnbZs-QuxR5mxpIl1y_7H-sj6PqlxH345sXQ_Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5554fbfbba.mp4?token=KnDT8AGDA2sl7I3ZRxM6vSz8COKgfLWMg-0s5QTu6ywjgRAEtwVGBQVWnKhsOxb7Xl_OjVn4S_OBuTTLNTvswjJTOwziGoj0VUBxHSw0873xyG3GLTfKfmpkSflTysDykNQGH9Mb5ypbbs4baseFXfX43Fm6PNzVJxbJKjOaBKubmfbCcC1dP1VJVFSlOejHx0oQcM5FUjYteLGCC5zWY0ZtmPUuYEyUxtNF40ISCaUpMDM0EutNwgIV9vAWK4Dbvigga8R7j1LAoSehhs1Za1whO9P_d61T1Ze9qQxeJvFMVwQhnbZs-QuxR5mxpIl1y_7H-sj6PqlxH345sXQ_Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
👍
ویدیو جالب دو بانوی کاروان ایران در ناگویا و خوشحالی بابت کسب مدال در آسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107857" target="_blank">📅 13:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107856">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cedf090cb4.mp4?token=V-gYY033xO_27Ia1K1QbGBJOv7kuhlCDq8rBIyZuxqQW7zd180ZqtxG8qP8LVywepUpgR2l80ti-GwcArIx6VLjKsenVk3EnA3YcAzOWa-zwQmR6OP_oIeoPYFs-Nkl-cK8vuyKyQEci9hImSt9WrDxPpaJ6KR5PaabW7qcrZU_bejUSjfnDRQ3VtAJxaJYodE0HzcwgpPn3-MsrJiUYk69nEOtpDpf8DL0RrAxlKsb9fbyEy4z3RC3Df1G1ceGzIk2jbQb78oszfETK3iSxrG1ft8CP32K3NqDmS0JRBso2h7R9mbmTbo5xVPYTCnNhkbZKeYDnG01bu69KRwlDvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cedf090cb4.mp4?token=V-gYY033xO_27Ia1K1QbGBJOv7kuhlCDq8rBIyZuxqQW7zd180ZqtxG8qP8LVywepUpgR2l80ti-GwcArIx6VLjKsenVk3EnA3YcAzOWa-zwQmR6OP_oIeoPYFs-Nkl-cK8vuyKyQEci9hImSt9WrDxPpaJ6KR5PaabW7qcrZU_bejUSjfnDRQ3VtAJxaJYodE0HzcwgpPn3-MsrJiUYk69nEOtpDpf8DL0RrAxlKsb9fbyEy4z3RC3Df1G1ceGzIk2jbQb78oszfETK3iSxrG1ft8CP32K3NqDmS0JRBso2h7R9mbmTbo5xVPYTCnNhkbZKeYDnG01bu69KRwlDvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های متواضعانه اسطوره مهدی‌ مهدی‌کیا درباره اختلافات بهترین نسل فوتبال ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107856" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107855">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54734be7bf.mp4?token=rBrnn0YcgbdFX_-rKnPMTdgC57BdnvQ9SYdgauefdI0zmYKmWICxnoGIwkRD4gWlGFu64g2lWtajlRC2vVxzVtIe9gsSdwt4AZWBbrozZQC5R46qGfUXAuab2vJHZCXe1m6txZqDzN1p20BJv5yUVBlFD7UBTqgFDuW0IcrxUCZSJaLpdiXnc6A9Y93KdhJLCDcvkP_Thv9YTBkos0GePTalBvLL7QN-ZSGJ02GQeWmYKYw5Wg78m1b1ogU5nclsmcKEyALimQdrKDLmuluxnXLSQVghUNryc6nM-ErHorH5GzijgBzj8t4ATborr5C1fZqthah3lBGzA9QBUScARA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54734be7bf.mp4?token=rBrnn0YcgbdFX_-rKnPMTdgC57BdnvQ9SYdgauefdI0zmYKmWICxnoGIwkRD4gWlGFu64g2lWtajlRC2vVxzVtIe9gsSdwt4AZWBbrozZQC5R46qGfUXAuab2vJHZCXe1m6txZqDzN1p20BJv5yUVBlFD7UBTqgFDuW0IcrxUCZSJaLpdiXnc6A9Y93KdhJLCDcvkP_Thv9YTBkos0GePTalBvLL7QN-ZSGJ02GQeWmYKYw5Wg78m1b1ogU5nclsmcKEyALimQdrKDLmuluxnXLSQVghUNryc6nM-ErHorH5GzijgBzj8t4ATborr5C1fZqthah3lBGzA9QBUScARA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
خاطره بامزه علیرضا بیرانوند از شب پیروزی دراماتیک مقابل پرسپولیس در ضربات پنالتی …
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107855" target="_blank">📅 12:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107854">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ko3QKtTayfiEBasqopsvzKUrVVKLe9ggJUZ2GIrG8e3-zk_NizAQJR1elJMBGfkiSmF4j-PLxPC8U5Nx9x-ovR1sJFPWNovZdb3mON5GGiFICO7btiKJ7LD1ebtcPP4uOSQrQqBs9Mse71q3GhxL98AmwImvjEaIPtLGcSHbGlAAPL43uZaKmccgNY5QGMq5GLTJOBIAAIuJhCz5QO2yk33u9WCXiWPUiJkl2Rj-OwSrepWE2a0U_4Cr3jzUSOPX6jfr46496fLGh3YRG6WL7kpGZRQIlg1qyvKwtL0Nvk8D09xsXYG4LbfS8wUoAooIVmI4kpktWHX_zijSChMQxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
استوری مدیررسانه‌ای استقلال در واکنش به مصاحبه شب‌گذشته مدیرعامل پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107854" target="_blank">📅 12:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107853">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKKbumzq_m6jHK-txcB7siZSjm8MDVRjuZEdzZbpLAg_xOJ92zNumXpxXCdqK-50ki9teao7UZ8jLlytJ_sd8e_3Jg-KYif0r8Skqxk7wgtj4_EPe5ef3YFR1Qxsausl8nahIGxydLwT_FqEWEnTVso5Pi5Xc6-YYQRFOk9JV0e2tk9qEG8VC8APYdMEokHp_Ah0xDfOQff8WB01G_Kj6nR_Gvm9ncGor-BIYEiLrr2i4Yk6z_AdDFD7mdFCyD0WDquBdajf4Sbn4x3wSs7UGaJ7qkDeh2irEiXW87WnUUq1oycFKVSSRp_-hryFBXPI9U5qO50rfMrw3246b_dEWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
هیئت‌رئیسه فدراسیون فوتبال اعلام کرد که جام‌قهرمانی فصل‌گذشته به استقلال داده نخواهد شد و پرونده این موضوع رسما مختومه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107853" target="_blank">📅 12:25 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107852">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f754e7f64f.mp4?token=mdmsBP83r28iEdtQ4GFd6wOeruGPXH4yhJqsuDP8K7modYDyxC0d7fVcHVqIEE8jvkS1lGZVbJ4ZFHyYUK4RXDraYQu28rjiMw9gLjgG5LC8EnSlIbFcxGzqkkRwZnkYAqkk42baE-bk6-4ZUxgeRdaNPuZKQtXzPABdy8HwX9kYx8h9WP36SbGUAiOwvCg9KSWmPALejxDMK156EdIe6CmawRg9BUDylJmmfdveTRVAPwNot537GAQwQVl8NbF4IhlXS0i3IawdVLnH3DjH-SHH17zmeEEDFYhiaE8gzzR31ohVpUULuJKEfgiGH3_K7Jwz2YiOUjE0-RH2CDPeDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f754e7f64f.mp4?token=mdmsBP83r28iEdtQ4GFd6wOeruGPXH4yhJqsuDP8K7modYDyxC0d7fVcHVqIEE8jvkS1lGZVbJ4ZFHyYUK4RXDraYQu28rjiMw9gLjgG5LC8EnSlIbFcxGzqkkRwZnkYAqkk42baE-bk6-4ZUxgeRdaNPuZKQtXzPABdy8HwX9kYx8h9WP36SbGUAiOwvCg9KSWmPALejxDMK156EdIe6CmawRg9BUDylJmmfdveTRVAPwNot537GAQwQVl8NbF4IhlXS0i3IawdVLnH3DjH-SHH17zmeEEDFYhiaE8gzzR31ohVpUULuJKEfgiGH3_K7Jwz2YiOUjE0-RH2CDPeDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
چالش فوتبالی با چهار اسطوره محبوب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107852" target="_blank">📅 12:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107851">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzhTDPvjc-8ZhnMaMIXtNRGM_jL5LbJ0cAQmd429Aar0Lnn_umAQwY22Okz43Xrsj2S3dWkmspZ7s-nRpVVBMrQwklo7U4YTEVLFTiB3bytjrQRKh3NDGTkoueeBLaD_i1Onigdi62lpyERD5VfidkIPhpdk0qThs01NcdTkZE7b8ZPNfYgjuYsxgCvlRjjAPHmFP7HmCDfrz__CHhC1dK_1T02o_MO6HBMyQfvkRXt2NNSmqwmQwtyYQwhqmNT2rD7H7zlc9Y9oxE_n0lIUpNwIKGCo-GbsAHhpr07J3zEgnQwFIhsLpInRdOg_oSG9E2vrrwPGovKaKS0jiAwG-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
عملکرد مهاجمان بارسلونا در این‌فصل چه در بازی‌های باشگاهی و چه بازی‌های‌ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107851" target="_blank">📅 11:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107850">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6fd2204c7.mp4?token=mWIl1sBbCyakJrOZSVFmUG3q_6uQmYcUd-4MkaPUxkElvwvbiaZ-gzlMvaLWKvghGhSBC43daFSpOnHp3mG6--Sy1tN64_lcEbsz_B1F_jURasiU2oRjavHo12gd_stSuPffsAqa-Dp6Ky1SjLB8vr3QivfBmia5REpGJW8aItIuAgcX-SueWncAP2rIYjUQKrtsnBkpAXU7K_6mnO16zAG8S2x-PTrMzxmK39bzXKiDmHc0lIHMYBAtwmc4VoJDiv9NHCyBjYkeYjbIQV-FIhGgRvSuhJpKLjKa2XjqyRrtZnkfadCTMGotMOdX0c9CJTzjNW9Jn83xiaakocTnjIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6fd2204c7.mp4?token=mWIl1sBbCyakJrOZSVFmUG3q_6uQmYcUd-4MkaPUxkElvwvbiaZ-gzlMvaLWKvghGhSBC43daFSpOnHp3mG6--Sy1tN64_lcEbsz_B1F_jURasiU2oRjavHo12gd_stSuPffsAqa-Dp6Ky1SjLB8vr3QivfBmia5REpGJW8aItIuAgcX-SueWncAP2rIYjUQKrtsnBkpAXU7K_6mnO16zAG8S2x-PTrMzxmK39bzXKiDmHc0lIHMYBAtwmc4VoJDiv9NHCyBjYkeYjbIQV-FIhGgRvSuhJpKLjKa2XjqyRrtZnkfadCTMGotMOdX0c9CJTzjNW9Jn83xiaakocTnjIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
خاطره عجیب حنیف عمران‌زاده از وسواس‌های فتح‌الله‌زاده: حاجی توی عربستان چمدونش رو زیر شیرآب شست می‌گفت با دستمال کاغذی کنترل تلویزیون را بردار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107850" target="_blank">📅 11:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107849">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8daf57827.mp4?token=ecWNWdVw28x69igCx1ust4DQIFt20mO8_VgHkgpC8mMc4zp2FwTaoocJ7K54jydrB5KdXOx036lM51YpbKghHpXDX4XBAbCZ591h7S2LwhUPwucjo8rE7g3xWqSheiVI9GhQCc8hDVD1MhJUyIp0apagGL11YL3fU-nzluBBwa72sDiERSEjf8aNc1G07Aqdp6a34ZcTfbVzIsukT-yF5jDBs1VhZHxJbdzGAK8YvFD60MqtWjIvtZnePN0LqniV8XSjgvGbvJw18sRlN0W2FKqgpwy7pywxdTFPWIWjNy0CQHUjXsFrkDGn3NUwr_bCmjny3qh_deJYymjSW_Pf5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8daf57827.mp4?token=ecWNWdVw28x69igCx1ust4DQIFt20mO8_VgHkgpC8mMc4zp2FwTaoocJ7K54jydrB5KdXOx036lM51YpbKghHpXDX4XBAbCZ591h7S2LwhUPwucjo8rE7g3xWqSheiVI9GhQCc8hDVD1MhJUyIp0apagGL11YL3fU-nzluBBwa72sDiERSEjf8aNc1G07Aqdp6a34ZcTfbVzIsukT-yF5jDBs1VhZHxJbdzGAK8YvFD60MqtWjIvtZnePN0LqniV8XSjgvGbvJw18sRlN0W2FKqgpwy7pywxdTFPWIWjNy0CQHUjXsFrkDGn3NUwr_bCmjny3qh_deJYymjSW_Pf5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
‼️
سردار آزمون به دو بانوی تکواندوکار ایران یعنی ساغر مرادی و فاطمه احمدی که در مسابقات آسیایی مدال کسب کرده بودند،‌ نفری یک میلیارد تومان پاداش هدیه داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107849" target="_blank">📅 11:22 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107848">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👀
‼️
🇮🇷
صحبت‌های شروین‌بزرگ درباره پیشنهادی که در فصول اخیر از پرسپولیس دریافت کرده بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107848" target="_blank">📅 11:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107847">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107847" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107847" target="_blank">📅 11:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107846">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ax9ITrDMBynSpmCgmNoR7EgHZc_6b018SRAW9zkif7-72HXrxc6hiEKcqIuPZ4fmkfw-5k-Mj8VFo4VUyK7FUx5muJSRUneO0ke0-c17b-8wtNhOFBN41iZVKdRpuXh_rCl1xn4qpaPz00WP34VIaOkU2ramEE5bEOIKD4HisNJafJiHdik5nFplmRy-dPmORDyXFSNQMosKKI9ePJ_g-v33_UB00nskS4Y28-N92H8hwpcIEvzxs069fl9NSW_B9Vv6dCMPe7dyIw77vS6NzvoLKark8cGIE-QhJTFUoKbRFTGwdgLlKLfvAXTNQ1sU9-D0Vs6Wqx7IwWrCghIqJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
بلژیک
🆚
فرانسه
ترکیه
🆚
ایتالیا
لهستان
🆚
بوسنی
سوئد
🆚
رومانی
نیوزیلند
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
http://T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107846" target="_blank">📅 11:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107845">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/294e1e1160.mp4?token=Eqo2hB58YjmXAhKL_eeMiIqaJwm-FIloCyGS6vEoAHTGh16J-SZ4On_DcfXGfnsexJIxjW6_wdEts39ySCgcvZ4penGfQkT4ohWuZgD6EHPvuLrYaNHfC13vGLZPod7kb1G4ri5KOv10lPC9OdJCl5ThpwFUwTavp5Bj32GuzRKPUIF25giJP7wBsG0i5DDX5_O6Zvl-PpT8RARuGVQX459gZn55uHeyCGuRmJleLkzQ94nWdC7hvyA6us94Dy13V2oiJcxXMM6iYyKGu0JMI0pfI29kdtnX8mgznk9_ig-vbiu9zjVlVBupjnvQZx4-WYbxA05Lx1idRtFe4VzYww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/294e1e1160.mp4?token=Eqo2hB58YjmXAhKL_eeMiIqaJwm-FIloCyGS6vEoAHTGh16J-SZ4On_DcfXGfnsexJIxjW6_wdEts39ySCgcvZ4penGfQkT4ohWuZgD6EHPvuLrYaNHfC13vGLZPod7kb1G4ri5KOv10lPC9OdJCl5ThpwFUwTavp5Bj32GuzRKPUIF25giJP7wBsG0i5DDX5_O6Zvl-PpT8RARuGVQX459gZn55uHeyCGuRmJleLkzQ94nWdC7hvyA6us94Dy13V2oiJcxXMM6iYyKGu0JMI0pfI29kdtnX8mgznk9_ig-vbiu9zjVlVBupjnvQZx4-WYbxA05Lx1idRtFe4VzYww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚪️
حاج‌صفی کاپیتان تیم قلعه‌نویی: امیدوارم در‌ جام ملت‌ها باشم اما قلعه‌نویی‌ دنبال تغییر نسله!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107845" target="_blank">📅 11:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107844">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‼️
🎙
🇮🇷
🇮🇷
بی دلیل از استقلال تعریف نکردم؛حمید مطهری سرمربی فولاد خوزستان: کاش سهراب بختیاری‌زاده خارجی بود!
🔺
حمید مطهری می گوید اگر نتایج سهراب بختیاری زاده را یک مربی خارجی می گرفت، همه کار برایش می کردند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107844" target="_blank">📅 10:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107843">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dt8coPtE-6_P7ihlN4jS-vqyD0Br_GBsSA1GK4X9LiCN8VCuuo7P2UR_kagT2ZBzn-2ygtUix62WNUIjoERycF4IabmCUHA85HamuIjdGNHD8FIaGip3NnX8Xo77r0cKpqd2f6RuBBu1wz8jYh_AXKesOgxZnipl0AQC9il2khDsj2bQ4cJqh7_zuy8EU0S-N3sd4c-Vtzv1J6JdtO3Hd9eeEisQ62EnFFqEwTFr7XmOP0DK6xiGnWan9BpgW96QqvYfzRkTEpeOJ9WWgEh8GH3xhxegsaKH2aeanYoqy4K1fCqW717er4hZYLV3rMGMOzIu4KuPmLQyqy4nayqUKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💸
گران قیمت ترین بازیکنان اروپا
⚡
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107843" target="_blank">📅 10:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107842">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75399136b6.mp4?token=aN_5WoTart5rJlV2eq6APrZlFG01yohvIW_7RLpUKaQxZ7SRuohvwi_N0ijip-lOE1KWsLkw3tfZTomCjd1MqrJHLxP5NM8SdY0xGdfF7yWZRCTFoqpig51Zjen0DA17ciQOVewnkI1shSZA8aRfvxPJ79fyBu9UESsVOtJeL-6xz7sLLro9zeuFCizpnAC5zHWKG3Vej_sqpaxp0Iv6wINlVYQaIwyjxeFvdL7QywfA3Eh-wo2bNby_fTqUrr1G7EWL5G5Ly2a73LC5jcl1eR22VyC-e3IYXUjzBVEY4Jf0Y9fQTxB4asCvCoQ6ZkvFcLtEc2Ra_pYBva-Zv-AGkpTqyPB00G8_98pmEzFJOrjVDauxzrsLg_H32Thszfpyxju3oOH1DaRaN1QbxKrN7wlZejBOuhKrUBxe0tPKpk4U1kh_zsZaEJiRyGky6TsHbGw_Jb_N4a7tcxlHseEZiigtLTiYXLFDqY3uoSFb6RNrci-8ZQFli-nMWIebqprUj_rh9gTVBOqFSITTN7rNUK0qsna_gjmM1hzEhvDsuzTbLhqjVPBylqTuAEkD_KEuGrvG7p8F-yWy2ixVD43beKXQtIMMJMXrdlfJowjNcThZ5MXWBD700CKUu65jUvEl9eUle4JXBRiuCUz_qDypXfLFlE94Rv9VZsGJae24mRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75399136b6.mp4?token=aN_5WoTart5rJlV2eq6APrZlFG01yohvIW_7RLpUKaQxZ7SRuohvwi_N0ijip-lOE1KWsLkw3tfZTomCjd1MqrJHLxP5NM8SdY0xGdfF7yWZRCTFoqpig51Zjen0DA17ciQOVewnkI1shSZA8aRfvxPJ79fyBu9UESsVOtJeL-6xz7sLLro9zeuFCizpnAC5zHWKG3Vej_sqpaxp0Iv6wINlVYQaIwyjxeFvdL7QywfA3Eh-wo2bNby_fTqUrr1G7EWL5G5Ly2a73LC5jcl1eR22VyC-e3IYXUjzBVEY4Jf0Y9fQTxB4asCvCoQ6ZkvFcLtEc2Ra_pYBva-Zv-AGkpTqyPB00G8_98pmEzFJOrjVDauxzrsLg_H32Thszfpyxju3oOH1DaRaN1QbxKrN7wlZejBOuhKrUBxe0tPKpk4U1kh_zsZaEJiRyGky6TsHbGw_Jb_N4a7tcxlHseEZiigtLTiYXLFDqY3uoSFb6RNrci-8ZQFli-nMWIebqprUj_rh9gTVBOqFSITTN7rNUK0qsna_gjmM1hzEhvDsuzTbLhqjVPBylqTuAEkD_KEuGrvG7p8F-yWy2ixVD43beKXQtIMMJMXrdlfJowjNcThZ5MXWBD700CKUu65jUvEl9eUle4JXBRiuCUz_qDypXfLFlE94Rv9VZsGJae24mRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇮🇹
آنالیز انقلاب تاکتیکی گاسپرینی در این فصل با تیم آاس‌رم که حریف سختی در اروپا خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107842" target="_blank">📅 09:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107841">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‼️
🎙
محمود فکری: باید به قلعه‌نویی حق بدهیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107841" target="_blank">📅 09:25 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107840">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75fb30e6b0.mp4?token=CTh5zjOe8ho7ocAqeVU8Hivo2W-vAzQJuLnQOUCY_ESm7j8HkhRIRn1fg1Z6uXhY_AG99oMXzkVgEwY8PNkq_RzH-5b0uRhk36Ls11O1q94JPsnSyHvKMMzKejt0C8IEAQxKy0eU0aUIbX-gIdewLW0-w0CojQhve7rZf2SzFarkAV8XZCd0m0gq3OsHosn0pWNxqXjpgAkn_aBPQ8q9yi3yUf1JTEeQY6jE1Ibz-1GxsdxzJI9a8VglVR-_5OvxSOg3cAx6_pqBzZUo5cC8pXv_ukd6AXkqKDC_6kNu0XS5lb-hyyNsZF3avYrpnmnCgNnDUOXvwRxsJtp0PHqcQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75fb30e6b0.mp4?token=CTh5zjOe8ho7ocAqeVU8Hivo2W-vAzQJuLnQOUCY_ESm7j8HkhRIRn1fg1Z6uXhY_AG99oMXzkVgEwY8PNkq_RzH-5b0uRhk36Ls11O1q94JPsnSyHvKMMzKejt0C8IEAQxKy0eU0aUIbX-gIdewLW0-w0CojQhve7rZf2SzFarkAV8XZCd0m0gq3OsHosn0pWNxqXjpgAkn_aBPQ8q9yi3yUf1JTEeQY6jE1Ibz-1GxsdxzJI9a8VglVR-_5OvxSOg3cAx6_pqBzZUo5cC8pXv_ukd6AXkqKDC_6kNu0XS5lb-hyyNsZF3avYrpnmnCgNnDUOXvwRxsJtp0PHqcQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇮🇷
فوتبال جا مانده ایران از امارات، از زبان شهریار مغانلو؛ دانیال اسماعیلی‌فر و برشمردن مصائب هواداری در کشور ما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107840" target="_blank">📅 09:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107839">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e551facae3.mp4?token=rms7ly4MwnBjjJePtn-XhZaacxrEWcO_C9rSH9isKkUNiOAf4X3-x6oSNncLxZl1S_umSHxZxiz3Q5pOGkIxQG4rqYyz4X4s0acFC2ZCCQw0JugXlPR1ncJ3ZBev3OP0I3XY8uLQZRYZhywBEuyqM3ugqaBy3Be2zEakTgS21jKI2pldxu1LeCHprDDFvauO6lKI6XcVUPyz3CoefHmve-kyCIprGRxmQU6IcjqKKfwvKwHJHJbdDMUeRiQu5ZEkDYdSFVJgiSSbHbgnFnL2sQOUa3n975CvMU5LvvKt28tNeAeJTcxfawbrIaypKql9II0GTh3_v4SGzpeyjLUyiIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e551facae3.mp4?token=rms7ly4MwnBjjJePtn-XhZaacxrEWcO_C9rSH9isKkUNiOAf4X3-x6oSNncLxZl1S_umSHxZxiz3Q5pOGkIxQG4rqYyz4X4s0acFC2ZCCQw0JugXlPR1ncJ3ZBev3OP0I3XY8uLQZRYZhywBEuyqM3ugqaBy3Be2zEakTgS21jKI2pldxu1LeCHprDDFvauO6lKI6XcVUPyz3CoefHmve-kyCIprGRxmQU6IcjqKKfwvKwHJHJbdDMUeRiQu5ZEkDYdSFVJgiSSbHbgnFnL2sQOUa3n975CvMU5LvvKt28tNeAeJTcxfawbrIaypKql9II0GTh3_v4SGzpeyjLUyiIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥶
🇪🇸
جدیدترین پدیده آکادمی لاماسیا بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107839" target="_blank">📅 08:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107835">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8fS0IDnk0eln0M7Gq6YBTjrN-zecD4gHBf6QRAFk2FkVDx0H9QDuvv1ya1Ek-E_U8e4dLIWnDVhnoAV9Mdo8C0fyi6cRNc8xJ_HIdMS2JJpLpeieLbdFdd1M4L0xQMcPmYF3hmofBqBZcOHQQo6WBMci00KCZCjhx8BPyMpenpRKWTdIexa9wsEcV-qiCEHmKlcwCeI4iXHxEMjbHZ9k0T4GycBA8G8-MCVyrHXy8lnzEIAbv907-ngIwqyqzpt6W0lVsJTtDnFtyAD3PzBi5wMFHjQQBDHbWUUEG7k7-g3OWpL9KeUTSp67Q88M3PYdPqyRAtzee6J3YRn3VVqrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🎙
🇵🇹
ژرژ ژسوس سرمربی پرتغال: آنچه بین من و رونالدو رخ داده یک سو تفاهم است که به آسانی حل می‌شود. البته این بستگی به تصمیم خود رونالدو دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107835" target="_blank">📅 00:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107834">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNa0E2pJ-XyQPwcJCRy8XuCf0LjVFfuFJ-2ks45-aRN7R4KMJ1uxu8LGG961iyo8mdV3nZ_llRZIiLHf-DpzQRx-xQQWACUTKj86kWbLwwMqhGmUMtI-3BC4Q2PNwEkcAyDO3APcPtsJdyOD6nCfTo2EAsDj08eAXLXo3a_Xdc7XdZdOcFRYoL94DyZbE-gof9f76AtMfJyyseRhnofou6rcwmyKZqEAj8Zt0DlDlJ6E64sFzI2vNkvQzyi74L5pUN_tjqhsOletA5E0MwRhTDgAijLMbq5Bccy1NWHETB60d7xkJlRYGs_VHp4GGKfLNpib-S21Y1XDb-6aa-PW6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
تیم‌ملی پرتغال به مرحله ¼نهایی لیگ‌ ملت‌های اروپا صعود کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107834" target="_blank">📅 00:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107833">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e30d963cb6.mp4?token=eRJ7MFvuzqM8cFBbjnqFvqpDjemxi6JK-mDtQYC2_CEZvl_2XFIoG_-kmhoRrX9Ed2QwMtW2sxtywf-6kdR93eTq-uPHv7tzD0Rzoo_Y3CugCIB7RAJ9atTQzfqbotoL2FrIe-BFMxqUu2NGvs9mW2N3ZNZUyYSvT_dPSSm4X10bPL45xBznXPySorSxFDpYaxK_VC9XRtdyL7P3h3v59pCWzfv8KntxJijBU-MbrcewzB2YoqcXV6ZvJ9zcr7u91TkIoEWrtL6rlK_d08-NVzqg7f1V7iAJyDtSZ5KBKOBdTIA9w0f2104XVs40bcBY6qbQnhse4Vs_cqLkQ1I30V3AlnIHfe_GduYG-5KQo3jPt0068hFzRoDgknbI4jdAsEYrGpMgVFsMbqrXjTd3sWKPNChaAXcFNTSCo-N0sL9aSUayulMHwMe5BZdDRuVoTf2uzB29Jv-2ApMCCvHiJ2oxiBc-9e6g1Gn1b6zouLMrE_xNbr1NJc3pSV-4fHUrCNz7M91_idNCX9AgvMlnxAj_uuzH3n61eg7lfnOZcDOCq2-pkJlcANYWiRkgV5rkFALutaxK2tlHkrcwJBNAjE6VtcF9fwu6UN9SkL6tkw6KWRTyF1p_n_6ZQ_YhmEGCE-O3ZnzTKOomiybjkHBMSv-FbEMCaLiunSDCMDh5yCk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e30d963cb6.mp4?token=eRJ7MFvuzqM8cFBbjnqFvqpDjemxi6JK-mDtQYC2_CEZvl_2XFIoG_-kmhoRrX9Ed2QwMtW2sxtywf-6kdR93eTq-uPHv7tzD0Rzoo_Y3CugCIB7RAJ9atTQzfqbotoL2FrIe-BFMxqUu2NGvs9mW2N3ZNZUyYSvT_dPSSm4X10bPL45xBznXPySorSxFDpYaxK_VC9XRtdyL7P3h3v59pCWzfv8KntxJijBU-MbrcewzB2YoqcXV6ZvJ9zcr7u91TkIoEWrtL6rlK_d08-NVzqg7f1V7iAJyDtSZ5KBKOBdTIA9w0f2104XVs40bcBY6qbQnhse4Vs_cqLkQ1I30V3AlnIHfe_GduYG-5KQo3jPt0068hFzRoDgknbI4jdAsEYrGpMgVFsMbqrXjTd3sWKPNChaAXcFNTSCo-N0sL9aSUayulMHwMe5BZdDRuVoTf2uzB29Jv-2ApMCCvHiJ2oxiBc-9e6g1Gn1b6zouLMrE_xNbr1NJc3pSV-4fHUrCNz7M91_idNCX9AgvMlnxAj_uuzH3n61eg7lfnOZcDOCq2-pkJlcANYWiRkgV5rkFALutaxK2tlHkrcwJBNAjE6VtcF9fwu6UN9SkL6tkw6KWRTyF1p_n_6ZQ_YhmEGCE-O3ZnzTKOomiybjkHBMSv-FbEMCaLiunSDCMDh5yCk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
گل‌دوم پرتغال به نروژ توسط گونزالو راموس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107833" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107832">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e974e0edb0.mp4?token=pv9mJmHB0rK0KEvRDD1bq1gCj6wxZa_unT9iJ9MpieKDQczQuITrX-epfrL8IxP70ZzAczDPCNGwCzXZpMp7e4Gdt6ZjaWvzq3FOn3o4wlLxn6C6aToie4oGrlpWSMl1OHLUwEk5qNWFQZc6hofM_s39w67-S9PPDwV9TXmTo9Q5kQyoSZ34k5MvWadkiNnSiM9HMEmvK_jMKggQQcj-IeGxs2avsfhUiUkGmi1qhD63ZRbaK5zQYepBMDPiFbQq3eTW-YlHNd9icy73Z1n1-pQHmVcT4ZS28KDRLleJBgo3mKYtBazX-GCjbMHK3PPdh-CJwUQmucj7IuULUBxyYoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e974e0edb0.mp4?token=pv9mJmHB0rK0KEvRDD1bq1gCj6wxZa_unT9iJ9MpieKDQczQuITrX-epfrL8IxP70ZzAczDPCNGwCzXZpMp7e4Gdt6ZjaWvzq3FOn3o4wlLxn6C6aToie4oGrlpWSMl1OHLUwEk5qNWFQZc6hofM_s39w67-S9PPDwV9TXmTo9Q5kQyoSZ34k5MvWadkiNnSiM9HMEmvK_jMKggQQcj-IeGxs2avsfhUiUkGmi1qhD63ZRbaK5zQYepBMDPiFbQq3eTW-YlHNd9icy73Z1n1-pQHmVcT4ZS28KDRLleJBgo3mKYtBazX-GCjbMHK3PPdh-CJwUQmucj7IuULUBxyYoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
سوپرگل‌تساوی پرتغال به نروژ توسط ژائو کانسلو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/107832" target="_blank">📅 23:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107831">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2872cf61d0.mp4?token=eWuzlDeQM8BGsWYD3GUkvnp7lIL_7wy3c2Dv54MepH1O4LxMJqs2-n6JX1mD2j_nRHXIDjWTR_y_v9TQIrHHw7Vtm0-MsEOAJ2xZ8xAHL6yMSNRoiUlPEkLMCpJlwndJX0u35mz0x7rKbzxqWuJ5XasMSxKVNp0kGXPK32ZYY3-LzBdnAZPso7gTLiCcsXXZZnqRZk_WJEKKQqjRLKYBVyWzgwzFDxDAvDs09lA-S8Qp1vnR7GVK7iV_FbuZknD4vs6hio7gzvhB8T2O_rpAuCT7dBOoSGM4K7-rUHm_f_wTB9SjVGK5Q4BZVWbFokcZP59IZsUNHo0pXptlJy820CLu_3dlLAC08vRzdDr3FsNJD2-F1bgAU6CS53uUnsvlEFgPNzJynJ5tVMlUgDwws3wqgZEdK7GmepCGnab4Et0HfsjywEtCKpuizsxMhSkCFk6mlGmyB4nUrBXAS3SThiyUX2i3UFxXkOswRXe_Vh8pTi2SqezluGrXL8awbU3CNyvRON-V0KA_KDbAPeapK0WYYYyCbKAjcZ2OeBGdGlKROU_TNa4bVa_PicjA14_wPczSkOKH_MZHMNZN58aatyLJirmBU7CfD34Ss5TVxBH8mbYy6rT5fzNPUgJtknM_pjnSyUZPmgEC5lxqt_Pt7Az0qcoD5KIvDfYQUl-HlIM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2872cf61d0.mp4?token=eWuzlDeQM8BGsWYD3GUkvnp7lIL_7wy3c2Dv54MepH1O4LxMJqs2-n6JX1mD2j_nRHXIDjWTR_y_v9TQIrHHw7Vtm0-MsEOAJ2xZ8xAHL6yMSNRoiUlPEkLMCpJlwndJX0u35mz0x7rKbzxqWuJ5XasMSxKVNp0kGXPK32ZYY3-LzBdnAZPso7gTLiCcsXXZZnqRZk_WJEKKQqjRLKYBVyWzgwzFDxDAvDs09lA-S8Qp1vnR7GVK7iV_FbuZknD4vs6hio7gzvhB8T2O_rpAuCT7dBOoSGM4K7-rUHm_f_wTB9SjVGK5Q4BZVWbFokcZP59IZsUNHo0pXptlJy820CLu_3dlLAC08vRzdDr3FsNJD2-F1bgAU6CS53uUnsvlEFgPNzJynJ5tVMlUgDwws3wqgZEdK7GmepCGnab4Et0HfsjywEtCKpuizsxMhSkCFk6mlGmyB4nUrBXAS3SThiyUX2i3UFxXkOswRXe_Vh8pTi2SqezluGrXL8awbU3CNyvRON-V0KA_KDbAPeapK0WYYYyCbKAjcZ2OeBGdGlKROU_TNa4bVa_PicjA14_wPczSkOKH_MZHMNZN58aatyLJirmBU7CfD34Ss5TVxBH8mbYy6rT5fzNPUgJtknM_pjnSyUZPmgEC5lxqt_Pt7Az0qcoD5KIvDfYQUl-HlIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل‌اول نروژ به پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/107831" target="_blank">📅 23:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107830">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d1f2465c.mp4?token=QFDo55nm6N0W4P9pc8EhoCLJ-2HJ1wMmw_Am_b5m-nDCDEe0SzYsmxNZeJmrJswdy9ZxRI3kpNGwcU04av-UUKKHdWq4wNoqxxTz_t8GWgBD9CPTwWYgmsirAjkX0_D6YvZhNK9H6ynIwal-OKc--K72eZ1SuWTciQivPLstfl1B-WypzfeVyhi0EmDv81pHwzAm-ck7kjQqPvI38MxdEHzPybAoXAbtisU8-KKIJnlIZYcbOYbZqx_9QTFoqLHXECadhVOLtVjnZ5KVW0-YO6q07au5bCNvGFS2fyOM66IH5a5ZpXnUYjrX_e82DspWUj2RqLm8DJ5XXx-F9IhXljlxxfhVzbyTP-PskoEJohd2yHIAiyj4nWIidlaJuCqEdaKUNUFLp89xkIKqty6MLhvsjofrZgZYWsJacXSysn7LiavyLJ_MmlKvkQLOt4Yeu-KtkarV67PQCtUXsJPdFdV2Mru5TpHPUcBkstSHNBdbzC0um59VQm9liPuPMw4w7iJTp6CfiFiv-4lNSjPAkEUxyoMe6fNvDqj5QlIkS3QnkEW82SBRJoKxt2VKkKmZ2HfcuOjyMIw-zQ3NAtObtilKA6OTFhmT3MQfi71oyau9XaqWH5w2iB4DB21dU6Vp0Ih8aEgxUY2bxJBbS_bWKCZ40ycZHwWjDRmeEmqitAY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d1f2465c.mp4?token=QFDo55nm6N0W4P9pc8EhoCLJ-2HJ1wMmw_Am_b5m-nDCDEe0SzYsmxNZeJmrJswdy9ZxRI3kpNGwcU04av-UUKKHdWq4wNoqxxTz_t8GWgBD9CPTwWYgmsirAjkX0_D6YvZhNK9H6ynIwal-OKc--K72eZ1SuWTciQivPLstfl1B-WypzfeVyhi0EmDv81pHwzAm-ck7kjQqPvI38MxdEHzPybAoXAbtisU8-KKIJnlIZYcbOYbZqx_9QTFoqLHXECadhVOLtVjnZ5KVW0-YO6q07au5bCNvGFS2fyOM66IH5a5ZpXnUYjrX_e82DspWUj2RqLm8DJ5XXx-F9IhXljlxxfhVzbyTP-PskoEJohd2yHIAiyj4nWIidlaJuCqEdaKUNUFLp89xkIKqty6MLhvsjofrZgZYWsJacXSysn7LiavyLJ_MmlKvkQLOt4Yeu-KtkarV67PQCtUXsJPdFdV2Mru5TpHPUcBkstSHNBdbzC0um59VQm9liPuPMw4w7iJTp6CfiFiv-4lNSjPAkEUxyoMe6fNvDqj5QlIkS3QnkEW82SBRJoKxt2VKkKmZ2HfcuOjyMIw-zQ3NAtObtilKA6OTFhmT3MQfi71oyau9XaqWH5w2iB4DB21dU6Vp0Ih8aEgxUY2bxJBbS_bWKCZ40ycZHwWjDRmeEmqitAY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
در مورد شکایت از یاسر آسانی؛
🎙
حدادی: چیزی که عوض داره گله نداره!
🟢
نامه فیفا به استقلال را خواستار شدیم
🟢
مدارکی داریم که بقیه باشگاه‌ها ندارند
🟢
آن سال هم هواداران استقلال قهرمانی آسیا را از ما گرفتند
🟢
رفتن کامنت گذاشتند عیسی محروم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/107830" target="_blank">📅 21:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107829">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2aee117f1.mp4?token=t5gCGrP3To1cPSBko2uzrgwx3LsKiewXUzM_OQehZyhBVgfjYvL7jHdfWGzxz3ya4-lgvXVgKCex1AgtcRmQPjQpcjK5QG93OFOLAcSe8q52DIq04M2ByaT117B-T7jnBqMpYkjY-VKviUz_0DWrbkm4ZKFWgV-aJmtFOFkAWacMYe-Xd5uqQ6HL5vWBt_sU5v4qU3B85gR-Y-ulsyrxONLBGqXvxf_CioIzoADZ8T85Jp9C91nlnv1jwB377uJE0RUrJlG1Qvy-ZF98Zju7BMULiA4ZlDja_SKjspuMjilcx9E_5ENWC2Wg1vc4r2uaEYaeb4L7lEdtYseRXQlXOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2aee117f1.mp4?token=t5gCGrP3To1cPSBko2uzrgwx3LsKiewXUzM_OQehZyhBVgfjYvL7jHdfWGzxz3ya4-lgvXVgKCex1AgtcRmQPjQpcjK5QG93OFOLAcSe8q52DIq04M2ByaT117B-T7jnBqMpYkjY-VKviUz_0DWrbkm4ZKFWgV-aJmtFOFkAWacMYe-Xd5uqQ6HL5vWBt_sU5v4qU3B85gR-Y-ulsyrxONLBGqXvxf_CioIzoADZ8T85Jp9C91nlnv1jwB377uJE0RUrJlG1Qvy-ZF98Zju7BMULiA4ZlDja_SKjspuMjilcx9E_5ENWC2Wg1vc4r2uaEYaeb4L7lEdtYseRXQlXOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
👍
🎙
تمجید و حمایت زیدان از رونالدو:
"فکر می‌کنم اتفاقاً باید از کارنامه فوق‌العاده‌اش و کارای استثنایی که انجام داده تقدیر کنیم. اون باعث شد ما جام‌های بی‌نظیری رو ببریم، پس به احترامش کلاهم رو برمی‌دارم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/107829" target="_blank">📅 21:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107828">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af8a71f26.mp4?token=MqoGNKbdPcTcV7Kfnw_lj90v04iGUVud3Q5CA5AZc6N5msa8RPOWSRy6vxb5QKK-W8Lm2y7PG2d_dfTWDG8rTm260xpKdbMGZzLqrAMYnB3q2p74WiBWawNdI-dLF6mEJADD9wYUN60rXIbwjo_Kpldto4AsGjUEBk1K1Wl6MixlovpXH9f6SG-_X7YfGkxV6NDDDOfWzz9_cP7IzHpq_g7Z7XFd3THbipg6tUNJTRT6U_i2m7CVN_CnILpUKzA7gyv8OJo6ekD9AXGU4G1yORwaPCc8iBUTw1cUIbfHAKqwFyKBbHdET-JTZMGXiqD589L43YmnkWp6WEZvVO9STw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af8a71f26.mp4?token=MqoGNKbdPcTcV7Kfnw_lj90v04iGUVud3Q5CA5AZc6N5msa8RPOWSRy6vxb5QKK-W8Lm2y7PG2d_dfTWDG8rTm260xpKdbMGZzLqrAMYnB3q2p74WiBWawNdI-dLF6mEJADD9wYUN60rXIbwjo_Kpldto4AsGjUEBk1K1Wl6MixlovpXH9f6SG-_X7YfGkxV6NDDDOfWzz9_cP7IzHpq_g7Z7XFd3THbipg6tUNJTRT6U_i2m7CVN_CnILpUKzA7gyv8OJo6ekD9AXGU4G1yORwaPCc8iBUTw1cUIbfHAKqwFyKBbHdET-JTZMGXiqD589L43YmnkWp6WEZvVO9STw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🎙
پاسخ علی چینی پیشکسوت استقلال به مالک تراکتور: ما از منیریه جام بخریم؟ بیا تهران از نزدیک جام‌ها را لمس کن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107828" target="_blank">📅 21:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107827">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56554104cf.mp4?token=j2Nb-is624Tml-6i-MQmTMxPZTCMyQTy8Yd3PWb3SS4Yg4By1ak4O1rbFlPzZNC3IlJ7fbyn9LgmZJFDhdb13MTgRyeBfvKn-wlTkcSXb1FRAdnbdiJDX3L6yskrQt9AqbdvCBTJSrQzh9wt0To1z2ZjigP0EUsHRGVwpci1LBkCf3PqM8VN2Fhtox_VbfRVOhkG2tGkg67_w4jQgAyqMsjcDCTYhCRaeQx-OMYa7KiQDR-DzHAVwFFZI-GbVgXNFU5inJozFUGJtmeAMEM8x-Dzyk5Or4ni0-lcqF4DCn71eAlMlMoVLoNqXOLlHIGkzOvqYkoGL8niFTRoO86rzr3PedCvf3JZ9taAuFb1CFvQ9NjiIoJtxiihMM7ZC2RI2nLgLnEXoSU0Hu96xpso4Q4C6i5IFGSkLMqGNy26khmK8xR9z5-MZSHvyMxs_ejWjUVgvgWzCeo1eLyB9tgQYOsWOv7egLtibOrYRmtNx2mxnbQnqUy_90JiuHUwZ6I6Ze6XmTQgCuQ8e4nlh6WnEpjSF3lDYDRkbAksM1v-LcOc-CViDfV985vJa-O0xXOazCEC6UsF46KdMIQaw_GFDYJvZUZ1NI9FcpplTOb9enhH0WA92mrt1yKvKu1KWhaf5VxlDcs8vHE05rmu5B1_eXwpphEQyI9yL2YRi_iClAc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56554104cf.mp4?token=j2Nb-is624Tml-6i-MQmTMxPZTCMyQTy8Yd3PWb3SS4Yg4By1ak4O1rbFlPzZNC3IlJ7fbyn9LgmZJFDhdb13MTgRyeBfvKn-wlTkcSXb1FRAdnbdiJDX3L6yskrQt9AqbdvCBTJSrQzh9wt0To1z2ZjigP0EUsHRGVwpci1LBkCf3PqM8VN2Fhtox_VbfRVOhkG2tGkg67_w4jQgAyqMsjcDCTYhCRaeQx-OMYa7KiQDR-DzHAVwFFZI-GbVgXNFU5inJozFUGJtmeAMEM8x-Dzyk5Or4ni0-lcqF4DCn71eAlMlMoVLoNqXOLlHIGkzOvqYkoGL8niFTRoO86rzr3PedCvf3JZ9taAuFb1CFvQ9NjiIoJtxiihMM7ZC2RI2nLgLnEXoSU0Hu96xpso4Q4C6i5IFGSkLMqGNy26khmK8xR9z5-MZSHvyMxs_ejWjUVgvgWzCeo1eLyB9tgQYOsWOv7egLtibOrYRmtNx2mxnbQnqUy_90JiuHUwZ6I6Ze6XmTQgCuQ8e4nlh6WnEpjSF3lDYDRkbAksM1v-LcOc-CViDfV985vJa-O0xXOazCEC6UsF46KdMIQaw_GFDYJvZUZ1NI9FcpplTOb9enhH0WA92mrt1yKvKu1KWhaf5VxlDcs8vHE05rmu5B1_eXwpphEQyI9yL2YRi_iClAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
پیمان حدادی مدیرعامل پرسپولیس: ما زور داشتیم و تورنمنت سه‌جانبه برگزار کردیم. اینکه قهرمان فصل‌گذشته معرفی نشد کاملا منطقی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107827" target="_blank">📅 20:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107826">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇷
۸۱ سال گذشت؛ کلیپ ویژه سالروز تاسیس باشگاه استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107826" target="_blank">📅 20:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107825">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKsEoejUzty2TzY4Skhj2I6g0b2MseeYJvGm009_7ReaGgwK_Wm59o1QVk0zKeqHfUQJkzMfxX2m_0NCROHzXiB8kWV89YcQHuJt5UbRpcxMJMgfmxCU5UCLp7XQqwu9zAYOpIUxqSW6HV2zQBIhpfxeQya4NVoSgkx1mjJTilPZxCUzd3LFxrEI25whgcoNRRo5RGNFW6UN7Hh1O-j2TipOI75xqR8kJSu3nkUrv_I-pihfowXFqW5CKGUfmPUsyeZ1FT-K6PvUUWKWxcvm8Mxh2BlAHfb9_y_tiBV3jzGutNakHn_yOPrE1jOixnS7AnBDzndnb6YYvHjY_uD9gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
‼️
پیمان‌حدادی: قرارداد اورونوف را تمدید کرده بودیم که بتوانیم بعد از درخشش احتمالی این بازیکن در جام‌جهانی این بازیکن را بفروشیم ولی برنامه‌ریزی موفقی نداشتیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107825" target="_blank">📅 20:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107824">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‼️
حمید مریخ مدیر برنامه یاسر آسانی و نزدیک به باشگاه استقلال قصد داره که شیرزاد آسانوف هافبک میانی 23 ساله تیم ملی ازبکستان رونیم‌فصل به تیم استقلال بیاره و منتظر تاییدیه بختیاری زاده‌ست.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107824" target="_blank">📅 20:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107823">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50712b5d4b.mp4?token=VM6YDNCBFPKlgJh30ZHLXf7VkPQKacPAHGhuoOH7nALG2Tri_CVx5kpwNQF7Net7jXCO_DLNT33phIbp_hvAQs9cw2VCTC8BpQ-mmpGT3F_gWlUjgOdLVYwin7vSce4zbE0a7gDUBfH9Nyjp654Ri1QqDklDiuO57nReln8g0tsOVf9Qv01xvdsNCoWOTwdYBZxFLyK-DoRe6ZloECuNDZRMcIPSMJ1iqSRMwXvEOtmiPkEToIo6gmH-M58_VR_LcMo60gX4USNaaQfC_VL204qIq0LPtZnt2Y9MwZPEtT4FAoyQbo_Wbe9k3GbvZNtkGYR9GF4FRGJdV5Kc29-Ylw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50712b5d4b.mp4?token=VM6YDNCBFPKlgJh30ZHLXf7VkPQKacPAHGhuoOH7nALG2Tri_CVx5kpwNQF7Net7jXCO_DLNT33phIbp_hvAQs9cw2VCTC8BpQ-mmpGT3F_gWlUjgOdLVYwin7vSce4zbE0a7gDUBfH9Nyjp654Ri1QqDklDiuO57nReln8g0tsOVf9Qv01xvdsNCoWOTwdYBZxFLyK-DoRe6ZloECuNDZRMcIPSMJ1iqSRMwXvEOtmiPkEToIo6gmH-M58_VR_LcMo60gX4USNaaQfC_VL204qIq0LPtZnt2Y9MwZPEtT4FAoyQbo_Wbe9k3GbvZNtkGYR9GF4FRGJdV5Kc29-Ylw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پیمان
حدادی مدیرعامل پرسپولیس: قرارداد 5 بازیکن خارجی ما 4 میلیون و 80 هزار دلار است
🔴
در نیم فصل و تابستان بعدی بازیکن خارجی نخواهیم گرفت. ابتدای فصل بخاطر همین کادر ایرانی گرفتیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107823" target="_blank">📅 20:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107822">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65b6b0e4ee.mp4?token=fCHvFiyEMISAivg73V96N1XhLPR2w6Xjw9zmz4SsN7-vPlrAK9MdfD5xeXkmQVb0p02gbZzSLkUl0at2uNDXY_pPEk0w_28EkQTsG2IehkIOutp5XZ7MJi2iJRBS10hXNqH9sYQPXSY4o-h43TYRDW5AOpycriK70A9mnW8YsyhWtUUmphf2cQcaq6219OuN7E-lzEKSOOMoEnyF_ZuB_Dw9HM50DZ7mO9BfqQ2Za6KBjJiruuQvFgXDzcrUgFBaDvjUyhe_IBqov-PP0vaP3yV698egeu3xVhT48ym8PDRpr8b0mXQX7FPNO4jlHlZcM4_uRgqO4Tc67Wi9GG2JgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65b6b0e4ee.mp4?token=fCHvFiyEMISAivg73V96N1XhLPR2w6Xjw9zmz4SsN7-vPlrAK9MdfD5xeXkmQVb0p02gbZzSLkUl0at2uNDXY_pPEk0w_28EkQTsG2IehkIOutp5XZ7MJi2iJRBS10hXNqH9sYQPXSY4o-h43TYRDW5AOpycriK70A9mnW8YsyhWtUUmphf2cQcaq6219OuN7E-lzEKSOOMoEnyF_ZuB_Dw9HM50DZ7mO9BfqQ2Za6KBjJiruuQvFgXDzcrUgFBaDvjUyhe_IBqov-PP0vaP3yV698egeu3xVhT48ym8PDRpr8b0mXQX7FPNO4jlHlZcM4_uRgqO4Tc67Wi9GG2JgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
‏همسر
بیژن مرتضوی: تو مجازی به آقا بیژن فحش میدید ولی تو واقعیت دنبال عکس و امضا هستید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107822" target="_blank">📅 20:04 · 12 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
