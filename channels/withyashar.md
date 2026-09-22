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
<img src="https://cdn4.telesco.pe/file/T1l153eRC7HUg4l-nE7IVlI36daV8HIJJOlY5_hlO8aQJs47VmMpbPKt2J0viwLWtRFy5cOe-pGz6zbby0qgiig468RKeNLHjdQc4kI8nQWpPmRMO2wZ6xd2K6dwoRbWuQnIoLtdhrREDrVqz3dP0AKawDnQCtd145smfL632J4ludbtgUrnnQJ3zlxZzfkEtwnGlGBNE35Q615Vp23YVJ8cabR4GSgDdjY_WgOgDY_gx9b0JvAFTZDnBYxK6Sda8bp-_dS0yaEI63A-4KycdYsAgQTcyhk3pO5X4ZUk_gHUfHBbEBusc_uwLe-Jd8qynQLv1viLlPzF5_cvQbU7gA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 454K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 18:34:28</div>
<hr>

<div class="tg-post" id="msg-23814">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce094c02c0.mp4?token=tnmX9MyJRQ_BkzLMsPxfuw8iMd7Qu6roBPkwQeRxL0KDkehuf9L5sIBmDMRqgzDoo6yhc9wqO6bzuHskiKCx-lhudiAJrfACUFzuvWdglas7VrUVRbNdLiiVJqq1mJNL5iFakTGFSMI9GLDAfBBGF5Znse5UScWo_0od9d0BgsfS17zV_4E9Aa5WlWMw29nKDD_Rr8SOVfYnBYcN-qP_rdZ7rgsnhmDdTtJKHEJvrHeN0AbMawPglQAP-OB_dVN1qGgFrQU3boQl73TvaIEpQS11OWuAzqWlK7ZUoyZ2zHpehj1pbAJtyYqsfTS2mnlgJDIdTLQLz1acSyepB3lE2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce094c02c0.mp4?token=tnmX9MyJRQ_BkzLMsPxfuw8iMd7Qu6roBPkwQeRxL0KDkehuf9L5sIBmDMRqgzDoo6yhc9wqO6bzuHskiKCx-lhudiAJrfACUFzuvWdglas7VrUVRbNdLiiVJqq1mJNL5iFakTGFSMI9GLDAfBBGF5Znse5UScWo_0od9d0BgsfS17zV_4E9Aa5WlWMw29nKDD_Rr8SOVfYnBYcN-qP_rdZ7rgsnhmDdTtJKHEJvrHeN0AbMawPglQAP-OB_dVN1qGgFrQU3boQl73TvaIEpQS11OWuAzqWlK7ZUoyZ2zHpehj1pbAJtyYqsfTS2mnlgJDIdTLQLz1acSyepB3lE2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: آمریکا و ایران قطعاً به نتیجه خواهند رسید؛ به هر طریقی که باشد
دونالد ترامپ درباره ایران گفت: «آمریکا و ایران قطعاً این مسئله را حل خواهند کرد؛ به هر طریقی که باشد، این کار انجام خواهد شد.»
او افزود: «این اتفاق سریع رخ خواهد داد.»
@WarRoom</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/withyashar/23814" target="_blank">📅 18:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23813">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ: جنگ اوکراین زودتر از آنچه مردم تصور می‌کنند پایان خواهد یافت
دونالد ترامپ درباره جنگ اوکراین گفت: «ما همکاری بسیار نزدیکی با رهبران روسیه و اوکراین داریم و این مسئله را حل خواهیم کرد.»
او افزود: «فکر می‌کنم این اتفاق سریع‌تر از آنچه مردم تصور می‌کنند رخ خواهد داد؛ آن‌ها دیگر از این جنگ خسته شده‌اند.»
@WarRoom</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/withyashar/23813" target="_blank">📅 18:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23812">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ: بزدلان و خائنان دوست دارند بگویند ایالات متحده با کمبود مهمات مواجه است، اما چنین چیزی درست نیست.
ما بیش از آن مقدار مهماتی داریم که حتی بتوانیم تصور کنیم ممکن است از آن استفاده کنیم و در حال تولید مهمات با سطوحی هستیم که هرگز پیش از این تجربه نکرده‌ایم. ما ذخایر خود را سریع‌تر از هر زمان دیگری افزایش می‌دهیم؛ مهمات و تجهیزات درجه‌یک.
علاوه بر این، در آینده‌ای بسیار نزدیک، کارخانه‌های عظیم تولید مهمات افتتاح خواهند شد. در حال حاضر ۱۸ کارخانه توسط بزرگ‌ترین شرکت‌های صنایع دفاعی جهان در حال ساخت است؛ ۱۸ کارخانه در دست احداث است.
@WarRoom</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/withyashar/23812" target="_blank">📅 18:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23811">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ: ایران ۷۲هزار شهروند معترض بی گناه خود را به قتل رسانده است @WarRoom</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/withyashar/23811" target="_blank">📅 18:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23810">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc729c6f5e.mp4?token=Ca_upG2AZrh3hT0uk5vrZWMrwAm8RyM1roL5Wv3eTPFY8MeSZahunlzWI-2Bqje-vBdpUXET3r36pAKfAmL_E0bIPvOFzPPqfIapEQayo2LpVKYPXEKQlZ2wncDmDahy9c75qxgmDUwPZIiQ2Ik7v10mkbcnYKYf7AU3BznM0aHK-l8hEJVNkWatAUOkMOrO814b28bafC8gMM-B-n7J0BpTWxYdN44KeaoPwTGWlzgQ7bgoU6ThBvjUiKfhE4RO9y3pxq8bATYBhlgbqB6JN3DvO7cgjWG0EIeWYouU6spHDaKsVOJUwcyVRwmBhVJNc8PuicLRGtZ4yi3I0VErPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc729c6f5e.mp4?token=Ca_upG2AZrh3hT0uk5vrZWMrwAm8RyM1roL5Wv3eTPFY8MeSZahunlzWI-2Bqje-vBdpUXET3r36pAKfAmL_E0bIPvOFzPPqfIapEQayo2LpVKYPXEKQlZ2wncDmDahy9c75qxgmDUwPZIiQ2Ik7v10mkbcnYKYf7AU3BznM0aHK-l8hEJVNkWatAUOkMOrO814b28bafC8gMM-B-n7J0BpTWxYdN44KeaoPwTGWlzgQ7bgoU6ThBvjUiKfhE4RO9y3pxq8bATYBhlgbqB6JN3DvO7cgjWG0EIeWYouU6spHDaKsVOJUwcyVRwmBhVJNc8PuicLRGtZ4yi3I0VErPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ایران ۷۲هزار شهروند معترض بی گناه خود را به قتل رسانده است
@WarRoom</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/withyashar/23810" target="_blank">📅 18:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23809">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ: به ایران در ازای پایان برنامه هسته‌ای و حمایت از تروریسم، همکاری کامل اقتصادی پیشنهاد دادم؛ اما نپذیرفتند
دونالد ترامپ درباره ایران گفت: «پس از آغاز به کارم در سال گذشته، مذاکرات با ایران را آغاز کردم و در ازای پایان دادن به برنامه هسته‌ای و حمایت از تروریسم، همکاری کامل اقتصادی را به آن‌ها پیشنهاد دادم.»
او افزود: «اما آن‌ها این پیشنهاد را رد کردند؛ این یک اشتباه بزرگ بود.»
@WarRoom</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/withyashar/23809" target="_blank">📅 18:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23808">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ: ایران دیگر قلدر خاورمیانه نیست؛ هرگز اجازه دستیابی به سلاح هسته‌ای را نخواهم داد «آن‌ها قلدر خاورمیانه بودند، اما دیگر قلدر نیستند.» او افزود: «از نخستین روزی که وارد عرصه سیاست شدم، موضع من تغییر نکرده است؛ هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/withyashar/23808" target="_blank">📅 18:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23807">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd7a774734.mp4?token=LcygkMkjcALHy1x571aXIiX0aouewzryndaDfn3DebYUrbHoJ_pRzhJbCLIXDgQcvNns_CstBLbrdVC2doBC-_ER6LrFqi70o1tJo4QveO_dyoV1pYuwpI_sLlu7Z326DjDxFXVzPNAcjuDor_it_fMizqlRoXI8O4oXOSehNWxKvA4SuMI5VMbg9Eh6pU5tP2VOrB-MCoOQ4tZq6NGj9mlL8J1BZhvvEaQ-F0zZYLgxsmiWxFYgR0HjbhlCcuuG5cD02D8WqXBN5J7QLJwZ3FAuX9HtuyVkPYXNcIRP4w_79Ph88pKPoBZp0I8jv5P5-Gz-vL19-GJ28zq4oylfnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd7a774734.mp4?token=LcygkMkjcALHy1x571aXIiX0aouewzryndaDfn3DebYUrbHoJ_pRzhJbCLIXDgQcvNns_CstBLbrdVC2doBC-_ER6LrFqi70o1tJo4QveO_dyoV1pYuwpI_sLlu7Z326DjDxFXVzPNAcjuDor_it_fMizqlRoXI8O4oXOSehNWxKvA4SuMI5VMbg9Eh6pU5tP2VOrB-MCoOQ4tZq6NGj9mlL8J1BZhvvEaQ-F0zZYLgxsmiWxFYgR0HjbhlCcuuG5cD02D8WqXBN5J7QLJwZ3FAuX9HtuyVkPYXNcIRP4w_79Ph88pKPoBZp0I8jv5P5-Gz-vL19-GJ28zq4oylfnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ایران دیگر قلدر خاورمیانه نیست؛ هرگز اجازه دستیابی به سلاح هسته‌ای را نخواهم داد
«آن‌ها قلدر خاورمیانه بودند، اما دیگر قلدر نیستند.»
او افزود: «از نخستین روزی که وارد عرصه سیاست شدم، موضع من تغییر نکرده است؛ هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای دست پیدا کند.»
@WarRoom</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/withyashar/23807" target="_blank">📅 18:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23806">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac051de59.mp4?token=c_7f-f13H8p5J0zLSoIvfydA3vSsRdfZyb9L9dSWoreW-GHYOpUuH-Qui-nejHlmXk_DFWoGyZdQPZH7JyAxQmtNsvQ9ozppn-ntCNLPGf5mZ4UGZ6L10fpeOy7mqtl1qPEn-HpTQ0e2v111BneGBSrUbsQQKpGEcElqHNn3gU9Gduz-1MEX9GEZ9wFJkHs4hE3XUBm-6ROXCCEC7PfMN403-vU6g3DtdYmk3AiUrnoNwknlCAR6LlW3147AcngQe6lfdbEf8_INcIOH2DdfAybNbTg1PMBsm6SMczAAQTCR59sAWeniBDjX8_Gtgq7GaPNwyoPCyHQa5u_AG0cHGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac051de59.mp4?token=c_7f-f13H8p5J0zLSoIvfydA3vSsRdfZyb9L9dSWoreW-GHYOpUuH-Qui-nejHlmXk_DFWoGyZdQPZH7JyAxQmtNsvQ9ozppn-ntCNLPGf5mZ4UGZ6L10fpeOy7mqtl1qPEn-HpTQ0e2v111BneGBSrUbsQQKpGEcElqHNn3gU9Gduz-1MEX9GEZ9wFJkHs4hE3XUBm-6ROXCCEC7PfMN403-vU6g3DtdYmk3AiUrnoNwknlCAR6LlW3147AcngQe6lfdbEf8_INcIOH2DdfAybNbTg1PMBsm6SMczAAQTCR59sAWeniBDjX8_Gtgq7GaPNwyoPCyHQa5u_AG0cHGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«با افتخار می‌توانم به شما بگویم که
آمریکا بازگشته است
و کشور ما امروز از همیشه قدرتمندتر است. اقتصاد ما مورد حسادت جهان است.
ارتش ما قدرتمندترین ارتش روی زمین است.
فناوری ما رقیبی ندارد و ما تقریباً در همه زمینه‌ها
پیشتاز هستیم
.»
@WarRoom</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/withyashar/23806" target="_blank">📅 18:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23805">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">شاهزاده رضا پهلوی برای سخنرانی در نشست سالانه کنکوردیا و دیدار خصوصی با نمایندگان دیپلماتیک کشورهای حاضر در مجمع عمومی سازمان ملل متحد، وارد نیویورک شد.
@WarRoom</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/withyashar/23805" target="_blank">📅 17:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23804">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تلگراف : ترامپ در حال بررسی گزینه‌های مختلف درباره ایرانه؛ از مذاکره و  تشدید حملات و افزایش فشار اقتصادی گرفته تا حتی «منفجر کردن کل حاکمان ایران»!
@WarRoom</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/withyashar/23804" target="_blank">📅 17:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23803">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">با پشتیبانی هواپیماهای سوخت‌رسان BORA74، BORA84 و BORA94، مجموعاً ۱۲ فروند جنگنده F-16C از بال ۱۳۸ جنگنده (138th Fighter Wing) با کد دم «OK»، امروز پایگاه هوایی اشپانگدالم (ETAD) در آلمان را ترک کردند و به سمت خاورمیانه حرکت کردند. @WarRoom</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/withyashar/23803" target="_blank">📅 17:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23802">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
چند کشور که در تلاش برای میانجی‌گری میان آمریکا و ایران هستند، با هر دو طرف در تماس‌اند تا
یک دیدار در سطح بالا بین آمریکا و ایران
برگزار شود. این کشورها هنوز معرفی نشده‌اند و جزئیات بیشتری درباره این دیدار احتمالی منتشر نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/withyashar/23802" target="_blank">📅 17:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23801">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">کانال ۱۴ اسرائیل : پیش از سخنرانی رئیس‌جمهور ایران در سازمان ملل، کانال‌های رسانه‌ای سپاه پاسداران ویدئویی مفهومی و ساخته‌شده با هوش مصنوعی منتشر کردند که تصویری از نخستین آزمایش بمب هسته‌ای «واقعیه گرم» ایران را به نمایش می‌گذارد. @WarRoom</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/withyashar/23801" target="_blank">📅 17:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23800">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">هم اکنون پس از شرکتهای ترکیه و عراق، شرکت های هواپیمایی امارات و قطر نیز پرواز های خود به ایران را متوقف کردند. @WarRoom</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/withyashar/23800" target="_blank">📅 17:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23799">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رسانه های رژیم : «رئیس‌جمهور پزشکیان دقایقی پیش، پس از توقفی کوتاه خود ، الجزایر را به مقصد نیویورک ترک کرد.»
@WarRoom</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/withyashar/23799" target="_blank">📅 17:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23798">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">رئیس‌جمهور ترامپ هنگام ورود به مقر سازمان ملل:تعجب می‌کنم که سی‌ان‌ان اینجا حضور دارد و اخبار مربوط به مرا پوشش می‌دهد. شما نباید اینجا باشید. شما گفته بودید که قرار نیست اخبار مرا پوشش دهید. نباید مشغول پوشش دادن اخبار من باشید. @WarRoom</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/withyashar/23798" target="_blank">📅 17:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23797">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">هم اکنون پس از شرکتهای ترکیه و عراق، شرکت های هواپیمایی امارات و قطر نیز پرواز های خود به ایران را متوقف کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/withyashar/23797" target="_blank">📅 17:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23796">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/066e31f4eb.mp4?token=O9pbvJuUQSnYQ7IA7lsAY0N6XISHA93HSGLaG0aEE-xCLVM1CTHzHx1dxwLWpd6gvsao9ikOo4KngfiksZ68uGxkgPaK0Wvy_SDv6nh9EOZxo3xaBa7A613plcCLnCy-20xtwuHx5tYAPbv4ty2ysC71IGVDDU4X4qA9WwHjcXfsSn5tq9JDr3Bqc_5CY_NHLf4Rj527CODZjPsfLVAv_tcShsOrKBgrC2qHN38EobjYJXEQnX9ko8yk-kLNGSsJhDAOVB75OTIs9Hv9Nhs8wXfe_PAWbjf1LektbpRhud-oIKew7k0_CMgP7HDHjw0rk3NnaaRr-qjD78LcxB716g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/066e31f4eb.mp4?token=O9pbvJuUQSnYQ7IA7lsAY0N6XISHA93HSGLaG0aEE-xCLVM1CTHzHx1dxwLWpd6gvsao9ikOo4KngfiksZ68uGxkgPaK0Wvy_SDv6nh9EOZxo3xaBa7A613plcCLnCy-20xtwuHx5tYAPbv4ty2ysC71IGVDDU4X4qA9WwHjcXfsSn5tq9JDr3Bqc_5CY_NHLf4Rj527CODZjPsfLVAv_tcShsOrKBgrC2qHN38EobjYJXEQnX9ko8yk-kLNGSsJhDAOVB75OTIs9Hv9Nhs8wXfe_PAWbjf1LektbpRhud-oIKew7k0_CMgP7HDHjw0rk3NnaaRr-qjD78LcxB716g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ترامپ هنگام ورود به مقر سازمان ملل:تعجب می‌کنم که سی‌ان‌ان اینجا حضور دارد و اخبار مربوط به مرا پوشش می‌دهد. شما نباید اینجا باشید.
شما گفته بودید که قرار نیست اخبار مرا پوشش دهید. نباید مشغول پوشش دادن اخبار من باشید.
@WarRoom</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/withyashar/23796" target="_blank">📅 17:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23795">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تنگه صدای سلامی میاد
@WarRoom</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/withyashar/23795" target="_blank">📅 17:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23794">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0Z_LPxkANso4L9RxNUGqrVv7SRezbuHt6ECci9fBlWZfwHGAT7DeFM6yhFdL36i4xbL8WoWqTrUCE8f0AgfEoyr4Dpb8hZ0tLUcHTPqVVVSzauZGG09B9ryxw33IdWnce1d3J-utWeTR1Nozk0jqjVBWZKyM33SM94KvZMdjesbG6ND4q1TiNQAh5WE0G5EJJn-CnfZhK4lBfljV4moH1dpoCIYHduFMk7YY7gFVxdNoO6KrCCvU9d_4Nyk0Nd16V99HypWsDDLMEPbVe53rs7alRTUNMVt9bxrB4VAGK9xD_gPySQPMuOkb6G8s5UbDg4LlDRyhXZY0EVJ-5ui8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">​ جدول سخنرانیهای سازمان ملل مشخص شد
بر اساس جدول رسمی منتشرشده از سوی مجمع عمومی سازمان ملل متحد (نشست هشتاد و یکم)، دونالد ترامپ امروز به عنوان دومین سخنران در صحن مجمع عمومی حاضر خواهد شد.
پس از گزارش دبیرکل و سخنرانی رئیس مجمع و رئیس‌جمهور برزیل، نوبت به رئیس‌جمهور آمریکا می‌رسد.
زمان تقریبی سخنرانی ترامپ:
به وقت تهران: حدود ساعت ۱۷:۱۵ الی ۱۷:۴۵
@WarRoom</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/withyashar/23794" target="_blank">📅 17:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23793">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">عراقچی‌ هم وارد سالن شد تا سخنان ترامپ را بشنود
@WarRoom</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/withyashar/23793" target="_blank">📅 17:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23792">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ وارد سازمان ملل شد
@WarRoom</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/withyashar/23792" target="_blank">📅 17:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23791">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">با پشتیبانی هواپیماهای سوخت‌رسان BORA74، BORA84 و BORA94، مجموعاً ۱۲ فروند جنگنده F-16C از بال ۱۳۸ جنگنده (138th Fighter Wing) با کد دم «OK»، امروز پایگاه هوایی اشپانگدالم (ETAD) در آلمان را ترک کردند و به سمت خاورمیانه حرکت کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/23791" target="_blank">📅 16:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23790">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تنگه دعوا شد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/23790" target="_blank">📅 16:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23789">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه ایران، از وزارت امور خارجه آمریکا درخواست کرد تا در جریان حضورش در نیویورک برای شرکت در مجمع عمومی سازمان ملل، یک تیم حفاظت امنیتی آمریکایی در اختیار او قرار گیرد. بر اساس گزارش‌های رسیده از آمریکا، پس از بررسی تهدیدهای موجود علیه وی، تیمی از «سرویس امنیت دیپلماتیک» مسئولیت حفاظت از او را بر عهده خواهد گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/23789" target="_blank">📅 15:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23788">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe43fd0fd0.mp4?token=ZmOwLllFHXq_i9AoUy9uzKRb8WywTcBTF3eyUH8fEaKrY-BOi7FmOzrZNap322ZgVTpcVOYmxApI9-htY5Lfwh3W4yfO5XfzAvb0TU9FXiiw9sGXBoBZyPBUAHoAcCM80G5Zk_hldN8dEvB3KEVg2ze6iLyI2sdD_BmPZ5jklhMvG3gOI_Xnx06ynvGIf9lb5XERRwuUtLdiPznq_klp9EzaRV0MzvjDyv4u88NkC4NB7b-2GQMEgbH9aH_3sIJ6wXOl1ZGTehk6-cCr53Nvt-aWNB9JzCUz5F8y-mN8xIN-4rQVgQZAEil6aSXq-nbPuNTQvPwV287t86774y_ZXzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe43fd0fd0.mp4?token=ZmOwLllFHXq_i9AoUy9uzKRb8WywTcBTF3eyUH8fEaKrY-BOi7FmOzrZNap322ZgVTpcVOYmxApI9-htY5Lfwh3W4yfO5XfzAvb0TU9FXiiw9sGXBoBZyPBUAHoAcCM80G5Zk_hldN8dEvB3KEVg2ze6iLyI2sdD_BmPZ5jklhMvG3gOI_Xnx06ynvGIf9lb5XERRwuUtLdiPznq_klp9EzaRV0MzvjDyv4u88NkC4NB7b-2GQMEgbH9aH_3sIJ6wXOl1ZGTehk6-cCr53Nvt-aWNB9JzCUz5F8y-mN8xIN-4rQVgQZAEil6aSXq-nbPuNTQvPwV287t86774y_ZXzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، درباره ایران:
«رئیس‌جمهور ترامپ آماده دیدار با
مسعود پزشکیان یا هر فرد دیگری
است. اما اینکه چنین دیداری به نتیجه‌ای سازنده منجر شود، مشخص نیست؛ زیرا
تصمیم‌گیرنده نهایی در ایران رهبر جمهوری اسلامی است
و رهبر جمهوری اسلامی یک روحانی شیعه رادیکال است.»
@WarRoom</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/23788" target="_blank">📅 15:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23787">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abb2d25d09.mp4?token=FHDWFIugfK4VSbDXx3IBtW8HhSFm2hqcftNGn8Ekgca3T3F0r7w_YDsPBSB0EJLQr8iWVRQU9Tmy-rjKnDqClRAVGS5oRGTodbTmwNU0nx5CVPFfOOrDogeGg-XvyK0H_od5RYoOfREfwkkJSUbJ-6uHmpMKDdBu9KzWzhlddKsoo_TQO01r6i8h83_0yDsuIg--BVRwpYLnUcWYhGs9-TZYJD6yVINiF2sBN_63qwSekrFAxTSV7c241DVi9zzcYtexzEp8FSWEX2slLlmkQoSJv0LUhTh1NybthhsR_qZmFQ3b38eNTQJryx5m1blAqKviHJGuhkRFsWoW47kY2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abb2d25d09.mp4?token=FHDWFIugfK4VSbDXx3IBtW8HhSFm2hqcftNGn8Ekgca3T3F0r7w_YDsPBSB0EJLQr8iWVRQU9Tmy-rjKnDqClRAVGS5oRGTodbTmwNU0nx5CVPFfOOrDogeGg-XvyK0H_od5RYoOfREfwkkJSUbJ-6uHmpMKDdBu9KzWzhlddKsoo_TQO01r6i8h83_0yDsuIg--BVRwpYLnUcWYhGs9-TZYJD6yVINiF2sBN_63qwSekrFAxTSV7c241DVi9zzcYtexzEp8FSWEX2slLlmkQoSJv0LUhTh1NybthhsR_qZmFQ3b38eNTQJryx5m1blAqKviHJGuhkRFsWoW47kY2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، درباره ایران:
«تصور کنید کره شمالی در خاورمیانه شکل بگیرد؛ این برای جهان فاجعه‌بار خواهد بود. در آن صورت، قیمت گازوئیل که امروز مثلاً ۶ دلار است، ممکن بود
سه برابر
شود.»
@WarRoom</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/23787" target="_blank">📅 15:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23786">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2875ab9dd.mp4?token=IyAU8gO7CfI2ZifjkNw-uKwk3cVe0bikB8OvM8ANlHFxgmuSAXmr6OxV65LxGQEUl7ZBKJQCSc-At484VwX43N4YHwJsxk35coHOR5I0avBOIfLXxNMwd8DfBNHBWVjtpwjveIEcjIwVxfkJ0BxjzwOFNbDMuT5otIUcJE9vt-iNnXn9lgA6FpPP1e1eYwrhYMfhiz_0RMT47CghB8C8StwlP7ySI7fG4Rvnjyjm3JfylO5phA2F1v7sTCD75jC0QOZ8BA6nIQ0Hb2QSIq-AoR1kUjTTuTNmaiphE7Ww9Sa7Ukg0A56Ba9QNmWBKC4lr7m88395gtDe4uCg12wj5bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2875ab9dd.mp4?token=IyAU8gO7CfI2ZifjkNw-uKwk3cVe0bikB8OvM8ANlHFxgmuSAXmr6OxV65LxGQEUl7ZBKJQCSc-At484VwX43N4YHwJsxk35coHOR5I0avBOIfLXxNMwd8DfBNHBWVjtpwjveIEcjIwVxfkJ0BxjzwOFNbDMuT5otIUcJE9vt-iNnXn9lgA6FpPP1e1eYwrhYMfhiz_0RMT47CghB8C8StwlP7ySI7fG4Rvnjyjm3JfylO5phA2F1v7sTCD75jC0QOZ8BA6nIQ0Hb2QSIq-AoR1kUjTTuTNmaiphE7Ww9Sa7Ukg0A56Ba9QNmWBKC4lr7m88395gtDe4uCg12wj5bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روبیو: ما برای دیدار با هیئت ایرانی در سازمان ملل آمادگی داریم ولی فکر نمی‌کنم هیچ جلسه‌ای بین ترامپ و رئیس‌جمهور ایران برنامه‌ریزی شده باشد @WarRoom</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/23786" target="_blank">📅 15:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23785">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4ca3ee788.mp4?token=fCRL1OnNjNwpIXAyBrYBLwzzZAuHPR0EV0F5d1Ncp0IciUAFEztiB43Cj1OfNRCb9gY16hw09jtTcuBRqGkRt0FzeNaYf43qXDzQrUnu7uqsJEFtvlkJKmFysLxmCsG9HC5qng45hRWHUpHTD8V1bIRlEOgQK04rMmVIf5lLjVmpOk7qQHakUFfmtKYCYUQqk5QZ4Cbilnh1VQz9A2aTgA2BzCRWo2FP2DK4HxmrbA1V-LOK7d3qvvz43VT_u1xoKBDD9KdRaq4uPpmqjnF8HunySwDhYtDbstXKrP2xYYKpCosXDjfwocmYEFl58OMs6jh6gJBcVgqlZYDgnfVKUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4ca3ee788.mp4?token=fCRL1OnNjNwpIXAyBrYBLwzzZAuHPR0EV0F5d1Ncp0IciUAFEztiB43Cj1OfNRCb9gY16hw09jtTcuBRqGkRt0FzeNaYf43qXDzQrUnu7uqsJEFtvlkJKmFysLxmCsG9HC5qng45hRWHUpHTD8V1bIRlEOgQK04rMmVIf5lLjVmpOk7qQHakUFfmtKYCYUQqk5QZ4Cbilnh1VQz9A2aTgA2BzCRWo2FP2DK4HxmrbA1V-LOK7d3qvvz43VT_u1xoKBDD9KdRaq4uPpmqjnF8HunySwDhYtDbstXKrP2xYYKpCosXDjfwocmYEFl58OMs6jh6gJBcVgqlZYDgnfVKUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل
، در واکنش به اظهارات
زهران ممدانی، شهردار نیویورک
، که او را «
جنایتکار جنگی
» و «معمار
نسل‌کشی هولناک مردم فلسطین
» خوانده و گفته بود حکم بازداشت صادرشده از سوی
دادگاه کیفری بین‌المللی (ICC)
علیه نتانیاهو باید اجرا شود، گفت:«
شرم بر شما، آقای ممدانی.
شرم بر شما که از
هیولاهای تروریست حماس
که مردم ما را قتل‌عام کردند حمایت می‌کنید. شرم بر شما که به
اغتشاشات علیه یهودیان نیویورک
دامن می‌زنید. من به
سازمان ملل
می‌آیم. می‌خواهم درباره
سربازان قهرمان ما
حقیقت را بگویم و درباره
شما
نیز حقیقت را خواهم گفت.»
@WarRoom</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/23785" target="_blank">📅 15:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23783">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">روبیو: ما برای دیدار با هیئت ایرانی در سازمان ملل آمادگی داریم ولی فکر نمی‌کنم هیچ جلسه‌ای بین ترامپ و رئیس‌جمهور ایران برنامه‌ریزی شده باشد
@WarRoom</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/23783" target="_blank">📅 15:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23782">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ در تروث : بزدلان و خائنان بسیار دوست دارند بگویند که ذخایر مهمات ایالات متحده رو به کاهش است؛ اما این حرف صحت ندارد. ما بیش از هر مقداری که حتی تصور استفاده از آن را داشته باشیم، مهمات در اختیار داریم و هم‌اکنون نیز در حال افزایش تولید آن‌ها به سطوحی بی‌سابقه هستیم.
@WarRoom</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/23782" target="_blank">📅 14:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23781">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">رویترز:
ایران در صورت
کاهش فشار نظامی آمریکا و رفع محاصره بنادر ایران
، آماده است
تنگه هرمز را ظرف ۷ روز بازگشایی کند.
هیئت ایرانی در نیویورک اختیار دارد از طریق میانجی‌ها مذاکرات دیپلماتیک را از سر بگیرد، اما تهران خواستار تعهد واشنگتن به
تعیین یک جدول زمانی برای پایان درگیری‌ها و حل‌وفصل دیپلماتیک بحران
است. یک مقام ایرانی گفت: «آمریکا باید اعلام و رسماً تأکید کند که می‌خواهد موضوع را از طریق دیپلماسی حل کند و سپس درباره جدول زمانی روند مذاکرات توافق شود. مجمع عمومی سازمان ملل فرصت طلایی برای بازگشت آمریکا به دیپلماسی است.»
@WarRoom</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/23781" target="_blank">📅 14:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23780">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سخنگوی سپاه پاسداران:
اگر آمریکا به
کوه کلنگ یا هر نقطه دیگری از ایران حمله کند، با آن مقابله خواهیم کرد.
ترامپ پیش‌تر نیز تهدیدهایی مطرح کرده، اما نتوانسته آنها را عملی کند. اگر آمریکا حمله کند،
ایران کاملاً آماده پاسخ است
و تجربه پاسخ‌های قبلی ایران که به گفته او مانع تحقق اهداف آمریکا شده، تکرار خواهد شد. او تأکید کرد:
برای هر سناریویی آماده‌ایم و در هر عرصه‌ای که دشمن وارد شود، پاسخ قاطع خواهیم داد.
@WarRoom</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/23780" target="_blank">📅 14:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23779">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رویترز:
ترافیک کشتی‌ها در
تنگه هرمز به تنها ۲ کشتی تا پایان دیروز دوشنبه
کاهش یافته است؛ این رقم یک روز قبل ۱۰ کشتی بود، در حالی که پیش از جنگ حدود
۱۲۵ کشتی تجاری در روز
از هرمز عبور می‌کردند. رویترز همچنین گزارش داده دو نفتکش در هرمز هدف قرار گرفته‌اند؛ یک نفتکش با پرتابه ناشناس و یک کشتی حامل LPG نیز با بقایای پرتابه ناشناس آسیب دیده‌اند. مسئول حملات هنوز مشخص نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/23779" target="_blank">📅 13:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23778">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d07f32a5.mp4?token=gOG8xxoUgS76GKMj0uP6LZQtoEiXUmntk5QceoSDk_qGnC95k_mvMkdi6agUBjNxLYLq3M_caLvm9Xd3N8TbcQ4fP-wYn_i23pOBq-inipreMd5lMl0UDiAaqmelsoMhMfFw9ggOXyDE2NJ-JDYhn2EF1l1Q9sKliC5u-EIt6j8lQqUCXoDPO-PuV-n1IRFik2mzdig0shQzP4KWIOMlzFJvqSMi78lG7VKWYrxTKp_2fL7UZh18B0Tl9r7kxoELmSxXrIcoVMjKTJlF-4SBcP7lSj4bDNvUwoPBj3KGLKpf7Dbm0_rN5u4FQqGdsc9m5HWHcnB6N3ok869fQ2WURzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d07f32a5.mp4?token=gOG8xxoUgS76GKMj0uP6LZQtoEiXUmntk5QceoSDk_qGnC95k_mvMkdi6agUBjNxLYLq3M_caLvm9Xd3N8TbcQ4fP-wYn_i23pOBq-inipreMd5lMl0UDiAaqmelsoMhMfFw9ggOXyDE2NJ-JDYhn2EF1l1Q9sKliC5u-EIt6j8lQqUCXoDPO-PuV-n1IRFik2mzdig0shQzP4KWIOMlzFJvqSMi78lG7VKWYrxTKp_2fL7UZh18B0Tl9r7kxoELmSxXrIcoVMjKTJlF-4SBcP7lSj4bDNvUwoPBj3KGLKpf7Dbm0_rN5u4FQqGdsc9m5HWHcnB6N3ok869fQ2WURzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل : پیش از سخنرانی رئیس‌جمهور ایران در سازمان ملل، کانال‌های رسانه‌ای سپاه پاسداران ویدئویی مفهومی و ساخته‌شده با هوش مصنوعی منتشر کردند که تصویری از نخستین آزمایش بمب هسته‌ای «واقعیه گرم» ایران را به نمایش می‌گذارد.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23778" target="_blank">📅 13:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23777">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">کیودو نیوز ژاپن به نقل از یک مقام ایرانی:
ایران اعلام کرده در صورتی که آمریکا گام‌هایی برای کاهش فشار نظامی بردارد، تهران می‌تواند
تنگه هرمز را ظرف ۷ روز بازگشایی کند
. به گفته این مقام، این پیشنهاد از طریق میانجی‌ها به آمریکا منتقل شده و ایران خواستار ازسرگیری مذاکرات برای دستیابی به پایان دائمی درگیری‌هاست. این گزارش تاکنون به‌طور مستقل از سوی ایران یا آمریکا تأیید نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/23777" target="_blank">📅 13:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23776">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">وزیر دفاع اسرائیل، یسرائیل کاتس:
«با توجه به برخی نیت‌ها و گزارش‌های اطلاعاتی، به سازمان تروریستی حماس و حامیان آن، از ایران گرفته تا اردوغان، هشدار می‌دهم: اگر حتی یک سرباز یا غیرنظامی اسرائیلی ربوده شود، کل شهر غزه، همراه با خانه‌ها و برج‌های آن که محل فعالیت‌های تروریستی هستند، به سمت جنوب تخلیه خواهد شد و بیش از یک میلیون ساکن آن نیز منتقل خواهند شد. با شهر غزه همان‌گونه برخورد خواهد شد که با رفح، بیت‌حانون و ۷۰ درصد از مناطق غزه برخورد شد، تا زمانی که افراد ربوده‌شده بازگردانده شوند.»
@WarRoom</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/23776" target="_blank">📅 12:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23775">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">@WarRoom
DorDor</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/23775" target="_blank">📅 12:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23774">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23774" target="_blank">📅 12:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23773">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23773" target="_blank">📅 12:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23772">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/st8uf8GJzaFR7u8bNnIYS8YuBKRNIv0wcaVFw_152eFiNNDPob-DwMRLZwyxvcYnglewCNzyJQu9aaCNHvvP7p9xEJNxQAHr3pn3tNryv3SjtVrtFq5jM5uX0dDpZfCfH4fvC8uyrTJC14jY5bteUfvWcHq5Zimwr26QoEptgvKgBZS7ENh2GU8dJwBrU6wCgstRl9h6p8HLLdBDmBiRMgdDOrINIdkG15qmrILlEC7mqWlfFIFWJb6ZxbnuYfD846Pko4eSIhhBQykjnoTpOgJuiS5O6058p_rZVQP6vdE-lW2Lj-ob5t1aX40SWIHIciSzZR_txC1b45qd9pApqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتیجه اخلاقی : تو کار خدا دست نبرید هر چیزی حکمتی دارد
😂
😂
😂
😂
😂
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23772" target="_blank">📅 12:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23771">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">روز گذشته، گوشی یک پاکبان زحمتکش در مشهد به سـرقت رفت و یک هموطن با حضور در منزل این پاکبان، برای او یک گوشی موبایل تهیه کرده و به وی هدیه داد.  @WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/23771" target="_blank">📅 11:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23770">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3d0f93a54.mp4?token=SM2ILR2Kzqn4j52GFTlpjHjDzcbqIKapRhhUKBhAVksmEDVW9bSdIBPgt43DZSeziTDc4tIYgKf1ghCvHh_RQW23o1GYzvZ_s14c7xx_C9BmpGXsm25fScPZ4tpnYAlv1RdDT_VvwP-3jGnihXvKRjArIys33fdeb5Sn1U1mfL-Q2T_Ct262LU7AA1903axoUA3O3tS9ysDQQaoRQuie_wmf3V1yFqQN8Dsy7s8A78v8vNRABqj0PBrVo5jHHqeWAS-RF8p5FVZ6bJCBUIQ3_yhhgcNKfF7yr7lpX2SoldAJViVx0c7WEY8DtZjGOti2OHbauY9jiQW0jGydQcimMDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3d0f93a54.mp4?token=SM2ILR2Kzqn4j52GFTlpjHjDzcbqIKapRhhUKBhAVksmEDVW9bSdIBPgt43DZSeziTDc4tIYgKf1ghCvHh_RQW23o1GYzvZ_s14c7xx_C9BmpGXsm25fScPZ4tpnYAlv1RdDT_VvwP-3jGnihXvKRjArIys33fdeb5Sn1U1mfL-Q2T_Ct262LU7AA1903axoUA3O3tS9ysDQQaoRQuie_wmf3V1yFqQN8Dsy7s8A78v8vNRABqj0PBrVo5jHHqeWAS-RF8p5FVZ6bJCBUIQ3_yhhgcNKfF7yr7lpX2SoldAJViVx0c7WEY8DtZjGOti2OHbauY9jiQW0jGydQcimMDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز گذشته، گوشی یک پاکبان زحمتکش در مشهد به سـرقت رفت
و یک هموطن با حضور در منزل این پاکبان، برای او یک گوشی موبایل تهیه کرده و به وی هدیه داد.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23770" target="_blank">📅 11:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23769">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آسوشیتدپرس:
شی جین‌پینگ در دیدار با ترامپ تلاش خواهد کرد آمریکا را به
توقف فروش تسلیحات به تایوان
متقاعد کند و به توافق مشترک سال ۱۹۸۲ میان واشنگتن و پکن استناد خواهد کرد
، تایوان و ایران
از موضوعات حساس روابط دو کشور هستند , باید دید آمریکا چه درخواستی دارد
@WarRoom</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/23769" target="_blank">📅 11:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23768">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">رویترز: ایالات متحده قصد دارد یک پایگاه نظامی متعلق به دوران جنگ سرد را در منطقه نارزارسوآک در جنوب گرینلند مجدداً احیا کند و همچنین در مسترسویک در سواحل شرقی، یک حضور نظامی جدید ایجاد کند؛ این اقدام در چارچوب توافقی میان آمریکا، دانمارک و گرینلند انجام خواهد…</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/23768" target="_blank">📅 11:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23767">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">رویترز:
گروه هفت از ایران خواست
تسلیح و حمایت از حوثی‌ها را متوقف کند
و حملات حوثی‌ها علیه عربستان و کشتی‌های غیرنظامی را محکوم کرد. G7 از حوثی‌ها نیز خواست حملات و تهدیدهای نظامی را متوقف کرده و به روند سیاسی بازگردند.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23767" target="_blank">📅 11:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23766">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d93d52cd3.mp4?token=UmQcdN6xkd13NBs18XRquh8EcWh8tMz3UIDeAgQhHOeXs_T2JCK_y8XlOqSAse5rpOT_Oh_-BsFXoLwnbFLZ109SVRLUWHXKBt2KjiQ495IPZ_PwH46zyj3AXvC-LZ05FzLSbm_t2TlRsgDMoAp26v7-Ngat31qal1zZyteJ8NnvGG7MlbXun0ELHPHLsrjjIacLWnFJ1f26pI1pcz0CLkAbHHqFt42pHvry7QpE6m5REyC5PFjs4xnEGhtkYcRBnm_fmc3U5fKY8fKH7x_TxUopM4d9F3dS5WcO_e1-eJvXvyp_5Ymk10sygI5jTn1FOEbqNSTvq70CQ_rfWPJwMSzWwITsiRWFKNi0pZarUyUdkOe5G3t_uSxPVHOR3Nsufjypr1QVewEidGJ66mWL8s6Lqt990QdvWQbi0b0jtWLmCu8hc6EkzZsnRpn6LGYW4UAQToCHhat5sPaAiVjIXViR8O8PWc7wBUzKk9eufnZE55SYj9tLqMLZ2VDQEPBneb8ME0WwDr02THbdusY9-SY6PdPnf9umaN6xI8hF9tGO_LOdqh0qNSDBcM5HLrVXCLfZ1ryAOrEMdWwkFptgvRpq9zJzOeSt9sh1U1qkRkgH39XKmrrfHaTIA2yuNkhl1dvX4qySVRf7gN3wCo9s133GDJ5vfOjIEt6QtVgsRUU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d93d52cd3.mp4?token=UmQcdN6xkd13NBs18XRquh8EcWh8tMz3UIDeAgQhHOeXs_T2JCK_y8XlOqSAse5rpOT_Oh_-BsFXoLwnbFLZ109SVRLUWHXKBt2KjiQ495IPZ_PwH46zyj3AXvC-LZ05FzLSbm_t2TlRsgDMoAp26v7-Ngat31qal1zZyteJ8NnvGG7MlbXun0ELHPHLsrjjIacLWnFJ1f26pI1pcz0CLkAbHHqFt42pHvry7QpE6m5REyC5PFjs4xnEGhtkYcRBnm_fmc3U5fKY8fKH7x_TxUopM4d9F3dS5WcO_e1-eJvXvyp_5Ymk10sygI5jTn1FOEbqNSTvq70CQ_rfWPJwMSzWwITsiRWFKNi0pZarUyUdkOe5G3t_uSxPVHOR3Nsufjypr1QVewEidGJ66mWL8s6Lqt990QdvWQbi0b0jtWLmCu8hc6EkzZsnRpn6LGYW4UAQToCHhat5sPaAiVjIXViR8O8PWc7wBUzKk9eufnZE55SYj9tLqMLZ2VDQEPBneb8ME0WwDr02THbdusY9-SY6PdPnf9umaN6xI8hF9tGO_LOdqh0qNSDBcM5HLrVXCLfZ1ryAOrEMdWwkFptgvRpq9zJzOeSt9sh1U1qkRkgH39XKmrrfHaTIA2yuNkhl1dvX4qySVRf7gN3wCo9s133GDJ5vfOjIEt6QtVgsRUU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خزعلی: شاه به قم آمد و به همه آخوندها گفت دوره مُفخوری گذشته است. هزار و چهارصد سال است که فکر شما تکان نخورده
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23766" target="_blank">📅 10:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23765">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1192bf611.mp4?token=qmgejNvprTkpPrSeBwjVnL9LzGjYN41Oe3WVGUQiI9bG9OydnQ14S_JHZwXRD2axTJjLR-ogrmAd-xPSbzfdPNXNpSXSs90JnKz5cIj6wwJr_jIUuE6FKNq14j0ssEF34CdGCvrB7wIGKdFP8aQlallgqq4fskcvUA63bla2mfZuv0uIz4YXuOF8ds4L-bttnY3Vzhe9dSXbJ1x8kNhiPcnnxgX9tmkxp09qxOh6RAm_Ghf19ecaD4gCT82O4t1DnyZlMekKEZ2WNAi1ANGBJbV21I153z6qBaLAxrtWeDdy2x5AyNE-4IufTQOA5YZ9BIYUsubboNm966lco3kcmG9L9hTkJuY54-kqFVkfnkoh6gX4tomZKG_FhlXIOeZLoR8cAePU-XdwyHnIdjCZK1debOQkL1DqUMx9naRTfVuS1sKJ5Nua78gQZ9AXy_3FuRjy-5t280XGSD0HvUxCuO9EsYXfCjdc8tbdJNFQDD8owo_a5zZf3RypZ6cXGTVbpM3EQnnrFZEim7zL-t3rqxGoiSEt9WJ4ij-BvIeLkZwg5hNRJyL_cZ1Wnxqi4F9AeW03DahI5NRkQS7WB7_lQnMJHj3uqduQq0Mb2c1sg0CTHB4pWumWZtya8M-iyVddzP4lP4j7CKTsJ6rNXdF4KK4GsSr7eyNl5vjNvwgiPJ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1192bf611.mp4?token=qmgejNvprTkpPrSeBwjVnL9LzGjYN41Oe3WVGUQiI9bG9OydnQ14S_JHZwXRD2axTJjLR-ogrmAd-xPSbzfdPNXNpSXSs90JnKz5cIj6wwJr_jIUuE6FKNq14j0ssEF34CdGCvrB7wIGKdFP8aQlallgqq4fskcvUA63bla2mfZuv0uIz4YXuOF8ds4L-bttnY3Vzhe9dSXbJ1x8kNhiPcnnxgX9tmkxp09qxOh6RAm_Ghf19ecaD4gCT82O4t1DnyZlMekKEZ2WNAi1ANGBJbV21I153z6qBaLAxrtWeDdy2x5AyNE-4IufTQOA5YZ9BIYUsubboNm966lco3kcmG9L9hTkJuY54-kqFVkfnkoh6gX4tomZKG_FhlXIOeZLoR8cAePU-XdwyHnIdjCZK1debOQkL1DqUMx9naRTfVuS1sKJ5Nua78gQZ9AXy_3FuRjy-5t280XGSD0HvUxCuO9EsYXfCjdc8tbdJNFQDD8owo_a5zZf3RypZ6cXGTVbpM3EQnnrFZEim7zL-t3rqxGoiSEt9WJ4ij-BvIeLkZwg5hNRJyL_cZ1Wnxqi4F9AeW03DahI5NRkQS7WB7_lQnMJHj3uqduQq0Mb2c1sg0CTHB4pWumWZtya8M-iyVddzP4lP4j7CKTsJ6rNXdF4KK4GsSr7eyNl5vjNvwgiPJ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چک سنگین شاهزاده به صورت موشتبی خامنه‌ای
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23765" target="_blank">📅 09:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23764">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رویترز:
ترامپ امروز در نیویورک با تعداد زیادی از رهبران جهان دیدار خواهد کرد و
ایران، اوکراین و یمن
از محورهای اصلی برنامه او هستند. همچنین قرار است با رهبران کشورهای خلیج فارس درباره حملات حوثی‌ها جلسه داشته باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23764" target="_blank">📅 09:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23763">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رویترز:
در یک تحول سیاسی داخلی روسیه،
رمضان قدیروف
بار دیگر به عنوان رهبر جمهوری چچن انتخاب شد؛ نتایج رسمی تقریباً
۱۰۰ درصد آرا
را به او اختصاص داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23763" target="_blank">📅 09:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23762">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رویترز:
ایالات متحده قصد دارد یک پایگاه نظامی متعلق به دوران جنگ سرد را در منطقه
نارزارسوآک
در جنوب گرینلند مجدداً احیا کند و همچنین در
مسترسویک
در سواحل شرقی، یک حضور نظامی جدید ایجاد کند؛ این اقدام در چارچوب توافقی میان آمریکا، دانمارک و گرینلند انجام خواهد شد که قرار است در نیویورک امضا شود. نارزارسوآک در گذشته محل پایگاه نظامی آمریکا با نام
بلویی وست وان (Bluie West One)
بود که در دهه ۱۹۵۰ تعطیل شد. منطقه مسترسویک نیز در حال حاضر توسط واحد ویژه دانمارکی
سیریوس (Sirius Dog Sled Patrol)
مورد استفاده قرار می‌گیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23762" target="_blank">📅 09:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23761">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آسوشیتدپرس:
بریتانیا اعلام کرد به درخواست عربستان، برای چند هفته
سوخت‌رسانی هوایی به جنگنده‌های سعودی
انجام خواهد داد. این نخستین حمایت نظامی مستقیم بریتانیا از عربستان در درگیری جدید با حوثی‌هاست و لندن آن را اقدامی دفاعی عنوان کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/23761" target="_blank">📅 09:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23760">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پزشکیان : دشمن در تلاش است تا تمام راه‌های هوایی‌ و زمینی را بر ایران ببندد تا ما را مجبور به تسلیم کند.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23760" target="_blank">📅 09:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23759">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">الجزیره: نیروهای اسرائیلی به شهر الرفید در حومه القنیطره، در جنوب غربی سوریه، نفوذ کرده و اکنون تعدادی از خانه‌ها را تفتیش می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23759" target="_blank">📅 09:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23758">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fffc1acfa.mp4?token=ARbeTyMWXFOAAXc1iCwMB2-NsCUOcLKU1kNOGOwPnUSv2U2K95tBCLqxYqyt6U68U0AH2v8xBJtbHbbvZbFf5taGr_SIuWhvXcdIC-fxXf0Mk8v7n2JqgfTAMHD3LTLl3s74w8OiNkDCkCfUdvP8_6IMbUCXzKNr3iABoqSyywIrHz1tQR92NSWfefzUSXf5yTgCVULFGSCSrhx0779da9T2V_IeFqAEv7xG3LIX7jlxF6kIVGsmJMWj3K00LCERTelq-ZRYsMeAh_8STe2JRsRtrV8bR4EKoFu8lwXq-Tv9nCs4TAKKfzkteHFr6stbOOB55ckP70PNs17LSHuO7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fffc1acfa.mp4?token=ARbeTyMWXFOAAXc1iCwMB2-NsCUOcLKU1kNOGOwPnUSv2U2K95tBCLqxYqyt6U68U0AH2v8xBJtbHbbvZbFf5taGr_SIuWhvXcdIC-fxXf0Mk8v7n2JqgfTAMHD3LTLl3s74w8OiNkDCkCfUdvP8_6IMbUCXzKNr3iABoqSyywIrHz1tQR92NSWfefzUSXf5yTgCVULFGSCSrhx0779da9T2V_IeFqAEv7xG3LIX7jlxF6kIVGsmJMWj3K00LCERTelq-ZRYsMeAh_8STe2JRsRtrV8bR4EKoFu8lwXq-Tv9nCs4TAKKfzkteHFr6stbOOB55ckP70PNs17LSHuO7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس:
«فکر می‌کنم بسیاری از آمریکایی‌ها می‌پرسند:
چرا قیمت بنزین این‌قدر بالاست؟
دلیلش این است که
ایرانی‌ها همچنان به سمت کشتی‌های تجاری موشک و پهپاد شلیک می‌کنند
.
این موضوع، اساساً
به ایرانی‌ها مربوط می‌شود
.»
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23758" target="_blank">📅 09:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23757">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJJXVSNRzYUurV2hHBMWb21vetPaLUe1ROy2EqHE7G9ubgFO-YLeIT2kEsPXhaCMRJIPeCFnM3lMo58vuKlndwDktRHslhbP35KkeZDE9ULM0nc4aU-n81CEfUEk68cXaQyU7Oi5gMcGW8Ry75JkSTasUpCFUd2dCtZksTH9UkFqOTUX5mKOO3nK8-gHDU95uT-osPnV9K-2PBa2osCqxGQxfkBpunZqOlt8FoQHKxN6CvFPiPxETPAg3Be48_R7Ovhydqb74jFhgMz4w_PciAYVGClnH9eAX0uQty_xbbuSK5ij-v2JWL0n3wrPDlAscKR-t-l5BnSDRj365T4YjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان راهی نیویورک شد ، خلیج فارس همچنان در کنترل انبوهی از هواپیما‌ها و پهپادهای آمریکایی
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23757" target="_blank">📅 08:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23756">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4e96acdbd.mp4?token=MWeDEY60H8drwqDUwf4P5tbXpAZ9IaZGbxU_Q1jkG7FTVZpvfAXQPYaYCF2kNjVaF1O2lkM45XgTeuQLoVwseStY105e95HBs_dk3chXtdxIb9MWitOjs0y8YqNBlFeUdBQAduugxd-RaEevLS9bf1uLRf2PaTCZeDWgWFI5wjxSaTNg-e2H6w3AufvxpcjgovWmnJ3Y_eGaA1lr_XCFYHGx6m1BJ1eTOT-NimBF4X4iaABy0nF_YcTOTuTmib9jNLujFoHKzjxHLRq47nT2NoZckFoMaXgz8do_0D8sLAzyJN95okPwprgZHzIfWNGF0TTs7GhS5tRzRGTAyfaRxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4e96acdbd.mp4?token=MWeDEY60H8drwqDUwf4P5tbXpAZ9IaZGbxU_Q1jkG7FTVZpvfAXQPYaYCF2kNjVaF1O2lkM45XgTeuQLoVwseStY105e95HBs_dk3chXtdxIb9MWitOjs0y8YqNBlFeUdBQAduugxd-RaEevLS9bf1uLRf2PaTCZeDWgWFI5wjxSaTNg-e2H6w3AufvxpcjgovWmnJ3Y_eGaA1lr_XCFYHGx6m1BJ1eTOT-NimBF4X4iaABy0nF_YcTOTuTmib9jNLujFoHKzjxHLRq47nT2NoZckFoMaXgz8do_0D8sLAzyJN95okPwprgZHzIfWNGF0TTs7GhS5tRzRGTAyfaRxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در‌نیویورک
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/23756" target="_blank">📅 08:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23755">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Geu8Rz8OskgLK4jSTmoVKtAp38GMUFt8fC1Tkk2rCQb39NIfutbxYAYe4pT7Y-KaCYDa2tEku5mjS1XCmmjiXI8baE1OBGNZp0Av6RroqJ9oB1_4BwHOC3SopfXxPayF5ZLxQfpq8Wa093BkI0Me9qtZY_g3ZsrlccHjmXqa3OK2LmTcFdH2JXU0Y2JJ9TlZrfoggrbESFdxblTpvVuAbgqpEXWqkNKeCRU16ALQdcY4qYGHVVP8vHK8J7Ujk97TGl1DHzqXk9r2VTZr1AKbWFAZJESzZ6i83ybqgWhdx_JmQpCEYoAlk-oiG_20wikdCmTKmqkrqHx-oCVTeEkAgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ شبکه تلویزیونی خود را راه اندازی کرد
کاخ سفید : «ترامپ تی‌وی» (Trump TV) هم‌اکنون در حال پخش است؛ برنامه‌ای ۲۴ ساعته و به‌روزرسانی‌شده به‌صورت آنی که گزیده‌ای از بهترین لحظات گذشته، اطلاعیه‌ها و جدیدترین و مهم‌ترین اخبار دولت را یک‌جا گرد هم آورده است.
همه لحظات مهم قبلاً از تلویزیون پخش نشده‌اند، اما حالا این امکان فراهم شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23755" target="_blank">📅 07:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23754">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‏جی‌دی ونس، معاون ترامپ، در گفت‌وگو با نیوزمکس: ما تاسیسات هسته‌ای جمهوری اسلامی، به‌طور مشخص سه تاسیسات هسته‌ای را با یک حمله تاکتیکی فوق‌العاده نابود کردیم. علاوه بر این باید اطمینان حاصل کنیم آنها قادر به بازسازی برنامه هسته‌ای خود نیستند. @WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23754" target="_blank">📅 07:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23753">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏جی‌دی ونس، معاون ترامپ، در گفت‌وگو با نیوزمکس: ما تاسیسات هسته‌ای جمهوری اسلامی، به‌طور مشخص سه تاسیسات هسته‌ای را با یک حمله تاکتیکی فوق‌العاده نابود کردیم. علاوه بر این باید اطمینان حاصل کنیم آنها قادر به بازسازی برنامه هسته‌ای خود نیستند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23753" target="_blank">📅 07:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23752">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، گفت: «این را به صورت زنده در تلویزیون‌های سراسر جهان به حاکمان ایران اعلام می‌کنم؛ ما می‌دانیم حساب‌های شما در جزایر ویرجین بریتانیا و شرکت‌های واسطه کجا قرار دارند. خانه‌های چندصد میلیون دلاری شما در سراسر جهان را می‌شناسیم و قصد داریم همه این دارایی‌ها را از شما بگیریم و به مردم ایران بدهیم»
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/23752" target="_blank">📅 01:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23751">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گزارش ها از برگزاری جلسه اضطراری فرماندهان نظامی ارشد کشور های عضو ناتو.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/23751" target="_blank">📅 01:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23750">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">شبکه ۱۲ اسرائیل در مورد یک مسئول امنیتی ارشد اسرائیل:اسرائیل برای یک تنش احتمالی با ایران آماده‌سازی می‌کند.
وضعیت حساس و قابل تغییر است، و در صورت شکست مذاکرات بین واشنگتن و تهران، ممکن است تنش‌ها به سرعت افزایش یابد و اوضاع از کنترل خارج شود.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/23750" target="_blank">📅 01:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23749">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d0c485c05.mp4?token=L76gwMQr6x3eGAU8Ft1LyBjE3oyWKP8IyuWpBhl-tfRkHZJ5NoWZpQApjyLqagI0LamlxNtZFTbHDcw4CZwMQLHqsGWezJJDTL7lfdXCLeQ_nd7flpo-qw2cHEI5LgdIc8z6OxSMuH_41c3qKMo-lV6YAYIlS3nfAx0HsOf_F2Bi1lOBtt-BwdL883tFs0SflyYCTeI6C06Sby0JbldRsvQI2uaNdwmP0IdFmlMc1AIEZbqBxafyyKYuxmCk9AAgkCvo3_2FdliSPnagYDG2uk6ZtW7Z-uf2FF37bKm-NMI32P3sREFpeA9hqBKTIn1vG_nPtKWvbQChKUPNWLbeWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d0c485c05.mp4?token=L76gwMQr6x3eGAU8Ft1LyBjE3oyWKP8IyuWpBhl-tfRkHZJ5NoWZpQApjyLqagI0LamlxNtZFTbHDcw4CZwMQLHqsGWezJJDTL7lfdXCLeQ_nd7flpo-qw2cHEI5LgdIc8z6OxSMuH_41c3qKMo-lV6YAYIlS3nfAx0HsOf_F2Bi1lOBtt-BwdL883tFs0SflyYCTeI6C06Sby0JbldRsvQI2uaNdwmP0IdFmlMc1AIEZbqBxafyyKYuxmCk9AAgkCvo3_2FdliSPnagYDG2uk6ZtW7Z-uf2FF37bKm-NMI32P3sREFpeA9hqBKTIn1vG_nPtKWvbQChKUPNWLbeWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها به سلاح هسته‌ای دست نخواهند یافت؛ بگذارید همین‌طور بگویم.
وضعیتشان خوب نیست. در واقع، امروز جلساتی در این باره دارم. عملکرد آن‌ها بسیار ضعیف است.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/23749" target="_blank">📅 01:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23748">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZ7mED18b0E2drjNdDbfD8XrhjJsTo6zW-_ondKBelIy_OqmfYn3586jbnIseyvdYW3I2tRx2xkcj8inHU7alNNB0AP0rJIjM20Uy3k03vUdnJqPcl4hEOyyV7VH2oloWeWT2YPhZ04SOVuUyB6EcJtdRgNdI6y5N_SujYDFcdu7-ZI22UjaPKU7Y6-s5cPIeC_VAMpzkh0EHjUTnc-L_pEmQtp6ox4_tgG4Aw6987_FJ7JJH7PDttaaMDW7AJAWmLdnwoPToW2Pf_yZjp52fPcn1MzFOaU5zdGXadnglNropsB1P8wd8PVzRcV8O3r2CsNRVyUOJ7C-NhaVImwjXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصاحبه آیت‌الله خمینی و ابراهیم یزدی با مجله پورنوگرافی پنت‌هاوس، در جلد ۱۰، شماره ۱۲، سال ۱۹۷۹ ، روی جلد هم عکس مدل دیان ویدر است. هماهنگی مصاحبه‌ها را قطب‌زاده که عامل کاگ‌ب بود، انجام می‌داد. همان‌طور که می‌بینیم، این رژیم از ابتدا بر همین اساس بنا شده بود. ابراهیم یزدی بعدها در آثارش توضیح داد که نه، ما با نیویورک تایمز مصاحبه کرده بودیم، ولی پنت‌هاوس آن را پخش کرد تا قضیه را ماست‌مالی کند. خلاصه محتوای مصاحبه، محور صحبت‌ها بیشتر در مورد انقلاب ۱۳۵۷، شاه، آمریکا، حکومت اسلامی و آینده ایران بود.که واقعا آینده ایران مانند پورن شد
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/23748" target="_blank">📅 00:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23747">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">فاکس‌نیوز: ترامپ، در آستانه
هفته ای سرنوشت ساز
و دیدار با رهبران کشورهای حاشیه خلیج فارس در حاشیه مجمع عمومی سازمان ملل، در حال بررسی اقدام بعدی خود درباره ایران است.
ترامپ به فاکس‌نیوز گفت: «من در حال تصمیم‌گیری هستم. سؤال من این است که اگر و زمانی که تصمیم بگیرم، آیا کل کشور را منفجر کنم؟ آنها بهتر است رفتارشان را درست کنند.»
او در حال بررسی گزینه‌هایی از جمله اقدام نظامی، ادامه فشار اقتصادی یا تلاش دوباره برای توافق با ایران است.
ترامپ به فاکس نیوز گفت:  برای دیدار با مسعود پزشکیان، رئیس‌جمهور ایران، در این هفته آمادگی دارد، اما در حال حاضر هیچ دیداری میان دو رهبر در برنامه رسمی قرار ندارد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/23747" target="_blank">📅 00:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23746">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‏منابع محلی نزدیک مرز ایران و پاکستان:  تعداد زیادی از افراد مسلح بلوچ وارد منطقه رادیگ در مند، شهرستان کیچ، بلوچستان شده‌اند و طبق گزارش‌ها، در چندین نقطه ایست بازرسی ایجاد کرده‌اند.
‏گزارش‌ها همچنین حاکی از آن است که یک اردوگاه نیروهای امنیتی پاکستان مورد حمله قرار گرفته است
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/23746" target="_blank">📅 00:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23745">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نیویورک‌تایمز: علی الزیدی، نخست‌وزیر عراق، متعهد شده است گروه‌های شبه‌نظامی مورد حمایت ایران را تا ژوئن ۲۰۲۷ خلع سلاح کند. طبق این طرح، ابتدا یک دوره ۹۰ روزه بدون حمله میان شبه‌نظامیان و نیروهای آمریکایی در نظر گرفته شده و سپس تحویل سلاح‌ها تا ۳۰ ژوئن ۲۰۲۷ انجام خواهد شد. شبه‌نظامیان خواستار تمدید این مهلت تا پایان ۲۰۲۷ هستند. الزیدی همچنین گفت عراق به‌دلیل بسته‌شدن تنگه هرمز حدود ۶۰ میلیارد دلار و ۶۰ درصد درآمد ماهانه صادرات خود را از دست داده و ایران اجازه عبور نفتکش‌های عراقی از تنگه را نداده است.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23745" target="_blank">📅 00:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23744">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">BTC 84,100$  @WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23744" target="_blank">📅 00:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23743">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نیروهای مسلح لتونی کشور اروپایی: آماده باشید! به اطلاع می‌رسانیم که احتمال وجود تهدیدی در فضای هوایی لتونی وجود دارد.
حدود ۵۰ دقیقه پیش، هشدارهایی در پی احتمال وجود تهدیدی در حریم هوایی منطقه «کراسلاوا» (Krāslava) در لتونی که در امتداد مرز با بلاروس و در نزدیکی مرز روسیه واقع شده است  فعال شد.جنگنده‌های ناتو به منطقه اعزام شدند. هنوز جزئیات بیشتری منتشر نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23743" target="_blank">📅 23:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23742">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">رویترز گزارش داد که جان راتکلیف، رئیس سازمان اطلاعات مرکزی آمریکا (سیا)، اوایل امروز، بدون هماهنگی قبلی، در جریان سوخت‌گیری هواپیماهایشان در فرودگاه شانون ایرلند، با زلنسکی، رئیس جمهور اوکراین، دیدار کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23742" target="_blank">📅 23:55 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23741">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">تحلیلگر آمریکایی : ترامپ با یه مصاحبه و جمله احتمال توافق، قیمت نفت رو از ۱۰۷ به ۹۷ دلار رسوند. عربستان هم به دنبال بازگشایی خط لوله شرق-غربه و با این تفاسیر دیگه نیازی به تنگه هرمز نخواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23741" target="_blank">📅 23:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23740">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">چپقچی وزیر امور خارجه برای شرکت در مجمع عمومی سازمان ملل وارد نیویورک شد.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23740" target="_blank">📅 23:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23739">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نیروهای دولتی یمن: تلاش گروه حوثی برای نفوذ در جبهه "العنین" در منطقه "جبل حبشی" در غرب شهر تعز را خنثی کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/23739" target="_blank">📅 23:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23738">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/23738" target="_blank">📅 23:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23737">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/23737" target="_blank">📅 23:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23736">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM.g</strong></div>
<div class="tg-text">یاشار داداش انشالله اگه ما تو این انقلاب شیرو خورشید پیروز شدیم
شما ایران میای؟
تکلیف چنل چی میشه؟</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/23736" target="_blank">📅 23:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23735">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">از گزارشها اینگونه بیان میشود که از حدود یک ساعت پیش سامانه میخک واردات خودرو را بسته
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/23735" target="_blank">📅 22:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23734">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ماهان‌ایر: از امروز ۲۱ سپتامبر
پروازهای خود به استانبول، آنکارا و گرجستان را متوقف کرده است؛ مسیر تهران–مسقط نیز از ۱۷ سپتامبر متوقف شده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/23734" target="_blank">📅 22:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23733">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترکیش ایرلاینز: طبق اعلام یک نماینده این شرکت،
تمام پروازهای ترکیش ایرلاینز به ایران فعلاً تا(نوروز) مارس ۲۰۲۷ برنامه‌ریزی نشده‌اند
و ادامه آنها پس از آن تاریخ نیز تضمین نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/23733" target="_blank">📅 22:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23732">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">الجزیره: در چند ساعت اخیر گزارش شد یک
کشتی دوم
نیز در تنگه هرمز بر اثر برخورد بقایای یک پرتابه ناشناس آسیب دیده است. هیچ‌کس زخمی نشده و کشتی به مسیر خود ادامه داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23732" target="_blank">📅 22:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23731">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : باز هم برخی ادمین‌های بی‌اطلاع تلگرام اشتباه کردند و نوشتند «هلیکوپتر جدید مارتین وان»! اولاً نام آن Marine One (مارین وان) است. مارین وان اسم یک مدل هلیکوپتر نیست؛ به هر هلیکوپتری از تفنگداران دریایی آمریکا که رئیس‌جمهور را حمل کند Marine…</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23731" target="_blank">📅 22:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23730">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، برای نخستین بار از هلی‌پورت تازه‌ساخته‌شده در محوطه جنوبی کاخ سفید استفاده کرد و با بالگرد ریاست‌جمهوری «مِرین وان» از این محل به مقصد خود رفت. ترامپ در پیامی ضمن تشکر از جیم تایکلت، مدیرعامل لاکهید مارتین، گفت این شرکت کمک…</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23730" target="_blank">📅 22:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23729">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9df0feca14.mp4?token=L35Gzk78wqVtIFatUe5Jfy3bf46iRdwTrcQNCxFH23esFT6FRP9PjxXP0PWAcQWCwuGO3xe5Fqve01QPuYETQOxJAS6Q5zUohwCqHfwTaLw_CM2ZI4pyENXakh1a2tT1yiywAU0CYlmC-lc9CJTPNCylnr_pFc55lzHD5foaHziJKr-DgUrNk6NPqcG1I_RmN1Gdfpben4wpwL1C0k1pQQtWI2Szkp239yLVjzHAq5aXO0c8q4NjE36lw0yn57Vde08oTrcROyc9seVyMzpL-LwCnoddjHxJLsl0aAqcfUdXlzNTw8OD-VXhjjaH0Ft2MOKdwPoNMSonfru1AOpyEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9df0feca14.mp4?token=L35Gzk78wqVtIFatUe5Jfy3bf46iRdwTrcQNCxFH23esFT6FRP9PjxXP0PWAcQWCwuGO3xe5Fqve01QPuYETQOxJAS6Q5zUohwCqHfwTaLw_CM2ZI4pyENXakh1a2tT1yiywAU0CYlmC-lc9CJTPNCylnr_pFc55lzHD5foaHziJKr-DgUrNk6NPqcG1I_RmN1Gdfpben4wpwL1C0k1pQQtWI2Szkp239yLVjzHAq5aXO0c8q4NjE36lw0yn57Vde08oTrcROyc9seVyMzpL-LwCnoddjHxJLsl0aAqcfUdXlzNTw8OD-VXhjjaH0Ft2MOKdwPoNMSonfru1AOpyEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، برای نخستین بار از هلی‌پورت تازه‌ساخته‌شده در محوطه جنوبی کاخ سفید استفاده کرد و با بالگرد ریاست‌جمهوری «مِرین وان» از این محل به مقصد خود رفت. ترامپ در پیامی ضمن تشکر از جیم تایکلت، مدیرعامل لاکهید مارتین، گفت این شرکت کمک ارزشمندی برای ساخت هلی‌پورت انجام داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23729" target="_blank">📅 21:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23728">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تنگه صدای علی لاریجانی میاد
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23728" target="_blank">📅 21:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23727">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsntzRA4qe-dIwwiNdrf4MGyWmwPbVwdk1jp3pgakahWmGtWme-Iqppkc6l0jUZo3jHFlY1aYV3DudFdfZ57JsdKNFIJ00_jNDOyV-2n8BbRG5sKz95wqZKdZZOelrWlW3qITtJJR4qGpLl-rJi8i3OQr387GYPpZGpmuLqWuSF_JnufTpKDDygcAyjIfcRlMCwVM9_9h_QYkB_ca55F0LiTx-gIpWcCZe5svDEpqVCIvoYTtPRk8DMq3yfMiCgjVru8yrgILEllLQ1IYOrlozaMEIrDqnmIScFm7d9H0ld2MghsoNLwNM4olyf0vtcj3Ifljqyd2tmSI3tAyyOB9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرقت موبایل یک پاکبان در مشهد @WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23727" target="_blank">📅 21:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23726">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خبرنگار الجزیره: ارتش اسرائیل عملیات سوم تخریب را در مناطق تحت کنترل خود در جنوب شهر خان یونس در جنوب نوار غزه انجام داد.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23726" target="_blank">📅 21:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23725">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بلومبرگ گزارش داد بریتانیا در حال بررسی گسترش حمایت نظامی از عربستان سعودی است؛ ریاض از لندن برای مقابله با تشدید حملات حوثی‌ها و حفاظت از خاک و زیرساخت‌های نفتی خود درخواست کمک کرده است. عربستان همچنین خواستار حمایت عملیاتی و دفاعی بریتانیا شده
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23725" target="_blank">📅 21:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23724">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بلومبرگ گزارش داد ایران به یک محموله دیگر گاز طبیعی مایع‌شده (LNG) قطر اجازه عبور از تنگه هرمز به مقصد پاکستان را داده است. بر اساس این گزارش، یک محموله دیگر LNG قطر نیز در همین ماه با مجوز ایران از تنگه هرمز عبور کرده و به پاکستان رسیده بود. کشتی حامل محموله جدید قرار است فردا به پایانه واردات LNG پاکستان برسد
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23724" target="_blank">📅 21:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23723">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کان: منبعی در شورای رهبری ریاست‌جمهوری یمن گفت تماس تلفنی ترامپ با رشاد العلیمی، رئیس این شورا، چیزی فراتر از ابراز حمایت احساسی از سوی رئیس‌جمهور آمریکا نبوده است
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23723" target="_blank">📅 21:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23722">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f0a6a7ba3.mp4?token=slD67-GV52hGE1UnkGCVsu9ou3TA6-rb44XCTAvn0IpTL1nVDtFkrpaKO3ourGZ11IQS9JZ15YDGrGCqEsfNBk1KSkbYI3hygIUji7IShLt7STj24vgrML_LUZLekEIUYZlebvoYzOQE9hULVVZeUACVhC64ZUN2PQbN4mw9CQa7ra6Ej1NMDsQzOkUE6l8XOyywjHBFMFUcrF42oXvvX834VotuQ3ku1ldRwCgWpGfORBxtV9j9hev7itavhoOVjp4gr4ZevlxHuKUNxSDlGJ-LDS2e3k8O0nqHsFx5dSmK8u9azOKBJXB2A_k8GXfK4L-ZloZoglhWlIWoTViQ3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f0a6a7ba3.mp4?token=slD67-GV52hGE1UnkGCVsu9ou3TA6-rb44XCTAvn0IpTL1nVDtFkrpaKO3ourGZ11IQS9JZ15YDGrGCqEsfNBk1KSkbYI3hygIUji7IShLt7STj24vgrML_LUZLekEIUYZlebvoYzOQE9hULVVZeUACVhC64ZUN2PQbN4mw9CQa7ra6Ej1NMDsQzOkUE6l8XOyywjHBFMFUcrF42oXvvX834VotuQ3ku1ldRwCgWpGfORBxtV9j9hev7itavhoOVjp4gr4ZevlxHuKUNxSDlGJ-LDS2e3k8O0nqHsFx5dSmK8u9azOKBJXB2A_k8GXfK4L-ZloZoglhWlIWoTViQ3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی وینس، معاون رئیس‌جمهور:
امسال در ماه نوامبر(آبان)، سرنوشت‌ساز خواهد بود. یا باید در برابر این دیوانگی بایستید، یا با آن همراه شوید.
و ما برای ایستادگی در برابر آن و مبارزه با آن اقدام خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23722" target="_blank">📅 21:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23721">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eW1BRUUGU0ewZhdrYL6ErT0b8v-2eESL6vfW5Om4PCknUsG-RI8_HsYbebwItKQHOQHJVD11ZhM6mtoGMN2mcXN_KWCYOHuXRJGo2HD46QpjybFwDhQfq0QuOgDAuWKSbXLh5FCj8ql6uzxq0ZZgiylZvlXxKCksL2v4PhZC7mpbv7T7_tS6TtXktXKr7Syo5xXj35JSsm1JgDQepC66R4TkGfr77idBb_wJmGyHvYfVAkKZwX6FvMXOnuoJMDjkQ5A2GdG_-PNjlfftwz0VojiXoghJ8qnX_jggO4IeWzHX76UxB4u_vVLGKmciMgidgZ-gsSYoGM77eG4ciJ84sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت برنت به زیر ۱۰۰$ آمد و حملات موشکی جمهوری اسلامی به کشتی ها تأثیر خود را از دست میدهند. قیمت در این لحظه ۹۹.۵$
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23721" target="_blank">📅 21:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23720">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا:
ما ایران را
بیش از هر زمان دیگری تحت فشار قرار داده‌ایم
. حدود یک ماه پیش پنج اختیار تحریمی جدید علیه حکومت ایران به دست آوردیم که حوزه‌های
هواپیمایی، دریانوردی، رمزارز و طلا
را شامل می‌شود. از
۲۳ سپتامبر
تمام خطوط هوایی ایران در سراسر جهان تحت فشار قرار خواهند گرفت؛ به این معنا که در صورت فرود هواپیماهای ایرانی، ارائه
سوخت، خدمات فرودگاهی یا فروش بلیت
می‌تواند باعث شود ارائه‌دهنده خدمات از سیستم مالی و دلاری آمریکا کنار گذاشته شود. او گفت آمریکا شبکه‌های تسهیل‌کننده انتقال پول به ایران را شناسایی کرده و در حال متوقف کردن فعالیت آنهاست. تاکنون
سه بانک
نیز هدف قرار گرفته‌اند؛ از جمله
شعبه دبی دومین بانک بزرگ مصر
که به گفته او بیش از
۱.۸ میلیارد دلار
به حکومت ایران منتقل کرده، یک بانک ترکیه‌ای و شعبه‌های خارجی
دومین بانک بزرگ روسیه
. این شعبه‌ها تعطیل خواهند شد. درباره چین نیز وزیر خزانه‌داری آمریکا گفت واشنگتن با کشورهای مختلف در حال انجام
گفت‌وگوهای محرمانه و پشت‌صحنه
است و در بسیاری موارد این روش را بهتر از رویارویی علنی می‌داند.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23720" target="_blank">📅 20:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23719">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رویترز: حوثی‌ها امروز تلاش کرده‌اند ارتفاعات راهبردی یمن را تصرف کنند تا ارتباط مناطق ساحلی دریای سرخ با بخش‌های باقی‌مانده تحت کنترل دولت یمن را قطع کنند. این تحرکات همزمان با گزارش‌ها درباره خودداری ترامپ از حمله مستقیم به حوثی‌هاست.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23719" target="_blank">📅 20:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23718">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آسوشیتدپرس: یک مقام ارشد حوثی امروز هشدار داد کشورهایی که در عملیات عربستان علیه حوثی‌ها مشارکت کنند، ممکن است هدف حملات قرار گیرند و گفت این گروه فعلاً قصد حمله به کشتی‌های آمریکایی را ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23718" target="_blank">📅 20:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23717">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaooJnm5TZb2iIp8z9AvEAFDmSdrZZeRxZZsuyGyAgXLYE1XtR14LvUnQeWJH9YgUjQm1pF6gDA5erIUJMBpIoKLc7nC_EvVXfnPgyyJuZaQYrU_beBPYFPDa_RMXQ1weC7Cikwb8YhRBrVNYUsZgeVcBPYzvQSFeJSaQcXAFDK69oW1lViBQfhew6cBK-TGxLChSzUlvzWF8FgnHGGVmyFqVgfJJwRmqBCCyZ3F6xcElEVNav2zVzHndIpa6Tcf0HVj-KC5RO9fM4wc8iJ_MuNP73s222nMfeO1Tjm-YPs8ZohuN7XoUYEUH8jQuivEgy85BaThMDWk2lJdp9bFwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت تنگه ۷ سوخترسان ۱ پهپاد و پی۸
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23717" target="_blank">📅 19:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23716">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTal2TC46KAeqK36XdjN9y772dAfSvMh34rV-W0wxnYcXX4pTNV6GqfM3eQY3j02XLdZScfcuf3WONCa0A8ImVzCYuAm1f0q7CtIsnT5NSGoBTMYrGpdJMSl0QShQz5Y71vfjTjxIk4AI_F4EaTN0Zxn__Fv9beAdli73sbXtiZWFaXr8NwFn7WyDJwtIoAU_h6FHVb_y3ICCB2eqikD_q-ys8aPwJVb1EXckRpLyvHWcrMUj4NC6A0E59lPhms01vl47FOAauQqeMYIf9qMByhYG9fInqBYLT4QnOct-yAZqrGJj7Odq0No3GYvBsx1I5BVrs6rBQpEDNyFLfft-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد یک نفتکش حامل گاز مایع (LPG) هنگام عبور از خروجی تنگه هرمز، بر اثر اصابت بقایای پرتابه‌های ناشناس آسیب دیده است. طبق گزارش فرمانده کشتی، تمام خدمه در سلامت هستند و هیچ‌گونه آلودگی زیست‌محیطی گزارش نشده است. نفتکش به مسیر خود به سمت بندر مقصد ادامه خواهد داد و مقام‌ها در حال بررسی این حادثه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23716" target="_blank">📅 19:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23715">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmbjucuHdkRNjea_LwYaAnicVyCuLTuyuLP9L6IcVzO-x_tIIvN2Z_lCc7aDiM-fHJfjYedJZiGDwm7R0XULKCA19CgDLLioXSrwxWOss-xqJF7OFNI0w-L85XNhDflkTis0sD-BcfEHJYtGLJ_SHDw26BeRQ6n72JFcN_EzGEu-q6PdB5VOoftmRK3MKp4mH2oadRmHCow2fTB53QDQFvPLFnDU1GQSSNPEMXq1oNjlapL_YWZt9Vwl4qrEZGvJ4fzSVCfIZKt5wmpMyuebGoS_5Iug4XkR4XAl3V9F4yCpr4ruZGPA7R3y-AqIZu7S3WYGsB_HLv_RW9oulNI6fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، با انتقاد از هشدارها درباره خطرات هوش مصنوعی گفت: «همان افرادی که می‌گفتند به‌دلیل گرمایش جهانی تا ۱۲ سال دیگر همه ما خواهیم مرد، حالا می‌گویند هوش مصنوعی ما را خواهد کشت و ربات‌ها به ما حمله خواهند کرد و همه‌چیز یک فاجعه است.» ترامپ با رد این نگرانی‌ها درباره هوش مصنوعی گفت: «هرکس هوش مصنوعی را ببرد، برنده است! ما اکنون از چین و همه دیگران جلوتر هستیم و من می‌خواهم همین‌طور باقی بماند.» او افزود که نمی‌خواهد رشد هوش مصنوعی را محدود کند و معتقد است این فناوری می‌تواند از انقلاب صنعتی یا حتی خود اینترنت بزرگ‌تر باشد. ترامپ در عین حال گفت آمریکا مراقب خواهد بود و وزارت دادگستری و سایر نهادهای اجرای قانون در صورت لزوم مداخله خواهند کرد، اما او همچنان از هوش مصنوعی و «ابرهوش» حمایت خواهد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23715" target="_blank">📅 19:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23714">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRMUdlFH6WpwxE5O901Q_4c7GVmcm0IYxslHSJqfhkEm8hX1zJ46_sK3avqdAEhwyxF3CcN2scsp-6ww39jMd9snBfWxbg5bwvvtxXA6FX3lwCAqEp5zV_yYc2-JraZ5qjbV_qyouCKZvJ8qm9LFhyZNvVr469XPrEfRdou8wK2QXq-e-Mes6EGgkNvWvMcaYwlLvxtB5h0gBKza9a_z8Z22K9oy3rWUkwKhG4EXcW6Ha01BoFBbzcqBljSuX26kGGggA8P3llPpxKt_QHFlsKRKLptItr7737j4cyHbX4dx6NYOelacY-9tLX9wyqBJm5W8z0CdqyyKpplGEa_fqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره‌ای نشان می‌دهند دست‌کم ۲۵ هواپیمای سوخت‌رسان آمریکایی اکنون در پایگاه هوایی العدید قطر مستقر هستند؛ این بزرگ‌ترین حضور تانکرهای آمریکایی در این پایگاه از زمان آغاز جنگ با جمهوری اسلامی در فوریه عنوان شده است. این تانکرها در اوایل درگیری به‌دلیل تهدیدات موشکی سپاه پاسداران از منطقه عقب‌نشینی کرده بودند و از حدود ژوئن روند بازگشت آنها آغاز شد. هواپیماها به‌صورت پراکنده در پایگاه پارک شده‌اند؛ وضعیتی متفاوت با استقرار متراکم تانکرها در پایگاه هوایی پرنس سلطان عربستان که می‌تواند نشان‌دهنده تداوم تدابیر احتیاطی در برابر حملات احتمالی ایران باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23714" target="_blank">📅 19:30 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
