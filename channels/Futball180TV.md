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
<img src="https://cdn5.telesco.pe/file/PoUlvBa05GRbPf5Elr3w4_gx1mIswz2U2oMjBLqwSX7n47LgWccWx6r_p3nH2NNjsaBWI_fCpUK4_SQJVV6gvJQ4rE961xHTnl8vk0WLGAfD087BAcY9Bvdiwvcn9G-dTDCSfX4PN4WPyTAiM6KeYZsD5QZn9pi-9DfB0v5qGKHdxw7rqgUioL_SFSuza9GM37h3h2DbhRMg-ZQGzaSb-muhGiLxhuQpkfywUK7jbSWE2GC5rMbLZTv9B9YBjHf3sPtWCFTAwaBwoecJbnHTrlhZSxVJGQlxC_3_WdG8WGnzlPRIRs-HOvZ2SlJz5lcpGATYh4Ki62JDTaUNgOV7xQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 214K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 19:18:04</div>
<hr>

<div class="tg-post" id="msg-91196">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYudx2_QyoU0EZwfRIIuBe4xoG4Af8FoKKZuRxP3cOO9Z8_d9S9zz6-JNkVbXgK5a2png9z53-iUOLl6HzJAL5uZop7Mr9MEO5kLrpfA3s-WuzkwpNmfywhdaE1emmr6y3Ov1twAOYc2xNQ7bYjCbUJ2yeafj7ec_yg5PizSLiHNm2dvgXZ2dayYADmJsh-znTle3gosZxyrK0GPHPcvA0_mYfIOtk31eYtsJq7N3y9zbQLqnMScZnxNuxHD3GGwF_sV5r3I8xZSRe5pMPSK8eCgv6raE4hkypqZULURfSF-NoIY5yKsTgVs8R-I0gOue0athIzx3Du6N_1lt-8qbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
الرياضية عربستان: الهلال رسما برای جذب عثمان دمبله به پاریسن ژرمن آفر فرستاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 316 · <a href="https://t.me/Futball180TV/91196" target="_blank">📅 19:17 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91195">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nperU1tBOzcyCWfROGIO2tfL6zdboELNnYzHpo0RwQe2L4NMIufuSFi6ybNiQ2MfrdTt2Q_AzmlOcbABV2yaHY79dykn_ZSGQKb1NhFtXQ0hQNRlEGHukIFjOeUtftQ0iGbrgtw4Ok5L0bsglE3AxOaqsy-dqNuIafv3-jbLH56xfEkhYZA7rEEpPyTjLetb5CRM-_MJzf9-8XyUl6aB5jG9De-UAyCQTqRZehXDKVdF8O1aVqv9gdp2xvM-z03IN-zAeFKbhX7aQkTpkwhsYzOfjzTWIsDrD2TsvcP4Qs1r22uucGHWceXk-U6K9_m6LZRRA4f6byr1szTgzVgZ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه اوه نیوکاسل چربش کن
@Futball180TV</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/Futball180TV/91195" target="_blank">📅 19:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91194">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10990086be.mp4?token=I1ENTcc8kn6w0_4-zdwRj48FcRdEMGeU5w47lheG4q2AVrs5NZX6aN-WxMFn_aSuOgBwNxNsrV943WugX1XI4-TwBeMJ1CYQfIBMqsYepoW_-KnrrJZY9Bn3K0_5CTr7wBUVzyTPMCI5AiE0vafaLLBIV-TOib_eA-2hKB2_ua_TRuz1l9rVx-g5R1PWDQs6pfvB0YWOfQgApbdr_FVw5A5wxS2c62NbGnC7FqeUOCeVQzdvZKiy0kso2KUhr-94Ze62tpegDBRdCuvfj6fOby_nTXz4oe_zBrkjHXfXAGlSEuTApKMy6rMdctbP0OazOgb6z1Lq_Y_O1UJCAzeTcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10990086be.mp4?token=I1ENTcc8kn6w0_4-zdwRj48FcRdEMGeU5w47lheG4q2AVrs5NZX6aN-WxMFn_aSuOgBwNxNsrV943WugX1XI4-TwBeMJ1CYQfIBMqsYepoW_-KnrrJZY9Bn3K0_5CTr7wBUVzyTPMCI5AiE0vafaLLBIV-TOib_eA-2hKB2_ua_TRuz1l9rVx-g5R1PWDQs6pfvB0YWOfQgApbdr_FVw5A5wxS2c62NbGnC7FqeUOCeVQzdvZKiy0kso2KUhr-94Ze62tpegDBRdCuvfj6fOby_nTXz4oe_zBrkjHXfXAGlSEuTApKMy6rMdctbP0OazOgb6z1Lq_Y_O1UJCAzeTcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🙂
چیشد چیشد ازگل؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/Futball180TV/91194" target="_blank">📅 19:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91193">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
الرياضية عربستان: الهلال رسما برای جذب عثمان دمبله به پاریسن ژرمن آفر فرستاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/Futball180TV/91193" target="_blank">📅 18:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91192">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8fab7e29.mp4?token=VILca6qm2gr7v7hNukGoqYpIsi2sVjPj-JoQbRKFUJUmkgQTTI_blDfIAOtZe9e1IS2CQwLzkeCcz4OZBDStKdPQ9vZhuiMmYVk7SpdQbQNAOGi0I8a99BgOt7IjRxMnt3hzgZe5Vc9zxTFKXMrZvmEgfg1Fu74n8u2ooO9K7P4IOm768CzeFaHIeUQ8LyIqimt5qzjhS164FxLY-c-6Kkhr5pkideuRfjLnOlb9SGGvWJk-k1PKbaKn07MXcXgN76buZHcUswoQ3T5biEhLgfLk4MG7SIuZki4-6ojW3WQ1_W_NIeaZ5s6mo-Qs3QcQTFX8njOs4roJQAnE081aZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8fab7e29.mp4?token=VILca6qm2gr7v7hNukGoqYpIsi2sVjPj-JoQbRKFUJUmkgQTTI_blDfIAOtZe9e1IS2CQwLzkeCcz4OZBDStKdPQ9vZhuiMmYVk7SpdQbQNAOGi0I8a99BgOt7IjRxMnt3hzgZe5Vc9zxTFKXMrZvmEgfg1Fu74n8u2ooO9K7P4IOm768CzeFaHIeUQ8LyIqimt5qzjhS164FxLY-c-6Kkhr5pkideuRfjLnOlb9SGGvWJk-k1PKbaKn07MXcXgN76buZHcUswoQ3T5biEhLgfLk4MG7SIuZki4-6ojW3WQ1_W_NIeaZ5s6mo-Qs3QcQTFX8njOs4roJQAnE081aZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
اعتراف نیکبخت به تبانی استقلال و پرسپولیس در دربی!
‼️
😐
نیکبخت: اومدند گفت چون جو استادیوم بهم ریخته است بازی باید مساوی تمام شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/Futball180TV/91192" target="_blank">📅 18:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91191">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tavvniJVoYpYUTjFq9885uX261S3BlX9HOUMxbQdBBkhdLWw8REHhYcnUH7rNsfBFn91pSECKHddL7psMdc8n1zL2Y7hA2JG5lGKcADhbBYo-qEdK-5gqs2Y4wxnWNSxCdrmYrK-9vzs8iqFCUey0UbjPzvT_kyvUc-_zlYtsSlUCPe0o50rTXqLigqlLq65TpyCUEJggrh4dk7sIUd5SCLLS1kUwhkelXKMufiZnW6sK5DmQm2z_pHwXFuPaXjqdJ0yz-l2F7aW7nB8f_i6Q4ZY9O_gL8TctHPzLgs8tx9xZZmQk4ZWca354c4d5sYImdktiDafDbeTDND5fxhozA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوضاع خیلی خیطه:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/Futball180TV/91191" target="_blank">📅 18:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91190">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یحیی گل‌محمدی لژیونر جدید فوتبال مملکت:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/Futball180TV/91190" target="_blank">📅 18:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91189">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnsZ0G9YnifIfawEQkt5sOQxP7da35yT_rLafmTb-4WsBn65AmDY7qf7QMr-TbjEacTmwrKgGWkpUt1faY52Vp7pegnpV2zkqqq23Zqkx4zZGQuerL9DWUHeKZ135kI-C4sh6HbGaf1zLFCT-M71ifvdQusneZdVRkdFg4s4XEUIUUacXxKPqSAEL1iRLUMkxj5Ok-s7ox4RDz7KP119mtXrevJx5JFSwRFcgKTNsc3sNgyGgoR9_7DtW0JJAhDqZJ8kEkqSYw2d2ZBrOWWM3r8c16iuQwjDat4i1DUgAEK90i0MzBh1Y5o1pvGjM3vAnnRfCQMiXckO-6to0QSb-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوضاع خیلی خیطه:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/Futball180TV/91189" target="_blank">📅 18:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91188">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3kwhqAr6Q68ltTL7-HgJxw4n2AM_vdN_jGg60Ix9KJrJTTj7OMNM_ztg573JecpjGbjXGoZ8hSmim0iViDtUkQi_RqqMYqrKGb6fhiaaeEj-36cz2xEOe-9wgzG35bFkmHKq1lqFleyUli_RUSoAQCgRONEOmWVvTwtf_zgm0jOxAptYwS_op4lbYGa_qKEy9ukcY6x8spn9dBl4kghk7xbbVYzJCHIYyKtp_Cwd_pwhg0YIMRC1pH3jUBSC2x1W55l70gzyAU8hLkq8Latwpi_W6xr7p9LkqEa8G7l4w5HdmHHbaO-EiUz6sAOLDj2ytJyJzkcF-8tuwb2kEz39g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🙂
به برکت میانجی‌گری(همون خایه‌مالی) برای جمهوری اسلامی، اینترنت جمهوری اسلامی پاکستان هم دچار اختلال شده
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/Futball180TV/91188" target="_blank">📅 18:17 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91186">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzodrfXq9K2uEAqck-oe9IWlVPWHLFjyARqwus6tOy6GdDIEHs5WdLuVpsveRWlKGV6xb_b5DEAgWJJrz5c5JV748_hYXte1LRm2e7DN1hxYot_IPx3jAFSZSTJeRS-KidiQ6-avqERwpPEO6ZsDvsTKO7ieK2MGZgMZTsjQlFAhDF6qkBMZ_A7tpoVWmgAVZPedrKd_b3u7Okpbtl6As11ukTwf-H4ASXLy-0IAMkE2vcjIgMb4eFMHAoXrC9bACXdQS6PseVoA-9lHd8KzqBl4EUsa8yqXScCd0elpOQ-apf1QzJz67ynyW0Y4ZbYnFRQVjK0EWtzI7Vr-wfb5Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثلث های سه نفره خط هافبک اسپانیا برای هر جام جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/Futball180TV/91186" target="_blank">📅 18:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91185">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niVv6pxQ0GH_Av_2qnECyvpVGomw2GpdwIrUMmuk1KHd955QxM3ok3QvCPhHykp796YTUzFU9EgsuKqS6vSRcCLXY-nyVDdxG3wPofP2TT_RGSxMiTryDWRCusaj5cAJ4jXLAMqhYltrgKBIXHaYXXimSBx7SF60H76Ktlo1TOFfpgzoqoiWnnfM8tPBOlKVLDrzX-woX_ADyukR0m32jFXWgLn_oC9b2JXsk0CjtCEVk2Zb29aaXQLQ_nJOvLPVn7DUAkrGdlng6BokEZ0H0u6NZdpZmVK8_d6VhcwbRPMvue7VlTEuMCOwdfwdE8b6jAiRTLLXAvjqpHlG9IEqgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇦🇷
❌
#فوووووری؛ لئوناردو بالردی مدافع آرژانتین روز گذشته در تمرینات دچار مصدومیت شدید شده و نمیتونه در جام‌جهانی حضور پیدا کنه. بزودی آرژانتین نفر دیگه‌ای رو جایگزین این بازیکن میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/Futball180TV/91185" target="_blank">📅 18:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91184">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64d61c1cf6.mp4?token=aLUO8msBLUauVmxSADwspkcpLSxzfGK0Qc4I3dfwnyLT4so0Ejth0PNQR5HGCBlFZHFco5xDZTd1Mtuu16yvxcSxojksCtivATbqbJyyEO74pPbq1rDL912HGrS7SMNqCfNCElUo1eQ4T6CbP1VtCVXOLIK1Ag1zLgYAIXhKt-At47xh-bqWPc6VKYRsXIgv11eMjosXpSNJHG6lTbaFaJvkLlazVtZ08VtaHzPp0QQZrWJqF85qT5OpdkM1EpHb4UWbQr8KRsz_Hxzm7akMDeEmbWqx7L2gkghqxRnfOwr3NPtYhEZhib1Y_vSNH00BTIL-lX3pcfmBmzRnDQHFIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64d61c1cf6.mp4?token=aLUO8msBLUauVmxSADwspkcpLSxzfGK0Qc4I3dfwnyLT4so0Ejth0PNQR5HGCBlFZHFco5xDZTd1Mtuu16yvxcSxojksCtivATbqbJyyEO74pPbq1rDL912HGrS7SMNqCfNCElUo1eQ4T6CbP1VtCVXOLIK1Ag1zLgYAIXhKt-At47xh-bqWPc6VKYRsXIgv11eMjosXpSNJHG6lTbaFaJvkLlazVtZ08VtaHzPp0QQZrWJqF85qT5OpdkM1EpHb4UWbQr8KRsz_Hxzm7akMDeEmbWqx7L2gkghqxRnfOwr3NPtYhEZhib1Y_vSNH00BTIL-lX3pcfmBmzRnDQHFIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇪🇸
🇪🇸
خبرنگار
: رئال مادرید یا بارسلونا؟
👀
پاپ لئو
: پاپ برای همه تیم‌هاست، اما پرِووست برای رئال مادرید است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/Futball180TV/91184" target="_blank">📅 17:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91183">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
🏆
🇮🇶
🇺🇸
#فوووری؛ آیمن‌حسین ستاره عراق دیشب در بدو ورود به آمریکا حدود ۷ ساعت در بازداشت اداره تحقیقات و مهاجرت این کشور بوده. اتهامات این بازیکن ارتباطاتی با گروه حشدالشعبی بوده و مورد بازجویی قرار گرفته و سپس پس از ۷ ساعت آزاد شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/Futball180TV/91183" target="_blank">📅 17:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91182">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eda27170e.mp4?token=s1fguAUaFCc91Ga6Lazh7rUCB0ssxayVxqN2qcnPmOEfM1wZgGl2mn3YOWDjg_QK-0P7pMwVUa3M3ci3Bzoa5dIhAe_xAqKkIiCShsdgzhkfQX8YzE7AdUJg4-V3aQH1NVQWyFbZWOYrRQ3Zk1SEaeR-Sc9wy-AiK-O5_rbnqSQIC4Prt131R78CNSJc37X-1HI7H2ukkAk2CMWwvzQdPxvGlLgE8RHMl3EXhWXnBzpebW7BXCeC3YLsyF7AEz5d0o6LooZDuesNXQSoznmeDRu20MfGdBCdPAE_0Ob_7YVk6XYoUleeG1_cOV9ElrJm8fXg2IqBtRYYo3Fwp-xCAGQq-IG6m6pPEdFLClw3WjEdvy7cqO1ooNX-d99QHcMuPSsCEm3-zk2t9hLbhpnsrA_RXE-D3UP1rOCSbTd0zD_Ihm0bP61kUncpYWHpc4LO2mxToxILWDUesL7_Am56KlpJUPBPTUYuRMpOClwiw0vQkHEWf-8sAMXP_T5zYn-jTtGO7kCiMpWwQPMvS2DOgi6a-wSRgAaQP5ERwOMYzhRFf5GYSHhNdHplaBcPz9eivvkzSbNp9aXJBNLDg10Lf0_IKWh4nE1MoWRCzXeR5QaLo6cdjqnON8E9p6a9IXXF-uGcSJvD3gMkYnGkmRGgEXzPhZnhaTfCx-ZuI-VhWjc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eda27170e.mp4?token=s1fguAUaFCc91Ga6Lazh7rUCB0ssxayVxqN2qcnPmOEfM1wZgGl2mn3YOWDjg_QK-0P7pMwVUa3M3ci3Bzoa5dIhAe_xAqKkIiCShsdgzhkfQX8YzE7AdUJg4-V3aQH1NVQWyFbZWOYrRQ3Zk1SEaeR-Sc9wy-AiK-O5_rbnqSQIC4Prt131R78CNSJc37X-1HI7H2ukkAk2CMWwvzQdPxvGlLgE8RHMl3EXhWXnBzpebW7BXCeC3YLsyF7AEz5d0o6LooZDuesNXQSoznmeDRu20MfGdBCdPAE_0Ob_7YVk6XYoUleeG1_cOV9ElrJm8fXg2IqBtRYYo3Fwp-xCAGQq-IG6m6pPEdFLClw3WjEdvy7cqO1ooNX-d99QHcMuPSsCEm3-zk2t9hLbhpnsrA_RXE-D3UP1rOCSbTd0zD_Ihm0bP61kUncpYWHpc4LO2mxToxILWDUesL7_Am56KlpJUPBPTUYuRMpOClwiw0vQkHEWf-8sAMXP_T5zYn-jTtGO7kCiMpWwQPMvS2DOgi6a-wSRgAaQP5ERwOMYzhRFf5GYSHhNdHplaBcPz9eivvkzSbNp9aXJBNLDg10Lf0_IKWh4nE1MoWRCzXeR5QaLo6cdjqnON8E9p6a9IXXF-uGcSJvD3gMkYnGkmRGgEXzPhZnhaTfCx-ZuI-VhWjc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥲
🇮🇹
نظریه محبوب:
جام جهانی بدون ایتالیا اونجوری که باید نمیچسبه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/Futball180TV/91182" target="_blank">📅 17:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91181">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtAhMJK_b_kRXss01GVdsB15BpqzMKAFRfFUHvEiyWgD0iMqDF9f1Hh31xxOrYySv10XNAcLdZZb8OfQ6T1ZRqaUqTejhtGRpJB1sTNqg8t8frl_ipxqBe7eWFH7TNqdovC5VF54wcigvjszlWsXHC4uSlmXU646sDXx4ZJsjSg-8_8j83IInYyu2VBTZZ4kaJgtzyXnN1lilXdT5DkMFcyYHCvoNa0je6BRvJZnf_ZSSjd0UqsAGgqDaMs-idmJqVzshBSWUICUdKyZl2KQUpwvhlj29D1XSpU0OutZJs_qm-LmznMuTAIaRsHnKPh_10QPeoKICw3lsP0NPepCMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙️
پاتریس اورا: «نسخه پرایم من در مقابل لامین یامال؟ من او را زنده زنده می‌خوردم. متأسفم لامین. دوستت دارم اما از کریستیانو بپرس، از مسی بپرس، از بازیکنان دیگر بپرس که موقع روبرو شدن با من در بازی اصلا دوست خوبی نیستم".
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/Futball180TV/91181" target="_blank">📅 17:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91180">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4803f256d5.mp4?token=pUbv8IpFGP8nNMxqtJGmh-xiJBalLw1QVeNuNQgEryQE57QWICBktheQT606UWN2L6-3067Wgy0pUOLsWnbKH_UoFF7JaRut9cLRQrtd8frXxs2pVt9yfofBnhF371UnUiAOAEjnTlumJgSf3dcgk_0niUrhcjug8J1qlIseQJB6-ISKFWwLyfubZy9nvmzcXhMCCr9cSQOF-lLylZpVJmn4KCk8Skgq4Qn0SuZMLhRdfb2ahhUlI0zmxH-Gn-Qu0sPGykeyPO0_fVQMTSgE8Kn8Lb7aNDJT686BtFOnphBrjLmLpCD1eCxHJpO_NO6MrFkotwZxgMHMofM-rlwuog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4803f256d5.mp4?token=pUbv8IpFGP8nNMxqtJGmh-xiJBalLw1QVeNuNQgEryQE57QWICBktheQT606UWN2L6-3067Wgy0pUOLsWnbKH_UoFF7JaRut9cLRQrtd8frXxs2pVt9yfofBnhF371UnUiAOAEjnTlumJgSf3dcgk_0niUrhcjug8J1qlIseQJB6-ISKFWwLyfubZy9nvmzcXhMCCr9cSQOF-lLylZpVJmn4KCk8Skgq4Qn0SuZMLhRdfb2ahhUlI0zmxH-Gn-Qu0sPGykeyPO0_fVQMTSgE8Kn8Lb7aNDJT686BtFOnphBrjLmLpCD1eCxHJpO_NO6MrFkotwZxgMHMofM-rlwuog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
تفاوت قیمت خودروهای خارجی در ۱۲ سال اخیر
اینجا هم قیمت فرغون تو یک سال از ۴ میلیون به ۴۵ میلیون رسید =))))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/Futball180TV/91180" target="_blank">📅 17:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91179">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wa0DbPYTmuxiy1803XSQkptsmAWFK_KABhyygWqgkKVZArLuyEbCdRawQVa0zOFHTtZWge0clnXHbZgPJvGGFofTCTS3X90eGZgjAMR02Y4Eclg3Ju_DMdxLsHj9x5LnhWZ0Ftx54SHywpPmm0pAHq-J7-wj2uYIpL6dMWq4RNPX5J5LUfhb2-cUxaXWQ_2CA740JT0vQn72HJBYTDs5eodDbN64ZrHCwet1XJnhNVL7H_KocoKUw35K7yrwtWsRbiWr3_qU5GsZKmXHW9T8OQh1TwUJ-6NAGrpTjuNp4lQFfaGuVxLx-WQHCS_gkSSAJR1ztczVUFLTS-h7NxSy6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه این دوره هیچ‌ تیمی تصمیم به شگفتی‌سازی نگیره و ضدحال نزنه یک چهارم‌نهایی احتمالی این شکلیه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/Futball180TV/91179" target="_blank">📅 17:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91178">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecfebd678d.mp4?token=rWjpFJk581PcAhvINH_N-4XaCKgsL-gqEEyexsOHWLVRYP_yGxZlOc3jOr947h3yuf3vMHUvgh8KadcG5YkOBTll1l-uoGciVtQGHPFemuLHehvq42or7auGCkpreh3rbPu94AuL5-9TQIrDndey8k0eANCHrQaOEB06XA0eoZGWIn6RvrulACrVWMRXuBDLBWkbnfUjg8btanjfNnmtcUPcMzx9rE_zMnKevf255ljsYBZnLAw-ABL1hOnytMxX4Vb3t9ueF_Pu78ECU1hlrxrLnuA8kcHeIuzt1Hu-j1Z29-9srnL7FB_DVeM3SzQL6lbB_TAi7_ng0WwSVSRkZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecfebd678d.mp4?token=rWjpFJk581PcAhvINH_N-4XaCKgsL-gqEEyexsOHWLVRYP_yGxZlOc3jOr947h3yuf3vMHUvgh8KadcG5YkOBTll1l-uoGciVtQGHPFemuLHehvq42or7auGCkpreh3rbPu94AuL5-9TQIrDndey8k0eANCHrQaOEB06XA0eoZGWIn6RvrulACrVWMRXuBDLBWkbnfUjg8btanjfNnmtcUPcMzx9rE_zMnKevf255ljsYBZnLAw-ABL1hOnytMxX4Vb3t9ueF_Pu78ECU1hlrxrLnuA8kcHeIuzt1Hu-j1Z29-9srnL7FB_DVeM3SzQL6lbB_TAi7_ng0WwSVSRkZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دم جام جهانی یادی کنیم از بزرگترین غایب پرتغال
😭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/Futball180TV/91178" target="_blank">📅 17:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91177">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a09753bd04.mp4?token=FDojfLiWFx1uTgjnaWg698HjfkxqTvYk6j11ZEdrHXMQJozf5qOvsnUYm_N_m24xTYNa4vo711J9nAHV6P1BRLWa_r-DAm6eEDSl_jRG-q6aDPDvodIxnNQ_ltUIanZI7k6rOAYtK0zuqWjpNM9Tmyd_Ho6zR7RaMMwPB2EBhiSHY4_cPcU7q1RzpqQBIS1ByBkbSl2zjnVeVopxSjQUX-cegnQDtk1UCti_9jJlNca1nJgpugH3ty2w8p9yM3BxOZwSrusWXtGks_aJj4FPwg3Ng3FHYIkTJI7JsU4mS8NO46fkP8YRafrb2c7dHx1EJhLhqNZbG8Oclip2ZzYNGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a09753bd04.mp4?token=FDojfLiWFx1uTgjnaWg698HjfkxqTvYk6j11ZEdrHXMQJozf5qOvsnUYm_N_m24xTYNa4vo711J9nAHV6P1BRLWa_r-DAm6eEDSl_jRG-q6aDPDvodIxnNQ_ltUIanZI7k6rOAYtK0zuqWjpNM9Tmyd_Ho6zR7RaMMwPB2EBhiSHY4_cPcU7q1RzpqQBIS1ByBkbSl2zjnVeVopxSjQUX-cegnQDtk1UCti_9jJlNca1nJgpugH3ty2w8p9yM3BxOZwSrusWXtGks_aJj4FPwg3Ng3FHYIkTJI7JsU4mS8NO46fkP8YRafrb2c7dHx1EJhLhqNZbG8Oclip2ZzYNGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
پرنسس لئونور دختر پادشاه اسپانیا که آقای گاوی زحمت کشید بهش پا نداد، بلند شده رفته سربازی و اینجوری داره فشاری روانی از دست دادن گاوی رو خالی میکنه
😂
😂
😂
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/Futball180TV/91177" target="_blank">📅 17:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91176">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pH9yMoz5DGsLtTXHz37BErYCGv0-H8dQltC9Oga7eUCtsoIJGEBrVcQoMa1A6JMjVGM4jTuA2fRQ2VdeiVziRGtUPAO4UnaY8RrDdTl5sgCzRt8ivxHaZLePrUFAJwNBoJSxlM_LgZxwk2XGnHCLiEoaQb3aNwmiPw-4LZS9adYIkEeZiYaFwT13lDO9Ui5Bpzx4l_SHpJka23zh2mELdOSy5NZEq8a2h6_7A6xobk9NDxZBm6s62Mjq2fp63vUKNVu-R2EQPHweHOeNMYI4WmGfCbNCnKsKZRFENz2CncAmM8dXU4dWIrzxCfuhbLrUbVoavOvHB-pAweyfITGC2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
از مایکل اولیسه خواسته شد تا بهترین بازیکن فعلی شش کشور مختلف را انتخاب کند
🔵
مایکل اولیسه:
🇩🇪
آلمان: جاشوا کیمیچ
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلستان: هری کین
🇪🇸
اسپانیا: لمینه یامال
🇧🇷
برزیل: نمیدانم
🇵🇹
پرتغال: برونو فرناندز
🇦🇷
آرژانتین: لیونل مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/Futball180TV/91176" target="_blank">📅 17:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91175">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c576d4593.mp4?token=MjYADQQfGq0Hm5dzwaC3gpH84FxbvB-IBR0dGdbFPLtqZdShrRzMS8bA7Ql1nFvpVhaedQgMt4imr1peFnlh8mcwzP7f-FkHLlIqK1ssvuC7h28tuaNjtqapu6X79P0tGFfoecKIWtvX11af2jbSwdQK5urvYv2O-ij4razgBJqyDihbPyyPHBJukwuK8dGeSm4C2NW9WVRtHUrY1-vPoi9xDibZ7YBGWvWICMZ4End9XRJq591vhfZNzPhTbg9qYgym1XBnAk2usLkOlcYcdqUwn4brfKT1WJzAddUyVSBJMGB2JJYt3mqLbztcz2U-WWqQKcGF0kkw-i7q54n7CIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c576d4593.mp4?token=MjYADQQfGq0Hm5dzwaC3gpH84FxbvB-IBR0dGdbFPLtqZdShrRzMS8bA7Ql1nFvpVhaedQgMt4imr1peFnlh8mcwzP7f-FkHLlIqK1ssvuC7h28tuaNjtqapu6X79P0tGFfoecKIWtvX11af2jbSwdQK5urvYv2O-ij4razgBJqyDihbPyyPHBJukwuK8dGeSm4C2NW9WVRtHUrY1-vPoi9xDibZ7YBGWvWICMZ4End9XRJq591vhfZNzPhTbg9qYgym1XBnAk2usLkOlcYcdqUwn4brfKT1WJzAddUyVSBJMGB2JJYt3mqLbztcz2U-WWqQKcGF0kkw-i7q54n7CIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
روایت چلنگر مترجم سابق برانکو از تجربه همبازی شدن با بهرام افشاری در مرد عینکی: بهرام از شدت گرمای هوا، نزدیک بود بیهوش بشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/91175" target="_blank">📅 17:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91174">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
#
فووووووری
🔴
حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/91174" target="_blank">📅 16:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91173">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZy6rnjtkFjnXXyBtDggwE8uHAl7Uzg5w9pf3Z3N-dBjd90y7xGBghJLCenXyS5f0I7S97zzODdXLlMzCgpzeKZQ-n7LYyeYbLr07UNTqUnCSQPpcL0tL-VsIbKiP9QyzL2wxG4NeCEKUXl9tIr0XlLY1GWBeejL18swA-jyNp533IE2HQmBEbx6DpEvdm-u5B4el_wFWNQABOy2WbMHxk7EZzEg8BT6eYRAmhH5j2rbeZeN_9KFKs9kJCBQq1B_EQiPcAspFUt0iQhpSgFLm4S0hhIBP5PyRzlHC4DNIiMtvKyY1zZ7HO6kt_C-S4FiqWH_LLz408jMWWwZ5nnpCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
طبق گزارش امروز لكيپ:
❌
تقریباً تمام بازی‌های جام جهانی (۱۰۴ بازی) ممکن است به دلیل شرایط نامساعد جوی، در حین بازی به طور موقت متوقف شوند!!!
❗️
احتمال وقوع رعد و برق، تگرگ و حتی گردبادهای قیفی شکل (تورنادو) در مناطق مرکزی ایالات متحده مانند کانزاس سیتی، آتلانتا و دالاس وجود دارد.
‼️
همچنین خطر گرما و رطوبت شدید در شهرهای ساحلی مانند میامی و هیوستون وجود دارد. در حالی که مونتری ممکن است دمای بسیار بالایی را تجربه کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/91173" target="_blank">📅 16:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91172">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAq90tZ2rNVUTsMmcf6gv0owP1F-ZX4_V0OTO-He1Ifwmtlb0txzUSOZFMMscdsIaOt0VK1X0k0Fb5ozVbyVswkE29dazb_Xj1SpxlysMQPv-IAzqgNKh43cUhi1Wn_hKHLDVYag6u_fC1LZCfi3T-JAfIqkFRmqwmK-lVRpkbz3w3pV0XsWjA3HlDzpTy-eE2vhzhrUpH4BGp16qBKPhXe0k9qHo7wGfaR6umho5O6K1OS_5YZYxeGwGy3D-GkM17REx2yeEjRecl6dG9YCgROA5d37t605VPqYdR6L3XbQUet8frpVtk8PMzjXt79MU3L6XuoSk0i9o-BGxygI1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
معرفی‌مختصر تیم‌های گروه B جام‌جهانی
🇨🇦
کانادا
:
لقب:
Les Rouges (قرمزها) / تپل لیفز (The Maple Leafs)
ستاره‌های اصلی:
آلفونسو دیویس (ستاره بایرن مونیخ) و جاناتان دیوید (مهاجم یوونتوس)
سرمربی: جسی مارش( انگلیسی )
تعداد حضور: ۳ دوره (۱۹۸۶، ۲۰۲۲ و ۲۰۲۶)
بهترین مقام: حضور در مرحله گروهی (تا به حال موفق به صعود از گروه یا کسب پیروزی در جام جهانی نشده‌اند و به دنبال شکستن این طلسم هستند).
دوره قبل (۲۰۲۲): با وجود بازی‌های خوب، با ۳ شکست در مرحله گروهی حذف شدند.
نحوه صعود: به عنوان یکی از سه میزبان مشترک این دوره از رقابت‌ها، بدون حضور در مسابقات انتخابی کونکاکاف، مستقیماً وارد جدول مسابقات شد.
﻿
🇨🇭
سوئیس
:
لقب: Nati (تیم ملی) / شیک‌پوشان قرمز
ستاره اصلی: گرانیت ژاکا، آکانجی، زکریا
سرمربی: یاکین
تعداد حضور: ۱۳ دوره (یکی از منظم‌ترین تیم‌های اروپایی در حضورهای اخیر)
بهترین مقام: صعود به یک‌چهارم نهایی (در سال‌های ۱۹۳۴، ۱۹۳۸ و ۱۹۵۴)
دوره قبل (۲۰۲۲): صعود از گروه و شکست مقابل پرتغال در مرحله یک‌هشتم نهایی.
نحوه صعود: صعود مقتدرانه به عنوان تیم اول گروه خود در انتخابی قاره اروپا (UEFA).
﻿
🇧🇦
بوسنی و هرزگوین
:
لقب: Zmajevi (اژدهایان)
سرمربی: سرجی باربارز
ستاره اصلی: ادین ژکو (مهاجم کهنه‌کار و گلزن تاریخ‌ساز) و ساد کولاسیناچ (مدافع باتجربه)
تعداد حضور: ۲ دوره (آن‌ها برای اولین بار در سال ۲۰۱۴ برزیل حاضر شدند و این دومین حضور تاریخ کشور مستقل بوسنی است).
بهترین مقام: حضور در مرحله گروهی (جام جهانی ۲۰۱۴).
دوره قبل (۲۰۲۲): غایب بودند.
نحوه صعود: آن‌ها با خلق یک شگفتی بزرگ و حذف/شکست تیم‌های قدرتمندی مثل ایتالیا در پلی‌آف سخت قاره اروپا (UEFA) توانستند بلیت خود را برای سفر به آمریکای شمالی رزرو کنند.
🇶🇦
قطر
:
لقب: العنابی (عنابی‌پوشان)
سرمربی: جولیان لوپتگی
ستاره اصلی: اکرم عفیف (ستاره تکنیکی و آقای گل جام ملت‌های آسیا) و المعز علی
تعداد حضور: ۲ دوره.
بهترین مقام: حضور در مرحله گروهی (۲۰۲۲).
دوره قبل (۲۰۲۲): به عنوان میزبان مسابقات حضور داشتند اما با عملکردی ضعیف و سه شکست پیاپی در همان مرحله گروهی حذف شدند.
نحوه صعود: صعود مستقیم و مقتدرانه از مرحله سوم انتخابی قاره آسیا (AFC) به عنوان یکی از تیم‌های برتر قاره که با پشتوانه دو قهرمانی پیاپی در جام ملت‌های آسیا، با اعتماد به نفس بالایی صعود کردند.
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/91172" target="_blank">📅 16:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91171">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eze874oKvzeeV6rZsu8UimAKgaQs9CUNoyt5RLeLivrQdUBRv3fVCE9p4ogxodSuS5zlhySnT8pSLbEdua1NAMeQ-avcz_cD7sTSNf13IH7i6TKZyUefZMACE9H6smN_tTU7tbvHjR9BscibUQ5PjljJLoIT9QsJmXlJ0bEW4sBf3u22zPDAyH_qJrTdKclWE3ieywNvgvZWqjRjf4qmXyVsAC4bk-8nHRoTuJlvnFhJ2kx0VusV4ZY8irWrIKeIG5k8c6vSUd7mj3FXRmtOsZp14s3yueUuu3mpAI7fXtTlckR6gKetTJw1PJGtoMQwBiGlKcA4_nrfJcyWeVhRmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس‌تیمی تیم قدرتمند اردشیر قبل سفر به مکزیک
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/Futball180TV/91171" target="_blank">📅 16:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91170">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nG20bGYtOsMAmI6NJC60K7xINxjJU1H2-xOT5sKUCsFEhEpWZituejSUX-lndouwaDJYNsNopW-aVKKHINJnlCoe0OdRJTP-lRHe6ZWk5kS5X-J8D60DYeLm3T-O69pbPXTE-9JPgo-pCtto7MFPtVS1Vn_ffW0KIfN13UjLI2VZeKK0XA52MSFbzUYnsH6XQtnTV_P-LRya9vgtNKfutpbxvEA7lxYsbGvwJMwIC8ugawYK_Gi0-VMzIdGucAoPchgAGqgH_MhjvcnnzdKQx-cFHGiRsNY3TMADSgA8MVgscVwKrtZO-qT0IksLvpfNZdhCfAZ-tUk_q2CwTH1A4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سامان قدوس تو عکس رسمی تیم قلعه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/Futball180TV/91170" target="_blank">📅 16:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91169">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mNrOl_xbyN2sAqTRvpWPzg3rPLPDwgsfRpTGKYtNDgG5q0ZmlXtmlk_WdfULtEpQHgGgAZdrzkoDK3Ae8hCijpfAwTdSfoCDBS8gpGF1ViNbjU7LBMso3WrPwI6FJKy_SQ-Evc77TmF3bD0tICEQUa2RTsBpyWS3xwJeONSR0v2vEBX-0Zq9_buMTFHLzqFukDjdWfx3PX3ZPdcrjGV91BA1UUydC2vHYtPQixdFSE91OFDLnkEKHmousAaoHjDn8GJ3CYmoyGkgTGi_5HDtWdAdNA_mkY4UKUaL7XwjfqMWNmS1DuZOSq0LXb2RToz65Uvtq-Rlj9uLesvatnTDhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
؛ به نقل از موندو، دو تیم سیتی و یونایتد خواهان جذب بالده از بارسلونا شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/91169" target="_blank">📅 16:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91168">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a405dfd62.mp4?token=vKp76OEagXc-Zsuxbi7i8i-BRqSQlm-jhuGME3GFmt9UMO3rArhcmkP9G4WZ_8uK9NZnfnLzcorY0RJ36-GtiE9_DMq6_Ca85UcdGVW0sHS-cY1HQAJGBmZp_H9VAyvdLbyZCisIHpbzJ6XtVN4laD9bMQJbP9BPsJOsQ7akV64ubVpMQsRWRK-nkRgeUihonqvhM_X_0mNjQlu30Hg0-gQXR2tmzvSBipmCXZOU6xiktfCcxz_Q611Li1ndJjbyAp7HFHr9yhNAgryc6oVa3hrKB-B0NsFUg0ZsEwFyNaGB7P1r45i1nxmkCEFMmiojbp57hrUKp9PTAaMhUAbYaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a405dfd62.mp4?token=vKp76OEagXc-Zsuxbi7i8i-BRqSQlm-jhuGME3GFmt9UMO3rArhcmkP9G4WZ_8uK9NZnfnLzcorY0RJ36-GtiE9_DMq6_Ca85UcdGVW0sHS-cY1HQAJGBmZp_H9VAyvdLbyZCisIHpbzJ6XtVN4laD9bMQJbP9BPsJOsQ7akV64ubVpMQsRWRK-nkRgeUihonqvhM_X_0mNjQlu30Hg0-gQXR2tmzvSBipmCXZOU6xiktfCcxz_Q611Li1ndJjbyAp7HFHr9yhNAgryc6oVa3hrKB-B0NsFUg0ZsEwFyNaGB7P1r45i1nxmkCEFMmiojbp57hrUKp9PTAaMhUAbYaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
وایرال شدن عجیب و غریب موزیک شکیرا برای جام‌جهانی در سراسر دنیا؛ واقعا محشره و همه نسل Z باهاش ویدیو ساختن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/91168" target="_blank">📅 16:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91167">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGybo2KC-z6uGfMMNxMyqYLNl79Mv2oSIV0y_K--wVvMTGsoma2_yxlcShbhSkWTJT2R-xzBm828ZGpro96_rFMRScjOPBT3daw4sTi-i9a00YtmaJIGz4LCv5dHx2ksM9UAeBjHS-O5clyrr2YLWkRJb3-xw0USU6aPhsC2_nCb1BYgP8Z2KQTXH8I8j4uCs4TYHeoVb4_gcyfauASfu2sxOqyKPFX-X38Yepg-g3ebTRqE1mi4r8YG2WJvQAJ5Y09Rosu_7a0NgXpSd3g8OBPViOoY9EiPRkcXfzwknJJ3KjdQjWNLKum7ZT6N4Mpjdi3Z12u9k3oBKxZEwYTtOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
🇪🇸
🇪🇸
فلورنتینو پرز: عمرا بیخیال ماجرای نگریرا بشم. انگار بعضیا حافظه‌شون خیلی کوتاهه. این بزرگترین فساد تاریخ ورزشه و من تا آخرش میرم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/91167" target="_blank">📅 16:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91166">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5532e9c9d8.mp4?token=NDsX7J9MeFAwUYuuXZD5Xs59P6sEqhyEixoSsDskKAPxEnkmR3W8FKTPL_B_tQaBDmtqB8jRNd8-lDmmZMesATD7pVlwQXd3DFx7niC_cm17dFcaeazhEhLynfpbQ9QkauqvvGIthqeM89ExQY8Fa97zdfUlizx_QWx8ChuNqjogg_ySsoGL1MNL-ZSXZEgOuik-19lgbny5W3tr9eW0vSfs8NajGZ0dgm8Qw8DTko1KHnz4DBHWhW6DbGNhcU1UguD_YsiwRjCL4NJaCAXWsXM94L3dsb3thrMvSUpGiYNUJ-eLq9HHhr96K1SMTEzc3wSh256pUu-QWJtHWYFiSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5532e9c9d8.mp4?token=NDsX7J9MeFAwUYuuXZD5Xs59P6sEqhyEixoSsDskKAPxEnkmR3W8FKTPL_B_tQaBDmtqB8jRNd8-lDmmZMesATD7pVlwQXd3DFx7niC_cm17dFcaeazhEhLynfpbQ9QkauqvvGIthqeM89ExQY8Fa97zdfUlizx_QWx8ChuNqjogg_ySsoGL1MNL-ZSXZEgOuik-19lgbny5W3tr9eW0vSfs8NajGZ0dgm8Qw8DTko1KHnz4DBHWhW6DbGNhcU1UguD_YsiwRjCL4NJaCAXWsXM94L3dsb3thrMvSUpGiYNUJ-eLq9HHhr96K1SMTEzc3wSh256pUu-QWJtHWYFiSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
پارت سوم ورزش در خانه؛ حتما استفاده کنید و واسه‌ دوستای گشادتون بفرستید
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/91166" target="_blank">📅 16:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91165">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea44f33918.mp4?token=u4Lo5qNLCIn2MkovK1gaZSIWp3juR4wqZpkPHEMIghb78UEtoBzGJDUAjr23vPr-vx-TEz38_ibOpd12ZaXJx_egHXzS_GKfvkpdgFGRwCCEw_mZ1__7SkjcpsRGtQdNjfyQyWm5QX09weIDNEVxubQDWDNauYTBpysAhzSjkioE46b7G8hFzSR7xCKVFJP158qobV13fMvqtA5r_QdS_lSRtv6dT9-UH5M1SVqHUbQTuAqVXzGOD3gA4gYMnnYAKCc1youpn6RtBBXBajwaQ6DcAMgpKioRfQaPKy0OyrA1eFYdoRHtZ1f6sPGpb_WmnV46Tjvx2V52_jQeFlnKIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea44f33918.mp4?token=u4Lo5qNLCIn2MkovK1gaZSIWp3juR4wqZpkPHEMIghb78UEtoBzGJDUAjr23vPr-vx-TEz38_ibOpd12ZaXJx_egHXzS_GKfvkpdgFGRwCCEw_mZ1__7SkjcpsRGtQdNjfyQyWm5QX09weIDNEVxubQDWDNauYTBpysAhzSjkioE46b7G8hFzSR7xCKVFJP158qobV13fMvqtA5r_QdS_lSRtv6dT9-UH5M1SVqHUbQTuAqVXzGOD3gA4gYMnnYAKCc1youpn6RtBBXBajwaQ6DcAMgpKioRfQaPKy0OyrA1eFYdoRHtZ1f6sPGpb_WmnV46Tjvx2V52_jQeFlnKIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
🇲🇽
در آستانه جام‌جهانی، معترضان در مکزیک، تندیس‌ بازیکنای جا‌جهانی رو در جریان تظاهراتی برای افزایش حقوق‌ها از جا کندن و لخت کردن
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/91165" target="_blank">📅 15:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91164">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e51373c01.mp4?token=Z43sxIliNHGS_Z-Ek2adgIJwjIDN8lAiffuSjFpekhNV304oGjzE9OJO6vs0WkIBWz0_1YCwQGL8UDRpwB1OmU6MCb8jmjH7f85gn1u_oFipPb5nKE3ISa64d3XspwHExDyXV4T5gK6Z_AsOapFQFrPfv2em4ALlvcEOg7D2u_kQmLVZw4ZDCsMt-ZGeFnXhgQ6xYjjBzPUZliszC7v7vVchrieubB-SXtfLs8AvO7yyC-j1FT5BU8LUtj34tes51XCHN2rh0g-uKLrTLrQN6fhBf-6YTsX08eh2x1nWARuqMLf01qiwo-fX48bPjm6UAApVhbYjE5ET3w-eBkmhXXtyFVikXO6y81mEjlbNGL4rVLrBTxd9rM_pC37eqTcp8EisUKYcatEeROfw53iNtfxZ54wQmeDMyiHhWoR_SVloeO6_sDCJtN07t0oGP7_zBgRZgq8e2woGze_xUteGlNZ_nm28WQ8N5wa5A1ZQYxGRx4Sy7Vfy8xiyjO8RQ1g69aNPdKdp3p1uCke0WXjZKwS76rwOoFtPh96bJeVfR9xwM7pIpXpJCb6gG-X4g8UFN1wJxm7MDq7ON8LbjSC0trT8IVaa3cZdOZt8jd0VZfnytK1hU3MnRlQkXzt4CMqmSAXQOdsRP6C0nE10ERYjO0FOoN_vNOC-w6kPMbhUADA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e51373c01.mp4?token=Z43sxIliNHGS_Z-Ek2adgIJwjIDN8lAiffuSjFpekhNV304oGjzE9OJO6vs0WkIBWz0_1YCwQGL8UDRpwB1OmU6MCb8jmjH7f85gn1u_oFipPb5nKE3ISa64d3XspwHExDyXV4T5gK6Z_AsOapFQFrPfv2em4ALlvcEOg7D2u_kQmLVZw4ZDCsMt-ZGeFnXhgQ6xYjjBzPUZliszC7v7vVchrieubB-SXtfLs8AvO7yyC-j1FT5BU8LUtj34tes51XCHN2rh0g-uKLrTLrQN6fhBf-6YTsX08eh2x1nWARuqMLf01qiwo-fX48bPjm6UAApVhbYjE5ET3w-eBkmhXXtyFVikXO6y81mEjlbNGL4rVLrBTxd9rM_pC37eqTcp8EisUKYcatEeROfw53iNtfxZ54wQmeDMyiHhWoR_SVloeO6_sDCJtN07t0oGP7_zBgRZgq8e2woGze_xUteGlNZ_nm28WQ8N5wa5A1ZQYxGRx4Sy7Vfy8xiyjO8RQ1g69aNPdKdp3p1uCke0WXjZKwS76rwOoFtPh96bJeVfR9xwM7pIpXpJCb6gG-X4g8UFN1wJxm7MDq7ON8LbjSC0trT8IVaa3cZdOZt8jd0VZfnytK1hU3MnRlQkXzt4CMqmSAXQOdsRP6C0nE10ERYjO0FOoN_vNOC-w6kPMbhUADA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
یه ویدیو از بازیکنای پاری‌سن‌ژرمن موقع ضربه پنالتی بازی با آرسنال منتشر شده که نشون از زرنگی شاگردان انریکه برای گول زدن بازیکنای آرتتا داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/91164" target="_blank">📅 15:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91163">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c5176bab.mp4?token=Q0avA-sA4HWDGlUI7OY-r_7Q_WrtEbPMjEgzHd_K2WOPJOO7jo0redSVLHWIa3pGme6uNzdjL_-1auaOalCCJ65pG7meeTieu1Q1KR99fki7RHBuuvwCci7xtSygBkXM4uzgiLZ_UWxTMQty25rxrB8kxiyNTSPaBxO3sAWUusbxIcKnhKRBmmll30YuG7u2dbT_v-8RqtgIVFFK4CF5w6Gkuy1EBnDBOuhfIsMxoeRGAVSdXXMwvUohhRjwAvids6M06tnpXWJFcBzgPtUNxbDygiDyfzxyEQkFaqnsABX3zgbrZ6s3iZxTwCVC2K3MXlApGvo98ZjwU1GOiV-4ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c5176bab.mp4?token=Q0avA-sA4HWDGlUI7OY-r_7Q_WrtEbPMjEgzHd_K2WOPJOO7jo0redSVLHWIa3pGme6uNzdjL_-1auaOalCCJ65pG7meeTieu1Q1KR99fki7RHBuuvwCci7xtSygBkXM4uzgiLZ_UWxTMQty25rxrB8kxiyNTSPaBxO3sAWUusbxIcKnhKRBmmll30YuG7u2dbT_v-8RqtgIVFFK4CF5w6Gkuy1EBnDBOuhfIsMxoeRGAVSdXXMwvUohhRjwAvids6M06tnpXWJFcBzgPtUNxbDygiDyfzxyEQkFaqnsABX3zgbrZ6s3iZxTwCVC2K3MXlApGvo98ZjwU1GOiV-4ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
💥
رونالدینیو به یامال: این راهی که تو شروع کردی رو من آسفالت کردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/91163" target="_blank">📅 15:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91162">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBPKey0AWKWG7hadyn5G9nKtnSwj0xd0yoyi2kC63ZS1QKJTZ-S-uLvbnLyWUEL7jo1ZMb4S6xkrO_dP7fBhVdn5z3YiU63Xndw7pvSI7QftWkiATDcaTYZB4_EWknKAl25RocIOdI5BmKJbQKtahhhJMFGuMZBbDMRDP1xIF5_Wg9LgKGxmgYHsOmW945nZ2MjAgp2fd5DyBaXqjDvpLwwm-322AeVAzFC03RfTohrBMoSAOUDDjSnZT8w9vEXr9QQIXdE7rjkoAVbQJJitNZKLg6UNxuRtuXUnaTMasdoCZUsk3-1lZWJq2F_AkOzxVR2kPoArYmEoGjNp5r8iXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇫🇷
عکس‌رسمی تیم‌ملی فرانسه پیش از اعزام به جام‌جهانی و سفر به کشور آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/91162" target="_blank">📅 15:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91161">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebc14c7273.mp4?token=LCd9Uoj_w3mVU2k8xuFljV0msvbhc8O-QdqCyl4EbPNqGywKhhwikQWpjRr2WCc40fB6nkyfkfggTbtUVd14WCtaV6tSFA58UjC2sYe68KeVRVrcd_c9KMPBqp15Mo7NA0mX3kjQOMC2lP-Dzjvv4qCswqlrAYku_2rEuUcK9EDX9kOhzSjiSMUEbnL-1XQtMFLrinYKb-e4PYuU0g4bJzTyiZIEiVSOOaTF1-MKwRRuohi7tHN2WHs8LizQsTyp4WeQzifgre4R7gGR1ag9crxtcYREwusXNYxraSDXHK0Kf2ZUW5xravSIHPu2lTNfJwfdcamla8zAQMRdjDHLvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebc14c7273.mp4?token=LCd9Uoj_w3mVU2k8xuFljV0msvbhc8O-QdqCyl4EbPNqGywKhhwikQWpjRr2WCc40fB6nkyfkfggTbtUVd14WCtaV6tSFA58UjC2sYe68KeVRVrcd_c9KMPBqp15Mo7NA0mX3kjQOMC2lP-Dzjvv4qCswqlrAYku_2rEuUcK9EDX9kOhzSjiSMUEbnL-1XQtMFLrinYKb-e4PYuU0g4bJzTyiZIEiVSOOaTF1-MKwRRuohi7tHN2WHs8LizQsTyp4WeQzifgre4R7gGR1ag9crxtcYREwusXNYxraSDXHK0Kf2ZUW5xravSIHPu2lTNfJwfdcamla8zAQMRdjDHLvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇵🇹
یه سری از دوستان نمایشگاهی ایرانی از بیکاری اومدن برا پرتغالی‌ها چالش جام‌جهانی رفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/91161" target="_blank">📅 14:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91160">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🎙️
زلاتان ابراهیموویچ:  صحبت درباره قراردادهای رئال مادرید در این تابستان خیلی خنده‌دار است. فصل گذشته قرارداد بستند، هزینه کردند، جشن گرفتند، صفحات اجتماعی را پر از طراحی‌ کردند. سپس فصل با ویترین خالی به پایان رسید.  و حالا فکر می‌کنند بعضی نام‌های جدید…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/91160" target="_blank">📅 14:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91159">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucRu9PiUlbXc0-ziElXKWzG6Rw5Lak-ZgABv1CuQGDrjXD99sYOnIGwoKhiVPiINT_Yld0EpaGa0ch_9-U8adADm_i46HkKOwjXuhIGd8OgkLLGupe-hKPqatJm2tk3iWcggfAv0ccVVEyRFuZyv9Ha11P77nXUSLmAbVaJ5BNj0HccgEqY-blgG_D2w4JPTZvM8h-GayvOx6vbBvNXkpzdD_BGbUPufwU29KOtqXoQznLHE6tjU85IFIDakm6_bM8wWG-8gE7hGaj9Uwgn92Qiis-otuBCbisJaekuVJtj0otR14U-1ZLk-bCvBG8Wq8NyW4rupP9LhSFiMMf-9WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙️
زلاتان ابراهیموویچ:
صحبت درباره قراردادهای رئال مادرید در این تابستان خیلی خنده‌دار است. فصل گذشته قرارداد بستند، هزینه کردند، جشن گرفتند، صفحات اجتماعی را پر از طراحی‌ کردند. سپس فصل با ویترین خالی به پایان رسید.
و حالا فکر می‌کنند بعضی نام‌های جدید ناگهان آن‌ها را قادر می‌سازد تا با بارسلونا مقابله کنند؟ حتی اگر ژوزه مورینیو خودش برگردد، مشکل خیلی عمیق‌تر از این‌هاست.
اگر بارسلونا پروژه‌اش را کامل کند و بازیکنانی که واقعاً نیاز دارد را بیاورد، رقابت بسیار سخت‌تر از آن چیزی خواهد شد که بعضی‌ها تصور می‌کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/91159" target="_blank">📅 14:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91158">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd80803a67.mp4?token=bAEsUD2YedeMXk1kyQkO6QlmhOnfP9-sq1KfBYCvWldKBFNsyXfmL0pUH8Ze0d_ya2_lgEx8SRlmYJbixq_si1B-tqLON3w4bL2odwXKx_Oa3GM3J5XYWgkixG6W0v9Ipx2CLj_xI8Imj3C2lBWqcLqSV4Q5IFfW5aOBqm-JG6dSHKY-vhGzoy5GOu36GJh_dEufhkVnWQqhl0njLCZ20m6FxJ2UWWwYW5ZCwloZEk4hhHjVFKS-ovK5Vd6xrRevevIkBQ2SKG8jPM_CgiLLje1396AINCApRlahfxKs6K0BJCFOkYzJtyJBjvNUMcF18NzLHDEpbuHVDcXh-UpJNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd80803a67.mp4?token=bAEsUD2YedeMXk1kyQkO6QlmhOnfP9-sq1KfBYCvWldKBFNsyXfmL0pUH8Ze0d_ya2_lgEx8SRlmYJbixq_si1B-tqLON3w4bL2odwXKx_Oa3GM3J5XYWgkixG6W0v9Ipx2CLj_xI8Imj3C2lBWqcLqSV4Q5IFfW5aOBqm-JG6dSHKY-vhGzoy5GOu36GJh_dEufhkVnWQqhl0njLCZ20m6FxJ2UWWwYW5ZCwloZEk4hhHjVFKS-ovK5Vd6xrRevevIkBQ2SKG8jPM_CgiLLje1396AINCApRlahfxKs6K0BJCFOkYzJtyJBjvNUMcF18NzLHDEpbuHVDcXh-UpJNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇾
تیم ملی پاراگوئه هم به این شکل سکسی بدرقه شد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91158" target="_blank">📅 14:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91157">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gweyh3Z90BKMXbTKR67bd1RhtU5h1rNmRbVd-ZpVa-ITykvYjV5eqhiA-QkGfKiEnkB-wZGqyz69EC3-TDo6751PTV5XdNcJEtB8y7r6sZ38EmC3hfBzGx0v4cbQrmUKd0aBiWmEfpww9nAwI7jSMTvaQ5z_EdWSm9WcqyI1SZL-GHc4sg-_MIhKKmcJzPCK23Ju2ePzI1G5jSqqTKPsikyp-_waqFKzjJ1am_jvGYf34WaGcRysC70bQFfi8IbojgJcztubYFwqDjCZhGPOF8lTI8g-IEnnX370_fB-EL-UeH8f93SBDu0-L9FIE1ilTpz7did4IErvftKrf5fBUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خاله دلیتا تو جام جهانی مجری خواهد بود
🍆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/91157" target="_blank">📅 14:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91156">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJtYwfClyNmiwoTtxPI6dZvr-xa2Sod1IszwQ2bqzLA_men7X-UOWKq6eRmB3PrAKS1urSCOBCmv2CPDVibdMOR3hJePalSBnp2C7rSmacAc5fmxSGM_M3mdBplmqYQ4Mu7gb20VuoPGhvdwMdbgL5yQKAwSavOGXW-Hgp4gq6VSf4XYRn_ZLT0Dpy_CDSOvZJ7kgaaiWCAVSHxp6OnPElF_xbsxFCAGosKpw4v-S_h0tH3u383Uq0S9tWWp5iRq5iOJYAMO8_Jifa40HkqIKmPIu08bpaCiyP4UW5yQSD4OPYTmFztpAylDR5x43wnRlsoiJTRlNpC-mMt3yGRIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">11 سال مثل برق و باد گذشت..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/91156" target="_blank">📅 13:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91152">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SdGE1EeWGNck2qT6dCx8Wb7r2NFchTNSD_hFn2BpbWXsNGyy-k_uC_U6pDxjVvdeQuxL0W8aMJcA8vALVtJCiZ1Er4ZXeLKap8q4tuEG1AvH5JgyXBQ7Ih0mSqWUsPREcbWKVDR0DmwqNGLw8yQNySET3sYb9fcBtECKyf25iEPaqaZzOI80JiVO8nJuwLuGeRHI8qbO7CoBHxWodRfn3Xarr0UpUaLAMuY0hj885NzfVbIAaglmij2PbAK5-onj6D0c1b8GhE4zFbWaxNqcI7kXwA6ktuPLYBa0cMmUwDQmQe90JVokQVWbz2CW8f0q7D2QzVUGnRBU0_YHViU7RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aYVW3ryfu07r8xL8OjLcQJkK89BLE9dAUram6keVba9k2Pd1cNeegqmJUZTpNPHn5SJNhhqgFsfu47qQ3ZNVIjM0ZcVMP3q47pfcrtTSGrvqkfW59-cFz-3lMkpfk7QD_eejtaH4A9Hre7GXDziJaRBGAAbqrgCJohcSUJmJ3ZsBCnaXfp3xP6WtrNZoyuduLUhJT8Dveh3i_YC5wJFdSAt1SlPLWb-zd-JEm2gW6nBe1Kw-5STbkmV-nYM3uUTTnodtXmHeRXUKGTIMA6iOfrZJIwoZrDC-8m31JuQ_edTQn3XUIHtk80XI55CCH-b2nkcc6ijwk6fOFxdzVq9Y_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZImLL07aXPRlUhilaMQJNN5EfpsBtH1UH483p3OKj8L-F2HluR9bplFcPjEjQTCpb3as4uGUFc2bGd_Fvw8urE4n1GJvOg11LsLm1cKn0GcOi4nW36QZ0Ak3PMuvSv96wN1b4n3yHXE9HJsUMQ4YwigUVz1Ywr6FQiZebsrmFVQU5c40-nkJ591BCpHvcIcGHyJgpB67nPLjfvjXSjoY8mZsY2cLE-VSPSudkG0vRMSVsxbdBLoRSzQ4yaLPqo0ZFRWCCZo6gdojR43X1qr1mVkuuOjvL4KBe-blWOPEtKgomEx_NGvES9ufvO8Z8bwBnP-opFNe7tjXqFb62qGbew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SDAIOHYnCcuDGA8ZWc7w85Y84ReJoo7VKfAWM056aeFrZD0J7hXZGevHBcJW5JVCFv26Zc940csCzePng9blq8WIjK_UDap-JwXw43H5MEyGi23eZy-a_Rn5UgQqROG3u9XbMWSGdlrZq_0aTIrlRaNyihb3GPYgdmoDCp2TTqRb9MQ29Wm-fLrsTIXCb22z3BGWuSbVwx-5RzsOJtEJpCVHs2IlCLrU0N1b1FsY27QaFU1hHfmKOa0RhFmd0-XsSLlaqWq9xzA-H0KQrhUcqvBkalKtpa5rSpE7l84FHZMUWtRYzBQo3KJzKHcxQx1cwyWu_WD-a_Hs8Nx1rmh0cw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🤯
مادلین رایت هستن که بعد از خداحافظی از فوتبال تو سال ۲۰۲۲، به طور کلی وارد OnlyFans شد و درآمد سالانش از حدود ۷۰۰۰ دلار به ۱ میلیون دلار رسیده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/91152" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91151">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_ePsXRWeo0WxxqsLN3Umh3mJ35cEh5zF6XJEhA37nmqHh9ElzqOHo64kIIpo32LNSGUA55gI3NPUT-wqoL1GuGt6_spa1OuT9akWj-TUiEYVkThb71pbYjdivs2kZFkQ5F2-kNqmaG-XLu4SKiVUX61ofMoEwIBuAiLwX4GsttV9OI2SwO2Q6fHXOp4xmHMhluYyxK0BloDRFUyUTBEVe_1DeCwsqQrNuvh_jSlnu9YPBsDO2K6H-rUrbFG2QD3V2X1mbc_C-Nxin1-VpilexOiG7EsTBksFvL6kGVQj5do4TUCHSm1F8uTIYggxdSWYOiq1lejZayFywxzYdT3mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇫🇷
عکس‌رسمی تیم‌ملی فرانسه پیش از اعزام به جام‌جهانی و سفر به کشور آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/91151" target="_blank">📅 13:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91150">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
‼️
موسی‌جنپو بازیکن استقلال قراردادش رو فسخ کرد و یه پرونده جدید به لطف علی تاجرنیا برای این‌تیم در فیفا باز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/91150" target="_blank">📅 13:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91149">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J64Aa2ddxYMNZhhbzlwdSNs58y4zk85aVEPCgZfVXYRhHtoAGKIBdwit0YhI9pE0UT5oO6azu7QW4dileGA9cCFeMdD3IR7HGSwOuZbudoMbApyzp8Qe99jgxBFFpdgDZsH-PCZEoWWhQ-1WUGZuMFXICXNbadiBod3-KcbcpQ9f4ouwp47gsM8GnrIJ_obEAlw9ytjpnNf-845xbo5WEk9jSAMND-P_3WfYfrXgg8um7eTZoqcXdv7mlng9c38VYiLgIz8XGtx1iUfb8ukCpuZlhXnS5aOyU2PjJk2q9GPZX4bKYGcdpWNDqcS0NFYHNZ99fvVqOblZGhXJI424DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از ترانسفرمارکت، یامال و هالند با ۲۰۰ میلیون یورو باارزش‌ترین بازیکنان جهان هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/91149" target="_blank">📅 13:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91148">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
#فووووووری
#اختصاصی_فوتبال‌180
؛
🔵
ابوالفضل جلالی در لیست خروج باشگاه استقلال قرار گرفت و فصل‌آینده جایی در آبی‌پوشان نخواهد داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/91148" target="_blank">📅 13:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91147">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5H3m9WiWezbWX9cNSaDjJWj6rkLRlE-56PpTmRTG2OKVQqX-VBY9gfBPurx7PcAwZ1CKD3DygrNt8yqNKIknfJ9rrk7dWUqLd99MmFjKR108_fb8eXvAFYxuwvrFMIS6uDm2sUZ8ivFFjMn47x-GNdpxRaHLYzVXOgJ_KHE-O0KInm1URuTAaI4-BL1QzSEWDC5CvfpcRguT_qO19VF3rNf-UpDPi6lV5hjI36vbJXLDuSJJG0J33rtIjPQmj1YKiFqEo_UEvyzxyTtT0LkaHzRJhtCfAdsRbJZioTC1-v8yNVdElkz0iwdxM92oDXZ34wuWuii_TLb-bBI_lEMqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🇩🇪
اولیور کان مدیر تیم‌فوتبال بایرن‌مونیخ:
🎙
اولیسه باید از خودش بپرسد چه می‌خواهد، رئال مادرید او را در گذشته غرق می‌کند و به بهانه اینکه ما در گذشته بهتر بودیم فریبش می‌دهد، مجموعه‌ای از افتخارات و جام‌های قدیمی، اما بایرن مونیخ آینده را به او می‌دهد.
🎙
رئال مادرید باید دست از زندگی کردن بر اساس افتخارات قدیمی بردارد و تلاش کند در آینده پیروز شود. در گذشته نام رئال مادرید بزرگ‌ترین بازیکنان فوتبال جهان را جذب می‌کرد، اما اکنون اینطور نیست و آنها هر تابستان باید بنشینند و بازیکنی را برای پیوستن به تیم قانع کنند، ما گذشته آنها را نداریم و آنها آینده ما را ندارند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/91147" target="_blank">📅 13:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91146">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
وزارت خارجه آمریکا:
فقط برای افراد ضروری از جمله بازیکنان و کادرفنی تیم ملی ایران ویزا صادر کردیم و افراد اضافی جایی در آمریکا ندارند و نباید از امکانات ما استفاده کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/91146" target="_blank">📅 13:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91145">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiOM5CL92d9Oz6OcClQqPxDDmmHPKdKgXqX62Hejl4ojrkpneyRhvfgkSAXxFtR3C0msvAckvFBg_4ii0oatbSWBSzGPiGKXxu69sx5LKc5K2ZBhxLJzciPy-b8TZYaXnIGUwJiTffSQtEpn_B8h-pea5lZsLNMw6LTkBDYCQ_g0_ApLcTwexpyzD8c6zz54uhDeyJIaG87WV0J5qG25J3uL_BDpaIFFhKp7Yf5js_Yk_4i87wiC15-YzId-VKC46Nbe_xC_of8zEfle6fOgqXEGwf0rop30E3GCcsFOwxnXCQRo1xBCHDi6RzDBDhjds5mj_rmhC3axnbdVZ54Nlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
معرفی مختصر تیم‌های گروه A جام‌جهانی
🇲🇽
مکزیک:
لقب: El Tri (سه رنگ)
سرمربی: خاویر آگیره
ستاره اصلی: سانتیاگو خیمنز (مهاجم میلان)
تعداد حضور: ۱۸ دوره (یکی از باقوام‌ترین تیم‌های تاریخ مسابقات)
بهترین مقام: صعود به یک‌چهارم نهایی در سال‌های ۱۹۷۰ و ۱۹۸۶ (هر دو بار در زمان میزبانی خودشان)
دوره قبل (۲۰۲۲): حذف تلخ در مرحله گروهی (پایان رکوردی که ۷ دوره متوالی از گروه صعود می‌کردند)
نحوه صعود: به عنوان یکی از سه میزبان مشترک مسابقات (در کنار آمریکا و کانادا)، بدون شرکت در بازی‌های انتخابی به صورت مستقیم صعود کرد.
وضعیت فعلی: آن‌ها بعد از تغییرات پیاپی روی نیمکت، دوباره به خاویر آگیره باسابقه اعتماد کرده‌اند. با داشتن امتیاز میزبانی و بازی در ورزشگاه مخوف «آزتکا»، فشار و البته پتانسیل زیادی برای صدرنشینی در این گروه دارند.
﻿
🇰🇷
کره‌جنوبی
لقب: جنگجویان تائه‌گوک / تایگرهای آسیا
سرمربی: میونگ-بو هونگ
ستاره اصلی: سون هیونگ-مین (کاپیتان و ستاره سابق تاتنهام) و لی کانگ-این (ستاره پاری‌سن‌ژرمن)
تعداد حضور: ۱۲ دوره (رکورددار بیشترین حضور در میان تیم‌های آسیایی)
بهترین مقام: مقام چهارم جهان در جام جهانی ۲۰۰۲ (به عنوان میزبان مشترک)
دوره قبل (۲۰۲۲): صعود دراماتیک از گروه و حذف در مرحله یک‌هشتم نهایی مقابل برزیل.
نحوه صعود: صعود مقتدرانه به عنوان تیم اول گروه خود در مرحله سوم انتخابی جام جهانی در قاره آسیا
وضعیت فعلی: کره جنوبی ترکیبی از با تجربه‌های باکیفیت در اروپا (مثل کیم مین-جائه در بایرن مونیخ) و جوانان نسل جدید دارد. آن‌ها به نظم تاکتیکی شدید و سرعت بالا در انتقال توپ معروف هستند و مدعی جدی صعود از این گروه به شمار می‌روند.
🇨🇿
جمهوری چک
سرمربی: میروسلاو کوبک
ستاره اصلی: توماس سوچک (هافبک و رهبر وستهم) و پاتریک شیک (مهاجم لورکوزن)
تعداد حضور: ۱۰ دوره (با احتساب دوران چکسلواکی سابق) / این دومین حضور آن‌ها به عنوان کشور مستقل «جمهوری چک» پس از سال ۲۰۰۶ است.
بهترین مقام: دو عنوان نایب‌قهرمانی جهان در سال‌های ۱۹۳۴ و ۱۹۶۲ (در دوران چکسلواکی).
دوره قبل (۲۰۲۲): غایب بودند (نتوانستند جواز حضور را کسب کنند).
نحوه صعود: پس از ناکامی در صعود مستقیم، از طریق مسیر سخت پلی‌آف اروپا (UEFA) موفق شدند بلیت حضور در این جام جهانی را رزرو کنند.
🇿🇦
﻿آفریقای‌جنوبی
لقب: Bafana Bafana (پسران)
سرمربی: هوگو بروس(مربی باسابقه بلژیکی)
ستاره اصلی: لایل فاستر (مهاجم باشگاه برنلی انگلیس)
تعداد حضور: ۴ دوره (پیش از این در سال‌های ۱۹۹۸، ۲۰۰۲ و ۲۰۱۰ حضور داشتند).
بهترین مقام: حضور در مرحله گروهی (آن‌ها تا به حال موفق به صعود از گروه خود نشده‌اند).
دوره قبل (۲۰۲۲): غایب بودند.
نحوه صعود: صعود به عنوان یکی از تیم‌های برتر منطقه آفریقا (CAF) پس از یک ماراتن انتخابی فشرده در قاره سیاه.
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/91145" target="_blank">📅 13:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91144">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GA_UVDOLhS0zeR_LSSLTXXQ1kdpEtZ7oSODeRLpI-WKTxok0dQhd0jQGtwfLy-td0KWwbQGPU02DmYQ2cfPNFSbxaLrNZppy2Mzqnqi7FcR39mySSB0oT5gLQqVk9RreIe4KxxKsgEiONEL_isiUnQmXiOjneA3S3zirdHTmAkzaNP9YD-rzVcbXAKP4nd5gySSJTNjjl6t8_WQYdkw7-oshBdBgknI-C-kMQGp9P8fBEBuPr_O9ApTR0MSOlrT_QXiWyfFjgqlmfHZvsOV0r3VfnRnp7rsp4KZH4URAgvD0TNA-NuJ54_ZqPrTeh8B9QWEFGZ2qq64JpF3oQSCqNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاکا: «من علاقه‌ای ندارم که فرزندانم بدونن که روزی بهترین بازیکن جهان بوده‌ام. فقط می‌خواهم مرا بهترین پدر جهان بدانند»
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91144" target="_blank">📅 12:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91143">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bR2tknDsG5e1AaAzAIgbWU6h2-qthOrZwb3aloJvtcu_sq2J7CDJSYp2G5skk2b72K-xn9kZtawoAk9n8wNVXhhY0i5rjMfbsOW4Hp90ZafCbifzkHNUw35YsBUs565YqUoTCdDssW4_y6YqIvPq9fVxcfMvd2X4RWfA1D6bEtKiY-CEYsFf-oNnvZKG810dcB_5I2FUtL4WoutyfDorZ33jdbr_DNAPmiUWW-OBycOnQQlQxMdEItgEBPMul07DLHjMNZERraJ4_ibxG71Um8QHOhHcFmthB-KF2jLDZy6jT3PN4-zc3WUZ1aKBeJAib8j5NETnOI6Z0YHLBYCfgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
#فوووووووری
؛ بردلی بارکولا برای تمدید قرارداد با پاری‌سن‌ژرمن به توافق رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/91143" target="_blank">📅 12:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91142">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c06a46347a.mp4?token=esVn-radDNKIbMFVBaCAoSLBi5_cEWgSrIdb3hDrSJQnaHsUknJ3UOE0aRboPCT9d0qVyaoFFSX1JocZGaV7sz964nynBvg-k0PujLt5VjF2GZ55wXr4T-nYdL38srA9jM18lafgwfMSt5n0CmZUrx5wHsoC7g-9ASxmmymOxlLl3puGAxwZ0CLTjH5wRPkq-mFHTidnyD_aogrtCvhJNF8yQTcrM4_2WltrO2RVWhEDgCXQki7aDvhsoR2Apq2-o4TozzRBQVjwOdabruv07aKab1jQMWpOzBHQGKfOK6jV9jL_7U0osGfeQRK6f3vT6mAKq44upfHt6MabDrFiqzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c06a46347a.mp4?token=esVn-radDNKIbMFVBaCAoSLBi5_cEWgSrIdb3hDrSJQnaHsUknJ3UOE0aRboPCT9d0qVyaoFFSX1JocZGaV7sz964nynBvg-k0PujLt5VjF2GZ55wXr4T-nYdL38srA9jM18lafgwfMSt5n0CmZUrx5wHsoC7g-9ASxmmymOxlLl3puGAxwZ0CLTjH5wRPkq-mFHTidnyD_aogrtCvhJNF8yQTcrM4_2WltrO2RVWhEDgCXQki7aDvhsoR2Apq2-o4TozzRBQVjwOdabruv07aKab1jQMWpOzBHQGKfOK6jV9jL_7U0osGfeQRK6f3vT6mAKq44upfHt6MabDrFiqzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرژانتینی ها از الان تو آمریکا کولاک به پا کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/91142" target="_blank">📅 12:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91139">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d49e89d4ab.mp4?token=asyisFJpU0uS49VgtxBNAjiGwAvvZ7K7kasvNUfIsg3CKtxcriN9Jam-doM4bRZDlRwrIcMuuNsad5Pl47A-fk8OE4Yo39AuVnRFsQP-EXHovcTztBZ9cm5U3aFgLwmL2ul4TkDSXgQh-C7iRxZn-8zNcS8TfJynjxIPLEmI2RbEO4yuqYc238s3hhVSQhXfXRaWx0zk_W41aCX78i7LXP7ijxjTRvoEdqWjPMr0YvX1FiZUc4BX736cRu81YEYSlfSreSv3nP_YrzggVdqfWrcnT-q1lEbCC2-W2luEHfnwryoSRwReuIGL3do4JamxDbA4r0FeOAJe18oMHlnBNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d49e89d4ab.mp4?token=asyisFJpU0uS49VgtxBNAjiGwAvvZ7K7kasvNUfIsg3CKtxcriN9Jam-doM4bRZDlRwrIcMuuNsad5Pl47A-fk8OE4Yo39AuVnRFsQP-EXHovcTztBZ9cm5U3aFgLwmL2ul4TkDSXgQh-C7iRxZn-8zNcS8TfJynjxIPLEmI2RbEO4yuqYc238s3hhVSQhXfXRaWx0zk_W41aCX78i7LXP7ijxjTRvoEdqWjPMr0YvX1FiZUc4BX736cRu81YEYSlfSreSv3nP_YrzggVdqfWrcnT-q1lEbCC2-W2luEHfnwryoSRwReuIGL3do4JamxDbA4r0FeOAJe18oMHlnBNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
امروز در کشور، دانش آموزا به تأثیر قطعی معدل یازدهم توی کنکور، دست به اعتراض زدن
«خسرو پناه حیا کن، کنکوریو رها کن»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/91139" target="_blank">📅 12:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91138">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2773ec48db.mp4?token=A0Gtr-__nuWUzUw_oVdWKDWDWrZhp1hwkD3rOrqOLeg00ft-zigMyIN29_uY4fMvLOHKM9cp1B9aTiH09vJZfOltNE0AOFfsfMqLrcR56iIOT94C0BnbB7U63s-I0HpE0khbr-ZlO7tgfeqTkoSZeIUTIkg1gptNCQ98T3vT5j0MY6jl0e_dqwhwLW9cWBlKOKzHU6rw9w6IXqVx3IBdUpj9es8uVNA_2ZPig0jyupuJXzHZnqwA1B9LNKVO-EhoklxQyuPFRV9O2jFBX81FfluTLy0JOkM1nSz-tAIlCM_CQAVPRA5zPQqabGp58rlrmUQHesmH7Lo6i-V6hPy6FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2773ec48db.mp4?token=A0Gtr-__nuWUzUw_oVdWKDWDWrZhp1hwkD3rOrqOLeg00ft-zigMyIN29_uY4fMvLOHKM9cp1B9aTiH09vJZfOltNE0AOFfsfMqLrcR56iIOT94C0BnbB7U63s-I0HpE0khbr-ZlO7tgfeqTkoSZeIUTIkg1gptNCQ98T3vT5j0MY6jl0e_dqwhwLW9cWBlKOKzHU6rw9w6IXqVx3IBdUpj9es8uVNA_2ZPig0jyupuJXzHZnqwA1B9LNKVO-EhoklxQyuPFRV9O2jFBX81FfluTLy0JOkM1nSz-tAIlCM_CQAVPRA5zPQqabGp58rlrmUQHesmH7Lo6i-V6hPy6FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه قهرمانی تیم ام سی الجزایر تو لیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/91138" target="_blank">📅 12:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91137">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-e4yDA_cPSsig_65DdXqlTpHsZQgFnWBTWRwn-Fdl1Z6gxnXWhdGOS9MloSUwbqMOo2EBt_X9qVE2LNPLK1776xWGA4fHaFTwmyfNdIRfI41UE9K21UpTcgg41M5qWYhT_3NnPv8dJucTHXWMVUGUzbDROSh8t9-JA_f1rWIjRyWN7UVPxZMMBFVPZYcOMzjNol8FKbd2TQkCWRhopd6EeoXm7KAab8srpxJpKZarPKJc9dCiNcxsIyte-i_W_ndXmq7POQj1i6nracO--vfxIX59IK9HaaRafhskO4r07WbYgTc6lcKGWOKuDabnSLtG-5iga5RISrE_gQzq-LVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
لیگ‌هایی که بیشترین نماینده رو تو جام‌جهانی دارن؛
انگلیس با 165 بازیکن با اختلاف در صدر.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/91137" target="_blank">📅 12:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91136">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be064ede1a.mp4?token=s5SPjNgcgngpQk6RTnqB-n6Z3G6Ze2rm8hxt8P_uCRVY-TUlMlb9IB5cZirqoF8II4AuVAlgk2A9zuyQ2d0kh7h4Gs9TD89H8IgQYsLyY62f08LiQkyziXEPt_JK5sWVAMOmLKDFExHid0H7JazXGceaU05sDs-Tv6lU84-yZiPhojPvDaZLNumJ6BhYKL7LycbWr8ZivIEVTNmqYNO_PwxCysFf0cZ_4iX5VdzoTeN0TjQr7RqFGqcasAjd-C2AtohMMW8Xv76WGbNV0-mepvXZ8wxnFsPwrQgrCsG4UB64v-sdxNxcad3hlLf7-XgDAT15IUxj0E0-4gztji5r0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be064ede1a.mp4?token=s5SPjNgcgngpQk6RTnqB-n6Z3G6Ze2rm8hxt8P_uCRVY-TUlMlb9IB5cZirqoF8II4AuVAlgk2A9zuyQ2d0kh7h4Gs9TD89H8IgQYsLyY62f08LiQkyziXEPt_JK5sWVAMOmLKDFExHid0H7JazXGceaU05sDs-Tv6lU84-yZiPhojPvDaZLNumJ6BhYKL7LycbWr8ZivIEVTNmqYNO_PwxCysFf0cZ_4iX5VdzoTeN0TjQr7RqFGqcasAjd-C2AtohMMW8Xv76WGbNV0-mepvXZ8wxnFsPwrQgrCsG4UB64v-sdxNxcad3hlLf7-XgDAT15IUxj0E0-4gztji5r0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرکی به ایشون گل بزنه با من طرفه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/91136" target="_blank">📅 11:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91134">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R7pDwI8WWoPYCEEQIBGE3Iq2haXU_JHWMCWHkDh2MbY8I2n08al61wVmOfhSPVtWiTtHCyAxWUpgxBvw7-dIt74k8hjzydW1g_vE2KmIlK-6QYDQySIV7XpNyCDE3uVrF49prlWP96VnP5rC_oc5vxLgJH43ONv2aeLKZiAY2UR4PlSd8IwYMkcJ-yXtjvTquCDow600X32WuFScwVfixwaBt2bQ_VYFmXy-MYwyudHYAJFZTQo2UH4AkM9Jm4JOsrJJMO7JHuPotwT8Qn3HZ2TsvmdsPz5FxZAC5BL9cjGXdXwpQUWhrS6XMldu5vumVw9hlRMZCNtVdPSHqNuPZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q7UJLu7vL_BVfqH5u3qACaIFrA6czAH4glnu1bj9QJUZ0YS3cnFy99ZzqTZnBjxb8ps5qhFNWy-1bt_pO8H4ne8-ZypxjCH2yw1KKWSL8okhuYS71LzMB-bsC1yZWHRXz7mbbClH2u9XG734eJPPNvM3GlKm6_yfh8DswPcu9yP0qVXVGcthGhfTZZB_Ip1W5K_U9-iUZLOZj2KDCJ61uHeD9IV2WBQxuJNkYkvB4fVPnIhRcKPh80KYqujgZ7z84H12BeNvZzvOcivAnBlTAiYxkZP7BpUx8yaspCsk-jcZX0s8uZGwjPfOdsE2fYw3q-wJQAWf-MYWEllEw_Shpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
این‌چهره که مشاهده می‌کنید صدف طاهریان بازیگر اسبق تلویزیون و‌ سینما چند سال پس از مهاجرت و کشف حجاب، روز گذشته با انتشار استوری اعلام کرد که به ایران برگشته و خبرگزاری‌های داخلی هم تایید کردن
🙂
🙂
🚬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/91134" target="_blank">📅 11:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91133">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cc3fc13c7.mp4?token=shP2sMX1vx4EQYXltmiaMhbfIi0VlhLQLdnyUB-slReG7PztT9oXdYwu2IhM_9gyqNzcN4Z3zStBdXz-lp13OX1pv-rvW7TC54RKWQM1r3I-TGM4-oFMvyU-jsH4Pclar0VJ8X0XJnzdTw-9RONz_dm9lq1UjI1IhHq50yUy8uM5NKckBMk229ymro--pD09D4wiIjQSrj_DVUAklzt_e0Xy8EKw6Rhbklj00fflXo94ZncPpIXo2l0eFpX2L50C9iRkAeWhm2uGBNx7hpAEuqL_yaDhMw7Hw9IPxKVDWBFlcHB3RRi-xpOuatAkwjjXrs_95yp2VILfJIrwxHX_tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cc3fc13c7.mp4?token=shP2sMX1vx4EQYXltmiaMhbfIi0VlhLQLdnyUB-slReG7PztT9oXdYwu2IhM_9gyqNzcN4Z3zStBdXz-lp13OX1pv-rvW7TC54RKWQM1r3I-TGM4-oFMvyU-jsH4Pclar0VJ8X0XJnzdTw-9RONz_dm9lq1UjI1IhHq50yUy8uM5NKckBMk229ymro--pD09D4wiIjQSrj_DVUAklzt_e0Xy8EKw6Rhbklj00fflXo94ZncPpIXo2l0eFpX2L50C9iRkAeWhm2uGBNx7hpAEuqL_yaDhMw7Hw9IPxKVDWBFlcHB3RRi-xpOuatAkwjjXrs_95yp2VILfJIrwxHX_tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دوستان حکومت اومدن یه سری تینیجر رو دورهم جمع کردن تا با بساز و برقص از تیم قلعه‌نویی در آستانه جام‌جهانی حمایت کنن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/91133" target="_blank">📅 11:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91132">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/112d86fcd1.mp4?token=sDqKHFjruIogVTTeb2YYcy4yMiB5g3ZaiqlmkkoUrCok48DmtFGZ-ehkKIKrMTJ_rJEJAMa5fmsrL7ZkML_Zy1STuLVpn8yijS2ZgI63RqrpSKZukvgICkPM_NSaIzOtBL-y3xqpgUWJKL7O9Svpc53uQaAUkGl1EfjxkO6KKg72Yff4BZds65Y9ICs3P2_tM-yHaJ7ZUf2CxMkTaFqn26--Ey43Y-Zg9gNgu1qEesAzO4hScvpkibJRsq-iPCoKd8zAwLge-U5o9zAEP7kgiSRLEOrIlGVapVje7_QPXZIwsRXMzdJEsp9Vrzdr2GFFaqmKbNQsjlOvTa5GYAqb1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/112d86fcd1.mp4?token=sDqKHFjruIogVTTeb2YYcy4yMiB5g3ZaiqlmkkoUrCok48DmtFGZ-ehkKIKrMTJ_rJEJAMa5fmsrL7ZkML_Zy1STuLVpn8yijS2ZgI63RqrpSKZukvgICkPM_NSaIzOtBL-y3xqpgUWJKL7O9Svpc53uQaAUkGl1EfjxkO6KKg72Yff4BZds65Y9ICs3P2_tM-yHaJ7ZUf2CxMkTaFqn26--Ey43Y-Zg9gNgu1qEesAzO4hScvpkibJRsq-iPCoKd8zAwLge-U5o9zAEP7kgiSRLEOrIlGVapVje7_QPXZIwsRXMzdJEsp9Vrzdr2GFFaqmKbNQsjlOvTa5GYAqb1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
وضعیت لیگ پایه استان اصفهان: پیشنهاد میشه اگر افسردگی شدید دارید و مدتیه نخدیدید این ویدیو رو تماشا کنین
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/91132" target="_blank">📅 11:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91131">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=IDMO0JY3nx_i_W8vM3_Cdxy5hSG7RemxlESZ8T7d0cLfqQCfO7pOj1bbCdVh3441GQS6wTtOehzsu0IkcfvrmTKujlQ8mJAVfSTVbHiNo0Wo2h5HUgjfwghJo_VWFl5A0JGWBX4eD5b0oeo2CXY0sjp2GPDJHqPmZ9Wn_6XgU-YaPt2ektirSuVbZQFNb6X4CRDJNGErMvvm7vk61tiYn6G0pgnQ1u4O-BQmQXH8Wtt1bgr_Cgo6mBs-QKh6BroSxnyfPzUQr1kJffWB7zPQd96GYCV_pBCiJhk-Y3nrkj5QTfBxAvi7TEnrGxJJv4Cuxz3cr6USUdsFdPbntl0xhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=IDMO0JY3nx_i_W8vM3_Cdxy5hSG7RemxlESZ8T7d0cLfqQCfO7pOj1bbCdVh3441GQS6wTtOehzsu0IkcfvrmTKujlQ8mJAVfSTVbHiNo0Wo2h5HUgjfwghJo_VWFl5A0JGWBX4eD5b0oeo2CXY0sjp2GPDJHqPmZ9Wn_6XgU-YaPt2ektirSuVbZQFNb6X4CRDJNGErMvvm7vk61tiYn6G0pgnQ1u4O-BQmQXH8Wtt1bgr_Cgo6mBs-QKh6BroSxnyfPzUQr1kJffWB7zPQd96GYCV_pBCiJhk-Y3nrkj5QTfBxAvi7TEnrGxJJv4Cuxz3cr6USUdsFdPbntl0xhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمعی از هوادارای پرسپولیس صبح شنبه رفتن جلو فدراسیون و از مهدی‌تاج میخوان این تیم رو به آسیا بفرسته
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/91131" target="_blank">📅 10:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91130">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nn0BXD-xp1B-n3TAnhWVwp5eE0zUZMnRXz_HF5YLUEYOOpiTqMcRRKJd25ebxBd2rTjUQI_LD5yYjxxJ7W5GxW17_9IkFMnV4rNXOFNVGq33LvO6rpGyWymREeWm8ZlPTyFBRO-xnMSoC9oen41ao8Gg9YNmXem0OmBQDIH_kfpw1i7lkqMk81mEuAYw0M5q22LGS0Jbm9PUHc-hKZcsB8hUfKwtuAqcPMQFXhzwK59H5kfzzGzO6BblwqA_DdDEUzZwt-kro8fWbkZQqvZq1E2D0FZku9y3-SqBrA5MggzIj0UsxbjbT2xCRnvuMkiQMVUGaqTUFUgIrVllqBhRxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇦🇷
❌
#فوووووری
؛ لئوناردو بالردی مدافع آرژانتین روز گذشته در تمرینات دچار مصدومیت شدید شده و نمیتونه در جام‌جهانی حضور پیدا کنه. بزودی آرژانتین نفر دیگه‌ای رو جایگزین این بازیکن میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/91130" target="_blank">📅 10:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91129">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🇺🇸
مهدی‌تاج: آمریکا شیطان صفت درخواست ویزای منو رد کرده. از این موضوع بسیار عصبی و ناراحتم اما کاری از دستم برنمیاد
🐸
🐸
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/91129" target="_blank">📅 10:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91128">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ss6T0DR7HiJ8fWqTqeqdvlWXnwzZlf5oAsPlgYMOFHtylEYStfYwD_dduJgY0SgIM5ruustZkQkUG5_ogICLtNy1QP2vCFyRkBUGB4SSSyWwogayPrTgqRn7HmryBbSsemN3rSN2ZF2TkgKAakoZolI_1a5PcaRnAGuCvz74L9NqbpkocLnfAe0ahwEn_cs64W0CPXi6W9MOe14iyOq7M5BGtU19bM44kxH4hIdf0FG_GVu7bZ6qzg8-7vwwU7ASfoKlrIEOIYLZvd65MPHIJgJ_5CJLHEZp_0ITEoyGUmEH5Y-jdgZGPMqgQk_8MuUaMt7G4QQsVc5PMI6H6K-gTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
🇮🇶
🇺🇸
#فوووری
؛ آیمن‌حسین ستاره عراق دیشب در بدو ورود به آمریکا حدود ۷ ساعت در بازداشت اداره تحقیقات و مهاجرت این کشور بوده. اتهامات این بازیکن ارتباطاتی با گروه حشدالشعبی بوده و مورد بازجویی قرار گرفته و سپس پس از ۷ ساعت آزاد شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/91128" target="_blank">📅 10:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91127">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🇺🇸
مهدی‌تاج: آمریکا شیطان صفت درخواست ویزای منو رد کرده. از این موضوع بسیار عصبی و ناراحتم اما کاری از دستم برنمیاد
🐸
🐸
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/91127" target="_blank">📅 10:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91126">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/728bdf34c7.mp4?token=jjBO5X6oo1Z6i5pfmkPGhySMofQxSetL6UkI4-DAMPUXAW4hpcJl_GpQfxTX0244DxgfirvGpHpdWZ5fMAQFF7FZqX6vVeQOAti71r-rE9TmgsS-XtRb98SMRNT3cQL8PaLv8ulGDhuOkEIHSeNRn_1uO9Foz1TN_kXSoIs79aC32FwzUw_n6qDVKw7L2N47TMVU8zAVlsiyN9tePO6gLBHIKFzchEKfvOlXSwfRycvPSTdVXy_vpQ1m6Naiak4hBC41YUE4MoekUwpK3LH4h0D2afRzYcNtqE_PhcCGVHK-O8RC7YCkx--By1JEfjrymtj52f3r_rfzva5d6jxZmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/728bdf34c7.mp4?token=jjBO5X6oo1Z6i5pfmkPGhySMofQxSetL6UkI4-DAMPUXAW4hpcJl_GpQfxTX0244DxgfirvGpHpdWZ5fMAQFF7FZqX6vVeQOAti71r-rE9TmgsS-XtRb98SMRNT3cQL8PaLv8ulGDhuOkEIHSeNRn_1uO9Foz1TN_kXSoIs79aC32FwzUw_n6qDVKw7L2N47TMVU8zAVlsiyN9tePO6gLBHIKFzchEKfvOlXSwfRycvPSTdVXy_vpQ1m6Naiak4hBC41YUE4MoekUwpK3LH4h0D2afRzYcNtqE_PhcCGVHK-O8RC7YCkx--By1JEfjrymtj52f3r_rfzva5d6jxZmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زور این دوست عزیزمون از هالک ایرانی بیشتره
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/91126" target="_blank">📅 10:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91125">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
‼️
پشت پرده اخراج شبانه و غیرقانونی علی دایی و دادکان توسط محمود احمدی‌نژاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/91125" target="_blank">📅 09:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91124">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06eeae197.mp4?token=dMu1OamEKfTNa5E29ZfRsY2iqfE3o46rPQVVaRI5vt3lBAwcuWSMIrKhC8VTlgtsb_BYrI5ISEzZ9DBlVmo8sy2nE45nn8sIScZD6v-V5vBJTUkKXHkY0ib_MGSEPWf2AMhC7ZOHvi2q0hOjidyGDisEYljYKNexBMhV3932Ekwp1yEMtdQCsWLDaVHm3AoLwzsq_8byl4oauJiNqXUWWKoTqQft796V5AiOqPJ55IuJU9hknUYv0yJsVEhrOE2YDGVwSVfPo91NY6_KmkIOl6oGrnCNApzSB8bLju4VlvlsKWmKdlLQhgsi1I8qOpDCu3BoiDUEn3OmRClIndSvjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06eeae197.mp4?token=dMu1OamEKfTNa5E29ZfRsY2iqfE3o46rPQVVaRI5vt3lBAwcuWSMIrKhC8VTlgtsb_BYrI5ISEzZ9DBlVmo8sy2nE45nn8sIScZD6v-V5vBJTUkKXHkY0ib_MGSEPWf2AMhC7ZOHvi2q0hOjidyGDisEYljYKNexBMhV3932Ekwp1yEMtdQCsWLDaVHm3AoLwzsq_8byl4oauJiNqXUWWKoTqQft796V5AiOqPJ55IuJU9hknUYv0yJsVEhrOE2YDGVwSVfPo91NY6_KmkIOl6oGrnCNApzSB8bLju4VlvlsKWmKdlLQhgsi1I8qOpDCu3BoiDUEn3OmRClIndSvjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
👀
خنده‌های نیکی‌نیکول زید سابق یامال به رابطه جدید ستاره بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/91124" target="_blank">📅 09:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91123">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/806ce63d62.mp4?token=OmdJLl82YZub6ek8gkx22PHRwexpBtQRUl2sT5NlW0xeJW7IJrnyGbHCahpr9vkVBcwT9qirBb5XGK-0CCSM5dHH6Z41xk7yEaQPN10Pit8Eb3hWZta7oypfnuvKzA2Nsy3IPZC_1rP5_i9NuIJYFcowCm3_7IURUfRBwgPoCXcLpCc0qqPPKSWtCoyF3MV2vlsUiezpyelkvKZsmvB9E46zmiLYYiwW1F3rA03whiFCk1uKADyZhhDkaQk0x9T19orWtXkv4e3r3B7gbzHodUJt9VJr-mQBVT-VrUi42H56430_X66gbde7BVkLZvfH-f_n5Wtwg0-AC2UnA6q-Lxi4A6QEfsGWPnIPm4m6J6b-STQlyWOkP9mCBXbXeu9fZT8npt-0B79azw1BkZnDANmoXHpsX5C9hn1NJVzTaIr8hr6qpThZ-IWB4Jt9I7xtecNqWTLf4LllO_rMA6wdxRHDzEFhs0ha9Hx6FLiYnHfkUEjT_azn8loqBo0_XBtao96sVtup2vx35TpjoLCkLPZQqGtELKL2ukHxUUnoX-ftizWwCT2_PTr8qH4eEMNiIZGB_05XlIl9IHXcYPfvdqlVNMKHqWpgmjCiQxR70xLW-vxlSrYlVv1pslngxpKeoh9BqAVssmMyHvBoybDjYeHcbm9l5yRnEWbioZiHpCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/806ce63d62.mp4?token=OmdJLl82YZub6ek8gkx22PHRwexpBtQRUl2sT5NlW0xeJW7IJrnyGbHCahpr9vkVBcwT9qirBb5XGK-0CCSM5dHH6Z41xk7yEaQPN10Pit8Eb3hWZta7oypfnuvKzA2Nsy3IPZC_1rP5_i9NuIJYFcowCm3_7IURUfRBwgPoCXcLpCc0qqPPKSWtCoyF3MV2vlsUiezpyelkvKZsmvB9E46zmiLYYiwW1F3rA03whiFCk1uKADyZhhDkaQk0x9T19orWtXkv4e3r3B7gbzHodUJt9VJr-mQBVT-VrUi42H56430_X66gbde7BVkLZvfH-f_n5Wtwg0-AC2UnA6q-Lxi4A6QEfsGWPnIPm4m6J6b-STQlyWOkP9mCBXbXeu9fZT8npt-0B79azw1BkZnDANmoXHpsX5C9hn1NJVzTaIr8hr6qpThZ-IWB4Jt9I7xtecNqWTLf4LllO_rMA6wdxRHDzEFhs0ha9Hx6FLiYnHfkUEjT_azn8loqBo0_XBtao96sVtup2vx35TpjoLCkLPZQqGtELKL2ukHxUUnoX-ftizWwCT2_PTr8qH4eEMNiIZGB_05XlIl9IHXcYPfvdqlVNMKHqWpgmjCiQxR70xLW-vxlSrYlVv1pslngxpKeoh9BqAVssmMyHvBoybDjYeHcbm9l5yRnEWbioZiHpCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇲🇽
هنرمند مکزیکی با آهنگ جام‌جهانی این ویدیو تماشایی رو ساخته
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/91123" target="_blank">📅 09:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91121">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GDNbRnfv_rbd8Jhf9C0NPN2qobRhccslCf5Mn3dp0hqq-303f19PsgixP7V7XXD2ON-iaJxit9nHohsDg7f3RJJ2S-75DoDNK2NAdXGM-lx-IdxKwkXl5Hr3Q7BOR39rTVERHOBUhbuomj8FZziTiRzOSFDcErPGuoq36J6P1qI7rB591bsMl0T3qm5clCqvknOJGbV1v6zCDwl0ichVh5PYdAlbwCXNtq49dHLLEa-iJ2fmp0YGdCJ0dscVL832XpWvskk3J6bPLy6g1aWmwbX6a1XGZcNzavmNvVzOlKUSeteGAEIVSrmTas7HSSeDHZOvqzopPTA1FGfD-ReICA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gawLXhG5CKwqksBKCHiOZmQp8sIUlrH3vQWem06fbgvkcjb2_v0wA6RGFD_HEjCSBll45IIv1GX4tOSZf7PF2mnITOOwX3LTTiarGnSKv6kC69JixrVESRcBqN1wU2sdCB82L830BiXnQu2v95hiY_inady1i3KEvzJ38pYr40wYUzaoqP5-z-otckOGdyuL_4-OA6sDfTnPJJCW5mGYq22gL2bD-NpNPBHHZVuDMn8k-r_-D3kV2oLXETPGYNZAUeHwBr_VE2gBA36AwBEtyirZxrw0TonkHTeCREAcfTMzTmvnz98L9d-j6gqV5qLwQ_YBuxIhQuJiuruzoWUNug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
امباپه: به جز هواداران بارسلونا، همه قبول دارند که رئال مادرید بزرگ‌ترین باشگاه جهان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/91121" target="_blank">📅 02:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91118">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇪🇸
ورود کاروان اسپانیا به خاک آمریکا برای WC
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/91118" target="_blank">📅 02:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91117">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🗞
🇪🇸
رومانو: پرز عاشق و دیوانه اولیسه هست و برای جذبش هرکاری میکنه. پرز گفته این بازیکن منو یاد اوزیل میندازه و شدیدا میخوامش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/91117" target="_blank">📅 02:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91116">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHrAJhaquCGz-7R8Qb1t87xs2URfPk7ttq7mCvH_J2kTvz-oUrqGOhYlAmf1LLpWw6kbWN-I3bZnQwYm2gFHvzHmifSIJhcS2MFjt2WAENvDmPfJVPYQmyHhACZu5MNLXhwDp9OE0WbvJlW2aWOUIexZmvLKlb73LHMYBWf2ulbH-AT9ZSPTzENqq7xT3RpgHcMdbDB57mZD9gZQPogWzPcqWriYL5KHhZigLpfvIXvZVfbp7AGqpS20Qmadps4qpXBZroP9HqpINkH0HIvaPEVlX6JD6KAloFKmdZa6WaXB2FCD8EP0ZQJjHurno-hQKFjxtXrVSzp0nbBYL_6BJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇩🇪
#فوووووری
؛ فلورین پلتنبرگ خبرنگار آلمانی از علاقه بایرن‌مونیخ برای جذب مارتینلی ستاره آرسنال خبر داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/91116" target="_blank">📅 02:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91115">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🗞
🇪🇸
رومانو: پرز عاشق و دیوانه اولیسه هست و برای جذبش هرکاری میکنه. پرز گفته این بازیکن منو یاد اوزیل میندازه و شدیدا میخوامش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/91115" target="_blank">📅 02:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91114">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🇦🇷
❌
#فووووووووری؛ رسانه‌های ارژانتینی مدعی پارگی رباط صلیبی خولیان آلوارز در آستانه جام‌جهانی شدن
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/91114" target="_blank">📅 01:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91113">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🇦🇷
❌
#فووووووووری؛ رسانه‌های ارژانتینی مدعی پارگی رباط صلیبی خولیان آلوارز در آستانه جام‌جهانی شدن
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/91113" target="_blank">📅 01:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91112">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hjki2VdEwhvKzQxt_OPmVuNkNja9E9vI-jzihVLJuby4hyb-pMCVdjp5ZzvIzqy5FIwUV3XFNWhF1iRM7CiSJ7OjN3DKTEja_lca9_hDZ22Tp2kdqEc2uMv2XC-UDMooJjg2fntfAKCUrGNoOsL8F8GFAsuCPJlRcx_efC6uoCXsuRJZlIT-SOP1A_BwTSLNaYOKHJm4yY6Ts8tyvjM6XVEuEaToqti70LKAWFrjDLhqP95HrWCM8gKclo1HAahzlyJuNFlu385jyLu1a9caRRew7f-1IJgvVW7PHhjinGz26cGqzVm3lRnXD5n_t0RgGqlD3qYHBVXphGeMejjO1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
❌
#فووووووووری
؛ رسانه‌های ارژانتینی مدعی پارگی رباط صلیبی خولیان آلوارز در آستانه جام‌جهانی شدن
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/91112" target="_blank">📅 01:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91111">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkjsJl2p2Fycyi8f6IgbATN_mY0oUQoa41Ls3olDVUQorGiMTSGH9Uh3vPFvBiXd_vdw9SktxxVC_ufPLefEP3AQJGlS1XPN7QQ3l01dLriFEa3ONeBh5IUf9iSYFtIcIg2H42xGb1yVModrqLzA7FQsCw0xT2rO4kpjvXZH2Wot0P_ggbl2zRRVRrBSnf1sW6H1VLgmf58nUSoKErf8t8kLjDwwGi0kx95TKANWR9vHOZOeR0B_DSjSBuDrI5K7Ly6vFKjKnl16DZQK2BxIUePjFCbNQ0a63PcBoXFB0bUQYNSXbgn9gQbatYz0zNSj_Jt_zgwcO5kZbJ73UdZdPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت
؛
✔️
تیم ملی والیبال تحت هدایت پیاتزا دومین تیم جوان لیگ ملت‌ها
❌
تیم ملی فوتبال تحت هدایت قلعه نویی دومین تیم پیر جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/91111" target="_blank">📅 01:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91110">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAJFMhGV8q1vREuOcUQvrGZnT9RVNclbqOPPOnUEe6Jifj2uX83BsiHvk2tnbjDMaP9xAwH267Uix7p7Lj9OohO6H_Ug5SQ2GnIS2ZsE1n1hrsWBa1F8o4bz9MSdJ2Y0LNOKiraccyE_lg0rVlhmt5tdvfmEJm7JFSj35py9cSPZ193NH-C2IinygP_jdAokdU0PpURh6K92lFZZfeVYxIgDg1OiqxqtoOqKXSlYLhJix3LJK7YEoqKHAI4C0DOYbh_fubskDbaSKQtI4jFX39jW6qQZ_5vebbSFEiXtBJAOj9UvRwTXir3riqamET736xyCBN8_OERjZoxzPP9w6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🙂
🏆
هر سری جام جهانی میشه یادم میوفته تتلو میخواست جام جهانی ۲۰۱۸ کاپیتان ایران باشه با شماره هشت و ایران رو قهرمان کنه. بعد پاشد رفت تمرین استقلال که منصوریان راهش نداد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/91110" target="_blank">📅 01:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91109">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
🚨
موزیک ویدئو کامل شیدا همسر ایرانی مورایس برای جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/91109" target="_blank">📅 01:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91108">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcPIWNMFTuZdIlw2u02Qev4DKLmWfQ5wjWIXqx2OImrFBEZ28Z9hJNnds-p41oKAbAc_JHpHAnTjU2A3I5-Lx02UpuDDv0PioJjM3ZgX4DOcuZe5r1gGavwFVefQOGzyDwahWG9HxCa16PmuxtJkohpdYAqdt2_X2djTzcXrKio_p85UJU8LNBDkEgkEibQwij_K3iShvr-_IqWJROvV_ulrdaDUltIKV0tqCCGc_ZPchJ4Hnv1vmXLfAsXesnYG0rucSa1-9sEdGhr6Viq9EKPh7DX_i0B6oS4KAYpKL0SwTrTcX2srO7e2nvJBothwQASkiGVeTimrw-53xf2ivw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووووری
؛ یورگن کلوپ اعلام کرده که در سیرک انتخاباتی ریکلمه هیچ نقشی نداره و الکی اسمش آورده شده
❌
هرچند رائول به عنوان نماینده ریکلمه مدعی شده که اگر دوشنبه رای بیارن، مذاکرات جدی با این سرمربی آغاز میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/91108" target="_blank">📅 01:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91107">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
#فووووووری
؛ شنیده شده بخاطر توافق خرکی و خیالی، پدافند خارگ فعال شده و سپاه داره موشک میزنه سمت تنگه هرمز
🚬
🚬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/91107" target="_blank">📅 01:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91106">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crPfs3wpMSbXVI3UDnsATBxO6WbZ7zDyLHf-WBTvT_cWxBVQo9KzzniR18-mTPQK6Kb2V8vusGVxppCJTHGXYRZJqx4Onc7JrJg6EKn97wcOk1d_2AZjRVvMYcuT5z9F4kGrO07p2tyF7J2xHTDu7M05SmMtKvHkBv7Gt758SDhqoQ2QEu3f3TMuIicTrIcAXM7m4gqBqlhFL_LwfMawNgp3-ozYevVwKciNN-IOMVaKkpNphJEXx7JtqstOr1DINSwh4Ntn4UEBUDHvvjbtGnXQkckoVQbL6DQ7c4UNeRqWSJ-7_DMvZ6282ZXcxD15hQH-ngwZ5xJR9MC6MHga6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارل 18 ساله به دلیل پارگی عضلانی جام جهانی رو از دست داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/91106" target="_blank">📅 01:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91105">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/QpSIFKIAcEQZK4us3QTASdMWYX6acizh-lDq_Chemjnl09-jnEaMs4IDZHjqvuTQYddCe3rRzxmdtUcS_AL4zuUe5HXhzLwNDedK-gPbTdK-TiyRsDSO1SNYXERdTnyXL2_iTZaZIK_7ajd-_tmKLdAQhJAQHOhHDd7--eTLlA5XGOmEFi2tQfJAIHweEB90DVWzzN9QO9ySaxA_fGqyMNV5XFggMUAOk5Q4BDFuAadvk-QRUBUbnrvXS3UvLSXTHr8Z03o5I0RWMWxktFaX7Gl3e5p0Wp3MXVrV1RA9SI0jHjuoNba-N86do5KlsOrMk0DWCXrlSX5NuYRH1a-aWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوووووووری از رومانو: لنارت کارل جام جهانی رو از دست داد!
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/91105" target="_blank">📅 01:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91104">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
فوووووووری از رومانو:
لنارت کارل جام جهانی رو از دست داد!
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/91104" target="_blank">📅 00:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91103">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DK9EukpGD-t0D4k7t0KUFZhcBvl6efPKxqkJBtM-vv88TzNHCTnPKquhXOp1Sjd4rFjYnMLkZm6t53dIq4H8viVp_LOuOCitaG-UIoajZdnFb9pa3_q9IhtqoaJiqCYRLPRtBVTMYkn8AhLwGZyMTQFDzHa7F0Rd7h7dP5GahLKJqIJfkJSWHRh5bnI7x3qxUHfB4Wm3nkvKz_vk4dZGMsId6drb9_fjUSwFE-Z9LZu5xwzfMNPjRtKNVW3ZTY5TJmoPb9K4TEFxygosv14dwzRxbQkw49gFcDYZJH8T1T4aLw6E3QLIEz-yaYIm-7GhFc3Ux-uEeig3reAgotuSNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواب مایکل اولیسه به یک هوادار رئال که ازش خواسته به رئال بیاد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/91103" target="_blank">📅 00:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91102">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f8ee5741.mp4?token=VB_f2sl3MdPn1EJsmB37mOV6Gp2igpqoK05dz7Lf8GiFwqJl78YRA-jpAf7ogVZz69HZrF3AMn5nJPtyHhbIRnSK84DgAd-8RECwglFC28DIs2hL2UaVPAPAieEYJXUo9oML0j8dQmibJvHn7PauDD40w8Mqnr5tSYbXgKfofscXgAlrdzlRkjHajMTG1b0out_OxVGwvZRx3jG6aWWYU4HePHEjBC7sseaVNYDwIEFKR6WbUbrbDIzFiEmneVORSl81JMBST7ufl4Vd0Q3cfQZz9zMFPkqZctqT_Lmt6q1Ls2qFj2EBjBWzn_8K8Xs5ZecCsioapRtAnAh9GzBpcxYNA48XsZxBjZ-CYyukMD_2m_Zrfrg6PVkZnjoUYwuodkX8i4xbVjdpbBlzliZTLMFMM6JPCanFz-pSL_1paLSMQs5CxHZ0PTacVTlc6p9uO5EqQQzQl2jn_weahGSY5jqe1ZRDUCJ6pOjn9AsPvBc2hV72fqzCzrk1Wvvhw3VKDFZ7o0qORGGlZf7xfhifDUPtyR2GD6hiiPlEXw8I7IDFRqhTiPCBUFPzUD5OIFUYrPBepQUzIpiSsDXurXwXHhMNCq-s43g_CWm0Di_dowvNgQA3P9be7Os5gdUq8QHldVDLP5suYWmI0-inFiWN33vqCoJG3o7QRmnJqZw60sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f8ee5741.mp4?token=VB_f2sl3MdPn1EJsmB37mOV6Gp2igpqoK05dz7Lf8GiFwqJl78YRA-jpAf7ogVZz69HZrF3AMn5nJPtyHhbIRnSK84DgAd-8RECwglFC28DIs2hL2UaVPAPAieEYJXUo9oML0j8dQmibJvHn7PauDD40w8Mqnr5tSYbXgKfofscXgAlrdzlRkjHajMTG1b0out_OxVGwvZRx3jG6aWWYU4HePHEjBC7sseaVNYDwIEFKR6WbUbrbDIzFiEmneVORSl81JMBST7ufl4Vd0Q3cfQZz9zMFPkqZctqT_Lmt6q1Ls2qFj2EBjBWzn_8K8Xs5ZecCsioapRtAnAh9GzBpcxYNA48XsZxBjZ-CYyukMD_2m_Zrfrg6PVkZnjoUYwuodkX8i4xbVjdpbBlzliZTLMFMM6JPCanFz-pSL_1paLSMQs5CxHZ0PTacVTlc6p9uO5EqQQzQl2jn_weahGSY5jqe1ZRDUCJ6pOjn9AsPvBc2hV72fqzCzrk1Wvvhw3VKDFZ7o0qORGGlZf7xfhifDUPtyR2GD6hiiPlEXw8I7IDFRqhTiPCBUFPzUD5OIFUYrPBepQUzIpiSsDXurXwXHhMNCq-s43g_CWm0Di_dowvNgQA3P9be7Os5gdUq8QHldVDLP5suYWmI0-inFiWN33vqCoJG3o7QRmnJqZw60sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">First dance
❤️
Last dance
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/91102" target="_blank">📅 00:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91099">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/altX0g1VaYp1M4okEuBlsibP734DBiESqNnLHQo2-cajb5dZeQibY4eso9FdJOufYRST86_1BqueQijEmgCMmS6vFEo7Pj5G5X8i2hX5QhDNR4c8s8fPWXCPmZe7gBxveqCUNh5TzfoQ5pOTPC7VTSFLBCHskpjz3Ist1tI51ld7kZ4yfeE3Di6miraqVZVaX5YFQVfSGxPzae8fGobP4K_v4xm3VPU77M8yQlL9caLJgaFkEGHhWnvIVEMqp0x7LiqKGVeBrU1LxUqLdKG7ybACdZZYo6-Kq89mD1rqrATZxZ48RZQCEjPeP4xe6i59a8kGaP1P3RQlwWgE0NwwQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BEn-U6H7y-QD0lb0GxRIZ2O7rfqHnIMGX1FENFWrmqGJSRTtdSw9UXj71FZvq1NuAbazw2Kho3GKQ8fSfZEfFA_lseeVHeKGgu96n3YYfhJWYY5tKh3ZDcVSPLNZdbFt8qHd6mqcgv4UVMtgjJchwZsqfDfmDti9tFoiG4c_VLNtJLLPgq_rSW6oBWWEvifBXi0mVAlx-R5WqpDHYTTcBJpNqmdMTG0sVrtnus0qBCPTUrIf8OQnptdJISrXxDg0qlAQ5z74UDeGhGBKhipQzCaNZFqqSPLxN5nGdFsdOcuqngCEhzFK_xw5QLBocZ7SAb8kRpSouXyw_oCQ7I_HYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z3dW6N9h452lj3NFalbr825S7wkbsxnea3U_QwXvzlipPwa8a-m8BfKw-wgsQE6COLl3VbvTs0x_G0zX5PCvVzg-pbPPbFJ4q_Vw6Rga8t1-rL1jfD4JFxuRzzVbj9z-MoHKICa8H7MmijgMWqhIqG1sP8k0PB8QGHWV2XQyZHbsA8avT57afElLZAwj4jbhwErP2xgEzyCUfpitI69siE0Y3miW99dMTbHa_r2b5gyl8QBrPxn126GDmj1llFHOBZ37xoJYG5V1puR0Ja17LfM-i6UiQ22jXKs2wo--vCRIiXg0vHd-zmWYgP1MgnQSU1Jp0K5mROA4Mj3X9ZGYqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">زید سابق و با کمالات وینیسیوس
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/91099" target="_blank">📅 00:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91098">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcsEX7H2XxCT_j9Gm5mBGS5CbubbtTcLSw8YjcSd3HaD04l7_hxsSz5DV2RiLoHetrAp2cJxAnSFkyGmsNY3MgqpZXi2eXVYjmxQlZYsTkAOdbmk-5-4rC7scG0LFMCS_I5ETi56MFL6Z_eeuIQsuWofW8Tuy734DkJHo1XlYupXe_H4b5TD71FRTicdyqg4Vg-62sZOr7aWX-WY8jnLHpFLodRPPsH5QuOVIJrOr3ZBLvVC3nmT1kAo-euTOkGQIOGi1cN4wC6K0vYe_0c69Ws_ecD1sYEr35QEHxO_FKnR0FDFw5Fbg8si3iWGlzr2Ik6JAoy9j0AJxjMIYF3z9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوتبال همینقدر میتونه بی رحم باشه
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91098" target="_blank">📅 00:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91097">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mi8jYb7hPB-RUy1rRCB0sytzrRD2oAYUA5EiMiTxjgcrqRxyWNC_EA6A7nJPyN2T2j8FbVa47dfQBdZHQ5wHsIr_UTEov73i3aqaWHws75nSwhaaM0SThHop1hfXGO5JXZywIVnRste0oAlvNwMse_ccgqDLW2FNXXFKWwT1HCL8mQ9UWK5moLsX14IjfNbnm3-Zs2plyBMyCB2R053TCc4I346_DSremIqAdwdIIaSCZVwhKygqAxWbYxePwai6nkH7w9A7SrNXNXZLjXSCBkCgu-DRFDpalLA3wY1bOcgaNGZu1RZeZPy8RfZh54V1191nDBCtPfIs8Ta8hnE2nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ بازیکن تیم ملی کلمبیا در عکسی که مجبور شدند قبل از رفتن به جام جهانی با رئیس‌جمهور بگیرند، لبخند نمی‌زند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/91097" target="_blank">📅 00:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91096">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
پلی مارکت: صادرات نفت ایران به کمترین حد خودش در ۶ سال اخیر رسید.  @News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91096" target="_blank">📅 00:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91094">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J12lUz8RoBwV2dN8zQQqM4wuyj9yW33wQoN-QID4i9H8mojc9AlJyOQuv4cCf-fcyFE3v2gmxqAxcBYmGtYUiBAzLizQzM20BC3JGLr-7KpaOXOb1Xa7HE5hhtzwAj89obgQcW_cOkOIeAI3yS9qvSZ5JJkT7NFV-hRvPHVyCANeEge8ec2YywWyp3NenKawib6939_wFClpuelc8wFi_ABawkr-a505P4kfUDIHj1-cGEOtVUAg5IlFu6x3PIGOWWgJFLEDHIF1XYq-ia4J0zMBoD76j8RZpZO8nJNBBsr0F91PrG1kae5BM05S92O_uDLGdQuu8lERxTVGdr66xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OH756rzDh2bz1Y29Ka1rdQihDDVhlrhR92eNRzwUeqH5_gam9X8E9oJ8xYpRlejiniXzs37AT89squeS6KfVQ91eYZS7HUdJlWWgjA0Yr2XlQk5_x--tEylR1rfP9gIoANnP_rsCYE0iQrWJVANAcnQVlm1zwSxgbwK0OcUrVlT5dBXyeducfVTJQeFoPgiGJfF--1uxN2gR3vm2F2_2xWP19acZFtBJ-wNxI24gPk83YvKY2jo_gfioeE1vsT_XDLbk3uq5nlBVc1o3yy1Z4rDJXyToVgXfwZqehO8m2FhpVu226SDLTmoKLY6YU3Bgchs385_WGLg65loe-4CAWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
انریکه ریکلمه یورگن کلوپ را به عنوان مربی مدنظر خود معرفی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/91094" target="_blank">📅 00:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91093">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🔵
باشگاه‌استقلال با محمد خلیفه به توافق اولیه و شفاهی رسیده است اما این گلر جوان اعلام کرده که پس از جام‌جهانی و برحسب پیشنهادات دریافتی دیگر خود، تصمیم نهایی را خواهد گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/91093" target="_blank">📅 23:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91091">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrPwWVLP1uk7FVbvuFbhXj-oMnnciHTj_g7l6Bg5j9JO3yy5U8Qdo2_6CCmCV7ht-ayvtSNGzr1k5FOs1X4KGXBReP4kptkgS4PPfS9xM93ycd5SxdBWcO1AM8hLoTKecJg6epIt3Gl4EfaoFzqptVojH5h0B1CZfKuwN2vlllowte7AE35BDQb7E_31fuKGWeHdwhmEOOo-uG0G-AcQtrYjPnBI9rl5Zu2v48Znfk1rvUNQH6TaP1AZybosKGw9xb2t62SG3zd-8rpnulqpDRuj9MeUIQBQQBTgZ09mm24Ya2NAKV1SO1G-hNuuLMEYzAhaZyhV5fPWydEL45vOug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار بهترین بازیکنای این فصل پنج لیگ معتبر اروپایی در این فصل:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/91091" target="_blank">📅 23:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91090">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2q83Mw3Ski3hXMDLic-fFFY3cg4yOTPmk-eCelKdrhjQtVgr_1TvCi7BGKQnCi-RwaWY5AWiFDbkQ3KQBdRul6-3X7j5dYiZ4IhGtjWxogdrOyfEluecrToDOB9-wvBMjRdpzPEyKqrGue4NDQ6BM06nspX8ThwuAV6foE5hh4QKLjn27doStAeb9G8g8L2tSFkbcDCu9vmnAgWIFUhMWeokfTqkpGdiAl89mv0-aID231urDQfdwDVU4OJDulh8bYQl_vfFpvozh8p5N7j1AFtquFQX-HghwBeOYN9fjsCISEOuRG-Sn9X7hwczPkVWzrjGyJD573O1hcC_9Yw-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
انریکه ریکلمه یورگن کلوپ را به عنوان مربی مدنظر خود معرفی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/91090" target="_blank">📅 23:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91089">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🎙
تاجرنیا:
آمادگی هر تصمیمی در خصوص لیگ برتر را داریم اما اینکه لیگ را نیمه کاره بگذاریم و قهرمان مشخص نشود این خلاف عدالت است!
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/91089" target="_blank">📅 23:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91088">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696197860e.mp4?token=jiZvOA7Oclfp-DWeiKKpEmxJe4Fmq-YbaxcbXw5Mo-SHvm9AdZtqVfJq5H9-TRk_0eH4AJRRTGyhQqNNMiHbCA2TnJ4ZjSbOQgbI9UVD4os8qT-x8lI1IwsM6-k07gnnAN91mMO7DcoMkkygxjao2dzLCVru985-iNC6J0QtlNCel64Hc9udI5e_4IL2zrrBPnv0CVmxdbrTD6LNebUnEEZBGGdIIGLrYeB7nfUtcS7zcRAqLrFopSqqFj0UQ1I7dkfolB0dTJ_nPwEizPDE6WcyUN8qtXZfTRGgv1YwOkulgNEPL5WLudrQTgvWVgjk5qmG65XlqCK9IsPallUG7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696197860e.mp4?token=jiZvOA7Oclfp-DWeiKKpEmxJe4Fmq-YbaxcbXw5Mo-SHvm9AdZtqVfJq5H9-TRk_0eH4AJRRTGyhQqNNMiHbCA2TnJ4ZjSbOQgbI9UVD4os8qT-x8lI1IwsM6-k07gnnAN91mMO7DcoMkkygxjao2dzLCVru985-iNC6J0QtlNCel64Hc9udI5e_4IL2zrrBPnv0CVmxdbrTD6LNebUnEEZBGGdIIGLrYeB7nfUtcS7zcRAqLrFopSqqFj0UQ1I7dkfolB0dTJ_nPwEizPDE6WcyUN8qtXZfTRGgv1YwOkulgNEPL5WLudrQTgvWVgjk5qmG65XlqCK9IsPallUG7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل‌زاده:
امیدوارم فدراسیون پاداش بهتری از دوره قبلی (حواله ۱۰۰ میلیاردی ماشین) برامون درنظر گرفته باشه. ما همین حالا هم کار بزرگی انجام داده‌ایم
😂
😐
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/91088" target="_blank">📅 23:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91086">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fb5b6817b.mp4?token=RWUwWpuvrPB-y2QMeo1XNkHpzN9LSA9HTY1xlQeb9Z6kBRPd2-NbST5OIXF8prDielYw1C8QulcdF85CFMQtDjYVai2tinFmYKRGOCEKEGZfM2S2c_fufila4dRIJjGrXtSclTkbOa-vu15P2YngwWBTbU8MsWLLU-mLALyr2RreDbbryM76O852pRRkvoeLfyJdKqHX0OdFA_fkAEUBmwUb_x86IgSlGiOQLQPcbrnb4CgR-zUz1c_9MaklqyJ3MeJL0ss-WW02PzCWCG6HB-roRYNZS_wBp6vnB-2YWkj0_q63ZmttoiJtBGJNMTKJ3v8-ep1xE55W-PwMmLe_lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fb5b6817b.mp4?token=RWUwWpuvrPB-y2QMeo1XNkHpzN9LSA9HTY1xlQeb9Z6kBRPd2-NbST5OIXF8prDielYw1C8QulcdF85CFMQtDjYVai2tinFmYKRGOCEKEGZfM2S2c_fufila4dRIJjGrXtSclTkbOa-vu15P2YngwWBTbU8MsWLLU-mLALyr2RreDbbryM76O852pRRkvoeLfyJdKqHX0OdFA_fkAEUBmwUb_x86IgSlGiOQLQPcbrnb4CgR-zUz1c_9MaklqyJ3MeJL0ss-WW02PzCWCG6HB-roRYNZS_wBp6vnB-2YWkj0_q63ZmttoiJtBGJNMTKJ3v8-ep1xE55W-PwMmLe_lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زندگی در تهران بعد از جنگ خرداد 405:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/Futball180TV/91086" target="_blank">📅 23:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91085">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBMT9eZanSGrhSpGfPfS3e0na7J1s7yFNr1OWSktIopzSQkmGVMK8caYd3SdeLobzFjf5eh4O-nqNAW6Z1jcVsP-Yme-spz2h5QQRBpU-EiyYTSuOmHJR1wzllxV7sdLd66ak5ZQCvUtGNHw83uu_oakXwnGSVKvCHK4tdGbQbgbmDF16JexKfdwXchHNUeabuPCmNFONILjNpQ33U5U7b2ojBqkr-X47JwuM9-9qlMDZTUC4NbhtkwM3OOutds__pDSKJYFB2rz60-t7u1P7Fy7rMs_VqFnY03brWw7GO129cQ3lptYKlyxB_AWElgUGudodtMsWbj0li4gG5jUuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
موزیک ویدئو کامل شیدا همسر ایرانی مورایس برای جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/Futball180TV/91085" target="_blank">📅 23:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91084">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
🚨
موزیک ویدئو کامل شیدا همسر ایرانی مورایس برای جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/91084" target="_blank">📅 23:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91083">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_aKvhzp-_N2GAYGmPXH6FmkBQH7fwHrwvOLom0z2m34ZgKZ3l7pEAUzRyCjCs1CiuXYzNSf_pgvMznYWAGmXXnHTATmu-oKBSW2ILsuXcox3yXvyR0DlhvSACDRH58DZln6C6nSXEIHf9YwMbvF06VkCGZbvgs11ArVRcOy_nmIWJ5Czd3tzTFBVaqfpppSQVUL65YN_kx6N5kZNm6wF2bQUo68fj3hQpeGYucga3Dea5wvrg9bcXZMQ6CBAZS-NYw07xT8otO1RaifwZBbK5Zs8iMjMpMCOTO-GnODjgcVgNVsZDKr9slqLwOeasEecsLtxvFm_1YGnVEDtsiBYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم منتخب بازیکنایی که اصلیت فرانسوی دارن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/91083" target="_blank">📅 22:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91082">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUSoNXdDmxcepIoG2Aq-CPg9XnWEhBL8MMRTLFqO8kXc8y67CQbTxhlmkuuUO6OnEyz7pQIEjlnYPy2sZtl5zCvpMSQu29qmbzvllIog6LW6XvQfHwUzi875Q3IjH1sK2ktOX-SKubvvf61JauLiTGXspKzx6OtZ_LvUqh1tZOj0FpS59TM8gS_oi9VjBjWlyMsZwAAkCpIAqtTDx7aJUwF9QX6-rrPLLmGldT_OsBfr2voxSM0C3XTRk3Z6oGnbitokI8ZCQRTVGLkWvRFPFkeViOcEa2nkLSAkw-2pBHStcP7Xk1Zfvc18ZLbdKYlOQpViuq8qj8JC7Id5rDHeWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه تماشاگران فینال چمپیونزلیگ 2026 با یه بازی رندوم از ریورپلاته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/91082" target="_blank">📅 22:39 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
