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
<img src="https://cdn4.telesco.pe/file/jwQxZF53Dzr6mso90X8byu7b_3WJrjmq-3tYPuXMJtjVf0swgvqy-_bpHZ9rmZR_rdb3oa1L0Fyx-stJ0I8CnzQWdnoLUQsFFCwhn_b5rlX4FErNnEzPFIZ6OyqkMfx5x9cP7UFIqdW1OnjNh3T_DTzzaEJBuVk1BNsCsk7LiZ2XN4ctCyi7-w-GbyJCiFfFhjjUFVLzbcIUQjudmjngADiARphbNRlM1lghiSiRaZmKQVudMQ1Lfv96fsLBG9_R4oKqFmi5qZ6f_p5B3Jf5U_H7-Op5h7g1Hs74JbqsoKMo9rJxlt63sz9_Quyc_VNvXY_v-ocuSh-7ydX487sXTA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 133K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 18:14:03</div>
<hr>

<div class="tg-post" id="msg-69627">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_djTzwtK9pdTbOt5ZqBB1N1T6WgM6vRANX7LuL3rcj5Yw8hV9skDJQaps_duR7ZUBPgtdDNP4CnmJoCPwjdE6V5qmkrhEuPCEdD652yhg3snk0PGwwuH5qADit8cwJx6JYaZl4UX5UQonf_Wfs1Tk_wpNe-72rHwVKoarnDpPrdLFWiN0cFIHKY0JD-Px-ORIko8Z-IaJ7c-GM5-oihfkJ84Kx1XWNbNDLOj1smS0hEcVFJT4GWFd939hYDnRfkROqQvYJ5r9K6kLbGOiX8thXwRN-02joiAUtdXpR4edHfxNyI68tYtWB02jpY_yo5ndfoSOGH543jxFtJBtvgvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb7351e85c.mp4?token=XDiW72jW0vc5G12H98MlEdyL_Q2oe4-lVe2Wq4OuJqOTaRufLEzCmPh8YUB4rRIPImXsq3qy3wFG2XXZG7CBN3ykbA9O_VlxWX9Nj49AKYyZP5yBRw93nEjPIAJ3JqHoRMFmO1CRIaeTUsVsEiRXGrB6ZUUA3-NwBG9SQEix37q9s5UB3XFpjEWjLF5jqWJEIOwHLsYFHgMuaRZQ3pQDZLIYu5fAII3TouI1Bx_ZySJLFRR0ZCoLXm5QxRs3WLeM55y5YWpZqzzq0ZJf-zAVRIZ6MKoHC7t9Wvz6yYSpyMBBaJJToBRnnYkl4uLqYOKMZkqPx6_4tydrh6yuToFZNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb7351e85c.mp4?token=XDiW72jW0vc5G12H98MlEdyL_Q2oe4-lVe2Wq4OuJqOTaRufLEzCmPh8YUB4rRIPImXsq3qy3wFG2XXZG7CBN3ykbA9O_VlxWX9Nj49AKYyZP5yBRw93nEjPIAJ3JqHoRMFmO1CRIaeTUsVsEiRXGrB6ZUUA3-NwBG9SQEix37q9s5UB3XFpjEWjLF5jqWJEIOwHLsYFHgMuaRZQ3pQDZLIYu5fAII3TouI1Bx_ZySJLFRR0ZCoLXm5QxRs3WLeM55y5YWpZqzzq0ZJf-zAVRIZ6MKoHC7t9Wvz6yYSpyMBBaJJToBRnnYkl4uLqYOKMZkqPx6_4tydrh6yuToFZNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
زلنسکی:
امروز صبح دو پالایشگاه‌ مهم روسیه رو هدف قرار دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/news_hut/69627" target="_blank">📅 17:51 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69626">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67d7912f58.mp4?token=nLyWDsOZxDO2-4mfCcfQDnvEKmcovFa18L87vLtyenKCNvaP3CAl1IE9kzPJUUujeopZfX8Ot0dJPOsESnyY2HKhKogO_DYFr8JPN99IFrji7Ou4_4Z2lgqYE4sX_tbKVDybaqA3SCPN-qqxoVc1-pHSaQOLhWeE2cZRTfpsVBgY0h3AQvKV2n0a3X_glPGXJpSOZbqdupJXesnWUwOjcSfmbBOY1Wy6JyatT7U9fvDepMKxMtFVII0XaDyIlNG2iG3KlxbwFmljFRDx6WU-_Cis5rAqC92Y2pZfUYbUeXagtDuP8lLm9yFhds4CWNxB4VoAY51ZIFxOcHetA0p4Imx_pPW0s4JLs2iqHfuc-jC1DySs04YrB044ytt7lbCOf-07m9ufsPQMQrYGT83LAvNzLNP-4ctu2ZDiirOPnEn6QR7BDSOhWT1tXBlOwpzTzDDRiF_hkQkHzpix3_L6lsItpopWz3eT79e8Td-h3ymLBO5siVWcRSIgjafWezUiVKBkL4b4GVsE-UuamApUqnHMFNOihg6eeQhF5O4mJdQz-iXrljjeB3saIeTs6rDceP3h2TrJfpPtLGS4TR-zMNGA5mTEOOUZ_DmKmoVjYSaQsEAn1bmgwPp12KevwahkjFkKt2OJme6E0rMfhC87n-PJFFG5MBvZgs4NjK4toBo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67d7912f58.mp4?token=nLyWDsOZxDO2-4mfCcfQDnvEKmcovFa18L87vLtyenKCNvaP3CAl1IE9kzPJUUujeopZfX8Ot0dJPOsESnyY2HKhKogO_DYFr8JPN99IFrji7Ou4_4Z2lgqYE4sX_tbKVDybaqA3SCPN-qqxoVc1-pHSaQOLhWeE2cZRTfpsVBgY0h3AQvKV2n0a3X_glPGXJpSOZbqdupJXesnWUwOjcSfmbBOY1Wy6JyatT7U9fvDepMKxMtFVII0XaDyIlNG2iG3KlxbwFmljFRDx6WU-_Cis5rAqC92Y2pZfUYbUeXagtDuP8lLm9yFhds4CWNxB4VoAY51ZIFxOcHetA0p4Imx_pPW0s4JLs2iqHfuc-jC1DySs04YrB044ytt7lbCOf-07m9ufsPQMQrYGT83LAvNzLNP-4ctu2ZDiirOPnEn6QR7BDSOhWT1tXBlOwpzTzDDRiF_hkQkHzpix3_L6lsItpopWz3eT79e8Td-h3ymLBO5siVWcRSIgjafWezUiVKBkL4b4GVsE-UuamApUqnHMFNOihg6eeQhF5O4mJdQz-iXrljjeB3saIeTs6rDceP3h2TrJfpPtLGS4TR-zMNGA5mTEOOUZ_DmKmoVjYSaQsEAn1bmgwPp12KevwahkjFkKt2OJme6E0rMfhC87n-PJFFG5MBvZgs4NjK4toBo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇰🇵
🇺🇦
روسیه در حال آموزش نیروهای جدید از کره شمالی است احتمالاً به منظور آماده‌سازی برای عملیات آتی در اوکراین.
@News_Hut</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/news_hut/69626" target="_blank">📅 17:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69625">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d7f55ab9.mp4?token=BAnH3fYTCFDuyoDte_M-z4nwIavgDUTb9CScblyfv7sdC4FCxTnl0Wz9JSG15rxo4Q9ZReJtZuxPQB9gbRdVMth6_fKU7ucBhDD6eop-QjJBAVUB1Mpcbw1XDYYepe0_LEpgVSZQ3NaUcXW-a_0IymDvkSyGntewsd8yJIWkRuqhugt1P2NLdj4W2SX4m55sWpSYeEFKRtkpfFMY96kxqbDrr1X2Q6z-CPRTY1OSJ_hXZc1CzQWGfTg0K79VpZ4b9o9deWL2NouNK-l__X25YQ6_X8DfG16Va7TqZsHCUqNL_09tmtOaDkbfhKij0gHi2VURQFJnWBhzuUPwS_2Xpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d7f55ab9.mp4?token=BAnH3fYTCFDuyoDte_M-z4nwIavgDUTb9CScblyfv7sdC4FCxTnl0Wz9JSG15rxo4Q9ZReJtZuxPQB9gbRdVMth6_fKU7ucBhDD6eop-QjJBAVUB1Mpcbw1XDYYepe0_LEpgVSZQ3NaUcXW-a_0IymDvkSyGntewsd8yJIWkRuqhugt1P2NLdj4W2SX4m55sWpSYeEFKRtkpfFMY96kxqbDrr1X2Q6z-CPRTY1OSJ_hXZc1CzQWGfTg0K79VpZ4b9o9deWL2NouNK-l__X25YQ6_X8DfG16Va7TqZsHCUqNL_09tmtOaDkbfhKij0gHi2VURQFJnWBhzuUPwS_2Xpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
خرازی(برادر زن مسعود خامنه‌ای:
«آیت الله مجتبی خامنه ای سه سال از دفتر رهبری طرد شده بود.
برادر وحید حقانیان(از اعضای بیت رهبر شهید) عضو سیا بود.
پزشکیان الدنگ و پرت است.
قالیباف هیچ چیز از دین اسلام نمیفهمد.
خدا لعنت کنه دکتر مرندی(پزشک علی خامنه‌ای) ملعون.
دفتر آقا فاسد است، حتی دکترش هم فاسد است».
@News_Hut</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/news_hut/69625" target="_blank">📅 16:33 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69623">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/761165b2c7.mp4?token=u7Bo6HdUmDoQIUhH-iDMveaV8ip6ip4bnkF9QpeSDuO7nPDzsuMGIkHSmALl4-cQP0YFnIHzkgiLU-G8oJslH3f4NnIvg9R8KJvPzptyRTrVGoVCkjhsNIc9r5YTdnrCqRcvoqTyK7NY_ZvUnXw3B0eHOKV-FZfLd9bGToxHUfKhGv5-3YCsZj82eIYLPxoR8DaycAYH_L7xhrSH445JEfvLvY_0d_65O4ZfynToGuExQ6nil8Yk9O1WF2CGmX63KRlje6VNNRxrSAxMTfZI6hBN2HKBVHtkXL2M7oi2gJ0sheZhsv5beM9ngliYmy9MNY2NvvJRfshVwFl9kXRrzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/761165b2c7.mp4?token=u7Bo6HdUmDoQIUhH-iDMveaV8ip6ip4bnkF9QpeSDuO7nPDzsuMGIkHSmALl4-cQP0YFnIHzkgiLU-G8oJslH3f4NnIvg9R8KJvPzptyRTrVGoVCkjhsNIc9r5YTdnrCqRcvoqTyK7NY_ZvUnXw3B0eHOKV-FZfLd9bGToxHUfKhGv5-3YCsZj82eIYLPxoR8DaycAYH_L7xhrSH445JEfvLvY_0d_65O4ZfynToGuExQ6nil8Yk9O1WF2CGmX63KRlje6VNNRxrSAxMTfZI6hBN2HKBVHtkXL2M7oi2gJ0sheZhsv5beM9ngliYmy9MNY2NvvJRfshVwFl9kXRrzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
❌
🇸🇦
در حملات موشکی یمن به مواضع نظامی عربستان تاکنون بیش از 30 کشته شناسایی شده و انتظار میره تعداد تلفات بیشتر بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/69623" target="_blank">📅 15:59 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69622">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🇮🇷
🇴🇲
الحدث:
توافقی میان ایران و عمان در خصوص بازگشایی تنگه هرمز در ازای احتمال لغو محاصره آمریکا، قریب‌الوقوع است.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/69622" target="_blank">📅 15:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69621">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiB5x62V4UunRwyOVPGONd-RFcnHPFm6FbjnwZutgiOz1yFyaw04QWxIeqN4RkeNTcuq6pvyiltMBCppaxblRqRBEUCYYT_joWbqQvnV6SKPGaK0-gjHhWsIcIWm8cHVSa1BXbiiILz4XWM0nvpAyCP8ywv41mB3lwLIH2HrcqiYNAtbzxzhMNpWbqeNhWoeJ9RChkjl-tDu5jkkhkcaxH5xnAbxWaTSB-4zc735-YoQ29I1yN4juRtJcLVMRCgw1MY-Fm07oZB0icXnvwDYNsS5HGLQxwe-PDZzCadtP720e0-3S108SBuNWeqgNef0NO-YvLTBtIEB0YRFmWuZaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
🇺🇸
🇺🇸
واشنگتن پست:
🗣️
ترامپ به طور خصوصی به حامیان مالی جمهوری‌خواه خود گفته است که می‌خواهد جی‌دی ونس در سال ۲۰۲۸ پیروز شود
و از عباراتی مانند «ما باید جی‌دی را انتخاب کنیم» استفاده کرده است.
مشاوران تأکید می‌کنند که او هنوز به طور کامل در مورد جانشین خود به توافق نرسیده است و هنوز رقابت بین ونس و مارکو روبیو، وزیر امور خارجه، را حفظ کرده است.
🔴
یک منبع این موضوع را اینگونه خلاصه کرد:
«جی‌دی دارد به موفقیت می‌رسد و ترامپ آن را می‌بیند.» و خاطرنشان کرد که ترامپ دیگر به طور معمول نمی‌پرسد «جی‌دی یا مارکو؟»
البته او با مشاورانش همچنان برای این انتخاب در حال مشورت است
.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/69621" target="_blank">📅 15:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69620">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHRwKYdA8i9yQ933erKjRP2BRqqtWZyhb2Tp7sTto8F6qElY1PmPzcCmMSNFmBUPoW2lRmK2VdJDlj9vFlrDChvjA64UkWatzLFGz8Rr2UzV2tk8w_FZTyHQNXuoUUIZG0vCnHuIMUPAY66-huGsTbyco_GG8P36tQlM3FXR1XhtFo2mscKl-mNlbrzLqcyu-uCCi3Y-v0-epDTOkot4gOwOJcId7wHJnIh0fZbTs7NhLLj2djwQAsYb3jGQEd5cpTI4zFU47A6vnG1dUZbIxMjy2f98-4wkpRzFZhiKVp7GX_tshIYZ-fc-AIwqxrCCHqiqoUgrML-fa0u7kRmFYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
آمریکا از ناوشکن جدید کلاس Arleigh Burke Flight III؛ USS William Charette رونمایی کرد
نیروی دریایی ایالات متحده مراسم به آب‌اندازی و نام‌گذاری ناوشکن جدید
USS William Charette (DDG-130)
را برگزار کرد. این شناور از نوع
Arleigh Burke-class Flight III
بوده و بخشی از برنامه نوسازی ناوگان ناوشکن‌های موشک‌انداز آمریکا محسوب می‌شود.
◀️
نام‌گذاری به افتخار «ویلیام چارت» از نیروهای نیروی دریایی آمریکا که نشان افتخار Medal of Honor دریافت کرده بود.
🔼
ارتقای سامانه‌های رزمی
نسخه Flight III نسبت به نمونه‌های قبلی Arleigh Burke دارای بهبودهایی در بخش سامانه‌های دفاع هوایی و موشکی است.
مهم‌ترین بخش این ارتقا، استفاده از:
◀️
رادار AN/SPY-6(V)1
این رادار آرایه فازی فعال (AESA) بخش اصلی ارتقای ناوشکن‌های Arleigh Burke Flight III است. این سامانه برای کشف، رهگیری و مقابله با تهدیدات هوایی و موشکی طراحی شده و نسبت به رادارهای نسل قبلی توانایی بالاتری در شناسایی اهداف دارد.
◀️
سامانه رزمی Aegis
سامانه Aegis یک سامانه یکپارچه فرماندهی، کنترل و مدیریت تسلیحات است که داده‌های حسگرها را دریافت کرده و امکان کشف، رهگیری و درگیری با تهدیدات مختلف را فراهم می‌کند. این سامانه هسته اصلی توان رزمی ناوشکن‌های Arleigh Burke محسوب می‌شود و در نسخه Flight III با رادار AN/SPY-6(V)1 یکپارچه شده است.
❓
نقش عملیاتی
ناوشکن‌های Flight III برای مأموریت‌هایی مانند:
⬇️
دفاع هوایی ناوگان
⬇️
مقابله با تهدیدات موشکی
⬇️
اسکورت گروه‌های رزمی دریایی
⬇️
عملیات چندمنظوره سطحی به کار گرفته خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/69620" target="_blank">📅 14:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69619">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16b6e5f9de.mp4?token=MbbP4pG0abWelm6K51zY5ZO342FwtfE293orovXHlZFChhH0qxaxfv68Qu7WwAeJe7luXPni_g5BWy62zbLp0oGWcyiaxYj7gNhHHtOOp8CSFVZh-y9A__bC4XIq8Cpx9cdSmrE8bP2KC1a9am1u_LHfnEVGcbRnicM_qBDoiC_DVzieqxJyU5DXB5VpHdLTDsXEsSYGm_4oTf0o-1Al8CEEgpJKZPOAmGYnkSzFWhd49BBzM5f1DUyf3BeHZXgKhdE121um5tAM5zawMr7SPIllzQ8O4aXxQnvQZQvK29IsJygLSZxbz4YvbEdAuOXxAnodzwSravovsGyL_FTYsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16b6e5f9de.mp4?token=MbbP4pG0abWelm6K51zY5ZO342FwtfE293orovXHlZFChhH0qxaxfv68Qu7WwAeJe7luXPni_g5BWy62zbLp0oGWcyiaxYj7gNhHHtOOp8CSFVZh-y9A__bC4XIq8Cpx9cdSmrE8bP2KC1a9am1u_LHfnEVGcbRnicM_qBDoiC_DVzieqxJyU5DXB5VpHdLTDsXEsSYGm_4oTf0o-1Al8CEEgpJKZPOAmGYnkSzFWhd49BBzM5f1DUyf3BeHZXgKhdE121um5tAM5zawMr7SPIllzQ8O4aXxQnvQZQvK29IsJygLSZxbz4YvbEdAuOXxAnodzwSravovsGyL_FTYsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
مراد ویسی تحلیلگر ارشد اینترنشنال:
قاجاریه در عهدنامه‌های ننگین گلستان، ترکمانچای و آخال، سرزمین‌های ایرانی در شرق و غرب دریای خزر رو به روسیه واگذار کرد.
حالا جمهوری اسلامی، از سهم ایران در دریای خزر به دلیل نوچگی روسیه می‌گذره.
مردم ایران، این روزها رو برای تاریخ به خاطر بسپارید؛ جمهوری اسلامی در حال رقم زدن خیانتی بزرگ به ایرانه.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/69619" target="_blank">📅 14:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69618">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3de4ded641.mp4?token=ofJmCq23j_lKgX7CW8VsxfzPuzXr4JPJ1ODXcRebO3tmvm0jh4TC9pQm0baeYj7IlL-HD1GNF75a0L7ES-to3Wvw0CNeEEZK6X_HTsu7LJvcQZLMk-nYDO94zxnysAKvni4o_1ssSUtqlCJpbIBRzZNYh0GSOw6p_t9_YGKZ4Bv0eaClf7i1MiRoh-U5GJsqnUgYrlfT93xPUfdyCshajd0U6WIDYUmn5jnq7yNnx__MajSCUKc7kk4lcVUST8vCTv04RvLm_SA7K4je_CgWbX4ORYkQG-kR_rfvy4epQyLEEX0irSKEa7NPr_rFU_nlpE1F51j6g47rWcihyXYWyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de4ded641.mp4?token=ofJmCq23j_lKgX7CW8VsxfzPuzXr4JPJ1ODXcRebO3tmvm0jh4TC9pQm0baeYj7IlL-HD1GNF75a0L7ES-to3Wvw0CNeEEZK6X_HTsu7LJvcQZLMk-nYDO94zxnysAKvni4o_1ssSUtqlCJpbIBRzZNYh0GSOw6p_t9_YGKZ4Bv0eaClf7i1MiRoh-U5GJsqnUgYrlfT93xPUfdyCshajd0U6WIDYUmn5jnq7yNnx__MajSCUKc7kk4lcVUST8vCTv04RvLm_SA7K4je_CgWbX4ORYkQG-kR_rfvy4epQyLEEX0irSKEa7NPr_rFU_nlpE1F51j6g47rWcihyXYWyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو ای از صحبت های یک دختر درباره مادرش:
❓
کی گفته هر مادری قابل احترامه؟
از میزان اشغال بودن مامانم اینو بگم که تو سن 13 سالگی پریود شدم و وقتی بهش گفتم منو تو خونه 3 روز زندونی کرد و گوشیم گرفت و کلی کتکم زد
بهم گفت تو چه گوهی خوردی تو هنوز بچه ای چرا باید پریود بشی؟ و این خون یه چیز دیگس!
از 12 سالگی هم منو میفرستاد سرکار میگفت باید خرج مدرسه و خونه رو کمک کنی بدی!
همینطور که اینارو میگفت تا اول دبیرستان بیشتر نذاشت درس بخونم و 15 سالگی ترک تحصیل کردم
مامانم گفت لازم نیست درس بخونی باید بیشتر کار کنی چون خرج ها رفته بالا اجاره خونه بیشتر شده باید بری کار کنی
به محض اینکه هم 18 سالم شد از خونه زدم بیرون و الان 6 ساله نه میدونم کجاست نه شمارش چیه نه باهاش حرف زدم
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/69618" target="_blank">📅 13:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69617">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e79de90eb9.mp4?token=UIgwHemPib2U-cUBxwwE6FqxkakvNFUZ7X5DZxpe8LHl6lOU2rWsZpDE44RE0v67dYLWTYhLXtoRyPTBLuhytWyjElE9pFtVrucUue0K4j8aiGw9zCspkS8-dUGpnB9TNLEBWXMLL2WeElTriSpnGtXIlbBrSHpsHsJF2EjJtzsflUdu1aRXkRUscLA4-ovOW3GjxAD1cYvhuBuxl0fD4qtTtzA9pcd0TYVC6dTqShtOvfBHTUU10HXk8f2I-u_vv3Q5vdyvwiCwSKQNNqHwKbSMaFt27w18NDV3Nw72K2yHoVftsGyzCBW4cvCl6Un5SdsazJeFAgYUQvpSLOO_ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e79de90eb9.mp4?token=UIgwHemPib2U-cUBxwwE6FqxkakvNFUZ7X5DZxpe8LHl6lOU2rWsZpDE44RE0v67dYLWTYhLXtoRyPTBLuhytWyjElE9pFtVrucUue0K4j8aiGw9zCspkS8-dUGpnB9TNLEBWXMLL2WeElTriSpnGtXIlbBrSHpsHsJF2EjJtzsflUdu1aRXkRUscLA4-ovOW3GjxAD1cYvhuBuxl0fD4qtTtzA9pcd0TYVC6dTqShtOvfBHTUU10HXk8f2I-u_vv3Q5vdyvwiCwSKQNNqHwKbSMaFt27w18NDV3Nw72K2yHoVftsGyzCBW4cvCl6Un5SdsazJeFAgYUQvpSLOO_ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلمی که یه خانم حامله ایرانی از میزان تکون خوردن بچه‌اش توی شکمش منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/69617" target="_blank">📅 12:51 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69616">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QK3zh7nVzGOzv8urkM6sKjUUAgz4zdXG7E-PH-y4LRdA6WbpUQQl2Sfho_mUSopr_nZsTr4Y6JQQp065Uc5Y0fYhNSIVKGfca3WE6ZW28fKrIUBhcl8gM9iLwILAlMJoDwodiZD4yB8eiQoQBRuACv5gk1s9U4PeNNrVwzCnH2SRh2p5OxcQZCDuU1_bnxH4KUmx6OO-PUdSn4WAu__hFAHaWJWCGqpn5Li_Oj3a2Jf-lzwTKJ5sMxAv2DPTAFCzytfpxxFa0HsFpe5p4lzR6Ydb8XMRSH0AWQRXEM1hshp5J2j8BJsM_RpJFWmde2lhNvpRjazHy21p-h0wQVp3Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گزارش واشنگتن پست
:
دونالد ترامپ، رئیس جمهور آمریکا، هفته گذشته در کمپ دیوید با پیت هگست، وزیر جنگ، درباره کمبود شدید مهمات در ایالات متحده به شدت صحبت کرد و از او خواست توضیح دهد که چرا به نظر می‌رسد او در مورد این کمبودهای شدید که اکنون تهدیدی برای محدود کردن گزینه‌های نظامی است، فریب خورده است.
ترامپ در جریان جلسه کابینه در کمپ دیوید به هگست گفت که فکر می‌کرد مشکل کمبود مهمات "حل شده است". هگست از خود دفاع کرد و استیفن فاینبرگ، معاون وزیر جنگ، را مقصر دانست و گفت که او اطمینان حاصل نکرده بود که ترامپ به طور کامل از میزان کمبودها مطلع باشد.
در همین گزارش، روزنامه واشنگتن پست به نقل از یک مقام آمریکایی، اعلام کرده است که بیش از ۱۳۰۰ موشک بالستیک تاکتیکی MGM-140 ATACMS ارتش ایالات متحده در جنگ با ایران مورد استفاده قرار گرفته و تقریباً هیچ‌کدام از این موشک‌ها باقی نمانده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/69616" target="_blank">📅 12:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69615">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58d9f385e0.mp4?token=hs0Ra1ODMt_VFgHfth0Ld5WDBR71YzjpBTQhDbpYp-33YMMrpA_Ace8Bp_MKzU4M7_MMan5E1SGj8YeegrjHy5FNFmw49cUdZeRLO6I7dJPD5P01W6WdYP7gzSjpkkWZODDqXQTySivR7erGu2PP4c1LWYdBbVzB9GrXDcNn4BiuAfZ4iIQ0S2r1-fBKffjtpBw0Ih-XzabhuZjVzaAWeduH_T5A9RFITpOHj4Xlvx-VcmGKQnQ--Jcz26VceFS77odXdiIx_4M59-R0cQTmPfdqooiE3rJF868l_s8ZTu4-C7jz5WgliIWcBcdY_cfiSkhgTptpoeKNUyV_lxCjww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58d9f385e0.mp4?token=hs0Ra1ODMt_VFgHfth0Ld5WDBR71YzjpBTQhDbpYp-33YMMrpA_Ace8Bp_MKzU4M7_MMan5E1SGj8YeegrjHy5FNFmw49cUdZeRLO6I7dJPD5P01W6WdYP7gzSjpkkWZODDqXQTySivR7erGu2PP4c1LWYdBbVzB9GrXDcNn4BiuAfZ4iIQ0S2r1-fBKffjtpBw0Ih-XzabhuZjVzaAWeduH_T5A9RFITpOHj4Xlvx-VcmGKQnQ--Jcz26VceFS77odXdiIx_4M59-R0cQTmPfdqooiE3rJF868l_s8ZTu4-C7jz5WgliIWcBcdY_cfiSkhgTptpoeKNUyV_lxCjww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این نقاشی هنرمندانه با ایجاد خطای دید، باعث می‌شه دیوار صاف خونه طوری به‌نظر برسه که انگار داره به سمت بیرون خم می‌شه و برآمدگی پیدا کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/69615" target="_blank">📅 11:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69614">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9KmAVsQxldQPBagcPvceFS3ti8kRj20gpAuRXVzRtq28R9SMfr_nj-IDQKdk0PoIa_pZkSMDrZp32AcyvfBVFsxCC7p0feMkRAJVWtFR7iR1eqSkIElBv-2gKrdGRxWjdnPZKacnKa58d8nzNQvSDE_rJH8o-FgUVTjMD5g59X_Yju_e2csyeSm5BmFC3VIVmVm9i_G0BvTBQZ-N3YQ6Per7rFpHFOz5Lss2HlpmHHqyIl_saKpV9OM2Nv5Y_hrotyrii7eclDEgzYPswcZK9iT4Vrl6pjc8P_1Xj1nlliNnBVjXNo1OSxY99EWFfNyRY6VpVu8Yc4KVbISN3Aasw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرکز عملیات تجارت دریایی بریتانیا (UKMTO)؛
پس از دریافت گزارشی از ناخدای یک نفتکش در حال عبور از تنگه هرمز، هشدار صادر کرد؛
این ناخدا گزارش داده بود که صدای دو انفجار را در فاصله تقریبی ۹ مایل دریایی در جنوب شرقی «کومزار» عمان شنیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/69614" target="_blank">📅 11:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69613">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54b71c6863.mp4?token=L2UgWNTcy5ZTHUm4SgJyCIcPXMfjYVvBx6IADUHUcQn4NdvFCBJPa2Nvyk9RZrumovA4bUQaX6BIQbDroVftJ_Ys8WF6nKG5X91--p1oGigf4-itp6_mQreOC7Y1LnnUw1-3NLpcror5dDi_OjNxnjyshKzHJufrenztCC4K8CIGL_GtNQ7luu9pSuXOEQasBERl6-7r5IJe5JDCpSu2keXWppD8_ZRSZs4nEVL55NXNa0NIBEpoSpjLTizr-uztshtG7Vky__XElBS9_x8jgxuoBgff-tS3ltmF1wahOat7sa0sDA1pSRBHL4bK0F2Ygq3MLlz4Nvn4sBpH6_nggw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54b71c6863.mp4?token=L2UgWNTcy5ZTHUm4SgJyCIcPXMfjYVvBx6IADUHUcQn4NdvFCBJPa2Nvyk9RZrumovA4bUQaX6BIQbDroVftJ_Ys8WF6nKG5X91--p1oGigf4-itp6_mQreOC7Y1LnnUw1-3NLpcror5dDi_OjNxnjyshKzHJufrenztCC4K8CIGL_GtNQ7luu9pSuXOEQasBERl6-7r5IJe5JDCpSu2keXWppD8_ZRSZs4nEVL55NXNa0NIBEpoSpjLTizr-uztshtG7Vky__XElBS9_x8jgxuoBgff-tS3ltmF1wahOat7sa0sDA1pSRBHL4bK0F2Ygq3MLlz4Nvn4sBpH6_nggw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
حسن روحانی: اقلیتی می‌گوید اگر این جنگ تشدید شود، امام زمان زودتر ظهور می‌کند! می‌خواستند برای سخنرانی امام زمان در تهران جایگاه درست کنند.کاسبان تحریم ممکن است خوشحال باشند که جنگ ادامه پیدا کند.
عده‌ای دنبال کاسبی از جنگ هستند و از ادامه آن خوشحال می‌شوند.
در جامعه ما گاهی یک اقلیتی هستند که حرف‌های عجیب و غریب می‌زنند.
یک اقلیتی هستند می‌گویند اگر این جنگ تشدید شود و گسترش بیابد، امام زمان زودتر ظهور می‌کند! برای ظهور امام باید جنگ را تشدید کنیم.
خب یک عده افرادی هستند که نه با اسلام آشنا هستند و نه با مهدویت آشنا هستند.
یک عده هم هستند که دنبال کاسبی هستند، همان کاسبان تحریم در واقع. آن‌ها هم ممکن است خوشحال باشند که جنگ و آشفتگی ادامه پیدا کند.
افرادی هم هستند که ممکن است یک تفکراتی داشته باشد که ما باید برویم جهان را بگیریم و تصرف کنیم و همه را به اصطلاح هدایت کنیم.
من در سال ۸۳ رفتم خدمت رهبری برای یک موضوعی، بحثی پیش آمد در آنجا، ایشان به مناسبت فرمودند که فلان آقا، اسم بردند، آمده بود پیش من و از من سؤال کرد که می‌خواهد یک جایگاه بزرگی درست کند در یک میدان بزرگ در تهران. گفتم جایگاه بزرگ برای چه؟ گفت برای اینکه وقتی امام زمان آمد و خواست سخنرانی کند یک جایگاه مناسب و باعظمتی باشد در شأن ایشان.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/69613" target="_blank">📅 11:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69612">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxGLgKUB5OwXoXrDgl1W5WfwLOBB1W-z8Jn3KuUQ0kXzLvqPZN_YNy5OiD-I3QWtwWBrCwDC7NAXXnuf8uCaCRWmpTc-cb4H2mI-ftuEGDaPUU-wZdvtsqJzYXHZ6RQjj-tTwa6xC0Ch90EVd64KXwlRbk00qs11xbSvNeNtA38RxhygkdaEBqQTOxBkDz4NBswDsffm1_8y1jR2XLTaYnz9-AngqZYMd0iEyFKj80taS4nuvfkZ2FYXiSlL9Q9_mXPqNsyPbHSxkTxfO-VShfCEMLNqOwORDNy_yQaZWKvZHVY1rop1Y1CYQfq_b4vnCCHyQiTIGpCQq0s9nKuSbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐
اکانت رسمی تلگرام زیر توییت یه کاربر:
یه نفر پرسیده بود: می‌خوام بدونم دورف(مالک تلگرام) کجا قایم می‌شه؟
تلگرام هم جواب داده:
درباره خودش چیزی نمی‌دونم، ولی معمولاً منو خونه مامانت می‌تونی پیدا کنی
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/69612" target="_blank">📅 11:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69611">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69611" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پنالتی
راحترین بازی پولساز
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید راحتو سریع برنده شو
👌🏼
💖
مرجع
بازی های روز دنیا در ‌پلتفرم جهانی بت اینجا
⭐</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/69611" target="_blank">📅 11:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69610">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58d65b8db.mp4?token=qk-nFtGfPMCXwzYyQQwHRuHXTqBuwSWtMYmsaS-Ki8BZj23m4-9bkuploofbnJZKMJCIYJaRIW0U_6JsoX07Fbe8Ume-Zfc_58mg_PycZbbET02N77dFYSgyy_y37mh16PXiI5ysJpBeAWB6nkp6jG2n9-xc5FsKWkezHf-NpJfH5Oiz-8f1eQtXpVGaRx9mBmO3IF-KKlo3mu1Dbz9riVLDdxLP8kG1Evn93tfXXPI350afgecWvg7rnhvTIM9yp2ucz7ADz7sAaeOslQHJo0cfgthuRt2cpTXWZuZ8QWFJNw9XtoOmFmmap4fuKrHXck6LqD7_NODvkZwT55Rpa4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58d65b8db.mp4?token=qk-nFtGfPMCXwzYyQQwHRuHXTqBuwSWtMYmsaS-Ki8BZj23m4-9bkuploofbnJZKMJCIYJaRIW0U_6JsoX07Fbe8Ume-Zfc_58mg_PycZbbET02N77dFYSgyy_y37mh16PXiI5ysJpBeAWB6nkp6jG2n9-xc5FsKWkezHf-NpJfH5Oiz-8f1eQtXpVGaRx9mBmO3IF-KKlo3mu1Dbz9riVLDdxLP8kG1Evn93tfXXPI350afgecWvg7rnhvTIM9yp2ucz7ADz7sAaeOslQHJo0cfgthuRt2cpTXWZuZ8QWFJNw9XtoOmFmmap4fuKrHXck6LqD7_NODvkZwT55Rpa4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
آقاآآ این بازی
#پنالتی
چقدر خفنه
⚽
🟢
بازی خیلی حرفه ای و‌
#پولساز
پنالتی فقط‌ پلتفرم جهانی و معتبر
#بت_اینجا
✊
همین الان ویدیو
#آموزش
پنالتی زدن ‌رو ببین و با شارژ اضافی
🤩
🤩
درصدی که سایت بهت میده.
💖
حتما ویدیو
#آموزش
رو ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
r15
@betinjabet</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/69610" target="_blank">📅 11:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69609">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1558a77094.mp4?token=PY3bsXkG3DYkeJVIWBJLxSVhxirzLboyUVORauE7nzwN87mCDrGnUqmwMYEtqAke3xqqoQk0Iqhtx5t0GN5XQ7CgbCD1jM188yWMfipEi6OnIYFF_OqMynHV8ogjoSt8aLcC-vnbESvVSwGVVlX6ZZS1-lZW8YBVBTq0nRAbrJNjBS54Do0BIZ9UzOiNe2eGPxK5KzwFH9bTxWxdzxlZwm4A8J1lkxDJNgG07lKYqhlkT8C7pRjNAX6LTev8R151rVbOi1J4m79rT0eUlR8TwYkh1b_LiojTGoIsJPzB-6dJjGbT7E_jB8ChbI9Pz86j_X29RBMq03BWHp7_EWZqfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1558a77094.mp4?token=PY3bsXkG3DYkeJVIWBJLxSVhxirzLboyUVORauE7nzwN87mCDrGnUqmwMYEtqAke3xqqoQk0Iqhtx5t0GN5XQ7CgbCD1jM188yWMfipEi6OnIYFF_OqMynHV8ogjoSt8aLcC-vnbESvVSwGVVlX6ZZS1-lZW8YBVBTq0nRAbrJNjBS54Do0BIZ9UzOiNe2eGPxK5KzwFH9bTxWxdzxlZwm4A8J1lkxDJNgG07lKYqhlkT8C7pRjNAX6LTev8R151rVbOi1J4m79rT0eUlR8TwYkh1b_LiojTGoIsJPzB-6dJjGbT7E_jB8ChbI9Pz86j_X29RBMq03BWHp7_EWZqfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپی که حامیان حکومت برای موشک‌ها درست کردن
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/69609" target="_blank">📅 10:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69608">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc659092fa.mp4?token=bw1bdbN3MoYH_DqEGBQMWfi21YL7IxMKIN2tEVBuca0z9EsjhP71DRkBCCO4kABLdvcphhhgcchJyHYjCfB8AAX4hiXxdHoe8yJpnBhaIbvachwnEscblrIOX_R66W9XhqVFl9cJ1ZFmCNeyTaB8M3YRZo0OlrfZtD5Pdag4zz9-bi8L-RTyxtwSkXUtDKURuynv_TZIql0SBqh6xhuVJrx2xLSFyD9DiW8FQvDOUphYqE5QtKNCiWt-fZe2c79WrshvXpg8g_jD7UtuMeJFnDUoHQdsac8ZJHPb-34m8Yt6Dyu-fzN4kOdIKg51UyeIT6kXFbSp4d9ECvJ2NyZlRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc659092fa.mp4?token=bw1bdbN3MoYH_DqEGBQMWfi21YL7IxMKIN2tEVBuca0z9EsjhP71DRkBCCO4kABLdvcphhhgcchJyHYjCfB8AAX4hiXxdHoe8yJpnBhaIbvachwnEscblrIOX_R66W9XhqVFl9cJ1ZFmCNeyTaB8M3YRZo0OlrfZtD5Pdag4zz9-bi8L-RTyxtwSkXUtDKURuynv_TZIql0SBqh6xhuVJrx2xLSFyD9DiW8FQvDOUphYqE5QtKNCiWt-fZe2c79WrshvXpg8g_jD7UtuMeJFnDUoHQdsac8ZJHPb-34m8Yt6Dyu-fzN4kOdIKg51UyeIT6kXFbSp4d9ECvJ2NyZlRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🇮🇷
پزشکیان:
حوادث دی‌ماه پارسال قابل فراموشی نیست؛
یه عده بیگناه هم قاطی اون اون افراد تو خیابون ها شده بودن
وقتی روند به شورش رسید اتفاقات سختی رخ میده و ما دیدیم شرایط اینطوریه گفتیم کد ملی اعلام کنن و هرکس اضافه تر میگه هست خب بگه
کسانی که کشته‌شدگان رو ۳۰-۴۰ هزار نفر اعلام می‌کنن، نامرد و وطن‌فروش هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69608" target="_blank">📅 10:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69606">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c8bd143a1.mp4?token=k8WahlDW11x3V-jzss1ThYjcLQi1xxIU5Ohjs_RVrfbCnOhlpS1omaUAwl3mY-8Qt-F0HvIcmOrMDZotBzsahj-41Jj3BRE0J8SiNYRnEDXT5J1RsbotGa1TWA9SKWlHx_O6S5kTIi2ZolapO83d2oyuzV6vdd5JDagzfi4oNCgiaUjN4VxtREJkxP1P4gdqPuNUKqY1DbdCMycvjxl_Dai1aPo6mQT8dJnTTiZnRVbMyVf5bivgLbeb5cDRuQEyZitgudsVDjaxsdAZAlGRGAejlE6tQwoo5pj6JEcvGwaqOpbY_2qUO5y6MAconwDboC6PhX6SRLHPDmOgnxqS-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c8bd143a1.mp4?token=k8WahlDW11x3V-jzss1ThYjcLQi1xxIU5Ohjs_RVrfbCnOhlpS1omaUAwl3mY-8Qt-F0HvIcmOrMDZotBzsahj-41Jj3BRE0J8SiNYRnEDXT5J1RsbotGa1TWA9SKWlHx_O6S5kTIi2ZolapO83d2oyuzV6vdd5JDagzfi4oNCgiaUjN4VxtREJkxP1P4gdqPuNUKqY1DbdCMycvjxl_Dai1aPo6mQT8dJnTTiZnRVbMyVf5bivgLbeb5cDRuQEyZitgudsVDjaxsdAZAlGRGAejlE6tQwoo5pj6JEcvGwaqOpbY_2qUO5y6MAconwDboC6PhX6SRLHPDmOgnxqS-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
باقر خرازی (برادرزن مسعود خامنه‌ای):
ما باید از جمهوری اسلامی گذر کنیم. علت اینکه این الدنگ (پزشکیان) رئیس‌جمهور کشور شده و بی‌حجابی کشور را گرفته این است که هنوز از جمهوری اسلامی به حکومت اسلامی گذر نکرده‌ایم.
خدا لعنت کند شورای نگهبان را که این "آشغال" را توی پاچه ملت کرد.
چهل سال است با آقامجتبی رفیقم؛ او بسیار تندتر از پدرش است؛ اما یار ندارد.
باید به نیت حضرت فاطمه از هر شهر ۵۳۰ نفر جمع کنیم و به تهران سرازیر شویم و کار دولت پزشکیان را تمام کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69606" target="_blank">📅 09:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69605">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e59bbff0.mp4?token=C0kxf-l1Hr2A3Vh4FzIwYIctlfma0IZku8dlF5L2F2B9_Pdpy0Cs1w2OP_hrB1JmoIi4neHzFcloC-UjgMsw0Ha9EGjSjmECqjoR5dWmJtwkjy3ReB9GF03b7Sm5nqerPnN4qEH-zVP_Stcv-hlsX3w2PAKKVRL0svYmHf8FRC-Qv0_JWaK2WtBFpEx-qOZuobifihxZpKjb_IhOB3p2dtOhv3JrijPwKKmz2SpzkOjYKxYDXiOywR73KF6SYciZoSbf6kY8D-hg_hB2Et5neqhtd0SzY1ZCsiMYetBpdgZeY1yxIn4Fi3MgnZdTYWJTNBZ1a5hNrDOg2nDR4Hwj3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e59bbff0.mp4?token=C0kxf-l1Hr2A3Vh4FzIwYIctlfma0IZku8dlF5L2F2B9_Pdpy0Cs1w2OP_hrB1JmoIi4neHzFcloC-UjgMsw0Ha9EGjSjmECqjoR5dWmJtwkjy3ReB9GF03b7Sm5nqerPnN4qEH-zVP_Stcv-hlsX3w2PAKKVRL0svYmHf8FRC-Qv0_JWaK2WtBFpEx-qOZuobifihxZpKjb_IhOB3p2dtOhv3JrijPwKKmz2SpzkOjYKxYDXiOywR73KF6SYciZoSbf6kY8D-hg_hB2Et5neqhtd0SzY1ZCsiMYetBpdgZeY1yxIn4Fi3MgnZdTYWJTNBZ1a5hNrDOg2nDR4Hwj3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
ممکن است دوباره قیمت نفت را «بالا ببریم»:
«قیمت ۷۵ دلار است. ممکن است مجبور شویم دوباره آن را بالا ببریم. خودتان می‌دانید وقتی آن را بالا می‌بریم چه اتفاقی می‌افتد.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69605" target="_blank">📅 02:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69604">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69604" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69604" target="_blank">📅 01:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69603">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=SuFsuZlEmRCUrVjj50D-sxLa6U_s-AhzT3JjFTJ9EVo9R1ZqdksjqKKDQUx0h_Tis_nKEWNhp4spotVsvm_YtvmEZLYllOxoH34K3SZQe26kYmdpMMiE76Sl_H4qq7sCCQYlUjEo_2uw38UEcrOBRZKS6SmH2VNNumolPFvIiASBIeo6iEZojnfBMWBWwk9UQz4YWr4xHEHe3_MpoM5Caf5J0P2ytv3peRenwQP8uN5pAKOfNBsR1SltQ0rp2QHCvtSE4zJDCIJ_amDUxEYSAzTlgKHyE1W3OPkIHp4wGL6sJvS6n2nLZ_5EM00MOd-N9G0Z2RBalxJ6ljeNcK9opA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=SuFsuZlEmRCUrVjj50D-sxLa6U_s-AhzT3JjFTJ9EVo9R1ZqdksjqKKDQUx0h_Tis_nKEWNhp4spotVsvm_YtvmEZLYllOxoH34K3SZQe26kYmdpMMiE76Sl_H4qq7sCCQYlUjEo_2uw38UEcrOBRZKS6SmH2VNNumolPFvIiASBIeo6iEZojnfBMWBWwk9UQz4YWr4xHEHe3_MpoM5Caf5J0P2ytv3peRenwQP8uN5pAKOfNBsR1SltQ0rp2QHCvtSE4zJDCIJ_amDUxEYSAzTlgKHyE1W3OPkIHp4wGL6sJvS6n2nLZ_5EM00MOd-N9G0Z2RBalxJ6ljeNcK9opA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
به راحتی کسب درامد کن
💵
💰
🟢
ویدیو
#آموزش
بازی chicky choice رو براتون گذاشتم خیلی راحت و بدون ریسک و میتونی بازی کنی و کلی پول دربیاری
🔥
💖
حتما ویدیو رو تا انتها ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
a14
@betinjabet</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/69603" target="_blank">📅 01:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69602">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79ecaba828.mp4?token=j1NZ1EG8UW5hB7_h-gB1teuc-Zf3uwX07YKTOEHlU28ytUtV0pDOPqGMlxABmDie7JAg32XRQ-wJmRsfxEC-CsV-JlgThDqxjRAwmSvm2sAyPsS7zt7WhzRfbdDdqFLJn3C1sLLhdEbXcNIFqey1Yu_uGc1BBEr528VyWixe9dn8F26Hj4JR2nFw0d5Z1BSUp4IhAoA94vJFihThuMoLb_wCKP7SNarhj5uz7iaJJxxA27qOFAPs2CZmlsi1FA6j6YvRSswSAxPtJMn3lZtWdf6f4YQqqY6o0HomjnoE8cHE4eNV-EVWosznNrC2ttuazqWxkixucqkUcOfhS1TpXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79ecaba828.mp4?token=j1NZ1EG8UW5hB7_h-gB1teuc-Zf3uwX07YKTOEHlU28ytUtV0pDOPqGMlxABmDie7JAg32XRQ-wJmRsfxEC-CsV-JlgThDqxjRAwmSvm2sAyPsS7zt7WhzRfbdDdqFLJn3C1sLLhdEbXcNIFqey1Yu_uGc1BBEr528VyWixe9dn8F26Hj4JR2nFw0d5Z1BSUp4IhAoA94vJFihThuMoLb_wCKP7SNarhj5uz7iaJJxxA27qOFAPs2CZmlsi1FA6j6YvRSswSAxPtJMn3lZtWdf6f4YQqqY6o0HomjnoE8cHE4eNV-EVWosznNrC2ttuazqWxkixucqkUcOfhS1TpXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ترجیح می‌دهم با ایران توافق کنم، چون نمی‌خواهم آدم بکشم.
ایران به ما احترام می‌گذارد. آن‌ها به ما احترام می‌گذارند.
ما در حال گفتگو هستیم. ببینیم چه می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69602" target="_blank">📅 01:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69601">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca4b2dd818.mp4?token=pxUSujv-3Rl8OiXXfMvXLYQljw0mo51GFW8ZDb0LvoCtRaVORXWB81jSXuiKBtWH2sd4-Xg2MD7phzG2BMS4XF2Erb4x2xsuRjOYh7nEwtKX9peUiEuMw_pLyfMuQxGMlZl826lDC1UyDVq5TziGq_VT14pmXqWfuje0RWTQQ21CoOc0vB_2W43L1aXhhRC9SrQJu0GhvTa2mzscn0kpvQU-hI-yjZH_bFfE0R2lB2zGR2NWqkSFR9j6PxxC1zOIdaAmU-3K_QxpacqqVMiOot7diJfiEjegIgNHk1Ml3cPEUFaTA24hKdiRWXGdWj4D5Y7DVXAf7j2-WNobMxTvoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca4b2dd818.mp4?token=pxUSujv-3Rl8OiXXfMvXLYQljw0mo51GFW8ZDb0LvoCtRaVORXWB81jSXuiKBtWH2sd4-Xg2MD7phzG2BMS4XF2Erb4x2xsuRjOYh7nEwtKX9peUiEuMw_pLyfMuQxGMlZl826lDC1UyDVq5TziGq_VT14pmXqWfuje0RWTQQ21CoOc0vB_2W43L1aXhhRC9SrQJu0GhvTa2mzscn0kpvQU-hI-yjZH_bFfE0R2lB2zGR2NWqkSFR9j6PxxC1zOIdaAmU-3K_QxpacqqVMiOot7diJfiEjegIgNHk1Ml3cPEUFaTA24hKdiRWXGdWj4D5Y7DVXAf7j2-WNobMxTvoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
هیچ‌کس نمیدونه که کلمه «dumb» حرف «B» نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69601" target="_blank">📅 01:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69600">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇷🇺
🚀
ویدئو منتشرشده از شلیک گسترده موشک‌های اسکندر به کی‌یف و حومه آن در روز گذشته.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69600" target="_blank">📅 00:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69599">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTaJ9YZPScV5_S6PgHLPuPGYOCuh5GxbxtGcUQR0V3QXgMVcOw-oVPwmw1hbrQ0TdCE_O1wyAOitU94-MfXbvo-C7cah1vfDHvxH_vTRVah6OVFuUa0W_kUusOecySuinwcMtipDk16mfcjmK-cOUjD86xHJ1Wp7x_o27mfyj-AyCNach0GRqu1qOij5QuRVIIbbxWIQ-0wQUUg44iqztcaG4fkRuzbyAl3PXypvNiJmwUcBk7FB9MoGDKtNSq-elXVvfBL90kYXy4djLAV8LTaf73oT2xmUdCBzbUEnfRH8ks0rwIj0PRha9JyfuU4_HY7sBSssI7FWDc-frNNnMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ مود:
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69599" target="_blank">📅 00:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69598">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82acfe6016.mp4?token=f-vbOAVl0rYyNbMDT_37dGmw_H9dCwUD0h-rIoaG4SfcgOvaxhJJnicscVqmmdWNkFvR35KBj09DMP7qJzYc_B_-jy8DuWAuC12WbTms5HKZkXx-z0PwhvsN3-6yDjxVOeMqYRC-i3wqtOqaT6MYUHLh1J2Aobnh0UhqfFxCm8mYXDwxS9gphyKSZJmfJuznswcj70LbmlW47WOYd9zFQ-CNyOj1JS7qNBGJNdOf81kKBfdeo6pwPoVV1g3LEvGbWu2dQhHDsoO90bruaXKVUni0ONPSv0DnHN3yXn1zCXF657kux97hAdiG-1ib71se5yfK7CCJ6Mi7Qf66PS-LDg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82acfe6016.mp4?token=f-vbOAVl0rYyNbMDT_37dGmw_H9dCwUD0h-rIoaG4SfcgOvaxhJJnicscVqmmdWNkFvR35KBj09DMP7qJzYc_B_-jy8DuWAuC12WbTms5HKZkXx-z0PwhvsN3-6yDjxVOeMqYRC-i3wqtOqaT6MYUHLh1J2Aobnh0UhqfFxCm8mYXDwxS9gphyKSZJmfJuznswcj70LbmlW47WOYd9zFQ-CNyOj1JS7qNBGJNdOf81kKBfdeo6pwPoVV1g3LEvGbWu2dQhHDsoO90bruaXKVUni0ONPSv0DnHN3yXn1zCXF657kux97hAdiG-1ib71se5yfK7CCJ6Mi7Qf66PS-LDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فیلم وایرال شده از یه کارگاه آموزش فن بیان توی تهران.
چه خبرا؟ به لطف شما:))
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69598" target="_blank">📅 23:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69597">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51c05821a8.mp4?token=kTqoK6RLlKZgYkuUfgt0Ir1O2X3rg5u7WcWX8WZ_qlzeko3jIBZy5NYFEhhTfKvFTSGL6mdD-ylycHO1ccjbu90cEp1MSM9BgiyfAWK6f1Cwuf56W_4E5BKYS5En9amcMgmhPVe9uA1dZab0muU9R6UzgtAflv9BOuPZ8jN3QiZFSqgyq4vi7QHzdD4AiIL-PHNLr9IDr9D-1b1X93ezER87Z_QzEkPUTz-2tyZ5QF4LfANtimEVuaJuYhgL__aMsHqY4Gm1mDoQa5vSZbLn68X4aQM58CQE5r3akXAEDJvoAEVyccQHjGav7cpRNR2Zs1ZedqnmEdUH4PBjOQRF1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51c05821a8.mp4?token=kTqoK6RLlKZgYkuUfgt0Ir1O2X3rg5u7WcWX8WZ_qlzeko3jIBZy5NYFEhhTfKvFTSGL6mdD-ylycHO1ccjbu90cEp1MSM9BgiyfAWK6f1Cwuf56W_4E5BKYS5En9amcMgmhPVe9uA1dZab0muU9R6UzgtAflv9BOuPZ8jN3QiZFSqgyq4vi7QHzdD4AiIL-PHNLr9IDr9D-1b1X93ezER87Z_QzEkPUTz-2tyZ5QF4LfANtimEVuaJuYhgL__aMsHqY4Gm1mDoQa5vSZbLn68X4aQM58CQE5r3akXAEDJvoAEVyccQHjGav7cpRNR2Zs1ZedqnmEdUH4PBjOQRF1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇺🇸
دیروز یه خبرنگار از بقایی، سخنگوی وزارت خارجه پرسید چرا جواب صحبتای ترامپ رو نمیدید؟
بقایی گفت چون باید رفتار ایرانی داشته باشیم و حرکات زشت دیگران رو الگوبرداری نکنیم. آخرشم یه تیکه از یکی از حکایت‌های عبید زاکانی رو گفت : "فعل و عمل ما را و دعوی ایشان را"
🔴
حکایت کامل عبید زاکانی:
شخصی اَمردی به خانه برد و درهمی به دستش نهاد و گفت: بخواب تا بر نهم. اَمرد گفت: من شنیده‌ام که تو اَمردان را می‌آوری تا بر تو نهند. گفت: آری، عمل با من است و دعوی با ایشان. تو نیز بخواب و برو آنچه می‌خواهی بگوی.
🔴
حالا معنی حکایت:
یه مرَده یه جوون بی‌ریش رو پیدا کرد، یه سکه بهش داد و گفت دراز بکش تا باهات همبستر بشم [ کونت بذارم ].
جوون گفت: من شنیده بودم تو جوون‌ها رو به خونه میاری تا اونا باهات همبستر بشن [ اونا کونت بذارن ] نه تو.
مرد جواب داد: «درسته؛ عمل کردن از طرف منه، اما حرف و ادعا با دیگران. تو هم فعلا دراز بکش، بعدش هرچی خواستی برو درباره من بگو
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69597" target="_blank">📅 23:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69596">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
ترامپ بهترین دوست ماست، اما می‌خواهم یک موضوع رو روشن کنم: "موجودیت اسرائیل قابل مذاکره نیست.با توافق و مذاکره یا بدون آن، هر کاری لازم باشد برای تضمین آینده‌مان انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69596" target="_blank">📅 23:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69595">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Esgard-VPN.apk</div>
  <div class="tg-doc-extra">42.4 MB</div>
</div>
<a href="https://t.me/news_hut/69595" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پیشنهاد_ویژه
فیلترشکن محبوب اسگارد ‌وی‌پی‌ان
تقریبا با همه‌ی اینترنت‌ها کیفیت اتصال و سرعت خوبی داره. حتما امتحانش کنید
لینک گوگل پلی:
https://play.google.com/store/apps/details?id=com.vpn.esgard&referrer=628035</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69595" target="_blank">📅 23:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69592">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kpAnE54Gyh5M_6D8K0T6vk3GsGNxEFlhNLz5wJ8dOj-RSoOXolR9UqMnz0zxBa5ZqC745bFQS1REPQazzsHQWQ-TLslDfXoO1AOmEYePxSmUf7_2oeDjrz-_4kBO6uLBH4d8nZs6_TLyyRnNogSlvNCF24MkleiZqWiWvcvP04SSxah30bBz7AMw1eRJ7KMx7TFaCVwZ1ZbNR0QJcYsrl4e-M-6GYsAJRpRy469A6wGLgSwu2vmwnazUuYH4KV-74F_zguBvOA5X3ED2h1kAmecd4QhKdoXM96HUul7Bq6ge7VIkFW1eavKeIAZ4zNn-1-4HPYMhzfJrPIqdgGfcFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dVjCxnzpxsGLnxvH22EnxgKrGwAP4xI_rtZKgCJIzhUV6bpqnfGom3086yLyj1I9-eujSSkVf3Edl5cCV9ffAAYkehHRjqO8RPIU5Rsfq2WrUiFA5pKq9j6f1RmVIBnvI1pevbdA7BBHB33c3zR_znnSzjSk16hwrL5BSESuoYiv3ui_V7NyD4Xu6uqfAZ5nczuhCqLevpL-xB3TEA8jZq_jJNPjCKfkTXYub2WzLNK35hKirw75FdNTAkLSHJF2hHqVTUKpT1SDEDAX_iAEuAnGU5QOUgCvcTTbIHVcofOG_UxZz0Zdt1joNQHoFJOf22mzxAnyCYxPn9xc2oN36w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6780226a9d.mp4?token=v5wE3m6eAmBAWKBKvSN41YK_ljRbn8FsCp2tHUC9ED5W9qyiNbv9Xl48uT8Cx5rUn1IMn5r1bL6bKrog_mKXl1Odu36ryh07OEI1E1FzF-3aXB2MCI64zrFpDlgKeSgIcmvX3lBeWJBq7sCYLxoC09g8UIGHkYr_iv7LefBUCmiwkPI3NR0FtqDJ9jN0xeRMLZnfUL7ybawRuYmAbR20f6t7ydXGAdDvrgk0gnhBnHWBjE3OY3jTvXpekDacJ9SFmCF0siKj1L7h7XnAYgCrnjgvYOfUDR3uFA4PEX2woKiZMRyfoTKasTLtLuBPvCQDWQEUnJcGLRxgzyekQ1ko-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6780226a9d.mp4?token=v5wE3m6eAmBAWKBKvSN41YK_ljRbn8FsCp2tHUC9ED5W9qyiNbv9Xl48uT8Cx5rUn1IMn5r1bL6bKrog_mKXl1Odu36ryh07OEI1E1FzF-3aXB2MCI64zrFpDlgKeSgIcmvX3lBeWJBq7sCYLxoC09g8UIGHkYr_iv7LefBUCmiwkPI3NR0FtqDJ9jN0xeRMLZnfUL7ybawRuYmAbR20f6t7ydXGAdDvrgk0gnhBnHWBjE3OY3jTvXpekDacJ9SFmCF0siKj1L7h7XnAYgCrnjgvYOfUDR3uFA4PEX2woKiZMRyfoTKasTLtLuBPvCQDWQEUnJcGLRxgzyekQ1ko-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو لیگ دسته سوم تایلند، بارون میباریده، ولی همینطور فوتبال بازی می‌کنن
یهو یه صاعقه میزنه و صاف میخوره به یه بازیکن و اون بازیکن فوت می‌کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69592" target="_blank">📅 22:32 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69591">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvWg1y3cP7Klh5_CAHbtXxpy_kF9jhy14KFi0X6m200jqjSvx6N2I_ajP803i9w0-EyZqS7dJwgAFujXPE7qfMrCfrYxhKCRyPCTpHeOcJkw84E0LYG0g7HkCHstoGwIdSSF56wwDU-GmNva9POxhZIeI_z7ZDG5HAooKJZfhcnvJZbQDnwMSYzp6sajYsg9inHDvZsXSHe2drNvkEvhEEwZLyt8262jy9Xm2SmQnEwKNoKGp2vn9Pw-BF1BFEqJ3LMKshvV-0uP2Y-qncQOji0uU9FZ0aijlnjLZeratz8oWs5V_OvWuHjRyCW5uwDJfSbMDh9c4Z9zAeHtO4lVcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
🇮🇶
وزارت خزانه‌داری ایالات متحده تحریم‌های اعمال شده بر شرکت هواپیمایی فلای بغداد و چندین فروند از هواپیماهای آن را که در سال ۲۰۲۴ به دلیل ارتباط ادعایی با نیروی قدس سپاه پاسداران در فهرست تحریم‌ها قرار گرفته بودند، لغو کرد.
این لغو تحریم‌ها، شرکت هواپیمایی فلای بغداد (که با نام عراق اکسپرس نیز فهرست شده است) و دو هواپیمای بوئینگ ۷۳۷ (YI-BAF و YI-BAN) را از فهرست ویژه اتباع تعیین‌شده توسط OFAC حذف می‌کند و به تحریم‌های مرتبط با تروریسم آنها پایان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69591" target="_blank">📅 21:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69590">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPaw0qx88yQMq1jxFX5FY-nOAHIG8Gxx5aUMmCLDDRekkKKMOtLXhLl_C7HE6lzRfiGJTlfu2VgMizad0KFi7jkKvQ1honHiSLQmIzDtepNfoDoWg-W_xml1R7mJGi45kF5av7OR7icUBGSZ7Qrjay0YECSGn6pmGB0tKUm-0IJhnrUxM7fU-ylyP5xgH8T0SVQZrwKABnZiQ8Z-DVHNWoUdFd_ZAdRPonYFp4wnO8cDufZWYwUma_JFVISsRNPd8GiqrubIS1cfDMbtfgrab-_KXBCG19TltHPlTzZbOvFEiBYkgzKz4o5YPrUfnq8MvN4xQCcAkR95x-M9ijnM8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
غریب‌آبادی، معاون وزیر امور خارجه جمهوری اسلامی:
ایالات متحده تقریباً ۴ یا ۵ روز پس از آغاز دور جدید درگیری‌ها، پیامی مبنی بر درخواست مذاکره و حل‌وفصل مسائل ارسال کرد.
هرگونه توافق در خصوص تنگه هرمز باید صرفاً میان ایران و عمان باشد.
ما هیچ‌گونه دخالت خارجی در تنگه هرمز را نخواهیم پذیرفت.
با اجرایی شدن توافق جدید، مسیرهای موقت فعلی در تنگه هرمز بسته خواهند شد.
بخش قابل‌توجهی از مسیرهای تردد کشتی‌های ورودی و خروجی به آب‌های سرزمینی ایران از این مسیر عبور خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69590" target="_blank">📅 21:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69589">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca751f3e8.mp4?token=GQAuoe0pmBOIdAIPeZY8E0BSjVrZWdT8_0ihmgxCcjz48n4-NQRWsPGK23_as7Q1zvwU3_tcc7Cileb3b-14fC1I1erQogllKPncSUF1dXBz481cieZ1UBF4NuTBtjMK_bCZwrEFXe4jle9qSU6Fqm3IZIJIoRZmXrflF7Pf-ldrgNoYl6uHpi6yUBL7w-9TrkQ4XPwFd0XsmCLm3rPsuiCBDhnFm0KYzou9kDdus0_8bQ-MB8eSg9tXy7bSnRafSJAnrk470bE5qDTs6EH2VJKTVzpDO9I5W6kl0ahbnJDo2pq7DlBc5sb1LsjGMz--DmKxsrEGVN5h2U-fze4jVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca751f3e8.mp4?token=GQAuoe0pmBOIdAIPeZY8E0BSjVrZWdT8_0ihmgxCcjz48n4-NQRWsPGK23_as7Q1zvwU3_tcc7Cileb3b-14fC1I1erQogllKPncSUF1dXBz481cieZ1UBF4NuTBtjMK_bCZwrEFXe4jle9qSU6Fqm3IZIJIoRZmXrflF7Pf-ldrgNoYl6uHpi6yUBL7w-9TrkQ4XPwFd0XsmCLm3rPsuiCBDhnFm0KYzou9kDdus0_8bQ-MB8eSg9tXy7bSnRafSJAnrk470bE5qDTs6EH2VJKTVzpDO9I5W6kl0ahbnJDo2pq7DlBc5sb1LsjGMz--DmKxsrEGVN5h2U-fze4jVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
❌
🇮🇱
امروز در پی وقوع انفجار در ساختمانی تله‌گذاری‌شده در «مجدل زون» واقع در جنوب لبنان، دو سرباز اسرائیلی کشته و هفت تن دیگر زخمی شدند.
حالا قراراست بنیامین نتانیاهو، نخست‌وزیر اسرائیل، و یسرائیل کاتس، وزیر دفاع، ساعت ۲۱:۰۰ به وقت محلی نشستی امنیتی برگزار کنند. محور این جلسه، حادثه مرگبار امروز در جنوب لبنان است که منجر به تلفات متعدد در میان نیروهای اسرائیلی شده است.
به گزارش شبکه ۱۴، انتظار می‌رود مقامات سیاسی در این نشست درباره انجام یک واکنش نظامی قابل‌توجه گفتگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69589" target="_blank">📅 20:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69588">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12fe6dbab2.mp4?token=ZAaeXpxz60vGRalSsCHIy0s-IOwhgcDnX-2PIBBDaIwSl8VgtQfIGYx64OATKB5_JDizJcoXhN2N02WFMa7Egi5Ah57wktDlkb3AIECHlvjXiFK-KyLJ1qZiDszFRkTpz9B3a8fQWJLa4g_q-11Q-6cR_n6_UBI1Ih7gs1SJIY9POC3UC_Ad54n-BgIuzMo1lrbQIVNUT1sFdG8D_B4i2G9qRZ-bmBYbK03fHJjgvf7pBvqM_wo8i_awAd6vqvEylsDMDj9fAd1O_rJlUCIQWNcmANt7xXGNoaEc8bOQgZOUYyKa15klI90erX9JDsrQQhoVzNpYZzDgTk_9oNtlTarrJRbJN6wckK6Rkfk0iK8pT-VU2PM3ri5FVOLkahQt4ZWRlNXa7_eNBeDfJRGncFT7U7X26kh6WHZSfaznAaKPsKferyX-gLT-rsf3XP4sYcpZ7Xyj6WpNvAlixepDX9cfc7xjQDFgcu5JemsQAItZ-D2eeDrdTlOY65LAGZIhZ5__08vBiXLonxu0T_aMeh2fPamNAexFtr4Tozo_wFbg-vDNbro-isi2Kwt7AXPtMKoZtUZHhEPreooHNkD4Fvxc5DfDW9PwiTLnzBYBxYwgP2OuNMmZAZHYtGL1-94Z7RHaMxBM1_A_CrWMKD_WK7D3vLQtT96tCeeHcWH8bPI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12fe6dbab2.mp4?token=ZAaeXpxz60vGRalSsCHIy0s-IOwhgcDnX-2PIBBDaIwSl8VgtQfIGYx64OATKB5_JDizJcoXhN2N02WFMa7Egi5Ah57wktDlkb3AIECHlvjXiFK-KyLJ1qZiDszFRkTpz9B3a8fQWJLa4g_q-11Q-6cR_n6_UBI1Ih7gs1SJIY9POC3UC_Ad54n-BgIuzMo1lrbQIVNUT1sFdG8D_B4i2G9qRZ-bmBYbK03fHJjgvf7pBvqM_wo8i_awAd6vqvEylsDMDj9fAd1O_rJlUCIQWNcmANt7xXGNoaEc8bOQgZOUYyKa15klI90erX9JDsrQQhoVzNpYZzDgTk_9oNtlTarrJRbJN6wckK6Rkfk0iK8pT-VU2PM3ri5FVOLkahQt4ZWRlNXa7_eNBeDfJRGncFT7U7X26kh6WHZSfaznAaKPsKferyX-gLT-rsf3XP4sYcpZ7Xyj6WpNvAlixepDX9cfc7xjQDFgcu5JemsQAItZ-D2eeDrdTlOY65LAGZIhZ5__08vBiXLonxu0T_aMeh2fPamNAexFtr4Tozo_wFbg-vDNbro-isi2Kwt7AXPtMKoZtUZHhEPreooHNkD4Fvxc5DfDW9PwiTLnzBYBxYwgP2OuNMmZAZHYtGL1-94Z7RHaMxBM1_A_CrWMKD_WK7D3vLQtT96tCeeHcWH8bPI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فاصله ایران تا آمریکا با موشک فقط چند دقیقه‌ست، اما پیاده باید نزدیک ۱۹٬۳۰۰ کیلومتر راه بری!
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69588" target="_blank">📅 20:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69587">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0660a7fbd.mp4?token=BKgwkZefWWmNU_pEUzwVR9uWLzELLsOTDfauAyCXg1mh6UlmoKugXza6OexcTq6B1oT_Z11V6QkerukZF_LSAHvkgOVjtOsTOzw2Zo79koYvNis64nbDzosLBr-rth2zlT-YQcb1wW9SJcZ1uQamm-CKoY-CtoHOftWLWpF4zCWZcwTUvBWRXuEYzwixaXOteo4I03LgWKwnm68nDLqUexkZQxp2VVNjaiqc-FJ5klbj2gcbnZojiDKVMdAvH8yrphM7DNU_E_ZWpErqEGhf3rZQSCg3FllmU0vv-Z93Yk3C4D6rAnqnWiOzywKm8e1YrBlsTtXKmr4Azjw1Cutn5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0660a7fbd.mp4?token=BKgwkZefWWmNU_pEUzwVR9uWLzELLsOTDfauAyCXg1mh6UlmoKugXza6OexcTq6B1oT_Z11V6QkerukZF_LSAHvkgOVjtOsTOzw2Zo79koYvNis64nbDzosLBr-rth2zlT-YQcb1wW9SJcZ1uQamm-CKoY-CtoHOftWLWpF4zCWZcwTUvBWRXuEYzwixaXOteo4I03LgWKwnm68nDLqUexkZQxp2VVNjaiqc-FJ5klbj2gcbnZojiDKVMdAvH8yrphM7DNU_E_ZWpErqEGhf3rZQSCg3FllmU0vv-Z93Yk3C4D6rAnqnWiOzywKm8e1YrBlsTtXKmr4Azjw1Cutn5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو:
ترامپ بزرگ ترین دوست ما هستش اما به صراحت میگم وجود اسرائیل قابل مذاکره نیست.
با توافق یا بی توافق هرکاری که برا آینده مون نیاز باشه رو انجام میدیم.
نیاز های الزامی سیاسی مجبورم میکنه این مراسم رو ترک بکنم.
در حال حاضر توی یه رویداد بسیار مهم نظامی سیاسی هستیم.
این جنگ موجودیتی هستش.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69587" target="_blank">📅 20:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69586">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">خفن ترین تیپستر های ایران با هم جمع شدن و TRUST BET رو تشکیل دادن
👍
هیچ سایت بتی دوست نداره شما این کانال رو پیدا کنین
رایگان بهترین شرط هارو براتون میذاره
حتی هزار تومن هم دریافت نمیکنه
سریع از این لینک جوین بدین کانالشون
👇
(این پست پاک میشه)
g14
https://t.me/+cBQ8n7zLQiUzN2U0
https://t.me/+cBQ8n7zLQiUzN2U0</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69586" target="_blank">📅 20:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69585">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/or_dxgK1JqGul4BBExqnNvUA7YFTRSfUzFcWJJGrhRueMnNVJnynpU9cilc7zKT9aFI69DwvLpcKW3FVkKlYfb5RVGJ81r0IMHOcaHUCfhpYvl_8Yl3-6rJl6C317GxY7EYWhLFg3wA4vB37LJNlTyfSus_1GqpLXaYUlzLL97ZvBR2NWVkaZGUUPJe5emB1FC0WLyWJalShMUSESCk-Px6PmKGBkZOmc2Dl4ft_KwPIv2_XJ3BSlxTIN6AoxLicNIdVLDpDMYpGBmqFgCInGvRtFmBp9D_gtrKt0j1AyGvJ2YBrRJ-_Qet1T72B96QSFdSpFiUCCGNIaVXvQrv-uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">40 میلیون تومن برداشت روزانه ی کانال تراست بت
🎁
پول دراوردن از بت تجربه و استراتژی میخواد نه ادعا
برایند ماه تیر توی کانال تراست بت: 78 درصد رشد سرمایه بود
✅
40 بازی اخیر 34 برد
📊
💠
https://t.me/+cBQ8n7zLQiUzN2U0
g14
💠
https://t.me/+cBQ8n7zLQiUzN2U0</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69585" target="_blank">📅 20:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69583">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19fc284b17.mp4?token=GgpTwNeM3J9akqUFNh-tqJc3SM1zGMrp627DForFApulrT8XpLskmUxoz2ErJUp0B92DdOXIQ7qIDxDcL_5bG_1Dz8T4QnNOwgY44-kGl5km6LUFUY1OlnaUFiTaCwZIPkUjbUDtQV5A2_SbpH61uYWu9rj-i_Z3ayLnc6G329_OiNtwtcU5UDaE9VT1DaEdsz7_2ZtjNXYrjnE163Fhay1pWfQ9DkwvOrgIS1ntlpEnMgditxSnV7XPHO-jYgfxJ32waS0HTYcKMuu87_FTR7jgntK_csbgFRmCcoyyhHGClWiCkNj6kmAoJN-DhPe7zUt2cVpjmVr7KGsqGEnGhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19fc284b17.mp4?token=GgpTwNeM3J9akqUFNh-tqJc3SM1zGMrp627DForFApulrT8XpLskmUxoz2ErJUp0B92DdOXIQ7qIDxDcL_5bG_1Dz8T4QnNOwgY44-kGl5km6LUFUY1OlnaUFiTaCwZIPkUjbUDtQV5A2_SbpH61uYWu9rj-i_Z3ayLnc6G329_OiNtwtcU5UDaE9VT1DaEdsz7_2ZtjNXYrjnE163Fhay1pWfQ9DkwvOrgIS1ntlpEnMgditxSnV7XPHO-jYgfxJ32waS0HTYcKMuu87_FTR7jgntK_csbgFRmCcoyyhHGClWiCkNj6kmAoJN-DhPe7zUt2cVpjmVr7KGsqGEnGhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
پلیسِ رشت یه ون آورده وسط خیابون و شروع کرده داره به دخترها اخطار میده؛
بعد واسه مشروعیت دادن، یه مصاحبه از این خانم رشتی رو منتشر کرده که‌ با میگه:
گشت ارشاد رو دیدم احساس امنیت کردم.
امیدوارم این کار ادامه‌دار باشه چون اصلا از وضعیت سطح شهر راضی نیستیم.
چهره شهر اصلا عوض و زشت شده.
الان همه فکر میکنن رشت این شکلیه ولی خوب‌هاش رو نمی‌بینن.
گشت‌ارشاد دغدغه اکثر مادرهاست نه فقط چادری‌ها!
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69583" target="_blank">📅 19:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69582">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
منابع عربی از حمله موشکی سپاه به بحرین خبر میدهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69582" target="_blank">📅 19:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69581">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d659457195.mp4?token=bXwbNcsEBbT2tLEetN9wFYGVnIklLWFvaoN-uhhErX4855G1hQ3mpliLbzI3gKczUw9p2xnqeiO7W9InOCqY-kUa5OOn01yCqHi5U_EWccNTFmhS8G-gtBnkR_AL7gI4veWaJRXI87YxuRmlBHf433nU0MmvQiwr5cbWnasHr69jySAEjaOW9qnfBMePcdxLhGNZkWPu3NM8NjKGBbpvoucL2U8D8mk9AQrggpyFih4Rfq9zYF4c6fobI2OGE4r1iZQ6r-eYXchB6wzjMFfooK83W7m5TuWAVWCDlg0SOU7NYz986RjnHQHlTdOyyvNuyi_SZKCblpCgUA3erlG7TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d659457195.mp4?token=bXwbNcsEBbT2tLEetN9wFYGVnIklLWFvaoN-uhhErX4855G1hQ3mpliLbzI3gKczUw9p2xnqeiO7W9InOCqY-kUa5OOn01yCqHi5U_EWccNTFmhS8G-gtBnkR_AL7gI4veWaJRXI87YxuRmlBHf433nU0MmvQiwr5cbWnasHr69jySAEjaOW9qnfBMePcdxLhGNZkWPu3NM8NjKGBbpvoucL2U8D8mk9AQrggpyFih4Rfq9zYF4c6fobI2OGE4r1iZQ6r-eYXchB6wzjMFfooK83W7m5TuWAVWCDlg0SOU7NYz986RjnHQHlTdOyyvNuyi_SZKCblpCgUA3erlG7TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مصاحبه تاریخی فیلدمارشال رضایی و خنده مجری:
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69581" target="_blank">📅 18:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69580">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4yj504r1nQJnMy0EIWUurHsH65x0WydSVFxgPd285WjOf1tPzmRo2oQ3kVjoMu2SI6dM1_2-H5femv_Mb4pQKQXw6IWodmxh3tkT0aGbgKBO3FaWni4NSDgg3hotJTLrq7LkhkaETuGYG_M99eefKZ86W4LIsjIEq9_2KrrimRceMAD2uJnu18ZbPgM0sLw46xTZBped8C6_VaSuvPm9pbsuUb8V6U4yb7ctoCyfHAplmOQEabJXWAHOvedDVIyeAo7SrkT5Lm6sl-35_e7KDuSDzf6hNTn42C-ZDkClFF3XuRWv1QtVeXlBqqZLHsuiQM6N2PxI1p7LKbYbevsCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پهپاد مافوق‌صوت Quarterhorse آمریکا به مرحله آزمایش نظامی نزدیک می‌شود
واحد نوآوری دفاعی آمریکا (DIU) برنامه توسعه پهپاد Quarterhorse شرکت Hermeus را برای ورود به کاربردهای نظامی دنبال می‌کند. این هواگرد بدون سرنشین با هدف آزمایش فناوری‌های پرواز مافوق‌صوت، سرعت بالا و قابلیت استفاده مجدد طراحی شده است.
مشخصات اولیه Quarterhorse:
⬇️
نوع: پهپاد آزمایشی مافوق‌صوت
⬇️
سازنده: Hermeus
⬇️
طول: حدود ۱۲ متر
⬇️
پیشرانه: موتور جت توربینی با فناوری توسعه‌یافته برای سرعت‌های بالا
⬇️
سرعت نهایی Quarterhorse: تا محدوده مافوق‌صوت بالا (هدف نهایی برنامه Hermeus رسیدن به سرعت‌های نزدیک ۵ماخ است)
⬇️
قابلیت‌ها: پرواز خودکار، استفاده مجدد، آزمایش فناوری‌های پرسرعت
⬇️
کاربردهای احتمالی: شناسایی دوربرد، آزمایش سامانه‌های آینده و مأموریت‌های نفوذ در محیط‌های دارای پدافند پیشرفته
پهپاد Quarterhorse هنوز یک پهپاد رزمی عملیاتی نیست، اما آمریکا آن را به‌عنوان یک سکوی آزمایشی برای توسعه نسل آینده هواگردهای بدون سرنشین سریع و کم‌هزینه دنبال می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69580" target="_blank">📅 18:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69579">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3689824738.mp4?token=kZIsSFGHXZvdma-WwqHpOW45i6Ah6zDY1bzvzYVVYzdaXnEaM7COdtrkw48SdSIU6zamcB_dMwpYlNVK4uAkSd2RAqivhppMvsjLpXqIxv9Hzm43dJ1awHFUksn5Jzybo-jLeSMwpyLenZ2UrGI8TRDGn9eYgzqeKbaHYv_0WW7HJkhpGY_4-YxljaWJ2mi5u89rbJMmfyiXWwB3iMx2Jl0LD5nVdNHYGJfXzq6bGO_XsPlh9BksqGUHwujkt_qtA5K-cltwnalXZ5mSThnQSeDKLcAJvn2h5utG0E12aqVGywBqhebfGfMNyJeJooaiG8D4bsk4zG-JcJGW8eQdig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3689824738.mp4?token=kZIsSFGHXZvdma-WwqHpOW45i6Ah6zDY1bzvzYVVYzdaXnEaM7COdtrkw48SdSIU6zamcB_dMwpYlNVK4uAkSd2RAqivhppMvsjLpXqIxv9Hzm43dJ1awHFUksn5Jzybo-jLeSMwpyLenZ2UrGI8TRDGn9eYgzqeKbaHYv_0WW7HJkhpGY_4-YxljaWJ2mi5u89rbJMmfyiXWwB3iMx2Jl0LD5nVdNHYGJfXzq6bGO_XsPlh9BksqGUHwujkt_qtA5K-cltwnalXZ5mSThnQSeDKLcAJvn2h5utG0E12aqVGywBqhebfGfMNyJeJooaiG8D4bsk4zG-JcJGW8eQdig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
یه سرباز روسی توی دونتسک اوکراین لخت خوابیده بود و داشت افتاب میگرفت که يهو…
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69579" target="_blank">📅 17:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69578">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5fdacb808d.mp4?token=rKGRO6fSDcT6uWLDhwOTIKf8MP4HhDsuj_sCj-2b2j00z7_yuYVygnveoix21qoZOZe411ZRmBGLWBi4R3gEld9Tzci-a-mZTKQdMmwQAcj3d0bNMnHSPM2N8-U6us0UxmYNP6xlCWoycLSzOAFj51JmIOU_cXWuqK1tvUp5mmZk3Q-xKQvGlHYTYN5E_AjTabLNJgMgCcmLY9qRasnp3oR9cvDHL7EyppsnTxRocmS1Knmgkx4lsdEt-agLZ6ErPEujs3fdZi4XfTrVkVio5fXUHkNRLQ1parIKsAxmFdFR2k0IzHdeYJEYxZeW3tlix-ciICSF1PGrqlnTO5F0kw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5fdacb808d.mp4?token=rKGRO6fSDcT6uWLDhwOTIKf8MP4HhDsuj_sCj-2b2j00z7_yuYVygnveoix21qoZOZe411ZRmBGLWBi4R3gEld9Tzci-a-mZTKQdMmwQAcj3d0bNMnHSPM2N8-U6us0UxmYNP6xlCWoycLSzOAFj51JmIOU_cXWuqK1tvUp5mmZk3Q-xKQvGlHYTYN5E_AjTabLNJgMgCcmLY9qRasnp3oR9cvDHL7EyppsnTxRocmS1Knmgkx4lsdEt-agLZ6ErPEujs3fdZi4XfTrVkVio5fXUHkNRLQ1parIKsAxmFdFR2k0IzHdeYJEYxZeW3tlix-ciICSF1PGrqlnTO5F0kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
توی مراسمات اربعین امسال آهوی ایرانی کباب کردن و به زائرین دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69578" target="_blank">📅 16:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69577">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rz6cwyDOAT67aZDauQW7F_timmBDF5vr2hboHNxx2RC-CJ3YnJAiDm_1tV0IthZVI1L_VCNQs_q7bZCHIHbLvX8fPbV27Z_HdYx5EXREBfNFKjL_5rA7EFo--ghmwF2z7ngjvqJY10WZsPaDsObGsbpDxTZLlzuZZnbxGdBFF-Ky5Zii9n9Pzlyakqhv9ZF8bjhNzIWyU7-yXgKsRU9ATUgdX9UwSHQ5SWyf9lznF7J-_pHAyW90ApWPoYOvXNbnKrI3vAXIDQW6N-EORSTx_yrcvk669zNhWC6YTrgxIMQJi9GYD5CtDPwBFcgG4fAHL3W53GYiedcF2YOu-skFOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
#فوری
؛ ارتش اسرائیل برای شهرک المنصوری در جنوب لبنان هشدار تخلیه صادر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69577" target="_blank">📅 16:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69576">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66218d020e.mp4?token=C1v8jFhUbq2xc6GPPzb_JehKefO3prUBlVxFSoTB7JkY_m8tLj35TWhA9DO4Vge7jmZftOE1CWKm4Irrtm3teTgkO75uU836m9h72V29OurhvBREPHp_lXpNfMc4RkdmaIlLynBYH-yLXl7vU1Ro5evJyQQauOredLDqOZa8RkaaczuTQkX6RbbVlOTRQW1ItGxXtpk9zIOratJXc0i4PIUIbTEf_TU-lcPbZv0AoE4qlYU-jKiklcZQGm2RDOqBYVtdmr1oI91vUhSGSeHLwnZoAAg88aCrVcrTKncrfaUKNxE8pV_jqllwQlUuhcb9gyUWpHKIWTmiecVGGNF7Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66218d020e.mp4?token=C1v8jFhUbq2xc6GPPzb_JehKefO3prUBlVxFSoTB7JkY_m8tLj35TWhA9DO4Vge7jmZftOE1CWKm4Irrtm3teTgkO75uU836m9h72V29OurhvBREPHp_lXpNfMc4RkdmaIlLynBYH-yLXl7vU1Ro5evJyQQauOredLDqOZa8RkaaczuTQkX6RbbVlOTRQW1ItGxXtpk9zIOratJXc0i4PIUIbTEf_TU-lcPbZv0AoE4qlYU-jKiklcZQGm2RDOqBYVtdmr1oI91vUhSGSeHLwnZoAAg88aCrVcrTKncrfaUKNxE8pV_jqllwQlUuhcb9gyUWpHKIWTmiecVGGNF7Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
وزارت دفاع روسیه تصاویری از حملات پهپادهای جت‌سوار گران-۴ به سه کشتی باربری در دریای سیاه غربی منتشر کرد.
وزارت دفاع روسیه ادعا می‌کند که این کشتی‌ها تجهیزات مقصد ارتش اوکراین را حمل می‌کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69576" target="_blank">📅 16:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69575">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/474cba356d.mp4?token=HakvLClBiPF4UMwsIGhE2K4tCyKjCOv8QOmeMQjTvA5Kl0kFXBkuM4KrNDvUU0lXcYKKp5KltBSiP26b0hjTlzFYypuQRqN9T8ywo39glv10bH34jww0plhvbVdPQCm_3k1Z2Zli1Gq6xtvKECBxQ0SqcD_q7BL9efSSqhIfWCcqeyudD7SUgxlagE36DI-GwW2wfISN5Tx5ZiWxJ_7IkWQuQjArv-8WNhaR5QAPPgGEPYaj6ulRJAx19nZHeYRhESfWTBUWC4B2SmZ89bRSmJGakfyOHFagxoRWMsokqO1Atc76pcfszDEC2PH7kWKqXKDglK3fBZlcoWMKtr66Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/474cba356d.mp4?token=HakvLClBiPF4UMwsIGhE2K4tCyKjCOv8QOmeMQjTvA5Kl0kFXBkuM4KrNDvUU0lXcYKKp5KltBSiP26b0hjTlzFYypuQRqN9T8ywo39glv10bH34jww0plhvbVdPQCm_3k1Z2Zli1Gq6xtvKECBxQ0SqcD_q7BL9efSSqhIfWCcqeyudD7SUgxlagE36DI-GwW2wfISN5Tx5ZiWxJ_7IkWQuQjArv-8WNhaR5QAPPgGEPYaj6ulRJAx19nZHeYRhESfWTBUWC4B2SmZ89bRSmJGakfyOHFagxoRWMsokqO1Atc76pcfszDEC2PH7kWKqXKDglK3fBZlcoWMKtr66Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی صداوسیما خبر کشته شدن ترامپ رو تمرین کردن
😔
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69575" target="_blank">📅 16:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69574">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNjWoXlj792yiY_FN7rJp7uncrCGQSZuVFFjJ2PE3oGCX23LwT4XibuhG-wZ5nT_AsTBsNP0XA1syhdNv5IkRmEEogvGIX8qkEvCxRTVUMEcqQwqPjNFfX9aclZmFtAUNr_h_6BIA3wJxAx_SVGEGnNStboZOCaBTRYGiQZ5tJqF1abqUYo7INl9xPVStCi80fB3mqPsJabwpWIx9llI_1jgp-gC3-r0VVA74nR0oYOHuq2KXuoCiuFjLcXwcfoBqBVcLJ1fvHWZYVAjVbpBJARHr7LYdw-PJid5ZZvTTbZJwHhYFC3CdInMHn0hJJTFTVrXNFNSfWw5wKILikweog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💢
📉
قیمت نفت با کاهش های پی در پی به ۷۶ دلار رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69574" target="_blank">📅 15:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69571">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fg9ObyU5a_RlbZCHIJzPOGWmrIi7SHHBt5xXvjqSJVQESaBfU4xUMHf0ZlOLiFwgwyju-1bmSCzz6oHrDt2XSOds-eIQBpc6M9gzH1G5cC-sXSFFHq-POXb6QTIkmhEEDb1h7QPdX3MI-BEn0t0l-ARrphwP4WdR-QoCXUMd2TN5KA11DLUUIKjg9WWr-ynibensouySCTiSmrZ5M1ydGcH1uGsFhR9PFm60N6-D8dCHh_qRAAFWC_YoySkn8M9a6T91cpzzGnw8HUYhUc10tfBSD2VVax-ROd35dDqeB6OzSD7gG_EpgieNNGXpa1PTLc1fwRs8zCrqlbLBGRVtog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nQLTqC-ZTXv15hOAmSRZicGy6yK4Kz6JYWGh9StPogdMJ3-4ctlP2h2-GWE-MSt4wH51x0qcHXNznMkg46kf9rEw6u3S-1Ucx-_eU5s4jurh8vJ2DHOXGL8eUWjbDFxfN_gs3pWfMWvpAKiAjfx7XeRkOdCbBMHFRyR2MIXWRvLmBwzcu4rTniKIuEu6onfe_PyuJh3m9Ft6cZW1pfIv2RMwf9gRsNX7dXmHdD48sMJfOLQhRIT01wbGgqDyICYiQkgl8W94IzW-VL0ckeUfdFqL1e6xntV5bSWPoUxZKaCAWGrpLZ5kCy_cfEJ3tv4xlYb0CgoFMUpWokqIIAbYAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bW7OrLk0a0J5xrHx3WyofARaMuDkBEBsRMeLTIuPqvaFLIII-I6Ca5RyebYgcJIJnYg9axdyeWUE8Dd2Te1yiP6mg6DndnP4xURiuK4D15JxSFchBKCmvPR5l3YdbyxEKA7NCaTDnl0fk9c11G9RKEqIaddpT3mCl35HGNTb8ru-13ZnC5ulE8udKFQ0heGHVQAsVf8KDV1vKWDMJrPHuTk6UlSbtwWkMUAKnsh2QTPkivmo-8picx8MIyakjVPhb1cVp_XB-5g9hyxlTYJHNnpBWidl2QUO_xlfaFwT8f7aCaLccoBxg-jDBRMvzA6BzVEkPPjU3nQFtS-PEW69DA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
پست جدید و لاتی کریس رونالدو؛
"
اسباب بازی‌هام
"
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69571" target="_blank">📅 14:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69570">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8tUwdFU4fX51PQLn9Sj8wNiYSjIE_VhUKBeP8lN_loinqMUBm1xoZBH3kau6E6r7FTFZZp3m_yTE9gzP9zkkg1PiqGC4QY1w1LHc07owf2DjomMCizOKM0M_3D1n_hwZ7TIvpbxORlHXy-KhJC4CA5mco-Odpbtvv4H68itoG1DqtJwsgl3ha59uLjAPYDJEeCWJhw9hjOZc6UbcJpirsezZrceefgopWpj0iIaHHtk6p9boi5h58UHoWNl3q4IXuPsRP_7XrickNQ5EDwPsQYGjbMZnIQ5SkELzbr8lvG79Vu4lAmhbqC2lWwe85Cst1AA3-U6yupz9d5FDv69pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
دسته‌ جدیدی از سوخت رسان ها برای مذاکره وارد اسرائیل شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69570" target="_blank">📅 14:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69569">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlJ1W5bbOEvBnRhsI9OqoifEqfkSeQJnVEbEaWiFw0yQZ5DnCxABL2QJCYe-2Nmll_mIuUDsiKjQTrZYFgkbh6XTAKO3YgKjn507Vvjbkyc-fD9tCbSyh-l6WCIJvhyxOeGw2_xltzB0nv4KJ7N6FTSL4EvQJM0JJ8-JxrWt06tB_ATvhpYcJx1WuWhYvChj7XvPSpywdGvGofYu7JEbf-sNuTfhTuO_UJNXDpG5dagrEmR8h39Dd9JIDCiBx0sgHcJD3Fi22dPkTxwXtTpmn0Y0Fc-2Ws2fYi1pK0sh6dLSwunMBed02WFS4-C1qvtoMFHdt_BABmHJrFhdd1px7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
❌
حمله هوایی ارتش اسرائیل به شهر المنصوری در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69569" target="_blank">📅 13:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69568">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f4b05f8c.mp4?token=rkrZ7RcS87Vgocfe1v7C_GwgvMXEjrx2EUsi28FdA3WgvMpRlJ1pqgubv1KXhnu4AI0ut-ec-OH3PusR2upvb2xBbc3yfXVoldq1q1gbC24HHHo9fPIeFioR7vpQ5mD4H5qpEtXDjH8v7SnhBhHkp01Kc1-JSDiKlRqA3KztU02Put1kQ78F4xVYMGVLwdZfo97cQDqwLGAha6lYREvVME5tCAYYqWc3yB6yyXFBu4UGrVJ-f20qU6rRAR_zED0xG4frtOmZSXsASfPYtM4ubbr1TDl1lXwD2HyOzVihbNiBL28tBtYyKxarhKlTFNtsXtg8t7ClVL1jq-sR_JgtdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f4b05f8c.mp4?token=rkrZ7RcS87Vgocfe1v7C_GwgvMXEjrx2EUsi28FdA3WgvMpRlJ1pqgubv1KXhnu4AI0ut-ec-OH3PusR2upvb2xBbc3yfXVoldq1q1gbC24HHHo9fPIeFioR7vpQ5mD4H5qpEtXDjH8v7SnhBhHkp01Kc1-JSDiKlRqA3KztU02Put1kQ78F4xVYMGVLwdZfo97cQDqwLGAha6lYREvVME5tCAYYqWc3yB6yyXFBu4UGrVJ-f20qU6rRAR_zED0xG4frtOmZSXsASfPYtM4ubbr1TDl1lXwD2HyOzVihbNiBL28tBtYyKxarhKlTFNtsXtg8t7ClVL1jq-sR_JgtdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇷🇺
دیروز طی یه مراسم تو روسیه، یه چترباز از هواپیما پرید پایین ولی چترش باز نشد و سقوط کرد و درجا مُرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69568" target="_blank">📅 13:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69567">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7CK_bVnYAE4KUc3dUvSc96k80gYp0uUiQd-Ti8GzMSjwc5q-gq465OFgoEqaQkQVncR07MLOqrr66GU3rgrbnhNkI_WB_8GLCP--zaggQ8k-G2mGLiW7FMgkSInuF_LmJ4a_9X6PdZhAhkqR4kqQN43YLp6DvsAIkmK3RBuvWEPz0Kj5_C_Hl_ekTTydjQJsBuu54iD3Xz73GKr9o-rH4_SKLmpRr14u62bn5u3BF0oBc_Sgt_waLU5kTXspYh7Xk7-XP_z5M8COr-FnX6zu42hCkEXZfAzCY3vrA6NpM44DAekVTKq-Vl1V2bHn4biy3g6SFZzv9mhnC5AmYn8yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
دونالد ترامپ تصویری با هوش مصنوعی از خود منتشر کرد که در آن با لباس نظامی در کنار ژنرال پتن و ژنرال مک‌آرتور دیده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69567" target="_blank">📅 13:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69566">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cc20a5985.mp4?token=Y5wQLAQ4xfrqgnP1zkhVyqP4bJLFzBcwqF7_I84p8jd2LXcW91dyktUzFtZDoQNEYBcNqHX38gFihN0SOdLxOQKilgvSISxZKU_YCV8YiOWIDDtN6maSqiUNEbj5NQl26ZMkStFHTMbReA8x4Do9NLQ99ZNNTJvgoLHfmDiWpyJxgerRSTalJ7pOGQ17Qom8X6oltsCEpMHZASVjAyxcXr8-S2Ps-vK_ClzoEQxtxuKGRL-FkpcMpPfwJ0X4npe7bvI41wr8J8MERqwNv6uzddKB5RHRtkN7XAJTNqRRWPZER0kScvhN2k46dQTYzLq15JQ6A6KFFUYzqPOYOX5Y9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cc20a5985.mp4?token=Y5wQLAQ4xfrqgnP1zkhVyqP4bJLFzBcwqF7_I84p8jd2LXcW91dyktUzFtZDoQNEYBcNqHX38gFihN0SOdLxOQKilgvSISxZKU_YCV8YiOWIDDtN6maSqiUNEbj5NQl26ZMkStFHTMbReA8x4Do9NLQ99ZNNTJvgoLHfmDiWpyJxgerRSTalJ7pOGQ17Qom8X6oltsCEpMHZASVjAyxcXr8-S2Ps-vK_ClzoEQxtxuKGRL-FkpcMpPfwJ0X4npe7bvI41wr8J8MERqwNv6uzddKB5RHRtkN7XAJTNqRRWPZER0kScvhN2k46dQTYzLq15JQ6A6KFFUYzqPOYOX5Y9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درباره ایران:
خب، اگر دوباره پا پس بکشند، ضربه بسیار سختی خواهند خورد. آن‌ها این را می‌دانند؛ آن‌ها این موضوع را درک می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69566" target="_blank">📅 12:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69565">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336dcdad36.mp4?token=cb3LoDHP3aXbpKnzIL23BIoLE5Vd7j4lZgcHFCAiVjvDhfGdxj7YKBPP8Az0FGpnBig6vYMge3qHRdoONg9ebtP9g7Yc3iWlwuCS_GLjWKmjL7DFRxnJdqHQ3Uo3bP0R8pRz-kV-QxDByAXWIiz-EJDzZjr4JZYqP2NfnfytgxKOcOp0qnBBFWT7Ic7hItryx0mDtojq-u35owxvtX9uU30Wf0E4QTtzV6CyXqWU2up4Eh8R1elW5qfjKHly4smHpvfRoXpcrvEDZPuFIgUEBjlVc4ifHBzDr4bkWgDXY8EIqDSydpgO7AnipUCXGiQAxKcPdvMnPzkHLy2xT0zk6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336dcdad36.mp4?token=cb3LoDHP3aXbpKnzIL23BIoLE5Vd7j4lZgcHFCAiVjvDhfGdxj7YKBPP8Az0FGpnBig6vYMge3qHRdoONg9ebtP9g7Yc3iWlwuCS_GLjWKmjL7DFRxnJdqHQ3Uo3bP0R8pRz-kV-QxDByAXWIiz-EJDzZjr4JZYqP2NfnfytgxKOcOp0qnBBFWT7Ic7hItryx0mDtojq-u35owxvtX9uU30Wf0E4QTtzV6CyXqWU2up4Eh8R1elW5qfjKHly4smHpvfRoXpcrvEDZPuFIgUEBjlVc4ifHBzDr4bkWgDXY8EIqDSydpgO7AnipUCXGiQAxKcPdvMnPzkHLy2xT0zk6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فریادهای مجری کشمیری(هند)صداوسیما درباره تنگه هرمز:
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69565" target="_blank">📅 12:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69564">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/69564" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
R14
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69564" target="_blank">📅 12:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69563">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/loa3S-ALQsHtRl87ubvJ34--P_v6yAu2OKHb4i3fofpuCtEIn1jkYwEsYnvvr4kiSyDWVZtGbF96uq6QxsC0FUTt5-UwCIsc2Lm5kqHrE_n36EETbsQ7jQOEaGNvIZArCSCXH96OnhC7ezYMy-7bXcAlyxusnib-2fRKn7PBfE03JthtUJIz9z5Qm2zWHqPaP_daRie43r678kzlJr4HvQRsC5-tOS1z-H0GQmrSMKR1SyQ8Umk90WTsTfuWdXLOJefXFxWkh848K6LHCcfJ6nV2Td88dcIgpp607MPrusz40C6F-2bZ2ktapfuFIU5foDCKX5FyWKjKrXig8z0buA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r14
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69563" target="_blank">📅 12:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69562">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aba5ea669d.mp4?token=iSoqNWiJXV4gQDwffb_69Up5yzLeswNDDf7H_XGkhGytu_s78j0lK60ZUUrO2_I8RTlP34aHjYaTWfHQjVrRMTPJmV6I9cRKs87mRJJlk5DF6CYjQZhWNwuQMdaaRGQobtYLq3tBAHujwdzmLF9BvbmKflneakYhSIy7PmviHxThHFaZdZhWQqj54wblEjbHz1oiBn2t4sibM8ohef4-zzpBbJSGeoXLITSP9C8NWS_lKeZtaAVlxXlPchT3yo3js60694dcm1HsT2Kt2rIE9zsTfpqSE8NwxQhAVHK0qHXnscfIRHPsFVYojPrQrTyHwPx4-1XOEWDG9Bsl1AFngw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aba5ea669d.mp4?token=iSoqNWiJXV4gQDwffb_69Up5yzLeswNDDf7H_XGkhGytu_s78j0lK60ZUUrO2_I8RTlP34aHjYaTWfHQjVrRMTPJmV6I9cRKs87mRJJlk5DF6CYjQZhWNwuQMdaaRGQobtYLq3tBAHujwdzmLF9BvbmKflneakYhSIy7PmviHxThHFaZdZhWQqj54wblEjbHz1oiBn2t4sibM8ohef4-zzpBbJSGeoXLITSP9C8NWS_lKeZtaAVlxXlPchT3yo3js60694dcm1HsT2Kt2rIE9zsTfpqSE8NwxQhAVHK0qHXnscfIRHPsFVYojPrQrTyHwPx4-1XOEWDG9Bsl1AFngw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محسن رضایی :
به عنوان یک سرباز از‌ همه ایرانیا تقاضا میکنم یکمی دیگه این شرایط رو تحمل کنن. چون ما داریم در کنار آمریکا؛ چین و روسیه به قدرت چهارم جهان تبدیل میشیم. این شرایط گذراست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69562" target="_blank">📅 11:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69561">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1729d69d0e.mp4?token=QsmRtkMApRfSwUg78uAEnQQjKUa_mZf_Y224psIvkilvP0RDPoWtY2OQLVIm_vTf_MO1yw3vVMfYWVX8ypPTXpddRJyF__EVyXBvV2ozgAXjCR5MuY9UG1sqfttkD-1TJrMjXM9a4ab7OOm5tRWIrXarYeau_n0b2uDkLAljPRC_4crUKn9pQ6q0oxBOWSbGC_dKPhihJQSWST0hkpeoNDNB5Cjkyc1tsgMtyb04CdApBXbt0pA1tbB-4eF2cXKD1_UVpTbfZ7oxOrSL1vd27-ZZfZd4NeCU7pfGOqJjz99oOOmnCiKpNB26eWVoZqJBiIRIfeQjNgsMVKJe-gMOKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1729d69d0e.mp4?token=QsmRtkMApRfSwUg78uAEnQQjKUa_mZf_Y224psIvkilvP0RDPoWtY2OQLVIm_vTf_MO1yw3vVMfYWVX8ypPTXpddRJyF__EVyXBvV2ozgAXjCR5MuY9UG1sqfttkD-1TJrMjXM9a4ab7OOm5tRWIrXarYeau_n0b2uDkLAljPRC_4crUKn9pQ6q0oxBOWSbGC_dKPhihJQSWST0hkpeoNDNB5Cjkyc1tsgMtyb04CdApBXbt0pA1tbB-4eF2cXKD1_UVpTbfZ7oxOrSL1vd27-ZZfZd4NeCU7pfGOqJjz99oOOmnCiKpNB26eWVoZqJBiIRIfeQjNgsMVKJe-gMOKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
املاکیه دلقک:
تا ۴۸ ساعت آینده خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69561" target="_blank">📅 11:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69559">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sVcx3dM7cMO-CqtuuFcaZk5ujRXlUKvBNB0cD8Hnvsu7KCqrMk65aDzCOV0kuxny3ZO1mONgyUgyDdVYMhQ0IZns9KEAcDquaZVTToY_HdtFpWpd8cZV2Z67lyOnGyMHP62C6Z0XuIMQVmSV1YFauKDZCwvaRaIo-BT6pe49E3WDh_7xlUPDDmk3iMAsfDGRxHn3i0t_SapU8piRu-cjb7-oL-DIF0JJb6oP5_alDOJNYGd4zgacBoQ24qpibHB5_JVAXmOI1DfNfqSi-PINBOuIYpCOSHGgcL3KhInqK9I4hHLtTuaM3tjDOh22H6Z5FNfub-rxqkpUwoMs_BJUpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e2fe475d0b.mp4?token=X0oANciPcqUaIcOMHNxJNvyRDBLcNUieP_3x5GsYjjuBFV5ONl_oltrYYyn6MEiljYsza-LDX7SBBiYWRBiPlsUPvTUhVR4zWcogJXRwStNh8tMWbbz1LG-IOq-bDMBjsq9N6qgcQoHdcSGMYBNTV6EJHhwcwgYBSZpHx3f5hzZ1XbFW9wcE_c3Ga_452U0dCiVAzWL_NGVmZ4evtiHX3d6hQkABlvwa3_wb-ZdCjEJ1AkHDsSi6Mabzz3Bl_eKnbSk-IXLXk74wK5K_9IxHvMud4YX0qMGHGtuVc83hlsE6e3RLBThxyBr5wG07dYjgwQxB-GwqGvFO-66aWARocg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e2fe475d0b.mp4?token=X0oANciPcqUaIcOMHNxJNvyRDBLcNUieP_3x5GsYjjuBFV5ONl_oltrYYyn6MEiljYsza-LDX7SBBiYWRBiPlsUPvTUhVR4zWcogJXRwStNh8tMWbbz1LG-IOq-bDMBjsq9N6qgcQoHdcSGMYBNTV6EJHhwcwgYBSZpHx3f5hzZ1XbFW9wcE_c3Ga_452U0dCiVAzWL_NGVmZ4evtiHX3d6hQkABlvwa3_wb-ZdCjEJ1AkHDsSi6Mabzz3Bl_eKnbSk-IXLXk74wK5K_9IxHvMud4YX0qMGHGtuVc83hlsE6e3RLBThxyBr5wG07dYjgwQxB-GwqGvFO-66aWARocg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی:
🇮🇷
جمهوری اسلامی دریای خزر رو فروخت رفت!
در تازه‌ترین قرارداد، جمهوری اسلامی دریای خزر رو تقدیم روسیه کرده و یواشکی دارن میبرن مجلس و تصویبش کنن.
سهم ایران فقط به ۱۱ درصد رسیده! شما ایران رو فروختین و شرمتون میاد بیاین به مردم بگین.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69559" target="_blank">📅 10:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69558">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6f67c295.mp4?token=At5m3n3ja0aeIYl-uZ5rXmuTRpHdRzX1uYVEX1ACW_vFay2W7lBYrGy7JTewpQG4kz5CsOm6ZSQFE7P3lnre9jbWPrlgy3RUG2zwnxHCSN7GErm87QVs5x9Z-BM1KYVhdMDNyow-yJ-yWYCZSsbjY7CMmUwCuv_Fd2-EPW7gw5-jGqFJgn_eIod3e4ggP2kCcn5ClH1f0OgUVIa-EgzvZo0u6ZM4kpB8x5bg-5qgqLjDbAOB7ujiRRRvMMrLtBRlibFKol9UWv5rGSZqULD-M_o5h6DHRoh56Q9_Y9uFpD4n_MttFuIRwkkZ7LhNNFyx9p4uKNfTipbCUz6TUh5a_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6f67c295.mp4?token=At5m3n3ja0aeIYl-uZ5rXmuTRpHdRzX1uYVEX1ACW_vFay2W7lBYrGy7JTewpQG4kz5CsOm6ZSQFE7P3lnre9jbWPrlgy3RUG2zwnxHCSN7GErm87QVs5x9Z-BM1KYVhdMDNyow-yJ-yWYCZSsbjY7CMmUwCuv_Fd2-EPW7gw5-jGqFJgn_eIod3e4ggP2kCcn5ClH1f0OgUVIa-EgzvZo0u6ZM4kpB8x5bg-5qgqLjDbAOB7ujiRRRvMMrLtBRlibFKol9UWv5rGSZqULD-M_o5h6DHRoh56Q9_Y9uFpD4n_MttFuIRwkkZ7LhNNFyx9p4uKNfTipbCUz6TUh5a_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
پرزیدنت سابق، جورج بوشِ پسر:
مذاکره با قاتلان، گزینه نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69558" target="_blank">📅 10:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69557">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmFgfZmwe-4skWuc3Ka0FDkL961L_HwgyVCf2RoXza9gnSEVQXfc40oCG-13ailCiJgCw17QxmQtJShKigenthtUWltQSVLbydIn-VwFPifnjdAwYDVv87AZjH8F6ks4PwPXAns_gjZxfP4Bb69scM6E43UiMLPq_ud53-SqqCOhc7BNG5faPnCJuZuwd3BmPCErQATA2DEs37eeINkjOy5QhjBY5yEYiEMRDMqqwUTy9ICowYr6l8s0MsLMWWnMwJ1kkeeiTim_vNXip6gJvSGhA3iXdQNXF38U9e6e_M0Z6yMtHBNq8M-tSZWzxlLosH2SUtQH6ei4tzQqFZ7G7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇴🇲
🔝
بر اساس گزارش آکسیوس، آمریکا، ایران و عمان به توافقی موقت ۶۰ روزه برای بازگشایی تنگه هرمز نزدیک شده‌اند و احتمال دارد این توافق روز چهارشنبه از سوی آمریکا اعلام شود.
🔴
مفاد اصلی توافق:
- کشتی‌های ورودی از مسیر شمالی در آب‌های ایران تردد می‌کنند.
- کشتی‌های خروجی از مسیر جنوبی در آب‌های عمان و با هماهنگی ایران عبور خواهند کرد.
- برای عبور کشتی‌ها هیچ عوارض یا هزینه‌ای دریافت نخواهد شد.
- مین‌های دریایی در مسیر مرکزی ظرف ۳۰ روز پاکسازی می‌شوند و سپس این مسیر برای تردد دوطرفه باز خواهد شد.
- پس از این دوره، عمان و ایران درباره یک توافق دائمی مذاکره خواهند کرد.
همچنین قطر، پاکستان و عربستان سعودی در میانجی‌گری نقش داشته‌اند و کاخ سفید نیز مستقیماً در مذاکرات مشارکت کرده است.
طبق این گزارش، عباس عراقچی با این توافق به‌صورت اصولی موافقت کرده بود، اما تأیید نهایی باید از سوی رهبری جمهوری اسلامی و شورای عالی امنیت ملی انجام می‌شد. یک مقام آمریکایی و یک منبع منطقه‌ای نیز مدعی شده‌اند که این تأیید روز سه‌شنبه نهایی شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69557" target="_blank">📅 09:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69556">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5c55d9f368.mp4?token=J6EJGpXiaiS1Put3zbsiILRdkt7Uz1_M9EavW5ELJ8YMPXeNeRj05tItvTiK1icevCKr7h3TjwA8rg-1AKE-tE4B3j4SNa7UAOfD_CugRet_BacKkF34_OWdqSjZzqWcqXPPXiqsuDxsfXYCMqPkr5xluDg409SmTr5Ju7W1NYmryBHbCi6Yxc_gK0Q1MQiNMochJhwMFiCyv07S2m8wN2Rgg8rje5UrKsRj3bd_LfY-afT3o9OAl39Y4iLeguO12RtuyJHCNVAqN0lecF9ugCY9KgDTCbkqw4I06U8wBqQStLxHNQPt9EX4Ua--LA7uPMZ9qXtG7FVZc9EGdSkc6mfhSlNCi2dLk6pnZChJee0jUMYm11fh4zLYTLA0vjWGwC2iEBmg8p1ox3sGb_9Kw2ELK1aHr6wtBuX4HCmkJDRHoj8UfaymjKpOSJzBeJLf-IXw2Yu_TKoONVszo4usNPnaBLcXTWwtJSPupQGFSxNCGfQscWKo6Vhcd_5qXWtWIYUdvm8AiYyBsNbFT44ay5DezfwSHMOt3hUyvdNZqvUfEkStxyilH3rvxHbjqrHHUoI2ILeoskYdlFapH6ElFy2O-LebW43G3F1hDFA4120hC4H3adp5DmiG1_xaZxAZcXj6Tt4kkO4A3NwPjoKuVLhQj0-uII5aYeOAhi0YhHo" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5c55d9f368.mp4?token=J6EJGpXiaiS1Put3zbsiILRdkt7Uz1_M9EavW5ELJ8YMPXeNeRj05tItvTiK1icevCKr7h3TjwA8rg-1AKE-tE4B3j4SNa7UAOfD_CugRet_BacKkF34_OWdqSjZzqWcqXPPXiqsuDxsfXYCMqPkr5xluDg409SmTr5Ju7W1NYmryBHbCi6Yxc_gK0Q1MQiNMochJhwMFiCyv07S2m8wN2Rgg8rje5UrKsRj3bd_LfY-afT3o9OAl39Y4iLeguO12RtuyJHCNVAqN0lecF9ugCY9KgDTCbkqw4I06U8wBqQStLxHNQPt9EX4Ua--LA7uPMZ9qXtG7FVZc9EGdSkc6mfhSlNCi2dLk6pnZChJee0jUMYm11fh4zLYTLA0vjWGwC2iEBmg8p1ox3sGb_9Kw2ELK1aHr6wtBuX4HCmkJDRHoj8UfaymjKpOSJzBeJLf-IXw2Yu_TKoONVszo4usNPnaBLcXTWwtJSPupQGFSxNCGfQscWKo6Vhcd_5qXWtWIYUdvm8AiYyBsNbFT44ay5DezfwSHMOt3hUyvdNZqvUfEkStxyilH3rvxHbjqrHHUoI2ILeoskYdlFapH6ElFy2O-LebW43G3F1hDFA4120hC4H3adp5DmiG1_xaZxAZcXj6Tt4kkO4A3NwPjoKuVLhQj0-uII5aYeOAhi0YhHo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
تنگه به زودی باز میشه یا ضربه شدیدی بهشون وارد میشه ک باز کنن
اونا با من مودبانه تماس گرفتن گفتن میتونیم صحبت بکنیم؟
ضربه سخت ایران تو راهه ولی قدری دردناکه نمیخام ازش استفاده بکنم
خیلی بحث هایی خوبی داریم ولی اونا نمیخان اعتراف کنن چون یکم نگرانن
شما میگین مذاکرات فوق العاده داریم ولی اونا میگن دروغ میگین
اونا میخان معامله بکنن و بشدت خواهان توافق هستن
در عرض ۴۸ ساعت خواهیم دید چه خواهد شد
قیمت نفت و گاز دیوونه وار میاد پایین چون سه شنبه مذاکرات فوق العاده داشتیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69556" target="_blank">📅 09:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69555">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d290294320.mp4?token=LuM57P0gQ0K49Oiu2iKRf4_Amp4eTVcUFw9RJL4eVYd1a9fS7Qc5j2oixNbLAAXSWiAsn0n9JHMt0pGX55CWL4X4N_BOmSajHwbyXOjfNSAUUDpl_g4VRYh3Xkoe5580Cgamv5_RgF7r2PK91f3b6m7jcOrNUfCHSJIcxWJrMSlbr_AEFYRSliD-6tO_xL5VFFdoaXOWycwQiroYz37_5URIhfES3elEed6f2sfbBu-3oLUlAF0kOrXTFPgvLSqmq90fW05TKhOTXMrYsSexYdq4x2_1CUgxjtCPZTOlbJgmwJE4VbLE2Tc5Eya8zEWRAkRzyh-tJ44YqpXEVUuoGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d290294320.mp4?token=LuM57P0gQ0K49Oiu2iKRf4_Amp4eTVcUFw9RJL4eVYd1a9fS7Qc5j2oixNbLAAXSWiAsn0n9JHMt0pGX55CWL4X4N_BOmSajHwbyXOjfNSAUUDpl_g4VRYh3Xkoe5580Cgamv5_RgF7r2PK91f3b6m7jcOrNUfCHSJIcxWJrMSlbr_AEFYRSliD-6tO_xL5VFFdoaXOWycwQiroYz37_5URIhfES3elEed6f2sfbBu-3oLUlAF0kOrXTFPgvLSqmq90fW05TKhOTXMrYsSexYdq4x2_1CUgxjtCPZTOlbJgmwJE4VbLE2Tc5Eya8zEWRAkRzyh-tJ44YqpXEVUuoGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
اینترنشنال:پزشکیان و مجتبی خامنه ای باهم دیدار داشتن و این دیدار تو یه ماشین بوده
؛
مجتبی خامنه ای صندلی عقب ماشین نشسته و تو یک مکان نامعلوم و پزشکیان صندلی جلو نشسته و حق نداشته عقب رو نگاه کنه فقط صداش رو شنیده
.
پزشکیان از مکان هم بی خبر بود فقط برده بودن ببینه اونو.
پزشکیان قرار بود از فرماندهان سپاه از جمله وحیدی بهش اعتراض بکنه که زیاد در دولت دخالت میکنه.
مجتبی اجازه مذاکرات رو بهش میگه ولی با هماهنگی سپاه پاسداران.
پزشکیان کلی مشکلات اقتصادی رو بهش میگه و میگه که اینطور بره ورشکست میشه دولت.
پزشکیان از این دیدار خسته میشه و میگه میخام مجتبی رو ببینم ولی به هیچ وجه اجازه دیدن رو بهش نمیدن.
پزشکیان که فوقش یه ساعت میشد فقط صدا می‌شنید چهره ای از مجتبی ندیده بود.
پزشکیان اصلا از این کار رضایت پیدا نمیکنه وبه رئیس دفتر اعتراض میکنه.
میگه این کار جز خورد و حقیر کردن من نتیجه ای نداره .
بدجور عصبانی میشه و جلسه خیلی کوتاه تموم میشه.
تصمیم استعفا از این جلسه شروع میشه چون پزشکیان احساس میکنه دیگه قدرتی نداره توی اداره کشور.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69555" target="_blank">📅 09:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69554">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d7b56246.mp4?token=A1DEm7i2XAONlhWNJvLjDUQCpYMF3n-NfkeWDj8aU6QXhihXNwKAI3xnKkufBGA_L5iMvNbOiML3SZ02XkBcp1NJ5N61GioACccaOhDKw-pja7N7XnKi0Y9J1VX-zMK7rxS_Wss2LK-wZQNjQHseTTNznMyFwy-WbiWYSG7miJNHRyBCzwYgfePfeRFgOy_oJ33Cv-EmfgUddtg1h-ZQFgmcoylnX796r1D4Yo2iZ5j2l393MALLv9o_oalnB3ZQqgMcncSMKtHmmoXT023vxsh0CJCxnkoRgq6Mcp_hxeRP-1ZC-4QhnzPn8UgeTsfas-eCZAWKdMCYWFDHseunkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d7b56246.mp4?token=A1DEm7i2XAONlhWNJvLjDUQCpYMF3n-NfkeWDj8aU6QXhihXNwKAI3xnKkufBGA_L5iMvNbOiML3SZ02XkBcp1NJ5N61GioACccaOhDKw-pja7N7XnKi0Y9J1VX-zMK7rxS_Wss2LK-wZQNjQHseTTNznMyFwy-WbiWYSG7miJNHRyBCzwYgfePfeRFgOy_oJ33Cv-EmfgUddtg1h-ZQFgmcoylnX796r1D4Yo2iZ5j2l393MALLv9o_oalnB3ZQqgMcncSMKtHmmoXT023vxsh0CJCxnkoRgq6Mcp_hxeRP-1ZC-4QhnzPn8UgeTsfas-eCZAWKdMCYWFDHseunkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
بازم ترامپ از ترور جون سالم به در برد:
⏺
فاکس نیوز؛
مقامات اعلام کردند که یک مظنون مسلح به نام «جنین جان تائله»، ۳۸ ساله، در زمین گلف «ترامپ نشنال» دستگیر شده است؛ وی متهم است که پیش از سفر رئیس‌جمهور ترامپ، تدابیر امنیتی را زیر نظر داشته است.
پلیس اعلام کرد که متعاقباً از منزل این فرد، یک قبضه تفنگ مدل AR که به‌طور غیرقانونی تغییر یافته بود، جلیقه ضدگلوله، خشاب‌هایی با ظرفیت بالا، مهمات و دفترچه‌هایی حاوی «مطالب نگران‌کننده» کشف و ضبط کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69554" target="_blank">📅 02:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69553">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">#اختصاصی #فووووری
🚨
ملی‌پوش پر حاشیه در آستانه پرسپولیسی شدددددن  https://t.me/+FgpywJWoBXVmZGU0</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69553" target="_blank">📅 02:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69552">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cKqZoYEpNliIX87QMXgk0NoI-K7zv0D-RUnJgnCiP_UZy6VEQxkPf1N7WXUEgnvW8W5wMxAMZznpvIJzO326bhLcMnv2tLDbV99qrMyhBf-aAiqrCvmf9xoKynROnUTCq0Fv6gL_5n7nUgqSGny0vlzTKQtZmlxC1wA4RcfjdZL1X86h680RIIBY0SolARDvtPKbC7xWmcmmlKbeTG-2ZYSFLpg2Vrxx5Bg3yPW7Z8JXdbSUxkr8cysyJBYyJOMLxRytecfDXtA_OAG9fXrU3ASnzGY2OIgivNN9QOYCd45Oct2hOu77mEwE4IBL-la9TR0vHoSM0trvxxjaYoWS_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و پرسپولیس هنوز هم شانس رسیدن به هم را دارند!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69552" target="_blank">📅 02:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69551">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbrIClA7RtgUscxZNjYRnH6SAgBM53qXXcGBJ2TitXbF3FArCO8q1EmFXdgsTBCENk9aalrsk7ZCF5vEkidicUnYOFmlGWNaF0uP31hEXWx9Rk-zvI5RcvFUL3AmHlCz_LwSfUCQ34b9fAa1Z0cf9kOvvwx2mJ1oziWr8pnPZW2pbke1cedrDqLbPBhO4XR6B_3KKmG9k_kDIsze2T74RJbFqu0CxeAkCysx1PDCOKurTxO81kJFR-lvq_7ZkRpyDE8QdqmjQQ0Jo6VGaVZ4cdKICV2wfco2VH5jjwRJAm9CgNIPxvbjTe7Kfa2klkzQc0IICLmexN9KhV_NDNBiwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیزارم اینو یادتون بره
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69551" target="_blank">📅 02:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69548">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vn8J-KVbJw590JiLJdGrIJ3s1c3ihtlZUbNfB7HqvbZeaWzaN8rhvrKpSrk33drROo0EflGzNMdbQHofYSJwxqvrtJ57nnDWKFnwAqLWe6kQAxXd4iAksk9Iq2TMVYsUXZxKEw0K1rdeymlMZN8cD4c6qn-5kne6DWr9UWhCtSow9raLIKMi0ujiONFaWQSmdHumv_z3HsiqzaGfpgE9Xi8W0Gy4aBo4yhVaRwQ8ZPFLpJKNf30ADrQGgypY1xhRiH7J_ryxdoRpQOVXiXZLAsyTbQul5GZgT5LjlDcQvxo4vFT9xkY-pNsS3xfflqas3WRsI7Zmtw38WA7tqp_1sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/URMU9Rurvk2-9b3xR8zXVjpYmt_A0w273mIpTYyBmY-6HY14sAk9M1yFTB9Z7Xr5Sww4FjShKk7J-6TCdWjWabHmy3_3p2zeYgoznmdlaqFbTmksrGVFUA-8eNIWZw31ALA9evqD0xx98udenmMF5MZbLltHmVArYZyzPglq8ijQkYXKg59CKS8URf-hAgDbfSn4RuZuB_CAsODoOzhlhMsxb76bn2_BosH1V0uMp2hws1ik4-dN3f_TQu91-MKVI6Dbt-eRfUdlNiniIU60OuQ8aukV_Y05jy7iDf8GzlGSx6DlpuvutqUu7k4NuouPhajTGXy8MDxSRqNAzoYZHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d579f85e4e.mp4?token=fC18xOF1wKrJNuNJAEA8bnUP5lQL6sO5hG6CGGkqwh1WfjbTaMYNiGRrVEXcahHh5IkVdphKHrbLTECRCfg09XHbLOuM1y9MLCH6dndOCSKM5WzzP2Elox3Djzha1fZ1RURaVKRE2KIMw7P0iE6URdS-JzgeQ0mT0DyaH0CkFzY8CfQ9dOO-Q_7uDfrG0FlPgJ14A_u2NwKcenDKNNY-WK8eT-QjOAV3KnqlHhzvFCX-Z62ey4_VvzUk8Q310GJ5toUkoSBSWGYGfwyTW3ZzJKrGJMGXnJE1K5QnRHMsq9Mk7w6yGVJjf8E2MPKE_19MTyAcrKUR5mVIDX46uM5Uww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d579f85e4e.mp4?token=fC18xOF1wKrJNuNJAEA8bnUP5lQL6sO5hG6CGGkqwh1WfjbTaMYNiGRrVEXcahHh5IkVdphKHrbLTECRCfg09XHbLOuM1y9MLCH6dndOCSKM5WzzP2Elox3Djzha1fZ1RURaVKRE2KIMw7P0iE6URdS-JzgeQ0mT0DyaH0CkFzY8CfQ9dOO-Q_7uDfrG0FlPgJ14A_u2NwKcenDKNNY-WK8eT-QjOAV3KnqlHhzvFCX-Z62ey4_VvzUk8Q310GJ5toUkoSBSWGYGfwyTW3ZzJKrGJMGXnJE1K5QnRHMsq9Mk7w6yGVJjf8E2MPKE_19MTyAcrKUR5mVIDX46uM5Uww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
حملات شدید و سنگین روسیه به کی‌یف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69548" target="_blank">📅 01:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69547">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWY8gC6d6x17UK314iAuRNyEmGhQ0ani5mlIpT6RDySBrZlqIZwCM_9975GtINM9LVy0MI7d-Z1J1GHIMet4uGEqlynAVKaxz0A6EIHua8pGQIaKAfV3IBT0hlVsw_uEmCDcZNwUzRLkWLN591p_9hUqpWJD9wdc9xej9OuNSN7a0KIDvFfMKI6UTHbdNkMXonusWKUlXWRa0WTCLfMwHyZYZ3Fjn1-hkcaVHlvlLU6IGHltfRbiPOPiWoCdnoSRkELhKM3vMrADOkb3QtoS_cMOEvyu6EmgEZZVRrm8VADY1cIu3ioZrCaGmux4g5_5kQySXL4MW0c2bQtjHLrUCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
علی قلهکی:به نظر میاد یکی از گره‌های اصلی مذاکرات ایران و آمریکا، ماجرای تردد کشتی‌ها توی تنگه هرمزه و هنوز سر جزئیاتش به توافق نرسیدن.
هنوز مشخص نیست کشتی‌ها دقیقاً از کدوم مسیر باید رد بشن و مسئول امنیت و هماهنگی عبورشون کیه.
ایران می‌خواد کشتی‌ها بیشتر از مسیر آب‌های خودش عبور کنن، اما آمریکا و طرف مقابل مسیر عمان رو ترجیح میدن.
اختلاف اصلی هم روی نحوه مدیریت، امنیت و کنترل تردد کشتی‌هاست.
هر اتفاقی توی تنگه هرمز می‌تونه روی روند مذاکرات هسته‌ای هم تاثیر مستقیم بذاره.
آخرین پیشنهادی مطرح شده مطلوب ایران اینه که کشتی ها حتما مسیر ورودشون، مسیر ایرانی(شمال)باشه و مسیر خروجشون حدود ۴۰٪ کشتی‌ها از مسیر ایران و حدود ۶۰٪ از مسیر عمان (جنوبی) عبور کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69547" target="_blank">📅 01:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69546">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SE4udoqB4VWx58vTfleV04lyaABkvxbpJQ0l3xIcmP2-gAhRogoVo4oD0Lkamg3SUtsqhSi7S8shFAJ2tefZPHJc3MrwrDPTG1TFR3KCkNWaL_EA5vne5KSw24FHYu2CxI7zuWr3VAPH67WgJWRdXlHNzOFwsmAS592e7IY8_xN3IFevHSr8mUzGsWI2ZjRbpV_GCYCw1kO-23kgmPwBg91rNdFV2C3veKkcftwnxplj_L-3jEfrIEj0COv00syBYihkM7KwcVOhfy5gVBGN9ozgLzOd76nupekEAinuWl1J-2hOtJOqFe8rLa4QicyHPh5sxnREgIYQSSz0wAijaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇺🇸
بازگشت غول‌های سوخت‌رسان؛ بزرگ‌ترین آرایش هوایی آمریکا از زمان جنگ خلیج فارس ۱۹۹۱.
پس از پایان جنگ جهانی دوم، جنگ خلیج فارس در سال ۱۹۹۱ با استقرار حدود ۳۰۲ فروند هواپیمای سوخت‌رسان، بزرگ‌ترین تجمع هواپیماهای سوخت‌رسان در یک عملیات نظامی به‌شمار می‌رود.
اکنون نیز در سال ۲۰۲۶، با استقرار حدود ۱۹۳ فروند هواپیمای سوخت‌رسان در منطقه برای پشتیبانی از عملیات علیه جمهوری اسلامی، یکی از بزرگ‌ترین تجمع‌های سوخت‌رسان‌های نظامی از زمان جنگ ۱۹۹۱ شکل گرفته است؛ آرایشی که در بیش از سه دهه اخیر کم‌سابقه بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69546" target="_blank">📅 01:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69545">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aL9afYcFY-O4vd_IqdTDdPFH7cUj2phKwWX1oGThzsuVMmXv5ckNIeKOy2VA-ssWc6TgXj0BepPFci1yQzGjvztLmlCozNbLlHcDbMu-h_yVR64-BdcYuGLUMDWR92l1zzTOOwY4AyZP5v_NpBlfTORj1n0CTXnzCY0M7UP3-hZMoCWO5Y5gWnTABXrO7tbg8zzZtOc7lCIn4uJV9a6nRPgb9oOPIwbBzqPEvZh_j8ExaIyJWKk62zPTFJb3E0_Sxh733EncSf5_xOovfbb-ss6qo2jpdYlmB-0xga6VnTGi87d3XSiwc8RNTfehxINUWRNWVWOucDpXrknegp68wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام:مسیر جنوبی از طریق تنگه هرمز برای تمامی شناورهای تجاری که قصد عبور از این آبراه بین‌المللی را دارند، همچنان آزاد و باز است.
طی سه ماه گذشته، نیروهای آمریکایی علی‌رغم اقدامات خصمانه و بی‌دلیل ایران، به بیش از ۱۰۰۰ شناور برای عبور موفقیت‌آمیز از این تنگه کمک کرده‌اند و این ترددها همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69545" target="_blank">📅 00:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69544">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31eaaf6719.mp4?token=lTwDI-i_S0usRHC2qt6hpzKIk6xumEHuK5z0n6jpL0Dt6zUf92yNNRUB80wrXNSGc2ZM9eI3uqIxGoDsELl5ce4AieVakReAkRnRbfIHK4htumyvd-aPN2CvUBbLBw69mLthWjAFAEFtbSfWG5dAa3ZxObIsf1v3_tmR68lt66UFcIo8_J-f_sh-M0_nDrOID66Z-fSifMSWrgYXv_HRdeNUA7Vd5eMRHzqB9K2GA8bHgEojEQaf4lfh_fbA4o2Axym46GrBOMenpt8EQPO-DA1t4G6tHh5S3teyX6cuNDC7VRckYHDTFE13oz79GTYymgWzWrxPJAHkn-4ObFOwWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31eaaf6719.mp4?token=lTwDI-i_S0usRHC2qt6hpzKIk6xumEHuK5z0n6jpL0Dt6zUf92yNNRUB80wrXNSGc2ZM9eI3uqIxGoDsELl5ce4AieVakReAkRnRbfIHK4htumyvd-aPN2CvUBbLBw69mLthWjAFAEFtbSfWG5dAa3ZxObIsf1v3_tmR68lt66UFcIo8_J-f_sh-M0_nDrOID66Z-fSifMSWrgYXv_HRdeNUA7Vd5eMRHzqB9K2GA8bHgEojEQaf4lfh_fbA4o2Axym46GrBOMenpt8EQPO-DA1t4G6tHh5S3teyX6cuNDC7VRckYHDTFE13oz79GTYymgWzWrxPJAHkn-4ObFOwWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان:
اگر استعفا بدهم، رسماً اعلام می‌کنم؛ استعفا نخواهم داد و خواهم ایستاد
ما با نیروهای نظامی، کاملاً هماهنگ هستیم.
می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و این‌ها یک چیز دیگر.
همه مردم برای ایران سختی‌ها را تحمل می‌کنند.
یک عدد سه هزار نفری را سی چهل هزار نفر گفتن، نشان می‌دهد که این‌ها چقدر نامرد و وطن‌فروش هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69544" target="_blank">📅 00:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69541">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KDoqaiHhB1y4iTO3zwyRb88gXE4-EnNKkTPB5bGJs8wp0SAXkEQmrkiL6SxTrGOo9EJzKoV7DBaTRemenyOVahiyG4pmW017vBr6B27k1q1Xc0grWDNU0maj2G2U0DUF99wkan3A6Xk7FGvzJGFAnQxoHJrI616BsepujnNF5lmoEKoewhzfu48kgY1YhseEEZnn7UAjHXueb-MFLgsL2oennUUb-0KzsUvLlgSl3aVCgrN8mB5q0BjT4NHHYazT75qBi3odJnisex0Ak3jJhr50TrWG2vz30cTbL2bhBcA18lDMf1W8_a6Ml4F5r8xKj6iJ7qhHlSAI3Gh6EIj83g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZtlcPYU-7V8qWWfcX5sMlbbashiZH4ki4G8rTFOD4Ob7XPlfLj2BMw3X5VNd7I8Atrc9HxahhSN_PSrXvAbu1VlOaAs54cUy53WKKerqVeaxg0Z60oZd5F5j53pvge8xYpswDKd59QrZY6LQOLLpbx2wYvsFC7kAF7jWb7fKw-JxdIL30YTazHJwmUGXhc99elF_czE8VNxfDrumTCsEEYEhUZxKUcwNj9tjLfmzJcgL4k9h2Ce6xxi7L0WqYDWJHuD2vkhV230rFkblOH2Ovnue3TofG-_HBNjKQbcjVBSioUq2T1dPzowUQf8Hs1ty9KTN1K00ShrpclZgBRt4CQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▪
🇺🇦
رونمایی اوکراین از ربات رزمی «Droid TW 40»
.
شرکت اوکراینی
DevDroid
از ربات زمینی تهاجمی
Droid TW 40
رونمایی کرد.
این سامانه با حداکثر سرعت
۱۳ کیلومتر بر ساعت
، برد عملیاتی
۵۰ تا ۷۰ کیلومتر
و ماژول رزمی
Wolly
مجهز به نارنجک‌انداز
Mk-19
کالیبر
۴۰ میلی‌متری
عرضه شده است.
برد مؤثر این ربات برای درگیری با اهداف
۱.۵ تا ۲ کیلومتر
اعلام شده و
Droid TW 40
می‌تواند در حالت آماده‌باش تا
۱۲۰ ساعت
در میدان نبرد باقی بماند.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69541" target="_blank">📅 23:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69540">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gng3xWCbaSNIZmwntc8387pC8WEvaPg5b1tVA9KwWuKVjh4drd8gccuSFgBK8lyM46HOu5HLrv-Ic4QuwmJN84fG7gIO_1lcNKwiQxrZ6VMq7CEhnbm-H3KVYnDR0INiiwO5odHS3JDsNYgAOwis-hetncTQ9aayCW3qxk5RtB2mKGckof_hbtROHn2XhHAVAu8BfDCUWq10MOkiKwbqwXko0JCLTO3uA4NOHje2N4_S9T-vVR-W4Ik66HDsHKq1Byxj1fSNGsmCXGz1HU4uS0oavV54U5LqMFmIhumToNZCh9YFhT0M7-EtgfZiyFZf1eo6rr8NnCigVgOrOPvQGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
نقاشی وایرال شده از زمان قاجار:
در زمان قاجار زنان روی یک وسیله تاب مانند میشستن و یک زن قدرتمند، اونارو بالا و پایین میکرد.
شاه یا یکی از سران مملکت هم اون پایین دراز می‌کشیدن تا زن انقد روی آلتش فرود می آمد و بالا می‌رفت، تا ارضا میشد!
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69540" target="_blank">📅 22:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69539">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c9b5938d.mp4?token=Zl9itye3HdDQ8SQpmdaoPeSP9ukr_lQdCS4ueCYNNC2SOf5I0s3OPh7SF7iY7rDk2_11mNOYnjPGR8DzvzTFPa0yf_HrXVHbTe9yRILOgOoaZEQxDikjRrBDObpGmhZ6zjxV823wiJOj6HmiZ1OV7z8RcHjJR9dFlpwR4WajPecqqbF6TSz6KDxsLdiQtynsOVEHn2i0fAK-_m-U0y2bEAHtydUfqZKRTqMDDbXU4tHfZgHKiHsuohDVBWgehmI8Jhxbzo1Vkfe_mmwC_4cAMs2vKJEqjwgYqQi3sMSc_yfpDT5QtBjT9xz0Wl7A_xCGSmk9kNq3kTfESNV7-E1BDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c9b5938d.mp4?token=Zl9itye3HdDQ8SQpmdaoPeSP9ukr_lQdCS4ueCYNNC2SOf5I0s3OPh7SF7iY7rDk2_11mNOYnjPGR8DzvzTFPa0yf_HrXVHbTe9yRILOgOoaZEQxDikjRrBDObpGmhZ6zjxV823wiJOj6HmiZ1OV7z8RcHjJR9dFlpwR4WajPecqqbF6TSz6KDxsLdiQtynsOVEHn2i0fAK-_m-U0y2bEAHtydUfqZKRTqMDDbXU4tHfZgHKiHsuohDVBWgehmI8Jhxbzo1Vkfe_mmwC_4cAMs2vKJEqjwgYqQi3sMSc_yfpDT5QtBjT9xz0Wl7A_xCGSmk9kNq3kTfESNV7-E1BDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیو ای از یک پهباد روسی که یک شهروند اوکراین رو تهدید میکنه و در آخر هم خودشو میکوبه به طرف و منفجر میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69539" target="_blank">📅 22:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69538">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3447971507.mp4?token=rgL0rsxYjrJqiTtz4OhdZqUTGIpx0RrzXg7gNe7ExfX9_RGQpqjHOXvwNBcQDBL2BRq5YRzP1UYupbeOqSLd93PeFSjfVAQN_MO5lFpQiIwxwHM0BLITiY5EmSvgmKkyHwO7PBtwwP5fFGdfcKeR8wdExaEwabjubI46QAzXy28JeT7BdekrdDLsbEQJXAQwfvKYgBQ381z8kHHeLCVE-vBpHSzzHxiEd11vQu2JyiFldXIMVlgFB3oMlmjs_M1sF3HUDT1q9aM7eUZIRJ0xdTFbfDPYsZ2hJsVJdzxXu71pLfQ25B25eIUpIKAjGKCyIZ0YLWp-75LIUG8yv4U2wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3447971507.mp4?token=rgL0rsxYjrJqiTtz4OhdZqUTGIpx0RrzXg7gNe7ExfX9_RGQpqjHOXvwNBcQDBL2BRq5YRzP1UYupbeOqSLd93PeFSjfVAQN_MO5lFpQiIwxwHM0BLITiY5EmSvgmKkyHwO7PBtwwP5fFGdfcKeR8wdExaEwabjubI46QAzXy28JeT7BdekrdDLsbEQJXAQwfvKYgBQ381z8kHHeLCVE-vBpHSzzHxiEd11vQu2JyiFldXIMVlgFB3oMlmjs_M1sF3HUDT1q9aM7eUZIRJ0xdTFbfDPYsZ2hJsVJdzxXu71pLfQ25B25eIUpIKAjGKCyIZ0YLWp-75LIUG8yv4U2wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
چهار سال پیش در چنین روزی، یعنی ۴ اوت ۲۰۲۰، انفجار بندر بیروت — بزرگ‌ترین انفجار غیرهسته‌ای در تاریخ معاصر — پایتخت لبنان را ویران کرد.
هزاران تن نیترات آمونیوم که به‌شکل نامناسبی در آشیانه شماره ۱۲ انبار شده بود، دچار حریق و انفجار شد و موج انفجاری ویرانگر ایجاد کرد که چهره بیروت را در عرض چند ثانیه دگرگون ساخت.
این انفجار دست‌کم ۲۱۸ کشته و بیش از ۷۰۰۰ مجروح بر جای گذاشت، حدود ۳۰۰ هزار نفر را آواره کرد و خسارتی بالغ بر ۱۵ میلیارد دلار به بار آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69538" target="_blank">📅 21:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69537">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8eaaff36d.mp4?token=SV8_8m0q8b4bMCgxOO1S1SELhTMvEEO9vW_iZANzJc-azF51_RHEBpbNmq8fRSxwPiBthwf6Mo9MQwBFagWVeLqEdLQqfKq_N_HtM0Y5HAQM-k9gl4TGWi1SZKgSit0kY1tYHqzO-DrAAXW_nxyt3IuRTxReZY3BYNCB_zzona6rVeKbgcsOdsIoG3vdkz3TBYUO6ZuBSJXi1ZgDSjqyC8bQQwuOUkPfesDEUl5h-pD6PRlxm8qtl47KvLHCc9AjaEYqL0fMTkMh5F1P0L2M91BgPgb6rLgq3UeAypqMnoR78O8eGqrWU5ljBhLiHyjlG4WwMStlMkEzqtcqre614g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8eaaff36d.mp4?token=SV8_8m0q8b4bMCgxOO1S1SELhTMvEEO9vW_iZANzJc-azF51_RHEBpbNmq8fRSxwPiBthwf6Mo9MQwBFagWVeLqEdLQqfKq_N_HtM0Y5HAQM-k9gl4TGWi1SZKgSit0kY1tYHqzO-DrAAXW_nxyt3IuRTxReZY3BYNCB_zzona6rVeKbgcsOdsIoG3vdkz3TBYUO6ZuBSJXi1ZgDSjqyC8bQQwuOUkPfesDEUl5h-pD6PRlxm8qtl47KvLHCc9AjaEYqL0fMTkMh5F1P0L2M91BgPgb6rLgq3UeAypqMnoR78O8eGqrWU5ljBhLiHyjlG4WwMStlMkEzqtcqre614g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
ترامپ و تیمش تصور می‌کنند که می‌توانند حماس را به خلع سلاح و غیرنظامی‌سازی غزه وادار کنند.
آن‌ها پیش‌نویسی برای ما فرستادند که ما با آن موافقت نکردیم.
این پیش‌نویسِ ما نیست؛ ما نظرات خود را ارسال کردیم. ضمناً، ما نظراتمان را پیش از آنکه شاهد هیاهوی رسانه‌ای پیرامون این موضوع باشیم، ارائه داده بودیم. موضع ما همین است.
و ما بر سر منافع خود، هم با درایت و هم با قاطعیت، ایستادگی می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69537" target="_blank">📅 21:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69536">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6rlKbOP9VYu0ksdYEbErdKaY8dazrz7gSK7lawqg872UwJkdOq_8g0mkg34nDZy3EHDwTaBdpSZHPMouSWRudjnXsKfZgxtLl3StrBs_go9niLDO54spWoNVx6ot4VOB8hQPNzEQYwdgmO_vtQ4vupafh_iGxIZdJnKJHWkWhktt9G2QN1Q0asXtiDpyE66mDO4Fu35Kl9Z_k43FigYm5kpF9VQo6c-69nQjsJeyxtf05FCdEcAJmLPXRmiwAxiNUAChCQwjxkvIQTnfbL0TGgLW8L_h4t8KhvUCDkaUMDcJMMBosRxkGaz6t7MhLW5R4axmnZe_R8idu_gZthAEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
وال‌استریت ژورنال: در حالی که دولت ترامپ بر نزدیک بودن احتمال دستیابی به توافق تأکید داشت، وقوع حمله‌ای جدید به یک کشتی در حال عبور از تنگه هرمز و بروز اختلاف بر سر مسئله عوارض در جریان مذاکرات برای بازگشایی این آبراه، چشم‌انداز این کریدور حیاتی انرژی را با ابهام مواجه کرد.
به گفته میانجی‌گران منطقه‌ای، بر اساس پیشنهادی که هم‌اکنون در دست بررسی است، کشتی‌های عازم خلیج فارس از مسیر آب‌های ایران وارد می‌شوند، در حالی که شناورهای خروجی از خلیج بدون پرداخت عوارض از آب‌های عمان عبور خواهند کرد.
میانجی‌گران اظهار داشتند که اگرچه دیپلمات‌های ایرانی در ابتدا از این پیشنهاد استقبال کردند (زیرا تا حدی کنترل بر تنگه را حفظ می‌کرد)، اما تهران خواستار حق دریافت عوارض ــ که احتمالاً با عمان تقسیم شود ــ و همچنین دریافت تضمین‌هایی در برابر حملات مجدد، پایان محاصره دریایی آمریکا و کاهش تحریم‌های نفتی شده است.
مقامات ارشد منطقه‌ای اعلام کردند که آمریکا و دولت‌های منطقه با درخواست دریافت عوارض مخالفت کرده و خواهان تضمین‌هایی هستند مبنی بر اینکه ایران و نیروهای نیابتی‌اش، قلمرو آن‌ها را تهدید نخواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69536" target="_blank">📅 21:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69535">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qoXkvJtHKzkRPH1yRGVIzOGAvaHJOeLPKJVeFQxXpRP7wBcQIdqiNNQd5SVJA1bkkFjnYObrNn4gNwloGXCXu4WA8gXa5lKu1fR7wW-ju0GqBJuYN7QmE-yCMafEaiNKDwQA4KjiQRhSc3yU2avb04J9-ZlNtXcoBlC8ZrkiplhtfKd7KGk4Ewzpd-glKDmCNgAqGeB6ztgsmx28v3NDRLx5VgXgwZaj71w5RmaixXN6F2fwzIhYj2QldCFooFUEDdc7Et6-V1N8FrUmBgCt_wsd95pkg8f4-DthxTGxbkQ9a9fP-IKYS3jRh3Mub33PC-jHHAPIqFZuvDJUrg9P7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام:یک ملوان نیروی دریایی ایالات متحده در «مرکز اطلاعات رزمی» ناو «یو‌اس‌اس باکسر» (LHD 4) مشغول نگهبانی است؛
😃
این ناو تهاجمی-آبی‌خاکی در حالی که از محاصره اعمال‌شده توسط آمریکا علیه ایران پشتیبانی می‌کند، در آب‌های منطقه در حال حرکت است.
تا تاریخ ۴ اوت، نیروهای آمریکایی مسیر ۴۵ کشتی تجاری را تغییر داده، ۲ کشتی را از کار انداخته و برای اطمینان از رعایت مقررات، وارد ۲ کشتی دیگر شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69535" target="_blank">📅 21:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69534">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19c9ea7021.mp4?token=gSrKBfxcJ8mz-oeWcjh8qBI8C7LWWvnUhYtpYlbox-xJV8Cm7WQHI-_EQ1B-CzfsY2qyA9inNfzAJOKGFoIl6l7US19kq3FdJlYjRGH4tvtuADLwtzagBe5WfxR5AwXtaMo4od9tg19zRjS-SkBYblr-LFsfWBOsVu4PVQ_BWBxoGT3RBwjiN2s-2GPVe0Pyuc4BfyOKPt5Z0Dz_F7GYg0g1a7Re95gG_FIb-BdZZUS5oWl-w99K3STXoSTpu1ZIugN4QQnw-QnrbB-lmC7a35QErrPRzA1zrKvcKiKUh5yZU0Urxhb4NCE8aa_XsjZ1TkOew4pQx4Eml_d0fgJk5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19c9ea7021.mp4?token=gSrKBfxcJ8mz-oeWcjh8qBI8C7LWWvnUhYtpYlbox-xJV8Cm7WQHI-_EQ1B-CzfsY2qyA9inNfzAJOKGFoIl6l7US19kq3FdJlYjRGH4tvtuADLwtzagBe5WfxR5AwXtaMo4od9tg19zRjS-SkBYblr-LFsfWBOsVu4PVQ_BWBxoGT3RBwjiN2s-2GPVe0Pyuc4BfyOKPt5Z0Dz_F7GYg0g1a7Re95gG_FIb-BdZZUS5oWl-w99K3STXoSTpu1ZIugN4QQnw-QnrbB-lmC7a35QErrPRzA1zrKvcKiKUh5yZU0Urxhb4NCE8aa_XsjZ1TkOew4pQx4Eml_d0fgJk5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام:
یک جنگنده رادارگریز F-22 نیروی هوایی ایالات متحده در آسمان خاورمیانه از یک هواپیمای سوخت‌رسان KC-135 Stratotanker سوخت دریافت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69534" target="_blank">📅 20:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69533">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESKF3EnNW2C7WOm710Y8fN0MlF_079fUng6F-qvTH7m4o0UvPQ9YzMTGc0N2mIQ5HDzvR_v1tzdnbs4T3NnMmCw3TVj2UfemrxiNTK1uF46Po6CQLn2dCuc_yK4s6neIV39LG_wFMZa5mnrB_dltNgOfW7N3glDeAxO3QyzSFMjJGXA_jImStXE5EKs4HOZebU8TqV4pI9RAFTPn2bBs4hTr-MeloaEZxAITZmSajMYsv7x4dy6HRJ8B8VuIkH4zcqwr0Csz6cUIcgaLnrspacM7LZGBw1_G3ZbhbnHBFPaFwQlUNM4DSk9h6oM8lNUPn1h4oaR0eQ2kl85PuY8XSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
بلومبرگ:
ایران در حال بررسی امکان مشارکت کشورهای اروپایی در عملیات مین‌روبی در تنگه هرمز است؛ اقدامی که نشان‌دهنده احتمال تعدیل موضع پیشین این کشور بوده و می‌تواند به تلاش‌ها برای ازسرگیری کشتیرانی و پیشبرد مذاکرات با ایالات متحده کمک کند.
تهران پیش‌تر به‌طور علنی با هرگونه نقش‌آفرینی خارجی در مین‌روبی این آبراه راهبردی مخالفت کرده بود، اما در هفته‌های اخیر و در چارچوب گفتگوهای گسترده‌تر پیرامون عادی‌سازی تردد دریایی و کاهش تنش‌ها، انعطاف‌پذیری بیشتری از خود نشان داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69533" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69532">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3030125dc6.mp4?token=n2usCCrj4GJB5u3LHLJ1vY_MWaZ-c9UJzzatfNxiYLp0xPETAb5PAJWjXPa-o3iMa0UHS7sq7f7-iViq4BTJDtPCGp3z0jWbGceQjI4ezj0xg2xXAXNZ2F6y3iTk8f_CXSc4MJC8eIEx3L7K6Ca7ZxdwtrFKpqbw-FerR8jj-1-gwlHFegtIchPn3jQBUp4jzZ6x4v6iPBrWvHH_jsX863QgQWKq28m3QwJxeWYhHaajq-CH-Qpjgb8hvvACfbGaQ1tUtHlIVsLA2Kobun4OBum37tYp8w9awgT75lromRS1ojup-ZZd30hJTenRJ4LKpM_aa1eWx4jEKZQMp6of9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3030125dc6.mp4?token=n2usCCrj4GJB5u3LHLJ1vY_MWaZ-c9UJzzatfNxiYLp0xPETAb5PAJWjXPa-o3iMa0UHS7sq7f7-iViq4BTJDtPCGp3z0jWbGceQjI4ezj0xg2xXAXNZ2F6y3iTk8f_CXSc4MJC8eIEx3L7K6Ca7ZxdwtrFKpqbw-FerR8jj-1-gwlHFegtIchPn3jQBUp4jzZ6x4v6iPBrWvHH_jsX863QgQWKq28m3QwJxeWYhHaajq-CH-Qpjgb8hvvACfbGaQ1tUtHlIVsLA2Kobun4OBum37tYp8w9awgT75lromRS1ojup-ZZd30hJTenRJ4LKpM_aa1eWx4jEKZQMp6of9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حسن عباسی:
زیر جزایر و سواحل تونل‌های موشکی متعددی با امکانات متروسازی شهرداری تهران ساخته شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69532" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69531">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتبلیغات</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1S_g-dLWKDvUv7Sec21Qq7v1f8FUrpcPDHB2ZgIkXe_klOa4CW8yZa4w5bbP3PaKlPjlQVG1S0v_Bv45Jpr8TFwHy-tltBVgRgCZ8vm70ZY1Zuz9YXT4qGlV795foWoB1iW-i1OaOK7IV9aWLfmjec1g_XY0ulHPz1Jdp2CSP8M4w5j2OJG438feDx_kmGcEgmvErz3c_bkcnHZ3Pl3ZSdf9B19LTET_ZqUkO5SSRQPOy8pIMd3aqioYm4M02aNocWlVaXtNmIrIc6a8NZOiYKhSjAZMOIX1qmsQifc1NQ-Ycsf9Pa2zESqOSDsBAxb8U90wgYx-B0oXrMkmNyp5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
این حساب دوستمه تو ۱ ساعت ٣٥ دلار یعنی ۷ میلیون در اورد
🥇
گفت یه روش که با گوشی انجام میشه
💎
۹ دقیقه اموزش میبینی سرمايه اوليه ام نميخواد تا ریسک نکنی
🚨
بعد ۹ دقیقه میتونی روزی ۳ ۴ میلیون با گوشی در بیاری
رو لینک ثبت نام فوری بزن اموزش ببین
⬇️
⬇️
⬇️
🆓
ثبت نام فوری
🆓</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69531" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69530">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca94237dda.mp4?token=GRi99QKClrJ8_Kc0uhMJhMiPQ-rjylXV6eaRf1b4aVNkYuv91caorTMoGXWj-dlw_F3ehdiNrGYgcwSIE_6j_GS4l8wCyHVvLApczByH1jrnSiCsM6xXUgfqBJn3x2CwKbw0Oz3HBqI1gLEju7iJMwKxdfHqS0UgnSIfw06RNN40z1cRXs_ybbv0ofbxdWlhsU0sayS0jjpn9XPtnShP0cxYWqbcqtqqpN3dFdmBoc11Ma9kx5e75MBe10tdmRpnv1SulFvzJBKqVL9-fsBdTGdxJbcpH3zpqqL9LBdAtZ6wAW65j8_jBl63RbYDfuhh-5FM_5P9HiZZJRWRbtAFEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca94237dda.mp4?token=GRi99QKClrJ8_Kc0uhMJhMiPQ-rjylXV6eaRf1b4aVNkYuv91caorTMoGXWj-dlw_F3ehdiNrGYgcwSIE_6j_GS4l8wCyHVvLApczByH1jrnSiCsM6xXUgfqBJn3x2CwKbw0Oz3HBqI1gLEju7iJMwKxdfHqS0UgnSIfw06RNN40z1cRXs_ybbv0ofbxdWlhsU0sayS0jjpn9XPtnShP0cxYWqbcqtqqpN3dFdmBoc11Ma9kx5e75MBe10tdmRpnv1SulFvzJBKqVL9-fsBdTGdxJbcpH3zpqqL9LBdAtZ6wAW65j8_jBl63RbYDfuhh-5FM_5P9HiZZJRWRbtAFEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
غنی‌سازی اورانیوم چطور انجام میشه؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69530" target="_blank">📅 19:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69529">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tW1hJv2jg2ZtKcWCkEnsMXYrVUkrI24Y4lN1JCgQZvKzZogsRDM32XuwwLSmn-n2XJVPrvTlD1OV6DCfsAEgkQFIKuxWArv4XVC6N5YmUxmvzm-VOQRqsFV3AcSJZwawQscgDyY9oCZH2Me-nA7CHXVt9gJYGCit7uKLlL3VVoJsILM1zEAPMIeKx53eI_sfw91rmymUL4w1WA1e_9jN1IJlOWCTUncswG664Tik7SLRhEYPTfeOmekIPg-ZVUKfEdWXzwyyMBCx9wzTA2px0py5Mcpuwm7UCo2zw2uwls4LnT5P8IPqsIGx47TS2zoHWHL2zcCtVQT4N7EBqVqtDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
"توافق قریب الوقوع است" با از سرگیری مذاکرات با ایران درباره خلع سلاح هسته‌ای و تنگه هرمز.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69529" target="_blank">📅 18:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69528">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو، وزیر امور خارجه درباره ایران:  کشتی‌هایی در حال عبور از تنگه هستند. هم‌اکنون نفت از طریق این تنگه در حال جابه‌جایی است. تنگه باز است. ما درگیر گفتگو و مذاکراتی میان عمان و ایران هستیم؛ موضوع این گفتگوها آن است که چگونه می‌توانیم در کوتاه‌مدت…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69528" target="_blank">📅 18:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69527">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1eaa69fa8.mp4?token=DoAxFJj_cZJudMpsZzbeEdkAVXxBHMWBYmS8ApaB2XSbJoCfGQ6ddGxGypeGL-O_LUNRjUFitwTc0IWwdlMWF45WX18L9uj9Rt-hbvCZgdZXbodXCs1uTYdHmQ0OeLESbKY8E_OTaM_Lehl3QW9wuWkZlyhbcAreWB3KZXGM-pCp5YD36xT-MhcI4NxOS7-sN5Dsoj9N99tgm6Ylg7TxOxuKw_WcDXRvraKwXwe8xvqvlk_o0GToNcPcUnEZGNG0nwvPyK7tZrC1yEPHGP67gmjd2oNYKDMqSWoT3RK1Z0q5bm2gMpJXRfQKsC7nN8llGyr2x6eBawMFYOzcDSr7jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1eaa69fa8.mp4?token=DoAxFJj_cZJudMpsZzbeEdkAVXxBHMWBYmS8ApaB2XSbJoCfGQ6ddGxGypeGL-O_LUNRjUFitwTc0IWwdlMWF45WX18L9uj9Rt-hbvCZgdZXbodXCs1uTYdHmQ0OeLESbKY8E_OTaM_Lehl3QW9wuWkZlyhbcAreWB3KZXGM-pCp5YD36xT-MhcI4NxOS7-sN5Dsoj9N99tgm6Ylg7TxOxuKw_WcDXRvraKwXwe8xvqvlk_o0GToNcPcUnEZGNG0nwvPyK7tZrC1yEPHGP67gmjd2oNYKDMqSWoT3RK1Z0q5bm2gMpJXRfQKsC7nN8llGyr2x6eBawMFYOzcDSr7jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو، وزیر امور خارجه درباره ایران:
کشتی‌هایی در حال عبور از تنگه هستند.
هم‌اکنون نفت از طریق این تنگه در حال جابه‌جایی است.
تنگه باز است.
ما درگیر گفتگو و مذاکراتی میان عمان و ایران هستیم؛ موضوع این گفتگوها آن است که چگونه می‌توانیم در کوتاه‌مدت و هم‌زمان با حرکت به سوی مذاکرات بلندمدت‌تر پیرامون خلع سلاح هسته‌ای، امکان عبور ایمن تعداد بیشتری از کشتی‌ها از تنگه هرمز را فراهم کنیم.
در مذاکرات برای بازگشایی تنگه پیشرفت‌هایی حاصل شده، اما هنوز توافق نهایی صورت نگرفته است.
ما امیدواریم که این توافق به‌زودی نهایی شود
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69527" target="_blank">📅 17:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69526">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78294ca69a.mp4?token=UUMJXA1Uz2i2cQcTCNyfyBXdFbkcFGmslPPF7OfzzbQpOEBoSaCiUo4qpnDXaOc9L14Dyg72Q3cvInFa3QX3vS7VkdiRjQjJpdPdwiGhpfabdKdSfOGX1dHPQabVZX_iS-5GNHsL7KzBea6sVWVS7j8R8ke5-Si43wyBvL4WNIu5VDXxF3Gj3oOGIvT15UxhIeoZ-FaoYTDxfnRnXSq8o5pmIVSJYRSpxsX8TrN3_etixgXbDZujzlt5VcHD1st_SCljYoBwwCwouxA2bMrCqU47M22QHJsp_kF-2HkyLD12qCjBMtZzazuKCyXSe8UGaspZwGEL9mSrPr88eGzlow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78294ca69a.mp4?token=UUMJXA1Uz2i2cQcTCNyfyBXdFbkcFGmslPPF7OfzzbQpOEBoSaCiUo4qpnDXaOc9L14Dyg72Q3cvInFa3QX3vS7VkdiRjQjJpdPdwiGhpfabdKdSfOGX1dHPQabVZX_iS-5GNHsL7KzBea6sVWVS7j8R8ke5-Si43wyBvL4WNIu5VDXxF3Gj3oOGIvT15UxhIeoZ-FaoYTDxfnRnXSq8o5pmIVSJYRSpxsX8TrN3_etixgXbDZujzlt5VcHD1st_SCljYoBwwCwouxA2bMrCqU47M22QHJsp_kF-2HkyLD12qCjBMtZzazuKCyXSe8UGaspZwGEL9mSrPr88eGzlow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو پاکستان، یه تجمع ضد جنگ برگزار شده بود که وسطش یه گروه جنگی اومدن انتحاری زدن در رفتن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69526" target="_blank">📅 17:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69524">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57327c22c5.mp4?token=ctSlnAtD_d5BYNb5qPTIScQ8K4N9pZxm-tSzhry1Ut6nF8ygp-sSA5hQK72tD3gurANNuQ7Spn46-12C8OshHSzZewx5vJZ_UfC0oWQlmGmTsnzOhzKGhOHfbYF2ybDgoz_gYrfQjNrVo8xcxKbFc9YG73hTM3b8LGoLk_oObISa5dw9H_spJWRfKtYckl35k_p3pN2oXki2ljOBj5BUkXkyaCc5hIOEVDMPUlSgxRVcy4wISQxgLitaugvtfdAlh0ea2Vwc7A3BewKiAeGIwa6a3BYElwD1WDyTl6Q1byYuxdcZULgQDfgZDMxYHsOqOp3geqW7sHAo5vBFVL36ljdgg0zRbfUVO8QTjVSJFhIcXp5MjfVkpVfynLo0nQ9EJgD2cM93EVLsKvP7k-id7qtncfZh4NBfKcSyGXaoZbxe7o40keD9BCC89NFv-XBQTHoAPDJ434PsRpfic6ljSwk26r7QL-QmuLdqHWOFRecX7lkfOsoZe1bZp8vQ9Gyr70EknBGx-K6fI0eQ38X20VnWwHe1QR3XdDpz-X1MXhTD2YHBEE9zoZXu3zYFvaIf4fzz_tIU5C5hd3roPPYkZbCXP4-fI5jWdD-BuBecaeDTYQTccQOKjrXDKkpWFyzu5oGdpx8C4YUOrdjZ71k8TxDM4CMVNS3Ff14AZ_Nle64" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57327c22c5.mp4?token=ctSlnAtD_d5BYNb5qPTIScQ8K4N9pZxm-tSzhry1Ut6nF8ygp-sSA5hQK72tD3gurANNuQ7Spn46-12C8OshHSzZewx5vJZ_UfC0oWQlmGmTsnzOhzKGhOHfbYF2ybDgoz_gYrfQjNrVo8xcxKbFc9YG73hTM3b8LGoLk_oObISa5dw9H_spJWRfKtYckl35k_p3pN2oXki2ljOBj5BUkXkyaCc5hIOEVDMPUlSgxRVcy4wISQxgLitaugvtfdAlh0ea2Vwc7A3BewKiAeGIwa6a3BYElwD1WDyTl6Q1byYuxdcZULgQDfgZDMxYHsOqOp3geqW7sHAo5vBFVL36ljdgg0zRbfUVO8QTjVSJFhIcXp5MjfVkpVfynLo0nQ9EJgD2cM93EVLsKvP7k-id7qtncfZh4NBfKcSyGXaoZbxe7o40keD9BCC89NFv-XBQTHoAPDJ434PsRpfic6ljSwk26r7QL-QmuLdqHWOFRecX7lkfOsoZe1bZp8vQ9Gyr70EknBGx-K6fI0eQ38X20VnWwHe1QR3XdDpz-X1MXhTD2YHBEE9zoZXu3zYFvaIf4fzz_tIU5C5hd3roPPYkZbCXP4-fI5jWdD-BuBecaeDTYQTccQOKjrXDKkpWFyzu5oGdpx8C4YUOrdjZ71k8TxDM4CMVNS3Ff14AZ_Nle64" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی به انباری از Wildberries در منطقه کراسنی بور در منطقه لنینگراد روسیه حمله کردند.
انبار اکنون در شعله‌های آتش فرو رفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69524" target="_blank">📅 16:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69523">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/523118296c.mp4?token=MVilxIpVU09sDY8p_9ACMzzhbH4EXFk_IBzUP4WmydsPpibNbBCCrN9Uuyvjs3uLJNrIafrf4rI66BVbhuXJEc8nI8G8Ovi9MsXaLLZDS5XGuUpE2nQF7bIdKatlt1WoNJqeJnp7JeifWvdbX-IQegYQpLTNOcMUWMrm0UjOesB6VzFqDR3Rhk8E6NrMqSgB9MBkhmcYVtrC9elV5OeoiJuqRBqLo1W8PYfOrHuYP3jggwDZfCjNft0E5HHwH2n24UOknNrbVVBSeuYFv_jwRP9yTDCPRtUBobExWvHviwd1_uGzO8hi2RIcE0x1FrnOhKI6IdbrAGEHzEzYW7uDCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/523118296c.mp4?token=MVilxIpVU09sDY8p_9ACMzzhbH4EXFk_IBzUP4WmydsPpibNbBCCrN9Uuyvjs3uLJNrIafrf4rI66BVbhuXJEc8nI8G8Ovi9MsXaLLZDS5XGuUpE2nQF7bIdKatlt1WoNJqeJnp7JeifWvdbX-IQegYQpLTNOcMUWMrm0UjOesB6VzFqDR3Rhk8E6NrMqSgB9MBkhmcYVtrC9elV5OeoiJuqRBqLo1W8PYfOrHuYP3jggwDZfCjNft0E5HHwH2n24UOknNrbVVBSeuYFv_jwRP9yTDCPRtUBobExWvHviwd1_uGzO8hi2RIcE0x1FrnOhKI6IdbrAGEHzEzYW7uDCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی:
خرازی برادر همسر مسعود خامنه‌ای افشا کرد مجتبی از استعفا های پیاپی پزشکیان خسته شده بشدت و در صورت تکرار اونو برکنار میکنه.
این اظهارات نشون میده جنگ قدرت بی سابقه توی باند های مختلف سیاسی امنیتی رژیم بالا گرفته.
بحران بدجور یقه جمهوری اسلامی رو گرفته.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69523" target="_blank">📅 16:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69522">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/800e043d01.mp4?token=oc1-qPrYwFQCcjt-6m457Att9JtNEnI5CugzalTly62uF5s3lSgaduME0AmyslxtFir08ZXV2G3sjTi146uSMPk8s9WQdTJIbaqFkILDZev-TUkJZt4uzlZvN9SvjdDaFdmXv8mHdIGJU3i56Dl-s41-Y42pw4v2IExW0V4dgzHkdjdiRXL0CULa43fCR9poPNhT--OysjxI1rx88JfxfVQUKwNiPTDLb-pXTrILHUiRiZEMYT2MvMtLndp_v1hT_9he81VEXlfzeo2etevYeEnRfvBpsyo4oEm5r1k9clfk6ZoLHBTyaL30k5vy5l884CxmWSc6i7C9kZo8zel3Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/800e043d01.mp4?token=oc1-qPrYwFQCcjt-6m457Att9JtNEnI5CugzalTly62uF5s3lSgaduME0AmyslxtFir08ZXV2G3sjTi146uSMPk8s9WQdTJIbaqFkILDZev-TUkJZt4uzlZvN9SvjdDaFdmXv8mHdIGJU3i56Dl-s41-Y42pw4v2IExW0V4dgzHkdjdiRXL0CULa43fCR9poPNhT--OysjxI1rx88JfxfVQUKwNiPTDLb-pXTrILHUiRiZEMYT2MvMtLndp_v1hT_9he81VEXlfzeo2etevYeEnRfvBpsyo4oEm5r1k9clfk6ZoLHBTyaL30k5vy5l884CxmWSc6i7C9kZo8zel3Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
محمدباقر خرازی درباره بمب اتم:
«در اقیانوس اطلس بمب بزنیم و سونامی ایجاد کنیم که موجش به سواحل آمریکا برسه!
تنها راه حل نجات ما ساخت بمب اتم و شلیک آن است!
«با اطلاع»! میگم ایناهایی که با بمب اتم مخالفت کردن اون دنیا در عذابند»
وقتی ازش پرسیدن که حاجی زاده گفته ما بهتر از بمب اتم رو داریم گفت: «جدی نگیرید این حرفها را»
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69522" target="_blank">📅 15:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69521">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQ745p03YLyRQx0bV4r7inUgSUyzMW6QpwjFqCZh9Vb4f5ov-mA4GKHco83BriFhkngvitUu--sps8riQR1x0Ose0iz9M1LkSIN5vwS9iw1SH7Oj-stN7GpXvxJM3pubsu76hCnzz_dBK-wyk4ONIeRKfgw1krL0eqmodqm_zfB-m0-ny6qsvEqmUo_2kkJoU2HD_N9uHEAr1fFvzS3r-B3u6XE0hMWJTeKHmCBUBNaKjVrOCl2v6p_MN9_zyDDEp2G2J569vg-4HHL8aIiaLx2kW1DSrBPCc12PcfaYLC4-VAnTdTasHxBEnq435Ud-A8FkHbul4F9MiJ1P6GUVpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
بلومبرگ:
ترامپ به ایران مهلت داده است تا سه‌شنبه با عمان در مورد تنگه هرمز به توافق برسد، در غیر این صورت با حملات هوایی ویرانگر به این کشور روبرو خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69521" target="_blank">📅 14:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69520">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🇺🇸
🇶🇦
🇮🇷
سخنگوی وزارت خارجه قطر:
تلاش‌ها برای دستیابی به یک راه‌حل کوتاه‌مدت میان ایالات متحده و ایران در جریان است و متن توافق احتمالی نیز تدوین شده است.
این پیش‌نویس هم‌اکنون میان طرفین در حال تبادل و بررسی است، اما هنوز دستور کار مشخصی برای مذاکرات مستقیم میان آمریکا و ایران تعیین نشده است.
تمرکز دیپلماتیکِ فوری، حل‌وفصل تمام اختلافات عمده نیست، بلکه هدف، دستیابی به کاهش تنش در کوتاه‌مدت است که بتواند راه را برای ازسرگیری مذاکرات هموار سازد.
برای بازارها، این تحول سیگنالی مثبت محسوب می‌شود؛ چرا که هرگونه توافقی می‌تواند خطر تشدید درگیری‌های نظامی را کاهش دهد، از تنش‌ها در تنگه هرمز بکاهد و فشار بر بازار نفت را تعدیل کند.
با این حال، همچنان باید جانب احتیاط را رعایت کرد: اگرچه پیش‌نویسی وجود دارد، اما هنوز مشخص نیست که آیا واشنگتن و تهران هر دو آن را خواهند پذیرفت یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69520" target="_blank">📅 14:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69519">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TU5QJD5wD0PWhXrTvLO75t55V038sAc5ThvQtDLaLrVhSRHaar9qUMB9OtPxo2Ehq0goy-fh1CJnQkLJqRirRHricTyBgC-ELM51gGs0ASt4SoA7UO0HKir6ans-xqdBsJ0nwp4AM2NHYZgv-jPh7ktAgbr3l4Ddr2eOqC9xGIzgRB-soIvituGUGlUtXKsb_imydEeYFkHMrMefn7W0DAhatiTLzmEq3TAltfjkPMiOdTRUnyOHoHH0YKGFdq_14uwJZXL0pyS3cGZGGOA2tb1Jn7om6K82xffcu2OjECj4X2RV-dZtBksJs_q82i4NukPPdv7koa_LXOOMx6SHgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
هیئت مدیره شهرک صنعتی شمس آباد:
دقایقی پیش یه مخزن گاز توی یه کارخونه منفجر شد و باعث صدای انفجار، دود و آتش سوزی شد.
هیچ حمله‌ای صورت نگرفته و مردم نگران نباشن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69519" target="_blank">📅 13:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69518">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8fbdc7b7.mp4?token=LsR6o8zFBh9Mj6mycV8E2qv91iokVyM1WNQoWUsQVrCd97HxRK-ZLSPE1InD4nAWMXbsQKr1k2k_0uQyzh0MohZQ3Dp-YOBQldNh31jiTyZSi-VQhymW1DFYU14-NByTccLNp_w4z4-WM-fmsY65T5V8xnlkOKXakjg49ge75C-HSZGOWPlK6lPF1XNI0Om7yzHPLfkJ0bawfMBfArN-BXrbh9mT1LJTH4Ttl0VuS_E1OgoyIBGK0bCpdzrGveSJfotHrf1wYMvM9XGPVaWxRFsRqnZgxQOi7yqsffaQh7hSTs-ZssMMnLZ7WMxDzBDO-C06zfRwDgm4FpOG-BK4VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8fbdc7b7.mp4?token=LsR6o8zFBh9Mj6mycV8E2qv91iokVyM1WNQoWUsQVrCd97HxRK-ZLSPE1InD4nAWMXbsQKr1k2k_0uQyzh0MohZQ3Dp-YOBQldNh31jiTyZSi-VQhymW1DFYU14-NByTccLNp_w4z4-WM-fmsY65T5V8xnlkOKXakjg49ge75C-HSZGOWPlK6lPF1XNI0Om7yzHPLfkJ0bawfMBfArN-BXrbh9mT1LJTH4Ttl0VuS_E1OgoyIBGK0bCpdzrGveSJfotHrf1wYMvM9XGPVaWxRFsRqnZgxQOi7yqsffaQh7hSTs-ZssMMnLZ7WMxDzBDO-C06zfRwDgm4FpOG-BK4VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
تهران
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69518" target="_blank">📅 13:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69517">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⏺
یک مقام ارشد ایرانی به رویترز:
طرح پیشنهادی تهران به عمان در خصوص تنگه هرمز، اختیار کامل بر تمامی تردد دریایی ورودی را به ایران واگذار می‌کند.
علاوه بر این، بر اساس سازوکار پیشنهادی، عمان تنها پس از اطلاع‌رسانی به مقامات ایرانی اجازه عبور به کشتی‌های خروجی را خواهد داد؛ امری که تضمین می‌کند تهران همچنان بر وضعیت نظارت داشته و امکان مداخله را حفظ کند.
این مقام ارشد اظهار داشت که بعید است ایران جایگزینی برای این توافق جهت بازگشایی تنگه هرمز را بپذیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69517" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69516">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KabYz5DX7SJ09YyAxE8128lsDSnRO2fJDAYnitDvObZbz3GH5WmrM2-ypyTXdZLG3v8ybz3DJTf8EK3gzW59ypldIm0K0WknkonCZKbNWvRfOj1uT_U0wpOVGleat1mqiJqPj7YuyrPANOu56Lr3LvOIO-7ewc9Lg4k6QEsevxSqVHnYPs0wVyRgcp8Wup1Y641t4naX6Hzg8u_3bv6tSGPTpmOHygvfMFkbto9hTj_8RN2GUAjGdg6rrFw47x2ExP5ebYMUvR5GaSkAWbux5tDGiTxNmFByJ96gbQ7qndhRiqg1UHd0WQIBwyts6VVplTxboGchnmYcaAHi9Aie5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69516" target="_blank">📅 13:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69512">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lc4m0Qmher6SKw9UVIbhkoFWL3fZvfTCNL_yx2Us_EV7DPH5WnvZL5EG3NL3gcqpy2GZ7UygQ7KeTkS21he5eK08tZIUdBgsUhFYqjQIJfLmSMZTnsVSeVBQyPMXoa_uUy-dk2DJa6ljr_QR6KFqfbLF0rW-jDolU9nr7_mjTeV8giXExDmcMBAsdDoxKKwgXzLbK2aTCnDPAwkVIAuu4bCXfxfSxutTtY1dZhvFz354sd150CGejdsP17dYczIKPecHbyQ9i66JEmFsChfdOyMNhnuadp63OzTgnInwrADw2mKsShqdDJbJjp2KdW0vrqxqh1JC1qDs7g3r8lpfGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gtp-IzxURu51q4CHW6GOzXpm5sWCWrjE9qCUfW-rKg5MWDuw1W1Jw9CHlCdFeUmxNG7QPFVTAaCP2jVVzKhXbvt_kRtEyQs0JLYd215EP4PF2c3GfWfdIR4rT-voNkFE-w-v8d_8b3HfjCUwOB2NnZJF9k1d4JmLnDCAT5JRKW-bBIL0qVLOak5SyF0tuF9lgSbynVhAikvkZWBXKX1LL_0gwHgOwTUghem151ak2-nN3_7e4Cf0U489lQqc25OEOF2kD5gX2BKh4cDnSJxErVNwCZksKPcLo3xoqzEMd8kqvgddJq2NPTTULcR5EtrLP-g4blR29G_rZm-MlamsAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/snGzAw5Ooeb6recSJlNt6wb2lx4_r-n3Wuf-kAWsY_3ubBQzUctXJk5XOqXcAI8fuShzkIO17_C92OVfMW1aYyPxxApJ6vAh8Kcm0JkbXeL-0UjxgRLpRHDAQGLPihVk_HH3E0bg9tI2ibnP18XgPUA1ZJuhHRaGlD_wHR19qML6LGFg0ORvyTJeHve4ClD29UCtMerMypZstSftOr8R5PigpnwZs_FEBfrg4jpNAHFE6XCW5e7-tmi7K8YqlC0oi09LBQxKHSJrdhx8uBDNk_hI-po6r0rG0XETBPzTaOUMNs_FLukzDpVR4bZUpIPmoP91voEzIEfJxYGE3Ib_6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y7RxucC_Q7aoQ1zkZnJA-agieTpj3LheNdzGALapnEMx0q9l5Omb1gjG5z0vrDP--B-zp1ByhXmJ9MwbQnJVC2tTAKh6WM4mrF81eZg30zX6YvesYc8toBtkKDDjYkPZdO2P8WDZeIbi1wJj4pFlVIdg3Y4tk0MMtN3LT9JATmkYyE1KVpF7NK2x7zooHmKXlHSRyHqTxj3x0MVkm7nNO7kh_eVDAk65XHogrAcaxa1KQTmqCgh8HjLvjAx3DHrQp7GJ8XYKW-Wu2BG8tFjeogguI_N86TI7sGSdz1KIdqVfVo_a0ySlG9A7k-Raih90Kl1hvmCV5hd-833kjNZsiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
شهرک صنعتی شمس‌آباد
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69512" target="_blank">📅 13:21 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
