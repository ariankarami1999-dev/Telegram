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
<img src="https://cdn5.telesco.pe/file/PWwb8sLpbgY0ZCNmZQLYm9Zam3CDDTGTgSh341yY00As8IFeXc6Yz9kjw5PFeDoH0cPDDlDtyh0ATYIOUffxHGM8t1B_6FtOKz1dyC7PT8JRLj6euAFG1xQVFpkM30LbnEdVI7VljHokLPFTyhQWMsZzL4z--roudc2rmR1jTVvzaJKc6HjbX_d3ePqCWvp36MaaCOmpBlk4qXzWXZhurtzXp_nfiP9xXfgSIF38tHfxV_jESyY-3PuSEPayEwAcTupwZBiw6z4rPuaH0qkwe9cM8SkxwXr2khVWdUNDBc0vnvP0shln7v-omG2DzjFs89dUres9r3_EiCpxqx7CMA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 538K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 18:09:18</div>
<hr>

<div class="tg-post" id="msg-101672">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EB70JOf1odqxzkYOu6FDTPTFHJbWe8mDCQ6pJkRrH6qdMKjF3vFJgzW14N8kMeIZpFw5YIWb8V3twGlrP2Kpg3xreOSqfP2CPECot1HelVNvWGiPb7dZ11VkYgcX3zOlcUTZ5GhXOzmi7w7ClOOADFwVsQXabcK_tMCropmI4pcvDgqZHy9EU4Lf0280AOuL87kjMx-UFj92i9y1RZPeCJNsMCXZ4rh4pTFP3XPUBX83DnsEBZPYv9kBwQVKWEOCKXd1V9uA2nIXqwsmdO2KlZhgPa5YaEgMEP6VNyEqS-PmpPg-2VSCjCvkw31hAjWGiFgapHoPaGpBunSe0r4P7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_فوتبال‌180
؛ باشگاه نساجی مازندران با ارائه پیشنهادی خواستار جذب محمد خلیفه به صورت قرضی به مدت نیم فصل از استقلال شد. این درخواست از سوی مجتبی‌حسینی به شهاب‌زندی مدیرعامل این تیم منتقل شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/Futball180TV/101672" target="_blank">📅 18:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101671">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815514f088.mp4?token=VXxUUX_kinZ2wdmNjcN694nTBiyonrspYBbogDFIjW-ShBZ9QzHM1q33nrak90xuLBxg39xiOY8wL39b4Vtx7wAO1R3jT6ye6KJ3zzgewmIok6KYWR-q_x6vRzGE4_m1g20SQn-ZSDhxhewkr-VtPBKFIZyVU9hbp8KIWIpZgQgl_0v_q3uV8liaiuiwckcKS3Sw3w0tJeH5YYYVp5HnYLwEgskwMj6qc0DJeAZ_QX_ljgZ1zCOAKbdv8T04A74X6NIMuAmhVg2nnETLhdj9vLjkuwdwtVRgn7ahtOZvIEr_YkdJELuhGT_ZQMoK8UXNuZIHjnHmPrtvPbM2kAcKIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815514f088.mp4?token=VXxUUX_kinZ2wdmNjcN694nTBiyonrspYBbogDFIjW-ShBZ9QzHM1q33nrak90xuLBxg39xiOY8wL39b4Vtx7wAO1R3jT6ye6KJ3zzgewmIok6KYWR-q_x6vRzGE4_m1g20SQn-ZSDhxhewkr-VtPBKFIZyVU9hbp8KIWIpZgQgl_0v_q3uV8liaiuiwckcKS3Sw3w0tJeH5YYYVp5HnYLwEgskwMj6qc0DJeAZ_QX_ljgZ1zCOAKbdv8T04A74X6NIMuAmhVg2nnETLhdj9vLjkuwdwtVRgn7ahtOZvIEr_YkdJELuhGT_ZQMoK8UXNuZIHjnHmPrtvPbM2kAcKIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
مارک کوکوریا موهای بلندش را فقط به خاطر استایلش نگه نداشته است. پسر بزرگ او، «ماتئو»، مبتلا به اوتیسم است و در تشخیص چهره‌ها مشکل دارد. کوکوریا می‌گوید موهای بلندش کمک میکند پسرش هنگام تماشای مسابقه بتواند او را راحت‌تر بین ۲۲ بازیکن پیدا کند. به همین دلیل هم قصد ندارد موهایش را کوتاه کند؛ چون برای پسرش فقط یک مدل مو نیست، بلکه نشانه‌ای است که باعث می‌شود پدرش را گم نکند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/Futball180TV/101671" target="_blank">📅 18:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101668">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ST6eo3B34Xj0ZeqX6Z3tSRbqDchYBiINa-qHASR8aMpOltYsx-9OKR0nD0i2kvw8xmvieaOKmTLXwrfefmHgpdP85m5nFQE8VMeIQgXS1lZuVGbkCTBwSAS64Dgl0YQpVAfWoqN0eEA9xkdhO8B3G80dHz8BD5uVF6mp42QRRs3K_P7UvNVgqzeFaKr140cJI1lJBIg6CKs2Ul-_tYiteRUJ58QKcCsdo-Cdl8lcPS_ApmUJB_bex7T9F1Yrgxd29qYJ217O8hwzUd8O1CfoIoJQ4fDfmwm2EmDCHIad0GVJbf4so-1h4XUmXvEFWKuFFcJVcVSx27Gv1HMN7CA1Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g1vkkjs21BmP7MfMcuyhV9smh1ODH-wqkd1bziKOL0-Pp5ZP6xSvKdRdsc9Qcanv0joIyy3EIN8GYdaBLxhKKrJIaIcgRGQeAK1vHUPDuAiWfCbekfu08ZaHyy01sBs9DkCA-olyU9ymp_zo9nU2RvbvH-Q6sFbuDUsF7Op2xAbycf_NPvHLRi3I3yIUUT29ebq7b8bZLNczV2WAoYXlZXhX7VqmKttJJZVLnVOJvmUqcvqP_k5LOlQk4HeCJRTZo9s6cv41h2k7G1VajipBagkFPM_10SHzind16vwJOBLmeKA6aXm-ppG4g2vQdDNPYlrkWNAc9C7gnntr5uu4Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BRrsPW05O3pwcUa82LJIda_m4qdtmLo4Y-wSmfelMnxaMHDajlA35i_8drW5F5zE7LaBDUWtSMiirTHq0xyiJZ5T1Q31gvEs3m10CUE0ioEF1N977Or1FwqmCUO8hykF3vNr8tAfR0dBN6uxKhkke2PetmyziMefOLqW7RIKMPCtGipe6a-1zGfjtpyWbGZr86veFxRcTzhuyEQaeRzW3DEWXgKot2654zUED9KK2OAwPEyPz2XW0KzMeq1jSJEckzXus65btVowV2T-TQXHZUuQFpjWOO8H7hALMtBTne-iVI6tHe4Y9FnZDSUWc3Ms0_GVZbdyVPIOugKivXij7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
رونمایی الهلال عربستان از کیت‌دوم فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/101668" target="_blank">📅 18:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101667">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGaeFby7uG2mrVSxh2Vi9NGZf5NOb_CHsP23AMWJqsFpp0Bl6EAVKm1OXp9lnchcuLvm8-HQ33PZLS7Z832YC0liB8JYC3_dq2E2qLozbsSSAjmVhTue4zcsbRbynPsjjG4Wqel4CBxdDzt0gEXNddKSGbe-poL07Uw4d1YtBDdKCqUWoKBm5lh21KMv4r2sqwUfbNXQvUkuoAohf3VQ1_MYz66HfEbbhH09940tJMtoKKRx72sYuV-YL2e3qS94adKcYgdYKmB-NheoNwXG3Bzw_PWWY78O0iuK2fAQiJvUUwMiY1RRV5NJH24ftVFnCIWzL58eKJEzm7Bhk6S4yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
جلد نهایی بازی FC27
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/Futball180TV/101667" target="_blank">📅 18:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101666">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7937bcbd97.mp4?token=h31z2uhBPigjGoLQYEi9zAnAItFRDVlvPc03CsZlBM_Ux5MnRV0yBxYg7IfWnpTpTUGK2xUZl1tmjdrQsytYfkLfaX6U-BR0c_M_q4yo5Ye1zBs84yi5YwldDYtttpP2l5SiaMdALCQlwOjUMqXzRMiQ7SRrXcH_ZSs8l5CymW_Gw4xi2cnk_hzEVcK4XEGHL19Z3FJLeRznfA5jJaDg3l2JlDME2Q0bFIzT7j-6eJP_8qiJVHUX8Hbc8zW4X-ziI0tZFqOxbl9yJwUry0xsCPI8EwWJ56d2Tua_Xc19epYnqd1MjKZvj8oUJ2cJv7uKriY2Wo2NJVqzoRxNyGx4ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7937bcbd97.mp4?token=h31z2uhBPigjGoLQYEi9zAnAItFRDVlvPc03CsZlBM_Ux5MnRV0yBxYg7IfWnpTpTUGK2xUZl1tmjdrQsytYfkLfaX6U-BR0c_M_q4yo5Ye1zBs84yi5YwldDYtttpP2l5SiaMdALCQlwOjUMqXzRMiQ7SRrXcH_ZSs8l5CymW_Gw4xi2cnk_hzEVcK4XEGHL19Z3FJLeRznfA5jJaDg3l2JlDME2Q0bFIzT7j-6eJP_8qiJVHUX8Hbc8zW4X-ziI0tZFqOxbl9yJwUry0xsCPI8EwWJ56d2Tua_Xc19epYnqd1MjKZvj8oUJ2cJv7uKriY2Wo2NJVqzoRxNyGx4ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔵
خاطره قایدی از اولین بازی در استقلال: جمله‌ای که بعد چند سال هنوز از ذهن قایدی پاک نشده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/Futball180TV/101666" target="_blank">📅 17:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101665">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f40a1d01f.mp4?token=kJvFWe3mZCGG68cTqHQ2uFqZMqDQ37LZDHlek1YO5aqW2nrQdKW9Ww7_BpkQAJbJEJlE6Si2sp0ThWHFVSW20p8U3jNCofIR58XL9jX1ISgd_kAvIMpikuw8aUsE5WQnCFcrf9wxawysz5HSLC55q5qyP1VZO_VwP89vwRNfJSjbljm-wTJUpTi7EfdVhfS-Pb9-umSImbl2CUEBobmRgBF4maR5mM5AwsWNvPuAtFvj1WyIzKxC-4B0bnwiqYAR4PI-yfbHiBWF3mOYOLHE3Xa-llRHssXiymloOUv-gmT7rY3s_DSbNRU2iDEBWKT1KHZSXvJW3lm9BjcHAYpyvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f40a1d01f.mp4?token=kJvFWe3mZCGG68cTqHQ2uFqZMqDQ37LZDHlek1YO5aqW2nrQdKW9Ww7_BpkQAJbJEJlE6Si2sp0ThWHFVSW20p8U3jNCofIR58XL9jX1ISgd_kAvIMpikuw8aUsE5WQnCFcrf9wxawysz5HSLC55q5qyP1VZO_VwP89vwRNfJSjbljm-wTJUpTi7EfdVhfS-Pb9-umSImbl2CUEBobmRgBF4maR5mM5AwsWNvPuAtFvj1WyIzKxC-4B0bnwiqYAR4PI-yfbHiBWF3mOYOLHE3Xa-llRHssXiymloOUv-gmT7rY3s_DSbNRU2iDEBWKT1KHZSXvJW3lm9BjcHAYpyvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
صحبت‌های چندی‌پیش مهدی‌مهدوی‌کیا اسطوره فوتبال ایران درباره تیم‌ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/Futball180TV/101665" target="_blank">📅 17:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101664">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PB6aURjh67VKJhAhNBy9vyaTrFb3BVsUtIe9XkvHlJ1FyUvXKiR-s6qgBYIqRj9OUkl6JcTgd0vPtTYadAeuvKC4Akg-lNny8TiRMkkTOlWmKubcg3thbQdGCSiZrNCDNuiM5F1IgQM1IKe61rE2Hkbkh3I2lIkCw7M9U9X4QirgVQFyOTdl0yaWHyzxwiuomxtGvI29Ndyd_uITtmrsXU4daVd4Yz-3f_WuDlrZ2oDRToXzWudkZ0LaYMDDbKcM2XWEOKpgICko6Mj93D6mj2atqceE6L4gxSWsWxXJK8RSrGhLuNoRCVcq_itl56qHrdyamqq25IxufwSw-s8ebg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گارناچو رسماً به صورت قرضی با بند خرید اجباری به استون ویلا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/Futball180TV/101664" target="_blank">📅 17:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101663">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUoWVDp1wJ2xdYE1idcnFrBSYzyEvdEL9EQu7JwCxwlyc93YpfbSRPtCFQZ70296OALQB2uBRAI0mDqsP0y-YG-2Gz9lLoKjHryfzLqhCp9RykDMNmt8cE9eLY_sCcdCl1g--XcBrMaVEI-cIk1OK0L4BNqDCx0U_ICMi3Wmo56XNuOPwgj6A1ciYD_eDQO6LjMFIiUjw3xPLaLwGMMaBNakmSMW8i5Rij8pGnh2d1jOOVgw4ARM1azTAruqp4qJzNPi38kscIA-2B0Bw1jXveEW99c8SNv2ZAFVO7678OnjH8tWri22CLFrN38O8t2mLKjwMOdpAHLRwhNvdR9mDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🔥
آمار ۶ مهاجم برتر این‌فصل اروپا:
🇫🇷
دمبله ۲۶ گل‌ و ۱۴ پاس‌گل
🇩🇪
هری‌کین ۷۳ گل و ۸ پاس‌گل
🇪🇸
یامال ۲۵ گل‌ و ۲۰ پاس‌گل
🇩🇪
اولیسه ۲۷ گل‌ و ۳۴ پاس‌گل
🇪🇸
امباپه ۵۶ گل‌ و ۱۳ پاس‌گل ‌
🇫🇷
کوارتسخلیا ۲۳ گل‌و ۱۰پاس‌گل‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/Futball180TV/101663" target="_blank">📅 17:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101662">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb77439ac7.mp4?token=UrS997TzuZJOYvpAJypwo2CjCsqREHKG1OO6Ho-mJ6zlE-b8FykqPNlCqRGzJPC5F9zLYxzc3LlvbsbBtHJa1mi817NmFSHs9pjUFmhp3BshXaAoIr4SMZL00GC0DbmG-zeIubRHQZKm1wiFOEen1Z9EacZlE5DmSsj4-_2dAy-em0wW0pSbE_oOwLUISPXOSRwA7fl36XXf7LfZcP3dDubNXnQRqby_uaLuU69HQd5__cME94MSXtlvhSIv0KOLhdAoEw2n7ae2PO4nQrAdqQKWbSIelrysuY8ZvIV3ONiEzMaIwOdKdkcO7uT0zR5jYmrTo86Su0CEc21uvDvrVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb77439ac7.mp4?token=UrS997TzuZJOYvpAJypwo2CjCsqREHKG1OO6Ho-mJ6zlE-b8FykqPNlCqRGzJPC5F9zLYxzc3LlvbsbBtHJa1mi817NmFSHs9pjUFmhp3BshXaAoIr4SMZL00GC0DbmG-zeIubRHQZKm1wiFOEen1Z9EacZlE5DmSsj4-_2dAy-em0wW0pSbE_oOwLUISPXOSRwA7fl36XXf7LfZcP3dDubNXnQRqby_uaLuU69HQd5__cME94MSXtlvhSIv0KOLhdAoEw2n7ae2PO4nQrAdqQKWbSIelrysuY8ZvIV3ONiEzMaIwOdKdkcO7uT0zR5jYmrTo86Su0CEc21uvDvrVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حمایت سید جلال و قیاسی از علی دایی و کنایه‌شان به بیرانوند: بعضی‌ها اصلا نمیدونن احترام چیه، هیچی دیگه سَر جاش نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/Futball180TV/101662" target="_blank">📅 16:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101661">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/098313b0c4.mp4?token=DSE3HdPOFMH0eypkvXK3igm_Wvs1UUa43lnv464WxEMPIsQaODGRxcrMKR2H27gEmQEiyPiQN_zZkwN2rYQleRWxWjU1a3dMI3mgrFy44itNXRjM_2IuNV7dDaX8EURXVH9im8yUnwLQACZ8Xd7hGUC9mTybEUtg5DuCGmHfGVeXyN3I1FRZxpahDl6KwOT3rMQzwoKjeuLNv2kK4ZSt6D2qRyX9lYVWHl1mOSdyCtk8_F7gqzzH_Cv95cBYvWwOWZt5YgT0zY_X72EVN5dEU-TWfYIEfyevX9WqoX381qjqNSOjseshBKWQCjbDY1i7m9FFna4gayYLM1Pq3GpNPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/098313b0c4.mp4?token=DSE3HdPOFMH0eypkvXK3igm_Wvs1UUa43lnv464WxEMPIsQaODGRxcrMKR2H27gEmQEiyPiQN_zZkwN2rYQleRWxWjU1a3dMI3mgrFy44itNXRjM_2IuNV7dDaX8EURXVH9im8yUnwLQACZ8Xd7hGUC9mTybEUtg5DuCGmHfGVeXyN3I1FRZxpahDl6KwOT3rMQzwoKjeuLNv2kK4ZSt6D2qRyX9lYVWHl1mOSdyCtk8_F7gqzzH_Cv95cBYvWwOWZt5YgT0zY_X72EVN5dEU-TWfYIEfyevX9WqoX381qjqNSOjseshBKWQCjbDY1i7m9FFna4gayYLM1Pq3GpNPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⛔️
نگرش متفاوت دو سرمربی؛ یکی شکست را پذیرفته و با قبول واقعیت به فکر آینده‌ست؛ دیگری زمین و زمان را بابت عدم صعود از گروه در جام‌جهانی ۴٨ تیمی مقصر می‌داند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/101661" target="_blank">📅 16:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101660">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2eee7743d.mp4?token=McoEZ5_BQRDembH1ZNyXeV5lEngGZp1x5N2B1-YYGYMudDA2qLjlEW28lnYFScAZ1DooPgcsb_nr2F22yDoYW3LqTmLTdFiCmpSbWCHxbSf0PAiAalVcsqj92FoNLOVZ-LRo6DOEpKq8co2FIloUqHA1Vj-viUQBpUVJWF3LEar3aMjPgH4uBTdBUx8vPddqpkz10U_rTlFCnQaPBMsSxCkK7CR8LCfnJOf_8RdHhECrCfL8lxtWnIqBHC3rtWneQOizXi-kCIr7e0HxH7Yxuuh3g1JYp0fCa7PoZN8oqrB39rrbTIqKTdAWuxoymmxz-T5ZfqtatYlibzznQjvzKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2eee7743d.mp4?token=McoEZ5_BQRDembH1ZNyXeV5lEngGZp1x5N2B1-YYGYMudDA2qLjlEW28lnYFScAZ1DooPgcsb_nr2F22yDoYW3LqTmLTdFiCmpSbWCHxbSf0PAiAalVcsqj92FoNLOVZ-LRo6DOEpKq8co2FIloUqHA1Vj-viUQBpUVJWF3LEar3aMjPgH4uBTdBUx8vPddqpkz10U_rTlFCnQaPBMsSxCkK7CR8LCfnJOf_8RdHhECrCfL8lxtWnIqBHC3rtWneQOizXi-kCIr7e0HxH7Yxuuh3g1JYp0fCa7PoZN8oqrB39rrbTIqKTdAWuxoymmxz-T5ZfqtatYlibzznQjvzKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
مهدی‌قایدی: حسرت خیلی زیادی دارم که چرا بهم در جام‌جهانی بازی نرسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/101660" target="_blank">📅 16:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101659">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
فرانسه کارکنان سفارت خود در تهران را تخلیه کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/101659" target="_blank">📅 15:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101658">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ca9e664c4.mp4?token=pDg6-wT3h_hqXaXduX-EgTvruowFfNu7IJVbklCPhendsL4OktX6XRBIWscmXMvNP2o4eEk9Hvs21ST-lO-K2OLazh_viNnGPxZ2ZHmtd2QzYy1snKRoJVMw0k7OYNTXerQ8wuPQcwO_oncOJZ3stLlzfUU6_rlooSSpMjhsWGe12F72hD9XAUocgrmUbuDJvaUx0vBOchMfQPqCWqjALf-J6Y5mBYxUEPwfzTGVio7y4Hx78BWx9K3u49WbOAT1xdc3p0RzIyjiKGmWU0D-wb5sI-Z53kksZPU6_TJYqxKZERay3265Kxo2jQOsYcMKoovig7t63I3CB-Xf9tIwgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ca9e664c4.mp4?token=pDg6-wT3h_hqXaXduX-EgTvruowFfNu7IJVbklCPhendsL4OktX6XRBIWscmXMvNP2o4eEk9Hvs21ST-lO-K2OLazh_viNnGPxZ2ZHmtd2QzYy1snKRoJVMw0k7OYNTXerQ8wuPQcwO_oncOJZ3stLlzfUU6_rlooSSpMjhsWGe12F72hD9XAUocgrmUbuDJvaUx0vBOchMfQPqCWqjALf-J6Y5mBYxUEPwfzTGVio7y4Hx78BWx9K3u49WbOAT1xdc3p0RzIyjiKGmWU0D-wb5sI-Z53kksZPU6_TJYqxKZERay3265Kxo2jQOsYcMKoovig7t63I3CB-Xf9tIwgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجراى مريم اميرجلالى و حميد لولايى در بين ٢ نيمه جام جهانی‌سمه خالص
🤣
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/101658" target="_blank">📅 15:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101657">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔥
▶️
چند سوپرسیو دروازه‌بان در فصول‌گذشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/101657" target="_blank">📅 15:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101656">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a89e53e52e.mp4?token=DfKOWMRJcQVnfVqhYDDtFfE-fat9g_Zd3CKqNiC-WFPmKonhckqnfXG7vIBqFAdVbzKEukRkq-MYUVWdEvsVdqcuec-xHr6Pt_WjVWXIbVg8ZHoZE9Ix91PaCUO_sCX5Dyq5luXSNgflpDPPfCh1HlgAn3of2Gu8CwIUfDek9e8E24dgSscR80xcHQV5QvNJzPKWHK43w2OzeybnkBhc1jPJZf6GvJDsuYvSyBmeI0_lBZt6FOwIDzpTu8dyUybpciSpYP6EdPq97O-NwiY6qEcu_N3tFQeVS31IoPwiQYk4-ii2KPFrExwOZ0HeZ7zeI4NZkR_EE00XfKef5G0z7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a89e53e52e.mp4?token=DfKOWMRJcQVnfVqhYDDtFfE-fat9g_Zd3CKqNiC-WFPmKonhckqnfXG7vIBqFAdVbzKEukRkq-MYUVWdEvsVdqcuec-xHr6Pt_WjVWXIbVg8ZHoZE9Ix91PaCUO_sCX5Dyq5luXSNgflpDPPfCh1HlgAn3of2Gu8CwIUfDek9e8E24dgSscR80xcHQV5QvNJzPKWHK43w2OzeybnkBhc1jPJZf6GvJDsuYvSyBmeI0_lBZt6FOwIDzpTu8dyUybpciSpYP6EdPq97O-NwiY6qEcu_N3tFQeVS31IoPwiQYk4-ii2KPFrExwOZ0HeZ7zeI4NZkR_EE00XfKef5G0z7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
❗️
علی‌قلی‌زاده: امیر‌ عابدزاده استعداد بی‌نظیری در نوشتن و رپ داره؛ از او خیلی چیزها یاد گرفتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/101656" target="_blank">📅 15:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101655">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEXta4jOvFS0jlo8G5qtenvAOSz1qbROLwkgaHVUi9u_Y5fnlOzhZt63E0x_MNUgxnaH1OI9HcYgS8k_rbYdQXapwCi1pPYzh0qqBnTxxanODtl6tl_Fc0GXuR97k4WOGF4MW_CHy2yT1ithKLnItzJLP5Nu5mpypUopM8E6NXoiB6-a6BKXJDphBwa1q1Q6qpua3zjEq0Jc22qeBSCVW3-bUyvtNAkDBwNj0VFHRluGR6OVoeBfKGxzT85zrfxhK-3BhRPQAotr2Cu80t0mc6-mvWiIQKq5z1TvP7ZZb23gAEytyUff0D8gs2NMBxmmOwav47yWZWPx6B3_8xqeGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت گاوی زیر پست یامال
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/101655" target="_blank">📅 15:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101654">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00c5973b07.mp4?token=mtxO93sMBvOhGgrxo0fbzTNaWK6XOr0RaS_iItNlzmUEu1B_8hzNWfBFb9lTAv_Xg8J-iFY4ZDBcy2z19hyHVcveYeNS4xHtxCNkR1_zqqCR2rc7EZox4m-u1uxta6yvj4G7_YaiIt7Hq9NMPWvS8rXxtT0cQQkGfjgo6w8FnrvGw0vzEBvLZt1QkUzjjGJItME_nbfCR7v5BVvJ8iRtSVL9vkgQoNPMvJtj2mb7DLYzjkLoqjCW3Knj5n4p4t8GX1UnPaS_gMMdeerp0YBS8h0oNvjQA3Xoz8JiAvorVE7xVyg4lDu9Rf_mqYwthVakZmH83oatO1YGCrZrf7FBdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00c5973b07.mp4?token=mtxO93sMBvOhGgrxo0fbzTNaWK6XOr0RaS_iItNlzmUEu1B_8hzNWfBFb9lTAv_Xg8J-iFY4ZDBcy2z19hyHVcveYeNS4xHtxCNkR1_zqqCR2rc7EZox4m-u1uxta6yvj4G7_YaiIt7Hq9NMPWvS8rXxtT0cQQkGfjgo6w8FnrvGw0vzEBvLZt1QkUzjjGJItME_nbfCR7v5BVvJ8iRtSVL9vkgQoNPMvJtj2mb7DLYzjkLoqjCW3Knj5n4p4t8GX1UnPaS_gMMdeerp0YBS8h0oNvjQA3Xoz8JiAvorVE7xVyg4lDu9Rf_mqYwthVakZmH83oatO1YGCrZrf7FBdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ینی چه بلایی سر اون تیم پرانگیزه اومده بود؟! ببینید قبل از بازی با فرانسه همگی بمب انرژی و انگیزه بودن ولی تو فینال امسال انگار همگی از مراسم ختم اومده بودن.
بازیکنان تیم آرژانتین تو بازی انگلیس داشتن به معنای واقعی کلمه میجنگیدن و بعد از بازی مثل دیوونه ها جشن گرفتن اما یهو نمیدونم چی شده بود که اونا از لحظه شروع فینال هیچ تلاشی برای بردن نکردن!
بحث تئوری توطئه نیست و هیچ خدشه ای به قهرمانی شایسته اسپانیا وارد نمیکنم اما مطمئنم تو رختکن یه خبر بد یا یه اتفاق ناگوار برای آرژانتین افتاده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/101654" target="_blank">📅 14:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101653">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d995b135a.mp4?token=SVCwjyTV6GoRnKf-DiNh9Q7KmbAOz6gqPN2mcBr4mTL4ajZRmHsAz-s2gT5DXwcGo0QLUQZCZUSjSYQEZQT4WGhmqY_lS7G_vI_kB-YQlYj9FXGAe_7xzl5vr3DCSrqShvMcZf5jqlNzL_WTagoM85-LQDu8w_7QG2ojS019HN7LUccfbdN6Rhz5hMnxzmBDRjJoLQWvGMHH3YBqYLWMSYT_J5Bj8QpieVL92lUBoMIBg6cal-aOmvkT_NJ3jQq_33dSYuEE9NxTpmztfuBwRKZYUyBSEQ69W8G20UavKE9zy-VPG3Sun0GWY3XTWhvu71S2n5pCnfwXmuHhdTp6cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d995b135a.mp4?token=SVCwjyTV6GoRnKf-DiNh9Q7KmbAOz6gqPN2mcBr4mTL4ajZRmHsAz-s2gT5DXwcGo0QLUQZCZUSjSYQEZQT4WGhmqY_lS7G_vI_kB-YQlYj9FXGAe_7xzl5vr3DCSrqShvMcZf5jqlNzL_WTagoM85-LQDu8w_7QG2ojS019HN7LUccfbdN6Rhz5hMnxzmBDRjJoLQWvGMHH3YBqYLWMSYT_J5Bj8QpieVL92lUBoMIBg6cal-aOmvkT_NJ3jQq_33dSYuEE9NxTpmztfuBwRKZYUyBSEQ69W8G20UavKE9zy-VPG3Sun0GWY3XTWhvu71S2n5pCnfwXmuHhdTp6cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
رضا جاودانی در جواب نگرانی عادل فردوسی‌پور، به جای فکر کردن به خودش، با آرامش گفت: «بذار بیکار بشم... مهم نیست.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/101653" target="_blank">📅 14:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101652">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7be59d405.mp4?token=llz5JqqhOVgmYOLCq2iNEjoS4I2hUF00HEotH3tJhWxvb6oE1KHWDmDhd7DzFzZXCnPPp7Appd7Ycn_WUf5kyhQMPeLN9G9SKRiYDCT4qZedqR_YqRVjuic5jmx5poOTrvi4SpPT3yscM5g7LxtSwY8TWSTBap8l6HFRqb4n1aRm58leADupqHYsPc9Ldd7PJFgcTEUzvBv7AL9BriwUXn5ZuzVUuXLRZOJqUsoheZHRtB4SgN-M_i2h4qL1ovHtDkb7IEB_ydPyfSjYXPaAIMEEOvNJNfRCZ1enadqEX_50eN6AX8oMnu8lBIMZPb7wmFuVx3D4jLv9VIx0HpYAFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7be59d405.mp4?token=llz5JqqhOVgmYOLCq2iNEjoS4I2hUF00HEotH3tJhWxvb6oE1KHWDmDhd7DzFzZXCnPPp7Appd7Ycn_WUf5kyhQMPeLN9G9SKRiYDCT4qZedqR_YqRVjuic5jmx5poOTrvi4SpPT3yscM5g7LxtSwY8TWSTBap8l6HFRqb4n1aRm58leADupqHYsPc9Ldd7PJFgcTEUzvBv7AL9BriwUXn5ZuzVUuXLRZOJqUsoheZHRtB4SgN-M_i2h4qL1ovHtDkb7IEB_ydPyfSjYXPaAIMEEOvNJNfRCZ1enadqEX_50eN6AX8oMnu8lBIMZPb7wmFuVx3D4jLv9VIx0HpYAFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇹
شیروانی، مافیا ایرانی فوتبال ایتالیا: به اینزاگی گفتم طارمی را جذب کن، اما طارمی در اینتر جواب نداد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/101652" target="_blank">📅 14:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101651">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yt7R2uoBeoROPW_AHJEW1FjeoWFO0I8Tllm18x3_mRoa7IOVOOugeqEu8V-0SkjdXJThq8-N2cXnuSxSOFy0d_UmZSCm2Bkyjppot1TiMcjbT6q9Xxx__iw573zoXrsjxx_o81nPDNrgijDATx1eieWOeKSRd42H69vaqo_T3GvtnCXD3f8Gxb3gdm2MUUUs_GdhRlMo8XVi1EnQwfc06QyoeofCuacrqMg1fBrdrHaAbPr1QCuloESx2CqXtTnv4E7GRN6fYYEH-LGIDvalFYFppAK9oGPdvYfm2gdPcqH8S4e0lSd_769BBCi9x4MaaP0Ag0QEC7hOOJzac4UMcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
کریم‌آدیمی برای عقد قرارداد رسمی با باشگاه بارسلونا راهی دفاتر نیوکمپ شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/101651" target="_blank">📅 14:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101650">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d13a0e1e37.mp4?token=nyO6He8tqNkdYda7SndI5Gi8Qm6nijscaJp_YqIVPhlKEtVl8XnicakskM6cT53M0UEqSvCQ9uLbqWlA5KIzGV5jJN_PxO1iHhN1B-JhyCx2Dt-M8j5VmMToqqM2B3VRIXJqkUfdr4pRQaYHEG52KmMwvsvh8pLyefAdV_5U4qPXsEK3FemnS6ciFDHodH4RG2B6spxsxEDZ07nRe7xKvFAx-xnF9jJuamU1EjfZa76tCovx81pOH7v7DbuZh2OtOOQV3ZX_AVFDq3uRvqVWjtu6LrC69C8i2u7LSR7T3zpkcPRvL3dbaBRbMh6TT1BNr53EUJempeCHIJkIfV_vVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d13a0e1e37.mp4?token=nyO6He8tqNkdYda7SndI5Gi8Qm6nijscaJp_YqIVPhlKEtVl8XnicakskM6cT53M0UEqSvCQ9uLbqWlA5KIzGV5jJN_PxO1iHhN1B-JhyCx2Dt-M8j5VmMToqqM2B3VRIXJqkUfdr4pRQaYHEG52KmMwvsvh8pLyefAdV_5U4qPXsEK3FemnS6ciFDHodH4RG2B6spxsxEDZ07nRe7xKvFAx-xnF9jJuamU1EjfZa76tCovx81pOH7v7DbuZh2OtOOQV3ZX_AVFDq3uRvqVWjtu6LrC69C8i2u7LSR7T3zpkcPRvL3dbaBRbMh6TT1BNr53EUJempeCHIJkIfV_vVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
محمد شیروانی از اعضای ایرانی مافیای فوتبال ایتالیا: با دیگو مارادونا رفیق صمیمی بودم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/101650" target="_blank">📅 14:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101649">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNm20_BFAwrUPw3tRY6UKH1IvQWBQo-CbpVT6GeXhqs1bNv4irF6X3HeackwGlx6rEzkWi4ckJt8Hv9QjG1FXDTocet5nMQ21KNnfP6eoef8bx1kvGIDDpziZNBshUl4YbC-bcYbwYHZDeFSI3JVI-dE_Iwx88YSRvdSERUsRyyO9bS6BSnK_9YNEGycZEa3f8uUVvWkgPPs4Ogi-TTWO5e2ZsCN9vUdyRBT0ZA5ZX9sAtMYygDJN-hF4LqPb67yM-rkSZOiYo4tQd4mMz7SM86dlOC9SrEhNIP3Jz3pR_bjNROt0hiiUBBZvmpT6s1KLtN3d_DlAJNFBYSLfFu2fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
⚽️
#فوووووری
از مارکا: انریکه در روزهای اخیر با فران‌تورس تماس گرفته و پروژه آینده تیمش با حضور این بازیکن رو توضیح داده. قراره تورس نظر نهایی خودش رو بزودی اعلام کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/101649" target="_blank">📅 13:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101648">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f57cc284b.mp4?token=n1dGlXSyxY50yVbXOffz3Q05Gvx05T6sn7fwxxZ0Po768Gv6-5mzzWbp4wqCK-iARp3rmu22eGhca1N2LYfXBdOdIfH21whX_WyTgXjzPwgiE2etjcJ87bODdAXFadx6qJDuNZCF7LrF7ZdXHdXvweQlFX5EVAAyjO1OM_FJG9v5DtO_PqbVT_PoyJemX7XhR-BV7SekJR_wyEsyZq1hHTTidaBrIbbNKrFUeBYCYmRYLk4s6FeLkoCg-5DeBs-GbGWgA4v4kxA85pUY-2Zr_9aIFgPXMWyeBmMq6jPts9Dy-Xz1esEVs5Hw1XXN1sumf9GMLcFk3TW7LfilvWAM4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f57cc284b.mp4?token=n1dGlXSyxY50yVbXOffz3Q05Gvx05T6sn7fwxxZ0Po768Gv6-5mzzWbp4wqCK-iARp3rmu22eGhca1N2LYfXBdOdIfH21whX_WyTgXjzPwgiE2etjcJ87bODdAXFadx6qJDuNZCF7LrF7ZdXHdXvweQlFX5EVAAyjO1OM_FJG9v5DtO_PqbVT_PoyJemX7XhR-BV7SekJR_wyEsyZq1hHTTidaBrIbbNKrFUeBYCYmRYLk4s6FeLkoCg-5DeBs-GbGWgA4v4kxA85pUY-2Zr_9aIFgPXMWyeBmMq6jPts9Dy-Xz1esEVs5Hw1XXN1sumf9GMLcFk3TW7LfilvWAM4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سیدجلال‌حسینی: بدترین خاطره دوران فوتبالم بازی معروف با اولسان‌هیوندای کره‌جنوبی است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101648" target="_blank">📅 13:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101647">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b841d71bb3.mp4?token=hKuIO07qLHFg8KO6y-7hP4XcE3fn_CyuJglrRolcgrlbmEhQZVdSQjLOYBdMvAYeZG6Zl9Aoo7ZcD_prkPWrqAf-Mtmva7onvzxCd5EoWFIrYeNKnAQqRV_ljojixDkGZKe08aBDMFUDwh4Iz8AzDlV1YZWOBzdXj6v0VW7SuzJyignW6B4bWiMKPa_EsnzkjbLB3qbbSoEmZZuDhaHXwqygzFULZff46QIlUDT2hdMU87GZ5smMnXntJEL5Osfo2FRqeV2RsA3NZT5hw3FZVZ12yzfG54WTz8667_cBQNDsZPx_a1l7OgdHTerCQc4yCc7XSv0bWLWz8jxviKFdUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b841d71bb3.mp4?token=hKuIO07qLHFg8KO6y-7hP4XcE3fn_CyuJglrRolcgrlbmEhQZVdSQjLOYBdMvAYeZG6Zl9Aoo7ZcD_prkPWrqAf-Mtmva7onvzxCd5EoWFIrYeNKnAQqRV_ljojixDkGZKe08aBDMFUDwh4Iz8AzDlV1YZWOBzdXj6v0VW7SuzJyignW6B4bWiMKPa_EsnzkjbLB3qbbSoEmZZuDhaHXwqygzFULZff46QIlUDT2hdMU87GZ5smMnXntJEL5Osfo2FRqeV2RsA3NZT5hw3FZVZ12yzfG54WTz8667_cBQNDsZPx_a1l7OgdHTerCQc4yCc7XSv0bWLWz8jxviKFdUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
کریم‌آدیمی برای عقد قرارداد رسمی با باشگاه بارسلونا راهی دفاتر نیوکمپ شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101647" target="_blank">📅 13:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101646">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c225ae4bf.mp4?token=U4UK2__64f870EtCsEaLgnagzyPmSZhx6PWCDA_5aXp8q6fLk0ehpQmBOVmlrMKoqGlrZiHgvlYgAhCqfGQURurHYmGHj001-c4WHmwmThDEyYMNQiynFNoRkWPEWSI-D63tlMASgIdc7A-oadMgvXds5otFWLVPvmhHQTVE8bhOVzQkPMEdUAH1GLC_PFiXBLu7zBHZ_kU1a_77_rrAUgBWCNtm5MIG5AVhfcxyQ_wp4t6rhx2PwSxbBxNK9QZ_7zQ1G0RhlNRIEvJj7lsd5RNzmUu7he9zZPcW6DUo5lkprny-4sPyJGLcWYRkDTyg-g6T09NtMxGcVxG0gigvp4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c225ae4bf.mp4?token=U4UK2__64f870EtCsEaLgnagzyPmSZhx6PWCDA_5aXp8q6fLk0ehpQmBOVmlrMKoqGlrZiHgvlYgAhCqfGQURurHYmGHj001-c4WHmwmThDEyYMNQiynFNoRkWPEWSI-D63tlMASgIdc7A-oadMgvXds5otFWLVPvmhHQTVE8bhOVzQkPMEdUAH1GLC_PFiXBLu7zBHZ_kU1a_77_rrAUgBWCNtm5MIG5AVhfcxyQ_wp4t6rhx2PwSxbBxNK9QZ_7zQ1G0RhlNRIEvJj7lsd5RNzmUu7he9zZPcW6DUo5lkprny-4sPyJGLcWYRkDTyg-g6T09NtMxGcVxG0gigvp4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
یادی‌کنیم از دوران درخشان سادیو‌مانه سنگالی در ایام حضورش در لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/101646" target="_blank">📅 13:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101645">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UB-0gjFjI39iLKz523C12fUEA89C9firbZ7I3TJdx1h96MdjIQx80cDCH3LzuTZv1GMeu2AjppCEYxSxKyIZZgXM1M8q4AGASEGnxO5ojdJ1ZhBSI11DAqDlYRTsKMx14Qeb7H-mD8fcv0RRRv3sHh68Sw4AH8o0JCqfsi1UOiPstR-tB3XnGTk4SDIh-wwmsSFXRS3k9618L9fWEcBN-DawKtSbVacUWCaCq_7tTHt7m1bAGLho4axCgd_dgswLDJxzTTJe7PgEsejjT02I6XBcFrvv7TjkG6mfE8zYaq89eSBleAaqU_NsH7ji6KY3sp96fh9VepDD64pWdWRdnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/101645" target="_blank">📅 13:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101644">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZzkipYEJdDbZu9DNq4hyDw0wR-fkemTVt0aZDbfll-6L7X4N2sCJtSAKRvVV3Mx2w81H2_6QDnGNzxjfxI15O5aXlHUGtfSU6shqD_YsjJvH91nq4nwDZpNoLF4smRCaVv3eGzpikV4lk3kfgRsbpfrMnY3KZO92m_BZQ4PJZT1JbamlxSzV2HPmBfT-QmdekRHdveJ6SVhbv4k9hWDBwfFEQqA6laP8aAJd28XBwAU38MOKKYCZed5ujrLecLsxk0tfulfSMgmrtxvQ4LZmh4RIz6uD8uitjmWfCX-lZT4IW5XCgRA1Jayf3T-0ESzxt7H-1gkJiLWcZ11OtCaBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
مارکا: رئال‌مادرید فارغ از جذب رودری، تمام تلاش خودشو برای جذب اولیسه به کار میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/101644" target="_blank">📅 13:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101643">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2BluY_gfOjyfl102Gr26qBniqJa0rl7a-yns9Qt2Heqd_4ETewu6uDcP5RL4bvgtdN7gNlc_BrvYLOUq6bhdHMVUQGBMXY1MZd2OM0QbEZevMTyhvCIRto0ks8m4ybGwpE5f5Hri0m9JXIylqmqw-Hl-yQJhltzRonrIAZGXaEif5-eL29kRCInAMjuV8gEPbxIpNM1oNpF0Hy404YDqwfnyrnqHEcAhgcGNBGj2a7AiCgm8zY-TCZU9EKV_4x3bkWvGDOuGTuzxfNgQ-gNGa8QtXskOse_78RcHOoshRlE4y90H8odabjDLDlkWrmRZKDygmj8vyvEucy5u4KxqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
مارکا: رئال‌مادرید فارغ از جذب رودری، تمام تلاش خودشو برای جذب اولیسه به کار میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/101643" target="_blank">📅 13:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101642">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c46077059.mp4?token=iW8KNdKeyjip4w_FVUQeqGB8VBwCnXq26sFT-4ppfGPrzNgACL0bhanqEGNcjWGn77lZ9HVMuBWYB-iKk_k_g1Lr-SSz6gSjwg_a5zVJQGvWt42XFyvUaRJp5e3aYUP0t2NyLB8A2Nt4d3kUkjqfRNzuKqhnHfagCexlJYuBLFiabbWVK8yeJ1u814c85UXbZJl1oOCBD5cHCcnJOoAfAdVTJehcNbpsCRdxKQs3syadx3bfQzWbLs_vPvIAteBt1aJznmvowZEavhJmBmIkaY71wksjXyyEBaBbku5uVmGW2osK4_MEKM3eUJ4B-wKKCGSgrZLyAjAz7MMyYifuyEgaWPPUALuboqV07fHFpYkg6Qo3cq1IM4T7bGOuyZggm0iyBQEsMQDUr3ljTzB1e7hHyhJMYaEkvJbHDy1wvKst4cG9jhfXAmtSsy8nsAwWwvt8AcZOJRYgBnlyFOFh3vH_IPOvf_74jUJ9ak_Gpevr0XsnohAmMhIA_AeyVbGN-11IoWccNrnI1LBf0T6CQ3HnzjMaV77teheOvqs8lbkdeqT8MqRuWVmFM_-APefnb1dFJzApArkIo4bC4TgSkhQ9p7OLMB4oE00jKDH29THUHCNNar2oLpVxQEn6jhiXS8RfPq3xapQIvvXZRsoFkCcQSkcpHOXhkx525pppzwY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c46077059.mp4?token=iW8KNdKeyjip4w_FVUQeqGB8VBwCnXq26sFT-4ppfGPrzNgACL0bhanqEGNcjWGn77lZ9HVMuBWYB-iKk_k_g1Lr-SSz6gSjwg_a5zVJQGvWt42XFyvUaRJp5e3aYUP0t2NyLB8A2Nt4d3kUkjqfRNzuKqhnHfagCexlJYuBLFiabbWVK8yeJ1u814c85UXbZJl1oOCBD5cHCcnJOoAfAdVTJehcNbpsCRdxKQs3syadx3bfQzWbLs_vPvIAteBt1aJznmvowZEavhJmBmIkaY71wksjXyyEBaBbku5uVmGW2osK4_MEKM3eUJ4B-wKKCGSgrZLyAjAz7MMyYifuyEgaWPPUALuboqV07fHFpYkg6Qo3cq1IM4T7bGOuyZggm0iyBQEsMQDUr3ljTzB1e7hHyhJMYaEkvJbHDy1wvKst4cG9jhfXAmtSsy8nsAwWwvt8AcZOJRYgBnlyFOFh3vH_IPOvf_74jUJ9ak_Gpevr0XsnohAmMhIA_AeyVbGN-11IoWccNrnI1LBf0T6CQ3HnzjMaV77teheOvqs8lbkdeqT8MqRuWVmFM_-APefnb1dFJzApArkIo4bC4TgSkhQ9p7OLMB4oE00jKDH29THUHCNNar2oLpVxQEn6jhiXS8RfPq3xapQIvvXZRsoFkCcQSkcpHOXhkx525pppzwY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
▶️
هنر استپ‌ و گلزنی از برخی ستارگان فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/101642" target="_blank">📅 13:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101641">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQTQDCu8aQ7zuakpbUfXhCdFY630mx3T3ZH65N2na0qIuah-jP822Sg92Cg1PB3ka3JrKp9YrO3c2ASwBNe8vm5ipDmG6nYvvbDe_9N9_SVieyivkjlGYJKtDRYVKKUzRV7BdVU2hgpqShYBFieiuMDM4meuIoqOL2-D84XLs-UMHd6SyF5Ko5jlG3CHkVTu1e1ZibFbZ-X1lugSQNST7beeuV8MMaq3gCmkorvfd8l7yOM6knAO_DHKvg0_9Qr4anGLpoj9NXs0_BgKaMxrwB567Bolo1O2kEaTCCq7ztot1aYMJJEzQhqdbPrIIjV_n774vuj0UZI92V-Ici7mkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
باشگاه بارسلونا در صورت عدم جذب آلوارز، داروین نونیز مهاجم الهلال را زیر نظر دارد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/101641" target="_blank">📅 12:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101640">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1YpMlAmcb2NTfC5Yj4ilbI8_iJx9dqH0osWatlmZoAw56x9ZEpNi-g0txXhyujO3PdIP0tgJGECG2YG2F_cxO2c2ChfZfSDpi9WrgU6I2IsU_qhGSgw1fa-q4uAXPIoTc7y2YA7OIxYhQI81s7lqMuRKTkxpdbTEPd06cYccn0cXutFa65leidiYMxyp-X12y__gt83Lb4mInda3_Q8ddEN7nOs9sF-tdTQ3mim3hyYS1_O5rEOfWFzcpW18s-KlRFw5FuD8l20x1iUcCATu9T4RA1YBs48E9m_NJoPhXI1I-QA7ybLE-jITcyNa5QFTT4LTj16LU7ZXbBA5K_9-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
😢
خانم‌شکیرا و چنتا از اساطیر NBA
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/101640" target="_blank">📅 12:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101639">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8fa0ff87b.mp4?token=MKTI8OAOR_1UmdjBIn-UDl8L9Vd7H9QuGyf7W7FCPw7yU5AflqcY9jFJCiduj0GycCv_iKHbrag5gjlvBdLNujkWcl8kTm4CHsiA2NyzfJpDMhOmUt5WMZxkc9NEfx588_Ol4Ed7WnLEcI3_D5vOHZcqjJrt4dJTllyf-sQKSl_9sxqrCT9hmlSbKVDxwNWtERZmnNqByHX7-5Wga0vDpOTvhRdxolDGJ6DjlkovWGCYDYZSTEilasGkxR4rELYO-PLOZ0iPwhYSmVvAVVMn_DFnsYJyuojZ39lrA9FhMLXAOQdb_Cy5o7n4ez_RWhKlKhFJ3P7KX23PKYr1YnFB8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8fa0ff87b.mp4?token=MKTI8OAOR_1UmdjBIn-UDl8L9Vd7H9QuGyf7W7FCPw7yU5AflqcY9jFJCiduj0GycCv_iKHbrag5gjlvBdLNujkWcl8kTm4CHsiA2NyzfJpDMhOmUt5WMZxkc9NEfx588_Ol4Ed7WnLEcI3_D5vOHZcqjJrt4dJTllyf-sQKSl_9sxqrCT9hmlSbKVDxwNWtERZmnNqByHX7-5Wga0vDpOTvhRdxolDGJ6DjlkovWGCYDYZSTEilasGkxR4rELYO-PLOZ0iPwhYSmVvAVVMn_DFnsYJyuojZ39lrA9FhMLXAOQdb_Cy5o7n4ez_RWhKlKhFJ3P7KX23PKYr1YnFB8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
سید جلال حسینی: اشتباه کردم همه زندگیم رو برای فوتبال گذاشتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/101639" target="_blank">📅 12:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101638">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RoaHS77mjbLzAqc3yRMAKZs5MfxFh_Snb8vfUutjG7sapZ_JQ18JeLJlcbmYAKAcDQzzuFxmPCjP77hKiz8bwlTTiGMG2Pd-zCu03HdN-wyQdr0AgMLrMImLUcQbK4bYRRlmsI4_fJXJHWq_QpoQebEfig6MjfRat8lm0pfHXEWzcAuOsm9FMKPt1Qnn4fuuUUmpcHjEYOwmxGSiM62YdYieQq4UZkCW-yY336e_3cviaarXmgvQJV0j_K_uc-HMw4avZ597wJhn5xbtN9jqiM2o2JfV0FRAHUbZ6YiAnU3B6_ut0OrGI5A3i8oXK7fz-YPs_srln9Bn406GcciOJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
📰
بیلد‌آلمان: آرسنال حاضر است برای جذب دیامانده ستاره ساحل‌عاج مبلغ ۱۰۰ میلیون یورو پرداخت کند اما این بازیکن خواستار حضور در پاری‌سن‌ژرمن شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/101638" target="_blank">📅 12:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101637">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e657d4048f.mp4?token=HtdMqQ1S46hWzVepHLJHG5jCBDmJ3iasMxkboArj4NEEQ58MVz3-tqd2c3bMquyXtd1j-3ItIVm9MU4o1UOhr0HZYU4W-Atvm9BaRlddlqInzNOJRZkiMO70-yoaihMO_Z1-vUJB5xXwWMxWAT_o3Iw76A3TsRVTFtj9K0mMe2zaIxzMz6UAkZnEO9vd024m4NPjU4CYN1vvFiOVZtEcynYMtBclwhCO3HtR4jIcjuc-7uP9QTUx26rkS5dHcS0d5awRzZLC3l7lMjlnMvk2XJsss2CeCnvBb-ul-RLhYjFqRm2hd0hNMSFnT6ovrvILfjH8gYrjSVJJ477Ge7m6H1-uTSBZQG1l2fUcvP4PWiRUVtCUYJMizUmPk7txe6lbXafDxQUFrxIxmmMrihOYcwq_OKHJmnLqeyJpV4e_8q8tRUToOD7nyjK11HlhPy2p7O3FKsOGj1uklS9LKTHRUnKTsMR9oCHHHxf0jwUxKD14tsUWjjI5E1bPWM3tSyd4PW-XpUrfc3wQ5KY3pGWEyOBAGT0x14KwWoAK9iqzi-lq2Ii9DUOeUgiZ0At8AEPsbTcHVt24d7TPfsR-WAQhKNOSw0X6L1knlWvKIc8eIza8ksjeebCRB9XL7D5NOihzz2x6nMWxDTAtrdDBoHZ2T9hJCM_KRaC2SrhsAJmP188" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e657d4048f.mp4?token=HtdMqQ1S46hWzVepHLJHG5jCBDmJ3iasMxkboArj4NEEQ58MVz3-tqd2c3bMquyXtd1j-3ItIVm9MU4o1UOhr0HZYU4W-Atvm9BaRlddlqInzNOJRZkiMO70-yoaihMO_Z1-vUJB5xXwWMxWAT_o3Iw76A3TsRVTFtj9K0mMe2zaIxzMz6UAkZnEO9vd024m4NPjU4CYN1vvFiOVZtEcynYMtBclwhCO3HtR4jIcjuc-7uP9QTUx26rkS5dHcS0d5awRzZLC3l7lMjlnMvk2XJsss2CeCnvBb-ul-RLhYjFqRm2hd0hNMSFnT6ovrvILfjH8gYrjSVJJ477Ge7m6H1-uTSBZQG1l2fUcvP4PWiRUVtCUYJMizUmPk7txe6lbXafDxQUFrxIxmmMrihOYcwq_OKHJmnLqeyJpV4e_8q8tRUToOD7nyjK11HlhPy2p7O3FKsOGj1uklS9LKTHRUnKTsMR9oCHHHxf0jwUxKD14tsUWjjI5E1bPWM3tSyd4PW-XpUrfc3wQ5KY3pGWEyOBAGT0x14KwWoAK9iqzi-lq2Ii9DUOeUgiZ0At8AEPsbTcHVt24d7TPfsR-WAQhKNOSw0X6L1knlWvKIc8eIza8ksjeebCRB9XL7D5NOihzz2x6nMWxDTAtrdDBoHZ2T9hJCM_KRaC2SrhsAJmP188" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
▶️
عادل و جاودانی؛ دو مجری، دهه‌ها داستان!
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/101637" target="_blank">📅 12:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101636">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJMZCH7caBcKfXO54NeZIaUyGFNfJ1KRoyhvFldhH4-nhIJjTPkcQ-bChmwxoPuqPDIPXHBjVGUQt-mWnit3Mrp2RdUctotc7AZC_ceBuVfVXxVU4DKfm9Wtlwvy46YpDC-j8ziirow9Wm01tL2Feo4Pa1RrcKWQGEo7V5GNTUCnEuZXo28C7i_Wos1aTXRZHtt6YOPY1bWe6Xeml25YSAcQ1XNn32arg5FtKBcHqqyRCCrOoPq_wC41Em7kea84JltVk_z_tP1NOkHN0kitNnauM5crrpCcqc0IlIZyKB-cS-kAM2PFnv3aT--L3Sfcl2EJMft5zy24Yr8zysZRjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مایکل اولیسه پس از تعطیلاتش باید به دنبال خانه جدیدی در مونیخ باشد. او از سپتامبر ۲۰۲۴ ویلای ژروم بواتنگ در گرونوالد را اجاره کرده. بواتنگ اکنون می‌خواهد ملک لوکس خود را بفروشد، بنابراین اولیسه باید تا پایان ماه اوت از آنجا نقل مکان کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/101636" target="_blank">📅 12:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101632">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v3DTjE_NpgnrSWErLrDpTiOdVc5GeTcVSLGT3AT67c9Wag7VAi-KmskcA3bIRKMUufKPUQ4gkJ6yG3oUvWb_oTcQ-Rtd5Yqorf_gpp688yb4ZNdGj-n4HWInXJkNMrWeY_ZpS8vFyPXOStH1PnL7qWEg55CK7Ib6qRZYpW7m5Fewl7_iKKpfIi8pn0_WYvxNGeVd_WF-JPvrAO9_bMO0wNN8C3pOjkSdklWK9RpZQnVmoC7fXypL4CnNYJO2Yz0g4cxnr12VlsBR6C32N_luO4mH1-Kvc6pQ82c_gGFckZ8klct2dzUbnWs3HA_juorJgxD_ItUCCUiTMskDBw_llw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aHn5aOL8pXiX3xG5A6LP3N9F1p7n4ueCvHKHHHSdo_xFg1rpMlFYFswE3E0JskNbRrT-qUAJGtDNqVmfWUz6kcMz3ry1RYPldS0rGfO62_PIJlcxLTxc3m22O9hfS0PS7iJtHD4OVu633GsaKxgvYIAFwkqSM9wNncTpY2R4yNTaFGvBx1hTGPs4NknXO_e2w2D95dxvTYDs1djPozhmOxkbTH5FWHrMMzaX0lXLlImzhUiR4xbhS3Onix3iOOqjNtDxWOc5PXPAnvdP8pbSdrGAQikNtoM-WGFzNp7UX82dEsBD9p3lcflLK3vLU7wpagqN9vSXZ867uUwcSmJzkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cEyjgrm9o5IGmIyl5Uxa_2jdBd46HMvF419gztY5n1iiCWJfcKQgWSpVahnjNb7T-ur5kTWl-yA3RvktA56up_bLekV8yxerOli39fWOFDTm9BuC1A24C2uMeFYeEhXjJHGw67EkaGoCh3sN1oGeRTpWdMtXJNcYRJXOWkElqs1RefpnzQzcETo8zGpDOi6eD5hCR0Z7ByQGiNTwNSOtUsu-XJhx9PwKyd4JBx9iNQjCb-_m1HcZq-lJUnnNl17L0xsLDxSOC-QcXTeO5N9X1cJoZtNwD-frPALLAnQMjGQEu_p_SzT8dYvGydKghTFaE7LXEfG8zjh0hHWREnsrqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G3VNxD6xFHK9uGfoiFnJHXbCjn2KYaLh98bSbwLVAw-dPgzBD6eDGCT5pTvUi-w5iKpHD4ehTFWu7RT9zfrVhGIXmKoDvwQ109ga7YBr139ib2eKa57PATqbsmoy_qR9xWRgW7c97igun7FJF9k5L3WfFbTyRooglep4WuhE_AsYKRUPPgAPf36h_L7j6kQTW0e6_KiQ42pWg50KSTOwKMq91YKtzB95p_vichwChX3khQd_yF-5TbExW2uyuoglpGCWnQzNTAWWXQiX5VaF9ILkdVpVbKlcdi-oHJ_twOIUeCSsbHZT4YMiHWEu8hLvSJE8mpTpxyFZl1o6NJM4Gg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇪🇸
کیت‌لورفته جدید رئال‌مادرید که قراره فردا رسما رونمایی بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101632" target="_blank">📅 12:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101631">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsKyoqlWRxZf6A6WsqKLY79ChaiDquHD39QOxmIxMOzktVHN-Uv6zCX339QjMLgf_lLdBokRhJDEHkM46z0e3pSnKxt6L1GxuzFwhXWyZdT8UO7G7yqyXSb2bsT6q15F6-YAsEEHWUyqJtQ0pHFdGkizpSNXVQ6U2MbZA5_Vztpw8XrR69GBNHjEDBIvqunYTAEsUASrlXFazlRhMeEQGEx24sS6in00sFO81ppwZNnHLKvOaKIQLntFRqJpMdetG3Cd5an0iDa3VnSCxkjwTYEFtjXWCKR5p5N1evmZMID-jxImp1ZqN1aw4NzskMwtcDVXU9kyQuHGyF5oBLwE7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
هواداران آرژانتین بعد از شکست مقابل اسپانیا در فینال جام جهانی 2026، یک دادخواست برای تکرار بازی فینال راه‌اندازی کرده‌اند. تا امروز بیش از 61 هزار و 500 نفر این درخواست را امضا کرده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101631" target="_blank">📅 11:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101630">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W66tuXdqWeUDlZg_bwj6uGKJG340pdvjqSvgnl1Wjv-StwTDM3hQTjcxBI4KE73IhAJYctr-O3EdfSfXQpiSKCHRV07ffoWlNkNlh9V0n65XrZdPVgadKHo53cFGv1RlEchk37P7fe50hk9KbmI3Tx0jG-u5quZT06g_WJlAnjYvikSkgb7k9jwxjUQIWkETMq06ypdUTlFIAezrXEZi69gtl85zxzhQylImcAHjiw8t7S4f2IoBLVmli9Jqtd6qqbfLWVm_NWB-cSS05KCdA7jDgYh0az0BJUvC5B0yi-w5d2sv_AWpo7bAkGVDry46qfWuhoX1AVTdMNXhwNgnhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
❌
لاگاتزتا: پپ‌گواردیولا پیشنهاد تیم‌ملی ایتالیا برای نشستن روی نیمکت را رد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101630" target="_blank">📅 11:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101629">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fde3785bf.mp4?token=eaIqlV4Zhr8Cxo8Et0SFkfOGX8BpSg6pjZmWlsazWHUP3E2fWb4qQqb369ibiu5Ea1ffUUYR8WiDd0YlPobietqnFfe-bnn5ZTT-9FKqW5o7bDtdq_86lg8t_oCp9iATnlEYzTmZ9azQ4gji9biYLv6nfvLuF0kbK48GVq2BMeEV4EK9fgJce1fxbe0rzjsX0DzfYAkRN4WTpn2LpgeU9kQufPAzUXdwnREzhs4Tep9oINuLxrXucQ1ERu6QkzUAA5bHc_toRfclAkadnEnp6Ik5YIuYBFG-2LH-6b5oi6ga63sCmKjKIpU5QUTAwqoK9LQxI35Yi8Sljh36QlBeTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fde3785bf.mp4?token=eaIqlV4Zhr8Cxo8Et0SFkfOGX8BpSg6pjZmWlsazWHUP3E2fWb4qQqb369ibiu5Ea1ffUUYR8WiDd0YlPobietqnFfe-bnn5ZTT-9FKqW5o7bDtdq_86lg8t_oCp9iATnlEYzTmZ9azQ4gji9biYLv6nfvLuF0kbK48GVq2BMeEV4EK9fgJce1fxbe0rzjsX0DzfYAkRN4WTpn2LpgeU9kQufPAzUXdwnREzhs4Tep9oINuLxrXucQ1ERu6QkzUAA5bHc_toRfclAkadnEnp6Ik5YIuYBFG-2LH-6b5oi6ga63sCmKjKIpU5QUTAwqoK9LQxI35Yi8Sljh36QlBeTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
📊
▶️
آنالیز‌بازی رودری ستاره تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101629" target="_blank">📅 11:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101628">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lyt0d-_L6C-mapZoWnLjEv_zUdsE4R6ouxtKa0W-3z-gpwnTms6ct97d2UTvAwEK1tcO3enI1--dGLbcjfeECqvofps6Iy0mwOfaWpMLprigsZL0pEvylO7xXyBYTyfE4dAfme7OsGAezLT5BZ2BUHCcnPKpyuNTg5l2GmFXigdOaUGyfz-wQzBKQjIJRviXE-C-35QIt_0uXkrnh4W4xf6wy1j-19K676cHLeC8lvKrApnCTMj3woMdvkfTbFowoULd5QT-6Gqvmh23xXH62WamBvRmrrho5vdFN3jpHJfiCpvZfE7HglRybaJTKHJ5e1pzxEmVdzDgNsrFSC65nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
🇦🇷
اسکواد احتمالی آرژانتین در جام‌جهانی بعدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/101628" target="_blank">📅 11:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101627">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LT_eFdm72l0lDVzw7nqmggVL4Sd5uMCwchlMXu4znszUaqXhOO0huZkmO8gRzXoT_gRlCQdn_r40TJhWDKI94ZlqPtipvS7JvhOfWJ3LnKJSwts3Y9IkIglzdM2_pWmgeJ6gPhg_J99B7iys_Lz8vBGKAa-7md1dcHspP7mMasrxcnYZASbRebX0DufYrp00wiGSNCt5sgS6njF7v6UOEuQdGf6t_5J0HvZtFrbb4EU95GBnBtDTPUVwIFEAZsCoCaeUihYeMDuttUPRVySMA9K1_5YT8sRfGA3dpQlScfde7VXQ_ShopIMifHmRUQUEBs4WYmLDrrjyE-0Pe82gJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+ نیمار بعد حذف برزیل از جام خیلی افسرده بنظر میرسه
- نیمار :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101627" target="_blank">📅 11:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101626">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBrI-Ze5fOWwFtY6qfxsWI9C-uFBchttRDRIr_C0g9lwbQtmzxAaKI0jIt_dZ3WVYJW68ZnkWpyf9e1yjiqKcsjNZfmF7piZqZc_BpX91wyoD75gS7-IYTWR_VjJgIS8UM8Bk33OJw0C4tR6VXFD5MlNbo3abIJF-h_QNsRIvMY0rnWEbn9f9Q7iPw0NBogRnRZsIj7gTASbj-cVJnB45NHkILLNCJeMDGKOf_8v7y8B1UT5e_r_6G2GSoH4A1MobA9iQ2QnC2ha24adDRY_833XCT7ogiS9YmhR5neMJo-1Y5u1K_3NlYXpSsCuZx7JcclzOxFpDd3LqWzI1rfQJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
😢
خانم‌شکیرا و چنتا از اساطیر NBA
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101626" target="_blank">📅 11:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101625">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuWdiwMDrh7zpU6uCZTWJdexgp69So8RZjjUSGtsOkSs7zsRA8DiOhtmBeie4nUDNoF_z9Y97s1_qdFBHMd2WIMJd2can0C8XWMjTqAhTMowemqh17a2F0pFdWchZ5Ox_CJStQ5Vc_58qVN3Grde0EeXiE0AdhNQxnRmpemZGjyb5gMlyulGzNgvYYEjv-DqmPVbb1Y_dRw6k03yU5fFGE8M97HD2XTLJfsH3Urqn7p0zq0r04iTJ8f-oazlXyyVM1VNvWsz15NYhGUxeP7BqCkaFxO0157h8Muhhv6y297o4Ln6Aa08VAXc4if0l6Q8_dDpfGHeVMeimdBPv_qs1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚽️
لکیپ: انریکه و پاریس تا 2030 برای تمدید قرارداد به توافق رسیدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101625" target="_blank">📅 10:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101624">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9443946ca4.mp4?token=AiX2X8oV0jy_OWehVauyTIchDNYPMZbwDh6Y8CLHQpJ45CxBAzb1_ig8z94D9Nhk6VR5pU3wZFhld5vmHfcdRRCp6eydedDpxdn-i1yMGUjK0uBBdEZSrikfxQRZ4vOGbVVJbOCcy4z4SsIKHOqdRk2TbD-zVIhUzr6uKYT-6MWxLiCUH4RpZnHkCAWcrgXd6DHdiW1J0mytsbHoJlaC47g3x0ZBcxmG4xRa2FeXjZ1Tmn4Z82Fi0XeMh7NSkvpXe3veM9IdI3-mCO6ZZRE4gni_spVFdNenzM45crv65bzJ0IfaKSlEkg9_Qrv57u14lJ2yUbgz0tkrmFbLZ_IDLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9443946ca4.mp4?token=AiX2X8oV0jy_OWehVauyTIchDNYPMZbwDh6Y8CLHQpJ45CxBAzb1_ig8z94D9Nhk6VR5pU3wZFhld5vmHfcdRRCp6eydedDpxdn-i1yMGUjK0uBBdEZSrikfxQRZ4vOGbVVJbOCcy4z4SsIKHOqdRk2TbD-zVIhUzr6uKYT-6MWxLiCUH4RpZnHkCAWcrgXd6DHdiW1J0mytsbHoJlaC47g3x0ZBcxmG4xRa2FeXjZ1Tmn4Z82Fi0XeMh7NSkvpXe3veM9IdI3-mCO6ZZRE4gni_spVFdNenzM45crv65bzJ0IfaKSlEkg9_Qrv57u14lJ2yUbgz0tkrmFbLZ_IDLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
سید جلال: حسین‌ماهینی واقعا بازیکن‌نفهمی بود. همیشه منو عصبی میکرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101624" target="_blank">📅 10:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101623">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/509c49999b.mp4?token=gwEVFSpld8jmNOpcRHP4CqgfXDGMbk9le0nwsGYyNPibFz80nH1jO6mzqEoc5_l7tX2-rq_WoXW0u0I9xzZdk9czIVeeLy8QXSd4UmyxjImbr-adqsiYgRmBb_ANqohw8hPjJXgfAJArX_hut8qVMiqGRtIkM8VKy0BOXYh8qzv7NBa1l1qMj4trFtYjd2Ng47Bqt_edM2zIZuk1Iyjqe-gurdEyDqgTe2S_rggSnH2LGVIYiFlgqD5ejV1-iisjRz9QhNvh4iNQCh-wXNMjxeopknG93m7SyegJP-R3yPyLR2AEaGQ8LlaR5s5KQFCHPr1Soh9Dyk8x2n8Vsy4xTk5WQcowGUvMExe-qEeXHMrx-ZJOTGQT3tCrfxISaWYWF5AJfBA4pp8fnwUEs-VcqTFXC1l1ojuG1c4HZsIwoIfv6n_eknlakR0XiYnmoylPsHAWm6QjabEBAHlRzmIIT6BF3_ALoGFjqzOVPOGJPzQ9FmIRvyt0i-pD857qW4NGYpJKYAXC2dRMMYOnT1Dare-pn4vUAqGVbuvbBCgRo0bkaNNKmy8WbqZHkZgVjqmDyiof24igxNEI7U2uced9RDfTYL5ZvqgntJwTrRygGfSnNk4-SpcXFENYBv59evZmEF3P6kjietHDhAtHhRzVwHzjH7TEdi8NJzTfMK_cGHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/509c49999b.mp4?token=gwEVFSpld8jmNOpcRHP4CqgfXDGMbk9le0nwsGYyNPibFz80nH1jO6mzqEoc5_l7tX2-rq_WoXW0u0I9xzZdk9czIVeeLy8QXSd4UmyxjImbr-adqsiYgRmBb_ANqohw8hPjJXgfAJArX_hut8qVMiqGRtIkM8VKy0BOXYh8qzv7NBa1l1qMj4trFtYjd2Ng47Bqt_edM2zIZuk1Iyjqe-gurdEyDqgTe2S_rggSnH2LGVIYiFlgqD5ejV1-iisjRz9QhNvh4iNQCh-wXNMjxeopknG93m7SyegJP-R3yPyLR2AEaGQ8LlaR5s5KQFCHPr1Soh9Dyk8x2n8Vsy4xTk5WQcowGUvMExe-qEeXHMrx-ZJOTGQT3tCrfxISaWYWF5AJfBA4pp8fnwUEs-VcqTFXC1l1ojuG1c4HZsIwoIfv6n_eknlakR0XiYnmoylPsHAWm6QjabEBAHlRzmIIT6BF3_ALoGFjqzOVPOGJPzQ9FmIRvyt0i-pD857qW4NGYpJKYAXC2dRMMYOnT1Dare-pn4vUAqGVbuvbBCgRo0bkaNNKmy8WbqZHkZgVjqmDyiof24igxNEI7U2uced9RDfTYL5ZvqgntJwTrRygGfSnNk4-SpcXFENYBv59evZmEF3P6kjietHDhAtHhRzVwHzjH7TEdi8NJzTfMK_cGHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
به‌بهانه صحبت‌های اخیر قلعه‌نویی؛ یادی‌کنیم از روزی که مایلی‌کهن با شدیدترین الفاظ علیه سرمربی فعلی تیم‌منتخب ایران صحبت و افشاگری کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101623" target="_blank">📅 10:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101622">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1802ff2c96.mp4?token=BhGlMe6MO0ffIHMO3vRdqAsWVuczUC-T3YH3quIlrP46GoKuEvopt8dH8pV4ycZe9Yw-r1Eg0ZUSRnBW9NvPHh7B9pXLCTHusW2HmX0-dSsqy2S3WTr6c_wIGpi4CrjRZYP6kaTHYFm9-sVLDbqfp_1FcMuP3UGM_Bss8PDYxspaPTXN65-Bd5YFrkBMDRmliHKROpCd1IbmyVdq-rM7Wya9kYfZAP22GM3HoTeVrpUQ62-51EDfQhnCCm0f_ZDxbjTwR-Hgp-K5K6xuItLfRlTr63TXgz7RD3byv3YOIJfmhTrlbV1QxjzaSkw6oTeowVrqsqdYMWTfMc_oaP0klg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1802ff2c96.mp4?token=BhGlMe6MO0ffIHMO3vRdqAsWVuczUC-T3YH3quIlrP46GoKuEvopt8dH8pV4ycZe9Yw-r1Eg0ZUSRnBW9NvPHh7B9pXLCTHusW2HmX0-dSsqy2S3WTr6c_wIGpi4CrjRZYP6kaTHYFm9-sVLDbqfp_1FcMuP3UGM_Bss8PDYxspaPTXN65-Bd5YFrkBMDRmliHKROpCd1IbmyVdq-rM7Wya9kYfZAP22GM3HoTeVrpUQ62-51EDfQhnCCm0f_ZDxbjTwR-Hgp-K5K6xuItLfRlTr63TXgz7RD3byv3YOIJfmhTrlbV1QxjzaSkw6oTeowVrqsqdYMWTfMc_oaP0klg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
مهدی قایدی:
۲ سال دیگر قراردادم تمام میشود، اگر آن موقع استقلال من را خواست، برمی‌گردم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101622" target="_blank">📅 10:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101621">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db54c4d205.mp4?token=q1hNUa0cUUJce11OTLHe3TmjqI1oPRKDpvjT4AaD8HPH-JWxxhtDtOJvF7lZxeLLqwNbGL8alT2dfxivFkxa3X6lD62n5ldJu0Japeo3eNsqCraURA7uji65HN5Bj3OOqP-SVN0EJg5VgROu25dIsDW7R_3nXYBmfeXy615eAV36Xo4ZC48ZS8RXalKzldk3tXhCCDGufr0xjcwRcsvBQIEfryji3_rAE2VqAaT9mOQsA62TGeCnUxGxPZ7VakM-CTmmBAv025EmQXdHL1biMSlsFP3-KZ_C-WbCWMC92K26XrcPi69HzlyBUj1i29BGmjRclEXvMrGBTRBfSymnTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db54c4d205.mp4?token=q1hNUa0cUUJce11OTLHe3TmjqI1oPRKDpvjT4AaD8HPH-JWxxhtDtOJvF7lZxeLLqwNbGL8alT2dfxivFkxa3X6lD62n5ldJu0Japeo3eNsqCraURA7uji65HN5Bj3OOqP-SVN0EJg5VgROu25dIsDW7R_3nXYBmfeXy615eAV36Xo4ZC48ZS8RXalKzldk3tXhCCDGufr0xjcwRcsvBQIEfryji3_rAE2VqAaT9mOQsA62TGeCnUxGxPZ7VakM-CTmmBAv025EmQXdHL1biMSlsFP3-KZ_C-WbCWMC92K26XrcPi69HzlyBUj1i29BGmjRclEXvMrGBTRBfSymnTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⛔️
سیدجلال: بیرانوند رو مخ‌ترین همبازی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101621" target="_blank">📅 10:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101620">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBnkEy5wgbBu1Yoz1HJbbH2BV0L6U6npaueS_9SLljXhol0vKx459pwVlnxReP_YtmYR1gMu_FuNW1P8IF6Rcp54qZVvmIagGKFFm1mThqLtPDv8uwzzXo5VwbIjj4iFalCVeYOiydhyKNWs_b48jAp7YgmxlLq6T7vpXhSzVrofIqVpb7mjHTQC8pvC1Lg4Jw1UKjZ5wqLgrG58XeKQOaiwHc06wPsyqFYxZUPJsh7_SFcLfWCKis8U0MktTBd036CL9kHFxzcygfHHUGyAseBWyMXkxxEM3-UY6-Gg5wevVX8nWNDrX4PqouapDNkW0d-8m_mP8qvWdXMXI4kvAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
استوری رسول خادم برای عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101620" target="_blank">📅 09:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101619">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46845c1eb0.mp4?token=sLJUDgc0of-IKVqDrbCPdHR5rGI_oS3DL51My0D9HNJOf8V8m4IWYpeeYbE7MgI9jWAusGll9eMI-W5SH36jSNtHadm7Ny4yGZe_mKP6PSDOEeHu51dCDTu4AKL0r20EFgIw7rjsNXZZZfDjSe98I7u203Iz7xUH3eSrCuNkoigZGhPfV7zkuXwGsc6WeCIhDMYAheSL7uTHX5xyYIIoFGx8Gt9qNbVqXDQD-A2sDakXySBOB6zbzFxDbHYQWVrG5ZHiX7IZuEmbTg6wrcf7nejungBHUCybJyeOLoz0k8a3XR8NNm2nqcwcHVAx2mcJ3dNEQGPxzWMPhdPABozQXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46845c1eb0.mp4?token=sLJUDgc0of-IKVqDrbCPdHR5rGI_oS3DL51My0D9HNJOf8V8m4IWYpeeYbE7MgI9jWAusGll9eMI-W5SH36jSNtHadm7Ny4yGZe_mKP6PSDOEeHu51dCDTu4AKL0r20EFgIw7rjsNXZZZfDjSe98I7u203Iz7xUH3eSrCuNkoigZGhPfV7zkuXwGsc6WeCIhDMYAheSL7uTHX5xyYIIoFGx8Gt9qNbVqXDQD-A2sDakXySBOB6zbzFxDbHYQWVrG5ZHiX7IZuEmbTg6wrcf7nejungBHUCybJyeOLoz0k8a3XR8NNm2nqcwcHVAx2mcJ3dNEQGPxzWMPhdPABozQXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
صحبت‌های جالب علی‌قلی‌زاده بازیکن تیم‌ملی درباره همسرش که فوتبالیست هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101619" target="_blank">📅 09:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101618">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ae48d98ae.mp4?token=cD7tmMVgfzIOghJiwWnaLrnVlTVOeVTB9vUSu875p65svDIXgavCOi0OzeDh_kNUyZrCPJB48eL2PYPLE8jHw2kL-Kzd2ic184GifTa2b8MR9kOqMX7r2kW6h6Y3ckzPfvluD52YTGS6GnMaNGH4xdSCCfBDz2RHOH1rNlSFAytl2iz77LaPU2q2dMuKbyvoEx-v30jaLsHIA0LUA5Jf66WHP2IX8vqPsNEpdkSMaBEVRycTQaW5gyeMPeegCoQowObC_mLCvOifxDS4kURC5VumAdPVkeeS7HXXOPWNdUnkxW3S51kAquF4ZJmkz2qqvzNbFycdZdzTLATG7DhnJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ae48d98ae.mp4?token=cD7tmMVgfzIOghJiwWnaLrnVlTVOeVTB9vUSu875p65svDIXgavCOi0OzeDh_kNUyZrCPJB48eL2PYPLE8jHw2kL-Kzd2ic184GifTa2b8MR9kOqMX7r2kW6h6Y3ckzPfvluD52YTGS6GnMaNGH4xdSCCfBDz2RHOH1rNlSFAytl2iz77LaPU2q2dMuKbyvoEx-v30jaLsHIA0LUA5Jf66WHP2IX8vqPsNEpdkSMaBEVRycTQaW5gyeMPeegCoQowObC_mLCvOifxDS4kURC5VumAdPVkeeS7HXXOPWNdUnkxW3S51kAquF4ZJmkz2qqvzNbFycdZdzTLATG7DhnJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
سیدجلال‌حسینی اسطوره پرسپولیس: رپر مورد علاقم تتلو هست. بعضی وقتا هم شایع!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101618" target="_blank">📅 09:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101617">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRA1i6EiRCtohnJSDyV3DVwmFW-2R4B7bLnoZoWlvgSG8zeleTVghG0pIuRPO-DVFvNvjmWpIe4vJrcY6RrPR_eclVfuxbxvGh_GxQ5gyHWJ7x-Vh37YkYWZVOsyyxm8Tg9Xdv0ESzcO_dGVXWsRRAfmcUzliYroh-Ut_7e7iXMS5Qx0qtxhfHMgSUOyltScoRDkKWV-DCCD5OVHZneBsGC8pfqeqlfwRoaWYWD07lSXO1vmUWPWcxhhEOrkHpkar65GyGhV8I2wKVi2xBDJRWJ5l5SgYcZ-lxBemj6mLt2WU2ECSaTFWr--nIrs_Qg72mHgQ3RoWWoZwfT20FWwpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو
🚨
🚨
🚨
🔵
⚪️
منچستر سیتی احتمالا مبلغ زیادی رو برای انتقال رودری به رئال‌مادرید درخواست خواهد کرد. حتی اگر فلورنتینو پِرز موافقت کند، باید دید که آیا این انتقال از نظر مالی برای رئال مادرید امکان‌پذیر است یا خیر.
🔹
🔺
رودری هنوز قراردادش را با منچسترسیتی تمدید نکرده است، زیرا منتظر پیشنهادی از رئال مادرید است.
💣
💣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/101617" target="_blank">📅 04:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101616">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2512ad65.mp4?token=jYhDaeQLDFmxk34XHVLKtkUuqdyiHqw9Uk_J8j8ZMcN4cgRx3LEwNhR8uggh-RosFZgDdr6OPabLYJ89NWzjkFjSlxdtTZRGAFPk1JLZhnNywqWTenc66JUz1qvY4c0yLB4YBe_QnQlWgBDXaIeb5lTZynPRyCVGoGmpMgrEVJ3iIvEnCLLqSqSZAk5GqLOQ6d93NLVB0xDRFxkmFnKA3IChUTL28LG4hQrBq70jtWdwxWGHbNUo-mlGaHRc5U17t67GSk8gE8oJh1ZCh8A-eztQM0XWadV08L9s-tq_BTB37UlRzHI4XOUOA-baqRwwtUrNgJwla4CU748FRHhpjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2512ad65.mp4?token=jYhDaeQLDFmxk34XHVLKtkUuqdyiHqw9Uk_J8j8ZMcN4cgRx3LEwNhR8uggh-RosFZgDdr6OPabLYJ89NWzjkFjSlxdtTZRGAFPk1JLZhnNywqWTenc66JUz1qvY4c0yLB4YBe_QnQlWgBDXaIeb5lTZynPRyCVGoGmpMgrEVJ3iIvEnCLLqSqSZAk5GqLOQ6d93NLVB0xDRFxkmFnKA3IChUTL28LG4hQrBq70jtWdwxWGHbNUo-mlGaHRc5U17t67GSk8gE8oJh1ZCh8A-eztQM0XWadV08L9s-tq_BTB37UlRzHI4XOUOA-baqRwwtUrNgJwla4CU748FRHhpjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
⚽️
خاطره مهدی قایدی: بیرانوند خیلی خسیسه. یه روز زنگ زد بستنی آوردن خوردیم و خودش رفت، گفتیم چرا حساب نمیکنی گفت فقط دعوت کردم نگفتم حساب میکنم
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/Futball180TV/101616" target="_blank">📅 02:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101615">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsAXcR-s_olgEOWnNWf-OKCBCqSG6U6YNWdRuueK0oLPslTLrQY3aQrY6R0dTv7poMG9zfaSd5R_Wsuzw4XanyPPq9L5E5Uvz5ba0PvUHgwGoGMljfwrHIsJ6HTapN1lbtjBdvbcCXXc8Ix9H26TFf5O9aioAWo6X66oHgWlhqyyTBRKPLIC0BidupI12VxiITKBJRnbFgXfmTdRbFsXs_RLetAmSJrX8RV81DoJoLdApYSjk_pQGHm2y3ntX1WjKiJz9vbGK3I2bT8lrwuJAEpr2kSRewOl-VjU_benDmUe2ls9rHDgsfkmBQtsioJPIAaFEXRk_bxLkeZvEofS1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
منچسترسیتی درخواست اولیه 100 میلیون یورو برای فروش رودری داشته. با توجه به مدت‌کم باقی‌مانده تا پایان قرارداد این بازیکن، رئال‌مادرید می‌تواند با رقمی کمتر ستاره اسپانیا را جذب کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/Futball180TV/101615" target="_blank">📅 01:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101614">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoNF5vC5FssHsx8amy8_BoR99Y-nb6i33RaDgCM-rpgNhVuFXzil3DIpojC7s0lFvTtUvFQ2YR8t5daLFuBy-nrCkNeKxfz2Q5j-KE96ExfrYANXG6HTOAl5Os3Nd4bvaySddZLs1XHobvrAA8n2p9edRzy6yTp4BP6GBj_kHw9CfN4D3I_4iISU6RyHEl5t6hHprF_R4k6dN_aeUPOvt0zWT5H4uhYYzzmq81CCG-sx2zOvS9H8mY82g_-5I93p6gnuZHp0M0grDSyKZ3gssdYzpYHjGow2SZZY89cUKaIdN-umyya9oM66cGNCw3s7rGcOpwmrPySKBCQBbXvQJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
منچسترسیتی درخواست اولیه 100 میلیون یورو برای فروش رودری داشته. با توجه به مدت‌کم باقی‌مانده تا پایان قرارداد این بازیکن، رئال‌مادرید می‌تواند با رقمی کمتر ستاره اسپانیا را جذب کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/101614" target="_blank">📅 01:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101613">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouZ0YSsQLGOVbv2HTZ9i0n4a8au9mReLqvoB4dh3CM4qjGt27T5bOzpEtDbgDzS25aikl3T2Kxee9Wu4yqdOArKqgIth2Fg7PmwH10BlBQ6WQndrM0abgUt8WVGkX2vN4gOeXoz5OcAbBoKLVk_d-fQgwqOd6WtQS-mWvnqpbahYoJJVXs8ZHbdLVrE_IbmGw9eaooBWLRIPoY3Z04wO2kPvH-OUQuXppDUywcDs5CZwbDlXhvIP1HvZiJD6fV8U6EViWe27FsZ-I8E87zSrDpFjbzuGEHNgpQIGZ9joAiv0X8RXf7999JkLkKuXNizeEYRD9q6tnQvwhm8sV0JRNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوید بکهام از تبلیغات تو جام جهانی 22 میلیون دلار درامد داشت و شکیرا 17.5 میلیون دلار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/101613" target="_blank">📅 01:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101612">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-Fy4RtiTaeAqrsrREQiwBmdohv9uesjICyVkMyoEA-rZ0eLuq1s027RsYqMdnlxlX9BSAEfHlXLB1UqDArpBteyJIsw0OexEJLM60x4qrLmTSuR0d9o_LNBtX-5k2wKXQPB9sIJSw5CyZ29A1nqPa11uorV0lo0AJ6yyex8psEYhLG1S4U23TocAJ7zk7aAYti0ATL3ceHrr-LPo_oOUAZmI8Q4qSuKrmY7xju-a2IiCJ91f6GP-wy-AHy5cGEJcU5JemsBhLTNeTUOWRgAo00-sSWfDV7We9RqFE-phRJT_n1uNNeKVjkZzKNuwldF6qsNwWZ03LlelWhKTJ8mMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط 3 بازیکن فعال حال حاضر فوتبال این افتخارات رو دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/101612" target="_blank">📅 01:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101611">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FK0f2y_l-H4Jedv-TNh95OaJvLNk5ugsKkUnK1d2_Pl4JDsnPQTyDOZg1ki9nDv-uEu-LBfFXBjf2CaZPYyS5JSWuj0-UsSc_Bm51ri-sm36_57gYaBfrq7LKd3PQ3XfJ2fmdOzMk14-MlZO-UtCEf7LdvN7Ci0O0K61VFeK9btHW3KwfRNvq0QiY_pvfP3sgeFgbc9nIky9jUsUDy-441kavsIIpSV1R56lQVRdO64-LPPvdT7756dEJcGk6JCK7tNCembXCYEaPYJUfM2u5MNCYSmJ8IXJKRW8uS6gZp6uESrm-9tsBUtjve0UdgLdUEbhXDu-Gs0Abkx6GfDZ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/101611" target="_blank">📅 01:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101610">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NfHClRqUXn5ljKMEKvbdTa0G2fT2dgOb9nKfeo0T20qnSLXwHcLC2Apc8wiPXCG6QG5g9QG0HzEVdibI7kIWQ5TPPa0SIuB4tXeM_SUKolAKJBYKTjwHCz7ZKFkDl5SldBbVH9Jp3p_hTPmkDDmMrl34g_k0LqeypoYZv090T5xSmNxuJRsckSL508szl4Z_Br8KkfvcJP4fGCY-X6BoCbQCPAna2b1a8YVub_GyNhPSc0KslfyiyFfBl82sbEeVwpqubPZVm8SobLx7vbLvJXGGc-C4cnAHQQEmb6vKhvZUo2XT1NJdPy40vE_phtAib9XAZRhxLOuqm-taY7PBTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
کیت‌لورفته جدید رئال‌مادرید که قراره فردا رسما رونمایی بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/101610" target="_blank">📅 01:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101609">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
⚪️
فووووری از پپه آلوارز: رودری با قراردادی 4 ساله به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/101609" target="_blank">📅 00:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101608">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaKeKoCb117tpwuVUqT38AKa3VX4E9bAlVMtqqfF2k0bFehLluDkdrL8LZN8GY3UmMJuBYk1zz7NDZxpYVuRCy5-A-rtILhkVcII1BUzrAdhfW_fJnSTf-zfo-0WlNe25yHyX-3SHaZ-VcOH7VpXyZeAnksq1EqZHiQEIloKzqf61s5pL5QU072Jx5X1U3nrsvLQG64TxRffEQlcdWWVVSep5mWMf9ayIC85gLH4d-PqvhwNHFPSJuadH9RG4glCoeHK5D0r26XdvQTUAHrTVjZVslIfB43oX00AOKh7m_-k_3jdZNs5xkPxNOXZDN-sga9CzQdB_o29IC3KOyEMpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
والنتین بارکو با قراردادی به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/101608" target="_blank">📅 00:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101607">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‼️
▶️
👤
حمایت‌جمعی از مردم فارسی زبان آفریقایی از عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/101607" target="_blank">📅 00:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101606">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی؛ باشگاه آرسنال رسماً اعلام کرد که با کریستوس تزولیس، وینگر یونانی، از باشگاه کلوب بروژ قرارداد بسته است. مبلغ این انتقال ۴۰ میلیون یورو است و قرارداد او برای پنج فصل اعتبار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/101606" target="_blank">📅 00:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101605">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cadIxgmmiPdPbG7gdOf4KdwgrUYhbSi7iQlp7k643nVMs_mICsiSfnfceDTQp4lHIMs5BfGbiHUpY3uTK6jw8d0oZkJVFSXkA3u2v77vi_DiE2nPNJJqIg1EZxMfygOOkFWYaPMMXLamQLlRJgwQLCTYTQC0oq6lSU8A7szb0ZlInBrlr9fs6u_P17zczmEDDGm3CAehEkbBOlnqtvqUNPkUWakcHXWRdUbDhu1ZW-SaeZGwWf7QhcuJbO2i1u-OjExj0yGuIAd902SQ58iJGuF6OoD4fdZSgKjtWeez9uKc6HaYgUbKEU4k5Hmyn3zzw2PWyjgvbA19JOgc7N0Naw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
؛ باشگاه آرسنال رسماً اعلام کرد که با کریستوس تزولیس، وینگر یونانی، از باشگاه کلوب بروژ قرارداد بسته است. مبلغ این انتقال ۴۰ میلیون یورو است و قرارداد او برای پنج فصل اعتبار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/101605" target="_blank">📅 00:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101604">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mM8vmT5isICxyAh4Ph7vSoEQDz78ZMDmTOhcpg1LrBqy_gjv9hB4d9kZy_RzFdOs58jHpx4EtZ85r5aGQya9wLMPtUh_eyo4pIPgJW7A8RZb42fQgckeKVRu_Hi9TJCQdswiiKOB_BNnAS5u8ROKxi1cM4Lk--9QkhTlDkhbEee5oVsSR7qts_Q9u5TBk15oE4mxn01lUZrsAfmx_FzhbNO9GHafSygf5NZP_ZCJBislFvOpob1bjVgg3S09Nf6A5aLi8iBV2f8IUkYToIyhA3mMNX1CTACm3zW67DxlyhsQJSJQPVlT42y6E0WDqZnRT707E1DHXLG56jLdcP3pyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
ده‌مسابقه برتر جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/101604" target="_blank">📅 00:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101603">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bmvtiLRpRq4aR5H09gkiM-J4iVqBig5k4T11JlLQ0J19PcjbTrRpUB9DGFhsToJ0fNvM9fS-_L5lZF9O1FJUKkJOyoDqtGEyZ2_ifeyrIoPe5I3ekpclztiSZPqx-KtU8QGyDfaLCz3iNDwvx0BdspYN4t6zDqrKyUpa3zPQHurvkd7TC9RLyWwXpWjQeRwTRoglHZd4jQSn6ZxF8x_8CJw67E2AgdSnVEFgWdPNZCtaEpn_jRNrSq7O959SYd5MG8vEzRjL0s9gR0SQSgwFGBeX4NLAkE6civk17FHvIJiGj_gdqn01dvp4pWTf2DESBJAomwRtOHcN03TK-OZ6Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بیانیه آرسنال: ویلیام‌سالیبا به دلیل آسیب‌دیدگی در ناحیه کمر برای مدت طولانی قادر به بازی نخواهد بود، اما تحت درمان قرار خواهد گرفت و جراحی برای او ضروری نیست. او فیزیوتراپی خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/101603" target="_blank">📅 23:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101602">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXUyhtEQsJ_pksnis6Eceiq_T5Kb9zbSW0h06bxFdJgz-6SmaiwF1d4jUgglOxc1lP4_-O2rfp-urCKu1slG4bVc2E6--FlFa8LzZGE8DRsRNjS1Q4aUkQd4Hm2lc5aS7xJlrikPonK2Wcmy9Kt8VSbGPf8C6dBTQFZLcEOqXN6CVCOK2RoyUYa00zRLyK1h6ekzxwauDZPq0Qx630siZzQhmD2mW3kGFX_fLkl1WnHx3xEkTE9ilQbdbvuTnHemhVOtE8E9jjuoeulV4K3GqXzmFciS9dky1h1YeqWirDPkLYZrvIBZVx6jTBLc2Bb2qlAQ7ERRAU7oZ_0waCJ17Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
توصیه‌مهم صداوسیما به مردم ایران؛ فقط کاش تجهیزات هم تحویل مردم بدن تا خوب بزنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/101602" target="_blank">📅 23:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101601">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGAuIJ3M5B-JgrH_3CAICG8fFI04GDI7Zu_IEOEE7Q_nTkt7fG-42OhKlNcMw6fNFZ5kWcpoIWbu3RtV6QUlp4bx1LoQmg5Gug-DlW752fOWhjiLTOzR6-mO9Boi2PoAwKpIB9aZSW4SkMvLjca_sgiBxJLIhdXyLpE6nBoh7GI6TayRvIDv8mZZFft-GP_FFlriv7TLPYLmGXbpXMSW_oEITUaQ_PAWG-ROUzZtdpd10oKJznWJ21VKefDDlBJKdWMo0VzYAu4cKF0DjVWHuTkUn3ly2o0VI3c17XgfR44OSU_oiaiezJV3_4RhdyQxlZRkXQOtCKL4Xj4O4Rcmkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
🔝
ستاره‌های حاضر در لیگ MLS آمریکا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/101601" target="_blank">📅 23:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101600">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoaQ_Z5gBJL9bS520SSIIXTe0wcEe5X3ea9KqRc1J1EiQL44w_nLGxzR0u-c4eEqOOGm7pbNktcsczZpwYvQVUgyo-_rIf8ueIPJCBMCOQSy4ReH_TjhcCQRwzd_RP8fdKzca-io7rZag6SjMcGzuYRTIscBaUZaPtYvkxl1AnqX6rnPMU6dTIMVOVQgfEkZgGAdf0SeQMYhMotXrODVOoPZt-zNW6a75fc5PFYM0L-Wt00_K9Wgz-VymfCyHOYbZMy8Qt_gg4DTXmMYWAXRi8r0LwVY73kPM9DxVYlxxMjgaQKXgKNkJBrItLzHmBimQknhB3gfxMNaTG7_QuiNLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فووووری از پپه آلوارز:
رودری با قراردادی 4 ساله به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/101600" target="_blank">📅 22:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101599">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODqweSpC82JCSS8Qw8vM7_i1qIIkNE7jWsQx36o-FzOvK6BhmdVQ6lip23X7Hlb0UCnxvZLQqkgh87FeisZeSRfE9InguGjxsJV4o9KvFSV-FSv1hvcZefTtyBb5TQ7M2DqYiAX9dW5o920nivBu-L4bjcZo7BiNK3VZ4AjVLsQmckU4sb92_wFQ9_korLAOD2HiD_GBPvxPa-Kb_aVyayLRokKQ1zda0zKu4O7NBht_HSUz7WixIXYxWPElZfLwXcDcnBbGhqXgU_8JFOhHOUsddhaLwhMLol_cmzuHM0KVmP3aXgBVOu1V4gaaw6hKtcT41qiWF4xtm4DmG3ID7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فووووری از بیلد آلمان: کیلیان امباپه به فلورنتینو پرز اطلاع داده که موفق شده مایکل اولیسه را برای پیوستن به رئال مادرید متقاعد کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/101599" target="_blank">📅 22:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101598">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMBapHJML2sW3PDJHdo0YNTdozvgDUogwFhbxpMSX7mO9eJc3N0P18UynovXTxPCj1JZqdusCkQhzaiR54_TzMtGwUMGAdsamsaWN3EMeRJu-WLzA68LTtp6nSmaFZTzpPTUib7bJcvdGjMgrV7adpzJyBE_nJIZGowwmlzz8T5rIGu3YRcThHF3CLEz1qMPzn-m2V4sjjblRse73ReFwJ6ldXHzNYPmxBcGRY7anKGAQtTLul31suXhi616gQGiGHB5ZaSJzkXEw5h5JHIJf_dzFd5SMaxHgl8fqLZ2cNR1V-_3A6_MipH72PqHxqz_4jMyzw62C7X6tYGGnv5uGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشکلی که وینیسیوس این روزا باهاش سروکله میزنه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/101598" target="_blank">📅 22:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101597">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nC6rt3wonH3MioqcN66FzB8h8YqSaTK_oF1glJNK1GFN2MNV2rZsbck9E4JSj-aIsKgLojt-VKx86q_yvbYZourpricS6s6n8vS4elDl99q5jDhXBKYXFV_codg1Eg6p9NMZ2nrc7xDNOHIWm11f2oKYgS3Rj4-8S64e-t3XSMlYzqIxen9Ru4Kea26hfaDMp-WIGlFlaElNpdQT-96eaFRKdIAkTHgCeg8Yx2PbSSVVV9ffO6mYm00jgoRPvUlB0n5bQrMSESUWYKfCctBUN1qxeHUlq5r8hCpxhn-nEHnJour-_8v18Fm03p6ZM8HDzVoYXPZRiRzi5nv_V_9uAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
فابیو کاناوارو:
اگر من بعد از قهرمانی در جام جهانی و کسب عنوان قهرمانی لیگ، توپ طلا را بردم، چرا پائو کوبارسی نتونه این کار رو انجام بده؟ به نظر من، کوبارسی فصل و جام جهانی حتی بهتری نسبت به چیزی که من در سال ۲۰۰۶ داشتم، پشت سر گذاشته. فکر میکنم او بیش از هر کسی شایسته بردن توپ طلاست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/101597" target="_blank">📅 22:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101596">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YM9qxUER-nhikRzRO-mtpnH3wDrfIscPwBf7nLN4YMMW6w6EZhpgO0DZGSYuDbRUL3rLYLvrxN6wd9cUBUBcwnzdBp4dqhSwpmwgVnLbcCitN7TjExta_g8A5lu2IquJDD_24rob2kBO8gV635U_R3bCJYyfTGUOG2Fp6Cwkiwe7eLOheiV45kAytZAHfR4_fKgLE_RKtsapKXO4RZGq7yMymFvaO6apHUI9R2mjehGekO7rtMNraj8KmVxU0UfU93utZUkqhVCl75zSJQFz_nGeRrD0sJHJi0jsq33Lht1V8WYGOoQdbmL5QynoU0neXHpYGHmQysKdqsLplreBCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🗞
رومانو: سامرویل ستاره وستهم با مبلغ ۵۵ میلیون یورو راهی الهلال شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/101596" target="_blank">📅 21:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101595">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mpf3CyzSwXdj0D_lEnByPRW0wzXdfSaIbYnJ5GCk2opyeKlXXk0GluPz7o6QC2Kumz0uULJSeOMTwmQ7c-4kxQWUGysq_qYrAs5UuiRQPakrREnfjd06oEIaE0pqFQc-xhXwzzKu5tw3Zj4xBiZjfR6qgxgjSJ06z7Q6B3jaIiwBs3VLp1c6A2tnwddleY3NzKDDkc8N9jbgPEDlOZPEKjxt5LzMHnf6RXJ-1GRXQrwNzDEZa4jfHRvoKG6UMD7ftK_uxU_w46DGsPyYmzX3cdO56IBk0MiitdLxnBKifeeLki5RoUNdsKc7j9p3JSviK8JhcIj8jFOYzg6Azi6RVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
لامین یامال ناخواسته بعد از فینال جام جهانی یه تبلیغ خفن برای یه برند لباس جور کرد! او چند بار توی بازی پیراهنش رو بالا زد و لوگوی برند آلمانی 6PM رو جلوی چشم حدود یک میلیارد بیننده نشون داد؛ اتفاقی که باعث شد شورت‌های این برند خیلی زود بعد از فینال کاملاً فروش بره.
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/101595" target="_blank">📅 21:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101594">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lcbpk5_7Z8U0MqLBnHcw-Q4cS0MkXv38HzsavYPs0vnmXwRFZC4STPd6PkbkAy2QiFVOBwTdBwapDNqChr6m78aJB3Oq5EnArSKNyLUZg4bzfFhV76zCkufC4u9GGdc94u38Rrg91y3lp_MzjQJdzNSCgXlkYz6kGQRtpc_OeRwDKmOi6y2ylEciFE2drIAaZBM0-eboYVCCNWnO-79-rODhGGM10grmKtfgcQWS8BPiuEQCNVuPSs2_QQ_IjHfAIrrYpL2xVtM0MH9pdOmS4ILRL4rFdRi83vqW0gX1Kb3QDS-IWrFeXr7kuZQNistDKJE1qd0Oo7s6Sny2GWucpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶۰ سال بعد، او انجامش داد!
✅
📊
کیلیان امباپه حالا:
⚽️
🥇
آقای گل جام جهانی ۲۰۲۶
⚽️
🥇
آقای گل لیگ قهرمانان اروپا ۲۰۲۵/۲۶
⚽️
🥇
آقای گل لیگ داخلی در فصل ۲۰۲۵/۲۶
تنها اوزه‌بیو
🇵🇹
پیش از این موفق شده بود در یک فصل، آقای گل هر سه رقابت باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/101594" target="_blank">📅 21:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101593">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
#فوووووری
؛ دیلی‌میل: نیکو ویلیامز ستاره تیم‌ملی اسپانیا پس از تعطیلات احتمال بسیار زیاد از بیلبائو جدا میشه. آرسنال از مشتریان جدی این بازیکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101593" target="_blank">📅 21:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101592">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76aa3864d3.mp4?token=ddr4Ne_PUeuFzwtm1G0kBxQwEjSik3fbz2Z9KnSaTqEaUBJETxg5RBXF_r_WwfX-FlDencWGxmcqHRLB3MzBiEXUdyNjKe3kVY3hvpErORDlSLEiD4G04bP-bNDnW47pddFzMDfEV_-IZdxhHM1MctPkMNDXlebGW_XG_msJmc_Mbs9IJMtVHz7Ih_W9TCJziPj01da1KQ21jihUD7NhdCJf0T4BlJYn_R8hFHy-CEngwt2l1f_j0dOeiyjUH9Z5UtJUl5I9NZceLSbBWuILmgYlkj91R0PKftqu6eZwmErx7XlanAcCU30mlbDsLIg1U53u2jIQGcdo_Y6xJysFLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76aa3864d3.mp4?token=ddr4Ne_PUeuFzwtm1G0kBxQwEjSik3fbz2Z9KnSaTqEaUBJETxg5RBXF_r_WwfX-FlDencWGxmcqHRLB3MzBiEXUdyNjKe3kVY3hvpErORDlSLEiD4G04bP-bNDnW47pddFzMDfEV_-IZdxhHM1MctPkMNDXlebGW_XG_msJmc_Mbs9IJMtVHz7Ih_W9TCJziPj01da1KQ21jihUD7NhdCJf0T4BlJYn_R8hFHy-CEngwt2l1f_j0dOeiyjUH9Z5UtJUl5I9NZceLSbBWuILmgYlkj91R0PKftqu6eZwmErx7XlanAcCU30mlbDsLIg1U53u2jIQGcdo_Y6xJysFLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
در اتفاقی عجیب، امروز تو پلی آف صعود به پرمیرلیگ مملکت مس رفسنجان تو زمین حاضر نشد و صنعت نفت آبادان با پیروزی 3_0 صعود کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/101592" target="_blank">📅 21:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101591">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3Kz_w0X93f5xx9iDSiSS3htjtJGw7tlmNtdJYx2LUeXqT47IjpdzhXatHIZXRMcfIQF_SIHDl90uuRuI8ax_Pw8I6Ixyrz812DrTXNvJsxvgbdGyWyN7Sl9a5WaB_FOKg-w_OaaW_MfOcvrgTnXPdOjL5tGj5Hb8i7j-HVDNE825Idk8Tmb7Zc7xW9XMCcRroj8oP_7d86iZbJhHofMLs4owpuWGvNF_NUm97tI9acn8G8cBHWgSEKwxD9yb48UZATOt1UCR7ESXHvpEW7yrIpY7Py-3Cca7fm69OehytwLWQl56nl3A1VPKKs80gEtoUw297B4DPJ-627FbSCA4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ یه پستی رو گذاشت که توش نوشته : پس از کشته شدن سربازان امریکایی، ترامپ به سنتکام دستور «دروازه جهنم رو باز کنید» و حمله به ایران رو آغاز کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/101591" target="_blank">📅 20:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101590">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQRhOrItO4cedIVW4ye9rG3Qrzi5K15VwOwdMOzPrYJWA2TMj8vVjv8EAIa3VHpAHkLAbY1rvJtKCWqSZ2PlYE8xS_aDzhYhmhmWb8RQWqjRIZVqA-VwoCVZTln6caifvHpE239QVVR_t01MeREXwkE2gO2WvjLDUIb1VacRFgihWQ5VNM_Xb9bESp_8a43B2kVd_k4J-CnHI1g5daHpNI_C2Dq5e5sUBZrlS6-fIHKf6IOf5ko9tmmESwKeoLULFVFR-iXe1XTKYvNoE5w7ck83aOT6WQDmbM4AXJweFQphaImrJZqIjzmU9IIrVNCsjB3YIQfChchujcvSPrOiFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
کنفدراسیون فوتبال آفریقا اعلام کرد که این مسابقات از سال ۲۰۲۷ با حضور ۲۸ تیم برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/101590" target="_blank">📅 20:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101588">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MGmJy4jU1SMPSPoRxnxEkGNrxiTd6-JRaM5bOANwnrnSyMVUq18rAh01Pf1C-_vTwtfzKSGyUpHJbKpvtqU5QoonVd_EcP8-RIXCgLXw4aV6jQumy2iOVqownS517DOErjTY7RMG9d2MChaY7ectP06j4h3BWzwy7Au5-hsEelbwz_v0itbM_XtPPvbw1nZjw2sryJz8bEiW34a5ywCdubyg8-keAFbhZrQPnkk5V6e8rcaB-pmN1FkH0hiJztZFC9CPq2WDV16YFsG93eMSiuWTBimIBCpCMXNCvhK4t9GKc53nCF4NFlWIQUW6suni7TVbRuklQyFLTjcciQ4y7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V_bR4gRDkX8PexaDOybh83DMgM5FTdfPwa1pPuuEvIjOUplG574QstC3KUVjMdnccKtYw5mMsGh6605EZsGHjVe8_DFiAJ5GbbQ09iEl7XEd1etLeLuM5FoS2IV5DbykNgyQePJ5k3eJjJ8JMrjBD9XdaUyOSWm5qgKfnPav90dmhgFkhzJvXk2QkVinb6bb19LnLtVgU0YvUqQfe2SLw7l-NMv-BKjKlp6pCTMH21fTwLiL5PrRPm9Mpy7kLZ1CzK4PfQoUmSHC_dIK_65WTNi-HE5PLeodWW9G4FX-QYh_XakX6n51I7LaOV5eRHG-AiyikFh2iJl5l_D7y89JYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
کاور رسمی نسخه استاندارد FC27
🔺
تریلر بازی فردا 23 جولای منتشر میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101588" target="_blank">📅 20:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101586">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPe9TrAPiHy3Py8tYEwjdtXBZozZOuNi1dDt3NntXMbh8Hqm1k_wLC8f5Srx-oEgcrjnilZEE7AYVpH5wJVQJb_Vb2L5fxRJrYZAnaLOeqttBUvKZcp1kOT2OQurS_jWVmyQsRA6opC4b9c13aAQg_H7ZjhdmA5lHxnGAzONSQLHZ9-qcXz31AKbr9ZY4A6ChN37OC1xuXnnrShUSCbNyaGDgJX27XmV0zt8HjD0unwlX1z3Hx7_4DpuuZmA9bewn4XmiVshWSL2WhhDBB3xySXezYKkr-Ftlf0uCHu3Oz7rLFA8TuOvvXfJy1oPoGtKJBxICFF21YSR3AFYJWCT1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6db999500.mp4?token=SLP1rEQMWT1whC1FY9Pzy97ABf7z0bnvcBR-wjV9GWCinpVivau5WBCFQDAnHcEF2vZ_Rr0nK7xIb-7u3TYBr1QR4RHj8q6bi-oRhrdwkUDbxy4e1cX2irj-Gp17v7AFJcJOck0a1S12Z5c95qER39TfzBmrj5TX_WHKmWrQD_Ukv_69pbBH4_Wq9-3IQVsxc3S6M3saRSOTCsAEBWWG6uva32iOUPVZ6MMAVfcU8BzRFcKqahi7tG2mA94_EVngL_e5p6TAMclkGNxrkPpkX9Al6I_ZwIN4IweDjvuxA8RNQGT9ItQmLXrmLCg-HlODJBzx_UlLEgZCLAAPUfbOTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6db999500.mp4?token=SLP1rEQMWT1whC1FY9Pzy97ABf7z0bnvcBR-wjV9GWCinpVivau5WBCFQDAnHcEF2vZ_Rr0nK7xIb-7u3TYBr1QR4RHj8q6bi-oRhrdwkUDbxy4e1cX2irj-Gp17v7AFJcJOck0a1S12Z5c95qER39TfzBmrj5TX_WHKmWrQD_Ukv_69pbBH4_Wq9-3IQVsxc3S6M3saRSOTCsAEBWWG6uva32iOUPVZ6MMAVfcU8BzRFcKqahi7tG2mA94_EVngL_e5p6TAMclkGNxrkPpkX9Al6I_ZwIN4IweDjvuxA8RNQGT9ItQmLXrmLCg-HlODJBzx_UlLEgZCLAAPUfbOTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📅
🔴
24 سال پیش در چنین‌روزی ریو فردیناند یکی از بهترین مدافعان تاریخ پریمیر لیگ به منچستریونایتد پیوست و با 30 میلیون پوند، گران‌ترین بازیکن تاریخ منچستر یونایتد شد.
🏟️
455 بازی
⛔️
203 بازی بدون گل خورده
✅
🔻
پرمیرلیگ [x6]
🔥
🔻
جام اتحادیه انگلیس [x2]
🚀
🔻
سوپرجام انگلیس [x4]
🔵
🔻
لیگ قهرمانان اروپا [x1]
✔️
🔻
جام باشگاه‌های جهان [x1]
🥇
🔻
عضو تیم منتخب فصل پرمیرلیگ [x6]
🥇
🔻
عضو تیم منتخب فصل فیفا [x1]
🥇
🔻
بازیکن فصل 1997/98 وستهم
🥇
🔻
عضو تالار مشاهیر فوتبال انگلیس
🥇
🔻
عضو تالار مشاهیر پرمیرلیگ
🎙
🔻
مایکل کریک:
به‌طور خلاصه، بهترین مدافع میانی‌ای که تا به حال دیده‌ام.
🎙
🔻
کریستیانو رونالدو:
واسه من افتخار بزرگیه که با یکی از بهترین مدافعان تاریخ همبازی بودم. فوتبال و شخصیت او داخل و خارج از زمین بی نظیر بوده. واقعاً خوش شانس بودم که کنار او بازی کردم نه مقابلش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/101586" target="_blank">📅 20:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101585">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkOwx7Xu6gx19iEXw47POnbCQBXe21zTC_-SpXnPSJVA-unFwlvKOS3-dF_I2noyP5lVvE0zJ7U8qLksUE3fTUDeXxc4IY1q_xBogH5os0iVPcIMCaFsWTJgBIJuO3RQ4DA3anozw8a_IH0M-Ofo_u-W56JgNyyWwzkxQ7OsLeSdmprgjeqvA8_FOV-s-IKP_-KyuD3NPGqf292kB1rlH9EqeYKMs69H9859xhg-jtl7zjFNi1FSVP_BjS_U9futP8QmpbF161bNfHrQ6iiZukRGwrlLpQ_0VYe-MRPdzKkymsrO1fBJmrujt-kg1ljsiPUimwxIHYvxJVp8GzT4Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کاسمیرو در انتقالی آزاد با قراردادی تا سال 2029 به اینترمیامی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101585" target="_blank">📅 19:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101584">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnYqOgKf2f2FxwpGmFPk-FJNLSjTR1QqfewWSh5ufq4VdxhzWTGYv3wO9rfRXiggsZ6ljOGtGs0wM5InbZu0tIv1IFDX3zQrRDWpYAIqk1XzbZOoJzNqqzpMC1EszNPC4Cn_ZJDNIOWxrk2k964vZyLE0hnu7oPGMm_HiPLGZwZr3hGMC6JuvQUNLYbv4CIiKJhFbc5eMVx3D0N1Lone3uhXRESsk82jXoZ1RsuyRFTAmr1GMhi8VQxs7_oTgcfO2_4w_A4eddJ5H2DH-LZcM6p8uNaLGssHD094HDYZFH0KZDDjmbDN2UENPDmNGOHHGDOq5WCyNDbYm59h54ZcHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از رومانو: گارناچو با عقد قراردادی قرضی راهی استون‌ویلا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101584" target="_blank">📅 19:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101583">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b963f629b0.mp4?token=kj9fFD8nSronQxFZ5JC2aXCpUaERut6wa7PJlH5QB-FO7TTeJ5_ee5Q5PaZuT8aqbQfZgegOm3dF4u3hx-h6IVn8rdvyb-RR9GYHQ9e3jcSkj46ZkAzrlO8GmcrlvSJlh7JUWg1l1W000Ss5sh7SBnDh023hQv8d2AhDKpTBHzNzf7g6yvI1vhn4Vf5LoSVhqT_BGm9dEfVNAzZj_9wShCtxc2eSeig2LLj62A5HJr3-LYk5xQ1zNtvWSHI7cEDidAZHi_XlvSN9U9mTlk7G7HdWiVU0VatMHP4xzF-DNNQAi7WJxZackOa7jUFDvpgU6ei9qB4YDsout7IQUAFxwppXJcqll4D_Gq-sKxCLWAgBrYbx9xqRfwAuZs1otgc2BiP0lFOpS99fG9Y6QYanQSWhbUbr6oW8cS-l2d54IyX69wASuAve-eBy1dYxp7LAjL5s_esHqr4FX8zsjQXtF3D0rvMWyYc_tPMlV7YFyORKeL3OR8jfk8FS37sa7QuLheCQam5Egi4k1SsEhMaYf5tJdi4S5K_QkoRvCy0RHjsuHvszl-Vzqos3DrI6CmZTRu4uhR6VdfZnqP13Eze1J6Ze1Uc9BKlvnQJc9n4ybY15HQA_APXUiOHsnCsTGa4SRt8qHDXofHCklWYP8-wwAdYuMNJC3pFuVBoZA4VeDMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b963f629b0.mp4?token=kj9fFD8nSronQxFZ5JC2aXCpUaERut6wa7PJlH5QB-FO7TTeJ5_ee5Q5PaZuT8aqbQfZgegOm3dF4u3hx-h6IVn8rdvyb-RR9GYHQ9e3jcSkj46ZkAzrlO8GmcrlvSJlh7JUWg1l1W000Ss5sh7SBnDh023hQv8d2AhDKpTBHzNzf7g6yvI1vhn4Vf5LoSVhqT_BGm9dEfVNAzZj_9wShCtxc2eSeig2LLj62A5HJr3-LYk5xQ1zNtvWSHI7cEDidAZHi_XlvSN9U9mTlk7G7HdWiVU0VatMHP4xzF-DNNQAi7WJxZackOa7jUFDvpgU6ei9qB4YDsout7IQUAFxwppXJcqll4D_Gq-sKxCLWAgBrYbx9xqRfwAuZs1otgc2BiP0lFOpS99fG9Y6QYanQSWhbUbr6oW8cS-l2d54IyX69wASuAve-eBy1dYxp7LAjL5s_esHqr4FX8zsjQXtF3D0rvMWyYc_tPMlV7YFyORKeL3OR8jfk8FS37sa7QuLheCQam5Egi4k1SsEhMaYf5tJdi4S5K_QkoRvCy0RHjsuHvszl-Vzqos3DrI6CmZTRu4uhR6VdfZnqP13Eze1J6Ze1Uc9BKlvnQJc9n4ybY15HQA_APXUiOHsnCsTGa4SRt8qHDXofHCklWYP8-wwAdYuMNJC3pFuVBoZA4VeDMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
میلاد کرمی: بخاطر چند میلیون پول بیشتر تصمیم گرفتم یه حرکت وحشتناک بزنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101583" target="_blank">📅 19:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101582">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7LadZTwB2HTKqtPFBELbyc-uevfu02tnkysdp5StLseONYAKcV2OPnsIq-hYWwDw9uc2YU3BTI-TBUuNdWcqysIGYBVqblCsh-q22Ub0zAkJzxq0gOHTpOBSBfBESw83PYzGN3HnmpsGPpTihDckm9zSP59mRvqCA6d5Rdjb7kFHTBbjMciRxyIdHckIEfuPVbQSunpp1Jm4aK3miVIWZ8ikgcvglMu8ogMKjLijxKK6bNnU0mAr6WFZbFPnY4kLLQfC5_OgaOK1JIdzFVbDWKLjMaG0suLnnSmvdmxs2OPKLxo8scjktD4rkE-AF7AAXAwi8ykipEt_xYTEYly8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏امباپه در این فصل آقای گل لالیگا، چمپیونزلیگ و جام جهانی شد و در نهایت هیچ جامی برنده نشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101582" target="_blank">📅 19:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101581">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/723401c013.mp4?token=brkYknl5fE-sLwIBi8ntKXb941TbebilVsP6kAfTILXTdBYhWbfu91qh5oH_C-tM76o-A8PeQgUxZep5dfzDLCGZRceaXm1BBINP4nP_rEACvUUpi8X-G2xks7R0xq27YD4BOdSI-EDTI4jM_W4lCFUg-AMsB1EhKSTFHnQ2b3Rd4OyaGdxvbMGx2Tbl9Gnk0bDFNyUGgHHOOGg799tYkSEgslpEXo7gLjWW9l9MBZuVFmB3A1_K2pywboIFaJZV3ojajdC-SiZE3Pxlgw7w6WSqyV52KgNbQXox9ZoBQ6nYA1Kh6pGBKEDppGAF0Jos4M4_CNV8d2DtOLjYDN7olA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/723401c013.mp4?token=brkYknl5fE-sLwIBi8ntKXb941TbebilVsP6kAfTILXTdBYhWbfu91qh5oH_C-tM76o-A8PeQgUxZep5dfzDLCGZRceaXm1BBINP4nP_rEACvUUpi8X-G2xks7R0xq27YD4BOdSI-EDTI4jM_W4lCFUg-AMsB1EhKSTFHnQ2b3Rd4OyaGdxvbMGx2Tbl9Gnk0bDFNyUGgHHOOGg799tYkSEgslpEXo7gLjWW9l9MBZuVFmB3A1_K2pywboIFaJZV3ojajdC-SiZE3Pxlgw7w6WSqyV52KgNbQXox9ZoBQ6nYA1Kh6pGBKEDppGAF0Jos4M4_CNV8d2DtOLjYDN7olA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
علی‌قلی‌زاده: در عمل جراحی رباطی که داشتم، از یک‌عضو جسد برای پیوند استفاده شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101581" target="_blank">📅 19:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101580">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkP7wUobFm-5zGNT_74LhmMxDW_xrrQvm6My3P-FO25on2yCcWovak2doEaa7iyEJLBWmK254pbxUIIc0jSFkQzKARXOMKNsizhLpQyjA3YYXdJqmz527uMfVF0jD4bVJRlw5j6SLIWM2nNAWmodl93N-j4z0yRo4M7J6Z05hWm-q4trgXBhMuCDNQd9QovM_TIlT9182DAK-1Hq15MepdS39YnMnV96MN1_AXRr0fPpjJCdfsTYt-xB21mTINcdbDQqQ90754ufAAdbNe1WE5Q3sBwyL3vja6TbXLGi7-6PP3E8t7j3lQFAF7OZJdwn23wsESthel8oGBBT2s-aGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پزشکیان:
دستور ویژه دادم که سایت عادل فردوسی‌پور از فیلتر خارج بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101580" target="_blank">📅 19:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101579">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvqwqsBn7KvE8aPKttUXRaDOsIEYmN0NQI2l8ZBbp0Dg9ZxJnt5QOQjlSZgSFqipnTaUj7cn8nFK44PQ5-urfKt7v_Es6V35PFrnEPWFUaB-V8chSM1qJ6wRS_b34uR11oHoqkLwe9L7TNYloDsKK-eQNmyE2-Aqw0b0nVWtABLI0kH1QJGviGS3zC38a39I0vT2gdHP8eUNaAZwe4CNjzN7A-sBTGb0Lsx-0WMAb4HxmiOFX2HUyfnddb1hG4aM7U_4Uscr2Tv98a1liZnWDD1Nu284Cg24b3C8kJ_9ctTSBSFWPega9u2A4tyb4PhbfosFhKcwoOXCS_DnFqSntQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاد بولی از زمان اومدنش به چلسی 291 میلیون پوند برای بازیکنای آکادمی منچسترسیتی هزینه کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101579" target="_blank">📅 19:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101578">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYPLqCeRU4xuXtiO6E7IyMHLcJRppwfU8tJnzGkzUboJy5EInUcznqJsjAP8us8yZci9_7JS1bKEQHWzlMcOcT665C9YRvQygWoAbXXG_dR0Z2O-HNpXQowakRVh2lAmM4C9S6EhsmQIQHf13KTmbmOOPU_k7VK40eDSonIkzFPPgFqPgz2phwIZnjThiec6D94bfmvUQKMht2o8rWZRUpciQK59GD11uWcMsEQhEmjm87uyNM1_4yBQrNF1KCe6EgoO-bGEvrgKXgLbl5RZXre2-OtkAECLTbbQgAD5Q68de1zcSMUrNOaF5uo9C_50deuEVUqiZ6_QdiyF1YRsMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101578" target="_blank">📅 19:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101577">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cab44dc23d.mp4?token=gvpwBlb1yyfQWaYz9R47lrfpnbPBvf4apjRrjrtF0jK-TeS52iHYPY-BxRorLGCCX5O9Uat75XJ76JnCIwzfuFkkBg1N7g121DqrFYZkVTGBvhaEBHlKN3Ht3oi6iA9v_BpgvAB1B_PFmXLtxv962z4o_Z48XI7etraW5vSV1ZBWmxSSCaDr6jtJpZ5jcCw51qnaP5gVPYuTkd-gj-u_KTAPd_ROcKxf-emWOYKYNuYiGVJmVoTmdi5WzDik_NayOUIgdAV2YySPCm--8ZQzP9P3WJCm1zJTGqLZYF3ckKmyOEDSbmFWgy-cNXD-UxNaE5hckl9Q9SCP6CAnxCwanA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cab44dc23d.mp4?token=gvpwBlb1yyfQWaYz9R47lrfpnbPBvf4apjRrjrtF0jK-TeS52iHYPY-BxRorLGCCX5O9Uat75XJ76JnCIwzfuFkkBg1N7g121DqrFYZkVTGBvhaEBHlKN3Ht3oi6iA9v_BpgvAB1B_PFmXLtxv962z4o_Z48XI7etraW5vSV1ZBWmxSSCaDr6jtJpZ5jcCw51qnaP5gVPYuTkd-gj-u_KTAPd_ROcKxf-emWOYKYNuYiGVJmVoTmdi5WzDik_NayOUIgdAV2YySPCm--8ZQzP9P3WJCm1zJTGqLZYF3ckKmyOEDSbmFWgy-cNXD-UxNaE5hckl9Q9SCP6CAnxCwanA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
دیس سیدجلال‌حسینی به محمدحسین میثاقی و عادل فردوسی‌پور: یادشون رفته از کیروش حمایت می‌کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101577" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101576">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0c61d3ee9.mp4?token=IjT8in5e_jQIG4zkXADOii-YLq0OCvn3MRBDty215pMf2_IYfbC1OAU4_fpf2a0YzxiFLm-AB1WqtCmesyyFrnGJI3QzIpTyVeYgB66umOgkZFzucvrOthJVdOFTt3E0_UqASxKHzrtA0PI2guc3akoPefhv3MyeLIOvWqJ2xZZp3T5qk4slEu4wTpnroZTGz7YYIu-1Rzb8-kB6nvn-iY1ApH6ppJkdgO1kA0ekUzPVhjtFuniegG5VbPRw2Id-jqXThHzlp2LS2UW3a0AT-xYycq8QCiO72xD1UpOpbaeZWSwa-PJyMSDI-4kiKhP-4MLXX2A-AyfUlUSHEu5NcmcYf94omKB-fHJ3bSlFCxWET8EfNRdeN0iEuXKQDFAa38TjhUYUgEdxHSHsZutBkY-9xz2jO903_i24mBOwnb2Uu2DdLAZrBQpngvvrBokqzDlYyQc_qZA9ke2tWYe8hIBa5ganhffLH079G-GqKvt1Hbp2PLBxkBWCHLqYN1LEN8uxEod6iUelwskI2GVBvtrkQB7QK3PKNxZtL9an9wtp6VB55tC00bRPIr1T2fpSIJ502ZSQHhDYKV2F8mfYykzIbRkkYcLF7Ju8AbnpWP6mIss_uWxdnpwEiTWSBFuDEUewdjlIAJsBfsgfB_Ge-b391xMosNV3NAL451_HvvU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0c61d3ee9.mp4?token=IjT8in5e_jQIG4zkXADOii-YLq0OCvn3MRBDty215pMf2_IYfbC1OAU4_fpf2a0YzxiFLm-AB1WqtCmesyyFrnGJI3QzIpTyVeYgB66umOgkZFzucvrOthJVdOFTt3E0_UqASxKHzrtA0PI2guc3akoPefhv3MyeLIOvWqJ2xZZp3T5qk4slEu4wTpnroZTGz7YYIu-1Rzb8-kB6nvn-iY1ApH6ppJkdgO1kA0ekUzPVhjtFuniegG5VbPRw2Id-jqXThHzlp2LS2UW3a0AT-xYycq8QCiO72xD1UpOpbaeZWSwa-PJyMSDI-4kiKhP-4MLXX2A-AyfUlUSHEu5NcmcYf94omKB-fHJ3bSlFCxWET8EfNRdeN0iEuXKQDFAa38TjhUYUgEdxHSHsZutBkY-9xz2jO903_i24mBOwnb2Uu2DdLAZrBQpngvvrBokqzDlYyQc_qZA9ke2tWYe8hIBa5ganhffLH079G-GqKvt1Hbp2PLBxkBWCHLqYN1LEN8uxEod6iUelwskI2GVBvtrkQB7QK3PKNxZtL9an9wtp6VB55tC00bRPIr1T2fpSIJ502ZSQHhDYKV2F8mfYykzIbRkkYcLF7Ju8AbnpWP6mIss_uWxdnpwEiTWSBFuDEUewdjlIAJsBfsgfB_Ge-b391xMosNV3NAL451_HvvU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
قدرت شوت‌زنی اسطوره‌رونالدو که اگر‌توپ گل نمیشد قطعا بازیکن مصدوم میشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101576" target="_blank">📅 18:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101575">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/641d875577.mp4?token=kSS6YpsoCKBMkl-lstWa6MeOZZifdxGma4zueO0Zx1flUn3lDhtrcYT2-JCqhxmRJpOXbYhuMHXprlLthNd3ahqImLJ6kmE_qiKon1Al7-XS4gBD7ZMkwhKSoWmkC6P4ioMxAw2_y58XXTTr_NwWIAcQG_WMeaGmHcvT4C239v2wBkvVKUjDXBXyujxUUMU7bx9ii67VRCPnRD-YGaKNCCOopkxI4BvTHuqE02IHfkd-qAlM_VsbxvVa6eY6X-0Z2s9H7SLNWm_faVnijjVwZFhkISw-UM71RmPt4S92NuXnQKmuVnu4AowBuzvM2NZ2NRD6xrYjaLdEFzpLs6BLUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/641d875577.mp4?token=kSS6YpsoCKBMkl-lstWa6MeOZZifdxGma4zueO0Zx1flUn3lDhtrcYT2-JCqhxmRJpOXbYhuMHXprlLthNd3ahqImLJ6kmE_qiKon1Al7-XS4gBD7ZMkwhKSoWmkC6P4ioMxAw2_y58XXTTr_NwWIAcQG_WMeaGmHcvT4C239v2wBkvVKUjDXBXyujxUUMU7bx9ii67VRCPnRD-YGaKNCCOopkxI4BvTHuqE02IHfkd-qAlM_VsbxvVa6eY6X-0Z2s9H7SLNWm_faVnijjVwZFhkISw-UM71RmPt4S92NuXnQKmuVnu4AowBuzvM2NZ2NRD6xrYjaLdEFzpLs6BLUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🎙
علی‌ قلی‌زاده‌: کل خانواده‌ام استقلالیه ولی من عاشق پرسپولیسم؛ خیلی دوست دارم در پرسپولیس بازی کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101575" target="_blank">📅 18:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101574">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdff7389ce.mp4?token=QfGOXBJAcnjK_tn6gIvjFyFAhE3udy3cmzkTmr90APNtNShjleHXykLpXjp1KjT-rRQPxwzCk36XN4B9seOe7F8JvwHcGO4DdpeanPBNLc0J2p5ekDu8mJqhVpYoFrBbhkqWmcF8bspT4rtkPp7uw9M-G_-ahXoLuhg2hS-567YKs_pykjvRcLnvX4vOn9sImCHZAbMINHTXP7rGo4foldB5ufuJBDL-ow4ieLVwoPLtVTwPB7rz7A4KBq__kogr7U8Bletgx5jEdOBFpCc4rnM0uzdJDSDHIV6fjttzngD0RJlw70Dmc5oBmFxfdlEr0--5LyRdqRJ9nnaJWS7d5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdff7389ce.mp4?token=QfGOXBJAcnjK_tn6gIvjFyFAhE3udy3cmzkTmr90APNtNShjleHXykLpXjp1KjT-rRQPxwzCk36XN4B9seOe7F8JvwHcGO4DdpeanPBNLc0J2p5ekDu8mJqhVpYoFrBbhkqWmcF8bspT4rtkPp7uw9M-G_-ahXoLuhg2hS-567YKs_pykjvRcLnvX4vOn9sImCHZAbMINHTXP7rGo4foldB5ufuJBDL-ow4ieLVwoPLtVTwPB7rz7A4KBq__kogr7U8Bletgx5jEdOBFpCc4rnM0uzdJDSDHIV6fjttzngD0RJlw70Dmc5oBmFxfdlEr0--5LyRdqRJ9nnaJWS7d5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
جواب عادل فردوسی‌پور به حرف‌های اخیر قلعه‌نویی: بودجه یک‌فصل تولید برنامه من از پاداش سرمربی تیم‌ملی قطعا کمتره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101574" target="_blank">📅 18:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101573">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhHrXbqJYoz7s-QRGFs-ITXRa6tLh0ZvKwdw7UJtefb7vji5znzXjrggLrsU6ScOx_gV7iKZXnbMkBCzYqC0fWxo0H1s1a6vzMkXh15Yx0_pUypphOsIj8AF0HjfNHwGFSOLVegP3yh4VghZ25KVDxycvpN2yl-Jkz8jueUfkUI3WDzLbC_20ZZCkZI7m0Y_y1S70l37y2Phs98AXCJuW9ivjK7dvTcJbHTY7bF4EyN2pGrqgIsEzzRwqNaQTCCEznDaFrMt_n7GJGI28iD8xNzlOmwSXYViFaG9ocKgz3RH-Ni8mDuQ_79Aoo4Bwf8DF425isxD26BdppJyqPoDlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
👀
فدراسیون بین‌المللی تاریخ و آمار فوتبال (IFFHS) به صورت رسمی لئو مسی را به عنوان بهترین بازیکن جام جهانی ۲۰۲۶ معرفی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101573" target="_blank">📅 18:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101572">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f420d24855.mp4?token=QvJLcNpcN_TIHUlKYt0kt0H8Kynx5qUgADcK8FPgUo8Ogxh81iI6breeRrsgFnAbEg4Sa_h8-UkH3IjZkHjlfiDFbkgfzp51TdaOer5dU7cwk5fXw4Zck7vSeaDx0yDvA-LlhfhahXZ98ofpU7qYpp04McvUdGfJLVOBPgm547pcPzqjGL8WBeNC-A-0NHnVtDput3ORNHqHfM-s2e8HT96fy0LaSDFTGGl5YvHJmHc2r7CvMXHw06DbaasVdhAJC9SAtFnmh2Zk1BZwJszJZHkW4WF-bskbH9oyCvlOSUEoyOf6LTNxTVWIJ9qEFmwKXOAlt5vbRfvvqu3_5cuUD7NYQYkZb7UVchPhTtfPFMvxDiDRku_ZlLyChAVXpjeXcPe5z3O-YdodJsecSvPx-iXfHm9jF-0As-kscpHye-X3lqR1JFnUodLYTnDPK0sOeVPc3ACO68INyQE5ju6EPQEPz4is60k3Zx1USayu2hM3HK5_Ld8fMxt2qIYj_PQEiN8uy_9oeT2hItUyjw3FwAXY4FOCH227Gqf41-ADyHyi0BF58S8K2Nbd1cJWBGNP6pmzdl7rNSIpH2TDpV0v2afWiC_f2dUe0807KN1pfWLhxm6q3CTjCSppkNI8C4ay3-jGWgDIc2Z-5x8tfd8NIMUitrkVXoBlVf6Aebw2jDc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f420d24855.mp4?token=QvJLcNpcN_TIHUlKYt0kt0H8Kynx5qUgADcK8FPgUo8Ogxh81iI6breeRrsgFnAbEg4Sa_h8-UkH3IjZkHjlfiDFbkgfzp51TdaOer5dU7cwk5fXw4Zck7vSeaDx0yDvA-LlhfhahXZ98ofpU7qYpp04McvUdGfJLVOBPgm547pcPzqjGL8WBeNC-A-0NHnVtDput3ORNHqHfM-s2e8HT96fy0LaSDFTGGl5YvHJmHc2r7CvMXHw06DbaasVdhAJC9SAtFnmh2Zk1BZwJszJZHkW4WF-bskbH9oyCvlOSUEoyOf6LTNxTVWIJ9qEFmwKXOAlt5vbRfvvqu3_5cuUD7NYQYkZb7UVchPhTtfPFMvxDiDRku_ZlLyChAVXpjeXcPe5z3O-YdodJsecSvPx-iXfHm9jF-0As-kscpHye-X3lqR1JFnUodLYTnDPK0sOeVPc3ACO68INyQE5ju6EPQEPz4is60k3Zx1USayu2hM3HK5_Ld8fMxt2qIYj_PQEiN8uy_9oeT2hItUyjw3FwAXY4FOCH227Gqf41-ADyHyi0BF58S8K2Nbd1cJWBGNP6pmzdl7rNSIpH2TDpV0v2afWiC_f2dUe0807KN1pfWLhxm6q3CTjCSppkNI8C4ay3-jGWgDIc2Z-5x8tfd8NIMUitrkVXoBlVf6Aebw2jDc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
وقتی صحبت از کارما میشه منظور چیه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101572" target="_blank">📅 18:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101571">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8udGqy-4PTTpoeUFAYjzV0I6FdcPwl8p5XXVo5KTLL4nVWXIvr6PU3IEnw0m1ospBOzmfeqpVSS7WzzfiuKvxeXBN_WEuxePqNohbE2Y8osR8_Icd2P_dIPn2ucDB4i5XXhCa4pg3ZoMUuOQJQ3N-oZ69PeNL2-GXAZNpSTOqoAK_iatqUrNSY44DUDxyTZw2n50LuOqVM4D2h6uEVygjrm8J-pTXZGB-RdmNnT-S5XS5PUHW07wV8LAy3o7m3avIa8hBz7LZXLw7IPAafpr7oVOKlVZ-GcOruOrdh_1Kl2oqnoo9YVk0JCNWMvLHDhmP5nwF2zVjvw7UY0vlQKCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول و آرسنال درحال رقابت شدید برای جذب بردلی‌بارکولا هستند. حداقل رقم پیشنهادی به پاری‌سن‌ژرمن حدود ۱۰۰ میلیون یورو تخمین زده شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101571" target="_blank">📅 17:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101570">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb17487185.mp4?token=iUje1aCi76ydWjn5GEigV8bWYqZEwv3rRAlHrVrAl9hYAtyuWtzZpNBu6Rmr7LorvfFeSnXbYgIPCxTbL4TjhyR1GXax4PZF9BlYJ87ov58CL8dDB7PpDJD7-89qkMMaSq_zbLnB-RLfLk7BGT-nSdkzhfl0pmEIKV3hqAhqgctr88hWYBwq4DdTZgGs-ItsL1RoH1PUyyih2kZjG_KlEyNyBfayWXen85B2yI6WDkW60HGtrNPKZdMEUWn2VbuwRRyQLzEpJDPBvMo7O3N4ryxyQ0IxWFxmKdx3oFWJcIXTH_W78WTq-WaaCRuuTBbQx7ect1W2Du1eXv59zbzgYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb17487185.mp4?token=iUje1aCi76ydWjn5GEigV8bWYqZEwv3rRAlHrVrAl9hYAtyuWtzZpNBu6Rmr7LorvfFeSnXbYgIPCxTbL4TjhyR1GXax4PZF9BlYJ87ov58CL8dDB7PpDJD7-89qkMMaSq_zbLnB-RLfLk7BGT-nSdkzhfl0pmEIKV3hqAhqgctr88hWYBwq4DdTZgGs-ItsL1RoH1PUyyih2kZjG_KlEyNyBfayWXen85B2yI6WDkW60HGtrNPKZdMEUWn2VbuwRRyQLzEpJDPBvMo7O3N4ryxyQ0IxWFxmKdx3oFWJcIXTH_W78WTq-WaaCRuuTBbQx7ect1W2Du1eXv59zbzgYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرصت‌سوزهای اسطوره فران‌تورس ستاره فعلی اسپانیا در فصل گذشته برای بارسلونا
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101570" target="_blank">📅 17:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101569">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea79a8c03.mp4?token=Be7Fh9XdGZWBOpE9jpZNWyB0FvggivvZ4Fe2VgS3ONEQeHORorLrX-Y0HhhtrAUDLqKgnrsFOMbhh2I3No2I2eSp_nVeoHNtNTMVc-kQrmYlXiw_IVTOU3DMG3wza1z43HfbUnvOAlV6apeb9b459WWoNtxzNAku1XLRg9PhzDD-Qbep9wpLzRihYZ_AChmN9Ow2LAZHF0oSLs8_ezOnhUwRzhf4eFtyn42L5Kefekd3AxGT_21CxzPCpZVnafH3_19lpU3xk-WpnFwuwVLUUHyNzqJCXZCF6zk3rViUzHgl0z0_-994q1NTPS5YFpz5_LuFKmURjNZHcq1mLc1bOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea79a8c03.mp4?token=Be7Fh9XdGZWBOpE9jpZNWyB0FvggivvZ4Fe2VgS3ONEQeHORorLrX-Y0HhhtrAUDLqKgnrsFOMbhh2I3No2I2eSp_nVeoHNtNTMVc-kQrmYlXiw_IVTOU3DMG3wza1z43HfbUnvOAlV6apeb9b459WWoNtxzNAku1XLRg9PhzDD-Qbep9wpLzRihYZ_AChmN9Ow2LAZHF0oSLs8_ezOnhUwRzhf4eFtyn42L5Kefekd3AxGT_21CxzPCpZVnafH3_19lpU3xk-WpnFwuwVLUUHyNzqJCXZCF6zk3rViUzHgl0z0_-994q1NTPS5YFpz5_LuFKmURjNZHcq1mLc1bOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
دسته‌گل استاد فران‌تورس در حین حمل مینی کاپ اهدایی جام‌جهانی از سوی فیفا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101569" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101568">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7FVz4NOBwFIGTJOPIEF2NfG_rsOOaINafs0FxO6nu-CnuV8IcqiTztd91I8Q6pNoz88A3O8CERSN65HzoPPjF-rQkEtAPTkdkVAJ6sO37CKnHLSoiT3v2rmgjVsYvc8e9uYcoLP_xcxP30JxBucuALQJrEf-Ow8M7URAgpb687vKbeEEcP-uRTSleA0cxfCS1QylEUO7KwIDJW3KT5GYopeaHv4Dxluz2Y09toCYMEua_vNt5Ltxltr5j-yeKh1go1s7Wjw-1NZY7AeS5hYSjMVYRNxMp0bDJ06PZvZAvlTCXUrWt8PpP8TcPVQD6gXV1MbBc2LYOcFKrKyZvU4Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
ترکیب منتخب جام‌جهانی از نگاه فیفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101568" target="_blank">📅 17:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101567">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e38a17a2eb.mp4?token=JDqyNHzptR_VxdVNSo8VRcy5f6QhtaYzjVq-S0KItbgjFerxhPWd9bbv6cdImfAnVaBuAHQb8texev0LsvM-4oInDL7-NKnSkmy99RsQuAXBGOBuPrv5r6s3yxUE6CUNJOZD4CB611e0rVuCcQIR4KU4p5WQjxxxDdZm12o_-a4Vn5gfRH6hyvLFjZMeYqC6jdH8pjS-XnPjYyUTFs7D8_kOFmPBaPXd1v-OYneBndCA2JGJe9Z8jDkn10AdwLn-Wq7sS9pgZ_VU3Tz4Airh6Rd3GsGDF5Y5GQZN6ycg-CNU7bSy7GHbQL6VaYGaIOlZgILF3QeqCiND-ng_m7nOeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e38a17a2eb.mp4?token=JDqyNHzptR_VxdVNSo8VRcy5f6QhtaYzjVq-S0KItbgjFerxhPWd9bbv6cdImfAnVaBuAHQb8texev0LsvM-4oInDL7-NKnSkmy99RsQuAXBGOBuPrv5r6s3yxUE6CUNJOZD4CB611e0rVuCcQIR4KU4p5WQjxxxDdZm12o_-a4Vn5gfRH6hyvLFjZMeYqC6jdH8pjS-XnPjYyUTFs7D8_kOFmPBaPXd1v-OYneBndCA2JGJe9Z8jDkn10AdwLn-Wq7sS9pgZ_VU3Tz4Airh6Rd3GsGDF5Y5GQZN6ycg-CNU7bSy7GHbQL6VaYGaIOlZgILF3QeqCiND-ng_m7nOeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
✔️
پیش‌بینی پپ در مورد شرایط رودری در مهر ماه ۱۴۰۴ که در ۲۸ تیر ۱۴۰۵ به حقیقت پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101567" target="_blank">📅 17:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101566">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be9c5de5c5.mp4?token=c_7EnTaFyMi3n8iqdYvBQcHSfxK7s84JTeGODL9szAqyv5DFZrIqK9h6npdOoOXoiDepXXPc-LfNzuoFsDT67N1HNAIOg9THN9apOH9YLbPIaTAKkPlabI0N5_FSLOVjk0wQdFDwJtAgJAGaet3O5O3zZ7wlTcV8Vempi_UohEhubZuur1GwVEkA1_TMpsqSsIt_aWDnSpi2gzTibumZ3ZbCyVQxMVzhEY5x11zAfY3UHTfcAp2cDFc05O4RNoN9e8MrfHKyiVWKDrPK_z5t_xWM0ao_86silveRyUOaFC1iE-dy5WtkGTV8P02NAMC3X1mK-sNbLNMI68PGp_B8C0XOfqn_uPTE8Et_cTd8IeXAblY2wXjznssOzOh0OsQMJqZpfTzqfcV2WG-nSt6_Ny7S-KRw4MhLiBDOY5cG4Xe3eDgo-XIyY2V6oBGVLREDWwsfz1qMpv1r4JfyxDvsbd-V_Lp0cEZmxQMiqLRV9bKyGkaNem1k6G4TJ2QaEc_DgHe35fkkHqtuCL54Yaw8vmjBhpqfcDvCLE3qm2tN89dVSQqrmUF7koTYlVfbEDppcRPKcGCzkkCJ4SehMset2yaMIaeinT2AlEfrGauNx5L2e42j_IZEsycENNkUVxUufHHMOjKC-nyXTZItrP3UyzWAaAMhmvIfj7J_BDqAV3k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be9c5de5c5.mp4?token=c_7EnTaFyMi3n8iqdYvBQcHSfxK7s84JTeGODL9szAqyv5DFZrIqK9h6npdOoOXoiDepXXPc-LfNzuoFsDT67N1HNAIOg9THN9apOH9YLbPIaTAKkPlabI0N5_FSLOVjk0wQdFDwJtAgJAGaet3O5O3zZ7wlTcV8Vempi_UohEhubZuur1GwVEkA1_TMpsqSsIt_aWDnSpi2gzTibumZ3ZbCyVQxMVzhEY5x11zAfY3UHTfcAp2cDFc05O4RNoN9e8MrfHKyiVWKDrPK_z5t_xWM0ao_86silveRyUOaFC1iE-dy5WtkGTV8P02NAMC3X1mK-sNbLNMI68PGp_B8C0XOfqn_uPTE8Et_cTd8IeXAblY2wXjznssOzOh0OsQMJqZpfTzqfcV2WG-nSt6_Ny7S-KRw4MhLiBDOY5cG4Xe3eDgo-XIyY2V6oBGVLREDWwsfz1qMpv1r4JfyxDvsbd-V_Lp0cEZmxQMiqLRV9bKyGkaNem1k6G4TJ2QaEc_DgHe35fkkHqtuCL54Yaw8vmjBhpqfcDvCLE3qm2tN89dVSQqrmUF7koTYlVfbEDppcRPKcGCzkkCJ4SehMset2yaMIaeinT2AlEfrGauNx5L2e42j_IZEsycENNkUVxUufHHMOjKC-nyXTZItrP3UyzWAaAMhmvIfj7J_BDqAV3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمود شهریاری چه اجرایی کرد
😂
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101566" target="_blank">📅 16:40 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
