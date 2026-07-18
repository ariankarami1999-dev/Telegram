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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 13:40:51</div>
<hr>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMDpU9RJwLRRIjiRFMe0sGJ3NrwrmFdf2PfehFhmkdXqUh-dZJS_E229LfzdyMaOgy__n2N-JtFFAEKxiJHxU07MjYQL-ujO_Om42sPD9XMZXePkqNIMnH_x1YeKoHKrYmxRoNWawoVOUQSOqfzO7JiMF5l5im618mLB3u8laqzuY4FIRiFJx36XnU-NvlIf1ylK1qUwWf3mPplnauoYo6UMMY5MW0w9QRy3yZ0cleH9azRFQvZ82H4EIsU4fhxoNf2H0l8M43rAUmmTPqhhaFYMEdqrCHRYDbIa62iV1JaZj81A9S_BT_Ab6SNGVI8lX6NxdkbSBAEtWJ2vTXGJcAZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMDpU9RJwLRRIjiRFMe0sGJ3NrwrmFdf2PfehFhmkdXqUh-dZJS_E229LfzdyMaOgy__n2N-JtFFAEKxiJHxU07MjYQL-ujO_Om42sPD9XMZXePkqNIMnH_x1YeKoHKrYmxRoNWawoVOUQSOqfzO7JiMF5l5im618mLB3u8laqzuY4FIRiFJx36XnU-NvlIf1ylK1qUwWf3mPplnauoYo6UMMY5MW0w9QRy3yZ0cleH9azRFQvZ82H4EIsU4fhxoNf2H0l8M43rAUmmTPqhhaFYMEdqrCHRYDbIa62iV1JaZj81A9S_BT_Ab6SNGVI8lX6NxdkbSBAEtWJ2vTXGJcAZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرهای جمهوری اسلامی
و کودکانی که تقاضای «سر» دارند!</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/farahmand_alipour/6215" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=SA-ntt700ZS27ZCnM1PiNsSePDF1axiFbA03JQFfuaOFqWbyyduRyJTtvqya6-H_Z2K7Oamjar4eZklB1QYQc1pvzsTYdRRn02OXfu8lGftKP99uxl26qkvGdX4ytjBpPklrMa3iy070vdyymHFQ2XG2_bGxhp2uSOXrdJmxMh-eLRD79ygeqrL4Me-9IXcWlaflbsFKgCxCKD_I1lBAnngVC616ufdZKt10cqluQBVDfTuzWhIyqV6Y1CMcy8rTJ4QmwlXFeD8GzdMs9LqfboKXAGxYXkORzO84M8JnySM7m_xJ_lyOTyfWJNVUd_pdyAOVagjTyOKiLqEBtsRlfnTUMe4EHaZZg0CqEXQQfyLuCO5IBoC4m4wdRp6uvEe-1-NbXyXAEWB9YIr45kM2ghDUvDRsYoeVom8_QfmwwnVsNdWRAB2lDx06huN7TkB_fhs7ajraVrqpKbat8Ii8SFryd6scxlZ9IT3mxPvGERisSB4OBx_sMey9D-STkndV1oetOIxpvdEWcj_R6a16uT4rHf31HvNV1_Lx0mpk23laoPUho1MIy7AxkokUxN_dJ4BOB3BWkNPOcCQH7m-d5JB4h0_RqzT-BExyeWPDqFH6Tp45ZI_nA_xTLUvRCw2kZ6ErDvT4e87g1ilxRoGxbkkEXelBAR07n0ynm7z5d4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=SA-ntt700ZS27ZCnM1PiNsSePDF1axiFbA03JQFfuaOFqWbyyduRyJTtvqya6-H_Z2K7Oamjar4eZklB1QYQc1pvzsTYdRRn02OXfu8lGftKP99uxl26qkvGdX4ytjBpPklrMa3iy070vdyymHFQ2XG2_bGxhp2uSOXrdJmxMh-eLRD79ygeqrL4Me-9IXcWlaflbsFKgCxCKD_I1lBAnngVC616ufdZKt10cqluQBVDfTuzWhIyqV6Y1CMcy8rTJ4QmwlXFeD8GzdMs9LqfboKXAGxYXkORzO84M8JnySM7m_xJ_lyOTyfWJNVUd_pdyAOVagjTyOKiLqEBtsRlfnTUMe4EHaZZg0CqEXQQfyLuCO5IBoC4m4wdRp6uvEe-1-NbXyXAEWB9YIr45kM2ghDUvDRsYoeVom8_QfmwwnVsNdWRAB2lDx06huN7TkB_fhs7ajraVrqpKbat8Ii8SFryd6scxlZ9IT3mxPvGERisSB4OBx_sMey9D-STkndV1oetOIxpvdEWcj_R6a16uT4rHf31HvNV1_Lx0mpk23laoPUho1MIy7AxkokUxN_dJ4BOB3BWkNPOcCQH7m-d5JB4h0_RqzT-BExyeWPDqFH6Tp45ZI_nA_xTLUvRCw2kZ6ErDvT4e87g1ilxRoGxbkkEXelBAR07n0ynm7z5d4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرنوشت ۹۰ میلیون ایرانی افتاده دست این جماعت  متوهم</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/farahmand_alipour/6214" target="_blank">📅 13:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!
در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.
این بار اما آمریکا از عنوان عملیات هم پرهیز کرده و به نوعی داره با سر و صدای کمتر، این جنگ رو پیش می‌بره.
رسانه‌های بزرگ آمریکایی هم  گرچه اخبار این «حملات» ۷ روز اخیر رو پوشش میدن، اما نه با شدت و هیجانی که اخبار جنگ ۴۰ روزه رو پوشش میدادن.
شخص ترامپ هم از  هر ساعت توییت زدن و تهدیدهای درشت، فاصله گرفته.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farahmand_alipour/6213" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fztRn2exidVShVS38-afA4hxkjC4LotutVqLbGDBvFUvD-29nZBP9JFyCL7UCGcECfGprImzN33WwgCoIPaSW2FuWVHFTWO2fKfDxp9AVxzBIzCt500bsZJTSCHWpOZGfxkCGA0ik7Jwq6bibYBtJX2872sSZ-qaWjTfiEts0Mrx1c8KG4JWUTrF7uuHiuQJKCz0DKYc2o9vRNnFAir2jPixfsvHsoZ2N8574OPlUdxL1cYWz-NNBQrElRsrczAoImUHWhG1c0Aj9WSDexb8ANzEOrVbmXwEnKgwwH6mhXcSmGjO5uIv_xJbfqaoxZ_6VWVsl5a-JveZLMFsYCaGOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه : در حمله به اردن حداقل ۲ جنگنده و ۳ هواگرد آمریکایی را منهدم کردیم!</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farahmand_alipour/6212" target="_blank">📅 12:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یه مرد هندی دیده یه تیکه یخ توی فریزش شبیه فرم مجسمه «شیوا» شده، یکی از خدایان هندی! رفته به همسایه‌ها گفته، ملت هم اومدن دعا و نیایش و اینکه این یک نشانه است و بردن غذاهای نذری و…..  :)
شیر، شیرینی، غذا، میوه و..
صبح یخچال پر میشد، شب خالی میشد!
و مرد هندی میگفت، شیوا، نذری‌ها رو پذیرفته.
در عوض مرد هر روز چاق‌تر میشد
این داستان‌ها براتون آشنا نیست؟</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6211" target="_blank">📅 11:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">💔</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6210" target="_blank">📅 10:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f27e890899.mp4?token=XuUOyura1PqFICYpN--FoDRvfugu2kZEVs2wn6ENQM2A_6TI2ExhizW7T2CiUht3FwzNzB82imwOhFOZUHd-55Jgbb5a6SMeV_PZUyMd2p55j1Px8FmxT_miJfNfetEJcvW6h7YpwMYuZ8Ia-czCSjQWZHSQ7OrjQIJ4U-ecQwCl-YTabn5IAusER03XdhzQQi6oryj0eY129E0IjLjDX5IT4pK1F4n85LTpcNSNEuauyLstLZVpo8AAHrvpTPYsynfFl7nIuCxH7FrjKHXTnj-uCceCIjzAMhkLSZ10JeKfnn_hRfJ0I2EKFQApnCwPe0osm-5aQNayy31ysY1eSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f27e890899.mp4?token=XuUOyura1PqFICYpN--FoDRvfugu2kZEVs2wn6ENQM2A_6TI2ExhizW7T2CiUht3FwzNzB82imwOhFOZUHd-55Jgbb5a6SMeV_PZUyMd2p55j1Px8FmxT_miJfNfetEJcvW6h7YpwMYuZ8Ia-czCSjQWZHSQ7OrjQIJ4U-ecQwCl-YTabn5IAusER03XdhzQQi6oryj0eY129E0IjLjDX5IT4pK1F4n85LTpcNSNEuauyLstLZVpo8AAHrvpTPYsynfFl7nIuCxH7FrjKHXTnj-uCceCIjzAMhkLSZ10JeKfnn_hRfJ0I2EKFQApnCwPe0osm-5aQNayy31ysY1eSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از پل‌های غرب استان هرمزگان</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6209" target="_blank">📅 10:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6208">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!  این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6208" target="_blank">📅 10:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6206">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان می‌گوید که چند موشک به تاسیسات برق و پمپ‌های آب‌شیرین‌کن مستقر در اسکله روستای بونجی در جاسک اصابت کرده است.
گقته می‌شود که این آبشیرین‌کن، آب حدود ۲۰ روستا را تامین می‌کرد.
🔺
شب گذشته کویت نیز اعلام کرد که جمهوری اسلامی همچون پریشب، به یکی از تاسیسات آب شیرین کن این کشور حمله کرده.
🔺
ارتش اردن اعلام کرده است که سامانه‌های پدافند هوایی آن کشور ۱۰ موشک ایرانی را که وارد حریم هوایی اردن شده و خاکش را هدف گرفته بودند، رهگیری و سرنگون کرده‌اند.
🔺
ارتش جمهوری اسلامی نیز با صدور بیانیه‌ای از حمله به پایگاه آمریکا و چند پل در بحرین خبر داده است.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6206" target="_blank">📅 09:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6205">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
وزارت آموزش و پرورش:
🔺
با توجه به استمرار شرایط ناپایدار در جنوب کشور، آزمون های نهایی تمامی رشته های تحصیلی پایه یازدهم و  دوازدهم در روزهای یکشنبه و دوشنبه،  ۲۸ و ۲۹ تیر ۱۴۰۵ صرفاً در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می گردد.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6205" target="_blank">📅 09:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6204">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=EQDqqUnmmainNW4tviUqMqoTQmCtCnAcytNt7YAFLSWRrA1ORHLYBc1GNW9hBgsIyYLMTR5IBxu6PXQciTqnEBnx147Lce8ij6qdUPeM9sOWsPJO-p4bYpFIRZDirBGhlXUVwU5CuxNkLWPVcaPFCB46Bc4evjZtNBH-OLdEk_nm_MxYANz3pkxKur017LU_7r8Lv3vIuS3tGrg0sLGq2zfrqQFh1FLI7LQ1p1nEeRSTYyjGMGatLTIhjn-05X7a9XC4vQGszGAzH6Q8R09tuFBnT5BWVY8TBvVRaHitBP6Py9AkDQ3lbek3qXjPuCTR7jwKl6vovs6XVlzNEI2rYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=EQDqqUnmmainNW4tviUqMqoTQmCtCnAcytNt7YAFLSWRrA1ORHLYBc1GNW9hBgsIyYLMTR5IBxu6PXQciTqnEBnx147Lce8ij6qdUPeM9sOWsPJO-p4bYpFIRZDirBGhlXUVwU5CuxNkLWPVcaPFCB46Bc4evjZtNBH-OLdEk_nm_MxYANz3pkxKur017LU_7r8Lv3vIuS3tGrg0sLGq2zfrqQFh1FLI7LQ1p1nEeRSTYyjGMGatLTIhjn-05X7a9XC4vQGszGAzH6Q8R09tuFBnT5BWVY8TBvVRaHitBP6Py9AkDQ3lbek3qXjPuCTR7jwKl6vovs6XVlzNEI2rYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مسیر ترانزیتی بندرعباس - سیرجان که در ادامه این مسیر به تهران وصل میشه.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6204" target="_blank">📅 09:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7U6VgsmWc6M0-vWa9P2SnAMmQ9Gp16g3XE_5UurUNL4IlTlKSRx-pA0V2WLJXDvF1OQQbYl0Fv6lL6vOjD_knC2Qm8xTG7d4EK2qW9viZqtLaUEsk-a3hRKaHsOoGZaiNt-sq2QeEwGRYlUGzG2JVLb9e_0ITB_ZUsBUDyfcOujpvBUAeOAwDAXKbaN-_0Khaqt-tzTRyevu3MxYUL79MaOA3o5d5tJGRGpeg5vSv_T1tZW2EYVVpUTpWzPcMtVrZqMIlODJNbm4A0EBvxRHor3Xrbhn4wpJnO6EARVCApNvIoR3cn0NDKeNBRQtHx-iRTESFnpMVSQBxVvTtBmuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه سپاه که میگه شب گذشته ۴ کشتی با کمک ارتش آمریکا قصد عبور از تنگه هرمز داشتند که سپاه بهشون حمله کرده و متوقفشون کرده.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/6203" target="_blank">📅 09:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwIKd6DytcskgrREZ8hwA8c0pD0sZgM_-vgLSFSuppsLWvo4lKHUdnYamvU6KTJ0ZIwie4YA-P8WvlGHSSsdL1Tqj1EqYmTBJtXSZZJjRFO3ivP5mNbMPqYPVtPXuQk9OJ3aio7IybF7LKje0fKB21QUwTvctk4viQjjQTVEGzMXgeQYKOZ-JI-ojiPVYjQYGeBhs_G-zPRglqIgT0eNEBsIyy61lsLPDIe3zNaTwlZG02u33BI7OSk33P83sDXz49KXOUPsyBV0Igb4hJ2yXW5ne1QUNBSUjH4NSib_WEtNlf3eOJo1lKyP202mi84jZO9uilhtDq90cEmta9cboA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا شب گذشته با موشک
به دکل مرکز کنترل ترافیک دریایی جزیره لارک، واقع در میانه تنگه هرمز حمله کرد.
این مرکز برای ایران یکی از مهم‌ترین مراکز دیدبانی و کنترل عبور و مرور کشتی‌ها در تنگه هرمز بود،که اکنون کنترل تنگه را برای ج‌ا سخت‌تر می‌کند.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6202" target="_blank">📅 09:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6201">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6201" target="_blank">📅 09:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6200">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6200" target="_blank">📅 09:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6198">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6198" target="_blank">📅 08:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6197">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔺
سپاه : به انبار دپوی قایق‌های بدون سرنشین آمریکا در بحرین حمله کردیم.
🔺
حملات ج‌ا به کردستان عراق</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6197" target="_blank">📅 01:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6196">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
وقوع ۵ انفجار در یزد
برخی گزارش‌ها می‌گویند که حملات در پارک کوهستان یزد بوده (منطقه سایت موشکی)
🚨
گزارش ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6196" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6195">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6195" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6194">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbBppC3kE4yiqvn1rPHo5LlwHBLSmaHvizSpBZGLNUz4gRKpxGzCOHkieTXV_mtXVmjA8iUFweBq2r_sO6aWBrzIUP04nKaaLvtIlzuYj_T33P6VB477eSUrzcfNbex07FxYKIvTm923ZWUCjQ_93cESQVKHSjPIcG6ZLG-uy4SVEsWn3jzpKo3FLv5GoPxQIZGWWxZHS6HAf_q0wNHP5j4C6Zk_B-wARPr6-kGZkylyPopWt8eL_7fO_hX5d873A1jCUqrPWjsA-ZQqOHlAJq5d_A6PJ4mb-Sd6oeHtXvna7lWiOQq52OF4-22STGgayexXHILpktMYVIw1eh-bVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش حملات ارتش آمریکا به بندرعباس، قشم، سیریک، بوشهر و اهواز</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6194" target="_blank">📅 23:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6193">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
سنتکام: ‏امروز ساعت ۳ بعدازظهر به‌وقت منطقه زمانی شرقی،
[۲۲:۳۰ به وقت ایران - یک ساعت پیش] برای هفتمین شب متوالی، یک دور حملات علیه ایران انجام دادیم.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6193" target="_blank">📅 23:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6192">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029791358c.mp4?token=G_Ar6iRCUc11R-46msXg1j-h30ffm98JIWUM_SzpGtvGP2VSkiH6v26FzQLGoQY19KhOYidUnba8ufzYCyub_qzKLU_VhhDWvLbzOtRSLaYy-oWiReFzdJnQQMIb0TWkK1-PQgH6MOujJtIB58jmQNUtAp6ptaHJ_0XIkwPaWjEzzOjbWWYy2t1mBkNtFBCflgIu8CmJa2q2UlzV7VapKHbxNU-dQOz5_gMR6WptDNsw5asRpCNsXTlh-OcMLpCvpFWhP1fWA1_HzotEvuN9vfYrg5NHY4i9IEj_A8PMgUMv3MgM4UbrK6UmYpiFSOPwwWC6ekRm8mAZcKArcqP6YLd4RXvOh05J8a6kZIWNJJsVMeLY07jgEWShJl21f7IZLKp3D-6D0vJk-MW5LK87cryhTE8YTqL8przbAL2ZzG1sFF_HQuP-ABDoMvbXgS0d8_dGZphfJdUVjYmS1UjCrPgUELzEPEfzUPupwyzMRaA_LzFCtb5KJV1w3PPSwmqAW8pMuYrig_MN8XItauN08_2sCoQ03OKrQnv2aUstJkNH87yYWd6uezQRyi4jqjmmpzvRbklmTyNBVe_RgDiOJ__flx_kb1NAh45LnFFfvgx63ieag599La85voJ5hef5Ogw60Jyx3rdAf3YVfXqULA9NN3Z__PFGyg5QlxNbMQs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029791358c.mp4?token=G_Ar6iRCUc11R-46msXg1j-h30ffm98JIWUM_SzpGtvGP2VSkiH6v26FzQLGoQY19KhOYidUnba8ufzYCyub_qzKLU_VhhDWvLbzOtRSLaYy-oWiReFzdJnQQMIb0TWkK1-PQgH6MOujJtIB58jmQNUtAp6ptaHJ_0XIkwPaWjEzzOjbWWYy2t1mBkNtFBCflgIu8CmJa2q2UlzV7VapKHbxNU-dQOz5_gMR6WptDNsw5asRpCNsXTlh-OcMLpCvpFWhP1fWA1_HzotEvuN9vfYrg5NHY4i9IEj_A8PMgUMv3MgM4UbrK6UmYpiFSOPwwWC6ekRm8mAZcKArcqP6YLd4RXvOh05J8a6kZIWNJJsVMeLY07jgEWShJl21f7IZLKp3D-6D0vJk-MW5LK87cryhTE8YTqL8przbAL2ZzG1sFF_HQuP-ABDoMvbXgS0d8_dGZphfJdUVjYmS1UjCrPgUELzEPEfzUPupwyzMRaA_LzFCtb5KJV1w3PPSwmqAW8pMuYrig_MN8XItauN08_2sCoQ03OKrQnv2aUstJkNH87yYWd6uezQRyi4jqjmmpzvRbklmTyNBVe_RgDiOJ__flx_kb1NAh45LnFFfvgx63ieag599La85voJ5hef5Ogw60Jyx3rdAf3YVfXqULA9NN3Z__PFGyg5QlxNbMQs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت شانه خاکی موقت کنار پل بندرعباس</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6192" target="_blank">📅 23:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6191">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏یک گزارش محرمانه که برای رئیس جمهور ایران تهیه شده است، نشان می‌دهد که تنها ۹٪ از ایرانیان از وضع موجود حمایت می‌کنند و تقریباً سه چهارم آنها یا اصلاحات ساختاری عمیق یا جایگزینی کامل نظام سیاسی را ترجیح می‌دهند - فاکس نیوز</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6191" target="_blank">📅 22:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6190">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:  ترامپ به ما نامه‌ای داده و صراحتاً نوشته است: «بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6190" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6189">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a688590cec.mp4?token=dqMNLy5DuGjWckG-r2UygVnWmDsmq92Exi1YoQ0O6lxrhCdZPX181OxMZTAtZbD4GMKDXfkgvtYT7xTsP6Is37cBdRrK5qr3wce0TFa_ieVhKQaYVwrzWZUSbsk6EPXlaBRtKqQk1pFaitiDqsH-ECEi12Ad-Ve4tcOqhqIesdamTAxHPinjuBXXBdLUmX_3KgKUKCVGCPqZ23a8hNb3mApxS8sRa4W-5oGT-bLXkn6UljvtRexzH7JO8301fbbVYHqPLhVRsD_4sqYErpE9D-b5Iw6IcM_jHPitnu-bcSPv4TNa0mmX_zXXRjqXzm9fFNJ5tz6us9-TJ30epQoRBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a688590cec.mp4?token=dqMNLy5DuGjWckG-r2UygVnWmDsmq92Exi1YoQ0O6lxrhCdZPX181OxMZTAtZbD4GMKDXfkgvtYT7xTsP6Is37cBdRrK5qr3wce0TFa_ieVhKQaYVwrzWZUSbsk6EPXlaBRtKqQk1pFaitiDqsH-ECEi12Ad-Ve4tcOqhqIesdamTAxHPinjuBXXBdLUmX_3KgKUKCVGCPqZ23a8hNb3mApxS8sRa4W-5oGT-bLXkn6UljvtRexzH7JO8301fbbVYHqPLhVRsD_4sqYErpE9D-b5Iw6IcM_jHPitnu-bcSPv4TNa0mmX_zXXRjqXzm9fFNJ5tz6us9-TJ30epQoRBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:
ترامپ به ما نامه‌ای داده و صراحتاً نوشته است:
«بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6189" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSelQUSbnD66uDeTp5bL3po6g8SfFc8Lgufij0DHBQAsu2sln-FSzWTYOBnHTLc064xhzSEGoORHCobTzzFwmtSZoCCOpKkO40sti1karBbE47fQhuOs5aG2_dyxDP-uNcSXCx4M0gxjpxlRM417gUywS9veu-Os54VQYWs6hcMXWwrN2NUac53OOCj-qeTqCO6qnx6fIfS5rdm9CaWI_61RGtgFhtRu_Rh7-7k1eyQqMDQGom_Kos9PpBO68d-7MGB1oZio0UVc6hi2wblCmtY9FzVOzDDgLb1BGIflH12SFBXLvdlVEgadEMRFsI7LFDEdiCQLNM3j5iu7fglhjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ایستگاه مترو در تهران با مجسمه مریم و عیسی درست کردن (که عجیب هم نیست،
نصف قرآن داستان‌های مریم و عیسی
و قوم یهوده) و پروپاگاندایی راه انداختن
که ما چقدر احترام میگذاریم به بقیه مذاهب.
بعد همزمان کلیساها رو مصادره میکنن
و صدها نفر به جرم مسیحی بودن
توی زندانهای ج‌ا هستن و اجازه داشتن
یک مسجد به سنی‌ها رو هم نمیدن!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6188" target="_blank">📅 18:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6187">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmBce1IBk4dyKqyfK1sMa8XdUKmtnv7OmRL-StLj7egWXZUkoWMdPR7zshwfUeL7pMoHD5dNpqwurwddZyTopoQgb1OS2xZQT4V6X3EdsZ8AKALYQb15_2zWVhU5JuDK_fyuLrH-TI5u8Omi3DAt8wITosBq2F264wPcQGwlK80Mxi5wArQIBLbQi7IxM5w3lXm6_H10TGsUrF9PQBrf0lQ92-UuHGe0bu8z-n-ppQohBkyo6ihwL9G8DXYaLI5XwFXK5t2sWZnIsMmx-kEHF6-L-pgAxF6ZuoGFrCn8Ak4hkRgpjhQaMU6_zKZIHO6o3ng8xeqCyxfrSmEZrk5XCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب طلاقش بده :)
چرا اینهمه کینه؟</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6187" target="_blank">📅 18:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gesvniza6TqNkTxaw1ifLUIv9yupbJvISt7dexQTIaT_sSQE0Ah4-eV3MqSYhLCVqivMGcWKSmYDX8SgQDrmEcuSg2U8QhpZcl_OJ88G-F3SwADv3pYVLl-EM6hjW9hiu_5sm_olF61Lba0YlrTR7q3r0TrzPT9pM27xKA-EDo-3zxrG3DBKuQDd8cw77dT1IPavRFne-Cst8gR6pBq9DqYESwTQUaXuWQJRULcuSyfpit5SW5-me5l0OyOGhdT0YaDz_KjxrcrrGlbKSsIMAQrhXDlVzqu9NFD72IQgYQ0a4eY3fxQ3NDcPKw-zvaHvXBuQUJFR3CSUMYBxSH_HAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل عرزشی !
من میگم اینها شکست‌های تاریخ
رو پیدا میکنن و به عنوان الگوی خودشون معرفی می‌کنید باور نمیکنید :)
تنگه احد! که نماد بزرگ‌ترین شکست و عقب نشینی مسلمانان در تاریخ صدر اسلامه،
رو شباهت سازی میکنن با تنگه هرمز
‌‌میگن همونطور که اونو در سیطره داشتیم
اینو در سیطره خواهیم داشت.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6186" target="_blank">📅 17:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6185">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=Aop4tcPk-_icJuhxU0qAubNSix414exMLaUUJc5R9rXEU4PNzSLZp6EuPa1t7yH8CCDhHccUubPx8IpcYElEM50iFweqqTPEYwAtKZ_tR8Q12V9Td-Tb5IXR2yCezlLiucsZl-fGdDEfQ5U6aZdw5sqI3o0T0Rnn2eGRiBSx53mSsjZtC6vo-dZCn2ZtNOlTi_znNV_sOi6Ag7bymknZrzRjJklmpR2aZAXiJYN1eSwNiMr5sBWtiFN0mrdgiPWhBVnWN9cjlHJ3mTffrQIACclfK_9VH6Oi4WQZd8yU-rnFeeJDQVZng9mCgqV93_Lb1Djx7vPKPrR4v6c_gbHtUzhSWiB-d4uXNsIixZW6w9Fgk9Xio8TlGbw0ktwoOQosskxuiDikoEt_RnvhWiMIRZn37raLr9NS7_DKdRxmrtKzZ24cvJvO2DzgaZ3IibyZxb793Jq9nR-1gu_5VfRdleb9TPjQD3jl5BVnAioJ7GOxeTgr-E3dmQTD7PLWcIjTYTIxS-BJ-AHXGacFiya6kgUcETso5JUzygAVR8Vb5xa057TO0vWhgNPF6YEn1PfDGO833bR1-z02CIbvsqBTRZuD6GhSLllfa5u3X3mwSR4SzssojgqkiXZOfUdJXFRe3S31mH4UqwC6FNOUiuh1vxQGGM3R8gNCnVI8hiOHBY8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=Aop4tcPk-_icJuhxU0qAubNSix414exMLaUUJc5R9rXEU4PNzSLZp6EuPa1t7yH8CCDhHccUubPx8IpcYElEM50iFweqqTPEYwAtKZ_tR8Q12V9Td-Tb5IXR2yCezlLiucsZl-fGdDEfQ5U6aZdw5sqI3o0T0Rnn2eGRiBSx53mSsjZtC6vo-dZCn2ZtNOlTi_znNV_sOi6Ag7bymknZrzRjJklmpR2aZAXiJYN1eSwNiMr5sBWtiFN0mrdgiPWhBVnWN9cjlHJ3mTffrQIACclfK_9VH6Oi4WQZd8yU-rnFeeJDQVZng9mCgqV93_Lb1Djx7vPKPrR4v6c_gbHtUzhSWiB-d4uXNsIixZW6w9Fgk9Xio8TlGbw0ktwoOQosskxuiDikoEt_RnvhWiMIRZn37raLr9NS7_DKdRxmrtKzZ24cvJvO2DzgaZ3IibyZxb793Jq9nR-1gu_5VfRdleb9TPjQD3jl5BVnAioJ7GOxeTgr-E3dmQTD7PLWcIjTYTIxS-BJ-AHXGacFiya6kgUcETso5JUzygAVR8Vb5xa057TO0vWhgNPF6YEn1PfDGO833bR1-z02CIbvsqBTRZuD6GhSLllfa5u3X3mwSR4SzssojgqkiXZOfUdJXFRe3S31mH4UqwC6FNOUiuh1vxQGGM3R8gNCnVI8hiOHBY8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیا بودن شعار به زبان عربی میدادن؟
چی میگفتن؟ میگفتن  سرباز ایران و وطن هستیم؟
نه میگفتن «سرباز دین و عقیده» شون هستن!
و کنار لبنان هستن! و مسیرشون همیشه مقاومته!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6185" target="_blank">📅 15:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hgquh2b8msOhBeJ2lRbL3ZOZASOfIG6XGdC1QQWVKqrt6Ccy0nrTYVgxQ4uCIlAdBncbBAsHb8Pt4peAm9QUEgbEQxMdBEu1ppFO2kgWrvedqfeW51HkRqSC_86ABo0Titrat1zlvSIIUQ2Uy_CEDCaKTmYigVi-h8xFBFvKf_ZmgUmuikbugM7MSisz97U4H2EWOa9ICG_oCCAbCVuMwctfcVFyKvAdfyW-by0DtktANZJU4HcDyLcYRy1Fanz4ErS7dGQRaZj2Ke0SKo-MCj79Fl6oMSSF5UYdbbykAvaXmYu9JuxBDqyfnytGLWRn9oVmhmeVvoWU-KZaoAuixg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی به تاسیسات آب‌شیرین  و تولید برق کویت حمله کرده.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6184" target="_blank">📅 14:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6183">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=vIowOB1SJy9uovufs9ZVCc5lwwcGV2wlFGuFhCH2uYAoEdO55kkeEq7OENK7zEE-taNwqce6KrTD_-MgtOK2ZNjhAWBcGP_HljH5uGo1X-TQj428ftb2OyZMMlP8AArg5AZklTO8kgTelQNgMUnni9AYN4vOsuOQHk4SKt1jjh6AFPDIqItYjgXjS7qYzsOSfpWkiZYvSkCE1ttJeNa0qs13BDwMcBlKz801EhjY8uCEtlONFAclDKU1jrT04DBrxX-FdNyoI4T1cxVMbBLNvXu7IbnzpQkGpGRnGU91xoNrGjPY5ofSQBLIRmuV_UKJAPsYkPRI3YMhZXb6AE02AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=vIowOB1SJy9uovufs9ZVCc5lwwcGV2wlFGuFhCH2uYAoEdO55kkeEq7OENK7zEE-taNwqce6KrTD_-MgtOK2ZNjhAWBcGP_HljH5uGo1X-TQj428ftb2OyZMMlP8AArg5AZklTO8kgTelQNgMUnni9AYN4vOsuOQHk4SKt1jjh6AFPDIqItYjgXjS7qYzsOSfpWkiZYvSkCE1ttJeNa0qs13BDwMcBlKz801EhjY8uCEtlONFAclDKU1jrT04DBrxX-FdNyoI4T1cxVMbBLNvXu7IbnzpQkGpGRnGU91xoNrGjPY5ofSQBLIRmuV_UKJAPsYkPRI3YMhZXb6AE02AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!  ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟  به خاطرش حتی موشک به اسرائیل نزدید؟  (که اونهم اومد در پاسخ ماهشهر رو زد؟)  خب جنگیدید و شکست خوردید!!! هم در لبنان،  هم ‌در سوریه…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6183" target="_blank">📅 14:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6182">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902cf63917.mp4?token=kuXzrLQ_GeZt2C5Th95czwRYUNwd9fSQpQBygzDadanw1f2DXToqs9_OA5Ql2eV-IUSIPo-0ymsTwqkDIAoL1LHV7QfVqsj8ltq1zqwp6euknyictCJCRGqTVIrSLJmk7JZXT4g6C2_15Qu5vP4pXDRAq_GKrFt55PeF9qGiLuRvNtrO1322kVVhLXUAtP7-OcndlmTkg-hMvkHFrK-Z4sGbFv7CSyg6BpxBH2yTDradPElQkrgCUgVDicg6OBv6v5bB0lf4G4jEr1_ySt1Iz0paOPUrEuoewKQ2Q7M_fcda26_HLFJnYL-ZHTWlE-8aq4Qnp1_jlrESmbr2tRD3CW2_IJwTuCDWXYD4ahSRQkTDDa2RRBR8IyDos3VUeWRkSKIi5IlmaTjbmAoa70gwWg7glO6aln2kXmWAfCkBQ2E-C3vqzsoJDSDnCr28MNkORYhQ8pUEVF3a4IVKEIJjyPp5RYDr-vL9FgCZs9kYu_49QuUDyeWLDglTh54VBCfmSXw5bJrb7xVRvBN71cypHPpFNE9AK7RLNPRknaHsKOP_p0aTefaHpuj8wqYF0yokZR8R7F8DdMxbdV3QC1MhyoKM2PWjKubJ8LCNTiI1Ow8M1PXDmvcZa9an3VblMJsD8xGmIT6uJ8rMJCFaGlanpADeSpVClfAS6E1RR86ELsI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902cf63917.mp4?token=kuXzrLQ_GeZt2C5Th95czwRYUNwd9fSQpQBygzDadanw1f2DXToqs9_OA5Ql2eV-IUSIPo-0ymsTwqkDIAoL1LHV7QfVqsj8ltq1zqwp6euknyictCJCRGqTVIrSLJmk7JZXT4g6C2_15Qu5vP4pXDRAq_GKrFt55PeF9qGiLuRvNtrO1322kVVhLXUAtP7-OcndlmTkg-hMvkHFrK-Z4sGbFv7CSyg6BpxBH2yTDradPElQkrgCUgVDicg6OBv6v5bB0lf4G4jEr1_ySt1Iz0paOPUrEuoewKQ2Q7M_fcda26_HLFJnYL-ZHTWlE-8aq4Qnp1_jlrESmbr2tRD3CW2_IJwTuCDWXYD4ahSRQkTDDa2RRBR8IyDos3VUeWRkSKIi5IlmaTjbmAoa70gwWg7glO6aln2kXmWAfCkBQ2E-C3vqzsoJDSDnCr28MNkORYhQ8pUEVF3a4IVKEIJjyPp5RYDr-vL9FgCZs9kYu_49QuUDyeWLDglTh54VBCfmSXw5bJrb7xVRvBN71cypHPpFNE9AK7RLNPRknaHsKOP_p0aTefaHpuj8wqYF0yokZR8R7F8DdMxbdV3QC1MhyoKM2PWjKubJ8LCNTiI1Ow8M1PXDmvcZa9an3VblMJsD8xGmIT6uJ8rMJCFaGlanpADeSpVClfAS6E1RR86ELsI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6182" target="_blank">📅 14:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6181">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6181" target="_blank">📅 13:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6180">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHMT8jncgARFCLohRUCFA70EBo2H66akw-7Wl5tFVf7wxBHn9oqXqxEjEhvm140GTxrf_U0ZY18T9T2AB9NTMQ2KbuTfLVYiieBvncvuzc5Lc87sjkw7pUyKaTzlrDn1AtVM0eS-V_CB0nhJo4vDbtrd_kqbiVEHR8tKV1ndq9WfbssCMqLpB3B81XV9IV78VZOks87b82YEL9q8HGuSP7PlSEjIn2-JnINBAP-5PBnXEMDsjdjBeOxSV5wFPoGuxJxjGuBsMEnL8-IuwRSfn-TZq_UoFw2VhMu4cBbzpgkOkomWzSOG87G1rQSyTDFmm5ruRyowqrt6qBCF86NqIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6180" target="_blank">📅 11:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6179">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d198d21980.mp4?token=YtOGyODo5hng3_HlSexgheUQvWO-c_8GBLqzW33GuXTvWWo3qy_7FCd53Jbi2DUkkEBbB1wXXgbRrIClAPj-iH27_OcD7up1uc54ey2sOFMNWsMmCsAFDHfVA8vK3PPIFf6-WkAegDbGOpDCs49zcpA2TDNIOvJ3It_IR-7zxBs4HWjHQbf0LTRswSRQ_bb7w-p46z8A_7u3RzgV1SjaMddLnxsvXxFZLKXgrmfj2FqOsX-jTP3swB-YIUpjvY7rc5u_IL_PjKW662nVC45dtCYLOY6o0BOyX4mTuc7mOiDXpuBXrJ-RoO2rnJ9GXWtzhMKXA6zKTbEeaUV8mjLwOYYZW5UAucJJlJC38pbqar75Lm41kyvbfgcfmTCjC8CyqY36yT4TXOxeRdUNsGt-vOObZBvVxQjvQu46kpJurO_YQhCsv8QLc9OMKQO-lzKikOe4DOuDnuY_FaOrwDyPPvBX3-2wnLc3Djoinvi4bA-2CXiUOpywJfPGqQ4-ID8qd1KLIPjZn1o6dfyqBf0B6SyEiQnJ6FF3JU5C6-ORiG-AXVoL2KnN0Dnq2kSgTwdkZyxPVjjeeWhQrjMpc4aImfhXNWUzgDRxzcML4jDtds7CVqIE8XEPQWMjsB1yx_7DJ1fqgRZ-4J36-3h1JgKxgSLWwHaJxVHzUSEssHdbtF0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d198d21980.mp4?token=YtOGyODo5hng3_HlSexgheUQvWO-c_8GBLqzW33GuXTvWWo3qy_7FCd53Jbi2DUkkEBbB1wXXgbRrIClAPj-iH27_OcD7up1uc54ey2sOFMNWsMmCsAFDHfVA8vK3PPIFf6-WkAegDbGOpDCs49zcpA2TDNIOvJ3It_IR-7zxBs4HWjHQbf0LTRswSRQ_bb7w-p46z8A_7u3RzgV1SjaMddLnxsvXxFZLKXgrmfj2FqOsX-jTP3swB-YIUpjvY7rc5u_IL_PjKW662nVC45dtCYLOY6o0BOyX4mTuc7mOiDXpuBXrJ-RoO2rnJ9GXWtzhMKXA6zKTbEeaUV8mjLwOYYZW5UAucJJlJC38pbqar75Lm41kyvbfgcfmTCjC8CyqY36yT4TXOxeRdUNsGt-vOObZBvVxQjvQu46kpJurO_YQhCsv8QLc9OMKQO-lzKikOe4DOuDnuY_FaOrwDyPPvBX3-2wnLc3Djoinvi4bA-2CXiUOpywJfPGqQ4-ID8qd1KLIPjZn1o6dfyqBf0B6SyEiQnJ6FF3JU5C6-ORiG-AXVoL2KnN0Dnq2kSgTwdkZyxPVjjeeWhQrjMpc4aImfhXNWUzgDRxzcML4jDtds7CVqIE8XEPQWMjsB1yx_7DJ1fqgRZ-4J36-3h1JgKxgSLWwHaJxVHzUSEssHdbtF0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6179" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6178">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=vc0928mitiTwmYXQRIsZzT98-CpK1c1ZaT4QPqVaHT_svZaMwRVf5V_CNWMv5NntA3yzc77EKAI9DOPFmgBH1bf31LYuafXFme6hHMKqlVQuhdaoQaKl8mt3dVTfyjWfrrBywxIp7_xymPEyXs7YrEH3qx0LiJwfsY98nXLl-hvCu3JzZtWnLt7bHXKLGtvLAIx737-ZH7BpPFljo_tfBe7Yh3Mn4UZh2mbO3Sj8xWIf4I32Z_AFFQzVA5hS0KC8mOS7bweWbY4ikKYP06mlsgoCcCcn4E4r206H0udeL02eSxO-OtNncIygCj6UiZ_s-xWM3-MDFGxU4REb5EGRRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=vc0928mitiTwmYXQRIsZzT98-CpK1c1ZaT4QPqVaHT_svZaMwRVf5V_CNWMv5NntA3yzc77EKAI9DOPFmgBH1bf31LYuafXFme6hHMKqlVQuhdaoQaKl8mt3dVTfyjWfrrBywxIp7_xymPEyXs7YrEH3qx0LiJwfsY98nXLl-hvCu3JzZtWnLt7bHXKLGtvLAIx737-ZH7BpPFljo_tfBe7Yh3Mn4UZh2mbO3Sj8xWIf4I32Z_AFFQzVA5hS0KC8mOS7bweWbY4ikKYP06mlsgoCcCcn4E4r206H0udeL02eSxO-OtNncIygCj6UiZ_s-xWM3-MDFGxU4REb5EGRRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی از سخنان سردار نقدی : اگه حتی به آمریکا حمله کنیم، قدرت پاسخ‌گویی هم ندارند!
با کدام پشتوانه اقتصادی میخواهند بجنگند؟ با کدام پشتوانه مردمی خودشان؟ همه جا در محاصره ما هستند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6178" target="_blank">📅 08:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=EiriIj2Bm9C4YG3rKLnZExHxFUNhb3SteM5pdcEhgnXuPc5Al-foaDVkz7C5tVecSm_outUjRL0lcuXlRdgFoK3WhTUm9KCwuM1eLeS3peCwA9WLLNHzfCnd_77glf3MRZp5g9PYGtG4Uw-a3_608I3tI4_aoD1zDwO42OkC6n6hk8fLee3FSNxaGgF5cx61Zvuggs4tjCsGLeCH4Hs9vEX_FosR80daeHqSAC2x08sRkGKARbiwFr5024_y1DYgdtaqYENPEebg40tpiY4lOZaYFqP3WTU9ful2aSNrrUBU5dyYETyHrBTUd4BXTFS78cgoAiHHb1N6Ovp4HuiOuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=EiriIj2Bm9C4YG3rKLnZExHxFUNhb3SteM5pdcEhgnXuPc5Al-foaDVkz7C5tVecSm_outUjRL0lcuXlRdgFoK3WhTUm9KCwuM1eLeS3peCwA9WLLNHzfCnd_77glf3MRZp5g9PYGtG4Uw-a3_608I3tI4_aoD1zDwO42OkC6n6hk8fLee3FSNxaGgF5cx61Zvuggs4tjCsGLeCH4Hs9vEX_FosR80daeHqSAC2x08sRkGKARbiwFr5024_y1DYgdtaqYENPEebg40tpiY4lOZaYFqP3WTU9ful2aSNrrUBU5dyYETyHrBTUd4BXTFS78cgoAiHHb1N6Ovp4HuiOuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پل  کهورستان در اطراف بندرعباس
که شب گذشته مورد حمله ارتش آمریکا قرار گرفت</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6177" target="_blank">📅 08:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6176">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار …</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6176" target="_blank">📅 08:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6175">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKYyJM0XDKbRHRkI8CFmuX1MQr7bkWhyQF1wRLBiWBQs6TfrbL2WoEpd8yirZKJk_HTBndjApm1Y-gMZZPS9ePpNL4m-Z3BkIEjKMYUEt9j89bPE29F4AOH_OmuTPg9pGPHnsiCGphEb28_OE7TfO7nTfSpgBs4nsh-9e3EUjDz5wxBEpcwWpwIlpwoS0Aj8k2cOoV4dUHkS4Ykbi8zIq8NsVcvm3pNrIy-mBXQRvGhw-F515GfUDzSxMALwlQhDd36bzkyEy45rgddFWlPWt62FVV5uBfRyniNoM9OipO1yZSIWFlyx9e_hCznrPrlm7ULJfSzQaY-rhDQB5UnSpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6175" target="_blank">📅 08:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6174">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
حملات شدید به بوشهر</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6174" target="_blank">📅 01:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6173">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=OkGyXw5AQWgQL0LTP8ddD2G-smHMAT20QW5a9zs8ubSpct2JO9MZvs7SRJAEtDIVztk4sN9M4CeSVNmepmTHpON8s_hHlKcY_e8jihIxyEbdoN4cW7lm8UVy2Aq_5uBWm1rdZMIQ4yOqALf1XCY9bu2OFIsFBEJ3G-kIqE94q_yLAD6vqwPFgPjdJn9ASVM2tc_IjfJAWIzdsG8dBKNf3G4h8RSmb--X767GbXrNnCyw1cEMp6yQ1Pq9iceBjJSfbZDE7C0MoSrU4cXnPiifVdLxe4LeYYk06iQ5dcrGtimlENUULoaSqZ8T4y_RJW-ewfxIgFcRYDIdlH-zJRVCaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=OkGyXw5AQWgQL0LTP8ddD2G-smHMAT20QW5a9zs8ubSpct2JO9MZvs7SRJAEtDIVztk4sN9M4CeSVNmepmTHpON8s_hHlKcY_e8jihIxyEbdoN4cW7lm8UVy2Aq_5uBWm1rdZMIQ4yOqALf1XCY9bu2OFIsFBEJ3G-kIqE94q_yLAD6vqwPFgPjdJn9ASVM2tc_IjfJAWIzdsG8dBKNf3G4h8RSmb--X767GbXrNnCyw1cEMp6yQ1Pq9iceBjJSfbZDE7C0MoSrU4cXnPiifVdLxe4LeYYk06iQ5dcrGtimlENUULoaSqZ8T4y_RJW-ewfxIgFcRYDIdlH-zJRVCaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏فارس: جزییات حملۀ   آمریکا به پل‌هایی در شهرستان خمیر؛ ۲ نفر شهید و ۴ نفر مجروح شدند</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6173" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faxD8dyf17mVj6HztsAcBaHNvAq566JY-RthpxQ-3BtIo8vjTAZ_T4Xb8Cbp8GZbY0oBvpZ-rYScxlNe_Itag534c1HSJNpKu9NNco3U6S9AkxFTjjKdMs8ZNU2bhO9C7WRb3SB96cZMl6nhUSfX-CZ9p3cC70YYmzLUZaYXUmnjdqyNGFixpqL2a9zCEDZ5ZQAFbgj4hqsmSFmcI8IzEPmjF4DNm5uS7FX9pElYyQXi6ZrFz-4JziDFOukw_0YkmPo46g7r62Dyuvh_YH-wfsAgzHU5diO_Zz7cLxUFlnLyjkp7SxceRP1TnNZLhQO0Hk6a_bALqpkRbHRyb9AMMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6172" target="_blank">📅 00:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6171">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
صدا و سیما :دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند.
بندرعباس مهم‌ترین دروازه واردات و صادرات کشور است و شبکه ریلی بخش بزرگی از این حمل و نقل را بر عهده دارد.
این حمله می‌تواند به حمل و نقل کالا ضربه بزند و به آن اختلال وارد کند،</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6171" target="_blank">📅 00:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6170">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
حملات گسترده به حمیدیه و شوش در خوزستان</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6170" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6169">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
حمله جنگنده‌های آمریکایی به فرودگاه ایرانشهر</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6169" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6168">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZ_fXO-f4KzgcJsZq7cTPm9G72ejHAXRz-5DKgqFJuq8WouBRezTz1L91v3q3r4j0VdZ_8YjTOURnC9HX-9H123f7hzqDvG2giW_gya0xRAHrkMs4jpfmH2drTcaESe7LgNoTfQqatG4lXlRSmoCuraosspxNHtMbCpC7ad4YKdrIuz_UUG5-3ABZx9TclDFx-Px-jXRpMUPVqRWXKR-847cojcR_FgS0jnUa1rd3eEzrzb2xBGGxD9_fTXGfLsqCqhUj1xcbgQSb9MoNl15H4JrRAgKbUguvyBDY-jeqBe2Tx3Bcw4iCh_aXH5WyKkoAMbqDZAgFjjK1my_vNlU_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=CS1h1uZG3MNaIvIBnAtvjckq2X6msTgzGOmypnP4Z2RFUsYaMPvligX3dSreQ_CLq7WSAHGyJ6l_GkPfwV_9b-Ox6uiwpPDZBpaW6kXLYt7yp-9cHA7NpHLwn0LddreEm_dmKm_VTuqWDs3qoLcBjkONbrPJEcTZx9Hog8c_Y19su95_lW54nJljnjqjuIC6z_Da_BU8K_WNApXPYFEUln-nI9UjVsf_eTcXtIF1UBL10Ssw7xcOs23sxbx_xkRPT-Kywm1ZB7FewCWwj-j_PMZ8dQpEueooN7g2jzcbdnoOWLDqhV5bWU5fZz3L5LRrsLTelvfXG7Jvtc24Q0GrYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=CS1h1uZG3MNaIvIBnAtvjckq2X6msTgzGOmypnP4Z2RFUsYaMPvligX3dSreQ_CLq7WSAHGyJ6l_GkPfwV_9b-Ox6uiwpPDZBpaW6kXLYt7yp-9cHA7NpHLwn0LddreEm_dmKm_VTuqWDs3qoLcBjkONbrPJEcTZx9Hog8c_Y19su95_lW54nJljnjqjuIC6z_Da_BU8K_WNApXPYFEUln-nI9UjVsf_eTcXtIF1UBL10Ssw7xcOs23sxbx_xkRPT-Kywm1ZB7FewCWwj-j_PMZ8dQpEueooN7g2jzcbdnoOWLDqhV5bWU5fZz3L5LRrsLTelvfXG7Jvtc24Q0GrYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که گفته می‌شود
از حملات امشب به بندرعباس است.
دقایقی پیش بندرعباس ۴ بار مورد حمله
قرار گرفت.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6166" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6165">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=mVH87pVZwxf0493a3kJGcePok0im30sf1XmGTjoFlgJHQ_6tHFcA3PSAMglZTrZxmG4akWAYPbZSyisYP_EZKwCF6R2ujfcnF69wju_lPPmA5vV3B5DfVsume1iPerSPs8AMp01uo360Bb6jBnahZ0Vfc0tOkn01XsYuvhiGmPth9xhHp0wAnfvsRoNkWw15aCam_JQ42-QhXtGVpB08fvqPWO1jblxSke41pDgReAzBRxIdzjykpSHr-aiz-cBTdKcNOeIlG-UV2uVqBxRXxm2c62nDw8pYJpInQtdS4GDg_WL4UBzrV0WgJVLA_Jjxhn2MDsXuonskn6GldZ2mxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=mVH87pVZwxf0493a3kJGcePok0im30sf1XmGTjoFlgJHQ_6tHFcA3PSAMglZTrZxmG4akWAYPbZSyisYP_EZKwCF6R2ujfcnF69wju_lPPmA5vV3B5DfVsume1iPerSPs8AMp01uo360Bb6jBnahZ0Vfc0tOkn01XsYuvhiGmPth9xhHp0wAnfvsRoNkWw15aCam_JQ42-QhXtGVpB08fvqPWO1jblxSke41pDgReAzBRxIdzjykpSHr-aiz-cBTdKcNOeIlG-UV2uVqBxRXxm2c62nDw8pYJpInQtdS4GDg_WL4UBzrV0WgJVLA_Jjxhn2MDsXuonskn6GldZ2mxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازغدی : اگر میخواهیم اغتشاش نشود
باید با آمریکا مبارزه کنیم
(که حواس مردم به جنگ پرت بشه
و تقصیر کاستی‌های حکومت بیفته پای جنگ
و دوباره جنگ بشه «نعمت» !)</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6164" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6163">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
استانداری هرمزگان:  در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6163" target="_blank">📅 19:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6162">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofGnuRarLJ2ql3PL3PHxREcObxXc0TDnHInR93MAzye7tF7G0gW-hk7OHIT93m-d3UMFNig3Kt5iZJkLvxf9mjgm35-WqdgLFPvager-y8C2KUx3c2fYf7tZGGDpRd1rjFz5z8AOqZ6jPdO9_mkeE-2bwg7I82D2vdQR80hyT_xOYgEEnPhZNkVnbBeuiS9PCAbJc3L21_DxajX_2_6geKNCbH6GKYbKWYXjb4Vs1Ld6Al44rZ1HJD9vohsKjTuwlXXcXHWTZB1dDNaNU80VTP3wEV3SWSXgDaO_h35Y8M_6-oSggavMea9sFRxUDTbj5mX8ABRNisw65p2q1puKdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
استانداری هرمزگان:
در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6161" target="_blank">📅 19:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6160">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=jImyMp-059WAcGn1XBh77Z-ypxcO5RsOppGVegn-I1UznT3UYMBIlE4YfQml8P2acQD5FIv6-lpI6f0IYn6dXORZBQ-y3lte-vKFR5i3vkKErOiXF_gIWIkV4V1q52e7lmQsz1SjZMxA7AvfiqUMGnpRsHEFaagzcOxoIQZsXCFKhkxPP5qVlyf8f4s3VCiKZfk_QLuXKA7YwqHZD76ku7CyOxK8UNnPvwM04SxC2WM1aFDxPFMuglqkEbLvmmvbPE0b_aOY3QoW6Ok1L8OXg_FxoAgPRLv2BMmavgMWGaK6kUMKnghlkrAYRnslePkQD3YDI_NB7ZfNNM1udxdS-5pcxp8poARXrl4ewA6EeKk_6Q48ghXEvkNS-FZebGNgMm5ggyErsWASyc-iJx9C66UXNJApF2-YCiegp7x9RiOet-NQXSJqCqTYNMTBezeiqYzRSap3DAnWN9lC-Oxe2Nk7lQKskt-_qhhW0HWUQ92looFSF9VnEaleSVKxmUoxzsoZHivLjUL4doHPjyD38MBr9fon2aNj35asvXGIf70c__O9COQeER9VBmv-aYls3zEA_3wX6_lafQV-sgl5VxLh26cLJKsOPaV8hlINnhGiZ8gEVdfdX53pzDi0VgYHW7cBK9DIkMs6_aTzB6w2Smc7F-t5WUakHHs5slSAgyU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=jImyMp-059WAcGn1XBh77Z-ypxcO5RsOppGVegn-I1UznT3UYMBIlE4YfQml8P2acQD5FIv6-lpI6f0IYn6dXORZBQ-y3lte-vKFR5i3vkKErOiXF_gIWIkV4V1q52e7lmQsz1SjZMxA7AvfiqUMGnpRsHEFaagzcOxoIQZsXCFKhkxPP5qVlyf8f4s3VCiKZfk_QLuXKA7YwqHZD76ku7CyOxK8UNnPvwM04SxC2WM1aFDxPFMuglqkEbLvmmvbPE0b_aOY3QoW6Ok1L8OXg_FxoAgPRLv2BMmavgMWGaK6kUMKnghlkrAYRnslePkQD3YDI_NB7ZfNNM1udxdS-5pcxp8poARXrl4ewA6EeKk_6Q48ghXEvkNS-FZebGNgMm5ggyErsWASyc-iJx9C66UXNJApF2-YCiegp7x9RiOet-NQXSJqCqTYNMTBezeiqYzRSap3DAnWN9lC-Oxe2Nk7lQKskt-_qhhW0HWUQ92looFSF9VnEaleSVKxmUoxzsoZHivLjUL4doHPjyD38MBr9fon2aNj35asvXGIf70c__O9COQeER9VBmv-aYls3zEA_3wX6_lafQV-sgl5VxLh26cLJKsOPaV8hlINnhGiZ8gEVdfdX53pzDi0VgYHW7cBK9DIkMs6_aTzB6w2Smc7F-t5WUakHHs5slSAgyU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی جدید جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6160" target="_blank">📅 19:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6159">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=Aad8yAX94iTE_r523ygbl-FAgDKk9nRlZkvfpx6tjRWjtZyYgfORebtKll5gz_XKbjlFVBocriHDAOtQDZfFHdj_7ZP1JuXpvs6Hl1hCZ1reyjo0G047fq2qGKudoCs8SR8LqW6V-VG88LXh1nO4vvUYFc6fyoKLCyAib5Zx2xeoOcL9oG2YiiGX694w8PXGjXbT4pTD419U--nJmhE0l3n-w4o7PnouwaDpGt4fIKhh4LLNzTCuUBHaGrlfHmJUyYgOqMriWZE2SE0kGoIqWBCUAKEx-6k7yjQA6691US5h6VYygEIg6g6mhAnCVtbHBgOVqtdScsJsQeFoUdq1mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=Aad8yAX94iTE_r523ygbl-FAgDKk9nRlZkvfpx6tjRWjtZyYgfORebtKll5gz_XKbjlFVBocriHDAOtQDZfFHdj_7ZP1JuXpvs6Hl1hCZ1reyjo0G047fq2qGKudoCs8SR8LqW6V-VG88LXh1nO4vvUYFc6fyoKLCyAib5Zx2xeoOcL9oG2YiiGX694w8PXGjXbT4pTD419U--nJmhE0l3n-w4o7PnouwaDpGt4fIKhh4LLNzTCuUBHaGrlfHmJUyYgOqMriWZE2SE0kGoIqWBCUAKEx-6k7yjQA6691US5h6VYygEIg6g6mhAnCVtbHBgOVqtdScsJsQeFoUdq1mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، تیر ۱۴۰۳:
ما غنی‌سازی را ۲۰ درصد کردیم جنگ شد؟ ۶۰ درصد کردیم جنگ شد؟
hafezeh_tarikhi</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6159" target="_blank">📅 18:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6158">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ایران که ۴۷ ساله که در آتش فتنه اینها می‌سوزه</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6158" target="_blank">📅 17:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6157">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سخنگوی قرارگاه خاتم : هر چه در منطقه سالم مانده از نجابت جمهوری اسلامی است!
ذوالفقاری: «همه آنچه که بنا به نجابت ایران هنوز سالم مانده، یعنی تمامی زیرساخت‌ها در منطقه، زیر ضربات پولادین نیروهای مسلح مقتدر جمهوری اسلامی در هم کوبیده خواهد شد؛ آن‌چنان که اثری از آن‌ها بر جای نماند و گویی از ابتدا وجود نداشته‌اند.»
سخنگوی قرارگاه مرکزی خاتم‌الانبیا همچنین دخالت آمریکا در تنگه هرمز را «خط قرمز شکست‌ناپذیر» جمهوری اسلامی خواند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6157" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6156">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=j9hWenINH0liig6oZkbEHZPQfLymOF--KipvSz_lWdJgRUWDl6NzzRjWVAX7VabFKxoWz5qjboIhargDTPhbzZCnAm2EiAD9Js6cAFUZjSpY8zd8RQDCrNgAc3nnNzQuSZeZyOP5bcmcgCWBxDyFapQaeeGK8rbErOXGHC2_-UHUoK8MyVo8uXjyyKh3UL-kMuaWjWYwFv8RQyKK-hwC-Prj1lxHeuHTAZMFaYipMbFUBJdXy9tiHw17WoftdTjeH-rbiPBa2YB1bQ6WdCaiiOf-U1sWqfBWYrbC8AmwMJqo1ryDuMoLDTnzi-KPUbHME3BnGj6BVxUEMaBVkuxX5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=j9hWenINH0liig6oZkbEHZPQfLymOF--KipvSz_lWdJgRUWDl6NzzRjWVAX7VabFKxoWz5qjboIhargDTPhbzZCnAm2EiAD9Js6cAFUZjSpY8zd8RQDCrNgAc3nnNzQuSZeZyOP5bcmcgCWBxDyFapQaeeGK8rbErOXGHC2_-UHUoK8MyVo8uXjyyKh3UL-kMuaWjWYwFv8RQyKK-hwC-Prj1lxHeuHTAZMFaYipMbFUBJdXy9tiHw17WoftdTjeH-rbiPBa2YB1bQ6WdCaiiOf-U1sWqfBWYrbC8AmwMJqo1ryDuMoLDTnzi-KPUbHME3BnGj6BVxUEMaBVkuxX5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شب گذشته ج‌ا به اربیل در عراق
علی‌الزیدی نخست‌وزیر عراق با صدور بیانیه‌ای،
این حمله را محکوم کرد.
در این بیانیه آمده که «به آژانس‌های امنیتی
مربوطه در هماهنگی با نیروهای امنیتی منطقه دستور داده شده که همۀ تدابیر لازم برای ممانعت از تکرار حملاتی از این دست، و نیز مقابله با هرکسی که به‌دنبال خدشه‌وارد کردن به امنیت جامعۀ سرفراز عراق باشد را اتخاذ کنند».</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6156" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6155">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mU9WTG0Pc89xDKb2j_De688h6Ew6uJpN0DwTMJxYOQcEesWqytf-9XVT6z3eHOsUCjH99iy15xUiwRGhRAo9Pp4qNAozuL4fTl-yZUtgvYo-AeyqXd6p5FqCbmLfqd7sVRrgMltehlwvvO2qhRtMOQmam5NC7UvSXR5YWVCr-3YjyPOXszbjmqQtJ1SfTiT6UTB8vhCS5fze2Pa5lKS_HXTsug9qV1JJSNGr32WXjEnr0RghDlFjV_KFW85-iF38JXSs5w-3d4twEJCtMsh_znMukdXZEOkioUUgquZYqAxateMKmD1OQelp27o8oeerbSnWXK1ws3VUk0qoBJF_jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وراجی نکنید  بگذارید بجنگند که صلح بیارن :)  مثل صلحی که ۴۷ ساله در لبنان  ‌ و غزه آوردن!  انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6155" target="_blank">📅 12:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6154">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وراجی نکنید
بگذارید بجنگند که صلح بیارن :)
مثل صلحی که ۴۷ ساله در لبنان
‌ و غزه آوردن!
انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6154" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6152">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=iQHftNqyXJ6rkGdbxvIqfN4hUm2CHQFajSQSaSahG18K1S5Sl-oUBF3rK05RBf76N4dxpePfYm-F8SW4LB8I-yRJFeeofxEr7-kXEWo0LPyFt_uthnKD8AfLOwJjr81IGycoaDxLo83GaIaNMeScqCg06361Pq5piWjP39OKy7DYSd2uhTdAAZkddMYvTwzSIaqRObW14-YnHLT3noMtBxMCnddfA-Bhp5XwN-rWo_DlP6oGPMXpd2inRMqJDr3FpXAFYAZy6jZy3fdlslugq77qdGMEskNm_pduFdj2zwqo2JBdtlS1iSKO_QUTTvfq7m3XC4s4acTXjXskHL3-PyMOfjxs13Hecf9HgeSVWradR4GHKtqwJ_wbjDiaZE6XQ-eDTZ-Z_tuCrOH1L2Xzus2q19r638T6CsxxmoASQy6Yx6-tHPzHK_9pzADJCeu7jvFC_VJtRW0KaY_kRO3O55fRqMaDf0CTBWsw8YSkUvrjelN7q-rfrIHLeGYpJDP-XMRlzHmGB4GnxOivaaWuqUnLpKZsjzvJy5U-Yc3uThxvp0QRCLsTJk4LDj9vGNhiot4Fnsb9IOpJ2CQLqUlWXNKKg2gcz1dfMv0FfEFzkDbCr-39uSrs6bbIN5lCrMHBMXBWPqusL6RfZtjHuYrNpDSktD4CLyQ_xZPaecHtemI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=iQHftNqyXJ6rkGdbxvIqfN4hUm2CHQFajSQSaSahG18K1S5Sl-oUBF3rK05RBf76N4dxpePfYm-F8SW4LB8I-yRJFeeofxEr7-kXEWo0LPyFt_uthnKD8AfLOwJjr81IGycoaDxLo83GaIaNMeScqCg06361Pq5piWjP39OKy7DYSd2uhTdAAZkddMYvTwzSIaqRObW14-YnHLT3noMtBxMCnddfA-Bhp5XwN-rWo_DlP6oGPMXpd2inRMqJDr3FpXAFYAZy6jZy3fdlslugq77qdGMEskNm_pduFdj2zwqo2JBdtlS1iSKO_QUTTvfq7m3XC4s4acTXjXskHL3-PyMOfjxs13Hecf9HgeSVWradR4GHKtqwJ_wbjDiaZE6XQ-eDTZ-Z_tuCrOH1L2Xzus2q19r638T6CsxxmoASQy6Yx6-tHPzHK_9pzADJCeu7jvFC_VJtRW0KaY_kRO3O55fRqMaDf0CTBWsw8YSkUvrjelN7q-rfrIHLeGYpJDP-XMRlzHmGB4GnxOivaaWuqUnLpKZsjzvJy5U-Yc3uThxvp0QRCLsTJk4LDj9vGNhiot4Fnsb9IOpJ2CQLqUlWXNKKg2gcz1dfMv0FfEFzkDbCr-39uSrs6bbIN5lCrMHBMXBWPqusL6RfZtjHuYrNpDSktD4CLyQ_xZPaecHtemI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگر نوحه میخونن و مداحی و رجز خوانی و.. برای کودکان غزه و لبنان و میناب و….. از تاسف از دست رفتن زندگی نیست! میخوان در این جنگ بی‌‌‌‌پایانی که با جهان دارند،  از جمله و در صدر این‌جنگها،  با خود مردم ایران جنگ دارند، سربازگیری کنند! تا نیروهاشون بزرگ‌تر…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6152" target="_blank">📅 11:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6151">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تمدن اسلامی! تا زمانی که توی مدینه و مگه بود قادر به ساخت «توالت» هم نبود!  مستراح هم نداشتن !! اما دنیا در چه وضعی بود؟  ۶۰۰ سال قبل از تولد اسلام!  توی بیشتر شهرهای جهان  داشتن توالت عمومی! اجباری بود!   اینها میشینن روی منبر  میگن «مدینه فاضله»!!  حالا…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6151" target="_blank">📅 10:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6150">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">تمدن مصر باستان رو مطالعه کنید ابتدا تا انتهاش بر مدار مرگ بود! فرعون از زمانی که سر کار می‌ا‌ومد به فکر مقدمات مرگش بود و قبرش بود!  هنر و پزشکی و علم و مهندسی مصر همه بر پایه صنعت مرگ بود!  مومیایی و اهرام و جراحی پزشکی و….. همه برای کار و کسب مرگ بود و…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6150" target="_blank">📅 10:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6149">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTgEtqv7tnpeNFLi_8TAP8hbOAlls5JTUlmabmvEypY9TRPDtYYvb0_stpHSAtC-RFpFaW32JZ4wYW43VitmwslfQKVDj4B6XeuViFNPvMvQnscWf3w3hjSi2Y5W2uOgo79Q0hkclGVmoUvCQBK69ORJOUXCrE1n73IcCmycx0nS4GwZ61rNAVA58aZq43sNEosJRRoE1Pz2ak9p8F88xRUWES83VD3hRGAUT-ng_XcgQCDD4mvAxujgFTBwlVN8JVcm4hKMsvUlutHw-edTSEbVOt-iAViusW59-xD_5GKT4tEuC_Pn7My_s5aqXp58ETgiPljRm1jWFKGkaIg12Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها شنیدید جملاتی با این مفهوم رو که زندگی و این حیات «زندان مومنه»!  آرزوی اینها مرگه! مرگ براشون رهایی است!  اینکه برن و برسن به بهشت و به زندگی!!  مرگ رو آرمان خودشون می‌دونن و زندگی و زیبایی‌هاش  رو پست و حقیر معرفی میکنن!  و اینکه باید دائم به فکر مرگ…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6149" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6148">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..  سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند. و از مرگ متاثر میشن!  تمام هستی اینها :  مبارزه، جنگ، کشتن،  کشته شدن و….. است!  زندگی براشون چیزی نیست جز  «مبارزه  برای عقیده».  و خوشحال میشن…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6148" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6147">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=p3VD_jqHJmcIz4Q0ptdU3ZAg3hC4l5n_J3hC-sIbNNtTaL8W2y5SKW_qrM-gojdUGAYdMw_s-DnSu1eoygSRP2rd3VSrECoIHRi51sVoqH8KSW8bVvtcKEE6OQldivoL3oR5g3OqFntE6JV8l0YjCiIeDpQHTAz9v12abofmXrr7ulC9NpY-U8b3NlXPT5QcovxH2cHF1hGQBJgL91QVltEPynRQHggkY4KJlyzXtkO9PfakLl7F_cFkBtZlLEbGUyEVcfkSNJ24mx0qm8fFr_BWm_tKfpzM8ZKBd5MX6xTwNOa9Vlm2s781oaZTGou2CAFG5_tzS1StFK7CH7x-eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=p3VD_jqHJmcIz4Q0ptdU3ZAg3hC4l5n_J3hC-sIbNNtTaL8W2y5SKW_qrM-gojdUGAYdMw_s-DnSu1eoygSRP2rd3VSrECoIHRi51sVoqH8KSW8bVvtcKEE6OQldivoL3oR5g3OqFntE6JV8l0YjCiIeDpQHTAz9v12abofmXrr7ulC9NpY-U8b3NlXPT5QcovxH2cHF1hGQBJgL91QVltEPynRQHggkY4KJlyzXtkO9PfakLl7F_cFkBtZlLEbGUyEVcfkSNJ24mx0qm8fFr_BWm_tKfpzM8ZKBd5MX6xTwNOa9Vlm2s781oaZTGou2CAFG5_tzS1StFK7CH7x-eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcFbAPRJf5AwuCU3ooCvc85WlfoKB2CqBHzVwa2jwhcn6Kl6ZeXklg8vhuphqseJ-xo204XKO3vNQZTnLvVG1ynay875B-H6FDQX9HCvHX4Oo6PIkfhVx7LQTInn0CeU5ZralO_RICfJK1tycfKrY1Nraq7clvUkLdETqcFj1a4sgwlhUBVnWqe9OEPRy-V8Quv2DtEyXDLYySmKaIXtVIsRnPr8UPwM7YI__ikd9YGgRUfr2YeDtGefaA6lzGncAHzUAgVaxErDollCeD7bhUO5VwmJomhA8n2WpIttX20STl2ZLcwrlHFjLeh-lyZHUicTnKtRfWPkS3r_mRc-Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران به یک شهروند زن آمریکایی که در دسامبر ۲۰۲۴ در دوران رئیس‌جمهوری جو بایدنِ خواب‌آلود به‌ناحق بازداشت شده بود، اجازه خروج از کشور داده است. او اکنون در سلامت کامل در خارج از ایران است. ایالات متحده آمریکا از این ژست حسن‌نیت ایران قدردانی می‌کند.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6146" target="_blank">📅 09:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6145">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">استاندار مرکزی : شب گذشته به دو نظقه در اطراف شهر خنداب حمله شد.
این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقا مشخص میکند چه اهدافی را زده و نه ج‌ا می‌گوید به کجاهاش خورده.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6144" target="_blank">📅 08:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6143">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اطلاعیه  ارتش:  سامانه‌های راداری، سامانه پدافندی پاتریوت و مخازن سوخت آمریکا در پایگاه علی‌السالم کویت را هدف قرار دادیم.
‏ رادار‌های سوپر هاوک، تأسیسات و سامانه‌های پاتریوت واشنگتن در پایگاه شیخ عیسی بحرین نیز طی حملاتی، آسیب‌های جدی دید.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6143" target="_blank">📅 08:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6142">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
استاندار سمنان : به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6142" target="_blank">📅 08:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6141">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-s4V7ZXg5qcM0Twg3RdWebkkYJERFz2_ryKjbFFS5nJjxlcrQuZzxKIx0QdjHpD7B-YtFrkL9f6Als6LcchVLkPguojk53S_hdEiOLeYsgrvp2gl237c53onG8YK7Ddqn5JO9_HLXfAwunxsOTUm4F7ZmEwgOYuH8tDIdqAObxJcCPUJG_Z12Wc4CUcBwM3G-fHk3xU9nIUIHLJc1u63zBZevVVkryRJu31o6R9JAQgLv151tfGjS6soxvfbkM4SshYlf2mk7UFiXCh79KWkxqK8MFAesitzy02-Ryidiepedtk5LkCb7zjHt_u3MpXuiMPpq98dC8j6Xtib2aqdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین یارو خودش از دست سپاه و نهادهای زیر نظر خامنه‌ای  فرار کرده و به آمریکا پناه برده!
و آمریکا رو خونه امنی پیدا کرد برای زندگی و نوشتن از اینکه اسلام چقدر زیباست و خوبه و سعادت انسان رو میخواد!
حالا از همونجا به ج‌ا میگه مبارزه کن با آمریکا! مطلقا تسلیم نشید! تا انتهاش برید!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6141" target="_blank">📅 08:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6140">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">برخی گزارش‌ها از تداوم حملات به اهواز خبر می‌دهند و اینکه تاکنون ‌۹  انفجار  مهیب در شهر شنیده شده.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6140" target="_blank">📅 23:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6139">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
چندین انفجار مهیب در چابهار و بندرعباس
🚨
کویت : امروز ۲۱ پهپاد و ۴ موشک شلیک شده از سوی ج‌ا را منهدم کردیم.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6139" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6138">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای ۲ یا ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6138" target="_blank">📅 22:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6137">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_F8BudiviQW1MDHIm4MmnB7hMzPLJDM5clkYaByqVZndjXRGNtX2QllAy1yO4NPuJQ7fvly3PlZ1iZrWe3PGaQnMW9gOwaBqN7mTxzQkIq-pP7VmY9LvXnGvfvgI0sVqnF8fbr6rEC6dbohgLzmLZ5bFZ2NgYJKALKdz2CbksMB9BnrMZXwRJ6tSeaHzIWCHIdMjXQFYNFW_862hlWddeDh37lg0Jcx_fjns_2zhE5qOLX5XwCMdNJ7M1bTq2BvmWr4GN03db4uHzkGVsQvdNgD-m8Muhke01PcVcuk37WVVMXLJs5DKAZx4Kl4P_C4aI-Lv6brGDCpcQuQLr7uew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">آنچه شب گذشته در بمپور رخ داد و موجب  کشته شدن تعدادی ای نیروهای ارتشی شد، قابل اجتناب بود.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6136" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6135">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e615d142.mp4?token=HljabQS_qzas6_xmDiXsN6-X3lCEXDZYbMvZzQEK0aHJw9kH8Up0c6O-YU3ILTSbYJRhsJVaxc5b8DgJv3G5ji7wdud3wqg-sijCunWEXQZ5nDChxuPEhJ8I6Pn27RqCSeKZCqaW79vCczI_IQ8C_BhUqY-HeCuV4_7buZkInnoldm_KFMOZBGqTnzncqkBqZyAvpPLzrRurgEsZrXc5I-zdnSSU4I10IiHMcXwhznqZUa_Di-x6nWqehlB0GzivYTpcTMGUdmPho0rBuvC4lvJvZnkvE3aUGTxGwYRmLClbxmUx2O_yQfZSum-a658qEFlLEBcg8DCfvXx7646k1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e615d142.mp4?token=HljabQS_qzas6_xmDiXsN6-X3lCEXDZYbMvZzQEK0aHJw9kH8Up0c6O-YU3ILTSbYJRhsJVaxc5b8DgJv3G5ji7wdud3wqg-sijCunWEXQZ5nDChxuPEhJ8I6Pn27RqCSeKZCqaW79vCczI_IQ8C_BhUqY-HeCuV4_7buZkInnoldm_KFMOZBGqTnzncqkBqZyAvpPLzrRurgEsZrXc5I-zdnSSU4I10IiHMcXwhznqZUa_Di-x6nWqehlB0GzivYTpcTMGUdmPho0rBuvC4lvJvZnkvE3aUGTxGwYRmLClbxmUx2O_yQfZSum-a658qEFlLEBcg8DCfvXx7646k1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش بینی تاریخی بختیار
در دو کلمه، برای مردم ایران</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6135" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6134">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=UXuv9htJZz9dNN4Do-YNitbjBUT27yz0_y9q-jdppQTgl2oXF7HpLmgu0Vm933fpkW9sHHbg1zhs-FJnQU952_ELjOf_yUpJRUVG9CBZykk-f6s28MzPw7r73TZ3D24H24-GYk10lZSWBYZW10jieCOxsOIBFKlf_Gt6i-gWlNDZx7KFmi2Mx--7GGYfKy8xXmaJKkiEl41-Q6qgMftE1YhtPLBWQp0zRF5EdCWU4ipknjZ6ypBw9XdLsuvR-Z4b1t1rCyNvQbLqHJMNqBNh3QIQPCITEp5DE7mJnpMcWK90CrENOHgs32LejIrUwX33Nczh67BLC5AmKrxyrAh8T4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=UXuv9htJZz9dNN4Do-YNitbjBUT27yz0_y9q-jdppQTgl2oXF7HpLmgu0Vm933fpkW9sHHbg1zhs-FJnQU952_ELjOf_yUpJRUVG9CBZykk-f6s28MzPw7r73TZ3D24H24-GYk10lZSWBYZW10jieCOxsOIBFKlf_Gt6i-gWlNDZx7KFmi2Mx--7GGYfKy8xXmaJKkiEl41-Q6qgMftE1YhtPLBWQp0zRF5EdCWU4ipknjZ6ypBw9XdLsuvR-Z4b1t1rCyNvQbLqHJMNqBNh3QIQPCITEp5DE7mJnpMcWK90CrENOHgs32LejIrUwX33Nczh67BLC5AmKrxyrAh8T4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی که فرمانده سپاه بود و سالها فرماندهی جنگ رو بر عهده داشت
اینجا میگه مطئنم که مسیری که در ذهن مجتبی خامنه‌ای است، بهتر از مسیری بود که شورای عالی امنیت ملی رفت.
مجری ازش می‌پرسه خب اون چه مسیری بود؟
میگه : نمی‌دونم ! نمی‌تونم که ذهن خوانی‌ کنم!
فقط می‌دونه خوب بود :) یه مشت چاپلوس !</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6134" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6133">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afsnWne__fhbRSOhogtVSa5LXC1pG_nskJIJKDozkBWzDmErKRzSC_UATIqKrw2dL_6To5Za4Vwg67JOGqyyuXGflUWvoy0ZjuEZceLSkYjdGrTXbC3eN9z6QfDsvE0975KW4NP3qmIiupyFgmRqTx9VBFKtspOXQrROlD_Ot19hrPmluBapYkVZBpxFoVrCFECDtD-weBKvCQUhC_VYMrxrcCX-AmmYFv2pDPfoH50_MNKMjio-AVrKq_eYELvRv77ijC4gWN_-s2_oqXI-NVS_v-avLowDC0vUrEirBSxptGJAQSz35ZtVuGa9lZ0AFXSgtBl87ywmh1t8-WqBPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
سنتکام : به تنب بزرگ حمله کردیم.
در جریان این موج ۹۰ دقیقه‌ای از حملات، با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی و محل‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را مورد حمله قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6132" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6131">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حمله امروز به چابهار</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6131" target="_blank">📅 14:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6130">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
ارتش: «آمریکا بامداد امروز با شلیک ۱۳ فروند موشک، آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور را هدف قرار داد
دشمن به مهمانسرا و اماکن نگهبانی پادگان حمله کرد
‏ ۷ تن از کارکنان پایور و وظیفه تیپ ۳۸۸ ایرانشهر شهید و تعدادی مجروح شدند.»
‏</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6130" target="_blank">📅 14:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6129">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
سنتکام : از نیم ساعت پیش موج تازه‌ای از حملات را آغاز کرده‌ایم.
(از  ساعت ۱۳:۳۰ تهران)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6129" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6128">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6QUUWvN5XLyK2xkdzkbTuUBfeli5jRhNQhAYuDXHyczqE3adJlIqPlkkzfMr81snHTboG1fzPHjYuLLB9bwTPtzcSoLJO8Mv_M9d3ZPyytMWFi9Z1kJe3ytXJNYKpoS8RCZ2_s9uTp0mlviCwYVnGz3vbPPiMXhrKFyrqGkyXGz9dOI7KZMNgm9ze69aC-MaDhub6HyTmxt0oBJ9fAWgyyYbgQ0InnpTh_NjfY-xeUxFexe3evtigTmpgB1eZnf_D9ujt_J9AzIsG-KCm_a9sAWncNu80tWFdig2clddx3eFRs7cs-b89cZJ60ydSbbSQN1oMIiWBSLEXtxAX8fQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابل توجه ساختاری‌های محترم
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6128" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6127">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=XUNkZlCvD3kkFl6xQry-0QuSwIGWAENPm2ougCSE8frfVbj3ngJGATRxTfPO0RLQHrhKoO0eM45hbDHyPoF_PfT306Hhdh3mCirzKTbLpdTwKnYn3DyMKZ6Z1t9iyWodTDXpE6YcuGXY_N3_-mRdDILLgDM40DXGEptANUKX7KTaUyYnXtm0habszMdK9X7wxr4GgkNrrfFSBIFiRGMQnYwqnBmykbKQmFH6G1LitZA5pBRR6LbJd7MNfWLwCujzcPdV3VsQFbUgUAAhCveo6fh6TOudC2pt4TuLnXXTdwnvhMOH60YxQkbdO1Lx-MdRGnNMekrobbgj_jFavPgavqTve5F2GCefGWCZVNWrum-8uzjkpJTuv2RsZPPXfzEIy27oDcEXluaykJTpPisAOZGeXJleVfDrSkSbTbUi-85GI5xJ7kTTeMiFfwgI4ExQGIwJPYjTiE8Gkw7kPu_OpLrDDnIAvGNs2UYqFoWOfKpGHt0logYBBzdwQeA5rNkdYD_8rHDlLHGUxPQcp6k_5xKTuyYFE3SkY7Dm-KP6mZxFjTP7kZfKrwRMjZaIhzWkLjz2fpoiSpDbkFI_rydva6mwmBcc4kO72QzE4zI9IEQugvBl_g7f1bS-uxi1UttkmRrAz1UKl1Gc92bndSNTRvoLhujRqkw18ujn-4x1PUU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=XUNkZlCvD3kkFl6xQry-0QuSwIGWAENPm2ougCSE8frfVbj3ngJGATRxTfPO0RLQHrhKoO0eM45hbDHyPoF_PfT306Hhdh3mCirzKTbLpdTwKnYn3DyMKZ6Z1t9iyWodTDXpE6YcuGXY_N3_-mRdDILLgDM40DXGEptANUKX7KTaUyYnXtm0habszMdK9X7wxr4GgkNrrfFSBIFiRGMQnYwqnBmykbKQmFH6G1LitZA5pBRR6LbJd7MNfWLwCujzcPdV3VsQFbUgUAAhCveo6fh6TOudC2pt4TuLnXXTdwnvhMOH60YxQkbdO1Lx-MdRGnNMekrobbgj_jFavPgavqTve5F2GCefGWCZVNWrum-8uzjkpJTuv2RsZPPXfzEIy27oDcEXluaykJTpPisAOZGeXJleVfDrSkSbTbUi-85GI5xJ7kTTeMiFfwgI4ExQGIwJPYjTiE8Gkw7kPu_OpLrDDnIAvGNs2UYqFoWOfKpGHt0logYBBzdwQeA5rNkdYD_8rHDlLHGUxPQcp6k_5xKTuyYFE3SkY7Dm-KP6mZxFjTP7kZfKrwRMjZaIhzWkLjz2fpoiSpDbkFI_rydva6mwmBcc4kO72QzE4zI9IEQugvBl_g7f1bS-uxi1UttkmRrAz1UKl1Gc92bndSNTRvoLhujRqkw18ujn-4x1PUU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سفیر اسبق جمهوری اسلامی در روسیه: مطمئن باشید اگر ترامپ را بکشیم نه تنها هیچ موشکی به سمت ما شلیک نخواهد شد، بلکه عقلای آمریکا با خوشحالی جنگ را تمام خواهند کرد.
کشتن ترامپ هیچ هزینه‌ای برای ما ندارد و با کشتن او جنگ هم تمام خواهد شد.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6127" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6126">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟  به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6126" target="_blank">📅 08:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6125">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lk2Mrskk-glq_7PspHjYERtu_PWxL_pWJ8HIWzFjCesAvPIScOVIHn4-6iphFcbfFsFgJ7iBXIjoRZcX-27GdO9z6Fuzh_NyisckKUo0zMwGfVjwBZypyKbX4ZgeKjRUosFF3XryZSKJYSpjp9TwTgBpxzvhq6WerJ5HpwDVqxVngFQMFkASUDP7Et5yEX_ZX7n69GE3AeLkjOKgLdIR8DD13_6VXYdmRrL1VWhMqD2LtcLvkfYDmLENz55JpftkZxZxLGF5ZFnzabGQXu8FdXk3BtvrRzyIDlKN8ZlIByi3JihsPFfOv3uWWBHTzK_-rLet4FhOM6Y5WLqjRICr_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟
به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت کاخ سفید برگزار کرد.
به گفته سه منبع آگاه، در ابن جلسه که ارشد‌ترین مقامات نظامی و امنیتی آمریکا در آن حضور داشتند در خصوص گسترش حملات صحبت شد.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6125" target="_blank">📅 08:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6124">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=ftzrVPCGUjms8upJYiWhbV53NCWlmh2E6IG6fZ_NW_OHHTjKLiKddKaFZS99j6g-r_GeKAOdaFpUjuNia7HtL-_vsGMTnC4_4RaFub23HtHQdJP_nbsR6JLDoJPdY8zQOZGfPjBflU3MR87JAZQm_z3Fn3ctAO2E5FGjNGkpnYvTYmApLoFQ1JK8BV9TT8lj_eBpMukV9vciPrvbI-3ukFeDj2_KtzErZaI6mqchhW0qTtEB_-2ykwLKpGpe-w_nobY5GrhEerDGWtt3o-90mStvZXNdBy9ibX2QxfuFa5y4AxTqAK_1uynFRLBquSUUrNtfiQSxM1-rTGOhFV7AlY8WOUTNzY9etEXJjVbvZ8UMauqG6U6RFrHnOrPDlzN6RoMeflOqKzLzunM58s47MNAcbOs9Iz6Ubwc53vr9llfrq9qaPnQ8acUYwMz1Fo6o0n38W6wlRwwi7iLje0QTfguInHWBA2_vEPeUQMAxbWOLa85_JT13JVPXoEqCC9-1gE_RIKhlpINcvDvPxhwuhblHYwyG18p79fc3q-XBCdPKyb29rffgOPDurzB4tpUXjGEGkhPwANcfZCX9RTNSsKtoIpwx79WH8zbbfED-F8wd47FUFo3mdAwp-252FfZCvKU9d7rVTq9PuzwZG7ipJWtqwzbYat6jlGrnuD0-rWE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=ftzrVPCGUjms8upJYiWhbV53NCWlmh2E6IG6fZ_NW_OHHTjKLiKddKaFZS99j6g-r_GeKAOdaFpUjuNia7HtL-_vsGMTnC4_4RaFub23HtHQdJP_nbsR6JLDoJPdY8zQOZGfPjBflU3MR87JAZQm_z3Fn3ctAO2E5FGjNGkpnYvTYmApLoFQ1JK8BV9TT8lj_eBpMukV9vciPrvbI-3ukFeDj2_KtzErZaI6mqchhW0qTtEB_-2ykwLKpGpe-w_nobY5GrhEerDGWtt3o-90mStvZXNdBy9ibX2QxfuFa5y4AxTqAK_1uynFRLBquSUUrNtfiQSxM1-rTGOhFV7AlY8WOUTNzY9etEXJjVbvZ8UMauqG6U6RFrHnOrPDlzN6RoMeflOqKzLzunM58s47MNAcbOs9Iz6Ubwc53vr9llfrq9qaPnQ8acUYwMz1Fo6o0n38W6wlRwwi7iLje0QTfguInHWBA2_vEPeUQMAxbWOLa85_JT13JVPXoEqCC9-1gE_RIKhlpINcvDvPxhwuhblHYwyG18p79fc3q-XBCdPKyb29rffgOPDurzB4tpUXjGEGkhPwANcfZCX9RTNSsKtoIpwx79WH8zbbfED-F8wd47FUFo3mdAwp-252FfZCvKU9d7rVTq9PuzwZG7ipJWtqwzbYat6jlGrnuD0-rWE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=MEPUzDOvVnJuc7RD6ddkmS3xDGILKLvpNdz51Z90c5s_i1eWsMU2FJJWvSnyOKvSI7GRm1PAY-zNKplrCrVA2uSPmXQkB4eXVrgxO-6P004ZTJtAbP4GzpnaZdjvTJ2TtJAgRNUk0c7TtzZqEnLVuljLOK-Jd5B3Ht3KIJ06njudX9kh0LRzMuFdV4f6snNWk4Vi3tylbl731mG8qeg4wi26TR55lF2FNvQsFtRYKMewAwCzckw74kwgUlobwxEzFmCaHAOmzD31omK3185NVEf-ux-YgENeme4_M2apmPhfngvESEot4MpCCM7k5q8o1lvbUFwvyXCe4zgZKBhsFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=MEPUzDOvVnJuc7RD6ddkmS3xDGILKLvpNdz51Z90c5s_i1eWsMU2FJJWvSnyOKvSI7GRm1PAY-zNKplrCrVA2uSPmXQkB4eXVrgxO-6P004ZTJtAbP4GzpnaZdjvTJ2TtJAgRNUk0c7TtzZqEnLVuljLOK-Jd5B3Ht3KIJ06njudX9kh0LRzMuFdV4f6snNWk4Vi3tylbl731mG8qeg4wi26TR55lF2FNvQsFtRYKMewAwCzckw74kwgUlobwxEzFmCaHAOmzD31omK3185NVEf-ux-YgENeme4_M2apmPhfngvESEot4MpCCM7k5q8o1lvbUFwvyXCe4zgZKBhsFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6123" target="_blank">📅 07:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6122">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=NPh0YyTi1Voqsy6Fm3OfZBYGNmkwjrp9n3c6AtZtDM6T0oQM-2jk-VBiLdTydFnEx4UbA9jOZey2PyvhbLQpzomFFDYCKylsMtmHAWoUKrwaLArhX-MoAsO4rV_3hYPJLY4FZNvu6WaablFevQx5yY79UWmpiAZog4oLwl7RK0WXE6_QmQakMoofxqyDO8b6NzwV18lD1z9LKvdjj9jZV-yQ5zLHJl94n_8uOX_ehG9gOEoUzv1gXfJ_G8FXkS_bKXolrEjFLMD1pgmiE1LCXG96lxiK36urQUDmvYmNzOMGDWzVJfIuJm-8KXBtKmLNl8BtN5vyVPlpe24G_fBqQ33wCGQKWK6MpU2vyzL0vTzeriyhi60_NWEMWPp_RNia7aJnf--GRZaYB1JetEP4BV6ZIihPr8OgjdWKbOUgdMkSz1BRsJsvvCY_zSTdWLwBMyy_O3iKSaXK0qWP8kpgAt46MhAyA0NVvyasfm05lwLAT7pXzBHkBKK-tcjckmBCjlJRr3CBB-4-IADpayRLP2Qckh75CevLLFhQ92XG41BL7hLY4QeX-oSiLT_sb0wSmHtPeT1-VuN9vVnx-d2J1V7IxO0aogukuGtk0j5Dk8miCF9hps9fL1zXd8591OH3WX67gyHOWsheR_O0EI22OlnFoKJJfkfS1p8SDoVbjig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=NPh0YyTi1Voqsy6Fm3OfZBYGNmkwjrp9n3c6AtZtDM6T0oQM-2jk-VBiLdTydFnEx4UbA9jOZey2PyvhbLQpzomFFDYCKylsMtmHAWoUKrwaLArhX-MoAsO4rV_3hYPJLY4FZNvu6WaablFevQx5yY79UWmpiAZog4oLwl7RK0WXE6_QmQakMoofxqyDO8b6NzwV18lD1z9LKvdjj9jZV-yQ5zLHJl94n_8uOX_ehG9gOEoUzv1gXfJ_G8FXkS_bKXolrEjFLMD1pgmiE1LCXG96lxiK36urQUDmvYmNzOMGDWzVJfIuJm-8KXBtKmLNl8BtN5vyVPlpe24G_fBqQ33wCGQKWK6MpU2vyzL0vTzeriyhi60_NWEMWPp_RNia7aJnf--GRZaYB1JetEP4BV6ZIihPr8OgjdWKbOUgdMkSz1BRsJsvvCY_zSTdWLwBMyy_O3iKSaXK0qWP8kpgAt46MhAyA0NVvyasfm05lwLAT7pXzBHkBKK-tcjckmBCjlJRr3CBB-4-IADpayRLP2Qckh75CevLLFhQ92XG41BL7hLY4QeX-oSiLT_sb0wSmHtPeT1-VuN9vVnx-d2J1V7IxO0aogukuGtk0j5Dk8miCF9hps9fL1zXd8591OH3WX67gyHOWsheR_O0EI22OlnFoKJJfkfS1p8SDoVbjig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا میبینم راست میگه …</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6122" target="_blank">📅 07:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6121">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwIrDISuRWdzbyGjIOTzBaLDguVGMywSHsm3qWGtjLuL2BfQl1nN53GaZ0mFQLG5AdBMhuh-4unZJzwWphBBLUZiJdUzAeqwfVCUY_aKK0S9CmvesvkMIbRAFsqpaMlY2OgBbkE4xPCo29WrAFoHQV6t6wJtR9b_2ACBIjPB8Jjd7RFnG-tUAiwFPhBKeNrNrA9uc-VY3ic9qJvqhuGFrqewoap3D8JqQ4iWO3Tr9JOBa8lYzUcgbd-p72sngXER6pQNRPXMRqRFgzFlfL-QYzYsnveKER0GDVoQJLje4qv0mbz07MaV92ppAZuLDeqgNIAxXBp4PCPcwm6g4qXehg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6121" target="_blank">📅 06:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAv8iMMfpBjWF-PerlHr-7U2BQORku-awjDDPj6Bw2J5bIWsaY2nHB-esv5yrGpvazyuZXCx_bZPJzs5weEOJFAQFOZci9_ncyAQ9ZV9zV-1aqDSufegHWPPD_ZnzYwhOZyZPFL_kZESAHHRd-WEpcKLRil0eXZElCizDJeeweanZ004IP3xWIt87mGOxgR4tDo63bs_as6prmtyCxJrV36kxSXqv7fFYfjpGNKpDnr6hgWDqqKqrr8arv9AJ2TKoMc7JUCkk5yQf4QJ-NnP--TPjc-rITiXblyj_7puRs4cBZLfxT8G_fV4psQTVS5eUWlMNb7Ig8a4-aoE7ZSnIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6120" target="_blank">📅 06:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6119">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=GF6ld030l6_jjvxr2tsyzuAg0vBNGJGML56I3i3euqb2jkKKgGfW20pygF1fJ__0xjPEEdibU21JTsvsT4G-pY_Z8tc9l3KNENA9wrtWbQU71MEv_RXlg08AzhUi-cVhb5VBWtfVNRXHoAOTlLMFxY2wBc3DLdr9K_vTpLQAuWRsRqEkPPvth5TZgHDmpgf8UQwOTnRzFLvk5Uvt8UF89x470GRyEin9Yw31Q9oBCWPt0EDYrK3z-vhJ72Ppdic5_TLr9aklHU1LzpK3Ef1drkVV52E71jm_i1ftQIEiU6D2GEZ5ssqrijGjq64fuAwk4oCYUziD5A7BdA0sbEyYRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=GF6ld030l6_jjvxr2tsyzuAg0vBNGJGML56I3i3euqb2jkKKgGfW20pygF1fJ__0xjPEEdibU21JTsvsT4G-pY_Z8tc9l3KNENA9wrtWbQU71MEv_RXlg08AzhUi-cVhb5VBWtfVNRXHoAOTlLMFxY2wBc3DLdr9K_vTpLQAuWRsRqEkPPvth5TZgHDmpgf8UQwOTnRzFLvk5Uvt8UF89x470GRyEin9Yw31Q9oBCWPt0EDYrK3z-vhJ72Ppdic5_TLr9aklHU1LzpK3Ef1drkVV52E71jm_i1ftQIEiU6D2GEZ5ssqrijGjq64fuAwk4oCYUziD5A7BdA0sbEyYRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام فیلمی از حملات خود به ایران منتشر کرد.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6119" target="_blank">📅 06:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6118">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=CpzCcFSXF2IBgeM8B8p2z6p6KZAHYthUOy53y9taxXe5Posp4yEpG0vhkmZ76F8ZcM9vmG0I-RHEnUpZMzv-Hd7dnBnOPylEmfiLGNOwZ2LjM3HFD0hk8FUld2_BqNv9KH-zc5gqJRIqcULsBfL9_B2AiLz-tCqW0T3bVr6gZ7elctjwcdF20zHQH9PE6MFXqkdL5OqLioNnrbTsewRIYBoKaIpsfg766DhllcLDRWXRvBrVCZt2PWamcdj102aizOm-qn7kMER39d2ebQ5CahfALA-XFC0qZaoMCC1OpqKNtc3RBxjK_tVOa9q0b0Ri6xYMoiW5V4VXg6Qi_pTmJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=CpzCcFSXF2IBgeM8B8p2z6p6KZAHYthUOy53y9taxXe5Posp4yEpG0vhkmZ76F8ZcM9vmG0I-RHEnUpZMzv-Hd7dnBnOPylEmfiLGNOwZ2LjM3HFD0hk8FUld2_BqNv9KH-zc5gqJRIqcULsBfL9_B2AiLz-tCqW0T3bVr6gZ7elctjwcdF20zHQH9PE6MFXqkdL5OqLioNnrbTsewRIYBoKaIpsfg766DhllcLDRWXRvBrVCZt2PWamcdj102aizOm-qn7kMER39d2ebQ5CahfALA-XFC0qZaoMCC1OpqKNtc3RBxjK_tVOa9q0b0Ri6xYMoiW5V4VXg6Qi_pTmJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : امشب، فردا و فرداشب به سختی به آنها ضربه خواهیم زد و هفته آینده پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد، مگر آنکه  مذاکره کنند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6118" target="_blank">📅 06:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6117">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caeb092620.mp4?token=UEHaymTrw_QTEiMopIktlrdWquEqWd00TKxj8yCp6lwwmxwdU_iLZ9dgD90RWhYrz494czyG_dIf42mz-r7QcwxLlSJawyH_PA-EPEadhws1RYgcJwZWBOnsEsChvPJyVp1gd-mScfdzStmFPX92sRqrMenlkUWr2zhYb2b7AALysb5x9AYZUOJKtU-eWaAakj6h1xyimYAd00z-h6QMr6iGxJYGyswJBuPJqZ7T5Kd0vPqJ6WDdoy7e95VQpcpHBvdyQ-2uTemQCSL3J0MQZ8DpljmIi-BzIduepwrDOllhg4C5UedEmrQsiK63qyuY6DYgKAbREAHonjpG5vTE7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caeb092620.mp4?token=UEHaymTrw_QTEiMopIktlrdWquEqWd00TKxj8yCp6lwwmxwdU_iLZ9dgD90RWhYrz494czyG_dIf42mz-r7QcwxLlSJawyH_PA-EPEadhws1RYgcJwZWBOnsEsChvPJyVp1gd-mScfdzStmFPX92sRqrMenlkUWr2zhYb2b7AALysb5x9AYZUOJKtU-eWaAakj6h1xyimYAd00z-h6QMr6iGxJYGyswJBuPJqZ7T5Kd0vPqJ6WDdoy7e95VQpcpHBvdyQ-2uTemQCSL3J0MQZ8DpljmIi-BzIduepwrDOllhg4C5UedEmrQsiK63qyuY6DYgKAbREAHonjpG5vTE7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ناشی از حمله پهپادی امشب سپاه به کویت
گفته می‌شود مخازن سوخت ارتش آمریکاست.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6117" target="_blank">📅 06:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6116">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360d24e506.mp4?token=H6i_RAJozUmU8N7IItFpa3cAyIW2x2CAYN_1XplWDi8srlGAg6iMG8G5etrZBE754qB_we9mH_VO4qvpim7QqIqlAbyKIi2xT14zgA5EPn0oMobptSmpbIbGsy1wF8poZYAoJFoHySzBCdmqvDcexj_rpT2kt_-RwDuGCyqNvvIJrBqwiWbnMWr-fjVD7Zw74v6Cnzg32UxbBAc_zX3VSUBY_etM3pbh3s58sQeMDxNCfMDOD5rLpo7l6kAG12TvjH9_0XVfPmHbC2XkOhTK5Els7DtmZr-zWD9BF4cGgGK-2j1KHORGtPLOkK902ihdkpv-6mhOs3osEkC8sNWKLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360d24e506.mp4?token=H6i_RAJozUmU8N7IItFpa3cAyIW2x2CAYN_1XplWDi8srlGAg6iMG8G5etrZBE754qB_we9mH_VO4qvpim7QqIqlAbyKIi2xT14zgA5EPn0oMobptSmpbIbGsy1wF8poZYAoJFoHySzBCdmqvDcexj_rpT2kt_-RwDuGCyqNvvIJrBqwiWbnMWr-fjVD7Zw74v6Cnzg32UxbBAc_zX3VSUBY_etM3pbh3s58sQeMDxNCfMDOD5rLpo7l6kAG12TvjH9_0XVfPmHbC2XkOhTK5Els7DtmZr-zWD9BF4cGgGK-2j1KHORGtPLOkK902ihdkpv-6mhOs3osEkC8sNWKLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی با موشک‌های حاوی بمب‌های خوشه‌ای به بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6116" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6115">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
ارتش : به پایگاه‌ها اف ۱۸ های آمریکا در اردن حمله پهپادی انجام دادیم.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6115" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6114">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‏امشب اتفاق جالبی افتاده، به محض اینکه خبر انفجاری در شهر و استانی منتشر میشه، مسئولان جمهوری اسلامی سریعا مصاحبه میکنن و میگن دروغه و همه چی آرومه!
‏اینطوری مثلا میخوان صورت مسئله رو پاک کنن.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6114" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6113">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcrzIeIjIblNPjt2T_Zp9vkzU9S9kchoPLOXxHdkdnR-V9IFvWoGMxWxG7tPd3TSykXPcoaZRSenToepU1CQeMsYZq592rFWuS3e3XEz57pDfRKAN31UpeSqQO-3EWVvit1HP7Dqz8ld5PH4KNb9idNAGS-v50h_AqMAkTC8jqcuDCwQNbH28uCGPbhAHtBDPh6Aryy7XjkQy-nA0hcyiIiOuzq_GaIwMSVPYv-OiZJZB4-AXenyP_-Mw2WMkZOED40XYRhVvuzhe3n_z0ZtNDPCYyg2hHMu-piPRUznMKobPEbiYSa4og6MO16OYKXyUzC7qRPCr7ISjx8Tb3yyPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگارهاشون می‌نوشتن که کشتی‌ها دارند  از مسیر عمان رد می‌شوند، تشییع جنازه،  بریم و کاری کنیم که  کشتی‌ها مجبور بشن از آبهای ایران رد بشن  و شروع کردن به حملات به کشتی‌هایی که از مسیر آب‌های عمان میرن.  به زور حمله میگن کشتی‌ها باید از مسیر ما رد بشه.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6113" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
