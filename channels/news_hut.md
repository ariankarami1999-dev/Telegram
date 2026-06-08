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
<img src="https://cdn4.telesco.pe/file/jwa-aGPNbzZ3bHB-Hhx__1Av4pwuR4mBTOGMKUVXnD3aZd0dNnj4uY4FQDnzBeYn7aplP0jhUpfHIrWY85IuIl0ph8s7h9Ka9KrOulKjt_qgl4nGo9rzNwmCUOQmRMxTFdCrFMbX8tvI0kv2--qiMuKeriVBoHynElbGYS1KOsZbXOuvny7cWIHeeqLNRDoFboiuy5JjKVmcDE1RqOuuN2dp3Fz9VA8di6p3xAGBBJEPvLnzY1ZVlYrJjAIPUyIW8Q_4Mo8jiOUgI93DyfL9TmXxepE6i-HjhxWhy6l1JBoYVT4X-Adifqa5nLHPtfMk09u3oJYSs-TlqcFdopoVPQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 228K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 09:59:14</div>
<hr>

<div class="tg-post" id="msg-65420">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9d994e5a.mp4?token=JzBYxwisdyR5mUdyR2mBYGEZYwKXlf799odZqkXejR76yn_IlCsVBVLN26Sra5IlZ_Fn1FbNtx623COOtKdDUssHDpo3vZUmvbnU2UiOyFvbOcRX0v90J6hpF-xxbxf7IfQ4J7QQJnP0P1jpHaNP7zNDKqqmVCye43Qh2A6yUYB2id5-Mnb8_505y6iHCJhpaK8GQDaUJDaJYg_DNNhhjl8hU-kkEnXmdc8WrFrtXJ_ng0nGbMj9ChJRx_WNVuDkVydoZuIlEcZAQbtN3FBYjeGtySlpUNd5jyYiucQtka4xOSHiO0rMi5kVumBQlRfnuMRRvwYzkVBrXfVCsLo6Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9d994e5a.mp4?token=JzBYxwisdyR5mUdyR2mBYGEZYwKXlf799odZqkXejR76yn_IlCsVBVLN26Sra5IlZ_Fn1FbNtx623COOtKdDUssHDpo3vZUmvbnU2UiOyFvbOcRX0v90J6hpF-xxbxf7IfQ4J7QQJnP0P1jpHaNP7zNDKqqmVCye43Qh2A6yUYB2id5-Mnb8_505y6iHCJhpaK8GQDaUJDaJYg_DNNhhjl8hU-kkEnXmdc8WrFrtXJ_ng0nGbMj9ChJRx_WNVuDkVydoZuIlEcZAQbtN3FBYjeGtySlpUNd5jyYiucQtka4xOSHiO0rMi5kVumBQlRfnuMRRvwYzkVBrXfVCsLo6Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
با تایید اسرائیل، پتروشیمی ماهشهر مورد حمله قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/65420" target="_blank">📅 08:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65419">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
پرتاب موشک از ارومیه ، لرستان و اصفهان به سمت اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/65419" target="_blank">📅 07:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65418">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووووووری؛ انصارالله یمن از آغاز حملات به اسرائیل خبر داد  @News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65418" target="_blank">📅 06:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65417">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووووووری
؛ انصارالله یمن از آغاز حملات به اسرائیل خبر داد
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65417" target="_blank">📅 06:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65415">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
با توجه به شرایط خاص مذاکراتی و همچنین آغاز جام‌جهانی، حملات ادامه دار نخواهد بود  @News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65415" target="_blank">📅 05:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65414">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
با توجه به شرایط خاص مذاکراتی و همچنین آغاز جام‌جهانی، حملات ادامه دار نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65414" target="_blank">📅 05:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65413">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b906cb3be.mp4?token=ZHVP8c4wqCH6Sq8y0QTkyziiTA9GB2zUS8YPWFxVzLduZfpnJAr7SqzEB1MfaiRKmOJBxkHS8uIerXyYkbgC95SeY1nKjMmS5fLcNjcparA0e3ZI3ZNwG_x_Lh1KkdWdaehDJ0x8MW2CqsTALTEIuNWpSsewn2sqWU_duYCJq-iQVHFQOy_0mcSw5j8OX_ibhMy2E1Xko70h7lcNfJ9kfQl5Px5bkLQjA8daWJCy_xXVuGa6gTvGTOgeMcSLmUm5GkYup6pfsfniKJM19_OGVg1BTB1snpPGn68dFy6or1taznpZL65b7CiEqoqB7k6kCsmGeTZIRxYzX2XrBlYmOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b906cb3be.mp4?token=ZHVP8c4wqCH6Sq8y0QTkyziiTA9GB2zUS8YPWFxVzLduZfpnJAr7SqzEB1MfaiRKmOJBxkHS8uIerXyYkbgC95SeY1nKjMmS5fLcNjcparA0e3ZI3ZNwG_x_Lh1KkdWdaehDJ0x8MW2CqsTALTEIuNWpSsewn2sqWU_duYCJq-iQVHFQOy_0mcSw5j8OX_ibhMy2E1Xko70h7lcNfJ9kfQl5Px5bkLQjA8daWJCy_xXVuGa6gTvGTOgeMcSLmUm5GkYup6pfsfniKJM19_OGVg1BTB1snpPGn68dFy6or1taznpZL65b7CiEqoqB7k6kCsmGeTZIRxYzX2XrBlYmOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
💪
گزارش انفجار در ملارد
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65413" target="_blank">📅 05:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65412">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
حملات به تهران  @News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65412" target="_blank">📅 05:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65411">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UA3i1CUw3EfprWaqyaO6PybnX9lwMmnAP6sXTxhYRdI_6GR8J2yjJvVGAZnaw6sTLUhU8aAvBd8YrFR39fUHeZ3jM8Rd1PcD_dyduQuWx5-9kxm4boMz-zTTX57Br3ErlbOfj_Kw2EersgXhEhYGbxZIIOWwjBp87Ipg4Fmfom7CI9SKzyLTpwQ4xD-DKsWMasYhZua6y4WYE6S0TDgSSiBJcVbAd4KJ2kJsBmkVhkBIbJNyzHI0IsFk2YuhbemufaxAP4M0B1EsNfARS8VM-L50NwopSINTMKvMzDMvjjcLeWgTS0E1TKRYa_SXSJFi_SSQCa5OYeCseerck0u1yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات به کرمانشاه  @News_hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65411" target="_blank">📅 05:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65410">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gegPZWZe_kgKMYRxTZCwfOTBN5yb0crzBSgKLjlvWfxrXlq-V59sIflsmnbIWtMySvsIiFRns5xCncVEJYUaEMsJCugZOMfnMTmr4d-tQaSMmyqs3JTkSOzIuaN_3mKWYbvZazqZ9cvCiEwYe3cifhy3-flbdzEzEU_F_SHJmcOWAqo2h82pzZhop30QCdaVn8SyY9FO1NIOzHU--sTVN73iTaKx7DKC6rZrHBQiFeT2ZzoECypVqwkP5ZB6Frp1WEFy27QrvbibrOP47ZoqTQU8e9VyeeFCCuG9EHFHr39HBo2p1KKyNmtVQJfa6Q5rxPNaOI77rP8d1R6VJNdkaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات به کرمانشاه  @News_hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65410" target="_blank">📅 05:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65409">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13951b2150.mp4?token=hW93ex46hi-HeNzI6qso0K0nudbLY_exyiVeGUe4fWj1exQB1RQn23awZ_MKMGbAxB4rJcqeGADJO_MdvuuM2XqtizfQyRZe9X7oIxL9G6E7Vl9XrCB2UOwer8auJUFVjZvWxMpW7dqwDPHga3hJPvOrV6AV9dwFTPwFbXBCiG2unKr0UCF2OoZIShCRrSsdUd3lKooWye3sIv0R7O472ITTZPfi6s0rYrWxLkiFgkEhbXCBlRNpebmi_3jagJDIiPWhhRmYy9PkWh0gjPbpELYw4Q_FGRMw1a2zg0lOyN0x1RosXB4FSPMJnlWxGKlQ1sRPaD7YE-DjMlgCQICNmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13951b2150.mp4?token=hW93ex46hi-HeNzI6qso0K0nudbLY_exyiVeGUe4fWj1exQB1RQn23awZ_MKMGbAxB4rJcqeGADJO_MdvuuM2XqtizfQyRZe9X7oIxL9G6E7Vl9XrCB2UOwer8auJUFVjZvWxMpW7dqwDPHga3hJPvOrV6AV9dwFTPwFbXBCiG2unKr0UCF2OoZIShCRrSsdUd3lKooWye3sIv0R7O472ITTZPfi6s0rYrWxLkiFgkEhbXCBlRNpebmi_3jagJDIiPWhhRmYy9PkWh0gjPbpELYw4Q_FGRMw1a2zg0lOyN0x1RosXB4FSPMJnlWxGKlQ1sRPaD7YE-DjMlgCQICNmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
انفجارهای متوالی در شهر اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65409" target="_blank">📅 05:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65408">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWvJJZ2fFK_K7tLHhKSbVwqGtapQjgNfVJrCWVTxnT5g23NpnIKckN6MM6bEGTvzr8qJQg4-lapoizc1_OrQc3oO_QbIVsrAndTbwH56PkY6nkB9pwlwexOdT5x-iQR_PHodjaO_A4wxSKrcpf7XWm-o_RuSXYUOhOC_qzZq-PDF1fNReYvxhQWP1alxPqnp8Ib9mN45rTUsxxr_AbjH6vXbbwur4GFfQAfPzzv0LhklsTp3TmFfkU97Xde7m0QqD3j4CAhLtYtolf3-emXG-VgdIoj8a7EM8Lv7RLvIp1EF0km8h1stmqi7mxViUQImpdGban5-jnolM1x2ay2arQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇱
نیروی هوایی اسرائیل اندکی پیش به اهداف نظامی متعلق به رژیم  ایران در غرب و مرکز ایران حمله کرد  @News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65408" target="_blank">📅 05:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65407">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r3i0V8mvuXZTJsI6jRbXTL3JW5LjS3LhQ8UQqfmJn6d-_BvTvu-5FjaY8zfqR7Rhm2feP0ItbE_XTjAEHN2FjBGi1hRmfiZgb4uKXTUBJ2I2F0mFE1SP7gXM-az7GY8Gn_QVeIosuer8hts_5JWR_-rkmSSmzSn3tAL1iAj0vJhfydnTkEoCoIClwQ7nZD5OzrozuVX36zfoHE8LCfKl94MeUNLrpmWoz0npl_7WabPCeMa_Fgm-R4wNMC-sr0lQKRHxuHbYxDcvTGpOJBuRByqRlqey8ZaPyJmUMKClg4HHhpt1ZYK5r4JCr-e18vzDpFfKKbEgQzr_xKvVVBlhiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇱
نیروی هوایی اسرائیل اندکی پیش به اهداف نظامی متعلق به رژیم  ایران در غرب و مرکز ایران حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65407" target="_blank">📅 05:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65406">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65406" target="_blank">📅 02:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65405">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rcDNm9TeGop8-QdjZaSmLcrTUuBF8-XmUjFP6IVaW4OuhM9YW3_RIr7VJIRVHLWN9-Jjo1kYCBmkDxU2J0PTspdwqxyETgNNenMZs8c0o6ZKEwDJDX-k6VsHAu-gbcfbT5zfWXzpOhSewIQpHcWfm0FQTiQ5aK2lBzIdu3kLYY4u6yEBjSJGLbUIcdFkNzapOGJJtaxq6xkXIt57LTK-F8Vov2skYP_11RCmrOnH9K5Oz-ewtrXmPZguLYmSJfIctw2MwKOUheUyZcCrXt84eai_31BM_ah18hI7RR1Tr-Pnaf_RYZa7pRjMydfTKSJHXxNf1VWwgMKnb3X_M6iO3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65405" target="_blank">📅 02:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65404">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-8fEM1juZoG-7tlMZrHflES7NoC8KedRsEcNwebzXoNvikmbGFPWPbqDnK2YMnVNkx0NjjalrPYKbQb804sYVwSpVOslZuY3Oxhmy__0DVMEFIM-thk4oSEvOhjj6mXMoEAXjbPjV_hONiDh3klB8zLvTgxbB7_qbW-8uXxpxS5qIps9hjVeLnn-YO2eNZABM2PuE4Glt4eRAVjSJ6HrF9wD6lH91Yzrsg6zZVu8kvCmN3dIyGFw6-y8FG6r4TBv_AsIGAD5SCdy8caICHSEZSUCZAOVLXpx2lNKw0RCqjbexNvLUBQDo9e3Lg5HgZfCGZ7eK_B_uXkqYM-E0muMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
مراکش
🇲🇦
-
🇳🇴
نروژ
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
یکشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه ردبول آرنا
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
مراکش در
۱۰
دیدار اخیر خود،
هفت
برد و
سه
تساوی کسب کرده است.
✅
نروژ در
۱۰
دیدار اخیر خود،
هفت
برد و
دو
تساوی کسب کرده و در
یک
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر مراکش
۲.۵
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر نروژ
۳
.
۸
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۱.۵
- ضریب:
۱.۲۷
🧠
وقتی از بازی لذت نمی‌برید، متوقف شوید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65404" target="_blank">📅 02:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65401">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: نتانیاهو چاره‌ای جز پذیرش توافق با ایران نخواهد داشت.
@News_hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65401" target="_blank">📅 01:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65400">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frombetcart - کانال بتکارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHt3tmSd0e5ae1nPSjlF4lOXadlSE41BSOhnQujsvSAHIWjuYOauWfn4UJRM3l0vZ-MyXPKjkxMu3lzriZVXhkjrqsPgcPligtB8azHzNQb9Z2vgNYTZGNiO06teZG6I0ohrN83Goa1zL3L5AdQTQhscx1KGa1dafW3PvbpZDKpd6tf-KoxztXp5hBVDc-bE1dXy_t4uZ2b2DmoW8dcvl5R5-jprtcK7LuTfhVRHM1oO5SR3Q1wk21LlBO72EECRjMCYLJ12_HFO1C1nPeEH17r7o-lWFW8a6MquHgCfeu8fliheyHjXk6FfSgeu1IsCjDlK6srq-J4SUXJvC_ljjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یه فرصت تاریخی!
💥
بزرگ‌ترین کمپین تاریخ بت‌کارت شروع شد!
🏆
برای اولین بار در همه‌ی جام‌های جهانی؛ جشنواره‌ای که تکرار نمی‌شه!
0️⃣
0️⃣
0️⃣
,
0️⃣
0️⃣
0️⃣
,
0️⃣
0️⃣
0️⃣
,
0️⃣
6️⃣
تومن
❗️
☄️
جایزه‌ی واقعی برای ۱۲٬۵۰۰ نفر
👉
http://bit.ly/4ep75qf
⏳
تازه لازم نیست منتظر بمونی جام جهانی تموم بشه...
🎁
بت‌کارت هر هفته جایزه‌ها رو مستقیم به حساب برنده‌ها واریز می‌کنه؛
✅
سریع
✅
مستقیم
✅
بی‌دردسر
⚠️
ولی یادت باشه...
این جشنواره‌ی بی‌نظیر فقط مخصوص بت‌کارتی‌هاست!
🚀
اگه هنوز بت‌کارتی نشدی، الان وقتشه...
⏰
فرصتو از دست نده!
👍
وارد شو و شانس خودت رو برای برنده شدن میلیاردی امتحان کن
👉
http://bit.ly/4ep75qf</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65400" target="_blank">📅 00:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65399">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
آغاز حملات اسرائیل به لبنان  @News_hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65399" target="_blank">📅 00:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65398">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
آغاز حملات اسرائیل به لبنان
@News_hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65398" target="_blank">📅 00:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65397">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل: رژیم ایران اشتباه بزرگی مرتکب شده، ما آماده‌ایم
@News_Hut</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/news_hut/65397" target="_blank">📅 00:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65396">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
ترامپ: نیازی به پاسخ نیست، صلح نزدیک است
@News_Hut</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/news_hut/65396" target="_blank">📅 23:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65395">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🇺🇸
🎙
ترامپ: به توافق با ایران نزدیک شده‌ایم و نمی‌خواهم اکنون در مذاکرات اختلال ایجاد کنم.   @News_hut</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/news_hut/65395" target="_blank">📅 23:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65394">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🇺🇸
🎙
ترامپ: به توافق با ایران نزدیک شده‌ایم و نمی‌خواهم اکنون در مذاکرات اختلال ایجاد کنم
.
@News_hut</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/news_hut/65394" target="_blank">📅 23:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65393">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
باراک راوید: ترامپ بهم گفت الان زنگ می‌زنم نتانیاهو و می‌گم به ایران حمله نکنه
@News_hut</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/news_hut/65393" target="_blank">📅 23:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65392">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ: حملات اسرائیل به بیرون هماهنگ نشده بود؛ اصلا از این موضوع خوشحال نیستم
@News_Hut</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/news_hut/65392" target="_blank">📅 23:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65391">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
باراک راوید: احتمالا اسرائیل پاسخ خواهد داد  @News_Hut</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/news_hut/65391" target="_blank">📅 23:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65390">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
باراک راوید: احتمالا اسرائیل پاسخ خواهد داد
@News_Hut</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/news_hut/65390" target="_blank">📅 23:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65389">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
📰
فاکس‌نیوز به نقل از ترامپ: چیزی که به ایران پیشنهاد می‌دهم؛ موشک‌ها را شلیک کردید دیگه کافیه به میز مذاکره برگردید و معامله کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/news_hut/65389" target="_blank">📅 23:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65388">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ارتش اسرائیل: تموم شد بیاین بیرون
😐
@News_Hut</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/news_hut/65388" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65387">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
ارتش اسرائیل: تمامی موشک ها رهگیری شدند  @News_hut</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/news_hut/65387" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65386">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ارتش اسرائیل: تموم شد بیاین بیرون
😐
@News_Hut</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/news_hut/65386" target="_blank">📅 23:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65385">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
ارتش اسرائیل: تمامی موشک ها رهگیری شدند
@News_hut</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/news_hut/65385" target="_blank">📅 23:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65384">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
وزیر امنیت اسرائیل: امشب تهران باید بسوزد!
@News_Hut</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/news_hut/65384" target="_blank">📅 23:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65383">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d76423eea.mp4?token=RJcCouP5LnDHhDYDYYA5TbmQ6xs-uujq3K4d3h0NfVkADxYGUxhsBzTRl1YYvQqXmr1mPJm_WZMpTZkUZgehZiLkZ_EmDS3JHngLkk-vgh7hbqq6seOACY2-rFfzhgWM2YSwg4H5aWo4K9cwDN5XLlIw4LlRM9JtFuINop7d4KeuhRL0FWxu1gMamJ3hykujbvIPEzUsYFdndyLUx6CQCvKJYk_sLsIZ4HvwGpRjial8iA_ItVJgKz8bq8UKuAhYy55ZwWxIgMz8GNzVs6L-C-HWA_HJKmm_lVG5AkQx_14iaAvmmWmTtERK5nMjm29rZhIB7d-Xu5DlN0RdTLmnIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d76423eea.mp4?token=RJcCouP5LnDHhDYDYYA5TbmQ6xs-uujq3K4d3h0NfVkADxYGUxhsBzTRl1YYvQqXmr1mPJm_WZMpTZkUZgehZiLkZ_EmDS3JHngLkk-vgh7hbqq6seOACY2-rFfzhgWM2YSwg4H5aWo4K9cwDN5XLlIw4LlRM9JtFuINop7d4KeuhRL0FWxu1gMamJ3hykujbvIPEzUsYFdndyLUx6CQCvKJYk_sLsIZ4HvwGpRjial8iA_ItVJgKz8bq8UKuAhYy55ZwWxIgMz8GNzVs6L-C-HWA_HJKmm_lVG5AkQx_14iaAvmmWmTtERK5nMjm29rZhIB7d-Xu5DlN0RdTLmnIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات جدید از اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/news_hut/65383" target="_blank">📅 22:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65382">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kw8wSP1u3_p1uEFWfeqAGQaAqJpKH7EXvvqvxTdJbKP3CmayTOLHeI063mMw4B1vM_IxAOHeutSJBMkJTi8ziSTYilsoP1r5VvQGgX9IstJ1iWCEEPtD6BG6c-EMkyMmuOs74B5jIGQrsiE_JUrCmmfo-2WkywT-8q4eNAGkaGmzrR4XKrV-xV5uY4pvIV7zh2hz62-2NHZO6tNT-CfBDH6sqtvW43kivxL5nqzeVsDZ_1Bj2DfviAluC3jCGh3e14Xdnxu7rm5vlktj6P7NZepJuG6bo3S5xtdrWkfUUFH0kl-SvZoTZYk8xgXXGkDBprYHYor9zOmXmKRg-ZcD-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی سپاه به اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/news_hut/65382" target="_blank">📅 22:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65381">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
📰
#فووووری؛ خبر اختصاصی ایران‌اینترنشنال: سپاه پاسداران آماده‌ی حمله به اسرائیل است  @News_Hut</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/news_hut/65381" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65380">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
گزارش غیررسمی پرتاب موشک از کرمانشاه
@News_Hut</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/news_hut/65380" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65379">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
📰
#فووووری
؛ خبر اختصاصی ایران‌اینترنشنال: سپاه پاسداران آماده‌ی حمله به اسرائیل است
@News_Hut</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/news_hut/65379" target="_blank">📅 22:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65378">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/asIWLaRYKIGB9o-HlE598HXYic5Kr-QCwYY-ma49XFGxXARMqinI5nw3oImDSPzk6ohprb7BqLOe3j3VW4N4LSzGMtJJA73Bw3Mg5vA2y51XcVE0Up3iQ3uDOyJaZk4eFoKNady72dvKuaE22bRTa_fZ1mfYhLP2OLZM5xersFMG3VjQkou-EwZvRYBDxIZ8xX5I-luHhxFgZ4hGPb_vov962dNYpBF807UWi4ZyVgcztKFGFHHIh0SR3f89ynf-fBysPnslp4UyuGokliuHz7bkiJ7Q4RvswXpMa9x-1JiBZhxNKabe4Qb_uT9kWDLkDk3h3zd01EEp-P5ibD3IkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پرواز تهران به استانبول به دلیل حملات احتمالی ٫ مجبور به بازگشت اضطراری
به تهران شد
@News_Hut</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/news_hut/65378" target="_blank">📅 22:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65377">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65377" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/news_hut/65377" target="_blank">📅 22:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65376">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrcdozbgLgRVPwmrKw7yPJRryJYtCN4AG6hOjGo5TvF5Kk0zI523szeZphkEpuYDFmEwEYnhVxoGyMB5zmeXhCmXVZxdhAv5Hs9ZM7KqfaSSrYZrNDf2GDrhQS03VlhHvEmC7m_78lATaNev2tTmQshVmD9fQrMgZsOgQZfhKeq-efakOqrkRorUbVubuz3Eor4KfsL3ddamdUk4IDOc9KKPpi3XO3MGMRTNp8C08pZff1V6m_hgG3NL3vsGtQPKJzpBOpP3rWByhmE9eJRk-rPyD5vxABzk02SeNz0-U2ImEU3KOwN3tOOIaHdjthGie-sLiE6PnQIhI4g1vhWf3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/news_hut/65376" target="_blank">📅 22:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65375">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/BeRbT08Jv8TY8FCnEasfbu_g3V1TJW83rt5vqVyXucTUolAYWzTH1FCzVpW77RZqdFZrl1PJppKzW5TBbwdxxn4Fjy_JvrF6YnnB1QIFLLeGOV7IM-Qu-tF7KZcedeEMSqPAzbfdo112BE94lfFPhnWRdClu9mFe8GxaCvusE4VKMwjpapjtgkFnNcJ-GXS_Bh_Et_wVgTOPSV5sqa8HQVvnZe3y3nFRoU7GiLAFzLtXMFrzYSuOdIA8HzTrLNBRgXH9Ua9SOIEpqDOhXlqltusa_R7CRdqED2gnaXEqyP0TrOvjCJcQ-H1wzCR3D0XJdTG_vhvXVh4iERR8Xv7GJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
د اتلتیک: نزدیک محل اقامت تیم انگلیس درگیری مسلحانه ای رخ داده و 9 نفر زخمی شدن!
@News_Hut</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/news_hut/65375" target="_blank">📅 21:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65374">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پشمامممممم؛ اریکسن وسط بازی دانمارک دوباره قلبش گرفت و سکته کرده
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/news_hut/65374" target="_blank">📅 21:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65373">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQKn-GtgpxrpooK3bz7_xDEL6emhBwaDP2_5aO_2LoK1m0dhR9mvPQQUSCcS-xk4oXCQZqT48P4sjLmd43cIgVbJkPGNkX2Y_ipSIl_a7N_E5_kJbXgQUELVfCkmQ1jFlqrKZjPntsFe6sycPAWPTi7qMbR-IhI3AAcqjFa34reXsdowJ8jQDwtL-Zc4fubwlMVsabwh1VKpnSr_W9e5ik429JcC_b9JMDjy8n7Pp7jNaZuP_9KuR5q0GOmx6ViROLAUCGpKX13sJUTk568Ub1uNsapWZxhT6dM7Q34Oy5HhlpY6ifdHWiMXrwk8siS3OyaEwzZ7en_vDMttmAWN5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ: ۱۰۰ روز از آغاز جنگ توسط واشنگتن و اسرائیل گذشته و به نظر می‌رسه تلاش‌های ایران و آمریکا برای دستیابی به یک توافق موقت جهت پایان دادن به درگیری‌ها با پیشرفت ناچیزی همراه بوده است.
همزمان، وقوع حملات جدید، فشار مضاعفی را بر آتش‌بس شکننده فعلی وارد کرده و دستیابی به صلح را دور از دسترس نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/news_hut/65373" target="_blank">📅 18:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65372">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دونالد ترامپ در گفت‌وگو با شبکه ان‌بی‌سی نیوز گفت که اصراری ندارد لبنان در توافق کوتاه‌مدت میان واشینگتن و تهران گنجانده شود.
‏ترامپ گفت که به‌عنوان بخشی از هرگونه توافق، دارایی‌های مسدودشده ایران را از ابتدا آزاد نخواهد کرد و هیچ تحریمی را نیز پیشاپیش لغو نخواهد کرد.
‏ترامپ در پاسخ به این پرسش که آیا این اقدامات پس از توافق انجام خواهد شد، گفت: بله، بعد از آن. اگر رفتار مناسبی داشته باشند و به تعهدات خود عمل کنند، آن وقت گفت‌وگو را آغاز می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/news_hut/65372" target="_blank">📅 17:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65371">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65371" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/news_hut/65371" target="_blank">📅 17:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65370">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qabe7FDBti2E5ig5tLeUb4N7t9uwa-iCrIjYF5VrkpjsNjDKpDg5PUnAAF3qkFWf7FQ8_9Rk0cDikujZRqMCWWETfkZ5AH9pe2doEA3eB7y04-ypH--D4udA8MsanosqzzTChup2pjv5nfD5oPiOU8v1BB3gEnRv2ULS7jfr9TxFgF_YCddmGuwcBOHYmM9FYYeZ_Yg8fSyHI8L0PH4xvxMqdkV7Xlo7awZDn97r5ulDd3OA0h3MJ3esh_5u5UnCWaXkzEvkoJnSv5Y7lmxs56bzNf3QfwufCKwaEp32_EEZL_BVdTyRAkdxe90kjwJk4yUHb1hAXtt2Hu9t4JCH2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤼
روی مبارزات با 1xBet شرط ببندید و شرط بندی رایگان تا سقف 100USD دریافت کنید!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/news_hut/65370" target="_blank">📅 17:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65369">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: احتمالا بدونیم مجتبی خامنه‌ای کجاست؛ اون از پدرش عاقل تره!
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65369" target="_blank">📅 17:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65368">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
صدا و سیما: منتظر واکنش قرارگاه خاتم باشید  @News_hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65368" target="_blank">📅 16:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65367">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‼️
محسن رضایی یک‌هفته قبل: اگه اسرائیل به ضاحیه بیروت حمله می‌کرد، آماده بودیم شمال اسرائیل رو تبدیل به جهنم کنیم   @News_Hut</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/news_hut/65367" target="_blank">📅 16:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65366">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‼️
محسن رضایی یک‌هفته قبل: اگه اسرائیل به ضاحیه بیروت حمله می‌کرد، آماده بودیم شمال اسرائیل رو تبدیل به جهنم کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/65366" target="_blank">📅 16:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65365">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون ضاحیه بیروت  @News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65365" target="_blank">📅 16:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65364">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L-lBQICoFGusAqBroZXCDf2DJPGS7MY0VmrhQsyHHIGqa8oXQIY-A5YhCHUUlohaL8UDQwX98D4fDvNRwkJBaaLPF7vd9rpm2QfpfKAUK6O4rtgcPJVBANxSbhSpaRJqeE0mvCv0SVeDY0dRYr2MXsUpQF8Uyd2uqimZHmo7DbwA4XczpIvqeYlzKhhdj2OOa0NjCaOn32Y-vlk44KgP6OGveIM8FYIt6EI2rcVQVXrS0V4UeJYYC4e3zmWe0z3AYfyrXaFGYOiRyXWynBvZde9LbAycvPr_PWLO7L6XLyknZcKMb_VJnOvgCsRe8p97LLzcZVcvZQPi2Lhg7h8Jiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون ضاحیه بیروت
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65364" target="_blank">📅 16:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65363">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛ اسرائیل رسماً به ضاحیه بیروت حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65363" target="_blank">📅 16:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65362">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGL_RAkMaJtjoxyZmNig6Ye5rFK70-BEFwc7P0BTfWOskwaSrsuNfMyg_3GMXb1ZH4aOyGN9PRF61EhVYXklbrPzaD23J0lpTOmoQPDEZIks_d156KO-eMGtwPCoW12nCx8QbG0VS_DgXgeQkDt37otinKYOF30TlIBeGMQra9OMnXm1zrzqZsnv_iwkjaIypOSWrNaWwYYoGM5kdNoAfLzlFu0E6sF2gPVqJoK1PYjDmZJSyqi0JfZutng4pxmAjsXXrcANbyvaderA_QqnDkUrlbAzfHkc3bnjkD_nSpKpD6uhifwMQmkDlPFap1YYQ3815Z3GqOmr8VUAwMo1Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وکیل امیر تتلو:
توبه «تتلو» از سوی دادگاه پذیرفته و برای طی مراحل نهایی پرونده به رییس قوه‌ قضائیه ارسال شد، ولی هنوز تصمیم نهایی اتخاذ نشده
اینکه موکلم برای ماه محرم درخواست مرخصی کرده تا بیرون از زندان مداحی کند، حقیقت ندارد
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65362" target="_blank">📅 13:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65361">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55cb33d933.mp4?token=bMlkyRnoIi7-41K95GCjFhYyNYgFKnuqtUkn1Ionse66VTW2MEAccDqvakRiapZiNMQFgUxiv1ROQ3yEp2NaF27ucAMwE4a_M2I7naAGxVLpOKfu5Iye6bbO3UI7E6y5ik57S-9MmJW8e-YSAaTk54k1EWyj6DXtBX6twW1gXU_gKqjlIC3vrpkj3eJOIcexrspVlOjM3ImMpdZHv3NEY6dZogGdNM6iR46Xbx49rG5IsqqQnYelIJH15EAvVgyFpuv2u3pIWqC7ZxuFdbJYflmo-zQWHv_yIOCVW4VfP16yst1XYhVkPEQQTJ2rrORio05ru9nH-083A306rKUMhHgeMQ7xJ_W3fvG46JWE5GD6eprZXMBc9IUoUtbCMfLw5yZsllI8dF8y8tUgHLGLa7-5nBwvidTVvscA7I6kYUKAFvqEvn9v93ShJVr37E8e5ynrcJtW875RLIUfNB4NhyZyZlZq-6nBilkd5Gb13crqhMNWl19_nz8nKQpGgm6DcBBs1LaLY6fWLipPIBHC8aTQDJqQOINzBkhGctyBKN5HFSdNCA0EVXPzUm5biu69z5T1-HZEkVprIcJvExt3KCt5DPxHzAFwrrTx5_NOvx_2QbLbS81r-ZwaJXmL0lENAYA0HDoSUY4TAx-pOUscEkW_kLJvRJT3nh_4zS7fxe0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55cb33d933.mp4?token=bMlkyRnoIi7-41K95GCjFhYyNYgFKnuqtUkn1Ionse66VTW2MEAccDqvakRiapZiNMQFgUxiv1ROQ3yEp2NaF27ucAMwE4a_M2I7naAGxVLpOKfu5Iye6bbO3UI7E6y5ik57S-9MmJW8e-YSAaTk54k1EWyj6DXtBX6twW1gXU_gKqjlIC3vrpkj3eJOIcexrspVlOjM3ImMpdZHv3NEY6dZogGdNM6iR46Xbx49rG5IsqqQnYelIJH15EAvVgyFpuv2u3pIWqC7ZxuFdbJYflmo-zQWHv_yIOCVW4VfP16yst1XYhVkPEQQTJ2rrORio05ru9nH-083A306rKUMhHgeMQ7xJ_W3fvG46JWE5GD6eprZXMBc9IUoUtbCMfLw5yZsllI8dF8y8tUgHLGLa7-5nBwvidTVvscA7I6kYUKAFvqEvn9v93ShJVr37E8e5ynrcJtW875RLIUfNB4NhyZyZlZq-6nBilkd5Gb13crqhMNWl19_nz8nKQpGgm6DcBBs1LaLY6fWLipPIBHC8aTQDJqQOINzBkhGctyBKN5HFSdNCA0EVXPzUm5biu69z5T1-HZEkVprIcJvExt3KCt5DPxHzAFwrrTx5_NOvx_2QbLbS81r-ZwaJXmL0lENAYA0HDoSUY4TAx-pOUscEkW_kLJvRJT3nh_4zS7fxe0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با زنده شدن دوباره دریاچه ارومیه هزاران فلامینگو مهاجر بعد از سال‌ها دوباره به دریاچه برگشتن
😍
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65361" target="_blank">📅 11:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65360">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZcZVouJ1EXlnQooayhyo-dh32Hga9Xef7_WZip0rghbA1FAiIG_UwqBWdsdA9B9j53OImfpgpIYIyTtFTJdG_IORHuOOYrmQRAvu2k8r4p_Od4DQGu1Lg2nPQLhc4dWhVyS39727HP4h7QSzGiPQDG_GDPBPX9B4pCRvlDbao_k0_a7DWvbJZF38O33HYTokYHNaFfh90UekH4bbr4k0y1OnL7jtYkH9nGicrCcmvg2fOxLxDGpPFAN4hp7Bzzi-0t4qRQim2GrpQWrgRiaDNXvjKNB9FZCOLGxv-TrXV0zuEjeguGPbEvl0bIBJvrBWjbFqP3whZ_Q8bULmt9p_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز خوبه خدارشکر بعد از این دوتا پویان مختاری هم برگرده جمع نخبگان جمع میشه
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65360" target="_blank">📅 10:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65359">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeyjHQcS3AIAizuoXx7Q3KkvRkcUoIa6RoOsxrV8qmr8NUlzgI6bh6QzDSt45ESwoH9swmkFieDwHVkte49BntsCccEU8ckEhMd_kwMR-ToM01p-Xp8dvVXOnQNoiQLf8hmTTIZdftxTtdYgX0qLvgtWroBVMcDQ_zPzgYseRRNEoxFYbuqQpCVeldaL9TVYzLuB2fwllE9YeLJBtHmiHbbv2YbX2NgfQxThpmqky0o5ScqI5c7Cb5j_87jsKfquH7f7jAluU56XChls_HC6W8zENra8HUNqz5a7IbhGGRWrXam8gVkrZOLVkk0B8D1C9i3h5j5erPktttrec88uhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش یک میلیون تومن وجه رایج مملکت از سال 97 تا کنون
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65359" target="_blank">📅 10:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65358">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884f21c214.mp4?token=OkY78PLRtalNJtF9GaIRck8lWV6GN6aeaPArpAoqIEvTKDYEMr55uCfXWOZEI1I5udO02_cXZdBP07IUfIsW0PDLwHeA8IcE8mMmcP410-7F9RMBOrYUaWO33pyNe_toNNmzs-M_KQlq7FYmUeJhRoYKxAU8QizcTPQi2IF0iL2k7KpXVayjsHBmGNS0McbDZf3YZi9YFtcfHhfamN2kf9istQVgKJz6GP6YHTLwqoA9yExf1-SVqUacGu-aJNLzDV6PpN0v1lK3wTyibnF2faGdfLqhz8fYMr6bXyHEiqQT-gBHwn11nzgva-WTxm-td2gM133CewD-xRaU8Fi2og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884f21c214.mp4?token=OkY78PLRtalNJtF9GaIRck8lWV6GN6aeaPArpAoqIEvTKDYEMr55uCfXWOZEI1I5udO02_cXZdBP07IUfIsW0PDLwHeA8IcE8mMmcP410-7F9RMBOrYUaWO33pyNe_toNNmzs-M_KQlq7FYmUeJhRoYKxAU8QizcTPQi2IF0iL2k7KpXVayjsHBmGNS0McbDZf3YZi9YFtcfHhfamN2kf9istQVgKJz6GP6YHTLwqoA9yExf1-SVqUacGu-aJNLzDV6PpN0v1lK3wTyibnF2faGdfLqhz8fYMr6bXyHEiqQT-gBHwn11nzgva-WTxm-td2gM133CewD-xRaU8Fi2og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از طرفدارای حکومت تو تجمعات: ما تقریبا یک ماهه تو خونه دیگه غذا درست نمیکنیم و طوری شده فقط میایم اینجا میخوریم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65358" target="_blank">📅 10:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65357">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🌐
آفر ویژه سرویس های VIP
✔️
🙂
Standard PLAN :
🔸
10 GB
➡️
90 T$
🔸
20 GB
➡️
160 T$
🔸
30 GB
➡️
240 T$
🔸
40 GB
➡️
310 T$
🔸
50 GB
➡️
390 T$
حجم های بالاتر از 70GB  گیگی 6,500 هزار تومن
💵
نامحدود PLAN :
🔸
ایرانسل و رایتل
➡️
450 T
🔸
همه اوپراتورها
➡️
730 T
⭐️
تضمین کیفیت تا آخرین روز
🖥
⭐️
تضمین اتصال پایدار
💯
⭐️
تضمین قیمت منصفانه
💵
⭐️
پشتیبانی سریع و واقعی ۲۴ ساعته
🔜
⭐️
مخصوص نت بین المللی
🔒
🔖
قیمت همکاری همین آفره
💎
🔴
@MAMADXVM
CH :
@proo_V2rayng
CH اعتماد :
@prooo_V2rayng</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65357" target="_blank">📅 00:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65356">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65356" target="_blank">📅 00:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65355">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BcKqHhnUNvrRAHTdsCdcGnMDes9-vX8oHMcswfofKxy_Q2bWRTNmpSDt-vqQm7v_JoLcANJaobo5aells5EK-lI2IY5hJccO-h3_OAshQvhRxt56VXAK4T7Un1ys-lbeh1BN435UyRzmrpdYfJ3JrufZL9diN59sSlqY_uTfXDZiE-hdLN0mLZhkECMAyceOUBeI-oVNbf4SVoVg3iQGB-4gHkpq9cPik8gJx3OeXmAd7kLw4Bdj61ZnAe-esrzKz3XJC99_Y8yMFnXW6BAsiXFDeL5-0TbiZMfAmcx4KySweRVGf9uivhZD-4QfFgj8rDcnQ6FX-_Ivm8qIj-IAaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65355" target="_blank">📅 00:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65353">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf1fba69e.mp4?token=AI9u9DojdLPwmQ5S_YfwmKl6O-yV676YN8hVyDWFAmWrL6Bx42qlslih2gbeSfk57wmK9oHfaHtYxXmBqXbjsGR45nn11g6wNzSFlnuepm2bXmHyXx6_hx75uWGbNfUVDbRFstVpZ7mJXhw-8ShclkWWLLK0tKj1UoNluGGPd0QEzJej9hS6Nd94fPHZU6LYDiWQZ8VkrTwk4rX6CexIAtSLoHUV5tT29yX3UlFccm9f60ldnAHBDMu9qO5o7f-Y-ufRD3tKUUG72-gD0SovicEIrBV-3wSbBU72wyzLL70bSRcsOPG86va0VYhIZq8ntdCl1DC8WXJygWOe0jhwlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf1fba69e.mp4?token=AI9u9DojdLPwmQ5S_YfwmKl6O-yV676YN8hVyDWFAmWrL6Bx42qlslih2gbeSfk57wmK9oHfaHtYxXmBqXbjsGR45nn11g6wNzSFlnuepm2bXmHyXx6_hx75uWGbNfUVDbRFstVpZ7mJXhw-8ShclkWWLLK0tKj1UoNluGGPd0QEzJej9hS6Nd94fPHZU6LYDiWQZ8VkrTwk4rX6CexIAtSLoHUV5tT29yX3UlFccm9f60ldnAHBDMu9qO5o7f-Y-ufRD3tKUUG72-gD0SovicEIrBV-3wSbBU72wyzLL70bSRcsOPG86va0VYhIZq8ntdCl1DC8WXJygWOe0jhwlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نیکزاد، نایب رییس مجلس: تنگه هرمز طبق قانون مجلس به حالت قبل برنخواهد گشت، تنگه هرمز برای ما از بمب اتم مهم‌تر است
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65353" target="_blank">📅 22:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65352">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
صدای انفجار در جزیره خارگ
تسنیم: خنثی سازی مهمات عمل نکرده دوران جنگه
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65352" target="_blank">📅 21:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65351">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZ2hz4IsUwE8P41uQVwwDlRx-N1GUGFWMDcr_dHg0LtSLEgdjN_fzeVze0NeVfpRZkunv60wC9a-ub-X3zoRf9KQIg7EyJpKoGOYhvj9mVCX2WPBkbaPOlKQhni_pcLGW_N9iPiFZ7dX-tI9J0q_TL4KyaXGlxteThTF_-wAjRxnr_BLLbqzXYqv9IHMBv_820Bs3ZJTOhDOKGlXDaksp00qvq_55vHan7LJWBqwt1db16pnjOEPPMsi52j0FyCtM3VfoJQlTcJ1WhOAHOJpuJ-9M0M6ETrSQ8LpT5BEo0lVV1DkY0mc6sKgnL2v16qDrrGu-YuA-IVXZSAtGzpyKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ تو تروث‌سوشال: کتابخانه باراک حسین اوباما، در ۱۰ سال، وقتی کاملا به بلوغ رسید!
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65351" target="_blank">📅 21:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65350">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/457010896e.mp4?token=G7OycO3-yeruLfN67ruhDrgBlxFF4bFC22dhxIIY7pFn0VM0FYJTE_sjKHaVYDH-6YH7pZPJrfU9eVvMT7Omp6dwoc5icvD8JYosT3VqATLCStxl3T8eKIa7FolHbwZPFHsgkMIVsST8Zfr6dQPFpx19sJyv54EJDxXTqbPDaa-NygPzuiA9Q6kVMQAmADVQoEoJjOU1eLCsSTOLFzwO9EFWynJDOvvqeCzt67Nyeec5Kzzx40S5Eg3rtYxx9E0-p7eSI2H3Bz1kwfTEnl8Oltsfr0MrB3aBLBoX5hE4vdTVlZIUEmSFlQHvGRvOzRmyKuaj2Myo-Xw1_DO9NVfs3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/457010896e.mp4?token=G7OycO3-yeruLfN67ruhDrgBlxFF4bFC22dhxIIY7pFn0VM0FYJTE_sjKHaVYDH-6YH7pZPJrfU9eVvMT7Omp6dwoc5icvD8JYosT3VqATLCStxl3T8eKIa7FolHbwZPFHsgkMIVsST8Zfr6dQPFpx19sJyv54EJDxXTqbPDaa-NygPzuiA9Q6kVMQAmADVQoEoJjOU1eLCsSTOLFzwO9EFWynJDOvvqeCzt67Nyeec5Kzzx40S5Eg3rtYxx9E0-p7eSI2H3Bz1kwfTEnl8Oltsfr0MrB3aBLBoX5hE4vdTVlZIUEmSFlQHvGRvOzRmyKuaj2Myo-Xw1_DO9NVfs3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با وجود مثلا وجود اتش‌بس ارتش اسرائیل اعلام کرد که در طول آخر هفته به حدود ۱۵۰ موقعیت زیرساختی حزب‌الله تو جنوب لبنان حمله کرده
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65350" target="_blank">📅 21:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65349">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65349" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65349" target="_blank">📅 21:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65348">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3H5Ll6AK00fldA5Xo9nkhGQITLwG4UPDu42V3R5cPKEVeSt8Qmkl15ba9bqz4JgBi2NlsefA62Ch6_bRVims7h4qtMx-w9XPpc-bZD3S0hAcflKcvstq_ZG6Pqr_yK1LdvjPAr5XYE9JnhO8rcTYMV69vczvGLmgJLOxhJKOMi6NjHCstnzkD6WbHypkqXccqwDAmfChsjBaFHKyZu-nJfYZAgJeE4IUN0BfXKuiQ3fBlRycIREKrwxdRSD6cnyivBImU745YgVFrlFS-Ud5ptcu80zTMAa56cDlDUSu0j0pJ1rx8MvEYWQuu8tqbZfUVcbOpe2cfxDjBm6BOv2AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65348" target="_blank">📅 21:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65347">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6388d22ab.mp4?token=nWBHIyxezB8G0OdKi-ouSweaVCeUQmchrMAhhJVqzFMskCSo-nVwvS54xBy84p4iuImF1KpuWTbe1bFdRSYqceUt8yLIL7GC9up8aWD5B7-TW6-cpLAOw24Nr8ULUs6ER-1UQb8aS2RULeMVZtWHZsy5DMdfdpwt7SRfLX0AUC96gbChtGj9_sHZ5Yp4Yz6Sohx7KH0kN7g-yBKpiuXh-VkaQ3cr27_pHO3nrVKtUkPHS8BnXs7dX3GgzGGQeTwRt6AAOLiA3IeZfhU7NZuAFC7ZnGacwWqJ7FNk6-WEi_uwVVTE2BmBAikElB_B0ZO4nF1qrUkRxTnTegPt31pqzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6388d22ab.mp4?token=nWBHIyxezB8G0OdKi-ouSweaVCeUQmchrMAhhJVqzFMskCSo-nVwvS54xBy84p4iuImF1KpuWTbe1bFdRSYqceUt8yLIL7GC9up8aWD5B7-TW6-cpLAOw24Nr8ULUs6ER-1UQb8aS2RULeMVZtWHZsy5DMdfdpwt7SRfLX0AUC96gbChtGj9_sHZ5Yp4Yz6Sohx7KH0kN7g-yBKpiuXh-VkaQ3cr27_pHO3nrVKtUkPHS8BnXs7dX3GgzGGQeTwRt6AAOLiA3IeZfhU7NZuAFC7ZnGacwWqJ7FNk6-WEi_uwVVTE2BmBAikElB_B0ZO4nF1qrUkRxTnTegPt31pqzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پخش دیشب برنامه «خیابون انقلاب» بخاطر این حرفا لغو شد.
ما اسرائیل رو تهدید کردیم اگه کوچیک ترین خطایی کنه میزنیمش، الان لبنان رو با خاک یکسان کرده و ما هیچ کاری نمی کنیم.
ما همش الکی تهدید میکنیم اگه فلان کارو کنن مام فلان کارو میکنیم، خب چیشد پس؟ یه بار به دشمن نشون بدین که ترسو نیستین.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65347" target="_blank">📅 19:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65346">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYs0Xqkme6lQda9Zd4f0A9VJo2KC9Y6mHscCQpFzZA1qKWdP65mmy9BFblwVwzPHrF6hl3jh-yE900eS4HfzQgWHBouPLbVnYui4mamMwfPoevCIc8Kjc1GMunXw1zEjpzTQQtUAU5lSZXdLSFsvtznMLgy6LjCg_zbpDIMHvSfOJ8z3a6970Axv_j5fybLRCqT1GWCkMsn1W3m5NFZiQFKyaJgelsZh7-J4v54OUMIQ_HkcTvBlwu2zG_kQyTnUOyMo3qONgHoASbpUs2FQ7x0peErnPqry2zQsGgthHfIie7cWuo3XWrb1rhqr1q_gS2osNRlZaA4C95usZlLV7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با اعلام وزارت آموزش و پرورش رسما امتحانات نهایی پایه‌های یازدهم و دوازدهم، به صورت نهایی و حضوری از تاریخ ۱۳ تیر برگزار خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65346" target="_blank">📅 17:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65345">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70f4e56d3b.mp4?token=VT5mVutuB_ytfUlDAAyp5b5h8Q3v7vytPZuww0KFwaqLjnfdl0gXhcFVRFkqgBcd5Lx6fzsL_XRASXOOY2qzNzdaCNFw5NBrR9L2U4rwFs7Tghf0j2NQvSpx7_dQ8t0s0cOXIACMbnbm8_cqkCNubkeU3oMP6Cd1kkXixZgZDKfH89Lqpw3YRz3U1kkE5XC9G-nxcA20xMQl-7p54bcGxV6RibSvhYNZPVaQ-42ILGbdSGB666Bdrg5IAG0cs6q7t19kqk86YyE2XoUOxK4R5GN5bQH6fFiuaFUZp5sBETFFUpjkTCi22YXVLZSfk0e5EXLoBL2Ju3cUtpoZaNuCYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70f4e56d3b.mp4?token=VT5mVutuB_ytfUlDAAyp5b5h8Q3v7vytPZuww0KFwaqLjnfdl0gXhcFVRFkqgBcd5Lx6fzsL_XRASXOOY2qzNzdaCNFw5NBrR9L2U4rwFs7Tghf0j2NQvSpx7_dQ8t0s0cOXIACMbnbm8_cqkCNubkeU3oMP6Cd1kkXixZgZDKfH89Lqpw3YRz3U1kkE5XC9G-nxcA20xMQl-7p54bcGxV6RibSvhYNZPVaQ-42ILGbdSGB666Bdrg5IAG0cs6q7t19kqk86YyE2XoUOxK4R5GN5bQH6fFiuaFUZp5sBETFFUpjkTCi22YXVLZSfk0e5EXLoBL2Ju3cUtpoZaNuCYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این وسط یه آتش‌فشان تو هاوایی امریکا به شکلی آخرالزمانی فوران کرد
الانه که تسلیم تیتر بزنه کائنات انتقام مارو از امریکا گرفت
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65345" target="_blank">📅 16:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65344">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hawyxom8LBhYoSNSzewBM3Eh7AcyQV9NfsO2Ikw-83qG5LB-5yx39d4GIOTRxhJshOX7fd3dE932bh0MV7BJ-Esj6HL_U1wpAu7z08heGx9RctVB5fyt_o6dWOj3F-G0snB2tjtHGOLDW3EjLSThLyZarAGUXBHQsyKvHrhEZBU-mzULtMKOLGHNBexBSxI_LTL9yl99nhvlYtkHA6TaRC5oJHSxUIul5WgGX9BBmW7YMmNLdIKg2omTS-gCzwcckDJBxuNpr7AfSsIAUQ5ROdkP838jSHj-givMIcLuLloUaufHM5P9qXALAuQeiJZPft5I7kpXUEOCNw1gULGAEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جمهوری اسلامی پاکستان به دلیل فراخوان اعتراضات مردمی اینترنت منطقه کشمیر رو قطع کرد
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65344" target="_blank">📅 15:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65343">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01c119656.mp4?token=JgW6LsC9HWjMRVLuccYn9bauy1kNxJuCmawFKNhlR4cnxivxcM8q7PfzGl34JrNkUAY_vFZtdt7iNmrhhzTUqNGOOKL2eOAzQUl-tlnDTwWL11zydIQtUhblnT-CYtdgWN-E34hCuFF0V3u4wLT3lj8KNyFnUxsjctHo5zdTbdwOOiAv0s-_cTQXJR74_bf3-lNEaSFO3ho6MDr0KLkLzo5MzEy8LdWMv1558NrByUpMaONw8nlAjZjHr3O-MuANVwza-O7sUEhkCJ41yGz81BiJbyL3ZhMAe369B3vA5Ho0BjQbh7rDaPaa58tVOpxo5GT02HPbtVYtt1dvwSIopg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01c119656.mp4?token=JgW6LsC9HWjMRVLuccYn9bauy1kNxJuCmawFKNhlR4cnxivxcM8q7PfzGl34JrNkUAY_vFZtdt7iNmrhhzTUqNGOOKL2eOAzQUl-tlnDTwWL11zydIQtUhblnT-CYtdgWN-E34hCuFF0V3u4wLT3lj8KNyFnUxsjctHo5zdTbdwOOiAv0s-_cTQXJR74_bf3-lNEaSFO3ho6MDr0KLkLzo5MzEy8LdWMv1558NrByUpMaONw8nlAjZjHr3O-MuANVwza-O7sUEhkCJ41yGz81BiJbyL3ZhMAe369B3vA5Ho0BjQbh7rDaPaa58tVOpxo5GT02HPbtVYtt1dvwSIopg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام ویدئوهای حمله به سایت‌های رادار ساحلی‌ایران در سیریک و جزیره قشم را منتشر و اعلام کرد حملات تلافی‌جویانه ایران به بحرین و کویت رهگیری شده است
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65343" target="_blank">📅 14:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65339">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xu8ZiHOfATfb6RVj6CmqEWU9g-q9mcnSIElN7QQknWDF7Y8JZnnAWUi9MyhDn-1JLuaaJQlnUfWTmPAnffIe4muvuWt_HnC_88hwhDr5oHr22BUKDprn0fRp96R5EUX6D2nMewhp-L0V2SjD_tL4jLTv03_vjNxZhMgBeDw5iyJxdNQb0nIov8owQsUEGm13Wu8Xv4ZoJN4aRTrxwgLa12nZCYxa2B1FCwTEot5sldiqB41pRCUY3ircVDX7rRDaAAcWJM0EcriReDeEgM7tCuAFLRvP-kIhU6jjashE3rYJc4NC6tGn-JXIMJ0tleK1m_rCAZ8JvCvmHnHoijjtmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MfOG1PXmcAUwwx4TG2Y4YFA5NKNIhwLMkcbTIx4Lx7ROhE1-dbmzuH4x1oN0vPXzTd7GAR0RKmz_2fx5HSw50zs5oHXRhj00Ql0wIGhasNcenNhpN5Vw5nTPLsts3ibUfbA2hVxWI8F0uCDvCFGbM-wt5tAQQxYAFFs9PgarHcbug86DNaPkZnYWBO4YyKsIWdhv9A76U3H0xBljRy0LhtEwjbYwg_vahJyF5YJpKlmXhftPc-Jb286vRFMp9DolGlLhul1zrDWJG4lfKzl8-uApYAFY-qG9ULQrd4TNLsnKmAakQDGG0LOZDl3E4NR8ApMUrla81XuXC1cWJT4D-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b-KyAEuJwg6Fo5fzBIizrgGu40A3YYfeMBgz7onMCpTVnamWzUNHF7tvte9Z7O99AkpXTo1T9RfdIxwnyOw7-qtJoUKaxQdgDoT_D-JcrRWgNphh3tQPtzD0pG2S9NlFsEIY8SIEs7WDwfh9OHq0c6ZdiCGxzOHcmWtTQNwxMCZj007t2wRUFe5dnxCm6VnZ3Ggjn_ZoXyg13yKCE6zXjvNbxdZ9h5ZExPt7q311Gk3rYamItGfWLZxSUas4RtQxjwvQkvoLp-xihihMg3RDRjl1L1DDx2t8ft7NpD-wONVbMz2iOrIoaQniJdmR-kwzBURWAg3vwwcH0MiBI8JdPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65aa546373.mp4?token=YuJwgyPVoKCBJVGgyG7LyfqeJqOXM_N6OLZqGVjztpqPe4PktwPnEolV-xgr8Laa7xKA9FJlVEx6NlyU3NEnk12KAa38cIlAgzXOo9uYvN1trQO5sqEPhlLAv_70lVZny8cbrTFmazLO5zIp6qG0r47uhTnTVFtlcYahnAOtgZgO65YuIxJu11FkJh_Z5jL754Vyn_nDSI1Eh1mjGu-aCyGdw53QLOqAOXp9c0KlzjpJ7hT3s1JM_MrXuh3wF5veX6vgvCTbTK93eTjcYPY6wNzftzKHm-3JgSTbFC_-pQ5dpqd8hYfcdfj_xpNnSAw98Uz-9IhPF56SPNDkd1TiPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65aa546373.mp4?token=YuJwgyPVoKCBJVGgyG7LyfqeJqOXM_N6OLZqGVjztpqPe4PktwPnEolV-xgr8Laa7xKA9FJlVEx6NlyU3NEnk12KAa38cIlAgzXOo9uYvN1trQO5sqEPhlLAv_70lVZny8cbrTFmazLO5zIp6qG0r47uhTnTVFtlcYahnAOtgZgO65YuIxJu11FkJh_Z5jL754Vyn_nDSI1Eh1mjGu-aCyGdw53QLOqAOXp9c0KlzjpJ7hT3s1JM_MrXuh3wF5veX6vgvCTbTK93eTjcYPY6wNzftzKHm-3JgSTbFC_-pQ5dpqd8hYfcdfj_xpNnSAw98Uz-9IhPF56SPNDkd1TiPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بعد از درگیری های دیشب سپاه با چندین پهپاد و موشک به بحرین و کویت حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65339" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65338">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIamXerxess</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65338" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65338" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65337">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIamXerxess</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-ReiFyD8-rI1KXYtsJtQmEIE0WBw2lw4qnRAYT5jvfAxt1AR9wVXtfMl8rg-Yh-1qPNuMq3IofimtvqDQD1UdnQeL07ElI__dIEX5HTuPwvHfatzXTCV2pgWdGTRQYk409KUXl9UrOKoYbDyCoBUCL_olCNKnSigb2vDv1tnvJGI2asRp7LPfcYofHZn_2T1iNi6u1sLvxe2oSF1wDw4KIrmfnqSLcvVcFQ9M4L3UTdvdyJmaITGr1nknR4-BTWheZk_tn04c5QpaasFfTe4yVWuFRyhRKnGB1Y6oGb3AOZZ4RZdE9AtxxDDkVhi8a54UkL6-YAIDDhOSseQyG4pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥊
پیش بینی بدون ریسک بر مبارزه
Muhammad
🥊
Bonfim
🥊
🔸
اگر پیش‌بینی شما اشتباه باشد، یک کد شرط رایگان تا سقف 100$ دریافت خواهید کرد!
🎁
💥
با پیش‌بینی بدون ریسک در هر حالتی برنده باشید.
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65337" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65336">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nyjYkfhWmF4MJRYQmroluhZjCdRL5DzuQp5YTukRv_WfjI1upkLVyjClbltDUrXEfvwtc4jvoyW1Pi8kX_ULHQDoUGumm5kj_NPXx5HwhcdC3HO11k1XjZHHCqDgUq_lo8iz6Ocy4LhZLe2EUW4bormMVNc8uqEyTBPH866stGRwGaUS_5N6K68tBMKfUq5SME8I_eGrK2f5AnKKciqRaxj-8cx6uvYg4lZAwfOKdNIgCDzEnzHScwSq8TW2n0-C0TmN7uPgpriCiIJ7MeTu6Z8Ngp4o12-vHl9PiTJAKLT7jqgBsDiGPR6mgQXZcD9509X5K0ogiV9gP3uClU5_Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
بیانیه فرماندهی مرکزی ایالات متحده(سنتکام) درباره اتفاقات و درگیری‌های دیشب:
چند لحظه پیش، نیروهای سنتکام چهار پهپاد حمله یک‌طرفه ایرانی که به سمت تنگه هرمز پرتاب شده بودند را سرنگون کردند. پهپادهای حمله‌ای تهدیدی فوری برای ترافیک دریایی منطقه ایجاد کرده بودند. نیروهای ایالات متحده پس از آن برای دفاع در برابر حملات بیشتر، سایت‌های راداری نظارتی ساحلی ایران در خارک و در جزیره قشم را هدف قرار دادند.
نیروهای آمریکایی همچنان هوشیار هستند و برای پاسخ به تهاجم بی‌دلیل ایران در دفاع از خود آماده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65336" target="_blank">📅 11:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65335">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSkEJj48og8mcyVyCA6rtDVK4TDEhU1sCNE4PvPpl2SFCUgwGz9-pWzeXT7ZF0udw93psedV1FCBoAZWNWNaKFWjs4ybMuOvB5xPVHA0nr6T6I4o7qNcATyZ_BCOr0vwrqmdq7YnMcD79zql0o79v2FK6-pima260mJCG0wHKDvvebvSqUSFYTfPQuMIBAymWM6dBZTz-ee7PreaWbspOfOF8G3OyI08vcZq_cldDSCVBSDePB9ohzPXSAlFVJ6JvOVMSNFov-zFIpP9VzwBTkHk4ViR6OvO3a-UNHORWyhX7Hgm_eD1bRXjCgNM04vWyxtoT-1RFNdP79woweAopg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم خمینی در سال ۱۴۰۴ Vs مراسم خمینی در سال ۱۴۰۵
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65335" target="_blank">📅 10:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65334">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887b98bc21.mp4?token=cLRr5KZuGCcoL_eXS4JP5r3wJQlJamsZgWxQb3NYLdfOKFVO-s1a52ITxrhTqCHidwEVfvpaoGBTXR727RLn5jZ2b6okA3cf6tAb3NX9nJ_IretauhyAM-AaVs3MsjV57GMy9T9jF7j-wW6WdRXcHND9egglANH6lO3FiVPLMEazyfdTbKJIk96wv1aMVl6012IuRV35zuCcMeGCSjrFojJf-dz83q5p1RtE1QCqfiIEGBLdILjzCD8TVPxiKCvCLukGOV9kGAyfPRDMp_YMcUmXxJ28BcGCG4G9CyqbdtfKJW6M67omy7K6r1hFD1TDJpRhwU5L7Yu6UnMQDiebxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887b98bc21.mp4?token=cLRr5KZuGCcoL_eXS4JP5r3wJQlJamsZgWxQb3NYLdfOKFVO-s1a52ITxrhTqCHidwEVfvpaoGBTXR727RLn5jZ2b6okA3cf6tAb3NX9nJ_IretauhyAM-AaVs3MsjV57GMy9T9jF7j-wW6WdRXcHND9egglANH6lO3FiVPLMEazyfdTbKJIk96wv1aMVl6012IuRV35zuCcMeGCSjrFojJf-dz83q5p1RtE1QCqfiIEGBLdILjzCD8TVPxiKCvCLukGOV9kGAyfPRDMp_YMcUmXxJ28BcGCG4G9CyqbdtfKJW6M67omy7K6r1hFD1TDJpRhwU5L7Yu6UnMQDiebxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: ایران با آمریکا به توافق نرسیده است چون رهبرانش «قوی» و «مغرور» هستند اما «آنها چاره‌ای ندارند.»
کمی زمان می‌برد. شما درباره ۴۷ سال فرار از هر کاری که می‌خواستند صحبت می‌کنید.
یعنی، این باید مدت‌ها پیش انجام می‌شد. این باید توسط رؤسای جمهور دیگر یا کشورهای دیگر انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65334" target="_blank">📅 09:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65333">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کانال کازینو…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65333" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65332">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e488d912f.mp4?token=PzmBJ0fHgvk9WWu2kUplNu4_s4RlnxyhsXdgE_YwwaHI-ASHFMmketLuLzDJy8ZGq-tCzmao5uagfX4zk4033w-APYOAiODvJFe6svlm6HVPTfLCc7jLIqxqVDif0WoJp_z3E96I8LQcLkvcd6owZPtl-w4vE5EH-9ToeeRGR00GeJULpcUaV7EgfLqIJubzZbIhuIazATAakINzocLh_bQ4r30q0nBahCzFl-bVJWjVTCEh-YsUStNWeuDSXVd2ITTSWZBbR2K8RUFAdy7WbABPE58dCtiBlBHJ7qec6oKmFa44ctB9dgziCga8IpvQzJ9L_YicLAmK5JfTo59tqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e488d912f.mp4?token=PzmBJ0fHgvk9WWu2kUplNu4_s4RlnxyhsXdgE_YwwaHI-ASHFMmketLuLzDJy8ZGq-tCzmao5uagfX4zk4033w-APYOAiODvJFe6svlm6HVPTfLCc7jLIqxqVDif0WoJp_z3E96I8LQcLkvcd6owZPtl-w4vE5EH-9ToeeRGR00GeJULpcUaV7EgfLqIJubzZbIhuIazATAakINzocLh_bQ4r30q0nBahCzFl-bVJWjVTCEh-YsUStNWeuDSXVd2ITTSWZBbR2K8RUFAdy7WbABPE58dCtiBlBHJ7qec6oKmFa44ctB9dgziCga8IpvQzJ9L_YicLAmK5JfTo59tqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
🎯
همین حالا عضو شو و شروع کن
👇
e15
https://t.me/+6ckCmywafrxiYzk0
https://t.me/+6ckCmywafrxiYzk0</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65332" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65331">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gb90iyhu5HAeP1ffIMK_y3TAZs8rMoOQDQF7knHgZVVEYTNuo41RAE2euMTgI4fOsxs-Px2GLAqqZsQTqsI7qdiLgg-6fEEs0qoiH9MGDFQ7Nq9s4MqLjG8CKeloxAwmJV2vxS4K9VQIKmK7zh4CejOLY116A06a8KaMK-pr8OXCI9FxxhNBeawJM3VmhP628DK3lRk4qaaIS7Dk7vzG7au5EuuOQvw9A0tQrh9itPKFnmutcLwKPRLQ7AejmDoY-iyAEoZ_DqpuOsz8LVCHV9D6b-bzXFewQvH_EOTENjXJ2VtrUGDLAu8OW6EQTF87CCKBJxZgv5sl2dFELwEtmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برزیل
🇧🇷
-
🇪🇬
مصر
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
بامداد یکشنبه ساعت ۰۱:۳۰
🏟
ورزشگاه کلیولند براونز
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
برزیل در
۱۰
دیدار اخیر خود،
شش
برد و
یک
تساوی کسب کرده و در
سه
بازی شکست خورده است.
✅
مصر در
۱۰
دیدار اخیر خود،
پنج
برد و
چهار
تساوی کسب کرده و در
یک
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر برزیل
۳.۴
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر مصر
۱
.
۹
گل در هر بازی بوده
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۱.۵
- ضریب :
۱.۱۹
🧠
اگر مجبور به پنهان‌کاری شدید، مسیر اشتباه است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65331" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65330">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇺🇸
ترامپ:
ما خیلی سریع از ایران خارج خواهیم شد، و این خروج به هر شکلی که باشد، چه به صورت یک توافقنامه و چه به روش بسیار سخت، بسیار قوی خواهد بود. روش بسیار سخت شاید آسان‌تر باشد.
اما ما خارج خواهیم شد، و قیمت کودهای شما به شدت کاهش خواهد یافت، درست مانند چهار ماه پیش. قیمت کودهای شما کاهش یافته است.
انرژی، نفت و گاز شما همگی به شدت کاهش خواهند یافت. و صادقانه بگویم، فکر می‌کردم قیمت‌ها خیلی بالاتر برود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65330" target="_blank">📅 00:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65329">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‼️
🇺🇸
ترامپ:  ما یک سلاح هسته‌ای را از بین بردیم. این قرار بود کشوری توانمند باشد که حضور هسته‌ای داشته باشد. ما تا حد زیادی این کار را تمام کرده‌ایم. به هر طریقی، این کار تمام شده است.  @News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65329" target="_blank">📅 00:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65328">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdccc3a3f6.mp4?token=ELuwauWuqnRfWUbuibIVnnFXJqAV0RHKavPGoaZJCuh6_Zg3i_pDOFRpAcDrs8QkmvGU95a6wImzc_1uJv-pnoQZYOpX-RgACxiM1WUI0KCp33fILjpzlrR1aOKQ2wvFTi8uQUO9uluWbXg-DeANPhLTQYioKRSFtXb0eCoH_6UHk3uYAav71c6peRQ-JEu340vmtUBuMWu6VX4WTKnyEtZCOUSh3FA0-YXo2vp2xlezei1DQNJgI79QWa4rIvL0xPYpjM8QVHJivCLcRv-fM7y8d1qxe1TSyvVyOSD-cQ_i0zItoA9BCebNrlRM3JLCtbWdIdPBQKl2u9ZVFJK0yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdccc3a3f6.mp4?token=ELuwauWuqnRfWUbuibIVnnFXJqAV0RHKavPGoaZJCuh6_Zg3i_pDOFRpAcDrs8QkmvGU95a6wImzc_1uJv-pnoQZYOpX-RgACxiM1WUI0KCp33fILjpzlrR1aOKQ2wvFTi8uQUO9uluWbXg-DeANPhLTQYioKRSFtXb0eCoH_6UHk3uYAav71c6peRQ-JEu340vmtUBuMWu6VX4WTKnyEtZCOUSh3FA0-YXo2vp2xlezei1DQNJgI79QWa4rIvL0xPYpjM8QVHJivCLcRv-fM7y8d1qxe1TSyvVyOSD-cQ_i0zItoA9BCebNrlRM3JLCtbWdIdPBQKl2u9ZVFJK0yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ:
ما یک سلاح هسته‌ای را از بین بردیم. این قرار بود کشوری توانمند باشد که حضور هسته‌ای داشته باشد.
ما تا حد زیادی این کار را تمام کرده‌ایم. به هر طریقی، این کار تمام شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65328" target="_blank">📅 00:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65327">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecba9ea726.mp4?token=TxLK3p-_tgWDeRNX4nGTplf-yeswg6jNtX-zUMw7FCO2FSwy_BmmEclFdmfw2tKFgEEgl1PztgIh5yPXQt4Daa9OFx0DaGw4R2L0Std7j743_A0yiJhSawL-VDcwsKcRVeA9x8M57UdvvXM5lcGrfLFko4l-nhMPfP4JxATwcUSyZHyZeOU9Q7BZuFsgkFmExeV7bVRTRNjW82AfF16CEBkAcQxEAZB-PpaHUNVwIrESG6llfeYD2WG_NKz2RoMerkB-OoLh6iA-vpOXlIxKKn8O0xp_I1qEEEYRY2rCwv0dZeM-ENuEw_eOBgwIp0RDY_bSnKBZaMShWsddLGiR-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecba9ea726.mp4?token=TxLK3p-_tgWDeRNX4nGTplf-yeswg6jNtX-zUMw7FCO2FSwy_BmmEclFdmfw2tKFgEEgl1PztgIh5yPXQt4Daa9OFx0DaGw4R2L0Std7j743_A0yiJhSawL-VDcwsKcRVeA9x8M57UdvvXM5lcGrfLFko4l-nhMPfP4JxATwcUSyZHyZeOU9Q7BZuFsgkFmExeV7bVRTRNjW82AfF16CEBkAcQxEAZB-PpaHUNVwIrESG6llfeYD2WG_NKz2RoMerkB-OoLh6iA-vpOXlIxKKn8O0xp_I1qEEEYRY2rCwv0dZeM-ENuEw_eOBgwIp0RDY_bSnKBZaMShWsddLGiR-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
مقدار زیادی نفت وارد کشور ما می‌شود و مقدار زیادی نفت وارد جهان می‌شود که مردم حتی از آن خبر ندارند. و به همین دلیل است که قیمت هر بشکه نفت ۹۷ دلار است نه ۳۰۰ دلار.
وقتی کل این موضوع (ایران) حل شود، نباید زمان زیادی ببرد — به هر حال، این کار انجام خواهد شد.
وقتی همه چیز حل شود، قیمت نفت ممکن است حتی از قبل هم پایین‌تر بیاید.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65327" target="_blank">📅 22:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65326">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">«منبع ایرانی: ادعای العربیه مبنی بر موافقت تهران با انتقال ذخایر اورانیوم به کشوری ثالث کذب است
یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایران روز جمعه گزارش یک رسانه سعودی مبنی بر موافقت تهران با انتقال بخشی از ذخایر اورانیوم غنی‌شده خود به کشوری ثالث را رد کرد و آن را نادرست خواند.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65326" target="_blank">📅 22:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65323">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CW52baBtNSCKGb3xpaYHOx9tZcSc1iOTKqvHwy4PDlMilz99AZJOuNqB9RBhS2Ikt02EMDsj-x8PIFt2ej6Gji3UOeTqVYlfYnLwDA1XT2rE45xeJfhWHnOFhRsdD9erAmYrOPCC2eonNljXIkNJLtrsskM4z8N5c1rBgQ1GBSILe_1h4j-hEXNbGbMwLmNGgTpawBFPxBY11h_kxRezpHYUU49oMg5rio-CUnedsJtfi9z0vXv3rmOxz6n6EcndjVSHlWaq-t83E_PLXpqtStYmyJP1apRhpiA-iMkCdt9KF9P2DlHLsh57h5P0z6zQBg0yzHa1JGJ1OP64Ky0wDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
صحبت‌های جوزف عون، رئیس جمهور لبنان بر علیه نعیم قاسم، حزب‌الله، ایران، اسرائیل و امریکا:
به نعیم قاسم(دبیرکل حزب‌الله) می‌گویم مردم لبنان، مردم شما نیستند. شما نماینده مردم لبنان نیستید. مردم لبنان از جنگ بین اسرائیل و حزب الله به ستوه آمده‌اند. دشمنی بین اسرائیل و لبنان باید یک بار برای همیشه پایان یابد!
ایران لبنان را به عنوان اهرم چانه‌زنی در مذاکرات خود با ایالات متحده استفاده می‌کند. این غیرقابل قبول است.
حزب‌ الله باید بفهمد که راه دیگری جز نشستن و گفتگو وجود ندارد. هیچ راه دیگری برای حل این مشکل و نجات آنچه باقی مانده نیست، جز از طریق مذاکره و دیپلماسی.
خطاب به اسرائیل، از جنگ از سال ۱۹۴۸ خسته نشده‌اید؟ واقعاً می‌ خواهید در صلح زندگی کنید؟ بیایید بنشینیم و صحبت کنیم
ما آماده‌ایم. ما مایل هستیم. ما متعهدیم. آیا شما هستید؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65323" target="_blank">📅 21:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65322">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwUkQ66HsBaMiOpzCWGuItlTkKaewFeiBJDv9W3MxVVvJjSYnQMq_gLbBvfdKXBNOF4BKbxwZrajwYaYdoLjx5563JfS3xPn45Kk_f6u1076PfiZWDKDOw8Axl7krOjVJ9GQlR1m5mYP6bCIXuot57BnDREB7XjktW30Tg_WDua1bqHGV3xoRPU3cjJmgUoYX8oUHfBLOmJZ0kq2CyGQnXaQ2-WfkVukGxjKz-UIfZPhDDcGNDfgWC_JukoF0USRNWvuY2z8L8ZAMWIXev5UMPtFM6AG8o_bsoxI1fi_H6E8SSIhUYNXMevBl8XYx13f6bqBRm5L4q7ERAdHLOGiww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پلی مارکت: صادرات نفت ایران به کمترین حد خودش در ۶ سال اخیر رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65322" target="_blank">📅 20:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65321">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5990d5144.mp4?token=Y3EGaqs3BzX7BwgZi1NU1ELCo_zYBeKj4xUDb-SrGT7GwIq8b30L3tqrIVs_78ZxbELdWlDf35XWPVr5l3Oyf0z-4uaNA2wsWU1TlBRwabWG05A5h7HVHvjnQFSlR31odoVaP7tt7HAGnD7LfrvrlVBbq-Ru7KfAtBrj2kphis4otgaKL6UXbxRa7cVfaBAhOjzPygOLURJk6kMmVlpQB93Hftc9AOiQvNcRRDxKj6xTZyU0mQULqPyuTo_KJamsosBmoz5HeZmoExE9zMHBD41dfkafUvAs7AFiWJI2rTCT6hM0gw9SWIXoIB84BCgPavtB5qYMa3vHJby4vqPQ4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5990d5144.mp4?token=Y3EGaqs3BzX7BwgZi1NU1ELCo_zYBeKj4xUDb-SrGT7GwIq8b30L3tqrIVs_78ZxbELdWlDf35XWPVr5l3Oyf0z-4uaNA2wsWU1TlBRwabWG05A5h7HVHvjnQFSlR31odoVaP7tt7HAGnD7LfrvrlVBbq-Ru7KfAtBrj2kphis4otgaKL6UXbxRa7cVfaBAhOjzPygOLURJk6kMmVlpQB93Hftc9AOiQvNcRRDxKj6xTZyU0mQULqPyuTo_KJamsosBmoz5HeZmoExE9zMHBD41dfkafUvAs7AFiWJI2rTCT6hM0gw9SWIXoIB84BCgPavtB5qYMa3vHJby4vqPQ4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ثابتی: قالیباف تو مذاکرات اختیارات تام نداره و پیشنهاد پزشکیان بوده. تو مذاکرات اسلام‌آباد اشتباهاتی خلاف خط قرمز رهبری شکل گرفته که باعث شده هیئت تذکر بگیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65321" target="_blank">📅 20:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65319">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31d6cf55df.mp4?token=gji_0NsXHmbNdG07wWgIuobwsrIeylQVjBie9oqTIbR1mn64h24rf1HBv64Qq6ArHsnLBKCadRit3pxbGLxp81TmZXmhcSKkqXAHGMKN8lrSIk0RvrYzgFu5boJ3wr3oztXHdB0O2J1ac57oW_EKLk3s_HIeZLOwKsZFDwedih4cMeBACiiO9t19XeIclaNxHzPC8fUCaFzZuucAhjuvuUMXWC5LNaf5VFlPw9UPUVoi3v4n-QSM29ZNV7XMc0K06_NTe5DKsEqfxdLvX7acBQ6R-jDqB5BoJIItOSdCim_5VrZUswEGqol3NrAIKIlvtcofpkXtvwScblZ9wdkFtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31d6cf55df.mp4?token=gji_0NsXHmbNdG07wWgIuobwsrIeylQVjBie9oqTIbR1mn64h24rf1HBv64Qq6ArHsnLBKCadRit3pxbGLxp81TmZXmhcSKkqXAHGMKN8lrSIk0RvrYzgFu5boJ3wr3oztXHdB0O2J1ac57oW_EKLk3s_HIeZLOwKsZFDwedih4cMeBACiiO9t19XeIclaNxHzPC8fUCaFzZuucAhjuvuUMXWC5LNaf5VFlPw9UPUVoi3v4n-QSM29ZNV7XMc0K06_NTe5DKsEqfxdLvX7acBQ6R-jDqB5BoJIItOSdCim_5VrZUswEGqol3NrAIKIlvtcofpkXtvwScblZ9wdkFtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شهروند کفن‌پوش اصفهانی خطاب به مسئولان: من رو با همین لباس ببرین توی دولت قول میدم همه مشکلات رو حل میکنم؛ تورم، گرونی، همه رو حل می‌کنم
از پزشکیان هم میخوام حمایتم کنه مگه خودش نگفت هر کی میتونه مشکلاتو حل کنه بیاد؟ تو رو خدا اجازه بدین من بیام.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65319" target="_blank">📅 17:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65315">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JhgyoHttcCseHtaAoagtvrXWlgqFYmkomSWWLsvu712OdOvLfYoz3a2KIPcd6S1yTW_241MDBzIL6ZmvPLr8sKRytTj1IOky0Lu7hemb8QJrHDgc4MGyaz7Uuj-ZNl1QARm_5edU_2Y_NxTXSP1KizSD72JoASXfuHm43w33GCqEyX1rvtUALiQeRcR0dDNewpYJlzPfkGBHAeZwLDQuLHZBVHx1evMHq92XT1fY8CZW_zyekXduaxn0M8ibYv4SrEyQzxHXeH5-UjHOX9ZGvhwvyP_EBGkl2R1RhXTkIg-Qn9ZYRWzQk7AgrEyJZA2muuuBMHrq9U1yr8NFEq7vwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Sm3Ckzg7QEm8XN29kl3RPrZy8FRVxsYLFzfnSgxZVmpFNFJ022sIaxCqiLUmGeIClA2EiN5wa6f3phTpkdLbHIPJWhEo9hZtAnokwU22QpDqmkXosyxBGll0_p3l0IksyLj8xG22PzpSoTvPBTpo9ODHkfMGkZBgsCYjjEAmk4-L00rd3ELeyhQUrpBYZXbI4sn4CxXdtGxeTvvmdTV4Mo1i2i69YWw-o-HPkmD1oGXQViUNyJFf-TklNdYH6cVkyE_dBTvw3L55000H28Bk7gnlcTS5nqCwcatUToL9p_Rx06A9UBzcmpOkngg1_mAf3nJv_KLqTyfm7l_ECXLMow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LN_JH4znYNHMjqwWlTLZmQYHZ6ZNq5hGUzwDY0S6Vm4FeEXOgrQdy1rYjf6z_iKYJDQ4onqWn2IO1lJbVl6jR2xdSR-rxYfNzkvN9pOTFn2MZKdeWVc_4zQCAy0T0QmCGbcaMFmFOJAZc3qCOtt47BN9povLlpWD9IN5H0V9PmDmShZBKvH3zch9hTDk9wByMYhoW-NuxqLQRdnvA0ZG1Gi4PwocksdVhepXpneZ7dfzOEkj0ju9masR7VgFrtp_aGwiiRF9tQjH1Ph3e34DgajGIHWeNeXYXiH2kB6sRu8FYxM3Ecf-kVMR5YpC_Ze3daocOGTnp6PsIcVbXEfB0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
فرماندهی-اقیانوس آرام ایالات متحده (INDOPACOM) اعلام کرد که یک کشتی بی‌تابعیت تحریم‌شده متعلق به ناوگان سایه ایران را توقیف کرده است
در طول شب، نیروهای ایالات متحده عملیات بازدارندگی دریایی و حق بازدید و سوار شدن به کشتی تحریم‌شده بی‌تابعیت MT DAVINA را در اقیانوس هند در منطقه مسئولیت INDOPACOM انجام دادند.
ما ادامه اجرای جهانی دریایی برای مختل کردن شبکه‌های غیرقانونی و بازداشت کشتی‌هایی که حمایت مادی به ایران ارائه می‌دهند، هر کجا که عملیات کنند، را ادامه خواهیم داد.
آب‌های بین‌المللی نمی‌توانند به عنوان سپری برای بازیگران تحریم‌شده استفاده شوند. وزارت جنگ ادامه خواهد داد تا عملیات غیرقانونی و کشتی‌های آن‌ها را در حوزه دریایی از آزادی مانور محروم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65315" target="_blank">📅 16:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65314">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guTTld75o1qZkWub2vkYU6BFmMJBrLYiWa8GgJByILmnzpnkasCS4eyPtgnyCaFN7E6kSLiD2T2PuNny0ku7LFII5FOVuQ3D942sn2mBlRf9HuyLaFFqZ2oCUY6LHN9gY_SE9XrwSzK9CIMgDE9ZeJme4OVHsBWRtdvYAFiIke9Qr2rsQq8vW98eJvufliIbajnxVHFNT9Qp7MUI4GSjTPDIwRAcPRQeghHD7fsTHeUWCWnW_eoZGDIZYEGQRtD5JWK846k0BJS-2icSScvidoJTlbGOZA8c0kisDI4qwEuafDeqT8UdCvnV2uOnUnYyC1TSIcBLkLEQqf0cbOrm2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
خبرگزاری العربیه : ایران رسما به پاکستان اعلام کرده که با انتقال بخشی از ذخایر اورانیوم غنی شده به یک کشور ثالث که مورد توافق هر دو طرف (ایران و آمریکا) باشد موافقت کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65314" target="_blank">📅 15:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65313">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bcc23b06e.mp4?token=H6st50JHOUF0CeURM8kxZBw8n0uxkfUF8akmYkIAyxGI5FdpJRydfwSZJGNtH7LLvQWtCoilyyAyKFaZXKGelwBC7oxrCB67wv3MMotjO4IvCJ5IXdyLP2rWGBM_2JqHXzWl9Ceq3PmW2Q6DelzvgTXcetnynaGq8nxPCXoqauwmRZ9F2aYmhBmeVroz1Hy87vJmTE29DpqppBwTDeVM3QiVAsqo7SqbwMDAcxzV7odBt0Lkx-VLH56OmGvS_KW09uzJB094vc0p9Y9v7MG__fQG9_P0J3TEhSkI8LjeL8RikrPjPNYkxUcYkPA4Dy1tgFxEL8PTuPG3VW8QNW8_1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bcc23b06e.mp4?token=H6st50JHOUF0CeURM8kxZBw8n0uxkfUF8akmYkIAyxGI5FdpJRydfwSZJGNtH7LLvQWtCoilyyAyKFaZXKGelwBC7oxrCB67wv3MMotjO4IvCJ5IXdyLP2rWGBM_2JqHXzWl9Ceq3PmW2Q6DelzvgTXcetnynaGq8nxPCXoqauwmRZ9F2aYmhBmeVroz1Hy87vJmTE29DpqppBwTDeVM3QiVAsqo7SqbwMDAcxzV7odBt0Lkx-VLH56OmGvS_KW09uzJB094vc0p9Y9v7MG__fQG9_P0J3TEhSkI8LjeL8RikrPjPNYkxUcYkPA4Dy1tgFxEL8PTuPG3VW8QNW8_1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قیصر خواننده لس‌انجلسی برای خوشحالی عرزشی‌ها پیک میبره بالا
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65313" target="_blank">📅 14:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65312">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVJFuNkUjMnGNne766pVkUjZnSpEH3XMwbonL4HuPjEIMbIbDEtSczh-5SI7m03z0bWjw-UyUwSGWb-qpq4ENwTq0n118Xl4SNhQXEAPUsDfjdTn_RjOgj5cvrK-EMLWX_W0uGVWu6Tc7EwfXE_7JdP5tIAqNzBxLpGyIjuRaKzvWFv6q8vHGrVfNm1hpiY1BE2YSghWmhgbvBXeIm0U8AvXzg8oDX0yVrSPyynIQ8qzyY0CLi6oiFOZoskIh5RY-9HOkLscDdSJxxfHolybYNUGxgXXt7b8guAxLsjtCi95_jW37aIIAJzOwQMP0ALOGcNkKWWiHZCO_uDbyRP39A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت‌کوین رسما به زیر ۶۲٬۰۰۰ دلار سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65312" target="_blank">📅 13:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65309">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb5ff9567a.mp4?token=DSmvXlx6GjrHBIapVYVAQTCf0KI-f5jOmlR_1jXCWV8lDLOBX-4ZD2MbyN5roAPKgymKa7AaG3xtD7l7oURO1K-DYnAy1UstSjVyQZeNGT4O_09G6Lu_2s8zS3cfbbXg5blZ1ckoaP5mvw5GLgcjDwqP5d_PqBXLOcIozWkSjaFRZl9epROGfPTElfjwrVhNXwSIyt17FmzqNIE_AYKlEGSmr2qJXywzXH8bKVY95URTZx6-IOVqbk6XzEnSCAuuTMMp2KM3UPoLRSEQGd5PCYVzK_JMlQAtXDw0SYwBnt6XkACXn2A3WBU_qcmGMxFK4vzv2Vc884U0SLYk-sSoDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb5ff9567a.mp4?token=DSmvXlx6GjrHBIapVYVAQTCf0KI-f5jOmlR_1jXCWV8lDLOBX-4ZD2MbyN5roAPKgymKa7AaG3xtD7l7oURO1K-DYnAy1UstSjVyQZeNGT4O_09G6Lu_2s8zS3cfbbXg5blZ1ckoaP5mvw5GLgcjDwqP5d_PqBXLOcIozWkSjaFRZl9epROGfPTElfjwrVhNXwSIyt17FmzqNIE_AYKlEGSmr2qJXywzXH8bKVY95URTZx6-IOVqbk6XzEnSCAuuTMMp2KM3UPoLRSEQGd5PCYVzK_JMlQAtXDw0SYwBnt6XkACXn2A3WBU_qcmGMxFK4vzv2Vc884U0SLYk-sSoDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مداحی محمدرضا هلالی مداح حکومتی با زبان چینی برای عید غدیر!!!
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65309" target="_blank">📅 13:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65308">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b7d22fc01.mp4?token=XO70wbM7FpbwDk5_CbOBJi52VPmvkaqVBQkiYkjEJOMaF5qZTZcr5ZvGg0UaAoeGjEt_1ZgQyY_98ZRHkLUH5zW-y0mnAg1MoUozRNmC48N_duNqhNLj-RNnOQYN-5ScEAJdDTyjshwWC_U4uyWPDpuBXsHF-wvBmYYrUYFHEXwnKyegFJXWnw-WamDNGuXVI0DYMZiHAiBRz_nleDJ3NpN0whe2JHdxHljoSa-U8fZVfBskGq5MZagZpSvqi0StsWoYW41_dLe_KoZUT0FdsDraGVV6Y0DO7eUgRD47PwTQHb4SXQ48arPVzlunyYHgMKCykv5er__5gpKWd_QOfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b7d22fc01.mp4?token=XO70wbM7FpbwDk5_CbOBJi52VPmvkaqVBQkiYkjEJOMaF5qZTZcr5ZvGg0UaAoeGjEt_1ZgQyY_98ZRHkLUH5zW-y0mnAg1MoUozRNmC48N_duNqhNLj-RNnOQYN-5ScEAJdDTyjshwWC_U4uyWPDpuBXsHF-wvBmYYrUYFHEXwnKyegFJXWnw-WamDNGuXVI0DYMZiHAiBRz_nleDJ3NpN0whe2JHdxHljoSa-U8fZVfBskGq5MZagZpSvqi0StsWoYW41_dLe_KoZUT0FdsDraGVV6Y0DO7eUgRD47PwTQHb4SXQ48arPVzlunyYHgMKCykv5er__5gpKWd_QOfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: عملیات خشم حماسی پدر، همسر و فرزند مجتبی خامنه‌ای را کشت.
🇺🇸
ترامپ: من فرد مورد علاقه او نیستم، اما احتمالاً او یک حرفه‌ای هست
در برخی زمینه‌ها آوازه خوبی داره، برخی‌ ازش بد میگن اما خب درباره من هم بد میگن!
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65308" target="_blank">📅 09:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65307">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پرسرعت وصله
👌
👌</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65307" target="_blank">📅 01:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65306">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Barko VPN_v2.2.apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/news_hut/65306" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👈
بهترین فیلترشکن حال حاضر ایران
👉
💎
با همه نت ها پرسرعت کار میکنه بدون محدودیت
💎
👌
پیشنهاد ما دانلود این فیلترشکنه
🔧
لینک دانلود داخلی با نت ملی با سرعت بالا
👇
https://uploadb.com/plx39j7b72sy/Barko__v2.2.apk.html</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65306" target="_blank">📅 01:08 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
