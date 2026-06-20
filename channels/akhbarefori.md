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
<img src="https://cdn4.telesco.pe/file/F64n2Ox_ZfqP2x1r_7p9hd8wQjQYsxt7wwfqWgfEKEW5LQ_9bOc9J_WSfkKEtALS1bVcw-FZiJ1OzDmxPUc_4tW9AkXnfBKvVP7t5a1-r0BGlxDicnhVelQ995_EnBdtJboAc8LvJ5IssDxtUdC7ZKMscsWht0h1XWMUuiUCIaPG2PwliKYJrRURSiA7tjn5vUTo_96iMrzWz02dEmsJIBRLL_J8ddYIYaVpjJ1R3-Arhkr4wiwb9dfJaHsitLucyWhvdDuVWY8NXr3EYhoXr9FIeKG6X0hB78Td-29VUw-Y3v9usvgOBdYwUUP352teABDs1ksUTbyq-WFLYi0myg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.43M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 03:11:38</div>
<hr>

<div class="tg-post" id="msg-661606">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4gtYktGezqLUWweU71rfyRCZHMzECgNaej0e5pxY6R-_qsFbNZfNDiNYiKE2uwpIlXZzZRSB5ZitDnsbHJ7OoLc8DQCBvZGtDm2z2xOJEQKVcvzu-1ns7qoImizr8RNnWTGfW1qN4PykrOQodlDJav4Vu4I0-yvu4vw2mwn-TWhtNvkjXpoEp8OKFLk8_CM8xojXKOGMCIoa4awn1PsD3ZOi1yDNNrwldcJpOC3JnAAfdVLdGA_iib_LWHVYY9i2DqLrxXoSKSLtzlbK7ZUCJ-q5yxHV_WfLZBl0xtZli7Nl6tDyALXhh3l9Y050eNsKDUv1I-dP-d1Y0gLHTn0sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💙
۷ روز ویزیت تلفنی رایگان
توسط متخصصان
اورولوژی و نورولوژی
، هدیه ایزی‌لایف به مناسبت هفته جهانی بی‌اختیاری ادرار است.
🗓
۲۵ تا ۳۱ خردادماه
🔖
کد تخفیف: easylife100
❗️
اگر مبتلا به این عارضه هستید یا وظیفه مراقبت از اشخاص دارای بی‌اختیاری ادرار را بر عهده دارید، برای مشاهده لیست پزشکان و رزرو نوبت رایگان وارد
لینک زیر
شوید.
👇
👇
👇
👇
📎
https://B2n.ir/ue2237</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/661606" target="_blank">📅 01:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661605">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🎓
فرزند شما فقط برای امتحان آماده می‌شود یا برای آینده؟
🌟
دبیرستان دخترانه هوشمند مدبّران (بارسا)
🏫
✨
در مدبّران، دانش‌آموزان علاوه بر موفقیت تحصیلی، مهارت‌های زندگی، اعتمادبه‌نفس ، تفکر خلاق و آمادگی برای دنیای آینده را نیز می‌آموزند.
🚨
ثبت‌نام آزمون ورودی آغاز شد
🚀
📩
برای دریافت اطلاعات و ثبت‌نام:
🆔
@Modaberane_Barsa
📩
یا عدد ۴۱ را به سامانه پیامکی
3000909030
ارسال کنید.
📲
❗️
آشنایی با روش‌های نوین آموزش و موفقیت تحصیلی
👇
🆔
@barsaschools
📍
تهران</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/661605" target="_blank">📅 00:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661604">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeHfSyjAFamUSeAE_Fxq8qpZqXYUd0X-l0z1ohJIE0BdlzsG950jc-LUhgXU2X52oNTfgE2iPc_xxIi6J5-K4nHBJ4zIpoyK0bRhqdBE7zokHiXu3pM6ELqPeckhCAY75qmN3ofDKyPT30LODKbQ7BvPPVtxZDsCkdZROvUtZKmJ04BoSweSpVeNsq_IQC4h1LF1KiPHwGqQDfQ49_rau8pdykBDdL6mX3xWBXokSwsxTbdixMUmI9y6yMrj6_94SJ4xaCPxLNaF3K3VSF9b1EZwfgzR4xlObwlu-WRVlhbQGJ9Xb1F5gFAUJPO5kWuzNLibNKu9lleZAsnv75PxPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف در بدو ورود به زوریخ: کودکان مظلوم میناب و تمام شهدای ایران عزیز را هر لحظه ناظر اعمال و رفتار خود می‌دانم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/661604" target="_blank">📅 00:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661603">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
بی‌بی‌سی‌: استارمر، نخست وزیر بریتانیا دوشنبه استعفا می‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/661603" target="_blank">📅 00:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661602">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7ff94695b.mp4?token=Fm-2vywR7oL7xyvVpMu3HnzuKr3Ag4wefEea_dnzBPeowQ0Y-LFU1kAP--XlLVphgrWlXc2ynBHM9gwrIJyt_jArvk8sTEtLEfFt3l1a-GYNkGfZZwc2cqHg6rQojruCexEFDOpcQQnXvggsfhQ89-KdLNKQMQ6bpVD3t7fDCbg0rQ6Z9aT8OMWr1sqlWhWxdXMIfSuaSXCO6Rw5zw7bOx8zzInidSZZEZp1bKMbB3CIB5S60vkcKraWcu1qJCnRbtxyF2hhglGaxlme7akoXBADE6gj9EBUvvWG3sN8Glkxdo3qMx7i1u3Pr-bXjYUue4j25DuUqqf9qJsVeHhWLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7ff94695b.mp4?token=Fm-2vywR7oL7xyvVpMu3HnzuKr3Ag4wefEea_dnzBPeowQ0Y-LFU1kAP--XlLVphgrWlXc2ynBHM9gwrIJyt_jArvk8sTEtLEfFt3l1a-GYNkGfZZwc2cqHg6rQojruCexEFDOpcQQnXvggsfhQ89-KdLNKQMQ6bpVD3t7fDCbg0rQ6Z9aT8OMWr1sqlWhWxdXMIfSuaSXCO6Rw5zw7bOx8zzInidSZZEZp1bKMbB3CIB5S60vkcKraWcu1qJCnRbtxyF2hhglGaxlme7akoXBADE6gj9EBUvvWG3sN8Glkxdo3qMx7i1u3Pr-bXjYUue4j25DuUqqf9qJsVeHhWLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاروان تیم ملی فوتبال به هتل محل اقامت خود در لس‌آنجلس رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/661602" target="_blank">📅 00:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661601">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
معاون ترامپ عازم سوئیس شد
🔹
جی دی ونس برای حضور در مذاکرات با ایران عازم سوئیس شد.
🔹
او به خبرنگاران گفت: امیدوارم بتوانیم پیشرفتی در مذاکرات داشته باشیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/661601" target="_blank">📅 00:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661600">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c337d72de.mp4?token=BFrz1zJQQ1jTM62e9XOnWw__9d0_4GX2_glUjvjyeItRowbWUxYT2-VOTfqYg-H_G1Ve5uJsV36MMDR_LpHEcNSHktN3LocH-Fzd59BLGll8QBkf5vpzNPy6AA1e1GQL7cvT83NRUfc_iliEyN8lWA2O35uLMVzm6pMmMNHhhA_0uB3qDL7qLPn_LHKsTsJqRm2yzkxnEH8k8ksLmDL04NqMyODR6cJU-uy2BaZlK6pMjB0H5neZiuBVH5_Be88klM-4ufpvZgbP61UedQPNnfhmU_n-96jtyb9Ce8mn2l08_hu0itNhoY4KGLTFRrtWcO7EHYde7mfHtecySWu9ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c337d72de.mp4?token=BFrz1zJQQ1jTM62e9XOnWw__9d0_4GX2_glUjvjyeItRowbWUxYT2-VOTfqYg-H_G1Ve5uJsV36MMDR_LpHEcNSHktN3LocH-Fzd59BLGll8QBkf5vpzNPy6AA1e1GQL7cvT83NRUfc_iliEyN8lWA2O35uLMVzm6pMmMNHhhA_0uB3qDL7qLPn_LHKsTsJqRm2yzkxnEH8k8ksLmDL04NqMyODR6cJU-uy2BaZlK6pMjB0H5neZiuBVH5_Be88klM-4ufpvZgbP61UedQPNnfhmU_n-96jtyb9Ce8mn2l08_hu0itNhoY4KGLTFRrtWcO7EHYde7mfHtecySWu9ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون ترامپ عازم سوئیس شد
🔹
جی دی ونس برای حضور در مذاکرات با ایران عازم سوئیس شد.
🔹
او به خبرنگاران گفت: امیدوارم بتوانیم پیشرفتی در مذاکرات داشته باشیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/661600" target="_blank">📅 00:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661599">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81bc4db8d9.mp4?token=RmX-5FfPPEvTnoLDkhN0IFQNQXUPAnWkNkJbDmJacnpUkxVrXAhcx0M7wbmddrak-IfUUS-6QefkLR0fKTrL6SqrTcXg8pCDxBoSpoMXY2tXinvQ8Ztwy_qHEfggHJ_11-Gj7_ptqOHisaS1e8Y5Un9T9EZV1ytOP3828g2Nvn7iwGHI2qMWMCdhXcpnL0QwU48J1AQpZfc6_zWAbBYedlep869PQzPJXtuwup5VpkKXf5VnWCdza5f41CfC_ng31M75tyu37ZrAfYib7Hc_SgfOzPJwQX5nHsc1ubhm0CRYIfG6ZF5IMuya1Ej1IdPVkBV-ZoRfuF1A6kE0h6NnyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81bc4db8d9.mp4?token=RmX-5FfPPEvTnoLDkhN0IFQNQXUPAnWkNkJbDmJacnpUkxVrXAhcx0M7wbmddrak-IfUUS-6QefkLR0fKTrL6SqrTcXg8pCDxBoSpoMXY2tXinvQ8Ztwy_qHEfggHJ_11-Gj7_ptqOHisaS1e8Y5Un9T9EZV1ytOP3828g2Nvn7iwGHI2qMWMCdhXcpnL0QwU48J1AQpZfc6_zWAbBYedlep869PQzPJXtuwup5VpkKXf5VnWCdza5f41CfC_ng31M75tyu37ZrAfYib7Hc_SgfOzPJwQX5nHsc1ubhm0CRYIfG6ZF5IMuya1Ej1IdPVkBV-ZoRfuF1A6kE0h6NnyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهردار نیویورک آیپک را «هیولا» توصیف کرد؛ «آن‌ها میلیون‌ها دلار پول‌های پنهان را صرف  حفظ قدرت خود می‌کنند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/661599" target="_blank">📅 00:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661598">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
ونس هنگام عزیمت به سوئیس: امیدواریم در مسئلهٔ آتش‌بس در لبنان و هسته‌ای پیشرفت حاصل کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/661598" target="_blank">📅 00:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661597">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc0bba0bd1.mp4?token=ieadhPNuRn6_JFJyDGDmcAvdXJ95ldjUpQeTjLQgk9omB1bHc3QE3FyXvRPcO5bBLMhtmin5BcEJGp6_p7lKs_MaugX3hB1jqIGy40glxvxDH2eQEPkdl-cz6aTf0Pcr7LflR2IX6QOjjjajd_AMNImpoyCBdVAYl8Qo_EJJ71Dia3X1WzNDxPQjye5aE9Mkf6A8I5xzla5ZDFGEHTgv8DP3qtjlFrJ2vxuPCON8xv8pKuEYp5BYaF4CJyCceY0SoDZaZn6UZAEU_H84oNew_5LY9ZFpFIYdPR3P1nD3zXvw5GlsuxE0ZHyRP6SGWuP03qR5VG27qGRqGqPUmmJ9Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc0bba0bd1.mp4?token=ieadhPNuRn6_JFJyDGDmcAvdXJ95ldjUpQeTjLQgk9omB1bHc3QE3FyXvRPcO5bBLMhtmin5BcEJGp6_p7lKs_MaugX3hB1jqIGy40glxvxDH2eQEPkdl-cz6aTf0Pcr7LflR2IX6QOjjjajd_AMNImpoyCBdVAYl8Qo_EJJ71Dia3X1WzNDxPQjye5aE9Mkf6A8I5xzla5ZDFGEHTgv8DP3qtjlFrJ2vxuPCON8xv8pKuEYp5BYaF4CJyCceY0SoDZaZn6UZAEU_H84oNew_5LY9ZFpFIYdPR3P1nD3zXvw5GlsuxE0ZHyRP6SGWuP03qR5VG27qGRqGqPUmmJ9Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هیئت مذاکره‌کننده ایران، با اسم میناب ۱۶۸، وارد زوریخ سوئیس شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/661597" target="_blank">📅 00:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661596">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hM5kjLfMKCPC_mgRY89_EOvYZ4nli1M67HIlE9EzKFJI5rUarrJG69mbFLb8qnWj5NJl6HCSQNXkpJP0tR_FTeh8jj1FwLKxY08atV-mS6_SCTu5x-5ymuDwnif1N1vX_arqClP2UEHht0qg9Fx_M8V03JhCvDFsqVIJDagokpE5vVng7oN7YOMmnX7770lvPOY3PVKvcBu4Jmo1hut8RpBIp1EB_05P3ikVT-DXB5pN4aKk8ZD80q5QBt-bk7Hr9mFOFkdQeYfgod4jKIKBbKx0wwsvpE3TYhzK8XkzJF6sSidDO0vMLWXfg7hjiyp42Uw3vD7-016pbWsbPBSczA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/akhbarefori/661596" target="_blank">📅 00:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661594">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73197ae8c4.mp4?token=FAehR-0S4lFvN2Uhf4mf3FIqDu0txNdTvIbsOGQhOOhcmPb3pfH9nKYlLYWpqRC6wP4O4oOqbSpd4AOj_-jS1zqiEj7f-S3DUVEoIC8gsMkXECYUBPUKY4N4VmQ6BDFNonS-bxAGtMINAeu2Rx2RhXC3oG6CBrTwWUPp33ZOzhCUmctrME-_YDZlarcYt-Ftlfqfi8_n_jDV3Ctti9VM4EYwP-lswbgrXmM2pKZAUH4Li182yh3U3LgxSQc7PivlkAvw4Gt-VkbJ3jfEBd6pGBwoC2Bryv6eq1_ic4PWM7L7vFz7B86KiYiGhcOWAIsTzORyYSdiioCwUfxJsPxtVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73197ae8c4.mp4?token=FAehR-0S4lFvN2Uhf4mf3FIqDu0txNdTvIbsOGQhOOhcmPb3pfH9nKYlLYWpqRC6wP4O4oOqbSpd4AOj_-jS1zqiEj7f-S3DUVEoIC8gsMkXECYUBPUKY4N4VmQ6BDFNonS-bxAGtMINAeu2Rx2RhXC3oG6CBrTwWUPp33ZOzhCUmctrME-_YDZlarcYt-Ftlfqfi8_n_jDV3Ctti9VM4EYwP-lswbgrXmM2pKZAUH4Li182yh3U3LgxSQc7PivlkAvw4Gt-VkbJ3jfEBd6pGBwoC2Bryv6eq1_ic4PWM7L7vFz7B86KiYiGhcOWAIsTzORyYSdiioCwUfxJsPxtVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل اول ساحل عاج به آلمان توسط کسیه
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/661594" target="_blank">📅 00:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661593">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
بدرقه ملی‌پوشان در مسیر سفر به لس آنجلس برای بازی مقابل بلژیک #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/661593" target="_blank">📅 00:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661592">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjGmqV_CjtRErOH3jNReD1G42gQ7IjEO9gQPrZ8W931RY9lWPG46uw4FHsOaDdWq6nPxWL1Iz_hVWio_NSekVzRvPPHmtz1cbgCxkuyiR0E-YPoBQ37G-ag1ODHqVx0p9ZZOnFOSrXXA4EKBNbw7WyxtMqmKpYHmmHzic9Vdy5LCKzHSiBEH8BPghWbUy1bGuB1k34foJtamEdP6ssXVa4pZ8MpfXstH_RdkR9udimCFtlDTr6NQRITUqgcaXI8dqEd1gsFvUkLecn4tME26Ezv5aSU8CYzWBqNPPLqhtyyFcf3rSjg7xu69rcw9TarPjD1bFCILFMDbaRR7bFkcLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه از سر رفع تکلیف؛ بلکه کاملا اصولی و روی خط استراتژیِ از قبل تعریف شده!
هم‌زمان با شروع بیست و سومین دوره‌ی جام‌جهانی فوتبال، فیلیمو برای دومین بار لوگوی خود را بر اساس کی‌ویژوال‌های مرتبط با جام، به‌صورت داینامیک تغییر داد.
اوایل دی ماه ۱۴۰۴ بود که در بیانیه‌ی رسمی فیلیمو اعلام شد، هویت بصری برند جدید، به‌خصوص لوگوی فیلیمو به‌صورت داینامیک خواهد بود و برخلاف بسیاری از فعالیت‌های مارکتینگی برندهای ایرانی که اکثرا از سر رفع تکلیف وارد فعالیت در این نوع حوزه‌ها می‌شوند، فیلیمو گام جدی دیگری برای پیشگام‌شدن در این حوزه‌ از فعالیت‌ها درمیان برندهای ایرانی برداشت.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/661592" target="_blank">📅 00:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661590">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KFDsLEs2dn-cDy1vojsT3fZSFaos9LlaTzUc9MIv3vOo3qJgdBm2m6lyu-sLpWnfjHgkmo4wYPTFglZTaQi4_RjzL2nI7ijav1gWtwLke8Oo88fTZSYmTjM-ygeTNoa8WXKoNJifuqha6gFYVtYrC16tRnq6sXJ9MSIq-PfaDtOBDb9fT3515udVJ1imzHqfQ2UQiUJmv4gJXHV0gfTb9u1OeiNsTzsWv-vfFdNlr3KV3IQp5ibFwPt6X9E2xKEyIku7OLWl-L8IAU1fYhwS60EmvtFtGYHNCGmo-fCFWgULhgukJFMUlVRqpo8bcL1wTSjvSunZeDGWhmGX94o0SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AC9WipnDGmETtneEnCqymdXzQmiAdhwVSmRVviCD57EemGJooL2b0TTYOWnYSAkA572LD9KsuF3glPIG-l7M8M7HzoMMmtDHewDpY_XKyd1xh5iWbIlir4k7OAw4GJvhDYi4--_N6cInZQHzNa3IBleir0pPm2o39PrqESbDIy3ED6WbfYB4oOaBPBd0V5oI0e6Keu-r_xsXsAlghRdVu7xanDzpR0SBy5YjhiruTAzxAFkZ-mr-sSNFUZc8_4LREFHuz-grt5WZDYiVez2W7823uTcRFgg8wn0ikram9oITsJhSJ7DS_PDMwJ2tvS35fa1DD-J7a7IK2V7yYoBLpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصویر دیدنی از زائر کوچک رواق کشوردوست در کنار تصویر نوه رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/661590" target="_blank">📅 23:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661589">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/128e650d65.mp4?token=u0ZlIH76pEIyVTrypsGbnq8hHy1Hn6Prj9rlZ4ZBO8AIBuZP_wNwahyQCh1VeFTvZc0aBJC6qzToIAhPZcFowuEqz1a2gtnPPBxsNPUEEykh76Ja85VBPH4UKANZMAvlNGVAlESQYB8LEQCxkZgGeDqMKzwNFIfaKHQ2VtX3iTB1oK7Bh07qV2p7kHjVR2Cg38FdTxKPaSw8RYLnBSHu6EFAtaqTl6E7gs9v3D_ItuO6ZH-MqruRB5_p0f-N6_y7gUSPopgPH0HI256-R8M04ZzWB7adzoTyfaR6yJ7QFfR3qfMuttkI-lzMfy8vYUI7CK1H3qx4Z4rxRWECdv8h9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/128e650d65.mp4?token=u0ZlIH76pEIyVTrypsGbnq8hHy1Hn6Prj9rlZ4ZBO8AIBuZP_wNwahyQCh1VeFTvZc0aBJC6qzToIAhPZcFowuEqz1a2gtnPPBxsNPUEEykh76Ja85VBPH4UKANZMAvlNGVAlESQYB8LEQCxkZgGeDqMKzwNFIfaKHQ2VtX3iTB1oK7Bh07qV2p7kHjVR2Cg38FdTxKPaSw8RYLnBSHu6EFAtaqTl6E7gs9v3D_ItuO6ZH-MqruRB5_p0f-N6_y7gUSPopgPH0HI256-R8M04ZzWB7adzoTyfaR6yJ7QFfR3qfMuttkI-lzMfy8vYUI7CK1H3qx4Z4rxRWECdv8h9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار مستقر در لبنان: حمله موشکی هدفمند و متمرکز در جنگ ۱۲ روزه دشمن را وادار به درخواست آتش‌بس کرد/ آتش‌بس های دروغین هیچ ارزشی ندارد و مقاومت، آزادی عمل دشمن را نمی‌پذیرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/661589" target="_blank">📅 23:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661588">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3943689543.mp4?token=NlVFrLI_8aXYQ9LEpCMgEvjkAlBBfZDS8EMor_sDlWP4K2Ww2xPJO1ZYq3RHveKqWbFrk_6xx6KjUXI4GnrBJ_Dj9BpuNvcFduez0YorvsCN5XvjrWcsvsJzQwLKPUVIRZsApOnNKZ1ECpJzY2zLB7QOpITIs6FyLTjT02UZTMDWBpiVzvqvV9yYM-owKNsoZpc7ToFfKhHy4yDUFFwNTHc2KKR7vJYrS-PKN3ldVMMK06kNzihV5ls99SA4vFdKOmFX61We49EN75-KG-uXYv0OfSs8E3knQ7m0FkS5Xg_cBEkaRnEvLp4ffsFK1YsR8Oewz04g24t7ew8bo_Xrug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3943689543.mp4?token=NlVFrLI_8aXYQ9LEpCMgEvjkAlBBfZDS8EMor_sDlWP4K2Ww2xPJO1ZYq3RHveKqWbFrk_6xx6KjUXI4GnrBJ_Dj9BpuNvcFduez0YorvsCN5XvjrWcsvsJzQwLKPUVIRZsApOnNKZ1ECpJzY2zLB7QOpITIs6FyLTjT02UZTMDWBpiVzvqvV9yYM-owKNsoZpc7ToFfKhHy4yDUFFwNTHc2KKR7vJYrS-PKN3ldVMMK06kNzihV5ls99SA4vFdKOmFX61We49EN75-KG-uXYv0OfSs8E3knQ7m0FkS5Xg_cBEkaRnEvLp4ffsFK1YsR8Oewz04g24t7ew8bo_Xrug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار مستقر در لبنان: ساعاتی قبل عملیات نظامی از سوی رژیم‌صهیونسیتی متوقف شده است/ دشمن قصد دارد دستاوردهای حاج‌قاسم و حسن‌نصرالله را در لبنان بگیرد و کسی به او شلیکی نکند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/661588" target="_blank">📅 23:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661587">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
بدرقه ملی‌پوشان در مسیر سفر به لس آنجلس برای بازی مقابل بلژیک
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/661587" target="_blank">📅 23:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661586">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
تعطیلی اقامتگاه مجلل محل برگزاری مذاکرات ایران و آمریکا
سی‌بی‌اس:
🔹
اقامتگاه بورگن‌استوک در سوئیس، مکانی‌ که مذاکرات  ایران و آمریکا روز یکشنبه برگزار می‌شود، تا سه‌شنبه به روی عموم بسته خواهد ماند.
🔹
این اقامتگاه مجلل مشرف به دریاچه لوسرن و کوه‌های آلپ سوئیس از ۱۷ ژوئن (چهارشنبه ۲۷ خرداد) تعطیل بوده است و قرار است از ظهر چهارشنبه فعالیت عادی خود را از سر بگیرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/661586" target="_blank">📅 23:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661585">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
خبرنگار العربیه: کارشناسانی در سفر ونس به سوئیس او را همراهی می‌کنن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/661585" target="_blank">📅 23:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661584">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/927b09cb39.mp4?token=qS0neilvE4ReZBTGyfvN6Kxie4LANlV2fPEzGsynGvaAaYC2ot1cRbL9JewMhaXSfxNs7r3D8i0N2wcM3QXFUH1V4pj2J03Ef3bJYQW_PrV4rKpA4OouZWwdLYh0FvC_BeqUiZN83fr9edSqQZpZH-4-LRgW_Dqn4wgVMia7wluVawkGfF4vx8xNjN7AHl3X_w6F_l5WblvEq2ReAlHFygmJduptGMb4yRxeaNG_KDvwBIRmMY2W6ZeidJ5uicctQUCKezIllOxqjUV-gYVgCA3jZ0-4XH6TqcGmbHCBqIQqDtZ3BVHq51Ij1w9E7Q43FsY_y-Bp3RLNE4D5Ysj0LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/927b09cb39.mp4?token=qS0neilvE4ReZBTGyfvN6Kxie4LANlV2fPEzGsynGvaAaYC2ot1cRbL9JewMhaXSfxNs7r3D8i0N2wcM3QXFUH1V4pj2J03Ef3bJYQW_PrV4rKpA4OouZWwdLYh0FvC_BeqUiZN83fr9edSqQZpZH-4-LRgW_Dqn4wgVMia7wluVawkGfF4vx8xNjN7AHl3X_w6F_l5WblvEq2ReAlHFygmJduptGMb4yRxeaNG_KDvwBIRmMY2W6ZeidJ5uicctQUCKezIllOxqjUV-gYVgCA3jZ0-4XH6TqcGmbHCBqIQqDtZ3BVHq51Ij1w9E7Q43FsY_y-Bp3RLNE4D5Ysj0LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار مستقر در لبنان: رژیم‌صهیونسیتی پس از آغاز تفاهم میان ایران و امریکا، بیش از ۳۰۰ بمباران در لبنان انجام داده است/آمار اولیه ۲۰۰ شهید و زخمی در این دو روز است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/661584" target="_blank">📅 23:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661583">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
وزیر جهاد کشاورزی: تا امروز که نزدیک چهار ماه از جنگ می‌گذرد، هنوز یک کیلوگرم هم از نهاده‌های دامی و ذخایر استفاده نکرده‌ایم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/661583" target="_blank">📅 23:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661582">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c40a0a59d3.mp4?token=cWEsPThsZwySigyv3AY6mlY-pMeYzHa93QpXAOrYYEc1ptFHOUJetzTi27gYCexCAbQ7DPt5D4RshbGXSaMo5vqBN1BgGaLaTDD1kItAK51TWAK0Ez-uv5ZsnWbQjwT-UXvdjz95nmEFvfrhA-LMkACxRxKwc9N4h2Cn503C8pEVEHtKJJIvmqdoTcm1PsBDXutnKRfVU65-SA__-3x6l-OF40v7XLKkZkj-YEvCrkDJnYe4ntYgUGnHxg4RF7NnHPW2ZEeaBZooe2ruVoDH1dYX4OzUmIlEj4RWGS5jufke5CDMAJqpjY70DInPfEGrrUj0fKDkRxM9XGrH-I3o5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c40a0a59d3.mp4?token=cWEsPThsZwySigyv3AY6mlY-pMeYzHa93QpXAOrYYEc1ptFHOUJetzTi27gYCexCAbQ7DPt5D4RshbGXSaMo5vqBN1BgGaLaTDD1kItAK51TWAK0Ez-uv5ZsnWbQjwT-UXvdjz95nmEFvfrhA-LMkACxRxKwc9N4h2Cn503C8pEVEHtKJJIvmqdoTcm1PsBDXutnKRfVU65-SA__-3x6l-OF40v7XLKkZkj-YEvCrkDJnYe4ntYgUGnHxg4RF7NnHPW2ZEeaBZooe2ruVoDH1dYX4OzUmIlEj4RWGS5jufke5CDMAJqpjY70DInPfEGrrUj0fKDkRxM9XGrH-I3o5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات تند سناتور آمریکایی علیه ترامپ و جنگ با ایران
سناتور جان آساف درباره جنگ ایران:
🔹
این یک فاجعه برای سیاست خارجی آمریکا، برای اقتصاد آمریکا، برای امنیت ملی آمریکا و برای ریاست‌جمهوری ترامپ است.
🔹
منظورم این است که، مردم عزیز، یادتان باشد که در روز اول این جنگ، دونالد ترامپ به ما اطمینان داد که اوضاع از برنامه جلوتر است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661582" target="_blank">📅 23:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661581">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
قلعه‌نویی: در جام جهانی جا برای اشتباه نیست
🔹
می‌خواهیم کاری کنیم که ستاره‌های قبلی نکردند
🔹
بازیکنان ما مصمم هستند که به دور بعد صعود کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/661581" target="_blank">📅 23:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661580">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
چرا کالاهای اساسی گران شد؟
وزیر کشاورزی:
🔹
یکی از علت‌های گرانی، اصلاح ارز ترجیحی است.
🔹
موضوع دیگر شرایط جنگی است که در جهان باعث افزایش قیمت حمل‌ونقل و بسته‌بندی شده.
🔹
افزایش ۶۰ درصدی حقوق کارگران نیز علت دیگر افزایش قیمت کالاهاست.
🔹
قیمت حمل‌ونقل رانندگان داخلی نیز ۹۰ درصد افزایش یافته است.
🔹
مالیات بر ارزش افزودهٔ کالاهای اساسی از امسال ۱۱ درصد شده است.
🔹
حقوق گمرکی کالاهای اساسی هم قبلا یک درصد بود اما امسال ۵ درصد شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/661580" target="_blank">📅 23:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661579">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
ونس: ما به مذاکرات ایران فرصتی خواهیم داد
🔹
جی. دی. ونس، معاون رئیس جمهور آمریکا، گفت که مطمئن است واشنگتن می‌تواند آتش‌بس را حفظ کند
🔹
او تأکید کرد آنچه دونالد ترامپ، رئیس جمهور آمریکا، برخلاف برخی از احزاب در دولت اسرائیل، گفت این است که واشنگتن به مذاکرات فرصتی خواهد داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/661579" target="_blank">📅 23:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661578">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b50b28ca66.mp4?token=ieQwGCY2H-L1DzcWwg6AfqLhIEIg-GsDUXWslGSvGUy4nXS9IGw9cdXi5xG-Y5NtWaEx0bF8MyOPZ9z5CKzj5bmA4Rr_agLVm-TjPQqcnYD4wZDHe2n9m9UhceM12oO7yMysxhWWdk5pc7XC2FC11mED6ZbVaDHmeVyhVLfSFcYd3H5F8ihnWQUAp7KOVtb0qscm0m8OvQgh_BQ2M49UlZY6moukseSklTHbqQgkuIa_DOSUohEnJfTk7bNnMU7Lybvfsw2RZCrnj6zGXb-UdfXCZBL8k0ZS9cQaiYRBgyArPar6P7t16x4gIrHP6OXROIvgKSVox1GiMMb2z-BoBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b50b28ca66.mp4?token=ieQwGCY2H-L1DzcWwg6AfqLhIEIg-GsDUXWslGSvGUy4nXS9IGw9cdXi5xG-Y5NtWaEx0bF8MyOPZ9z5CKzj5bmA4Rr_agLVm-TjPQqcnYD4wZDHe2n9m9UhceM12oO7yMysxhWWdk5pc7XC2FC11mED6ZbVaDHmeVyhVLfSFcYd3H5F8ihnWQUAp7KOVtb0qscm0m8OvQgh_BQ2M49UlZY6moukseSklTHbqQgkuIa_DOSUohEnJfTk7bNnMU7Lybvfsw2RZCrnj6zGXb-UdfXCZBL8k0ZS9cQaiYRBgyArPar6P7t16x4gIrHP6OXROIvgKSVox1GiMMb2z-BoBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیراندازی از داخل خودرو به جمعیت در شیکاگوی آمریکا
🔹
پلیس شیکاگو اعلام کرد که دستکم ۱۲ نفر در یکی از خیابان‌های شیکاگو، پرجمعیت‌ترین شهر ایالت ایلینوی  در آمریکا پس از توقف یک خودروی شاسی بلند و تیراندازی ۲ نفر داخل آن زخمی شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/661578" target="_blank">📅 23:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661577">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
حزب‌الله ادعای صهیونیست‌ها را تکذیب کرد
‌
الجزیره:
🔹
روابط عمومی حزب‌الله اعلام کرد ادعای اسرائیل مبنی بر محاصره مجاهدان مقاومت در بلندی‌های علی الطاهر صحت ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/661577" target="_blank">📅 23:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661576">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/071d4a05d0.mp4?token=slgbOOqSFglVJzvKL5uKdjt-rDYk0FMrDpAnaLOp8ax-sd-jWYBCwV5JlXYusAvRKvaaDzbEgnKBJzuvIKwRaXZe83Rz4BwZDf23KyR35q3b8QB2eYOfSC24f49GWGQ2_fCFg3vG-6nlLVvp09VTX4YjcqFKkmZWziw6mfqkoVb4xrq8Weqcf1aQ5QKfM92FJTwMIvw8YHP2utJKQosj1otUa1-5RttXR5hAA_38nL63d9ChkY3b4Zqc9z2eGPbr4-S9MxJ1jbYJoa-vR1k7Q1VfgYYXX8BjkfVABurp315AZBzuHmkuKOWCYyhmKs67nbiXlFWQgpuNgwA6TbAvYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/071d4a05d0.mp4?token=slgbOOqSFglVJzvKL5uKdjt-rDYk0FMrDpAnaLOp8ax-sd-jWYBCwV5JlXYusAvRKvaaDzbEgnKBJzuvIKwRaXZe83Rz4BwZDf23KyR35q3b8QB2eYOfSC24f49GWGQ2_fCFg3vG-6nlLVvp09VTX4YjcqFKkmZWziw6mfqkoVb4xrq8Weqcf1aQ5QKfM92FJTwMIvw8YHP2utJKQosj1otUa1-5RttXR5hAA_38nL63d9ChkY3b4Zqc9z2eGPbr4-S9MxJ1jbYJoa-vR1k7Q1VfgYYXX8BjkfVABurp315AZBzuHmkuKOWCYyhmKs67nbiXlFWQgpuNgwA6TbAvYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توافق ایران و آمریکا به معنای پایان تلاش برای تغییر رژیم است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/661576" target="_blank">📅 23:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661575">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/le9ZJsYs-bUCLOyAY4caiaLL_7kui_8Pcx3vQj_Oml0XrReG_7oJuSHUqeSjzo3fOSHgfg_U2sb62XyHQ6Zd84OjjCgJ5PBB5XBcFe8ppxs1n18jwtWlVNQTFLc78jgT14SUZsqFr9RAfvHf3yZx4weZVwKft53wIlFCIkQFx8Vhysx2gW1YAh1lirCyRmgbwYsMWAEWbfYpMSUCBK6g82ybYxGWQNMjdjCOh07TjAEtRBeIV-C6sN4ZSa95VCWfam3Qya7qvrQHOFLwg0x0_vHiV7Bo0CuzvGrQF9Kwf31mI4wtaRJx2viPYDNxEveMVfRETpR6D1AfRzizbgmdtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اگر توافق نشود، آمریکا در تنگه هرمز عوارض خواهد گرفت
دونالد ترامپ:
🔹
در طول دوره آتش‌بس به مدت ۶۰ روز، هیچ عوارضی در تنگه هرمز وجود نخواهد داشت و پس از انقضای دوره ۶۰ روزه نیز هیچ عوارضی وجود نخواهد داشت، مگر اینکه در صورت عدم تکمیل توافق، توسط ایالات متحده آمریکا و برای ایالات متحده، به دلیل خدماتی که به عنوان فرشته نگهبان به کشورهای خاورمیانه ارائه داده است، به منظور بازپرداخت هزینه‌های گذشته، حال و آینده، اعمال شود.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/661575" target="_blank">📅 23:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661574">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a195dc3a1f.mp4?token=d0cIllN93GpHTlUXaOSM_1FDdq_s8gf91kTDEnhFq2ZBd08Pzw702zGrYpp_D6Zs9e12DQtcrVGu8cbHROQcwiYwYBHmgbW_KxBEMsvnitnfNK0e-hSc7iqH-mR2MA4YheSNonxMrglN3PoAlBcmBEwLUgRtYwo7LUI1aO3_HqBHZlXK6vm8YlMHvOU_T-sYCZoaTgO_xU37OyahDIQCjBrFTcqtDjhlduYBM9Xk2TdU_wN8syjyOIs5If9AmSEocBi_68HfPr1Uyc3vP9gai41fhRQ3UQ5-jk-UYSMpHBrwnifp-f_LIcwUOsOFGx_36vOoWjoURa60eXBUimt0MHE0xeybY8skVx1PbpF1bxb43nIhE8ivYV9tVgCG7q4Ylrb9bFMNuvNO_RgFuRnFieU2nUaqk_ckZWzW0XS2l8emDJ0XJgHtEKl7_KplF60HQ5_5Y3AO9mBzSBGVsoOppR-wjSttebeWztr-8hTS9DmiZ1KrSBvGYXhJzscZvlYGMgHyyMvcvkVxAw7-6BSAqAldzwn3H8gAtwDunC8fcWc8KR-z5c97IGbatzdESLU_D70h470Yn6izdYhNfMlXOYL3zQljhMD-DzNFtkNVaJx5sVUySq9Y6l1anJain--VxnQLVuO_6sfnFAvc6U2FnzujSLu_gJrxmxWbziulD44" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a195dc3a1f.mp4?token=d0cIllN93GpHTlUXaOSM_1FDdq_s8gf91kTDEnhFq2ZBd08Pzw702zGrYpp_D6Zs9e12DQtcrVGu8cbHROQcwiYwYBHmgbW_KxBEMsvnitnfNK0e-hSc7iqH-mR2MA4YheSNonxMrglN3PoAlBcmBEwLUgRtYwo7LUI1aO3_HqBHZlXK6vm8YlMHvOU_T-sYCZoaTgO_xU37OyahDIQCjBrFTcqtDjhlduYBM9Xk2TdU_wN8syjyOIs5If9AmSEocBi_68HfPr1Uyc3vP9gai41fhRQ3UQ5-jk-UYSMpHBrwnifp-f_LIcwUOsOFGx_36vOoWjoURa60eXBUimt0MHE0xeybY8skVx1PbpF1bxb43nIhE8ivYV9tVgCG7q4Ylrb9bFMNuvNO_RgFuRnFieU2nUaqk_ckZWzW0XS2l8emDJ0XJgHtEKl7_KplF60HQ5_5Y3AO9mBzSBGVsoOppR-wjSttebeWztr-8hTS9DmiZ1KrSBvGYXhJzscZvlYGMgHyyMvcvkVxAw7-6BSAqAldzwn3H8gAtwDunC8fcWc8KR-z5c97IGbatzdESLU_D70h470Yn6izdYhNfMlXOYL3zQljhMD-DzNFtkNVaJx5sVUySq9Y6l1anJain--VxnQLVuO_6sfnFAvc6U2FnzujSLu_gJrxmxWbziulD44" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پس از بستن تنگه هرمز؛ چرا اسرائیل عملیات خود در لبنان را تعلیق کرد؟
نجاح محمدعلی کارشناس مسائل خاورمیانه در
#گفتگو
با خبرفوری:
🔹
معادله جدیدی در منطقه شکل گرفته است، ایران در جنگ و میدان، نظم جدیدی را به منطقه تحمیل کرده؛ نظمی که نشان می‌دهد جنگ باید در همه جبهه‌ها متوقف شود، به‌ویژه در لبنان.
🔹
با این حال، هنوز برای قضاوت نهایی زود است و باید منتظر ماند تا پس از مذاکرات مشخص شود چه اتفاقی خواهد افتاد. آنچه روشن است این است که موقعیت ایران نسبت به گذشته تغییر کرده و نمی‌توان نقش و اعتبار تهران را در معادلات جدید منطقه نادیده گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/661574" target="_blank">📅 22:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661573">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7b1efe9c5.mp4?token=IO8NlyycY6GJVK9l8PhZ1OgarEskf1MWN_dKMosJbkcIv_UnWxsrNG5pG40-9wYzVQLBpLnVyIMFlBZgY4kNCxcAT1n1cxobO5PWD5_8fPf51577xySiAcsmzxtiYfsvd-DCxkLvZhX-l9O20AxnG0NHUXkrKX3bG6lAlU6Rn5D3y0bE-i0uwMdKIJ-4wQql6AFzjgHg3JdmV3aNP77lm_tqWhXw3JxoM27P0m49WGveRb4oCkHBnb83xlYJqr7vegai1i2931XJIvIvkzWZy6gIi2JXMgOPIuVRZ2_pmHm25Ra8OPRNSMZMyJLFaxbTBymokd4tCHUpy9FtsdiqLkoba9D_WMZk85j69ZvoRjrNvA7-XnmoOQwDhqCv_HSBGuRRctKrFGMpezYojP5JkdkadlK8JnaY0l31zMZx9qSMXYIrCtDXSuXoGpAq8a63ec6S2ieQdgOX8cZgjP3tuhaegpfX2I8wrEO4T_n6pW6UqR_x4rv4VSr23zOq6eiZsk2sWQMbCyyUOUFV7KHZA7VT4JalNrCpH5KYez5U7mzt-IT-hcOVU2h5GMWs28G_bThiZtBDGhAmcw3RGOZ8bVpmlPAkDooujLKNekqF-1U2mKwK_uUl3-u7xXoQFr7J3JbFwYy1KtEit9I9Vuv1YOBgyJhZTbDSLqNGvmWBMKE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7b1efe9c5.mp4?token=IO8NlyycY6GJVK9l8PhZ1OgarEskf1MWN_dKMosJbkcIv_UnWxsrNG5pG40-9wYzVQLBpLnVyIMFlBZgY4kNCxcAT1n1cxobO5PWD5_8fPf51577xySiAcsmzxtiYfsvd-DCxkLvZhX-l9O20AxnG0NHUXkrKX3bG6lAlU6Rn5D3y0bE-i0uwMdKIJ-4wQql6AFzjgHg3JdmV3aNP77lm_tqWhXw3JxoM27P0m49WGveRb4oCkHBnb83xlYJqr7vegai1i2931XJIvIvkzWZy6gIi2JXMgOPIuVRZ2_pmHm25Ra8OPRNSMZMyJLFaxbTBymokd4tCHUpy9FtsdiqLkoba9D_WMZk85j69ZvoRjrNvA7-XnmoOQwDhqCv_HSBGuRRctKrFGMpezYojP5JkdkadlK8JnaY0l31zMZx9qSMXYIrCtDXSuXoGpAq8a63ec6S2ieQdgOX8cZgjP3tuhaegpfX2I8wrEO4T_n6pW6UqR_x4rv4VSr23zOq6eiZsk2sWQMbCyyUOUFV7KHZA7VT4JalNrCpH5KYez5U7mzt-IT-hcOVU2h5GMWs28G_bThiZtBDGhAmcw3RGOZ8bVpmlPAkDooujLKNekqF-1U2mKwK_uUl3-u7xXoQFr7J3JbFwYy1KtEit9I9Vuv1YOBgyJhZTbDSLqNGvmWBMKE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت تنگه هرمز از ساحل بندر سیریک
🔹
روایت خبرنگار خبرفوری از قلب تحولات جنوب ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/661573" target="_blank">📅 22:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661572">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
تنگه هرمز مجددا بسته شد
👇
khabarfoori.com/fa/tiny/news-3224511
🔹
ویتکاف و کوشنر در سوئیس، عراقچی و قالیباف در راه؟ مذاکرات از سر گرفته می شود
👇
khabarfoori.com/fa/tiny/news-3224325
🔹
بهترین پاسخ ایران به حمله بزرگ اسرائیل به لبنان/ این اقدام تهران ترامپ را به وحشت می اندازد
👇
khabarfoori.com/fa/tiny/news-3224502
🔹
لحظه قتل پسر 14 ساله ارومیه ای توسط یک مرد جلوی چشم مردم
👇
khabarfoori.com/fa/tiny/news-3224484
🔹
پزشکیان تهدید به قتل شد
👇
khabarfoori.com/fa/tiny/news-3224302
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/661572" target="_blank">📅 22:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661571">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2e34471e1.mp4?token=RgYwoYuW1cN4mckwL8qThhlR0TZgPAGbr24TSjcD215184QGxkivQXUphgVsF-2DfjjBEYj4cPaNPYuhvV8iJ7YPlq31ud0E8M6DhL1q1BgN_CoV_xP9NqAgFdidVijI1FzMipm6b2_kHIVE6EqBCTcjKltLQIxKVLSD_m_Eys-uidPVZbZtaiJtvTzqbWqLXQzHxnE6jLEB-mwqi20j0soIIDMO_oj01PEZsSPnRNQ8rLoE2Tn-bqNkyG8ornBUV5j7uf4Zj2f3URN7D99IT7Ipj84xkzcTDKlXFHY1GuRoo66OFjhFDmzAUtkdqdrtL6yahf1wG_CFzhpttZg96g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2e34471e1.mp4?token=RgYwoYuW1cN4mckwL8qThhlR0TZgPAGbr24TSjcD215184QGxkivQXUphgVsF-2DfjjBEYj4cPaNPYuhvV8iJ7YPlq31ud0E8M6DhL1q1BgN_CoV_xP9NqAgFdidVijI1FzMipm6b2_kHIVE6EqBCTcjKltLQIxKVLSD_m_Eys-uidPVZbZtaiJtvTzqbWqLXQzHxnE6jLEB-mwqi20j0soIIDMO_oj01PEZsSPnRNQ8rLoE2Tn-bqNkyG8ornBUV5j7uf4Zj2f3URN7D99IT7Ipj84xkzcTDKlXFHY1GuRoo66OFjhFDmzAUtkdqdrtL6yahf1wG_CFzhpttZg96g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر کشاورزی: افزایش مبلغ کالابرگ همچنان درحال بررسی است و اگر به نتیجه برسیم دولت اعلام می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/661571" target="_blank">📅 22:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661570">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYbz70nUZrxK5sOaPTOYSUjlWqMRLguXSu8gPatuH7E_oqhm64lUmOqBkbsdRZTZBp680rtOQatqLBEZdY4E-XKtak250t9wCM_aUqwOTwGsPdTfjUWvEK6i2NH2_0ywcCdS4fwSuWfWv5iJb-lqEDiwvKIBRIhbkHHp1lVv8EwvBrW04We-UAQ9zhIMNSknSDdmLcKtB_alKWKeA7zd5aeIAeW8j7b11lQx7whP_Klx0xozlMG9-xHT9Hum0r2r67_8Ce41vSjbxYGKswDdKhOA_gMFmliaRw9cq8rVeFaEKL_ZW_ZuXo2iVLTYlK5a_RbnV05r9ATsA4nyHLEoCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هنرِ هجرت؛ چرا نباید اسیرِ مرزهایِ جغرافیایی شد؟
🔹
امام علی(ع) می‌فرماید: بهترین مکان، شهری است که بستر آرامش و پیشرفت تو را فراهم کند. اگرچه حب وطن ارزشمند است، اما نباید به بهای عقب‌ماندگی و ذلت باشد. تعصبِ کور منطقی نیست؛ اگر وطن جایی برای رشد ندارد،…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/661570" target="_blank">📅 22:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661569">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1qKtx7EwzkD644soe1VsEINsurXF9qNJXj9whdZqcq-JcrCHMMVitDkbhWbxGOL8IlZoX-Wlc1wblQimUuRDWk_8_Wnax340pOOxyO4x2jIrVFIxt1BbVY0tJcrwktEIAcVPT47GBfpWusdi-hTW2ahNYwibOWPFGDdMn0JgiERif78xHSSRtRnIWh_SXWBKfcZJO29TPU0_ZK1CZwK7uwzqYvxjUaidp58fg7fsN6pSJE1OWcH_cbtVLenKMKfqvqMlZa9eGoxfJ-0WdEJY77bOKeuNKHAqmjEjaAyyWOLJbN2DnwoHstcd9NCHEyhlut5RXppz2VlNH85tJdePg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دوکو غایب بزرگ مقابل ایران
🔹
به نقل از DAZN، جرمی دوکو به دلیل عفونت دستگاه تنفسی بازی مقابل ایران را از دست خواهد داد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/661569" target="_blank">📅 22:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661568">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXmDItinVLk7Uhucd7tyLS3zgvMPyJWH4q7sjFxEQSLPKU-gClJWk3V6CHExZKS5qjjy3HZrie2SIMzRwmt1havvE-nHnY4EpWlpCxOcP6JEcR2Buzl7Rg7hLhIHd2y61umQaKQdV8hTEKZAtfOPeQxrp3LtyXJEIYx1Rb7P44ou2Pw1750GBGfGnI8UYyXxoFJBUn7t71NQPv_2RrgEn09I7o6iaG-w8TYmmK4nXb6E7euZ5z3kx6EqdAGo83iLd5OMOYIRushuyp1bo_X8saR4XBqlJ9ATlQbL48KmARJxTF6E6yc8ls9KfommZgUvAfUaklsOSw9dvtt8orNILA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مروری بر وضعیت فعلی و نحوه شکل‌گیری جدول مسابقات مرحله حذفی جام جهانی فوتبال فیفا
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/661568" target="_blank">📅 22:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661565">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C2tOTNe9MwxK0-_8PiRjq7V_AWqvavrshNvOlOINB5P9rs07Fr1NoTzdTmEibbnGZHqRcHNSbVsCJycgLltJ0yQZB3WYRfvOhS2iMDV82CZD1L6a6Nl6bFjatuppNvrkhYIxXOjfa5cvIuVrWHzEyDJcPiNewB75y55urjVorkH5_gAP-iFpBa3j60G3L2oNhTnUCjiRGvFOgB0vAacnEWgmnFqIKIOHfrrFNffzyt_plSCVAO-NZNntaRts8fR4v5mILeP8YMx_eFmgUH3MPMErxJXjKbVsGIXM6m_jrNmcjTDK1WJf-TnZ0SH0l0pM6FXuToCWTJ4VojTMSBbobA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r8nFFt7pl2jrvGiIQoa1zT3tpOGESWLHJG-ojNHOZxM8H-Txo3mR22hBxAYoO-BPiLsNgroVq0y083Of5MaIWBo5jGEyOLaJXuj6VuYOe0khn_sSIccvyTcYyRvQr1bYR75IydqzENbKuQtifTNO6-c8Cj1plo6DvUqWFYVOlVs_-1nbXROHfdN3KD7aS0hXdV8FChM6vahdBtdtjCocvwunfi0l8LcoWgJaG4SA2WGxBUB16yeaBZRm8xDOBh5dNS2fKPNP2M_-gqLLc1wkjnLHRxFTe2p6YhT3mA3cVgcNgG5qHows4a2c19bLQqfem_IkZA61HXb1iHqqrf08zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZvWOxehC-tXIt5r-zDwCwV1cYp3ees37-CDkZW-7ei0VjUjaw7B7GCDmTWBf3LOGW2-MuB2UYOjyoCqX9ZPj9HQ_yli6iAUklNosYEzw93hwF3E3nAU0dT6HcSMwhZ8bC_7z6QFnI7s1Z_dYC70aQOZyG7FTrn6C4AKFZ7OyXe6kB3WAnCMc5NKvB149TSaq5ybkHqpFnRCNRCSfGi-eGO7OJHignM6r9gInrTrDzuKHT7BmtIcayeN7xoFsHGktP7SUZmufvPFeR4S01Q4PITD6LruM9C8suLqkOPyocLDvDysxAIN3ALMQhGg56fxhu4b1kZwvU_esrxk6QD-zw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چندین حادثه آتش‌سوزی با منشأ اختلالات صنعتی در شهرک بت عین رژیم صهیونیستی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/661565" target="_blank">📅 22:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661564">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/144d7341a3.mp4?token=W15KCkPfps9dpTPrjAi7f9x0VQyzbY5dQQCV7j2m__F9yaWuPh-Q94tHFyHwVu0s3CK1OR0m6_phgXIGlSUYvW8cPl5Uvp-3ihdsW3-9UUKBEz7eEhkgBOH2Fr01pdawntqxX7eZfn9Saw-m_I8XdKgOkCaRAz43_xQyLrxVnsM5bPf3_RxLImdKvqv49SIROccduIvWzhgdYB8JDrlv2BQVpW3Yn4Wkl26n5mD35F4qv9mS67k1syHkQP-4TL24pFYxRUXKmLtejaQPDzRI3xLzSaXy-GT1k7wmvy4fHw-MLjgETtoA012g5bV6SpQDsJq_QhaukGFpG3l0I4sVDi0RCRxcrFn-mESCq5J2cLDU37-Syfly3hZK4i_Imjtbz4odHjv2Nxf8fNeI0pqe0dQGdo6T5akNKf5pu5Y9VVBrPVK-xcJsLRq1_x5x9MFoFue1P4nFf_66FNMGjN9eyYxUkeASJJtDHh7IlgUIBzXJQvS2LNPl5piLQDPIfaxhFja1_Jy53A0GkqoMxARKFMPlW8ELsgt5XE4gm7UPZs9pxVkj3BSlFi-jDA_yqqKEw5v1lB8x9-NMxmn5RSoYHICDA8cJG2tgLOIrduRebc-aM8H_NGup5SLTx8ArPauoe6syJ-u7rS16PQB0K1fjvR9joq7rPeNCW8egn7-6koc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/144d7341a3.mp4?token=W15KCkPfps9dpTPrjAi7f9x0VQyzbY5dQQCV7j2m__F9yaWuPh-Q94tHFyHwVu0s3CK1OR0m6_phgXIGlSUYvW8cPl5Uvp-3ihdsW3-9UUKBEz7eEhkgBOH2Fr01pdawntqxX7eZfn9Saw-m_I8XdKgOkCaRAz43_xQyLrxVnsM5bPf3_RxLImdKvqv49SIROccduIvWzhgdYB8JDrlv2BQVpW3Yn4Wkl26n5mD35F4qv9mS67k1syHkQP-4TL24pFYxRUXKmLtejaQPDzRI3xLzSaXy-GT1k7wmvy4fHw-MLjgETtoA012g5bV6SpQDsJq_QhaukGFpG3l0I4sVDi0RCRxcrFn-mESCq5J2cLDU37-Syfly3hZK4i_Imjtbz4odHjv2Nxf8fNeI0pqe0dQGdo6T5akNKf5pu5Y9VVBrPVK-xcJsLRq1_x5x9MFoFue1P4nFf_66FNMGjN9eyYxUkeASJJtDHh7IlgUIBzXJQvS2LNPl5piLQDPIfaxhFja1_Jy53A0GkqoMxARKFMPlW8ELsgt5XE4gm7UPZs9pxVkj3BSlFi-jDA_yqqKEw5v1lB8x9-NMxmn5RSoYHICDA8cJG2tgLOIrduRebc-aM8H_NGup5SLTx8ArPauoe6syJ-u7rS16PQB0K1fjvR9joq7rPeNCW8egn7-6koc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غوغای دسته عزاداری نوجوانان در حسینیه معلی شبکه سه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/661564" target="_blank">📅 22:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661563">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df5cdbc5ea.mp4?token=s8wiAjROMIcXTp6BFJTJq6jnCioTPuYbLjaYWUraXaTrnASXfM0u18CSQ8E5eFT-2wfCmq8V9g9QCHKzm_3vXJnS0vYgFiR4ZkYvwmiqNDBUXlz57LP9PdMZF5gu_8R1qnyrK2_IUfLj2Ag4F6iy7Lk0L5C38LyCEj86-NtD9KDo9rzycp-SoqFx4HTJXH0E3bIZf_L5eegs886PJGdo7rOCPQbz-Ry7AaPjq867sBl_yHrEkleuCEEVoMW4honbko7DoG7DKiND4FhGCj2tJjcZ4jVurT6fm6-InpST3-mgdnWp7ked1yKGSargnCM1QkVa78L_ulVkZ3kuBcIjYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df5cdbc5ea.mp4?token=s8wiAjROMIcXTp6BFJTJq6jnCioTPuYbLjaYWUraXaTrnASXfM0u18CSQ8E5eFT-2wfCmq8V9g9QCHKzm_3vXJnS0vYgFiR4ZkYvwmiqNDBUXlz57LP9PdMZF5gu_8R1qnyrK2_IUfLj2Ag4F6iy7Lk0L5C38LyCEj86-NtD9KDo9rzycp-SoqFx4HTJXH0E3bIZf_L5eegs886PJGdo7rOCPQbz-Ry7AaPjq867sBl_yHrEkleuCEEVoMW4honbko7DoG7DKiND4FhGCj2tJjcZ4jVurT6fm6-InpST3-mgdnWp7ked1yKGSargnCM1QkVa78L_ulVkZ3kuBcIjYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل پنجم هلند به سوئد توسط کریسنسیو سومرویل در دقیقه ۸۹
🤩
🤩
🤩
🤩
🤩
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/661563" target="_blank">📅 22:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661557">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdoizAPKzkjZUmptGiUgWJuBMptVcszvNdNrNHl6DU8GNm7ieeyz-A1Qzs7MyfVGCAehScCAhffSxwAosnr9MexCso7PpSShPxcxHrnDNZNG-he0FEneg5b9SFXlRd7yG9h7qhaLEISnBKq8sG8HvPa5irr0z0BaNe646S10PDTjwrTshSjo6xVR5baEHUXYvcojj-lZLuttJooSVJWMR8SmJ2IWC9L5ePyoDk1PLRtHUC49rhOr3joPl7IvYnBhFd3Qguk2MAIKxT-OUmoF5rT-VE2ZhzzTR-G3cDXkumVOYHWRDid7S8AJIVUIFhYwPLINJ_ckR9J5j0gzImHJ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/530fd80707.mp4?token=F0oG8w48BRyk1tUkdFhgT3XbLvUwlKDJh8dOBHzri2PvC2LFuP49q5xL487EQIgwSJTV2dLHOfpO3DVuOJt4OmhEqPYNSyGiDOIPRvlihG-rcyL538Rm8G6QRJFiCqQ76PKl4-AZWhFkNUoDh6dS-26pWx1xI2FfvRMixp7oYoRDaSdtbpoQaZ8cpTiwYIHFqA4CmRQfPxowzQhLj_HuWw2MkPgo-TTIIEAC_uqJLd2XaItqnAjv51NH2nxbQquMFUPXcPWJe9DBgVn_Q8hS_IoiTymNW7KMQTFW75N9w7421O3pSK1LTK1dm_kwSjlKKwSTpCqM09ieoPjO6piEsIIbROgFXqKjP6tt6KCTKjXkHoXC9FVE9Hgc4Og69pF50mvkob75wpezD0Rn-p1TtIVDwzCFY-ZiO-XLZJHpJZFZIDCbuGioSA2yfJv5AX26dcdJE-D974nU6deDLPVCUfB3_DSigqIjH6aRea_KuUf88hDoasC91OwNtIWIXBfKLu_V_JpzsnLGnTgUywJwI0x6yiUOQ5lXg5vUMd99ebTYOGdE7pG82m31W0GItxfcFwFPzgeVWTUlPhpqd4KmmDkacsm14SPZiuEeCy-4SLmfOf0YOSLi-_vyKASbfjGXBOxZoSE1amRxn3iiYg68eFaBhGqUYo_tlvFYERPQKUs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/530fd80707.mp4?token=F0oG8w48BRyk1tUkdFhgT3XbLvUwlKDJh8dOBHzri2PvC2LFuP49q5xL487EQIgwSJTV2dLHOfpO3DVuOJt4OmhEqPYNSyGiDOIPRvlihG-rcyL538Rm8G6QRJFiCqQ76PKl4-AZWhFkNUoDh6dS-26pWx1xI2FfvRMixp7oYoRDaSdtbpoQaZ8cpTiwYIHFqA4CmRQfPxowzQhLj_HuWw2MkPgo-TTIIEAC_uqJLd2XaItqnAjv51NH2nxbQquMFUPXcPWJe9DBgVn_Q8hS_IoiTymNW7KMQTFW75N9w7421O3pSK1LTK1dm_kwSjlKKwSTpCqM09ieoPjO6piEsIIbROgFXqKjP6tt6KCTKjXkHoXC9FVE9Hgc4Og69pF50mvkob75wpezD0Rn-p1TtIVDwzCFY-ZiO-XLZJHpJZFZIDCbuGioSA2yfJv5AX26dcdJE-D974nU6deDLPVCUfB3_DSigqIjH6aRea_KuUf88hDoasC91OwNtIWIXBfKLu_V_JpzsnLGnTgUywJwI0x6yiUOQ5lXg5vUMd99ebTYOGdE7pG82m31W0GItxfcFwFPzgeVWTUlPhpqd4KmmDkacsm14SPZiuEeCy-4SLmfOf0YOSLi-_vyKASbfjGXBOxZoSE1amRxn3iiYg68eFaBhGqUYo_tlvFYERPQKUs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
پک
#استوری
کلیپ های شب شب ششم محرم حضرت قاسم بن الحسن (ع)
🥀
این بار طوفانی به سوی دشت عازم بود
سهم حسن از کربلا غوغای قاسم بود
محتوای مذهبی ویژه محرم در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/661557" target="_blank">📅 22:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661551">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IpFOWlt1W7PKPBAN1-2VrklM3qa3GzICJ6vDdsIrbsf1g0VpzxA0VybBVqPMAtqjgBBXwRghl5e5T8P09g6f01mjHrgsAuvuC3U2D4_5kir_PbNiarSGc-oI9DamkWRLTXPQKoBxVDEe1cdaRFDF-6GyaO0ie9IMx3cWQ0Hp47NmCZ3UstyuedS01wklG7eemmvxpzOog-UzdR23qis9g6VosL1XrDzGVvTKvJMY8P1HDBzm1Bv5V7GzMhOsbiNXIWOm1kBv0g83J9tWreM9GcZtBdlG7FXORqAfS2cWjDadBr4il25Aag1q-mWb2f-dPhcI-Sz0LC0yN2hCQXCKJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eNXfnfbJvQIgR3CqQZ5diiBSGZr05JY-jwoOhmZrMufFCAGGPbelkJ9UBO83Y4tFsRzg09UwUk7y2bg3cT6eAk2ThFltIQEeB1XWYhKrpEqlBXAUch_dudHudQCzZ66hsjD6jxEAjhP-5hzKDcX6XT8oewnyFNcviBu-7TsWR_NDDgNnp2j6Jxq_VK4nfFtj98S-No-yFGzjNGnpvm3Ivo5WbHzSX_vSQyHIosu3MBu5iwxo-_5T8MCYVV-N_WQjtsyVSCpGdM-Cs898Sb5f-UfUP7LZvnf-SRDvAmq0X9HzBX8eKW1RAi2ilLV4oLAJbBA2VKWgXdWpzqux2TIf_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ms8zg81FoHIYM1DI1I_3MAG6TBRpV6gzUsXfSuO9hC5ZRh6GpT3-Ry3n_ilJRlZxF4qVVZJipuObFE9RkVOewBoFMXbQAQKFVcrvOJa_vyNgK92sFxMOn-a-BsCo-S51cZDXcHZf-oRZcShC_XA1Qg-ZXqMjcXE9Dqz2Wwc4EZFqaF4P-ZEsGNQQ2dynleO0z_BcwCpCBBt7HLzi8GXnf8sdux8443KF7v0WnScM0iVMumxePPyGHGAkxokbw-2QkDXcefY6Iy5WTRaf8Y3DnizN8GEzF379GmR_bK1yv4PjHeNsoHi4PsesNfNdx-KgDixhjjPwyGoP3TXI9_yyiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VLttIcjaLLuU-tCKQ32_1ueVeU2rTjL-QiMJuJiGLTE-Yn8lsNBq3SIepvh9JvT1gBo2Le96s21W2mu4adCkvJVOyXYkgK9E5_9yRJFY8F18tRAmsCqZYw43l6k7n2BSXeMXDg_0kUgwzlYhgOeTDpodqn2xgh57MqXJecFqD5M5EuCPI-QS_jidV2guxJRkfBTVGPFQOp1NjH-NXPSZlXhNFGqH1eENCyeWg8Wn-okhAjze5haGaRJ62xVSZciHZaUl9FUTHHPGCCfNh-H40XgasBaDuFdBaHd_d2afYTEFPy3faeFFy36laf_dbtvZyvKqJmo36Hc4Dkw7SvukTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CDt2QrXZHC0zOl4QeaZkwoEzh3TslpSDgdHnznZohg2iyDrf-ZWQ0wsWAiN1aTixtDVU6CG31ofzbrof2S5C13Pr8K-Z-SM9QIhon267Zs9JINdxc622Zv1zjEPLtVaIZgyhoSXgxafj8oRJYY38DpXaI-9YsF7YfS2kLMy4HDcllg0vzUt6f3NS0KjEtQ9LObCCMvbW58Fp2EaXenZ0iXn_Tbqrhv1dxklqKLLbl5wXezgaucc8BsNLmGYtwZWdSgj6H_g2iw2Mxx9uW85nvjq4zbrkqxW7aXSn7W_h_QBsLG-RZZAkW_rb3rXwVJZ1whLmkRCMRoe9A71KSAzLbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uUNk5XCy0Uhu6IMbjOi1U6P2AABgW57AgumgwfV7kQmYbiS56tlb9xNJpmEkbcIrC4OK2NBaFfIZVoAw2zgspMyWyVV8dOeBgiaFhSkn9_qH2gPRhJdaY5CEacpPsqBTlkNdbqRirHY2c5LOgg2TYRmi2FH0UAJSZI4iQIFqx4GdGxbfUmQ3MdxsXfnVtya_sNbJUp1e_fbY4rCWGg9vPksK3_-Wxg88tcnb03qnZaegnvOyJWSLNaDDIwP86LeII_O6t8vu8MYnS2UMltMaSY6iea-3gU98644IZIsmBBYMleqQMIdnL3Lc6AKq6q3aQ7rhmxFELDy2wOL0UV8NnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ترفندهای کمیابی که طعم غذاتو معرکه میکنه
🍽
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/661551" target="_blank">📅 22:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661550">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc45e710da.mp4?token=JMU5MEEJYYhzB3_1TLquoeFtLTaNBt0FmrFK4NLD_EnP86omNvDLMpviNhG1JefdUPjQGS2t7c8OJ1ieBMuNfydhAn0YbxOFnACK3XRQ9si1EZJQoT2aFo7tejEVbLvnemQObOGWvdbg66wzZXGCeBqvySfJzs5RNGdAZWGVBPN4NcsSoxgmsybaDOaO6HvPzo-eeM6E4AbGiWBw7ypY40RVDoyzX-gstRlOqqF0CLU_UhqyCYkpi0hiBKFWlJKC0V4eai5xVJdYi1k7R0J6dtit2-WtaQqBntPKULLAfHnrEqjCksbFZ3-dKE_LoVuNfiBnhPLW1c0uI-xZocZZnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc45e710da.mp4?token=JMU5MEEJYYhzB3_1TLquoeFtLTaNBt0FmrFK4NLD_EnP86omNvDLMpviNhG1JefdUPjQGS2t7c8OJ1ieBMuNfydhAn0YbxOFnACK3XRQ9si1EZJQoT2aFo7tejEVbLvnemQObOGWvdbg66wzZXGCeBqvySfJzs5RNGdAZWGVBPN4NcsSoxgmsybaDOaO6HvPzo-eeM6E4AbGiWBw7ypY40RVDoyzX-gstRlOqqF0CLU_UhqyCYkpi0hiBKFWlJKC0V4eai5xVJdYi1k7R0J6dtit2-WtaQqBntPKULLAfHnrEqjCksbFZ3-dKE_LoVuNfiBnhPLW1c0uI-xZocZZnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل چهارم هلند به سوئد توسط خاکپو
🤩
🤩
🤩
🤩
🤩
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/661550" target="_blank">📅 22:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661549">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
المیادین: هیئت آمریکایی در سوئیس حضور داشت
‌
ادعای المیادین:
🔹
هیئت آمریکایی در سوئیس حضور داشت اما اعلام نکرد.
🔹
جرد کوشنر دو روز است که در زوریخ است و منتظر تصمیم ایران است.
🔹
هیأت آمریکایی پیش از اعلام رفتن ایرانی‌ها برای مذاکره وارد سوئیس شد.
🔹
حضور کوشنر در سوئیس اعلام نشد تا گفته نشود آمریکایی‌ها قبل از تصمیم ایرانی‌ها وارد شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/661549" target="_blank">📅 22:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661548">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/176d19b23e.mp4?token=Wp4jUOkJbS5IeDpg6xYre5HDfnnaiP370kUceYsWKBtVWx88UP8RWG3Y9RLir3wGs_HdEnuQ0qfmBl-5qYM1NYawnzNIvmwTQWV_y0jWPtcjSZTdFQEmOEse1QT-whZERVGwGR29HYEXkSWNjyxoTxeleDvml15Bjaty_0-Kg7YkcYIyoHS4y-JuKUi_C6mxirjl20D--kqik7XwpdLrrsIAQek1e_XtvuiSmItoRdDzYqiqadOu3bDnQEm0F0-fOS63ecb0e9imgvKJDzuYmcPxzY1ACDeAE-SqxyoxmOWKf9Uti3XGMS8qc_-vJclAQbJd9ucpO8qwEcHz-7DE2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/176d19b23e.mp4?token=Wp4jUOkJbS5IeDpg6xYre5HDfnnaiP370kUceYsWKBtVWx88UP8RWG3Y9RLir3wGs_HdEnuQ0qfmBl-5qYM1NYawnzNIvmwTQWV_y0jWPtcjSZTdFQEmOEse1QT-whZERVGwGR29HYEXkSWNjyxoTxeleDvml15Bjaty_0-Kg7YkcYIyoHS4y-JuKUi_C6mxirjl20D--kqik7XwpdLrrsIAQek1e_XtvuiSmItoRdDzYqiqadOu3bDnQEm0F0-fOS63ecb0e9imgvKJDzuYmcPxzY1ACDeAE-SqxyoxmOWKf9Uti3XGMS8qc_-vJclAQbJd9ucpO8qwEcHz-7DE2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روی پاس زیبای ایساک؛ گل اول سوئد به هلند توسط الانگا
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/661548" target="_blank">📅 22:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661547">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRpdou9NA7oG8e1pclY3kB1RfFVIsP_0d3wlSkTca0E4oEkZMgkoKvQNlwdZfGL3CdifRcrXWktquRZtyp24PT1OkABJYxcPsXtLczZh8oRBUO7gKaxZth31pym19LejOUQIxylsVAwjHH3jOdAr2qow0SmBsxihltPwZ5yQjG7pdr9vA2tQX7RekaeVOr17sADtzKG8dv4tc7tHeK8ExQTykJnkvRF6XUNuqSQvaREK6T2nz59tcGGG3NSK-E8vSrxs0CMB93E9g_q8jd-zs2f6woH0ZPZvtsvE1j5-IJp84GTklZNtIIG_CXp2XvtaLD60H-GKZ0zh3W-L2mDnpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هواپیمای هیئت ایرانی از آسمان ترکیه عبور کرد و تا ۲ ساعت دیگر در زوریخ فرود می‌آید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/661547" target="_blank">📅 22:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661544">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGCzOBNeAUSNIBf581A-4eMFH3Ia_PjHk56zlyB8E5GebGqdXit7wdIMLYA5w-GL5bTCoLY6MsjC_QcWE_ZAlEucRShgiHi3UCbItnniy4k_OoJ4h2WydIryjYIJ9Y9sdq_YLOlZZmZn5odDV6agDx5nkOQHKN85F1G4EYx49a_ALABqcBwoGGDHKPslj7QmSu1aHsMWVvkRqxt1BbQUC4N8WbHLA18svcZtqy1BMzxsR5PE0wid3Aj6VspFqDJOcJ1DxpAwvESgkFK6uUx5jFc9SI3mPwCuXmQKXFICTzEwl4ZVVUHiDeC9Ht_2W-P-Py4Lg_jwSpRFFrgDn09wxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدیرکل برنامه‌های سیاسی صداوسیما: از راه گناه به مقصد نمی‌رسی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/661544" target="_blank">📅 21:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661543">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mq0PHi3OLqCQyN_K2BaJt9ZzNW6WDfFlhpzx1Q42tCsewpoMFAFmp6szBcNNrtF2acsmt_PnajGgjdRSdkg0uj3-kgZ5SH2fkfBfh5bVNpv_dQcjuvnexmboIKklKjvA4TSmmgKMjrV1cBow-lG5cZMWsaOnj5B28jLpyhmpacP4pWca936Re5LY4rf-SNFviTUXr8eee0O257J887_J2E4IflDToIaboTezIyoiPPDOxNlzifhKy9GsIDwng6wkyFLUtVbfEsxycRKxAxbOMKVFZEY87L0whaKpqI9c5Laax0LLWcyf0JQwQLARBUASFrmVK1JGcjcI6IYMUF1m_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در پی حرف های نبویان صداسیما بابت اینکه اسناد محرمانه کشور در آنتن زنده پخش شدن عذرخواهی کرد و مدیر کل مربوطه شبکه خبر استعفا داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/661543" target="_blank">📅 21:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661542">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fp2FH9G36HcAW27E79yBHXPsjeTKTui34TE6T8WDtVS-oc2vsmSBsyylhLcdECGIyVk-MmpUxMUuvXzM9datP64HeUTGOcIy1OIlTMh6z6tIUm-vG60UJxjvoYt-QeN-z-BUpnJevg4oPh3XGgfY_w4r3PdAc3tjRCPXo0Cm4FMRtevwLsWKgFJ_luTJAzx5cc2mwqL5akvqJ9MDj67eTEZEjycevV5v2wh5l_8dcR2BFuf81ewquFVZSx0uBJj58GERJnpTL0_aYtt3CIQAAipN73FicCw9-yy5jKBfyWVAV_XEnd0fNU2AQt3xEF8HLZiDWtb6Vtwd-_dtw4PNfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر بخش بدن با چه چیزی حالش خوب میشه؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/661542" target="_blank">📅 21:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661541">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZONx85YFxI2p1XugJNuoCzLOn1cZmrIBxEOW76ka4ary9aQl5oujW12hrM9eedyq2uGWS6CR9c8gcG0ik0-C2OfaQHfbmn6NBlGa77f1UJ18nIt8Loc4VEP6-3JI9VTt1PQH4wGjx0r0nBOzDJvTKZGh3_NVtI1w_t9cJBPlGDCXjr5uJt9Z34BUMVcEWpEPCupFHaf0uzz-M6lG37JBLUAtu-D5blOxb-OZGOaub2py-M_ssNtSARBpXNMBURLUbqQaQPCflXRfIfFabkBjOB6x38M23DEPdluJJw7MYPnu3Aho4fFNUC4n-XR3smhPPafQ-v7cKhJqQy9JH-93jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استوری نیهاد مویاکیچ بازیکن مدافع وسط تیم‌ ملی بوسنی از وضعیت کارتن‌خواب های لس‌آنجلس
🔹
این بود رویاهای هالیوودی؟
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/661541" target="_blank">📅 21:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661540">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKu0m05K6YHc6NC_daYYnsrrKxb9OKQPbvDC2YY33HHdM4CctWZQYlHMIcrQMtQZb8gjidztFwdgkPsDA4oF2r2Q8HMvT_FDLDHnytQWALBqCzWGk6F4xPuU0eracjphyayyu5qQBwy3bIcHMU4ZUaCtYMoZ3dEtxdLUaQcoVb4N23ipBRFz3H6a1GTOOBfFtCjPh3IDbY2WuR6VvT4T8caUF2fJKtSGPxGsEnzz2kxIwIhJHYJ52cBhVwe3lie78e-3Gp1VzuCxVliFUDtizkDqZRBtkyolN18DylllUi2-JQo86WKWHcTSILpYfKHKZYDQzc36Vqlji1bQ9CTX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه تورم جهان در سال ۲۰۲۶
🔹
ونزوئلا با ۳۸۷.۴٪ بالاترین تورم جهان را دارد، در مقابل کاستاریکا با حدود منفی ۰.۴٪ کمترین تورم را ثبت کرده است.
🔹
سودان، ایران و آرژانتین در میان کشورهای با تورم بالا قرار دارند.
🔹
در اروپا و شرق آسیا، کشورهایی مثل سوئیس، سوئد و چین با حدود ۰.۵٪ تا ۱.۶٪ تورم، ثبات بیشتری دارند.
@amarfact</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/661540" target="_blank">📅 21:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661539">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
خبرنگار صداوسیما در لبنان: از ساعت ۱۸ به‌وقت محلی (بعد از اعلام بسته شدن تنگه هرمز از سوی ایران) تا این لحظه، حمله‌ جدیدی به جنوب لبنان صورت نگرفته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/661539" target="_blank">📅 21:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661538">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
اطلاعیهٔ صداوسیما دربارهٔ اظهارات یک نماینده مجلس در شبکهٔ خبر
‌
صداوسیما:
🔹
اظهارات یکی از نمایندگان مجلس که در برنامهٔ زندهٔ امروز شبکه خبر مطرح شده و در آن به‌صورت ناقص و مخدوش به برخی اسناد طبقه‌بندی‌شده و مکاتبات مسئولان عالی کشور اشاره شده است، مصداق تخلف قانونی است و پیگرد قضایی خواهد داشت.
🔹
صداوسیما پیگیری‌های لازم را در این خصوص در دستور کار قرار داده است.
🔹
همچنین شبکه خبر با ابراز تأسف از بی‌توجهی این مهمان به موازین اخلاقی و الزامات آنتن زنده، اعلام کرد مدیریت شبکه ضمن پذیرش استعفای مدیرکل مربوطه، به‌دلیل سهل‌انگاری و بی‌توجهی به ضوابط حرفه‌ای برنامه‌های زنده، برخوردهای انضباطی لازم را اعمال خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/661538" target="_blank">📅 21:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661536">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
ادعای نبویان: نامه های مخالفت رهبری با انچه درون مذاکرات انجام شده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/661536" target="_blank">📅 21:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661535">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bef3787bd.mp4?token=LucYWcnUlE3fhOHK09LkHKfCS-DxHDGdLBod60DsYm35S-yuTvvSE0QGpRaAkRL602oDguGIrB-OUPnOLryg-9PO6TEGswhb5B4IU0GK0G4NWAB5YWISEVgFM-aII_t0VRq3jElzmlscH8PfJZVdRn8lmoQLLsBIpvOh-6ZHtur0ZYnDrwvICSTvYueH5zUAUhHuf78mCKwiGRgIwAdrRMfaqpkXyX-O_F_XxL0c03hTQWowfmapVbwYspdu_S31C52h2eKjMZNovNeuHxW0kDCPxVtOTLYHyZVAtD2kgM4TzL_thWdjFht-IdtZ1IwpKuIZoLHtdo-RMubme8HiJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bef3787bd.mp4?token=LucYWcnUlE3fhOHK09LkHKfCS-DxHDGdLBod60DsYm35S-yuTvvSE0QGpRaAkRL602oDguGIrB-OUPnOLryg-9PO6TEGswhb5B4IU0GK0G4NWAB5YWISEVgFM-aII_t0VRq3jElzmlscH8PfJZVdRn8lmoQLLsBIpvOh-6ZHtur0ZYnDrwvICSTvYueH5zUAUhHuf78mCKwiGRgIwAdrRMfaqpkXyX-O_F_XxL0c03hTQWowfmapVbwYspdu_S31C52h2eKjMZNovNeuHxW0kDCPxVtOTLYHyZVAtD2kgM4TzL_thWdjFht-IdtZ1IwpKuIZoLHtdo-RMubme8HiJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم هلند به سوئد توسط خاکپو
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/661535" target="_blank">📅 21:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661534">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lpb9pHM5iokuenrxdR2mBSYDY4s-YjCbO1pnp8kZBjhMOMKLI6iin8pcjLTnUleAzFQ8psdZwHon6UbnNbevBYWTK1b5ecwO2AggEse0_MlzcbHPiGYPsd3RnfnJcbPWj7_2JSusItAlI7viaxKkziPgcx0KOBa8hE1PilZVu6WSajtW_RHsfKvrFcS-2fu-iBAdqX84q9PhNTVwXS4Y-LXbRfYtEohy2hNj-cU1P_CczfHHVKyVFfQyv5RYLY-ADHI6LyyCzKvNp_W0qP6T5YIgTdkknctQrYgOLgYpId7yk9MmqmVF7SVWUPW_i_bdR6SDTvbQQGQwsI2EzHOhMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در پی حرف های نبویان صداسیما بابت اینکه اسناد محرمانه کشور در آنتن زنده پخش شدن عذرخواهی کرد و مدیر کل مربوطه شبکه خبر استعفا داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/661534" target="_blank">📅 21:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661533">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ac59ad1d0.mp4?token=M0195G0HhOg4DyJ8ituCMNWf4rMxMXZnJYzjxenNwFale2l8FCQ-oifk3HuypGwKU4xmUFJ3uFtgaGwMqbKzG30kCwep7YijZ1iqGUJAVO-l9AsqPK-Qm14kRcKJ-PLR_3JaLsrULqa_QbcZTZvKmMtqMmH4awTacjhsJYu1xBWuLLO74cfUkaVEqqr5l54ZMKicQCPXOn2eCp5VV5qYjQS3SaXtoI-tnKAEfmYqrFTzmk4BZOmIaBVVXrTz_iWbAoOch3T-L6RJAaKA8QF3EG3I8HEtpKm9unVGPbhqF6_yC6twiFE3KKr_cdO8ke15yktYC90vpoTtwxnp5o7DkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ac59ad1d0.mp4?token=M0195G0HhOg4DyJ8ituCMNWf4rMxMXZnJYzjxenNwFale2l8FCQ-oifk3HuypGwKU4xmUFJ3uFtgaGwMqbKzG30kCwep7YijZ1iqGUJAVO-l9AsqPK-Qm14kRcKJ-PLR_3JaLsrULqa_QbcZTZvKmMtqMmH4awTacjhsJYu1xBWuLLO74cfUkaVEqqr5l54ZMKicQCPXOn2eCp5VV5qYjQS3SaXtoI-tnKAEfmYqrFTzmk4BZOmIaBVVXrTz_iWbAoOch3T-L6RJAaKA8QF3EG3I8HEtpKm9unVGPbhqF6_yC6twiFE3KKr_cdO8ke15yktYC90vpoTtwxnp5o7DkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیام رادیویی نیروی دریایی سپاه در تنگه هرمز
🔹
به دلیل اقدامات اسرائیل در لبنان و نقض تعهدات از سوی ایالات متحده، تنگه هرمز به روی ناوبری دریایی بسته شده است. به تمامی شناورها دستور داده می‌شود برای حفظ ایمنی خود از این منطقه دور بمانند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/661533" target="_blank">📅 21:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661532">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
قدردانی پزشکیان از نقش سازنده اسلام آباد در روند دیپلماتیک منجر به توافق پایان جنگ/ تأکید بر توسعه همکاری‌های دوجانبه و تقویت مناسبات راهبردی
🔹
رئیس جمهور با اشاره به اراده جدی جمهوری اسلامی ایران برای گسترش و تعمیق روابط با پاکستان در تمامی حوزه‌های مورد علاقه طرفین، بر ضرورت بهره‌گیری از ظرفیت‌های گسترده موجود در مناسبات دو کشور تأکید کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/661532" target="_blank">📅 21:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661531">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20ade552e3.mp4?token=WKCBln8OWJBmuREFsY_01lkrLdAGWr_m4Re2EP4UVqXCNgYqcC5IOhPjkpLEiWFC1ubIEhgFva8nNg8jeJt7F5cEBtm7bhlP90kqOPFXG8PnnpQ8xorBkQYdclH-JMxz82z3s1E4lgT_ca0--LaS6SDhxfHngM9fdKJQJVlK3o4hBBNPGHXeTRWJW4K4E_oq-ksa7M7x4nboeao_HaIEHfnL9-W0_QORAHrdRpbvXkdtXJPt_us0ADYSbiasbVf7uG3sDvEWe5QJXwaxIi1GcyByVEgINKzq7jL-wq-4vF3puw8Y-sCn65ZlgAEoNmedg_AEPjj8vd4GBpnGSwn6fJ6UCK1rfNNsJHlMEUsvC6ump-nY2yqkSFBlem1d29zOQep19NGM0zREdyG4S6KdOWusg_e-CWS4Be2toQaq1nLr9v5aXsNiFSxeL5CQaDAqFyjvPvxTcUGn2TnuEzGcb9JN_bft_dA_5SeQC0mN9YgcKEG--kydQ8pTdZ5Q7_MKXidVG_vB4sHPO7ihWuufwUROj3KPllRNAujVA4zncpC_VvUqoUA5X_0KkuILoaw60aYCFD8_KfsCvCe7t3h5xznfcsjjP-L1gJB7zLSPPb_LqhKOlGtL6EBWubjyzX1KV_iH0L3PVrGbKkt3reoKUHedy_fIWPAXGIzs-5XqAQU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20ade552e3.mp4?token=WKCBln8OWJBmuREFsY_01lkrLdAGWr_m4Re2EP4UVqXCNgYqcC5IOhPjkpLEiWFC1ubIEhgFva8nNg8jeJt7F5cEBtm7bhlP90kqOPFXG8PnnpQ8xorBkQYdclH-JMxz82z3s1E4lgT_ca0--LaS6SDhxfHngM9fdKJQJVlK3o4hBBNPGHXeTRWJW4K4E_oq-ksa7M7x4nboeao_HaIEHfnL9-W0_QORAHrdRpbvXkdtXJPt_us0ADYSbiasbVf7uG3sDvEWe5QJXwaxIi1GcyByVEgINKzq7jL-wq-4vF3puw8Y-sCn65ZlgAEoNmedg_AEPjj8vd4GBpnGSwn6fJ6UCK1rfNNsJHlMEUsvC6ump-nY2yqkSFBlem1d29zOQep19NGM0zREdyG4S6KdOWusg_e-CWS4Be2toQaq1nLr9v5aXsNiFSxeL5CQaDAqFyjvPvxTcUGn2TnuEzGcb9JN_bft_dA_5SeQC0mN9YgcKEG--kydQ8pTdZ5Q7_MKXidVG_vB4sHPO7ihWuufwUROj3KPllRNAujVA4zncpC_VvUqoUA5X_0KkuILoaw60aYCFD8_KfsCvCe7t3h5xznfcsjjP-L1gJB7zLSPPb_LqhKOlGtL6EBWubjyzX1KV_iH0L3PVrGbKkt3reoKUHedy_fIWPAXGIzs-5XqAQU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای نبویان درباره عبور از خطوط قرمز رهبری در مذاکرات
🔹
محمود نبویان عضو همراه تیم مذاکره کننده در اسلام‌آباد با طرح ادعاهایی درباره نظرات و نامه‌های رهبری درباره مذاکرات مدعی شد که رهبر انقلاب در سه نامه جداگانه نظرشان را درباره مذاکرات مطرح کردند و فرمودند که باید در موضوع هسته‌ای به پیروزی برسیم یا اینکه برای همیشه از دستور کار خارج شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/661531" target="_blank">📅 21:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661530">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0421106705.mp4?token=aLe0bKjg7PYD_ouWwjz5qjdFb9YOjul5NKDsvEahVPl7ypyTorRtca1Vl-mOFYxDjztXwk5ccABG1hqYlW-8AkbQNA16MiSIh7m4f9BJCxKF--sz-Z-Ceb3qh2tZUGbKcverMbMF1DFbdOq09TMse7W-4l7uLcdcPAxfeFF4dF2x2LmY325G2vr6EsbDU9EsCwXTfhMVHAb7gMeF_1uYJvIFBYuP6Un4EQ2e9LBib-3UyKQArrvWTmEsQWJ0jqLtbe2l5u-eHrrm4Ox6xygU0JxjL6k_CI4RchVWxk9sK000_4mkfJpn1Bu3_bf-_dYDkaV6v0z_2sFOL1SIDJmWfncGsDFzTqs2epuOTlG8O5ggquldDZ4CQbO9z0-Q4azqUAiMGB1xW_g13GGYpO5ZiCMHx7FVNv58Df7yJLmfdskSLovJvFGUxX3tJEeIxNkqeEKoMWY-UzyPJl-CYiAOlf89kSizajEh9g6hTd8nb64XHuXHH8rl0vlGvCEXbxysW0wJMywZYXVuqwPIQ9c7ijrb7paEtTHXEwMYFby_5wBsEHSBe9Yw_TVW00gkkk-8kecyEYkhwXiUGsL7cqTnd6ZnL_SLWTzyBinMc6qAJkHCFHIuRRETCi7IJAapiTRx-qAR8X1lMC6E_slwT_ZSUBS_3OzlFOdI67kd5IMCS3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0421106705.mp4?token=aLe0bKjg7PYD_ouWwjz5qjdFb9YOjul5NKDsvEahVPl7ypyTorRtca1Vl-mOFYxDjztXwk5ccABG1hqYlW-8AkbQNA16MiSIh7m4f9BJCxKF--sz-Z-Ceb3qh2tZUGbKcverMbMF1DFbdOq09TMse7W-4l7uLcdcPAxfeFF4dF2x2LmY325G2vr6EsbDU9EsCwXTfhMVHAb7gMeF_1uYJvIFBYuP6Un4EQ2e9LBib-3UyKQArrvWTmEsQWJ0jqLtbe2l5u-eHrrm4Ox6xygU0JxjL6k_CI4RchVWxk9sK000_4mkfJpn1Bu3_bf-_dYDkaV6v0z_2sFOL1SIDJmWfncGsDFzTqs2epuOTlG8O5ggquldDZ4CQbO9z0-Q4azqUAiMGB1xW_g13GGYpO5ZiCMHx7FVNv58Df7yJLmfdskSLovJvFGUxX3tJEeIxNkqeEKoMWY-UzyPJl-CYiAOlf89kSizajEh9g6hTd8nb64XHuXHH8rl0vlGvCEXbxysW0wJMywZYXVuqwPIQ9c7ijrb7paEtTHXEwMYFby_5wBsEHSBe9Yw_TVW00gkkk-8kecyEYkhwXiUGsL7cqTnd6ZnL_SLWTzyBinMc6qAJkHCFHIuRRETCi7IJAapiTRx-qAR8X1lMC6E_slwT_ZSUBS_3OzlFOdI67kd5IMCS3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعاهای نبویان، نماینده مجلس از قول رهبری: آقا درمورد مذاکرات پاکستان فرمودند آنچه رقم خورده است با آنچه شرط مشروعیت مذاکره بوده است تفاوت کلی دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/661530" target="_blank">📅 21:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661527">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c988a41777.mp4?token=KPRMmkOFsE3xuAVzB8V88ZW_zu28RFoO_d2SHcjnqRga4csCryUDGobY1bitUQ58BP6za9p4-_GU46ocXro9ZAb5nfXYv5_zzXnXfT5dV7JUOX6c8NGpUH4_F8rD__h6W_dyIB_inIZI_BI9hQzg6DoZYdr9UOtuKcgHfAahy4cdgCL6OtBaTZkXTnXBMAzKwHgBOduamMhGMnQ0NdP0Cf-iCwNSwsJ9Z8Y1vjkI_ET4OobPzUlSeh6_9SBRc02p9J4NZAok2EnD-Sk5cuceVGWzK3kRQbljrCd62GjNm-tbk0ZTuLY5DYwpeaKeUChSLPnexEsxHw6q3lZtEOYVkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c988a41777.mp4?token=KPRMmkOFsE3xuAVzB8V88ZW_zu28RFoO_d2SHcjnqRga4csCryUDGobY1bitUQ58BP6za9p4-_GU46ocXro9ZAb5nfXYv5_zzXnXfT5dV7JUOX6c8NGpUH4_F8rD__h6W_dyIB_inIZI_BI9hQzg6DoZYdr9UOtuKcgHfAahy4cdgCL6OtBaTZkXTnXBMAzKwHgBOduamMhGMnQ0NdP0Cf-iCwNSwsJ9Z8Y1vjkI_ET4OobPzUlSeh6_9SBRc02p9J4NZAok2EnD-Sk5cuceVGWzK3kRQbljrCd62GjNm-tbk0ZTuLY5DYwpeaKeUChSLPnexEsxHw6q3lZtEOYVkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هماهنگی خیره‌کننده عزاداران در حسینیه میرقطب
یزد
#اخبار_یزد
در فضای مجازی
👇
@akhbar_yazd</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/661527" target="_blank">📅 21:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661526">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc5aa3a396.mp4?token=eS_JNZ8R82GzNEvC_L_Bm5lYjOLACGWaLAT0Deyu9MJG4PyHtvZ7mSpMh7KhWxdNh8wkfunq4BfOnH_dG-M-0neTqRS87SNPQePbqNSU2v1lgl4QmIM9jqGTyBKabREzUaVn6ZF8Voo6UzmCD8L5f_LfZQlswimeMEiR4oo29DzXabqSViVat37hDuo9cxVRlMVcs4nNE0Veb9bS_I6ozi2gc_1cXeDQxh57eTsGSuEyyMGnQv65tnYl6OpVcl5-5ouq48ehjwHVYJ-WrYleKnjrMgzh2940Imy9cT5ceqJCes36uTZF_yqKVluiY87StoQeEMzp-DT5YXtmdD28PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc5aa3a396.mp4?token=eS_JNZ8R82GzNEvC_L_Bm5lYjOLACGWaLAT0Deyu9MJG4PyHtvZ7mSpMh7KhWxdNh8wkfunq4BfOnH_dG-M-0neTqRS87SNPQePbqNSU2v1lgl4QmIM9jqGTyBKabREzUaVn6ZF8Voo6UzmCD8L5f_LfZQlswimeMEiR4oo29DzXabqSViVat37hDuo9cxVRlMVcs4nNE0Veb9bS_I6ozi2gc_1cXeDQxh57eTsGSuEyyMGnQv65tnYl6OpVcl5-5ouq48ehjwHVYJ-WrYleKnjrMgzh2940Imy9cT5ceqJCes36uTZF_yqKVluiY87StoQeEMzp-DT5YXtmdD28PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای جنجالی یک شهروند قطر؛ دولت هزینه هتل و بلیط بازی‌ها جام‌جهانی را پرداخت کرده است
!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/661526" target="_blank">📅 21:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661524">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
محمد عطریانفر، عضو شورای اطلاع رسانی دولت: پیام رهبر، بر مسئولیت پذیری رئیس جمهور تاکید دارد
🔹
در ارتباط با توافق، اعلام اینکه رهبری رویکرد دیگری را ترجیح می‌دادند بیانگر وجود فرآیند مشورت میان نهادهای تصمیم‌گیری است. پیام ایشان در واقع تاکید بر مسئولیت‌پذیری رئیس جمهور و اعضای شورای عالی امنیت ملی دارد./ خبرفردا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/661524" target="_blank">📅 21:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661522">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
نخست وزیر پیشین اسرائیل: اسرائیلی‌ها نتانیاهو را هرگز نخواهند بخشید
ایهود اولمرت نخست وزیر پیشین رژیم اسرائیل:
🔹
اکثر اسرائیلی‌ها هرگز بینامین نتانیاهو را به خاطر ناکامی‌هایش و سیاست قطبی‌سازی‌اش که اسرائیلی‌ها را تقسیم کرده است، نخواهند بخشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/661522" target="_blank">📅 21:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661521">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YD1IhF-samiiF_W0MRCaf2uKLic3a9PIobOa6LnLz1ff6vxmmCaASbiX72l_wEJx4ai4WY4x56Aqa4qI5lUkDFFoTO0pSC-XDFq-Qwg5nxBqDB1-V0PsqUNc4ft-bAZHPzPrlzO2lstR9WfIDl9XmupX7alePygJKcHIfTWzH67SCRUpO04kwfkoZT1IdEjxS5iXINbUN0wS3O_083-3FpiBN2oZs7bCq5nOl3jxZmnNIWbZ6wpTTjrzictgtJpTkXG9Sk5WnLedOYa5FvSW_V6il-3ylLVGpLmxX4WxKrztzg4ltBGqyoFL4xws1jKhylGm5JNS-UsD2Qb12lP-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کمجا‌چوب مرجع تخصصی مبلمان تخت خوابشو و تخت های تاشو
✅
فروش ویژه تخفیف نقد و اقساط
مبلمان ال و تخت خوابشو
سرویس های خواب تاشو
کابینت و سرویس خواب
جهت رزرو و ثبت سفارش و بازدید حضوری
☎️
02122141020
☎️
02143000098
https://t.me/kamja_ir
https://t.me/kamja_ir</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/661521" target="_blank">📅 21:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661520">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aafb52f9ef.mp4?token=Ds9P8FgJZbHKIBcRK-eq1pgDlD1QmP7sMtEX_pt-kXY3AEy038sdYtFnDM39lAnoirZ9yUJLEaA0YknDJ9Jti4sEolPTaRSBKXrey-vzCvj3TtbwqHDGw1bxNGDpCoC6U3DjKH_VXqaYJVYq1jmQe8lJgFmu6LQ4GM75ICHcvrpz4SWf06SVaemlX8Jrdhi3IOgg_364xGXex8_zz6CkutZ4Cwqhxtt1LurcIsWDO68--a89PWMZoQbUKw36M2yj5XewHjBFB_j983olX8uHsQSSvd0FsTLr-ABhKeToSKyOZCqlmR5IAci69m5X9U6jfu5XC2JfppKABqv4qWMW_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aafb52f9ef.mp4?token=Ds9P8FgJZbHKIBcRK-eq1pgDlD1QmP7sMtEX_pt-kXY3AEy038sdYtFnDM39lAnoirZ9yUJLEaA0YknDJ9Jti4sEolPTaRSBKXrey-vzCvj3TtbwqHDGw1bxNGDpCoC6U3DjKH_VXqaYJVYq1jmQe8lJgFmu6LQ4GM75ICHcvrpz4SWf06SVaemlX8Jrdhi3IOgg_364xGXex8_zz6CkutZ4Cwqhxtt1LurcIsWDO68--a89PWMZoQbUKw36M2yj5XewHjBFB_j983olX8uHsQSSvd0FsTLr-ABhKeToSKyOZCqlmR5IAci69m5X9U6jfu5XC2JfppKABqv4qWMW_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم هلند به سوئد با دبل بروبی
🔹
طرح
طلایی
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/661520" target="_blank">📅 20:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661516">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6603f5fdf3.mp4?token=VDl3RTWSIBq99vOCS_wyyrpPHboeh4dlkELrNCjBBz5vrwY_HBzi8y_ns8DP1Vy_h75-gEeSBr5PKg9prpNB_xZnztuaLOaZrLOTz2Pa7hwDWxHe_vj2pdK1CDcMbxKOmXWZUGJ7rp3KBJ8VBd8zHb-916DsJd6aEfeB4Lys-7Zf2_L2kW8stt1gby-m2yD3xkWNgkisYwILPfJclMHKXPCGnDfbRwQd_F1FnwNkGTqfpRY48cMqN0TuZ3tZ7ngg6xjY7t3gXz3R15YKAFEySWl2WVXz4t7HANf9K1mhpKbtHkM2G7SII82bTf3lO2RR-hzmIjhLqbJdFZDxycu26w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6603f5fdf3.mp4?token=VDl3RTWSIBq99vOCS_wyyrpPHboeh4dlkELrNCjBBz5vrwY_HBzi8y_ns8DP1Vy_h75-gEeSBr5PKg9prpNB_xZnztuaLOaZrLOTz2Pa7hwDWxHe_vj2pdK1CDcMbxKOmXWZUGJ7rp3KBJ8VBd8zHb-916DsJd6aEfeB4Lys-7Zf2_L2kW8stt1gby-m2yD3xkWNgkisYwILPfJclMHKXPCGnDfbRwQd_F1FnwNkGTqfpRY48cMqN0TuZ3tZ7ngg6xjY7t3gXz3R15YKAFEySWl2WVXz4t7HANf9K1mhpKbtHkM2G7SII82bTf3lO2RR-hzmIjhLqbJdFZDxycu26w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول هلند به سوئد توسط بریان بروبی
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/661516" target="_blank">📅 20:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661515">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EptTAV0uH3BA37h0isVWL-pzfOcgdQiIIYj6VlaAoCvIdA2m4ZJnH0xceoOpZ2ZtwbUPJ355dYJ9Tq9cQD9vrt6c5Pb_OHSru43k_U_-rH4cjDuBO-GpkClHmSSm3HFOwAzNR2QNRuds5HD8mZ8UgtGpGNhAgJHPUvxgW3bGqWQ17H_hnoib9jiqplUfu7JE7QuTGS1Xppl71Ka9wu_IQlskSGPcYW6HeezewHeoZMhlXANk02VRaLqAhe72cvCYEyNips-gI1lXwL_jlBD-jFKowP2omvHw646beD62YIIikcon-G-LvcdO9otZPPOHWhN5PrblqKoEjwNY5ZrgGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سگت رو زنجیر کن
🔹
قرارگاه مرکزی حضرت خاتم‌الانبیا اعلام کرد که نظر به بدعهدی‌ و پیمان‌شکنی آشکار آمریکا نسبت به عدم اجرای بند اول تفاهم‌نامه پایان جنگ، و در واکنش به نقض بی‌وقفه و مستمر آتش‌بس توسط رژیم صهیونیستی در جنوب لبنان و کشتار بی‌رحمانه و آوارگی صدها هزار نفر از مردم مظلوم این سرزمین و همچنین با توجه به عدم عقب‌نشینی نیروهای اشغالگر صهیونی از اراضی جنوب لبنان، اعلام می‌دارد تنگه هرمز به روی تردد شناورها بسته خواهد شد.  اين گام اول پاسخ به عهدشکنی دشمن است و در صورت ادامه تجاوز گام‌های بعدی برای پایبند کردن دشمن به اجرای تعهدات برنامه ریزی و اقدام خواهد شد.
🔹
هفتصدوهشتادمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/661515" target="_blank">📅 20:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661514">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
جنگ تمام شد/ مردم سیریک همچنان لنگ آب
🔹
در حالی که خبر تفاهم، تیتر رسانه‌ها شده، مردم سیریک هنوز با یکی از ابتدایی‌ترین نیازهای زندگی دست‌وپنجه نرم می‌کنند؛ آب.
🔹
پای حرف مردمی نشستیم که می‌گویند روزهاست با کمبود شدید آب مواجه‌اند و زندگی‌شان تحت تأثیر جنگ و آسیب‌های به‌جا مانده از آن قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/661514" target="_blank">📅 20:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661511">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTJ4g9CJltVcrmV0ZDxAuOwAxMjO9wYUMZZRR5NC_5s--wGAby-_7u4hpjPl7WN16JsOkMJj_o7hyM0-d6FbDWH_eEzONRghXsWeoPt4pLENe38j8PrS2ZrTdr-7LmYkktJp6zLzFnIhkgx-67VukqrwMJdp1TC2bVocKnJ_YjWrVkQnwo_nyTBG4e1I3rXeNWlFkmiDCz8bflv10Mln32v_BHsNiRj4tiA9s5sPe9a1nQuEmZL_dnETMc2uL_2kBdS0bSFYV4VCSX8SN0wFkHMpi5N11vAVeIAYptnov4kZdXImAZNOYZtsN9gjSZgnbn1RHFHAXE6j2muEJo8yHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6e1956840.mp4?token=csaNd3COVACHBumTNfTh5FtFUWLc2IcX5l1IfUvU5zHiSN4jFEkBiXH-eyatmOC__dprxkhfEDoKyu9nc4-9Xq0E-Dn-9n2HlrRhIivefHysedp1nLilL-q36eb2MC-3csCiR_NOp0ax1ETtrNrScDu_8rIeyEURi1QU9ijvh8RKwQIG85E18sRtRwn31DQ5awoXHNXMWtYWYxM3LzsLbtbqJGJ2ZywwykeZevRAQr7bjXMcfa0SApQlQUsCDH92QNeebALH17e2kE6FWpqoQjbpgjof_7_6XNmhCbn4DuwYTz5Cn_-bJ0SiEP9hZrOr6K6z992uVBF2IVydt9ViAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6e1956840.mp4?token=csaNd3COVACHBumTNfTh5FtFUWLc2IcX5l1IfUvU5zHiSN4jFEkBiXH-eyatmOC__dprxkhfEDoKyu9nc4-9Xq0E-Dn-9n2HlrRhIivefHysedp1nLilL-q36eb2MC-3csCiR_NOp0ax1ETtrNrScDu_8rIeyEURi1QU9ijvh8RKwQIG85E18sRtRwn31DQ5awoXHNXMWtYWYxM3LzsLbtbqJGJ2ZywwykeZevRAQr7bjXMcfa0SApQlQUsCDH92QNeebALH17e2kE6FWpqoQjbpgjof_7_6XNmhCbn4DuwYTz5Cn_-bJ0SiEP9hZrOr6K6z992uVBF2IVydt9ViAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هری مگوایر در اقدامی غیرمنتظره، فروشنده برچسب‌های جام جهانی در خیابان‌های نیویورک شد
🔹
پس از اعلام فهرست جدید تیم ملی انگلیس و عدم دعوت از هری مگوایر توسط توماس توخل، مدافع انگلیسی در یک برنامه تبلیغاتی جالب در خیابان‌های نیویورک حاضر شد و به فروش بسته‌های برچسب آلبوم جام جهانی پرداخت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/661511" target="_blank">📅 20:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661510">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
از دار قالی تا دنیای مردگان؛ زنی که پس از خودکشی از عذاب هولناک «تشنگی» بازگشت
🔹
00:06:30 قالی‌بافی برای حرم امام حسین(ع)
🔹
00:17:00 تصمیم به خودکشی در لحظه دلشکستگی از رفتار فرزند
🔹
00:35:30 ورود به اتاقکی با پرهای ققنوس
🔹
00:42:15 همراهی من به عالم برزخ توسط دو موجود ناشناخته
🔹
00:49:35 تشنگی مفرط باعث تغییر چهره انسان‌ها می شد
🔹
00:53:50 دست به دامان شدن امام برای رفع تشنگی
🔹
00:56:10 خارهایی که مانع نوشیدن آب از نهر می شدند
🔹
01:02:00 تفاوت برگشت روح به جسم در انسان‌های گناهکار و بی‌گناه
🔹
قسمت نوزدهم (رشته به رشته، مو به مو)، فصل چهارم
🔹
#تجربه‌گر
: اعظم فکریان
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/661510" target="_blank">📅 20:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661509">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bh0jj_ccEi3n9igqrl5Cxci4vVnFS02ZQ2HDxtsb7M9FskwJ3WL2XLdu92Dy0DX0pGvt8LK2o_wkg-Pl7r5cv_k5SI60xNmDnP-7TuDhWHOlHEAvap_9yLmSdtAW5tGVj2ymv3Y5OrdmjERE0jK5MMaaFw2thW94XNaaOQinDZHsKX4ZD1-5gHaYAMuokogPkh6-vNnlYla5P_S92_-hjt6ST3LBKCaG3LSxiYM4rVYnonKV-f_msEH5zgjUl0HqQfWYgCwfe2lFVx6C8fmC776MzXRPAuGZxBvlmzeOZMxMPeHTlGFsqlFvGHD_zCQQTsG67g5NO_3QibYXxmXrEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استیو هانکه، استاد تمام اقتصاد دانشگاه جانز هاپکینر:‌ در نتیجه نقض آتش‌بس از سوی اسرائیل در لبنان، ایران اعلام کرد تنگه هرمز اکنون بسته شده است
🔹
به لطف ماجراجویی اشتباه آمریکا و اسرائیل در ایران، ایران اکنون همچون «شمشیر داموکلس» تهدیدی دائمی بر تنگه هرمز دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/661509" target="_blank">📅 20:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661507">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⚽️
نبرد ایران و بلژیک و هیجان فستیوال بزرگ گل طلایی بیمه آسیا
🕥
از همین
امشب ساعت ۲۲:۳۰
تا
دقیقه ۷۰
مسابقه فرصت داری حدس بزنی: برد، باخت یا مساوی؟
🥇
یکشنبه ۳۱ خرداد ساعت ۲۲:۳۰ همزمان با تماشای مسابقه ایران و بلژیک، شانس خودت را برای افزایش امتیازات و شکار سکه طلا امتحان کن.
🔔
یه راه ساده برای برنده شدن:
با ثبت نتیجه مسابقات جام جهانی ۲۰۲۶، امتیازاتت رو برای بردن جوایز بزرگ، بالا ببر
🔗
ورود به سایت و ثبت نتیجه بازی:
https://www.bimehasia.com/جام-جهانی
@bimehasia_co</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/661507" target="_blank">📅 20:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661506">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
هتل بورگن‌ اشتوک سوئیس کجاست؟
‌
🔹
هتل و تفرجگاه بورگن‌اشتوک در قلب کشور سوئیس و روی یک ستیغ صخره‌ای در ارتفاع بیش از ۵۰۰ متری از سطح دریاچه لوسرن واقع شده است.
‌
🔹
انزوای جغرافیایی بی‌رقیب این هتل، امنیت مطلق و دوری از رسانه‌ها را تضمین می‌کند. این ویژگی به همراه سنت «رازداری دیپلماتیک سوئیس» باعث شده تا فضایی دنج و کاملاً تحت کنترل شکل بگیرد تا با کنترل شدید روی روایت‌های رسانه‌ای، از ایجاد مانع در مسیر پیشرفت مذاکرات جلوگیری شود.
‌
🔹
از سال ۲۰۰۷ مالکیت این هتل در اختیار هلدینگ کاتارا هاسپیتالیتی، هلدینگ هتل‌داری و پذیرایی صندوق سرمایه‌گذاری دولتی قطر قرار گرفته‌است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/661506" target="_blank">📅 20:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661503">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z4728N0gQaex2KXspFAJm1bjpTyAb_stltu4REPxgdkfsdqTEAnZOzTIG7MHKl4eTxBAchlYpeA3OhiEcV9JOX1UI9y29GctBo_gGSr9Gy2mloFotizElXZhMHCFHdYUHJUTIWh39PG6aWoTF3bJXYSsxbRix0qBH0GCXVFieYHz4g5BC2VZe6V_dhy4rwzyazRkplnpCMgxdQ10jiV61nuHWLQhVMtOyySL0ZOR2S4AyhFlxrOw2f17gByZ_iqCZX4guinr0_bJY0f16V580f9Zv6Sw4h7bjwBRTMT9G0AM6LeyGj5cgHOhY6Pm2ylmgSqp0MbfXegoLzsrNWFGdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DnG25erurjV0xrMG7ZHq4PzmeW_jCx3-4sQW4wxkF1BDa8enp5u-2Z5i74KSX29vGX51JzQ4twEYgMZapJnLDrb-iF4UnGn4M09Hth5GifP52kYsc2NmRgIK_SuT4TjVxeMWumPJ0rh98Y-Aer5zo8kv0SI34ad1NdK99GQD09CGxn0PoMigu4BEBaLLyb02XSf7lzyX2rwZv421b9nWjVX3uESjgzPiejYp8jccTghxG_XH-uyaKNDRWX9YJ6r5ARNY9WcFkirRnTvUWYltMTyVZ4U6hiGBY38o4PM8l8W_EoyuLTXN6MHyksXZR7uUG77p3KtanLP5oRDXMDzg5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر کتابی می‌خواهی که اشک را از تاریخ جدا نکند، «آه» انتخاب خوبی است
🔹
«آه» فقط یک کتاب تاریخی یا داستانی درباره عاشورا نیست؛ روایتی زنده و نفس‌گیر از لحظه‌های کربلاست. یاسین حجازی با نثری شاعرانه و تکان‌دهنده، مصیبت‌ها و صحنه‌های عاشورا را چنان روایت می‌کند که خواننده خود را میان کاروان حسین(ع) احساس می‌کند. کتابی کوتاه اما عمیق، برای تجربه‌ای متفاوت از عاشورا.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/661503" target="_blank">📅 20:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661500">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NbPScGKmfdmoVDXZ4ggXyurjJ-eEyqmQeaoe03cOf2zXJqHEQ6Eb3W-9hc-v82Qpi_4ouahDdccGjUYTktUX2ii_CYnNyxPtvRnU7zze2p0SvtPTInvvwjX6e8fwthr3BzoUSeWxY5LgG_JKOdZmxJpyrbxJDKLMkXoc_0oZ4knCrQNbjUimgDtCyIoio7IXJr9j0P6IACtmhne6M1KRlG5d06TEChUVA9YcsS-uy77EaRerB4iaSNBoT-HKDUGJpEbcArtdO1CyDJJz6zp3HmuovY2xgx-XWXBY8_F1yTBnmZpm7LJQClLOzMu10blpY7KRtY_4PnS7_wAGNDdkoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X_1oTy11naDJOKiiJ8R3r6jSEjuIvJg2-Cv5YJENX801ccA7U4v-Uli3tSGMXjVF5zXRLik4LDTXYLf_TWsS9WZCAonp_vKclg4PEwmayEtRmRV8grhY9qT4ztYtDWLM_Hn3YK4FSfsfbydWza0vOAx0XTeM2sJGZ3V0jrIxvicJlpfVxphXW3cy7MONgNq3fUD_J5O3ststMzVg5xjkfjvg3DgPc9u5b6EWfXtK4GUNR-XFuaLdpdhZInqaalTH1IMCYk3ZsAaVgogWuU3a_-FAFBFQ04fJRozaCccFcDeKc31ZeTHPGKoSv9rF4_sALf7B2JWqx9Y2sgfJ-wbH0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kU1fVNclBrN3ueVhHRKVeNxNWDfu155NTLt6c07zimJE5IYOTwfK42iiOrY95e3B6wLhdO_LWrseUIOiLtnC2EQBmKuRP5h-9WJiXOxh14b3qLs-iP_uj0hhx3iXQpV2e33xRCaKb_BXKhdpJbNHmloRgCq40mq8nASSXPE14hWvGBYF5HKUFGS_CSsHMABo9D816rxn-9DW2JtqMthd0annBCXCrCZdbwfBYacNMW64TuMoMpu2wNPAYDSMU2u24UPHuWSZ3h62tcbckKYlfFixohnnCk1dewTiMHPu5M6xbUmFnGhsbQxXT5gGXSYo9lak7K9SAkcYd5Wmn_XjwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فرود عجیب یک پراید موقع رانندگی روی پشت بام یک خانه در اراک
#اخبار_مرکزی
در فضای مجازی
👇
@akhbar_markazi</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/661500" target="_blank">📅 19:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661497">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
ادعای سنتکام: تردد کشتی‌ها در تنگه هرمز امروز افزایش یافته است
🔹
ترافیک کشتی‌ها در تنگه هرمز امروز افزایش یافت، زیرا ما همچنان به حمایت از آزادی دریانوردی ادامه می‌دهیم.
🔹
۵۵ کشتی حامل بیش از ۱۷ میلیون بشکه نفت از تنگه هرمز به سوی بازارهای جهانی عبور کردند.…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/661497" target="_blank">📅 19:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661496">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e355b9bc7a.mp4?token=XBDeQIFjJNTn_qP8bTDR1ctl6uQc5IZkFEvRB6FvipuIRKvFzgRlBg2cOyQY4_Le49q-jbaMC5Owbxrve1DE1NnuaDWxN-tpPJ-RSnUYM4iDru6usXCSlCYuNB9wUca5zLtKc1iFzCmU7orlAROB-PKvs33mOCFdtWezAsenQsjMwrBvV5xCV-75UYbPnsdsDD1GglnVvacW2bSgStl6m79ec8NmIhX3ezP5EuDj3NTEKGY0fEx_iwM7iikzdDe3sc-yq_dQ6LZTO8ERAftundi-oqQYunJ8TAtL65JJ7tzF2eP3RUoGOCT6_QPw1oBNNlZu1OPvlR00lVDiQ_e0IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e355b9bc7a.mp4?token=XBDeQIFjJNTn_qP8bTDR1ctl6uQc5IZkFEvRB6FvipuIRKvFzgRlBg2cOyQY4_Le49q-jbaMC5Owbxrve1DE1NnuaDWxN-tpPJ-RSnUYM4iDru6usXCSlCYuNB9wUca5zLtKc1iFzCmU7orlAROB-PKvs33mOCFdtWezAsenQsjMwrBvV5xCV-75UYbPnsdsDD1GglnVvacW2bSgStl6m79ec8NmIhX3ezP5EuDj3NTEKGY0fEx_iwM7iikzdDe3sc-yq_dQ6LZTO8ERAftundi-oqQYunJ8TAtL65JJ7tzF2eP3RUoGOCT6_QPw1oBNNlZu1OPvlR00lVDiQ_e0IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حدود ۱۵ سال پیش بازی‌های موبایل به این شکل بودن
🥹
#نوستالژی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/661496" target="_blank">📅 19:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661495">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5cm7OGR1hKKtEmc-PjRRS4rtSYnphWqqdKZFWj2k5yRBgg8ZsB-Khw3xQ7wVoOMLxsbJCD8KXtVNsgCNcZswpsxKZ9vVE0w7_EbMT0qUNmyhhTOCxGp9FKG1siEw2lpCGz5F3aoZy4EV63ixK9eoqYNOMvWf-DGrcfSwxY0zsoa_RI4m9R49cChuZZsL6xVkUCr-3MiJQdIdYYckAcl8lV7ZblLFj3YOavwhg4TzlbUJbU7sXIJu7npfDNECuD6fwLKQIRzxmUYtGDO4Ap9VRqgMNjwVxzGK8zFyhsARmjPSXM2C09iiFLk2y7PHCBKRE4Fa4v340U5MW2kU1etEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/661495" target="_blank">📅 19:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661494">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81e10405c7.mp4?token=T0fA8ietYOVyptWct3nlS4VQYfk5EIThyPsC-pggzmeCnhgVV09UoHP_1HXuxoDbsSjh0586kITdkuxIYiSHlBEBnxSIzW35nHWV3t0sV_El9P6PsyhgnxODVWU37sR595sj9zQIBoRp9EnC0dvrRDlqVRFNU1BxSeu6-x_TsuriLIoXTmVxD3k8Oxn4FHBwy8aWj1ybu0AbNDdWL1hp7kE-Afy-ZLhZP7jPp5K6kbluOFcBf_-0E6ZOYl7QY8p6uLvxvsf2oN6nVsSUiRung1q_RqyiXaTheTSiwLhUVALv4CKQogd4UJc3Ye85BbhQPtdq8e2lCM_ZB5JeWFAivQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81e10405c7.mp4?token=T0fA8ietYOVyptWct3nlS4VQYfk5EIThyPsC-pggzmeCnhgVV09UoHP_1HXuxoDbsSjh0586kITdkuxIYiSHlBEBnxSIzW35nHWV3t0sV_El9P6PsyhgnxODVWU37sR595sj9zQIBoRp9EnC0dvrRDlqVRFNU1BxSeu6-x_TsuriLIoXTmVxD3k8Oxn4FHBwy8aWj1ybu0AbNDdWL1hp7kE-Afy-ZLhZP7jPp5K6kbluOFcBf_-0E6ZOYl7QY8p6uLvxvsf2oN6nVsSUiRung1q_RqyiXaTheTSiwLhUVALv4CKQogd4UJc3Ye85BbhQPtdq8e2lCM_ZB5JeWFAivQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صداوسیما: بمباران در اطراف شهر نبطیه همچنان ادامه داد
🔹
رژیم صهیونسیتی در تلاش است ارتفاعات اطراف این شهر را تصرف کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/661494" target="_blank">📅 19:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661491">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65eed99daa.mp4?token=tvr-Tz9J5ka5ZTWiRHoKG7C-Rn8uBPt9Ys92-c9d5OTnrE-8y_6GBwW1RWKSuQ-X-liuaWwU8x1KcTPaEnGVfSmrwxLPzTnTmpP4gQDXdq6nRalLK5kwIOdOE_Fz184zM9qetX2sAl-vselEn9wA6Kqq_3Ssz05ndS1CyM15GbOwynsKbT50_e6zkngaQgpoqAEQIb6UvoxuLBDX7OaqB6fqm1IBfq8zpEQ-0rVFw_omlFQ7ZJrPaJDCiumW-Hz1HSA8RnQsbIlgQed9N2U0kXmYm_NMLuy6FWeGtnOb2x1MjlwJ0SBhrxpa9BWJ5fpZWuSqKs3P63ETGd5rsGhKXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65eed99daa.mp4?token=tvr-Tz9J5ka5ZTWiRHoKG7C-Rn8uBPt9Ys92-c9d5OTnrE-8y_6GBwW1RWKSuQ-X-liuaWwU8x1KcTPaEnGVfSmrwxLPzTnTmpP4gQDXdq6nRalLK5kwIOdOE_Fz184zM9qetX2sAl-vselEn9wA6Kqq_3Ssz05ndS1CyM15GbOwynsKbT50_e6zkngaQgpoqAEQIb6UvoxuLBDX7OaqB6fqm1IBfq8zpEQ-0rVFw_omlFQ7ZJrPaJDCiumW-Hz1HSA8RnQsbIlgQed9N2U0kXmYm_NMLuy6FWeGtnOb2x1MjlwJ0SBhrxpa9BWJ5fpZWuSqKs3P63ETGd5rsGhKXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مردی اهل ایالات متحده یک Wall-E لِگوییِ واقعی و کارآمد ساخته است
🔹
این ربات می‌تواند حرکت کند، چشم‌هایش را تکان دهد، به کنترل‌های دسته‌ پلی‌استیشن ۴ واکنش نشان دهد و صداهای انیمیشن را پخش کند.
🔹
درون آن موتور، سنسور، بلوتوث و چراغ‌های ال‌ای‌دی کار گذاشته شده. او همچنین دستگاهی اضافه کرده که قادر به ایجاد تخلیه‌ الکتریکی و شعله‌ور کردن اشیای کوچک است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/661491" target="_blank">📅 19:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661490">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlPkqcUUeZLpUXri1pFA9PlXHGGjZ7WP371zW9Bv0luQWFF3BE4jO4LeXp2BkzgH6yWpsS8ndPsxTcDUIi6WvenFm6VK6slp8ziQ73RfW79E9Awlph_iUhvSt0BNyFS_Cpj2wDs1AYymajcrVvX4kR5_9Wx3-NT-92rl5ibAXzKFqNbWcoP1RV9ao4Z4kxHTZFD0uPKgLrHb6L6CyIAW5S_MpA9j-ZIFB92-za5Sry8syq_M6lIuKlK2qbtI0CCy0JYsjeh0utm1tejr_05qlT7mcMUY8kjCanjKhdizkiv0RD_UeQZ5GnGua7O-2nfpnUJX8lBd-s0UlKXpU249DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کلیدهای میانبر در Word را بشناسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/661490" target="_blank">📅 19:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661489">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFXojKgCtZNPpPg80tyyKw_ARefCQikYM6q44zv5d-OXySIz2Z4lS65LUb_MUxrIXN2ToHGOVqLxqNRdRVSTZnQWtPsCnd-C3SVZjtZ-tkMKErgfKn2mCibbQE4gM2KBOOopBknF8elnpsyCHuOyxCvnMuY86OUIUUju4mCbavv12B4ppuXJgNHPPjhqT5vrH1ZVp4LW7BWVbWwZS76aHWoeSlzXXegEojtGC3WaZuGJYgMcXWyp33aQfxJBDsZwlJg0vRghnwfgoI5mrhIkR9xVMS-98Pl9EWB_4p6nzQiPASWFNVglBN7AHg0-PJ9qjqFe2F72lkQ4zDC8yLBZWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
«سقای شهر»؛ پیوند خدمات بانکی با خدمت‌رسانی به زائران اربعین
🟢
بانک شهر همزمان با آغاز ماه محرم از اجرای طرحی با عنوان «سقای شهر» خبر داد؛ طرحی با محوریت مسئولیت اجتماعی که با هدف حمایت از زائران اربعین حسینی و تأمین آب آشامیدنی برای عزاداران در مسیر پیاده‌روی اربعین اجرا می‌شود.
🟢
بر اساس این طرح که از ابتدای ماه محرم تا روز اربعین ادامه خواهد داشت، مشارکت‌کنندگان با افتتاح حساب ویژه «سقای شهر» و یا نگهداری موجودی در حساب خود، امتیاز دریافت می‌کنند. این امتیازها در نهایت به بطری‌های آب آشامیدنی تبدیل شده و توسط موکب بانک شهر در مسیر پیاده‌روی اربعین میان زائران توزیع خواهد شد.
مشروح خبر را
اینجا
بخوانید.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/661489" target="_blank">📅 19:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661488">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyIO1iJeANLJFkCtBS4TG3-9IO-MDIBH7Fb9C_UoTtIHbM3akzDjbzBBPiN8pK1pNOOHCuncnWjGlaR8vON9HCGfidw6toQ5NsHJGB30X6reNHnTAgOM56LtC3kpKuBkUAU9tVd_9Lg8ogN8hBjRoDtDf89Rh_wamnrkZkOAYHMpnEj27XHDg8PTeFJgEl9LAHBrDAZTl7Yf0WVywvUZLMBt8t7vS7MRM16QhFIQMhQA2esRhSiJJU6ncx_prfXtJ7siROvleZoGzAJu-ec64ww9nZTudp9Y1uoeiVkaoBpoxulm-H1aALZCuKpn7QMjojJQgGWjUc725BiyI_yGVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران‌خودرو: دوباره گران می‌کنیم
🔹
ایران‌خودرو که ۲۷ خرداد قیمت ۲۵ محصول خود را افزایش داده بود، پس از اعلام وزارت صمت مبنی بر لزوم اصلاح قیمت‌ها، قیمت ۳ محصول را برای مرحلۀ سیزدهم فروش کاهش داد.
🔹
با این حال، این شرکت امروز اعلام کرد این اصلاح فقط مربوط به همان مرحلۀ فروش بوده و پس از پایان آن، قیمت‌های افزایش‌یافته در ۲۷ خرداد همچنان معتبر و قابل اجرا خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/661488" target="_blank">📅 19:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661487">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7H366pqXg7iFEWd4kYqtn0DPuC9G6Dni1SjK-4P7IIJZRoRD4hvqpfdN9U61wUMW3NnlWwcUyuE8MWT4R9YHMW32kH5UgU6dzISxlV3f4Gt4QzvghobBhq1KRZ7jmnS1OlbpcXfvFvE2ALX_M5s3uzUIWGQewmR3XrEOpqmxS2ilPv67ebZ0lJqVtA2QCBea5DSIQvdQeAeFe9zuoj2uasOL7bfBZh1_LHb8FjcS3Mc6nWsbd6VyPrlk3mLF1WRH9jKAJADFVEFHU627xgG63oA7eTpomXXDdK6ma-jaao6Mhzl0D4dQ4ksLBn5lTyQC0WhvfR_gtHthMNF8XOCPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/661487" target="_blank">📅 19:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661486">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
ادعای سنتکام: تردد کشتی‌ها در تنگه هرمز امروز افزایش یافته است
🔹
ترافیک کشتی‌ها در تنگه هرمز امروز افزایش یافت، زیرا ما همچنان به حمایت از آزادی دریانوردی ادامه می‌دهیم.
🔹
۵۵ کشتی حامل بیش از ۱۷ میلیون بشکه نفت از تنگه هرمز به سوی بازارهای جهانی عبور کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/661486" target="_blank">📅 19:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661485">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
نتانیاهو دستور توقف تجاوزات نظامی در لبنان را صادر کرد
🔹
نخست‌وزیر و وزیر جنگ رژیم صهیونیستی دستور توقف عملیات نظامی در لبنان را صادر کردند اما بر تداوم تجاوز نظامی در مناطق تحت اشغال تأکید ورزیدند #Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/661485" target="_blank">📅 18:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661484">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
مهم‌ترین حواشی و اتفاقات جنجالی ۴۸ ساعت گذشته جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/661484" target="_blank">📅 18:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661482">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d26a976aaf.mp4?token=NDvPxDemwyNuWf5d4Z44ua2mQFFXJ2zvMVmjsp7S9MOs9m2vtHO1YE05KrtU-OWQbb7lA3Jtj5jrtiRkJij_HXgYRwdaxFtErRfqsVi3ZRXHK6MJxLN_aiwqcWbVIeufc44QnFjcJRtWFgZ9Gj5TS7BOrlXUtRqZw8vhDCZeiO-LbZFZRfShHIlpy6aJqP97bsECNk1vI8RV4l7eWmWGrwlvB17BTrjEpElD_MMEs0-7ZKhqBjTq-R8tnc3rwfR0B3mzHiKhz7xsRv-z9WHbe-2JDTJuwBwFd4Kzzg0ivYoWB_pqFwMzykByvh-CQVCZxdmoK3IHVr6mFcrabpbX7TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d26a976aaf.mp4?token=NDvPxDemwyNuWf5d4Z44ua2mQFFXJ2zvMVmjsp7S9MOs9m2vtHO1YE05KrtU-OWQbb7lA3Jtj5jrtiRkJij_HXgYRwdaxFtErRfqsVi3ZRXHK6MJxLN_aiwqcWbVIeufc44QnFjcJRtWFgZ9Gj5TS7BOrlXUtRqZw8vhDCZeiO-LbZFZRfShHIlpy6aJqP97bsECNk1vI8RV4l7eWmWGrwlvB17BTrjEpElD_MMEs0-7ZKhqBjTq-R8tnc3rwfR0B3mzHiKhz7xsRv-z9WHbe-2JDTJuwBwFd4Kzzg0ivYoWB_pqFwMzykByvh-CQVCZxdmoK3IHVr6mFcrabpbX7TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویداد داستان جنگ در برج آزادی برگزار شد
🔹
دورهمی صمیمی اهالی رسانه و کسب و کار با نگاهی به آمار رسانه‌ها در جنگ
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/661482" target="_blank">📅 18:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661480">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbWCq3Dz7MuNZua5f0kJXs5zPuMYEdqHRrQbrovHyhsxZYVOhcqHl2m6NzfOtIRqYnAEEXuqTbkIgcQcQLNYD9QxqEHAetGLsCTYJCKpTbnTRgjsDdATOvP1v9XCHw9aRbVkGzMciBTbKprccQGxAB5xcQSeEuExhh0qkAu1BzDlaLJjHj-CbEy7ILykJm-6RWK5pCV_OtNUPhiLHZFcDHHm8P9ce_Vxn_7riV13T3LTbpcpKn1VUHardizQoDDdV0qlA6IomysQxclMlkL581ea52HZg7AVkvnoq5NoYRCQ0h-vfIZ90rr0uN6DkvbAmODaj0aNtfTR6ep5I0QpBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حاج حسین آقا ملک؛ پاسدارِ ابدیِ شناسنامه فرهنگی ایران
🔹
حاج حسین آقا ملک؛ بزرگ‌ترین واقف تاریخ معاصر ایران و نبض تپنده‌ فرهنگ ملّی. او با وقفِ نفیس‌ترین کتابخانه و موزه در قلب تهران، ثروت افسانه‌ای‌اش را به دانایی پیوند زد. مردی که فراتر از زمان زیست و با…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/661480" target="_blank">📅 18:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661479">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
هشدار جدی مقام ارشد ایرانی به آمریکا؛ مهلت زمانی برای توافق محدود است
🔹
یک منبع عالی‌رتبه امنیتی و سیاسی ایران در گفت‌وگو با شبکه المیادین اعلام کرد که میدان نبرد و دیپلماسی در هماهنگی کامل با یکدیگر پیش می‌روند.
🔹
واشنگتن به تعهدات خود در قبال لبنان پایبند نبوده و این خلف وعده از نظر تهران کاملاً غیرقابل قبول است
🔹
جمهوری اسلامی ایران هرگز دوستان خود در لبنان را تنها نمی‌گذارد و از حمایت آن‌ها دست برنمی‌دارد
🔹
ایران نسبت به محدود بودن فرصت‌های موجود برای پیشبرد تفاهمات هشدار داد و تأکید کرد که زمان برای طرف مقابل بسیار محدود است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/661479" target="_blank">📅 18:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661477">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
تعویق یک هفته‌ای امتحانات دانشگاه تهران
🔹
تمامی امتحانات پایانی نیمسال جاری دانشجویان دانشگاه تهران با یک هفته تأخیر و از شنبه ۲۰ تیر، در همان ساعت، روز و محل تعیین‌شده قبلی برگزار خواهند شد.
🔹
آزمون‌های برنامه‌ریزی‌شده برای روز ۱۱ تیرماه، به تاریخ ۵ مردادماه ۱۴۰۵ منتقل شد. امتحانات دانشجویان مقطع کارشناسی در تمامی واحدهای دانشگاه تهران به صورت مجازی برگزار خواهد شد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/661477" target="_blank">📅 18:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661475">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rF7ntaKtKpKEmn31JXFaY_yzY30oK5atE3JFyPCyAwyIOe3UcMhde8mblaUxdLEXLU4NScbnLifLNrV8qikNqpIXmNE0ukwI4rZU8NmRaGmod0is4U-U0wXZHVxzZ0M_CYPb1LzKzBO5pknot5qc6OgDv5HoFiDk_VduXozIkeM2eG2qU4gdSNrhBbUBxLQKJz1PYIKb8V6E8f1V9v2NUEayg_rFQkJxhf75_MQ7MI2g47FPiJXelAig_KzU6DaHeSFZcwkgL3CwoKKDDakFKRiLNqT8aNru3IT6e91kvqBA4Bl8UYNvPjfESSNKxGzYYyrbzj_rQoTDhxRhVRKAyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین خبر از وضعیت میرحسین موسوی و زهرا رهنورد
🔹
میرحسین موسوی و خانم رهنورد، از بیمارستان مرخص و به خانه‌ای که ماموران امنیتی تعیین کرده‌اند منتقل شده‌اند.
🔹
وضعیت حصر کماکان پابرجاست.
🔹
طبق خبرهای رسیده، روند درمان میرحسین موسوی همچنان ادامه دارد./جماران…</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/661475" target="_blank">📅 18:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661472">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
آکسیوس: ویتکاف عازم سوئیس است؛ کوشنر هم‌اکنون در سوئیس است
🔹
انتظار می‌رود دور نخست مذاکرات آمریکا با ایران در آنجا برگزار شود.
🔹
هنوز مشخص نیست زمان جدیدی برای مذاکرات تعیین شده یا نه.
🔹
معلوم نیست ونس هم به سوئیس سفر کند یا نه.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/661472" target="_blank">📅 18:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661471">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
نتانیاهو دستور توقف تجاوزات نظامی در لبنان را صادر کرد
🔹
نخست‌وزیر و وزیر جنگ رژیم صهیونیستی دستور توقف عملیات نظامی در لبنان را صادر کردند اما بر تداوم تجاوز نظامی در مناطق تحت اشغال تأکید ورزیدند
#Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/661471" target="_blank">📅 18:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661470">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
هیات مذاکره کننده ایران تا دقایقی دیگر عازم سوئیس می‌شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/661470" target="_blank">📅 18:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661469">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41e56de999.mp4?token=GA4EZlfa1uqOxOhZU-Qzw7HXCdMaEPvktvBTSaD8rF-3rL2zcJ7ALfjhsRfygZcttgxNNQx6lJ2Sf9jWKQRwTGzwUfhgmuWHQKaQQYFGM5dyWMhDg1wFQMms9l486EnLOYV6QJ0OBaitMmN4McXt9ZFXQKMOIu35nhQyEJsHqStpkC-n2TJqTinJVh2T4I71_oGqiW1tSRpTOkg-onPJdYVDcQhVQ1p023oSS6hJKZSQcpuZNZG2nf3RyRm9pgNgfDwgsiX8HjrZ14Jk3s0DT9TkB7AfwJLrhCKAZq0QbaGDOG8SE7oFKJOa0V7T_rpQx4GscCmg1OL1AMq0xfQjMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41e56de999.mp4?token=GA4EZlfa1uqOxOhZU-Qzw7HXCdMaEPvktvBTSaD8rF-3rL2zcJ7ALfjhsRfygZcttgxNNQx6lJ2Sf9jWKQRwTGzwUfhgmuWHQKaQQYFGM5dyWMhDg1wFQMms9l486EnLOYV6QJ0OBaitMmN4McXt9ZFXQKMOIu35nhQyEJsHqStpkC-n2TJqTinJVh2T4I71_oGqiW1tSRpTOkg-onPJdYVDcQhVQ1p023oSS6hJKZSQcpuZNZG2nf3RyRm9pgNgfDwgsiX8HjrZ14Jk3s0DT9TkB7AfwJLrhCKAZq0QbaGDOG8SE7oFKJOa0V7T_rpQx4GscCmg1OL1AMq0xfQjMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اتفاقی عجیب جاخالی دادن کامیون سوخت روسی از پهپاد اوکراینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/661469" target="_blank">📅 18:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661468">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMG8Gy_iXwNB6xmUCWCMIB-kJcmzYDnnYRWWzgBMF1zwDXQsURIirGYLDsLE3muolcxb5vC2A2IFKsvoTFpMcYOtvIvHHglwwblq4OeyvEI6xB0318BNZSkp_6fREdSevp783Kq2xXPk9aVcLYIXumMK4VStf13pIxEdG8ltcCzJbGk7CTPBuEXq5nAVIk2Mud-vhxRwkn47V6ON91J0EDVsSBw_u2Xya-FuSkymq3BMOe4lIO_-927e4pUS1uyPD0_onGA2FE3ZhbV3uj-nn_SAb3Fi2S_jFWVSu3pIa3105P5xIJCad-Tn3VC9CI0Y7SLr2sjxqcMYrNv2F6Mxog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج بی‌سابقه حذف حساب‌های اینستاگرام؛ باگ یا سیاست امنیتی جدید متا؟
متأسفانه در روز‌ها و هفته‌های اخیر، گزارش‌های متعددی از غیرفعال شدن و از دسترس خارج شدن حساب‌های اینستاگرام  در نقاط مختلف جهان منتشر شده است؛ موضوعی که صرفاً به کاربران ایرانی محدود نمی‌شود و بسیاری از کاربران در کشورهای مختلف نیز با آن مواجه شده‌اند.
امید مهربان، پژوهشگر حوزه هک و امنیت، در گفت‌وگو با ما می‌گوید: «از زمانی که متا سیاست‌های خود را در زمینه مقابله با حساب‌های جعلی، مجهول‌الهویه، ربات‌گونه و شبکه‌های فعالیت غیرواقعی تشدید کرده، حساسیت سیستم‌های نظارتی این شرکت نیز افزایش یافته است. این روند را پیش‌تر در جریان پاکسازی گسترده حساب‌های غیرواقعی و کاهش میلیون‌ها دنبال‌کننده از صفحات برخی چهره‌های شناخته‌شده مشاهده کردیم.»
به گفته وی، در بسیاری از موارد زمانی که یک حساب به‌عنوان حساب جعلی یا مشکوک شناسایی و غیرفعال می‌شود، ایجاد حساب‌های جدید با مشخصات مشابه می‌تواند ریسک شناسایی مجدد را افزایش دهد. استفاده از نام کاربری مشابه، اطلاعات هویتی یکسان، تصاویر پروفایل تکراری یا الگوهای رفتاری مشابه، ممکن است باعث شود سیستم‌های امنیتی ارتباط میان حساب‌ها را تشخیص دهند و محدودیت‌های بیشتری اعمال شود.
مهربان معتقد است: «بسیاری از کاربران پس از غیرفعال شدن حساب خود، از روی نگرانی و استرس اقدام به ساخت چندین حساب جدید می‌کنند؛ در حالی که این تصمیم در برخی موارد نه‌تنها کمکی به حل مشکل نمی‌کند، بلکه می‌تواند روند بررسی و بازگردانی حساب اصلی را پیچیده‌تر و زمان‌برتر کند.»
او تأکید می‌کند که بهترین راهکار، بررسی دقیق علت غیرفعال شدن حساب و پیگیری اصولی موضوع از مسیرهای رسمی است؛ زیرا تلاش برای دور زدن محدودیت‌ها یا ایجاد حساب‌های متعدد، ممکن است دامنه مشکل را گسترش دهد و ریسک از دست رفتن حساب‌های بیشتری را افزایش دهد.</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/661468" target="_blank">📅 18:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661467">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
ابلاغ دستورالعمل فروش ارز اربعین؛ سهم هر زائر ۲۰۰ هزار دینار
🔹
بانک مرکزی دستورالعمل تأمین و فروش ارز زیارتی اربعین سال ۱۴۰۵ را ابلاغ کرد که بر اساس آن هر متقاضی بالای پنج سال می‌تواند تا سقف ۲۰۰ هزار دینار عراق دریافت کند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/661467" target="_blank">📅 17:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661465">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbHzUdSYnbA4DRv-P_bgIlZRT6hB7zKW5ODSZslqPi2LekroOQrmUpQFqQdHGmxr-yEhkOd-_0uMzVIdBa0GU3Lwpcf37tH_kjGj0_2h_-GxNRnezVkT_o2utIIVCgRKOKFxwg9NkDu5LuarQcL3-xBacYuChStionTY2X5ufd16UKZvP4_pX9B7rKXmT_P3sDAMZ0ENc4StelcIJE47XI7z9RAPR39_L8VZPpxqj3md7v6nc1joXcwxiVpqZc8jA3gGLAfvYHJaVV488oIkpLQouXvg8qlnZLvn1uHd6x9MEIMGywEvIEbXi5ay78j4StTI1mRsmdTtLwUgaqk4cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدام گروه خونی در جهان رایج‌تر است؟
🔹
O+ رایج‌ترین گروه خونی جهان است، اما در اروپا A+ بیشترین سهم را دارد.
🔹
O- می‌تواند به همه خون بدهد، در حالی که AB+ تقریباً از همه دریافت می‌کند.
🔹
توزیع گروه‌های خونی در جهان یکنواخت نیست و هر منطقه الگوی خاص خودش را دارد.
@amarfact</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/661465" target="_blank">📅 17:48 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
