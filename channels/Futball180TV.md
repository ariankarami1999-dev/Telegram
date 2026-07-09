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
<img src="https://cdn5.telesco.pe/file/KX6WaudVpnhPjmhPkiCidedTWThIbMksinPEOu-qhPEugewpb1EwhLwr1sQbob9rBUbqUBzVnCfbwwGseXgIp6JmvBAn4ZFxKLiy_R8JQ9Aw_AW77ZNXA0vwq8F-RCL5pqa5qDKQw4LBgN-0lBWoFoHy-UbUJElEd_hAbOhp5nKt8eKpdS4LfdnS9gZbIAWx5GQUvC7aRYZLRxd1A5L4nOm_C0E9J1POBKKKi_7k-Bktv6YxkeLfbWv-_5FdJK-pVNB3eMfW4akYsCbYofXxkrF1QJBJUM58EObip5i9W6wVD5jp9feq7d0z25VLb1gEpvArO2UthRXk6JWylS4U6w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 605K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 00:30:37</div>
<hr>

<div class="tg-post" id="msg-99282">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">😟
🚨
🚨
🚨
#فوووووری
؛ در پی تیراندازی در اطراف حرم مشهد، حداقل ۴ نفر کشته شدند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/Futball180TV/99282" target="_blank">📅 00:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99281">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvG1e5EC_9dDxnoduiMZSJh3q6NfZPDb5VGZYpLSfe5IWYi9jd6YQ3NZFbejTPbZxhUZjl-zZDjrG7YF7QcdanNRhAvQ-IO3_nie3d9fyAqJmyj8fmAIhRoX9PQWaf5Q7uNzPeJfJMdyJit5Zg9CLN2_sSb8m5Cqtb5_B3zU4CEzlblDAe99DH7uku1Slq8n-J-uASH39Lj3ipEC2wXROl2nqLR_QTHW_vlINhm3ka6dnXF5bYpz5mh2YD3-n_qL9UFB05A7tUALASe3dVmhac756LG2AXUg5ZrY6ynVoh3Jy4svqK17DJr7fw3RaQTDH8KZttyRyOjG5EfVo-lljA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیم‌هایی که در تاریخ جام جهانی بیشترین تعداد پنالتی را کسب کرده‌اند:
🥇
🇦🇷
آرژانتین — 19 پنالتی
🥈
🇪🇸
اسپانیا — 18
🥈
🇫🇷
فرانسه — 18
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/Futball180TV/99281" target="_blank">📅 00:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99280">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
پایان نیمه اول با تساوی بدون گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/Futball180TV/99280" target="_blank">📅 00:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99279">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shPi1YilqmK9hW6GA48cjRapl7JyEfioVmlAplsbUfGlyHbBpkwV_ZqYrjlUlAwNJi3gx3ZN0q-zVllOgmXD1TLdWQf7ZAupS3ptC0HpqKmKIUa0Xe5MxgUlpe0Kr7eBNh43Utk4zMc0g4POGdP0oObuAHP2k2V1i857FCgnjuLEVpjIWzl8hG7mam5U7DP_q0HtyhHAq5bnSl7maEJ2KjbxsfmfDWypN1aT4FkNDW-Xtz550nz1h7sBI-J39u02IBWv-B25HouSaZ1EJDVax7bt1Bfj_KpHYuCKm0M2jWfkogs--qvOG1q6NkMHoZfMB6w8pXL0_zQY2nAu9J2D0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این همه مراکش مراکش میکردن همین بود؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/Futball180TV/99279" target="_blank">📅 00:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99278">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kY8MUw8QIFWilxtEYSsPTtKxzYIUTrHch3TOhoaxg24TNIVe7Q6h32jEMmawM-88DhxbRsqLDSN3YDdOUv-OsMu-eA9YcieVByy3wclzKrrwDS3x8gU04F-7Lp03Kmp6XpaPK_rd-pe4Vqn5O8YizG3unBPO3fINI-vIXs1vfKVWG2duMMEVkNJSlC0B9lt0kY0-YF9CtCUKZ2ZrlWHlYdMt5dggLQSmH9jgxVAb8j9y3w6rlsad0JejMtxrVgvjInH7XQC0zTptFpCmRKcfQLSC5JVDLvLJbPbxQ5BuPIiIel3l214y67WwniXChMACep0C0sAJiMSln9gQhrwJCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانم شکیرا تو ورزشگاه
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/Futball180TV/99278" target="_blank">📅 00:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99277">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqZJNfJiiTGFUIfTa_hLaGWprGsnuGN3VjiP6Isa7Ymng7D56BZaD6suoQBliXcb6zjsU74fcqoirHALW4mFmojReZVCfeZokNSDV7G8ec32UtgnrFyVjnOBJsJNKExCTk0_bC23Aj_uMeYaSARVeNAk1J_65Ll5t-ZoEeJGK4B7W9BZlSRpyOn0T7v972bYCG-nOxMvvSyAT9m7utmRd4faNpSVU0l_E6KyT2lgz9mJd7obKCHfIljhD9_emckcix92c0_ZWXlI5pDQ6xtnmqk0D4_43wxlgUT8QGczo6QGhYVHUdFD5lSpCVj8FRuj7CYDQfkL2Qx6SzngnZZHqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانم شکیرا تو ورزشگاه
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/Futball180TV/99277" target="_blank">📅 00:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99276">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/df5b3f9b34.mp4?token=Su6UnOMoARCjTJTLcc_FS-8hDF1IglRLfKZBqVBRxoeFkRgdjgCyCC9H9gKMiGWBSkDZ1RadO3S8VNOtqpiC7eaAK_PDDxD4a770k79O1Fs3sURydoivxH77QnQfB2Y2qvCXJnCGUIIq_OvMufG9siWBj0NMJ__BLKv8vz7qXs4gB-i46IIEgN4rndNpRqdemKqQZ4bPMmzGj9Mjao5lTtuzB5pIxQ239NE4FVhOWTfP3w-1AFarFb5n2l7NN102lgVj_XSbGcc_PA9bQn4bL3w7b9CVcELXOwDnLudMHESIxIy0G1M59xGaLW_BEySHygF2PhxFd59VbW6nlBVeqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/df5b3f9b34.mp4?token=Su6UnOMoARCjTJTLcc_FS-8hDF1IglRLfKZBqVBRxoeFkRgdjgCyCC9H9gKMiGWBSkDZ1RadO3S8VNOtqpiC7eaAK_PDDxD4a770k79O1Fs3sURydoivxH77QnQfB2Y2qvCXJnCGUIIq_OvMufG9siWBj0NMJ__BLKv8vz7qXs4gB-i46IIEgN4rndNpRqdemKqQZ4bPMmzGj9Mjao5lTtuzB5pIxQ239NE4FVhOWTfP3w-1AFarFb5n2l7NN102lgVj_XSbGcc_PA9bQn4bL3w7b9CVcELXOwDnLudMHESIxIy0G1M59xGaLW_BEySHygF2PhxFd59VbW6nlBVeqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
صحنه مهار پنالتی امباپه توسط یاسین‌بونو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/Futball180TV/99276" target="_blank">📅 00:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99275">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ya6LGw_Qb9Qa1IaUSju7VXPxuVEvInLmq-6cn9KbKUfmt5XC4dj-iwf3MzvhPmIY9YeAL1eAwtcPwdW5i8-nUrpibEv4KkzZHlgglequmslhmt48u0fOe0pFPjXK-GtGY-lQgsGuRYsZnByUJTE6gW6lvbQMC7JJujdcQ8f7ulN2UVULKqTxVI9v0TidnTLb-pvgNJrjyMPaEriWeTLLMuniEG5nIdXA9TDRJeUpsu619_1defnLQn6nlLRJOycdV049guvutYDvvll2WQ9kSX4D19NPaiOO7M-6ll7NQSddBntRoejDH8raYJsstcKCFRZAdAxO1375hDtC3LbuFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپید که تو بازیای قبلی کیت هر تیمیو پوشیده اون تیم بفنا رفته امشب اینجوری رفته استادیوم
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/99275" target="_blank">📅 00:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99274">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بازم بونووووو</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/99274" target="_blank">📅 00:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99273">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وااااااای</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/Futball180TV/99273" target="_blank">📅 00:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99272">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UT1im_9U3HQOeg7ab5j0WI4CBJXonDZv_ddO70WdPmjTSfFpx06yrfLx2MkNQphdxUN1GLS33LckhNJoYR8KieJDU7Jl8dZTthtPnxXOmnTmZ8awYoTayqfmsg1K4DwzWF98meePAopSzZPKrIkKeaUQdUTpOZM4DAvHw42fWPNoZwYRyrjJO_imDhseYmbbvIvFd5yJgKQvCcmhzvinutY3qdDmXjpQFZD5x0euuM6GINmNh6fnNwQpgar4ZdJXJrsqcDKB4bmj9MStOUKrBuTZtc7Wu_cAQrgR9neLjn8kSjT-YnaPLrH61lBBHp1aVH-Sy9cTWKzL5pZKLVOjgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کصخنده‌هایی میزنه فیروز کریمی تو شبکه جم اسپورت
😂
😂
😂
مجید نامجو مطلق و پرویز برومند هم تو بازیای قبلی کارشناس بودن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/99272" target="_blank">📅 00:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99271">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">آب درنگ</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/Futball180TV/99271" target="_blank">📅 00:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99270">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">چقد خوبه این بونو واقعا هرچند امباپه هم بد زد</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/Futball180TV/99270" target="_blank">📅 00:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99269">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بونو در نقش گلر مصررررر</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/99269" target="_blank">📅 23:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99268">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رییییییید امباپه</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/Futball180TV/99268" target="_blank">📅 23:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99267">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گررررفت</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/99267" target="_blank">📅 23:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99264">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دیکتاتور پشت توپ</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/99264" target="_blank">📅 23:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99263">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">برای فرانسهههههه</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/Futball180TV/99263" target="_blank">📅 23:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99262">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پنالتیییییی</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/Futball180TV/99262" target="_blank">📅 23:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99261">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بازی دست فرانسس</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/99261" target="_blank">📅 23:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99260">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6ripqYZiG2JkQASRm_eAyER_eVbobDqT3gPZ-Y8CNXXnuVPXLOoED-b_7yKe0GYXoGkT1SO6HatGNdGM0jFJPrvKlKtS7t6lkC_uWGY3vpkF4yA2Xa3DPrRCuUD8al_wN79FyDp0Xb2dji425KvtmPGBLJb70PElre6EZvBOy3bYtPZfScaRYmB5zQXUo65lQ8_wuWhbP9JlFVdBoMRmtF00NfYeVd2izET62zMi93jQcrK479X7JvwBsc2Io0K8a0b8ajmL9hDZ_wBuc4wkwFeJgnBh4WNfk6B1ot0Q43RLVXle4MVBwpOPCj8VbXc5NZ_ptTS8DTW3Zw4chhTBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارشناسی کردن فیروز کریمی تو شبکه جم جزو آخرین چیزایی بود که انتظار داشتم تو این دنیا ببینم
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/99260" target="_blank">📅 23:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99259">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWSuwii_wpZOMbXMzDuTzFAXPQVxILY0ebJZFPijrgzN0Sd6rFbhIC4r5CysVkKmTwA_ID4Sco943mUHAc1Pkn3hJuCIRW5j8bjdgWxZOH2rHaksUlzW6LjcQONbgHctHZ0pONj52LVRQY4ZnjgAxIbF2NClnAQf_L5eM2aQ6QM2YBn43n7EjlvP8WGDPQiAQrHdM0cfoJ7F_LBw7nTcReukLkfEkdpap5rHNCc-dd5ChgvRm42YNSuOzZ8IW-eGgmS84_naCkULYqQ0GqjvKA878a79oIe4FsZ65RCrLkDDMIxt7kSYZiokU7ff0nhcba7Ps5l9nHxu2thT37OUUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارشناسی کردن فیروز کریمی تو شبکه جم جزو آخرین چیزایی بود که انتظار داشتم تو این دنیا ببینم
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/99259" target="_blank">📅 23:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99258">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXNmgaNUMfYHmzZLpeiL71sRrH_tgJKTxk6mZENEiM9sArobX1MWnGQo8Cyh5AFeO0CKqcuYx2tWF0LWgQs5W6M0WpdxkA_n2yUgR_9gsxiEsqnPJ9VBT0q-34_9DlII1b7kceRjomvJhDLVPz6cqebg6vr0LyNG3EorPVGDOOvZ8X-dIWZeNMoeOdBTz_MH8J4LZFqqDT9byVbx7Z0ADW5HaoOBmgGb5GLN1ankMPLO8ne17Lf6H3FAF3sFTnsWNxK9hg9HWqCcBBFly-10msWWbNb8Qr9vFpyvnBFYmiuJ8wvBkqn52vx1FugielMuK-qFnW9p4ScnnMLEm5N9Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون همیشگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/99258" target="_blank">📅 23:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99257">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">همه فکر کردن گل زد امباپه
🤣</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/99257" target="_blank">📅 23:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99256">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">چه سیووووی کرد بونو</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/99256" target="_blank">📅 23:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99255">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">برییییم سراغ بازی جذاب مراکش و فرانسه
🔥</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/99255" target="_blank">📅 23:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99254">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwZbl2-qBjCIlShtq6sx543qOkpqNRI2ittQiTZPaEwmM9H-urdHO8_AWd4qjGGjn7Ohd_RAu1-_DhiaH-c23zJQxDA5WRfqIU4aMrokLBfDd_8652J0JrLFnSKuOSjYu67dF1jKQ8ffI35dSb2ubZb4DglIsIwDYODBsKiwA2dn_oB54b8EKNV-a1DnuZcOyQtz0NW5zRmq7lKKcPbWtk8nVwcaRx0iJrsHIiEesl9hlvFOeKkA2TvkFK3NqMLdbplpE2ClJYPXI4MkJU59vnUqBy5TCJfBmLnuy2QCIpl-bh0nm55cUvFvabBtZeJDlH5aGHvquCgr4L7va7XBsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووووری
؛ رئال‌مادرید برای جذب یک هافبک ذخیره ترکیبش به عقد قرارداد با بروزوویچ ستاره سابق النصر عربستان علاقه نشان داده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/99254" target="_blank">📅 23:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99253">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc725a0eda.mp4?token=aVE2HJ2hs65tNTMxOKIgKZV9flJJcGuwQ-qlgBgxssVLb3kHOEb3qfMVhfENy9JtDo3ExUVm4iH2g3I164nA4tWS1qCqZduoR14dlHbinRaBcd3heoyLZyvA6pVaDS9Tqi-44AaDrrr-KYSKTcYZCRaryJWvt6uh2Ez4_9eXyQyLCOoRRHlHuLLc_ODk4iz-ap70pEXujBQnsVpdhcHinj-5Md1on_FkArWEx1eBCZv-M4-IitUkVfWL6qDPuk87UDLk8905DI1Nas88O0s0E-X1hZWv19oH8yaQHtMzMDxrNrq6-I-GvoDEpDhnv8CO2H0cUtFDXhk3i8oGwsKKbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc725a0eda.mp4?token=aVE2HJ2hs65tNTMxOKIgKZV9flJJcGuwQ-qlgBgxssVLb3kHOEb3qfMVhfENy9JtDo3ExUVm4iH2g3I164nA4tWS1qCqZduoR14dlHbinRaBcd3heoyLZyvA6pVaDS9Tqi-44AaDrrr-KYSKTcYZCRaryJWvt6uh2Ez4_9eXyQyLCOoRRHlHuLLc_ODk4iz-ap70pEXujBQnsVpdhcHinj-5Md1on_FkArWEx1eBCZv-M4-IitUkVfWL6qDPuk87UDLk8905DI1Nas88O0s0E-X1hZWv19oH8yaQHtMzMDxrNrq6-I-GvoDEpDhnv8CO2H0cUtFDXhk3i8oGwsKKbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تنها هشت بازی تا پایان جام‌جهانی تاریخی امسال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/99253" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99252">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCyi2M5KrnlChaOT4euxpTNotS1BeyRXYObD_lumJGdpDr_YxEVshCFnBySMXPt_EA_VK6O-BvS0Co-XBtfHcQfVCib4GXsskXjdRVOaV-1KxzaqNn8F7wBnN_kghqSh_nLk6Prw6hnaJVpqdUBIryftdRdw808IQaAs80XjT90UkHC0jDcLC-DwbVXHEdKQfRaIIu0-dFN6Zsl8DJ6ZoS86TNa7b1F0cJxmxE_EJwb8ERsXj3u_fFc7zikFvbUIv-jP3L76vhw7-ndlisaplY2wRHYM82t7Qmc9rHnFE6yO3XaMk3TxcDe-gLoXteNXyoJZBmqgv6PylQeoWNXN6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مربیانی که بیشترین بازی ها را در جام جهانی سرمربیگری کردند:
25 بازی - هلموت شون (1966-1978)
25 مسابقه - دیدیه دشان (2012-2026)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/99252" target="_blank">📅 22:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99251">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
یک مقام آمریکایی به CNN گفته است که ارتش ایالات متحده در حال حاضر مشغول انجام حملات نظامی نیست. گفته میشه کویت داره به ایران حمله میکنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/99251" target="_blank">📅 22:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99250">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
#فوووووری؛ شنیده شدن صدای انفجار در بوشهر، چابهار و اهواز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/99250" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99249">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRPohDOCtYTijLc0bmxXSua58o8wJZqC38Zl-o73-gM0AUZEvoSE_-Moo2N5GniFPPNIyIf6D8Xnz4vbytTfeVgJXgoTe4QPCNVqNShV9ZQIcP14lUVUJYJytcX8XMx0n06mrF5drAJNzWrjGQu4PJc_-ZR5eF86_4gatd0-PKpa4GyPcUkkqdvKzPL7awd8vH6C7R_FgSrdQ3pbmZLSOGpq_GW_4EYAGeEWhQw-yq6BM8KXgmEoJrnK9ZYCxRfCDbgTXh-t2g1E3rGXs6pXpRCciXGVNekpkQrgwytBsQUX8ZKLJ4j_pSjqeLKj4WmIOqc1StxzYIUxvdgL7SZzfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب فرانسه مقابل مراکش؛ ساعت ۲۳:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/99249" target="_blank">📅 22:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99248">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bsh0Y-44fBxmlwiPjvpsiTDW3GRVhB8vxvjIxrq7VGLjZcXo0MiYBIWo-ys2n95sOBxtmU181s7zWD_Yg_g3XMwBBamqlpQ-Ay6Kf979_WFCO39iobbeYMIxFfVH9Y5vkIeKxCmhUf9N22H8VS26Gwx26xmBiueyHDngKgv-qJ-5VbUnHDAlfREyQTllGmfmqyhvUlsbyL2OeMhkXbaIpM1INwasjxX7AejJELSoTbBsny055tY2kD-hMfxsFwbiXLVc6uUo2fq8N4M5SdgjzslRtIZPldAx1ieY_QmA2Dfm8EXLRC-ou59Gd96J7NXT9HEZhqvWQvIb4vDvoGrd-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب فرانسه مقابل مراکش؛ ساعت ۲۳:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/99248" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99247">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9IyyVe5K3GzykM2K_IbX7BCOf04Nq4tT4uhEQDwDaC1XY4fExgvuig8bbOEfVi-Ug3ak_KiT2fFZDjdCRnJftZxoSe6Ca5sr4UD0Kj9z6v5e1lp5C2ELopleSiG7PCb_eNsq_FVGw8iY7ltuFioEc-8fbRNAX9ocwsJhGseqCi95ns4SI5so0b1u9B-EDXy_iAWcrpRrIS6kbHhF4rOnOGlhoYLfiDLgVUWIAR9Jg1iRTS1c0LY2DypnJZivuzNlLD-xMCeAASWzPIWNA1rwWO1PpgabV-Y1hPYB-cc_EHTJojn1feAZw1Ne3RB4lcA83jzPJNCLHaBJoYi-IO-vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🔥
تصویر لیونل‌مسی با توپ فینال‌ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/99247" target="_blank">📅 21:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99246">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01bfe433ba.mp4?token=HChWGI2bMHhwh-UNCmyfVv7AgQ6FvjHYa-Mw9R5IN8Xcffm4HUo9g3WEhNpvLk-jCsbLI1uonwosBbZRv57QZYVmKkQ-B1oZROPdbslYthi0R9k4RDXfgGC0kicGMbEfpqlROxEDMv7ccuvXcVjxkhW4QukeeBHpk1sBUf4w3j4PjyTZEkIFmrPruo9tKO5x8NbeY0ZIWFQ2nhQMQ5UZudR8cNeUaUx81XtwM5pu7XizBgX-ey91xvl0cG_6Y6qlAQ517yisxvP_bbqMUck4FMqBf8jwrD71_eRO7et05v3WkxCDz9toHhAEVYTs8w9rT6nb8KlrqWvNAL4Mjyk7oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01bfe433ba.mp4?token=HChWGI2bMHhwh-UNCmyfVv7AgQ6FvjHYa-Mw9R5IN8Xcffm4HUo9g3WEhNpvLk-jCsbLI1uonwosBbZRv57QZYVmKkQ-B1oZROPdbslYthi0R9k4RDXfgGC0kicGMbEfpqlROxEDMv7ccuvXcVjxkhW4QukeeBHpk1sBUf4w3j4PjyTZEkIFmrPruo9tKO5x8NbeY0ZIWFQ2nhQMQ5UZudR8cNeUaUx81XtwM5pu7XizBgX-ey91xvl0cG_6Y6qlAQ517yisxvP_bbqMUck4FMqBf8jwrD71_eRO7et05v3WkxCDz9toHhAEVYTs8w9rT6nb8KlrqWvNAL4Mjyk7oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت رونالدو فنا تو دایرکت امباپه
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/99246" target="_blank">📅 21:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99245">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
#فوووووری
؛ شنیده شدن صدای انفجار در بوشهر، چابهار و اهواز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/99245" target="_blank">📅 21:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99244">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OD_UZ_e2hwzDkCyq8eBK-4CL9pVRA0g3R6lprSYdJh5mXcRtOMAMdtRY2SDTVM4lyqYqsRDFwdv939FmLADWoNZXvFZfQF19sK9wTgGLfS2g6iemlRKD8dy0bxWdtRSmVgLTW5u7Ew9OYzkxwA1ldn4DX7gmolyy9bzfScYiNO-v8XShWRZhzKRjHGCkchelrk2QrXAHoSlWSvLsEUxNVhK5XIWh6-CfPiZ4_btsrAGHDgk16GGk8C_9rp9oB8K980YEQLJ2TNp-x6FoJ1GBGwnOqBRamsjPmjyJQADJyJgP99mS43Hya7jRyAVWbul25H8NR8XadvnwdDTqkZhcnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🏆
دیدیه دشان امشب با ۲۵ بازی، رکورد بیشترین تعداد بازی به عنوان سرمربی در تاریخ جام جهانی را به نام خود ثبت خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/99244" target="_blank">📅 21:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99243">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jg_hTSzvK_mOnwOJGgdKdspsQf_92MimUVWDIaedmLWMVTc8sljsi2TSg7vCO0k4ALdhTeSNwyE1fgBjcQI6WB8rB4QzHYp4ZGIH9RiN7n-kqYyKwIgcTj9MGz69Yv7uJfhZT_ZsAfWqMm5JhD7bxOADz-axYL7hadcjfFGrw0cRPoHkBTy4MgpvRHiTc9VBNzqU_t3-CcVwWV8Phav5MYboIKrJiMVYGzSAH5ATQbrtigHfSVf5avB6NXLAKrH0rgrr9JKkK1CY7cLaKUyCGREEn39OuUazoFP4eQ1IQyioqiEc82sRvdEV63hcDbp7GcBB6in3Gh7WEXlRflEDWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: باشگاه چلسی از عملکرد آلخاندرو گارناچو رضایت ندارد و بزودی این بازیکن در تابستان جدا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/99243" target="_blank">📅 21:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99241">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MVk5lcNguR59PeOMsLp2m9vLw1a6iGV-fMbwyaqI9ToxH0CclqRDnzpp_MPz33E516rrTqL30YscBb-Zk1u4j_6pMtjtLkuRHaRBlg-LPss82mQxvHPsmHJXfejGZ-trtGyQOfpJQ4Qla2uHr_LeJ9F__ful96DkMrqdnuJ3Sg7PrpkwU-_0qMs25WKjRwh5Z6CCNnn__ekmWZccAwZOz1VCjBI1N0ZXBLvGwSavCAGcfA6qoQDF7WD1y4lFN4ke9T5drGWnkCWGJjlNph3WzuqaGLiTXOYibRdiAJiVUKbG378fTmpC7UBJyOvVPKt2O3IEKa052CnDYl1U9IgYPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B40zaVLX1Z9pYsgw4aqeu48luvQDpu5uX_NICdsBUJtkmON34uM5bSdY8RSlPPGY8RsfRB78Oqa41n--1EFYaNXEdkHOkGwc_VEs_fowji6CmsdgTC4dy4PEbwkFdot5K6DUcCRrWD1Yqj7Xr2TBT6Uopvqw2nbEwQ6pUCUKduVWwYLNotfGxe5fozRjvjg5KA9Z8MnVTuksEAzf857iowj-pDbLavnwgqdrWpobAKLUO1hkHQJfO3vtMe5kQorSUCwThwceVO9bIyzUH4iE5Q7U2-UgmAse1iVJ97tobatkfjwiRJF4uRXCGy4oPeuMz8dgLryQK42Tz7nU6CQVPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هوادارای مراکش و فرانسه
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/99241" target="_blank">📅 21:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99240">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1PdFxcTyJz0foYZ9kYhZ7A2ayVYIKmRULgieaPdZ_k9oa57h1cebc455YTbuW68fm7Pw1EZMvQ116Xm8S3j6411NZa11HN9KS4hkvFozV80OJHMCyCJx9V6_oDIRYVbOqfQ-3HzBDCBf2WEH-6rnEvWovZjBuWgR2ZD2Fnvr4Jyftg_YzB5Zo40MtRd6QH0hQed8FoXgxAcDMzRjPhJRVgT_0EtWoR5Cemns7WbgENAeZ_gIjWk3_NTOq5xp3kO96IrWJHnql9bXkiFCeRTa8kcBmhyUs3DppP05_zCYDtn2Dld7d5jr79GqOuBtk8siJOJhDlKSN_WRX5bAJjJtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔵
ژابی آلونسو درباره چلسی:
این یکی از بهترین باشگاه‌های جهان است و در دهه‌های اخیر موفقیت‌های بزرگی کسب کرده است. افتخار بزرگی است که بخشی از آن باشم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/99240" target="_blank">📅 21:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99239">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALNgGIFdIAYcxzmYKf6vaC4AlUjlnFNWAfMQHo3Nh8izdBjCUI_9ICRDnvVGhLcevo74M93jXeupjzeEQZmspIJQkmyj25_oNXi8mcJ0QrmPWGWUhRoGZuK2tGORQWSMQgkd8MurhfPHVAlyEd8-l3pGCzheH4fES5Yw-IipIV1YIcl-sncoL_plZ4UMoWG4TcNIbTN9tSnz8nhZR5M1fHzXVHNxgF8yzItmMr7Y_najTQwlXw8diqzqWZ3STUJTUInjDrhPg0EnQNZhCck98aByxNTU1XhHbFh03v8925yIWsrvdCDBokU7EfNeCdfaZ0hV3yMz-zwi_XsSoYYyiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏9 جولای 2006.
🇮🇹
در چنین روزی بیست سال پیش، ایتالیا قهرمان جهان شد و دیگر هرگز در جام جهانی، مسابقه‌ای حذفی را تجربه نکرد.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/99239" target="_blank">📅 20:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99238">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMP86KSnBVkYWffmgy4bM9h1_82iRNKm8_xcjzzBHjI77mvakJ5bttgi-8FKOFWxFDgzqu4_tUSzH26X-Hazn5zdyk1AhpGkMr1-Nd0WfDC3xdnBp8Y2C567fsza7ZZh2tUteAwG5y4sDorCsONaFC_P-yEBsqahUA8Lzs6YGt9NK0WAosCZhzWy8XBQ2lW7VlIXXG8AoF6FsOyT5gdVNhoJQQBumeJG8YLqaDLqkFeSeGgLA_r8UQQ_hQYpTvYvf2AnLrlizafkzQ8pE1Wqw3OTdXyVzKgSQZ8Er9PvDZhmoRDG5UiAcZJnuAOUUbW2m1YLJNFKHYeRkNq1Ev5e_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
🇦🇷
نتانیاهو: راستش رو بخوای، مسی 39 سالشه و اون قبلاً هر چیزی که می‌خواست توی فوتبال به دست بیاره رو به دست آورده و بارها شجاعت و بزرگی خودش رو ثابت کرده. ولی واضحه که هنوز حرف‌های زیادی برای گفتن داره. من در جام جهانی طرفدار آرژانتین هستم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/99238" target="_blank">📅 20:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99237">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJOE5q7awPifyKLD5F-NdPS-Wiv-RKwbXkHiE7uYrphktNdDHfLqfJKNvsTxvQZnsZB8TAR-LXhix4rlM20vNzLMPbdVjwRG2z6_FoqoGHbYsWS2VGJhVXIaeeUA86fNsT6czcpMHeftucEEzgI8qGmaRbkjWf5zfVtnPqKzSmkzVjygpyYdHs8N4bl-2_k85xSQlOtcwD12dVpvcZWFEvSI3LkTIirW3n4xIaZ6VeUbSoouA7wSC7iUET1yTBh_FrtObVW11NEaScn0IMwKfpWmGZJl_YDZCroISCSDLHr8Yz3jUiCHELpYFtCp1T36vrJvDfrqzJH99yy5jCG-5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
کارل دارلو گلر لیدز یونایتد به منچستریونایتد پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/99237" target="_blank">📅 20:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99236">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNydCLkvtR8tqTH9urLeoiYITM-ZpkPfiBieKYpe9wWc3-4qYFbEb0SHuzYdRwvOkkyVoPPw1pUFjfadf8t2qW6pSsEyWIaoUshYBeYw7CdjzUs_FrtUivWNNEWfUBmneIcIRCzP0FOcgMYE0USvJRnaVRVNQUL5RBw2zWGHRBf875MC2TswUK-rZ085DVzzAFfGka_vxrzpIYK4EtfvTlyJdWsu8V6zI0mfV4qA3IQ5flGS5ETnVrv2f38dIr271ZUqeb4qIv52jakb8tu3ujKImaChEaWn7oVutgyH9JPGrS7AU5ZNGC6OjzEjI53pu92snhbWjPBD46ycC1PtbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوتامندی نگرانی‌ای بابت بسته شدن تی وی تایم نداره چون همه سریالایی که میبینه رو روی کمرش تتو میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/99236" target="_blank">📅 20:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99235">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9MIMzoVj7p7qyAc68GNqtg38zOKsgDG-vkR4SwlRQr_birMdGFipyjj946fK7n5Tp8hfyqd0aiufr86KUMkwlvSpyoRt2ua3h1WkPkAbs9EOroojWFC_-FlaVMpueevGRqZ63Ip3tNUP4QaOdkn4VDbjyg9w7H95-4YMb2MssC1ZnKydylliakBHbXX1D_saABtNHUsUYtS8qM6kn7zqH-mb4MCFrnQv47JtcjywbQa1kiK0GqPHix2Bzi7vzyoNhGm9JFQzLhg0B56H1B5ZFjeT3FZN192jyvkw7neL2F4XHR2-4PUQUjrBOjQKes1W1z-OJNBWQqbEhk-AmMOkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇨🇭
ژائو پینیرو داور پرتغالی به عنوان داور بازی آرژانتین و سوئیس انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/99235" target="_blank">📅 20:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99234">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcN17fWIZAqG-aZQu1t9sZe8ARlKwMFWMpXFfwjGxf-Qr7kLXu9JwW_acobhhYjFm9oJvpAdw4bjEs78Bw8pDJfxp82U5nlsoxOkyK8TmPu2AlGQhtEjnyVN1wKsAOm1stOfAwfKtBvpOnN_Tt-y0lPIXKcHvX7eM_4wxgz7eq00y-YC1I61ACZElLmOJPft4PwC7xHYjf_e0eqbLlCmi3PCrjBu0ZOHV4LG3dLfOGPqNB5W2EYZyeVPgroJ4rbKczPSSJcf-WCrDIBTAqzOW00GAbG2vQpqzDlNfZSUsNP0TEQmqtZC2LhvnIVN0tL4U0xGBFb63qcayUcxE6ktXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بی بی سی نیوز:
قانونگذاران یوفا خواستار تحقیقات درباره اینفانتینو، رئیس فیفا هستند و ادعا میکنند که وی به طور کامل کنترل مسابقات را از دست داده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/99234" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99233">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66bc2aaa07.mp4?token=UHDZx6TzXow7moXi9raXXX_cr7vlhwsO5L1NX0yyNITmeHnWkL_C8F_xV3G0JwlkuuOrm9gpgQt8dn2RTc6J4QohduWA1NM6M1uKk6en1NdiEA42zygy0Ar1bMLQVYpcJx-jKISu8HkPoNOlotAwg-PGp9F6LD2bO9XoIlx_BLmguf0zwOHgviXo_RO41bmV5I7jWE45ZYG4EL8U5yW1tmzFbSga45UOmmd_69k4uK18b82ZYhQl0ZQyyvWmzQO_uLR8l1jZ_zs8IkNAltkIWxncrM_GzeSOTy0iklkdrrtX82C47k53vaOBNQfaBZqNhoUq8mNj6DzdOVrFuKkHKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66bc2aaa07.mp4?token=UHDZx6TzXow7moXi9raXXX_cr7vlhwsO5L1NX0yyNITmeHnWkL_C8F_xV3G0JwlkuuOrm9gpgQt8dn2RTc6J4QohduWA1NM6M1uKk6en1NdiEA42zygy0Ar1bMLQVYpcJx-jKISu8HkPoNOlotAwg-PGp9F6LD2bO9XoIlx_BLmguf0zwOHgviXo_RO41bmV5I7jWE45ZYG4EL8U5yW1tmzFbSga45UOmmd_69k4uK18b82ZYhQl0ZQyyvWmzQO_uLR8l1jZ_zs8IkNAltkIWxncrM_GzeSOTy0iklkdrrtX82C47k53vaOBNQfaBZqNhoUq8mNj6DzdOVrFuKkHKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریزمان تو اولین بازی دوستانه برای اورلاندو سیتی گل زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/99233" target="_blank">📅 20:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99232">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-q3YUKQNHCeWjbIxh63sjVNn9y4Hcp5iB51Cm5Wk9NEpixXgnb9CFyMnxSgGdqz_Vvb3-8ydJLMnpGkD4mMQWMnuxkSzHBrJoBdh7PjoM0RaHYDtPBiML5SjNY-ChbMacZ_c7XFdmENE4sfeyqlk7xgNG7NF3Ddk_ae6WVBZjgPADseDR1nqy1uh7LIuQ-D6D0GjAPrqC42C6FFkwpCukcL6u40BUg5H_6-xNDNtt-yZhv9-aBFq0DXBFOVcd5aedH2ulVD1r2otur5X6RRhkyQFlT_auaYRYTLoMZ8uYX5YqCxrLlr_IuApjPSHZy1-Fs8ca1gQDvBQJ3hNWp5bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
مراکش
🆚
🇫🇷
فرانسه
فکر می‌کنی کدوم تیم برنده می‌شه؟
👀
🎁
۵۰۰ دلار جایزه
بین تمام افرادی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، طبق قوانین سایت تقسیم می‌شود.
👇
همین حالا پیش‌بینی‌ات را ثبت کن:
https://t.me/betegram_bot?start=p4_r4EF37DCE
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/99232" target="_blank">📅 20:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99231">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2de986e6ef.mp4?token=RcNAVtYuSuHZKta1Go60L5e974nQtW2K0mNsx317dDGXtpUGVPO6YOJ8_MAnqPT-yadCLFSRvnrR_xlMjwLUlvXlKAa3gROWWudpmZJZoOtPH3hHnR3ifBWSIb6xbXtzZBIIYPlJAnjsnNso4E87qFQONm62oKs31WzHlTHBMFwSFkj84AXYkRaju3l3QOflx8ZI1ce8ORw6N1_4oxGM0KkR18oOvqFEBoEiSmjD3JFXBPHZ5Rx5ssxfx5ukx4MitFJGp1Gu-l8YfivaZXDrVagznnIhHA_z14tDVbRIKJW-nsO6hb1HaNxTzTMNMegk9hodgzPbqSzsKC0_VCvPTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2de986e6ef.mp4?token=RcNAVtYuSuHZKta1Go60L5e974nQtW2K0mNsx317dDGXtpUGVPO6YOJ8_MAnqPT-yadCLFSRvnrR_xlMjwLUlvXlKAa3gROWWudpmZJZoOtPH3hHnR3ifBWSIb6xbXtzZBIIYPlJAnjsnNso4E87qFQONm62oKs31WzHlTHBMFwSFkj84AXYkRaju3l3QOflx8ZI1ce8ORw6N1_4oxGM0KkR18oOvqFEBoEiSmjD3JFXBPHZ5Rx5ssxfx5ukx4MitFJGp1Gu-l8YfivaZXDrVagznnIhHA_z14tDVbRIKJW-nsO6hb1HaNxTzTMNMegk9hodgzPbqSzsKC0_VCvPTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش یامال قطعا یکی از بامزه‌ترین و کیوت‌ترین موجوداتیه که تابحال دیدیم
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/99231" target="_blank">📅 20:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99230">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzgwGbGhv9X3KsbjN9L36qOcUZXenqCSQH4kITAAbhKDfQ65sdpgomNAYPv87cw311geIy3Y3rkDcrEwXH2uwUWmrXr-u1Amzar1PArqR73t4Re8XVBHu8x8ZTyjwXJhA2ryWZ4m3fsygqDSj1KhsI9tYYmFZE-gtz8zp6MATUac7oL4YCxthbjFhWZnF794WGh6AsMOzatq77cNjJv4MSgfBKu9HH069e0PfzNVhB6lWeZnYodxcb5DsKxKE2TmXk0_p-tozUoKqMhyiWuitCKsOKh3_SyZIa_oc2gtE0UmsoU4mxbf_MVyVNt1z_BiMPjvSHGtOgX_E2AA9JtB0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
لوییس روخو:
باشگاه بوروسیا دورتموند، پیشنهاد اولیه بارسلونا به مبلغ 20 میلیون یورو برای جذب کریم آدیمی را رد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/99230" target="_blank">📅 20:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99229">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tg9c-qXofQG-SoZYIlT_dJR_iRy25UKnCk-T8_iqQiv8YtHM6qXA85j7CrKYkcqP-OKfqep_0jARvQlUxh88axburxIfp6mpiQX3kmbY_r9C05EOivQyW4Zg_FmclRWehvBEFCqulNhYTP3vexf185Y7UrNj4WXpE0S9nX_ozHLLkBBAsTAh_A2Rv3o7TDcAfhzptw7m-kxLzrc8fSaxhWkyELjKaJt9H8i-XIXZQxWw0RhoKyyC95yB3wSwe_y7S214HBvbCT0iAQ2J_ymLB93Gi82UUBmrE0Ec03DR2Qmrb8ZXu_m2fnd-OTSRYHx1DocUJnGzhk8o0jWBQSNoVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔻
#رسمییییی
؛ کوانسا به دلیل کارت قرمز مستقیمی که گرفت ۲ بازی محرومه و علاوه بر بازی با نروژ، در صورت صعود انگلیس به نیمه‌نهایی، اون بازیم از دست میده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/99229" target="_blank">📅 20:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99228">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzvsWEoWuH8WASo46RI2_mXfpgmfSBkDgADFFrgD52vwJ6TMJisibcyqs1oNCe8hv3PcofRm3kfGvsFG1T3uAgo25GyxVjbu4guIyR7lwtZhDBKJPYzxq_Kqv90X0IQftzyVr-_mIw3jbNJHbln8Zgr9TZQ_-nULf7cNoqkvuEtRpL1A4QD-vlR1lykHLbOlcfwlV4BWWEUMltYYGswex6lT10xMoLlfJfyjHUMXFDFSkhoKNHwJiGgZaXbrIE6bM2yBwIt7nFPQfoomX8fz4L1sT2KmnZHOlfbBgfhbUZGuDzA4-iHCYZ8VXK6AbEAFMS_ewBzF6N-xG_efRhQxQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
#فکت
؛
برای اولین بار در تاریخ، مرحله یک چهارم نهایی جام جهانی بدون حضور آلمان یا برزیل برگزار میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/99228" target="_blank">📅 19:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99227">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jU-UE0yM1HwCX1DX9a97wKBk7dUDmMa9yvx3P-LiszneChi0Fg4do-QCGm4kZDhGI0GBOty9syo_uNhcmSMGg5tfHdR1SJdhgxbuJ7vRgpm9WZz1zhpsU_GekYfVfr2Kr__Tei2Rv0WU9Cmdy7eBhAqcRS0PB2zG1qhWsRy-_KLr9AiD3KGmWONJVNxtfPIBr4QSB9DDN6QaueExRkrHd1uf0wZP87AhTLifDJ8VCISPpGrHM6UKKEUYeDfjF_Vv10GUxSYRZnFb7DUJ8QuOEnUXcMJROmnb04XWJ9kat6TB2kGs6znIl9_-cun1IFw5PN7k659Fuv28IRczR4Bumg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بانوی پاکدامن میا خلیفه: امروز من مراکشی هستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/99227" target="_blank">📅 19:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99226">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXClwSzkntCEzuc6knHrskKA--3yqty86gLgHMQ7UX0ykwq5oXkRJcsczejvKUXIZ_4h2IktyHR1lMc9ZnGhKz7qM6gICh4dCREXAcCE6L5M2yT12rXxywyb85jBSZSzrpzF2COEvUernTTCCsc0L9fhEVuNcuRFd8HfhQdhVbLg5_bwkvd4-1alXLCOyW-3-RRp-4WVUtYxoUKYduzYFP-NcJBmC11y4sHXkzNNOFP8TWC_x0B7iQMmx20eas2wKyUr9EiB7nCURnNPGaiOlfF1nt86rbrvkCPcPNoeg5jJ4s4gQ3BEsP5QfEiuaeUkzcb3qHREaSrqks_x1Kbmeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔻
یادی کنیم از تیم منتخب جام‌جهانی 2010 که با قهرمانی اسپانیا به پایان رسید..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/99226" target="_blank">📅 19:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99225">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvA0RcHD8ZsMfWh34_xrRjCVDM-iftZOnhRle17JzPsjMepGEXb6e15W-Mc4A1_7Exvtdx5qpXPiN6AlEOLUgZ03NkaGICkN0tabwckZy-hP0741ajYt3WBqBJMR9gj87IFI1qbUX53xYn2qxGm_nu_7pivVZPPGiO06_J6JsUQeVEo4j2xDWc1A0BkX2H1GX-cNq9VX9F0m09uGnHwS49M6CzkrJcIpeDUncqLmutRxwhAYlmWG5WxY8j-k5Kw5MnbBJTgBkzmM7Bbg5XrjHcACWITH20gXNyPL5ofDDDyTYfXTezOyPQj4aLcRF5UcwALmjbzFAUN4gidv_8q5hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پائو کوبارسی:
خودم را در حال بالا بردن جام‌جهانی تصور میکنم.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/99225" target="_blank">📅 19:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99224">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/99224" target="_blank">📅 19:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99223">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aP075B2GhwedAweAFGdJcEKtk6ZtJKlRYsYW6fsKbhSUbdFhI6eUQk2EY47XkdRz3rLdKzjCXJm0nBXnk06y4EnEKtl_WtlgXnhzrQRHmTiO_UV_9FWSOheLAZZYtpzm1v3vgOxOzyF7ecMn12dAC15SsEx_xX5fFg_yrQTfp19s5gJGw4NPMqIfXY4xh7w6jcY-dbTFrRWeuP2mepWt7hwcEcq9K_wCvTMZatGPjmKrjaB8NURPvzoOeOnSVN-g1fQNmo44DoCj0Ce64isOkG31E0T8_Sr3lpgT2XKZdNZhTrn3ENZdMfrH8AA_U4p5VoywKqlvRanlqVzHoYLUJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/99223" target="_blank">📅 19:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99214">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EK-Ht3pQgOwSZMyAApsHc4kRlc-gDFXSNYVb2vlBKpNxSOXklv0Ts5X4_Iw_4PdDnWeOu2WwX27UmI8dVh80-g9HUvpmZNbEkpAZ6hOaHkyIhFHLVXYCmRi7npF6Ou3utuqjgcNG-_dQgMHJnfhNxni2ANWx1CgdKaIFeALL_p6C056q3z1aCiKDXXkpgUCkTd8f5xOAC5cSkcf-Pz4PjAFwtjEy4hteXJ8C-qrLv6LVDVpMKZ2rC99ieFljEKFwgy5Txz656Gah2BnTaPn9UC7DRgCcbtof0EGz6WDnHYhr895rugbSCOCExa7qYoH50UWqij2bkuHXdUu5wBRLhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RfAXpWji_4-qUzahIEjtH2gMI-ldsqgGBrM4pFVn_z6KaUnnd2PFG2I1HuB05cx8ia6Bgr6JQDwiwAvwgKd9XrqOXjtRD87nGgKJFmYgXB0ucOE8pgiq5XsA_t1Z29zOIDWE9Xe7dOeA3bApuHa1eGo7bbuhYgN4OB2CB4fzH0HkGL98g90rD5uKAyPMaCv0Lerc3r5pW0GppjEpPs4GVkslIjlyyubfdfoqvst7ynjZ_LHSxta4SMo_mPithCT91-tv74hupJLtBF85BZVDJIp-GXjSOt7ae6qInvQZDyj1eVufwmnHXSsY85QyicMlP9nS02SaTRlYMR2baypS7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q0iJMXWUF_6vPlJ5QL8BTc8N3hHfLvuIAGX888HGlKqLz1nVTzVEqqumxDZ0eBonlYIZRfvbGZzbXGJUnqSPVHRsevHXoteFwkXWuS5GoVbkoI-MUDv-D7BOfOaS1ew7GBNh8Zelbrc6ST6F9eoc3EjbNhtkFqsevGEqwbVoirUqXKeTIxL_jt-nV55aujr7Z7PnNf3aQS1SYxVbAhPdlFXlNjYID5dNjF4tdlmMFUfTHJSRy_3xMafarCwpUfock5zr2VP6LXF5rwzjDpSlZUi0PmEIaHAsBs10b_0iEpbMu8VLD90cRdQvDAeQImxkSXaKjvSCtXMAkzARqpVvKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I9OxsnKpcTG7kc8Nl43WrnJC59faAJtD8vNR3gMJM2_dW9KR6KAFTl5KRq9fqYAvei8TL78BJWEpK-GCI-ZNKuTWUoXUfBPJkUpQr6BoM2w1W8oyYlbjAVK6286ihnpk9qH5fWdf6QTIM17eRABBspsaVdQF1vLU23g6ptjlm16g23OpxRtpDtu398aZgJDhvz47rlz5bL4oB31jr3m1JXAYYT7B5vXM7cvyFmylKBd8b0run2bu1D87OC6nnFgDl1QlpknhsIbNnh8IBs10XuJDNZ3-oFaTdku_m1x82wetzUYbjPw6vU_e_ryYwD-l-OS7rdOAYkPOBaRESVVWaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/faylKcVJAGahovOVKv7139MutAiaIn_urUE5Slm5G3Xd8dPB9GsRUpCVqILTOuZI7ubsnlU4GixavHNCxlNRnDrOnDeEqWVwqLzGQBk_7mF3vin1mzO-Z_DNSWvb3s-OAKj8Zby1CiDkj4Bk8Ksj-GIcA7mnetb19S1ImCG-LLMiedmVRMWcIRu0ck8IRPZWlub-TC13Nd-iNHBxY0o8wtw1zggmHt-3i2IweeZAW_XJaxLvw8ITItWSbsN6Q8ixLgy0sgkf7PQjHVjIgPS3jlx8ZW4BDlNC-1lf27xZmKn-AdsS_CHW0Gey7kTtuih1CBqt_7R2eLV-LJISnGGg4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZrR1WAx3qRdTQF79E15wDlupPKWhhjOJzcWtJNHNP-vGTZUBipLZcfANB2j-1jIS-GEkdZerh1AZZSWHKQWBu3MmGv067ALVs8sJpr97cgM5Q-JRj4oIH-R2zBN9hR4op-4cQg8cJC3eVAmLblWAW4cGuYV3GH9ZrFg-8wP8R6Let4_t1PdH6-JwxEUeM70xW4c36JEyWHSmSxe4B3s2g7Rd6TM2GcD3g4mFIGjlwZ8MmZaQGqfDmyy8iVekEDaeyDEPj0_Qh2IXvSD1hZ26QjBsr1D5Q7PmLzMqGIvsuqQY5Bcvj_wziypsNzJLO3MPJj6IsMxn7Vpjslb9mCojzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HANMN7VFg3Ee0oD4ITHKsBGJJjbmHJLpk8AFUKRJnY6DxUdIlLhqmtp8RfnaME6VTr7BOBhWflOEdT297AhoXN4mRbHxUrYEkR7KFpbvWDK48FLEQ08oMU3ulhS-y5mHri7Ez5sOuVdZJCeMUcjTaeMUIRS4gaOi9lRlLgA5BWViMI0cMxmps3dfhromcxScRgo51HOc7MgNiZmM-G4hAkuu1qyRy1kqok5BTBL7mU0IF5eMXgguMeQkr8xsVwBJmhYOJvKrr0pmeenygkonC6JoYhFLgPYzzQgKDKuo2tMnXH1ZEHtMM6OskxAuaztRUfNkgCYVsjQlgDsyoofVAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C7K7uRx76iOf3WmsK213vZcJ9L8IpiIkw53NalOUR-5A0wCsa5UBVClm66HuyT1vHw28XUFCxc1zPBIT7fMhethVYhHjgfc8THQyPYa6_4egUqbrJ5jFFnXpdqMxHzxyVUamqi0A0QHPMBgh_sYZDObCBUWb18GnmJ2MHuk4rJPCREvHAvY3wcpeTZDa3rlpBV0dyNzhtOQRWyhEOBs76Y4hhP65GR-E9GQAzfvyFnJRZBaDXh2h1To-4DdpqAjwUy8L4i_IoPvncaF1coMImYHzHG1BGSdbjuZEEY255U00-ReZ3-o4Au4mFgkHg2REqRwpyQeiZYivPpbN1vVaLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r0pTRzjnFShgRv999Q18jSXWfbOj3B5x5k1wN_Mhwgh6TNsUZvrGPto8VUejHDf-35x7We6x_KKQMi6ExbOi1k6Rk5JZ6hHFViqdh5CQHOmAww_FUm610YesXIDG8rwNTWkg7I-zPS8ntEoDHc3DA1h_fM9i2opYlV2Mn8JjyoXDaHF1fKYtJMbyNo1tDSIjA2Artj18bHtwIvH5UUGkY0LwIniL8MFXI2fGPzlqdWl8I4Y-6NZMbkfkzoGtWZ4CfJk3MkwnOVTWH0Scu4w5Z0s48oI4pftXX1xfwSIJFxsNMF64Hiv4shTkTAu3koblUBJfHtWQG54HCJ9lHJ9QWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تتوهای جالب تعدادی از بازیکنان فوتبال
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/99214" target="_blank">📅 19:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99213">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAhnEmzhgLzCZUnuo3KEt02xAIQAFWhUccemWEwTEW6khiGyMYBxvD09kKbvy1b31MwobogqP8MblbM5h1kThccyfU4afvAuKTKpWriXrlxjql14jw5TUHKtsSAwtzGckneG0AL2Ce6p_cwJlX4entWL7aTIy5zyAAwCmrTW6aQMLwO8ugFz9S7BGoBrhWM_eO4eue7Tk7VB0eI9OaCbKKY75i4QOkJcbPlTX13DaKKHG8Rbo7KrOMXEr9Z730C_ntfuBM_5UNMZfzrr2qqvHoBwpJR451Cb-Et56F68P0diBe1QxTxDkVi9ExcksJ6y1LAlSBsawk-lr3SNYfWi9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لکیپ:
اتلتیکو مادرید پیشنهاد خود را برای جذب میسون گرین وود ارائه کرد.
قرارداد 5 ساله، دستمزد خالص بین 5 تا 6 میلیون یورو در سال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/99213" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99212">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdnyFaw0cAM6d8qBGKz7gAZiheZd09lDEhodiQ9KX37AHb3v-CAkgK9saTxHIv5Cx0mBC0Owa2zqpvS3YWrPzGZpkpzVw3N0hezlUz1C3BgBetWTrvBvWZJJLbBMg_WzcEVR4Gglzhm0mLTNe3xlboCFYO_gKXyxSKAYk7NE6plZybAKCPXwbFViK3Z0AZd_JlU2ARmcKEsYaQiSCg71YWBilPBD6aGtpy3gCvW1pjVGB7Rj8-7vbQPmfj7weHWwQatigdu0M_x0GWPVbyJObnF274_f-R65jI6AAbENa145d7O2GJQXSyMXdXg6hTwSznB0zHYjnUu-5LS_TRQtng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
لحظه امضای قرارداد آلونسو با چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/99212" target="_blank">📅 19:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99211">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekNThqo4tRTxvWSSl7Uw2bJXxMhicwHrHh9saushi7xug3bhp-U1qzhjitKWGo65cM91tSUyKMmVWjdBIES_SlpUhNLsTqRlKEvxrRGQ2ov3HSk5ugZNKklDl8e669_3RcrkynQFfbhFme2MCp_e1rh-bNbJu_6m-4pk2qquXvvJL5my5E7i3zWFDo8UaJIl1evvmszrb69mYmzhFm5tHaLesN7eSZbc-B-CinL67i2gmksKOS5Yqe-fO67VnBaoM93FpgogGsj1rx7klcLOLFKlGQdM2lp8hssSNaC6CEJzPbL_jP1Vsir-WuKLeB41HFbNx57PrhDusz-qvzhMjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فیلیپه لوئیس رسما به عنوان سرمربی موناکو انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/99211" target="_blank">📅 18:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99210">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3e9304b6a.mp4?token=Z8RvVIewz-AO7IRyXArqWkJup6H-9UMefluyBMkpSqTHybZXiIcVUdlYlWKU2xminYTXU4ig1qOMUCklhnpVNMMy5vs9HLjfMUxnwuuq3OeH6ZZ0wwHtPJHNUvyNhXGUVedt8KaAMpLRwebM_nnktZWIOF-LFC0RAneIGuGvtDJR2_NzpLI_fbvf5QrJLvPcnaWiy-zICZS2Hb7XxP8u6m_bmHsHL0RlXtDFWAyJmTZ0ZjftdkmTpcc0iaAm8egMnLorU9aGvXBmM8c_2UM7YB0_agD1sWlHGp-0SuiJPuKqG304hqwGqlKVKEfW1pZx8uVXa4RtFgR4z3BxAwe_lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3e9304b6a.mp4?token=Z8RvVIewz-AO7IRyXArqWkJup6H-9UMefluyBMkpSqTHybZXiIcVUdlYlWKU2xminYTXU4ig1qOMUCklhnpVNMMy5vs9HLjfMUxnwuuq3OeH6ZZ0wwHtPJHNUvyNhXGUVedt8KaAMpLRwebM_nnktZWIOF-LFC0RAneIGuGvtDJR2_NzpLI_fbvf5QrJLvPcnaWiy-zICZS2Hb7XxP8u6m_bmHsHL0RlXtDFWAyJmTZ0ZjftdkmTpcc0iaAm8egMnLorU9aGvXBmM8c_2UM7YB0_agD1sWlHGp-0SuiJPuKqG304hqwGqlKVKEfW1pZx8uVXa4RtFgR4z3BxAwe_lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ می ۲۰۱۷؛ بارسلونا مقابل ایبار
همه‌چیز از دست رفته به نظر می‌رسید؛ موقعیت سوارز از دست رفت و توپ به وسط زمین برگشت… اما وقتی توپ به لئو مسی رسید، غیرممکن‌ها شروع شدند.
یک حرکت انفرادی، عبور از چند مدافع و ضربه‌ای با پای راست؛ لحظه‌ای که دوباره ثابت کرد چرا مسی برای ساختن جادو به فقط چند ثانیه زمان نیاز دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/99210" target="_blank">📅 18:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99209">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8sF1HaZEE7JwymtM79k0x4dnWxRVJejWVz6KNS_at5f1nK9AmFWnXlScvcdwlxa_JkVFu-TUb990PWtzpqlZPcMloj_1owGTL5QgFyPvOt9Nq9aXcBUqqtdkIOBRdX2STgDtNot_9jmf0rz0hsEd2IA0Gpo-mCo3pGDpYD9DoVPuCTdOLcqeaCrgxNva0FiDb0ds1juv68AcUYjO6S-0u_wlD-G5HwWX_7fT3zOZIT-URRxGPRrk8M4XN9ZU0UZ6YJEHZyGjmoPbmVii9euPLBijEzgsZ4TO_1ylPhdjXhArfEQ06Sha74uJqyhOOoxrt8qF6U4FNnq0ibgrnSOtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار صلاح تو دوران حرفه ای خودش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/99209" target="_blank">📅 18:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99208">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMzJ3-EEMMTrcqN_ja93cc6u8TwtI4qL97rBZPlTaSCXuBkdPx1kaD4TzGuUlixGUFRSmjNnPD_rlJefZaadvdVmxyjFoje8uUerW3Y7p3bQjOQDxKuvUKlY721kYIJlh2fiXRV_ZpcXfgcnuuPKAVyiHdb6uPUQ8wS_gAScKLnzJUHkTiT-ShBXAPEEPVwdJEsxsIxXicRpmcHRYkktUkPn5v819IFrZYhbOiJF1uGoGCsvAOn8TefVzJBsCmD7DUgJgBc5PnsMfowtQQmSzCL4k50lIRQbT8aT7zVU6Qz9aLM46J2E_qz-Ej6i4ReEDsheJ_eY4mgeSXiBU-Sorg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولیسه و ست کردناش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/99208" target="_blank">📅 18:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99207">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4532025b1.mp4?token=cx2tuP4Z-I47IILJ95mf1YSQL--PXEKZ0CfHIfiaAf3sMu-mcoWWF0uhJknLUsIiC9wOtO3INOTnNNyCv3CRto_nyjX5O5kFn_QHLQXGtXG1zr7n8lEt7CxkEOEWCKWPofdlEjY0WZmhvZiHtRekJ7kJ1QoUu05L3Id8CGncNv1iHrj-L4pTGDb91-Km-F361TwDl-NLoZRHCizwhGqUqh21bfETydwWGPxG3pKY9QZ1FxvTZ6oacAfPsEby_fANkjdnbHMD9sMSxQgxxeE8hsrhShPY5Z44-WNkFy227e3Zm079FmQs4zx1nQjNMtKOL8GGdX5l4Hl1P0zu5qjM-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4532025b1.mp4?token=cx2tuP4Z-I47IILJ95mf1YSQL--PXEKZ0CfHIfiaAf3sMu-mcoWWF0uhJknLUsIiC9wOtO3INOTnNNyCv3CRto_nyjX5O5kFn_QHLQXGtXG1zr7n8lEt7CxkEOEWCKWPofdlEjY0WZmhvZiHtRekJ7kJ1QoUu05L3Id8CGncNv1iHrj-L4pTGDb91-Km-F361TwDl-NLoZRHCizwhGqUqh21bfETydwWGPxG3pKY9QZ1FxvTZ6oacAfPsEby_fANkjdnbHMD9sMSxQgxxeE8hsrhShPY5Z44-WNkFy227e3Zm079FmQs4zx1nQjNMtKOL8GGdX5l4Hl1P0zu5qjM-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گل خودت رو بزن!!!
🔹
با افتتاح حساب غیرحضوري در باران بانک کشاورزی، از برندگان
۹۳میلیون‌تومن
اعتبار خرید باش!
🔹
۹۳
سال قدمت
۹۳
برنده در هر روز.
🔹
برای شرکت در ‌قرعه‌کشی
اینجا
رو کلیک کن.
شرکت در ‌قرعه‌کشی
🎁
اسامی برندگان تا این لحظه
https://www.bki.ir/fifa2026lottery
⚽️
فقط تا پایان بازی‌های جام جهانی فرصت دارید
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/99207" target="_blank">📅 18:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99206">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdd3eab163.mp4?token=vX52_ZA5rcuKuFmsycM_YUBAWgeKydwpvo8FDjqgQJC5G8B2MdAYerDlhBvHTUNA-ZbI8QnfKrj35byG5KJbYbEWVdQgmSaPpvLyyKOcjJeu9MsRadWEQH1olCMU774RbY1kDFYIo8aFMxsG1a2LIIR48hj4B-AASV0gBXrrMx75xQ2tLgXqqaBoTPDEnDQ8mLcug9qhAPWDeg2ruo5SQgncMgZRO8fqnMdIHLERKkUID3fAk-0wssB0zPslHo0VpxGFMhSZURWG2ytWC1lDl7Zbq_KPQaj2a_9DtpxkqI2XICydGzODytlE7zMTdbv_P-wiLFj93p49Ualgy2EeqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdd3eab163.mp4?token=vX52_ZA5rcuKuFmsycM_YUBAWgeKydwpvo8FDjqgQJC5G8B2MdAYerDlhBvHTUNA-ZbI8QnfKrj35byG5KJbYbEWVdQgmSaPpvLyyKOcjJeu9MsRadWEQH1olCMU774RbY1kDFYIo8aFMxsG1a2LIIR48hj4B-AASV0gBXrrMx75xQ2tLgXqqaBoTPDEnDQ8mLcug9qhAPWDeg2ruo5SQgncMgZRO8fqnMdIHLERKkUID3fAk-0wssB0zPslHo0VpxGFMhSZURWG2ytWC1lDl7Zbq_KPQaj2a_9DtpxkqI2XICydGzODytlE7zMTdbv_P-wiLFj93p49Ualgy2EeqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇨🇻
تعطیلات دروازه‌بان کیپ‌ورد در کشورش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/99206" target="_blank">📅 18:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99205">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a3f6f2a0.mp4?token=hoxrfsqm-NuyPthF7sCkbH343B2K3Fb7FPpTPnZr8PYEOD6c_v_BmzdsTpz8ejOKWH6CQRZs8S6a6QDag_G7ZKZWBwdRaNKD8dwMcpGagy4bXiYZxRTD1HFKQpZYqRECf5uTGQETC5aCdNyA_hxc4lhCRax3eqUddrkV0yAQfsOHcQzH6dfFwyFsH4Cy5XCGoFJR6P-3mvwuTYUqhGJ0MsbPijIF0ttVWJQeeaaYOe9angn7ZoPpYvLHYl47RQwxYffcClpuVXdMGXO_zqkJYMgG6dWA5vnSEFPfEQwhG0Mr-EsG8o4y0HqJbNhEKvr_mYbbbHRjg4GTxsNoIslcIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a3f6f2a0.mp4?token=hoxrfsqm-NuyPthF7sCkbH343B2K3Fb7FPpTPnZr8PYEOD6c_v_BmzdsTpz8ejOKWH6CQRZs8S6a6QDag_G7ZKZWBwdRaNKD8dwMcpGagy4bXiYZxRTD1HFKQpZYqRECf5uTGQETC5aCdNyA_hxc4lhCRax3eqUddrkV0yAQfsOHcQzH6dfFwyFsH4Cy5XCGoFJR6P-3mvwuTYUqhGJ0MsbPijIF0ttVWJQeeaaYOe9angn7ZoPpYvLHYl47RQwxYffcClpuVXdMGXO_zqkJYMgG6dWA5vnSEFPfEQwhG0Mr-EsG8o4y0HqJbNhEKvr_mYbbbHRjg4GTxsNoIslcIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نظر آرسن ونگر در خصوص حضور کلوپ روی نیمکت مانشافت
: کسی شکی در مورد کیفیت کلوپ ندارد. اما همانطور که بازیکنان خوب مربی بزرگ لازم دارند، مربی بزرگ هم به بازیکنان خوب نیاز دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/99205" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99204">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/033b9f8094.mp4?token=M3v4o5MDEFuvE2QGx_80aWv4P445D0cUTf5dqblrOfghRXWYiUGS7TAsz3kA3I8fG5zBl1IrlxiVMCx5uzVW731BJVMzqIdYwwBq22Ivw6Wy9mjexJXO9C-9FX8B1nkaE0e7Qr3QDr7j14P4ceaaJTHOoQOhJiFEFw-Er0KlUBan6pJgVnX5Whpy_adzw-CRap1Dfu3iCxDdWbit4zQoQ23tSjgc_8IkPOOHKq-K9Az33RR_q0ltoYQP96N_i4kSadECqSKA8QIEbXxZCCGHWXB9Vt3aw9NOyy6sSWPaC4NTgGc2Xz9UElZwnG9ojs6KX3fnwS2sDc-Wn4B8BbarxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/033b9f8094.mp4?token=M3v4o5MDEFuvE2QGx_80aWv4P445D0cUTf5dqblrOfghRXWYiUGS7TAsz3kA3I8fG5zBl1IrlxiVMCx5uzVW731BJVMzqIdYwwBq22Ivw6Wy9mjexJXO9C-9FX8B1nkaE0e7Qr3QDr7j14P4ceaaJTHOoQOhJiFEFw-Er0KlUBan6pJgVnX5Whpy_adzw-CRap1Dfu3iCxDdWbit4zQoQ23tSjgc_8IkPOOHKq-K9Az33RR_q0ltoYQP96N_i4kSadECqSKA8QIEbXxZCCGHWXB9Vt3aw9NOyy6sSWPaC4NTgGc2Xz9UElZwnG9ojs6KX3fnwS2sDc-Wn4B8BbarxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
نظر جالب مرتضی تبریزی بازیکن سابق استقلال و تیم ملی در مورد اشکان دژاگه و مواد مخدر جدیدی که فوتبالیست های دنیا به راحتی از آن  استفاده می‌کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/99204" target="_blank">📅 17:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99203">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15c8dc00a6.mp4?token=AD5Vdy5ONf0Y-Ggl-nt_yFEYjBzFaMFq98gakWgddCygHwKe8M-sh_Pr46dXKc0YBB7iQu7dwM2c2euFHXPBVRUlYIHPHLV_0Zm_vfDdTyolZB5LFVgcLPegDYBJ4bXjpcZnRXG_OSgAyV_OcEwxmzfuy5BygpJg9yK5hZ-ppi8DYc9hRTgYWVlo69R172qi-3lzdqKzKc95DeIgLNED7Mp3UXO2XTYPITL_JTAKRm6aKnTzdTTJwicrbraRw7phg4hcEcsJwor-_qpMvc1D-0o_4TycGyfB6nGDny111HTpvoS6UqZM-TaZ3Zan775LnTR268miDXTNMdsOBW0iNDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15c8dc00a6.mp4?token=AD5Vdy5ONf0Y-Ggl-nt_yFEYjBzFaMFq98gakWgddCygHwKe8M-sh_Pr46dXKc0YBB7iQu7dwM2c2euFHXPBVRUlYIHPHLV_0Zm_vfDdTyolZB5LFVgcLPegDYBJ4bXjpcZnRXG_OSgAyV_OcEwxmzfuy5BygpJg9yK5hZ-ppi8DYc9hRTgYWVlo69R172qi-3lzdqKzKc95DeIgLNED7Mp3UXO2XTYPITL_JTAKRm6aKnTzdTTJwicrbraRw7phg4hcEcsJwor-_qpMvc1D-0o_4TycGyfB6nGDny111HTpvoS6UqZM-TaZ3Zan775LnTR268miDXTNMdsOBW0iNDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
🇳🇱
به مناسبت بازی مرحله ¼نهایی آرژانتین مروری داشته باشیم بر بازی پرحاشیه دوره قبل این کشور در همین مرحله مقابل هلند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/99203" target="_blank">📅 17:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99201">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N6X0vZUF0DlITRToNilFVKYsKI6puuNjihiS6uhdvvdJHWHek8nwDFWXxxIarM9BtCvE4gdi2UOoJRclL00UAQcjsEzuz7pY03dJk2AQZgvIsfStYqw6IJrFIomIs7ILchd0Tm1-Qovto2TxeO2FYRJu3x0DXj9Q2APORRnqVfEWaAVWJ9TC9Znw3a588zCRUQ5Bb5OJmjW-uFgqaCR3ff_aetP8abCAuMgTN_VDwTx8La2biVdCMVof_nKq7p22T2RZ60dCt9apZnGiDDFKBZwStenqiSkPAugAGPh_L692-K6h453s64uxrQ5JflEOOR2QIOVRbWO8ITc9OMaJJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/phivM-m_qV7SBAs8TCkgMlzlDayvHWWEvIeXAA9bj7HsLR7D92MRZgaxlG5ouwrfTpodpcCMN84g9EjW4hgdPqrkyPmp2J7IiKO2X_w2pdQbhmMSDjA5J-0xpS_MMp-uY6EoYOkV9TjAZZ01Q5fiyAya6Z_wKk5UliCUhtjanP2Xhuvna4BUGBdKUIPLIA9bzSJR-3c8Kx5COKxqjJl1C2yDN-agmrzRtyrY5Iy2Mws9E9Mlng4KoW3pjvHmpTy-fXgt54vxxmt-_XcoFyBXlS25vTQM7jev_Ss2ch_GkHGjK2fxIR0u9SZz42qZeTnnZLvZYhd4NcyZCExWpf9TAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
ژابی آلونسو در جلسه عکاسی به عنوان مربی تیم چلسی.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/99201" target="_blank">📅 17:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99200">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/039d015f28.mp4?token=O7gj3f53-gz1mGyxwAaDHu0aNcrkB8GDUwQl6CwoL2B75RNcLClzClIwnLtwsgH7e2ODonLW78nO18Lk5I63Ne4i3COzNTFuRugHJZcayzu_upQmNcxYjRSw0sJ5iKigkjxvBpCBnB5CPayUSxRV5KLkXWNw1jErCSAnDbTeklHmfZOeWdtocOsFTzuB87URGvVFEr8TToqXg196l_Jti1rSlF2Gu4757560tUjLYnDirBPMDqDvJZIiaDtS9XbBcgf8s9LbZehusmUZfcVFjR1vzSn6xbJ7moiFHKdGw3-PR_mCZPxg7hDW8nKaepAV359nOrnvLMQE1HKh87H1gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/039d015f28.mp4?token=O7gj3f53-gz1mGyxwAaDHu0aNcrkB8GDUwQl6CwoL2B75RNcLClzClIwnLtwsgH7e2ODonLW78nO18Lk5I63Ne4i3COzNTFuRugHJZcayzu_upQmNcxYjRSw0sJ5iKigkjxvBpCBnB5CPayUSxRV5KLkXWNw1jErCSAnDbTeklHmfZOeWdtocOsFTzuB87URGvVFEr8TToqXg196l_Jti1rSlF2Gu4757560tUjLYnDirBPMDqDvJZIiaDtS9XbBcgf8s9LbZehusmUZfcVFjR1vzSn6xbJ7moiFHKdGw3-PR_mCZPxg7hDW8nKaepAV359nOrnvLMQE1HKh87H1gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
رونمایی از ارلینگ‌هالند در آستانه بازی با انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/99200" target="_blank">📅 17:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99199">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDAt-tizkxSaAtbYMc-FA3j4H_wIQ4deeo9bYa-aopUG2NCuF3bw9GYb1vS1UO7EwGXoaGk-CaIEWs5EoWvDR5OjfXAA92qS82e8opeJK9QJEEnle14yXa8gLoOcDlyxtGfqpPv8oCKLCaRJBo3n4LMd-exv38MV0sNQPMvcrgjlf29H16QgQ-HuaK95QQRqWw-Z2frtYi2LkgMNvbR6cGQiieItzJlzyRVRUZ6amvrZnOHn2tPa5O6LzWKv4KMZmtGD9noakdEUaLjdAIiF1ravn4gLy8QgIeWC8gHa3MrrpleEZbFsL7GBGa7RJy6AvKHWZS596r_olnvJBhKaaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇹🇷
باشگاه گالاتاسرای ترکیه درحال آماده سازی پیشنهادی برای جذب ماستانتانو هافبک آرژانتینی و جوان رئال‌مادرید است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/99199" target="_blank">📅 16:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99198">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dc2675cc5.mp4?token=uJBSuSgUPMkcQ13eo35lihykepV4Mw3V9H-1qRsZJA2u39K8yFlOwlQyT5MxIXRzXYx_i0jEqemPBywRzGMZSq5JdE2Cztgaoz0zow9a28qRF6SqUQLTWtAwZk0DPFCLOYnj4hB5dC_3I-FBTcxxcc5xUebyBVkbg6s8yDCzNMdcXTIUrLDpsGGRCjXGRe8QJaVgCgtbk2F_Y4YRmRqkVUZyfMVqNEqod1nVTvBuF-JZiHORbzLoFOWuNaf3RFlFuNYqNO6tHkJqMaRdzD9hkolNXClw8FkyV52b9r4N3jVzCoUkh-oQOv05ozfr5K7VEuSzeuFq_hKOIr6zjTqSBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dc2675cc5.mp4?token=uJBSuSgUPMkcQ13eo35lihykepV4Mw3V9H-1qRsZJA2u39K8yFlOwlQyT5MxIXRzXYx_i0jEqemPBywRzGMZSq5JdE2Cztgaoz0zow9a28qRF6SqUQLTWtAwZk0DPFCLOYnj4hB5dC_3I-FBTcxxcc5xUebyBVkbg6s8yDCzNMdcXTIUrLDpsGGRCjXGRe8QJaVgCgtbk2F_Y4YRmRqkVUZyfMVqNEqod1nVTvBuF-JZiHORbzLoFOWuNaf3RFlFuNYqNO6tHkJqMaRdzD9hkolNXClw8FkyV52b9r4N3jVzCoUkh-oQOv05ozfr5K7VEuSzeuFq_hKOIr6zjTqSBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
👀
دوربین اختصاصی لیونل‌مسی در صحنه گل‌ سوم آرژانتین به تیم‌ملی مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/99198" target="_blank">📅 16:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99197">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXnCZs6nYvcCG5r4c0i9WMjpNNpJNzfHnY84KjhbXHc13cQledYk6iW4UCXW8Mgk71KMjBmgDurCxpEyK9nA0G7yGGuSS2WT0Ng_z9PGT1d89W9YNOVUC-xufWdKEYyOSrm4pCbfmCkF-6k7cPOlR5OjNKCsvW7LSnPBLFmw_5nW_HIo6572_qmjDT4TEmUCdLoY1eWH0NLCy-TrhSJee0dV0c2uH3mpF53EGpoqwwyUEY48slQf0pK5_izajMbP_pvv2B-d2iJLRaRmtg9H_nKgz4jRjZcEoctYItYkx7GOVgOv9sKRRGkiUVrJ5AWOrHWQ_kSk1V75I1Dm14qolA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کوبارسی رکورد جوان ترین مدافع که به 5 کلین شیت پیاپی تو جام جهانی رسیده رو شکوند، این رکورد دست مالدینی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/99197" target="_blank">📅 16:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99196">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTyoV7IWJyA4ll0cMDL-cIg-pLa6HS61Q6TOQhzHD8LiS8MgVmYzCc5HigC0D-QgnuREwYV-s0PJyJAJfkBj8JWtI0P0ibzMJKWr48tLvkFxR_BRFnFa0o_tj_fcud_6RYJ2qRUgH8qADVzfoC4QWUnLjg4xept6_JQAsgLXz4NYpOzeki6R1wKZRbpc6ETJuVZ6sEMUpLOGcNNsgsO7EUabnRfRBHR0yF4-tstokbVZX2iyETMDsfy_Mub3a99nH5lSEZBiOPkN5excvnX_8VmmnGdeVZx05wtMRypmrNCN54r47lRe5w8kYTAxygBj6__qydxdLHVciIe3MVBv9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پوریا پورعلی، پوریا شهر‌آبادی، مجید عیدی و علیرضا علیزاده چهار بازیکن گل‌گهر سیرجان هستند که اگر اتفاق خاصی رخ ندهد بزودی با پرسپولیس قرارداد امضا خواهند کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/99196" target="_blank">📅 16:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99195">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ef7ff1dcb.mp4?token=bVH52dX8V9_WXmBd7c1nSMhkCAmnJqb7WMZSbNlBWvM1cAEPYnnO_yuLdIvBF2sA2ZhqmXJlR9ANgUPIViOksvRHx_SHF-ek0QjU6sNfiOPvxSkTs-J23VKga84b37pdvDcKyPdbCtAGkQPcNa_OmEhW94esJ4SDPDeJWRsdYsPqreaESaW-5OCVqo1GKdyxwlHmX9L45ebbv5IKb_1O_YEXDP0jxjZqinLbhC3lDfTX48JyC6zX3K03Tf5Xd6m6iFHxwE5Y-e3wJcvmz8KmO31QZR-trHlR4dLFZpB3CF4k98hZ56HeBBQzvaz-_KuOzsQVwPUwW8IbdfapxIsyJ0_3qg1F-jdiRXpHq8IZfEGTeTh2u7wk3BgHlajQkE0tS0ZVIQR1gVOzLsPS1xQyxBxJZ1QP3MCZ7106gWeDXwNOY6N0sx7oY9vAYMUlKxtNB4D9dqbmLoQErAwSJbkAoZra14bIsh_MkF9EFL-S6j16idAfJzp4e_GkSYrzoWCzgNN3ypU53NGOp94OSGQsLATG2Vd2DXogAU1s8a1QvAtqhiM9IIM6lg4AeJKH5dC5dN3Io0bmZBH-PRKuqkgeQbrs1MxV9zmvBYfCHT3IKKWfxUBxMCLAByMNGyslls80ba9H26bwXIAb5_zDoI6wuiQuMqr9pwT10nvFVZ4brHo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ef7ff1dcb.mp4?token=bVH52dX8V9_WXmBd7c1nSMhkCAmnJqb7WMZSbNlBWvM1cAEPYnnO_yuLdIvBF2sA2ZhqmXJlR9ANgUPIViOksvRHx_SHF-ek0QjU6sNfiOPvxSkTs-J23VKga84b37pdvDcKyPdbCtAGkQPcNa_OmEhW94esJ4SDPDeJWRsdYsPqreaESaW-5OCVqo1GKdyxwlHmX9L45ebbv5IKb_1O_YEXDP0jxjZqinLbhC3lDfTX48JyC6zX3K03Tf5Xd6m6iFHxwE5Y-e3wJcvmz8KmO31QZR-trHlR4dLFZpB3CF4k98hZ56HeBBQzvaz-_KuOzsQVwPUwW8IbdfapxIsyJ0_3qg1F-jdiRXpHq8IZfEGTeTh2u7wk3BgHlajQkE0tS0ZVIQR1gVOzLsPS1xQyxBxJZ1QP3MCZ7106gWeDXwNOY6N0sx7oY9vAYMUlKxtNB4D9dqbmLoQErAwSJbkAoZra14bIsh_MkF9EFL-S6j16idAfJzp4e_GkSYrzoWCzgNN3ypU53NGOp94OSGQsLATG2Vd2DXogAU1s8a1QvAtqhiM9IIM6lg4AeJKH5dC5dN3Io0bmZBH-PRKuqkgeQbrs1MxV9zmvBYfCHT3IKKWfxUBxMCLAByMNGyslls80ba9H26bwXIAb5_zDoI6wuiQuMqr9pwT10nvFVZ4brHo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇩🇪
فینال جام‌جهانی ۱۹۹۰ میان آرژانتین و آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/99195" target="_blank">📅 16:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99194">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/99194" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/99194" target="_blank">📅 16:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99193">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/99193" target="_blank">📅 16:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99192">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e630de904.mp4?token=ouYgIY9GjP6bXWbxClfQBB8z2ILKaYP-K1iINI9Js5utOyVs-hDE59NhdavHs22Tqy77CU2ea8vidJhvhQ8YjApVSeTWklLOGHEqq-UKykwz8w9zbvFYIqYe-_pWc0-6zq3DUHZy21dI32fF3kJ6fJiYOOdE5DCGSpyne82Lb4Ga2hTB1kjuyHqhavlp4YQG2X97bc8XeuUuYKItEgjm0lweUDtWAoCC8IN1SXfnSUnZwAcTRWVB4OoXPTSWTrqqtFFm7qlb7yJ-wXnYSbMPbbVz9dneGGntoufbauBXKW9eSbub8GpfnO5-aN05EaInNDpb_fV0SeHQWT3dxTQWrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e630de904.mp4?token=ouYgIY9GjP6bXWbxClfQBB8z2ILKaYP-K1iINI9Js5utOyVs-hDE59NhdavHs22Tqy77CU2ea8vidJhvhQ8YjApVSeTWklLOGHEqq-UKykwz8w9zbvFYIqYe-_pWc0-6zq3DUHZy21dI32fF3kJ6fJiYOOdE5DCGSpyne82Lb4Ga2hTB1kjuyHqhavlp4YQG2X97bc8XeuUuYKItEgjm0lweUDtWAoCC8IN1SXfnSUnZwAcTRWVB4OoXPTSWTrqqtFFm7qlb7yJ-wXnYSbMPbbVz9dneGGntoufbauBXKW9eSbub8GpfnO5-aN05EaInNDpb_fV0SeHQWT3dxTQWrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
احترام یامال به رونالدو در تاریخ ثبت خواهد شد.
👏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/99192" target="_blank">📅 16:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99191">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61fb637797.mp4?token=bNG0MPB41JczOqJaeP8FP2w2KeP90c8AY_Pe0ULTvAgDVrwHHNG4pqTt6AdoN5_CtJtzJ1zn_tujFMeY187-eKYFlSTgesT5OJlze63GH5ttIIrQOB5e69r-M3ssrUWYuKdCv3yIpqhpne3102qxGn3T6HC4yBa_ShQxPqvKX-YdJUklLEQdY09iU79IXTv_HaP2216PF_9Xt3meb48lsjX1VgCrchu9OEAWOIW3pFr-Yk_RjYUxF2gJgQU3j6TLQKK1Z_8CCFPc_a9hRGadvHRvuDp9xSOOIf-J50614XPT-4sWeTS6WPPfsav4vhZm9oeLk0TgnCpYZK-whxwzuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61fb637797.mp4?token=bNG0MPB41JczOqJaeP8FP2w2KeP90c8AY_Pe0ULTvAgDVrwHHNG4pqTt6AdoN5_CtJtzJ1zn_tujFMeY187-eKYFlSTgesT5OJlze63GH5ttIIrQOB5e69r-M3ssrUWYuKdCv3yIpqhpne3102qxGn3T6HC4yBa_ShQxPqvKX-YdJUklLEQdY09iU79IXTv_HaP2216PF_9Xt3meb48lsjX1VgCrchu9OEAWOIW3pFr-Yk_RjYUxF2gJgQU3j6TLQKK1Z_8CCFPc_a9hRGadvHRvuDp9xSOOIf-J50614XPT-4sWeTS6WPPfsav4vhZm9oeLk0TgnCpYZK-whxwzuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
▶️
🏆
دو قهرمان، دو قاب، با هم و تنها
🇦🇷
🇵🇹
تنهایی کریس رونالدو بعد از حذف پرتغال و مقایسه آن با تیمی پشت مسی، بعد از صعود آرژانتین
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/99191" target="_blank">📅 15:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99190">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPm-XngwJ0A-6YA0exNCykWMHmdKijEnjh7CuE8ddULcqpbXpEuwuyRc7daymk991r2GFjacWe3MXlD216OhrxYITo_5OBHIO7UTY-Boxf4FVf72y7pObM8WnTzPpaBLxL57S5LJ_s7E7Tndc6m0NAw4SapbWobPzG7bEgwLAdREoIlGICD8aAJ9B-YiRPBK_d3rM9jjo9cT2MQO1wF0UXbu3yNrNGIlvJza4YOfza-1M9M9j_c3YE8wRdnWTGR0yp-0UPyaQijA9XLMBPzLpZ-w0jDCDPW7aROHRIMX8djT1triHSZOZbb1qNohI_QlBWMRS3eUdvkiOUWg_oVMbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بانوی پاکدامن میا خلیفه: امروز من مراکشی هستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/99190" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99189">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54edf8ef7.mp4?token=udvOHWpZ_4ITlNbH_zSFVrBHbWtRYt2FXCgxKUTh7aDbjf4rS5e6fCqZ9oa5HYr-t1lLfCG2CHDwR2hSm6hA4PG2REJ3X5tropGKmSCrcASW2P20_eVi2dYioa5wxZNl4bpbuq9biCrAicOzW8Ci7D9spyQ7_tJmMaWqi37WM-wzEbQO7PyuwWLl0Hlnim5FimEOXJqpXJcwzlvi_B34H_zXvIeunUsG6LAwSm8fvpVZLu8yJEW3EQLk1LRS7C87tYIDatq_8yRYI9I1V5kZ1qs1IlVmJUduiLA91xAJmST2S9cPp6xe6upNjywFRowh9uP5EnsJn8WcrXZzSl-GiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54edf8ef7.mp4?token=udvOHWpZ_4ITlNbH_zSFVrBHbWtRYt2FXCgxKUTh7aDbjf4rS5e6fCqZ9oa5HYr-t1lLfCG2CHDwR2hSm6hA4PG2REJ3X5tropGKmSCrcASW2P20_eVi2dYioa5wxZNl4bpbuq9biCrAicOzW8Ci7D9spyQ7_tJmMaWqi37WM-wzEbQO7PyuwWLl0Hlnim5FimEOXJqpXJcwzlvi_B34H_zXvIeunUsG6LAwSm8fvpVZLu8yJEW3EQLk1LRS7C87tYIDatq_8yRYI9I1V5kZ1qs1IlVmJUduiLA91xAJmST2S9cPp6xe6upNjywFRowh9uP5EnsJn8WcrXZzSl-GiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
🇦🇷
از کودکی تا تاریخ‌سازی با لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/99189" target="_blank">📅 15:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99188">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4241c19a19.mp4?token=sEUxrjkm2VnbamALmtUA58SG93M15mT7GO-59hdd0ctHJiV86c8A_zdI-lX9ZryPs_9CHjo_3HFGoQ68iGEH2BBXXZmuGkmTAffZsZ6eTnLHcR4FuiZeRC_Ai8XZkM_-DeBGsrst1a_uUtb8zQP3MvjCUepV-OzFFjjzEcofl9mpbdMoX0G78Q-WXcQrBzgd3fw9L8ctukW-OkATAw3-Um-d4QSSy5co6QigplbYjDXY1eBc6ppxPMfF3j44FMA2dht3eoDx4mqBYszYKW3tf5si3s0_3WTFxau3NGZGas0NBu4RM3O9uvrGOWNfBlI6VpVycHpcw53cBJF_ciMHNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4241c19a19.mp4?token=sEUxrjkm2VnbamALmtUA58SG93M15mT7GO-59hdd0ctHJiV86c8A_zdI-lX9ZryPs_9CHjo_3HFGoQ68iGEH2BBXXZmuGkmTAffZsZ6eTnLHcR4FuiZeRC_Ai8XZkM_-DeBGsrst1a_uUtb8zQP3MvjCUepV-OzFFjjzEcofl9mpbdMoX0G78Q-WXcQrBzgd3fw9L8ctukW-OkATAw3-Um-d4QSSy5co6QigplbYjDXY1eBc6ppxPMfF3j44FMA2dht3eoDx4mqBYszYKW3tf5si3s0_3WTFxau3NGZGas0NBu4RM3O9uvrGOWNfBlI6VpVycHpcw53cBJF_ciMHNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
▶️
حرف‌های ژوله راجب فوتبال که محمدبحرانی از یه زاویه دیگه برامون تعریف میکنه. جالبه ببینین حتما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/99188" target="_blank">📅 15:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99186">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dGZqvuGUPKfKh4qdBebJbITfx5PH13tp8eECqZfhc-o4NkGK2L_mJMyPTO9HpWoSuBuVC1aBMBvdXVzInQgxA8hHmtE9XLwix434YJOFkdc9Sy5Q59VGitskp3voUIZ8dvYSsrTp9Cy_EHhfdV5m-PM70mEWEaQpgXqARRaSHsuNeSl_mVcdqIn76fqQC5hknmC398ySV-kDeKW7xHLRoZ9csAliy9NocfeAoxhp_KXYnpeyjQCtDMJp2C-OXQV9H-0XbX8pkbFUkWOY0IVvt6DUgciMGkYV7LpuEudKZUPp9aDThXhVE1qwMbVoOyUWSkKHxErppnRiDLWYTR9QKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TpmnYbXH7egv1HXZ2DwFuor3HLbKTIqHIXQoZynk9sYxfGxBghbo7VlOIfLUiZ2lh946xaLRnP7bTCoaaYA57p1I386o7OEyWI1l1H8lbP0DKxWHLadHUaV3EQOImj5BxfxXf03AomS12HVLs7-LUjPGk4GE2VKPzrZkBcRaCDstrIfL5F4VLik6gcKQ4Enpk3UboldqYcFoPtGhmZ4i7GexGqKbu5IQvntRlNt3xtUFQ1yS6A-nOh0xQFOZCaezYvc4hr37pZeuidXWFXoIOq1yRcyG9cDMRZ_iiVNgN4YucmeWzi3LpfyXSgimWj496PXOfEyMp_uV3G8Jlnwj1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
وضعیت اسکله بنود شهرستان عسلویه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/99186" target="_blank">📅 14:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99185">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
گزارش ها مبنی بر برخورد موشک و پهباد به سپاه ثارالله کرمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/99185" target="_blank">📅 14:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99184">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
فوری؛ از اکثر شهرهای ایران به سمت پایگاه های آمریکایی موشک شلیک شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/99184" target="_blank">📅 14:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99183">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4beeec2583.mp4?token=REq3s4LFHU2VIYMzYTwn_ZOG6XycJU8IvZUSotv2gsSm4PKTCX8UHEHdg2LaTEscG2jZni-z_eCle8N8SQT9u6QLXpNfnqOuOVj04nhJHb1YIV8zmY3SqwOOs9qtVi85LrfLeCepXlCMJzwD4kdlAnhrnVHDBRmFjL6a-jIGR0W7D-QpH2-WdqXhEOIGP5lIw3585MSsAQHkxQnA1WJDayGER5c4jj9uvjuCA_p6WhZNXHbCtsBcJGah5TBWltp1-MF1Nxi1ryW8brqVy1-m8VRDHDyAYfu4T5bCrXudpmeu9fW7ege1rZvZnAsCVF9MICnUV2hbW1b71wsNbnfTUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4beeec2583.mp4?token=REq3s4LFHU2VIYMzYTwn_ZOG6XycJU8IvZUSotv2gsSm4PKTCX8UHEHdg2LaTEscG2jZni-z_eCle8N8SQT9u6QLXpNfnqOuOVj04nhJHb1YIV8zmY3SqwOOs9qtVi85LrfLeCepXlCMJzwD4kdlAnhrnVHDBRmFjL6a-jIGR0W7D-QpH2-WdqXhEOIGP5lIw3585MSsAQHkxQnA1WJDayGER5c4jj9uvjuCA_p6WhZNXHbCtsBcJGah5TBWltp1-MF1Nxi1ryW8brqVy1-m8VRDHDyAYfu4T5bCrXudpmeu9fW7ege1rZvZnAsCVF9MICnUV2hbW1b71wsNbnfTUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇬
‼️
نمایی از سرمربی پرحاشیه مصری در هنگام اعلام مردود شدن گل تیمش مقابل آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/99183" target="_blank">📅 14:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99182">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlS-kOPRxIp_GWthCzvI8Xsfs68xgnZeAqWwkYCKTYj7bXhHZAsRTvwpzUZWwQ_rjMB_0DJHFgsYKZUAQ7WqW2_f9G8puOR8Pc5wPiVprHLCSrat9pILfi5C-lkMa1kx1T37VYThgDMiZWH7xanAm6_A_WNUbR4L2zCTynMudpqWZw06PBDSwd3UpYzEPnP_Dof1inRgyR9eNdrT2-W7thscLYBJpUAYjBlhsLboEhvFworHc5gcf6xfNRLja4ligji1H1TmCiIlz3L1jCVHXzM5Rg7FIjpwHd7d23lHnEeUAga8-WjS70ZNrmwIW4noT7ba4tUc8e030T7r9rnOFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لحظه امضای قرارداد ژابی‌آلونسو با چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/99182" target="_blank">📅 14:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99181">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
#فوووووری
؛ یک مجموعه صنعتی در کشور اردن مورد اصابت قرار گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/99181" target="_blank">📅 14:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99180">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
#فوووووری
از منابع خبری عراق: چند قایق و ناو جنگی آمریکا مورد اصابت قرار گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/99180" target="_blank">📅 14:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99179">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
#فوووووری
؛ گزارشات از شلیک موشک‌های کروز به سمت بحرین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/99179" target="_blank">📅 14:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99178">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
🚀
#فوووووری؛ رویت موشک‌های سپاه در آسمان اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/99178" target="_blank">📅 14:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99177">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=slKK-Li8McrZoeWhk3dbUe1u3gjdNKhmMy3-1cdMn-47CO_sBoEXc3F9dMmv_Vp_d1zf_WqcBsu7EVIWhdn2KiWGDbYQqPM6dVPvEQBFlWyDuSkfrxkDNJ-kSZH7c6dDXLaijzhrpmDzwU6jrjUMHGh43f1oqruYTX82kEIEtromOU__hMKSKNPcc9rO1998rBcSyn2JdiYHXvB_0KFvJc38DQrXGQYdLq52cQW3IPMVL-GgnpUjRwY3reHrjVxgJE0_lRKWsp7Rok_nf_VRJXF2IA0D1weteVIabWpEBU8CjSIzxtvAUCgh9xA1Hkhd-wgxdjylxnduItn3kNn7fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=slKK-Li8McrZoeWhk3dbUe1u3gjdNKhmMy3-1cdMn-47CO_sBoEXc3F9dMmv_Vp_d1zf_WqcBsu7EVIWhdn2KiWGDbYQqPM6dVPvEQBFlWyDuSkfrxkDNJ-kSZH7c6dDXLaijzhrpmDzwU6jrjUMHGh43f1oqruYTX82kEIEtromOU__hMKSKNPcc9rO1998rBcSyn2JdiYHXvB_0KFvJc38DQrXGQYdLq52cQW3IPMVL-GgnpUjRwY3reHrjVxgJE0_lRKWsp7Rok_nf_VRJXF2IA0D1weteVIabWpEBU8CjSIzxtvAUCgh9xA1Hkhd-wgxdjylxnduItn3kNn7fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
🚀
#فوووووری
؛ رویت موشک‌های سپاه در آسمان اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/99177" target="_blank">📅 14:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99176">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
⭕️
❌
🇮🇷
گزارش‌هایی از شلیک موشک سپاه از نواحی مرکزی ایران به سمت کشورهای عربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/99176" target="_blank">📅 14:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99175">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
اخبار غیررسمی از شنیده شدن صدای انفجار در بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/99175" target="_blank">📅 14:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99174">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJoeTqVwrwlCJqt6BH9vFOtVaXHUeEwjwYvrfaMGwJwfMpfUVRcwa3fz0yYnZqmoKllEianCK5eLxwFOICBuUOUwaZ_d8BQQXry0BoR_84abx2bNwgOIBcb0A6vMtla5JtvHEc6Y47xyTYPUE_g2J4b0_Csz9Pf61JOJJR17x1hIJkAtrw8pMYTNz38vWMU03dhcrlWchuvqCV_BgL024clv-o3DpQ37bDha6zbLf5gquP_m-imn5008ybhvDSZ4YaQb4vzQrzt3XahWVrhuzEq-XLZDVPE99pWNdM0fhsFY7ePI5dnzPr3F6MqRKGa7omWLwwU3vNQ8A_uxTlMPVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فلوریان پلتنبرگ:
نیوکاسل با فرایبورگ به توافق کامل رسید تا یوهان مانزامبی را با 60 میلیون یورو جذب کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/99174" target="_blank">📅 13:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99173">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای چند انفجار در چغادک بوشهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/99173" target="_blank">📅 13:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99172">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WiW31jyWY9Hd8ejOY7sPFdIDxF-mM_cxa_bnIqaFiFsvZfFz58-hegi5O4MCDIlqqcnx4eVRuOMnGj7WRhsumugkhs9tE5mjxbpjHgTcBjzxoakTWFxgn-oajKh2taG_KgmLg5Rzxg-wPnGcUuEZeAn0xpXCxP-xk8OpwUlEaI4RYBoW7ZhDGzLowLQIdaRdisO7OiX7Z_LyBO0bi3e3wlenQm4VYHvvaraHKRuIBsz4g8wzPQh3IiXRuuEdS5cV-T7tcP89SSvm7vcfQXiAzizi4E9YPjYuSdJLSH-ZqclGbfkAFZFjeC4Sr87DU4odfw0WYKuHWDphSzt4166W4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
بهترین ترکیب فعلی جام‌جهانی فوتبال تا پایان مرحله ⅛نهایی با حضور علیرضا بیرانوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/99172" target="_blank">📅 13:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99171">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای چند انفجار در چغادک بوشهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/99171" target="_blank">📅 13:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99170">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7337d363d9.mp4?token=LddNUsz-GSgsJB1LNMbUJAB99yZX3fxh8Yw86B4s3EYG7TzObDklB1ZD4CGGXIyfpnqY2_qV0nNAIqEFwVkoiiTsDq4XjEQIIRuyVTKa0vkuuB0AfNPw9jDDo3dLrQ7YoZy7kFEZkJWZyb17dp3T5LHmaXV9c66GM1x1I89_IwJUWH0sFtnOBzTxIeOINiTZGi_1g7NKlDE4hT74WqrZd0ynFFlU--2QgxfB9qi675jyaxKvYOzASDgkNUL9aVHNmCa_H_pOwb1TgzI7pyXfPBpH1RyAK_-kpqgEk2Iql27r5ELK2yT2qstCMJy_ZMHNWboTa6WsYAbcPVMbIUeBtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7337d363d9.mp4?token=LddNUsz-GSgsJB1LNMbUJAB99yZX3fxh8Yw86B4s3EYG7TzObDklB1ZD4CGGXIyfpnqY2_qV0nNAIqEFwVkoiiTsDq4XjEQIIRuyVTKa0vkuuB0AfNPw9jDDo3dLrQ7YoZy7kFEZkJWZyb17dp3T5LHmaXV9c66GM1x1I89_IwJUWH0sFtnOBzTxIeOINiTZGi_1g7NKlDE4hT74WqrZd0ynFFlU--2QgxfB9qi675jyaxKvYOzASDgkNUL9aVHNmCa_H_pOwb1TgzI7pyXfPBpH1RyAK_-kpqgEk2Iql27r5ELK2yT2qstCMJy_ZMHNWboTa6WsYAbcPVMbIUeBtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👀
هواداران اسپانیا در آستانه بازی فرداشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/99170" target="_blank">📅 13:40 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
