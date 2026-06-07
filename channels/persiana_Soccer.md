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
<img src="https://cdn4.telesco.pe/file/JrsEPndXhLSjgYLqJVYtMPs8BKmyyFw6I7YufMwrAmGr0ltk2v91X0R6QEfJP_UaeGn28zUvMlTG0FUF_mH5St4Y4_fYF5xAISMptj1K59NCaCBeUCYIObIal48mL2bcQGyHXLZ_1sJzera8WgmnXupcWYiHwXsoxntCvG2JyyeAIP4oURvC4rqelfBpsMBacRGGXHbuqFnpFfrbQPSEIKAFhtGdilZ8gAFX-EPz-jQUWrHzICM1lYnfobjsc-6_CW5WvkYHpqLqWU6o7R8VHwUJAIbNOtQUKPSjRdu67mw0tu53ahnVKrK2IO8_APifon-X93ujEtC7H1BBwdGFmw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 172K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 18:19:09</div>
<hr>

<div class="tg-post" id="msg-22943">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHly0IILeiePF_qCHBD4SRbb9Rm3urhHobK0ors47cB9I8QQvBepAliO5wsyqpdUFzNFhltqt32zv1QIgBgV_yKtTpQQ1NwCgTJhOMnDyaqiXGu9X_TkqTpTflW5YhfVvnQzRVWhorzEnwfhMX4MgUnyJ2VLeZg6QX7dZMadjSiU2kR0lpm5zPJQRoRrcJ5ldkuxTOOYKm0lPEpw6KVmykMlI6l9ljLmolS-5l1SifyNnv95zp8KQOD9H9PPWnFgtXJL_eJvZgI2mMagS0bbeAFr79NL5pzjoTE0npFC3GiiciTRK2-VRLH8qeyvqefG25hTwehdCDKPQky0bp4aQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/persiana_Soccer/22943" target="_blank">📅 18:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22942">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ebed3078.mp4?token=sicwJ6XRrYTPdKE3leVthno2oNtLtV64FifYGqduBnaRPq4a9FMjQ2t9OtF0ElI4gq9V1j6oExA518h0NQp9WV1PG5azfxGNRc3GUnF0TFV9I2-8CAQRhj6Qz2iz8i-z8dmlPri-zVIoiruPQG5qao6YD8RwO8uvgO_aMLNGdJVYVXOHAjmjeNqVlJZFZsTZtrM2aQb3KzT1Nbp51TWl0cUEQ-5kFPoMuKdqwe_sDQCPd2ZPP-aqS3iPOUwkO6lAtfYjBTrr0CUDcfOUzUHFKqxVXTH1XLbwqLcjz9BRmY5AYfxFBfIXPxhGG61aSx27eEzm79st77ouGvCQisUghQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ebed3078.mp4?token=sicwJ6XRrYTPdKE3leVthno2oNtLtV64FifYGqduBnaRPq4a9FMjQ2t9OtF0ElI4gq9V1j6oExA518h0NQp9WV1PG5azfxGNRc3GUnF0TFV9I2-8CAQRhj6Qz2iz8i-z8dmlPri-zVIoiruPQG5qao6YD8RwO8uvgO_aMLNGdJVYVXOHAjmjeNqVlJZFZsTZtrM2aQb3KzT1Nbp51TWl0cUEQ-5kFPoMuKdqwe_sDQCPd2ZPP-aqS3iPOUwkO6lAtfYjBTrr0CUDcfOUzUHFKqxVXTH1XLbwqLcjz9BRmY5AYfxFBfIXPxhGG61aSx27eEzm79st77ouGvCQisUghQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظاتی‌از مسابقه‌کاراته‌معلولین؛ این چه حرکتی بود تو زدی آخه؟ چرا از روی‌ویلچره انداختیش پایین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/persiana_Soccer/22942" target="_blank">📅 17:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22941">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-n7wNNqUz2oQks3v0F5Zm0KybnB3haXJNlAHOqHBg1LaHHONGaCgQmcgGXSKpUHCdiA9FzRnAXLUc9fXRRHSEp0r8QPdBgjG-4YIrWsQYaG4XAroy05o3YkiAqvhSyGwQzsy0FfMS2fLWVWyCMCb3w2-ozDSBxu2XA6U24GOIl0MiAsNg8Si-j_we4bpSuyQcILHlSuFCiDb4gRmzlTn-TPPb_oKfBaFwwdrrOs4vAGrHXfrY7YGPQI9o5t2OGTfctK7qlJlwlt18Ak-TYOR7xG1QzZHk2oHCjHPSbbZtMLboyJdxp7Jghm_bGWNCRPsKqAi0djslyPbZrKhp3IWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/persiana_Soccer/22941" target="_blank">📅 17:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22940">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzkX9afF1JyUjP2XblqhnlzKxxp9MMvVj6JCXbqln0RJ-yAuOsgERa44Gmt5_3GOnVzu1Ibxh45nChvzLR_JkDFearF4A5QRlYCQIHYedNSl_IJ3THg1RCwQayo5JL9YeW0FjLdxI7RswAxB2bzY_GYJ_3riLmDUKjp6Xvf0KoHfRwe_CQOSO7sY2Mc11s1EUUN0IyeRac_DwHOt8kWdyxv28qArW1-9Uz2jFZBjVP5DnZlG5QEYfmn5DtYwyK6_4sFTlX7U8d0ZkcAm4YEJ09lF7UXdazMYN5-OHzs6r90L2-_NeZYmoBmsw8cc7IpLUcoBEexaz4TqoFhmnQRE7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ مدیریت باشگاه استقلال به دراگان اسکوچیچ پیشنهادداده‌که تنها دستیاری ایرانی‌اش در فصل آینده سهراب بختیاری‌زاده باشد که درصورتیکه جنگ پیش آمد و اسکوچیچ مجبور به ترک ایران شد بختیاری زاده سکان هدایت تیم رو بر عهده بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/22940" target="_blank">📅 17:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22939">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJpOnoB_70ioQ34EcOzw6XXvOhoGCoG_7ZOe4YmWioh4jMWADJV7jNdvMikhCNsxgXsaYMPayCiqrB7UiIIl4RVV01mPyVUHjAP7zi_lzPtopQPVqq7teAoiIXUw_totezaVqImcUKj-7ARgtTGE5sGfkWLCqpEtdyrU1Xi_qmy937ywJe9FB6CpQFjGk-_QUvlBkBMjSDcc8OvlTxDBd5YuJeQQadWEh3nKcJm5G9tSykuu6fW64N-e3xBLPt5tFQ3gMsOzc1TAulABdh578DNwNILlhab5n6BnSvXHIxa24-1PUzPOaXG6OSJAxEobRM5U_RHGQbEImacCjRjoUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌ های رسانه پرشیانا؛ باشگاه پرسپولیس در تلاشه که مجوز فعالیت افشین پیروانی در لیگ برتر رو از نهادهای ذیربط بگیره و در فصل جدید رقابت‌ها به نیمکت سرخپوشان برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/22939" target="_blank">📅 17:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22938">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOoqj4OYUryczkD-XGCOhBBAt3-iIJYwAG0Kzv4mTiZDu44CyfT9ImW2bVTHGkUfMecrM-fhEPbuABeFNeE7xn6E8aBeNdH300rsqBkREGc-cwGGhZ6s7Tlcimr7ng2zX27zNn8KRDrDpkmrxB0GEGSk0q_rgPDxMMQQpIUzFlZLc24zXJR719OEqaJucLwgWuFIlyKh8U9WBcA-G6j6XVzBibitPzAEhXU4xhiMktWUw-Znqz5hz5N9S-YjkAGaeTB4o1gFc_nu2-DyWTnNACr3BdGETWn2OGxADWE5RVV4cwSSIb_aZTMWZtlsbPXkpsleVvnnxvgkJG3lBYdQyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
تا این لحظه فلورنتینو پرز در شمارش آرا از انریکه ریکلمه جلوتره و به احتمال زیاد امشب او بار دیگر بمدت 4 سال رئیس‌باشگاه رئال مادرید خواهد شد و از مورینیو،کوناته و دامفریس رونمایی خواهد کرد و سپس روز سه شنبه آفر 150 میلیون یورویی خود را برای جذب مایکل اولیسه…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/22938" target="_blank">📅 17:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22937">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca0d90aad.mp4?token=q_9e8d6dLF-tYBAGP9xMgFy8aIjdhF-yB-1cZEOgpFq_q6FOMzoC04Vh8FrIWEQlfwPoPhw2dw6J_koPVXmVhIOxv7HhPpU4e6SjMY8hylIW2umJrYEPvbFyoXOJ8PRtA0e71jbgW4E8rFfOyD-Lg9c6Fukmoj4e96X9sMlRyqcwW4ZxH8TUDEBN7QG11k7FrWeP0hLrQ3FZdjIDT-FhbfqgJhw6M45LcD2S3b5KX8uWZUH_ZKutq3xXsT44Kg61zpGfpfJegOLtznhxhk1IgDU3ypeDDK0m_MQ1W4kHmihH5-8TwKhKEkBGUVAiwn5q6eF1q6L6qpT1ELGYZ60a7buQpaLnH069WTdS3o1OPcm5mGVwoiAGfghO_qN5VQxcJUMIekf-gb1eunHBOhT9E49vJS3UiwuaWCyif5CmDLiaDCgGqWDNTn7iL6srnX1nPVMn238Zze9y98AwxcZJgxd20b4zEPPjqVT-CdP5zhRwUsnsqaQLm6RVBC9pnKAdhlgpu3QDxGkEMwKS0fZN7bIP46xCJerw_YIMX0avNlVmW_7rSYkE_CtB0EVHukOO_2xGwiNOKPvpYTwMCVacTTQWwfskQgIEuH-uk2NipmfFbbn1FWFJoWMaZq0jHBZHMhClOElvWT3jkYt3EclbluY2MjvUeRZ-34RgtXr9u9k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca0d90aad.mp4?token=q_9e8d6dLF-tYBAGP9xMgFy8aIjdhF-yB-1cZEOgpFq_q6FOMzoC04Vh8FrIWEQlfwPoPhw2dw6J_koPVXmVhIOxv7HhPpU4e6SjMY8hylIW2umJrYEPvbFyoXOJ8PRtA0e71jbgW4E8rFfOyD-Lg9c6Fukmoj4e96X9sMlRyqcwW4ZxH8TUDEBN7QG11k7FrWeP0hLrQ3FZdjIDT-FhbfqgJhw6M45LcD2S3b5KX8uWZUH_ZKutq3xXsT44Kg61zpGfpfJegOLtznhxhk1IgDU3ypeDDK0m_MQ1W4kHmihH5-8TwKhKEkBGUVAiwn5q6eF1q6L6qpT1ELGYZ60a7buQpaLnH069WTdS3o1OPcm5mGVwoiAGfghO_qN5VQxcJUMIekf-gb1eunHBOhT9E49vJS3UiwuaWCyif5CmDLiaDCgGqWDNTn7iL6srnX1nPVMn238Zze9y98AwxcZJgxd20b4zEPPjqVT-CdP5zhRwUsnsqaQLm6RVBC9pnKAdhlgpu3QDxGkEMwKS0fZN7bIP46xCJerw_YIMX0avNlVmW_7rSYkE_CtB0EVHukOO_2xGwiNOKPvpYTwMCVacTTQWwfskQgIEuH-uk2NipmfFbbn1FWFJoWMaZq0jHBZHMhClOElvWT3jkYt3EclbluY2MjvUeRZ-34RgtXr9u9k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اجرا چالش فوق العاده سخت ورزشکار روسی توسط یک ورزشکار ایرانی با رکورد زنی روسی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/22937" target="_blank">📅 16:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22936">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6gCaC4-YZtUZhvHU8FQ6AXoDXtYL_TvXcwTHvyMYnilnXHuuuXQhmfGkgNjokOFhcJkBd14ICrlavWg7mZiDz3vJVt2SMmwy-MXlImOcgJBuryZIiBSLBE1EyQkEHFvwuS6BIIbVfuc1L58XeQcZodeG_cx7lrvwSaju8drVhwxCruHjt4lpBEEJUkopBnP-Tr9knSZ7jB403xs8UyyXDS_VSvNVUxYa2Atn64z0HA6pELtA_NPsr5dbM6vRqA1SNBdNn-XOdSIbCPUj8ituD5Ki5o5VdnI2JDXvsIBid7O80V_TEhPrdFkIlF83tXmMcPQfg1uL0nEpF5eqr8cRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/22936" target="_blank">📅 16:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22935">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lax9yhjKNL9vJ_rldEiGHvr5zW8Gq9qoZTiGGwjt0-BqE9KGiVEQIvh5wMpkvYPmjI77wipqWd5lCKHUh9fJsxhpEVfbV9uGgQWU24WmpqF0udAaHM7_NDRNZBQrNAWxXdzRHWWPDnXsycTjhJCMiskVQZ6vq2gwnSRVImDb1DX1GIWTfCWh4moLC7beDzlben6Y4hmakti5qd8yigLXiBKsILU_CHvHjI3oGkapZU-ISbsSDj_dfYUwCA9jE1pCApkwWTV_F3PDOqZMPKqAGzjaDavK3jeO7yjlYzxpHG9DbhiTLx6GDPuJ3k7IlFk8MBWhEtaRTvW1ymSGCaB54g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌انتقالات|گستون‌ایدول‌ خبرنگار آرژانتینی: با جرأت بگم که آلوارز درنهایت از اتلتیکومادرید جدا میشه. مقصد بعدی آلوارز صدرصدر بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/22935" target="_blank">📅 16:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22934">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGb4bf1aCCyq8tuGJ5mvYk5fT2TvU2YIOv3PTNnLs_2-y_Z1atgivEOjM_MWkpPA3HQj-fGN5RgYrq0VXXKIEuFL0rkXHttGTH5pkqyqTQzdmEDVJ4NODfcCZltxY3HqhAHHYBdTu5N_glROUyDovTrL3QoAK5i-sgLTK9gURw6EeMIMGFY-aX1kwPhHHQaR-vybV9arduGsVX4eVwbWG5j-L1r12oU5LElUz0EXKWzMMEMXLtsMYwKyloxJ01OetbKSbKVAuYwDmhQ85x8HM2-90ImFWPJTsye5urEOXgIB9c_BZTmt0mERtma9sVuQVdGkshcXk5ogMXbAqF_FZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
تا این لحظه فلورنتینو پرز در شمارش آرا از انریکه ریکلمه جلوتره و به احتمال زیاد امشب او بار دیگر بمدت 4 سال رئیس‌باشگاه رئال مادرید خواهد شد و از مورینیو،کوناته و دامفریس رونمایی خواهد کرد و سپس روز سه شنبه آفر 150 میلیون یورویی خود را برای جذب مایکل اولیسه…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/22934" target="_blank">📅 16:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22933">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139c25f87f.mp4?token=XkARHvqKBgZkA05ewjraQ5MTp94QtQjnNjc1iI3JMkQ2cHMu-rsr9XOPBdOwisFiInSU_uF0oNoK7QhtyyBlAKOj8w23wLhcwr9jl5Q_eJGE-UwPBMmGBY_2fSouINCnk1WBsf_9DsrNQqFScNvMZ32BbOd8RkO0B9LrV8ZD0NZ_xeWmY2RtdsNH4CRL40BtxQEqZGGnLe2v2DQzzP4gucWqPvWHxwxjU-2sQQnEEzAPYWTqg2uC6VLE-8vphzv7pY2M5gcBy3qgbDc_nl48rMVIe3sXnlGgWZEC1vVezgHIKPGu7nLJRx-_9AGB49lx_BAAf-hIZM-I_jdK6Iz-Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139c25f87f.mp4?token=XkARHvqKBgZkA05ewjraQ5MTp94QtQjnNjc1iI3JMkQ2cHMu-rsr9XOPBdOwisFiInSU_uF0oNoK7QhtyyBlAKOj8w23wLhcwr9jl5Q_eJGE-UwPBMmGBY_2fSouINCnk1WBsf_9DsrNQqFScNvMZ32BbOd8RkO0B9LrV8ZD0NZ_xeWmY2RtdsNH4CRL40BtxQEqZGGnLe2v2DQzzP4gucWqPvWHxwxjU-2sQQnEEzAPYWTqg2uC6VLE-8vphzv7pY2M5gcBy3qgbDc_nl48rMVIe3sXnlGgWZEC1vVezgHIKPGu7nLJRx-_9AGB49lx_BAAf-hIZM-I_jdK6Iz-Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
آدریانا اولیوارس مدل مکزیکیم رو بدنش عکس تک تک بازیکنای جام‌جهانی رو چسبوند و از دخترای مکزیکی دیگم خواست این چالشو انجام بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/22933" target="_blank">📅 15:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22932">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icyxPyIMZLXOhBnszi35S8RatgFTuemTgjKWycB06ecJQF1CE7oE8D2uRfWfpGq8MPhhghIAOGgio9DV2rzWJ6FTB540MMUaqEGO2JEM_tIQof5YYfwZxdNP2LUysVdBz6_uZnKc5gKePympxw9b59Xfgon_4LHOh56rXpAdGv-X71IV_fOUQTaqOjmvtVwwBTe-wXCQThNIdBhoNQwRez4tEuin8y6_QaQM2CxdOdvzLrYsbx1uH-4Ssfn-X3D1cIaZfvGIXh_8Mr-dEsZG8o4G5FUqN0YKxB46OtkhpSA4aUvL_loQA3C-oglqH337dZAmcosOSOLc0HmTTQ_w9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
انتخابات‌ریاست‌باشگاه رئال‌مادرید از دقایقی قبل شروع شده و تاپایان امشب هم مشخص خواهد شد ریاست کهکشانی‌ها به کی خواهد رسید. شانس فلورنتینو پرز بسیار بیشتر از انریکه خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/22932" target="_blank">📅 15:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22931">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cu3cCPiB9biljzNroIHYzHyC89wbuPEBbARpbRLYq0Cm5gWvEqqkZeJgaq7ffeOaeEfH9mNTmxEczRW_zWx0HQs-8YvIYax3pjf5ISUkGWbpQywvM8yIo5k2EwzpKvK_-IllC1THLR9aCGvuHkpsixcGG3wKaQot2TsSSFyygcGDSOm3Xvn6BMz923GtXYWcr1Q4XwVKRkcV7OyIVS9srylj4oVSxs1oIse42mqBP-s-ktKnM5DgoztYdCYE3qhi7bGk9zvuYKT0zvpCjCfELURJ-uo07tt2J4dwGqrzqUmWhQuYgS-JTNpZzTNGzGDVekZMfRt0n1EPY3zTiYYMGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال خطاب به‌تیم‌های خارجی که خواهان به‌خدمت‌گرفتن امیر محمد رزاقی نیا هافبک 19 ساله این باشگاه هستند: 3 میلیون یورو پرداخت کنید رضایت نامه این بازیکن رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/22931" target="_blank">📅 15:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22930">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvhkRFYyRgNlK-o_v4rpmEogdBCaM5gcd_UpFF7oQKzr4yzAQiG2BGm10gp7bc2HdalE6he3RQps4PrRds9vH8yfH0rsux6Sw-H3SO_F3U0s0I7MdKFRAMKQT_9e-GRjW_Dw4jUxa7kVxwA8I35fj0BjhkAREoBPfsJ7zreTrz_j622H3aocOYow6UXGLBsHUi5PV6ZFWCG0vmyq0qXEVGlVCvmjRX3Ci9jAW14xKmdmx2JsG2-Xb6xkjSkYshK8j0XVACLubgK_DCz3h-2Ehslj0TRxqsV7qOp1A7mtXjiagi_9MCd0Pxbd1z6NmQeoBWYGAB0iMkUleN9aBU5u-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
معرفی دو تیم بلژیک و مصر برای رقابت‌های جام جهانی؛ جفت تیم‌ها حریفان تیم قلعه نویین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/22930" target="_blank">📅 14:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22929">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZl1mcDoI_JdnFB42XtXrYojR63BnVD3abjvllFIOeXuNhAFgQunmic6pVr0gK64ccnsf5_4FSr1ydBWXx84W6axrtVLpYdB9LBBH9f09pnwj7d46I3I7voEuSpPNRoG5jeEH81E--R0LoLVI9Z0cVg3XZCgGPwayf9SApwvGJINzcIXbuQltH3arXKpkkGclXCTsuejlzVeWmEL531IAuiopnl7e389Z1o9tLPQ2HGV6KRvG0WBV7pd69s0pyOy9esz8u1yWr-cwHopVPT05upQ78bYa7uhWTZmeMiJZqhv8u7ikLV36-XMa90qn-T4uVisARe8T_e3MQAeixzgXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/22929" target="_blank">📅 14:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22927">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fq1YDIVfOjXgt2_yDpN6M-hVNnKckgY2c4cViBNErqKiXb5aRM9AjPyaiGGHJU-ME-ADEQ7OYm2jpQy1OUCGc1j7MJWliiQjnj_1fhM3IcmEPItjgmvLoisopdWOSaTISVMjFwayNhNJC_zMkFk9DtvwQu7NfalD-Wu0d9x5nL_oHjhhTdGAe7peTw1KPDKShMBsQgPwmUz07zq8GfJk63bSLkzXgP0ziPGZ7m4pTEAWhzHkNibcI_mQJ7GP72I2dqNe8vfhdSfWtFSPgr-d9HHOTX4iDWhKuhwT15MPuk-eXvrEGlcsj2hD71i9fk53ErSnZ-p-1bDQOsrkg1XJtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iGpnqHYCr0dQ_DyiXnVBayshFJ4LuhoXSzR_Jmq5XbtBGnpuNZS7j1bxhDoNQTlHh8KlEqVDEzEmk5eDE88VHmutflqJemHm7Zitez9Yf5WlTFz23jy8UvM32QsqgzHIJcejE0xg_ZFym2zoA8Y9-zeT3_I4KlDCURbGRzU5_8niK2P_uPNcliZ1U9-0TVsJdVuoxVYzi-ndLem9TzXeagOO_5L6VHmX-q7lTWZivqqqJ9eVAN4U1T42QaydtBmaKPWqGWL42XHYROHukcXmf0UdqSGqguyRueCUUCL4LxCh0VpUhP9TYJVjmkmKXIiDo6PkCSRjosidSPTBMa2XOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
معرفی دو تیم بلژیک و مصر برای رقابت‌های جام جهانی؛ جفت تیم‌ها حریفان تیم قلعه نویین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/22927" target="_blank">📅 14:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22926">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZRbNBgpsVD2311F6i1IL-lk3Lj8sYXnf0ZdZnM_1Ox0PBmhYOJ7cecOV46KNXdqTsoNjBkJXdw8y3GXCKk3Q5wNa_j6Ju08XGIyU_pFvmK4Z7qwgYeUm_URcCrzTcs1Xx15hZOZkOlW2xY9MkJ-BUt0lw-De13pVs4LMw40LZR0pegjeDF-dFSTXfEqRvM2rnXZcn7WIh7g-qr3l4sRqI2f52KrLWJrCmNp1y4X3uFf1G_VIVgQl5GopJSXoooJY6HyZ_tweCxB-Uhyx0ItutGmQVPIZsuMdUJS6xVFdMkPWOQgDa_APUAtFqwcdJya1eP-NKcXku2BrX77pI_low.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/22926" target="_blank">📅 13:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22925">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moUtooTgecRiJfSZkBFiXpQEe9gpqP-n619GsI_RbrUGl4ZJuJ66PQ7uZMXBG5XALrjO7RelA1AIN4IDJbu3AKo6ijWnId5RA9o2Ns97yQKTny-huZMcZGf6hEgYg0W2J-lcAcj_vJHFI9wL-UEUdaB4JO5q32zAh4yxAIEuDJRPVETWBzQXZ1Y1ZhHzVUvM5kaWpG85VvO-PfiLJbR1xT8hyWkrW_jRsX1X4MmvsqhMOTGZJNEEaZlSTKzNuM3Wst1wNGg2DC8JhrD4_dyKkLnKOVMfv2p5_8Acxed2WUYd-Vd0FwWqWAGSQ5ruU1e4F0QRmNa_6NEglyAeH7uvhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادی‌کنیم از این ویویو بسیار قدیمی امیر تتلو درباره استقلالی و پرسپولیسی‌بودنش در زمان‌های مختلف
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22925" target="_blank">📅 12:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22924">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYFOij0AgEd0DxBV4rQUdrdAcRzSvtLbM9gaFcBQMcJ5mbeFgMfpmKd0-tXrnARchmxvWoaFoga4dLvyXmELkuaTZBl7GlvhJmS6lhQE2wCvdyBuBtyA9bfBVNG5SIq65mObeqFZzuHR9WHQdob19IFGfdoznqRiKDEgADVb5Jc9q3RFRinpbkh6kYC0kfz0BrHwta2zhGbWKlGSEiwNYgVZsmk7HH5BrMJAltrndrg1vGhRHpGEebupPTkm2OnG2R51T1ZKdhhUYWMOT6I8MRt-F38oF0eqwBKbQzyKt1niIn8Yym4DP4xLcLUmWeszpyxQIdr5ue0SQOcb900LZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ هفت سال پیش در چنین روزی؛
ادن هازاد باعقدقراردادی به‌ارزش بیش از 100 میلیون یورو از چلسی به رئال مادرید پیوست. او در طول 4 فصل حضور در‌این‌تیم 76 بازی انجام داد و تنها تونست که 7 گل بثمربرسونه مابقیش مصدوم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/22924" target="_blank">📅 12:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22923">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a46a056081.mp4?token=JvFX29dfyr3k6eZoNzbbizD2pHcgYcYd9ObKJf6fvHB13GErjG5qDn9Sqq4OuAI9uJUEA1Rbt--SICKN-knnrdtWwgMhDodGpR-vVqnwfZNdU876nZ0Tg_bOoCMa6IzIOH0i5HTbECln6_nEyxurW0S53VZAKg-6h-BCJWHeafM3Ep8rg_QnrPTznprIHv832X4H7hX-Gv_h0QgxMBHl6YUaKVhxGDcKdM-atWTG9U7kqRNrVAdBmlHVe34BDy1aiIB1rt-6khjRGSuES_fVgL36QMidInK9Kf9WdBrGuykFBRIT7JDoDnVAw4nkgR4QIxE6fFlOxW4JZJhbKHYHWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a46a056081.mp4?token=JvFX29dfyr3k6eZoNzbbizD2pHcgYcYd9ObKJf6fvHB13GErjG5qDn9Sqq4OuAI9uJUEA1Rbt--SICKN-knnrdtWwgMhDodGpR-vVqnwfZNdU876nZ0Tg_bOoCMa6IzIOH0i5HTbECln6_nEyxurW0S53VZAKg-6h-BCJWHeafM3Ep8rg_QnrPTznprIHv832X4H7hX-Gv_h0QgxMBHl6YUaKVhxGDcKdM-atWTG9U7kqRNrVAdBmlHVe34BDy1aiIB1rt-6khjRGSuES_fVgL36QMidInK9Kf9WdBrGuykFBRIT7JDoDnVAw4nkgR4QIxE6fFlOxW4JZJhbKHYHWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
وضعیت‌‌آکادمی‌های‌ژاپن؛
قشنگ‌ مشخصه دارند برنامه میریزن که یه روزی قهرمان جام‌جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/22923" target="_blank">📅 12:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22922">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKnxU1o3xGCGkeus0PDmo-Vm-nH9h0ktOfQnd1Wu7ujFzwI1BtMayhq98EAeE382smq_RaiHXnlcyWjfmlX5dBhMT9cN19xhtzglL6ktj5tWc766Zczz846iRA3Gk1KiSd8zHap8qi3rEi05LzMuXnCRQzU_7AFVP_13CQgSQcFDiQzLZpUbmVAEVqBkXBCOLvZe-lJeWDeZ1kBSwPViW30E6qh2zgztLko054Voxliv3fxInDZm6cs6D99i04NpFvelBsB4oyyIoCJwTnXRgLVXyghaqSouGHIMDwwsRIb9UgAq-vkG7gcj2XKz_sYozNT5NzXrouLPWbr47pkwqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ حدادی مدیر عامل باشگاه پرسپولیس هفته آینده جلسه‌ای با مدیربرنامه مارکو باکیچ برگزار خواهد کرد تا تکلیف نهایی موندن یا رفتن این ستاره مونته‌نگرویی مشخص‌شه. باکیچ علاقمند به موندنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22922" target="_blank">📅 11:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22921">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad2a01aafa.mp4?token=n3OgRashE32iQ5Kt0TzVA-6iyCFhjq-z0wbAAUPrgMJH8ID95-YevPfbS6UUmMzWsDc54Nwq6pK2REdzeAoClbEhp6S9JFvOMPoG5Qfw1j8vENjOENjU-d6fGDa8Fe1ns6dtp2m7rSDivnpJYBEY1z3SkMazkd4yB4s4V3rj8-aTVf1T0KS3tspyruSNAR9gQ8-ZAd0SHbhU8BDHxH_ktgNPxrDwMbN1kMZUGdvAX5XzJCF3ptqsH-OF7xUE6_PYdrtEmDTyp23rYzCOlUI0XjualbVtrmHrEPc2zUd9BNLN6lJR95_6olhd5_Evh2bYPOC09wwFaCaTM9ITNSt8NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad2a01aafa.mp4?token=n3OgRashE32iQ5Kt0TzVA-6iyCFhjq-z0wbAAUPrgMJH8ID95-YevPfbS6UUmMzWsDc54Nwq6pK2REdzeAoClbEhp6S9JFvOMPoG5Qfw1j8vENjOENjU-d6fGDa8Fe1ns6dtp2m7rSDivnpJYBEY1z3SkMazkd4yB4s4V3rj8-aTVf1T0KS3tspyruSNAR9gQ8-ZAd0SHbhU8BDHxH_ktgNPxrDwMbN1kMZUGdvAX5XzJCF3ptqsH-OF7xUE6_PYdrtEmDTyp23rYzCOlUI0XjualbVtrmHrEPc2zUd9BNLN6lJR95_6olhd5_Evh2bYPOC09wwFaCaTM9ITNSt8NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیبروین یجوری به تیبو کورتوا پاس میده که انگار هنوز از دستش‌بابت دزدیدن دوست‌دخترش فشاریه و میخواد کاری کنه در تیم ملی سوتی بده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/22921" target="_blank">📅 11:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22920">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22920" target="_blank">📅 11:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22919">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okeDmGPSsnfqlz1TZJHa7O4wjFo_t4dttwoBH1LsumkFzCKGiffhsB76nIyI-FrV57MfqyHkKegCYw9QmQORBlt-b-GzixJbRC_5PtkHVwOTWVaFnEjJMbDBS55UDD6FEsEBQuSIVfYZOaWPqu2MXvmzErCNQ-NtR0bQ2pzBM1gOkEdC7D2h5prblUJ6lh_KOr3S6sHdDX4zLVsiAHnbp4ddDZE7Yd3gTEK800xrsnpCDIImcU91pPZu3LQtg3VrT7WCqu-zFdrF4VEd5ix5IDlxPagQUUK-fjAl8G6npUCfUTBCgUQqYXP0tU3Hh4ka7-Q6NKEM4p4fluZkmtaPMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: با توجه به شناختی که ازفلورنتینو پرز دارم به‌احتمال 99.99 درصد مایکل اولیسه این‌تابستان‌باهرمبلغی‌که شده به رئال مادرید خواهد پیوست. پرز این قول رو به مورینیو داده که با هر قیمتی اولیسه رو به برنابئو خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22919" target="_blank">📅 11:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22918">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t21qgX5LTokgLK3BRgE2cgPt70MYznGmEjk9d37uQ62KhmblNZmdbFyxdA5kyLhM0QFEFZAZqKdS8SMD7yduqxmhj-bvZH7nHvDTyUhtgNrNpi39TrUNhD9Lgg6-O1E6XeY3wN_-Xb2dIUByj045L5pvDt7FlOXqKP_0HrbpF_7Dm3T33bUD0KRuhe6vXLs3MwdPao98UwuaDHRpfAQvI0mUXRqDUS2OS1U2P443gMLrtEK176__cE6UHtLCc9k4hc8Y9GSg1Vbdh-nRq8JikDHQyhDjPlfBFsQymzUbkI4jOOEQucF_fVWH2unV98rIy8qS8cFVhL1SEpjmhNgYBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22918" target="_blank">📅 10:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22917">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d705d6a743.mp4?token=j_Gzgp3T-pK-Hd-aNx_gTryRYWXxA0k8sc50UjzXq8qsQjph0RrKwoSWigw0kQla3heN0Lh0VtjH90yK7XIpJBuNoaARjTIThT5fyU-iKSsjleSqh4TaTfe9TAFe0HdsRPy2w5xm9pttjsxC1tlTMrNELy1vTLu4gK_6MvKaM_IF7Mwao_hjFQAtdpeKTM1LPtJgAsHJ_SFxSKeNunr-YTBM8ETeCZTcoCzw_-0PcIWU6ebSEsqjm1vZQYBa-YGiv0kVE0h4l9YVFG0aZPRM4BEVRsCcE-e6Bt_W0Ez0k5ZIZxBbjebIa-l48JjLfIpodMVLTO8956oNVpPkb4itdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d705d6a743.mp4?token=j_Gzgp3T-pK-Hd-aNx_gTryRYWXxA0k8sc50UjzXq8qsQjph0RrKwoSWigw0kQla3heN0Lh0VtjH90yK7XIpJBuNoaARjTIThT5fyU-iKSsjleSqh4TaTfe9TAFe0HdsRPy2w5xm9pttjsxC1tlTMrNELy1vTLu4gK_6MvKaM_IF7Mwao_hjFQAtdpeKTM1LPtJgAsHJ_SFxSKeNunr-YTBM8ETeCZTcoCzw_-0PcIWU6ebSEsqjm1vZQYBa-YGiv0kVE0h4l9YVFG0aZPRM4BEVRsCcE-e6Bt_W0Ez0k5ZIZxBbjebIa-l48JjLfIpodMVLTO8956oNVpPkb4itdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جایگزین تشویق ایسلندی رونمایی شد، تشویق وایکینگی هوادارای نروژ؛ تو جام‌جهانی اینکارو بکنن ارلینگ هالند جوگیر میشه به هر تیم 5 6 گل میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22917" target="_blank">📅 09:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22916">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0rBoKmDsahUAsx6lmB7bdQCob-TLx_eFd7mgTDlgw2niOHugjpEy9Q9wYsZ8AHKMkW3ogL-umi9C5ETLhGnfWBRG-r7vLRkz0vrgoUlSEQpfZiHvzSo_5i9yp0JyXF4RHIgoTHFCrxmdLvW5rgmR8Z5EXFmLrZFr0GJHXG1CMPAZhqDmc8tEErKg5CHlbqD61FFUZzBvzB2ik4m2v9ltCzaSas-Cp5scyvpEOtYBQEpbrNzDW4HdtCMJ_nHmp7cF3q9mbUqYS_xiBGS51hgXHZPnwRN6q3xEkn---LtTtp20bIlqcNB6BUudYePCyFv0rXE5k0h5oD8GIeNe_1zPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مصاحبه تاریخیی کاکا:
برام مهم نیست که بچه‌ هام بدونن یه زمانی بهترین بازیکن دنیا بودم؛ فقط می‌خوام منو به‌عنوان بهترین پدر دنیا بشناسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22916" target="_blank">📅 09:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22914">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtifistF-Suma4gY48jUyYxHe3YBZLs-BzZqosDKcP-RcmYiDRVWvcAxpbVnrNfC4TdNpfabINQO0Hpzw5-doPASvCBagQf9ckDzwzCgwbJCI4FjnwPIS5Y1LSKeaV9BIwSZj-OVoOMBgp5WA0_GrfPqdjfkhfwnVug88JnoEDli6MN8HhH_kb-rrrmkwV9Zm84lXL4BX6t3wvAr3YCqZSGJyv78ASlwRvzbzoWWkyGzfBUFEcxvv6fMxzKqsfPIvhYAAq2OvuFzWwRVTwihGhFBBlpjBym6y4UIUA0fWG5ycN-66ReUcKGfob9Br5YfrMn7idfyj_aOVetl7eQ4QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارهای‌‌‌امروز؛
تقابل شاگردان کارلتو با مصری‌ها و جدال یاران مسی برابر هندوراس
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22914" target="_blank">📅 01:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22913">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRrktIR7x4WE2S3YS5KliW6K2Pf2e6F-DXuqhvdMcsxP6IsmbjukKTfOghBRHamUi6ArosSbL12R_Y95IUL3dM8JD2DT5IfABJNSbMtb6AJQwm3QMmELfxREyoaBLEAu2TCmdfnnRnT0bEEzS7-bgArO0KrcNdy4ZSfqm-CJ5095QgTLdRx_s8-kJiHCqK8-VAW6Fa_8gL09HctEqKQNvcWKYz0hwGUbq-Xwz8UKM2ueENVXdQwxGLdjoXhf7cj5RF_xJPjQWlmVH5WLckcJ-J0dqpcYNByWb62AKM2UmpkzFrANfsYR4SxnL8aXNLvoutH4wm3gOQ73DKAtzvX-HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌روزگذشته؛
از بردپرگل بلژیکی‌ها مقابل تونس تا برتری تیم ملی پرتغال برابر شیلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22913" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22912">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvLLkO536MxvJoQ7KU1-KR4WS0P02LRidK6-ZYsBtsgBCJhqzJftDuuasfmZFnYate8GFC39tMDkOkTe60w7SwT0iCZvgUizLVue9KWqMKvUy391C3xyLD-9mTqrZeVBYAU6PU_XhrlKbY5aIwTY4X9koGNvWketwRmYd6Dy_2WL9UH1mnmgrYQS6gWkl0ptu8KOrlnGgR1Hqh4PxDinbXnRFg9F3pXM2_7_B6xV-ur_9d748Bn7me6r0JoKr9Wsv043HX8wcztNsNtESJil_ZM7yT1WKRpqfIbr0-mVp9aP43Zser5cAtAQOE7IZyfYpt_CCB0RTleT9cSHwP5Xnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22912" target="_blank">📅 00:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22911">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc9d6ea65a.mp4?token=HmdcgGZgFDqCly93n9t-wZxRJA3BQBfq2r6oPNhR672mDwGC-ABPAFzqXm2vP9P-uVavw1lTlTPptN2-hW5XV4qMMPDddg1J5VHkQk0q4BknoO5hVFsZtMbtN25oZNDoPQ6SRPpCnPLufei68L_iX1iOLLv24luelnk8QgtBHPpu03nHbOvHA714E44wmeGRFPa5RU5_oXUxrVHQydsc648E4a0qnJOIIeF-4fPfwmcoZEqNpZtlVauNJXgSBQ8vjod--OV5X9pnn4IFHynXGvPwYYb4fq6K3rpXX4uHNIwhBPf-P_mBs5kxeBy1qiAQzYBFfPbVQvYE15Ztz9_HAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc9d6ea65a.mp4?token=HmdcgGZgFDqCly93n9t-wZxRJA3BQBfq2r6oPNhR672mDwGC-ABPAFzqXm2vP9P-uVavw1lTlTPptN2-hW5XV4qMMPDddg1J5VHkQk0q4BknoO5hVFsZtMbtN25oZNDoPQ6SRPpCnPLufei68L_iX1iOLLv24luelnk8QgtBHPpu03nHbOvHA714E44wmeGRFPa5RU5_oXUxrVHQydsc648E4a0qnJOIIeF-4fPfwmcoZEqNpZtlVauNJXgSBQ8vjod--OV5X9pnn4IFHynXGvPwYYb4fq6K3rpXX4uHNIwhBPf-P_mBs5kxeBy1qiAQzYBFfPbVQvYE15Ztz9_HAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصدومیت شدید مهاجم صنعت نفت؛ ویدیویی که روزتونو میسازه؛ فقط کامنت‌ها رو بخونید
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22911" target="_blank">📅 00:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22910">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7334e55a73.mp4?token=MJ5146J0BxurMCBThaFCnfx8MLoRcUXMgo9DOhfk_ZGtQcuz7zKHyKtwIukqNDzz_m_EprBSbQ0kZDS-OCpoQNJUrIBF849KuMtYoWeZ--LYoQppgFQoKXMS2S36CYu-waC1ySkskAtcPZI7fhRBXRB7Y4u4cuRKGUf1DFRe0F6ZDlIoWxk-TQPVjpSMQiiHZt3nqsfxXR0SAXCSXvyLvCTnrSk572Ethk9S41zG6gGEZYpwRicesUtGPoRvdM7jHWCkvmBV1s-LbQMVxv8q6F-ynD5Nfe1YV8Mw3B-VgfKC0SsqAMkDJcx8FjYjpOvnFvY9qAFrmdzwYH-7xodFLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7334e55a73.mp4?token=MJ5146J0BxurMCBThaFCnfx8MLoRcUXMgo9DOhfk_ZGtQcuz7zKHyKtwIukqNDzz_m_EprBSbQ0kZDS-OCpoQNJUrIBF849KuMtYoWeZ--LYoQppgFQoKXMS2S36CYu-waC1ySkskAtcPZI7fhRBXRB7Y4u4cuRKGUf1DFRe0F6ZDlIoWxk-TQPVjpSMQiiHZt3nqsfxXR0SAXCSXvyLvCTnrSk572Ethk9S41zG6gGEZYpwRicesUtGPoRvdM7jHWCkvmBV1s-LbQMVxv8q6F-ynD5Nfe1YV8Mw3B-VgfKC0SsqAMkDJcx8FjYjpOvnFvY9qAFrmdzwYH-7xodFLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
امباپه27سالش‌شده؛هالند 25، اولیسه امسال وارد 25 سالگی میشه. اینم لیونل مسیه در 25 سالگی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22910" target="_blank">📅 00:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22907">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c2e44c05.mp4?token=oDCTpYDoJrvPipyPLoYf14I2r4YjKbSyxedtWOfe5-eMfgA3L-jajBhXkFZk4qMzx-JJJj-dovjAnlyp_lMS11iKrOkCK55gW3KSZQgkzSrmPRIewaZ3AFM35LiThBtWgZIz0NBsKLL-7o4OWxV_5IP6ScOVrVbr0OD1ergW-ZWiD2an-fdGHriL-nveMbWf8sUmYvKFiEdHRKHokKbvGtDscA4vaN7NU6Wn1wtw0TWqE7Ky029aio7KiM989gi55HacGb987KnxTr-NOvG_zjm437yU4oPINxi8xQ53p7vZitBaT4ehH5lR1V8OkcAWUjdijJgHhcUTcOgQe3Sw5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c2e44c05.mp4?token=oDCTpYDoJrvPipyPLoYf14I2r4YjKbSyxedtWOfe5-eMfgA3L-jajBhXkFZk4qMzx-JJJj-dovjAnlyp_lMS11iKrOkCK55gW3KSZQgkzSrmPRIewaZ3AFM35LiThBtWgZIz0NBsKLL-7o4OWxV_5IP6ScOVrVbr0OD1ergW-ZWiD2an-fdGHriL-nveMbWf8sUmYvKFiEdHRKHokKbvGtDscA4vaN7NU6Wn1wtw0TWqE7Ky029aio7KiM989gi55HacGb987KnxTr-NOvG_zjm437yU4oPINxi8xQ53p7vZitBaT4ehH5lR1V8OkcAWUjdijJgHhcUTcOgQe3Sw5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وقتی‌داماد مجلس خیلی فوتبالیه، کریس رونالدو فن هست و به‌هیچ‌وجه هم اضطراب اجتماعی نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22907" target="_blank">📅 00:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22906">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762477e8bc.mp4?token=pNkFsbAtCSPYpsk2zRnAcgMgAd9kRxusgvC44WnqOZO0zXlY1pS_HT0lG1DdUcmPtMT5ayCM1tmwmjAr5WfTf79Zj-bGqxpUm3OWljv860WpPVEwxzd94hhHr9oBMoWL70pJ6qfxWKZqzey5L4FGB0G35ZlF05ufzRawl0KmfpNytLCOYGfKtgWCl058WgYipF5DeiVblIT5r395-pk1aQ107hKshwyxyXMTcC_njNSHyqhzNvmKrDCMU6J3j61xztHpeIsZtsHJHk7ViH2DdoXDR6Td56PpTEkPKf4yqRH8BCYeMjEUYhoblrGh3xLMg24tfTZ8KdTas1plrQI1vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762477e8bc.mp4?token=pNkFsbAtCSPYpsk2zRnAcgMgAd9kRxusgvC44WnqOZO0zXlY1pS_HT0lG1DdUcmPtMT5ayCM1tmwmjAr5WfTf79Zj-bGqxpUm3OWljv860WpPVEwxzd94hhHr9oBMoWL70pJ6qfxWKZqzey5L4FGB0G35ZlF05ufzRawl0KmfpNytLCOYGfKtgWCl058WgYipF5DeiVblIT5r395-pk1aQ107hKshwyxyXMTcC_njNSHyqhzNvmKrDCMU6J3j61xztHpeIsZtsHJHk7ViH2DdoXDR6Td56PpTEkPKf4yqRH8BCYeMjEUYhoblrGh3xLMg24tfTZ8KdTas1plrQI1vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ژائو نوس ستاره‌تیم‌ملی‌پرتغال و باشگاه PSG که در 21 سالگی‌فوتبالیست‌حرفه‌ایه، 2 بار قهرمان UCL شده، میلیونره و با دختری که عاشقشه زندگی میکنه؛ برادر در داخل و بیرون زمین زندگی رو کاملا برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22906" target="_blank">📅 23:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22905">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqveG-8xxhnW6hsMDs-V78OyDQkQN9VNq9QHJboaT63gEs41e8nOoGERj-9X1VrhNdGX1iB-jxLnZZgU-hQblMldnQ5PM08E37pBuQFPd5NuWPZXG42mBQ0vmG3j8SGuI5CkwfJv5HwyP_Y6WTA6whbQVx8J540N0WSlsgKFCpiF387aYZPYYQId4Dg6bVU2ZdNB9ZJhKU5KFfKtcIt5wPueLrmmXNOodzz30wJr0qgPGf2ykM4sZOf4Hib2ObRne386tchO2txNS2SWSytKd5ghfj_a4pC5m85xBaRg-1Q9uepOghG9tUdzaOjvOV0vm8BcdK_x1z1Ldwurlk9rZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇪🇸
#تکمیلی؛خوزه‌فلیکس دیاز: مایکل اولیسه از طریق‌نماینده‌اش‌به‌مدیران بایرن مونیخ اعلام کرده که بعداز جام جهانی 2026 تمایلی به ماندن در آلیانز آرنا نداره و قصد داره راهی باشگاه رئال مادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22905" target="_blank">📅 23:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22904">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7O4ED3dK706BpzIKC5oRiik3YNibmNFsiqwCTfpfm5z1fuRmcLhdBdLHBD9cxlzgwqHm-mOU2X8vHL4ZZACgLjbLxbzu3e8_dSGYlf2NWZIDxP3xALUWuJ7picSkqDaFAYAEXtYTyhxSkEJFGUFB254lx0OpPXgYlkzly7xfIS2cV2IIpPntYSFnZsO36F2-pVXG8JbPu6fbo_vrtrrqDhODVPvK7V_z9iL2dUhnCYSULGYYdWUoGZHSsGsUISuw_F_D4_d93js7WYozU6375ZXTL15mDxpbVMxoS4QW2o1VW_xeLISisiwT1KQkCEckducJYIPj_nRNuC7Cxt0Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق گفته رسانه ها؛ یوتیوب بزودی طی روزهای آینده بطورکامل رفع فیلتر خواهد شد و همین الانشم روبعضی اپراتورها مثل مخابرات رفع فیلتر شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22904" target="_blank">📅 22:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22903">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNTFTE-kkveQarPzAUL5fkR6lOzJXHBbWC1N85669ZrWqS-Dt1xDHqp51eDv1mXoO53bJRN0P7ZAVWzkPrsDXFdvdbPOPUSJjqQg0x2MFtVfBZokNYVi0YRd-iEoDnghsQrxTsXR2wD28VZw61jIuH6-OAN2M-Q22LguEvJ-rMSCBefUSomDEA45EgFhFhkWlHnU0Ya1o2NE-PBMjbtrrLKZpShRqNUSjaWKRQSGk45GjZQomXHXqny12qY5aETZTMmmA5307URjjlfhTUfdvPCbVyGJQT0nzy4IzM9vSwHtSCgM7rOnIlj01lOwp2a5mzf7-WlsIubMCxIzxRzftQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌اخباردریافتی‌رسانه پرشیانا
؛ ریکاردو آلوز ستاره پرتغالی سپاهان که با شروع فصل جدید چهار ماه از همراهی طلایی پوشان محروم خواهد بود به مدیران این باشگاه اعلام کرده درصورتی که محرومیت او لغو نشود یا به حالت تعلیقی در نیاید قید حضور در فوتبال ایران رو خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22903" target="_blank">📅 22:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22902">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhsJtp8HlHJ2ayvkDCnPaLqnzk_MHpLPjJNujYbIiRDJPcPpiAQ8yW_HCvDDRSNxgP9MsMXKpZPoygZqNM6KndasVVFSXT01jHY9yeFOGk8DexVZV-LvzGvwXOHv7BOxqkAMK4yYKQwNaXwoU9CYtEFjifjTVcx47zyjyJtqJd3_wGNvzoRTolxwsujrteXVXhz-g9GaAg9yWEJnkhQKfTzAJnVD8s8Jm0XUYxxvqD__hPpsKJK3lb3eJl3LVsg_N_5ALsGZGdr5gD6PR0kDBq1PGKDHtaW1Pj0yHS-fLjSZlWDyB7oelgnUD_-zbC7Hu_K6NmGf640PA84qnUfQ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ پنج مکمل‌ ضروری و مهم برای رفقایی که بدنسازی کارمیکنند. هرچند با این شرایط اسفناک اقتصادی مملکت خریدشون شاید سخت باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22902" target="_blank">📅 21:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22900">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LBfsvKoly6_bLn28_7FiU2WZCEzBKrRzr29k6HoMkNjQDUcrpsM_xG5kMFkCs55BrocHlF-BlGW5MQX4HmJn239q7nNWG82GGvrevsCpYeMz4leZgdZGepXnJhtGAbZUyvzqo9-Qg8B_5y1PuArYukdOEGK-vmzMTg3rHDH9PS09t1G7qpFyDm-KuFITNUJrIvwfnw8Ar8Nv3U3ybTk2RRitXWnWr2juG3M7PSDsdqRkdC975wiHItBEetgY3NaDcn9JyviKLHDpk6ULfpYOwY0qxSauzqVZB0rOiA6EzYK5S6Yr5ekH8caZuOUdLZk8F93_GvtENBZANtfjO9JYww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lZEsIeJEloPKwNLO_KWU6SO24CQrRpcQubf8mdCAVsKnAzsWDLyMqquLUSAdiYVfiKesj57gDmHpiJAXpl5NsQ9_Crjb_sUO-EA3wilrB2gUmJ_qTYgnInoOIyrCBZhZcqcHxZwKK4SI_qpkTJcr6d324ODQVvzXfA_IeEgactHljQBVA09lUq3rU4bicXCYnYWsX9kF79W0LNaUY6zhcQKKTrWXon3pfUa7QCHPu-z70Ykw0yTBTEbdPalx-ykozEWDFQlNyLnPhThLmDDTwmLnzE55pDeuLLfr2IAFmPDGxuwUAfGNminFSjJSf3ha7BPCugSM5sgrxkcE0qNf-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بماند به یادگار
؛ یه ریاضی‌ دان آلمانی به نام Joachim Klement که قهرمان سه جام جهانی اخیر را با مدل خود درست پیش‌ بینی کرده، معتقده قهرمان جام جهانی ۲۰۲۶ هلنده.
مدل او که عواملی مانند تولید ناخالص داخلی، جمعیت، فرهنگ و رتبه‌بندی را در نظر می‌گیرد سناریوی نسبتا جالبی را پیش‌ بینی کرده: تیم ملی برزیل در مرحله یک‌شانزدهم نهایی توسط ژاپن حذف میشه، آرژانتین تنها نماینده آمریکای جنوبی در ¼ نهایی خواهد بود و در آن مرحله مقابل پرتغال‌میخوره و در نهایت‌ فینال بین هلند - پرتغال برگزار شده و تیم ملی هلند نیز قهرمان می‌شود. البته این فقط یک پیش‌بینی آماریه و تضمینی برای رخ دادن قطعی آن وجود ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22900" target="_blank">📅 21:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22899">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNQwLDo0tJn2KH_Ijo5hQyxNuXSapQPlERNfC7F5c0srE3GbFpKy481es7Evl93KmMt6mQCFzmcRBmLJcgV0OeGFrBsdyOQ_OgK8HIbKiCFofHxHlXUNJ2hO-U7jLHa2F3ujxyoxGyQuFIsR03GAeCWHJEtFPWkV7F3lYl-mx1IQ5g0zvACWn_CKEQZDzOOVXL4d-gQYnm5iYp4stKSRrIkQ1N9lujeAA1qMnYR5CX9EG2F2hX9iDitwEhNXrgDpcOeBrV3mW3E7UUWARByzss9nMt3YhdXo3lmGBssSQDJz7NxLbAvEGY0Za6cIagcyGMs9ltuNMe4OIrB39WJCiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22899" target="_blank">📅 21:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22898">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dm_r1pXk962sWolCcUTw0yOORRk4bS_CnoyU6xGPUp0gQ5brs8ICsetXJivv4RoWNZIGp_RfStDBTkuncmPI0Tj3KPi4YHBCle8WJaNdTjIqQUyZZ7Xy5O0yMEIa9mnz8NAcjkSx7c7oqE6FQxv2oyy2Afqnz3BJ8RNq8i1K2l4gJUj-Its6t85IOhhPFzIkeHXr1sExj-1tmMreg0LZQpwYh-lnAazOeEQEc1l4_bpR-GlIorv4TzJtZaQYaxxrRoG09CG2tum9nRsDuJCFJLFKqa1LZzANGwT39O4VExjPmivsJSW2XhYhpZ6ExJoj8TjnjMoRhHU93vmSnZz9JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌استقلال با فروش جوئل کوجو به تیم نفتچی ازبکستان‌موافقت‌کرده و بزودی این انتقال‌ صورت میگیره و کوجو رسما از استقلال‌جدا میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22898" target="_blank">📅 20:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22897">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73008adba.mp4?token=HPpqGv9dfLr8jZEtAEVtpRREXZOfaTlpcpZFOSxc0UZD-y9qj23ITq-pUJht9A7az6j2JadjgawJCQ-JVHDeJZFnbSZAJpasVzWbqUXsxbE_NBxWR9k-xlSGwMb3G8QPnH3fCc2UIkpPI5wRj5P2LLI6_L3XzDTon5yPrZDvRJgV8qQJpTroP-dK5bGs0bZvSlcOm6V9QNsmsSGEmuuuRTZhfuL8IcUHflW_zHBCIBswfN0g6Ms8UaO2A1hGSY7BoLQ2nCUNHB5jjYjG0CHzTbvY4qPKIXEx77r78y-zvhlWCb3n8mm2eIFztppsC8iFNU1lTZWR5oPS-U7xq-l4Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73008adba.mp4?token=HPpqGv9dfLr8jZEtAEVtpRREXZOfaTlpcpZFOSxc0UZD-y9qj23ITq-pUJht9A7az6j2JadjgawJCQ-JVHDeJZFnbSZAJpasVzWbqUXsxbE_NBxWR9k-xlSGwMb3G8QPnH3fCc2UIkpPI5wRj5P2LLI6_L3XzDTon5yPrZDvRJgV8qQJpTroP-dK5bGs0bZvSlcOm6V9QNsmsSGEmuuuRTZhfuL8IcUHflW_zHBCIBswfN0g6Ms8UaO2A1hGSY7BoLQ2nCUNHB5jjYjG0CHzTbvY4qPKIXEx77r78y-zvhlWCb3n8mm2eIFztppsC8iFNU1lTZWR5oPS-U7xq-l4Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبیکه‌مسی شخصیت‌منفی بود؛
آرژانتین ـ هلند؛ یک چهارم نهایی‌جام‌جهانی 2022. درگیری بین بازیکنا به حدی زیاد بود که به نیمکت دو تیم کشیده شده بود و این موضوع باعث‌شد مسی به قدری عصبی‌شه که یه نسخه از خودشو نشون بده که کسی تاحالا ندیده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22897" target="_blank">📅 20:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22895">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOBQ7IFImwswuiMZKWw6SQLoFj2a8hD2TqnCvVZ_VEdF6K3e-iGDwtJYEMevV8DWcJlSeb9bvaxhnFS-Vvps3gwUkvueUaCEIH_EcYtJvJtuW39F7aUiaT9FNjKp8-VM4BNPRv9Y4IAoYuXrU041rRnvQ_aQLQdeDyhoZnxFly6bZSEsesd6JZtogvQZBy1ZHpFW0-tWqlJFTiflr1yxDTikSyft7ivGZ1GCc7_51c2AS6O1I36I67t1-6FjO7NptpfYr6SENI0_YAWjocpVMZ97FGQIzDtnTfQbOFbv1QCqQGmI-EeWOkpkg8n3b5wo6NUbZmpAUK8KlDT1gQMQLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22895" target="_blank">📅 20:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22894">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc1ec4c74.mp4?token=It_y1HfRbkO06J0i4IfZoTBUxDe0S3S9OZtoPuKTSrIzREsnU77MRi7BOiq7tPCpfBaLL_tx53toMqUjuef1weBO1r5TGT1-FI1d_MZrI-YGhpgeqC03JzEDLffSnN59DAjPWEiMmpaf8quiUufsQdlQHhjdOzEgjg3S5Mcl0eu7os7Rj4tOZwTxDA8PfAcjuYwvkd74nxkZHNGvYVDMVfA0pasgZJzSNEzcqVTZCtYfVUYg-mYqFRUoJ5ZUoriOW-FNavUjbUxz7lSdDBMlDBnDBw94A98PqTy-aRNEA2adjFJUd4PU9IozeE--SevTOyJZqo2tK-BIiFDM52SH8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc1ec4c74.mp4?token=It_y1HfRbkO06J0i4IfZoTBUxDe0S3S9OZtoPuKTSrIzREsnU77MRi7BOiq7tPCpfBaLL_tx53toMqUjuef1weBO1r5TGT1-FI1d_MZrI-YGhpgeqC03JzEDLffSnN59DAjPWEiMmpaf8quiUufsQdlQHhjdOzEgjg3S5Mcl0eu7os7Rj4tOZwTxDA8PfAcjuYwvkd74nxkZHNGvYVDMVfA0pasgZJzSNEzcqVTZCtYfVUYg-mYqFRUoJ5ZUoriOW-FNavUjbUxz7lSdDBMlDBnDBw94A98PqTy-aRNEA2adjFJUd4PU9IozeE--SevTOyJZqo2tK-BIiFDM52SH8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇨🇴
وقتی بازی‌های باشگاهی تموم شده و از بازی در کنار هری کین میرسی به بازی در کنار این:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22894" target="_blank">📅 20:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22893">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZn8I9yTAuKXWI-l0YUXfAus01I95Wh84w49JhZnVBSEcct8WFnI2qQjlMtmpspoACCaaSgmW6xFHW0zZjiBwSjTy9nlzyThYEB8IEXvuuuBw0bCUGtjYPlQv_-Exo4-cFz2LcSttg2GmqNsk31kqZLd9hISI1kfnA3pP2dip0lQJu8PVk9khN6YoasLfZjHId9BcNFRC-6CkZlx4f93OZAjRvhdGq2YTz9zsFUWoan_TT77IyCyTibL9uhvTm17OekwaPIiWEXbhsQJdsk3LvyR9P8jhH0rBjVq7l0WZWqWm1dPVRi99Z3FIHMORDmvXGJD_5kFjwMU2XXmU_JLXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: با توجه به شناختی که ازفلورنتینو پرز دارم به‌احتمال 99.99 درصد مایکل اولیسه این‌تابستان‌باهرمبلغی‌که شده به رئال مادرید خواهد پیوست. پرز این قول رو به مورینیو داده که با هر قیمتی اولیسه رو به برنابئو خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22893" target="_blank">📅 19:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22892">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_NZcihzRjAdH9a8ZZOcWJIZ9o6ZB2CvfrYdw_hAmxT7pOwaQI852u2mhCGNUxXzGNuS7qfloS-OrI43964frZ7LDyy8ooOM48et3Xu7z1pN3AHPNwSLJmSoVerD0baKrDA6KpYFT7MyI4bkVoAyfhzbhD8wMlGUJxfVqvzRokgVe_BbYz0V7gSg3FypsISgvNpIaP5hIRjZK0JVh2M7eE59NmMLEwHh-jJb74fGG-wNVkG63QtP5y4jK7n0GQmb3dsjbENHwr39yiZbWFHvwwFmd8JjAb9dWFCgdb05lsVwzsJFNq3fchCtop_UkoLOV0PWmLzpb7r6gXs2rzM1Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
در تازه ترین رده بندی فیفا و آخرین رنکینگ اعلامی قبل‌ازجام‌جهانی 2026؛ شاگردان قلعه نویی با یک پله صعود در رنکینگ فیفا در جایگاه دوم آسیا و بیستم جهان قرار گرفت. ژاپن بام آسیا ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22892" target="_blank">📅 19:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22891">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf50298d76.mp4?token=aQNtd36uME4sfOYIiO2o39F2-hMAjTvOdxnXvoAksW3tjBOg6VTqUOB3xXAVzBD-V8H7dXQ9Hb4B8D3k2anhmOJrsoFX3V1Rd1BJP8Gop3_2Rb2tJ1w9FU0ORrB9UbtEFo8txwOXQK8hbTHjGDLyajZRHOshkZXPojOQSbt1bCqCAq6HI05lfXWOlPlAX9NxHuG4FrFXFob67Gha2pKaLrkokQYln49nmh-nVYRqaePAL7TrQQuqCfbR6dcgv0i9N_ax0LVb_20DKbTEk5WfR9qt_ZGsLZLj7QVxf1-uM4T1qOA5BEv4JoGMqL55RHkuk2i7hMkSzGO7RV2jpg181akcGZsrN_123pQKfx8h2eOXeXeqEhnVHMgVGQcINYcCsdNM21ytcTSqjq9ba7ty_zUX42d-5ZNuRhJTKB_FFuO8G_JOddvUGk2jW-m0VPe9s7VAGVgj50T446Ya9wyGQL37m_efpnick-TUqivVe1KOaM1pKLMT8Svr5cuo2zoUCwD3IMymOTJhL-X--AhfS3Hsuy9_H9MdL5Vo0ixTJL9aMm6Z5WvvN21-wrWcaZ4ukZ0J57nNPyFwTNb0CCwpR20Ndf03FDEsYsblQibwzkPO9aN3R7Rt4e98eh3y4wU41Bc_ShiL6D-huhWZhqmofpIJ-M1jjoCHbfsG9lBi9V4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf50298d76.mp4?token=aQNtd36uME4sfOYIiO2o39F2-hMAjTvOdxnXvoAksW3tjBOg6VTqUOB3xXAVzBD-V8H7dXQ9Hb4B8D3k2anhmOJrsoFX3V1Rd1BJP8Gop3_2Rb2tJ1w9FU0ORrB9UbtEFo8txwOXQK8hbTHjGDLyajZRHOshkZXPojOQSbt1bCqCAq6HI05lfXWOlPlAX9NxHuG4FrFXFob67Gha2pKaLrkokQYln49nmh-nVYRqaePAL7TrQQuqCfbR6dcgv0i9N_ax0LVb_20DKbTEk5WfR9qt_ZGsLZLj7QVxf1-uM4T1qOA5BEv4JoGMqL55RHkuk2i7hMkSzGO7RV2jpg181akcGZsrN_123pQKfx8h2eOXeXeqEhnVHMgVGQcINYcCsdNM21ytcTSqjq9ba7ty_zUX42d-5ZNuRhJTKB_FFuO8G_JOddvUGk2jW-m0VPe9s7VAGVgj50T446Ya9wyGQL37m_efpnick-TUqivVe1KOaM1pKLMT8Svr5cuo2zoUCwD3IMymOTJhL-X--AhfS3Hsuy9_H9MdL5Vo0ixTJL9aMm6Z5WvvN21-wrWcaZ4ukZ0J57nNPyFwTNb0CCwpR20Ndf03FDEsYsblQibwzkPO9aN3R7Rt4e98eh3y4wU41Bc_ShiL6D-huhWZhqmofpIJ-M1jjoCHbfsG9lBi9V4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شنیده‌های‌پرشیانا
؛ایجنت‌مطرح فوتبال ایران که ارتباط‌خوبی باستاره‌های‌خارجی‌داره؛ بار دیگر ارتباط خود را با خامس رودریگز ستاره 34 ساله سابق رئال مادرید و بایرن مونیخ برقرار کرده تا درصورت تمایل او رو برای فصل آینده به لیگ برتر ایران بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22891" target="_blank">📅 19:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22890">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06fdcd2c12.mp4?token=rWvSUEC-gfbfRM8_m8YGhotY8IspBhmpW68DT0j6Q2KIBMZFonDj2DdI7ivlz-BpdzwDI_4zUn5KrcgyaRFF0YOxncF2R0N2A0rfpPtD6JuSCb06mrRz3CvGQXwaAenlu0JwO1wiQOQLWMi83TlFAwsxPdGsEWO1ZeI7xrMa_YKYcmcs8zBP6zet0qDjKKSpI39O2BoBDD-i0D0V-hYJz7AcI0PMF7VfkCArhNXOkffE9KZEudCsHSdSuBPF_q1qs2t4RWV9Ey81Nw7b0mgIp9LuPNU3_2n36a2pYKKo131QlLC5XAxPLQhG8lSU51ynSYs5V7gchClK5modBv_qFk6r5puBppULeX3Aqq1DchV6c6ebmVsgyZA22FXni2kB17wk4kBy6V5UiR90DD4y1XlTO5cUBiE6s9bX9kUEC-KSoDy7q1E32ADNmKiAMz2LUP7CrUrDQhJ2g7_D3D3BaX7WXeh_f5fmfyGm2FdPnoR2maZl-pHDp1-TeHcrMU7x5jDNXmHHmFCDpm9TtxSQfpzBqIx7rwXoOfwaGL-kd8YBcrz-WOjYuehgrFN1xaP-vuRBNcyoUc74BrITiOhLAGkAJEO_R59efjESEJPiH4qTrQGryzKNnPPyRRMpK9FxbVl4T7TIieDBl4-fNUWVte4d5z947eXYRxwMRIRAct4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06fdcd2c12.mp4?token=rWvSUEC-gfbfRM8_m8YGhotY8IspBhmpW68DT0j6Q2KIBMZFonDj2DdI7ivlz-BpdzwDI_4zUn5KrcgyaRFF0YOxncF2R0N2A0rfpPtD6JuSCb06mrRz3CvGQXwaAenlu0JwO1wiQOQLWMi83TlFAwsxPdGsEWO1ZeI7xrMa_YKYcmcs8zBP6zet0qDjKKSpI39O2BoBDD-i0D0V-hYJz7AcI0PMF7VfkCArhNXOkffE9KZEudCsHSdSuBPF_q1qs2t4RWV9Ey81Nw7b0mgIp9LuPNU3_2n36a2pYKKo131QlLC5XAxPLQhG8lSU51ynSYs5V7gchClK5modBv_qFk6r5puBppULeX3Aqq1DchV6c6ebmVsgyZA22FXni2kB17wk4kBy6V5UiR90DD4y1XlTO5cUBiE6s9bX9kUEC-KSoDy7q1E32ADNmKiAMz2LUP7CrUrDQhJ2g7_D3D3BaX7WXeh_f5fmfyGm2FdPnoR2maZl-pHDp1-TeHcrMU7x5jDNXmHHmFCDpm9TtxSQfpzBqIx7rwXoOfwaGL-kd8YBcrz-WOjYuehgrFN1xaP-vuRBNcyoUc74BrITiOhLAGkAJEO_R59efjESEJPiH4qTrQGryzKNnPPyRRMpK9FxbVl4T7TIieDBl4-fNUWVte4d5z947eXYRxwMRIRAct4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
5 سوپرگل دیدنی‌از روی ضربات ایستگاهی؛
از بین این پنج تا کدومش رو بیشتر دوس داشتی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22890" target="_blank">📅 18:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22889">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWHnOLi99ZPVEt9JnxVZD9aSZf8NG8jwCB6p4lqix7uyXRq1IibzFmx21QZ76qBpZhxmJHNZGYSfGLVWMR1Q8PWneblZCvZHYKR0yup2n3Lo8NRkf5_xQeZStKi4Wn1i-Yjs5SMUELrJmmseXCk3eLFWgnJrRN4nSE16UEeHc68zL4kLnV7oU1CO6fQ1E_s0mFWLYoN6FAwv4pJTZWOVXwEj7aLN76p3DK8CkH3uXT7CaKCqPBxnScZ2sIxeLuqJ05U2x9yeViXqjVLc3fRC4W5h4O18lXG1m0V2F9O8RCNkaZICl_63bjPpUAIsYM5TMxrsLcWF6ISqr2ySC2b7yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
در تازه ترین رده بندی فیفا و آخرین رنکینگ اعلامی قبل‌ازجام‌جهانی 2026؛ شاگردان قلعه نویی با یک پله صعود در رنکینگ فیفا در جایگاه دوم آسیا و بیستم جهان قرار گرفت. ژاپن بام آسیا ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22889" target="_blank">📅 18:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22888">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb97f5a2f.mp4?token=pgpqlPYYYGRnkYFR6mIyjMu9bUXtaEuZ7mzxpNGpOlu5aeUuNfa2sTBHfAp_wf0CHQFdidJmES6pWoCN-CYq2UHgZviuMs4OWr8nZiLxJh7RjuVR8lHvuAqYrefuCfNyYgrUSOF9R6MMPudZ4zA2098MSoD3dsfmKAyLbY76w0G70103zpNH4NpozXNaV3tcLWOcjE9lHSUitBANyFR0GdcElZYUOpvy3h3A9OfJbJMDv9py-7zgowrGUZRyAjV2tvRlhPX9tkLfo8LqDSXEnq31aetTWwQGkO9fbRqsK6HtSTQbyOboqHJIJMFkYwYEc4AhzM3oK2um972K7hjiTTzBqnixPLb_m5n4M7NgRFKZ6pH_CXk3iDf5zUtsXvXAan0OBRFZHF0dm0kYZLjoPRG8qPqEE4bJk7b8J6pZ0lwgW9r7jjShKnDIQ7KJY5FafFS9z60qVth728elc3URQa5HqXYLy7KYzmLp8dPkd_iof_UrDPpuJO48sJefyg5k-W6t9smmvdnLYSlfP7Vd_lmJBobA2XgjBS2v-T574ZxjW-7LR4BJ34sg4Z0yqLKaL5nA8-opYkHQlwJxNVAvgLmEx1Az33dGJSFifcYKg24yWGmiAmFI-mfdMxLmJd9iEg88aMlCcglaoB1JEkE7EsHytpB-mZoTUebatWYPfE8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb97f5a2f.mp4?token=pgpqlPYYYGRnkYFR6mIyjMu9bUXtaEuZ7mzxpNGpOlu5aeUuNfa2sTBHfAp_wf0CHQFdidJmES6pWoCN-CYq2UHgZviuMs4OWr8nZiLxJh7RjuVR8lHvuAqYrefuCfNyYgrUSOF9R6MMPudZ4zA2098MSoD3dsfmKAyLbY76w0G70103zpNH4NpozXNaV3tcLWOcjE9lHSUitBANyFR0GdcElZYUOpvy3h3A9OfJbJMDv9py-7zgowrGUZRyAjV2tvRlhPX9tkLfo8LqDSXEnq31aetTWwQGkO9fbRqsK6HtSTQbyOboqHJIJMFkYwYEc4AhzM3oK2um972K7hjiTTzBqnixPLb_m5n4M7NgRFKZ6pH_CXk3iDf5zUtsXvXAan0OBRFZHF0dm0kYZLjoPRG8qPqEE4bJk7b8J6pZ0lwgW9r7jjShKnDIQ7KJY5FafFS9z60qVth728elc3URQa5HqXYLy7KYzmLp8dPkd_iof_UrDPpuJO48sJefyg5k-W6t9smmvdnLYSlfP7Vd_lmJBobA2XgjBS2v-T574ZxjW-7LR4BJ34sg4Z0yqLKaL5nA8-opYkHQlwJxNVAvgLmEx1Az33dGJSFifcYKg24yWGmiAmFI-mfdMxLmJd9iEg88aMlCcglaoB1JEkE7EsHytpB-mZoTUebatWYPfE8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
انریکه بال؛
سبک بازی فوق‌العاده و تماشایی تیم پاری سن ژرمن که ۲ ساله هیچ رقیبی نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22888" target="_blank">📅 18:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22887">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQQiylQvl7aTHbuB0CKiytEVG6p4Tlz2sap3WVhVKMw91YWz9BavZwcwX3nmmcSrfKNiNsslXCXGhhe4sYLKMPoDxYWYyaXbnvi9AIlmryM6jyojr0-jDyMjnekmc1klqmr3jqBn9jtlz2BGLhtn1AGWZZgSY7FJ5NLpEke24TNj21KtRRpjK6gjBAG7x9938FalPEbKj1RVQG1WD6A2oSNJENUq4OXC9C0pChfqXONRg34XoT8sLwaanucSAGu1wDG6LZBxySg-LBqkFb9btFewoZO_SKlNaPVMT5TKrZvAahb1DqivbqM2pbPyQbC3jKAaAXL80p5IRcUnyghiyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌ بندی لیگ برتر بعد از سه هیچ شدن بازی گل گهر - چادرملو بسودشاگردان مهدی تارتار؛ پرسپولیسِ اوسمار ویرا برتبه پنجم راه پیدا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22887" target="_blank">📅 16:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22886">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efa86e852f.mp4?token=couni3_i9qN0T7yhUgK3g2JehuqYLkLEHOyWHR4NfZ2xpAil3QTmuneSmFZdhu0Y4yONJP9JBnlivyoX-szZpixoWfF3ZIUuVyPwFDXXOs8TeAY1oReopQJiKluVU8L3tThmiZMiRHIGKGFQPUMfQ8BL56_wVIEZHYHRHVR_MV9P87FH45K8M_x0kvRmVXpC6nQUcnD8pAHeqiDCzapDO_rBqMDVralNr58mkTjgfIfD_sSl_hZ2MKKwCjU1Rag_3JD8kct-dItbY2rPAcqgCUmWU86GtGFNEmo1Vxu879WDTYb4EUyRPI6tntf2jwEtEv593swhHqGHuBDHvuCgPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efa86e852f.mp4?token=couni3_i9qN0T7yhUgK3g2JehuqYLkLEHOyWHR4NfZ2xpAil3QTmuneSmFZdhu0Y4yONJP9JBnlivyoX-szZpixoWfF3ZIUuVyPwFDXXOs8TeAY1oReopQJiKluVU8L3tThmiZMiRHIGKGFQPUMfQ8BL56_wVIEZHYHRHVR_MV9P87FH45K8M_x0kvRmVXpC6nQUcnD8pAHeqiDCzapDO_rBqMDVralNr58mkTjgfIfD_sSl_hZ2MKKwCjU1Rag_3JD8kct-dItbY2rPAcqgCUmWU86GtGFNEmo1Vxu879WDTYb4EUyRPI6tntf2jwEtEv593swhHqGHuBDHvuCgPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرد‌هاوقتی‌میبازن
🆚
وقتی‌میبرن؛ لبخند برای پنهان کردن درد و اشک برای رها شدن از سال‌ها جنگیدن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22886" target="_blank">📅 16:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22884">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u70Qd-usbsjNo_Hfsrl0MTt12Sm2b8C8TbyRX5ApjM7MRnEzZX6tFVAK9Ilw_yBvxBCNyP4ad9IE84qmijSHGb2bN-X7MvatgoUZdCz0-5m4IzcqRsojii2cd_-jzHOTszpKtVjAC7h03BcYv93bD6FKdf0adc-qc_ea_ePENkNi1lhX4OkxJoxDZyFxM4sjA9J4TKHwEZKq8SmDk_LEGHGKYSF5SOW83W4PwLi_nkwFbGvPqi0S3nNBdDcOIWPJApK6a9-KS07-Q8x8kD5GDV6taiMqLznTDc5evqkkH6yF7NBfAHLDgCyCjqwxYfkB_BMIK_r9u33pU_VhEq4cmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FDNB4M1cbdq65D57DNSKXkhubEMMR51D35MjrnSvpe3ouHgYqKDrr1YNSWHnxc603v1GtsClf4YlSgRIICJ0QZhz22OVAMOpVzha28Xu7PTa719jEf8wJCDyBJXTrMqltVlZnKFXgMWQqpzEJ9tUEY0bkWmBZRnGVhAGTQbHaF7EludJWocdbq-ght9207gC0NK7mUMWzvvf25AhfXNMej3gKvRQwbNqK65137a7n6RYn4RbNmVF5XFZK5Z2Tnbq7y7m5c9tLkHu-GYSoksnDLYtTCrewdPfNXgTbbp0mex6QsIRLOXA-Ikbp_1E7iYAY7WWgme_Cm1D3whcbd6bhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🟡
🔴
#نقل‌انتقالات
|شنیده‌ میشود آتوسا یوسفی خواهر آریا یوسفی ستاره‌بانوان سپاهان مدنظر تیم بانوان‌پرسپولیس قرارگرفته. آریا هم مدنظر تیم آقایون پرسپولیس قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22884" target="_blank">📅 16:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22883">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZst_fvd3_7zK7nIEfaKqAjQBIAE4KdSk6pwNktHQvCXB_dy95_ps-p33z7JIxfaYf2uAHr8-ACZxxTlSL4JS70NqpyuQYjbnX-L8Rmar_tA9a0CYxQHoxdqYmUE6uFJrmRbW5KTsGVIC6trQU2F2blCIhbf27TqBnDVVuJGetaGLbVMjURH2XFJ34xRneCZsEUBAiai9wa8sw3tkNssQ4k-vGuBzQLgCqkfSinXEaDYx9_nGP7buLLBKT7tA6nN9VkdYXP-pK7_2dZqzgKYOUiEOhcu9JEwwHKhamop7jFQ7de9cqyMiNYNoo9n6EvUNilWALAg7lKJOZt13cwU0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
#تکمیلی؛دولت‌آمریکا: به افرادی‌که حضورشون درجام جهانی ضروری‌بود ویزا دادیم. دلیلی نداره به تروریست های جمهوری اسلامی هم برای حضور در جام جهانی ویزا بدهیم. ما هرگز اجازه نخواهیم داد پای همچین افرادی به خاک آمریکا باز شود.
‼️
مهدی‌تاج:اصلا درخواست ویزا ندادم…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22883" target="_blank">📅 16:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22882">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uau4_XtyLpsg9qxtyytnTNjMl_V2tV_fbRmqrDeJqcbY1qd6hZe6C4Oipej-q3bEocOcMnk1hKqh74K7akSqAqNaiEEZdjgx33r0dBf0ByvUa1vvVF58Rmbcsux3AL2d0V0veOK4dhFk9mb-NODkbGscnKN9GGQhJJOfn8g4NkpstaX3eM5cKZasYICDYwicNPXUzYIBz-VEJhQ5KLp6ZfS3UCMaCNIEDSyuVL0PZB4XAFEvItjAODAGkgCsE35XMXAzYWeWGhag47orOHo6xOsijvamta2OXgTKhTIgyFXLRpm0J0_Bekz90tlOnGlnlvEbrsVm8_lNkFtPH9TqcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ باشگاه روبین‌کازان‌روسیه به مدیر برنامه‌های کسری طاهری اعلام کرده هر باشگاهی که کسری طاهری رومیخواهد باید مبلغ یک میلیون دلار بعنوان رضایت‌ نامه به‌ باشگاه ما پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22882" target="_blank">📅 16:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22881">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VV-aGTfkUXr0OswtOfLf46NyAE6nKe2Nb26csXZKD7LqCwSxcOp3MBuPfuw-clCXIWJ3Xf--iFVJgNnnvSRrWm8WLf3MyG1HtEz71kKrUjHql5IjEEh3InTWAcKhByQny_qmEHd8siWLo5kdhvKpZ_KM0mCd5PVGqpMaFKCmppQdp6P3pNxGdvPxHrI5ktWXn6Zlfuju6XhvicSWFbIAh-dR6vAopA_Y5fYFBGCoEymFeXZIvpQp_dokhsTFhMus-cbXyd03XxR93RJg-SCqS5QDIcW-TzgyJfRUAPEmo3r4uZbKbh6MbfHc1qZPrgw8N2Gcv6terdS0G7lalnK_uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/22881" target="_blank">📅 14:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22879">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k-pxo27FcvWK0fz9hkfbLbOgiKIgiUeivPTibUxg3KWBR1ppgHW095tDs8w_X78Osh9gwegQ5ycgv2qKIY1qBbYkWvA-nFWlw6ZtJGTO2Lw1IJYvc_SEV-FlS6COXSnAS4wCdRS5pNcRQrjHElc2TZxGQ4tRVOM3l-goybJhrOJ4GYrg1nuqOzaUTV3rLI4f4iCmb6nGGazlaJjQU81KYRYckR5cRZEZ__Q0nhl1HGLd6a2WNeKHREc0cq-6xX5Jah2-dPX_7HiE0dw5mMxbQLgq-hCNsrSFZmlO8XLrm4LCuEN_u5HVVot7_fVtNM8JqqeP9VLEVkZkOzuqyD0uHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ga17V4ZVAryoXuQtK5_pg1kY9ITNpLMHmfmj8sXo9ipLb4Q4V1Wwx3sU0fPKBuSnpAfTT6T-WWHwJ0CpPHlmrS84-snlrDsDw5QJlDsaGYwTx7QT8zu7p3OSSjVL3wUaQNnlzEYptZgTAD0jDLoGFyWCTQxJZE_tNAw0Krz0okDAuUce9tHNMq9NDvqk6h3AXMN9ZWyvRa_YyuzRlXtoegB_3aGoKuuJill6SWn6XWXCWf_dmaa0ADSjLreO8ljkkH3KxouwWE1GOwPuEE2z5LOGYS_adoFjc8Xx8GK7ldEMnldAhTUZmOcfv8wtWREA1qktnyjP9ShnKZbjtA1Hsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
خط حمله هشت تیم مدعی اصلی قهرمانی در رقبت‌های جام جهانی 2026 آمریکا
😍
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22879" target="_blank">📅 14:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22878">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dU0_tscYcorHiRiYqka4_r5fhfGJ9ORb7G6r41nR875gL8loar1qGBQILlprn7KcAaU0cFQa2vJnSmdSV53mYbYtV9AhCsXCAvOZPxpx_nPGSgXrsoR7gB51G9BhHsY91MOcLIh4z_seaKwMDKtjc39DdXZL5PD1VRfvpRBqFiKvNJCJq9Tjf0Inc9CVddlOih-FbsRcvo41EFlS2m-Yba9Hr9kIxKnffwXmpbFc2j70qPNUjO3WV9muXnOi4nBg2ZuMbShkBZTcfiSwfJX9pOjPyVVtKKv1IAM7ukwVmM3maEjexGEqQRbFLwbLk5APdJbUUdpPLgEbwkEm76uphw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22878" target="_blank">📅 14:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22876">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLIhOil8j9FLAPvr32VUv7N1yY_-5C7LU-0TvX7NQbK_jq-bulkIOQRHdiV-bVRVqtxJOsSZ0Hz7GskvOWnSwGgq1OwRwG1AWk-EtQtos3ewQa5BoCe3WA76z_818C5nRdO-yBwTgEAINu6nKdOkyHgIZWuKmzMVcOzAo_SRZrwzSz5goiI1C5lbxcg3O2nJIXq2LUv7nBBikOkxVDt-pPGrmKYrE8e1ynBzsyub4b6D2wY9ja5ie46PvdRsVVZH3Uyk3m19tJuq3KADIyROxdJ-ofEH4UuxMYRqBrlX5fJtT0SNlo81RfBE7txbvDWJ6incq1Y6w71LqKcedbqslQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال با مدیر برنامه‌های موسی جنپو برای فسخ توافقی‌ قرارداد این بازیکن‌به‌توافق کامل رسید‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22876" target="_blank">📅 13:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22875">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=AuOL2UbF0OP7j5_fzzeqL7WjcBMZxxKPCGFlgiacxvkIfLGVaYQ1r1ItU1G1nF_XKAxNROApEE0kw92GcEeqqbvIQy8DD7H3rP-RInqJI4ayT_uVmy6y8CRaBdXvHCW7wBRW_0EGDY46MzHQ5aXkgz9I8rzlvkS_jQLyQKmZPqw6TI1-Fn7G4zPbS1zV8kjOrYP3Npu83kyn0UBtmonWCUr_fptcFWlmgkzIiQVCGSqQZw4uAqgKKIxQ48dwAEa-TFeds5OPHWMq0DFG67ZWpdr7kexwRf_Lkk1BrlEpatTHIGXn0naCwxXuFvLoyshuW_EL8FqKIoYctD3dBeoo9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=AuOL2UbF0OP7j5_fzzeqL7WjcBMZxxKPCGFlgiacxvkIfLGVaYQ1r1ItU1G1nF_XKAxNROApEE0kw92GcEeqqbvIQy8DD7H3rP-RInqJI4ayT_uVmy6y8CRaBdXvHCW7wBRW_0EGDY46MzHQ5aXkgz9I8rzlvkS_jQLyQKmZPqw6TI1-Fn7G4zPbS1zV8kjOrYP3Npu83kyn0UBtmonWCUr_fptcFWlmgkzIiQVCGSqQZw4uAqgKKIxQ48dwAEa-TFeds5OPHWMq0DFG67ZWpdr7kexwRf_Lkk1BrlEpatTHIGXn0naCwxXuFvLoyshuW_EL8FqKIoYctD3dBeoo9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22875" target="_blank">📅 13:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22874">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYawLOpzyHWL-f27sJAQWFV0Cp9uLGVIPPiBgKFQqIIhkssbRzFGgmBYXVd0tvjwuxWWANvg9RXPHVISbqtGHstq4p88iSBjA5WLa1zv-QfOl5p6JaiSzv7WEQSCXoqsJkRMFstzxD8LxjzI8RODgSzZKdMkhGMiViMLbQyehYxIIpeDT99OKEJvTZugP0WWYmFlGuVeOtWiIakBUhFyLAaOvdLV_E-a7kQ6p7h4k3YPXV5yfOl5qN-ibPPN3wBWLgX5Gb_bcoYR0NiURIeJR0Rcfos5ZXNVbYl3txrkbBfPRdArC4RRpOuBFfG6qKFId5oixc9vj4YysZaiMj5i8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/22874" target="_blank">📅 12:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22873">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxjXxWnaGkwSKvukRltKxVuTXvEN2I0h_3lgcpQkx6nwsH4djh081EF4iZjxYldOESzvrOb45zHA6lhgati82478Xmzlsty9JsqL0Ncknj1VCrQtO6XWgt115QWiof6I4f5VJ70Y3uWsWoM7H41COOcCEjhjU-aUOQeD7IqrZzAPE1mlwkARcT8Up466INKcorI9XRM6gE8MkoeGnVRYBcmfWa1xfSnilBpQkfVLqLNBVKPw3rCrrp1mAmhsSTPuBcmlB2WTHnhJVVn7dnLCE6bSdlANJyTK5f7N32Ufg_kxUNo6ySp7mcdr_CRLp5fH-OmfIQO51yB6s8JEl_KIQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟢
#تکمیلی؛باشگاه‌آلومینیوم‌اراک: در روزهای اخیر مذاکرات مثبتی با یکی از اعضای هیات مدیره باشگاه استقلال برای فروش محمد خلیفه و بهرام گودرزی دو ستاره جوان خود به آبی پوشان به توافق کامل رسیدیم و به احتمال فراوان این انتقال بزودی رسمی خواهد شد و پول خوبی به‌باشگاه…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22873" target="_blank">📅 12:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22872">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQaeDKXN_5oPYxzse0Po2l0LvBXMnVfCmk8Ikyd6uUyxWaUyDIGe_jNpDIuIhk0qdc2Vwk2J6BmvHlp0cwiQGlS0q6jeApDGdAvaeHWAakY2l3poJODqWJYjbHQF7d8iLbLYibET_-mF_KFCB1okDPBehl0L4wrapROLtmeek3uIXf-zq5Qd1z406tdk6-32xKHuGBsTqIMrqc7Ub_avleQsda114uk0e8IgCD1O0-SX1m2cyLSCpAYKO3rFTDCUrui2a5D41LhKQzagUaa_ov5gOELNbB3QFe10rdJiu8qsh3Hwy-AhHWQ_r1j6rQjvsfXHoMMhz1oVKD-Zh5yyaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل‌نفراتی که دولت آمریکا براشون ویزا صادر نکرده و گفته حق ورود به آمریکا رو ندارید.
‼️
مهدی‌تاج رئیس‌فدراسیون، مهدی محمدنبی مدیر تیم، هدایت‌ممبینی دبیرکل فدراسیون، محسن معتمد کیا مدیررسانه‌ای، مهدی‌خراطی مدیراجرایی، مسعود اردشیر افسر امنیتی، مهدی ملک…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22872" target="_blank">📅 11:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22871">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3LKY3Wap2zb6_ZlUgmRq52UfVr3TowdexCeaD-RHZ7lYkWYMFbmNCcc-A6FomXMKg6av6iiW_LQp-wKWgw7dulk7U0g9wHHYtMuVaLXMU3WfdkFKENJo6FpLFwT64EVRDZuJ-TUscT055Ni_2rhCzZqcUGbZILcviLOe2YbyW9KkNoh4RjwMWd1JSxJTEVzHb1WkOVzqUmfQHfxVeyaeMLLU1uQHtHa8H2BIRBQsIthH3x6dd0G1ZFAwCaKpW5OEuQHH98sVcL5Eqy7i6RX_1udFXyUWEP5OY8FVWwZ1TaxrkfxhVx3qpP4PNNKzExG4Sb9NIaTjUZajnZN3nO4aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ تمام رسانه‌های معتبر خارجی از غیب احتمالی چندبازیکن تیم‌ملی ایران در رقابت‌های جام جهانی 2026 به دلیل عدم صادر کردن ویزا از سوی دولت آمریکا به دلیل خدمت در سپاه خبر میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22871" target="_blank">📅 11:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22870">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35d2a48cbb.mp4?token=rK7HW38znZeduUGe77taNYXWL4iHmAc4pkot7dQLt1jLy8tEianX-vvQvC3t8eXfSsU9oP1oR5G80-1eIrtta8gQiPYBs1IEWBwU00B_FxjCoSBwdy1XEENoxphdsZ_Rk2eB4jCPcCRnvpwnSbYwi5oEVnE6TEnYb8z9cvDk9LjoDbuewSZqunBIeOdIw_78gKYwMaQDx8CPXY4I0AsGzCSM8gMoUpoUYo_ViLB8HW6o3o5z_FvfNo4Lm7G70YAEvy46qVssOE6eVrNIjKqy67NyGPCOdtRdTFiLq9bSazXkfI4HOIiqJiwUf_jUaj7mpx37rzt7PB7julkoOvkyZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35d2a48cbb.mp4?token=rK7HW38znZeduUGe77taNYXWL4iHmAc4pkot7dQLt1jLy8tEianX-vvQvC3t8eXfSsU9oP1oR5G80-1eIrtta8gQiPYBs1IEWBwU00B_FxjCoSBwdy1XEENoxphdsZ_Rk2eB4jCPcCRnvpwnSbYwi5oEVnE6TEnYb8z9cvDk9LjoDbuewSZqunBIeOdIw_78gKYwMaQDx8CPXY4I0AsGzCSM8gMoUpoUYo_ViLB8HW6o3o5z_FvfNo4Lm7G70YAEvy46qVssOE6eVrNIjKqy67NyGPCOdtRdTFiLq9bSazXkfI4HOIiqJiwUf_jUaj7mpx37rzt7PB7julkoOvkyZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
اجرا‌ها و موزیک‌ ویدیو‌های شکیرا برای جام‌های جهانی ازسال 2006 تا 2026؛ کدومشون بهتر بود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22870" target="_blank">📅 11:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22868">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MW7RUwYRMgknZGw4XDTcv6PveYbjYXKUgoWm3opXj1cVpblt1xJpTbHFvJzuw9Mgh5whCrfam1hyGIb2cRC2jbrDfJfvYUZVaxTdtAtbOyZplawsnU0a6GjOVhjm2-fyJJxBHOXi8YIPCMIpphUYcbkEhaqp8RZoLNnKiUq05oO-xKpPH4zzT6zx2J6pBtVrP_15reQBCP3dQmvF2QnO6Wxfz1oyZxcccjXyldtDLUMP98Z2jawVyQd3Nuh6n1vgccaWKExgLLyAdyaA-bYVH-2BjCC7vFvanAYwg09Pl1InjADPk6cZacL5oNHp3lIc9hFbgy18ezKzjRY5VMxZHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ظرف 72 ساعت آینده از لیست اولیه اوسمار ویرا برای‌فصل‌بعد پرسپولیس رونمایی خواهیم کرد. منتظر جوان گرایی و عوض شدن شاکله سرخپوشان باشید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22868" target="_blank">📅 11:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22867">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yh41ns4Zca5wE4vvQ1psAOw5QE-9uf1Wiq_Hy3vstmJ9Ego2JChYuUbFe6JaGfEmQ8nHyHezFVPITz8X_QSmHSlUVcvBEEcCOPlaKBH4u0UIaMjvHnDZt2j--jZv4INUMWyXIs6k2goFoIxVcD1BMVSxu0cGVB5OO1egUHRw87nYe_-Apg_aaqVfZvEGv0UzEnxFWUvEzGb_RfYNs6NTCF_ODZp34g4qY6QSlvQpY6GZtmq3CxEaLHZEk4_qhjTP80wptLK7IMh0jHXmkC5MKsWjnVBKmaY6OT8M1t_6O-aeKthmZfGs1XkRM-ci-GUY914trxG3Eti4JyLPIiX9UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22867" target="_blank">📅 11:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22866">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=Qzwb1p0CanJ4ddCONSLFJq73XKqLbN3k-18JENvRKsejGMbKaHszQzeRLXIE5CyRdYhmZybFya6Wvxj77Jlj6ySsdnOMwfrtXQpQEmRbPgvyQ-r9Xt9PB_meNk11a6N6ZR_7zDn_q7pvmi8bO70XseZJ8X8fPnoEiCl52SVz9WQo9mCMk9lvzNtstKAHLN8YNMkTPhGo-3brsMcMErmFhxxoL-Cb8a25n9uU_XRVuJQ1rmn6iI-gRgqYyU_nqjNLJ7iBe_XQP-fNxAP6_ZxyHrMSa0lK85NOJ1lNhU9vK6gIX8FVaXBoz_vst04IJNETi546Z6yy48dJSJfHyv1WVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=Qzwb1p0CanJ4ddCONSLFJq73XKqLbN3k-18JENvRKsejGMbKaHszQzeRLXIE5CyRdYhmZybFya6Wvxj77Jlj6ySsdnOMwfrtXQpQEmRbPgvyQ-r9Xt9PB_meNk11a6N6ZR_7zDn_q7pvmi8bO70XseZJ8X8fPnoEiCl52SVz9WQo9mCMk9lvzNtstKAHLN8YNMkTPhGo-3brsMcMErmFhxxoL-Cb8a25n9uU_XRVuJQ1rmn6iI-gRgqYyU_nqjNLJ7iBe_XQP-fNxAP6_ZxyHrMSa0lK85NOJ1lNhU9vK6gIX8FVaXBoz_vst04IJNETi546Z6yy48dJSJfHyv1WVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تعدادی از هواداران پرسپولیس مقابل فدراسیون فوتبال جمع‌شده‌اند و شعارمیدهند که پرسپولیس رو به جای گل گهر سیرجان به لیگ دو آسیا بفرستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22866" target="_blank">📅 11:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22865">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">▶️
هایلایتی‌کوتاه‌ازعملکردخیره‌کننده مایکل اولیسه دربازی این فصل بایرن مونیخ مقابل پاری‌سن ژرمن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22865" target="_blank">📅 10:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22863">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9211e2c5d.mp4?token=nPdAuhV1-qCa543H6NjQqcjHCKvDuoHFaM-ytNCZ94DF0ubZ-wfBFZTVgA1eb0n80qbAx8CH0ZTHBngPtaV0pN-qLsK0yGtKYDzl-TvDTHdQfr7wHWFJU0xdQ-C6Nb5Hm1Q59_9PBP7n_GW8U3EyR7h5b4Yiemb-5zdehQnnvcv768ntaxbr8-ndq608mIlWRhyRz7Swu6a5ACHp5sXG3Cg-eu3s_gVqaj21av7D4DHVs4OYWGsPAwkRPiNUbzvSAcoHn3d9s-J0qLAorpomR-X5zU4alC7oQJvZ7ImxuFvgJ-XKNNTUTOmQ93oVfNBHmjvm4tBe0sTlBQI_-NNy7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9211e2c5d.mp4?token=nPdAuhV1-qCa543H6NjQqcjHCKvDuoHFaM-ytNCZ94DF0ubZ-wfBFZTVgA1eb0n80qbAx8CH0ZTHBngPtaV0pN-qLsK0yGtKYDzl-TvDTHdQfr7wHWFJU0xdQ-C6Nb5Hm1Q59_9PBP7n_GW8U3EyR7h5b4Yiemb-5zdehQnnvcv768ntaxbr8-ndq608mIlWRhyRz7Swu6a5ACHp5sXG3Cg-eu3s_gVqaj21av7D4DHVs4OYWGsPAwkRPiNUbzvSAcoHn3d9s-J0qLAorpomR-X5zU4alC7oQJvZ7ImxuFvgJ-XKNNTUTOmQ93oVfNBHmjvm4tBe0sTlBQI_-NNy7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کیلیان امباپه: همه فوتبالی‌ها قبول دارند که رئال مادرید بزرگ‌ترین باشگاه جهانه جز هواداران بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22863" target="_blank">📅 10:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22862">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nt0bcEb1NAnDesBtiaEv-v_xlQuAc_yRyXwcLwjBvCsio7Gy6snBlSvAeWnYHgwquDSFirv1EvAlk_toneaXo8iSEEfrtpM077Ex_vyJpdu3JCWOb5kckZpS140D1r0w9URHXxsMRzCkRC3KyCy4h-Qcu9UO-dlBASArtTc4v7N2qXwlrVxvRUrlIPIgacoYozgtEt7R_PFYbVlfqiX9P3B_vEdKKG5HJLK4BYf3F9cLVMNw0MpyipHecUvCLkxBZLGla49CO0ekN2e2DK_VwRe0gEK-_CC36I3d12DASjG5F3th7Yf6j3v37-MMXOWOWUqwLbF28nVPdWXBIwGmrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیشترین‌سرچ‌های‌ایرانیان‌بعدِ88روزقطعی؛
بعدِ بازگشت اینترنت مردم اول دنبال چه چیزی گشتند؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22862" target="_blank">📅 09:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22861">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73764a80a.mp4?token=TUipPhYlL85GIDdEcIi-eDrTmyvNHgamgbkOcw4OY4JZIJ0BpRGYxqcUbTwx7Yf_2AI6p_2KCioLcJiyCWAG8r6_rrefGp5l5ZDYkhM_IUP_hj3kab9WO6nA2CxcRMG3_uI3PkNGDUPKqP13CecwykgYpCcZ6cxCMD8bsff3mzIcZIpHWqSqYigZhGxsAiaruRdxUYhuYlwelZJxlp3SNqI8Vr0j4cwjEYwQhOVnWHyHdqWKgrTm3PLjQ0kQ9kndwJsRIexHCkZRDu5lfBFo6Jvjys04IBbsvi6J1iJkmTJdfQU_jdaB5aBcgGb0s-YTzpYcRQB4PvOsjaPtm8ldYENTjrHz1MXn8do-o-VS6_ir3AwWciQK8VbEQL-cksa1O2yZcFr9OeUBmYVftjIViLVNsge-Q_DPUlmPWqFu1PPeGXXtqZoRSJdM8KS8uBPo8pSYHrwltXYgTOVT_dnlIVDolJ7t-zgF78ftdBJQK5HyO_2spEeED4BcgLktfm9cwN8J5hQJVqIFpByS_81JweiC0mm87x783QE-onl31pxnu5Ob4yYrgk2WIJQBaeVcyZ5gN4mjaJxRuOV6L4YVlGUJEWMNvNdFoVDaNz3DMmDujdyrULt3ehZgiZMTavgeBCyzynDiwOXE5ZEELeYowBEjnBg3MNNf7kOfI-PzRII" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73764a80a.mp4?token=TUipPhYlL85GIDdEcIi-eDrTmyvNHgamgbkOcw4OY4JZIJ0BpRGYxqcUbTwx7Yf_2AI6p_2KCioLcJiyCWAG8r6_rrefGp5l5ZDYkhM_IUP_hj3kab9WO6nA2CxcRMG3_uI3PkNGDUPKqP13CecwykgYpCcZ6cxCMD8bsff3mzIcZIpHWqSqYigZhGxsAiaruRdxUYhuYlwelZJxlp3SNqI8Vr0j4cwjEYwQhOVnWHyHdqWKgrTm3PLjQ0kQ9kndwJsRIexHCkZRDu5lfBFo6Jvjys04IBbsvi6J1iJkmTJdfQU_jdaB5aBcgGb0s-YTzpYcRQB4PvOsjaPtm8ldYENTjrHz1MXn8do-o-VS6_ir3AwWciQK8VbEQL-cksa1O2yZcFr9OeUBmYVftjIViLVNsge-Q_DPUlmPWqFu1PPeGXXtqZoRSJdM8KS8uBPo8pSYHrwltXYgTOVT_dnlIVDolJ7t-zgF78ftdBJQK5HyO_2spEeED4BcgLktfm9cwN8J5hQJVqIFpByS_81JweiC0mm87x783QE-onl31pxnu5Ob4yYrgk2WIJQBaeVcyZ5gN4mjaJxRuOV6L4YVlGUJEWMNvNdFoVDaNz3DMmDujdyrULt3ehZgiZMTavgeBCyzynDiwOXE5ZEELeYowBEjnBg3MNNf7kOfI-PzRII" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
#تقویم؛ یازده سال پیش در چنین شبی؛ بارسلونا لوئیز انریکه با مثلث خوفناک MSN در فینال لیگ قهرمانان اروپا یوونتوس رو با نتیجه قاطعانه و پرگل سه بر یک شکست‌داد و قهرمان این رقابت‌ها شد. این آخرین قهرمانی آبی اناری ها تا به امروز در چمپیونزلیگ بوده است.
⚪️
…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/22861" target="_blank">📅 01:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22859">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bx7phG5vZLrGAXKFFrRT9GifVwTaiWNylwpIhQpTPRP2e3shfwH-_tOF8sS_G8Fs6wsr9JlR3LX5jNOxgV_a_6hU-7u7yVBF1tlABdYTRUkunu64EgzUpp3xKH1iRrCQ_0MxCKT-AyUarMI0SatKzOEaT94clTtXiWzEVqOmhLq2VSX3USoS8Z3KiwSMkLxUTHm5o6-8A5rbdlv4o1wuvZqXDgal867K0oiQpJ5GaxqENiYb-cVcwA4ldVO_H7H3VJA5_OpW_ZOVsYzwGOT9gBLxumzwc0Luwaq9ttYHuszRx0NoDJKIf5mGtXkpIpJMfwADwux8fn8JyswU-ClEjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T9_lcB7_c1QL2cAwQ7Vy5z06eR4WUij9njwca6AN5m-QfgUIsaZuFl9oIj9eQgXyAotH_LOAicBbyQWT4r0u3LjHAxUrijde8qt-AIgKAatuzWQLDHdOU06JOtId0NC_DtlKF5IxK7Squ_kzgIKidZnIcNLGFYzV9UYi1R9XkziKSaUGWZUAP0tCpE7PWpiNt1MY9zeZyAqFvn9gBFeEVgI6dxqeIzLZ4EJSnKYnHbbNl_IwWV8Q9Mld32SbwifBTgtLlPAxXqnx_87ekNeSzBr6KR1eAXas_IyThroPAjBiCXYiMf91Lu--KGm453w3RvszXRy4i_Q0K1PY_t4FXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
#تقویم
؛ یازده سال پیش در چنین شبی؛
بارسلونا لوئیز انریکه با مثلث خوفناک MSN در فینال لیگ قهرمانان اروپا یوونتوس رو با نتیجه قاطعانه و پرگل سه بر یک شکست‌داد و قهرمان این رقابت‌ها شد. این آخرین قهرمانی آبی اناری ها تا به امروز در چمپیونزلیگ بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22859" target="_blank">📅 01:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22858">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9AGy_SotXHUrcUEHtNkeXFcGf9quGg362FTYqsl20O2He15Ebi4GatuAbjrOaPvQDPdH3UhbkVzVB00pWsv9sTgPIBgJMuWk7DlnL-bR_WP5W9Yhv2UiIRNyCRbkkfSvtN8Jhar7F6V08VcOAEU5f5JRCMRlW8M5sTcSIt3-Zqdz3HMZNFCOPFg4pFWn4gH2upCmi_sms5A0O4xHFSLBAmB3n2h-Mu184yPjn6l5asbFoCPMVefgt2pUjt9gVhZrSwpbnmUxRPNCL_-0CH1PBLtfELwu1JEl-qFSY_p0yOdxnyfCV014ISe7LQ6bYMNTKS7wQolAu0Czgj-IEw68A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌کامل‌دیدارهای‌‌‌امروز؛
ازجدال‌یاران رونالدو برابر شیلی تا تقابل آلمانی‌ ها با شاگردان پوچتینو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22858" target="_blank">📅 01:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22857">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efrIcPzfN-1oCd9wu2LMjJ_FXx7zD-ir52ugG7uugtVZwgFOIrHGR6DrRqRiwUMK3GvtEXkB1tGC-hdTKLJyceSxAVSTtE3xyEUxUgv0_Eovl7fOKCzO0ZSCLyYbvRd8hqdQhpk2_qcnCQVo7HhqIzdhtrlWbyrvqnFK0qest8Z0oW92Xu3qKmwICBedkPcu_UF1nVxLk0ZqHGys-P68Prlv-RtZSQLOsL29N9s0AM4oQzGk5e0cb0q6kdKb6MdOgrNpdws9jUfnG4lqUNoikc0XoFg3B3IOw4jjTH4aIRl1whd325CZwa6qae3xSjeCquPmKweFw4fv-ukPGZBH2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌ روز گذشته؛
استقبال مکزیکی‌ها از جام‌جهانی 2026 با جشنواره گل برابر صربستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22857" target="_blank">📅 01:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22856">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plfbsQPBX_pj_l1KkakF7JvomPN6NGBDO5YEGD03rTTLN6EQactAszi6koYwLiqVKiNmtgpOzW4Vt-5DHFXFq3vv0Sru-ZCypJm5Gw1-7mpC8RCKL7tpIdJ0PZxYq7D0rtGqq3G2-tJknrSzLqNeggEjUa6qN_n6PqgWF77T2fpYuE1PlGTuFVdceLWf8mxOvewdPU_CYhAjncUa6yvbr9uLC0T2GXpWNrys3l3EeeU-U0RRw089hANvfPFBk6FQ1ijDPxEI29RlBHvTgaIsYxGhhgxpoMpzoiyFXKnIuby9IyS4H2vDtpleVg9y630SqEeHboEBh-oqVZujeczEtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شوک‌دراردوی‌ژرمن‌ها
؛ لنات‌کارل‌ستاره 18 ساله تیم‌ملی آلمان درتمرین امروز این تیم بشدت مصدوم شد و رقابت‌های‌ جام‌جهانی رو از دست داد. ناگلزمن سرمربی‌ژرمن‌ها بلافاصله آسان اودرائوگو ستاره 20 ساله لایپزیگ رو به اردوی تیم ملی آلمان دعوت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22856" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22855">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeX6yryPK3yOw9jjjawEcVHC18-P2efjH3XZ_XlGytyY8j5KwOGcUvJt17LK7OZvMwpadUaeNEdyH_QQA7ZA6saQ1T1wjRlj2rThNap-9vzDBYmJYoUvdeiyYfl1qd2KvmCIF6BRGyJ9bw7GkGQtayY-MH2o01fxfXl6xOIRZJ1bcjthaGNpWWMTglTJw2rWz6ngeEx5-UM7Pzl9g13PebkCvxXJv4l7arhMuvmws8pxGYQJBZXoRzyjX8UR3gvxFWhAbZvgFcwayMvhxjD2BPcwBm2sQQE7GPJYawanZHZ16rMCkNVq0wgGLhHOOsNdVK2eboIIQ14h5jqplhBJqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛طبق شنیده‌های رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره ایرانی ماخاچ قلعه بزودی از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/22855" target="_blank">📅 00:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22854">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSx45ueRi8qZkk4iGQIk9CDbvdO19nGbKlDvxYO8MCwvnnqZNcl4mvWe_bpS_L4d_ygkdtDl54G6mFyapGb2VOV4IOfGSVn4-PLIamnhCLTh1sTMx_bzzw3Wa3tzWXrkMZAVt0tVwjS6YZP_OHPOzOzG7F2f96gTm9o-JbpLVjpBeKxYhaSweCkPV_OzmkROdZLMGgOQU5avbRoOLlrJ-T9VKR6c5-YpyWwdDPiXhNjdwMhuPVLUMYaMfUROiIni4vmlMZk4o3NmKiuOOZUqSWyGpCFoINMGpUbLf45LKPKap_FpaItBSPPua5Wns2tLZXxcjUIAwbUlX_fpL8NG1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چت‌جی‌پی‌تی،دیپ‌سیک و گراک بدون فیلترشکن در دسترس قرار گرفت. همه برنامه ها دارن رفع فیلتر میشن جز تلگرام،اینستاگرام و توییتر؛ سه‌برنامه‌ای که بیشترین استفاده کاربردی رو دارند باید فیلتر بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22854" target="_blank">📅 00:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22853">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e00cf6e9a5.mp4?token=dw0P9fd-9-3EpmSpm5sSPC1yiJ6q88_pC8ifCmkuf-lV0fK1ssqY3L0xXuLWPTJMVbE2CCRaXUB6-dSzjckMa2Vmx5y6nPqBJ89E_a0Q1L3kA-7mpudUmQcGa0vrWtxylpWK9wc0mE1FWeNTHpuGD1Udr1Wavgy0Gj6sJmwi2UojM0V-h7KI8orH8d6FuteIyLLyncDgLhZmBNEH-HwXhDh4Ir-CA328nwCQpiu2bbh2Vn93O_ETYCr2Oke_nIQCrC2VIsaZDta4OcSryRAV8iiKolxNHSpNT9YZN9jt-wdzr3fpwINpvVtmlqn83cbT0sqcPvhHLeXjxw2fdgxB-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e00cf6e9a5.mp4?token=dw0P9fd-9-3EpmSpm5sSPC1yiJ6q88_pC8ifCmkuf-lV0fK1ssqY3L0xXuLWPTJMVbE2CCRaXUB6-dSzjckMa2Vmx5y6nPqBJ89E_a0Q1L3kA-7mpudUmQcGa0vrWtxylpWK9wc0mE1FWeNTHpuGD1Udr1Wavgy0Gj6sJmwi2UojM0V-h7KI8orH8d6FuteIyLLyncDgLhZmBNEH-HwXhDh4Ir-CA328nwCQpiu2bbh2Vn93O_ETYCr2Oke_nIQCrC2VIsaZDta4OcSryRAV8iiKolxNHSpNT9YZN9jt-wdzr3fpwINpvVtmlqn83cbT0sqcPvhHLeXjxw2fdgxB-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ابراهیم کوناته مدافع جدید باشگاه رئال مادرید هستن دربازی روزگذشته با ساحل عاج؛ واقعا مدافع قحطی بود که فلورنتینو پرز رفت این رو گرفت؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22853" target="_blank">📅 00:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22851">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktBqosyM_6xl_6_dgJoFmkhpWQcHgf-x3gqYu0_SpBeDAnHuxtzICzUicmc3aDE9pTOleB0C5rD-CwBaXbcGs13l107ZaW8UHqhdYfUT3Uzwmuqx1MLXITtPvifcODY8H3wbIgvT3llzDqz3P36AFYTbAVJnarupjxK2kudJHwZY8kCr2XKOLFqftVJ4OQdjqHU-XGfHfqVbBAsBQcl607S_CHVrr--f7M_FL2jdO5nwq44GqD9E4ILbGxY2InF6o_fdHqkepR60H69eT7JA8qm8__VdU7r33gAnKciYkG2TmmB_j7r32rRDYmIIVHrBUUtF7emZlQI-x5Xv6ufvpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
علی‌‌تاجرنیا رئیس‌ هیات مدیره باشگاه استقلال: یک‌‌نفر از اعضای‌هیات‌مدیره تیم استقلال در طی روز های گذشته با مدیران باشگاه آلومینیوم اراک صحبت کرده‌ تا انتقال محمد خلیفه رو نهایی کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22851" target="_blank">📅 00:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22850">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nn78Y2KbDIuNhm9tLmtxfKJAjOyO_OBVZSevoJQqz31RYyGjhdr2aj_woGqGvS7O7llCXZTSG6-oExZFcqyQ4-8UKUxX4YLTHSV2hNShrkxHvYLgqMhXdyKH04nx0bzCoPaSG_mdemvRW__naDWZoBFQiD-uZhiLsBBNebODZXvfLLiAbkYAgjBS_HgBtCty4JLnkdU-XrDoiUgZJvFPEeKFjqf9YZ__yD2zNLSEO2MXtVAOszeT9wON6qNre3nljfRrDHCGrzv3cItrPyCfdrQP5VV5ngGI6vUpY9yh5g1LvrON6J7uIssPkmHFtFo0L0lfPeQFuEI0pUBLptBdkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22850" target="_blank">📅 23:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22849">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aedcb21ace.mp4?token=sCs_H5Mf-cCodRU-bvjlvuizdQRoLxDcuY8GZfcnBtx22EQsbQtyFRSe1MP6-OAlZTklZ_gLmxWnh00ypjH9kWXmzao3m_RJpS7VJhkj6Xn14xiN1psELFyZyi5fo3bwqekoUCQwqAHmPsh3MPOqUjTLAGjuA6ymJZB8CAujr-nLkwHjtM3GCLseexotXYWGg6noz-xkACfORUoujWhujl7kCmW2LrMUy1I7Z0rQOyIWOzIH_Me4-LHXRDxbyiAnta76reNVTL4FZZ7x8yBsXq_NleA0c37y1i898mHHJdc4I78-7r4X2U6pdi92KogALMFXIFyQYyiIEgirzM4oMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aedcb21ace.mp4?token=sCs_H5Mf-cCodRU-bvjlvuizdQRoLxDcuY8GZfcnBtx22EQsbQtyFRSe1MP6-OAlZTklZ_gLmxWnh00ypjH9kWXmzao3m_RJpS7VJhkj6Xn14xiN1psELFyZyi5fo3bwqekoUCQwqAHmPsh3MPOqUjTLAGjuA6ymJZB8CAujr-nLkwHjtM3GCLseexotXYWGg6noz-xkACfORUoujWhujl7kCmW2LrMUy1I7Z0rQOyIWOzIH_Me4-LHXRDxbyiAnta76reNVTL4FZZ7x8yBsXq_NleA0c37y1i898mHHJdc4I78-7r4X2U6pdi92KogALMFXIFyQYyiIEgirzM4oMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه پرشیانا؛ باشگاه آلومینیوم اراک اعلام کرده‌است‌که هر باشگاهی محمد خلیفه رو میخواهد باید 100 میلیارد تومان ناقابل تنها بعنوان رضایت نامه این بازیکن به ایرالکو پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22849" target="_blank">📅 23:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22848">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e230120d7d.mp4?token=Tqn4M50T7l_6D5TKL32pGSFVICZUjY-QGJsqnibCIGGTeCjinZr5jllk2WLn2O5F0mLUFSxAKXoJJoape6Q1m6BieSduKByAJeual62VtW6l0tgdNEjoaotj1ufLw_bKbcjAFlRGMxdh0FMtDqvypT6O2fvw_acTUgi0oHfdfiYh09TnEnNhAhJRsgZjRVOs3hThdCykn4NR6OXBOED-k-qccPeoz6fXBMaPrwGtAXNgasLBGIRuQabJunmHnm_wbYWzBosxWn1aIGK0dNh3oYg5EZ-6TaMNeYpqMHGRXd6T3DkzW6N3kpnz8AXMAY8uYa2OfUUqrB8BOrYuZa4S1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e230120d7d.mp4?token=Tqn4M50T7l_6D5TKL32pGSFVICZUjY-QGJsqnibCIGGTeCjinZr5jllk2WLn2O5F0mLUFSxAKXoJJoape6Q1m6BieSduKByAJeual62VtW6l0tgdNEjoaotj1ufLw_bKbcjAFlRGMxdh0FMtDqvypT6O2fvw_acTUgi0oHfdfiYh09TnEnNhAhJRsgZjRVOs3hThdCykn4NR6OXBOED-k-qccPeoz6fXBMaPrwGtAXNgasLBGIRuQabJunmHnm_wbYWzBosxWn1aIGK0dNh3oYg5EZ-6TaMNeYpqMHGRXd6T3DkzW6N3kpnz8AXMAY8uYa2OfUUqrB8BOrYuZa4S1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی؛ اینکه خبرمیزنن پنجره نقل و انتقالاتی باشگاه استقلال بازشد زمانی صحت داره که درسایت استعلام فیفازمانیکه‌نام باشگاه استقلال رو سرچ کنی بالا نیاره. شماهمین‌الان هم نام باشگاه استقلال دو در سایت استعلام پنجره فیفا سرچ کنید بالا میاره چون هنوز بسته است…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22848" target="_blank">📅 23:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22847">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfPJ54DviPFr4ZOTtG9tWWA4W4SF8ukFm7LR_s52mi3t6hBIrT4I8qpyac9yZLqrXTEg2C5XOM-0zW-nOkPe0JqjCZbIVeN_XZ6A9BGJuOZ45iJttwxId8cH8BJqduWpmlZ_t8432MHvWh9mYeNs0TdraSEMtCDPCcVWrLm6hD6rvFKPTqCQp8z7U0921Y8ZmzrbbntTqbqD5OYcsHGjTyKejcNGU6RItAcfzvGBeoL6nLhfdn8-VmT7ru4HG9e7YHKl2KHP2QTF5aNzsb9pPoR2T5R32E4ca8v-PHhUG7VM7enxLsjIZiOT1JA9LgRZ2fMJ97Ob3c_PlygFEOjDWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کیلیان امباپه ستاره رئال مادرید: به پیوستن مایکل‌اولیسه به رئال‌مادرید بعداز چام جهانی بسیار خوش‌بین هستم و امیدوارم هرچه زودتر این انتقال دوسر برد برای ما رقم‌بخوره و اولیسه رو بزودی در تمرینات رئال ببینیم. او یک بازیکن فوق‌العادست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22847" target="_blank">📅 23:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22846">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">▶️
انتشار موزیک ویدیو جدید شیدا مقصودلو همسر ایرانی خوزه‌مورایس‌پرتغالی برای جام جهانی
🔥
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22846" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22845">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa70e9e949.mp4?token=NgM8A0ahBvm77xQYBzGiz2qYP48DqWxnYweZ78j5oK7FSQZsrRWTTwRHxqnRHZwlcY8Egr5sCeObVVmPKM6haefJXVcffL6DRDaF2BhQXnQ1SeruvjToN6UfGTAInldby7L3uecC7Vou4RkcAUOxgp0Qal3SMK5X5WikXmt7gU2AR7yFK1f_xHB9rQka2Z3fBqZ9AwgbnIsC-NT1c8C8W2NlDcGcdeuyDmn6PJ3HRR29T9kSKf8kfLRb1te-LfNKBNGE5mZFUPT1nOzINP717ufKm0s_4ZoGhITxBE4L6d6erNTyJ3K9PYMz3k2I0oS8inp_yzFHqs-nMTDweCOMEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa70e9e949.mp4?token=NgM8A0ahBvm77xQYBzGiz2qYP48DqWxnYweZ78j5oK7FSQZsrRWTTwRHxqnRHZwlcY8Egr5sCeObVVmPKM6haefJXVcffL6DRDaF2BhQXnQ1SeruvjToN6UfGTAInldby7L3uecC7Vou4RkcAUOxgp0Qal3SMK5X5WikXmt7gU2AR7yFK1f_xHB9rQka2Z3fBqZ9AwgbnIsC-NT1c8C8W2NlDcGcdeuyDmn6PJ3HRR29T9kSKf8kfLRb1te-LfNKBNGE5mZFUPT1nOzINP717ufKm0s_4ZoGhITxBE4L6d6erNTyJ3K9PYMz3k2I0oS8inp_yzFHqs-nMTDweCOMEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22845" target="_blank">📅 22:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22844">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080305bcc8.mp4?token=cQk4gxHgnhjNvK2k6JSxjnGNXUh9IppwZ2zVPDzCc2FtxSDZmnBs7dkPNWvo8tmE5zNGqw10hV9IaBMCL5kqVCInwKsMXnqEiAz5x9o6FfiV0_2u2Ysd5kqTPEBPL-WMD1gCbv6Aw22Hd85d-U05MPRvkyQS0IjrczgHiOLgy3ICS44-WAWhbNZWnUSZnisrVU-GHCivGh-RvoO_KnEDPXbqfzM5Y208l3NQC01L355VEDv7qgHOls3pvkoPRO86AvudVlBF7CRk2zoBvUdc5U5SH7_UeIeucT633SPOvNK4Wqb1Cft-3WwfoYIBCpaddI3yfFJ_4Dqhr0IgDuCeXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080305bcc8.mp4?token=cQk4gxHgnhjNvK2k6JSxjnGNXUh9IppwZ2zVPDzCc2FtxSDZmnBs7dkPNWvo8tmE5zNGqw10hV9IaBMCL5kqVCInwKsMXnqEiAz5x9o6FfiV0_2u2Ysd5kqTPEBPL-WMD1gCbv6Aw22Hd85d-U05MPRvkyQS0IjrczgHiOLgy3ICS44-WAWhbNZWnUSZnisrVU-GHCivGh-RvoO_KnEDPXbqfzM5Y208l3NQC01L355VEDv7qgHOls3pvkoPRO86AvudVlBF7CRk2zoBvUdc5U5SH7_UeIeucT633SPOvNK4Wqb1Cft-3WwfoYIBCpaddI3yfFJ_4Dqhr0IgDuCeXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
ویدیویی‌از قهرمانی تیم زهراگونش در سوپرلیگ ترکیه؛ زهرا گونش بهترین بازیکن فصل لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22844" target="_blank">📅 22:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22843">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63cbb26f8b.mp4?token=j1RRVOODxGI9Hqd2pemdZrGplKSIZzTJ75ILFjnaL4bF-2oXCzgmnj-_Kfpvz3os9rnuLKEPUniCmuVgo0_kZRv7-_AY6uvuqe82XK3uUU_WzsMhfU-xjENLhRweRLWEjoriZvUKProDsK2ZOtBW0HFy-R2HBZ_L3oAZXrKY0KUzAf8LG8fHwKZeA4MKEGLX3tY_YM2MdnQz1imW_UHrjEd7oiROzQiqtYohJvd9CHHdvBruRosYsUWYT8OK-nC3ptqjsu9lf-0Y9HZIN_tv1ZzG5ZHV3KP7VX5DMX8Dyb4Ig-lQbPkFnVplapxmDio8Fg9VuFxV1tmCvriD6ld3JkPtaQ-vxc1m9xHsOc-_BWLYccmQpqA-KvXOR5HX3x51wd26g3IdQ0j0jtzrgUeTU5Y8zI2NvXQIQIjXr0tfJL2UpJcGx7pIyQcU7XECTIHaMyLuxCN2wWhWsczYAhnfTijKB9ljkgKLHzozwO-QuokYkNvWgmS3HO8srK6PiNk1Jmh9C1fBKmjPiCMRSwm8fxcrw9iTDdlqBD86swMvGjHJBnACZHa-1iWtBRWz5ytsYxiCN_tsUm5DgpL69Rw_tA_h7M3hT6g_OgCz_mIyc6SGmWi8ZiODtTg6kWSDN8x0W1Q4qya-HxgXlt2AYISbANDaUP5pT0GF_9IIR21Jmuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63cbb26f8b.mp4?token=j1RRVOODxGI9Hqd2pemdZrGplKSIZzTJ75ILFjnaL4bF-2oXCzgmnj-_Kfpvz3os9rnuLKEPUniCmuVgo0_kZRv7-_AY6uvuqe82XK3uUU_WzsMhfU-xjENLhRweRLWEjoriZvUKProDsK2ZOtBW0HFy-R2HBZ_L3oAZXrKY0KUzAf8LG8fHwKZeA4MKEGLX3tY_YM2MdnQz1imW_UHrjEd7oiROzQiqtYohJvd9CHHdvBruRosYsUWYT8OK-nC3ptqjsu9lf-0Y9HZIN_tv1ZzG5ZHV3KP7VX5DMX8Dyb4Ig-lQbPkFnVplapxmDio8Fg9VuFxV1tmCvriD6ld3JkPtaQ-vxc1m9xHsOc-_BWLYccmQpqA-KvXOR5HX3x51wd26g3IdQ0j0jtzrgUeTU5Y8zI2NvXQIQIjXr0tfJL2UpJcGx7pIyQcU7XECTIHaMyLuxCN2wWhWsczYAhnfTijKB9ljkgKLHzozwO-QuokYkNvWgmS3HO8srK6PiNk1Jmh9C1fBKmjPiCMRSwm8fxcrw9iTDdlqBD86swMvGjHJBnACZHa-1iWtBRWz5ytsYxiCN_tsUm5DgpL69Rw_tA_h7M3hT6g_OgCz_mIyc6SGmWi8ZiODtTg6kWSDN8x0W1Q4qya-HxgXlt2AYISbANDaUP5pT0GF_9IIR21Jmuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
کاشته‌های‌دیدنی رونالدو در تمرین امروز تیم ملی پرتغال در استانه شروع رقابت‌های جام جهانی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22843" target="_blank">📅 22:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22842">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvkbIQDCxdi8yj4yzhBGks5yGneboXUvtLm8bWRdcyE4h2VFVfJykbBwr52mHknLnS6G0BPCrs6KE9IfSIYjSHG_K7EkhBuOvkkjQFsVWiBh_WrseitFYqn5b_EmalAwleTZ6EYCEjQiCLqrkJAP1q1C_Z_p9Xqn4eZ_b6HmQkyOL7bXLdBlVeSX3eJ79yKLa03VxI4TxeM2UgW0oe6vVGk4icwmJOzohFvRTHZipZmgEleWN-XWW2NOElw4TKfJBD_9N2zPCjNp0WiG8Rji9zTuDA9Kw5JxvLpz6XH3leicvmGmt2BkmolHCikZ48eF-WYc-4BE5TiYv9zdhmvSLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛رسانه‌های‌فرانسوی: کیلیان امباپه، مایکل اولیسه رومتقاعدکرده تابافشار به سران بایرن مونیخ موافقت‌خود را باانتقال‌این ستاره 23 به رئال مادرید در پنجره نقل و انتقالات تابستاتی اعلام کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22842" target="_blank">📅 21:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22841">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NP5bXRLGbBAah7ccYEC-cjT366bOHMOONEfMbdsHIuqPbVOZYXwCLepqCBWNuVRKXYobEOqKZfxXThW5f5y9gWzyVHsomnBDsD-yCqf1Qi2ahoVCj8C7Jbsa5FMMte7rhIfJWaci_mKES8kO_xV8l13gJXWe9KDStSboDh0rDUX9ofM_dbm03KXue59420CcLKYJzfr7KUc5f0XO2auBsgN87X9KKPwLRuRxsrUDOG6ryKI3juN-U526UyOSvCuGPkoiJlO3Z-otqA-d6MttVDDkWq8UoO5pbmVQ6TD6mF1_iSlWIHQmB-2v-ZBxpQC5MJrC9D3xkcRzFJHJyeaXbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22841" target="_blank">📅 20:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22840">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c01b9049b.mp4?token=JMmgvjWsKs9XH-ML6RdrWi2YKmUoIUyTkdJKEFU-xj4IOU8ca4nua78UKYovfAJ-Plk29p8rdNEroPx1k3KOsNv4fDLbZ0mQx1kyICrNLSdR0GOsF8cwXRvHMAj2cH5vfy2hrf5J7ppJWhQToq6ub86EIexsHNmi3v0wCBjVA7f7uaUgmUeaGKfLcgKqtHyVH9ZBCN6IoJfG5EHoGyr6PiPhVORchl2Xj6j8juWYBMdgELQi1L-8bXtNPxbDKTMRRpxtDiBUD0pNIzJmyvPtqig4EWIx3KEr5eY69BpRXtJJm81V1sLGC5e2LWhtwxYPIpuAKljRH0E65isTtl9BWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c01b9049b.mp4?token=JMmgvjWsKs9XH-ML6RdrWi2YKmUoIUyTkdJKEFU-xj4IOU8ca4nua78UKYovfAJ-Plk29p8rdNEroPx1k3KOsNv4fDLbZ0mQx1kyICrNLSdR0GOsF8cwXRvHMAj2cH5vfy2hrf5J7ppJWhQToq6ub86EIexsHNmi3v0wCBjVA7f7uaUgmUeaGKfLcgKqtHyVH9ZBCN6IoJfG5EHoGyr6PiPhVORchl2Xj6j8juWYBMdgELQi1L-8bXtNPxbDKTMRRpxtDiBUD0pNIzJmyvPtqig4EWIx3KEr5eY69BpRXtJJm81V1sLGC5e2LWhtwxYPIpuAKljRH0E65isTtl9BWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
@Persiana_Soccer
| Out Of Context</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/22840" target="_blank">📅 20:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22839">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgtc9jWRH3SdCicSdA76wzMF9J8L0Y3LzhLcLD_Qac6OkgGfQvxN6EhJ9JBlr9KWUcjC6yUB1rZnSI28mFIYKH3FZpe14kaalqGCxQK1sdzQ_Zxdx8COsCXqM6cHsUGwFOD_j6k38He6cysX85WhxdmpRnfuDfX5q_ky973WMB546EgizztnKSNNljfrm6C9CGUQc4DDKWvUcXItFdlNdikBqmDOIib8Nt06lDal3Fx5FlE_5zlv3YtUfT3z4cSj5eeLQg15NzjnKFP-dPJFzL8lPH9dD0YFghcySJBuZWsPACD-p-aC4LvI9oAFILMSYJqaIfLr5wDz42Ns7rqgoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#نقل‌وانتقالات|ادعای اسپورت: آرن اسلات بعداز بر کناری از تیم لیورپول به گزینه اصلی هدایت باشگاه آث میلان تبدیل شده و مذاکرات بین این سر مربی و سران روسونری بزودی شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/22839" target="_blank">📅 19:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22838">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0dJJPN3OE_nofjhev_ib7T7G4DHqEn-emowlNWA9FuOtEupq1xmrwPulZWJ1Oe58L543BuT-VtIQ41kWfXAVnYfqsC08ATs4wTtML_ZHSsBnp6vwOBzSEqVZCR4vApdCuCTHfF7WL2Kj0d7luSn3pJJA4oiRR-eHnJn2_4p1uhl1__fsfT0y6b18r_C2IMN8KtdyoDeKx-gZ5MlvGbbQMHdXGav1VMXF6YTWYzMIdr6XnwuzYQykAnQNEjUXHLDrqk3RA9RQIQ9OluptIzSJu6eNeY2d3jgcienhXCBF_q9pAtHjhSEnNN345jXqy_2NsxsI5mLEN4pQX15MP1dRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تاتار سرمربی گل‌گهرسیرجان از طریق دوستان نزدیک‌خود درباشگاه پرسپولیس اعلام کرده درصورتی‌که اوسمار ویرا از این تیم جدا شود حاضر است از گل‌گهرجداشود و راهی تیم محبوبش شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/22838" target="_blank">📅 19:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22836">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPXqxSfPac1xFwLuw8yFk5nPDPmg1zAr_rb0Ky1y0M5MRAfEBJPRjU_dWiQVhX3V1p3K6nOhpco0OGWvqq9-HmO56d5hvsHiSR5Vf1tKLtSLSTA3pwv4ml89UgQbLFwZk7PNvT0uS8tlUzOUD6CH1z16SNgKJUa2LXffXXyQQxlYHqzPnXmqRADr-w-5PZATz6b_jeFNN0va6mRVSYskl7Dkf5tHfQl5HqxDAOpFYLupqxqs6a51CiaI8CaRR1D00ovRdfuo9HILE8U7cccZ9hmRd9y7_c5v84VNv9IdmAQgEzEnV8PwPLSb5a6zBbuoERNPWhhtCqazkzYFQoreOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a220e76f7.mp4?token=gQGPhNWo9iY_LEaypsEj2qN4QNfdBrUbm-N7My6xPXKi7x0zu4vixRrkHtZdYNVbnQ7KFOGqivoERA-S6l2HQXu9T7hLFkCpoO31baS1SFuCf76vcfDVgADxq91Ck2FngyfVj_ScgJbrlMnsLsholVZdeA6izK9ammtUu-XMyT4F7NT_QvW8h4riej4J900TewCqeT_IW8HtMXPGN1Hq5yJyazwHZ3MbkoOJkTubebui8DgBhtq55iRwT2leqLy_hghwDwz2g0CQmoCr03xbAyePnFUdmpnUe805qYi86QcZ-hAOC44fjApLcjLOGvM13nN7C3shPxY7Fz7tBNtKZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a220e76f7.mp4?token=gQGPhNWo9iY_LEaypsEj2qN4QNfdBrUbm-N7My6xPXKi7x0zu4vixRrkHtZdYNVbnQ7KFOGqivoERA-S6l2HQXu9T7hLFkCpoO31baS1SFuCf76vcfDVgADxq91Ck2FngyfVj_ScgJbrlMnsLsholVZdeA6izK9ammtUu-XMyT4F7NT_QvW8h4riej4J900TewCqeT_IW8HtMXPGN1Hq5yJyazwHZ3MbkoOJkTubebui8DgBhtq55iRwT2leqLy_hghwDwz2g0CQmoCr03xbAyePnFUdmpnUe805qYi86QcZ-hAOC44fjApLcjLOGvM13nN7C3shPxY7Fz7tBNtKZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ارلینگ هالند جدیدا تکثیر شده؛ نسخه هالند جونیور، نسخه هالند پیر، نسخه هالند دختر:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22836" target="_blank">📅 19:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22835">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArLjkwZ4rECnRl6k8CdEYxArLoPJT9mrZO2YFePlha_m_rSBXWxeZ5ZpfWwlRH01CrmKTWKrvnKvCzvRtSW7T1dGTn7ulmM9hGBHpAVfkVzXUEmVTXTULULu4gfm-qj-JBRiY1W0KjUTl8e52U-m3DvtFtQVUUneFKklP31CSvlykFwnH5_iVA5RG6BYl9BIldI5rT6MeLK6PVOx9RcW5d7un2DbQJS01MXqYofbouJGnTb9MS4yETMhx_YA9RC-G_XRMBK_L1cYl-yPyN9VE1CFJVMimf1dIl8iIpKPoNVpbPqyC0_OdqevH7NAKfJ2xiP4PfxYG5tQMnazq9ZIEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو هم‌تاییدکرد؛ پرز میخواد به هرشکلی که شده مایکل اولیسه رو تو این پنجره به رئال مادرید بیاره. اولیسه شماره 11 جدید رئال خواهد بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/22835" target="_blank">📅 19:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22833">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIAxUbQWtuGgHgiSQcJ-Y_04FxZp_kGYO_8TeIWspdiuqXUnP7aNtd_TVHLs2y24WPeWnHnFk-E7FA0D_EdNt6iEqahsezahLTdWd3K_j6_OeUPXPOcKEV43pBW_3nNPRD07ExznjBChFgRkYzovbFrsHTvUwChXubOfMz7ePeZ7505WsdB3qm3jwGmXRfjUWpPpd8IrTNOLHV4Tg-dX0N6uI08Np0EnzekzAnjsfbK7VoqpG5VRgdOjo5AxWhSvIwvX89ghxPPP9Ny-gYLHpeTLY3OAk82vRrYvPywJHgV3PCpO5he_iRtqY36zwK1Fsnreb8SzGfvItI4VQ4tNKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا محمد دستیار تارتار در گل‌گهر: باشگاه پرسپولیس باتارتارمذاکره‌کرده واگر اوسمار برنگردد تارتار سرمربی می‌شود! او می‌تواند تیم پرسپولیس راقهرمان کند! باید چه کند تا سرمربی شود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22833" target="_blank">📅 18:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22832">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnM37mQrTOFSmjQpYL9ed-vHV0kiifugymvjaZ9_XU0PP3L2lbFfXF1ah5FC0KbO3cZuJVyIHb0zBysM9JJspNlkW1S5tPDv9enDY9lzU5taK9KqC1WV8cj9dZaozc6nMAvZg_FaZdgAyCuV9aiBljRXTTyD-swuhNYdNYjZAMPbYz4DmJq_8Gy4vTnGPh04pHqtJ1TzuvvG_ONPWl4hUMdKkFYcCX5GL98xyKHjQn3ZlSEYwdphf8vXgfkIx9dDzAtiEFfAtyZbvQqOldo60cepv1sc1nzx1Lh75rtJszCPq8fqOz5ekDjDKCTwLfae5m9ybMOPldsFsz6al6dcKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو هم‌تاییدکرد؛ پرز میخواد به هرشکلی که شده مایکل اولیسه رو تو این پنجره به رئال مادرید بیاره. اولیسه شماره 11 جدید رئال خواهد بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/22832" target="_blank">📅 17:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22831">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1lzA1SmLrGED4_GCer2eueko-CnnbmXBIssw1Unsu_y03knWNxTVG-2a37cIxcQ5pEVC7l9ZAeZ8M6q6Q2MErTPTcpgGIw_0HhzMNct91kGma3m-Nkhw6yT-TzdaLtyyesjOG0K_onQblE6RgvWpwOWO895KwShu0SLrQRaUwxUJuTQx1t0PlQrFPuTRjUt_MxhC6lYJwOIj8SS2Q8G6ty_hM4XtjlMu2vyV2yw9KXYV2nS3pocF9EFZJ6GFLpWse7WDi5Mk5RXhS2Y7YAr0yw-g0vfeTpZbMoJKOVhgyHS351I3szlWG1tVCkvNbEQ2mQe2nW4s1g4K8PqDuU26Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛‌خوزه‌فلیکس‌دیاز:طبق اطلاعاتی که بدست آورد مطمئن‌شدم‌که‌منظور فلورنتینو پرز همون مایکل اولیسه وینگر فرانسوی‌بایرن‌مونیخه و روز سه شنبه پیش رو آفر 150 میلیون یورویی خود را تقدیم سران باشگاه بایرن مونیخ خواهد کرد. خودِ اولیسه هم در جریانه که پرز میخواد…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/22831" target="_blank">📅 17:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22830">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjV4NnffSXTnDKfvtNFLCuL-1g6XNbvWes_3W2pD_OK6588-Yzgp1GByBaMapN9Y8NTnul4x-wqF70ENIpcnl8HUmeQ0GZH54JuJ-o50oWYHk8RZDdI8vkXt487LiEGUkNf_yW0thiaTy6T_YrGkJ-hZX2chhraipD6-pBKDTgvWy01kwh83GRXAwyVc2ef1WWRefPnTDzxIZA8Pc3HFSV15_cIaoXnV6tXXz0-pfBhbpGPVEqTLCZ-Fv0ZaMLoAtdwXRAYn4NX-wCYKLaRDdbafiaw3Lyx2Up50_WPNlNUVojm4pWMJl4hRkcjvUTuEIg6GbCkWwoC12AEpl6nbPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ خوزه فلیکس دیاز: علی رغم تکذیبیه شب‌گذشته فلورنتینو پرز؛ باشگاه رئال مادرید بشدت علاقمند به پیوستن مایکل اولیسه به این تیم است و قطعا در این تابستان برای جذبش تلاش خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22830" target="_blank">📅 17:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22829">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/976cd07773.mp4?token=hu-e6515imjAQWKt3V8LaQA9IQpFWaQiDpPnPyS25fpdNSJGgUVN4nP6aGk0NLVyshPcLA3It05NO0nvau3iBQtGu-AyapV_kPISRh6Qz5yysyPLLj_x6uwnITG-B4pp0VLHJFH8P_5kQEuVQJ-2GJMZVlGFLZx_PCncYgjgZwZAmyEF1OdKqyWnm0Jwgbeu0jfON70fYu4CbibED9wPi7HeM4btPsCMmdc0LZE_Oie1L-oc-OBSzQId59lJ4QnorzvCYAhjcAPhXOaR3E2Da8e-91ux7JvinPKZSH6QVM6Nz9nA78THmcw46vnWSVg5lDCScx16KHU2fjm5i2PvaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/976cd07773.mp4?token=hu-e6515imjAQWKt3V8LaQA9IQpFWaQiDpPnPyS25fpdNSJGgUVN4nP6aGk0NLVyshPcLA3It05NO0nvau3iBQtGu-AyapV_kPISRh6Qz5yysyPLLj_x6uwnITG-B4pp0VLHJFH8P_5kQEuVQJ-2GJMZVlGFLZx_PCncYgjgZwZAmyEF1OdKqyWnm0Jwgbeu0jfON70fYu4CbibED9wPi7HeM4btPsCMmdc0LZE_Oie1L-oc-OBSzQId59lJ4QnorzvCYAhjcAPhXOaR3E2Da8e-91ux7JvinPKZSH6QVM6Nz9nA78THmcw46vnWSVg5lDCScx16KHU2fjm5i2PvaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌های‌سنگین‌ابوطالب‌به‌تیم قلعه نویی:
شک نکنید این تیم قلعه نویی تا فینال جام جهانی میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22829" target="_blank">📅 16:46 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
