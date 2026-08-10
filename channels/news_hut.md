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
<img src="https://cdn4.telesco.pe/file/hgaNMQBLNoko9mWJVnqLLwyR8FdM8ThgUeBqvkki8BOD2SOK1A5hBY-cLbCQn6kbM16gYQqJLnChyTzOav-4mxgbfIgQuS9LSBir7lNNTdVkjGZJGubKlB2cud-vIfSljPc63J7hyw_uGzFccZdWxSoCB1xIoTQySCA3sTMJk4FGTNwQ745vHQsC48b7zi2VOHdwwvAcd2hJKokgl2a7wC6p8FPg6CTp1sM1CwGUFbpZCCroX6MkPYADInKVkIqaYRznXiGXQpexTr5lnyjI437OfUYi8_vpaISchRgMMFFR-rk5xMwYz4PK76j9yUv4X6kPIyIWq1V55DX4n1Y_VA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 129K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 13:24:39</div>
<hr>

<div class="tg-post" id="msg-69837">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d242d991d.mp4?token=rPAkqv-3x05ZThgtJvl2TYoAHLsCew5xlsipPPExJIV7EWU6FKSJJ90Z7yazBHnRppbEtK6dO-GXQwUdAKryHY02-7Hx4zuBAFgbyzvlNS0Xvy8NFW5mG2M_wkq_GqHL0y4UZfI6fjGKjz5iphDr2YDGqSrLEFDeHWaTKVgjcPf82dpFz6VPZrUA2rPh_ubrFQR75N3ytFYNNakuD51CCzEQME8C0yn1tr-PxOm77NM_OZXC70lcwN5aCQGKcSxSYU3WOCZOsJBIqg_ucSvpTOvPt78Sd04evlXeircccqSU-ZJbTkjddul5XVRYbp29s8KqRPGYpq-sZZJnAfSPKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d242d991d.mp4?token=rPAkqv-3x05ZThgtJvl2TYoAHLsCew5xlsipPPExJIV7EWU6FKSJJ90Z7yazBHnRppbEtK6dO-GXQwUdAKryHY02-7Hx4zuBAFgbyzvlNS0Xvy8NFW5mG2M_wkq_GqHL0y4UZfI6fjGKjz5iphDr2YDGqSrLEFDeHWaTKVgjcPf82dpFz6VPZrUA2rPh_ubrFQR75N3ytFYNNakuD51CCzEQME8C0yn1tr-PxOm77NM_OZXC70lcwN5aCQGKcSxSYU3WOCZOsJBIqg_ucSvpTOvPt78Sd04evlXeircccqSU-ZJbTkjddul5XVRYbp29s8KqRPGYpq-sZZJnAfSPKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فوران یک آتشفشان قدرتمند در جنوب غربی کلمبیا
@News_Hut</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/news_hut/69837" target="_blank">📅 13:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69836">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81027c9c4b.mp4?token=tbGcqSd53OT5sHIMu4M0nAqij47iE3bm_H9rmcmhRF5dDZP3-lcV9NWhCqyVz9ltuM2vbYQKddPFwKrhoezjaUrnHQqh6b0pfgBRrExxRLQBXuXhgV9HgbdW53jaCwOKk662E_FD8dzxydun0UkxqsnPfZpvp4xTVV4c15ylQxXFWtHSeT5fZPvf5wELZX15ER79k1xo2z1R9y31OgEZHo6PxYbgTGQoHQ8-_E6urkfsu9NaGt1OtB16WEHrtrdlobDOI1qbRwU30i3zYAYJWgdf6mtEG8twbI47faUHrhU3uyQ7qr1RPv5hm2uUG8d165IBY-wO7BHupSrbBxSHuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81027c9c4b.mp4?token=tbGcqSd53OT5sHIMu4M0nAqij47iE3bm_H9rmcmhRF5dDZP3-lcV9NWhCqyVz9ltuM2vbYQKddPFwKrhoezjaUrnHQqh6b0pfgBRrExxRLQBXuXhgV9HgbdW53jaCwOKk662E_FD8dzxydun0UkxqsnPfZpvp4xTVV4c15ylQxXFWtHSeT5fZPvf5wELZX15ER79k1xo2z1R9y31OgEZHo6PxYbgTGQoHQ8-_E6urkfsu9NaGt1OtB16WEHrtrdlobDOI1qbRwU30i3zYAYJWgdf6mtEG8twbI47faUHrhU3uyQ7qr1RPv5hm2uUG8d165IBY-wO7BHupSrbBxSHuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشتیبانی سنگین و فوق العاده از نیروهای زمینی آمریکا در جنگ افغانستان ( طالبان ) توسط بالگرد آپاچی ۶۴ با توپ ۳۰ میلی متری M230 Chain Gun
@News_Hut</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/news_hut/69836" target="_blank">📅 12:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69835">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ea33d827b.mp4?token=QQmIszP4ZkbNfK9mdXODMiMxYbgJZtgx98UvVYiGEX0jbidFKJIbN1ci4aADHxcmql7b6M42KPxZjqx-16O-a3aKxgtlolcwkzlyrvE-fhFO5WveAcnO4dNwPqarR4NDUenAt7-ByagJ6_Y-nMAGmjnV8oOz5J22ADHQwQWXP4wHH1gzi_dJn0ortzDNNNJ53fINPtQWnUiyqI4a6npNZ7RoiBO8mB0NoSAqwK3NpUEzU2wp2xHEvMLF11diBphXKSpSUeeZub_dNbkJV4A7ppvJcpO-j-W20SNsbK6C6Wnwb6Lq2SjGYPEwY-ytE-PWzLTex1hzP182ZCq0KANAKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ea33d827b.mp4?token=QQmIszP4ZkbNfK9mdXODMiMxYbgJZtgx98UvVYiGEX0jbidFKJIbN1ci4aADHxcmql7b6M42KPxZjqx-16O-a3aKxgtlolcwkzlyrvE-fhFO5WveAcnO4dNwPqarR4NDUenAt7-ByagJ6_Y-nMAGmjnV8oOz5J22ADHQwQWXP4wHH1gzi_dJn0ortzDNNNJ53fINPtQWnUiyqI4a6npNZ7RoiBO8mB0NoSAqwK3NpUEzU2wp2xHEvMLF11diBphXKSpSUeeZub_dNbkJV4A7ppvJcpO-j-W20SNsbK6C6Wnwb6Lq2SjGYPEwY-ytE-PWzLTex1hzP182ZCq0KANAKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پرستار از اتفاق عجیب شب زفاف یه زوج میگه:
ساعت ۴ صبح یه خانم با خون‌ریزی شدید به اورژانس منتقل شد و اول فکر کردیم
سقط جنین
اتفاق افتاده، اما بعد مشخص شد مربوط به
شب زفاف
بوده.
خون‌ریزی اون‌قدر شدید بوده که مجبور شدن بیمار رو
جراحی
کنن.
⏺
پرستار توصیه کرده زوج‌ها برای اولین رابطه عجله نکنن و با آرامش و احتیاط پیش برن تا به این روز نیافتن
.
@News_Hut</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/news_hut/69835" target="_blank">📅 11:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69834">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53aa49426e.mp4?token=En1Z16W3ceQw1DrnI_5XYBZg52qkJgoqUWqOpwsKdVYXTRSDwvtrYQjIjBNGpAoLumBFVk5RrxazBfGEi_w9ObtIQm1gX8bOE-hhc8vFBn0znyEKqL6UXl6gk1VH8gJa7Wtb2uvzYM2iYe2McpkLsPn_3plAhwYWGVMxSvFmw8mt-XEyyafzoCXuN5-WfHf0EM-GO5u-ZQ-13iVhbRlzoAHDZJWIK9JIhXAgX93qLL0fpJt5aXIH7UaTB7wfec0tjtFeDcUVYvAm0GpCSASVQyZGj9vCQtFCKka0r0OIZliYmH38sVOm-WDEOwkbfU0nHym7ASFDnUvwpdEL8V9dWTaR5otlsSZqIqAVW3pkbJoWCvXjVvaVEY1QLIorpwURr56PJY9J0i9HKoAQpHkM4zEZP5PK9uUTiFGG9jT_voiVj42KEwmO_tX3FpPlQT0tMDUswZXMOAN-iib0ye8SBjMkYm2tvxyz53B9mDpXXwa2t-k8dZRdEVMkTGQRVVx3K_2cNVyFEbZhqPlaAsr22__EcWKpmyj61iyaiP3cDYQ41ADgZbtmZ0N__IWAZvXcOzbYAVf-NQ3hXA-SyfC4P6PKq44WxWkPPVJj-JoADfMcLeqWqA4qgIAfDhOWCN-e3HdiO4xe2SJhzP4q7fyo4Wj_ue11kKdAZSDgzSNc_HM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53aa49426e.mp4?token=En1Z16W3ceQw1DrnI_5XYBZg52qkJgoqUWqOpwsKdVYXTRSDwvtrYQjIjBNGpAoLumBFVk5RrxazBfGEi_w9ObtIQm1gX8bOE-hhc8vFBn0znyEKqL6UXl6gk1VH8gJa7Wtb2uvzYM2iYe2McpkLsPn_3plAhwYWGVMxSvFmw8mt-XEyyafzoCXuN5-WfHf0EM-GO5u-ZQ-13iVhbRlzoAHDZJWIK9JIhXAgX93qLL0fpJt5aXIH7UaTB7wfec0tjtFeDcUVYvAm0GpCSASVQyZGj9vCQtFCKka0r0OIZliYmH38sVOm-WDEOwkbfU0nHym7ASFDnUvwpdEL8V9dWTaR5otlsSZqIqAVW3pkbJoWCvXjVvaVEY1QLIorpwURr56PJY9J0i9HKoAQpHkM4zEZP5PK9uUTiFGG9jT_voiVj42KEwmO_tX3FpPlQT0tMDUswZXMOAN-iib0ye8SBjMkYm2tvxyz53B9mDpXXwa2t-k8dZRdEVMkTGQRVVx3K_2cNVyFEbZhqPlaAsr22__EcWKpmyj61iyaiP3cDYQ41ADgZbtmZ0N__IWAZvXcOzbYAVf-NQ3hXA-SyfC4P6PKq44WxWkPPVJj-JoADfMcLeqWqA4qgIAfDhOWCN-e3HdiO4xe2SJhzP4q7fyo4Wj_ue11kKdAZSDgzSNc_HM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایشون هم اینطوری انتقام قتل حمیدرضا رجب‌زاده رو گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/news_hut/69834" target="_blank">📅 11:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69833">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48e95fc990.mp4?token=gMNSLpPY5lZzOYBt8Tmes5GaczRNVGQfCsEjvuiv2pWALv0_Ph4KAgmkUO50kWF0ZKGG5uHIZdNNXJB9rROrvSU8nvZVhoujOi1Q1-KcIU0dz3pGBmTDPq5ngS3jACEuLSmlXNNq_X95SXm9RScBWyZiELRZNjKkq-Fvb5BM6AhAmrEx8jfBesRsHeVsME9NzNMK7n9t_CTcLPCHQC49xPIUUD80gpyAgB_k8Awsj2wcVE1pOr4qj0xEPBYK7_1NvMiWlp4N9AfdeLNDf0hFF3gMozm3Xvbbg0t4nACwo5s1fCsOknKr4e7sGm0dEu6uTfKhZ7Cc-L1kfs9nvi2Sfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48e95fc990.mp4?token=gMNSLpPY5lZzOYBt8Tmes5GaczRNVGQfCsEjvuiv2pWALv0_Ph4KAgmkUO50kWF0ZKGG5uHIZdNNXJB9rROrvSU8nvZVhoujOi1Q1-KcIU0dz3pGBmTDPq5ngS3jACEuLSmlXNNq_X95SXm9RScBWyZiELRZNjKkq-Fvb5BM6AhAmrEx8jfBesRsHeVsME9NzNMK7n9t_CTcLPCHQC49xPIUUD80gpyAgB_k8Awsj2wcVE1pOr4qj0xEPBYK7_1NvMiWlp4N9AfdeLNDf0hFF3gMozm3Xvbbg0t4nACwo5s1fCsOknKr4e7sGm0dEu6uTfKhZ7Cc-L1kfs9nvi2Sfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دریک، از بزرگترین خواننده‌های دنیا؛
با 140 میلیون فالور و ثروت 250 میلیون دلاری [50 هزار میلیاردی]
وقتی ممه‌های بزرگ یه دخترو دید، نتونست تحمل کنه و براش هاپ هاپ کرد
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/69833" target="_blank">📅 11:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69831">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d3c25ee1.mp4?token=eTViVL0FvSG-oafPDDr3TZqDiarBMuH4tXJM5iHd77x_ixPNfRablcvBuXP5RJ9uEmFK4mc1WEVohaVuU61WUip03atvR5LCFt1XTEuJA6mLzVtbSzM7FZfAofdtwKUZDBupzBEif90uWmwvY7tFHkiX8VvcUty5BREj9MNwqz2vXxbWOikebFQXo-ghFtu-DIuvcb3Osqy28659NLVMXX7KB05jg8oVqBBRyXf4MylkFQFsR9abg-I41sycivQlTHxDmwkR1-YaJa9uy0C97SZS6hAd7smvOcWoRyegTK3yTo727_RasDA3Xlvm1i9aqJJzTKX7GBUKrUVDz5Ol82A-dNyZtPqc-9rHFoh02DM3H4XeosEwMyFa8SBynNySGpLFMlph3iGAAsCk98cufxHBoCWQdMuCuI8E9mUjjsVbsYydLYu1Ez3M4PTeWMZwyElYGBzmo0igytQeZCKTrFgQRRusUryWmJbjobf6MBRChLnP6d7_DBvpQaHfUS0X4DMfC-Q6l-k00V9S6TvRdv44CiWsLBCpO_lDIbJEzmdPNXy9Lgc49QjOsLPANVAM6K2xQBkBE37vZafuTGZC4JcdRacfG51dwbAGeSKwCWAq3EPoIujIcpnhGcyH1hVekMwVD9pwLr4yeBpPxCkSvgW9oYVaGkCoi-dPttqritE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d3c25ee1.mp4?token=eTViVL0FvSG-oafPDDr3TZqDiarBMuH4tXJM5iHd77x_ixPNfRablcvBuXP5RJ9uEmFK4mc1WEVohaVuU61WUip03atvR5LCFt1XTEuJA6mLzVtbSzM7FZfAofdtwKUZDBupzBEif90uWmwvY7tFHkiX8VvcUty5BREj9MNwqz2vXxbWOikebFQXo-ghFtu-DIuvcb3Osqy28659NLVMXX7KB05jg8oVqBBRyXf4MylkFQFsR9abg-I41sycivQlTHxDmwkR1-YaJa9uy0C97SZS6hAd7smvOcWoRyegTK3yTo727_RasDA3Xlvm1i9aqJJzTKX7GBUKrUVDz5Ol82A-dNyZtPqc-9rHFoh02DM3H4XeosEwMyFa8SBynNySGpLFMlph3iGAAsCk98cufxHBoCWQdMuCuI8E9mUjjsVbsYydLYu1Ez3M4PTeWMZwyElYGBzmo0igytQeZCKTrFgQRRusUryWmJbjobf6MBRChLnP6d7_DBvpQaHfUS0X4DMfC-Q6l-k00V9S6TvRdv44CiWsLBCpO_lDIbJEzmdPNXy9Lgc49QjOsLPANVAM6K2xQBkBE37vZafuTGZC4JcdRacfG51dwbAGeSKwCWAq3EPoIujIcpnhGcyH1hVekMwVD9pwLr4yeBpPxCkSvgW9oYVaGkCoi-dPttqritE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی شبانه به مجموعه‌ای از اهداف در سراسر روسیه و سرزمین‌های اشغالی حمله کردند.
پهپادها مرکز خرید گالاکتیکا در ماکی‌یوکا، که قبلاً مرکز منطقه‌ای بود و در سال ۲۰۱۴ توسط نیروهای روسی تصرف شده بود، را به آتش کشیدند.
آنها همچنین پالایشگاه نفت در نیژنکامسک، تاتارستان را هدف قرار دادند، در حالی که روسیه ادعا کرد ۱۵ پهپاد در نزدیکی مسکو سرنگون شده و عملیات فرودگاه را مختل کرده است.
طبق گزارش‌ها، حملات پهپادی باعث قطع گسترده برق در ملیتوپول، بردیانسک و دونتسک شده است، در حالی که انفجارها و آتش‌سوزی‌هایی در سواستوپول و کرچ گزارش شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/69831" target="_blank">📅 10:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69830">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69830" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/news_hut/69830" target="_blank">📅 10:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69829">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=rwgRWaNaGx4XA7ZfyAOTy0V1jNGwpH4jolTzD4puVq2Kc42eKHwEi-x5eeSlIUqoZ961WDwIWG8KdTwM4NI9E0p7118NzDFlMca0-Su3FZv2d80DNAY92u-vhqpa03Xa33DPMaMOy-KR8Dmf1kenZRDSecSUnjBcwBTuBjWYJSsMgrrfytM369HCpcUdIQ0JfpOHh6QNKeWKgz0iVMPiPa53rXZ3mb5IMEixokJjCZtFOoPOaJK9BPQTimnoKrhoLK0CcVCg6GOV3BHQpJ2YgGKEDWQzm_L0Zp9Sdx9I8ovnudDrpvHMchDeukSUF74o4eFKkiqqN5_QnSXkYu4Aqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=rwgRWaNaGx4XA7ZfyAOTy0V1jNGwpH4jolTzD4puVq2Kc42eKHwEi-x5eeSlIUqoZ961WDwIWG8KdTwM4NI9E0p7118NzDFlMca0-Su3FZv2d80DNAY92u-vhqpa03Xa33DPMaMOy-KR8Dmf1kenZRDSecSUnjBcwBTuBjWYJSsMgrrfytM369HCpcUdIQ0JfpOHh6QNKeWKgz0iVMPiPa53rXZ3mb5IMEixokJjCZtFOoPOaJK9BPQTimnoKrhoLK0CcVCg6GOV3BHQpJ2YgGKEDWQzm_L0Zp9Sdx9I8ovnudDrpvHMchDeukSUF74o4eFKkiqqN5_QnSXkYu4Aqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
r19
@betinjabet</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/news_hut/69829" target="_blank">📅 10:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69827">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOrIUiCg1IO2cbdmPEolU6nYYTbKRy_ytvK9qaCKhMRULf0_wxPII4bmsWOLGRP0pTTtxdYMO_ESxJjYyzluaWng4lT63neKx4JXbznKLLQ2prYBLS1JqePUehNpt5YNcF-fES_InaEFKFm1eO6i8rEGqXKBpJRm2v0wkPe6cuaCvBTEkwLzwneP_dDON2FvrRJU9Yse-SaBbLcf3nkqyB6KgHrVKnHQj7beuvRz9XKk8WWf6E6yAlQsPSfPk7bkJSJLy8RwWu4bbXiEaOWP_vGacVaQ2jzh-yB9VEz0pBCMX_sBHo3mhCKKB7MZd09STzCdaSEj28Pm9ClUDZ3ikA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
شرکت آمریکایی BlackSea از پرتاب یک پهپاد FPV از روی قایق بدون‌سرنشین GARC خود رونمایی کرد
؛
این شرکت اعلام کرده است که با استفاده از تجربیات به‌دست‌آمده از جنگ، استفاده از پهپادهای FPV هدایت‌شونده با فیبر نوری را پیشنهاد می‌کند.
محفظه‌های پرتاب این سامانه قادر به حمل پهپادهای FPV در اندازه‌های ۵، ۷ و ۱۰ اینچی هستند؛ پهپادهایی که از نمونه‌های FPV مورد استفاده فعلی روسیه و اوکراین کوچک‌ترند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/69827" target="_blank">📅 10:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69826">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4c36a2172.mp4?token=gbg9WJT6sz1_2aixdFoa4iRrvC3lJOjc8AqYWL_NMPmecZo1UpSl1TXmjRXVxYPqfXmixKG-sMVTtIdIoNRYwBq7a1p0Ua4gpySrTZjeYEiREHw6sPXsd9B1KoZxd5TZCZxDO7Ei-orWNogq4WMjPgXmRvHZeKRwBf4R8yyTfyVwaoNThNk9Upmdl-UgTDdbtXndL3TArNZMl6ldXykD2A2JW8SEgAh3x00nqvqz_FgxSQUBGyhm2w8-g7WKChfnIpbOvXlzwZtVjYGE5cfRlHDNH6HIX3RJkB1BgZaLzDwATofiQEKkPLBHbe9luAv-FsBmyvDmgywXPTncD2VOrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4c36a2172.mp4?token=gbg9WJT6sz1_2aixdFoa4iRrvC3lJOjc8AqYWL_NMPmecZo1UpSl1TXmjRXVxYPqfXmixKG-sMVTtIdIoNRYwBq7a1p0Ua4gpySrTZjeYEiREHw6sPXsd9B1KoZxd5TZCZxDO7Ei-orWNogq4WMjPgXmRvHZeKRwBf4R8yyTfyVwaoNThNk9Upmdl-UgTDdbtXndL3TArNZMl6ldXykD2A2JW8SEgAh3x00nqvqz_FgxSQUBGyhm2w8-g7WKChfnIpbOvXlzwZtVjYGE5cfRlHDNH6HIX3RJkB1BgZaLzDwATofiQEKkPLBHbe9luAv-FsBmyvDmgywXPTncD2VOrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
جهانگیر، سخنگوی قوه قضائیه:
آخوند خرازی، بابت صحبتاش تحت تعقیب قرار گرفته و به دادگاه ویژه روحانیت احضار شده.
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/69826" target="_blank">📅 10:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69825">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🟡
📰
مراد ویسی تحلیلگر ارشد اینترنشنال: «جنگ بزرگ در خاورمیانه، برای سرنگونی جمهوری اسلامی است.»
⏺
پرسش این نیست که کدام زودتر می‌رسد؛ پاسخ روشن است:
جمهوری اسلامی سرنگون شود، مردم ایران به یک حکومت عادی می‌رسند.
جمهوری اسلامی سرنگون شود، نیابتی‌ها خشک می‌شوند.
صدام رفت، یک کانون تهدید در خلیج فارس از بین رفت — کانون دوم هنوز باقی است.
خلیج فارس می‌شود منطقه‌ی صلح، ثبات و توسعه؛ چون امارات، قطر و عربستان دنبال توسعه‌اند و ما هم دنبال جبران خرابی‌های جمهوری اسلامی.
ثبات منطقه از تهران آغاز می‌شود، نه از میز مذاکره.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/69825" target="_blank">📅 09:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69824">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdd241cc6.mp4?token=IDy_MP9sjUkJI2Mu9ve4Ihy1cIiKO8hymb2A9j8IaclwzkEtc_Pr9iceBv6zS4KHvEOUeQFpjTUWwgp7kQzuHLHZgp13Pqm4KeDt7tmSKr7BYNc-dlIUXihBUgeb0yrjeMOPMO5C7ZK8vEh-_-gDSeacwPgMtdGiHiCm9t2ftpUQzdL5Z3WTtLWWEVKiowWdduMtMTw2CdGb8Jmfir_gL9Yktclgr9Gs5KKjaisUNxf9cDEsK4qCmlxQevcDWDDegBd0a2cPyNs0NL3TAfLc7PqvTzNCZgTcvZSXRMT-CZ4td_CQJgcJ7x3Gq-OPYJiyJLMlRszwvjP6q4Cpd2BvVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd241cc6.mp4?token=IDy_MP9sjUkJI2Mu9ve4Ihy1cIiKO8hymb2A9j8IaclwzkEtc_Pr9iceBv6zS4KHvEOUeQFpjTUWwgp7kQzuHLHZgp13Pqm4KeDt7tmSKr7BYNc-dlIUXihBUgeb0yrjeMOPMO5C7ZK8vEh-_-gDSeacwPgMtdGiHiCm9t2ftpUQzdL5Z3WTtLWWEVKiowWdduMtMTw2CdGb8Jmfir_gL9Yktclgr9Gs5KKjaisUNxf9cDEsK4qCmlxQevcDWDDegBd0a2cPyNs0NL3TAfLc7PqvTzNCZgTcvZSXRMT-CZ4td_CQJgcJ7x3Gq-OPYJiyJLMlRszwvjP6q4Cpd2BvVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یکی از نفس‌گیرترین ویدیو های منتشر شده از جنگ؛لحظه بمباران شریعتی تهران!
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/69824" target="_blank">📅 09:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69823">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69823" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#بازی_پولساز
⚠️
🔥
بلک کارت جدید ترین بازی معروف جهانی هست که فقط کافیه یکمی باهوش باشی تا حریفات رو شکست بدی
👌🏼</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/69823" target="_blank">📅 02:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69822">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6c003ee1.mp4?token=X-4qSlha0JrFoPLquYa39K20mwOW97yyB85QAa25Lc4TmjM0gT680SUEL0SC1-DBnBTcl86huza6QWBPaIAaMqYx_FcemPd1spNW9SSKsTNz_cxKHLdx8wGA6KBOjcUjaEOaGZzrM8xezzU29xeKcYPvTnmMwqqzFAp9qFJKtDu95MNT3bAU6dEt1ed23PJ1e2Ai-B94IDbIcUKxwnRQs5LOvOnh5m2itRWBKAZ7zxLEKtQkLxmYl_X7gIyVMq1cjD-l5PHf5vE8MEUDmhmKZp48dv682KHA3Wm6PV_PhB1cabkuOxI7xEXraiMMZNKI3l9Udw00NLS-XS5aUiMA5DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6c003ee1.mp4?token=X-4qSlha0JrFoPLquYa39K20mwOW97yyB85QAa25Lc4TmjM0gT680SUEL0SC1-DBnBTcl86huza6QWBPaIAaMqYx_FcemPd1spNW9SSKsTNz_cxKHLdx8wGA6KBOjcUjaEOaGZzrM8xezzU29xeKcYPvTnmMwqqzFAp9qFJKtDu95MNT3bAU6dEt1ed23PJ1e2Ai-B94IDbIcUKxwnRQs5LOvOnh5m2itRWBKAZ7zxLEKtQkLxmYl_X7gIyVMq1cjD-l5PHf5vE8MEUDmhmKZp48dv682KHA3Wm6PV_PhB1cabkuOxI7xEXraiMMZNKI3l9Udw00NLS-XS5aUiMA5DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😯
اگر هوشت بالاست
🗼
:
❌
👍
این ‌ویدیو‌ آموزشی رو‌ ببین و با ‌استفاده از هوش بالایی که داری پول در بیار.
🟢
بازی خیلی حرفه ای و‌
#پولساز
رو‌ از این ویدیو یاد بگیر
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
a18
@betinjabet</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/69822" target="_blank">📅 02:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69821">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:  اگه ایران از این به بعد به هر کشتی‌ ای توی تنگه هرمز شلیک کنه، فرقی هم نداره با موشک، پهپاد، راکت یا هر سلاح دیگه‌ای باشه، آمریکا در جوابش یه پل یا نیروگاه برق ایران رو میزنه حتی اگه نزدیک تهران یا داخل خود تهران باشه.  @News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/69821" target="_blank">📅 01:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69819">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAalZDk8Wivp1rb54E8kcJ5VThVJ22LOTeEUOU6S6b3hnxtsvmSn_B3-2ZTka-p_FWhjDAN2Kzgdy1T-2gmjvj_nM-MD1RZ3prV_JkuDQ2LpIU7g5QK648_O1TWbn4QeQeJuKXPEqgTnd19gsyKdoDHyp8zPWZyVZ_c1VI9BKpCEfSWslM2OmHvurPdkyKBtkhcqGSbWr3OzXfTHv6LAYhX9NXR46g7266VYxYsGQ6K10fkyaey8Pv5gGYmR1K7_obWoK70-xuzLr9jdJdHeHcVxQHXwVK-cfHGRS-E0b_Aw2oG4y7Mg1v-zlKrM5QARaQ5LjU3XMdDMs8ynS0J65A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94eb35c039.mp4?token=mW-Ug_57wgUgDXLmyxDw5O-XYxVhA7S-igS2Uw8G5blNg6qF1slO0nlysQkLM1dBIBED87BiUSMu4HpQDaK93Ht1ITqiREbpCcbcWciFlpdVdpjM6Tvq6mf9bsllZOcuz3ZtEqx9ABTDUFH1WXJ40N-AlHbFSpA3f6EoOS0bson78KFXYO4vbCn6hFptWkKq60cfyhUtt5CggELQnGwvhkmpcipRbChjSjhAbgNThtP4sRmPL8Pf7p8FHV4D0xz7jcp3zj6X44dSrRItBrfUSn9MIsK1eDSLqAooeiOTLvMPWcX4nlz94x5C4bwfvxXIj0QN2ktWGIvsZJejn336FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94eb35c039.mp4?token=mW-Ug_57wgUgDXLmyxDw5O-XYxVhA7S-igS2Uw8G5blNg6qF1slO0nlysQkLM1dBIBED87BiUSMu4HpQDaK93Ht1ITqiREbpCcbcWciFlpdVdpjM6Tvq6mf9bsllZOcuz3ZtEqx9ABTDUFH1WXJ40N-AlHbFSpA3f6EoOS0bson78KFXYO4vbCn6hFptWkKq60cfyhUtt5CggELQnGwvhkmpcipRbChjSjhAbgNThtP4sRmPL8Pf7p8FHV4D0xz7jcp3zj6X44dSrRItBrfUSn9MIsK1eDSLqAooeiOTLvMPWcX4nlz94x5C4bwfvxXIj0QN2ktWGIvsZJejn336FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇨🇳
🇸🇦
یک پهباد ساخت چین متعلق به نیروی هوایی عربستان سعودی در آسمان جنوب کشور سرنگون شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69819" target="_blank">📅 01:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69818">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLT9nOrd8oXIU_faWtHmZjybtQspThvfagr1bJ6Mz7vLPjD22JbPLGvocevoaJIwo_o9_4A0LmWPRuG93DXuxQQ99b_uyNTKb27rGQU_8KszyHYoFcO0Mll5MMpWtIp_xPxHpOqVCb1oQrBrJeeixFgbTu-misf0uZHupwa7ofJHeWr5PiaWBkHkLqVs6L5V_fD6xIRSID2cO7_ls0CRWeoO3PLhGDmkiv9N5pr3R1tpXp4U6rGV8-WaT6AC88dP6WDeu79DkgaA_7b3LYPleBWoEjNCSZP9I05sUkqvzuM7navhV0YnRFDRwLKfa0CmGyGC27qBxKu0VZu5eX0QGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در تروث سوشال:
51سال رفتار نامناسب!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69818" target="_blank">📅 00:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69817">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dbf391292.mp4?token=bfCMG8yW2sTsgJURA_fWZSbxtIbSOY2gOvciXoy1ijZKWHga1b57d2qRVJj3VI1_8p3eWvUxmwyOrjGWsTi87A7BRBK4dh6HpvHDTc3VnHSLYwmajVssr3-ivGaJxmrB0-eA6UqQ7061WiycMrKXcNT8fjc8eaI-nQLs3lqIdIbKpt2eU7EkBpouU7JaVqGgX6pD1M7BnslhjhHanHuy89u_1-6ZaOARw1CbvvFLRLBLEE_7lUGE7OgTJE7qK8_l4ME44Y_mMCmhtJgzcOdm2avbXucw6Fs8PNwJnRplJcAmervmLZxNDCxoOOKmVpSSiegl7aq2KU1yIVgNGoeMiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dbf391292.mp4?token=bfCMG8yW2sTsgJURA_fWZSbxtIbSOY2gOvciXoy1ijZKWHga1b57d2qRVJj3VI1_8p3eWvUxmwyOrjGWsTi87A7BRBK4dh6HpvHDTc3VnHSLYwmajVssr3-ivGaJxmrB0-eA6UqQ7061WiycMrKXcNT8fjc8eaI-nQLs3lqIdIbKpt2eU7EkBpouU7JaVqGgX6pD1M7BnslhjhHanHuy89u_1-6ZaOARw1CbvvFLRLBLEE_7lUGE7OgTJE7qK8_l4ME44Y_mMCmhtJgzcOdm2avbXucw6Fs8PNwJnRplJcAmervmLZxNDCxoOOKmVpSSiegl7aq2KU1yIVgNGoeMiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
آتش‌سوزی یک کشتی در پی حمله سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69817" target="_blank">📅 00:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69816">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🇮🇷
سپاه‌پاسدارن یک کشتی را در تنگه هرمز هدف حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69816" target="_blank">📅 00:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69815">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec1565ac0.mp4?token=jHZN-e5Ju2bc8KZ04rUEH7DfSIT_gGf1QZ9vdY_FvTsl0kPcNDBhq0SHBfJdftjclz5_wZD3t_2oR4493RGl1KbJtTCKEa8KiZkkmHY71CrtiUi-eTzkCr0h83yJY1kA1I1CCAh4q99lIUX3UgnJkx-8DRMsmCBHwAB1GYNgIijyGsLlue6CP8htGoiSUwvgiXm9FpsjHIGIEluCsaGRlzRbRoOl7ACgRBLM3xIgh9RdGRJFHRy5MbI7oaPM8QpB_g885ANHJozWhnx-RKNLfKhwhyoiVIHrMDbf0tVOwdowzvE6TVXD8t_gb7RXHnAd0jJ6wdlRfVAUCQ1QEXPJsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec1565ac0.mp4?token=jHZN-e5Ju2bc8KZ04rUEH7DfSIT_gGf1QZ9vdY_FvTsl0kPcNDBhq0SHBfJdftjclz5_wZD3t_2oR4493RGl1KbJtTCKEa8KiZkkmHY71CrtiUi-eTzkCr0h83yJY1kA1I1CCAh4q99lIUX3UgnJkx-8DRMsmCBHwAB1GYNgIijyGsLlue6CP8htGoiSUwvgiXm9FpsjHIGIEluCsaGRlzRbRoOl7ACgRBLM3xIgh9RdGRJFHRy5MbI7oaPM8QpB_g885ANHJozWhnx-RKNLfKhwhyoiVIHrMDbf0tVOwdowzvE6TVXD8t_gb7RXHnAd0jJ6wdlRfVAUCQ1QEXPJsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو وایرال شده از یه پسرِ جوون تو تجمعات شبانه:
به ابالفضل راضی‌ام جنگ زمینی‌ بشه، یه تنه 500 نفرشون رو حریفم!
ایشالا روزی بشه مکه و فلسطین رو آزاد کنیم.
ایشالا روزی برسه آمریکا رو نابود کنیم و تو کاخ سفید نماز بخونیم.
نیاز به بسیجی‌ها نیست همین بچه‌لات‌ها اسرائیل رو میگیرین داداش...
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69815" target="_blank">📅 23:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69814">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b396273688.mp4?token=jmFmCWdcFVtwtiIUSxeffNfjPqKpuZ8IA1HyfWUMtgbR1_YeY9jqMjdYcuJt6d5NZZopNzabRLY6BTdgMyCdKpf4a8wT_m_fMzVtuYiaP2OK2buxL12VkLWAX6Hz2MHpDnd1YfUjl8C3x63r_uyx_Mvl4owhkysZ_2ZrksFzAXzKOVePPcuOElCso7czis6dt3RhipEj30OsZQvJKnKwbZIKCSzNWg1VdHShvVad4oNjhLsDcr87oJTI3-vfv2PkfvKHpTJhom4bG3mTo_naQCJKvmGOdK4j0WOMcYAEaxEJbPIwnZGdQSQrb6Y14dRtkd3houmsVCPKz7YJrZAidgivB0W60gy8TW4wxsJt4QFMX0qQGpCL2vDvqJT5-fCPqCVT7qKBiblU7L465vH957DOR5QUYMVOzUYYWX2r-aczAH0N5lJKOd_GD7fnF3yEEwJ0tVSBQHNeHk7mjqWaqMm160IRVjKoHQXJeKdXgpd4WqURjoifhZDrjB-gy_ZHUKD3TN2Ov6rG9hTTC4LW5RSCsBwyRgeQcF63uIroIfltJeM3iTrHPk5kV8qYz17TH_HzFVIRHS2n5JuexwfOVBwrdDTUgv4Z33i_JD8OwbHaAeKqKB3vNYKRgLCWVEb5bkQ5u8tDpKPP_pzl94bzvxKi5isNF9R3QCoalfOGrQ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b396273688.mp4?token=jmFmCWdcFVtwtiIUSxeffNfjPqKpuZ8IA1HyfWUMtgbR1_YeY9jqMjdYcuJt6d5NZZopNzabRLY6BTdgMyCdKpf4a8wT_m_fMzVtuYiaP2OK2buxL12VkLWAX6Hz2MHpDnd1YfUjl8C3x63r_uyx_Mvl4owhkysZ_2ZrksFzAXzKOVePPcuOElCso7czis6dt3RhipEj30OsZQvJKnKwbZIKCSzNWg1VdHShvVad4oNjhLsDcr87oJTI3-vfv2PkfvKHpTJhom4bG3mTo_naQCJKvmGOdK4j0WOMcYAEaxEJbPIwnZGdQSQrb6Y14dRtkd3houmsVCPKz7YJrZAidgivB0W60gy8TW4wxsJt4QFMX0qQGpCL2vDvqJT5-fCPqCVT7qKBiblU7L465vH957DOR5QUYMVOzUYYWX2r-aczAH0N5lJKOd_GD7fnF3yEEwJ0tVSBQHNeHk7mjqWaqMm160IRVjKoHQXJeKdXgpd4WqURjoifhZDrjB-gy_ZHUKD3TN2Ov6rG9hTTC4LW5RSCsBwyRgeQcF63uIroIfltJeM3iTrHPk5kV8qYz17TH_HzFVIRHS2n5JuexwfOVBwrdDTUgv4Z33i_JD8OwbHaAeKqKB3vNYKRgLCWVEb5bkQ5u8tDpKPP_pzl94bzvxKi5isNF9R3QCoalfOGrQ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خرازی:
این کلیپ ها جعلی و هوش مصنوعی است؛
من این حرف‌ها را نزدم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69814" target="_blank">📅 23:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69812">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1fdc25902c.mp4?token=QqG_6UlDzGCbV-lHWzeJS_BycqdVSePLrPt2thJZH42ndtAleMmod2G9FEPooDHgKoki_6eaWW62EXCJeO8ax-ljxrkpe7M3YyDGTKjXP-kU6N5PYDqa_71MLCmDXNQTwZoGjBu8Kg1snPdg-3wDPYE7PZb6rjsy9IHmG768s_P_3rzLgQgdykTyYaPL3BfbTCrDYOU7o_bKVDNQ2hA6XzNmz1noBasOZGQz3I2fLoLOQ6MIYu3T_35rCP7xTMbdy_gtCuwVxSN21VKRCvsEO65occzbyx8Rzwo1ULiP48nHMDmfVaaRN8BA0ipcJ7GSv7YS1WrRze2hzTyR47cHBg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1fdc25902c.mp4?token=QqG_6UlDzGCbV-lHWzeJS_BycqdVSePLrPt2thJZH42ndtAleMmod2G9FEPooDHgKoki_6eaWW62EXCJeO8ax-ljxrkpe7M3YyDGTKjXP-kU6N5PYDqa_71MLCmDXNQTwZoGjBu8Kg1snPdg-3wDPYE7PZb6rjsy9IHmG768s_P_3rzLgQgdykTyYaPL3BfbTCrDYOU7o_bKVDNQ2hA6XzNmz1noBasOZGQz3I2fLoLOQ6MIYu3T_35rCP7xTMbdy_gtCuwVxSN21VKRCvsEO65occzbyx8Rzwo1ULiP48nHMDmfVaaRN8BA0ipcJ7GSv7YS1WrRze2hzTyR47cHBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه ماجرای عجیب و تلخ که زندگی یه ورزشکار رو زیر و رو کرده
این بنده‌خدا یه ورزشکار ۱۳۰ کیلویی بوده، پرس سینه می‌زده و از بهترین راننده‌های جرثقیل هم بوده؛ ولی یه ماجرای مهریه کل زندگیشو زیر و رو کرده...
همسرش مهریه رو می‌ذاره اجرا و حکم جلبش صادر میشه. وقتی مأمور برای دستگیریش میاد، فرار می‌کنه و مأمور هم به کمرش شلیک می‌کنه؛ گلوله باعث میشه قطع نخاع بشه.
حالا با وثیقه آزاده، ولی هنوز داستان تموم نشده؛ همسرش گفته فقط یه هفته وقت داری، وگرنه دوباره باید بری زندان!
از یه آدم سالم و ورزشکار، رسیده به این وضعیت...
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69812" target="_blank">📅 22:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69811">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🇺🇸
وقوع یک حادثه امنیتی در نزدیکی باشگاه گلف ترامپ در شهر بیدمینستر، ایالت نیوجرسی؛
فرماندهی دفاع هوافضای آمریکای شمالی (NORAD) دو فروند پهپاد را که حریم هوایی محدودشده بر فراز بد‌مینستر، نیوجرسی (Bedminster, NJ) در نزدیکی باشگاه گلف ترامپ را نقض کرده بودند، رهگیری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69811" target="_blank">📅 22:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69810">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgwFKpIHtlzeXzT82CB7DZdji1huTDYpsxxZmZBH_FGIc488NWWvwRmOLYQGa2JSs1qeGPtsg80yXolxt181SuLJBFRUdUJBtICug_7ZNr0zKa5pgwOxiHJaAFcfZ2lrxw7RZ5se6I2KKpzpGP53pd1RDq7dfx7yGTMn_QXwIDbkKqoGVVFRJdeFqaUMlVMBupAwYd7NEERM1ksjmflyATiRBjN-o79VtWccNEZ4KeA6YKOo25CzhAEcnyRej1-xftNtYewjSFK3_YdVphqdaNqj41PCQtvX6IUslsW2Fuj9TuwLfQ06TCJvXMPPLOYXuUlG_qxeNhRqRYekMugb3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
با حکم مسعود پزشکیان محسن رضایی رسما دبیرکل شورای عالی امنیت ملی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69810" target="_blank">📅 21:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69809">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
یه فلسطینی به زور بچه شو میفرسته جلو سربازای اسرائیلی، بهشون میگه شلیک کنید بهش!
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69809" target="_blank">📅 21:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69808">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmncPrG5mHce104jBLxS2X2l5oIom3p0Hu7ASxwvdAAF5N4LpYFxmJSbNDafS1a64wD_Nj_VAgFKGvGBZG12ekidRLgn7YT47M25hjkDN2xliKYm9HpOtvf8BdA7wAKzsN5dQNsZdm0hhVwJ1BjjTW2Og3WscEvX5nBBrhe5PLIRR1kK9GQArFubb7dtp6XaebkCcgqQzIJ7zppMYwYnZNZdksoINnInf0ovgukQY-tZ2y3jJ4nkb4masltZ8ovKWVhshmBwXeUaYPdVydpqgWk_npExatlk6fumBfGhFaBRsGx4i8-m5y3Poy2obC6Yz8IkRfw4qL4CEApqNLnGzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
🇺🇸
اکسیوس به نقل از ترامپ:
ایالات متحده در رابطه با ایران «بی‌سروصدا» عمل می‌کند، که نشان می‌دهد واشنگتن فعلاً از اقدام نظامی عمده جدید خودداری می‌کند و در عین حال اجازه می‌دهد فشار اقتصادی افزایش یابد.
ترامپ با این استدلال که ایران از نظر اقتصادی «در وضعیت بسیار بدی» است و در حالی که محاصره دریایی ایالات متحده فشار را تشدید می‌کند، برای پرداخت حقوق سربازان خود با مشکل مواجه است، گفت: «این [مشکل] حل خواهد شد. همیشه حل می‌شود. مثل یک بازی شطرنج است.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69808" target="_blank">📅 20:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69807">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🙂
لحظه کمیاب واژگونی کوه یخ غول‌پیکر در سواحل گرینلند؛
ویدئوی ثبت‌شده در ۲۵ ژوئیه ۲۰۲۶لحظه واژگونی یک کوه یخ عظیم در سواحل گرینلند رو نشون می‌ده.
با تغییر مرکز ثقل بر اثر آب شدن یا جدا شدن تیکه‌های یخ، این توده‌های عظیم برای رسیدن به تعادل جدید می‌چرخن.
در این فرآیند، بخش‌های آبی‌رنگ و شفافی که میلیون‌ها سال زیر آب فشرده شده بودن، برای لحظاتی در معرض دید قرار می‌گیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69807" target="_blank">📅 20:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69806">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1384fab4ec.mp4?token=dpGM_-RvfpSWzTEUt4_t27903OkYhy_980ofaDEU8R_8hZI9mOajR_pVbv5QyUsMCsmYJQ1dntm4WdMJQAma75U80k8TmktacnVDItonvh0p5cUbJRF4AxT8nifTq9WUhNax2lb36sqmyRtxCSrrwLikqN3ZZtLAD1yREU1dV6_a18wHIpo1anIFRynqUsxDd8hubgQ_SQY3ICPPvB7sYxu07HxoEmLq4cTBDKzXd3y-VU8fKV6--9zpQ1fuAEqhw-1tOuGAu9tTFOIFezBittavKD7vQ4XLoFguD3xoYCOaOMdqDKXKiZSSRNyvolJqskde_bt9DHwQZsd5H6pVVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1384fab4ec.mp4?token=dpGM_-RvfpSWzTEUt4_t27903OkYhy_980ofaDEU8R_8hZI9mOajR_pVbv5QyUsMCsmYJQ1dntm4WdMJQAma75U80k8TmktacnVDItonvh0p5cUbJRF4AxT8nifTq9WUhNax2lb36sqmyRtxCSrrwLikqN3ZZtLAD1yREU1dV6_a18wHIpo1anIFRynqUsxDd8hubgQ_SQY3ICPPvB7sYxu07HxoEmLq4cTBDKzXd3y-VU8fKV6--9zpQ1fuAEqhw-1tOuGAu9tTFOIFezBittavKD7vQ4XLoFguD3xoYCOaOMdqDKXKiZSSRNyvolJqskde_bt9DHwQZsd5H6pVVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
طرفدار حکومت در واکنش به کشته شدن حمیدرضا رجب‌زاده:
شما زدین مبارک شما ما زدیم مبارک خودمون
خدا سرشاهده جرائت دارید بریزید خیابون
یجوری تیکه تیکه تون بکنیم یجوری ریش ریش بکنیم شما رو تاریخ تو خودش ندیده
به جان امام شهید قسم به جان رهبر مجتبی قسم شما رو با کارتک از وسط خیابون جمع خواهند کرد
جنازه شماها رو میدیم سگ ها بخورن
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69806" target="_blank">📅 19:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69803">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PxwWh7QponTpuggkzwx_0IdNqszDbqiW-kjQ4kntDjt7teANDQQmgTACuK9P4AitOtITDZvtlqs72w3OErhavFcNdRLyv1RHp3mqQGtamYOnP4-2QKaV6TrDtCy_KakAj_fJZIZH4urTo6Ht5rqrJESHD5xOg5gVLYCb9sseVKyidexPmodvBNHxP2S0qrYic_5DcOiMbI6-4C6n3TKKBXRkpxLsqFKTSfQF-WNSxEjSJSbfunUAqITxpZHjocBTgHiVeblALtQzMzcZoH4L9Nujwfp9BIsTgOWq70nTVrFSDXDYSnITMfXZFj1VnupA_i2M7_ANW93gvIU6cVq1Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PhO51RDwKyjJilJ9-FcugYsvlbwpG3GQVJV_x-YdQE4rpVvaGfspMjNvCKg-SI-BAOqu7a1B0kqeKKQIUO0HCZv4KgM-5sgjQD0mJ6UbFCM28CmF0EiOOvlN7WwYBN3VSdp3dSG4EXsx3tlmHhszSxtC0_gimJa42PQVYx7jjBTGxvCjyF_clL91xvtU_R9rQQsarz_UMsqmsLTaKCda7omSVPZHQQqCEg3D66kJsM6X2hqjHSmA2wpEGGtrQMZLFqTX4NVQSFuQWu21iUaKCxMpNLnvia69M6twmDcJ2KFbvy6FS4crE85P6sZDmKny2fcGq1KM67A5kwJM3ip5yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bAFUVAs7ZSIZFnEL50U6ugeESfwRNY4zdalV5Oc_BZuzezf4oYVpJln7Yiwy4PwQ7yzYNX-7KZJ9xNcqZsCvqWvgq_lizsvRqv13pTtOpxij9iBr-gr7gEZd7cOgdozSFRCMVVKZa3vfEhPCCz3G8-Dz8Hr3Ag9QJeHxmLUdYqCtgLKKkpoKkd38Kq953tu6X3Ag4mR32hEL2TLRmR5pcFv20QcWP6qeB2zXtKyLGvLYVN-KQidABMztaTIvlfRGaEcFPmH9eAyxo2GOnlV_cbfDFbaXpRy6M4dbkd1Ff0oRlpK0L4DMZx87IRlbZTiT-i03iDFbtBp66nU_hsfI1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ریورز یکی از مشهورترین فمنیست ها که زن رو برترین موجود میدونست و خودشم علنا لز اعلام کرده بود با یه پسر خوشگل و پولدار رفت قاطی مرغا
☺️
☺️
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69803" target="_blank">📅 19:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69802">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0cbb95dc3.mp4?token=jTOpibOZJDRcDdpfIRWZ9qm8IngDC4ubchT1mTSGDWASrf74zYGt2H01hyH1GVbGsAzXxEVhWkWpDJCTKBF2utphdkWAgBSgoVhc0hcGZ8JT30PVqpfChpjggOZEyn2eVNaG8Wf0lby_qr-LY_kjq_7Mm57jyzrkYqyFRkoD1i2bA1gVuuKp1VFjfTzVUtvn4OKQxACLFXE3VXQzXok_d7x7VQUHQ_0K08BiN8DrF5TM9vOlsbWvJXBn2rT3ME0GoXF_YNnf3TqQj6bgwnrrluIrpyTHbWJDNIZouOfHV78-rpQPo7IjeVCnLF9onTaWnV4DDthp0967UTa73W-UGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0cbb95dc3.mp4?token=jTOpibOZJDRcDdpfIRWZ9qm8IngDC4ubchT1mTSGDWASrf74zYGt2H01hyH1GVbGsAzXxEVhWkWpDJCTKBF2utphdkWAgBSgoVhc0hcGZ8JT30PVqpfChpjggOZEyn2eVNaG8Wf0lby_qr-LY_kjq_7Mm57jyzrkYqyFRkoD1i2bA1gVuuKp1VFjfTzVUtvn4OKQxACLFXE3VXQzXok_d7x7VQUHQ_0K08BiN8DrF5TM9vOlsbWvJXBn2rT3ME0GoXF_YNnf3TqQj6bgwnrrluIrpyTHbWJDNIZouOfHV78-rpQPo7IjeVCnLF9onTaWnV4DDthp0967UTa73W-UGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
یک فروند پهپاد بدون سرنشین جنگی (UCAV) نیروی هوایی ایالات متحده از نوع MQ-9A Reaper که از فرودگاه چابلی برخاسته بود، در نزدیکی گورستان چابلی در جیبوتی سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69802" target="_blank">📅 19:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69801">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">پول درآوردن از بت دقیقا جاییه که فرق استراتژی داشتن و ادعا داشتن رو مشخص میکنه
👌
15 بازی 15 برد
✅
من به پول شما نیاز ندارم و چیزیم به شما نمیخوام بفروشم g18 لینک چنل https://t.me/+_btGj-rRAxs3NGVk https://t.me/+_btGj-rRAxs3NGVk</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/69801" target="_blank">📅 19:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69800">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7tPTKa_Bidi3-7kwY9Nt7n76PUha8ZPveqm9NVnvRSnc5Qb8Pz385gEZUm2gMj6hU9jkO7FM2iOlpCsulb8MrnaTVwQGmQKsD9Ckw-KjqQeK5SC-b2ruWaTLYnoro8Tf8IuhrZ6t6if7KyegOKLS-rZ_Jmp1EXUhXf3TvQ6R1UQh7XVzn8ZwO-o93HDYSml2lxelOvRQBiKmp0eEEEKBkSxIcANz-ab0PI2sPdlLq7tdtws8-bqzKwWJDgXFckDm1tSayBtFdgipnnajxvYFwdYHyRpiYWAc4E2zCcmK-64lb6aHELgx3aCIoMKXrTpp9RzRJRzWQcw7g6JkvN3Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پول درآوردن از بت دقیقا جاییه که فرق استراتژی داشتن و ادعا داشتن رو مشخص میکنه
👌
15 بازی 15 برد
✅
من به پول شما نیاز ندارم و چیزیم به شما نمیخوام بفروشم
g18
لینک چنل
https://t.me/+_btGj-rRAxs3NGVk
https://t.me/+_btGj-rRAxs3NGVk</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/69800" target="_blank">📅 19:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69799">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411943761d.mp4?token=jKHf1UPk-ukrTGEIcht31d9Yu4D1amAuUjpaxz9xY0BsA6wObzsSV_hn7tH9yYA5z3bwePhf1f8vhk_Ln6NwCeRHkfUpZWkwZzxZndAgBuJ6uFNjfpRk1wv1tlMddM_NDM6SaaeC4-Orq-HfRXpurvmhG-uG2qQqVEszdm4myPm_h4zixDH_6WngGJwTRh0RYQxx2sCIsvVLanrIzE2azr_RRIcMKSkzRsrKvvCsNeUk9DwWLTc1VVhdhVkm5sEbkFj7UCHJcsB8mkMdE3tVdlfGMcCFJ_S_pk7T6OS1P3b89gTWLQuf2ho8B7yy9o7SNhFBI5CAkim2rTSP87Bq2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411943761d.mp4?token=jKHf1UPk-ukrTGEIcht31d9Yu4D1amAuUjpaxz9xY0BsA6wObzsSV_hn7tH9yYA5z3bwePhf1f8vhk_Ln6NwCeRHkfUpZWkwZzxZndAgBuJ6uFNjfpRk1wv1tlMddM_NDM6SaaeC4-Orq-HfRXpurvmhG-uG2qQqVEszdm4myPm_h4zixDH_6WngGJwTRh0RYQxx2sCIsvVLanrIzE2azr_RRIcMKSkzRsrKvvCsNeUk9DwWLTc1VVhdhVkm5sEbkFj7UCHJcsB8mkMdE3tVdlfGMcCFJ_S_pk7T6OS1P3b89gTWLQuf2ho8B7yy9o7SNhFBI5CAkim2rTSP87Bq2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
آقای پزشکیان بچه‌ها یه شوخی باهاتون کردن راجب درختی که میخواستید بکارید توی پاکستان، برامون بگید قضیه چی بود؟!
🇮🇷
مسعود:
من فیلم بلد نیستم بازی کنم.
اینکه الکی یه خاکی بریزی و بگی من درخت کاشتم پس تو نکاشتی.
ما نایب رئیس بودیم توی تبریز باید ده تا درخت میکاشتیم همشو خودمون کاشتیم.
ما کشاورزی میکردیم، همین الان اگه برم مزرعه خودمون بیل رو میگیرم کار میکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69799" target="_blank">📅 18:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69798">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0eb6125750.mp4?token=WMUjWT51G07CG1vsyrpmOPiNh0XuF292ms4p_P5YqTq8KFewrVEjcZFkv0wE0McSCDEjch4FnQeh6nMoek8ndn2fI3sEC6PDDAbH_tp2kSlxI2l18NFX94Y-GygBT54Q9lOaCNXkd1ogHp9_clwbnLXi4GvBC7-0Sfqkv3MguEUkwDB3lsCP6QhjRw4Npv0r9fj5Qjm4_DH-mzgcgBYuUPuhNrcBIxG96AwVXrtut1udVSxCT1JjVSbjBqlxz_VHYKZKpiYJESt8f0nxP97MlD1tvMz94FT403zmshRJccr2yfgGV9CJAoHMk-DMpYyag-cTvrUBQ7rlL2TT-ZGnhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0eb6125750.mp4?token=WMUjWT51G07CG1vsyrpmOPiNh0XuF292ms4p_P5YqTq8KFewrVEjcZFkv0wE0McSCDEjch4FnQeh6nMoek8ndn2fI3sEC6PDDAbH_tp2kSlxI2l18NFX94Y-GygBT54Q9lOaCNXkd1ogHp9_clwbnLXi4GvBC7-0Sfqkv3MguEUkwDB3lsCP6QhjRw4Npv0r9fj5Qjm4_DH-mzgcgBYuUPuhNrcBIxG96AwVXrtut1udVSxCT1JjVSbjBqlxz_VHYKZKpiYJESt8f0nxP97MlD1tvMz94FT403zmshRJccr2yfgGV9CJAoHMk-DMpYyag-cTvrUBQ7rlL2TT-ZGnhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخشی از مستند«پسرملا» روایتی از چند سال آخر زندگی روح‌الله زم:
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69798" target="_blank">📅 18:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69797">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
📰
وال‌استریت ژورنال: دونالد ترامپ، رئیس‌جمهور آمریکا، از چند هفته قبل برای اعلام پیروزی در جنگ با ایران آماده‌سازی‌هایی انجام داده است.  او به مشاوران ارشد خود گفته است که در صورت بازگشایی کامل تنگه هرمز توسط تهران، می‌تواند این درگیری را بدون دستیابی به توافق…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69797" target="_blank">📅 17:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69796">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVxno7dpNWnY3OYhdlIkvukSi-z7UDpGo1f5KYnTQsAythq0G-vw4xbNxgYhyDHadPzX2-9Ig90iPkwiKBL0Bpauf7RtXF4sPAANZ65oTCrL0xi4TK62acYAOE3o5B3-UtVfItA6Nge4w5E_rk3Tpj1Bmtv_XqLVKD5CJ0g2Yuu1xPqywXn8_Gw_KdFdE-UQWH-Z-VMjygl4dQkh3jXqpTRT4ZEwUfAnBzK8XDBznfiOc75fHPUkzvWMkobb3a-dfg5mR57w_aqwtqlqmBRW5mnJXfuMvqEDbgucnnj-jsZsrSZrWoiI4kmLF5aWkj3BsvN9zjAbIEJ8xSSNxniODA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
📰
وال‌استریت ژورنال: دونالد ترامپ، رئیس‌جمهور آمریکا، از چند هفته قبل برای اعلام پیروزی در جنگ با ایران آماده‌سازی‌هایی انجام داده است.
او به مشاوران ارشد خود گفته است که در صورت بازگشایی کامل تنگه هرمز توسط تهران، می‌تواند این درگیری را بدون دستیابی به توافق هسته‌ای به پایان برساند.
ترامپ معتقد است که ایران احتمالاً در طول دوره ریاست‌جمهوری او، برنامه هسته‌ای خود را از سر نخواهد گرفت، به ویژه پس از اینکه آمریکا سال گذشته سه مرکز هسته‌ای بزرگ را بمباران کرد. مقامات آمریکایی می‌گویند که اگر واشنگتن بتواند فعالیت‌های هسته‌ای تهران را کنترل کند و ترافیک تجاری از طریق تنگه هرمز از سر گرفته شود، ترامپ احتمالاً تمایل بیشتری به تمدید آتش‌بس فعلی به طور نامحدود و رفع محاصره بنادر ایران خواهد داشت.
مقامات آمریکایی اعلام کرده‌اند که ترامپ همچنان مایل است تا در این بن‌بست دیپلماتیک جدید صبر کند، به ویژه زمانی که قیمت بنزین نسبتاً ثابت و در حدود 4.02 دلار به ازای هر گالن باقی مانده است، در حالی که سال گذشته این قیمت 3.16 دلار بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69796" target="_blank">📅 17:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69795">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa7b5af888.mp4?token=T7hoDAsCq9Qviek2hfJVzGHmYZOlfU5NSsSebaT-ywgSHNDBxaMZTlSVifBEbI-Ivkv_FGZnlkz3_OVYxd40aGkYDpPMhVX9AJuTAOBFwg1m32-UwP41C8o0koxG-uAQ6N6keJkieaiO1FC47Wk7s68PVgQ81AHQeeb1wJpHGR5DoZ2ECZmZ6HOPefdTocyjQ6BQVouWKxQsJK53yAix_jXlYBMJCWks5pbTeYRNuUud0w_jlwKpMz3m_djo3ldJWguiyM9fO-YPz75UkEHybd2MV_6xn9MH9UpmcwTYIhuiCJ6z5ZlzVj6sHc-wjtHKhPePB_J6oF-4RSehxKYeHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa7b5af888.mp4?token=T7hoDAsCq9Qviek2hfJVzGHmYZOlfU5NSsSebaT-ywgSHNDBxaMZTlSVifBEbI-Ivkv_FGZnlkz3_OVYxd40aGkYDpPMhVX9AJuTAOBFwg1m32-UwP41C8o0koxG-uAQ6N6keJkieaiO1FC47Wk7s68PVgQ81AHQeeb1wJpHGR5DoZ2ECZmZ6HOPefdTocyjQ6BQVouWKxQsJK53yAix_jXlYBMJCWks5pbTeYRNuUud0w_jlwKpMz3m_djo3ldJWguiyM9fO-YPz75UkEHybd2MV_6xn9MH9UpmcwTYIhuiCJ6z5ZlzVj6sHc-wjtHKhPePB_J6oF-4RSehxKYeHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تصاویری از یک پهپاد تهاجمی اوکراینی که به طور موفقیت‌آمیزی سه بار متوالی، موشک‌های پدافند هوایی زمین به هوا از سیستم "پانتسیر" روسی را در دریای سیاه جاخالی داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69795" target="_blank">📅 17:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69794">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">⏺
معاون برق و انرژی وزارت نیرو:
خاموشی‌ها در مناطق عادی ۲ ساعت یا کمتر است و مناطق گرمسیر به دلیل شرایط خاص، از تخفیفات ویژه برخوردار هستند.
همچنین برنامه داریم تا یک تا دو هفته آینده، محدودیت‌های برق را به حداقل برسانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69794" target="_blank">📅 16:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69793">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3f5dd815.mp4?token=HJMQKtL9aPe-S0PWDnU2AIfHNMaGbr8IJ7krIx1zt1l64_uT9Grx-1xAwq4nGgy3WeaVDxUSfCGmQHyU9oXfRTcqi775KadQsbd4HC_lLPjYiutXiJuKi9Yud2ZTq77t5E6f7lSttVW5_-628CvOew09Rro_ETy_sR1xqZYsgj9CR2GHKXP8z1nV6RpRBdA5l-SftU8DZ1j5eI50ngWMgGG2xt3wTGfvK_pcdD3mJrj-DcHcWc-VKSax0BgIf9ngLsjvG65Uy6LKtA-txaxf4-lQhSOhKQqJ6FSm_X-sFAhmCj9mm6nAKSjtjl-bVx3xhDSfOMcUtfLn6ub5xGbJL6QnA4dndPrf_qfM-86bKLwxrprY7cQzFt7mkx-KfQKh-P4nki2H0OjLh98LXo9EXL78ana3640r1lEqospMoiFUMQwfqwVduObUVSeFNEMHGIRy6-Oy20lwdDjoFxzwyAQe7OejzYFIsxP6fHHqHjE9IOVgMkuRYNCXIBVUTtJdfrCyL2gjUAymQ1d_vwq-j8MR_klKN_Eh0paEaw3KPlAttjw0h4rOgD74XbZ1rRdTrf5EaBzQ4Xl5b93InC5HHgKJbhmk0ACqC9hAgioPId2MkW9KagQM4TMDnMSJ5NaI-YM0f6sdGDUAgC4a3IjmVL2HFlGhxOEz53ss4kNcdFo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3f5dd815.mp4?token=HJMQKtL9aPe-S0PWDnU2AIfHNMaGbr8IJ7krIx1zt1l64_uT9Grx-1xAwq4nGgy3WeaVDxUSfCGmQHyU9oXfRTcqi775KadQsbd4HC_lLPjYiutXiJuKi9Yud2ZTq77t5E6f7lSttVW5_-628CvOew09Rro_ETy_sR1xqZYsgj9CR2GHKXP8z1nV6RpRBdA5l-SftU8DZ1j5eI50ngWMgGG2xt3wTGfvK_pcdD3mJrj-DcHcWc-VKSax0BgIf9ngLsjvG65Uy6LKtA-txaxf4-lQhSOhKQqJ6FSm_X-sFAhmCj9mm6nAKSjtjl-bVx3xhDSfOMcUtfLn6ub5xGbJL6QnA4dndPrf_qfM-86bKLwxrprY7cQzFt7mkx-KfQKh-P4nki2H0OjLh98LXo9EXL78ana3640r1lEqospMoiFUMQwfqwVduObUVSeFNEMHGIRy6-Oy20lwdDjoFxzwyAQe7OejzYFIsxP6fHHqHjE9IOVgMkuRYNCXIBVUTtJdfrCyL2gjUAymQ1d_vwq-j8MR_klKN_Eh0paEaw3KPlAttjw0h4rOgD74XbZ1rRdTrf5EaBzQ4Xl5b93InC5HHgKJbhmk0ACqC9hAgioPId2MkW9KagQM4TMDnMSJ5NaI-YM0f6sdGDUAgC4a3IjmVL2HFlGhxOEz53ss4kNcdFo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو:
به یک نکته جالب توجه کردید که ایران به همه منطقه حتی فرای منطقه حمله کرد جز اسرائیل؟
تا الان به ما حمله نکرده ممکنه تو آینده بکنه ولی میدونه جوابش چقد سنگین و دردناک میشه.
شایعاتی هست که اسرائیل عقب نشینی کرده و ضعیف شده.
این شایعات از کسایی به ما روانه میشن که میگفتن اصلا نباید عملیاتی توی لبنان و ایران بکنید.
لازم باشد بخاطر منافع ملی به بزرگ ترین دوستانمان نیز نه خواهیم گفت.
منفعت اسرائیل رو پایبند به هیچ توافقی نخواهیم کرد و ما مستقل هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69793" target="_blank">📅 16:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69792">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef1f7ed1d6.mp4?token=YYDxX8dGgvrp-14gd3y43y9jyMi0J4xtSR3PpglgoWV4L2T3JS1llfbWEZoJsWcGLrU6LRtmjwpybEDu24rlnxOPaOUBWVYVtMYFUgDfFspg41tCdEX6lTJ2yNyFpFSIEJ4gofcYtq1liCkMjD2xBXJAvWvhvkDGp2dUZzUEfRf2MjtGcJSsQN-9icJdTI_3NC0hDVQVbRQ_SwnE0K1y0JkMPHELRlryMPLaLhWDPxnsrDPvYK1eRok4rg1oYXOWY8LbXC-bRh8jEfDIpWhX8H449U3KGUk1tKU6pjuIyy8eWf5Hl6gXgiWIaOJbNRh1S964z6MDLxy9qJ42ZxiRWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef1f7ed1d6.mp4?token=YYDxX8dGgvrp-14gd3y43y9jyMi0J4xtSR3PpglgoWV4L2T3JS1llfbWEZoJsWcGLrU6LRtmjwpybEDu24rlnxOPaOUBWVYVtMYFUgDfFspg41tCdEX6lTJ2yNyFpFSIEJ4gofcYtq1liCkMjD2xBXJAvWvhvkDGp2dUZzUEfRf2MjtGcJSsQN-9icJdTI_3NC0hDVQVbRQ_SwnE0K1y0JkMPHELRlryMPLaLhWDPxnsrDPvYK1eRok4rg1oYXOWY8LbXC-bRh8jEfDIpWhX8H449U3KGUk1tKU6pjuIyy8eWf5Hl6gXgiWIaOJbNRh1S964z6MDLxy9qJ42ZxiRWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت آمادگی جانفداها:
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69792" target="_blank">📅 16:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69791">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26df8fab5.mp4?token=NzkmIUAERO83HMWptUxSOGE1mRmDd72A_mG88IBCkpwNuCCPwL4obCL7KMPV9465dpJsEhnj4ienOS1kbjSYmkK8Zjct3ODv2qW4syMvQq24WnSbJhFN18csKJb3_ORGFAdN5__t3E3tsquT7i0rEd_7-JLpqFF4vw-0_F5oelpLqRXIlVfPk7HQImeuYeFQrmmbPZaP1lJ4L-K3l1ig9Ix57m7XOTRt20rSOLYlCq-Ml_54sZEuBW9g2gcqrN5QVbOd9xiY7AOUESk16c8aAGAnT2JWdaiSlSuBDjcU23v9a5Qcve4knFTe3jBmgBhc7dNsXzd4OdbpzoA1MNBP_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26df8fab5.mp4?token=NzkmIUAERO83HMWptUxSOGE1mRmDd72A_mG88IBCkpwNuCCPwL4obCL7KMPV9465dpJsEhnj4ienOS1kbjSYmkK8Zjct3ODv2qW4syMvQq24WnSbJhFN18csKJb3_ORGFAdN5__t3E3tsquT7i0rEd_7-JLpqFF4vw-0_F5oelpLqRXIlVfPk7HQImeuYeFQrmmbPZaP1lJ4L-K3l1ig9Ix57m7XOTRt20rSOLYlCq-Ml_54sZEuBW9g2gcqrN5QVbOd9xiY7AOUESk16c8aAGAnT2JWdaiSlSuBDjcU23v9a5Qcve4knFTe3jBmgBhc7dNsXzd4OdbpzoA1MNBP_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ژئوپولیتیک:
ایران سامانه‌های پدافند هوایی ساخت داخل خود را به عنوان جایگزینی کم‌هزینه‌تر برای سامانه‌های گران‌قیمت خارجی معرفی می‌کند.
طرفداران این سامانه‌ها مدعی‌اند که آن‌ها موفق به رهگیری هواپیماهای پیشرفته شده‌اند و استدلال می‌کنند که فناوری بومی می‌تواند بدون تحمیل هزینه‌های سنگینِ تجهیزات وارداتی، دفاعی کارآمد فراهم آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69791" target="_blank">📅 15:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69788">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cUlyjM0FRyW92uyLxH6DQq5f2d6m-Wdr48x0sHk2xdDdBlUoOV8nH7srqzUzbrbYoap_URstfZQ7-S2c-3ym3qRTBNUlVK3X5ADUIJbixPJ2_ftfLfFYJ_EjOlbeBfbJVafmfnLlsAOZJ9SdQ209iC16cCTrbU-DKPFAhjGpTkzPj2atVCbhfclU3se8TVqHIuExfzyTKbHBxfkL8OWNZDHxHFZu-CWixtJb8CIEs5YmV0gVA4vbVOA3tsq_dRkwXh4zq4QDTXBxAMreMyEMdrj0uuzoxXZcPPNgVXV9JSb8fI5HEwxdZdaof5dlgcSL_OG4ikBKxoUzmwyPuHO-Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hZFmxF16-FL2P4EdjInkeXQ6C6N2izWhjAnBblVBBO8n0DNVyhRifKOLI60XVaRztZYA_hG0O79IO2LZi1TlbiiIvCcffQ-3BXPKSPsg7OC9GKTx824pESKNZHlQ_Sme2DMTvH54lYjWev3w62ztaai0OEL0td8zIY2X8a98zQjidW7rvYNo-yLLa_1AHDuNGKKeuvGYUIFbdp5v-Utv5F3Leuk_tdHU_RuPIx5JEXi15tCi_LUaHiM3lKXK_8P61NkJkhgQWjWkRxU9WlMlhDjfl7gHHj_IYxp6bCE3F2OJlfDZ9R7MorpHl1ZR-euJ8feKGyl2tFYkJwadYLbROA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DwoZg7wZWQqpLVILaY8daqzaEMuxrWlxqQXp49IxrlKrfkzr0rJMp21SAtd2lPs-rsUtjKLeLlzusuLJsB3XOtZC7vaZ6Cc2dxFSf_D7ilwPeQOtHVA86HbW4oxoMspq3mBiqC98oudHzT8Iw9d3fn0YnKQU1owaH-dNKDqIn116B2khj1KhmOhF0a1VNrxm_usfChzJeD0mCzfGeldp4jh9Ly_2eXfZvOVaIi2voTK-ApoCRAIWaziEW7LZVURZQzamCxI5USCXHpr38xyr904obG94Y0qw917Ed7gfXoNgVnethhVXFsc7Wcqus2hX40U_jABzgSwxG67vNoON4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
‼️
🔞
ابعاد جدید ماجرای قتل حمیدرضا رجب‌زاده توسط یک بلاگر دختر:
حمیدرضا رجب‌زاده، یه مداح جوون، بعد از خروج از خونه ناپدید می‌شه. پلیس در تحقیقات به یه بلاگر زن می‌رسه که قبلاً با حمیدرضا در ارتباط بوده و اون روز هم ازش برای یه ملاقات حضوری دعوت کرده بود؛ حمیدرضا به این دختره بارها بخاطر حجابش تذکر می‌داده و بهش می‌گفته بحث سیاسی نکنه
طبق اعتراف متهم‌ها، این زن با کمک پنج مرد، حمیدرضا رو به یه محل خلوت کشونده، بیهوشش کرده و بعد اون رو با ضربات چاقو به قتل رسوندن و قلبشو از سینش دراوردن و رو صورتش مایع منی ریختن، بعد هم جسد رو به اطراف پرند بردن و آتیش زدن و از صحنه قتل فیلم گرفتن؛ با اینکه چند نفرو گرفتن ولی متهم اصلی هنوز فراریه!
🔞
ویدیویی که قاتل منتشر کرد
⚠️
⚠️
حاوی صحنه های وحشتناک
⚠️
‼️
اعترافات بلاگر دختر:
من با مقتول در فضای مجازی آشنا شدم  او مرتب به من تذکر حجاب می داد و می خواست درباره مسائل سیاسی حرفی نزنم و زندگی مناسبی داشته باشم من این موضوع را با دوست پسرم درمیان گذاشتم که او پیشنهاد داد مداح جوان را با بهانه ای به محله خلوتی  بکشانم تا او با دوستانش دست به قتل بزنند او گفت که گروه های منافقین بابت قتل بسیجی ها پول پرداخت می کنند بخاطر همین بعد از اینکه مقتول کشته شد فیلمش را گرفت تا به آنها بفروشد
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69788" target="_blank">📅 15:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69787">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRl98yTq1Voa3ORWiCenX6ETMzfoGmgr_hSNDJvzc7YMIknkk07y5s8byAm95Y0JQpRw3BoBDS_16_IUuB6nxneJRCf0_dgtUkd7K8jF1fLmdvm2vx9iY7QD5B_i_m1tT1fsLazc8mloAEJfW9x5TwPqb5yZ3jiBIwAy-YKWoauY7l8sLfBP5-htLNUeIohFKkqJmIFByIprE-xRj24xQn8LKsDLoxEfAURKQYWj00MKmZ66puJnEVPp5MiNMbiIAmBEw5xWAbMDha_df4namIBgk3v1broYvyCCKLWvKvlULl05aRzxhDJsPYPq0p4oZem608Fb3esQJ11GgJ-rZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
فرماندهی مرکزی ایالات متحده:
ملوانان آمریکایی در حال تعمیر و نگهداری هواپیماهای F/A-18E Super Hornet در عرشه پرواز ناو هواپیمابر USS Abraham Lincoln (CVN 72) هستند تا اطمینان حاصل کنند که تجهیزات گروه ضربت ناو هواپیمابر برای اجرای محاصره ایالات متحده علیه ایران آماده ماموریت هستند.
تا 8 آگوست، CENTCOM 53 کشتی تجاری را تغییر مسیر داد، 2 کشتی را از کار انداخت و 2 کشتی دیگر را نیز توقیف کرد.
🔴
ارتش ایالات متحده همچنین به بیش از 30 کشتی اجازه عبور از محاصره برای کمک‌های بشردوستانه را داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69787" target="_blank">📅 14:59 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69786">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
ادعای فارس:رئیس‌جمهور با رهبر معظم انقلاب دربارهٔ مسائل اقتصادی و نظامی کشور دیدار و گفت‌وگو کرد.
پزشکیان همزمان با شروع سومین سال ریاست‌جمهوری با حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای دیدار و گفت‌وگو کرد.
در این دیدار به‌تفصیل دربارهٔ مسائل و مشکلات کشور به‌ویژه تأمین نیازهای معیشتی مردم، شرایط موجود جنگ تحمیلی سوم و آیندهٔ پیش‌رو، تحولات حوزهٔ نظامی، راهکارهای ناظر به تأمین منابع و مدیریت مصارف «ریالی، ارزی و انرژی» و همچنین تعامل اقتصادی با طرف‌های خارجی تبادل نظر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69786" target="_blank">📅 14:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69785">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‼️
صحبتای این خانم در مورد کافه رفتن و پیدا کردن پسرای پولدار، خیلی وایرال و جنجالی شده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69785" target="_blank">📅 14:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69784">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ab9ff0322.mp4?token=EXqy5gEJVi_VwrkQirp12BDZma0B9BzSCy9nbFPxnlgSU1eua6kwnjZzLvc41g4eafkGCe-ZIAewizEZ-14LVumrcz8pCVX738ssvSbRt6DA5MdMKWiXG0ygyDEjBTcGkE5N4K8kJdhs7DxzUHODTdx7ClwG9aqxifYu-iCpWJBwZCuez4lMw5ds0TxnRjq3WlRAcfUXRew2df-DmE9SnqEnRQfUqRfZo4TZxhOjxuzZrFjXsqUDI00nIbqOw6fZdXKQUI7FRkgx2eIaj95Mb_c77hhrS9dOer3zm0N4CAZ8Tc88pWr7WZvtm7uGHj-adcq9nk6vFDYBsMnNPtInWA5taZUlRVeVBhtFU_ZbwVRlab4F7hq17aGn-ddhuRgcFw-N7saVUd57Q9c1ilKv5XYeGgzr_OQA5LaT45J3JNJh312GM3CyMe-v4y6ZiTZKxcu1xSV2jisaGE6pN9sF80VUeVAkJZ5qShwR6TZpuE6AFjP9YBMtpEmppqk374kPelP19sqwQPZ2wK8JGuHn8BEggpiLAzG4RvWKRoG8Vr44i9WjWrfOoV-x3RZeZ6O2-NggUdKd1gN5-orQ-i-xS35uiw1MUojMCOE8-hUKhjxWcDdYza8UYG2r6GWhDqKV0mAxpac_3dBrVY2XuaYjMOql7iWK7nW22jWxb-6qeWs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ab9ff0322.mp4?token=EXqy5gEJVi_VwrkQirp12BDZma0B9BzSCy9nbFPxnlgSU1eua6kwnjZzLvc41g4eafkGCe-ZIAewizEZ-14LVumrcz8pCVX738ssvSbRt6DA5MdMKWiXG0ygyDEjBTcGkE5N4K8kJdhs7DxzUHODTdx7ClwG9aqxifYu-iCpWJBwZCuez4lMw5ds0TxnRjq3WlRAcfUXRew2df-DmE9SnqEnRQfUqRfZo4TZxhOjxuzZrFjXsqUDI00nIbqOw6fZdXKQUI7FRkgx2eIaj95Mb_c77hhrS9dOer3zm0N4CAZ8Tc88pWr7WZvtm7uGHj-adcq9nk6vFDYBsMnNPtInWA5taZUlRVeVBhtFU_ZbwVRlab4F7hq17aGn-ddhuRgcFw-N7saVUd57Q9c1ilKv5XYeGgzr_OQA5LaT45J3JNJh312GM3CyMe-v4y6ZiTZKxcu1xSV2jisaGE6pN9sF80VUeVAkJZ5qShwR6TZpuE6AFjP9YBMtpEmppqk374kPelP19sqwQPZ2wK8JGuHn8BEggpiLAzG4RvWKRoG8Vr44i9WjWrfOoV-x3RZeZ6O2-NggUdKd1gN5-orQ-i-xS35uiw1MUojMCOE8-hUKhjxWcDdYza8UYG2r6GWhDqKV0mAxpac_3dBrVY2XuaYjMOql7iWK7nW22jWxb-6qeWs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
عباس عراقچی:
اکنون هیچ مذاکره ای با آمریکا نداریم و نخواهیم داشت
شروع مذاکرات بدون پایبندی آمریکا به شروط تفاهم‌نامه غیرممکنه
ملت ما تسلیم اراده یک عده خاص نمیشه
بدون تحقق حق ملت ایران کوتاه نخواهیم آمد
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69784" target="_blank">📅 13:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69783">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34556823e0.mp4?token=Q3gLE8H5crL0VsvHfM9CH-cqAeKckd4-augsrbtGKRDrSl0Kt17VjfsGPn5iBfRV-pwRbCBFpqLG7coCaTuMSsM9iMjUrLWGoLY9_X7e7kwVNkPOkVCbV5UH52xfe_wz7lLovc0AqjqWr30ppbKGe6TGkOcF6-_lf8R7dtX-cUwNP9erp688N7wB2NhHiVaVUXUZljIOUBtr8gLmLFy0uRya1P194X7xHI6_eL9PZMjWvIpx2p4KmXK8z9V18JyxdRAb6FnU3ZpGjeVpw-Yy7cYR1EMAvyUi4bmiuMjg86uv4ghQESOermyroYgMQLS4bpghoBL3SVrVTkdQmAgYDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34556823e0.mp4?token=Q3gLE8H5crL0VsvHfM9CH-cqAeKckd4-augsrbtGKRDrSl0Kt17VjfsGPn5iBfRV-pwRbCBFpqLG7coCaTuMSsM9iMjUrLWGoLY9_X7e7kwVNkPOkVCbV5UH52xfe_wz7lLovc0AqjqWr30ppbKGe6TGkOcF6-_lf8R7dtX-cUwNP9erp688N7wB2NhHiVaVUXUZljIOUBtr8gLmLFy0uRya1P194X7xHI6_eL9PZMjWvIpx2p4KmXK8z9V18JyxdRAb6FnU3ZpGjeVpw-Yy7cYR1EMAvyUi4bmiuMjg86uv4ghQESOermyroYgMQLS4bpghoBL3SVrVTkdQmAgYDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو رو ببینید تا متوجه بشید با قیمت الانِ یک نوشابه، تو سال ۹۵ می‌شد چه چیزایی خرید...
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69783" target="_blank">📅 12:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69779">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frV9QJC8LyoM1TolvKt6ZstoCmdWSk6MTYms_23439F1HambTeZanW2-OtbvopMn1EAuiL3ZuaYIc-nM_5_X7uKboq5lBWdOHHlP-aN2PGbjtUrC_An4aZfpaDYYii_g6KBixMhomhsBMot1CWshKz-TbtaHG-gE45ZXegUO6uhTtlkpFc2fHlJDINkNZQVTj80IaFJ2a-ylVco_sxf2am66vaM7IGAPvqIXBCdUUDNOCNsxvdYIQmgyBrbTtKMEvDvh0PJRTvyMolPNOmOdegBJ-y5Ndii0t303qT4v_L_pLkDA-ZMas8QY0QMqsIFM89kM2nTpKy4t33dQ2v402w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e5f1aeb56.mp4?token=Oa_FLMDJ9iU_6xNTTGBXYnR4GORUzdZpaAbUbVe30JzFTJYEuxuFjb9JUeCUjvQQVGkGasEIjxAl8oMUBU9Z3rGjYjYXEry5S9rdYqov0ovqN3ckAEpMGcPNIMovufc22TL22OVuUV2NfOm3hee-ETjhRWaCev24mgAFrUqW7PrD6neY3AcZuTuN4egYvhD335vobRp7K1jhwBxYjClBJ0Mnbcp8ivElaCtpKbnMnR0ex5O8mOTO_W5YZBHVidD8sqS46-05FY3_un7wWkv_sUe0vJWvU-BR4lFVPpwRXE1qn_RFswYCyHVUQy0OmJrv2yJvZfbABeHFpVW6etptTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e5f1aeb56.mp4?token=Oa_FLMDJ9iU_6xNTTGBXYnR4GORUzdZpaAbUbVe30JzFTJYEuxuFjb9JUeCUjvQQVGkGasEIjxAl8oMUBU9Z3rGjYjYXEry5S9rdYqov0ovqN3ckAEpMGcPNIMovufc22TL22OVuUV2NfOm3hee-ETjhRWaCev24mgAFrUqW7PrD6neY3AcZuTuN4egYvhD335vobRp7K1jhwBxYjClBJ0Mnbcp8ivElaCtpKbnMnR0ex5O8mOTO_W5YZBHVidD8sqS46-05FY3_un7wWkv_sUe0vJWvU-BR4lFVPpwRXE1qn_RFswYCyHVUQy0OmJrv2yJvZfbABeHFpVW6etptTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی اوکراین به بلگورود
نیروهای اوکراینی شب گذشته حمله گسترده‌ای پهپادی به شهر بلگورود روسیه انجام دادند که در پی آن چندین ساختمان مسکونی هدف قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69779" target="_blank">📅 12:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69778">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/69778" class="tg-doc-link" target="_blank">دانلود</a>
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
r18
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/69778" target="_blank">📅 12:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69777">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cm597jNowI3znnDqhWQalerNZw2KmD6LLenkPevh0SvaSdNB5q4F2XGmSuO2vfosOOgCbepoOJIo7isZwl7KNJTxMBfvw2OudeDmv3bs_6NqE2Rku4nsg93v749XBxgCLN0TaTv2T9METN0cnLKjTlznhGj6FwrTb7fiyAzZHyy0xOq9npA9qq7s9zg3gv6b9hkruwKn7HJZ9fOOcdq2p4iWITIAxvbzNF5VQQVpt6RIVTWUlgJv8ZTzCl1IeaiKSmsqtnSDHA3CwRhHeo2gNJMuDXvFMxWXLJTfDEb7IYE5mzRkVCke3BfsGQ5l5mdueh5TCatOcyn_woUJO4zlwQ.jpg" alt="photo" loading="lazy"/></div>
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
r18
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/69777" target="_blank">📅 12:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69775">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c93de8243.mp4?token=v3WJAi_6k8EncNrHVviABfMhI1IjZfrj6rFQLeRx_IzZQQl1riYKCDxkGtpUWd6njdlJytGd8TZTwGpYilzduvzsHJl1_JhLBAaO6zHceRJVOW4CCGPJaMlDgUfNL1lTDNjE6nvq312trDUhI325a1u_QTxTyzg2nSUvGZezxHTbF62U-_QM_vTHN_ZrDkn9V8fOftXIPyDyox7cD5f2ji_yYZ8WeGHH2VZmaeFHuxmTSnGFV1-dYJP3f1KQ5VpaxKd39A7hMegzh_XibHBkQjm0d3tMnzwrKjpQDgtjw0bgltj5LWoB_PHnZGwCb4bbKGmCmx9nslBhKnGN4n-Qtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c93de8243.mp4?token=v3WJAi_6k8EncNrHVviABfMhI1IjZfrj6rFQLeRx_IzZQQl1riYKCDxkGtpUWd6njdlJytGd8TZTwGpYilzduvzsHJl1_JhLBAaO6zHceRJVOW4CCGPJaMlDgUfNL1lTDNjE6nvq312trDUhI325a1u_QTxTyzg2nSUvGZezxHTbF62U-_QM_vTHN_ZrDkn9V8fOftXIPyDyox7cD5f2ji_yYZ8WeGHH2VZmaeFHuxmTSnGFV1-dYJP3f1KQ5VpaxKd39A7hMegzh_XibHBkQjm0d3tMnzwrKjpQDgtjw0bgltj5LWoB_PHnZGwCb4bbKGmCmx9nslBhKnGN4n-Qtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
⚡️
تصاویر جالب از لحظه برخورد رعد و برق به ساختمان مرکز تجارت جهانی «اسپیرز» در نیویورک؛
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69775" target="_blank">📅 12:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69774">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b13fec044.mp4?token=QjQsE2_gc1ObJ17GhBp8VaA5A5YWgfQ-K2RctgGmu_dy06fZuIUgHrvPz5PZkyG_W_UAiAu2Cw0mnsrHuARsv1xG3e01W5O7JRNi5MbAZ-XlcYH36sOSpiPa9S4jMXLyJk5rT3s2gdlntd2cd-UaVYkvoCtJIQROPx78f7R066EY-rFLYyI-4nOPl2Nfo93CS1fz5Lhu9m43ulxJjtRmQ8gpf-yljzlpcfQkQQIJ8IIi1UcBrHX6tKVtmVoI2Zk3kC6hjKZ2U1sGWRKZ1EOHhhirPrxYBPyKCjsr7v6G84-zxTxVGPlVtW3fdGFq1BgRGwGck025pjnXma2qa-fOnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b13fec044.mp4?token=QjQsE2_gc1ObJ17GhBp8VaA5A5YWgfQ-K2RctgGmu_dy06fZuIUgHrvPz5PZkyG_W_UAiAu2Cw0mnsrHuARsv1xG3e01W5O7JRNi5MbAZ-XlcYH36sOSpiPa9S4jMXLyJk5rT3s2gdlntd2cd-UaVYkvoCtJIQROPx78f7R066EY-rFLYyI-4nOPl2Nfo93CS1fz5Lhu9m43ulxJjtRmQ8gpf-yljzlpcfQkQQIJ8IIi1UcBrHX6tKVtmVoI2Zk3kC6hjKZ2U1sGWRKZ1EOHhhirPrxYBPyKCjsr7v6G84-zxTxVGPlVtW3fdGFq1BgRGwGck025pjnXma2qa-fOnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
گوشه‌ای از سخنان وایرال شده خرازی، برادرزن مسعود خامنه‌ای:
جمهوری اسلامی یه موشکی به اسم «رستاخیز» داره که میتونه یه دور کامل دور زمین بچرخه و به راحتی خاک آمریکا رو بزنه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69774" target="_blank">📅 11:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69773">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0189fef147.mp4?token=ihTDv-4BRClK6tiyoRTF72cOhe_gRoD0kqf9KqFfkhef-rmZRUIU2pZ5Cnc4aD4hQIeG6zIXf38D1hMLjP3yIG2A_3U0Um8JtLf6IRpc5UeSCKE4mNBRmDpn-rdg73vs6X-nXZG8xtVFyvdt8dPWFF98BzIb16ZmwRjJq02UXJf9FCq1UPXlLhISCxMyQXUXpSp89ori8y-UNt1NHz1xZ-qTKLElT8f2hmfXt0m9Su9UPAxinoIOSMUBXBTDKFQV7kcBi4ocJT9U6v4fUxF3MhcdlTIQigfWWpb2QzzuwKqLsYiQwxuldJq5_mHJBtOInL8Hp5ZNnhyM9PBZGsDh05hg9PH-Q-qco8joqLJxVuCgEvVKFwuCqYiXOLDWT7Hte7COxEbSIVi3HB4DYlccXS_tcyACpMWaznwHtCxiAJOfaY83vClWqZfx9dDXwzmxac5_JpqOcQ47imIsQc4jrfS2GsmJMlOoVWHzuJboMlG1FqcGJCTB6_zJAOe9P6vSFQORZiRPEtL3Ej8hDm3TkVz3Toq9h2roBLFhBfDmFNGArSEfpZ-c6ZU9FuzT0WJIrZPU8sWavaTz9Ek19Fa3b90p4BRrwNw22zySdexz2QVBR7Lu41j2haHf67kGG1vmhn4N24hh8MIHsIfbu4JGI7MfG0mTGcA9BZUtqSqrNwM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0189fef147.mp4?token=ihTDv-4BRClK6tiyoRTF72cOhe_gRoD0kqf9KqFfkhef-rmZRUIU2pZ5Cnc4aD4hQIeG6zIXf38D1hMLjP3yIG2A_3U0Um8JtLf6IRpc5UeSCKE4mNBRmDpn-rdg73vs6X-nXZG8xtVFyvdt8dPWFF98BzIb16ZmwRjJq02UXJf9FCq1UPXlLhISCxMyQXUXpSp89ori8y-UNt1NHz1xZ-qTKLElT8f2hmfXt0m9Su9UPAxinoIOSMUBXBTDKFQV7kcBi4ocJT9U6v4fUxF3MhcdlTIQigfWWpb2QzzuwKqLsYiQwxuldJq5_mHJBtOInL8Hp5ZNnhyM9PBZGsDh05hg9PH-Q-qco8joqLJxVuCgEvVKFwuCqYiXOLDWT7Hte7COxEbSIVi3HB4DYlccXS_tcyACpMWaznwHtCxiAJOfaY83vClWqZfx9dDXwzmxac5_JpqOcQ47imIsQc4jrfS2GsmJMlOoVWHzuJboMlG1FqcGJCTB6_zJAOe9P6vSFQORZiRPEtL3Ej8hDm3TkVz3Toq9h2roBLFhBfDmFNGArSEfpZ-c6ZU9FuzT0WJIrZPU8sWavaTz9Ek19Fa3b90p4BRrwNw22zySdexz2QVBR7Lu41j2haHf67kGG1vmhn4N24hh8MIHsIfbu4JGI7MfG0mTGcA9BZUtqSqrNwM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بابای این دختره چون دخترش توی امتحان گواهینامه قبول شده براش BMW 225 خریده ناقابل ۱۲ میلیارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69773" target="_blank">📅 11:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69772">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/973161bf95.mp4?token=vSXtuxLGbZ_g_FYlBR4sY5soCeQTkMkJtxS3pLyVu4QT3b_aDHaz8oZKTkrBifNQ3fo8Ps7hyTEj4-fMHF83rCU46x-WQ8IgDQ9fSlgXb1L-FRXGMdJ8S_Afh08gbkB7TNZTOcTwfxbmIpg7im2O2T22xsZBSiv3j6ifBqIbp1uPklQLIbNjlKzV2NeQ4RnCgKRqgMaedkbF-OSxnz7G-VSvb0VSwO98OpisrZZdKCHpe8pzQiW_E0BuKDjZLZ3f4KFyCE5I9oHEsTJqKK2mbvEPZxBfIyqMOMBLLg90nA2jdIGKzC0IKFLba6o2WzqfHghcPuOx8JtWXmORi1re8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/973161bf95.mp4?token=vSXtuxLGbZ_g_FYlBR4sY5soCeQTkMkJtxS3pLyVu4QT3b_aDHaz8oZKTkrBifNQ3fo8Ps7hyTEj4-fMHF83rCU46x-WQ8IgDQ9fSlgXb1L-FRXGMdJ8S_Afh08gbkB7TNZTOcTwfxbmIpg7im2O2T22xsZBSiv3j6ifBqIbp1uPklQLIbNjlKzV2NeQ4RnCgKRqgMaedkbF-OSxnz7G-VSvb0VSwO98OpisrZZdKCHpe8pzQiW_E0BuKDjZLZ3f4KFyCE5I9oHEsTJqKK2mbvEPZxBfIyqMOMBLLg90nA2jdIGKzC0IKFLba6o2WzqfHghcPuOx8JtWXmORi1re8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
علی مطهری، نایب‌رئیس پیشین مجلس شورای اسلامی:
از همان ابتدا، هدف ما ساخت بمب‌های هسته‌ای بود و باید تا پایان ادامه می‌دادیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69772" target="_blank">📅 10:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69768">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c32fad0f32.mp4?token=F1NA2E4qS5rt8bIOx7HdwZOYXZ7TfrpcnMqflPUvif0u_pUzuVRdZeNXy87bOX55DGbVcmQQos1oQxBKTHxL5bhDQQ9rrIhdzY_1dV3QPGD03oXldxKWNECrKmoQrYeyYvLBRPZD8NEcJhS7D7NfG916VsVtwyxZiMR4hSLjfbXd9ZcNA8TQ6HPo4EZ6tEiC15aPaV4Ijxn4eGIvNdbLUczoOgI338SqpsyNUCK8ipAkYEkb695ZZNr_XekUBCEZOBgK3LDOcdR2ZvBkDuhGtloXyxd6eERJ-4wn8prcsxnPS6SgC9PFtGVWH-4FKdRQLyhLMcdPNXO0YSBJNRzRHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c32fad0f32.mp4?token=F1NA2E4qS5rt8bIOx7HdwZOYXZ7TfrpcnMqflPUvif0u_pUzuVRdZeNXy87bOX55DGbVcmQQos1oQxBKTHxL5bhDQQ9rrIhdzY_1dV3QPGD03oXldxKWNECrKmoQrYeyYvLBRPZD8NEcJhS7D7NfG916VsVtwyxZiMR4hSLjfbXd9ZcNA8TQ6HPo4EZ6tEiC15aPaV4Ijxn4eGIvNdbLUczoOgI338SqpsyNUCK8ipAkYEkb695ZZNr_XekUBCEZOBgK3LDOcdR2ZvBkDuhGtloXyxd6eERJ-4wn8prcsxnPS6SgC9PFtGVWH-4FKdRQLyhLMcdPNXO0YSBJNRzRHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ایشون به اسم آرش، خودشو اولین:
همجنس‌بازه، شیعه، پادشاهی خواه، دو رگه تُرک و لر معرفی کرده که پشمای همه ریخته
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69768" target="_blank">📅 10:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69767">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4c02b892b.mp4?token=Z0mVGTKaVEhnk0_-Ve6bqVVwhuRStV-_9Wk7muk6lSctKJahtTjpkVWk5KfpkN-Py04RDgtYXPbhaqa99JWe5MJer0XzhQ89RjJztiPdehkjFJa7MXxmZg9kALdqt1GH3ykj81iLYZBDArH_TPALrTFN6Ks4ZoOrVYgxtZisoLfXyGPLS-p-lucdtuMjDse__Evz2kneWP_-7RZMyPEZpS1MNYVqLkE5Gqg9kf1o3IhgQAceOXxLcOOx5a6Fo7Mm4fcncEcsGcqSVv4bSlKzZWm7LGzfL_NXFBddPq9FI-8hp5I36dtJaevzODBfIUWy4BpPKjTpzTMaSV38dm38Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4c02b892b.mp4?token=Z0mVGTKaVEhnk0_-Ve6bqVVwhuRStV-_9Wk7muk6lSctKJahtTjpkVWk5KfpkN-Py04RDgtYXPbhaqa99JWe5MJer0XzhQ89RjJztiPdehkjFJa7MXxmZg9kALdqt1GH3ykj81iLYZBDArH_TPALrTFN6Ks4ZoOrVYgxtZisoLfXyGPLS-p-lucdtuMjDse__Evz2kneWP_-7RZMyPEZpS1MNYVqLkE5Gqg9kf1o3IhgQAceOXxLcOOx5a6Fo7Mm4fcncEcsGcqSVv4bSlKzZWm7LGzfL_NXFBddPq9FI-8hp5I36dtJaevzODBfIUWy4BpPKjTpzTMaSV38dm38Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرفای یه طرفدار حکومت درباره حجاب:
آقای پزشکیان واقعا مرسی که گفتی نمیتونم قانون حجاب رو رعایت بکنم
مجلسی که ناظر هستی توام دمت گرم که اصلا فکری برا حجاب نمیکنی
پزشکیان داره میگه ععععععع مگه هنوزم گشت ارشاد هست؟؟
بحث دیگه حجاب نیست بحث پوششه پوشش و اصالت ما داره از بین میره
تو خود اروپا هم قانونی برا پوشش هست نه اینکه لخت بریزن خیابون
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69767" target="_blank">📅 09:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69766">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed36a1671.mp4?token=W6mt_FJtyXM9a8DM8_f5s9r8Ezw3BTR5EwfqrYChMZJ-okQ7rcF1hNIH2KoqAkRTvbQcOL7z9VkQ7dyIlqaRtpryRC58wY7akBtU2hxH4k4rIY3M0ySz-ZMPj70MzNlWU_FrkN8XgLwibBMcBY66knxPBCfQIKilb5sdn-E2pZ1qqPHzzO0MyPwi5gn-jgdX9v9Bb1NfDqe94e22-yBo4GTGUVTjVE1GwbaOYONwYRF03GK3TlDVPFqp8wN0skRp0RBMooL2e7Opw8B7ZtKhAG3BNFsn6FVGJW2hMlqXCXTAN5Rxb8YJjuX4m9nE04EqN5VjZg9AW5cI6-qb3gQ0kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed36a1671.mp4?token=W6mt_FJtyXM9a8DM8_f5s9r8Ezw3BTR5EwfqrYChMZJ-okQ7rcF1hNIH2KoqAkRTvbQcOL7z9VkQ7dyIlqaRtpryRC58wY7akBtU2hxH4k4rIY3M0ySz-ZMPj70MzNlWU_FrkN8XgLwibBMcBY66knxPBCfQIKilb5sdn-E2pZ1qqPHzzO0MyPwi5gn-jgdX9v9Bb1NfDqe94e22-yBo4GTGUVTjVE1GwbaOYONwYRF03GK3TlDVPFqp8wN0skRp0RBMooL2e7Opw8B7ZtKhAG3BNFsn6FVGJW2hMlqXCXTAN5Rxb8YJjuX4m9nE04EqN5VjZg9AW5cI6-qb3gQ0kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدیو وایرال شده از فردی که در زمان رفراندوم سال 57 حضور داشته
:
وقتی من روز رفراندوم رفتم بیرون و دیدم گفتن ۲۰ میلیون نفر رای دادن زنگ زدن آدما بهم گفتن بیا ببین چخبره.
اونجا رئیس حوزه آخوند بود و این بیجک های صدتایی رو میدادن دست مردم میگفتن بنداز صندوق بگو مرگ بر شاه.
جمعیت ایران اون زمان ۳۷ میلیون و ۲۰۰ هزار نفر بود.
کل کسانی که بالای ۱۶ سال بودنو و میتونستن رای بدن ۱۸ میلیون و ۷۳۲ هزار نفر بود.
آمار رو با خنده اعلام کردن ۳۰ میلیون نفر رای دادن.
توی وزارت کشور گفتن که اینطور نمیشه پس گفتن ۲۲ میلیون و ۴۰۰ هزار نفر رای دادن و ۲۰ میلیون و ۴۰۰ هزار نفر به جمهوری اسلامی بله گفتن.
اینو حساب کنید دیگه از کل ۱۸ میلیون نفر واجد شرایط مخالف بود مریض بود زندانی بود و.... از اینجا بود که من راهمو از اینا جدا کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69766" target="_blank">📅 08:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69765">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-release.apk</div>
  <div class="tg-doc-extra">4.5 MB</div>
</div>
<a href="https://t.me/news_hut/69765" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎲
همین امشب با اولین شارژ
🤩
🤩
🤩
درصد شارژ بیشتر بگیر
همین الان شانست رو با موجودی اضافی امتحان کن حتما بزنده میشی
👌
👇🏻
👇🏻
🌐
Telegram
🎲
🌐
winro.io
🎲</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69765" target="_blank">📅 01:46 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69764">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhXc56xYblTBsZigAZnvY5a3MYOupwQERq1BI5q-qnQ_Ag5gQfzXKiRESEj9ASScJ-il6Rv5p2VV7yeNg8gcJn6J6g6-wNT2PXhYW9K1PZPztJgDTnoRT94ifxvzQkKo7OiVi_VsKcOKYYDlw8PI9QULWhNpU2dYFWXO4j1dX7ODqTmO-VG8HFhmfMNLWB2sKot-K3vjRX1rPyqIWpFB4Svs9KXlkk9Vg35CujUlc9P0mxRXs3uosIBzkcFaMBeWT9q8iMaEZO6q49eZa3Haf4vn6isHA7v4BJYj5vNhOUiuk_0lr-jsPGscCLo_IgXHfo_Lu1yI6m7Wd2EHMc25HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
همین حالا موجودیتو
🤩
برابر کن
❌
☑️
۲/۵ میلیون شارژ کن ۱۰ میلیون شارژ شو
✅
برای اولین واریز تا 15 شهریور ،
0️⃣
0️⃣
3️⃣
درصد بیشتر در وینرو شارژ شو
🎁
✅
به ازای هر واریز در وینرو به ترتیب 300 ، 150 ، 75 درصد بیشتر شارژ شوید
.
🔊
با شارژ اضافی بدون ریسک بازی کن سرمایتو چند برابر کن
⚡️
🎲
ثبت نام آسان و سریع کلیک کنید
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا a17
🌟
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69764" target="_blank">📅 01:46 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69763">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20cf5580ad.mp4?token=EcJuigeNiUpNc2yrhKqFxe8XqI21jjwlMBU4Vzp3OB-WI2zaknylg0hDLF4FhXbGhDdKOzQuIxptfbBbCDXU8fN1uAAgVXCa1ZFFT9zcnAU42l1vlvd_rwnlzb1pmBi__4bnhmgKKSoYbenh_Zo_wy7A21oWvrAtPH7qBpOGhnd2dEFeqadWuJuWil4kpMMndWrQ_rlj3JZ374PsdAxy-Ra36Db4MrXmVFknaBorFs3uJEpv6j2nefVmwylyKgUdTrfgHbKJdW6eph7G8g7SdbMUx_wd8y-Zk8dzqLsZ4MhzEs0GWKfBu6NRu56YOGWcTpmHZJ-8owFidXK6iNgVpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20cf5580ad.mp4?token=EcJuigeNiUpNc2yrhKqFxe8XqI21jjwlMBU4Vzp3OB-WI2zaknylg0hDLF4FhXbGhDdKOzQuIxptfbBbCDXU8fN1uAAgVXCa1ZFFT9zcnAU42l1vlvd_rwnlzb1pmBi__4bnhmgKKSoYbenh_Zo_wy7A21oWvrAtPH7qBpOGhnd2dEFeqadWuJuWil4kpMMndWrQ_rlj3JZ374PsdAxy-Ra36Db4MrXmVFknaBorFs3uJEpv6j2nefVmwylyKgUdTrfgHbKJdW6eph7G8g7SdbMUx_wd8y-Zk8dzqLsZ4MhzEs0GWKfBu6NRu56YOGWcTpmHZJ-8owFidXK6iNgVpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇷🇺
سربازان روس با تفنگ موفق شدند پهباد اوکراینی رو سرنگون کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69763" target="_blank">📅 01:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69762">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
‼️
حمیدرضا رجب زاده یکی از مداح های حکومتی بوده که چند هفته پیش به قتل می‌رسه، حالا یه کانال تلگرامی مدعی شده اونا این قتل رو انجام دادن دلیلشون هم اینه بوده که این مداح تو دی‌ماه جز نیرو های سرکوبگر بوده و به سمت مردم تیر می‌زده  ویدیوی قتل که قلبشو از سینش…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69762" target="_blank">📅 00:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69760">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ku_aRAGwSZ1KGtLD06XhdNjYQwJBBjRue-pnhmR33fZ-YYn9z0i7ZwP6BiUwzglBIQIrGcC1rsNXD-L_VOzKmhdPT2KSZIfp2lCvXMK9aM1T71oIv_oskcbvc1IN0KAVujlu8K1WXwNR0Uxy88qDDgwGVZJp9Z-Hap8FvDqub-kTlQz_pKm1FimL9n6RCEd_4HQbxc64BcgdJpyVJv85agcqvlhWsO5BK3F5VgmI4DvF862vmTITT5JPj8ewpN9Vx0LAd25EwuZrialSorB63u_58TV032v43Gry_pD2Y9s52P-pLI88U6VehAx9oIrXJcavpSJ1lUcFxXRc6S5-Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5e8a9ce1b.mp4?token=OXTXV8Tn_pZksKwb9MemOn4-fdsLGwcmyCbAOBhXXpMivxNeJY9JsNI5mqjwpgUi1Gy_FFVfEM3Kcph7VGm8V_ltJyTvM4lhMWgkBTdJo9CCqesfyi-Xkp52_fsxw-QZoDLE4qs79kreG_SSGwSn4OK2iMxGSNFQp-5SV0kKa0duxlBHuVGBz7kA_KZNrvi1bCYYE7nidKyM3mAizMbbiAHKp7IbDlFQd_xTE4L9XqflasUNjqmiDW2mUZcIlnwr5rW0ez2xr6LNRKjrIDxJWms0t4MjtZNimk5hFRJzBlpU-VTV-Cm-ldldzvp0yO7C61fRM-9BJ4KHhxCVmVHrkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5e8a9ce1b.mp4?token=OXTXV8Tn_pZksKwb9MemOn4-fdsLGwcmyCbAOBhXXpMivxNeJY9JsNI5mqjwpgUi1Gy_FFVfEM3Kcph7VGm8V_ltJyTvM4lhMWgkBTdJo9CCqesfyi-Xkp52_fsxw-QZoDLE4qs79kreG_SSGwSn4OK2iMxGSNFQp-5SV0kKa0duxlBHuVGBz7kA_KZNrvi1bCYYE7nidKyM3mAizMbbiAHKp7IbDlFQd_xTE4L9XqflasUNjqmiDW2mUZcIlnwr5rW0ez2xr6LNRKjrIDxJWms0t4MjtZNimk5hFRJzBlpU-VTV-Cm-ldldzvp0yO7C61fRM-9BJ4KHhxCVmVHrkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حمیدرضا رجب زاده یکی از مداح های حکومتی بوده که چند هفته پیش به قتل می‌رسه، حالا یه کانال تلگرامی مدعی شده اونا این قتل رو انجام دادن دلیلشون هم اینه بوده که این مداح تو دی‌ماه جز نیرو های سرکوبگر بوده و به سمت مردم تیر می‌زده
ویدیوی قتل که قلبشو از سینش در میارن و رو صورتش خودارضایی می‌کنند رو هم منتشر کردند و بعد برای خونوادش فرستادن؛ چند ساعت پیش هم اعلام شد که قاتلین دستگیر شدند
🔞
مشاهده‌ی ویدیوی اول
⚠️
⚠️
مشاهده‌ی ویدیوی دوم
🔞
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69760" target="_blank">📅 00:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69758">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a034d8d108.mp4?token=dcQeR4Sma3SLEJKqGIr0hx4L93aOseprUkEUuAJnx_6E0JbFNXhFb0ofs3uWq5A_tWaui1LCQGlTXTurR9dnfaap3nvPs38Ek7_p15a4Tnp3dha76w6fmWPld_D7NawPBk16lSIFeEVw6m7-peWy2VRgB2Eu4uYOarlyt0y8Mj-FZh3YwR33pVKHZsk1QSBWlgHKgfWAzQp5wpGa_RPNnEYaV772R64M06Cs2Lhc3jJWn5j4yE97cFOTsOsk7P4EpS2KXjR6uO9fcvgil5JEXYiilO02CiUmlHbQXKMx0jvN5swMa3gapyaNy4Zka4A-SSRukyCvKqNFpe7MC5ufZHKIX3xkbLUCXIQntgidncqK_HM-DYRRAn8fG-Yq7wJrS-tpMZ_buKcA9sWsh-UnKqQvO5yn0c70n8K8o32qjXjLjqyZI6hcx5aCk3EfIxHH92gKYZiuzz2MHR-yXOCgY-hAuWILyoPMkIFGfaXOvvDEj4hDl9qPcmQEymEVaErSZhDR2lXC-xmsqvcehlfFlvWBdqd7MNJpzKLYkYVPVWwwOW89S8lwDRuRNbYm4b4vVpyjitl_Oqr1w8tmCZ0Ml5kWOo8lRHiulbkNwYyBS7zL78tCI9UESpoFXjwsj-leeb3XEfSjOBQ7rviWqWJJ77uz2tEtNsLVG1f80xfRW28" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a034d8d108.mp4?token=dcQeR4Sma3SLEJKqGIr0hx4L93aOseprUkEUuAJnx_6E0JbFNXhFb0ofs3uWq5A_tWaui1LCQGlTXTurR9dnfaap3nvPs38Ek7_p15a4Tnp3dha76w6fmWPld_D7NawPBk16lSIFeEVw6m7-peWy2VRgB2Eu4uYOarlyt0y8Mj-FZh3YwR33pVKHZsk1QSBWlgHKgfWAzQp5wpGa_RPNnEYaV772R64M06Cs2Lhc3jJWn5j4yE97cFOTsOsk7P4EpS2KXjR6uO9fcvgil5JEXYiilO02CiUmlHbQXKMx0jvN5swMa3gapyaNy4Zka4A-SSRukyCvKqNFpe7MC5ufZHKIX3xkbLUCXIQntgidncqK_HM-DYRRAn8fG-Yq7wJrS-tpMZ_buKcA9sWsh-UnKqQvO5yn0c70n8K8o32qjXjLjqyZI6hcx5aCk3EfIxHH92gKYZiuzz2MHR-yXOCgY-hAuWILyoPMkIFGfaXOvvDEj4hDl9qPcmQEymEVaErSZhDR2lXC-xmsqvcehlfFlvWBdqd7MNJpzKLYkYVPVWwwOW89S8lwDRuRNbYm4b4vVpyjitl_Oqr1w8tmCZ0Ml5kWOo8lRHiulbkNwYyBS7zL78tCI9UESpoFXjwsj-leeb3XEfSjOBQ7rviWqWJJ77uz2tEtNsLVG1f80xfRW28" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو این مملکت اگه پول داشته باشی، حتی کمپ ترک اعتیاد هم می‌تونه شبیه هتل چندستاره باشه!
● بعضی کمپ‌های لاکچری خدماتی مثل:
🍽️
غذای رستورانی
🏊
استخر، سونا و جکوزی
🎱
بیلیارد و پلی‌استیشن
👨‍⚕️
پزشک عمومی و روانشناس
📱
موبایل و لپ‌تاپ آزاد
🛏️
اتاق‌های VIP
ارائه میدن؛جایی که دیگه از کمپ های معمولی خیلی فاصله گرفته!
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69758" target="_blank">📅 23:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69757">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a2b2f82e.mov?token=YcTlSxjjFbjLDDUP5rmC1OHw0tSfnluNJ6cdX8ssk6JdiIM_iE204NxGJt3gugsrWZE3BAAd4YFMB3HrXkzGJq5lxt9y2QP5SbCq_X_l3_6VewUhLbEiTLCXx9HjyjS_IdacHGAWqCJStkiQt9Hn2otVRGTkqC1aH5Wi8qgHmRk6nEN2rvOw8xUbN0R_gPM-HQbmycFjvbZO1-QDQdQF14MNaSrS5mMidFBUu6a7AMusEL17-MH2gA2fgUfqwjZvn0SvcCmpcYNsUKngnC-QgJhFAmpkL10tD5T0fX0PN5Ny2GDcCQdGiYyUF9GpmJ2BUpJ1b3hJtyJZFi8NPYpn-H8IJ-G0ALVCAIfx5r-xaqLacsWxGEMG00DQkSQks_GxVVptPrrELCKxHhabRinrnhnwmYjiHRHbcVjZo2YP6lOZw-lSAWM7E_OXfcFesXM2crEcU4UzkmHL2do4vK2-XS_SFZ8V-c90Yf2-WLPjfDYJstVrMohK-uDQtNGEztNGcD24xp3gRjaiOtUGw3Cx9bSl6abpB3JGxKYgf8yHTlNXZ4JxE51G_cDE5TrsgHbQMOht6Ww17H6_GL70v3HYcLOV9YrciWIQskMDMBWdkDcGpHqg9A9I5j2AWFPXAuKBj8X6qq8P7ZgIT9LpVw4nunUdX0GjaVm5biVxcvKrg3U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a2b2f82e.mov?token=YcTlSxjjFbjLDDUP5rmC1OHw0tSfnluNJ6cdX8ssk6JdiIM_iE204NxGJt3gugsrWZE3BAAd4YFMB3HrXkzGJq5lxt9y2QP5SbCq_X_l3_6VewUhLbEiTLCXx9HjyjS_IdacHGAWqCJStkiQt9Hn2otVRGTkqC1aH5Wi8qgHmRk6nEN2rvOw8xUbN0R_gPM-HQbmycFjvbZO1-QDQdQF14MNaSrS5mMidFBUu6a7AMusEL17-MH2gA2fgUfqwjZvn0SvcCmpcYNsUKngnC-QgJhFAmpkL10tD5T0fX0PN5Ny2GDcCQdGiYyUF9GpmJ2BUpJ1b3hJtyJZFi8NPYpn-H8IJ-G0ALVCAIfx5r-xaqLacsWxGEMG00DQkSQks_GxVVptPrrELCKxHhabRinrnhnwmYjiHRHbcVjZo2YP6lOZw-lSAWM7E_OXfcFesXM2crEcU4UzkmHL2do4vK2-XS_SFZ8V-c90Yf2-WLPjfDYJstVrMohK-uDQtNGEztNGcD24xp3gRjaiOtUGw3Cx9bSl6abpB3JGxKYgf8yHTlNXZ4JxE51G_cDE5TrsgHbQMOht6Ww17H6_GL70v3HYcLOV9YrciWIQskMDMBWdkDcGpHqg9A9I5j2AWFPXAuKBj8X6qq8P7ZgIT9LpVw4nunUdX0GjaVm5biVxcvKrg3U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
نیروهای روسی به هدف قرار دادن تدارکات اوکراین ادامه می‌دهند و یک لوکوموتیو دیگر را در نزدیکی ایستگاه راه‌آهن «لوزووا» در استان خارکیف منهدم کردند؛
منطقه‌ای که یک کانون کلیدی برای کی‌یف جهت انتقال تجهیزات نظامی و نیروهای کمکی به سمت دونباس محسوب می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69757" target="_blank">📅 22:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69756">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da63e2e1aa.mp4?token=RxMQS3FAeIQQ-lY4cvREGF9MdmY1L9warKF3lYiY6-OVuzMcPZv9tXJREzeFCWEqVdNzU3XdrcLJafmX4hFI0o-w6DllhOTrTmsw5kBbGIAR0aAmOn0uup88Nq5CZPPTsPIRlTD7qIyvN9rY5308qJRRksBuAFtU8rm9kjWal9Zgu08jm1zlsX6dMVjcCwE2Y6B5lZ4DXbdrBtiJ5LP7UyhYoRY1trU5MhCUb1N3SBF9TkuRnGJUYhW6aXSA_CN4Qiu2o89inRN43vDoec52qoeO7vmqgBij9xo-ePwUSrFfX8BUBHm6T3FqefUuw2n-ieBL87tzFc2ZBWE_rT3mfmQw_t6Rgfvz4ShT6MtJCXhStH0pe4LDxe1JlIWw-IwcC6kmB5W2muLqCQS7s9gk9YYgw9uZNYcnlL7bJzN8nU7bvrHyZ0EGNJuDHDma9RcPlruoR5G3abc6YaV6JGc5thxRNtjwO4u4EKLzKYSb8ooEcj_IQoHtTIQ4iOcn71kClBAknCqNiquJo4iIk3aNE1-IMPjuM7j0BBt6-TxmGbT0xDjHDtpTfuvd1Km5q2jC8BojvOUZzCZ_uDT-6Fc0m9GqBdGVTtvfX9gSkX_reHILJ2f1_NGegQLxLlI6xysOjD3Qe8SOmma9nQiFjdSNRlJQskNZ8oZye9PMJezuloA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da63e2e1aa.mp4?token=RxMQS3FAeIQQ-lY4cvREGF9MdmY1L9warKF3lYiY6-OVuzMcPZv9tXJREzeFCWEqVdNzU3XdrcLJafmX4hFI0o-w6DllhOTrTmsw5kBbGIAR0aAmOn0uup88Nq5CZPPTsPIRlTD7qIyvN9rY5308qJRRksBuAFtU8rm9kjWal9Zgu08jm1zlsX6dMVjcCwE2Y6B5lZ4DXbdrBtiJ5LP7UyhYoRY1trU5MhCUb1N3SBF9TkuRnGJUYhW6aXSA_CN4Qiu2o89inRN43vDoec52qoeO7vmqgBij9xo-ePwUSrFfX8BUBHm6T3FqefUuw2n-ieBL87tzFc2ZBWE_rT3mfmQw_t6Rgfvz4ShT6MtJCXhStH0pe4LDxe1JlIWw-IwcC6kmB5W2muLqCQS7s9gk9YYgw9uZNYcnlL7bJzN8nU7bvrHyZ0EGNJuDHDma9RcPlruoR5G3abc6YaV6JGc5thxRNtjwO4u4EKLzKYSb8ooEcj_IQoHtTIQ4iOcn71kClBAknCqNiquJo4iIk3aNE1-IMPjuM7j0BBt6-TxmGbT0xDjHDtpTfuvd1Km5q2jC8BojvOUZzCZ_uDT-6Fc0m9GqBdGVTtvfX9gSkX_reHILJ2f1_NGegQLxLlI6xysOjD3Qe8SOmma9nQiFjdSNRlJQskNZ8oZye9PMJezuloA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از مردم پرسیدن "چه فکریه که نمیذاره شب‌ها بخوابین؟"جواب‌هایی که دادن جالب و دردناک بود؛
میدونم پول دار شدن زمان‌بره ، ولی خب به این فکر میکنم که مامانم داره پیر میشه...
من چی کم داشتم که بهم خیانت کرد؟
برادرم که فوت شده، هنوز مراقبمه یا نه؟ دوسم داره یا اینکه واقعا ولم کرده؟
اینکه الان من بهش دارم فکر میکنم، اون داره به کی فکر میکنه؟
یه دختری هست که میخوام خوشبختش کنم، امیدوارم لیاقتشو داشته باشم..
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69756" target="_blank">📅 22:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69755">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">⏺
ژنرال برد کوپر، فرمانده فرماندهی مرکزی ایالات متحده، در اسرائیل فرود آمد تا جلساتی را با ژنرال زمیر، رئیس ستاد، و مقامات ارشد نظامی اسرائیل برگزار کند. این مقام آمریکایی پس از برگزاری جلساتی در بحرین و امارات متحده عربی، به اسرائیل سفر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69755" target="_blank">📅 21:19 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69754">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11c35a859.mp4?token=H9Zm9KTeJ0rg9_L-tBTjX94tD0XbU42NAjfxhGy0th5zgT-VPTmNZk6X5ZNmXP40ppiAEdCB9RAXH57LubnOxDczs443O_Rx32jGeqTCH0VFPrAE9difSGEe-7R3ZmXGYunpg6rH3YxYpnX_cD9FhN8oFmdhEaGEjOGs2vxJg2xJN31PGQzT3Bh92fHbAhUotNpebX3inNwgj03Xf7v-3NtFWlLpvZTgAoKoMNWYOJD44KBp7qUmwMgo-u1htrcS9-sTjxObAcHdjldQrmRyh0VljZ37GjDPOiORzXhIQoECoRyfnpUB7B77l5i3cu0HeuJ4b-kylLA50b49XVvuU6ebPAjrfjTR6vS0_yzMaxrqxYTCSApjGkpIr6rQUd-aV6R1i_V5T7vP7ISnoK2CcDBoHxMeQfPngqwqeeMNZn9183iFja8hsjssG0LvblAkWfCUsjxfdtiWwCnY2cH4g5SfWMW5TE7PPIBkfkLSBCBrvSzMJ2AIditgoPovjm5dtKvE4Erle7Mw73xoab-vyTbV9LLw9I3x3G4aDulSZsMbeZN8sOscebyGpx1vDQG9EUoFCbaj6iwrfjEMFzMn9vabChBNTKP0aSKFYkXJCG28RFZhJA8o-8L6RPoDZocFV-ZTk9GYw28i4i-6i-dWUw21ly8uzVi8BMZGsytEgt8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11c35a859.mp4?token=H9Zm9KTeJ0rg9_L-tBTjX94tD0XbU42NAjfxhGy0th5zgT-VPTmNZk6X5ZNmXP40ppiAEdCB9RAXH57LubnOxDczs443O_Rx32jGeqTCH0VFPrAE9difSGEe-7R3ZmXGYunpg6rH3YxYpnX_cD9FhN8oFmdhEaGEjOGs2vxJg2xJN31PGQzT3Bh92fHbAhUotNpebX3inNwgj03Xf7v-3NtFWlLpvZTgAoKoMNWYOJD44KBp7qUmwMgo-u1htrcS9-sTjxObAcHdjldQrmRyh0VljZ37GjDPOiORzXhIQoECoRyfnpUB7B77l5i3cu0HeuJ4b-kylLA50b49XVvuU6ebPAjrfjTR6vS0_yzMaxrqxYTCSApjGkpIr6rQUd-aV6R1i_V5T7vP7ISnoK2CcDBoHxMeQfPngqwqeeMNZn9183iFja8hsjssG0LvblAkWfCUsjxfdtiWwCnY2cH4g5SfWMW5TE7PPIBkfkLSBCBrvSzMJ2AIditgoPovjm5dtKvE4Erle7Mw73xoab-vyTbV9LLw9I3x3G4aDulSZsMbeZN8sOscebyGpx1vDQG9EUoFCbaj6iwrfjEMFzMn9vabChBNTKP0aSKFYkXJCG28RFZhJA8o-8L6RPoDZocFV-ZTk9GYw28i4i-6i-dWUw21ly8uzVi8BMZGsytEgt8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
شاهنشاه آریامهر: اون روز دیگه من نیستم ولی حقیقت هست
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69754" target="_blank">📅 21:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69753">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EI12c-f_kw6CQupxfGxeHhs4lLB0IhuvQxaPeL3vjTC0KRris93BmimfDt7DET9-Gvvja8s2GnLH-tmg0ANkT7WAqvUkjtQzOm1q5LcYgb5z_3QAZvmVl7qPo0tOZ8XcuETCtAXStfnx-RV_ehrhoxQHQ8Fr4Hrji7pQRQvfNx6u1knBbx4Iq-kQcd0el0DX9EL4mvasaJ9NKY759YKkJqipVibz8R2eHjPT37Xr-lJP2G5MHk5SLD4KLEpw0hWkpU6WcvztKScSSsWiR8QWMiFxgMkyYyujla03-HkGKzQy4ZSBai-oi6PbnGx7kv_uUQXyP0p2pAzzOJCtHZPs7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کانال ۱۳ اسرائیل:
اسرائیل خود را برای احتمال اقدام یک‌جانبه علیه ایران آماده می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69753" target="_blank">📅 20:56 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69752">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1727b3200.mp4?token=MWEU8MEr130kJr7ZuHpf5iyHhbJ4uEW4HMPmgaAnGRowXdnQxPaRRV6AXSyevZkGjhvZQbd8jhbZQ2nHGJFgueUWmYrx7Xdt0ldhkv7Snd2zG2AYkr7eHMsK93fZchB_MemU3xb14_1B5ccKrmhphpUB_vQV-4xzFvsG4MGbPe9geCxAOJz8kf45vX4kpOw753nRQu1OiOZymRFBAvAU4AjRyuyfWX45uTNFe2uH3AQenJfxTce8m6WZTas5l810KK6ArTe13QVFOtP95oQw_zSsMJY1U80IcbHTQFiggJ3bpkmG-mY0GKqhYvZb9PRiLs9jAvdo3sW7DIWcBZ5rJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1727b3200.mp4?token=MWEU8MEr130kJr7ZuHpf5iyHhbJ4uEW4HMPmgaAnGRowXdnQxPaRRV6AXSyevZkGjhvZQbd8jhbZQ2nHGJFgueUWmYrx7Xdt0ldhkv7Snd2zG2AYkr7eHMsK93fZchB_MemU3xb14_1B5ccKrmhphpUB_vQV-4xzFvsG4MGbPe9geCxAOJz8kf45vX4kpOw753nRQu1OiOZymRFBAvAU4AjRyuyfWX45uTNFe2uH3AQenJfxTce8m6WZTas5l810KK6ArTe13QVFOtP95oQw_zSsMJY1U80IcbHTQFiggJ3bpkmG-mY0GKqhYvZb9PRiLs9jAvdo3sW7DIWcBZ5rJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حاجی‌دلیگانی، نماینده مجلس:
قدرت چهارم جهانیم و حق وتو می‌خوایم!
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69752" target="_blank">📅 20:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69751">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8f98a7872.mp4?token=sfEudmcnJ5GARDBwaxu2XzIX-y9_xSZsKMY5MwU61gNx2dAunW4Woi5gpsGs1q2A8mWRg94uLrMbo-VQtj5Mr2GQ1k6RU-BVt46XDGxVmpelsJtfRRj-s2qYzX4Zkv9YsmOldZpzxyZhR-Abb15ECsTycNwZxHU9s78oRHMPlyPZqNhz2KGe9eTDQZJVVD7svkObAH_oQBRY969AJU43w_FHE_stDbrT6oBToXHV92jnLq4_aOE9jiaX3yshnVR_LwPEjSmn4IcC3B9GYcqbogflL2KhKK6qUIg_gjcpkeQnhIjFFcgFi5f3ClCOxFUmjtH5wZuH02I0Dz2VmHjcKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8f98a7872.mp4?token=sfEudmcnJ5GARDBwaxu2XzIX-y9_xSZsKMY5MwU61gNx2dAunW4Woi5gpsGs1q2A8mWRg94uLrMbo-VQtj5Mr2GQ1k6RU-BVt46XDGxVmpelsJtfRRj-s2qYzX4Zkv9YsmOldZpzxyZhR-Abb15ECsTycNwZxHU9s78oRHMPlyPZqNhz2KGe9eTDQZJVVD7svkObAH_oQBRY969AJU43w_FHE_stDbrT6oBToXHV92jnLq4_aOE9jiaX3yshnVR_LwPEjSmn4IcC3B9GYcqbogflL2KhKK6qUIg_gjcpkeQnhIjFFcgFi5f3ClCOxFUmjtH5wZuH02I0Dz2VmHjcKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
معاون رئیس جمهور آمریکا آیت‌الله جی‌دی ونس:
در کنفرانسی، لحظه‌ای پیش آمد که من و یکی از دوستانم داشتیم درباره مسیحیت و مذهب کاتولیک صحبت می‌کردیم.
درست در همان حینِ گفتگو، لیوانی از روی دیوار پایین افتاد.
می‌دانید، فکر می‌کنم یک فرد خداناباور (آتئیست) احتمالاً آن را این‌طور نادیده می‌گرفت که: «خب، چه اهمیتی دارد؟ لیوانی از روی دیوار افتاده است.»
اما در آن لحظه، احساس کردم که گویی خداوند سعی دارد پیامی برایم بفرستد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69751" target="_blank">📅 19:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69750">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b83cf8ea7b.mp4?token=bs3JZiBFj5xt5wGXJrmHKG2FFEGDfHIdPGMOZS1k3zddg6swWJhIla8YK0YHTvYscmamETSmmyupwr-mu_e8tkIeLyisPu1S5zOzxdSqgSUBNWIytHUkIL7CB7x1N54wMYyQ0ttLGRRnMt6KHIjHF0e2bQZ8dv9JixiRz3DOfwyptL4NJjxERMWUYRUok5wRWmi8RvJQqzDCp4p6SMDpCnG2GYBoXhXJlSuUFLzdeAzN9Fp_gaDHJQOKRRcGg_LXCW0IOFIvs06b8zHGgEu19IUsAGW2VYrDIrybpFYqDRoUWcBOCfMOBcpxYBDDRLpgdfCP2krQRvCOaxfisJoO4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b83cf8ea7b.mp4?token=bs3JZiBFj5xt5wGXJrmHKG2FFEGDfHIdPGMOZS1k3zddg6swWJhIla8YK0YHTvYscmamETSmmyupwr-mu_e8tkIeLyisPu1S5zOzxdSqgSUBNWIytHUkIL7CB7x1N54wMYyQ0ttLGRRnMt6KHIjHF0e2bQZ8dv9JixiRz3DOfwyptL4NJjxERMWUYRUok5wRWmi8RvJQqzDCp4p6SMDpCnG2GYBoXhXJlSuUFLzdeAzN9Fp_gaDHJQOKRRcGg_LXCW0IOFIvs06b8zHGgEu19IUsAGW2VYrDIrybpFYqDRoUWcBOCfMOBcpxYBDDRLpgdfCP2krQRvCOaxfisJoO4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداوسیما تصاویر مربوط به هواگرهای آمریکایی و اسرائیلی که توسط سپاه منهدم شدن رو منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69750" target="_blank">📅 19:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69749">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69749" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
با این سایت به راحتی میتونی کل ضرر های جام جهانی رو جبران کنی
بونوس هاش واقعا عالیه
👌🏼
بدون قیدوشرط
❌
با هر 1 میلیون شارژ ،
🤩
🤩
🤩
هزارتومان شارژ اضافی بگیر
🅰️
❌
❌
طرح شارژ رایگان فقط تا پایان مرداد ماه</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69749" target="_blank">📅 19:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69748">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0HRaVP2M_3fM6n_kNaYpf_okPyPBJxrfdqqikdtaGM0SgvchN0l8gvDrTrn1IEdxXcMTa_lIftug2UyShBmiD5T6TGVHUCAP9xHT6Q8qRv3O03XAWc0aSSUYGEOTABhHqXx5VMGdBo9qDL-cnJXPNSOaLuFjQUSuPjT8u3ru6WZSfRoZp_Nlv5SaGkbN01DprwMd2S1KJreHgkKGrS9E84bjp6hQ2SAajgxU4NOv1d1kzxO-1WHo7_yZZWfo5grUhbmjGJdpPrnCim7HV8KqIb_IKprE2hfQ8KGzw3A6PeJwlhGBVz_z6c97HtRPSs2d2XArI6UA5x2RTatU8xh8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛍
#اتلتیکو
Vs
#منچستر_سیتی
💰
🛍
#لیورپول
Vs
#موناکو
💰
زمان: یکشنبه ساعت ۱۴
🚨
تجربه پیشبینی مطمئن با
🤩
🤩
🅰️
شارژ اضافی و ریسک خیلی پایین در
#بت_اینجا
رو از دست نده
❌
🤩
🤩
درصد برگشت وجه در  صورت باخت:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
g17
@betinjabet</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69748" target="_blank">📅 19:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69747">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmZStvdLzdYhcnHW87Kw7fwi88fz2VUChi_jm2-31qnJzvJsrZR13gsqTs728xCB1d6Smt8GWuhNUb6RGGKP90Gh_-I01w63Ma_amnXHdLhMrvTFeO8OHhSUvj-PUnCqWCallZVKbfuwvX30K8fncy-XZiIni5pZuFA36qP6A75hJHP58QKxg__18sZaY9XWDi70leLa1-4-78D7imBU8W0KmRDpE9tgrULrnrFzt3yFzv-rjWwuPGbX30KqYdCyNz4Tt0CZiaZteUPxNkeqYdZswDjD-NUefTIV90w-iE7ACe1APAq5QQbYyBBVBBThU8W-WRdNDsAMa9VHOcHArg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
بیانیه دبیرخانه شورای عالی امنیت ملی:
🔴
اگر ایالات متحده رفتار خود را اصلاح نکند، تنگه هرمز باز نخواهد شد.
اصلاح رفتار به معنای موارد زیر است:
عدم تهدید ایران به هیچ شکلی و به هیچ زبانی، و عدم توهین به مقدسات مردم ایران.
پایان دادن به جنگ و تجاوز علیه ایران و متحدان آن در لبنان، فلسطین، یمن و عراق، برای همیشه.
رفع محاصره دریایی و عقب‌نشینی نیروهای نظامی دریایی و هوایی از اطراف ایران.
پرداخت کامل غرامت خسارات وارده از دو جنگ تجاوزکارانه علیه ایران.
رفع تحریم‌های ظالمانه و غیرقانونی اعمال شده بر مردم ایران.
آزادسازی بدون قید و شرط وجوه مسدود شده و ضبط شده متعلق به مردم ایران.
🔴
اینها مطالبات مردم ایران هستند که در طول ۱۶۰ روز حضور مستمر در میدان‌های جنگ و خیابان‌ها، فریاد زده‌اند.
شورای عالی امنیت ملی هرگز عقب‌نشینی نخواهد کرد، نه در جنگ و نه در مذاکرات.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69747" target="_blank">📅 19:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69746">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CExtg6B1-AIa0jI6Mx14RkGUv9rAmCH8ZHotWaD2oRU28D0H3I5hlZfFya6syIQlQq6wCPUtbJMqEs3uA4IgdLf0YWnhGmhZgyG0Rui9dkLCR_kahKOfd982K8ctOnZJeBGsfoZmTuM3-T5yPOrhhKa1u2k2X0pBN_FBD5meaQIJgrdrbprx_yW9mxscKZeVtSit6nYM5L69VX8qBk8uogsX5b0GdOUNM-zriP96ZTZFnZ-WIWSh-jSRlGyNaoB39Hr6fAMtvBaYa2-5jLN6E-r34rNghXCROkJ0a-rcEnPOOTeZlq0HZmJvaoBwZF-XEyJ5IhtDuF87i1XGym7KCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/69746" target="_blank">📅 19:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69744">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUqZ35Ol3JcLHJYizcoU5V5G6-iMLwh0sKWN0hiu1ig1CMfp6n6aaHBkAIyFghF1ibc7tKi_asGYMC-dAHH2s7Zp2hrxkET5uNL5dsAwCgBejQGv8BWu1qCfNMlXfQjqkdPr1WDJOWA4sW7-a8IEoulAvtHOtwqW7xyqvtSO0OhZwci9s27NjUJ2q4K5leMA0gwNNQ_5ag_6LB3udRzLgLRI8NDup-HctLLAPHBy1qCUpBuZyaIZ8oOabg1eSUnEaidjc3_UCfWRcix-kZi_boGs7lu_r_CwnMGVGWTsITAm5e5Rk0Ueldww2GOyT2FirjAgbC03h8AQBOyto37q9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک تایمز:
ایران فهرستی از خواسته‌ها را ارائه کرد که این موضوع، امیدها را برای بازگشایی تنگه هرمز کمرنگ‌تر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69744" target="_blank">📅 18:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69743">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhzWKiHu_nhpaR6VBlTuHTVKIgy5aoFRKYKjiOZSXnjqrRRwkCm-cHWnR_uKYHHCu6b6XPR8atsil_svDII1c5tbzjFkSYKW3uP6sU-NzTzQAyBt3zgU9koQRtDOIvItzVWpFcSGgaqRCBZnRswxTt3ugJbnFg-oDHU7VSxEDmt2zRPlkSAcImnpgppEi6JX-PuplIXDw8qgLdZaeG5StmNBAopq9BxoWWarYsmEjWeR_JcDdc1maQ-is8PMHnR_CINk3jKKSAlQm-C3x1fc3vTCVti7gOgT3rKni2FhvDe0qAIPgK5hdiHU98S2_T4W3AJIjceifqc2cmt6WZOjqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سازمان حمل و نقل دریایی بریتانیا (UKMTO):
گزارشی از حادثه‌ای در ۱۸ مایل دریایی شرق خصب، عمان دریافت کرده است.
یک منبع موثق گزارش داده است که یک کشتی مورد اصابت یک پرتابه ناشناخته قرار گرفته که باعث آتش‌سوزی شده و آتش  خاموش شده است.
هیچ گونه آسیب زیست‌محیطی گزارش نشده است. کشتی و خدمه در سلامت گزارش شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69743" target="_blank">📅 18:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69742">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/43af7e53e1.mp4?token=c9vd6slvtRKPXlCf6Uip8ibbzbBn08mlEjr_bD6wI1BxZZJ-bzyd4MxPJxx6Bl8EcMG56pYWbgMnNakW0DYuv1UPvORNdBKZD7qaO0avCilpd73m3NrpbkJiwQfBzXOMDqwYs6INqLN3z5_xr5g6qeZiLbPusFwTskGYPxHXJ5I9xE4ejL2CYu-dx4dHsgtqR-ACt7LyTSyPS2v4Ma6feNj7oJ4FORAQMTUHFp4R0fkKy7OXBBOadFSe-ZbFj_N8JtMRyNGXl6e8jqYgBgSK8j3mKxcw2Ie5euA3pQhFuyLBTnOVQKYQX2Wh1WtjTd9eP4d7p9lm83uOnZFwjZK2lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/43af7e53e1.mp4?token=c9vd6slvtRKPXlCf6Uip8ibbzbBn08mlEjr_bD6wI1BxZZJ-bzyd4MxPJxx6Bl8EcMG56pYWbgMnNakW0DYuv1UPvORNdBKZD7qaO0avCilpd73m3NrpbkJiwQfBzXOMDqwYs6INqLN3z5_xr5g6qeZiLbPusFwTskGYPxHXJ5I9xE4ejL2CYu-dx4dHsgtqR-ACt7LyTSyPS2v4Ma6feNj7oJ4FORAQMTUHFp4R0fkKy7OXBBOadFSe-ZbFj_N8JtMRyNGXl6e8jqYgBgSK8j3mKxcw2Ie5euA3pQhFuyLBTnOVQKYQX2Wh1WtjTd9eP4d7p9lm83uOnZFwjZK2lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
صحبتای یه وکیل مرد:
توی تمام این سال‌ها به این نتیجه رسیدم که نود، برای پسرا معجزه می‌کنه.
پسرا عاشق اینن پارتنرشون بهشون نود بده، اصلا هم براشون مهم نیست کجان، سرکار، خونه و...
من خودم یه بار وسط دادگاه بودم و دوس دخترم برام نود فرستاد، منم گفتم این واقعا محشره، مرسی.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69742" target="_blank">📅 18:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69740">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RA4XGz0D4lfa88hgnlAx8cfFlot84QnEq2fYbafR7FOoQtgoL7gc2feUhHOLkq-DxUyfnh67qi9eoyGroKCkTvzdibJsnpsR6_VtBobUHKNgaFzCT7fj8nSIIzKb3tXpiMdlJG7clCBP7Qw1VE03XOJYHw90VapkiWOcIBsRz-qjtwZTcmOkV4jdcpBd7u7YtuQ7Ngbxuns6BLMCpJnk8zx6ohlimN8nJ2QDHS8fwnK6bM9D2XH8ZzXAEkzfX-UgigugnE6eDYJs1j15BaX2x1x71gflYYMg1W_SWgt8-Bn42VzVLD6wcDwiFmBRhijQSKB9p20AioXU3_fLkfD8Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c7e1449f7f.mp4?token=TnXHrelqNJdHpM1yVXlM5d0iWAjkP3aNaA21s18-PxFiTKGTWxxhtAba-HRNc8FuRIry6sp3xgW7_io6fe1_psAMWHN8q4L8gPa85Ams-m8sLOJZkUbNO3RZmyCPl1e0YfuI-atQlOFS_pjat6OAk0J9V5zt0DNWdXwse5atYd4tDEzZsHh5X4w7uPRgZZBggvvcdy9mDxm3HTBrk5iTl5AGkBrZiOkGwvqSW4_er1pWaFP6f9tk-24qB4WCqsCrPPV5_q8HknZLkLni3bniqUuvUIw3C4UoPnoAYYqqzt-tqUDxTjeBYyoM_rhn4KkL2Mlx7C7Lrk4fy_lHr8JQuw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c7e1449f7f.mp4?token=TnXHrelqNJdHpM1yVXlM5d0iWAjkP3aNaA21s18-PxFiTKGTWxxhtAba-HRNc8FuRIry6sp3xgW7_io6fe1_psAMWHN8q4L8gPa85Ams-m8sLOJZkUbNO3RZmyCPl1e0YfuI-atQlOFS_pjat6OAk0J9V5zt0DNWdXwse5atYd4tDEzZsHh5X4w7uPRgZZBggvvcdy9mDxm3HTBrk5iTl5AGkBrZiOkGwvqSW4_er1pWaFP6f9tk-24qB4WCqsCrPPV5_q8HknZLkLni3bniqUuvUIw3C4UoPnoAYYqqzt-tqUDxTjeBYyoM_rhn4KkL2Mlx7C7Lrk4fy_lHr8JQuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی اوکراین به دو پالایشگاه نفت در روسیه
پهپادهای اوکراینی بار دیگر پالایشگاه نفت سیزران در استان سامارا را هدف قرار دادند که در پی آن، آتش‌سوزی گسترده‌ای در این پالایشگاه رخ داد.
در حمله‌ای جداگانه نیز پهپادهای اوکراینی به پالایشگاه نفت ایلسکی در منطقه کراسنودار حمله کردند که باعث وقوع آتش‌سوزی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69740" target="_blank">📅 17:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69739">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6b8444e04.mp4?token=q3y8WzwlTzzJXKXRthrO1YNzzh5LYk_PPNhAEipiUL-ebVXG-ic6-PEyAxP8Wu-P_nsoKiXv_eIOftZORZdeKYgao5OpnNCnT2Va0q-48lVVdKjXq2qO6w2Z-EZDUkngW4kfPqSZSKy6v1jFGWUZVm1PQCtwFrXWXa-XM-dTnXmVXiQwpsKdvvSJ8JIxCXhQ96tfW33uxkE_snqr_z9ElrZkzY2vx8MVkgw0y3DdUG029LtK5ANn7pXt8DxBxAGPgJ5ESWQRFfGOuX5yCuSPFzOa3gUOGhq_CL2dUy7c3i31SWxCC0i3nBtCFFN_Q7kIZltr7XqP81LRRSDMT2godS8VjOdUbC7o1yBYaESi44ileDsf_gzmoJhmuBpEPGhCnHIDcFMjLUFsNu-2busHDolJdq4fjt2vNpxxcJCHCx_H3OfWoYDLmg7sWRV6LRCqV4GbW3vawuQio8wd19Fa2_XSsappt72NxDi06FiHT9htgEXpyM_Wv-E009JKF3Nadqw0Lu5MHibcUKpdxc7v42ohbge8hiB73ElAWK2K47_v_7cpfQacpezv8LdLdXPzsnIEWCSwifvPDMxRpfKDyna35aQIhFJXPLIwDaOZrRxm0p1yDGo4x8FnrfQOdf9ilbHYVQ1QX4DVyPcedmLE0nEBKFqD6DClPXaZyN7_G9E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6b8444e04.mp4?token=q3y8WzwlTzzJXKXRthrO1YNzzh5LYk_PPNhAEipiUL-ebVXG-ic6-PEyAxP8Wu-P_nsoKiXv_eIOftZORZdeKYgao5OpnNCnT2Va0q-48lVVdKjXq2qO6w2Z-EZDUkngW4kfPqSZSKy6v1jFGWUZVm1PQCtwFrXWXa-XM-dTnXmVXiQwpsKdvvSJ8JIxCXhQ96tfW33uxkE_snqr_z9ElrZkzY2vx8MVkgw0y3DdUG029LtK5ANn7pXt8DxBxAGPgJ5ESWQRFfGOuX5yCuSPFzOa3gUOGhq_CL2dUy7c3i31SWxCC0i3nBtCFFN_Q7kIZltr7XqP81LRRSDMT2godS8VjOdUbC7o1yBYaESi44ileDsf_gzmoJhmuBpEPGhCnHIDcFMjLUFsNu-2busHDolJdq4fjt2vNpxxcJCHCx_H3OfWoYDLmg7sWRV6LRCqV4GbW3vawuQio8wd19Fa2_XSsappt72NxDi06FiHT9htgEXpyM_Wv-E009JKF3Nadqw0Lu5MHibcUKpdxc7v42ohbge8hiB73ElAWK2K47_v_7cpfQacpezv8LdLdXPzsnIEWCSwifvPDMxRpfKDyna35aQIhFJXPLIwDaOZrRxm0p1yDGo4x8FnrfQOdf9ilbHYVQ1QX4DVyPcedmLE0nEBKFqD6DClPXaZyN7_G9E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌐
تریلر اولین فیلم ساخته شده با هوش مصنوعی
!
فیلم Hell Grind
اولین فیلم بلند سینمایی است که تماماً و بدون دخالت ابزارهای دیگر توسط هوش مصنوعی ساخته شده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69739" target="_blank">📅 17:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69738">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpFV5iGRTG6o3umlZzIzsgWdxvpz0ncAqndCODjINM-BBlpX3X3VqSiXZvOCsAmoA_E1RW---Fp_OXhln5FqbgIAtVpQzTFRtGPwlcUlflKgpMJ8GpNzyIJCyrIVSnz17qbngso_dflyvf1mhogHZHgbv3dh8u2IDg0bykhAsqtG5cyT7WpVq2wL9DshYMlkBAsEAXyBOuMI0VD_0t3G3-UUonU2P9Q3Gj-y-L0THyu1B707uY75b-gCkZc4nGTvVdPrYQedMs6Qi5YOcmSVzIa9-_Munka-f-7g2hIzQWZJ5kAQRyKET_LXfv5-NpC_t3lNsWtWCgAmNxXbSQXg_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇦🇪
طبق گزارش الجزیره، ایران امروز صبح به یک تانکر نفتی دیگر متعلق به امارات متحده عربی حمله کرد.
این چهارمین تانکری است که متعلق به شرکت ملی نفت ابوظبی (ADNOC) است و تنها در این هفته مورد هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69738" target="_blank">📅 16:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69737">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a24c34d2da.mp4?token=LoZSritnq67ulT06u8wCi8491tS8pgX9UBsCjHrW4FZHqptkAcy9QbZ2BiUcySi2xgMmOgYiEEmPCJfT5Fu6hoSpIuM5aQARSUko91mY0oMvIwCWB8fobknNBsPKpphOHwJBjJpeOnVTgIrg5UTfwWNiy-Mlqelm4zO4q1cbR1PrmvciD4ZSU20Qdgg3PV04lQ3sXx_5Cg-0Pb_VVUBGJo1OKTdAGJ9EExC1nJVZyTRZqSrsCCeKsHQLasHDXHKnduSHHNagDsxjsy6ltYhdRC3f0Sb5T_YmVa8st1xY22ZlEvFkJrrePZ_R37Xb1naW4Lcafn7VCGSaZ0wcUK4P6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a24c34d2da.mp4?token=LoZSritnq67ulT06u8wCi8491tS8pgX9UBsCjHrW4FZHqptkAcy9QbZ2BiUcySi2xgMmOgYiEEmPCJfT5Fu6hoSpIuM5aQARSUko91mY0oMvIwCWB8fobknNBsPKpphOHwJBjJpeOnVTgIrg5UTfwWNiy-Mlqelm4zO4q1cbR1PrmvciD4ZSU20Qdgg3PV04lQ3sXx_5Cg-0Pb_VVUBGJo1OKTdAGJ9EExC1nJVZyTRZqSrsCCeKsHQLasHDXHKnduSHHNagDsxjsy6ltYhdRC3f0Sb5T_YmVa8st1xY22ZlEvFkJrrePZ_R37Xb1naW4Lcafn7VCGSaZ0wcUK4P6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های ظریف درباره سهم ایران از دریای خزر:
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69737" target="_blank">📅 16:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69736">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a9432f087c.mp4?token=Osx54qgmuQC-01J1C4xZzsJdpGk6oj1qZVfGC1GyqDTFt5ddLx0gK2E7iSCOP1Uwy5GydpE2KkFhqQIW81TYx2hdOjA_Ieatr-bEI-_HuMSYhepcXmczpNvBwSdyGT1Nvqh_7kSxwc1hnWTjV3vnYOGywx5pFL2SgasvNdcMroos_HiImWwx93bGwPR4pBIGjmsWpxBIRbfCKqp4g36pMSCln1jpzGTQluIfuU0Vfop4EUfzUCXnR9QR5HCr1RToOjsPRtQeIjPirb3ZpWjbwLV5174dmk_CisH6C5b4TWgPabro0nsNRUMNfCi2q0mFaiVxJLLiA2XM1sIma3CwTA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a9432f087c.mp4?token=Osx54qgmuQC-01J1C4xZzsJdpGk6oj1qZVfGC1GyqDTFt5ddLx0gK2E7iSCOP1Uwy5GydpE2KkFhqQIW81TYx2hdOjA_Ieatr-bEI-_HuMSYhepcXmczpNvBwSdyGT1Nvqh_7kSxwc1hnWTjV3vnYOGywx5pFL2SgasvNdcMroos_HiImWwx93bGwPR4pBIGjmsWpxBIRbfCKqp4g36pMSCln1jpzGTQluIfuU0Vfop4EUfzUCXnR9QR5HCr1RToOjsPRtQeIjPirb3ZpWjbwLV5174dmk_CisH6C5b4TWgPabro0nsNRUMNfCi2q0mFaiVxJLLiA2XM1sIma3CwTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه سکانس از فیلمای قبل انقلاب و داستانِ شب جمعه
😂
اسم فیلم: لج و لجبازی
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69736" target="_blank">📅 15:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69735">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇷
🔴
⏺
‌وزارت خارجه جمهوری اسلامی : کنوانسیون خزر منافع ایران را از بین نمی‌برد
🇮🇷
معاون وزیر خارجه:
در پی تصمیم برخی کشورهای ساحلی، پای بیگانگان در حال باز شدن به منطقه خزر است.
تصویب کنوانسیون رژیم حقوقی دریای خزر به معنای از دست رفتن منافع ایران نیست.
این کنوانسیون حضور نیروهای مسلح کشورهای غیرساحلی در خزر را ممنوع می‌کند.
تعیین خط مبدأ و حدود بستر و زیر‌بستر ایران موضوعی جداگانه است و در این کنوانسیون تعیین تکلیف نشده است.
به گفته غریب‌آبادی، اجرایی شدن کنوانسیون می‌تواند چارچوب حقوقی و امنیتی خزر را تقویت کند
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69735" target="_blank">📅 14:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69734">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🇮🇷
سخنگوی سپاه پاسداران:
بازگشایی تنگه هرمز تابع سازوکارها و شرایط تعیین‌شده توسط جمهوری اسلامی ایران است و ارتباطی با مذاکرات ایران و عمان ندارد.
بازگشایی آن منوط به پذیرش کامل شرایط ما از سوی ایالات متحده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69734" target="_blank">📅 14:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69733">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
قوه قضاییه:
آیت‌الله خرازی به دلیل حرف های کذب و دروغش تحت تعقیب قرار گرفت و براش تشکیل پرونده دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69733" target="_blank">📅 13:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69732">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e778f30e9c.mp4?token=c0wz4X7PMrNZ3iP9_kgsgcDTV-JL-0c5avAv3bi8WCGKJXqNBbKibhM6O1_KGldlVhbHdBI7mxCJoDHpC9jtntcsQoSIGwNK800C2JJWbAMHF2jiOaNNRfDfxNZS0Jo8Tj7HUJz21auRKyrb-BGzt6slSDYnAwqsvHX-lyyhcaDdUHbjCH-KkHPhw3apNWyEjb28KVk6grv7FjXnWuH2W4U8wm8j_PzzaHtycLX2GRJJWt7roxBHrmp7ID5dk093rNQMimO6tTA3CcEfxIiqkNho2C3NTTenDn3_nfkC3UyjAGRL2DM77FqAegHYVzhmThviUodWKq8bthGspsKu3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e778f30e9c.mp4?token=c0wz4X7PMrNZ3iP9_kgsgcDTV-JL-0c5avAv3bi8WCGKJXqNBbKibhM6O1_KGldlVhbHdBI7mxCJoDHpC9jtntcsQoSIGwNK800C2JJWbAMHF2jiOaNNRfDfxNZS0Jo8Tj7HUJz21auRKyrb-BGzt6slSDYnAwqsvHX-lyyhcaDdUHbjCH-KkHPhw3apNWyEjb28KVk6grv7FjXnWuH2W4U8wm8j_PzzaHtycLX2GRJJWt7roxBHrmp7ID5dk093rNQMimO6tTA3CcEfxIiqkNho2C3NTTenDn3_nfkC3UyjAGRL2DM77FqAegHYVzhmThviUodWKq8bthGspsKu3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مقایسهٔ قیمت های سال 1400 با 1405:
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69732" target="_blank">📅 13:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69731">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6SrGjokEvkQzGnQT7WsYFJVq_dlsohEA8N1yD9Hu_AlkOdvbY22_SZ1WXvsEQTqex-gW2zjRzJK2Ie9Fm2_27QHRIhQ5XGQ2P_kGt14tKvEQ53LKkw-4L-5NH1MXU9H9Ea_BWpNDW4HxPoTm0f_2DqYsq6SzfU4Vo-kMIitbZ4pGyv_nPit4TSE4srhP-1drxpl6v2DlLM8BwcHxxfH4fD_gOnNNpfjcbVOqoiERIIujKwr9IXrkFcNEndBeO8cvOk2jbW0qVFnX9eYmtZPsaA7E6GyMHlzlX7GbE5mpszWTaAluqZeNDB6qX5K3Sbw6iyROh0aZHFISheEAgM0MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
تعداد زیادی از سوخت‌رسان های آمریکا از ایالات متحده و اروپا در حال حرکت به سمت خاورمیانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69731" target="_blank">📅 13:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69730">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb80381b74.mp4?token=vqlxkwrvkuP6I8r5cGkewRqfddbk2TD7hhKAsrML8ijh947tNAV-wjelX1J2E_HL17GmjtMoOO1sZv3jKhv_el3jIMU7yfjIrScz4vgKzfUFNFAnkB8PgfSTEEQfgAPFoNxFYawmdtukfa64HDT20X-pIl53pp2GwuSt9BvSP053vTrTaU92_JvY1xst83znYDj0Dcx4MII4aVQDK1s2V6v4RX_p4UREolvqwnE-gl5b6fNDe_iDZLcvR5IAnIcXtsCCxHizAwUPA4IaYYztvbgHnWrTL5odTIqdBLBT7ICuhaTO1krYsgT-LwX-ydHoc12Ynov6oa5IYoK7nbRnyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb80381b74.mp4?token=vqlxkwrvkuP6I8r5cGkewRqfddbk2TD7hhKAsrML8ijh947tNAV-wjelX1J2E_HL17GmjtMoOO1sZv3jKhv_el3jIMU7yfjIrScz4vgKzfUFNFAnkB8PgfSTEEQfgAPFoNxFYawmdtukfa64HDT20X-pIl53pp2GwuSt9BvSP053vTrTaU92_JvY1xst83znYDj0Dcx4MII4aVQDK1s2V6v4RX_p4UREolvqwnE-gl5b6fNDe_iDZLcvR5IAnIcXtsCCxHizAwUPA4IaYYztvbgHnWrTL5odTIqdBLBT7ICuhaTO1krYsgT-LwX-ydHoc12Ynov6oa5IYoK7nbRnyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه آخوند
:
قبل از انقلاب باید شب و روز میدویدی تا خودتو خانوادت از گشنگی نمیرید،الان وضع مردم خوبه.
وسط جنگ با ابرقدرت ها واسه خودشون میرن تفریح و در آسایش و آرامش و کاملا شاد هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69730" target="_blank">📅 12:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69729">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fce1bb2a9c.mp4?token=bLEvH-BVsciTMLQekJGDJdtY43cUpd5CX_3NhwHxTuBBvzr6agbql2iCZYTzM1RhryIZONEKq7LzmBnuGvQq5G_EZGvvG-F4NgpNvuH4H3UHmO5785u4kfMrnGbAt3FYU9v1LfdKoPNoQJ6CjI3piLg0hALG9dCt6TBykNF_X4pNhT_OKM5Z9gp-uX73UKdtyaQV5crD1zYf6w7kpNnVTbVci25Yfky2ck5MBQMwCUApxxNUhx-UbaZOkyzo39iIgN3leYQ9VbUbvlSHyG5tf78aAlLH6AjkfvYx0Iuvwc8I1G28SZwoKbS5R-hYLRc24cU8C40Mew0-mQFVTSNYQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fce1bb2a9c.mp4?token=bLEvH-BVsciTMLQekJGDJdtY43cUpd5CX_3NhwHxTuBBvzr6agbql2iCZYTzM1RhryIZONEKq7LzmBnuGvQq5G_EZGvvG-F4NgpNvuH4H3UHmO5785u4kfMrnGbAt3FYU9v1LfdKoPNoQJ6CjI3piLg0hALG9dCt6TBykNF_X4pNhT_OKM5Z9gp-uX73UKdtyaQV5crD1zYf6w7kpNnVTbVci25Yfky2ck5MBQMwCUApxxNUhx-UbaZOkyzo39iIgN3leYQ9VbUbvlSHyG5tf78aAlLH6AjkfvYx0Iuvwc8I1G28SZwoKbS5R-hYLRc24cU8C40Mew0-mQFVTSNYQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📰
مراد ویسی تحلیلگر ارشداینترنشنال: جنگ جهانی سوم در راهه!
هر چقدر اتفاقات و شرایط رو بررسی میکنم، دقیقا مثلِ قبل از جنگ جهانی اول و دومه.
توافق و تفاهم نامه همش کشکه، هیچکس تو خاورمیانه حاضر نیست سلاحش رو تحویل بده، یه جنگ عظیم و جنگ جهانی سوم در راهه!
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69729" target="_blank">📅 11:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69728">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41f0d554f1.mp4?token=INzTWqWu7zbu5fnz89Fo3k4uloAeKHZA4K-Xo6DSyicmczWgk7LwQmzJyxvCyzZzawrCcZeIvgablgFluHBh_EnUsSPxoBHvx40L3jiqWC6A0U_QTBpOgx5Um-x9l-OZWSH57GYNE76e8N67c1AYiHHZGMyzwM0d8Yoit9DSFi48CluVTr7hkAHQGAG2j6_0fr-qTFrCN_opxAbUnKMJgFOobWIMZjkf6VELpR_3U_il6LEvh_tUebL2mzUe6LhQ9dPrBK7Q1KUjyG9KPPTIzAvYoT-yRFmGHhzKxulMeWmrbDxVAynXhcgzQNdFTjO4vuimMGJvO6JYqbUC9qFmfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41f0d554f1.mp4?token=INzTWqWu7zbu5fnz89Fo3k4uloAeKHZA4K-Xo6DSyicmczWgk7LwQmzJyxvCyzZzawrCcZeIvgablgFluHBh_EnUsSPxoBHvx40L3jiqWC6A0U_QTBpOgx5Um-x9l-OZWSH57GYNE76e8N67c1AYiHHZGMyzwM0d8Yoit9DSFi48CluVTr7hkAHQGAG2j6_0fr-qTFrCN_opxAbUnKMJgFOobWIMZjkf6VELpR_3U_il6LEvh_tUebL2mzUe6LhQ9dPrBK7Q1KUjyG9KPPTIzAvYoT-yRFmGHhzKxulMeWmrbDxVAynXhcgzQNdFTjO4vuimMGJvO6JYqbUC9qFmfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
نویسنده امریکایی
:
ایران مهم ترین مهره روی صفحه شطرنجه
!
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69728" target="_blank">📅 11:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69727">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
نیروهای ویژه دریایی اوکراین از تاریخ ۶ جولای تاکنون، به ۲۱۸ شناور در دریای سیاه و دریای آزوف حمله کرده‌اند. همچنین، بین ۱ تا ۸ آگوست، ۱۲ شناور دیگر از ناوگان سایه مورد هدف قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69727" target="_blank">📅 11:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69726">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69726" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69726" target="_blank">📅 11:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69725">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc7f1c8ee4.mp4?token=XAxqfBoIWQc7QFL4r-pFS8XXvWajeSzbLixzJ-ZVi4c2m_ECCz2kaUftaRUVBkzOC9SruEFs9sKgl72oBlbEYvl_0WvqHYPULPFRo4I3UHCkdCvm6KgxkufhQhy-LBz8JlPhengRj4ZIa5fHWgZwMvVEV2AU9pKapGhXWkldKXFxIaXX4SywXJ3_GKr08OabwBYQVRWJWeclggU-tyZmy4Wepo0NEhJBcro3Ck3zVMZnvZl-lbbcoUapBtUtbUaL0EWEzioNYjalHCd2180oP3LDonzplLue-GIjYli4zkSWlkit3anHaDIfUmu3dfV2B7RQhl4Pd4DSO_TYoOYCkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc7f1c8ee4.mp4?token=XAxqfBoIWQc7QFL4r-pFS8XXvWajeSzbLixzJ-ZVi4c2m_ECCz2kaUftaRUVBkzOC9SruEFs9sKgl72oBlbEYvl_0WvqHYPULPFRo4I3UHCkdCvm6KgxkufhQhy-LBz8JlPhengRj4ZIa5fHWgZwMvVEV2AU9pKapGhXWkldKXFxIaXX4SywXJ3_GKr08OabwBYQVRWJWeclggU-tyZmy4Wepo0NEhJBcro3Ck3zVMZnvZl-lbbcoUapBtUtbUaL0EWEzioNYjalHCd2180oP3LDonzplLue-GIjYli4zkSWlkit3anHaDIfUmu3dfV2B7RQhl4Pd4DSO_TYoOYCkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
اگر
#تندو
تیز هستی اینو ببین
💵
💰
✊
این بازی فقط سرعت عمل بالا میخواد
😍
🟢
ویدیو
#آموزش
بازی AVI رو براتون گذاشتم خیلی راحت با سرعت عمل بالا بدون ریسک کلی پول دراورد به همراه
🤩
🤩
% شارژ اضافی
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
r17
@betinjabet</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/69725" target="_blank">📅 11:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69721">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dab2dda1d.mp4?token=BdVszowdbaUdd1D8bkCTpSr9nNYDPynCKdkRdl4VgSL-hLsf0TowwAHGtOhLGxDZI_4CGIXlXwuN6Z4aLuo8p6HvDV_IjMvsQ-nyQ2K4vrFA5YIxhGb2M2otg2cAAjQLaFV8j-uJjRHTZ_0RdtMPhNR1GQZ6JJ_1QUbgevL5-zUztf0gbj04uIAzABlA1NMitBpPYyTGytaISPDzjr2fkJEe6PxoNL7HUaQC7AUy9IGFIGnCFHjUOopBq5Fh-YuaXO4aIQty35-kF1lfQyG3xa6JqUSzDXEHysVHzKa81sVlI8QWsaEQQaOnR0a2FlApliTun-p4BXT-_unSKw_nCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dab2dda1d.mp4?token=BdVszowdbaUdd1D8bkCTpSr9nNYDPynCKdkRdl4VgSL-hLsf0TowwAHGtOhLGxDZI_4CGIXlXwuN6Z4aLuo8p6HvDV_IjMvsQ-nyQ2K4vrFA5YIxhGb2M2otg2cAAjQLaFV8j-uJjRHTZ_0RdtMPhNR1GQZ6JJ_1QUbgevL5-zUztf0gbj04uIAzABlA1NMitBpPYyTGytaISPDzjr2fkJEe6PxoNL7HUaQC7AUy9IGFIGnCFHjUOopBq5Fh-YuaXO4aIQty35-kF1lfQyG3xa6JqUSzDXEHysVHzKa81sVlI8QWsaEQQaOnR0a2FlApliTun-p4BXT-_unSKw_nCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این روزها قبل از ورود به هر بالا پشت بومی، سعی کنید در بزنيد؛
چون قطعا یکی اونجا هست که داره سعی میکنه سیاه بشه
😔
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69721" target="_blank">📅 11:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69720">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aa229942a.mp4?token=PXTCCIYZL4Rn1cwCq4FBdTID3EpjtzVMsjLKLOdwwHO56ITnjE0clhjEMdTiwdkBTdk9GyRBhQdmSWoZyb7l7jc-wpigd8WnaDpTuSLGioTpT74I0hxmIP6eQ2YbAma2bJCfY3lNd1tvf13bNK9W0PR0PtNlqR1AB3uTgVOYhdA-Vuc3UuAO1Et7fuPEgihEBHmd8F09EmDqsJhDhUOYa8MQviT4Fyeit-dOWk9SIcNW4RVukjwfrC1zpEHE446Bi0_iNqZgHV1cApkDegNndSaiEbsyPbjkSAC8T-nUm-eVIIwR8KrT5SkgRM8aWnjWE-KeLeGOuD6eDzvfyjyqhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aa229942a.mp4?token=PXTCCIYZL4Rn1cwCq4FBdTID3EpjtzVMsjLKLOdwwHO56ITnjE0clhjEMdTiwdkBTdk9GyRBhQdmSWoZyb7l7jc-wpigd8WnaDpTuSLGioTpT74I0hxmIP6eQ2YbAma2bJCfY3lNd1tvf13bNK9W0PR0PtNlqR1AB3uTgVOYhdA-Vuc3UuAO1Et7fuPEgihEBHmd8F09EmDqsJhDhUOYa8MQviT4Fyeit-dOWk9SIcNW4RVukjwfrC1zpEHE446Bi0_iNqZgHV1cApkDegNndSaiEbsyPbjkSAC8T-nUm-eVIIwR8KrT5SkgRM8aWnjWE-KeLeGOuD6eDzvfyjyqhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رجب صفروف، عضو تیم روسیه در مذاکرات رژیم حقوقی دریای خزر، (مرداد1397):
همه ما انتظار داشتیم ایران درخواست پنجاه درصد بکند. قانونی هم بود.
اما جلسه اول یکباره جمهوری اسلامی گفت تقسیم برابر بین پنج کشور، یعنی کمتر از بیست درصد.
برای ما عجیب‌ و غریب بود که چجور ایران دارد از حقوق خودش گذشت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69720" target="_blank">📅 10:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69719">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6ISICtkhzS4q-Uzt_-xf6qboDciX-4CzNfBiSK_MXLVgiakARce4b54GfDwqRKKmHPzVlXdkcUZcS1ZbOkkzrZLki31Kl5LJGSj6P2-f_C-cmgNl7NXcVgPQS3qD_NAzb_5tBfRA-9iYHMCHjz8QmYpay_3dRxVnaMY_Z_RgR0pdoQmF08Q6jDS1qh7QMNFBUobOH0v3VdNs083T_h3b_0KQejWnlNLTdFpBmkD2k7CuS_LihZ3C4n-rMQUFYjDvMHdXoOQZ50x2InxbfAazbIviLepf1FMKavlDZw5j0tTvyxMYHHIUXySAf2awPNfZKaSeO1j97fzJD4HtLZjiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سپاه ساعاتی قبل یک کشتی دیگه رو توی تنگه هرمز هدف قرار داده؛
گزارش‌ها حاکی از آن است که ایران به کشتی‌ای در تنگه هرمز و نزدیکی سواحل عمان که قصد عبور بدون مجوز را داشت، حمله کرد
ه
است.
یک شناور تخصصی که برای مقابله با نشت نفت و اطفای حریق طراحی شده، در منطقه‌ای که نفتکش هدف قرار گرفته، در حال فعالیت است.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69719" target="_blank">📅 10:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69718">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9bc484b9d.mp4?token=PHis7DuQEa9slkCrtJZrhDN79jM_rb5VV5HmLNgw5Btv4p4jEdKRyE6fKGzgUHOX60cQY2aBxQH3RXCFmPqXt9EreZR54mh65LLcDjm0QOcx5qRnUi2ikHWqs_t9Qae22qxFxeANOr6D7sLNoQhE_HrJ9XaA4izVHJc4RGXJqjZruagYGtN_owq3mzMQDQEdLXhl82r-eBihkBoNTFPoV3Tv0u_hBE1rLhvLwa-kqwj8cPcRpObWVEe2dCY1a7oCrEaX89dMlhZ_UrNtqozIcl5RmJQkajwrMEN9UnexcbpHJlMGo5pkqWQLzuldfEzV-nQ4vPAY_ZkqRBFrp7itzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9bc484b9d.mp4?token=PHis7DuQEa9slkCrtJZrhDN79jM_rb5VV5HmLNgw5Btv4p4jEdKRyE6fKGzgUHOX60cQY2aBxQH3RXCFmPqXt9EreZR54mh65LLcDjm0QOcx5qRnUi2ikHWqs_t9Qae22qxFxeANOr6D7sLNoQhE_HrJ9XaA4izVHJc4RGXJqjZruagYGtN_owq3mzMQDQEdLXhl82r-eBihkBoNTFPoV3Tv0u_hBE1rLhvLwa-kqwj8cPcRpObWVEe2dCY1a7oCrEaX89dMlhZ_UrNtqozIcl5RmJQkajwrMEN9UnexcbpHJlMGo5pkqWQLzuldfEzV-nQ4vPAY_ZkqRBFrp7itzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شادمهر عقیلی، قطعه‌ی گل یاس از البوم مسافر رو که سال 1377 منتشر کرده بود، بعد از 28 سال دوباره بازخوانی کرد و تو اینستاگرام منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69718" target="_blank">📅 09:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69717">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0959732695.mp4?token=PYZNBbGcTaeQKlu5PjCKQagW9R2mN68kUz9ye4RjbH-Pw0dbyHslKog3W4YLJrvi-GaadpyxnzU2clKvC7zu6xB8UYd407Bt9GKXXj0Hkxqd-zbgoh6XkSY-RJwzTEY7exllSH8rtTENvg2v2odkvUpNMqpGHa6H7kek242neiZF5234-Fu-WqK3adaEKMZzq_Vo4-WY3BW1wpwkyJiKh7PhyBtkXDCjlDT9E1N7JVNmrneNw9KeEvm72RlMc4p_RQVCHlC5fzYnCF3vsTC3iHVfI2TvqYFO-1dxk44-Bu8GSnyubRkYBbdH7cwX-t3Odz74F4qDTfUdgr-KnXbedA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0959732695.mp4?token=PYZNBbGcTaeQKlu5PjCKQagW9R2mN68kUz9ye4RjbH-Pw0dbyHslKog3W4YLJrvi-GaadpyxnzU2clKvC7zu6xB8UYd407Bt9GKXXj0Hkxqd-zbgoh6XkSY-RJwzTEY7exllSH8rtTENvg2v2odkvUpNMqpGHa6H7kek242neiZF5234-Fu-WqK3adaEKMZzq_Vo4-WY3BW1wpwkyJiKh7PhyBtkXDCjlDT9E1N7JVNmrneNw9KeEvm72RlMc4p_RQVCHlC5fzYnCF3vsTC3iHVfI2TvqYFO-1dxk44-Bu8GSnyubRkYBbdH7cwX-t3Odz74F4qDTfUdgr-KnXbedA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مسعود پزشکیان:
تا وقتی میشه حرف زد چرا جنگ؟
ما با همین گفت و گو تونستیم جلوی جنگ لبنان رو بگیریم. (اسرائیل از همون موقع تا الان تقریبا هر روز داره لبنان رو میزنه).
تونستیم محاصره رو برداریم. (ایران درحال حاضر تحت محاصره دریاییه)
تونستیم پول‌هامون رو برگردونیم. (هیچ پولی از پول‌های بلوکه شده به کشور برنگشت)
تونستیم قسمتی از تحریم‌ها رو حذف کنیم! (درحال حاضر تحریم ها بیشتر از قبل جنگ شده)
بعضی‌ها تو داخل کشور فقط میخوان که ما بجنگیم
،
اتفاقا اسرائیل هم همین رو میخواد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69717" target="_blank">📅 09:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69716">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👑
آخرین مصاحبه شاهنشاه آریامهر محمدرضا پهلوی با دیوید فراست (پاناما1980) زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69716" target="_blank">📅 09:01 · 17 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
