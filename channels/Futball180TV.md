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
<img src="https://cdn4.telesco.pe/file/tlyKg76lpw8Dwz9VZcua3ejW6ZAgoBIZWmcmyMxPLgvRAiKIIB3RPFsXSUyJD3943lL8JfUwepa3p0I7HGKOFvuypCu04HQOMbuVfcqggEU2Pa-AxbengxfO3tp9bNWF2bqVvQPgs21hldZ0NB2MOfk6-yuQT-CgTyjJK3qbkShnUGzBywrVN8N-yehekMNu3bmzaF50XesgEJDJiIfl-4kgoGpkIWzLpdXQIcME7BkRLHYNlFGJNCxI3RoZ4KNQJZj8a2Fn93LGJkFPpIoL6YnTRYn38ZsNaj7euayJSAVW6Hh4nyB7IVK9Esq1RWJyzZKASIUnFjFQLHUiXLv8jQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 151K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 19:19:40</div>
<hr>

<div class="tg-post" id="msg-90638">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e11054c811.mp4?token=gwf1-LIburJpIfHNhFt6_bDvLFF6Pl8-pMyd6IF7_FyUYCH4luXAg3wqO4xPYb4CySp8w8e9mWMJ9P2-n09CHvIigBWA4cePubecYhhPv48CqqwLtJ7tvz81sUdnSL7TlagiaiTxaUd1lphE0Z25n52qqOUfc5EatJIJlnqOPwD1XlHC3JHcM2poMJPHzYPzJgxduyg5LVUv00rOOUa9COblY_o2wIG0P5EwMEkzxI5WoTzw0QtPj2OyZSGpTgHuYeuoXBy8OqeubIBkuspzn5bkpcp3tinmeVkty0so67Rl4P5E0U_IHCUKE3Y9Obc6uS7Lo58C6KplZQ6aDqw7UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e11054c811.mp4?token=gwf1-LIburJpIfHNhFt6_bDvLFF6Pl8-pMyd6IF7_FyUYCH4luXAg3wqO4xPYb4CySp8w8e9mWMJ9P2-n09CHvIigBWA4cePubecYhhPv48CqqwLtJ7tvz81sUdnSL7TlagiaiTxaUd1lphE0Z25n52qqOUfc5EatJIJlnqOPwD1XlHC3JHcM2poMJPHzYPzJgxduyg5LVUv00rOOUa9COblY_o2wIG0P5EwMEkzxI5WoTzw0QtPj2OyZSGpTgHuYeuoXBy8OqeubIBkuspzn5bkpcp3tinmeVkty0so67Rl4P5E0U_IHCUKE3Y9Obc6uS7Lo58C6KplZQ6aDqw7UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جام تو خونه میمونه
😉
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/Futball180TV/90638" target="_blank">📅 18:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90637">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cg3pCt7ofhOfAw0EHBeJhXGEM1i2qcF4tsjdbvqvKKBWeigbyCuALKlPLWK6fkYe9FoeO5o49Ylj2AvVJDLMgsB_gDOPq-Mp8HLhzUf8in7DfxJuA2yASukGt6iS4lA4CSaKvbOItMz66TBTtwIjKTqgkZmw_9e8fURtZVPgjtA3ghk_SwHi1VoWM92YV6-ySww6PynyoFDXgsdRAvpg47yVxexFISfjSJlqb22DigLAUbXAIi21WD_zCHjT8JqcUeKgnH8ortIQKpKL7Of_Zv_q1UXzPyGBJYLGKRB0KyeQuVpvNBpvmu0JoAgJyPO24WQ73zkFZcVipesiuJc-ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بعد از متصل شدن اینترنت، معاون وزارت ارتباطات برای اینکه پیام رسان های داخلی ناراحت نشن رفت از کارکنان پیام رسان «بله» تقدیر و دلجویی کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90637" target="_blank">📅 17:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90636">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QBN92qBLVsW1DBIYCOd4RKdGJz_VwYJbTMNZCyfnASz6beGUhSPmzhKDnv9AuKxT3cl2JFfB8HBzAXXzVf-_qA7r82T0coeLSx4lPtgyM5Jgv75Hx0B9PR3RJmhNYInPJNVtRO5Njso7dkofukTlK4U_WLLlsnSVw0Cg5BYbFpkWnvqCKn_KdSJFn4-_ltEgQBItbL7PpV-b8w3FSHBY00RMxgLwvV7jdh-GGtysHJvySFSCWhyQLvlIYncYsz97aJ1C70miVkh75ovn4mDI2OXhWt3TgJKoJ9UbZ7YaAe-wogcsiWIdooYuSSnUwFsKCWsa6Fy6fKm-e5QePOydZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تعداد قهرمانی هر کشور در سی‌ال:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90636" target="_blank">📅 17:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90635">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a15c25cc8b.mp4?token=RUYEUvG1RWLrzfnTX010hmefXGZnmne_uYJ6uQiJIuqRB16AdToPn4eDXV0rsaMuqhfrVGEfwOj3NX2DoE29S-hKDrgDsmuLRTeB2IyOjzzQ_o3ZUeGaVE21JWghzURRdr-ftg64Ghi3f9kqa3_tA_Iopn26uZ6n93MDSlRcaphOI4_ecc09uWb3UjKUP11LWwEw8fHZ8a0Mat8BukWYFDjtM6_VdSMP6iiI5YgxwAos2ihyxxaZH-vbZ7s9NDNUdPYSWCPu3MztLgMxMS2Ildu2AN4Lg4pGrcVfj6POahtCG6U20Wtfp8Ti7KG_XOu7_NSzIls4gBXCfnjG0NJR9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a15c25cc8b.mp4?token=RUYEUvG1RWLrzfnTX010hmefXGZnmne_uYJ6uQiJIuqRB16AdToPn4eDXV0rsaMuqhfrVGEfwOj3NX2DoE29S-hKDrgDsmuLRTeB2IyOjzzQ_o3ZUeGaVE21JWghzURRdr-ftg64Ghi3f9kqa3_tA_Iopn26uZ6n93MDSlRcaphOI4_ecc09uWb3UjKUP11LWwEw8fHZ8a0Mat8BukWYFDjtM6_VdSMP6iiI5YgxwAos2ihyxxaZH-vbZ7s9NDNUdPYSWCPu3MztLgMxMS2Ildu2AN4Lg4pGrcVfj6POahtCG6U20Wtfp8Ti7KG_XOu7_NSzIls4gBXCfnjG0NJR9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇧🇷
Vini
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90635" target="_blank">📅 17:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90634">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da899e08a7.mp4?token=RoSAxFLCdP3FeRvDNwmNXPHA2Ll_NKM_RmIrk7L7nRt0Vwtv5H4GG0UEsgOUg-jTcZ5_QIR84Uhq8zCFjQiJoVjKcOStKki4RTC18x_xJ9WJo4ujWB67zjasK9QEr56Rc_D3DfcdHJ1Bx88EagOG0pqzvdyNyz3viOoPmRdqBtrZGtTKKU06gk5yjaqM323Rz5qpBUzkwSDupmaMAWWkHWhlgNgIK2MgUQ-Y-paVDwS2-XpZCCUCPUnZe0EyjVOkm3REIyT0MO_8RdSDUbtRQje2-jGlxWFy0J6V0vUIjtUnCDRwf-SWm5fjkKMX7l0L5WMxP_P2dTBKDP4CLzBgBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da899e08a7.mp4?token=RoSAxFLCdP3FeRvDNwmNXPHA2Ll_NKM_RmIrk7L7nRt0Vwtv5H4GG0UEsgOUg-jTcZ5_QIR84Uhq8zCFjQiJoVjKcOStKki4RTC18x_xJ9WJo4ujWB67zjasK9QEr56Rc_D3DfcdHJ1Bx88EagOG0pqzvdyNyz3viOoPmRdqBtrZGtTKKU06gk5yjaqM323Rz5qpBUzkwSDupmaMAWWkHWhlgNgIK2MgUQ-Y-paVDwS2-XpZCCUCPUnZe0EyjVOkm3REIyT0MO_8RdSDUbtRQje2-jGlxWFy0J6V0vUIjtUnCDRwf-SWm5fjkKMX7l0L5WMxP_P2dTBKDP4CLzBgBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حدود ۹۰۰ نفر در جریان ناآرامی‌های پس از قهرمانی پاری سن ژرمن در لیگ قهرمانان اروپا در فرانسه بازداشت شدند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90634" target="_blank">📅 16:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90633">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🔵
باشگاه‌استقلال با محمد خلیفه به توافق اولیه و شفاهی رسیده است اما این گلر جوان اعلام کرده که پس از جام‌جهانی و برحسب پیشنهادات دریافتی دیگر خود، تصمیم نهایی را خواهد گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/Futball180TV/90633" target="_blank">📅 16:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90632">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b05db8d1.mp4?token=DqJKdwD_idhHP8VZBiAqNP6NLRRW7DAHpheyToCpWiYh8G-nGtlt8Eau8FQouJFokILlrkvulOOk2jxuVcl_x1gmiq_Xa7rNZMXEvEOVXxzmDY1akOB0L-Hf-jQ37JhqLTSA9412KrQ8sqgbo33nMiGHo4ISN9AA-_0UtoZLCV0hCspChqHL6cFrl6KISjRXEe1BGpGvtCnqF6J1UBZOMytOs8sXgzFR29fGi4EfP8ylWc2Evv6Y1rEtF_Od2JnlvzBR-c3y0QfLH__nJuFF-BbD2Z6q0AOjBfrlplhPvA_w-vwokkCqKqkQd7ESIT4cnAAd8YOFiSEb1u8o0YInPDuSI2_gCLFIfobCXXbfZWKhAJxAEq_StDHxzmDn6SIGjYl3tWNUC1AMcxKetEeuWmmXNpKrcgBz4ecnWoRwHfbP15obeiiYr70PyzfO0mewYnGr3qCCjc4rJ_XlaYvIuY8Fhn5Bb62X4wq-uqtsHVcJFzsohbXX6BcX6uK_VyCT0gmD2K8N6qjONmVyRe3Nf5LAUB8un3I-kkIqiJ47ShSx4qqXZOqS4J4eab4oeB5m-aIrYcV-kF09bygwThbsYaQ2woXVpY8oU6Bxrtix3G7Ds6aVE-TawCQDaqtOP1fh33hhM5OdyJ31KMYfas9lJJEb4l8ZL5nd-5BQGvYUGLI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b05db8d1.mp4?token=DqJKdwD_idhHP8VZBiAqNP6NLRRW7DAHpheyToCpWiYh8G-nGtlt8Eau8FQouJFokILlrkvulOOk2jxuVcl_x1gmiq_Xa7rNZMXEvEOVXxzmDY1akOB0L-Hf-jQ37JhqLTSA9412KrQ8sqgbo33nMiGHo4ISN9AA-_0UtoZLCV0hCspChqHL6cFrl6KISjRXEe1BGpGvtCnqF6J1UBZOMytOs8sXgzFR29fGi4EfP8ylWc2Evv6Y1rEtF_Od2JnlvzBR-c3y0QfLH__nJuFF-BbD2Z6q0AOjBfrlplhPvA_w-vwokkCqKqkQd7ESIT4cnAAd8YOFiSEb1u8o0YInPDuSI2_gCLFIfobCXXbfZWKhAJxAEq_StDHxzmDn6SIGjYl3tWNUC1AMcxKetEeuWmmXNpKrcgBz4ecnWoRwHfbP15obeiiYr70PyzfO0mewYnGr3qCCjc4rJ_XlaYvIuY8Fhn5Bb62X4wq-uqtsHVcJFzsohbXX6BcX6uK_VyCT0gmD2K8N6qjONmVyRe3Nf5LAUB8un3I-kkIqiJ47ShSx4qqXZOqS4J4eab4oeB5m-aIrYcV-kF09bygwThbsYaQ2woXVpY8oU6Bxrtix3G7Ds6aVE-TawCQDaqtOP1fh33hhM5OdyJ31KMYfas9lJJEb4l8ZL5nd-5BQGvYUGLI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇿
ازبک‌های‌جذاب آماده رقابت‌های جام‌جهانی
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/90632" target="_blank">📅 16:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90631">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/079475458f.mp4?token=GHxxRDZDLjlqXX5nk1mCJEJw3Ifq2gE6BFL6wslJDg9vjUMxVcfBNt2Oh-sQRd5G_b-JLrWytyqiYXEGGl-p7X4wdcuIx3nqGkY3pHi1R6GTynu5R2pi10Kgs8HipiYzrYvvY-B7ExU0VS-7YTbQbDACtF5uJXlhfjTy91nZKFO8V8VBpuwVxbSnEbsjOyjJimc-Ttm80guFlAtgUJ-yBI2s-rUnIstkaaPuHmseo0vKPwvOJQGp02YwR6u5UCmzYIzYurFOlyjlYdG1fdkJOqWgoHDgzKqWtt6V1EkuFHCmB1rf9OPRIpNJRvliSwmKQ9FAsn2yxtOpv9WnnIaQ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/079475458f.mp4?token=GHxxRDZDLjlqXX5nk1mCJEJw3Ifq2gE6BFL6wslJDg9vjUMxVcfBNt2Oh-sQRd5G_b-JLrWytyqiYXEGGl-p7X4wdcuIx3nqGkY3pHi1R6GTynu5R2pi10Kgs8HipiYzrYvvY-B7ExU0VS-7YTbQbDACtF5uJXlhfjTy91nZKFO8V8VBpuwVxbSnEbsjOyjJimc-Ttm80guFlAtgUJ-yBI2s-rUnIstkaaPuHmseo0vKPwvOJQGp02YwR6u5UCmzYIzYurFOlyjlYdG1fdkJOqWgoHDgzKqWtt6V1EkuFHCmB1rf9OPRIpNJRvliSwmKQ9FAsn2yxtOpv9WnnIaQ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
همچنان حاشیه‌های دوس‌دختر امباپه!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/Futball180TV/90631" target="_blank">📅 16:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90630">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfc7d5cd4d.mp4?token=s8QWXrOMPG786LVRA8wRAorUHo6kwtWzyaowPOCl0qhHeZqQJkT1nZJ4NGtAN3BXVX91gVgbGkKsTYVZ9ZJuSfB4ZDehYEj7bMp-PkYea2RNn5zVhYzO_MlUUURnGTE5WXwwNScoSrKSnqCom8ASW073YzsTwIQ_9t_0fp32HOWNCvVAc1uRDpVomU7RQOcxOLfgHvdlacIwRGT2l_8vieTKmgmHPLhSFmfdW0QaB36bD83LkW16aElnXsv4pcPIW6LVrdIOFA3lF9pGwZyYj0VeFxhw8cs-KHq2uxDjFW87N8rrJMpebRBPpikPXkr--cpmkw7FGLbvf3ML7HiOsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfc7d5cd4d.mp4?token=s8QWXrOMPG786LVRA8wRAorUHo6kwtWzyaowPOCl0qhHeZqQJkT1nZJ4NGtAN3BXVX91gVgbGkKsTYVZ9ZJuSfB4ZDehYEj7bMp-PkYea2RNn5zVhYzO_MlUUURnGTE5WXwwNScoSrKSnqCom8ASW073YzsTwIQ_9t_0fp32HOWNCvVAc1uRDpVomU7RQOcxOLfgHvdlacIwRGT2l_8vieTKmgmHPLhSFmfdW0QaB36bD83LkW16aElnXsv4pcPIW6LVrdIOFA3lF9pGwZyYj0VeFxhw8cs-KHq2uxDjFW87N8rrJMpebRBPpikPXkr--cpmkw7FGLbvf3ML7HiOsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
دیشب بازیکنان پاناما بعد شکست ۶ گله مقابل برزیل برای عکس با نیمار به صف شدند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90630" target="_blank">📅 16:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90629">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
لیست نهایی تیم ملی برای حضور در جام جهانی 2026 اعلام شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90629" target="_blank">📅 15:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90628">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d59f93bc5a.mp4?token=nuxs2WXTSYbX-KxOoooYj4KZiT8-Vr669TBlzKpxt4mX5XFZzNDZPf90DE95soHCqVXSfs7MZ18mo8t1dQ3LaUHARPrbdkU8D60ET-t9FPWQk71ZW6MQoLVpAevsnhFeNq6-yt6ddDRfBO7v_XxjB7yTX6_3-TWEOPH9GDLNUq0RLB4ApX2cJ_bxeNxAm21N_1skVCUTPax5zxK_ZW0GsqthDMS29f5JSRUpeD-SnkMkuYDrR3EjU0LTViQmH9oN1-uEgqBfemK80VWn5GrVB0AxR6Be97vJQ9Hwl6EQIUU0pU0GelCrgNpc9_BXSca1QD15fCJc-H4m9mfAgrlQ_wq5sYf531oy3_rIskBJF7N0Auc9YNMLdH-OR9mOOy2hW8RvF663ueR_bZfmzFgR93dcINvL3XDyQTPed6dhE0i-xB974FNT9Vji0C8_syraGHIWa1UO63GiVXKGI52DgoP457fUrIK9qyQpdrDVYaZuoNZ6aE5sqcLEvabUgVztqL4ktTW6FbiJ0li4gFD8KFxywV-wn0D2KQI8y9DHtsdZkM06pEILvJcQuysJTEE4yuE413gmG3yJN44HJuC6jGMKIEqxEmpj5OvQMtF_qXLSscW5Em8UT1QZxHk5xuhw9dTrzby5h0hrPZSDcSMGDaE3gGI47t_sHg2SczB9s44" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d59f93bc5a.mp4?token=nuxs2WXTSYbX-KxOoooYj4KZiT8-Vr669TBlzKpxt4mX5XFZzNDZPf90DE95soHCqVXSfs7MZ18mo8t1dQ3LaUHARPrbdkU8D60ET-t9FPWQk71ZW6MQoLVpAevsnhFeNq6-yt6ddDRfBO7v_XxjB7yTX6_3-TWEOPH9GDLNUq0RLB4ApX2cJ_bxeNxAm21N_1skVCUTPax5zxK_ZW0GsqthDMS29f5JSRUpeD-SnkMkuYDrR3EjU0LTViQmH9oN1-uEgqBfemK80VWn5GrVB0AxR6Be97vJQ9Hwl6EQIUU0pU0GelCrgNpc9_BXSca1QD15fCJc-H4m9mfAgrlQ_wq5sYf531oy3_rIskBJF7N0Auc9YNMLdH-OR9mOOy2hW8RvF663ueR_bZfmzFgR93dcINvL3XDyQTPed6dhE0i-xB974FNT9Vji0C8_syraGHIWa1UO63GiVXKGI52DgoP457fUrIK9qyQpdrDVYaZuoNZ6aE5sqcLEvabUgVztqL4ktTW6FbiJ0li4gFD8KFxywV-wn0D2KQI8y9DHtsdZkM06pEILvJcQuysJTEE4yuE413gmG3yJN44HJuC6jGMKIEqxEmpj5OvQMtF_qXLSscW5Em8UT1QZxHk5xuhw9dTrzby5h0hrPZSDcSMGDaE3gGI47t_sHg2SczB9s44" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
یه‌کم از جنارو گتوزو ببینیم که دیگه بنظر بازیکنی تو میلان و ایتالیا مثلش ظاهر نشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90628" target="_blank">📅 15:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90627">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIxCrhpUeCgzhAdm1gAcjiYGe6cHy3k9jQCMvvE5BBVntKSzvVxkVTZRietAB2EgqcM7pQjsGvGesdVAMLhJlKe6Eb596JxPct-0FszVVGmterDKCBU-u4f8wxQxZOqcAlShuYBjDkYLyapFgT1e4sZMx14U3za6389gvhAMGWlM-Gss2p_SewMUvxxi4oTAWrlczhLA4Cio1AMNqYioBTqSFj0FZcJ-E-4pt9Kt_LYx6FhJWwo6HkGh0jiEDHFjM5Y_JYezaXtzn8fsHTPyD0NTRBtGvT1l-JCXY3PouHfwck3AwyRnGUIBKHaIVgNWZRqOLLSVyZ_nI5R0m4Uh_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست نهایی تیم ملی برای حضور در جام جهانی 2026 اعلام شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90627" target="_blank">📅 15:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90626">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda3613d9c.mp4?token=Ae1uMevPvXxfIyxPTDJcp3279TkRt3LKjIgXFiTvDE2zPeAakpiuuACfA1RjG6w9C041iAMjWpRrUQDg3ufgzyHYs9S6KbWOMRQK0O7LVhdewnTNJbec1CNnIOWLJry7V5xfoE7Fzkmqxsc7B8_aQt5gAFYxIups0zF2ScJX-jiB-mc61dJt6Rm9z1SC-aNOhket_spSxTGc4FzaPcK4LH3LiLaU1EAcBLwyduwWbw-MltQ3_B0JERkOLCQWNycsFUmwwDaJbHanIGSqm_fadsfca0LyKl1fPucAnLCEXEaa9btjdfIbWsGBvBkhh3N89bdgdWEZrPAHCbaAmA4n_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda3613d9c.mp4?token=Ae1uMevPvXxfIyxPTDJcp3279TkRt3LKjIgXFiTvDE2zPeAakpiuuACfA1RjG6w9C041iAMjWpRrUQDg3ufgzyHYs9S6KbWOMRQK0O7LVhdewnTNJbec1CNnIOWLJry7V5xfoE7Fzkmqxsc7B8_aQt5gAFYxIups0zF2ScJX-jiB-mc61dJt6Rm9z1SC-aNOhket_spSxTGc4FzaPcK4LH3LiLaU1EAcBLwyduwWbw-MltQ3_B0JERkOLCQWNycsFUmwwDaJbHanIGSqm_fadsfca0LyKl1fPucAnLCEXEaa9btjdfIbWsGBvBkhh3N89bdgdWEZrPAHCbaAmA4n_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇸🇳
کشور سنگال با انتشار این ویدیو نوشته که ورزشگاه لس‌آنجلس یکی از میزبان‌های جام‌جهانی مشکل جدی در چمن داره و خواستار بازسازی فوری این زمین شدند
در این ویدیو مشاهده می‌کنید که توپ با برخورد به زمین ارتفاع نمیگیره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90626" target="_blank">📅 15:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90625">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/90625" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
✅
🎁
کد هدیه 100 دلاری:
Sport100
🌀
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🥇
صرافی معتبر
🌐
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/Futball180TV/90625" target="_blank">📅 15:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90624">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">چرا این روزها همه سایت جهانی
MelBet
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالا
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت،
از جمله کارت بکارت
🌐
اسپانسر رسمی لالیگای اسپانیا
😀
مورد تایید سازمان Gambling Judge
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/Futball180TV/90624" target="_blank">📅 15:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90623">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhbVL23_I3QgCjKVCUuL63M6IfLe8fdNUuSrQlWzchLCwz5ODb_2YSzJLm-kVkxmIdF_OiHeOPXGQIwaKfEi9A8NpSRHAfwemN12ZjnoHIU71Yyrmr-f8ZyWdrlUZlbuhBOxeSb5rpBqXt31AyoZAGuaWtbvsT-nOFzMIQqeW0biVRYc1-gA_eB4BQ3vfJwMfMPRGE-vpgIEO5jPaBNijPACo2o37EXXrCRWqgVuy_Y2q-VQ_KYK3DzUpwTsC4KDdH8UVkfUaOIStn0wcd5f3J_twv7k78SlgeIW8uV93qSrVuxXTegVudxYX0xZ7WOxdih86W9cLR8q7ph5H_V1YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی و بادیگاردش تو اردو آرژانتین
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/90623" target="_blank">📅 15:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90622">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUIVbgIeTNqkDCHw2EIxDc8iCM2QdMGCjvg-0ehwgbjHREgBD-eMyFfBAgYTxkZgRGGmDwpwCPXt3kME6ILm9LDNYoTxmRVbKUmQwTYlNMUOBfIbC1nFHZuM7f8PQ0_5awgKvetHdGRfUm1sPpi8CbDB6w5_UQAzM4udlonjYD7S97eBHnqi7gLfyek1y93D2CxQ7BuliC_S-gbrdgtfEiB5pO3zzsWWw7zrkk5elFIAnmYNtCzAhV_3xW46dJjglc_Al2qSLT7H7nnCUvFmoU4780sJ3a4poNY-99Nu6YXqSC0A94LLSNgwNZ3klNIT3KDGsn1J2QS3kgSJKl_ozQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فووووری
؛ با اعلام رومانو، قرارداد آنسو فاتی بازیکن بارسا که به صورت قرضی در موناکو بازی می‌کند، دائمی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90622" target="_blank">📅 14:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90621">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0da9f9a8d6.mp4?token=Io7D4SHfzaAkDfhTUPwUtbn2h10HEqitbFPpoGFv5NDRbQS6pMa4_W-knZcr6mFAsC5GUij1hnhrkTOBGNbYaxF3SZUBmHxXIlKWnCUf-ct_aiJkY8_8xE0QgFsJKKqyvGGl-7o8j1mYJOocFZjzYAvgqIyppiO3isKFj2ekDXIOnem8Tdm7Ys_zezodZ8QLPPIjD74aVjokrOcrrQadonRX26In10Uw1bLphGVgWL099uQ0Emb4wzKJRTwaXTzHMYpHetmsBA2sU_B6JDXY0SBGBRf6yMf2N13W-ea66WPgzYS3bndHMYo_OypzFVFubspDZoBv1Cugo-eRGGbBAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0da9f9a8d6.mp4?token=Io7D4SHfzaAkDfhTUPwUtbn2h10HEqitbFPpoGFv5NDRbQS6pMa4_W-knZcr6mFAsC5GUij1hnhrkTOBGNbYaxF3SZUBmHxXIlKWnCUf-ct_aiJkY8_8xE0QgFsJKKqyvGGl-7o8j1mYJOocFZjzYAvgqIyppiO3isKFj2ekDXIOnem8Tdm7Ys_zezodZ8QLPPIjD74aVjokrOcrrQadonRX26In10Uw1bLphGVgWL099uQ0Emb4wzKJRTwaXTzHMYpHetmsBA2sU_B6JDXY0SBGBRf6yMf2N13W-ea66WPgzYS3bndHMYo_OypzFVFubspDZoBv1Cugo-eRGGbBAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
یه بلاگر اروپایی اومده فینال چمپیونزلیگ رو اینجوری بازسازی کرده. حتما ببینید عالیههه
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/Futball180TV/90621" target="_blank">📅 14:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90620">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uorrTJckCvLr0jknpnOzt5qSKpyZlVSuaAX3khuP3BqcnbSeWoJhHdJ4vwZSGrESVInudqxN5ZURc6Nj_-hczTPufIeqrJuCTaAuHJUfPVtUB7QZez0dGZWbTW0-GLzQHhSurzL6H8rMGErLoH5fVg-hnZZArjqrbhG9isJmDsyrpYJyYn6Kv-sLGQwIvkPSHQIO6GUP4L1Uoy54fzEkKx9zhRuC8dqfFk3rzkUztTcwzuhjFE223dQDhr60_iOonb6jldzFs1XfqC60NkaBb8LUBwyKnoVtAfpFDei43F1KiyA1HH3KBaQIDgcivhxoLIuof_VZhWKhaTLAfzgvOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#نوستالژی
؛ سال ۱۳۹۳ و همزمان با جام‌جهانی ۲۰۱۴ برزیل، بسته‌بندی خاص چیپس در ایران برای تزریق نشاط و تماشای مسابقات در ایران...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90620" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90619">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
سرزو (رئیس اتلتیکو مادرید):
«جولیان آلوارز بازیکن اتلتیکو مادرید است. نه فقط برای فصل گذشته، بلکه برای سال‌های زیادی در آینده. ما همیشه در حال تلاش برای جذب بهترین بازیکنان برای تیم هستیم. تا ماه آگوست، وقتی لیگ شروع شود، هنوز زمان زیادی برای بررسی، پیگیری و انجام خریدهای جدید وجود دارد.»
﻿
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90619" target="_blank">📅 14:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90618">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEPL0oxibqAN33EUQgfuW78sLZTWC7XMzsQgfsZ7jF1n4AZw3WtnEzMDtlafJCJL9JBWfHVpRC7QpWxl0a4kBwsIPNKCOmvH7L--ae67j2naHJ-pskl0ialD_Hd5EPmgYqmDM4pKdERwZ6NPEHIsV2f9fmqZj2bQDeUVk4CxKiRxVz02nbSGjLaV6w0Iea3FIZ8Mqdi1iV75sc8HS0uTSTJ_sHiei2uTKs7an1nqGk5eA3dVrS94X4IsFKgZKpW1KDBgzYI66SWkvxMSL9d44eM3E0kR7pOXK-_4J9nC7J5SYOkmIHY-e1nd6uULRmYZCcCFlFbRwzYQMQ7z2zu-Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
⭐️
مقایسه آمار دزیره دوئه و لامین‌یامال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/90618" target="_blank">📅 14:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90617">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14d1ebf50c.mp4?token=R8ZY3A96Znu1MM7QvVA79K9a49E-EyKEmVRjEUrF65nqddJjz_NHYasKoHH6cuUzWg9Dem_P_dZFhzKr5I2gkcVPEIhP0Hu7ifcQT-T3Obosc8WHGojFlrH3ItzXQXSuZ9KY7pyHcjVqwh_n-yxTqAmPQWNg8FKEG_-sjikTbiKEFnrCfmOqMEYIky7L67t67oZyaLLdGgZSSaHbFD6EZrIMkc0zEpcWKAuRsuB6UD5oqVRnDkQYptnHYC77qiQvlvBxN1CKmubvVQytKJgURdQUTi2SUtV49MlKCxr-seqGRyHcKxzUefrC9pYxkAuEvkOnMB9Z9u1TuibyZa6RR4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14d1ebf50c.mp4?token=R8ZY3A96Znu1MM7QvVA79K9a49E-EyKEmVRjEUrF65nqddJjz_NHYasKoHH6cuUzWg9Dem_P_dZFhzKr5I2gkcVPEIhP0Hu7ifcQT-T3Obosc8WHGojFlrH3ItzXQXSuZ9KY7pyHcjVqwh_n-yxTqAmPQWNg8FKEG_-sjikTbiKEFnrCfmOqMEYIky7L67t67oZyaLLdGgZSSaHbFD6EZrIMkc0zEpcWKAuRsuB6UD5oqVRnDkQYptnHYC77qiQvlvBxN1CKmubvVQytKJgURdQUTi2SUtV49MlKCxr-seqGRyHcKxzUefrC9pYxkAuEvkOnMB9Z9u1TuibyZa6RR4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بالاخره یه ایرانی هم پیدا شد برای تیم قلعه‌نویی چالش اخیرا ترند شده رو اجرا کنه
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90617" target="_blank">📅 14:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90616">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cz_WRCyOHMRA67dTKuB1c6bKG-DQCGXLaPi9v9mHSPMntddkLO9uPJvkGJ1nGI8upRdM3Z8lpfgveq-H-nkxMmMkaaETbDZhqQQxIiKVgAXxwPVYRkkShaquHeeL5dWGMThn7EjrZOsRRYi3cMc23CgPb8-VLGomkFl1xuixKsAthJ-NJcmCi4SokZ2IQyl09Zh2-kv2MNn-0M5klU6qPL7GDQan2jg0Ioqd0TvxRP-JPZ9dynzjlsL-kcT6gqdocEXaX6WXo4Pc5ZbkwMBktd1NC6dgrYfGgz8aEpVV7f79ab6aQWaD1vQt5m2nOiXUid9HrK-pQF_pzTcpOQPAgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
داویده آنچلوتی به عنوان سرمربی جدید لیل فرانسه انتخاب شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90616" target="_blank">📅 13:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90615">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
#فوووووووری
#منهای_ورزش
امروز حوالی ساعت ۱۰صبح در دانشکده پزشکی قزوین، یک دانشجوی مرد در ابتدا همسر دانشجوی خود را به ضرب گلوله به قتل رسانده و سپس با تفنگ، به زندگی خود پایان داد. سپس این دانشگاه تا اطلاع ثانوی تعطیل شده است
😐
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90615" target="_blank">📅 13:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90614">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a22b3eef4.mp4?token=pJ_1NHGJXVisGuqeQAgbVsjTYbfdPQXV9GudV7Z1L7Xs9xogr8kK0PaqVfgo_DwyBJ-D3xe75D47DK6i1xJTf2reyWcmz8cqezpXV-y-kKkBf4nDK4vhsqhhwZJeM7eBCz7AuQ6PMLTAe49lhI1q-Yz0IN97Y9lN25L4aWn0IOmxbaWFXCl4clkVF-THc_AVOAC2xYymJ3Hr8xrvWhXXJuaCZbFrEhYbWhTPmYEjkylayyHftm_OkvR4PSsNR9aqK9sCUUrXragqbbxj8U5Cvz-uKmyBpTQLYhheocK2F8ac63CtqwNl5Ykka2EBROj-Ze0TxBd4HK7s7dCRUQueRjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a22b3eef4.mp4?token=pJ_1NHGJXVisGuqeQAgbVsjTYbfdPQXV9GudV7Z1L7Xs9xogr8kK0PaqVfgo_DwyBJ-D3xe75D47DK6i1xJTf2reyWcmz8cqezpXV-y-kKkBf4nDK4vhsqhhwZJeM7eBCz7AuQ6PMLTAe49lhI1q-Yz0IN97Y9lN25L4aWn0IOmxbaWFXCl4clkVF-THc_AVOAC2xYymJ3Hr8xrvWhXXJuaCZbFrEhYbWhTPmYEjkylayyHftm_OkvR4PSsNR9aqK9sCUUrXragqbbxj8U5Cvz-uKmyBpTQLYhheocK2F8ac63CtqwNl5Ykka2EBROj-Ze0TxBd4HK7s7dCRUQueRjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بعد فینال Ucl بخاطر شرایط جنگ در اروپا، استفاده از پرچم روسیه برای سافانوف گلر psg ممنوع بوده اما دوس‌دختر سافانوف با چنتا تیکه پارچه برای شوهرش یه پرچم می‌سازه و بهش میده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90614" target="_blank">📅 13:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90613">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnD7sPnov07hlBJIkES6K0yyA9ovbuBxvw1XlC6OPDiSlFbbfAeiO74ITTsmY3yynJq5Svh4o4-R1eZ_jCBep_TkFs2-cHmXEVlTm2swymOOI1qSb4s99y4Jok1bXVzVum-yR02mfFXTumGff4DYlLsmMHZSCpTsR_m-npZQmC9yF4ldiYA4S4T3_UizWT64kU4zr56rqwn17wSuCkoq3hNDCTIFFITUKjOBoEnnbCUmLNItL4qPt9suneQBM28b48oSn-wiWwycYM2xjmyb1O-2U5D2cTO7rmX4-xgkkQiPYKUlwBX3rTYwN3f7yaZhrbZD2DmkphKIYQrqvIj0pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات
|نمایندگان انزو فرناندز درخواست رسمی خروج از چلسی رو به مقصد رئال‌مادرید به مالکین شیرهای لندن ارائه کردن. فرناندز گفته به هیچ قیمتی حاضر به موندن در لندن نیست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90613" target="_blank">📅 13:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90612">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJtPqOewT9yO0sy1BrkugQdYXnCIopq4y_C2qvgZ_I_M8y2YvHEVy8DUR-Qp0D5eR8CsoGy_2U9xVbZ0Bw1OpqnplsJM4J7_W--SeZJENEDTZjtP_5lFmP94pS-vWYH2NMJg_3wh6Aza2o8gTtPBDBcOtD42vE2pN_ouzA5q76N3_4DPjnKTue7LHefLMo_jxwXDK4Y4ergNoam-bG94EStqekYBFc-_x2PC0-GREgnHDwDhpDvVIaabNL7qJxZQcoP1YMHgZueftXDip-AoYuQw_TmJS2I7hZc6JLAqbqpzSpLRhvBQ1oOGTjlYwKNxMnpVaZwsbc-ArLchuyT4Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
مارکینیوش با عبور از دنی‌آلوز حالا تبدیل به دومین بازیکن پرافتخار تاریخ فوتبال شده و‌ فقط لیونل‌مسی از این بازیکن جلوتر هست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90612" target="_blank">📅 13:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90611">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B90uMvLM-yUBJHzoXmdPfmmvAtLjZwiO8PL363NlCt6imgU0mShocaLkrOLYt8qbC-osnYTfzEtA-9Pz_-fi7b6nHnnr0GN_-ad07K-xeaAsRyTMJH6ClXgfPHdXqgfiiU_VgVMijl8CSgOCxQOAIYcw9zch2YBV_oFauISuNYg5P4qL9YVPvo-jMvWH14gfWwMt0pVUdWqQ2x_A5ZkZb6LxNobf0Dh-ow3FQkmlJTj5bmhHzL-6kmILOrIA4mkanhJhyyPT77braCupJ1SrX3x_LbzsY4w5hNiawzKzaKotzN75W06yQ0Hb8TjwMdKQDuYmh46GDmjjz9dO9iWpvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
داستان خولیان آلوارز تا الان:
❌
تصمیم نهایی گرفته شد: بازیکن در اتلتیکو مادرید ادامه نخواهد داد
🇪🇸
مقصد مورد علاقه: با بارسلونا بر سر تمام شرایط شخصی به توافق رسید
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
خارج از داستان: آرسنال و پاریس کاملاً از رقابت خارج هستند
🇪🇸
فشارها: بازیکن و نمایندگانش با تمام قوا برای نهایی کردن قرارداد فشار می‌آورند
🇪🇸
🇪🇸
موضع مدیریت: بارسلونا پیشنهاد رسمی ارسال کرده و منتظر پاسخ اتلتیکو مادرید است
👀
🇪🇸
طرح جایگزین: بارسا پیشنهاد دومی آماده کرده در صورت رد پیشنهاد اول
✅
پایان مورد انتظار: اتلتیکو از تمایل بازیکن آگاه است و نهایتاً مجبور به نشستن پای میز مذاکره خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90611" target="_blank">📅 13:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90610">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmoYAWNqPjqFBk54PDY_6UpMbgolXo7q3RTaSe4vrEmiaWeRmLE9caw6L4G1dIakKx7RK-5kv6WMJ6vxwVQ6jvnxTJpkZ-JQznyqSHKSDKLUTQvpC9qP0eLGwldlIv8Qb7UNOs81cCkQ9pkPPezsww9QZmZQ11y_UrSoxhbUsq82K8KMRBv-G453_nyMiLy5R6rwzfXs1y2rOWrCgKyC0_JA9x6xVaaWIwpPmsK_FFkyLLb4ElFNSD5hx_dK3mqECLpU0TrRBUE2h6zV48W4YBUx1ZuH3p6yAOZOwg3Ox5O2VP_07YZvNDvbIUSIByERLT_j9KtZ5zQM9OG_oLxsoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سافانوف گلر پاری‌سن‌ژرمن و همسرش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/Futball180TV/90610" target="_blank">📅 12:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90609">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90609" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/Futball180TV/90609" target="_blank">📅 12:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90608">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFRZio9V4wVRljg2LzxRnYhDsAU7lV1itGYjjFMRAkPNbn5nj1VuOUxI5RT8JmECEUC7mZa6N-6bQeVgjOV_b_1946ZPyhMq82x4TNqfywf91tajkyznEOcW_ws1H3Hy09iF4Fd716zBihZO9VNKdUpNXXUJM2i_dK493L75Xbyt40L165NwiB3nkode4hujQqYfZLJaP1sCFUDLtVug7Deb-xfH_401uD7aw5kjRfPz-EuadZ7XR3_HzF0opMGtHBwLZSgk2T-x_utHhLRZelGm3G1CK9oUJdTpt2mt7UVNljRuFxH4oRkAMVXjcyQPYtwRF6XvC8mnH-d71cJnzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌇
بونوس‌های شبانه از 1xBet
🌒
هر چهارشنبه و پنج‌شنبه از ساعت ۶ عصر تا ۱۱:۵۹ شب، برای واریزهای 5.50€+، 50 اسپین رایگان در بازی
👑
Crown Coins
👑
اهدا میشه!
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
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90608" target="_blank">📅 12:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90607">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de9fc7368f.mp4?token=m414ojYnDCb0WrQx8SZjb1DB3NSuQuDsT7wQM_q35eR3-P08hughCoZCrNmZxVImRwVNTOor_OtDxGtF8Yx3_ZiHZKJzOZFUy1QbMSXWQVnhv9N3THWppxt9no5MeOEs7qAynlfmNnlhZldgyVOkNdza9R5jTrPKDMpo6AxgtFNnez0tPLf8EHOoGHh9s8BXDuY00Y6ZnpUbcVfGLYF5Fileq_uH8TGyC4XhnV_5U6QSrnK-Mw9Qnf7vYUitHnpaCeoUOuVnfhp0mt_chfl9sgy6IUHYA6isnDiNMeYzjfK_biso9Zx8_bVHpgxuicA8hFon5nKKzA3Pn4m0A3g7mqBi3EOiy2fGbey1nSgm0TtldiKPJkTQ9wHPizC29xy2jNdyQ5s9wu2MXa5F_xnxs3HmFEDgkYDN1MFQATf0bqyYfTWaZw9UoP5AFN4i0x37gfyKthilVX11r2qbP64AJLZBVyUuSgUOFy07J0WTtXfuwhmWnLv_PkOIXLLgInfJabuIOmsaxxpIYYn4GXsUnrZfa5mviWHYVwulj0-unaokM5MvDwHO5ftnQUh8XGys3dM7c2YND3itm9lKt-bIAa_9VPpYHW1nNUozVCNSdZ_bVWa0YUoIz9VfsJBR455egPWhTu55yvfMKlHQj1pk53ZoBvmUamzQa-D0mwX6rTo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de9fc7368f.mp4?token=m414ojYnDCb0WrQx8SZjb1DB3NSuQuDsT7wQM_q35eR3-P08hughCoZCrNmZxVImRwVNTOor_OtDxGtF8Yx3_ZiHZKJzOZFUy1QbMSXWQVnhv9N3THWppxt9no5MeOEs7qAynlfmNnlhZldgyVOkNdza9R5jTrPKDMpo6AxgtFNnez0tPLf8EHOoGHh9s8BXDuY00Y6ZnpUbcVfGLYF5Fileq_uH8TGyC4XhnV_5U6QSrnK-Mw9Qnf7vYUitHnpaCeoUOuVnfhp0mt_chfl9sgy6IUHYA6isnDiNMeYzjfK_biso9Zx8_bVHpgxuicA8hFon5nKKzA3Pn4m0A3g7mqBi3EOiy2fGbey1nSgm0TtldiKPJkTQ9wHPizC29xy2jNdyQ5s9wu2MXa5F_xnxs3HmFEDgkYDN1MFQATf0bqyYfTWaZw9UoP5AFN4i0x37gfyKthilVX11r2qbP64AJLZBVyUuSgUOFy07J0WTtXfuwhmWnLv_PkOIXLLgInfJabuIOmsaxxpIYYn4GXsUnrZfa5mviWHYVwulj0-unaokM5MvDwHO5ftnQUh8XGys3dM7c2YND3itm9lKt-bIAa_9VPpYHW1nNUozVCNSdZ_bVWa0YUoIz9VfsJBR455egPWhTu55yvfMKlHQj1pk53ZoBvmUamzQa-D0mwX6rTo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
برخی از برترین گل‌های فینال لیگ‌قهرمانان اروپا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90607" target="_blank">📅 12:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90606">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVDaqBP_AedBDAQn2G169EtlffBu_wL3WBVnh5CdeoKk7mozNPxU2boEawj0GcNNBUL6klDA11gNr__JLR7RDx5MM0uwC3AGQeOwYm8GQxscFIaNtvYPfwZgn1jJSQYwIi_LjoQcB_thqGQJqZK-CSwO1uCtaeqP2AQjKl0tEtG3ku3jrn3yPRx9XEqP6AqBEj0Bs5D75oIFiLiDSCNsPhgIqlF5w-fUJomBMXCnNXx1IsahMA_bCQMmCt_LnIS4nsCLoUuTJ1tRIGHgqnDmIsGyvMEt0cqw_lOu1RofT8sPI78yomDn_fbV8hEERdOw55fw-I-C4DA3Ku1qCJnDtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
گزارش‌هایی غیررسمی از فیفا:
❌
فیفا قصد دارد «تمارض یا مصدومیت ساختگی» را به عنوان یک تاکتیک در جام جهانی ۲۰۲۶ ممنوع کند
❌
دیگر اجازه داده نخواهد شد که از آسیب‌ دیدگی دروازه‌بان به عنوان بهانه‌ای برای توقف بازی یا گرفتن دستور فنی از مربی استفاده شود
❌
بازیکنان همچنین نمی‌توانند در این مواقع به نیمکت ذخیره‌ها بدوند تا دستورات تاکتیکی بگیرند
✔️
تصمیمی که هدف آن افزایش سرعت بازی و کاهش تقلب است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90606" target="_blank">📅 11:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90605">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7181ecdb60.mp4?token=JK-JxAlzqgIHoNXcmP6ZZld-2NJvQcy4FFYAysDacUYDhqqJYD9WbgbUj04xV-lD0RlIs_QCcukQu_pUq7KBMaQTSv6L1G1zXBFfTdch5FPu-YUdYBNDIGPF8h6N2RNbxcKwjAkniv0EUpuxnAJRULNWt9GQI_dzz6Hv0T8vnfW2ALasBKGConluAAXmVGkmIvIV9zmTY4kZkJoGY3k__6ZpNEkZxQsT6kNL2Mj6wnRya54emUoS6MwNPrb_WhTXNrEEAqQVjfhKezf7p3jZOUb_eI8uNv_W4OUOosH_aydxeG4YJMihi3RCSeLlNwWWVb37C6avhdmF3Y8TOynTEH94CG1Nq8VRR82bPAqon2m-jpxdSZcUL7lLo68hQ4DF2R04s0o6w_wHQjtcJIIZjOM9FG_iPxyZyz1gK_7m0s0RpWNY7hxjfNJuuHh7pDHnALaWvNLJqtz56dGU8tafPMTNABDVq5TdT16G-MZFHBwTI8ytHwCyNVBso4w9WQiIDD-jJoeQaP7gW7s3d5ZbJFDC966UvnCpotG1Cx1K2U9RUAIQFA-WjKmV5KASCLvq_Lpg4bxgWQ7i7GbAsaMAGPlKwrNMNynsU4g6r7kvEPMSw-HrPqcylM8SK35-TSJ8pZd2bLbBs5oPJ9bHMKBazfV_ulRf0IMnF4BJ_z2YHlM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7181ecdb60.mp4?token=JK-JxAlzqgIHoNXcmP6ZZld-2NJvQcy4FFYAysDacUYDhqqJYD9WbgbUj04xV-lD0RlIs_QCcukQu_pUq7KBMaQTSv6L1G1zXBFfTdch5FPu-YUdYBNDIGPF8h6N2RNbxcKwjAkniv0EUpuxnAJRULNWt9GQI_dzz6Hv0T8vnfW2ALasBKGConluAAXmVGkmIvIV9zmTY4kZkJoGY3k__6ZpNEkZxQsT6kNL2Mj6wnRya54emUoS6MwNPrb_WhTXNrEEAqQVjfhKezf7p3jZOUb_eI8uNv_W4OUOosH_aydxeG4YJMihi3RCSeLlNwWWVb37C6avhdmF3Y8TOynTEH94CG1Nq8VRR82bPAqon2m-jpxdSZcUL7lLo68hQ4DF2R04s0o6w_wHQjtcJIIZjOM9FG_iPxyZyz1gK_7m0s0RpWNY7hxjfNJuuHh7pDHnALaWvNLJqtz56dGU8tafPMTNABDVq5TdT16G-MZFHBwTI8ytHwCyNVBso4w9WQiIDD-jJoeQaP7gW7s3d5ZbJFDC966UvnCpotG1Cx1K2U9RUAIQFA-WjKmV5KASCLvq_Lpg4bxgWQ7i7GbAsaMAGPlKwrNMNynsU4g6r7kvEPMSw-HrPqcylM8SK35-TSJ8pZd2bLbBs5oPJ9bHMKBazfV_ulRf0IMnF4BJ_z2YHlM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
پشت‌صحنه فینال لیگ‌قهرمانان در استودیو گزارش‌ ورزشی که دیدنش باحال و جالبه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90605" target="_blank">📅 11:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90604">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ff67e8c4.mp4?token=dpI6fsUME-Jdmh-QiiMajwiwHyRX3g9Oo-YyphesHPiXFd4Rr4KjGMqyxEi4IJW_XrxmZuaFkMzzDOKf6JaLa8c5mRpksWbOVeQicauarIt6sEtlu5tGCFOVDJJE498cAdCRynr2NP5eAxUUFOUbOHlyXxj_aHqQBsE8-HJbOjhNSOD-IzOcB1Gm4YgPC-qjtAr5EbyenKvBgeAfmJ2GOnZ-aPaIvCIAY2LJeNlJ9I5XOwMkUdjVi6olcGAr4JcA_swAsYEMmuQpagjIVXBl3WCkvq08KHRoXHB43OX8lI_cTHcRg1kpCzALw9Ze_OYPrTQZr_xrm56MymtUWDF0rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ff67e8c4.mp4?token=dpI6fsUME-Jdmh-QiiMajwiwHyRX3g9Oo-YyphesHPiXFd4Rr4KjGMqyxEi4IJW_XrxmZuaFkMzzDOKf6JaLa8c5mRpksWbOVeQicauarIt6sEtlu5tGCFOVDJJE498cAdCRynr2NP5eAxUUFOUbOHlyXxj_aHqQBsE8-HJbOjhNSOD-IzOcB1Gm4YgPC-qjtAr5EbyenKvBgeAfmJ2GOnZ-aPaIvCIAY2LJeNlJ9I5XOwMkUdjVi6olcGAr4JcA_swAsYEMmuQpagjIVXBl3WCkvq08KHRoXHB43OX8lI_cTHcRg1kpCzALw9Ze_OYPrTQZr_xrm56MymtUWDF0rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
اکسپوزیتو زید جدید امباپه درحال قر دادن در کنسرت دیروز بدبانی!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90604" target="_blank">📅 11:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90603">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4pYKbUNr7L-IISiVhl7zbv-c-_M1wB28Yqv_dwBbJiX8TwwKNU_rPG7y84fFdgZUUZfFLQ6wYNGS09xFqXOo-gFqnJn5M_KxJFCw4XHk0jGaQmZ_1WsmvqxFi9dLuyUo-ivVhEqlmmNue1Bk3LpDNGxLdm0t6Pq1Rqs9i2Xa0hJ8bW83WBEpt7IZ9_wPH6siACZu_1Br5Jtm72nB8NtKwT3-pQQUfBKZkrEn6xf-kt25RO0dHZd698J19vMXMco3dOHDYOoMfWq0frjoZHuH5CfJXV_2eI9kMiXQhstFh5zlnDwFLEtYeJvZaE646W5tdJY5fF8Jqrj0cRuLFtNzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
👋🏻
جیمز میلنر ستاره سابق تیم‌های لیورپول و منچسترسیتی از دنیای فوتبال خداحافظی کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90603" target="_blank">📅 11:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90602">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4e59e2547.mp4?token=Aqzd7rtPStwn37vpnjDU_3z6k2s78aBe5X4iNdQR6uw_r2f-qjSxcqFMJCsKcTruYHx4wHcugRhMLAx5gGxX-Z4tbDflfjLrT6mlNBA19p-dhI-nv7f2QKNEGJIqbfUzfJe7bPmWmuUGOh5ZnV_xLCJEYonyOAifL0j79YE_w1xE6WmuNLJ0tSgb3EINXAnhWkSgRJbQI7VMZ3UV0DMy_dGbh_x7n7gaQ3xrcDH3S7xPAi1H0G6E5rGecBqp28vYOKB7mGa6MX6w8Ukfd7uKAtvU8XscKupaow6JWe0qTwFXgozM-UfspmvSx4E0LmLABtIfIEKwb4AnbsIWR7XzZRhoYzRkEotmnUiueSwaxeMHy5WKgDdmp0hDLL_RXYAFns46gojD4TZnMbUlH-cyef0hrt6LWjM6ze6C7T62ORJ6tM2FFS-l5RFAo80SKN9V05CXca5yp4LCN764v5U7F1cIX3mq5drN6am0-_cjuHjhDAj3fWdUDyqDRSQ5HrRsGx8QRoG_-HWrD0yLcq2DPCe6CW7k4MmP4ayVwBGJCU-hji83G4x_lAkEV0efk3DNC9ffn19LgCSHqAAMfa_6ZMycUpKI3TNc15aNAZ4j9ngA_CEGc3LD9W4gMj4mgxMHewoJSd-7UXp9bPpLpGhwxNMhU7Wq4wR0STGKACNka20" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4e59e2547.mp4?token=Aqzd7rtPStwn37vpnjDU_3z6k2s78aBe5X4iNdQR6uw_r2f-qjSxcqFMJCsKcTruYHx4wHcugRhMLAx5gGxX-Z4tbDflfjLrT6mlNBA19p-dhI-nv7f2QKNEGJIqbfUzfJe7bPmWmuUGOh5ZnV_xLCJEYonyOAifL0j79YE_w1xE6WmuNLJ0tSgb3EINXAnhWkSgRJbQI7VMZ3UV0DMy_dGbh_x7n7gaQ3xrcDH3S7xPAi1H0G6E5rGecBqp28vYOKB7mGa6MX6w8Ukfd7uKAtvU8XscKupaow6JWe0qTwFXgozM-UfspmvSx4E0LmLABtIfIEKwb4AnbsIWR7XzZRhoYzRkEotmnUiueSwaxeMHy5WKgDdmp0hDLL_RXYAFns46gojD4TZnMbUlH-cyef0hrt6LWjM6ze6C7T62ORJ6tM2FFS-l5RFAo80SKN9V05CXca5yp4LCN764v5U7F1cIX3mq5drN6am0-_cjuHjhDAj3fWdUDyqDRSQ5HrRsGx8QRoG_-HWrD0yLcq2DPCe6CW7k4MmP4ayVwBGJCU-hji83G4x_lAkEV0efk3DNC9ffn19LgCSHqAAMfa_6ZMycUpKI3TNc15aNAZ4j9ngA_CEGc3LD9W4gMj4mgxMHewoJSd-7UXp9bPpLpGhwxNMhU7Wq4wR0STGKACNka20" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های بامزه صادق درودگر راجب مصاحبه و مناظره معروف و جنجالی شبکه خبر
🤣
🤣
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90602" target="_blank">📅 11:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90601">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05002ce01c.mp4?token=mzZBd3AfPrkQrHABQc53KwjoIVTvGoeEJSH5dgEq4-CBrswXvCs9Gt50G3dHuwqpYuKdgg_0Ba4aikcC5hytOrIDB0C6-2shThrwdjVtu7i5iLVPEhknXITfRuWdts0PExmKw2jW9-9m4T9p07BaMUM5OB_GbEskIB3Kr6aPuBXkgaEpIOLdvRGfqsAxFnmX_uhfbOtxT5L5_Uj2uejfNImzxyNnC2v33ly96r5-I3r3XzIdAJbnZo9Pt826vn1I8TDxJVsuxGTWEEDEExX0R2fnMU72pY8RYDVxfgfVAhNYT8ifKUbPMr7ML1fulEeC1edenjgVeQWa2FFm2eroBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05002ce01c.mp4?token=mzZBd3AfPrkQrHABQc53KwjoIVTvGoeEJSH5dgEq4-CBrswXvCs9Gt50G3dHuwqpYuKdgg_0Ba4aikcC5hytOrIDB0C6-2shThrwdjVtu7i5iLVPEhknXITfRuWdts0PExmKw2jW9-9m4T9p07BaMUM5OB_GbEskIB3Kr6aPuBXkgaEpIOLdvRGfqsAxFnmX_uhfbOtxT5L5_Uj2uejfNImzxyNnC2v33ly96r5-I3r3XzIdAJbnZo9Pt826vn1I8TDxJVsuxGTWEEDEExX0R2fnMU72pY8RYDVxfgfVAhNYT8ifKUbPMr7ML1fulEeC1edenjgVeQWa2FFm2eroBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
#رسمیییییییی
؛
گل فده والورده به سیتی به عنوان بهترین گل فصل لیگ قهرمانان انتخاب شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90601" target="_blank">📅 10:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90600">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aChMRVcawUFok5kRox4WmwrnsTZHP9EAay21xbEUqSZMaWyVd78upCLOlSkmEYAuXbPlUwQlHPMo8LopJOYzTew2r4WTWszwhL50GKxmAu04KUxVSBH2YFBjQbjl2XIbItFdtP-k5wTkWrEAsZotYoSv4wK9neZomNtJAaNyn8Pcz0QvNYwWvPxKEhklx-VyIHn7nEzq3DASR3qdDcaKvayOsMbs_DSxNg08VWRHtSQAiMaCsCbgRPzsMFUmT46-EoMPXtW7FvkplyJVWEA0_rYV0Um--IcbSzpJFpF4EYIUcJf5Ru5p60MAo6ezA-xvroZEa06kW4XgmVUNkSuJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
علیرضا فغانی اولین داور تاریخ فوتبال با سابقه قضاوت در چهار جام‌جهانی مختلف
❤️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90600" target="_blank">📅 10:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90599">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
⚽️
❌
🔵
#اختصاصی_فوتبال‌180؛ فرهاد مجیدی سرمربی سابق استقلال بدلیل موضع‌گیری در اعتراضات دی‌ماه، شرایط حضور در لیگ‌برتر و بازگشت به نیمکت تیم‌سابقش را ندارد و شایعات مطرح‌شده پیرامون حضور وی در فصل‌آینده کذب‌محض است
❌
درخصوص نیمکت‌استقلال طی روزهای آتی اخبار…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90599" target="_blank">📅 10:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90598">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qb3WqCC_hD4I7LbWrzx6-McmWU4bykmIvXWTOzQTF80FcVSZOHuGu95R0EHJsoquY61meigV875Vw3Bh3-Sef3MGpeCxyGmM1bi1apvqhziMPaKzuFgRc77UfKDARlBFnYMvhTVY9kdVCG0X4O34Ihs4PpN3MFGht3kwjzEZRbVGusziZcXSMg7tXG7VjzuVCyAACoXfbsdUUCmkGF7PYMIMEZ85N8_TzCbkIlYpCmwc9oa8sVzJtKSqkzsxpMYjSk3ecPS-ztAjxJmOT65p6THVqfSXdE_rKkviwRqcLfulMUZNJyZFBl0a5_5VTbMl1YIAjcQnFXs-kFHRL-GcaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری
؛ گستون ایدول خبرنگار مطرح آرژانتینی: با جرأت میتونم بگم که آلوارز در نهایت از اتلتیکومادرید جدا میشه. پیشنهاد پاری‌سن‌ژرمن بسیار بیشتر از بارسا هست اما آلوارز فقط و فقط به بارسا میره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90598" target="_blank">📅 10:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90597">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/458f4f6058.mp4?token=C7NgZpEzoDWLDCs3l-K-eWWtOIRWfi7xf5LsuzQzAnuAXexYuq9bv4gUq4EfPX0XkKQTe4jyFx_dajfMLomvlwKvckUSsimD6iuxnEvoEy1POIrD_AUY9W33GC03rmsx6nGYW2RONSQFrW3_PnRsMEuUSmYQ4Hi982GAZxVMk2UMxgMRyRcBw-3Nd5pE41TNnjVdeiAfVQF4Q8XdrO5LrF7GYpryfTgk0PBXWe406DFCpB16WTU6USQr5LKQ4Pihp-6s3xDtq0gSnux7yquZXxcIJByU3bi623TGAVq2cLb6y6xdScRe4cIi6Evyds2MbWtHubaAVR1KssxPW6_Gng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/458f4f6058.mp4?token=C7NgZpEzoDWLDCs3l-K-eWWtOIRWfi7xf5LsuzQzAnuAXexYuq9bv4gUq4EfPX0XkKQTe4jyFx_dajfMLomvlwKvckUSsimD6iuxnEvoEy1POIrD_AUY9W33GC03rmsx6nGYW2RONSQFrW3_PnRsMEuUSmYQ4Hi982GAZxVMk2UMxgMRyRcBw-3Nd5pE41TNnjVdeiAfVQF4Q8XdrO5LrF7GYpryfTgk0PBXWe406DFCpB16WTU6USQr5LKQ4Pihp-6s3xDtq0gSnux7yquZXxcIJByU3bi623TGAVq2cLb6y6xdScRe4cIi6Evyds2MbWtHubaAVR1KssxPW6_Gng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیکه علیرضا دبیر به پزشکیان بخاطر پوشیدن تیشرت
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90597" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90596">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgEA6-fNoWEra3qdSIKTOXx5ysFOHrnnVkBDbUVJU_b3KliQw6gEIkTLB0QRF4sz_J2ippFxBNPsT51mx4uRgG3ax3Pwlh5b5GvdRgJZD6_rfEaJGElQbFI9vWf7v_Mzt9MAZ4ib1ZfL3PIf27PS7nRzSTjGgyRNIMdvgFuICfXQ2AcIdRBE0wFcB1zaksAurnd2O64DowKTEwBMOAhv2hLXmArsUtAIQngaiv-brUCdfC20uygK8JJf3Njjj5fW70kai64ArLp0pCyphQgblvq6EooqIA3mWpNpcBqznbKP4_wxEbgujfwv5aL4l2oD8SSAbn9oRYcGXPdIH3UjFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏟
تمام استادیوم‌های جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90596" target="_blank">📅 09:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90595">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHW7iHfcdf3puZV_L1Z9XQjZTW87MYA1XukIXRKVXDDoO0B_ibgWw1ZPQzzo6rlKwAfs-hoE-tK7r0dIvuLhdy7QgLlhMOJa6PRXe7LjmFXvNiEoanCS1R0hD4MVRWcPNMGDU524vkb6dxNoWuoTeEQeZImTuQQM7HhwqHm-G6WkaoPvbeDNQH9RAu5U_dlRKGR2LrMfy5LjSFGcfly1n6wuBHojL8q39gawA2b7Vp3vgrkjDsNdRgH9_eBcsZiZjGbbVk7jGZtt_qWao6aiRU346czBYYVueMZDLOKjRLG4DmXbIx2e_AQaZDFEOp1iPEJvneJajK7g0QrIEUuCLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ابراهیم‌کوناته‌ستاره خط‌دفاعی لیورپول از سوی صندوق سرمایه‌گذاری عربستان سعودی رقم بسیار نجومی‌پیشنهاد دریافت کرده تا به فوتبال این کشور ملحق شود!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90595" target="_blank">📅 09:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90594">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f927e35e14.mp4?token=Qgyo5zJbLOA1HVJS2qryl_f6tCMV6s4dRDlMYt0gK4HYxqLl-hbMXP8T0DGHtzrddZMf9FexVenZwdKRb0P4eCyb-29OlE2G-lwfKxxOrqstiVs71hYaV29ghndgrTV7tNAI0Bx3kfEYBoR8J4HQU5qT2rjLHDAa4VuQCC2V7W75EQG0W1W85vF3s8mQCW5U2JJflUhXCIrv8JjgDcjIpGmJ8rssndjB5et8lJdBEUpD7kFnbRHmK68Pp6H9QbjhKKgBKuBIydFz_Th9KkoolGBvWNd13RoMNF6Fbuh9gsGtD1WoiQiT8wSC32erI4XzX7OvF6X6HX9n44uWslXQlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f927e35e14.mp4?token=Qgyo5zJbLOA1HVJS2qryl_f6tCMV6s4dRDlMYt0gK4HYxqLl-hbMXP8T0DGHtzrddZMf9FexVenZwdKRb0P4eCyb-29OlE2G-lwfKxxOrqstiVs71hYaV29ghndgrTV7tNAI0Bx3kfEYBoR8J4HQU5qT2rjLHDAa4VuQCC2V7W75EQG0W1W85vF3s8mQCW5U2JJflUhXCIrv8JjgDcjIpGmJ8rssndjB5et8lJdBEUpD7kFnbRHmK68Pp6H9QbjhKKgBKuBIydFz_Th9KkoolGBvWNd13RoMNF6Fbuh9gsGtD1WoiQiT8wSC32erI4XzX7OvF6X6HX9n44uWslXQlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو رژه قهرمانی آرسنال بیشتر از جام لیگ برتر به کون هینکاپیه پرداختن
😂
😂
بن وایت میکروفن گرفته دستش داره اهنگ میخونه هینکااااپیه کونتو نشونمون بده
😂
😂
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90594" target="_blank">📅 08:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90593">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d9e66e04d.mp4?token=tK0jsfaHswpZF4XlwQY5xyKN1S2d_et2kcwa3yB99wQq7hMUTcsAGsHVBe7CxTx_LGl8PxDCbYuVBRdxWNR65CtvxvHuwkBDiHMsh6MJS2loMcWjMvkjZaU9c5i70VYFGKkyngFXb7yIApPRlup7aDQEPcqEx4sKDLSaNwL8UYhcfxi8FaxN9K3ATVzPIIahfX8s_m_WkvrqQ1R2HIg0p5meDQ-FlY6-JdECGoUFhtH5n1Sy_CI-20IwyPPuI2s8j-u4bdsYnlunDGKVAWwxAxEc9EgatR4O2lK3pPVIha3-Ag51ukdO1m0I4zaQP3_AXqb2e8vYuhFTePcGkx4sSz8h3_ZJvSTXhbrhi7sk6QFmLEFKMf9nREEkIKhEqFnecaSaFX3z5LSjJ99L_CCjQpgpWpmdk_6yHT00_xg2PtZygTdoX48Qjl1EAuXJD3Z9770xVaNQ3Hibxg1TFmkRwEqTiC-q9v3wCkGKcafB06AMo8unV6oQ9E2zuWh62Rqv_Ie2-oopx4V4G4aJX-Zq7-LzAJWcSjuZoZskFNVxTs_Fs4LdUG30PX3kne-QQjpOoL4GkU58v3l76fhQEsRtRygXaxaK4ffkp1_sxvU8gizLj8OLAjqTxZbUGmM4NMQqd-4fPAT3AI9-tWCKQuk_8VimqnNb6mudpYToSZpUkwE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d9e66e04d.mp4?token=tK0jsfaHswpZF4XlwQY5xyKN1S2d_et2kcwa3yB99wQq7hMUTcsAGsHVBe7CxTx_LGl8PxDCbYuVBRdxWNR65CtvxvHuwkBDiHMsh6MJS2loMcWjMvkjZaU9c5i70VYFGKkyngFXb7yIApPRlup7aDQEPcqEx4sKDLSaNwL8UYhcfxi8FaxN9K3ATVzPIIahfX8s_m_WkvrqQ1R2HIg0p5meDQ-FlY6-JdECGoUFhtH5n1Sy_CI-20IwyPPuI2s8j-u4bdsYnlunDGKVAWwxAxEc9EgatR4O2lK3pPVIha3-Ag51ukdO1m0I4zaQP3_AXqb2e8vYuhFTePcGkx4sSz8h3_ZJvSTXhbrhi7sk6QFmLEFKMf9nREEkIKhEqFnecaSaFX3z5LSjJ99L_CCjQpgpWpmdk_6yHT00_xg2PtZygTdoX48Qjl1EAuXJD3Z9770xVaNQ3Hibxg1TFmkRwEqTiC-q9v3wCkGKcafB06AMo8unV6oQ9E2zuWh62Rqv_Ie2-oopx4V4G4aJX-Zq7-LzAJWcSjuZoZskFNVxTs_Fs4LdUG30PX3kne-QQjpOoL4GkU58v3l76fhQEsRtRygXaxaK4ffkp1_sxvU8gizLj8OLAjqTxZbUGmM4NMQqd-4fPAT3AI9-tWCKQuk_8VimqnNb6mudpYToSZpUkwE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
وینیسیوس دیشب با این گل خودشو برای جام‌جهانی کاملا سرحال نشون داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90593" target="_blank">📅 08:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90592">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMagZ-vfDbD8xAKYoE8mzzKReLVCh4ll8OwM9oEwEjKNcYvMgq699l1VGQJdcw4CvZhuuyaAdR8uYVODDy-BubAvEi2QZdQQZt-LoZM3-XJMQhxa08Z5pmnUAs4EcODGL3FOYj79B9YMd91RaagJ0BHGAIjFx_veNvlEhYQcBhU75jGcR0P-IA4jeAUrNXXRvU3sN1Zj6T_-NpdY7ufP1quvB0fgjw0uyV_T368szfizGAGWRYG_0JPp5gKVLJpmBn09WCnWz3kmtQUlaqAGqs5o4fFFGIqR4ptcC87_AUbHf_4ZhVVGYqmBwlpQKu4hGdmgp5Qqe5e8yhe37VzqPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
وقتی همه چیز متوقف شده بود
پرداخت سود دلاری اطلس ادامه داشت .
📊
ربات هوشمند
اطلس
یک سیستم سرمایه‌گذاری مبتنی بر آربیتراژ در بازار کریپتو است که با استفاده از اختلاف قیمت صرافی‌ها، معاملات را به‌صورت خودکار اجرا می‌کند.
تمامی فرآیندها شامل اجرای معامله، ثبت گزارش و پرداخت سود به‌صورت سیستمی انجام می‌شود و کاربران می‌توانند سود روزانه خود را برداشت کنند .
🔹
بدون نیاز به دانش ترید
🔹
واریز و برداشت آنی
🔹
پشتیبانی ۲۴ ساعته
🔥
ورود به ربات و مشاهده :
👉
@AtlasSmartBot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90592" target="_blank">📅 00:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90591">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
اگر همین الان توی سایت #وینرو عضو بشی
🤩
🤩
🤩
هزار تومان شارژ رایگان میگیری
❕
✅
من خودم عضو شدم بدون واریز ۵۰۰ تومان گرفتم باهاش فوتبال پیش بینی کردم پولم شد ۲ میلیون
❕
💚
خیلی راحت هم برداشت کردم کل پولم رو
💵
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر،…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90591" target="_blank">📅 00:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90590">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYRTcUm1XEkonXMFoOqqWDLZt2it1Ln920xHL6TARFD7YKYH1RSR6MMfN0525uOUVNsgeybYKk6NqPBJasq-ysbfB9z3YTF8InngjOhf3WMfniteW18x2zdu18VBg1AL42tLppaBnQv3ormIrjnVLih3bot2hXusLKhWPJzhfs-SvXD1gKKKDT5wAV0prNJan8JouP_GQfOXZScbFij_z1GGh2lxfWA3rbwI0ufUjACo7F7vPZGDrkaEE6pgsCkww-E2Yr0t-1wI-6Wi8lpp25sYNf8SnIMz44JrfPFbYBfqML0DgFXp4xl2uP63fe5E--qA53T8UMMlrHqWRKntEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اگر همین الان توی سایت
#وینرو
عضو بشی
🤩
🤩
🤩
هزار تومان شارژ رایگان میگیری
❕
✅
من خودم عضو شدم بدون واریز ۵۰۰ تومان گرفتم باهاش فوتبال پیش بینی کردم پولم شد ۲ میلیون
❕
💚
خیلی راحت هم برداشت کردم کل پولم رو
💵
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
🔴
این فرصت محدود رو از دست ندید:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
a10
📱
@winro_io</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90590" target="_blank">📅 00:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90589">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0ItCHsxD0-uslZ-b8JYKyF19eGJJeb6rgG9OclQtt5rQC2hUFpaRGmsy4T9KlxfN36tO0_RSf7fG9lWMi2k5C7iXgPyj3wy-na0Ja1twe-ueA5SGwgv7IashmfMt7mzAhCUsguqmx7qobXFMW7UOwJkRwRXqKix-1NxbfejcgZ8Apndr4quk1M83O32JeWPC6Eta888sWM6lEmD-sc8GT5lB5_tO_XXYo72sR0n5ZGZa1Diz_kWIP66Hb3pyXg3_7WnPHSmbWXbSgZLV2UlhV1oBvDvpYyNMKef7oMwkj5f2VY1U1GLpLMM88fVF3H70vVOfPx9GOh2kOgw7YgI4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید از اسطوره های فوتبال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90589" target="_blank">📅 23:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90588">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🎙️
مهدی تاج:
بازیکنان تیم ملی دنبال پاداش و حواله نیستن، هدفشون از صعود فقط شادی مردمه
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90588" target="_blank">📅 23:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90586">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCl7xKa_zUz9xtWuQP1oTvYJLOjx-19tujirPCXNE-LSApVfz2KRLmgqllhpOmUZxy31IOUcy1CR3Kir5KMY_amK13JerIgdX8TVBMVassw1iXN4uCQmxYrIDFR7fbMouNDdsfGKyEOyC_ddVLwPeVpzQJkMJTgBalef7xg9yUh_vruTFsqth_eWgbBbDeZA1yz1EJhfRyMCpYn6OpMwS3p9udKkdV7AOSUJXGkWjN9TSE5dq_axSrv3ppXS-jDsp5bIl-ylDmjxYbU7R8MdI3wZEFP49SwGftwXvOoLQPu9C9Y-6qiThaHcnk6Lwo63_M_6sysIIJ_K3UwTMX5PTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
ایندیکایلا :
آندونی ایرائولا سرمربی لیورپول شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/90586" target="_blank">📅 22:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90585">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0yEEFV3sZTIH02QJGQGAk5AeE4mmnD1qMMW2jgsR_2yB756YUzJytb8n4NPrROAlRqbNbSHlOlG5kP4z6xotO-KIKzwA5IVNfMvqeoFvoZ2d1_SFPfen1OXasJSltT0PzB-4m9zWproC0tZqfVq6bb1frmjz6nt7YCeSLbfipOzEcxOUJDI6_CL3vq9ka9EEqrq4U2Vao6XJucvat6rxiztHgdx3dnMfKwDZjOhHlnxdA0vGYNWxe2YYCOyJmbqig9LrjmTic_3qs6PcaejbFwLncP19tchPQfq_M3OgvOKQMFxD-FBD4GsvNAfASLl9T9BwRDYsoaOlXsUFhjLSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوورییییی
پدر آلوارز پیج باشگاه بارسلونا رو فالو کردددد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90585" target="_blank">📅 22:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90584">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5wBtCNXI7oaGI-unNwmtxWU4UpDRjf7ED4pq598zlaG2LLOgMPqPKvj5NfxARAdrcEtDoTq6f6wCQZ_2r5gE1RLVI8KpER8ha2NB_K3uLEFQQTj1Cvh9715gw_aDyJXHpg_Vr-WlZDt-FGWLyRy7zwlUlV8wIcUWQNsw2yZvup1888FeJ4K-T6hxBMOwFFX9r6V21nmHiGsqGT4VkwqXHusqHTfx8CKdUkQv0HSijez91FFBgSFBIKP086pyQahkziFOj5RF_pry4oj7oFPh8hdXjMK3tcUYL4cvGfQZ2OV56Jousmk-NBPNvIge_uYlK7MFsF62V87MhWXZScU_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نروژ
🇳🇴
-
🇸🇪
سوئد
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
دوشنبه ساعت ۲۰:۳۰
🏟
ورزشگاه اولوال
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
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
✅
سوئد در
۱۰
دیدار اخیر خود،
چهار
برد و
دو
تساوی کسب کرده و در
چهار
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر نروژ
۳.۷
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر سوئد
۳.۴
گل در هر بازی بوده است.
🚨
نکاتی در مورد بازی‌های رودررو:
در ده تقابل اخیر دو تیم، نروژ موفق به کسب پیروزی در
چهار
دیدار شده‌ است،
پنج
بازی نیز با نتیجه تساوی به پایان رسیده و سوئد در
یک
دیدار پیروز شده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۱.۵
- ضریب :
۱.۲۷
🧠
تغییرِ مکررِ سقف روزانه، نشانه وضعیت ناسالم است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/90584" target="_blank">📅 22:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90582">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e5c0ed52.mp4?token=dvQ-J2fCOT5yqC-6XWOvJth0uBIjk99B9EosC2GvCmNoukzdfaRQ7pM93b91A_5T9aaou_nqrm181mdfINDGFBlqavvqStTGBNJtgaUMgTFNaD1Bs0hRq9JiSH04c1ndmD9hw-sFeEqWCFZRjCnokRmHwT690iPoCkb6g6_ootoS9BlaLaZ-aNlQQYeKpL_LL-i54XzUApOKBTjaU20g20yX8WaNQ_eWcHOlRseXZTpkc5JJBJ5CuZf2el829I8m6ciXUoWoyeqI3CfzkslOZPIO7lfjypgi9Qm9BABRdtJQC7CVsbMDWpz_XC7hc6AGWY8UBgprZnFJM7jMG8a98A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e5c0ed52.mp4?token=dvQ-J2fCOT5yqC-6XWOvJth0uBIjk99B9EosC2GvCmNoukzdfaRQ7pM93b91A_5T9aaou_nqrm181mdfINDGFBlqavvqStTGBNJtgaUMgTFNaD1Bs0hRq9JiSH04c1ndmD9hw-sFeEqWCFZRjCnokRmHwT690iPoCkb6g6_ootoS9BlaLaZ-aNlQQYeKpL_LL-i54XzUApOKBTjaU20g20yX8WaNQ_eWcHOlRseXZTpkc5JJBJ5CuZf2el829I8m6ciXUoWoyeqI3CfzkslOZPIO7lfjypgi9Qm9BABRdtJQC7CVsbMDWpz_XC7hc6AGWY8UBgprZnFJM7jMG8a98A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عثمون:
سال بعدم قهرمان میشیم هتریک میکنیم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90582" target="_blank">📅 21:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90581">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDOy_o0dJFVpf7BWAZs225uRVbC4-MmsrIURNDbI8pTzh_RrvEcquJGBclMONw1Czer14Yzp0vp99BClp_VtBxhSFg11jAx-FbbWr7EBpR7PUIq0xqfJD5SEbQ2SrNLl236ysYmfvod0e5-yXQRngo2k68NQ10prYwan6v-AjpleSqXbiH35Nu4GF6_HExMKbod8Qj40WLEihB4-DEz_sr-LYb4jgvA9g9ttV8N1wwC6-289km_YtoUWEyfIgKf6U1ZV4B3bECc8r0L6iIIgi1ozcb4FHWRZbt0AyvImL4KA0KPO9gCOCxkX97fY64k-OUlh2sS4dEFnD1BcG49wZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و جای ژانا همچنان کنار انریکه خالیه...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90581" target="_blank">📅 21:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90580">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f41d871c.mp4?token=OgWzE5jvuIsECEPz8WZVRCmNZdS0BakEP99jJ5dvvPryiWMsOOcTjmsVQOMXZorodS6H6K1LRtrHAAhLa10w3QnFvb1-_pnIig_H84boWhZ0ZkAGSOjfEWOi7SBLXoqdb4HUsLoDrN3O-mf10YM_tltLLTp_Y2v7ix6EYgUFK7Ec2rZCfq2AlNVrsdeXqInG1PGpSENhc7_09B0B2iN9MAz3-dVnCAgR5eKapt7qBl8i3QC2VT3w9kA9s8yGteRqNHCyJu1towD8Ie90U0401w43iRJkPL0gxriHesE0q7J0SucoPvcQ44POnrrXkTeHmQiXmPRcstEiHfQWZzfvQDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f41d871c.mp4?token=OgWzE5jvuIsECEPz8WZVRCmNZdS0BakEP99jJ5dvvPryiWMsOOcTjmsVQOMXZorodS6H6K1LRtrHAAhLa10w3QnFvb1-_pnIig_H84boWhZ0ZkAGSOjfEWOi7SBLXoqdb4HUsLoDrN3O-mf10YM_tltLLTp_Y2v7ix6EYgUFK7Ec2rZCfq2AlNVrsdeXqInG1PGpSENhc7_09B0B2iN9MAz3-dVnCAgR5eKapt7qBl8i3QC2VT3w9kA9s8yGteRqNHCyJu1towD8Ie90U0401w43iRJkPL0gxriHesE0q7J0SucoPvcQ44POnrrXkTeHmQiXmPRcstEiHfQWZzfvQDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
پرایم‌گرت‌بیل واسه دوستانی که فراموش کردن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90580" target="_blank">📅 20:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90579">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/870d923735.mp4?token=LYnMZu5-fEQ3JpoCm1rbAuIHFNjgwBXAzLw4CjRr1N8IxjFJevOjTODe_4CsJaHJiDgH2LqhAxGs6GaH41RGpjafbYwYl95mG7476lsHgco-0cTDx_K9Aa8GswF3l_E0N72RGmeyPnZkjIfj-ipX7_O9yrsAexMIw0QGDnm1kf4en8sNL-RmGnTQ2VzzbKsE_YyYbnU0w4wOCP458eqqg8TDPTfyvutAPeYXf9gpzbz7utRZQIa4oMS6t2qePCoKpK7LLYcVnDj0zrSVUAVuDENIrWAAgeITAtg_JUR8Cia5e1nVC96CmSBiOBEz3yZeU7bzoYOX0eu8Yw4E1u__KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/870d923735.mp4?token=LYnMZu5-fEQ3JpoCm1rbAuIHFNjgwBXAzLw4CjRr1N8IxjFJevOjTODe_4CsJaHJiDgH2LqhAxGs6GaH41RGpjafbYwYl95mG7476lsHgco-0cTDx_K9Aa8GswF3l_E0N72RGmeyPnZkjIfj-ipX7_O9yrsAexMIw0QGDnm1kf4en8sNL-RmGnTQ2VzzbKsE_YyYbnU0w4wOCP458eqqg8TDPTfyvutAPeYXf9gpzbz7utRZQIa4oMS6t2qePCoKpK7LLYcVnDj0zrSVUAVuDENIrWAAgeITAtg_JUR8Cia5e1nVC96CmSBiOBEz3yZeU7bzoYOX0eu8Yw4E1u__KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه صفحه هواداری اومده گفته که داوید رایا با این سطح هوش تو ضربات پنالتی نشون داد که اصلا‌ گلر خوبی نیست و قهرمان نشدن آرسنال هم یکی از دلایلش همین موضوعه!
این صحنه مربوط به یکی دیگر از دیدارهای آرسنال هست که تو ضربات پنالتی جناب داوید رایا قبل حرکت بازیکن برای زدن ضربه، شیرجه میزنه
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90579" target="_blank">📅 20:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90578">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">امیر قلعه‌نویی:
چیزهایی که سه سال اخیر به دنبال آن‌ها بودیم، در بازی با گامبیا به آن‌ها رسیدیم. بازی با مالی هم محک بزرگی برای ما خواهد بود
😐
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90578" target="_blank">📅 20:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90575">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daioRumMAQ1Y9OcdYae9sFRe7D0gan9yqmce3Vbu03Os0QQqHPhTyL1amn3Sc0EMhMWVjm9FdH2mfPfqabcY8KN2rsoiQm8qwA7qxpN_J1kXYrjHu7RRXR9JH8dwn4mrsNHLyJa3CTg9s91yd3LbgQp7IwyY2AeLjjorW2q80B1CF_Fmh-C4G6QC1HGTmK-idCcGb4AsIn2Tx4ATRn7PFotP3ncxmzaqXbJcxy65Z7khQZTbeHUhrK835NM51JELpmWorgOqhnCwC3GAeyF6XhhuWlPfob_CxytYucus3Yey26IqfdL80q2N0xcw4eQSZpB3O0tHbroyPFrriP898Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
در جدیدترین آپدیت تیم‌های برتر اروپایی، بایرن‌مونیخ همچنان صدره. پاری‌سن‌ژرمن به رده سوم اومده و بارسلونا جزو تیم‌های برتر نیست. در مقابل رئال‌مادرید تیم دومه!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90575" target="_blank">📅 19:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90574">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
‼️
دیشب قبل بازی فینال یه هوادار یونایتد میاد یه آرسنالی رو اذیت می‌کنه که در ادامه ببینید چه بلایی سرش میاد
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90574" target="_blank">📅 19:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90573">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HM-z-ASALi1lo5FzzIx23c_n5TAc-jsBkr_Nl9TFZqRouXdcvyGBFohiPRxdG4if0Q94JH8O01yJCGuSUew0AijNtTKbqheJbEQFKeJHA1WcMbXhKOqZUALluJt_b_fvzYokE6e-NYLEOwYZr1Clrn2mCYBQlXaITabZOZgzWVsx13-g3-ysrJViB_-iU8b19IPFGVmS7xUuIqdPK7MJRvFLIQa2rcFHUrvqvxXOCZ_4X5UrvfDQL7GTgmvnbSznSeMpRklARryTs7groWCJJeOxqZgn3JrEqWXBe6pe4a2WnRcM_6WlCZhHEaKEqmHaZxawsahjUz2n-xrX0-iWbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
کواراتسخلیا به‌عنوان بهترین بازیکن فصل لیگ‌قهرمانان انتخاب شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90573" target="_blank">📅 19:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90572">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">💩
⚠️
دیگه #فریب بونوس های الکی سایت های سودجو رو نخورید
❌
💲
بیا توی سایت مورد تایید ما یعنی #وینرو و با عضویت 500 هزار تومان اعتبار بی قیدو شرط بگیر
👏
🤩
با عضویت
🤩
🤩
🤩
هزار تومان اعتبار رایگان بگیر!
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io  کانال بونوس…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90572" target="_blank">📅 19:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90571">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqqgBU8gg73ozXRXodIzzRRHNkKGF1JHmkVrs1sXQxaRtm4eQyTEBLfXZ_p05dfwMktrnUbG9IgxashCAIWyA6k7FSVB5xVH6RlEwWOexM9Zo5rHD8YkNtAeW6jtKsSQ-Oaqx6Ku3K6ycXmwjwnWVpLux2aZ98GUNsL2QVDLlpo-n5Z9zyjjdHMC-M41pVWvYa28wH6etW1_FTekVoJdqifwvzX3UQ382Lmdn1SBrVX4tAkeMTlerSYj0JYQzt0LLic1BoyACQvboC5lWB_9-MMY0kQc0y2z9UQaJ_IUG_Y9tMjPXtVwPGSjwr9iqlG41Cx1DKdOq1eYF4d8yGvrew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💩
⚠️
دیگه
#فریب
بونوس های الکی سایت های سودجو رو نخورید
❌
💲
بیا توی سایت مورد تایید ما یعنی
#وینرو
و با عضویت 500 هزار تومان اعتبار بی قیدو شرط بگیر
👏
🤩
با عضویت
🤩
🤩
🤩
هزار تومان اعتبار رایگان بگیر!
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g10
📱
@winro_io</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90571" target="_blank">📅 19:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90570">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
اتفاق عجیب در یکی از بازی‌های آمریکای جنوبی؛ یه بازیکن وسط بازی سکته ناقص میزنه که با خوش شانسی محض و اقدام سریع، جون سالم به در میبره
😕
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90570" target="_blank">📅 19:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90569">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کنفدراسیون آسیا با مجوز حرفه ای سپاهان موافقت نکرد و بدین ترتیب فدراسیون باید یک تیم دیگر رو انتخاب کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90569" target="_blank">📅 19:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90568">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VED_WD7HE8HGqO1NqVSeMpkSLJPlcq5akzG-mWhEQQVKiENHOeh36-X8YehjgurYAm7tBQ3_BxUQnRidnHwHTgDAsYIaQJNqmLP6vSRCwjuj7DhG7s6z2Sev96BehJaICL2X0veIoeQRm93HBwoDKtyc9ZVB-GMlTTHQSFsgvnsiJn7twu3SWJwRjCMDG_JSCdyux2jLpz-I4gRfhTGdRNVbshZprtbgwhfZuBWOv7GWxYvO8kKQjVvxvKkfC9g6THHD1M4PN96MkIYPD7jN8Xs5s0cps1lReldcoY8UPu90GDiLJhhkCq2fzI-f7q3LnevQr3BidZ5RWLlPXQ_yOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم‌ منتخب لیگ قهرمانان اروپا فصل 2025/26
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90568" target="_blank">📅 19:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90566">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qcj_iHazqnDFzoh9BEH0iJqOjIRsYrqDuuNndugg6Duo0uEa_EH0RJLDLNXJyMPtMMVzGmOjNZKeEPY91Ww_IP2fV5QPtM54kNAMQ5bniR8_2-3kD-PAW7rSAeYNgxGTgNF3UGLyWfVfnx2Dy-FG6QDcJBC0MZ63yOrek_kle2by6_hKj2Z6mVC7ZjsTfFbRxrXNr3_lcBdABnaDo3Fjvd0v3u_xJeIMlI52DKJlKe9hVQ-4wdq0c0gCRls5WROU5cGenm8AGOm3HizWyX04ov1_y5ILJu7t2EZ913EAx-IBTlFGYvSRnikGeTPWJvcsk3mHlELRVv7oyoPltjeMmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حدود 1 میلیون نفر تو جشن قهرمانی آرسنال شرکت کردن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90566" target="_blank">📅 18:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90565">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c385efd6aa.mp4?token=YYAmspNC_2_1ie1YObzgYP8bd6dZyqye3bh0xng95SGAxukPoXrqSG_u3Bw8HIk5bDaQdmS97EbqNcxKH6HaaeZV66jDvKR0hmxBNwn9M1DPYU9ApOjdUuhbI6m1_AL69V8tIWH1wda2DavizRDyla7dkkaOQso-wsHBdSzfvplldineacIUCiXNP3uJg5r5lA9ZCT0J1oYjuXjCwFo_68LTKyXbTBYPM-_vJCaS60aRvDkssnzeS2nwf9o4BddQdp-Nq7mUat4mK47fVGpbJsQn5Ht7MAWTOwE3t7hsukVni0teaxw-oR6iW9iGx9tRq2wpiTLdpHPptEmXG7PnMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c385efd6aa.mp4?token=YYAmspNC_2_1ie1YObzgYP8bd6dZyqye3bh0xng95SGAxukPoXrqSG_u3Bw8HIk5bDaQdmS97EbqNcxKH6HaaeZV66jDvKR0hmxBNwn9M1DPYU9ApOjdUuhbI6m1_AL69V8tIWH1wda2DavizRDyla7dkkaOQso-wsHBdSzfvplldineacIUCiXNP3uJg5r5lA9ZCT0J1oYjuXjCwFo_68LTKyXbTBYPM-_vJCaS60aRvDkssnzeS2nwf9o4BddQdp-Nq7mUat4mK47fVGpbJsQn5Ht7MAWTOwE3t7hsukVni0teaxw-oR6iW9iGx9tRq2wpiTLdpHPptEmXG7PnMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست اکانت باشگاه الچه
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90565" target="_blank">📅 17:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90564">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPNdcE3SmKL2q5CB8aBX58RNu7Nz_tdIOdgT-1LtrlnsMJM9f2EoLvLXoqZnZsrgPeAz_8XAbrryy8Xy2S8_LPUwvYB4RHCEVdZXnb5DgokgIzAAsDtHXvyfd-u4RqBDLTT6ILO3Kut0urmYCCASU4KFecWqZekhkMv28ZpHSb4hrPIknNE1yvcW49WU15cv8xbf5rCnT9pEK88wDj6oym8Bft40celVUdbAB4qrwNBIx3JMvrV1Dj5RNm1_v-IlZ_2Mz_YLAXjcbLGk7zGPthu0WEQTUUYhbi0fARjR0nGbtyS5VFKft1T64WOBcm1cycRYvyH1aQJ5FboW_njiXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بیشترین تاثیر گذاری تو لیگ قهرمانان این فصل
🇬🇪
کواراتسخلیا : 16 گل و پاس گل
🇬🇧
هری کین : 16 گل و پاس گل
🇫🇷
کیلیان امباپه 16 گل و پاس گل
🇦🇷
‌ خولیان آلوارز 14 گل و پاس گل
🇬🇧
آنتونی گوردون 12 گل و پاس گل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90564" target="_blank">📅 17:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90563">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f90b184b2c.mp4?token=IiliLULFDMN0AVcTyqSFMO4BWXgoboQbXEw6VRQYC-0JRtcusG0Z2JfdYueyTM3tnLMih0tQ9vAZnCwgJ7dcxzXC735XIDpzfbc6-ye_QIQmwb3TcQWjggxgn6Zra5gVzf1nNYsa1ao1HxnPz-EZoIsuAHWO6tC4oP03CR22fJgXwY4S9r0Jaf9JJjvJ6JWPsyJXtNZwbN4-evEwIPug1pyKmCyfs6YDVHmZdmPc0LH32tAcRdQq8Fl1JThZK4NeUFX-o3xgmVQfl6e5z6g3QGhVPhi5RPXsTd45oWYMV4TY2_q5vYPUGTyoPGI2NKsIdItxcXRCYIQUQnBCoDK_1gY2bfs7AcBjUo8P3qxPZE5nQ8QiSLJMcl_NJItHjDyKdHMp8Ff-LKFFqvcRP4GRyGtfdoZeG0unCKtSF0r9d_9QP_3wZD0L85d4gef9swR4mfdtrxfLm7-dTJAxY467Llw9E4UbG1TvCX0Gcvghy9YBaUcuDGsNHWPlLW09-mWCBpILiE_8V1RN-6_iruQo7WWNB2iuOYuqohrFKKCIAg3tYeMPKZdbZidYwbiFnzGXG-2FeW-ZWYH__ntv14Vkt6Y8IFZwwVZ8JiPTqe-757FGM2ZEhRQ-rJlvY8R4SO9qLkYsglDxND5fCgkcmrGhWy58dw5abqU7VJfV_VYwyY0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f90b184b2c.mp4?token=IiliLULFDMN0AVcTyqSFMO4BWXgoboQbXEw6VRQYC-0JRtcusG0Z2JfdYueyTM3tnLMih0tQ9vAZnCwgJ7dcxzXC735XIDpzfbc6-ye_QIQmwb3TcQWjggxgn6Zra5gVzf1nNYsa1ao1HxnPz-EZoIsuAHWO6tC4oP03CR22fJgXwY4S9r0Jaf9JJjvJ6JWPsyJXtNZwbN4-evEwIPug1pyKmCyfs6YDVHmZdmPc0LH32tAcRdQq8Fl1JThZK4NeUFX-o3xgmVQfl6e5z6g3QGhVPhi5RPXsTd45oWYMV4TY2_q5vYPUGTyoPGI2NKsIdItxcXRCYIQUQnBCoDK_1gY2bfs7AcBjUo8P3qxPZE5nQ8QiSLJMcl_NJItHjDyKdHMp8Ff-LKFFqvcRP4GRyGtfdoZeG0unCKtSF0r9d_9QP_3wZD0L85d4gef9swR4mfdtrxfLm7-dTJAxY467Llw9E4UbG1TvCX0Gcvghy9YBaUcuDGsNHWPlLW09-mWCBpILiE_8V1RN-6_iruQo7WWNB2iuOYuqohrFKKCIAg3tYeMPKZdbZidYwbiFnzGXG-2FeW-ZWYH__ntv14Vkt6Y8IFZwwVZ8JiPTqe-757FGM2ZEhRQ-rJlvY8R4SO9qLkYsglDxND5fCgkcmrGhWy58dw5abqU7VJfV_VYwyY0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برزیل از همین الان یکی از مدعیای اصلی جام‌جهانیه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90563" target="_blank">📅 17:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90562">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRNzdS04FSfHaENVOZVGQ75p6o9l8Oi3T4IiqdFcrefPOGx3NI1HoG5EVlBhCfOZ0aCTBDfDuUNuSUurJjXz4ffR-inpGwzZQx7FW3SC1lzbWnhvUKLKB9W1apWCyI-F2rk5xJSjhCyMkq2cal6y1o7KrQGbgGJyus8J7dF-X2pNa9kdGx4_PfT8Rl5GtEeAtVd3P2s39LrQLcrrulzKXVeo_jSA_qSOUDKb1oU71vpwBWAAMlEVw7nDzlgjzQ79wi8jQxeF1Af2WvpWYsb4UEyjiTI7lZC7N9a5Gaw6mnj3VNeqggLawnLv21WVYPPBPHVn61LZWyIOWwkL5gtrvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نونو مندس ‌23 ساله با 19 قهرمانی
🔥
1 لیگ پرتغال
5 لیگ 1 فرانسه
1 سوپرجام اروپا
1 سوپرجام پرتغال
4 سوپرجام فرانسه
1 لیگ ملت‌های اروپا
2 جام حذفی فرانسه
2 لیگ قهرمانان اروپا
1 جام اتحادیه پرتغال
1 جام بین‌المللی فیفا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90562" target="_blank">📅 16:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90561">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSbnc0agg6WEJy2UdZDsfZTOkCKYwe6-z8hLfh5hOp6y-JjQRaWCdhusDroCrfp_ceDQgE6X2J9gQvXhUkeNqdCkHAfBrqvpIH3Zn2T0XJpMRnVIcCunm6_2jdBx4UHLcQfvQkD-Z5EGSJauWhmCKCqONL-27EPyztIvY-4tzEzjBS8GhbFYmuVbOKdrVTijv5TmgeiH2D8uLzORP_Htyviz_63hNlAK_TTqrEaNlFxfw7YDCcaci0DzKLgeOlSUT8-ATeqdDIQ-ST97Uj2U0BHtOaD2aJNpD4MnHeBZKSL_mvNNzJxz-xlOb-GCaXBimJK00XwZ8DW6mOVnUYivGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
🤯
🤯
فکتتتتت پشم‌ریزون اینکه ویلیام پاچو مدافع پاری‌سن‌ژرمن این‌فصل در اروپا هر ۱۷ تا مسابقه رو کامل و بدون تعویض شدن بازی کرده که یک رکورد خارق‌العاده حساب میشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90561" target="_blank">📅 14:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90560">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJeeLgaPHzD00TrhWlVs3JLs-FMEEHZ--xgzhrHwf_BVyUmwEw8MxHDrEzw-y_fFokmqEYd0CAZ3wL4fChKIS5X2E-DrEuNA5-yIy6Iqz2n2iSvqqauwMFhhnFfl8VTlu8qF8-Fxv_mNQ_BzLrlOhR_ldDsECmh1Tg_LSHEY229jHjgaYqVADIPlaF5GxNSB5ewx-d_hgKs9VQHszDh81xtTYDQ9opjKxxS-axAWmZBQnTpcIDLfbNfNNs1S_3FQi5azSYnHXCGTzpqcuwjmhbU8nlVDmVQeV5bY1cTV9zgPjgH3K0ooDa5bTgW8UQoYq8gZhF16pLnUKwHpdzCJ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
🇫🇷
وقتی صحبت از ثبات میشه؛ کافیه بدونین ترکیب اصلی تیم پاری‌سن‌ژرمن نسبت به فینال پارسال تنها یک تغییر داشت و اونم گلر بود. خلاصه که نون تو ثباته و ناصر خلاف خوب بعد چند سال فهمیده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90560" target="_blank">📅 14:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90559">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGAl9qILkm9wRMKp4TnqMUlmdJac72jVDNIS27jljVaKXs1YMyGVgvAprphc45-7bn_HAoX87LAsVWVEaZtSflI69doqa5jt-6I7RDV7R_ND9MZ9iPDQ0u5veP8YWYTQybJ9aozeYK5zEK4OYhRiXVMls0eE7BJX12CK22vZ_7KTk_cQjzSqgHIZ_HGxhvbDDVb-0vgOD6M4zomvmjF1IQ-fAiVLVWm2pS6EQZxOBxHlXo77uFRpe5nkoAASIRN5mpz9C9MI9U_iiCS081jWEeE9G7SptUIksPUsHJK-SeXdHP8QtZH40d7ikzClqZh6mlz3oETez-jCozq3qZ_zBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استایل جدید صابر ابر بازیگر سینما
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90559" target="_blank">📅 14:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90558">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADJ5m6xzMliercUXfHw94TW6kWEmRDP-hiAAfql9BRcC0nhWGfAuptZFZME1HuHZXfyYbCea5d_uj-h3TyIoCnoz8qhHQkHqruxtnab84GWOr6hbl7Kbgzub6wWSpSZrbMctcY2wbTde0kpi38oE0L9gqErleAT7M0Gso7QCZ5EkmcHKboJkSPCCeKGZhkd6RDY2P3hoZXvUa1RqoWtDBl-LkcTrpg_LUrYmnF6WV866_qY6Kpot7zdAIh0gs52NxqSpL90CThEgavPROecudOc0ti5my0aXFZ_3UZDdboryv2Ug-Xc7s8VFgoelLStIm5m6ADNxUDIoEJrvKzvCRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
‼️
کوارتسخلیا: بازیکنان آرسنال بویی از رقابت جوانمردانه نبرده بودن. اونا خیلی سعی کردن منو به بدترین شکل مصدوم کنن هرچند تا حدودی موفق بودن ولی درس خوبی بهشون دادیم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90558" target="_blank">📅 14:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90557">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0gOCU_4kqIzTz6z7GjYn_Hwaq2Oqy5HxPcfh4HRlaEcZKZA1bT9Nx4UgMhn3EWglQSyfkdeLnbX_zXIenbWdpvkumBqRKdD5sAK6mQRMwj33kVWcT9L8YSLihXKAxB3OSNdgEcldnTY-PJT6K8f1APdA6uUgoPGMz43H2WsDwhQtIVPHuGLS12eklTOkpuElvnZLnjivkhRnh8-WwGGUv3dGT83GvDFjq62VdV3qeLb0QFhZFxWrRIQzPzyN6WMWbx4BDQ7QOITVu4i-h8khhp2x8UemcklOWSnFJj_lbsidN1uGxZGH5uC5WCJf-uzPzkvQlYEwThFTrOTDN07LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
وزیر کشور فرانسه: در‌ پی آشوب دیشب خیابانی در شهر پاریس، بیش از ۷۰۰ نفر بازداشت شده‌اند و حدود ۶۰ مامور پلیس شدیدا مجروح شده‌اند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90557" target="_blank">📅 13:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90556">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vc7gu0utaN3LJ2Dsw6hg2eNSP_ynsfP8Xd5aCz9krujicLX6qORgN1G0XYPsomdiVPU0DYI6UlEQsgKVHpgkBwQL9WLuc3YuQuwBYgC-N7IhqZhPHAdG1LJnvID5zJEl2hm5B5wcV1U9ZpAZs3raza4d2k4Qrj_0PJYpBX8vdnWUxUKNp2nDc9ANA9X60J553My2uedr356BKzwb8EJmCtCqxTwrZoIJ8e4wWTjPkGDKJuu-Df6BZoa4A3241kec0jsJLf_lDCrXPnFeeKJ0rFpzNLw7zzJgQVEjt5LtOcdjZ_WpdfD7VB5CSAEYxBTuXENtOaP0KfQZi_p0jP9zbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
وضعیت وینیسیوس و دمبله با و‌ بدون امباپه:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90556" target="_blank">📅 13:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90555">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDEyqUSRx1Yu9oneOA9wJeK5c_QX38mNANa6antEe-cRupv8g6b2pI2uXGDRcZm2hkXM95hOsimy15gC8oNUAQpk2SOF0EWBU70MCk5FlFIgdzrxID75fVCNuH9gbtJWnOQCOYKfQbKkDdWagm4Ubi5enG794bbbd07-yoaxWx3sG1zYrGUL8zkn4UskW0kdn53KwI6VE7_b3Zz8IS2VhQs1Jc92trDvM3k2hZLRGXbJPgZplBqwPyJH1UbiX_Wpjvaz9RmPvU5jcbkBADlPNhNgiI0sbQmqJQJPO5DqiDGasrnubr0MIomaDUQTJUfF7JOIUIpiiUqvus71AKWCaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مونیرالحدادی بازیکن استقلال و همسرش در تعطیلات
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90555" target="_blank">📅 13:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90551">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba8df4a4da.mp4?token=uzSIqLZ3bGuRQmJrbnTOmlbLI07EbdENVbc0P5-JLQhYDQaOUtIIIjdov1ZI2XC8fniWjz42Od9AYd8C_qXQ9giiYahK4XRpeJhYL5M47fpCWmrJuR13Pi-IrXS6QFnR3pkRdhP-nTlp_LJkSK5PVZExvAdRLkRvrhtSXqQiGXgAMS5tUJ18rhiz_xnSbs_Q5LqCNfntlsocphbWv6ZARMqHR19VLhAuCFliYCxOxPbp2cAs7kc4s5KWNwHjqHQiiFFGAa8ERrWABx39UAjHY-ctJ6-6tLljYW76CdXKNLyASTCiPLJnbRkenxevbF-inaB5h4k7qv84xFbZ1wPhFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba8df4a4da.mp4?token=uzSIqLZ3bGuRQmJrbnTOmlbLI07EbdENVbc0P5-JLQhYDQaOUtIIIjdov1ZI2XC8fniWjz42Od9AYd8C_qXQ9giiYahK4XRpeJhYL5M47fpCWmrJuR13Pi-IrXS6QFnR3pkRdhP-nTlp_LJkSK5PVZExvAdRLkRvrhtSXqQiGXgAMS5tUJ18rhiz_xnSbs_Q5LqCNfntlsocphbWv6ZARMqHR19VLhAuCFliYCxOxPbp2cAs7kc4s5KWNwHjqHQiiFFGAa8ERrWABx39UAjHY-ctJ6-6tLljYW76CdXKNLyASTCiPLJnbRkenxevbF-inaB5h4k7qv84xFbZ1wPhFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لوس بازی‌های قبل ازدواج لامین‌یامال و دوس‌دخترش که در فضای مجازی وایرال شده. فک کنید ده روزه دیگه بازی داره زیدش هم اینجوری میذاره دهنش
🙁
😔
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90551" target="_blank">📅 13:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90550">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qs3vco8O8L2hCGxxXoKzY-ZTSXQWn_WpNcWNcf23snDHie1gvjoWIlebzoPDjhMMulK4aquJZ0_BpbIt1OFcx34NaHvP1yxzHFSSgQYBqDPNcPb5Raar9ap0nH4oQZAOtsu6Br0idgo6ZCr0pLIZjWLkbGbGvQEC-puxdjCFFZl3AOS4rTRhalZvqmtxBLL0f1QnKoifPZ_52H93L_4_Cx5V2hp9FP2J7zj6h97H7RbFujW2t-YMndGCbTelc0gkeNE_S2dVEv6Nc9xnVDqnhpRLdSUF7wEsJ_GFJOsXBJcbDWb-t7pnOqpWU3sl_r-nk_-r0dbOJ1_A1xSZpXTCyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ روزنامه‌ اکیپ فرانسه مدعی شد که ناصرالخلیفی به مارکینیوش پیشنهاد داده که بعد از جام‌جهانی به تیم الدحیل قطر ملحق شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90550" target="_blank">📅 13:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90549">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVmxtgLg2mDA7avYQUQK_TA2xW479VKz_Oq7awXQo4MUAXuEj31mXYbi0LbKS4R0o6iMVt0ze5Wk5HfHMyu9Cp4eWEQkpbXBlhY7NOYKfCYWHN01JE01gpfxD3ny1Hqf_fNDp32m1PnVSeQwxgRksZvbMkKEKknLSNxYNyI1vTgMI73IWT36yfcFmwy7RF7aUqUukeTlAKpzhiFga2FpzABsNIVcJ1QnNz4MkG9VYx3axGjAUROr8z6CZqa5vM-LhoZY1kbIXEgTXnbSl6h_dEl5_Gl9wVEeSHBz-kDRtWdbwCw8lWcj5hxrA7v-f4hQNtFYcTIYHUeovVxt1H_pxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخت و اقبال آقای امباپه رو مشاهده می‌کنید:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90549" target="_blank">📅 12:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90547">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11672147cd.mp4?token=gmsIOBCnrF2ip3i99B6qkuURpKjnagtfRZRjXrrvz4s4UGwdQ83ADn2qSlq8D4tMnOZSqhQMoCCefmoW8vkAV1N32UE4DaOS5cCCBaLy-xn3GWCDgZ19JTfFcDu4LD6F7mJvoHVgNrVTqQWS1jFpWaz6rmWixFCwFHaBdv2F1BJ81bEHan7VYPIzzXXBjlfvYLz0WkoAg8EbveJ-VNFSwDGGvPMWCjKIpz3gBxj5CrFanoSc66kgmSqcZvoqAJFItV8JDyslgGRIntePKDyqujsupc7dnwKQUI_yilFIVcUlyjZut6HTLaMBsknO27168yv5vVSyTXZhuNoAJnuskk6PDOpdKKwVZOYAt7mFj-vb2J3mTP-vTn3dpSiO1tOzF2qvG-dLZV3zJoZ5jqyeBaVjTLVB1QlQ_by0JyShaT2r71mwukMt9CYL5QY60KS_0HnSOxFDDbyC51LPJ98iQiJ4LeVWiZQ-nz2kNa9c32jQQcPC0zD_GvcdY55VUAXa-NKzFj_QoEi9j0wIPsZTrlbhUfBvZj9B1R1AngyUR0d48ElhoHy6SLV_Jed4ZNTHgcE7IAr6uZojJhvKKEdH0vy6Z7HCSNBayJipMJN4ZYWnZqKjGkLMa83ffzLrt-TuqglFYqP4YGzaURqFD_gTMQWqIHgGkDaaJiDELM_CxN4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11672147cd.mp4?token=gmsIOBCnrF2ip3i99B6qkuURpKjnagtfRZRjXrrvz4s4UGwdQ83ADn2qSlq8D4tMnOZSqhQMoCCefmoW8vkAV1N32UE4DaOS5cCCBaLy-xn3GWCDgZ19JTfFcDu4LD6F7mJvoHVgNrVTqQWS1jFpWaz6rmWixFCwFHaBdv2F1BJ81bEHan7VYPIzzXXBjlfvYLz0WkoAg8EbveJ-VNFSwDGGvPMWCjKIpz3gBxj5CrFanoSc66kgmSqcZvoqAJFItV8JDyslgGRIntePKDyqujsupc7dnwKQUI_yilFIVcUlyjZut6HTLaMBsknO27168yv5vVSyTXZhuNoAJnuskk6PDOpdKKwVZOYAt7mFj-vb2J3mTP-vTn3dpSiO1tOzF2qvG-dLZV3zJoZ5jqyeBaVjTLVB1QlQ_by0JyShaT2r71mwukMt9CYL5QY60KS_0HnSOxFDDbyC51LPJ98iQiJ4LeVWiZQ-nz2kNa9c32jQQcPC0zD_GvcdY55VUAXa-NKzFj_QoEi9j0wIPsZTrlbhUfBvZj9B1R1AngyUR0d48ElhoHy6SLV_Jed4ZNTHgcE7IAr6uZojJhvKKEdH0vy6Z7HCSNBayJipMJN4ZYWnZqKjGkLMa83ffzLrt-TuqglFYqP4YGzaURqFD_gTMQWqIHgGkDaaJiDELM_CxN4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکا اومده یه ویدیو گذاشته از اقدامات سریع در حین فینال دیشب و جمع‌آوری صحنه کنسرت قبل شروع بازی در کمتر از ۲ دقیقه
حالا این سرعت رو مقایسه کنید با پریمیرلیگ جذاب ایران که خدا میدونه همین‌رو چقدر طولش میدن تا جمع کنن
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90547" target="_blank">📅 12:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90546">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👀
لحظه دیوانه‌وار قهرمانی پاری‌سن‌ژرمن در ورزشگاه خانگی در پاریس؛ دقیقا استارت آشوب دیشب تو پاریس از همین جا بوده!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90546" target="_blank">📅 12:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90545">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHMi0894viOrZcsjVk_t-9wrc6d6hUGBM7qNH7mkP6tthBAtVOg-31GuyXvgd5Esj1TJW8YJNDUrFWSRiw_vGG9N_DqxiCBgIsbEVrksNh4y9_Pu8llrRgYPZ9nNhay4VqBk1zULb_eycXJoTjEJO2FCED9N3eB2YJx5OYyiFl1VYmWMm30VGXKD2KUUvqtppqnWMoW8FPMkvbPXZUBT5uN8MsbYGVforanqZGuOPLqh6LVyb_QaS7g_fhbmzGufG3YNlvaW0yr-lSuaBpp2dT4OzufdRqDaKlcHB5B93i6nlrqEqCuHpt9I8JjtH9ZbF9dHkFVo4LqmvF2zlK9f7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوپرکاپ اروپا
استون ویلا Vs پاریسن ژرمن
22 مرداد
آر‌ بی آرنا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90545" target="_blank">📅 11:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90544">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4dd57d3d9.mp4?token=F0X8NqCR8lQUAGjySyvm0xFxp8N1wMGSqUUyk-J0vtBLMg2nzkYRCzLc6wifrVtLxYDWUrr7N9qZd3QDsjoePsD1uJfllSsaY-HUfI-RorYYF9hpDQ25wtFcWdclbCwN2sfJ0XwdzzEQS1r6w_6C4RtHMww-MEUd95Fa8JIfDY2dwW71j4sv5v4EniRTULQiNmGlnCeBfKuM-RaoLiLqe50s0AIxdsnaATZo-01QJRGVNMTSKHCac5HS2oRZU9Y_qdT8YoWDlmsapCXBruxLjG95NA8o20pMH1q-lgLIoSZrW60aZY_2_DBwT78lUNvlL-V9RK-hSBhXkWvdfLm-UzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4dd57d3d9.mp4?token=F0X8NqCR8lQUAGjySyvm0xFxp8N1wMGSqUUyk-J0vtBLMg2nzkYRCzLc6wifrVtLxYDWUrr7N9qZd3QDsjoePsD1uJfllSsaY-HUfI-RorYYF9hpDQ25wtFcWdclbCwN2sfJ0XwdzzEQS1r6w_6C4RtHMww-MEUd95Fa8JIfDY2dwW71j4sv5v4EniRTULQiNmGlnCeBfKuM-RaoLiLqe50s0AIxdsnaATZo-01QJRGVNMTSKHCac5HS2oRZU9Y_qdT8YoWDlmsapCXBruxLjG95NA8o20pMH1q-lgLIoSZrW60aZY_2_DBwT78lUNvlL-V9RK-hSBhXkWvdfLm-UzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو هم تو فضای مجازی دست به دست میشه از این بلاگری که قبل خراب شدن پنالتی دیشب گابریل، میگه توپ گل نشده و پاریس قهرمان شده
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90544" target="_blank">📅 11:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90543">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔵
عاشقانه‌های بازیکنان psg با زن و بچه هاشون بعد فینال دیشب:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90543" target="_blank">📅 11:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90542">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a6ea91f0b.mp4?token=Oo6YMhS7ZcFR4GzY4KsKlXRTesFL6q7zaqRKPLuSBp4ra7kn80eg5vd1YndGaCm38cUzCuHqYvCnil5knyVIT_moLzbUgVW7xHaMEpvvhNjBz9bwTcP22fHcuOu0LxNFdeixqxdlTrNMaBFEI-MGVryjFSau3IgzrPbdElRCQ2NjXkiq0T_V55EJ3LgqYOS8TLDw-4dLUfpmMKcnsc22jctZlROrEFs_5Iruw-jpSV3__TYREij23-uomLsGYOVDPKZ_eLvfIxnSxxlsD9v-HWcBYJv6gOn6D0R27fWDqZJcMh_82t_xitJmqeYNoQvDIiMWIcWvTjKN_C4wvO7fmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a6ea91f0b.mp4?token=Oo6YMhS7ZcFR4GzY4KsKlXRTesFL6q7zaqRKPLuSBp4ra7kn80eg5vd1YndGaCm38cUzCuHqYvCnil5knyVIT_moLzbUgVW7xHaMEpvvhNjBz9bwTcP22fHcuOu0LxNFdeixqxdlTrNMaBFEI-MGVryjFSau3IgzrPbdElRCQ2NjXkiq0T_V55EJ3LgqYOS8TLDw-4dLUfpmMKcnsc22jctZlROrEFs_5Iruw-jpSV3__TYREij23-uomLsGYOVDPKZ_eLvfIxnSxxlsD9v-HWcBYJv6gOn6D0R27fWDqZJcMh_82t_xitJmqeYNoQvDIiMWIcWvTjKN_C4wvO7fmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانه‌های انگلیسی از این واکنش دیشب رایا وسط پنالتی‌ها پشماشون ریخته و عملا گفتن این گلر کسخل مسخل از کجا آوردید که قبل زدن ضربه شیرجه میزنه
😂
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90542" target="_blank">📅 11:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90541">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1dc755209.mp4?token=umvZJneXNUb-PGYhSuWVQb-fUFoQoFoa2XpJ_fJjXinV_kXzr3vrA1SB0nvCa-ERs0zu3JeBWxmZ0ZWWUsu0Qp2w9YC5OuGcKu-PwfbeD9B7lTs0FgKMi8QbIbESP7UJlxQr8Aa0uVmnbljcfTzHzHyh7gzQ6jCAw3LHzxSeAGrsSJRPSIycTCLRb57IHN6ZTdtjHykkkojFqKbHGqGBdkuaS7ppTSN-WfcEyHi4pdSmseMQ6TGjPHFZT8ya5IQ92SI6UpL2k2F68p0HMACbuIfDMpxhxIPqlh8ust-XENA_vAX0z15tU_h0SX8KSxd0I3pdZmi-WwRUfdNb9wicdEcalNnCz8QgzkLdie1pD0tEmJjuE4UVPJ6mDE9drIPUf6ecgrBUGLIkKx6pkSE6GBlTRr08LKjNG1hzAdcmxg9pv0JM674DVWPHldC0ltowoPtXTh60ImoIUzEu9zqR1ttoxvstTy30h6-ynxO1SjRy4w-CvJGYtlOUSG_pv8HNqB1l65UIQt6G-8Z2X1DYQuHdw_XfchgQNR0ZAqSnffpH21k0LZbAj-9htKwW29hfE7JnfxgWtkuum0sFimpKUHHhdXK8J3aNtdbqJNaifgdEMSeDmaJJdHswAvjYTRi-ro47RGHuJ7nWmETx4OkOONdVauHAKcQykZ4po0GO7zI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1dc755209.mp4?token=umvZJneXNUb-PGYhSuWVQb-fUFoQoFoa2XpJ_fJjXinV_kXzr3vrA1SB0nvCa-ERs0zu3JeBWxmZ0ZWWUsu0Qp2w9YC5OuGcKu-PwfbeD9B7lTs0FgKMi8QbIbESP7UJlxQr8Aa0uVmnbljcfTzHzHyh7gzQ6jCAw3LHzxSeAGrsSJRPSIycTCLRb57IHN6ZTdtjHykkkojFqKbHGqGBdkuaS7ppTSN-WfcEyHi4pdSmseMQ6TGjPHFZT8ya5IQ92SI6UpL2k2F68p0HMACbuIfDMpxhxIPqlh8ust-XENA_vAX0z15tU_h0SX8KSxd0I3pdZmi-WwRUfdNb9wicdEcalNnCz8QgzkLdie1pD0tEmJjuE4UVPJ6mDE9drIPUf6ecgrBUGLIkKx6pkSE6GBlTRr08LKjNG1hzAdcmxg9pv0JM674DVWPHldC0ltowoPtXTh60ImoIUzEu9zqR1ttoxvstTy30h6-ynxO1SjRy4w-CvJGYtlOUSG_pv8HNqB1l65UIQt6G-8Z2X1DYQuHdw_XfchgQNR0ZAqSnffpH21k0LZbAj-9htKwW29hfE7JnfxgWtkuum0sFimpKUHHhdXK8J3aNtdbqJNaifgdEMSeDmaJJdHswAvjYTRi-ro47RGHuJ7nWmETx4OkOONdVauHAKcQykZ4po0GO7zI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قیچی‌برگردون‌های پشم‌ریزون پریمیرلیگ در سالیان اخیر؛ واقعا هرگلش یه پوشکاشه
😮‍💨
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90541" target="_blank">📅 10:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90540">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a27edc87ad.mp4?token=GaMtlC8HkoEMg5xg4P4aafzp1wHfeyajTNCI7uwUpP_b4gCWZLXPe1KMToatgUnIRBXVhks8pMvlDlnnSbULkWTsSolxN7KdhNnxghHIWQyMQw_7IQ-wuIVPpgqRNP3Z1xU2EU5QCThp794P1AVR-LHmvB1yHZ4SrjJVEXjWqYtHlwPND1z5A5jVK2O1RyxhDJHCK0AY3V4Y_jyXn9WFW9qfMCKUw-ZRfgUFzWHzJTvWydlNTlTs6rJ652ymsqHCr6_6JsR90CUyinws5kPbeK8EDU_XvSv1Mvw4AcRr8propWEi7GoAVZKCuSOR2HLlyxReatCaCuDPye-v_mNcoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a27edc87ad.mp4?token=GaMtlC8HkoEMg5xg4P4aafzp1wHfeyajTNCI7uwUpP_b4gCWZLXPe1KMToatgUnIRBXVhks8pMvlDlnnSbULkWTsSolxN7KdhNnxghHIWQyMQw_7IQ-wuIVPpgqRNP3Z1xU2EU5QCThp794P1AVR-LHmvB1yHZ4SrjJVEXjWqYtHlwPND1z5A5jVK2O1RyxhDJHCK0AY3V4Y_jyXn9WFW9qfMCKUw-ZRfgUFzWHzJTvWydlNTlTs6rJ652ymsqHCr6_6JsR90CUyinws5kPbeK8EDU_XvSv1Mvw4AcRr8propWEi7GoAVZKCuSOR2HLlyxReatCaCuDPye-v_mNcoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضدحال عجیب و غریب به تماشاگران سر صحنه پنالتی آخر دیشب گابریل
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90540" target="_blank">📅 10:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90539">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XszxUTE3R9wS0TbO426yNUcki4i7lp23LWh5BkUU49TmFcdxM4R-rGmdM9GqDXR1DU3uZnYRdavxzKbyxNlE9oZA06ECYw2eoSyc_NAVgHDw1kz-4GdSzW2Hn8rOaxOmbt6rMIBu1-64M2k-DX9bl-BaSs_5p84hmdMQJqkqbVUVBqxyfyL8hv_mEIwGVx-CeAkD8P7b5kXGbNfFC2Akn_aYnZyOEbs-_mJRNpnptDSdYzjdHoNrTMuLlCsyFIRm3JmI6RFwdpVQg0tJ2TsvBbLy02_HjLg7I-NV9yIGH_bhH2AzewEFoNntzcJ36h-1dsa40SwBBIvF1MgqacHrDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رافائل لیائو هم این وسط اعلام کرد که دوران بازی در میلان تموم شده و تابستون جدا میشه.
مقصد احتمالی: پریمیرلیگ انگلیس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90539" target="_blank">📅 10:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90538">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/888a4aa5cf.mp4?token=LLJI-MS9aKV3ItxmfHU3MY4SReEw_dVNfCTBGa7SKocYGXhzFpw-MVWxLlnQnYV0FXODEwzA1z9WOg-WQeaTu5mDk6Wy5tjn2zrvfaI3-RqoqvUj1Lp5Fq5MPwSu-yiPm6Ep_RKLJ39z6jxeth_l-5cDvcCF_cg_YmQnoSITXI9LxPgVsGiuxRnzMovdnYb0jzcs_5nWFXazz81-rD-Cos29mX9_AE0uzaRD8cDmNdAIvf6bHxSFy-C9adoMW4UxUFFj41gkdv_HF8c8LruShf24oQOgSM2XxV20hUx6Xc0EUkwa3W_Vzs33F9njZB_gs-EHkqTYdPZCmRBq324jng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/888a4aa5cf.mp4?token=LLJI-MS9aKV3ItxmfHU3MY4SReEw_dVNfCTBGa7SKocYGXhzFpw-MVWxLlnQnYV0FXODEwzA1z9WOg-WQeaTu5mDk6Wy5tjn2zrvfaI3-RqoqvUj1Lp5Fq5MPwSu-yiPm6Ep_RKLJ39z6jxeth_l-5cDvcCF_cg_YmQnoSITXI9LxPgVsGiuxRnzMovdnYb0jzcs_5nWFXazz81-rD-Cos29mX9_AE0uzaRD8cDmNdAIvf6bHxSFy-C9adoMW4UxUFFj41gkdv_HF8c8LruShf24oQOgSM2XxV20hUx6Xc0EUkwa3W_Vzs33F9njZB_gs-EHkqTYdPZCmRBq324jng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو مسابقات پایه ایران، یه گلر وقتی تیمش جلو بود اینجوری برا حریف کری میخوند که در نهایت ...
خودتون ببینید عاقبت گنده‌گوزی چی میشه
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90538" target="_blank">📅 10:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90537">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔥
برندگان جایزه پوشکاش در ده سال اخیر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90537" target="_blank">📅 09:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90536">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a192f49940.mp4?token=gXIJ4aEzbNA24qcwOw_QawUcci56AgkN64EuOw_5pbPGI0CrAMdbjC-D325v3wYIY2as1-5mFP5WKyEQz1Z-CjwdQRK-x6cUZPKPrVon7KyauRdvbbTFSg9bWBmDhPYe9b8O96-u9g0jVviKt7MOZTXygzxEPDa3W0NaYJ-txhwyMj7U1DmYcFFG0UUC-S5qRvjBsjwawwmMe6Mcyaet7ynZ3iNK4V4IL9NzhklYkrebYf8fio8NeHwsBcEClk3Te9dUUNZxRFJFd70V45vMgRUhJKk4gypp8d_2v90Ow0H8gyvNXaUV0V7KeSGHHzz34T8TvU6nxAsEFv6gB9hY5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a192f49940.mp4?token=gXIJ4aEzbNA24qcwOw_QawUcci56AgkN64EuOw_5pbPGI0CrAMdbjC-D325v3wYIY2as1-5mFP5WKyEQz1Z-CjwdQRK-x6cUZPKPrVon7KyauRdvbbTFSg9bWBmDhPYe9b8O96-u9g0jVviKt7MOZTXygzxEPDa3W0NaYJ-txhwyMj7U1DmYcFFG0UUC-S5qRvjBsjwawwmMe6Mcyaet7ynZ3iNK4V4IL9NzhklYkrebYf8fio8NeHwsBcEClk3Te9dUUNZxRFJFd70V45vMgRUhJKk4gypp8d_2v90Ow0H8gyvNXaUV0V7KeSGHHzz34T8TvU6nxAsEFv6gB9hY5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
چیزی که اینروزا اتلتیکو بجای آلوارز به بارسا داده:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90536" target="_blank">📅 09:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90535">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae10b6cdcd.mp4?token=eXbRRIkdWsuYnv5jWxYYn5W8la9xVXar5uYaE88-Uj2lYGxE3j65AQ4sEPEeiCX8JB2NiwkQ5pKy8rk0ubQDhkjZj1kQEjGR3azzUPX5KFT7DRHrAwN6NRfnkycHTMKeCNzD5V1uP-Vz6air8tL8ygGEQy-Ffw6CZeJUZ72mTLlSdl6ppe37g-IS0cxzNnHm4bW9tz9cUVcf0nTRDRAUowSTsDgp4ULlkC7VI6J24VajfpJJ7D26i-34EBQEp95R0v7S5u6hy3v5sZ9JpSEXxICqJ2vLlvhjRtDSLguUb-JMCsL_-V917mPTzivXPkXp5h-M-pOKPo76OEvzjb1gzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae10b6cdcd.mp4?token=eXbRRIkdWsuYnv5jWxYYn5W8la9xVXar5uYaE88-Uj2lYGxE3j65AQ4sEPEeiCX8JB2NiwkQ5pKy8rk0ubQDhkjZj1kQEjGR3azzUPX5KFT7DRHrAwN6NRfnkycHTMKeCNzD5V1uP-Vz6air8tL8ygGEQy-Ffw6CZeJUZ72mTLlSdl6ppe37g-IS0cxzNnHm4bW9tz9cUVcf0nTRDRAUowSTsDgp4ULlkC7VI6J24VajfpJJ7D26i-34EBQEp95R0v7S5u6hy3v5sZ9JpSEXxICqJ2vLlvhjRtDSLguUb-JMCsL_-V917mPTzivXPkXp5h-M-pOKPo76OEvzjb1gzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لوتی‌بازی مارکینیوش و دلداری دادن به هموطنش گابریل بعد خراب کردن پنالتی
❤️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90535" target="_blank">📅 08:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90534">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5c5d95ce.mp4?token=ITaRzs8HfpqGFBElUbZQ44REtD3f0kC2SQfKsTeoMeSMfJ5dYWJWrjGk2ZU-_B0Z7V6pz-a_ozq1U2RUBCmWNQscS-0l1NXaIjnd2OIQKur7OP_Rp9QpAExf6bRvR4bDJvjo61FkHG7mXiC737W8XDcnM3mfmd_-lfx5ZmrS1zvrNoabMjMo2Vjy4B-ncdqtCGGoqxI3nRskZTloHWvJId8CvGzs80wM2lVJor6TelBPmDKpUTUV8Gx_QLZMvrQ9lyH-CN328Kz_s7tkiDF2NcNcWb_wBNFK01p_sb-rXNdJts2tdB6n-z90iWAkS43huFYKy5kFlUHk33AiGSIcEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5c5d95ce.mp4?token=ITaRzs8HfpqGFBElUbZQ44REtD3f0kC2SQfKsTeoMeSMfJ5dYWJWrjGk2ZU-_B0Z7V6pz-a_ozq1U2RUBCmWNQscS-0l1NXaIjnd2OIQKur7OP_Rp9QpAExf6bRvR4bDJvjo61FkHG7mXiC737W8XDcnM3mfmd_-lfx5ZmrS1zvrNoabMjMo2Vjy4B-ncdqtCGGoqxI3nRskZTloHWvJId8CvGzs80wM2lVJor6TelBPmDKpUTUV8Gx_QLZMvrQ9lyH-CN328Kz_s7tkiDF2NcNcWb_wBNFK01p_sb-rXNdJts2tdB6n-z90iWAkS43huFYKy5kFlUHk33AiGSIcEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاریس دو سه تا دیگه قهرمانی چمپیونزلیگ بیاره از اون شهر فقط یه خاطره میمونه
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90534" target="_blank">📅 08:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90531">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEakT6JXNLWuadmbVVhptCfIJ8yFA8Z46P2nx2ROSnxlNrKT-Vnk2nn9BFDkLRKB0p6yd9S9yiHjHo5qPZ6WjqZCX6L2Pevma_ZecytkS9zfeg1wPApkb_9fTGyyhm4yPD3F6hbO1L2QlOG8Ksak7d06LRtgyN72TlzQtDQsQSLveyRqIFAit8ILIXnxgG-EmTOL-KLN2duTmjmhG42UbBx-cHx65r91J6Z-6PaHXrvKKc7HafqTGhOZLSwJTFoc7pV-IVI6mQ7xrCS3YEcB9UZf88rqA8WpguHFbcPamr_wU1HpKBoHdFSmlyb7FJOb60LEVosfhhm1JqWGlNIgzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
شماره 10 برزیل رسما از وینیسیوس گرفته شد و به نیمار دادن. البته قبلش توافق صورت گرفته بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90531" target="_blank">📅 00:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90530">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aac643b260.mp4?token=IKG2Kv0I549im0dz4zYnId29JI2I03OC20U7K1iX-O-O_OlTxkfGNUr5dGr-UKLQs36tAD4B9GU9oC04buIU61XbMydlVGbEQGnxsiSzoHl19cw_SRyeiDBGnQGMlqUMVLTpUImrr9-7vhdN_UFlC1J7GflbRfA7h6p9mDSbJlFUfAzBcux5VEiA6eiaOsLWtvbAMvcnbKAm4yFdz9YQkhMHZoe5p1VwtU97qfrvwNtzW5zxJKSJg-dZ0mSSSRLuxvlfFwyRmss1MhpbFh2x-wAxorloHNRKVLXMd2-lFM6h1GJGnpdaVeXbIm0IQfG_Re2YCE0nAEGgaCgld4mDaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aac643b260.mp4?token=IKG2Kv0I549im0dz4zYnId29JI2I03OC20U7K1iX-O-O_OlTxkfGNUr5dGr-UKLQs36tAD4B9GU9oC04buIU61XbMydlVGbEQGnxsiSzoHl19cw_SRyeiDBGnQGMlqUMVLTpUImrr9-7vhdN_UFlC1J7GflbRfA7h6p9mDSbJlFUfAzBcux5VEiA6eiaOsLWtvbAMvcnbKAm4yFdz9YQkhMHZoe5p1VwtU97qfrvwNtzW5zxJKSJg-dZ0mSSSRLuxvlfFwyRmss1MhpbFh2x-wAxorloHNRKVLXMd2-lFM6h1GJGnpdaVeXbIm0IQfG_Re2YCE0nAEGgaCgld4mDaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جام‌جهانی نصف شب با گزارش سرهنگ:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90530" target="_blank">📅 00:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90529">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmWOJpZi4tOsuWIMDepI_uDWEBSXUFfwz-I0TF-BdbDpNiaaJikR4MWAxbUg9KO1APUC1HGyunVuud86oOZHQynW9A_DnM7rX0Owmk6pmaYt9iP0ZvKmXYMnYh3LAkYhG4I64GpIirtRLQYyg8y8A5PSEnc8H4pbBq9VO0ZhHuX0zoHyOWbodFqPz-fmb6dHZBzYXXq_YhtWjUYqlX4lPMp9n7FKS4sW4NfidMNajAlkvE5B-vLeINTHKvrT6AetO-1gwWeYEASDADy6c2YPtpbCJK29Y2qW8UJklHOK5xU4BkXyHeiyU_4HYpPn-KbJ4_2oaITwOljFUL7_RdC2-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه با 15 گل زده آقای گل این فصل چمپیونزلیگ شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90529" target="_blank">📅 00:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90528">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00937b1a6d.mp4?token=NfIc-nNA84XLVCbC_Ik8OCm8qW8sAPfAjUVm7Ogo2JU4klFPfnFDiN-XDSnA6brxW0505VTu326kmb98B4V_rBOhbkErHdQT2B_BPTw1GqSXWH5_Rn5PxqfS244YgOeh9spSNGBgSNG78EweJvyT-OR_BOQQeFWVhVpQjA5m6brRrl_R--iV7X7KWjyeeVYy1CLT26--AdPPrrHMY_htIk21XzlBAKHwlUQ6miLnd6xdNub14GE3UYqRQJk6i0NOyMGUjVn0NCAWAE3GA1d9AY2LZcZRAfVMzdil6vj0qU0lFdckILw6KB4noiImmMOuOmsuzjjHuM2WGDw58Tpwlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00937b1a6d.mp4?token=NfIc-nNA84XLVCbC_Ik8OCm8qW8sAPfAjUVm7Ogo2JU4klFPfnFDiN-XDSnA6brxW0505VTu326kmb98B4V_rBOhbkErHdQT2B_BPTw1GqSXWH5_Rn5PxqfS244YgOeh9spSNGBgSNG78EweJvyT-OR_BOQQeFWVhVpQjA5m6brRrl_R--iV7X7KWjyeeVYy1CLT26--AdPPrrHMY_htIk21XzlBAKHwlUQ6miLnd6xdNub14GE3UYqRQJk6i0NOyMGUjVn0NCAWAE3GA1d9AY2LZcZRAfVMzdil6vj0qU0lFdckILw6KB4noiImmMOuOmsuzjjHuM2WGDw58Tpwlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل گزارش امشبش رو به این شکل شروع کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90528" target="_blank">📅 00:37 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
