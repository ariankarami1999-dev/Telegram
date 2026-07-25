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
<img src="https://cdn4.telesco.pe/file/o9dZy5nQlUhSL222gtmk9640dRbnHsLVsUe3zxCjFF4TFWKqQp_lbfEj83AuxWBH7F-bqSoDBg3e_aDofWl_3soe6FsX_GxsDmhNyJ_Q_jggjpBsbNHt4jzZzrWlRAmqAKErtRZNKBGHQHrFr95JhJa9tTKvKOY75kUzqsxsdqdJGgcnH3lmm57gESSR1gmZ0P_LPjh594PNKQoFHInAmXSBTV5fPLgDhlq0kzxPopyHEh39las_X5QQu3vylqKd0-iNwwbiHrA8csi6qnfUqkBDRb-mo7R-TDkGG37_NxRr1alp4pXBtszy-gx6HL5RjPvvPSzu8aJ1RKW4Zi8NaQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 939K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 01:53:38</div>
<hr>

<div class="tg-post" id="msg-137595">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89df9a7d6b.mp4?token=Cb3eyjfJn12hlhqGCnmhQOqsGRQ1c0n7OsBctGhmuQF3erOBfvFV-8RDQlDb_FsW2b5Zdbf2penKlG87GB_CM-V91yNii0mQ79Dl2YTvgPK6isV7HdSS1f3ywrAUWDN7dmKAg50lDGG1wbPT_D-iqUcjhD6QlMab2vHPAgC_om1VEVq_ESWtT4ndUzkQRDKdAH5eSIm-O_IXMfq1QV9To52WZWLS000uP8e3keCXp4hQW7ozWZvSizoscCdKBVAvwqg0AmSiw9iUpJ43_DwnkTSMS_OiM8AQPSppD2UTFeJyf2yLeoS-eFh1CIyipToh6ShQ_Y6YxGIPg4oi88pHBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89df9a7d6b.mp4?token=Cb3eyjfJn12hlhqGCnmhQOqsGRQ1c0n7OsBctGhmuQF3erOBfvFV-8RDQlDb_FsW2b5Zdbf2penKlG87GB_CM-V91yNii0mQ79Dl2YTvgPK6isV7HdSS1f3ywrAUWDN7dmKAg50lDGG1wbPT_D-iqUcjhD6QlMab2vHPAgC_om1VEVq_ESWtT4ndUzkQRDKdAH5eSIm-O_IXMfq1QV9To52WZWLS000uP8e3keCXp4hQW7ozWZvSizoscCdKBVAvwqg0AmSiw9iUpJ43_DwnkTSMS_OiM8AQPSppD2UTFeJyf2yLeoS-eFh1CIyipToh6ShQ_Y6YxGIPg4oi88pHBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش آمریکا فیلمی از شلیک یک موشک هوا به زمین هلفایر به موتورخانه نفتکش لاوین در خلیج عمان منتشر کرد و مدعی شد که این نفتکش تحریم‌های ایران را نقض کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/137595" target="_blank">📅 01:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137594">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozenIUcvFftmkPFPw7y6KvVsR5bB4W7N5RymTd-Tmg_vRHpX8O3gZukrSGBV3NCMahss_gKnqB1D5776cP9TKLS0lJg62oApd90CzfuwgvLsw4SWTsdaxdBrQairOuV3vuIT04IxMwFA7XZ_TAkSCVBT8Km2r5myEwB67ETF25rBndzvkm6Se3Wm1rOLpGyPYBfXq0C_feeJVOj-pEtGVUNtvJDVIuGIqR2aqflpHTIxbCDNroamCHVNHVOJN3_KiQLgjPFTFWYQzkT9OCbeDBXrUkJCrz6StLjSop1OO3rXxqAJj8pRcrHidSi8vq-Rdf3m_asy_kR50HN-LdbIHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آزاده آل ایوب(خاله نرگس): نباید به بازداشتی‌های اعتراضات عفو داد و باید همشون رو اعدام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/137594" target="_blank">📅 01:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137593">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
سنتکام:
محاصره دریایی آمریکا علیه ایران همچنان به‌طور کامل برقرار است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/137593" target="_blank">📅 01:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137592">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf0bd1b6b2.mp4?token=B1l8ynEF4QHnjMmi9HU3EjGeGwR18f5U4b5w9CHnK1BAoY4_MOSPmGU6Dbz8G6BIekpUrQEs7Ut_VAq4ULtXcHwzHhcoBVsXk3hIiexWpGAvgubxn7uUFZ81CnqbZhcx2N3ykyhpCF6TlEeggjub4GIwZ55SEm9EbAUI0hr-9xcBtMrr8mGg3M7saTXvJHIUm1FB9MnA6FozQVivoef5rq8JkYS_3GaFeJJmu0Qvl_lvDbWsVLYs9aW4drfo0Et26bO32lBE7-OjlaFNZ-4XP_8S2-v3mIfxM0tUTu_hdEpqF7KEnHR2QK1lZ_Sj2eBIBGvprNMBIV6CnMmy9YMktg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf0bd1b6b2.mp4?token=B1l8ynEF4QHnjMmi9HU3EjGeGwR18f5U4b5w9CHnK1BAoY4_MOSPmGU6Dbz8G6BIekpUrQEs7Ut_VAq4ULtXcHwzHhcoBVsXk3hIiexWpGAvgubxn7uUFZ81CnqbZhcx2N3ykyhpCF6TlEeggjub4GIwZ55SEm9EbAUI0hr-9xcBtMrr8mGg3M7saTXvJHIUm1FB9MnA6FozQVivoef5rq8JkYS_3GaFeJJmu0Qvl_lvDbWsVLYs9aW4drfo0Et26bO32lBE7-OjlaFNZ-4XP_8S2-v3mIfxM0tUTu_hdEpqF7KEnHR2QK1lZ_Sj2eBIBGvprNMBIV6CnMmy9YMktg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تحلیلگران در تجمعات شبانه در حال قانع کردن امت معکوس برای توافق هستن
🔴
یک تحلیلگر پایداری: با این محاصره اگه توافق نکنیم اوضاع بحرانی میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/137592" target="_blank">📅 00:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137591">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/137591" target="_blank">📅 00:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137590">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-y91r-HMTpW8gJcKe8PnsjofNhv3trMCp3TzqR5uFWsXQMrH3yab84ug-RXGoHOfPcRXWjMGpKWMneUIjwKCoNaNtdF5Ehk3tpXyOjVedmcm1t6O-yt368YI_Aphn5grxPuGxjEUB6hs_y6uChji6omOJ7ttlzW9zkR708CcWGjlBn1BxsvXbgpoxJFVME-MOR2TG2IdpaKoSrM1aP8uuWSZXhL1mlP8DioPCfY1XKSBsVbibEBIQdIW7uyfUPzi6ZU9rBrEX6147OZsA_QetPUgUWO2HbYotfXhihxyVQ_E42bPUBeQEX0bbD_18nirniuifDMAPSpZxdVPmFp-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلاکاردی در تجمع امت معکوس که تایید کردند تنگه ننشونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/137590" target="_blank">📅 00:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137589">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">⚠️
تماشا برای زیر 18سال ممنوع
‼️
❌
ویدیویی منتشر شده از سواستفاده جنسی از کودکان در جزیره اپستین!
🚨
مشاهده برای افراد زیر ۱۸سال و افراد دارای مشکلات قلبی ممنوع است
◀️
مشاهده فوری فیلم</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/137589" target="_blank">📅 00:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137588">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2m_vo8KGJkOPyHwSOWL4j7uzYwoxX9mmfxxtnlHHisBq8SmgpEEiDoC_CUpFfYvYACqTMqWt2ATK5LG1piWtNvTgop8NqE1a5WREs7fN54CNFwHHDEMj0HvFrGv-IeElguvegmVhiMJUfIPswpOapbbObxzJFTAb7DF1pfqLJOmLGn_nNrsx-MJwpQBANKyLT7CmAy2R01AJ72MJgsEc-dcspHsGC-ZVyEmTe390hwOxkjuZfAQ3xYyoKpxuJ1EVxm2s4b2jYwTXFWYx7GboxwSo9N2Yq6WrcvwIky_EXsl1kSYUMrjkgK_i96-zrvDSGfQNlGjTdC2J0OVP4s61A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
7 فروند هواپیمای سوخت‌رسان آمریکایی هم‌اکنون بر فراز خاورمیانه در حال پرواز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/137588" target="_blank">📅 00:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137587">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxXZnAbsUBoeOuY2-G6N0fEYL_SrY9Zbvt5UM8B4nEOKM4zvhPfuRr4uNNKEGJq7NVBYizt7W3UTih2sbV_kq2_5GOobWxIPVIBpcvQrswfjB37FapXGhfnEbyP5JT3iH5mtJGpL7ROdShcqoDa1yLux_gTCKbdo5QqS98YKJnwXgbsQDQsy8Rf3UFgKWn107c8l0XCFNesPhw2LjQ6zAht7SQ8ZyTgp6pEFbe_L7YxqhCuiMaQ0Se_aDUZSVHOSB1LapMcAJPlLZ6_bQBpXJ99mYldrBXorH6SEUfXJbGwI5Lde9LgEYLb4L2xeepKeS9Yh0rMcTO_6qkoMQ6Oqnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه جوون قائمشهری بعد از مصرف عرق با رفیقاش جوگیر شد، این حرکتو زد و جونشو از دست داد.  [@AloTweet]</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/137587" target="_blank">📅 00:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137586">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0ac09831.mp4?token=fpHIThcXPyJ3fUirJQXlV8F86d6o9u6uwg6yeAmkoECtg_Bh6UTOdUqclbMeTEk84FOl5nELG_7EtV2wGQZoKgBdBUxQoSXkSTthvXq4qaQx_d1Yvk9r37Hw51RiwFebRQE4zrH77xdxHdo7JMS14vB08G4UejT1VzYgSjHDpSpqu0dOUZdfjkUhu5NFvfE8DYClzthSR9S8A-xbKnUoCL9OANN4AgqNm8fREVufxBDHWtxOEryn6CkZhHfFmqEv87wtHl5LA8IgYeHKabNnOIUPUvlsO5R5i7nBNfO3slKY_XaQ4UJISkiNtRnyicECy4Pkt5KiYUM4D6V4ZndVNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0ac09831.mp4?token=fpHIThcXPyJ3fUirJQXlV8F86d6o9u6uwg6yeAmkoECtg_Bh6UTOdUqclbMeTEk84FOl5nELG_7EtV2wGQZoKgBdBUxQoSXkSTthvXq4qaQx_d1Yvk9r37Hw51RiwFebRQE4zrH77xdxHdo7JMS14vB08G4UejT1VzYgSjHDpSpqu0dOUZdfjkUhu5NFvfE8DYClzthSR9S8A-xbKnUoCL9OANN4AgqNm8fREVufxBDHWtxOEryn6CkZhHfFmqEv87wtHl5LA8IgYeHKabNnOIUPUvlsO5R5i7nBNfO3slKY_XaQ4UJISkiNtRnyicECy4Pkt5KiYUM4D6V4ZndVNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه جوون قائمشهری بعد از مصرف عرق با رفیقاش جوگیر شد، این حرکتو زد و جونشو از دست داد.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/137586" target="_blank">📅 00:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137585">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAZMljDUMg5DRwCf-gW55bi2VSwZ8rc0sBP7NXw-9gAcSZ36l2OliTSt7HJ7K-mstg7uvw-FihwQ4Jp79nT6h-1yLrSRjpVtChc-iVcpO23WyN_c5BxasmW9cK8uQD27Vog591ja0mylsqKPY_6CGoQJD42k0p-UR4cya-wUMbLSJsPokFH2dAbUD-xjAkXQpjjy1u8Wjgxbkq_tRtCaski0pQA83KJ_W7Cz5cEEvTlU_f9o10q0Y9uUdimzCTPR1UsXqO_lK24HdGxdX1vjon3GRWvz4cUFmACJL8wlUWCzH3BFem_MIOPvQ-D4qwCLB3_f6tsVT6ka05OMakM0VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری ایمان صفا :
من همونقدری که برای بچه های 18 و 19 دی عزادارم برای بچه های میناب ناو دنا سرباز های کشور و جنوب هم عزادارم
اینا همه بچه های ایرانن
یه سری تلاش دارن اینها رو جدا کنن و به نفع تفکرات ایدئولوژیک خودشون مصادره کنن
یه سری توله رجوی و چپول هم نطفشون بازشده هرروز یه چیزی میگن
من رو صورتم رو هم اصلاح نمیکنم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/137585" target="_blank">📅 00:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137584">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
عراقچی خطاب به مسئول سیاست خارجی اتحادیهٔ اروپا: شورای امنیت و اتحادیهٔ اروپا باید رژیم اوکراین را بابت حملهٔ جنایتکارانه به کشتی تجاری ایرانی پاسخگو کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/137584" target="_blank">📅 00:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137583">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/430d4c737a.mp4?token=mcZdbPLGjOex_EGRTaJRc49Bx8JcUdAFTRx1aTRCBoDNAGRPsrP4dkCZ1gb-E7TAh5O84-hIX_Nt_ASnqG0ckDX_Gaj0Q8P-9LQhFPIomnBSmkhIJqlvasYGRfCBAkvd-0MlUCbvmlcmeafWv2OW0vGEU6oZLwwwEBq5kcXGzBRhdEls5ukjY9Sx3DTdLjShmASxSI2HaE6wUZo4nsLHiEzUspp9zOGJiuw7IcgVo83RtR0t8LhMyyU3X4UBSTU3Sm5wdZelhoXG5WxVFgbnYP9fYlNnOuBZoQrcWvxpZHyO4QmWqW7NqRy_wqlFH_mdkjSfAJOCZx7AZXdSK6bjNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/430d4c737a.mp4?token=mcZdbPLGjOex_EGRTaJRc49Bx8JcUdAFTRx1aTRCBoDNAGRPsrP4dkCZ1gb-E7TAh5O84-hIX_Nt_ASnqG0ckDX_Gaj0Q8P-9LQhFPIomnBSmkhIJqlvasYGRfCBAkvd-0MlUCbvmlcmeafWv2OW0vGEU6oZLwwwEBq5kcXGzBRhdEls5ukjY9Sx3DTdLjShmASxSI2HaE6wUZo4nsLHiEzUspp9zOGJiuw7IcgVo83RtR0t8LhMyyU3X4UBSTU3Sm5wdZelhoXG5WxVFgbnYP9fYlNnOuBZoQrcWvxpZHyO4QmWqW7NqRy_wqlFH_mdkjSfAJOCZx7AZXdSK6bjNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شریفی نیا: اکبر عبدی پرفسور سمیعی سینمای ایران بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/137583" target="_blank">📅 23:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137582">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
العربیه: دولت ترامپ در صورت به بن بست رسیدن مسیر دیپلماتیک در خصوص پرونده هسته ای ایران، گزینه اجرای یک عملیات ویژه و گسترده نظامی برای ورود به تاسیسات به شدت محافظت شده هسته ای و خارج کردن ذخایر اورانیوم غنی شده این کشور را روی میز بررسی دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/137582" target="_blank">📅 23:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137581">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoPAxyp-Dj5NBczODqa2YDvnH8UckRIy--5OBToFT6Gu_snBynSHEFmW-g6E_KDvTL1EpdlIKqJ-dfpE2Z5D2C8E6VHce0llmlq4uKLTqT1scJxlxVDlci73vYNju4-c7q-R7rl-Af8zw_l0_wwqMJRE1wiS7zjFVK__C37sK7Oolr2IU8PK-uoN5vii8LESk7lycB0FdTEr-4giyL4zIfL3ZD_9QjlDI2c0xLs2e_LY3il5OqvsRktD6mpFXH3snaT6Cctoy0ge_kIw3uOmOXyuCIS4XL7j4gUDpaAzohzX_lhJ9daKCDp_uP8n2cOJEzzjY6Ryya5Yi37S6la1Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سید عباس تو قرقیزستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/137581" target="_blank">📅 23:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137580">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d2a9eeb2.mp4?token=YSH9zsq9Ik6WVLuDmAPWQkCKjmtnRzRpXkdyWIEwBKBAsP8WYp4zfMCJoiBq3Pnmwek0vjlcfq0XjQIwt6fxufFrcQrnyj05DW51fSGxLYPh-CXKCX19TPRNeBZGK3V_jMCKRvFws80z4yQGl-FeT0ms5xzqoQxEZyP7jCgQhfNksfhO2dSyZNhCB-NTjuKPq20USY3HawBdLCWspuOpCqdKCXKQVOGcdBxrexmZD01BlYHvgkJFWBg360oHsyvNHmJ2Yro0s_bmsZAD3I3C_BrPqafA3eq3LSDa1xk1F8m8mPFa29mVKDJZxaoJZlYyfLNYi3pWozqTQSid4pa8Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d2a9eeb2.mp4?token=YSH9zsq9Ik6WVLuDmAPWQkCKjmtnRzRpXkdyWIEwBKBAsP8WYp4zfMCJoiBq3Pnmwek0vjlcfq0XjQIwt6fxufFrcQrnyj05DW51fSGxLYPh-CXKCX19TPRNeBZGK3V_jMCKRvFws80z4yQGl-FeT0ms5xzqoQxEZyP7jCgQhfNksfhO2dSyZNhCB-NTjuKPq20USY3HawBdLCWspuOpCqdKCXKQVOGcdBxrexmZD01BlYHvgkJFWBg360oHsyvNHmJ2Yro0s_bmsZAD3I3C_BrPqafA3eq3LSDa1xk1F8m8mPFa29mVKDJZxaoJZlYyfLNYi3pWozqTQSid4pa8Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی ارتش : پدافند کشور بازسازی شده و بخشی از پدافند که آسیب دیده بود را بازسازی کردیم؛ همچنین تجهیزات جدید وارد کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/137580" target="_blank">📅 23:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137579">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMMbK_njMPoxWveqjplt3CIH1QCsBmsZbSZD88HinV_3wW8WN9tdr3Cii248oy8gfeln6yGJXyN-xOHGEOLGcsHSHY2WMQ-gCKsfviMB-R245Hi_h9cByPQGkRuhEn9EfPL-4Ll2OzFfFrU2MArQLYvK5b563WDMOEUaj-yNiQbwl68KFcufMrfz7qvc1vpj1xf5TkAqtEilQ-kMO5lgwLhTHEPAmbRKG8Nk8phYq0F1fJC39zVpUXAIbPmkYGOfO6WeFyCDlUXssdblTVwphHla4IoA2WvXqlob4X-mDut3V532WktKf-aI6oORQ-wE3TOYpwlZdtVDeTIJ9D2-ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اخبار جنگ ایران و آمریکا
در سریعترین زمان باخبر شو
🆕
کلیلک کن
⬇️
⬇️
@Breakingpersian
@Breakingpersian</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/137579" target="_blank">📅 23:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137578">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
سخنگوی سپاه: انگلیس درصورت همراهی با آمریکا هدف مشروع ما خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/137578" target="_blank">📅 23:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137577">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
خبرنگار الجزیره در تهران: هیئت عمانی تهران را ترک کرده اما امیدها برای یک راه‌حل مسالمت‌آمیز و دیپلماتیک را افزایش داده و گزینه نظامی کمرنگ شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/137577" target="_blank">📅 23:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137576">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxCJKKbwRKQ5ivGWPAbJ0t5D15cBmUGqTtU_LY42yQlrUB0KRlHEG4rNfBoPkszW38ttYvc4oH2MKiD2H5zf3xPEHWvlM4gVAfKUZt_LnELhMfVU4oIuVUBwLNFopYmvGCxEvHd5PyXWIv53BjoVvAo88hW8xsGQ1wps_aItGThustvZh37i1YjwpznRC2zVw3lnGDyxkLOHTbWE9xXUXeYdm-vBbJBvg3tv_jl-oGwKs7eppih2ykSSHr6T5t7ci_fOzhlU6xu-E2aJWC3q9aRtjunIplkarObrKV4DOHnjjohze0v6ZX2mtPvu9R3INqNhfuMfQQ4IAtKJ6I6wdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف:  حملات ایران به اهداف آمریکایی در منطقه، تا زمان تسلیم کامل دشمن و به عنوان انتقام خون کودکان بی‌گناه در میناب، لامرد و سایر مناطق، ادامه خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/137576" target="_blank">📅 23:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137575">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اینجوری که قیمت تتر هم داره نشون میده، تا یه حدی دوباره به یه تفاهم نصفه و نیمه رسیدن!  ولی صداشون در نمیاد…
✔️
@mahaneconomy</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/137575" target="_blank">📅 23:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137574">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
رسانه های عبری: کابینه امنیت ملی اسرائیل، فردا تشکیل جلسه میده
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/137574" target="_blank">📅 23:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137573">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
فوری / شبکه ۱۲ اسرائیل: نتانیاهو قصد دارد در جریان دیداری در کاخ سفید، اطلاعاتی را در خصوص احیای فعالیت‌های هسته‌ای ایران به ترامپ ارائه دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/137573" target="_blank">📅 23:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137572">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4RiTD5hkb7oIT_1E8rzDmz_aWnmAnbir3Tl5U4XbZmTM6uk2PuHNWE--wis9U5s_2nmdQD2Q-zhyYO3fZ0whfjuL07OILLwJOc0zTrx62fCnMcyNFxAibM0LrP3nlzl2YYkXYRCejuAMaAP-WOuoL4mlngaDjISzewmERde3lRHctsnxETtJFUmyUhn30CRHBtcZj2gxa3WqSa-i-aLjzn7rrzEuO7SJOIR4EjIOeBOLj1YTMBK081JNOp6Xuhawjya5GBkKY4UL1rRSrqMkvhGpEmZTiZtg_Xe85Fn1xwQZwVpWKn2szxjcBZW-1vxOy6CZ74qKF_zSSs-UmnbAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زلنسکی مدعی شد: روسیه به ایران در تصاویر و دیتای ماهواره‌ای کمک می‌کند!
🔴
رئیس جمهور اوکراین: از ابتدای ماه جولای، ما نظارت ماهواره‌ای فعال روسیه بر کشورهای حوزهٔ خلیج فارس و تأسیسات نظامی آمریکا مستقر در آنجا را ثبت کرده‌ایم. این تصاویر متعاقباً در ایران ظاهر می‌شوند. همزمان، همبستگی آشکاری بین تصاویر ماهواره‌ای روسیه از این مکان‌ها و حملات ایران وجود دارد – هم پیش از حملات، در مرحلهٔ آماده‌سازی، و هم پس از آن، برای ارزیابی خسارت واردشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/137572" target="_blank">📅 23:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137571">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-k4W4vydaLoz7E8uUSdVzCaRjgraDkSR3gzTVKiLMHOU1Ma7rKLu48D7pO7tNtPexzp_DZC5KReh2O3n5xYncNPamQK4Bh4xMiW0qHOmLCD6Zus5quSeW8l-jwbNBPhJ_wclt_SYT7K70Xn2TTiOj5jrU39wZJwH2vg-epQpvZEH6B-BcBbfzjvoDyr33rUDRHiz6I-0e34s4hIv4b-KcGBG3VAg1RW1pR0U0pIyWiUz2leUjNB7C65RJF2IxIM_Nuwq0fHqlipEQjKdBhVkAmSKNTvMN15e0M8PATipspPPMXxlo6v1E0fx56xaA5HYA_HUKLAKKOiXYZTdCQo6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل:
یک پهپاد در نزدیکی خانه بن گویر در هبرون سقوط کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/137571" target="_blank">📅 23:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137570">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
سخنگوی ارتش: بخشی از پدافند که آسیب دیده بود را بازسازی کردیم؛ همچنین تجهیزات جدید وارد کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/137570" target="_blank">📅 23:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137569">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ادامه آزار و اذیت ماهیگیران ایرانی توسط نیروهای دریایی کویت به مدت چند روز متوالی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/137569" target="_blank">📅 23:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137568">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
پیت هگست، وزیر دفاع ایالات متحده، به MTV گفت: ایالات متحده در روزهای آینده حمایت خود را از ارتش لبنان افزایش خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/137568" target="_blank">📅 23:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137567">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBIr_lQ_BphHMQxLxlU4S36XmcNNNsima-nE_fkNJw_aQDKgWxPSMyLfLYAn0G9_dKu8Bvmhgqi8IMMrX4lU22Sgv2tXSOr7NH1WTZOo6xaVL_MQ5eZESnpkopUPDp10lBUZWKd-pKjpvnXMh9bRGaJOAyyJHbAjIvJJkSxHCMF4gdsqo1IaWPsak6YJ0peYEPaa7zrTmPrgqRvKvbze5oE9tuVr_GkXgwDNhSz9v_pWOkJaCluuRK6CrYr4lMixrWq-hlMTPPhOmK-7ywnxcoRxfE2yAg7eEd73unedhrNBH7HpHAgsS7ZRZIIzCTEIja8G4TgHSFOxfjzp0FN3rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
تماشا برای زیر 18سال ممنوع
‼️
❌
ویدیویی منتشر شده از سواستفاده جنسی از کودکان در جزیره
اپستین
!
🚨
مشاهده برای افراد زیر ۱۸سال و افراد دارای مشکلات قلبی ممنوع است
◀️
مشاهده فوری فیلم</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/137567" target="_blank">📅 23:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137566">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8N6WT5bSfN2zuEkJl7uqpCb3TPQgsmQPW5eE4SBLmaRhoxtfKG0bzJz2nM3x-oI8RFxMTriMR5crV0Tq_WLbVSmwCNAq38vnmagRrTp0weFeEqzxENS8tPblrioXVvO9RSs9dWFE4dJIhHY6mBdUp-TKH1MIbARSV1ZPLaQtyyfjuNSDZkfI4B_lc_4f6ap-jV4qWmXPdJYSzmYhuPhJyz0cKY22-_k1dkyURMAoxyhR7CaZC2vBqbvr1xkGpzNiP0X8kFbXg0C1hT7Wvxm5U3pi3JZN0VsE-TfR6h7HGy_nK6SyKfi7ytsMkc63V-ZNhsZABj9fvOBnPqWcx34uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شهریاری، گوینده جمله تنگه ارث مامان ثابتی:
اونایی که شب‌ها تو خیابون ول هستن، شعارهای
کصشعر
و متوهمانه میدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/137566" target="_blank">📅 22:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137565">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل:
نتانیاهو قصد دارد در جریان دیداری در کاخ سفید، اطلاعاتی را در خصوص احیای فعالیت‌های هسته‌ای ایران به ترامپ ارائه دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/137565" target="_blank">📅 22:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137564">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/alonews/137564" target="_blank">📅 22:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137563">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/137563" target="_blank">📅 22:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137562">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIU1C4EHsnAOqnbdnKL8F3LyC7-CJyzGEK2A2e8afdCe7trSyCga7E0MQUmvJIhxEZTBUS0QBEGZYRNS65xBd3GFn_VRu_ogPs_BIxrbA0gHV3P7QABgIZWscUfNvcIvmoPILTRHlomVYsl5G4BunuDgmoDHBTjmgzIbUp5wqzHpht7QZrNzdMO4hpwt1Wx42iFX1wK-YLshUNMrjHcG6koSi-8Im9O64_6dmEDnuZ2qSVZyJ5YZXQa5ycnFe4hLYUFkJErAhtPw-ZtptQHH9cCCGBB_Wq-w2-uvq5mOa_XdwP9_4tpuFTrj9XDIfoTytFmf72Z6JEMu-9oDF8R6QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
وزارت خارجه:
حمله اوکراین به یک کشتی تجاری ایران در دریای خزر که منجر به شهادت یک ملوان و زخمی شدن یک ملوان دیگر شد را به شدت محکوم می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/137562" target="_blank">📅 22:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137561">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzeUPMyP6kXQYnKtGwFZli7vq42HIuje8H-egxDTRlneRKzT8dokvrnUODi82jKhPH8huxVmOX9cH8nHo77wpOErtlT7Dj1SWBFf_PaoKXmcOz_ruMpIkuL55e0SWAf63T4MYcWo-SZP-WvEAs4lAVwdwCjOmGmAZpd2NY7goWNtXD6ExSkRhDQCgD8z2lAsis4PABw51J0VWsiA94BbglXsuJyO4G8x9SU92JLas73BdjteB094FlUr_40b4klLkYjbehM5Mt-tahhhYHl1DOvnSknZ17Um4ZXXF58Pt2G4eBstaX2n_0sXly5rfffKL20beSRPYREUIg2dMzsXgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دقت کردید از وقتی سوریه دست جولانی افتاده دیگه کسی نگران حرم نیست و امنیت دمشق رفته بالا و زائر هم اونجا بیشتر شده؟
🔴
پ.ن:قبلا میگفتن دار و دسته جولانی میخواد اونجا رو منفجر کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/137561" target="_blank">📅 22:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137560">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
سخنگوی ارتش: تمام پایگاه‌های آمریکا در اربیل عراق نابود شده است
🔴
‏دیگر توان عملیات نظامی از پایگاه‌های اربیل وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/137560" target="_blank">📅 22:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137559">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzezwKAFoS7bm-AWDhhBwUgKXfSV76kMr9e1J4AusYmCDrCOOtbsIhltP47U4VsYIIjWbPzCjp6ykbXU7TNeX0lVsfwPumc9Xp_st7cpJSTSAIr7q_CfEhmf40ecaoRMEkxkSyX117vT0RBr9TSbaEESzArrsp7eBJLATPt4mVRwU0EO4l5mavYZZ-et52uG8cz2EAOLOcN43L-YF35_QcDbLHZHm5vLxbvAOQBDt9dRWoUF7aufI4MArTXshyqs6G7eAWYvVzsgOP2JJpZJHizjeiQkyuK62q8akuSyGYe3SvWRJbUOM93SO8TFnx7t5WFDV8l0LNVjoJ1aMY4V3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاهش محسوس در ارسال ترابری‌ها به منطقه؛ به نظر می‌رسد هر چیزی که باید به منطقه منتقل می‌شد، شد
🔴
بیش از ۲۴ ساعت از آخرین شلیک آمریکا می‌گذرد و گام بعدی مشخص نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/137559" target="_blank">📅 22:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137558">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45fbc06d1c.mp4?token=XpKmUtr5Dl0hHS37Bp2Pnd6B9rFpMODFt957k-UWL7HhJNqTCqfv5jsiRlsQhLJqhfWIMYqcwroqJ5zeEW12HwsGkOX9AwGWK7Xcxf4-hpogdZ8V-tgWnkYEq7mJAjE9RokONNs8LktHbU_ymLcrvbM7dZk2RLSjm5jOVZujia-FOcXfg7bKIE7KxOUAqYXOmiLFbwwxLv_vT8E_q_q6XxYRNsgE8p1FDK0-UQGPzEiwd0lI909WVbDd1PPzZ7Mi0hYmDKo0DakKDHwRJHr0RStj9veMjMFofDuZBUELOTp1dxYPQbL5_6AuIJZ-BZKaNXxh32XAUkyXf4PbbkE6Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45fbc06d1c.mp4?token=XpKmUtr5Dl0hHS37Bp2Pnd6B9rFpMODFt957k-UWL7HhJNqTCqfv5jsiRlsQhLJqhfWIMYqcwroqJ5zeEW12HwsGkOX9AwGWK7Xcxf4-hpogdZ8V-tgWnkYEq7mJAjE9RokONNs8LktHbU_ymLcrvbM7dZk2RLSjm5jOVZujia-FOcXfg7bKIE7KxOUAqYXOmiLFbwwxLv_vT8E_q_q6XxYRNsgE8p1FDK0-UQGPzEiwd0lI909WVbDd1PPzZ7Mi0hYmDKo0DakKDHwRJHr0RStj9veMjMFofDuZBUELOTp1dxYPQbL5_6AuIJZ-BZKaNXxh32XAUkyXf4PbbkE6Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
‏مجری صداوسیما میگه موساد بچه هامون رو در دی‌ماه کشته بعد احمد قدیری کارشناس میگه در دی‌ماه در یک اقدام انقلابی گفتیم کف خیابان بکشید چون دستگیری و دادگاهی و اعدام دنگ و فنگ داره و مجامع بین‌المللی هم گیر میدن! همونجا کف خیابون برای حفظ« پرستیژ» بزنید بکشید و خلاص...!
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/137558" target="_blank">📅 22:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137557">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">📱
لطفا توییتر الونیوز رو دنبال کنین
🔴
پست های انگلیسی در رابطه با جنایت های حکومت به انگلیسی نوشته شده و افراد مهم منشن و هشتگ های مهم قرار داده شده.
🔴
ریپست کنین. مهمترین کمک این روزها جلوگیری از پروپاگاندا حکومت علیه این قتل عام مردم هستش. خونشون نباید پایمال…</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/137557" target="_blank">📅 22:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137556">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IR05YcAzkVQlyHOuC-i-m5vqOi3NpfeaDM9b62jv1_RRabE8612ygQ1tSg2wm5LGDTXvgr1EIvz9C4MTXALKObrq4blTZhpVzDgsertXEyZXqqbx4V27frZlQHhQ4KeXDdFV0rjPLDOBBu11eNodnFyEO1bCouVIGA3qQhQUdvqb3xQMfBN7fyt3CwkkUvZEuLtIYpFLw1KCdSRGia0npTgKccCZTBWqIQOmWK5xJv79b4rt1_8m-jJrYZ03Mys7HjXu4bsB3y2pxJeN9aFfQg05hf_CABReuFd4Lkx8xunoEbZkY_3K9NXIjnQu94ni465N0LrrJmzGakGfzL3oLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ژیلا صادقی: شیر تو آمریکا لیتری ۶۰۰ هزارتومنه ولی تو ایران خیلی ارزون تره
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/137556" target="_blank">📅 22:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137555">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/137555" target="_blank">📅 22:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137554">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db14df2e2d.mp4?token=vnGqq12YgQoFBnPpugP29o0akisERkMYHp98rfz1iTwRp9A9fsOspKJYoUWeSMR8Tdj1I0c4Uc8YQGwrXZ-TbcTbyBXcgZw5ApkUFYi1led_9Wb3aI34ZT9nx0oMb_lToA8-unMCs9WyaHwxT1CHoBg1yfYWzcu4YXdSerlHNsuixisLwu51eHZue20kM89Xq79KVBlt19_QX5qQY18kz8EMfAOwmrznYlicLvpQuKGAkSHC-t7qnm2opQeR5_-rxcFVBcpojhwnAMt8IotC-MRmToqghZHisq7wyefZw0iX2w8XdwhpwUnPB4fb-WFu4QTXEQvhryLyHOWjn2XBMZnygXA8nzSLDMNETQ6qPFinIWl2b45yexYcDR33SIq-7LV8w91zi8N1p37GNcX620q58PFw_btjxASFHarLpkCeMxdFP6HOR2FLT7ojHfilTS9elw_wKr-oqSNxypeQBYSvrilitLelI20RadiC865LQLNb_ccn9sSL8Ucfkl_mVmkTwzfz2mCIejWGLtE0riyzhWCkujkgxPla5avH6e0VnSFD_boxGT1yysfm9ar4lgGzdGB7Phi50jE1nN6_xQ7hUhemwl89gGGLQnmDLRh12V7IzYZJ-8P-IXo1DMSlOBd8SRfw4XN6LM8ONfujKmi9WnR0knUepQlgkw9ZjrY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db14df2e2d.mp4?token=vnGqq12YgQoFBnPpugP29o0akisERkMYHp98rfz1iTwRp9A9fsOspKJYoUWeSMR8Tdj1I0c4Uc8YQGwrXZ-TbcTbyBXcgZw5ApkUFYi1led_9Wb3aI34ZT9nx0oMb_lToA8-unMCs9WyaHwxT1CHoBg1yfYWzcu4YXdSerlHNsuixisLwu51eHZue20kM89Xq79KVBlt19_QX5qQY18kz8EMfAOwmrznYlicLvpQuKGAkSHC-t7qnm2opQeR5_-rxcFVBcpojhwnAMt8IotC-MRmToqghZHisq7wyefZw0iX2w8XdwhpwUnPB4fb-WFu4QTXEQvhryLyHOWjn2XBMZnygXA8nzSLDMNETQ6qPFinIWl2b45yexYcDR33SIq-7LV8w91zi8N1p37GNcX620q58PFw_btjxASFHarLpkCeMxdFP6HOR2FLT7ojHfilTS9elw_wKr-oqSNxypeQBYSvrilitLelI20RadiC865LQLNb_ccn9sSL8Ucfkl_mVmkTwzfz2mCIejWGLtE0riyzhWCkujkgxPla5avH6e0VnSFD_boxGT1yysfm9ar4lgGzdGB7Phi50jE1nN6_xQ7hUhemwl89gGGLQnmDLRh12V7IzYZJ-8P-IXo1DMSlOBd8SRfw4XN6LM8ONfujKmi9WnR0knUepQlgkw9ZjrY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایلان ماسک: در سیاست زیاده‌روی کردم!
🔴
بهتر بود به جای دخالت در امور اجرایی واشنگتن، تمام تمرکز خودم را روی مدیریت شرکت‌هایم می‌گذاشتم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/137554" target="_blank">📅 22:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137553">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
وای‌نت: قطر و عمان تهران را تحت فشار گذاشتند تا سازش کند و از یک عملیات تقریبا قطعی و بزرگ آمریکا جلوگیری کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/137553" target="_blank">📅 21:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137552">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ترامپ در گفتگوی تلفنی با شبکه فرانسوی «ال‌سی‌آی» (LCI) اظهار داشت که اگر «صددرصدِ آنچه را می‌خواهیم به دست نیاوریم»، «قطعاً» گزینه ازسرگیری جنگ تمام‌عیار علیه ایران را مد نظر دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/137552" target="_blank">📅 21:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137551">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vohlvh_cj8t_s9laa9W00N_yd7qPDW9BCvBXV6iqVSjZfoVfvNA6dalY-MwrOpzh5oQ8l94EVipSrDhMyFQSD4Hd58KuxBU9B-jzGiyxePs_gDWjBFufncsl-8rczsKZPZ9fKNxE4uLCDIze_iEv_Qv1lE8gHX_fSQR-Di7pvxcAmj6AoaDFBn0d7WOVWfsuGlNtmSYwtaZoBeij2WpDFejNHms4hx_gzgPPFhjwv6ZRlVpOu-fw7DGGfb88GmpZgOt-Yhj9NQkXSnCEHZ4PijraSfZv2zEg6-ZBHAsOuyGBikTxn-uTCVoBtqbYezna5X308iKsJCWtFaVf9ZIqDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای آواکس E-3G Sentry متعلق به نیروی هوایی ایالات متحده در آسمان منطقه به پرواز درآمد.
🔴
این هواپیما شب گذشته حضور نداشت، اما امشب دوباره در آسمان درحال پرواز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/137551" target="_blank">📅 21:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137550">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmuZ2h_ysEGyEyKzg5o2q144qt7KaIoiECuVlNXxWhu9No6Lg-B2yfhUkmSi7I9di-iN-bkuercov9r0yfuWtnGlXaxCo79fmJALHSulWqeUwfLB92_JDqf8QBEWwiRmHP0-_sWrv71uzTOMhT9yVzuPN1ctC6bQ8SEvQE9N5ew6gql6JTr3D8fh852Bz1e6hdYqGHpwMuFmGzbe8SFcCil2MQyYmvq5nT93r7JibnovfQyPJVXypE7J5mttm8oEukHl5fCubpSSPzWyjVMPtA5ZSzQ5pmbig5D6YkgHFmJgI9T8jFHDuVlG2f4J94I2APqnLJsgVk9SCJSfjKS8ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به نظر میرسه عملیات پل هوایی آمریکا به پایان رسیده؛ درحال حاضر فقط 4 فروند C-17A در حال پرواز هستن. هر چیزی که باید به منطقه منتقل میشد، منتقل شده حالا بعد از حدود 18 ساعت بدون حتی یک شلیک، مشخص نیست گام بعدی چه خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/137550" target="_blank">📅 21:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137549">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
منابع وابسته به سپاه : کل خاک اوکراین در دسترس موشک‌های بالستیک ایران قرار داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/137549" target="_blank">📅 21:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137548">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7f5eac88.mp4?token=OOl0AxjHPvf4PToLoNocUQCYpcBqHnzAE0_7bOSEHATkVJuJZMAYcbZigd87y6eJp3kVPGGcfGZGrJ4kweWMSlOM_SFlZ2WtCVE3U3zksg43ovwTDm8daiZE__0O-aeLMYVuGp8qPu3UjV1SmsLH2nRTdOAviWoNpfhJ60Uoz4SpaKTqYrMLNc-vGn3RRuCmCOakavWrTfNve2pyj_ANpTcqHv4HLNWNVtWgeTbLexDmrlfE0SgOd8td5_fj1tOlvnJkjeWt003eYLQ1jvdzLhMhRDogodKaQML3uup7LUElA6CVZ1fPwuIQM4liM9pjtBcR3XvnZl29WjolPYCT0oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7f5eac88.mp4?token=OOl0AxjHPvf4PToLoNocUQCYpcBqHnzAE0_7bOSEHATkVJuJZMAYcbZigd87y6eJp3kVPGGcfGZGrJ4kweWMSlOM_SFlZ2WtCVE3U3zksg43ovwTDm8daiZE__0O-aeLMYVuGp8qPu3UjV1SmsLH2nRTdOAviWoNpfhJ60Uoz4SpaKTqYrMLNc-vGn3RRuCmCOakavWrTfNve2pyj_ANpTcqHv4HLNWNVtWgeTbLexDmrlfE0SgOd8td5_fj1tOlvnJkjeWt003eYLQ1jvdzLhMhRDogodKaQML3uup7LUElA6CVZ1fPwuIQM4liM9pjtBcR3XvnZl29WjolPYCT0oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بزالیل اسموتریچ، وزیر اقتصاد اسرائیل:
خداوند در دهه‌های گذشته، کارهای شگفت‌انگیز و معجزه‌های فراوانی برای ما انجام داده است.
🔴
پس از 2000 سال تبعید، آزار و رنج و سرگردانی، ما به سرزمین اسرائیل بازگشته‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/137548" target="_blank">📅 21:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137547">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae537cb11c.mp4?token=MLsuYai9aYgtThjzINMZwPXOo_cbX6vhEvSRAfd4dEuUNQTFs5V1xlQUMQ1QQjzhoBZNZltLjl5UdXVXD7jL8nVVRP_M38olt0tCQfgR5neC1m_dqgWgiKgr5oG8AIHCGFaXe-dXLIe5SaFodPm8DN2hD9IX--AcYj-h-pG1FKz1n82o6PwISIj_s8OVPwhXF42Z3JiLhXQ5X5MV3Pa86aTgomy3vbUg0gKy8si9GVErO26dQSzMxCiDYQqmEQ6GxsXNi6_lXx3VbhdH_HMjjyXAh-KIjltCtb-QMNlGYqjlpk1wlcOXKGyvcGEJDysVvzCrwHkcYTznlR1Vovod0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae537cb11c.mp4?token=MLsuYai9aYgtThjzINMZwPXOo_cbX6vhEvSRAfd4dEuUNQTFs5V1xlQUMQ1QQjzhoBZNZltLjl5UdXVXD7jL8nVVRP_M38olt0tCQfgR5neC1m_dqgWgiKgr5oG8AIHCGFaXe-dXLIe5SaFodPm8DN2hD9IX--AcYj-h-pG1FKz1n82o6PwISIj_s8OVPwhXF42Z3JiLhXQ5X5MV3Pa86aTgomy3vbUg0gKy8si9GVErO26dQSzMxCiDYQqmEQ6GxsXNi6_lXx3VbhdH_HMjjyXAh-KIjltCtb-QMNlGYqjlpk1wlcOXKGyvcGEJDysVvzCrwHkcYTznlR1Vovod0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بزائل اسموتریچ، وزیر مالیه اسرائیل:
درسته که محور تحت رهبری ایران تضعیف شده، اما احتمالاً یک محور سنی جدید شکل خواهد گرفت و ما باید با آن مقابله کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/137547" target="_blank">📅 21:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137546">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb3075e4fb.mp4?token=qYlm8AyVa9VeQU1aO-y0XZ2aGdP4cAA6-vTzeFOxqQ5iLlYA8do4tDRNyuALmw3rro6e-8EGaC4eCMUjwzWkukCtgOw0GZLv2Dn1WD5YkhQjWKdTjyAMGCnK6fROdcB3zVmE5Zl2sMuALpX0alUbHb2HvFb47FQcDLL4-gStSjdlHrG3TOcSo-GdcfwcRrTe6r4scOipbYPjgHjrGPvOimxRVR28-BipoFkNSzEPiQCBzWQMyKILkpWbT35BnPpEWTMd5opiBslpX3dkXlCj3AOlGa6_ol3sukXPfYeyH-0CNF-EeDImG9GXt0aDdKA9c6MWHNX98O_LWDYRGNrJxYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb3075e4fb.mp4?token=qYlm8AyVa9VeQU1aO-y0XZ2aGdP4cAA6-vTzeFOxqQ5iLlYA8do4tDRNyuALmw3rro6e-8EGaC4eCMUjwzWkukCtgOw0GZLv2Dn1WD5YkhQjWKdTjyAMGCnK6fROdcB3zVmE5Zl2sMuALpX0alUbHb2HvFb47FQcDLL4-gStSjdlHrG3TOcSo-GdcfwcRrTe6r4scOipbYPjgHjrGPvOimxRVR28-BipoFkNSzEPiQCBzWQMyKILkpWbT35BnPpEWTMd5opiBslpX3dkXlCj3AOlGa6_ol3sukXPfYeyH-0CNF-EeDImG9GXt0aDdKA9c6MWHNX98O_LWDYRGNrJxYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بزالیل اسموتریچ، وزیر اقتصاد اسرائیل:
رقابت جهانی در زمینه تسلیحات، فرصت بسیار بزرگی برای اقتصاد اسرائیل و صنایع دفاعی این کشور است. ما در این زمینه، پیشروهای جهانی هستیم.
🔴
حتی کشورهایی که از نظر سیاسی یا دیپلماتیک، تمایلی خاص به ما ندارند، باز هم در این حوزه به ما نیاز دارند.
🔴
ما شاهد حجم سفارش‌های بسیار زیادی برای شرکت‌های دفاعی اسرائیل هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/137546" target="_blank">📅 21:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137545">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
اکسیوس: به احتمال زیاد، مسقط و تهران امشب یا فردا به توافقی در مورد هرمز خواهند رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/137545" target="_blank">📅 21:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137544">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا اعلام کرد یک پرتابه به یک نفتکش در ۷۰ مایلی دریایی منطقه «الشقیق» در سواحل عربستان سعودی اصابت کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/137544" target="_blank">📅 21:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137543">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDZ7lZykvzN7mAi9BLJ2_5CLOu8MbE_HvBx9JX02H4lkETIIOK4w2RkPnAMuPXBymyVfpNEDx4GQuOzJ78p3k-aDa5uNNnWl5mL4pVSoIp9rMLr204bR2OZJ-UFsB6pyy6Rr2obUhot9bsdU1mqk4v3Fr7wVT3SJtqQvRPZqoqI12fQVD_pJy5ocdyiyat111x4t253hP2UaJeVNJ2s04hDB-bXCDaAEOmMSNIykEE9jIKwOe3mN4zPepf86bhn2-kwRZciVa_bmSZ8t1mY9rkzHN8gT8d5gGjtnH25Qll-chpwBW0lloFliiHUzQgR0meZZog48LerbNwetkBBJxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انتقاد کتی پری از کاخ سفید بخاطر استفاده از آهنگش در ویدئویی از حمله به ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/137543" target="_blank">📅 21:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137542">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
سازمان رادیو و تلویزیون اسرائیل: در حال حاضر بیش از 90 هواپیمای سوخت رسان آمریکایی در اسرائیل مستقر شده اند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/137542" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137541">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
گزارش زلنسکی از برنامه های روسیه برای ادامه جنگ: پوتین در حال آماده‌سازی مقدمات برای یک بسیج گسترده‌تر است.
🔴
ما همچنین شاهد همکاری روسیه با کره شمالی هستیم. روسیه قصد دارد 30 هزار سرباز دیگر را از کره شمالی دریافت کند و آمادگی‌ها برای پذیرش آن‌ها از ماه ژوئن در منطقه وورونژ آغاز شده است.
🔴
کره شمالی نیز در حال آماده‌سازی برای انتقال سامانه‌های پرتاب جدید برای موشک‌های بالیستیک به روسیه است.
🔴
روسیه به کره شمالی کمک می‌کند تا نحوه جنگیدن را بیاموزد، سلاح‌های آن‌ها را بهبود می‌بخشد و به آن‌ها تجربه استفاده عملی از این سلاح‌ها را در دنیای واقعی می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/137541" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137540">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ad5f15cf.mp4?token=GcrzXgwWGGm7v2nAUZf09DXz1jOQKjeLIBuKGXYR-QGbUO3psimBox4PGNc3_mRNZw3qiHpSugz33rJ6R8dUdiY_g5tjiYs5Rhy3elvpR1LnOH-piv1JZ-JMUGv-UUjXL1WF8bJ4zTXSjYiiiMKZtwimq5WQLboPebMtAkY2OcwUHcGoNdZ7gEcsUn5vZEeT63QDu5N57Gf3y9yHQg8vowOayh7_hj-c26vOeAwyjphqLTA0svdrhoDuXqs3bS9RQNsHCQaD-l_9kXJB3dNhmkpQI-7_Woo_sWi6YK-vp2rTHuRoh4qBIJlnl8VKqqwHmACrET9DjE_91PZayiQeO2AgfYBdxgEYFQfGZMZIj43uy9zFBKUS2TSNIIipxhNFO1H2Aa-_b7Mpy56YxgrnSRBE8IP4LPiWjwUsAT-l_Og78MEb_XLvxUP3K7gZA9RgyeHqvSlyYlgryFwS_kyI8bzZO0VmYtppT4bnDYtQ5nwzgc9IZUO-RQr_xeZw-LFVi61nE5vzRCwbDrYdpuKx10SK0PeBYCUPg5udAtuGyzins76LThQy6QlqzQ4k7YP6F4ZwkN0vUWUn7KQo5WvqPw69xx_44HV7C4VCEV6N8zW16moL-W2MWz5I9gJpRFb8uCmAQLRfXQwzGT_V9cOTBuM73UcIY2WBO_v2_Te5Eyo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ad5f15cf.mp4?token=GcrzXgwWGGm7v2nAUZf09DXz1jOQKjeLIBuKGXYR-QGbUO3psimBox4PGNc3_mRNZw3qiHpSugz33rJ6R8dUdiY_g5tjiYs5Rhy3elvpR1LnOH-piv1JZ-JMUGv-UUjXL1WF8bJ4zTXSjYiiiMKZtwimq5WQLboPebMtAkY2OcwUHcGoNdZ7gEcsUn5vZEeT63QDu5N57Gf3y9yHQg8vowOayh7_hj-c26vOeAwyjphqLTA0svdrhoDuXqs3bS9RQNsHCQaD-l_9kXJB3dNhmkpQI-7_Woo_sWi6YK-vp2rTHuRoh4qBIJlnl8VKqqwHmACrET9DjE_91PZayiQeO2AgfYBdxgEYFQfGZMZIj43uy9zFBKUS2TSNIIipxhNFO1H2Aa-_b7Mpy56YxgrnSRBE8IP4LPiWjwUsAT-l_Og78MEb_XLvxUP3K7gZA9RgyeHqvSlyYlgryFwS_kyI8bzZO0VmYtppT4bnDYtQ5nwzgc9IZUO-RQr_xeZw-LFVi61nE5vzRCwbDrYdpuKx10SK0PeBYCUPg5udAtuGyzins76LThQy6QlqzQ4k7YP6F4ZwkN0vUWUn7KQo5WvqPw69xx_44HV7C4VCEV6N8zW16moL-W2MWz5I9gJpRFb8uCmAQLRfXQwzGT_V9cOTBuM73UcIY2WBO_v2_Te5Eyo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار علیه شهریاری در تجمعات شبانه؛ مرگ بر جیره خور آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/137540" target="_blank">📅 21:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137539">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
وای‌نت: اسرائیل خود را برای حمله گسترده آمریکا به ایران در فاصله شب جمعه تا بامداد شنبه آماده کرده بود، اما دونالد ترامپ برای دادن فرصت بیشتر به مذاکرات، این اقدام را به تعویق انداخت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/137539" target="_blank">📅 21:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137538">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
تايمز  اسرائیل: ترامپ از ارتش آمریکا درخواست کرده بود که حمله به ایران را به تعویق بیندازد. او در حال حاضر ترجیح می‌دهد که به مذاکرات ادامه دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/137538" target="_blank">📅 20:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137537">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سخنگوی سپاه: طی ۱۵ روز نبرد (از ۱۷ تیر تا ۳۱ تیر)، ۱۱ هواپیمای جنگنده و بالگرد آمریکایی را روی زمین و در حالی که در پایگاه‌های آمریکایی در منطقه مستقر بودند، منهدم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/137537" target="_blank">📅 20:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137536">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
آکسیوس به نقل از دو منبع: ارتش آمریکا در حال کار بر روی طرح‌هایی برای عملیات بزرگ احتمالی علیه ایران است، اما ترامپ هنوز دستوری نداده است.
🔴
تصمیم ترامپ برای توقف حملات در روز شنبه، ساعاتی پس از ورود هیئت عمانی به تهران برای مذاکره در مورد تنگه هرمز اتخاذ شد./ ممکن است تا پایان هفته، توافقی بین ایران و عمان در خصوص تنگه هرمز حاصل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/137536" target="_blank">📅 20:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137535">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
دو شرکت زیرمجموعه لوفت‌هانزا آلمان پروازهای تل‌آویو را تا سه‌شنبه لغو کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/137535" target="_blank">📅 20:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137534">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF):  در پی گزارش در مورد یک تیراندازی در منطقه جامعه سوسیا، کمی پیش از این یک درگیری خشونت‌آمیز بین شهروندان اسرائیلی و فلسطینیان در منطقه شکل گرفت، که در آن هر دو طرف سنگ پرتاب کردند. این یک حادثه تیراندازی نبود.
🔴
سپس یک تروریست سلاح یکی از شهروندان را دزدید و به سمت آسمان شلیک کرد. علاوه بر این، یک شهروند اسرائیلی در نتیجه پرتاب سنگ‌ها مجروح شد و برای دریافت درمان پزشکی تخلیه شد.
🔴
سربازان IDF در حال تعقیب تروریست هستند و در منطقه چک‌پوینت‌های جاده‌ای برپا کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/137534" target="_blank">📅 20:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137533">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
معاون نخست‌وزیر و وزیر امور خارجه پاکستان، ایزاک دار، با شاهزاده فیصل بن فرحان آل سعود، وزیر امور خارجه عربستان سعودی، گفتگو کرد تا در مورد آخرین تحولات منطقه‌ای تبادل نظر کنند.
🔴
آن‌ها همچنین در مورد امنیت مسیرهای کشتیرانی در خلیج فارس و دریای سرخ گفتگو کردند.
🔴
هر دو طرف مجدداً بر روابط نزدیک بین پاکستان و عربستان سعودی تأکید کردند و بر اهمیت ادامه دیپلماسی تأکید نمودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/137533" target="_blank">📅 20:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137532">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
الحدث: وزیر خارجه عربستان تماس تلفنی از همتای پاکستانی خود دریافت کرد و درباره تلاشها برای کاهش تنش در منطقه گفت‌وگو کردند.
🔴
وزیر خارجه عربستان و همتای پاکستانی‌اش درباره تلاش‌ها برای تأمین امنیت و ایمنی آبراه‌ها بحث و تبادل نظر کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/137532" target="_blank">📅 20:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137531">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
رسانه‌های عبری: احمد وحیدی و مجید موسوی در صدر فهرست اهداف ترور اسرائیل قرار دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/137531" target="_blank">📅 20:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137530">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gU7T2uI8ochagAYINdINXI_FKYp4Ef3T8Mcif86IizbrOgvu3nhJoKbEao0n7QJD40lazc2-vfVRNeDtmI0p1aWOervYZJO12uIYj6z2aelci_mNnR4KsZZUpoJK7hAv_Fech_Xkv2ulw65nOTdUMyvOX5scUKz7xAD4boJmKH4nL5bouQBexn0iJg1iHrS9DTSL7jznNg8jT9A1_Wyypx5BA_jkljrrU_zlZmoHArp12-F-EEHoSW_T_nKC9-RxEvyI2rH6LoHrbEQz8wG0lxQklxfTDVsOWpORoVtB5E2ed-FjsRCgLbo3vbpdujh7sJyxFMIDboTdVVcg9PxYDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صفحه رسمی سفارت آلمان در تهران شایعات تخلیه کارکنان این نمایندگی دیپلماتیک رو تکذیب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/137530" target="_blank">📅 20:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137529">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80c6d15482.mp4?token=fcn5F9m5FEn9BPfFNxLkqZKsyJX0VHVwixMvFiYUZClbWb93IrvZ4nzQHO_OmyB2oept68szq1dQF4HZM4T0uBCzhHT5NaqZpBxKW88woP4JM7BziB6aWxDs2Pcq7Ic5tD28ELf13eGLcdt3rh_Pvae8WIUIwZJRpLAyNsRAiqmpskbqCcNurO2al8NsZCyTAa5IHp6XYq2sMLBdhaXpY57zHivKnmY-0Yi94Gn9A5_oTeyZDJioimNHoRk4ZeRi75kGcHT7x6BAkxAxkE1ntSQT7IBms88vD0BAlVgwG2qOAXLqnlv4qB1Wt1MGacOOLQQARFethYgYvIzodoTKFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80c6d15482.mp4?token=fcn5F9m5FEn9BPfFNxLkqZKsyJX0VHVwixMvFiYUZClbWb93IrvZ4nzQHO_OmyB2oept68szq1dQF4HZM4T0uBCzhHT5NaqZpBxKW88woP4JM7BziB6aWxDs2Pcq7Ic5tD28ELf13eGLcdt3rh_Pvae8WIUIwZJRpLAyNsRAiqmpskbqCcNurO2al8NsZCyTAa5IHp6XYq2sMLBdhaXpY57zHivKnmY-0Yi94Gn9A5_oTeyZDJioimNHoRk4ZeRi75kGcHT7x6BAkxAxkE1ntSQT7IBms88vD0BAlVgwG2qOAXLqnlv4qB1Wt1MGacOOLQQARFethYgYvIzodoTKFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ موقع تعریف‌کردن ماجرای تیراندازی در ضیافت شام خبرنگاران کاخ سفید یاد نیکی میناژ افتاد: «بعد از اینکه صدای تیر اومد، مردم داد زدن: "بخوابید زمین! بخوابید زمین!" همین باعث شد نیکی میناج شروع کنه به رقص و تکون دادن و قر دادن! باورتون میشه؟ خدایی فقط اون بود که فهمید منظور اصلی “Get down” چی بود!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/137529" target="_blank">📅 19:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137528">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
برخی منابع می گویند:  با افزایش احتمال شدت‌گیری قابل توجه تنش‌ها، بار دیگر میانجی‌های مختلف پاکستانی، عمانی، قطری و... هر یک با موضوعات و طرح‌های مختلف در ۴۸ ساعت گذشته فعال شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/137528" target="_blank">📅 19:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137527">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
پس از اتریش و ایتالیا، دو شرکت دیگر از گروه لوفت‌هانزا پروازهای تل‌آویو را لغو کردند
🔴
پس از شرکت‌های هواپیمایی اتریش و ایتالیا، دو شرکت دیگر زیرمجموعه گروه هواپیمایی لوفت‌هانزای آلمان نیز تمامی پروازهای رفت‌وبرگشت خود به تل‌آویو را تا روز سه‌شنبه لغو کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/137527" target="_blank">📅 19:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137526">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
مقاومت عراق: هیچ عملیاتی علیه اربیل و کویت انجام نداده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/137526" target="_blank">📅 19:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137525">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
حوثی های یمن دقایقی پیش یه کشتی دیگه نزدیک عربستان رو مورد هدف قرار دادن
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/137525" target="_blank">📅 19:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137524">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e37e5e25.mp4?token=UrbXwah1TACZKycEf8uSlf910Jui9HcMJ-ExtY7XQJnt94s-Qjtw6XGsO2s1roauVS7AiZnvvePIsfzG6Q9bnbX3iFM_CU7LR2ARtOdIvldG3uLYYUELgehY0KrTFblHK00Laj_4gKVyjUGWOb7BvFQ632F6BYrnHIXNUQrpvxMl39Tm5UEVjF7h2gftfvJFYDMVVU-oIS6DChVbXj9yU5IgiVmpWpddbYxkFptUBJp-x0fu81FLyQdLdj0O0DpAJe4QdJWfCoYkkhOrETAqx2TlvQQzeeXdjoMznKFdhPoRMl1b6w7k3_ZcF_Mt7dExFezD3Sd2b1vQWPoHKBV-WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e37e5e25.mp4?token=UrbXwah1TACZKycEf8uSlf910Jui9HcMJ-ExtY7XQJnt94s-Qjtw6XGsO2s1roauVS7AiZnvvePIsfzG6Q9bnbX3iFM_CU7LR2ARtOdIvldG3uLYYUELgehY0KrTFblHK00Laj_4gKVyjUGWOb7BvFQ632F6BYrnHIXNUQrpvxMl39Tm5UEVjF7h2gftfvJFYDMVVU-oIS6DChVbXj9yU5IgiVmpWpddbYxkFptUBJp-x0fu81FLyQdLdj0O0DpAJe4QdJWfCoYkkhOrETAqx2TlvQQzeeXdjoMznKFdhPoRMl1b6w7k3_ZcF_Mt7dExFezD3Sd2b1vQWPoHKBV-WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو عجیب منتشر شده توسط وزارت جنگ اوکراین از سرنگونی یک پهپاد شاهد در آسمان کی‌اف
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/137524" target="_blank">📅 19:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137523">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1gwe0D34HU7MnnO_CgLXAwHr8gS0PpjTkj1uFzw5fLZi_idrA2Br4VIYG4-t6zf_r73rERqTNEQrX_vsv_IgVRJa6JIfmYU_cfB_i6Yr0USeWAcaOE2eT8tWfJ-Le2roYYM1PmKjxFklAexB9FIi17v-Clf45iE6vUGazGx3ckL3gvgr0C1bZ3JxpY0JUDHOfAJ7AtsG-4ox0pmawkTd884mSBrrTvo8_KrbUJTIhqsnai0ZmJyc3QpOQ-rX8vaC6Gz_XwTqB_Ldyp2S9Fu7zq4SNQATblpMDfLaMnDZXzzPEtn7W4gU2wky608y6JJMrobrUKKeguOXO9DoTikXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر منتشرشده از فرودگاه اربیل نشون میده ده‌ها فروند هواپیمای نظامی آمریکا در حال فرود و برخاست هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/137523" target="_blank">📅 19:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137522">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmL8_p3D9tjPxDPfcBHhcQO488kdLixIripQsKTdCe6vQZTh0v7nSJnxqe2EOVymW7tdndxhI861MUoSJ75VWBpZiqsGpNxlfNITD9My9kKQBdoJbqrlFFjdd2pacYDEuyt31hvTG06NSGWoj5e49fHszq6ohXKCBEsPynV2lQ5UX7iXF5KCFURdgJqMMVmGN-lmYNFAsTTjDMNct5dkz6B8KNNIxhCA6KULK4wyRlvptkqxofU1tE3GpDEdLEAR4f8C37XMBbUFfcQZK1gcA3SA75nPGmG47fY9TQ1ugu1mhDJXZIH1Ext1lD1nJ7i21ftW-32mXIGjOKuhtBwf0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تروث سوشال ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/137522" target="_blank">📅 18:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137521">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
عراقچی: ما در تماس مستمر با کشورهای منطقه هستیم و توضیح می‌دهیم که هیچ دشمنی با آنها نداریم.
🔴
برخی کشورهای منطقه اکنون دریافته‌اند که حضور پایگاه‌های آمریکایی در برخی موارد به عاملی تهدیدکننده برای امنیت آنها تبدیل شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/137521" target="_blank">📅 18:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137520">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
اردستانی، عضو کمیسیون امنیت ملی:
شاید آمریکا با سرگرم کردن ما به «تنگه هرمز» و «کوه کلنگ»، یک رده از مسئولان را بار دیگر ترور کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/137520" target="_blank">📅 18:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137519">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
اکسیوس : آمریکایی‌ها دیشب برای عملیات بزرگ‌تر علیه ایران آماده نشده بودند
🔴
برنامه‌شون فقط حمله‌ای در همون حد و اندازه حمله‌های دو هفته قبل بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/137519" target="_blank">📅 18:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137518">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
سپاه: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در غرب زنجان در روز یکشنبه
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/137518" target="_blank">📅 18:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137517">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
فوری/ کانال۱۱ عبری: ترامپ، شب گذشته یک حمله بسیار گسترده در سراسر ایران را به تعویق انداخت، به این امید که بتواند به مذاکرات بازگردد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/137517" target="_blank">📅 18:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137516">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
وزارت حمل و نقل قطر: فعالیت‌های کشتیرانی برای تمامی انواع حمل و نقل دریایی و شناورها از ۲۶ جولای به طور کامل از سر گرفته می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/137516" target="_blank">📅 18:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137515">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbpA0n1z0KOnBcKPtcijIJWD-W54TiVP5eIHIFi4N_GrhXTXH3l9XS34Han56ocKHZWrKmbL6ShAD5anQoDJMozgYl8V2See2Uj1LFk6o-tiUKX9cfHLlh5yOslQaeEP7tsROnFhVfyxWSjKWLPXxTLKMF1qrsBRY2NaNbpk2YZiYunrHLOnvYHEOgnF2WlBoHSgXTxGly4guDU44ydrZaQHzEB3D0i2FpaeobIq6PGgiOt3VW09UNqQIxYIDbFd7aeudB9yDmIF6b7q2ebnT7F6LsUgD9wnaLCy97L7BucXSubcODqx-EnotKjAtzBa_InoujX_mngmecAGasVAZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبری مبنی بر " ارائه طرح جدید آتش‌بس از سوی میانجی‌ها به امریکا و ایران" در فضای مجازی درحال وایرال شدن است، بایستی اشاره کرد که این طرح و خبر جدید نیست و مربوط به هفته قبل (۲۰ جولای) است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/137515" target="_blank">📅 18:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137514">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
ادعای کانال ۱۲ اسرائیل: آماده‌باش در سطح بالا در اسرائیل برقرار است؛ آنها منتظر تصمیم ترامپ در مورد آینده رویارویی با ایران هستند
‏
🔴
شرکت‌های هواپیمایی خارجی لغو پروازهای خود به مقصد و از مبدأ اسرائیل را آغاز کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/137514" target="_blank">📅 18:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137512">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XyArOyZghggNM22YpYYRfoM12tT3ycrL3IuEmnyc-JC2m_RDg41fQLwzDyK8t-ueyUCYw22rvGG3RqnJhlqJBqB5D0qjKcsOJwTcvgNwJb937ZNh_56kNKI8Q5iYGdb6X7_CNsSo06C3LtK5LkzJKiHi9DBCqvNmBxf-9YNfFhpqxXKKWrs2G6nyyVfrzlq3aqN9CObj8qk4bVspU7T53qAuoZorHCSJ7DIQQw-j_4Tto_hqgBN5nmGnZ0-omuI4R8fLW2WyLoUqCkmVTbyGyE2lMd1QGIqWDILCBbuCTecHM3L7Hytk_JLTTNhJW34b2S6zzYYioH_HSW21RvRw_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fIkfgPkAf-Z10WAGrFNkN10RE8tre_9d3ar8cQi06GNaPz6-Wv25Hyj4bhWU-KqYIaZD7HCDczei3M_5t9JmmaI_tHjyXj6bxbkdkl7SZRUVXFr7wWm7k9wNONyXfZQj0rjmf4kSCrvH4rhwTd0SNvQk3VwfufvqBXu77RO8Lme60qMwqelD6EuQaR3xm9OSS_CJHvAf65nz506FKA8CPxn002i98_a7-nty_3rWY6gTNSD0S_x6KtIoRizmvC3zk-lmN-epdBbQZbBplXUNOZEpsF8Ebbnh6ixTsjidS-3ZAKMnaWNP8YEpSzS06wnwBLk83POLcPu6uBz89oBiFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
فردا و پس فردا هوای گرمتر از نرمال میشه و دیگه بعدش برای یه دوره طولانی کاهش محسوس دما و دمای خنک‌تر از نرمال برای اکثر نقاط کشور داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/137512" target="_blank">📅 18:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137511">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f0579d0de.mp4?token=fBM2tdy7PiglCjhTRybvo355plVprUTg-fuaz1TwHuma4qnZ3BqF2nAYYc-a2ryYL7JSTkxSrOas-LT_M-BYNzVwJ0SVLYfQR7b4i4dOGB5-G70KSS6JGnLWCoO4a23h0rha7X5OCQILlEvPuGD7l0mKliB5yiEJABAeca5enKAXxeBQBbuagfm-HCklaAXR8zA4mT9spC-3VCSCt_VLb5HCE9YKP-zLcXituu1q97gPzKBDq0czuGNWKj9ku6ZfygSEDd-LC6zy19_fKrkcN0ukDYPv9FLygwmznUAtdmk1J-hxRvKpw2b_pIMkBw4McclQJKhzLYKG07c5eVfl7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f0579d0de.mp4?token=fBM2tdy7PiglCjhTRybvo355plVprUTg-fuaz1TwHuma4qnZ3BqF2nAYYc-a2ryYL7JSTkxSrOas-LT_M-BYNzVwJ0SVLYfQR7b4i4dOGB5-G70KSS6JGnLWCoO4a23h0rha7X5OCQILlEvPuGD7l0mKliB5yiEJABAeca5enKAXxeBQBbuagfm-HCklaAXR8zA4mT9spC-3VCSCt_VLb5HCE9YKP-zLcXituu1q97gPzKBDq0czuGNWKj9ku6ZfygSEDd-LC6zy19_fKrkcN0ukDYPv9FLygwmznUAtdmk1J-hxRvKpw2b_pIMkBw4McclQJKhzLYKG07c5eVfl7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواپیمای آمریکایی اکنون در فرودگاه بین المللی جده فرود آمده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/137511" target="_blank">📅 18:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137510">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a86JoaTH_3w-6HEU3evyA_aUTuAr0jpjJ61yQvLzJWSSdsGgpk57pl7JujG0NspBzCIQ1eppfAQk1GN32ByEi7j1aHo4BXj8qvOVyVzEURjKo1XSwSP9krGSpEaxTMvQQyeEZUZJ8lcP8X50SJ4X2XJpzvLT59uCqQb4GrMGNP-guQdjF5qQU6Nsx3LkPaqxDtGd6bqg1HqaXsiGUMljsajWJTPUTmR1m-d1JKIepOISIuB_0klcg1el2xvmFuJbeth-quMCRyWGsn1m_zgE_T9dHGlLotu-_4_Mb6I_gkL4j7GMjuwyKevflxFn7aLL2nlJ73zqU9RnF8ple4Fc-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
آموزش تیراندازی با سلاح به کودکان در میدان آزادی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/137510" target="_blank">📅 18:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137509">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmoV8c4C6whWUvTwqoEuyWnGo-KGpphkDwlo4kp1b5KFXLsw8MwV_3Ic_rC-Gc5g1UFYc46g6sjKx3jzWdM7L-s5322ULcq2uzvssZObj7RMMGEd1GJE8blbScDJGdE3QKhLs1Q7DSCqipeZQIV5Mujs1naZcyK8FQJb-wY1cAfBZyA9-sLHVJKcdqk0n1pNSLNasQbAl8kloC4TrBct_SSNU0fy8LYZULgkLhFWK7s6Aq-N_-pAWByeD5EPQjEU6G_SrpPck9tzm8zi9Kv3sXrwgamKwJpnlWlnwgej-v8g7nGUVVHvTcg8hJ5rMGYGKWyVcBT4GKfhiDMJgfUqdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
لورا لومر خبرنگار نزدیک به ترامپ:
‏در اعتراضات دی ماه ایران، 100 هزار نفر کشته شدن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/137509" target="_blank">📅 18:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137508">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
حملات اسرائیل به شهرک کونین در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/137508" target="_blank">📅 17:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137507">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsxV7M49bG4jwLdMYFA3RqvFU_tt6lvAhMI5ZwcN1MDn1eritynKSVxeV3pPejyPUrNtoK1u-aCadqBIlCKN-d93oDzH8MhHUYZrFVv8v_1GVWOzjDOGxjpHka3bjcgRq1FIj2EpwHqtofHarHEjmcQcqkZJS3KapyYg6VKkIV9WYsBD8hcLooXIcdH_4BSHLh3RAdnqufZqCCA7OD7KcQ_ETlaS6FcXdqgh2f3NpuzrAU1ChmY5QEX4t3TSMA4LDOCa43Zl_FQGH-zLBMSWVMIy8-wdJ4-SD874vpgUIyRpJk8M_UmJI_osIq0AH8tvAI3Wfry8fw5FaESEkjx-lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قاسمیان، موسس
شلتر
:
اول اسرائیل رو نابود میکنیم بعد میریم سراغ عربستانی‌ها و بعد امام زمان میاد
🔴
پ.ن: عجب پوست شفافی داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/137507" target="_blank">📅 17:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137506">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل:
لغو پروازها به مقصد یا از مبدأ اسرائیل آغاز شده؛ این احتمالاً نشانه‌ای است از آنچه در راه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/137506" target="_blank">📅 17:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137505">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
شهریاری: ثابتی با فساد وارد مجلس شده و هیچ رزومه‌ای نداره و با رانت اسم خودشو جزو ۳۰تا نخبه تهران رد کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/137505" target="_blank">📅 17:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137504">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2-wMiWbQ2WHZ-_K8BWsnEW5U2-FKSj_ET_RCMSaBqze8G689YwqU1Lvc9EadsHwj26_v4e5WoSO6qO4svBe7aoCWtDbz8VsSx0GIkAfL1In2bIfXVehnveSt2FGGXQySeG1D3_nNDSelOoS2v9P3E9a6PTaHZ_Lt6R14wJvAcBfv7BfbJlihn1M6K1QFL9SHhqQVP1v6ntwEW2ZqWv_wUnZNjk3RVHtv5m-8wafBUqEKQPyQed45DVgs7UQKkimxgSIxyyYl8LZ5dxNtS8fwJvEQrvlGJVDt4DAfVRzPJxAAGbmIx7n83DfpcPQWhbERAvPwuGd3_m9as-Yj86l9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ام‌جی لاریجانی:
آقای شهید اینترنت رو به کشور آورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/137504" target="_blank">📅 17:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137503">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcFVMSl4Jw0tRW6wA9UudZIqzQNxDGw6xgFuDF3Ta3DsAK6lTrEUFWCS640x11oa6sWqxRybZViiLJbFe5HfBoj9p9PU5Xh4_yectYf7VBL50tjpkcJjxv2dPI4dZ-LVc2ZhDjJrtngBtAclpl_-EfLSwwnGdVQj4caDkP0hHUjXwzrtNc5Atj1IdsyrLADslDJK9xxRl2Qi5Dj7HrdHbXGv4nXJN0YurC-e8aOc8qHL2_owLnenyyxLTOlCOQQEcL4TRwJ_KY3hx2Y1p5Go_Z61xvVTq3zpGl298oTyE4jL_nMe_vQ9l-SI4_hOvJFcmrb8ZSuAXRCZpoPlXQTTgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکسیوس :  ایالات متحده درخواست آتش‌بس موقت با ایران را مطرح کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/137503" target="_blank">📅 17:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137502">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
نیویورک پست:
ایالات متحده در حال بررسی طرحی برای خارج کردن اورانیوم غنی‌شده از تأسیسات هسته‌ای ایران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/137502" target="_blank">📅 16:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137501">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cp2mSQlB2YgpS0IEg7i63aVLiq8mzukMKLakeKGhJrmVxwdheXDHOtAkF2BWwZBNSmBcmcxWPgxxPy7KMk5Vz9kQDfrEJEr2UBNrsAcDlhh38x0GLrTzNGONU6u7jpUGu1W6nf5aOuYj2tzW3lfWgixF-bDPH07kG0cyldnrJ0COtjk17DRdEuWl5Y_9d9P-3bcpysRi7vIsPCXPsRuS_uhlb3Xp90ITJ_Y-28yw0vAhvMXpDFTaWj9e2_6tg8Wdh-se8TUEolkd-S-gn6ruhif_Vk95kxUKV4cdX0SNHndQG1Jz0J8Zx_D1w-gHkBl2RX2og9H-UGBaB6652d10WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قدیری ابیانه: آمریکا برای حمله زمینی به ایران آماده شده و این حمله ممکنه پیش از انتخابات کنگره آمریکا و حتی در روزهای آینده انجام بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/137501" target="_blank">📅 16:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137500">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
دختر ۲۰ساله‌ای که تو خراسان اقدام به تهیه فیلم‌های جنسی ارباب و برده میکرد بازداشت شده
🔴
محتوای چنلش هم تو بات گذاشتیم و میتونید ببینید  زیر ۱۸سال
⚠️
⚠️
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/137500" target="_blank">📅 16:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137499">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
فوری/باراک راوید:
طرحی جدید میانجی‌ها به امریکا و ایران ارائه شده که شامل رفع محاصره بنادر ایران، بازگشایی تنگه هرمز و پیشنهاد دریافت «عوارض تأمین امنیت» توسط تهران از کشتی‌های عبوری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/137499" target="_blank">📅 16:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137498">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74e22034d8.mp4?token=kUzHNI47P_bUpXgB6csKwoGuIxMT0uWJpegx1jFLbzL0BYe6L3BWo06mB1eUBopXtXShnsHs1HNWw9BZrcj3A5KAqHbGwMuOf4dk0cpSRr_Q7qYTG7D4FGemR9WcCt8RSZyYqluDryzqSRp4pJ7gvSYGYxiDN_V0EhY3Ej_fyOXV-SmpS_M2b92WjK0CMDCCvyzHKn3Z-fQCzyfXBrs7iz4iP2sHQJLOVoiE6Yn_tehlJiq4qa7yPVM54K0sGwGnXJhaBSbJQ4HqyoLQmw4O1bQ2iIdKa4IkRm2kpSBGMAvetZesVjh04xDjcBwyP_ieE-5NuYbc0WPfKqCusbhulQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74e22034d8.mp4?token=kUzHNI47P_bUpXgB6csKwoGuIxMT0uWJpegx1jFLbzL0BYe6L3BWo06mB1eUBopXtXShnsHs1HNWw9BZrcj3A5KAqHbGwMuOf4dk0cpSRr_Q7qYTG7D4FGemR9WcCt8RSZyYqluDryzqSRp4pJ7gvSYGYxiDN_V0EhY3Ej_fyOXV-SmpS_M2b92WjK0CMDCCvyzHKn3Z-fQCzyfXBrs7iz4iP2sHQJLOVoiE6Yn_tehlJiq4qa7yPVM54K0sGwGnXJhaBSbJQ4HqyoLQmw4O1bQ2iIdKa4IkRm2kpSBGMAvetZesVjh04xDjcBwyP_ieE-5NuYbc0WPfKqCusbhulQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محمد یاراحمدی، دوبلور پیشکسوت سینما و تلویزیون درگذشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/137498" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137497">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
رادیو رسمی اسرائیل: ارتش در کرانه باختری دستور گسترش دامنه عملیات‌های تهاجمی خود را دریافت کرد.
🔴
ارتش اسرائیل تصمیم به استقرار ۸ گردان در لبنان، ۵ گردان در غزه و ۲۶ گردان در کرانه باختری گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/137497" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137496">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
اکسیوس:  طرحی جدید میانجی‌ها به امریکا و ایران ارائه شده که شامل رفع محاصره بنادر ایران، بازگشایی تنگه هرمز و پیشنهاد دریافت «عوارض تأمین امنیت» توسط تهران از کشتی‌های عبوری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/137496" target="_blank">📅 16:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137495">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8e4bbc306.mp4?token=kyxE82MLNSU0g9lxSi6OJRgf6TcWfBKm7mwU1vDlvxC949Hc0LWtBK47CTWW-z-9aPqtIK1GqLwW12ie8PLXnmXGwAVfAC70agfErh23aI6peAelK2tmraLOkPW6YJbBNQtleArpsB4gAgy70T1Z82CPlpAwM4Wx1wiN0hxKUyEFBFIVfhU1pRipcp2RriLkZvhcIswSTgjRAcbLMMx75Y5WhOUZkOsQ-OJYazrgwZX9OZb1QS9nJ8_W2yqG8mtNWqs6PqELZ8lwGifUUcf4sJ_7vR4SHTehF2emFxmHgqBp98CsP41FlZAE3_ECV094SbLAyGzx5-rRZLpavCoExA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8e4bbc306.mp4?token=kyxE82MLNSU0g9lxSi6OJRgf6TcWfBKm7mwU1vDlvxC949Hc0LWtBK47CTWW-z-9aPqtIK1GqLwW12ie8PLXnmXGwAVfAC70agfErh23aI6peAelK2tmraLOkPW6YJbBNQtleArpsB4gAgy70T1Z82CPlpAwM4Wx1wiN0hxKUyEFBFIVfhU1pRipcp2RriLkZvhcIswSTgjRAcbLMMx75Y5WhOUZkOsQ-OJYazrgwZX9OZb1QS9nJ8_W2yqG8mtNWqs6PqELZ8lwGifUUcf4sJ_7vR4SHTehF2emFxmHgqBp98CsP41FlZAE3_ECV094SbLAyGzx5-rRZLpavCoExA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اوکراین تصاویری را منتشر کرده که نشان می‌دهد چگونه پهپادهای روسی با شلیک از سلاح‌های سبک از داخل یک هواپیمای یاک-52 سرنگون کرده اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/137495" target="_blank">📅 16:23 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
