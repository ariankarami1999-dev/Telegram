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
<img src="https://cdn4.telesco.pe/file/Wb5vikQKjnR3R064ZObBTHz1gJJuCo74W78UKpOhVvFS2Map67uxXatO8taB6JER1dNWDdtX0pdhMfysmMZxqgirDg0QiTRwZ67CR8ZHsW_VI-92p5iIsCCAFjG0B6jxrbmA0IVR3STpyV-PDjwTSMvhL2uBUwlv2KoilXLF-LfhntpGDwhks-qwkVJ2OIFOqneekX8pII0Q-D1-C0vPozQxFBzvhKZaI-BC6SqcIZijzwedTv3AwRKEatLyjBaJ1sGn3FQ-bzNd_bghF1vbMkHbnUIPbw1paApMmKXdpQsUJ7rJlDcD2N9ZWLnkW1yh-jUA-oXT2tZSVNLX1Q1OSQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 127K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 08:54:13</div>
<hr>

<div class="tg-post" id="msg-69922">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال…</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/news_hut/69922" target="_blank">📅 01:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69921">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=IMji__YcFJlviLGTI_s5j7bEjpZ5-2ZstFa9XPTpc8mj2gnY_yYHf3lkxbxZXFrex3F5s50PcMX-JgQ9bUJ1h9HFJS2qUbg3IzHOSt343eblKxTMmgP8Mt1LpsQVHQ51iw7S9DTvbvIfXnI2EacAlDOl9mFyp3LljYHywsMCpVtSIsszw4gH2cv7hRjm4DqUR-K-wn0bvKFj3I0I4isu6Mz5TdzTGU1a-b8uCE4Xc68g_LT53MX-EFNCMSwdpXYkZtWX1gpI9xZLhisOrwdFa0_ds4i4ZFpQILrbh8Q9djPen1vFu7Ic0Q2u28bNxYtTKTp6kFkk2RW2rTdi3W7TaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=IMji__YcFJlviLGTI_s5j7bEjpZ5-2ZstFa9XPTpc8mj2gnY_yYHf3lkxbxZXFrex3F5s50PcMX-JgQ9bUJ1h9HFJS2qUbg3IzHOSt343eblKxTMmgP8Mt1LpsQVHQ51iw7S9DTvbvIfXnI2EacAlDOl9mFyp3LljYHywsMCpVtSIsszw4gH2cv7hRjm4DqUR-K-wn0bvKFj3I0I4isu6Mz5TdzTGU1a-b8uCE4Xc68g_LT53MX-EFNCMSwdpXYkZtWX1gpI9xZLhisOrwdFa0_ds4i4ZFpQILrbh8Q9djPen1vFu7Ic0Q2u28bNxYtTKTp6kFkk2RW2rTdi3W7TaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a20
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/news_hut/69921" target="_blank">📅 01:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69919">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0c53c5d72.mp4?token=CDjHmWIMNl80RjVBGXHog3qk2fHnCf75eCwNoJVMPO-m0enE2_cSRU-eNnBjkxJ49p5v3YHFqlqFbmCuV1pFtKXj19jI_MjuJ6fIYPhlG2GRG3VRKO_3xUkSG_6Ww953IWjDzOI6Wzx17JnMe4ak9S6vxxB5nhq1x-WJw2R88p8MuKF8gp0ZCTyd_qIYBoyfuLZgvZ0Hu6TlYo5Ajn3tV0Mti-ubXYrUzzKOUC7vFDV6t2MrsINWwVzh8djrDB6ZxGeEccGx4II5Fw-vHPEvbiQCxWqr85iJVTP4Enyi4iUFgUaS6f903FVGebJEN0tUs8lETYoGf9TWbClrEWt8nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0c53c5d72.mp4?token=CDjHmWIMNl80RjVBGXHog3qk2fHnCf75eCwNoJVMPO-m0enE2_cSRU-eNnBjkxJ49p5v3YHFqlqFbmCuV1pFtKXj19jI_MjuJ6fIYPhlG2GRG3VRKO_3xUkSG_6Ww953IWjDzOI6Wzx17JnMe4ak9S6vxxB5nhq1x-WJw2R88p8MuKF8gp0ZCTyd_qIYBoyfuLZgvZ0Hu6TlYo5Ajn3tV0Mti-ubXYrUzzKOUC7vFDV6t2MrsINWwVzh8djrDB6ZxGeEccGx4II5Fw-vHPEvbiQCxWqr85iJVTP4Enyi4iUFgUaS6f903FVGebJEN0tUs8lETYoGf9TWbClrEWt8nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی یک مخزن در اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/news_hut/69919" target="_blank">📅 01:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69918">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c665ef2ed.mp4?token=BGLhLE2EfDQ3At4NXmIT0pJdECfDDvlo32bLKCbPcCl2cW90h2ZbZh0c2Vuo3As_LNQhZQe8LWwSoLhNNJGDj6a7deEFYhNeWASwJH3cF8QBXudOGrf7m3V3NmCcPPyiowZt4nVv5I9yXN2bcrNr0zBqBaFLOIXZAxQL4j7v6P0wmJGn_-nirNDx00OZhTnuRGzGXZ8Mx6k1reRYTxH3owDLNQ-FczLx197y44_A7SFqO4ZX2CQf0tYktrzp-PEw8KAwCOWGS8Ils_-42r3eQVSef8hSMKtGuzTk-0Lb7it7dKtamxZ3kVPdF38YAwDEpZapsEd9MR3fwW0CoOvgfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c665ef2ed.mp4?token=BGLhLE2EfDQ3At4NXmIT0pJdECfDDvlo32bLKCbPcCl2cW90h2ZbZh0c2Vuo3As_LNQhZQe8LWwSoLhNNJGDj6a7deEFYhNeWASwJH3cF8QBXudOGrf7m3V3NmCcPPyiowZt4nVv5I9yXN2bcrNr0zBqBaFLOIXZAxQL4j7v6P0wmJGn_-nirNDx00OZhTnuRGzGXZ8Mx6k1reRYTxH3owDLNQ-FczLx197y44_A7SFqO4ZX2CQf0tYktrzp-PEw8KAwCOWGS8Ils_-42r3eQVSef8hSMKtGuzTk-0Lb7it7dKtamxZ3kVPdF38YAwDEpZapsEd9MR3fwW0CoOvgfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اولین ویدیو منتشر شده از عروسی رونالدو و جورجینا:
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/69918" target="_blank">📅 01:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69917">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d80bd3b48d.mp4?token=VJDvgNFKSgOPEGDIMbx6aUoEedqNPCh5ZzAScX9g34BsalSP9aBx0qddY1dQ6iS8965PU8KsOmHztCzy_kq89y0zJ2HRF0RTV4GNWEtMKDNvTJYa1WdWZev4kcmqF_qBfdzY9rgZO218IvtHFM3iF5Nqh_MhqTt_YlUevo-jNrDInWVx5vcPXUibcG5lHU-r_mLNjc6OmDJue-wkQW12Zg7bgiq6Z6jhqAlaB4-drmDMohmqmo55xX_SlkhFufGDJcufuBGvWKTDUI1iHingAD2bCBCdZXnH6fD5xXnHCJGEmVWtmbse8paKml54MXzGSwRUrWEL8Y1aepYuwdu49Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d80bd3b48d.mp4?token=VJDvgNFKSgOPEGDIMbx6aUoEedqNPCh5ZzAScX9g34BsalSP9aBx0qddY1dQ6iS8965PU8KsOmHztCzy_kq89y0zJ2HRF0RTV4GNWEtMKDNvTJYa1WdWZev4kcmqF_qBfdzY9rgZO218IvtHFM3iF5Nqh_MhqTt_YlUevo-jNrDInWVx5vcPXUibcG5lHU-r_mLNjc6OmDJue-wkQW12Zg7bgiq6Z6jhqAlaB4-drmDMohmqmo55xX_SlkhFufGDJcufuBGvWKTDUI1iHingAD2bCBCdZXnH6fD5xXnHCJGEmVWtmbse8paKml54MXzGSwRUrWEL8Y1aepYuwdu49Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نظر محمدرضاشاه پهلوی درباره نفوذ لابی یهود در آمریکا:
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/69917" target="_blank">📅 00:21 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69916">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJELHkLyB_FIWXKu2R7vAXTSvb635MgDUc4geghaMkRoQz4Q_hkE8mU52S_Gv7FMgvIhpsKkw-9LpAc-Z69lV7LZOiNtQq8RYPBDtPcTm_EqUGkK1M70DVVmJlIL4lYJfq97A9qaYNTrJk35TwBsBOlDIuI27wN92xi2Z0XwbmVqEanQb1Rm1c3vBZYZAgI06L9jy_8uluMcGpUIeibhtcQha5l7kowrYgJbgPcX6dfv1apC2KnnujlaIxNtJKz1DhrTYMTBKTGnVkBdbeMSiA5c-SVVim-f-dmHtZKvfwUwH4JfVwdtR_O0ZBcmbL0GMy0kkJbHF4jyvBK3Lap63Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رونالدو و بانو جورجینا رسماً ازدواج کردن.
رونالدو هم گردن گرفت بالاخره، دیگه وقتشه تو هم گردن بگیری
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/69916" target="_blank">📅 23:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69915">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d1d1d4e3c.mp4?token=UXSce1fnygdLNIyfCs7ho4gKv6JtN76hz45rOhBBOIG4E7yLIfSyyT8MY1LQ8Ydl2PR6uop00_bEj3xgRh31rMlMMYMFZtviS6LXoZbGQXvzudvaysTmNP8Balinw68Wb20-7c1pLJ117V3ubTGR08wtyLIaiLq4DLDfUou5CjArerpicL23jXt87RUImyOSkmm0KDG9wp7WWMCJDpmA98DvNJeDVBMZhNRfQ_BvkyELU-mbtAOQt94YtlNQfx4W5Wfr5aM7muG78qMgiA4yPj-iCjWmO1no7f1_pkWue-1d0C9_DjlGj8_7PtsV3co9LmHuYGKD0JITwTlop6BmFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d1d1d4e3c.mp4?token=UXSce1fnygdLNIyfCs7ho4gKv6JtN76hz45rOhBBOIG4E7yLIfSyyT8MY1LQ8Ydl2PR6uop00_bEj3xgRh31rMlMMYMFZtviS6LXoZbGQXvzudvaysTmNP8Balinw68Wb20-7c1pLJ117V3ubTGR08wtyLIaiLq4DLDfUou5CjArerpicL23jXt87RUImyOSkmm0KDG9wp7WWMCJDpmA98DvNJeDVBMZhNRfQ_BvkyELU-mbtAOQt94YtlNQfx4W5Wfr5aM7muG78qMgiA4yPj-iCjWmO1no7f1_pkWue-1d0C9_DjlGj8_7PtsV3co9LmHuYGKD0JITwTlop6BmFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
روحانی:
صدام پس از کویت به دنبال عربستان و امارات بود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/69915" target="_blank">📅 23:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69914">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🇺🇸
سنتکام اعلام کرد نیروهای ایالات متحده از زمان تقویت محاصره بنادر ایران، ۵۵ کشتی تجاری را بازگرداندند، ۳ کشتی را غیرفعال کردند و برای اطمینان از رعایت مقررات، ۲ کشتی را بازرسی کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69914" target="_blank">📅 22:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69913">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaTDaFlrweW6jENPOUEmp_UQ1uByyOCbOriYgyxPfrv6_vtLZEEBeDJ_NgMMAOx3q-7rCAk4LKH07P5t3R_ywK0QjG7_nOHmOqlTrp8pN7khskWyPR7s1eyO2o6nMUUDAO22SV-WzLVDSHrTPWKSUrj9pFHVyxx0Gqv6neQgC3CBrSRtgJ7tc-4zbB8oqqLJCMaUCSuYuxEas4EbjWdK8ooemk0yVgP7xchx-mhv4wsbvZCiu6llwp54ELZx975WtEMZutNuCN6T-xV1BLkZCR94zUWYisRK8qipKvezptaYn83i1DuyEtt518r0i1K_jTl0MMG7030VH5OjKQBRjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
📰
وال استریت ژورنال:اسرائیل دولت ترامپ را در جریان اطلاعاتی قرار داد که نشان می‌داد توطئه‌ای احتمالی برای هدف قرار دادن هواپیمای ریاست جمهوری با موشک‌های زمین به هوای دوش‌پرتاب وجود دارد.
مقامات امنیتی ایالات متحده متعاقباً پس از اجلاس ناتو، رئیس جمهور ترامپ را با استفاده از یک کامیون پذیرایی فرودگاهی در آنکارا به یک هواپیمای نظامی جداگانه منتقل کردند، در حالی که مارکو روبیو، وزیر امور خارجه، دیگر مقامات ارشد و خبرنگاران به عنوان بخشی از یک عملیات فریب در هواپیمای ریاست جمهوری باقی ماندند.
در نهایت هیچ موشکی شلیک نشد و هنوز مشخص نیست که تهدید گزارش شده چقدر معتبر بوده است. این عملیات اولین باری بود که چنین اقدام فریب‌آمیزی در دوران ریاست جمهوری ترامپ استفاده می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/69913" target="_blank">📅 22:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69912">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f811c57f.mp4?token=DptFxnPWfJlHOGpCqO7KcFw-a_6851Tv6JiuggyYM22atizUhqM4TQW3u70O6gAJR18TWdj3UBCktzT06mp64CgnUB8ZFlWK454mEd8AGBUVxUn_M1ek5bjj1bZ3nVeXNgFFTQ0SiRbcqxwkB-hGt9Yl2s5smFFv_D9iLXvWfNtJa1SlH-fmmpC23ATjprHtf5uBacAenNMYeMGa_7jGNUVPnaq4bTva6k8upxQ7B4F5KJoasB065P83pG6LO641uLSJVkS3LzWQaGinzGRkvTAw8EcnAt-7YLJNw1kwIqbk3Lex6jKrZNHyMp6PyUA1krMXQw2yIJAANpfWek3pRU3J3n3AWUzIswL4vQuBor_KrZ_D9ddw48Zs0idRRVixQbBSYtEclPyiLB2Mu7tcw1Zkx5NgL-YuuJL1tM7oEC8nAqLzTK95_fS8DKB4q1ReH_23qjpx1zndRHyvdeUFSwz4cU8rbnjQGCncL7nxFxOOZDro88j4YBEKQmPmlANdC3SYRjaEfegvPQ9QBgFQztSAskyX0ucXVFQvURLBYfGckatn1fk9UPNdGKWqQXLUp9L7xED5u20ecM2w1Egq8buDvihclF1kMPt72Yp_9_UOFJRFVPqLc4assS30eQlDnKjft8HGB-rYybBzKafQ16d80L5JBUzoOz_OH0xX2Oo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f811c57f.mp4?token=DptFxnPWfJlHOGpCqO7KcFw-a_6851Tv6JiuggyYM22atizUhqM4TQW3u70O6gAJR18TWdj3UBCktzT06mp64CgnUB8ZFlWK454mEd8AGBUVxUn_M1ek5bjj1bZ3nVeXNgFFTQ0SiRbcqxwkB-hGt9Yl2s5smFFv_D9iLXvWfNtJa1SlH-fmmpC23ATjprHtf5uBacAenNMYeMGa_7jGNUVPnaq4bTva6k8upxQ7B4F5KJoasB065P83pG6LO641uLSJVkS3LzWQaGinzGRkvTAw8EcnAt-7YLJNw1kwIqbk3Lex6jKrZNHyMp6PyUA1krMXQw2yIJAANpfWek3pRU3J3n3AWUzIswL4vQuBor_KrZ_D9ddw48Zs0idRRVixQbBSYtEclPyiLB2Mu7tcw1Zkx5NgL-YuuJL1tM7oEC8nAqLzTK95_fS8DKB4q1ReH_23qjpx1zndRHyvdeUFSwz4cU8rbnjQGCncL7nxFxOOZDro88j4YBEKQmPmlANdC3SYRjaEfegvPQ9QBgFQztSAskyX0ucXVFQvURLBYfGckatn1fk9UPNdGKWqQXLUp9L7xED5u20ecM2w1Egq8buDvihclF1kMPt72Yp_9_UOFJRFVPqLc4assS30eQlDnKjft8HGB-rYybBzKafQ16d80L5JBUzoOz_OH0xX2Oo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
پرواز بالگرد آپاچی۶۴ آمریکایی در نزدیکی قشم
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69912" target="_blank">📅 21:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69908">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b1WUNPlFdZkM_HjxFoT4VJwk6WC-nMklk980PxhF44Lp98852B7wOjtg0cyZOXiAPyR96T_4p1CPVTail4-AksO2XzuNN2EMHgnRHrCvUx34ICnDeYXDsjv3CS2ltHbf5Rra_WQlXp2Zvo7uzj4BKaoJaA37dKnx8SEPlEwYutd18X-BEa3ptkkdDkgKlcdij2whV7efqT8Xvl2vMlY5Dyt7hsrq2njy4mR5OAg2WCWzVt3jMvi6GQ7seszFDXjrB0bj-nyXVKXdC9erPSsBjddnXprIP_MTu8hJdz7gN2A5Rd3LO2BWGjSF_ROzmoxj1DWc9FWYG5_ZsOsOL1Va1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qv80zNPmg5Ubj5fh6i04tpv-NWRq7h-daejE0gA7SRMLOS5hiLJ0oao5mqbBxlYogGyd908WCz6YJ9EBjQ6-N1HCEkBL6kS3mQxwFeFiC9jUNMDip8Satn4ed7BsRHBuPccizckY-TUOrhKFWrfnW659FJQe3RItgsWgQ2KXMt_Hn2I_L3g-yNOhTs34VsQ5xmfF-lsUpIayGQ1LxNt7wzYUOmXpMCsJsVF-JqJldJn_TF8_8tIwPZk2G6x1u6KJ_WwiSZs6xCx1ZGJk1tIo3OZTMQkuTQB-KOWDEcN8aPImMc1WHOrv48tmI9LQVX2U_mAuQ-L9473iH9gJMwAvqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RDFYdFDC5tvxqyGFJ4IxEP7CRhvvm8d2QKmWlfewvIk_iNWgdjlEPwRROu8H5RAfHwCic25IGbJmCyR9amklNEvnuaA2cujRaXDHihkVxASUCG_HfWwiz85vA4bGipIiRwexsbhzpprgWCTNYDoiuntbvaR7HQRz0nELOHC_g-6XEfabbpQqz3J4xoKcKr8Op2ichIy4-hiUVg-1ANgoC987Ko01YGxPHI7kv9Fun2AngP-8bOyJmGAX6ABIvCxtfE7X_0QgUEhtFp8fDnnhF7j1IS-UUYNrvqCJRN2ViITW0an-Dw1wpJRk1XkQpM8cBrt-ohIKSw7RODv3djPlLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbbe5c4282.mp4?token=hyjBIDsDZV9N4eP4HsAYvkpjjmFkYKHdfszekCOV9L-PVzysureZnvQVw3ztKUMfUGkK-gcFEeg4IWpqCTLeTn5nQcU9-7HVQ0qlp5-lY2dSLXTIzMRFfe0Bq88Ix0HlkTd8Ntd_cH_RA0hTHVlYDhpzdWc4nTvjbaEKNHto-jF7i3erl09nckZhnB2WOgPhhZw60ETyQvRMJKMZlQ_d8RGEBBXZ4cGyf4bTI7LHq8L09YWfDr6mc1s3WBr_7r_FydAuPf8j8n4r8xcFVRlppCpFPgXJQaoRrnkvYjjIpws2ZghQTX0JhNMDItH6rLEulmI4aGoswp8B3cOM3-uC-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbbe5c4282.mp4?token=hyjBIDsDZV9N4eP4HsAYvkpjjmFkYKHdfszekCOV9L-PVzysureZnvQVw3ztKUMfUGkK-gcFEeg4IWpqCTLeTn5nQcU9-7HVQ0qlp5-lY2dSLXTIzMRFfe0Bq88Ix0HlkTd8Ntd_cH_RA0hTHVlYDhpzdWc4nTvjbaEKNHto-jF7i3erl09nckZhnB2WOgPhhZw60ETyQvRMJKMZlQ_d8RGEBBXZ4cGyf4bTI7LHq8L09YWfDr6mc1s3WBr_7r_FydAuPf8j8n4r8xcFVRlppCpFPgXJQaoRrnkvYjjIpws2ZghQTX0JhNMDItH6rLEulmI4aGoswp8B3cOM3-uC-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دریک، از بزرگترین خواننده‌های دنیا؛  با 140 میلیون فالور و ثروت 250 میلیون دلاری [50 هزار میلیاردی]  وقتی ممه‌های بزرگ یه دخترو دید، نتونست تحمل کنه و براش هاپ هاپ کرد  @News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69908" target="_blank">📅 20:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69907">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bcf8b7227.mp4?token=GDAb3PLrKQW5fhvI-pEU-NyOTkmpnSSoDgVQg1y-TLTw0ZRo3MTsV8QU0gSbsLjpVLPJ9Dxoa-pLs5FVgfpDzSPtdBzkbIHs1Y0TS7UXYBW-Q2lJ58a9wqvTBVByd_K2RtJAgJfjCkclEupTK_qAj1XzVLa1K2kK9CBo6D7Ri8Y1vEXYZMsuPmYmaANi79KFOwtnRph_tTECIRdmCZ6eh3gO9PnP2YFZWC9adb9v6ds48RUtBGrah3Y1dBNmehmr1LHR8FNj5HuKTsXRU_DNVT5A-X_GOBKl1euuEMKssrVnr6ws-dcChlm4_jm9N5yzZO_qv4iD0BPYBku688Pnkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bcf8b7227.mp4?token=GDAb3PLrKQW5fhvI-pEU-NyOTkmpnSSoDgVQg1y-TLTw0ZRo3MTsV8QU0gSbsLjpVLPJ9Dxoa-pLs5FVgfpDzSPtdBzkbIHs1Y0TS7UXYBW-Q2lJ58a9wqvTBVByd_K2RtJAgJfjCkclEupTK_qAj1XzVLa1K2kK9CBo6D7Ri8Y1vEXYZMsuPmYmaANi79KFOwtnRph_tTECIRdmCZ6eh3gO9PnP2YFZWC9adb9v6ds48RUtBGrah3Y1dBNmehmr1LHR8FNj5HuKTsXRU_DNVT5A-X_GOBKl1euuEMKssrVnr6ws-dcChlm4_jm9N5yzZO_qv4iD0BPYBku688Pnkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
رامین رضاییان:ما خودمون از عمد به بلژیک گل نزدیم و تیم بلژیکو نبردیم.
🔴
چرا؟دلیلش:
جلوی بلژیک شما دیدید مهدی طارمی یکاری کرد تیمه ده نفره بشه.
مهدی بخاطر تیم به بلژیک گل نزد.
من باهاش صحبت کردم داداش چرا نزدی گفت داداش اگه گلو میزدیم فشار وحشتناک میاورن و جبران میکردن، حقم داشت مهدی
🧠
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/69907" target="_blank">📅 20:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69906">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🇮🇷
فیلد مارشال محسن رضایی دبیر عالی شورای امنیت ملی:
آمریکا باید جنگ رو پایان بده و خسارات رو بپردازه.
به هیچ وجه کوتاه نخواهیم آمد.
تمامی جنگ ها باید در کل جبهه مقاومت پایان یابد چون شرط اصلیه.
شروط دیگر را نیز از طریق میانجی ها گفتیم به اونا ک باید بهش عمل بکنن.
توافق با عمان ربطی به باز شدن تنگه هرمز نداره.
پول های بلوکه شده باید آزاد بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/69906" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69905">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی We pari همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/69905" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69904">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/si5K2npmDngoSkXO-2TisKJqVVaT4L5pFjMwbVHLj8V3xqVYCOMMHfTvgih9AA61O0LaVHJIj2JImoBE4XKuRzqeU7T0RozD_sIPCiim9duSG9ICESNIIx7tCDQlibe3ze6dtS2RzneRNId6ZMxxGAUGNJeitxv5HyWvr8wDLdn3lqFSwqPi0_LVDwK6KEY8CZ63OeogCKwbipCHFg6_I4swszxGX-IZdKAqqu18ovOB9VvzfU3zGS37m7emwAsU-Z1_o7e4TlxI9xsCbV-wgV_7a3uSl186JE1a7ZQmK8MF_XNkVaHzh4l9nVdKwlokVfWww0tKm-5hTzwhK3Qz3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/69904" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69903">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e58dcb779.mp4?token=lBV4ToCv3YuwX4SYEqBs8ci3i00nrf4N28m1W5VKRrl9W8kvtCwG7-P5FjmEwmWybXgeWe0zX3xAxZ69RR3bvgja2kG7aoo10R3tx_LXft_4DYA0zT8vtWrQbvaVO9qC9ZJ3RpquQJ-AdpBNgwRVysUrQnEwKUtayVKPlccFcftMCa4-o2Xy3UX97C6ZBwYrMJkzwmvbKLmEZ0LbtNwNqwDkCxfgutpLeivFFFQzpvVNY1ewY3oFiQSGAqNT4BdHSYXbqpjb09TEkzPdyFDLgKa-RuIu-cobGPPS6Tgu5tFmrtBSa5z5TIp4ODZjvodadUP_q1-vx4I_P09qhY_aFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e58dcb779.mp4?token=lBV4ToCv3YuwX4SYEqBs8ci3i00nrf4N28m1W5VKRrl9W8kvtCwG7-P5FjmEwmWybXgeWe0zX3xAxZ69RR3bvgja2kG7aoo10R3tx_LXft_4DYA0zT8vtWrQbvaVO9qC9ZJ3RpquQJ-AdpBNgwRVysUrQnEwKUtayVKPlccFcftMCa4-o2Xy3UX97C6ZBwYrMJkzwmvbKLmEZ0LbtNwNqwDkCxfgutpLeivFFFQzpvVNY1ewY3oFiQSGAqNT4BdHSYXbqpjb09TEkzPdyFDLgKa-RuIu-cobGPPS6Tgu5tFmrtBSa5z5TIp4ODZjvodadUP_q1-vx4I_P09qhY_aFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
روایت تلخ یه فرد نابینا:
اینکه من نابینام به عقیده پدرم کارمایی هست که دارم بخاطر کاراهای اون پس میدم.
پدرم وقتی جوون بود نابیناهارو مسخره میکرد و بهشون میخندید.
مثلا پدرم بهشون میگفت بیاید جلو بیاید جلو و وقتی میومدن میفتادن تو چاه و پدرم مثل خر بهشون میخندید.
پدرم بهم گفت من این کارارو وقتی جوون بودم انجام میدادم.بعدا وقتی تو دنیا اومدی دیدم نابینا شدی و این دلیلش کارمایی هست که من باید پس بدم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/69903" target="_blank">📅 19:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69902">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfb370d6c1.mp4?token=HzYiZY1sqVLIqKjNol8p-jllT7FckJ2lHwXEzmWLcHOLRSOeDaOuczem-opuAtPZ8TDrlBtRgXSW4JOMEDQIez7_a-rIvTaGOo4iuHGsyvRK0Zx9RVzga0dqV2djTaahIRiwSGaZ9YULIgiZCLQ1q_2zxilmTaXiVw0yQj4jD5PaeYX-olWAOXxuLA8D7muVNA6uDBXO1XLcUP3vcfS5TmayBD1ZTXxu0E-nYjxJffXI0j8w8ccFKNnvbSYsNm3me7JFljLQW4fNDLe-PezoViahTyJefPi4FoDxQiwnNXESpqsRz16MM_UMb7ojFaoQAfw7qUAqlxONBJdsPVtA9RNkYmjqyb-EhsrsO5rGUz1hunQ2lSC5JoYMJa9BSvDqRfFmaYV7A-Zm8Mf4FkDJalojnpzJyvR-SHxgGy6HI0S_sKNJYf_Y7MVIynFE8aTe8r3pyZzvdq1v7XuvUpWqQKt9HlU3oKNHU3aKAXUJ3Eho2pfmsmFF6katENitvj2x0NJPMtcEskLzjBFbWNPQvrK5Xpg9_SbOalpUMzQFnhV7rQFkHe9wRkKBw5VPPunrO-JtfenjFTPKX1pwtaq595fnr0OdfQHzmuL6xEfAWW7P0Qrw22nCYm5T-WYD8RkENOv9d-IACPVBTiWslbnWzpwQBKqAKe7R11CNMieIopk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfb370d6c1.mp4?token=HzYiZY1sqVLIqKjNol8p-jllT7FckJ2lHwXEzmWLcHOLRSOeDaOuczem-opuAtPZ8TDrlBtRgXSW4JOMEDQIez7_a-rIvTaGOo4iuHGsyvRK0Zx9RVzga0dqV2djTaahIRiwSGaZ9YULIgiZCLQ1q_2zxilmTaXiVw0yQj4jD5PaeYX-olWAOXxuLA8D7muVNA6uDBXO1XLcUP3vcfS5TmayBD1ZTXxu0E-nYjxJffXI0j8w8ccFKNnvbSYsNm3me7JFljLQW4fNDLe-PezoViahTyJefPi4FoDxQiwnNXESpqsRz16MM_UMb7ojFaoQAfw7qUAqlxONBJdsPVtA9RNkYmjqyb-EhsrsO5rGUz1hunQ2lSC5JoYMJa9BSvDqRfFmaYV7A-Zm8Mf4FkDJalojnpzJyvR-SHxgGy6HI0S_sKNJYf_Y7MVIynFE8aTe8r3pyZzvdq1v7XuvUpWqQKt9HlU3oKNHU3aKAXUJ3Eho2pfmsmFF6katENitvj2x0NJPMtcEskLzjBFbWNPQvrK5Xpg9_SbOalpUMzQFnhV7rQFkHe9wRkKBw5VPPunrO-JtfenjFTPKX1pwtaq595fnr0OdfQHzmuL6xEfAWW7P0Qrw22nCYm5T-WYD8RkENOv9d-IACPVBTiWslbnWzpwQBKqAKe7R11CNMieIopk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو ای از لحظه حمله آمریکا به پل B1 کرج:
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/69902" target="_blank">📅 19:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69901">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
🇺🇸
پرزیدنت ترامپ:از شیوه مذاکراتی ایران ناامیدیم.
ایرانی‌ها بازی فریبکارانه‌ای با ما در پیش گرفته‌اند: در اتاق‌های مذاکره موافقت می‌کنند، اما در رسانه‌ها [توافق‌ها را] رد می‌کنند.
ما از هیچ کمبودی در ذخایر موشکی رنج نمی‌بریم.
ما می‌توانیم با نیرویی عظیم به ایران ضربه بزنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/69901" target="_blank">📅 18:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69900">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24b53c400c.mp4?token=C5K5dCv8f60ZvPFjTEKnqEsQvziVup1Qdfxq672zG64rnkyLzNVOdMTo9Kn52Ba4AMPckLFFywANo9s6XdbVX11EVgbka0hsG_AWk2mscR1XeK2Hsin2acR9hLdeFS3W5Tzwwu_QeK1FrzUrNosMa4ubBNVIPu_6vYYvH42Cbsoai-AJLDbIhIs5nJGfsht_7I7aSTjVBPUzd3nN_vr-HNEqx5J8uAsaVwUABOJQxiS1y_jpKYbdQsoGwTjbLDQ7eTkRgiG4BN5VVRO85B-bCwmQr5JkHX72PHE1Op_opIbPwopnZ56VrhzxRCKqiq4SgveppQWlD__cuznUL2zAUwvBACeV9sDa4RBP0WxaMpWi4HGvTyywcKcGlUxMfA_lXtGFXpLMUXIwNtexJ659jpFSXD4aN7qUW6nQSHFbOUSESiJH_79__fzBaIOw_vQEVdKwwiVJQjigQf2BdbB8ee4hic7GR6fq4Y2um7-f22v-avIjg1MdL0dxe8sm-N-iiqerwqlFvJNR84wjVThBp8zAxOdy58Qox5KTbFFpkdXnotnFKXuFj0jDtYf-POD1x-LBTSz5n2xt3pLkULV3qHELdEM6VN8tDfOfHW0_hmiMucT0gRLHSYOjdh8Y9hxwbb4701RAjVuhlxFwfLGC16ry2D8VntHD0xMRZTgtGLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24b53c400c.mp4?token=C5K5dCv8f60ZvPFjTEKnqEsQvziVup1Qdfxq672zG64rnkyLzNVOdMTo9Kn52Ba4AMPckLFFywANo9s6XdbVX11EVgbka0hsG_AWk2mscR1XeK2Hsin2acR9hLdeFS3W5Tzwwu_QeK1FrzUrNosMa4ubBNVIPu_6vYYvH42Cbsoai-AJLDbIhIs5nJGfsht_7I7aSTjVBPUzd3nN_vr-HNEqx5J8uAsaVwUABOJQxiS1y_jpKYbdQsoGwTjbLDQ7eTkRgiG4BN5VVRO85B-bCwmQr5JkHX72PHE1Op_opIbPwopnZ56VrhzxRCKqiq4SgveppQWlD__cuznUL2zAUwvBACeV9sDa4RBP0WxaMpWi4HGvTyywcKcGlUxMfA_lXtGFXpLMUXIwNtexJ659jpFSXD4aN7qUW6nQSHFbOUSESiJH_79__fzBaIOw_vQEVdKwwiVJQjigQf2BdbB8ee4hic7GR6fq4Y2um7-f22v-avIjg1MdL0dxe8sm-N-iiqerwqlFvJNR84wjVThBp8zAxOdy58Qox5KTbFFpkdXnotnFKXuFj0jDtYf-POD1x-LBTSz5n2xt3pLkULV3qHELdEM6VN8tDfOfHW0_hmiMucT0gRLHSYOjdh8Y9hxwbb4701RAjVuhlxFwfLGC16ry2D8VntHD0xMRZTgtGLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
رونمایی صداوسیما از «قوی‌ترین سیستم جاسوسی جهان»
تماس با پذیرش هتل عمان برای جاسوسی:
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/69900" target="_blank">📅 18:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69899">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736f2f73f3.mp4?token=Fr18eSrt-8ecWO6VQxJWKwEIW8jy13hyTLRHl-e-BMq3rtIrWI47dfo77R77VWYAgTyCsIozQe1Ml260dBQlPPMGLQpAOR7DOX2lEINpk9jiY9-9fw4qdEqvGtPJkUyPFW_fkJylAq4fG4qYIgHQ5anWHrCga5kyBfrNLw3voQYk4KPannwJD1xpnepGBnYauyUS0p-T_oZ6WSi3MtdB76fgdTD_93Y5m7WV2wkWbwd7HEx19CHim9UbLPQEc3hIdUgmDfVtRlW-NohU3rEMjTpnQh01UcWqHVercnIZ3V4DmxjmqPWBXsQweU7ta3BDOPQIE7vjlGhSBa40CU6eyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736f2f73f3.mp4?token=Fr18eSrt-8ecWO6VQxJWKwEIW8jy13hyTLRHl-e-BMq3rtIrWI47dfo77R77VWYAgTyCsIozQe1Ml260dBQlPPMGLQpAOR7DOX2lEINpk9jiY9-9fw4qdEqvGtPJkUyPFW_fkJylAq4fG4qYIgHQ5anWHrCga5kyBfrNLw3voQYk4KPannwJD1xpnepGBnYauyUS0p-T_oZ6WSi3MtdB76fgdTD_93Y5m7WV2wkWbwd7HEx19CHim9UbLPQEc3hIdUgmDfVtRlW-NohU3rEMjTpnQh01UcWqHVercnIZ3V4DmxjmqPWBXsQweU7ta3BDOPQIE7vjlGhSBa40CU6eyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
مشاور قالیباف، مجید شاکری:
هیچ کس نمی‌تواند با ترامپ به توافقی برسد.
این تیم فعلی با هیچ کس به توافقی نرسیده است.
او هم با ما به توافقی نخواهد رسید.
همه فقط در تلاش هستند تا "تحمل کنند و صبر کنند" تا پایان این دوره.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69899" target="_blank">📅 18:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69898">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c85bc1feb.mp4?token=dzUEO3U2pBpEr0vlRc_K1HKdatV-CorGbQzeyoVbr8RilpPXaPXnGW_mbkv79tmQsoryjs5S80u5xgCh0NVcQ69rt8HQXLBF-0WEsAY8mMFWqEsuZwvDSDkrCytXbWtp4GcTUncathZb5ijOq7WME75S2unX-HCrgAsApYTXDVd-OTuMU5ZiypHTEouqTrXi8YJL4ZvstabeBCX3vSreS4YncEfazekfkYigLL9MWi4SZ_jlUwC-ZETcO-Dun5Bnesau45aLPr_lLym8Q0vEgMtTIZyQOBEUmPLGYiBh7UTiwOuvWIATcrUybNfSkKjOPd1bx5NaFiexp123quREvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c85bc1feb.mp4?token=dzUEO3U2pBpEr0vlRc_K1HKdatV-CorGbQzeyoVbr8RilpPXaPXnGW_mbkv79tmQsoryjs5S80u5xgCh0NVcQ69rt8HQXLBF-0WEsAY8mMFWqEsuZwvDSDkrCytXbWtp4GcTUncathZb5ijOq7WME75S2unX-HCrgAsApYTXDVd-OTuMU5ZiypHTEouqTrXi8YJL4ZvstabeBCX3vSreS4YncEfazekfkYigLL9MWi4SZ_jlUwC-ZETcO-Dun5Bnesau45aLPr_lLym8Q0vEgMtTIZyQOBEUmPLGYiBh7UTiwOuvWIATcrUybNfSkKjOPd1bx5NaFiexp123quREvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
نیروهای روسی تلاش کردند تا یک گروه بزرگ از خودروهای سبک را در یک نقطه تجمع، تقریباً 20 کیلومتر پشت خط مقدم در منطقه دونتسک، مستقر کنند.
همانطور که در اینجا مشاهده می‌شود، پهپادهای تهاجمی کوچک اوکراینی این گروه را مورد حمله قرار دادند و ضربات متعددی به آن وارد کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/69898" target="_blank">📅 18:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69895">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c9ff38ed.mp4?token=lPu7GUcIFMWRpxRITLehSIKfW6ksi7l0QCk9d3x7ywLp0HZyZtvDyZGLSV_UOzIBoLSOvfwmpoTx0Jw7iCzmYw64IPAow1F8zAwt3_c6yQc25uAMrH5BIJF6ES2d03DOrlvhrmO1fXO-mWXW7JEaOte71uCxV7AEJBlKVQT-j3Y3gBrD6IIyay8J43LhI2chfAW7AWRsJk6p2qFmVKzggv1jEwtNWa5wwYPH7STU5RKRUjhkbk2LTr4AJrAJQMaZqpI1hE2FgJ7O0FuTZNIIlZ8cjN1NdXrSvgDlnONWvpk9ovk4fs1UPhxtSTL7U0rYLC61OGO1lKSpTB23ofjPow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c9ff38ed.mp4?token=lPu7GUcIFMWRpxRITLehSIKfW6ksi7l0QCk9d3x7ywLp0HZyZtvDyZGLSV_UOzIBoLSOvfwmpoTx0Jw7iCzmYw64IPAow1F8zAwt3_c6yQc25uAMrH5BIJF6ES2d03DOrlvhrmO1fXO-mWXW7JEaOte71uCxV7AEJBlKVQT-j3Y3gBrD6IIyay8J43LhI2chfAW7AWRsJk6p2qFmVKzggv1jEwtNWa5wwYPH7STU5RKRUjhkbk2LTr4AJrAJQMaZqpI1hE2FgJ7O0FuTZNIIlZ8cjN1NdXrSvgDlnONWvpk9ovk4fs1UPhxtSTL7U0rYLC61OGO1lKSpTB23ofjPow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سامانه‌های پدافند هوایی «اونجر» (Avenger) و رادارهای «سنتینل» (Sentinel) ارتش ایالات متحده در نزدیکی محل بازی گلف ترامپ مستقر شدند تا پوشش حفاظتی کوتاه‌بردی در برابر پهپادها، هواپیماها و موشک‌های کروز فراهم کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/69895" target="_blank">📅 17:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69894">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f4acff5e.mp4?token=gA7iENkfM9tF17WNCrCsyZeITH1stldmNNt1cZv_Uwn_2iB--LfLSqOteNaOdUAuNgawKAGZGcO16qQ42zTXeiB4thzMCOPMhIOcZIuhBM0hSGIJoEmFm30a0wnQUyTUFE_1uVl-uJg5gC-KZgJUVdM_d239PRgf_Smq_c-wrhpMuRWV_Na14LLzopySK6VYkiBD4oazCZMXcnGUTtY0gdoiFC6xv4N-Z6gdNwfEaoxcDfXGRFEHtiaVgL1Q_lzyF16NxqbE7TNC8kg93nyvhqq5qOrjKirQY1dn4k7mm8iQn7EL6v142dvEvuIQq1yOMz6n2mN8jiy0AE7v38XT9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f4acff5e.mp4?token=gA7iENkfM9tF17WNCrCsyZeITH1stldmNNt1cZv_Uwn_2iB--LfLSqOteNaOdUAuNgawKAGZGcO16qQ42zTXeiB4thzMCOPMhIOcZIuhBM0hSGIJoEmFm30a0wnQUyTUFE_1uVl-uJg5gC-KZgJUVdM_d239PRgf_Smq_c-wrhpMuRWV_Na14LLzopySK6VYkiBD4oazCZMXcnGUTtY0gdoiFC6xv4N-Z6gdNwfEaoxcDfXGRFEHtiaVgL1Q_lzyF16NxqbE7TNC8kg93nyvhqq5qOrjKirQY1dn4k7mm8iQn7EL6v142dvEvuIQq1yOMz6n2mN8jiy0AE7v38XT9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
دیشب توی تهران، یه نفر با یه دست رانندگی میکرد و با یه دست فیلم سوپر میدید
😐
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69894" target="_blank">📅 17:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69893">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDNB0EVzqzqMfUgalQ6xd2FlmnlFxdRgd2zmUovzqh8VwvDwOORoxM9PEsN5V_bpgnk1Hp1G5j8wNdGkYqf1NL9oxaejEqYFmZg4WJee2Yc-FB11V139fqA5uMg4yO-VtQ_pFWPPk3uwKFwYhHnjf6YBpgdFu7noyC8hy9MCvNZg8FMJuVAj0EXYb3M7WgBlEEdHASPG_8rCbrh4OHhW01yyGRFtWv7guKdQFKCFcSnOeiT4vbkImNFEV0bxChZVtpjKZzGceTq0e24orGjWhQ7QrAgZpqz8pcxZWYEUYlV7jTBB2S6trNN_6ah5CWvswCvI8P9aArg2uTVDKdUaBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
📰
وال‌استریت ژورنال:نیروهای آمریکایی بامداد سه‌شنبه به سوی شناوری با پرچم پاناما آتش گشودند؛ این اقدام پس از آن صورت گرفت که شناور مذکور ظاهراً تلاش کرد محاصره دریایی بنادر ایران توسط آمریکا را بشکند.
پس از آنکه خدمه این شناور هشدارهای مکرر نیروهای مسئولِ اعمالِ محاصره را نادیده گرفتند، یک بالگرد نظامی آمریکایی سکان کشتی را هدف قرار داد.
خدمه شناور در حال تلاش برای انتقال به یک کشتی غیرنظامی دیگر مشاهده شدند.
در نهایت گزارش شد که هر ۱۷ خدمه کشتی در سلامت هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69893" target="_blank">📅 16:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69892">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VooULoBmfIZORG4nwH6kqwAV7BMpjyAI0FcqeClRoYU3MiUmAjTUnP09jcPlzty2bS2-axH09yTOiAgdMY2VqzJszCKfblukEIaFu33wYQu9b27BwdNNp4isiwCUrpm6xzXhcrfQ65znwd44QjMPAk0lTChhZLqLYCTG3iGai5B5HQZI-20bD-_-YNWS6M1s0tuwjlKE9ANKA0bYwLDec7TPfnfPjbmfYZ49chCkFlHwjhoZ6WqjGXfXPq5Rx13KOYWhpCfUojtxZ7IQY9b3uJ1VgA2-bzwKjP9v4JGZSPM0WAZK-_jGllB3qc_eglqv8DR9lwZUa_zwzA3aKqzNpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📚
#فوری
؛ زمان برگزاری کنکور مشخص شد!
صبح پنجشنبه ۲۹ مرداد : کنکور تجربی
عصر پنجشنبه ۲۹ مرداد : کنکور زبان و هنر
صبح جمعه ۳۰ مرداد : کنکور ریاضی و انسانی
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69892" target="_blank">📅 16:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69891">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62f8b2cd3c.mp4?token=MBjmGItyz1jseoM0JhB4XAZRi-QZqc4p4Z0kAZCT8o2vdQ6cq8VV_STxKeltI9SdMuI9yAFhEHbud3YZmdADpbpvavH0MpY3LZmFGkCJDE68adw-8DWwzUNQaL0xS2NwYHHjHeAEWGT4KVQUgfC7E4NWyWxUE-bfpnyWJSmUKXjE5FOsHLWvZzRktCW5DMEsRXQDKX1fHb4yw1yB1iVn_HTNnUaJCe39hjHazo61_cCcbWdqMIdWq5HYG7SxlMlCphGpSkRTaB8yXHf3azp9alUxLt-Apr0Jd1iqhNdbZK4eoNuB33koF8keVkUGGU8Ktu0bL2AIuubF7_mmgQuZag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62f8b2cd3c.mp4?token=MBjmGItyz1jseoM0JhB4XAZRi-QZqc4p4Z0kAZCT8o2vdQ6cq8VV_STxKeltI9SdMuI9yAFhEHbud3YZmdADpbpvavH0MpY3LZmFGkCJDE68adw-8DWwzUNQaL0xS2NwYHHjHeAEWGT4KVQUgfC7E4NWyWxUE-bfpnyWJSmUKXjE5FOsHLWvZzRktCW5DMEsRXQDKX1fHb4yw1yB1iVn_HTNnUaJCe39hjHazo61_cCcbWdqMIdWq5HYG7SxlMlCphGpSkRTaB8yXHf3azp9alUxLt-Apr0Jd1iqhNdbZK4eoNuB33koF8keVkUGGU8Ktu0bL2AIuubF7_mmgQuZag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
یه آخوند توی برنامه زنده داشت به اجرا نشدن قانون حجاب اعتراض میکرد و میگفت ملت بالای ۴هزار تا پیام دادن برام؛
بعدش گفت بزارید یکیشو رندوم براتون بخونم:
چیزی که خوند
😔
:
«آقای پفیوز احمق بیشعور حرف دهنتو بفهم»
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69891" target="_blank">📅 16:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69888">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/698b90aa95.mp4?token=p-VomaNDYZlvT2IYbbEW1cDa7JefcGz3HvPO5tHsIm6GT-ljFJQvKit8NJWtY4qBeRq3I9QiNQfnBdChIQo5-R6SS6i0IPgFuZs_oB3_8sDJsOGGh4pzLAtzWo5pYu7koEPTPE_SmYuD4TPFIAOUZ1QmbC-CaD6dMMx9Elvga4MxiikJcEKdfwEqJdtBJHEew17n9gVRSM1upZ0QeeYiqpGar6cb7E1exZX7iygbyKdij-4TdVdR2OD0XcNrTx8SWZA1tvAcsezV0N-lRnlsZnSIyXQxJN9e5efI5TTXWZh5FpJSZJTG-bGU5-U9_xu5uP0AJZPl-nBu13ddcFyxYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/698b90aa95.mp4?token=p-VomaNDYZlvT2IYbbEW1cDa7JefcGz3HvPO5tHsIm6GT-ljFJQvKit8NJWtY4qBeRq3I9QiNQfnBdChIQo5-R6SS6i0IPgFuZs_oB3_8sDJsOGGh4pzLAtzWo5pYu7koEPTPE_SmYuD4TPFIAOUZ1QmbC-CaD6dMMx9Elvga4MxiikJcEKdfwEqJdtBJHEew17n9gVRSM1upZ0QeeYiqpGar6cb7E1exZX7iygbyKdij-4TdVdR2OD0XcNrTx8SWZA1tvAcsezV0N-lRnlsZnSIyXQxJN9e5efI5TTXWZh5FpJSZJTG-bGU5-U9_xu5uP0AJZPl-nBu13ddcFyxYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترلان پروانه توی آخرین مصاحبه‌ش گفته رابطه‌ش با شروین حاجی‌پور یه اعتماد اشتباه بوده و این رابطه تموم شده.
بعد از این مصاحبه هم شروین یه موزیک منتشر کرده که خیلی‌ها معتقدن حال‌وهوای بعد از جدایی رو داره.
جالب اینجاست که اوایل رابطه‌شون شروین توی یکی از موزیک‌هاش گفته بود قراره تا به دنیا اومدن نوه‌هاشون کنار هم بمونن!
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69888" target="_blank">📅 15:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69887">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05e9aa8412.mp4?token=C8moe2I4UqswvFSUvAHcxLZ6lw2_LZx1X3K9-jdyFTnX6-lhsEZ3MW_800dA2f0wKiG9k6MCXnUMM5jwOV-Mk91TQACOLI7gAUNURHuWUOsfSQfxzaW_SQMxx6gGrmlJhmJfXP8CEUNN8EPCOzmgIuKU3c1aSgH7alLkI7M2ie8GxVX_lW9zibOGRVd2OTWmMF-HIYOtyBL2bMiyyrJFX6Wxawx5axF-4J5orRiDj5-ndS-BjlYF8cLajDq68dxqf7OaOTmmW9g-S5dFcO1rukWIOeGXCIe0rwnMqLUR792SqQFsfgjO4rRK2z0ZZlaT2Ex8kb0XFB4gHX-g6kMlyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05e9aa8412.mp4?token=C8moe2I4UqswvFSUvAHcxLZ6lw2_LZx1X3K9-jdyFTnX6-lhsEZ3MW_800dA2f0wKiG9k6MCXnUMM5jwOV-Mk91TQACOLI7gAUNURHuWUOsfSQfxzaW_SQMxx6gGrmlJhmJfXP8CEUNN8EPCOzmgIuKU3c1aSgH7alLkI7M2ie8GxVX_lW9zibOGRVd2OTWmMF-HIYOtyBL2bMiyyrJFX6Wxawx5axF-4J5orRiDj5-ndS-BjlYF8cLajDq68dxqf7OaOTmmW9g-S5dFcO1rukWIOeGXCIe0rwnMqLUR792SqQFsfgjO4rRK2z0ZZlaT2Ex8kb0XFB4gHX-g6kMlyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرود هواپیمای F-18 بر روی ناو هواپیمابر در هوای بارانی.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69887" target="_blank">📅 15:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69886">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e61a50ec6.mp4?token=n03_xE3asT670BsnXZghShswKCySLZsIh2pyLJ_IZPZ4mZ2TAwGrXJINGMc4RnIWdTZMoSHRUN_2NiY38XxaRr-gUGpfIOhByA-a6PSeaU7sZFoFVC9BtCs7GMoBgeM0pX38VfXoqADvnODNusIx2Xl2yw8bw2NfBUYDqlP-mbe6rfTCTkbAz3GU84eSr-VAxsQdgKt81y84s3IRWUQbQs-TO_HwdjAJEhaJbdIRxHuCZGphvhk3ejtQjWGOi9IcLoZNrL5cNPrZmfFJ4n4cmwLQdTuBhVXqeSjenOS0hN8eYY-JSuM8O05cVJpJ1kfNNzqf0GwEvS4pFTnQmRcYqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e61a50ec6.mp4?token=n03_xE3asT670BsnXZghShswKCySLZsIh2pyLJ_IZPZ4mZ2TAwGrXJINGMc4RnIWdTZMoSHRUN_2NiY38XxaRr-gUGpfIOhByA-a6PSeaU7sZFoFVC9BtCs7GMoBgeM0pX38VfXoqADvnODNusIx2Xl2yw8bw2NfBUYDqlP-mbe6rfTCTkbAz3GU84eSr-VAxsQdgKt81y84s3IRWUQbQs-TO_HwdjAJEhaJbdIRxHuCZGphvhk3ejtQjWGOi9IcLoZNrL5cNPrZmfFJ4n4cmwLQdTuBhVXqeSjenOS0hN8eYY-JSuM8O05cVJpJ1kfNNzqf0GwEvS4pFTnQmRcYqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان زیبای زندگی کسی که هممون باهاش خاطره داریم...
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69886" target="_blank">📅 14:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69885">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
🔴
ما سه راهبرد داریم:
ادامه دادن به همین روال فعلی؛ یعنی صرفاً پیش رفتن و نظاره کردنِ وضعیت وخیم آن‌ها، چرا که تورمشان به ۳۰۰ درصد رسیده است. ارزش پول ملی‌شان تقریباً از بین رفته است. آن‌ها حقوق سربازانشان را نمی‌پردازند و سربازانشان در حال ترک خدمت هستند. بنابراین باید همین روند را ادامه داد، چون این وضعیت پایدار نیست.
وارد کردن ضربات بسیار سنگین به آن‌ها، یا... در واقع راهبرد سوم، شکست دادن آن‌ها از طریق اقتصادی است. اما ما به هر حال داریم همین کار را می‌کنیم؛ این [راهبرد] تا حدی بخشی از همان راهبرد اول محسوب می‌شود.
از نظر اقتصادی، وضعیت آن‌ها آشفته و نابسامان است. آن‌ها نمی‌توانند وام بگیرند. ما کنترل منابع مالی‌شان را در دست داریم؛ همان دارایی‌هایی که در اختیار داشتند و رقم بسیار بزرگی هم بود. آن‌ها سرمایه زیادی داشتند و ما اکنون کنترل کامل آن را در اختیار داریم.
من بانکدار آن‌ها هستم. من بانکدار آن‌ها هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69885" target="_blank">📅 13:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69884">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71d56160d7.mp4?token=h_0Py_gcslcw5U9kGT_jUm43hMSIBWEGMDSNyXe6hyQ5uiqAx_A6WhPYShOY7eAbTbSkvbTCpd1EUlRBanQWiuG7hgDByv7wVo3OKAIZb_t1_IkDA_OxyBf48M0__HPasnyFQrS1wr3-5e8wBI_jmDHqfGW_X-N067ES8HmARbqQP1gOstXAgph8-pWXMlb8OGfGHeBEzPAlmKoaG9ty2smC1z2yqE1kFxPVIL1-1EEcBoofpXHcEHh0FnmXDsbfC3dh_n5hmW6JfHYRJS72heuW8qgaO63mA36OeFUU4_YURM_8Q_vwaQMC9fCtQvVKrgDKLvt1xjqssIDDWjUe4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71d56160d7.mp4?token=h_0Py_gcslcw5U9kGT_jUm43hMSIBWEGMDSNyXe6hyQ5uiqAx_A6WhPYShOY7eAbTbSkvbTCpd1EUlRBanQWiuG7hgDByv7wVo3OKAIZb_t1_IkDA_OxyBf48M0__HPasnyFQrS1wr3-5e8wBI_jmDHqfGW_X-N067ES8HmARbqQP1gOstXAgph8-pWXMlb8OGfGHeBEzPAlmKoaG9ty2smC1z2yqE1kFxPVIL1-1EEcBoofpXHcEHh0FnmXDsbfC3dh_n5hmW6JfHYRJS72heuW8qgaO63mA36OeFUU4_YURM_8Q_vwaQMC9fCtQvVKrgDKLvt1xjqssIDDWjUe4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سینا حجازی، خواننده:
اگه زنِ هات میخواین، زن گوشت‌خوار بگیرین، زنایی که گیاه خوارن، سردن!
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69884" target="_blank">📅 13:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69883">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbTS8WBs5qKhTj6UpCLJj008xm8WI7bwPPnFmR-NEJEzIhhcFH2Kg_UFC35DoOjEyytYl2FQwV2hh0bVUBzod55TapzYYIicQD0SOBaHeGiUVLu2VzXkveZBzz6bzFAEYbne3zZyiXPTyqmnoUmabruH_4AUd8nUml2wm0-XVJjGnUKIep0jzcXJeGSmzt_rfNZT8nwAK_bJOTSZg2zkaMVoaQqy6zCP2XW9mPj71VVazeiPG9eyyHLAB1I5Ay0JX8IL8rHcEzhD-PmFQBAZtNHjfaN10JsaJPWcFfgGsT1mYW5tHP8jaXEL3BXhy3n2ojoE6oINRmodl4zzch-kpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا:
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع حادثه‌ای میان یک نفتکش و نیروهای نظامی در دریای عمان خبر می‌دهد.
هویت نفتکش و نیروهای نظامی درگیر در این حادثه هنوز اعلام نشده است.
در حال حاضر جزئیات بیشتری در دسترس نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69883" target="_blank">📅 12:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69882">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b61a921e39.mp4?token=QDmc7BEKxzZFjGS-X5YRclZjIeQmXpJW07WH4dqEbAg9bg20ORRIVxQ377F_MYBH2LlcdmD6zaHlYLvh6HAFJoJJUas6w_oIP7XobMRaEJ_pZ_ijkMTu5mnmJUkVJuSUjSeuWkPnDzJ2P8d98AM_o5YgRr-AhM8ASziP7bfQJAoRxFdEe26BSc3LkLycuyGUA2C7NziozW4I8cOPSgk3a_rqZ8KdM0lUdU_t9Xi0Wv7KLcezMp0-UZxa7shXCnNhLWoGg1NCEzEDF_3gRQ0wxbBuWWgrDHysmXtDtz6brtgOOHfCwaTKySDuA3a49g5q39_HENw48M1fdI_ZR9Vz8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b61a921e39.mp4?token=QDmc7BEKxzZFjGS-X5YRclZjIeQmXpJW07WH4dqEbAg9bg20ORRIVxQ377F_MYBH2LlcdmD6zaHlYLvh6HAFJoJJUas6w_oIP7XobMRaEJ_pZ_ijkMTu5mnmJUkVJuSUjSeuWkPnDzJ2P8d98AM_o5YgRr-AhM8ASziP7bfQJAoRxFdEe26BSc3LkLycuyGUA2C7NziozW4I8cOPSgk3a_rqZ8KdM0lUdU_t9Xi0Wv7KLcezMp0-UZxa7shXCnNhLWoGg1NCEzEDF_3gRQ0wxbBuWWgrDHysmXtDtz6brtgOOHfCwaTKySDuA3a49g5q39_HENw48M1fdI_ZR9Vz8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تازگیا به نوع مدیتیشن تو تهران مُد شده که کلمات رو به صورت نفس‌نفس زدن میگن تا انرژی بد ازشون تخلیه بشه
😳
هزینه هر دوره بالای ۴۰ میلیون!!!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69882" target="_blank">📅 12:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69881">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46ae8f31fa.mp4?token=mWnf5cZEcjEeGDq8z9C5OUtsbhgryxre5E95SQN4wlO43Mlvi3n4daDVV0uNm7zt8jCNqBnwCSoTdWbgaorSwNbzHPCOnruPkT58DMuEJjl7vHyOeUbdNl2u4PrUCdGLGNbNXmyAaV4fMHmDQdExNsBIyubUZ09dhoo9dB1xakQhG75Sie9JeHidX2tE9LVvqh9y8-O9BuYuyR7EzX5BlYOwK6BkyLDNNrKcsHGt5TewcC6YmpVSXVONNvq7cssvVkYuc2jSDILkZlf5vcXDJwnImUVq_6azcMXhHx2IY8rb0_pHy8Vb_7uq8nGd9NwFCd7Nyimf663XybTV8oYPSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46ae8f31fa.mp4?token=mWnf5cZEcjEeGDq8z9C5OUtsbhgryxre5E95SQN4wlO43Mlvi3n4daDVV0uNm7zt8jCNqBnwCSoTdWbgaorSwNbzHPCOnruPkT58DMuEJjl7vHyOeUbdNl2u4PrUCdGLGNbNXmyAaV4fMHmDQdExNsBIyubUZ09dhoo9dB1xakQhG75Sie9JeHidX2tE9LVvqh9y8-O9BuYuyR7EzX5BlYOwK6BkyLDNNrKcsHGt5TewcC6YmpVSXVONNvq7cssvVkYuc2jSDILkZlf5vcXDJwnImUVq_6azcMXhHx2IY8rb0_pHy8Vb_7uq8nGd9NwFCd7Nyimf663XybTV8oYPSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
استایل ثروتمندترین ورزشکار دنیا
🆚
استایل پسرایرانی با ماهی ۱۵تومن حقوق
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69881" target="_blank">📅 12:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69880">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf27d27808.mp4?token=setARej3TUu-2HFoVM9bQr96Y3nCyQgNPKBEeNv4fPUfBRCvV_FkcvkcjowkcbTQbpUzNxPYqE_V2zsdQraGh62bCYxMUvWgpW1Piy5MXtTAlpA6JHPd7VReNSXGgDW4eIyDRxKlqXzDUDvulePQJBZlnHLbMO_iU2QFNY_IOfUFThDyfLfdZ2i__n43wi0txuey5w8iMdrzUNPDw7uHg_F1emq2GeGrg6H7umVOIfIMg9piGX1aCRVXBxPR0MsGRo0vuTbt7am0BgKQ71BXeBKIZKL-xgqKFUEYMZ5As-OEcEwPjSRJu8UC91Pvx4T0_M2eNmKj2zZ1pgSt6R3PPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf27d27808.mp4?token=setARej3TUu-2HFoVM9bQr96Y3nCyQgNPKBEeNv4fPUfBRCvV_FkcvkcjowkcbTQbpUzNxPYqE_V2zsdQraGh62bCYxMUvWgpW1Piy5MXtTAlpA6JHPd7VReNSXGgDW4eIyDRxKlqXzDUDvulePQJBZlnHLbMO_iU2QFNY_IOfUFThDyfLfdZ2i__n43wi0txuey5w8iMdrzUNPDw7uHg_F1emq2GeGrg6H7umVOIfIMg9piGX1aCRVXBxPR0MsGRo0vuTbt7am0BgKQ71BXeBKIZKL-xgqKFUEYMZ5As-OEcEwPjSRJu8UC91Pvx4T0_M2eNmKj2zZ1pgSt6R3PPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:درباره گرانی ها هم توضیح بدید؟!
🇮🇷
مهاجرانی سخنگوی دولت:
قبلا توضیح دادیم، گرانی های موجود دلیلش فشار اقتصادیه.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69880" target="_blank">📅 11:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69879">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1ee7cbbf.mp4?token=dRI5baYmi4hbWk_YlgNVc73JlbamEyfzRmRDtsrzUjRpJc60nkccZaPiwjKD-m04Ab2cY5_cP2FuMdvzJYkSiDgAR7Omstg6_oHQJfOD_iHvX_Qj3Bkhg_GMxfHcqndWbHqKcSlnE5XdHtyXNhKPv33jxL1qSlwoWsDhKVA0O_ENivcSG17WfoH2e-3fQj2GxTZpSf1XyD_FOX6qs4MjFg_XIi-T-3jRoCwMo8fafiim7WdLhQJhR86oAT65PkjTLlSR0ubvKhjjRuIwqrz1PUtTqUpyIxFqHxZcVsDLDK534gq11MQrQMbgF-G9ivM87YEPeq7EKDR_ZnwhmLY14A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1ee7cbbf.mp4?token=dRI5baYmi4hbWk_YlgNVc73JlbamEyfzRmRDtsrzUjRpJc60nkccZaPiwjKD-m04Ab2cY5_cP2FuMdvzJYkSiDgAR7Omstg6_oHQJfOD_iHvX_Qj3Bkhg_GMxfHcqndWbHqKcSlnE5XdHtyXNhKPv33jxL1qSlwoWsDhKVA0O_ENivcSG17WfoH2e-3fQj2GxTZpSf1XyD_FOX6qs4MjFg_XIi-T-3jRoCwMo8fafiim7WdLhQJhR86oAT65PkjTLlSR0ubvKhjjRuIwqrz1PUtTqUpyIxFqHxZcVsDLDK534gq11MQrQMbgF-G9ivM87YEPeq7EKDR_ZnwhmLY14A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دکتر مشاور خانواده :
یه مرده اومد بهم گفت زنم عاشق دوستم شده و منم بهش گفتم که تو حق داری باهاش رابطه داشته باشی!
گفت منم با خانمِ اون آقا چندبار رابطه داشتم ولی چون اون خانم خودش پارتنر داشت، زیاد خوشم نیومد و کات کردم...
ولی خب موقع سکسِ اون آقا با زنم، من اونجا هستم و تماشا میکنم!
الانم از اینکه خانمم از اون آقا باردار شده خیلی ناراحتم چون آمادگی داشتن بچه رو ندارم.
ولی خب بازم میخوام شناسنامه اون بچه رو به اسم خودم بگیرم...
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/69879" target="_blank">📅 11:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69878">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/69878" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/69878" target="_blank">📅 11:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69877">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCL5pMj5gRmRht7322033OL9hKO1-HB7_FUuWqlTAWmsQ9wo80tVVXnDMc0MyyuUcA0SvzjMXm2r1cIp6xuB5J8-l5Q5Dp23hps7N45DuVpog46vMIo3Itt1RO1D_Umsj8-RB5Y1bbWMO6TljXTMEQde-J5DIjCfu6gNJEFAMZBXtPW3GJnNhk59jaFvYj_6wGLX__41F1xWRNdltU0NE5yvtRg-HvKRylxvUWqMRZqocM4zuGOAVrbcGWt-GAhmCyASxBOuqKllp7IcSZOS6IbK5wu-8aGiGUpPKOygequn9i5rbKvcyv8ZJ5pXNnIjexfilMnu0atC_yOtWKILJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
r20
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/69877" target="_blank">📅 11:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69876">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2435556002.mp4?token=lAnIi6utS7j7Ke_TxJ5VQ4bTYNg9--354N1HBVq0BhJ2gfOfdZH8X4fjg9JMNHbX9r_V0HRD7DD1uDS_aMWQLe_0ftjzMqrGuP8tXrcAEMeQ9Do1A-Q8zaaaycKCQOQUDXqn3LGYu3mD9vYIRbLk4wDK-DNG4H13MBVWux-hBgzO9r4uK-wJjN-W0cgObqONk6lCD6qOwfmnug-s8Nn2ScTZHBsgeOxkIkRy4dW1N6UmsGE188Niu2WlLQLyGmFeP1AZAHGNFDWu3BbkMxFqYPbB7NNpNlfbVL95YH_ZI61YYgzCX_47YMgL34mdBbCFimljEowaDVVORNKK_6QbIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2435556002.mp4?token=lAnIi6utS7j7Ke_TxJ5VQ4bTYNg9--354N1HBVq0BhJ2gfOfdZH8X4fjg9JMNHbX9r_V0HRD7DD1uDS_aMWQLe_0ftjzMqrGuP8tXrcAEMeQ9Do1A-Q8zaaaycKCQOQUDXqn3LGYu3mD9vYIRbLk4wDK-DNG4H13MBVWux-hBgzO9r4uK-wJjN-W0cgObqONk6lCD6qOwfmnug-s8Nn2ScTZHBsgeOxkIkRy4dW1N6UmsGE188Niu2WlLQLyGmFeP1AZAHGNFDWu3BbkMxFqYPbB7NNpNlfbVL95YH_ZI61YYgzCX_47YMgL34mdBbCFimljEowaDVVORNKK_6QbIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری و بلاگر طرفدار حکومت:
یعنی چندنفر باهم مشکل داشتن و همدیگه رو به طور کامل میشناختن
این پروژه‌ها از این به بعد قراره زیاد باشه واسه اینکه میدون‌ها و نیروی انتظامی رو ضعیف کنن
قاتل‌ها تو کمتر از 24 ساعت دستگیر شدن و کشور الان تو بالاترین سطح امنیته مخصوصا تو تهران.
متأسفانه قراره خون ریزی های از قبل برنامه ریزی شده شاهد باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/69876" target="_blank">📅 11:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69875">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022aef02ab.mp4?token=XWv6XSvxtElGMe7hHjhlF1FxFy19fejTyqMO6oPjYNNAfOBH75tqspZ6o96eVuhMNW9yTsSfrGCIR95ZarMAqTFPjLyZN0M3ycJ5cHr_oNuAPpaaF_vVK4jo7q7q5KgC0vwYrqc4cW1v3ICkzMyYSiK4v94O02B8XInUYkUL3D75u3AtaD9r_AZnoQgjmyNRRB2bmPsGBq81sRtgwGQsnWgmeGHrNy4cJ5GOF23190B3D1b2xkfUyljBmtwywcntfG-_cV4WdgklB17yWURKcDC3rhGyxBPwDg8EyWHyUzf06sjnZ-mlSfS-HNbZnTLvCuxnimhhKGh2wzpwDZFsIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022aef02ab.mp4?token=XWv6XSvxtElGMe7hHjhlF1FxFy19fejTyqMO6oPjYNNAfOBH75tqspZ6o96eVuhMNW9yTsSfrGCIR95ZarMAqTFPjLyZN0M3ycJ5cHr_oNuAPpaaF_vVK4jo7q7q5KgC0vwYrqc4cW1v3ICkzMyYSiK4v94O02B8XInUYkUL3D75u3AtaD9r_AZnoQgjmyNRRB2bmPsGBq81sRtgwGQsnWgmeGHrNy4cJ5GOF23190B3D1b2xkfUyljBmtwywcntfG-_cV4WdgklB17yWURKcDC3rhGyxBPwDg8EyWHyUzf06sjnZ-mlSfS-HNbZnTLvCuxnimhhKGh2wzpwDZFsIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇺🇸
واشنگتن پست:پس از تهدید ترور از سوی ایران، ترامپ مخفیانه هنگام ترک اجلاس ناتو در آنکارا با هواپیمای دیگری جایگزین شد.
او با هواپیمای جدید ۷۴۷-۸ اهدایی قطر (اولین سفر بین‌المللی ریاست جمهوری‌اش) به ترکیه رسیده بود.
برای عزیمت، او علناً و جلوی دوربین سوار هواپیمای قدیمی ایر فورس وان شد و گفت که می‌خواهد «به یاد گذشته» با آن پرواز کند.
اما دقایقی پس از سوار شدن، او و چند دستیارش از طریق یک کامیون پذیرایی فرودگاهی که کانتینر آن به صورت هیدرولیکی به دری در کنار و دور از دسترس رسانه‌ها بالا رفته بود، به یک هواپیمای کوچک‌تر C-32A (757 اصلاح‌شده) منتقل شدند که از دید پنهان بود.
سپس هواپیمای قدیمی ۷۴۷ به عنوان طعمه پرواز کرد و همچنان از تابلوی تماس ایر فورس وان استفاده می‌کرد.
روزنامه‌نگاران و برخی از کارکنان کاخ سفید که در هواپیما بودند، اصلاً نمی‌دانستند که ترامپ با آنها نیست.
به آنها گفته شده بود که پرده‌های پنجره را بسته نگه دارند، که امری غیرمعمول است.
هر دو هواپیما با فاصله چند دقیقه در فرودگاه سلطنتی میلدنهال در بریتانیا فرود آمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/69875" target="_blank">📅 10:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69874">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ما ۳ استراتژی برای برخورد با ایران داریم
رصد نقاط ضعف این کشور.
وارد کردن ضربات سنگین.
اعمال فشار اقتصادی.
🔴
اکنون ایران در وضعیت آشوب اقتصادی قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69874" target="_blank">📅 10:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69870">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b616d440e1.mp4?token=kwbcItVEe6WsZZzF5O5trVUT6LMDUkhU7_NeVqBKK65b4WedGCnpK62KLxUuSUGdXyFU3mE0x4ALQUP6kDnp7HVEaetn3GPH7W61yvgEYs3LpCCfSbAzlYIomHojfyUald0hrc5AgVPg1kNCWyeo7ItpR11_RHEqOaLaR2wLyH3Bu69hqL6kuJsUn0gsWA2lYsZRj8TN9PzkrPp3W0VPBq4yEttPOZxV_CN4tbNLlQcJUlZ4mk9ThwPgv0Hu-XKZ2UqJLh3dS7PxWY3YA8BNTcEBFR-z9jmXmzD0UIfrEXxGHKuoNfnXvjLyVnwkBxZg8PP2h68E2LYlupZk-B7anQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b616d440e1.mp4?token=kwbcItVEe6WsZZzF5O5trVUT6LMDUkhU7_NeVqBKK65b4WedGCnpK62KLxUuSUGdXyFU3mE0x4ALQUP6kDnp7HVEaetn3GPH7W61yvgEYs3LpCCfSbAzlYIomHojfyUald0hrc5AgVPg1kNCWyeo7ItpR11_RHEqOaLaR2wLyH3Bu69hqL6kuJsUn0gsWA2lYsZRj8TN9PzkrPp3W0VPBq4yEttPOZxV_CN4tbNLlQcJUlZ4mk9ThwPgv0Hu-XKZ2UqJLh3dS7PxWY3YA8BNTcEBFR-z9jmXmzD0UIfrEXxGHKuoNfnXvjLyVnwkBxZg8PP2h68E2LYlupZk-B7anQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
دیروز تو کلمبیا، یه زلزله 7.4 ریشتری اومد و اینجوری به ساختمون ها خسارت وارد کرد؛
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69870" target="_blank">📅 09:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69869">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22c07c5ff9.mp4?token=AvKiYSfl6M-p9lOHxLRBCn-Jla1DaRCtXJGq1SsDEmx0CX14nv4j-1a_q0Snc8WQ6k454wm0DubNjWz2fzOMvZj092h7hif3XUDTULhf_F4R9aI2uZ8amsBBhAAcBwSUKI6ffOxcnQkfsWEgkO1gwt0ayYUsd9LzRqhDy2q4Qwib7ATJymnUPyEPOHSqbkCQ_-uYa44OQEv5oIit04kTZdWD3sFJcYxr7M2Ee68Ia7sCAZdXPxsvibVi0wlRx8l15Y8_9EIBcpATFkpb8IlexqfGA43L7qMrGt_xwOMZvtvpb51qDIzkthQP68-pta8tlb7-2FRPQfZU5wrPg52-nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22c07c5ff9.mp4?token=AvKiYSfl6M-p9lOHxLRBCn-Jla1DaRCtXJGq1SsDEmx0CX14nv4j-1a_q0Snc8WQ6k454wm0DubNjWz2fzOMvZj092h7hif3XUDTULhf_F4R9aI2uZ8amsBBhAAcBwSUKI6ffOxcnQkfsWEgkO1gwt0ayYUsd9LzRqhDy2q4Qwib7ATJymnUPyEPOHSqbkCQ_-uYa44OQEv5oIit04kTZdWD3sFJcYxr7M2Ee68Ia7sCAZdXPxsvibVi0wlRx8l15Y8_9EIBcpATFkpb8IlexqfGA43L7qMrGt_xwOMZvtvpb51qDIzkthQP68-pta8tlb7-2FRPQfZU5wrPg52-nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
خرازی:
مجتبی خامنه‌ای اگه تو این سه سال از دفتر رهبری طرد نمی‌شد، می‌کشتنش
خود علی خامنه‌ای هم همین‌طوری بود، تو دفتر خمینی هیچ جایی نداشت
از احمد خمینی بگیر تا کروبی و... همه میخواستن مرگ علی خامنه‌ای رو ببینن.
ابراهیم رئیسی هم قصد داشت رهبر بشه که شهیدش کردن
اصلا بحث همینه مجتبی اگه زیاد پیش پدرش دیده می‌شد خودی ها میکشتنش
تو بحث رئیسی هم یکی از اعضای دفتر اومد خونمون گفتش ک دارودسته اینا میخاد رئیسی رهبر بشه ولی شهادت جلوشو میگیره
خیلی حرفا هست ولی خب مطمئن نیستم بشه گفت یا نه
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69869" target="_blank">📅 09:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69868">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
🇺🇸
✈️
پشتیبانی سنگین آپاچی‌ها از نیروهای ویژه آمریکا در افغانستان
⏺
تصاویر نادر و حدود ۱۵ دقیقه‌ای از عملیات دو فروند AH-64 Apache در افغانستان؛
آپاچی‌ها گروهی بیش از ۲۰ نفره از نیروهای طالبان را که در حال آماده‌شدن برای کمین یک گشت نیروهای ویژه آمریکا بودند، شناسایی و درگیر می‌کنند.
در این درگیری، آپاچی‌ها ابتدا با توپ ۳۰ میلی‌متری M230 مواضع طالبان را زیر آتش می‌گیرند و سپس برای درگیری با اهداف مشخص‌تر از موشک‌های AGM-114 Hellfire استفاده می‌کنند.
تصاویر این ویدئو با سامانه تصویربرداری حرارتی FLIR نصب‌شده روی آپاچی ثبت شده؛ به همین دلیل صحنه‌ها به‌صورت تصویر حرارتی دیده می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69868" target="_blank">📅 09:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69867">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/69867" class="tg-doc-link" target="_blank">دانلود</a>
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
a19
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/69867" target="_blank">📅 01:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69866">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0qM5kjoIJqU0AIXS9S5w0xr3tgOn5hBvFfruKkPABUpoBA1KGgTTSvcRY6OQZOi7IschglWqRcptU3xqNlh5xpDyfeWJ6dUvIFS4NjwrXfMH8aPNwHUe1VeO3QSSAhkAkC9gm12Pjo8YjG9GPMq3hepMRlctCIJ4Gi-acFrYRCwB-XNK0IJ-gh3lobE2ovZg4mGt_A87hRCuaT1cfghWrbfhsyXsT-sF38bDL_Kso20c3DTbn6wfVKeFiHD-DNwYIGXZfgKgpqmOeYEh00PmkvSVr1dPvevg7sxv2Wa7LaVsu2gKUl1amUwuOgmz0bdhya62KRS-me5UikW8phGCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
a19
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/69866" target="_blank">📅 01:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69865">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/6ad4ea0af6.mp4?token=qnE2MqxU1ZsqZ_bJnuF362Z4QY55Nx1PsWWtTQTH_CURxn__nWfRLrTXqke2LRNbdgsobwpuRJxfEcFWYKQk0mmNFLNJjZpepHG9W1XtXOEA2TCkow9bEU_d_3NpxrfnczYQkL6JnhgUEffl9tOe51htkhmLLCbF3SVVko_LyOgM6g32LgP3aGBo-VuWhGZDRZV3j3MV7nU35KBeS7vWPsVyM7RRB_RatxRXMHTnaN5wxenN046uNCrGA1UcYC3mg9WgpxHXYecddlAq--qolQj83WsQkTPqrnE4GENXK3Ncmea_diUw5ZXwLPFrJw0Clu2wuwf06tfu5BUDbQWNvhDIavm-InugdpJVAuZiWGbPzBYhPYlcZUgbQo7lbIVjafDlV4MqRkOv8zkbCoX8dAK7TSRxGi0HuNu5GfdhB9mI5iOakjQMyhbXGZu0OCageimzINWwK9JkLrbE_QD7Lguewm2_5k6nxlqXAeF_ZhPqPUc-N4BFpa0nBqHRZAW8FT7u01rOMmYx8LxG-8Q25uAvWd3Z8TiURqOskZo8cZrNtsP5CPjXncbiTeTveJwJP2hMvIUyBeV1o6wGkLNm1DlhoEs34WOKji1hpHDldnsiEgKlx_LzXleHLbNU2y8DTbfNhXL8wp48pl_7hZ2tLkSMb7Rr-gKUzMZWM7eqU74" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/6ad4ea0af6.mp4?token=qnE2MqxU1ZsqZ_bJnuF362Z4QY55Nx1PsWWtTQTH_CURxn__nWfRLrTXqke2LRNbdgsobwpuRJxfEcFWYKQk0mmNFLNJjZpepHG9W1XtXOEA2TCkow9bEU_d_3NpxrfnczYQkL6JnhgUEffl9tOe51htkhmLLCbF3SVVko_LyOgM6g32LgP3aGBo-VuWhGZDRZV3j3MV7nU35KBeS7vWPsVyM7RRB_RatxRXMHTnaN5wxenN046uNCrGA1UcYC3mg9WgpxHXYecddlAq--qolQj83WsQkTPqrnE4GENXK3Ncmea_diUw5ZXwLPFrJw0Clu2wuwf06tfu5BUDbQWNvhDIavm-InugdpJVAuZiWGbPzBYhPYlcZUgbQo7lbIVjafDlV4MqRkOv8zkbCoX8dAK7TSRxGi0HuNu5GfdhB9mI5iOakjQMyhbXGZu0OCageimzINWwK9JkLrbE_QD7Lguewm2_5k6nxlqXAeF_ZhPqPUc-N4BFpa0nBqHRZAW8FT7u01rOMmYx8LxG-8Q25uAvWd3Z8TiURqOskZo8cZrNtsP5CPjXncbiTeTveJwJP2hMvIUyBeV1o6wGkLNm1DlhoEs34WOKji1hpHDldnsiEgKlx_LzXleHLbNU2y8DTbfNhXL8wp48pl_7hZ2tLkSMb7Rr-gKUzMZWM7eqU74" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇦
لحظه سقوط یک جنگنده میگ-۲۹ اوکراینی.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69865" target="_blank">📅 01:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69863">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcca7b928e.mp4?token=OUHK-dAQ5JsAp9-NOdS-XgwDq32Mj4g-vcjGergdM3L5COl0n5eyD4uob_QxLOEdd2EGpc_tlyCeDowlyRjLR_7AAxtZpuvlRY93CRO68s-DQE9PPc-_IZzK3NSefUA6inlO5k8wsjGtMcDG3Zvm3WAYH43uGEmyRBE1TtdCVRLn-dD6lBUMbOoR_JlJ8UNU1coSX-1wKfPg9GVM9534TnEouvNe4rE_6mi0lzL88vL-6VCXbprnSsUiK5E_oIx92QRDZUpJcrxW7v4pTVXBt0XLHZHVkVKH351YdeGepthAkcPCZRahKXJt9BuLWz7RbHnOU9Y2UMbe0KV8irOD-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcca7b928e.mp4?token=OUHK-dAQ5JsAp9-NOdS-XgwDq32Mj4g-vcjGergdM3L5COl0n5eyD4uob_QxLOEdd2EGpc_tlyCeDowlyRjLR_7AAxtZpuvlRY93CRO68s-DQE9PPc-_IZzK3NSefUA6inlO5k8wsjGtMcDG3Zvm3WAYH43uGEmyRBE1TtdCVRLn-dD6lBUMbOoR_JlJ8UNU1coSX-1wKfPg9GVM9534TnEouvNe4rE_6mi0lzL88vL-6VCXbprnSsUiK5E_oIx92QRDZUpJcrxW7v4pTVXBt0XLHZHVkVKH351YdeGepthAkcPCZRahKXJt9BuLWz7RbHnOU9Y2UMbe0KV8irOD-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
املاکی رو ببینید؛طرف یه ساعته داره جلوش گوه میخوره بعد این کصخل یجور لم داده رو صندلی که انگار تو تخت بغل ملانیاست
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69863" target="_blank">📅 01:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69862">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d1e744df.mp4?token=g64uw6Q8Imy9BPgxwv4QG292nl3sQaXGB8bZj1yE_UlpIN4rkHklfI5wXfwafpaENgSJ9oF2dhS1z9ArB9quCvhafYbMtDUoyIY2EyeRb2-jB0bkivsXKWh6k-wz_ygaudwM7GZwnE273z5wg6qSiN2cFCRYC1Rk2o3fmG4k8ThC_H8uXJTfLJ6FjRH-MRybBo2nK-nWWx2S_THtoE2xWpjP0v1piAJ6yMHqgkJ7wGUZev1QFyKTipkpK_TnJIGZxa6d2GNvmXELp0ATKZz1v0-bMxMZjetlx-IJlN2uMPFQC5uePTXu9TtKFVXS9q-Jex0GsZKx91HJPvuiUmI-Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d1e744df.mp4?token=g64uw6Q8Imy9BPgxwv4QG292nl3sQaXGB8bZj1yE_UlpIN4rkHklfI5wXfwafpaENgSJ9oF2dhS1z9ArB9quCvhafYbMtDUoyIY2EyeRb2-jB0bkivsXKWh6k-wz_ygaudwM7GZwnE273z5wg6qSiN2cFCRYC1Rk2o3fmG4k8ThC_H8uXJTfLJ6FjRH-MRybBo2nK-nWWx2S_THtoE2xWpjP0v1piAJ6yMHqgkJ7wGUZev1QFyKTipkpK_TnJIGZxa6d2GNvmXELp0ATKZz1v0-bMxMZjetlx-IJlN2uMPFQC5uePTXu9TtKFVXS9q-Jex0GsZKx91HJPvuiUmI-Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: گفتید این آخرین فرصت ایران هست چیشد؟؟
🇺🇸
ترامپ: به زودی متوجه خواهید شد
ما توانایی افزایش تنش رو داریم
خسارات های جنگ رو از طریق منابعی از ایران جبران خواهیم کرد
خسارتی رو اگه قرار بشه کسی جبران بکنه این ایران هستش
هیچ اتفاق بدی قرار نیس بیوفته
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69862" target="_blank">📅 00:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69861">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10abc62a6.mp4?token=TEKR7_SfnEddC9CN3FMMdDOefyKF55d8kREJvveUfpCEigPorE-bKpSi8Z65yKcu7CqUp6gecv29zkGos4MPTavAFrIiU0aYWbxxlPQthR6jrClhW81VOQMFaKbk97uzP-9lezr_vlfu307DUFz7db4PDQl-wBv308bk2q7p9EGP2m6R7UmTyFjRgAn9cPO33eVhxrXDuBc09Y1n6Ol52EDI5IL4KsobeY9Y59bjvIIe35dpHYdGGcwWkwE28VFjixJOLFuU5rNH0QZ6HRYIEUgjt-kXuFWHAw0kJ8Pa_0_u1nmKMyAAy5sZ6xyd0GgEjHzJuBVYfr_5nPYzP3RcEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10abc62a6.mp4?token=TEKR7_SfnEddC9CN3FMMdDOefyKF55d8kREJvveUfpCEigPorE-bKpSi8Z65yKcu7CqUp6gecv29zkGos4MPTavAFrIiU0aYWbxxlPQthR6jrClhW81VOQMFaKbk97uzP-9lezr_vlfu307DUFz7db4PDQl-wBv308bk2q7p9EGP2m6R7UmTyFjRgAn9cPO33eVhxrXDuBc09Y1n6Ol52EDI5IL4KsobeY9Y59bjvIIe35dpHYdGGcwWkwE28VFjixJOLFuU5rNH0QZ6HRYIEUgjt-kXuFWHAw0kJ8Pa_0_u1nmKMyAAy5sZ6xyd0GgEjHzJuBVYfr_5nPYzP3RcEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
پس تنگه هرمز کِی باز میشه؟
🇺🇸
ترامپ : بازه!
ما صددرصد کنترل تنگه رو در اختیار داریم.
همون طور که احتمالاً شنيديد، كل تنگه رو مین روبی کردیم. البته شاید هم نشنیده باشید.
اونا میتونن دردسر درست کنن، ولی ورشکسته‌ان؛ پولی ندارن، ایران کاملاً ورشکسته‌ست. حتى حقوق سربازهاشون رو هم نمیدن، نرخ تورمشون 309 درصده.
ایرانی ها صدها هزار نفر رو کشتن، حالا دارن تاوانش رو پس میدن.
اگه قرار باشه خسارتی پرداخت بشه به نظرم ایران باید اون خسارتها رو پرداخت کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69861" target="_blank">📅 23:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69860">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
گزارشگر: شما گفتید که این آخرین فرصت ایران بود. حالا چه؟
🇺🇸
ترامپ: شما متوجه خواهید شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69860" target="_blank">📅 23:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69859">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8eb808fce.mp4?token=qsIMToV-onKuF7zUPn6WC-txpFCralTOdXt3his5jQ53OUq7gtr1ZXqnCpYiuL5fen-qDeTZ_72r4ELeZoVd7Nc1ajqYTFrOca5Ik6TPZjElZcb2jLbKfIMKwAZDjzThlrzpNtglP3PCeexipXQmu2W9rhQwPCPHJx9X1q7RZOGLkYq6yOSbh5uhFS6QXvwUBp1VGH-IHYJgmy7wkln8lvssHiF85yQeLcAc0ENvNNXU8EZsZ9yafAjs-l-FuRK1-hgDi4IVSl951uzJfr8826EUI7zXM3qLFD4ozQi6jcgy-YPslH45YyElmIpp5DGyEBeremoWmFCauhNxiZUnxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8eb808fce.mp4?token=qsIMToV-onKuF7zUPn6WC-txpFCralTOdXt3his5jQ53OUq7gtr1ZXqnCpYiuL5fen-qDeTZ_72r4ELeZoVd7Nc1ajqYTFrOca5Ik6TPZjElZcb2jLbKfIMKwAZDjzThlrzpNtglP3PCeexipXQmu2W9rhQwPCPHJx9X1q7RZOGLkYq6yOSbh5uhFS6QXvwUBp1VGH-IHYJgmy7wkln8lvssHiF85yQeLcAc0ENvNNXU8EZsZ9yafAjs-l-FuRK1-hgDi4IVSl951uzJfr8826EUI7zXM3qLFD4ozQi6jcgy-YPslH45YyElmIpp5DGyEBeremoWmFCauhNxiZUnxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
🇮🇷
عظمایی فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی:
«اگر اسرائیل، ایالات متحده، یا هر یک از همدستان آن‌ها حتی جرأت کنند نگاهی خصمانه به جزایر خلیج فارس داشته باشند، با کمک خداوند متعال؛
چشم‌هایشان را کور خواهیم کرد و خلیج فارس را گورستان آن‌ها خواهیم ساخت.
»
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69859" target="_blank">📅 22:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69858">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c15a39d1d6.mp4?token=tH2PFWVmoeUp1XQrbhKv3pe3rLSe_cpg3vgBARwIuuKJC4SIF1p4qxMn_JnvnrH-Q2J1oggAmE9ZqiJLgn828O-vmFiVqLtkmnF-Jp-rkz0oMyS1rbG_acofXdaShGlh7VxCTYq4BTcwOXdQsYs_jlV0-Zfi82f0raxBQsJNW26In_12TD5FtAlK_tWhXfxChad0STMgoWc3spk6NR4cPeNyPe-tAjfjRiAWhPYbPQgsJxj8KfPYsT_c5FKPhquEAMm54DchQ40Eoey9YCK9UtTDOka68HA71qwnCzvdxtva2UGw5kCvN__5cEtq0BSylokZXoipk7zpwHzno-XOwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c15a39d1d6.mp4?token=tH2PFWVmoeUp1XQrbhKv3pe3rLSe_cpg3vgBARwIuuKJC4SIF1p4qxMn_JnvnrH-Q2J1oggAmE9ZqiJLgn828O-vmFiVqLtkmnF-Jp-rkz0oMyS1rbG_acofXdaShGlh7VxCTYq4BTcwOXdQsYs_jlV0-Zfi82f0raxBQsJNW26In_12TD5FtAlK_tWhXfxChad0STMgoWc3spk6NR4cPeNyPe-tAjfjRiAWhPYbPQgsJxj8KfPYsT_c5FKPhquEAMm54DchQ40Eoey9YCK9UtTDOka68HA71qwnCzvdxtva2UGw5kCvN__5cEtq0BSylokZXoipk7zpwHzno-XOwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باشگاه مختلط تو قیطریه تهران همراه با استخر جکوزی سالن  ماساژ سالن بیلیارد سالن بولینگ و...
😟
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69858" target="_blank">📅 22:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69857">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MipWUjnUZhQjit_i0VjWiYZ1eIVevu34-n1Rrqnjp6pb29T0Tc17Pml5yBgjbW4D2_Be1gXSI5998OjgH1Xmu9Mz1g8USg023RRk51yL2aulhlnyoNWDuYmCDrAAFaRWWT3jwYAmJbO_tXBtR_a0cT7nvYReMth1yyz_37NsWUJ8bP4QEwIMYIJJIwxu8AiPO9KeiJaOiP7fRy3nUGTwUunXAESm_vy2cpKOgSen5_A7BYaXPonhWqMY-PCgzioBnSIS2FBcMf7ScEEz1IEYaN4LSuaOmxlhrInfQw48rAfaK41e01_a8_PrvmtmzRGrdzeTm7VoL0RpUcxJpZLLbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ درباره ایران:   می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار غرامت بابت خسارات وارده به خود در جریان درگیری نظامی پنج ماه اخیر هستند (درگیری‌ای که آغاز شد چون آن‌ها نباید به سلاح هسته‌ای دست یابند)؛آن هم در حالی که این موضوع هرگز در…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69857" target="_blank">📅 21:26 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69856">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79470446aa.mp4?token=f5w1OySLunKHzTSo7at1xagE0E7kWuPGcpiUh0Tuleztxt42x9WrPUGglc1m_dTXkMVz2vwAQhzhyplzW3_nYYVMCpWbfSNpdVTzxWF0yKwY76bU6CpzmvSB1whYEuQsZzOK8j2P9U2okiVL0a0Z8RIVQZ3JOLa6Td7-F-FaPYhCEE4Sk99ejewvENURZ6Gt5FkGc68T0XBIFhS2SrjW-ja8fmiMBbEprPxN-wd_klaCnaip-sxGpgE_3bEUNW7GYR9Oi8R2EhEe1Ge1loapFTTe91kvgCI0LvtnIwlGM_4bqOWOVR5lmm7ziYD7sOPbxdw6zllhCaQCr-Bogj1r_FUPQKqM6heBRhTpE386_QkeTbG7Wqte-Zgag8x3rJi0Jx-2RA1c3duyixelIjA2p8JpqTGPlq4VuOp6tVBGmip67eC9a-yQ99SKxyPFOzHhkT10nOaxiKftJGMPAu-0tkQWtHZPGQkJzQdnpix4vcHtzmFI_DYkJvin75v9t7_kNuAynV4Cs0NGyIlfZFWh_Bo1eazTd9HS9r5HAQoP9d43SP9g38jyzodTCCGy7PhePcS29bu4BdELvnmvwwSkpB5JVUj4dd0sIMAEosc1xojpZuGDueCV4loiWgxuzeiFadiIVGWAlssfsoK8u_0e90WzVj3Sdyt3o0xt08HBilk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79470446aa.mp4?token=f5w1OySLunKHzTSo7at1xagE0E7kWuPGcpiUh0Tuleztxt42x9WrPUGglc1m_dTXkMVz2vwAQhzhyplzW3_nYYVMCpWbfSNpdVTzxWF0yKwY76bU6CpzmvSB1whYEuQsZzOK8j2P9U2okiVL0a0Z8RIVQZ3JOLa6Td7-F-FaPYhCEE4Sk99ejewvENURZ6Gt5FkGc68T0XBIFhS2SrjW-ja8fmiMBbEprPxN-wd_klaCnaip-sxGpgE_3bEUNW7GYR9Oi8R2EhEe1Ge1loapFTTe91kvgCI0LvtnIwlGM_4bqOWOVR5lmm7ziYD7sOPbxdw6zllhCaQCr-Bogj1r_FUPQKqM6heBRhTpE386_QkeTbG7Wqte-Zgag8x3rJi0Jx-2RA1c3duyixelIjA2p8JpqTGPlq4VuOp6tVBGmip67eC9a-yQ99SKxyPFOzHhkT10nOaxiKftJGMPAu-0tkQWtHZPGQkJzQdnpix4vcHtzmFI_DYkJvin75v9t7_kNuAynV4Cs0NGyIlfZFWh_Bo1eazTd9HS9r5HAQoP9d43SP9g38jyzodTCCGy7PhePcS29bu4BdELvnmvwwSkpB5JVUj4dd0sIMAEosc1xojpZuGDueCV4loiWgxuzeiFadiIVGWAlssfsoK8u_0e90WzVj3Sdyt3o0xt08HBilk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله تند مجری صداوسیما به علی دایی:
وقتی جرائت نداری جیگر نداری به دختر اونور آبت چیزی بگی پس اینجا هم خفه شو لال شو
یه گروهی گول میخورن میریزن کف خیابون بعد از این دایی و خاله ها زیاده هشتگ نه به اعدام میزنن
یکی از این آقایون مشهور دخترش مورد دزدی قرار گرفته بود کم مونده بود دزد رو بکشن بعد همینا هشتگ نه به اعدام میزنن
بعد این وحشیا این بیشرفا جوان مردم رو به شهادت میرسونن یه عده یاد حقوق بشر میوفتن
اعدام نفرت نمیاره شماها نفرت انگیزید شماها ترحم انگیزید
ولی یه پلیس یه گلوله شلیک بکنه داد میزنن عای دیکتاتوریه عای خاک خون کشیدن
شماهایی که لال هستید همیشه لال بمونید حتی اون ور آب
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69856" target="_blank">📅 20:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69855">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCryMxwQ7tObpVshmg39x4z9f_b1cC0oX_V7vZB5iEF1ZWcDnDG9IWCGs_agJHVd6ojkd4D9KMcjpuqYEogtvkiWM_QsvexZyPWge0hfd8GSEXtZuwoTHQiwuEKdDqxrBSAximumQdNMy1gaKPwwni2rbdp_kNjg5efEg8CguOjFvOs9Cl8LV0-VZR_k18HAYLAjf9vJd6IHAJuWaIpr8BFtscjL2nwlZO8vd7kl1UBVFkqUwv6eHpOW7x18U9QmvvXQgpBITtZ89tgcKQHxefcPtv-jG-Xtoz05X9qp4LcjpLL02_p3dwX-wzzE5K47zHZxE6HC9JAaCiCTwmz8AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ درباره ایران:
می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار غرامت بابت خسارات وارده به خود در جریان درگیری نظامی پنج ماه اخیر هستند (درگیری‌ای که آغاز شد چون آن‌ها نباید به سلاح هسته‌ای دست یابند)؛آن هم در حالی که این موضوع هرگز در هیچ‌یک از مذاکرات یا دیدارهای ما مطرح نشده بود!
اما این ایده جالبی است، چرا که من نیز اکنون متقابلاً از ایران درخواست غرامت می‌کنم؛ غرامت بابت تمام کسانی که آن‌ها با بمب‌های کنار جاده‌ای و در درگیری‌های متعدد — که به آن شهرت دارند و در ابتدا تحت هدایت ژنرال سلیمانی انجام می‌شد — به قتل رسانده یا به‌شدت مجروح کرده‌اند؛
از جمله خانواده‌های کشته‌شدگان حادثه ناو «یو‌اس‌اس کول» (USS Cole) و هزاران نفر دیگر که در میدان نبرد جان باخته‌اند. به‌علاوه، باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران طی ۵۰ سال گذشته به قتل رسانده نیز غرامت پرداخت شود، چه رسد به آن ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
من به نمایندگان خود دستور داده‌ام که این موضوع را قاطعانه در تمامی مذاکرات آتی بگنجانند.
از توجه شما به این مسئله سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69855" target="_blank">📅 20:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69854">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHsAx5Z300f4CEVsFtZFLgD9WAz7NveKBKpwZ0EtNt8lo3O4W98uljRQpgEKCZHe04CCrAwCBzJCtH4RfAMkNOimas7aIKChnqxNe6nHe3VqefL5jfJa61-61cSdS4VArcPUjhfbwCl-cRmzZziwDv0McV8F5u0k4ZrpqoP6Bx8HoofqEzx5GnJVW6EBoaUx0FBWtAH7k3j4nX037f86dFYCOK5eUiyEPxkMtnobzO6Ov7yoCcP_IYlBjyzk-tTSGLM8Opr4Lu5yT16417SDJl9q5C3m7SLwHCVfywcQXVhUIxFc5-quFj9iPquhbYm0nhA53NtaMDL3ro_utZa-jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
مرندی:
‏ایران آگاه است که نیروهای رژیم ترامپ در کویت، امارات متحده عربی، قطر، عربستان سعودی، بحرین و اردن در حال بسیج برای یک حمله برق‌آسای بالقوه - احتمالاً در کنار نیروهای اسرائیلی - علیه مردم ایران هستند. جمهوری اسلامی با پاسخی سریع و کوبنده آماده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69854" target="_blank">📅 19:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69853">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🔴
🇮🇷
لیست فرماندهان جدیدی که مجتبی خامنه‌ای انتخاب کرد:
سرلشکر  علی عبداللهی به عنوان رئیس ستاد کل نیروهای مسلح
امیر کیومرث حیدری به عنوان جانشین رئیس ستاد کل نیروهای مسلح
سرلشکر احمد وحیدی به عنوان فرمانده سپاه
سرلشکر مصطفی ایزدی به عنوان جانشین فرمانده کل سپاه
حجت الاسلام طائب به عنوان رئیس سازمان بسیج مستضعفین
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69853" target="_blank">📅 19:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69852">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f1723f2a3.mp4?token=It_13FwSqKyrHTo8uYbUc-TJVtr1yp2lFI4OLUGFvLTpKktNLQ9G5e0CDwHEQAIegBaffYF1dYmzEHFuGna8LmrtM5m-k19JvfUxup1p8GTR7q6UuvJNpJYEdOjQa25SQxlK7yQpckWEMbhhME06GAi6yOKXbLeVC12VDSN38XymjkQuOEQjohJYEKupcYyL0RDlNb41HRWprohyRMA3l62ApE2ipHTQrG12NgrTn0FQVEZRG6m6jOisGa2I6BvDw3CEqCk97VAjZwbz25rHzhrXCwRbgyVvPrHCZSmPsg_rl4-lj9keUZcP72cc8hoptqYVXu6SV6iSaP-pi8kvSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f1723f2a3.mp4?token=It_13FwSqKyrHTo8uYbUc-TJVtr1yp2lFI4OLUGFvLTpKktNLQ9G5e0CDwHEQAIegBaffYF1dYmzEHFuGna8LmrtM5m-k19JvfUxup1p8GTR7q6UuvJNpJYEdOjQa25SQxlK7yQpckWEMbhhME06GAi6yOKXbLeVC12VDSN38XymjkQuOEQjohJYEKupcYyL0RDlNb41HRWprohyRMA3l62ApE2ipHTQrG12NgrTn0FQVEZRG6m6jOisGa2I6BvDw3CEqCk97VAjZwbz25rHzhrXCwRbgyVvPrHCZSmPsg_rl4-lj9keUZcP72cc8hoptqYVXu6SV6iSaP-pi8kvSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇫
طالبان به طور رسمی برده داری جنسی زنان رو قانونی اعلام کرد تا محدودیتی از این لحاظ نداشته باشن!
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69852" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69851">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69851" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🙄
همه بت باز های حرفه ای دنبال
🔞
شکار این بونوس ها هستن
✅
لیگ های معتبر اروپایی شروع شده بهترین فرصت برای جبران ضرر های جام جهانی
💯</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69851" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69850">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAW4iPz5OkVvZ_gvKw49nOYBQBsRRj_CmKTLn_noftg9cUzcaD89fuCA4Vo9zKaGFMjngkV42xghC78D3cZZgKPe-sswesMILHe5cEFp6rimNkr-yPm1NTuh_atQ6cMEMqlk3yurA2RmZOHZpNyrEIXpZcisXWX9DhtPc4yoDhs647ydD2Nykg1jfFKFit3gQjMlIjRafM_YpAYt2xgFz_-rdiJgA3H3H7-vi-M71eyIGOve41Rnz8x62hDXgEZ0xAHVf-KKKvzROukR6-6t6YZ9Alyym18H4jJg3yKAnuOoSjMFmAUXZ9HHxaUD6BS3RUK7z4ZRumdq-C9yzU31Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤔
شروع رسمی لیگ های اروپا
❄️
🆕
بهترین فرصت برای جبران ضرر های جام جهانی با جشنواره رویایی مرداد  ماه
⚠️
هر افزایش شارژ مساوی
2️⃣
1️⃣
🔣
شارژ بیشتر بدون محدودیت
☄️
به همراه
🤩
🤩
🔤
کش بک باخت همه روزه:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
g19
@betinjabet</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69850" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69849">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
⭕️
مجتبی خامنه‌ای تا ساعاتی‌دیگر اسامی فرماندهان جدید نظامی را پس از بیش از ۵ ماه رسما اعلام‌ خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69849" target="_blank">📅 18:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69848">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a2288e087.mp4?token=rG7Ct1GHVEvnSzTfUyL9B8nnEREn-fyqckn_lnI_8rlaiIJELqJWEo6Ut9SKEDW2S_1AqtBcH10WhuG0WrV9R9JP9YYIgBwpBh0gHmuYTIA-xkyRQGofvAL9gx0obEgY_QzxV2q7XnV1Bd3iVaBFRFt_MM1PdY_7wJcL_cLLNfZwt_rjpQ88QDBWq8JL57nzVzNaRlorq4ZNA_lE_N0LQ9GzayPB9-lW7nP0JgnFWnYXLYkMZJQw5gFbWykeR43-njWZ6MJiOW7VfvFd5uwEZDT_e3aiFJ6odygaziW-wW2p-FN28xLkUXJuynOlk0n_S1PF26oE2Tyl3h3GzVKe6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a2288e087.mp4?token=rG7Ct1GHVEvnSzTfUyL9B8nnEREn-fyqckn_lnI_8rlaiIJELqJWEo6Ut9SKEDW2S_1AqtBcH10WhuG0WrV9R9JP9YYIgBwpBh0gHmuYTIA-xkyRQGofvAL9gx0obEgY_QzxV2q7XnV1Bd3iVaBFRFt_MM1PdY_7wJcL_cLLNfZwt_rjpQ88QDBWq8JL57nzVzNaRlorq4ZNA_lE_N0LQ9GzayPB9-lW7nP0JgnFWnYXLYkMZJQw5gFbWykeR43-njWZ6MJiOW7VfvFd5uwEZDT_e3aiFJ6odygaziW-wW2p-FN28xLkUXJuynOlk0n_S1PF26oE2Tyl3h3GzVKe6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان درباره مجری و کارشناس‌های برنامه به وقت ایران:
این همه علم رو از کجا آوردید؟
چندتا جوون نشستن رو صندلی و درباره اقتصاد، سیاست، جامعه شناسی، کشاورزی و... نظر میدن.
از چهارتا جا یسری اطلاعات ناقص می‌گیرن و بعد درباره‌اش حرف میزنن و نسخه می‌پیچن و جامعه رو منحرف میکنن.
من 18سال تو دانشگاه درس خوندم و استاد تمامم، الان فقط اجازه دارم درباره یه گوشه قلب که تخصصمه نظر بدم نه کلِ قلب، اونوقت اینا...
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69848" target="_blank">📅 18:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69847">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7c4253089.mp4?token=ftkS-Jw3Mze2P3QCxz0ULZHU2xzh7CiCrO1PdwaqYHZv_2DMpFGWHxe45RgSAMTreINafYgoUAzrEs5mjFOY5Nv9GyKnQLT68EhR1G4GVwo-GRGqW9DmeS1TwAf2eGt2css0r-6XVPtFB8hCUagCy5Vnmy_cr_8xdputLCqgyb1YzpovMkg_bzjK61EfeGW-MVXiDN_G5NzHprCyvRmjSxwOW9pruHyS7kwdTAEFCEsdEYA12vvtWh_U8RAbk7-cyvCzQki8AdVchYFjUBP5kGEKQ1S_xO1G_O4Agqk4jLL17e6uw0Z5yqrBqelvNt5NjHYL3quHIGZ_eDcuw4Pu3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7c4253089.mp4?token=ftkS-Jw3Mze2P3QCxz0ULZHU2xzh7CiCrO1PdwaqYHZv_2DMpFGWHxe45RgSAMTreINafYgoUAzrEs5mjFOY5Nv9GyKnQLT68EhR1G4GVwo-GRGqW9DmeS1TwAf2eGt2css0r-6XVPtFB8hCUagCy5Vnmy_cr_8xdputLCqgyb1YzpovMkg_bzjK61EfeGW-MVXiDN_G5NzHprCyvRmjSxwOW9pruHyS7kwdTAEFCEsdEYA12vvtWh_U8RAbk7-cyvCzQki8AdVchYFjUBP5kGEKQ1S_xO1G_O4Agqk4jLL17e6uw0Z5yqrBqelvNt5NjHYL3quHIGZ_eDcuw4Pu3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
فیلد مارشال محسن رضایی (1392):
اگه آمریکا به ما حمله کنه ما همون هفته اول هزارتا آمریکایی رو اسیر‌ میکنیم و بعد در ازای آزادی هرکدوم چند میلیارد دلار از آمریکا پول میگیریم و اینطوری مشکلات اقتصادیمون هم حل میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69847" target="_blank">📅 17:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69846">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b47958b9.mp4?token=JqtXJe5J5rctee-lDU1uIn17pAPS6ZmTZ-dZsffUpAD0eFqwWoq2vSNryui8_j2E2Rc479aY3962hKBCHFQkmEKJ7SsABHdXf9Vp-9-wpUEGGbgPLorzRUeLWsGyXqwLNdAxWCB-m2_8oD042K08Xpr6MXZAHVMzT0YdJMozeIPG6nJ43gO1z-6IWeweFDvpqLLh0D40NnrQrVhtXFl0AU8JpyDuO7bVbVeeWvKoXbKQjloJjVwOhxl3wbii61XqINn79trokk-0Si_IcmkNAX7VkRq8ok6UAmtQx-X49kYazsXu7Au6zPEdwK1TBd6mCREMy--D3YAuAM5pLuF-kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b47958b9.mp4?token=JqtXJe5J5rctee-lDU1uIn17pAPS6ZmTZ-dZsffUpAD0eFqwWoq2vSNryui8_j2E2Rc479aY3962hKBCHFQkmEKJ7SsABHdXf9Vp-9-wpUEGGbgPLorzRUeLWsGyXqwLNdAxWCB-m2_8oD042K08Xpr6MXZAHVMzT0YdJMozeIPG6nJ43gO1z-6IWeweFDvpqLLh0D40NnrQrVhtXFl0AU8JpyDuO7bVbVeeWvKoXbKQjloJjVwOhxl3wbii61XqINn79trokk-0Si_IcmkNAX7VkRq8ok6UAmtQx-X49kYazsXu7Au6zPEdwK1TBd6mCREMy--D3YAuAM5pLuF-kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی سمه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69846" target="_blank">📅 16:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69845">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37165ac1ad.mp4?token=kke_YsYQ3hmJpx_EUfyBazUDNqUsQWtC7A1MVlZxTTfGgCLZMxf008GCf7SSJCperflz4uFWEa3RIpraxFt8lNEqCCu4cAuZVoW6d_ZwbnQ9hAQa5tK8rMncBYex3vX62XXzpLClVujBkIq1gNSKM1BxaNEtMydYCcptVue6gWj8rkZ7rvBpcqEKq6wCTQK7SfEE9cyHDcTjdEdqiK5xZSqlLEqNScAkYwSN6iqE7ED8dQVLhyLXlhtBSVrsbBSvet9Gv7W4ge7mutVcWwuygDyG7uW-oLJKopHWVQ4QDx8T_EenTviTyJJGbVr0x2AL-vD2rzatBhJDxx5VPimJJj35FEJ9NSNocPyqCohsIS9z3JYhPPDZ9zkfMDdy7MjgQxn3Ag_IeIqfpF6-Pqr1rmVtmiMnM3brn__mAp0WIxmmAc4tiE0h6eoZ6GbKAVmqwOXFQWHo7_q_yNsBZPTO4pojvb9x0RlZGrSFyEekjt7rtcdnncTtDsUDE6wquwqfuGff2KcJDp5yPcWG3cqOMrkpXAXibQVNWUaOWUDXdBZxR4NHBds4ZJFORPj2CpXJX6gzr16VqFQjcVOvjnRDmPkRSWZqD7mLSiz2qQcs6IqCxaJIH62p0iZj1hS-JhxD6VKyWyokKKsO5Wr_oWZuPcO_VU3PlaB2shCfo277-Oc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37165ac1ad.mp4?token=kke_YsYQ3hmJpx_EUfyBazUDNqUsQWtC7A1MVlZxTTfGgCLZMxf008GCf7SSJCperflz4uFWEa3RIpraxFt8lNEqCCu4cAuZVoW6d_ZwbnQ9hAQa5tK8rMncBYex3vX62XXzpLClVujBkIq1gNSKM1BxaNEtMydYCcptVue6gWj8rkZ7rvBpcqEKq6wCTQK7SfEE9cyHDcTjdEdqiK5xZSqlLEqNScAkYwSN6iqE7ED8dQVLhyLXlhtBSVrsbBSvet9Gv7W4ge7mutVcWwuygDyG7uW-oLJKopHWVQ4QDx8T_EenTviTyJJGbVr0x2AL-vD2rzatBhJDxx5VPimJJj35FEJ9NSNocPyqCohsIS9z3JYhPPDZ9zkfMDdy7MjgQxn3Ag_IeIqfpF6-Pqr1rmVtmiMnM3brn__mAp0WIxmmAc4tiE0h6eoZ6GbKAVmqwOXFQWHo7_q_yNsBZPTO4pojvb9x0RlZGrSFyEekjt7rtcdnncTtDsUDE6wquwqfuGff2KcJDp5yPcWG3cqOMrkpXAXibQVNWUaOWUDXdBZxR4NHBds4ZJFORPj2CpXJX6gzr16VqFQjcVOvjnRDmPkRSWZqD7mLSiz2qQcs6IqCxaJIH62p0iZj1hS-JhxD6VKyWyokKKsO5Wr_oWZuPcO_VU3PlaB2shCfo277-Oc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بقایی سخنگوی وزارت خارجه:
تنگه هرمز از زمان حضرت آدم تا ۹ اسفند برای همه باز بود
ادعای ساخت سلاح هسته‌ای ایران توسط نتانیاهو دروغی بیش نیست
به ترامپ بگم که ایرانیان شطرنج بازان حرفه‌ای در طول تاریخ بودن( ترامپ جنگ ایران رو به شطرنج تشبیه کرده بود)
هیچگونه مذاکره مستقیم با آمریکا نداریم
باز شدن تنگه هرمز منوط به لغو محاصره دریایی هستش
نگرانی بابت پیمان دفاعی مکه نداریم چون همسایگان ما هستن
بحث کنوانسیون دریای خزر به مجلس ختم شد و تصمیم نهایی با اونا هستش
درباره عمان نزدیک به یک تفاهم هستیم و به زودی نهایی میشه
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69845" target="_blank">📅 16:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69844">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c431777b9a.mp4?token=KnUvsHsx1j4p52TOcjZ7WE6W81c1u7suQHaimkSisk3Z5Rj_gX2nFJ_2tJd5oM5-80-Ez5ub9iIfGMoY2iAye6-8g572LYjENnknsLx7ElVTSt-ZrmNroyebr6Tx0UzHOcN0h_LpjZx_VhustaDb8lu80dDE2tJnZTs2FW24fJRYYpjYqYdDk94jD1WH7FeodScMKP9BfO2SgEXIV_SxzPUW08gEbzjdQKme40B1PDdJGQKEabJn3JvlIm6uIJsGZ-6PPFWKl23IAGFWWOI7zRId8Ykn8cZyaapmxU4BXBsvKE-0uZEaEkBeLo8D52r3Kt7pm_ug201dFWZky_waozzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c431777b9a.mp4?token=KnUvsHsx1j4p52TOcjZ7WE6W81c1u7suQHaimkSisk3Z5Rj_gX2nFJ_2tJd5oM5-80-Ez5ub9iIfGMoY2iAye6-8g572LYjENnknsLx7ElVTSt-ZrmNroyebr6Tx0UzHOcN0h_LpjZx_VhustaDb8lu80dDE2tJnZTs2FW24fJRYYpjYqYdDk94jD1WH7FeodScMKP9BfO2SgEXIV_SxzPUW08gEbzjdQKme40B1PDdJGQKEabJn3JvlIm6uIJsGZ-6PPFWKl23IAGFWWOI7zRId8Ykn8cZyaapmxU4BXBsvKE-0uZEaEkBeLo8D52r3Kt7pm_ug201dFWZky_waozzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
پزشکیان:
با رهبر هفت ساعت دیدار داشتم و درباره مسائل مهم کشور باهم گفتگو کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69844" target="_blank">📅 15:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69841">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nkrhsexXG_ORyYeCf66fr-_DWm-wOCjA12hmv2aysgAyp4pAep4qndzqD3VqIddhu6DcvEBmxVRRTscKK5wMNDrNF1xircWkpUbaVuNX5Wc41Y6vISjKWpB1OuUsA53FidszJ5kbTYqxNavtjeW5dc6yKAEokxKQ4zVzdV5lzv34jbXcxdM-_MBWtjjS8L5ld5PzajXiHkmyYRnczuoLouUS6QPWGU0LpeEsb-DSGx7wg1PlkQn6Iw7KdrfBW5K7KSNsuIaWEeCUI9ACJgMS2B_QfJashX1LFZJqvUm5g_jsTyBGRKHU8yl1EIty-iwTE0sFnWFFcvIZbXzL1hXi3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vUYsgp7OQ-SBU-xbhAkv1HzVZ4RKd_lpJpgr6zhJzHRVwzISdpOF6UPpQ0dV2FqqNa6iQiPqwcfdgfSjIP8gdijMiRNJjKfrXDvi6QWt3_TKNwb1Rs2-NASNfx8FwODC-S5x2tS1F9HoZzzKCKlRbnrQ5g5Rs7vM6G3JpaYnDOuZzF-6xOhB9s7T-HINGwDarh1ISufR6P9hinK0jnjK2HfOwCgPcM7pFYuUf4bwdZWbT2huLD1vhhkf1iZtDWkfbA6Re-kXPCYcdhn39T8OziBiVU0MYfPO_CxtsL4yKYFLdtzej_8aTQA84gK06NEE5ByConMNzGcZ6xPlWLNI0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92217bf769.mp4?token=bY_I45_3kvcW3Y_bjHyf13eeChim9xpxokGOAip9-7TMPY77o7aBMMqLH6DeMhIq_YDkbzOSXqT2lCgKFMyTQVOr7XSQGFwM_3OCD7Hxkfi8e_n5U52kezWJXOsdri5IaCVQtx0AbsyQj2y49XKTSJ1_H3J5yLRcCZMD7OpVxeP59YXSF7DE0kG01yxYDwrbi-12MP22IIH81Iq_rl98sDE8rzVq9ramAPyhRsNeuO01j8UYWf0Jhe8o8VZ1U5yPtxqcglnPlq1M3bi3wG3RLU5e0CuoaXrvrDlA46DrVfANZ7MXMhyeEothJNvoJZ11W6Vg6I2Kfi5Vd615tqLjBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92217bf769.mp4?token=bY_I45_3kvcW3Y_bjHyf13eeChim9xpxokGOAip9-7TMPY77o7aBMMqLH6DeMhIq_YDkbzOSXqT2lCgKFMyTQVOr7XSQGFwM_3OCD7Hxkfi8e_n5U52kezWJXOsdri5IaCVQtx0AbsyQj2y49XKTSJ1_H3J5yLRcCZMD7OpVxeP59YXSF7DE0kG01yxYDwrbi-12MP22IIH81Iq_rl98sDE8rzVq9ramAPyhRsNeuO01j8UYWf0Jhe8o8VZ1U5yPtxqcglnPlq1M3bi3wG3RLU5e0CuoaXrvrDlA46DrVfANZ7MXMhyeEothJNvoJZ11W6Vg6I2Kfi5Vd615tqLjBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
دیروز عراقچی برای مهمانان خارجی تو ساختمون وزارت خارجه بساط تعزیه راه انداخت
😳
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69841" target="_blank">📅 15:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69840">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7709b161ed.mp4?token=tr7my-_XCeqCDW6GFM9Z5s6ImAa6UJ3p8eMwGK8y6B6ckP5QzpJl-P--5UuuHPHt4KRZCx0DUKVMZzwjxmMKGbwDaHmEhs6JsyUWR_UvRP4Xa1EKZ9JcaDmwGa0B3d7qMhb3jq7Aj-Uv8eCyDAuCJfGCODXQAaAM0M4-42eZLk00rGknR_EbcWli6pG_sHCpq3-G119EEIZEpkkZVtaIpFpURQSe42-QEtVr10Hm7OitkrQsGGntWvI0Be2NjV3MWEMgfPigHWStKYoAY7uDV9-bIuyvw__cDwBf-zXSBTmLGs2RWCXwLd8551hInTsIAVJlbRfufxjmQS2fs8radw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7709b161ed.mp4?token=tr7my-_XCeqCDW6GFM9Z5s6ImAa6UJ3p8eMwGK8y6B6ckP5QzpJl-P--5UuuHPHt4KRZCx0DUKVMZzwjxmMKGbwDaHmEhs6JsyUWR_UvRP4Xa1EKZ9JcaDmwGa0B3d7qMhb3jq7Aj-Uv8eCyDAuCJfGCODXQAaAM0M4-42eZLk00rGknR_EbcWli6pG_sHCpq3-G119EEIZEpkkZVtaIpFpURQSe42-QEtVr10Hm7OitkrQsGGntWvI0Be2NjV3MWEMgfPigHWStKYoAY7uDV9-bIuyvw__cDwBf-zXSBTmLGs2RWCXwLd8551hInTsIAVJlbRfufxjmQS2fs8radw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وایرال شده از قیمت یک پک آرایشی که ناقابل سه میلیارد
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69840" target="_blank">📅 14:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69839">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gr7lFUWdxmQmfiUh0dyFkwE9scOU7dxW6LF62Jz-oqazQb88ib1l9Y5a7s9ot6v6cDjbB3C3FStDYUmnoaP_Nyi1RxGZGWC_JoiEgJtqJTCByz8EINqHNP5y_Bfbw1VEoagTdkgx3ppFmSCx7VF7VSG_BPC2FQaRivtRGckZHlgGOUZHgd-MMhsehNjdMSdHdD7jzFmrv58b4vmcFzhUlZA-glf7OGrqtu3uw6rw7HQVfza2fl4HeM-mw-hPaT9MVCe_gdxFREWAoqs09y6n9vqhJOKFmXonzFJaPZTifczkJn4Hy0MiNZam3ivevOqgWvgRHfRdyb3EdN3M7WCgIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
یک مقام ارشد آمریکایی به من گفت که کاخ سفید از اظهارات نتانیاهو درباره طرح غزه «ناراحت نیست» و آن را بخشی از فضای انتخاباتی اسرائیل می‌داند.
این مقام آمریکایی گفت: «ما نیازهای سیاسی "بی‌بی" را درک می‌کنیم. تا زمانی که او به انجام آنچه ما می‌خواهیم ادامه دهد - به‌ویژه در خصوص مهار حملات به غزه - مشکلی با این موضوع نداریم.»
به گفته یک مقام آمریکایی، نتانیاهو هفته گذشته در تماسی تلفنی با جرد کوشنر، فرستاده رئیس‌جمهور ترامپ، وعده داد که علی‌رغم تردیدهایش، به این طرح ۱۵ ماده‌ای فرصت دهد و حملات به غزه را محدود کند تا روند خلع‌سلاح این منطقه بتواند آغاز شود.
از آن زمان تاکنون، اسرائیل حملاتی علیه غزه انجام نداده و ارتش اسرائیل (IDF) به‌تدریج در حال عقب‌نشینی به سمت «خط زرد» است. هم‌زمان، آمریکا و میانجی‌گران خواستار آن هستند که حماس روند خلع‌سلاح را آغاز کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69839" target="_blank">📅 14:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69837">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d242d991d.mp4?token=KdMoYsRlquVKf7PGuCiJC2TkV2vEWekABxw--cMmNipF5nTCQaciT6a8BX9BGiDqtgeR0gRATq0M5luLE7PoYmEebtKaIKhJiN_kiTszUKFTiH1jSxZvt_P_4WvFk8ZsbFFP9iK0iBCaMRZlIG0WRyoFWaUAfpwgrS5CEQZ6QyoBxlzh15p-1UO0hHVRiR7W38Lmv0SrwkFM-oUWuzHeS_PLeWda6VPBsWYhUTXwQCjdM2ObfU76StE0iH96VDR8ebK850Vfyw3wKHLK4fbADqaUImAuTkxaJlkcXOB6ygjX4MpPUKY-tHCHfvft_KjKBxjh7c3U1HHHdLqviVs52w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d242d991d.mp4?token=KdMoYsRlquVKf7PGuCiJC2TkV2vEWekABxw--cMmNipF5nTCQaciT6a8BX9BGiDqtgeR0gRATq0M5luLE7PoYmEebtKaIKhJiN_kiTszUKFTiH1jSxZvt_P_4WvFk8ZsbFFP9iK0iBCaMRZlIG0WRyoFWaUAfpwgrS5CEQZ6QyoBxlzh15p-1UO0hHVRiR7W38Lmv0SrwkFM-oUWuzHeS_PLeWda6VPBsWYhUTXwQCjdM2ObfU76StE0iH96VDR8ebK850Vfyw3wKHLK4fbADqaUImAuTkxaJlkcXOB6ygjX4MpPUKY-tHCHfvft_KjKBxjh7c3U1HHHdLqviVs52w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فوران یک آتشفشان قدرتمند در جنوب غربی کلمبیا
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69837" target="_blank">📅 13:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69836">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81027c9c4b.mp4?token=pFnO7iLDQ3zuCvXZNw5M7FX6ltWw63sblTFQpbB4w2NLjafgC1BBt0Xs7wqZkEuAgYcwjW83BvkrL3jV2XiiCxPyopVm2N5lvMB0YXnXkQPBBVLj3fNoJZJV_Yef-rllcQ-BFifiS-pYPZgRyyyKpNJ9-qWIAcdMOA-GLFlPNM7EKmpVH1n4JLx8Nd13kPy-eYNN_lnG_n-VTOY13mbCh0mcxrGsZBQ28jukQH2z8zK91vCxx6jBOrzWojZ7M1xEyeVR1z38Sq2ZNN6XhTVzrDO19cAPzgRMRLphowGBTe_B0JTVAVCphnCT3tz4hFBzhceWtmg2SRQ-DpOJenRbVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81027c9c4b.mp4?token=pFnO7iLDQ3zuCvXZNw5M7FX6ltWw63sblTFQpbB4w2NLjafgC1BBt0Xs7wqZkEuAgYcwjW83BvkrL3jV2XiiCxPyopVm2N5lvMB0YXnXkQPBBVLj3fNoJZJV_Yef-rllcQ-BFifiS-pYPZgRyyyKpNJ9-qWIAcdMOA-GLFlPNM7EKmpVH1n4JLx8Nd13kPy-eYNN_lnG_n-VTOY13mbCh0mcxrGsZBQ28jukQH2z8zK91vCxx6jBOrzWojZ7M1xEyeVR1z38Sq2ZNN6XhTVzrDO19cAPzgRMRLphowGBTe_B0JTVAVCphnCT3tz4hFBzhceWtmg2SRQ-DpOJenRbVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشتیبانی سنگین و فوق العاده از نیروهای زمینی آمریکا در جنگ افغانستان ( طالبان ) توسط بالگرد آپاچی ۶۴ با توپ ۳۰ میلی متری M230 Chain Gun
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69836" target="_blank">📅 12:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69835">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ea33d827b.mp4?token=mH6wzoQLqyO3H2yZqeDY7IEySk-dEf5eow7Xm04Ha2ev7ENjmuMB20FRa06HDBeZGedZ0yGbrLmPZwqs8WdHO3K4xJddT8UqLWLMJYieAOEQ9O_ojZLZsK3a0l1r4PQIz4TsJMcITpLe1M8DHwcLg7oPKenSlB7a7nEDEw_D8Lbkrd8EFbHabmes-kJIdXV44mCvZH7FBlpUapbwlYqthSRDvXavh36-jNRu3-4SvbJnIKlNFW05LDNnYOBFQBjIVV0lwdCi6cg4aXWDIRDLjE4I7mUGwg1CdfZwbZ_XPz2aoG5t3KIZQ-ajKAZW8bE14-VI-xdrHUip8FYgk-IfRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ea33d827b.mp4?token=mH6wzoQLqyO3H2yZqeDY7IEySk-dEf5eow7Xm04Ha2ev7ENjmuMB20FRa06HDBeZGedZ0yGbrLmPZwqs8WdHO3K4xJddT8UqLWLMJYieAOEQ9O_ojZLZsK3a0l1r4PQIz4TsJMcITpLe1M8DHwcLg7oPKenSlB7a7nEDEw_D8Lbkrd8EFbHabmes-kJIdXV44mCvZH7FBlpUapbwlYqthSRDvXavh36-jNRu3-4SvbJnIKlNFW05LDNnYOBFQBjIVV0lwdCi6cg4aXWDIRDLjE4I7mUGwg1CdfZwbZ_XPz2aoG5t3KIZQ-ajKAZW8bE14-VI-xdrHUip8FYgk-IfRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پرستار از اتفاق عجیب شب زفاف یه زوج میگه:
ساعت ۴ صبح یه خانم با خون‌ریزی شدید به اورژانس منتقل شد و اول فکر کردیم
سقط جنین
اتفاق افتاده، اما بعد مشخص شد مربوط به
شب زفاف
بوده.
خون‌ریزی اون‌قدر شدید بوده که مجبور شدن بیمار رو
جراحی
کنن.
⏺
پرستار توصیه کرده زوج‌ها برای اولین رابطه عجله نکنن و با آرامش و احتیاط پیش برن تا به این روز نیافتن
.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69835" target="_blank">📅 11:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69834">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53aa49426e.mp4?token=OcguwEt13kKmmO8C_jcXEHSAzW0BpGfSSS9PB-E6wx4s0ZkKa2Qoh8i5F9Hn1A0zW5SdEKbsUptXjEW0BdARFfok4dKVQfs1nR6tz-1cm3nUc4Xw6tbTrvz-XsF50A3nU_bZMwXcZ-61JDxU1xNJmU8Q26u5nSaeLSvMnKOk_gihzLC_UGV57o5VFz8Z1SeYtyLsFyHZxGcvbpw2ReaGOqqLMlSkKywq_UZNBvmzT_RtSjkQ1pG3AcNa82rDEWTkjf0B09WH7SksTVbLA9guWfK7bFvLIw-0CHIEheDMlnrlG1CZX6z4dL2OM0AsFllTVC7dtNqvVUCGE_YE0sILQl3RGfXDFkxgF3kCFJL3ACNxEV5_k6VVah8Us0VfWG5wFfB7ZrA--usNpVLvFoHd7f3XSlV0wpoWNuEuXLwev1LFj_6dO-dBoHySK8uLzTPqQcNszd9WWA0wEMQ2Kgrfl47pHb1J4PIAxqiFEWJlEqJqdumpb7pEWlfSyRwfPWiwREAUuf8gwoRNei4c8IcVu3z2tt9yCXJzGFIN1L4OH5iWbJ7D4uoYeVl-JUVuDjxPgJP11QDomklv2P8pBG9n93OhtfB9AwSTpFd0ZZoHvEqvm6TBpoPvZMvzz5B9Oi-VfkmA5GYyW7qUMB6aHdIu8IVlc2-N6-5jNIG5sDH37Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53aa49426e.mp4?token=OcguwEt13kKmmO8C_jcXEHSAzW0BpGfSSS9PB-E6wx4s0ZkKa2Qoh8i5F9Hn1A0zW5SdEKbsUptXjEW0BdARFfok4dKVQfs1nR6tz-1cm3nUc4Xw6tbTrvz-XsF50A3nU_bZMwXcZ-61JDxU1xNJmU8Q26u5nSaeLSvMnKOk_gihzLC_UGV57o5VFz8Z1SeYtyLsFyHZxGcvbpw2ReaGOqqLMlSkKywq_UZNBvmzT_RtSjkQ1pG3AcNa82rDEWTkjf0B09WH7SksTVbLA9guWfK7bFvLIw-0CHIEheDMlnrlG1CZX6z4dL2OM0AsFllTVC7dtNqvVUCGE_YE0sILQl3RGfXDFkxgF3kCFJL3ACNxEV5_k6VVah8Us0VfWG5wFfB7ZrA--usNpVLvFoHd7f3XSlV0wpoWNuEuXLwev1LFj_6dO-dBoHySK8uLzTPqQcNszd9WWA0wEMQ2Kgrfl47pHb1J4PIAxqiFEWJlEqJqdumpb7pEWlfSyRwfPWiwREAUuf8gwoRNei4c8IcVu3z2tt9yCXJzGFIN1L4OH5iWbJ7D4uoYeVl-JUVuDjxPgJP11QDomklv2P8pBG9n93OhtfB9AwSTpFd0ZZoHvEqvm6TBpoPvZMvzz5B9Oi-VfkmA5GYyW7qUMB6aHdIu8IVlc2-N6-5jNIG5sDH37Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایشون هم اینطوری انتقام قتل حمیدرضا رجب‌زاده رو گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69834" target="_blank">📅 11:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69833">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48e95fc990.mp4?token=rcOdFFIdLKyIhoQ8HYCLpzjuBLuSApOhuruQZZgXeCAE50SKwu3F8Z-3Qnl8xaNWFquLz6JDi0TEZZNDIr_zWf1u0NLsqFRbI2mbJe9kMhMWSYH3g8SYrtKkfPCyxc5npqTAteX9DAqJRpfsiwWEsa3Z9Jl5SXh_OguVm-TbhvwRwU2HJVO8zLB3MPcBdiNO1A9yPGOODzxKgHygBG4CJlgNKApTyUDPhCgpTNGyEedIlRdNh-aF1-QlxNwpNpDJconh86L8cSjcBpmuB-7Kek-uxPcHe2KdAgN4u3TuvSGxhFZUgTyAgM1cvnEPKZBVj9ZfmzDkD9BVrB_5KejnFw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48e95fc990.mp4?token=rcOdFFIdLKyIhoQ8HYCLpzjuBLuSApOhuruQZZgXeCAE50SKwu3F8Z-3Qnl8xaNWFquLz6JDi0TEZZNDIr_zWf1u0NLsqFRbI2mbJe9kMhMWSYH3g8SYrtKkfPCyxc5npqTAteX9DAqJRpfsiwWEsa3Z9Jl5SXh_OguVm-TbhvwRwU2HJVO8zLB3MPcBdiNO1A9yPGOODzxKgHygBG4CJlgNKApTyUDPhCgpTNGyEedIlRdNh-aF1-QlxNwpNpDJconh86L8cSjcBpmuB-7Kek-uxPcHe2KdAgN4u3TuvSGxhFZUgTyAgM1cvnEPKZBVj9ZfmzDkD9BVrB_5KejnFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دریک، از بزرگترین خواننده‌های دنیا؛
با 140 میلیون فالور و ثروت 250 میلیون دلاری [50 هزار میلیاردی]
وقتی ممه‌های بزرگ یه دخترو دید، نتونست تحمل کنه و براش هاپ هاپ کرد
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69833" target="_blank">📅 11:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69831">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d3c25ee1.mp4?token=aM47c6PBoy5Sev_X7raygLN9DEUxeubsAvBUoxMMPCH-4XM00xMmPcQaQBzR6cUI_Kh7uVUG_JjYyQnzPwAOijQae_6OKyKZvy_3R3hy2PXY3D2OFRhj4JVUxxwVrPNR5aWDnxuo87FH-dbcDiZLlgfsZq_9Em0492PA2v2esi82Wou5PKaojdJKIczwNNDNR-wS3WijEQUZlZuI3biDNAFH8Dc4QxFHzGm9Fnv02REERwcGHOyhGDgj3kLF02zW7m3EZDBMwaY1Z2ozIqNdMxc1xUnulC4pSMY_GTTJGOENEzVk3biiX7q9kEGNYKl3SNDo4qCqJAmIlIAmLgMWBzBtY_uldSDcqkeq-zk7OB13L7lIznT8x75deGOWvlk-VxLUIQjksqiAHVUzbRd6ex-sA3I7wB0MKmHijtV8bX2taObhf-DGMBYI7We_CndP3OnoIrVnFAwY5BKP7mQC8SunXEF5KbLMUt_wLrBi9-bZLsCoQF0sFJ1WPPAwCo861q-JR_O8IBrzmiJ5vyXp3Bq18kIwqcAnYmsAZYupN13d2Qciw1aKFlYuc43pF6tOj5UotldBepcEV1d6uBMb-jZtRuKmhfZzpCi-QIFfMZfbk0OzXx3au2h87hMzOuHDnjiW9DEYWFpPoBiY5mfRCkTkdNJzwTArNH2ZyWIszIE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d3c25ee1.mp4?token=aM47c6PBoy5Sev_X7raygLN9DEUxeubsAvBUoxMMPCH-4XM00xMmPcQaQBzR6cUI_Kh7uVUG_JjYyQnzPwAOijQae_6OKyKZvy_3R3hy2PXY3D2OFRhj4JVUxxwVrPNR5aWDnxuo87FH-dbcDiZLlgfsZq_9Em0492PA2v2esi82Wou5PKaojdJKIczwNNDNR-wS3WijEQUZlZuI3biDNAFH8Dc4QxFHzGm9Fnv02REERwcGHOyhGDgj3kLF02zW7m3EZDBMwaY1Z2ozIqNdMxc1xUnulC4pSMY_GTTJGOENEzVk3biiX7q9kEGNYKl3SNDo4qCqJAmIlIAmLgMWBzBtY_uldSDcqkeq-zk7OB13L7lIznT8x75deGOWvlk-VxLUIQjksqiAHVUzbRd6ex-sA3I7wB0MKmHijtV8bX2taObhf-DGMBYI7We_CndP3OnoIrVnFAwY5BKP7mQC8SunXEF5KbLMUt_wLrBi9-bZLsCoQF0sFJ1WPPAwCo861q-JR_O8IBrzmiJ5vyXp3Bq18kIwqcAnYmsAZYupN13d2Qciw1aKFlYuc43pF6tOj5UotldBepcEV1d6uBMb-jZtRuKmhfZzpCi-QIFfMZfbk0OzXx3au2h87hMzOuHDnjiW9DEYWFpPoBiY5mfRCkTkdNJzwTArNH2ZyWIszIE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی شبانه به مجموعه‌ای از اهداف در سراسر روسیه و سرزمین‌های اشغالی حمله کردند.
پهپادها مرکز خرید گالاکتیکا در ماکی‌یوکا، که قبلاً مرکز منطقه‌ای بود و در سال ۲۰۱۴ توسط نیروهای روسی تصرف شده بود، را به آتش کشیدند.
آنها همچنین پالایشگاه نفت در نیژنکامسک، تاتارستان را هدف قرار دادند، در حالی که روسیه ادعا کرد ۱۵ پهپاد در نزدیکی مسکو سرنگون شده و عملیات فرودگاه را مختل کرده است.
طبق گزارش‌ها، حملات پهپادی باعث قطع گسترده برق در ملیتوپول، بردیانسک و دونتسک شده است، در حالی که انفجارها و آتش‌سوزی‌هایی در سواستوپول و کرچ گزارش شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69831" target="_blank">📅 10:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69830">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69830" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/69830" target="_blank">📅 10:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69829">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=J85hOGq5bpjFBYyZWd0-UVey7f5Ak3GSly-0OUzBnI9Q4N8YWi823c2WyfLWpc96t11H7hn5kyNXZb1FJv_5QbjSLpEW6bga2gHidrh6wIi2ZWatKrWEJSykVVHkM9_L810ks5j-NXU63S5x7U7vEH3BeiwFCC8aDg58kOvM3MnYun1RZNnxTdI-WMllN77XHHu3WMDp9XbFCT8X9iVr8bR4M8c4PTxpIJq1feJJtqpVtDibDJvucRuJxQUr4xaqbT2AbeOPmhP5bs1uPQHYEdqai_bVydtmTaSggkzhU3YwMU8o3nLjWrnuRuc8AheyPFyBy4wHJRFvG8WuFxoHIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=J85hOGq5bpjFBYyZWd0-UVey7f5Ak3GSly-0OUzBnI9Q4N8YWi823c2WyfLWpc96t11H7hn5kyNXZb1FJv_5QbjSLpEW6bga2gHidrh6wIi2ZWatKrWEJSykVVHkM9_L810ks5j-NXU63S5x7U7vEH3BeiwFCC8aDg58kOvM3MnYun1RZNnxTdI-WMllN77XHHu3WMDp9XbFCT8X9iVr8bR4M8c4PTxpIJq1feJJtqpVtDibDJvucRuJxQUr4xaqbT2AbeOPmhP5bs1uPQHYEdqai_bVydtmTaSggkzhU3YwMU8o3nLjWrnuRuc8AheyPFyBy4wHJRFvG8WuFxoHIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
به راحتی کسب درامد کن
💵
💰
🟢
ویدیو
#آموزش
بازی chicky choice رو براتون گذاشتم خیلی راحت و بدون ریسک و میتونی بازی کنی و کلی پول دربیاری
🔥
💖
حتما ویدیو رو تا انتها ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
r19
@betinjabet</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69829" target="_blank">📅 10:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69827">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Liogt2K5R90FTRF7C0_rlfx_PyrNAJbTw1l7lb0UzbZK-JfehrmGLP-uRFcdr2rhCu1woNw9bZshyVgBkb8e3nljrVFDDEJQa-3kk2x-YVSKsd3dTDVSeLS3Jw1v8BHK3tp0kFp51myzZOubAXxDhO78ZPE1b5WKJ71wPl3xjuNPi6oRc237OTC-IbGlSlpm3PGPOrCr9MiCin55R9m8RAn-THbXayVQ5Gu1Vupt1G5ndsJATQs6stLPYYj5I-0b2BMy5hZoBCPXdRm4OkcYzRlXYW0A7O6Log8Hh6WJfQps9LxY4n3Kb6Crc37vf3scLPROib_PiPFjWiG78TWhGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
شرکت آمریکایی BlackSea از پرتاب یک پهپاد FPV از روی قایق بدون‌سرنشین GARC خود رونمایی کرد
؛
این شرکت اعلام کرده است که با استفاده از تجربیات به‌دست‌آمده از جنگ، استفاده از پهپادهای FPV هدایت‌شونده با فیبر نوری را پیشنهاد می‌کند.
محفظه‌های پرتاب این سامانه قادر به حمل پهپادهای FPV در اندازه‌های ۵، ۷ و ۱۰ اینچی هستند؛ پهپادهایی که از نمونه‌های FPV مورد استفاده فعلی روسیه و اوکراین کوچک‌ترند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69827" target="_blank">📅 10:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69826">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4c36a2172.mp4?token=BLabfG2BTMKyDh_Sq_aUd2A13hnkMYvT2zeJVjpyC7gN6H9W15Rml2OWtucrByxOSVF7dYqTWgZI6VTuXkvhbuvnCvmoPi5ti3kKmdPakTaTUY0j5Q7Bgfp3Yt-vsb-zro4zUeg7xCOgHUMe5k5ZZcdH5-JtQ5mSA8RZLAoY_9RqqzFvFm4TH-kwsNNv4LMjVNLx6_-s-KkJCYMYEYvl0D8W-WxEXP1OxKFFlz2DnCtGuwK2L3yDRNTHm0pIhMfCp1DQF3NcPcapQGKeq2JBWNo091KEa0e5rDr0WGcVrqyuqjp3QKeDx79sP0Q2hzConNNf6gARFSaw12qdw05uzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4c36a2172.mp4?token=BLabfG2BTMKyDh_Sq_aUd2A13hnkMYvT2zeJVjpyC7gN6H9W15Rml2OWtucrByxOSVF7dYqTWgZI6VTuXkvhbuvnCvmoPi5ti3kKmdPakTaTUY0j5Q7Bgfp3Yt-vsb-zro4zUeg7xCOgHUMe5k5ZZcdH5-JtQ5mSA8RZLAoY_9RqqzFvFm4TH-kwsNNv4LMjVNLx6_-s-KkJCYMYEYvl0D8W-WxEXP1OxKFFlz2DnCtGuwK2L3yDRNTHm0pIhMfCp1DQF3NcPcapQGKeq2JBWNo091KEa0e5rDr0WGcVrqyuqjp3QKeDx79sP0Q2hzConNNf6gARFSaw12qdw05uzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
جهانگیر، سخنگوی قوه قضائیه:
آخوند خرازی، بابت صحبتاش تحت تعقیب قرار گرفته و به دادگاه ویژه روحانیت احضار شده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69826" target="_blank">📅 10:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69825">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🟡
📰
مراد ویسی تحلیلگر ارشد اینترنشنال: «جنگ بزرگ در خاورمیانه، برای سرنگونی جمهوری اسلامی است.»
⏺
پرسش این نیست که کدام زودتر می‌رسد؛ پاسخ روشن است:
جمهوری اسلامی سرنگون شود، مردم ایران به یک حکومت عادی می‌رسند.
جمهوری اسلامی سرنگون شود، نیابتی‌ها خشک می‌شوند.
صدام رفت، یک کانون تهدید در خلیج فارس از بین رفت — کانون دوم هنوز باقی است.
خلیج فارس می‌شود منطقه‌ی صلح، ثبات و توسعه؛ چون امارات، قطر و عربستان دنبال توسعه‌اند و ما هم دنبال جبران خرابی‌های جمهوری اسلامی.
ثبات منطقه از تهران آغاز می‌شود، نه از میز مذاکره.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69825" target="_blank">📅 09:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69824">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdd241cc6.mp4?token=YBJq5lqregy6cXMucmGiCIzciQlNeKlBYjz_BWbu7Dm0-2tiJsnZlGYR6qcL6ZnMzt-FgvH05WxjmxGFRsffb0Cxc-nOtlvzUFDgBJpkLhRzRRFp0BncrwiP44b5QDu-ffyCNUHA6Mf05cAOcTo3FaJv9dvMLhI0I8i8t2OKwJXRK431ZK5Vhefk6EpJXA308kIntjSZrNinByzuziwWkkHUCzXFWVWP0zVhoY-xf_7ADSHWH_CpLEBZRWbPXDEQiGZ6xNaKQoWcn3EKULzGkxy1nOfbfdKUzYkinkr2Bl0yYPcwOBAsJ66iVmOF-joKjCmoYisDsxRw6v8fgrAixQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd241cc6.mp4?token=YBJq5lqregy6cXMucmGiCIzciQlNeKlBYjz_BWbu7Dm0-2tiJsnZlGYR6qcL6ZnMzt-FgvH05WxjmxGFRsffb0Cxc-nOtlvzUFDgBJpkLhRzRRFp0BncrwiP44b5QDu-ffyCNUHA6Mf05cAOcTo3FaJv9dvMLhI0I8i8t2OKwJXRK431ZK5Vhefk6EpJXA308kIntjSZrNinByzuziwWkkHUCzXFWVWP0zVhoY-xf_7ADSHWH_CpLEBZRWbPXDEQiGZ6xNaKQoWcn3EKULzGkxy1nOfbfdKUzYkinkr2Bl0yYPcwOBAsJ66iVmOF-joKjCmoYisDsxRw6v8fgrAixQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یکی از نفس‌گیرترین ویدیو های منتشر شده از جنگ؛لحظه بمباران شریعتی تهران!
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69824" target="_blank">📅 09:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69823">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69823" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#بازی_پولساز
⚠️
🔥
بلک کارت جدید ترین بازی معروف جهانی هست که فقط کافیه یکمی باهوش باشی تا حریفات رو شکست بدی
👌🏼</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69823" target="_blank">📅 02:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69822">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6c003ee1.mp4?token=cMDl0woi4wpiKiQshFe0_1Ja74oD9ZmiHQUwsLr8itDVIUuTmZ2wfxDjZieEXq679w5O6FQQ5FpyZ7KmoXLAOZygy3d4LkuXuEdL2Bj8tVajJ0XN-ghaeU10zRMCnX1-KNZh0RlI8kzg5IGrtgJ2l2ep-4LcH5aL1SauzaunqAKOUVBL0rcTtkprX368TXwp8FHdw2ECwS_G2JdyoScCC6-1BL96Q1pcqO2Ob5ihnyYiUbHKcGAkJABH5oDbi-bOdz9qoAUf5Cs9yCb4k1_0LX9dgzCgoHUTXGRMEeML063bNHezxSugjGBckdPadUYHozZR9l-61-e6VEa96lpI1oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6c003ee1.mp4?token=cMDl0woi4wpiKiQshFe0_1Ja74oD9ZmiHQUwsLr8itDVIUuTmZ2wfxDjZieEXq679w5O6FQQ5FpyZ7KmoXLAOZygy3d4LkuXuEdL2Bj8tVajJ0XN-ghaeU10zRMCnX1-KNZh0RlI8kzg5IGrtgJ2l2ep-4LcH5aL1SauzaunqAKOUVBL0rcTtkprX368TXwp8FHdw2ECwS_G2JdyoScCC6-1BL96Q1pcqO2Ob5ihnyYiUbHKcGAkJABH5oDbi-bOdz9qoAUf5Cs9yCb4k1_0LX9dgzCgoHUTXGRMEeML063bNHezxSugjGBckdPadUYHozZR9l-61-e6VEa96lpI1oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😯
اگر هوشت بالاست
🗼
:
❌
👍
این ‌ویدیو‌ آموزشی رو‌ ببین و با ‌استفاده از هوش بالایی که داری پول در بیار.
🟢
بازی خیلی حرفه ای و‌
#پولساز
رو‌ از این ویدیو یاد بگیر
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
a18
@betinjabet</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69822" target="_blank">📅 02:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69821">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:  اگه ایران از این به بعد به هر کشتی‌ ای توی تنگه هرمز شلیک کنه، فرقی هم نداره با موشک، پهپاد، راکت یا هر سلاح دیگه‌ای باشه، آمریکا در جوابش یه پل یا نیروگاه برق ایران رو میزنه حتی اگه نزدیک تهران یا داخل خود تهران باشه.  @News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69821" target="_blank">📅 01:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69819">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSUbxf6IRIzR1sqpcLmqIc7Nhn5S2rXc4_ZacybvubhncfFkSSUoP5kQJDtW7q84s-Ql7UtSWVKv3sr_rsaZ148uwCWEQ35hUktVlksso-DPh-RKWiMwbKfKpWdVIwDSvLV8pDqRYdyf394qZfLhc5D0LLbrLxgzZdgLG0Udcf4DC3IIlQyJNGatUo4yJeb51bq5mPYNVM8T8MIc_mfEfNbpXywBDcHXelWpnSN8U0bomogbYsDSX7IfIWEpn7cLjM7loFzII_2EDW6uVH1k7SZ-H-pkgP7SmGiFjqsTQco0EOoOiwELhBHY7HrcmntTv4CSyTHwOpsuQXGp4Gz6ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94eb35c039.mp4?token=qm_h6ln92548UIuoHUH8mGp79-6lRbBOnIzjl3mK3WoHnGt0XuyLKRsJSa9F0L9gxwfTj1P5m4kKIXnFd58jttZXFYMDvIf7CNiz_-t3srKSWDkeIx5KQ4UI9RWdlllrbOI_cgshXy7xoOWu1YkkByRencsLu_OgkO1fCwmalzdGoF4gQACusiPHpgTtPlnCkHicMZolnDrpPqnVJbq7O-6BhXn_XBIiOJK4b_broh3dBO0zg14IFjsYf1W8uZQvFuREGr3ZoHhmpP4tkQvd7fVM0Yr9lNC_hdCAsvt28OJO2DyMoR0hNQfWKTDy4YtY4C7NaWo7xq0KpgKSUyxj2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94eb35c039.mp4?token=qm_h6ln92548UIuoHUH8mGp79-6lRbBOnIzjl3mK3WoHnGt0XuyLKRsJSa9F0L9gxwfTj1P5m4kKIXnFd58jttZXFYMDvIf7CNiz_-t3srKSWDkeIx5KQ4UI9RWdlllrbOI_cgshXy7xoOWu1YkkByRencsLu_OgkO1fCwmalzdGoF4gQACusiPHpgTtPlnCkHicMZolnDrpPqnVJbq7O-6BhXn_XBIiOJK4b_broh3dBO0zg14IFjsYf1W8uZQvFuREGr3ZoHhmpP4tkQvd7fVM0Yr9lNC_hdCAsvt28OJO2DyMoR0hNQfWKTDy4YtY4C7NaWo7xq0KpgKSUyxj2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇨🇳
🇸🇦
یک پهباد ساخت چین متعلق به نیروی هوایی عربستان سعودی در آسمان جنوب کشور سرنگون شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69819" target="_blank">📅 01:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69818">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyaT_f4QYqHRdvdaZXDZDT_ZBbeDtUCE-dpLAi3NJFL5e4G9kHrEx91UaSRWi7gFgDKJgpHEFAclEAgfSi4UKZvmXFpAbn6zYVn4NtBISvErit8WOlVW6yg2z0e-VUnHZfBm5O7zUZ9sIR9QrxNUlJKs6xJRE8uSR5Lk_0nY0wv0JMcCIcUyibF7mfz8uW4aghe5VG4Bcd-LDP10G7UX3-xyXWfy-JRjNBXDTYhACgp9li35ybriLnOVa7w1fGUqmy9miCpRpjCpyyBKhZie-LvjocA--Fu9-TcubF0SUEO4BWI4WRJyqNH0dMPM_4-oQtgmy0-MKtT3QZE43t2eJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در تروث سوشال:
51سال رفتار نامناسب!
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69818" target="_blank">📅 00:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69817">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dbf391292.mp4?token=tMXt9X_TsVbNfOly2AkiazwiPyD2fDuYSKARaeYpiY2CjxCtrySQebgEmRLMEvKU0L5sbTwtJPrRoaJ8uCM43Idpw587YijG5nw1nPxs6AF_0Tgak0hc1pjavTkEsyJmv_pzrvu1QpUP_EDUdtkyQa4hkCMCg79fvvCXuDSybnv23z0ySDmePyEmnPL8EOpjbEaj4B2mNMA_p2KLpZ_7DnbB1LBbvbLMMuuD1yBNIpyMRhmMfOpec3G2tNXUzluZ4kGj8lBOxDz4x20i_jlb0cOhUjjEynHTdu7iF8LdUHIKdrGMY4KPeDLQuCKsAa2Zr9TT1EC0vNlzbRvvTi-8nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dbf391292.mp4?token=tMXt9X_TsVbNfOly2AkiazwiPyD2fDuYSKARaeYpiY2CjxCtrySQebgEmRLMEvKU0L5sbTwtJPrRoaJ8uCM43Idpw587YijG5nw1nPxs6AF_0Tgak0hc1pjavTkEsyJmv_pzrvu1QpUP_EDUdtkyQa4hkCMCg79fvvCXuDSybnv23z0ySDmePyEmnPL8EOpjbEaj4B2mNMA_p2KLpZ_7DnbB1LBbvbLMMuuD1yBNIpyMRhmMfOpec3G2tNXUzluZ4kGj8lBOxDz4x20i_jlb0cOhUjjEynHTdu7iF8LdUHIKdrGMY4KPeDLQuCKsAa2Zr9TT1EC0vNlzbRvvTi-8nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
آتش‌سوزی یک کشتی در پی حمله سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69817" target="_blank">📅 00:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69816">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🇮🇷
سپاه‌پاسدارن یک کشتی را در تنگه هرمز هدف حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69816" target="_blank">📅 00:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69815">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec1565ac0.mp4?token=wCO5zxaVXZqwZvweQwu5NHACrjCIdvgdEh4Na8aBYX05eKyZ3agUuRLXLnRXZRMmUomjzRDtLmLRLs6bTIzs7wAX5LqfjjN_1bjw-LQ5mI3hdkusRs7Ok6jM-5h5LzV7dqwIwbUBwlQSLj2ODdQaKFKLrdXISAGrifgwMNzIuuKDuL3-r7maAP6CuIV17RWhYraW83Fb5R7JV1_9cCv-SB9Aka2Sm-21woTn5gQEEPp9tvC4syRzWpusGFj2UcGwYSBLF-aFoaiDz6dBfZe-tdNEOoI-Rsg0z33DIErMFtXm1hdNfQdqpxZGdBsCl2Q3ks8imO0r3_K--PceTEyfKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec1565ac0.mp4?token=wCO5zxaVXZqwZvweQwu5NHACrjCIdvgdEh4Na8aBYX05eKyZ3agUuRLXLnRXZRMmUomjzRDtLmLRLs6bTIzs7wAX5LqfjjN_1bjw-LQ5mI3hdkusRs7Ok6jM-5h5LzV7dqwIwbUBwlQSLj2ODdQaKFKLrdXISAGrifgwMNzIuuKDuL3-r7maAP6CuIV17RWhYraW83Fb5R7JV1_9cCv-SB9Aka2Sm-21woTn5gQEEPp9tvC4syRzWpusGFj2UcGwYSBLF-aFoaiDz6dBfZe-tdNEOoI-Rsg0z33DIErMFtXm1hdNfQdqpxZGdBsCl2Q3ks8imO0r3_K--PceTEyfKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو وایرال شده از یه پسرِ جوون تو تجمعات شبانه:
به ابالفضل راضی‌ام جنگ زمینی‌ بشه، یه تنه 500 نفرشون رو حریفم!
ایشالا روزی بشه مکه و فلسطین رو آزاد کنیم.
ایشالا روزی برسه آمریکا رو نابود کنیم و تو کاخ سفید نماز بخونیم.
نیاز به بسیجی‌ها نیست همین بچه‌لات‌ها اسرائیل رو میگیرین داداش...
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69815" target="_blank">📅 23:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69814">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b396273688.mp4?token=gOaM8-hDwWkEHOK89UstLfuE_IYBXcRxmRUTgx-DWix_5B30BdeyrPdwsZMj6ZGx1oWfHu7UTZ_nDkeZ-jCkAOg27kcR0j3wrnibD9xsl1H-PtcKSC0E-sqki86d4H_3m87eFPA5Vi5jvJ6LuNtuazsIhAKlmlitHBfzXRBvxQW7AVz2GH3XZh3D_KAiD7cjg9Lk4BBA-DLQGM9pYjxL9qWX5rOCiGIO-09mNRVaGd42s0BvKdmaVzWBOVxY1BzmGl6k5nIXfRgtJVgkIOIk4aGZuqAr_2_k5qqUXJ2smf6U-z-Iz5ZAtkXqzISeibZuTZ82UVCMkjqzCUtCOoIJV5daK-ZfPgZNdFsJGW4t8xxoHy19b_VQKVbh69kMU5r3C9jEQNe97F9GgBSOMmKeoAZY083qMvX3umsrWIb7V4HIrllrMtVzlfpd0XPqvFn2mbPJIUphsQsGxuvcPvH3tiMrnjaicDhPcOUYxwOz_giftl0qL-q5cXeP2DCkcgM6qQuSUkCmXhsdp-CyF3drW6gp5hFT5vWclxSkcTg4FdVrx90GMHvcfPuwoXRwJmtZ_bGubd78fs3dRYWQ4KsxQCm1zyZCls5xiN90R4rVSMcmy8iejpMEbxArMxX8KWdlWZrjs9Vx0UI2DgXApP_9hc60LHx8xSSF_1lcsifsRRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b396273688.mp4?token=gOaM8-hDwWkEHOK89UstLfuE_IYBXcRxmRUTgx-DWix_5B30BdeyrPdwsZMj6ZGx1oWfHu7UTZ_nDkeZ-jCkAOg27kcR0j3wrnibD9xsl1H-PtcKSC0E-sqki86d4H_3m87eFPA5Vi5jvJ6LuNtuazsIhAKlmlitHBfzXRBvxQW7AVz2GH3XZh3D_KAiD7cjg9Lk4BBA-DLQGM9pYjxL9qWX5rOCiGIO-09mNRVaGd42s0BvKdmaVzWBOVxY1BzmGl6k5nIXfRgtJVgkIOIk4aGZuqAr_2_k5qqUXJ2smf6U-z-Iz5ZAtkXqzISeibZuTZ82UVCMkjqzCUtCOoIJV5daK-ZfPgZNdFsJGW4t8xxoHy19b_VQKVbh69kMU5r3C9jEQNe97F9GgBSOMmKeoAZY083qMvX3umsrWIb7V4HIrllrMtVzlfpd0XPqvFn2mbPJIUphsQsGxuvcPvH3tiMrnjaicDhPcOUYxwOz_giftl0qL-q5cXeP2DCkcgM6qQuSUkCmXhsdp-CyF3drW6gp5hFT5vWclxSkcTg4FdVrx90GMHvcfPuwoXRwJmtZ_bGubd78fs3dRYWQ4KsxQCm1zyZCls5xiN90R4rVSMcmy8iejpMEbxArMxX8KWdlWZrjs9Vx0UI2DgXApP_9hc60LHx8xSSF_1lcsifsRRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خرازی:
این کلیپ ها جعلی و هوش مصنوعی است؛
من این حرف‌ها را نزدم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69814" target="_blank">📅 23:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69812">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1fdc25902c.mp4?token=iMTckGkntDIL4NIS-Na2lCkq16MhazJPmkc3Sc8eQqCcar51QSTddZsLOW5ZzXyriosn2MGe2Fv7mucBAEmnKwbV4-YmAidQa-fVjVqtZu5v9BPrfa_c2LhkgP9Ik-OPVHwaKZdcLcE1-R_vA4aj18lpcSUF5Sq-P9adppkDOOSU62O2dj7ZxgaoyBw9LfQKjTjGb9r6zcwgp557VvCCjYCWuR3M2Y1-MEMOuBO9NBw7hlHjIpX-M3TIIsHRFApIFWil4FuraAqEDji-8uO7LGheRrsb0WpIbJ73vqNuShdnnqCLEhGejfbaPDPfXv3pe9s0Q-pPy7H7X-6j_I6HzA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1fdc25902c.mp4?token=iMTckGkntDIL4NIS-Na2lCkq16MhazJPmkc3Sc8eQqCcar51QSTddZsLOW5ZzXyriosn2MGe2Fv7mucBAEmnKwbV4-YmAidQa-fVjVqtZu5v9BPrfa_c2LhkgP9Ik-OPVHwaKZdcLcE1-R_vA4aj18lpcSUF5Sq-P9adppkDOOSU62O2dj7ZxgaoyBw9LfQKjTjGb9r6zcwgp557VvCCjYCWuR3M2Y1-MEMOuBO9NBw7hlHjIpX-M3TIIsHRFApIFWil4FuraAqEDji-8uO7LGheRrsb0WpIbJ73vqNuShdnnqCLEhGejfbaPDPfXv3pe9s0Q-pPy7H7X-6j_I6HzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه ماجرای عجیب و تلخ که زندگی یه ورزشکار رو زیر و رو کرده
این بنده‌خدا یه ورزشکار ۱۳۰ کیلویی بوده، پرس سینه می‌زده و از بهترین راننده‌های جرثقیل هم بوده؛ ولی یه ماجرای مهریه کل زندگیشو زیر و رو کرده...
همسرش مهریه رو می‌ذاره اجرا و حکم جلبش صادر میشه. وقتی مأمور برای دستگیریش میاد، فرار می‌کنه و مأمور هم به کمرش شلیک می‌کنه؛ گلوله باعث میشه قطع نخاع بشه.
حالا با وثیقه آزاده، ولی هنوز داستان تموم نشده؛ همسرش گفته فقط یه هفته وقت داری، وگرنه دوباره باید بری زندان!
از یه آدم سالم و ورزشکار، رسیده به این وضعیت...
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69812" target="_blank">📅 22:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69811">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🇺🇸
وقوع یک حادثه امنیتی در نزدیکی باشگاه گلف ترامپ در شهر بیدمینستر، ایالت نیوجرسی؛
فرماندهی دفاع هوافضای آمریکای شمالی (NORAD) دو فروند پهپاد را که حریم هوایی محدودشده بر فراز بد‌مینستر، نیوجرسی (Bedminster, NJ) در نزدیکی باشگاه گلف ترامپ را نقض کرده بودند، رهگیری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69811" target="_blank">📅 22:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69810">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtQDvwhg98fmLGHL5HllBITCimAaREy-Ib2rtWHcqlESPNDC0dq1VSvTod8chbstEGX0tz5z3XppgO_uR7_5ZNFFVG_T-qJ218afQ_isBrlKLqHilE1XckNi-omlahWz_aTBA-y3WufaHMs__tHrGhaTEjhrfR7M38URjUAPkP5IGwvmJd8hL3ha_XyL4umA8rs2rPRD7vRGXFGppsXaiLtfNvnVeIJb4MFSGlPEC3STJOFEygH0X3Ubp6XDSGCE3hU14CeHMLeTsFWEXH50f5MdwvLGhFCh-mRP-Dz5scdpu_gK_Rso8QQGkqJzWv3fjJQmbYu2PqDmWxLpkP_xsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
با حکم مسعود پزشکیان محسن رضایی رسما دبیرکل شورای عالی امنیت ملی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69810" target="_blank">📅 21:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69809">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
یه فلسطینی به زور بچه شو میفرسته جلو سربازای اسرائیلی، بهشون میگه شلیک کنید بهش!
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69809" target="_blank">📅 21:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69808">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cb4mJHDGEukj3aEMhyRRAH99h8qpTeNU_chLvM5G7Ju0H7iYT2rn2P_EiB2pGfv2QhTeMvoMiJr_c_jPnyyV7WgK00PkRD0xdMGBXMIA1Gz_nxsUHjUQszo1DVrSiSezut_GMR2kdXGZPbRQ0nkuTx8HHGVR-2Qhg30Eh5t0rkhoLKjp1PDAjgAj1zvV28IT0TbXVpJSis7YBR-hyc1PsdJIG9sAgV6ynfSnv00WK_sqqd9sjyuX5JBEZEBqYh2nTV91d9agmXgEoWdCVoP17JhlUNMr71BzWWnp8j1YKMmMCtYPj6Vd5ujz51LZpopZ_wCtlC0X5Fw3SLlv7GOASg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
🇺🇸
اکسیوس به نقل از ترامپ:
ایالات متحده در رابطه با ایران «بی‌سروصدا» عمل می‌کند، که نشان می‌دهد واشنگتن فعلاً از اقدام نظامی عمده جدید خودداری می‌کند و در عین حال اجازه می‌دهد فشار اقتصادی افزایش یابد.
ترامپ با این استدلال که ایران از نظر اقتصادی «در وضعیت بسیار بدی» است و در حالی که محاصره دریایی ایالات متحده فشار را تشدید می‌کند، برای پرداخت حقوق سربازان خود با مشکل مواجه است، گفت: «این [مشکل] حل خواهد شد. همیشه حل می‌شود. مثل یک بازی شطرنج است.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69808" target="_blank">📅 20:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69807">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🙂
لحظه کمیاب واژگونی کوه یخ غول‌پیکر در سواحل گرینلند؛
ویدئوی ثبت‌شده در ۲۵ ژوئیه ۲۰۲۶لحظه واژگونی یک کوه یخ عظیم در سواحل گرینلند رو نشون می‌ده.
با تغییر مرکز ثقل بر اثر آب شدن یا جدا شدن تیکه‌های یخ، این توده‌های عظیم برای رسیدن به تعادل جدید می‌چرخن.
در این فرآیند، بخش‌های آبی‌رنگ و شفافی که میلیون‌ها سال زیر آب فشرده شده بودن، برای لحظاتی در معرض دید قرار می‌گیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69807" target="_blank">📅 20:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69806">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1384fab4ec.mp4?token=T84GzoVBN5ICjnpzQ3bVonhAwvHweIQJmH7c-wsmd-awqKYujV4M9c3_YepUsZM0sRabm2kGVNSdQvZKZykW09vAoiz13twOIic_ECryu05GmqAlR4t7M_q5rrORchHX3r1nyFn3EtaMyX67wOQq-SKbvbRtyJiUhNnfLMJT7t182rj2Wg_qiEpraJaz9wxlHNuqZ2ZerjmJVA8GD71VcbqPGV5OpeBhPgzLjlSG5XDGOVOzSqFvIjkh8M-FlhaMSGo-KQoABj_AUXsRU8SrRzWzVCRE13QZI4g-ckQ4VSKPK_7Jjxk2qCas5UFtwsYoxJhUDZ713u1b1po_FIvDQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1384fab4ec.mp4?token=T84GzoVBN5ICjnpzQ3bVonhAwvHweIQJmH7c-wsmd-awqKYujV4M9c3_YepUsZM0sRabm2kGVNSdQvZKZykW09vAoiz13twOIic_ECryu05GmqAlR4t7M_q5rrORchHX3r1nyFn3EtaMyX67wOQq-SKbvbRtyJiUhNnfLMJT7t182rj2Wg_qiEpraJaz9wxlHNuqZ2ZerjmJVA8GD71VcbqPGV5OpeBhPgzLjlSG5XDGOVOzSqFvIjkh8M-FlhaMSGo-KQoABj_AUXsRU8SrRzWzVCRE13QZI4g-ckQ4VSKPK_7Jjxk2qCas5UFtwsYoxJhUDZ713u1b1po_FIvDQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
طرفدار حکومت در واکنش به کشته شدن حمیدرضا رجب‌زاده:
شما زدین مبارک شما ما زدیم مبارک خودمون
خدا سرشاهده جرائت دارید بریزید خیابون
یجوری تیکه تیکه تون بکنیم یجوری ریش ریش بکنیم شما رو تاریخ تو خودش ندیده
به جان امام شهید قسم به جان رهبر مجتبی قسم شما رو با کارتک از وسط خیابون جمع خواهند کرد
جنازه شماها رو میدیم سگ ها بخورن
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69806" target="_blank">📅 19:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69803">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o7EUN5drfg3N-mN5erHb6RgJL2Tf7D_MQ9xwDE3s58CytDl3QZOi9lvuaTTV4jInDpafhi1eyNzDav34Y6pkeG8a2Qmd68GjAH2xIOocGKS8mhhmreL9347VCPxjHXPSV4YNVybiv50WC91crbJW3qFLCVWdivRWHqyw7r0VrFW5fjQ68R1mwijzu9zip9monDgWkTYeDUJ1tyQ8xqQVz4qbV1WuTEZB0jKJeqrCEUQiIZ_wiHakUQfgg-KVHLfEAW01W3_E7Mdm7xmnwOkeiBWZz9w10Z_tz0Ddx7NPgoRLGtNssw42LV2doO-lmH-Y3SkbLztJp07IwWSMwf6FPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jcNw9BNXUTfOT0Q_TBDnS-0q3rjiPdFRWS0wfzxMFFvJo5xwpJ7nd1YKnQbV8_dCPCchAbfLm0SfE_djXpFPX6EwSk6n77V9IVBzQX7Ii0K0mGHWazk4qZu-ZZnvZu8jnjb00CvBdjSpEZn21XckX0hxzxz7rHtbHm5UHBHvtoFKvZjxl-P053ND_Wcj-AV39yBzWEGswSSNIIB2tYscOoLhb2OuTOfc3cGzl8eZCEGTwOc4imfcB6XLZSn36Os3pXJDkNr-CZrtEw5ocYLvaKSKguKo2IEKLZ_ZChYtW2EIIinwrUVscAciTeQQOjwiahfaIA-UJrAsXJKlUdYEKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GJgIbXzkiiDxMTSOmIAtwaZFT7-L18WPLbykhePKi7MruT64sQ7W-nUL1mRqt6MfHUGp5oPFCou5MeyMtUdS3LZHNTTE8qTIp4GYhs-sHYG0Q-kZVYa6W43WmO3vyzLr1cFuD7fLaY0rT7g8bPaVYFI1VV8VKj63SOwkgFG80eMsJTcpaoM-R3gvAPsJUtnSQ2ODbGSflSV816EEXFn_imvMvRvi55E4007qi3Yp92do0rBJuz7vI9va-116FIHPgvk9qbjwV6kGY66adUxN9z_8sYQ-RRwhR62wSAQNTAcoYiDe5UzD8jqyOToZVohC00pHuAbuk6Wgh-FVTdXQnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ریورز یکی از مشهورترین فمنیست ها که زن رو برترین موجود میدونست و خودشم علنا لز اعلام کرده بود با یه پسر خوشگل و پولدار رفت قاطی مرغا
☺️
☺️
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69803" target="_blank">📅 19:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69802">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0cbb95dc3.mp4?token=MfFdLlfWGsqj-GClDz_GIv_sGq0QMYwuBdDnbNgEHLjIplCSNvSyyWBUp_mN36yLAkF8nrzCpKRswGFzJ418tu0a-6A9IWL0dktxVF6jtHUY9e2COGTLe__2Rf_c1N0_IsI651HFIsnZsKsQN7jR9Gaw1PIZu6FhXx1eTwHKsbsHNMuglJsZNtBRpZbJK-_nlZYe4CrfbFMud0LQeUc1T1AHpQZougqZha8DJcHHzJAiL5gLevQ2RnxdNehqdfQVaFR4tO37d5mpONDcgq-tiqPxnbj-s0MUTiZXekRiSR91hslMfxXefy__bt83aXcjj9JiZzRG63AM_KbNq1Xlhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0cbb95dc3.mp4?token=MfFdLlfWGsqj-GClDz_GIv_sGq0QMYwuBdDnbNgEHLjIplCSNvSyyWBUp_mN36yLAkF8nrzCpKRswGFzJ418tu0a-6A9IWL0dktxVF6jtHUY9e2COGTLe__2Rf_c1N0_IsI651HFIsnZsKsQN7jR9Gaw1PIZu6FhXx1eTwHKsbsHNMuglJsZNtBRpZbJK-_nlZYe4CrfbFMud0LQeUc1T1AHpQZougqZha8DJcHHzJAiL5gLevQ2RnxdNehqdfQVaFR4tO37d5mpONDcgq-tiqPxnbj-s0MUTiZXekRiSR91hslMfxXefy__bt83aXcjj9JiZzRG63AM_KbNq1Xlhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
یک فروند پهپاد بدون سرنشین جنگی (UCAV) نیروی هوایی ایالات متحده از نوع MQ-9A Reaper که از فرودگاه چابلی برخاسته بود، در نزدیکی گورستان چابلی در جیبوتی سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69802" target="_blank">📅 19:11 · 18 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
