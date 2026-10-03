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
<img src="https://cdn5.telesco.pe/file/Aj2aWSJG0UXKpRu9MOq0_S_E2bDOfE9AChne8WTpd6SndE0yl1ggeGJDztFQ_tR4qJDIRXnYA6K3WB8sdMCGgnxfh9HSFRSIw4PZAJ9aUx5d5J6XFfpJJ4eDI9K0xdvXa15QNiEVmt6g2BCgUC4FC4i3a_MvDD6v9UV5viPXNzsUndc90McBwz0E2WsUFVI6VnKe0t7dBOx1nRb76MOhyrCQ-vwTg3icGQ_YnMxAISUK9R20sL7npEq0MQZWuiq9GiVNqwnUnaTD6JNJ0ysGUq4lmUFWHo2c9W9n2zwP5OHZ_HxLzLhDOM83XkZtUtpIRemM0paNxwKNsuhFm6NyCA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 393K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 17:51:23</div>
<hr>

<div class="tg-post" id="msg-107758">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxdopRhKSpNyt5SVK5505vsG4h4V9gexyPWOA_BGSsW-1OiinOBnCfmB-YD_5vHOGvS92RssmAlH5Otv2kxCV7St_FvtxRJn800OjN12RySVkHP4f4AQxTNAEuFbgo_yp19onc1yJXplwXZkkxMeYUDcdGWpSOGLjiawhkSVsoO0Fop5UuwH0gC-R7QcBnQ63btg-yyROLH-rozWQB32vEwnUQYekuSR-LJ_luZJIY2bYOVV5puhfR3Io_OctcChSHp3P6iDOzGAMmzIk2tBvC6pgI8TSrYz7JGE1DreIkgXS_i6uQg7m8n-M-NueirDDrsRXdYV2TY2Du1RcCeCTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💵
دلار به 271 تومن رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/Futball180TV/107758" target="_blank">📅 17:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107757">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfd85597f0.mp4?token=fiIiAs9SQAu-2FTpHqP2Gnh5sBScrgOHl4fMy4h6XqN0tobGWfNrQX6sHKt-XHV5rX3AQmM35di-8_xTTQjFtMNvVS6BHUTKsel2B1DCWj1O1tnFLV-VeIqXRklM6u__-65DCYat7Ma2GalsBPjShm9t7uPdj_P6GdqLJWnuHFCU_K06i9sXgs8PkbcNXirxxLKXPonubQn5SRlcq3z7BEBb0FEOM6vpRwysxy9cYsr2ji-NifKDfW-qZA2n7smFgafq1Oq6wnhs_dvnliHNnDLKmCGEeu2TwpuBqmxd9YRTodk1qVFUk2z23qu_UlhGbeItZopfLfYGeGy99XSx-mC8QtVw2gRC9xgiV4hmgXs5_HB2xyk5E_AKUSYY7jDdVwgN4vgw5J7S7PdHz-XV_r2C0J0tyjzF0PmUFF3RY_LMvCKZAZewY_CZl-t8QDTlLFbyevew84_9FHpinu1Sv6I9g5Hbu16fBpRAMSuAd87z6gPa7z9GdYjzt7dzU_TdQzccuYak6PEGQAYJ_3-uYIJaRQ0kATvuCrkGOHHapRdbYhWLx1agttjfcgYig9GnV5_0o_LMXJ0XU77yQjhWbdPpRYSXpgXp59vVAdx-DdkK9tqjS9iKgmRe3shMsXNcJ1M0ZnovZEJn8Z8Qu1e_-EG65AVQBzQhpRbVaPckjdM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfd85597f0.mp4?token=fiIiAs9SQAu-2FTpHqP2Gnh5sBScrgOHl4fMy4h6XqN0tobGWfNrQX6sHKt-XHV5rX3AQmM35di-8_xTTQjFtMNvVS6BHUTKsel2B1DCWj1O1tnFLV-VeIqXRklM6u__-65DCYat7Ma2GalsBPjShm9t7uPdj_P6GdqLJWnuHFCU_K06i9sXgs8PkbcNXirxxLKXPonubQn5SRlcq3z7BEBb0FEOM6vpRwysxy9cYsr2ji-NifKDfW-qZA2n7smFgafq1Oq6wnhs_dvnliHNnDLKmCGEeu2TwpuBqmxd9YRTodk1qVFUk2z23qu_UlhGbeItZopfLfYGeGy99XSx-mC8QtVw2gRC9xgiV4hmgXs5_HB2xyk5E_AKUSYY7jDdVwgN4vgw5J7S7PdHz-XV_r2C0J0tyjzF0PmUFF3RY_LMvCKZAZewY_CZl-t8QDTlLFbyevew84_9FHpinu1Sv6I9g5Hbu16fBpRAMSuAd87z6gPa7z9GdYjzt7dzU_TdQzccuYak6PEGQAYJ_3-uYIJaRQ0kATvuCrkGOHHapRdbYhWLx1agttjfcgYig9GnV5_0o_LMXJ0XU77yQjhWbdPpRYSXpgXp59vVAdx-DdkK9tqjS9iKgmRe3shMsXNcJ1M0ZnovZEJn8Z8Qu1e_-EG65AVQBzQhpRbVaPckjdM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
گریه‌های بی پایان بازیکن سابق استقلال در شب دستگیری در کلانتری دماوند!
❌
خاطره بامزه بابک مرادی از دستگیری بازیکنان استقلال در شب سالگرد ازدواج مهدی قائدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/Futball180TV/107757" target="_blank">📅 17:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107756">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107756" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/Futball180TV/107756" target="_blank">📅 17:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107755">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUxqxVTh9N65Pu5ENq3nEbyOAOEfIaMaFku84JJ5Hhb3v2XIXWScHwigRkVT5HiAsQk8bfWm8HHTdkaQ3SgTggLLY8-kDNap7xH0BI_g3h6LKPYlYvwN-GkgmbGfFAsOg_ETRlkol7F4UrN0tSzo7MiW999zNlqEQGG_iLwqWabZ40c93L58iKo2D7oLYxNO0jCUDhQTDwL28WXImNbCbVQen6K7TF8q_ANXXmO4tMvbOtrA8x7q8vUCmxi9bFVHsOvsONUEZYhLiwAMCvKUjKNVYW1nEWV8cSlXA3Zl7bOLqKOTZpbGWcVBtNsAIqvvEX1V1uDHN0nVI3xxxwOiCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز انگلیس
🆚
کرواسی را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
انگلیس: ۳ برد، ۲ شکست و ۱۳ گل زده
کرواسی: ۳ برد، ۲ شکست و ۷ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/Futball180TV/107755" target="_blank">📅 17:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107754">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967556808b.mp4?token=jGxO8HW_Aw_YqMQ1OvjzPQ5YcY2wua0Vr8nATI-sED2DiRonGZ3nicTztTq2qfa2lpLzQenc3w5cX9TmzJEIyqEzGwfSny2IiN344zXbUrOvAm1fsTnVDEz2haWEgkXvBsdvYOzi40e-g3xoeUY9JnS8TGXYH5WaMFUY78s9ZacMyN3dNpo7otwfneAvTNrq8L-kyZcTYRxdXY5-1J4TRYAWXoMma-qeov_sQ3K1Jffa-rZBjd8YOoURYl-Mv9oIgAojsMTENNKeRH5NgluUWjK579o6jOPr1U--MtLXInXVCsiRmEu4a1P09Eon7XEov6JGGkUut-O9z8sktr_nIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967556808b.mp4?token=jGxO8HW_Aw_YqMQ1OvjzPQ5YcY2wua0Vr8nATI-sED2DiRonGZ3nicTztTq2qfa2lpLzQenc3w5cX9TmzJEIyqEzGwfSny2IiN344zXbUrOvAm1fsTnVDEz2haWEgkXvBsdvYOzi40e-g3xoeUY9JnS8TGXYH5WaMFUY78s9ZacMyN3dNpo7otwfneAvTNrq8L-kyZcTYRxdXY5-1J4TRYAWXoMma-qeov_sQ3K1Jffa-rZBjd8YOoURYl-Mv9oIgAojsMTENNKeRH5NgluUWjK579o6jOPr1U--MtLXInXVCsiRmEu4a1P09Eon7XEov6JGGkUut-O9z8sktr_nIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇸
و بشنوید از مدل ماشین دروازه‌بان اصلی و معروف تیم‌ملی اسپانیا یعنی اونای سیمون
👀
🚘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/Futball180TV/107754" target="_blank">📅 16:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107753">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b23bb5ad12.mp4?token=A8a7_Z-c11gu1NoNk49UkO8xbt8AlRXM3KQfcJmkENalqg5zVStqq6EtLd7XHp-kqNxyYvxrJtoSn2qPl8UOTugmY7YLq4RbPwHGfNPbBh_ydgKqyy8UOP8qByICEYtpQJ9KfGe2iZg2V1UWCvPnsYXW8x1C414U5NQW-KRab1pb9fPyAy8Xcb4A4WAtazXNcllIkQA1TsBikpZk21EHvAb5FqztivuXISUqoT6d7JhjJU7tDXsYGVMV9oMzJboOpKYtLlGZBlnTr46zd_wVYIcWmoKwPMxehs9c9w-PNKj3Kg9SR2bCoS73zoK8cKFL6yZBd69ucIfKmOIF-DL8Koi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b23bb5ad12.mp4?token=A8a7_Z-c11gu1NoNk49UkO8xbt8AlRXM3KQfcJmkENalqg5zVStqq6EtLd7XHp-kqNxyYvxrJtoSn2qPl8UOTugmY7YLq4RbPwHGfNPbBh_ydgKqyy8UOP8qByICEYtpQJ9KfGe2iZg2V1UWCvPnsYXW8x1C414U5NQW-KRab1pb9fPyAy8Xcb4A4WAtazXNcllIkQA1TsBikpZk21EHvAb5FqztivuXISUqoT6d7JhjJU7tDXsYGVMV9oMzJboOpKYtLlGZBlnTr46zd_wVYIcWmoKwPMxehs9c9w-PNKj3Kg9SR2bCoS73zoK8cKFL6yZBd69ucIfKmOIF-DL8Koi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✅
ویدیو کاربردی از نحوه جدید سوخت‌گیری که به تدریج در کل کشور اجرا خواهد شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/Futball180TV/107753" target="_blank">📅 16:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107752">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b48e9e7f4b.mp4?token=e5nDSRW9PjIXJSF7POIo9mORgBDJWJQBFUO22o6-z69TwHb9ekQFQUMJm6dBpkVkBSiv030HeLOl7cM24_h6D6Fl_YI2q0Y01anIhKex9cNYDtSNDH2aoWwJbl_gDbtYDqu7xLIJEPQFm5llVs9jJ0Oh2YDwpOG_dR3sfBKZUQupmwUAyJQzMsfgFBFOH5B1nUVAd9js3oBS0-WlmwV9dVmiQ7HrrPaA-9YApyv6OGKmpH9JLxxcZB89ExGKK449hcpfOtP9aKEd0evU8fMm_B5L_qL330EIFoJ1HIMv-DFQvcqKZHFopmjshuf8Hv8_iZPCLFO8vyl5_hmz0b62zx3W0fpusrpp-B1piQVNFxLUajXokuV0dt7Rnf0ubODnXNI3uonH4-BuDp_p0OeBEV8EplUtFy2fJUrW6VRjfJO3vbqzk-EN3vry-UDq-q-bB5IM_06b3PLy3lbA6xJN1yR-vtkIrsk92qiSNCQIHGZugh_SgwQ8vblOQsw_eX6lQlDc9ccG1G7W7dpup3rQ3TVQ4BzkbMgXWnQrPAtolQYKEDJ_zyyUR0CCtZipDNNLdElZnLk2T5c9z130fXa71mQtbG9C9HO6AM63pRG1IxfhBbeBr6qc_96Sg0VxdjoEKLyY2TQ3oslihh0MgHnZYBWOCwu67-PaHkYGgiYL3TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b48e9e7f4b.mp4?token=e5nDSRW9PjIXJSF7POIo9mORgBDJWJQBFUO22o6-z69TwHb9ekQFQUMJm6dBpkVkBSiv030HeLOl7cM24_h6D6Fl_YI2q0Y01anIhKex9cNYDtSNDH2aoWwJbl_gDbtYDqu7xLIJEPQFm5llVs9jJ0Oh2YDwpOG_dR3sfBKZUQupmwUAyJQzMsfgFBFOH5B1nUVAd9js3oBS0-WlmwV9dVmiQ7HrrPaA-9YApyv6OGKmpH9JLxxcZB89ExGKK449hcpfOtP9aKEd0evU8fMm_B5L_qL330EIFoJ1HIMv-DFQvcqKZHFopmjshuf8Hv8_iZPCLFO8vyl5_hmz0b62zx3W0fpusrpp-B1piQVNFxLUajXokuV0dt7Rnf0ubODnXNI3uonH4-BuDp_p0OeBEV8EplUtFy2fJUrW6VRjfJO3vbqzk-EN3vry-UDq-q-bB5IM_06b3PLy3lbA6xJN1yR-vtkIrsk92qiSNCQIHGZugh_SgwQ8vblOQsw_eX6lQlDc9ccG1G7W7dpup3rQ3TVQ4BzkbMgXWnQrPAtolQYKEDJ_zyyUR0CCtZipDNNLdElZnLk2T5c9z130fXa71mQtbG9C9HO6AM63pRG1IxfhBbeBr6qc_96Sg0VxdjoEKLyY2TQ3oslihh0MgHnZYBWOCwu67-PaHkYGgiYL3TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عجب دوران‌کودکی جذابی رو‌ پشت‌سر گذاشتیم...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/Futball180TV/107752" target="_blank">📅 16:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107751">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9d2f3d6a6.mp4?token=ALhoXvt3fGD_5MIrVfF71E8NZ73wZXvBrMYAUjU75WSJwb48GCqd1LwHntC-vdMxhtSsll051ysUadAYykDM6guOMksjwwDz5H4CheZJBD-rj44HcJVefDHDWqVbjReTlaom7LD_7jkoko5FWP0LEmIu6DXbRl6tdl1m59kBBNG1X8vHcgu3mT4deErGprLlwEn5Xc_6DrOVl5txg2hvE05Oqxv9E1D-9tdO4a_mXAH2Dn1nUeXLlsoKpXVywxnVubXkiMsl7BPyz-igFETHeXXQai5a4rF_HyfpvC8Cft7jrRysZ1ek37LsSiUPnw6BnDCrMvyM0n8VDfxqqXuKfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9d2f3d6a6.mp4?token=ALhoXvt3fGD_5MIrVfF71E8NZ73wZXvBrMYAUjU75WSJwb48GCqd1LwHntC-vdMxhtSsll051ysUadAYykDM6guOMksjwwDz5H4CheZJBD-rj44HcJVefDHDWqVbjReTlaom7LD_7jkoko5FWP0LEmIu6DXbRl6tdl1m59kBBNG1X8vHcgu3mT4deErGprLlwEn5Xc_6DrOVl5txg2hvE05Oqxv9E1D-9tdO4a_mXAH2Dn1nUeXLlsoKpXVywxnVubXkiMsl7BPyz-igFETHeXXQai5a4rF_HyfpvC8Cft7jrRysZ1ek37LsSiUPnw6BnDCrMvyM0n8VDfxqqXuKfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⚪️
بازنده‌های پر سروصدا یعنی اعضای تیم‌ملی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/Futball180TV/107751" target="_blank">📅 15:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107750">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhy9EdnXRPc30bmjUsTtWZru-EjOOS9xEHmlyN5UHuA_uupXHeeCZ1rUnZEl5-CPgmvTyeGruy3zw1fckzZmZW4QRclOUlyu6NYJgU8qm0a-5WgI5_JOsWHO3f9vWg9bvDFq4dXK41ER3F0oROaKI5xiQRJ2fd45P0sfzUmUmhPzrNz0z2tVt-6A26TeDDuUS6X8CjiKwn1HqGzfcvms2FxJh_vkObEIhPK1Shbl0_wbTklFmhJDIFt5NqH6xRf4ZJKf97ZfkYB1VxqcHcOJp_YEO7Gd4gEZ53Teo133Fq8oYeaOMmMnz96II0Hlhs6p--OTDtTDboq8QsLDsPl_cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇺
میسا رودریگز "تحت تاثیر" قانون "پنالتی به سبک مارک پوبیل" قرار گرفت که اکنون توسط یوفا اعمال می‌شود.
❌
در بازی پاریس و آرسنال در لیگ قهرمانان زنان، یک حرکت مشابه حرکتی که مدافع اتلتیکو و دروازه‌بان موسو در برابر بارسلونا انجام دادند، به عنوان یک خطا (پنالتی) اعلام شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/Futball180TV/107750" target="_blank">📅 15:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107749">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🇪🇸
رومانو: بارسلونا پس از فیفادی قرارداد سه بازیکن یعنی رافینیا، برنال و ژاوی اسپارت را تمدید میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/Futball180TV/107749" target="_blank">📅 15:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107748">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86371ca1ee.mp4?token=n_slhyvr_8X-4mH85LnbcxDVZz-9nW9anS-9cf9ZauP3C_hJKsNubCGucXpqHVBHJa2cl5agX6FinPUP7YAcRHDU-q-Xe8cNNCYeolErPSX4FWBJZvzANgNLUGmaGOM8b7nhjALDH0aTPvdXFS1q7RnN3nwlBRLO2Yuj9arnPTDJT_IjROTBFbuGY7dSFMTsZOoOGa7-rhuSwhQxuKxzp16Au8k4NoO_3BgzfTby9nfAikRSvYd9-j_P2qkLmf5BNkw1pMUqyLS0TejzD_dIrK6x73rCTpjHXU6YOADyLv8zPmWI0fGuspJJ89-bbWxzy0TkevljKhLt66kWqGsCxTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86371ca1ee.mp4?token=n_slhyvr_8X-4mH85LnbcxDVZz-9nW9anS-9cf9ZauP3C_hJKsNubCGucXpqHVBHJa2cl5agX6FinPUP7YAcRHDU-q-Xe8cNNCYeolErPSX4FWBJZvzANgNLUGmaGOM8b7nhjALDH0aTPvdXFS1q7RnN3nwlBRLO2Yuj9arnPTDJT_IjROTBFbuGY7dSFMTsZOoOGa7-rhuSwhQxuKxzp16Au8k4NoO_3BgzfTby9nfAikRSvYd9-j_P2qkLmf5BNkw1pMUqyLS0TejzD_dIrK6x73rCTpjHXU6YOADyLv8zPmWI0fGuspJJ89-bbWxzy0TkevljKhLt66kWqGsCxTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
مهدوی‌کیا: دوره پرولایسنس در آلمان در یک سال برگزار می‌شود؛ در ایران ٩ روزه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/107748" target="_blank">📅 14:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107747">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e10be0d86.mp4?token=KdxyZRvbHH1Pr9MAw2ZNOWR0X_jxsXUVJcnxqB6I8YTMuw8f5EPpzmfmO2bt17VENpVQHyam6xTdaPDL1XaEHoLYZU8WpkGQWJUGvSTHT1t33KidPZD340rMOlN7-a7LlJLdrPH9iMckD3wiFMOXfuPGQpD86BiEpzhUZQOAjdSAtqJ2QwLr6fpmk0FZlBIxG1sKxb0Z2zIQZkKpmSoaT1-pJklq8Zol-HsJivwPJO67ctsUzbIysLwTtAnPfG0_EDGMttZ0Odh7fHb_gpHL7sXtMByLbwV4p0M_OFu-MNhK15Tf9rqv3q__oRn-SdvkoFvl2yC3QpAVUTW4CrlUHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e10be0d86.mp4?token=KdxyZRvbHH1Pr9MAw2ZNOWR0X_jxsXUVJcnxqB6I8YTMuw8f5EPpzmfmO2bt17VENpVQHyam6xTdaPDL1XaEHoLYZU8WpkGQWJUGvSTHT1t33KidPZD340rMOlN7-a7LlJLdrPH9iMckD3wiFMOXfuPGQpD86BiEpzhUZQOAjdSAtqJ2QwLr6fpmk0FZlBIxG1sKxb0Z2zIQZkKpmSoaT1-pJklq8Zol-HsJivwPJO67ctsUzbIysLwTtAnPfG0_EDGMttZ0Odh7fHb_gpHL7sXtMByLbwV4p0M_OFu-MNhK15Tf9rqv3q__oRn-SdvkoFvl2yC3QpAVUTW4CrlUHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
😳
ویدیوی وایرال شده از کلاس تخلیه گریه برای بانوان در تهران! این خانم‌ها برای تخلیه احساسات خود در کلاس‌ها پول پرداخت می‌کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/107747" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107746">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd4b89af76.mp4?token=AJH3ByaB5mn5Z-aLqqLREFN52o-_Lrd94FCNVwB0tp3YxkMkGO7syxzMY0Qj6JjjunvVB_R9UccYcjhpValvwxR_UrqRsX3uJq5DVQ-4Fu3qIHWZhnTT0Xq4EANN00Wke1K5ZVjpbYb8UpVPbTkSfpbnoVeqVi_taO8QWUWhpJ_Q3AxFZ3FsFtkO_MKYyiaTH5E5IWz_EexMhwVmROi6WRD_gjSxCNjAua3fHhPerAnDKSyThAJtTgigH-BrOLJosUkIAd1sRSEETEUNI0iuC5PT6Oa5JipXswEV-4hAb_lxnNHkBaZ1BRDl_KorWLvj8De0IEuGDiTxZ_68jP-oQLZSryAWF5FPJVo9BsYoxAy_-5wDEaLikEJywRyJB-ciVCCkM35lDwzjpLZjkLdzhVlAnveyZBelc_Y5U2qedIDZ9e1GYEheeGiBzZrib9gfImdJ9eOVI00LrvGkhBca2b_PQhzV9nqrovwlTBhkWypwlQjT2ZFGzjkGftjDRs2Cu8NAsynpLJkhYd01modT0K77uVq4IOzBTRRMng-Wpyvfct-1ImUglxPDsp-WuwM_5Pw-RbjhAr2FYpQHErSBQfFC8RXAOFu1OYqNdgNqBPjP36lupn5D291zxEksljnX_55jRTFIhC8a2zZMMf1-OT0MCsEEHKvwk5XN8T8e9ro" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd4b89af76.mp4?token=AJH3ByaB5mn5Z-aLqqLREFN52o-_Lrd94FCNVwB0tp3YxkMkGO7syxzMY0Qj6JjjunvVB_R9UccYcjhpValvwxR_UrqRsX3uJq5DVQ-4Fu3qIHWZhnTT0Xq4EANN00Wke1K5ZVjpbYb8UpVPbTkSfpbnoVeqVi_taO8QWUWhpJ_Q3AxFZ3FsFtkO_MKYyiaTH5E5IWz_EexMhwVmROi6WRD_gjSxCNjAua3fHhPerAnDKSyThAJtTgigH-BrOLJosUkIAd1sRSEETEUNI0iuC5PT6Oa5JipXswEV-4hAb_lxnNHkBaZ1BRDl_KorWLvj8De0IEuGDiTxZ_68jP-oQLZSryAWF5FPJVo9BsYoxAy_-5wDEaLikEJywRyJB-ciVCCkM35lDwzjpLZjkLdzhVlAnveyZBelc_Y5U2qedIDZ9e1GYEheeGiBzZrib9gfImdJ9eOVI00LrvGkhBca2b_PQhzV9nqrovwlTBhkWypwlQjT2ZFGzjkGftjDRs2Cu8NAsynpLJkhYd01modT0K77uVq4IOzBTRRMng-Wpyvfct-1ImUglxPDsp-WuwM_5Pw-RbjhAr2FYpQHErSBQfFC8RXAOFu1OYqNdgNqBPjP36lupn5D291zxEksljnX_55jRTFIhC8a2zZMMf1-OT0MCsEEHKvwk5XN8T8e9ro" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇹
یکسال پیش در چنین روزی برتری پرتغال به رهبری رونالدو مقابل اسپانیا در فینال لیگ‌ملت‌های اروپا و قهرمانی در این مسابقات!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/107746" target="_blank">📅 14:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107745">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9decbe8c9.mp4?token=quFPAjmM8fI3S56DEj3NruPLnnrJ7B-POa4WE3YeqjseQKCJoLK7zODJgn6qWMc9M273K0dnam6hIACd_6e9_pQsjET5pYWzpetMGUHiEnPWk-yc7b7B2fXJF9FifGv96t_ci23m9qy5WFH1XlGjHkJCtojpflEbNy-VLmU6axI5YHnB5gyt4oKwFJHNXbVtif6CZ68N5FDGcLxIOF1lGluf-ncJu1WSmxo1dOraWIfjG88gw11HJc9KNOgzn5eFb-y-3f-Ae9msPUrItn60OHOquVXO-ySe2UugBiRxhDKOwmgqDfxDyqhdRCVrofkHBPekmitRaaqYMtmM-wTIxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9decbe8c9.mp4?token=quFPAjmM8fI3S56DEj3NruPLnnrJ7B-POa4WE3YeqjseQKCJoLK7zODJgn6qWMc9M273K0dnam6hIACd_6e9_pQsjET5pYWzpetMGUHiEnPWk-yc7b7B2fXJF9FifGv96t_ci23m9qy5WFH1XlGjHkJCtojpflEbNy-VLmU6axI5YHnB5gyt4oKwFJHNXbVtif6CZ68N5FDGcLxIOF1lGluf-ncJu1WSmxo1dOraWIfjG88gw11HJc9KNOgzn5eFb-y-3f-Ae9msPUrItn60OHOquVXO-ySe2UugBiRxhDKOwmgqDfxDyqhdRCVrofkHBPekmitRaaqYMtmM-wTIxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
یک شرکت فرآورده‌های گوشتی به این شکل کاملا منطقی تبلیغ سوسیس‌هاشو کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/107745" target="_blank">📅 13:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107744">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c197e3a2a3.mp4?token=rP-Y3J9rz7LqNcHjb4k_tItCfk_7ymL4RxL_ghvMQ0rkLXXJRRnrYbZVBjPXHEY9Tgje1L_hdUFTogdbJelAZzxR39r8r1tr9iI1Kv-drRZAhDg731nGb9JYl5FYBrJGoeLDCvRgHbJE9oEISiKDMUxhqU_4Jhk9O_9PLOQ0-R-dE1IfBAU95N6Lxrs2jKtoGDCvLU6mimE5v8Z109e_LvZ8RXdpnK_kr08T9IgJzExOxc6cFB_Z010YgBoqmTwd6541_WRM9g4xyCvfNUqUno68a_psUrvgc-vssQ9Azk_by30Wd9ZMDjw4nVjlujd6EFCHOmCeElrr1ZgOWW6XwKnrrYBNU-oecVOph83VZng1XfUE1BBYoGdu-zSHHV9RV-Qrd719O1sH2WAVKH1eRWBVUhBWQfrEcahht1__elhstBUOQ9af9pmRxaxWGnIupVr4Fp0cYkE88GF7EiPeB2gUFnwuLuRBkJvW_5EkpVg00sKB9BgeTfRoU_Yiw7RrLE16L6l3r0qFb967zOeRjDmw3Y-X1IEEmorpuTXXfn6p3C3rZgpG8NG4E8X-n6gLU6n1x_dWQ4pmZKC9l6RmpXDvIkcsqJL2bN04SLo_eeNWX1i2gM5_PRwwGwcFdRH8E_DYt-ryycI-GjZNLsU_akz6mDWUXfJQe3JE-fgGnAk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c197e3a2a3.mp4?token=rP-Y3J9rz7LqNcHjb4k_tItCfk_7ymL4RxL_ghvMQ0rkLXXJRRnrYbZVBjPXHEY9Tgje1L_hdUFTogdbJelAZzxR39r8r1tr9iI1Kv-drRZAhDg731nGb9JYl5FYBrJGoeLDCvRgHbJE9oEISiKDMUxhqU_4Jhk9O_9PLOQ0-R-dE1IfBAU95N6Lxrs2jKtoGDCvLU6mimE5v8Z109e_LvZ8RXdpnK_kr08T9IgJzExOxc6cFB_Z010YgBoqmTwd6541_WRM9g4xyCvfNUqUno68a_psUrvgc-vssQ9Azk_by30Wd9ZMDjw4nVjlujd6EFCHOmCeElrr1ZgOWW6XwKnrrYBNU-oecVOph83VZng1XfUE1BBYoGdu-zSHHV9RV-Qrd719O1sH2WAVKH1eRWBVUhBWQfrEcahht1__elhstBUOQ9af9pmRxaxWGnIupVr4Fp0cYkE88GF7EiPeB2gUFnwuLuRBkJvW_5EkpVg00sKB9BgeTfRoU_Yiw7RrLE16L6l3r0qFb967zOeRjDmw3Y-X1IEEmorpuTXXfn6p3C3rZgpG8NG4E8X-n6gLU6n1x_dWQ4pmZKC9l6RmpXDvIkcsqJL2bN04SLo_eeNWX1i2gM5_PRwwGwcFdRH8E_DYt-ryycI-GjZNLsU_akz6mDWUXfJQe3JE-fgGnAk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🥇
کامبک جانانه یونس امامی در مقابل کشتی گیر ژاپنی و کسب مدال طلا بازی های آسیایی ناگویا با گزارش ابوذر کرمی نیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/107744" target="_blank">📅 13:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107743">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnpqjvDqCg6qCRet0Oxw78HIKw9QzmWSsElcEBbBX7Hx8EXufmnjxu-ORASRVAaZOlvjjCORLYCI63iOWnQ8km2_FJU18Q8lYUwk-RNZaq6dJdpnLZe16XCuILPYrS9sA3OZ0XKqWz-7eej0dghHx1RfsX6FYwCGHAE6SUoiqYvYvppeCFnMg9zMiICwD4SWfWG-gitcYlaGmW2cpBTsP8UTAZX3DOZaMMkpBW3Us6jciZ6-i3vfY79jYOxT3iTsCNH59RJhFF0Mba31ALGsXjvSlKT2mIF4R3xoLfEpx4MiCGulci5A9LaZo662TStNGz2eFdSvnicImyPIL5PUaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
رافینیا در این‌فصل از مسابقات فوتبال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/107743" target="_blank">📅 13:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107742">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/096e7cab86.mp4?token=f4z1qpXfllLXGM2mrIbL89Pc7UHwbPJoi4VxOgoJbMYjQ5n5ws0pxpZhoV44aF3vHr33l18pfPT_hrOkpuhmkrKE0Vl5eKWQIecrJaT8jU5cmqpVMMv4YrHU5juknYRyesizZhV6ckLxTC9bdZjPwb1oFddzdT2-7jTF80EOq12vGF9eUX0GjlrFuK_ufEhbsvZVopbtThzxHB4LMHddnDmXZBExahcUJ2Di7Lzhq5a5_i-mhlgZL1KYXWtx3L8SGY-yQudK-HbC5ScuDsVOBpTGgwKpymdq3jiTTXfQcZXDsmmRL2n6-jLiOMpql7SsHMxsOm3b2obx_NmRh0Hlog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/096e7cab86.mp4?token=f4z1qpXfllLXGM2mrIbL89Pc7UHwbPJoi4VxOgoJbMYjQ5n5ws0pxpZhoV44aF3vHr33l18pfPT_hrOkpuhmkrKE0Vl5eKWQIecrJaT8jU5cmqpVMMv4YrHU5juknYRyesizZhV6ckLxTC9bdZjPwb1oFddzdT2-7jTF80EOq12vGF9eUX0GjlrFuK_ufEhbsvZVopbtThzxHB4LMHddnDmXZBExahcUJ2Di7Lzhq5a5_i-mhlgZL1KYXWtx3L8SGY-yQudK-HbC5ScuDsVOBpTGgwKpymdq3jiTTXfQcZXDsmmRL2n6-jLiOMpql7SsHMxsOm3b2obx_NmRh0Hlog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
میکروفون باز، کار دست گزارشگر داد؛ جمله جنجالی هادی عامل علیه حسن یزدانی!
🔻
در حالی که پیروزی امیرعلی آذرپیرا مقابل آرش یوشیدا یکی از مهم‌ترین اتفاقات صبح کشتی ایران در بازی‌های آسیایی ناگویا بود، صحبت‌های پشت صحنه و خارج از گزارش روی آنتن زنده، یک حاشیه بزرگ برای کشتی ایران ساخت.
🔹
❌
👀
هادی عامل: صبر کنید ببینید اگه (یوشیدا) تو مسابقات جهانی به حسن (یزدانی) بخوره، ببینید با حسن چیکار می‌کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/107742" target="_blank">📅 13:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107741">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35b732453.mp4?token=rdSplSXen1FHjiH_m_hEB3faK_W71fMk4nxqfc5FO56Ao_oLIK8G-B6c02RbrlpEUyvaVJiOC2un7XMz602htAhyeHATfMHRig8j2WDVvI5BEWysvnPXexpW2i-ScAMFWPjXva11FSXoGmwBoxKa3ndcAFg9Rqbn_fsUUbl9o9jQ4zY2IQ1JhKFSYmCkiqDruenYt0nTzetiI8JGqv1SkUIBybJfX_EvOc37zDLdAn2cO2O09RS6y0vTKhhh8gdNBNqEgoxT3CXosqqOL-MbnF-WioNih6jB_bQ9N0rXMIRoe3Nri8i98AFWwNEmRfMCrc0yIaoGa_FtSSHWCeZFbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35b732453.mp4?token=rdSplSXen1FHjiH_m_hEB3faK_W71fMk4nxqfc5FO56Ao_oLIK8G-B6c02RbrlpEUyvaVJiOC2un7XMz602htAhyeHATfMHRig8j2WDVvI5BEWysvnPXexpW2i-ScAMFWPjXva11FSXoGmwBoxKa3ndcAFg9Rqbn_fsUUbl9o9jQ4zY2IQ1JhKFSYmCkiqDruenYt0nTzetiI8JGqv1SkUIBybJfX_EvOc37zDLdAn2cO2O09RS6y0vTKhhh8gdNBNqEgoxT3CXosqqOL-MbnF-WioNih6jB_bQ9N0rXMIRoe3Nri8i98AFWwNEmRfMCrc0yIaoGa_FtSSHWCeZFbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
گزارش‌های مستهجن و عجیب گزارشگر تکواندو صداوسیما در بازی‌های آسیایی ناگویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/107741" target="_blank">📅 13:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107740">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isQPH-Id727fmrJcJyBQSxwg8ckipGb1uxk7QfLPaMd8ka8pBWfJ68OExDfFKUtZK7uv4Dxd3jlI_2aHG41Lah6cKsvYsfdcTiFwJagOWEAUoe66qDAkBerDex6Xvy1vsSf8VtveTUyaGs-7zAQajUBEG1EsIjD22bJMvEr9jsKb-wVqDSk1o2ClF5Bid2UqHApqEkINPtjEylc9uDQ1rFyAxAJcqwkVQOHPi_wa67m7IyZ7x_o4aZuZV7cMS62v49rnifZZTIB-vlxAw4kgS-lxu8MeWXIyZf2EXg8eXTT-Md6gJe4aezm7fXU7dupZHL6YTzsbLEcAxb-NdxG37w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
📊
برترین گلزنان تاریخ‌بازی‌های ملی؛ حضور اسطوره علی‌دایی از ایران در رده سوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/107740" target="_blank">📅 12:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107739">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/888405197c.mp4?token=GfQnryFQ76cXq4EGywq7-kdMMWuLSOrZJ-Iy7x_RGk2whjX1e3T6bWt7Cr5ocNurFBCgjj7DLTm5mjKn6G5scv1aQP8ezkFB56gp1acUbyyE_REPLrl_XM2XDABe8j3J5xLxmqDxb79XhKcOX2GLsO71SsJBsVFMMGJH6wnxbqEshP6RIOKYs8chLIfiuw_yCo3BRHTcs81C9f8Bii0i6vfb6O8nxRwRQZeqwTG6BI8L8ifMvdP9p1hITWZU_OohgX3oimuC1uHgeN5eCANA5MlltOoG6lHNk7u4gJxs9zFZjba9ff15FqBsASHW74VIIX1qimKTlTCb6AVR5XBPUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/888405197c.mp4?token=GfQnryFQ76cXq4EGywq7-kdMMWuLSOrZJ-Iy7x_RGk2whjX1e3T6bWt7Cr5ocNurFBCgjj7DLTm5mjKn6G5scv1aQP8ezkFB56gp1acUbyyE_REPLrl_XM2XDABe8j3J5xLxmqDxb79XhKcOX2GLsO71SsJBsVFMMGJH6wnxbqEshP6RIOKYs8chLIfiuw_yCo3BRHTcs81C9f8Bii0i6vfb6O8nxRwRQZeqwTG6BI8L8ifMvdP9p1hITWZU_OohgX3oimuC1uHgeN5eCANA5MlltOoG6lHNk7u4gJxs9zFZjba9ff15FqBsASHW74VIIX1qimKTlTCb6AVR5XBPUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
ناراحتی‌ و گریه ناهید‌کیانی بعد حذف شدن از مسابقات آسیایی تکواندو ناگویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/107739" target="_blank">📅 12:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107738">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56498866f7.mp4?token=Bmyp3IH6A7iUTY-Uw8qg1VOIJAtWZ3TlPYjsvBvn-E9RALLE6iV50ZZepJ_iCNHk73IVY7CvAp92H5btXfkPii-KVPhX9akF3HPE28kGuw1cRlpxNKD965lVrT61jSdXIqhreD4fM0mphuUGTN-vApjEKbPkZHbRwYMgoe0FO50Q3NpCM-NwpAsPXAUSlNEhxR3uZXH0_qRqyYfy21C1IHEurTd5X4WdUl8Y97iZi5CoFQLdd5qBaolMu4mOnQn5NKA58oN0UAwktj0thRBVstHqRC2tVH02I3YOvBboo3LCpPVWtxfHlg-1vbnaiyhPH1W_A_Mjr4j7vE-ItntsLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56498866f7.mp4?token=Bmyp3IH6A7iUTY-Uw8qg1VOIJAtWZ3TlPYjsvBvn-E9RALLE6iV50ZZepJ_iCNHk73IVY7CvAp92H5btXfkPii-KVPhX9akF3HPE28kGuw1cRlpxNKD965lVrT61jSdXIqhreD4fM0mphuUGTN-vApjEKbPkZHbRwYMgoe0FO50Q3NpCM-NwpAsPXAUSlNEhxR3uZXH0_qRqyYfy21C1IHEurTd5X4WdUl8Y97iZi5CoFQLdd5qBaolMu4mOnQn5NKA58oN0UAwktj0thRBVstHqRC2tVH02I3YOvBboo3LCpPVWtxfHlg-1vbnaiyhPH1W_A_Mjr4j7vE-ItntsLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
👀
گزارشگر تکواندو رو مشاهده میکنید این چنین در اوج در حال گزارش است
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/107738" target="_blank">📅 12:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107737">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dW1I-D5yIZ0VYU3RZg8whvpipAkemamzrUCeSU04viw9iiywIkMXfDLPk8KQ7lw6NEoMwrhj5QolzJTVBbIEBfs_PspdDZV-jXlXUWZHYIKLapnuC8QQAKtUj9Yqu7YhQLk-1rv9TkKJpLH79yIQRGe17n5rE6nKeEyzca9UShiRoqCKbwM8huPoi85F92qepIGQv02sGEThwKYWu-WkUyZ3hcfybnuUqJF-kSaFAzqVStFgtyYB4TGrtP4kpwaG6NP1O2vkbRymGs0lI9LoF2TKkRaWkOgIpD2QGpS9sFccz2Ax4uHWl9wxAK-QWqxuzS0MIbHiDr0OhMlbijeLaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
مسابقات لیگ‌ملت‌های آسیا به شکل اروپا قرار است از شهریور ۱۴۰۶ آغاز شود. ایران در سطح یک این مسابقات قرار خواهد گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/107737" target="_blank">📅 12:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107736">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uc8cRPXD8vsV3f9-IrstFqcWlEWMiTCMUSpZuw-ToL7NfbTLx1lPHS3rNegw0AN2fPTwqWwjbZTsPrHmCpL_7tiFFrtcm9AtNSAp80D8CncJan5yjVTzGEbUD-ERQXfH3Bve26XDUqRJcqewk9VFbAR5Ll4iXOedy5st4F5m3RcI3oTcakW3fMY3-OiZpDkcuY5OjvNpCJrH0mjVbaAW-BVf8AWA2Sy0YTqh1wjD86EWoVGJWPLv4hPEs-dLowSKxMR8ZxjG-TfdG5MI8RUi4Yx0qZThpjKSh1JqaOViJiVzFj1bh12hJzDkBoEvYjraTBXs0ysI2v-Fv2EC3FiV4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
اسامی نفرات برتر آزمون کنکور ۱۴۰۵؛ نتایج اولیه برای تمامی داوطلبان تا ساعاتی دیگه اعلام میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/107736" target="_blank">📅 11:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107735">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6316faf3f3.mp4?token=flybz9ItoMS6sEBPiVVe5YMVMHyFkXWH5AneycrGOHlTm-4i9HF94tay19CgSEYpaKcWPPUUnd36Rqm6-m94nJYRWl1_-_AHe1mb0ejvpWcmRUA8NJxTvK8ux_dGBkQNFXDfmSXHbxvJQ9VRQy-gyL0VhXWIFZsvagK0aFBWXynRvYhnmrw0GFTdE32pD-ZKAVPGtqcoZVb26nJ0bAP7aMcvxhfcpmQHPmFGolrneVZr3eIZddNYR7cDhfY2zjHbU0SaDwOAAqoDaEp4F1XcBgf3-Ke0JRiKjmwTSorh4AcXBIFjVVuMJDlPUIJ5u63REoJ_YU2tbNzISCY4Moflag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6316faf3f3.mp4?token=flybz9ItoMS6sEBPiVVe5YMVMHyFkXWH5AneycrGOHlTm-4i9HF94tay19CgSEYpaKcWPPUUnd36Rqm6-m94nJYRWl1_-_AHe1mb0ejvpWcmRUA8NJxTvK8ux_dGBkQNFXDfmSXHbxvJQ9VRQy-gyL0VhXWIFZsvagK0aFBWXynRvYhnmrw0GFTdE32pD-ZKAVPGtqcoZVb26nJ0bAP7aMcvxhfcpmQHPmFGolrneVZr3eIZddNYR7cDhfY2zjHbU0SaDwOAAqoDaEp4F1XcBgf3-Ke0JRiKjmwTSorh4AcXBIFjVVuMJDlPUIJ5u63REoJ_YU2tbNzISCY4Moflag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
شبکه سه اومد بازی جودوکار خانم ایران تو مسابقات آسیایی رو پخش کنه که جودکار ایرانی تو ثانیه اول درجا بازیو باخت و حذف شد ...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/107735" target="_blank">📅 11:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107734">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107734" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/107734" target="_blank">📅 11:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107733">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6FLNldS-KgCaXRWgOxluArANTbFmBadjYmxRHU5ioCQkzjfvK8n2QmMWcvl0rKUHOElazl8bZJdx6pHkbhkA1PLchF7Oev6IIxNPNuWnr8LCBSwz5LSrgzHWF5jJGU6yLzWXB1HiJgnmEbaFpwd0cAbsyjx5BlNU7ELcvGVsHZnsEywKTV_TcWn48m4IfsAxEQeCZe0YTRe2rC50mWLkpgoUtKq7P4-oLyayyKPzFKQmCtSk5Uwfo42ikb8whFsr5wjPiPtxZRofKUPePmyeNjiWtE9NuI90DJ-XRIeBcBxjVqDK4PeyZW00RabjkKZKvfla6FezLlyVzKNHF8yhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
انگلیس
🆚
کرواسی
چک
🆚
اسپانیا
اسلوونی
🆚
سوئیس
لومتزانه
🆚
اینتر
یووه استابیا
🆚
لاتزیو
برزیل
🆚
هند
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/107733" target="_blank">📅 11:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107732">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68d8475315.mp4?token=gpzp-AShVAvso6JbHfBE-avOY9_KHD0MsfXEYUvULkiN7ZBXVTxpKSkeDXGLltSPbNDWayVyauJKaSBOqDTP4EP9nHzeoagEpJbCQuoMGuM6ffshqhuyJtYorG674SlBAt9-n8BVIcumnq7OC_VgLsFIin_q1WYL2XsA1iPNtbnRANjpDybyRwH479vIvMFnIF6IR2zwSnmv7DrSiRqYy_Ains1NTaH3ZchSmmRB1Wrm6nSqg1ZmCamPLk5jWoaYwyu3H7naiByK43AKfx6uuIhKkMgx_qf_l5A7XmQSv0n2lz8debDZWlyGbF72b-ZYNYMZVWG0rPnYTJCdZYek5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68d8475315.mp4?token=gpzp-AShVAvso6JbHfBE-avOY9_KHD0MsfXEYUvULkiN7ZBXVTxpKSkeDXGLltSPbNDWayVyauJKaSBOqDTP4EP9nHzeoagEpJbCQuoMGuM6ffshqhuyJtYorG674SlBAt9-n8BVIcumnq7OC_VgLsFIin_q1WYL2XsA1iPNtbnRANjpDybyRwH479vIvMFnIF6IR2zwSnmv7DrSiRqYy_Ains1NTaH3ZchSmmRB1Wrm6nSqg1ZmCamPLk5jWoaYwyu3H7naiByK43AKfx6uuIhKkMgx_qf_l5A7XmQSv0n2lz8debDZWlyGbF72b-ZYNYMZVWG0rPnYTJCdZYek5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
⚠️
دو قاب از بيژن‌مرتضوی به فاصله ۴ سال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/107732" target="_blank">📅 11:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107731">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fbb258d04.mp4?token=oB3Bv6Wnx8FOQ5x1wAj9GNxcbVY8duNjG-ZqGULbAmF4PmkKzzs9M0mxEE6sJ-8qEU4rbx0WTfsSqxJAO81EVUOsJzk_MXKLfJpU8H0BctUwlzb-AjZR_CtjrhHJRJJRF53Qu2AXKbDyZIlUNdGdreGd7hZlxrlP85hP7McMPLz97WpODZ-kWjxuIM6wOFGyFK8ATZWjWpwi4GES-49WtYKtGqcDBk96dvBmqfOaLPzk1b1IZfcl6Ou8qIWyeyNRMTDNkN1qbMRtKnxZQYqNadrbYWw62ctJGkaftcZJB7BzK0KcK-06DaC6mm_1xDD2GV_VGYEFRXv8N8hvg8Xn8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fbb258d04.mp4?token=oB3Bv6Wnx8FOQ5x1wAj9GNxcbVY8duNjG-ZqGULbAmF4PmkKzzs9M0mxEE6sJ-8qEU4rbx0WTfsSqxJAO81EVUOsJzk_MXKLfJpU8H0BctUwlzb-AjZR_CtjrhHJRJJRF53Qu2AXKbDyZIlUNdGdreGd7hZlxrlP85hP7McMPLz97WpODZ-kWjxuIM6wOFGyFK8ATZWjWpwi4GES-49WtYKtGqcDBk96dvBmqfOaLPzk1b1IZfcl6Ou8qIWyeyNRMTDNkN1qbMRtKnxZQYqNadrbYWw62ctJGkaftcZJB7BzK0KcK-06DaC6mm_1xDD2GV_VGYEFRXv8N8hvg8Xn8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚪️
نه به تیم‌ملی چیز جدید اضافه کردن و نه تونستن جام خاصی به ارمغان بیارن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/107731" target="_blank">📅 11:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107730">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8086af61bd.mp4?token=foUEFXCssXbEJ0msFbbNHl6di65p11sKGUGU-bcY2KmpuMq9zAWHOi0nQ1lwC8i4ZtKs6gv17Cz6LyItHIkLsC2pRj5_toW7SN1uttkg2J0UCaXq1bRvHmV06XJEwWeUDhjPkxo4IjT_o738OT6xzD1j_L-r_1iwAMcQFXd2IMCcuSdCfBRYGd7HNIqAc9Y1Y88L-iLCh-PAzFDmADa2c-10BkYcxFkf4uGy1X5yttNrv2jyIvr95TJ3wOxOzc723sC03ZdUbVqBHFTZ8QQ5tPrpqXwT8ZpcLtERxMM_mDHLS-GvirxdPdrZgbub8NWza26Xlyn_BnKraD9TH3ii2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8086af61bd.mp4?token=foUEFXCssXbEJ0msFbbNHl6di65p11sKGUGU-bcY2KmpuMq9zAWHOi0nQ1lwC8i4ZtKs6gv17Cz6LyItHIkLsC2pRj5_toW7SN1uttkg2J0UCaXq1bRvHmV06XJEwWeUDhjPkxo4IjT_o738OT6xzD1j_L-r_1iwAMcQFXd2IMCcuSdCfBRYGd7HNIqAc9Y1Y88L-iLCh-PAzFDmADa2c-10BkYcxFkf4uGy1X5yttNrv2jyIvr95TJ3wOxOzc723sC03ZdUbVqBHFTZ8QQ5tPrpqXwT8ZpcLtERxMM_mDHLS-GvirxdPdrZgbub8NWza26Xlyn_BnKraD9TH3ii2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
▶️
تلخ‌ترین صحبت‌های مالک موبو نیوز در گفتگو با امیرحسین قیاسی...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/107730" target="_blank">📅 10:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107729">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdae91c6ba.mp4?token=oekTctRr4nbHlsQxdeitvMqQdCNaZUrHImR-dwDerAGkCouyaRSufAfhbDQdheNK55vW6mcIxkSnET8jdU8pHb6nvTwW4v4yaH-GhtQQkS0ektW0xG1izpi2eu1aioy6IfVtb_kBHjtGZ05gExlPd7QGAnUrdbVOl_21QILBYmMB1lSlBvfefS7aFQwh18HwkUIhcMNQUHdHACsdVOD8DhWFOitoY_cnD5fV7HRsQ0ad0XoE7YN9pE8SmwKpchrrlr2_R0TewyTqLksVSkMgaecpftjZ_PlgHgdRNZks_mg1ApE2pTkybEfyX_hgNF94wZzVlNbWsgeqqVEO2YytIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdae91c6ba.mp4?token=oekTctRr4nbHlsQxdeitvMqQdCNaZUrHImR-dwDerAGkCouyaRSufAfhbDQdheNK55vW6mcIxkSnET8jdU8pHb6nvTwW4v4yaH-GhtQQkS0ektW0xG1izpi2eu1aioy6IfVtb_kBHjtGZ05gExlPd7QGAnUrdbVOl_21QILBYmMB1lSlBvfefS7aFQwh18HwkUIhcMNQUHdHACsdVOD8DhWFOitoY_cnD5fV7HRsQ0ad0XoE7YN9pE8SmwKpchrrlr2_R0TewyTqLksVSkMgaecpftjZ_PlgHgdRNZks_mg1ApE2pTkybEfyX_hgNF94wZzVlNbWsgeqqVEO2YytIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
یه راه خوب برای کنترل هزینه‌های اینترنت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/107729" target="_blank">📅 10:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107728">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c37b6c6ac.mp4?token=MWjERDyw-tg7WEaQ8ylhRboQKa5FCxxTzIAYtRIlFqh4qY0LxOtOmXNaNix7IuIRMJxCPsjZTmVZjiUbZTxGQ1lDe8TbCFfjLiGKG7FV3th2_LvXN2aXUiqCTcugqgTWP7hHzS7Aa48TEBPlcwuctozmOhvOJ7F7lHxCikCkdXqWlw6ujwDORDA9qbZOOg09wqILrR0fOZJ5UIzPnQGM14XX-qiH1ILi0WjJIfCTmnyr2YqGktkYwaPBM-K8LpFwOEnc_mYhMCFYHLpR8Hp9G_dEny5HvPr8xOHK1wpRmGZFjLdTkBDQDNSX66GzdmseghlPsHRkNgqmTQeRg_qfnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c37b6c6ac.mp4?token=MWjERDyw-tg7WEaQ8ylhRboQKa5FCxxTzIAYtRIlFqh4qY0LxOtOmXNaNix7IuIRMJxCPsjZTmVZjiUbZTxGQ1lDe8TbCFfjLiGKG7FV3th2_LvXN2aXUiqCTcugqgTWP7hHzS7Aa48TEBPlcwuctozmOhvOJ7F7lHxCikCkdXqWlw6ujwDORDA9qbZOOg09wqILrR0fOZJ5UIzPnQGM14XX-qiH1ILi0WjJIfCTmnyr2YqGktkYwaPBM-K8LpFwOEnc_mYhMCFYHLpR8Hp9G_dEny5HvPr8xOHK1wpRmGZFjLdTkBDQDNSX66GzdmseghlPsHRkNgqmTQeRg_qfnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
بیخیالی بازیکن های پرتغال از رفتن رونالدو دقیقا یاد این سکانس تاریخی میندازه !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/107728" target="_blank">📅 09:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107727">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Esk-r_K88P1XUXjoiQDCFbD-hHL3hCZKyxLHHO9GSbd_YXzU87Br8Frbpl6ZruS7iLkSEboH-UnMZAeVasSX_aC-JCHX5Y_CsFJV54ljscCWyTcXKgaW4MURfny66Whdf1tkDfNPb-Pg318jV0SGtAxs7TpsdFov00UQNGK7t1qosM3biO6wlXCCCVx2RYfzeb5kwLq-IEkPS1pdZBahUwqqDKoaNHDW-f-YktK2tesgjQ03we_YqSRwGsvdBWQytxsEvJI7CYbjZK_sIcQD84kQwkRFBxAErKDLliU6sDkrKLRw36BucydoCYkw26W7-kM2tFBJs27TjYpx-t_gLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇶🇦
با اعلام‌رومانو: ریاض‌محرز با عقد قراردادی به الشمال قطر، رقیب استقلال و تراکتور در لیگ‌نخبگان آسیا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/107727" target="_blank">📅 09:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107726">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b5c7684c2.mp4?token=X_OKzcp4JD9HRtRDSfxlmDRgsBPub-reCxStULcNXLTOE5BqBeJT8oFzTWb6PzAw8KKc_caLR9n9fRVfLdqPYjw5tv-mbq-1-x3zkRANnABLSVM-MPU7-NKGaDbbTzhVBC4BtrJQ2ukl8bQe-R-ynMf1JWHfYqngVNs5YJENmqgcu2RyGuwQT1ZbS4HQrcGcUJLSWFpRULcDt8D742BrWGfjovsYuNr9VcoXD8GddYhvDVVNdEY-7PF8qb0OJDdnrTG0KceHHCxo740kAYHjLwBcCTZjZeau0sWIpS5Y0V5PnNs3A266XRWZbfxJlpkRalKPf_CAyrihXzyvo-jPjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b5c7684c2.mp4?token=X_OKzcp4JD9HRtRDSfxlmDRgsBPub-reCxStULcNXLTOE5BqBeJT8oFzTWb6PzAw8KKc_caLR9n9fRVfLdqPYjw5tv-mbq-1-x3zkRANnABLSVM-MPU7-NKGaDbbTzhVBC4BtrJQ2ukl8bQe-R-ynMf1JWHfYqngVNs5YJENmqgcu2RyGuwQT1ZbS4HQrcGcUJLSWFpRULcDt8D742BrWGfjovsYuNr9VcoXD8GddYhvDVVNdEY-7PF8qb0OJDdnrTG0KceHHCxo740kAYHjLwBcCTZjZeau0sWIpS5Y0V5PnNs3A266XRWZbfxJlpkRalKPf_CAyrihXzyvo-jPjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚪️
سقوط تیم‌ملی به روایت اصغر مازیار!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/107726" target="_blank">📅 09:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107725">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d02e44cc.mp4?token=Af9e2naN4SY2kx_h5bI-FjVTo62emdrOaN7Ikjtc8rLGYOogXejL3CzvTjh3qXNs3Zn-a8-yPecpcc-Dd2HHgD48ElwIZ7ANRfigs8N3zDpjY4fCT0s1HdYBl1pLx9cL9ZTQ--05J_Cg3zT8tyxUy7jMXcCCcA_dJhhKzFu5jHyTU_CF7bLaIO5FP5zliZRV63_YqKNxacSeIqdX4fqnYN53ZQXTCoTzD6sWZdWJUjxSYi4ksUb1GYjwF4VX8xmuSZb5kcaQGlPTXhDH3pDLkYQgBSQ9MiY8Yu0kF3hf99xF54hEN3Intq5Mg02y1LoWhKN3CHP1aShc0WxHRShkAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d02e44cc.mp4?token=Af9e2naN4SY2kx_h5bI-FjVTo62emdrOaN7Ikjtc8rLGYOogXejL3CzvTjh3qXNs3Zn-a8-yPecpcc-Dd2HHgD48ElwIZ7ANRfigs8N3zDpjY4fCT0s1HdYBl1pLx9cL9ZTQ--05J_Cg3zT8tyxUy7jMXcCCcA_dJhhKzFu5jHyTU_CF7bLaIO5FP5zliZRV63_YqKNxacSeIqdX4fqnYN53ZQXTCoTzD6sWZdWJUjxSYi4ksUb1GYjwF4VX8xmuSZb5kcaQGlPTXhDH3pDLkYQgBSQ9MiY8Yu0kF3hf99xF54hEN3Intq5Mg02y1LoWhKN3CHP1aShc0WxHRShkAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وای این چه سمی بوددددد
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/107725" target="_blank">📅 08:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107721">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107721" target="_blank">📅 00:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107720">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvKBn_NQq1Q9-3z8bXNHJWRRDI12Ci1oTv1ZPMdLxKhbxbM2bZGAvB6edv5Al-WRLDz9fHCexX21_frUXU3fhQQltS-JyUq36SjCi8IwCMEgGsq8cf6dtyPsCKWISCmee_di7SiIzdESrom-RCSaq_ZzPcvZE0_fTRiYRtWAeR9EeivwhtCU9I5iou5hjfrlAYtD2yGOhHxq6UC_6-U-0peaaiMK3mMP89tXyLPx3TxczVf03UJS1LEguGir7MkJVr0Od_DTO2nOb9HMjRnh1xdDWnWJQFL6DNrC4PbCfnOwbcRRBBIck4oWPrx2KrN_w7ua2MEXJrfWqAhhZzGX5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
بنر هواداران عربستانی برای بازی مقابل قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107720" target="_blank">📅 00:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107719">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇹
🇫🇷
هایلایت بازی فرانسه یک - یک ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107719" target="_blank">📅 00:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107718">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
❌
🇮🇷
علوی، سخنگوی فدراسیون فوتبال: استقلال قهرمان فصل گذشته نشده و بحث جدیدی درمورد اهدای جام به این تیم نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107718" target="_blank">📅 00:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107717">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b540d3428e.mp4?token=k2zNmqP7KDOCslNFvoQor9joDZNXBchO5Rj_PE9O4jv14VdIkooVMvpu5ptCVkfwoiczYttv-bZG5wt4dY_3ElBGdKPE1Hv_J9u4vUqJyBmV4D3NtjkwUKkGi-sSFux2oRS02h8Oq5tumLfQcOzMWvqmFGYY8B-ymHdFS0pV-TPC12zSsJV0hQ-4fkWXs0Or0G3VvWQVAhrPXDi5PoES7S280Nk7mN7jU7TW7u_MMIEXs0ekThx8kYRLWjvmV8EGGV4zEKJmp-kePUYZNrdvy_IVjAVWa14PlxEOSve0Eu1bUpxlKu06FtQ7OphQGJKSs8O3SPP89uar38M4kzN4aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b540d3428e.mp4?token=k2zNmqP7KDOCslNFvoQor9joDZNXBchO5Rj_PE9O4jv14VdIkooVMvpu5ptCVkfwoiczYttv-bZG5wt4dY_3ElBGdKPE1Hv_J9u4vUqJyBmV4D3NtjkwUKkGi-sSFux2oRS02h8Oq5tumLfQcOzMWvqmFGYY8B-ymHdFS0pV-TPC12zSsJV0hQ-4fkWXs0Or0G3VvWQVAhrPXDi5PoES7S280Nk7mN7jU7TW7u_MMIEXs0ekThx8kYRLWjvmV8EGGV4zEKJmp-kePUYZNrdvy_IVjAVWa14PlxEOSve0Eu1bUpxlKu06FtQ7OphQGJKSs8O3SPP89uar38M4kzN4aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇧🇪
گل‌سوم بلژیک به ترکیه توسط لوکاکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107717" target="_blank">📅 23:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107716">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5cfe007c4.mp4?token=riVFj6oSrkWh3v-8PSRcaY5P_7urF7RsP7IIBgfAM5Hw4tje8QCUQ9p40Pmf_drYZGVgEtvlCCKqkBAGfxhBfBMhHofh_d-XdxKJbBhwUu-XJP7lLrVN0cCddIbE_c5ddzBvoSVj5sF74xoblj-0zdvGnDBIpmyrwFXnyGPFHv2GAbiok5xOu1ypvPRfjTDgbnhbUzGQJEBdksNvrLfcGMCQ1Ltb4lH3BggBCoAcPMxAxjN-M1FC5TvGp18jQOWo3E1lq-GcO3EuJhcGqWzuAcoTmvZROOv9JwjFS9IhhsVVfMxgwLHqutJpSWqcuidPI6wPqX0HXSCJby8sKMhcTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5cfe007c4.mp4?token=riVFj6oSrkWh3v-8PSRcaY5P_7urF7RsP7IIBgfAM5Hw4tje8QCUQ9p40Pmf_drYZGVgEtvlCCKqkBAGfxhBfBMhHofh_d-XdxKJbBhwUu-XJP7lLrVN0cCddIbE_c5ddzBvoSVj5sF74xoblj-0zdvGnDBIpmyrwFXnyGPFHv2GAbiok5xOu1ypvPRfjTDgbnhbUzGQJEBdksNvrLfcGMCQ1Ltb4lH3BggBCoAcPMxAxjN-M1FC5TvGp18jQOWo3E1lq-GcO3EuJhcGqWzuAcoTmvZROOv9JwjFS9IhhsVVfMxgwLHqutJpSWqcuidPI6wPqX0HXSCJby8sKMhcTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇹
گل‌اول ایتالیا به فرانسه توسط باستونی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107716" target="_blank">📅 23:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107715">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f73a4fb35.mp4?token=oyBsf8njn0nKzMVgLrx9T_M8UGUgicXhcc9vxgPlipDEg-eZPt-eivHpfKxPCCyYNm4oL6goxBt67WX7hY0pRnat0xWRjhxPvXQUpcxpk_LuPKjvqyd69RxJmbdREInFLScyR2GU1SNjcVrvnZtX-vowNRi1LM5z2s-qyPOUKz7h3smZyjNS-l77dqgjNSNAhQ0NV709ck5N438BIGVJ4pbGATy9eCe02Ra1vic4eAlzDuFi-zscq0Ohu2jPNh39zXygJtOc_xcLUQTsRS7YhtCs6le_TvQD5gA1EjtGJUff8EXmOz6UPyCUrU6hWo448vQFyUUpHsdy4UUfntpXzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f73a4fb35.mp4?token=oyBsf8njn0nKzMVgLrx9T_M8UGUgicXhcc9vxgPlipDEg-eZPt-eivHpfKxPCCyYNm4oL6goxBt67WX7hY0pRnat0xWRjhxPvXQUpcxpk_LuPKjvqyd69RxJmbdREInFLScyR2GU1SNjcVrvnZtX-vowNRi1LM5z2s-qyPOUKz7h3smZyjNS-l77dqgjNSNAhQ0NV709ck5N438BIGVJ4pbGATy9eCe02Ra1vic4eAlzDuFi-zscq0Ohu2jPNh39zXygJtOc_xcLUQTsRS7YhtCs6le_TvQD5gA1EjtGJUff8EXmOz6UPyCUrU6hWo448vQFyUUpHsdy4UUfntpXzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
✔️
گل‌تماشایی کوین دیبروینه مقابل ترکیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107715" target="_blank">📅 23:44 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107714">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گلگلگلگلگلگلگ دوم بلژیک به ترکیهههههه دیبروینهههه</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107714" target="_blank">📅 23:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107713">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3dc430d99.mp4?token=rsUToci10qiHfj6Y5LUvK0zqTsrBQQCvU4NM8Zjlmrg6KV8VwtRUxHm9iNh3Ce53_DwenlOetpH_YW15en39aXKxULmgL-Eej1llzjRSJ_WNRLgcSdli9QnQXIRKIrveq-xUd0skwDjFa2CCSV7uCkAvSp_CGV5ZDcLxidil0rqDwVjxdw6bYZ7RYU1TW14zdS2Fb0Vg2ZZjjhdBsVQeL-G9tSXy3yh1Q2VqqVg5ca1MAZF91ov6hxdK7y44ZBiWYCBr6FcGQk4lsxIJuXI90ZEqEGWap8G0JZUt4hCFK1Hs3a_O1YkUuslMqXZjuesJPYI9H_BTXHnWI88Djm0XLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3dc430d99.mp4?token=rsUToci10qiHfj6Y5LUvK0zqTsrBQQCvU4NM8Zjlmrg6KV8VwtRUxHm9iNh3Ce53_DwenlOetpH_YW15en39aXKxULmgL-Eej1llzjRSJ_WNRLgcSdli9QnQXIRKIrveq-xUd0skwDjFa2CCSV7uCkAvSp_CGV5ZDcLxidil0rqDwVjxdw6bYZ7RYU1TW14zdS2Fb0Vg2ZZjjhdBsVQeL-G9tSXy3yh1Q2VqqVg5ca1MAZF91ov6hxdK7y44ZBiWYCBr6FcGQk4lsxIJuXI90ZEqEGWap8G0JZUt4hCFK1Hs3a_O1YkUuslMqXZjuesJPYI9H_BTXHnWI88Djm0XLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🤯
سوپرگل دیدنی اولیسه مقابل ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107713" target="_blank">📅 23:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107712">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سوپرگل اولیسهههههههههه</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107712" target="_blank">📅 23:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107711">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فرانسهههههه زددددددد</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107711" target="_blank">📅 23:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107710">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گلگلگلگگلگلگلگلگل</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107710" target="_blank">📅 23:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107709">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e970c7c18a.mp4?token=F-cN5IaruPjwDil07sr1x0UMojKj4VqtPLYx2A8wg7I_1SNuFGSZIu7w_DACkEp5z2GU8LWgXMAboat6w4f4jQV6oRLEN7CYgA2PDGnAShCNRiroojVSWgedbuQCqzhmxPxzxZ7eyGTaVr_BHNIoefSkDl-EhO4sPnc8vtbHM9B8Fys_8Ni5VIU3sVW0AucOJ9fGsIXi-CYS0xF5wTgOXcoNIRCiPknhtzdX-WF0NFGuTl4csM2YkKLq98tedkb4aR9uvxBVQiz-kM4jlzcrAX0x81AvHmcinxngEqc4NjBSHdE6Q7lT3BC-m-WHSeZfAO7DD1S_tMQSfgx8GuEcCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e970c7c18a.mp4?token=F-cN5IaruPjwDil07sr1x0UMojKj4VqtPLYx2A8wg7I_1SNuFGSZIu7w_DACkEp5z2GU8LWgXMAboat6w4f4jQV6oRLEN7CYgA2PDGnAShCNRiroojVSWgedbuQCqzhmxPxzxZ7eyGTaVr_BHNIoefSkDl-EhO4sPnc8vtbHM9B8Fys_8Ni5VIU3sVW0AucOJ9fGsIXi-CYS0xF5wTgOXcoNIRCiPknhtzdX-WF0NFGuTl4csM2YkKLq98tedkb4aR9uvxBVQiz-kM4jlzcrAX0x81AvHmcinxngEqc4NjBSHdE6Q7lT3BC-m-WHSeZfAO7DD1S_tMQSfgx8GuEcCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
استقبال بی نظیر و خوش آمدگویی هواداران به زین الدین زیدان سرمربی جدید فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107709" target="_blank">📅 22:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107708">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0312a011f.mp4?token=VS8iReTMf9z8pzAqG7YCqp49mWiyXQSgFO3Rv1z9OLr8JQKmSVaPRzhMACMTZDE6J9gLIm5I-TJQsDOApjtsVF4IJyev-lcFAc6-v9GFVrZF5Et-I5ompSkzvZWnx1b_0ddwwA6JBJzTzv8h2Ejfc6HQXs3hROa5cO3-ce1X3gtGYsUcxesyA-1bLclZckWcVmiIx2TWwrqLO6aMdfbfUJSPbP3yZ9aYtx-vMj0rDrKSSHuQenUlu_Uam1C8-BnXMIfRwVPZPePIuHmgXTToHCxY6T0DC3wsaC6FlZsadLJCIEmvOrPD_XfgyGiXzqrSCaQl0QLe2m-uIXglgg4lHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0312a011f.mp4?token=VS8iReTMf9z8pzAqG7YCqp49mWiyXQSgFO3Rv1z9OLr8JQKmSVaPRzhMACMTZDE6J9gLIm5I-TJQsDOApjtsVF4IJyev-lcFAc6-v9GFVrZF5Et-I5ompSkzvZWnx1b_0ddwwA6JBJzTzv8h2Ejfc6HQXs3hROa5cO3-ce1X3gtGYsUcxesyA-1bLclZckWcVmiIx2TWwrqLO6aMdfbfUJSPbP3yZ9aYtx-vMj0rDrKSSHuQenUlu_Uam1C8-BnXMIfRwVPZPePIuHmgXTToHCxY6T0DC3wsaC6FlZsadLJCIEmvOrPD_XfgyGiXzqrSCaQl0QLe2m-uIXglgg4lHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل‌اول بلژیک به ترکیه توسط کوین دیبروینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107708" target="_blank">📅 22:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107707">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f5c780577.mp4?token=iI98XJ7F_rICun8zDywcoQ-9PYLL0dKcVg3wVR3So2zhbNjKOUoDoaUTFp30VN_0WGrTRplvdTeR6bmWj-sQEth0IF_Lt-9lEJ6tI3_jQZ958DP1qofVRPUa9YVzxw0IhEgywrq0ip3KcwySozyz-_cDMm0sD2Qb7Mfb7uMT_1AnKhEgp35Xxd7_DcUVb_2CS6BcuUzl5JkGHX3P_doa-PZX_GVMhOC5jlu2tLrAGpF4OpTBfzbZ1GceDvSUx4z7mAN6_GcXXyzU89XrOKcwKFxrYmGZGQz_Vp7-keX_7OOBHqTiqvyjP42PR5Brpdm6U6IlpZD6ySWGi0gsg7K9Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f5c780577.mp4?token=iI98XJ7F_rICun8zDywcoQ-9PYLL0dKcVg3wVR3So2zhbNjKOUoDoaUTFp30VN_0WGrTRplvdTeR6bmWj-sQEth0IF_Lt-9lEJ6tI3_jQZ958DP1qofVRPUa9YVzxw0IhEgywrq0ip3KcwySozyz-_cDMm0sD2Qb7Mfb7uMT_1AnKhEgp35Xxd7_DcUVb_2CS6BcuUzl5JkGHX3P_doa-PZX_GVMhOC5jlu2tLrAGpF4OpTBfzbZ1GceDvSUx4z7mAN6_GcXXyzU89XrOKcwKFxrYmGZGQz_Vp7-keX_7OOBHqTiqvyjP42PR5Brpdm6U6IlpZD6ySWGi0gsg7K9Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
علوی، سخنگوی فدراسیون فوتبال: استقلال قهرمان فصل گذشته نشده و بحث جدیدی درمورد اهدای جام به این تیم نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107707" target="_blank">📅 22:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107706">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3539953949.mp4?token=cRa-eenfal5ZhpKJSJEBPiiiV-vEnE5VzMnJX3KxaZ6ORtQhFT451BhwElSexEoezaY66ATIdnM90QQ93MH6D-MqxReqzM5ImOqEHtvAjFFFMn9xPvY07HRpj-AeI2xIiENr0JZ7EMyz6K8s-R4cqE6PSbN4kh7Uq2Cwn0xTdziIxD9QVxOs3GaKdBsMkoSAeWq_qy7zFELGvhi2f2dktkyrpbP1X7QK3X7ghEoLAxPIaJVNOjNHZKFiP3dRYnNGCqZoIgvbBScLNJi_sKxYxWLq2V3Q6qY-qqb6ZruflSeClQTVtc0BQWYlYCdMuieIBiSNUOXRTjgBTrGPuGAaGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3539953949.mp4?token=cRa-eenfal5ZhpKJSJEBPiiiV-vEnE5VzMnJX3KxaZ6ORtQhFT451BhwElSexEoezaY66ATIdnM90QQ93MH6D-MqxReqzM5ImOqEHtvAjFFFMn9xPvY07HRpj-AeI2xIiENr0JZ7EMyz6K8s-R4cqE6PSbN4kh7Uq2Cwn0xTdziIxD9QVxOs3GaKdBsMkoSAeWq_qy7zFELGvhi2f2dktkyrpbP1X7QK3X7ghEoLAxPIaJVNOjNHZKFiP3dRYnNGCqZoIgvbBScLNJi_sKxYxWLq2V3Q6qY-qqb6ZruflSeClQTVtc0BQWYlYCdMuieIBiSNUOXRTjgBTrGPuGAaGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حاج صفی: می گویند آقای قلعه نویی با یک نفر(جواد نکونام) مشکل دارد که من را به تیم ملی دعوت کند تا رکورد آن فرد را بزنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107706" target="_blank">📅 21:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107705">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KW2CM7MjvOtq4x9bnv-hv9wVGT6Ztc9fYEmc-F8rTfKEdpVykdnlHf_fySZrYiaZju-FuBkvBCJ08GcYplR7xJbqsX3VkmjGCUj8tbcGpijr5zwaqAv83x1tVWUFox6PtfPye_cUSY_I87Qej54IFLAPnW9ubut0992r571X9mSV2H5XKFNm393PaEwZCRGTCKqYwHdfBicfYlZwSUd7EHbRMK8fQFglDXTiLU2e1QWQf5xPsC27Z0hr6Vbo6bnA88cpPJrzixVxnszGuMjSVY-duZE0_HkxW8YwhY4MoU8F1F_LZY8t3Tpzr6FQC-DaTaPi5KmYWtTp7VOYXVMrvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب تیم‌ملی فرانسه مقابل ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107705" target="_blank">📅 21:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107704">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdDQCHF_2cqfEGKkDL5opqewlbXYn4bC7k6IzvUHlEZ1ja0EWeDJMq7Iq-DhMJD6s8FGwwaeth4i-EvwZ0t7ao7vECwh0aHRwooWFX3K7bSJEtQd61ipkZ9lreOe1Tr9XtCEwK7V6kUhd2R6_V8Ex8MlsB7xXKtqjNGqr_vGjJyFc_k2LgjbvP-ktPfICyp8n2VSvtZ0GSJXfuU6kCGMQe0ruULKZIZfS81mj2x_bmdd2tMnjSWnV9FEF0UXBDQetuN5jJXNuw1LY8YNOKUtzCBEb2qfbS5uyh4Qm9ASFej9-5cMveYBaRnTNGsCRxQS5cdMLzorm2vrDhi0mjIQ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
پیش‌بینی‌های زلاتان از برخی نتایج فصل:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیگ برتر انگلیس؟ منچستر سیتی.
🇪🇸
🇪🇸
لیگ اسپانیا؟ بارسلونا.
🇪🇺
🇪🇸
لیگ قهرمانان اروپا؟ بارسلونا.
🏆
توپ طلایی؟ لامین یامال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107704" target="_blank">📅 20:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107703">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E557w0XL4jZbU2Mang9T6PfVTV1vJRYBaCfqHOjQOLVeLRs5or-EXOrj1hySRk7-9HuNu2EpeTYox1KqKuYRCmmW6ipOIDg8VpbscItEQoMIc8ShpYRcV2DTKnBbm4XZQ1ybylxNK4q8U8YxakdUPbCO1kpaB60MTJcLGthhHxkwCeZUnzrMdu2EniJtrxIYKdG1bhdNE06r-3VG0FR5oBul_ztD4C_F-JLGxW7wGTY8QJA6Xj2XetMj8noWoxY89LuyzJzDtKSKCpdCkFN19aok2zRUL-MTkHK2iRUruT9qtEqeohYh5k_s-vMF9ND8dM5x6rf0Xa0oGwA7NKoWRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب تیم‌ملی فرانسه مقابل ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107703" target="_blank">📅 20:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107702">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGh59HkTQEMcpXXr2tBf9xX-NU71ruIQpXUi6eRC5qPQO81Hbwb2Gj0T2fUH1HL0rRhqGwpC7qLn7llAlGrQilAwOHR-_Z1BTvwBpKZcWy5VnhMGCT3YCFi7XwYPT3wSSayuXJKh7eXu0u9QS1fIUlnh4axQS4VliJievBEWE91OX0xP6-nS4qT1AgL1jFUIWLwRRPqCEiV0DGyMsNOQnPvNTyq3G_5UQeS13QRFj1xRoy4e_lNWTyfdTk5864hQPFC3L106chSrek9GuWTlB9WjzAXSRCOUzHWx5BBoOJfwOoq10-_ZgjVrHs2XvCbH8pw4hdebV92-Khdx-5CFmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📱
نشریه The Athletic
در فصل 2017/18، گواردیولا اولین عنوان قهرمانی لیگ را با منچسترسیتی به دست آورد.
منچسترسیتی حدود 100 میلیون پوند قوانین مالی (PSR) را نقض کرده است.
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107702" target="_blank">📅 20:24 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107701">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af474384fb.mp4?token=jpCq5ic2ljRUGZEXnUDgKE0vbbjeusjGsVkFMqY8zx8MritAPDxki4Fp7LjZ1CKMbT6Pve12zysOVHwnu4pq9QSEwLbZ8vRwoVDXm_Sa-mCatzps6HR4EUn6VGU7u7vXAfTvX_f85IR_N3f9NvDc-gg01rGKVU2gB41dDL8Zii5QQW9l0KbXDBsX9ATfjzQezMVvzTmprPGhtSbiOH_wbjMj522jE8hE_sdWc1-vOktm81uEEuWY-1cnNfqeNqz6kClDilLx6NsTJDKLiYgN5Vruj_UygyDm5JDGT591P7AeJ8ztFHPTOzi1w-ixRPVtkm7w4mY_nbiqzVc7aC0aEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af474384fb.mp4?token=jpCq5ic2ljRUGZEXnUDgKE0vbbjeusjGsVkFMqY8zx8MritAPDxki4Fp7LjZ1CKMbT6Pve12zysOVHwnu4pq9QSEwLbZ8vRwoVDXm_Sa-mCatzps6HR4EUn6VGU7u7vXAfTvX_f85IR_N3f9NvDc-gg01rGKVU2gB41dDL8Zii5QQW9l0KbXDBsX9ATfjzQezMVvzTmprPGhtSbiOH_wbjMj522jE8hE_sdWc1-vOktm81uEEuWY-1cnNfqeNqz6kClDilLx6NsTJDKLiYgN5Vruj_UygyDm5JDGT591P7AeJ8ztFHPTOzi1w-ixRPVtkm7w4mY_nbiqzVc7aC0aEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚠️
رضا علیپور، نایب‌قهرمان سنگ‌نوردی بازی‌های آسیایی ۲۰۲۶ ناگویا، با انتشار ویدیویی در اینستاگرام، به پخش نشدن مسابقاتش از صدا و سیما اعتراض کرد: «همه مسابقات را صدا و سیما نشان می‌دهد؛ سکو، فینال، چه برده، چه بازنده، اما به ما که می‌رسد،‌ نشان نمی‌دهد. قضاوت با خودتان.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107701" target="_blank">📅 20:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107700">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad5607ff2b.mp4?token=BvML1delyE9aOT9bC_toYBUpcqFLMW2aozmefpfqeoPouzdhDD10z-jHc1x0KnqHnWGcl-TDH_z7-nLutzoXwkGiYkdHiVaiImZhLI6qRtncbKrEHrBS7JyPaOwDz0buQySeR_CzP9mJVpaC-uySDwIzE0RBEvfPRqy-tHzxaNTAU_Ab6fLAGd6HvQe0FaRNXbsOsJJ5YxJ3jg-FWHJ1rllV4bg_mRzP0iq0xgX2wD-NBbIPQ2VDBLX-gEp-eKkYmtDRl8vX06z7SMdmkToJTdkXUPz_CtUyVH43YBAjlh_tHLWf0A1R2qn1bQ1W5x73coS-WJXcjkvlZDNHDcM_qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad5607ff2b.mp4?token=BvML1delyE9aOT9bC_toYBUpcqFLMW2aozmefpfqeoPouzdhDD10z-jHc1x0KnqHnWGcl-TDH_z7-nLutzoXwkGiYkdHiVaiImZhLI6qRtncbKrEHrBS7JyPaOwDz0buQySeR_CzP9mJVpaC-uySDwIzE0RBEvfPRqy-tHzxaNTAU_Ab6fLAGd6HvQe0FaRNXbsOsJJ5YxJ3jg-FWHJ1rllV4bg_mRzP0iq0xgX2wD-NBbIPQ2VDBLX-gEp-eKkYmtDRl8vX06z7SMdmkToJTdkXUPz_CtUyVH43YBAjlh_tHLWf0A1R2qn1bQ1W5x73coS-WJXcjkvlZDNHDcM_qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
حاج‌صفی: در کار آقای قلعه‌نویی و کادر فنی تیم ملی اصلا دخالتی نمی کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107700" target="_blank">📅 20:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107699">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f60d798d01.mp4?token=fA-e7EKjRfsPWtql8cz7vJn0oHlnhof5aeLCBhimK2RKbvrUEPxThdjzsZerwfAtxSdkM_43G-LIWyCa1Mq5_uEE854EFgdqsbvt1nWlWI-Zv9OfFa2dSn19uRKSgI5lVfEfJhpNS-ISDrL0T43as8Y0SVhqJW9R9ygvk-cfRoPHQMNSq0tVihQ692srnM99jyWf32-M40vApwhEc6SPlrH5hcLnq1pxbxXEFLp9uL7BJV5MqahqDVYfbkU68KsucZsSWphgbMdjSz9XrPNnosHdUcpauP4aqo49xVychOB5BmvZUjXqGF2JmeM7bXPou58BMIJym3yC_tHL5Qc1VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f60d798d01.mp4?token=fA-e7EKjRfsPWtql8cz7vJn0oHlnhof5aeLCBhimK2RKbvrUEPxThdjzsZerwfAtxSdkM_43G-LIWyCa1Mq5_uEE854EFgdqsbvt1nWlWI-Zv9OfFa2dSn19uRKSgI5lVfEfJhpNS-ISDrL0T43as8Y0SVhqJW9R9ygvk-cfRoPHQMNSq0tVihQ692srnM99jyWf32-M40vApwhEc6SPlrH5hcLnq1pxbxXEFLp9uL7BJV5MqahqDVYfbkU68KsucZsSWphgbMdjSz9XrPNnosHdUcpauP4aqo49xVychOB5BmvZUjXqGF2JmeM7bXPou58BMIJym3yC_tHL5Qc1VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
درآمد ۲۰۰ میلیاردی مهدی شجاری مالک موبو نیوز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107699" target="_blank">📅 20:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107698">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8956163759.mp4?token=HjMM1nQYjLM3tNp-yiS7eOG3JwXk2S_vX2xFkKSlIg3RCXc6SvtJrIJJJc95E20ay2pjmH1veJwlS_RjrPy-i7zjDVd593DVuiGVYLO4DhFfYmOn8rIgr0dNCQ5E2YDMpMtllnKImr2iWGsbGQXN92Rhv49R5DIscW2u0ujmvsuZPzNkZrp9GsYvp5tZkRGEWURLh5kXY99PlgdcT_JH8aZ_5dQ7n-KBfopI_9OukdYdKfs-8MCyxsEKEXcXJTPhNhZ6UJKtnLVMiOZE-FV8LEc-bQastW4SftQotqe9LrvDfW8XBOPyesoraevWvu9E20Wntz7Efg7Sd71MZiA6eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8956163759.mp4?token=HjMM1nQYjLM3tNp-yiS7eOG3JwXk2S_vX2xFkKSlIg3RCXc6SvtJrIJJJc95E20ay2pjmH1veJwlS_RjrPy-i7zjDVd593DVuiGVYLO4DhFfYmOn8rIgr0dNCQ5E2YDMpMtllnKImr2iWGsbGQXN92Rhv49R5DIscW2u0ujmvsuZPzNkZrp9GsYvp5tZkRGEWURLh5kXY99PlgdcT_JH8aZ_5dQ7n-KBfopI_9OukdYdKfs-8MCyxsEKEXcXJTPhNhZ6UJKtnLVMiOZE-FV8LEc-bQastW4SftQotqe9LrvDfW8XBOPyesoraevWvu9E20Wntz7Efg7Sd71MZiA6eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤡
کیف کوک ژسوس بعد جدایی رونالدو از پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107698" target="_blank">📅 19:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107697">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/263935f09a.mp4?token=LPPWjC1ZSz-903KAKDcAPQvt6Cv-lbcrGhMffRmJxgPn86V4tWZqEdTJywFNP-NHUKsu9MKIA7ymUMlPdhcuIgOTnbBv9zP6jTYuckd7A3VbSt4q1K75-1VZSC55vfa9a3mNkJj_atc0vXB_ccdJN-T1NjcJhQxy6Fl64BY3gQUdi89AiD_hH3iDc-zF1sU5a9fz4fEUzBCM2j3PYjtXPsZNwVvSPv7G5Ki-Uk_OyjOrhy5c4Vbp3F2avG73yXEA8Lkfx2Qk9dyYMEvV9GXubQWEMed4MY9YwlbPQQRERoH8AYqU377UwMdfWArGILa3YHLwpxnLr3iC1UEHotd1uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/263935f09a.mp4?token=LPPWjC1ZSz-903KAKDcAPQvt6Cv-lbcrGhMffRmJxgPn86V4tWZqEdTJywFNP-NHUKsu9MKIA7ymUMlPdhcuIgOTnbBv9zP6jTYuckd7A3VbSt4q1K75-1VZSC55vfa9a3mNkJj_atc0vXB_ccdJN-T1NjcJhQxy6Fl64BY3gQUdi89AiD_hH3iDc-zF1sU5a9fz4fEUzBCM2j3PYjtXPsZNwVvSPv7G5Ki-Uk_OyjOrhy5c4Vbp3F2avG73yXEA8Lkfx2Qk9dyYMEvV9GXubQWEMed4MY9YwlbPQQRERoH8AYqU377UwMdfWArGILa3YHLwpxnLr3iC1UEHotd1uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
انتقادات از صحبت‌های عجیب احسان حدادی رئیس فدراسیون دوومیدانی جمهوری اسلامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107697" target="_blank">📅 19:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107696">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a8b7a5dd.mp4?token=Z1e-yuSatW7fKPlUqMCHihpL3sFWks9_MbEkO_RJubljeqVvtVzSfA3S_YOf2SC3C_yQqwB-11osBR6BOrqXnHojC7NloLNJuWV80RWjYuRp6eEkNMC68WPC9dVGYlUkgyS0LQJZaVe16M5HDmgTZj-UlANtnSdTrQqNA3xBWIcimX_YzR7_qsJtF2nifwt_ZXbnA7sxY74FcScl58zqf8lABaGCErAyQSCoCWpC6Hh-w5qCRcWhK8sZyBEolF5i9DokkdCi1TtbV4GZMrdIbyVgKJfBjlV8u4NGhdiK-pl8jBULXiIHbvLc6jLMz8HMgx3Y76AWUDccuKp8oZTeKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a8b7a5dd.mp4?token=Z1e-yuSatW7fKPlUqMCHihpL3sFWks9_MbEkO_RJubljeqVvtVzSfA3S_YOf2SC3C_yQqwB-11osBR6BOrqXnHojC7NloLNJuWV80RWjYuRp6eEkNMC68WPC9dVGYlUkgyS0LQJZaVe16M5HDmgTZj-UlANtnSdTrQqNA3xBWIcimX_YzR7_qsJtF2nifwt_ZXbnA7sxY74FcScl58zqf8lABaGCErAyQSCoCWpC6Hh-w5qCRcWhK8sZyBEolF5i9DokkdCi1TtbV4GZMrdIbyVgKJfBjlV8u4NGhdiK-pl8jBULXiIHbvLc6jLMz8HMgx3Y76AWUDccuKp8oZTeKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
✅
کیفیت تصویربرداری با آیفون 18 و یک سوپر دوربین فوق‌العاده از سونی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107696" target="_blank">📅 18:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107695">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svSheFDVfXczv3-JUrLbmfWn51VWlAv30fhMpoAPIlgsnO0q_ZAGVxN-wmZLcKY7Pn-_bcwWYlrhS6bes28HHkfvSQXDDRjRGz1_9UOamDDAHf74EBD_u1ZXnkpzk41b71s9-gy3-WqHYqZiEkC2zUlENqpZGrw-rX7M2Mvgd0Qq6t8BdgQf09Aoq9bqUw1pIeIW_q4raf_4x-leUMsCO2RrC1WqeW6a_1CEqys9Nw6R8FCArHwxgbBrnzKUZFwfs1YWIsGPLp_kCaJjneHP2iaM-NQGEUQqAHX4OjWD0WMb1MBniDZUFeDvkUdBsKA05qinGTGOPAEJmjPailNTaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
✔️
پرسپولیس در دیدار تدارکاتی مقابل گل‌گهر سیرجان با گل‌های محبی و محمدحسین صادقی به برتری رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107695" target="_blank">📅 18:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107694">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvSytj8SlTK55dC3SVaJXzZQnRq4KOiuii-r_ntvH5lNsfZ4DBgfKx49Mm-IscMKdqV-qDKjNAncO4M-08BCciDAxhFZqDZJ9KVnDmzCN6jC1JE5wkFXdpH593EzYCY-aLUPFYnGDMEFGm8ZyvjSWSgYOz33NYoGxv64B9FO1rlXVu-4QJBeq04snWH39bl_uZBZYJG31-3AYNPlHdTIo1j9vCVYv_88Wac9dBw9OL6OL5MA0ZOq3XVJCP3VRgUqHLAEwr170O6TZbiqlK3BquQ7SUGq5B_gozL2lknckSNKjDQAh93tkx42wetRv3R04HXSL0LNCKfV0gbMlmzPIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
یوونتوس قصد دارد تابستان آینده به عنوان بازیکن آزاد با ویرجیل‌فن‌دایک قرارداد ببندد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107694" target="_blank">📅 17:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107693">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/507dbd5bf2.mp4?token=UmMn-A8VlcGSgKf4xjCnn9ZgOXW6y9XWzxjeJB41w6Wr1a6-BzR-jHOKMo2echaV6ZkpLimQYRyHTcHgcukLFz5YZYccP6I_Y8-5a1YunsVibIJm69J04U8XL-K79Fafo8LC6mj9QEDNbj8DTy3ymkyqWEYiaJnImOYstdmpVXLbVIpzditfaRvTtCqL-RTdai652-zOR6xp3EXZ-gEj2IRunpQ-DZabTi6aiVqLMeVGF9okFkg7z-fqOvXhHVF-DMUhFQaCISJREihbkNDGufs-s1rNSR-tXmaFCrRJecH4I6-N3_0YsYIcCyWaqU_zwcF6ErX8uvHld8caN2bqxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/507dbd5bf2.mp4?token=UmMn-A8VlcGSgKf4xjCnn9ZgOXW6y9XWzxjeJB41w6Wr1a6-BzR-jHOKMo2echaV6ZkpLimQYRyHTcHgcukLFz5YZYccP6I_Y8-5a1YunsVibIJm69J04U8XL-K79Fafo8LC6mj9QEDNbj8DTy3ymkyqWEYiaJnImOYstdmpVXLbVIpzditfaRvTtCqL-RTdai652-zOR6xp3EXZ-gEj2IRunpQ-DZabTi6aiVqLMeVGF9okFkg7z-fqOvXhHVF-DMUhFQaCISJREihbkNDGufs-s1rNSR-tXmaFCrRJecH4I6-N3_0YsYIcCyWaqU_zwcF6ErX8uvHld8caN2bqxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
امیرحسین صادقی: علی منصوریان بهم گفت چون شبیه نیکبختی، یا باید زن بگیری یا نمیذارم فوتبال بازی کنی! با حاج محمود سفت وایسادن تا زن بگیرم حتی شاهد عقدم بودن که خیالشون راحت شه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107693" target="_blank">📅 17:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107690">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa4517b308.mp4?token=oxQDibweoJWjdHDIVX_r0j_8OnudMnKYwyTjtx-zrTXKWJBJS6sXYQNg-oUbAK38JVf3hI5tdJZSa7G7t_Aay0Sm54G4HqXQHtZ2No4PN-CWk_soG7vTdRMbJDj5A_jejwH6k7m0AEjWtz8mg1lPsFycs0Cg0NS1-Etpx9f3AimRIhsV3k3X0BVEwgNo_kG6iS-pcuwAlpllGxVrf6eFUZeEc8L9h0w7QNKd9hvIOq0cJGo2yD09Qh7uh7-yEmVb4F-3jSUHy68C8bp9NDYh_8uGWT0mZPTwSqOSGkiCd3n_nMMN-1RXrOnO2C4orTtuRwPH2pTxrkI8hMEys5JYKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa4517b308.mp4?token=oxQDibweoJWjdHDIVX_r0j_8OnudMnKYwyTjtx-zrTXKWJBJS6sXYQNg-oUbAK38JVf3hI5tdJZSa7G7t_Aay0Sm54G4HqXQHtZ2No4PN-CWk_soG7vTdRMbJDj5A_jejwH6k7m0AEjWtz8mg1lPsFycs0Cg0NS1-Etpx9f3AimRIhsV3k3X0BVEwgNo_kG6iS-pcuwAlpllGxVrf6eFUZeEc8L9h0w7QNKd9hvIOq0cJGo2yD09Qh7uh7-yEmVb4F-3jSUHy68C8bp9NDYh_8uGWT0mZPTwSqOSGkiCd3n_nMMN-1RXrOnO2C4orTtuRwPH2pTxrkI8hMEys5JYKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
تعجب و عصبانیت قیاسی از قیمت دلار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107690" target="_blank">📅 17:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107689">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fac9f22f0e.mp4?token=im67lQVViswFxZTRXEt1qQG_oKWyIMMVDWI_j-9ycqbwP4Ncb9qKUMuHhEcwzfOEKmWr4vSeXm0Omkgagw_Iph0vr9UqSosDcYu8K-CevFOsySgTWnYI-FQsT1S1k-6czybCHXigEXlTgNr-ZQ388Cov4Gsm_28f9UchZye-WrkNibOQHl2UvAKa1_y9RLAFivvVxAbUtWb5I8mbqC_sgWHB4aVoG3MXPfBx_RrZcetujtUJUO2wtrmjNGe2wcmRjKqBRUtxID9jICXztBApk4WGQ0Lpv7Sf1jCriYh7wj5mMxtGeFwIb__bFGNBKVohH6n88KBjMM-P5lm8_r9c1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fac9f22f0e.mp4?token=im67lQVViswFxZTRXEt1qQG_oKWyIMMVDWI_j-9ycqbwP4Ncb9qKUMuHhEcwzfOEKmWr4vSeXm0Omkgagw_Iph0vr9UqSosDcYu8K-CevFOsySgTWnYI-FQsT1S1k-6czybCHXigEXlTgNr-ZQ388Cov4Gsm_28f9UchZye-WrkNibOQHl2UvAKa1_y9RLAFivvVxAbUtWb5I8mbqC_sgWHB4aVoG3MXPfBx_RrZcetujtUJUO2wtrmjNGe2wcmRjKqBRUtxID9jICXztBApk4WGQ0Lpv7Sf1jCriYh7wj5mMxtGeFwIb__bFGNBKVohH6n88KBjMM-P5lm8_r9c1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
امیرمحمد، خواننده آهنگ سنی نردن گوردوم رو بردن برنامه تلویزیونی ترکیه، اولش براش دست زدن و کلی تشویقش کردن،
ولی به آخرش که رسید دیگه نتونستن جلو خنده‌شون بگیرن و همه زدن زیر خنده :)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107689" target="_blank">📅 16:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107688">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c643f6bb4.mp4?token=KVOObC3_NaFVp7ATmRvJiwejQ00f4FLF5h-0EWzxarImlwKhcVJ6duaaRmSP90uHjdMQFT6hy6gs4SSXdHVU2ZT-soM41_DQac3cy_WaRYWuUjHM6aE7wYEqjCwCPS7yurU0uoptsATN-RsJtILxbkl2L5e7BgeL7aQOGNsSKNLnD-yjmIsNUUuJ5KVrZrQH85j-r8tX3F6OmNdC3DG0v8e5EgWaTiU9Obr8R023HJYbO-NeVAsp528M3qu9-REMBwS0f0Fbw9U1YFDDpaRmgZ3j_PGrRvHk-7N8T4v_dZcsMdizakHojBL2Yblrvz3G5NGe2gSJR7T0CFBRMckdfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c643f6bb4.mp4?token=KVOObC3_NaFVp7ATmRvJiwejQ00f4FLF5h-0EWzxarImlwKhcVJ6duaaRmSP90uHjdMQFT6hy6gs4SSXdHVU2ZT-soM41_DQac3cy_WaRYWuUjHM6aE7wYEqjCwCPS7yurU0uoptsATN-RsJtILxbkl2L5e7BgeL7aQOGNsSKNLnD-yjmIsNUUuJ5KVrZrQH85j-r8tX3F6OmNdC3DG0v8e5EgWaTiU9Obr8R023HJYbO-NeVAsp528M3qu9-REMBwS0f0Fbw9U1YFDDpaRmgZ3j_PGrRvHk-7N8T4v_dZcsMdizakHojBL2Yblrvz3G5NGe2gSJR7T0CFBRMckdfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
خوانندگی فرزند محمد شریعتمداری وزیر اسبق کار و صمت و مدیرعامل هلدینگ‌خلیج‌فارس مالک باشگاه استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107688" target="_blank">📅 16:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107687">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebc463f33d.mp4?token=Gkbkre9vfVVaXRgo9xRbSMuYum0s75R2q0nFLn6bZrkzVGeJu3du7oY85vTzlCwHoP9pQi59XdvU_yV-0DXw2NSkc8tR5BBQlAAikRTZFH4IvGNbHX0TVYxRuQm5Q62d427YP0JYNfk9jY7xoVZG8TO-zfcZ8N2Ty879hKDEBdI_bpDAvvq-BuRwtiqqd756YHqQ8v6AuhZu4q2ZCYDGK5lws4kGbw8LqD9hRTH27nggQleVAGhJRGJWBq54jbImzExehpT2Z2ji6S1azQf2F9yOse7-m5Y7l9XpoC4cHer9RaZqQF_5_sl7-EZEAFCtzyKEG1s0pzFo5ovrPIldU4c6BGjVQ01WNytVkhFB1heqK3qp2qXEMH0PLLP8epbdIGZHCW996m50gKzhylCGPJXmESjvyuZBq7ewZR52EJNir6-RzDvs2vKs23rSMlrcVQS7y-amy8j5qrCAQ55VPSm1WAnwAUEqmxl7XizXuVIrfGMv7aE4463laj4HqMXciVHHEnK7OP5xctlL9_rndUvJU55A554qKVI6a2HrfD0uUyyvcJorYtR5qKuR_MevSqelg4cc44FiaSS0_nvIDljuCUHYXA7Lu6Zu_WpUIcMeYDwzQwjDeLzZ3zhFo3ippGLoJqnZcOY5q5OIPzn0Fru4_95JQzvcqKGf90f3FOc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebc463f33d.mp4?token=Gkbkre9vfVVaXRgo9xRbSMuYum0s75R2q0nFLn6bZrkzVGeJu3du7oY85vTzlCwHoP9pQi59XdvU_yV-0DXw2NSkc8tR5BBQlAAikRTZFH4IvGNbHX0TVYxRuQm5Q62d427YP0JYNfk9jY7xoVZG8TO-zfcZ8N2Ty879hKDEBdI_bpDAvvq-BuRwtiqqd756YHqQ8v6AuhZu4q2ZCYDGK5lws4kGbw8LqD9hRTH27nggQleVAGhJRGJWBq54jbImzExehpT2Z2ji6S1azQf2F9yOse7-m5Y7l9XpoC4cHer9RaZqQF_5_sl7-EZEAFCtzyKEG1s0pzFo5ovrPIldU4c6BGjVQ01WNytVkhFB1heqK3qp2qXEMH0PLLP8epbdIGZHCW996m50gKzhylCGPJXmESjvyuZBq7ewZR52EJNir6-RzDvs2vKs23rSMlrcVQS7y-amy8j5qrCAQ55VPSm1WAnwAUEqmxl7XizXuVIrfGMv7aE4463laj4HqMXciVHHEnK7OP5xctlL9_rndUvJU55A554qKVI6a2HrfD0uUyyvcJorYtR5qKuR_MevSqelg4cc44FiaSS0_nvIDljuCUHYXA7Lu6Zu_WpUIcMeYDwzQwjDeLzZ3zhFo3ippGLoJqnZcOY5q5OIPzn0Fru4_95JQzvcqKGf90f3FOc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
یک‌دقیقه با اسطوره رونالدو در لباس پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107687" target="_blank">📅 16:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107686">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/098c9ea234.mp4?token=a6bGS3ioeE_Q6JJpD0Bb9PQO738ZIlnffDEW5Kj0q0p96ECx4oFrrsntjiH51Ja3RoBsCppgLKcmr3nJqOYZnG_rLebYMoK4dDvkokuxP2Z45Fqgjzt9XE-neBFDor8V_C9yDU4BogG4HO9GneQcZtMltKEeeOcs1KmuCEbwEDxwnznDW81UoruB6xAQCpbPc1Xf8QvSJZ8xH80ezAJtoUgZv1NbA_6Rlz9bY9OFPXub5azfOGsuburIHV8mT6dVHh6HR1CIXxnZWuFJXnFGzXrs1bG8fySrSlBAsjdfLBhKrB2CnbqUX-hXOdJi3DSgB5yjtJJDvsy0sHUF4W9pVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/098c9ea234.mp4?token=a6bGS3ioeE_Q6JJpD0Bb9PQO738ZIlnffDEW5Kj0q0p96ECx4oFrrsntjiH51Ja3RoBsCppgLKcmr3nJqOYZnG_rLebYMoK4dDvkokuxP2Z45Fqgjzt9XE-neBFDor8V_C9yDU4BogG4HO9GneQcZtMltKEeeOcs1KmuCEbwEDxwnznDW81UoruB6xAQCpbPc1Xf8QvSJZ8xH80ezAJtoUgZv1NbA_6Rlz9bY9OFPXub5azfOGsuburIHV8mT6dVHh6HR1CIXxnZWuFJXnFGzXrs1bG8fySrSlBAsjdfLBhKrB2CnbqUX-hXOdJi3DSgB5yjtJJDvsy0sHUF4W9pVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ابراهیم شکوری تا رحمان رضایی ...
‼️
در جواب ناکامی بگویید: یخورده سرما دارم
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107686" target="_blank">📅 15:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107685">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/086fe81733.mp4?token=n2fL6HucYGck02lIrKJxfnNecHFRmvtYqr11RPE6XUN7KSKyMmMfV9nfD0QO3M5K62CgeIovHa7o6jCW16Lf-3ymXg_ghCmtb4hUXye1xZPor17cx672MpDaqqkArT7F6HIuOfTWceHP4p-6W3oV-VZr92Vgjwp0gRq_3ERhuwd_Pcod3wdSddqWahIM0OnC2gfoGdmSI9s2GyJFZUcf0jWcRbnUxindWNSAsU4oTXRTrZhpv9Mlj97E3A7cAd_2WxzfmkARaKyNJj-LZkZbyoxxjqOZPUvCbeSFiTl3XGfpWiQO16EXkkbkW30v4spaaj8X_IKXNdIYKuJmqQ0YFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/086fe81733.mp4?token=n2fL6HucYGck02lIrKJxfnNecHFRmvtYqr11RPE6XUN7KSKyMmMfV9nfD0QO3M5K62CgeIovHa7o6jCW16Lf-3ymXg_ghCmtb4hUXye1xZPor17cx672MpDaqqkArT7F6HIuOfTWceHP4p-6W3oV-VZr92Vgjwp0gRq_3ERhuwd_Pcod3wdSddqWahIM0OnC2gfoGdmSI9s2GyJFZUcf0jWcRbnUxindWNSAsU4oTXRTrZhpv9Mlj97E3A7cAd_2WxzfmkARaKyNJj-LZkZbyoxxjqOZPUvCbeSFiTl3XGfpWiQO16EXkkbkW30v4spaaj8X_IKXNdIYKuJmqQ0YFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
‼️
رونالدو رفت و پرتغال تمام شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107685" target="_blank">📅 15:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107684">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/it-EWR5Zk12aJeM7m3mUdgczrp_S9PLhc97na59I2efhQrqJjIpT_FMCoqkjyAc6hEtEJ00XkiHGlk8Wzpy_g56pf_TFoPyWFzc1S6FbeRlze9VpYYmvT-ovQSP-Aq_16EsErF-lUaAHWbDUfjOqcMocFM0xRzmwU-Wk67R2MAzaGTzjSx0W3c2Rhtu0oTnH50ZXz1nAdwaUcJAJuTuUSNrg7_kz92VE5WalFKKk-HcRyOiML-3TjaJ0-bDFrL8-6ZNAgDlXS2Lo5wb-kkisCSWooKQve626K2-UU2hy17wjAXXIhq8dC6lya4K4NIVrvZ7gISg5b2dLXZZx3KC6Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✔️
🇪🇸
فابریزیو رومانو:
🔻
نتایج آزمایش‌های کادر پزشکی بارسلونا تایید می‌کند که مصدومیت عضلانی رافینیا که در اردوی تیم ملی برزیل دچار آن شد، جدی نیست. رافینیا از هفته آینده در دسترس خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107684" target="_blank">📅 15:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107683">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2fc633f5.mp4?token=TqhrcBqOs6iUaOVInmRhVcIf8i9YWNmjseWRRAXCr7wSFfS80dtXU8R1CZsVM8F5-KA9zS8aCUxcKhjrOZASPcIN4KS2ucmxFVqX3EpKsdXkQYWCex-T2uwXaN6aGcNK7wRWymnPyIpl18XndtMbZNRl1PUuEAuSRFW8_yx_uL3RNNc6dz2ApE4fcpXyIXsZaAXMskr3q7d4AJdWRkgKN9UTHa8M-b9yhM2Z3hzBigPOw1JayyVjJZIFnQHpKPIeXIPxlFESqsp4vlr0pWEfPXDrftisfbg1r7j5_2oBb-digNFqsVvc6JtptvS1WrTbgEa19FK9gbGS-1hxLjJocA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2fc633f5.mp4?token=TqhrcBqOs6iUaOVInmRhVcIf8i9YWNmjseWRRAXCr7wSFfS80dtXU8R1CZsVM8F5-KA9zS8aCUxcKhjrOZASPcIN4KS2ucmxFVqX3EpKsdXkQYWCex-T2uwXaN6aGcNK7wRWymnPyIpl18XndtMbZNRl1PUuEAuSRFW8_yx_uL3RNNc6dz2ApE4fcpXyIXsZaAXMskr3q7d4AJdWRkgKN9UTHa8M-b9yhM2Z3hzBigPOw1JayyVjJZIFnQHpKPIeXIPxlFESqsp4vlr0pWEfPXDrftisfbg1r7j5_2oBb-digNFqsVvc6JtptvS1WrTbgEa19FK9gbGS-1hxLjJocA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔝
🌟
رسانه‌ها با انتشار این تصاویر مدعی شدن که نیروهای خنثی‌سازی هسته‌ای آمریکا همراه با یگان 75 عملیات ویژه، شبیه‌سازی و تمریناتی برای تصرف و پاکسازی تاسیسات هسته‌ای زیرزمینی ایران انجام دادن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107683" target="_blank">📅 15:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107682">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0274908694.mp4?token=vDYIFyKgfemI5zZAil-0xSQX_LTxgEiktKvey-H8yL21FEGo5LabhlQ_izyzQM0jMyjhdhEK17Ng5kMIWVAklJVrNiW8amXz5b8iXdVZHTbsoZzHbNOM4JD56UCxcvNXWYXAGwWPWUp78yr7kM4dZQ0qkDsEAv3pycnHkplz07U2XwcMdW91XJNiz1nrXYS-zefzHi-3bxxd2TMG8zXCe5nb6-LXszz8eYssm86RsY4Xw46NrCYwAZZKFl879YFtLk449Gpx4twQ-W4rXshwtADX6BEs44-oATv6owA7PlgDgfqfOiNgfgAoc3JRc4X7vbbt6vtXeEsYzz1GmupzBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0274908694.mp4?token=vDYIFyKgfemI5zZAil-0xSQX_LTxgEiktKvey-H8yL21FEGo5LabhlQ_izyzQM0jMyjhdhEK17Ng5kMIWVAklJVrNiW8amXz5b8iXdVZHTbsoZzHbNOM4JD56UCxcvNXWYXAGwWPWUp78yr7kM4dZQ0qkDsEAv3pycnHkplz07U2XwcMdW91XJNiz1nrXYS-zefzHi-3bxxd2TMG8zXCe5nb6-LXszz8eYssm86RsY4Xw46NrCYwAZZKFl879YFtLk449Gpx4twQ-W4rXshwtADX6BEs44-oATv6owA7PlgDgfqfOiNgfgAoc3JRc4X7vbbt6vtXeEsYzz1GmupzBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
⚽️
پایانِ متفاوتِ دو اسطوره.
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107682" target="_blank">📅 14:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107681">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6703d31fc.mp4?token=pVQkApfXJAcynkCAUK2rXhZ495l0eLCRQM-e_20VvZJJBKmtl7ibw2_SiRPXynaHn94xYlpNPYsuP4s6HifG95zTBp2qIXnz4gL5NlUUr5QPT06ekW5CS_BQcAjGin3pTt9oT7QqnxO6VKtESvHWmw-svunn2XOKAGMYLCXqDECQIiffW8Zzy2DiN79M5q2nkShsNl2nMWw2CN50o34GtTitRRx4p4rgCVlVuOCR_2W1CQcEzMhcPprL7Pseg8OWfQSvGDuwcww0lslkTIydphSKAuaK0VYHkno_JPLu1MXdn5DqGNwXN8zsyEOjhQ9ZEIR1QcgympGjcg-8Qm9EAhmNE-mNjaVYYBkjBecgyst-PG3a6CLV4_zDJLl7CfCQZrzQesgpOfS4eqEQL-OTFWWZrOhnqrspAUq4CD3zS7K6HPA91FBe-Tj7AfTjfRmJ2N1aSC5CkyIGNmvy5kCU7l7Wz2PIGf2jDEs5Zr4vDUA3D1LcFieVRlV7FP3_oYmhB8vcF0daIsy2j9yWuzH7PR3Wcs_so5e5nzLXHh74AV-OD1MopZxObkhkugX3qAU8yfsWecNFwvlYsvkgAqOijKTIBGOdS6yYI69CTVoglKE5zsgn5emmtX8LO2CiCFde3Wp8EE5GTVwoCI4pK_Se94FkXPGr5n0qQ3FoNHBchu8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6703d31fc.mp4?token=pVQkApfXJAcynkCAUK2rXhZ495l0eLCRQM-e_20VvZJJBKmtl7ibw2_SiRPXynaHn94xYlpNPYsuP4s6HifG95zTBp2qIXnz4gL5NlUUr5QPT06ekW5CS_BQcAjGin3pTt9oT7QqnxO6VKtESvHWmw-svunn2XOKAGMYLCXqDECQIiffW8Zzy2DiN79M5q2nkShsNl2nMWw2CN50o34GtTitRRx4p4rgCVlVuOCR_2W1CQcEzMhcPprL7Pseg8OWfQSvGDuwcww0lslkTIydphSKAuaK0VYHkno_JPLu1MXdn5DqGNwXN8zsyEOjhQ9ZEIR1QcgympGjcg-8Qm9EAhmNE-mNjaVYYBkjBecgyst-PG3a6CLV4_zDJLl7CfCQZrzQesgpOfS4eqEQL-OTFWWZrOhnqrspAUq4CD3zS7K6HPA91FBe-Tj7AfTjfRmJ2N1aSC5CkyIGNmvy5kCU7l7Wz2PIGf2jDEs5Zr4vDUA3D1LcFieVRlV7FP3_oYmhB8vcF0daIsy2j9yWuzH7PR3Wcs_so5e5nzLXHh74AV-OD1MopZxObkhkugX3qAU8yfsWecNFwvlYsvkgAqOijKTIBGOdS6yYI69CTVoglKE5zsgn5emmtX8LO2CiCFde3Wp8EE5GTVwoCI4pK_Se94FkXPGr5n0qQ3FoNHBchu8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سکانس جدید از گزارشگر تکواندو براتون آوردم
😆
😆
😆
😆
😆
😆
کسب مدال طلا توسط ساغر مرادی در رشته تکواندو با شکست حریف ازبکستانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107681" target="_blank">📅 14:41 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107680">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/353ac7dbfb.mp4?token=XmgkuVqBChEnzaxhhEvb9m8vtI0qj6ORr58y2jMeWBqJa9wHIzItnegQdPBlRDzttEOR7-x7ouElAf1yz6PGH66SFBEU-s_8H4anu5_mPrPjzlHJ6OxwDx7aD0arjhHPxlCvtBuHmq82djRPXPfpzODtL6PVBf9F54s6JbPbudBBeIQHY6MIJfF5q7fJR0j-03g1UznY6uuLoGDqdcmPRCTted8va7z3lEyXcFkFtmOOUQPcDa7x0oKhxOQa0W8yXxozhPtQsKJRxFMM8xW8Hj2fnFejE3aXqwNr64UYOxLIPfWq0d_0XTv_FiQntW8r26MxLgQZWzWR2W0XssxloZfO7XjRQ6AUYvkNf7MRNcoPz7SOvmSuWdMD3_a4l1vYzWoh2YcyL_2Vn1XvKJncH-jaewk-3W4PVZJ9MmGCUM1kotm7hao1rbmplZWvOJzRLPVzbhRPpr5SFsZkPYI3E6fhb39p2iBBkQiqthD_bGFA3DX5Bgucr1tuZjQjMTIayV94ztzh7-hjLYNIi0d03hMGN8UNQtd4ghvFJhmHukfcdSY7iLeewt5KST6yLcf60sN_XSYk684ypa8EVVxR-rIRmFx8g7EgVeciIlBzBwjQ9kcsbxdvBluBBAZAOqR2o3Q7z4u7_ZSA_Kv644oghdOP0FcJzn_9bq0ZrpTLmb0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/353ac7dbfb.mp4?token=XmgkuVqBChEnzaxhhEvb9m8vtI0qj6ORr58y2jMeWBqJa9wHIzItnegQdPBlRDzttEOR7-x7ouElAf1yz6PGH66SFBEU-s_8H4anu5_mPrPjzlHJ6OxwDx7aD0arjhHPxlCvtBuHmq82djRPXPfpzODtL6PVBf9F54s6JbPbudBBeIQHY6MIJfF5q7fJR0j-03g1UznY6uuLoGDqdcmPRCTted8va7z3lEyXcFkFtmOOUQPcDa7x0oKhxOQa0W8yXxozhPtQsKJRxFMM8xW8Hj2fnFejE3aXqwNr64UYOxLIPfWq0d_0XTv_FiQntW8r26MxLgQZWzWR2W0XssxloZfO7XjRQ6AUYvkNf7MRNcoPz7SOvmSuWdMD3_a4l1vYzWoh2YcyL_2Vn1XvKJncH-jaewk-3W4PVZJ9MmGCUM1kotm7hao1rbmplZWvOJzRLPVzbhRPpr5SFsZkPYI3E6fhb39p2iBBkQiqthD_bGFA3DX5Bgucr1tuZjQjMTIayV94ztzh7-hjLYNIi0d03hMGN8UNQtd4ghvFJhmHukfcdSY7iLeewt5KST6yLcf60sN_XSYk684ypa8EVVxR-rIRmFx8g7EgVeciIlBzBwjQ9kcsbxdvBluBBAZAOqR2o3Q7z4u7_ZSA_Kv644oghdOP0FcJzn_9bq0ZrpTLmb0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥇
کسب مدال طلا توسط امیرحسین زارع با شکست حریف چینی در فینال بازی های آسیایی ناگویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107680" target="_blank">📅 14:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107679">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
وضعیت عجیب عدم پاسخگویی اعضای تیم قلعه‌نویی درباره نتایج ضعیف اخیر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107679" target="_blank">📅 14:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107678">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6MRe-D3LLgcTTWGlpEnRFo2s4bhEc9b0hd3pi-iWSi593IIrOLv_Qh0a1tenq5xCRpu9rZLj7kxWJ8gCpgj_BnJviUgoXQL9tS8CaATxP38RErTxwZpUtC2K4LGX4prnuH1XseoH9AROOLwfJrw4XWYSjXhGfjF7r_v-KImbm-JFLEmH1BAaEwqzOKE7b3Wjk4Z6N8bMMKq2nHpDfsi_V8Rq8-sYPGjvCccIcfu4liUY2SRXKG2kjtE2zrWtchgx1LHRH3L-4HIOn-A5L5Sg1Y-1VolMo9251nnoNjrfWo5q19aahSQ2EeN6Bk0MUSd0YXhUmqgkIkWjguqZA8L7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
⁉️
مسی یا رونالدو؟
👀
🤩
توماس مولر:
"در طول ۱۰ سال اول دوران حرفه‌ای‌ام، همیشه کریستیانو رونالدو را انتخاب می‌کردم و همیشه در مقابل او شکست می‌خوردم. اما وقتی به کل تصویر نگاه می‌کنم، متوجه می‌شوم که لیونل مسی، بزرگترین فوتبالیست است."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107678" target="_blank">📅 14:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107677">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3d0d9fde.mp4?token=AfsNHVqmwHZ6XdjMJl909AL24Kf2PYejSJMoffpLzyKwlnr3pUbQl9_X-iVJGMdwt59JB8f7TfliuUSObai6-UKuHlNoxAI5lm8d4A1YNh0GmZ6wjiOzx4Ey0tPSIpGxCbXpVJoHY7TE2iwtwTJju9hM0CT8-W6RuOGuu0l0--dZF1BKM8HfynO0YSZH-I5l1Yeo5JWgzIC6tfB-BGT5grqSybcalOsMmUniAbvIjvzAayQxFPOXswtswoifMBR9y7w1kKzI_H6W26jR8_32H9-xluVhd_v9sIJiPHaLEy6PUxkmjXTNKHEUr4ckrkbGrS-wlTYfH0IgERfnL0UTkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3d0d9fde.mp4?token=AfsNHVqmwHZ6XdjMJl909AL24Kf2PYejSJMoffpLzyKwlnr3pUbQl9_X-iVJGMdwt59JB8f7TfliuUSObai6-UKuHlNoxAI5lm8d4A1YNh0GmZ6wjiOzx4Ey0tPSIpGxCbXpVJoHY7TE2iwtwTJju9hM0CT8-W6RuOGuu0l0--dZF1BKM8HfynO0YSZH-I5l1Yeo5JWgzIC6tfB-BGT5grqSybcalOsMmUniAbvIjvzAayQxFPOXswtswoifMBR9y7w1kKzI_H6W26jR8_32H9-xluVhd_v9sIJiPHaLEy6PUxkmjXTNKHEUr4ckrkbGrS-wlTYfH0IgERfnL0UTkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚽️
دیس سنگین ژوله به قلعه‌نویی بدلیل سوال عجیبش از خبرنگار ازبکستانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107677" target="_blank">📅 14:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107676">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eade000140.mp4?token=P2bGA8Fe9h2Cxb4BQ1gwT8hZoLkHqv6NV0nucNXxRRxliYkWNlE9R8WQJmABewZvO70RrdNefMl0Jb7dvF2LyrmkOWDqWt0WCLbFDuBajU7n8sJf7HZLdUO3f7zoDu7CmAx4rpCou9E05-Eub93-zKSuK8GS4e4tagIWTfA0Cfpe5J-lDMCXBiKoIixhruegZwtJKqWjytL5NDAdO31Ur6Isr2yDCrs48zA6YIHRu70nSdzWaaInu8iOo80BGr9zb3UaKDNlYcRAI3J7iHCiq9ONh-JME0TfaZIOe4wFCydPAC_NItAEv_5PM0pU0yjTG3v09S-OHVT1MmpriFXQgj87KbbqiDqGMB_bf4fqOMhbu2F2AOv47Iq3I5WezGk0nj25VwpV25TJl30PpqCWsXr3ZU49-cN0NbBYat2N9XjnedXt7A_wak8-7jQNvX5bEL66ylGjuaA4OCStBg5tUwHxg6uxPDNrx71ezaRiI5ys1gs5FjdUlKjmV_EWHyOPqyKC_vZ5WdGCNqyzZ_nReMkHJBa01gEp2E1nJJzgFUyRnNsSdjLTWvjUH0w6OBcNzuDwKcOIS9FC4-523ZcpBH70kOHs_TWkpcOvasnNQMR5hduLTTgQaixB6wiAfPmuH9CeqKDXps-eRb4z-McrAeMjpl5NM4GU5_D02ln5a8M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eade000140.mp4?token=P2bGA8Fe9h2Cxb4BQ1gwT8hZoLkHqv6NV0nucNXxRRxliYkWNlE9R8WQJmABewZvO70RrdNefMl0Jb7dvF2LyrmkOWDqWt0WCLbFDuBajU7n8sJf7HZLdUO3f7zoDu7CmAx4rpCou9E05-Eub93-zKSuK8GS4e4tagIWTfA0Cfpe5J-lDMCXBiKoIixhruegZwtJKqWjytL5NDAdO31Ur6Isr2yDCrs48zA6YIHRu70nSdzWaaInu8iOo80BGr9zb3UaKDNlYcRAI3J7iHCiq9ONh-JME0TfaZIOe4wFCydPAC_NItAEv_5PM0pU0yjTG3v09S-OHVT1MmpriFXQgj87KbbqiDqGMB_bf4fqOMhbu2F2AOv47Iq3I5WezGk0nj25VwpV25TJl30PpqCWsXr3ZU49-cN0NbBYat2N9XjnedXt7A_wak8-7jQNvX5bEL66ylGjuaA4OCStBg5tUwHxg6uxPDNrx71ezaRiI5ys1gs5FjdUlKjmV_EWHyOPqyKC_vZ5WdGCNqyzZ_nReMkHJBa01gEp2E1nJJzgFUyRnNsSdjLTWvjUH0w6OBcNzuDwKcOIS9FC4-523ZcpBH70kOHs_TWkpcOvasnNQMR5hduLTTgQaixB6wiAfPmuH9CeqKDXps-eRb4z-McrAeMjpl5NM4GU5_D02ln5a8M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥇
کسب مدال طلا توسط محمد نخودی با شکست حریف ژاپنی در فینال بازی های آسیایی ناگویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107676" target="_blank">📅 13:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107675">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46780b4e7.mp4?token=NBIy1JyDhMk9aPnAuLkJaKGFJoHgX24-Mzo6obUTCRMe8XR6Eq69GLr0t6JKJBNngsxONgDSwjxZCVqXPRC8usV8IKtzIb0SZs9SQuFoATJH2LxsRWgCK_XDK87fuKWlA_vtPc93_4LP187sI6kdLWLclcDPHunedlulc-mZPp-D6dHQvFNYal52yTh6uZg7Fvody64aZlr4B-UgI5OcxWQDTvqmzqbzBwyqe-OHbUftsagBAIn_QbFDHl56t7Pgp8FV-uvIRQp5v6bQ_693plFXQoHcvH1u0eFwJ6Tu1k0Kx4ASv1AgMCKMDrcH1NTQE0glUmZGkGheMZvzdjZtSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46780b4e7.mp4?token=NBIy1JyDhMk9aPnAuLkJaKGFJoHgX24-Mzo6obUTCRMe8XR6Eq69GLr0t6JKJBNngsxONgDSwjxZCVqXPRC8usV8IKtzIb0SZs9SQuFoATJH2LxsRWgCK_XDK87fuKWlA_vtPc93_4LP187sI6kdLWLclcDPHunedlulc-mZPp-D6dHQvFNYal52yTh6uZg7Fvody64aZlr4B-UgI5OcxWQDTvqmzqbzBwyqe-OHbUftsagBAIn_QbFDHl56t7Pgp8FV-uvIRQp5v6bQ_693plFXQoHcvH1u0eFwJ6Tu1k0Kx4ASv1AgMCKMDrcH1NTQE0glUmZGkGheMZvzdjZtSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت آخرین اردو تیم ملی قبل سربازی =))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107675" target="_blank">📅 13:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107674">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnA-7P1-1unfaJjgTL0k3BKWSuB2FtRkTaUuACEn8Ihi1l0JlNn3UsZsEMU_CDT4y0QvWoEyNCpjmOqs6aHA2qGlb0vr-zb4AajZvQVekEwe6th9jdb422uCZGWHFcobzuL9CBEpo2ietobPEXB7iYKFIG1LRLWIzrmb9wVRdEQraQiuiDJMjhDYnOo_-snv0ZhfmEOHttVh4wBteeuPonVoLH2H4JvJWnmmqtMjMMjnzukxFzusM4zU_b3rL5Pa600iEWi7T8HXPDUuzJ-chX1HdJAZhhwNEH0buFZDeJA7whCI0i1IyIsZDvDpyymnnifDl-y-vmav3vFmHNjVdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
هویلند بازیکن تیم‌ملی دانمارک: شادی دیشبم برای ادای احترام به رونالدو بود و هیچ قصدی برای توهین به بازیکنان و مربی پرتغال نداشتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107674" target="_blank">📅 13:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107673">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/817ab8c188.mp4?token=X0zpMFDs7f-tuPxjVdFwFN37CBbkuA4my10SQhg1VYmmRm-LiWiMNE2wRuyfijZGXmD7_EASPkS-j07RSiHo4dUeoeBLMzvWFixtP4dced9Ws23pMsUHkos5rs5qHItOuVVB3m5BI1-d10urLn78UU2TKgt_PzBTJ_9WcVSmWbqfg_9XDn3qkyvnUXXicq8QEcDr1bCEmx2-fZQ4bZQycgIsZpvUyuv-87QOA7o1oPyhk9NNV825IJDIVuYk6YooZQPF2olzwQh00WKSqNqa2WTrrtvBOJX-DKSYd3kMsOLidCTB0urzKmWpjkmGG10F_V_c6exDjR2zZhkYJHfGZZjNyn7YRXYoAptnnjsPNEma4fwDG7XvM7XWcT1P7-sGsrM1ahUL5AlVgrogZNfe1-Y0T1KMAux8BEFGBV9grDSJCPXSo3C_txemFQHSEj_lBH7wVH-WuX85geXroIgFw7Lw7Elo2UynjNbyDfAHk7jXkLHDvYm0pqtpKMd6sEyPWfCIGjMeJqVdBNd7622FS_69gr8JZJzhdknBujBgvXpVoI_A4HV9cTMZBK7SaOjDGzQc-IFLtwURaUPakBF6GQSd4VyYtUcdVyjq9eaUi8fFy7WeVDa6YE6Pc2QG8moH9hWuWpszRrn4nIgBcBQ2lp6wacOwgBETonvmjTS2_38" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/817ab8c188.mp4?token=X0zpMFDs7f-tuPxjVdFwFN37CBbkuA4my10SQhg1VYmmRm-LiWiMNE2wRuyfijZGXmD7_EASPkS-j07RSiHo4dUeoeBLMzvWFixtP4dced9Ws23pMsUHkos5rs5qHItOuVVB3m5BI1-d10urLn78UU2TKgt_PzBTJ_9WcVSmWbqfg_9XDn3qkyvnUXXicq8QEcDr1bCEmx2-fZQ4bZQycgIsZpvUyuv-87QOA7o1oPyhk9NNV825IJDIVuYk6YooZQPF2olzwQh00WKSqNqa2WTrrtvBOJX-DKSYd3kMsOLidCTB0urzKmWpjkmGG10F_V_c6exDjR2zZhkYJHfGZZjNyn7YRXYoAptnnjsPNEma4fwDG7XvM7XWcT1P7-sGsrM1ahUL5AlVgrogZNfe1-Y0T1KMAux8BEFGBV9grDSJCPXSo3C_txemFQHSEj_lBH7wVH-WuX85geXroIgFw7Lw7Elo2UynjNbyDfAHk7jXkLHDvYm0pqtpKMd6sEyPWfCIGjMeJqVdBNd7622FS_69gr8JZJzhdknBujBgvXpVoI_A4HV9cTMZBK7SaOjDGzQc-IFLtwURaUPakBF6GQSd4VyYtUcdVyjq9eaUi8fFy7WeVDa6YE6Pc2QG8moH9hWuWpszRrn4nIgBcBQ2lp6wacOwgBETonvmjTS2_38" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✔️
نکاتی‌که قبل از خرید آیفون دسته‌دو باید بهش توجه کرد؛ برای رفقاتون حتما بفرستید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107673" target="_blank">📅 13:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107672">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNL7z30y-fiq85k5sPHu9zV6jZAbpGM-Pi0efauFl0GK9BEAOw036WH6Hj_P2yes0r1WiMyiRepehIT9p8WbMtwHW4uUcvAMTkAyc8NYsrw8q40joyZnLHDhlzZXq66EAbkVhWsd4YoWKAG70K3IlYEbIEQxZbtTSYQXYn3sAGHRQip5ogpChfbF2yyvPVZGkRpAN1FeXzNIzwihHcSC95RP2MX9i11Y2eE5BCq4PPmcWSi6dy_5AESQWwpHddDDbkEdy55t3LM5g7DJcluPQasjyemVXj6MGQIvtWN9gnjynO3YnLGTee77Yvx1s5eva3Vga3MciEx4NCoWHUUcsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
😐
استوری همسر رافینیا ستاره بارسا!!!
فوت‌فتیش هستید دیگه چرا علنی میکنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107672" target="_blank">📅 12:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107671">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78eef6851e.mp4?token=qHR2_cn-5-LI1OEVvi2U7kiVZKxkO0N7-GWeeO50TIB591AG1Pf5lqLXCP78Y4D_LKP83arfRg2udW5DvKWm6JmKaUWNBDTbq7Pc0nUqOUbBRtf9l-PpvcJn2yGoPZx4rr471wfCrxWEPG47uty4q3fndliCDqnMg4zeSVYZ1SQYMmOTFiRrwFVTFJvRwbx9exglQW8ytUjAqyng_ZdHD8MBjp6zjlKpZMQkedAsByx1JyRowMS8l2zoO52f4QSYf1cKTRGrhhWzkl_NXuPoYFTnSHYEH1uUMC9ro9P6kRkqVXWFqoMOU7uvXdPAGTuGdI7VDVM69rC-VYF-n3AhFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78eef6851e.mp4?token=qHR2_cn-5-LI1OEVvi2U7kiVZKxkO0N7-GWeeO50TIB591AG1Pf5lqLXCP78Y4D_LKP83arfRg2udW5DvKWm6JmKaUWNBDTbq7Pc0nUqOUbBRtf9l-PpvcJn2yGoPZx4rr471wfCrxWEPG47uty4q3fndliCDqnMg4zeSVYZ1SQYMmOTFiRrwFVTFJvRwbx9exglQW8ytUjAqyng_ZdHD8MBjp6zjlKpZMQkedAsByx1JyRowMS8l2zoO52f4QSYf1cKTRGrhhWzkl_NXuPoYFTnSHYEH1uUMC9ro9P6kRkqVXWFqoMOU7uvXdPAGTuGdI7VDVM69rC-VYF-n3AhFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
‼️
🎙
واکنش متفاوت بازیکنان تیم‌ملی پرتغال به خروج ناگهانی رونالدو از اردوی تیم ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107671" target="_blank">📅 12:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107670">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeVbVTNkj4YogMWOGODX0qMsEETn-ak85zgDg4RFvnVcCYuVi3Jf17KO1XMAD0656GnqLOnedlonlpx6NZ6wtpz4ToSl4GCz0r-mmglF_vbExP6Z0Lv9cZiT5QQKZthOPhuKu21Cm6Az_P4svxcdYYIFXVd-uHLle9ScNTlqOHGhj2JAwMajje2Bco-1lii2lQf3nidR6tLU1l1-K8YwLL8Q8oFYSvN1bc_-80w6IUpcvhJu3WfE1aQa7h5yk9w0YUj8jZR6-9p_3Ri7aZ082WT1V9-9-ncVVtwnvAv53j_449K6T42ZjX7bDZdrZ5gDGacGB3L2RupJn4kirPXDdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇪🇸
تایلر، د کریتور (Tyler, the Creator) هنرمندیه که تصویرش روی پیراهن بارسلونا در ال‌کلاسیکو رفت مقابل رئال مادرید قرار خواهد گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107670" target="_blank">📅 12:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107669">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPQWKXGpOZGGxApKFxPiml9Sm1H-NR48D34iYwlSIZazHDxsX8arXlTm_W2TIDC2QG2Tv4hqfZ00reJVsL094ndz-o_tzOhXGyU3NqJQhgCDEVdce5vgkeFR7X7ic-GvP56TyAo7dI6eHwsL83GjYXnqHUuYWZZPDrpLuyhrM91vIeci7DmueE0veZTLu20JcvfMhc5IyzEPJTzbkdW2K2JfGQdX4AawlSew9HNjqFFi0lIESF3lHfB7I1s2uIW9o-x8V0d42h4goX6Si2Np4I9WXcXVKl1XNrv9jRrQF-zyCa3YNOjtSDw9Ji-MSEsvvPRVACAjl6fxdhorno-K7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇵🇹
خط‌حمله پرتغال بدون حضور رونالدو:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107669" target="_blank">📅 12:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107668">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xnl3mzoypa3arp-RPbe3of6UF_NiqkPaE7hyo_TsiaFOLlURxgoYrEsjNEK90k1rKw2WPBlBk4N7_snOkZEcxCkkZIeGLKJMawlQ893ywwzEm6NnGUb-fXe-psGX56w8yPAhszmhtnXeYb897Up4WoDF1IYa1JUT_sFwgoToS2EVgjXI4dZJQoZPiUwP65YRGB3gE_5-yyqxcBGUSrVXMqktnld6rGyRMQ0o1KuVgwhwlo-hms1X54vJ2_KUgQ2BQWMouIvNB3qCsUr4fXQLEXoxJ7tAQPZAFX0KB1QybqCyMP0N8bjhE-aBizvxSgon9EBVci7w9PJS2Bi5AU2JEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
📊
بر اساس انتخاب  بلچر ریپورت ، لئو مسی بهترین بازیکن تاریخ فوتبال است.
۱.
🇦🇷
لئو مسی
۲.
🇧🇷
پله
۳.
🇦🇷
مارادونا
۴.
🇵🇹
کریستیانو رونالدو
۵.
🇧🇷
رونالدو نازاریو
۶.
🇳🇱
یوهان کرایف
۷.
🇫🇷
زین‌الدین زیدان
۸.
🇧🇷
رونالدینیو
۹.
🇩🇪
فرانتس بکن‌باوئر
۱۰.
🇪🇸
آندرس اینیستا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107668" target="_blank">📅 12:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107667">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721222cb0e.mp4?token=OVLfjw0JAxgsV_Jq_N6EfSoEhIoohRnnrI8-fg-E8FkaBM6iU75yH5_q_3620vH91WUI7zVg-thSGx0xwQ0gL7mw8ZDyk5ij8ZJojDL5GbUxOxVM4JtSIN1oa5OHBhniWx9UXbtsTS-z_zk0g44OhH7POTYSD9A5a6pmiX7zYA9CaqtmMR5mEswxgcURYQ7I-AfzMIZpScqTvdFPrAJJ-WUjmkG3chf2bRjHz3ODaUsWWa9uXjNuwRfHhrqNkSMXb2kOlnRcxZJcTySDy6YRSuaDUolTS2tiR7VmqntyvbV4c7-LcYx-5JNb6G32pAR0cmZnR3c9XYWqGy9-wRvXpS1j4kzog_3X44niDb_-jQn-tdryqRIhXJFoHMzJnzCThQCnghpzRJx7LXVQQL2v7N0d0ieai_5-qvrVN3pmeh-wVSAOw7OJ5bG-4n4eOn7KMrtBtgY8iQMsvcfJ80q6mJkI32jIH7MLLzlS4Bq9dSzogOxATKve03lkzQu0OymHuiXa1ptTmH8eHdX-2daLPnTKNxrX4ErKclMomC8xiXaIfXvw0jIkvxK4AEHmole0E-AreK7Z1PoDDlIis70qCaerCwEEkr0a7CRpmZPDkIScyUb9z7O_KpYGWUzE0trFDXngixIgUCcQovpsp-4rZYi8hqxSKU7N0b29mljd1dc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721222cb0e.mp4?token=OVLfjw0JAxgsV_Jq_N6EfSoEhIoohRnnrI8-fg-E8FkaBM6iU75yH5_q_3620vH91WUI7zVg-thSGx0xwQ0gL7mw8ZDyk5ij8ZJojDL5GbUxOxVM4JtSIN1oa5OHBhniWx9UXbtsTS-z_zk0g44OhH7POTYSD9A5a6pmiX7zYA9CaqtmMR5mEswxgcURYQ7I-AfzMIZpScqTvdFPrAJJ-WUjmkG3chf2bRjHz3ODaUsWWa9uXjNuwRfHhrqNkSMXb2kOlnRcxZJcTySDy6YRSuaDUolTS2tiR7VmqntyvbV4c7-LcYx-5JNb6G32pAR0cmZnR3c9XYWqGy9-wRvXpS1j4kzog_3X44niDb_-jQn-tdryqRIhXJFoHMzJnzCThQCnghpzRJx7LXVQQL2v7N0d0ieai_5-qvrVN3pmeh-wVSAOw7OJ5bG-4n4eOn7KMrtBtgY8iQMsvcfJ80q6mJkI32jIH7MLLzlS4Bq9dSzogOxATKve03lkzQu0OymHuiXa1ptTmH8eHdX-2daLPnTKNxrX4ErKclMomC8xiXaIfXvw0jIkvxK4AEHmole0E-AreK7Z1PoDDlIis70qCaerCwEEkr0a7CRpmZPDkIScyUb9z7O_KpYGWUzE0trFDXngixIgUCcQovpsp-4rZYi8hqxSKU7N0b29mljd1dc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
👀
📊
راز شروع بازی‌های پاری‌سن‌ژرمن چیه؟ این آنالیز بسیار دیدنی رو باهم ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107667" target="_blank">📅 11:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107666">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgga2p3XmdLuE7nv22lazYIKIwmzblJ5TPVBq0PclTABLKpn3w6yyLyaaLE2xFssuJMQMK7xMgBEZpf3sAuhVYiajzH4HnV4Qbbbe_2AqsAk_36Y37rfUK2N6lpfI3_JJTbxhvFNrvaU9TWwH4bz3uWjSJhBHIegOB5sPmZ7FcsGCM6SSmKbWfrW6W_EeqWy7Bwp1WR_4H7lo-zDGuBq-89YX6njuGtIjIqXUbHWcqCLxkrStCPuTKM1ZezyHspGgQQED7T89JHXTz7IQ84EZ-VN4Y4p6wJF8U-GcEaDfqJi3FtCFQi-nJL3gJq3UZVvc9St8aLlxs8SbWTlu4Jjbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
تیم‌ملی والیبال ایران با برتری مقابل پاکستان راهی فینال بازی‌های آسیایی ناگویا شد. برنده چین و ژاپن فردا به مصاف ایران میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107666" target="_blank">📅 11:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107665">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ju9FZKCVgtfIygtpSQoy4lSfbn7GinJszdEXjkrZMcnr8GjlRqR2e-BuzZwznB6lWUmhzOUqT1jm1Bg7ZRPd4fI1Iyo0ML5kNWLng-3Pu9wbrapCt2--usqocHYkA9Y80lTUOKzHepDnNlBqHZpJEMpVlr0DVIqUEhU-0q5FnKPijtTLgsPfzBpIEGIEUHoT1vGpcdNmr9xoqgPw8NtjVmYc2bVoxF_Wbr3iEZ1i_PVpwxoVCUOgIE4pV0KuCGMGaBIDQKx2uO7nI-KNnNf0TtfY_R8XHy0Y7vSrDgoE-vg5XVxzWoNkx-KKCHv3uQ2qcVjKnB6Eq-pVNSHHlO18Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتغال نباید فراموش کنه که رونالدو عامل کسب سه جام ملی مهم برای کشورشون شد:
🇪🇺
یورو
🏆
لیگ‌ملت‌های اروپا 2019
🏆
لیگ‌ملت‌های اروپا 2025
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107665" target="_blank">📅 11:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107662">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkKgg42kKKWzlnltbEh-5tUbNQgVg635jn1VZTLus6PzN7htOd_boABN4P3Pu6yODY79wqpAJYNnh4mkPyGVWAw4aaFO8KqfnoIsoBmNv0POqevH72GJbo-mmoLpZzF6Wmi6Tgn2L8y1I1Kb_FcYOH0ZHfxp06s4epTwisU033znglp3iah4ras_nV6dSfQkRPBrAUdBDBN082IzS9AD4PNK7VVdbAhVioqXNPtfKsnaU-rKUT8ws3Oi3f5bt2Q5q-uLQ_MVvLdpvOX8ligoT3Ixp6okvjXlcV-ZOvr6uVFz5gXQ0qwQDxwwtz4pkMWJLksGYsIz168Lv4WtMKkUag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری یاسر آسانی در کنار وریا غفوری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107662" target="_blank">📅 11:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107661">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/312a800413.mp4?token=azOfWtdV6EjGG4y9sc3g3zQt84EWqc2LMyX1NcbtFmNrjJsoB99WaV5Ac51ah-D4DYoodFRrw9uh-E9cd5g1Az6xLugW_x7UuSjHPpcPGBfAVeNHN12Fc6NrhVKwVTCKLu2kgElff30W9O-ngBrpdKheaav06-li1WqW0-TAusEK4FfSJX7kW8hXixflQhrjEr320IIsps8qYmeQkMNbqaKts4lpm2GpkAxbzauOjvKO6zIsplHvRrkkXznnrwwxIiYO8z9X7nsKfkoLMp78jK7i6JyrzHqPogQB79H4CHAljNXZjUIB3H2lOHv5vEZFHz-4qY6Bo4IQk6wlaGeoZX-fKrz2v-qZcynQaq6ve4HbwwEWtFm_rnkHggRdbr8jrp5QmFhNZLw3SHYjecb5N34X1nRaL1k9XqPktyxKKsw3Tfw5I0aUxUNC30M4ivmuishcn_JxQ3dbtxOhgB37bSRU4EUivHFkCiu9KEA9muo9LB7361UVydZ1-l-UL0BvSybdECtoTcjX84bXhfz789ViGXFlprZpdb1q2Z0hq_Q2bSd46MSGkmdFdf-dx0wHX81W6_m5Rm24x_w860ux3UE51lNNQoYCQ8kK44nda8Cc3mq6KOwdG8QSbQkkcPGXlHv6oGSkCBCm0nOHJhBAK0hfDFf1Poc-9-a1Iuj6nmk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/312a800413.mp4?token=azOfWtdV6EjGG4y9sc3g3zQt84EWqc2LMyX1NcbtFmNrjJsoB99WaV5Ac51ah-D4DYoodFRrw9uh-E9cd5g1Az6xLugW_x7UuSjHPpcPGBfAVeNHN12Fc6NrhVKwVTCKLu2kgElff30W9O-ngBrpdKheaav06-li1WqW0-TAusEK4FfSJX7kW8hXixflQhrjEr320IIsps8qYmeQkMNbqaKts4lpm2GpkAxbzauOjvKO6zIsplHvRrkkXznnrwwxIiYO8z9X7nsKfkoLMp78jK7i6JyrzHqPogQB79H4CHAljNXZjUIB3H2lOHv5vEZFHz-4qY6Bo4IQk6wlaGeoZX-fKrz2v-qZcynQaq6ve4HbwwEWtFm_rnkHggRdbr8jrp5QmFhNZLw3SHYjecb5N34X1nRaL1k9XqPktyxKKsw3Tfw5I0aUxUNC30M4ivmuishcn_JxQ3dbtxOhgB37bSRU4EUivHFkCiu9KEA9muo9LB7361UVydZ1-l-UL0BvSybdECtoTcjX84bXhfz789ViGXFlprZpdb1q2Z0hq_Q2bSd46MSGkmdFdf-dx0wHX81W6_m5Rm24x_w860ux3UE51lNNQoYCQ8kK44nda8Cc3mq6KOwdG8QSbQkkcPGXlHv6oGSkCBCm0nOHJhBAK0hfDFf1Poc-9-a1Iuj6nmk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
عشق به مارادونا، با توصیف آقای گزارشگر
🎙
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107661" target="_blank">📅 10:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107660">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/74ab0dda5d.mp4?token=t6zsaTzoBzlE2-LziEwfd-BSKH-EekuhtLe305YU-ndyQz_Ssi_C5MmKlDigie49nHDdvdn1z1NkFhib1JAmwPzdJLcSOJYvkZ9-j-fTd371t1fToPE0auq1GQ8IpjDkhnki-iCTA4RpCKxncLNEGi7sFALn8Zcn_IOUrjcqDr91F99p72_Xh1hfVN9Q74acbX9r8LCHvWT8IC_u2fBF5Yn4oo-9xogUothJEiaShvzttfcLxzHv7MUoP9VBXSdOgxa89LjPjTRhrueCbxkTGpvTaAMmFJV3vAxYzI-Csg0z31DB88skEsdB8OMINcMxHPP0HXxgNDmDHU289rcHdg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/74ab0dda5d.mp4?token=t6zsaTzoBzlE2-LziEwfd-BSKH-EekuhtLe305YU-ndyQz_Ssi_C5MmKlDigie49nHDdvdn1z1NkFhib1JAmwPzdJLcSOJYvkZ9-j-fTd371t1fToPE0auq1GQ8IpjDkhnki-iCTA4RpCKxncLNEGi7sFALn8Zcn_IOUrjcqDr91F99p72_Xh1hfVN9Q74acbX9r8LCHvWT8IC_u2fBF5Yn4oo-9xogUothJEiaShvzttfcLxzHv7MUoP9VBXSdOgxa89LjPjTRhrueCbxkTGpvTaAMmFJV3vAxYzI-Csg0z31DB88skEsdB8OMINcMxHPP0HXxgNDmDHU289rcHdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اون بعضیایی که میگن از صفر شروع کردیم ولی خب ؛ صفرِ شما ها، صدِ خیلیاس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107660" target="_blank">📅 10:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107659">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jW_gv0UDUCyZCaKDrO0fc9Qx4tI6dfMSOJMSzt_xJpNGb2iYi3zmvAA3KtamfSnmQQpQOLfdfYqwATjMbtW9NYyIgM0xX4aaAGG1MaKE8_FVXAqsVnwxXhz1oTmEx4vstK7xrg3Q6G-TrKGs-u57247dfzKNCegoc-9QTXwU5eZAZQ-yLmobkaxK3E-yRlGmwI_1LJKoVJgsuMNtVyOpD2MBxJ5-51E6T1eBBRRvko6mJkFLZovXPr3YHVlZy5Bl7k7kibq5okEvoZJnn8cu1Urjx3eGYC_QMJ3GKtIuUXB-FdTTXTn6EJwzmXy4IiPiSJUMSvxvh3g9ap28LFsdZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏟
بزرگترین ورزشگاه‌های تیم‌های ملی در جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107659" target="_blank">📅 09:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107658">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XA83MWlH9Ydm6vw6sgXnsdBtm8YT_ci8z0chaKcMKC_9Gukulp6Ax_P70ETFCGZUXFNY1gjJ6zm05u3VKkL-cp59C69wnHTuyWFiu7cCHXxDr0qJKUy5Lq6KWGVTKhRtu5f7z1id8qLI0gAmx7WaWMsAWMA0ajHwj6Lul7ajd2VAZo1O7Y-b6h4aImwzSBW07JXXYBAMHZ7iGAcndRT6zmFgt8Ju7m1Vu-y3T48vTpOWE-617BkF1mqI7MmepfAi7hD5Txo-lsi4U8rk4-n4MKFqb85IDwPVMepGFqC74xu-EDPCAAol6ZwZpeiixJMzisKXrMFRUJTZhKnXHefN0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🐐
🔥
آمار و عملکرد مسی در تاریخ کریر فوتبالش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107658" target="_blank">📅 09:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107657">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85455aa172.mp4?token=D8rmm8ktWsm-Vq5hslzIFUQmFae3PP1M9DXD715m34iO3q22SNdWRI-Egb9rTJVjHXr5Nlo8t_1UKPNS3cjCVpsz_FetFAx8ZzuMB6pRd4SGOqeoaO3sArUn7rxiaf3c6E_a04ljvBeCYk8QA1VSN4GLEe1PkB1NHKgklY1UpkCDocgoFYwRpgw3q3iHu4a887lzwkgf4PEM_8cfBL3rJEqGHyA830Jq5bPkpZXh4ZCoe3cl35_y0IS3hHviGaUaDqXrwih_yOnr_AaYsNcTm8j73DjR-kBmLPJwbQ8F6ocDmAVo_r4WGJofVY7qu2FzMLIMOrvSCiNW4O07sfurF62cWXt_585uNhZ__Ka91JFL_M0MSkUS_YwCe75Fw1ATnD8L73QPekSiHdA_h-W6EV4BJCFQpyVEXWv9Z8eS1kS8VaUIbhceXzh7bNJUFkyT3UR-0QBhCl7SO7LkTwDN5KC71CF7Es-9ruNgZtJ6dUIhMW06QcI5i24NI34XXWSW8fLypJ-p7AUyH3wSRxJ1_Pspo5RVUHFJ_0BfCHHNxHkVEEnezlUKeUSkTqzAZX5ET-q8m6_3SKd4UTAkZd16YKIezlqw50XgKUJQmEDJtxY2YunpkIe3TdDWQKDozRphTw1MPorFBooZai7rUNVTW8ojO2kMGMju1KmRpXMz3as" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85455aa172.mp4?token=D8rmm8ktWsm-Vq5hslzIFUQmFae3PP1M9DXD715m34iO3q22SNdWRI-Egb9rTJVjHXr5Nlo8t_1UKPNS3cjCVpsz_FetFAx8ZzuMB6pRd4SGOqeoaO3sArUn7rxiaf3c6E_a04ljvBeCYk8QA1VSN4GLEe1PkB1NHKgklY1UpkCDocgoFYwRpgw3q3iHu4a887lzwkgf4PEM_8cfBL3rJEqGHyA830Jq5bPkpZXh4ZCoe3cl35_y0IS3hHviGaUaDqXrwih_yOnr_AaYsNcTm8j73DjR-kBmLPJwbQ8F6ocDmAVo_r4WGJofVY7qu2FzMLIMOrvSCiNW4O07sfurF62cWXt_585uNhZ__Ka91JFL_M0MSkUS_YwCe75Fw1ATnD8L73QPekSiHdA_h-W6EV4BJCFQpyVEXWv9Z8eS1kS8VaUIbhceXzh7bNJUFkyT3UR-0QBhCl7SO7LkTwDN5KC71CF7Es-9ruNgZtJ6dUIhMW06QcI5i24NI34XXWSW8fLypJ-p7AUyH3wSRxJ1_Pspo5RVUHFJ_0BfCHHNxHkVEEnezlUKeUSkTqzAZX5ET-q8m6_3SKd4UTAkZd16YKIezlqw50XgKUJQmEDJtxY2YunpkIe3TdDWQKDozRphTw1MPorFBooZai7rUNVTW8ojO2kMGMju1KmRpXMz3as" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
ابوطالب آماده ورود به فساد فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107657" target="_blank">📅 09:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107654">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107654" target="_blank">📅 01:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107653">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5WOhk2pAl5913VdC397_lLnGKa4uOrMlYJ-SpIk9Aro7xDQRWCKfEuyg5V78nrYnc8XIaY8dsaeoKVNjcT_pNstsPUxXIcJxcgBQuHSy_kHTBjklqwuxeuEnOpuL7lBvGWfXmsTz-xZsRo0XnB_Lzc-NeXlHUkfXz13jzUjB1aQI0jJqjqgo5PcVI0aamQ5ZGED4YW_re67J_ZLJJOzzLq5uqOd6hWdaqwT3F5Btz-MG9pMCApymXjn3XmuBDNb0xMT3UisQthCCM8-lPA6r_bCePWgXtGsxPmjI_LeL4zcyYbt6RfFGnESbYnpP8cqgUJPEMQXu4l8bz_rqmp3OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
کنایه ژسوس به رونالدو: خوشحالم که گروهی از بازیکنان را دارم که به ایده‌هایم احترام می‌گذارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107653" target="_blank">📅 00:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107652">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Glon90hX1_TgRIEAHF1onsaCEAeAaSbBho8Jd6OR71qkLAiC91mc7T3gMTakshThC3ukobdgKgP8_3VdLdz6FlgJ4LcvSd-Ug3KgbAAMBwGEOyBDAi1DR_ee29ikZp3G0dGLV-MXe5ceOnYZECQBYz6EzdJvRXK-ch-TvOfUI574YgiZAP3MWuQN72HM3bXybsZIGYyGN_x0iV58O0Ieuce6uBAAOULeTw_TueTRdsQduuhoZS8VY6rPFIQcEBe9wqVbUDBC3pKnAQu0uikX-iwtw7IKCxAIosTcWHbU-mNRPThN_9bOulgfucH02IhgDBb8oPJFVexCcX_fVer13g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
کنایه ژسوس به رونالدو: خوشحالم که گروهی از بازیکنان را دارم که به ایده‌هایم احترام می‌گذارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107652" target="_blank">📅 00:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107651">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-dVSyh2ryiqvUdiOk-YSDtnleM7ZXcnND045vSk0hW7CGxoMyEijTbdpGNgFXySMNoVxA1trE7skZlLvMnLf0nMLIJObeSBAjlK3VDGv1--jFqcWy9BImrz71S_XnkKyzwOWwlmbJH-EKf_1kUU1zkmYv6jrrIh8NrgBjiAysNU6laoOMWFNXX9lmjszskLn0txrbAdQ6C5gdfwS1sBi3PrZBE4vhkhFFYJqYZMI8L9uIgmv3dqNqcg5NtD9CxiGX4xaKH7wOmwkJkXZMHHx3SHhvlvQQ0UPnyDsnAGkX7ZPihDgaQYGnCFFTv9gCbX2Ctx64gjzMJ6CRt_vnMD8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
عملکرد فِلیکس تحت رهبری خورخه ژسوس در تیم النصر و تیم ملی پرتغال:
🏟️
50 مسابقه.
⚽️
47 مشارکت.
⚽️
29 گل.
⚽️
18 پاس گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107651" target="_blank">📅 00:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107650">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44b6b9a87b.mp4?token=VFsT5q4d0K4ZTSv7EVWVBROiBf4tCzjgyW9xpUPcrkQYJtdlTuesn-UTyeERRdrbw4QBXp5PnvQPhXTbGuBNafxGkKqHMI8w0tKveXAKmno15uTWaBtUX-a0HtDAbtmOb0tYar4SRf6f52c7qkKjgfw-E8C0l0thJtyUVevinHLHsHi9fr3XmY-_VcxMMymkJ8gsljY39J7kyiixcTqlfy77ZEjBf6RwUW_4wjq21Wc_YnUq4JEot0ihmZQCRu6TSHHZtC5Xbenr3PuJYoefd8ahatlpw3yxZmHyV2PYicj6SA_HEX_zWH5X7_uqfYZ4aOJ7IsRd4KCB_3IAy6R0ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44b6b9a87b.mp4?token=VFsT5q4d0K4ZTSv7EVWVBROiBf4tCzjgyW9xpUPcrkQYJtdlTuesn-UTyeERRdrbw4QBXp5PnvQPhXTbGuBNafxGkKqHMI8w0tKveXAKmno15uTWaBtUX-a0HtDAbtmOb0tYar4SRf6f52c7qkKjgfw-E8C0l0thJtyUVevinHLHsHi9fr3XmY-_VcxMMymkJ8gsljY39J7kyiixcTqlfy77ZEjBf6RwUW_4wjq21Wc_YnUq4JEot0ihmZQCRu6TSHHZtC5Xbenr3PuJYoefd8ahatlpw3yxZmHyV2PYicj6SA_HEX_zWH5X7_uqfYZ4aOJ7IsRd4KCB_3IAy6R0ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
گل‌چهارم پرتغال به دانمارک توسط ژائو فلیکس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107650" target="_blank">📅 00:05 · 10 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
