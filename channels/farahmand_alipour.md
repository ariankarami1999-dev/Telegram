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
<img src="https://cdn4.telesco.pe/file/cbU3eORFKmYNVSaWUlIQMdEaNUhjNftOgBwQ1h5nHZ397Szdl2nKaEWa2E3WS0-f5klnTNxrnEtX6ckcMQJ_mlvM5exD7qdh9ILCj8PgAZD8xcT3e2a4BewtfomKlz9maQQ8N5hsJ67-cOHiMZkEw_-1f12kU4f8OllskMgvBPTouWNppR1eDfpIuOG1jr3yYpSqBjySfmHIhdUOjZ5M-k08rUcUq6GHZ2UFgrbnplzhFKqyNkCbj-PEDdbAjH__6FZfCWZGoM1GW5hxcatieEb-AAHpFq6mIYMVoyZptkXZlPY3AjvTVZ-LvjSeAD4U86Unv89fLJ1N6Kf9m9nQAQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 65K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 18:13:51</div>
<hr>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
حمله ج‌ا به بحرین</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6218" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6217">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">شرکت ملی نفت کویت گزارش داد: در پی حمله جمهوری اسلامی خسارت مالی سنگین به یکی از تأسیسات نفتی‌مان رخ داده است.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6217" target="_blank">📅 15:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">آماده‌سازی اذهان برای اشغال مناطقی از ایران در صدا و سیمای جمهوری اسلامی.
«مهم اینه که گریه نکنید، بری تلاش کنی [اگه تونستی] پس بگیری.»</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6216" target="_blank">📅 14:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMDpU9RJwLRRIjiRFMe0sGJ3NrwrmFdf2PfehFhmkdXqUh-dZJS_E229LfzdyMaOgy__n2N-JtFFAEKxiJHxU07MjYQL-ujO_Om42sPD9XMZXePkqNIMnH_x1YeKoHKrYmxRoNWawoVOUQSOqfzO7JiMF5l5im618mLB3u8laqzuY4FIRiFJx36XnU-NvlIf1ylK1qUwWf3mPplnauoYo6UMMY5MW0w9QRy3yZ0cleH9azRFQvZ82H4EIsU4fhxoNf2H0l8M43rAUmmTPqhhaFYMEdqrCHRYDbIa62iV1JaZj81A9S_BT_Ab6SNGVI8lX6NxdkbSBAEtWJ2vTXGJcAZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMDpU9RJwLRRIjiRFMe0sGJ3NrwrmFdf2PfehFhmkdXqUh-dZJS_E229LfzdyMaOgy__n2N-JtFFAEKxiJHxU07MjYQL-ujO_Om42sPD9XMZXePkqNIMnH_x1YeKoHKrYmxRoNWawoVOUQSOqfzO7JiMF5l5im618mLB3u8laqzuY4FIRiFJx36XnU-NvlIf1ylK1qUwWf3mPplnauoYo6UMMY5MW0w9QRy3yZ0cleH9azRFQvZ82H4EIsU4fhxoNf2H0l8M43rAUmmTPqhhaFYMEdqrCHRYDbIa62iV1JaZj81A9S_BT_Ab6SNGVI8lX6NxdkbSBAEtWJ2vTXGJcAZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرهای جمهوری اسلامی
و کودکانی که تقاضای «سر» دارند!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6215" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=SA-ntt700ZS27ZCnM1PiNsSePDF1axiFbA03JQFfuaOFqWbyyduRyJTtvqya6-H_Z2K7Oamjar4eZklB1QYQc1pvzsTYdRRn02OXfu8lGftKP99uxl26qkvGdX4ytjBpPklrMa3iy070vdyymHFQ2XG2_bGxhp2uSOXrdJmxMh-eLRD79ygeqrL4Me-9IXcWlaflbsFKgCxCKD_I1lBAnngVC616ufdZKt10cqluQBVDfTuzWhIyqV6Y1CMcy8rTJ4QmwlXFeD8GzdMs9LqfboKXAGxYXkORzO84M8JnySM7m_xJ_lyOTyfWJNVUd_pdyAOVagjTyOKiLqEBtsRlfnTUMe4EHaZZg0CqEXQQfyLuCO5IBoC4m4wdRp6uvEe-1-NbXyXAEWB9YIr45kM2ghDUvDRsYoeVom8_QfmwwnVsNdWRAB2lDx06huN7TkB_fhs7ajraVrqpKbat8Ii8SFryd6scxlZ9IT3mxPvGERisSB4OBx_sMey9D-STkndV1oetOIxpvdEWcj_R6a16uT4rHf31HvNV1_Lx0mpk23laoPUho1MIy7AxkokUxN_dJ4BOB3BWkNPOcCQH7m-d5JB4h0_RqzT-BExyeWPDqFH6Tp45ZI_nA_xTLUvRCw2kZ6ErDvT4e87g1ilxRoGxbkkEXelBAR07n0ynm7z5d4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=SA-ntt700ZS27ZCnM1PiNsSePDF1axiFbA03JQFfuaOFqWbyyduRyJTtvqya6-H_Z2K7Oamjar4eZklB1QYQc1pvzsTYdRRn02OXfu8lGftKP99uxl26qkvGdX4ytjBpPklrMa3iy070vdyymHFQ2XG2_bGxhp2uSOXrdJmxMh-eLRD79ygeqrL4Me-9IXcWlaflbsFKgCxCKD_I1lBAnngVC616ufdZKt10cqluQBVDfTuzWhIyqV6Y1CMcy8rTJ4QmwlXFeD8GzdMs9LqfboKXAGxYXkORzO84M8JnySM7m_xJ_lyOTyfWJNVUd_pdyAOVagjTyOKiLqEBtsRlfnTUMe4EHaZZg0CqEXQQfyLuCO5IBoC4m4wdRp6uvEe-1-NbXyXAEWB9YIr45kM2ghDUvDRsYoeVom8_QfmwwnVsNdWRAB2lDx06huN7TkB_fhs7ajraVrqpKbat8Ii8SFryd6scxlZ9IT3mxPvGERisSB4OBx_sMey9D-STkndV1oetOIxpvdEWcj_R6a16uT4rHf31HvNV1_Lx0mpk23laoPUho1MIy7AxkokUxN_dJ4BOB3BWkNPOcCQH7m-d5JB4h0_RqzT-BExyeWPDqFH6Tp45ZI_nA_xTLUvRCw2kZ6ErDvT4e87g1ilxRoGxbkkEXelBAR07n0ynm7z5d4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرنوشت ۹۰ میلیون ایرانی افتاده دست این جماعت  متوهم</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6214" target="_blank">📅 13:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!
در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.
این بار اما آمریکا از عنوان عملیات هم پرهیز کرده و به نوعی داره با سر و صدای کمتر، این جنگ رو پیش می‌بره.
رسانه‌های بزرگ آمریکایی هم  گرچه اخبار این «حملات» ۷ روز اخیر رو پوشش میدن، اما نه با شدت و هیجانی که اخبار جنگ ۴۰ روزه رو پوشش میدادن.
شخص ترامپ هم از  هر ساعت توییت زدن و تهدیدهای درشت، فاصله گرفته.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6213" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fztRn2exidVShVS38-afA4hxkjC4LotutVqLbGDBvFUvD-29nZBP9JFyCL7UCGcECfGprImzN33WwgCoIPaSW2FuWVHFTWO2fKfDxp9AVxzBIzCt500bsZJTSCHWpOZGfxkCGA0ik7Jwq6bibYBtJX2872sSZ-qaWjTfiEts0Mrx1c8KG4JWUTrF7uuHiuQJKCz0DKYc2o9vRNnFAir2jPixfsvHsoZ2N8574OPlUdxL1cYWz-NNBQrElRsrczAoImUHWhG1c0Aj9WSDexb8ANzEOrVbmXwEnKgwwH6mhXcSmGjO5uIv_xJbfqaoxZ_6VWVsl5a-JveZLMFsYCaGOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه : در حمله به اردن حداقل ۲ جنگنده و ۳ هواگرد آمریکایی را منهدم کردیم!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6212" target="_blank">📅 12:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یه مرد هندی دیده یه تیکه یخ توی فریزش شبیه فرم مجسمه «شیوا» شده، یکی از خدایان هندی! رفته به همسایه‌ها گفته، ملت هم اومدن دعا و نیایش و اینکه این یک نشانه است و بردن غذاهای نذری و…..  :)
شیر، شیرینی، غذا، میوه و..
صبح یخچال پر میشد، شب خالی میشد!
و مرد هندی میگفت، شیوا، نذری‌ها رو پذیرفته.
در عوض مرد هر روز چاق‌تر میشد
این داستان‌ها براتون آشنا نیست؟</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6211" target="_blank">📅 11:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">💔</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6210" target="_blank">📅 10:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f27e890899.mp4?token=XuUOyura1PqFICYpN--FoDRvfugu2kZEVs2wn6ENQM2A_6TI2ExhizW7T2CiUht3FwzNzB82imwOhFOZUHd-55Jgbb5a6SMeV_PZUyMd2p55j1Px8FmxT_miJfNfetEJcvW6h7YpwMYuZ8Ia-czCSjQWZHSQ7OrjQIJ4U-ecQwCl-YTabn5IAusER03XdhzQQi6oryj0eY129E0IjLjDX5IT4pK1F4n85LTpcNSNEuauyLstLZVpo8AAHrvpTPYsynfFl7nIuCxH7FrjKHXTnj-uCceCIjzAMhkLSZ10JeKfnn_hRfJ0I2EKFQApnCwPe0osm-5aQNayy31ysY1eSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f27e890899.mp4?token=XuUOyura1PqFICYpN--FoDRvfugu2kZEVs2wn6ENQM2A_6TI2ExhizW7T2CiUht3FwzNzB82imwOhFOZUHd-55Jgbb5a6SMeV_PZUyMd2p55j1Px8FmxT_miJfNfetEJcvW6h7YpwMYuZ8Ia-czCSjQWZHSQ7OrjQIJ4U-ecQwCl-YTabn5IAusER03XdhzQQi6oryj0eY129E0IjLjDX5IT4pK1F4n85LTpcNSNEuauyLstLZVpo8AAHrvpTPYsynfFl7nIuCxH7FrjKHXTnj-uCceCIjzAMhkLSZ10JeKfnn_hRfJ0I2EKFQApnCwPe0osm-5aQNayy31ysY1eSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از پل‌های غرب استان هرمزگان</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6209" target="_blank">📅 10:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6208">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!  این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6208" target="_blank">📅 10:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6206">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان می‌گوید که چند موشک به تاسیسات برق و پمپ‌های آب‌شیرین‌کن مستقر در اسکله روستای بونجی در جاسک اصابت کرده است.
گقته می‌شود که این آبشیرین‌کن، آب حدود ۲۰ روستا را تامین می‌کرد.
🔺
شب گذشته کویت نیز اعلام کرد که جمهوری اسلامی همچون پریشب، به یکی از تاسیسات آب شیرین کن این کشور حمله کرده.
🔺
ارتش اردن اعلام کرده است که سامانه‌های پدافند هوایی آن کشور ۱۰ موشک ایرانی را که وارد حریم هوایی اردن شده و خاکش را هدف گرفته بودند، رهگیری و سرنگون کرده‌اند.
🔺
ارتش جمهوری اسلامی نیز با صدور بیانیه‌ای از حمله به پایگاه آمریکا و چند پل در بحرین خبر داده است.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6206" target="_blank">📅 09:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6205">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
وزارت آموزش و پرورش:
🔺
با توجه به استمرار شرایط ناپایدار در جنوب کشور، آزمون های نهایی تمامی رشته های تحصیلی پایه یازدهم و  دوازدهم در روزهای یکشنبه و دوشنبه،  ۲۸ و ۲۹ تیر ۱۴۰۵ صرفاً در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می گردد.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6205" target="_blank">📅 09:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6204">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=EQDqqUnmmainNW4tviUqMqoTQmCtCnAcytNt7YAFLSWRrA1ORHLYBc1GNW9hBgsIyYLMTR5IBxu6PXQciTqnEBnx147Lce8ij6qdUPeM9sOWsPJO-p4bYpFIRZDirBGhlXUVwU5CuxNkLWPVcaPFCB46Bc4evjZtNBH-OLdEk_nm_MxYANz3pkxKur017LU_7r8Lv3vIuS3tGrg0sLGq2zfrqQFh1FLI7LQ1p1nEeRSTYyjGMGatLTIhjn-05X7a9XC4vQGszGAzH6Q8R09tuFBnT5BWVY8TBvVRaHitBP6Py9AkDQ3lbek3qXjPuCTR7jwKl6vovs6XVlzNEI2rYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=EQDqqUnmmainNW4tviUqMqoTQmCtCnAcytNt7YAFLSWRrA1ORHLYBc1GNW9hBgsIyYLMTR5IBxu6PXQciTqnEBnx147Lce8ij6qdUPeM9sOWsPJO-p4bYpFIRZDirBGhlXUVwU5CuxNkLWPVcaPFCB46Bc4evjZtNBH-OLdEk_nm_MxYANz3pkxKur017LU_7r8Lv3vIuS3tGrg0sLGq2zfrqQFh1FLI7LQ1p1nEeRSTYyjGMGatLTIhjn-05X7a9XC4vQGszGAzH6Q8R09tuFBnT5BWVY8TBvVRaHitBP6Py9AkDQ3lbek3qXjPuCTR7jwKl6vovs6XVlzNEI2rYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مسیر ترانزیتی بندرعباس - سیرجان که در ادامه این مسیر به تهران وصل میشه.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6204" target="_blank">📅 09:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7U6VgsmWc6M0-vWa9P2SnAMmQ9Gp16g3XE_5UurUNL4IlTlKSRx-pA0V2WLJXDvF1OQQbYl0Fv6lL6vOjD_knC2Qm8xTG7d4EK2qW9viZqtLaUEsk-a3hRKaHsOoGZaiNt-sq2QeEwGRYlUGzG2JVLb9e_0ITB_ZUsBUDyfcOujpvBUAeOAwDAXKbaN-_0Khaqt-tzTRyevu3MxYUL79MaOA3o5d5tJGRGpeg5vSv_T1tZW2EYVVpUTpWzPcMtVrZqMIlODJNbm4A0EBvxRHor3Xrbhn4wpJnO6EARVCApNvIoR3cn0NDKeNBRQtHx-iRTESFnpMVSQBxVvTtBmuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه سپاه که میگه شب گذشته ۴ کشتی با کمک ارتش آمریکا قصد عبور از تنگه هرمز داشتند که سپاه بهشون حمله کرده و متوقفشون کرده.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6203" target="_blank">📅 09:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwIKd6DytcskgrREZ8hwA8c0pD0sZgM_-vgLSFSuppsLWvo4lKHUdnYamvU6KTJ0ZIwie4YA-P8WvlGHSSsdL1Tqj1EqYmTBJtXSZZJjRFO3ivP5mNbMPqYPVtPXuQk9OJ3aio7IybF7LKje0fKB21QUwTvctk4viQjjQTVEGzMXgeQYKOZ-JI-ojiPVYjQYGeBhs_G-zPRglqIgT0eNEBsIyy61lsLPDIe3zNaTwlZG02u33BI7OSk33P83sDXz49KXOUPsyBV0Igb4hJ2yXW5ne1QUNBSUjH4NSib_WEtNlf3eOJo1lKyP202mi84jZO9uilhtDq90cEmta9cboA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا شب گذشته با موشک
به دکل مرکز کنترل ترافیک دریایی جزیره لارک، واقع در میانه تنگه هرمز حمله کرد.
این مرکز برای ایران یکی از مهم‌ترین مراکز دیدبانی و کنترل عبور و مرور کشتی‌ها در تنگه هرمز بود،که اکنون کنترل تنگه را برای ج‌ا سخت‌تر می‌کند.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6202" target="_blank">📅 09:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6201">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!
این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.
🔺
ارتش آمریکا همچنین دیشب به چند پل دیگر در شمال بندرعباس حمله کرد تا ارتباط زمینی بندرعباس با بقیه مناطق کشور دچار اختلال شدید بشه.
🔺
بین ۸۵ تا ۹۰٪ واردات کانتینری کشور از بندرعباس (بندر رجایی) صورت میگیره. ماشین‌آلات، قطعات خوردو، تجهیزات الکترونیکی (لپ تاپ، گوشی و…) مواد شیمیایی، مواد و تجهیزات بیمارستانی و… همه از این بندر وارد ایران میشه.
🚨
کالاهایی چون گندم و روغن، برنج ، ذرت و…عمدتا از بندر خمینی (شاهپور) وارد می‌شوند.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6201" target="_blank">📅 09:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6200">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=XvbzOqCHC6WprXv2z7mdMkC-4iWEHIkbpZYqa3PVxCjR459d3FR2VYqZx93Oux4K-tAVg_pjtdcreqeEfXlF99UsDcJkfWLwJf8LNe1uuBFZB-jv6oJSegjPTNugft3XVuubVuTykDpyZb-lGSVIjrsCd4gzv2h7BvnqU1Llrq6jdqYh2tMQjgYryMP_CUkZcVxJh6pnbRjehtC4zRkuIZzajjKh7DN7OYGYzAnfS2DjFoxI1cl7oeEQweqE_33qj_os53X5njkrodDZYAUidogCtyi9WAST-5Sw_tcTVKO-6zmiLmbbG_34375LHHoEruunshCKDoxV_JPmK764WCP6wsZOSsW-gnGjMdTuyV3-Z9aoyyuc0OV3Zi-7hGQxldeJj2MIklCUxjnDxGGUQ4BP071Am6HviihHg6sVc_5iJ8ceL6PzF2WyY1kmvg3UngFBeMsgvqX41LF6RR6OSnVvzy6Gol3b-IaYqDvt48MlqRK4A3p6LsahP_z05zhUUE377f2B4W5mYdJCYMimxsMjMV2FDW4zXap3me9PlZJhWltiEkNYY6b22kno8x0Ap32hsBDDqOdERnr_PmFPEkcK9iqilKNgDsZNGvSBT75MGPvrmbjqbovD7rBOHH8L_jc3DB5HKQ25XSMBT8WojH2aeazv3q_FCBJ3BIhw-eY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=XvbzOqCHC6WprXv2z7mdMkC-4iWEHIkbpZYqa3PVxCjR459d3FR2VYqZx93Oux4K-tAVg_pjtdcreqeEfXlF99UsDcJkfWLwJf8LNe1uuBFZB-jv6oJSegjPTNugft3XVuubVuTykDpyZb-lGSVIjrsCd4gzv2h7BvnqU1Llrq6jdqYh2tMQjgYryMP_CUkZcVxJh6pnbRjehtC4zRkuIZzajjKh7DN7OYGYzAnfS2DjFoxI1cl7oeEQweqE_33qj_os53X5njkrodDZYAUidogCtyi9WAST-5Sw_tcTVKO-6zmiLmbbG_34375LHHoEruunshCKDoxV_JPmK764WCP6wsZOSsW-gnGjMdTuyV3-Z9aoyyuc0OV3Zi-7hGQxldeJj2MIklCUxjnDxGGUQ4BP071Am6HviihHg6sVc_5iJ8ceL6PzF2WyY1kmvg3UngFBeMsgvqX41LF6RR6OSnVvzy6Gol3b-IaYqDvt48MlqRK4A3p6LsahP_z05zhUUE377f2B4W5mYdJCYMimxsMjMV2FDW4zXap3me9PlZJhWltiEkNYY6b22kno8x0Ap32hsBDDqOdERnr_PmFPEkcK9iqilKNgDsZNGvSBT75MGPvrmbjqbovD7rBOHH8L_jc3DB5HKQ25XSMBT8WojH2aeazv3q_FCBJ3BIhw-eY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب گروه موسیقی پاپ «BTS» کره جنوبی در پاریس کنسرت ۸۰ هزار نفره برگزار کرده !  شخص رئیس جمهور و همسرش هم مشارکت کردن.
راه کره شمالی : موشک، جنگ، مقاومت ، تحریم، فقر، گرسنگی
راه کره جنوبی: احترام در جهان، تولید بهترین کالاها ، رفاه مردمش.
مردم کره یک ملت هستند، با یک تاریخ و فرهنگ و زبان مشترک،
اما در دو حکومت متفاوت!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6200" target="_blank">📅 09:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6198">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5132059c16.mp4?token=FRJB6a2DWt6nOid-BClhhjow_-KrFCMvrZ8ntDleTUI4kPj5xLmah5CK-XhLIDEEjcJQV0MFH5kOqkRisK2BV0HG3adSVr9MN6qkGIIbTuDO0C9uGBMTUJphzoJec8_wWJ3DbjWmteOhTnv_ltUA7ZIEZENaeWRU3i2PtgLPH1nESxKceg_tl0D-e_XDG1LqJhkbwRDkABJ2YlWhCl0blYcmE_gxnyt_dCsIkULSZF3knbr1ptjS2yS4ftSznN-AgVy72UYNTeANy_WkcrciErfDabJUsEtsz34umBU3w3tcSHxQPP6gk_MUAamA7qBZ3lhDt0DPnFJ1NfjlMjWE3WBUrDGCS3hAXLA0sNFqOqHbgm47Gp9fpmOVHN-9WofqPIMPi3k_HsHmCEX_am_ipYOlW1egvF6kGtUxn107Q3pQV7xhxwde6SIMJMa8pq_ZNTDxltSS3YYIL9_WFcSX4tE7ur6-OXbsY4DpKhoaP5lY9dy_ZXo5DJFLUQDTtWGLOOnahLteGMUKlIC7oFKIsGfUH8Pa6SvDf4VlLUaY4O0ykaoNYz8_vH1IlFN2DIiNtapZli-bqlBGVt2JB6qdanbHV6ytIf277AB0VpcHsLLUJgGd6q2e0H637Vg0XuUo2AXzUgdsm3g6V0aE1sjrXzncNO2ZLHEcPqpX49vL4to" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5132059c16.mp4?token=FRJB6a2DWt6nOid-BClhhjow_-KrFCMvrZ8ntDleTUI4kPj5xLmah5CK-XhLIDEEjcJQV0MFH5kOqkRisK2BV0HG3adSVr9MN6qkGIIbTuDO0C9uGBMTUJphzoJec8_wWJ3DbjWmteOhTnv_ltUA7ZIEZENaeWRU3i2PtgLPH1nESxKceg_tl0D-e_XDG1LqJhkbwRDkABJ2YlWhCl0blYcmE_gxnyt_dCsIkULSZF3knbr1ptjS2yS4ftSznN-AgVy72UYNTeANy_WkcrciErfDabJUsEtsz34umBU3w3tcSHxQPP6gk_MUAamA7qBZ3lhDt0DPnFJ1NfjlMjWE3WBUrDGCS3hAXLA0sNFqOqHbgm47Gp9fpmOVHN-9WofqPIMPi3k_HsHmCEX_am_ipYOlW1egvF6kGtUxn107Q3pQV7xhxwde6SIMJMa8pq_ZNTDxltSS3YYIL9_WFcSX4tE7ur6-OXbsY4DpKhoaP5lY9dy_ZXo5DJFLUQDTtWGLOOnahLteGMUKlIC7oFKIsGfUH8Pa6SvDf4VlLUaY4O0ykaoNYz8_vH1IlFN2DIiNtapZli-bqlBGVt2JB6qdanbHV6ytIf277AB0VpcHsLLUJgGd6q2e0H637Vg0XuUo2AXzUgdsm3g6V0aE1sjrXzncNO2ZLHEcPqpX49vL4to" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا قبل از جمهوری اسلامی
ایران همین جغرافیا رو داشت، همین تمدن همین مردم و همین نسبت جمعیتی،
اسرائیل باهاش دوست بود و آمریکا پیشرفته ترین  سلاح‌ها و تکنولوژی
رو بهش میداد و اسرائیل برای کشاورزی
و آبیاری به ایران کمک می‌کرد.
شما اومدید شعار محو دادید و پول و سلاح ریختید توی لبنان و فلسطین و…….
🔺
همون روز ۲۲ بهمن به دفتر اسرائیل در تهران حمله کردید !
🔺
اردیبهشت ۵۸ رابطه با مصر رو به خاطر فلسطین قطع کردید!
🔺
دو ماه بعدش روز قدس رو راه انداختید!
اینها کم آوردن ، میخوان مردم رو فریب بدن و بگن «مسئله ایرانه و تاریخ و تمدنشه»!
نه خیر! مشکل جمهوری اسلامیه</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6198" target="_blank">📅 08:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6197">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔺
سپاه : به انبار دپوی قایق‌های بدون سرنشین آمریکا در بحرین حمله کردیم.
🔺
حملات ج‌ا به کردستان عراق</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6197" target="_blank">📅 01:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6196">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
وقوع ۵ انفجار در یزد
برخی گزارش‌ها می‌گویند که حملات در پارک کوهستان یزد بوده (منطقه سایت موشکی)
🚨
گزارش ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6196" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6195">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=d6t47YdvP10R0v1fENWJP8R_yxhOelrWasMtcDXyZV1mv6Ut1kpgOkNJQ6Xs_zN-ab5QRzrQT6NGwQsjZvUlXDC7_-Mi5ziWrWr0FnQjXgHgEVTcB-lMm57t95mwSnBx21TzTl1nFZH2QSXl4l5coGysvVgIUy5nH01U54kLls3YsbBphbJTFlm9JAXU8LpQTnzKSbWHGbmyTNXksvPLc3R0mq3_PONM3YPkpr6Ov-kriN1ZG5BYi9j6eoJ-mg18xAhoWwsE0YLQoDB7tiEmAdX495jvFjmIreqx4ZX5VPRa77o5PGPkiGMv6KA4CZYAjn-AM2NVYWbfz3xpqiyb6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=d6t47YdvP10R0v1fENWJP8R_yxhOelrWasMtcDXyZV1mv6Ut1kpgOkNJQ6Xs_zN-ab5QRzrQT6NGwQsjZvUlXDC7_-Mi5ziWrWr0FnQjXgHgEVTcB-lMm57t95mwSnBx21TzTl1nFZH2QSXl4l5coGysvVgIUy5nH01U54kLls3YsbBphbJTFlm9JAXU8LpQTnzKSbWHGbmyTNXksvPLc3R0mq3_PONM3YPkpr6Ov-kriN1ZG5BYi9j6eoJ-mg18xAhoWwsE0YLQoDB7tiEmAdX495jvFjmIreqx4ZX5VPRa77o5PGPkiGMv6KA4CZYAjn-AM2NVYWbfz3xpqiyb6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گزارش چندین انفجار در لار
برخی گزارش‌ها از حمله به سایت موشکی لار خبر می‌دهند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6195" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6194">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCjDx_NuRVFEa6ssaJXOeHV-WvSqYJcK-aA1H7RmKdQEHlC-by0mB-80DliOToPJuo1akr58vgDzJPq5fXmWH1EFPzJ1Q_82aKRj0tH-cYWN32yABuOlnnxUy1XbKYklcsV5oAiOJRdojlgguK1uFSEbYzo3sEpK5r-waOpjTcwrGSJSwle_RUCFghHflOQDsoqWwJceReoFjv6yDCI5CvIJMwvoDPLPLSxi8bKTDKO9Bq2oKU8iogwqe9Ff17kgnxtmgKFcTjUeUybCcbiXAycTWCgj0g5S6z_F6fx9PGMEX9Nyu4kQKNB-uZ1oBdsGzpjmqJLi7cWi2L8JKOWRtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش حملات ارتش آمریکا به بندرعباس، قشم، سیریک، بوشهر و اهواز</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6194" target="_blank">📅 23:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6193">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
سنتکام: ‏امروز ساعت ۳ بعدازظهر به‌وقت منطقه زمانی شرقی،
[۲۲:۳۰ به وقت ایران - یک ساعت پیش] برای هفتمین شب متوالی، یک دور حملات علیه ایران انجام دادیم.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6193" target="_blank">📅 23:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6192">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029791358c.mp4?token=Tlh-1jWOoJY6uIcxeTz3X0J5hVHy2Cp9O6Aeh0faq2RWeI1G3ucIs1J9yrOtxHZvvoXPsh2chafpU3THCB01zaw4D0ksNPHp1PUE3XPXD5P6x8N8UCH0TO9oUbKFK5KmqOI3PWIxoWFkPdFeBWzfWRF18WpI9pLYqD9WhBuBsmrwZjJmUIFXsnJHmw7jru7HEPcutLopZx9euCTrebycRk4HkFCfjup6JgKCFH7sCigwtOMLz-rutn3GU6FXpjivAYN0nXEH49oNTvkJ6vB86th1i0PKsc_vG9dL6F7GGPMVLau8MWtnS1d6JKIm_DdGFpTbLIZ-UBNNAia-17khOaiqCKk47i-gMx9g8QKT7FB8GROtl0thkYETi3btjkh6v1nVqTuT7wNmwmYxll_axmO-6Pjmf9ybKwHbKFuoIWR2uvf-T8hbLZJ65XyM7vBwurIVYOSBD6O9HPXpidyyQjcYc8ra9AGOdHfYWYTMIh7GNhjFK8wj6l4zDyTtK9TANyeKL3m33ytLlgnDCyoh8dzuhFSl30lFfA7fqq-_0frw3o_-pRSlRN9MeqDm8PLJZyB1QEknISTGOz0KkQBkvAI_4mvp3JVbnhNe8jk3--Bbga1REulcQ3jDVXxRoUOWuEQB7xPvbL_l4syr6VdVu4me2_dnREMfvhYSO_Uz_Fo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029791358c.mp4?token=Tlh-1jWOoJY6uIcxeTz3X0J5hVHy2Cp9O6Aeh0faq2RWeI1G3ucIs1J9yrOtxHZvvoXPsh2chafpU3THCB01zaw4D0ksNPHp1PUE3XPXD5P6x8N8UCH0TO9oUbKFK5KmqOI3PWIxoWFkPdFeBWzfWRF18WpI9pLYqD9WhBuBsmrwZjJmUIFXsnJHmw7jru7HEPcutLopZx9euCTrebycRk4HkFCfjup6JgKCFH7sCigwtOMLz-rutn3GU6FXpjivAYN0nXEH49oNTvkJ6vB86th1i0PKsc_vG9dL6F7GGPMVLau8MWtnS1d6JKIm_DdGFpTbLIZ-UBNNAia-17khOaiqCKk47i-gMx9g8QKT7FB8GROtl0thkYETi3btjkh6v1nVqTuT7wNmwmYxll_axmO-6Pjmf9ybKwHbKFuoIWR2uvf-T8hbLZJ65XyM7vBwurIVYOSBD6O9HPXpidyyQjcYc8ra9AGOdHfYWYTMIh7GNhjFK8wj6l4zDyTtK9TANyeKL3m33ytLlgnDCyoh8dzuhFSl30lFfA7fqq-_0frw3o_-pRSlRN9MeqDm8PLJZyB1QEknISTGOz0KkQBkvAI_4mvp3JVbnhNe8jk3--Bbga1REulcQ3jDVXxRoUOWuEQB7xPvbL_l4syr6VdVu4me2_dnREMfvhYSO_Uz_Fo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت شانه خاکی موقت کنار پل بندرعباس</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6192" target="_blank">📅 23:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6191">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏یک گزارش محرمانه که برای رئیس جمهور ایران تهیه شده است، نشان می‌دهد که تنها ۹٪ از ایرانیان از وضع موجود حمایت می‌کنند و تقریباً سه چهارم آنها یا اصلاحات ساختاری عمیق یا جایگزینی کامل نظام سیاسی را ترجیح می‌دهند - فاکس نیوز</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6191" target="_blank">📅 22:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6190">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:  ترامپ به ما نامه‌ای داده و صراحتاً نوشته است: «بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6190" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6189">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a688590cec.mp4?token=Im5i5p-hyNq2xM9wxf9pYIbgHK5TFyzBN5ybBHHqCCJJqyirg1hhB5Kf9kXsnVYRFr-nJUjLekgamv8MxR2KwhXbvw7GbIEwZvDszF9QJgjw8tBAByJytpcxOP-y0ozXSwEnNFEUdEzD2a7VbxWVXAKSjI1618mfvhPD45TZj3HRfDGfXQzb5iv5WMnjworbVeAxWLeFdb8mRAC7524zLixuRwXo40-u-Mx-TH7G4n7dpuUgbNsrJz9eV8paLB67Xp4cjzx4vLoB9oSbAksZj5ygMq5nS9xB_ojfL8tABn2KuWY1ZMdwhdv6Cp-2semY-63QSHJQ-lgUzCsXhAwq9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a688590cec.mp4?token=Im5i5p-hyNq2xM9wxf9pYIbgHK5TFyzBN5ybBHHqCCJJqyirg1hhB5Kf9kXsnVYRFr-nJUjLekgamv8MxR2KwhXbvw7GbIEwZvDszF9QJgjw8tBAByJytpcxOP-y0ozXSwEnNFEUdEzD2a7VbxWVXAKSjI1618mfvhPD45TZj3HRfDGfXQzb5iv5WMnjworbVeAxWLeFdb8mRAC7524zLixuRwXo40-u-Mx-TH7G4n7dpuUgbNsrJz9eV8paLB67Xp4cjzx4vLoB9oSbAksZj5ygMq5nS9xB_ojfL8tABn2KuWY1ZMdwhdv6Cp-2semY-63QSHJQ-lgUzCsXhAwq9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:
ترامپ به ما نامه‌ای داده و صراحتاً نوشته است:
«بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6189" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8xGVrTe_9_Cxjc_VEYIjSYphnPbiXtkDbjiiO-HnaDTLjqiFv7pRfmQAygDv_M-rRNmScqxqg-ezUn6X83GIExDcAecEWis418z2UnvCYuFDXEtdzFeXp7TB5_0atg-QONRcsKooVuFERrid5H5ffJQLb-UNYNRY0XmfW64C0Hvgagq9nySSNKKvMubZ86V57nZpXkdGjNE9Nji1UPqHrIQ6NzYheOTHxqaC__4TfV6yEoViX9rK4J8s49tdXAn7ruv94v5n9qy5UtYDkNAreYVdQ1HHFzIkT07FfG9cB7PkEwaqdPGxh_9g1fl2Mk25keSlmnHCOITY2g1psbj2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ایستگاه مترو در تهران با مجسمه مریم و عیسی درست کردن (که عجیب هم نیست،
نصف قرآن داستان‌های مریم و عیسی
و قوم یهوده) و پروپاگاندایی راه انداختن
که ما چقدر احترام میگذاریم به بقیه مذاهب.
بعد همزمان کلیساها رو مصادره میکنن
و صدها نفر به جرم مسیحی بودن
توی زندانهای ج‌ا هستن و اجازه داشتن
یک مسجد به سنی‌ها رو هم نمیدن!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6188" target="_blank">📅 18:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6187">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJnHZOjCQwv5SRdZVYajwXIME5tmc7FfXt0x5h0Vw4sYb3aEGc-583nXXhWSFESCCNtsRR4qYhx9PSaMyousfF34OBJL3fm7r6dudC6sqWgtX2ryoXi7dZQPkIEmADVzkm_ZQvxiUxGuBxOSA6yqqrErh_Mp3mHjQf-sxIyMJGSthKQQ2yMx9jFiUjclv4WhAQr1Z7gP9C1L2_T_Ivd9Y4V0R-EJCOcCPkNtKPtbWLKXDZP2vAfGSI716GM9Snv4ORlBVB-x0sUrkG4Y9lNdCdHoPmhWVXzd3g4a6SfCG7yp7eK-qq1tCsHTSpGW7bsnnzpp4xM6x6_Jee3iZLZKwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب طلاقش بده :)
چرا اینهمه کینه؟</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6187" target="_blank">📅 18:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHyJe3YcOogfxW6-p0sEEL2I7z5mlVATINPQjEXatvB_dIq1SYC9wLGZDQyJrzD4V1Bb7dUFf_lsVhGHEiP46575e-oip_R1ceTbxnKr6fxMkZaJyhUI98RF4zYtmxl6YMhmSyDz4TXgCceu4hOE81tBMrZSxM2gvxF55LVqdGNPpFm3Yt3NLJ32s9YbbPumOUWuq6fE7iGf6TDnaOq2Wqc_CFVYhUoBKm7-E3UA3vpL_dJCaP3p25191_DeYBdt5HbqwDJ2OA7w2_CmsZB8NR96Uj-sKhPjZriyBfQnj1sRzddOIdieASHW5Gpny9VFCEO2tn3FRf02Y2K0iQaYHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل عرزشی !
من میگم اینها شکست‌های تاریخ
رو پیدا میکنن و به عنوان الگوی خودشون معرفی می‌کنید باور نمیکنید :)
تنگه احد! که نماد بزرگ‌ترین شکست و عقب نشینی مسلمانان در تاریخ صدر اسلامه،
رو شباهت سازی میکنن با تنگه هرمز
‌‌میگن همونطور که اونو در سیطره داشتیم
اینو در سیطره خواهیم داشت.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6186" target="_blank">📅 17:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6185">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7Jo5zxWZPRLa3zQ_Dd2oYybNAXqV8c7A4JJi6cy6bfYaya14imNqDee1g0QYdwUzS4CyZzajEXzLHtAatSHhCNfSkBQLTkbO_Afv5bD0tao4kxCKzs3MQv00adJL4iaodAWUcvmaiK5nNwyyzx8NEUc418tBDZtQpDbaGctjZTSwv3JAALHj3gXNoeym5z22oktwixVICSOIiECK-t2Zarfkz1Os67ZuIvNrweSgTfMObhvVa0vjjDkZRyBrT4EPklK7lRqep_qsAoQIXY05g-bhLe-bWptSeQmMYC-_jsAvtROa9jYlIbeGwtpL3stl_Pvv3a3JmGgykxWXjHeg90Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7Jo5zxWZPRLa3zQ_Dd2oYybNAXqV8c7A4JJi6cy6bfYaya14imNqDee1g0QYdwUzS4CyZzajEXzLHtAatSHhCNfSkBQLTkbO_Afv5bD0tao4kxCKzs3MQv00adJL4iaodAWUcvmaiK5nNwyyzx8NEUc418tBDZtQpDbaGctjZTSwv3JAALHj3gXNoeym5z22oktwixVICSOIiECK-t2Zarfkz1Os67ZuIvNrweSgTfMObhvVa0vjjDkZRyBrT4EPklK7lRqep_qsAoQIXY05g-bhLe-bWptSeQmMYC-_jsAvtROa9jYlIbeGwtpL3stl_Pvv3a3JmGgykxWXjHeg90Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیا بودن شعار به زبان عربی میدادن؟
چی میگفتن؟ میگفتن  سرباز ایران و وطن هستیم؟
نه میگفتن «سرباز دین و عقیده» شون هستن!
و کنار لبنان هستن! و مسیرشون همیشه مقاومته!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6185" target="_blank">📅 15:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pi2Wt9gKve-N5CSr24PouBAmcIdSNreH19XSsc8iL_cvNg0l07TnVUZdfQbc2dYsb8cyweTxucAWziPvL_W45bkthEkkeqsrPR0pWkT-7F2x5pPEt2IFqtZP5SOnZTCABxNwr1KlwxL_sErkLc2ndj4BB-8HtVBym-rXWLqRAxscjjLb1VJlOdnSeuUufvdsIHm3NkP_bBJNwYf3egHjPTB5JD6K-MvDuc9E5YBW4mI_o6RX19iaMRO6119pfX-yqNnkaxEBXZN2wHpScA2l2wJMxS-IgzJjmca7yo9LLkYdAHQ7jl113I_vlnQsVwBQG9DhtaNbgGMnG33BgzoKCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی به تاسیسات آب‌شیرین  و تولید برق کویت حمله کرده.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6184" target="_blank">📅 14:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6183">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=NQkVc5Wuo-AZ2dFBdHU0Y0e4odEYVjoTBKH56eeeTw9bz0aR0Mn2yEfWOyZd4nHtYGq-nFQhGpOQB-50vQz2kL4VB7v2Png4FLnng5fiwuHQLbtgedZlruk1q7zsfHkb2cK3AsDT_jPm7SD0f3r6wzTAZJXsQQypAASWA2UezP3gdd7nEqoCPspALiJYdmjSc8Iu2mmqDnVELw0AqiHemQRVAkOmPtl66vUXF7_0G0xLiUMefzVMQ5egfnb9i3tarLBAEPD4C7e2wqyw4LS6LNwwBEmSGbf-NiaEG32WaVMxr7g8iNjdfk82BWwDk1N5VSRnczsk2oFb_s61Fuvi4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=NQkVc5Wuo-AZ2dFBdHU0Y0e4odEYVjoTBKH56eeeTw9bz0aR0Mn2yEfWOyZd4nHtYGq-nFQhGpOQB-50vQz2kL4VB7v2Png4FLnng5fiwuHQLbtgedZlruk1q7zsfHkb2cK3AsDT_jPm7SD0f3r6wzTAZJXsQQypAASWA2UezP3gdd7nEqoCPspALiJYdmjSc8Iu2mmqDnVELw0AqiHemQRVAkOmPtl66vUXF7_0G0xLiUMefzVMQ5egfnb9i3tarLBAEPD4C7e2wqyw4LS6LNwwBEmSGbf-NiaEG32WaVMxr7g8iNjdfk82BWwDk1N5VSRnczsk2oFb_s61Fuvi4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!  ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟  به خاطرش حتی موشک به اسرائیل نزدید؟  (که اونهم اومد در پاسخ ماهشهر رو زد؟)  خب جنگیدید و شکست خوردید!!! هم در لبنان،  هم ‌در سوریه…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6183" target="_blank">📅 14:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6182">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902cf63917.mp4?token=lqg2JYv0XO9fYMjtxUbV_6P4R8AyjpjDZogUxuOqCkXZQKvxQYsHkKprf-4pOnGGt0eV3IJ9Ce4eMDuuPD-lli3-WGpnAcr0-rdbqWhtDdgZY8O-vXlzngHUnHmUUcrxlWDemY0dS254kQTLd7eT2a7ziMtKN2C7lkvKRoGg-6r7nuzsGlus3npwtSx4EdcB4hdkHbusM43cCuspjFO9dCTTXb7fKx-sOFP34aHku51NaKkMQheMseh3JdbzVlKgeBcvjouVYA-drcgeH8eCnYl84lYwMUBaOoupGBE91uDhxKqL7grC5wF6KZzj_LRZW3GATKRsDvYYQ0YPSGf8ybxkva9AEokp6WUIxMVUVL-rXDZskvqgrhTBNCeZVUUywtxLBgAxnc5ZGPacdUqP7qHKdTYLf-1jp1BA3P-1uP9l4h4e69jITisurpZEQzZSaQGy3AXIneqRuJvwiGePM9XGkFC_PEuUfF4E-xAnbIyhi0Cg0_b-B_xAMWfpE8jz4STG-7ew9AIgNXy-Xm7bvjalc4Z92QSCJqodwf7WQCOdyyHFqHIwlSXyw8aIVHrFe7R8aIk6DxfiEnzalPHF2P9_3X2Tg-fuxPnFJcRjLbbeUXYtOAZ0KH_QUVYogxuJAxE19TVuov3PlN_Iumw4Mo2WQ5TDWyyPa5XA_p95k3k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902cf63917.mp4?token=lqg2JYv0XO9fYMjtxUbV_6P4R8AyjpjDZogUxuOqCkXZQKvxQYsHkKprf-4pOnGGt0eV3IJ9Ce4eMDuuPD-lli3-WGpnAcr0-rdbqWhtDdgZY8O-vXlzngHUnHmUUcrxlWDemY0dS254kQTLd7eT2a7ziMtKN2C7lkvKRoGg-6r7nuzsGlus3npwtSx4EdcB4hdkHbusM43cCuspjFO9dCTTXb7fKx-sOFP34aHku51NaKkMQheMseh3JdbzVlKgeBcvjouVYA-drcgeH8eCnYl84lYwMUBaOoupGBE91uDhxKqL7grC5wF6KZzj_LRZW3GATKRsDvYYQ0YPSGf8ybxkva9AEokp6WUIxMVUVL-rXDZskvqgrhTBNCeZVUUywtxLBgAxnc5ZGPacdUqP7qHKdTYLf-1jp1BA3P-1uP9l4h4e69jITisurpZEQzZSaQGy3AXIneqRuJvwiGePM9XGkFC_PEuUfF4E-xAnbIyhi0Cg0_b-B_xAMWfpE8jz4STG-7ew9AIgNXy-Xm7bvjalc4Z92QSCJqodwf7WQCOdyyHFqHIwlSXyw8aIVHrFe7R8aIk6DxfiEnzalPHF2P9_3X2Tg-fuxPnFJcRjLbbeUXYtOAZ0KH_QUVYogxuJAxE19TVuov3PlN_Iumw4Mo2WQ5TDWyyPa5XA_p95k3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!
ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟
به خاطرش حتی موشک به اسرائیل نزدید؟
(که اونهم اومد در پاسخ ماهشهر رو زد؟)
خب جنگیدید و شکست خوردید!!!
هم در لبنان،
هم ‌در سوریه هم در غزه به مردم گوش ندادید
جنگیدید و شکست خوردید!
۲- اتفاقا چون رفتید توی لبنان و غزه و…… دنبال کشیدن «دیوارهای آتشین» علیه اسرائیل و نابودی اسرائیل بودید، و افتخار میکردید که  بهشون
موشک میدید، از طرف دیگه دنبال اتم
و هسته‌ای بودید، اومدن و ایران رو زدن!
هم اونجا شکست خوردید و شهرهاشون نابود شدند
هم ایران داره نابود میشه!
نتیجه ۴۷ سال اسرائیل و آمریکا ستیزی شما!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6182" target="_blank">📅 14:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6181">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=STKGq280VNHRbosAUWg2hT8VXIim7OLFUsRhOTPRUvdbI9p0-DkHQ5HrCw4ywN5Gu9eTIf_K19rFK8XqpzXZkuIrD_lfolR5h0AYbeUkFl22Bu64s3N7z2BzKMVW0AXh3FpQhne7X_VP0L00QVaWmAzpeGhzLubdgYOCvI1S6EFuAWa5-LBnJ1w84FmIy6gH5zeC6kGXbt-lPaKGxbrQjtVGkLqaTKjdcIqC9euQM8IOBhfHTmERtmCy3XdldNXu-4ECWBrB2J2I49RU6rFodrm-SvvDOQkh19zxX2lKU_19wznG0yyxQf-lfwdHNJr10mwM60PTqjIHyZV7YyT3Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=STKGq280VNHRbosAUWg2hT8VXIim7OLFUsRhOTPRUvdbI9p0-DkHQ5HrCw4ywN5Gu9eTIf_K19rFK8XqpzXZkuIrD_lfolR5h0AYbeUkFl22Bu64s3N7z2BzKMVW0AXh3FpQhne7X_VP0L00QVaWmAzpeGhzLubdgYOCvI1S6EFuAWa5-LBnJ1w84FmIy6gH5zeC6kGXbt-lPaKGxbrQjtVGkLqaTKjdcIqC9euQM8IOBhfHTmERtmCy3XdldNXu-4ECWBrB2J2I49RU6rFodrm-SvvDOQkh19zxX2lKU_19wznG0yyxQf-lfwdHNJr10mwM60PTqjIHyZV7YyT3Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت وراثتی بود
یکی می‌مرد یکی رو به جای خودش
معین می‌کرد
مردم هیچ نقشی نداشتن!
میخواستن، نمیخواستن باید قبول میکردن.
🔺
خودش چطور رهبر شد؟
با نقل یک جمله شفاهی از خمینی!
گفتیم بعد از شما چه کنیم؟
گفت : همین آقای خامنه‌ای»
🔺
حکومت وراثتی بود : مثل پسرش مجتبا!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6181" target="_blank">📅 13:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6180">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrdFKGIQBWjUw1RJcihytPhUH9HMMNxQuaX2B6JC6995MqV5wKah86jVtj9JdNC2QVliKqV15whOKECHUfUDJyccstyj8wdkiVX54mG3IzWj0jRQxzTHOldWxWeKcn6v0jeSsqeM2FiPt7DCSVqvzZ94hR22CzMP_kbNriBKco2ZFDl3WHwdTlfVaXaWoViEXeYeqYUw8WCLNOtPlZSZzqAULh7UW2lzK8WUr4N3KcCV3ZUzO49C9G4ptRXDb2x8UQndnUa7aoRKepG4IVpfG7nkd66ooVmvx64yI7wRmZ9hMn5vMyaRGVgYGwLjhZO-pJR0_PGEbBvLbb-9RQvCxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تاریخ هزار سال پیش نیست!
که هر چی دوست دارند روایت می‌کنند.
داستان همین روزها و جلوی چشم همه ماست!
گروهی برای خونخواهی خامنه‌ای
دست به حمله به اسرائیل زدند،
اسرائیل برگشت و ضربه‌ای بهشون زد
که یک میلیون نفرشون آواره شدن!
و همین امروز و بعد از ۵ ماه، هنوز نیمی از این افراد آواره هستند!
۴ هزار نفرشون از جمله ۷۰۰ کودک کشته شدن (خود قالیباف و خود حکومت گفتن اینها برای جمهوری اسلامی کشته شدند)
بخش بزرگی از جنوب لبنان رفت
زیر چکمه سربازان اسرائیل،
رهبرانشون حذف شدند.
دستاوردش چی بود؟ افتادن به التماس
و زور و خواهش برای «آتش‌بس»!
الان میگن این «اسوه و الگوی مبارزه دلیران» است!
این اتفاقا آینه عبرت و نتیجه گنده‌گویان‌است!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6180" target="_blank">📅 11:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6179">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d198d21980.mp4?token=LxlrPni9WFY1ZlX7V6co4-xBFOzCg2uURGQ_9vmdUQKvgzs7XKHcv4JXnCuTfUdakh2aRBVu9AO-69LUAZPzh3554sBtsKUS4o8ioWVsoUTYLRIM7dL7IKLwCtoZHJG51DeTHT0GbJnYNNcvdDcc2ef9B8IucOtiiB02_BytQy8ufP-Fw1gckoYe6FkRVZuCmuosSDK-iPc5aqUKDXFreLoVRPLszO-4RvIOGt4i53JC3yZVppUACCTBV8H_F75WMffr5UP0VOMD4OF3SIwsHykfy24z_LrpOolW9CRx-GZ--OFYFw1O9Vso-Dd8DK-9AawIPh2yC7aRVmAV51ljzQr7lIKzG9yDbyrR93wJ0Mag5jFRaV31i_nxKMko0LFCBR1O9EZPMqrOdYA7w86D4Bswz71wxVqHZecTKNEKIKN5TkyWDG3Hv_Io_cQwq6YTZMOKe0TGyuarW57bZIs_1fKSG2PEUmd1eP8SLjjsDzY1cZbvJ-F2uXbJgQ4-ZJMy7ERDbJwKz7j2zydNqbWuaLerFVK5rr-n007-akLoZ554gdF6aKvop59olCbHRjqIngu9apmNxPQTqMvVq0Og6Ek3inYzhfYqeWZG0Y8yIIYW_meIU2fzm67gqj5t8KOIY-F22g_5IyVjsb42L4nfIYeUwTo23Dt76nLe4zgqOI0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d198d21980.mp4?token=LxlrPni9WFY1ZlX7V6co4-xBFOzCg2uURGQ_9vmdUQKvgzs7XKHcv4JXnCuTfUdakh2aRBVu9AO-69LUAZPzh3554sBtsKUS4o8ioWVsoUTYLRIM7dL7IKLwCtoZHJG51DeTHT0GbJnYNNcvdDcc2ef9B8IucOtiiB02_BytQy8ufP-Fw1gckoYe6FkRVZuCmuosSDK-iPc5aqUKDXFreLoVRPLszO-4RvIOGt4i53JC3yZVppUACCTBV8H_F75WMffr5UP0VOMD4OF3SIwsHykfy24z_LrpOolW9CRx-GZ--OFYFw1O9Vso-Dd8DK-9AawIPh2yC7aRVmAV51ljzQr7lIKzG9yDbyrR93wJ0Mag5jFRaV31i_nxKMko0LFCBR1O9EZPMqrOdYA7w86D4Bswz71wxVqHZecTKNEKIKN5TkyWDG3Hv_Io_cQwq6YTZMOKe0TGyuarW57bZIs_1fKSG2PEUmd1eP8SLjjsDzY1cZbvJ-F2uXbJgQ4-ZJMy7ERDbJwKz7j2zydNqbWuaLerFVK5rr-n007-akLoZ554gdF6aKvop59olCbHRjqIngu9apmNxPQTqMvVq0Og6Ek3inYzhfYqeWZG0Y8yIIYW_meIU2fzm67gqj5t8KOIY-F22g_5IyVjsb42L4nfIYeUwTo23Dt76nLe4zgqOI0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو‌شب پیش شعار میدادن که
:
«
جنوب ایران نکند جنوب لبنان شود»!
حالا دیشب شعار دادن
«جنوب لبنان و جنوب ایران
اسوه! رزم همه دلیران! »
خودشون می‌دونن جنوب لبنان ویرانه است و
مر‌دمش هم‌ آواره! فعلا هم زیر چکمه‌های سربازان ارتش اسرائیله. برای همین اولش میگفتن
«نکنه مثل جنوب لبنان بشیم!»
حالا میخوان هندونه بگذارن که جنوب ایران «اسوه رزم » است و برید جلو!! بشو شبیه جنوب لبنان!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6179" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6178">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=BAkBmO1Y_3_cO96tT0LRFHt5jx2JeCl6frB8LQO-GQB_iIxi8cX9zFu5ReCGbo5Yt9oKeMSArgS7NCyTFQMRbIN7R9GUxa7oQhefSjwRJigpPhfhrgpgt5H5CPbdCZ4oyLcfP6pDPBPYGSt6ucTMALXMQs84IsStBk50y8u_D-lg58FpW2cfUydFdmhPGO1LnOYYaMOr_LRt-wETUUCBh-JXQHtAsbrNuTRl6ShJ3a4DElZhM_8tS-pwwigoMrzh8tuprLWggLp1EKsQKwn-h6XkOq3mgmFVUesR4PyXAKymqDFaTamesLZXD9_OJj-61f6AyT-m8CYrckbIaxTZ_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=BAkBmO1Y_3_cO96tT0LRFHt5jx2JeCl6frB8LQO-GQB_iIxi8cX9zFu5ReCGbo5Yt9oKeMSArgS7NCyTFQMRbIN7R9GUxa7oQhefSjwRJigpPhfhrgpgt5H5CPbdCZ4oyLcfP6pDPBPYGSt6ucTMALXMQs84IsStBk50y8u_D-lg58FpW2cfUydFdmhPGO1LnOYYaMOr_LRt-wETUUCBh-JXQHtAsbrNuTRl6ShJ3a4DElZhM_8tS-pwwigoMrzh8tuprLWggLp1EKsQKwn-h6XkOq3mgmFVUesR4PyXAKymqDFaTamesLZXD9_OJj-61f6AyT-m8CYrckbIaxTZ_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی از سخنان سردار نقدی : اگه حتی به آمریکا حمله کنیم، قدرت پاسخ‌گویی هم ندارند!
با کدام پشتوانه اقتصادی میخواهند بجنگند؟ با کدام پشتوانه مردمی خودشان؟ همه جا در محاصره ما هستند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6178" target="_blank">📅 08:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=AatvXsJl1X6K-I7w9Xz4o6FkNPC2gggknhlapALcSXOamizUULUaEvZQvbmbqwTVnnnWfK-pfL2EnO7lpiSQyl45trpzzzllbnKb_kQYd5qgHH0fzgNZmfl7idfZwpwkFEl-lBG9DyiVO8Tr4eAgPWVzvLlpjPHg2jZ2xE9qi8s83cuS6Wf0-d1UCl-hlPaDtc8HCyV5QjkaqcIj5NW1ch4ba-e_zoomxAHHQjYkP3QbS7uNRE9-2sStJmIwmBaYU8pTRtP_a3USbVNiy_w8b4tCsRbHi9Az3RAk1EEP8RxSeh9nfDl7sXR4bk6NVewLeDwvLCgL8GOdK2D9eG9INg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=AatvXsJl1X6K-I7w9Xz4o6FkNPC2gggknhlapALcSXOamizUULUaEvZQvbmbqwTVnnnWfK-pfL2EnO7lpiSQyl45trpzzzllbnKb_kQYd5qgHH0fzgNZmfl7idfZwpwkFEl-lBG9DyiVO8Tr4eAgPWVzvLlpjPHg2jZ2xE9qi8s83cuS6Wf0-d1UCl-hlPaDtc8HCyV5QjkaqcIj5NW1ch4ba-e_zoomxAHHQjYkP3QbS7uNRE9-2sStJmIwmBaYU8pTRtP_a3USbVNiy_w8b4tCsRbHi9Az3RAk1EEP8RxSeh9nfDl7sXR4bk6NVewLeDwvLCgL8GOdK2D9eG9INg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پل  کهورستان در اطراف بندرعباس
که شب گذشته مورد حمله ارتش آمریکا قرار گرفت</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6177" target="_blank">📅 08:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6176">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار …</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6176" target="_blank">📅 08:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6175">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPEMApvxw9zxSGBCxh36Y86iyHnt8CtQHDRgGWwZygS62-gk7SBOVHYQLGPQhSc6UeSJV0r9Ev0JX6Wi4UEIKUBIbRgIt2GxatGZagYt0rutA2_1z43K-ytL3qdC1_VVBTzbEnAcTwDEsMLLd6iaJoNYMfSXtYCBIIt07WtsTiH7ZOfIzzUEeB8uQtkkcbbLeEDgDyD21xbJrSTTC_3PAGWlvUDIjN71oW_GRRvOBdHIOSLivgQocwQz4gaUw2Qkai80gqJQdFn36EJ8b5HMHEN3imK0RK3sT3dgfUNM2bP4MmQrwsIv7MpjabT1w40fPFiz7rxbDlyYg_gxJcn28w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار - شیراز
🔺
تعداد کشته‌های حمله به پل‌های بندر خمیر به ۷ نفر افزایش یافت
🔺
تفنگداران آمریکا : یک نفتکش ایرانی را توقیف کردیم.
🔺
دیشب برای نخستین بار جمهوری اسلامی به خاک سوریه هم حمله کرد، هدف : پایگاه آمریکایی در التنف
🚨
تصویر : آمریکا برای سومین بار به برج مراقبت دریایی چابهار حمله کرد و این بار آنرا منهم کرد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6175" target="_blank">📅 08:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6174">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
حملات شدید به بوشهر</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6174" target="_blank">📅 01:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6173">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=mD6FWwpGhkIYx1WGBd-yrKxb06S3E-Hrc67Q2dAaCWDICI7oWjnnZRaz9X5kyK2RudqmEgMUgm3dpdGOgftWyS3Ko7cJKL_kV_eF18f6fk5MLSFVAHCS2axWhHaSdeyabOj2Hl951T_aa0gWuctpSUO_FuI8BKpRdynMciU66AfBVkctYy7pRDVp-xqVZFx_VmnDRAQyheRWuq7CDNxUCueg1SEhHjCP_pw3xIJjunImpKEl4bPKpUYInKxjX3Fp5Nt7fwXVOUDcOcG2ufU4Un_XIjFCdpC4hBAgw-uHARNMT6VSegcwZCcVVIEBN0uLAJhlSd8merlLpMBQ_1D7KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=mD6FWwpGhkIYx1WGBd-yrKxb06S3E-Hrc67Q2dAaCWDICI7oWjnnZRaz9X5kyK2RudqmEgMUgm3dpdGOgftWyS3Ko7cJKL_kV_eF18f6fk5MLSFVAHCS2axWhHaSdeyabOj2Hl951T_aa0gWuctpSUO_FuI8BKpRdynMciU66AfBVkctYy7pRDVp-xqVZFx_VmnDRAQyheRWuq7CDNxUCueg1SEhHjCP_pw3xIJjunImpKEl4bPKpUYInKxjX3Fp5Nt7fwXVOUDcOcG2ufU4Un_XIjFCdpC4hBAgw-uHARNMT6VSegcwZCcVVIEBN0uLAJhlSd8merlLpMBQ_1D7KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏فارس: جزییات حملۀ   آمریکا به پل‌هایی در شهرستان خمیر؛ ۲ نفر شهید و ۴ نفر مجروح شدند</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6173" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPfQ_uwY-BVKBpLC8AS9bXYSKprOxw4vZrhVWCF5BQUEL7xpbAbghzYBfdD3KRnFx_2FO-vvGAspOOXo7jNh448_wJ3h146FZf3ylzTeTMwRYPi3RAMNRAxkJ8GigpVCwappCW192JJ2YiHz54YXm-Q0yl-IqWgYAfPQpEOl_1CxoROUL6R5CaRgJBVDMfskDEvBRlrZUzAZe9yd1YJnGE_R2c_H2urIe3DUmuiow32m2b8O1jOI5PuEBX2VJTBfeq-X66Vd475u86k6rlKCtH9ZfVTcq4eJsftvcnzzcudJ1DynsvBoPWMy2i8SIGfj2a__YELlaibQa07JdU6sag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6172" target="_blank">📅 00:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6171">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
صدا و سیما :دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند.
بندرعباس مهم‌ترین دروازه واردات و صادرات کشور است و شبکه ریلی بخش بزرگی از این حمل و نقل را بر عهده دارد.
این حمله می‌تواند به حمل و نقل کالا ضربه بزند و به آن اختلال وارد کند،</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6171" target="_blank">📅 00:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6170">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
حملات گسترده به حمیدیه و شوش در خوزستان</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6170" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6169">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
حمله جنگنده‌های آمریکایی به فرودگاه ایرانشهر</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6169" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6168">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067abcc49e.mp4?token=Sf3BSp2XgUJrarh_FJePomHLDwUYEQM2ceTlXLM9Qj56s7abk0WE3GT9Ee93lHI77K9yjp1G5JshKkMbE2peXQjBk3jmrJYsylMPuhmcguKAyfWF9OMY2rH8d-e3h9JKwnhsjYkq5GS9z2b4VHvxHQVw0Mu2K-lgyvbqtI_hR3yewlMnRqej71B2yLp-yRQJU8iYasPFkvV4AqeKXuxKU9h8GaV5mFd0HVpna4rZZxnf5_6eZBGUmOkEuJAT5kFFJdX9R-c3aA7emj4UckYZEpX-9A26m6Uy4SKhy2AxkKqaKAv9lMb1ToRY0mXGQAsDdmWbvtVAWxyHmdpph3PwRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067abcc49e.mp4?token=Sf3BSp2XgUJrarh_FJePomHLDwUYEQM2ceTlXLM9Qj56s7abk0WE3GT9Ee93lHI77K9yjp1G5JshKkMbE2peXQjBk3jmrJYsylMPuhmcguKAyfWF9OMY2rH8d-e3h9JKwnhsjYkq5GS9z2b4VHvxHQVw0Mu2K-lgyvbqtI_hR3yewlMnRqej71B2yLp-yRQJU8iYasPFkvV4AqeKXuxKU9h8GaV5mFd0HVpna4rZZxnf5_6eZBGUmOkEuJAT5kFFJdX9R-c3aA7emj4UckYZEpX-9A26m6Uy4SKhy2AxkKqaKAv9lMb1ToRY0mXGQAsDdmWbvtVAWxyHmdpph3PwRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس
خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6168" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6167">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3ph2uF2bTERWTmtl9jLwFuhqBDRxpDL_f-v3AXTgXRaix4l8WNPy40p3opVHb8l--zfjGle2uE2nqYT6LxqT3m_7aLQOVMyHX3q-bhnASDDww2kfAFK1-5E6yB5fWFF6YDlQ4N9YqVX330hPHc_F-evIMTVZOKR1YjnnsHKbHXZqwP1xpc_GzWE4wdsA80nzxe3IurnvKXWzNXtM-fD5sG9wRsTXu2P6RLYL8TpHGYKdye-asaH6ctLXDddjXoX8NIb5ADJkqwobORLqcxC4q6zH8v8xJxG0EKVCn1G66ZpexjWrkU2_nUPB-c038sUKnI6axrixnDUVHIs5QPCMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اهواز تحت حمله شدید
حداقل پنج انفجار مهیب در اهواز
🔺
انفجارهای مجدد در بندرعباس  و قشم
🔺
انفجار در بهبهان
🔺
انفجار در بوشهر</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6167" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6166">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=Hyc2kIz7snBl5RMOc_8jQJ3GEUuNrLlqaUW_0d-7UBLncoxEbqMw8d3wRoDXjDlbzjDugU5bry2LbPMP7ZGTwsmQcAW-97wp1wD8P8v6AYq77NFFXW86VX-qmPASrsScXMj08zhyxpJ9Hpx1DNcT5MYyDhsZ6KfcR9jAJugZLsOOiM8CVwnKoSgOwNFwpk1mOoijnXG2BmSToA2wluFhdJpeo2kc2XvKgzhRrXvhcU4LS1CJBO9_hEfNL4Z38lqwcsV1f_axKnlqu269gg5VWoJgKSm9wrd7dAPmx7i6y87RRftIsDfI18xgz-Wovpo82nWTf2FtGBbu4qC7EYtDpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=Hyc2kIz7snBl5RMOc_8jQJ3GEUuNrLlqaUW_0d-7UBLncoxEbqMw8d3wRoDXjDlbzjDugU5bry2LbPMP7ZGTwsmQcAW-97wp1wD8P8v6AYq77NFFXW86VX-qmPASrsScXMj08zhyxpJ9Hpx1DNcT5MYyDhsZ6KfcR9jAJugZLsOOiM8CVwnKoSgOwNFwpk1mOoijnXG2BmSToA2wluFhdJpeo2kc2XvKgzhRrXvhcU4LS1CJBO9_hEfNL4Z38lqwcsV1f_axKnlqu269gg5VWoJgKSm9wrd7dAPmx7i6y87RRftIsDfI18xgz-Wovpo82nWTf2FtGBbu4qC7EYtDpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که گفته می‌شود
از حملات امشب به بندرعباس است.
دقایقی پیش بندرعباس ۴ بار مورد حمله
قرار گرفت.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6166" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6165">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏
🚨
🚨
سنتکام: موج جدید حملات در پنجمین شب پیاپی را شروع کردیم.
🚨
مهر: حمله مجدد آمریکا بندرعباس
در ساعت ۲۱:۳۵ نقاطی در بندرعباس مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6165" target="_blank">📅 21:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6164">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=HriUUMI-EH7Ln0_Kr4D2PyNH5SJMyPQYbjDsleUZ89FyyCL9Ip_tpTnKouYlng_mVd-J9RIWWCwZvvVWFWYu0DeCIIRWfUDJAZHp51Hj7tLjvcvZfn2ND1AgyUfOk2j5wg03mLM2hYefPMzzr9DiCvjJAHNM39Orj7d0VqjiZp7KJvubbqNkH2pNj0pBLrasP6VtDSPxUDTabxaZTTYTjSxtmS4pgSyV-1tDhVwq9g9J0qmPjJT3g_CMKUmUdYBQEA-4u-wzJ3mtOYJjp0tAHkA-5xgo7zGVZF90Zb6n-Qk37UPa_T4b2s71vODHbQ87S1jri8hxjfCOG3-pHzZOZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=HriUUMI-EH7Ln0_Kr4D2PyNH5SJMyPQYbjDsleUZ89FyyCL9Ip_tpTnKouYlng_mVd-J9RIWWCwZvvVWFWYu0DeCIIRWfUDJAZHp51Hj7tLjvcvZfn2ND1AgyUfOk2j5wg03mLM2hYefPMzzr9DiCvjJAHNM39Orj7d0VqjiZp7KJvubbqNkH2pNj0pBLrasP6VtDSPxUDTabxaZTTYTjSxtmS4pgSyV-1tDhVwq9g9J0qmPjJT3g_CMKUmUdYBQEA-4u-wzJ3mtOYJjp0tAHkA-5xgo7zGVZF90Zb6n-Qk37UPa_T4b2s71vODHbQ87S1jri8hxjfCOG3-pHzZOZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازغدی : اگر میخواهیم اغتشاش نشود
باید با آمریکا مبارزه کنیم
(که حواس مردم به جنگ پرت بشه
و تقصیر کاستی‌های حکومت بیفته پای جنگ
و دوباره جنگ بشه «نعمت» !)</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6164" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6163">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
استانداری هرمزگان:  در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6163" target="_blank">📅 19:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6162">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQmY6brtNRQwea_Ga2dByDT8s25iNqMJW-ZdMXVyhqVRmh-L-2itsoLBgfo29QncZS83EpT_PLhxza1kqRntFU5HV_yg6zj9kvMD-uRyEN6B6ln3UGyRe2mUbvg2qLzlRKeMSuzlOpUmREIrmQZI14cdofRZid9W5c8yI7KcafU-hyJAyBiFaRYPt5gYTRIzkBkIu_mybpTTUJ2DldqG4IUAQQvRBI4ipSU8blH-ACCjIIeqhPv2dEZn8Tve2YG8ulilgoRx1PWwx59AW2f8ZdCTHeWGI84-Il4hSsN_X_Ursdv0PKARElUOm2au4gjiYlPNkH5OzofZouhZDXpPvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز :
پاکستان به ایران هشدار داده‌ که اگر به عربستان سعودی حمله کند، پاکستان آن را حمله‌ای علیه خود خواهد دانست و اعلام کرده‌: «این خط قرمز ماست.
»
پاکستان و عربستان قرارداد پیمان دفاعی مشترک دارند که بر اساس آن حمله به هر کدام ، حمله به دیگری تلقی می‌شود.
🔺
برخی اعتقاد دارند که یکی از انگیزه‌های اصلی تلاش پاکستان برای میانجی‌گری میان ج‌ا و آمریکا ، نگرانی از وقوع جنگی است که دامنه‌اش به عربستان برسد و پاکستان را ناچار به ورود به این جنگ کند.
اینک که تفاهم نامه کنار رفته، پاکستان بیش از پیش نگران این موضوع است.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6162" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6161">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
استانداری هرمزگان:
در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6161" target="_blank">📅 19:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6160">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=jImyMp-059WAcGn1XBh77Z-ypxcO5RsOppGVegn-I1UznT3UYMBIlE4YfQml8P2acQD5FIv6-lpI6f0IYn6dXORZBQ-y3lte-vKFR5i3vkKErOiXF_gIWIkV4V1q52e7lmQsz1SjZMxA7AvfiqUMGnpRsHEFaagzcOxoIQZsXCFKhkxPP5qVlyf8f4s3VCiKZfk_QLuXKA7YwqHZD76ku7CyOxK8UNnPvwM04SxC2WM1aFDxPFMuglqkEbLvmmvbPE0b_aOY3QoW6Ok1L8OXg_FxoAgPRLv2BMmavgMWGaK6kUMKnghlkrAYRnslePkQD3YDI_NB7ZfNNM1udxdS-3MHfTVB4pmkr86yazP_u7bUGQXTjWtCQCmY6RLF6bU6e9BO8z77TRscCngMd8dgsjLGWC7pM-A7-ClrPBr35POPc6OR08h7oFcSRj5P4j15UqEdwY7PYAQnZ_8ugOAdgVULaImTIRxJo5ZEfRLwdFe5elyujmf292xQOGTtUCNEyoDv_vfILg0hpDK82hljOTB6z0uqcJpwYvB1unomCGvZWOmaRQ4VUUiuMJ4hbEhMLLlwzOrgySDeEx2Ix-OKgq4LHdKq6Y-BvIIlhfdmhrNnbjRV7zivA7yVokeFqCQZvePW31YHDHVfe4Zw6qQR2ETpiVPBtWgfZ4NXK0yyT6s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=jImyMp-059WAcGn1XBh77Z-ypxcO5RsOppGVegn-I1UznT3UYMBIlE4YfQml8P2acQD5FIv6-lpI6f0IYn6dXORZBQ-y3lte-vKFR5i3vkKErOiXF_gIWIkV4V1q52e7lmQsz1SjZMxA7AvfiqUMGnpRsHEFaagzcOxoIQZsXCFKhkxPP5qVlyf8f4s3VCiKZfk_QLuXKA7YwqHZD76ku7CyOxK8UNnPvwM04SxC2WM1aFDxPFMuglqkEbLvmmvbPE0b_aOY3QoW6Ok1L8OXg_FxoAgPRLv2BMmavgMWGaK6kUMKnghlkrAYRnslePkQD3YDI_NB7ZfNNM1udxdS-3MHfTVB4pmkr86yazP_u7bUGQXTjWtCQCmY6RLF6bU6e9BO8z77TRscCngMd8dgsjLGWC7pM-A7-ClrPBr35POPc6OR08h7oFcSRj5P4j15UqEdwY7PYAQnZ_8ugOAdgVULaImTIRxJo5ZEfRLwdFe5elyujmf292xQOGTtUCNEyoDv_vfILg0hpDK82hljOTB6z0uqcJpwYvB1unomCGvZWOmaRQ4VUUiuMJ4hbEhMLLlwzOrgySDeEx2Ix-OKgq4LHdKq6Y-BvIIlhfdmhrNnbjRV7zivA7yVokeFqCQZvePW31YHDHVfe4Zw6qQR2ETpiVPBtWgfZ4NXK0yyT6s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی جدید جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6160" target="_blank">📅 19:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6159">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=W-AnG_N3P2qtpxXGUkgRY1QreMDMDzQuLl6eLfRLIEfISKxskjGPqrlQGfdZtPGK3Xdlqq9J1zvKnNAYJicwLb3QIYpSp1zN9a_70jtkU20pR3qalIkeck9pfteUJYCHQBGcTj3heRwwP6Z8KxpF_4Yr0TjwoYp-7JshiJv4p5IJxvZisiCva5VU165WKqZdjybcrAPeWQj5tB4-0i63wubtTAJ7rV_X7JUK9781hLuRo9d4KzqR4wOgjZ-pUeagiWLHLkTW5BG279vZfJZiWok0n_zhKVRZB6YQlbT6OBM61-YWYPHgX15FWyILwpBhZ2KhqPv4h8whW-rIuzjjpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=W-AnG_N3P2qtpxXGUkgRY1QreMDMDzQuLl6eLfRLIEfISKxskjGPqrlQGfdZtPGK3Xdlqq9J1zvKnNAYJicwLb3QIYpSp1zN9a_70jtkU20pR3qalIkeck9pfteUJYCHQBGcTj3heRwwP6Z8KxpF_4Yr0TjwoYp-7JshiJv4p5IJxvZisiCva5VU165WKqZdjybcrAPeWQj5tB4-0i63wubtTAJ7rV_X7JUK9781hLuRo9d4KzqR4wOgjZ-pUeagiWLHLkTW5BG279vZfJZiWok0n_zhKVRZB6YQlbT6OBM61-YWYPHgX15FWyILwpBhZ2KhqPv4h8whW-rIuzjjpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، تیر ۱۴۰۳:
ما غنی‌سازی را ۲۰ درصد کردیم جنگ شد؟ ۶۰ درصد کردیم جنگ شد؟
hafezeh_tarikhi</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6159" target="_blank">📅 18:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6158">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ایران که ۴۷ ساله که در آتش فتنه اینها می‌سوزه</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6158" target="_blank">📅 17:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6157">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سخنگوی قرارگاه خاتم : هر چه در منطقه سالم مانده از نجابت جمهوری اسلامی است!
ذوالفقاری: «همه آنچه که بنا به نجابت ایران هنوز سالم مانده، یعنی تمامی زیرساخت‌ها در منطقه، زیر ضربات پولادین نیروهای مسلح مقتدر جمهوری اسلامی در هم کوبیده خواهد شد؛ آن‌چنان که اثری از آن‌ها بر جای نماند و گویی از ابتدا وجود نداشته‌اند.»
سخنگوی قرارگاه مرکزی خاتم‌الانبیا همچنین دخالت آمریکا در تنگه هرمز را «خط قرمز شکست‌ناپذیر» جمهوری اسلامی خواند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6157" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6156">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=XYvZVHr5eiUoHlG6tCDR8PtLdXeVlrM0DyFcgFP6gHdMYGlRUMoXjRv_laTGNiUsj9RhTFvA4-RWWEM4V1JB46vDuIRhFNBWdNLrO4UfMIDxF8a33_qg5lO-XUlOhWs0UA5bpCu-bF1ViOa2J1M18cN6XYcwTpIq2x1JlAyhigfXtlEZuUoWe9FPs6leDeEsOTvt8Ru8uEvLtshsFSmpGN9P9Q8bnyVNjha04wNhkyp8UnDWg4VjHVDJZKYqoLS4MswqAM4wcoKDW5OJq_kqhvF-suZFCn_MsXX22Mtf9_IsKekGeSmSYmu0od-GGVn_rGk-Ah0T1hFxcCbH-UMHqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=XYvZVHr5eiUoHlG6tCDR8PtLdXeVlrM0DyFcgFP6gHdMYGlRUMoXjRv_laTGNiUsj9RhTFvA4-RWWEM4V1JB46vDuIRhFNBWdNLrO4UfMIDxF8a33_qg5lO-XUlOhWs0UA5bpCu-bF1ViOa2J1M18cN6XYcwTpIq2x1JlAyhigfXtlEZuUoWe9FPs6leDeEsOTvt8Ru8uEvLtshsFSmpGN9P9Q8bnyVNjha04wNhkyp8UnDWg4VjHVDJZKYqoLS4MswqAM4wcoKDW5OJq_kqhvF-suZFCn_MsXX22Mtf9_IsKekGeSmSYmu0od-GGVn_rGk-Ah0T1hFxcCbH-UMHqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شب گذشته ج‌ا به اربیل در عراق
علی‌الزیدی نخست‌وزیر عراق با صدور بیانیه‌ای،
این حمله را محکوم کرد.
در این بیانیه آمده که «به آژانس‌های امنیتی
مربوطه در هماهنگی با نیروهای امنیتی منطقه دستور داده شده که همۀ تدابیر لازم برای ممانعت از تکرار حملاتی از این دست، و نیز مقابله با هرکسی که به‌دنبال خدشه‌وارد کردن به امنیت جامعۀ سرفراز عراق باشد را اتخاذ کنند».</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6156" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6155">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQbrKorPbY5H5Od68weN8LlA6fk50iZtDXL9C6ZOorX6jcvvT373Lx7TaoA7GLUbx_FSl3B2f530jWdoBPrqpcga3L9-GxEErtJv3o3Obh4adoxaqbhQnADelJMPXIc4eU3BJ9_Wrg0rmCaQxEheFPKSr3DFB4u4q1r1D-2DEXluuzyqFjQypi5bmRUvAVQSwn6d306x06CEDQicGt77zFxLwvpE61WcFkSH9NUOyQ15yKwa9dsgNDj9bUgattkPtWDMdDQiHJOA6uIYSM_dYd3Bihr11kBT_8UGPZGPTFjKbHBRjMtW9imzbHtvRkmVdb28xqDJ1vPzH6m7iRYtqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وراجی نکنید  بگذارید بجنگند که صلح بیارن :)  مثل صلحی که ۴۷ ساله در لبنان  ‌ و غزه آوردن!  انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6155" target="_blank">📅 12:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6154">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">وراجی نکنید
بگذارید بجنگند که صلح بیارن :)
مثل صلحی که ۴۷ ساله در لبنان
‌ و غزه آوردن!
انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6154" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6152">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=h2-9Owhi_3GWjOjulEMbVDc-SpxOoABWcbgilgFuBEy9P8jIABvy9It5PPOISFcVw2-g6SZAV0sxpPtfG_exyawNIySMFXF0FyOrE4SNlN_jiJ7qMUeTzXgChoapB_Sq8IdaLw-pUASCzSAC4vo7WRNsh2J6l4JzhVJ_T84AnoFNcYKaVDMzDLZLmOQOASuELUnV7Zl7tjajG5JJj5cMvCD4cXKg_m4rwI0vDMJOa8RptLUyXw4oFvF53_8E4_LO75GsaCkIXBsEevYGqrodA188HRHGPCzto4Q_14JNa5RarAtyWBvBQSSDeV8u7vL-MvvQXoFbkAiDWRFfSftQjFLxMocbwjH4-NQ5FVu-m3_k3bkxNbid7-0WW7VuOEYVTuLIEYtSWftsOZkJY12mgDRBnbv-Hjb376DGpHS7Lh3JiEksf6ZQTECQIbZhc9-VLu7Fj0zc_WBMhPf8eq1uWxJectQdgz4GXE7vHkOCR6FN9IY18RzJzlfeiHOI5GpOtcKKE4QqWPE4bwMSKjCpGgazncd8vUr1_vFfH0f2V4BWTIP4AGvJPn0nbX5Fca5PWwChliVeCuUkidj6Zfjp6bzn4s_AdAaNw5ZjvQLMhcSNWRkPEgdbbGi844y88jT5lcLnyvXZAvjdmlWE0fkjDFjZAMxiAE_zibjXU9Dt5NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=h2-9Owhi_3GWjOjulEMbVDc-SpxOoABWcbgilgFuBEy9P8jIABvy9It5PPOISFcVw2-g6SZAV0sxpPtfG_exyawNIySMFXF0FyOrE4SNlN_jiJ7qMUeTzXgChoapB_Sq8IdaLw-pUASCzSAC4vo7WRNsh2J6l4JzhVJ_T84AnoFNcYKaVDMzDLZLmOQOASuELUnV7Zl7tjajG5JJj5cMvCD4cXKg_m4rwI0vDMJOa8RptLUyXw4oFvF53_8E4_LO75GsaCkIXBsEevYGqrodA188HRHGPCzto4Q_14JNa5RarAtyWBvBQSSDeV8u7vL-MvvQXoFbkAiDWRFfSftQjFLxMocbwjH4-NQ5FVu-m3_k3bkxNbid7-0WW7VuOEYVTuLIEYtSWftsOZkJY12mgDRBnbv-Hjb376DGpHS7Lh3JiEksf6ZQTECQIbZhc9-VLu7Fj0zc_WBMhPf8eq1uWxJectQdgz4GXE7vHkOCR6FN9IY18RzJzlfeiHOI5GpOtcKKE4QqWPE4bwMSKjCpGgazncd8vUr1_vFfH0f2V4BWTIP4AGvJPn0nbX5Fca5PWwChliVeCuUkidj6Zfjp6bzn4s_AdAaNw5ZjvQLMhcSNWRkPEgdbbGi844y88jT5lcLnyvXZAvjdmlWE0fkjDFjZAMxiAE_zibjXU9Dt5NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگر نوحه میخونن و مداحی و رجز خوانی و.. برای کودکان غزه و لبنان و میناب و….. از تاسف از دست رفتن زندگی نیست! میخوان در این جنگ بی‌‌‌‌پایانی که با جهان دارند،  از جمله و در صدر این‌جنگها،  با خود مردم ایران جنگ دارند، سربازگیری کنند! تا نیروهاشون بزرگ‌تر…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6152" target="_blank">📅 11:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6151">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">تمدن اسلامی! تا زمانی که توی مدینه و مگه بود قادر به ساخت «توالت» هم نبود!  مستراح هم نداشتن !! اما دنیا در چه وضعی بود؟  ۶۰۰ سال قبل از تولد اسلام!  توی بیشتر شهرهای جهان  داشتن توالت عمومی! اجباری بود!   اینها میشینن روی منبر  میگن «مدینه فاضله»!!  حالا…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6151" target="_blank">📅 10:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6150">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">تمدن مصر باستان رو مطالعه کنید ابتدا تا انتهاش بر مدار مرگ بود! فرعون از زمانی که سر کار می‌ا‌ومد به فکر مقدمات مرگش بود و قبرش بود!  هنر و پزشکی و علم و مهندسی مصر همه بر پایه صنعت مرگ بود!  مومیایی و اهرام و جراحی پزشکی و….. همه برای کار و کسب مرگ بود و…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6150" target="_blank">📅 10:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6149">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dajTuahianWlYbY-g2F8NlPL5cptqQqYoqftx9-XoCiRGMPMk6rPZ5exKH8GPMqNhFOI0FVHvVQqnKeq0hVOTpuJjxyKqnk0MLh5fGjtSv-m1y9Hvhg09FyTv45Uf3a8e-kA_6pAid8GuG7ATS05Hlu6uoDeIwbIfMIGDvth1k1G5GCpanRxDev9BzK-AAavsp901kxewe3HnDnGo4TPmRKR4t7l8s4NRnb3IQmb86RJSbefWjocEZU5A9tSI7Hu5FOqFul0tcZZJh6vIegBHT67Jga2_44kho333L-43F1t8jebct0k6_PWx_S6EKHFxJ21DSYp0CmvtHsTAXMFCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها شنیدید جملاتی با این مفهوم رو که زندگی و این حیات «زندان مومنه»!  آرزوی اینها مرگه! مرگ براشون رهایی است!  اینکه برن و برسن به بهشت و به زندگی!!  مرگ رو آرمان خودشون می‌دونن و زندگی و زیبایی‌هاش  رو پست و حقیر معرفی میکنن!  و اینکه باید دائم به فکر مرگ…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6149" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6148">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..  سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند. و از مرگ متاثر میشن!  تمام هستی اینها :  مبارزه، جنگ، کشتن،  کشته شدن و….. است!  زندگی براشون چیزی نیست جز  «مبارزه  برای عقیده».  و خوشحال میشن…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6148" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6147">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=bSB5fHan92TcDiW7rKoBiVDsE93YX7HABsdaMsUSYqNZVa9Xw0vFMIjQJNDR27YWGrHZcZBbxxKlipo9SgrjOVSw_HzJYJy5DkpF8oO9qEpqtXbxbFlqxAMjKtJc742dvkeJ4irdf37SgiNYgu9JQ-7gB2eyUC4lSalOK6i5vvpL4jxK0H9tGsrQLTTz1Uok0YjsN0cy1qsqb_YeS7UWcbVthbUs5uXReY1ICvgCtrdLnTHoIneWtevLwXCtJaXXpC6JfvsbC5WJGnFeGjnd2VeOSTekDsr4gVsFPDYcqyfMIxk_Nm6RttiG0J8y0UukynkJDbp4UOAYCmbq69xDpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=bSB5fHan92TcDiW7rKoBiVDsE93YX7HABsdaMsUSYqNZVa9Xw0vFMIjQJNDR27YWGrHZcZBbxxKlipo9SgrjOVSw_HzJYJy5DkpF8oO9qEpqtXbxbFlqxAMjKtJc742dvkeJ4irdf37SgiNYgu9JQ-7gB2eyUC4lSalOK6i5vvpL4jxK0H9tGsrQLTTz1Uok0YjsN0cy1qsqb_YeS7UWcbVthbUs5uXReY1ICvgCtrdLnTHoIneWtevLwXCtJaXXpC6JfvsbC5WJGnFeGjnd2VeOSTekDsr4gVsFPDYcqyfMIxk_Nm6RttiG0J8y0UukynkJDbp4UOAYCmbq69xDpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..
سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند.
و از مرگ متاثر میشن!
تمام هستی اینها :
مبارزه، جنگ، کشتن،  کشته شدن و….. است!
زندگی براشون چیزی نیست جز
«مبارزه  برای عقیده».
و خوشحال میشن اگه زندگی رو به خاطر اون عقیده نابود کنن! زندگی نیمی از مردم جهان هم نابود بشه براشون مهم نیست!
چون «برای یک هدف بزرگ‌تر»! مبارزه میکنن!
پس چرا مثلا روی مدرسه میناب مانور میدن؟
چون میخوان شما رو بیارن توی صف مبارزه خودشون
برای اون هدف بزرگ‌تر !
برای جنگ‌های بی پایان تا رسیدن به هدف بزرگ‌تر!
اینها نمیجنگن تا در این دنیا آرامشی باشه
و صلح بلکه میجنگن برای آخرت!
برای اون دنیای دیگه مبارزه میکنن!
از این زندگی و این جهان متنفرن!
این زندگی رو فقط یک پل می‌بینن! یک فرصت برای مبارزه و کشتن و کشته شدن و….. که بعد توی اون جهان به آرامش برسن! این زندگی فقط عرصه و میدان جنگه براشون!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6147" target="_blank">📅 10:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6146">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXQIp3Hudq9Em_dQQep6ynmJKOhyLJsTbk5aeJAbw_LIbDjU1TCi3z9BAK3yZEIVDN3i6E6t0lRL1EgoUy-ZKXQXBXSXznEEMZFckYpBEmG3ABYlPm5fa-3svQUXjblBRKnMKOKNRmTmY26k3huLRUOwKOsR62q43j0j69xEzLESMoueoZQEGxOwewC82QUyYmvhI2XhCJum9NOFchyGAm2r0-BUxNNPYpEIF1QkflcBQacUcaHGSZW6xnwF_YE5IJ1aBOZoZFvjf9uw3ryOtOXqpz4H0ENtu0WxFJgiX1kFoiJVwOEwrnDrfngkU5B5wxtr1elZENtpwt6ogdqc7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران به یک شهروند زن آمریکایی که در دسامبر ۲۰۲۴ در دوران رئیس‌جمهوری جو بایدنِ خواب‌آلود به‌ناحق بازداشت شده بود، اجازه خروج از کشور داده است. او اکنون در سلامت کامل در خارج از ایران است. ایالات متحده آمریکا از این ژست حسن‌نیت ایران قدردانی می‌کند.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6146" target="_blank">📅 09:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6145">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
حملات دیشب به استان‌های خوزستان، سمنان، مرکزی و لرستان
🔺
دیشب تعداد زیادی انفجار در اهواز شنیده شد. برخی‌ها تا ۹ انفجار و برخی تعداد انفجارها را بیشتر تخمین زدند.
🔺
گزارش‌ها حکایت از آن دارد که یکی از موشک‌ها در اهواز و در نزدیکی یک بیمارستان (بقایی) اصابت کرده.
🔺
دیشب همچنین به چند نقطه از استان لرستان حمله شد، برخی گزارش‌های تایید نشده از حمله به پایگاه موشکی امام علی در لرستان خبر می‌دهند.
🔺
استاندار سمنان نیز گفته که به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.
🔺
استاندار مرکزی: شب گذشته به دو نقطه در اطراف شهر خنداب حمله شد. این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقاً مشخص می‌کند چه اهدافی را زده و نه ج.ا می‌گوید به کجاها حمله شده.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6145" target="_blank">📅 09:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6144">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">استاندار مرکزی : شب گذشته به دو نظقه در اطراف شهر خنداب حمله شد.
این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقا مشخص میکند چه اهدافی را زده و نه ج‌ا می‌گوید به کجاهاش خورده.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6144" target="_blank">📅 08:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6143">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اطلاعیه  ارتش:  سامانه‌های راداری، سامانه پدافندی پاتریوت و مخازن سوخت آمریکا در پایگاه علی‌السالم کویت را هدف قرار دادیم.
‏ رادار‌های سوپر هاوک، تأسیسات و سامانه‌های پاتریوت واشنگتن در پایگاه شیخ عیسی بحرین نیز طی حملاتی، آسیب‌های جدی دید.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6143" target="_blank">📅 08:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6142">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
استاندار سمنان : به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6142" target="_blank">📅 08:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6141">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hoXZvwdEL33gJlDnwxE4c4npSLHq5PXUQkcbbfOt63CZ-hfATssLQ7yONxb-0Qb0WHyty5ehxrLAubsX-5uDYjMGDXSuceou0DOvY6sQPewbTkzLH0iMCbFqbbLeLqzxbm9M02UeIfSTbcgLNJjA8gpLJFfjuTwJkr7bmVUdzixNFRVviY7hFd83aQOFOVWBhbO1snq8RbhKbb8Re9yKnYSieXLbf2zQczl8nVYWVy73iw78VHLIhR_y9oH5enKV5sG-SEMYuKgpQIEGrRng90x5MnXoFOcEtnrM9Hu4JubA_C2FnNgi-oz9TIlwlvyLPExF1Xn4qznb6hW6qpi_8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین یارو خودش از دست سپاه و نهادهای زیر نظر خامنه‌ای  فرار کرده و به آمریکا پناه برده!
و آمریکا رو خونه امنی پیدا کرد برای زندگی و نوشتن از اینکه اسلام چقدر زیباست و خوبه و سعادت انسان رو میخواد!
حالا از همونجا به ج‌ا میگه مبارزه کن با آمریکا! مطلقا تسلیم نشید! تا انتهاش برید!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6141" target="_blank">📅 08:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6140">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">برخی گزارش‌ها از تداوم حملات به اهواز خبر می‌دهند و اینکه تاکنون ‌۹  انفجار  مهیب در شهر شنیده شده.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6140" target="_blank">📅 23:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6139">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
چندین انفجار مهیب در چابهار و بندرعباس
🚨
کویت : امروز ۲۱ پهپاد و ۴ موشک شلیک شده از سوی ج‌ا را منهدم کردیم.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6139" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6138">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای ۲ یا ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6138" target="_blank">📅 22:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6137">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZfiDyG5_lZfuCfP37bu0yAt0ZZ9jtXyEiRSHW-AzoB6-QfOhvE9-uSKNX_j_3AQGvQr3eaFoXMFMMI8uB3BFIubLQG1BWiroowvAfqzIwTsElQxrQVqjHjn6MerKG104E0zIlkZE4V7xQUnGAgUbfkW-EwwGRAV4URc836Fyvv1Cfi-OwyR2_4fZR-cDYhrYjHWCEVgfZv1SLf4kuSHjt90NEpCHrT4s9ByCmyJ27-M4ENJ9WsMFJwxlVoPA8-EUMqS-j4pupjz8efZY65x-BZn3LamNSzWDOGI3e9P6kaOnFRO35YHH1zbSbvVrvn8U_i0z5HL1elLAD05H6NmWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما دیگه جرات حمله به اسرائیل
رو ندارید! خودتون هم خوب می‌دونید!
این ۴-۵ روز هم به همه جا حمله کردید
به جز به اون کشوری که بیت‌رهبری
رو زد نابود کرد!
و نشون داد دقیقا کجاست که سست‌تر از لانه عنکبوته!
ولی هر چقدر دوست دارید شعار بدید!
اون حزب‌الله تروریست هم رفت انتقام بگیره  هنوز و همین امروز هم نیم میلیون نفرشون  توی محله‌های مسیحی و سنی لبنان آواره شدن!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6137" target="_blank">📅 20:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6136">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">آنچه شب گذشته در بمپور رخ داد و موجب  کشته شدن تعدادی ای نیروهای ارتشی شد، قابل اجتناب بود.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6136" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6135">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e615d142.mp4?token=QEhLYZTMx4TQWZYLOteG1lNiENCNsJJdklSU0l6bX11uNEsx7_GH0gw8mVvcOTHpWM0sgCtlY4KE7V680ZocQYAbrKWrCS8btU2mPFzACEjXpTm_ORClYP4AlGAvYN8HGlyGZqYzgaAMWGwJI1ijWH720BIqVdc0R0EbNyYB_9EhDrtdnnoEKkw7ok5ygBUfgKkQmm4Wt3mH1EEEqFqhptcvWHT9C8krw2rR3-2nTnpjib_WdFvBL8WKRa-OZVMCG68TuuIprBoPPwY9pzlJIGvjiZka7wd1YiRdVWzlIyMQR7kGAYHuOXmJKXncpfxAwKEqw-41Kzcn3k46bRlvXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e615d142.mp4?token=QEhLYZTMx4TQWZYLOteG1lNiENCNsJJdklSU0l6bX11uNEsx7_GH0gw8mVvcOTHpWM0sgCtlY4KE7V680ZocQYAbrKWrCS8btU2mPFzACEjXpTm_ORClYP4AlGAvYN8HGlyGZqYzgaAMWGwJI1ijWH720BIqVdc0R0EbNyYB_9EhDrtdnnoEKkw7ok5ygBUfgKkQmm4Wt3mH1EEEqFqhptcvWHT9C8krw2rR3-2nTnpjib_WdFvBL8WKRa-OZVMCG68TuuIprBoPPwY9pzlJIGvjiZka7wd1YiRdVWzlIyMQR7kGAYHuOXmJKXncpfxAwKEqw-41Kzcn3k46bRlvXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش بینی تاریخی بختیار
در دو کلمه، برای مردم ایران</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6135" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6134">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=d2XrTKTTKuMCFSBoaIJCFjrlO-fWkcLZq75RIjftwCctMj5TyOqLNYtGbI93M1_-EONCsyMU2QNmlxRqDgeT7UglRJGJZV0oVHZgKK_tuXkaLfqcmiTW0FbmIP_HodRnhnoE61CLfmsSJi0MG0nJlRxpmJUHeE9f6_XO7cjDcmNlO1s7DJy6IEkbmzw5FwwJg6l_NpNyaBoeFIqTsCBXjlCY-Q7ypAlvSEbSoYf1HrUv-RJ9mFvw8GoCO2dakUzrp0AOVkhsmChcV0rvG9jTEiDjx73LjdoAICjv1M7WvxdCz1cCNA1gzMIofo_VxlhzT2ecM9Ofsdd0Ybqt8dO7QYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=d2XrTKTTKuMCFSBoaIJCFjrlO-fWkcLZq75RIjftwCctMj5TyOqLNYtGbI93M1_-EONCsyMU2QNmlxRqDgeT7UglRJGJZV0oVHZgKK_tuXkaLfqcmiTW0FbmIP_HodRnhnoE61CLfmsSJi0MG0nJlRxpmJUHeE9f6_XO7cjDcmNlO1s7DJy6IEkbmzw5FwwJg6l_NpNyaBoeFIqTsCBXjlCY-Q7ypAlvSEbSoYf1HrUv-RJ9mFvw8GoCO2dakUzrp0AOVkhsmChcV0rvG9jTEiDjx73LjdoAICjv1M7WvxdCz1cCNA1gzMIofo_VxlhzT2ecM9Ofsdd0Ybqt8dO7QYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی که فرمانده سپاه بود و سالها فرماندهی جنگ رو بر عهده داشت
اینجا میگه مطئنم که مسیری که در ذهن مجتبی خامنه‌ای است، بهتر از مسیری بود که شورای عالی امنیت ملی رفت.
مجری ازش می‌پرسه خب اون چه مسیری بود؟
میگه : نمی‌دونم ! نمی‌تونم که ذهن خوانی‌ کنم!
فقط می‌دونه خوب بود :) یه مشت چاپلوس !</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6134" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6133">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIQOztj8EO1b6lOlSkWDiu7ug991pC_SGescf5wnAgsjwtL12N-V3Zcwi2ICYNpIXlNrtfN6RrWx0LfnwnT057oqSTVh-RZT88GNRcD7vwd2IDma8bP8rkJvtSwaFRkyehKsmVTsF_QDea_UMwJ9ltYFsqRUrPG0B8oCr9DM3XQun1DtYEXtCicxFRpcxSzdV9tUOB5BT_xGy74NLhe9a1nJKOwu0u-FRoqiV0_HL46BccwR8WYz6024nmK3Geh-c2dwE4rGaX2u-7f8Rym42rfW6VtFHF0HMvGtspRBRNYadGDxQgy3-wx-c16vOqlZCJmxPFSu4n7BtkYij8kqmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی از اجرای حکم اعدام محمد امینی دهاقانی، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، خبر داد. مقام‌های قضایی او را به آتش‌زدن فرمانداری و کلانتری مرکزی شهرستان دهاقان در استان اصفهان متهم کرده‌اند؛ از روند بازداشت، بازجویی و جلسات دادگاه و … محمد امینی دهاقانی خبری منتشر نشده.
براساس اطلاعیه منتشر شده در خبرگزاری میزان، ارگان رسانه‌ای قوه قضاییه، حکم اعدام محمد امینی دهاقانی پس از تایید در دیوان عالی کشور، بامداد امروز ۲۴ تیر ۱۴۰۵ اجرا شده است.
در این اطلاعیه آمده است که امینی دهاقانی روز ۱۹ دی ۱۴۰۴ با پرتاب کوکتل مولوتف به ساختمان فرمانداری دهاقان باعث آتش‌سوزی شده و سپس یک کوکتل مولوتف دیگر نیز به سمت کلانتری این شهرستان پرتاب کرده است. مقام‌های قضایی همچنین مدعی شده‌اند او در تحریک معترضان برای حمله به کلانتری نقش داشته است.
دستگاه قضایی جمهوری اسلامی بخش عمده پرونده را بر اعترافات متهم استوار کرده است. در اطلاعیه رسمی ادعا شده که او در بازجویی‌ها پرتاب کوکتل مولوتف به سمت فرمانداری و کلانتری را پذیرفته و همچنین گفته است قصد داشته از یک قبضه سلاح کلاشینکف، که به ادعای مقام‌های امنیتی از ماموران گرفته شده بود، استفاده کند.
محمد امینی دهاقانی همچنین به «بازنشر و ارسال محتوای تبلیغی علیه جمهوری اسلامی، تشویش اذهان عمومی و برهم زدن امنیت روانی جامعه» متهم شده است.
او همچنین به «درخواست ارتباط‌گیری با حساب‌های کاربری» مخالفان جمهوری اسلامی و «درخواست ارتباط‌گیری» با صفحات مجازی مرتبط با خاندان پهلوی هم متهم شده است.
مقام‌های قضایی هیچ اطلاعاتی درباره نحوه دسترسی متهم به وکیل مستقل، شرایط بازجویی یا روند برگزاری دادگاه منتشر نکرده‌اند. همچنین مشخص نیست اعترافات منتشر شده در چه شرایطی اخذ شده و آیا متهم امکان رد یا اعتراض به آن‌ها را داشته است.
اعدام محمد امینی دهاقانی در حالی انجام شده است که نهادهای حقوق بشری بارها نسبت به افزایش صدور و اجرای احکام اعدام برای معترضان و متهمان پرونده‌های امنیتی در جمهوری اسلامی هشدار داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6133" target="_blank">📅 15:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6132">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
سنتکام : به تنب بزرگ حمله کردیم.
در جریان این موج ۹۰ دقیقه‌ای از حملات، با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی و محل‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را مورد حمله قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6132" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6131">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حمله امروز به چابهار</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6131" target="_blank">📅 14:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6130">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
ارتش: «آمریکا بامداد امروز با شلیک ۱۳ فروند موشک، آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور را هدف قرار داد
دشمن به مهمانسرا و اماکن نگهبانی پادگان حمله کرد
‏ ۷ تن از کارکنان پایور و وظیفه تیپ ۳۸۸ ایرانشهر شهید و تعدادی مجروح شدند.»
‏</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6130" target="_blank">📅 14:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6129">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
سنتکام : از نیم ساعت پیش موج تازه‌ای از حملات را آغاز کرده‌ایم.
(از  ساعت ۱۳:۳۰ تهران)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6129" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6128">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixCeTnRmZ0FRtIVwRbG1bfrNaPhEoOv-LHURcDor1H5T-KNntC5Qnbw8lvpDOiJ6PjxymXl1oy6H1h8JvBmzKhHBfCgkduWWxatYI1NXt9NF1_-S7Xo7GbZEY_ZBTPhx9fedn_XdVF0hq1AWSeGG5MlITky8gOKE4G4mlPglmvTGeFl4kWqaoEI93EnEQYXsbyoK_T7NHro3qSrH3WVu-aEYAhKewEevmiiR8HfgaSArh3f0h0axg7U93-eZizz9ehvOzlpCFK-JUP8jhZEXQS7pvrnmKxOT9-yDaTEgCswgFQjsMynT80eaR3f6y_NHUQ9tNzVARuvNAlHUFLm59g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابل توجه ساختاری‌های محترم
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6128" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6127">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=iMdgn_NeOr3Ihg8-cJ9d7VojUX-Azs6TRKHC_hUboNOr3pbijxr_m1AkLdQqn2ZgBFkwHTNTE-gM0RSb_HDlitU6XHEGV_Fw7jYZdY6S4rKO2T_JR7lFGYVkqiFjgO5XUzLg4ZMMyjOxD_CRymwhyRYJnLd6oq02PqHqEFcwQsw70flmo9larB-rlmnkSZD-avEe-nU2uyVK6XABm5VLmux1p5SfmaGhKr25Q0rE7nHoc_oy2VpyoGk7kmk1mk_NXpKM66lnOA4Na4ZvuVjOJr6qToz543Cj68_Kk0bVXaIRkSd_WoThvyViYA2bZ4DW8bq3n3nhSjUEkruyTljAy5H3MIa41Iy2L0DMzoI57dyv10rLuXRAlVjiOyn1thO2clLDETgGmQosMHOqjozMqdvmPakvPawCxSaYx693QnUyZTGy2k4-upcOGrz1hYTOtl3nnEFuFhWbMU7NAzFrfkGrtD3FdAlWjh7PYGFEA7HKITjqpy7Cq7yGaxZHf2tllAHWrJgN2Gvze3W9f8_rifDtAsmbgQlr_H1b704dSrQdeXw1ck_edi_oAY0r_cZQOsr5zbvk6vfxgUylYofiAtFx4E0L5Veu0X6ask3teeo9jwDQtjAmFam-TSqUt0I842apnQcmcB98UzO1CWhRt2UMakOzWq3m_oBNzOLhRzo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=iMdgn_NeOr3Ihg8-cJ9d7VojUX-Azs6TRKHC_hUboNOr3pbijxr_m1AkLdQqn2ZgBFkwHTNTE-gM0RSb_HDlitU6XHEGV_Fw7jYZdY6S4rKO2T_JR7lFGYVkqiFjgO5XUzLg4ZMMyjOxD_CRymwhyRYJnLd6oq02PqHqEFcwQsw70flmo9larB-rlmnkSZD-avEe-nU2uyVK6XABm5VLmux1p5SfmaGhKr25Q0rE7nHoc_oy2VpyoGk7kmk1mk_NXpKM66lnOA4Na4ZvuVjOJr6qToz543Cj68_Kk0bVXaIRkSd_WoThvyViYA2bZ4DW8bq3n3nhSjUEkruyTljAy5H3MIa41Iy2L0DMzoI57dyv10rLuXRAlVjiOyn1thO2clLDETgGmQosMHOqjozMqdvmPakvPawCxSaYx693QnUyZTGy2k4-upcOGrz1hYTOtl3nnEFuFhWbMU7NAzFrfkGrtD3FdAlWjh7PYGFEA7HKITjqpy7Cq7yGaxZHf2tllAHWrJgN2Gvze3W9f8_rifDtAsmbgQlr_H1b704dSrQdeXw1ck_edi_oAY0r_cZQOsr5zbvk6vfxgUylYofiAtFx4E0L5Veu0X6ask3teeo9jwDQtjAmFam-TSqUt0I842apnQcmcB98UzO1CWhRt2UMakOzWq3m_oBNzOLhRzo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سفیر اسبق جمهوری اسلامی در روسیه: مطمئن باشید اگر ترامپ را بکشیم نه تنها هیچ موشکی به سمت ما شلیک نخواهد شد، بلکه عقلای آمریکا با خوشحالی جنگ را تمام خواهند کرد.
کشتن ترامپ هیچ هزینه‌ای برای ما ندارد و با کشتن او جنگ هم تمام خواهد شد.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6127" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6126">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟  به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6126" target="_blank">📅 08:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6125">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ur-HI7opDHkc3dhTTL_hTKHJvfpwqoNFbYK8NztvUEL6Ncx6ABgchlYMqp-GjdSI4-ChbK2U3jEa0VMZyA3GYSWeUn3U0SrW2hFpd25GgjV77RaJP9lQps8CkCm5TRub2U88nHsYJVLc4M7cnJnriat0ou7lrZU_FJMc51yObmqP9P-iaa1rOFQ9ukv-e9guVT1A0hEpRgCmqcQVMh8bQFLUNuMlu2f1__KIs7S_NzKYxy238jSBLh-yEtco7bjX7mWAaS80fdSDRh4WXJ3WmY2AVpLZ0vqxVmKOp_YhenFsHpNmMIkNdpIYj9O7nYdAZdLOZF8OTTgRUwveAqYk9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟
به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت کاخ سفید برگزار کرد.
به گفته سه منبع آگاه، در ابن جلسه که ارشد‌ترین مقامات نظامی و امنیتی آمریکا در آن حضور داشتند در خصوص گسترش حملات صحبت شد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6125" target="_blank">📅 08:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6124">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=ftzrVPCGUjms8upJYiWhbV53NCWlmh2E6IG6fZ_NW_OHHTjKLiKddKaFZS99j6g-r_GeKAOdaFpUjuNia7HtL-_vsGMTnC4_4RaFub23HtHQdJP_nbsR6JLDoJPdY8zQOZGfPjBflU3MR87JAZQm_z3Fn3ctAO2E5FGjNGkpnYvTYmApLoFQ1JK8BV9TT8lj_eBpMukV9vciPrvbI-3ukFeDj2_KtzErZaI6mqchhW0qTtEB_-2ykwLKpGpe-w_nobY5GrhEerDGWtt3o-90mStvZXNdBy9ibX2QxfuFa5y4AxTqAK_1uynFRLBquSUUrNtfiQSxM1-rTGOhFV7AlRGmKxNB26voYYWJTTgELE0jN4NFQ5pACk_59IVDuyRo8ED9gxeZImd5qKYnvWNG4SPD4O6XxI3vQTK1LnKb-SaxiGYwXT7SgZzbLnxlcUNlUcoMa904V9Z7cohMF4SEJqfiXaP7hHea_CQntdhvCdstB0NhaQaJlsWVez_LzZdHWZQmWY6iC4K1GIjgEc20dJvMcDxvGL2pun1bbIeFpx6oE5d4TV17gtokiy2KuCd-q2ufXJWthFj_-VNd04QwTCEBo-1ujETAR3HCw2gqmD4pkJ7flEtE0LljQ6Oc1ajrAdfooyaKT2wOnOwsrPh2CpefiQzbnMS6gha8PMznD10" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=ftzrVPCGUjms8upJYiWhbV53NCWlmh2E6IG6fZ_NW_OHHTjKLiKddKaFZS99j6g-r_GeKAOdaFpUjuNia7HtL-_vsGMTnC4_4RaFub23HtHQdJP_nbsR6JLDoJPdY8zQOZGfPjBflU3MR87JAZQm_z3Fn3ctAO2E5FGjNGkpnYvTYmApLoFQ1JK8BV9TT8lj_eBpMukV9vciPrvbI-3ukFeDj2_KtzErZaI6mqchhW0qTtEB_-2ykwLKpGpe-w_nobY5GrhEerDGWtt3o-90mStvZXNdBy9ibX2QxfuFa5y4AxTqAK_1uynFRLBquSUUrNtfiQSxM1-rTGOhFV7AlRGmKxNB26voYYWJTTgELE0jN4NFQ5pACk_59IVDuyRo8ED9gxeZImd5qKYnvWNG4SPD4O6XxI3vQTK1LnKb-SaxiGYwXT7SgZzbLnxlcUNlUcoMa904V9Z7cohMF4SEJqfiXaP7hHea_CQntdhvCdstB0NhaQaJlsWVez_LzZdHWZQmWY6iC4K1GIjgEc20dJvMcDxvGL2pun1bbIeFpx6oE5d4TV17gtokiy2KuCd-q2ufXJWthFj_-VNd04QwTCEBo-1ujETAR3HCw2gqmD4pkJ7flEtE0LljQ6Oc1ajrAdfooyaKT2wOnOwsrPh2CpefiQzbnMS6gha8PMznD10" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مزدوران حکومتی شعار میدن
«جنوب ایران نکند جنوب لبنان شود»
عجب! شما دیگه چرا؟
خامنه‌ای میگفت «جنوب لبنان الگوی پیشرفته
و موفق مبارزه ایمانی است»! سالی یک میلیارد دلار از اموال ملت ایران رو میدین به گروه‌های تروریستی اونجا  و تبلیغ اینکه ما اونجا پیروزیم و …..!
ولی ظاهرا اسرائیل در جنوب لبنان چنان درسی بهتون داد که الان خودتون هم میگید نکنه بشیم شبیه اون «الگوی موفق»! معرفی شده توسط خامنه‌ای</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6124" target="_blank">📅 07:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6123">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=C5mc5WUAFpISCMMk0IbwB8XUEF0ExbU2DXdTXIbVz0muPsM1Aba32hgdtatb7kNYj4LpqpQvfGtYvuniqutmlyxXtEvJOOH51hH4fu-2qsNGcP_nv8mr3tWKHnvRy2HAeCCZ86VvkL7YdWu-kX7ZHN9hIkbxve8LIctMo2J2Ez9RhlqBv3s_OUHHmWkTEQ_HthtQwcyWAC0pRHaizivlsTOZkpUGa8bP3Ypf1b8A_AJD_MmYTq7Zy7XuuwQ61O4qzRnH6gsy81BtAjHCdyErjHOUr-YiisXWuSJCMxlWFhLrzy6xRKoHGFVOOTfCGXsH2tyzeMgaCfy-fHZ1qJPF_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=C5mc5WUAFpISCMMk0IbwB8XUEF0ExbU2DXdTXIbVz0muPsM1Aba32hgdtatb7kNYj4LpqpQvfGtYvuniqutmlyxXtEvJOOH51hH4fu-2qsNGcP_nv8mr3tWKHnvRy2HAeCCZ86VvkL7YdWu-kX7ZHN9hIkbxve8LIctMo2J2Ez9RhlqBv3s_OUHHmWkTEQ_HthtQwcyWAC0pRHaizivlsTOZkpUGa8bP3Ypf1b8A_AJD_MmYTq7Zy7XuuwQ61O4qzRnH6gsy81BtAjHCdyErjHOUr-YiisXWuSJCMxlWFhLrzy6xRKoHGFVOOTfCGXsH2tyzeMgaCfy-fHZ1qJPF_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6123" target="_blank">📅 07:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6122">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=IU9vALSt0DWiEC0ks3Wk9L1QyJlPxpLiqUV_KE4UTXN3Ztsu-UM8CPiCNkyhgJXOx6GTp4dKnqIibTrPFU70GSwnHkCfq8lTGJas5TTyFAEATMzUj9oiwiqsf4KPx9I5yqBkAZNsN1_9742CKSOqMpLr7kcsKPEyakfyGZVNcdR5UbhSTQEjY_5CBn0CujD6TOlaewLFEW9gAZn-PPSJQf6-g1aMRSXp-qAgz0SfmDAKJToHrqp_k9P_bDHrYHsDncNTT61Z3edRhJQtRRPbkr7qlZcKYcyPbzljzWiXwegppyl_VmWwFPecbnbynzciRVuFjkah1HgKcRRZ-t3hQi0FvOMxdTo8DKM8-rF3T9DOwrwZ_WRwUSLuIIGU6iGsbQ5bJlo_RHHxAkUXIpyWxdOlXVPKyQMRAM-XHs0_xHtn9iYHx_TjertgSneKi3f0s3AjaERqcelj7M6hs51Q0W0Itq93GQV0FjwFXLh9BVwlQQ5arwyUJnQEbPLj5jeyU9IsS6roKoSZRzCIO1Oat_9pjI3U47lkzqqtkUZVTn-yJPLGW3PCSugBRwFrXDOhNMXyCiQTHzOKsgsdo2N0a4UeWj-h5vwH79mcqfcVM5feyKeQY5t0efRMtv4Q0s69D44UZoSjC52xZFHZ9hgAg916KHbazJ_VtzvoIs_ih4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=IU9vALSt0DWiEC0ks3Wk9L1QyJlPxpLiqUV_KE4UTXN3Ztsu-UM8CPiCNkyhgJXOx6GTp4dKnqIibTrPFU70GSwnHkCfq8lTGJas5TTyFAEATMzUj9oiwiqsf4KPx9I5yqBkAZNsN1_9742CKSOqMpLr7kcsKPEyakfyGZVNcdR5UbhSTQEjY_5CBn0CujD6TOlaewLFEW9gAZn-PPSJQf6-g1aMRSXp-qAgz0SfmDAKJToHrqp_k9P_bDHrYHsDncNTT61Z3edRhJQtRRPbkr7qlZcKYcyPbzljzWiXwegppyl_VmWwFPecbnbynzciRVuFjkah1HgKcRRZ-t3hQi0FvOMxdTo8DKM8-rF3T9DOwrwZ_WRwUSLuIIGU6iGsbQ5bJlo_RHHxAkUXIpyWxdOlXVPKyQMRAM-XHs0_xHtn9iYHx_TjertgSneKi3f0s3AjaERqcelj7M6hs51Q0W0Itq93GQV0FjwFXLh9BVwlQQ5arwyUJnQEbPLj5jeyU9IsS6roKoSZRzCIO1Oat_9pjI3U47lkzqqtkUZVTn-yJPLGW3PCSugBRwFrXDOhNMXyCiQTHzOKsgsdo2N0a4UeWj-h5vwH79mcqfcVM5feyKeQY5t0efRMtv4Q0s69D44UZoSjC52xZFHZ9hgAg916KHbazJ_VtzvoIs_ih4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا میبینم راست میگه …</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6122" target="_blank">📅 07:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6121">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCWbk6Z5ZikfeyJ3LbUUREgwPEEhUj8O0lTsCPl-mmkiQsO49O2CyFK2T37h0A2XYftPSYNp44PbRYzYZzX2g18mRTzP0K8X1LQCNVxudZXRbtW0OfhRaC2cCnGZ6_P4Q69AWa-HEyxYRFvmJOzCTps8d4T0lGw_AYWom7atKuuPruN8sMjKb7EQYQzIYSLq3z3MFn_FS8cervtWsydiN36Nsn_yYexE22xFtU7To2Al-4qT5AUloUk2eXc8l8KA7WH4Yg03_CqNMpQPuU_Lbb-wLOdG95VmRjOQZ-I-qL6ftpBewmdzhfRGPkDmuuMbeUlLGG6Mxe46QSqVh-VOTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6121" target="_blank">📅 06:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ovfb1WG_Keb2gePA3t0KGQfxba0DnBR25yeilNWy6KVFJWJ8ToKyCMcWJr2d8cRUkIwBnKM9yzIVdpYeCw0cJAH84nOwf0fEmiC0zzsLI4eBLafvHBLHYNkfRRNZ5okeQ7qMgrGaaEZdCghGQ_J6wKvG-o038frOr3w7XMIT2TVOqN0TBcARe3J0Cr_wYC0cMiK9Tyx-UyR5D_1kFCvLs1TbgU5q0vu3s0ELY5ufTuztg1fyVNG8Rh4XFjnqN3cMl-PC8tGQh0f3ckGDb7gZj9qgb3YBiG3CDGpiIpHxooT0QyFaaCI1_I91RCys6auL-voX4tO49hs3ym6uDhKHTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6120" target="_blank">📅 06:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6119">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=qymI-w5KxpIK7sPAtZN5TGlqBonFU8mxcxpWIeHNKqr6vpFjq3m-DzYK0SsqZE3IGIuWDVzZ-z31-PXckQf8Xk5msaORaKVB28LCHBEf5LrUBQmAycQdYw1dYShRGr3ehG_YlDBuHNI9vH7zW8BjWqJz_3lvRpj-KAXD2nWZA3oZksZKrSXvrr2cBCNWjcET2joXunErZAwKpAQ7xFDWl49uEsBwZcbfeahZV3qBN9dmF65uMM8UkSmZhAFq9xXu7m3nmGHplwbrfDICUMCu1OMapKSgLM_K6au1azfp6pzOU0UF64e4LcRGz0gMfi_9bxuRzUvietCQ50SKqwzs0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=qymI-w5KxpIK7sPAtZN5TGlqBonFU8mxcxpWIeHNKqr6vpFjq3m-DzYK0SsqZE3IGIuWDVzZ-z31-PXckQf8Xk5msaORaKVB28LCHBEf5LrUBQmAycQdYw1dYShRGr3ehG_YlDBuHNI9vH7zW8BjWqJz_3lvRpj-KAXD2nWZA3oZksZKrSXvrr2cBCNWjcET2joXunErZAwKpAQ7xFDWl49uEsBwZcbfeahZV3qBN9dmF65uMM8UkSmZhAFq9xXu7m3nmGHplwbrfDICUMCu1OMapKSgLM_K6au1azfp6pzOU0UF64e4LcRGz0gMfi_9bxuRzUvietCQ50SKqwzs0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام فیلمی از حملات خود به ایران منتشر کرد.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6119" target="_blank">📅 06:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6118">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=FPzhnCYWqL-y50rX4GrxW9gHwKJ-noFAlZF3HVpoV61a0-WWMLHbq3UmctPZFa5snB2ZtrknyXx1ubMC7NHE3JuSmg6FhdLXeVYqenosDCz-zncMNPLoSIQFyoHq3lMIylAgRa1im4I9tmPe8f7Lyom6lyYphkJ56V9PHrLSIhPO73b0QqGqO3pIffbhCx-PjUUJrhPErbFyR_77BHsVRCT1UVwhuJ81aERdcSM-63qXdDnA6akU-FCgHhqpi1pBmrXbs9ZjvxCrATcX90DHiHQxU6ol3CR-XP92VrrOBGdndKPB9x8mIdDx5ua9fBz8jeDHJ2a4VVyedWkI6yKcTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=FPzhnCYWqL-y50rX4GrxW9gHwKJ-noFAlZF3HVpoV61a0-WWMLHbq3UmctPZFa5snB2ZtrknyXx1ubMC7NHE3JuSmg6FhdLXeVYqenosDCz-zncMNPLoSIQFyoHq3lMIylAgRa1im4I9tmPe8f7Lyom6lyYphkJ56V9PHrLSIhPO73b0QqGqO3pIffbhCx-PjUUJrhPErbFyR_77BHsVRCT1UVwhuJ81aERdcSM-63qXdDnA6akU-FCgHhqpi1pBmrXbs9ZjvxCrATcX90DHiHQxU6ol3CR-XP92VrrOBGdndKPB9x8mIdDx5ua9fBz8jeDHJ2a4VVyedWkI6yKcTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : امشب، فردا و فرداشب به سختی به آنها ضربه خواهیم زد و هفته آینده پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد، مگر آنکه  مذاکره کنند.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6118" target="_blank">📅 06:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6117">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caeb092620.mp4?token=oPyje4zmGlJm4WeLsrwj3Lfb3YqFl-ebZ3X_aW_FddWeGARfeIV_ma693KVSZteCy3m-5T9astvqyBojZxM3QqT4paUmY_PH8bRvqNJu62XoMwyEhTdgpprvA3hVkl9JPFXrQAaMWkJxd1uG2_Ai-B5jbhGj6ff8JP0sZNRIkVO4HwEFVoGCIs2RcpAGSftP3hy8ga052zkjqK5wryvuV6x2eIktvfHmbrxL6Up2hlNstFHoFW6l8OoMxVqca11l85_fLJo4iZmFczoMz3a0lmVGVzLnfvCtTnjFF5ytLAS1tJK8-qN2cpDshgaHNOVCuWJThdSEr1VQmetsV0TsvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caeb092620.mp4?token=oPyje4zmGlJm4WeLsrwj3Lfb3YqFl-ebZ3X_aW_FddWeGARfeIV_ma693KVSZteCy3m-5T9astvqyBojZxM3QqT4paUmY_PH8bRvqNJu62XoMwyEhTdgpprvA3hVkl9JPFXrQAaMWkJxd1uG2_Ai-B5jbhGj6ff8JP0sZNRIkVO4HwEFVoGCIs2RcpAGSftP3hy8ga052zkjqK5wryvuV6x2eIktvfHmbrxL6Up2hlNstFHoFW6l8OoMxVqca11l85_fLJo4iZmFczoMz3a0lmVGVzLnfvCtTnjFF5ytLAS1tJK8-qN2cpDshgaHNOVCuWJThdSEr1VQmetsV0TsvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ناشی از حمله پهپادی امشب سپاه به کویت
گفته می‌شود مخازن سوخت ارتش آمریکاست.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6117" target="_blank">📅 06:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6116">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360d24e506.mp4?token=WjgdUHA9zpIoaLTBo8I1XZxNDz4odACfS6zkFCMc3ydSQoOgFoNvo17StgAcySI1FrmE3LujXR_AcmMq7rrT5GpYWgEb_19_489ZNujmbYGTL9gvLF7nQW6cxwc9jksJ-_Ya93cKCFSU609HZfgg6J4dJUGb6aIVo7VilNNImw-9oz2GLwcoIzU4WPDvmbR8wXSCZo-3nxraaXPAnCdCyI021V2_nxRw3BlHEuSFv7QWs_EnjnKyhRpgR8qT6ON6HK87k7eLKItih2jgOiqcYeL1Vj5gQE1YuW0ISOzN8y-1M5aX7wIJ8npdKF_A69UMEM8noHtEaVM_3nKvk-KlhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360d24e506.mp4?token=WjgdUHA9zpIoaLTBo8I1XZxNDz4odACfS6zkFCMc3ydSQoOgFoNvo17StgAcySI1FrmE3LujXR_AcmMq7rrT5GpYWgEb_19_489ZNujmbYGTL9gvLF7nQW6cxwc9jksJ-_Ya93cKCFSU609HZfgg6J4dJUGb6aIVo7VilNNImw-9oz2GLwcoIzU4WPDvmbR8wXSCZo-3nxraaXPAnCdCyI021V2_nxRw3BlHEuSFv7QWs_EnjnKyhRpgR8qT6ON6HK87k7eLKItih2jgOiqcYeL1Vj5gQE1YuW0ISOzN8y-1M5aX7wIJ8npdKF_A69UMEM8noHtEaVM_3nKvk-KlhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی با موشک‌های حاوی بمب‌های خوشه‌ای به بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6116" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
