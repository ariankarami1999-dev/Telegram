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
<img src="https://cdn4.telesco.pe/file/f5CneY1ZmHC-EdsPeX0rWrP_ycM56U6emOhgrWJ81iyiKfpvkXhTPW5AssA0okJxzriOgEhJa8_Q9ydaKXI0Gvla0k9UZUpd4lKqf470xkmVXNJqsVCze1jlmzBfT4obc3T04OFbsEhkUFTbLbHfAD3AHLWqTqa7KbIqAbsAYaFUTcLEWqdWWElMEkT-aMKxK_QkLiP9Oq3Q_qaJCgAhZs1kMVULObJofL7djf3-N8fEEqIsbFIzrkESQhw4DhRwRVDJLvQfDcEJ2MPKFDYlFIdKNQjZFZmc2UJToGPON2biXS31jFbk48Eccy9cHsgfRXTAQiQGFwHcBz1RM9gzXw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 260K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 18:30:12</div>
<hr>

<div class="tg-post" id="msg-11292">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وزیر نیروهای مسلح فرانسه: ناو هواپیمابر «شارل دوگل» در دریای عرب مستقر شده و ماموریت آن «دفاعی» است.
@withyashar</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/withyashar/11292" target="_blank">📅 18:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11291">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e37fa8adaa.mp4?token=MNkJjvAUdobrPP2sa3GSg9TWKz9EhmlKLYqeKBbJZ2-sHCdcBDvwKdfLcIxQosFzUXnHg-fmQVnHsyMVgj2fGtl2Ib6dgB6wNWJ9dunMXPHlaepSuniLq2kW1_4CvTxeSMWbRaqzLb4v1iidC_wVs-eaO5JpdNhTwS7KDGUe1YP6AWRQnDYZMVDr0ZzN_tzI1wKVWhAjlBHEXgVlcn75V8K1ZazmRpSHjQscJ8dLc0EAtFyY3yebniLz5xAEMjW2GbPdpg8bGtpwomkajF4y55vChx_OWxbpN28ISQIVUUq1U_MMnp9Cjl5h6U3GU7j56CGqD2n4R4s01ij9xKSvwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e37fa8adaa.mp4?token=MNkJjvAUdobrPP2sa3GSg9TWKz9EhmlKLYqeKBbJZ2-sHCdcBDvwKdfLcIxQosFzUXnHg-fmQVnHsyMVgj2fGtl2Ib6dgB6wNWJ9dunMXPHlaepSuniLq2kW1_4CvTxeSMWbRaqzLb4v1iidC_wVs-eaO5JpdNhTwS7KDGUe1YP6AWRQnDYZMVDr0ZzN_tzI1wKVWhAjlBHEXgVlcn75V8K1ZazmRpSHjQscJ8dLc0EAtFyY3yebniLz5xAEMjW2GbPdpg8bGtpwomkajF4y55vChx_OWxbpN28ISQIVUUq1U_MMnp9Cjl5h6U3GU7j56CGqD2n4R4s01ij9xKSvwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: دیروز از دریادار کوپر درباره حمله به مدرسه دخترانه(میناب)در روز اول جنگ سؤال شد.
ترامپ:  منظورتون همون حمله اولیه‌ست؟ اون موضوع هنوز تحت تحقیق قرار داره.
خبرنگار: می‌تونید تأیید کنید که موشک آمریکایی بوده؟
ترامپ: شما از کدوم رسانه‌ای هستید؟
خبرنگار: بی‌بی‌سی.
ترامپ: بی‌بی‌سی فیکه با من حرف نزن.
@withyashar</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/withyashar/11291" target="_blank">📅 16:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11290">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc3a3a9b4.mp4?token=nwLzFS6H-Lf9MOGh_FrJ6nL0vg6Qn2mySRouTpx0NTdWXJ7Ex4Wlq4kJBxGwnddJjtSAUp_2TQ2M_bmf9yHzq9H4xCOJ7C4Sqy9eQSRtEyEXQP7kfHN21UBFn5cDzCJijj56824oX7mCl4wtzAMI8p2YGc6gJlNSgChTnvqvZMPCT92edo5re0AVRGu9Jc8lnK3vYSbMkAN7fb7ZXiBD0YDaPiWsETg31wsBTmyl--cOF2niWW53Vy20hMseWbziDekUuanuFt9IgYsDMMpgTQDe4gTysgoQI69wCun5vQ6gHCNWJfdjscB1pUrBS_M4_EpM_JB9ILpUcZx1ttI8Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc3a3a9b4.mp4?token=nwLzFS6H-Lf9MOGh_FrJ6nL0vg6Qn2mySRouTpx0NTdWXJ7Ex4Wlq4kJBxGwnddJjtSAUp_2TQ2M_bmf9yHzq9H4xCOJ7C4Sqy9eQSRtEyEXQP7kfHN21UBFn5cDzCJijj56824oX7mCl4wtzAMI8p2YGc6gJlNSgChTnvqvZMPCT92edo5re0AVRGu9Jc8lnK3vYSbMkAN7fb7ZXiBD0YDaPiWsETg31wsBTmyl--cOF2niWW53Vy20hMseWbziDekUuanuFt9IgYsDMMpgTQDe4gTysgoQI69wCun5vQ6gHCNWJfdjscB1pUrBS_M4_EpM_JB9ILpUcZx1ttI8Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥲
@withyashar</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/withyashar/11290" target="_blank">📅 15:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11289">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/238609fcd8.mp4?token=XMi7pehevpegMHZSP6wTfhAon1qrjk6n_1Ktfg-BV_uLNuD4C6GQYF93Uv571ltK4ZnFUJ3f4uAu2LbA90238Wc9R6YwAZwYf6Ox8jfNEkPmFqTuVhAGCgISF7nHDOPMbN47ZwwCVJ06T4pV5p4asO8uze63UQ3-usOc12KowbEZHUBDdWVtQy8fVUp-tZqxFAjWc-skIMe96VgGriIdqKUtJCyoqvVGLYBtRee-lyojJIsnCSnJPBmUadpGW9NXspm612ql_fFZykNl30H5eHmDtxYbKnwmcrc9xoY9ajgBoQLZtbFQgmftQ3cZzwDE4i6PRm9UCNX1tZVIFlSlnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/238609fcd8.mp4?token=XMi7pehevpegMHZSP6wTfhAon1qrjk6n_1Ktfg-BV_uLNuD4C6GQYF93Uv571ltK4ZnFUJ3f4uAu2LbA90238Wc9R6YwAZwYf6Ox8jfNEkPmFqTuVhAGCgISF7nHDOPMbN47ZwwCVJ06T4pV5p4asO8uze63UQ3-usOc12KowbEZHUBDdWVtQy8fVUp-tZqxFAjWc-skIMe96VgGriIdqKUtJCyoqvVGLYBtRee-lyojJIsnCSnJPBmUadpGW9NXspm612ql_fFZykNl30H5eHmDtxYbKnwmcrc9xoY9ajgBoQLZtbFQgmftQ3cZzwDE4i6PRm9UCNX1tZVIFlSlnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز 25 اردیبهشت روز پاسداشت زبان فارسی و بزرگداشت فردوسیه
@withyashar</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/withyashar/11289" target="_blank">📅 15:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11288">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4486529b5a.mp4?token=uy2xKt02W_WhIxBpmPwNcrKPHjlpkTCk-x5hq8MVrmgYW-h_GguGKkVZ5v2g7i_9mV0celcgFUX6ILMSkex4EtpItTwuf_tKDT4wbIKunF6mBBKKJeXc6xHik4H-PRTyeaO7kncPSmlx86I3JCtLyeVp_fEeN7C1dW_yUvZjN3-6CXcWsHKiLFF5Dx0VTnpspeWrDosCqHX4V8IZgEZbVj8hNP20rtSJI80fCq4CAhr3fU2eDtvsGciH_am6X6GYwBzyFFq8wW9BDw5HOyKDyRewfWqu91Lwxxbbdrf6O62U9L8xDgZVJSiaVZOBZAABuFGQ21mTeaARJDCbYl-ZsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4486529b5a.mp4?token=uy2xKt02W_WhIxBpmPwNcrKPHjlpkTCk-x5hq8MVrmgYW-h_GguGKkVZ5v2g7i_9mV0celcgFUX6ILMSkex4EtpItTwuf_tKDT4wbIKunF6mBBKKJeXc6xHik4H-PRTyeaO7kncPSmlx86I3JCtLyeVp_fEeN7C1dW_yUvZjN3-6CXcWsHKiLFF5Dx0VTnpspeWrDosCqHX4V8IZgEZbVj8hNP20rtSJI80fCq4CAhr3fU2eDtvsGciH_am6X6GYwBzyFFq8wW9BDw5HOyKDyRewfWqu91Lwxxbbdrf6O62U9L8xDgZVJSiaVZOBZAABuFGQ21mTeaARJDCbYl-ZsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روانه شدن نفت در سواحل جزایر خلیج فارس جمهموری اسلامی داره نفتو تو دریا میریزه و جان موجودات دریایی و زیست بوم ها رو به خطر انداخته
@withyashar</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/withyashar/11288" target="_blank">📅 15:10 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11287">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27bba1486b.mp4?token=pLnDaFr-3feCYO_irtXUm_BfPj2T6Ymm1O4rAuCttedNCHqFzYY0-Qi8OgjYjNTEfHSZm1V-mXYEN_y0PPnJDGUJUcjihgIKplJiryydreIWQ5eeVqpTGqGC-dBnq7q_-6N3TK0jNcRxWiWTZujMr8DOs1Do9gWGbvzByYeM2gh1dY99KEiCw052G5l-v5xYN9c-ysF3IkLCc7Bdqsduf6zyFZdQTR2Qv4H7dg059jADLTsJwqP5Z_z3zVQPBroqDJDZWhCNinBUMsIT3dcxE8P7yIUUyxfqgLflP67fnThxhDcpNUVxxjL65O9ctdWQcy_1astjEBvWxoHnPh-SIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27bba1486b.mp4?token=pLnDaFr-3feCYO_irtXUm_BfPj2T6Ymm1O4rAuCttedNCHqFzYY0-Qi8OgjYjNTEfHSZm1V-mXYEN_y0PPnJDGUJUcjihgIKplJiryydreIWQ5eeVqpTGqGC-dBnq7q_-6N3TK0jNcRxWiWTZujMr8DOs1Do9gWGbvzByYeM2gh1dY99KEiCw052G5l-v5xYN9c-ysF3IkLCc7Bdqsduf6zyFZdQTR2Qv4H7dg059jADLTsJwqP5Z_z3zVQPBroqDJDZWhCNinBUMsIT3dcxE8P7yIUUyxfqgLflP67fnThxhDcpNUVxxjL65O9ctdWQcy_1astjEBvWxoHnPh-SIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صداسیما : نتانیاهو نه خسته شده نه عقب میخواد بکشه بنظرم واقعا مَرده واقعا مَرده و میخواد ایرانو
از 100 درصد به 20 درصد برسونه
همین الانم اماده ترین عنصر برای
حمله به ایران؛ اسرائیله
نتانیاهو نه کم آورده نه علائمی از خستگی داره نه پشیمانه
@withyashar</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/withyashar/11287" target="_blank">📅 14:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11286">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ به فاکس‌نیوز: ما می‌توانستیم پل‌ها و شبکه‌های برق ایران را نابود کنیم و می‌توانیم ظرف دو روز همه چیز را در آنجا از بین ببریم.
@withyashar</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/withyashar/11286" target="_blank">📅 14:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11285">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ به فاکس‌نیوز : ما ارتش ایران را نابود کرده‌ایم و شاید باید یک پاکسازی سبک انجام دهیم.
میتوانیم نیروگاه‌های ایران را تنها در دو روز از بین ببریم
اگر ایران اورانیوم های غنی شده خودش رو تحویل نده وارد ایران میشیم
@withyashar</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/withyashar/11285" target="_blank">📅 14:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11284">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/withyashar/11284" target="_blank">📅 14:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11283">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromJvd</strong></div>
<div class="tg-text">مارو به قاهره میبره؟
خب پس بذار هرچی میخواد بگه</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/withyashar/11283" target="_blank">📅 14:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11282">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ به فاکس‌نیوز:
پیشنهاد ایرانیا که برام رسید همون‌ جمله ی اول متنشونو که خوندم برام قابل قبول نبود و سریع ردش کردم
@withyashar</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/withyashar/11282" target="_blank">📅 14:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11281">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9df234526d.mp4?token=O_2xlkyPdLHSXgujYu1iKbtIgjz7DzMuOb-N6mir_NfdfjJbMrs8eq1EQ5LWAda963P6OJBDK_czB-Rd_fafLMYvk8HHi7tdXfRnS753Ys26FU_kivS0Yf8KsZ100atpBP-GoZia6-rjQYtP_xgjoiIiKdpzw6hLSQuIzGFJvVY_Dqh-axI6NX2r1_r8_DbEepXgfkKnGJvWnoc5G4x5THc_Yuvk-IvOpQxYm700VqqEE-BvqN_jm3mxBpObf-K1ZWBeXuoZrDpqwzz3GbdpuAvqQNwnNVj4oX_9_9E41WPrVbv7LoOw_sDLNXcXClrGPlhdTipOEH2dg_aCnHRqpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9df234526d.mp4?token=O_2xlkyPdLHSXgujYu1iKbtIgjz7DzMuOb-N6mir_NfdfjJbMrs8eq1EQ5LWAda963P6OJBDK_czB-Rd_fafLMYvk8HHi7tdXfRnS753Ys26FU_kivS0Yf8KsZ100atpBP-GoZia6-rjQYtP_xgjoiIiKdpzw6hLSQuIzGFJvVY_Dqh-axI6NX2r1_r8_DbEepXgfkKnGJvWnoc5G4x5THc_Yuvk-IvOpQxYm700VqqEE-BvqN_jm3mxBpObf-K1ZWBeXuoZrDpqwzz3GbdpuAvqQNwnNVj4oX_9_9E41WPrVbv7LoOw_sDLNXcXClrGPlhdTipOEH2dg_aCnHRqpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ وسط پرواز به فاکس نیوز اعلام کرد که ممکن است توقف ۲۰ سالهٔ فعالیت هسته‌ای ایران را بپذیرد.
ترامپ:“بیست سال کافی است. اما میزان تضمینی که از طرف آن‌ها می‌گیریم… باید واقعاً یک بیست سالِ واقعی باشد.”»
@withyashar</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/withyashar/11281" target="_blank">📅 14:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11280">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ وسط‌ پرواز به فاکس‌نیوز : «من دیگر خیلی بیشتر از این صبر نخواهم کرد. آنها باید توافق را امضا کنند.»
«مواد هسته‌ای» ایران، ممکنه به چین یا آمریکا تحویل داده شه!
@withyashar</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/withyashar/11280" target="_blank">📅 14:34 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11279">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ وسط پرواز به فاکس نیوز :
اما در نهایت فکر می‌کنم الان آخرین چیزی که دنیا نیاز دارد جنگ است، مخصوصاً جنگی که هزاران کیلومتر دورتر است.
شی درباره مسائل مختلفی مثل ، حملات سایبری و جاسوسی صحبت کرد. گفت هم آن‌ها جاسوسی می‌کنند و هم ما. این یک واقعیت است و همه این کار را انجام می‌دهند، اما معمولاً درباره‌اش صحبت نمی‌شود.
او گفت آمریکا در چین جاسوسی می‌کند. من گفتم ما هم همین کار را انجام می‌دهیم. این یک واقعیت است و مسئله‌ای است که همه طرف‌ها درگیر آن هستند
@withyashar</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/withyashar/11279" target="_blank">📅 14:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11278">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ وسط پرواز به فاکس نیوز :
شین گفت برخورد شما قوی‌تر از قبل بوده، چون ما با انها(حکومت ایران) رابطه داریم و ما درباره این موضوع صحبت کردیم. من گفتم این مثل جنگ است و حق با من بود. موضوع قدرت بود و همه با آن درگیر شدیم. این موضوع روی رابطه ما تأثیر گذاشت، اما قبل و بعد از آن رابطه خوبی داشتیم و الان هم رابطه‌مان قوی است. حتی به جایی رفتم که او زندگی می‌کند، که اتفاق نادری است. با هم ناهار خوردیم و درک خوبی بین ما وجود دارد. فکر می‌کنم او معتقد است اتفاقات مثبتی بین دو کشور در حال رخ دادن است
@withyashar</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/withyashar/11278" target="_blank">📅 14:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11277">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ وسط پرواز به فاکس نیوز :
نیویورک تایمز هم گزارش‌هایی داده بود درباره تحریم شرکت‌های چینی که نفت ایران می‌خرند. درباره آن صحبت کردیم و بعداً هم صحبت خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/withyashar/11277" target="_blank">📅 14:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11276">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ وسط پرواز به فاکس نیوز : شین گفته جنگ باید متوقف شود. من چنین حرفی نمی‌زنم. فکر می‌کنم او آدم خوبی است، اما از بعضی حرف‌هایش خوشم نیامد. مثلاً گفته کشتی‌ها باید بعد از پایان کار نفت متوقف شوند. ما هم از نظر نظامی تقریباً کار را تمام کرده‌ایم، اما هنوز کامل نشده است.
ما حدود ۷۰ تا ۷۵ درصد کار را انجام داده‌ایم، نه همه‌اش را.
برمی‌گردیم و بقیه را هم تمام می‌کنیم
. بعضی بخش‌ها هنوز باقی مانده است. توان موشکی و پرتابگرهای موشک هنوز به طور کامل از بین نرفته‌اند، هرچند گفته می‌شود حدود ۸۰ درصد آن‌ها نابود شده است. تولید موشک هم بیشتر آن از بین رفته است
@withyashar</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/withyashar/11276" target="_blank">📅 14:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11275">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/withyashar/11275" target="_blank">📅 13:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11274">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خبرنگار الجزیره:
تهران به‌طور رسمی پاسخ واشنگتن به پیشنهاد خود را دریافت کرده و ایالات متحده تمامی شروط ایران رو رد کرده.
@withyashar</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/withyashar/11274" target="_blank">📅 12:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11273">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">😂
😂
🙌🏾
@withyashar</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/withyashar/11273" target="_blank">📅 12:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11272">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ در تروث : پژوهشگر چینی به CNN گفت که به نشست ترامپ و شی نمره «۹.۹۹ از ۱۰» می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/withyashar/11272" target="_blank">📅 12:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11271">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEONf_M-WuYrVL32B2UDArWZOalfqpKb0EAS42fXbAUbCkW9jBq07W6XoTLIR6QiTXMSDmVG9mZOp9aBJDg7RL4elZQpoz5wu4G9YT24ClwN3ycN-8hWhfY_B8hA5Pr6SBHl_anrg8RfVRx2m_QQnjtrNyEtRMXXBw28UB-A2-HTjbbyhoi9i_bIbH4Of08x0ojYMFZyo02J58zWj7y094Ovt3n2gh9wOTIEMmCid_1tyjOun7o2_GUJVfSsaCyUEFkwmNILGTXwXVAlnBf5eAsAeXDbQPNdhH9AoNrh8iW6V1qq2-F9yyfI72BKePKzjQQ3T64Mx-nsSqsLuVV0vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد قنطاری، کاردار جدید سوریه در واشنگتن دی سی
😬
🍔
@withyashar</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/withyashar/11271" target="_blank">📅 12:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11270">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">@withyashar
part3</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/withyashar/11270" target="_blank">📅 12:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11269">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veQjoz8CJqAJQJO0lrU12Ge8qWVEheeEUhBKU3Sswi7qBt8CiRWlvcOiYrQgWB_4Z8Tbt5k97wkysAVgzs1dtLOaJ4rUwWav3nqh4KIoNTdI8zsBVFa-h4A8P1QwnJH7_tgB7ekhQei9-dFOwTrTZ0I1SSqRriH-z00SgldeHY3XVAU-eZ9gJMchW4afRtwLuGioyp5tY29iY_5_2yT5QNYB3ypVfjSVtI0IRQ05bG6iA6MTqTuXRkVO9-6AODLjd-5aBK0dj_eZevNmwUkj48_rLLRmnqgq6HaAtsN5CkhJZqexk97dTa6LrQB1Pi0m-vqsRhDcykVgvgfzUFcJ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
🙌🏾
@withyashar</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/withyashar/11269" target="_blank">📅 12:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11268">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">هم‌اکنون حمله سنگین جمهوری اسلامی به مقر گروه های مخالف در عراق
@withyashar</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/withyashar/11268" target="_blank">📅 11:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11267">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">طبق گزارش روزنامه «ساوت چاینا مورنینگ پست» و بازنشر آن توسط «بلومبرگ»، انتظار می‌رود «ولادیمیر پوتین» در حدود ۲۰ مه به «پکن» سفر کند؛ تنها حدود ۵ روز پس از دیدار «شی جین‌پینگ» و «دونالد ترامپ» در پکن.
رسانه‌ها می‌گویند این سفر احتمالاً فقط یک روز طول می‌کشد و بیشتر در قالب یک دیدار کاری و هماهنگی سیاسی انجام می‌شود. همچنین برخلاف سفر ترامپ، ظاهراً خبری از تشریفات بزرگ، رژه رسمی یا استقبال بسیار گسترده نخواهد بود و این سفر در سطحی ساده‌تر و کم‌نمایش‌تر برگزار می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/withyashar/11267" target="_blank">📅 11:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11266">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">@withyashar
part2</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/withyashar/11266" target="_blank">📅 11:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11265">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ در تروث : «وقتی رئیس‌جمهور شی با بیانی بسیار سنجیده از ایالات متحده به‌عنوان کشوری که شاید در حال افول باشد یاد کرد، منظور او آسیب عظیمی بود که ما در چهار سال دوران جو بایدنِ خواب‌آلود و دولت بایدن متحمل شدیم؛ و در این مورد، او صددرصد درست می‌گفت.  کشور…</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/withyashar/11265" target="_blank">📅 11:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11264">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">@withyashar
part1</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/withyashar/11264" target="_blank">📅 10:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11263">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d76eba2226.mp4?token=Ih9AObi2nU2uZD_47cidRudDuIrfNIpoB5hoSmj-FdOxBWdtVvP0LDdqzdyueXSKgAhB0gq55kJmUPbEcY6_HZsInnkiILRPnjaVpOxTxkyw3E-CVrIfCeG3ODGiCzYFhkUDRi4q6Qkf66f_MlZaqOS2d5FQH1Bjty4zW_K_JAaz2ZpBh0TBLJNT4er2moYLizzzfGBS0LOCwsWztJ7YV0ZP74wVIRn0S7Ttn4M_OG9SxVSQzvohnKCKOhGaxyKYxsNPDDpNOnEl4ZKkCR3dwe_LnQ_EcUcZSa2H85DAMt88lp7OuHE9-Co6rHdR-kmejW5qChVjhWZTyGtmARkxcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d76eba2226.mp4?token=Ih9AObi2nU2uZD_47cidRudDuIrfNIpoB5hoSmj-FdOxBWdtVvP0LDdqzdyueXSKgAhB0gq55kJmUPbEcY6_HZsInnkiILRPnjaVpOxTxkyw3E-CVrIfCeG3ODGiCzYFhkUDRi4q6Qkf66f_MlZaqOS2d5FQH1Bjty4zW_K_JAaz2ZpBh0TBLJNT4er2moYLizzzfGBS0LOCwsWztJ7YV0ZP74wVIRn0S7Ttn4M_OG9SxVSQzvohnKCKOhGaxyKYxsNPDDpNOnEl4ZKkCR3dwe_LnQ_EcUcZSa2H85DAMt88lp7OuHE9-Co6rHdR-kmejW5qChVjhWZTyGtmARkxcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar
منتظر ری اکشننن</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/withyashar/11263" target="_blank">📅 10:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11262">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromayoub</strong></div>
<div class="tg-text">نظرت چیه؟قبل جام جهانی میزنع یا بعد؟</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/withyashar/11262" target="_blank">📅 10:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11261">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">کانال 13 اسرائیل:اسرائیل انتظار دارد حمله احتمالی آمریکا در ایران از فردا با بازگشت ترامپ از چین آغاز شود
@withyashar</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/withyashar/11261" target="_blank">📅 10:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11260">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9469892534.mp4?token=P_5M7TwDuV4n_r2zF4YUzUAkvxF2dEPJ9hd0XdG3kfhtRki3ev9TxS1z9RgOrPGtfiJSQTGLiczuRQG1rmFioWjEr66kmFGK6AvG-nEUQdno59kKgiU_E-a2GxEoIE1tt0skbAzsGkVZJSn0MxiLFuX5ZFe9kDavevBg4zSIPBz9Vb74mmZf4bcNtqhobWkX1Pj8Od5Bw7OvP05Q5SspT81uD0Xo6cwyRygbAyVE_JsDSxPe2fFj5cO0hv7mCKs8oT-Tk9AGzEKLwn8pPGofFYmNf5olah3tbpE_Jh3qqP09r87Pp0uYSK2YiCHYvnDUui24RKZYuds2R83pP0CdpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9469892534.mp4?token=P_5M7TwDuV4n_r2zF4YUzUAkvxF2dEPJ9hd0XdG3kfhtRki3ev9TxS1z9RgOrPGtfiJSQTGLiczuRQG1rmFioWjEr66kmFGK6AvG-nEUQdno59kKgiU_E-a2GxEoIE1tt0skbAzsGkVZJSn0MxiLFuX5ZFe9kDavevBg4zSIPBz9Vb74mmZf4bcNtqhobWkX1Pj8Od5Bw7OvP05Q5SspT81uD0Xo6cwyRygbAyVE_JsDSxPe2fFj5cO0hv7mCKs8oT-Tk9AGzEKLwn8pPGofFYmNf5olah3tbpE_Jh3qqP09r87Pp0uYSK2YiCHYvnDUui24RKZYuds2R83pP0CdpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایان سفر ترامپ به چین
دونالد ترامپ، رئیس جمهور آمریکا، پکن را ترک کرد و سفر خود به جمهوری خلق چین را به پایان رساند.
شی جین‌پینگ، رئیس‌جمهور چین در آخرین روز سفر رئیس جمهور ایالات متحده گفت که دونالد ترامپ به دنبال بازگرداندن عظمت آمریکا است و او نیز متعهد به هدایت مردم چین برای تحقق رستاخیز ملی است.
شی جین‌پینگ همچنین تأکید کرده است که چین و آمریکا می‌توانند از طریق تقویت همکاری‌ها، روند توسعه و پیشرفت خود را تسریع کنند.
@withyashar</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/withyashar/11260" target="_blank">📅 10:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11259">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1169f33889.mp4?token=fD4qi8aVVKJSMeXHbr0Rd79XoTxG_ngkbHtOBhXfNEH6I1KkZuFUpHolbZcRNjQlBimldOudbIgOyK9CNHEpFDk7fUH4gQQxUB9J7RcO7PCA-LLX13oMZ58TdPpXChv-RWo2ET8Qa5QkDNaxVRHm58zosqjBR6o2J9b38b3ouhUtOndhTehRXrKIhU7C17aVteHYCsoWYiRugLcqBF0wrgZBL79zY4Y-F7cUl3UwzeExjCfeS-MViOphRL5siouOkUT2SkfztpYIi0xe6pTjVf0Np3kqw3lKPvwYhlQ2B_mubXWwnot12Ms9L7JSGuWTpIfRRfzBMF90od_khHIuYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1169f33889.mp4?token=fD4qi8aVVKJSMeXHbr0Rd79XoTxG_ngkbHtOBhXfNEH6I1KkZuFUpHolbZcRNjQlBimldOudbIgOyK9CNHEpFDk7fUH4gQQxUB9J7RcO7PCA-LLX13oMZ58TdPpXChv-RWo2ET8Qa5QkDNaxVRHm58zosqjBR6o2J9b38b3ouhUtOndhTehRXrKIhU7C17aVteHYCsoWYiRugLcqBF0wrgZBL79zY4Y-F7cUl3UwzeExjCfeS-MViOphRL5siouOkUT2SkfztpYIi0xe6pTjVf0Np3kqw3lKPvwYhlQ2B_mubXWwnot12Ms9L7JSGuWTpIfRRfzBMF90od_khHIuYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: امیدوارم ایران تماشا کند. ما دقیقاً می‌دانیم چه چیزی را آماده کرده‌اند. می‌دانید، آن‌ها کمی استراحت داشتند، بنابراین سعی دارند چند چیز را با هم جمع کنند. آن‌ها موشک‌هایی را از زیر زمین بیرون آورده‌اند. همه این‌ها در یک روز از بین خواهند رفت. امیدوارم این رو ببینند چون همه کارهایی که در چهار هفته گذشته انجام داده‌اند، در یک روز از بین خواهد رفت.
@withyashar
یاشار:خوب دیگه رسمأ داره میگه جنگ میشه و هم داره میگه حمله خیلی سریع و محکم انجام میشه همانطور که گفتیم</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/withyashar/11259" target="_blank">📅 10:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11258">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آمریکا پیشنهاد ۱۴ ماده‌ای ایران را رد کرد
طبق اطلاعات رسیده به تهران تایمز، دولت آمریکا پاسخ پیشنهاد مکتوب ایران درباره پایان جنگ را داده است.
گفتنی است ایران پیشنهاد خود را مبتنی بر مذاکرات دو مرحله ای ارائه کرده بود که در مرحله اول منجر به پایان جنگ در همه جبهه ها شده و در صورت تحقق شروط ایران، مرحله دوم مذاکرات که درباره موضوع هسته ای بود، آغاز می شد
@withyashar</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/withyashar/11258" target="_blank">📅 10:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11257">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مجلس نمایندگان آمریکا برای سومین بار طرح دموکرات‌ها جهت محدود کردن اختیارات نظامی ترامپ علیه جمهوری اسلامی رو رد کرد.
این طرح با نتیجه ۲۱۲ در برابر ۲۱۲ به تساوی رسید و در نهایت با اختلاف یک رای شکست خورد.
@withyashar</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/withyashar/11257" target="_blank">📅 09:48 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11256">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ، به شبکه فاکس نیوز: مذاکره با ایران درباره کنار گذاشتن غبار هسته‌ای به دلیل تضاد در تصمیمات ایران، رفت و برگشت دارد تأسیسات هسته‌ای ایران تحت نظارت مداوم ۹ دوربین، ۲۴ ساعته قرار دارند. هرگونه تحرک ایرانی در داخل تأسیسات هسته‌ای با واکنش مستقیم نظامی…</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/withyashar/11256" target="_blank">📅 09:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11255">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e641dc900e.mp4?token=W5J62XPL3MlKGEvZf-hAIFxRt_4RnnXsbppm7cVG1A6PcFFCDF219RxAuJEynNnUgJ7jh3OufvE-X4KyAEHtFOBzruLq9W0LZ_Uk3AjZ_uWrGNLkEkafs8rzeo2WaelIODSbJoFUChJWufHMOFVVGuWhKvW_CaEgXx-bXSDp78coStauOVJwsBSOMFAzs6VRAW5c9TuuPN4NyRS-VtUMEhzVMHIlv2qq6f2v9ufR4b6rtUCRXgzz7ozptjUtgck_bP1CcQN2NbFfPjKGR0i-Ub5YYGhgJUqNnh_H8-ixPBo2fKN19boFPuelSm2SYagxOkoioU44DlNdU9eu4KpcbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e641dc900e.mp4?token=W5J62XPL3MlKGEvZf-hAIFxRt_4RnnXsbppm7cVG1A6PcFFCDF219RxAuJEynNnUgJ7jh3OufvE-X4KyAEHtFOBzruLq9W0LZ_Uk3AjZ_uWrGNLkEkafs8rzeo2WaelIODSbJoFUChJWufHMOFVVGuWhKvW_CaEgXx-bXSDp78coStauOVJwsBSOMFAzs6VRAW5c9TuuPN4NyRS-VtUMEhzVMHIlv2qq6f2v9ufR4b6rtUCRXgzz7ozptjUtgck_bP1CcQN2NbFfPjKGR0i-Ub5YYGhgJUqNnh_H8-ixPBo2fKN19boFPuelSm2SYagxOkoioU44DlNdU9eu4KpcbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ ترامپ: ما مشکلات زیادی را حل کرده‌ایم که دیگران قادر نبودند و این رابطه یک رابطه بسیار قوی است. فکر می‌کنم در مورد ایران کارهای فوق‌العاده‌ای انجام داده‌ایم، ما هم صحبت کردیم.
‏ما در مورد ایران بسیار مشابه‌ایم، می‌خواهیم این وضعیت پایان یابد. نمی‌خواهیم آن‌ها به سلاح هسته‌ای دست پیدا کنند. می‌خواهیم تنگه‌ها باز باشند و ما آن را برایشان می‌بندیم، آن‌ها تنها تنگه را بستند و بعد ما هم روی سرشان بستیم.
@withyashar</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/withyashar/11255" target="_blank">📅 09:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11254">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ، به شبکه فاکس نیوز: مذاکره با ایران درباره کنار گذاشتن غبار هسته‌ای به دلیل تضاد در تصمیمات ایران، رفت و برگشت دارد
تأسیسات هسته‌ای ایران تحت نظارت مداوم ۹ دوربین، ۲۴ ساعته قرار دارند.
هرگونه تحرک ایرانی در داخل تأسیسات هسته‌ای با واکنش مستقیم نظامی مواجه خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/withyashar/11254" target="_blank">📅 09:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11253">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/11253" target="_blank">📅 01:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11252">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBehnam Kok</strong></div>
<div class="tg-text">آقا ما استیکر حامله میخوایم</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/withyashar/11252" target="_blank">📅 01:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11251">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ در تروث : «وقتی رئیس‌جمهور شی با بیانی بسیار سنجیده از ایالات متحده به‌عنوان کشوری که شاید در حال افول باشد یاد کرد، منظور او آسیب عظیمی بود که ما در چهار سال دوران جو بایدنِ خواب‌آلود و دولت بایدن متحمل شدیم؛ و در این مورد، او صددرصد درست می‌گفت.
کشور ما با مرزهای باز، مالیات‌های سنگین، ترویج تغییر جنسیت برای همه، حضور مردان در ورزش زنان، سیاست‌های موسوم به تنوع و شمول، توافق‌های تجاری وحشتناک، جرم و جنایت گسترده و بسیاری مسائل دیگر، آسیب غیرقابل‌تصوری دید!
@withyashar
رئیس‌جمهور شی به هیچ‌وجه به رشد شگفت‌انگیزی اشاره نمی‌کرد که ایالات متحده در طول شانزده ماه فوق‌العاده دولت ترامپ به جهان نشان داده است؛ دورانی که شامل رکورد تاریخی بازار بورس و صندوق‌های بازنشستگی، پیروزی نظامی و روابط شکوفا با ونزوئلا، درهم‌کوبیدن نظامی ایران (ادامه دارد!)، قدرتمندترین ارتش جهان با اختلاف بسیار زیاد، تبدیل دوباره آمریکا به یک قدرت اقتصادی عظیم، جذب رکورد هجده تریلیون دلار سرمایه‌گذاری خارجی در آمریکا، بهترین بازار کار تاریخ ایالات متحده با بیشترین تعداد شاغلان تاریخ کشور، پایان دادن به سیاست‌های ویرانگر موسوم به تنوع و شمول و بسیاری موفقیت‌های دیگر بوده که فهرست کردن همه آنها ممکن نیست.
در حقیقت، رئیس‌جمهور شی بابت این همه موفقیت بزرگ در چنین مدت کوتاهی به من تبریک گفت.
دو سال پیش، ما واقعاً کشوری در حال افول بودیم. در این مورد کاملاً با رئیس‌جمهور شی موافقم! اما حالا ایالات متحده داغ‌ترین و پررونق‌ترین کشور جهان است و امیدوارم رابطه ما با چین از همیشه قوی‌تر و بهتر باشد!»
@withyashar</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/withyashar/11251" target="_blank">📅 01:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11250">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">فاکس نیوز : تو سفر ترامپ، بین مأموران سرویس مخفی آمریکا و پلیس چین، تنش ایجاد شده و درگیری لفظی و حتی فیزیکی هم پیش اومده.
@withyashar</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/11250" target="_blank">📅 01:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11249">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TB8oJUkyrSBysRzP-M_1gQ-TT5d3knMSu1TIdnQf7KJno1nPyjHRF6Nk9UMwmiNOWOfxnZKSbsmm18zk5JDZOAOMY1k7OQZnozCeBvVRZ2HqmelGWJVOTWlXErNhCjRmefjvt2zYqMklAS4TOt7Lqs4_nxvLCDx-5TrfP5YBRvsYzzl5kHkk3V-L9d7L9GmAikt69UL2F4PJFLHLfkTZlsxVQ582t8G9_8Hu9KfzajkH1hACSIRJUAzBnYvjI-agiAl7IOCneOOdOsueNcTNewe9hgs7r2CGy02s0oyO_EcnKKZfcM9FBa8wt5PaJdkIFu-c3UAJIvLIcz5O5CTv_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کت کش ها در مراسم اربعین کتلت سرلشکر سیدعبدالرحیم موسوی در قم
@withyashar</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/withyashar/11249" target="_blank">📅 00:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11248">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b591abd93e.mp4?token=c62lvPJg4n5FaSYq0sRyAY7_FWcXhjMKaox2rPsMnWzGi0lhaQwWdmNlSF6at01Hn2moIMrRQcuD4iiz6vQDJUsjF3C3DbVihHvcYpQsQOexe6Mbh5lvPHKkk64lRUuGr-hAfZFL_LmRw3h3rYMWn3uQHwS94SjyJQYb3yAkIV-t_6Fayx8TMQVONYTK62As8mHdHVDEvUEKUlg1PoycG2yX0FVm1454pMgw4o7jsyfh4SQN17FDoO9MT3JdQsOyDPO_XMsBT6GUI2QSNgBRUat8-XRn7hwPDgSCUCKBOJ0vBr39BP3GduTaSjYN_7Mb6OtVK06ClqYcE-7OQSolOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b591abd93e.mp4?token=c62lvPJg4n5FaSYq0sRyAY7_FWcXhjMKaox2rPsMnWzGi0lhaQwWdmNlSF6at01Hn2moIMrRQcuD4iiz6vQDJUsjF3C3DbVihHvcYpQsQOexe6Mbh5lvPHKkk64lRUuGr-hAfZFL_LmRw3h3rYMWn3uQHwS94SjyJQYb3yAkIV-t_6Fayx8TMQVONYTK62As8mHdHVDEvUEKUlg1PoycG2yX0FVm1454pMgw4o7jsyfh4SQN17FDoO9MT3JdQsOyDPO_XMsBT6GUI2QSNgBRUat8-XRn7hwPDgSCUCKBOJ0vBr39BP3GduTaSjYN_7Mb6OtVK06ClqYcE-7OQSolOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ به دلیل مرگ برادر بزرگترش که بر اثر نوشیدن الکل جانش را از دست داد ،مشروب نمیخوره ،ولی اینجا جرعه‌ای از آن را مینوشه و به نشانه احترام به رئیس جمهور شی جین پینگ
‏ولی داشت بالا می‌آورد
@withyashar</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/withyashar/11248" target="_blank">📅 00:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11247">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">طبق گزارش‌های امروز، هرتزوگ رئیس جمهور اسرائیل حضور حضوری خود در نیویورک را لغو کرده و گفته به دلیل «شرایطی که مانع سفر شده» نمی‌تواند به آمریکا بیاید.
اما این سفر یک سفر رسمی سیاسی به کاخ سفید نبود،بلکه مربوط به شرکت او در مراسم فارغ‌التحصیلی «Jewish Theological Seminary» در نیویورک بود.
در عین حال، خبر جداگانه‌ای هم درباره سفر احتمالی بنیامین ناتانیاهو به آمریکا وجود داشت که دفتر او گفته بود هنوز برنامه قطعی‌ای برایش نهایی نشده است
@withyashar</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/withyashar/11247" target="_blank">📅 00:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11246">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">طبق گزارش فاکس نیوز : رئیس‌جمهور ترامپ و هیئت همراهش در طول سفر به چین از تلفن‌ها و لپ‌تاپ‌های جایگزین استفاده کردند به دلیل نگرانی‌هایی که داشتند مبنی بر اینکه مقامات چینی ممکن است از آن‌ها برای نصب نرم‌افزار جاسوسی استفاده کنند
@withyashar</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/withyashar/11246" target="_blank">📅 23:52 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11245">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">همینجور این پیغام میاد دم همتون گرم مخصوصا عزیزی که یاد کرد از من
🥹
🙌🏾
❤️‍🩹
میامممم میاممم</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/11245" target="_blank">📅 23:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11244">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMmd</strong></div>
<div class="tg-text">یکی اومد رو خط برنامه کامبیز تو اینترنشنال گفتش از همه مجریای اینترنشنال تشکر میکنم ، حتی یاشار وار روم توی تلگرام ک خیلیا اخبارا رو ازونجا دنبال میکنن دمتون گرم</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/withyashar/11244" target="_blank">📅 23:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11242">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دیده شده پهپاد شناسایی و صدای پدافند غرب تهران
@withyashar</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/withyashar/11242" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11241">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اعتراضات کوبا شروع شد کشور در حال  فروپاشی
طبق گزارش‌ها، شبکه برق کوبا در بامداد امروز دچار فروپاشی شد و مناطق شرقی از جمله شهر مهم سانتیاگو دِ کوبا بدون برق ماندند. مردم به خیابان آمدند، قابلمه‌ها را به هم کوبیدند، زباله آتش زدند و شعار «برق را وصل کنید» سر دادند.
دولت کوبا علت اصلی را تحریم‌ها و فشار آمریکا بر صادرات سوخت به کوبا می‌داند. رسانه‌هایی مانند رویترز و گاردین نوشته‌اند که پس از تهدیدهای جدید دولت ترامپ علیه کشورهایی که به کوبا سوخت می‌فرستند، ارسال نفت از ونزوئلا و مکزیک کاهش یافته و کوبا عملاً ذخیره سوختش را از دست داده است. وزیر انرژی کوبا گفته:
«ما مطلقاً هیچ گازوئیل و هیچ نفت کوره‌ای نداریم.»
در بعضی مناطق مردم تا ۲۰ یا حتی ۲۲ ساعت در روز برق ندارند. این وضعیت باعث خراب شدن مواد غذایی، اختلال در بیمارستان‌ها، حمل‌ونقل و حتی تعطیلی برخی خدمات عمومی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/withyashar/11241" target="_blank">📅 23:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11240">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/141998de31.mp4?token=mWjKL2syYnwh-XyrnfJBPHJ8rVi-6aZV8LWqYTdoxOToXzAtM6eyMdGUPLTLhHhn9i4PcpnklZS0g1eSAhFe19wCr4F-Ib1wIr7ho47yrZ6esNIL-apTeZymZZ6wLd2O_wDPcHFzS8R2FJKdT5tqIfQyeJ9_pFD7z8UTjlZnaB0e8bsqWAxnxNq5boTh56UnqHV0AqSLrCJNKJr-gti6kn2H0s5ttNudyjvSzSMPNF7jYd70J71HJS2Pqba2ZyWtmxD3bvhgeuJcK8CFhkYfAxAgn65GZxuCI-_0g8S6HHKDuKJf829-WZ9-1g4lzU43de0qiw7RnkkDaWGNh1MVzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/141998de31.mp4?token=mWjKL2syYnwh-XyrnfJBPHJ8rVi-6aZV8LWqYTdoxOToXzAtM6eyMdGUPLTLhHhn9i4PcpnklZS0g1eSAhFe19wCr4F-Ib1wIr7ho47yrZ6esNIL-apTeZymZZ6wLd2O_wDPcHFzS8R2FJKdT5tqIfQyeJ9_pFD7z8UTjlZnaB0e8bsqWAxnxNq5boTh56UnqHV0AqSLrCJNKJr-gti6kn2H0s5ttNudyjvSzSMPNF7jYd70J71HJS2Pqba2ZyWtmxD3bvhgeuJcK8CFhkYfAxAgn65GZxuCI-_0g8S6HHKDuKJf829-WZ9-1g4lzU43de0qiw7RnkkDaWGNh1MVzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیروزی بزرگ برای‌ ترامپ ، فاکس نیوز تایید کرد
رئیس جمهور چین، شی جین پینگ دستور داد در مورد ایران، «هر چیزی که ترامپ نیاز دارد» را به آمریکا بدهید.
از ‌آمریکا سویای بیشتری بخرید.
نفت بیشتری از آمریکا بخرید.
از آمریکا گاز مایع طبیعی بیشتری بخرید.
۲۰۰ جت بوئینگ ۷۳۷ مکس بخرید.
@withyashar</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/withyashar/11240" target="_blank">📅 22:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11239">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خبر خوب
😍</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/withyashar/11239" target="_blank">📅 22:54 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11238">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7bad13156.mp4?token=bpCAOSuqZtLMYAYqnB-HJEb7KW_ce2oe6N-ZpHUw8Uaikh-TrI0KkCfKFYF4fmaCiHTJoNx6Tt5QGt1Pqk2DwwI8NgFbCAxeY115PaztVOHpb9444oh4WXSpF8qkFVxbZGtloHkyaxJST0EfhddYwQKHh2DJIfe7W43JKios9YgIllAm-2eFZzsBro135NHjiCtadw66QKvNz86u0xR9Y4JCs5vi37__w4FjISf4yvbPwE331Lis6yMLC-CyYznquvE8peE--8g-CnJtOrYKqgog7eOtgYUe3aeJ4gAszehZ3A1fZZv0y86szcKsHF8Po91diT2KZClqBn8PKvgldg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7bad13156.mp4?token=bpCAOSuqZtLMYAYqnB-HJEb7KW_ce2oe6N-ZpHUw8Uaikh-TrI0KkCfKFYF4fmaCiHTJoNx6Tt5QGt1Pqk2DwwI8NgFbCAxeY115PaztVOHpb9444oh4WXSpF8qkFVxbZGtloHkyaxJST0EfhddYwQKHh2DJIfe7W43JKios9YgIllAm-2eFZzsBro135NHjiCtadw66QKvNz86u0xR9Y4JCs5vi37__w4FjISf4yvbPwE331Lis6yMLC-CyYznquvE8peE--8g-CnJtOrYKqgog7eOtgYUe3aeJ4gAszehZ3A1fZZv0y86szcKsHF8Po91diT2KZClqBn8PKvgldg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: دشمنان ما به دنبال نابودی همه ما هستند. همه ما
آنها بین راست و چپ، سکولار و مذهبی، یهودی و عرب تفاوتی قائل نمی‌شوند.
@withyashar
نتانیاهو: اورشلیم را تحت حاکمیت اسرائیل برای همیشه حفظ خواهیم کرد</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/withyashar/11238" target="_blank">📅 22:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11237">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/withyashar/11237" target="_blank">📅 21:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11236">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سومین دور مذاکرات مستقیم لبنان و اسرائیل در واشنگتن آغاز شد
@withyashar</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/11236" target="_blank">📅 21:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11235">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ اعلام کرد که انتظار می‌رود پکن ۲۰۰ هواپیما از بوئینگ سفارش دهد.
@withyashar</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/withyashar/11235" target="_blank">📅 21:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11234">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کان نیوز : مقامات ارشد ارتش اسرائیل و سنتکام  هفته گذشته جلسه داشتن و منتظرن ببینن فردا ترامپ بعد اتمام سفرش چه تصمیمی میگیره
@withyashar</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/withyashar/11234" target="_blank">📅 21:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11233">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016c112e90.mp4?token=Lyah6gFCEmODdi8dMub3GVR5nhEoc4Xbx22HDQWkX-6Q0iA0T7QoIA2pT7NvXoCmHDpq6ZdZD74W-y6MgeZHsK6h1JS4gFMNb5sRnBeuMKXAdO_d4T-DoNN_9RvwsDc05n31HV7mBDh_SulyZxeoXQ6st-076cu7bnHxVfMpdMi3wnf-C7A5AGug5vVudTJHmQolxTHjzF6Mxgb08b_Ua4ESfO0g0zbPm0WX-3fp2kf6Y_4WtLU-T_EPxyFd96VHt0xMUqUktNKDoPCQbZnSu1lhfG-WBOzHMSew48cP92kqfnCMj0ePYtuEMEObZST0QrSSqY-Nxo48lJZVNR29sHEFzOB99sQDGAHqhHPxcg8BP3yzckEoxOaBKa2O0rFhzbkEgHrYk26R6lVv2E9ZBTlfvaehndw9VJSS3NTocvLMd-sG2xEXzFj4RYdKWwNS7RrmgNCYSg6gF1efDf3vu7-MlOvgiYiy6V29XAl2tvoRsl5hU75eHd0NDqxi4RGqaBBn-YAIF7Qu_A7LgR0q1QkaT1FurO3S2JW8_S6SD3IJya44ZoIBIVVTI2-F8wQsPfmmkfOn8HRDK_l79U98HeK_XS3vaVG0A_llUVIR0tRgjSOmnvBYT4CPPzC6pX-VyP4ufVJXKfnLcaYjo80GQAPkZZm3ddGyAq5DB2da1yk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016c112e90.mp4?token=Lyah6gFCEmODdi8dMub3GVR5nhEoc4Xbx22HDQWkX-6Q0iA0T7QoIA2pT7NvXoCmHDpq6ZdZD74W-y6MgeZHsK6h1JS4gFMNb5sRnBeuMKXAdO_d4T-DoNN_9RvwsDc05n31HV7mBDh_SulyZxeoXQ6st-076cu7bnHxVfMpdMi3wnf-C7A5AGug5vVudTJHmQolxTHjzF6Mxgb08b_Ua4ESfO0g0zbPm0WX-3fp2kf6Y_4WtLU-T_EPxyFd96VHt0xMUqUktNKDoPCQbZnSu1lhfG-WBOzHMSew48cP92kqfnCMj0ePYtuEMEObZST0QrSSqY-Nxo48lJZVNR29sHEFzOB99sQDGAHqhHPxcg8BP3yzckEoxOaBKa2O0rFhzbkEgHrYk26R6lVv2E9ZBTlfvaehndw9VJSS3NTocvLMd-sG2xEXzFj4RYdKWwNS7RrmgNCYSg6gF1efDf3vu7-MlOvgiYiy6V29XAl2tvoRsl5hU75eHd0NDqxi4RGqaBBn-YAIF7Qu_A7LgR0q1QkaT1FurO3S2JW8_S6SD3IJya44ZoIBIVVTI2-F8wQsPfmmkfOn8HRDK_l79U98HeK_XS3vaVG0A_llUVIR0tRgjSOmnvBYT4CPPzC6pX-VyP4ufVJXKfnLcaYjo80GQAPkZZm3ddGyAq5DB2da1yk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار ، شواهد نشان دهنده حمله غافلگیر کننده برای کتلت پزون است
@withyashar</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/withyashar/11233" target="_blank">📅 20:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11232">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30fb109482.mp4?token=BV3J-AOMgr2UlbOH4oH6JcxDjdlDz0Dxs0jIJrs8WQbP7FhaGoyHW0tsqhDAtC7xb879EfuNsn1zFJozH4RtX0KbIjXE8KmGQrfGlPP-zQmrvOKSih_yJ2DG-KBjACZI6gM3EyLe0Xjzy0zTyvRrwXiL_y4F_V0Jp1s5H4YHJP6BOrcr4ciPrekYUY4peFQc8cqJQEFUEcruKsfT7cOy3K64SJZwcKf489X-wVLyUpR42rUK5mXDKCfx0QzQGkOrFiHYQqFFm9yIIxu2TW1jrThgYQ-_xF3sET4Ftjm64uo9A56ocDzQC7IXvufEtumBeaoeFIAwNxv8j2cJY_j-pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30fb109482.mp4?token=BV3J-AOMgr2UlbOH4oH6JcxDjdlDz0Dxs0jIJrs8WQbP7FhaGoyHW0tsqhDAtC7xb879EfuNsn1zFJozH4RtX0KbIjXE8KmGQrfGlPP-zQmrvOKSih_yJ2DG-KBjACZI6gM3EyLe0Xjzy0zTyvRrwXiL_y4F_V0Jp1s5H4YHJP6BOrcr4ciPrekYUY4peFQc8cqJQEFUEcruKsfT7cOy3K64SJZwcKf489X-wVLyUpR42rUK5mXDKCfx0QzQGkOrFiHYQqFFm9yIIxu2TW1jrThgYQ-_xF3sET4Ftjm64uo9A56ocDzQC7IXvufEtumBeaoeFIAwNxv8j2cJY_j-pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در سال ۱۹۷۲، شهبانو فرح پهلوی به دعوت رسمی دولت چین به این کشور سفر کرد؛ سفری تاریخی و بی‌سابقه که در اوج جنگ سرد، نماد دیپلماسی بی‌طرفانه ایران بود
@withyashar</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/withyashar/11232" target="_blank">📅 20:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11231">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">آیا درباره حمایت چین از ایران با رئیس جمهور چین صحبت کردید؟  ترامپ: ما در مورد این موضوع صحبت کردیم. منظورم اینه که وقتی میگید «حمایت»، آنها با ما جنگ نمی‌کنن یا چیزی شبیه این. او گفت که تجهیزات نظامی ارائه نخواهد کرد، این یک بیانیه بزرگه. اما در عین حال گفت…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/withyashar/11231" target="_blank">📅 19:35 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11230">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/withyashar/11230" target="_blank">📅 19:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11229">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">«دریادار برد کوپر»، فرمانده سنتکام:  «فرماندهی مرکزی ایالات متحده (سنتکام) مستقیماً در پاسخ به تهدیدهایی که جمهوری اسلامی ایران ایجاد می‌کرد، تأسیس شد.  رژیم ایران طی ۴۷ سال گذشته منطقه را دچار هراس و بی‌ثباتی کرده و دشمنی با آمریکا را به یکی از اصول اساسی…</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/withyashar/11229" target="_blank">📅 19:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11228">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/withyashar/11228" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11227">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗦𝗨𝗦</strong></div>
<div class="tg-text">خسته نباشی یاشار
نظرت راجب سیم‌کارت پرو چیه به مردم عادی هم دارن میدن الان</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/withyashar/11227" target="_blank">📅 18:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11226">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">لطفا عکس از اس ام اس هایی که رژیم میده برام نفرستید ! خیلی خوشم میاد ! اگه قرار‌باشه هر روز اونا اس ام اس بدن شمام همتون اسکرین بفرستین که نمیشه ! به هیچ عنوان اسکرین ندید دیگه مخصوصا ‌جانفدا رو … مرسی اه</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/withyashar/11226" target="_blank">📅 18:54 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11225">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ: رهبر چین پیشنهاد کمک در مورد مسئله ایران را داد
او قول داد که تجهیزات نظامی به آنها منتقل نکند.
او می‌خواهد تنگه هرمز باز بماند.
@withyashar</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/11225" target="_blank">📅 18:48 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11224">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سناتور کنگره خطاب به برد کوپر:
برجام توانایی هسته ای ایران رو محدود میکرد ولی ترامپ پاره کرد، الان وارد یه جنگ بی‌پایان شدیم، آیا ترامپ هیچ وقت به شما نگفت چرا برجام رو پاره کرد؟
کوپر فرمانده سنتکام:
خانم سناتور زمانی که این ۸ سال پیش اتفاق افتاد من یک سمت دیگه داشتم! من سیاستمدار نیستم و نمیتونم جواب این سوال رو بدم!
@withyashar</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/withyashar/11224" target="_blank">📅 18:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11223">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e028b3e623.mp4?token=NgTyTVjNZiE7f1yHwmDG_B_zvYEwvHAmCBnYcupv9zVRCI8l_ozrLmTnIrA6RaD42tZ__ObPzFFmXqjgFDWyUQbRLRsNU7OtOgDxcgjckcu9RzTcjCcfcKxaHKqek_SH10Sjo-Yr-8-X_p7Ea8Y7nijHiPFsYfSKpKqSkn6FWs3EEaZpbS_-MBsD29HOi0WqHQZz_sD8DYa5zwybTbY3w0TQyZvNIxW1klSVE2wuec5w7U-LqAoz89H4K2ufnUn2V_QobhI9S-n0AVBo_9pixk8mgvtobgE_C1NOT7t5iI0PMQaO8Kf9sprk_Kd-VHJU-5BBsviGUkoKFnh-WzWbDYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e028b3e623.mp4?token=NgTyTVjNZiE7f1yHwmDG_B_zvYEwvHAmCBnYcupv9zVRCI8l_ozrLmTnIrA6RaD42tZ__ObPzFFmXqjgFDWyUQbRLRsNU7OtOgDxcgjckcu9RzTcjCcfcKxaHKqek_SH10Sjo-Yr-8-X_p7Ea8Y7nijHiPFsYfSKpKqSkn6FWs3EEaZpbS_-MBsD29HOi0WqHQZz_sD8DYa5zwybTbY3w0TQyZvNIxW1klSVE2wuec5w7U-LqAoz89H4K2ufnUn2V_QobhI9S-n0AVBo_9pixk8mgvtobgE_C1NOT7t5iI0PMQaO8Kf9sprk_Kd-VHJU-5BBsviGUkoKFnh-WzWbDYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«دریادار برد کوپر»، فرمانده سنتکام:
«فرماندهی مرکزی ایالات متحده (سنتکام) مستقیماً در پاسخ به تهدیدهایی که جمهوری اسلامی ایران ایجاد می‌کرد، تأسیس شد.
رژیم ایران طی ۴۷ سال گذشته منطقه را دچار هراس و بی‌ثباتی کرده و دشمنی با آمریکا را به یکی از اصول اساسی حاکمیت خود تبدیل کرده است.
سابقه خصمانه و مرگبار آنها علیه ایالات متحده کاملاً مستند و ثبت‌شده است
@withyashar</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/withyashar/11223" target="_blank">📅 18:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11222">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">آیا درباره حمایت چین از ایران با رئیس جمهور چین صحبت کردید؟
ترامپ: ما در مورد این موضوع صحبت کردیم. منظورم اینه که وقتی میگید «حمایت»، آنها با ما جنگ نمی‌کنن یا چیزی شبیه این. او گفت که تجهیزات نظامی ارائه نخواهد کرد، این یک بیانیه بزرگه. اما در عین حال گفت که آنها مقدار زیادی نفت خودشون رو از ایران میخرن و دوست دارن این کار رو ادامه بدن.
@withyashar</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/withyashar/11222" target="_blank">📅 18:38 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11221">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">برد کوپر فرمانده سنتکام مدعی شد:
توانمندی‌های موشکی، دریایی، پهپادی و صنعتی ایران 90 درصد تضعیف شده است. او افزود که نیروی دریایی ایران تا یک نسل دیگر نیز به سطحی که پیش از جنگ در اختیار داشت باز نخواهد گشت
@withyashar</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/withyashar/11221" target="_blank">📅 18:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11220">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fca974d01b.mp4?token=rQTRtX_2oW2rrpr_spyVN6NAOUW3R_FjCc1b2QNgZoiVKf40cxZb6xV1tmDPn1_IdGHDT3tTzDOvCgCCty3mS1ZQXQiwx2a5viS59LI5EVif5Jl7_xZvcisTULL2XRgpKWsBKrLEvudUEefVLcAPUlpeO5cKzehqor_O0CSJs9g_FpD0Vd-Xfno-DpqLblUKfXp9W51lmd1-OwzMQ83O1npfTIlihfM_gPvSQWuiN5uvsjR0b1HsXrTW7-1YpE-TaxxTSvkOIuiBDXWkZAqY07RAzY6rNWP_Njp7-LKINrcrWYxTHw1FUz5VloLX1uqDBSV17zXk2qymXtJCyb9ThQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fca974d01b.mp4?token=rQTRtX_2oW2rrpr_spyVN6NAOUW3R_FjCc1b2QNgZoiVKf40cxZb6xV1tmDPn1_IdGHDT3tTzDOvCgCCty3mS1ZQXQiwx2a5viS59LI5EVif5Jl7_xZvcisTULL2XRgpKWsBKrLEvudUEefVLcAPUlpeO5cKzehqor_O0CSJs9g_FpD0Vd-Xfno-DpqLblUKfXp9W51lmd1-OwzMQ83O1npfTIlihfM_gPvSQWuiN5uvsjR0b1HsXrTW7-1YpE-TaxxTSvkOIuiBDXWkZAqY07RAzY6rNWP_Njp7-LKINrcrWYxTHw1FUz5VloLX1uqDBSV17zXk2qymXtJCyb9ThQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک و پسرش  «اِکس اَش اِی-توئلو» «X Æ A-Xii» در پکن
@withyashar</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/withyashar/11220" target="_blank">📅 18:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11219">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فرمانده سنت‌کام: ظرف کمتر از ۴۰ روز می‌توانیم به اهدافمان در ایران دست پیدا کنیم
@withyashar</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/withyashar/11219" target="_blank">📅 18:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11218">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نتانیاهو، نخست‌وزیر، و گیدعون سعر، وزیر خارجه، به مقامات دستور داده‌اند تا مقدمات طرح شکایت افترا علیه نیویورک تایمز را آغاز کنند.
این شکایت به دلیل انتشار یادداشتی از نیکلاس کریستوف که شامل اتهاماتی مبنی بر سوءاستفاده جنسی از فلسطینیان در زندان‌های اسرائیل بوده،
مقاله کریستف با عنوان «سکوتی که تجاوز به فلسطینیان با آن روبرو می‌شود» روز دوشنبه ۱۱ مه در نیویورک‌تایمز منتشر شده بود.
@withyashar</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/withyashar/11218" target="_blank">📅 18:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11217">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmKE4oosfMosE7UMfCndBEZH5wxewYELQ0Hf_cwJB__4SaSECCRl5A3ph-r2KbudjebP-APXs186o_R_Lo41rAcy_VPqgsUgm9uICSEznP9XJkran2F09dqYmGZGCnk3GiqtdtsPLpD0NWJSJ-uAtjaw3nE0y--WBJboo0GWwDXjWsqCEhwdkZFumO0YCnkJu1rtXMOktXZUDnPdvvsJDeiQmhJ45QHvqtLMpNncwtMQvItmo31zcyhDis9PvIfbvMnayvQThZF7ApFNDG3ltjd-IXrqh3k1Nx6iMf-ZeAzXB1MKiyCSuZpDavdf5ib3wjZfyhfuUqqa1BIAqHMyOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">INDOPACOM
، فرماندهی نظامی آمریکا برای منطقهٔ «هندو-پاسیفیک»ایندوپکام: تفنگداران دریایی ایالات متحده، واحد یازدهم اعزامی تفنگداران دریایی، در حال انجام تیراندازی رزمی بر روی ناو جنگی یو اس اس کامستاک (LSD 45) در اقیانوس هند هستند. واحد یازدهم اعزامی دریایی، که بر روی گروه آماده آبی-خاکی باکسر(USS BOXER) مستقر شده است، یک نیروی پایدار و قابل اعتماد رزمی است که به بازدارندگی و واکنش به بحران در منطقه عملیاتی ناوگان هفتم ایالات متحده کمک می‌کند.
@withyashar
یاشار: ساده بگم ناو باکسر وسط راه مونده داره تمرین میکنه و معلوم نیست کی بیاد !</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/withyashar/11217" target="_blank">📅 17:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11215">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d789d55b5d.mp4?token=kiB5IF4T1t0q2BgNwtNxXABEFDU_d6yBfQTHA7qE0tOjDrp1G-5a-BUe2kYHe9FszWFDUZ0Nx1WyhzEkNmRSE8So9Vyh0OY5miwKpWIUMAGK-0QtQlh5YXl3ZCOVr5_yxq3TKKIk--MW8L0fB4bmj-szF7EVQv9dnRb3bJLGnlQUSAyHo2bqQrbpVqJNlgkp6FgPAdkt-MUWdrC2pBD1mZRusYazLx5etumbR0o7LB3RhIt67CWWC59gHBw1DcHMlp5t-4gvMwBm75cZcSUUrU2Dv_NiEMPqAC37DGAVnVqAkqAXr-DNohbKfNmpNRPfvm-cZ2oi8KLuT6jbANEkGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d789d55b5d.mp4?token=kiB5IF4T1t0q2BgNwtNxXABEFDU_d6yBfQTHA7qE0tOjDrp1G-5a-BUe2kYHe9FszWFDUZ0Nx1WyhzEkNmRSE8So9Vyh0OY5miwKpWIUMAGK-0QtQlh5YXl3ZCOVr5_yxq3TKKIk--MW8L0fB4bmj-szF7EVQv9dnRb3bJLGnlQUSAyHo2bqQrbpVqJNlgkp6FgPAdkt-MUWdrC2pBD1mZRusYazLx5etumbR0o7LB3RhIt67CWWC59gHBw1DcHMlp5t-4gvMwBm75cZcSUUrU2Dv_NiEMPqAC37DGAVnVqAkqAXr-DNohbKfNmpNRPfvm-cZ2oi8KLuT6jbANEkGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشیT1 "ترامپ موبایل" بعد از نزدیک
یه سال تأخیر بالاخره داره عرضه میشه
یه گوشی طلایی ۴۹۹ دلاری با برند ترامپه که
چیپ اسنپدراگون سری ۷، رم ۱۲ گیگ، حافظه
۵۱۲ گیگ و دوربین سه‌گانه ۵۰ مگاپیکسلی دارهبه نظر میاد در اصل یه گوشی ساخت چین باشه که فقط مونتاژ نهاییشو تو آمریکا انجام دادن
@withyashar</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/withyashar/11215" target="_blank">📅 16:49 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11214">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مارکو روبیو : ترامپ موضوع ایران رو با چین مطرح کرد و این خیلی مهم بود
طرف چینی گفت ما موافق نظامی‌کردن تنگه هرمز نیستیم
با سیستم عوارض‌گیری هم مخالفیم، و این موضع ما هم هست
@withyashar</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/withyashar/11214" target="_blank">📅 16:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11213">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وزیر خزانه داری آمریکا:ایران رو انقدر تحت فشار اقتصادی قرار دادیم که توی پرداخت حقوق نیروهاشم به مشکل خورده. دارن نفسای آخرشونو میکشن
@withyashar</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/withyashar/11213" target="_blank">📅 16:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11212">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c931f479b.mp4?token=mWY8uZvMs2fwGZ-viVx_YOShlLzfZBIYzgFsLLPbBQD81ecR5TRRijwnnATGv8T7tKKoJQgrmd1sW1P1J7DR1Z3bbciNtb7EScmdpS8ysz4A8icqCJRpiNNsj55SOseWGXBnU5O55zmxbZmB0V-x0TCfSjjwJJM8AJV24NGgN2XSCwHy16VFdjqsDGfwt9ocRK6lXhjayr6-rO9ORKCSKRb6zpj6Fa18lRUgQnQqOpbzVwXRhelM_FKKLPAOqOBEq2FzFIXAeOCU9EjB-qlvpNf02GrHW8Tl5iu1X-f2vvq81I6FGGTarKqSdMg2EDY6j1iLHkOV2M5kwVHoXob8Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c931f479b.mp4?token=mWY8uZvMs2fwGZ-viVx_YOShlLzfZBIYzgFsLLPbBQD81ecR5TRRijwnnATGv8T7tKKoJQgrmd1sW1P1J7DR1Z3bbciNtb7EScmdpS8ysz4A8icqCJRpiNNsj55SOseWGXBnU5O55zmxbZmB0V-x0TCfSjjwJJM8AJV24NGgN2XSCwHy16VFdjqsDGfwt9ocRK6lXhjayr6-rO9ORKCSKRb6zpj6Fa18lRUgQnQqOpbzVwXRhelM_FKKLPAOqOBEq2FzFIXAeOCU9EjB-qlvpNf02GrHW8Tl5iu1X-f2vvq81I6FGGTarKqSdMg2EDY6j1iLHkOV2M5kwVHoXob8Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز درباره ایران:
ماموریت ما کامل نشده است.ما برای احتمال اینکه ممکن است مجبور شویم دوباره اقدام کنیم - شاید حتی به زودی - آماده‌ایم. اگر اهداف تأمین نشوند، دوباره اقدام خواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/withyashar/11212" target="_blank">📅 15:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11211">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aobFCBjvo1lnKDBVuMBqBUU9m0r8aTm9RsDxUwj2pg9snREGDVA647rhg8D5UFhJ2n1woobV43nJNCK8fmsxQcDsdNNNMS9T5W52Ej8HUeuss86mUc-JIjtGYR7WxlIHs3kOKv75VtMXFr8geJWLkzvrXbwMylZUXe5ov_7y5ISl7aNYh_zHJGBf3kwCr6Inx5x6GOS2xi-2TxF3T6-c1RKeB77NrAju6ipkAiefiqyGh-XwvT37PiTQZ5Cg8shYSnbrVkwGNWcSdaPnPiVjCa72SaXkWQ-D1Wl58Iz4r5Y0TMJr0eQDO0pjau7BEc4x8QX-oUd4Q7T2lvs0T4y0AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلفی لی جون، بنیانگذار و مدیرعامل شیائومی با ایلان ماسک
@withyashar</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/withyashar/11211" target="_blank">📅 14:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11210">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">الجزیره: چین با آمریکا در مورد ایران انعطاف دارد، اما در مورد تایوان نه
مسئولان چینی پیام واضحی به ایالات متحده ارسال کرده‌اند:
چین در بسیاری از مسائل مانند ایران، تجارت و فناوری آماده انعطاف و پذیرش اختلاف نظر است، اما در یک موضوع حساس، انعطاف‌پذیر نیست و آن تایوان است.
@withyashar</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/withyashar/11210" target="_blank">📅 14:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11209">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cda0441500.mp4?token=IQ-9TSgo002kQhYqLbs3oj7FF0FRh4NTEumGB1laM2oaCnb9LB2ImPQ69qj0iUK-dS1pIVtGU8aLgMgIycZOetkgobBecZ45XnxUo-EbWoWpwCQzWdv_8dxYZ8ErZUEXxvRkA9i4CnDvi0BwxvvUAoYQH5MqeUq5uriv1e4UxsPN82uhkTfaVoR7ozacAhBMjwhVNJjlnZW0jH4EGkwdBbkh_dtcwPLv7q31T5ZlFmLGTkbKPPTV3Kwryqg4ZI0Mvm1yChP6gRHotprhX5Q5KXWpJAuMWu-jebZSdVYucOnrWNEK6eh_VTN1or_89rWjNi561IsfmOaEklCLkfreyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cda0441500.mp4?token=IQ-9TSgo002kQhYqLbs3oj7FF0FRh4NTEumGB1laM2oaCnb9LB2ImPQ69qj0iUK-dS1pIVtGU8aLgMgIycZOetkgobBecZ45XnxUo-EbWoWpwCQzWdv_8dxYZ8ErZUEXxvRkA9i4CnDvi0BwxvvUAoYQH5MqeUq5uriv1e4UxsPN82uhkTfaVoR7ozacAhBMjwhVNJjlnZW0jH4EGkwdBbkh_dtcwPLv7q31T5ZlFmLGTkbKPPTV3Kwryqg4ZI0Mvm1yChP6gRHotprhX5Q5KXWpJAuMWu-jebZSdVYucOnrWNEK6eh_VTN1or_89rWjNi561IsfmOaEklCLkfreyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان لوله لول سر میز شمام
😂
@withyashar</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/withyashar/11209" target="_blank">📅 14:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11208">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا:
تأسیسات اصلی بارگیری نفت ایران به مدت ۳ روز است از سرویس خارج شده است
@withyashar</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/withyashar/11208" target="_blank">📅 14:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11207">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خبرنگار صداوسیما به نقل از نیروی دریایی سپاه: از شب گذشته تاکنون ۳۰ فروند کشتی از تنگه هرمز با مجوز ایران عبور کرده‌اند
@withyashar</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/withyashar/11207" target="_blank">📅 14:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11206">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">شی جین‌پینگ: چین و ایالات متحده هر دو از همکاری سود می‌برند و از تقابل زیان می‌بینند.
دو کشور ما باید شریک باشند نه رقیب.
@withyashar</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/withyashar/11206" target="_blank">📅 14:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11205">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ از رئیس‌جمهور چین برای سفر به ایالات متحده در ماه سپتامبر آینده دعوت کرد
@withyashar</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/withyashar/11205" target="_blank">📅 14:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11204">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">آکسیوس: یکی از گزینه‌های ترامپ پس از بازگشت از چین از سر گیری پروژه آزادی در تنگه هرمز است. گزینه دیگر  ترامپ حمله به زیرساخت‌های ایرانه.
@withyashar</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/withyashar/11204" target="_blank">📅 14:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11203">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">طبق برنامه ای که قرار داده بودیم   ترامپ و رییس‌جمهور چین برای یک مهمانی شام با یکدیگر دیدار کردند @withyashar</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/withyashar/11203" target="_blank">📅 14:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11202">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24c3a9a1e.mp4?token=su9SzGzJWXtRsKbsXAoW4naYH0axvpyrSwYwZnLwdfpwJehXCwdwq3AaxMQfeiIIgZhKAWVYXxybTgRQXFsY5PH04AMipvC9dPHWjzVpu7Owchs-xPwjH5jMGbsjNddpFNmr19zGTDfgrgMZMYP0dKAUKRrvOV8wPPyg6e3vXo_zCgX4Z8HuuhVer63XR-_3lFE2pm1Jc5wGA_9lwhugAIi1fqXob_Cy6fEnKXoRJzhgZpATtXcyoFSK7PmelhJjADJ5XJsl6OYkJQMQ4oDWqqRCn5MAKiPE-Ewj96gz5eSw1ee8XgZpL9GZVucoK3qZOpkP4fWzm8fmWvMtpCJTRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24c3a9a1e.mp4?token=su9SzGzJWXtRsKbsXAoW4naYH0axvpyrSwYwZnLwdfpwJehXCwdwq3AaxMQfeiIIgZhKAWVYXxybTgRQXFsY5PH04AMipvC9dPHWjzVpu7Owchs-xPwjH5jMGbsjNddpFNmr19zGTDfgrgMZMYP0dKAUKRrvOV8wPPyg6e3vXo_zCgX4Z8HuuhVer63XR-_3lFE2pm1Jc5wGA_9lwhugAIi1fqXob_Cy6fEnKXoRJzhgZpATtXcyoFSK7PmelhJjADJ5XJsl6OYkJQMQ4oDWqqRCn5MAKiPE-Ewj96gz5eSw1ee8XgZpL9GZVucoK3qZOpkP4fWzm8fmWvMtpCJTRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه های ترامپ با حاکم چین به این ترتیبه : مراسم استقبال تو تالار بزرگ خلق چهارشنبه رسیدن به پکن ، استقرار و استراحت پنج شنبه ۱۴ مه - ملاقات با شی - ضیافت دولتی با شی  جمعه تاریخ ۱۵ مه - جلسه عکس با شی- چای با شی - ناهار با شی و حرکت از پکن به آمریکا، @withyashar</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/withyashar/11202" target="_blank">📅 14:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11201">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/withyashar/11201" target="_blank">📅 14:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11200">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">فارس:
عبور کشتی‌های چینی از تنگۀ هرمز از شب گذشته اغاز شده
@withyashar
یک کشتی ژاپنی هم اجازه عبور گرفت</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/withyashar/11200" target="_blank">📅 14:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11199">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کاخ سفید اعلام کرد در دیدار ترامپ و شی جین‌پینگ، دو طرف بر باز ماندن تنگه هرمز و تقویت همکاری‌های اقتصادی توافق کردند. این توافق شامل افزایش سرمایه‌گذاری چین در صنایع آمریکا و گسترش دسترسی شرکت‌های آمریکایی به بازار چین است.
ترامپ: مذاکرات پکن بسیار مثبت و سازنده بود
@withyashar</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/withyashar/11199" target="_blank">📅 14:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11198">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">با رفیق اروپاییم نشستیم داریم ویدیو مسیج های شما رو نگاه میکنیم براش ترجمه میکنم که داری چی میگی، بعد یهو میگه اینجا چی گفت، خب من چجوری گربه گیر رو ترجمه کنم
😂
😂
😂
😂
😂
عشقی سلطان یاشار
❤️
❤️</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/withyashar/11198" target="_blank">📅 13:54 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11197">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahdi</strong></div>
<div class="tg-text">با رفیق اروپاییم نشستیم داریم ویدیو مسیج های شما رو نگاه میکنیم براش ترجمه میکنم که داری چی میگی، بعد یهو میگه اینجا چی گفت، خب من چجوری گربه گیر رو ترجمه کنم
😂
😂
😂
😂
😂
عشقی سلطان یاشار
❤️
❤️</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/withyashar/11197" target="_blank">📅 13:51 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11196">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e51a90e1f.mp4?token=coZ6lSiCzrW-ZcORmRwF6UJ3iP0EO__LkIjsF8a4ajVAdepO0IIL85JWxqY-YWTV-Mr4gxSM66uinbZc0sRtm2DIkiXvdXPst3mlSYBsuDExbEKtmxg1gzxAHGWb3lQF1tuyWho9QiAKtQFL0xAv4eqltYxrmbRdcjBKTbKHbctkajtQKBzm2EtGT_ykij40XySt78OWqAIzXd5zGmLK0EUlanJG1EnfYOYvggwkVy43Cxm3lToPLmqIN0JbSSpoCiPQLGMMCvjoHVv_MQa_ck8PIXvAFXxKh3WEB8LKnfnwqWgPlHZFIdWI1Eg2JIMFDXvvi_5igwRzEMqZDDqc_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e51a90e1f.mp4?token=coZ6lSiCzrW-ZcORmRwF6UJ3iP0EO__LkIjsF8a4ajVAdepO0IIL85JWxqY-YWTV-Mr4gxSM66uinbZc0sRtm2DIkiXvdXPst3mlSYBsuDExbEKtmxg1gzxAHGWb3lQF1tuyWho9QiAKtQFL0xAv4eqltYxrmbRdcjBKTbKHbctkajtQKBzm2EtGT_ykij40XySt78OWqAIzXd5zGmLK0EUlanJG1EnfYOYvggwkVy43Cxm3lToPLmqIN0JbSSpoCiPQLGMMCvjoHVv_MQa_ck8PIXvAFXxKh3WEB8LKnfnwqWgPlHZFIdWI1Eg2JIMFDXvvi_5igwRzEMqZDDqc_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/withyashar/11196" target="_blank">📅 13:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11195">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اتاق جنگ با یاشار : جابجای‌های غول آسا دو شماره یک «AirForce1» هواپیمای ویژه ریاست جمهوری و «B1 »بمب افکن اسطورهی آمریکا و خبر ویژه از داخل ایران  https://www.instagram.com/reel/DYQCr39RJ4i/?igsh=MThycjJiYWZmbnJ3dA==  کارای اداریش رو انجام بدید تا بعدش بریم…</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/withyashar/11195" target="_blank">📅 13:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11194">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آکسیوس به نقل از مقامات اسرائیلی:
در پی احتمال تصمیم ترامپ برای از سرگیری جنگ، در اسرائیل حالت آماده‌باش حداکثری در طول تعطیلات آخر هفته برقرار خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/withyashar/11194" target="_blank">📅 13:08 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11193">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یک مقام کاخ سفید به فاکس‌نیوز:
رئیس‌جمهور چین علاقه‌مند است نفت بیشتری از آمریکا خریداری کند تا وابستگی کشورش به تنگه هرمز را کاهش دهد.
@withyashar</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/withyashar/11193" target="_blank">📅 13:08 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11192">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">جان بولتون: مذاکره با ایران برای یک توافق هسته‌ای هدر دادن اکسیژن است.
این افراد دهه‌ها پیش تصمیم استراتژیکی برای دستیابی به سلاح‌های هسته‌ای گرفتند و در این ۴۷ سال هیچ مدرکی وجود ندارد که نشان دهد آن‌ها این هدف را رها کرده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/withyashar/11192" target="_blank">📅 13:07 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11191">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f2c74f17.mp4?token=VvaxPow0VMGG7cWDMUtb1bUfKwsEXYsDs8REwc74eCQf4Gdg1rf6sOVJKR15KEIWRg7jb1YfCa8P_opJ0J9Vjk2o3QZuoOczEFBCsezWfZvZsd5rD09TYjYnx40l43mh1isY_9FtidrjThJxLgR5APOJbEIseMoxzdwaAoWSwUULZdKb7feOQM3Dfau8VvBVOcGyfU7-OcWR2CTbnHDi55MHVHcoWSNBBqB_A2uVvccphj5ZzEPeV3HB5jpV3etHXvQ4AXchrZqM4uGM_2ueKk23x21hGOMZAEatEWgTF5wo2m1Go8ufXUq4Ims_5Je2AHqBD3mFRyK2mwNTZSKjVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f2c74f17.mp4?token=VvaxPow0VMGG7cWDMUtb1bUfKwsEXYsDs8REwc74eCQf4Gdg1rf6sOVJKR15KEIWRg7jb1YfCa8P_opJ0J9Vjk2o3QZuoOczEFBCsezWfZvZsd5rD09TYjYnx40l43mh1isY_9FtidrjThJxLgR5APOJbEIseMoxzdwaAoWSwUULZdKb7feOQM3Dfau8VvBVOcGyfU7-OcWR2CTbnHDi55MHVHcoWSNBBqB_A2uVvccphj5ZzEPeV3HB5jpV3etHXvQ4AXchrZqM4uGM_2ueKk23x21hGOMZAEatEWgTF5wo2m1Go8ufXUq4Ims_5Je2AHqBD3mFRyK2mwNTZSKjVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ بعد از ۵۰ سال، اولین رئیس‌ جمهوری شد که به معبد آسمان چین رفت
@withyashar</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/withyashar/11191" target="_blank">📅 12:48 · 24 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
