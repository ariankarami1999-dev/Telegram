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
<img src="https://cdn5.telesco.pe/file/gNNVh2833jllNBAAH0LtGceiQcALpzka1QtHFEjyV2-vEJydTmamlHEyCM4cWvCzGzfPZROuz29eXgqDhzrBDAt_EeGVWUFJ8Za8-uBiExI8_oaAaS-DnjZaOIzumN-DCI8oi03mS2fymuFA_itAzKqDNGDXc_gqKbPNJ97heZ03tq4NhSQeSIbiTVDDfY5zFnA0rCiu1rxZWfvx4R58G-ntJbB02j5ev6sxDuG4UWiOAGa14KOcQ_U6cd5ywP5eugl11OuUwU-1Gou5u1SU1lMuids4XdZz5x1tlNWe9XIVGe72ueAJz3MotP7TDt1YyIjtK3o6D3hrIgu5Mr0OiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 531K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 15:50:01</div>
<hr>

<div class="tg-post" id="msg-92907">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/431d2a83b7.mp4?token=nfLgBW8Z8tRWnlIaqAAsYsFoyLeVn0GKpp-uYIHK58T9_PRItvNZxBENzMwpJoYF1xsyAIOtAX0d7vpxZgaYmpp4DTEp71hqXx2ULdN6c7CO3TvsZRat9pYVGcgwh4k5c2aHiiISlWQzWrLB1-aPsKZgXhEgixmQgi3siPSqFMLdlDfnQxhv4Jo_Mh9d9aFxN7Qxi5W6bkJvaq8z_hR6Tm9bLUUn5hw0UiFaCycZ2KWIkW6FgSG0-xmJvs6aFJVQvg6t0yZlbEK6k9Y4KixI5RVhh3mWU5gdwFoMiOxsQgT85ki-qcrpor2R86yw3Bl55tufzSsxs6_F_Drbs0a9ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/431d2a83b7.mp4?token=nfLgBW8Z8tRWnlIaqAAsYsFoyLeVn0GKpp-uYIHK58T9_PRItvNZxBENzMwpJoYF1xsyAIOtAX0d7vpxZgaYmpp4DTEp71hqXx2ULdN6c7CO3TvsZRat9pYVGcgwh4k5c2aHiiISlWQzWrLB1-aPsKZgXhEgixmQgi3siPSqFMLdlDfnQxhv4Jo_Mh9d9aFxN7Qxi5W6bkJvaq8z_hR6Tm9bLUUn5hw0UiFaCycZ2KWIkW6FgSG0-xmJvs6aFJVQvg6t0yZlbEK6k9Y4KixI5RVhh3mWU5gdwFoMiOxsQgT85ki-qcrpor2R86yw3Bl55tufzSsxs6_F_Drbs0a9ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ماموران امنیتی جام‌جهانی یه لول خاصن
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/Futball180TV/92907" target="_blank">📅 15:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92904">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r26IGMYJ0r9yB042oARR2C_el8-8pSmjrKFSKDM5VFjUXI50mu3T3M2ylZpvVUPBDQwOuu1tMVY0ch7htJODWpy7okOVslyIOdhbJWTfq1IeiYaAl5HBOwb3RDcKzPeNsAEzC7OM4Q061y0R609QKbvZx06ay9mN8A9eBk9DJIym8qrrgxI0ThBt5KIbWQN-mD7K4ZiZ7Py_afY5GAhmm3gEHJzh8s542KZPgGcpLDNRnAVHJxjxGg3WHZZan1XwuLv8S142mscJEfk_rf_sHVUqknzetS25YGfsFhQqlJl5KmbgE1Xmfbgo160fMdjCwBNh2u1yGrmNe61pSMvUZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AkPKD8Lj_OFz6GKr5qXNlSawMzyicvx05w9KBFja9ok1rrNiEfd0W6HSzYR1LqczIR2iDFPb-o2ILEQjsZ7W56y3d1UuwMOwjJ8nB2-x5tcMf58PUUjq9xfAv8-3u8Sw2yE9WiJqRNq6Tp4UpdaDS1WEArJ0nwq9JYOxttmKddIFWuhTzHtC3hTLUm2NPdBXqZmZh0K4Si_Gt889yv-OEuOPJlriKmlFVre_iSacZwUnfX04YrBcAYsoQrMrEYmCpg4gE_88qbbAvesz2gCLPsCFK2xFGDGUIvEOyh0TIYbR3ZRSeT7_i4DPZ7cYRdMa76GzL-dVVw3jvv5xg1uQyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oW40gRVayyRJSdZ4GOFBOU_fax1LNggcLAhiWHdZQFWYMH3T9xxpJPlipa2A2aCd8W5Swru0jZiXGT5uWs_PZaanfLQMZvQM5jMOZgINUABkzXYFD-JntVlqwXkrnsDbI76lTJosFmNMAPveB_mkFWyaH6KrLihdHhNa-in6kcpV3Fa19XfO5gix7ValKX6wBp89hBowR0dG7tmuHk6Oagqnb3YRHNY5NSKvupmOLTeAS0JG_1vhKUGgoIuYhHhMKvyUp5eqt6wPA3gxc3iW3nCQrbnVStFu7_dm1tamdusIBmF7UkWJWmX2apJMhqHNgtK9Flsw4A-pfDBkEFEwNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حضور بانو ویرجینیا در استادیوم بعد از آشتی با وینیسیوس
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/Futball180TV/92904" target="_blank">📅 15:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92903">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20da7b34f9.mp4?token=S-9-7RcqzCdEFDrRoCsa6L3S4hZ48se3IYPnKdLNmB01eo4J0bxzHCjEkKBymzbLgjWL-lQwEsStjoXPg9a5lLKbUfYIG1SKfqSyXYepYzlYgmjUWC24MHZX3E1HV4W79fSnQ2YfMbuX_DFoiu585fG5wwajUqSivlci-Pg7B87JfwC_Xh0xMSHQq8eTYGJFnJb1VSwWbqH2LPcqIHmtSeIj1dVJQBDb-gyncqR1m4jZdA9aexeJFVUtjzAy8OTSdeJ_0IWV0CJ_pJo28IzltiexAk2Dblitr83dWJzyN2fuvIsDOaITtSY2HT2nLK8KP4_gqvYPtmIjlJQdEHW-eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20da7b34f9.mp4?token=S-9-7RcqzCdEFDrRoCsa6L3S4hZ48se3IYPnKdLNmB01eo4J0bxzHCjEkKBymzbLgjWL-lQwEsStjoXPg9a5lLKbUfYIG1SKfqSyXYepYzlYgmjUWC24MHZX3E1HV4W79fSnQ2YfMbuX_DFoiu585fG5wwajUqSivlci-Pg7B87JfwC_Xh0xMSHQq8eTYGJFnJb1VSwWbqH2LPcqIHmtSeIj1dVJQBDb-gyncqR1m4jZdA9aexeJFVUtjzAy8OTSdeJ_0IWV0CJ_pJo28IzltiexAk2Dblitr83dWJzyN2fuvIsDOaITtSY2HT2nLK8KP4_gqvYPtmIjlJQdEHW-eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
توضیح پیرس مورگان از برتری مارادونا نسبت به مسی و پاسخ جالب جان تری از تجربه بازی مقابل مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/Futball180TV/92903" target="_blank">📅 15:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92902">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc3493e5a4.mp4?token=jhRPJAYz7wDg49BIati8kIfHXl-rqa1DHEbejTYha-Dqg5oQK5aFChATMZSdADZkT8yogd_gwrRKGNQihEFv79bccRtDmL6jj6N8vPzFM02vIkzAbgcRmTM33mvYYXhzgWmZy3K6iF1oAe_hxW_Bk-rAF3UN2FBS5FTvr8Q40nTivffKwIFpVyruJ5PgrrHO8NFSb0h5IZJSGXWR09O3sIWiGeBA000txMSD2-em1d2k6Xj6bHVSrhdiwxpEgWNLgmS6r8uLXSWiA_OJSVXE5wAVGFcNHK6BifplSQ2TSM2R0AvzQ_tjCW7gM3Bu1fYHuopU1F8n5ZMV8YwJJ0UVmJSQ0nbX6Rew7tdYeIAMX6oUWVdMx3xi9Ptc1Hxfe21M3thrviungdvuP2d2FSNUyV_C6tvhBxFzdE_j8-I2c3j2lNJrRMrTIwHHCMVd9KscyqyvcBRtBCzU2zcEspXVNjl5FfeDqNvzszKbWe3XSagZv6APkdOVIGmpMqnpYKnfTNRENjQ9VaxT3BZmMPOvokVmmspnQDoK-GSfMnar-w5dnb5OiSKbe3ki1BdMoHFPgdxiXR3-8x3-HSjNhSmF8g34ZeciGtetamCoATm2qJuiF0f3iuUfvwl77kS3YLCJuVfFndmnQmpth3kCyzmSeC8jN03rwccZb5trqKCK-Mo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc3493e5a4.mp4?token=jhRPJAYz7wDg49BIati8kIfHXl-rqa1DHEbejTYha-Dqg5oQK5aFChATMZSdADZkT8yogd_gwrRKGNQihEFv79bccRtDmL6jj6N8vPzFM02vIkzAbgcRmTM33mvYYXhzgWmZy3K6iF1oAe_hxW_Bk-rAF3UN2FBS5FTvr8Q40nTivffKwIFpVyruJ5PgrrHO8NFSb0h5IZJSGXWR09O3sIWiGeBA000txMSD2-em1d2k6Xj6bHVSrhdiwxpEgWNLgmS6r8uLXSWiA_OJSVXE5wAVGFcNHK6BifplSQ2TSM2R0AvzQ_tjCW7gM3Bu1fYHuopU1F8n5ZMV8YwJJ0UVmJSQ0nbX6Rew7tdYeIAMX6oUWVdMx3xi9Ptc1Hxfe21M3thrviungdvuP2d2FSNUyV_C6tvhBxFzdE_j8-I2c3j2lNJrRMrTIwHHCMVd9KscyqyvcBRtBCzU2zcEspXVNjl5FfeDqNvzszKbWe3XSagZv6APkdOVIGmpMqnpYKnfTNRENjQ9VaxT3BZmMPOvokVmmspnQDoK-GSfMnar-w5dnb5OiSKbe3ki1BdMoHFPgdxiXR3-8x3-HSjNhSmF8g34ZeciGtetamCoATm2qJuiF0f3iuUfvwl77kS3YLCJuVfFndmnQmpth3kCyzmSeC8jN03rwccZb5trqKCK-Mo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
صحبت‌های حمید محمدی از دلایل شکر‌آب شدن رابطه میثاقی با عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/Futball180TV/92902" target="_blank">📅 15:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92901">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">Live Volleyball</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/Futball180TV/92901" target="_blank">📅 15:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92900">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hmxygqt07reJA8u6MMMi0GOEhsY5fIeDfJdPkWHfLOGTH-If1tUR4sqBdfF3ygEkqiVsqzC1QqQc16XtTWa1T7IeF2Ovzp8LeZeYaK9ImQ6HFiOsv4gXhIjIIXAOLI8PUocv4BpE1Elp7a_OULODC0DBWW9hS_UPDGIwQgeUcHV21v-NqD2nOGGNLdAJ3qPoMrZzRIGSraBG_tHM-FXOJOc9i-xPxfJ4G5TyZXwbnNMofLZt5jPICALo7q1rS5Kf9c-dSEZpDeD9dfGUhyztVd9gzo5-pAFkdU4G5MfultoHAhmpmJ5usAnNYn2eTQO0MW_PEvNTv7KBdpYLqaUVkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
رومانو:
🔹
پدرو پورو مدافع راست تاتنهام که گزینه رئال هم بود تا 2031 با تاتنهام تمدید کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/92900" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92899">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0194235547.mp4?token=Un-zQac9Xir_OASLZhLBLFH0Pcwf2Kn5n1xGhtPmDqnHN4Opa177zUgYbym-0SrW8mqJcvBKgLwZkOEb6HqqM0ikntlaynvXtRHWO2G2P1c9usFRGdZDi1C1utFJMhhelW5uGmWoQ4DS5bFKBijJ_zXVZwr3A1vCpatCEhuhiHaEu8oH7RfiOx5tCBzM0E3KqlN42W5RUHCQpBCSBASKgMoMD60IDqQ8OXdRlNUb8Dw18d7OinZtfYmtaJDr3zhavSbGsWIDE96nx1DxdJJv2op-dnFC37AWOpi8VwcSZPlhsDI-ha3r8xHZb9CHiehs2j0NzEtoj2M032QOcoY1QqOUXTDbpuTFiFhj0zUoojOF7jPTVVQxdg6p7g23yh6s8sbf0jhD-HHstLyL8oIuIJoSilu15IuBquo0H60ktTWcsyFRfY-Pdd_9nNxu7vJC5jX7ZW3TfXufD95gYCj32ZbIu8WwzFFSFO5rVwjsXZFpiDmAg06ZexBioQlAin3bdhBblfqem5mdJQn7SRWsr-bjzQHE1UHgt1CkO7tIq6014D_JQqAuoVn_VhCwTGrhP9nKKVRuTXuG3W3yvJzmiDVbxSqmG9fbGCpzRrSF-yT1hyCL_b6HR3lxsa9jSWxUZA-bJtBnosX74QJK2DfMVsf4FRi7itpZcT9lUCz7CM8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0194235547.mp4?token=Un-zQac9Xir_OASLZhLBLFH0Pcwf2Kn5n1xGhtPmDqnHN4Opa177zUgYbym-0SrW8mqJcvBKgLwZkOEb6HqqM0ikntlaynvXtRHWO2G2P1c9usFRGdZDi1C1utFJMhhelW5uGmWoQ4DS5bFKBijJ_zXVZwr3A1vCpatCEhuhiHaEu8oH7RfiOx5tCBzM0E3KqlN42W5RUHCQpBCSBASKgMoMD60IDqQ8OXdRlNUb8Dw18d7OinZtfYmtaJDr3zhavSbGsWIDE96nx1DxdJJv2op-dnFC37AWOpi8VwcSZPlhsDI-ha3r8xHZb9CHiehs2j0NzEtoj2M032QOcoY1QqOUXTDbpuTFiFhj0zUoojOF7jPTVVQxdg6p7g23yh6s8sbf0jhD-HHstLyL8oIuIJoSilu15IuBquo0H60ktTWcsyFRfY-Pdd_9nNxu7vJC5jX7ZW3TfXufD95gYCj32ZbIu8WwzFFSFO5rVwjsXZFpiDmAg06ZexBioQlAin3bdhBblfqem5mdJQn7SRWsr-bjzQHE1UHgt1CkO7tIq6014D_JQqAuoVn_VhCwTGrhP9nKKVRuTXuG3W3yvJzmiDVbxSqmG9fbGCpzRrSF-yT1hyCL_b6HR3lxsa9jSWxUZA-bJtBnosX74QJK2DfMVsf4FRi7itpZcT9lUCz7CM8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇨🇴
این پسر آرژانتینی وقتی بزرگ‌بشه میفهمه چه نعمتی بغل دستش بود و استفاده نکرد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/92899" target="_blank">📅 15:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92898">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8RplT6wTAVx4nSk3Q67eXUqYQjq1Eemsq_9ll8-2ijMBKWt39HooN0CdnAbAcPtP4CSg743sMD5y0S4UOhoWJjLNnv97ImeorsU3AluZteLo0WfJ5F9JBPom8Y0tlyYUzedQAf7O01YjjaxBWzTYOmnQIZrO_hlOhn9w6c9LfM8X1xqCp3aSyfgye6y1ElhzvAVcChoghYedUC2R2fcPBAVtf4JW3YTMjWh3zW62N1IIgmPo_GypIzJoiC0ovfAu5-w57AermKzD8I7FNIBY6XQkyc2WpCklr8fkBRKI6EvXSIU98XVszQUR9rJNtl0EJTUdIyJ4UjybUXHFjmlrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار و ارقام تیم ملی آلمان در تاریخ جام جهانی
🇩🇪
:
🏆
• ۲۱ حضور در جام جهانی
🏟️
• ۱۱۲ بازی
✅
• ۶۸ برد
🤝
• ۲۱ تساوی
❌
• ۲۳ شکست
⚽️
آلمان در مجموع ۲۳۲ گل به ثمر رسونده و ۱۳۰ گل دریافت کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/92898" target="_blank">📅 14:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92897">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
#فوووووری؛ حمله دوباره اسرائیل به ضاحیه بیروت، توافق به هم میخوره؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/92897" target="_blank">📅 14:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92896">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دیشب تو بازی قطر سوئیس، یکی از هواداران(خانوم) شرتشو در اورده بود انداخته بود وسط زمین
⚽️
@fotbal_xc</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/92896" target="_blank">📅 14:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92895">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPgNkVSJiYcuvKvVahOvA840_rrUZ5W8lKZUeMQoPaD39S7eqluVEyjhPOSJkh9VyT9hwnf-rRlPoKGR2-dSTN91PLEv8Og1839UsYRfwiY_xNgwn7fcQB3vY2-LpRYU0_3IEBYM280c8m6TZfumrU58kzhVqVdbkD2hTzxSA0EKdvJDkfyrJHxqaF64YnTX9RkJPqYKN7tAJaCXMl7BFv0uzG6YBsoAffdp_JwIwBtYJA-rkbsnO1qVRnn8AkRlktONd4MnClavz8ULeVGY6GyMPN6MTeOd9OIHkrKyA6B2Gcc5NdzNAzSQKxYTyh4hTomLVHJW3XfnEvQh1ubVUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#
فوووووری
؛ حمله دوباره اسرائیل به ضاحیه بیروت، توافق به هم میخوره؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/92895" target="_blank">📅 14:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92894">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b1d4f272c.mp4?token=dAPYeZNRJJEavrbzFqrDCGtnxBtxp0TSP0xjeCDIH9RVNCrASpw07x7Y5SLXs6S5CE5cQb5FhcGV0--w89u5_FIGinzORwonpaCUNKeOZfn5rECinU8uvFh-9LtbDlg5tIb0dvpBO6yCOXpkpxLGtxwBgDRP7lPG0mQZTFbdijv9MS9qebuu6eKILV0KxQuSbo8MXF55hmoF9Ca1rVcYBYUNoEkndicYiD8ZfYFiTvKLbgl_80g7DJ3Oa97mCaUMe926o9te5K5tmcOtK9N0QU7xNg7KH5SBbqU7vrs9cYIBER2S6HX3YVdirv9d2dbjMZK8jYd3B3Y03bHEfOznng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b1d4f272c.mp4?token=dAPYeZNRJJEavrbzFqrDCGtnxBtxp0TSP0xjeCDIH9RVNCrASpw07x7Y5SLXs6S5CE5cQb5FhcGV0--w89u5_FIGinzORwonpaCUNKeOZfn5rECinU8uvFh-9LtbDlg5tIb0dvpBO6yCOXpkpxLGtxwBgDRP7lPG0mQZTFbdijv9MS9qebuu6eKILV0KxQuSbo8MXF55hmoF9Ca1rVcYBYUNoEkndicYiD8ZfYFiTvKLbgl_80g7DJ3Oa97mCaUMe926o9te5K5tmcOtK9N0QU7xNg7KH5SBbqU7vrs9cYIBER2S6HX3YVdirv9d2dbjMZK8jYd3B3Y03bHEfOznng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باشگاه بدنسازی تو یکی از روستاهای مملکت
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/92894" target="_blank">📅 14:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92893">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxxNXg1e-o34d6yEyIk6XN7slHm-Fjco6GfWJTKlRfFzm6M2eRvpQFGqWybY3j_omr3RIiIb-HydAHdHyux_5qOfovn-Y-8wVj_2UZnC6Hqy4bO66vAVyMltA-5TAwi7fTX0ZXBy9upkq5Ml4Lf9_KbHUIpnwqkUbBH1hPmemE62DGI7gzfj8vpvETGDak5_vN_CQrppaMeq2wSNaiE4CbxhnEm-L6fSC_eetlZyu1PzqxuyEkfvBL6ULsT47moDstgB6QjiWNA_05vDOnwCmj80wjcWm9MyGJpkvw2o_h2Mamihti0wWGkT-Y7UOY36w4xZ8xk-FaXPwpJbvf-IFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیبی که استیون جرارد دوست داره تیم ملی انگلیس با اون در جام جهانی بازی کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/92893" target="_blank">📅 14:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92892">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da69a4b2bc.mp4?token=boKESNbqN9P_17fEa8khWiMsTYE12RA7TBm_E2qA_Ll3c24SfAXjPP42B6gWUhzcw1z-UMBfi56D15X56uiVg_iJlsQIK4RxjoPnCCnPZ3y1UA1FND3UDP3L4My92VG0CpxERsY-QNHLS_IbdHbOWgtamvHqEaiKYv1OfDcSmccIU-DwWQ-RRFXpWnCazgeW2n8ZAJbvr5xXKOPh_e8-NFxztg2-WZunXg_dVlTzbbTbFBpha-zfNygj2kAjsR1_CKSeLlMbnZkFjsF_jz2pUyh7KqgPfh6QKP_BAU6e9ro1suA3T_kOOvnt_yzE6f2LgjN8A19P479Mocl9qMoBYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da69a4b2bc.mp4?token=boKESNbqN9P_17fEa8khWiMsTYE12RA7TBm_E2qA_Ll3c24SfAXjPP42B6gWUhzcw1z-UMBfi56D15X56uiVg_iJlsQIK4RxjoPnCCnPZ3y1UA1FND3UDP3L4My92VG0CpxERsY-QNHLS_IbdHbOWgtamvHqEaiKYv1OfDcSmccIU-DwWQ-RRFXpWnCazgeW2n8ZAJbvr5xXKOPh_e8-NFxztg2-WZunXg_dVlTzbbTbFBpha-zfNygj2kAjsR1_CKSeLlMbnZkFjsF_jz2pUyh7KqgPfh6QKP_BAU6e9ro1suA3T_kOOvnt_yzE6f2LgjN8A19P479Mocl9qMoBYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
🇧🇷
ویدیو همسر نیمار برای جام‌جهانی در حمایت از شوهرش و تیم‌ملی برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/92892" target="_blank">📅 14:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92891">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNjBOpe33GFlpls7egJehzSabg7YVYtyhbHponv_CTSJ2Ua5iaYNUigE2_rqB6b4rHxYQxM1nuph8VLhfB5771x6ukHOG_3UexKEKA0ZK0_UaGRM6dJ2_xniQK185smyRgGzb_GyNhdymd88TDwJ2RW0u7o_HrmJhhY9Z_sD_yPJf-MRgTzz3VfjdWTW2djFYeA77Y3xTcj-cas6CeXR_aHWaM0Xsj9iW7ZycIazPD9JvcciH0_awhUA5RiqT_HOtkSXmCx2B7qnmcAdTc16CgZP-U0lDQXol0YeulIK60wCxFkpJ9KVyUUSwo3sz0H6q19NnkK55eUiQmqOpg2gcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏴󠁧󠁢󠁳󠁣󠁴󠁿
یه فکت بی‌اهمیت بخونیم باهم: به جز گل‌های به خودی، هفت گل از نه گل آخر اسکاتلند در مسابقات بزرگ توسط بازیکنانی به ثمر رسیده است که نام خانوادگی‌شان با Mc شروع می‌شود.
‏
✅
مک‌استای
‏
✅
مک‌لیر
‏
✅
مک‌آلیستر
‏
✅
مک‌کوئست
‏
❌
کالینز
‏
❌
بورلی
‏
✅
مک‌گرگور
‏
✅
مک‌تومینای
‏
✅
مک‌گین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/92891" target="_blank">📅 14:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92890">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCF0-4-YJtzL1EsK-FAI2EY_3UbPwIkDTAWdEVQFM4IZBn4OSmJauUW_lrcN1xE6AHOp1t2m09kBwSLmwB9_fCnhFHnnYCOOlBe2po60Gs4qzabMvaGATRBzMBclDy8cyiHyn6qO1KosUohqs4EfnHU4TcU6QOeZZ7t6poU1RE5IX5sC2X1vG8L50EOOiKt7Nabi_oTPY5eST3cwJOW0IRbRYe7tBazW41d6bMze4_kk5PRz0miH6f8yYb_s7etD6fh2O6K1flLXfT1PdjFvHeG49BozjdHAOU8c4tHO29wK2B7Z4beG7DMIZO_iG30LUivEw_Ifi1X-b8-_DvJn5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
فیفا اعلام کرد که به عمر آرتان داور اهل سومالی که توسط آمریکا دیپورت شد، مبلغ ۱۰۰ هزار دلار حق‌الزحمه پرداخت خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/92890" target="_blank">📅 13:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92889">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNwr-Qv7Jo95gCJoH0Xo9Km4-KQFvlfO8TC9BYuc0UvS0TqNn8-aMCz699yfd5mYjK9z0Q7hka8v92siV6zqWjrWdVSfqQ4EkAmZaKy2N4nHx4WQXytSnPuoMA_hswxVigp3ckGrVm3YYGFOQ4H7hnA4fTSSeW3U_zCZALyzVoXaBTq_tBnW7kAcQCh7kKZJh0Ikgp9raUbzIua2-GUm5demgvDMm3KUVIBXllA9Okrv0JEeuPwpTv0qEs60aM6U_Q7dO8_XamhYt96YcrlHEC6gUFBRtaB5IxxzmiiKDPwmxYlt_KQn7dG-gO17H9im2Zuari1qVdTP9XnwTrGyoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نیوکاسل برای فروش ساندرو تونالی خواهان دریافت ۱۰۰ میلیون پوند شده. آرسنال و منچسترسیتی جدی‌ترین مشتریان این بازیکن هستن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/92889" target="_blank">📅 13:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92888">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1AlOtHZnnN6eW_JOGYrbvelEHDmgETf_jE9-7vYBhardvTzcobFCv2Sh6Plf8Dk_F5lRq-YkGBCVwYnGoKj3srYhVNj-iLQST40WmyIY40Go764BT9YQ-p7mZ_K5LrXEbItyYcRLzLBzMrdMswEtWscGweJ2lXKcomEXzxG3VmsBwt06JUtmfVJA9I3qI5TA-nizMKfV0uwe2SsV8Hk-MifqTAmbX9gUHkzkihycvWqVTdwcCLUzVtD42JpIaUJvU51nuv5PpeENhdF_-_YbcKRqGE2DT_h5asHEqK3vEgO9UIzqtANqenYImEgdDzozEK8qxpE7lXVa6Ocy3899g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🏆
🇵🇹
ویتینیا:
🔴
برای من، اینکه با دو تا از بزرگ‌ترین بازیکنان تاریخ، کریستیانو و مسی، بازی کرده‌ام، چیز بزرگی است، ممکن است بعد از تکرار زیاد عادی به نظر برسد، اما اینطور نیست. به نظر من آن‌ها از بهترین‌های تاریخ هستند. افتخار بزرگی است و غرور عظیمی که بتوانم زمین بازی را با آن‌ها شریک شوم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/92888" target="_blank">📅 13:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92887">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ab1ae15fb.mp4?token=eoUYYXEdhpk67ct84J06fekxMhyCedyVpB_7fE4dyThOAPECp0x2jFhSD6Qarx4z8NVoEwrFyNbIawFk8qVgC8M1Gqb9P3Mos1-PORcv775CZJ78WSgWtMQYtBeLoH9eMCVUQj4yC8vGc4ZsY6ub5gne4apVScmz4qnzDb-t0-0e-mjx4ZIfdoRHhxzH7_2PWcR6D-QeAN5UD5YGVLxs3OVUYzWmTpFQoWeIlkVHzA9f3yBjYV2TzAP27vSGMHrXOwruhNUY6l8-V1eW5lhErG2kLGXeEXx6BgSLlYRGQ5fMym78u97-3RRm2F3aLAXq5c5v6TljHurP6xU8kjOWAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ab1ae15fb.mp4?token=eoUYYXEdhpk67ct84J06fekxMhyCedyVpB_7fE4dyThOAPECp0x2jFhSD6Qarx4z8NVoEwrFyNbIawFk8qVgC8M1Gqb9P3Mos1-PORcv775CZJ78WSgWtMQYtBeLoH9eMCVUQj4yC8vGc4ZsY6ub5gne4apVScmz4qnzDb-t0-0e-mjx4ZIfdoRHhxzH7_2PWcR6D-QeAN5UD5YGVLxs3OVUYzWmTpFQoWeIlkVHzA9f3yBjYV2TzAP27vSGMHrXOwruhNUY6l8-V1eW5lhErG2kLGXeEXx6BgSLlYRGQ5fMym78u97-3RRm2F3aLAXq5c5v6TljHurP6xU8kjOWAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
دیس‌بک ابوطالب به میثاقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/92887" target="_blank">📅 13:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92886">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPa1pkj7bWzMAnlpsVRQmA9PEWBfk-s2VN_ggTY9CX-O2e7zl66UhoLbT8VhkkBcDPw-B9TyfDm3jrrLLVKxKQYs9Xxedvgv6Lukuuo4X3tpxwcNIXLfd2dkzV7pi8MbUQZLFE2MCQRc7gvaE7dUGv2ojPsVQH-YXbBIsy77x6zmQYXd2PrtiULk3zPm-6eGppDjfdTeX0NfjqcbPnEd2hwALarKylZylfsTF9ktkORkYsdMSJFFozD9omIVBx-QsZ5ucSNyKVD-dKtU6c5mrJG2FppHlGjszAmfoOpaeNXM_xUKSFwvdIDCWtTOD75_8D3nFWylUxa_FtjFwqZ5cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جام جهانی پر سروصداش خوبه!
🔊
بازی ها رو تو ویلاهای جاجیگا دورهم و پرهیجان ببین
وقتی بازی‌ها نیمه شبه، یه جایی بهتر از خونه برای دیدن فوتبال لازم داری. جایی که بتونی با دوستات در نهایت هیجان بازی‌های جام‌جهانی رو تماشا کنی
🏠
⚽
ویلاهای مخصوص تماشای جام جهانی جاجیگا رو اینجا ببین
⚽
🥅
🥳
https://j1g.ir/t7
⭕️
جاجیگا، خونه خودته ;)</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/92886" target="_blank">📅 13:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92885">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94684b60b2.mp4?token=Mpi1jm3UALKDAd2ryUdZm_zSJQ0jmjs8LMe1oqPVjjo1QtwBv_YG-93qjk3fis80J_HyYrUxdMsOFfdj-i5tZnM4ulVUDW9tMWU54J4HF6nH5ilA_JX4HLPCDp07kEHnIniQ8q7SdEfmhXbhV-fAjgUD8zjhtqle0ZosaE6MpairMx_UJHVWaSPNMtgQ-0rSJsjEBDriS6bpOQ_0LAg5jHQTrnp83FOMoC0u3WKGDsdPMkQTRwtivrvGbfgPOxEXeZeYouBpUKnBAqyPRFiINiShhjxH-SIhmXkp8WQvml3gZ1hFLdt-iRKI6Lz_WpN63srtMIsISSDqmnhSH4orDIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94684b60b2.mp4?token=Mpi1jm3UALKDAd2ryUdZm_zSJQ0jmjs8LMe1oqPVjjo1QtwBv_YG-93qjk3fis80J_HyYrUxdMsOFfdj-i5tZnM4ulVUDW9tMWU54J4HF6nH5ilA_JX4HLPCDp07kEHnIniQ8q7SdEfmhXbhV-fAjgUD8zjhtqle0ZosaE6MpairMx_UJHVWaSPNMtgQ-0rSJsjEBDriS6bpOQ_0LAg5jHQTrnp83FOMoC0u3WKGDsdPMkQTRwtivrvGbfgPOxEXeZeYouBpUKnBAqyPRFiINiShhjxH-SIhmXkp8WQvml3gZ1hFLdt-iRKI6Lz_WpN63srtMIsISSDqmnhSH4orDIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپید با همین کسخل‌بازیاش اینقدر ویو میگیره
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/92885" target="_blank">📅 13:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92884">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tXAVScJ2TC6dXAU9fiGDxEqUbQYGShRTv1n8mOo_GR-yn9595_K9DjKj-hwfS0lhBDA5w9E4PIExhZSNtTJoh4uI_v9HN9_6f0RaFKUX9nj3E_VK2lpcbAfuSu8xJaIa16v6D4ebVk7TTIqUsDOcGXeLSAwT6AcdIcNVUF7OsNmI5YAYOCUnLcMpt4nXMIfr6SXyerl9jppsj6Zdq8HP67qWOpQsZByVQKjYBDsEC-V8FS9GqdrDdZPN4EaIesAflwsN1yshdluOBaaN9-Bae3o5MAz0gO73pgp25xYGd3fanhvr2vbS__WCQDX1UvziOhNPe9qitdpdSjKd9irC5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇪
🎙
کوین دی بروین درباره جرمی دوکو:
عملی‌کردن دفاع مقابل دوکو به صورت تک‌به‌تک به مدت ۹۰ دقیقه تقریباً غیرممکن است. او همیشه در هر بازی بین ۱۰ تا ۱۵ دریبل انجام می‌دهد. با سبک بازی‌اش، به طور مداوم چندین بازیکن را جذب می‌کند و این فضا را برای ما ایجاد می‌کند. بازی کردن با او زندگی من را آسان‌تر می‌کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/92884" target="_blank">📅 13:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92883">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d82ee8274f.mp4?token=E-G2UT1snt-mmAbnfLXVsoiyjJZeZw3wACuhfLV-4c7ISCOOlof867hQoezrSy3B3Ue2G52_X5BOODCjfGs25wvs5SaNRGdQlsqdu15KoFPhQLC444jbdJSunm__664e3A7M8CCBoRBBMHWd7Eao4i9KvLGPT4iXs85sk9OJkY2LXN8C4u6qTs100t5qrroezgZnyrz3iZPfZPvMZZSuhrg3jjhUzmxnqgXmLzMqg-Ahhm6vbQz2zEk1wJly_ib3yCiOHwIzBw2oLlCm3pA1ihHNqESEINMT6pwzRkM61y4zTvTv_qBApXNSpOWA2-Kf-10fpIM3FNr1PUswv8tVUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d82ee8274f.mp4?token=E-G2UT1snt-mmAbnfLXVsoiyjJZeZw3wACuhfLV-4c7ISCOOlof867hQoezrSy3B3Ue2G52_X5BOODCjfGs25wvs5SaNRGdQlsqdu15KoFPhQLC444jbdJSunm__664e3A7M8CCBoRBBMHWd7Eao4i9KvLGPT4iXs85sk9OJkY2LXN8C4u6qTs100t5qrroezgZnyrz3iZPfZPvMZZSuhrg3jjhUzmxnqgXmLzMqg-Ahhm6vbQz2zEk1wJly_ib3yCiOHwIzBw2oLlCm3pA1ihHNqESEINMT6pwzRkM61y4zTvTv_qBApXNSpOWA2-Kf-10fpIM3FNr1PUswv8tVUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🏆
خبر خوب برای هواداران کرواسی؛ این رفیق عزیزمون گفته که براتون تو جام‌جهانی حسابی برنامه دارم و منتظرم باشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/92883" target="_blank">📅 13:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92882">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dCim27bO1qlirHvvF7t40F0an9RLe1k5FUuFobKbuMhNZ8KUHsl1p5XHh88B297yqGvVYCxoiBSnolVDioB_e3KhwBLf7hb6d-xtxsSXsF5dHDiiT96Q5jFIVKHnTLHyC273LUeHKDg97YXNJPqw6Ew53FI4CRMEbXb6gL3S12puu0HB1-tdzzyzdQZ2TkOL5a30QH30O6TaaNJnrAZnx2A610wQ0SpzofjMEcxpV1hJIJUiklJ3ofEHCRQyvgaVD0fJKeE079IvO0kF77kRlha0A8wxwXtcFtRmEpePoLol-FwaI4QbLzuqPmDj7ohB13brmcwl1JC2VZE4N5CGgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
🇲🇦
‏مراکش اولین تیمی است که با ۱۱ بازیکن متولد خارج از کشور در یک بازی جام جهانی شرکت کرده است
🇫🇷
‏۴ نفر در فرانسه (دیوب - نائل - بوعدی - المرابط)
🇪🇸
‏۳ نفر در اسپانیا (صیبری - حکیمی - شادی)
🇧🇪
‏۲ نفر در بلژیک (الخنوس - طالبی)
🇳🇱
‏۱ نفر در هلند (مزراوی)
🇨🇦
‏۱ نفر در کانادا (بونو)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/92882" target="_blank">📅 13:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92881">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K46JVBaowM41qf-1238vyWnPjhcXqIHTCvpL6R7s5a6wi9Ca-Qv_0wBIw8dF1SrEcIgMh3BKUT4Ss61miCnUNlUC0aFV3n2CswnxCOSTT7HncrKnMMKuP_W4XCMIzsrISlKO2kf5JLWOlPv5tmg0ZpJM6oNBz9yohEaj57Xp00ZaPtFknKPj01ExjH_QHDD5m368cvilw3kV-B031Wu1oBczS2Ktl_aW6pRZ1kUsQtMn3oOiPMzUVXxiEtsfbVSz1e57PEhu0VC7VUmfGONnyvqxJCvR6_P3nDrmBDN8axj2dO6kNbWR2JtDxjEEMihuXyhgwdyGjrvuDB9C_3zXtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
📊
🏆
آمار مسابقات جام‌جهانی تا اینجا:
💥
8بازی؛ 19 گل؛ میانگین 2.38 گل در‌هربازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/92881" target="_blank">📅 13:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92880">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‼️
یه هوادار کره‌ای بلند شده رفته استادیوم بعد مکزیکی‌ها اینجوری پشت سرش حرکت نژاد پرستانه میرن که طرف پشماش ریخته
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/92880" target="_blank">📅 13:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92879">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b98e2b8a04.mp4?token=NVLOczLZgeX8zz84VuuvGbEMGUVU0azIXYrEEiQi6ZdS2TWyVd2TJRvGHC2sI4bAuxSb6dTi1b_1-HvY4O8OoITSVk7FRQMIk3zIZ1suhuZTUkK9ARwKfHPVBQ7xYW1XU277eTPypzzGVTMCLqhaMGFeRJgWyZYqkZJeJXginC9uRnx1g_-6U_ID56f36CUyLzqxvMsk91vyPDHu-qhNwtY_VWEuq8KgldTaViEgqEP67sNzoklKbaECjWr9XtCiaZhnqCfNb3FzefIO7QnQNbEHKvBowK2804GbXQgzHvU5ZUBJrwhTLs3IAQlF5eXkvsE2vLVH4GoRdCpCCUUj_TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b98e2b8a04.mp4?token=NVLOczLZgeX8zz84VuuvGbEMGUVU0azIXYrEEiQi6ZdS2TWyVd2TJRvGHC2sI4bAuxSb6dTi1b_1-HvY4O8OoITSVk7FRQMIk3zIZ1suhuZTUkK9ARwKfHPVBQ7xYW1XU277eTPypzzGVTMCLqhaMGFeRJgWyZYqkZJeJXginC9uRnx1g_-6U_ID56f36CUyLzqxvMsk91vyPDHu-qhNwtY_VWEuq8KgldTaViEgqEP67sNzoklKbaECjWr9XtCiaZhnqCfNb3FzefIO7QnQNbEHKvBowK2804GbXQgzHvU5ZUBJrwhTLs3IAQlF5eXkvsE2vLVH4GoRdCpCCUUj_TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
جمعیت فوق‌العاده آرژانتینی‌ها در آمریکا برای حمایت از تیمشون مقابل الجزایر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/92879" target="_blank">📅 13:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92878">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/92878" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/92878" target="_blank">📅 13:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92877">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kgrq2jZAndNcvSA2_76cStLdyj5CIgWSqDp9NR1efpeLirRkElQbIDpe8rsExUB_iwzjkSx3OsSMMvYjDH7Ark262Z0pDAUCbRQgWbNhHIzc0vNr9POrnwYubx0aJNqmv9buJDTLmIT9nisPXlj-xecNpEWug0CAAZMHLG2NFkr8FTr_2npoCG9tdkcX0Qj33xh9kbiCPDU74bbS1pQEPcbItml2CVl2-ovBJFwjgc5iAjv23SqM3eLtc-RDHod5KvqxYaXcZ9ydB9rjhG21-JrZer0RZzYtA9Ac5Am2O9EoBucx1T1HG6mODpztP4EDEOHQPixoNPQAUtMMdz8_Cg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/92877" target="_blank">📅 13:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92875">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🏆
🇺🇸
ویدیویی دیگر از برافراشته شدن پرچم شیر و خورشید در استادیوم‌های آمریکا حین برگزاری جام‌جهانی؛ به گفته ایرانی‌های حاضر در اونجا، پلیس گفته که هیچ محدودیتی در آوردن پرچم وجود نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/92875" target="_blank">📅 12:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92874">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f330d63e81.mp4?token=HPQVQPeMGnxDwyBxU8FRDRlYNo2GhAZwKxhBy1w43az1VCHLPV8UTbX5jKbaYoHf9pyfqgh8k3Ml0JKiCxiuHrbmeUVgRZ3xPfSGZtLvJhIMUwBD34B5SJXTho7-gLYz4nEsQl9453xhuFepzi3VmPLFXRyoGLM0Rul2LDnB1nE0IiNVvH42M622hxT0P8wzrM9eSPQQ8oKklEijyJd9BLJDkVvpkqGVOafNa7_ibDtugvhdLaZhdhbd9NKZukp8TdApRvmF8EmlbOPdq3UIj-AgxWQkSKK34vBnlL19HIAf9d96CboP-tTSjy0QIT2HtGDuoy2O7gQr6KvySKfn8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f330d63e81.mp4?token=HPQVQPeMGnxDwyBxU8FRDRlYNo2GhAZwKxhBy1w43az1VCHLPV8UTbX5jKbaYoHf9pyfqgh8k3Ml0JKiCxiuHrbmeUVgRZ3xPfSGZtLvJhIMUwBD34B5SJXTho7-gLYz4nEsQl9453xhuFepzi3VmPLFXRyoGLM0Rul2LDnB1nE0IiNVvH42M622hxT0P8wzrM9eSPQQ8oKklEijyJd9BLJDkVvpkqGVOafNa7_ibDtugvhdLaZhdhbd9NKZukp8TdApRvmF8EmlbOPdq3UIj-AgxWQkSKK34vBnlL19HIAf9d96CboP-tTSjy0QIT2HtGDuoy2O7gQr6KvySKfn8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
روایت جواد نکونام از پنالتی چیپ یحیی گل‌محمدی به چین در جام ملت‌ها آسیا ۲۰۰۴، در گفتگو با امیرحسین قیاسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/92874" target="_blank">📅 12:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92873">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
تمام بلیت های بازی ایران نیوزلند فروخته شد
و مجموعا 70 هزار هوادار در استادیوم حضور خواهند داشت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/92873" target="_blank">📅 12:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92872">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c1c285036.mp4?token=MBB5mCV0xraxuOwtElGYfnB-X7cgy4OBXOfkXsc60pJX6P2b8QRJ1oHpET-8j-_cwbeMZCgMqhglFb6dmjuDUCCfZZDfIYb_W2zGrLzWTHjNicR1feCLOv0tnf4gL_uPdgmWyWHStCml2ZFGydJzIhTfOupQV-68PM5oXmfGFSCgWrdXeFAkylb0_U8IuMwj-1UBstZwnWV-F_ax_MiWrIGtMn2_SLUCal5lELP3DM8OhmhtTQoOXKAX2cN2dFG-JNczMeYqsZ7G0ZOgdjgo31hgv38F4IhcFqhNAd2n1DSMVbUsAHCzTqGAOqbZ19H5PR79c7IGNtv0ghR6IU2UkRItbV9HIQJ30PT4ZN5IWYPxA8neOFGLMp78mdb8gvPtuaYU2YQ9cN66e0FDoqF4kMcFlvknkJu1AQNhrIvV5RLge7z1kGR-aY5IDuAsanSGDJtbvckUV3aGqxM9SxD01lQI19b1l-F_sR0Cb_0rOdGUIqSxIX7u48saZMFAQeOcbvccVC_P9SA9X1GytoN6v7N6oSUZuoIxFNCLp4ZWHfR3p37fyWrmZUnecR63n-6Rjh1GlbvlkVXemWfwn3VSWVGNP4jF_fZkC5CoYHyUwuJqEjgLQ-rE5Wg0icKlOlPRoKtICGU3I0Vk7P7NfgGG_mFxoOhqj79c261E04F_WFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c1c285036.mp4?token=MBB5mCV0xraxuOwtElGYfnB-X7cgy4OBXOfkXsc60pJX6P2b8QRJ1oHpET-8j-_cwbeMZCgMqhglFb6dmjuDUCCfZZDfIYb_W2zGrLzWTHjNicR1feCLOv0tnf4gL_uPdgmWyWHStCml2ZFGydJzIhTfOupQV-68PM5oXmfGFSCgWrdXeFAkylb0_U8IuMwj-1UBstZwnWV-F_ax_MiWrIGtMn2_SLUCal5lELP3DM8OhmhtTQoOXKAX2cN2dFG-JNczMeYqsZ7G0ZOgdjgo31hgv38F4IhcFqhNAd2n1DSMVbUsAHCzTqGAOqbZ19H5PR79c7IGNtv0ghR6IU2UkRItbV9HIQJ30PT4ZN5IWYPxA8neOFGLMp78mdb8gvPtuaYU2YQ9cN66e0FDoqF4kMcFlvknkJu1AQNhrIvV5RLge7z1kGR-aY5IDuAsanSGDJtbvckUV3aGqxM9SxD01lQI19b1l-F_sR0Cb_0rOdGUIqSxIX7u48saZMFAQeOcbvccVC_P9SA9X1GytoN6v7N6oSUZuoIxFNCLp4ZWHfR3p37fyWrmZUnecR63n-6Rjh1GlbvlkVXemWfwn3VSWVGNP4jF_fZkC5CoYHyUwuJqEjgLQ-rE5Wg0icKlOlPRoKtICGU3I0Vk7P7NfgGG_mFxoOhqj79c261E04F_WFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
🇳🇱
جمعیت پشم‌ریزون هلندی‌ها در آمریکا قبل بازی امشب با ژاپن؛ بازی ۱۱/۳۰ شب از دست ندید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/92872" target="_blank">📅 12:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92871">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IK4sRHw8bF0sqIsefhYl3LBgWKG24kBuXB8nq11DIID9WjpD1GEB03SEt0B3T1tp7XUEMj1rYerVhPDqbM4lqItPG9hFQjb4lduRWQLlME-J9rXgY9gZ436XwzkvgIQdfO7mpoT8sa2fJ4WGlI_fsAqqKkXpgylnu3ghNpxBzz6QfosUF8QtltDsi26PgNC-ZeUeRHNqQNPHjQrEE6kxOp2GjT9sEfImVL0EB2ynd5l0Foe8OcwFE68drOHGQiuuLxLHcrpzalql7kctB2EiBnJ1NvFdCcUhv2JxGGj2ot8qBfDdiwVn6-A6uZpFP_EeZ09EtbZxvcH3fjQWWEIlYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
میگل سرانو:
ژوزه مورینیو تصمیمش رو گرفته؛ فران گارسیا در تیم میمونه و آلوارو کارراس باید به دنبال تیم جدیدی باشه.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/92871" target="_blank">📅 11:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92870">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">وضعیت تنگه هرمز  پاره شدم
😂
😂
😂
@sammfoott</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/92870" target="_blank">📅 11:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92869">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">💥
🏆
پارت‌دوم لب‌گرفتن کره‌ای‌ها و مکزیکی‌ها
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/92869" target="_blank">📅 11:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92868">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vMbb7HDuN4kjFMaclwQr4Nd-ugDxoTNgxVkWt3ASWWu_gGjilT8C1SYxM3fUocldHm1KX8K_bryyBqw7C64K0HVCklyHOqH0dw0nJdy1oTqsJ69L9iLbkQEp6BHVxwVNdjv1_MRH2_39qu0lniPb11daRy6onQP-gwz26-flJlbdIOmt4lwYsB7KA6625ds4hDrOjJN74kLNImvHDFNWrMoxBVVBE3zk1PBlxA8tIRzgcnxneIF5cxW4W2RMD0EMAG7oHJewf5FUQZJkAZU1xC9kjb2VzN4C2j933-ZWuxSmYBXhIM1GHVrf-i4ZrZUaemTcGfhSp1R1IAOFTaRNlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رسانه‌های اسپانیایی مدعی شدن که مورینیو از عملکرد کارراس و گارسیا در دفاع چپ رئال‌مادرید رضایت نداره و ممکنه در صورت پیدا شدن گزینه مناسب، این بازیکنان رو در لیست فروش قرار بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/92868" target="_blank">📅 11:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92867">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4cb205515.mp4?token=Jm4lxnBpumOFL0ASrQxfhnKOGZe_AvjVsZxGxAdF3IB8vPr_C1uX1xWsthWz08IxvSabaPiazOC8r1SGd4BtYfPsk21DuPVHCmGW92gjmvGmAWY3LapfQntUYQqF2NlJE1WQAwJaXUfW_6TdyzvoHJ1_5jWNQe2FFUPbr2DEDq1R7JMbuO9U8a-VSa4BvWQAR52twEqMC06pDg3vRWvsc8T6n2W0ZPLplSPlxAANzWdrYTIbeHsgRCL0CvAL12B697IQUtREV_cX3cfVfUFxzopqG-gPHc1aOEWkaRaul8Uc9Z7sr2Ag1sDOwClQEj8qP6-2vv3tNbqNuBXxqLNivQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4cb205515.mp4?token=Jm4lxnBpumOFL0ASrQxfhnKOGZe_AvjVsZxGxAdF3IB8vPr_C1uX1xWsthWz08IxvSabaPiazOC8r1SGd4BtYfPsk21DuPVHCmGW92gjmvGmAWY3LapfQntUYQqF2NlJE1WQAwJaXUfW_6TdyzvoHJ1_5jWNQe2FFUPbr2DEDq1R7JMbuO9U8a-VSa4BvWQAR52twEqMC06pDg3vRWvsc8T6n2W0ZPLplSPlxAANzWdrYTIbeHsgRCL0CvAL12B697IQUtREV_cX3cfVfUFxzopqG-gPHc1aOEWkaRaul8Uc9Z7sr2Ag1sDOwClQEj8qP6-2vv3tNbqNuBXxqLNivQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
🇺🇸
ویدیویی دیگر از برافراشته شدن پرچم شیر و خورشید در استادیوم‌های آمریکا حین برگزاری جام‌جهانی؛ به گفته ایرانی‌های حاضر در اونجا، پلیس گفته که هیچ محدودیتی در آوردن پرچم وجود نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/92867" target="_blank">📅 11:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92865">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VbJhqGPi8KxoC-96RJk8PmRle-9kjk3tDX06zQ2hHfY1__LjrkkAOh4WsmFqlEarTv7JFDKixUJOkjSm0zum_3CU4au_46XUlLzcjAfuFkhbUpfRCWP7uWAhG6U3mN_TpKFAvpCnvdOQawpFwecRUhRctTLEbKc85IuJoVFZxA7BRZGTOY6qS1dHIYDfep7x064qkKpkYbVjLlROfZT3M7YFHzPDgb_PYZ8OtNb9QlL8i3iuDdC4So6fh-65O0f2EUr4iB1tpMxoQQad3Kky8EuIIHDKjGm8mwbIhKFWRLjZzPcuIExxsVbJAun29H6gD5jqXPThQzFTlLkwcnFo4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lA9VhhVGCYNwWGOtkdnawcBMpTpUXEoVXShDgm4XS_bHH8PxoTH3Iy2GKxKQ_beEFVIXzDrKiOZBdVK2irZ3BqtkGG74DaOzmRoG4mApTKa0F3MmRs58LWELgx5QukVHy16T3utdPVo7LyQMV08S4qFQy6vly2G27zJY9Yh2f9Crrcv4hGp_MkFPzP1B6ceDBQPRUHRqE3NQ8G2eTvKIU7MjNSxKRiTjZ5KN4uqXyGZ9Drd1uE1Rm28GCb9dXSBkcxcwiDoV2CLqCTLvSui7_Qkeo01SR17gbCRalt__mmNJVOzKnf23GLTOl0Z5P_NCPo30OwaiZOTcXQnt6RJVPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
❌
برخلاف ادعای فدراسیون که به نقل از فیفا گفته بود ورود پرچم شیر و خورشید به استادیوم‌های آمریکا منع شده، تصاویر دریافتی از روزهای اخیر نشون میده که فیفا و مسئولان امنیتی هیچ سخت گیری نشون ندادن و به نظر در بازی‌های تیم قلعه‌نویی قراره حسابی از این مدل پرچم در ورزشگاه ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/92865" target="_blank">📅 11:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92864">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83cfe6bdbc.mp4?token=vrpa4mVVPbNWMMv1qs04bKS2msUdHwhYRcJtKcdHHvtCWi5NUVNepVdAUVfbNax0TsyyhtvHXsd9LSMxD_m5z8c7LLtFxXVDE7CKy1yN9jsnOWjNbaQcRPbF2sz0fxnyEAGn11VnlnlRbTO8BOXFddBxHjySZtXjAAEuirSwFxjHnKSkCVxLq1LXVqiTzS9VlZWheDVcz_DWFw2r-Ap47eK300mo7pfgcf-enWzLgBYfI957DlIGcJVgNPHY8bUVh554k4Cct5KcksrrJ7zHBY9T0G_xxyrtVaYyB6bbTrCayaepWCVnbhTwXl_gck2oZ95OJBVhg8tahD2LvV2mvlFZZJCnDByoaeWeFC_3li614RphXZcspU-LeBHJxlJ4vVx5SbJkPgXEKStHd5c__tl9vmCBZS0UoMLKvk7_qM1RKrPtQmkJ3bw6DlHzSt49Gvpa63orwzSlwEvRNXVJmbSDj_ht9rGday7J806ZJAFr2f-RKzPML2i2zDBO6pbt0pmH__FVdUlJT3YHiH-hC4N65NMElB-AapN7r4VxCFQ56MMRa1V4wov2AI-aRwOcJb48e1Kz95_WKOjf5w8GnvQPuVR76OIgjT_LMh6jXevIl_YyRNpLVy-vDp6FJZ8eF22MKEN_cC3MyncUptM38K1pjOP7jcX-0RKU9tcWALE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83cfe6bdbc.mp4?token=vrpa4mVVPbNWMMv1qs04bKS2msUdHwhYRcJtKcdHHvtCWi5NUVNepVdAUVfbNax0TsyyhtvHXsd9LSMxD_m5z8c7LLtFxXVDE7CKy1yN9jsnOWjNbaQcRPbF2sz0fxnyEAGn11VnlnlRbTO8BOXFddBxHjySZtXjAAEuirSwFxjHnKSkCVxLq1LXVqiTzS9VlZWheDVcz_DWFw2r-Ap47eK300mo7pfgcf-enWzLgBYfI957DlIGcJVgNPHY8bUVh554k4Cct5KcksrrJ7zHBY9T0G_xxyrtVaYyB6bbTrCayaepWCVnbhTwXl_gck2oZ95OJBVhg8tahD2LvV2mvlFZZJCnDByoaeWeFC_3li614RphXZcspU-LeBHJxlJ4vVx5SbJkPgXEKStHd5c__tl9vmCBZS0UoMLKvk7_qM1RKrPtQmkJ3bw6DlHzSt49Gvpa63orwzSlwEvRNXVJmbSDj_ht9rGday7J806ZJAFr2f-RKzPML2i2zDBO6pbt0pmH__FVdUlJT3YHiH-hC4N65NMElB-AapN7r4VxCFQ56MMRa1V4wov2AI-aRwOcJb48e1Kz95_WKOjf5w8GnvQPuVR76OIgjT_LMh6jXevIl_YyRNpLVy-vDp6FJZ8eF22MKEN_cC3MyncUptM38K1pjOP7jcX-0RKU9tcWALE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کنایه‌های امیرحسین قیاسی به قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/92864" target="_blank">📅 11:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92863">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdGen2XSe1b38JDcdtpT-n-OL7aaOFpxoUFudgF301tt5pQ86jL-J6fgSOkJ_A5PmWhhCEfXRUxiCOid3DZgbERKE0ykYzkxadQPVGhBTFsZPqhcrmnit3H1zfUIdDLOBXYrOstIoHDBcdlXEEAk69oSVG-uiuKscTdHe0nfZMcWpNB9f8aFffBGckAicDnBrN8QdI-mBw5m86VLJcFZO_fdjJn8AgU-rUbUeaspIOQvOGgkFTkpybSFomdyl3OfWpeUuc0JG_fCWTZo4jbOYDzCiTV4guBH35ubKjp5FqSSaR8oLj-dM9eFoorGGaDge0P29OpFRonSjrJHxjhe1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
در طول سه جام جهانی گذشته، تنها دو دروازه بان در یک مسابقه 8 سیو به همراه کلین شیت ثبت کردند:
✔️
اوچوا در مقابل آلمان (2018)
✔️
پاتریک بیچ در مقابل ترکیه (2026)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/92863" target="_blank">📅 10:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92862">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔥
🏆
🇦🇺
شادی‌فوق‌العاده مردم استرالیا در آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/92862" target="_blank">📅 10:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92860">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBT8iXJZ9SHkD1ThPSgqnihYPwK5Ue7ja4e9fehiuU0jgmJoEjMLKI7elvP1JK4K_zjgMfVfVqPR2SmrkAqVy22gBOeDBqBtPNx8Ywasm-Yi1dTsAQdDl3oXK5Zq7Xi7fNqs7Fke7lmrboFdTSPRnp5rR0MxqvTuw_krvdxrjbPm7xALRTwZcF7nqG9Fx8VheBEyvjJdjswYoomRzBxCy4fhgzSe0sg_4gQxreRCkRCQWYi9tEL8UPK5RHBTpD-MAM2SmdBPxpbrzC0_sCknOTN5o6qm6cEwb9pmyZw57RTYmLbJnu7uWmlLzzjsmtObQFViXW7riic7IeI12GCnyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دیشب اسطوره‌های واقعی هم تو ورزشگاه حضور داشتن :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/92860" target="_blank">📅 10:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92859">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088ff3d6a4.mp4?token=ZB3qIic4HQgvJwKqqvuCNGaycs3bUVDA3W62G3KuPelO09EvKy28XSL4RUPUAZeokWdBqYWYmK3ujiiI4jI08fVTcZ8I552kvNbrWChR798mM5cugl3rq337hacEjz2VKT3uXjidLLNW4ITiV7_W4mxOGyK-O1gYbr2LMH2FiJ4pxnyWujw5Pb75XF2Ez-5m3Plv_PMA4JkSagyL2L1cgjIO4O44DGKeny1ATvvEjj7UI7JJZfcFK-Gn2bzIJbQnO4lxtLPyd968MCabL9MnhVdOJZCSW9vqrd4NdKJUuIdoKS4GbE4L6LerO5X05xWrwelxFGQkmMMfSzpZdtS16z598M-HPZyAUcJqqlwYixO_dgBL552ihUnvP2myEZ7XKWf4fKpMyC-Vwzve6qJmjNqVEr0R6CEBfoWKjZ0Lh6LfZ0cnVL2iwmJFhgBMOgs48sm8Qrq1JkOPT6Sl5L80bAP3-loly0RCbzW8BlJeiHkCPAFUGKMBSEyXVZnnlWl-BJYzG_c3l_b8KM-XbqIA0NO8qRzNEilpKEbYK8gbt5-SfUT2jcvnaINBHX5V0BzrGQ3e_yHmQ7OYyutUTEji_NvvrOaAGtKLfdjmiql-89vEpp2DqfqD_vfgg2KIUQVh3MWqopj1kgg5mISn6Z4SlOTHS-AeGHzSiJBKzYRfVFs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088ff3d6a4.mp4?token=ZB3qIic4HQgvJwKqqvuCNGaycs3bUVDA3W62G3KuPelO09EvKy28XSL4RUPUAZeokWdBqYWYmK3ujiiI4jI08fVTcZ8I552kvNbrWChR798mM5cugl3rq337hacEjz2VKT3uXjidLLNW4ITiV7_W4mxOGyK-O1gYbr2LMH2FiJ4pxnyWujw5Pb75XF2Ez-5m3Plv_PMA4JkSagyL2L1cgjIO4O44DGKeny1ATvvEjj7UI7JJZfcFK-Gn2bzIJbQnO4lxtLPyd968MCabL9MnhVdOJZCSW9vqrd4NdKJUuIdoKS4GbE4L6LerO5X05xWrwelxFGQkmMMfSzpZdtS16z598M-HPZyAUcJqqlwYixO_dgBL552ihUnvP2myEZ7XKWf4fKpMyC-Vwzve6qJmjNqVEr0R6CEBfoWKjZ0Lh6LfZ0cnVL2iwmJFhgBMOgs48sm8Qrq1JkOPT6Sl5L80bAP3-loly0RCbzW8BlJeiHkCPAFUGKMBSEyXVZnnlWl-BJYzG_c3l_b8KM-XbqIA0NO8qRzNEilpKEbYK8gbt5-SfUT2jcvnaINBHX5V0BzrGQ3e_yHmQ7OYyutUTEji_NvvrOaAGtKLfdjmiql-89vEpp2DqfqD_vfgg2KIUQVh3MWqopj1kgg5mISn6Z4SlOTHS-AeGHzSiJBKzYRfVFs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🏆
وضعیت این‌روزهای دوس‌دخترای عزیز:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/92859" target="_blank">📅 10:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92858">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUSNxGbuHm2PoAoZ65oRhVHeRKlYBSXBUP5EMtSa3bmlguu1ne7UBEpm3ZXniIqpCTOS521KE-MQu8bD9jHZFR0au9wTpC0iGlVHNsYB8ufgd8Ag8ObpHmGrqOEBanfkVaffOLmHXO-Rnyv16MVNzGx_F61V7J6e8QBIamHXgN8upk-FFM-53QNKMF_BMYfkul8XgSCvIYePeFqDPEaI6Sc_3rJOWi2xsb3ui_qBiGUZEnqDvstDH6BdzGLi5Eyz-BJGVyFJ-lRxaNYLifOpMo75FoBOfwT32kuCdRYqkwJX6oQCASVjWwPEEEydKYXiRf5fL5khyIHpMxK05swl7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نتایج تیمهای آسیایی تا این لحظه در جام جهانی 2026‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/92858" target="_blank">📅 10:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92857">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dcfc7ed9f.mp4?token=cV4ozZtUhgZr3SuMepqijsd6Hn5RoKuIcGaHjhFPYaFLgczyLaicsx3HmQBzPC-n4W-25JmzWjPU344Z5vcMWcmmJv04MFXbc6SIPDDrNIaE9fWsCziCMVg0Ig7MvGHCA3mloC66bxZSUrEEm-C9bURTf9p-1H5g7kw9R-rTi7Pqas42VC9GFbDxLVcPeUiMbJjEDp3m_6PXfXMdpB6UOdVdmG9UED8UL4NijEEXSekreizoeCJa3r9O7gYi9SiSKI8fRbrQ5BSBB6sNeCpf4zDmn7ZdEWzG_q1ITBCfr7knPXGoS7G6e6nH7TNrsOOmoqYAZWXpBHYmysOI5pw9oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dcfc7ed9f.mp4?token=cV4ozZtUhgZr3SuMepqijsd6Hn5RoKuIcGaHjhFPYaFLgczyLaicsx3HmQBzPC-n4W-25JmzWjPU344Z5vcMWcmmJv04MFXbc6SIPDDrNIaE9fWsCziCMVg0Ig7MvGHCA3mloC66bxZSUrEEm-C9bURTf9p-1H5g7kw9R-rTi7Pqas42VC9GFbDxLVcPeUiMbJjEDp3m_6PXfXMdpB6UOdVdmG9UED8UL4NijEEXSekreizoeCJa3r9O7gYi9SiSKI8fRbrQ5BSBB6sNeCpf4zDmn7ZdEWzG_q1ITBCfr7knPXGoS7G6e6nH7TNrsOOmoqYAZWXpBHYmysOI5pw9oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی|تیم‌های آسیایی به دومین برد خود در این جام رسیدند، ترکیه بعد از 8 بازی شکست ناپذیری بالاخره باخت
🇦🇺
استرالیا 2 -
🇹🇷
ترکیه 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/92857" target="_blank">📅 10:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92856">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLiKem_Re2e3xpOso6LSHjq0YyundC76WTniucoXZTkw2NeD31sYTdeBkCiJgen5TNcORZBu8l8i0BRdr3MSTIqCZEgbt2-w5kEEJVY2s1kj3KDtmALIz1oH6-Cahq1-MdVmC04tt2xPHgrtIOkOz-ApuswE4F_Slv58ZkZUCc4fNEfjYiDRw9thODArs95X603kpq-SurX-xcZmNU1jN3gpRPIU-t1MbdjWhP_0xlYPdPnAwJzwYf2i3DJDypZdl4J7XeU5-DafHICr4oWgYQ1eUPRCcVKlmPrLLYZjDtd4y6M09yfcZTj6zI4p7_tBx_dO5fg-AAuPciZLE30Lxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی|تیم‌های آسیایی به دومین برد خود در این جام رسیدند، ترکیه بعد از 8 بازی شکست ناپذیری بالاخره باخت
🇦🇺
استرالیا 2 -
🇹🇷
ترکیه 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/92856" target="_blank">📅 09:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92854">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohI8Y4t75G4PMepFWY8gvIwCt5-pqWmYmg13el9BhfbyElAFsJpxOEwjuO8uSYHqhpw0PQX8sZoANvKlxr6F0RMxFIUiOjt63RYKRyLtaj1WJ93wUzh-ZoAiHA1w77oPjOKT7-cMSHwSzAu11fDYY7gW5Qu324xy7rC-xoywj4xHWoyJB08t1bngGNxfopCUFTQ6qgFnWsKEvUrKdrXXVFgeNgWbu29S67cAXiXmHDmm9TLbIN_PXjZLIGQtZgjUw_zR7xKoJX9Uy2VekhugDILG2QjPpmI0eqxF1DPmvy_0M5afYsuk8BknW5SvcO4O8ND_hAn5fmV3qycn3jefrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
رومانو:
روبن آموریم آماده پذیرش تمامی شرایط میلان برای هدایت این تیم است و تنها منتظر چراغ سبز مدیریت است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/92854" target="_blank">📅 09:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92853">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRBmQdXt2JbVujqKN3ic3VlotHEa41JQu_eMr_38b8wFEc1hqeIz-a5F-hmA_wW3MZ_J84CudJMmQQW7kjemMnTP_XUZ2NV4w19hFivJHafp-BBnRtBW8n8LBREK7bDUk9Morid_8v_U2ty_KoQ7pDQrpi0uLa-RxSji35BDhut3ySYAdwD7ydAClH_nO3w_XIPCMYcDnc7jbtzNf-jJt3euLK2T-MUs7CHrnI_uThTvaqFxwLCm-JoSkBznMEF_ST24AMqlVTI_Qba-lCTrPKNiUzPoKF2uwJqhXERkFnT74yg9teASCw8A1NaZ77Bbix36durRsEO5aM4SI2aJwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بیشترین تعداد پیروزی تیم‌های آسیایی در جام جهانی:
۸ پیروزی —
🇰🇷
کره جنوبی
۷ پیروزی —
🇯🇵
ژاپن
۵ پیروزی —
🇦🇺
استرالیا
۴ پیروزی —
🇸🇦
عربستان سعودی
۳ پیروزی —
🇮🇷
ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/92853" target="_blank">📅 09:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92852">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKw1y6P4rmXuqZSOnYjfsQ6LdlsU0YEqjPdhiqOyOOezRQfdApu_bvf8abXUE83XHI_hgQleA6jhrzJXAAIiCukSiteh0fX-WrOj9aGeF0Co4u7w_bnt8qlZ0qxSvc5rl5NRaPrGLl-N04cbcSr-dBOkGEVtw5Z1DxYndeIRWH6BkTgfiYAVokGqdwyOukb5h5DN4NCy_ycIPhCflR24CgNfQIvW26GMkZe-gPkjaSeRktQ2RgFLxYS72uzQkj8voRzng2vH7ZmwlJafowvzEfIzrp8EbGtUJZ27bugprbJGu07SgLJLCyB1lZzudP_D9qesquBu-beOsEVFJwTNNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
پاتریک بیچ گلر استرالیا تو بازی امروز با 8 سیو بهترین بازیکن تیمش بود
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/92852" target="_blank">📅 09:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92851">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgbKJaGOQqVy9lpSUBMh916NnXUMdHYRCtGhE7f4i9ErcYRsM_sF9z6CzqeONzbp5Uvrcqay98oFD2XrKbGJ2x3lTCNqo0ve2krb7O8QOEEMeIWD87bOU7nMTR_25PEe6OiV3-2ek0EAOOYdW_TpgYMgJHZZgxbLyCH-Ya3jbN_Ch3x0tBayTxeN3VCxLsA1Edc1Xxcf6_RATs6A1G3gwwTqu5KHEKqae4CJWxH3Z2K1LUn8EQChU9mhp-4mQ5F0bJvRm2g1Ix9gqMn8DSTI2_YSWCXhHeR2KGUriHEomJ9FQHhE5lRIG3jIAZVf5h9eO7kyAlKo_jWsLOzFLEuCOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه D جام‌جهانی پس از پایان هفته اول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/92851" target="_blank">📅 09:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92850">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frVC3GNbpFmBWMrl6nLvdOkyG2ZIk21C9ulaStyy5u3t9G_xW_93JQ9lLrkH4aToXHKPNli3HUuwdwX8ctfdyC6SobJf0Je1rZRl9lhD_8zfRWwL5zhWnRWaLhzZ_eaZHukvonfwj9m-J9yhDe31t00ELGnNdogF7MxDCqAitOv2h5poqGhGkuOZH183AkADmZYL_uTZaeCErbjEXFXfuoQ3OFswpeTFlYofn5pILX0eZoKV-0DpW7QUBrxh_AlHH63tuVX1nWtUqcjzovubr94eLh1_7SZ6WDJ5Hu7gTiHTL_OVO1V4vFX2Naf4BlFEQ6hd1c0WYpS-oCR3ISA5hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی|تیم‌های آسیایی به دومین برد خود در این جام رسیدند، ترکیه بعد از 8 بازی شکست ناپذیری بالاخره باخت
🇦🇺
استرالیا 2 -
🇹🇷
ترکیه 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/92850" target="_blank">📅 09:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92844">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H7kEu28YwfrZXY4BIqy4npoDYP8aUBqND4sp73BktMQ2rl1dbhusciIy8oOvrr3YicEzcO1hlnJXJ3fyfh4qKyOgTnIX-lgUl6uVI6eQLAs2r8X6AyabCzXpPAZjYLugm3jeJDk_1hA0nrIBDjYmEu5PJCNLc-wR_XQOu_5FIZFvVOBOJWbir2QaW66XC7GcU8sAiOnakB7L3zite45MgBvzQmwSP8Vh6bdlVST9Ve6EI_KAw3RmdqTtOTBb6pyj9txPgIFklXS6OjaRwIiA_k76TxOiq-0TQ4DDtfd511FCULUE2npDVZGPe8sr0JNjyAOpgGLBv0RkPJZ2nIXuTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eIwpyLNVxjDesfdnL_jSLpW-2DdwHInrs55qT84BOfpPfipKca83T4SWorSR1Bs9swidDbnzOAGwEVbllFhVUr9s_cWgd_kdM86Vt4N4FIOLItm1RfkgPWJPUxmNjscb6DSraOfH4ONolz_5TBAsKJiitKmYzVph9QKd_IDWyt3EhTjFroEQn2rRd0Un-62zPT0sC9HgnoDUdHxL4qxp8oZmctDdOz9r7dfCwiI7NEXy0UD8kj0Gvc6hs_n5QMjYjDucazi1xhxr5HpV7pnR3DZQcTzXppmLyRDZhpSfoaFYHVZnokPPbirVPFjflfKcGRx3KIAav2spP8i9Rh2JRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eO-fdgxjE9CPTyx1CXUEmGhOm0CXUhTGytgq8goldn07kPufzSjjskuvQwHJ7oHY14MBde8VNvVB1Rik03rC03L-Ywfgs_zphU3118Am7E07O9lUOqJMR_0BthlxmrdjgPV8xt3xjVYI7ep37-VJUZMNhh3nt6JNSSesZpehjGm3c75M5r6ttGY63iGU8BQ3r53RMW2KZ--LkxLgJ1COo-pTUhPrQY_VUH8qeQL8AVQKXBPLS7I8TrWfTWWHkJwbUOmdi23CTZWpSDSj9UGpiijsalKD_ZsWRRNA4FZ-fTGBNTAHAGkymyRodl7Jr1bb-ea9h4eZDajOuyVTD6atgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZuBNez2VEt7Ig8EoC3MXYR6DNUyekI8Vy-ftduHTyFv7k0L4Ki8su6SJlA2hCVxAzbMH_HSVIJEorPam9Peni3f4HIAM6KvIkWS1zmqtVBqBoa7gqsQ3U-8YBLxpdDSNCzwqLlpdlV3qoEjayZl7dbLrVKTdXHS-fkAJa2Ds9h7fY1TvZfHa9eQmQLcivNMJynxrWr-JWzq9KmpUHaWOUrgdM25qT8XQEQRBGPDWeDOnHBmGrnVAmVpASsyyxZnoDdPEg-dNHNDXKnY8zYjPkheyJzt1XCPwCLZ8ShPIxdHE_jXdrqOKitdP-2caq5IWPiEPtQ6c4NRzoKJwFyjkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uk81fqV-tY0q7osEalQPGayScPxtB0y0HSDOsWMlMTM3IzajDhkK7r96GUD5_9Q94CYLGfLyCH5_90YZOIBVVui6bolET7u9v9lHRbiBiPAGzYUHXdzhKAQugtf5IDpQf0pVPEwEVthNb7AQR4OuiIPIpAXlLbOkacfcbjzndjywvVV5C9jmQQ9qnBqZg5mt5hSiQvbhL01LpgVkpp2tDumv7MH7L2lFpaboZDUiL5lmt-t5ClKTKRQ0peb7xGAYNZhtNp8Lu2ruOrPL5-zFKQErhQ9zyi6dRVxkYS1uktF-mceprkuOxduVmZ9qbmcbaq-AEAD_sqzcs75YOTORzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BzQ2onVLo3tZHK7ZiVSoES7CYlAeRMu_KThDouAd0VlzyEERPYlCpNjaLzZKdrg5g73wa1CT-duul1zFuIxB2_21_-XUmKR_1mzffDdhod31Zdw45M0iNU5DdwxIYo-cyxFyqZvfTpGv8PpnJdyAWxA_Q5VogPc1fa2TJOfKKC9veGMw2gHC0ffatRKtI_SYYsMIQU9X9Yn1pJHWNwZPYgSV_iH2ADsP4d96X60IJHC2xaqyNWh8y5H5DyT4qU2W_5nIA3x135QKHWfzPR2qnUPX4zh63zlgipQULj7t4nNpTYyIKpH0euJeU3v6dWHbDko-pe4MQ-P8aS9NLeiEng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
استایل جذاب همسران برخی از ستاره‌های برزیل به مناسبت جام‌جهانی
💚
💛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/92844" target="_blank">📅 09:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92843">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دفاع تیمی استرالیا واقعا شاهکاره</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/92843" target="_blank">📅 09:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92842">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db6857d54a.mp4?token=AAB-FU8zs5OeqB0JH6ym6tUcIEHO_ggkgPoDC1AQrbHvhrY9WE_r_UVXOB6EicxOagxNgXAr4j9s0QpRRzVvkvqE2Zz_Olrj3bQMw1xmGQ-mAPCrPOz0J73om5z1D0z5EZz7-pOGku_G0XNac6k1vnVHn7d3F8x6NZHlI0pyY1YVXBFfOm4SeWhP_VYMZlo01ngM5iO-0v4V8eVuJ3DKlHH10j0mRgMp2BavxCzd5BVr6imQN3-XF-g5_AKoOOULPbbftDn5lykSoi-9g0HjdONmkBw66F0v_0TYQctrrBrP-_xq02a9xOVsIcQi7pZMeRU6btw8ZBzLAEsD20_lrK3EJksDob7eEu4lb0y19vwu7OH6xPHug4Ad_AgmgYDl0BNN4Bxblaq_uuGAzfYdjvnwj_zPhiTIkRGVCUI5ACeMrUCgUPQ6vTnV3NYpwNEKtoVdKVGkZimegEN6WEDuOPUIH7iOs8aymk_L_2P6eXqWU_2jFT9f1c3VY58oAvamdber8Wvyx2yo2d-ZhrvbvupFfv9oIq7sTpOs6tc5rkdZ9spLb8HmQUvZPy9DO6XiGbDjnl2KYPqx2g30Oo1M2MVkpUntVPUqY_8JMmOjmMTDbCvfCbuVzLt4ly3LeBC6XbuCfc1EnZXEnk1Rm1cjBpk5f5DWTYEWwxEOiAg9DOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db6857d54a.mp4?token=AAB-FU8zs5OeqB0JH6ym6tUcIEHO_ggkgPoDC1AQrbHvhrY9WE_r_UVXOB6EicxOagxNgXAr4j9s0QpRRzVvkvqE2Zz_Olrj3bQMw1xmGQ-mAPCrPOz0J73om5z1D0z5EZz7-pOGku_G0XNac6k1vnVHn7d3F8x6NZHlI0pyY1YVXBFfOm4SeWhP_VYMZlo01ngM5iO-0v4V8eVuJ3DKlHH10j0mRgMp2BavxCzd5BVr6imQN3-XF-g5_AKoOOULPbbftDn5lykSoi-9g0HjdONmkBw66F0v_0TYQctrrBrP-_xq02a9xOVsIcQi7pZMeRU6btw8ZBzLAEsD20_lrK3EJksDob7eEu4lb0y19vwu7OH6xPHug4Ad_AgmgYDl0BNN4Bxblaq_uuGAzfYdjvnwj_zPhiTIkRGVCUI5ACeMrUCgUPQ6vTnV3NYpwNEKtoVdKVGkZimegEN6WEDuOPUIH7iOs8aymk_L_2P6eXqWU_2jFT9f1c3VY58oAvamdber8Wvyx2yo2d-ZhrvbvupFfv9oIq7sTpOs6tc5rkdZ9spLb8HmQUvZPy9DO6XiGbDjnl2KYPqx2g30Oo1M2MVkpUntVPUqY_8JMmOjmMTDbCvfCbuVzLt4ly3LeBC6XbuCfc1EnZXEnk1Rm1cjBpk5f5DWTYEWwxEOiAg9DOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇺
گل دوم استرالیا به ترکیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/92842" target="_blank">📅 09:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92841">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پشمام استرالیا دومی هم زد</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/92841" target="_blank">📅 09:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92840">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
پشماتون بریزه؛ یه پسره ۳۰ ساله تو یمن که بهش میگفتن مرد عنکبوتی و شهرت خاصی تو صخره نوردی بدون تجهیزات ایمنی داشت، چند روز‌ پیش موقع انجام کسخل بازیاش تو دهانه یه آتشفشان اینجوری سقوط کرد و بعد حدود ۳ روز تونستن جنازه‌ تیکه‌پارش رو از اعماق آتشفشان بیرون بیارن
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/92840" target="_blank">📅 09:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92839">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">استرالیا عجب اتوبوسی چیده</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/92839" target="_blank">📅 08:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92837">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shg9kgJN8p3UOHTUe_QMTriiNVhUkQdPq6aWSmdB0Tl2MGM_Uv-hlLSJ5-_6AX0kxhtn1OFqRJNFD6wXdswAwItG6W940UxH-BBKSxljsIKAIsLd-K1J8CFtKbFg_ufTBQckXAgzD9pT6ZDfNIoDQDLP7Y6s67nKmwbsqLBXCCxdpN8NyrLinRCcvvrEoUmgbe3ki5gx8M9Ynb-kkk_azoJ5aU6Hdp6Q9oFpiCgYQCXRMAHq32D97dycIoc-ZPC-61AOA_5vfZiqJJo3PtTjBpMzQsNnS-DnvRgS0JW6A_GFZIl5AnM9kgusWJHrTXU6s47e-ebwrTKnG3S-87im1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحنه ای جالب از بازی ترکیه و استرالیا:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/92837" target="_blank">📅 08:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92836">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترکیه تو نیمه دوم فشار آورده تا گل مساوی رو بزنه</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/92836" target="_blank">📅 08:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92834">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">شروع نیمه دوم</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/92834" target="_blank">📅 08:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92833">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMJbRIcKQ4jDVAYZBBoBSljtME1_Jk2Tub715kjCgdun6_R0Yp-MNzrqUXBeoZTq4O0WuhMe6WMZpUZFDsdwLsVbJIqhTFA8WZZIFJta6Gd94wj2ER5QCZyDku9_h1DG_KFj2mmNBzHQADPHy7Kg5g5tvRYkcek4coF7yF2_3--fUhT_9mut8nVl8rC7ApgjEoWyAt_R_eD--h53ZZ-wyCDq3uOvXKSm4QU4jRkTOt_o3mLWYVbM_f2SWMNNqNc47Nc6X62vcYRBBUC8sZvugF3a49bVNUqP8oXsWZ61B2Nqqnc3hMSYLXCR0f5-TReLyV3YighpitNIPoTIRsdbTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نستوری ایرانکوندا با 20 سال و 4 ماه به جوان ترین گلزن تاریخ جام جهانی برای یک تیم آسیایی تبدیل شد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/92833" target="_blank">📅 08:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92832">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پایان نیمه اول
🇦🇺
استرالیا 1 -
🇹🇷
ترکیه 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/92832" target="_blank">📅 08:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92831">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHWTZ2mgp7ocExsb4kzDxnXlNmpUE5Q7miaawmQhVNcoqocKd-hmOE_9mp9LUqv3_PDt-K1kLoERqGK67QS4IPMPT9Z4Y7cuprXILYg7oxhGTwzOGaF2n515fDcaRw6vWZQN8EQ5WBYkSBfTpqqZ7RsIKXJC6YQOnDBPbrmuOqT40oPmMEzA6lA7G5qBfxLmm2YwVR6GsP2jpgCcRay19drpfmdP9Rv6D8FWSSwzkIaWLLQLaEy_Epxh5J4HH38ZzU2sQFp9oTpuxkup1PwOfI_oZKfwSo0OrQqWH11SBZyev3PqvTwRkkG8Znm6EuWzO-IPQWjz4Xsr_5Tfloo9yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇺
خوشحالی ایرانکوندا به سبک تیم کیهیل اسطوره استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/92831" target="_blank">📅 08:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92830">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29527446d1.mp4?token=HFRJwGMagOG53OYiodAHqhBjkd-Dm9mTLTVNUQwx0QCeyXnehOoAy4W2HnEcmrqBTtTjaRWVBa10HdXR7Sek-90sr3skvJ2_M8hh-C2s5gwDKZFX7sLRd2yNc-5x9Q6XYWWwhBhfXw40VObjS75rwtli5GhDC4fxmnaIWyCBtXoAzH7Rp-lpTs_M2vTFGQ6srUdCsrikiXT21KRONXkuxxmSUCcstHZSFj0UZpodLNcExqgxui3cKgIUlvl4ekFVb2z49QDs-CxwpD1WEd3GQxjc3x2GLS1IazdKYlBZG48bTBAbSMunjM3mh1Eejt3kph30LA2Z0nxmtXm1qLmG0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29527446d1.mp4?token=HFRJwGMagOG53OYiodAHqhBjkd-Dm9mTLTVNUQwx0QCeyXnehOoAy4W2HnEcmrqBTtTjaRWVBa10HdXR7Sek-90sr3skvJ2_M8hh-C2s5gwDKZFX7sLRd2yNc-5x9Q6XYWWwhBhfXw40VObjS75rwtli5GhDC4fxmnaIWyCBtXoAzH7Rp-lpTs_M2vTFGQ6srUdCsrikiXT21KRONXkuxxmSUCcstHZSFj0UZpodLNcExqgxui3cKgIUlvl4ekFVb2z49QDs-CxwpD1WEd3GQxjc3x2GLS1IazdKYlBZG48bTBAbSMunjM3mh1Eejt3kph30LA2Z0nxmtXm1qLmG0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇿
گل اول استرالیا به ترکیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/92830" target="_blank">📅 08:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92829">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">زننده گل استرالیا اسمش ایران‌کوندا هستش
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/92829" target="_blank">📅 08:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92828">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بازی اونقدر جذابه خوابمون گرفت</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/92828" target="_blank">📅 08:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92827">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گللگلگلگگل استرالیا زددد</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/92827" target="_blank">📅 08:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92826">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">شروع بازی ترکیه و استرالیا</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/92826" target="_blank">📅 07:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92825">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bvp5kySwPbOHHTt19kUcSKyvLBgL9OeuN_gMByynZqnqlTtDLukZT2EpZe5D05r58Bo-5maZaiobJsafaFxi_2f2EYjKNsSuF6AYwkttYuWT6YrPAhmiZlDgplRr8doy5Czhk8fuopeEZyOpVKkoFsdur2swVm-MzZ1oMSHsVqICBSNw7b9X4XAq1juVbhicPpe-FUYUmQJu2ambTWVm0yTFDvq2RpXr30JXPScjmnzorOA1wLCRqzvzbvkXtSjdX9odfOm9IQz1xZnyIaqXut1ecZnjl0FRDwoygnCfYVMZwRSbWlu-60MlI43UTI9X5iRUtsxjEaYGEySnnyJm_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استایل عجیب هوادار ترکیه ای
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/92825" target="_blank">📅 07:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92824">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">شروع بازی ترکیه و استرالیا</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/92824" target="_blank">📅 07:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92823">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIYU6ZpQdKMa8TBg7W65T06a8LzUWz4NqKewFhGZbcKf6B6Z-yUHinrc6-C65a-vxKvPisojfy3suiyuqhI9U55m_pt46aqYKbCOsO-t1lF-Ytj6lIzYgAjAGNM4J4hirVtTjQN3K4YjiBBq7V9ueqvEbhgNnMdFbkmRP4T2SrjLspQvrb3XbS4F6Wk1AgwtQCkXhsfHH8mAoMSr9vQ43KmV4sf8RvCAhxa_AG-EqK20Loo9Y0epRaT5HVNKHd2BzTzjWiJ5YBnL-yWzmkrxLBKvQQ94HAKfnL0YpmAsCiB1JsQpfjz2Z8sFqbZfPXy423yVJoaCETXaFjE804c5ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇺
🇹🇷
نمایی از استادیوم 54 هزار نفری BC Place ونکوور پیش از شروع بازی استرالیا و ترکیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/92823" target="_blank">📅 07:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92822">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhRiWEgYsBmH2FFW5M0-LGp4oTZCvGYpNsDqZEiEgPz_G1A_5XxHNBlJN0-9dDbe3R-CJ-elZn7PGn8nv3a1eqyOv6hjtivpBgSQER-kCvcn-JyJZ4kGgFIP3mT0695YZWz8kzGD_CshqZ-mABJ0mLECrH2QqAzn8j_iD5gPHEKTGl0KCFfxMeJqF9HQi-6HlZ05ilNef_tYtYhbpj1CNpoBtHVFoi4VJetQWvtNf4VdDhHEw2dNvNCDNdGZ71zoiIopkMNax7an1746TN_ac7ITratDCjouJ_eR6o1vWh3gFV5Tf8V2BhfT6MOWA9Fb6h3vFpiCtIHN4r-wGM81Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁳󠁣󠁴󠁿
گل‌اول اسکاتلند به هائیتی توسط جان‌مک‌گین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/92822" target="_blank">📅 07:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92820">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Epvw1MmRO327R1yN-_xGmY9SbSW-mWybYc5a5CMvBmDiGwx3VpSY0A2pnAfNDQf3o6cDrqu8AB_kvtQlyMIQGNOp4Sq_7Ilg_XBb3ucK0cWVJqkt-tyVnc2rsnPNgmFWsNnJ0NRsp7ld72aOcmXrtIt9pYOsmVRZeeb6E081Rra3xGPzWDNZxYspZhiIQacarYRKPzwOfp6ThG2wCK9pLSv8BHZQn-eF9tOloNQin4g2LEtvWFpwb6WyWpdsh-GTQYVUdZ5CpGrBFyXxV-TfHcY5YDLvW9lGvENyW3-NhQ4J6SPFrxhV4yw8Y5MDcGH7FHk7o8tkVbN7hkJog6hJCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Arg_iyujsM0jwFlYQMqFW9J3hKvTCgQjN5X0D3CAY372ndeIHatzaO86E-C3tTN4L49uF8E1u0R04NBUMr42QqVUDlJtT9zpLhUPPsroUTkxXBiy78aCVgvydVM_PSh4eJk_BkCpN3pw3ZnNuaZ3phiNWN3PtrngNTaSljxGg0gRauya5a_mYhfHMNMnXEkggYwlSOuqPjqISQbosos_wHu90MveJGil43fhNfYnEP-iV2ueYpawHFMKf4r3Pp9vfB3ZCzWg1kdaDGmiD-hwkxln5aKB5Vrm1cEQvgu5Ty6mCQWPj6iaLiX-6r-jWTd5qsggR2liG8ln5AkFYo0S3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🏆
ترکیب دو تیم ترکیه و استرالیا
/ساعت ۰۷:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/92820" target="_blank">📅 06:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92819">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">این بازی کصشر خالص بوده تا اینجا</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/92819" target="_blank">📅 06:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92818">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJ7TNNvfIPvM5i06TQ_sT2pXpFTa8lBkYKl2USlrrj1E-MAH861P9QnmoESkWphDK8EZG9hp-KLS9KQgQIX5hNQnQxUrpYZj33DKYgQHqUSIrSTIMZk2c2G24vqukfNUGBBzo8d4SACXloMd3ZCsI0FQnPaWm6U3f7lKblkwWGwleFTtoPXF4O3baMHp04BJKkls1sZ5thSLUv0Y8LuqqBdeZ5bbt_UWoYlihAkhBIlaqPlcqAQ1xJ6lQGu-CcOOoOQER4IflRU4WIBiE8Vwf0RLyA8bPIRmglCLtMctmXNucAyHDFnmbYf5whXVgOoGo5TudebUpTco3KLKyurhfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دوست دختر رودریگو دی‌پائول:  «بعد از جشن قهرمانی آرژانتین در جام جهانی، رودریگو مست به خانه آمد. من مجبور شدم مثل یک بچه از او مراقبت کنم چون نمی‌توانست جشن گرفتن را متوقف کند. به او گفتم که دوستش دارم تا آرام شود. سپس او پاسخ داد: «من هم تو را دوست دارم…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/92818" target="_blank">📅 06:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92817">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-pYTTi210vygWzZwCBjmRqz0_0Ie9hvL91CUUFk2jRbA2Ef1VQ94dBL9yaTmwaaM7lfj2SW1T3QkKwg1O9v9Kwz9_KhmCdIqKR9hX8YO2CJQms0e_pRSAzcibQKxisZ6UDRP-r1lVeGaZu3imey2xJMs7ZCYlTdgfB_rRgPwmXLRIwN_HFc6tvw7bJZ-vdOCGeHjH7ppO0gxAUnSo9FhVmrscI-O2gPXhYKJUSjI2QlF4Gle23lWAdFnLv0NU7BXXHe2TuSnQJZT9M7ozCLW5yGtSRj_g6R4ROjDp8locWoIkxEggMT38taNWz4yQBvsr7g9v1hgTnTIyuG9dEZbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوادارای برزیل دیگه خیلی جوگیر شدن و اندریک رو پله جدید میدونن
🫣
🫣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/92817" target="_blank">📅 05:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92816">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcdOTswMXmgUzWAKAKslXHIPPJ3EDCuI4VIpw7U-69KWIUcNT5Tqdwn5vjtWqMzoPbFi1pkjl4dedtmcg3YNk4PZQm9oLxCTsIRb379GXWVtTw7FqKKTvLNU4idYb30SA_QNwkghy-jdx7oM2NyEcAHCp4MjFtaRzpkkxItmo8e85MmiU4qDYJ5-f06SNzWmwKHsnLJIW4Gp77IbwaAf9l_0PBBJm2lCAoli-bl8wCOs8fx48YDcvxRaxvVx4zVVcRwQ8eB9pujkncQtCrj6CFxkQxWZve96kvy5PrKTmjp5w3N5QGevgLQoVKrBX9WhWQgeTLZB2WmDvgfxeSFzIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴
جان مک‌گین اولین گل اسکاتلند در جام جهانی از سال 1998 را مقابل هائیتی به ثمر رساند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/92816" target="_blank">📅 05:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92815">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🏆
🔥
پایان نیمه اول بازی
⬛️
🏴󠁧󠁢󠁳󠁣󠁴󠁿
1️⃣
🏆
0️⃣
🇭🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/92815" target="_blank">📅 05:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92814">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0-XR2TYaOx-bmnT01ZlORYXA37NPw2-XLQCoets5trbSDbWt43mzZ6GNwtgSIEIsGjJ45qb6BjbE5BOLAMlDad-nWmvG6RET3jioqtIxO4XjoYEiVXFMCf_cu5DY3IC45E3TLqJXp0-29y6x-_zq215KNFYVi4npejPk6hG52s6zjLSyheIQ7WdcftDOZdbpFWo2fepgJQpRxzeRgdCh9ZftEMnQ1z7RfBHogMU1spc22v48BGApHObiyZCYVm7kChrCATuISB8EoKg8oTndEEyJrhbmQkvS-P37Fus27dlRyZEFDBdmTZlF1XZYPRC4EYyb_k1qDxHJTXbPXUqJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
بازیکن متولد ۲۰۰۷ و ۱۹ ساله خط هافبک مراکش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/92814" target="_blank">📅 05:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92813">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93bcbb2b8e.mp4?token=fFSQIOkatVOGT4Pt88kcT940qDF1y0V7ViumPoXhn7CqC3jbsPINyP-wRpw5Ylkia-MFx0fckqZpzTnH_9SJGXDJ6iRbt1UWd7Lgd9Hc3sZ97Rk0Fy45DKASs-AudRTxZ3Gc5olvtawryLceJkC66Ak7OX9qCIDw0JV_J7Mj3QM2HsU_UX4fFr2-P7mTS_lvLf4pwiTPA3NUs_mHJYiJaHCM_PGugCpAMA07PkIckL4j_Ta6S3yIkcdMAnVvGaXVaXcTo0j7rkvfh2jlJVavzlQE1kkEFaN9dF3eW5Oq-SxznX8C3IetLjk5viQJPb0bAZY2D_CZkbAHOO5HDAejCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93bcbb2b8e.mp4?token=fFSQIOkatVOGT4Pt88kcT940qDF1y0V7ViumPoXhn7CqC3jbsPINyP-wRpw5Ylkia-MFx0fckqZpzTnH_9SJGXDJ6iRbt1UWd7Lgd9Hc3sZ97Rk0Fy45DKASs-AudRTxZ3Gc5olvtawryLceJkC66Ak7OX9qCIDw0JV_J7Mj3QM2HsU_UX4fFr2-P7mTS_lvLf4pwiTPA3NUs_mHJYiJaHCM_PGugCpAMA07PkIckL4j_Ta6S3yIkcdMAnVvGaXVaXcTo0j7rkvfh2jlJVavzlQE1kkEFaN9dF3eW5Oq-SxznX8C3IetLjk5viQJPb0bAZY2D_CZkbAHOO5HDAejCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁳󠁣󠁴󠁿
گل‌اول اسکاتلند به هائیتی توسط جان‌مک‌گین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/92813" target="_blank">📅 05:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92812">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گلللللللل اول اسکاتلندددد</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/92812" target="_blank">📅 05:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92810">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n22HBSgvYmlAmbHVSZH5H4RuQ7LPZEY28wIZD2-wgchQy22Pdzo9fs6PDuciUE7xOsQ3FSbj00-ulT_ph6t6PB9Iwse5Lb5ALTgKail9WqEcjwrwmksyZOFA-0FlLxF7JZJe9KQWpSdOFoIErdf40Wwf5tLCTdnDZJZ-pq5po2j9VU3pHYMXRfRoL8VlOBs_G8Qu7ZHvRh0sKIkp8vc5UnEN6c8mOauKy3oixVxF4HlThxfJZ8B2_mhkN7MOXuKqXAjPSpoQH5jj06U6qfQhS0yZIr4yDIa9VDmI8bb3wqAJnlHzdtC92_hH1uVBuQfuJmonOEKs51tVJfFXfYbTfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cRkgOtT5XTHDjI4oJhYTfDkpyTG9W-2iz2FUXf0b0CdZ7EH2wjILuDUDs-_EqLLSVZ1A1n0K2Yuz8daU9mT6rFd4aBJLyS2pGw9mtu-152t5SMktULSQuSUoOm-W363rsWlTm9I1UVIQyOn1lCtlBgZgTz2j8_p8hdn3DlTO85XsLVJSdijSJzot4ZFMYdvwDRJh8Tw0o-t-ygwI9_YorfEn6kzUGKUmR4HR-lLUUCDZxKpPBH7TAM4OOynGRr-N-vBCQNqLU8QCl2wvLTolJ63JGiZ7cRJDiLbkKV-BL_Wn2ZWq5xabw5G4kSDgTYBjnYZsCXuJJ7x_sMZ2PDheHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇶🇦
صندوق سرمایه‌گذاری قطر اعلام کرده که بوعلام خوخی پس از گلزنی مقابل سوئیس در جام جهانی، 3 میلیون دلار و جدیدترین رولز رویس فانتوم به ارزش 550.000 هزار دلار رو دریافت خواهد کرد
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/92810" target="_blank">📅 05:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92808">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O8rB0fpRY8c6p2Tug35BPlZz3uOXwNBJa_Cbs5CFV2KCxqvmr-V_bc9It1ttaEHXoTqR5S80NmvUS02DpbeMyAVjF6HqoeuKUIY6u_poxvrML0DYtGe3FOcg-yXDIup2HpBJrJkiA8IeUwQfp4TROOLLqn-6Ih-KsMCH0hW0IRoOHGywa7-VL-HP7ltOClEo9Q12ID120hXZuHkF5FULv3NxBTJGFrMFVlo5eMWzss9j3UgYXvOoEnGSAbTlB75VLmj76U1ap24PLFSdN82OOminwjlDlHlSRhXFwaOiMWo1ZsbEPPE-7jk_lxDd_wGNqIDG-ByNI_6p9xvU8FuFfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WoAeikRjnllgGjLr6fOTOckde2AjsfqNK_e_SrwQm3uC8W2DsdnGOmvJ_wS_H3ahgpx7I4tozmn1Ki-JLOFDC4frM5wAGnoRtc5kwt-BFIMOdyMIl3cYd86Oxw08P-ysNvIW9_mg-ETRV_T9CURskrQ4420aNOzmKsx0O1SWqexy6nVs9pF7r5J98-ReGSb75t4TkgBx-KcOorG0F1bGHAhnTRUD9KkLNt_yUN3y51dt9rsvmr86ARbuJ32PAC5-XtdybEW88UzR2r1LK7xE7r00TPjlEqtTvdAwybaplNSklFvBRkafQT6g2qcqsb4-O12Q46-_8fJnd2cXq4zmCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جو ورزشگاه قبل شروع بازی
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/92808" target="_blank">📅 04:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92807">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بریم سراغ بازی اسکاتلند - هائیتی</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/92807" target="_blank">📅 04:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92806">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-fjSkzaf60wGFvtZi4Tr8sRfVox3qaBAKveSo8UP-2azXnRe-jYHE1C7letEkteNeaLoqcrghEkueFhT4hyGuh65h2aH4porjd5ZGYfbSDsnuVW9VeUeDvRCcSbBrCZtL4ss12pcA6ANhcLEoTjJ-yAF7jFEwhN6u5z_n76HVkDyF1vHw_YrY1lipt4XOma_M_NU5xA3Sd-M8h-GTINr8Lt5byG6h6L-US_dR4FzSDEjjbpd-3o9awWwlfAgQnQfCWgkxDwOH0DwWOcVikVsexlkbZshtDZmrqHQ39XQbM64I4JQGbSuCZNSm3bKK8FtkVGyR9xfhVQeOZeo1Iv4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین باری که برزیل در بازی ابتدایی خودش در مرحله گروهی جام جهانی شکست خورد به سال ۱۹۳۰ برمیگرده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/92806" target="_blank">📅 04:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92804">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oyUjeYv3i54sLuJrUJ2ts5wAqAcclrwxR8HaE0i2uLi8xPqppqK2Skq5IRRhYxYkSzByI1ejhBcPuXl8z1R7_xStvGUGwABXs4yPtQ9mUuZ1gycKeoQb2KWlZV-Dsa8NcZekrXJb82lQD32Lm0IbFfc1Ohy0PTAE09FqQYm2y-aiuoP1zigBo4Ina1dMyAF8yDBq-PZWUL0ioqPPv3LK_x_YCZzV3KyQFuz5MCaL-8nsVswMaQlCdWFY5nadpO0xZdfep2PAgnlu4YANVrBtqWrgb8QuoWVifRly1NaiWpfGBmSIpo4wE9T7gQXyPgVLczEA7NbzgA8X1mcQmerMeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aI3mLAr0NGh11ZZuw8uItQ6gPKdAqMbHQ-RAsTgIdstglZwYfAHs4ILvoVWLH1x5xTwQlQdYtl2FydNZqf-kHxMKq6kP-XjIFu5gOKt34I47s95NfqG1Lb1FgdNn5Z5cGDBYOdbfu3gbuUBL8PFV_de8ycZBa7Qlel3LrC_IAFmDJ-1B3vjMwMDxJunq70zqCvQ136L8RjWcaG0jXnOJ_QPzpyY-JtiPO1heczCXY3Q8hw_cK2Fl6efNbSr1CfuSNxkBHKWsFaANSu-FgigZoP6m8BRr0n0PA_im9n3pNQrfQbOLTrDkOdOiJYiO5MAH9GDCTTAFCwW5rhdvvl4eWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
خلاصه کریر اندریک زیر نظر کارلتو:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/92804" target="_blank">📅 04:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92803">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPt-f6wRACkKOLVA3w3i8og35fG8LMDlhDHDfS48sabiBSY1zg1trcCsJJbejf59yJMjQKxk4PgnmQzXLvy5kV6kjsEgDaUaj9KGrAb6ZcSNV3oR0u1zqOlx_ucFs-XAuij2MWy9ysmbZNJvPsiwtcckxpUTUjETqpNg0ozGHvyLRqz4hjBAylS9aZFIistOP-irqmT1nRPRNtLm9uS6vCJh5ROIAUFwZ-xZL7G9oCr1wBIAdlDaZyvvDJFzMz_YbzgoHXJ2Mx_s_hKMlabTK_wDfr5TouP6-NaMMD9jrxX0_Gpl7R2jH64nLx4FxQz2utC_T56jnxRFPwVfCy1Osw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
🇧🇷
🇲🇦
آمار تقابل برزیل و مراکش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/92803" target="_blank">📅 03:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92802">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojp1D8paeEifEzGxNljAVIpqLhBHK0DUidjc1CgI4hTaCpQP1DOZPD2oEt8Bv5xTrtCf1PAHmCfxcq6NbCF7v4lJNYA09OvS_mFadRMEFZby7WLRu57NKDDI_lZUkzQ0JvWPw1QOIipi9pxnr79KLP3cEwygdhOw2tw64hXNNW3G8ihAjdAdP-l42FiGyM8rJFMeet7PJcVUetZPe5XzcDsVSP88hBYsAq20KAHGXAdOqOKEEgWFtvX1HK04TeXGV4bDAjqPvSfO5IuX8hXBbwuXiZOmgZYNKS7Mj01JLdAHgtPAlO-DCLtMZkWgSKAdFsXMB-4vlH7cCThbBDWsnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وینیسیوس بهترین بازیکن دیدار امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/92802" target="_blank">📅 03:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92801">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sH1VVhzm9KUj0ZIJIY0CNB4KdB7FMuqUSNyxnTdORehe9ShVmDJSpo8dPWT0QFh5zZH1qPsq5RXxAGWTvFDItAItjmbExfLnH6ldkQ03Y2W-7jACWdvF2JLCY7EUad1g51wFSLegrhhICeiS4d9KbCXicjenHy7Aru6mQr1n55vZ9fWs4Rz1rgSare12Idct8IZcsvRUbnUX2_GIMgiNSDmkUQZbfUatjcbbdFUtudFc8QU3ui3GNaQlNZoJOo_hHiyEpcyu6Q9XSwraNASrbpxa3BjgIon70RQT76uWieeuUKcqFFn5pdlJ7cI0tFlj8CEUmo8zChr82pUWPRHu5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نمرات بازیکنان برزیل و مراکش در بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/92801" target="_blank">📅 03:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92800">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">شب خوش کونم از ته ته داره میسوزه
ولی بر میگردم
😭</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/92800" target="_blank">📅 03:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92799">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwjBNWCsPWhnhcOsXdJDS_VUnmX15eY5JqVt7uyEgT6QFeksKJyhO_jTTvG5NHfIhr8RjoZdDroXSqsk-4PQ0AE07yLw5p8ZwNG9XQRKtp3ew-AKllll7hEaB_xydhdtKikh6TpR8Sakw0GwmHI4gQQ8nk7zUdFdbpyay0tFwOiCfZa22e2b8Ros8Bz_IyKH6ogGGE2kLZ7GhXZ5m3URnLsDOwz_jQUS1JZnWx9ZKMQGdPrDUYVCQ0Qf_NUgapTrTC4likIkHkF2yQ0v04cNZfh-hfQ9goW_9ZwyJyM8wU8lLbBVoA-qYfQUflefw-Wkr4tkq3jrfyFnbOlYDdWwfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
وینیسیوس با تعداد گل‌های رونالدینیو برای برزیل در جام‌جهانی برابر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/92799" target="_blank">📅 03:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92798">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QL-35NIngBMcMYjfI1dEyVUvsUgseyIzSo4-fjYvN3SxULAqi9fgFtv78IPwjuxVRKb3OvUdHeQmYK2aRtiSAEPRfYDLhpBjCflqN-B4W_bI-htp8i_jrTgn1wX8WQskaJsBG39vHl-FcwnXmjJeghHk2NZ6A5shGjHESYHTtcyDamjzdrC-GrCr8Hfyfv-SZkJnYcuG0-lRcCwhGR-xTQ--6sMROOzYcvzT7NCkNgPo6tLGqX1ahm4J6nM_GWvr-v0MsX4GY3BhkkXBdmCb9x6y2It7ZYh0NpOmBq-8bu8J7JQwrie5ai6JrIzgEwOncGucToB2Z9mSrFIAc4JhtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی|نبرد هیجان‌انگیز نایب قهرمان آفریقا با مدعی جام در روز سوم بدون برنده شد؛ برزیل برای قهرمانی در جهان نیاز به تحول اساسی دارد!
🇧🇷
برزیل
❗
-
❗
مراکش
🇲🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/92798" target="_blank">📅 03:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92796">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ARkEAPvVaWR-IONODdIeYghURa_ZHEV8BVjWjJIXLkg9eXu_jXm-kEpdSgU5a7Be-nWPU-CMr7yVJ-Y29mdi8U_uNlnH3Tfh6xlTMaY4eBbmXUhhTMX1VVDf6rj9xlTyHYE91HlG95ZdoQb4y0FPA3MhpJVYT23VhMbjLeh3RusG_NDCMe5brEqpvlInoSrGjfb3b2XBZ2oluHkJjZxmmtOb2pA0c8nJwdwtwBw-N_GwfLsaDjMsgCFOadIfc5wS4iSi0Kmz3945tWNL4N29VyFmeumf0J4RKsn-xJyaiweD7MQ6mAYsa8D83-7arh9bHGuss40M4bkYDr2gb_HYYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KRmI41q11kfYEYfruO3LpFHvSeXVP4mw7tXkCc--rRFFlqxpI91dLStH3jH-yBJHb_rdKAapIX6_EoukzlqL0p2gsCzuqY5rSR858b2tQr4OmmvQrVJKmKSAg5GaR6B0mS0Qxr4n_FzpAgfqYwQXdClpmMKKdv-dWku8IGnFacEEQehY3T1JRD8kxm9CUMGp0eptVWko_6XJ3N6mlb4ueWOydm9bnbHVyG_3xwFg5k0U5yqGOJambU0WO8SQQnK1SJZcsE58U2HiI2s5lqdXxo1-O2sYznWHetRimgeXo_2hzse6sX2db352FB6_EGgRz2jm1h3jTyU8WXH3iSBcHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🏆
ترکیب دو تیم هائیتی و اسکاتلند
/ساعت ۰۴:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/92796" target="_blank">📅 03:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92795">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بابا بزنید دیگه
🥺
🥺
🥺
🥺</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/92795" target="_blank">📅 03:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92794">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ee5b8e61.mp4?token=f1Se9ol1l5Yt2bnYBpzenjCqswws3NQo5dNEz_eGALZfsy3oCUeOWBUEeBF0VdObE5VMT5X6r0XpPrvjzXe-XPJ66RSTTfPiLL9kb5DGPy6NvQH-9faZiLn-yoVuB7jncHWrWXqn-olaonqNIij0_28jvTnMD-w3LBra9OqZO58YxfF_vhWRNWI9bWgV3qb27METy7sm19flUvnUssnCqCMZpbClKzjDPI_kLJYLRXNOG9HIahEAvP4jYmT79g3SIiBQCEKqVxr07GFbmh_b11HvX6IWcOGVIj8RXNHZGj6oIFUyQzmJRYCwGoahN9Q0GsaT29mXFoSsUD_Khmia2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ee5b8e61.mp4?token=f1Se9ol1l5Yt2bnYBpzenjCqswws3NQo5dNEz_eGALZfsy3oCUeOWBUEeBF0VdObE5VMT5X6r0XpPrvjzXe-XPJ66RSTTfPiLL9kb5DGPy6NvQH-9faZiLn-yoVuB7jncHWrWXqn-olaonqNIij0_28jvTnMD-w3LBra9OqZO58YxfF_vhWRNWI9bWgV3qb27METy7sm19flUvnUssnCqCMZpbClKzjDPI_kLJYLRXNOG9HIahEAvP4jYmT79g3SIiBQCEKqVxr07GFbmh_b11HvX6IWcOGVIj8RXNHZGj6oIFUyQzmJRYCwGoahN9Q0GsaT29mXFoSsUD_Khmia2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی برزیلی‌ها از گل وینیسیوس کف سائوپائولو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/92794" target="_blank">📅 03:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92793">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Du_L2ww82aHz7K4vl9GK5SIisVRkV4hAbJ_bkWntYhniSkadi97r6Fvn4qQN1uowx506O2z2o2_P0w4kXmZEy759ZW8faFKNmHHJM48_87zC8lDKTdy2JMGT6b2eLuLbSHVwioUkkyHByIovr95KG3UcKkiBOx4pz3b0fvzlNdMJ2EznGefBvVGigl4DiEa_S-t6OOFDmWrMHb3Wttu_FXwyln9NIj6EBGjdsvD5b2pII3jpvRFG9oa8pCl6a5BJYFs7vEJ3T5LGiLMcM_DaAi_K0IFeGqoIa8R-wSNkRtgeZqoD8XuAeC3-arVIaz2UwifkEAy_14K9UviTTSO5jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
بازیکن متولد ۲۰۰۷ و ۱۹ ساله خط هافبک مراکش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/92793" target="_blank">📅 02:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92792">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9d20b3cd9.mp4?token=RdAQSv9MRgx0vKLsR8wxoRsVvp2F9R36a40l6zdojcLEBY391ZSeAuEM0k3NxkUCzOKGSlMji8xoMbciuh5LkjHXi_BZeeQXxpPlufhJf-z8mYfEV5XtkX7qN5TBkPbaN9LuOYWYIVnkp1BObWH-JXQdpTSPXizkCc4X-KkFtbG3l14YtsMjvQQb15czKgxOpJeL9YqkGJAoj7v_FvZSwgVLeO9rslTviDgbv1jgFksNOSEU3vD-uElCEPhSU9GyGvYASL4HR08q2jUlQ8AupJKFZbrwUNoLwhRIuzaH_usMZK3zu8McLSD6RNlVFcoC6bfIfC4YXGq2mJJmewJn8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9d20b3cd9.mp4?token=RdAQSv9MRgx0vKLsR8wxoRsVvp2F9R36a40l6zdojcLEBY391ZSeAuEM0k3NxkUCzOKGSlMji8xoMbciuh5LkjHXi_BZeeQXxpPlufhJf-z8mYfEV5XtkX7qN5TBkPbaN9LuOYWYIVnkp1BObWH-JXQdpTSPXizkCc4X-KkFtbG3l14YtsMjvQQb15czKgxOpJeL9YqkGJAoj7v_FvZSwgVLeO9rslTviDgbv1jgFksNOSEU3vD-uElCEPhSU9GyGvYASL4HR08q2jUlQ8AupJKFZbrwUNoLwhRIuzaH_usMZK3zu8McLSD6RNlVFcoC6bfIfC4YXGq2mJJmewJn8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
صحنه مشکوک نیمه‌اول بازی که اشرف اخراج نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/92792" target="_blank">📅 02:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92791">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/92791" target="_blank">📅 02:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92790">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tfxWwAZfiJ1JwMFV6y9jsyAFu-Lbjsa10DqqqXz3EV4qa1Gw3rfoCihwZeLM-9himvcxuQMJlmC4d2UytgUa_EmsxuDJXO_t4DCLLtLYeZV2UPmdHI8kqpqNia5v84iz-Z-_T-h5zplIEb5SDTKXbrKLsLI-bzt8FXuqZt82a9w3AnJ7DtC1prsafozyI_w_9HId3kw7F_fvgv0x-kNHpK6JBL5G-iQw7I0pZDn58Vi71fgzj-HQzJWTVPKiVskUN5Y8z9DSvJx6gCveATNIM41DRmzFVgqzAeaTVGNMiWimOmR0i2a8LGSCAWwXVQFLkSuFI0JGIt-IsZk3ujmU8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/92790" target="_blank">📅 02:42 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
