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
<img src="https://cdn4.telesco.pe/file/ngRiI43z79T5slZA7coKcTX33-02lPZQaZzaDwAGESXqsIPfccW2UIz5i75jg_Z1h8zdh6Rj5RSnzMSXhLuTKC1XP-FTcSAd-st7jmniAz26nmYvjt9agHTSWn146UtFrvT8nE7Mc4LrnEYdPlMCxduwcH4TdOJ-T8-w6EUqtedMnWIfyjjWopwvgYPhdVBwqtyRbxCrRHGdH8IS31hLd_82jD7f-5Pf3VTPbme11RrHtKpVgibvQOBFGngZhABPVK6khmcL959uMRYkeHQRbnVQRPSp87ffHCUCToHXnR6EhYZnrImm1YSDI4ZxEFN80E7KUFiLc8PpSxLuUZeZ2A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 01:37:44</div>
<hr>

<div class="tg-post" id="msg-72919">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZAwcLmWNg_2EoaLprX2Ub-8QmrD5YLVkcSDSY1oYvs0WstHfalIl0YBhO_uvWN1MQTOTKKe50ouahWfzad4HFlEE3TEIturERCQE8cTb7a8ZCzYzA1FTSMTTWU-q3G6u-z7rIHY-I7bjSmXbHxuamvvyizpohytz0PWHJH5-IbmmoSdzIbTZMz64GAAVwyfAAwbEkiH27RKnpU-ti0p4TfInzuYY64151OiAS5bhUozIWdTKrVcbNWWsmnWChrSmsLwVNnXs9nWxpcyFeCcnbHM6LjmdfAtcCYm50Z90zOVzOOiA_FpGZvsfz-praSpS7OUmriFd590XILtbOnGhEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ce4yhSfQTZ_wOkokYX2_MKq7S0MHreG8bO8k9uXq3NXetAfuIZIsenVotqscldQ0WkHyqIZF9Z-Ju2MOi9pC0xv8f3dEM18YkzpFEl1nqQrD2xCc-7X-VrIERg0QjYCX0o2i1ogSusX_Ke-38qUyVrGwsdADJ_QWDfjRC_jyafL9bPASjzcVmFeobBxkreKDUfOtyqYfBKA6D-E_8WBUb47FXMctWJC4iY-736r8X3m4dabL_cEeIgy87VPqyLeXX94kPO6r0Es5HpALOduB9zWHcRoYx5WY5tA9OmLvyzyPv7xhm6ETqJnMiNylm0eioajpmoT26379JKr3ImwIsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adea54d8bc.mp4?token=TFqQJi_dbAJTzrNZBlBY5jmxdUvquYI-AVCff7RYgehAEjfa1b8ACJVqOWEgDj9jr2HkBO0epgO2_Ey7VTKd2WPi_bJ557G3uAZhkyBQKU1h3nYSXZ5UFoN0yOlGS4fUnKcIldXs3nEpaqghyx3uiSRcbxPmw_9msyy4FL6aUmJvIT6g1kTuuEdFAuWyhNXZmAjCUXJzDIljV1X637BMbG9aPo33HJH5HUKK1oMxMj9wRgb239e5Edjm9lIvLcJVv45B9afDaXyRJaVtLIgTyfNw4qkv-c6XfSPI-EYsRe4f3ftDE_KlpNe20OfkhRKauThARQxmauK_PN0do4ScLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adea54d8bc.mp4?token=TFqQJi_dbAJTzrNZBlBY5jmxdUvquYI-AVCff7RYgehAEjfa1b8ACJVqOWEgDj9jr2HkBO0epgO2_Ey7VTKd2WPi_bJ557G3uAZhkyBQKU1h3nYSXZ5UFoN0yOlGS4fUnKcIldXs3nEpaqghyx3uiSRcbxPmw_9msyy4FL6aUmJvIT6g1kTuuEdFAuWyhNXZmAjCUXJzDIljV1X637BMbG9aPo33HJH5HUKK1oMxMj9wRgb239e5Edjm9lIvLcJVv45B9afDaXyRJaVtLIgTyfNw4qkv-c6XfSPI-EYsRe4f3ftDE_KlpNe20OfkhRKauThARQxmauK_PN0do4ScLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۷اکتبر ۲۰۲۶؛ناو هواپیمابر کلاس نیمیتز «یو‌اس‌اس رونالد ریگان» (CVN 76) در حال ترک سن‌دیگو:
@News_Hut</div>
<div class="tg-footer">👁️ 430 · <a href="https://t.me/news_hut/72919" target="_blank">📅 01:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72918">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b185c0bc3.mp4?token=XIGvKj_m-14wbh5pJ4mg2fi483Ct4ufx7k-NbIKfIOYbE82gEzaw3uKuX0UCdaWR0J1uKBdQJ58r3Y3wj2i23-xRZcoIBdP7Sjv4Znh7-YuMKQKGVP563U07cGxu4OmDEJX-18beIMIOwZIF9DFK-zoBPlv6tStOIMChvXodjElYROBdnDR_mCUcU69pkCDqWzlyeICd332ziN5Dbvvk3at5dM7AgjbeZCdShrQvNIGjUdzjm7idlGOHReZdy6sWQ5LQISFCuAK9zqSS1e3DVbulc2-52T0eFj45jYA91RBywT9YmCHJLZUYmnPyE9O0LO8gMJi9UPnUt3WGy4Z5VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b185c0bc3.mp4?token=XIGvKj_m-14wbh5pJ4mg2fi483Ct4ufx7k-NbIKfIOYbE82gEzaw3uKuX0UCdaWR0J1uKBdQJ58r3Y3wj2i23-xRZcoIBdP7Sjv4Znh7-YuMKQKGVP563U07cGxu4OmDEJX-18beIMIOwZIF9DFK-zoBPlv6tStOIMChvXodjElYROBdnDR_mCUcU69pkCDqWzlyeICd332ziN5Dbvvk3at5dM7AgjbeZCdShrQvNIGjUdzjm7idlGOHReZdy6sWQ5LQISFCuAK9zqSS1e3DVbulc2-52T0eFj45jYA91RBywT9YmCHJLZUYmnPyE9O0LO8gMJi9UPnUt3WGy4Z5VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست وزیر جنگ آمریکا:
«ما با نیروی دریایی ایران به یه توافق رسیدیم؛ تصمیم گرفتیم اقیانوس رو باهاشون شریک بشیم.
نیمه پایینی اقیانوس مال اوناست.»</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/news_hut/72918" target="_blank">📅 00:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72917">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7AWcHv68OgmUyfr2lJblKEWhn1Evwb9iYrw_HXFwIj4jksuC2EI6noukzOC5tCIwJ-PwaaM-yM4YTwf5mxseoQzgjclQC6RmuxN2XZgrsbzFyNiuV8xFpSLFOPIC9Z7H2qZky0uGRXWqDM2ssRgPFb92nVPi5mdUV_LA72kaVtaxlLb3z2ZsL3365f_fK-XFE9i-vLYrq6aVnPNYI1pShGncQ2LnjhggG921qaQ7MA2Re2tlEqDIFvIJrgJnwbrHDbG3yaa42sKQWDF7lAK_JIbaHnG8naECmdFRgo6cA1lBCR-ah0T-mWicHPR8EmbAGMED_fMS2VvbFFtuTgFVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتلانتیک: کاخ سفید از پنتاگون خواسته گزینه‌های حملات جدید آمریکا به ایران رو پیش از انتخابات میان‌دوره‌ای ۳ نوامبر آماده کنه؛ البته هنوز هیچ تصمیم نهایی‌ای گرفته نشده.
به گفته مقام‌های آمریکایی، ترامپ می‌خواد قبل از انتخابات نشون بده که در جنگ پیشرفت حاصل شده و هم‌زمان به کاهش قیمت بنزین کمک کنه.
همچنین گزینه‌های اقدامات نظامی گسترده‌تر برای بعد از انتخابات میان‌دوره‌ای هم در حال بررسیه.
@News_Hut
| The Atlantic</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/news_hut/72917" target="_blank">📅 00:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72916">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce779c5dfa.mp4?token=AyWl8RUWBBSwecwIXKuXtsFk2POzCZ-OWMmOQIivOPcdZvhTL0lq_7MCLTXbYqvEAScDPI8m9B--izAFrIYIozWW3bab1szzaeDeovEW6zTjOShauKCqbXI_qsFE5CLD4X7Ua66IWARDPq3nbbhsf6PMeagOxecLKBLcexC8ItR1j2rLwVYxPNHYbPKvmYCvkl2Ddo_dcvhrTWeM-2SG5zCJhrEXawH-RvxclERf1iIUatiHthZgX4nOGUXTjJgcFNOhN1OWHmKXdEuFbylKHYXABMIZOragCHpfFBUYOCmYPPKitiFECmAwhgaaJ2gD2_fGb_juc6OzKq0K1mAUVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce779c5dfa.mp4?token=AyWl8RUWBBSwecwIXKuXtsFk2POzCZ-OWMmOQIivOPcdZvhTL0lq_7MCLTXbYqvEAScDPI8m9B--izAFrIYIozWW3bab1szzaeDeovEW6zTjOShauKCqbXI_qsFE5CLD4X7Ua66IWARDPq3nbbhsf6PMeagOxecLKBLcexC8ItR1j2rLwVYxPNHYbPKvmYCvkl2Ddo_dcvhrTWeM-2SG5zCJhrEXawH-RvxclERf1iIUatiHthZgX4nOGUXTjJgcFNOhN1OWHmKXdEuFbylKHYXABMIZOragCHpfFBUYOCmYPPKitiFECmAwhgaaJ2gD2_fGb_juc6OzKq0K1mAUVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست وزیر جنگ آمریکا:
«ما با نیروی دریایی ایران به یه توافق رسیدیم؛ تصمیم گرفتیم اقیانوس رو باهاشون شریک بشیم.
نیمه پایینی اقیانوس مال اوناست.»
@News_Hut</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/news_hut/72916" target="_blank">📅 00:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72915">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4015ec5f18.mp4?token=tWt2KeTnmhfZXM4mwYYV7fDTuVQACTkQtT1kecaR_ygPLsJkxdh7POaYlHlSPYXNHYTPUGqIWVTcU7xHxzD1UeDQbuS2IiiZKpSJ8k15t2QfU27N9qJuiqOJiG2cbUEKxgql4DT4N66peII6tl_RkSjv483TzqO5q2evO4bbv4M5P5luVLF-B4paKqnuE8uoFwlW0goIx8Jf-UZvH27xkQfU3X4Q1LyDPKL9BU3FBeuYUIdTsFsKBSwTn4hxKUhYCDWHLie013ODwM0qZ1CNShLcFp7U1KmV8bUWdIFfQfeZn0is4u5KnXsbh12sT9nXiA-fUOLpdFHbyVGBydnmMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4015ec5f18.mp4?token=tWt2KeTnmhfZXM4mwYYV7fDTuVQACTkQtT1kecaR_ygPLsJkxdh7POaYlHlSPYXNHYTPUGqIWVTcU7xHxzD1UeDQbuS2IiiZKpSJ8k15t2QfU27N9qJuiqOJiG2cbUEKxgql4DT4N66peII6tl_RkSjv483TzqO5q2evO4bbv4M5P5luVLF-B4paKqnuE8uoFwlW0goIx8Jf-UZvH27xkQfU3X4Q1LyDPKL9BU3FBeuYUIdTsFsKBSwTn4hxKUhYCDWHLie013ODwM0qZ1CNShLcFp7U1KmV8bUWdIFfQfeZn0is4u5KnXsbh12sT9nXiA-fUOLpdFHbyVGBydnmMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالله سرحدی، مقام طالبان:
زنان بی‌عقل هستند. آن‌ها از نظر عقلی ناقص‌اند.
آن‌ها هیچ‌چیز نمی‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/news_hut/72915" target="_blank">📅 23:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72914">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/982682c0ce.mp4?token=HYwl5kBAkq43NZ6CT-P5YGuW3u22Bz_CPNsJMzWc_1X4mjQS4M2NkqyiEEf17DMAM70BNqwGzgB50XaWyb-SGijcIhCcQ-9Awnqk0HkM4jqOdZW-2MENXR6OqAA3rAePEy9VSZXYPdOSCcd9oAV-_fbajuaQ5DYRzPnR_XAcGPL6sgOfgA-_RLs-AZXyhI8_naClCVueyJaBBJcWNE277F_TI-8LD_YWsmcbjUyoixbEF78mm8zTfAr0x8d2tNIMVcTGuWT-aKtLj8AM7fIFjEvJzHRd9q9IgqQM0YQRnzDN13eDSJHlXmJ5AkW_ZL6q5uCTOzbC5F61N9YN-Zk1EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/982682c0ce.mp4?token=HYwl5kBAkq43NZ6CT-P5YGuW3u22Bz_CPNsJMzWc_1X4mjQS4M2NkqyiEEf17DMAM70BNqwGzgB50XaWyb-SGijcIhCcQ-9Awnqk0HkM4jqOdZW-2MENXR6OqAA3rAePEy9VSZXYPdOSCcd9oAV-_fbajuaQ5DYRzPnR_XAcGPL6sgOfgA-_RLs-AZXyhI8_naClCVueyJaBBJcWNE277F_TI-8LD_YWsmcbjUyoixbEF78mm8zTfAr0x8d2tNIMVcTGuWT-aKtLj8AM7fIFjEvJzHRd9q9IgqQM0YQRnzDN13eDSJHlXmJ5AkW_ZL6q5uCTOzbC5F61N9YN-Zk1EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انگاری پرنده‌ها با این هموطن مشکل شخصی داشتن و اینطوری باهاش تسویه حساب کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/72914" target="_blank">📅 23:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72913">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f06b3f32e4.mp4?token=p83g57JMwb6Ucwm228T6mEUn-u9wrsCu53lydzyVouhDJabRmOezsAG5vO40-_wX4lKbFWBHd43ce5e9bUJwt3moby56BjuKpwM31qIYb8x41AtpBYWFFAtMd4QPw1pKUrSdCJZBBn3JZbEntVigkpqSboTY48LnCEZbBBrenf5UFHQyqjMAsXHpM7MtTDJbxLHnT3Ay7JwKFuSYxMK_TmpsXUEoI4zNAxJObh1ZXVo2OQZl-tIIOlUY6N7pW3fQ1x8I89iCiKpty1BM5YiyPGYiMG6zQxgrmDWoseTSeDzdV8I3fpSxIGiht1qPKfYpz4JnORq445ZOmzoqIif7uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f06b3f32e4.mp4?token=p83g57JMwb6Ucwm228T6mEUn-u9wrsCu53lydzyVouhDJabRmOezsAG5vO40-_wX4lKbFWBHd43ce5e9bUJwt3moby56BjuKpwM31qIYb8x41AtpBYWFFAtMd4QPw1pKUrSdCJZBBn3JZbEntVigkpqSboTY48LnCEZbBBrenf5UFHQyqjMAsXHpM7MtTDJbxLHnT3Ay7JwKFuSYxMK_TmpsXUEoI4zNAxJObh1ZXVo2OQZl-tIIOlUY6N7pW3fQ1x8I89iCiKpty1BM5YiyPGYiMG6zQxgrmDWoseTSeDzdV8I3fpSxIGiht1qPKfYpz4JnORq445ZOmzoqIif7uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختره 300 تجربی شده و زنگ زده به مشاوره‌اش داره گریه می‌کنه که چرا نتونسته زیر 100 بشه...
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/72913" target="_blank">📅 22:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72912">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aaff4cab2.mp4?token=fAF1-5E8N-6ZPF6r_3-S9PvQ7PHxaaF-bjhLVqpZRHWtjvSDNHuGdnjVK14nIwBSYB5Z6xdIT9JlXapecZfi1MOhbiWW30MZQq-7JG2FI2TLsdP63zyleCtatZAHouK-99JEaS8qjuT-lXxzEnQWHAvZwhmt86XcMG3H75DWmvMpe9NGIMhvwg-UrsKPJl-hb-vlKhQtIhvk1UTE9jo_wNUPFSibnP1lN6lFtMO8ycPefV68AwJ4TBt0ExT6kcP0tr1DBt7_aZF45SB9lLRqs-Eg9ORVFPIaYRYYdMgIwkGInx5XU4Ip5RiPOUAR27QEsFWTe7-IDc3pqNbhQvIIOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aaff4cab2.mp4?token=fAF1-5E8N-6ZPF6r_3-S9PvQ7PHxaaF-bjhLVqpZRHWtjvSDNHuGdnjVK14nIwBSYB5Z6xdIT9JlXapecZfi1MOhbiWW30MZQq-7JG2FI2TLsdP63zyleCtatZAHouK-99JEaS8qjuT-lXxzEnQWHAvZwhmt86XcMG3H75DWmvMpe9NGIMhvwg-UrsKPJl-hb-vlKhQtIhvk1UTE9jo_wNUPFSibnP1lN6lFtMO8ycPefV68AwJ4TBt0ExT6kcP0tr1DBt7_aZF45SB9lLRqs-Eg9ORVFPIaYRYYdMgIwkGInx5XU4Ip5RiPOUAR27QEsFWTe7-IDc3pqNbhQvIIOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیوپ برای استخر یک میلیارد تومان!!
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/72912" target="_blank">📅 21:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72911">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b310f181e.mp4?token=M6EHW_HnmPzIN6P5djPpa9foCeFs89ln86OGf7ohmlTgaj1b1art6YKCJSm5gXwJFN8nyQPVZkr9cGgocKPK8uJ3X-WdYYwkJTstvVAHSLfEDoTNj9dIE24ibw76KXcxylOG087zFV_GtTeLKvcH1_8cH4bm_HelalSJUCsV8nveNmLNL_qOiOLf4HZnvmk8LFquFsjz1wOIBaGb2lazmbAGnC7tuppwfD2hN3MPt2uNu5G0R8kkTgaRjyHPCP5i_1FQ4FRsJdNZfryM3vx-W8oOu-PUC-OizWfKo9Nt2R6VD5lPi1largjKxpVRHwq9azUtHSgQH-o1H9aH8znw9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b310f181e.mp4?token=M6EHW_HnmPzIN6P5djPpa9foCeFs89ln86OGf7ohmlTgaj1b1art6YKCJSm5gXwJFN8nyQPVZkr9cGgocKPK8uJ3X-WdYYwkJTstvVAHSLfEDoTNj9dIE24ibw76KXcxylOG087zFV_GtTeLKvcH1_8cH4bm_HelalSJUCsV8nveNmLNL_qOiOLf4HZnvmk8LFquFsjz1wOIBaGb2lazmbAGnC7tuppwfD2hN3MPt2uNu5G0R8kkTgaRjyHPCP5i_1FQ4FRsJdNZfryM3vx-W8oOu-PUC-OizWfKo9Nt2R6VD5lPi1largjKxpVRHwq9azUtHSgQH-o1H9aH8znw9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«شاید من جلوی نابودی کامل جهان رو گرفتم، چون ایران هیچ‌وقت سلاح هسته‌ای نخواهد داشت. و این اتفاق خیلی مثبتیه.
رئیس‌جمهورهای قبلی باید این کار رو زودتر انجام می‌دادن، یا اصلاً یکی باید این کار رو انجام می‌داد.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/72911" target="_blank">📅 21:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72910">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ecb506785.mp4?token=vyAVFA4KRFzM8LumP2d1mNamvHWVNk4ikbyR9UGDTKfKPD2bYy41CFkBJOtfT6lxE61p8EdNWd53ky1OodMBIlgbjVElB4xvXjb03AeGKEHG_oL0oMdaOmemzuV1U3PG5H8yDOJxHx5mf4IwjPKCui1Yxqb9A9OVXxG_KPBzcYUhR9N6RkbsTqwgTYmzB3iaElXb4oclW7JZqhrrYLLdYYjIrpmgn3N9p9UzQPXeXfNuuRaLzdaWNNK9nftFBQXcw39l7j4QDsb60-CEvd2TXv6_RfDRF_Onse9O0SSAXo768JdYtVK_0zdH2ZkKd-b5lWYMgb0vpSxjWUgYhRyU-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ecb506785.mp4?token=vyAVFA4KRFzM8LumP2d1mNamvHWVNk4ikbyR9UGDTKfKPD2bYy41CFkBJOtfT6lxE61p8EdNWd53ky1OodMBIlgbjVElB4xvXjb03AeGKEHG_oL0oMdaOmemzuV1U3PG5H8yDOJxHx5mf4IwjPKCui1Yxqb9A9OVXxG_KPBzcYUhR9N6RkbsTqwgTYmzB3iaElXb4oclW7JZqhrrYLLdYYjIrpmgn3N9p9UzQPXeXfNuuRaLzdaWNNK9nftFBQXcw39l7j4QDsb60-CEvd2TXv6_RfDRF_Onse9O0SSAXo768JdYtVK_0zdH2ZkKd-b5lWYMgb0vpSxjWUgYhRyU-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: الان از روسیه همون حسی رو می‌گیرید که اوایل کرونا از چین داشتید؟
ترامپ: «چین اون موقع خیلی چیزی نمی‌گفت و روسیه هم الان خیلی چیزی نمی‌گه. ولی روس‌ها می‌گن که اوضاع کاملاً تحت کنترله.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/72910" target="_blank">📅 21:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72909">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ded261ded0.mp4?token=Jqehxe3WTo009zaPVpNdPQKSePT8mTTMgraGBOwZWxSy1MjumnjkQLisOBrOc23KbAzdsgskN7OjzUnFicnupwLSEaGUkebkyczPZNq5PyRyRo88EeC_57WPmbBE7IAh4b8yx6p3cgwJRtHYnNBvZpycvowiqZXDCb5hV3oLO2teGt7A8UrLQEV9Nc2ZdOVr7WOEyvg-jMwvNm-NSzusDufTTZNQCQovC0dARK8akTIiIph5aI-Gr0d_joDw8jRzdRS94GdG2U9R7AplGPZA6WoT15lLYWiMqsjpQ0vBSlFBfaqqMcHKDjjQAmR3VayGXl17G_KVTy960haVSM42Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ded261ded0.mp4?token=Jqehxe3WTo009zaPVpNdPQKSePT8mTTMgraGBOwZWxSy1MjumnjkQLisOBrOc23KbAzdsgskN7OjzUnFicnupwLSEaGUkebkyczPZNq5PyRyRo88EeC_57WPmbBE7IAh4b8yx6p3cgwJRtHYnNBvZpycvowiqZXDCb5hV3oLO2teGt7A8UrLQEV9Nc2ZdOVr7WOEyvg-jMwvNm-NSzusDufTTZNQCQovC0dARK8akTIiIph5aI-Gr0d_joDw8jRzdRS94GdG2U9R7AplGPZA6WoT15lLYWiMqsjpQ0vBSlFBfaqqMcHKDjjQAmR3VayGXl17G_KVTy960haVSM42Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا طاعون در روسیه یک سلاح بیولوژیکی است؟
ترامپ: «فکر نمی‌کنیم این‌طور باشه. خیلی زود متوجه می‌شیم، اما فعلاً فکر نمی‌کنیم سلاح بیولوژیکی باشه.
روس‌ها هم می‌گن اوضاع کاملاً تحت کنترله.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/72909" target="_blank">📅 21:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72908">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا، در سن‌دیگو همراه با تفنگداران دریاییِ بال هوایی سوم تفنگداران دریایی در تمرینات بدنی صبحگاهی شرکت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/72908" target="_blank">📅 20:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72907">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c97edc55.mp4?token=n07azNhjZaff3C1EfVFBEPty2P0pP2xbervo_Z-aiQk32X-IHjPBPKKa8tYNNF0TzeXp1wOgPUjwN5J-j4iXnaPpS_Ydhecc0w9HKDoJbE3VejnIAiucXXzvERdY-qWgtbkPd1UrUnYeY9GMYruVuA2bt36DGiwiFGM7gieYNgpo6ohg2_6D_J0cwTYOc4Ce_8WJ9KWNc7sue0ehkDX2Bs87_W2XcbKu-hP5cKAfn1y-B50vfl_XvK4DCSySSN9o1ApXDR2CRn--76iujOYTzhjdnQ4jRNIWCXfJEznPfd_iopT4L9Gadwy-STl6KOgYL-pAqmdusCxpP1LGEZHP7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c97edc55.mp4?token=n07azNhjZaff3C1EfVFBEPty2P0pP2xbervo_Z-aiQk32X-IHjPBPKKa8tYNNF0TzeXp1wOgPUjwN5J-j4iXnaPpS_Ydhecc0w9HKDoJbE3VejnIAiucXXzvERdY-qWgtbkPd1UrUnYeY9GMYruVuA2bt36DGiwiFGM7gieYNgpo6ohg2_6D_J0cwTYOc4Ce_8WJ9KWNc7sue0ehkDX2Bs87_W2XcbKu-hP5cKAfn1y-B50vfl_XvK4DCSySSN9o1ApXDR2CRn--76iujOYTzhjdnQ4jRNIWCXfJEznPfd_iopT4L9Gadwy-STl6KOgYL-pAqmdusCxpP1LGEZHP7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجایی که مشاهده میکنید تگزاس نیست، کوهدشت لرستانه که یه چند نفر با همدیگه به مشکل خورده بودن و تصمیم گرفتن با کلاشینکف حلش کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/72907" target="_blank">📅 20:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72906">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXlXro9wdaigkDFBr4v_co9MQiSgXZCg25eJnf1Pf5E0GQcYUH3roQp5sX8DX7ZMx2LplyE2sq7aC0QHtRlWCFT70wTUVT_DDD0NVXYEG-xVNr6IxoHyOLT_ya0Z36dFuwd5CYIQ30UVch9q714i7q5wapzlK7HPPm8DuVCi-WNqvQWK6ZE1Cn3E7kas5zrVnv6J3PjRmHLRhzXtYC4y0zIpy913FtPXdviXiyy8FQBjIZzYcoAp5Mg3c8iHTdQjYgdcs7FIv3SbN3sXhsGd62YrLfSP-fQKhsWPyNSoDjBho3r1CO-jh313ADFR1lNjBNRKMgNrBI67feHy8DqdWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: حزب‌الله حدود ۲۰۰ میلیون دلار از ایران گرفته تا بین لبنانی‌هایی که در جنگ امسال با اسرائیل آواره شدن، کمک مالی توزیع کنه
!!!
طبق گفته منابع رویترز، قرار شده به هر خانواده ۳ هزار دلار پرداخت بشه.
حدود ۵۰ هزار خانواده که خونه‌هاشون تخریب شده یا از روستاهاشون امکان رفت‌وآمد وجود نداره، در اولویت قرار دارن.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/72906" target="_blank">📅 19:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72905">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb95b8f0e3.mp4?token=JkQyy7GJvPTobNXNY2Hjb5LGpu7iYVr-4NRb9cNS4iVxe2pWktwS614EvLJ745yelJRgN7RPiowmj2DNK409-hw-9iJ3iFMAcTwfB6HJpl9ueSZb55iUvjfLW9XQH6oslQk6h5qfLWNvK98kuXgDtgSr2HaTis-QqqnWnPAX_646XTCHUDVtoKDRvAndos54ojy9FOylfek0N6uy5wfSFwgavD6kioML5aW3m8rSs8iawbx-zsmY6qHN93M1fyVcnlCYcvXmVsZo25zlj7yXd_wwsHCI3cPtF3CCIrSX3PrS9g5tjysXZKJd6zTKXVJvgMP8Ri7R1l9c4Ad3zpB6Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb95b8f0e3.mp4?token=JkQyy7GJvPTobNXNY2Hjb5LGpu7iYVr-4NRb9cNS4iVxe2pWktwS614EvLJ745yelJRgN7RPiowmj2DNK409-hw-9iJ3iFMAcTwfB6HJpl9ueSZb55iUvjfLW9XQH6oslQk6h5qfLWNvK98kuXgDtgSr2HaTis-QqqnWnPAX_646XTCHUDVtoKDRvAndos54ojy9FOylfek0N6uy5wfSFwgavD6kioML5aW3m8rSs8iawbx-zsmY6qHN93M1fyVcnlCYcvXmVsZo25zlj7yXd_wwsHCI3cPtF3CCIrSX3PrS9g5tjysXZKJd6zTKXVJvgMP8Ri7R1l9c4Ad3zpB6Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همتی: علت این‌که ۲ میلیارد دلار ارز برای بازار تامین کردیم این بود که به ترامپ و وزیر خزانه‌داری‌اش بفهمانیم مشکل تامین ارز نداریم!
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/72905" target="_blank">📅 18:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72904">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a9610ab5.mp4?token=VgclEwo3KsolDYjH3FjKMuGCCOnZ-g8LjNbtnAHZIjiSEHcLPDTTevEBFNZn3qVw6rxM6376xPH_Vapg8R7HA-tDTacZg7XNZ9nvThb3Xqy7mn5JNagxtJCtwrxp2hww1tldOL_Dkh6QRsv0bwh6fxr3CBfvCey4JoT9-sTH_di7VU4B3WvNx1BOEjYaeMnbbUcjbOPr2WzLKUcsHP4deK3WIAa_kb34QlXu8GDXzfuYXFH0j9bqjyeu4zFrUg7QpfOTLBd5rwmtu0dfkP-86jaGbxvZalZxNBAUyKagO-nWAXUidiKQw72oEYIrie9Z-9EuoX94lPpsHFF43xvs7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a9610ab5.mp4?token=VgclEwo3KsolDYjH3FjKMuGCCOnZ-g8LjNbtnAHZIjiSEHcLPDTTevEBFNZn3qVw6rxM6376xPH_Vapg8R7HA-tDTacZg7XNZ9nvThb3Xqy7mn5JNagxtJCtwrxp2hww1tldOL_Dkh6QRsv0bwh6fxr3CBfvCey4JoT9-sTH_di7VU4B3WvNx1BOEjYaeMnbbUcjbOPr2WzLKUcsHP4deK3WIAa_kb34QlXu8GDXzfuYXFH0j9bqjyeu4zFrUg7QpfOTLBd5rwmtu0dfkP-86jaGbxvZalZxNBAUyKagO-nWAXUidiKQw72oEYIrie9Z-9EuoX94lPpsHFF43xvs7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#مهم
؛
مجری: «شما در سازمان ملل گفتید: «یک روز، که شاید این روز چندان هم دور نباشه، مردم ایران آزاد خواهند شد.» منظورتون از این حرف چی بود؟
نتانیاهو: «مردم ایران خودشون می‌دونن چه زمانی و در چه شرایطی باید کاری انجام بدن. وقتی زمان و شرایط مناسب فرا برسه، اون‌ها به پا خواهند خاست و این حکومت سقوط خواهد کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72904" target="_blank">📅 18:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72903">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72903" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/72903" target="_blank">📅 18:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72902">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3tnzkPZTU41i8Il0x8yZFj9z9slzoa0_mQMl131aSd4jhPwmrmQQwE40KyVrBedVpXSjQDsGMSATypM4-24iSPc0rlxmgfxKlYaNKTZTfkrLrk3AxjwGvS_7_nvFU8Qx3zjBCMUUtzfE5L5UHSb1ZXfYWnsaPsViEoiK5GB12a8i5pQrCjfZMwOKYcPeyvjsCm_lgTypKlOdm5-oaDF-fAh3VCiYVdk-NWMg3k4aekdOu4NkGQPGLQLeZPpUn5q-W14kAuXp0JGtj-DwyYpj8ULBaQJQVVBz700dh_CAzWXGNQGesgnnPcUeJXcMsRVP-8vk7vg4_oweMqGdxxWHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/72902" target="_blank">📅 18:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72901">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0613e028.mp4?token=C18I7yR7tqU0dMtUO4byQ4XqW251nY5ubY6MsihK_LWhnxtS_iJjqAGBiVogeqwVYRu8zhrU75cKPnxOpYGsEHG5m3f7uDEQZf2WoppixY-QONJc_dhjtPGtlvu_mmVCFdKVCTG3IgdNiQx9wvB_iVpHdWut2VSdSQtbj-Q0tSrwCYQ5XH80kRm5S1tLu2AXi0YeaxVunu3BRMddiZhYkIij16XlPzrJwT-lz49_zLyR47acbTyl9gRJOfy-vRhMI81Esww8wri0ia_hrkEtXlJ426cr8fR6IOWJBfwkXh7_hKFUx4Nj2kQxrR-XmTZYZ08Ey-E1QI2GghsgUof_iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0613e028.mp4?token=C18I7yR7tqU0dMtUO4byQ4XqW251nY5ubY6MsihK_LWhnxtS_iJjqAGBiVogeqwVYRu8zhrU75cKPnxOpYGsEHG5m3f7uDEQZf2WoppixY-QONJc_dhjtPGtlvu_mmVCFdKVCTG3IgdNiQx9wvB_iVpHdWut2VSdSQtbj-Q0tSrwCYQ5XH80kRm5S1tLu2AXi0YeaxVunu3BRMddiZhYkIij16XlPzrJwT-lz49_zLyR47acbTyl9gRJOfy-vRhMI81Esww8wri0ia_hrkEtXlJ426cr8fR6IOWJBfwkXh7_hKFUx4Nj2kQxrR-XmTZYZ08Ey-E1QI2GghsgUof_iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این تریلر Gta نیست، ایران خودمونه!
چند روز پیش توی بازار آهن تهران، یه نفر با ماشین میزنه به یه موتوری و فراری میشه، پلیس هم میفته دنبالش.
چند تا تیر میزنن به چرخاش و در نهایت گیر میفته و حسابی کتک میزننش.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/72901" target="_blank">📅 17:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72900">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aced9e8ba.mp4?token=Whi8RWH_kDQq55IhMuPK_Yf9As6xXhiXfS6rwCmeFhYpJOicciDEc3uyRhKR5kc81WqpBeUa_Sxhof3_KZjiLplm9f0c4EIGFmAk5FFrmHtLWzhput2yx_HyBKFJ1rb8EAfXXv1e6w-07Qsuo9T31teXg3TAbRFUWpAhjb8L0PKjS9unJUQjuPAYUymbL0qlJXUJjt_eLxQtEs5WoEL20rPSeLO2aYcSO9aVrRBFAUuhURRHkyZ5BgcQo1I3WqOFZLfZNDN-H5P7CC-Lm65bkA2cXOqtzchv4L36m7v6acXmJnXNcl5wriyu8Poq9SKbnqSpq8HJaxQbiiJWcy9OIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aced9e8ba.mp4?token=Whi8RWH_kDQq55IhMuPK_Yf9As6xXhiXfS6rwCmeFhYpJOicciDEc3uyRhKR5kc81WqpBeUa_Sxhof3_KZjiLplm9f0c4EIGFmAk5FFrmHtLWzhput2yx_HyBKFJ1rb8EAfXXv1e6w-07Qsuo9T31teXg3TAbRFUWpAhjb8L0PKjS9unJUQjuPAYUymbL0qlJXUJjt_eLxQtEs5WoEL20rPSeLO2aYcSO9aVrRBFAUuhURRHkyZ5BgcQo1I3WqOFZLfZNDN-H5P7CC-Lm65bkA2cXOqtzchv4L36m7v6acXmJnXNcl5wriyu8Poq9SKbnqSpq8HJaxQbiiJWcy9OIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه خانم در جستجوی کار:
بعد دیدن یه آگهی منشی مطب با حقوق ۱۵ میلیون تومن رفتم مطب اقای دکتر
خیلی همه چی هم شیک و با کلاس بود؛
وقتی گفتم برای کار اومدم اقای دکتر(آلت متحرک) بهم گفت اون ۱۵ میلیون حقوقی که نوشتیم فقط ۶ تومنش برای کار تو مطبه و اگه ۹ تومن بقیشو میخوای باید به خودم خدمات جنسی بدی
😐
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72900" target="_blank">📅 17:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72899">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94cb601ba6.mp4?token=JdETC5TZxkteGvyyOJWZwIMAqPqY-XaLlh0i5lKFWCJKawTLfwcaQ8W43XHnjmWZDgoAJAV9g5QVPUg00kFMUBhzgMcEXnNCn2g3Zg12euThtTKDcZf6DtClhglhEiIUETLclG05eUn_OgXTpvsEMp5TqBqGdhs_VQ4kpqZ5leg9teE3qJy_kNp5YbUiGJKlhkorxmr1HBkNTX5k4UsbJURnNfgKQMb0WfTc6SdjYDSAz_whdXExJEr3Js5eC70wnv0oYMvJuM5NsdT6EPCmNq_71FEXma0ePM3DaCHgS_1Q8tuAOQsCXdngUBS-kKH4oGHxZuX4F1PleS1669OFhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94cb601ba6.mp4?token=JdETC5TZxkteGvyyOJWZwIMAqPqY-XaLlh0i5lKFWCJKawTLfwcaQ8W43XHnjmWZDgoAJAV9g5QVPUg00kFMUBhzgMcEXnNCn2g3Zg12euThtTKDcZf6DtClhglhEiIUETLclG05eUn_OgXTpvsEMp5TqBqGdhs_VQ4kpqZ5leg9teE3qJy_kNp5YbUiGJKlhkorxmr1HBkNTX5k4UsbJURnNfgKQMb0WfTc6SdjYDSAz_whdXExJEr3Js5eC70wnv0oYMvJuM5NsdT6EPCmNq_71FEXma0ePM3DaCHgS_1Q8tuAOQsCXdngUBS-kKH4oGHxZuX4F1PleS1669OFhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی از اینستاگرام پکیج پولدار شدن خریدی و خیال میکنی دیگه کار تمومه...:
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72899" target="_blank">📅 16:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72898">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7100f309a7.mp4?token=u45ry_UeSiRvKPUaQ4tQXg_FjfZQcjUb2M4PDFZ0SD-_ogC5mMOrisdQ8YTrgeGs3Mcr7LBD6qYgvEVca8R2ckHVR5CQAwmUqj04kfiYYKV7nXXg4sxiJh3bdiZAwh8KFkNQ2dWz4Gww2GWmb62yq331_w6fXkN-YPghVoQyn84DzGKlUkFeL02kzlPLaSRXaQnxosBvs0_dVhWuibHcXHgKoymOPEbZBwUHUv7-PQihil5QFDgfoCqZmTOH2LRbmNQB55llLRWJM18f5A2VYD18gxDOilmbjQ5GcTvgL5opUw10IsJbwh1J0CzakGvzC6jXs5E7xVZpxVLLMuwqHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7100f309a7.mp4?token=u45ry_UeSiRvKPUaQ4tQXg_FjfZQcjUb2M4PDFZ0SD-_ogC5mMOrisdQ8YTrgeGs3Mcr7LBD6qYgvEVca8R2ckHVR5CQAwmUqj04kfiYYKV7nXXg4sxiJh3bdiZAwh8KFkNQ2dWz4Gww2GWmb62yq331_w6fXkN-YPghVoQyn84DzGKlUkFeL02kzlPLaSRXaQnxosBvs0_dVhWuibHcXHgKoymOPEbZBwUHUv7-PQihil5QFDgfoCqZmTOH2LRbmNQB55llLRWJM18f5A2VYD18gxDOilmbjQ5GcTvgL5opUw10IsJbwh1J0CzakGvzC6jXs5E7xVZpxVLLMuwqHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی وایرال شده از سورپرایز تولد علیرضا توسط مامانش. دخترا اگه نصف عشوه علیرضا رو داشتن سر خونه بخت بودن.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/72898" target="_blank">📅 16:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72893">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LLE2g-fCSryCzljLb-D-HjZCTaNo16suZbGg8Yc6pTBOdTMzp4iolk7iocZq_6ovX39Pyv7xhVpjOlMZQy4WZN9R0C6WzmkEf4dmyC4GD4wnfKPU4jMcCtrmy8RB3HW-qhLCH_oLHh3UXtjjNb5Oz-ZoI3vECEKmo7EvfgRt7gbmaDc5kQSDHzl3RaeaJB2YYYu2eIP2jwaOkcDgFx_4aT55vRH0Io0Vh06W29l5E4X0woTReBq4zeT1yEp4gFHS0Ft12jcfR-wohF-93Vyo9Qwvl66VOXCdLZA48kKShmAsWS1rlBBKQsXjY7JM9VuJ0esZKZXuuXezJk6uEM_mfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iFJIlIi5iDnsHQCbn8MkqgTOXZujakpes54ZR_GJqwtdD0UYp6pKH-_dAQoZSkZFRUfJWy8xcMgpeb3MypDBfq5KNVutyXmfTU1rrK0jhk-rW6TPmFAB_qLLVfYvpMord6D8tkSAm1EEqhEGX7yq98xB3qcDpnnkP35xUVwqs52NfAExhQ2ktAUapiW1lNXtc4MwqJ5M4udNA-8pBCAdQIvwc_bFw37_Z5OffiFPV_lsWEMMxQiya5_q12n71kEhjLUPPEDnqKm0VqugsjhycV0R-iOZ2GzgsNy6iuEnR12fbvbq0EjOkhjWXM2XrFsoxz09H2P_GMieMLa0mVTIIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d935bdc93d.mp4?token=Mhr_vNGotDc0vZk-bTBZCGaHi20bhd1QDhs8BPG6YxCzggzUsOGCSNtJUMzZKPVVvK1zJyLLsljcNM0VksvbU3y0idjG8Ojueh806wBGJEZJRa5jPVuf_CNSG_g6rGf86jWlwjdVW-bFDKp-ctTTrMaM_0rBz0FsVEvtnjOfjNT_N0XStCHqbTsxUNpM6L9aAKwzm0X94O1M3A2gm9Kzll-YLGmjzhs8nlLusyW4ZQmoGkHj2M9ytuiSyEMACYH5aGq3WIYckVNCTCh9rYOLDnShOJLHmq6NPFFUnIoOAoL-8NlLYtrnC4VYo_RjpgS9Df1hLaUB973gS-NGWo4zhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d935bdc93d.mp4?token=Mhr_vNGotDc0vZk-bTBZCGaHi20bhd1QDhs8BPG6YxCzggzUsOGCSNtJUMzZKPVVvK1zJyLLsljcNM0VksvbU3y0idjG8Ojueh806wBGJEZJRa5jPVuf_CNSG_g6rGf86jWlwjdVW-bFDKp-ctTTrMaM_0rBz0FsVEvtnjOfjNT_N0XStCHqbTsxUNpM6L9aAKwzm0X94O1M3A2gm9Kzll-YLGmjzhs8nlLusyW4ZQmoGkHj2M9ytuiSyEMACYH5aGq3WIYckVNCTCh9rYOLDnShOJLHmq6NPFFUnIoOAoL-8NlLYtrnC4VYo_RjpgS9Df1hLaUB973gS-NGWo4zhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز، ۷ اکتبر، سومین سالگرد «طوفان‌الاقصی»؛ حمله‌ای غافلگیرکننده که سال ۲۰۲۳ توسط حماس و گروه‌های مسلح فلسطینی انجام شد و حدود ۱۲۰۰ نفر در اسرائیل کشته و ۲۵۱ نفر هم به گروگان گرفته شدند.
بعدش اما ورق برگشت؛ جنگی شروع شد که نتیجه‌اش ویرانی بخش بزرگی از غزه و کشته‌شدن ده‌ها هزار فلسطینی بود. اسرائیل هم از همون اول گفت قرار نیست ماجرا رو همین‌جا تموم کنه و دنبال کسانی می‌ره که در حمله ۷ اکتبر نقش داشتن.
و این وسط، فهرست ترورهای اسرائیل هم کم‌کم بلندتر شد؛ از فرماندهان حماس و حزب‌الله گرفته تا چهره‌های ارشد نظامی و امنیتی جمهوری اسلامی؛ یعنی جنگی که قرار بود با «یک حمله» شروع و تمام شود، سه سال بعد هنوز کلی حساب باز و بسته‌نشده پشت سر خودش گذاشته.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/72893" target="_blank">📅 15:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72892">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GR2jb0RuNOjz1-_ZYXBl6sZKOFCTzDi8QMjUhauOGZFkUwJ7mZdT8lY7ZuykMmT-ThCl1qsiHG_rqSjVYX2eS5-ULYdSiqfZdpvqC3vC5v9s562P43WuJUiP3kSNI_sijWDqLx5ydYVRXBajNWU5WiQSO8TZFOvmflXfliwce0cPl9jFNM_5ndKee0BAtlhvKkiBP6YWmENELrZMdnc1hqwk-nS_udw1qUkc_4La4vM5iij-XTztRtfAL7tCtRdHLcOAf0g5IQHGVYjEeoQID_DYKekpIyevsI78235XEpRDG-w06JdqD-Hn3AP0kQ-YI-I-fo8FEt0sMrygx_7-YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رتبه‌های برتری که مدرسه فرهنگ (وابسته به حدادعادل) تو کنکور امسال داده :
زرین، پسرِ بادیگاردِ علی خامنه‌ای : 16 انسانی
محمدباقر، پسرِ مجتبی خامنه‌ای : 106 انسانی
محمد‌امین، پسرِ بذرپاش (وزیر راه سابق) : 173 انسانی
محمد، نوه حداد عادل : 910 انسانی
محمد، نوه محسن رضایی : 1700 انسانی
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/72892" target="_blank">📅 14:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72891">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e1e3a6f34.mp4?token=AGFWSqvmRYHch8FOKhMpJemtJAGf28DmOxSBOFxMTeMMofYErR2NvWAL6Y-QR3TOEVZ9OS82jtJz1rdrGFX-bg9rODepKVyrdiyV7qVeaPzIt8Z48MWoXfhmSBF65hyiUYIvlsKEze_QMprAV9OwkvjY0zthveuuEKqsnzALfv-a1K4A3-e43zpg1C-dmkUtox7YMe90wGS4l4zOIwkfGGGux2Pm24YogwQgqTzBlZvu8YTXj8rFIKIrLrh-D1T15ocbykR19OfnLRzgIlntnA18FMvqwlYfiTldqjY6die7RB9jriNqLzSjXOlZt_R7n0TQv88kP5IguRCP0cIioA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e1e3a6f34.mp4?token=AGFWSqvmRYHch8FOKhMpJemtJAGf28DmOxSBOFxMTeMMofYErR2NvWAL6Y-QR3TOEVZ9OS82jtJz1rdrGFX-bg9rODepKVyrdiyV7qVeaPzIt8Z48MWoXfhmSBF65hyiUYIvlsKEze_QMprAV9OwkvjY0zthveuuEKqsnzALfv-a1K4A3-e43zpg1C-dmkUtox7YMe90wGS4l4zOIwkfGGGux2Pm24YogwQgqTzBlZvu8YTXj8rFIKIrLrh-D1T15ocbykR19OfnLRzgIlntnA18FMvqwlYfiTldqjY6die7RB9jriNqLzSjXOlZt_R7n0TQv88kP5IguRCP0cIioA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کوچک زاده نماینده مجلس:
به یوسف پزشکیان بگید یه بچه دبستانی از پدر تو بیشتر میفهمه!
حرفایی که تو میزنی باید امریکا بزنه نه پسر رئیس جمهور ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/72891" target="_blank">📅 14:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72890">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab42cc577.mp4?token=bCwwLzwydRKsgwPAwBxdwhMR5voxK76-XAR4W92J9bIDI7yZS-XRpviZ00sjubLY4YehB3ez72rllDHhxkxhFou6MqKjsipK3-5_sLDxZIq36FtZMqOkCnQWi9We9eEU5UX2_rdJfAsZytyW66G9_4LtB6bDilZg2O3lbrZ4x_zKTsqeNbvxcoDm_1i5wjsYtFZ9bnePaurGWffwFTp7w5n8d7SgipUoMhyGFfOSLRjcBSz2apEufLFn2fxnaMXsrSvNaj8ltJdpHwat3SvzBTR6HWUhiim3tAoTV4L_ikEjE0EOAssdUCk3D0rls4Wr4HCTZREXAZlTDR9aJ5fmeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab42cc577.mp4?token=bCwwLzwydRKsgwPAwBxdwhMR5voxK76-XAR4W92J9bIDI7yZS-XRpviZ00sjubLY4YehB3ez72rllDHhxkxhFou6MqKjsipK3-5_sLDxZIq36FtZMqOkCnQWi9We9eEU5UX2_rdJfAsZytyW66G9_4LtB6bDilZg2O3lbrZ4x_zKTsqeNbvxcoDm_1i5wjsYtFZ9bnePaurGWffwFTp7w5n8d7SgipUoMhyGFfOSLRjcBSz2apEufLFn2fxnaMXsrSvNaj8ltJdpHwat3SvzBTR6HWUhiim3tAoTV4L_ikEjE0EOAssdUCk3D0rls4Wr4HCTZREXAZlTDR9aJ5fmeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر نتانیاهو درباره ایران:
«کشورهایی که حتی به ما حمله می‌کنن، یواشکی و در خفا می‌گن: اینا باید سقوط کنن؛ دارن همه‌مون رو خفه می‌کنن.
ما مطمئن می‌شیم که سقوط کنن. سقوط می‌کنن.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72890" target="_blank">📅 13:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72889">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec68a44315.mp4?token=I-3rBJU5sU86q4JDxHY60bILlyFaxFqmjqnmcnSWEtKKI3aUZMqQiLb6WvJrfcB0SkNHdhe7tM02mGSDm_uNAdCcMZrNQPMmIiPjqEr3mR84NjLyFGzD2iuUMNxAkMakYB3EW7HxmmItkpq-St_P5k50Sir2U6PzepB6LPcsddFYv2U0EjydypTB2T-CrGSVm1L55bPn1Qz6dptd_CUGz4u3NuZrzKfrbZnl6HBMAXLY930Q6Mev1inJbl46TETIlu2nbsutB7MZ--yjB5F53KPQk2LM-RaV-DdK9UGYkxf9suuNUdWcj5gK8zpeyyMaaMmxnmG4zY8ICnu6_yX32g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec68a44315.mp4?token=I-3rBJU5sU86q4JDxHY60bILlyFaxFqmjqnmcnSWEtKKI3aUZMqQiLb6WvJrfcB0SkNHdhe7tM02mGSDm_uNAdCcMZrNQPMmIiPjqEr3mR84NjLyFGzD2iuUMNxAkMakYB3EW7HxmmItkpq-St_P5k50Sir2U6PzepB6LPcsddFYv2U0EjydypTB2T-CrGSVm1L55bPn1Qz6dptd_CUGz4u3NuZrzKfrbZnl6HBMAXLY930Q6Mev1inJbl46TETIlu2nbsutB7MZ--yjB5F53KPQk2LM-RaV-DdK9UGYkxf9suuNUdWcj5gK8zpeyyMaaMmxnmG4zY8ICnu6_yX32g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران:
«هر دلار و هر سنتی که این حکومت به دست میاره، خرج جاده و پل یا بهتر کردن زندگی مردم ایران نمی‌کنه.
این پول رو خرج حزب‌الله و حماس و شبه‌نظامی‌هایی می‌کنن که از داخل عراق موشک شلیک می‌کنن، و همین‌طور حوثی‌ها.
باید پولشون رو برای مردم خودشون خرج می‌کردن، اما به‌جاش پول رو صرف تروریسم و تسلیحات می‌کنن.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72889" target="_blank">📅 13:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72888">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aba6a5b62.mp4?token=QHlUPIci89FlXS9P4xcSa75ZMoG7MVuHiutsZvtMSa1dM8o88_17ohHKRNWoJCYqTDZ58mQI1jGH_QQqoDTPJB9-0hX5SJklyW5mf3Z8hdCusUQ1QmU4EJ65mJqubAgY-pFqAZil7gjkvlqhRA3_icV841kaIc7KiaHHACCikOpgU6Zzj6Oqx-ZEbYCkyd74n7PmEQ09n5jDGTQFNkq0ivO_GI8BlJMY6lo7efN3pkVWACNtXV4efYVtqaNnRCmhMFx4OuTkzJnZ0JlE95hp597CnLUoCVSkzHeYPKDD40I1i3uzOwfoMZEU7jnNF3xurFfZqCfUgJJuILIdWByZmzX4Qi9qB90QWFyzU_xviOKWGegqS9kTxIyfPFuEmDrtEHJOCnCuvi3YM2vCDjlC4QexBRGGSkZN43P0uEJWeAwniyY0Pp2L6U7bbnmiYoMguN9AfjT50ZUaXtPJV9LCBFdJhT0SZ174_0VItm_J-C4fkDNr5ZpwzzuY9CupIi463TSk1CUYZMKctMl8yDHeouv1HwYmkheqcl_fheuhGIkUGwlI0uFh-idSPSbfJ-w-V32JRCo9u-Foin650G7Ody-UCv_TYktmekZ6hofBOPOtjOpns2AehhUzBpoc3K0NriG-HXLb-fpZws25ajWRA0REP83u2aPlWavMDpjYc7E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aba6a5b62.mp4?token=QHlUPIci89FlXS9P4xcSa75ZMoG7MVuHiutsZvtMSa1dM8o88_17ohHKRNWoJCYqTDZ58mQI1jGH_QQqoDTPJB9-0hX5SJklyW5mf3Z8hdCusUQ1QmU4EJ65mJqubAgY-pFqAZil7gjkvlqhRA3_icV841kaIc7KiaHHACCikOpgU6Zzj6Oqx-ZEbYCkyd74n7PmEQ09n5jDGTQFNkq0ivO_GI8BlJMY6lo7efN3pkVWACNtXV4efYVtqaNnRCmhMFx4OuTkzJnZ0JlE95hp597CnLUoCVSkzHeYPKDD40I1i3uzOwfoMZEU7jnNF3xurFfZqCfUgJJuILIdWByZmzX4Qi9qB90QWFyzU_xviOKWGegqS9kTxIyfPFuEmDrtEHJOCnCuvi3YM2vCDjlC4QexBRGGSkZN43P0uEJWeAwniyY0Pp2L6U7bbnmiYoMguN9AfjT50ZUaXtPJV9LCBFdJhT0SZ174_0VItm_J-C4fkDNr5ZpwzzuY9CupIi463TSk1CUYZMKctMl8yDHeouv1HwYmkheqcl_fheuhGIkUGwlI0uFh-idSPSbfJ-w-V32JRCo9u-Foin650G7Ody-UCv_TYktmekZ6hofBOPOtjOpns2AehhUzBpoc3K0NriG-HXLb-fpZws25ajWRA0REP83u2aPlWavMDpjYc7E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
«اقتصاد ایران داره به نقطه‌ای می‌رسه که از نظر شدت وخامت، فقط تعداد کمی از کشورهای دنیا چنین وضعیتی رو تجربه کردن.
و تمام این وضعیت تقصیر روحانیون شیعه افراطی‌ایه که توی اون کشور تصمیم‌گیری می‌کنن.
همین‌ها هستن که مردم بیچاره ایران رو به این شرایطی که الان توش قرار دارن، رسوندن.»
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72888" target="_blank">📅 12:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72887">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGLcb464ywRpQ0kW5v8hsDBeFNVIhKhRHRGPgApLW3X2cNy2fKY9BGfjKjYZXyfI3fCVILVOLhrhXJF4PdVeYkCL-AplaGwdXOFdUvx-J5KEczu_nTAf992H2xITq5x5-Xr-HswcyflH4wyn42fhuFalA4vG0PtLusuRpwU1FuH5UpFV9YQPyguCkLkKQLpy3H898-GzKtTihLldIu8Fc8714Qo4lJxSi6uns22NTnmW9vbIm0WakcIw1QkCU-c61rnADhFjxBAb-Bqq_oGE1CpKwnewST2tBRO9C8Ph3m22Mh11rGDfpKMbwYNJHUS3HkhKsoaoY4XEA9LPkaBRhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله ونس، به رویترز گفته آمریکا هنوز دقیقاً نمی‌دونه بعد از کشته‌شدن علی خامنه‌ای، چه کسی در نهایت تصمیم‌های اصلی ایران رو می‌گیره.
ونس گفته آمریکا در حال مذاکره با مسعود پزشکیان، رئیس‌جمهور ایران، و عباس عراقچی، وزیر خارجه است، اما مشخص نیست این دو نفر در ساختار فعلی قدرت ایران چقدر اختیار و قدرت تصمیم‌گیری دارند.
او گفته یکی از چیزهایی که آمریکا متوجه شده اینه که «کاملاً مشخص نیست ایران چطور تصمیم‌گیری می‌کنه.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72887" target="_blank">📅 12:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72886">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpiYH-45PVQ1FG3_sHkcUNCVSyTp0tgsWIfM8CyQ-6_IUKq_2HwLDTmSF6cp7AVIHltvDg19lPNd_8qbNgl1uH2vuwautgPhIuG09Jr7YCvk2s1gL10hcXSJeHocJi6jh7ZQ01sw4NEaYoYw6bxRJ8sl-LxgUfMBfZobHShGK2A3TRbd9yKah8nsEaK062StnOxMwz6cRn1kAxKm3j3VXtzMoWHI8R0BKBQD4DEPKW-7kTEb-y5lr8ZCHqZs1SNAoZNdtRUGsz36ouoU_l3O8gHtyuhaAk9t9uDJurYzhiSz_oF6FlDNrB6b4c-VfD_lnZ9o1oDFJ5w3h_ybIC42OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله ونس، معاون ترامپ، به رویترز گفته اگه ایران بخواد به توافق برسه و جنگ ۷ ماهه با آمریکا تموم بشه، باید ظرفیت غنی‌سازی اورانیومش رو به‌طور قابل‌توجهی کاهش بده.
ونس گفته آمریکا دیگه به وعده و قول برای محدودیت‌های آینده اکتفا نمی‌کنه و باید اقدام واقعی و قابل لمس از طرف ایران ببینه.
اون همچنین پرسیده: اگه ایران واقعاً دنبال ساخت سلاح هسته‌ای نیست، پس چرا باید اورانیوم ۶۰ درصد غنی‌شده داشته باشه؟
با این حال، ونس گفته آمریکا همچنان برای توافق آمادگی داره، اما امتیاز هسته‌ای واقعی از ایران می‌خواد و تأکید کرده: «قرار نیست حرف رو با عمل عوض کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72886" target="_blank">📅 11:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72885">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bff0381d0.mp4?token=ObULtiA1JTy6ykgGqNWhjuVA2VtJ6ArQrmmTqPtzaDwIq_BHqmNC70FLgqZs_72yfSp-7vFlIstWgUq8OUxvtyKzwr4CoezgB-KM5ApyzVIiGKkn1KQ6LHk-CVMpJ0NuCd72SgYQ56NqfyNBB1cR6lJVhzkaBTNG9A2a0kQ-D0JobKFxSFPDlz523rxs4jh6bKBjGPwLEf9TEqUerOQ_OtsRalkn9mECG9o10fMyJQv_GBfwdhhOlIPdBofm_TSKeb4RCnSYFQMUqaN3ZZzGpDg-ukZ5O6NQF9siceM3D1F9i3dYzfh_M4MQDtwgCmFfz-ouHGB22dj38aVPPKNotw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bff0381d0.mp4?token=ObULtiA1JTy6ykgGqNWhjuVA2VtJ6ArQrmmTqPtzaDwIq_BHqmNC70FLgqZs_72yfSp-7vFlIstWgUq8OUxvtyKzwr4CoezgB-KM5ApyzVIiGKkn1KQ6LHk-CVMpJ0NuCd72SgYQ56NqfyNBB1cR6lJVhzkaBTNG9A2a0kQ-D0JobKFxSFPDlz523rxs4jh6bKBjGPwLEf9TEqUerOQ_OtsRalkn9mECG9o10fMyJQv_GBfwdhhOlIPdBofm_TSKeb4RCnSYFQMUqaN3ZZzGpDg-ukZ5O6NQF9siceM3D1F9i3dYzfh_M4MQDtwgCmFfz-ouHGB22dj38aVPPKNotw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخوند نبویان: نماز و روزه و گناه و... مهم نیست همه کار باید کرد تا نظام حفظ بشه!
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/72885" target="_blank">📅 11:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72884">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94194705f4.mp4?token=CKtW0c0VTkPp6-hN6HjDsvNUhPvVMg6acKUV8s_Cqi0V3ILLQBOIJGIKibRWsmuj5GIe-te-Xy-q72QTxPSGqcOGqFMthwHlXrGzBNmXCY8MEp4-IoSLn3yrSFKgnLyZ6tpwmGVbE0cRLEr7ydMICcd1z8nkKEZtUCysYsxZdZf0cFee5T95-6cWMYfhl12eDFTP6zOymE-dnu5MzrAnz0VIAI6l5RYatP1jWKww7Q7dJf0Vvpm1WAlkB_1OA6wayD6hSawo9u3CRsQomnMLOBf2njbt73yINsdt04D2NoONS_ELjMZD0mku2fj5dx91Vrf0QkzvvN5SkJEa0JRayQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94194705f4.mp4?token=CKtW0c0VTkPp6-hN6HjDsvNUhPvVMg6acKUV8s_Cqi0V3ILLQBOIJGIKibRWsmuj5GIe-te-Xy-q72QTxPSGqcOGqFMthwHlXrGzBNmXCY8MEp4-IoSLn3yrSFKgnLyZ6tpwmGVbE0cRLEr7ydMICcd1z8nkKEZtUCysYsxZdZf0cFee5T95-6cWMYfhl12eDFTP6zOymE-dnu5MzrAnz0VIAI6l5RYatP1jWKww7Q7dJf0Vvpm1WAlkB_1OA6wayD6hSawo9u3CRsQomnMLOBf2njbt73yINsdt04D2NoONS_ELjMZD0mku2fj5dx91Vrf0QkzvvN5SkJEa0JRayQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم زیبای و ویژه برای وداع با مسی با نمایش پهبادی در آسمان!
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/72884" target="_blank">📅 11:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72883">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72883" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/72883" target="_blank">📅 11:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72882">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdidU8RdJxpe8ePdxbY-Hm7f2UDMjU1O54GqmJqYom01tLZbLMFiOOVoHC0QbKfThD99iGLeYmPLJfmx1_XQtKFH8OjuGA-vetoK_qles8jSmeEJrRPK7UVkpyPvHiu3KLI9Q-Kzyf1mGdaiSHd3Zr4jt3xMggYV-0gUVibGwHnSk7wj4M1tp_JPZEHRnGKcxCXmIwSuMBNQdOvii51nUV-n9IVKLpYVMl9ovhS0JZa84tPZ40HtmrHGX4IgOfxpUsLMgiTNtp5-lQaOV8hMBOPJOTX5oWTjSdrBQzfTcMJv-QRNvrUcD6g2YoU5hySPs5wEgRWmNQH__P-sh5uxVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/72882" target="_blank">📅 11:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72878">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d39cf67708.mp4?token=mHQuv6ucqm4I75PGQFEQDoOwc7NII93Mdj3w88kSLaVd_OEC97qfgb-OoFQoiKBoCUbakcNPgFn-lfDYA6yeIm6jyQQd8ZL-8BmEPBCmLURfFyMULReWOx4oltx8gkK0IJ1VNZDB7lCzrWko6H6HJI1Hi92Idkm2Wd8S59nm2rnLNi_dGd69mx-xRobgoZ77W8Qi2JH9XtCpqaEbTvfybbGxc6uhBtRaxeHwJMPvGFzBy7e6cd1zQVLFg8v1rl5eaC31WtAS3knxz3_3HpkR6wCEIY_F8vpj69QYzz_neOMAy9I_AtZBNr9kjVF-jO2pBszGPOTqrblWcQHtBioLqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d39cf67708.mp4?token=mHQuv6ucqm4I75PGQFEQDoOwc7NII93Mdj3w88kSLaVd_OEC97qfgb-OoFQoiKBoCUbakcNPgFn-lfDYA6yeIm6jyQQd8ZL-8BmEPBCmLURfFyMULReWOx4oltx8gkK0IJ1VNZDB7lCzrWko6H6HJI1Hi92Idkm2Wd8S59nm2rnLNi_dGd69mx-xRobgoZ77W8Qi2JH9XtCpqaEbTvfybbGxc6uhBtRaxeHwJMPvGFzBy7e6cd1zQVLFg8v1rl5eaC31WtAS3knxz3_3HpkR6wCEIY_F8vpj69QYzz_neOMAy9I_AtZBNr9kjVF-jO2pBszGPOTqrblWcQHtBioLqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالاخره رسیدیم به اون لحظه‌ای که عاشقان فوتبال تحمل دیدنشو ندارن...
لیونل مسی، اسطوره ۳۹ ساله فوتبال، سه‌شنبه ۶ اکتبر ۲۰۲۶ برای آخرین بار پیراهن آرژانتین رو پوشید؛ این بار در ورزشگاه مومنتال بوئنوس‌آیرس و مقابل بنین.
مسی بعد از سال‌ها افتخار، جام‌ها، اشک‌ها و لحظه‌هایی که برای آرژانتین ساخت، جلوی چشم هوادارانی که برای خداحافظی باهاش ورزشگاه رو پر کرده بودن، رسماً از تیم ملی خداحافظی کرد.
از این به بعد دیگه مسی رو با پیراهن آرژانتین نمی‌بینیم؛ پرونده یکی از باشکوه‌ترین دوران‌های ملی تاریخ فوتبال هم اینجا بسته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/72878" target="_blank">📅 10:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72875">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca1a543a9.mp4?token=Cf100OcmVp2d24EWgPdZoWCNt3MUmxXTltNTIaVZsia7G9IpGixCWomLfUg0c6AkzybDa8Ov6TczYptaUr8J-ZjjlFlX0LBjobtm7YDGA4x-RgleV2b9jxZMtCdtHutjAIAZpOXnwEsj0ZzZPCejplFP31r0jdvjYGgC3NyklTGWiYewJZMl7FjjeF5JuFgL4AJXYZMy0nIBY_iN2djdb9DSANq4hvPhukCEYThcz1pVHhxRYS6jIwAI3eIUuRqxf2Hozi5Hi6bEObWkFBRwLSw08BGoegBjGCjgxUJz-XAC3BfjUXI-jal4KazHVpBOLo99ZLTdhAN1w0QrOw-gOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca1a543a9.mp4?token=Cf100OcmVp2d24EWgPdZoWCNt3MUmxXTltNTIaVZsia7G9IpGixCWomLfUg0c6AkzybDa8Ov6TczYptaUr8J-ZjjlFlX0LBjobtm7YDGA4x-RgleV2b9jxZMtCdtHutjAIAZpOXnwEsj0ZzZPCejplFP31r0jdvjYGgC3NyklTGWiYewJZMl7FjjeF5JuFgL4AJXYZMy0nIBY_iN2djdb9DSANq4hvPhukCEYThcz1pVHhxRYS6jIwAI3eIUuRqxf2Hozi5Hi6bEObWkFBRwLSw08BGoegBjGCjgxUJz-XAC3BfjUXI-jal4KazHVpBOLo99ZLTdhAN1w0QrOw-gOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی ایتا و روبیکا تصاویری از یه سلاح ایرانی تو مرز ایران و عراق منتشر کردن که حتی خودشونم نمیدونن دقیقاً چیه :
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72875" target="_blank">📅 10:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72874">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78e235c72.mp4?token=EXgVkdn22zrbc2pKQRMHFlQkZ6sPCKb6pjyUpuN59DEqGon95JhMv2ZXGM5GcMwX3p8e2gKqDdlZvpxZq2dKtGXzO3neKksmu2pC5Cj9pwmHryFOXipGx4Uxf5531uHcVrS0dqbdDcHk6XRFdLiqtrQ-0twCEvDrgmw4_R9V7Cb3wnQBxlAY7mIBLt8GR0TF8kPCxRuANA1M_KDIrVKJNqkgqk8Jmo9rygJnpl64r5z-X9rYdvov2Zn_fGuPUR9YzmURat72nqu_Pdd92SlLKVDndZOUhRSi8V9B9GmYxIqA6XO1J2xi9D0CU8QZtOYgkIzc1S3yzD-x9SQ9KYOdgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78e235c72.mp4?token=EXgVkdn22zrbc2pKQRMHFlQkZ6sPCKb6pjyUpuN59DEqGon95JhMv2ZXGM5GcMwX3p8e2gKqDdlZvpxZq2dKtGXzO3neKksmu2pC5Cj9pwmHryFOXipGx4Uxf5531uHcVrS0dqbdDcHk6XRFdLiqtrQ-0twCEvDrgmw4_R9V7Cb3wnQBxlAY7mIBLt8GR0TF8kPCxRuANA1M_KDIrVKJNqkgqk8Jmo9rygJnpl64r5z-X9rYdvov2Zn_fGuPUR9YzmURat72nqu_Pdd92SlLKVDndZOUhRSi8V9B9GmYxIqA6XO1J2xi9D0CU8QZtOYgkIzc1S3yzD-x9SQ9KYOdgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک اخوند در تجمعات شبانه: ناو آمریکایی آنچنان از ترس موشک ما فرار کرد که چند هواپیمایش تو دریا افتاد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72874" target="_blank">📅 10:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72873">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ab32d7fd77.mp4?token=I0k-iF9tnNH6ZQfBmeslTNlPQQap9H5FXuVyGehjMengiaDnb92bh436N_7nlkyi4c9WEap3tX_SnQTEuEg6Xnqd203qvm9h_KBJTkS1UEJNgCbI4NDgsG5VLjpVQh6CLzBFedGjgM-kzJ-LAq22onjWxoQGj8jei0m6lyuMcS3xa4dIXCBnPG4vu-BRP1wa5acp_sTZg36AXc7zVnpENnFRlqJtdPV37ipww9NazB9Md_LwvCoh5IH5ZE2PR0EDJtL1VU41MeQbkUEoQoET35746j0xIv8Xhbk9JmiMGPCx4GTCyXSWdd4vRIRd187aSngmlg0BDRiANy_n2ADeOw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ab32d7fd77.mp4?token=I0k-iF9tnNH6ZQfBmeslTNlPQQap9H5FXuVyGehjMengiaDnb92bh436N_7nlkyi4c9WEap3tX_SnQTEuEg6Xnqd203qvm9h_KBJTkS1UEJNgCbI4NDgsG5VLjpVQh6CLzBFedGjgM-kzJ-LAq22onjWxoQGj8jei0m6lyuMcS3xa4dIXCBnPG4vu-BRP1wa5acp_sTZg36AXc7zVnpENnFRlqJtdPV37ipww9NazB9Md_LwvCoh5IH5ZE2PR0EDJtL1VU41MeQbkUEoQoET35746j0xIv8Xhbk9JmiMGPCx4GTCyXSWdd4vRIRd187aSngmlg0BDRiANy_n2ADeOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدون شک این یکی از عجیب‌ترین پرونده های فساد توی تاریخ ورزش کشوره!
یه خانم با تیمای بزرگ فوتبال مملکت قرارداد می‌بسته و می‌گفته بهم پول بدین، منم در ازاش با داور سکس میکنم تا نتیجه رو به نفع شما بگیره!
بعد از دستگیری، این خانم اعتراف کرده که با بیش از ۴۰ داور سکس داشته و باعث صعود خیلی از تیما شده!
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72873" target="_blank">📅 09:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72872">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da58b38a06.mp4?token=OeEtDiGHT6evPSHMYQLwc4zvVUcT8duT90h9wLx7ThYc4y58oYNE7BwDtYdt673rxqfQvySRo6GvjlQgAF2rMNN2rSfY-gK0_C93UwFmLPKkJ_AavsCBVzxx8Y7FoC3iifyGeJcjuNfV-r5-AygXmucUbLxkSCj0tq7I9T8TcLOYfg1a0w1er8wPrtjoprBo1FOTbcuNC1UyJEJZrdAotJun1e9qPW5z-duw_RnJNstG1n_0ds7KiefXxBAOHWE_K4VgajTO7YRWoKq5EGYoBx4RceZ54QpX7xzPiAbXPcSoPd2KK0UYPb6S2FH21o89ZTbiUTlJMUgkq0F7juFVhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da58b38a06.mp4?token=OeEtDiGHT6evPSHMYQLwc4zvVUcT8duT90h9wLx7ThYc4y58oYNE7BwDtYdt673rxqfQvySRo6GvjlQgAF2rMNN2rSfY-gK0_C93UwFmLPKkJ_AavsCBVzxx8Y7FoC3iifyGeJcjuNfV-r5-AygXmucUbLxkSCj0tq7I9T8TcLOYfg1a0w1er8wPrtjoprBo1FOTbcuNC1UyJEJZrdAotJun1e9qPW5z-duw_RnJNstG1n_0ds7KiefXxBAOHWE_K4VgajTO7YRWoKq5EGYoBx4RceZ54QpX7xzPiAbXPcSoPd2KK0UYPb6S2FH21o89ZTbiUTlJMUgkq0F7juFVhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همتی رئیس بانک مرکزی:
حداقل شش ماه اول امسال، عمده کارهایی که کردیم این بود که دو تا موضوع مهم رو به نتیجه برسونیم؛
یکی کنترل تورم، چون به‌خاطر رشد نقدینگی و فشارهای ناشی از دو جنگ پشت سر هم، نقدینگی شتاب بیشتری گرفته بود.
دوم هم اینکه توی این شرایط بتونیم کالاهای اساسی، دارو، معیشت مردم و مواد اولیه کارخونه‌ها رو تأمین کنیم.
این دوتا استراتژی اصلی بانک مرکزی بوده و خوشبختانه بخشی از اقداماتمون هم به نتیجه رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72872" target="_blank">📅 09:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72871">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اینم شیرینی مدیر به شما عزیزان
😁
امشب سه شنبه تاریخ 1405/07/14 به مناسبت تولد دخترم آیلین خانوم
♥️
از الان  تا ساعت 10:00 صبح لینک کانال vip طلا و ارز یارا را #رایگان کردیم برای 100 نفر اول
👇
꧁༒VIP CHANEL  GOLD༒꧂
🔞
ولی اینو بگم شرعا راضی نیستم جایی بفرستید…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72871" target="_blank">📅 01:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72869">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اینم شیرینی مدیر به شما عزیزان
😁
امشب سه شنبه تاریخ 1405/07/14 به مناسبت تولد دخترم آیلین خانوم
♥️
از الان  تا ساعت 10:00 صبح لینک کانال vip طلا و ارز یارا را
#رایگان
کردیم برای 100 نفر اول
👇
꧁༒
VIP CHANEL  GOLD
༒꧂
🔞
ولی اینو بگم شرعا راضی نیستم جایی بفرستید
لطفا رعایت کنید تا حق خودتون ضایع نشه
🙏
چون عضویت فقط برای 100 نفر بازه
هرکس سود کرد دخترم و همسرم رو دعا کنه
❤️
🙏</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72869" target="_blank">📅 01:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72868">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72868" target="_blank">📅 01:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72867">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hD45zIHF7oEWppHNy6ahrydKEswY5TMeLk77tOZOg4UXf1zIlu6yGk0SlxSAtQ2C9fc4rycRfFdmCb-9dUCSUD6ort4YpVzwH8WobJgNhrg8x1OdyjfbM9wyxqPVa1WMCA4sgkTuUjSfatkUWDXaEGBcFU1xzsKzLnDN4Gopas_UeOyrJZ9RW_guOJlWZauWXwI-MHcc1bjmaB-M0rIFqdpWSx0YYJVskZvHIwAdYfa3Ddb88M8PMI9eJJoWJNWyN355pnNodbaRxwFzZUKJIgayNRfOrTUYf6NElxlYaKDUhhTQtTJLZ74ZrvZnwBs4NJnnwIlvSwxmXYycxwYLXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72867" target="_blank">📅 01:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72866">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeieVgVfjK4AWlX21Q1YtERJp_2EG_x0jfQaddxKtoY0RIlnlw3hWUUWeMeXld9ayDLCuOM1bMsFHcUXtSL5PUBDCUmv6Cds8YMJ2Wmmm6F0FKe84JVekFBe6fNZc9ahNlEwYXGKF4DT9_Qe0FSxrpYwedAbg-6mWmsk4fvi8WZPJhv33N96_vvECkIkxjnGR9ys7zoOPb2fNB4Wwu2IbWejf1LxzFp7s5yCTXVYWnQqn12dfczWb6M5RpX--niCEGx4Iqr6nJXuiEnVXVpAR3xwwBdjN2XT2LeXPT4YCCcF152dMiS1YKK92MVretMDozrYcpmWZfAkIRSqRAbwQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسنت وزیر خزانه‌داری آمریکا:
«ایران یه وزیر نفت جدید داره.
با توجه به اینکه ایران از ۲۵ اوت حتی یه بشکه نفت خام هم روی هیچ کشتی‌ای بارگیری نکرده، این وزیر نفت دقیقاً قراره چی رو مدیریت کنه؟»
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72866" target="_blank">📅 01:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72865">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c65f0143c.mp4?token=De_5jnZFuO_x-xQd_Tbw8-hdEqAdORT772MCSil5mhIKaSB2ib6EKjwsQi9zf3lBHkwkaTTWnIXyO5zNIDVzhJNZE5tFkA4wcBOuVPQSYrIopJszWqhKVlbzvjIe9tvT2wa4fw6wrxVoJj2H7HZC4dZ6ytPi01SRHfZ8qNbuBAUGUo1ykI3PRdToj7JAA_mOpEoucLlx_bUED00_xKJhVlZ3VluM-lxHzIveY4TKypcNaarA5vy8VzTDM7MJeQn8xtSGt6PFaaWVU5lcYD-JGHQu8sSrhzvH91JZgNWAMELysd-uJKsufyT3ba42rZw0AcS3rVqt8_ZrATXixQNCPTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c65f0143c.mp4?token=De_5jnZFuO_x-xQd_Tbw8-hdEqAdORT772MCSil5mhIKaSB2ib6EKjwsQi9zf3lBHkwkaTTWnIXyO5zNIDVzhJNZE5tFkA4wcBOuVPQSYrIopJszWqhKVlbzvjIe9tvT2wa4fw6wrxVoJj2H7HZC4dZ6ytPi01SRHfZ8qNbuBAUGUo1ykI3PRdToj7JAA_mOpEoucLlx_bUED00_xKJhVlZ3VluM-lxHzIveY4TKypcNaarA5vy8VzTDM7MJeQn8xtSGt6PFaaWVU5lcYD-JGHQu8sSrhzvH91JZgNWAMELysd-uJKsufyT3ba42rZw0AcS3rVqt8_ZrATXixQNCPTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: درباره طاعون در روسیه، با پوتین صحبت کردید؟
ترامپ: «به‌زودی یه تماس باهاش دارم.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72865" target="_blank">📅 00:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72864">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f6433023f.mp4?token=u2NRhdLIvpBK9QgLtEtS9TjqXesRFb-whR39BOaNr__1gD1hxUv5qjc0t7HVaOV0N8ml83u2MkdqgS--Pz5Cw_GRtYEzsht5Q99E5y4v_CgdblVdCHMS7a5pTQl0TqF8cJtKsMt5NVSs50Ezofzvlk6Sqzsw7Je2oDVxqb6g2WdqGgdoby6GouRHL_H4xU6xnRmCz_BlhdoR2ZefPreOOqo-2Xsft10PsVzoimnXXUE50PzFvPQsZzbVH0vQoZ7HpitnFFDen0_egEO45zKT-EoGiG_BXSVi36mgT0tpwLsqNCEftahy6GHR1yg7VtJxzk67KhB9xtjQ2__sWjd30Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f6433023f.mp4?token=u2NRhdLIvpBK9QgLtEtS9TjqXesRFb-whR39BOaNr__1gD1hxUv5qjc0t7HVaOV0N8ml83u2MkdqgS--Pz5Cw_GRtYEzsht5Q99E5y4v_CgdblVdCHMS7a5pTQl0TqF8cJtKsMt5NVSs50Ezofzvlk6Sqzsw7Je2oDVxqb6g2WdqGgdoby6GouRHL_H4xU6xnRmCz_BlhdoR2ZefPreOOqo-2Xsft10PsVzoimnXXUE50PzFvPQsZzbVH0vQoZ7HpitnFFDen0_egEO45zKT-EoGiG_BXSVi36mgT0tpwLsqNCEftahy6GHR1yg7VtJxzk67KhB9xtjQ2__sWjd30Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«می‌گن: اوه، ما شش ماهه که درگیر ایرانیم!
ما عملاً همون لحظه‌ای که بمب‌افکن‌های B-2 حمله کردن، کار رو تموم کردیم؛ چون با اون حمله، برنامه هسته‌ای‌شون دیگه تموم شد و ۹۵ درصد دلیل این کار همین بود؛ شاید حتی ۱۰۰ درصدش.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72864" target="_blank">📅 00:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72863">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50efa3f342.mp4?token=OfIIPpASaQAuGIOFuauBgNEvw8fIXYZlv5AzimIeiXluZfnzpBU2rLWZwGIlDcg8y3KPUSZrCrASW_uWeaKkY0uZau50mJ9MCotOgDCRRbVblTvp6Lrbfvmof625mdg3Ia8penVp58dQXy-xxTsHboFEDHCW81XElNKv54OVgZqImjbR-X-xAqsUmM2tMIf9qsfr-qUxvxpNY6s6dGqVC2kU-fH4Nyi-PLyGIf0UACobBo1fcS2sghHdCQT59eZuscxJRlY_fldO5JMM7316M4UlyZLqHPVej6kTK3692nypqk8xKLbWyu7XFKQ_O34a2NHNl1YyiOvoVKRYHL1-gIVVo1cQqEzI411e7_zdiRaqm0Awgm-7KWlPwudLBQ9TBQ_bBcHEAbnQTiixB64flVzu7HzqyT8cZYIKPu57el2V0MLOG3Go9Fj_NZR0WyOdrlxTtwnr0RhSj8fcyILXxpOixm_Zs9d8sZL9riloC5MiKvOiQIBMHM9BCJPDvggBGXpbqnjFwoBbEwu6tA5sj8T6ImyXqiX3r9jH-i_qUik0mGA2qNIkFilp0X6Xo8NtJovb6HodXiu2OWrBPgbuefDMv0psqWuW2mLBwS2N3ndNh0z33apC972k2vYWZWibyq8Pr5vl26p-NmLyMFFdLLV8YCe9XE6wfyCQY0Fqnf8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50efa3f342.mp4?token=OfIIPpASaQAuGIOFuauBgNEvw8fIXYZlv5AzimIeiXluZfnzpBU2rLWZwGIlDcg8y3KPUSZrCrASW_uWeaKkY0uZau50mJ9MCotOgDCRRbVblTvp6Lrbfvmof625mdg3Ia8penVp58dQXy-xxTsHboFEDHCW81XElNKv54OVgZqImjbR-X-xAqsUmM2tMIf9qsfr-qUxvxpNY6s6dGqVC2kU-fH4Nyi-PLyGIf0UACobBo1fcS2sghHdCQT59eZuscxJRlY_fldO5JMM7316M4UlyZLqHPVej6kTK3692nypqk8xKLbWyu7XFKQ_O34a2NHNl1YyiOvoVKRYHL1-gIVVo1cQqEzI411e7_zdiRaqm0Awgm-7KWlPwudLBQ9TBQ_bBcHEAbnQTiixB64flVzu7HzqyT8cZYIKPu57el2V0MLOG3Go9Fj_NZR0WyOdrlxTtwnr0RhSj8fcyILXxpOixm_Zs9d8sZL9riloC5MiKvOiQIBMHM9BCJPDvggBGXpbqnjFwoBbEwu6tA5sj8T6ImyXqiX3r9jH-i_qUik0mGA2qNIkFilp0X6Xo8NtJovb6HodXiu2OWrBPgbuefDMv0psqWuW2mLBwS2N3ndNh0z33apC972k2vYWZWibyq8Pr5vl26p-NmLyMFFdLLV8YCe9XE6wfyCQY0Fqnf8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«نیروی دریایی آمریکا یکی از مؤثرترین و نفوذناپذیرترین محاصره‌های دریایی تاریخ رو اجرا کرده. هیچ‌کس تا حالا همچین محاصره‌ای ندیده؛ حتی یه کشتی هم نمی‌تونه وارد بشه.
اگه کشتی نفت داشته باشه، به کابینش یا سکانش می‌زنیم؛ اگه هم نفت نداشته باشه، کلاً غرقش می‌کنیم.
الان محموله‌های نفتی که از خارج ایران ارسال می‌شن، تقریباً دوباره به بالاترین سطح خودشون برگشتن.
یعنی به زبان ساده، تنگه هرمز متعلق به نیروی دریایی آمریکا و ایالات متحده‌ست؛ جای واقعی تنگه هرمز هم همینه.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72863" target="_blank">📅 00:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72862">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52bb6008cb.mp4?token=BNDxnlkHW9GZuH743iwTcw6Ph4IOtk_WQbyzr_XHjUd4bUCEpVGnZRO_TC1QH9mySkcDxVh0Y1jvyGXMmhFvTIYe_VolL9ti4oE_S1wtjjtDeVgCXKZ1bsuT11RZHYDprNVi-MyXbJllgRJ5b05HPN9bwyEBTfL1vSblt3dleiH26ShwSvHzSqlilTnDEtxjqGOFgXzNgaZFVTGM3pPm-AN-NpKVVGT4Z6Un2tOZIbbZnACrAuR3AY1dWQpyQBDwhzmB4Y8KEQ3k10aIrCTtkPne3oZa9KEsq5Nur7FSxKjzF2m1K-oZSSVWbz7Egzmq-BdmisedxQIgPTCByU673ya_ajQCsXs2hizj0d8fV4vCTJYetKex3Vi3b9YW_Ln7eqzEXzMWW9xcA91-IhoPQwikCEZgy0Cl3FUrjoivxhIboRK-UUgWvevoP2Q-qsAijEvOTz0lhoYA0mOjteB8_CVByYUDl35dyFlDTeztpgWwSWWp6vDGCjj_y72WqGDhrL93PMKEXnPe2K1MHXR_IhyU2dzrP8zsgjA3Y__ZsdZM7TAyCad2RfZvTIopPzTHjWEfn6GPqjcVQLyeSSU-MtfsoyAC52PDbUrIS8qonhdXXcFupeXkIxDlbJuvXDpBmI9v3oNs089RNzJfJTIxzPBQefiMFXzquvGZ_1ZEbdI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52bb6008cb.mp4?token=BNDxnlkHW9GZuH743iwTcw6Ph4IOtk_WQbyzr_XHjUd4bUCEpVGnZRO_TC1QH9mySkcDxVh0Y1jvyGXMmhFvTIYe_VolL9ti4oE_S1wtjjtDeVgCXKZ1bsuT11RZHYDprNVi-MyXbJllgRJ5b05HPN9bwyEBTfL1vSblt3dleiH26ShwSvHzSqlilTnDEtxjqGOFgXzNgaZFVTGM3pPm-AN-NpKVVGT4Z6Un2tOZIbbZnACrAuR3AY1dWQpyQBDwhzmB4Y8KEQ3k10aIrCTtkPne3oZa9KEsq5Nur7FSxKjzF2m1K-oZSSVWbz7Egzmq-BdmisedxQIgPTCByU673ya_ajQCsXs2hizj0d8fV4vCTJYetKex3Vi3b9YW_Ln7eqzEXzMWW9xcA91-IhoPQwikCEZgy0Cl3FUrjoivxhIboRK-UUgWvevoP2Q-qsAijEvOTz0lhoYA0mOjteB8_CVByYUDl35dyFlDTeztpgWwSWWp6vDGCjj_y72WqGDhrL93PMKEXnPe2K1MHXR_IhyU2dzrP8zsgjA3Y__ZsdZM7TAyCad2RfZvTIopPzTHjWEfn6GPqjcVQLyeSSU-MtfsoyAC52PDbUrIS8qonhdXXcFupeXkIxDlbJuvXDpBmI9v3oNs089RNzJfJTIxzPBQefiMFXzquvGZ_1ZEbdI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«من مدام از رهبران کشورهای مختلف دنیا تماس می‌گیرم که بابت جنگ ایران ازم تشکر می‌کنن.
منم بهشون گفتم: خب، خوبه! کی قراره پولش رو بدید؟
ما داریم بارِ کل دنیا رو روی دوشمون می‌کشیم. اتفاقاً از این کار هم خوشحالیم، چون خودمون قوی‌تر شدیم و بقیه ضعیف‌تر.
اونا دیگه ضعیف شدن؛ دیگه کارایی سابق رو ندارن. ما داریم کارهایی می‌کنیم که هیچ کشور دیگه‌ای از پسش برنمی‌اومد.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/72862" target="_blank">📅 00:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72861">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ درباره ایران:
«ایران یه کشور شکست‌خورده‌ست. همه دارن کنار می‌کشن و می‌رن. اقتصادشون هم عملاً به خاک سیاه نشسته.
وزیر نفت ایران هم گفته: «من دارم می‌رم، چون کشورمون دیگه تمومه.» خودش دقیقاً همینو گفته.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72861" target="_blank">📅 00:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72860">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24dabc9ec.mp4?token=Uy_bY7ZevrQn85cni5rLFLf_hqZmk5wtIph799BHvS6qJbWurAII5hm2Bg96WKKcTealXJIX2MePoHQW6ZJvPkPXrX7UYr87ab__fS7K5uXbQaf2oiPG_AP9NaRpHU_2bj_CI9eomLgDBE7JykTP5fPo-w7bry4gKiIJCaplta3g40NvvrHMxABy9u5H3PU_4uHFd-6dND1zbDazzSPZ4_XqsN-At5JXYLQjMXYUdvVB0AGZsMmvLoeb6BiycQ_BTkaAfFgjm-eu5gtrjCdVShnMFqPjLSMtmpyyHNxiq_6xubQqzDdlKL-bs7FnL7uG8So4dyLuhtIRKMpqqDWr6QMWWICMOWDtZUg6MbV2yhT6OWA7VvABqJjHHRPXfANy2UXu_uuoBnnvoeRbmhWX0m082v7CWHs7ITuzDTVp1SXk6gFYTPuucORUEuzeXKvqkniAD33k_XgQjlvyrRD6dBGgjNNfD5_lOyfzxelIPlq9e2pxKSym55hnYnrSSW7XF95GlSxfZfhU_z-8861CF7CV9q7dTpmeM5EAeM48UYlX4gp0EiLpx1BC80TChtOoqH156FAn97CYh7fpdwKQOHHl1IJn4E0jMonEI5FcN3tlQh71H_iwUmUycjWLsrkJ805ialD5bK1kYQYzobkY6J6x_49rj8DeX-FQ-bmJk3o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24dabc9ec.mp4?token=Uy_bY7ZevrQn85cni5rLFLf_hqZmk5wtIph799BHvS6qJbWurAII5hm2Bg96WKKcTealXJIX2MePoHQW6ZJvPkPXrX7UYr87ab__fS7K5uXbQaf2oiPG_AP9NaRpHU_2bj_CI9eomLgDBE7JykTP5fPo-w7bry4gKiIJCaplta3g40NvvrHMxABy9u5H3PU_4uHFd-6dND1zbDazzSPZ4_XqsN-At5JXYLQjMXYUdvVB0AGZsMmvLoeb6BiycQ_BTkaAfFgjm-eu5gtrjCdVShnMFqPjLSMtmpyyHNxiq_6xubQqzDdlKL-bs7FnL7uG8So4dyLuhtIRKMpqqDWr6QMWWICMOWDtZUg6MbV2yhT6OWA7VvABqJjHHRPXfANy2UXu_uuoBnnvoeRbmhWX0m082v7CWHs7ITuzDTVp1SXk6gFYTPuucORUEuzeXKvqkniAD33k_XgQjlvyrRD6dBGgjNNfD5_lOyfzxelIPlq9e2pxKSym55hnYnrSSW7XF95GlSxfZfhU_z-8861CF7CV9q7dTpmeM5EAeM48UYlX4gp0EiLpx1BC80TChtOoqH156FAn97CYh7fpdwKQOHHl1IJn4E0jMonEI5FcN3tlQh71H_iwUmUycjWLsrkJ805ialD5bK1kYQYzobkY6J6x_49rj8DeX-FQ-bmJk3o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ترامپ درباره ایران:
«ما توی جمهوری اسلامی ایران داریم خیلی خوب پیش می‌ریم. کل اونجا دیگه داغون شده.
باید کار رو تموم کنیم؛ فقط مونده تصمیم بگیریم چطوری تمومش کنیم: با راه خوب و دوستانه، یا یه راه نه‌چندان خوب!
خیلی زود می‌فهمید قراره کدوم راه رو انتخاب کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/72860" target="_blank">📅 00:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72859">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423715c427.mp4?token=ah9ca_ahEz0cuFAva2vhXA7ai3F7ZRrUbC-7sBb5BtM6m258MZN884SgeBkegwZVV_IqK2kMEcDnzm33zmbzd2NQ1BsZe2Sd5B-U06_ZX99oUNOlcVjyU3xB6Yc0kQmlAKaEN4w8bYjayUlm9LtEPx5u6XaFHUp2J1IJdDIR62VlYOEK49A-e2wnV5ikQMmZAe2Rj3AYEm72rcPgU7HM1tIjvhIxgmO0jSzHo_p4ehv2Qe4293wLlZXiWbdNshWX3OPD1PHcKDMnmVjvePg-Dztl7i_ySHoiC8JYRn3592Q3smqp6JJPhdvPZH6D1BW-gT6Q43I2SlZATZz8S_TrBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423715c427.mp4?token=ah9ca_ahEz0cuFAva2vhXA7ai3F7ZRrUbC-7sBb5BtM6m258MZN884SgeBkegwZVV_IqK2kMEcDnzm33zmbzd2NQ1BsZe2Sd5B-U06_ZX99oUNOlcVjyU3xB6Yc0kQmlAKaEN4w8bYjayUlm9LtEPx5u6XaFHUp2J1IJdDIR62VlYOEK49A-e2wnV5ikQMmZAe2Rj3AYEm72rcPgU7HM1tIjvhIxgmO0jSzHo_p4ehv2Qe4293wLlZXiWbdNshWX3OPD1PHcKDMnmVjvePg-Dztl7i_ySHoiC8JYRn3592Q3smqp6JJPhdvPZH6D1BW-gT6Q43I2SlZATZz8S_TrBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«یادتونه خمینی رو؟ همه‌شون دیگه نیستن؛ همشون رفتن.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72859" target="_blank">📅 00:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72858">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/484ca32fc4.mp4?token=agtP3lRdDZZUDqW5VkxDt-x-r1GP74ne327a1RENHQrdSIsynRuVjGr4eN4q4vORYCBwp2Iw66ig50xQ9p1vUjJ-EcCkCHVcRFopeflpZxWTB0nnjRCSw7ut6biUGF_OCaV_ElcILQsva0mvGgxzDvabW66XTwcXxKuju_pAVwmQKUtZ6Vtlm5FG9rjHyQ4v0eKS2lYeVzWUN8kqpXpIEGb1QA7EIsfAfhNKNgth53O6bqN3FnHRyUVoh8nJt_YAlylj93S2SVcww1BZvrPq0MAVCuru7VPgo4hZjdpX9490ENDVCxF8b-8EK7jLT3hAa_ur7NZ8JCON6xglZ1j8jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/484ca32fc4.mp4?token=agtP3lRdDZZUDqW5VkxDt-x-r1GP74ne327a1RENHQrdSIsynRuVjGr4eN4q4vORYCBwp2Iw66ig50xQ9p1vUjJ-EcCkCHVcRFopeflpZxWTB0nnjRCSw7ut6biUGF_OCaV_ElcILQsva0mvGgxzDvabW66XTwcXxKuju_pAVwmQKUtZ6Vtlm5FG9rjHyQ4v0eKS2lYeVzWUN8kqpXpIEGb1QA7EIsfAfhNKNgth53O6bqN3FnHRyUVoh8nJt_YAlylj93S2SVcww1BZvrPq0MAVCuru7VPgo4hZjdpX9490ENDVCxF8b-8EK7jLT3hAa_ur7NZ8JCON6xglZ1j8jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛پرزیدنت ترامپ درباره ایران:
«ده‌ها نفر از سران تروریستی ایران رو از هستی ساقط کردن و مستقیم فرستادن اون‌ور، پشت دروازه‌های جهنم.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72858" target="_blank">📅 00:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72857">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da78ea97a3.mp4?token=m7-rxyZRokXoFy8lkRvGRXAw3gN2Y-kjDHFBnhxBB8kAuVAxlMmHHSwe7c3XLAfQSn3bo55ay3LclDQrvsyF18p68qeeTNyfYjAdCbZTWCTdj39sVkdacePDTRFc9DwFtmRGSJMVRKWHtADwUfAZDxc1n4BQNn56fUMNfMGALZ6oBn2a-jlJ1mdrT_iU6bLLuE4_huqpzVjJpxszP3ueA337U6cObR-nFp_VNfZHZf0RQRJqw4MLzC6b221Dv_I7KXgQRX75yFhMG2AXnhB-BlRwCzsVuAXEcRI_-o8ii9aqKkYBg28aQtzLrYWFmNtV7rlMGByZQDKlflnRFajWoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da78ea97a3.mp4?token=m7-rxyZRokXoFy8lkRvGRXAw3gN2Y-kjDHFBnhxBB8kAuVAxlMmHHSwe7c3XLAfQSn3bo55ay3LclDQrvsyF18p68qeeTNyfYjAdCbZTWCTdj39sVkdacePDTRFc9DwFtmRGSJMVRKWHtADwUfAZDxc1n4BQNn56fUMNfMGALZ6oBn2a-jlJ1mdrT_iU6bLLuE4_huqpzVjJpxszP3ueA337U6cObR-nFp_VNfZHZf0RQRJqw4MLzC6b221Dv_I7KXgQRX75yFhMG2AXnhB-BlRwCzsVuAXEcRI_-o8ii9aqKkYBg28aQtzLrYWFmNtV7rlMGByZQDKlflnRFajWoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری؛محسن پاک‌نژاد، وزیر نفت جمهوری اسلامی، استعفا داد.  @News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72857" target="_blank">📅 00:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72852">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Shatel-VPN.apk</div>
  <div class="tg-doc-extra">58.4 MB</div>
</div>
<a href="https://t.me/news_hut/72852" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فیلترشکن شاتل
🔥
✅️
تازه نفس
✅️
تست شده رو همه‌ی نت ها
نصب از گوگل پلی</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72852" target="_blank">📅 00:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72848">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Tx3tteo2kBW-WzA0GewIzbcAfj_wA04fpF8unDXWVwNwAr4ELm9CXVRgc8zuwV6nNorTH1bjV2v-8C7ns2889iOuhemgGFZl7uC2C1JoERLeSZSR0CSOl7mR9J0i4jZYXsgF9Tl1qpHtIaIMDRHTssiRMsd-4RERdczCMNN0sAt64Tvh36r6-SEmPcUF4flyYyTaJQF8n2Hbf0bosF-Em-VkaRbb9HQjgJ0puB7yj-O4YEWFP50U4AiUnamtLv2GikGTxn4Zcu-bGCDVYuVEQ9iGtjneWUsVnDsWS0z2R1Jp_CU93Mt1n5d7j-aFOgVt0kxrVaKlx2vmovnU7t4mMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bIyQ5CRqmV9JGd5_x0DSXipN77yjSgL-oZ-TyHUkVFmBoJEjdf6i5VLkZwo7qz6a8ZqQ1cCFCgmXd0aRXrGhyClrN0QlJpj_FtfZdljzdB4Em2u7dbl0FO1Z8C9Ygrw-a47uBb7O0iCmg4cuPPV45m-nAkCSQ_VPrk8DlC6v2uPd3RekgVRX1tCFkVoz0UlfrybhWDh8lLD-IGcreA6-GMNwYjPb5WyvPmXSOkF0UttMs-NcIosTngyCj9y5uo5VH4BpzaF3BjBDZTJfIFLQjtMzse7DfHeQlVZBCgdG9ywoCEL1itMobRdk-hFiTaAJgO95jEwgkDbkicUpJQoxew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6fa9e6973c.mp4?token=tfwcccW4w8dDJ_IrvlfFSFOAO8yLbwzvIH09MquK1dl973VCEi5L1WKl5Yu8VQu4JkK_EGFqu5MNA8et6F5v0gdzrgsTzlZnKCb07_Jbb9VD8RBa1FobyK8b9AJplxAua0FRkLeeGfNUVAon8XDoabTzYKwFRNjIZ7_IleDas-0KngN2DV79De4ngIQKusj6EDbtWy1CZfrZeGL0Kq3BTmBGsZwQgvbRhRqJqMRvKBv4vrKZxvgdvZXOXjY5IWI_2uCQMQbv28TEKqewx2o4wyzqNdsVFgEEeYxWa6OWHdQ52C0EEpuGxjfa_qaYXFrmF1LNOI_FdHvW35qRnHAvdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6fa9e6973c.mp4?token=tfwcccW4w8dDJ_IrvlfFSFOAO8yLbwzvIH09MquK1dl973VCEi5L1WKl5Yu8VQu4JkK_EGFqu5MNA8et6F5v0gdzrgsTzlZnKCb07_Jbb9VD8RBa1FobyK8b9AJplxAua0FRkLeeGfNUVAon8XDoabTzYKwFRNjIZ7_IleDas-0KngN2DV79De4ngIQKusj6EDbtWy1CZfrZeGL0Kq3BTmBGsZwQgvbRhRqJqMRvKBv4vrKZxvgdvZXOXjY5IWI_2uCQMQbv28TEKqewx2o4wyzqNdsVFgEEeYxWa6OWHdQ52C0EEpuGxjfa_qaYXFrmF1LNOI_FdHvW35qRnHAvdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گویا صرافی ایرانیه «omp finix» که دارای امتیاز رسمی و تایید شده هم هست، پول مردم رو بالا کشید و ۳ ماهه درخواست تسویه حساب مردم رو پرداخت نکرده.
مردم هم مقابل قوه قضائیه دست به اعتراضات زدن و خواستار تعیین تکلیف و پرداخت پولشون شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72848" target="_blank">📅 23:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72847">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bd2fd9d91.mov?token=izJCjWZkFH5URZo-W0I14weZm4hQqdD7j139xo8GobWrXAPd1rMKeSKp8qqqwHHVorw6QK6SjvmS7XnL8TQKN0Qoocem0O-poFVrWDfwcF0BKi87n8vysdtsj3NpRmwKTDg5veQyTrnefhoNQiwlHBmmPu-H-6Zhes4mkU3xHPny2xZSYYeO9RR5xuEK0SP6OWhOKhTKrSSeg4wQjwSimue6-SmFAe7fjUK6vvBcSrIvSrUkvrD1NFA1OPRR5Tkesjb2UcJf6OxmPRLm3dejIP_xqFg1o_w2CNAA4rZ8CkzafiI6spVPkOm8ZbZWGLkvGVecoiv2WGAzG3Dy9tBXyyEF3DxK2VQpVsX20n1UxF3Gzmb-XWXJ_ohxBxNMireisT5y9-koYOYc7yheOfHYeQ2D7VMEdnu1yLH-AQpZhKce1I4-isiPi5gV3mYbgZ1ufgAmbnun0YWi7V3J5drAeFJMfgDo9wNZ_QRGyLjz0_8ou2bCNHlDPjVx9kPA6b2Ovbyv8deEzhpgrfc82STKHXPbF9vCzDpSDUrtOwpxkeDAqNexZ_zyhYHvez7HwZKd8HpZ2VwGm2oxrbQ4Bg5tUdVNCrzhC3YQHCp8Lt_3mq6Hi83oQ_WN_v45Yl7_dqaa9DSz1HQxyb6iuZDhTqZvp2i3kfH5vxwBOSw9_GAxV8Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bd2fd9d91.mov?token=izJCjWZkFH5URZo-W0I14weZm4hQqdD7j139xo8GobWrXAPd1rMKeSKp8qqqwHHVorw6QK6SjvmS7XnL8TQKN0Qoocem0O-poFVrWDfwcF0BKi87n8vysdtsj3NpRmwKTDg5veQyTrnefhoNQiwlHBmmPu-H-6Zhes4mkU3xHPny2xZSYYeO9RR5xuEK0SP6OWhOKhTKrSSeg4wQjwSimue6-SmFAe7fjUK6vvBcSrIvSrUkvrD1NFA1OPRR5Tkesjb2UcJf6OxmPRLm3dejIP_xqFg1o_w2CNAA4rZ8CkzafiI6spVPkOm8ZbZWGLkvGVecoiv2WGAzG3Dy9tBXyyEF3DxK2VQpVsX20n1UxF3Gzmb-XWXJ_ohxBxNMireisT5y9-koYOYc7yheOfHYeQ2D7VMEdnu1yLH-AQpZhKce1I4-isiPi5gV3mYbgZ1ufgAmbnun0YWi7V3J5drAeFJMfgDo9wNZ_QRGyLjz0_8ou2bCNHlDPjVx9kPA6b2Ovbyv8deEzhpgrfc82STKHXPbF9vCzDpSDUrtOwpxkeDAqNexZ_zyhYHvez7HwZKd8HpZ2VwGm2oxrbQ4Bg5tUdVNCrzhC3YQHCp8Lt_3mq6Hi83oQ_WN_v45Yl7_dqaa9DSz1HQxyb6iuZDhTqZvp2i3kfH5vxwBOSw9_GAxV8Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار رحیمی: از امروز اگه یک سایت یا رسانه قیمت ارز (مثل دلار و یورو) رو منتشر کنه با اون سایت برخورد قانونی میشه.
جدی‌جدی اینا فکر می‌کنن با پاک کردن صورت مسئله، اصل مسئله هم پاک می‌شه!
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72847" target="_blank">📅 23:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72844">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c58dc98573.mp4?token=gLpeHS9BQBWJDr9QyhpqF9zdkEd1LYhdlKKnmsbcQDUN8kGQJzKzF8i5txt2ig6eKwukDlw1Dx0mGdtMtOJGdUDcvtixCCXGh9Dp7oo8F9DKT2II2K9o6KFcqzrJz3Z5Gn6aH1L_cUX5zlzlQ5SXLuWE6g4JW6qA0SmI8HdhrRfcTQeRD9hVn7t8yAo3cKTKfBZgAjazf2T-b_98QUeYyYfaQTha6OP8oFGdftad5AaMpTPTMtcqobATyxjxP5lruMRcPKk_yOfcuHtR4bfJcauzaz80oF2Z97TAX8clMZO-SwKkt_g9dfAhO974uQ4d0qOVWddI8cQ4qXQ72uSKUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c58dc98573.mp4?token=gLpeHS9BQBWJDr9QyhpqF9zdkEd1LYhdlKKnmsbcQDUN8kGQJzKzF8i5txt2ig6eKwukDlw1Dx0mGdtMtOJGdUDcvtixCCXGh9Dp7oo8F9DKT2II2K9o6KFcqzrJz3Z5Gn6aH1L_cUX5zlzlQ5SXLuWE6g4JW6qA0SmI8HdhrRfcTQeRD9hVn7t8yAo3cKTKfBZgAjazf2T-b_98QUeYyYfaQTha6OP8oFGdftad5AaMpTPTMtcqobATyxjxP5lruMRcPKk_yOfcuHtR4bfJcauzaz80oF2Z97TAX8clMZO-SwKkt_g9dfAhO974uQ4d0qOVWddI8cQ4qXQ72uSKUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی بزرگ توی آب‌های نزدیک سوچی
امشب یه آتش‌سوزی گسترده توی آب‌های نزدیک سوچی روسیه راه افتاده؛
توی ویدئوها یه خط طولانی از آتیش و یه ستون خیلی بزرگ دود سیاه دیده می‌شه که از نقاط مختلف شهر هم قابل مشاهده‌ست.
حساب‌های نزدیک به اوکراین مدعی شدن این نفتکش هدف قرار گرفته، اما منابع روسی فقط گفتن یه شناور نزدیک بندر آتیش گرفته و فعلاً علت حادثه مشخص نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72844" target="_blank">📅 22:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72843">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">شلیک چندین موشک ضد کشتی به سمت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72843" target="_blank">📅 21:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72842">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ایران در اعتراض به برخورد دولت فرانسه با اعتراضات دانشجویی و چیزی که «نقض آشکار حقوق بشر» عنوان کرده، سفیر فرانسه در تهران رو احضار کرد!
وزارت خارجه ایران هم از فرانسه خواسته به تعهداتش در زمینه حقوق بشر پایبند باشه و آزادی‌های اساسی، به‌خصوص حق تجمع مسالمت‌آمیز، رو رعایت کنه.
جالبه رژیم جمهوری اسلامی که بویی از حقوق بشر و برخورد مسالمت‌آمیز نبرده میاد به بقیه کشورا برخورد مسالمت آمیز و رعایت حقوق بشر توصیه میکنه!
یه نکته دیگه هم که هست اینه که تا امروز هیچ گزارشی مبنی بر اینکه معترضی در فرانسه کشته شده وجود نداره و گزارش های رسمی که وجود داره نشون میده فقط بیش‌ از ۲۱۵نفر دانش‌آموز و ۸۵کادر آموزشی زخمی شدن.
از نیروهای دولتی هم حدود ۷۱۵ نفر نیروی پلیس و ژاندارم در جریان اعتراضات زخمی شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72842" target="_blank">📅 20:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72841">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJhm1kYnrcy90wA8RL1lSKyrP6z9DmHjrIiV1qWORHI_8_Mhuc0L7hg0mYfVlTKOoFUaJYUsB2wRHmaHJB4bowWfUklGMqq0o1rmFgDIp8h29Pwnrzgoyc4WpdjFWM2NDvl6t_GE6ez-wLVECCTPylc-BypGui313dhyIhqc8XjR0B6V7u2FbdT66iVxIDoVnSAmKInnHsv5N_nrjyUgyHez5KqJV0WWaRgmBOmdq2s3p4rWBOjXkVc8QreFjl_-JKnCqqF6e99BMF0pMVNbTcjSg0SulJn60mZpgXB02MdmC0n5DFDEezrDoxbvygS6FWPFqTlQgM1zi32DflB-8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت خیابان های فرانسه پس از اعتراضات گسترده دانش‌آموزان و دانشجویان به دلیل کمبود معلم و وضعیت بد مدارس</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72841" target="_blank">📅 19:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72840">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">#فوری
؛رایتل رسماً به مزایده گذاشته شد؛ شستا ۱۰۰ درصد سهام این اپراتور را با قیمت پایه ۱۳۰ هزار میلیارد تومان (۱۳۰ همت) برای فروش عرضه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72840" target="_blank">📅 18:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72839">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">یه مرد ۲۲ ساله بریتانیایی به اتهام مشکوک بودن به آماده‌سازی اقدامات تروریستی، در ارتباط با پرونده مشکوک پایگاه هوایی RAF Fairford بازداشت شده.
پلیس ضدتروریسم انگلیس گفته این فرد امروز توی وست‌مینستر لندن دستگیر شده و هفتمین نفریه که توی ارتباط با این پرونده بازداشت می‌شه؛ البته تا الان برای هیچ‌کدومشون اتهامی ثبت نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72839" target="_blank">📅 18:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72838">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d2245088c.mp4?token=OkfE0rzvRiEfcj5w41AYbZL4-SUlKw3XH6EUmTiGRBcbN9hOpA_KDeQuPLGWP2piMAopMSdeta2vgSgT5s8ql6H59QNJfSpFrV_gf4Ld3g5S7sL9ClbdTBAeT-xWzPxv1ZSx6ijZkxreGHuqscrc2cm42SsoDFBDtJRZprDODM1uvf3Yc1A3GcKfd7S2yHOd3O6w-W4DT21MntuY5fuu0AkkpAFVK9_IKq7r8QTiDdGeVKebiwloS0C9CjyNEQE-5-XdmuyPAt3afQd7_UZvjDpXXye1TciDAQHto3UBdfEMW2VtuRzOBk0uYrx8mMObtEImJ5VBRPwbxNSvqaawMYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d2245088c.mp4?token=OkfE0rzvRiEfcj5w41AYbZL4-SUlKw3XH6EUmTiGRBcbN9hOpA_KDeQuPLGWP2piMAopMSdeta2vgSgT5s8ql6H59QNJfSpFrV_gf4Ld3g5S7sL9ClbdTBAeT-xWzPxv1ZSx6ijZkxreGHuqscrc2cm42SsoDFBDtJRZprDODM1uvf3Yc1A3GcKfd7S2yHOd3O6w-W4DT21MntuY5fuu0AkkpAFVK9_IKq7r8QTiDdGeVKebiwloS0C9CjyNEQE-5-XdmuyPAt3afQd7_UZvjDpXXye1TciDAQHto3UBdfEMW2VtuRzOBk0uYrx8mMObtEImJ5VBRPwbxNSvqaawMYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکرون شاهد نخستین شلیک آزمایشی موشک بالستیک جدید M51.3 فرانسه از زیردریایی هسته‌ای «لو ویژیلا» بود.
مکرون:
این آزمایش، اعتبار و قدرت بازدارندگی هسته‌ای فرانسه رو نشون می‌ده:
«برای اینکه آزاد باشی، باید ازت بترسن؛ و برای اینکه ازت بترسن، باید قدرتمند باشی.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72838" target="_blank">📅 18:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72837">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b292f769f.mp4?token=KWexotKy77YeizBliO7SkbzdAsVXsC-y2Y9VMvBEwe9eKh0ZP__DvEfhl31DXaIj7wKyttPuL8VRAeEZPY75OJaIB8fIB9zv1XzrU0Ops5CfVwEYaUzROqDVVIYrbMOI2oHChgRWHYfEPBdeVOHaTT68f-LJ6YzhFnmw1EVvXKGGXvqbqeBrRrkqp9U2xsiGPac_392Zk_PV93_mxRyFT-EJJLM6jAMP4MIKhDu58KJIrgNTXy30jzdVZWN2AiXjxdKrZcu3pJBRuaCKPfPGCRmvsLV4gYFIDRba05AKFuOnftipFRBmO08KFCFqlaLFNAaUzQq-X_5qI-rmxt4cVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b292f769f.mp4?token=KWexotKy77YeizBliO7SkbzdAsVXsC-y2Y9VMvBEwe9eKh0ZP__DvEfhl31DXaIj7wKyttPuL8VRAeEZPY75OJaIB8fIB9zv1XzrU0Ops5CfVwEYaUzROqDVVIYrbMOI2oHChgRWHYfEPBdeVOHaTT68f-LJ6YzhFnmw1EVvXKGGXvqbqeBrRrkqp9U2xsiGPac_392Zk_PV93_mxRyFT-EJJLM6jAMP4MIKhDu58KJIrgNTXy30jzdVZWN2AiXjxdKrZcu3pJBRuaCKPfPGCRmvsLV4gYFIDRba05AKFuOnftipFRBmO08KFCFqlaLFNAaUzQq-X_5qI-rmxt4cVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل: هر موقع میرفتم خونه و می‌دیدم کفشای لِه و درب و داغون پشت دره، می‌فهمیدم مجتبی خامنه‌ای اومده :))
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72837" target="_blank">📅 18:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72836">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72836" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72836" target="_blank">📅 18:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72835">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfwyaBsNTTry3Aoq-l-NVAwmY860NQSVlbRWr1zNxvLv7cNWd8p3uz8wvaW6Bc2FtCxvrYz1IZESiGbEd1d85xcV9VRYwospx3vtop3D6FT8rKYoBg2OR-pNZ5dOMedFXqEQU0uNFdgev-yxF7kHWLAXe0u3QZl5Z2NqdqWA47mlLtHSMJdTlA0-6zl8Mjfm5x5qJwtNQ3EetQvNHbaSTZCLfasjSoMuXYJGxfsag2pabkmPoGP_btu_kAUGMet1m-CLUTstTHdLBvooB7DAh1zSKMSEoByQzMoqyISpBrxwFYByMDcj5QD4ZompanaaCaydoyTbPcKcilQHkE_nxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72835" target="_blank">📅 18:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72834">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مارکو روبیو درباره مورد مشکوک طاعون در روسیه:
«فکر می‌کنم روسیه باید اطلاعات بیشتری رو در اختیار دنیا بذاره. کاری که باید انجام بدن همینه و امیدواریم همین کار رو بکنن.
ما هم داریم موضوع رو خیلی دقیق زیر نظر می‌گیریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72834" target="_blank">📅 17:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72833">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab24bbc88d.mp4?token=G2kfSZfogCT7yeNciZZcA19hucgZHqYOZ-favgNmZhL8dZqiuDt0qs0LfbAgCu-O9elT-AEBLopuWd7s2TxiPRbtu49UgPW4OyI68aeG5LTEvfp4pSqzWXAR_K7F44qhuQjzLxD0aZnyD5j5EcI_8ERpnuyobcKGZpyjDzCK6wAlmThkVokL2K6AYpG2-YFydi3FN2YhACgCPIHmEpkSuwFnu1N89RjhfHXtkgGDTxNwEW4OVZb3hUsnXa0ISGPnK2jSWk2LQbkHPlo4zaqIX5WpSFdlXP1QiekMgO-ikG7I713uFPlg-VqgxE3Z7fMxgddkb2GlaXTMBA7ILeaeuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab24bbc88d.mp4?token=G2kfSZfogCT7yeNciZZcA19hucgZHqYOZ-favgNmZhL8dZqiuDt0qs0LfbAgCu-O9elT-AEBLopuWd7s2TxiPRbtu49UgPW4OyI68aeG5LTEvfp4pSqzWXAR_K7F44qhuQjzLxD0aZnyD5j5EcI_8ERpnuyobcKGZpyjDzCK6wAlmThkVokL2K6AYpG2-YFydi3FN2YhACgCPIHmEpkSuwFnu1N89RjhfHXtkgGDTxNwEW4OVZb3hUsnXa0ISGPnK2jSWk2LQbkHPlo4zaqIX5WpSFdlXP1QiekMgO-ikG7I713uFPlg-VqgxE3Z7fMxgddkb2GlaXTMBA7ILeaeuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زن بیژن مرتضوی : مردم ایران در دنیای واقعی خیلی خوشحال و شاد هستن ، واکنش ها تو فضای مجازی دروغ هس و حقیقت نداره
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72833" target="_blank">📅 17:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72832">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4be4d4d973.mp4?token=bZswq5MoOSAHu82pukQE2GX7YjKzGdeZDILUbPk4f9OP-EAa41s1twxwOg2Fi0plu0bGMH1t7XJ8Mg-Um_zRbvaMQeRpChnnTSRIkplBtxhrfep2nUghlLGnTdFgeCz3tevdA_w75CTmzi_4L4bbklmqrCRUINpqxOTblsklvZRlrDDxbjwUGov64NkOhs15MWxtOAnd-6F1iYHDCtSh3YEV_XSQL9YfcQ_DEu9TgfUHotbCzPLzUVTbusyEV9lzL5HB9s_rnFll3PDbJ0SUTDCYfIWy5bgEJzurnBropYkplK2GsmcPrvnu7JYUD8zR2MapwmW_K6iGNY3NMHmhwIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4be4d4d973.mp4?token=bZswq5MoOSAHu82pukQE2GX7YjKzGdeZDILUbPk4f9OP-EAa41s1twxwOg2Fi0plu0bGMH1t7XJ8Mg-Um_zRbvaMQeRpChnnTSRIkplBtxhrfep2nUghlLGnTdFgeCz3tevdA_w75CTmzi_4L4bbklmqrCRUINpqxOTblsklvZRlrDDxbjwUGov64NkOhs15MWxtOAnd-6F1iYHDCtSh3YEV_XSQL9YfcQ_DEu9TgfUHotbCzPLzUVTbusyEV9lzL5HB9s_rnFll3PDbJ0SUTDCYfIWy5bgEJzurnBropYkplK2GsmcPrvnu7JYUD8zR2MapwmW_K6iGNY3NMHmhwIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوش چشم بازم تحلیل کرد و گفت جنگ در پیشه!
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72832" target="_blank">📅 16:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72831">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd2b481530.mp4?token=FGku_vtEh4VRt6Yrf2U_BFTPTiteAZxa6FEQCh9WAt-ldsjDd3zXIzdHyj2R7zc-f5i12CV9eCnKz-eqZKNh8Ll3lwGdvP3WFRZramY-eXMsg8jahG_vuthwkygXJc5gPhGgZv8nrVc-sgBpHlvXWb_XFW1pvZctXVfN6uEiz4c7Zac4Qy5JQxkoMdAKMy8VNpQ7V67Ji_3FkxD9-iVzXbbPj1XD21tsP7x54OuVM_vQNzllqTsWUz8DuU_S2uLUBOaIHn31IuEEhZ9Ydokca7-61oWVmFySqWeCdkg99TE5ZI8OOWUHXC5JLLws_mte_J2kjMc6b4VQadNx3fxpjg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd2b481530.mp4?token=FGku_vtEh4VRt6Yrf2U_BFTPTiteAZxa6FEQCh9WAt-ldsjDd3zXIzdHyj2R7zc-f5i12CV9eCnKz-eqZKNh8Ll3lwGdvP3WFRZramY-eXMsg8jahG_vuthwkygXJc5gPhGgZv8nrVc-sgBpHlvXWb_XFW1pvZctXVfN6uEiz4c7Zac4Qy5JQxkoMdAKMy8VNpQ7V67Ji_3FkxD9-iVzXbbPj1XD21tsP7x54OuVM_vQNzllqTsWUz8DuU_S2uLUBOaIHn31IuEEhZ9Ydokca7-61oWVmFySqWeCdkg99TE5ZI8OOWUHXC5JLLws_mte_J2kjMc6b4VQadNx3fxpjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدنی وزیر دلقک اقتصاد: درمورد قیمت ارز از همتی سوال بپرسید.
خبرنگار: همتی هم گفت از شما سوال بپرسیم.
مدنی دلقک: نه دروغ میگه از خودش بپرسید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72831" target="_blank">📅 16:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72830">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cac062b9b9.mp4?token=TXif2UlV-v6qc2hzH-zibjcIg9EZHFAXHnEyShlggLC5dg8r-YPxHwVAXrxgFqOlijZc2sVwqu7NHnNcDgzzTDEkWBXP7otqruyYq-HR9Hs-eXeLvmPO1iZwKnayerJvPjZwTnuCDYcnMETJ3tE-Sf2on6tB2EYiRSp1LVS3jhUtmaTRRXEAmGX1ZR_d0lGEqaCidnDM87Wx0I98ThZG6orW1I22_AtR1otY07c1VN74aO8ugkn_T_jRWivKxFPS6zLaomw2Oh4dlIlguRd4FuEM-YoA5Q56VL0JPUmqWW1eTa5PonX937Jo6gct3iLLlcXzw8oCG6qelVOR19GR_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cac062b9b9.mp4?token=TXif2UlV-v6qc2hzH-zibjcIg9EZHFAXHnEyShlggLC5dg8r-YPxHwVAXrxgFqOlijZc2sVwqu7NHnNcDgzzTDEkWBXP7otqruyYq-HR9Hs-eXeLvmPO1iZwKnayerJvPjZwTnuCDYcnMETJ3tE-Sf2on6tB2EYiRSp1LVS3jhUtmaTRRXEAmGX1ZR_d0lGEqaCidnDM87Wx0I98ThZG6orW1I22_AtR1otY07c1VN74aO8ugkn_T_jRWivKxFPS6zLaomw2Oh4dlIlguRd4FuEM-YoA5Q56VL0JPUmqWW1eTa5PonX937Jo6gct3iLLlcXzw8oCG6qelVOR19GR_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراد ویسی:
اسرائیل توی ۱۴ ماه گذشته اسم ۱۴ تا خیابون و بزرگراه توی تهران رو عوض کرده! اونی که عملاً داره اسم خیابون‌های تهران رو تغییر می‌ده، اسرائیله؛ اسرائیل همین‌جوری مقام‌ها و فرمانده‌های سپاه رو می‌زنه، بعد شورای شهر میاد اسم همون‌ها رو می‌ذاره روی خیابون‌ها!
دفعه قبل هم بعد از جنگ ۱۲روزه، اسم چند تا خیابون و بزرگراه رو گذاشتن به اسم حاجی‌زاده، سلامی، باقری، رشید و شادمانی؛ یعنی اسرائیل اینا رو می‌کشه، شورای شهر هم جلسه می‌ذاره که خب حالا اسم کدوم خیابون رو بذاریم به اسمشون!
در واقع اونی که داره اسم خیابونای تهران رو عوض می‌کنه، نتانیاهو و موساد و نیروی هوایی اسرائیله؛ شورای شهر فقط می‌مونه و تابلو رو عوض می‌کنه!
با این حساب، اگه همین روند ادامه پیدا کنه، باید منتظر باشیم هر بار اسرائیل یه مقام دیگه رو هدف قرار می‌ده، تهران هم یه خیابون دیگه به اسمش دربیاره!
یعنی خلاصه تقسیم کار اینه: یکی می‌زنه، یکی تابلو می‌زنه:)
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72830" target="_blank">📅 15:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72829">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/le7XtEAKDnGGwl_Joclv6MEFiSobBewmmg6-MOcSKb9iQGBWEanJwn2ZsiTXUt3C9PKzAWPtUExLQ78PopXa0IyLss9IeVpPDVV3rNZpBYDtvmHgFPbS_r2zx_ZdtEbLIFvPtCtMQ3SAq0ry9jHGnutRiiEKfDik_XCibjfFj9FPs9WqKfYtgGQ77888sMOnFGhn6pYE4X967OUztAm0rMLqh3Dqfb7olil4L7VNy6I1xa3FuKCfWmBG7LesQyesNTkmq_ODvX7D-RMyNdoy7etpKhEaFkJCfICf-KMoCGw7prCGvcS0V8PhqajlovexZlI2J2se_D0bPIXyTZ2YsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماتون بریزه از تاثیر سهمیه! توی کنکور امسال یه نفر رتبه‌اش ۸۱ هزار شده بوده،
که با سهمیه ۲۵ درصد، رتبه‌اش ۲۸۳ شده!
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72829" target="_blank">📅 15:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72828">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2512f994a.mp4?token=EFhm8hISNtjzqYw9WZnE2-IiKsQMmtWUg1ZAhn-mKtb49TNK8IpYLVGfMpWtsy27ZyEj4jEnikTHCyM447oUgRv9vvwq69gD1EeXo7nd81LUXVgiKOQihTlYekpHQ78ICseCG5KdHSgD4sn65IvdMKqgNwOUEfWSw6AzHYiPW0apz9o_i2bZhwpBQA7RGrd88Boyf7Isdy-Zi6iPqvCrmPJfmLU-bChqdGvcL-fH8h6Aoc1g4y2arxxJ1d2voUxQgA5aEqTFZbvh46Tti1cQgaDAJz3K8mTLtghrtls7WpA37XXG8E6tAkiujYVGBmddwKxZ5RYxwIhbx1lPzxw1oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2512f994a.mp4?token=EFhm8hISNtjzqYw9WZnE2-IiKsQMmtWUg1ZAhn-mKtb49TNK8IpYLVGfMpWtsy27ZyEj4jEnikTHCyM447oUgRv9vvwq69gD1EeXo7nd81LUXVgiKOQihTlYekpHQ78ICseCG5KdHSgD4sn65IvdMKqgNwOUEfWSw6AzHYiPW0apz9o_i2bZhwpBQA7RGrd88Boyf7Isdy-Zi6iPqvCrmPJfmLU-bChqdGvcL-fH8h6Aoc1g4y2arxxJ1d2voUxQgA5aEqTFZbvh46Tti1cQgaDAJz3K8mTLtghrtls7WpA37XXG8E6tAkiujYVGBmddwKxZ5RYxwIhbx1lPzxw1oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کشور چین واقعا عجیبه، روی یه شهرک یه شهرک دیگه هم ساخته شده. شبیه فیلم inception شده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72828" target="_blank">📅 14:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72825">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ANM0EKGPkIJ61aoBjTmvEKmDuppy9VtYpyvuwwhtz7kZ3nPV-Eufksj32kJBvB7vU7msPVNdwFQczcDK4kNcbKq7Lrpk0P2azyc7GAp2Al-JEQar18thi06WfFVcPdOsQjwJm_8cJ-LO4XNI9WRMLpiD0WAWZzdmMuTkb7eVvZc_VeVMNBtzb9r4XK8zfifkDqYd3DjDVO4DtOYIboZZF4JnwAfee8rHDmbHZaHpUVBXh7IxHyaBq3dzKxqcEY0wuCySUSSKRugmLkwoEaZgt4563a24p-hSIFgPWh0XHNARUNWkqZWfoYq4OccGk9kCp10VKkbXXT0aQwGRYRUrJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OkG-keXzZ3yz8Ob03zlkS1HLpzwroWRhlFcI6zTF9n_igLvRp5gR8FeY1r3rMB3zVY19hWACvaO4XK-7Fg68vC0TAbzp23uQMetFMmrf8cxLf2tKJrwpDtAPEjzpmEJxFA0j1M85EmxZbuQsTc1m2hjlftGOjD2BeD10tUfS3QTBEFtnuphuuS9PYwbr-dvfyPrTABCynndmWQddkA-GLMSs7MKxGxWWAaohlRHWITLg0PIwAeoU5JUklvNhlRDQ10CHcQzcnu2QjtCvQS0krmF0sZU8MIqg-CH4nKTyUBQMmNTcpnSLCJWPzeFs6lUw5x07EmXWJIwlM1hZOm7h2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e31c23155.mp4?token=ANeIj_9NgDKn9nQXBEkShG1KvipSsUxDBRfke0ZWMY5zwmlkvImEXNOnWTPTMVnkHelSOOjLp5ZTiW1_f1WGeorsYirjhlVkKqPqtkQXTWYAxL2yyXbCXwFohqjwNa0OS8sTk9K2tHNggf8V0_xGNOyXV3uO5LgwJwwwC-p9PvzrDOIy312-FbQAg1v85EC-EUvtAqOH6kQ6_JqixV_LYF4XEq0N7yVMDwIu9AQG0n68FI2UUGO5hxiZYammY56OGSBKi05owqpzN-VeKJdYFf7djGEXZkyUSe55GJhYHLYQrih_MoIef2dmHMYxop1a6cSSrjnm3GJ5YagkhOrUoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e31c23155.mp4?token=ANeIj_9NgDKn9nQXBEkShG1KvipSsUxDBRfke0ZWMY5zwmlkvImEXNOnWTPTMVnkHelSOOjLp5ZTiW1_f1WGeorsYirjhlVkKqPqtkQXTWYAxL2yyXbCXwFohqjwNa0OS8sTk9K2tHNggf8V0_xGNOyXV3uO5LgwJwwwC-p9PvzrDOIy312-FbQAg1v85EC-EUvtAqOH6kQ6_JqixV_LYF4XEq0N7yVMDwIu9AQG0n68FI2UUGO5hxiZYammY56OGSBKi05owqpzN-VeKJdYFf7djGEXZkyUSe55GJhYHLYQrih_MoIef2dmHMYxop1a6cSSrjnm3GJ5YagkhOrUoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم یکی از همون ناوهای آمریکاییه(USS Delbert D. Black (DDG 119)) که سپاه تو بیانیه‌ها گفته بود موشک بالستیک خورده و «خسارت قابل‌توجهی» بهش وارد شده. ولی خب، به نظر من برای ناویی که موشک بالستیک خورده و خسارت قابل‌توجه دیده، زیادی سرحال و سالمه!
الانم برای استراحت چند روزه خدمه، وارد پوکت تایلند شده و بعد از تمیزکاری جلبک ها مثل روز اولش می‌شه!
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72825" target="_blank">📅 13:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72824">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdf3b5b159.mp4?token=hFEdkAbACXpTZawKqF2hLLtUlPiKQxArdhWCQunlZBLRguyO-4bvQt1FYiHl08xsMUaR8mFC7Fiq-sNrPDUMSB_TMM7x-fTeMz4-0nQI6JjyD6XyhzMUzszDMh_tijyhJu0YEpvsfxGHPl0J_IEr0ytAiKU-FSHVV-VriHbYBPE_jSiCTSjUKfql2II-zlsncVhSFvuRUK8jdIlqmDDlvoFGrEeBzHzj30Yo_GqnrO2BwSC9Gs9BzOlob0HyG29FxP9decxvwlp1pOdJaVMcmowPSwmQ5zOYIFhckcIhYd-6ZiaAcAM7FCiuvxntrVnPYeaYgUW6--b5NUGAwUKWuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdf3b5b159.mp4?token=hFEdkAbACXpTZawKqF2hLLtUlPiKQxArdhWCQunlZBLRguyO-4bvQt1FYiHl08xsMUaR8mFC7Fiq-sNrPDUMSB_TMM7x-fTeMz4-0nQI6JjyD6XyhzMUzszDMh_tijyhJu0YEpvsfxGHPl0J_IEr0ytAiKU-FSHVV-VriHbYBPE_jSiCTSjUKfql2II-zlsncVhSFvuRUK8jdIlqmDDlvoFGrEeBzHzj30Yo_GqnrO2BwSC9Gs9BzOlob0HyG29FxP9decxvwlp1pOdJaVMcmowPSwmQ5zOYIFhckcIhYd-6ZiaAcAM7FCiuvxntrVnPYeaYgUW6--b5NUGAwUKWuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه خانم طرفدار حکومت:به پسر نوجوانم گفتم اصلاً نگران نباش!
خواستی سیگار بکشی، بگو خودم برات می‌خرم؛
خواستی قلیون امتحان کنی، با بابات می‌بریمت سفره‌خونه؛
فیلم مثبت۱۸(پورن) هم خواستی ببینی، بیا با هم ببینیم! این‌طوری دیگه خیالم راحته که همه‌چی کاملاً تحت کنترله!»
@News_Hut
😐</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72824" target="_blank">📅 12:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72823">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e258d805f.mp4?token=o9NpQ9J5aCk4DUxnv-K5gw0J8SHaDvlnhmjat18n489boYvIa8v2B4gumRwbBKl60jwSqccbI2Qfqa6wuUJWLnf456o0T3CYyZpwzpIIciEW4Br4Dg7JiLP03W2OgANQ5QqTbyFCMGZtY-A72s5rmSvJQLUaFrgRzy9XMJBfj8DSGJgYYFWFHD7YsBJQ2NnmjBZ5uaV7RAZZSZ_wg6mTy_gNM8KxlS58mr0e2of1nRX1wJUWXJE2Fp-5gIRz-4oGBrCI9iXAY7zhY8x0UXqM_ZO3c15ZECde-7Mghun39ft2rxV5bIrnJYDpyL2theuCKx9Vgw_3GfhNIbWWyTaWbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e258d805f.mp4?token=o9NpQ9J5aCk4DUxnv-K5gw0J8SHaDvlnhmjat18n489boYvIa8v2B4gumRwbBKl60jwSqccbI2Qfqa6wuUJWLnf456o0T3CYyZpwzpIIciEW4Br4Dg7JiLP03W2OgANQ5QqTbyFCMGZtY-A72s5rmSvJQLUaFrgRzy9XMJBfj8DSGJgYYFWFHD7YsBJQ2NnmjBZ5uaV7RAZZSZ_wg6mTy_gNM8KxlS58mr0e2of1nRX1wJUWXJE2Fp-5gIRz-4oGBrCI9iXAY7zhY8x0UXqM_ZO3c15ZECde-7Mghun39ft2rxV5bIrnJYDpyL2theuCKx9Vgw_3GfhNIbWWyTaWbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سال 2023 یه میم به نام Opium Bird خیلی وایرال شد که یه موجود بزرگ و پرنده‌مانند تو کوه‌های برفی رو نشون می‌داد و سازنده‌اش گفته بود که سال 2027 (۲ ماه و ۲۶ روز دیگه) می‌فهمید یعنی چی؛
حالا شباهت Opium Bird و طاعون
👺
و همچنین لوکیشن برفی اون میم و آب و هوای روسیه، دوباره همه رو داره به این فکر فرو می‌بره که نکنه داریم وارد یه سیزن جدید می‌شیم...
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72823" target="_blank">📅 11:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72822">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dc05a4717.mp4?token=cuw19W8nzcpWpEYL8wje0QrFufv_PG7QtUbqYv_fkQ8s-7irqr2kOE6FCG2PoZnV0pzPF8nVVe_7m2HTUtqr1AcprVDLcrGVFfZR73rp94m1CToHroVJnvVyCZSpOSioobFyeT3jJDuN9O2IsIXtaHfktTBc0TduuU56f64Sp1nfBsJ3J5j5SiD8eDnfh-XFb0DZ3qsqRwBh1L53QBdkiKW4IUcXcWeGAUHT_cs1LOVRPkaxNbkgsABz6w1Zd9KOCZW4grh9hN3N1LvvYTTrmMU5TbBXRaM9XCLFnkuEJwSzxwbs0-QDCeWTOJu-h0BZcZCMMWreaVT4HRHWTXtOEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dc05a4717.mp4?token=cuw19W8nzcpWpEYL8wje0QrFufv_PG7QtUbqYv_fkQ8s-7irqr2kOE6FCG2PoZnV0pzPF8nVVe_7m2HTUtqr1AcprVDLcrGVFfZR73rp94m1CToHroVJnvVyCZSpOSioobFyeT3jJDuN9O2IsIXtaHfktTBc0TduuU56f64Sp1nfBsJ3J5j5SiD8eDnfh-XFb0DZ3qsqRwBh1L53QBdkiKW4IUcXcWeGAUHT_cs1LOVRPkaxNbkgsABz6w1Zd9KOCZW4grh9hN3N1LvvYTTrmMU5TbBXRaM9XCLFnkuEJwSzxwbs0-QDCeWTOJu-h0BZcZCMMWreaVT4HRHWTXtOEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«همه دارن می‌گن من GOAT ـم، یعنی بهترینِ تاریخ.
من می‌گم: «پس واشنگتن و لینکلن چی؟» اونا هم می‌گن: «شما از اونا هم بهتری، آقا!»»
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72822" target="_blank">📅 11:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72821">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/affe4d122e.mp4?token=nvYzKSUewGlMO3ruPFO9fngMm9gl8S7lbmNHdvwxS65ydsgEaUnGJt2iR5GTVH-b8nymARVIWOaVouPHbjZs3uw9i_mPA42boUskNYEU55sNRbLin9QpBcQ2DCFteLcQ_DKzfByBAqbBOTku-UY1on8RnEWWAwlfEQ5seYWNbM-Y6LG0rp0gW220oq7jMjuES2YKMzNseEXqEnluEZjbNFOS89yXpKOiYyTbTw9EZoSCbLB_Zh3LP6gLoKRFZINVxDlxYZzRA3IvmZ3WgZjoVm67p9yO3yF280Z4bpmhBIbFAQjP3_Gipe_snVLtyNlFWZkMjx6LmoGs08S6Kh16Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/affe4d122e.mp4?token=nvYzKSUewGlMO3ruPFO9fngMm9gl8S7lbmNHdvwxS65ydsgEaUnGJt2iR5GTVH-b8nymARVIWOaVouPHbjZs3uw9i_mPA42boUskNYEU55sNRbLin9QpBcQ2DCFteLcQ_DKzfByBAqbBOTku-UY1on8RnEWWAwlfEQ5seYWNbM-Y6LG0rp0gW220oq7jMjuES2YKMzNseEXqEnluEZjbNFOS89yXpKOiYyTbTw9EZoSCbLB_Zh3LP6gLoKRFZINVxDlxYZzRA3IvmZ3WgZjoVm67p9yO3yF280Z4bpmhBIbFAQjP3_Gipe_snVLtyNlFWZkMjx6LmoGs08S6Kh16Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«این جنگ خیلی زود تموم می‌شه و قیمت‌ها هم قراره حسابی بیاد پایین. شاید حتی خودتون بگید: «خواهش می‌کنم آقا، این‌قدر سریع ارزون نشه!»
😂
خودتون ببینید تو یه مدت کوتاه قراره چه اتفاقی بیفته.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72821" target="_blank">📅 11:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72820">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67e9f8cbdc.mp4?token=QLJLKwjNFBfHAPNVPgiJZj1bsITFC40NAfA7PIfwFDhUxQA2lagUTYAs2yxRSRY0AQPTlYH5rQBYDer7L-BydIFb4TNeSzwwQbxSsu22mSrdkpsIqVo9u7YHSIns6x-cvjhVRZyLG4kr0MEvy7SJEhuFPiBZNVyI4wcATRSGWkMvj3oxnP1siqfzRkcrZU1Nrc5c4Fa1l9SgY2BD1BXdYvRolJVWeCCdLDn0ZEEpniG5DAxutGbZLU5uK7i_5R_r4aMCQwZF9MI0CYywIfF10fCEqCmJQC1wfGjpJHk1qbqUUVfTZ6_y7DKwkU1VBrFRvXiiaN421aPa-6MRqAHWfxCe-Ctd04ruZzwqB_MMoNhtXgJPGINJ7QE9Vtkd5jzGH8dt89tyhGpLuYPY1unxBmc0B4ujyog3oE0bm_H8B0uFX9opw8ycytQQ3Ek1Pk65GJhOjp4TlD6GUJ4nV_lNkrIhKqHF92QbTxNDKFosASl6-ggB41OcdbgMGOKlLPnYAzeE_Dr0nAmUgsbdAp_uAce_upY_TltmW3NOGF_GA4qolbxX7Mbf0bZTHo1oUxydb2QhZqSQ8YL_UHN2uzjYXZc1xj0ZZGFfdtaQIzq3WV6Ydlozt-0MQZBw5yTN8cuP-BQ0i0UnSOuzjcgr2d8UHvJFuB2sezUvgH4L2_5hens" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67e9f8cbdc.mp4?token=QLJLKwjNFBfHAPNVPgiJZj1bsITFC40NAfA7PIfwFDhUxQA2lagUTYAs2yxRSRY0AQPTlYH5rQBYDer7L-BydIFb4TNeSzwwQbxSsu22mSrdkpsIqVo9u7YHSIns6x-cvjhVRZyLG4kr0MEvy7SJEhuFPiBZNVyI4wcATRSGWkMvj3oxnP1siqfzRkcrZU1Nrc5c4Fa1l9SgY2BD1BXdYvRolJVWeCCdLDn0ZEEpniG5DAxutGbZLU5uK7i_5R_r4aMCQwZF9MI0CYywIfF10fCEqCmJQC1wfGjpJHk1qbqUUVfTZ6_y7DKwkU1VBrFRvXiiaN421aPa-6MRqAHWfxCe-Ctd04ruZzwqB_MMoNhtXgJPGINJ7QE9Vtkd5jzGH8dt89tyhGpLuYPY1unxBmc0B4ujyog3oE0bm_H8B0uFX9opw8ycytQQ3Ek1Pk65GJhOjp4TlD6GUJ4nV_lNkrIhKqHF92QbTxNDKFosASl6-ggB41OcdbgMGOKlLPnYAzeE_Dr0nAmUgsbdAp_uAce_upY_TltmW3NOGF_GA4qolbxX7Mbf0bZTHo1oUxydb2QhZqSQ8YL_UHN2uzjYXZc1xj0ZZGFfdtaQIzq3WV6Ydlozt-0MQZBw5yTN8cuP-BQ0i0UnSOuzjcgr2d8UHvJFuB2sezUvgH4L2_5hens" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«یادتون باشه، این جنگ یه چیز مصنوعیه؛ یه مقدار هزینه‌ها بالا رفته، ولی خب برای اینکه دنیا امن بمونه، قیمت زیادی نیست.
اگه اونا بتونن یه شهر رو بزنن، بذار لس‌آنجلس یا سن‌دیگو رو بزنن؛ این در برابر حفظ امنیت دنیا، قیمت خیلی کوچیکیه.
در واقع، این ماجرا تقریباً دیگه تموم شده.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72820" target="_blank">📅 11:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72819">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb2e238707.mp4?token=hFQJm_ouQFQpVM64hZI2TEGjF3h5zllxHlji2_GZcZrE6brfE7142oweTdr3aj4DfNyNOPaTYtXYYVLpc2wAGaAICF4sYmE8fxuzXskWqvRVazQaVSrVAVGOJe3bBJq2tGw4ZTrXj1VvLi9HjLFzitVuLiKeLIxrvxAzSvKW91WS-Uood4aSRi0Tw8yCUT1InujCGj4LxUy20N5aOqEAaBS-upGQd9eIfES12vnqIn2MwtzZOWPq_H_42Niw6fHtWlOmkMUddrlKcz6ipsnCpkRHqSPErEYTFQRcMc9n07lmFdKh0w5xMi00EOxbF5Zp9YfqCeOyPRizbCzLPyOMRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb2e238707.mp4?token=hFQJm_ouQFQpVM64hZI2TEGjF3h5zllxHlji2_GZcZrE6brfE7142oweTdr3aj4DfNyNOPaTYtXYYVLpc2wAGaAICF4sYmE8fxuzXskWqvRVazQaVSrVAVGOJe3bBJq2tGw4ZTrXj1VvLi9HjLFzitVuLiKeLIxrvxAzSvKW91WS-Uood4aSRi0Tw8yCUT1InujCGj4LxUy20N5aOqEAaBS-upGQd9eIfES12vnqIn2MwtzZOWPq_H_42Niw6fHtWlOmkMUddrlKcz6ipsnCpkRHqSPErEYTFQRcMc9n07lmFdKh0w5xMi00EOxbF5Zp9YfqCeOyPRizbCzLPyOMRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: جنگی که علیه ایران راه انداختیم برای «
نجات دنیا
»ست!
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72819" target="_blank">📅 11:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72818">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/225b755540.mp4?token=Om5VZWNb5TJab02nIOlkIfibnLmFGfq5_fxOVpy9aoIADaq8RfKDlvI8GKPvSkRe-lyOJJP9qLQOg50J57r-YM2CXm4gng7jvvj1zAH6GxmV4e_sCTkRtZTrdqN8FNzO4cnV9NhXGQcLXTXFyMYjOglQe3UvaladcbwPezGJeZs-eAi_E3WxQPm0s4gnuliBmtbEaFMzCMxtj0bizkmMH_XdkH_2Ha_9NBEVEQX_NVZYHHQiBqZi1eD-n6i70jOA1Ce-EtozsYaVAaCAJFBmdmUWvIeinsmm4RTd5iH2r83mVsUclEgGsuMZD65XDiDAi1K5PTsHU1nQDvvUVi9_roi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/225b755540.mp4?token=Om5VZWNb5TJab02nIOlkIfibnLmFGfq5_fxOVpy9aoIADaq8RfKDlvI8GKPvSkRe-lyOJJP9qLQOg50J57r-YM2CXm4gng7jvvj1zAH6GxmV4e_sCTkRtZTrdqN8FNzO4cnV9NhXGQcLXTXFyMYjOglQe3UvaladcbwPezGJeZs-eAi_E3WxQPm0s4gnuliBmtbEaFMzCMxtj0bizkmMH_XdkH_2Ha_9NBEVEQX_NVZYHHQiBqZi1eD-n6i70jOA1Ce-EtozsYaVAaCAJFBmdmUWvIeinsmm4RTd5iH2r83mVsUclEgGsuMZD65XDiDAi1K5PTsHU1nQDvvUVi9_roi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«راستی، داریم حسابی ایران رو می‌کوبیم، اینو که می‌دونید دیگه؟!
در هر صورت، این داستان خیلی زود جمع می‌شه.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72818" target="_blank">📅 11:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72817">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72817" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72817" target="_blank">📅 11:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72816">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjtXJv_rH-_IAF_ICfywRunhce-vWH1_55P-VPu9L1J7hr1JaSSmko-cNwfXhYu4t_jMtg2vhwM-ffFQrJe7nPEUX5dG2rrOmhDScdYcUKtcKkE7U55-17T_4RCOzgeU-w1xxqHdfHbpvcCVBENYdIWNzx_FQ5bTJ3lYO284deFYCXX5xIYrAObKTvWFxwXiC06W7DD96J1NcR7uZ-CE6PFd9W45O3UCI4bcr9JUj7wDrgVBO0zLhwxG3SefS2cd3VH4_x72VOF33-Pm6RE4ltmfeoJG4ng6T-13seKhw5YZcIWXQV820wiFUTeN8L5AQt1pbuR1SjBsFSVILL0xrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72816" target="_blank">📅 11:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72815">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c201257b1.mp4?token=vxat3Kkpkuz1NyP7DPTSpITztATGcB6nOMBDu5lDDAX5tMgQlgRbgnruggFzxYFfI1gxKGsvvrttbZPEs60PR4RVMP2TFkBWIf1IIUtSXVdF20A-rUmuKa_MFdUtd8bs9P5U6xxeYBPkyd2xGFDL-WEcuoCJBwpFdipjC7-slUs548c2EYeZ-CVvLkDDgf8Ly0XQHpwrpnIylNVyvO2H9ywzXP1eDB9wXLu80hsvzKWejouLOh-V0BWCvgrkgYGsa_QkNO_VdcIUqZJk3se2ywMDcSyN6PIOvUF34X2UIgBCR4CH9wIRe2cA9QmDjqTICOpbHc9wkzijeS9eGJrl4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c201257b1.mp4?token=vxat3Kkpkuz1NyP7DPTSpITztATGcB6nOMBDu5lDDAX5tMgQlgRbgnruggFzxYFfI1gxKGsvvrttbZPEs60PR4RVMP2TFkBWIf1IIUtSXVdF20A-rUmuKa_MFdUtd8bs9P5U6xxeYBPkyd2xGFDL-WEcuoCJBwpFdipjC7-slUs548c2EYeZ-CVvLkDDgf8Ly0XQHpwrpnIylNVyvO2H9ywzXP1eDB9wXLu80hsvzKWejouLOh-V0BWCvgrkgYGsa_QkNO_VdcIUqZJk3se2ywMDcSyN6PIOvUF34X2UIgBCR4CH9wIRe2cA9QmDjqTICOpbHc9wkzijeS9eGJrl4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوستاد خوش چشم: اگر آمریکا بمب اتم بزند، ما هم پدر بمب‌ها را به آمریکا می‌زنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72815" target="_blank">📅 11:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72814">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/796b47b54e.mp4?token=Gaw66hUlMRHTvVdJPbtWRoDlnQhcwpY7s9JfN6KdTGtNUumPZ6F_PD12CyJBElmuTiQmnrYo2E5RhUixN26B-I0YYbE2QukKdHBHeVhStTMMTPPzWjbCy4nqU91zl0uxcKg9kUbLOdNugXkiZSYtfDEXqHvX324OdekePRdE3scOGVMUliyAY6teGfZ0vRnE7DvkPnGaEeeZaqjsjiyfDsiJEAzGTadm1ySmz9N0qctuSHnY8fS1dK22ZKrb--eVOc3D2M_3TqNxbmiBX35zoGD9nVwd1WX4LQ-FlgQQaPpbLNtd7KcLkIxHIBia0aNw4XAjbYYjhzsr0iZD02o5xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/796b47b54e.mp4?token=Gaw66hUlMRHTvVdJPbtWRoDlnQhcwpY7s9JfN6KdTGtNUumPZ6F_PD12CyJBElmuTiQmnrYo2E5RhUixN26B-I0YYbE2QukKdHBHeVhStTMMTPPzWjbCy4nqU91zl0uxcKg9kUbLOdNugXkiZSYtfDEXqHvX324OdekePRdE3scOGVMUliyAY6teGfZ0vRnE7DvkPnGaEeeZaqjsjiyfDsiJEAzGTadm1ySmz9N0qctuSHnY8fS1dK22ZKrb--eVOc3D2M_3TqNxbmiBX35zoGD9nVwd1WX4LQ-FlgQQaPpbLNtd7KcLkIxHIBia0aNw4XAjbYYjhzsr0iZD02o5xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران هر روز ترسناک‌تر میشه، یه پدر برای اینکه پسر 3 ساله‌اش رو تنبیه کنه، یه بسته مداد رنگی 24 تایی رو فرو کرده توی باسنش!
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72814" target="_blank">📅 10:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72813">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0246c863e9.mp4?token=YM50DU7-KlWg6Q2vo1QZsCFxzYeBp1GW92IHuiINUc-07Ncb1hjyNAIfJLjlCCgIcgAY2o0pAzBlQ2qQ5QG18Q62Yd5Jd-6enLp-NDp5NcVIgKKnExG8Hgm4WpIL7pQ1xWWpv1SvimrV30pq1TA1bS-179QzaJVsRlRxipgaIhyQmxUB8S7GXsK8yV1Ix9e6HdSiUzD1Utj1PPxU3WTSuWer29vCMG8ga80mGKSqpZpZFdMuH2Hmu9Kh2fitv7rCTWO2dkS9eZ_VvfwdOTuUzTuVB_n7dFxBi7kAQ_dEUc3a7CjFgYurCEirdrJhCJBKY2DT2rx4azB9KKgr-kEZhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0246c863e9.mp4?token=YM50DU7-KlWg6Q2vo1QZsCFxzYeBp1GW92IHuiINUc-07Ncb1hjyNAIfJLjlCCgIcgAY2o0pAzBlQ2qQ5QG18Q62Yd5Jd-6enLp-NDp5NcVIgKKnExG8Hgm4WpIL7pQ1xWWpv1SvimrV30pq1TA1bS-179QzaJVsRlRxipgaIhyQmxUB8S7GXsK8yV1Ix9e6HdSiUzD1Utj1PPxU3WTSuWer29vCMG8ga80mGKSqpZpZFdMuH2Hmu9Kh2fitv7rCTWO2dkS9eZ_VvfwdOTuUzTuVB_n7dFxBi7kAQ_dEUc3a7CjFgYurCEirdrJhCJBKY2DT2rx4azB9KKgr-kEZhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو تا از لوکس ترین مدارس بالا شهر تهران که شهریه شون یک میلیارد تومنه!
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72813" target="_blank">📅 10:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72812">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84c2a17b7a.mp4?token=chbMkY507FWQsZUGCorupsIfv8KYDQusyQxPdsP57XtBHp2i7u4nKmkg9ldyhWyV3UN1uLZuOBAbJZfcoXAF0mnG2fcw4LzTbAeeQD9WUIGLq2kRfXeqfOWcfYA7Wpz3Z0x-6YrHXQ4UgDGU7ptwrZNGhnxtTEwlffOjQZboM-oqblRIBYi0paPJYqZhGPEQVMrJyuV2rqZsnwU72y3MutzwwuAh1qwY1jJSJ2yiL-zZwXfMjCYWfqgO1etuH5PrThb9fN1sbHsaBiTs5e0qirfBAOrDvg0j9egEUkxXUvZtFCv0GXoW1pWQkcuX5aHzTzRx7c37B9ODbIsqZzXJOGyMQ1VY-7Xk95xSkjQXEGC1g3loZPDV9cEym5DCgkmXw4rR-cDuoBTgndgFw2PpgH5gACUENW82FgejC7BQyMVoG7r1MIZdH5USzoNDVELLmE3jkBm2IpP1StXfMGqEwlLvgpA2NIdu2aqMXdE8czlfalEM8HCQSiS4KTM0sgClNAGEM0-Vz0NNI7NQ2tk7FrruCRhqPtgSyuL0z6Q5YAaVM9UjwAZ8FIIdsOnjoV-u8zD5iL139QXvJ9RTKstUY6uq1l8bT4QJZJm6jnvP1buryHaQqk-XgDzV84Lm4HdN8LiLmkeQG-ziylOHvkwz3CjLGen4K8MVZAtlVPVrgKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84c2a17b7a.mp4?token=chbMkY507FWQsZUGCorupsIfv8KYDQusyQxPdsP57XtBHp2i7u4nKmkg9ldyhWyV3UN1uLZuOBAbJZfcoXAF0mnG2fcw4LzTbAeeQD9WUIGLq2kRfXeqfOWcfYA7Wpz3Z0x-6YrHXQ4UgDGU7ptwrZNGhnxtTEwlffOjQZboM-oqblRIBYi0paPJYqZhGPEQVMrJyuV2rqZsnwU72y3MutzwwuAh1qwY1jJSJ2yiL-zZwXfMjCYWfqgO1etuH5PrThb9fN1sbHsaBiTs5e0qirfBAOrDvg0j9egEUkxXUvZtFCv0GXoW1pWQkcuX5aHzTzRx7c37B9ODbIsqZzXJOGyMQ1VY-7Xk95xSkjQXEGC1g3loZPDV9cEym5DCgkmXw4rR-cDuoBTgndgFw2PpgH5gACUENW82FgejC7BQyMVoG7r1MIZdH5USzoNDVELLmE3jkBm2IpP1StXfMGqEwlLvgpA2NIdu2aqMXdE8czlfalEM8HCQSiS4KTM0sgClNAGEM0-Vz0NNI7NQ2tk7FrruCRhqPtgSyuL0z6Q5YAaVM9UjwAZ8FIIdsOnjoV-u8zD5iL139QXvJ9RTKstUY6uq1l8bT4QJZJm6jnvP1buryHaQqk-XgDzV84Lm4HdN8LiLmkeQG-ziylOHvkwz3CjLGen4K8MVZAtlVPVrgKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: خبر داری دلار شده ۲۷٠ تومن؟
یه خانم تو تجمعات: اره ولی ما بخاطر وطنمون اومدیم، اگه ما نبودیم دلار حتی گرون ترم میشد
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72812" target="_blank">📅 09:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72811">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4d885120.mp4?token=VHPKRE3As0YnRAgWl61aeBLWd8xR8RIbmtGvofqAXIOzLhlGYChd1lYpZUIs3kX3Z41CWE0mhWV5aoz2L2GVCGUHCsq0WhR90RVduwUIO2_7IL_uE4wRdg9ygN1xrx0GatmaiKAtMFO1ZdfrpRRgrxxhhOydwrIdP2bURZyt3xKZ_O25RRTsyOMcq-OkaanrcObu0bPdluqavYn0oTkigwGj8Cu9a3YIct74aAYSWEH4irEKzcD9FG3U8Sa-_m_34txmEstAFeddj8csG_1shwfjDWdA0fko3qyr2F3Wv_zgi_jlo3QlZ4bwl7Uy9srPzBAIKPz6ybQUlHEACzuuIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4d885120.mp4?token=VHPKRE3As0YnRAgWl61aeBLWd8xR8RIbmtGvofqAXIOzLhlGYChd1lYpZUIs3kX3Z41CWE0mhWV5aoz2L2GVCGUHCsq0WhR90RVduwUIO2_7IL_uE4wRdg9ygN1xrx0GatmaiKAtMFO1ZdfrpRRgrxxhhOydwrIdP2bURZyt3xKZ_O25RRTsyOMcq-OkaanrcObu0bPdluqavYn0oTkigwGj8Cu9a3YIct74aAYSWEH4irEKzcD9FG3U8Sa-_m_34txmEstAFeddj8csG_1shwfjDWdA0fko3qyr2F3Wv_zgi_jlo3QlZ4bwl7Uy9srPzBAIKPz6ybQUlHEACzuuIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آجرلو عضو تیم مذاکره‌کننده:
بابا بالاخره یه جایی باید قبول کنیم یه‌سری از این تحلیل‌ها اشتباه از آب دراومده!
هرکی نظر متفاوتی داشت رو «خائن» و «وا داده» خطاب نکنید؛ وقتی می‌گفتید ادامه جنگ این‌طور میشه، اسنپ‌بک هیچ اثر اقتصادی نداره، نفت میره روی ۱۵۰ دلار یا با شکست ترامپ در انتخابات کنگره همه‌چیز تغییر می‌کنه، باید امروز جواب همون تحلیل‌ها رو بدید.
اینکه بگیم «ترامپ انتخابات کنگره رو ببازه، دموکرات‌ها جلوشو می‌گیرن» هم خیلی ساده‌انگارانه‌ست.
بین انتخابات تا شروع کنگره جدید چند ماه فاصله هست و رئیس‌جمهور آمریکا هم قدرت زیادی داره و می‌تونه سیاست‌هاشو دنبال کنه.
خلاصه اینکه تحلیل غلط، تحلیل غلطه؛ فرقی هم نمی‌کنه از طرف چه کسی گفته شده باشه. به‌جای توجیه و فحش دادن به بقیه، بهتره بعضی‌ها یک‌بار هم بابت پیش‌بینی‌های اشتباهشون پاسخگو باشن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72811" target="_blank">📅 09:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72810">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72810" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72810" target="_blank">📅 01:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72809">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIk7IYVxTyJXSSdB1EHecZbXVSt5NcL6YuxTbpy7RPzCGEnhqZnyBfDDpXDsFB7jJmnlJVQdbAl9XjFJbTfJB8S0vUMue7Q9njsTd-2OdwyFfp_yOIRESkjgvaMjcbBmUJSdoX0uLgXKULngmTyP2D7_KB_OQWqmUHADZ7qYjoCnpZWVIX0odeW-uKTKmzTcF8TB_JPIOkX2s2i3zEFhrXO3psKIIkCOF-xDhIQpt0rOVU1JV-YfijthHyHhNOlWrgmgcJXlHfyYAO3RSdgEEoNwIWn0l748czOFTbLh8UuzFonfeSYF2SerzkSdC0a7M5MkgjJkp7ZMjovkgSvQpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72809" target="_blank">📅 01:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72808">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9d28d251d.mp4?token=psG4IOp2mWpZqCZSLL9FGhufO-mOsFTZ5gC7gjN4VIGXus9bvFrcVPZINn7QCc41kVQBdoPW7dLpluVCKpeuqa-lbWtreuk4tVmFDZfCHg47NKO0m2fwIA_WRLoygFePrD9OOlLqyUOtdiyp-cpvFShYySVm6VvZHP_qmOfG3dKa7bFz-JvP6lfYiFb44SOaoc609YdM4relUJrVbJqY_iJsTaZbJpwcu2Hf3J8hZYlf_XWNrk7L3e2mdVzOzcNEUo6VsH34bAh93bspQqCFpb_BrSf0_M6uH9eKY9osx0lENlttYP0s4sWNJmyFcas9iCuvTZFhvwKt5pnLdQTDUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9d28d251d.mp4?token=psG4IOp2mWpZqCZSLL9FGhufO-mOsFTZ5gC7gjN4VIGXus9bvFrcVPZINn7QCc41kVQBdoPW7dLpluVCKpeuqa-lbWtreuk4tVmFDZfCHg47NKO0m2fwIA_WRLoygFePrD9OOlLqyUOtdiyp-cpvFShYySVm6VvZHP_qmOfG3dKa7bFz-JvP6lfYiFb44SOaoc609YdM4relUJrVbJqY_iJsTaZbJpwcu2Hf3J8hZYlf_XWNrk7L3e2mdVzOzcNEUo6VsH34bAh93bspQqCFpb_BrSf0_M6uH9eKY9osx0lENlttYP0s4sWNJmyFcas9iCuvTZFhvwKt5pnLdQTDUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین ویدئوها از شهر طاعون زده شلخوف در روسیه:
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72808" target="_blank">📅 01:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72807">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a90e5ff82.mp4?token=KQSTKNUYTwwiCPPDwtKUtUfm7Eb0i74_dUwVuntNkjiaAVpYE5zipYylzLP1f2CuGfiX_5S21y8dLGZyN885Wz8FQI3uyU2oGKl2kO03Eq3LSIFxq4lQV2CERmnBHDBzUm0pWTtTpO93D7yC0YrutJbKiX8492es2PNEqrs6PyDdEPXdRwIp3m7lwLIPzfUJ3onV9PGlo1s3Kg4KT17n2yFhtplS1sSfYImD2xjD24kg0QogypT7o6zftVQFRNm1LgePUcWKodVO5uPfptQj4yObHfHI1PC3M3lj39dEIAdSP96C769jJX-0VOfhOQHOzmYm7m2jlj67JLbbvSuRtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a90e5ff82.mp4?token=KQSTKNUYTwwiCPPDwtKUtUfm7Eb0i74_dUwVuntNkjiaAVpYE5zipYylzLP1f2CuGfiX_5S21y8dLGZyN885Wz8FQI3uyU2oGKl2kO03Eq3LSIFxq4lQV2CERmnBHDBzUm0pWTtTpO93D7yC0YrutJbKiX8492es2PNEqrs6PyDdEPXdRwIp3m7lwLIPzfUJ3onV9PGlo1s3Kg4KT17n2yFhtplS1sSfYImD2xjD24kg0QogypT7o6zftVQFRNm1LgePUcWKodVO5uPfptQj4yObHfHI1PC3M3lj39dEIAdSP96C769jJX-0VOfhOQHOzmYm7m2jlj67JLbbvSuRtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو پشم ریزونی که ارتش یمن منتشر کرده که دارن با ماشین، حوثی‌هایی رو که در کنار ساحل گرفتار شدن و در حال مقاومتن رو زیر میگیرن و له میکنن:
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72807" target="_blank">📅 01:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72806">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e493def7.mp4?token=A2RuJMpyXKUYXucDqc_znhniIYU3qwACiQyWyccXHMLzEGv_ZwUSSlVoywxDTnaqOAoWhbapQ877eWkr79wRRxcuHkD5QJZw7qDLLHW_PniGjvAtaZg3Y3k2mP5e4PcHmWAub3xj9B6Sv4ROcCFOBmvOvcxKUkciBC5k388YOkpNvHrAsCrUIMLsfKkiWylerQyTS-HhfXIU0L49TzvVpuYs1hi9srG1YbBIT-6CGAqnGv65cj4aduPNYpPG3pFBOzV1LtZeXlz2VHuhfVom_PNgqxss6e9zZIiQkc6x4iB95wRTOLyIl3_rhwRelPrj3NHTOqY6GNJUp-ZewP23zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e493def7.mp4?token=A2RuJMpyXKUYXucDqc_znhniIYU3qwACiQyWyccXHMLzEGv_ZwUSSlVoywxDTnaqOAoWhbapQ877eWkr79wRRxcuHkD5QJZw7qDLLHW_PniGjvAtaZg3Y3k2mP5e4PcHmWAub3xj9B6Sv4ROcCFOBmvOvcxKUkciBC5k388YOkpNvHrAsCrUIMLsfKkiWylerQyTS-HhfXIU0L49TzvVpuYs1hi9srG1YbBIT-6CGAqnGv65cj4aduPNYpPG3pFBOzV1LtZeXlz2VHuhfVom_PNgqxss6e9zZIiQkc6x4iB95wRTOLyIl3_rhwRelPrj3NHTOqY6GNJUp-ZewP23zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان سخنرانی حسین رحیمی، رییس پلیس امنیت اقتصادی، درباره افزایش قیمت دلار، برق محل برگزاری سخنرانی قطع شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72806" target="_blank">📅 01:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72805">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVu5uuchekYIgrtpjwyVBzUBZvdFCsnhNQTE_0BSiiFGHJ78RJ1fvEh7NNcMzhLhGUANkN5TPytBh4c4IY_i_gUuvDKH6D1REmTaKybziQ8XOel9A3gxFoXhm99lDHuyPI50c7u7KQQkeXYeKtrP8rmsZ8lZw0eoIiwtRqNEGnX3SJz0E_YNPZjmItSijjFosB7A3KadZ4i4g5psnpxRsQar1GARf0b0epmVk85kZy4XPQ3YhRN3sqAPTylyUV7erRcWUQd9g9qIF5w6PWZgPddoiMc9Sy4tV04ZmLa3NcpnoIE4RhYpKveJgaYHbR45i39_IMdx9BJ4rCnRyP827w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت درباره ایران:
«عملیات طرد اقتصادی» نتیجه داده؛ ارزش ریال به پایین‌ترین سطح تاریخی رسیده، ایران ماه گذشته هیچ نفت خامی برای بارگیری روی نفتکش‌ها نداشته و حتی یکی از مقام‌های ارشد امنیتی ایران هم گفته کشور در یکی از سخت‌ترین دوره‌های تاریخش قرار گرفته.
حکومت ایران در حالی مردم خودش را تحت فشار و رنج قرار می‌دهد که منابعش را صرف حمایت از تروریسم می‌کند و عملیات طرد اقتصادی تا زمانی که جمهوری اسلامی از تأمین مالی تروریسم و ساخت سلاح هسته‌ای دست نکشد، متوقف نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72805" target="_blank">📅 00:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72804">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b15ea218.mp4?token=akzJ6L7pgFem9_83-S4t90c9s1pHt75zJ5ZQN2nwvP5ZdV5A2I4Wm75hUcMS_4ws7W4ZFe43828nWjVjq3JBcmB8FRYFo2-o1gY6vuP6-LhJ1rrvVI1VcxAoYo4LuYm4pMZMAt7ONMdy9fPWlc7MrWiaLjXLzThN9YbRpn2_sVq0QMv1boAXoY422Pg3KDcxADqiSPJmLp6Whac2GTCK-XbTcVAS8n9eJW308UfEzevcnkwbh58BeyNrjYQcTnFz4aJ1nUKkP2etyk3NRASGrLTn2Pwd26l2DE58R8paIzrLGTJGCEqiRG5XtTjrPTddrX4VYNFlmnlfQrdVGMQbag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b15ea218.mp4?token=akzJ6L7pgFem9_83-S4t90c9s1pHt75zJ5ZQN2nwvP5ZdV5A2I4Wm75hUcMS_4ws7W4ZFe43828nWjVjq3JBcmB8FRYFo2-o1gY6vuP6-LhJ1rrvVI1VcxAoYo4LuYm4pMZMAt7ONMdy9fPWlc7MrWiaLjXLzThN9YbRpn2_sVq0QMv1boAXoY422Pg3KDcxADqiSPJmLp6Whac2GTCK-XbTcVAS8n9eJW308UfEzevcnkwbh58BeyNrjYQcTnFz4aJ1nUKkP2etyk3NRASGrLTn2Pwd26l2DE58R8paIzrLGTJGCEqiRG5XtTjrPTddrX4VYNFlmnlfQrdVGMQbag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ترامپ:من فکر میکنم ایران مسئول حمله به هواپیمای «فلای دبی»است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72804" target="_blank">📅 23:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72803">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ:
ما مقادیر بی‌سابقه‌ای نفت از تنگه هرمز خارج می‌کنیم. یکی از مشکلاتی که داریم این است که پالایشگاه‌های روسیه به‌شدت هدف حمله قرار می‌گیرند.
این یک مشکل است، اما اوضاع به‌خوبی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72803" target="_blank">📅 23:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72802">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سؤال: آیا نگران شیوع طاعون در روسیه هستید؟
ترامپ: این بیماری‌ای است که قبلاً قادر به مهار آن بودیم؛ اما به نحوی، آن میکروب‌ها قوی‌تر و هوشمندتر شده‌اند. آن‌ها مثل یک ارتش هستند. ما به روسیه کمک خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72802" target="_blank">📅 23:37 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72801">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c9bba814.mp4?token=PhdFcj6zOg2GwXReCLTFr6R_PZrBeoPTdryu5Lx50tzrTyjNTyqzv6WglzDff94xk_EtXtpW7N8QRcHTCUSt7hBRA2jpiFNYqhs09FG9yQl7OUvsr2nbHSy56BPu67hI_zYZaW5m9r3ZcV_plb-o4UlQHh5WvZ633sg0Ks54NPxUgQca662iNAXVS3gon_c-o0DC0qA6VqMcPUwKzkQ2l0ObPBQWAkqmYcDWy-IQ3Zqm_-TayPQIlVK-NFpDbGBk3sg7eXx6BibZ-qH7GL4aYHXhur1JLGhaVmMrdWRZy5x_zvah9BJdIsfoCNf9801jkR0jvrbLWlCLNuiss9V8SlzGthofHp97-F3rGfKqMO9uPnSMoOAv1IQk-nf4QGAlEb21JOO62eqhRjNQdajdjoe2G45N5tSXeT7K2Z1wHp-1NLaCSVJVkvLz6_MegPz1ZJn9035m-bgBFkX8RLH_e2Vtvfqp2AfoyDUbD3AmEdVz9Kw4DxjrnClVOOO7dLWDZzImFeTzwEnk0kX-zSCfcaj1NWF0W5GyFGJU3oalQlipcsyjvQhdrjE60XjTsJP5WBZ9s3ELhWzbYfQ05Ih5jwIZNoeDD9_9_nalfxkaPwcu3Zwek5ZpzbMqVAJpO2ZxFLfEvWm7pIy3A2lmCXD-85SxduED_Lel7iIZ-y2c_M4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c9bba814.mp4?token=PhdFcj6zOg2GwXReCLTFr6R_PZrBeoPTdryu5Lx50tzrTyjNTyqzv6WglzDff94xk_EtXtpW7N8QRcHTCUSt7hBRA2jpiFNYqhs09FG9yQl7OUvsr2nbHSy56BPu67hI_zYZaW5m9r3ZcV_plb-o4UlQHh5WvZ633sg0Ks54NPxUgQca662iNAXVS3gon_c-o0DC0qA6VqMcPUwKzkQ2l0ObPBQWAkqmYcDWy-IQ3Zqm_-TayPQIlVK-NFpDbGBk3sg7eXx6BibZ-qH7GL4aYHXhur1JLGhaVmMrdWRZy5x_zvah9BJdIsfoCNf9801jkR0jvrbLWlCLNuiss9V8SlzGthofHp97-F3rGfKqMO9uPnSMoOAv1IQk-nf4QGAlEb21JOO62eqhRjNQdajdjoe2G45N5tSXeT7K2Z1wHp-1NLaCSVJVkvLz6_MegPz1ZJn9035m-bgBFkX8RLH_e2Vtvfqp2AfoyDUbD3AmEdVz9Kw4DxjrnClVOOO7dLWDZzImFeTzwEnk0kX-zSCfcaj1NWF0W5GyFGJU3oalQlipcsyjvQhdrjE60XjTsJP5WBZ9s3ELhWzbYfQ05Ih5jwIZNoeDD9_9_nalfxkaPwcu3Zwek5ZpzbMqVAJpO2ZxFLfEvWm7pIy3A2lmCXD-85SxduED_Lel7iIZ-y2c_M4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: آن چه تهدیدی بود که باعث شد آن هواپیماها را از بریتانیا خارج کنید؟
ترامپ: احتمال وجود تهدیدی را می‌دادیم؛ خب چرا باید آن‌ها را آنجا نگه می‌داشتم؟ با تهدیدی مواجه بودیم. ما کسانی را که آن تهدید را مطرح کردند، می‌شناسیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72801" target="_blank">📅 23:36 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72800">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f6705b0f.mp4?token=FSnOzS-KXGgl-Jzfp2OI14E98WUyJClk-jOYKcg8s1QMl9xgNJWYq0gkXyGC1JikL_RmJ31E21-p1uP41yXQX7LyImFCh44wrNBAV5e0x4f0WI2hOJgV7ClWJMIxsLqNZ-Tlj2a96zAp9ZK2964nY2vqsMHit8G_mFKXosOfzXodPFOouq-Ym80OqgdsBztI5G84d2Q2zD1-KHwgTU7zjae56Gu0-IfrBGBTe-xvw5uYr0NG5NL5dOMmQe9Z0qbxZqPH0lGABx4OvzfllwQvSJyFaYj-I-HFpuqgLJQ-SgOUwCGS8et5Y2TZRufCGB732vhIFsJmymw8lpLEFx2LVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f6705b0f.mp4?token=FSnOzS-KXGgl-Jzfp2OI14E98WUyJClk-jOYKcg8s1QMl9xgNJWYq0gkXyGC1JikL_RmJ31E21-p1uP41yXQX7LyImFCh44wrNBAV5e0x4f0WI2hOJgV7ClWJMIxsLqNZ-Tlj2a96zAp9ZK2964nY2vqsMHit8G_mFKXosOfzXodPFOouq-Ym80OqgdsBztI5G84d2Q2zD1-KHwgTU7zjae56Gu0-IfrBGBTe-xvw5uYr0NG5NL5dOMmQe9Z0qbxZqPH0lGABx4OvzfllwQvSJyFaYj-I-HFpuqgLJQ-SgOUwCGS8et5Y2TZRufCGB732vhIFsJmymw8lpLEFx2LVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: آیا فکر می‌کنید این خطر وجود دارد که ایران پهپادهای رزمی وارد بریتانیا کرده باشد؟
ترامپ: نمی‌توانم چنین چیزی به شما بگویم. اگر دست به چنین کاری زده باشند، بهای سنگینی خواهند پرداخت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72800" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72799">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a5b0254b5.mp4?token=Og9s9dyrqny2C_z4DQ-UExVgA7CpoqjTnxtPggdwV4yIFhC_zBgUWs5zwGRszsswrPJlMVnnATLnbxwxqeUU59zzb1iTi3G7yDCl5RUAi9LFJ3BKTPyxb0qoemBepX-FH4WJg2dIhMs6N6rGMebYRwRcTeiU3mZhDLtzo64b4BR3lGzbVODmMHA6g7e3yzAlN3BB7GcIzNF5mevSbCmcvNSgJ7dN-Ww0S5gfGYXKIWbLRVwaSBwlpg6oF9HAssS-So6zkhRFNRvxaFvkeFC9IUhkEARkg24Lbu9EWMP1ava4c9M7A679y9wifJ0vea_oAFyUiuOqjDfgwd_4BR5QuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a5b0254b5.mp4?token=Og9s9dyrqny2C_z4DQ-UExVgA7CpoqjTnxtPggdwV4yIFhC_zBgUWs5zwGRszsswrPJlMVnnATLnbxwxqeUU59zzb1iTi3G7yDCl5RUAi9LFJ3BKTPyxb0qoemBepX-FH4WJg2dIhMs6N6rGMebYRwRcTeiU3mZhDLtzo64b4BR3lGzbVODmMHA6g7e3yzAlN3BB7GcIzNF5mevSbCmcvNSgJ7dN-Ww0S5gfGYXKIWbLRVwaSBwlpg6oF9HAssS-So6zkhRFNRvxaFvkeFC9IUhkEARkg24Lbu9EWMP1ava4c9M7A679y9wifJ0vea_oAFyUiuOqjDfgwd_4BR5QuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوال:نظر شما درباره ضدحمله عربستان و یمن علیه حوثی‌ها چیست؟
ترامپ: همه چیز به خوبی پیش خواهد رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72799" target="_blank">📅 23:33 · 13 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
