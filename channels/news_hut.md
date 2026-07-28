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
<img src="https://cdn4.telesco.pe/file/O4y7_nVToHYxusaREwx8d8sM7w88xMfGmuipw6sHA4rsD13pkL1H8wz0s-2IEDirmsw4oNLAfBGEm5BxhFL8ArH7jiSRawffylSnKV7F4z885ms-dDmPB5VKZW2TGRlKC7P6W0VhhYhb-fPK4z9Jq2QVGGa0DC0w0iz6oq-rBVIG_5m7R_GrRgSNb3Nm9mhWSmvRZMvJIf6HEJLi20OUMYMiPhVWzQu8894Q9SOLda0nnQftnrMuxEk6AxuspOZm5jgfOCUFWK9Vg9hKz0pm_qF_u8ou-B3rT6DRadscfnnh1aC1OEas5PBmvA3tQr5jaXcH9vrbgLh6pump7ftLjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 146K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 08:43:33</div>
<hr>

<div class="tg-post" id="msg-69099">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jdsbe81osTFb4pOrF4_Uo6icxw-Q09sFiWXlnPoajV_h0TDHeDQNoX5k8rZPDljX5bDu9Qy2--x0RoxUVlJULqhSzd54MhIJvcYKp2biD8L7n6XnvAEXpTKA--U3p8IgT2xRAFNO9pMEOUXPbmLjb42yJy1D_jG8AmzdO9TRxk6S4JH3yBC3ptHRjvnj1HKk-FZBoST-yVCC37fxCKefLxSumde51pChikq97NSTRkx7V2IEcC49bOswwRjskatp5LNEV_U8Uhh02wKywJ0Yl5xaY-yM3FQ10KVZ0fp235DRAhXCgaQahwf4Yf-mjtl_yrd-JZhwhBE8S1WVEUxFag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nuTsAa_5IKnvSpKWmhS3iYcWs6W8Nxk-Zm2IBu6rX6lPA0ElL-ra_APo9C44m75YTdxZUv_Lge1UwKVsCmshMSam7spnmdBlv4-jZw6YMI2qeFU5T-PfF1bI8bHniqC_HX4YprSbNn9RN3hxHd1KSNjS4wExIga36bwrDFIkWnfcGNrU5k65pkh4SSas3qtIDN_bMVa6oDkx1lvyYeJkGi-U-mpziCium9sLiqmy2Pzvk5oIrXG00giCQnDqxpR_v6OdcMSTFAb63ZQjXCVspRvLNNw8bo_iaqEGJ-qgTsqRrA0PJ-wa3FBUEimaBKJhIkUygCbNk4DaUA1pd-aNcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتان گرامی جانفدایان میهن
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/news_hut/69099" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69098">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">#رسمی؛ جمهوری اسلامی دقایقی پیش، پس از اذان صبح، ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری را اعدام کرد.  @HutNewsPlus</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/news_hut/69098" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69097">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">#رسمی
؛ جمهوری اسلامی دقایقی پیش، پس از اذان صبح، ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری را اعدام کرد.
@HutNewsPlus</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/69097" target="_blank">📅 05:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69096">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">متاسفم برا یه عده که ذره‌ای شعور ندارن و چند ساعته مدام در حال پخش انواع فیک نیوز هستند، بهتون کاپ طلا می‌دن که خبریو زودتر منتشر کنید؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/69096" target="_blank">📅 05:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69095">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f40f91b5.mp4?token=ogt0YlaIZYKOiSgZnvcR5N8kChf2NkRD_4sCSGM5fh15APFfjByoGRp_1H8tmurXgG-crAwT_1KZftZcOpdw3KsnlhN4NsF7Y19nETOl7jfBD3ztLjIBlS59Jgn6vU250gbyQxqiElvtWENH2dVwsxNtsPX2XAnXRg2kJTqzZgmPUC-YH6yv6m2Md7IAF8swfYuHDkHlUSz9-2hhZWBbFUVg87VjBKQ7Q6DORCjzW28wCqiCO1UcPIjDUI-S-fd825_n31ershEB5ssv9jbA6Qic1Mq_NMc9AbB4tM3DphX8pi4_AQae4cwQicD9ow8htswBZ5bZLXyzn_GoA_UHzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f40f91b5.mp4?token=ogt0YlaIZYKOiSgZnvcR5N8kChf2NkRD_4sCSGM5fh15APFfjByoGRp_1H8tmurXgG-crAwT_1KZftZcOpdw3KsnlhN4NsF7Y19nETOl7jfBD3ztLjIBlS59Jgn6vU250gbyQxqiElvtWENH2dVwsxNtsPX2XAnXRg2kJTqzZgmPUC-YH6yv6m2Md7IAF8swfYuHDkHlUSz9-2hhZWBbFUVg87VjBKQ7Q6DORCjzW28wCqiCO1UcPIjDUI-S-fd825_n31ershEB5ssv9jbA6Qic1Mq_NMc9AbB4tM3DphX8pi4_AQae4cwQicD9ow8htswBZ5bZLXyzn_GoA_UHzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردم دارن شعار سر میدن
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/69095" target="_blank">📅 04:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69094">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دفتر رضا پهلوی از جامعه جهانی خواسته هرچه زودتر برای جلوگیری از اعدام معترضان در اصفهان وارد عمل بشن!  @News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/69094" target="_blank">📅 04:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69093">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دفتر رضا پهلوی از جامعه جهانی خواسته هرچه زودتر برای جلوگیری از اعدام معترضان در اصفهان وارد عمل بشن!
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/69093" target="_blank">📅 04:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69092">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">لحظه‌ی اذان صبح و آماده‌سازیِ شرایط اعدام، در میدان علیخانی اصفهان</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/69092" target="_blank">📅 04:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69091">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">باز می‌گن چرا مردم ایران دین‌زده شدن، شما یه نگا به کشورای عربی بندازین، مردم، حاکمانشون رو می‌پرستن، بعد این شیعه های مفتخورِ بی‌همه‌چیزِ خرافاتی، جوونای مملکت رو دارن تو ملا عام اعدام می‌کنند به بهانه ها و دروغ های مختلف، همونطور که ۱۴۰۰ ساله چیزی بجز دروغ…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/69091" target="_blank">📅 03:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69090">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">باز می‌گن چرا مردم ایران دین‌زده شدن، شما یه نگا به کشورای عربی بندازین، مردم، حاکمانشون رو می‌پرستن، بعد این شیعه های مفتخورِ بی‌همه‌چیزِ خرافاتی، جوونای مملکت رو دارن تو ملا عام اعدام می‌کنند به بهانه ها و دروغ های مختلف، همونطور که ۱۴۰۰ ساله چیزی بجز دروغ و خرافات ندارن به مردم بگن
#hjAly‌</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/69090" target="_blank">📅 03:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69089">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/780d746559.mp4?token=vTxt-jX5uNMRWlgvA6BN2Nvy8G0nSWvUL9H84ZS3ecPaF9bNp0VKmqfR4NyeoMor-83xAUyLbl2QBN1QJrTswQpM-U0m0UD4U6JYO0-dmR9uFisHILMGOByPj3HkJzH0_hXo3yjml9i4XSo-j04wlzn1c-zJjqRJ8EHkmvaLT8sreV9S6EUqtG9TJPXOVDurALpQjLNHzDm1bi3KgfK0anlSGXdGT6n5cHP-ZDq64gwe2Tj1HazVZaoy20x-uKgNsJE3_YZTJV_EkCaDnAnaY5leyPL1qJQpejP_gPR_OJTvPXHNQ--8u31u8041-KkK-Kwp3g4bENGFFVvLQxj4mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/780d746559.mp4?token=vTxt-jX5uNMRWlgvA6BN2Nvy8G0nSWvUL9H84ZS3ecPaF9bNp0VKmqfR4NyeoMor-83xAUyLbl2QBN1QJrTswQpM-U0m0UD4U6JYO0-dmR9uFisHILMGOByPj3HkJzH0_hXo3yjml9i4XSo-j04wlzn1c-zJjqRJ8EHkmvaLT8sreV9S6EUqtG9TJPXOVDurALpQjLNHzDm1bi3KgfK0anlSGXdGT6n5cHP-ZDq64gwe2Tj1HazVZaoy20x-uKgNsJE3_YZTJV_EkCaDnAnaY5leyPL1qJQpejP_gPR_OJTvPXHNQ--8u31u8041-KkK-Kwp3g4bENGFFVvLQxj4mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میدان علیخانی اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/69089" target="_blank">📅 02:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69084">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZlqrKuZmVX9yitzN7jA9vC4oIecmreKk8purk10CfNZQ1kZ0XgID6iUMHofN9f1aR3XwfNrnb4AWrFuwQgcLtnu5F4bnvE9klPXHCYuGukPgkZEzAD9QVPG9JF6FAEnFGu1pXrXtmVVodHu3Y4verYCnW6KH3EPL9_GBEXZmkFGEW7yhdisomZDpGl9MTaeBmFZoxpl6SvMkxmNqNIqsSFa6UbDndBDLOun4d-WJUoDM2cUaYYYHk6IsrC1SiXiPzKKl6_CfM6PbuBcb8pgcmaspoIt_FzCSKi6YvpGM2zNZb2lOuBeWmGnOMylM_VlDH9CipKF1BN0XaJS_FetPTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IjnRbPL0gKmeSVRIQ55ydtleZndlWRy6dSheiLBi0Kqnjv2boqwUZAUdLZlQJa_SMvpSJMmN4X-_ehHCzJn3Gdg4hUwXmmD5lFU9I-bGq9_5nApDjfMCYdl1HSVkaPFIn8RKVhx2nIwmg74R_l7ThqjFNHIlLkAboBgd1yoGWvtzEZoiU7PCTzVpBOAnfESsBSNCeud_mTlKBfosvYCYOVAy5dvziRDsXz8P3akoSaz0RoffxTblXc-RDdYr1j3XE5NHgGUFUm9yH887GbS1KXqga1877cLhP86AtaT64LeXdR97or857RZn6s7inMoeWEBmKO4b3KZodGa49_jLIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H-aIQnU62DOAuH9pBxeg9zaDhtoYXSj-Zfe61HSKQiWCI1RgKvV_v3G3k0Xi1QKWrg1e_jiwJMg8zJjg_-NeP6k8xpEcp6Is8jZmXKiJNoQs-3XRjB0GhkNEabhvztlXrWwmtTqNsN_uerNpCNkjbnMwBfwlOwwXuRPXKaI3KWX-727AOA0uawy9vXaXirvqAAnVccOPzGgOO01maqRqWQ0374Uurr5nfAWaFSBgPGY3mRP0Zpy-GYZlmNwd_6UmY_2VVt0CWY_3FT4qpzFrCgvhWf76jWbmRWQLNacZQZjvPFpNr7q3UNbldo6k-VbD7ImdS1KSKfvbTysma40BUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491b6de7b5.mp4?token=e40-PYmRHc-UiBy_VT5pi4rVjcvR4wasmJD2iemt7q6RNXyOAS9iBamOnCGbxvuLzP4iKV5RLkhWfNVWq-B_EXPduIeksdvKJFs5OBPoRaZB07nTaBZIwrGtpjrCwluhXwab54PWWRS6PUGG9yoAgjtLsP5edUefJa2gqy2h8Yv-PgGqgaUj9bI3qjv3l00znZAvr_Ih6q33F-yjieEZxBH9LFaDjz9dTrN9IZJ4aHORhiBeOhzikixWUnShABCRg6SOLkzpsTvq_Y7vRetinloKbNLOoVuFduY_TfBN6N30XBnbWAtmCF11vNhmtFwdgYUtQ_NZXkJ10f9om7TgGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491b6de7b5.mp4?token=e40-PYmRHc-UiBy_VT5pi4rVjcvR4wasmJD2iemt7q6RNXyOAS9iBamOnCGbxvuLzP4iKV5RLkhWfNVWq-B_EXPduIeksdvKJFs5OBPoRaZB07nTaBZIwrGtpjrCwluhXwab54PWWRS6PUGG9yoAgjtLsP5edUefJa2gqy2h8Yv-PgGqgaUj9bI3qjv3l00znZAvr_Ih6q33F-yjieEZxBH9LFaDjz9dTrN9IZJ4aHORhiBeOhzikixWUnShABCRg6SOLkzpsTvq_Y7vRetinloKbNLOoVuFduY_TfBN6N30XBnbWAtmCF11vNhmtFwdgYUtQ_NZXkJ10f9om7TgGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بامداد سه‌شنبه؛ تصاویر از وضعیت میدان علیخانی اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/69084" target="_blank">📅 02:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69083">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7f398a76c.mp4?token=l_K9Oi3Hxcaw7YKxOrpAKfovJ2ZUB3WN6CGaIF7YdtBQyvFrnF4ErAelpPjUlYnrqGkSjju04fA4oZiurbRgO3WjwmvJMmA8E0YZ42Fr575FCYGGvs8TJJfhmotmf_ucmB_plTQgz2kfjiIBX0xQRWN05-N3WC70-V7FHSZg3B-rTfzazvFT5i7927mAV9quRVY8J4RWrn54zx6mpTp9ekbpP74KciZwZzbxgYN9SYe9lrYMQZBcO0-OWlELhEQrufGAll_u7c58-W1pdqz6iTd480GlQh_VBYZ-3hy25ef8uUJ_bywKcF6Fon0EJjdOxiTLOqLRwOG1INryxmQD3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7f398a76c.mp4?token=l_K9Oi3Hxcaw7YKxOrpAKfovJ2ZUB3WN6CGaIF7YdtBQyvFrnF4ErAelpPjUlYnrqGkSjju04fA4oZiurbRgO3WjwmvJMmA8E0YZ42Fr575FCYGGvs8TJJfhmotmf_ucmB_plTQgz2kfjiIBX0xQRWN05-N3WC70-V7FHSZg3B-rTfzazvFT5i7927mAV9quRVY8J4RWrn54zx6mpTp9ekbpP74KciZwZzbxgYN9SYe9lrYMQZBcO0-OWlELhEQrufGAll_u7c58-W1pdqz6iTd480GlQh_VBYZ-3hy25ef8uUJ_bywKcF6Fon0EJjdOxiTLOqLRwOG1INryxmQD3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داربست رو نصب کردن و جرثقیل هم آوردن و متاسفانه با اذان صبح، این جوونا اعدام میشن
🖤
طبق گزارش شما مردم وقتی میرن میدون علیخانی و می بینن مامورا اسلحه دارن، جرعت نمی کنن کاری کنن و فقط نگاه میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/69083" target="_blank">📅 01:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69082">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=GC1Xw8Cj2OJA7MMbnJFL0jSiaa4qnMzKfdeQA0Fb1NZX6hI8x-fDteF_0qIxrtwilI-6v-BserQEMZ6YZuNlPp9ATqO4-b0Gvy3_ChAu6fYMe22J1As_2Eg3QrZOaNQuWJI8pG8RGmfg9l5moDmkSEPhMW97G20N12gp4VyDyc0pvTsA4bZNdqZ3MzvmycPCBkzegE99j2zCc8KzuSvSywHEXBmmxm85r1eb1J1sprkLdYeRcKNPzUn0xQ4W16I2uZNd7S2PB2g6y-S3U6QvBbb0V54YnJMgvkhIkpyZUirwGuiADEIckvb4amiuEHRKT_AiHio351fm5Ng44AeNZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=GC1Xw8Cj2OJA7MMbnJFL0jSiaa4qnMzKfdeQA0Fb1NZX6hI8x-fDteF_0qIxrtwilI-6v-BserQEMZ6YZuNlPp9ATqO4-b0Gvy3_ChAu6fYMe22J1As_2Eg3QrZOaNQuWJI8pG8RGmfg9l5moDmkSEPhMW97G20N12gp4VyDyc0pvTsA4bZNdqZ3MzvmycPCBkzegE99j2zCc8KzuSvSywHEXBmmxm85r1eb1J1sprkLdYeRcKNPzUn0xQ4W16I2uZNd7S2PB2g6y-S3U6QvBbb0V54YnJMgvkhIkpyZUirwGuiADEIckvb4amiuEHRKT_AiHio351fm5Ng44AeNZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از آمار تا پیش‌بینی
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/69082" target="_blank">📅 01:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69081">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhBuQGyyPr6eyWJcmt_U5zLfLqYKjafqXFgIH6Buz0TMYOC3AwGpZji_GnTMXCtf3jqBjHh37TDJ6N4b225ehR8aIBQ2iB4uxBiT1lmbsEEG6j5NhHl-cFYk1xLtlSFH4_Crds3SgkJk35__b-vOjB-27rzQYa3UQ0qGigK_IV40EBcyyhdLVEEdRr0CuAHfX2SNyrI1u0gb7d10HXooAwq4o048XQcWZPzttU2I-Dp4ETf4w2ml6vD7th2kBzpcVCg-NGbpvoKMUznmE06ppypFnjj3pprRRoammZvU49kIu81fe6_df5SkqeUh3WaxiC7iwxziXg4YK2TE36Q-0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنر نصب شده توی میدان علیخانی اصفهان:
«هیچ جرمی از نگاه قانون پنهان نمیمونه، دیر یا زود عدالت اجرا میشه»
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/69081" target="_blank">📅 01:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69079">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sSiitJHnnsizCihsCX1SA-2B_HL1Fj8rL9cOJbn8268E9xV3C10Kuqv5c9iZ-Gcd12uxFML1J_BYsoFFQRrp3utI38C70hslJ8SM7ITTH_wSnNwHWP8PvcpgrpgfIeXqk41WTttbYogGqO5lza6qET2-EP67OnS4QrxWf6sbtinWZh-p-I-ozYVMGynbjSxX1BwKrv_R1iiissgrhZbsIckRmB6kO8tOUdeQ1xp3XRvq0_MFO3ipBBFLMPojYkFOETFuwzWO39cPMhpYNtNCV5-DGWt4m6MIFokhhzO9X1omUr9W5P9mI913n-QxFaevE70YmXzoDZ8S8Bsza0p_ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DbA_XbCnOEGyMVzXmEvO36VBUzs5nB4B5bTQDw4QjiBXusKM_PDE78X5JOZINGZvwkYiwUHbYloSpa52KKpA208NlmwSpuhaXd-EMmcA86xJekr9QgN0l7CSFCRXXIPLbeMI1ZO_aJOvsKqjW88Pl1vKqFTycCBfqvhYRfqkGKeOmlMLbvZ8Qo8AvGZR5XftpOUsCNQrAWBruA6Q4VLXfl7AqALKX91ZqCmKUjOH0oG-hT_USur78dd8_A83B3rnfm94uq96DYrNG35GI484diGpmP47ByKT_ZRCtBDdL_0glg47jEuuUUfi3V5JKxh-Yypyi8PhJHwPg0RID7svtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گزارش ها
توی میدان علیخانی اصفهان داربست نصب کردن و جو به شدت امنیتی شده؛
طبق گزارشات ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری از معترضان دی‌ماه و پرونده میدان علیخانی اصفهان به انفرادی منتقل شدن و قراره توی ملاعام اعدام بشن!
طبق گزارش ها این سه عزیز آخرین دیدارشون رو با خونواده هاشون داشتن
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/69079" target="_blank">📅 01:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69078">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3738c7aef1.mp4?token=e35AWVXQdPdGK00CJxmkPwkL2NOLYtqDnJSS0mrwC6jje9OT5wDOqeyn3zx3-B3PqeKVjN1-EL-abBZ_APT-7ZWNM1hAI6NXCNtnp8fmGerIfzOrDgeATuaNkKGal0W4fRqqABhaQTFhaV6qjYIDRphDO_3oZmntJV4DCAN6n8QuQ9WA38WEgQybFLKxxWIxkQf3CRSgWQGhF-PDfMRyUdc26-bo6Dp-4pRF7yswjvPtkF9iCH9Af5yYnctE2VN1cvqXNC-zgyrDnIIQ6YgGp8fFrpCcArpI3mwsHEjYqsF6BzMSxX-2cjlF9n0ZT2G1Th6QJtcKn6kS4tq945yaaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3738c7aef1.mp4?token=e35AWVXQdPdGK00CJxmkPwkL2NOLYtqDnJSS0mrwC6jje9OT5wDOqeyn3zx3-B3PqeKVjN1-EL-abBZ_APT-7ZWNM1hAI6NXCNtnp8fmGerIfzOrDgeATuaNkKGal0W4fRqqABhaQTFhaV6qjYIDRphDO_3oZmntJV4DCAN6n8QuQ9WA38WEgQybFLKxxWIxkQf3CRSgWQGhF-PDfMRyUdc26-bo6Dp-4pRF7yswjvPtkF9iCH9Af5yYnctE2VN1cvqXNC-zgyrDnIIQ6YgGp8fFrpCcArpI3mwsHEjYqsF6BzMSxX-2cjlF9n0ZT2G1Th6QJtcKn6kS4tq945yaaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
همان اتفاقی که در ونزوئلا رخ داد، در ایران هم در حال وقوع است.
مردم فقط آن را نمی‌بینند.
نمی‌توانی به آن‌ها رشوه بدهی؛ باید شکستشان بدهی. و ما داریم حسابی آن‌ها را درهم می‌کوبیم.
مذاکرات دوستانه‌ای در جریان است. ایران می‌گوید: «خواهش می‌کنم، خواهش می‌کنم، محاصره‌ای در کار نباشد.»
سوخت برای مدتی پایین آمد. بعد، آن‌ها درست رفتار نکردند و من مجبور شدم برگردم. حالا دوباره دارند درست رفتار می‌کنند.
هرگاه کسی جلو آمد و پرسید: «چرا داریم این کار را می‌کنیم؟» فقط بگویید: «چون نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست یابد.» خیلی ساده است. همین و بس؛ دیگر نیازی نیست چیزی بگویید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69078" target="_blank">📅 00:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69076">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWvvY0owfPbWxb7l8STSmAKde0mo96ElwXhdGs2av4symFPONA13GMwitdD6t3afXP4cilzOMqHUjQEhVgqE3jshEeNFSUe17q_SOV97HcWJaIJ3NyJKKszDOr7dAtr7plAGVkMnN-qhQHPF7k3Mi20NLNPcMdbgdAnPBZ57q1bca02EV7xb5azMDVXI3RkKJGsyjtUTq6mXs5BF5aV5MBw5Wk2lxwHfCHuzIJJKK2fR9pMjpgVfjAIbV7lnI9fxH6uYs0H7hKizFhRRQBnwcoUwUFzipDisTVZNIwwUGGyHxY22yNlP0Zazc-KsCdPdDcsq3GYeLV5WBqRSPQcYIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
کانال 12 اسرائیل: دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه در مصاحبه‌ای با شبکه ۱۲ اعلام کرد که تصمیم گرفته است حملات آمریکا علیه ایران را به تعویق بیندازد تا فرصتی دوباره برای مذاکره فراهم شود؛ با این حال تأکید کرد که در صورت شکست تلاش‌های دیپلماتیک، ممکن است دستور انجام اقدام نظامی شدیدتری را صادر کند.
- ترامپ در این مصاحبه گفت که ایالات متحده در حال انجام «مذاکراتی بسیار عمیق با ایران» است.
- ترامپ افزود: «اگر این مذاکرات به نتیجه نرسد، ما به اقدام نظامی قاطع بازخواهیم گشت.»
- رئیس‌جمهور توضیح داد که با درخواست میانجی‌هایی که از او خواسته بودند فرصتی برای مذاکره قائل شود، موافقت کرده است.
- وقتی از او پرسیده شد که تا چه مدت حاضر است به تلاش‌های دیپلماتیک فرصت دهد، پاسخ داد: «مدت زیادی نه. یا کارها سریع پیش می‌رود، یا اصلاً اتفاقی نخواهد افتاد.»
- ترامپ گفت که روز جمعه تصمیم به تعویق حملات گرفته است، زیرا کشورهایی که میان ایالات متحده و ایران قرار دارند و همچنین سایر کشورهای خاورمیانه، از او خواسته بودند فرصت دیگری برای مذاکره بدهد. (این کشورها و افراد شامل عمان، قطر، پاکستان، مصر و همچنین نمایندگان ترامپ، استیو ویتکاف و جرد کوشنر بودند.)
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69076" target="_blank">📅 23:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69075">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
قرارگاه مرکزی خاتم‌الانبیا:
آمریکا در تداوم شرارت و ناامنی در منطقه و به دنبال اجرای محاصره غیرقانونی دریایی ایران، طی سه روز گذشته اقدام به تهدید شناورها و کشتی های تجاری و نفتکش ایران در آب های ساحلی و سرزمینی کشور ما نموده است.
هشدار می‌دهیم این اقدام آمریکا به منزله توسعه جنگ در منطقه تلقی می گردد و همانطور که نیروهای مسلح جمهوری اسلامی ایران در میدان عمل ثابت نمودند هرگونه تهدید و شرارت ارتش تروریست آن کشور را بی پاسخ نمی گذارند و با آن برخورد خواهند نمود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69075" target="_blank">📅 22:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69074">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b46871a0cc.mp4?token=Myd03zLlAHndm4fO9c_r1Dh4GmbcKZ7KYIeRHkNxnRma0JGU67kwfT6rJVITacTj0OZlsKub5ooanTwdqqQF9BCFTNarTjVJgO-EwdKGhMgYwMVcKdBuHdaztA1mANn0uIeYlSBOOKRXHBCPc6UR8_HrMwbqeBd9PwkJSzLTK1lv9Ols9LMnDi0uf3sC0T7BMyKTo4h86WJgKAWNYgyQwjGQVadKtr19PV4sNsoNqOoa9VVPTB9JEXxS7NH_d38dccMcZbPd7vIzq1MsSmGcsHhLnWKxZ_7NXLCP8q3XK1mnnI3531EpVIIoo7uXWVVm8eeTStYXsb79qR4dMk1l8Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b46871a0cc.mp4?token=Myd03zLlAHndm4fO9c_r1Dh4GmbcKZ7KYIeRHkNxnRma0JGU67kwfT6rJVITacTj0OZlsKub5ooanTwdqqQF9BCFTNarTjVJgO-EwdKGhMgYwMVcKdBuHdaztA1mANn0uIeYlSBOOKRXHBCPc6UR8_HrMwbqeBd9PwkJSzLTK1lv9Ols9LMnDi0uf3sC0T7BMyKTo4h86WJgKAWNYgyQwjGQVadKtr19PV4sNsoNqOoa9VVPTB9JEXxS7NH_d38dccMcZbPd7vIzq1MsSmGcsHhLnWKxZ_7NXLCP8q3XK1mnnI3531EpVIIoo7uXWVVm8eeTStYXsb79qR4dMk1l8Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
زنده یاد مانوک خدابخشیان:
هر کس رفت سراغ s400 روسی, یعنی کارش تمومه!
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69074" target="_blank">📅 22:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69073">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-text">💎
فرم نتیجه دقیق رایگان با ضرایب بالا
💎
بهشت سنگین زنا و افراد کم موجودی
👍
https://t.me/+LVbtmWdHFTdmN2Rk</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69073" target="_blank">📅 22:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69072">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUzFelpAKkjFEsaglVX1vT4Gia7qms-npYENNv7adEsoXXSQ7_GSAGvVyFMypAGysoIwSbRM1GWkXGPtudkbqKPUy4xVGitmdy-9D-L9JITREPOwMU7n8KcMXlrces0RFrZqDKCURVQzIcgGpCEO1r7lMgzRg0kLon_fhtyckAtiCNkk5nwTIqtr5GlwUpZRn-T4ja7y_2PH4gHuw_pEEI3LBRv8PtriC7lPNg0MbA9_AS7RalzNbsc6B0bT4scTI2YRlomTbXntI_l3xasCgGtRpj1s6WeE0Pk-ofGbsbmG955KxXOe8lboWt4-HluA3TMlrqx_BzrIcS9j9wpyUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
فرم نتیجه دقیق رایگان با ضرایب بالا
💎
بهشت سنگین زنا و افراد کم موجودی
👍
https://t.me/+LVbtmWdHFTdmN2Rk</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69072" target="_blank">📅 22:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69069">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4dc96cd73.mp4?token=ayMyS7KXwzR2XD5GPLqyIZya3XYU6MS99fjuX-QH9YW2KmeaRCa8D9roosYOzsXpHHSVuHfLlzBfCovoQ_fziqIxaNrzVwGsjReNMAK-zjmFNSxZbzgqkjXe3s1sPQ6d4v_kHXcfQHHoI_BGwjVQwiz-oo3RJsGzu193rtdVKkz_2PF1pNsnAsprILEVtIga4Cw-dsQWQdmZoFVCLrW_ncSKFZBGVGR0OM5FcY4F0ScxbwSOTaU8YfDZZ3j6LoEOIUzE1m73fZgOB5S_BVyjCLzDUadOXEXAlXqrpm3TomURebDNwb7IwyroK1GeTYF6Ird1EmJez7zrg4tB4v5z-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4dc96cd73.mp4?token=ayMyS7KXwzR2XD5GPLqyIZya3XYU6MS99fjuX-QH9YW2KmeaRCa8D9roosYOzsXpHHSVuHfLlzBfCovoQ_fziqIxaNrzVwGsjReNMAK-zjmFNSxZbzgqkjXe3s1sPQ6d4v_kHXcfQHHoI_BGwjVQwiz-oo3RJsGzu193rtdVKkz_2PF1pNsnAsprILEVtIga4Cw-dsQWQdmZoFVCLrW_ncSKFZBGVGR0OM5FcY4F0ScxbwSOTaU8YfDZZ3j6LoEOIUzE1m73fZgOB5S_BVyjCLzDUadOXEXAlXqrpm3TomURebDNwb7IwyroK1GeTYF6Ird1EmJez7zrg4tB4v5z-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⏺
حسن روحانی درباره اعتراضات دانشجویی تیر ۱۳۸۲ (17خرداد 1392):
آقای قالیباف من دلم خیلی نمی‌خواست بگم، ولی شما من رو ناچار کردی. شما می‌گفتی دانشجوها بیان تا ما گازانبری برنامه داریم تا تمام کنیم.
ما می‌گفتیم راه این نیست که ما مجوز بدیم بعد بیاییم گازانبری این‌ها را دستگیر کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69069" target="_blank">📅 22:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69068">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ab4cc3c2d.mp4?token=qT0rkXMXMGzoDjKC9-88HuVAvq4eO6JmV2Zb3X2Cg5y6UfL2ZPoSa9L-1Ddx8PvsjOOq_1kWklHwvC8Y3I40Qz4bAC2b1zy5NWGrQj0RB-ffi1heemEyyLlomDjC2qYlTzvTQcWHbMU9LX14xwXnYA2mvfG4zzd6mk-vhd_ToG7VCaIkYhuHAbZcUSAcyWN_AqQPy0MofNmZLucQYvZ1yG5WFLtKzi4TtOae38WnLN64Cyac3d8IOfvABt6NLon8Jqd1YhE0TiiHdlNTZT-gUuxW7Mxp-JiVxeGPqr0PVZQgBPEPoRfYy2dgdWycNdo68JH7puGF3tgaQ-xersTK_TG2bAzuCO37ti2blp3hnjozEv-AEWy4huFp7CrUfzvs5QZ_QYtPrONmBNfs5ZM4EbIM4JjiOiwdfdCcu-ZPdx5Wcej9NAxH_RFXdsJ7SjExMtd6_4pv-fLLha-65MOPZnXk-5NutLL6D-ZVPQ9Cdp0EcHM81hVBdol3eZ0e7yjz2iKQsmSWfBfJpGOsnQRSg10_l-VHik9FWmM9viFlSTuW462qwae7iiEuTh2oZaD43_sHVzoYi9aAOO-_HqAYQsIQ2bDy7xWnt03frVOsifedyMAPgPy3X2cSdz4kQ9zi-8iRSBcgT-A5P46lSENFNUA6yKKwOEzLyV1AxvrFpos" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ab4cc3c2d.mp4?token=qT0rkXMXMGzoDjKC9-88HuVAvq4eO6JmV2Zb3X2Cg5y6UfL2ZPoSa9L-1Ddx8PvsjOOq_1kWklHwvC8Y3I40Qz4bAC2b1zy5NWGrQj0RB-ffi1heemEyyLlomDjC2qYlTzvTQcWHbMU9LX14xwXnYA2mvfG4zzd6mk-vhd_ToG7VCaIkYhuHAbZcUSAcyWN_AqQPy0MofNmZLucQYvZ1yG5WFLtKzi4TtOae38WnLN64Cyac3d8IOfvABt6NLon8Jqd1YhE0TiiHdlNTZT-gUuxW7Mxp-JiVxeGPqr0PVZQgBPEPoRfYy2dgdWycNdo68JH7puGF3tgaQ-xersTK_TG2bAzuCO37ti2blp3hnjozEv-AEWy4huFp7CrUfzvs5QZ_QYtPrONmBNfs5ZM4EbIM4JjiOiwdfdCcu-ZPdx5Wcej9NAxH_RFXdsJ7SjExMtd6_4pv-fLLha-65MOPZnXk-5NutLL6D-ZVPQ9Cdp0EcHM81hVBdol3eZ0e7yjz2iKQsmSWfBfJpGOsnQRSg10_l-VHik9FWmM9viFlSTuW462qwae7iiEuTh2oZaD43_sHVzoYi9aAOO-_HqAYQsIQ2bDy7xWnt03frVOsifedyMAPgPy3X2cSdz4kQ9zi-8iRSBcgT-A5P46lSENFNUA6yKKwOEzLyV1AxvrFpos" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❓
توضیحاتی درباره کوه کلنگ و چگونگی نفوذ به تاسیسات آن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69068" target="_blank">📅 21:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69067">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cf7ba0e57.mp4?token=sZOIGoyNh-WhiyOWKuj6MToOIpkyF4RtPn2ar8Mr-FfldyrwSd9Ke1gwPdl5fJiqeUa9EOqr-x7mH8SAc5i1sCzJ2E-fsYGxiB1vEeQIKXWo4YESTl_K4KLjLluL5oidi6mPH9MZKfWfOjs7R4aU8wEa5ds3sJ8WP5GxvoOGCFN0AbTaBGmAu9rC5cepVdH8brrKDHiz72zfGDEehqp766nSMwTPNRFO27TkW1Xs2TXEK5ldzI0o0ccV3O4oruR7xmY8i_WmHGX_FF44JPiiLPR1fIdY0Z_fSHR4g0tPZ7ro0Eg0njJTFmBrNnfXDBIvsz9bJiXCNyYcp9s5mkmAVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cf7ba0e57.mp4?token=sZOIGoyNh-WhiyOWKuj6MToOIpkyF4RtPn2ar8Mr-FfldyrwSd9Ke1gwPdl5fJiqeUa9EOqr-x7mH8SAc5i1sCzJ2E-fsYGxiB1vEeQIKXWo4YESTl_K4KLjLluL5oidi6mPH9MZKfWfOjs7R4aU8wEa5ds3sJ8WP5GxvoOGCFN0AbTaBGmAu9rC5cepVdH8brrKDHiz72zfGDEehqp766nSMwTPNRFO27TkW1Xs2TXEK5ldzI0o0ccV3O4oruR7xmY8i_WmHGX_FF44JPiiLPR1fIdY0Z_fSHR4g0tPZ7ro0Eg0njJTFmBrNnfXDBIvsz9bJiXCNyYcp9s5mkmAVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا نتانیاهو می‌خواهد که شما با ایران به توافق برسید، یا می‌خواهد به حملات خود ادامه دهید؟
🇺🇸
رئیس‌جمهور ترامپ:
«بی‌بی» عالی بوده است. [قدرت] ایران به ۸ درصدِ آنچه چهار ماه پیش بود، رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69067" target="_blank">📅 20:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69066">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73754cc159.mp4?token=Ukz55_dqPAUpK7JHY9do2uLV41K1HBVfWDIdEDlfga7zMPy4Tl4ykB0VJmY_uEGajD4LDfTzaTSNKND5kTQBFMgNW1lHqSSf_AGtQHo3IaOrQjJg7lrlBoJQVCTW6uYbByFokxU-LRKI49dsbnBanFLiPAjoYfRJbPcKo2IvOg-stvLL3oiClJod5jHHHgCNchibL-OuiWwtj7AMBXU2TfSHv4Zhw4c4vo77vPQfTDb_itq5rBWkze1FKxONvbg9h7GX_vOeii3cBhiSi_73920ZGyA8xEEgR18fPCWaoLCSegMfp5vvnUz5T7NMPZ1mgCyim_snY_VqOmYX8ysZpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73754cc159.mp4?token=Ukz55_dqPAUpK7JHY9do2uLV41K1HBVfWDIdEDlfga7zMPy4Tl4ykB0VJmY_uEGajD4LDfTzaTSNKND5kTQBFMgNW1lHqSSf_AGtQHo3IaOrQjJg7lrlBoJQVCTW6uYbByFokxU-LRKI49dsbnBanFLiPAjoYfRJbPcKo2IvOg-stvLL3oiClJod5jHHHgCNchibL-OuiWwtj7AMBXU2TfSHv4Zhw4c4vo77vPQfTDb_itq5rBWkze1FKxONvbg9h7GX_vOeii3cBhiSi_73920ZGyA8xEEgR18fPCWaoLCSegMfp5vvnUz5T7NMPZ1mgCyim_snY_VqOmYX8ysZpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
درباره جنگ با ایران، از توصیه‌هایی که هگست در ابتدای کار به شما داد و نتیجه‌ای که داشت، ناامید شدید؟
🇺🇸
ترامپ:
نه، اون کارش رو عالی انجام داده.
ما ارتش ایران رو نابود کردیم.
اونا می‌خوان مذاکره کنن و ما هم داریم مذاکره می‌کنیم.
این احتمال وجود داره که به توافق برسیم.
اگه اون کاری که ما انجام دادیم نبود،
الان اصلاً حاضر نمی‌شدن با ما حرف بزنن.
هم از طریق واسطه‌ها و هم مستقیم،
خودشون درخواست دیدار دادن.
الان هم داریم مذاکره می‌کنیم و امیدوارم اتفاقات خوبی بیفته.
امروز قیمت نفت هم حسابی افت کرد.
مذاکرات خوب پیش میره و
احتمال زیادی هست که نتیجه مثبتی داشته باشه.
اما اگه توافقی حاصل نشه،
برمی‌گردیم به همون کاری که دو روز پیش انجام می‌دادیم.
🎙
خبرنگار:
شما و نتانیاهو درباره ایران هم‌نظر هستید؟
🇺🇸
ترامپ:
یه اختلاف‌نظر کوچیک بینمون هست،
ولی در کل تقریباً هم‌نظر هستیم.
ایران توی 14 روز گذشته ضربه سنگینی خورده.
اونا خیلی محترمانه از ما خواستن که
«لطفاً حملات رو متوقف کنید، بیاید مذاکره کنیم.»
الان دقیقاً توی همین مرحله هستیم؛ باید ببینیم آخرش چی میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69066" target="_blank">📅 20:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69065">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klTK5t0OXCI6uNkPbjlVPhblzhIy3m1BmUD-Fxmp1i0z7uJdt7iEJGg-RBRxCWlSTkbmQdN1u21mSLiqCZ-o24Nw6-7ImLPh7OgXnI9stdon3uQCaIe9ZTgkdj44vPPnED5P1Dt_jVzOASJ1mCcwLLyATXy9tPKGekxGU3PBes_gl_COVQtrRcLM6mmuXSvLWPpgXXnZsh2Ds9nNON--CoKnCyqLyjnRGbNcABqUTAaos1hNVdbB6VO01bAFMbLw3BMF5WVkLz6g_SSwj8Q3map9S8uyjFsWzM2wOl4JOMFSa5-EUfjexnchBjFdlNqIsGX4d4NQsh9KhqkFqoA0nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇦
وزیر امور خارجه اوکراین:
تهدیدهای ایران غیرموجه و بی‌اساس است. رژیم تهران شریک مستقیم تجاوز روسیه به اوکراین است و با تأمین تسلیحاتی که از سال ۲۰۲۲ تاکنون موجب مرگ اوکراینی‌ها شده، به جنگ جنایتکارانه مسکو دامن می‌زند.
ایران هیچ جایگاهی برای وانمود کردن به اینکه قربانی است ندارد، چه رسد به اینکه بخواهد تهدیدهای خود را با استنادهای مضحک به منشور سازمان ملل توجیه کند.
ایران همچنین با این اظهارات تلاش می‌کند تا توجه‌ها را از اقدامات تروریستی روسیه علیه کشتی‌های غیرنظامی در دریای سیاه — که امنیت غذایی جهانی را تهدید می‌کند — منحرف سازد؛ اما در این کار موفق نخواهد شد.
حملات روسیه به آزادی کشتیرانی در کانون توجه نشست اضطراری امروز شورای امنیت سازمان ملل قرار خواهد داشت و ما انتظار واکنش‌های قاطع جامعه جهانی را داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69065" target="_blank">📅 20:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69064">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ec0fc6074.mp4?token=tyMFVzgu3OcOprLW4shxBFsSfgtlNqGfT2iTzCFBXFgAl1vIFVvoTIR1HW8u9Sq7BhD_is2gszB2F248-XJRFh2sp9NraWsDXbMSrR3q98yaMIJD_ggXADl1SlcMUAtN1cp48B6xFZum399MFQkgiWwBGt261PQfUxjEld0Cs1x2v83Yy-ENBrn_hie4DSWbxwqg1GeS-246Lm8BTuNH_8L_3uGcVW8XUEz4N1hr49LoG4Df9t-RdNRVV8jjKQs1uCcn9C01mSfmFL6bHWsuKvfDla69Zy2J9BZhUp0gUwv0lRdqKBsQ7qxdMn9A3vBweI8YAp2jPkBavKIFNC1T4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ec0fc6074.mp4?token=tyMFVzgu3OcOprLW4shxBFsSfgtlNqGfT2iTzCFBXFgAl1vIFVvoTIR1HW8u9Sq7BhD_is2gszB2F248-XJRFh2sp9NraWsDXbMSrR3q98yaMIJD_ggXADl1SlcMUAtN1cp48B6xFZum399MFQkgiWwBGt261PQfUxjEld0Cs1x2v83Yy-ENBrn_hie4DSWbxwqg1GeS-246Lm8BTuNH_8L_3uGcVW8XUEz4N1hr49LoG4Df9t-RdNRVV8jjKQs1uCcn9C01mSfmFL6bHWsuKvfDla69Zy2J9BZhUp0gUwv0lRdqKBsQ7qxdMn9A3vBweI8YAp2jPkBavKIFNC1T4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدباقر قالیباف، (اردیبشهت 1392):
در اعتراضات کوی دانشگاه عکس‌ام روی موتور با چوب هست. جایی که لازم بوده چوب بزنیم کف خیابون چوب می‌زدیم. افتخارمون هم هست.
در شورای امنیت گفتم هرکسی بخواد بیاد کوی، منِ قالیباف لوله‌شون می‌کنم جمع‌شون می‌کنم.
محکم وایسادم مجوز تیراندازی در کوی رو گرفتم.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69064" target="_blank">📅 19:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69063">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ به کانال12 اسرائیل: اگه مذاکرات با ایران جواب نده، دوباره حمله می‌کنیم
«الان داریم مذاکرات خیلی جدی و عمیقی با ایران انجام می‌دیم، ولی اگه به نتیجه نرسه، دوباره دست به یه اقدام نظامی خیلی سنگین می‌زنیم.
زیاد هم به دیپلماسی فرصت نمیدم؛ یا خیلی زود به نتیجه می‌رسه، یا کلاً بی‌خیالش می‌شیم.
همه کسایی که توی مذاکرات با ایران درگیرن ازم خواستن حمله نکنم. مدام می‌گفتن: "شلیک نکن."
برای همین تصمیم گرفتم فعلاً حملات آمریکا رو متوقف کنم و یه فرصت دیگه به دیپلماسی بدم.
به نظرم ایرانی‌ها می‌خوان به توافق برسن و منم قبول کردم حملات رو فعلاً متوقف کنم، چون نه چیزی برای از دست دادن هست، نه چیزی برای به دست آوردن.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69063" target="_blank">📅 18:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69060">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8aee1d66.mp4?token=pM19W93uwqGrF7Vs1XBlyXuyw8og9LHnMO6lbUCYxnqc0NM6H-BSAd-0jo5es5_nLSZ_PcK6-RDzTWPHJYjrDk8JNnCuN0l2dg3V-OT868ydK6ggeqDPMvsqk-LPwMZL-DBAOL9mONQBJWv-b1lAEJXTvCABeiZZh8oi8d3QpZSyV_FHLDlkLOKyZGKuuBczcMlAJSyJmQFg4yHF6Grw7d-UVM6XLbbQiO45lTyETxfcHy_2-TyQjP5cvZSI1-MmkukqBfOqc6vabEdZaG0kFAEv-0-8asAxqB6E4pJpBewpFaGq22WVD2Z325hGduTxxRic_4GbSjOvDbow04GV7J8XJaTqoLHcR3pLuO_C4oj3-qpPMb_kiH9VC7PILo0dk2COvoUhUyc8flPVU0xvDXqjk9plpCU6eetMg_hdVbcJAlaLN-b1mmnMRWeTeIUHLAdjg1XIhyg_irfBMG4hL7SqrpcuwINroTxoy-TAtd2k8kjVUy5mcj5q0MIYMAxq9GLA9QZiAtb-PfFUXKsmegEP1wdsV_Mlc6l6ovSvaMsS98ATf8R2J2owuQrHxObR-XuaknlNmziGgDsZN4S1pb1C4RE_KLf0yBxbLSTZrxkeuAy4kFQtk1j2pNZcum0aO4J0HzcrRTTSvIrxvc69sdU8hJjBNWTd2F3SminZLYU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8aee1d66.mp4?token=pM19W93uwqGrF7Vs1XBlyXuyw8og9LHnMO6lbUCYxnqc0NM6H-BSAd-0jo5es5_nLSZ_PcK6-RDzTWPHJYjrDk8JNnCuN0l2dg3V-OT868ydK6ggeqDPMvsqk-LPwMZL-DBAOL9mONQBJWv-b1lAEJXTvCABeiZZh8oi8d3QpZSyV_FHLDlkLOKyZGKuuBczcMlAJSyJmQFg4yHF6Grw7d-UVM6XLbbQiO45lTyETxfcHy_2-TyQjP5cvZSI1-MmkukqBfOqc6vabEdZaG0kFAEv-0-8asAxqB6E4pJpBewpFaGq22WVD2Z325hGduTxxRic_4GbSjOvDbow04GV7J8XJaTqoLHcR3pLuO_C4oj3-qpPMb_kiH9VC7PILo0dk2COvoUhUyc8flPVU0xvDXqjk9plpCU6eetMg_hdVbcJAlaLN-b1mmnMRWeTeIUHLAdjg1XIhyg_irfBMG4hL7SqrpcuwINroTxoy-TAtd2k8kjVUy5mcj5q0MIYMAxq9GLA9QZiAtb-PfFUXKsmegEP1wdsV_Mlc6l6ovSvaMsS98ATf8R2J2owuQrHxObR-XuaknlNmziGgDsZN4S1pb1C4RE_KLf0yBxbLSTZrxkeuAy4kFQtk1j2pNZcum0aO4J0HzcrRTTSvIrxvc69sdU8hJjBNWTd2F3SminZLYU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دیروز بعد از 25 سال، قلعه‌ی الموتِ قزوین با رای مثبت داوران یونسکو، ثبت جهانی شد؛
قدمت این بنا برمیگرده به 1100 سال پیش، دوره‌ی دیلمیان، که ازش به عنوان یه مرکز استراتژیک استفاده میکردن.
سال 654 هجری‌قمری، حین حمله‌ی مغول، هلاکوخان دستور میده که این بنا رو به همراه کتابخونه‌ی ارزشمندش به آتیش بکشن.
امروز فقط خرابه‌هایی از دیوارها و پایه‌های قلعه مونده، ولی هنوز هم به عنوان یه جاذبه تاریخی-طبیعی خیلی معروفه.
قلعه الموت 30 اُمین اثر ایران تو میراث جهانی یونسکوئه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69060" target="_blank">📅 18:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69059">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1028348d85.mp4?token=JhWm_H2tnjoPdm9rhsAsElV0kH-eO9rQEE9RBvvZtQ2GuMCPh51zBHJPowt6vgQi97aQm-MD5TtVrt2hrSCzZP8Iqzp-eFX2SpFju_u3xw0XKOVwT43haWetBGFvGv1S9aXFovMZFnSP4NSMMhamZdY1OKExc06MS930WU5xPxKFKmLZDCyWqYLMHHCi9xPBad7zarq6L4P5x-F4JnmxlsKydwpD28hivjpyUsyztOHA5ZfxQfIHPJSwmxoKe2IfoP-qHnSho4_kTXVyplxGqfAwHzbWkMnD4m4vINaZFRbd33y8GGwfkVY2Ye665iUX5_PDNq3eaJnjSPUgytLiGLHirssbeFAIWTaB2YLfCN6J_VqfXtI2__l_2YKwHEDMUweGd8HMx8utEE4b_aUfbG2PePol96ZQhjXyL-cXjNgIy4J1ZBWEBnFOl0h_rHXiAdJnehFla_BZkEFWz394b2lb8eymNA0snB2gKwNFMYbHmEQY_LIDmJzsPjvOwOYRVXSuuAyfEtLlwgY-ztqwPdxiC8JlWjnbJOXdSrZgcNcJIspUVZSqSUwJyTHbsJf81OiQ0OKIdPHAlsL5iAQ8aoc4RV1XQFH1Ic74-C27jFKO5y4tf_DqogMlnjEO4NW_UadobimmWfyyHTQABlwakZY8NaSyfzMs7ukqd3QH7mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1028348d85.mp4?token=JhWm_H2tnjoPdm9rhsAsElV0kH-eO9rQEE9RBvvZtQ2GuMCPh51zBHJPowt6vgQi97aQm-MD5TtVrt2hrSCzZP8Iqzp-eFX2SpFju_u3xw0XKOVwT43haWetBGFvGv1S9aXFovMZFnSP4NSMMhamZdY1OKExc06MS930WU5xPxKFKmLZDCyWqYLMHHCi9xPBad7zarq6L4P5x-F4JnmxlsKydwpD28hivjpyUsyztOHA5ZfxQfIHPJSwmxoKe2IfoP-qHnSho4_kTXVyplxGqfAwHzbWkMnD4m4vINaZFRbd33y8GGwfkVY2Ye665iUX5_PDNq3eaJnjSPUgytLiGLHirssbeFAIWTaB2YLfCN6J_VqfXtI2__l_2YKwHEDMUweGd8HMx8utEE4b_aUfbG2PePol96ZQhjXyL-cXjNgIy4J1ZBWEBnFOl0h_rHXiAdJnehFla_BZkEFWz394b2lb8eymNA0snB2gKwNFMYbHmEQY_LIDmJzsPjvOwOYRVXSuuAyfEtLlwgY-ztqwPdxiC8JlWjnbJOXdSrZgcNcJIspUVZSqSUwJyTHbsJf81OiQ0OKIdPHAlsL5iAQ8aoc4RV1XQFH1Ic74-C27jFKO5y4tf_DqogMlnjEO4NW_UadobimmWfyyHTQABlwakZY8NaSyfzMs7ukqd3QH7mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از یه هموطنمون که برق خونش رفته و کولر ماشین وصل کرده تو خونش
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69059" target="_blank">📅 17:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69058">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BupSD1V0Sg2x4ZGsllBrHLS88oGyGMitiK5GQ0d4ESQPgXMOGZS9pNS7juVvvxhTWp5nDkfC-LWvY-puVmyQk1lcMUnZjpAAVehnRrZJKmIkfo4NZU8yvI4WE2-VUXmJ2TITK8Qi3_RwT14sW9bp13syHXZe9cPDrxi02lmkRSQJ1-HCU9hVji_8w-OCrhEdtReeAt3mx5yPDj7CE_8ht4AyEfQ7Els8aOxOhVG7iGWREGvZZX4Il4KSePvLU7U62Ab9TBmPVJuDawei84JTxTTVYTUt8NNRTm817n1ePHsJw4wPzMwFoRYuM7RWBhnw1rM5XwjIoqYqL3vUVecqow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
قالیباف خطاب به مردم آمریکا:
دلتان برای قیمت فعلی بنزین تنگ می شود.
بنزین در آستانه لیتری ۱۰ تومان
!
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69058" target="_blank">📅 17:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69057">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4svIsG0l_KaI6or_AEgGqGLx2t8H4LgBntmzDtqupgWeUFSzQH4HuP_RYuQVD_qETEi8QQ-2HcvdmG58iLeoVQJ65WnizFDQT5P8rgwcDcf4nFXyi8AtXouD23m_TUQYD8zmWFAH85cEsuq7tXLuQE0scjhNM_tL5mKCx7MWC5BcSiDuow5N2NWUDihgxnhgx7SHX8zfVoi--SPEHVea2rdoRcSJcJ3G9_RAvFSmWEl9TQUgRs-u_04boUKnbwEghFctVgxAmbhqwblJ1holDtUfccnYCgVY41UfZ5ykkHfdantEnC_eJ_VKdSZeWSUVOYjTF9n7yHCxl6cH9kacQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
همشهری:
سران قوا با بنزین ۱۰ هزار تومانی برای «سهمیه سوم» موافقت کردند.
درحال حاضر، سهمیه سوم بنزین با قیمت ۵۰۰۰ تومان عرضه می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69057" target="_blank">📅 16:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69056">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OG_3E5E6kkFsTF9Fgx77inZMi3CQawzXc_8K7KRPbdfm3tLzd7XpIdo5iQPasGnquVsPRzPjUcJYJL8KNAsoriHINFLU9xD4oISqX7FjotiFXdheuKIeXcGOkMICbbpz6BXeEaCP-egrExJZ4-Ds0PkLhojSMF0CIQj2fx920-abWaDC_XwaFZhW-UBlXaQLdvYkvrMKHa4T6doBCR29m0wGIdtWX37ExjGk6RihxeIwNxnf9mniSj0rftFewXcGKVGuKHNLTNkDFEyfSbAgj6m38HVMefQzqhB95Db597-3stbtjpso79j_VklR5QCrvucmywbodciRJdohPz9Xbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇦
وزارت دفاع عربستان سعودی:
رهگیری و انهدام تعدادی پهپاد که از خاک عراق آمده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69056" target="_blank">📅 16:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69055">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69d958cc0a.mp4?token=PQIqh3KYnld4F0Ygkvf54WUUxg1PyxsR1HXl7VhggtTokpa7uMc9HbRkmXqlA3JYHjQovY8qVgsMM-zRhOLNET72aWheYOXSB_5vFfvdSjKAHD52Zb3C3b0BmAZQyhLLbgbS59fL_cGiXuaSPmkZpBlvRBWmxs69eBziWt9IgAavJrjKSw7fr_tgi-hJv829u5RO2MFboSWdr7B3A5fi1uVMxf8VXWSmIdFtLK0ybR5Yi0QW92uIzFWV4Tpoj0HIuqQsAvwzZ4J08l195Z_GoOUIggxLmMyiNqxx4gjS7RY2oDZmUFGxwKIk5v-59QzDjFGkFdDq-yTmic-nd0Jl4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69d958cc0a.mp4?token=PQIqh3KYnld4F0Ygkvf54WUUxg1PyxsR1HXl7VhggtTokpa7uMc9HbRkmXqlA3JYHjQovY8qVgsMM-zRhOLNET72aWheYOXSB_5vFfvdSjKAHD52Zb3C3b0BmAZQyhLLbgbS59fL_cGiXuaSPmkZpBlvRBWmxs69eBziWt9IgAavJrjKSw7fr_tgi-hJv829u5RO2MFboSWdr7B3A5fi1uVMxf8VXWSmIdFtLK0ybR5Yi0QW92uIzFWV4Tpoj0HIuqQsAvwzZ4J08l195Z_GoOUIggxLmMyiNqxx4gjS7RY2oDZmUFGxwKIk5v-59QzDjFGkFdDq-yTmic-nd0Jl4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخورد صاعقه به موشک چينى در لحظه پرتاب‌
👀
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69055" target="_blank">📅 16:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69054">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e50eb610c7.mp4?token=pItSRNsJN9zE2gKs_iS7xp4glhcTg2KlQRKgJHQ8C3FH2SEzPAqXUXFD9Ba4t_BnD9d5YJ6gIXdu57eQVZmd6HHDWaoJyr9J88jrO-q9NaQklvl_UVeyEwzKcMurwWRvM6PJyRpLBfc41cAydXcQgllNUNRBQJsxTSDiAyfYk86L4XoxLbr8-POmJPSAsedv-dnR9UE_CITlDpDueZuglo7n8FH7Z-NqDovAaswIMaxlNDruBSsUk2SlLzmy9sRPdvViPmpKR5Kq7k0SV7hiSZ66g9ZKTh8zxFtvIF9_mhLKjCAaKllS8kNPoqIdjD2OH9n0pK5BmeNBF5S0OTzcFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e50eb610c7.mp4?token=pItSRNsJN9zE2gKs_iS7xp4glhcTg2KlQRKgJHQ8C3FH2SEzPAqXUXFD9Ba4t_BnD9d5YJ6gIXdu57eQVZmd6HHDWaoJyr9J88jrO-q9NaQklvl_UVeyEwzKcMurwWRvM6PJyRpLBfc41cAydXcQgllNUNRBQJsxTSDiAyfYk86L4XoxLbr8-POmJPSAsedv-dnR9UE_CITlDpDueZuglo7n8FH7Z-NqDovAaswIMaxlNDruBSsUk2SlLzmy9sRPdvViPmpKR5Kq7k0SV7hiSZ66g9ZKTh8zxFtvIF9_mhLKjCAaKllS8kNPoqIdjD2OH9n0pK5BmeNBF5S0OTzcFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو:
من در راه واشنگتن برای دیدار با دوستمان، دونالد ترامپ، رئیس جمهور ایالات متحده هستم.
این هشتمین دیدار من با او از زمان انتخابش به عنوان رئیس جمهور است، بیش از هر رهبر بین‌المللی دیگر. این یک امتیاز بزرگ است، اما همچنین یک مسئولیت بزرگ است.
بر اساس تجربه من به عنوان نخست وزیر، باید در این دوران پیچیده با عزم و اراده قوی و خرد فراوان عمل کرد.
ما تمام موضوعات دستور کار را که در صدر آنها ایران قرار دارد، مورد بحث قرار خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69054" target="_blank">📅 15:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69053">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
«در حال حاضر هیچ مذاکره‌ای با ایالات متحده نداریم و به هیچ آتش‌بسی تعهد نداریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69053" target="_blank">📅 14:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69052">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFmqH8elXS56si3Ze7X0x4JLq7UEs6pOSw6pQaa8aFfkrl81gAM5BEkYe2VQ2BBKyon4VOZ_t5eKmuRH1lp-QKb6930n5cU3t4FXEkZUprkYHEqjwL5MfLQW5th938Z_uUhFaEnn3lT_VXgdY8lQcfceIOUOLQ3OzyyETMbzuh2CHamdbvt8EuH9uTIUbx1ev2Ggb-Ip_ZQcoDd6ADG2tzVp7Eh_9qGQL8tvop6ZeXZ57ChjS3OA4tx-Tqgv4BAnYBJkt7HlFIn5o9KmGKufuiD3OYVXM8eokv7PpFDTEEAQha5y8XlMzYgBlBcN5MasF7LmwYDkSl5jyWNz-s0pAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇮🇱
🇺🇸
هواپیمای نتانیاهو عازم واشنگتن شد!
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69052" target="_blank">📅 14:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69051">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ri3zgKDD4PzB-hSUZl5DEEQ1ok9ZOK8LqfTPUFfZIVwjxqNhGMIRzDXlRDMcBhZ-60tQ7om9gktzy240sSHuJDzcHv__TjNbNmuNh8VFDAqojH1rRHsy6eISsyvWOWDO_6GIJsBPGRwtQVegwh3m8wWNog_--b9RRv174DjLh-eOMIdzYZrf43VatafxR7xaMnx6DRL7WOS8u5m_VnpBecjk8Qfdkn_SyaAhXMSAcBTKBjv62KEZz_dI6MJoFw4vXt11-1H2UiCug5R5DhZbwhSoAPJ0hCpCDGtq0_nXuIhMJp-2OP-Y9fjP9aHtTB2B8LCpiNBEr2LjVqbV1r6V0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
کروز AGM-129؛ موشک کروز پنهانکاری که از «بالا» نامرئی بود
موشک کروز هسته‌ای AGM-129 Advanced Cruise Missile (ACM) یکی از پیشرفته‌ترین تسلیحات دوران جنگ سرد بود؛ سلاحی که بسیاری آن را «یک هواپیمای رادارگریز بدون خلبان» می‌دانند. طراحی این موشک به‌گونه‌ای انجام شده بود که از زوایای بالا کمترین بازتاب راداری را داشته باشد؛ به همین دلیل ظاهر آن برای بسیاری شبیه یک هواپیمای وارونه به نظر می‌رسید.
برخلاف موشک‌های کروز متداول، سکان عمودی AGM-129 به سمت پایین قرار داشت، ورودی هوای موتور در زیر بدنه تعبیه شده بود و خروجی موتور نیز به‌گونه‌ای طراحی شده بود که امضای حرارتی و راداری آن از دید هواپیماهای آواکس و جنگنده‌های رهگیر شوروی تا حد امکان کاهش یابد. این طراحی نتیجه تغییر تهدیدات دهه ۱۹۸۰ و ظهور رادارهای «نگاه به پایین، شلیک به پایین» بود.
این موشک با بردی بیش از ۳۲۰۰ کیلومتر، سرعت نزدیک به صوت و سرجنگی هسته‌ای W80، از سامانه‌های ناوبری پیشرفته شامل ناوبری اینرسی، تطبیق عوارض زمین (TERCOM)، لیزر داپلر و حسگر LADAR بهره می‌برد که امکان پرواز دقیق و پنهان در ارتفاع پایین را فراهم می‌کرد. AGM-129 تنها توسط بمب‌افکن B-52 Stratofortress حمل می‌شد و هر فروند B-52 توان حمل ۲۰ فروند از این موشک را داشت.
با وجود فناوری بسیار پیشرفته، هزینه بالای نگهداری، کاهش تهدیدات پس از پایان جنگ سرد و تمرکز آمریکا بر جنگ‌های ضدتروریسم باعث شد این موشک بین سال‌های ۲۰۰۷ تا ۲۰۱۲ از خدمت خارج و تمامی نمونه‌های عملیاتی آن منهدم شوند. امروزه آمریکا برای جایگزینی آن در حال توسعه موشک هسته‌ای پنهانکار LRSO است؛ برنامه‌ای که میلیاردها دلار هزینه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69051" target="_blank">📅 13:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69050">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Avd69e2wBFFcmBb1oEjAIWkk9VvvWfyncVAIZQWjSs2PckiofFvH3_nicQdnWT47lNrpxnA3OVrxbOFnA0Wk9Lk2Iyk77xlJiOyByPm3hWgZ0t69br99_WEI8sav1i6I9FVJDr9xtZFEn9LnEdZu1XLetIHnVSSCjvaxof6MYP_rHk1vYkmJlau2Zdbs1Drs2ziLlRuvQraepRlgDiG4CPh_YYtdM16SpMxXqvohevC_oq9k4uUL_EyFYvLnESm9OZxWiZu31uyYBrd0OuYztfTdQzYCyGg406rclC8qoG5JUqZMZ6wvz0msPphPqITd-JbrR01-LYm7SSExKf2AXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
👑
شاهزاده رضا پهلوی:
چهل و شش سال از درگذشت پدرم می‌گذرد، اما او امروز زنده‌ترین چهره سیاسی در پیشگاه تاریخ و دل ایرانیان است.
شعله عشق ملت ایران به او روز به روز بلندتر و فروزان‌تر می‌شود. همان‌طور که جاویدنام مجیدرضا رهنورد به نیابت از میلیون‌ها جوان ایرانی نوشت: «نسلی عاشقت شد، که تو را هرگز ندید».
پدرم با تمام وجود، عاشقِ ایران بود. قلب او با طبیعت این خاک می‌تپید و باریدن باران بر دشت‌های ایران، برایش بهترین و زیباترین خبر بود.
او در ۲۲ سالگی، کشور را در شرایط دشوار اشغال متفقین تحویل گرفت و با تکیه بر میهن‌پرستی، ایران را به سوی دروازه‌های تمدن بزرگ هدایت کرد. اگر فاجعه ۵۷، مسیر تاریخ ما را منحرف نمی‌کرد، ایران امروز یکی از درخشان‌ترین قطب‌های رفاه و توسعه در جهان بود.
هم‌میهنانم، اگر به راه او باور داریم، مسئولیت بزرگی بر دوش ماست. برای وفاداری به نگاه او، ما باید ایران را از این فرقه تبهکار پس بگیریم و آن را دوباره بسازیم.
پاینده ایران
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69050" target="_blank">📅 12:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69049">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/743c9eadbb.mp4?token=EaRjg_64jXnlzs-ZMYNhFqXB3QYZNuEAb_hMOii8heF-lGfeGW_yopJHp4mEcPB7sNfgxbvevZcHPbo9pz_lgwFKVTitAkn3fCeUqXjtFpudjoRvF4e1wQvk8-A_wkfudtDLOqi2JFTnRBU0BfM1pYtDqbbKc8f9PtkoqN9Gh1_vVSXXA1hlXRMbUWcQHPDtjObEJaZ0qTwRn-0GnQ_KkiF3C8Hpj9xq-n-FVLJjtciaQjwSKvWvjXKh415RM8OlOyJA3lUyXl58iYHK2RGyPkk09thLNbDxjZrwV9zQbgPNaB_o_NBS9bDbU5POWMDOD156gvKqL4FZsVcrtzzzKhNHtZF1wRQ5_m-VFv11H2tCZ1sQwGLvtMyweMesVrmqYasmZKfqqLqiObYBUBdU7WpF4ahg8aySkT7O4LRa7weYziThI-ql09OKa-XbAI-HQgtKR6B62ZRCUXF8Pb9COtiXC3yQGSCZ8UXem5t7rGTmlt1eS4z-7Egi_X3RZFzJgs6DXnYjj0xAkVCWbqlT-149Dpp2lBUO9G-XSbOL8mviQH1dpRBg_Qk2D4-sdYgROMT11qn8nJ-w-6fucdjs3LR0Mwsn_Bg9S-NgIqCfdA7WSEdd9ZNKbQkcfMo451GB8P_hj3CaF0oeGZ87AMRlU_7GCHoUXdkI2ni8gYlLw0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/743c9eadbb.mp4?token=EaRjg_64jXnlzs-ZMYNhFqXB3QYZNuEAb_hMOii8heF-lGfeGW_yopJHp4mEcPB7sNfgxbvevZcHPbo9pz_lgwFKVTitAkn3fCeUqXjtFpudjoRvF4e1wQvk8-A_wkfudtDLOqi2JFTnRBU0BfM1pYtDqbbKc8f9PtkoqN9Gh1_vVSXXA1hlXRMbUWcQHPDtjObEJaZ0qTwRn-0GnQ_KkiF3C8Hpj9xq-n-FVLJjtciaQjwSKvWvjXKh415RM8OlOyJA3lUyXl58iYHK2RGyPkk09thLNbDxjZrwV9zQbgPNaB_o_NBS9bDbU5POWMDOD156gvKqL4FZsVcrtzzzKhNHtZF1wRQ5_m-VFv11H2tCZ1sQwGLvtMyweMesVrmqYasmZKfqqLqiObYBUBdU7WpF4ahg8aySkT7O4LRa7weYziThI-ql09OKa-XbAI-HQgtKR6B62ZRCUXF8Pb9COtiXC3yQGSCZ8UXem5t7rGTmlt1eS4z-7Egi_X3RZFzJgs6DXnYjj0xAkVCWbqlT-149Dpp2lBUO9G-XSbOL8mviQH1dpRBg_Qk2D4-sdYgROMT11qn8nJ-w-6fucdjs3LR0Mwsn_Bg9S-NgIqCfdA7WSEdd9ZNKbQkcfMo451GB8P_hj3CaF0oeGZ87AMRlU_7GCHoUXdkI2ni8gYlLw0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ایلان ماسک : در سال ۲۰۳۶ پول دیگه اهمیتی نخواهد داشت.
پول رو برای چی می‌خوای؟ برای کالا و خدمات: غذا، مسکن، حمل‌ونقل، سرگرمی.
اگر ربات‌ها و هوش مصنوعی بیشتر از اون چیزی که هر انسانی بتونه مصرف کنه، کالا و خدمات تولید کنن، دیگه به پول نیازی نداری.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69049" target="_blank">📅 12:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69048">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">و همچنین یادمون نره طبق اطلاعات موجود، آمریکا همچنان به تاسیسات زیرزمینی هسته‌ای ایران حمله نکرده، یعنی اورانیوم ها همچنان در دست ایران هستند، اون فتوای پدر بود که گفت بمب اتم نخواهیم ساخت، ولی الان مملکت افتاده دست پسر و تندرو های سپاه، پس آمریکا حتماً این رو در نظر داره اگه نیروی پیاده نظام برای نابودی تاسیسات هسته‌ای وارد نشه، ممکنه از طرف مجتبی خامنه‌ای با یک سورپرایز مواجه بشن!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69048" target="_blank">📅 11:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69047">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uW2Q3N56kec2IOBIner8y4HmSmILluGaNwHntKycY871xHOSeKYBAj1a4UB9le8XQ8_yyGghMSGI5msmM-mo1zYYOjg4IGac7jfc3UMqQDTrd2tqXtsT9YLmfWhUQDPuf5DH_6hUKJKgjQx_hRIsVAW-uZ1B15mlPyXGBBeRcSBCqMX9XXd0KZM6h5FzYxKaxXGcYwgCEJalraEkq0LZrnxMpVEk5LK5lGSwJTwJITdWXzP-odFvY1zri6gd7EyuI2TjxBptNNoQGADP07yWOR7LtwhpRipmdNqLfWUxGXVff0be67C3Qv1JKV0YhgzEksMLClPV2ywEuF87K_UX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
وال استریت ژورنال:ترامپ حملات به ایران را متوقف کرد؛ در حالی که مقامات در حال بررسی کاهش ذخایر سامانه‌های پدافند هوایی هستند.
ترامپ برنامه‌های مربوط به یک عملیات هوایی گسترده ایالات متحده علیه ایران را متوقف کرده است؛ این در حالی است که مقامات، مسیر دیپلماسی را دنبال می‌کنند و نگرانی‌ها پیرامون کاهش ذخایر موشک‌های پدافند هوایی آمریکا را مورد ارزیابی قرار می‌دهند.
با وجود اینکه ارتش برای انجام حملاتی که می‌توانست تا دو هفته به طول انجامد آماده شده بود، اجرای این عملیات به تعویق افتاد.
در حالی که ترامپ تأکید دارد ذخایر تسلیحاتی آمریکا همچنان بیش از حدِ نیاز است، میان فرماندهان نظامی در خصوص اینکه آیا کاهش موجودی موشک‌های رهگیر «پاتریوت» خطری جدی محسوب می‌شود یا خیر، اختلاف نظر وجود دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69047" target="_blank">📅 11:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69046">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=rSy7xXDJnVGwz5Pw-7H9zSkT0A6fiBL6jJYhalKV0nSh2dgwfA9mVOoGMvZB3dPCcCoeZCWo4xpmkeIuNGo5CL15ELSND1DYTs_quX837bgKtyv6aJWxRrv21wUnJo3zpatYnR3KIneO0eNoFoNm7d2LTPqbI1h2lwteU2QdIZao8rgPUmguV1BxrssoInfYbBvM6pzY6jLsHxgCXB14K_cSwegMQxMc3SF2sQOS0k057epZrNDj31fmwVJcA4cKl9RroMjkc_UVwcbqPYkt90c0XyGJesR4v-l0sjLT9hdhIRH26QuBboILJ3WocrB6PZWzrbLDo-3x9JzPaWJxXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=rSy7xXDJnVGwz5Pw-7H9zSkT0A6fiBL6jJYhalKV0nSh2dgwfA9mVOoGMvZB3dPCcCoeZCWo4xpmkeIuNGo5CL15ELSND1DYTs_quX837bgKtyv6aJWxRrv21wUnJo3zpatYnR3KIneO0eNoFoNm7d2LTPqbI1h2lwteU2QdIZao8rgPUmguV1BxrssoInfYbBvM6pzY6jLsHxgCXB14K_cSwegMQxMc3SF2sQOS0k057epZrNDj31fmwVJcA4cKl9RroMjkc_UVwcbqPYkt90c0XyGJesR4v-l0sjLT9hdhIRH26QuBboILJ3WocrB6PZWzrbLDo-3x9JzPaWJxXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در ۲۹ دسامبر ۲۰۲۵، خودروی آنتونی جاشوا در نیجریه با یک کامیون تصادف کرد. در این سانحه، سینا غمی، مربی آمادگی جسمانی و دوست نزدیک او، جان باخت. جاشوا پس از ۲۰۸ روز دوری از رینگ، با آهنگ «نقاب» از سیاوش قمیشی به یاد دوست از دست‌رفته‌اش بازگشت و در یک کامبک احساسی دوباره وارد رینگ شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69046" target="_blank">📅 10:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69045">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToFNKrBPP-FwnkbjxgYubi1zoHJ5rozCxD0KjuL923o3lCeLhkjJIBksUKbwJtlIRBAxAopvfOHFr__kdt208UT2m42-MqERjO_gaKT3nRAsGWujuMPuD-dDQ0r9VfsjoM0ByBzTNaNW6NTAHIel7zgILVm8TMVvv0zbNCUl1OLgv_p9Hrd5BH02OJvPBY6NL7mH4JS8Ucl4CiwaWpDCq2N78fgTBup34O4rgp-k5mYJkm4voijkxmK8oK1QYw0pTHXv-SBgN4mNZeoDhpnzOMkb7EH968AKp8k4bNSvO6tS7ak-RU7l-BJArhs05eMalzqWoKeoeX-vl243_zEDog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوش پرتاب میثاق ۲ / ۳ دست نیروهای رژیم جمهوری اسلامی:
⏺
نقاط ضعف میثاق-۲ و میثاق-۳:
برد و ارتفاع درگیری محدود
وابستگی به خط دید و اپراتور
آسیب‌پذیری بالای نیروی شلیک‌کننده
محدودیت در برابر اهداف سریع و مانوردهنده
عملکرد ضعیف‌تر در شرایط بد جوی
محدودیت در مقابله با پهپادهای کوچک و کم‌حرارت
ناتوانی در درگیری هم‌زمان با چند هدف
تعداد مهمات همراه محدود
فاقد سامانه دید حرارتی/شبانه پیشرفته برای کشف مستقل اهداف در تاریکی
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69045" target="_blank">📅 10:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69042">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/biIi4RNoG2kkpkKYpyZ_w9uqIpQIjv79ZswfRiLUOzP0dxtLhlqkEpuh3aAxULStH5XVahMP_Lt8jF8el59hSwLy277MdZfJgyk5SS6gVq7QNssZMrnYkX2X2Atte9ERZTOamleBzDp0YLN1HcNk127Tu4dNhWTEsshVh7ITVtPniQhn-zR-lS76VLY6scS6Ic7pB4jiEC8SXwo3c8noujUVjXsREcN9RbieSRaFofZhDpSZNym3t0gUV2B9aRZfLUh8oBh4YFcFmzekaIdyaN99kBX4nQibPHMmKCryP_myqiYXavpvEexj52ji-ei-s1N9kQ5O1uv748jfPRGUkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/q_EeYIxjsI2AlPltSIkDJIhgGHgCfhMstj0OTOcZCJfnJ0higFZdRxkYQPbwN53mctjBR74xR6GFt_Gqoj3bHQTy1vN4y2pz0NyktSluhUJu65v7oUoOZ8obbwYiXiBeMyrqFIyjILLMIa2RD_Zc12Thpbu7ecuyricvjfk21ABBXuz4dzdIMqsoI1bEnJKql6w_j7mArtfZ_yFI2qd5BAcUzAWsJSTUXXgZJJeCusVCvzL9kjl4i-jI3BEtRUOE40wMB5qwnNeOtcUCkHxEev-KZMIqdNbuHHICEUcQJVHKQOzlrkaf2yDiRX9vaoFKVZ1eYeSlftt-Lqv4hQjVAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/23b96717f5.mp4?token=SrlxTlXaGMAYdTU1ywBu81b3SoNbxRaiAf4_ENrdhTEqZJhKxidWwObk488laCvwY0INjcppFXJhc4AN7pvfiU0eI_hui5wxnb37GoOZ0p1-zzP2He7ZVW07_lTVfiXVc7AcGssArCpvqFdcYIUrB8-D-1Az8fQw0IQYGbqUrfZoa3_uGTu9fXkgPckZRkaFF7jt6-olbuA_e2-SVn-ljEe-0M9LhuYOv2h83jfijRwp_BBGgK9wjKhQTOBEymctIZ68ggVk-7C6q_Uy-K1UDkpDTUSxScFdkDMFxQSUrtzZWnuRA_fbqp4WC4940PjcXy_HbkmqrCOOlaYy6YWyWw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/23b96717f5.mp4?token=SrlxTlXaGMAYdTU1ywBu81b3SoNbxRaiAf4_ENrdhTEqZJhKxidWwObk488laCvwY0INjcppFXJhc4AN7pvfiU0eI_hui5wxnb37GoOZ0p1-zzP2He7ZVW07_lTVfiXVc7AcGssArCpvqFdcYIUrB8-D-1Az8fQw0IQYGbqUrfZoa3_uGTu9fXkgPckZRkaFF7jt6-olbuA_e2-SVn-ljEe-0M9LhuYOv2h83jfijRwp_BBGgK9wjKhQTOBEymctIZ68ggVk-7C6q_Uy-K1UDkpDTUSxScFdkDMFxQSUrtzZWnuRA_fbqp4WC4940PjcXy_HbkmqrCOOlaYy6YWyWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز ۵ ام مرداد، سالروز درگذشت محمدرضا شاه پهلویه.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69042" target="_blank">📅 09:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69041">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzz3YYHThj6dmVjF9GXQqfFra9xEfRA8ViPLDeVPPUmqM6RvjkOjegDUcsRUe6u70X_knK09Ibkxd2xJEkwonqm8uqSDa3WbuEhzcd4Mo-Qj0n4il2IfGsnFUXWU_2_yr-rd9HYyxS2S4Zis1zFczpQheqf2Pt-OAQ0y5Bn2FufifyI7PH_Ka3Vlkw4K6S_ahyFGGXDXnJ1ZLcu57JuBNPNnwltxFcv7Z7ys_66bx4DLXdardkIVPgHQBDfL6qWF_bNHnzqWp8kGFnzQwRv0cUd5kjDS73FQeXX_df4IR4kYwRGK5G0_H0Mz3_BTtzOrZM0bWC75fHQh7f9UdqwWlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ابراهیم عزیزی رئیس کمیسیون امنیت ملی : هر حمله‌ای به ایران همیشه هزینه داشته و امروز هم همینطوره. آمریکا و اسرائیل این موضوع رو خوب می‌دونن.
اوکراین هم ممکنه به‌زودی بفهمه که ایران هیچ اقدامی رو بی‌پاسخ نمی‌ذاره.
فهرست اونایی که درباره ایران اشتباه محاسبه کردن، هر روز داره طولانی‌تر می‌شه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69041" target="_blank">📅 01:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69040">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpRwGhs5OiQMTF7T6HMETnROLBRXADmQjVzJBs3GcDlohcK1S4WnTYK5QY5ZmfVrWYrWHsrwCc4zOoCCZ6KQ2kMwORFCzpo_3_Qo1e6vfX_LCiW3HGBVTuUxmlUWi1DYm6aDgE8iDuqP2bLbrxjO2SvL-U3gvAflshq4tdOXu8GCVB6Kk7AOBr650IJTrraJxseIjTOLuC9sep2pdETemnDeJ_NHpIWb9RJSMZsTQ88hBV7wjQHMP4ouYhYeEAIf3qYMgexK8cbP3vMA_d_lN-A2vsBb74xWbVPmOB4DQr_4Hmp60H5LqZUpDm4T7HUWFHfQfunsXONPMOe_T57atg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ آمار تلفات نظامی در دوران ریاست‌جمهوری خودش رو با رؤسای‌جمهور دیگه مقایسه میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69040" target="_blank">📅 00:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69037">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d3F2MwhRnBY3MvihXMY5P32DGoljZd-AvQxkmyiE0IOyl_EQ1nOUJIw0I2Vn2Z-xRoghsHYexzW3m6muP44bhwY5QRrzQryDgr8EFrg4KXfw2kzoO9iHccKyq8vOUlckd7j3D3NfF8UAEmSe2vzrOORFGUc6EDm8Rm13tnImFPeZEJVIWJITLVuD3Z5ApGm56z3UdufbVOXm-mv5TuBVS7EzncPoLmq4JVgKQAxTrCvKOujtkoeYdWlRz72YrvGCNQ08J51IGJpljCC0wDwdl3N09LPbJl8kx_gW8ipmHgxnyuyaqy_ZhFGZIhNAMzkkLhu7oClwoA5Qtcfkf9korw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MhDU4XYG8gB74ks5acfwEXpqC0JMvNawAHzKg4x8mc3ERzxh8jaqQll1OoIx_NbTRigY5F_iQtOBLIEZyEE5MmjBdjezpxsfqp31HVuUdzY4GTIk4ehgU1lDfT2jH-3DlYAjS4sPnEyPv2cy9BUux4DP75eM7VTipaOv2HItLuOT5OrHxHfEaBpTlm34PKiFGkt0y-Ww1cQBEpPOQRSC41GOUhBis4drlM1S7cX6XLtYpgHyAJjLuHyTZzRKLa2nzSgNGIdCZEsqjL3X3nZ3NbfMdm8aDvks_kNs6t2rU-MlbvYzMfmC-rSDZ10MQkN8PQBzhAO9_hFYok1oP_YHpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yqzy3ffnik4hvwVo6Bg96kJed3bvWcMV2bjFLbTrzr0Ee3WfzKE0JDfb2XcPmYjI4J48w35kSXuq6W8pamXWKDfZw9Jaj2gv6BZXzMlo_zgN6AT3vG421xxbELNyVy8xrOuEHY-DjU3U_s_g3K8-pU45bS0V42x-KBR_268OZZ3yJvzOBcWaPhemrzE8daCntYsf_9B8glZM6m6GGngYTWcYVKRZrD8NEXiYj19WaTRhyrzkSmiAhNAmNBtNTar9SGRr8EF8O2RjaSL13tMzILgYtorjUFj8TwzlwpxXFVZIPezQ2_l_vnvBeM-e977u8XxVktDfKojuWPnDf0FzGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
ترامپ در تروث:
- به طرح اعتماد کنید
- وحشت در واشنگتن
- آمریکا بازگشته است
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69037" target="_blank">📅 00:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69034">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LX6eICXMCavd6o-O9-spIhe01B1ctdOn4s1DiWiTyRWu0fWZruRHs9OtnntbVnvLwxfLu3hDDqo7jyYrUWLbl6ra49PUBcMlpqYgYwSgfuNot1_cxcCF-JO4zaeOf9f8GHDOBd2zeGKZmaTZxU-Yn5MIFDusHc-HewoeVbHsCgL_eYK5A1w1oL-kQ-__nfhATaipQyKdhQPfAAUJTexYHNNDPSITR_tRCdu2qT-5luaxfcu-2EKyb0HEg8H2PKil-qxr641gpARO85sm3dGtyJ2QhNNEQHz9dd4fAdipZgIGPQbkHekAZ9qsgAnTp9aJJzIqIM0bLPPyxFQewqcUEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CzQfN9o4SsNgkboQYYHciN4Il5X_pb_UBMNStcY1WPA__CSb_VmVILrFgnv9do7156ieYvTe5sHfZxCJpyMCmGNUVeTUVHRtMh_4LjDd_Glpk6IMMVzw5ca571BruRDSbvIn6dUdGUCrl1K2TKi1vxt2DtGk4Pn6OEA3Q8PKgA48E_UDLTFd-nX8CLTMW-MZShodkY1miZkElqF7C3zavIruJU9VHRjZhI0ZZLOQtD8kaz6HsijaDQyT3Y5CR8lhSXlESgYhxYZI2k3yUbA7V5Rmo3GDKYiyOxxsNPd6sJTYQ2Hc1za93OC-MTjjdgBb6DOfhbRioQkglb_L6BlMCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hL14UkJdXDBQLH6G2Cthtqz1uQvtJ_w3yvyhy9E3vUHvFauFRcz3YDmZ_dfbgACqEPHRkXss7WwuhuCtp-jaQs22Y1kcElchxy7hQmGUbj0GVhqFecy3uw1OBNCfgtDbwqVuYlIf649_9pHaCTx8iGu_Lhx8rOBtnhvn-XuWn1fkXVASLpISvjtddA6OxaDMmgdYf1AiHm4JSRyOCxlq9_MU9l8NIuOYeUGXgbtJ_jc5bTy6YpHn9HYNYPqmRYJk8HeCYcsuBt5sCi1uyL2WtIxMbr7Po9pz0tnOmjCfqKaZ7npMjeZSwgOUl7PP2moUl9DiK5ploKFXGE8baVDqRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">املاکیه دلقک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69034" target="_blank">📅 00:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69032">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vK0_2D9Z1Bx4D9MDvFKbkJt1ulA-rc_yAAMOHWCBsinonrcI-g5E80sAlvRmo4NqHW5HOCBEgyGfreEJl1cQzNhQZYLKoyAdN-GrR6ie2GdRMv2FmWBV8GD4hBvJ88s9CyVDpJoID2KAGN8FNBZIP4Fgn3VzDi4PzmjtZ4jcy3p0OBpVGoAWB5jcNRemEHYeOqc1GLmrl7oLVlbz0HkIgnd-eGqp0fbao0jKBKPGra_L1vqf7Sbc5FdK6JZ9sIvPsKwf9fGdQ3F6Ie_oXd2tsD4ItAhnyGeQJDIR5Ne1-iKCdEf4YbuC59MDwNXAhZX-P1ty7jhCC-CmjsgbI9hl1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KQduswxdCjxutPDKOwr_aiF9rYRGPYj1UAOZZaTGSXXsvLq5C63oeAjlmc26Cv2qwKCqZcbFHuKDpyf-h35KK8ToQXzikfbr3vK05fK5ufYnmS9C1DFgHjnf2wEho0AsRKSmmnVfjT50oZRZmJ4uX66FBnqw7sfaI7tj5XGMwE7nyxjtNaym5btrX0RB3T0ei7W7WJmTrNCNy2MW2gTy8BTdO7bphHDOfbnz0tfUYnPTUa0H8bLJliUiJrNNwInjFj6FvFV8BGt8AU0oUHwZ0jiFGhdObPdSSk8Qk_hUw_gT76oPt4sXEt8RnF89XAIM207dYBr1IzhCS5fJ37HY6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
همچنان ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69032" target="_blank">📅 00:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69031">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رفتیم تو 05/05/05 برنامتون چیه؟
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69031" target="_blank">📅 00:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69028">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T1vk-QkUgyMsoBWY8Tf6hedlLeqwU3BErfgHca7nFHKpqobThhcQRpiHOJT4-_kAPyM9O-g_ie4XyqNpPczY2FeDt6gTBUaSzh6ji0iF-xH6Z_3zzIegtpi6d7__VOUf_M_eOwWNnq33f3GRoeMkxDgFwsLl4cL8x8ocq7mrfH-hwbrHzgIYoREcK8vk7RFQ58WLzsUjqzXj1UczM4iELvLHGDN2iT8UaJRcA0FE18aPkOPYG1BxydW9E0IKC1iCowXWvN0gY7bxhuAd50X5gKV03rJY7_nGAUooSKvdHfc89D0pxMSK8nY1Uty83XRc-EaH8rWHCIG8v5fAdDic7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Li0Y5TnC1xmIKK_LziZsrC88M9ONfll2tKyjGc9838NPgX-Q1J74TO6w0uvEfCOnT-cm3YMvI_XMnaxjKmJrHYtTmXoFuA6MX98rwoCdMBWq1o5-8FY0YiQw7LZPBuJDtVcNgXFNDAZu0rKKHXNYLP_pmwN3v56PwG8PM6bHhmZMaFmfJB9TnAuSM7xp1VhK1tkq8mFrNrJqQ2OlMtWVsPEdY2_tbYIYb4UIROwcWQXZppjtXtQwqVgvVXBJo0ORv3L1d6DlYNLSk_3-8s8cUsqqnK-EL2usy6nfoVmyGorizIujJiq27U4_xznyq16jiBhG7eGYJn1wHnjH9W7-zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BPu2ig-6n2eYDB8cUq_CWMB-ItpMVSU4dKCHgOPr7HRsM-2dLM-_cxDSFe9vnd7hd-xbXAj8bPh-aiv8R_JOgCg2ION09u7yMttajblb-pOHU_l7_aDmyw3JJUg3zKKtF85YiayDNhq0wlLKi54bx2IUcKDdKWjMtgdj2V2In7rn0xS9yJKiJ_mR2oZQs38ARt5S2s0lusAo2OVAv8xgtrUiCN1gEE1H-Isj2aI-SGYxxFzlJDFP0NLeT13g4A80WdFMisywYeEOXkoIjMK4LSFXuYLczOQNJmS-a6P9vPGzUOpzz_sbyD8lCZAzjXnfiB-AVdNOl7GNbbVah_rvvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
تصاویر دیگری که ترامپ در تروث سوشال منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69028" target="_blank">📅 23:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69027">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
تصویری که ترامپ منتشر کرد: حمله به خارک  @News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69027" target="_blank">📅 23:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69026">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8FisaLURLxSO3fvTpa-8fuuZPk_TEIoH4NQUIeeVsI05MZlKpHDmeXStohU-F4n8UQeyXQYQwpNOctxt3NdVN6a-cRUCzjGcR8ezd9h-YEoNq9J5rC7YXmoXGW506kaIbNQ_QBYdi6KXkzMcREuED9nFSJrNa0IeC4QVIRSM7ira-lrOob9YKspkF0hutMCXJXsKWXlSgK_LXFHVcvYGbPy6fbZ465bZM9be6lhWs6NaVcQ3lRF7mAtzZBjJJ5Endt4GTGrjiUT8A-t4H4q848kKv20Q_YHKGUkpTfMincGMjCtER7Q2LwbJZ8igcIBrxcl9gBjCuVtQxgDRJAUkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویری که ترامپ منتشر کرد:
حمله به خارک
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69026" target="_blank">📅 23:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69025">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e3f5c86e5.mp4?token=gqmp0uSh1GEgJS65jgGhEMwhyhhd8zzGDnEQ8-pUdPbM31XaZitgT4lTHem_FkBOo4ZkcGjCgiIq9epAtIpaBQOxW7DTHv9IF2GK2SYNbcrwRosOY9UpE7geb_whDf7_FiEe5Wv_u4B6PqEX_okKu9yCOIwtjF2LDZoYAoye9TRR5KXLDfRPpb6SJP1k9IcYgdaAFSiF8N79sH8JFJe8fDfl81huq8Pp_qZQqfI32I6zAwD1-1ySdSYfzveExGEyHt3ZgXUKHkqS06cdFbOqskDfIZRVqiZSROvWflT6Jxf9oRvOUq2wwxolcONUfGpCOwc_u941co9rCJvixZmKTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e3f5c86e5.mp4?token=gqmp0uSh1GEgJS65jgGhEMwhyhhd8zzGDnEQ8-pUdPbM31XaZitgT4lTHem_FkBOo4ZkcGjCgiIq9epAtIpaBQOxW7DTHv9IF2GK2SYNbcrwRosOY9UpE7geb_whDf7_FiEe5Wv_u4B6PqEX_okKu9yCOIwtjF2LDZoYAoye9TRR5KXLDfRPpb6SJP1k9IcYgdaAFSiF8N79sH8JFJe8fDfl81huq8Pp_qZQqfI32I6zAwD1-1ySdSYfzveExGEyHt3ZgXUKHkqS06cdFbOqskDfIZRVqiZSROvWflT6Jxf9oRvOUq2wwxolcONUfGpCOwc_u941co9rCJvixZmKTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
سخنگوی ارتش درباره عدم حمله ایالات متحده به ایران طی دو روز گذشته:
«آمریکایی‌ها سردرگم شده‌اند و استراتژی مشخصی ندارند.
اهداف آن‌ها برای بازگشایی تنگه هرمز و نابودی توانمندی‌های نظامی ایران ناکام مانده است.
🇺🇸
ایالات متحده اکنون ممکن است یکی از سه گزینه را انتخاب کند:
عقب‌نشینی از جنگ
انجام یک عملیات هوایی گسترده
اعزام نیروی زمینی.
ما برای هر سه سناریو آمادگی داریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69025" target="_blank">📅 23:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69024">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTZyB34q4sxuO6MoDlf2wuRhhSjL-qqlwKa_79MFH8y31bhitusu-ln09YLKhafaLpl3JO48cPqWXjOyCyXzs760QIsLKewupn3BOCjywyLHEP1TMq9EFLQSGfGtkLbbMOV3rbiVlkQYkhd0dAwaLelZqKbRvK3mCbWx65rSftymojOGdyxiMEotCTBPjPMYU6c32WyDKu2zOGAqkYTv52rTfGuyGYNKoT7OQLsaQK5ye5wBq3FV7SxUJbx2NJ540SMuGqyJU8PEJXwIKsB1yD-0xoXLNBA6IEtB4swUC1YCClNho3jB-4zujoFgas24gMeQ4oVZUH-GgW4qr2ovKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇬🇧
🇺🇸
اکسیوس:آمریکا و بریتانیا برای برگزاری کنفرانسی بین‌المللی درباره تنگه هرمز برنامه‌ریزی می‌کنند.
دو دیپلمات اروپایی و دو منبع آگاه به وب‌سایت «اکسیوس» گفتند که ایالات متحده و بریتانیا قصد دارند هفته آینده نشستی سطح‌بالا در لندن برگزار کنند که بر تشکیل یک ائتلاف بین‌المللی احتمالی برای حفاظت از کشتیرانی در تنگه هرمز متمرکز خواهد بود.
بازگشایی این تنگه برای کشتیرانی تجاری، عنصری کلیدی در هرگونه راهبرد خروج ایالات متحده از جنگ با ایران و همچنین در تلاش‌ها برای ایجاد ثبات در بازارهای جهانی انرژی است.
به گفته دیپلمات‌های اروپایی، برنامه سفر و تاریخ آن همچنان در دست بررسی است و هنوز نهایی نشده؛ این رویداد احتمالاً وزرای دفاع و فرماندهان ارشد نظامی کشورهای غربی و کشورهای منطقه را گرد هم خواهد آورد.
پیت هگست، وزیر دفاع، و ژنرال دن کین، رئیس ستاد مشترک، احتمالاً در آن حضور خواهند یافت.
یک مقام کاخ سفید تأیید کرد که ایالات متحده و بریتانیا قصد دارند هفته آینده این کنفرانس را برگزار کنند. سفارت بریتانیا در واشنگتن از اظهار نظر در این باره خودداری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69024" target="_blank">📅 22:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69023">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbmdtoVo5IUTMt24KK_P5wYpf-czFo5CIf74V5Un0uxs0CUairs9YL-CkRVlJNdMcthhElhLFYMovoH5Ba6AJB_MpGHcGpk3ZrxfypY5W7KoRDqOqVHlz7t1yJHa1oU39yk_dQhQZmvZvKa8KC_ZVPYmhicr6oqX7DOsqPC4q7SvX1rAflq7-KAB7bMTjFNxIepy39jSHYW4-o4sYXgldfO7_oyZYh_MTXwcg3eDjjl037aBVghI4TWL4dHdruKVOUAEabSilgbZnnxtYdCGzOi9PN3qNe-QJ_CVvN43CmG1xjnNHec1PLV6QDIyraUSRaM3tnfmTMEdFSECzc5gbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آکسیوس: دریاسالار برد کوپر، فرمانده ارشد نظامی آمریکا در خاورمیانه، توصیه کرد که کارزار بمباران در اطراف تنگه هرمز متوقف شود، زیرا این عملیات به سقف کارایی خود رسیده است.
- این تصمیم پس از نشستی با مشاوران ارشد و مقامات نظامی اتخاذ شد؛ کسانی که طرح حمله جدیدی را برای آن روز به او ارائه کرده بودند.
- در روزهای پیش از این نشست، ترامپ تمایل داشت که به عملیات رزمی تمام‌عیار بازگردد، اما دیدگاه او از عصر پنجشنبه شروع به تغییر کرد.
- او تأکید کرد که دو هفته حملات در منطقه تنگه هرمز، توانایی ایران برای حمله به کشتی‌ها را به‌شدت تضعیف کرده است.
- کوپر خاطرنشان کرد که اهداف تعیین‌شده برای بمباران، عمدتاً تمام شده‌اند.
- فرمانده سنتکام گفت که گام احتمالی بعدی می‌تواند ازسرگیری عملیات رزمی تمام‌عیار برای تکمیل آن ۲۰ درصد از اهدافی باشد که ارتش آمریکا تعیین کرده بود، اما در جریان «عملیات خشم حماسی» (Operation Epic Fury) به آن‌ها حمله نکرده بود.
- او تأکید کرد که در صورت عدم تصمیم‌گیری برای بازگشت به عملیات رزمی تمام‌عیار، ادامه کارزار بمبارانِ دو هفته گذشته هیچ فایده‌ای نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69023" target="_blank">📅 22:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69022">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTsje_2q1vtvpMqxa7EOSwVfaU0LZaBjCbkdDFUR7cyCfMESTQV0AXltZY8hGpLABJhBTZWOUWQ8Br2NhBLhPXw71w-k4zi3A0K9jgn7qmdw5Nwmr4RChysrCcfp3WFPMrnau_OU8Zi-xDZblz4_4x2W5AbLkFjR9-Du2E_2vhQ0SBtn7yODGP4Yg571_XdSffNk5aF_0OiqNi9hGR75tI-_GvrSolxRdwFZI-PUrXI_VcPoyStWUXK9Ws04AcfOAym3AqTdbEWv93rG6Gbn7RGqNSHe_NR-4ePQ-PpVllIUQfOWYJYz6KwmP4Me_z_oIhI93hLC14GgsMXDitvsRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ان‌بی‌سی نیوز:
فرماندهان نظامی آمریکا عمداً به برخی از موشک‌ها و پهپادهای ایرانی اجازه عبور از پدافند هوایی خود را می‌دهند تا ذخایر رو به کاهش سامانه‌های رهگیر را حفظ کنند.
با توجه به اینکه ایران از آغاز جنگ نزدیک به ۹۰۰۰ موشک شلیک کرده است، فرماندهان اکنون فقط با تهدیدهایی که به سمت نیروهای آمریکایی می‌رود، مقابله می‌کنند - و اصابت به باند فرودگاه‌ها، رادارها و انبارهای سوخت را می‌پذیرند تا پاتریوت‌ها، تادها و رهگیرهای سری SM را که جایگزینی آنها سال‌ها طول می‌کشد، حفظ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69022" target="_blank">📅 20:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69021">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhy7b1g_NwNlJBSLYtpa8KKiWvJ7gdpbGnGQrGo8DsslHIh_ji0YVfi6bWLv3VgyjrLz5cUuJMcIUN4qWw-tyegyUM5A1TbAQzwp1de8g9DyAAzMUyIM8xJRgdTHN7jTw2Q04Xj0gb4mNPJXXU000ma7-Wcz5pA49O9uxweZ9epZJhUFokuKokt9mpotfBs3h0g3keGzwt4phFCVhJ2iqT4l0cwqqzzd0xDKMskRKaOn-5KasWp8pKSA7EJD2bqjcHvvpyByD-fImtJLQdIScU1v0s3BtywYtF5XUbPCpsWMXRVHdHdMkk9aUvOfxYwrcHwaLeqcflJnmRhUfWKxGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
عراقچی:
زلنسکی به یک کشتی تجاری ایرانی حمله کرده و موجب کشته شدن یک دریانورد شده است؛ اقدامی که نقض آشکار منشور سازمان ملل و به دستور اسرائیل، با هدف کشاندن اروپا به جنگ آن صورت گرفته است.
در گفتگو با «کالاس» (نماینده عالی اتحادیه اروپا) و «لاوروف» (وزیر امور خارجه روسیه)، تصریح شد که اقدام آن عنصر مفت‌خور در کی‌یف، هرگز بی‌پاسخ نخواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69021" target="_blank">📅 19:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69020">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78921238e.mp4?token=bjgSh4HbZFqG7KQqhSL6pjtAydZr5VxsAanu1VH6uoCdxVwkC0I7z1xDJqw6B2MabCQ5yU72DIFaK4EksSD3ixawMbXncDhgtGP7_FhalofAXGNBZU9tVsfOLguOY3_mNZ3YydsUcrqZxHe7YtJORUEL-RpKAGCWYJC5lIW_GGuMWrSi5-TaJu7Q77xC-JnTNd-Fi2I-QkchJ9eTshKOP7qPqi-xrr3-lVUAu8e_jnwmwcqlIYh-u0sSljT5qs9RIQO9B3yXxAKP0nLBPz4ujj9jVjKEKHUt3_b39lpchq6n052lE9BBgf5T-ueoDuwptBQGSIh8SeYBrzD39PlmkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78921238e.mp4?token=bjgSh4HbZFqG7KQqhSL6pjtAydZr5VxsAanu1VH6uoCdxVwkC0I7z1xDJqw6B2MabCQ5yU72DIFaK4EksSD3ixawMbXncDhgtGP7_FhalofAXGNBZU9tVsfOLguOY3_mNZ3YydsUcrqZxHe7YtJORUEL-RpKAGCWYJC5lIW_GGuMWrSi5-TaJu7Q77xC-JnTNd-Fi2I-QkchJ9eTshKOP7qPqi-xrr3-lVUAu8e_jnwmwcqlIYh-u0sSljT5qs9RIQO9B3yXxAKP0nLBPz4ujj9jVjKEKHUt3_b39lpchq6n052lE9BBgf5T-ueoDuwptBQGSIh8SeYBrzD39PlmkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوتا جوون خواستن برن جزیره لارک دیدن قایق نیست برداشتن شتر هارو انداختن تو دریا دارن میرن
😟
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69020" target="_blank">📅 19:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69019">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd02960948.mp4?token=Hp1Bgcw7vOddjj8Mnbxxl48b_f4dczXNkWLiBWsKTqA_dOeJvFQOujm2wFbLKqRhcOju-WrNbx4fxtcKSbNkh8nVuwUbBvqnNosy7iTu3w327CDLBpGnx5Z6JnRtzrZ7VLVoW4M1URZqrdF_qc393dICG0KOgn5TSm4wE1dNlpvYnwGmwXfjqAk7h5T-HWEcvxc1dTCRhvIxzyU22EQemvhVcXPiJUYQ1hOvEYycQTp6W5O79XVGNwhfr7t6ueZho1ri--ACGHYoyjdgRZg_06mWmoKHDwjbNLKMhPVJC_Mh0m-eckMMs3OJ4H6E1-jg7DePPab4H1noKBVpV9qoyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd02960948.mp4?token=Hp1Bgcw7vOddjj8Mnbxxl48b_f4dczXNkWLiBWsKTqA_dOeJvFQOujm2wFbLKqRhcOju-WrNbx4fxtcKSbNkh8nVuwUbBvqnNosy7iTu3w327CDLBpGnx5Z6JnRtzrZ7VLVoW4M1URZqrdF_qc393dICG0KOgn5TSm4wE1dNlpvYnwGmwXfjqAk7h5T-HWEcvxc1dTCRhvIxzyU22EQemvhVcXPiJUYQ1hOvEYycQTp6W5O79XVGNwhfr7t6ueZho1ri--ACGHYoyjdgRZg_06mWmoKHDwjbNLKMhPVJC_Mh0m-eckMMs3OJ4H6E1-jg7DePPab4H1noKBVpV9qoyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ویدئویی دست به دست شده با این مضمون که اگر فکر می‌کنید ترامپ واقعاً دنبال اینه مذاکره کنه با جمهوری اسلامی سخت در اشتباهید، این ویدئو رو ببینید تا متوجه بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69019" target="_blank">📅 19:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69018">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bca3e5bc1.mp4?token=ebwraftU5jnb_ka0PxBTqFj3EUkYbY5lKtRacPV18gi1QQYvmQKTFN9hoTD6Tw6CuIdnDxJZBTSaKqDJnIYrVHxPCjayPzr_aytHxacp3L6FtDZbEk_ZzF56Gk1dErQkydozc1QGtZG7-cYljZCsfB0WgS2KdWAdT2cXSO9tXFHNxAIkSed2mKtKlDj7rJ-JQiftla6PCdcIPY8MJs27n-IPT5GPz8JvCZQWlnwvO6fYiZUfl-SG_LvEsDBlBdHpkf7PdT6vwLHP148KYxaiYjnlcWF4xMlLu-lgSdu92_TUnM0nfzEcu_gflzeJLb5XO3dvWIZ2ifNn5AuscUe6uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bca3e5bc1.mp4?token=ebwraftU5jnb_ka0PxBTqFj3EUkYbY5lKtRacPV18gi1QQYvmQKTFN9hoTD6Tw6CuIdnDxJZBTSaKqDJnIYrVHxPCjayPzr_aytHxacp3L6FtDZbEk_ZzF56Gk1dErQkydozc1QGtZG7-cYljZCsfB0WgS2KdWAdT2cXSO9tXFHNxAIkSed2mKtKlDj7rJ-JQiftla6PCdcIPY8MJs27n-IPT5GPz8JvCZQWlnwvO6fYiZUfl-SG_LvEsDBlBdHpkf7PdT6vwLHP148KYxaiYjnlcWF4xMlLu-lgSdu92_TUnM0nfzEcu_gflzeJLb5XO3dvWIZ2ifNn5AuscUe6uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇺🇸
مداح حکومتی خطاب به ترامپ:
"تو گوشِ کَرت اینو فرو کن، خارک‌و‌سه جزیره مال ایرانه"
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69018" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69017">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHldiObrwryycHG3Peia7Rv47_9JhkTNdMhqaODpJQUKhMnXVu2EY6ejxMZj_-x9kpn3eg_OD4saFsdxz-Psx2EAg5rxJxINpLr_Btqh1FKBRkS7r9lV5itJ32V9JAEPz4P29ykN_N4cFpYtoMxFadhyA0Jo71cifFsvncVY_nEPT_6OCwxHI5OJ3M5p1NYn2xvKbrWBQjrXgCe7ceFnO1Ly6LFoySU-PRnNExol99q6pF0siL06Z2e8hP8aXsUlIyBhmtxfyM8tglPZWtWbmwLEiCV9XxzupVP3W17dpkz1aJxhXcsOJZDLRLmmykVeCjt0jKYLgGQXsVxFB2xUiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
العربیه:
- ایران به پاکستان اطلاع داد که از مذاکرات خارج نشده، بلکه مشارکت خود در آنها را به حالت تعلیق درآورده است و تمایل خود را برای از سرگیری مذاکرات در دوحه، ژنو یا اسلام آباد ابراز کرد.
ایران به میانجیگران گفت که با ایجاد مسیر جدید در تنگه هرمز موافقت نخواهد کرد و به پاکستان تأکید کرد که باید طبق یادداشت تفاهم به مذاکرات بازگردد.
ایران خواستار آن است که مذاکرات ابتدا بر تنگه هرمز، سپس بر دارایی‌های مسدود شده و در نهایت بر مسئله هسته‌ای متمرکز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69017" target="_blank">📅 17:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69016">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dcf952e60.mp4?token=lcbXSq7MqoMQPjSG-pdFwXwsuz6Fy5orJDDO1-OKeMj5Qv57IWnGsCBvUntK0PkEfRlZT5lWPOiVE9avl1vl1mSbOU0FuRahA3IQrmOeuQ-d1cBkFAdAYCENXtq7PSUMrns-Wq8VHZ7Olonq3wHIdEOTRoUAbmeRFZvi1ftDn31xturgFd4RzjYu20mptEF_PFgt5i0HhEylk2-vhJa-J-SC9sj446Q29r1E_7jAMbpE-u_57lBCJ0O8b-JllBV6cOJvxNVnxjtCPQBfRcaaPsS4oQA3OKP2X9OBPupJyoeVkj4ACJ5cCWHkV82WKGCGiddnyrB0v4HIce7b3EYQWaWN-P7_MHE4_qO0Huzw0K5FdCDkoP9y5qGyU75N8Kp8zxDDtJzWWCmUJU2YCvBtrFg8s5LgmACg89M5n5Hf3wa-yIYkav3mOT4lfPBxMVQS201UShqioVR4Plz3G6CJIY5HUMEsGtRyIJQf54oootosbBoz0VDbI2iGseXmn5_LEoRHlOxnuBZ247ZzAB2cFcoAkabU3In17YrdTo8p0LO80yuf8y93a51XwGixEiiQjCuJO1Hd_dy5UUQTp_1vqkcNpeOcvU9FKGU7xZiznvTdt_GY6YHe48c-XsiLLRpD2TPSljT52tGywwwbpGNVACg9w_9NOTwxead24bfGTl8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dcf952e60.mp4?token=lcbXSq7MqoMQPjSG-pdFwXwsuz6Fy5orJDDO1-OKeMj5Qv57IWnGsCBvUntK0PkEfRlZT5lWPOiVE9avl1vl1mSbOU0FuRahA3IQrmOeuQ-d1cBkFAdAYCENXtq7PSUMrns-Wq8VHZ7Olonq3wHIdEOTRoUAbmeRFZvi1ftDn31xturgFd4RzjYu20mptEF_PFgt5i0HhEylk2-vhJa-J-SC9sj446Q29r1E_7jAMbpE-u_57lBCJ0O8b-JllBV6cOJvxNVnxjtCPQBfRcaaPsS4oQA3OKP2X9OBPupJyoeVkj4ACJ5cCWHkV82WKGCGiddnyrB0v4HIce7b3EYQWaWN-P7_MHE4_qO0Huzw0K5FdCDkoP9y5qGyU75N8Kp8zxDDtJzWWCmUJU2YCvBtrFg8s5LgmACg89M5n5Hf3wa-yIYkav3mOT4lfPBxMVQS201UShqioVR4Plz3G6CJIY5HUMEsGtRyIJQf54oootosbBoz0VDbI2iGseXmn5_LEoRHlOxnuBZ247ZzAB2cFcoAkabU3In17YrdTo8p0LO80yuf8y93a51XwGixEiiQjCuJO1Hd_dy5UUQTp_1vqkcNpeOcvU9FKGU7xZiznvTdt_GY6YHe48c-XsiLLRpD2TPSljT52tGywwwbpGNVACg9w_9NOTwxead24bfGTl8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو رو ببینید تا از انواع بمب سنگرشکن و هسته ای اگاه بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69016" target="_blank">📅 17:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69014">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead75df70e.mp4?token=qRuwbDyzuJjJ2fjl9LYKV4k7yAto2pRdVOK_xO5XjDv26OFgaMu8CE51i5ti_zcq7laHJdOEOt58JEauFvKeQoVq8jz_qD7vA_HAAeGtXKc1J2CqRyRSmj78qb6NUQvhpKN-w585A7MAHLySMYoNndj-YlzuA0GUIRWG46auZlpg8XRENp-8usb_WI24T-7RKHR2hqkBWNuAAVE40sScIWx8ynALtETd02oyNPuL30mnzSEdesNzm-H-zSeCgRzkqFHBnZ72uwhn6PHt6X2gfPyMeUDlZrBlbXyRrrAa1idfjDIgpS63nxdzWv_U-Pda_y4TlQdvN1um6p5BJhqn5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead75df70e.mp4?token=qRuwbDyzuJjJ2fjl9LYKV4k7yAto2pRdVOK_xO5XjDv26OFgaMu8CE51i5ti_zcq7laHJdOEOt58JEauFvKeQoVq8jz_qD7vA_HAAeGtXKc1J2CqRyRSmj78qb6NUQvhpKN-w585A7MAHLySMYoNndj-YlzuA0GUIRWG46auZlpg8XRENp-8usb_WI24T-7RKHR2hqkBWNuAAVE40sScIWx8ynALtETd02oyNPuL30mnzSEdesNzm-H-zSeCgRzkqFHBnZ72uwhn6PHt6X2gfPyMeUDlZrBlbXyRrrAa1idfjDIgpS63nxdzWv_U-Pda_y4TlQdvN1um6p5BJhqn5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👑
شیوه برخورد با آخوندها در زمان رضاشاه از زبان خمینی.
رضاشاه، روحت‌شاد
👑
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69014" target="_blank">📅 16:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69013">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3FNp7plsxW0xkCCDUgFrReBzti8lDuEMrZRWNaRKTermrYPcnPjdOKQtIfRo9ZYnCDSO5QfU7P7Tx4YWc2gqEXMFmVbjSJuy5CIH4p2HU-LtyeM6ynCBdREw7drztm_JUUFWxZl-1iE-y8qxodJV7ArZACCMn4C3B-Qti1emesI1Ep4Gp7tnggYx01wU6_nZXaD7abjTNCpxlD08XZlCNfxIyKssTW50VQeVGEvha0ICwwD_-f_wcyizJnYfuTlBgXo-Up2pp39ZNvahU7vYRzog1e5jCIQDev98n26_Q44PxbWxKzXIIHzhggafdTjBAW2fH63npaB-kU76qzudg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
العربیه:
آمریکا و ایران به پیشنهاد مشترک پاکستان و قطر برای ازسرگیری مذاکرات، پاسخ داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69013" target="_blank">📅 15:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69012">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZmsBr28BtZNu87IDdUxFdZCQmTwoIG-fkRPdGk9bJlURWvRs5UzNQrSSB1VGhgroO_G6M7ACoAycRkIENv8ojgSmJVWsm4HuMPmwBHMONrHZG58NgJu7tJV4lkz77vqD1Vir8UCz4F9QC6Cipt1p69vVWw90uSdp0W0059g2Mh3SXeQX3UcRsWdGu9Et9Yp3PFJQ51REDRcL0ePrY0J4VB4hlCbV2LhqcXFZdwdMbkoAE_NFSw3sxFibRW0Wx0Q3hyZz3Hht_yqz3N59bVkd8dRFHrpSnPnZGYXN3LGxpAQXGC0ZSNPUqBwd9edwNmnPxVmYqCbSkL5Dd6RVH8FFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امجد‌طاها روزنامه‌نگار عرب:
ترامپ حملات علیه رژیم جمهوری اسلامی را نه به دلیل مذاکرات، بلکه ظاهراً برای انتظار جهت برگزاری جلسه رهبران اسرائیل و دریافت آخرین تحولات از سوی آن‌ها، به تعویق انداخت.
این وقفه بیشتر به خریدن زمان شباهت دارد تا تغییر مسیر؛
تأخیر به معنای توقف نیست و آخر هفتهٔ پیشِ رو می‌تواند سرنوشت‌ساز باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69012" target="_blank">📅 14:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69011">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=CJsDvHwgIHCt40eIKqfuudF1QKtK3jFcSmMNA3m0qhNr7inBx7JHvtHzOju8E5TqGcmKkCejcE3NBDB273rUxhapEFOrmufn4215vx2XTYk0wXK98Pp9smJMdGIJ5XXMY4D_v_PPturdRiljXZih3vSvEw8982umoJ4etNUKx-QCUU029VpCPPSiTnMAhbFl8NHm4P1qZkfAu5SSCQxKFYpoxsmieQty4Vmh_uw9scaUzoG27L2_9pswNIs6-QyzWICvFOP_nLTn-ZV9uaKr5pdN71zkbWxoQ4hh_Bl3RgIKvIcfWp44O1KyiuPbM-EyGs3o4IlTAI6lS0ZhhZgiKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=CJsDvHwgIHCt40eIKqfuudF1QKtK3jFcSmMNA3m0qhNr7inBx7JHvtHzOju8E5TqGcmKkCejcE3NBDB273rUxhapEFOrmufn4215vx2XTYk0wXK98Pp9smJMdGIJ5XXMY4D_v_PPturdRiljXZih3vSvEw8982umoJ4etNUKx-QCUU029VpCPPSiTnMAhbFl8NHm4P1qZkfAu5SSCQxKFYpoxsmieQty4Vmh_uw9scaUzoG27L2_9pswNIs6-QyzWICvFOP_nLTn-ZV9uaKr5pdN71zkbWxoQ4hh_Bl3RgIKvIcfWp44O1KyiuPbM-EyGs3o4IlTAI6lS0ZhhZgiKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
نخست‌وزیر نتانیاهو:
فردا به دعوت پرزیدنت ترامپ به واشنگتن سفر خواهم کرد تا با او ملاقات کنم.
پس از آن، در مراسمی به افتخار یکی از دوستان بزرگ اسرائیل، سناتور لیندسی گراهام، شرکت خواهم کرد. باید بگویم که او از زمان تأسیس اسرائیل یکی از بزرگترین دوستان اسرائیل بوده است و شایسته است که این افتخار را به او بدهیم.
من با رئیس جمهور ترامپ ملاقات خواهم کرد تا در مورد تمام مسائلی که در حال حاضر در دستور کار است، از جمله وضعیت ایران، گفتگو کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69011" target="_blank">📅 14:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69008">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oEjj3fZXvyg_dvODS_ZTJ8ixDO9N96RUQMTJ32UKTBhjc12dXBOXZpUAHyetBg4G6sfE8GAZuz5jNLMKfGkfyORjR38gdEdLtg0kCdsUQTZ7BbrJ6Abq6y1zCmZpGeNGlNQdFoRiadGYcM-_8mHpiaZl1EfzFnU9E79Zmsp65o29IGCq6Y4S9sSDmfz--a19zfCClKxM86yaxXdcTcQsP3QUJkCa0oJ0qAto99BrgflKsxQaJofLbIPUuLGehmxP0BjAXI6xGBasKkykR8EBbtXslJBaWLpwpaDqV1dZORyBdQXuT6bdpbw7qaltfw_VvWbv_pD4nCfkXp4KAeh9UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/s9p5ritHFGJElNsjdsFAuS3ABeI-pjLRXfHHm701YXL9BtuR8hBl4Mt_OIjlk5K4jYF0npHYEsGOrIx19HdfJnRqIyIBsfBC3C-5siHB5u0GiLfjZvJWVaEt2rscGAJeIBriyS98sWvp7xyCcb6L-iUdAqKdnMuTgIuvy_Ucpe56Ydn9aX3aDOnRYFt7Jq470Wp5J73IdCwsqVN2f4dewcJ8naIjRkxNRFXm9gEVJdCio0oubZxqDLLEka_83Yb34cKBlbIq3XTYgwf_mpeP0Q2-mxr7eoHK0iqiBNmg4EedVMjoTfU0ImXEUuQledVDh3gv7OEXFjtVNKrJl7Hjyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb51b8cf9a.mp4?token=f0Qup1yXBa8-pnYuLgtP9ow7uDIsyqshlWLlzu48Z1blBk6QkErOSEPEOvGb-_7DuQPCrMmfmJxaYmSHdMRDRmmk49xWR7Rfr_2yW_gQUSUMz_t-FvufD9QlU2a4WX2Uqaex2PxiaySSEwUkzbhsyFtmhXBdbfgTymDL1Yci94Y_yahJxhziQra911aJEmm4PSYKnVjHb7qj9IHCIsDKVPYI2KQz3Ps9l0QrCp20_j3CPlcox3aiWADwxdNE29ilji29ShUzafETtp285n0mQbxwGDnv2YY3azPhkVVJfL2KhtacGeuq-xu0LSNOWExIvXpoGEuIJuyHtMWGDiqNDA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb51b8cf9a.mp4?token=f0Qup1yXBa8-pnYuLgtP9ow7uDIsyqshlWLlzu48Z1blBk6QkErOSEPEOvGb-_7DuQPCrMmfmJxaYmSHdMRDRmmk49xWR7Rfr_2yW_gQUSUMz_t-FvufD9QlU2a4WX2Uqaex2PxiaySSEwUkzbhsyFtmhXBdbfgTymDL1Yci94Y_yahJxhziQra911aJEmm4PSYKnVjHb7qj9IHCIsDKVPYI2KQz3Ps9l0QrCp20_j3CPlcox3aiWADwxdNE29ilji29ShUzafETtp285n0mQbxwGDnv2YY3azPhkVVJfL2KhtacGeuq-xu0LSNOWExIvXpoGEuIJuyHtMWGDiqNDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز ۴ ام مرداد، سالروز درگذشت رضا شاه بزرگ؛ بنیانگذار سلسله پهلویه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69008" target="_blank">📅 13:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69007">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇷
محبی سخنگوی سپاه یه لیست از خسارت های آمریکا گفته:
⏺
در حوزه راداری و پدافندی:
۷ مرکز فرماندهی و کنترل
۳ سامانه ارتباط ماهواره‌ای
۶ رادار پدافندی پاتریوت (سامانه‌های پاتریوت به قدری ضعیف شده است که موشکها و پهپادهای ایران بدون رهگیری به هدف می‌خورند)
۳ رادار کنترل و مانیتورینگ هوایی و دریایی
۸ سامانه راداری کشف و اخطار اولیه
۷ رادار دفاع موشکی هوایی
۳ سامانه راداری EPS
۲ رادار EPS 117
۵ رادار برد بلند
۲ رادار پدافندی
۱ مجوعه راداری تاکتیکی
⏺
در حوزه پشتیبانی و لجستیک به منظور کاهش توان عملیاتی:
۶ مرکز تعمیر و نگهداری جنگنده و بالگرد
۳ مرکز پشتیانی و لجستیک
۱۲ مخزن سوخت
۱۷ انبار پشتیبانی تسلیحاتی و قطعات شناورها و هواگردها
۶ زاغه موشکی
⏺
در حوزه زیرساختهای عملیاتی:
۶ آشیانه پهپاد ام کیو ۹
یک سوله آماده سازی جنگنده اف ۱۵
یک سوله پهپادی که ۸ پهپاد آکبند در آن بود
۲ مرکز فرماندهی
یک سکوی سوخت‌گیری ناو هواپیمابر
یک آشیانه هواپیمای پی ۸
۴ سکوی موشکی هایمارس
۵ آشیانه جنگنده
۴ مجتمع پدافند پاتریوت
۶ سکوی پرتاب موشکی
یک ایستگاه پمپاژ سوخت
۲ مرکز مخابرات سیگنالی
یک مرکز داده‌های اطلاعاتی
یک مرکز هوش مصنوعی، پایگاه مرکز پردازش داده مربوط به شرکت آمازون
یک مرکز دپوی شمپاد (شناور مدیریت‌پذیر از دور)
یک اسکله سوخت
۴ شلتر جنگنده
۶ رمپ پرواز و توقف
⏺
در حوزه عملیات هوایی:
۱۱ هواپیمای جنگنده و بالگرد (روی زمین)
۱۷ پهپاد شناساییی و عملیاتی (۸ تا آکبند بودند)
یک هواپیمای جنگنده اف ۱۵ داخل شلتر
یک هواپیمای پی ۸
یک هواپیمای ترابری سی ۱۷
۸ هواپیمای سوخت رسان
۴ بالگرد سنگین
۶ موشک ذخیره
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69007" target="_blank">📅 13:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69006">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⏺
🇮🇷
بقایی، سخنگوی وزارت خارجه جمهوری اسلامی:
مقامات ایران و عمان در تهران گفتگوهای سازنده‌ای درباره تنگه هرمز انجام دادند و رایزنی‌های فنی و سیاسی در این خصوص همچنان ادامه دارد.
چندین دور گفتگو در روزهای جمعه و شنبه در سطح معاونان وزرای امور خارجه برگزار شد. در شرایط کنونی، هیچ تغییری در تردد کشتیرانی در تنگه هرمز ایجاد نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69006" target="_blank">📅 12:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69005">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
ویدیوی تعجب انگیز از داخل هواپیمای یاک-۵۲ که در آن تیراندازِ صندلی عقبِ اوکراینی، از کابینِ روباز با استفاده از تفنگ خود، پهپادهای گران (Geran) روسیه را سرنگون می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69005" target="_blank">📅 11:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69004">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=aEF37n-GaflSr5kbHBgJFyEPZCNBILPkEZ75UcnkCuidDeg4y_2LCtrOv3uPH3KWs5EoXhClJCwwFd9L-Bg1YqbXcjGC2BYZf8y66hidLTW6swAk4sX5ld8ZE1Y_QbZfcgAsPE6wndbVy9dWzxRsV4NjjB9rSHqGjMEX7V9Kw3405hrvvVI5ijp9LTucm6MK9QLdl1MWjB-AW6ye1mg5JBMeFXkSttl9FhhiA8I8OQC01i_AwDHAOoOGV1yNxvDIBdE_2g6iBH4Z8Dh2mh3cbOfY3b-ugqhMCsubItJqg0iG1GcP1btMXT8yKQiwEEAUXPFuQxo2PydRxQ9xgSxiqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=aEF37n-GaflSr5kbHBgJFyEPZCNBILPkEZ75UcnkCuidDeg4y_2LCtrOv3uPH3KWs5EoXhClJCwwFd9L-Bg1YqbXcjGC2BYZf8y66hidLTW6swAk4sX5ld8ZE1Y_QbZfcgAsPE6wndbVy9dWzxRsV4NjjB9rSHqGjMEX7V9Kw3405hrvvVI5ijp9LTucm6MK9QLdl1MWjB-AW6ye1mg5JBMeFXkSttl9FhhiA8I8OQC01i_AwDHAOoOGV1yNxvDIBdE_2g6iBH4Z8Dh2mh3cbOfY3b-ugqhMCsubItJqg0iG1GcP1btMXT8yKQiwEEAUXPFuQxo2PydRxQ9xgSxiqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
اکبراعلمی: مزد خدا بود و پاداش الهی بود که مجتبی انتخاب شد
😐
خدا امسال سه ماه قبل از قدیر ؛ قدیر رو برای ما نهادینه کرد و خدا برای ما مجتبی انتخاب کرد.
شهادت میدم والله خدا انتخاب کرد مجتبی رو.
با این انتخاب خدا کاری کرد نه نام خامنه ای نه راه خامنه ای تعطیل نشود‌.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69004" target="_blank">📅 10:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69003">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=WP6hio5ThQ7bwpc-umCXYqfPTsamTFaaRiho6xAL_74HLSw51t2zmEB_ypY_ZUNSVY9AFdAMZ69uo5lbKKXDz9ytY9rLUQ6KsQM1WdSGa07DkD2punl-mCsiaqtImoyHIrY10XXSOuTA0lvbhj8tbexyxbITnT_26P_G8ujMLmgIaBd_Hmtdm8AG9QF9He63FlDi6U5G6Md2QaExEzAe7rjwFZtxUVcdlggOnmtnLPiddC4fPkrRbhZf0nTj90eYI1hWlB56YaBtDVmQ3GuiVyi76eX_IdqrgAkg1zjc6vb1Q7TLOuEOUy3z7j45pKGNhrMWLFislTUH4MDwl-rrhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=WP6hio5ThQ7bwpc-umCXYqfPTsamTFaaRiho6xAL_74HLSw51t2zmEB_ypY_ZUNSVY9AFdAMZ69uo5lbKKXDz9ytY9rLUQ6KsQM1WdSGa07DkD2punl-mCsiaqtImoyHIrY10XXSOuTA0lvbhj8tbexyxbITnT_26P_G8ujMLmgIaBd_Hmtdm8AG9QF9He63FlDi6U5G6Md2QaExEzAe7rjwFZtxUVcdlggOnmtnLPiddC4fPkrRbhZf0nTj90eYI1hWlB56YaBtDVmQ3GuiVyi76eX_IdqrgAkg1zjc6vb1Q7TLOuEOUy3z7j45pKGNhrMWLFislTUH4MDwl-rrhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبل از مرگ خاطرات آدم میاد جلو چشماش
من موقع مُردن:
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69003" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69002">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDZU8gTfslk9JGJ_Dfjs7nSARof6yFr0k13875RIVOJM6FanNyrMcVaYqi0nQFcFp1q506u-MGd6jdkrxILvOyPE_6X8PQR5l7gu7MGna1a1zbVUvsJLBAXZUcbE9Go-iyt5L_nV9efgXKHsH6F0gecLIPpDeoL7QzExmRkwns9hyMIHGs2QQwbo0tE7HlCIqd_3S7_xNQXcJQuM9F2IFua-5CF1A_gYHoFNkRUOqi78qMPEhgnM3lG89nYJ9_o7iJuStYvJ7Hos4_8xUvKK1tzNnoNnOBJKrqNqzwg5hei25yYCetmcSE4co9zYNR34N-Jn7puhPCDuSxo9m-S1MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نیویورک پست:آمریکا طرحی را برای ربودن اورانیوم غنی‌شده از تأسیسات هسته‌ای ایران بررسی می‌کند.
نیروهای عملیات ویژه آمریکا در حال آماده‌باش هستند تا «پیچیده‌ترین عملیات تاریخ نظامی» را برای تصاحب اورانیوم غنی‌شده ایران از تأسیسات هسته‌ای به‌شدت مستحکم‌شده، به اجرا درآورند.
جوزف راجرز، معاون مرکز مطالعات استراتژیک و بین‌المللی، گفت: «گفتنش برایم ناخوشایند است، اما فکر می‌کنم محتمل‌ترین راه برای خلاص شدن از شر مواد هسته‌ای ایران — دست‌کم آنچه اکنون در اختیار دارند — یک عملیات نظامی است؛ زیرا مذاکرات پیشرفت سریعی ندارند.»
یک منبع آگاه از برنامه‌ریزی نظامی روز جمعه به واشنگتن پست گفت: این عملیات بسیار پیچیده شامل هزاران نیروی زمینی خواهد بود که به تأسیسات هسته‌ای ایران حمله می‌کنند - از تله‌های انفجاری عبور می‌کنند، از خدمه ساختمانی استفاده می‌کنند و یک نیروی دفاعی بزرگ را در اطراف این سایت‌ها حفظ می‌کنند.
به گفته آن فرد، از آنجا یک تیم کوچک از نیروهای عملیات ویژه، عملیات واقعیِ بازیابی را انجام می‌دادند؛ فرآیندی که «بسیار خطرناک» توصیف شده است.
این یک عملیات لجستیکی سنگین و دشوار در یک محیط رقابتی خواهد بود. ارتش ایران کاملاً نابود شده است، اما آنها هنوز از افرادی که از مادورو محافظت می‌کردند، پیشرفته‌تر هستند.
بر اساس گزارش رسانه مستقل و مطلع «های ساید» (The High Side)، این گروه از نیروهای عملیات ویژه می‌تواند شامل «اسکادران نقره‌ای» (Silver Squadron) از تیم ۶ یگان ویژه نیروی دریایی (SEAL Team 6)، گردان دوم تکاوران (Ranger Battalion) و گروهان ۲۱ مهمات ارتش باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69002" target="_blank">📅 09:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69001">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-JDfDsz4SWw50OwCV5ubg4WSxrGARGTt0RVLNY0l8JG5sq6GpmlV6SmOrZH9G_m947TztQ0t0ZpSrsxoE-kyo4GNzz_5Y9oK2wXVLPNJ0Y46SANXDiIMrBlfeFlXIiB8Yk1_ZSO8wunCu7-2EKFOkEHHONIbbN5R9sMUEzJMRhhT0OT8Vfonq0UWULqJycHvy49DhUTKS4wOdqKGRBXUeP4Yn2VHOGwGZkkjeQ0Gzwna4ikasrtfAGEWzBC7RsooA9evE3xTtRNXIxdVxFhKT9GZ1QwsUDQD5PRYln7p2tvMly2VizY1_MH0JYKIKsyAEKKhqthIMJ7Z0KjLxobhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
رادیو و تلویزیون اسرائیل:
با وجود تعویق حمله آمریکا به ایران در روز جمعه، روند پیوسته ورود هواپیماها و تسلیحات آمریکایی به اسرائیل همچنان ادامه دارد.
آمادگی‌های نظامی آمریکا، حتی پس از لغو حمله برنامه‌ریزی‌شده برای شب گذشته، همچنان در جریان است. این تقویت قوای نظامی، بخشی از تلاش گسترده‌تر آمریکا برای حفظ فشار و در عین حال، تلاش برای بازگشت به میز مذاکره محسوب می‌شود.
در حال حاضر، حدود ۹۰ فروند هواپیمای سوخت‌رسان هوایی به همراه یک اسکادران از جنگنده‌ها در اسرائیل مستقر هستند. طی روزهای اخیر، محموله‌های تسلیحاتی و موشک‌های رهگیر بیشتری نیز وارد شده‌اند که یادآور تدارکات و آمادگی‌های پیشین است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/69001" target="_blank">📅 02:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69000">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eae9373361.mp4?token=LdgbFp6WHYA0PaW2rrnowEedF2lic3UIqFr3cbOD_mkoH80MQcfEwiYAj9XUEXscq_PzALLzpu5VlVkPMxgm-vf5XxzTMwNEcgrOBmAifLemxV6kr5zCR1jTyutKzt54H-Rn_rXeBRaIeucY3jN_OdKwHVj77tB2vaw-kPZMC5mis82qax72_hwKX0ZzMBLrqheHfisHQTyA38-xaMzjna7EoGMLC2GDg9PtRkCpzfcGBt3syklRQtnv4r6F-SmpBBMrhyOQx7R4F7bxPN0PxLTPYrFuJ2JeLfCtS6ZL76yM-iDp_Dc7f3jmBjH1K2eiPUIiF6NkJqmVIPfWMbHUIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eae9373361.mp4?token=LdgbFp6WHYA0PaW2rrnowEedF2lic3UIqFr3cbOD_mkoH80MQcfEwiYAj9XUEXscq_PzALLzpu5VlVkPMxgm-vf5XxzTMwNEcgrOBmAifLemxV6kr5zCR1jTyutKzt54H-Rn_rXeBRaIeucY3jN_OdKwHVj77tB2vaw-kPZMC5mis82qax72_hwKX0ZzMBLrqheHfisHQTyA38-xaMzjna7EoGMLC2GDg9PtRkCpzfcGBt3syklRQtnv4r6F-SmpBBMrhyOQx7R4F7bxPN0PxLTPYrFuJ2JeLfCtS6ZL76yM-iDp_Dc7f3jmBjH1K2eiPUIiF6NkJqmVIPfWMbHUIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو خاورمیانه همه دارن هر شب در هم میذارن.
🇮🇷
واکنش عباس داوینچی:
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/69000" target="_blank">📅 02:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68999">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=M90ZEtYttntyZRDOfqI_lDIzMFwYMWOJzAbAXd-HguY4sBWLt777GG4f8yzj3P8C7XNEK-Mpd3Ws71SSRmKwDtpBUKIrWDmKx3syeYioj73aMqMLulmQ3YLBImUyyh1jUEDZwnrb51ZyY1P5VkLzJJJE6CsXdUpNTJM3IRZUNclt5Qb1-J8YU84rNcnyBEKhi25MLTz4348l1g7PvJ1tfAWAtJpnQqWz1yM6KCVot_vzb8ImtIm7a96X6GKGYuiJfLlc4JuFKkGtjsRfzN7wVD_IKZ4cwF0i-0aM2YEV0E2ZrrCMa857495EXL9oLi7-gjujIltLq3JDCiBC-Z0feQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=M90ZEtYttntyZRDOfqI_lDIzMFwYMWOJzAbAXd-HguY4sBWLt777GG4f8yzj3P8C7XNEK-Mpd3Ws71SSRmKwDtpBUKIrWDmKx3syeYioj73aMqMLulmQ3YLBImUyyh1jUEDZwnrb51ZyY1P5VkLzJJJE6CsXdUpNTJM3IRZUNclt5Qb1-J8YU84rNcnyBEKhi25MLTz4348l1g7PvJ1tfAWAtJpnQqWz1yM6KCVot_vzb8ImtIm7a96X6GKGYuiJfLlc4JuFKkGtjsRfzN7wVD_IKZ4cwF0i-0aM2YEV0E2ZrrCMa857495EXL9oLi7-gjujIltLq3JDCiBC-Z0feQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
محاصره دریایی ایران توسط ایالات متحده همچنان با تمام قوا در حال اجراست. تا تاریخ ۲۵ ژوئیه، فرماندهی مرکزی ایالات متحده (سنتکام) مسیر ۱۲ کشتی تجاری را که قصد عبور از این محاصره را داشتند تغییر داده، ۲ کشتی را که از دستورات پیروی نکردند از کار انداخته و برای اطمینان از رعایت کامل مقررات، وارد عرشه ۲ کشتی دیگر شده است.
پیش‌تر در روز جاری، نیروهای آمریکایی عملیات بازرسی و تأیید وضعیت را بر روی نفتکش «چارمینار» (Charminar) با پرچم کومور در دریای عرب به انجام رساندند و این نفتکش اکنون به مسیر خود ادامه می‌دهد.
نیروهای سنتکام در تاریخ ۲۴ ژوئیه، نفتکش «لاوین» (Lavine) با پرچم موزامبیک را در دریای عمان از کار انداختند؛ این اقدام پس از آن صورت گرفت که خدمه کشتی چندین بار تلاش کردند محاصره را نقض کنند و هشدارهای مکرر را نادیده گرفتند. این کشتی دیگر به سمت ایران حرکت نمی‌کند.
نیروهای آمریکایی همچنان بسیار هوشیار، متمرکز، مرگبار و آماده هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68999" target="_blank">📅 01:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68998">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quTwFOh0xcOOw4l5OcxD95BBqyVFBDSl1iR1OAMEyJt2NuSNCMR7uGUpfDHB7bEpi7fBmh0eT8rRpBdPAtHn8CdBbWL1h1X4Mv-3GpTYyQNAfZFIGL2m5S3ugXn-kvlGthoXHyxjELoPEMdCYpxFedvvvuuaCqT7TqlpxKEyeTTSPF_W04gLqzGtG9I-YsdJUn_zZKCER3ahkTDI_wv7WwiTWTsE1yFubCBl0NyCSMsMCToOo03Krh4Z6j9kMWSgmnePa6yViAkIViCqnXR_U9UVMhkq6A8KYtC9__xg2bWJrpK5baeAnWQ9pDPgt6S_ZC72CfoCxdIiQBx7y7hc0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ فروند هواپیمای سوخت‌رسان آمریکایی هم‌اکنون بر فراز خاورمیانه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68998" target="_blank">📅 00:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68997">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
اوکراین، یک کشتی متعلق به جمهوری اسلامی را در دریای خزر هدف قرار داد!
تاکنون مرگ یک ملوان در این حمله تایید می‌شود، رئیس جمهور اوکراین می‌گوید این کشتی حامل محموله نظامی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/68997" target="_blank">📅 23:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68996">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=dgy8QDWnCM1KlolVaBbOfyeNAELN5thrg4ir7FED8JI5c_pC2GOmHRoq7C3xJAesAzX7rWgp2gszISEb47z2L_M_vcsyA1AUyB58cXSKYV4wwxi7zHCt_QqYn8GLqIPIGzn8ucANzEA6dpphl6tZftxkoGzWvQpWGKrSy5Z3UQB6Dt3Hd6Rbsnl-w0qB9FG6ySo7HyMeuPM5uzKrs5pNBx1TFYYlxZjpoqjyXkO2pmx2qg7-XdOmAnE_O2Zsfoi_RkXMupfRIdhCnYsXAyK6GMFWClSrISvTO0QqeD9N8spMNPwS00fYo1vLIquTcsgqZw5XfhvyKrVFla6LEx6TLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=dgy8QDWnCM1KlolVaBbOfyeNAELN5thrg4ir7FED8JI5c_pC2GOmHRoq7C3xJAesAzX7rWgp2gszISEb47z2L_M_vcsyA1AUyB58cXSKYV4wwxi7zHCt_QqYn8GLqIPIGzn8ucANzEA6dpphl6tZftxkoGzWvQpWGKrSy5Z3UQB6Dt3Hd6Rbsnl-w0qB9FG6ySo7HyMeuPM5uzKrs5pNBx1TFYYlxZjpoqjyXkO2pmx2qg7-XdOmAnE_O2Zsfoi_RkXMupfRIdhCnYsXAyK6GMFWClSrISvTO0QqeD9N8spMNPwS00fYo1vLIquTcsgqZw5XfhvyKrVFla6LEx6TLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پیروزمند:
تا کی قراره ایشون ( مجتبی خامنه‌ای) بیرون نیاد؟
🎙
مجری:
تا نابودی کامل عوامل جنگ.
⏺
پیروزمند:
خب اینطوری شاید ده سال دیگه طول کشید خب ما تا کی اماممونو نبینیم؟ اینطوری همیشه در موضع ضعف میمونیم.
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/68996" target="_blank">📅 22:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68995">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlRkHqSelH3zHB2BqGcXAQ-4R4trrNZq8bWQEVOY-VD2xWMiByKquzGDXOil4hy0p1mUa9B6z87EWCq5E1yBfxbRreO0pFVqgrRZIqhYTCOOOlSRRuVbbQLipDbgaj7JTrkt0_MpgxtJqre74p3kUBSQxqSYWtJcivrvkwuw2OfFgLGk2vo4U9BJMJGeruUz09iSFZBW879rCD6EkON2NZcY5OSIA7rawL7xW6Z47ZS1EvODt87Yd9OzD2lN92MrOxrkKPjCK2zbTb4juxaw-N0J8a1KSP6AgeDE2pLGT81gbga0CQfBQMgiJxMg3J9TOYKI5nmq00Y7qWW0RGn2LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ در گفتگوی تلفنی با شبکه فرانسوی «ال‌سی‌آی» (LCI):
اگر «صددرصدِ آنچه را می‌خواهیم به دست نیاوریم»، «قطعاً» گزینه ازسرگیری جنگ تمام‌عیار علیه ایران را مد نظر دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/68995" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68994">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtMNkRw4_fTEmuyhOxuWAkztDkhVuhd4Fl6JyRx4lF0IVy_xC7hkNuV9CV_TnRMcvRwucJVfE6O3ILYyg4059Fw97cJGqlSiDp1orAjOxj-AkvpBIKWktuSzJHQ3nBtt09spZpdt0s35EBJ_kWllTZYZzz5-iNys-WaJ4aGA7i7l8I6QgpiXA-x-glKW-cxxx6SGhYyzRhGndOIrCJa6Hjc3RNoUo6FguW_zvO0q-2_FJ7-vdq2VsK0hdvlmy_kKvqqw5gmQ3_SIKBu22GlSl88WkIx629-TCb-eB9V4y1PDIhkcllya5Wace1p3c2lUD4kkCofQqTnhOCbKKLgwVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:
رئیس جمهور ترامپ روز جمعه به ارتش ایالات متحده دستور داد حملات به ایران را متوقف کند و به تقریباً دو هفته حملات روزانه پایان داد.
این تصمیم در حالی گرفته شد که مقامات عمانی در تهران مذاکراتی داشتند و گزارش‌ها حاکی از پیشرفت در جهت توافق احتمالی برای بازگشایی تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/68994" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68992">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-7f89nV8VuMtIHtoRvSeD5c7H16XcCzRCrzzy7pTkMDU3L3Jd6nrfasr35QBwbJwpBZJWI-qKyXEQxi6NHjidN0poWku0_2OVw3nWviB62E0Gfkdxdh1qP0K5buY-R2fnFDe8Dwqn1sFSwfWkb56fNKu22BdWHGiSdQQ1KFAXdT87BiCTkSzaPWHYqJurhN8XcRFDetuLhaxJMtXmuE-tchaBFB2P31ROevESPRlCZSp1BG1jxKI6hoxdG3trCOAoNavb3029lYAgqDrVr6mpFpoNi1OKKQfHWCZ263WElyKCa5yxDxtfAez_cUXU7jvTJq6iesdBGcngsDHBR36w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=Jj8ygxEymEovYjQkqQNIhiAZlu7T8QjexI-1VjuVDptdDocZmblOWw_3-bybqXjqleYNKXcqpxfqNafq_tq-s7Mud-0I-L2qxt_EhDOVvzNsu9VWM7JQ-kUb1Rp_CRKovvu-oCJZgRRL_it8TzZQpHVNxSuPHt1689oixn9J5E8ESif5A6aDG3YHfYjm4JC1pWX1Sv2BzolJOsCR_6l-6ELnqHCE4tuH8gbLSy6sh5kHQDkW79U9RJVhmquVHCCoJaQdVZBBpfcJaXncPHSf9O76CkXFZCxuL1tgiLxSBZoTjLob-2RArAnN5ybnOj8qcET1QgYr6mUx7AHWDfdEZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=Jj8ygxEymEovYjQkqQNIhiAZlu7T8QjexI-1VjuVDptdDocZmblOWw_3-bybqXjqleYNKXcqpxfqNafq_tq-s7Mud-0I-L2qxt_EhDOVvzNsu9VWM7JQ-kUb1Rp_CRKovvu-oCJZgRRL_it8TzZQpHVNxSuPHt1689oixn9J5E8ESif5A6aDG3YHfYjm4JC1pWX1Sv2BzolJOsCR_6l-6ELnqHCE4tuH8gbLSy6sh5kHQDkW79U9RJVhmquVHCCoJaQdVZBBpfcJaXncPHSf9O76CkXFZCxuL1tgiLxSBZoTjLob-2RArAnN5ybnOj8qcET1QgYr6mUx7AHWDfdEZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ساعاتی پیش یک هواپیمای آمریکایی در فرودگاه جده فرود آمده است. به نظر می‌رسد این هواپیما یک هواپیمای آواکس مدل E-3Sentryباشد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68992" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68991">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uN1Zxh9ro_YLCstXgNEUoNNvugPRMEYI7UkZk09ryToXJu-DK9i1EyZ1GNMAoaClh-CLVQuqJ7PkqXuMVhh03-j0BdxV1kxUfLiCtPCo9uNWLOQCI36XOt33Bj7B8LJLyB4icEDd9o_GLpLG2G3FQebOw7dATrP9OMsNcRzHaU_YMtZQrkW4FvajUYQ4bgzpbQSrOaqRyerwOrOs3B7YXuiJXtgHvP1fZ60hBWMaECDnOqQaW-SmTsuEOrS4S-u5Bz_L6HvUQt6aiw8Gm1SIg6r1BNLClkv3dy-3LFB9MQU9ZdHFpxaq5ZfRD15GtLEFJcHGtkDHwTgF6DRmCgdtaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
باراک راوید، اکسیوس:
آمریکایی‌ها دیروز برای عملیاتی گسترده‌تر در ایران آماده نشده بودند، بلکه برای حمله‌ای تدارک دیده بودند که از نظر وسعت، مشابه حملاتی بود که هر شب در طول دو هفتهٔ گذشته انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68991" target="_blank">📅 19:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68987">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4bab692977.mp4?token=TmA2nDVEUMQhobvI_JABsc_N2BZ6hnlMAxZIcDwh5cmPnotSUCbBNhyw_ME-JglRR3bHYa6O6V5dcG6HAAdZ2JrtZ5GvXdeKNZrVYtnATFIU5GBC93uHHGWr1hU88TsRpoOKxwQR9rA-eZlZujBzoXXkEtACQpWXhmbuDwK5viod4d6te2EZ5K7A-PBqkg0vb9WyDvfSHcYmzL8vIHYMbnxvH_cbUtLWxg6gcYxK2wNzT-SrZYSnUlE-ExOgHPAfrw9Mlp3sJYlGNtMWhnA1X1b0VK8WNombQO995WIQ12XlcXVQgSTLPWhZ6In_RBhHDZVGt53CjDKIUkpX8HTtPg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4bab692977.mp4?token=TmA2nDVEUMQhobvI_JABsc_N2BZ6hnlMAxZIcDwh5cmPnotSUCbBNhyw_ME-JglRR3bHYa6O6V5dcG6HAAdZ2JrtZ5GvXdeKNZrVYtnATFIU5GBC93uHHGWr1hU88TsRpoOKxwQR9rA-eZlZujBzoXXkEtACQpWXhmbuDwK5viod4d6te2EZ5K7A-PBqkg0vb9WyDvfSHcYmzL8vIHYMbnxvH_cbUtLWxg6gcYxK2wNzT-SrZYSnUlE-ExOgHPAfrw9Mlp3sJYlGNtMWhnA1X1b0VK8WNombQO995WIQ12XlcXVQgSTLPWhZ6In_RBhHDZVGt53CjDKIUkpX8HTtPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلنج شکن معروف اینستاگرام که هر چی داف بود میاورد پیش خودش و نالشون رو درمیاورد دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68987" target="_blank">📅 19:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68986">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=XNRN1KvhrUcUWFdhKxYwvGSphKjrKVz8QnsI-PYeu8KK2Q2AdzlPBH4SwODXuuFgy0FrsOp-O-41xzrOhKFWLq1xrjIC48wwMFOPiP3H1w0-0Dvk5usIVVuJfEUbMDds_rChu3ikEGD2ru-y5cwVNDux9kd1QeUkoxpJRcSOkFmIDsX49Q6-3MEkMPuqBDm8YlK2ZRvAcS0VtWJ5TiInCPI4YV6P5VUfiQv0xHoAcbMoNFWJC2-UPgun5KG_wedb4lF2OcwLu1LE1k59OBnpzEAMx-AmjJLzAPC7TX8oCO5x-XaZcKOWMXc22o9XFNfSsBPv55XBvT2tMEeX3JKOUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=XNRN1KvhrUcUWFdhKxYwvGSphKjrKVz8QnsI-PYeu8KK2Q2AdzlPBH4SwODXuuFgy0FrsOp-O-41xzrOhKFWLq1xrjIC48wwMFOPiP3H1w0-0Dvk5usIVVuJfEUbMDds_rChu3ikEGD2ru-y5cwVNDux9kd1QeUkoxpJRcSOkFmIDsX49Q6-3MEkMPuqBDm8YlK2ZRvAcS0VtWJ5TiInCPI4YV6P5VUfiQv0xHoAcbMoNFWJC2-UPgun5KG_wedb4lF2OcwLu1LE1k59OBnpzEAMx-AmjJLzAPC7TX8oCO5x-XaZcKOWMXc22o9XFNfSsBPv55XBvT2tMEeX3JKOUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تیم‌شی‌هی سناتور آمریکایی:
جمهوری اسلامی گروهی افراطی و تروریست هست که 47ساله کشور رو تصرف کرده و ایدئولوژی نفرت انگیز خودش رو گسترش میده.
این رژیم اهمیتی به سیاست های حزبی یا اینکه به چه کسی رای داده‌اید نمیدهد.
آنها میخواهد همه ما را بکشند.
ما این جنگ را شروع نکردیم، اما تمامش خواهیم کرد.
حملات موشکی پراکنده به کشتی ها یا تحرک قایق ها در تنگه‌هرمز نشانه قدرت نظامی نیست بلکه دست‌و‌پا زدن یک حکومت در حال سقوط است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68986" target="_blank">📅 18:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68985">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzkSX2PacMsv-v34lGCNnMdR_x0lVAc82udyHthofnEOHeVz1nsXL7epryIZ-NzPS8c7WWfyGdAsxM6nWoYOCNLHrWY4jHndDX_kEbji88QQfZiE-sHkJ_BqS497WD_Gyx1peaUEPzrZ18J8j-oK1DBpqCH4sFeSp7Vx0h93UtjpMHBAun7BPQJqx1rQdYc6sxJTo1A5-uj0Xl4Uh3UnaSy253mnCQlJnNUfgOx6Dkid_NqIjU4fEZ_eO5dK6kr65-CY_aQQY1Yu7egl1uGKHAg8GzS5J37PdG4E1OCWvKdnWPGFDxYfcMeKRokYwdn-D_hDOUIOVM-mAB-NOASzVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
وای‌نت:اسرائیل انتظار داشت که ترامپ دیشب ایران را بمباران کند، اما در نهایت از اقدام علیه تهران صرف‌نظر کرد.
اسرائیل روز گذشته را در حالت آماده‌باش برای یک حمله بزرگ آمریکایی سپری کرد و انتظار وقوع آن را در طول شب داشت؛ اما سپس متوجه شد که ترامپ در حال عقب‌نشینی و دادن فرصتی دیگر به تهران است.
قطر و عمان فشارهای سنگینی بر ایران وارد کرده بودند تا پیش از وقوع حمله‌ای که تقریباً قطعی به نظر می‌رسید، کوتاه بیاید. برای نخستین بار طی ۱۳ شب گذشته، ایالات متحده هیچ‌گونه حمله‌ای گزارش نکرد.
یک منبع اسرائیلی وضعیت را این‌گونه توصیف کرد: ترامپ تمایلی به حمله ندارد و تنها به این دلیل به سمت آن متمایل شده که احساس می‌کند دیگر گزینه‌ای پیش رو ندارد.
ارزیابی اسرائیل تغییری نکرده است: احتمال دستیابی به توافقی واقعی صفر است و تهران تنها موفق شده برای خود زمان بخرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68985" target="_blank">📅 18:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68984">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=kY4hdYyUvWeWB1rwT22gJITv97CbKdvEolv00GLVywTYuLW71JY1fwn6Y6B0RPPHK1EWDIBFFmXjO1BMUKfMTituZPMsSard33RzwNxlTTanYaEOCmO02RbrpzyWufhEtg-3LK-AUpCwpYyk-lSj1AGeU5Rja2gqFdaspHNwS9Pm37BqhOdqopGmfYQdhxGxA2UeJFTLHfBhro5VTuTGagkZfrM_wNEkN-JFs6S9Zo-uVlSJHM-2eRQTxN24hrh6y31YYJxeA18XC4MvGjN_w9mK24Piiwo2-biveYQJXVE3jFUY-IUr-gwSjxnLhKjDwaRbyQgEViR3rT48tG-Apg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=kY4hdYyUvWeWB1rwT22gJITv97CbKdvEolv00GLVywTYuLW71JY1fwn6Y6B0RPPHK1EWDIBFFmXjO1BMUKfMTituZPMsSard33RzwNxlTTanYaEOCmO02RbrpzyWufhEtg-3LK-AUpCwpYyk-lSj1AGeU5Rja2gqFdaspHNwS9Pm37BqhOdqopGmfYQdhxGxA2UeJFTLHfBhro5VTuTGagkZfrM_wNEkN-JFs6S9Zo-uVlSJHM-2eRQTxN24hrh6y31YYJxeA18XC4MvGjN_w9mK24Piiwo2-biveYQJXVE3jFUY-IUr-gwSjxnLhKjDwaRbyQgEViR3rT48tG-Apg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فارس با انتشار این ویدیو:
مردم جاسک، اسلحه‌ به‌ دست منتظر اومدنِ نیروهای آمریکایی هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68984" target="_blank">📅 17:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68983">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=TVf7WtYlAtVmcMe4xijQDvKSVG5Fnja5-8mIxYTi4nIYqKaUZkVYpHqRaoouuUX56QDfvHF47fgG2nrspKCBHHYeiiT_xW51zPhFreBh52IQTypMBu6d1ZGr09ijI12crL1CkxgSfKuMi3LflBdLIfQKLpeXLvnJa1cXqbPOs1PhbMzJNK8C5rg_UnL0M1YJ80_hvBsQpnb9yH0yK1L9WkXw89v4__f5MsA7Z9pSxBwA9RCILA2VKJWs3-zvaIvJzm2kua_kV9dipWX9n-ga7dCqeF57i_QMaqL5LfAvhpKRHlYq4X7ib-O26hoT23S4FTfiaRQVW6bcNiDA4V50ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=TVf7WtYlAtVmcMe4xijQDvKSVG5Fnja5-8mIxYTi4nIYqKaUZkVYpHqRaoouuUX56QDfvHF47fgG2nrspKCBHHYeiiT_xW51zPhFreBh52IQTypMBu6d1ZGr09ijI12crL1CkxgSfKuMi3LflBdLIfQKLpeXLvnJa1cXqbPOs1PhbMzJNK8C5rg_UnL0M1YJ80_hvBsQpnb9yH0yK1L9WkXw89v4__f5MsA7Z9pSxBwA9RCILA2VKJWs3-zvaIvJzm2kua_kV9dipWX9n-ga7dCqeF57i_QMaqL5LfAvhpKRHlYq4X7ib-O26hoT23S4FTfiaRQVW6bcNiDA4V50ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از طرفداران حکومت، با انتشار این کلیپ آمادگی خودشو جهت
مبارزه زمینی
با آمریکایی‌ها به رخ کشید
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68983" target="_blank">📅 16:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68982">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⏺
🇾🇪
بیانیه نیروهای حوثی:
در پاسخ به تجاوز آشکار و جنایتکارانه عربستان سعودی، نیروهای مسلح یمن دو عملیات نظامی دقیق و موفقیت‌آمیز انجام دادند. عملیات نخست، با استفاده از ده‌ها فروند موشک بالستیک و پهپاد، تأسیسات حساس شرکت آرامکو در جیزان را هدف قرار داد.
عملیات دوم نیز با بهره‌گیری از تعدادی موشک بالستیک و کروز و همچنین پهپاد، تأسیسات حساس شرکت آرامکو در ینبع را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68982" target="_blank">📅 16:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68981">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=CDKjEzc9sjI6mcsVa67CpX0V9n7VpEcm8WRf6lQHAY9MBDf8BJ5F_pWFF4xDLkXYMNwu6TH7huAefvWI-IpiA5g8JGBmtjkwMO5TUPYsHp9VCjRftLsHhpx6kjEOYm8cx6hCyctjYeDVZIvDx2DlRzGLNqKscsxO_WREyQg3g9VdhTKrQgciPu2Z8Rn_jME6IMajP28E6N3Xa1p8nnln3bKQZfsTDqII0Boznoh59Rj0y8uZx_YCOiZA4X3WuNHYyNE0FEnKEamTJk6_wI_o6iDkDOKmuLKaRYDAwqbNxS7o1JkRQESb0nlBNDMkwSPRWUDzNTL6cMjEhJ2Kc14VSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=CDKjEzc9sjI6mcsVa67CpX0V9n7VpEcm8WRf6lQHAY9MBDf8BJ5F_pWFF4xDLkXYMNwu6TH7huAefvWI-IpiA5g8JGBmtjkwMO5TUPYsHp9VCjRftLsHhpx6kjEOYm8cx6hCyctjYeDVZIvDx2DlRzGLNqKscsxO_WREyQg3g9VdhTKrQgciPu2Z8Rn_jME6IMajP28E6N3Xa1p8nnln3bKQZfsTDqII0Boznoh59Rj0y8uZx_YCOiZA4X3WuNHYyNE0FEnKEamTJk6_wI_o6iDkDOKmuLKaRYDAwqbNxS7o1JkRQESb0nlBNDMkwSPRWUDzNTL6cMjEhJ2Kc14VSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبتای دیروز پزشکیان که تا به بحث مذاکرات رسید صداوسیما سانسورش کرد:
بعد از جنگ 12 روزه، علی خامنه‌ای رسما اعلام کرد که ما دیگه با آمریکا گفتگو نمیکنیم و صداسیما هم اعلام کرد.
یه روز رفتم پیش علی خامنه‌ای و گفتم خودتون گفتید نه جنگ - نه صلح، حالا ما چکار کنیم؟ گفتش که برید مذاکره کنید و ما به دستور علی خامنه‌ای گفتگو با آمریکا رو شروع کردیم.
تو آخرین پیامش هم گفتش که برید مشکل رو حل کنید چون تو حالتِ نه جنگ - نه صلح نمیشه کاری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68981" target="_blank">📅 15:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68980">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=jHX1sWqA02PA6XdoQ4bxlupkUSnOeJ8IkTvc2VKM3_BFGwYFur679tMiZpT3sne03hce0WiBq7YEXr3Iue_WMABKHLOm6Uz02MkcGOoRQdfOMHa5qRPcmnPNvBdo3hSLU2uYiydGqzmN78cPQPf8URgl4RAw5VuZ-g9j45E5n8GGFu9xU_NAYLDHmuxevknqSQOBY3qYeicMlhh4MEqM7A-erVtMxR20Qo0s_7zhQHkh-MD2npLxSSU3RreN4qyD-5NWWzKiilzRkIzXaf8idUbw5pJp-EMPn_NM-pNiCn5QZXW68HrZKEoxyTfim0S5ssCUZYsORozcnw32dOABKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=jHX1sWqA02PA6XdoQ4bxlupkUSnOeJ8IkTvc2VKM3_BFGwYFur679tMiZpT3sne03hce0WiBq7YEXr3Iue_WMABKHLOm6Uz02MkcGOoRQdfOMHa5qRPcmnPNvBdo3hSLU2uYiydGqzmN78cPQPf8URgl4RAw5VuZ-g9j45E5n8GGFu9xU_NAYLDHmuxevknqSQOBY3qYeicMlhh4MEqM7A-erVtMxR20Qo0s_7zhQHkh-MD2npLxSSU3RreN4qyD-5NWWzKiilzRkIzXaf8idUbw5pJp-EMPn_NM-pNiCn5QZXW68HrZKEoxyTfim0S5ssCUZYsORozcnw32dOABKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروهی از طرفدارهای حکومت با مقوا عکس رهبران ارشد نظام درست کردن و اومدن تو خیابون
😳
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68980" target="_blank">📅 15:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68979">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=XWS-IWUUk9BNXVb68Roo7tkXV3UiVAt-vOs2lpbRtUEIIkhoQuIH_3D6ciHB-btALYmpkrQEmnqcExMoG7msIftQpjAtTQWYU3qq4Uy1wPareaKXoGQsDSCaHF3AhElDmeV1Hv8NBc9twvAMUqsiCfI1tZEuag7LOVijuCskAiHqHG2AuwNF0PcczX5CgBJfbzDp2yBBd1kju5auUgzjj2TT8XUTICej-6tYaEICy0Z9Y6r2s73sGNY9e8NY6Jssyf8lR5LBoen1a4Rep3gkW8akp1yakX5Q45gE9dlTKem5Lmxv264VGsOlNxslKIAjBbb4VwSZU1mpsqALXIdGnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=XWS-IWUUk9BNXVb68Roo7tkXV3UiVAt-vOs2lpbRtUEIIkhoQuIH_3D6ciHB-btALYmpkrQEmnqcExMoG7msIftQpjAtTQWYU3qq4Uy1wPareaKXoGQsDSCaHF3AhElDmeV1Hv8NBc9twvAMUqsiCfI1tZEuag7LOVijuCskAiHqHG2AuwNF0PcczX5CgBJfbzDp2yBBd1kju5auUgzjj2TT8XUTICej-6tYaEICy0Z9Y6r2s73sGNY9e8NY6Jssyf8lR5LBoen1a4Rep3gkW8akp1yakX5Q45gE9dlTKem5Lmxv264VGsOlNxslKIAjBbb4VwSZU1mpsqALXIdGnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
تغییر قیمت یا سهمیه بنزین قطعی است.ما علاقه‌مند به افزایش قیمت هستیم!
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68979" target="_blank">📅 14:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68978">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iaaQWmTgpqO3ZtWCUj0E2HR9EQgl1UGGnUX_AtgnVH0XYB9X7q1EAwipIkm_ZHK5kKx8fwbeZRKa33Nob3ObPI72LcX8Nb4YsTCkEoFb4YfJmLBJEiUm9Oeg9nbhzxpLQAPg_czloc-8BnkO8wbW0Kt4EwkkncaeX1BOpP3XTXgTBJJE652T1-zFA4WFBJOfHhsUWRSbacTISjrIu3RyK4gTQuvCUqJhl9i7IcdhnDHO1Ub3t5YCa-Y6Q9W6_gDIp9vzShkaGHygbiCY2YNtlG8vxTQSUTD1777GG9C4-h2PoUe16i8fcBkMW_14F2hzy2DTFElYltaYph8V1Y34kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی:
در پی حوادث تنگه هرمز، طی مذاکرات سوئیس تصمیم گرفتیم برای جلوگیری از سوءتفاهم‌ها، یک خط ارتباطی مستقیم ایجاد کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68978" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68977">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=tRsaK27UA2vSjgkd-18jiA6poBJOywQbd0NgsRxNSbne6K16288FpsGANq8Lvn185GW6f-Wu4LRi_rQE8N8B6OCsEPlg3ZwBTEjefPvYbKtdwqoVRaxflZkPmNHO34_DPuG8o9vMmlZ1ias0ds_I9YSZAEChrOz77gUVSwf5MBuDyfTx7imUeG4RYU_gN44bcHYomT5YFgjZZ8XLQJpSebloKmdgH8o7_GgzSzkPZERfn-AeMo50PNvvkXOFUkFpbJJV20EjPhxViJZ3fVON6sKZ8qKwVEQN9M_FvZAHkUlIVPiTX1m82L7P0OqKRcLFybzWnxMyJH55dlvWqRLNiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=tRsaK27UA2vSjgkd-18jiA6poBJOywQbd0NgsRxNSbne6K16288FpsGANq8Lvn185GW6f-Wu4LRi_rQE8N8B6OCsEPlg3ZwBTEjefPvYbKtdwqoVRaxflZkPmNHO34_DPuG8o9vMmlZ1ias0ds_I9YSZAEChrOz77gUVSwf5MBuDyfTx7imUeG4RYU_gN44bcHYomT5YFgjZZ8XLQJpSebloKmdgH8o7_GgzSzkPZERfn-AeMo50PNvvkXOFUkFpbJJV20EjPhxViJZ3fVON6sKZ8qKwVEQN9M_FvZAHkUlIVPiTX1m82L7P0OqKRcLFybzWnxMyJH55dlvWqRLNiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حمله موشکی حوثی های یمن به پالایشگاه جازان شرکت آرامکو
عربستان
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68977" target="_blank">📅 12:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68976">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISi9dsDZZt81rQCnbKrJZfMKI_yeYyJHf5fGP1MSPEAQampipJ1uEq6JKDSmjkAl3pikbhnUfyJJHqGdLH-8DgX9lROy3UtBC4EUejluLmrCGjPHkX3dmfI-wjo4ezr1Rg9p94JhhCynCNutKGGLwnMNXHw6iiL5VKw-ftaZ5WMMeEESPQcfmFuDW655AQJnbdwAmTyOWCjFlzip_Y4oflb_VEZVNbXlwWoz3GucVfxebBYhTDzQLEwwJoJEi0WD9kRRP9THaa2pNABnnylspCVzT3OCcM-H3zsJ20ZlY16g3CrztsN_hiR9m8D0r6Y7BAByNWdv52bttpCk6Z_IPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
سازمان عملیات تجارت دریایی بریتانیا گزارشی مبنی بر وقوع حادثه‌ای مربوط به یک نفتکش و نیروهای نظامی در خلیج عمان دریافت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68976" target="_blank">📅 12:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68975">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=JSM5CBBIUNRkUj7dAumIM1ewqdlipRxzWWLqIVVL0RdURGutftkWy0YtipoEygWgJeDRFxLu2khyFBMV1QMaa3sMO9TzmMko2fsdtMCMFauyEh6ttLMQtx1Wmoc_hCLy8R4ZDUqAaH6tC_eqqYs6_6c5YwR2BOLmjiCM29shUuD9t5VOvUcUW_KeKDvjtanm6cAf8higyoXZYiXAsAQmC-fLwkKTgKeNdkbFGjn3OPa5u36Oy0ss2nuDBnw_W0drS9XPrpqyrpKfX7qOrnAlw10wIPQHGQOxrwuPFX9EJSgrd4ZTaVlL1x7_kgIKac2KUGNn9MsfygpptYc7AmzcMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=JSM5CBBIUNRkUj7dAumIM1ewqdlipRxzWWLqIVVL0RdURGutftkWy0YtipoEygWgJeDRFxLu2khyFBMV1QMaa3sMO9TzmMko2fsdtMCMFauyEh6ttLMQtx1Wmoc_hCLy8R4ZDUqAaH6tC_eqqYs6_6c5YwR2BOLmjiCM29shUuD9t5VOvUcUW_KeKDvjtanm6cAf8higyoXZYiXAsAQmC-fLwkKTgKeNdkbFGjn3OPa5u36Oy0ss2nuDBnw_W0drS9XPrpqyrpKfX7qOrnAlw10wIPQHGQOxrwuPFX9EJSgrd4ZTaVlL1x7_kgIKac2KUGNn9MsfygpptYc7AmzcMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
مجتبی خامنه ای چندماهه رهبر شده ولی حتی کسی صداشم نشنیده. اون حتی به مراسم تشییع پدرش نیومد. خیلیا هم معتقد هستن که اون مرده. نظر تو چیه؟
🇮🇱
نتانیاهو:
حرفات درسته ولی طبق ارزیابی ما اون زنده هست
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68975" target="_blank">📅 11:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68974">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">💢
ویدیو وایرال شده، پشم‌ریزون از گات تلنت
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68974" target="_blank">📅 11:15 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
