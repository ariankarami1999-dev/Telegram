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
<img src="https://cdn5.telesco.pe/file/DPP5HhYYUGYjyVXrL_7I4Z3Ky7Ov59Ar0OL3a2X0GauUquZ4Kxdq7L7tp3IK-wJfxR0g3ZiHw2OL8Lyb2j646j65fJLOiKpDEFH9bX7BhmWV6lU72bGp03gHg0RZA-oUsv8ZT338Sjj9dhq2tRATaaeG30ym7oVsqvrWiPNdSL5YKq1SHMwkc37Ew7lSVXTgVMYZEOPIDhuhT82pSyHehlsiiTXSxSAYRQlUTg1AVlnn8RJtUJVRcHWrQteDbVuWT4ivknpxD9nnxqDpgWp8BAySCGDojkCsxRzaTrT7WGewZ_xS-Mlise-UGV7HKPQTZvYFQVJyEXoe_rsC6NbsCw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 640K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 23:57:09</div>
<hr>

<div class="tg-post" id="msg-98226">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYLIO2-8u_sPGiG9KarkZsHvVG0m9pv3V5-zav_qbVfNWLFsFLxVm4o5L3KCdLjGbr7fo2xeJY5vYEIf8BiaHXRbiPtabv2tuLXnCalUTLWhoeqTzHJVlm83uvU28-2_WFzUFSHTI4lK4axnCNqyrJRWsEGN2lgO8T9w2nrf2Xj2xi9nWGHSJzxXy9IdKq4c76ZdJW1djxIFCAY5ykrgf8NAgBy1nwaQ9xgeN2PZT70kyuwi5wH8H-HGTU4jT8mK7zFK6F-Z3WI-FEDBfL2D1mwbYwIulRdIVBIFThj2XXhND1wfxwyw09K1E0Br_AKB8PAiO1H2J-_Fo9ec4jDVog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دماسنج‌های داخل استادیوم محل بازی فرانسه و پاراگوئه عدد 140 درجه فارنهایت رو نشون میدن که معادل 60 درجه سانتی‌گراده!
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/98226" target="_blank">📅 23:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98224">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAQK3u5HUxniqGJSw7HCmToLfP0W3bzPH64lL0ADVNSMoMS4gr8sqokHWXx3tdcRIt768Aepc3KvYnPgQS_7_fA8LZfeq9baXPxvoRosPeKEUI9-Pc0EDHzQNuuTqI46LU9PEKRk9WcdK2Fo8ls4Jpm4AhvEaUxxceW0miMuAYpxv5486II8eLXyoQJxeS-Bt-e4a_nUz3U7Akd9pFegsFbgowWkRO9d_uLucr7G1tHSjIEpCx5-TtG23DlqH_7SdyCMA5epqKmAswSNeGU8SqYT3E0GBVtM9VlKJLtP8yB3a1Xe4XIkta62w34BKbn_O0WWM6yGQpWGiW7QRUeRZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولیسه به این شکل وارد استادیوم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/Futball180TV/98224" target="_blank">📅 23:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98222">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qdtnKQe6FL3oGEByMDJ3tRwClpJJIdfcL1Chy8YN68ICfRTloG70obCJOxvCq0KOO3aEr5xm855ymYzW7J5MtAx9ufhsnipvwmlDU0c_flcio3OYr2Z5otFhnrfLZomZAo5vlXBTuSyUe_J1_GB1nPNzh6wZaC_PxbiLOA4tcdslv0ri-Uo2hFt8YEKvoW_Zl7JVthk9CsRyMG65jHBWuai8RYRtpYOclv9v96maFr7s-ArCCufh7oj8skwPHBxyjp_GrRjIvhhcRdzmQrjraJHNso8coASU-VnSaWHc6bpuR2kQNzWCHcBCQrYlradrbe06UJ5YTKWX90IVrGlB5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AKiEVTVaZmGAqGfsRtcZj870iOU1uw6o5OIqj966hXD5BhNQoqwcguU9zWwL6P9isYN0qrCV5v6RgIaWUJ1-pmzUDY2FXL_uOhxx-8lQGSv1_stEKQ9mvP7vT_zNSRLMwCYWgWl7FtajBr4HYekhlIVpf49QvyIgQEofQJgVbKuS-YZ_SB9EyoHMHV4t_1gKnQE7QPVO2pg6wvzQhMQGEK6zDeajckt79GYWWFrrtP64-S3ceRjCdZv-RFRHCDIgjMgn4K3fHpDoQHA9q49a7TUe9MS-_b4j8Sqb0njTwL9zbowPzYu-CBdslcBp4boxaiY9bX59coC9cpqAorhlKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇵🇾
🇫🇷
ترکیب دو تیم فرانسه و پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/98222" target="_blank">📅 23:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98221">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvvTKNtPUQVtHfyPnG1XPcm3eBz9GMla3HEWl7u8WLfWpG8ytzsakjPDnZ3MzDHAl02Sj-mhbJcHOv5ZbmOTMqDPvjuufz1UXrbeonPI-Sipoegam_qkI7OcxNA9tqGuplbl8wP0kp51UBa0IuR4rS1FJL8d4a5VoSsrr4cJ5ejyJDdNCAE6zYayGie2wikkGQHx62L61-qaGVMHqnGdJUdEJXKAyHJM2UXib1FO-hVGKcVk3TmoCyxo0iYdDGW4H6YsRoNKd7SFExYUKabcTms1-jddZH55zM6ykV5Vo8haWmBHtNjcYx6e1PuX-sIgwo8GomoEkId_xBxCKkqHkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🏆
اشرف حکیمی با ۳ پاس گل و ایجاد ۱۵ موقعیت، بیشترین تعداد پاس گل و موقعیت ایجاد شده را در بین تمام مدافعان در جام جهانی تا به امروز داشته است.
🇲🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/98221" target="_blank">📅 23:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98220">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwVlw3nzi9040asIQeOOJqXBNATIXBndOCHAmBPgRZBNfk6AAPrWIiTCOJLNxECpPJj5SoK8ZGb6BqJhIslWqhPjxvbsxcterPGuN2TNbxgE0vFGuLzcxzNjPJnO_AICQ2RUS1i-GxvIdATo92JrxrXkxFsVuiP0xyZY-6eNvK_WziUe2hdjrv6YwMkSS0EAXULla0wCS8DNvGb_JuYFfgX4smjEulKzWXU5_lt29Qz3CQIPIbCW6Jp8lQCJ9SC7k3qFWcCRd4N555fR1BlQIlx89bU_XMV5uT7OzI_X8t-n9-6jFuqnNuwPZl5bzNDKhZgHmEbIMnqME-5EHQSBTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بردن مراکش کار هر تیمی نیست.
😏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/98220" target="_blank">📅 22:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98219">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYjUdw-rTAieu-jA50wYl0D-jiltbAbkn8srEhdaZibN1VsR45mS9rV_aF3GeKreXr3U3khVpF5qoVrNhJMTI81cpKcjPnQrONu61MA1pien05KJ0TjBaKx5F-XP_2yyQW9q2OSnmo9Ai59YhCpoiudRGuebC0Da9pcUpTK8IbIQLZc6YN7eb2VTuJwSUWz3d6EjhTA8BMJzS5_tQSQ-TQf9ZGpI_oHNwj7r79E_NQgzxmQTFhxIc69ha7jShX_tw7o9RYa5Z6Rg3epQz8q7h_B0gIbn8VMVqJTzNqgJMnEQ8jy6t9banJejgKdmLvMsH5eS6anOAgQPYI1Cx-kAUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇦
یاسین بونو، نخستین دروازه‌بان عرب در تاریخ جام جهانی است که در 5 بازی متوالی دروازه‌اش را بسته نگه داشته است.
‏
🧤
بدون گل مقابل کرواسی
‏
🧤
بدون گل مقابل اسپانیا
‏
🧤
بدون گل مقابل پرتغال
‏
🧤
بدون گل مقابل اسکاتلند
‏
🧤
بدون گل مقابل کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/98219" target="_blank">📅 22:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98218">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
📊
|| بیشترین پاس‌گل در جام جهانی 2026:  ‏5 پاس گل -
🇫🇷
مایکل اولیسه ‏4 پاس گل -
🇧🇷
برونو گیمارش ‏4 پاس گل —
🇲🇦
براهیم دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/98218" target="_blank">📅 22:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98217">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTcZAw9fWkrjgdjsjBGf2MhjYXy4vwVBXdaxTuZrLVWizmSM-GpnkKmuHetHwAuKYssBU98X5XuKGHgl4AgG4cLxHgIvFFPI9U0qbD_OoGHnjZ0pMOGQy-VEasISIByLk63-gNJ0wWBwkeC-42PiSnuME2p85h4KH2SG8_p9LFbSffZc5v51UkYg_7QRvY6TnmUJzQYvhjAQbet71q-ZMRRX-4kfrD7TSQr4cDmp3mcQxEsvNVDGb3WrcaHl96oQpVtBkwwFUaW3n8iRrRDXbsUXvOCGMG_4dFTEArQWQh7jrRvUbjTkDR2BehAMW8JbMBBnRxdILf6M7AIo6VEUeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
عزالدین اوناحی:
ما تمام تلاش خود را برای رسیدن به مرحله یک‌چهارم نهایی انجام دادیم. هواداران مراکشی در اینجا اقلیت بودند، اما به ما قدرت دادند. این پیروزی را به کشورم تقدیم میکنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/98217" target="_blank">📅 22:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98216">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVs5bR-uSZr8stoyTf2z5SSXqeOGvSn6kezZeRcOWcDfh2FR6kDBguBUZyerG1trWnuNQgHms0JB7wa6HzbvUdfGrO4OshuAYyPVw3mPuka_xxCqV-MntT9sVl0WzEuAZBMkl0XVfgfMu1sIVe_1l54j9m4Sw3CJkWGWEreOpfPx5T0lW8PcJwQcom4_JrAsEAhQ7_r0_onPJCNP6EEOntuDE7iiHGMtHvYJYHJlQV1KIQHulq6FtAYIvYBo7fCNp1uVI24QU_qoQ35hYAimHqd-SZhf3Nj7Jt8e2aOGF8Cs8sU94lTxMF5QIk6IDUtOdm4FwvwDenD1I_6WriOhoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
|
| بیشترین پاس‌گل در جام جهانی 2026:
‏5 پاس گل -
🇫🇷
مایکل اولیسه
‏4 پاس گل -
🇧🇷
برونو گیمارش
‏4 پاس گل —
🇲🇦
براهیم دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/98216" target="_blank">📅 22:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98215">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsTuVSSBMVRB7GolJtua6U7gfbc69gSjeOStOObPC9TBhNd2z9BvO_nUf_eUbABGRaH1CjXctKQihUHKbf5DnjvhPha3dDoq_zB_Dds_y632RFkV7APmULVVmwDTqc5wqAkRECW3dWEpDOMvgMyx8Hh5AujrGAmgNfZzx4z39o5o1A6Imb-2-pKSITvieaU8vHd3O_h1x9_v5drkIU2c2Q3QoNQvNSJFUOMpHBSRxtBwHb0fbjPnrZtl6-E-0EQR2VhU-3XUeY5CLILZ-ZOI6ee0QzhFRY1ohc1MPoQ_dG5Hx8O00uZ0b2dTPCEiPpp0yXNjwOwaP7twwA0VThJnIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بیشترین تعداد گل‌های زده توسط تیم‌های عربی در جام جهانی:
30 گل —
🇲🇦
مراکش
💎
18 گل —
🇩🇿
الجزایر
16 گل —
🇹🇳
تونس
16 گل —
🇸🇦
عربستان سعودی
11 گل —
🇪🇬
مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/98215" target="_blank">📅 22:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98214">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iG_nOxxOW1jXC76gyMClkuwOcBbvF5fH8_mkhzjFSTpDz3d-1TNQGSkq8TMo6zuzVwKwiNQQT4D842xbiQ0dLR_U0N4DIBjoSGlo0QN-8LgwWMipq5Q4Nqy2AcAWf3Rh46a9uIknWYNCS1kkmQaIFigmyFP-_ScARSny3tD46Qx_XvOjctX241pSKLqeMrduJG9ESkIYHkZLl9HWXZlUYE26JvkYjUfBp_QuneVxw7AXYNM4HOAaEookglDHbcfbENMVlIEKsUglKoqX8FkP2htxF82VVapLAcjHtjpsLlAX3vhtN451bVoPuf7dtsVpMHcOvUs8mpe3Dhc_SRB-qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
تیم ملی مراکش، نخستین تیم آفریقایی و عربی در تاریخ است که در دو دوره مختلف از جام جهانی، به مرحله یک‌چهارم نهایی صعود کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/98214" target="_blank">📅 22:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98213">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHjV4lWF3yym1aMZD_OCMGqI_O4xVS1W7LEzVvr9i2c0MQ_hi4WTrWzuamQXLxWckcZMTNPyNDd-JxvIttqcVM8VqCKgMAmvuZTLJepJj5jcHbUi7NW4xs0Nu6iGkx40sFZvqSFf24cAGnn-f9_ViSJwS9j4LaHSBXBqltPiDqw7gfVw3WD7Hlo1o2WUV3AI4h-Ssiw6Qfi2CUxlD28l7a8VmAcDooTl3DMwwa-KwtuLr8q5L-u45Wcz4Sp3brmcMTSyYlmM0Nb5frkHsRt1weu2xIGrOqDV66HD6TPGD52e0GYPdpISMwbjTAajpCvPdHBEs4VyWncVxptmee67uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇦
عزالدین اوناهی مقابل کانادا:
۲ گل
۱ موقعیت عالی ایجاد شده
۱ پاس کلیدی
۲ شوت
۲/۳ دریبل موفق
۳ مشارکت دفاعی
۳ دفع توپ
۶/۱۰ دوئل زمینی برنده شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/98213" target="_blank">📅 22:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98212">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🏆
پایان بازی | صعود مقتدرانه مراکش؛ شیرهای اطلس همچنان در مسیر تاریخ‌سازی!
🇲🇦
مراکش
😆
-
😏
کانادا
🇨🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/98212" target="_blank">📅 22:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98211">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEvEXDMVh9vQCp8WyUhJ_-ECCYqE3AGRlAxNnFSVcXIOaOuv1SZpEz6S_NJN42N7j6P0BVJVl4BzO_0mWPjnGyzBOMsDgJRaLepz6BGT26GmNvk1pRv5jN5fENyaHfwonk-7HsWDkhV8Uc-GYsHlcr24RtXy8Zu33App5X0ynDplNg_C0GMZojJ0c_rZagJwKsZV5rXRABv6oIVEyZpHMZ_zqR_6gApn68AwUsi2YpRvIecOoe75L-4SyPEvX_hwHSM640BGJ3iZwbXgBukxktd1Uc4POmp271QcGI8sGHeWJMz1NM5bg71FcR4HOd22PM7D7c0vDk-Ig7tE6lTN4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | صعود مقتدرانه مراکش؛ شیرهای اطلس همچنان در مسیر تاریخ‌سازی!
🇲🇦
مراکش
😆
-
😏
کانادا
🇨🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/98211" target="_blank">📅 22:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98210">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d14181bcb.mp4?token=CQJf2EBjhezzLFePji_GOfRP4coU9xCWVK-kz_u2ytg92kCwKON7AFEnOv3OL17azAhe1ECw8ON5ChZQPajcu3AkAsLgQMoiWvc-FZQFols_CMLRv2WAqiAJeBwzuTlVUcgJ7cqc00QYLACKO5A5K-fp7ODQ1sQ1IN77yBru23eKlsPY7ypM2IyuOvhejbU8lYTJcNy77UnHWoCL8LTC-yKMfjHK2xB2xt9jqXbxyMgTZFyL0-5ZlcCSs6sfIo7IINTZmMOMSrjpq9AaIez-ZwXUzXxotkcSeLdpNCP89x0VSP8pZowQag-bG5GHUsBXKMrNIoqpw6O3_QGXoVrOVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d14181bcb.mp4?token=CQJf2EBjhezzLFePji_GOfRP4coU9xCWVK-kz_u2ytg92kCwKON7AFEnOv3OL17azAhe1ECw8ON5ChZQPajcu3AkAsLgQMoiWvc-FZQFols_CMLRv2WAqiAJeBwzuTlVUcgJ7cqc00QYLACKO5A5K-fp7ODQ1sQ1IN77yBru23eKlsPY7ypM2IyuOvhejbU8lYTJcNy77UnHWoCL8LTC-yKMfjHK2xB2xt9jqXbxyMgTZFyL0-5ZlcCSs6sfIo7IINTZmMOMSrjpq9AaIez-ZwXUzXxotkcSeLdpNCP89x0VSP8pZowQag-bG5GHUsBXKMrNIoqpw6O3_QGXoVrOVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
گل سوم مراکش توسط صوفیان رحیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/98210" target="_blank">📅 22:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98209">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گلللللللللللل سوم مراکشش صوفیان رحیمیی</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/98209" target="_blank">📅 22:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98208">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYYX4WM-zngWxgEC9hgbnMryHZ6OmcshBRRCS2yuDotjiUaufnXZATSfLnjs8_Jw5-gJWX0uEjwLiiefIOJttfRVo-hmo55C9mlEoTi9hjtFovR_rPtOwf9lCgSwBRv-nkfcDtDdwjJQjXzfb03yHJymmm69Vr-Behar3cymaeD--2cTHWCs_pgV7bqwnXHhaxYR6TFrmr6-hkmojcFn86B9Dj4Dgw8-eDXZL2IwcEII3C4DDGoQuqTGzXGyU8amxVsnty5ut59kLgELaHE4AvuZA6jIfd2a3fbq0tQnYFrPatbSRBjEZrxaghMm2CpRpjG9ekY7FH6wOfiKQCzqYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانوان عزیز مراکشی خوشحالن منم خوشحالم
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/98208" target="_blank">📅 22:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98207">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9a15c420ea.mp4?token=MpG2cjHjL1H0q8uApLXd4EXHMnUns4qX3Ai37ohDzDeiqzEuhOiS1UmRszAty-Ts4oabc16iyf2d61cp7PkJpY3mi1RC2p7RITkIikGURLRW58VYSbmP0dnsXJaTXzIIRiud11MvFEkeOTGDs4gyxtlcEILTWKSmBevkjOjm0mX9S6nSghT7dxTaZG5ebC3RScOyyhJZHTeKQDm0Y-nYjjEHWzQ-2XgfkV-VkpQ4W0Gldi-hWiWF-CN1VNv6m6zarLobTjtonTvk5UDjoa3840F94LiX9dVIfPT7mlXVFYp_hWI649SoLP-s-3dq7Ye04I-YHWbAPOyCB-Q7mQavLw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9a15c420ea.mp4?token=MpG2cjHjL1H0q8uApLXd4EXHMnUns4qX3Ai37ohDzDeiqzEuhOiS1UmRszAty-Ts4oabc16iyf2d61cp7PkJpY3mi1RC2p7RITkIikGURLRW58VYSbmP0dnsXJaTXzIIRiud11MvFEkeOTGDs4gyxtlcEILTWKSmBevkjOjm0mX9S6nSghT7dxTaZG5ebC3RScOyyhJZHTeKQDm0Y-nYjjEHWzQ-2XgfkV-VkpQ4W0Gldi-hWiWF-CN1VNv6m6zarLobTjtonTvk5UDjoa3840F94LiX9dVIfPT7mlXVFYp_hWI649SoLP-s-3dq7Ye04I-YHWbAPOyCB-Q7mQavLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
گل دوم مراکش دبل اوناحی با پاس دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/98207" target="_blank">📅 22:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98206">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گلللللللللللل دوم مراکش اوناحیییی</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/98206" target="_blank">📅 22:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98205">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQ4uAk76Tbn-BHMRB_2a9WrIbFRMBJUdvChX8g7Cz381EVjGU90b3oDz5mGfcYbiGdcxbxQcqBDlHAgT1EHCTu_XPY4YTvQ7OBQNFwiloNYOGTX3mwtn0A5P1r6E3ItlRGqdQyv0ORRgdrbmg_LTac4qOzM5QcxWKSnQ8jJvPejhAAeee8k1yu7CpcCS_fk-Nd4EaisW3mTxz4yH-tG6XRg6IynKfNANZq8AtR6PBw6tD88hbbNGqh-EjwsYSBbyyvV5vpVrm2S1E5Ht01RR6kkuEEihfgrn89bXpVoEOdrptObZ2jw5g4DnILzjQGjR1xusE00AB3Z1m3Iu4W-ieg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل موی جدید رافینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/98205" target="_blank">📅 22:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98204">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/98204" target="_blank">📅 22:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98203">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mcNLItQIXTnII-_uSMClNruOA3V2w4U5L2Yr9hNK8PTZdCejnvJsm-oL9NzUSaRtJBvRePPMURr2A-Kc22T7ONT1fjjhAbmqyuh5uKAlMs-GZhRweHxB6RtOGCnh8N5elfhp9lhkbvuHjtMdLgEjJJQ4Lo4Ha3ncmiz2HDw_xqsMST1QLTwd2Hy7M4CiEa2eCbtXsktNui-SMOTzhigPUxm_vVcIVhgmmKkjUatWRW95ZLfh9MnRYLo-YcZE5_OLpr670yBMiiw8QHk4MgJU7Nb9aUGgyGFp5REzFVJRiRpE601_7VEDZcWXdz4NyjbqNzm1_cSJLZOViIwNws2jlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/98203" target="_blank">📅 22:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98202">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79bed95c4a.mp4?token=ROxAJ8fOpehQb_EngRa_pWqLTGT8-RpCIOm8poQbTajIw0_qynaX9SRTTK93yjWfj318Ic-Nec9QLez1TcrWBlY1ltQWomFzAHvEF8FranIg7K9wQO_B6yxdcABao7idoF9GuT5EA4FONbLcoWsJBJzpbLRS2kkDymSylq-bh73IEjpe5MCdbq5SMV2XSHH20fwdHHejcB1vYYQ57AuXgMXVEaUy-YQhYFVE-fOO9lX-CMBGQQ2YkhY8qudLZd3LVwe-87_k-HZ-XCI_EyjY5fFkknSUrcr2fpuAHTJfMaTP3fNBDG305riPhYUqTdkfmz6YNeH6yo6jCRTj267qVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79bed95c4a.mp4?token=ROxAJ8fOpehQb_EngRa_pWqLTGT8-RpCIOm8poQbTajIw0_qynaX9SRTTK93yjWfj318Ic-Nec9QLez1TcrWBlY1ltQWomFzAHvEF8FranIg7K9wQO_B6yxdcABao7idoF9GuT5EA4FONbLcoWsJBJzpbLRS2kkDymSylq-bh73IEjpe5MCdbq5SMV2XSHH20fwdHHejcB1vYYQ57AuXgMXVEaUy-YQhYFVE-fOO9lX-CMBGQQ2YkhY8qudLZd3LVwe-87_k-HZ-XCI_EyjY5fFkknSUrcr2fpuAHTJfMaTP3fNBDG305riPhYUqTdkfmz6YNeH6yo6jCRTj267qVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول مراکش به کانادا توسط اوناحی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/98202" target="_blank">📅 21:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98200">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مراکش اولی رو زددد</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/98200" target="_blank">📅 21:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98199">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/98199" target="_blank">📅 21:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98198">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بریم سراغ نیمه دوم</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/98198" target="_blank">📅 21:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98197">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rcsse4UfEKd-pUZunvQEGt8vS9Jv5JBqjVJbPW5nU1OTin3vwf6DKIqrh87LL-xWMMxZS0DwRj9xNME7-n2CTnjtsVEbE3Aiw39R5IoJ21jqCRUGzEYo12pVuUMW_odtwJe46BPLHPrXqdKydClGbCizVaa_FGlv2eL8RrQI2gsuBeFSykQlbyuZMb0MTPKJhu7SkK8HkPP-7SQ6_aqMFP5xmNhcfONghvGuKp-U-sfN0SZ4P9ptgK07ylACBPJOu4m-lrr0KD4K67mFOFrC3AaQxsjcuNkMnK-myZ5n_11KNr04Dsc_7tZd8SMRxXeskUZG0zD2jMZE5TLSOlwmxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه اول بازی مراکش-کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/98197" target="_blank">📅 21:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98196">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcsqZNZ3bQFbtLeCZTI6gowxFmgC6EhB6a0p57mdp6Z_Za6shwMVA99Aqjs3MDwj-72kVVaDiMyRBbfHB04WGMZIefKq0ocApOIUkFZqfFC8GU80Z1KkEfgFOEo3-u8b5Q8feJVj2xz9fpA-qc7FR91tVXUY6wO_7ZtmW7ryIvAFX2scbStk3lAbnBoO4hsqH--rboF1MttjLft3B5-not68ubj2TPReT932pApdiGXR8ezQFGTf16luI03gCxLMy-IuI0iuJBQP1CfFFL3ZTvcR_IOXVIizF_fVPL_k8kmydXYdxpuHvjoOyXpVO3bBDK7BClHRGNcYLUxu5DgHRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی اینفانتینو هم دیگه خسته شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/98196" target="_blank">📅 21:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98195">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پایان نیمه اول؛ کانادا 0 مراکش 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/98195" target="_blank">📅 21:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98194">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwvUM3VgqCp9ycaE8WbdgKBlufdVG7em6Wh8Cg3tsMA4NrNs47PVMuXfpyl7vSP9xOpufQgG9vYpDbdwriqX9vcm4h6psVbdzeBeaxEQdgBRQ3wmP5Q-4WODLFsfgKz08rtxOc0NvnftXhQbjEM-NZGUDg8-StBdpLgmrOyufu9wk2SwYa7IPK3hH8VD-UOuuZmSpknBIbAaPmV-ueNoD4URe4GsKMH5OTJDiWegQ1IMhw-BlYS1P7zBql9RURgBQKS-3kX9yTFcLbDPRVTfjDDGcz0418ggsZcr1kB4CnnRcZc0AKTlPF9rP4XgP4aa10O_xqrLWAIqm_-yQ1PtdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایباری مصدوم شد، صوفیان رحیمی جاش اومد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/98194" target="_blank">📅 20:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98193">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdqfekM_oL9fTvyNa6IP59g2obFJ0zuJJmPr7eSCh39muzuNCYT2uI1HMxWeopYm3VKUTTPm1Bq8melbDE7XiUm20A18pmJAxu-Mp7vEz6CZGZd_yp1UN6uR0Bccm7Beu8sGnRDKt1RKtdwZR05lR9C6mwES3uNV992BDfc3kUr-9N-MdN96GI9LKi0xB0Nd_e9YIu30lZGaajIWXJbJ7e3Aepm7HlejfMpgHdpmoxAnoX5p_MZP7LsvQrZLof95HA0-OEs10hxv6Ow9-aNIvfBHEYcudAL2nsJ7tVtV9_NpGa1pgGX9PHsp1MyJYL0xquo0ve2G5UaH3KIvMhp56g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون همیشگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/98193" target="_blank">📅 20:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98192">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIvv1C_oYgbDAlQbK9_yxQgsnD8STju052XY366bYp1yRoVzs2VIvMmEM-jBh9kZOeH6kl1C-dlXWRFIu_AIwEz1QXU0TTbcZ5BOxJJgwjCZAgKlGf1hIFIgyL3jmxX8LHvJ4CYkPF2Tz4DLkLz7Q-umqcWFjuClmPAkWeMBeLmVFIyVbijW87Z3ezN09CWPUGPE_sMaJpIKCiH8sWcDmw7qXHCikwwb7Qswmyo2UbeD7EIqTxkFFLk_8UU69EOGv9eVJuKikGcS6a9yH4857HLOJKNfjeERRQ3RTOUkv4Yi35TuiHOeGPz2so1Z9JzchEiAe-hp29BgGHO3H4PHPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب گلریه این یاسین بونو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/98192" target="_blank">📅 20:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98191">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سوپپپر سیو‌ بونو</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/98191" target="_blank">📅 20:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98190">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">شروع بازی کانادا و مراکش</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/98190" target="_blank">📅 20:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98189">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🇹🇳
فدراسیون فوتبال تونس از انتصاب هروه رنار به عنوان سرمربی این کشور تا پایان جام جهانی خبر داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/98189" target="_blank">📅 20:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98188">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OF5zJaNFeTTo-3w_ymFWvRhm2KDCeHjhSfggGi3UIBP7my_evtgFqcO7xZHh5mBolf_I6PJztBsBva5XNxYe4u5GODdTXJ8Yy58wsnNbNHmcSJdvrDgKrCvETqidS_HK2_IJJooiEw6_4bZF4QNRSf7NhZcgXzuR3MJVqdh28b4bKKjBSHz6Mjo7ufRTXFPwHgociQNFB9avkKAi9Y1gHT2QteJhmbfY-0RNNdzy2_WJKYVbIZFNqCz40pappc5Ic_lgaFn0iFP8fJvlxQApZji7pg4N8xHaLFIGG-j3fUJpbEk15Gx1p5oBbfUBAG3Ry8nrmB-lVD-2q4abIbOcTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
🇪🇸
آنتونی تیلور داور بازی اسپانیا و پرتغال شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/98188" target="_blank">📅 20:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98187">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N38WORcAe2cCP9Ta_LjUYjRzrDsu-4UwERUdadfrhqLKX0e0unkblZ3vIAhPWQen_5u6Up499Tlwiu9Iq5RQHsN0XZqLAA_H_bYqV_1CLPjo1J4TKpi96njGF3u3pn4x6xtoSDDwLMsTypLdN6phnwSHl9ukSMTwQR_K0wp5Ig8F0LQUqOTKjbzj3AfUPdTTGh2FP0vTldlazOGdMVEDlqDM4V8vHrI-0GHgKydQ49V0O8MhL9opLAKjSOxiEm-5hlCE-0lix6qJe1aRCQv01RvdNswsR2jFt9uHuljPiTzteblCamNZFkUfOBj63R3AlY53FHw6n9m2Sh0XAZV2hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
پدری، هافبک تیم ملی اسپانیا و زیدش، الکساندرا دورتا، عکس‌های جدیدی از کوه لی در لس‌آنجلس منتشر کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/98187" target="_blank">📅 20:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98186">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXMTQHjDdV2nl7PRYK-qDFKkwlPqf_DuDtEpZm-aZRp2CYrWC_MNH6dPWLT6enLUtmeXrTati_7VLO-mHTNeep4Zib_cipx9FA9SG_rC1w4ScIHFGX4mx2By2iJpU0CEEQ4IZnnudQIu09Oyohm739DycB6cmpBU9kU4WVm-Ztrg368UWZ4qMUYYF23b29inwRgU9kbxUKQhVoWF-EBIys3UAvKopT9CSCZ_Ur6NSeLKGnZLvfhFJ7xqMbDaXx__d_T0m5dLAo6LXgp7_VzedirB2pB4BewDMJfjli-mt7oeWKdcOztRBlVOB803RFlUF-nf7g9wMMILIznuWXHb0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
#فوووووری
: بشیکتاش ترکیه با آرسنال برای جذب تروسارد به مبلغ ۱۸ میلیون پوند به توافق رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/98186" target="_blank">📅 19:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98185">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oL8chZRAukZ9rMygwq320cS4thPmXbSq_VIzlNZGbp1RrvLlhL8OOMC47JVZP4TLeTHd0uitZB0wgvw79JhdIQwyWcx5UnK5NHd_XouaSqn_E-Cg0weVtfJDmwEOpnYz4vRPFLoxjeAA5Dsmkr7wnigv5BNntF7H3i0NNkOAKjHIYMoVw8jo92K7IdvoEqg-qUYeyHWJEalkhRgoy8Ufgl-SQhk5zgzZG7C-Pm-J_MpSy0Ow2zYqR094PItHGZ0O-tIOq9qvmk7rshH0gJbbCwO5RLhRaheTU_FABSR5Swaqk5SpGo3UmNBEME7yA0RNZTr1jAl08oLGS_MV0TdgUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
— RMC |
🇫🇷
🇵🇾
فدراسیون جهانی فوتبال (فیفا) اعلام کرد که به دلیل شرایط آب و هوایی، احتمال به تعویق افتادن مسابقه بین فرانسه و پاراگوئه وجود دارد.
‏"ما وضعیت آب و هوا را در فیلادلفیا به دقت زیر نظر داریم و در حال حاضر احتمال زیادی وجود دارد که به دلیل شرایط آب و هوایی، این مسابقه به تعویق بیفتد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/98185" target="_blank">📅 19:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98184">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4be21116.mp4?token=DtSDbTKZ-QC5VJSrlSH7PmYja75j7_m4rPXK6zvMKS_jLFm0JVbkfs4ETstBmG_sdCuwx9l5F11f3VT2vNddpPX-7TajlaBO9Dg6f6eoYTzbQ9Ke7yaO5dk3faHAOY6jlGVJCbhsADhYd1Xj2CqLD_JZbQHxTU_h9Vi6aT4koiBT7MTGiS_-I6MTpCP1M_itS-rEeqhqgFYmOZ2HokivfX4UOPleFOkE6hQqonvzsCY7ajtwTTUVu9VllzxIKglzw4hKrJrc2ahY-hTKFtUNFCmp4dBIQnItETMB2M1iKzpuKvHcD5Lox_ODqCnBXbZqOGIyASnmdl08UtX_nqeoCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4be21116.mp4?token=DtSDbTKZ-QC5VJSrlSH7PmYja75j7_m4rPXK6zvMKS_jLFm0JVbkfs4ETstBmG_sdCuwx9l5F11f3VT2vNddpPX-7TajlaBO9Dg6f6eoYTzbQ9Ke7yaO5dk3faHAOY6jlGVJCbhsADhYd1Xj2CqLD_JZbQHxTU_h9Vi6aT4koiBT7MTGiS_-I6MTpCP1M_itS-rEeqhqgFYmOZ2HokivfX4UOPleFOkE6hQqonvzsCY7ajtwTTUVu9VllzxIKglzw4hKrJrc2ahY-hTKFtUNFCmp4dBIQnItETMB2M1iKzpuKvHcD5Lox_ODqCnBXbZqOGIyASnmdl08UtX_nqeoCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
در کمال ناباوری و سرعت، به یک هشتم نهایی جام جهانی رسیدیم!
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/98184" target="_blank">📅 19:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98183">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a342fb6d.mp4?token=KXhfFO8G7xlkhjqdkB47IQ_G0yW7Qc0P07AJf3RKgePsiAnSHkKbGkEpBU3dKTIGLEjt5xiH_Y98OvlhV6BggCNLbWFc-K85wZIYdFUXXP541lk4w8tMyUtJSCZBoUKGPQx28tEP1gOAjS2JkibCWN5hQIRXYHVvx7aznkcQttpUj9rCJXH_YFUtdalmc8KwUVKngU-IaXcxAhyB7-q74OXVfEBuoPgXWy_HALhTGR6ZavN4UrYewQLNrsqQ-2gZKeXJIswLmzGLGpzSRqKMP9a72bI4V1EiQp7rO2j9xKpQ_2iswTmdqQ7b38vClG_RNx4CjDTKaVaJbXAYiRYg5ZgJrsxrR7V-5253Y483ahhQJzF_sstGI4_jAf1tjpBtL-Em1QgkapCS7B7aiRqOderWq6BE2ArdNmbOmPXxurDA-cj7TKVRY_cI95IYLVYqaITDzOWxEJQVAzX2a2q8DqmsnpEe8BNRlgz6tEKWuxZUWr52mXK8HkJ_ZJcFz2eMowDC-2kP8ikxTRlRATWf4Ousi__CR6lREZ7cbn9uzDo277FtPSsWP5JCVcoxeKZaFkP2-B_U-S2R_xxc9fTx3Z9QG04sOgH_UfJUqKtcDs2EWSjDNBCDuDFhQ7vD2PZYokN6jhyuOatGKk9BRMeoSGAiV8h21wh3ryownjAWMpU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a342fb6d.mp4?token=KXhfFO8G7xlkhjqdkB47IQ_G0yW7Qc0P07AJf3RKgePsiAnSHkKbGkEpBU3dKTIGLEjt5xiH_Y98OvlhV6BggCNLbWFc-K85wZIYdFUXXP541lk4w8tMyUtJSCZBoUKGPQx28tEP1gOAjS2JkibCWN5hQIRXYHVvx7aznkcQttpUj9rCJXH_YFUtdalmc8KwUVKngU-IaXcxAhyB7-q74OXVfEBuoPgXWy_HALhTGR6ZavN4UrYewQLNrsqQ-2gZKeXJIswLmzGLGpzSRqKMP9a72bI4V1EiQp7rO2j9xKpQ_2iswTmdqQ7b38vClG_RNx4CjDTKaVaJbXAYiRYg5ZgJrsxrR7V-5253Y483ahhQJzF_sstGI4_jAf1tjpBtL-Em1QgkapCS7B7aiRqOderWq6BE2ArdNmbOmPXxurDA-cj7TKVRY_cI95IYLVYqaITDzOWxEJQVAzX2a2q8DqmsnpEe8BNRlgz6tEKWuxZUWr52mXK8HkJ_ZJcFz2eMowDC-2kP8ikxTRlRATWf4Ousi__CR6lREZ7cbn9uzDo277FtPSsWP5JCVcoxeKZaFkP2-B_U-S2R_xxc9fTx3Z9QG04sOgH_UfJUqKtcDs2EWSjDNBCDuDFhQ7vD2PZYokN6jhyuOatGKk9BRMeoSGAiV8h21wh3ryownjAWMpU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇲🇦
هواداران مراکش در آستانه بازی با کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/98183" target="_blank">📅 19:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98182">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aj2PgvHuAOgFzVgbR-4lQfSXdrpXyEKZ2WDThQUCh_T0Q526lok6rQpo-HGzaQLiTYRObnVBJqtv1ZX3I53_OzBmdsMf3vX0Wc5SiV_a1S3P2pcFeu9-LOYxJM4ajcYdOei31CsSp5CF9AMe8OUS1UucwJerVSf4udvEqkwyjK49BZ-kJeVET9DgJ4dMwkbOBk0Jcaqpenrchx1irSP1yz-qrQDDCQQePJy5Re6zWGiUmiZeCvXpuCLfWDuPjn3m3-sSFaqbx0iu-g8ZMwbZ-OoUzP5sF1X5PITKINoM1aOnSI3KJKwaYTAtEKOuYVf4ie8F8WNNuOVptdnmTm6nGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇦
ترکیب مراکش مقابل کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/98182" target="_blank">📅 18:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98181">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKtpJ_KJGDqr5UYabpwHqDQJ1R3qTszwn7NJIyWgmHMm0Y1k8MsY2ULQcu7Fe1XEwvdnHBn2ItxxsX0NTZVqL7_NYBktVmDgIvhRi1tvmyta92a3RKOdIExiD4d2A0B-NHvux5OQLDHThBRFhi1tRADgvMQ6Jj3HZq6Vrmmi-uZMqZkIqsJrN4Wj0zVF9vD5rIbm3fL01X26dMAuVUa-9ARZtCxKxi6jdFbQMcFnHVB9TO2AB8yzcUOWDynB2FzENKymr48H-gRL_WZrttviTppHSR4IliWkZ5DNfeLCEMtZUC7Rhod8xBM7TvJo8NWf7F0mT8iNN7yAG0gsrlOBqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
🇨🇦
ورزشگاه NRG برای دیدار مراکش و کانادا آماده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/98181" target="_blank">📅 18:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98179">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nZoLubezeLmDQ4DO54rJAahRT0fvtkvRMDTCY0WsPo96LGqtUy4nE3hQHtiYNiB31vkgpeIVaBCNTxjrPiTjZczMD2zBcBj-us8r0NUoKJJrjbynM86__Ye4fHnb2fCTSu0XxAcVmdh9fJ660wjlcyu3AasnptTjt2smMrfws4l3_G200rJ96WtaZFtCEdQnk0_67rM2sdXjUUhG4TZ0lk52roxqR2NNaYgnacqdfnD6MSMbEqrQsGvZVyO3C0y7MBkMVKS1Agg9jH6IXCiRhNpASSGBOI3eXdx0V3t0Xm5_f2yAuolI1MXnFjQG-nr_Dre-HuWEJU8II0IBgdw7qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NQyBLzKRdHU0OWvxXRHZ5mtj1VkeSnMpS7CtYCxM286fsVd35D7f78jVDFp7qXMIAeqb6WqhyuLOIGILoxTHfv0w825vnHwxZwR8tTupv6qiRGAMdPM_Xa2SKlVoat1zlUGNX6DNqonviDc_n9T7_B16IC4mHNEGm8R-SpT_R4kiUNiUNsPVHe1viQfWq-zPzfb9HJC2vlPsCTjgCK9ItsUq_P4Z88n2yEMtT2RH2lmzCteFYCJ3dmSRH3wswCkQoGjwum55fMZOvpWhxWbmuse2xJj9FaXfOzM-4dPlnW2z08Jf8bTclfPjeXnyXKug-vEb-3VSInmGIpxWTZItGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
📊
طبق گزارش سایت Score 90:
✅
احتمال پیروزی تیم‌های ملی در هشت بازی مرحله یک‌هشتم نهایی جام جهانی
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/98179" target="_blank">📅 18:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98178">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af013992f8.mp4?token=qZyUhyzdicKgkSmTT9bbZP8faRqFBUYq62ILZF4l8hg7gzGOhmNSzAB1wtxa4mkjWp63OW3DN6jPIEJbKI2vdnP2roeZ-vW306eRIzoLVHfZNPk1YZS4h709Dr-Yi-MMSnInUI8DJXmDE4iADZ62N3m_3Rj1FQhxgt_-4CflHOlRyrbkcRvOzbWAiYSYoysbRLatmyHU01QT1W9y_BPkk1K_xFECsaDf77Y7hOnT6imKhXHLkZTDoBwvGapwQmSuowzhyS6277zpK9_ZdzB8WRw8ORcpkPBmQ4X0aSKkUo2cZe0h2PJ_UgtdgZ_hNgk9h7FkYRMnqJK7UtSrqkR8dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af013992f8.mp4?token=qZyUhyzdicKgkSmTT9bbZP8faRqFBUYq62ILZF4l8hg7gzGOhmNSzAB1wtxa4mkjWp63OW3DN6jPIEJbKI2vdnP2roeZ-vW306eRIzoLVHfZNPk1YZS4h709Dr-Yi-MMSnInUI8DJXmDE4iADZ62N3m_3Rj1FQhxgt_-4CflHOlRyrbkcRvOzbWAiYSYoysbRLatmyHU01QT1W9y_BPkk1K_xFECsaDf77Y7hOnT6imKhXHLkZTDoBwvGapwQmSuowzhyS6277zpK9_ZdzB8WRw8ORcpkPBmQ4X0aSKkUo2cZe0h2PJ_UgtdgZ_hNgk9h7FkYRMnqJK7UtSrqkR8dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهرداد صدیقیان: چون رو جورجینا کراش دارم دلم میخواد پرتغال قهرمان جهان بشه
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/98178" target="_blank">📅 18:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98177">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🙂
🏆
🇪🇬
شادی سم محمد صلاح بعد بازی دیشب و صعود به مرحله ⅛نهایی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/98177" target="_blank">📅 18:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98176">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwhfWmdVpQTSLmgSz1cuFVtFxQr-x_r-lfsVKa0sPNra5_sO5EpLaucBhBRC_Y3m3SeQKINRTK7aQ725OaZUkMglZkwbS7xR_9DW0FcLwHVSaKGRHOwT7TZ1QbuLXTUjLEr-9JxRdLfTnFhXsIPh0vnn-lG69z98FYHrhwD67UseLC0XGG-6oA66pMVFVIK21gm2ZrsjAzI58UOKBfKDtq8dv75dlLd_WCNaTYUIBPhNToQOO4HhEyZwmDMyS-TiDg1MLCVfGR7aMRNgBoefscTM29KNtXU4mB6PhC1WuBlwBYK0-JUamKpC5ah0C5T9KRG0Hxbp_KV0H6TmaLpduA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
میگل سرانو:
باشگاه رئال مادرید اعلام کرده که منابع مالی نامحدودی نداره و انزو فرناندز، هدف مورد نظر رئیس باشگاه نیست. فلورنتینو پِرز، قصد داره یک معامله بزرگ و مهم در سطح جهانی انجام بده و معتقده که اولیسه نامیه که باید به این تیم اضافه بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/98176" target="_blank">📅 18:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98175">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
😐
مهرداد صدیقیان بازیگر سینما میگه تونستم مخ دختر مایکل اوون ستاره سابق فوتبال و برنده توپ‌طلا رو بزنم و حتی برام هدیه آورده
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/98175" target="_blank">📅 18:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98174">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gudfLJ7XJyeEgfLhUAwMtnpX8EkxjI9FMfP4NMFdMgXT3FrNiinpUadxEOq07AQISRq7xHrrUIRLo9Z9MqIkmWBmGUrYX0OMyqpVcMoXvlQsH0Lplg39ixDVLONNBP6QvxhNYfhi69vI7U33LQxetWdpCWmcr3V8FMfCCXaYaVHzBSi6rYVAAXfmW1TwoMygQ9XOito8ZLJ0PIckNFsCaOXuA71sc6KRnWcpCo4BnW_Pfke6TaSxB5Ob3f2LWcF0VMS-KRwTQsb3KIxdv2WoSoaXlDL9GtecMdsYSuWkjsAW-xpEPIp2mkD0bLj3Acz3qseU4C7EuJTK-sP49dedKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🇭🇷
اظهارات فوزینیا، دروازه‌بان تیم ملی کیپ‌ورد، درباره مسی:
‏" به او نزدیک شدم و حتی فرصت نکردم زیاد حرف بزنم، اما او بلافاصله به من دست داد و گفت:
‏' عالی بودی. تو یک دروازه‌بان فوق‌العاده هستی. حتماً مردم کشورت به داشتن تو خیلی افتخار می‌کنند.'
‏ شنیدن چنین حرف‌هایی از کسی مثل لئو برای من خیلی ارزشمند بود. از او تشکر کردم و گفتم: ' ممنونم، لئو، تو بهترین هستی.'
‏ سپس از او خواستم پیراهن بازی‌اش را به من بدهد، و او لبخند زد و گفت:
‏' حتماً، آن را به شما در راهرو اتاق‌های رخت می‌رسانم.'
‏ این لحظات را تا پایان عمرم به یاد خواهم داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/98174" target="_blank">📅 17:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98173">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👀
▶️
🇨🇻
کشور زیبای کیپ‌ورد که علاوه بر فوتبال جذابش، این جاذبه‌های دیدنی رو هم داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/98173" target="_blank">📅 17:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98172">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a6f3f631a.mp4?token=LgL8TG_B-DM_dIXDVt4g-8JCLxsJ8PGv4iHGAUaHGaazCSHmWu4TAohUR2ilTRXEYyR2FCHkgpzTUQTcjdyGsxuIiEaZD55v3YaOm4eX_buwpAoSujYJPJBiiTJLeod0o7ByqaqUfYaEOp7DF2Qt1V0dXnezRayofl6fOi2Y1wOsjHAaKjsNHlcZJPN469zKfi0MHuonhkbqBvQsLha8BlmqhJKy0gm1HDDlvx9qMD9FG6EMPL77paHbAIUTUWhA3WK7hiPwrjt97yb9SlK6RmTwgL4aIiwDMl2FiAtAJhpf1t_sniV5xQukXtMOgOFFpPQVtL_sD8ahI7i2h6H_Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a6f3f631a.mp4?token=LgL8TG_B-DM_dIXDVt4g-8JCLxsJ8PGv4iHGAUaHGaazCSHmWu4TAohUR2ilTRXEYyR2FCHkgpzTUQTcjdyGsxuIiEaZD55v3YaOm4eX_buwpAoSujYJPJBiiTJLeod0o7ByqaqUfYaEOp7DF2Qt1V0dXnezRayofl6fOi2Y1wOsjHAaKjsNHlcZJPN469zKfi0MHuonhkbqBvQsLha8BlmqhJKy0gm1HDDlvx9qMD9FG6EMPL77paHbAIUTUWhA3WK7hiPwrjt97yb9SlK6RmTwgL4aIiwDMl2FiAtAJhpf1t_sniV5xQukXtMOgOFFpPQVtL_sD8ahI7i2h6H_Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇲🇽
هوادارای خانم انگلیس در آستانه بازی با مکزیک که پسرای مکزیکی‌رو تو خماری گذاشتن
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/98172" target="_blank">📅 17:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98171">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPZoNPfkkWFkPnksXzK9IwkYDilCZM4Jp5NZwpZ-a1stOeSpp-ugqaqZQjrRqPhrDdOk9Rfi4P0kZW99pmqkuf3zZzx1shzU3kb1_745F912rI5OmgATx9S7UYXM1JB_RURZ8RAHk7VlUdMSyQoq_blzSIP5jI_h610gAXLqFA1goamksSisEUeiRJ9lvJG9XJ1HL3tiVDD63OcUxxcFeWQSI8ZnVTN_k6vuffkf8RaxCaNPRklrBcYv37vXXe0-ZTIWJ58Sc6lCw1qGEA15RQ1CBWqxElZjfMoD632635STuqnzG-Rx4lJ8fDPbY7yIvQQ66WBChb10wzoD5DrQ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
⚪️
فوری از آاس:
باشگاه رئال مادرید در این تابستان با هیچ هافبک دیگری قرارداد نخواهد بست. این باشگاه با جذب برناردو سیلوا به عنوان تنها گزینه در این پست، رضایت خواهد داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/98171" target="_blank">📅 17:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98170">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f0c663da9.mp4?token=LJPLRApHzP-P1CPdCiDh-kn3yyyh0788PKYdeJ8sL685jB7Ls3j8_L6uwFt3Pmogfl4nqKFsNjVcSFq__CW_-PtiRmxMyaxIOE_t6zI3eCR3n0ym3qcQg9r6j_-ylHztk6jaAFoF-RaFJZRXWMllBAdp4yhcngd5JfewvcbAid-4QFrq4jt_0-v06v25kQpcz5a_BRMbN94rDvRYd-lciR4Co_Og_KorSKKVpUvIycn3THClR9RWuvIbIsTYUVndLiIJrHoPPzQfIih5PNcpeclQf2TV37lsFwQxpLR-wmh2L7G4CnFzXqXYRPGsXuVxCbj_eUPCgSemU3eCIKLiUIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f0c663da9.mp4?token=LJPLRApHzP-P1CPdCiDh-kn3yyyh0788PKYdeJ8sL685jB7Ls3j8_L6uwFt3Pmogfl4nqKFsNjVcSFq__CW_-PtiRmxMyaxIOE_t6zI3eCR3n0ym3qcQg9r6j_-ylHztk6jaAFoF-RaFJZRXWMllBAdp4yhcngd5JfewvcbAid-4QFrq4jt_0-v06v25kQpcz5a_BRMbN94rDvRYd-lciR4Co_Og_KorSKKVpUvIycn3THClR9RWuvIbIsTYUVndLiIJrHoPPzQfIih5PNcpeclQf2TV37lsFwQxpLR-wmh2L7G4CnFzXqXYRPGsXuVxCbj_eUPCgSemU3eCIKLiUIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇦🇷
🇨🇻
امکانات سوئیت ۷۵ هزار دلاری ورزشگاه میامی در بازی دیشب آرژانتین و کیپ‌ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/98170" target="_blank">📅 17:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98169">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58ab6c152.mp4?token=CY2oqK7JvW0NSD0LxrK0ySMZO-VDEDNqJ3pILsvJuGprKWGdualW5tn7dHQyYrkC4D-kvOE3jzKfIP7BECL0u_4hPoyesTs1IQhKRHz73LuIHZjO8lb8f2Savn_mhv5yEYDymoC4DujDn0B5X1_DGA0U43iYelAWOvT82ptmbWH-_oxEf6xWoHHgy1x85WzUvHOBg6L0lDA4Nq8SWGovlWCjl32jK4MRDF5GQEyXFxOAL-kn7xPsTg4PXDOSm4kVjEAQVQt47qgXRtqsx5Xz2ujIxMuToMgpsj3ShCm44An4kAEAFmS4LgnfPB5b7LTCtBYb33FKScHZvnX4mAVHQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58ab6c152.mp4?token=CY2oqK7JvW0NSD0LxrK0ySMZO-VDEDNqJ3pILsvJuGprKWGdualW5tn7dHQyYrkC4D-kvOE3jzKfIP7BECL0u_4hPoyesTs1IQhKRHz73LuIHZjO8lb8f2Savn_mhv5yEYDymoC4DujDn0B5X1_DGA0U43iYelAWOvT82ptmbWH-_oxEf6xWoHHgy1x85WzUvHOBg6L0lDA4Nq8SWGovlWCjl32jK4MRDF5GQEyXFxOAL-kn7xPsTg4PXDOSm4kVjEAQVQt47qgXRtqsx5Xz2ujIxMuToMgpsj3ShCm44An4kAEAFmS4LgnfPB5b7LTCtBYb33FKScHZvnX4mAVHQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گریه های شدید یک خانم تو مراسم تشییع خامنه‌ای :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/98169" target="_blank">📅 16:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98168">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a2a62f27.mp4?token=NWgQ3ihfBwIQxQhc0wI_83xGSdTkaF5G20QSASYJ2QbgTKz8PvH2Ghimw0i0q7CmfNHtLc7gqVtFdai48NGRaWJFjQWYRt7PbTo35LrqIDkTaVUvxt8DVIO1HT_V-Np7iBCYekUK4YClOXm29Z_qy4ITt_QGRJv0hqaAhRUt1ZjluLB8KSKSu6aGxw6VJp6h1zRp0vuJKQpX7W55jUzm844cWZSm6hQxNgALvPcComP5IIeoisSTYRlekmYC5OMfhlGNO6GXmCq62RARCYoVHzVH3aDKbP_-s53Dt-FCAyzjYe9Bb9Mro1k73AaDv0OdSjnvWuNBQmNr6bIjlC85hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a2a62f27.mp4?token=NWgQ3ihfBwIQxQhc0wI_83xGSdTkaF5G20QSASYJ2QbgTKz8PvH2Ghimw0i0q7CmfNHtLc7gqVtFdai48NGRaWJFjQWYRt7PbTo35LrqIDkTaVUvxt8DVIO1HT_V-Np7iBCYekUK4YClOXm29Z_qy4ITt_QGRJv0hqaAhRUt1ZjluLB8KSKSu6aGxw6VJp6h1zRp0vuJKQpX7W55jUzm844cWZSm6hQxNgALvPcComP5IIeoisSTYRlekmYC5OMfhlGNO6GXmCq62RARCYoVHzVH3aDKbP_-s53Dt-FCAyzjYe9Bb9Mro1k73AaDv0OdSjnvWuNBQmNr6bIjlC85hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
برد دیشب آرژانتین احتمالا بخش مهمیش مدیون این سوپر سیو امی‌مارتینز هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/98168" target="_blank">📅 16:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98167">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5efd98ee66.mp4?token=SWzTRplsLRgefH5Cwtk6eDNDDpTf7nOC8r1iJbqfj0f_HvuXna37lh7k-TVoOumogq6wk_9zFKmJQ7G31OO_PnPf0EzXAf6PmPlRGuvXZWVRoi-HuyspNqX1qC8TQIwR_-K3MkWHcvp3dpF9zg8DKsE2RuBlel3UMCJlUl00S-j2ELriFYnga94KkgiyMUjM25W9rgHVj4xnEwVwfsXu21i2OQ89lae7pNacvY28fAZ2SkubTkLPpp4enAKWWR_eDWWZJ6v-gh7fAYngtPZcjPcjR1StjklSo7m1I-3I-93NUoqOmjpdocRX1Madc0yXipXKX9jlxn2eYDaVbr3kLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5efd98ee66.mp4?token=SWzTRplsLRgefH5Cwtk6eDNDDpTf7nOC8r1iJbqfj0f_HvuXna37lh7k-TVoOumogq6wk_9zFKmJQ7G31OO_PnPf0EzXAf6PmPlRGuvXZWVRoi-HuyspNqX1qC8TQIwR_-K3MkWHcvp3dpF9zg8DKsE2RuBlel3UMCJlUl00S-j2ELriFYnga94KkgiyMUjM25W9rgHVj4xnEwVwfsXu21i2OQ89lae7pNacvY28fAZ2SkubTkLPpp4enAKWWR_eDWWZJ6v-gh7fAYngtPZcjPcjR1StjklSo7m1I-3I-93NUoqOmjpdocRX1Madc0yXipXKX9jlxn2eYDaVbr3kLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
😆
رفیقای من وقتی دختر میبینن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/98167" target="_blank">📅 16:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98166">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🔴
#فوری‌#اختصاصی_فوتبال‌180
🔴
تا این لحظه و با تصمیم اعضای مدیریتی سرخپوشان، سرمربی آینده باشگاه پرسپولیس به احتمال بسیار زیاد گزینه‌ای داخلی خواهد بود و خبری از سرمربی خارجی برای فصل‌آینده نیست.
🔴
در بین گزینه‌های اصلی همان نفرات همیشگی یعنی یحیی گل‌محمدی…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/98166" target="_blank">📅 16:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98165">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🔴
#فوری‌#اختصاصی_فوتبال‌180
🔴
تا این لحظه و با تصمیم اعضای مدیریتی سرخپوشان، سرمربی آینده باشگاه پرسپولیس به احتمال بسیار زیاد گزینه‌ای داخلی خواهد بود و خبری از سرمربی خارجی برای فصل‌آینده نیست.
🔴
در بین گزینه‌های اصلی همان نفرات همیشگی یعنی یحیی گل‌محمدی…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/98165" target="_blank">📅 16:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98164">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🔴
#فوری‌#اختصاصی_فوتبال‌180
🔴
تا این لحظه و با تصمیم اعضای مدیریتی سرخپوشان، سرمربی آینده باشگاه پرسپولیس به احتمال بسیار زیاد گزینه‌ای داخلی خواهد بود و خبری از سرمربی خارجی برای فصل‌آینده نیست.
🔴
در بین گزینه‌های اصلی همان نفرات همیشگی یعنی یحیی گل‌محمدی و مهدی‌تارتار قرار دارند و چند گزینه عجیب نیز به گوش می‌رسند. از طرفی نیم‌نگاه برخی اعضا به بازگشت وحید هاشمیان نیز می‌باشد هرچند که بنظر با واکنش خوبی از سوی طرفداران پرسپولیس نخواهد بود
❌
در صورتی که با نفرات اصلی ایرانی توافقی صورت نگیرد، گزینه‌خارجی در مراحل بعدی مطرح خواهد شد که به اطلاع شما خواهیم رساند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/98164" target="_blank">📅 16:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98163">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b6f4aebb1.mp4?token=ZG5-n2W9tvWNElzQ-9eO_TnubWwH3Ci1aA9gNZ-pjeNRyL4wT29zNyqU0qBzP8kBN-dmdBiYj4NUW4dQJwtr0y__SfVOZ49SPmDYcwgSchT2orRBErLX_2b4ryocWR_LBCy1vaJUAuCSGls4z2s9get4hzMG7moKq17F3YWMXt_jmg5nFi9SgbBL_TqSiqYIhODUkr-wxdVgnz0Eucw67mO83M4YDVCS12GbfZxSDv8EonEqQje_RQxhiRlc4529jwpo06micFXr10FmixZAEYiNFPppUh6iFUNAa5KMuMWYYU5VrN6CJyE8VqZhd7CJx92YuxfhvyEQnCZ6Zji_IUasV5UepTeT294PEpaKVCOXv8awYDX9k7Otr_ZX0fz0Dyl7DGlyUIxnhWbCK82mdrv6V6YCBJVg62n6oKSLtqDBEbxwOYFIP0VtRMDmss42EWZgREOsanuOszBgdgRXpddetrGy16MYXhGKKRJ3_cg_KQqdjCWLLAS8BaEaPk57Waw_6O6cuzvVMZ4PLvHiP9Z6tVNhH8Tb-pE1YjM6_AzA-HRuFVSZpurkv_2CY0TZsrYS8l4mJN0SC_tAaSlqwFtd2Oo4CWLwLPDto4r3xUTgN5S9nwVR6ARFHfyUSz-JRpWYuStskekC06_RUIZgsEt3nu5TSo4yPtl4PEokE3k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b6f4aebb1.mp4?token=ZG5-n2W9tvWNElzQ-9eO_TnubWwH3Ci1aA9gNZ-pjeNRyL4wT29zNyqU0qBzP8kBN-dmdBiYj4NUW4dQJwtr0y__SfVOZ49SPmDYcwgSchT2orRBErLX_2b4ryocWR_LBCy1vaJUAuCSGls4z2s9get4hzMG7moKq17F3YWMXt_jmg5nFi9SgbBL_TqSiqYIhODUkr-wxdVgnz0Eucw67mO83M4YDVCS12GbfZxSDv8EonEqQje_RQxhiRlc4529jwpo06micFXr10FmixZAEYiNFPppUh6iFUNAa5KMuMWYYU5VrN6CJyE8VqZhd7CJx92YuxfhvyEQnCZ6Zji_IUasV5UepTeT294PEpaKVCOXv8awYDX9k7Otr_ZX0fz0Dyl7DGlyUIxnhWbCK82mdrv6V6YCBJVg62n6oKSLtqDBEbxwOYFIP0VtRMDmss42EWZgREOsanuOszBgdgRXpddetrGy16MYXhGKKRJ3_cg_KQqdjCWLLAS8BaEaPk57Waw_6O6cuzvVMZ4PLvHiP9Z6tVNhH8Tb-pE1YjM6_AzA-HRuFVSZpurkv_2CY0TZsrYS8l4mJN0SC_tAaSlqwFtd2Oo4CWLwLPDto4r3xUTgN5S9nwVR6ARFHfyUSz-JRpWYuStskekC06_RUIZgsEt3nu5TSo4yPtl4PEokE3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
🇦🇷
گل‌سوم آرژانتین به کیپ‌ورد از این زاویه جالب و دیدنی تماشاگران رو ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/98163" target="_blank">📅 15:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98162">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-Vr9eTRDWiK3Dc2ewDfBlhfnnttWIsuhvI-YxciVORhH3M4pTCVAqYn93TqUGN2VYiYGFUiO2_-bxNMDyjVGkw2UFFoUwFeJo9hkTFvOZkR0SbZkgbbjvYtN4D9m52KnI-7UQUyYFoVJMTVQ0YnJXnb4J24hAj3e15bdWYtZmv2rdo7FfQZuaUCjtZ2gj2ohJHdLsn5Svq1NNNJ8aHcb9sj6_pBIJ7xwFo2uah8AcnNot1Y9erNRjqOAKGRe4EKonxsGy4oZFz2MMJxfs6_3h-Yc_0wGixrj7yIXWuSs3ePX_St_6wvf_f-yHXqBqV26LKN77WjMIWjBgqOlXrDew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریک فهمیده رو هرکی ببنده میبازه، 1 دلار بسته رو صعود مراکش
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/98162" target="_blank">📅 15:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98161">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/98161" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/98161" target="_blank">📅 15:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98160">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/98160" target="_blank">📅 15:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98159">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/341bb1b1be.mp4?token=L73fiFyuP7eI3oifk7_nUdV-yXNMXsAhVk79hQ_T6_ZGgPcLK4Dv1Gh6J2_jFLC1I6poi4hkgESMMn-iaI8iV_5FHBVQzdTYK5kODqxgQiTrYLiYt7c8FhS5eF_l-6jIndzD5Mvsg0_fBI6CT_8G3L5GRUiPYwPUj-reuP6fzI73QW0GN63w65y2mDKXD95yfYRTVnw4ZH8w-ixXTaLLC5rQn-YFzXcK5JVKpvikHexGEas_YMo3TR_avJJHOUx_Wi2bbKRpJbUidC0ZoWgESyDvDezwNZkRgAkHGzPFmZ9ir868_wYnGoRNl155puTwnmZHhjVxCNhl6opSnhNCBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/341bb1b1be.mp4?token=L73fiFyuP7eI3oifk7_nUdV-yXNMXsAhVk79hQ_T6_ZGgPcLK4Dv1Gh6J2_jFLC1I6poi4hkgESMMn-iaI8iV_5FHBVQzdTYK5kODqxgQiTrYLiYt7c8FhS5eF_l-6jIndzD5Mvsg0_fBI6CT_8G3L5GRUiPYwPUj-reuP6fzI73QW0GN63w65y2mDKXD95yfYRTVnw4ZH8w-ixXTaLLC5rQn-YFzXcK5JVKpvikHexGEas_YMo3TR_avJJHOUx_Wi2bbKRpJbUidC0ZoWgESyDvDezwNZkRgAkHGzPFmZ9ir868_wYnGoRNl155puTwnmZHhjVxCNhl6opSnhNCBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
عادل فردوسی‌پور: اگه همین روند ادامه داشته باشه، علیرضا فغانی نیمه‌نهایی یا فینال رو سوت میزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/98159" target="_blank">📅 15:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98158">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkqYqNbmrZIUbyeaMHzP7qNaUeGJd-iN5owsisWdfpaWrEs9aQmwIjidLgDEgC8jnRIZp19rEX-0lQoBIrYqwiq99SWefCwyfgmI_To793KtRtiGuYXwI0U_VyR4ZuUIqOMMNFgb8YEI5AZ2S1veRFunkEyHmeQkoJGBPfubLQN33EWns3O1AcY4AIE2x7tXqR0JNxciOuHvw9XW1qS5DxIQcCd9omrAIgifBxcQM7RFnF0eO5TGQUiMm6c-Dyu_d1HuH74RwN9fWIwk7dkAUGfu7vmioAl3ZbsHoY_zEz81bDUnXn_zVJm4dc0OhnJb0NwlRxUN1QWCM9ODHnyB8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
هوادار جذاب تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/98158" target="_blank">📅 15:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98157">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1aaf3f086.mp4?token=paQLqk99jWa4NMI9yxXMdGn1nQybULc4D_t_GaufyNL9_4VqLkrqvtxAaz7dJfKcN_-2qR1d9hGyfhrV9Cj__EF4jJsUUIawYA9VXs2o1hrzGFM6nAe7soB7NIn0dZEfCT6JPcczTcHVXcWpIEORYCmeiaQ9rieZEkLDYA0BlxaK0FMj35pM3kLIzPGkLf2BApN-HwrpFpImRJoRDUfrNBatXrSyNVp2yw5Q5QMh1pULW-3D0-ImK6yf8C6bqYCeNGs2dmiYkdf3AmG_olVXxZUaAbGChl8c7Z9JttskkrwoXQLN4K_QmGy0OKkqGOPwvwYtqCgdR0fJpCxmYsh_4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1aaf3f086.mp4?token=paQLqk99jWa4NMI9yxXMdGn1nQybULc4D_t_GaufyNL9_4VqLkrqvtxAaz7dJfKcN_-2qR1d9hGyfhrV9Cj__EF4jJsUUIawYA9VXs2o1hrzGFM6nAe7soB7NIn0dZEfCT6JPcczTcHVXcWpIEORYCmeiaQ9rieZEkLDYA0BlxaK0FMj35pM3kLIzPGkLf2BApN-HwrpFpImRJoRDUfrNBatXrSyNVp2yw5Q5QMh1pULW-3D0-ImK6yf8C6bqYCeNGs2dmiYkdf3AmG_olVXxZUaAbGChl8c7Z9JttskkrwoXQLN4K_QmGy0OKkqGOPwvwYtqCgdR0fJpCxmYsh_4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فتح‌الله‌زاده اومده برنامه ابوطالب جلوش یه لیوان آب گذاشتن و بقیه ماجرا
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/98157" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98156">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kInOvKX5cOK_9UzaB6BoH1qiHOVCdYsGlU3oiU4GfziEnpb7mX1114BPHnvKvTTPpglN-_legGWAf37NIkWLquBXnTDSt-EWFSahu0h722LZif9latWcR86sLCYIjMRzyktYT9RSm_ObuhA_1wWaSOreH7P0kaIRwiqbezHUKvmpRwtG2S-Sk-ptsWnIL4x4JMBb7njimoadvw-vxbFuTmdSyZjI1TU6EfKCpLvG1v-eJoyyfCH2xV9WY6Lj0rRFEEPhALdYdHXSdIs7ISqQ-Bxw7O4U_ONXXsOJR15VG6inmzwbudb14gs-E4U-_E4vkseupamN5669EqLow4siPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
حمزه عبدالکریم بازیکن مصر در پاسخ به سوالی درباره تحقق رویای دیدار با مسی :
🔹
ما با آرژانتین بازی میکنیم، نه مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/98156" target="_blank">📅 14:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98155">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a433836c4.mp4?token=jO9WJDxQIAKlCDgXOBzZypbjIwSKq0HSW0ihMSmJc7qrCLWz5OmiibyrPmzNX7uOYkRMMucwwlce9_v4Wst2Coz6JFGQ-9NrgUUBBP4iLyInYWPWrztUgMUO1p_Q21r7uMCHdKcilSn0Tk_CwbswypAKHMTiCziqLCyQ9vjS2smCcBpPb0g4RVc7e0jkhfUvLtB3_e8sbF99DzuA14n1PPGhZBhFYQSpk_W-COy9dQ0fSrouIfuE3BSsIEVkysZvrMoWNDY0LSOp782JRWPVcGFIqGxd4DR9DiRss6njRv2L8XG-sn4uacNxSEsxnHfo5fiTaUWGOtqWk-7SOSDy-JelMwDhKSImU4qOd95sIzedNvpJbbG4md6e5ePIHNC05pxwQ6UEHcXmanoY7dzCVV2twvvTn0Vz29PUgYImg_w2fEYmcAFNTdohCvaqBOTT9hOlgZLCpA96qQkAiFPnI_QLHAfWnrxaWRkdEHAS6PiiJCSPDdODsKHF7L4MDQbwBdSBGyA5ni01ZxeGAHK4UFNV06sh8XUFjWU-Qvviu2BHjj7Q8ZdjgpVrENMiwg0G7U821jXLYqmKOPbKnzJwYMU8RTYlzOxR5MtmBE9MCETjttgLDWa3Uugd1pSlh5DYIGpTkHq2beavgSsp60JV0MGvZPcOGdbvbWJGL1LlTTs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a433836c4.mp4?token=jO9WJDxQIAKlCDgXOBzZypbjIwSKq0HSW0ihMSmJc7qrCLWz5OmiibyrPmzNX7uOYkRMMucwwlce9_v4Wst2Coz6JFGQ-9NrgUUBBP4iLyInYWPWrztUgMUO1p_Q21r7uMCHdKcilSn0Tk_CwbswypAKHMTiCziqLCyQ9vjS2smCcBpPb0g4RVc7e0jkhfUvLtB3_e8sbF99DzuA14n1PPGhZBhFYQSpk_W-COy9dQ0fSrouIfuE3BSsIEVkysZvrMoWNDY0LSOp782JRWPVcGFIqGxd4DR9DiRss6njRv2L8XG-sn4uacNxSEsxnHfo5fiTaUWGOtqWk-7SOSDy-JelMwDhKSImU4qOd95sIzedNvpJbbG4md6e5ePIHNC05pxwQ6UEHcXmanoY7dzCVV2twvvTn0Vz29PUgYImg_w2fEYmcAFNTdohCvaqBOTT9hOlgZLCpA96qQkAiFPnI_QLHAfWnrxaWRkdEHAS6PiiJCSPDdODsKHF7L4MDQbwBdSBGyA5ni01ZxeGAHK4UFNV06sh8XUFjWU-Qvviu2BHjj7Q8ZdjgpVrENMiwg0G7U821jXLYqmKOPbKnzJwYMU8RTYlzOxR5MtmBE9MCETjttgLDWa3Uugd1pSlh5DYIGpTkHq2beavgSsp60JV0MGvZPcOGdbvbWJGL1LlTTs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
دل‌هارو ببریم به سمت بازی Pes2013
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/98155" target="_blank">📅 14:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98154">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">💥
▶️
عملکرد لامین‌یامال مقابل اتریش که هرکاری دلش خواست انجام داد بجز گلزنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/98154" target="_blank">📅 14:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98153">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2xS7AU2rC2I0qRkgK0EgwozgV9PS4Ep220YucQ4Co0kfKuhqKLp1w3cJ0jhUF5kB8FjY11qw4-LxR09Xmvw96OoOQTitSXAg22ii6OalKa2Ll-LjkspZp3O1cB6Fs5F09ebDvdea3lyK1PVH87ehdAey6I8jXnnyOmR7zOW0-YD3WolTHBlhNXDheF24uX8uEeedMEsF1lmsYLPZth1vAvOl97em0OrKXBVZtiSBQiVEQWnJDAptAfXM7CjL-83rar-yDIFcwYyCseGbbaQANFJpXUe3YP03eOH_F0Syqtrlg8NWtBo4wOeTNRL5RAEvIPLLv6E4WcKsvwJ9K3y6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بازیکنانی که تا به امروز بیشترین موقعیت را در جام جهانی خلق کرده اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/98153" target="_blank">📅 14:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98152">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGu2_WJ99jG3CFJUpI4yMChKNGSEe8WjEoxmUgamVBZijSXbc8ZnkeFSwXHUbubDf2zzBEURI4VlKz0T3dPfgyuv7Aksw01PCoaS_3hbv6ycbrFj5LkQgdzDpCc9Isqdcbto3fWBB8JcTv2TLev564HiCYDtXevFMjrNOd6daWtJNGR50pyeb1dRddXJVWE1w9m8QS7a4akbSitqlvikSkY1oS8Cw4z0MI2xQF7y_dMJ-hgvX4ysREPjWEFlZBhnEpruutRj3iVJ2UWWkWAWlf_VsWs-USkfreGVlHE_0br9cpJ-DIEbQMckKtOi5wA01eJLCyiUbYesXWIxf7OsWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب مرحله یک شانزدهم نهایی جام‌جهانی از نگاه سوفا اسکور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/98152" target="_blank">📅 14:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98151">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc006f9bf2.mp4?token=VorenHKBl6hvjA5Jizet2wUaORqiiZ7LgXeptbK-0knyih7i0iDKC8WT-z4naJQv6pF9GdU7zBGbnwa6ynitmgmRPLUFT5sLIsehARraWFLOphmXlEH_0GvY5iUYR1MBFVbyBa8yii6o9MzEuxWpgwVan3-HiSOsJSw84YmzZk-VAs9yVQBfaXN6Q7oKVipGi0TT-1lLr-H-9-yc5OHLjbYhp0SnK9Q4m4ylQZTXZEFepWlF8HF5IcyfDfXzBH9FAJT1rCz4lXsC0r6Iqblwcnm77SOf34uHID_adEJNr0kJknZs-pMOf1C5Kh12Thxrmm0PnygIVZ4EkWA8mDKTRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc006f9bf2.mp4?token=VorenHKBl6hvjA5Jizet2wUaORqiiZ7LgXeptbK-0knyih7i0iDKC8WT-z4naJQv6pF9GdU7zBGbnwa6ynitmgmRPLUFT5sLIsehARraWFLOphmXlEH_0GvY5iUYR1MBFVbyBa8yii6o9MzEuxWpgwVan3-HiSOsJSw84YmzZk-VAs9yVQBfaXN6Q7oKVipGi0TT-1lLr-H-9-yc5OHLjbYhp0SnK9Q4m4ylQZTXZEFepWlF8HF5IcyfDfXzBH9FAJT1rCz4lXsC0r6Iqblwcnm77SOf34uHID_adEJNr0kJknZs-pMOf1C5Kh12Thxrmm0PnygIVZ4EkWA8mDKTRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهرداد صدیقیان از فوتبال دیدن فقط زن و دختر بازیکنارو دنبال میکنه
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/98151" target="_blank">📅 14:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98150">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6NDc7beKzSKPLwPlXG3g7urGJb6iSz9KgXvCGWJJV_DiWOpMQ_r9hnWBMyJ0avxNNZ-C8VAKwukEfhIFsWEKCiuGBazPX0lu-sJ8NMSaSNAPVVPE34AL60IlcxvGGrGCGhOqFWdwmnkA66AQIqx2zzdWNftSKeq_pNHX5509iCo8j_a5hJidSGfT7_wW-XGwWFs43kP8k-XaFnjOy_rQcfC1zLbl-dIdmcfIZMIDq29FRFAAYcQN-xHIibcbg-7OlKt9TQ9Pr9pYp6U7LiwxkodyoPoXkX_71Of2pAkcKjWkGTZb3CHnIYk1XdBoQ3PrYCqTODsvLksvJI7t8ue8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
جیانی اینفانتینو:
‏"در این جام جهانی، مسی با یک سبک فوق‌العاده و شگفت‌انگیز بازی می‌کند. ما او را به خوبی می‌شناسیم، او یک بازیکن نابغه است و همیشه خوشحال می‌شویم که او و سایر ستارگان را در زمین مسابقه ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/98150" target="_blank">📅 13:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98149">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/618fa5af23.mp4?token=kFI203u6FgN1oXY8CqYuP42c1yhGhCKC1-uXMUwVGi0MkYBINwrPghzIuPfjivKzDTey-uPY0yJlg-xE11kq2OFpGgvLdlUe9dtnzOoIzoartbfAul3URzGW06vWFBnUc5tTdVVkS4pqSXmQRaWlxggnADF4TKQPeR_nemvohXUEi8ppLvqV8iyLo-v2bYCQkuJkVY585Kh9epeE-5xNqWswZJSxrOVQLLAiXJv9bkAuBFQx6JX428HnjEon833gxqlfqv62_HnAoaUC4sG_BXni2qT-hIWeMykcj8yJwZJvbokBsXNgFgETzGKlGx8EsxvVANOvq86UmqQRFRGP8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/618fa5af23.mp4?token=kFI203u6FgN1oXY8CqYuP42c1yhGhCKC1-uXMUwVGi0MkYBINwrPghzIuPfjivKzDTey-uPY0yJlg-xE11kq2OFpGgvLdlUe9dtnzOoIzoartbfAul3URzGW06vWFBnUc5tTdVVkS4pqSXmQRaWlxggnADF4TKQPeR_nemvohXUEi8ppLvqV8iyLo-v2bYCQkuJkVY585Kh9epeE-5xNqWswZJSxrOVQLLAiXJv9bkAuBFQx6JX428HnjEon833gxqlfqv62_HnAoaUC4sG_BXni2qT-hIWeMykcj8yJwZJvbokBsXNgFgETzGKlGx8EsxvVANOvq86UmqQRFRGP8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇨🇻
ووزینیا دروازبان کیپ ورد پس از درخشش مجدد برای کشورش مقابل آرژانتین:
"تقابل تک‌به‌تک با هر بازیکنی همیشه سخته، به‌خصوص با بازیکنی مثل مسی که فوق‌العاده خونسرده و قشنگ می‌دونه چطور فضاهای خالی رو پیدا کنه. برای همین مجبور بودم خودم رو آروم نگه دارم و تا آخرین ثانیه ممکن مقاومت کنم؛ خوشبختانه موفق شدم توپش رو مهار کنم.
بازی کردن مقابل مسی یا هر کدوم از بازیکنای آرژانتین همیشه خیلی سخته چون اونا بازیکنای تراز اول جهانی هستن. اما این رو هم دلم می‌خواد بگم که هم‌تیمی‌های من هم لیاقت این رو دارن که توی بزرگ‌ترین و بهترین لیگ‌های دنیا بازی کنن."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/98149" target="_blank">📅 13:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98148">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f3e951975.mp4?token=Y1VyQEDAT7rteTVk0sA9p1NoEEI0_MC4gqhE3v9PPQ0E4_ywBQmTvxZT4T3NgMMnPjjMlC079nXQDSn0ZpcdNLRM-Nyzs1wZaIUbqZuqGAxA2JZT2m5TyCvn-0J7aBaUZ0ZXRP0oc5x0tg2yKi1-T8234oMZFOqMb_PPlpsCcyrc0ygqp0PXFOC7FgsQDUthckz4NzW0oKGbKsl55ns_10CFcsn80wYsuF2BF34XnDJ4d_f8HPekn62e0EvIDC2B1PvR-zW5nnkb9cQky5t0vGv4Rl-ikzrxa0y1315QeD-m0s3y4GuhsQDuxw7TjEju793GnqUM-mQ98k39spPvFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f3e951975.mp4?token=Y1VyQEDAT7rteTVk0sA9p1NoEEI0_MC4gqhE3v9PPQ0E4_ywBQmTvxZT4T3NgMMnPjjMlC079nXQDSn0ZpcdNLRM-Nyzs1wZaIUbqZuqGAxA2JZT2m5TyCvn-0J7aBaUZ0ZXRP0oc5x0tg2yKi1-T8234oMZFOqMb_PPlpsCcyrc0ygqp0PXFOC7FgsQDUthckz4NzW0oKGbKsl55ns_10CFcsn80wYsuF2BF34XnDJ4d_f8HPekn62e0EvIDC2B1PvR-zW5nnkb9cQky5t0vGv4Rl-ikzrxa0y1315QeD-m0s3y4GuhsQDuxw7TjEju793GnqUM-mQ98k39spPvFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی
🇵🇹
پرتغال
🆚
اسپانیا
🇪🇸
از این نما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/98148" target="_blank">📅 13:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98147">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRvyu0SNEmwM4QTeOSRyMgMjtkXcI5XpvtDixEePRR-3TcQY9jAtFXRlhQlfRK9vKzS3mHdajvz-HJoEAu_boFNQuCjVZnpNGRi78euXM7Kx4KiZQVPbqjLLii8DjQUVcY0_m1GDHvHwE5rQlFUxdSj5GWoYjfYbFLk-3MVSK0Y9NFEIw0WEe14g2GLAYRK8hfafBAxVLvrYimp5wzJDj2uvnlVXf7g7EKtzaVX4_XFxhIPhtXeuoRReKNahrwTqCGueGu26AW2w-JiljDt-5RM2Iwq7IbwG55ab7ytM9_36CwB34OaoW5hKXtNSaeI3MS0xAscPhXEZD_DgKBLx6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
متن خبر: خداداد عزیزی دقایقی‌پیش مدعی منتفی شدن حضور اسکوچیچ در پرسپولیس شد
✔️
❗️
🤩
واقعیت در پرسپولیس: جنگ قدرت شدیدا در باشگاه شدت گرفته و چند نفر اصلی بدنبال فرو کردن گزینه‌های خودشون به نیمکت سرخپوشان هستند. صحبت‌های خداداد عزیزی هم با دستور زنوزی رخ…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/98147" target="_blank">📅 13:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98146">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f532fa68ef.mp4?token=oO-cyzcuKXEJQjQ2AL-xDFX0MaYa_zWGdzO-VWt_xTkoyE_vrU1TlJDbH89zqect0mBBUOMBhBFiw8CVv_cKk-1K5xWn1oOqtxZ67IxrNDuB7IbZ5quafIthBYfzzd7Oq1wf8MMLbzrcDLNVNCNNhD1NC30DHQNKx62_2SajsMfC8AMTlC7vSM8Tm979Zmo5nsnepEY3kzoYFxlA_EpEhTJBC9CdD0QzXBLRG5AEDgZwdxl536N9GmzKOqgwcwQ8dxNQy4RGBPDoGbHxQpRYSY4LuzOqwmz39JABm6xffuSYAGAXoT56IWjq6gnyqFSM-XTJ8G3WsMp37e1CICrZ_2UFIYpvD7GpF3GSxynUHyqIVbr5xFcqFnmD0HqlY62TsxVU7T1EI1Ebm4VIwCd-YJU72tJd0FcZ3E6kbSYVcpYivEx7jl9VVwdsJLKOjbXIMKoU4eVxAlIwgGZYaH1rPFqGbtdgB25-BF2WOh9WKQskp0Fu7T7G45QlV0YyHpcGcAqBfYHdn1JEkITcmpYJxh_NL6j0kSXH5tQTfStGxnQrUkqU8U1Vz2rfN0D0Qhsxi0nTTNhcyM0DWoiD5t_3ieJvwoT6gB6sw4r_C9jyfdEBr6MQXgv2jx-L-GYxSmpFSvXbRhci691NjlrLlvrgHcPtgK2Inj_dihHhh-7-au0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f532fa68ef.mp4?token=oO-cyzcuKXEJQjQ2AL-xDFX0MaYa_zWGdzO-VWt_xTkoyE_vrU1TlJDbH89zqect0mBBUOMBhBFiw8CVv_cKk-1K5xWn1oOqtxZ67IxrNDuB7IbZ5quafIthBYfzzd7Oq1wf8MMLbzrcDLNVNCNNhD1NC30DHQNKx62_2SajsMfC8AMTlC7vSM8Tm979Zmo5nsnepEY3kzoYFxlA_EpEhTJBC9CdD0QzXBLRG5AEDgZwdxl536N9GmzKOqgwcwQ8dxNQy4RGBPDoGbHxQpRYSY4LuzOqwmz39JABm6xffuSYAGAXoT56IWjq6gnyqFSM-XTJ8G3WsMp37e1CICrZ_2UFIYpvD7GpF3GSxynUHyqIVbr5xFcqFnmD0HqlY62TsxVU7T1EI1Ebm4VIwCd-YJU72tJd0FcZ3E6kbSYVcpYivEx7jl9VVwdsJLKOjbXIMKoU4eVxAlIwgGZYaH1rPFqGbtdgB25-BF2WOh9WKQskp0Fu7T7G45QlV0YyHpcGcAqBfYHdn1JEkITcmpYJxh_NL6j0kSXH5tQTfStGxnQrUkqU8U1Vz2rfN0D0Qhsxi0nTTNhcyM0DWoiD5t_3ieJvwoT6gB6sw4r_C9jyfdEBr6MQXgv2jx-L-GYxSmpFSvXbRhci691NjlrLlvrgHcPtgK2Inj_dihHhh-7-au0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇹
فرنوش جعفری گزارشگر دختر ایرانی: رونالدو قبل پنالتی گفت بسم‌الله!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/98146" target="_blank">📅 13:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98145">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCYE3GlyQ12hm_h5oovy0PVwNL7GJ8LLgzAZfs8K8sS-ARJbo6tQZBGFdchyEDaCfJero0vBFe49UoBKBBqlIQixdtkcTQKTXX7eQE9JMtOdFAYXfbTFXo1_SojbE3y7YWonQyj7Z_9JiKbFZwcHqUtsu-rlPsCZTXTJt08G-IFYdANJe3HgwF9AiA1XTw0yk7MBwtADP60aG7e66a-3BVsfUCeWXe1avgU25MUX72ng24v3DY0xGLRtWxjCKdyvOXoJOJ95cS9_4X3ssYoO37fUeLM5DbRnGAI1LRPFX9p0DtCbGJEiEQr-ld79KYrNHL150lliXYtAKTJRNfG6Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇫🇷
#
فوووووری
؛ شوامنی بدلیل مشکلات عضلانی در بازی امشب با پاراگوئه غایب خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/98145" target="_blank">📅 12:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98144">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1560d3443.mp4?token=fxzIMSbbNYBMcIqPuu_lRk-qRT6eTYMG9AbFre7WR15v9g0rjUDUdaaCQgyFMd_7kjqju_6N29LopfwPbRjRBwldA55MZjq7_xy4yoYZi96JIeK0lVXRyHKi9EcLKq2cQJenyRBTVj7M8m0h42S5NKcD4DkpKPmf9losEyIFZg71_1mwXNW2h_tUimtoUZ6FVCm-8UFX_NsvpMsAoqHOAfL_EiUuKD8rH6o5uMs-GH9J9ppC6r1ukrD2DMN-NtdoAfr9kTgHVL3jVSDFLTZDubQ492t2Ol9VG79Fv0h-na_30jYZ_LUVWZ-Oy71gSiln7rdMP5JrZr6iG3Y-_sYaLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1560d3443.mp4?token=fxzIMSbbNYBMcIqPuu_lRk-qRT6eTYMG9AbFre7WR15v9g0rjUDUdaaCQgyFMd_7kjqju_6N29LopfwPbRjRBwldA55MZjq7_xy4yoYZi96JIeK0lVXRyHKi9EcLKq2cQJenyRBTVj7M8m0h42S5NKcD4DkpKPmf9losEyIFZg71_1mwXNW2h_tUimtoUZ6FVCm-8UFX_NsvpMsAoqHOAfL_EiUuKD8rH6o5uMs-GH9J9ppC6r1ukrD2DMN-NtdoAfr9kTgHVL3jVSDFLTZDubQ492t2Ol9VG79Fv0h-na_30jYZ_LUVWZ-Oy71gSiln7rdMP5JrZr6iG3Y-_sYaLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
👀
دیس هادی حجازی‌فر به حسین‌میثاقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/98144" target="_blank">📅 12:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98143">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e644ac1b7.mp4?token=pNZPKNyNeWskfhkfX9bG9rVjNmYKpd_CEm1S714WcH5il-QDkT8LaIB_COuM0V9eks1c9H4cz3FkcR3m8XKxDs_LgtwMKurJYUWYAbpjUgXISkUGB0LHhd4hWd7XDV1aB3-IstYTNcxXEufLSBe74AH9ekHB1Q4-lnKxqly4BWyWmFpIoMoYpNIqLdcTWteMe9tPw73xqsIq12S6StIdd4m18lYe1GFel2umV_kjIK6m3uv_zsnjFm9B0eGEtoSEkgObGNp3_Myrh9BXqDd4-6IImRA9LKScOXY97jcNgUlJMCDxZIQlPjenPPnWY986y86yujTTta-wc2kzFQni2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e644ac1b7.mp4?token=pNZPKNyNeWskfhkfX9bG9rVjNmYKpd_CEm1S714WcH5il-QDkT8LaIB_COuM0V9eks1c9H4cz3FkcR3m8XKxDs_LgtwMKurJYUWYAbpjUgXISkUGB0LHhd4hWd7XDV1aB3-IstYTNcxXEufLSBe74AH9ekHB1Q4-lnKxqly4BWyWmFpIoMoYpNIqLdcTWteMe9tPw73xqsIq12S6StIdd4m18lYe1GFel2umV_kjIK6m3uv_zsnjFm9B0eGEtoSEkgObGNp3_Myrh9BXqDd4-6IImRA9LKScOXY97jcNgUlJMCDxZIQlPjenPPnWY986y86yujTTta-wc2kzFQni2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇲🇽
رییس جمهور مکزیک: از مردم میخوام اگه جلو انگلیس بردیم، زیاد مشروبات الکلی نخورن
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/98143" target="_blank">📅 12:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98141">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32c0e1238c.mp4?token=UPNFTJikV6QduWXbamw7f-F69F5qWPPWNk4nFERpeD04T8OmY0phe9wVi2WbYqklSVlv4gN3ArzPiFCoofGPLbbx4ZWmII540R1WTFkUinhTCQJvblvx_wuTpmd_pSAGAzgLmu9kO4OrBzF5uwU5xrr8LF3fETi1ZV9MdJ8b4nHB-YiwXWKmuz1D8D7VUx-SK4Zke2HFFU_Bvg__Y1exnwT5DF39uMDaRhxAGZVOpDn92bAHWS3ISJWBk386rz4GHnIZjGTW7ipm6t-f5fXWkqFCoQrsvbFhf9QA_BVG3k3mBD_-Ono894Fbgp5WLTA41Qbx_MoOQENRxZTq6GIH3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32c0e1238c.mp4?token=UPNFTJikV6QduWXbamw7f-F69F5qWPPWNk4nFERpeD04T8OmY0phe9wVi2WbYqklSVlv4gN3ArzPiFCoofGPLbbx4ZWmII540R1WTFkUinhTCQJvblvx_wuTpmd_pSAGAzgLmu9kO4OrBzF5uwU5xrr8LF3fETi1ZV9MdJ8b4nHB-YiwXWKmuz1D8D7VUx-SK4Zke2HFFU_Bvg__Y1exnwT5DF39uMDaRhxAGZVOpDn92bAHWS3ISJWBk386rz4GHnIZjGTW7ipm6t-f5fXWkqFCoQrsvbFhf9QA_BVG3k3mBD_-Ono894Fbgp5WLTA41Qbx_MoOQENRxZTq6GIH3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇵🇹
رونالدو با ارسال ویدیویی به پسر بچه‌ی ونزوئلایی که از زلزله جان سالم بدر برد ولی تمام خانوادش بعلاوه یه پاشو از دست داد، از اون دعوت کرد که یکی از بازیاشو از نزدیک ببینه اون پسر هم توی بیمارستان این کلیپ رو دید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/98141" target="_blank">📅 12:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98140">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fe8d2196b.mp4?token=Bkd8NRPdKaYvNbQeKRtaPoQWuyR7jf7Qievqj3-CpE-kUEweoY7v3op9rTENHyJsrVn2jHAkXotzYEDSojETfQJ4GAIOC82sCgI71Dm6QCx9_UxMkD_YepId3tjYAw7lJAYMEFn-9aMOolxP_5LY6QK1yVCcIMctVXxCEon7JVERP0xzCL3Su83curBbRdaJMIG6sdEDz-QKeFPQtNoHuyGkcu2O_8mvKnh41icPV4vXTA0X56u3oXAJkr5yo8EKhqJuB2CPjt_IRhRoy7pzVrKQ1C78t9XMI4E0Jh0rwEwTIva9G-1Twf6QZxUKQeLGwLYbs4NyuyPtmtWy2x6gbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fe8d2196b.mp4?token=Bkd8NRPdKaYvNbQeKRtaPoQWuyR7jf7Qievqj3-CpE-kUEweoY7v3op9rTENHyJsrVn2jHAkXotzYEDSojETfQJ4GAIOC82sCgI71Dm6QCx9_UxMkD_YepId3tjYAw7lJAYMEFn-9aMOolxP_5LY6QK1yVCcIMctVXxCEon7JVERP0xzCL3Su83curBbRdaJMIG6sdEDz-QKeFPQtNoHuyGkcu2O_8mvKnh41icPV4vXTA0X56u3oXAJkr5yo8EKhqJuB2CPjt_IRhRoy7pzVrKQ1C78t9XMI4E0Jh0rwEwTIva9G-1Twf6QZxUKQeLGwLYbs4NyuyPtmtWy2x6gbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
تکرار ادعاهای کسشر فتح الله زاده در گفتگو گو با ابوطالب حسینی: اگر مدیرعامل بودم مسی را می‌آوردم…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/98140" target="_blank">📅 12:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98138">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l8_twwpU2MnKvjQz8ceOWeMJmY5LKelhs6ioNkcAaR3H-SWDOBUdsloI2ioXnqLZosDejmM5wKkqgaKlkzF-zhb0a37-BfxD1nxv5uEifQcFlkVrvCq_PzbPwIIWWa4CLPjMDGypwgbgcyE32NMNIiuiHvLu6PU8IszdbIe94bnTEXZ50TaTnEBbr52nBlYMorIVIqTN_rUeRy4cwD5CNKeBDgk8uIP43EAgBZiqUnn81F7bf2MkKrv6TC21GtP8WK3YEcbHSdl_f6N8e_RCupzaO9Q-bsd5dAat7ld5GWEnt3876LNb_Vs6Ci0vNvRH48tlE1gpj6j8dGVlVHfWdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RTO0UkvlrREVxN5TJgDq9vN6NiNd1lfCC--dNdRtIf_V63O2CCkacZBPxcZhiYyR9ahsHQuCjqG-qBOPoa8psmlIZ2H-pOopeTCEwx7BQRU5nVfIQ_pDl_HUgsTjNtSuTnt3NdMnOmgL6NOOMCOD67gFYWLyzje_SLJeaP7LcC9oFn5TKG8Jff-agwpHW5f3RXFw2DhxJA6cl_1kXJx32U3zUKkZELie7Z1KO0637Y4gPz-VUrFCPKw1uUdn_euFSz6Z_4sA9sOohFaKU0hzjec_NN05f8-pL7jBJhjDiCIOvOkewVOx-kfU1qxLD6t0zzDe3eacYv601_IFqWsdmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
‼️
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هتل "انگلیس" در مکزیکو سیتی، به دلیل نگرانی از احتمال ایجاد مزاحمت و اخلال در کار تیم توسط هواداران مکزیکی قبل از بازی، با تدابیر امنیتی شدید و یک "حلقه فولادی" محافظت می‌شود. نیروهای پلیس، واحدهای ضد شورش، موانع ترافیکی و گشت‌های یگان‌های ویژه ارتش در اطراف هتل مستقر شده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/98138" target="_blank">📅 11:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98137">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7c8cb22e4.mp4?token=qrGz-HF5CyilhW_-YeGAxl23zhk9l6n58_xDXm6Wwkdf3Z75nBy3bLVFuhb50J5v7svc78LRUMNYdjPLI3zUKNS4Uy8MNgnOW2t5jgqMXOIL19L1tK2_iZ7UAOePasEVAuhvKk_9he5pfVk3NOe6Xbr_HRNlJ0jINT_dyohkT3oBH-X5rsPJr8B9YPi2wYdkxHiVpTs51tw2wzttPtgo5Tx0apXshfZEUbNKkkUtqb_3ztOyYIKd_5hfGo79HLTxLuIeq-1ujHZ1WPu8m9w8aDbZer6Z8OBVlbizwywRsILi_NQYT3xa3NkUrbV24zbGpm7yZokrh48q1vlaIVm-tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7c8cb22e4.mp4?token=qrGz-HF5CyilhW_-YeGAxl23zhk9l6n58_xDXm6Wwkdf3Z75nBy3bLVFuhb50J5v7svc78LRUMNYdjPLI3zUKNS4Uy8MNgnOW2t5jgqMXOIL19L1tK2_iZ7UAOePasEVAuhvKk_9he5pfVk3NOe6Xbr_HRNlJ0jINT_dyohkT3oBH-X5rsPJr8B9YPi2wYdkxHiVpTs51tw2wzttPtgo5Tx0apXshfZEUbNKkkUtqb_3ztOyYIKd_5hfGo79HLTxLuIeq-1ujHZ1WPu8m9w8aDbZer6Z8OBVlbizwywRsILi_NQYT3xa3NkUrbV24zbGpm7yZokrh48q1vlaIVm-tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
😎
بهترین گل‌ فعلی جام‌جهانی از این زاویه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/98137" target="_blank">📅 11:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98136">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/384560aaa9.mp4?token=mtSuoqkYZz4gL--cZjggFAMZoDUO4tKkvjGXP-ean-F29oq7X55VjW4sgI0MRSxhV9nAs-TJfvyPd4wQHHFCGYuEeB1A4QpD9GrOYoUSFGSiyNo7VmqwEDYJH5r0puzNAD6QAih1yrKQhvtQ8-_Ap5lMG6fJB_gy67nXQWnK9t9YD0aNtrNG1O-BeSc8EisBowqurPz0hCMsl3UGQr9_qwXcD45NT1aJOE9iyaY1y4j-SUUXMOGHJzN2mW6ughSG4zCmtAa-wEzO_xxStXQLFSq6gEHxIqyZBa4Dr59F15HruE8trIpT_MyeH3GrbKnhPYjnJHnLOcRGdNtdSksREQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/384560aaa9.mp4?token=mtSuoqkYZz4gL--cZjggFAMZoDUO4tKkvjGXP-ean-F29oq7X55VjW4sgI0MRSxhV9nAs-TJfvyPd4wQHHFCGYuEeB1A4QpD9GrOYoUSFGSiyNo7VmqwEDYJH5r0puzNAD6QAih1yrKQhvtQ8-_Ap5lMG6fJB_gy67nXQWnK9t9YD0aNtrNG1O-BeSc8EisBowqurPz0hCMsl3UGQr9_qwXcD45NT1aJOE9iyaY1y4j-SUUXMOGHJzN2mW6ughSG4zCmtAa-wEzO_xxStXQLFSq6gEHxIqyZBa4Dr59F15HruE8trIpT_MyeH3GrbKnhPYjnJHnLOcRGdNtdSksREQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیپ ورد سرانجام تسلیم شد.
💔
آرژانتین به یک هشتم نهایی رسید.
🔥
🇦🇷
😎
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/98136" target="_blank">📅 11:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98135">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34ed4cf233.mp4?token=BZjofSApfRdkm-K-7YXcnisSz01Fk6MgZucwWdGBTDsNXfLwrr-FURGKPeDm67Gsi50dA0CDzsR5AIUpHOy582QXw8sbod3RP05LMKHYSOudmQFMx2-CIew84MMtV5MrxLkWSJ0KX46eeeQmP4fVqkMxG5PHrGC2FxGpgoIX6m1Uh7k3q3w8RFa0L-hIs37Pj9ehqN8Cft9fV02pYrjK046NGxdqryl63ozWO7gwyS6rJJ7krisuZG5fzc2BhGMFrds-N93jOQzzLDQTmDJX6PzLG_qz_pEqCtt6uOZDN32RPt_4F3qmcjxU68SacI1SgAaxeaVE37Waz_jhvpiQXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34ed4cf233.mp4?token=BZjofSApfRdkm-K-7YXcnisSz01Fk6MgZucwWdGBTDsNXfLwrr-FURGKPeDm67Gsi50dA0CDzsR5AIUpHOy582QXw8sbod3RP05LMKHYSOudmQFMx2-CIew84MMtV5MrxLkWSJ0KX46eeeQmP4fVqkMxG5PHrGC2FxGpgoIX6m1Uh7k3q3w8RFa0L-hIs37Pj9ehqN8Cft9fV02pYrjK046NGxdqryl63ozWO7gwyS6rJJ7krisuZG5fzc2BhGMFrds-N93jOQzzLDQTmDJX6PzLG_qz_pEqCtt6uOZDN32RPt_4F3qmcjxU68SacI1SgAaxeaVE37Waz_jhvpiQXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇨🇻
خلاصه‌بازی دیشب آرژانتین و کیپ‌ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/98135" target="_blank">📅 10:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98134">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257254cbc6.mp4?token=kvH--j2PC9t0E1ZbSrcwmJ5KAO6USzbzXTVoxwRW0iVh8y6u2B3RjCx0qPsXhkWcw-PZyzu6geGFifAzcvywsJHyuxkX3is4bCsLvWYOIxKIYUdHxOBBaWcIBPQbuDmlLBguvInsMRvU3AURY607BWduKVUh06qMdWXdhiXIAqaJhuN9t61bxmB2fjfR0clhNBKT59t-D01mNW579lwMR2MUan5wVXBRF322aeaEZl8DpCWKm_AFoQPFYxKrjz49sNmr86QfNxh85hq2GxeGiqmIYT1G2oK2phZ0zUjb7ACuVlFfLSI9Yyb_WgEGX2CP7fZhIcxnQSWQ_0cOU3jPbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257254cbc6.mp4?token=kvH--j2PC9t0E1ZbSrcwmJ5KAO6USzbzXTVoxwRW0iVh8y6u2B3RjCx0qPsXhkWcw-PZyzu6geGFifAzcvywsJHyuxkX3is4bCsLvWYOIxKIYUdHxOBBaWcIBPQbuDmlLBguvInsMRvU3AURY607BWduKVUh06qMdWXdhiXIAqaJhuN9t61bxmB2fjfR0clhNBKT59t-D01mNW579lwMR2MUan5wVXBRF322aeaEZl8DpCWKm_AFoQPFYxKrjz49sNmr86QfNxh85hq2GxeGiqmIYT1G2oK2phZ0zUjb7ACuVlFfLSI9Yyb_WgEGX2CP7fZhIcxnQSWQ_0cOU3jPbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
جدی‌جدی ۲۰ سال از این قاب خاطره‌انگیز گذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/98134" target="_blank">📅 10:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98133">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be274a4b56.mp4?token=uEgoKYHNtwgWTCGEBTTzLpXhmL56bRyxFkjy788gjEm9gJYafVhhe7AHEg4uGVtr9jWZx2Uq90RxtV5hxwvB9LQ43yAUiEEkhVA4Tg_FPOF295aBoqxj0OBYsoLIDrSzuIYyZm4aAJhmik_q_aC1cWv7bLDH5Jq9ADld238qYVywjzoIMvowNmpVM7OyjedqfTMFMuAPXGqqCDCf3oKdsHrnu3LUK-UUQZMFcOBDN9Gg0btE-2juT5-TWXEntB74m9e5dssCGVjlRpAB88QC7XUvfU4wrhTVvadBjF7BY5zsC_tBhS2rU68aiGbbbJijrWun0huAHBhGgUKB_US60Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be274a4b56.mp4?token=uEgoKYHNtwgWTCGEBTTzLpXhmL56bRyxFkjy788gjEm9gJYafVhhe7AHEg4uGVtr9jWZx2Uq90RxtV5hxwvB9LQ43yAUiEEkhVA4Tg_FPOF295aBoqxj0OBYsoLIDrSzuIYyZm4aAJhmik_q_aC1cWv7bLDH5Jq9ADld238qYVywjzoIMvowNmpVM7OyjedqfTMFMuAPXGqqCDCf3oKdsHrnu3LUK-UUQZMFcOBDN9Gg0btE-2juT5-TWXEntB74m9e5dssCGVjlRpAB88QC7XUvfU4wrhTVvadBjF7BY5zsC_tBhS2rU68aiGbbbJijrWun0huAHBhGgUKB_US60Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو مکزیک یه زن و شوهر دعواشون شده بعد بازی که اینجوری مرد بیچاره افتاده خایه‌مالی
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/98133" target="_blank">📅 10:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98132">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c85478b9cc.mp4?token=ebDBVVDixVvk88-8XuGrURZSgAc_jPuT_7wkLCVFt1TZrSuTxF0dsxXIbBMcRqqSn1h68U6NjHppOC0RzJidV7zGFqNQs2ZCx_YXLyfUVnmMkzJQJyrWyGYt0kklO_3gNujPAMfrILuiRDXRL1a9z-kGNVBQm1g_TBHmFddd6EoVp4rmYFDdhjxlJ5St5ZhJLDMYRTPT9FOJqETc0QD0V1ILRLt7zMmZEINcsrro6gwuFLnlW9RHw6g4R4oV5kWcv2YEa-t-mX_kug_lGzTE7tLB8lG6kx3W1IcDqv2qe5_gHVpQo3lZ5jFRSsVFB7QFnj0w_kmC1ireBT0217Cehw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c85478b9cc.mp4?token=ebDBVVDixVvk88-8XuGrURZSgAc_jPuT_7wkLCVFt1TZrSuTxF0dsxXIbBMcRqqSn1h68U6NjHppOC0RzJidV7zGFqNQs2ZCx_YXLyfUVnmMkzJQJyrWyGYt0kklO_3gNujPAMfrILuiRDXRL1a9z-kGNVBQm1g_TBHmFddd6EoVp4rmYFDdhjxlJ5St5ZhJLDMYRTPT9FOJqETc0QD0V1ILRLt7zMmZEINcsrro6gwuFLnlW9RHw6g4R4oV5kWcv2YEa-t-mX_kug_lGzTE7tLB8lG6kx3W1IcDqv2qe5_gHVpQo3lZ5jFRSsVFB7QFnj0w_kmC1ireBT0217Cehw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
ورژن فارسی آهنگ جام‌جهانی
😁
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/98132" target="_blank">📅 09:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98131">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbf09c69ac.mp4?token=ccS97BRulUQFTCHos0fehb48toKSJsuLi4PVXS3tDjQGBV7OE1Z_JqMqlQxsArViAOl2taSVSg8mOS2WBgz5dCZtQYbNEevkIdNzNjqiSOZ2wy8JIEZWTo2ree01NSHD_PY6Cn18wUx9feO19wrzsRLWzgufJBTpz72YWfchvg1MPiiw0kyIVpJiCT-TpI_5rUWLXdO2qGbKiOOrROPla7fJVMihcKYHsjFgi9z3Od2YVzeJugGyES4JLrEtWV5S6P3bo9p0J8F8DqcOQqylY28HhQUJ59muY7gaBs1k8XnlUZbBEOEW2sAVi_w8UPG29cNcESEP91wPvWQGbmgpww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbf09c69ac.mp4?token=ccS97BRulUQFTCHos0fehb48toKSJsuLi4PVXS3tDjQGBV7OE1Z_JqMqlQxsArViAOl2taSVSg8mOS2WBgz5dCZtQYbNEevkIdNzNjqiSOZ2wy8JIEZWTo2ree01NSHD_PY6Cn18wUx9feO19wrzsRLWzgufJBTpz72YWfchvg1MPiiw0kyIVpJiCT-TpI_5rUWLXdO2qGbKiOOrROPla7fJVMihcKYHsjFgi9z3Od2YVzeJugGyES4JLrEtWV5S6P3bo9p0J8F8DqcOQqylY28HhQUJ59muY7gaBs1k8XnlUZbBEOEW2sAVi_w8UPG29cNcESEP91wPvWQGbmgpww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
خلاصه بازی بعدی فرانسه و پاراگوئه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/98131" target="_blank">📅 09:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98130">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3536115386.mp4?token=XuC2jArNZdNQs8oVRKtjZfY3eRA5DWr_EJxS77X8ubAWnTkatfZ91fKEEdB8qsCeum6CAzWm-iVJOW_mgjx6uV4-kOSyQo2g9GY13O7QfjPVlQq46GdW28zaSsXVmyOj2Fxn4eI3ZzEXzcsugLBZgZK2o-ZAfUtVpz1_2heFDcaytjmq3FI16-IoEIaRGcDJ22xjY5x2sZYS_1KNLp1l9dKR1hQ_ZhXx4KBfBwtXcJ8z1_iv1oLHX_qERlFPjBAdDwsYwKbsidIZDGodFUl0PhnY2kPIzc9PprSoNl0D826OanGWU1R4xdXtIaqv8bFN-IiEwJVPEphj9xXO7lDdiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3536115386.mp4?token=XuC2jArNZdNQs8oVRKtjZfY3eRA5DWr_EJxS77X8ubAWnTkatfZ91fKEEdB8qsCeum6CAzWm-iVJOW_mgjx6uV4-kOSyQo2g9GY13O7QfjPVlQq46GdW28zaSsXVmyOj2Fxn4eI3ZzEXzcsugLBZgZK2o-ZAfUtVpz1_2heFDcaytjmq3FI16-IoEIaRGcDJ22xjY5x2sZYS_1KNLp1l9dKR1hQ_ZhXx4KBfBwtXcJ8z1_iv1oLHX_qERlFPjBAdDwsYwKbsidIZDGodFUl0PhnY2kPIzc9PprSoNl0D826OanGWU1R4xdXtIaqv8bFN-IiEwJVPEphj9xXO7lDdiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
اگه کیلیان امباپه در یک کشور دیگه به دنیا بیاد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/98130" target="_blank">📅 09:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98129">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyj2XTaJytA4PGwkosTyNsbL23_5dcNLkI6KXBs368nX-PjSe9hQLUVVy5ammFTY9UQdQZA9D0aM0DdqqTk-P23XfVGb7LZv8b16E7t432chUtgMKXTNHjcQXT0X8I6wvuNTa-t0P78SNyyEBzeNVyRwFNdyuBb8Gas-xYKq8Fz4uFpBKy7IWlONidVmwpvZXv1uHA_xDgF9Dij6l9blqsPSWjrcG10he6fia-j53HayWoKbOySttkfXT3ysFb3gIxKrY5s9hZnSFO8kthKciTH8iKDsEmvS80Ow5kkyLtxC-ESoK27vQbZqyb0t-ReN-L_gOfmM4EGst80KYGMaDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
ولی چه کیری خورد این بشر؛ تو چند ساعت هم تیم ملی کشورش از جام‌جهانی حذف شد هم جادو جنبلاش اشتباه در اومد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/98129" target="_blank">📅 08:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98127">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBGnFUEnKBF8NevvTqxuC-oAbW0ju-6Y9F3R1qmqcaFA24doJY83k76gnbgebeGQCPuAfJd4r8eYbaRSxJzoos_0iiC7nalMZXnnFPavYxoIWBT8qCHEubhQhnWXjnVMD9ptFH1K6YNExNpJTLq0B1l2mTdulmLyoIvoDBagk_PNFeaAKLnPOWct_tymd66jNvfJD01YL0caOzcOfqgI4LogbBIyZfZKYiyaYzpBNwFAyYlg-Nl7NqvcBsl0ZQmK3XxquawNapXUn3QcDSTubocaovpBfPkAq9SImlvE2PGLJNYltBSVOlZVdH6Hvm8GznDZJN4OR5Cs7mYMyh9MgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
برنامه مسابقات ⅛نهایی جام‌جهانی
🇨🇦
کانادا
🆚
مراکش
🇲🇦
🗓
شنبه ۱۳ تیر ساعت 20:30
🇫🇷
فرانسه
🆚
پاراگوئه
🇵🇾
🗓
يکشنبه
۱۴ تیر ساعت
00:30
🇳🇴
نروژ
🆚
برزیل
🇧🇷
🗓
يکشنبه
۱۴ تیر ساعت 23
:30
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
مکزیک
🇲🇽
🗓
دوشنبه
۱۵ تیر ساعت
03:30 بامداد
🇵🇹
پرتغال
🆚
اسپانیا
🇪🇸
🗓
دوشنبه 15 تیر ساعت 22
:30
🇧🇪
بلژیک
🆚
آمریکا
🇺🇸
🗓
سه‌شنبه 16 تیر ساعت 03:30
🇦🇷
آرژانتین
🆚
مصر
🇪🇬
🗓
سه‌شنبه 16 تیر ساعت 19
:30
🇨🇴
کلمبیا
🆚
سوئیس
🇨🇭
🗓
سه‌شنبه 16 تیر ساعت 23:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/Futball180TV/98127" target="_blank">📅 07:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98126">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZ6FwZsKcKl95b5gvh0kLcqMGF2MlWiS-UDCcdB0l2s3OyrDmP3ht4vBXZ_knvinxxfT7LHahURLiJGUVS8b5XU2aSMaS1BL7Ax8pOQoQIxo2xyLhcLBgcKaVB1R3BaodTnWZXUj11v_Ftixeopdh1LaTb97OVTkAG_ciGN4UhS3sLd97tOeBYp_-rYSoJnt-OTJYNjcVyqIh6bNq3T2rm7xoqyTdOcu6Ap_XuXg0eM8HojGaJd2kNQif3CjSVg9vpE9kC3cVB_Se2BQZTiq4UUjcovptFnL6deRNjtFGeLcJ7npM_oMT5OCLWW4XOJ8t4JdxPi8qDffUAzQzFDKwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفساید
❌</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/98126" target="_blank">📅 06:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98125">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کیروش کون سفید پشت هم داره از کون میاره</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/98125" target="_blank">📅 06:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98124">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آفساید
❌</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/98124" target="_blank">📅 06:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98123">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کلمبیا دومییییییییی</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/98123" target="_blank">📅 06:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98122">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">گلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/98122" target="_blank">📅 06:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98121">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VV3yQGj6PtVZjDWavWTWkKEbbcPGXtzu6vgEEebncAXzVM4MTwie0yt0QUY1OQm3hQpWnRBDmzpYMp9SQbpl8Eda1lSlBkjdNWQBo_sYMpipq9jZHFHhXgIhiTLIk2WKhs_R0tHFLBESqjx9BpPjZ2tuYNqWXzy1BrzYwP1_bEx_N0aIvvbHKRApr949ha-j1Yny0TPb58Rc-zX_yCR_RbK4HbejfnJEyFLZBhXVvGzm4CLa_q7i7a13yDyDrTvZPvLntaP6W8ZExmyjmUyUtkU0bcJB1ZQ1Eveaytnypq-chvWZBE8q4tkW69fHrRCweuzaLvqKFHXFIF3AF7YJ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار دریبل‌های موفق این بزرگوار: 2 از 2
🔹
نیمار: 0 دریبل موفق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/98121" target="_blank">📅 06:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98120">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FH6JPbB5mUXLGLG3hF_W96HKNEexMt7YdNdRuz-5_LyRzKyQJriYJsMjYD-m85k_R4IRK2M1yuQiyNil66DU3t0G1DQeGNkEyFEXSklsZIOQSZij6Q8Sb5oqMQBvJFp8Ijz7mdYM0Sro2oAQCcfLaGs-WMtzpGaUB6mHQTmJ6SGIK_RtOhnJGdaFLOm6iGmO42rl7OopXZkHkm-wrB9ooKu7_tIPmnBNLHyAiGXOwmixpyG8uoQmjruAQiBzNyRUFwMZ9s0ojx2xBEkrMq-Z_USQgBcS-L3ThzH1KnIta16IqYgoz4f1hzXM0qa6A5PONZBjZ6zF-zsU_kUxYAyODQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خامس مصدوم شد و بین دو نیمه تعویض شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/98120" target="_blank">📅 06:13 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
