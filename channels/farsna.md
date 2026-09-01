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
<img src="https://cdn4.telesco.pe/file/U3aLflqBG6NJyk7q4Vg-PRRqaGwhBzWGwAynLeJHYFY9Kw3iEffaHLjBQbid81CsF7SFK8N2_EREOAPaTRBrwk6yuae6gJ8WmTiQC2HRZz4eCLNAA1KCf0KZDxe3rJ-_RTXQO57AHJ7lf-JPGHzR5desY-6g-h9fu5gWXYq4p029jBNT9oJbsSzsmM0IWHIBHJ_c7fax5WQm-azkknRZWY_ZNCihxadIdLpHqIDahZ76gPnpNylNMPAUhpSf2x81ed4rYkYOgKLd9rlVBj76ZMthsjrCW2vJ9h6DzrU-2QpssMmP6Pyiwf8gYzkJJlGNusvcGneDfP-MqRp4mkLeWg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 03:11:27</div>
<hr>

<div class="tg-post" id="msg-459602">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‌ انفجارهای مهیب بحرین را لرزاند
🔹
منابع محلی گزارش دادند که پایگاه‌ها و منافع آمریکا در بحرین هدف حملات موشکی و پهپادی گستردۀ ایران قرار گرفته‌اند. @Farsna - Link</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/farsna/459602" target="_blank">📅 02:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459601">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وزارت کشور بحرین با صدور هشداری از شهروندان خود خواست به نزدیک‌ترین پناهگاه یا مکان امن پناه ببرند. @Farsna</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/farsna/459601" target="_blank">📅 02:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459600">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">وزارت کشور بحرین با صدور هشداری از شهروندان خود خواست به نزدیک‌ترین پناهگاه یا مکان امن پناه ببرند.
@Farsna</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/farsna/459600" target="_blank">📅 02:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459599">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/404c7bc669.mp4?token=TUzaRIT7GfaBQ2O4KAgzTGuKTFPKVFdIWDB6znhpMXoawRDNCTAUYGEN6gaNHNakvL-VbbUZAiSyU0J-r5o9elhdq5MXVy2ojrdWhWtLd1PicATAGdLE3SyEHhHogxDopbOEze8axHfTBPs7U1EUcGXZu0abXZYWvERfOlaTFHhrOWNwcA0Q8ahaH1s3Tfr6k823Vy30FNiemiMUspVJaaPJ0XnSq94prerskDTNRb7a7AJDK7IVvvhopuDIorWoHXvQRDCKgzyrAYG4YB37aPYTUlCRB3xv2EQokQAIToO6KxYoIlyVYIuns6cczqpt1BpE36DtLz3f6ZmXHCyXHEuOaz3h3vBRdOJ4qM-YRJm_NxdcWEjWETqEe3bvwxZkujlMdNUnc-4viL6-83V4IIto3cGpLA3j1i82Jnm1Uq2cghq6r89A8WQEnaKd0drL4sbcBRvD7MGgFEpVtVlGzQsB88zblsVM8KFEdyqAVTuYhvKnp88mYg8G4fLlSSQVFjs_7o1QYA2dylYUiBiuRGi9qp4Ky7nRsf0unpDCNOp3ITHVYO4cxx3ByhC8h6kGVN9wv-lLaIh-aYQC9hWck7doWCepsRGB-SGCsEgakQyRfkiH3TxMIpkS8nXS9TDl42N0HDPWWYCVSZ20Wtf0DxhqUSwiiSownjUtnOiZgiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/404c7bc669.mp4?token=TUzaRIT7GfaBQ2O4KAgzTGuKTFPKVFdIWDB6znhpMXoawRDNCTAUYGEN6gaNHNakvL-VbbUZAiSyU0J-r5o9elhdq5MXVy2ojrdWhWtLd1PicATAGdLE3SyEHhHogxDopbOEze8axHfTBPs7U1EUcGXZu0abXZYWvERfOlaTFHhrOWNwcA0Q8ahaH1s3Tfr6k823Vy30FNiemiMUspVJaaPJ0XnSq94prerskDTNRb7a7AJDK7IVvvhopuDIorWoHXvQRDCKgzyrAYG4YB37aPYTUlCRB3xv2EQokQAIToO6KxYoIlyVYIuns6cczqpt1BpE36DtLz3f6ZmXHCyXHEuOaz3h3vBRdOJ4qM-YRJm_NxdcWEjWETqEe3bvwxZkujlMdNUnc-4viL6-83V4IIto3cGpLA3j1i82Jnm1Uq2cghq6r89A8WQEnaKd0drL4sbcBRvD7MGgFEpVtVlGzQsB88zblsVM8KFEdyqAVTuYhvKnp88mYg8G4fLlSSQVFjs_7o1QYA2dylYUiBiuRGi9qp4Ky7nRsf0unpDCNOp3ITHVYO4cxx3ByhC8h6kGVN9wv-lLaIh-aYQC9hWck7doWCepsRGB-SGCsEgakQyRfkiH3TxMIpkS8nXS9TDl42N0HDPWWYCVSZ20Wtf0DxhqUSwiiSownjUtnOiZgiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سپاه: حملۀ سنگین موشک‌های بالستیک به آشیانۀ هواپیماهای بدون سرنشین در اردن؛ تعدادی از پهپادها منهدم و تعدادی از خلبانان و خدمۀ فنی پروازی به هلاکت رسیدند
🔹
روابط‌عمومی سپاه: رزمندگان نیروی هوافضای سپاه پاسداران انقلاب اسلامی در یک حمله سنگین با موشک‌های…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/459599" target="_blank">📅 02:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459598">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
سپاه: پادگان تفنگداران آمریکایی در اردن هدف موشک‌های بالستیک قرار گرفت؛ تعداد زیادی از نیروهای آمریکایی به درک واصل شدند
🔹
روابط عمومی سپاه: ملت قهرمان و بپاخاسته ایران اسلامی، ارتش تروریستی و شکست‌خوردهٔ آمریکا، عاجز از رویارویی مستقیم با رزمندگان اسلام…</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/farsna/459598" target="_blank">📅 02:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459597">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f143426d42.mp4?token=vhaPUrSG_6svMm4LDfE9GYASSATcYT1PmGMIxL5TiiyBDMXJ_MRUitxDNF8MMKcAHm4XE8JZg8AqTzLrMm3CQuYCxHrce7u1pWK113wcOIIT0QR7i6eHgN4tGsHx5Muvoy6TXt5FzuEJO-8GHT_QdrBWeF2URkNQWealf-KPDA9R7uIoqMKHofOD3U_3T1Oeg09Pl4jfadM0cQcRmF80kJhK3UgVmEDaojTqI9R58VQcWZOUiYnrWdm-qc7Wi_Fvk1L0Nim7d_u2RSD3trlI_Wxjkxr9rjhK13PSeRtPCePMk7D52PBg4RjBvEHackmW35S0M8ZIdvGOoE7zXvzRnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f143426d42.mp4?token=vhaPUrSG_6svMm4LDfE9GYASSATcYT1PmGMIxL5TiiyBDMXJ_MRUitxDNF8MMKcAHm4XE8JZg8AqTzLrMm3CQuYCxHrce7u1pWK113wcOIIT0QR7i6eHgN4tGsHx5Muvoy6TXt5FzuEJO-8GHT_QdrBWeF2URkNQWealf-KPDA9R7uIoqMKHofOD3U_3T1Oeg09Pl4jfadM0cQcRmF80kJhK3UgVmEDaojTqI9R58VQcWZOUiYnrWdm-qc7Wi_Fvk1L0Nim7d_u2RSD3trlI_Wxjkxr9rjhK13PSeRtPCePMk7D52PBg4RjBvEHackmW35S0M8ZIdvGOoE7zXvzRnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت شاهد عینی از لحظۀ حمله به جشن عروسی در کوهستک سیریک   @Farsna - Link</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/farsna/459597" target="_blank">📅 02:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459596">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuMprmcBrmuJz4p5AO_LXhKXdchCJ4FY4qa1rWuf3wG2Viryzf-anaUXCFod-ZOae6_y2BlhcUUvQ8FUWIqd62Hid1E8oHPIlfrMsSoOdo4LB6FXzZMLXjbhZ0ZTJPQ85y0QxvvdsVWDysd9hybeawf3oqhTrcfh_6xg_5CqTiKAwm1UY7u2NyadzJb3F13V3amkeB38zbXRa0yuLKCyxEuM9hAIAGRKQUp_k96uHaoz2guwEz5K3apnphhEpi_W1WdfiyLH60Tmjau1idCaMQwdyJIAvzCkbvMB3zbdeKr3-oDliJb4NJrx2-X8t4Q6HXPeOD_dAE5TvPox4iit5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون سیاسی سپاه خطاب به کشورهای منطقه: یا آمریکا را بیرون کنید یا پاسخ کوبنده بگیرید
🔹
سردار جوانی خطاب به کشورهای عربی: بهتر است آمریکایی‌ها را از کشورهای خود بیرون کنید و پایگاه‌ها را پس بگیرید.
🔹
در غیر اینصورت، نیروهای مسلح ایران ثابت کرده‌اند از هر نقطه‌ای در کویت، بحرین، اردن یا هر کشوری که به ایران تهاجم شود، با پاسخ‌های قاطع و کوبنده مواجه خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/farsna/459596" target="_blank">📅 02:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459595">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
منابع عراقی از وقوع انفجار در مواضع آمریکایی‌ها در اربیل خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/459595" target="_blank">📅 01:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459593">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5PbBo8C4chXRviYGG6JcNzGS6BU2zutGlWY8EBzG9Wnlf2xNusVbCxNXzIx3BNlft-FTUtAmwb2SKg7y-4JPgt-Uw0LoRt_ZMTCX02VXc8xNWn1zGZqQOpY57ruOOTYPeZxYu905G_aI447MewRRc_RlCzJtyXzQ6dXh4HQNS0NHT5GgTjEZaddzmHFI1vicdlOydDPt3d3KWBHMqq8EIzMX3uyr2mf7LZzR8BvDt-Ijb1WTbX7HqUhK-kEL8Jv3Niu-Zm6-RtOUyOmCurLD6K6c4Z7OUyYQ-KFiOIhF-iYcyYklPzjmmtJo50PwbKXqArxF-qfRuvyV9KvT8EbWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مخابرات هرمزگان: در حال رفع اختلالات ناشی از حملۀ دشمن هستیم
🔹
اداره‌کل مخابرات استان هرمزگان: در جریان حملات آمریکا به مناطق غیرنظامی و زیرساخت‌های خدماتی در بخش‌هایی از مناطق جنوبی کشور، به تعدادی از دکل‌ها و سایت‌های مخابراتی و اینترنتی خسارات جدی وارد شد.
🔹
عملیات تیم‌های اضطراری برای رفع مشکلات پیش آمده و وصل مجدد شبکۀ مخابرات و اینترنت درحال انجام است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/459593" target="_blank">📅 01:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459592">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
منابع عراقی از وقوع انفجار در مواضع آمریکایی‌ها در اربیل خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/459592" target="_blank">📅 01:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459591">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7sGQu5_erQkkVD1x9lrayAiQQZZYGRJ8hevTedudG9VFGV2WIPhxQFhp_MxYN5fQ0Ews9EF0kpLQoMcopwUJcHm9G7U6NYhMofswtL0SRxgAEKu7303XjfmJ-FVJx5t9Dl2-V97rkl5Qj1BWGJM54tqaPWzywUL2E130AdXhBCg2ZP1l8EReXOX6oYZFF_rCvxmiVfyQgsxqsryZd5dTkvp0PbwttJo4UdbXnDHokii1HrKTdUKFlXllGHlUOqcqRtFHaEMBdSq5exMs2ITILUo_u3CpEB9IYQJdjBHjR7s-jPSFcMZ1Zcit12P5k98hCEirikQ8Y1Gn4fQZnD-1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش بقائی به حملۀ آمریکا به جشن عروسی: هر روز بر سیاهۀ جنایات آمریکا علیه مردم ایران افزوده می‌شود
🔹
سخنگوی وزارت خارجه: فهرست جنایات آمریکا علیه ملت ایران اکنون کامل‌تر از همیشه شد. امشب یک منزل مسکونی در کوهستکِ سیریک، در حالی هدف حمله قرار گرفت که مردم در آن مشغول برگزاری جشن عروسی بودند. بیش از ۵۰ زن، مرد و کودک بی‌گناه شهید و مجروح شدند.
🔹
این قساوت را نمی‌توان از زنجیرۀ حملاتی که پیش از آن در میناب، لامرد، قشم و دیگر نقاط رخ داده است، جدا کرد؛ همان‌طور که نمی‌توان آن را از حمله به اهداف نظامی جدا دانست؛ حملاتی که با برچسب‌ها و توجیهات فریبنده پوشانده شدند.
🔹
خطرناک‌تر از خودِ بمب، عادی‌شدن بمباران است؛ و خطرناک‌تر از سکوت، آن است که سکوت به معنای مشروعیت تعبیر شود.
🔹
ایران به این جنایات وحشیانه قاطعانه پاسخ خواهد داد. اما دولت‌ها و سازمان‌های بین‌المللی که در برابر چنین بربریتی سکوت می‌کنند یا در پی توجیه آن هستند، باید بدانند که سکوتشان بی‌طرفی نیست. وقتی حملات غیرقانونی و جنایات آشکار، به اقتضای مصلحت سیاسی، تطهیر و توجیه می‌شوند، مرز میان محکوم‌کردن جنایت و عادی‌سازی آن از میان می‌رود.
🔹
کسانی که امروز سکوت می‌کنند، فردا خود نیز از پیامدهای این سکوت در امان نخواهند بود، چراکه چشم‌پوشی نسبت به ظلم و جنایت آن را مهار نمی‌کند، بلکه مرتکبان را در ادامۀ جنایاتشان علیه همه جسورتر می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/459591" target="_blank">📅 01:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459590">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
برخی منابع عربی از شنیده‌شدن صدای انفجار و فعال‌شدن پدافند هوایی در کویت خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/459590" target="_blank">📅 01:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459589">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
برخی منابع عربی از شنیده‌شدن صدای انفجار و فعال‌شدن پدافند هوایی در کویت خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/459589" target="_blank">📅 01:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459588">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9849737611.mp4?token=QOt8jiRJ-zvAYzsfPZtAQI5-Nbrjfx_BaVWoo2S5osuwIa2iH-1nqpt04v-X5YxnEiXq37Ui_lbxUIFONyQvry2g9vadKGz1CzVbzKTPNoicgzmVzs8hSzx6Q1O3sc3jBIKkF-S7RedcRxZ7gN2bNRokjgAcaq5Clz5Ghi4n2lR262N7oOavkPVOyt0l4K2V3HguJyzYhJ6um5VuP0mIYoaMRJqjeuwRT9stsMje_YwHvfMCLtgaNqz8ZHaHX78vhksyYKyJZzfRZttK-UyKJaqB68zPRXHtXvoicys76zpWDrYLMZ_NwmxzRx94_G99evFbfjQKkC71QcM-Tw-nTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9849737611.mp4?token=QOt8jiRJ-zvAYzsfPZtAQI5-Nbrjfx_BaVWoo2S5osuwIa2iH-1nqpt04v-X5YxnEiXq37Ui_lbxUIFONyQvry2g9vadKGz1CzVbzKTPNoicgzmVzs8hSzx6Q1O3sc3jBIKkF-S7RedcRxZ7gN2bNRokjgAcaq5Clz5Ghi4n2lR262N7oOavkPVOyt0l4K2V3HguJyzYhJ6um5VuP0mIYoaMRJqjeuwRT9stsMje_YwHvfMCLtgaNqz8ZHaHX78vhksyYKyJZzfRZttK-UyKJaqB68zPRXHtXvoicys76zpWDrYLMZ_NwmxzRx94_G99evFbfjQKkC71QcM-Tw-nTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ اولیۀ حملۀ دشمن آمریکایی به محل برگزاری مراسم عروسی در بندر کوهستک سیریک  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/459588" target="_blank">📅 01:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459587">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3969eedd.mp4?token=urxPRzo8G7jRK20Aegf0Pm16teTD0V16-y0yOcb-tNZglFCRaOYFJAwlNNgNOjMxECCI9UVGcyiKe6vzi7Ided4iowpsdJoRD6gvGT6RqQh1eUQgLBuMmo3ZC0utEO65OVXn0QfDlU5IZJ62w1OergxWvB8Ec0Bnu7uwp0SvDPLT2GulDdRaAwD4CxafDtS8aa1xkSFViUAvdSJu0gIy7D2zHZUNUa9WHDLGjeNfoGJcjIVyAEQDwxb0SwI1p8BpJ6qrNnVHj0j_f-FwGNHWGkzZO5ccoqJExV-hWXKyx_sup0-Xkghb0JHIt9htCeRHRECwSP8a2sK2PeDe6vpAHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3969eedd.mp4?token=urxPRzo8G7jRK20Aegf0Pm16teTD0V16-y0yOcb-tNZglFCRaOYFJAwlNNgNOjMxECCI9UVGcyiKe6vzi7Ided4iowpsdJoRD6gvGT6RqQh1eUQgLBuMmo3ZC0utEO65OVXn0QfDlU5IZJ62w1OergxWvB8Ec0Bnu7uwp0SvDPLT2GulDdRaAwD4CxafDtS8aa1xkSFViUAvdSJu0gIy7D2zHZUNUa9WHDLGjeNfoGJcjIVyAEQDwxb0SwI1p8BpJ6qrNnVHj0j_f-FwGNHWGkzZO5ccoqJExV-hWXKyx_sup0-Xkghb0JHIt9htCeRHRECwSP8a2sK2PeDe6vpAHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌شمار مجروحان حمله به عروسی در کوهستک به ۶۸ نفر رسید
🔹
بنابر اعلام هلال‌احمر، شمار مجروحان حملۀ دشمن آمریکایی به مراسم عروسی در کوهستک سیریک به ۶۸ نفر رسید.
🔹
شمار زیادی از مصدومان کودک هستند که به بیمارستان‌های سیریک و میناب منتقل شده‌اند.
◾️
همچنین تاکنون…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/459587" target="_blank">📅 01:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459586">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BI-U3s7BiQA_GyiUN-SkQhPrrHilQNC6QXOtrSAhI2oSXmIDplHH5S2M9ZDavgWeEn8fpfyzr-NzX6gMpoBosBoM95YLVK0W6EYGkzNeb_geKSg7u7S1btuOmWDGlE2MIFCv-vS0OCoiIodbbCKCtxASvqlFlB3Q840TVoZIgkDh-sPGK0jqoyIk0gWJrQIzEYRqpEGsIWOeyg5xDZH_uSWeYPicnQLShsOhSzI23o-SaQh4QdNc8SugPBFVmhVgg2VmvO7BlEoS8mDUJuBPE0CctvVMWwbaOXgpaYD0simYerlvTrzHozlsvZDZX2YwTsqsuBAg34ru0W3m_AFiKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رئیس کمیسیون امنیت ملی: هدف قراردادن یک عروسی و قتل‌عام مردم بی‌گناه در کوهستک، گواه نهایی استیصال مطلق مدافعان دروغین حقوق‌بشر و تکرار جنایات آن‌ها در میناب و لامرد است.
🔹
این جنایات بدون مجازات نخواهند ماند. هیچ‌چیز آن‌ها را از ارادۀ کوبندۀ نیروهای مسلح ایران محافظت نخواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/459586" target="_blank">📅 01:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459584">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xk99dBMYXzve1hT4bTH676PGERmjHebB2xin3myBvtyTP4E-GW0KwRFncoAUuLAQokc4nvJUNchbz9sIxIkSS4Hr-UO3zk64_7pcxhwCT6sLe1sBPwv4zmBJB-asFcsH_TAQkYvst48UuhkahsEifYyx72GVTN8DbnFhTSxIlc80x4Wy8HA-NMtjB_HWndecv-E0rL6XadRhKeofrHECu9rHidia6KZXMMVWmEr7N-TBM5ml_SRUblU6_8M3vUZqXgb02Ufqf65awQncoW7JviuZTw6yF4Tt5etgvulJbxDnrxIZYw6VzPuag2sSCmdIzErl3pxdld-ORK6_1BPhuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j-Hns17GPu2EmA7SIs11Spp5yppsRtr3E_dTiecDjjR1S1lZ5k-LnRddVYgsNe6CM6kkUmpVcZ8lZXUUB9WkZoHa5yWls4l16WMbpECPsUil9xBxVzfexnmdAJBl10PVH9vge9WGZkRrl1Yfje0aPi7EweifHr6_93N_Nvm3E0pLiigrMN6O-NOIU79Tcx1cT1TosjD9H5dSMZDYYbtTImqHMYbtnTdj1mpPaUuPz7PsXnVg7PBrkd7l9-hynpcMhKA47soOcVJLhjUQPyzjJqTwcLVuh6q5UZMrU3HSd6cuQXCTgyHsCSOZEjLYjcp9Vl436JOpB_df43Lo8Bu-fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌ شمار شهدای حمله به عروسی در سیریک به ۵ نفر رسید
🔹
هلال‌احمر: شمار شهدای حملۀ دشمن آمریکایی به مراسم عروسی در کوهستک سیریک به ۵ نفر رسید و ۵۰ نفر مجروح شده‌اند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/459584" target="_blank">📅 01:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459583">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">برق مناطق آسیب‌دیدۀ قشم وصل شد
🔹
فرماندار قشم از رفع قطعی برق در مناطقی از این شهرستان که در پی حملات شامگاه سه‌شنبه آمریکا دچار خاموشی شده بود، خبر داد و گفت جریان برق اکنون در تمامی نقاط قشم برقرار و پایدار است.
🔹
همچنین عوامل شرکت توزیع برق هرمزگان نیز در تلاش برای وصل کردن برق مناطق مورد حمله در کوهستک سیریک هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/459583" target="_blank">📅 01:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459582">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0635efc59d.mp4?token=eV7VpLejfnDu5uWbbFbZU2x2MZ3IH95acvuA01Hbaoj3AIUJSl9MxvGVCaNpfdPpT2Ok2B0u2-wNwJb-pgbMxMWeZSBf4D-dOli8ES8Ypx1cirfGhR-M2Q0shixkoXnFm7Kzc5nA74-5CTGywu0abNvL95VuoMbQqk5prCMZudpTRYLPhaEBtbazsF9xVx9tD-D3gIr5RaTlvBZsZyTeAW_oufWChWlCFgdChQ939F-8amvtJK0YIj7bRkgRAGUzkrUBXM-lh6Z1_XZgD_0QLX5duotFZ0GXy0q98wZkhXqwhp18CPZoMyWk5X2KAExP4UxkuZo1PZlI1Mww-MkyzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0635efc59d.mp4?token=eV7VpLejfnDu5uWbbFbZU2x2MZ3IH95acvuA01Hbaoj3AIUJSl9MxvGVCaNpfdPpT2Ok2B0u2-wNwJb-pgbMxMWeZSBf4D-dOli8ES8Ypx1cirfGhR-M2Q0shixkoXnFm7Kzc5nA74-5CTGywu0abNvL95VuoMbQqk5prCMZudpTRYLPhaEBtbazsF9xVx9tD-D3gIr5RaTlvBZsZyTeAW_oufWChWlCFgdChQ939F-8amvtJK0YIj7bRkgRAGUzkrUBXM-lh6Z1_XZgD_0QLX5duotFZ0GXy0q98wZkhXqwhp18CPZoMyWk5X2KAExP4UxkuZo1PZlI1Mww-MkyzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظهٔ اصابت موشک به اهداف آمریکایی در اردن  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/459582" target="_blank">📅 01:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459581">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">۴ فوتی و ۱۰ مصدوم در حادثۀ برخورد خودرو با تجمع‌کنندگان در مشهد
🔹
ساعتی قبل یک دستگاه خودروی جنسیس در بلوار وکیل‌آباد مشهد با سرعت بالا منحرف و پس از آن با تجمع‌کنندگان برخورد کرد.
🔹
در این حادثه ۴ نفر فوت و بیش از ۱۰ نفر زخمی شدند. @Farsna - Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/459581" target="_blank">📅 01:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459580">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93e2b5cb22.mp4?token=VR74fYM4HtbCaEhw859FeHnewlMHU4eoJpcAfmm1dZ_dHrCfK5Z9B4KagWoLkZ4KNrWZ4BWElNFXG2J-QoK0hpOVYfMjLlzFHKeoBDzELiv2ukgHpn2mPJ3CXeyaoK_brGfymfzDuRXty7ZVbIj-9DhV5xiBcgb27l0Cvw5PTg7OcnXdCMZyNccMTuBPHQuINNcaNsmtrR5O4Wm9R38II1FDeEGXLHPKpQVy7iZ_M6DIHjAOyrOvudJii1ztBDgUNEngyv7GBZVjp4x5isnXqOkM8nn3epM9dAnn9CteIPKE6LAsgAXRqqy990NtorGkzJIVKkazzxuZCVsLZc3kzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93e2b5cb22.mp4?token=VR74fYM4HtbCaEhw859FeHnewlMHU4eoJpcAfmm1dZ_dHrCfK5Z9B4KagWoLkZ4KNrWZ4BWElNFXG2J-QoK0hpOVYfMjLlzFHKeoBDzELiv2ukgHpn2mPJ3CXeyaoK_brGfymfzDuRXty7ZVbIj-9DhV5xiBcgb27l0Cvw5PTg7OcnXdCMZyNccMTuBPHQuINNcaNsmtrR5O4Wm9R38II1FDeEGXLHPKpQVy7iZ_M6DIHjAOyrOvudJii1ztBDgUNEngyv7GBZVjp4x5isnXqOkM8nn3epM9dAnn9CteIPKE6LAsgAXRqqy990NtorGkzJIVKkazzxuZCVsLZc3kzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حملات پهپادی ارتش به پایگاه‌ آمریکا در بحرین
🔹
روابط‌عمومی ارتش: در بیست‌ونهمین مرحله از عملیات صاعقه و در پاسخ به تجاوز دشمن به مناطق جنوبی کشور، ساعاتی پیش ارتش جمهوری اسلامی ایران، تاسیسات راداری و مراکز تجمع نیروهای تروریست آمریکایی در پایگاه شیخ عیسی بحرین را هدف حملات پر حجم پهپادهای انهدامی قرار داد.
🔹
پایگاه شیخ عیسی بحرین، یکی از مهم‌ترین و حساس‌ترین پایگاه های آمریکا در منطقه خلیج فارس و از مراکز مهم تعمیر و نگهداری بالگردها و قطعات پهپادها و میزبان هواپیماهای شناسایی است.
🔹
رزمندگان ارتش جمهوری اسلامی ایران، به شرارت‌های دشمن، پاسخ کوبنده و گسترده داده و انتقامی سخت و پشیمان کننده از متجاوزان خواهند گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/459580" target="_blank">📅 00:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459579">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🎥
مجروحیت کودکان در حملۀ آمریکا به جشن عروسی در کوهستک
🔹
بیش از ۱۵ کودک حاضر در عروسی کوهستک سیریک در جریان حملۀ آمریکا به این شهر مجروح شدند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/459579" target="_blank">📅 00:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459578">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">شایعۀ حمله به کرمانشاه تکذیب شد
🔹
معاون استانداری کرمانشاه با رد شایعات مطرح‌شده گفت هیچ نقطه‌ای از استان کرمانشاه مورد اصابت دشمن قرار نگرفته و وضعیت در استان کاملاً عادی و تحت کنترل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/459578" target="_blank">📅 00:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459577">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73a48d0c20.mp4?token=epBb4Kyh2UsTtaAUM31-VH2Rh6CRh4q_moGFxL6ZF2G9VSLbZIAv_pCSmVm_OUyYj8MXueVoLMgsedcCxDRetB0rK6nc90epECLalDLQVvK9RNmWLf0P45mx1nEW4MuO5z4hV9phOy01fResLfN2p7jRrD8lQLyG-6twK9lUggWpXeL-UgEs9TiDucR_VXkbdaNsPcPe-CTqUYooD3bWwLNq9v4pJLMMKMi7eryZPGpQiJqom5g2UObuc8soHSoCZ7CcH4D-8bNckCr5bdKw3eJnB0tzyAQ8TT12PqH1oNa8SL7MAjtZlbDKqILR4Wets93eT61KXVNtLIV7CjzpLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73a48d0c20.mp4?token=epBb4Kyh2UsTtaAUM31-VH2Rh6CRh4q_moGFxL6ZF2G9VSLbZIAv_pCSmVm_OUyYj8MXueVoLMgsedcCxDRetB0rK6nc90epECLalDLQVvK9RNmWLf0P45mx1nEW4MuO5z4hV9phOy01fResLfN2p7jRrD8lQLyG-6twK9lUggWpXeL-UgEs9TiDucR_VXkbdaNsPcPe-CTqUYooD3bWwLNq9v4pJLMMKMi7eryZPGpQiJqom5g2UObuc8soHSoCZ7CcH4D-8bNckCr5bdKw3eJnB0tzyAQ8TT12PqH1oNa8SL7MAjtZlbDKqILR4Wets93eT61KXVNtLIV7CjzpLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصاویری از جنایت آمریکا در سیریک
◾️
ساعاتی پیش مراسم عروسی و دو دکل ارتباطی در کوهستک سیریک مورد حملۀ دشمن آمریکایی قرار گرفت که تاکنون ۴ شهید و ۵۰ مجروح داشته است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/459577" target="_blank">📅 00:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459576">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd0f4552b1.mp4?token=FvscptrOTlNv1G-i0n24BMYZvrhaJO0fmBGKK1C_wnPW3bD5_1MNAhSJxlyvdARtEZyknnHXTL6QlbO13WK2M8m8DmFTdTOF0tzqG-SbIh1IKdAdbdnusKKnJBK-k2ZR2CBPMDyuftE1CDqr87bcXPHb_3bHZu3kVPqr55L9EzHo3thJWs9rWw_2r19epbQ-I0uniUIBb4C3CEBiqqvmqhwYHaEqQGa77O0WaYVsYb7DJAVZejA4R3fUBy674CZt9Gk1lmZ4C2jgAqUb4dtiSitbFxbX_OU7tpqw9KW5yL9Y4NuSCNmxYZiEge4-4Jopx3DVESBUw82SKDVxF-Te_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd0f4552b1.mp4?token=FvscptrOTlNv1G-i0n24BMYZvrhaJO0fmBGKK1C_wnPW3bD5_1MNAhSJxlyvdARtEZyknnHXTL6QlbO13WK2M8m8DmFTdTOF0tzqG-SbIh1IKdAdbdnusKKnJBK-k2ZR2CBPMDyuftE1CDqr87bcXPHb_3bHZu3kVPqr55L9EzHo3thJWs9rWw_2r19epbQ-I0uniUIBb4C3CEBiqqvmqhwYHaEqQGa77O0WaYVsYb7DJAVZejA4R3fUBy674CZt9Gk1lmZ4C2jgAqUb4dtiSitbFxbX_OU7tpqw9KW5yL9Y4NuSCNmxYZiEge4-4Jopx3DVESBUw82SKDVxF-Te_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه: پادگان تفنگداران آمریکایی در اردن هدف موشک‌های بالستیک قرار گرفت؛ تعداد زیادی از نیروهای آمریکایی به درک واصل شدند
🔹
روابط عمومی سپاه: ملت قهرمان و بپاخاسته ایران اسلامی، ارتش تروریستی و شکست‌خوردهٔ آمریکا، عاجز از رویارویی مستقیم با رزمندگان اسلام…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/459576" target="_blank">📅 00:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459575">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">۴ فوتی و ۱۰ مصدوم در حادثۀ برخورد خودرو با تجمع‌کنندگان در مشهد
🔹
ساعتی قبل یک دستگاه خودروی جنسیس در بلوار وکیل‌آباد مشهد با سرعت بالا منحرف و پس از آن با تجمع‌کنندگان برخورد کرد.
🔹
در این حادثه ۴ نفر فوت و بیش از ۱۰ نفر زخمی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/459575" target="_blank">📅 00:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459571">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s_PW4mVC6m3ahKunGnus1L9rpYkeybq0gr3-Bl-qeam2Qj9k0S-G6A8OpaBH5SifUrPQhjltm16_Ys7TIZtthf1sBprH_4IQYMrXzeGmSXtIyq43BtUGX_uVTCbqc4DVkWoFkSblhuXlSsx1Seqmgokeitx6WQX-0v6tHIxs5xFS9M5Vj9Bz2NoFujjfcRpVaZBxl8Ad_vZmN1oc5kw-AW4bYA6ORys1uXqp6PapP3X-EK_g2kCWW2rTzWHCNjC25QjThdbRpqclO4vVupISagHQP2xq81uLT3QCltJkJgeXU0AbbA-Q8CNkeZz1sP52xVbjW5EyDfV40bp2OpIglg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S37qn6SVsAMrjoZ4yonlD-8iALhbJiiV7QkiOZJREJgxnMxeJRTjOEiXXchFSntL3SDq82BeGGkv1RA0gKczgctPshIWkUODnw7Cy0cvIl3yULTTy2F4MTXs-9fQ-pfj1FCHSjzqPWNU_fIPra5o5v8NnxzeOPbXXvT0oqH1MGQVvA3OJbs4C4rORWIQd9trOPvp-OKxLJn8k8fXO8xFeqtuSmZ5uk7IjhnpTDXeGCU9DVTOMPTRAh5MKo1ukkblOOs09Vrx7f5Zbbl0aafXkzfXxXCVcvgAN-rmRbtOoHdoVd6KLDjTFXGspZ7CsEgVtsT7hINEjnEnN7HyrDu8kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U6-xIbTEdw9VLyx7rzqWTOjuL6SD363BaQ8Vyt1Kqaxwzy8phCRPl88EGQ567X2wDPFG0Pe5I3U0FvWcZtsYZNcFW5feVZX5y7hPBgJN6BRf2X5SNo4Rp1hfJQDVVeW_4cj8dNWu915QVInJmY109dCe3HfZ-I9TBKqBSB3zvLhXNvbq-e2BBmj5fAu7Z0BTeIfwz-cbOD6roMtQmLRKV2AXkWJQCHwPOb28OE2no0ULBXnaMXqMaTjLn2KZM6Uj4Mo1VBhCpVG0uzLoJROiLkx6d5QmBXB2NJvwszDN343EMrUi-FzPrBpn71GOVJkoCgwB2is5-AmsWkxDHnUhbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fSvH4GHANxufwKTLcIW3MaAhfF5LyoY7bYfWL2DlZI561ixRF338Qa1K5W8hA6jxpiJp6aR1yTK_LgQwArQVdBVQ8saRi0GsKhFMmWROnYhx8XbeLx3JQxgTuJvpgut6lwTIzDjWf1xJXqf9qjVVJBMlONG7oO1gj0M20H6FX4aptHsmQ6wO5F27WRe7Bf5sDUM2sJEDPw2n-cttBCdmFTReWmTomoDe9KlwIoV9mc_0SfHJov5azuU0mo3JH2dVciot3lTtxs5Yv7GrwybmZwBMkTY_LDcbvY44DmKPpRzGJRZJPR5DyeF2FUxmfq3y9M8F8aBNsDsudriaNBVPmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
تصاویر دیگری از جنایت آمریکا در سیریک  @Farsna - Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/459571" target="_blank">📅 00:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459569">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b69d034784.mp4?token=KErlguA7UeE1i6NPo0LPFJu27xMA-J65d8ic16MBGx3hKGmZIbB9tWbRRikEAWvLbuFIJulwITsevNTBuDoiXgBo3by56lxSSJVr9J-oJ2HEx-evr7htvX2GFz2xHXdbmPlTqHCs8qaCOsHsYR-PMLFNoxy58bAoaDmPhx3etl1R5yIbw4s-jlUrVxOJmuUllcxgPSlk-Mpxoh6PZ98DBnkNWbuOATKeKllZm1Klo8s0NwpqzpVlU15fm7MdEGI8ZDBae69zuNBZB_eGHAYNtFzhIkSdpFt3oMl3taRq8i3HqEeiT0gOgpD7EZEHYtPQ4vz21lHzpFogL-mj2V3OFhDVCJzhbI6JeTVAiGV8rgIiYRkYtByG_-ystHVUdm-fUCN8fdVLYdTa50aCqmji-vq2cZJWXWp1MXHVuYyHi2ozgLB6DZWo6sAmLOT7R4lybep9n9EvoB1RX3vQKG-lRDAVfR6xCzGHEgkQCk7wj7j5Oj6gFWfMwYLcKu-8lqpgAj1YF8o3GOuUrVkkYJFA-yPgTOKtSlmkkpTkjzImifQAn0RQPTUeXG1YDQ3yqrH3wT0G1zv2UOn27AVlaO5sQgq-wQ7B9IlIL1G65ChO6Ff6qzpziOKFaVJyVkDTicsWty0oDZs46LgUcIUFWhEu9wN1680Rgxzj_-6zqu-1-Y4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b69d034784.mp4?token=KErlguA7UeE1i6NPo0LPFJu27xMA-J65d8ic16MBGx3hKGmZIbB9tWbRRikEAWvLbuFIJulwITsevNTBuDoiXgBo3by56lxSSJVr9J-oJ2HEx-evr7htvX2GFz2xHXdbmPlTqHCs8qaCOsHsYR-PMLFNoxy58bAoaDmPhx3etl1R5yIbw4s-jlUrVxOJmuUllcxgPSlk-Mpxoh6PZ98DBnkNWbuOATKeKllZm1Klo8s0NwpqzpVlU15fm7MdEGI8ZDBae69zuNBZB_eGHAYNtFzhIkSdpFt3oMl3taRq8i3HqEeiT0gOgpD7EZEHYtPQ4vz21lHzpFogL-mj2V3OFhDVCJzhbI6JeTVAiGV8rgIiYRkYtByG_-ystHVUdm-fUCN8fdVLYdTa50aCqmji-vq2cZJWXWp1MXHVuYyHi2ozgLB6DZWo6sAmLOT7R4lybep9n9EvoB1RX3vQKG-lRDAVfR6xCzGHEgkQCk7wj7j5Oj6gFWfMwYLcKu-8lqpgAj1YF8o3GOuUrVkkYJFA-yPgTOKtSlmkkpTkjzImifQAn0RQPTUeXG1YDQ3yqrH3wT0G1zv2UOn27AVlaO5sQgq-wQ7B9IlIL1G65ChO6Ff6qzpziOKFaVJyVkDTicsWty0oDZs46LgUcIUFWhEu9wN1680Rgxzj_-6zqu-1-Y4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه: پادگان تفنگداران آمریکایی در اردن هدف موشک‌های بالستیک قرار گرفت؛ تعداد زیادی از نیروهای آمریکایی به درک واصل شدند
🔹
روابط عمومی سپاه: ملت قهرمان و بپاخاسته ایران اسلامی، ارتش تروریستی و شکست‌خوردهٔ آمریکا، عاجز از رویارویی مستقیم با رزمندگان اسلام…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/459569" target="_blank">📅 00:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459568">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMoZYnWSoe_62j-M9j-uAimEK5xZ5U0kPYpgxtnNJjoQ3jbIHWNk0731DJK6rTkY5xgxNGndGOFq8Lbn5cl8wDeG_zs_kJ-1reRqVqUo-eNiVK56-Wh8xGLEtxs9q6LwV0cw1Ya_-pxgj9219chgQrT65gdd8WQFgByjEmBKTo6Dz2BrsCQZ3EBpLckG7ZFC1UFMZk64QUim3391wCvjZa2CfCLyOJ4WBMm48yI8N-qK7pjj_FmuC9whfUSeGQPrNGuOQ8yzGM5NOBFhdrtAtfMFTBIFG0aZ91B7Lbc2VY32m4xLFVn-J3nl7KZNwtaYzxmehvEMjHvCX2D0ZEaC1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رهبر انقلاب: ملّت عزیز ایران و جبههٔ مقاومت، درس‌های فراموش‌نشدنی برای دشمن آمریکایی دارد.
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/459568" target="_blank">📅 00:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459567">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
سپاه: پادگان تفنگداران آمریکایی در اردن هدف موشک‌های بالستیک قرار گرفت؛ تعداد زیادی از نیروهای آمریکایی به درک واصل شدند
🔹
روابط عمومی سپاه: ملت قهرمان و بپاخاسته ایران اسلامی، ارتش تروریستی و شکست‌خوردهٔ آمریکا، عاجز از رویارویی مستقیم با رزمندگان اسلام با حمله وحشیانه به یک منزل مسکونی در سیریک، محل مجلس عقد دو جوان پاک را به خاک و خون کشیده و با به شهادت رساندن و مجروح‌کردن نزدیک به ۵۰ نفر از مردم عزیزمان خاطرهٔ وحشیگری مدرسه میناب و ورزشگاه لامرد را زنده کرد.
🔹
رژیم کودک‌کش آمریکا در این حمله جنایتکارانه یک بار دیگر با به شهادت رساندن چندین نفر از جمله یک کودک، عمق کینه‌توزی و دشمنی خود با مردم ایران را آشکار کرد.
🔹
در پاسخ به این شرارت سبعانه، رزمندگان دلیر نیروی هوافضای سپاه در موج دوم عملیات تنبیه متجاوز با رمز مقدس یا رسول‌الله(ص) با حملهٔ سنگین موشک‌های بالستیک به پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تیتین، واقع در سواحل خلیج عقبه، تعداد زیادی از نیروهای آمریکایی را به درک واصل و چند تاسیسات مهم و بالگردهای هجومی دشمن را منهدم نمودند.
🔹
عملیات انتقامی نیروهای اسلام ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/459567" target="_blank">📅 00:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459566">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ad153b05.mp4?token=fBTdem3wQ-e8_upsofxDbR4wLfFiRV96kFsrtqNMdZDXlpxjfRs_ZNKXmCVcyqjK7eL9xYgA3fox4LWrgWasQATEhWj3qRel4Pfv7gFkSnPtUKRzlfVAML_qHiCBSHJjbibDe-BPnoqk7KUUUCnh_4DvdF8GquKmaTBwFr1086i78MaXCBWCKbfpZ2cEjLWTBtXFSl9sJHcn3W1t3_fOvebMCtr8BNcTPSucKdqQT1i0xhNdJ_NUEoiWIgFxYs0WzSfn2f15PTWUBFqn-QOXVf21XSo_32fJscf6a8Cmg8SaRXr5r562jpKRCOh_5ToJiN-BR9acaqjCUXD4-TSnRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ad153b05.mp4?token=fBTdem3wQ-e8_upsofxDbR4wLfFiRV96kFsrtqNMdZDXlpxjfRs_ZNKXmCVcyqjK7eL9xYgA3fox4LWrgWasQATEhWj3qRel4Pfv7gFkSnPtUKRzlfVAML_qHiCBSHJjbibDe-BPnoqk7KUUUCnh_4DvdF8GquKmaTBwFr1086i78MaXCBWCKbfpZ2cEjLWTBtXFSl9sJHcn3W1t3_fOvebMCtr8BNcTPSucKdqQT1i0xhNdJ_NUEoiWIgFxYs0WzSfn2f15PTWUBFqn-QOXVf21XSo_32fJscf6a8Cmg8SaRXr5r562jpKRCOh_5ToJiN-BR9acaqjCUXD4-TSnRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاین در شب ۱۸۵، قرار عاشقانهٔ مردم را رقم زد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/459566" target="_blank">📅 00:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459564">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EcD3DgACwGkXx29_2fELfzKoymcQfFXTamkR0xdiAopSpNIFAP7pWxqaKEjndKQ-p7yfD43c4WRc-1mf87U2fnSujH0Zj0shwY7P5DDTct5GAKOmuSrkjhCDfifis4MC2yA-LTd94zMAW8fOV9ZB2lIvtJh00gzhJEBhMM2-42NL2rJv6C1ErEmed4EmhChYdrcLzJq7kxFN3cX9r4y1i7DCjw7w4vuAAiPLpLtqRbgBfAkmXnvQeYQfwLh5bWkZXJR6c6uoLPvXWv3t9eJwW880Ahhcz51U4ZIdbsYBAY89xfLcDduvt05qjGJLs0cfHCrcaOqj-MkVmMLkjEuecA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AngxF6Dc5x6VzVKaX1n1e5pvEyKcy_iWvw_FiMqsVHZwlSx1Ti-39btKt61oONrk3j9eH7duVg4Ity8jn-RReucZsZ_8RzV2ipmnIT3oTQruu_4yO7zyWwgsUYomc5lEKgQaqyyRNa1Q29X7T4ihmP421jgcQGfcv9E1TZDP_h9rWiprIfEiIuYKJb7ID3Dve-GGJkG8URnMW25Nr--5HGqzor6uAiaKAnNwmhmZLvJOVW19PGjWIleq4Xu6rowtDJbJ_E6YFxlxE85uV-N6OHmuhBSKbl7OPS9ds7S_CmgwdnA9OfbOAgDFzaB0LLD2XM3RCEYu8VIpHxdze78BiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌
🔴
افزایش شمار شهدای جنایت آمریکا در کوهستک به ۴ نفر؛  یک کودک خردسال در بین شهدا
🔹
هلال احمر هرمزگان: در پی حملهٔ موشکی آمریکا و اصابت ترکش به یک منزل مسکونی در روستای کوهستک از توابع شهرستان سیریک در استان هرمزگان، که مراسم جشن عروسی در آن در حال برگزاری…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/459564" target="_blank">📅 00:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459563">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/861251ffab.mp4?token=eityLSgihF0ZtI294-0bgSFK15qIoAJw0viD5SnVztH3Xyp31-cRswWdSszyn1tweYs5o0JKaPvpXpbfv7bfioDjDq3Q3uHhOgraZFnOlQ0zVpCt3bZgANr_9bElQqcac2-q2SvVv1ZpP1RrDpoEgLao1fjRvwfp7TAPs6cSjO5Td_Oytru5sWlOduEjnpKTianVOPldSDDmjB7Wus8b0vxDB0vt7uEpRPjK9mNmtOciaXNrKCp06cPTmYVC9WlecPMuFdin8FSAOJ96ERks-jBY3d62Q6n8vtvg_X7hzphOY6R0COzgefIuNapphJz_QeEjQmuJatfndHKL8jcFAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/861251ffab.mp4?token=eityLSgihF0ZtI294-0bgSFK15qIoAJw0viD5SnVztH3Xyp31-cRswWdSszyn1tweYs5o0JKaPvpXpbfv7bfioDjDq3Q3uHhOgraZFnOlQ0zVpCt3bZgANr_9bElQqcac2-q2SvVv1ZpP1RrDpoEgLao1fjRvwfp7TAPs6cSjO5Td_Oytru5sWlOduEjnpKTianVOPldSDDmjB7Wus8b0vxDB0vt7uEpRPjK9mNmtOciaXNrKCp06cPTmYVC9WlecPMuFdin8FSAOJ96ERks-jBY3d62Q6n8vtvg_X7hzphOY6R0COzgefIuNapphJz_QeEjQmuJatfndHKL8jcFAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خرم‌‌آبادی‌ها: ای ارتش ای سپاه، بزن بزن ماشاءالله
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/459563" target="_blank">📅 23:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459562">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87d9ddf473.mp4?token=FCQmX5nnPY9Bf6uFZnLLobL94k5Q2TtUsxdBhwjSQsNCsj0x0jxOhNoNa00RGjBUxMRdLEt4laYu4NONXFpqdRKFD5pgk1LazTQPCn0r9Aqd7_e1XMK9fv-c5fb8Vz_7BHAvK_1vO9V6PzYdQEj5Yzlk0AVm-mAsXuE0i7PcNJvVTDq6XeUl8OBWA992ZZmfvcopRx8pyxti5cY6KKcRRHXnxBXz2MAnHgvsIt40PnMLMlJmdNtenkOHFmnZNDI0Elr0e774hAficTd5ieEz5zMMV-1ll2ODZAykZOD2tjdTIRcFyG1ISENHiSGXh2coadjmU6mse72_-N5lOMjBFTDfj5rlvRzJvHwFX2Rx2InjRyOb4xO5b52p68bmcbGXsVTx8IX6fsHYpCV-3hacDeyORzm3nodavk03dcJd6MInj90BJ4BcytAA_ahrqL6BnUB0IbQaiVddHrT4TM_6y8BHlVM9w8l8bUJf9uQYV3glohFdqJCenQUNaPQbXovG1nVazAroWQlxbyurkDYAcsOhTe04E-5-3qz4wJdBPzs6qzehlAmUlhLBMYn29WOa5_IWrJ6LUGXYsjSraoRdj_wH50a7fsAragnx-fkbp83wwYbshLz3EAxg_UKXvuQd33FKTa3Tkeo-Kxusu4LkXPKTIZaJsK6iDiACNFW4sOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87d9ddf473.mp4?token=FCQmX5nnPY9Bf6uFZnLLobL94k5Q2TtUsxdBhwjSQsNCsj0x0jxOhNoNa00RGjBUxMRdLEt4laYu4NONXFpqdRKFD5pgk1LazTQPCn0r9Aqd7_e1XMK9fv-c5fb8Vz_7BHAvK_1vO9V6PzYdQEj5Yzlk0AVm-mAsXuE0i7PcNJvVTDq6XeUl8OBWA992ZZmfvcopRx8pyxti5cY6KKcRRHXnxBXz2MAnHgvsIt40PnMLMlJmdNtenkOHFmnZNDI0Elr0e774hAficTd5ieEz5zMMV-1ll2ODZAykZOD2tjdTIRcFyG1ISENHiSGXh2coadjmU6mse72_-N5lOMjBFTDfj5rlvRzJvHwFX2Rx2InjRyOb4xO5b52p68bmcbGXsVTx8IX6fsHYpCV-3hacDeyORzm3nodavk03dcJd6MInj90BJ4BcytAA_ahrqL6BnUB0IbQaiVddHrT4TM_6y8BHlVM9w8l8bUJf9uQYV3glohFdqJCenQUNaPQbXovG1nVazAroWQlxbyurkDYAcsOhTe04E-5-3qz4wJdBPzs6qzehlAmUlhLBMYn29WOa5_IWrJ6LUGXYsjSraoRdj_wH50a7fsAragnx-fkbp83wwYbshLz3EAxg_UKXvuQd33FKTa3Tkeo-Kxusu4LkXPKTIZaJsK6iDiACNFW4sOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اراکی‌ها در شب ۱۸۵: خلیج فارس تا ابد خلیج ایرانی است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/459562" target="_blank">📅 23:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459561">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGCaMzeXXx8regOr9ja4W45r-IhZyTKtpIgoaT4NgOlfQ_x8qDhMKflfGdNPxXaEpIjsWOxNLkqkVK2vgSPBdFTz5CmPZzJwV5OVpeJ9KiILYr7tTju3L9u8Dk4Uh6w9TftSQFeJiexlnTMqEfU8lyiy39bio8NCVRBRw01OY5Tr9-cMkg5mpilxyOk8-xtts8o0cOaS9SY3n9zOsyH-_CZtTRqEXp5r5_fgZ2Phmcis2kvb_3F5p02d9TrCaRenBYadG2XQCWFn1Smqeya31COxRy4_EsYxoxHr5Q0dm6Gns4rQvGE2yXHZ7yEuwr0sCaKdkA9AsoDb8ZbGIE9ppQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت گشایش‌های تازه؛ از دارو و انرژی تا زیرساخت و حمایت اجتماعی
🔹
روزگار ما، روزگار دوگانه‌هاست؛ از یک‌سو موج‌های ناامیدی و از سوی دیگر، تلاش‌هایی که بی‌سروصدا در گوشه و کنار کشور ادامه دارد. در کنار چالش‌های موجود، طرح‌های مختلفی در حوزه تولید، انرژی، فناوری،…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/459561" target="_blank">📅 23:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459560">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1042a89ac9.mp4?token=dBLqer4E2ktc5n9kXmeuBNqCyqNQoyqEidrclmEWH1lWRMFCX0KgPMSVIxGSYmNpaLmM-JslxEV5rZ2XkqKaoNq4cNtqPpNMPnWiOgFvcRpsOLleb1vBc8upGJBQ1LpThy_zvB99pimywdXKA1-9EgX9RHTboRZjdyx6vgljuOpxJ1LQRUInDwYwNeXN86nvZkvROvft8JFhshL8eZQ00I_RekTY8TD2g2Z5Gx993g7FD6scJKBaSsmDu7cw_ucWER6_JQRkf7rt57u13iq50OgC6LN3QAxOUvRPG6hx0oWgWvsUqB3oLXEQNZpQduv8NOUpFrera1A7LB5Ta9mLLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1042a89ac9.mp4?token=dBLqer4E2ktc5n9kXmeuBNqCyqNQoyqEidrclmEWH1lWRMFCX0KgPMSVIxGSYmNpaLmM-JslxEV5rZ2XkqKaoNq4cNtqPpNMPnWiOgFvcRpsOLleb1vBc8upGJBQ1LpThy_zvB99pimywdXKA1-9EgX9RHTboRZjdyx6vgljuOpxJ1LQRUInDwYwNeXN86nvZkvROvft8JFhshL8eZQ00I_RekTY8TD2g2Z5Gx993g7FD6scJKBaSsmDu7cw_ucWER6_JQRkf7rt57u13iq50OgC6LN3QAxOUvRPG6hx0oWgWvsUqB3oLXEQNZpQduv8NOUpFrera1A7LB5Ta9mLLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از محل عروسی در بندر کوهستک که هدف حمله آمریکا قرار گرفت  @Farsna - Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/459560" target="_blank">📅 23:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459559">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار از پایگاه‌های آمریکایی در اردن خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/459559" target="_blank">📅 23:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459558">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‌
🔴
افزایش شمار مجروحان حملهٔ آمریکا به مراسم عروسی کوهستک به ۵۰ نفر
🔹
معاون امنیتی استانداری هرمزگان:  در پی این حمله تاکنون ۲ نفر به شهادت رسیده و ۵۰ نفر نیز مصدوم شده‌اند.
🔸
با توجه به وضعیت برخی مصدومان، احتمال افزایش شمار شهدا وجود دارد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/459558" target="_blank">📅 23:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459557">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/484a9459e9.mp4?token=hvlnpcOn6hNBOmD1dN4_mkenVkA8Kee6oWBSK6M9FGFxUeNDEafmhpMQXB7mzF5vKDdHuvSmEnik753Z5XOe6CZLUmm6i21uX2z9J4o3qJZ07gJaFQeze3a-IeW3vym-M5tpsLQWsJi0Q8BfbdJzExGK_6N8Oeb9zo3QYjEel1E64ADzwXxcmbnOlS0ueeZ1K0n_q0Pv30XWbZaOJ7fVQSReCUh4IX3lwAt1n2lgrRQv8JMLouvMFrB-qjjVAW8uarZxeumMGfmzIMTO6DnDKCh_0miNJUNNuA6anK3cD9fYMIDI72re_o4ZKfhIr7K9FxT7sCX2HSmHMzRjCL7mzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/484a9459e9.mp4?token=hvlnpcOn6hNBOmD1dN4_mkenVkA8Kee6oWBSK6M9FGFxUeNDEafmhpMQXB7mzF5vKDdHuvSmEnik753Z5XOe6CZLUmm6i21uX2z9J4o3qJZ07gJaFQeze3a-IeW3vym-M5tpsLQWsJi0Q8BfbdJzExGK_6N8Oeb9zo3QYjEel1E64ADzwXxcmbnOlS0ueeZ1K0n_q0Pv30XWbZaOJ7fVQSReCUh4IX3lwAt1n2lgrRQv8JMLouvMFrB-qjjVAW8uarZxeumMGfmzIMTO6DnDKCh_0miNJUNNuA6anK3cD9fYMIDI72re_o4ZKfhIr7K9FxT7sCX2HSmHMzRjCL7mzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بافقی‌ها هم‌قدم با ایران قوی به میدان آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/459557" target="_blank">📅 23:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459556">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39bd610791.mp4?token=NKv342M1U3ZQdVAgfdG6401sYdhC2mSZVn9ETIoy2t9TQtabRx0zhxZ_X5jaaxawTKRvg7fc1QQK1kOH2hBANTSBCoWyECUWEwKYnDd874rz1CffkuSqU7WPz5gplpoVtZm_47AGLrdkVUqhs0u3oa29J4i6DmfPwyBTfh2ps1iEszUuor76u90j6QX5bR7JUUG-HOqVgrDohr3yNKMP9BD-xzgJtSw-7dQ0nX2Yi7rvNtAT1iKuDM7eKhYJtgErH18fRy0mfyMHCAiYLFG5Q8J59qSdZarxcelpQL8DXgeToFWGZU5qEB0gSx6zZFjZdMZ3Ru4OJIN-zJ15hlT3Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39bd610791.mp4?token=NKv342M1U3ZQdVAgfdG6401sYdhC2mSZVn9ETIoy2t9TQtabRx0zhxZ_X5jaaxawTKRvg7fc1QQK1kOH2hBANTSBCoWyECUWEwKYnDd874rz1CffkuSqU7WPz5gplpoVtZm_47AGLrdkVUqhs0u3oa29J4i6DmfPwyBTfh2ps1iEszUuor76u90j6QX5bR7JUUG-HOqVgrDohr3yNKMP9BD-xzgJtSw-7dQ0nX2Yi7rvNtAT1iKuDM7eKhYJtgErH18fRy0mfyMHCAiYLFG5Q8J59qSdZarxcelpQL8DXgeToFWGZU5qEB0gSx6zZFjZdMZ3Ru4OJIN-zJ15hlT3Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم همدان امشب با شعار مرگ بر اسرائیل به میدان آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/459556" target="_blank">📅 23:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459554">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9740e69e4.mp4?token=SDksmspTStUG0fJ-LxRSL5NOrRn0gSlvesnUU28FkAo5LXOfVOyNPKlOOczhhgFrjFSM2xZGdvVxAF4jpum6XnRlmxVcH6e0DFXwhCAO5NtBdMrfdtupNQMkwWOSPEeGUmgNu0v6IVkuAyyrP36Q431FoTsvZWXillTSqetZ158AEekQXqMbQXqn7wYEX-2xElCYwBjpfTtoSV7qR5PCqf4L3ddm6qmW3VbW66EjWlLOFq44SXYa9c7kSkF9fXdAEdYYCJbwKBx2YeWGKNKy-26TwzDcr7Ioe7HXisV4fW6pQ2Cm-mt7GNDZ09krwcEbpM1VKJlx06WaZ_z2E_kMag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9740e69e4.mp4?token=SDksmspTStUG0fJ-LxRSL5NOrRn0gSlvesnUU28FkAo5LXOfVOyNPKlOOczhhgFrjFSM2xZGdvVxAF4jpum6XnRlmxVcH6e0DFXwhCAO5NtBdMrfdtupNQMkwWOSPEeGUmgNu0v6IVkuAyyrP36Q431FoTsvZWXillTSqetZ158AEekQXqMbQXqn7wYEX-2xElCYwBjpfTtoSV7qR5PCqf4L3ddm6qmW3VbW66EjWlLOFq44SXYa9c7kSkF9fXdAEdYYCJbwKBx2YeWGKNKy-26TwzDcr7Ioe7HXisV4fW6pQ2Cm-mt7GNDZ09krwcEbpM1VKJlx06WaZ_z2E_kMag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
افزایش شمار مجروحان حملهٔ آمریکا به مراسم عروسی کوهستک به ۵۰ نفر
🔹
معاون امنیتی استانداری هرمزگان:  در پی این حمله تاکنون ۲ نفر به شهادت رسیده و ۵۰ نفر نیز مصدوم شده‌اند.
🔸
با توجه به وضعیت برخی مصدومان، احتمال افزایش شمار شهدا وجود دارد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/459554" target="_blank">📅 23:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459553">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgR0zPexpb2LxzPXI6JtZP_ZwSLN-h15l3bps1uqAxDL6TI9BcF91JOfZVs7LEFpSVj3D87MjW2e8mC2dj07dP1t3WJ9fwrFQJcIf9ALk3HsL65LPgirCp9NHLO-TG1ONq2kt62sV2r_hmH_AiEAisenvlFj-crVQydCdmWRJXDnIq3s1_OM7FFUUtJetOiWjdvahMEJY5xEMVK-yeqq6iXG25PH5ACASqvYRiI0yBRaWWXwGLRtgZlvKy9a3VlzsROtC99vhsqnPCaNKvFK0_gVP62gllktwWWBpDU-vWUNrKBWwA48rR9YIeucWJeUMMGcDDnTTGQYoMYLSn4Z4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی ارتش: انتقام شرارت و تجاوز از دشمن گرفته می‌شود
🔹
سریع، کوبنده و گسترده.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/459553" target="_blank">📅 23:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459552">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‌ ۲ شهید و ۲۰ زخمی در حملهٔ آمریکا به مراسم عروسی در سیریک
🔹
معاون امنیتی استانداری هرمزگان: در حملهٔ آمریکا به یک مراسم عروسی در کوهستک سیریک، تاکنون ۲ نفر شهید و تعدادی مجروح شده‌اند.
🔹
مدیرکل هلال‌احمر هرمزگان نیز از انتقال حدود ۲۰ مجروح به مراکز درمانی…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/459552" target="_blank">📅 23:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459551">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار از پایگاه‌های آمریکایی در اردن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/459551" target="_blank">📅 23:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459550">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
حملهٔ موشکی آمریکا به اطراف شهر اهواز
🔹
معاون امنیتی استانداری خوزستان: نقطه‌ای در اطراف شهر اهواز توسط دشمن تروریستی آمریکا مورد حمله موشکی قرار گرفت.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/459550" target="_blank">📅 23:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459548">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‌
🔴
تکمیلی؛ حملۀ دشمن آمریکایی به یک عروسی در کوهستک
🔹
معاون امنیتی استاندار هرمزگان از حملۀ دشمن جنایتکار آمریکایی به یک منزل مسکونی و مراسم عروسی در شهر کوهستک سیریک خبر داد.
🔹
بلافاصله بعد از وقوع حادثه نیروهای امدادی به محل اعزام شده‌اند؛ جزئیات حادثه…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farsna/459548" target="_blank">📅 22:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459547">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/960eed7922.mp4?token=NPcBUly8NYzu_iF1d2LGe-LRHR2eDOXueDbwX7-nzpUF-Kgfb6ZQQx-q1fecfLBM2mg3Ka3fOS6jSwIqk11cxPNoelq43aTkWaLljU4SwG8yG78eHZDhIG3po8v5Y3W9Pp1xrPBQJTdqFdQatqjI7XxkMT4obv0dp5X-O4h9nCm06UGRr6oTSkCHpy7xsR4r06-F8huqH-DqxHqTpK0fhe-F__lJJSqDGsVRZBnlP3WGncQbS020cmgN5H4vVtdGBSctkKYDz_8874dAKeVxK6gALQf0JlGQVt-A3GFGMIhq4NrcVv3xjyzg_pObuL2IlAI4h9GK5EWmcjPo1mOihA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/960eed7922.mp4?token=NPcBUly8NYzu_iF1d2LGe-LRHR2eDOXueDbwX7-nzpUF-Kgfb6ZQQx-q1fecfLBM2mg3Ka3fOS6jSwIqk11cxPNoelq43aTkWaLljU4SwG8yG78eHZDhIG3po8v5Y3W9Pp1xrPBQJTdqFdQatqjI7XxkMT4obv0dp5X-O4h9nCm06UGRr6oTSkCHpy7xsR4r06-F8huqH-DqxHqTpK0fhe-F__lJJSqDGsVRZBnlP3WGncQbS020cmgN5H4vVtdGBSctkKYDz_8874dAKeVxK6gALQf0JlGQVt-A3GFGMIhq4NrcVv3xjyzg_pObuL2IlAI4h9GK5EWmcjPo1mOihA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیام مردم شهرکرد به رئیس‌جمهور آمریکا در شب ۱۸۵
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farsna/459547" target="_blank">📅 22:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459546">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e38c8c8a60.mp4?token=ne9s8PxKefd1JR_h40lWpdMURoyefVFnxM8hzssK8Km0XtaZfX0uUzhAS9Xb2alPgM7GMKT2iek9w-eUQay_Mu4Z8qaKA_9KhVuGd8V0q86S8MnCzcr3XesSLFaCcbPEJtxS2FutflgjWnJRxQlquTIcjwvSCGqhae7J_hL68jhkFi9ufV3FztQ7BpoQQQLWiwziaHz1DgbT_bU8FFhDnapFCSrot2fJxtpYrbxEcwbBjLc6dU0Y27ajhrEJxBIFaqLJnab1q9t7wsjgzZzXBoq-ubjfnlZQ-EhkA9G8-kchbGKeojaKN4jh_gNvtsHrAujFUqejmA5BOgyIcjhUblpMnTFIW_npg4l4SK0en8kPHwMxTmV5YpootlTfkv4UGsMwiy_hpSJeIF69maG9ZZSkrNt0z_rmqXhW0JmZBbwkIuoKohxNvVDPN4kW3kybt4NLbzFN4xdaFs_YJnF4S2OqvcvE38GKDnD6Wj2oHJVio86stdbuEjmUxIHQC7u0WK6Bf7Uc00zj8N-RXs9BC1NTip3P1GAhWlAT1xnMpDuHnNBp9hVWHyKSE5ymFD4U7YhbAbnDIvkxZ6yLN5zp0QE3zsBk6TxlNlIu-QbzA92iOWMg1XTssSlp9DGkn36DaDV3rvig1FaPckjeiQWJ9BmPyqQQ9TeyC6mqgVCyw6I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e38c8c8a60.mp4?token=ne9s8PxKefd1JR_h40lWpdMURoyefVFnxM8hzssK8Km0XtaZfX0uUzhAS9Xb2alPgM7GMKT2iek9w-eUQay_Mu4Z8qaKA_9KhVuGd8V0q86S8MnCzcr3XesSLFaCcbPEJtxS2FutflgjWnJRxQlquTIcjwvSCGqhae7J_hL68jhkFi9ufV3FztQ7BpoQQQLWiwziaHz1DgbT_bU8FFhDnapFCSrot2fJxtpYrbxEcwbBjLc6dU0Y27ajhrEJxBIFaqLJnab1q9t7wsjgzZzXBoq-ubjfnlZQ-EhkA9G8-kchbGKeojaKN4jh_gNvtsHrAujFUqejmA5BOgyIcjhUblpMnTFIW_npg4l4SK0en8kPHwMxTmV5YpootlTfkv4UGsMwiy_hpSJeIF69maG9ZZSkrNt0z_rmqXhW0JmZBbwkIuoKohxNvVDPN4kW3kybt4NLbzFN4xdaFs_YJnF4S2OqvcvE38GKDnD6Wj2oHJVio86stdbuEjmUxIHQC7u0WK6Bf7Uc00zj8N-RXs9BC1NTip3P1GAhWlAT1xnMpDuHnNBp9hVWHyKSE5ymFD4U7YhbAbnDIvkxZ6yLN5zp0QE3zsBk6TxlNlIu-QbzA92iOWMg1XTssSlp9DGkn36DaDV3rvig1FaPckjeiQWJ9BmPyqQQ9TeyC6mqgVCyw6I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بر‌وجردی‌ها در حمایت از نیروهای مسلح: بزن که خوب می‌زنی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/459546" target="_blank">📅 22:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459544">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سپاه: حملات از سر استیصال دشمن قفل تنگه هرمز را محکم‌تر می‌کند؛ رزمندگان پاسخ پشیمان‌کننده به متجاوزان را آغاز کرده‌اند
🔹
روابط عمومی سپاه پاسداران انقلاب اسلامی: ملت بصیر و انقلابی به پاخاسته ایران اسلامی؛ تداوم حضور شما در صحنه، دشمن آمریکایی را خسته و…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farsna/459544" target="_blank">📅 22:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459543">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpUwB8Evwyz8pymgH1PdkkLtHwBCsXm_DS3qu51q7qR0is_ZEGc9OFfQTFYizPUPCor3tgsXmyTtPmlT7B2ATNDTTqD8lsPgWDZN8KK6vrR7QxP_aZ89lQoDb2ZuiYeSdUaPYEr3OhMgrENB6vs84wI8B6HX5pdnwday0P1b2jKUt_wkVT_ppm4nSakScX4Sk9CEJ87-RI1SVup1FyY6zKgMYePoPHInbwp2WrvTn6kUh-cK8JG_lrUM7eRJYN3e3PWi9HBIt-Q7Za0duiqqtp0Ut6WUkKlF-aEdJdS_21nrTNLhCwSO7s1FkHk4CC7FywfjQL3tQTOTeT7I_OXhhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: حملات از سر استیصال دشمن قفل تنگه هرمز را محکم‌تر می‌کند؛ رزمندگان پاسخ پشیمان‌کننده به متجاوزان را آغاز کرده‌اند
🔹
روابط عمومی سپاه پاسداران انقلاب اسلامی: ملت بصیر و انقلابی به پاخاسته ایران اسلامی؛ تداوم حضور شما در صحنه، دشمن آمریکایی را خسته و مایوس کرده است و مقاومت و اقتدار فرزندان رشید رزمنده شما در تنگه هرمز، سردمداران کاخ سفید را کلافه کرده است.
🔹
ساعاتی پیش در حملاتی کور و از سر استیصال، ارتش متجاوز آمریکا نقاط متعددی در سواحل جنوب ایران از جمله چند مکان غیرنظامی را بمباران کرد.
🔹
حملاتی که قفل تنگه هرمز را محکم‌تر و عزم رزمندگان را در سرکوب نیروهای اجنبی مداخله‌گر در تنگه هرمز را راسخ‌تر کرد.
🔹
گزارش نتایج عملیات رزمندگان متعاقبا به استحضار ملت شریف ایران خواهد رسید.
و ما النصر الا من عند الله العزیز الحکیم
@Farsna</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farsna/459543" target="_blank">📅 22:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459542">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تکذیب حملات دشمن به «جم»، «کنگان» و «لنگرود»
🔹
شبکه‌های اجتماعی از وقوع انفجار در ۳ شهرستان «جم»، «کنگان» و «لنگرود» خبر دادند که مقام‌های استانی اصابت هرگونه پرتابه و حمله دشمن آمریکایی را به این نقاط تکذیب کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/459542" target="_blank">📅 22:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459541">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
حملهٔ دشمن آمریکایی به منطقه‌ای غیرنظامی در کوهستک
🔹
استانداری هرمزگان: دشمن آمریکایی در حملهٔ وحشیانه به خاک کشورمان یک منطقهٔ مسکونی در کوهستک را مورد حمله قرار داد.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farsna/459541" target="_blank">📅 22:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459540">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e810f08972.mp4?token=uVUbGxhM_GgwUGAZWSNt62mzMI2wBt-ckiBzezAs7h6pgJEeAV3SDrqcoueaBIhwU7CgbSyqy1nHUtKc0qN5KUhN6V2i6A23BTTqe3Yjww7gF8XBwqiu4jQjlvZItSU1nT3fCSEqhMYxbGCZS8bm5uQDcC9LiV2bWfKIrJl-XNrSNB6N_VA3Ub9NfcxnXSNQvtSXvZZ-jnZaEZGot3YGU3GUutI-V7Ci07N2tSxYs2aGDe0sYBJJsuZBt9iE9nRW7Ka9wLVPratHuIID-Gi-KVJw0xnyfpKwOrcf5sDIwDTvM0xCXAnowStmIycdLjaSp3l2G5Mhr9t-ohL9cje1rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e810f08972.mp4?token=uVUbGxhM_GgwUGAZWSNt62mzMI2wBt-ckiBzezAs7h6pgJEeAV3SDrqcoueaBIhwU7CgbSyqy1nHUtKc0qN5KUhN6V2i6A23BTTqe3Yjww7gF8XBwqiu4jQjlvZItSU1nT3fCSEqhMYxbGCZS8bm5uQDcC9LiV2bWfKIrJl-XNrSNB6N_VA3Ub9NfcxnXSNQvtSXvZZ-jnZaEZGot3YGU3GUutI-V7Ci07N2tSxYs2aGDe0sYBJJsuZBt9iE9nRW7Ka9wLVPratHuIID-Gi-KVJw0xnyfpKwOrcf5sDIwDTvM0xCXAnowStmIycdLjaSp3l2G5Mhr9t-ohL9cje1rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع ۱۸۵ مردم کرمان با رنگ‎وبوی جهاد و حماسه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/459540" target="_blank">📅 22:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459539">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اصابت پرتابۀ دشمن به محدوده خارج از باند فرودگاه جیرفت
🔹
معاون امنیتی و انتظامی استاندار کرمان از اصابت یک پرتابۀ دشمن آمریکایی به محدوده خارج از باند فرودگاه جیرفت خبر داد.
🔸
این حمله هیچ‌گونه خسارت جانی به دنبال نداشت و به باند و ساختمان‌های فرودگاه آسیبی وارد نکرده است.
@Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/459539" target="_blank">📅 22:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459538">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
منابع عراقی از شنیده‌شدن صدای انفجار در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/459538" target="_blank">📅 22:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459536">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
حملهٔ دشمن آمریکایی به منطقه‌ای غیرنظامی در کوهستک
🔹
استانداری هرمزگان: دشمن آمریکایی در حملهٔ وحشیانه به خاک کشورمان یک منطقهٔ مسکونی در کوهستک را مورد حمله قرار داد.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/459536" target="_blank">📅 22:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459535">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqYuC_o0h1b2fFD8gTDSMPb6qVdCKVm0iaWTO-TGEMYusTnnlSrmI2Lv9zuof_DONY8YChnE47HoUZq_G7bw5kBaLxZH9mzW9LUtztEZqZf6BIu0sCsERBmLw4RbW34J0ahzceKvxCIoT2QedqGToysEAry_jjTxKopbdiz81Lv6YDoy1H3HP83QkMMY0DMlwxzd_nLoZ7WPLcHOgO4EcH79Si9SuSGZ3uJiDI4MKeekeOW3DKfO19COgpSJAy-M1X_9m90mKcWF4-b683TEcsAslxzwpHG_zEc23iPFSR0QeuI5xL7JVpKeDhCZSrnZyseGZJS7eianBx6OlSPl1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویب دریافت هزینه خدمات از کشتی‌های عبوری تنگۀ هرمز در کمیسیون امنیت ملی
🔹
سخنگوی کمیسیون امنیت ملی: بر اساس ماده ۳ طرح اقدام راهبردی تأمین امنیت و پیشرفت تنگه هرمز، در قبال خدماتی از جمله خدمات دریانوردی، محیط‌زیستی، سوخت‌رسانی در شرایط خاص، بیمه‌ای، ایمنی…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farsna/459535" target="_blank">📅 22:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459534">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/623c890cf8.mp4?token=cxLjYV_fJbwrg2eJ--fBut_n0dO7JCWXcWDHAHKlg7XttwMVjTN8Qy95phDdyRxdDOEYewudPKDVQ_nz6spVZNAkeRaxF2ZFoFFAFUmoeEP_8rDP0wGwXH1Z9tJz9ZVmBqfJJzFjNAU5Es7EpMaSv8Zv37Icy6u4WiJr8C2emoj5-SdiYQ_KkMFVsEOT7zi9v-p2Ax8d3YkGMLrV-g2xCJfW5sXPsHDJV9ix58mVqxMlFE89DK_6HqnBVPoFyBkxNNYIRqIiZH2VEJjhM4yGpI-OM2B_FUQBSBk5dvKePcWR4MlFEOqAsdIowkBMIfIBsGAgKOMn7cRh-QIAxajGaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/623c890cf8.mp4?token=cxLjYV_fJbwrg2eJ--fBut_n0dO7JCWXcWDHAHKlg7XttwMVjTN8Qy95phDdyRxdDOEYewudPKDVQ_nz6spVZNAkeRaxF2ZFoFFAFUmoeEP_8rDP0wGwXH1Z9tJz9ZVmBqfJJzFjNAU5Es7EpMaSv8Zv37Icy6u4WiJr8C2emoj5-SdiYQ_KkMFVsEOT7zi9v-p2Ax8d3YkGMLrV-g2xCJfW5sXPsHDJV9ix58mVqxMlFE89DK_6HqnBVPoFyBkxNNYIRqIiZH2VEJjhM4yGpI-OM2B_FUQBSBk5dvKePcWR4MlFEOqAsdIowkBMIfIBsGAgKOMn7cRh-QIAxajGaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان در شب ۱۸۵ هنوز با حضور مردم روشن است
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/459534" target="_blank">📅 22:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459533">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در عسلویه
🔹
فرماندار عسلویه از شنیده‌شدن صدای انفجار در این شهرستان خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farsna/459533" target="_blank">📅 21:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459532">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3xVs2nf2lIaNgXVGwG3nLDpv5HytRmQjY1a5sLfp23XnD-8ruSj1XlPG4BTsgPD2UKEkset5pIT32_n-79tRGxQIvEv96Glj9EAbZ5uRDUl0fI8egYJSZdhqrSPeYEsPjbtrlznuMoGdIUlZAe54cBsPMrrYcWLqlC3souqAa8H8tRAjkLi9xdQLysGEWCt7_wLFIs8Iy9DKEh8STobYK0pwkG8lKo9hgY4_pqHCY87CyPN5WOObAvYYgTFmH9K4BOvYLM47X6rVmrbgbHD8fs5hX0LTA6f-UPcnBzBuGiUHwhxpSkepixlTovyxCauTluUGv29DshKhwoxh1Hacg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده‌کل سپاه: هماهنگی پدافند هوایی ارتش و سپاه معادلات دشمن را برهم می‌زند
🔹
سرلشکر وحیدی در پیامی به سرتیپ الهامی، فرماندۀ پدافند ارتش: هماهنگی کم‌نظیر بین نیروی پدافند هوایی ارتش و سپاه و شبکه‌سازی یکپارچه، به‌روزرسانی مستمر فناوری‌ها و اتکا بر توان جوانان دانش‌بنیان ایرانی می‌تواند معادلات دشمن را بیش از پیش بر هم زند و بازدارندگی اطمینان‌بخشی را برای کشور ایجاد نماید.
@Farsna</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farsna/459532" target="_blank">📅 21:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459531">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
شلیک موشک‌های ایرانی به‌سمت مواضع دشمن
📝
مشاهدات میدانی خبرنگاران فارس از شلیک موشک‌ و پهپادهای ایرانی به‌سمت مواضع دشمن حکایت دارد.
@Farsna</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/459531" target="_blank">📅 21:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459530">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175cd3fff.mp4?token=jS-z_A-auWEt1XWUEwwxRpPN9lboVJ5xwfCAX7dys8QSexSpmjQGYffzEcTTIEuJN46HNWJPe6Y799kOqACX13kf_zSjVNjLTKcEJxqtSWvfEMLUgRpvxLSaxMs2ifxdwY-kYETDHYOdL9hlYTTW5tNU0wb5OUgBznTukPm97C6JGH6SxLfq23xWOiFSHsxbzdLzkmk8KB1mBzWLlnGw28woLL0a9At9GReGkxBaSkqAM__LegS-rFQt_kyzLrRcPWjxalCQjHV4xzIbU8esDCoCNP8IYuVSIR0HtI7QV15Tfs6rvwVji5xhgy2O6dM_TDYzj8zoFwAZWw-zshzzcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175cd3fff.mp4?token=jS-z_A-auWEt1XWUEwwxRpPN9lboVJ5xwfCAX7dys8QSexSpmjQGYffzEcTTIEuJN46HNWJPe6Y799kOqACX13kf_zSjVNjLTKcEJxqtSWvfEMLUgRpvxLSaxMs2ifxdwY-kYETDHYOdL9hlYTTW5tNU0wb5OUgBznTukPm97C6JGH6SxLfq23xWOiFSHsxbzdLzkmk8KB1mBzWLlnGw28woLL0a9At9GReGkxBaSkqAM__LegS-rFQt_kyzLrRcPWjxalCQjHV4xzIbU8esDCoCNP8IYuVSIR0HtI7QV15Tfs6rvwVji5xhgy2O6dM_TDYzj8zoFwAZWw-zshzzcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: کسانی که تا ۳ شهریور به اماکن اعلام‌شده مراجعه و محل زندگی‌شان را اعلام نکردند، تا پایان شهریور فرصت دارند برای اعلام محل زندگی خود اقدام کنند تا کالابرگ به آن‌ها تعلق بگیرد
@Farsna</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/459530" target="_blank">📅 21:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459529">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6888c2e65.mp4?token=J5uxHPL2fwGtDk6yDtjyNY2kZ44VwAsLcSqV-vm4X0PI2xA9K6cztv8Ig8R-myyluG5UteA3LhmTQ6v1oveBnFGGKpqVexBdisPvvW5XU0CrFepsZklAFeeGG8ZZwyuk2vo8iKQ7c9QLOcE5rE21tTfvnKlRv1FQDfq_wui_Asa2_eMAPaSeWlpjtx7CXx1CRK50uT-Qc3NKyUO7gkXOz5lEFgfWJ8WqhZ3jLvwrG45E9E0DyKwBRFZB11Ij8B0AlV7PbC5uOAo2dIkkfvGhOxvEU4Om3gCguf72iaGqi_PeUOJpq_Hk1a3j-O8kCltesJVMNCVRESQbkitrZXTHL59-0uQQuXPLD0OMVU1CLHZ5ABQDXphkmbFACVxB3Gg8UqsQQCrollPvvLPVFX8p1ntcwen1RabSyFKSzRnhs7GZ1Y220lLaRqAs2DgbUwE5vq6mUmjhmv6Xc3eEps78p-vAP7CIV1H6Zx2QbvID8CjbPkTGdMTRxoeeZAFQOcIDb2UMDhHFqQCVT7Rr3s93BaMpQYHg7pvlmLn7DYrH9TNXHjSYoN2W8Bs4jTWsl6yg3yp5qizxFuZusXKg2RjklH_DhQ6slxrMlRcUIsuzRJJKLXuyAGe-xXDIEvlhoDk0Tq-WLbqKSRXCu0M5mWECWbQzMUP-nw7sz0FLn7DWj0s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6888c2e65.mp4?token=J5uxHPL2fwGtDk6yDtjyNY2kZ44VwAsLcSqV-vm4X0PI2xA9K6cztv8Ig8R-myyluG5UteA3LhmTQ6v1oveBnFGGKpqVexBdisPvvW5XU0CrFepsZklAFeeGG8ZZwyuk2vo8iKQ7c9QLOcE5rE21tTfvnKlRv1FQDfq_wui_Asa2_eMAPaSeWlpjtx7CXx1CRK50uT-Qc3NKyUO7gkXOz5lEFgfWJ8WqhZ3jLvwrG45E9E0DyKwBRFZB11Ij8B0AlV7PbC5uOAo2dIkkfvGhOxvEU4Om3gCguf72iaGqi_PeUOJpq_Hk1a3j-O8kCltesJVMNCVRESQbkitrZXTHL59-0uQQuXPLD0OMVU1CLHZ5ABQDXphkmbFACVxB3Gg8UqsQQCrollPvvLPVFX8p1ntcwen1RabSyFKSzRnhs7GZ1Y220lLaRqAs2DgbUwE5vq6mUmjhmv6Xc3eEps78p-vAP7CIV1H6Zx2QbvID8CjbPkTGdMTRxoeeZAFQOcIDb2UMDhHFqQCVT7Rr3s93BaMpQYHg7pvlmLn7DYrH9TNXHjSYoN2W8Bs4jTWsl6yg3yp5qizxFuZusXKg2RjklH_DhQ6slxrMlRcUIsuzRJJKLXuyAGe-xXDIEvlhoDk0Tq-WLbqKSRXCu0M5mWECWbQzMUP-nw7sz0FLn7DWj0s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیاط شهیدی که سند دروغگویی منافقین است
🔹
منافقین مدتی است تلاش می‌کنند با فعالیت‌های خود در فضای مجازی و کانال‌های ماهواره‌ای، چهره‌ای جدید از این تشکیلات تروریستی ترسیم کنند.
🔹
در راستای همین پروژه آن‌ها به‌تازگی مدعی شده‌اند که «مجاهدین» هیچ‌یک از مردم عادی ایران را نکشته‌اند!
🔹
اما هزاران خانواده ایرانی، سند زنده جنایت‌های منافقین‌اند؛ خانواده‌هایی که پس از دهه‌ها، داغ عزیزانشان هنوز سرد نشده است.
🔹
شهید حاجی‌هاشم، خیاطی که در نماز جمعه تهران هدف ترور منافقین قرار گرفت، یکی از همین مردم عادی بود.
@Farsna</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/459529" target="_blank">📅 21:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459528">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/317136bcd7.mp4?token=jiQG6kT1pz2E0stLsnD2caACq4Fbyc-JDxReYLy8Pa5Rw4wUcD48VIip1-AF9Qs1jkOrHSn6y1zO8PvgoUdnp4wZ1zaUhuMp7uYp-yChn81fpfD4WsE2GSYMzWpbjPwfsgJl3nHlr1ftJvwQsIIQjmqd_HEC_yEZEsUWyrPiQXHLYfYf3y1nYfii5GI9e-HpTHgT1BsKDsat4EWHdHZFhAN2SNhccaph09XQawcgZxLHuVZ-0XCgEFwgWYwKXDX54VY2GJVMa5Jx2AeKaN4Jbwaazz4ojmRTUEKfO1VC6rzEH4BjI_iXugmn1Us78l5No9BWZNr5sinYcL4WpR4I7le7VTeKC36oftCIJYeBJHAJPQnMijIGKLcbMeezM79kQFjEsVcfcBxx7odE4Tep6ROa48fyZzbq5vymR1Ecz1kYnNOb5Uz1-VcsUyaDMrnNNsjdoj47Y16WhJNIifm5tMRbRXWtP2fg5IRINjTXo3JQP0ucCxvqGGATFsAOdKrxg5yZqrnd0Ow-XGDy-xdOFyj09pYg7IhnPaUXul5N1IdFaxB_m15dMSiejUKRf0-MxlqNpCYkRQNceE4wHkdbnECF2Wcj3he9OpTv8DO4KIiIR9rfKM-OWk8NDn49E7fIJa0EcengqpFHAJdwVJM_359dJYddXErlBXYeX60-hbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/317136bcd7.mp4?token=jiQG6kT1pz2E0stLsnD2caACq4Fbyc-JDxReYLy8Pa5Rw4wUcD48VIip1-AF9Qs1jkOrHSn6y1zO8PvgoUdnp4wZ1zaUhuMp7uYp-yChn81fpfD4WsE2GSYMzWpbjPwfsgJl3nHlr1ftJvwQsIIQjmqd_HEC_yEZEsUWyrPiQXHLYfYf3y1nYfii5GI9e-HpTHgT1BsKDsat4EWHdHZFhAN2SNhccaph09XQawcgZxLHuVZ-0XCgEFwgWYwKXDX54VY2GJVMa5Jx2AeKaN4Jbwaazz4ojmRTUEKfO1VC6rzEH4BjI_iXugmn1Us78l5No9BWZNr5sinYcL4WpR4I7le7VTeKC36oftCIJYeBJHAJPQnMijIGKLcbMeezM79kQFjEsVcfcBxx7odE4Tep6ROa48fyZzbq5vymR1Ecz1kYnNOb5Uz1-VcsUyaDMrnNNsjdoj47Y16WhJNIifm5tMRbRXWtP2fg5IRINjTXo3JQP0ucCxvqGGATFsAOdKrxg5yZqrnd0Ow-XGDy-xdOFyj09pYg7IhnPaUXul5N1IdFaxB_m15dMSiejUKRf0-MxlqNpCYkRQNceE4wHkdbnECF2Wcj3he9OpTv8DO4KIiIR9rfKM-OWk8NDn49E7fIJa0EcengqpFHAJdwVJM_359dJYddXErlBXYeX60-hbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع مردم انقلابی بندرعباس در شب ۱۸۵
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/459528" target="_blank">📅 21:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459527">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d871010fbb.mp4?token=ljKh09rfqUEztgLOY46uTTP1_G2BEhSYBFgE0RsXhdGcDvINufWM3n5CKsQnwU0op-YlCik87QQcSJpIs5AXS_tFHtELcdMsc138mkSXMGr67rylveQRk1jPPA1f3lxpVLCDK-hDjy8X0axteSDenRrbQAlSCYIpaKJ0adJHJPnwZVl2NHWaG_lWbKXZJvVOtKn2JVkQ4SnnSTdZMgUpmv4q35QVYlr-Z-42gUo-KMrWImYrseA_a9boibuHf4Wb-OEzx5K9c9cMxzPFHixreINuZFZviAqMPzBKFWyUCLAVbbf5EO8b06KIeqPzM8ye1G9pxi0GIF1yjjoZR4zhJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d871010fbb.mp4?token=ljKh09rfqUEztgLOY46uTTP1_G2BEhSYBFgE0RsXhdGcDvINufWM3n5CKsQnwU0op-YlCik87QQcSJpIs5AXS_tFHtELcdMsc138mkSXMGr67rylveQRk1jPPA1f3lxpVLCDK-hDjy8X0axteSDenRrbQAlSCYIpaKJ0adJHJPnwZVl2NHWaG_lWbKXZJvVOtKn2JVkQ4SnnSTdZMgUpmv4q35QVYlr-Z-42gUo-KMrWImYrseA_a9boibuHf4Wb-OEzx5K9c9cMxzPFHixreINuZFZviAqMPzBKFWyUCLAVbbf5EO8b06KIeqPzM8ye1G9pxi0GIF1yjjoZR4zhJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هر آنچه امشب در هرمزگان گذشت
🔹
اژدهایی، خبرنگار: در حملات امشب تاکنون کسی آسیب ندیده و زیرساخت‌ها نیز سالم هستند.
@Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/459527" target="_blank">📅 21:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459524">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bi1mP8QUBpOiQf45EXW5oaTL6cpoL-0iwxEumBoG64v-OiLyYNKQvJ1QVxfrBONdzbrqEkeGBd2mDVr2zyhVFe1f9FQaQp5G5vLo-2BcSKDzYbnzAeUGt3wnZurIQmX0Y56KtSkw-T2i2-YzFKRsRnJh2NOArW3u0LVXKkv9_WhJkaZsnIff590PeSPkAwg7_hudI46IpRkfWU_Yb9J5YkcbGTyVMPo9hIS-w3s9smmwbvU3cCqAMMhHCaffR9-Wz2z_mGNeNuQYJB6s9O98p-k0ClzrEsrLUEpaJ4c4SCIp3q3qv--AzhTAG9RPxN4xREqYG1mRyzZ87Ul7Mg3S0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد کل نیروهای مسلح
:
هزینۀ سنگینی بر دشمن آمریکایی تحمیل خواهیم کرد
🔹
ستاد کل نیروهای مسلح و قرارگاه مرکزی خاتم‌الانبیا: در پاسخ به تجاوز هوایی ارتش آمریکا به نقاطی در سیستان‌وبلوچستان و هرمزگان، نیروهای مسلح جمهوری اسلامی ایران ضربات کوبنده و شکننده‌ای را به دشمن زبون و شرور آمریکایی وارد خواهند نمود.
🔹
ارتش تروریست آمریکا هر چقدر اصرار بر شرارت در منطقه داشته باشد باید خسارات بیشتر و سنگین تری را تحمل نماید.
🔹
بارها اعلام نموده‌ایم و اراده کرده‌ایم که تحت هیچ شرایطی از حقوق ملت قهرمان ایران کوتاه نخواهیم آمد و هزینه‌های سنگینی را بر دشمن آمریکایی تحمیل خواهیم نمود.
@Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/459524" target="_blank">📅 21:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459523">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pR6r_jWtmXbVwqAAqoGG24_nLxqe8jxTxTyO387-weCEnxm-69IzyMH7-MR-H9PeXoECbq2VF7qf6Ar9FEpWPHWEc1dQBr77NzSx3IOZIfo9q6g2q4-l47tQh5J2k37k7UEHsmIBKcDhU9p-o9sVopcUqtVafAoo4MvK_v25TFfiUPxPSXlcukhwQ89uyOF1s5860sn5NBd_864bQjQg-KMexyOo1CsljgUo80E9dD3cguPxlo3MUv5WqF07M0gNkbAQHMFHsrHNk6WXvzwxhiPVNJ1GjDLsvoP-JP62WdQuPaPcll8L3FyTHacvHQkQsuE7IShIZGo737A-PRnj3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سخنگوی سپاه: تنبیه سختی در انتظار متجاوزان است
🔸
آمریکا از حملات جدید خود پشیمان خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/459523" target="_blank">📅 21:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459522">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‌
🔴
سازمان تروریستی سنتکام اعلام کرد به اهدافی در ایران حمله کرده است. @Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/459522" target="_blank">📅 21:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459521">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYIUJEaWi9svgAabqjLBKzYz3XPj9CJBOuT3Fg6IvoX2UBrYGFX_gB_PHT2kqYTRJ3A8hyJvPH5yxD8ou7rU0kwR-lxYrklOzW0ukVw95-vmXz-Chvr76UKjAAGSaKpENxnO_jWpnd834i0LmaKy1L9n-dlneRSWiP-Vl8BLiMR-5TlLl7Yg5FQw8ER8Rzn6FtO9NDtSR-3QLMQz09q9m9NGgR2CQWWOCU1r8nFY6IN6CzX9PY3phhMRlfi8H9cR1mWnk6gIqdpwudFHDqNet4d80k8j2QtNr_mEN5AgFtZRVenUreHPbfxFxUb2ntZ_NnBsM4eclQpuMOVozwwj4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سفارت آمریکا در قطر: آمریکایی‌های حاضر در خاورمیانه نسبت به خطرات آماده باشند
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/459521" target="_blank">📅 21:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459520">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10ca5b4f63.mp4?token=mYPewlBuEzTemUqOI2eXCWJO33Zcchb_CrPWNvO9mC-5yeKtDKKZKYLny4Qi9fe8ICDwiH-xVSNcnfn9E0xTuU-yKHBeecqbgUdPOHR9Lf0Nr_5CgzOowMnGPy2gTbp51-7BMVbIGhe7EQmb1MYXKfBPMauf1WGvciagu0jt_ZFFmcTGvCnTZM2A5AC3aQYE8JdoN3K4D4bThWuEkY0S_gDywXk1AqR5DRiv2ZylUV9HoTRk-mES4CaAxfr672ArIvKTSDka-abKJHQb7dmr5X5Hv0jJm1i6PKLH8ibjvp-hqcfsKrUffEsVd3PjlMK1itvP-mWgM219AaEus7_OQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10ca5b4f63.mp4?token=mYPewlBuEzTemUqOI2eXCWJO33Zcchb_CrPWNvO9mC-5yeKtDKKZKYLny4Qi9fe8ICDwiH-xVSNcnfn9E0xTuU-yKHBeecqbgUdPOHR9Lf0Nr_5CgzOowMnGPy2gTbp51-7BMVbIGhe7EQmb1MYXKfBPMauf1WGvciagu0jt_ZFFmcTGvCnTZM2A5AC3aQYE8JdoN3K4D4bThWuEkY0S_gDywXk1AqR5DRiv2ZylUV9HoTRk-mES4CaAxfr672ArIvKTSDka-abKJHQb7dmr5X5Hv0jJm1i6PKLH8ibjvp-hqcfsKrUffEsVd3PjlMK1itvP-mWgM219AaEus7_OQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل توانیر: تا اواسط شهریور حتما خاموشی‌ها تمام خواهد شد
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/459520" target="_blank">📅 20:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459519">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9bd0f58f0.mp4?token=Fk-Edc5XkvI86JWgY1V3vw1-5LEoqha2dAOCw4j4sedCGBAIbAA1RaJakuGw2OdGCU7saYCHVOlshXRKAYxQNRPxiCgyRQMl0nwSlArJy3nfUCVF8ifjfXNIg9N4uQ9v7fYqzHZJ5CF4oTnTaVn7URL-3gm2QGN3VYqU4J8iufowbn5O97YGge-CtRCQqJRHNojm75neVsY1IfC4FP1ObKGGMCLd7zDtHZBWFMsa9E69HuDSpo8ElsCkHqxrWBNkHaL3emM-Q2az1B7N9-OS4yw0GfNpUdT9BeHNaWDlVlp-XauR5mci65YSv46P5jnOm5ATa53-YGq2twJcY28MyVR9PNMo7RzFobU35Zhy9HZs6hz1e4aBkVJahImpXawWGEjWP5-qcLaXnOVFLeqD7dTRHPaOX6EbCd7EYrAg09j0H8I162N9vV_kf9E4RQn7lWjXrOI8iMUisqGiO1GFhYGYcvYdjFltPZWUfgpapvNgUdsSvhBLvdO6ZEETA5ZVXvQkoR1p4azm3bZChbWu31kVc3XXfHLeDEjQra-Ore7Bu-lVJRUOU_-QsXfpUFNyhaJ2EwFZpskou-Q-JemMdH_1yKOw1SxxpPT-mNFsdowimI0je5rxsOry6zXm_tqKB5KhU3MZqN3d8GVqEF_G4lBoToTAX6Z1szdmREfXAf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9bd0f58f0.mp4?token=Fk-Edc5XkvI86JWgY1V3vw1-5LEoqha2dAOCw4j4sedCGBAIbAA1RaJakuGw2OdGCU7saYCHVOlshXRKAYxQNRPxiCgyRQMl0nwSlArJy3nfUCVF8ifjfXNIg9N4uQ9v7fYqzHZJ5CF4oTnTaVn7URL-3gm2QGN3VYqU4J8iufowbn5O97YGge-CtRCQqJRHNojm75neVsY1IfC4FP1ObKGGMCLd7zDtHZBWFMsa9E69HuDSpo8ElsCkHqxrWBNkHaL3emM-Q2az1B7N9-OS4yw0GfNpUdT9BeHNaWDlVlp-XauR5mci65YSv46P5jnOm5ATa53-YGq2twJcY28MyVR9PNMo7RzFobU35Zhy9HZs6hz1e4aBkVJahImpXawWGEjWP5-qcLaXnOVFLeqD7dTRHPaOX6EbCd7EYrAg09j0H8I162N9vV_kf9E4RQn7lWjXrOI8iMUisqGiO1GFhYGYcvYdjFltPZWUfgpapvNgUdsSvhBLvdO6ZEETA5ZVXvQkoR1p4azm3bZChbWu31kVc3XXfHLeDEjQra-Ore7Bu-lVJRUOU_-QsXfpUFNyhaJ2EwFZpskou-Q-JemMdH_1yKOw1SxxpPT-mNFsdowimI0je5rxsOry6zXm_tqKB5KhU3MZqN3d8GVqEF_G4lBoToTAX6Z1szdmREfXAf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان‌هایی که هرشب به رنگ ایران درمی‌آیند
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/459519" target="_blank">📅 20:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459518">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18bb4d009a.mp4?token=EKHX2o_L5imOCV2vpVafSU5TtAmhvdz8ghDpr026qNos-E6SXFrlhvsWkZrqMyV3LBF1n9EXbRdB_l_gl1JB1xHmQIMDVKEEqGXDD1aXfr79jZq8g7u_oYpEbQ1erhp_ysEnrBEkgyILm2NcxUSY2KmCb8cNk0tePRYkIcVOv8TeOfszT4HGv4IkyZt_ldwD3Nq0ud62XTjlWlqePeNep3aI_EK6YjPk--UJI_Yd3rWXaqOw7mimAzGcSCMOEir04_g2US3xetI2_7fBFr09J2n4V0wh8tXNOOOV0vOGslN5LhEduIwgC41NY6LAiiTHNES70a2jXBqQstci0RiXXDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18bb4d009a.mp4?token=EKHX2o_L5imOCV2vpVafSU5TtAmhvdz8ghDpr026qNos-E6SXFrlhvsWkZrqMyV3LBF1n9EXbRdB_l_gl1JB1xHmQIMDVKEEqGXDD1aXfr79jZq8g7u_oYpEbQ1erhp_ysEnrBEkgyILm2NcxUSY2KmCb8cNk0tePRYkIcVOv8TeOfszT4HGv4IkyZt_ldwD3Nq0ud62XTjlWlqePeNep3aI_EK6YjPk--UJI_Yd3rWXaqOw7mimAzGcSCMOEir04_g2US3xetI2_7fBFr09J2n4V0wh8tXNOOOV0vOGslN5LhEduIwgC41NY6LAiiTHNES70a2jXBqQstci0RiXXDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اهداف مورد اصابت در نبرد هرمز؛ چه نقاطی زده شدند؟
🔸
نخستین تصاویر هوایی از هواگردهای منهدم شدهٔ آمریکایی
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/459518" target="_blank">📅 20:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459517">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef4e101624.mp4?token=mgVkFZs8DSxdefAfl_YTTJEGOqG6MwV02hSIQzIfMPq2nSltGjmHGtSp16JVWjHXetHIW9ilJRPp1fG9xQavrXn9C9DHNZpcr9QKbaUyM8ZpTdhGyHOaohh9UaXyovN_WGGvcGMBNUgiTRmxYFw1Vol9Ad287rsq18v3mhdGkFXioD5WSNLgjfqJR1cMT2Y5iLl3s2wS-qmYheOiX0w8QQMomO7TJJiQ1Qz9a0drUr7DJFrOSwcM80-21pFpYYiwJQZDyTQee7ph9zGUcyQ-txHaqMpNMFRpBqNapgOOgQ7woXvT5V2KaRlQGtwphsRhDr1gijT3Ol7AiHQDAQFpwG9zFiUDz9NSQbOjZQOyG1DOnN530iDmNm_iQ-mOh9Eru-_xCewM_e2GTjHqPIxWFrY_KMuASqZ8DjUvs9Hn6dBxq5S2G7GhqreMNSzQZnCBQ_55PbwlXRv4XoH-VApFH0Iuh-t8HDR2jGPLNMtq8E1Ryh8R8DxJabf0YqhUBaoV6D9pmt0MTnep9BynkMt-bL9RkbatlXU-AcBM-HzCJc9rjjthCRZ-GgUErRR6SZ5-pLxR1C3vLRbSfWL87ph_74fmqI9ApoIIThPWKafA3UQhKSE4uKExyUt2cltEnqgrvdBpmRFAkFiIxEWhJFFfmEV0dfV6l6-8X7sjEpzjWBE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef4e101624.mp4?token=mgVkFZs8DSxdefAfl_YTTJEGOqG6MwV02hSIQzIfMPq2nSltGjmHGtSp16JVWjHXetHIW9ilJRPp1fG9xQavrXn9C9DHNZpcr9QKbaUyM8ZpTdhGyHOaohh9UaXyovN_WGGvcGMBNUgiTRmxYFw1Vol9Ad287rsq18v3mhdGkFXioD5WSNLgjfqJR1cMT2Y5iLl3s2wS-qmYheOiX0w8QQMomO7TJJiQ1Qz9a0drUr7DJFrOSwcM80-21pFpYYiwJQZDyTQee7ph9zGUcyQ-txHaqMpNMFRpBqNapgOOgQ7woXvT5V2KaRlQGtwphsRhDr1gijT3Ol7AiHQDAQFpwG9zFiUDz9NSQbOjZQOyG1DOnN530iDmNm_iQ-mOh9Eru-_xCewM_e2GTjHqPIxWFrY_KMuASqZ8DjUvs9Hn6dBxq5S2G7GhqreMNSzQZnCBQ_55PbwlXRv4XoH-VApFH0Iuh-t8HDR2jGPLNMtq8E1Ryh8R8DxJabf0YqhUBaoV6D9pmt0MTnep9BynkMt-bL9RkbatlXU-AcBM-HzCJc9rjjthCRZ-GgUErRR6SZ5-pLxR1C3vLRbSfWL87ph_74fmqI9ApoIIThPWKafA3UQhKSE4uKExyUt2cltEnqgrvdBpmRFAkFiIxEWhJFFfmEV0dfV6l6-8X7sjEpzjWBE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آن‌چه در سفر پزشکیان به قرقیزستان گذشت
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/459517" target="_blank">📅 20:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459514">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tr46aAa6MWHcnFZqe4nluTjP_qIxU286hEDANGCk8ccnzQXqcoPlc0fSdGRe6fJK7CYuhBTPYMIfHqfVyekuw-qabfO356GSRqyM03vnSdxSvoU487b3CymvzM89xeffPLgAcMHT3kjZlkd95pvLDM2nSR9TkTsLs4gs15Iz46ibUDLR3ME3B6fjOXGxUho1pmhlbeLH5OzWzdLmFojBjUGmxts0cu1-YXqF4DvaWCC7PdIEAZWUxsPISPg5yZjtngkSDCABO4O25UgxEHPHPolUHI6vq9f7aDAgw1C-vaYjQt0WbxE-13LbilXpfToF4ipaNOB9N0x_qA9CeamJEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پوستر فدراسیون فوتبال برای شهرآورد فردا با استفاده از هوش‌مصنوعی
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/459514" target="_blank">📅 20:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459513">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/618cba8f6d.mp4?token=uGQYsVZ37f3R9x_oFmr5GbBx67n8WPiZvNifwbsAMUVtpBvJLAj5-3_yq4XAbdvKjXlErKyPXJVouLic7FCHBcmk_wJKaL2G5bysAm8y3YtwYFSs1jtEFAsIA16bPmsIBoUOXaFH0wGM4AFSXatRNv3slhuYV44UiP1bDZqvsoAUBm3sI67q0gBCddyoetpKBrKFSGMF83AKztLAHyKoredHgOdQNKyyCSMQPYzgLIV9po5bobOwfkzO37w-vJI0f0wTvV0netfC4fmbM_Ot1q2oX8Kr5RULv3g8hWEMJBye2TQHidOReMR3fP4prtNjemBuEhY6xwxfHEdHyHS8fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/618cba8f6d.mp4?token=uGQYsVZ37f3R9x_oFmr5GbBx67n8WPiZvNifwbsAMUVtpBvJLAj5-3_yq4XAbdvKjXlErKyPXJVouLic7FCHBcmk_wJKaL2G5bysAm8y3YtwYFSs1jtEFAsIA16bPmsIBoUOXaFH0wGM4AFSXatRNv3slhuYV44UiP1bDZqvsoAUBm3sI67q0gBCddyoetpKBrKFSGMF83AKztLAHyKoredHgOdQNKyyCSMQPYzgLIV9po5bobOwfkzO37w-vJI0f0wTvV0netfC4fmbM_Ot1q2oX8Kr5RULv3g8hWEMJBye2TQHidOReMR3fP4prtNjemBuEhY6xwxfHEdHyHS8fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بلایی که ترامپ از آن می‌ترسید، سرش آمد
🔹
جیمی کارتر، رئیس‌جمهور ۴ دهه پیش آمریکا بود که ترامپ با تمسخر ضعف‌هایش، برای خود در انتخابات رای می‌خرید و می‌گفت که نمی‌خواهد شبیه او باشد. دو ضعف بزرگ کارتر که در تاریخ آمریکا از آن یاد می‌شود، عبارت‌اند از: «شکست…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/459513" target="_blank">📅 20:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459512">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">طرح تعطیلی پنجشنبه‌ها به صحن مجلس بازمی‌گردد
🔹
جعفری‌آذر، نمایندۀ تبریز: اصلاحیۀ کاهش ساعت کار هفتگی به ۴۲.۵ ساعت و تعطیلی پنجشنبه‌ها با رفع ابهامات در کمیسیون اجتماعی، برای رأی‌گیری به صحن علنی مجلس بازمی‌گردد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/459512" target="_blank">📅 20:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459511">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNUoQzBq8zf9vY17UUwWoVtnR7FAGRwQ8QpCjfnYoCd8L6EsS9Af2aZ0OZuL98YLlvLF_yOn8SnollM-OU2fhEFFGB2i_-kgR6DRhCd0J01zJ5q3fvg_KzOv3uAXft1ZthgV_1O-dpY0UilYrDnLC5RKMFH-ylrN_WGQ_I391O18O750qaNCkdyG0ca6L5IXXG4A-hRoEiEinK-ItA_3XWY1ZeyAF4AO6u43YTD2iTfUwRPTkM91AXSctfLpRjnOmYbrjPE0jNivwUrvFFnNca7JTMyb-dZYLSOBLp_FPiZyqhT5DlfyL05X2kezx2SR7gDd3YtZaMBDsYxd4GTqBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملهٔ خرابکارانه در نیروگاه آلمانی
🔹
یک تأسیسات مهم انتقال برق در نزدیکی نیروگاه زغال‌سنگی «ژانش‌والده» در جنوب ایالت براندنبورگ آلمان، امروز هدف یک حملهٔ خرابکارانه قرار گرفت.
🔹
در همین حال، گزارش یک روزنامه آلمانی از منابع امنیتی و صنعتی حاکی است که تأسیسات مذکور چند بار هدف قرار گرفته و مهاجمان از سازه‌هایی شبیه راکت‌های دست‌ساز حامل مواد منفجره استفاده کرده‌اند.
🔹
حمله‌ای که به گفتهٔ منابع رسانه‌ای و امنیتی، هدف آن ایجاد اختلال در شبکهٔ برق و احتمالاً رقم‌زدن یک خاموشی گسترده در منطقه بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/459511" target="_blank">📅 20:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459510">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‌
🔴
شنیده‌شدن صدای انفجار در مناطقی از بندرعباس، سیریک و قشم
🔹
هنوز محل دقیق و منشا انفجارها مشخص نیست.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/459510" target="_blank">📅 20:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459509">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhILu41FzcNrK5rgFb_2BqF8LeuW3p7wc6Yk8ibbcf8YTjE7mSxH6Bty2HJSym6Bm1o2N-7KY0NEefvh0t7oPFOQGk--cPDK_R8TvHJmF_Qic4vvL08dIgvhf3vmgbwKS0e5lXuneQf2OpAGJPmZ6h_nMMOTMe2esCsuwNITSx3QK1KQEAgU-Gq0ENSaiWa4vTjmZnNFIUo3MH2uffj-oBixdBAxawSFiSkGnZRP1U7vQi9uGdbBQK6833NXn5Ex5TtHyvElZQlxWLs5i4tx2gCzsc-DSmyfrwwUbWUeko84kF8FbTnwgMWBrJ2wTg-oxhL2lSBKqdzxZJPAT__uLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قیمت نفت از ۹۴ دلار عبور کرد
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/459509" target="_blank">📅 20:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459508">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‌
🔴
شنیده‌شدن صدای انفجار در کنارک و چابهار
🔹
دقایقی قبل مردم در کنارک و چابهار صدای چند انفجار شنیدند.
📝
هنوز محل دقیق این انفجارها مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/459508" target="_blank">📅 20:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459507">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
معاون استاندار هرمزگان: تا این لحظه هیچ‌گونه اصابتی در استان هرمزگان تایید نشده است.
🔸
از دقایقی پیش برخی رسانه‌ها از شنیده‌شدن صدای انفجار در نقاطی از استان هرمزگان خبر داده‎‌اند. @Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/459507" target="_blank">📅 19:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459506">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kb0V2M7JGGAF98ii4lH4fAvY0V1Qu8iJr6t36OQ7tSu6TRYos2nX3igDdo8AKiLHSRXIvGlj0DbAi8Q4LAIrHpIJ-sY8hZ2MAewQBSvGI8HP6QP7AmHtLMtt8f2R5w270_kPS5nZ59e-dqywa-amjqAr2_0vrHONChLV0JXWaAJeqYP74qHsANBWi_DIdS3cfB5VfwD7tByl576_Suo5fPIZniGNHbuJoakPuRGgKhQcebB-Ky-4J9MU1x9YcXFwh7GwotIAkl4h0AE8fxyzDYidAR0LlGl5WO7m_cObdEMK5_hklL99jTTfG_FmdmAzO-SDfW3V-9WyX8T4s3hBiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرایی اصرار حزب‌الله به حفظ یک تپه
🔹
فشارها برای خروج حزب‌الله از ارتفاعات علی‌الطاهر افزایش یافته است؛ اما این جنبش معتقد است تحویل این موضع به ارتش لبنان، به الگویی تبدیل خواهد شد که ممکن است کل جنوب لبنان را تحت کنترل اسرائیل درآورد.
🔹
حزب‌الله براین‌باور است که اگر قرار باشد علی‌الطاهر در نهایت از دست برود، این اتفاق نباید با یک عقب‌نشینی داوطلبانه رخ دهد. از نگاه این گروه، اگر نیروهایش بدون دریافت تضمین‌های مشخص از منطقه خارج شوند، اسرائیل نه‌تنها از تهدیدهای خود دست نخواهد کشید، بلکه احتمالاً آن را به‌عنوان یک روش موفق برای رسیدن به اهدافش در مناطق دیگر نیز تکرار خواهد کرد.
🔹
تحرکات نظامی اسرائیل در جنوب لبنان نیز این نگرانی را تقویت کرده است. از نگاه حزب‌الله، هدف اسرائیل صرفاً از بین بردن یک «تهدید محلی» در علی الطاهر نیست، و حزب‌الله معتقد است اسرائیل به دنبال ایجاد یک مسیر عملیاتی به سمت نبطیه، اقلیم التفاح و منطقه جبل الریحان است.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/459506" target="_blank">📅 19:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459505">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
معاون استاندار هرمزگان: تا این لحظه هیچ‌گونه اصابتی در استان هرمزگان تایید نشده است
.
🔸
از دقایقی پیش برخی رسانه‌ها از شنیده‌شدن صدای انفجار در نقاطی از استان هرمزگان خبر داده‎‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/459505" target="_blank">📅 19:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459504">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51eaa49907.mp4?token=es7ZqPWCLxsVQdkPCYsdxKbcSkglh-UBMtQGDnmDCXBUZYrQO7EiErtiGdwUWiSYXcjiwYxOVpkfav60gIhYlP5iIo5JapK5HmGh22DTw__U4Co5sFbGOxzMLcpdGu1SVhP6Ey3QNbvXvIOAkpC64Cq3F4ZhGCJitXb9kUj3RN16KWJM1T9SL1xf5E4l0zhBJd6Q4fHfELi7M8gcx5gMofYyoXa1D_06jznrymTtmSqwm4m8LHhgx73xHS0yRlLmIumOrFrN9rEIz3bgKS2Wht-OBYzxdu49Ctsy__VROHsmRW0zoxMYkizq0BWqk1QcduTeKG_L9xtYYCuzisr5aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51eaa49907.mp4?token=es7ZqPWCLxsVQdkPCYsdxKbcSkglh-UBMtQGDnmDCXBUZYrQO7EiErtiGdwUWiSYXcjiwYxOVpkfav60gIhYlP5iIo5JapK5HmGh22DTw__U4Co5sFbGOxzMLcpdGu1SVhP6Ey3QNbvXvIOAkpC64Cq3F4ZhGCJitXb9kUj3RN16KWJM1T9SL1xf5E4l0zhBJd6Q4fHfELi7M8gcx5gMofYyoXa1D_06jznrymTtmSqwm4m8LHhgx73xHS0yRlLmIumOrFrN9rEIz3bgKS2Wht-OBYzxdu49Ctsy__VROHsmRW0zoxMYkizq0BWqk1QcduTeKG_L9xtYYCuzisr5aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بعد از شهادت فهمیدیم نخبهٔ موشکی است
🔸
گفتگویی با خانواده شهید عرفان کشاورز کیا از نخبگان هوافضا و شهدای جنگ رمضان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/459504" target="_blank">📅 19:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459503">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNqW04PObfo6dLuGssxyEk4iKc4l5Oud--7nJEBhbHY4frUvpPswplH_6tQDGwt8n7xs2m2I6RRPqjeIn5v0JBwHJq2G8sBR0ylL-pXMibuIZTgOXPkPgTCN1ZGd_HkJ5PSDLGjJZodRCkVg2g_ZPqDUJPVvomrCa-KXrZmURLjveMU1k3wOX-tENEFrcjyMaepBT_5xRdC50MpYOOmUwrw4KXryg-RSNs_eNSkZDbLxPI1pTdW_r_90ztZ9QSHp96JEjtnffCCSNajJghMQ4Elcezb_BYPreac0dyEiVBS_GmDPsn5cx7RBRiXZomglKF6yChZyVNLbflm2JXompg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمک‌های برنامه جهانی غذا به کرانه باختری، نصف شد
🔹
برنامه جهانی غذا وابسته به سازمان ملل هشدار داد که کاهش بودجه، این سازمان را مجبور کرده تا تعداد افرادی که در کرانه باختری به آنها کمک می‌کند را از ۴۰۰ هزار به ۲۰۰ هزار نفر کاهش دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/459503" target="_blank">📅 19:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459502">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4726a8e5c.mp4?token=kj-5k8CjNQbCtCwwkVuvkvBWro_OsfNMqGazvgOl0jc4UkTeoXxX-Fd7KCJHyIIFiACIIQlvFY7Z6-UWVUInxrzpSc1WdTr3urVDOU69oSoZkRsIL0n2aACpRpxTus8k1C3eVeAkLOEMSlbxdOe4VcBnttCEur6PjSBVp9F60WSf4H7cXAJ_wNBXn0QUnGlygZBfNkmfKWBOLQmVIybkf2vIyb45Gtz1v91hV9xRUTH-PRG3tll5bCpsvZ_-KT9-9AKotr_W2okzettpVBH5IcBVdLVp5kOtDWQDPzy19MYzmbtOSGIO2x7qP5BvMz6gQzsbx9NCzGf7dC0RSG5Asw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4726a8e5c.mp4?token=kj-5k8CjNQbCtCwwkVuvkvBWro_OsfNMqGazvgOl0jc4UkTeoXxX-Fd7KCJHyIIFiACIIQlvFY7Z6-UWVUInxrzpSc1WdTr3urVDOU69oSoZkRsIL0n2aACpRpxTus8k1C3eVeAkLOEMSlbxdOe4VcBnttCEur6PjSBVp9F60WSf4H7cXAJ_wNBXn0QUnGlygZBfNkmfKWBOLQmVIybkf2vIyb45Gtz1v91hV9xRUTH-PRG3tll5bCpsvZ_-KT9-9AKotr_W2okzettpVBH5IcBVdLVp5kOtDWQDPzy19MYzmbtOSGIO2x7qP5BvMz6gQzsbx9NCzGf7dC0RSG5Asw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: علی‌رغم فشارهای آمریکا، تمایل کشورهای شانگهای به همکاری اقتصادی با ایران قوی است
🔹
راه‌حل تفاهم اسلام‌آباد ساده است؛ آمریکا باید به تعهدات امضاشده بازگردد تا ایران نیز تعهدات خود را اجرا کند؛ ما پیش از آن اقدامی انجام نمی‌دهیم.   @Farsna</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/459502" target="_blank">📅 19:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459500">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e51ad29841.mp4?token=lXAnoillbcxRT1zTCEcgYEMfo7vO75G-mU-BA-z4j9xCwlxYRPDz73_bqEoxO6Tfx-YBdb3mtKEnEmF25qug4TnnVjECNqUlQ6j5Z3LyuM7DVqqGqoXnaZKpb3GCWz-FAbTuImZ4qJpshKeoyHH1HKmZCz5TaKAKi1g_8Tc0ZEgpj9icKuyLVoVAKh1u4sxwkog6Oq35NPT5k5s7T6Mv8zo87hEiZ8wVz6TCp3OorYzlQvsA4UQB5QD0OPQI_kOaaPMesyU8Fg5JxI0TWljHaHuj2oNLe7urPBPWNMWz6g_29B3ePoWnztBRa6_ccNj8N5Dybc47eUSaSmHKMCPt4lnl_OUsih9VVgmcKj_TJi4zZE2owmDzCWxb-ljJu2abCRaFZqrx4Ajc72pnniAuwWbSdGPKk9t9tO8v7LUFsJYEXSUkpPhmVeyn3c_GPLV2H64Duer-A75KL7t8wu-ZXnyYzui0DtzpKTO3PMi_1f6WbE_ARz8hW4B375z0pGTRBr7xq_4lp9HdtrYLA3QHcK39lPp4NsY6zGptUL64TDClT_FHsOQdJ39lzb5P5S7z7adk75J23LUoc_JdY62AISFNOaumyqrq0hxfJSf6UVSkoX8DcbqiaDVcPmxtqybZnkrdjhDhai_0omVnq9Wdol6GXc-KJXqhSjaVGYBSeTI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e51ad29841.mp4?token=lXAnoillbcxRT1zTCEcgYEMfo7vO75G-mU-BA-z4j9xCwlxYRPDz73_bqEoxO6Tfx-YBdb3mtKEnEmF25qug4TnnVjECNqUlQ6j5Z3LyuM7DVqqGqoXnaZKpb3GCWz-FAbTuImZ4qJpshKeoyHH1HKmZCz5TaKAKi1g_8Tc0ZEgpj9icKuyLVoVAKh1u4sxwkog6Oq35NPT5k5s7T6Mv8zo87hEiZ8wVz6TCp3OorYzlQvsA4UQB5QD0OPQI_kOaaPMesyU8Fg5JxI0TWljHaHuj2oNLe7urPBPWNMWz6g_29B3ePoWnztBRa6_ccNj8N5Dybc47eUSaSmHKMCPt4lnl_OUsih9VVgmcKj_TJi4zZE2owmDzCWxb-ljJu2abCRaFZqrx4Ajc72pnniAuwWbSdGPKk9t9tO8v7LUFsJYEXSUkpPhmVeyn3c_GPLV2H64Duer-A75KL7t8wu-ZXnyYzui0DtzpKTO3PMi_1f6WbE_ARz8hW4B375z0pGTRBr7xq_4lp9HdtrYLA3QHcK39lPp4NsY6zGptUL64TDClT_FHsOQdJ39lzb5P5S7z7adk75J23LUoc_JdY62AISFNOaumyqrq0hxfJSf6UVSkoX8DcbqiaDVcPmxtqybZnkrdjhDhai_0omVnq9Wdol6GXc-KJXqhSjaVGYBSeTI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان در دیدار با گوترش: سازمان ملل باید در قبال تحولات بین‌المللی نقش‌آفرینی مؤثرتر و کارآمدتری داشته باشد  @Farsna</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/459500" target="_blank">📅 19:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459499">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f83a10d37.mp4?token=T-K2Dc8PSVBEneByghjZF70znMmjwW3hW8MNKnSR1vRRlbnZxB9UigzsrdXKB7LKHJfaoni7tW8zIyAuumNpyuHUWp4IJRdl7TKfvGD-lrrShf2K8xUXKodYLDX_XIFVL6HSaIxtFeZeoZPKbztXs68NRQ9ZC7tUIqz99VmasxkjG7ksS-484WheWIiXwG36nBG3csQl6CfANNJBUbH3QS0GJyS6YPnzL5Gkt3vC2HcxWfrDoU_dzjzhCyqboNfQHrk4_rQg5rrTx_XKBlgXDp0aExXrncZ4HPKGTQbeWZCR3zcRvLWoEpNK1EzoEMVJTSrPZWvkowLss0NJ9RLtyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f83a10d37.mp4?token=T-K2Dc8PSVBEneByghjZF70znMmjwW3hW8MNKnSR1vRRlbnZxB9UigzsrdXKB7LKHJfaoni7tW8zIyAuumNpyuHUWp4IJRdl7TKfvGD-lrrShf2K8xUXKodYLDX_XIFVL6HSaIxtFeZeoZPKbztXs68NRQ9ZC7tUIqz99VmasxkjG7ksS-484WheWIiXwG36nBG3csQl6CfANNJBUbH3QS0GJyS6YPnzL5Gkt3vC2HcxWfrDoU_dzjzhCyqboNfQHrk4_rQg5rrTx_XKBlgXDp0aExXrncZ4HPKGTQbeWZCR3zcRvLWoEpNK1EzoEMVJTSrPZWvkowLss0NJ9RLtyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: در جلسات شانگهای و شانگهای پلاس، بر مقابله با یک‌جانبه‌گرایی غرب تأکید شد  @Farsna</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/459499" target="_blank">📅 19:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459498">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f99fd37fd.mp4?token=unBqQc0nhGvUvpzTMeoy429yDJXodRkuSlLhJ9-FNSauurBBCl8RCCHLb47ZxdKlTV6uOPQTW3bIy8IlC_YoLnRu4KFSrHBCIS1Xzsen9vFZJOM58xyOQLu_VqmyGjI3ebwa2OMjHwUAES19UJ2YyAugeQvNEAqMcG10qU2P87Qem_yesjq2GhBY0m1vD6MGStvFOJfJUYqbq9ByRhAQehD_wySWfBECC6zt0jcQsYspO3P4T8qUfmf4cIYF7ciFYW6S-bnqg46wQTqISNq3PuAv1KHmLezrbvt4qMQwM4bupIVkRW37njUIiZGhr12s2FOJZE9oSmU47vRw4x7Qmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f99fd37fd.mp4?token=unBqQc0nhGvUvpzTMeoy429yDJXodRkuSlLhJ9-FNSauurBBCl8RCCHLb47ZxdKlTV6uOPQTW3bIy8IlC_YoLnRu4KFSrHBCIS1Xzsen9vFZJOM58xyOQLu_VqmyGjI3ebwa2OMjHwUAES19UJ2YyAugeQvNEAqMcG10qU2P87Qem_yesjq2GhBY0m1vD6MGStvFOJfJUYqbq9ByRhAQehD_wySWfBECC6zt0jcQsYspO3P4T8qUfmf4cIYF7ciFYW6S-bnqg46wQTqISNq3PuAv1KHmLezrbvt4qMQwM4bupIVkRW37njUIiZGhr12s2FOJZE9oSmU47vRw4x7Qmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: در جلسات شانگهای و شانگهای پلاس، بر مقابله با یک‌جانبه‌گرایی غرب تأکید شد
@Farsna</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/459498" target="_blank">📅 19:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459497">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdq7llibEPMUmrB3WMcTv4XOI07geEC4eHzpBqYcQiBPjgG_WwUnYTEmNR4OLgjXD5HENYZFzHnH4mML3_ss99PN8ZOhh4y99mZBCPAkDARo5ko4dmmm_1vMC-hqvdaI9gs0UW0N3DH_1YFE0uNHCjE7uvrFL6_MpYhw8Mw4wDNVUk6nPP2bj12QKRbrS_xswnxUhb3me0S_VScAPUXtWepwqO14SZzzx9CPDzorKf5nuYKwolgwYIzszAwiSz37q2uRoCzR7QQ8DXiHSUFP4FDg6GDBUZ_HyL4vMJQ0sJpacvFANa8HPXqS3FpcKkyZsE4KIZN7dR563ylrnlTf0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار از پرچم سعودی در تنگهٔ هرمز
🔹
براساس اطلاعات ناوبری دریایی، دست‌کم ۱۰ نفتکش با پرچم عربستان سعودی، پرچم خود را به لیبریا تغییر داده و همزمان نام این کشتی‌ها نیز تغییر کرده است.
🔹
بر اساس این گزارش، این نفتکش‌ها در نزدیکی خورفکان در امارات متوقف شده‌اند و احتمالا در انتظار فرصت مناسب برای حرکت به سمت خلیج فارس و عبور از تنگهٔ هرمز هستند.
🔸
شب گذشته یک نفتکش عربستانی حین گذر از تنگهٔ هرمز هدف ۳ پرتابه قرار گرفت و منفجر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/459497" target="_blank">📅 19:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459496">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c7c15031.mp4?token=C4GFOqQ6PkLBEBv9IWzFJ9_Jxxxkaj7FQK96euc4p5c0tGq9NqzKQsf2AUSZjnCQmJ_4604gQwLF8m-M9CuNju1CvBzZO-ie3knS_DMz_zAsnQ3NieLED0V53VcKzZfPCm3ZWH7DFsHy53cy4iL2jLAb53kG6RYFcPk-jeKEwcer0u-X_Z1NkXx8uOZjhMuAfG7XnRJ7AwfrEx0F9O0nx73Onv1i_09kmjydTl1D37QQHFl7JX0UhiSAZ2dGg2agfIeY8K32C01knc9nCaw62TH7_kuaH7x79i4CgcyP2WKsf67mBYa8j-IjXOfiw7dxOIQV6PgEOWdmNhfdKpTWvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c7c15031.mp4?token=C4GFOqQ6PkLBEBv9IWzFJ9_Jxxxkaj7FQK96euc4p5c0tGq9NqzKQsf2AUSZjnCQmJ_4604gQwLF8m-M9CuNju1CvBzZO-ie3knS_DMz_zAsnQ3NieLED0V53VcKzZfPCm3ZWH7DFsHy53cy4iL2jLAb53kG6RYFcPk-jeKEwcer0u-X_Z1NkXx8uOZjhMuAfG7XnRJ7AwfrEx0F9O0nx73Onv1i_09kmjydTl1D37QQHFl7JX0UhiSAZ2dGg2agfIeY8K32C01knc9nCaw62TH7_kuaH7x79i4CgcyP2WKsf67mBYa8j-IjXOfiw7dxOIQV6PgEOWdmNhfdKpTWvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آسمان چین صورتی شد
🔹
آسمان شهر «چانگژو» در استان جیانگ‌سو چین برای چند دقیقه به رنگ صورتی و قرمز درخشانی درآمد و منظره‌ای غیرعادی را رقم زد.
🔹
این‌چنین منظره‌ای پیش از این نیز در نقاط مختلف جهان دیده شده و گاهی از آن با عنوان «شفق طوفانی» یاد می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farsna/459496" target="_blank">📅 19:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459495">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d2fe8f5b6.mp4?token=Cyc3EwEo4qWQFIW9WQIj5gMdRF5wcmO1cBJQXWNc8g4mV2I5wNv68EqRPo2-L8XSAmyR9AtW-7i83WQfqw8FdFZECPZpeA7EiV6uymwWc3axcqTytc8vAAEoT5cwkhaYAKuA7T4VpEwlVdrnBd3TfzwT3EffY4A81fniJX12bnHQo3CuFjNvMVh9e-dSpRcZ5jwYKDdUUefYoqyr16JL05UcyCYov9iHGoMvHhyUX9yB_SO3qCSIBDDM6Wt4fJBw7rbN6vVVnoCkS2-m9tXZDRgJxbyZY91lWEr5l5o7L3mnHvHdOuonWcLvIVRt3NkkRQ8oxQC1-bdTmhtFyABEYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d2fe8f5b6.mp4?token=Cyc3EwEo4qWQFIW9WQIj5gMdRF5wcmO1cBJQXWNc8g4mV2I5wNv68EqRPo2-L8XSAmyR9AtW-7i83WQfqw8FdFZECPZpeA7EiV6uymwWc3axcqTytc8vAAEoT5cwkhaYAKuA7T4VpEwlVdrnBd3TfzwT3EffY4A81fniJX12bnHQo3CuFjNvMVh9e-dSpRcZ5jwYKDdUUefYoqyr16JL05UcyCYov9iHGoMvHhyUX9yB_SO3qCSIBDDM6Wt4fJBw7rbN6vVVnoCkS2-m9tXZDRgJxbyZY91lWEr5l5o7L3mnHvHdOuonWcLvIVRt3NkkRQ8oxQC1-bdTmhtFyABEYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: در جلسات شانگهای و شانگهای پلاس، بر مقابله با یک‌جانبه‌گرایی غرب تأکید شد  @Farsna</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/459495" target="_blank">📅 19:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459494">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bde26b3ca2.mp4?token=vFNEJXaCus2-Pm4Q_d6UWZ9eANQku3qhIKpVFnVuKf7wSj9smW3jIb2M_4Yt_Zeam8lIr_73q2W72eIvP6ve86ZPCACu8oBPwFrb9x7LIbxTDOnSq1JoAj3pLI_hQ-jslGu4F7fxG57NwJVa5PW4OQcuzbPFj9sNzxl_CB48BMqFdsu2BXITBEYelViihxC_cZ-8MWs1s2Q4LwjkXoUA_9BJ1kSq5i3zHE12gl-eHF559mPGePdEGd4zBOt_1zoiUlcpV_Yrf_xEM30dXaH9W_r-qmL5qD22fch-gAPIUO2aox8bB3MUTkD5LTr01hXcCfQqnkbt6VZtP0IpDs7IaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bde26b3ca2.mp4?token=vFNEJXaCus2-Pm4Q_d6UWZ9eANQku3qhIKpVFnVuKf7wSj9smW3jIb2M_4Yt_Zeam8lIr_73q2W72eIvP6ve86ZPCACu8oBPwFrb9x7LIbxTDOnSq1JoAj3pLI_hQ-jslGu4F7fxG57NwJVa5PW4OQcuzbPFj9sNzxl_CB48BMqFdsu2BXITBEYelViihxC_cZ-8MWs1s2Q4LwjkXoUA_9BJ1kSq5i3zHE12gl-eHF559mPGePdEGd4zBOt_1zoiUlcpV_Yrf_xEM30dXaH9W_r-qmL5qD22fch-gAPIUO2aox8bB3MUTkD5LTr01hXcCfQqnkbt6VZtP0IpDs7IaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
عراقچی: بیش از هر زمان دیگری، آینده چندقطبی و چندجانبه‌گرایانه است
🔹
خوشوقتم که همراه با رئیس‌جمهور دکتر پزشکیان در اجلاس سران سازمان همکاری شانگهای در بیشکک قرقیزستان حضور پیدا کردم.
🔹
در دیدار و گفت‌گوها با مقامات ارشد اوراسیایی، چینی و جنوب آسیایی، بر…</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/farsna/459494" target="_blank">📅 19:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459493">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0bbbc3995.mp4?token=v9zIepD_esAHpwan0jtW8ck1J2yBszjSanHRqezt3MJ01qJ1i3rAdjnYUgp_szJgnqpjd9KZzlaJXQep460xCb3WTeUAUjVkEFO9qGUUWVSPJ1drR6N0X8Q4hdBDlwY6P-Z9Xay3eyjgxfzWdkqAQXQHl_YjFn1ZsXPMuSFqBKuyNWvFxM5gfHufNmUs1bkXH6SiXg1pmDbKLQNcH6lDaMv9PyAj0F3HWkRfsqCxQ46TJ168tx_6kGuJUZ5JwwIRyqdE2R1oJXPUCppVb3_47SB1Fgqy3TYI7wB-ZUH-lsTQvTztGAB4NocoC7CR7E5LTCAp2jsVojTY5IXCJUfB3nzIGYsBETIN90y030qbCgHRT6QTK7SoQaBMiUU9bbH7g39tpEoteaR_VblBQvbFwa6czFcExHnHjshD9hVhiEWxiYGmfVNNClloeAJv4_XWafrcKCdjvCVXXfgFgZbC3iv1UMc-hN2eGe5mpwAizOQVVQHy3fKT5MNTsxr4VQ7Ve-CVhiIDPzWq7e0bOjOdHSol-lRqX7gxtsbXAvZErn3CMacF70Tz09qGI563UNsfvLHsoA2dCIUJPtZAHyg9qiYuDzO8my4OG0Mlt-vab11tRIWzfOigIiB2l22P4fhncxBqS-xFqLSt5CNpoQIjj8ivOd2ZKzGz72IREQAHvlc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0bbbc3995.mp4?token=v9zIepD_esAHpwan0jtW8ck1J2yBszjSanHRqezt3MJ01qJ1i3rAdjnYUgp_szJgnqpjd9KZzlaJXQep460xCb3WTeUAUjVkEFO9qGUUWVSPJ1drR6N0X8Q4hdBDlwY6P-Z9Xay3eyjgxfzWdkqAQXQHl_YjFn1ZsXPMuSFqBKuyNWvFxM5gfHufNmUs1bkXH6SiXg1pmDbKLQNcH6lDaMv9PyAj0F3HWkRfsqCxQ46TJ168tx_6kGuJUZ5JwwIRyqdE2R1oJXPUCppVb3_47SB1Fgqy3TYI7wB-ZUH-lsTQvTztGAB4NocoC7CR7E5LTCAp2jsVojTY5IXCJUfB3nzIGYsBETIN90y030qbCgHRT6QTK7SoQaBMiUU9bbH7g39tpEoteaR_VblBQvbFwa6czFcExHnHjshD9hVhiEWxiYGmfVNNClloeAJv4_XWafrcKCdjvCVXXfgFgZbC3iv1UMc-hN2eGe5mpwAizOQVVQHy3fKT5MNTsxr4VQ7Ve-CVhiIDPzWq7e0bOjOdHSol-lRqX7gxtsbXAvZErn3CMacF70Tz09qGI563UNsfvLHsoA2dCIUJPtZAHyg9qiYuDzO8my4OG0Mlt-vab11tRIWzfOigIiB2l22P4fhncxBqS-xFqLSt5CNpoQIjj8ivOd2ZKzGz72IREQAHvlc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در هفت روز جنگ، ۱۵ استان را سرکشی کردم
👤
پورمحمدی در بیست‌ودومین قسمت برنامه ماجرای جنگ۲
🔻
قبل از رسیدن به هر استان، به آنها خبر نمی‌دادم تا متوجه شوم واقعاً در استان چه خبر است
.
🔻
در همان وسط جنگ، با استاندارها درباره پروژه‌های توسعه‌ای استان برنامه‌ریزی می‌کردیم.
🌐
@majaraa_media
نسخه کامل و با کیفیت را از
سایت
و
آپارات
ماجرامدیا تماشا کنید.</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/459493" target="_blank">📅 19:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459492">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJcBv2ZCJLNU_QZxc1YwRh6KgvcFr-Xk6SeswHmrUkoAqc1bwOWkIfnYvIbNwnKQTGaeJcpOAFYM5uccsN2M1VNFJuHhoef6N2DJjsvZTrFI4cFYfUJEBfa7WMFvgNmX-y0ftMH69GADleGJnDv6MGl4xgPMVpjZcQMOqqX2zB395ERaPFCs45NEy3Hx6JS4uHyEK0DI3ZIx0wyXfMhqFCIIWtlaqzZBRLBlun1IvTn9MDw5kQ5lxxiedKGSrgAi2NrftY1YWC0bFd0GyglgAQFoXeS3mFL_ApecvzFh_tKihEP4VIa0HqeOwTqPllkeZUPFqMWkd8Ma7NgUNKQaeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تداوم روند مثبت درآمدزایی بانک پارسیان؛ تراز عملیاتی مرداد ماه از4 هزار میلیارد تومان عبورکرد
مجموع درآمدهای عملیاتی این بانک در ماه مرداد به ۱۱ هزار و 360 میلیارد تومان رسید که نسبت به تیرماه (۱۰ هزار و 311 میلیارد تومان) رشدی حدود ۱۰ درصدی را تجربه کرده است.
در بررسی عملکرد پنج ماهه نخست سال ۱۴۰۵ نیز، بانک پارسیان با کسب ۴۴ هزار و 615 میلیارد تومان درآمد عملیاتی و مدیریت هزینه‌ها در سطح ۳۳ هزار و 725 میلیارد تومان، موفق به ثبت تراز عملیاتی مثبت ۱۰ هزار و 890 میلیارد تومان شده است.</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/459492" target="_blank">📅 19:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459491">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/459491" target="_blank">📅 19:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459490">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-TopaHmxlkZA7siDahiCuM2qip50sCZJOGJHtKYcVmd2SvaQzW9ch-z2slYgoBPGDBVKold8kWpAbvxJfuKGDt4NM1IMDp5zU5__IrCXS71WYTuytf_ZrQNCj9FWW3UTBkzkGbsRAZv1HXwr7D1wQMPLP_Pv7cH4q9VpgJY9wHPdOlamxlC6ggWf5K1OS3ZnCsJFbQoixxEdwuqz2akf9CabhxzrMD7cWcRmKQ9j_8bAfeBEoWDez56Q7F-lHgCk5ifOs-0TcNh_J3RQwz9Jnw_Kyr_4DKJxnwl_YYKxCYREIIobkQkLdzMDAe24OgS6a2JeKY2SHWzRxBOx8T_2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عراقچی: بیش از هر زمان دیگری، آینده چندقطبی و چندجانبه‌گرایانه است
🔹
خوشوقتم که همراه با رئیس‌جمهور دکتر پزشکیان در اجلاس سران سازمان همکاری شانگهای در بیشکک قرقیزستان حضور پیدا کردم.
🔹
در دیدار و گفت‌گوها با مقامات ارشد اوراسیایی، چینی و جنوب آسیایی، بر دفاع اصولی ایران از حاکمیت و تمامیت ارضی خود و بر ضرورت اتحاد برای مدیریت روند افول یک امپراتوری بیمار تأکید کردم.
🔹
بیش از هر زمان دیگری، آینده چندقطبی و چندجانبه‌گرایانه است.
@Farsna</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/459490" target="_blank">📅 19:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459488">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqa4qpvzAztOFwZWivQmBb5QU5P44HnglD_VkupgJlj8R_bHDd509NF-snZ8_VWGPddInrmjLfumQxPgMQstiyt-DXdPXfoHnodCH7isqqaMX-DFnaoOBiajsKrQZ07664BL6Nq-_kR7e4Z2fc6pRH0T0peTrmEkfmi8iJQ_bjos0uP1QABEdP0D_FTRTIoD9Dhx8rsL3B60NIYsW3dsm3i7OcJAi-1oD5O1JPKmWFjabYZAEeZVoM4XQlIwY_Dv__fRWRYL75jvRstMNrNlIP4R2a-tJW-sZzEHjmiPMTWBl1AXVIFNulS19sANEsX299bnHB-GHoFjGxMWqZMuhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در دیدار با گوترش: سازمان ملل باید در قبال تحولات بین‌المللی نقش‌آفرینی مؤثرتر و کارآمدتری داشته باشد
@Farsna</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/farsna/459488" target="_blank">📅 18:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459487">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f9aac287a.mp4?token=vMCjq-2CcCw1eDFre9fIDzgYTDS3PNOu7ul7-2esAs-lYgMT1VeYoMGBUAN6n_fhlvVMkDZqo9HkqQzQ6vERIje3wwu3ZUUDbrPmZye2VEH9k06OnEtu_jniUTDfN60QTa_22W_hxAvaIMBI7ssdd0IwuWr7Tez4QtLDfZwlOXBV7zsmSYH6cyFF3zH53EeV6Mt9Vw9Un01_azMgVW5u1gaLK3VmzbkzfL1YqjddD57Ebjzw-1i0fba-4_oD1MTaCuFGME60BAWQY4x6QKOpWQHBZnHkLMsLoRL4SBgaZS71l97yabNMx0lM5jmeEbnUwLvV7KXM6u9FiF2sfk85Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f9aac287a.mp4?token=vMCjq-2CcCw1eDFre9fIDzgYTDS3PNOu7ul7-2esAs-lYgMT1VeYoMGBUAN6n_fhlvVMkDZqo9HkqQzQ6vERIje3wwu3ZUUDbrPmZye2VEH9k06OnEtu_jniUTDfN60QTa_22W_hxAvaIMBI7ssdd0IwuWr7Tez4QtLDfZwlOXBV7zsmSYH6cyFF3zH53EeV6Mt9Vw9Un01_azMgVW5u1gaLK3VmzbkzfL1YqjddD57Ebjzw-1i0fba-4_oD1MTaCuFGME60BAWQY4x6QKOpWQHBZnHkLMsLoRL4SBgaZS71l97yabNMx0lM5jmeEbnUwLvV7KXM6u9FiF2sfk85Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: همهٔ اعضای شانگهای بدون استثنا، تجاوز به ایران را محکوم کردند  @Farsna</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/459487" target="_blank">📅 18:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459486">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35e7c1d89b.mp4?token=Zr3YdXSSs2KxqIS8NlXByiwEzFhtU0xhkw3C3oJ1ZVN7F3V7ipbnyVv7kbP5sPPRgzP9-K1EQn6hCOKXShmi9v1pMm62qVD3ta3BCSBODKpbn_V7vb8H5Rbsw6yRoPkArBiONk381N0BCb3aEQE9twigsIJP7ljNlKmP-6UadQeoQKI542KO8yJr-m_ZpzFFXQKsfVlZ3lsbVkaRmpQzReQBNKBIuZY2fc47joOY7bc5ucZiTxN2P19ai-_vCkAvZ8gQOedbSRL_2Wzpu6q5nkIULjIJy1WKdym_e_yyALqPHKu76hb_QgbEzkvQLLKuEShQznKipQ0klsxl1Md4RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35e7c1d89b.mp4?token=Zr3YdXSSs2KxqIS8NlXByiwEzFhtU0xhkw3C3oJ1ZVN7F3V7ipbnyVv7kbP5sPPRgzP9-K1EQn6hCOKXShmi9v1pMm62qVD3ta3BCSBODKpbn_V7vb8H5Rbsw6yRoPkArBiONk381N0BCb3aEQE9twigsIJP7ljNlKmP-6UadQeoQKI542KO8yJr-m_ZpzFFXQKsfVlZ3lsbVkaRmpQzReQBNKBIuZY2fc47joOY7bc5ucZiTxN2P19ai-_vCkAvZ8gQOedbSRL_2Wzpu6q5nkIULjIJy1WKdym_e_yyALqPHKu76hb_QgbEzkvQLLKuEShQznKipQ0klsxl1Md4RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس اقتصادی: سیاست قیمتی برای کنترل مصرف بنزین، به دلیل نبود خودروهای کم‌مصرف جایگزین، با شکست مواجه شده است
🔹
محمد‌حسین صبوری، کارشناس اقتصادی: مصرف سوخت ما نسبت به سایر کشورها در سطوح بسیار بالا قرار دارد و بخش عمده‌ای از این موضوع، ناشی از استفاده از خودروهای فرسوده و غیربهینه است.
🔹
با وجود اینکه تکنولوژی‌های جدید وارد شده‌اند، اما بحث اصلی بر سر سیاست‌هایی است که باید در حوزه خودروسازی اجرا می‌شد تا این وضعیت تغییر کند.
🔹
نتیجه این اشتباهات امروز در قالب ۲ چالش بزرگ خود را نشان می‌دهد نخست، وجود انحصار در صنعت خودرو و دوم، افزایش بی‌رویه مصرف سوخت که ۲ یا ۳ دهه است کشور را آزار می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/459486" target="_blank">📅 18:52 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
