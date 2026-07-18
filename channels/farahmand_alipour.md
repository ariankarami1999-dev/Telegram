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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 14:57:31</div>
<hr>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">آماده‌ای سازی اذهان برای اشغال مناطقی از ایران در صدا و سیمای جمهوری اسلامی.
«مهم اینه که گریه نکنید، بری تلاش کنی [اگه تونستی] پس بگیری.»</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/farahmand_alipour/6216" target="_blank">📅 14:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMDpU9RJwLRRIjiRFMe0sGJ3NrwrmFdf2PfehFhmkdXqUh-dZJS_E229LfzdyMaOgy__n2N-JtFFAEKxiJHxU07MjYQL-ujO_Om42sPD9XMZXePkqNIMnH_x1YeKoHKrYmxRoNWawoVOUQSOqfzO7JiMF5l5im618mLB3u8laqzuY4FIRiFJx36XnU-NvlIf1ylK1qUwWf3mPplnauoYo6UMMY5MW0w9QRy3yZ0cleH9azRFQvZ82H4EIsU4fhxoNf2H0l8M43rAUmmTPqhhaFYMEdqrCHRYDbIa62iV1JaZj81A9S_BT_Ab6SNGVI8lX6NxdkbSBAEtWJ2vTXGJcAZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMDpU9RJwLRRIjiRFMe0sGJ3NrwrmFdf2PfehFhmkdXqUh-dZJS_E229LfzdyMaOgy__n2N-JtFFAEKxiJHxU07MjYQL-ujO_Om42sPD9XMZXePkqNIMnH_x1YeKoHKrYmxRoNWawoVOUQSOqfzO7JiMF5l5im618mLB3u8laqzuY4FIRiFJx36XnU-NvlIf1ylK1qUwWf3mPplnauoYo6UMMY5MW0w9QRy3yZ0cleH9azRFQvZ82H4EIsU4fhxoNf2H0l8M43rAUmmTPqhhaFYMEdqrCHRYDbIa62iV1JaZj81A9S_BT_Ab6SNGVI8lX6NxdkbSBAEtWJ2vTXGJcAZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرهای جمهوری اسلامی
و کودکانی که تقاضای «سر» دارند!</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/6215" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=SA-ntt700ZS27ZCnM1PiNsSePDF1axiFbA03JQFfuaOFqWbyyduRyJTtvqya6-H_Z2K7Oamjar4eZklB1QYQc1pvzsTYdRRn02OXfu8lGftKP99uxl26qkvGdX4ytjBpPklrMa3iy070vdyymHFQ2XG2_bGxhp2uSOXrdJmxMh-eLRD79ygeqrL4Me-9IXcWlaflbsFKgCxCKD_I1lBAnngVC616ufdZKt10cqluQBVDfTuzWhIyqV6Y1CMcy8rTJ4QmwlXFeD8GzdMs9LqfboKXAGxYXkORzO84M8JnySM7m_xJ_lyOTyfWJNVUd_pdyAOVagjTyOKiLqEBtsRlfnTUMe4EHaZZg0CqEXQQfyLuCO5IBoC4m4wdRp6uvEe-1-NbXyXAEWB9YIr45kM2ghDUvDRsYoeVom8_QfmwwnVsNdWRAB2lDx06huN7TkB_fhs7ajraVrqpKbat8Ii8SFryd6scxlZ9IT3mxPvGERisSB4OBx_sMey9D-STkndV1oetOIxpvdEWcj_R6a16uT4rHf31HvNV1_Lx0mpk23laoPUho1MIy7AxkokUxN_dJ4BOB3BWkNPOcCQH7m-d5JB4h0_RqzT-BExyeWPDqFH6Tp45ZI_nA_xTLUvRCw2kZ6ErDvT4e87g1ilxRoGxbkkEXelBAR07n0ynm7z5d4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=SA-ntt700ZS27ZCnM1PiNsSePDF1axiFbA03JQFfuaOFqWbyyduRyJTtvqya6-H_Z2K7Oamjar4eZklB1QYQc1pvzsTYdRRn02OXfu8lGftKP99uxl26qkvGdX4ytjBpPklrMa3iy070vdyymHFQ2XG2_bGxhp2uSOXrdJmxMh-eLRD79ygeqrL4Me-9IXcWlaflbsFKgCxCKD_I1lBAnngVC616ufdZKt10cqluQBVDfTuzWhIyqV6Y1CMcy8rTJ4QmwlXFeD8GzdMs9LqfboKXAGxYXkORzO84M8JnySM7m_xJ_lyOTyfWJNVUd_pdyAOVagjTyOKiLqEBtsRlfnTUMe4EHaZZg0CqEXQQfyLuCO5IBoC4m4wdRp6uvEe-1-NbXyXAEWB9YIr45kM2ghDUvDRsYoeVom8_QfmwwnVsNdWRAB2lDx06huN7TkB_fhs7ajraVrqpKbat8Ii8SFryd6scxlZ9IT3mxPvGERisSB4OBx_sMey9D-STkndV1oetOIxpvdEWcj_R6a16uT4rHf31HvNV1_Lx0mpk23laoPUho1MIy7AxkokUxN_dJ4BOB3BWkNPOcCQH7m-d5JB4h0_RqzT-BExyeWPDqFH6Tp45ZI_nA_xTLUvRCw2kZ6ErDvT4e87g1ilxRoGxbkkEXelBAR07n0ynm7z5d4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرنوشت ۹۰ میلیون ایرانی افتاده دست این جماعت  متوهم</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/6214" target="_blank">📅 13:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!
در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.
این بار اما آمریکا از عنوان عملیات هم پرهیز کرده و به نوعی داره با سر و صدای کمتر، این جنگ رو پیش می‌بره.
رسانه‌های بزرگ آمریکایی هم  گرچه اخبار این «حملات» ۷ روز اخیر رو پوشش میدن، اما نه با شدت و هیجانی که اخبار جنگ ۴۰ روزه رو پوشش میدادن.
شخص ترامپ هم از  هر ساعت توییت زدن و تهدیدهای درشت، فاصله گرفته.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6213" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fztRn2exidVShVS38-afA4hxkjC4LotutVqLbGDBvFUvD-29nZBP9JFyCL7UCGcECfGprImzN33WwgCoIPaSW2FuWVHFTWO2fKfDxp9AVxzBIzCt500bsZJTSCHWpOZGfxkCGA0ik7Jwq6bibYBtJX2872sSZ-qaWjTfiEts0Mrx1c8KG4JWUTrF7uuHiuQJKCz0DKYc2o9vRNnFAir2jPixfsvHsoZ2N8574OPlUdxL1cYWz-NNBQrElRsrczAoImUHWhG1c0Aj9WSDexb8ANzEOrVbmXwEnKgwwH6mhXcSmGjO5uIv_xJbfqaoxZ_6VWVsl5a-JveZLMFsYCaGOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه : در حمله به اردن حداقل ۲ جنگنده و ۳ هواگرد آمریکایی را منهدم کردیم!</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6212" target="_blank">📅 12:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یه مرد هندی دیده یه تیکه یخ توی فریزش شبیه فرم مجسمه «شیوا» شده، یکی از خدایان هندی! رفته به همسایه‌ها گفته، ملت هم اومدن دعا و نیایش و اینکه این یک نشانه است و بردن غذاهای نذری و…..  :)
شیر، شیرینی، غذا، میوه و..
صبح یخچال پر میشد، شب خالی میشد!
و مرد هندی میگفت، شیوا، نذری‌ها رو پذیرفته.
در عوض مرد هر روز چاق‌تر میشد
این داستان‌ها براتون آشنا نیست؟</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6211" target="_blank">📅 11:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">💔</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6210" target="_blank">📅 10:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f27e890899.mp4?token=XuUOyura1PqFICYpN--FoDRvfugu2kZEVs2wn6ENQM2A_6TI2ExhizW7T2CiUht3FwzNzB82imwOhFOZUHd-55Jgbb5a6SMeV_PZUyMd2p55j1Px8FmxT_miJfNfetEJcvW6h7YpwMYuZ8Ia-czCSjQWZHSQ7OrjQIJ4U-ecQwCl-YTabn5IAusER03XdhzQQi6oryj0eY129E0IjLjDX5IT4pK1F4n85LTpcNSNEuauyLstLZVpo8AAHrvpTPYsynfFl7nIuCxH7FrjKHXTnj-uCceCIjzAMhkLSZ10JeKfnn_hRfJ0I2EKFQApnCwPe0osm-5aQNayy31ysY1eSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f27e890899.mp4?token=XuUOyura1PqFICYpN--FoDRvfugu2kZEVs2wn6ENQM2A_6TI2ExhizW7T2CiUht3FwzNzB82imwOhFOZUHd-55Jgbb5a6SMeV_PZUyMd2p55j1Px8FmxT_miJfNfetEJcvW6h7YpwMYuZ8Ia-czCSjQWZHSQ7OrjQIJ4U-ecQwCl-YTabn5IAusER03XdhzQQi6oryj0eY129E0IjLjDX5IT4pK1F4n85LTpcNSNEuauyLstLZVpo8AAHrvpTPYsynfFl7nIuCxH7FrjKHXTnj-uCceCIjzAMhkLSZ10JeKfnn_hRfJ0I2EKFQApnCwPe0osm-5aQNayy31ysY1eSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از پل‌های غرب استان هرمزگان</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6209" target="_blank">📅 10:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6208">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!  این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6208" target="_blank">📅 10:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6206">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان می‌گوید که چند موشک به تاسیسات برق و پمپ‌های آب‌شیرین‌کن مستقر در اسکله روستای بونجی در جاسک اصابت کرده است.
گقته می‌شود که این آبشیرین‌کن، آب حدود ۲۰ روستا را تامین می‌کرد.
🔺
شب گذشته کویت نیز اعلام کرد که جمهوری اسلامی همچون پریشب، به یکی از تاسیسات آب شیرین کن این کشور حمله کرده.
🔺
ارتش اردن اعلام کرده است که سامانه‌های پدافند هوایی آن کشور ۱۰ موشک ایرانی را که وارد حریم هوایی اردن شده و خاکش را هدف گرفته بودند، رهگیری و سرنگون کرده‌اند.
🔺
ارتش جمهوری اسلامی نیز با صدور بیانیه‌ای از حمله به پایگاه آمریکا و چند پل در بحرین خبر داده است.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6206" target="_blank">📅 09:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6205">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
وزارت آموزش و پرورش:
🔺
با توجه به استمرار شرایط ناپایدار در جنوب کشور، آزمون های نهایی تمامی رشته های تحصیلی پایه یازدهم و  دوازدهم در روزهای یکشنبه و دوشنبه،  ۲۸ و ۲۹ تیر ۱۴۰۵ صرفاً در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می گردد.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6205" target="_blank">📅 09:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6204">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=EQDqqUnmmainNW4tviUqMqoTQmCtCnAcytNt7YAFLSWRrA1ORHLYBc1GNW9hBgsIyYLMTR5IBxu6PXQciTqnEBnx147Lce8ij6qdUPeM9sOWsPJO-p4bYpFIRZDirBGhlXUVwU5CuxNkLWPVcaPFCB46Bc4evjZtNBH-OLdEk_nm_MxYANz3pkxKur017LU_7r8Lv3vIuS3tGrg0sLGq2zfrqQFh1FLI7LQ1p1nEeRSTYyjGMGatLTIhjn-05X7a9XC4vQGszGAzH6Q8R09tuFBnT5BWVY8TBvVRaHitBP6Py9AkDQ3lbek3qXjPuCTR7jwKl6vovs6XVlzNEI2rYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=EQDqqUnmmainNW4tviUqMqoTQmCtCnAcytNt7YAFLSWRrA1ORHLYBc1GNW9hBgsIyYLMTR5IBxu6PXQciTqnEBnx147Lce8ij6qdUPeM9sOWsPJO-p4bYpFIRZDirBGhlXUVwU5CuxNkLWPVcaPFCB46Bc4evjZtNBH-OLdEk_nm_MxYANz3pkxKur017LU_7r8Lv3vIuS3tGrg0sLGq2zfrqQFh1FLI7LQ1p1nEeRSTYyjGMGatLTIhjn-05X7a9XC4vQGszGAzH6Q8R09tuFBnT5BWVY8TBvVRaHitBP6Py9AkDQ3lbek3qXjPuCTR7jwKl6vovs6XVlzNEI2rYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مسیر ترانزیتی بندرعباس - سیرجان که در ادامه این مسیر به تهران وصل میشه.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6204" target="_blank">📅 09:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7U6VgsmWc6M0-vWa9P2SnAMmQ9Gp16g3XE_5UurUNL4IlTlKSRx-pA0V2WLJXDvF1OQQbYl0Fv6lL6vOjD_knC2Qm8xTG7d4EK2qW9viZqtLaUEsk-a3hRKaHsOoGZaiNt-sq2QeEwGRYlUGzG2JVLb9e_0ITB_ZUsBUDyfcOujpvBUAeOAwDAXKbaN-_0Khaqt-tzTRyevu3MxYUL79MaOA3o5d5tJGRGpeg5vSv_T1tZW2EYVVpUTpWzPcMtVrZqMIlODJNbm4A0EBvxRHor3Xrbhn4wpJnO6EARVCApNvIoR3cn0NDKeNBRQtHx-iRTESFnpMVSQBxVvTtBmuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه سپاه که میگه شب گذشته ۴ کشتی با کمک ارتش آمریکا قصد عبور از تنگه هرمز داشتند که سپاه بهشون حمله کرده و متوقفشون کرده.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6203" target="_blank">📅 09:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwIKd6DytcskgrREZ8hwA8c0pD0sZgM_-vgLSFSuppsLWvo4lKHUdnYamvU6KTJ0ZIwie4YA-P8WvlGHSSsdL1Tqj1EqYmTBJtXSZZJjRFO3ivP5mNbMPqYPVtPXuQk9OJ3aio7IybF7LKje0fKB21QUwTvctk4viQjjQTVEGzMXgeQYKOZ-JI-ojiPVYjQYGeBhs_G-zPRglqIgT0eNEBsIyy61lsLPDIe3zNaTwlZG02u33BI7OSk33P83sDXz49KXOUPsyBV0Igb4hJ2yXW5ne1QUNBSUjH4NSib_WEtNlf3eOJo1lKyP202mi84jZO9uilhtDq90cEmta9cboA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا شب گذشته با موشک
به دکل مرکز کنترل ترافیک دریایی جزیره لارک، واقع در میانه تنگه هرمز حمله کرد.
این مرکز برای ایران یکی از مهم‌ترین مراکز دیدبانی و کنترل عبور و مرور کشتی‌ها در تنگه هرمز بود،که اکنون کنترل تنگه را برای ج‌ا سخت‌تر می‌کند.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6202" target="_blank">📅 09:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6201">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6201" target="_blank">📅 09:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6200">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6200" target="_blank">📅 09:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6198">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6198" target="_blank">📅 08:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6197">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔺
سپاه : به انبار دپوی قایق‌های بدون سرنشین آمریکا در بحرین حمله کردیم.
🔺
حملات ج‌ا به کردستان عراق</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6197" target="_blank">📅 01:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6196">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
وقوع ۵ انفجار در یزد
برخی گزارش‌ها می‌گویند که حملات در پارک کوهستان یزد بوده (منطقه سایت موشکی)
🚨
گزارش ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6196" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6195">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=dfaAKyRCDXSJtwQ2Kp52tYSddR5rfJwsp1vtElLD50iMuuTJHcgi3NmSjdk934oFPpGpNOgF8qO_F6ueFJydedzHuoV4wGOcU70-jzt1wHpNkKzJHa1xwctgxRHgyxjvfOI7m4amCW-X2zvd33lr97jN1WfiiRFJG1OwO3WEPaCusBlLrXl6cTHewG_Q3u7KYUihDB9q6VHpGmnLSdqyxaM0dERSom19dUYN6QyBpXDa53zXYbIen8-IaoirW65W86yUhkxyzYl_RDYV19dJ7s-WaMeEFL49spKu2DpJh4f7nMbhT8VLDFISKTMlDMIGBHYAQXxb74TifeYkg6ADWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=dfaAKyRCDXSJtwQ2Kp52tYSddR5rfJwsp1vtElLD50iMuuTJHcgi3NmSjdk934oFPpGpNOgF8qO_F6ueFJydedzHuoV4wGOcU70-jzt1wHpNkKzJHa1xwctgxRHgyxjvfOI7m4amCW-X2zvd33lr97jN1WfiiRFJG1OwO3WEPaCusBlLrXl6cTHewG_Q3u7KYUihDB9q6VHpGmnLSdqyxaM0dERSom19dUYN6QyBpXDa53zXYbIen8-IaoirW65W86yUhkxyzYl_RDYV19dJ7s-WaMeEFL49spKu2DpJh4f7nMbhT8VLDFISKTMlDMIGBHYAQXxb74TifeYkg6ADWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گزارش چندین انفجار در لار
برخی گزارش‌ها از حمله به سایت موشکی لار خبر می‌دهند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6195" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6194">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbBppC3kE4yiqvn1rPHo5LlwHBLSmaHvizSpBZGLNUz4gRKpxGzCOHkieTXV_mtXVmjA8iUFweBq2r_sO6aWBrzIUP04nKaaLvtIlzuYj_T33P6VB477eSUrzcfNbex07FxYKIvTm923ZWUCjQ_93cESQVKHSjPIcG6ZLG-uy4SVEsWn3jzpKo3FLv5GoPxQIZGWWxZHS6HAf_q0wNHP5j4C6Zk_B-wARPr6-kGZkylyPopWt8eL_7fO_hX5d873A1jCUqrPWjsA-ZQqOHlAJq5d_A6PJ4mb-Sd6oeHtXvna7lWiOQq52OF4-22STGgayexXHILpktMYVIw1eh-bVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش حملات ارتش آمریکا به بندرعباس، قشم، سیریک، بوشهر و اهواز</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6194" target="_blank">📅 23:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6193">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
سنتکام: ‏امروز ساعت ۳ بعدازظهر به‌وقت منطقه زمانی شرقی،
[۲۲:۳۰ به وقت ایران - یک ساعت پیش] برای هفتمین شب متوالی، یک دور حملات علیه ایران انجام دادیم.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6193" target="_blank">📅 23:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6192">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029791358c.mp4?token=GfztFYSabcZxvCqs7z2LLb7hNuwTT9T8wpIIKGCmQCttv3y6mjs-WYZtIUnikcAzjr-PuKYs97ddQJ0JbER8CTzW8p-87YUURyTX_nYtjPASUB9i-DWWW5uyu2j7hvASeiOfJEsfYlWpJo3RopuU1LdfJ2XMvOSOPS2NxHwpuVGeSmlVT29xR4b5YwKw6LgekhRwFne401aKkb9sa_6WHIR-EZfby6QbrYuK8naETrxOv9QSXbiNtI5lwdN3D1jLxJUb9CRJKDl_GAWKNmFE56Ibcn1b139pFYCkJzFTzgRC75cAMaw8-MgprOO20FUZPhW7qdqQiBGnYN6MJnV8jhiKs3D--HELLnlTG7_4e4Gyw4NVIR5IVhnvgf_WFCmcBu0Rn0wOz2ltwr37aAHdnKvQq8Sg_MuL_Sq00mZH_UHmP9nDP3Cl1TqqpVwxP06xMl8u1v95WpSJZg2hjzHfqeL4FGrkZIg20uqenU0g_gBbS0otf__Rc0XJq7qMH-HMldffVb1y-Gu6SiVESnyXPVrf0UWUIiOtmEH6OyOca_9p1UlJMgRIH2iwaegjJZN5Ad4x3Wp3l-8o7ZEOhpYJO0ukGC_4GsXPruo1mr8Fise-YsFZfddETpRB1KEm-oHJVBWfD5ZrgQZor0Ie9XgFt85onEpJpJDhh6YwnKw2RNc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029791358c.mp4?token=GfztFYSabcZxvCqs7z2LLb7hNuwTT9T8wpIIKGCmQCttv3y6mjs-WYZtIUnikcAzjr-PuKYs97ddQJ0JbER8CTzW8p-87YUURyTX_nYtjPASUB9i-DWWW5uyu2j7hvASeiOfJEsfYlWpJo3RopuU1LdfJ2XMvOSOPS2NxHwpuVGeSmlVT29xR4b5YwKw6LgekhRwFne401aKkb9sa_6WHIR-EZfby6QbrYuK8naETrxOv9QSXbiNtI5lwdN3D1jLxJUb9CRJKDl_GAWKNmFE56Ibcn1b139pFYCkJzFTzgRC75cAMaw8-MgprOO20FUZPhW7qdqQiBGnYN6MJnV8jhiKs3D--HELLnlTG7_4e4Gyw4NVIR5IVhnvgf_WFCmcBu0Rn0wOz2ltwr37aAHdnKvQq8Sg_MuL_Sq00mZH_UHmP9nDP3Cl1TqqpVwxP06xMl8u1v95WpSJZg2hjzHfqeL4FGrkZIg20uqenU0g_gBbS0otf__Rc0XJq7qMH-HMldffVb1y-Gu6SiVESnyXPVrf0UWUIiOtmEH6OyOca_9p1UlJMgRIH2iwaegjJZN5Ad4x3Wp3l-8o7ZEOhpYJO0ukGC_4GsXPruo1mr8Fise-YsFZfddETpRB1KEm-oHJVBWfD5ZrgQZor0Ie9XgFt85onEpJpJDhh6YwnKw2RNc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت شانه خاکی موقت کنار پل بندرعباس</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6192" target="_blank">📅 23:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6191">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‏یک گزارش محرمانه که برای رئیس جمهور ایران تهیه شده است، نشان می‌دهد که تنها ۹٪ از ایرانیان از وضع موجود حمایت می‌کنند و تقریباً سه چهارم آنها یا اصلاحات ساختاری عمیق یا جایگزینی کامل نظام سیاسی را ترجیح می‌دهند - فاکس نیوز</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6191" target="_blank">📅 22:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6190">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:  ترامپ به ما نامه‌ای داده و صراحتاً نوشته است: «بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6190" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6189">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a688590cec.mp4?token=UQ1y20bvYjb7tx0gnaLiM3rvQos3vKGbhVM23bJ4fYHDVPMvFQzStKiL982LlPb9aTyY18qqg2xS-fwT2DrI2SqJVc5ybbs4EylusGp3Tzbc5sYt8Gpuy8bB-AtsFe9D4M1dCrEjKq9vmMTrdhQULfODIsuon0Zv6qBHF1CqEJgkUUtX0-PyUKpOiQH2BCWODpa1uCc464Af47jqr1K-9lLcci58isSy_tSJKA92O8qIWAg0fsYJpHDCbpt2RAs_aDouDPCkiPBLYIMfeCuC39SwmTu4BB0cDLfRhRpkcMXtvblG5fNJYbqim4rOXZ5HOqCpRkV-R2pAz7w75OLyNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a688590cec.mp4?token=UQ1y20bvYjb7tx0gnaLiM3rvQos3vKGbhVM23bJ4fYHDVPMvFQzStKiL982LlPb9aTyY18qqg2xS-fwT2DrI2SqJVc5ybbs4EylusGp3Tzbc5sYt8Gpuy8bB-AtsFe9D4M1dCrEjKq9vmMTrdhQULfODIsuon0Zv6qBHF1CqEJgkUUtX0-PyUKpOiQH2BCWODpa1uCc464Af47jqr1K-9lLcci58isSy_tSJKA92O8qIWAg0fsYJpHDCbpt2RAs_aDouDPCkiPBLYIMfeCuC39SwmTu4BB0cDLfRhRpkcMXtvblG5fNJYbqim4rOXZ5HOqCpRkV-R2pAz7w75OLyNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:
ترامپ به ما نامه‌ای داده و صراحتاً نوشته است:
«بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6189" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mczv1NAQG8fBbp94MDUMpxSWcxFvwCAb_YTZ22JDxMA4tXyEhYqwOEbmaGFc7ROIwsW3mD5Y7JmDjGos-tQlByjA14bmhUUL6kitTCiN0BBHyr7jGHDJywDFuAoNGGDFZqUV-WztcyijtUoqeb8wSSoZs8YDGfsLFky-c9uri1p_6PF2Eeq8eWVOYxD3forWHoRWn5hlt7Mn2ZRaFCqXKXtLyb6cO7k_WPDN6WcDNKxRJK5wzq-AryUwXuNM5zdPdxk7jUViBoI16T3WyTL0ZANyV1uTufO6W4Y_HBkb-7aVkSg8xvDmK5aqeNSkFUEmLSNoCODLIhEraoP07mh-xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ایستگاه مترو در تهران با مجسمه مریم و عیسی درست کردن (که عجیب هم نیست،
نصف قرآن داستان‌های مریم و عیسی
و قوم یهوده) و پروپاگاندایی راه انداختن
که ما چقدر احترام میگذاریم به بقیه مذاهب.
بعد همزمان کلیساها رو مصادره میکنن
و صدها نفر به جرم مسیحی بودن
توی زندانهای ج‌ا هستن و اجازه داشتن
یک مسجد به سنی‌ها رو هم نمیدن!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6188" target="_blank">📅 18:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6187">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vz6qX1avsv5lvKOUK4fzeHU5iTcUFG4_gPHoDg3j69iQczOmxO9_wQ9nsWLfKGXFcewpBOuLmcAX8KqU_BA0I32_Wt0K4VaW7sfryB5qA5iPApZQoi2IVjmteUerLSOAlO4P6dlPjBkfoV2oUjIEap6GUExgysSn2RzKsCQkiRcSDt1kS4VnXORjk-8JWAPsbVywwInRKUxvUx0xPQPqPY_iWoveYUcEMMmO7A37unueYOV0d8-DhDg9va9iaLae22VCYvEl9HpCn6KJkk9djIOGTYa58DQ5-Y3ki21T4C6ggBifSp50mD1h0DyOVAWoQWpki0O20Fmxwz9YI4Rl9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب طلاقش بده :)
چرا اینهمه کینه؟</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6187" target="_blank">📅 18:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_Ih3R1LUbIgjdInPt_StaLn2hzBLRtUUhVsRXSPwMAzafOm8HmF9NC20F_c6qRyxaUYKtq6Gn9FyJWCP3ecVLlQZma4P2ASc5wE6TyesvYzXj6GMx0rsPcwIwfVzVMC-ACId8CApLe5hJK8XMiUxgS7NzdRvN7sXgrkccOBoiBlCXOBV0G6BB9QV2pMeMJRTcRUCifbz0LH_Fdmfgi8tj9mw3WnC10LYLB1-CjsONipdYkCtbqrMi4uPaSLLQjfA56xFH6OezAbnUuunaUbHNUX7k5QK3ZysAJLFZerGCC6YnzU75tQyiB8XAmV6J4t2poKndNh3fR0DTTqsSGvwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل عرزشی !
من میگم اینها شکست‌های تاریخ
رو پیدا میکنن و به عنوان الگوی خودشون معرفی می‌کنید باور نمیکنید :)
تنگه احد! که نماد بزرگ‌ترین شکست و عقب نشینی مسلمانان در تاریخ صدر اسلامه،
رو شباهت سازی میکنن با تنگه هرمز
‌‌میگن همونطور که اونو در سیطره داشتیم
اینو در سیطره خواهیم داشت.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6186" target="_blank">📅 17:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6185">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7JhqYztsdWakDZH_d08tg4ULWSJm2qm_p9KVKQjdFXw96E1ZN5KQuEmk0QWO8zWK1cUj0YDFILzH5eQbh4Fn3Bg3_-5LyqtPcx5nfJXVkXBrhAhW8x0BEL_BW6MeyaJ1gT80IMHm4td_FmeNpIS7Fdpik1s_llhRd0wDUFXAVo0tfK7Yh3kXmUJBY6z59L1b9IgHaZ39R9SkcFPpPARY4MShOQ5IcFCAyy7q8XYleOWjmTfOkOfBmGlzHQLxG7VP1he8d_vQ1BjgK3gcOiUJf9pY4mdLI7v9vh6oGqaKm-iDvbDVffH5QpfcfafTkelfwtd0Xc7XaZhWFn19PDJKLtD8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7JhqYztsdWakDZH_d08tg4ULWSJm2qm_p9KVKQjdFXw96E1ZN5KQuEmk0QWO8zWK1cUj0YDFILzH5eQbh4Fn3Bg3_-5LyqtPcx5nfJXVkXBrhAhW8x0BEL_BW6MeyaJ1gT80IMHm4td_FmeNpIS7Fdpik1s_llhRd0wDUFXAVo0tfK7Yh3kXmUJBY6z59L1b9IgHaZ39R9SkcFPpPARY4MShOQ5IcFCAyy7q8XYleOWjmTfOkOfBmGlzHQLxG7VP1he8d_vQ1BjgK3gcOiUJf9pY4mdLI7v9vh6oGqaKm-iDvbDVffH5QpfcfafTkelfwtd0Xc7XaZhWFn19PDJKLtD8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیا بودن شعار به زبان عربی میدادن؟
چی میگفتن؟ میگفتن  سرباز ایران و وطن هستیم؟
نه میگفتن «سرباز دین و عقیده» شون هستن!
و کنار لبنان هستن! و مسیرشون همیشه مقاومته!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6185" target="_blank">📅 15:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZy5UzdIhwzwsAkwB9v8uxzHmUB-hM8TBOor5mAKzAJG21w7g4oKwi3Xa6U3eWpNrA5v4_5Hn1WtSZGRzL0XHG8vO3dKIz3MzMoPEU1mdPwoBSi3V-uXfNsAD_DGQCyP-HDLEOiulmxOdkgQ4-rvpTSwpu47wQv_73aap3AiRdif7qyCDTfQl1oWz6up19rleQ-WxEXiz4MQl4aXWRjqlTt_8YAOwsLERREokTNRT9UwwvDklPazonDJGGAU2mbe6ka7PFpxV4jRcwQRkU5HNrcYB8BFl3vMioBjMgxlAhD35Xz8GNqRWxX-ngafbSzD2ceDF8MOwY6lbUFABnV4Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی به تاسیسات آب‌شیرین  و تولید برق کویت حمله کرده.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6184" target="_blank">📅 14:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6183">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=vIowOB1SJy9uovufs9ZVCc5lwwcGV2wlFGuFhCH2uYAoEdO55kkeEq7OENK7zEE-taNwqce6KrTD_-MgtOK2ZNjhAWBcGP_HljH5uGo1X-TQj428ftb2OyZMMlP8AArg5AZklTO8kgTelQNgMUnni9AYN4vOsuOQHk4SKt1jjh6AFPDIqItYjgXjS7qYzsOSfpWkiZYvSkCE1ttJeNa0qs13BDwMcBlKz801EhjY8uCEtlONFAclDKU1jrT04DBrxX-FdNyoI4T1cxVMbBLNvXu7IbnzpQkGpGRnGU91xoNrGjPY5ofSQBLIRmuV_UKJAPsYkPRI3YMhZXb6AE02AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=vIowOB1SJy9uovufs9ZVCc5lwwcGV2wlFGuFhCH2uYAoEdO55kkeEq7OENK7zEE-taNwqce6KrTD_-MgtOK2ZNjhAWBcGP_HljH5uGo1X-TQj428ftb2OyZMMlP8AArg5AZklTO8kgTelQNgMUnni9AYN4vOsuOQHk4SKt1jjh6AFPDIqItYjgXjS7qYzsOSfpWkiZYvSkCE1ttJeNa0qs13BDwMcBlKz801EhjY8uCEtlONFAclDKU1jrT04DBrxX-FdNyoI4T1cxVMbBLNvXu7IbnzpQkGpGRnGU91xoNrGjPY5ofSQBLIRmuV_UKJAPsYkPRI3YMhZXb6AE02AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!  ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟  به خاطرش حتی موشک به اسرائیل نزدید؟  (که اونهم اومد در پاسخ ماهشهر رو زد؟)  خب جنگیدید و شکست خوردید!!! هم در لبنان،  هم ‌در سوریه…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6183" target="_blank">📅 14:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6182">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902cf63917.mp4?token=NGDbx1yDWQRqWsMLTTDgFTJ5swIOIjcMo_OACBi6yFUyO_mojruKNzVlV6Fa7jZAbYrP1FtrGLRCvKkvk07KkAih3mSbRoGym6IA-Je7k68W8kU8ySuh3gMGK4ep1AwqjCsJfk3_RhhSHE6RYnk-tWJCW8Iwy-GeeGOc605p6hXgiDrDxPZSuS7OWnofVnd8cEDqngf1nbnc9AsXZbB8Tj1Fp2Hy7RD-_6eEknMye3Y6GrtLrRd6RAH3dPjFqridPo-2w1d6C2CriJoOJlh9mRNoqgT4x_n9pPQT_Z-tCSR0o2I3BJtB1ttUJkh781MHLn1WJ8jxMn4paLgq-tAEHpSZY0YiEZcSHgxsjKLdv3RxrKg6eLw8g5jWQgmwIWzy7-nF4DqczGuaRF4NDYIq640QE1dDmcRaJfoQB3BbjTfF-6rxuPKcObSv3FHus4qIyZ4y-8k4CDqwkZ4xXxyLeGTRXPChw112OoTBseocNSIUrFVEdn9bcGwnLMPOkPobTHYd0SGzbAc8tTSvWeDMTgkC09c4Hc1YBZwUM9_we3sYfcuYGRMMT02G_6ToI2yTLliQVj6GVtKQQtKy9rmMFUILXcLe-9C0BsROfSuJzQRp82nYVSoZJ596OpNmz-JqsFS0zfGIGsbwfC2Rsiict3kDMtBXrxMWikltYq_SqYY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902cf63917.mp4?token=NGDbx1yDWQRqWsMLTTDgFTJ5swIOIjcMo_OACBi6yFUyO_mojruKNzVlV6Fa7jZAbYrP1FtrGLRCvKkvk07KkAih3mSbRoGym6IA-Je7k68W8kU8ySuh3gMGK4ep1AwqjCsJfk3_RhhSHE6RYnk-tWJCW8Iwy-GeeGOc605p6hXgiDrDxPZSuS7OWnofVnd8cEDqngf1nbnc9AsXZbB8Tj1Fp2Hy7RD-_6eEknMye3Y6GrtLrRd6RAH3dPjFqridPo-2w1d6C2CriJoOJlh9mRNoqgT4x_n9pPQT_Z-tCSR0o2I3BJtB1ttUJkh781MHLn1WJ8jxMn4paLgq-tAEHpSZY0YiEZcSHgxsjKLdv3RxrKg6eLw8g5jWQgmwIWzy7-nF4DqczGuaRF4NDYIq640QE1dDmcRaJfoQB3BbjTfF-6rxuPKcObSv3FHus4qIyZ4y-8k4CDqwkZ4xXxyLeGTRXPChw112OoTBseocNSIUrFVEdn9bcGwnLMPOkPobTHYd0SGzbAc8tTSvWeDMTgkC09c4Hc1YBZwUM9_we3sYfcuYGRMMT02G_6ToI2yTLliQVj6GVtKQQtKy9rmMFUILXcLe-9C0BsROfSuJzQRp82nYVSoZJ596OpNmz-JqsFS0zfGIGsbwfC2Rsiict3kDMtBXrxMWikltYq_SqYY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6182" target="_blank">📅 14:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6181">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=lmR-ARVmr8eXUfMk0CdPUTceJ_TjTdqgO5ZHst5sSBhZ4RssLpfQrqc6gUtPakMl6z-1RzCVsZPzkS7tyms-ernWCv9vgH7VQQZ-VHWr11zbscS5rm7gnghQKMKeLsCg0U25y8vghabj2yhQZL5GYkDVbytiNflky3S4nWNuipWfKTq4bqM3u_q2G6eiOimZGP3InOc4JRT61I3pzTaky0lDXo6oRtQYq_qE-5uieGNQPLcL1s9TKlnleg_HnPbLAYmHL8dmvs5oBatfKaIjH1kG51JIO9cim5Vz7cvTT0PR2VSZKlonfZHtg_28YWgLmA4BdxHcg3arTUdGiKzJaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=lmR-ARVmr8eXUfMk0CdPUTceJ_TjTdqgO5ZHst5sSBhZ4RssLpfQrqc6gUtPakMl6z-1RzCVsZPzkS7tyms-ernWCv9vgH7VQQZ-VHWr11zbscS5rm7gnghQKMKeLsCg0U25y8vghabj2yhQZL5GYkDVbytiNflky3S4nWNuipWfKTq4bqM3u_q2G6eiOimZGP3InOc4JRT61I3pzTaky0lDXo6oRtQYq_qE-5uieGNQPLcL1s9TKlnleg_HnPbLAYmHL8dmvs5oBatfKaIjH1kG51JIO9cim5Vz7cvTT0PR2VSZKlonfZHtg_28YWgLmA4BdxHcg3arTUdGiKzJaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6181" target="_blank">📅 13:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6180">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcOgsz3CbF0DIz5qbLeXx5GyMcIYA_gC3TWtd_lPB98gLZ6jP-HZREPACIJl0Ywm_kuZoyYYib5QVoMlZpQ-UISUxn2b9vm7aOJiC-m2vyBs44MdjbMZVZdgRHBKOiyXPO2uBKVHnIL9M3WE_BTFiHEsbn4jCp9yGfW-qU6PB6l7o8kNpYQ5j1ndQ_3RIq6j29f8SoorCHTjmUdbQcHFXiPOXQVt51eAWBrSWiK14xo4YBx39ebEIoInTVhDpmEqj-l7JB19vuB1YInOqMjfLgXgaSArQs2CPoKSqZR1s2qQ1ZxxVVnQ9HOktGTzMK8xOfkBebB3HE_qFxXIjFMBLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6180" target="_blank">📅 11:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6179">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d198d21980.mp4?token=OLAN_hznuF4T0wTkwPHHtmr1Pj8-zoFTSUddBUKDDqk-fxfybEG4lag3nkZbCLqBZ6GW1meLRc7QgEL3lkNRz0YyhS1GMjLQhiKTu0AlhBR-w9kKWtyzdw6VnNsWIQzor72ILqDOgMs-Grn--VgfcMbWbqzHjKof0B9J--G-QUQ4efc9W-1vonqR6Uvn9bxY9VPXSRq7_C0y-FRrZHtSNj6fcxLV_l22s_80DYklledwePghpPz61svUVrp4eavHR4V06aYZGngWSibbo274VIR2J-IgYAoUmhKnroe4boCMRm6hWwnwvuW13dexwMAjBOeKQVPsL6GAy_3wIGY_szvi0vjkoGZDjCnapINeqBopzoj-LcT_0ht1NH6hcOBCOEHdMJO1-vB4BglCVuLhK_iEzvsSTJH3_GthFR65yR1kADNwgLdDhx3xfNqgaQGHBEniiTBUz_8f6S0P1XmP99MvgLcqRRtXdAfU5-xx1bMOvFDBvUUM2YxpvScSPEN7j1yhmsgiXtHZQpdcGdAEZdlLIiDhGzdunfPsL4eLrGMdUK5W3rocuQwzJ6TlltsqdaQV-D1dhWCQS6-axQ3FxmLG2iq6hgivES5i6rZGkUqjBjDImc-l7_1w2mDRlw9Gd21o-Nu0E4Da7NE526LfXaEtsEIkrOWGVbhwv_rsmMs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d198d21980.mp4?token=OLAN_hznuF4T0wTkwPHHtmr1Pj8-zoFTSUddBUKDDqk-fxfybEG4lag3nkZbCLqBZ6GW1meLRc7QgEL3lkNRz0YyhS1GMjLQhiKTu0AlhBR-w9kKWtyzdw6VnNsWIQzor72ILqDOgMs-Grn--VgfcMbWbqzHjKof0B9J--G-QUQ4efc9W-1vonqR6Uvn9bxY9VPXSRq7_C0y-FRrZHtSNj6fcxLV_l22s_80DYklledwePghpPz61svUVrp4eavHR4V06aYZGngWSibbo274VIR2J-IgYAoUmhKnroe4boCMRm6hWwnwvuW13dexwMAjBOeKQVPsL6GAy_3wIGY_szvi0vjkoGZDjCnapINeqBopzoj-LcT_0ht1NH6hcOBCOEHdMJO1-vB4BglCVuLhK_iEzvsSTJH3_GthFR65yR1kADNwgLdDhx3xfNqgaQGHBEniiTBUz_8f6S0P1XmP99MvgLcqRRtXdAfU5-xx1bMOvFDBvUUM2YxpvScSPEN7j1yhmsgiXtHZQpdcGdAEZdlLIiDhGzdunfPsL4eLrGMdUK5W3rocuQwzJ6TlltsqdaQV-D1dhWCQS6-axQ3FxmLG2iq6hgivES5i6rZGkUqjBjDImc-l7_1w2mDRlw9Gd21o-Nu0E4Da7NE526LfXaEtsEIkrOWGVbhwv_rsmMs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6179" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6178">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=R6LPguV848wFgZiuOtR6GSZtqmWNt4HrDz96KCk9_NMbQbOL6efbzG121WxQU2GVDsy90SkL7psHxgsXr_eEsDmFP3pzsGMqG_poYcfC2b2qcdI5TO_7BAD18PJCZouIqAaKCd6aFq1EaaCw_Fo-s5wqQW8D3bXVL9jhgIw4bSLkAJkkYxOCxpcoZR2yTAlOYjPY_oLYS_BJ8l3Uqcserw_TppwMxSqWysPHM-UeefNcB_AAUUFkYMiFe99mqeXPtTIlnblkvr1jJjfDOnICozRxI_z3GxhEcnmOF5s2ZPMvuSkRrSMHTu7rhnH80l-XzM1xAFpUqWgAudxH5NL07Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=R6LPguV848wFgZiuOtR6GSZtqmWNt4HrDz96KCk9_NMbQbOL6efbzG121WxQU2GVDsy90SkL7psHxgsXr_eEsDmFP3pzsGMqG_poYcfC2b2qcdI5TO_7BAD18PJCZouIqAaKCd6aFq1EaaCw_Fo-s5wqQW8D3bXVL9jhgIw4bSLkAJkkYxOCxpcoZR2yTAlOYjPY_oLYS_BJ8l3Uqcserw_TppwMxSqWysPHM-UeefNcB_AAUUFkYMiFe99mqeXPtTIlnblkvr1jJjfDOnICozRxI_z3GxhEcnmOF5s2ZPMvuSkRrSMHTu7rhnH80l-XzM1xAFpUqWgAudxH5NL07Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی از سخنان سردار نقدی : اگه حتی به آمریکا حمله کنیم، قدرت پاسخ‌گویی هم ندارند!
با کدام پشتوانه اقتصادی میخواهند بجنگند؟ با کدام پشتوانه مردمی خودشان؟ همه جا در محاصره ما هستند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6178" target="_blank">📅 08:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=h-5B7ghpPDlXQRzvmhatGNZIXoMOA1twN529VjRY9IhcZEspTYfDvPoE5bKuNgd-QIFzhOJTPkznrdzosilgyFStGVDMWgpTdVCsRXJpegVI2gwYcIXB4XmQy9xhhwNzYu5JM_2tgfwn3ADq3i-vnyEJyR6YPI6r0ZA5B7kUhh-dygB6CzThXRs4sbVx9pjRwsI1H6wbvl-8Wz7gnkVFsA1lhy_wYfZDAIXWGlGm6xiNbPuXGvkth7ClsYvsIaM5A7bH2Ly0jc3VNZlQFq4s0KjWxSWG-VeWKSJMOfe9C-FLJpXjYJWNgZL6LI8gesKb0ynUz02l-k3gKPSqKPiJ5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=h-5B7ghpPDlXQRzvmhatGNZIXoMOA1twN529VjRY9IhcZEspTYfDvPoE5bKuNgd-QIFzhOJTPkznrdzosilgyFStGVDMWgpTdVCsRXJpegVI2gwYcIXB4XmQy9xhhwNzYu5JM_2tgfwn3ADq3i-vnyEJyR6YPI6r0ZA5B7kUhh-dygB6CzThXRs4sbVx9pjRwsI1H6wbvl-8Wz7gnkVFsA1lhy_wYfZDAIXWGlGm6xiNbPuXGvkth7ClsYvsIaM5A7bH2Ly0jc3VNZlQFq4s0KjWxSWG-VeWKSJMOfe9C-FLJpXjYJWNgZL6LI8gesKb0ynUz02l-k3gKPSqKPiJ5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پل  کهورستان در اطراف بندرعباس
که شب گذشته مورد حمله ارتش آمریکا قرار گرفت</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6177" target="_blank">📅 08:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6176">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار …</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6176" target="_blank">📅 08:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6175">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSHY9xfavKyHoxavaSMGRAwWFL8U22_tlIClAKu-sM26pL94PQacolQgiK0PFY52Pdm-of1WXaMerL63VsMVV7tXNhd6r_08sKkW2bEMnXnLhMv9bVRQ0bXRYjAj79Dfps-pagp6s2-xrGf4i2xHut5S5Ih7_chSS5PmUJKNeEQXpsjxf33xVoaUe-RLRWpjpuc7wsvAUJXqUbRPcSq5JnkJ_uX5nEEsmzaJzA_tILxnr2v1e5t7_mqc4Ap40o74iMsYu3VI9cdW5j_-R1mCtM8tv85yLu0DP1EymLj63wlbzy0xrTMBXasSUdSSkodqHliGKxkTF6P-DWC7R-03MQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6175" target="_blank">📅 08:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6174">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
حملات شدید به بوشهر</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6174" target="_blank">📅 01:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6173">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=bG5jKnnpWnn6nASA9ZUORA5hQSLp11rfzlEP3L7YKN-UzJTPjBLe0kT1zydLNjrF_zaXBJdlCMdckMhrUzQ2X-11v_fd3JPP34fqxRWnZbYmNLeHkVrilwwqm1oHIS9RWxSey_qsERyuDpsXLy4_6oFn34D8YeI-VW-jjLEgPt4Nd_UHWYZknVmHjG6cJgpTnWGAqELwgxg97MugU2eM3Z5IWjsRb5rVm4zoWDp7jzOrOwo76SMFUUmRVmNkEC0B50onTA5MS2NPB6oEW24b8vlIxw4vO_FClcUvbYN14bDnDG3ZR0rf3mI727nWHdVKh45eZ_awerZkGZgDJ9_ZjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=bG5jKnnpWnn6nASA9ZUORA5hQSLp11rfzlEP3L7YKN-UzJTPjBLe0kT1zydLNjrF_zaXBJdlCMdckMhrUzQ2X-11v_fd3JPP34fqxRWnZbYmNLeHkVrilwwqm1oHIS9RWxSey_qsERyuDpsXLy4_6oFn34D8YeI-VW-jjLEgPt4Nd_UHWYZknVmHjG6cJgpTnWGAqELwgxg97MugU2eM3Z5IWjsRb5rVm4zoWDp7jzOrOwo76SMFUUmRVmNkEC0B50onTA5MS2NPB6oEW24b8vlIxw4vO_FClcUvbYN14bDnDG3ZR0rf3mI727nWHdVKh45eZ_awerZkGZgDJ9_ZjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏فارس: جزییات حملۀ   آمریکا به پل‌هایی در شهرستان خمیر؛ ۲ نفر شهید و ۴ نفر مجروح شدند</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6173" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAukCoR_CL0E8oZ5MFvUoXUlxFSjEnSYR5GplwDH1AgihsbIuqy14jZ2-GfvY3WakqtCciE8YQOojOhn62slA1GqTBSGxDsXad9iy7GKpPKbfmxyt42YNeA2uuxvWqgVe9REKWGLpuXyTah3VovIOuWJt35fGL5V-gQdacGCumgGltcFyMsoLTbDln7oaIfXvtiLwydF6SFEOW9hrxI2PBa_TBcmPcqGrRrUJyW3LHw1xjKbOLDuMd-SgHcbQ4bpeXdPctBUwd7i097DJl-2F7YEQVQHY-cAjoObxOs2MrQs2_p2Z8ffgdXV1XkkglE8YE0j5KJRWU_191EI0qQWWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6172" target="_blank">📅 00:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6171">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
صدا و سیما :دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند.
بندرعباس مهم‌ترین دروازه واردات و صادرات کشور است و شبکه ریلی بخش بزرگی از این حمل و نقل را بر عهده دارد.
این حمله می‌تواند به حمل و نقل کالا ضربه بزند و به آن اختلال وارد کند،</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6171" target="_blank">📅 00:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6170">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
حملات گسترده به حمیدیه و شوش در خوزستان</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6170" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6169">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
حمله جنگنده‌های آمریکایی به فرودگاه ایرانشهر</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6169" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6168">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067abcc49e.mp4?token=csWHlsAw7-HhJAPe8667ih7ECZXAad8ENvfUDed8LmLI09mnGOi7DY3SyMr6nj0vFzAvdckSDeor5TM_40OZ3VZ641phHSLTnQWLpnXIdYadL1GcQ0pRsPVrZowMXjDHknxSYKfiU29Y5rd1tzR8Wmv3VvldUeqXBquIetzWTaOU3y1uOdyvfcppK7WjD6MExHrlR-m-TZY4XHngF-mgkx_vkVHDpZUyoWLW-Z3U44lOTRKn4dngDjHekZM8Vfn6WRxKK4A3WPPQWkQtP4JPzSkPQwMBr-WkTYibozf6fUh-aiSQsK3u_tcggJ22KBsbM3cdrAJW7rl_i7GHia0WtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067abcc49e.mp4?token=csWHlsAw7-HhJAPe8667ih7ECZXAad8ENvfUDed8LmLI09mnGOi7DY3SyMr6nj0vFzAvdckSDeor5TM_40OZ3VZ641phHSLTnQWLpnXIdYadL1GcQ0pRsPVrZowMXjDHknxSYKfiU29Y5rd1tzR8Wmv3VvldUeqXBquIetzWTaOU3y1uOdyvfcppK7WjD6MExHrlR-m-TZY4XHngF-mgkx_vkVHDpZUyoWLW-Z3U44lOTRKn4dngDjHekZM8Vfn6WRxKK4A3WPPQWkQtP4JPzSkPQwMBr-WkTYibozf6fUh-aiSQsK3u_tcggJ22KBsbM3cdrAJW7rl_i7GHia0WtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس
خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6168" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6167">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYjMC9y1G2lIANREBHOLTtb2PYUQrVSRxD8-PtqAuv5Obtm8hzcHerGDNG2FE1nEAdZwOlCfqh1c4EiCD1rpSIl4jtjfGtp0xhXEW8nRycfZoC04UsTG2L32puotm-kYiRB0KQUHg8awpU6g9KXEcGwAy4iGnv_PkYevmD7HGdurWE9eagd8zGIpoRw68oeVo8gOphYZpVdDtFoXnQ2lNT_0Q-urvpO-xJbAZ9cUWmFCMySLSuA84Kf6IZGSxsF3TH6Sw329B5C0Sb1fiHNG8Zf_1vs4hawxvV4n2NK5NffHfOtIN2AHUzPEwbpRh4Wv7aOHVvbdXXV8TTBuyjIG7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6167" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6166">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=BsICY8BIRdaXUlj0x4jXpSwUIAco9yDd-qNngt1eYWtL9q0gL6S3DFm-skLljXwfobCygsS-2ZvkPVZJn-cf37-K0T0twdkkg9xs9RsYuUhIYlMFABeb05aQAw3JVJ7Cq-r7iQIeG7PDO59zy-uPO_eRiO4GZma66B4wQyU5M6OwL9lckamuWj035deB04qLy90XEaxMYr-3HvMgnKKcvDozWB_nw6v_Tyb0yYocMxQwOQmFnL8vfsSUGke3Shmoq4P6PyrOTJjsbBrGxN6Aemt2XUZ644g76JEUKkAJ0PvcUE-nytc9_bO46tWTCApBA_RWo1paIVf-VriMFnbJ5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=BsICY8BIRdaXUlj0x4jXpSwUIAco9yDd-qNngt1eYWtL9q0gL6S3DFm-skLljXwfobCygsS-2ZvkPVZJn-cf37-K0T0twdkkg9xs9RsYuUhIYlMFABeb05aQAw3JVJ7Cq-r7iQIeG7PDO59zy-uPO_eRiO4GZma66B4wQyU5M6OwL9lckamuWj035deB04qLy90XEaxMYr-3HvMgnKKcvDozWB_nw6v_Tyb0yYocMxQwOQmFnL8vfsSUGke3Shmoq4P6PyrOTJjsbBrGxN6Aemt2XUZ644g76JEUKkAJ0PvcUE-nytc9_bO46tWTCApBA_RWo1paIVf-VriMFnbJ5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که گفته می‌شود
از حملات امشب به بندرعباس است.
دقایقی پیش بندرعباس ۴ بار مورد حمله
قرار گرفت.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6166" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6165">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‏
🚨
🚨
سنتکام: موج جدید حملات در پنجمین شب پیاپی را شروع کردیم.
🚨
مهر: حمله مجدد آمریکا بندرعباس
در ساعت ۲۱:۳۵ نقاطی در بندرعباس مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6165" target="_blank">📅 21:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6164">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=OpFJfSQR4A6ZFqmV1SjvbWqIq2QEdctGROBBJK4ca_elR5T3QYWydF9EadsjUB7onzTViUywXgRC2EO4QcQZ3cYhTXvNeHwLiDtI37xciSVvFtXr09kpwlFm63WywFyluMJHL1r41HUbE30oF6D6lAVRjQJ81Elceh3hRK8YRxISPg8ROn4iZjmpmJ95Qd186vxmMvb4rCiboc3dc8mzGLFMxZ9LcJ1pMfcO4rPWsjiHzP2Q7R4n_oh1ShrVXnEOvAPdyIfxurnTqVmzO2uH9GqTDGFmluKbvV1S4Oop4k_JHWp_ioMcUkSacvzQmXtuJvXK8126qM7Fx-el0tYqLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=OpFJfSQR4A6ZFqmV1SjvbWqIq2QEdctGROBBJK4ca_elR5T3QYWydF9EadsjUB7onzTViUywXgRC2EO4QcQZ3cYhTXvNeHwLiDtI37xciSVvFtXr09kpwlFm63WywFyluMJHL1r41HUbE30oF6D6lAVRjQJ81Elceh3hRK8YRxISPg8ROn4iZjmpmJ95Qd186vxmMvb4rCiboc3dc8mzGLFMxZ9LcJ1pMfcO4rPWsjiHzP2Q7R4n_oh1ShrVXnEOvAPdyIfxurnTqVmzO2uH9GqTDGFmluKbvV1S4Oop4k_JHWp_ioMcUkSacvzQmXtuJvXK8126qM7Fx-el0tYqLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازغدی : اگر میخواهیم اغتشاش نشود
باید با آمریکا مبارزه کنیم
(که حواس مردم به جنگ پرت بشه
و تقصیر کاستی‌های حکومت بیفته پای جنگ
و دوباره جنگ بشه «نعمت» !)</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6164" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6163">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
استانداری هرمزگان:  در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6163" target="_blank">📅 19:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6162">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gw5qWTV-LvTDVt8euEVpcQ3e8GU-vuFha0zzcbu5ouZWEWyFp0OHDrImONQo9awXZHxw1eBxmPZjdd9f_udGQyVlbYp9Le5P5Ol_dhw2pNnsLT4fI6EOWTAcVNyckRsSIMfkCD095Dq2Dj2fcrOBynQyJ464OSrVJU0FX30EdVeJkQC4knxioIBasZ8wQ2F76uTaJeXDU3V3JbbgFS-shbIDUyg9PWlh3bF8kYC-ydCRzm8aAgqdcUaKrO2wbNkeNrO-NlYCutkTojG4Z08RMsynnqUUQwy5GPMde0lngmR-ye0H6SU5e0dOO-mpYRIdbcsktXH6mZJjLTwNs91Idw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز :
پاکستان به ایران هشدار داده‌ که اگر به عربستان سعودی حمله کند، پاکستان آن را حمله‌ای علیه خود خواهد دانست و اعلام کرده‌: «این خط قرمز ماست.
»
پاکستان و عربستان قرارداد پیمان دفاعی مشترک دارند که بر اساس آن حمله به هر کدام ، حمله به دیگری تلقی می‌شود.
🔺
برخی اعتقاد دارند که یکی از انگیزه‌های اصلی تلاش پاکستان برای میانجی‌گری میان ج‌ا و آمریکا ، نگرانی از وقوع جنگی است که دامنه‌اش به عربستان برسد و پاکستان را ناچار به ورود به این جنگ کند.
اینک که تفاهم نامه کنار رفته، پاکستان بیش از پیش نگران این موضوع است.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6162" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6161">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
استانداری هرمزگان:
در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6161" target="_blank">📅 19:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6160">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=odTYSqMApeFPY7Ws3LYwEdDtCr4PAKpc1WF1v41-WwRQj1NXA8Mawe5r73_NVLAA-ZigfSxih1AzPsgWKZ3wV-Jer8RxRTaYiWCzoqCEE-CPfYExgiAu8607-nRwlUUMl0QjSs-Iie3V4kXOr4ZTGE6ZOJJQBXEvbN5ptDZy1o5-Nv3caKCdEPT1OZFkr4wWjao8NjA9M4raaS-SrrCqyvdHvwjMu4ulWkfw18RHTMraOIjLHqbjQLEGURy8gF2JFXjEbw6GBubCwF6_s_Mx5qZw9cmuE9ApKhe1tImAqvx_DCPwA7NXWDaQ-3lKfUo75XCR3igaax7aAZVP820OaxYJv6bQvn7-qYW9Acwyi2zVKsB80qylQjr7m6D6_QTs9z5zXtxri3yf5v_CRljK2zBLv5CXZSzosjLMUdFlGktTU6YmrHoX4lJpy30BomoKnnFjRdMUHrU3uSpY9S7J7uLgZJAuntsbbrygTnvSEb1tVISeQqCuCEGvW2pXG9gw_yyFvRqZfYG-Nr4akyLmrNJQJmcIrUTW1MsQzovkdzJFKkNTIEr88BEkh29HZqhPEYXEviZ46AMGsp9gsgZowZDRsJ3W8rwyp5_zD8pdBNO5WegP2GLXYhyfzsB493Y0He_oGWo_0hw9YySpRX2b0sTGKxFXA3UMkKwkClgEsw4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=odTYSqMApeFPY7Ws3LYwEdDtCr4PAKpc1WF1v41-WwRQj1NXA8Mawe5r73_NVLAA-ZigfSxih1AzPsgWKZ3wV-Jer8RxRTaYiWCzoqCEE-CPfYExgiAu8607-nRwlUUMl0QjSs-Iie3V4kXOr4ZTGE6ZOJJQBXEvbN5ptDZy1o5-Nv3caKCdEPT1OZFkr4wWjao8NjA9M4raaS-SrrCqyvdHvwjMu4ulWkfw18RHTMraOIjLHqbjQLEGURy8gF2JFXjEbw6GBubCwF6_s_Mx5qZw9cmuE9ApKhe1tImAqvx_DCPwA7NXWDaQ-3lKfUo75XCR3igaax7aAZVP820OaxYJv6bQvn7-qYW9Acwyi2zVKsB80qylQjr7m6D6_QTs9z5zXtxri3yf5v_CRljK2zBLv5CXZSzosjLMUdFlGktTU6YmrHoX4lJpy30BomoKnnFjRdMUHrU3uSpY9S7J7uLgZJAuntsbbrygTnvSEb1tVISeQqCuCEGvW2pXG9gw_yyFvRqZfYG-Nr4akyLmrNJQJmcIrUTW1MsQzovkdzJFKkNTIEr88BEkh29HZqhPEYXEviZ46AMGsp9gsgZowZDRsJ3W8rwyp5_zD8pdBNO5WegP2GLXYhyfzsB493Y0He_oGWo_0hw9YySpRX2b0sTGKxFXA3UMkKwkClgEsw4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی جدید جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6160" target="_blank">📅 19:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6159">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=lAOZu5aK5we9KiEJLlBFk9va4NBks9kleoTw2fmQ5kWN4R9LrC9mESjTcrxentYOhN7ooRdAz0reD562pA_EizjdXJGHsI1NebhB6xHj5uu4O_JXkngjN-vfgl2XJLfTfkEYqL81Hi4_a1aMG_oSGXAQ4qDKi--LcEGzQGhBXgHobUjZ7eiwpdyn0p8PrIgXuuhi97Kf7MEt3uQvokX4al01Lt6HfAIH8rIPTcu9BF1mXJEjoH79eEpb4mxTzAgccPjVweC5gYkaqed_WkIzqkRn15wm9CIjoWSHAirkgnPicbQf-Zx9UFEXk3WGViapxkk0TzMcE2UU-8JyUtl22g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=lAOZu5aK5we9KiEJLlBFk9va4NBks9kleoTw2fmQ5kWN4R9LrC9mESjTcrxentYOhN7ooRdAz0reD562pA_EizjdXJGHsI1NebhB6xHj5uu4O_JXkngjN-vfgl2XJLfTfkEYqL81Hi4_a1aMG_oSGXAQ4qDKi--LcEGzQGhBXgHobUjZ7eiwpdyn0p8PrIgXuuhi97Kf7MEt3uQvokX4al01Lt6HfAIH8rIPTcu9BF1mXJEjoH79eEpb4mxTzAgccPjVweC5gYkaqed_WkIzqkRn15wm9CIjoWSHAirkgnPicbQf-Zx9UFEXk3WGViapxkk0TzMcE2UU-8JyUtl22g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، تیر ۱۴۰۳:
ما غنی‌سازی را ۲۰ درصد کردیم جنگ شد؟ ۶۰ درصد کردیم جنگ شد؟
hafezeh_tarikhi</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6159" target="_blank">📅 18:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6158">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ایران که ۴۷ ساله که در آتش فتنه اینها می‌سوزه</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6158" target="_blank">📅 17:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6157">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سخنگوی قرارگاه خاتم : هر چه در منطقه سالم مانده از نجابت جمهوری اسلامی است!
ذوالفقاری: «همه آنچه که بنا به نجابت ایران هنوز سالم مانده، یعنی تمامی زیرساخت‌ها در منطقه، زیر ضربات پولادین نیروهای مسلح مقتدر جمهوری اسلامی در هم کوبیده خواهد شد؛ آن‌چنان که اثری از آن‌ها بر جای نماند و گویی از ابتدا وجود نداشته‌اند.»
سخنگوی قرارگاه مرکزی خاتم‌الانبیا همچنین دخالت آمریکا در تنگه هرمز را «خط قرمز شکست‌ناپذیر» جمهوری اسلامی خواند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6157" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6156">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=DviT4azVpxFvlzZ6VQeFEGayEhZbqxwzPp3gxyB-06axri5Sfnn3XGlDSG6JlQVwx9jVKs9q9iHj_sCajolBHv9cExk18c6gNIhjn-UBDMh0Jt7lL064rRnuD2BZOgw_xwOLTSv9QYYoMdAl03ugD0SWLWD4ag05J9rSX4nK3xlluB6-e9Db043HXSg70houStFWj4OOOHZr9WGxGZ2BOQXKuyD10N9oabyl6qkQHmVFRaqUjk5Ojooo9QO6IN-lOBOA1atGn0a0xzsPECkq9Xuk51m1FHDRCtYZ2jPCXE-e4KFRJge_ToDyLlI6wmztvM1Ur1gYKaKSfuoIkn-lBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=DviT4azVpxFvlzZ6VQeFEGayEhZbqxwzPp3gxyB-06axri5Sfnn3XGlDSG6JlQVwx9jVKs9q9iHj_sCajolBHv9cExk18c6gNIhjn-UBDMh0Jt7lL064rRnuD2BZOgw_xwOLTSv9QYYoMdAl03ugD0SWLWD4ag05J9rSX4nK3xlluB6-e9Db043HXSg70houStFWj4OOOHZr9WGxGZ2BOQXKuyD10N9oabyl6qkQHmVFRaqUjk5Ojooo9QO6IN-lOBOA1atGn0a0xzsPECkq9Xuk51m1FHDRCtYZ2jPCXE-e4KFRJge_ToDyLlI6wmztvM1Ur1gYKaKSfuoIkn-lBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شب گذشته ج‌ا به اربیل در عراق
علی‌الزیدی نخست‌وزیر عراق با صدور بیانیه‌ای،
این حمله را محکوم کرد.
در این بیانیه آمده که «به آژانس‌های امنیتی
مربوطه در هماهنگی با نیروهای امنیتی منطقه دستور داده شده که همۀ تدابیر لازم برای ممانعت از تکرار حملاتی از این دست، و نیز مقابله با هرکسی که به‌دنبال خدشه‌وارد کردن به امنیت جامعۀ سرفراز عراق باشد را اتخاذ کنند».</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6156" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6155">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TsBA3yrbi7TNy9I6HNGpIpmDGYz3pKOYH4O3pEdVAAEUura9oIBQ3rPtev-qX8MmeeznGb2NYNFAflugevaAIQds_7vR_r06MIJ5ljSvFqRMBpMOCW6IAN-BTFwcPW5D6R3HhpGmsTHRJB2SrXUM8KtQfMng7Zpn4og1K0vjyc6qTCA5n4VolPmXuRHBXQduHOFg4A_oHMqjjkf93mm3GIyLVJD4SkoeiyJvA3pB6KAfI5wviDFxLozleh3iyyti9Cm3yuQyVLYEPnqQp5ULPcDDb3S9vtvL_TeBPTYIDI-pimAJarA4F_hm14Fy2frbeu3fYGc84_7zXRtdOFzt1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وراجی نکنید  بگذارید بجنگند که صلح بیارن :)  مثل صلحی که ۴۷ ساله در لبنان  ‌ و غزه آوردن!  انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6155" target="_blank">📅 12:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6154">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وراجی نکنید
بگذارید بجنگند که صلح بیارن :)
مثل صلحی که ۴۷ ساله در لبنان
‌ و غزه آوردن!
انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6154" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6152">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=e72xK25bdaRvo7JsMN3nXu2MePp2PNzc9JBj7i072H_KtI7IE4WcUdWW2sdvnRAi_agDqlV78VdJYPmva39fHYXNmgl84bHH6DBKGHTwNrP-kQo_rDHVrJrIG7i_VE6RWRzEyweuVp28es_5h2q7vPlCgf3YqZIXs-vdzVxpc5aWJ9df-3nka-va8asQlrSVSe6DCRF0fIdlXO4h-9ZPJf-2I9MtSn-bH525hCjJtVeCzWTGrHKkAmjM1F_zHiXYlKHtYkabSSHwvXeiLnljnfFJz_vpHSZfc9VQ0lSzPnu1PfHCwYxYBCAG5DQF8yemLPo80wRGreipt-mEkVmidCnz1NIV4nQxxst8UXcA4ANs4eNyD3w2bwmT9DHI94il9CVgNIN0om38_M95Ryshhlv3d7vBNxaFSHQYEnxR8dJFcJr9bolChLMSsJjRvbDbGPnQuIyz_-GLZ7XkaJ0lSy-lHcgOPW4Jek3sOXnIk0IpQVZP8snDolT9D3ehfuouP267z8jJQzRxSq-M98Ec2eBR0Xkui4BaNMcsYiOGAHL_8nWea1A-H_qj4oRKIoRo6Ud6P4_CpelOGM3C_v3nYB4HGNfPQohxu8MAbWCbdtnoxqiANJfFBQuhhkem2eVsW7oM4lBA9nS0wexdJTg2OB-YueiV8p46x8nG26rlSSY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=e72xK25bdaRvo7JsMN3nXu2MePp2PNzc9JBj7i072H_KtI7IE4WcUdWW2sdvnRAi_agDqlV78VdJYPmva39fHYXNmgl84bHH6DBKGHTwNrP-kQo_rDHVrJrIG7i_VE6RWRzEyweuVp28es_5h2q7vPlCgf3YqZIXs-vdzVxpc5aWJ9df-3nka-va8asQlrSVSe6DCRF0fIdlXO4h-9ZPJf-2I9MtSn-bH525hCjJtVeCzWTGrHKkAmjM1F_zHiXYlKHtYkabSSHwvXeiLnljnfFJz_vpHSZfc9VQ0lSzPnu1PfHCwYxYBCAG5DQF8yemLPo80wRGreipt-mEkVmidCnz1NIV4nQxxst8UXcA4ANs4eNyD3w2bwmT9DHI94il9CVgNIN0om38_M95Ryshhlv3d7vBNxaFSHQYEnxR8dJFcJr9bolChLMSsJjRvbDbGPnQuIyz_-GLZ7XkaJ0lSy-lHcgOPW4Jek3sOXnIk0IpQVZP8snDolT9D3ehfuouP267z8jJQzRxSq-M98Ec2eBR0Xkui4BaNMcsYiOGAHL_8nWea1A-H_qj4oRKIoRo6Ud6P4_CpelOGM3C_v3nYB4HGNfPQohxu8MAbWCbdtnoxqiANJfFBQuhhkem2eVsW7oM4lBA9nS0wexdJTg2OB-YueiV8p46x8nG26rlSSY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگر نوحه میخونن و مداحی و رجز خوانی و.. برای کودکان غزه و لبنان و میناب و….. از تاسف از دست رفتن زندگی نیست! میخوان در این جنگ بی‌‌‌‌پایانی که با جهان دارند،  از جمله و در صدر این‌جنگها،  با خود مردم ایران جنگ دارند، سربازگیری کنند! تا نیروهاشون بزرگ‌تر…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6152" target="_blank">📅 11:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6151">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">تمدن اسلامی! تا زمانی که توی مدینه و مگه بود قادر به ساخت «توالت» هم نبود!  مستراح هم نداشتن !! اما دنیا در چه وضعی بود؟  ۶۰۰ سال قبل از تولد اسلام!  توی بیشتر شهرهای جهان  داشتن توالت عمومی! اجباری بود!   اینها میشینن روی منبر  میگن «مدینه فاضله»!!  حالا…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6151" target="_blank">📅 10:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6150">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تمدن مصر باستان رو مطالعه کنید ابتدا تا انتهاش بر مدار مرگ بود! فرعون از زمانی که سر کار می‌ا‌ومد به فکر مقدمات مرگش بود و قبرش بود!  هنر و پزشکی و علم و مهندسی مصر همه بر پایه صنعت مرگ بود!  مومیایی و اهرام و جراحی پزشکی و….. همه برای کار و کسب مرگ بود و…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6150" target="_blank">📅 10:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6149">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3eAitnSBXzb3Xg687yVK0uOPbY5eVdVW26gFoe0Fz_8slGYwQ5SQ-6Q6e2yKJqInoJtA1D5gDFn6_V3RmyGg8cK8lmyJFXMYMvQAlL22-X030pHeceVRm466GgW6MJjZgHxrKyKrZ_93YHb2caCecYfJZ-pQvfeRlnq1sSoznGzfhxCjpAZKFNFRVJRrMD3seIr2DLDdVE2NIAQ91jUe9H2WGUYwIAOInGMgm03moof0MSzRZpNJgdIeWwE6CcN51RNVOyPomhPNeWGkRbK5Fufb_5PaPj7QHYHedEnxzUuftCEgxf2fbPv9tgOcMzmN12fPMdo2OSR3GbLFCUjUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها شنیدید جملاتی با این مفهوم رو که زندگی و این حیات «زندان مومنه»!  آرزوی اینها مرگه! مرگ براشون رهایی است!  اینکه برن و برسن به بهشت و به زندگی!!  مرگ رو آرمان خودشون می‌دونن و زندگی و زیبایی‌هاش  رو پست و حقیر معرفی میکنن!  و اینکه باید دائم به فکر مرگ…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6149" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6148">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..  سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند. و از مرگ متاثر میشن!  تمام هستی اینها :  مبارزه، جنگ، کشتن،  کشته شدن و….. است!  زندگی براشون چیزی نیست جز  «مبارزه  برای عقیده».  و خوشحال میشن…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6148" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6147">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=kYDGx8swTRs6otQ76O88qQhgcYtMjW7GV9vjSeqFvOYi9ydqKoE8NGUBeJ11ukayrUdJEak_am7tNcq8mjfI3PBYI_6WKFyHpxF3v1nLsv4F-v13khAtzj0VO1LrMalLq6CuCGIR5ZN13gEaeZ69bQMFOWlaUP5fwP3GrCX-QtSOxnlLvhp1pcHTAq7h7_Jr1N31jE1d30SWLUwZof8iWDoA-kibjnFFCovkzQhXegogFrA4aDnpzQ0GN1WcB8BiQ3jh65gGPzpZtYXOQXTAtdjNmcoIu26dzI1KmC1StI0Uh3SPvocRaIVjVghBRXcwdcGWkj4L297jyiUDBenVKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=kYDGx8swTRs6otQ76O88qQhgcYtMjW7GV9vjSeqFvOYi9ydqKoE8NGUBeJ11ukayrUdJEak_am7tNcq8mjfI3PBYI_6WKFyHpxF3v1nLsv4F-v13khAtzj0VO1LrMalLq6CuCGIR5ZN13gEaeZ69bQMFOWlaUP5fwP3GrCX-QtSOxnlLvhp1pcHTAq7h7_Jr1N31jE1d30SWLUwZof8iWDoA-kibjnFFCovkzQhXegogFrA4aDnpzQ0GN1WcB8BiQ3jh65gGPzpZtYXOQXTAtdjNmcoIu26dzI1KmC1StI0Uh3SPvocRaIVjVghBRXcwdcGWkj4L297jyiUDBenVKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6147" target="_blank">📅 10:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6146">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWnrtxWFzK9lu57tijE4pOcvn2ssr7RFJzlOq81IF7M5qVr_csbkvbLSat7V5NHw63FXWwojlBQVP6DW9wG6B4OUy29LVzit3GyvlLZFXyf4XJ63ao-eS4f0HN6v86v3gL0FJCEX-yIYoad_vUyIYTUerbtiDhuHd-0zr8MY-pdMk6hIqGdFiXsRXzk-Cpm0_q_oimA_-Cm7EAk-LLkUffXRyL8gqH6F7ap5sYGzh1pbLiOmo-dOD8ULrNg1_gdoEPxEdq0OTIZ63mfJZ7DEMAY02DH1JVvrES15cqWFstN5iHmDzvRlQoIP8krytUvIS6a8J-RJY2n0e9Whm8OE2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران به یک شهروند زن آمریکایی که در دسامبر ۲۰۲۴ در دوران رئیس‌جمهوری جو بایدنِ خواب‌آلود به‌ناحق بازداشت شده بود، اجازه خروج از کشور داده است. او اکنون در سلامت کامل در خارج از ایران است. ایالات متحده آمریکا از این ژست حسن‌نیت ایران قدردانی می‌کند.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6146" target="_blank">📅 09:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6145">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">استاندار مرکزی : شب گذشته به دو نظقه در اطراف شهر خنداب حمله شد.
این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقا مشخص میکند چه اهدافی را زده و نه ج‌ا می‌گوید به کجاهاش خورده.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6144" target="_blank">📅 08:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6143">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اطلاعیه  ارتش:  سامانه‌های راداری، سامانه پدافندی پاتریوت و مخازن سوخت آمریکا در پایگاه علی‌السالم کویت را هدف قرار دادیم.
‏ رادار‌های سوپر هاوک، تأسیسات و سامانه‌های پاتریوت واشنگتن در پایگاه شیخ عیسی بحرین نیز طی حملاتی، آسیب‌های جدی دید.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6143" target="_blank">📅 08:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6142">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
استاندار سمنان : به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6142" target="_blank">📅 08:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6141">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tpuqv0RzqXAZ8RGaWYXzKWJac-aCq5ZKaAxN1O6OdoyY9irm_hbT0BOQYhvEi2Bbql20IAYY0D9XTQPWOaX_iOtLRUvzcU5ND2ui1aTYMe-MtK6EyV5Bf8yYXqQ3ttsNW60HNQSHyE3iNRAP7Cz82FW_kbt8ZkOfZhx66SwvIWgPsqwieENbgFAHvPUjD6v16htb5nSKsVj7GyHtutmiIb62_mECki_3H5tvkKbJOjKbJUekGWGNoT2kALlzRu1prf3tGRjKZQWbFZj3zycdj08l--jJv84qk01IxuZPAESow9elBuF3Y3YJuvxPS9NJic0uKsOvg1UxS0PVS-ALuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین یارو خودش از دست سپاه و نهادهای زیر نظر خامنه‌ای  فرار کرده و به آمریکا پناه برده!
و آمریکا رو خونه امنی پیدا کرد برای زندگی و نوشتن از اینکه اسلام چقدر زیباست و خوبه و سعادت انسان رو میخواد!
حالا از همونجا به ج‌ا میگه مبارزه کن با آمریکا! مطلقا تسلیم نشید! تا انتهاش برید!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6141" target="_blank">📅 08:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6140">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">برخی گزارش‌ها از تداوم حملات به اهواز خبر می‌دهند و اینکه تاکنون ‌۹  انفجار  مهیب در شهر شنیده شده.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6140" target="_blank">📅 23:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6139">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
چندین انفجار مهیب در چابهار و بندرعباس
🚨
کویت : امروز ۲۱ پهپاد و ۴ موشک شلیک شده از سوی ج‌ا را منهدم کردیم.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6139" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6138">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای ۲ یا ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6138" target="_blank">📅 22:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6137">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JAXh5lxbd1NCmf0uttDIloAguYwpDnESaxBwSZcAYSKaOA7DbEIYcIStfjhvQVJqALr-9AfXma0cZ258H4T2iRjEW-cgyrvlXuSIMrq-qkV2t_M_396mvN73g2mUXWSP1TCS48gT-HHlQE9HyayXuks-bFA4s9FduqUybVVyhn1RKcfAuXlZQlN22UYNYN60uAYADDUuspxAzyRPlLtbf2FDnCXc-aSo5x1_4Cun480sHAxQ30R2h2gZ0bOwxDjZFKetJau8wfHheCKFdG901t1PSpZ3hEadPJECSQTtuvbamiopH1jYDrPHlSFdvpWEJ0mZv5EfhhXuXlxHLCl82w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آنچه شب گذشته در بمپور رخ داد و موجب  کشته شدن تعدادی ای نیروهای ارتشی شد، قابل اجتناب بود.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6136" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6135">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e615d142.mp4?token=qWoR9Y7IB9il5Nzno2FnYfPrD_PSsxBz35lw7AHVy62ucrEZ-ZsT8t78yP5C5gYI9UEn9V3ZKfzDpIPP4TrBcxpBM8jctOQlzR7wb3q0x-en_2W8pU6cFRaeLEX7CE4ArAmdyTV0nJsGkAW5P7bt27-utytfCMX_Bx1_2En7IrlMz17H6F1m-ZYPnh44VLX6KlX-Ac30o5HTL0DBhrNI_jwJiPbf7PFf7kvN0R038wgGTYBDJ8krOyTEoWp51jMpuoFpQvZ8-NvdTD-w5k028tlHR-pMp45JRKWhX3-uypdbYRx1Sk89BtOShiDFsVxRRtdcXCzGtKO4T4jRTgtl7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e615d142.mp4?token=qWoR9Y7IB9il5Nzno2FnYfPrD_PSsxBz35lw7AHVy62ucrEZ-ZsT8t78yP5C5gYI9UEn9V3ZKfzDpIPP4TrBcxpBM8jctOQlzR7wb3q0x-en_2W8pU6cFRaeLEX7CE4ArAmdyTV0nJsGkAW5P7bt27-utytfCMX_Bx1_2En7IrlMz17H6F1m-ZYPnh44VLX6KlX-Ac30o5HTL0DBhrNI_jwJiPbf7PFf7kvN0R038wgGTYBDJ8krOyTEoWp51jMpuoFpQvZ8-NvdTD-w5k028tlHR-pMp45JRKWhX3-uypdbYRx1Sk89BtOShiDFsVxRRtdcXCzGtKO4T4jRTgtl7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش بینی تاریخی بختیار
در دو کلمه، برای مردم ایران</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6135" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6134">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=jPsXPENGF9bp-Hu38f5fAHUgolg9a0dyhYIaVKxJpJvfm30g5gUEcWteN-hGxMPZFbbCzI0Yt85M8G2W-b9XglmT9_3THeaIJ6z0bs1GrF9JQ8xy5VbY6yguS754jmU7sE6-6x_VOZRf7CTZr4YqpFGh4DOcTtt8xT2LMPNo_8h2eK2hd4ZlyJo6pVExP3fneYLGjtJGOrYFXaGrTy858hY2CgFXbyTY0MfEX06bO-73AHS7Bt6Iu2Ikodq39YQipq_RcluDqaAALbyJZT19o7GA7ZdOiGxf_nZKLyqu9De2b9rb83nxsoqeEA77wyWhts9SlEqVqgD6fno2IuS1voi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=jPsXPENGF9bp-Hu38f5fAHUgolg9a0dyhYIaVKxJpJvfm30g5gUEcWteN-hGxMPZFbbCzI0Yt85M8G2W-b9XglmT9_3THeaIJ6z0bs1GrF9JQ8xy5VbY6yguS754jmU7sE6-6x_VOZRf7CTZr4YqpFGh4DOcTtt8xT2LMPNo_8h2eK2hd4ZlyJo6pVExP3fneYLGjtJGOrYFXaGrTy858hY2CgFXbyTY0MfEX06bO-73AHS7Bt6Iu2Ikodq39YQipq_RcluDqaAALbyJZT19o7GA7ZdOiGxf_nZKLyqu9De2b9rb83nxsoqeEA77wyWhts9SlEqVqgD6fno2IuS1voi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی که فرمانده سپاه بود و سالها فرماندهی جنگ رو بر عهده داشت
اینجا میگه مطئنم که مسیری که در ذهن مجتبی خامنه‌ای است، بهتر از مسیری بود که شورای عالی امنیت ملی رفت.
مجری ازش می‌پرسه خب اون چه مسیری بود؟
میگه : نمی‌دونم ! نمی‌تونم که ذهن خوانی‌ کنم!
فقط می‌دونه خوب بود :) یه مشت چاپلوس !</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6134" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6133">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbohsEc1Rjlh1EsSrgaeKNRyogjmU7biho5cHpVa1sW8Qlb2zIaqmEQYNkyPYLIuG0x020prk2pfqh4NvrwDCylGuO9rcLidnxLI3syjGQdrs14xmfpLqK37gKalBPLEdD09Us4esKf8U7Nz2PH2EP4WVLz_BH3ZUoVkjYsA7kWGHmcJPq2cLSt4XhUnG6P0srijhaNN9Q7YBsHIBfzhmEVTLt2v6hOhjvkG9vsuhwc2wC2u4KyO_MgSkZCsJc07AM9seOaPLC3tThGeIQ4JzJHwsPam8mDY-12ESw4vdHA5mdUi19CRR7JgVUTAtv792wIDmQ6vJyVJ3DXBYJ2nOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
سنتکام : به تنب بزرگ حمله کردیم.
در جریان این موج ۹۰ دقیقه‌ای از حملات، با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی و محل‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را مورد حمله قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6132" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6131">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">حمله امروز به چابهار</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6131" target="_blank">📅 14:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6130">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
ارتش: «آمریکا بامداد امروز با شلیک ۱۳ فروند موشک، آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور را هدف قرار داد
دشمن به مهمانسرا و اماکن نگهبانی پادگان حمله کرد
‏ ۷ تن از کارکنان پایور و وظیفه تیپ ۳۸۸ ایرانشهر شهید و تعدادی مجروح شدند.»
‏</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6130" target="_blank">📅 14:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6129">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
سنتکام : از نیم ساعت پیش موج تازه‌ای از حملات را آغاز کرده‌ایم.
(از  ساعت ۱۳:۳۰ تهران)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6129" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6128">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOqvKd2TZyMt338K3F3kPc9nv4yVVb_g5hjdl7U6KUIaBEg4Za8qa5tXl1ukiymvrsavZzwzl-ZWWwH3fClssxCcyvfCMEExFFW27cZSpXRJAtlDhNHAu8MuglWXO9G8Bqh_fae77XjW-GSYFiDLkgOqtx6MgbYTBOcPG8kSENEi-wTMKEUhCwx74s3NNk3mfBWofkJXiwq3yLVtqS4T-HLmO6JlV17LgVaNvOrKuGuJPu67Xb-kmq1Ka2GkjeJEAwQ0d1lSpRz4OmH6-wC35ipiCxuKBlNQUgc8VJLqzEv-bjpHjRt8GXYi29F_KcY7cHoKkZSrzqNZNRQ7NuIeeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابل توجه ساختاری‌های محترم
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6128" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6127">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=KLraFk8dm5V56PjAT5JdP52z3G3VM6JDFFatfUZ-tAToI6fLXNpWT6Qx4qEcfqt_gwD_z0fwVoG5lz9bweUHzo6D1UasIWd6WscVrohpOtLmdXhMlpKwijMaiqExtKS_FJ7391KzowjREvDshnmBewg0Tspq6mFGuqv5S8lwQCcC5hQ92Ov6WciAAr3ISkIYZ2yiULYlB4UX8VXmzUho8grroiYvitPki2YgWN7DHAz1tl9BtX4uNZWPuTiJXxyDT3U8qdX3ffgNJSnAgRYsEgurOLdbHcy6uE0vTiHKVUJ46EHIu87IG4ijHMkQ3aLH9EWGa2tCJCgnJRvaVaA6uiRDQyKDLyRP0C-lbKnas-8t_sJxjmB9uCVUGuPUIY2hyNFThsThY0Vc8II69tW6Egjg1yWxGiWHHz6ZhpwCec4IJ1l7WBGK5RBqknrAyMB7Iucz195pJK_UrptpZMTzkw5u8uIKtJ9_hAvSHxFVmV0iQhQ5osZdit8rZpkbQWpoO-C-4Izub4o6_FKtGQAJdpZtPgOYh3f8f6T3vGfslngo8mMkEuMxD52y7GVqZMjzoyECMR_-0sWo_uElnb-wbbdmB6aOylkSbk3HZ7A36JIPFZmZNd57dPox9b4cfKsL7057cvdkUxKiitG-G_Gm2F6xaQNS9qbfGakEJdilKJI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=KLraFk8dm5V56PjAT5JdP52z3G3VM6JDFFatfUZ-tAToI6fLXNpWT6Qx4qEcfqt_gwD_z0fwVoG5lz9bweUHzo6D1UasIWd6WscVrohpOtLmdXhMlpKwijMaiqExtKS_FJ7391KzowjREvDshnmBewg0Tspq6mFGuqv5S8lwQCcC5hQ92Ov6WciAAr3ISkIYZ2yiULYlB4UX8VXmzUho8grroiYvitPki2YgWN7DHAz1tl9BtX4uNZWPuTiJXxyDT3U8qdX3ffgNJSnAgRYsEgurOLdbHcy6uE0vTiHKVUJ46EHIu87IG4ijHMkQ3aLH9EWGa2tCJCgnJRvaVaA6uiRDQyKDLyRP0C-lbKnas-8t_sJxjmB9uCVUGuPUIY2hyNFThsThY0Vc8II69tW6Egjg1yWxGiWHHz6ZhpwCec4IJ1l7WBGK5RBqknrAyMB7Iucz195pJK_UrptpZMTzkw5u8uIKtJ9_hAvSHxFVmV0iQhQ5osZdit8rZpkbQWpoO-C-4Izub4o6_FKtGQAJdpZtPgOYh3f8f6T3vGfslngo8mMkEuMxD52y7GVqZMjzoyECMR_-0sWo_uElnb-wbbdmB6aOylkSbk3HZ7A36JIPFZmZNd57dPox9b4cfKsL7057cvdkUxKiitG-G_Gm2F6xaQNS9qbfGakEJdilKJI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سفیر اسبق جمهوری اسلامی در روسیه: مطمئن باشید اگر ترامپ را بکشیم نه تنها هیچ موشکی به سمت ما شلیک نخواهد شد، بلکه عقلای آمریکا با خوشحالی جنگ را تمام خواهند کرد.
کشتن ترامپ هیچ هزینه‌ای برای ما ندارد و با کشتن او جنگ هم تمام خواهد شد.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6127" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6126">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟  به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6126" target="_blank">📅 08:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6125">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrqeLbKwyJzHhIZK_qIRc1IwJPnfLFAgGfaxRBOT8aQYvvWGXNXXwhCZDvLM_fZ5RrYYW0IIXEE_n1Sp3HDnSTcFwYDYqkt-6abBT9YwxHnASLagYpsfq89GTDCr8PjvJgCzcquEfR5t0E4x1-jclANgWyu__N950uuLfngMf1gIA3rKIHp1rw6gQmBg4coaYFCKXjjBndz-UPvQ702xdIE3T6fvxV4YORA6vWBg0MuUjVjg20PBf2wKnLYEmeW447xWfZk551M8b_Cx9F_NiWgB_3SeFpiG1pfM6uK3vUoFm1ohOuNjcCok8nn9f_yaNm3-cm0eENKKEXCDf3ZvNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟
به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت کاخ سفید برگزار کرد.
به گفته سه منبع آگاه، در ابن جلسه که ارشد‌ترین مقامات نظامی و امنیتی آمریکا در آن حضور داشتند در خصوص گسترش حملات صحبت شد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6125" target="_blank">📅 08:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6124">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=ftzrVPCGUjms8upJYiWhbV53NCWlmh2E6IG6fZ_NW_OHHTjKLiKddKaFZS99j6g-r_GeKAOdaFpUjuNia7HtL-_vsGMTnC4_4RaFub23HtHQdJP_nbsR6JLDoJPdY8zQOZGfPjBflU3MR87JAZQm_z3Fn3ctAO2E5FGjNGkpnYvTYmApLoFQ1JK8BV9TT8lj_eBpMukV9vciPrvbI-3ukFeDj2_KtzErZaI6mqchhW0qTtEB_-2ykwLKpGpe-w_nobY5GrhEerDGWtt3o-90mStvZXNdBy9ibX2QxfuFa5y4AxTqAK_1uynFRLBquSUUrNtfiQSxM1-rTGOhFV7AlX4seMKMU45mRtVjCKYM0sNuRRSfeUC7WnFt0ZVEAmjnnRREYV_LPrC6wtR9adIRCTf_zaWpw6yHLf5u8OIFsZNHJCh2yQSr_Oo5J_mLCuGnrwNZxlvQ_BKoNoNVQVeDIg0FoE3OhbEd0WWDXPlHt8acJ6lZeECk-QP-ivohIyif_W1I-GzXOJ2QjUDS0-nKHIoTRp61o7hWwxC2-ir8JwSRcMoAK2N-fUh2IDg5kHMkMG8oigqMRI7M0kymEArNoVOzFLTeYHoFf9T_ET25Aexe6fBqRF3Z9LKAopilO5ahWdts-AqhJdp12Abw7kt5ItKtWwRkXNsQ0V6Tww_8K7o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=ftzrVPCGUjms8upJYiWhbV53NCWlmh2E6IG6fZ_NW_OHHTjKLiKddKaFZS99j6g-r_GeKAOdaFpUjuNia7HtL-_vsGMTnC4_4RaFub23HtHQdJP_nbsR6JLDoJPdY8zQOZGfPjBflU3MR87JAZQm_z3Fn3ctAO2E5FGjNGkpnYvTYmApLoFQ1JK8BV9TT8lj_eBpMukV9vciPrvbI-3ukFeDj2_KtzErZaI6mqchhW0qTtEB_-2ykwLKpGpe-w_nobY5GrhEerDGWtt3o-90mStvZXNdBy9ibX2QxfuFa5y4AxTqAK_1uynFRLBquSUUrNtfiQSxM1-rTGOhFV7AlX4seMKMU45mRtVjCKYM0sNuRRSfeUC7WnFt0ZVEAmjnnRREYV_LPrC6wtR9adIRCTf_zaWpw6yHLf5u8OIFsZNHJCh2yQSr_Oo5J_mLCuGnrwNZxlvQ_BKoNoNVQVeDIg0FoE3OhbEd0WWDXPlHt8acJ6lZeECk-QP-ivohIyif_W1I-GzXOJ2QjUDS0-nKHIoTRp61o7hWwxC2-ir8JwSRcMoAK2N-fUh2IDg5kHMkMG8oigqMRI7M0kymEArNoVOzFLTeYHoFf9T_ET25Aexe6fBqRF3Z9LKAopilO5ahWdts-AqhJdp12Abw7kt5ItKtWwRkXNsQ0V6Tww_8K7o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=Tyde9AYdLClPxk7ZrZ_9RQKay3epmj2M2d-_fSXJxKN6mWGTjmi96pPBZKRnqFlwQfq3s1rO9-p5ytLVOYYwWDr1t1EDD2hhl5WLFwSr5sOvvd84g8Ll36te6QEwSJ213-TTMapdSqh__9sgo2ZZPBJa26yYhJ9neS-8XOkoyW7K0wIV6WnPa-lY_2TF6ASREpjeAv1jKx3udWDRcVdfpQcZL-guS8aMN7xMvPTCge7V7HHk01A70GBEOVuOthegl28XpW91FD8el9nFKOXgcNcuO68f-PFuP_kYBd0YvgHGLqjQ45Vc6KLsB_dXDxpj-kvzH3x_DolieHCVjvNJGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=Tyde9AYdLClPxk7ZrZ_9RQKay3epmj2M2d-_fSXJxKN6mWGTjmi96pPBZKRnqFlwQfq3s1rO9-p5ytLVOYYwWDr1t1EDD2hhl5WLFwSr5sOvvd84g8Ll36te6QEwSJ213-TTMapdSqh__9sgo2ZZPBJa26yYhJ9neS-8XOkoyW7K0wIV6WnPa-lY_2TF6ASREpjeAv1jKx3udWDRcVdfpQcZL-guS8aMN7xMvPTCge7V7HHk01A70GBEOVuOthegl28XpW91FD8el9nFKOXgcNcuO68f-PFuP_kYBd0YvgHGLqjQ45Vc6KLsB_dXDxpj-kvzH3x_DolieHCVjvNJGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6123" target="_blank">📅 07:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6122">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=inZpjYtKVw43WBM_OMTSi2xq-HIgLvz1aeM0hkGkTXuHLunCjgSJ7y-YJUbnu5y2py2DyI8eSFPSyw5cS0baKb0ag21BKdUvm-XrrHYSh9seOWmOinyl9hp5B7dEz3DVAOi26a-HNJfBHrTYxO0XPfmBU7rf0qMX2jp4JrkT6J0ob25pJkLRUf8iHgoNcQtCWSLLxobd-wX9AxcrTrb-fzco1ceM7FWf8gyme-uT5a7em8iW-7qkj3xH4FjgjSJD_1weMyTftgoOb32VjMAa_YHgmwrCRX6_P2jlnSVRBQrjEfm5b-2w1otgikmRaWgauCxbDaNGgd1jxzl4WSk6vbr3NGIVdLGEZrStrui2aQybpRL3avaZ2txMM1YvkCirtdbc8-SBX1bBgkjH-1ehqZsNADqjr23LOe9ivmh0nioouNA9qLr5gKKqiuVu0KGOZMbYJCT3X2U7lNDVQrjNdUxyMGcy-YPvXrCxOXYGkxpggGJnyoz3SDfNFyovxdYJ-tpvjzP4N2gIKVVNEA2dScpKjXFep6HvT4vnya-DxMLfog1TByUheTUihvhwSGEi1lAI5vycyTyMQTIzfB2Oxowx22fsA9wo-TRiJZgDGnsPN3u2jFkQSxRWaaQjdLRLdKyxsMIN45veAGde0othnQiHdDhByDlxerGYabJR6E0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=inZpjYtKVw43WBM_OMTSi2xq-HIgLvz1aeM0hkGkTXuHLunCjgSJ7y-YJUbnu5y2py2DyI8eSFPSyw5cS0baKb0ag21BKdUvm-XrrHYSh9seOWmOinyl9hp5B7dEz3DVAOi26a-HNJfBHrTYxO0XPfmBU7rf0qMX2jp4JrkT6J0ob25pJkLRUf8iHgoNcQtCWSLLxobd-wX9AxcrTrb-fzco1ceM7FWf8gyme-uT5a7em8iW-7qkj3xH4FjgjSJD_1weMyTftgoOb32VjMAa_YHgmwrCRX6_P2jlnSVRBQrjEfm5b-2w1otgikmRaWgauCxbDaNGgd1jxzl4WSk6vbr3NGIVdLGEZrStrui2aQybpRL3avaZ2txMM1YvkCirtdbc8-SBX1bBgkjH-1ehqZsNADqjr23LOe9ivmh0nioouNA9qLr5gKKqiuVu0KGOZMbYJCT3X2U7lNDVQrjNdUxyMGcy-YPvXrCxOXYGkxpggGJnyoz3SDfNFyovxdYJ-tpvjzP4N2gIKVVNEA2dScpKjXFep6HvT4vnya-DxMLfog1TByUheTUihvhwSGEi1lAI5vycyTyMQTIzfB2Oxowx22fsA9wo-TRiJZgDGnsPN3u2jFkQSxRWaaQjdLRLdKyxsMIN45veAGde0othnQiHdDhByDlxerGYabJR6E0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا میبینم راست میگه …</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6122" target="_blank">📅 07:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6121">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgdYMak9UBeT_iKcKPZgPreoHrcQtsNK-TjKfSxdIKktI3NAlvHX1pC-vhXn0sXRWJocrmJOxca2M8f2EZqJyBYAbfuoMGURkUKZ-jhtfePijwfe_7-x0vSjsGZqDT7hIVgcxfYsqFiTX98_I3tHZm7y3PS6tDisXuX4R-VWsuQFFsQp6aVzrfHRKPfjPPBzPaxYqgTpmRg6cQ40qZcxFqZMnvZA6ev2ht5wUfrj2E4IjDvFLAN6RYM16NLgtaJQDptLcfbL06j2rsX4YRp9mIL4Hde0wwifTJ9V7jgabqM4UxVTuXOX-WP3TjD6S9_YVzjwdbq-e7HhiKc8MI9JwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6121" target="_blank">📅 06:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLsGyXHOjGRFK8eDr7JIEFedj4lY82Xs1VdQMh5u5xSWQzD1JXCqLvz2KWkP2Q19wHz9b4Ox0rKzmvappKVvbZ_wlGMGLU8SJgzpUWNB1FnfU8NBqrb-kHtgluBebmpDtX89Sta-vTsoaz6vAqLPkOIG9gLYwh57Y7ddvfYmtvlCNiKRKSYnQ9MmiLykcO4O9eJ46wcXEFVdmLoO9BR6HDuYTqyUIu31orOC12DgIm_wxHa1Z3zQVBrjHjteETDqsQmdUTqXgNxUWNzyp454-vImajS8DzK9IrZ2gVAhIewvn9W87PqfVRADrZjPY_Fv78L6uA1mRCqJWN-QtrIxLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6120" target="_blank">📅 06:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6119">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=nQP27tOIV0s52orvycY5Zag4wgpXFuxvrbPlxin3PZxekwzpjuAhVf1ltUcM_CKJwKIGC2VZ8ZF_TdXIQmz3kfPF2KCPwsv2e2Q8tcDQ40Tk98Ir5aUrQPHjBDQIao5KOvKquHmiQtrIr7YUFmSymjiIeiIJkr1y6YyHEQV03bkm9uq1DAY17ah0OFSHNhMd8rwYBcRKk14z8QnleyL_EAI1NowNQRZnxHWqKc3GLEZdTKepAkOkqroLs6oa0L_6w5hk2gE1mUaC0lS8WPSGvIeZ9yKBSLkzzuE0h6txmcrXdvSUfyEV_ypUEv9Bag4VWcaWnC8bJseUD_urXEfVaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=nQP27tOIV0s52orvycY5Zag4wgpXFuxvrbPlxin3PZxekwzpjuAhVf1ltUcM_CKJwKIGC2VZ8ZF_TdXIQmz3kfPF2KCPwsv2e2Q8tcDQ40Tk98Ir5aUrQPHjBDQIao5KOvKquHmiQtrIr7YUFmSymjiIeiIJkr1y6YyHEQV03bkm9uq1DAY17ah0OFSHNhMd8rwYBcRKk14z8QnleyL_EAI1NowNQRZnxHWqKc3GLEZdTKepAkOkqroLs6oa0L_6w5hk2gE1mUaC0lS8WPSGvIeZ9yKBSLkzzuE0h6txmcrXdvSUfyEV_ypUEv9Bag4VWcaWnC8bJseUD_urXEfVaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام فیلمی از حملات خود به ایران منتشر کرد.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6119" target="_blank">📅 06:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6118">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=ggri2RA9d-oLUvkuxDMkTM9XIM8nVBKwZmbnwQCeQoz_kIwvGoS8zBgzYD9cQ8jrF2eKlLMjsIOW66l5NNnWAyylESwNw5Kvz90Q7oBaSXXviZh7ytvUqrtLdIdsF6d6xSf992WM9UnacyecYbzL_pbL0N_DVxlNe7v_iEoZvmtKd59NPfrlcGCWOwqYFAuZLXLWtAt4wv9IA1Tq9Nk8wswWJkshCZEfF1qkpLCVENfRTQZGek6PlB_aM6FTh1s43Fvq_TN1VuakheXnNI-4ynjgLyegEtXedfdjkaVOi1pURgg64enjM4PW_7TB_1gxMfb2iqZ4U4MJYcRxpZSTfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=ggri2RA9d-oLUvkuxDMkTM9XIM8nVBKwZmbnwQCeQoz_kIwvGoS8zBgzYD9cQ8jrF2eKlLMjsIOW66l5NNnWAyylESwNw5Kvz90Q7oBaSXXviZh7ytvUqrtLdIdsF6d6xSf992WM9UnacyecYbzL_pbL0N_DVxlNe7v_iEoZvmtKd59NPfrlcGCWOwqYFAuZLXLWtAt4wv9IA1Tq9Nk8wswWJkshCZEfF1qkpLCVENfRTQZGek6PlB_aM6FTh1s43Fvq_TN1VuakheXnNI-4ynjgLyegEtXedfdjkaVOi1pURgg64enjM4PW_7TB_1gxMfb2iqZ4U4MJYcRxpZSTfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : امشب، فردا و فرداشب به سختی به آنها ضربه خواهیم زد و هفته آینده پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد، مگر آنکه  مذاکره کنند.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6118" target="_blank">📅 06:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6117">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caeb092620.mp4?token=LJRl2lXFgbbTxJrTxaDVjwWHAzpWH4xQD0USICRFy3N7vUWCh6wuKcJBHagrxfODM6NXjtq6se03uyEGSZFz8dIRcEVpW82_r2TOJ1EWxjT850rxJNVRrVk-tPzrgO-7DgNgRfTIjwBzt8V-vB0qI1ei5VJbaPMnYCyl3p2lEn5ykXMS5N_9Zsi7cezYjpHAtx2bx83dI9iRYMgP-2SsptjFZCOO20wnAGEyJxav7sIWv7AGhNWoqwCMysKSsDK4O6gtCPXnt8aPDOMp00xInYAD-0ZJRe7j7weoTCnGcIHCNvKZS9zjg9izkMReJ2B0ms8YW62Aaix81dhnjULYXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caeb092620.mp4?token=LJRl2lXFgbbTxJrTxaDVjwWHAzpWH4xQD0USICRFy3N7vUWCh6wuKcJBHagrxfODM6NXjtq6se03uyEGSZFz8dIRcEVpW82_r2TOJ1EWxjT850rxJNVRrVk-tPzrgO-7DgNgRfTIjwBzt8V-vB0qI1ei5VJbaPMnYCyl3p2lEn5ykXMS5N_9Zsi7cezYjpHAtx2bx83dI9iRYMgP-2SsptjFZCOO20wnAGEyJxav7sIWv7AGhNWoqwCMysKSsDK4O6gtCPXnt8aPDOMp00xInYAD-0ZJRe7j7weoTCnGcIHCNvKZS9zjg9izkMReJ2B0ms8YW62Aaix81dhnjULYXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ناشی از حمله پهپادی امشب سپاه به کویت
گفته می‌شود مخازن سوخت ارتش آمریکاست.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6117" target="_blank">📅 06:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6116">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360d24e506.mp4?token=kEm-LwCM6nIAQiGulvVNAyfS0B9l30OZUYLVcQZ57pKVZAiPUDgOgCoSsBcdef7THL1WK75RPfpjUnOgPXFT0PRPxQuWllLQO_EDCibTZx6ZiquzJydwl5tQiEt0lH5dAuj0C-P6DtO1cdW0m7pMlyIawr6myO13j9PvVyX__h-ryriTk4-L9BdNJlX-RJmFjeenh7TZqtXk3lZULxAg0k26PMM9u0b8ljMSa0mSQ8xI1I3Bg9cue5AaKjJLvBCzboZ5f6WCg8b8bNCcpSbxUUp_vqmPvl9pU2hkCKdeEa6D8vLU0HjdnO5-WlPhOYZN05nnH_s-RXrRD25--TQJBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360d24e506.mp4?token=kEm-LwCM6nIAQiGulvVNAyfS0B9l30OZUYLVcQZ57pKVZAiPUDgOgCoSsBcdef7THL1WK75RPfpjUnOgPXFT0PRPxQuWllLQO_EDCibTZx6ZiquzJydwl5tQiEt0lH5dAuj0C-P6DtO1cdW0m7pMlyIawr6myO13j9PvVyX__h-ryriTk4-L9BdNJlX-RJmFjeenh7TZqtXk3lZULxAg0k26PMM9u0b8ljMSa0mSQ8xI1I3Bg9cue5AaKjJLvBCzboZ5f6WCg8b8bNCcpSbxUUp_vqmPvl9pU2hkCKdeEa6D8vLU0HjdnO5-WlPhOYZN05nnH_s-RXrRD25--TQJBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی با موشک‌های حاوی بمب‌های خوشه‌ای به بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6116" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6115">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
ارتش : به پایگاه‌ها اف ۱۸ های آمریکا در اردن حمله پهپادی انجام دادیم.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6115" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6114">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‏امشب اتفاق جالبی افتاده، به محض اینکه خبر انفجاری در شهر و استانی منتشر میشه، مسئولان جمهوری اسلامی سریعا مصاحبه میکنن و میگن دروغه و همه چی آرومه!
‏اینطوری مثلا میخوان صورت مسئله رو پاک کنن.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6114" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
