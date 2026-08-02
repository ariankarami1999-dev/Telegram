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
<img src="https://cdn5.telesco.pe/file/t9V3qwRjqkK3Gm4E0f9xr6BO-LmX9NjH0IqfYWSeWlsIiSvL_YOIVhZ1R-3F8MBPhgvlotiG2ZurOOXQ-OoTbaBIX-tMSKqbYpGvVPOGbS57znO2LKARPlNPdroTfHYV5ts-gfEf7-XqzdGCRqBAM20tscYAu12dUkHjTSDDR9Aj-VNj7oL9I4pZdF8cPOpaGKa3e9e3rldKuTi3VGlWrNu53nhPT5H4cJiiTWpxYaMDY3ewNCMpD5rYCtExd_sNS-dPgS2Vqjt2uJkyFca9KmZlu5J3YxIcARAHVqpaJUlnIltmy8pqnrHNqxDi9H7xA0MxNKnD5DttpJ23a847yg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 503K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 10:57:27</div>
<hr>

<div class="tg-post" id="msg-102546">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2090c572a4.mp4?token=XroAY9u-8DgYpJtxbAovszkiZuV-loKCtMbmlKgzvp7fA3xAiEo4ATiIaAgw-NI_ZuDGxGZE_p2nzzmb97T4wd9fwvlcRwxTkmhZsqu-OKuJ-TJNGjE4lGB0rrhouQdsdWVz5onQHgGODh_kDI1X9xN6nLcLrkoHLR4lHxIs3rAB_wGz_P-QBQqvUo9Vig3Gs0GzoZSL2aegpBK9SjcX-mA16h4fU_t879dNGXqFkjMPteB6Q0ODxKceKVlJ5FQAi3hOEhYDe46RlT9NCcJ0rJIpiaBjWA1jJ1aDOvelEmCxs_QwM7b0-mXOszD106saoSP4yLmkMilJg1xGdIzvXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2090c572a4.mp4?token=XroAY9u-8DgYpJtxbAovszkiZuV-loKCtMbmlKgzvp7fA3xAiEo4ATiIaAgw-NI_ZuDGxGZE_p2nzzmb97T4wd9fwvlcRwxTkmhZsqu-OKuJ-TJNGjE4lGB0rrhouQdsdWVz5onQHgGODh_kDI1X9xN6nLcLrkoHLR4lHxIs3rAB_wGz_P-QBQqvUo9Vig3Gs0GzoZSL2aegpBK9SjcX-mA16h4fU_t879dNGXqFkjMPteB6Q0ODxKceKVlJ5FQAi3hOEhYDe46RlT9NCcJ0rJIpiaBjWA1jJ1aDOvelEmCxs_QwM7b0-mXOszD106saoSP4yLmkMilJg1xGdIzvXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
تمرینات سخت و نفس‌گیر بادیگارد لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/Futball180TV/102546" target="_blank">📅 10:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102545">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f010d3bc34.mp4?token=sHLKZyBA7IwEiSBJ9BXep9YZ9p3YMGnRYCfXBkd0bq-6f3Px3Rx6deDyd26QxbUaDq85MVofagixtMoZA0u5rrd63AgKDHhMDvAwdwypD-PMWTEEpiokA1nKgb4jPiCkUinIy3TfToP2JbOYoTV10BPPQyJH5e-J35hZeEuCOgyFYmTwvfpB-T_-9zEvdQP8TMd_iWhgFOU8YcJc22_QItBxkWsa-T0dDZgqQuzm638vWN5GhV4i_1tCf4PlOZcaLq-irAKw8SIsHYjktmv-U0BDP7CHRp--wFmBOuyG34awma5Yxwq0PyLBWdfPlKQg9DrRJQ4ODQMiJuIEOUNNrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f010d3bc34.mp4?token=sHLKZyBA7IwEiSBJ9BXep9YZ9p3YMGnRYCfXBkd0bq-6f3Px3Rx6deDyd26QxbUaDq85MVofagixtMoZA0u5rrd63AgKDHhMDvAwdwypD-PMWTEEpiokA1nKgb4jPiCkUinIy3TfToP2JbOYoTV10BPPQyJH5e-J35hZeEuCOgyFYmTwvfpB-T_-9zEvdQP8TMd_iWhgFOU8YcJc22_QItBxkWsa-T0dDZgqQuzm638vWN5GhV4i_1tCf4PlOZcaLq-irAKw8SIsHYjktmv-U0BDP7CHRp--wFmBOuyG34awma5Yxwq0PyLBWdfPlKQg9DrRJQ4ODQMiJuIEOUNNrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لواندوفسکی هم در آمریکا پاش به گلزنی‌باز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/Futball180TV/102545" target="_blank">📅 10:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102544">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a652d9a082.mp4?token=da_snm1DjMbDeDEx8bWfCfcMB53QQXAL4Knkp_eNGEd1PafEmimg2-3DZS7F7SaxY3dMpiokVknUUexauau0kpRWzbcAW86LqIchSdIZvD0E89oqFR1LW_-zhOKYPEpl1HoAFBdJfdHcWoFBcpadtOTAj4zfsgmeaxeuF-ENW1JVmVj51F0F1vut-h_XEKkp_CuiJ6PstWUAjicofHMWBmjV0rXABp-o6PcKEmnq0X8XJGljlJM5nRSbhYrse9Iv1f08YoUpjEnCeTMmPaQqGsWfEATaIFMB-f3x33J0UocVBobLqOCU6KE7QogZTOue_hQpypk-ti-7VGds8Ewkew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a652d9a082.mp4?token=da_snm1DjMbDeDEx8bWfCfcMB53QQXAL4Knkp_eNGEd1PafEmimg2-3DZS7F7SaxY3dMpiokVknUUexauau0kpRWzbcAW86LqIchSdIZvD0E89oqFR1LW_-zhOKYPEpl1HoAFBdJfdHcWoFBcpadtOTAj4zfsgmeaxeuF-ENW1JVmVj51F0F1vut-h_XEKkp_CuiJ6PstWUAjicofHMWBmjV0rXABp-o6PcKEmnq0X8XJGljlJM5nRSbhYrse9Iv1f08YoUpjEnCeTMmPaQqGsWfEATaIFMB-f3x33J0UocVBobLqOCU6KE7QogZTOue_hQpypk-ti-7VGds8Ewkew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
گل‌زیبای لوئیز سوارز در بازی اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/Futball180TV/102544" target="_blank">📅 09:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102543">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ebf3b2b10.mp4?token=YXt4-0nT7LDHdfzKjkRWc2Td2ufOgF2fM4-eR1u1xQjyNrwJ0lR_pMBONntFZta5TthzbssuUgsT9v_CHPErLPAFuQIKPDmkGfw3LbqVWePIxbaU9rKIarkajV6c9-O_N2it-AqajB12JHg_qZUWjTCTun8OB0QXVwmwqj3OYVy3I-Xjy4tDkEKYlgbB1IEi6AA0n7SyQEapDZRAdTk6r9dh6VxZgjw26h1-vMYp_HaiuGM_c5Lw8NWDxCizwKgEckpNfGKmYR7YvO5nwDJvhYfr8worTqO7C1MRE4y2opUijLPECCgOd5SQK3C6P71iUQSrtGS8T6OfI9z1BG1xVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ebf3b2b10.mp4?token=YXt4-0nT7LDHdfzKjkRWc2Td2ufOgF2fM4-eR1u1xQjyNrwJ0lR_pMBONntFZta5TthzbssuUgsT9v_CHPErLPAFuQIKPDmkGfw3LbqVWePIxbaU9rKIarkajV6c9-O_N2it-AqajB12JHg_qZUWjTCTun8OB0QXVwmwqj3OYVy3I-Xjy4tDkEKYlgbB1IEi6AA0n7SyQEapDZRAdTk6r9dh6VxZgjw26h1-vMYp_HaiuGM_c5Lw8NWDxCizwKgEckpNfGKmYR7YvO5nwDJvhYfr8worTqO7C1MRE4y2opUijLPECCgOd5SQK3C6P71iUQSrtGS8T6OfI9z1BG1xVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
⚠️
استاد کاسمیرو دیشب گل‌کاشت و تو بازی اینترمیامی موفق به ثبت گل‌بخودی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/Futball180TV/102543" target="_blank">📅 09:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102542">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q59OSAtfrpCUVoTduRY2AMt69f2btWXtgTsWicBIRsiRBvbyE2kZLBtuHnBjJ4R3TMySAgRXHPEOICG4V9aGxevlSb7Sse0FUy6McXh5NH97S9DYfwJlvXKXb_-oKIo014lLqRawODUwk-LB3NA23CGjwobErFgpvQ6ku61OURlFLSgfVNUTNdNTm3_dpN1oHfgWTlI2LMhU0jZDnqgdby7pxCxwqW-j7EzZp7jtrIMb331sIj8rDYdsThpVR6Iw6QbqcvDVTAtgQUqY7gQe6ML3FmyhlOHz_r07Qt1gQ57WszTuDRcTBCkODRxIj60EGRIKM9fOU-ZO2QBz5drzqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
لیونل‌مسی دیشب برای اینترمیامی در روزی که تیمش به تساوی رسید، حدود ۴۰ دقیقه بازی کرد که موفق به ثبت گلزنی نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/Futball180TV/102542" target="_blank">📅 09:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102541">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f4f92fcd.mp4?token=K8IznZSWnVgNFFhHNSYcQ50euXnqmlg7CeMIUtCfsHl1n9ctJAVlkW78O27fQmFOMeTOa1lrVBUWgFTB-sKCn0YKKSD75LKcqcaAw75gWB2VWLbyeG6lcq4iPRexAU5wqr_b2BjzHZpThfaVg1aXLxesWpSGhun7WEK5DxNAm7BX0vhYPBLCKkAR6iM0rP9EYvZ6ioP5a5ejdECjNLfv8dAoCaU8-UNlY9c_ecrzAeR9prxQOi2R2qhidRWg7-dX5daaOA2JBTCdkJGfZ6Z8OrA5WPoujQHAqe5smA7cDdmk_s5VqE7MvNQD8BAHXvhssRAYk7R3nJyI_Vt92WShEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f4f92fcd.mp4?token=K8IznZSWnVgNFFhHNSYcQ50euXnqmlg7CeMIUtCfsHl1n9ctJAVlkW78O27fQmFOMeTOa1lrVBUWgFTB-sKCn0YKKSD75LKcqcaAw75gWB2VWLbyeG6lcq4iPRexAU5wqr_b2BjzHZpThfaVg1aXLxesWpSGhun7WEK5DxNAm7BX0vhYPBLCKkAR6iM0rP9EYvZ6ioP5a5ejdECjNLfv8dAoCaU8-UNlY9c_ecrzAeR9prxQOi2R2qhidRWg7-dX5daaOA2JBTCdkJGfZ6Z8OrA5WPoujQHAqe5smA7cDdmk_s5VqE7MvNQD8BAHXvhssRAYk7R3nJyI_Vt92WShEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این تعویض کارلتو که خودشم پشماش ریخت و خندش گرفت؛ بازیکن ۱۸ ساله ۱۸ ثانیه بعد از ورود
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102541" target="_blank">📅 02:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102540">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4mqedJitNRF6rkZPo1zftI--9rDYWGAMGlm3EsVq6-1hFepkx7C46JgcqGr7bqlIziJk2NTM3rt3U1zxBXMrsfSh_zkVkcwLbdoEklnNQcKiApsok3XZ2N7BvAknU-S4HNp3ZkGvLtSg-dE4yFzsGCXB5A6BD7Edl5znpR1AtIRd7Dk98KXtve3jARVDSoyIz_102Ny3IsHvSgeDLKSlRSUT_wUXGEO-ZLYmXfUe_LiK6f160s0p7e46HnqGt1Y_s3A5ia3P4wL1OSQYmhfDJGWbY4EHGlGdymRAu4RXR8bKqPVyJLs5_dkI3QOsY2-NkpudajEDKUCFEUlrxSobw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
تیم پورتو پرتغال برای بار ۲۵‌ام قهرمان سوپرکاپ فوتبال این کشور شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102540" target="_blank">📅 01:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102539">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f4c2f037.mp4?token=T3Y7ldJ_JObOz7PCt2gVaM3qIw5QanJvLftxYBCP0xWxM_vv1eFHitbkL7nnCJ4bSB0bJelo2B4QvGHO500mDoLvKd7N04-UaCTlHCnlcpqZBoQS5_9H-GA0Gtw11megndRAy6fxBOVRSRGpzf0l3WbEDZcuhkIlyHkovxD4Ra3XFIAWCmDXG9mEXF4PNKPQucJHaLG3rJEOvX_U4FQf82QDyHWfAMpQDs9kYvC4mRp84ZkP_bxN8jgVs6Vi3KkAN5afOm3y6RqrDmIHlkJTwxd8Z70qt9V3_TdByOqAd59eliSjhXNT2zbmtVRJenFhBtzfEG6AUU423DR_gGvuyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f4c2f037.mp4?token=T3Y7ldJ_JObOz7PCt2gVaM3qIw5QanJvLftxYBCP0xWxM_vv1eFHitbkL7nnCJ4bSB0bJelo2B4QvGHO500mDoLvKd7N04-UaCTlHCnlcpqZBoQS5_9H-GA0Gtw11megndRAy6fxBOVRSRGpzf0l3WbEDZcuhkIlyHkovxD4Ra3XFIAWCmDXG9mEXF4PNKPQucJHaLG3rJEOvX_U4FQf82QDyHWfAMpQDs9kYvC4mRp84ZkP_bxN8jgVs6Vi3KkAN5afOm3y6RqrDmIHlkJTwxd8Z70qt9V3_TdByOqAd59eliSjhXNT2zbmtVRJenFhBtzfEG6AUU423DR_gGvuyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح برگزاری فینال مسابقات زارم کلایه استان گیلان رو ببین
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102539" target="_blank">📅 00:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102538">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93530c3ba8.mp4?token=P_wd8NUSf94dEYxIvCH6OEai1J7J_EUSOiNsm_KNvMUlWTrg32R0BOiJdZd-ksgs7u7Z9z45GR3cTWCTk1x-UpFo9tIjW7EAAyEGYnctobZG6cIXju4x9q12te4WqPafk5h1uDZUJ724FLUh7G9ufyEdnxULbaoWOJCbKywUvCTUmjoWMTfdsgZ5YTuZ0TPN25iyurQk2pamuMNQWeHurTiM2IKlQl2hm7UTg69qGRHVuE6zwe4AfLmTxsNZ2UVQ_Pw2WnwUUf-gooNP54kdopoZ2H8gmPDEk4Y8h4mqZ09KzyfjScjsmrVqCW7dB792GkjXYxV_mzXfIMF3msCAqEqd7gdZbi1dUe9g6DC57gOecC17l_jXlF3Tn4mq3iIJjY-K4X6Gp0BEqBBSK3oNco7cR9l8w5THXER7_lJyKXmm7Gljl8x0k2vzVjDl8EbVeHslPns2ZS4VlhZ8-Rg6SfL4xfjxzGKv4LEBxJ6genSDPaeVqCk4VE7e-BQ28Plqr0Dlwpi2MHDictaYOXUYGH_mO_osDRK8JWdRWoumpi0MPtHuhYd5YYJIa0tTeC4Njj2tD7vyZa8EwhQ3NwPAaTkCStO5vGsb8VjR29BmGmZVkJ_if58CXDUzitmKWDZuWz5vmh9cARg8wDOO12J2A5JSb55VqPDlsR7-NObDUZ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93530c3ba8.mp4?token=P_wd8NUSf94dEYxIvCH6OEai1J7J_EUSOiNsm_KNvMUlWTrg32R0BOiJdZd-ksgs7u7Z9z45GR3cTWCTk1x-UpFo9tIjW7EAAyEGYnctobZG6cIXju4x9q12te4WqPafk5h1uDZUJ724FLUh7G9ufyEdnxULbaoWOJCbKywUvCTUmjoWMTfdsgZ5YTuZ0TPN25iyurQk2pamuMNQWeHurTiM2IKlQl2hm7UTg69qGRHVuE6zwe4AfLmTxsNZ2UVQ_Pw2WnwUUf-gooNP54kdopoZ2H8gmPDEk4Y8h4mqZ09KzyfjScjsmrVqCW7dB792GkjXYxV_mzXfIMF3msCAqEqd7gdZbi1dUe9g6DC57gOecC17l_jXlF3Tn4mq3iIJjY-K4X6Gp0BEqBBSK3oNco7cR9l8w5THXER7_lJyKXmm7Gljl8x0k2vzVjDl8EbVeHslPns2ZS4VlhZ8-Rg6SfL4xfjxzGKv4LEBxJ6genSDPaeVqCk4VE7e-BQ28Plqr0Dlwpi2MHDictaYOXUYGH_mO_osDRK8JWdRWoumpi0MPtHuhYd5YYJIa0tTeC4Njj2tD7vyZa8EwhQ3NwPAaTkCStO5vGsb8VjR29BmGmZVkJ_if58CXDUzitmKWDZuWz5vmh9cARg8wDOO12J2A5JSb55VqPDlsR7-NObDUZ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صحبت‌های جنجالی قالیباف درباره لحظات حساس اولین‌روز جنگ با آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102538" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102537">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
#اختصاصی #فووووووری
❌
بمب پرسپولیس در استانه انفجار، اگه بشه چییی میشه عجببب بمبی بشه تو تاریخ ایران
‼️
‼️
‼️
https://t.me/+W21WaISjE0U4M2Nh</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102537" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102536">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FhRVZ1p3vUA9mSnKobfgjgPwwWy0A-BZ2HeLO5bandlWkyr9dwa66RGFgvz2e9fXFa2A5xvQn74nV2pgMr5gByA6vhB9aloXZwxMg7-jpQ5WbGRp81crj35kaldrCKXCBgUdSBt0XTFAHD79BACmJSRW8FzJbV_UZr0j4x2n3c9kHfhgwMTuCTa4pQSnH31OGr9ng1Yh4F-2U_9S5g1CHppXsaYIONcFsaSwLGXDh5M9PCK6CRcGEvOf4JqyFdI1SuHsJgy7cqHxhxz1K-zEdn71-eRPo8y1c7F9PVjTM4nIoMswAnvOcHkJqw2AtQpr7fk8AHu9cMHYRVNLj7hsKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#اختصاصی
#فووووووری
❌
بمب پرسپولیس در استانه انفجار، اگه بشه چییی میشه عجببب بمبی بشه تو تاریخ ایران
‼️
‼️
‼️
https://t.me/+W21WaISjE0U4M2Nh</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102536" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102535">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f15b1aab08.mp4?token=jXgD_uzKAljLQxdVNlMfnMzQlARduqxP2e0tJYzKOOGFzNeycYkVoljzhArrDBr9J0_50glsWKrUysH_bQ5jJJl7NUyoGMfjdVncPEU7_DBQra759fLbO4wn-kKDX-iAtfxaC5tnpCRYjoczGGqGkKl6gYC_qLr-j3cDPPZGEEj809FUpf1cN9H8Da0rLwU3dzk1bDdZhskoXUtAi8BpSfDv4ChIuSvAk0TG0yz21AmykPhgyftHK5Kqy4ejmWavCjGZHN8WwtplBIgTnk9UUWclB1SEhpXqp-KvVUXi0rY_bY8wiK_D8_CNPflZnIaBybmMYlZw24zUUpPxf_Yr0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f15b1aab08.mp4?token=jXgD_uzKAljLQxdVNlMfnMzQlARduqxP2e0tJYzKOOGFzNeycYkVoljzhArrDBr9J0_50glsWKrUysH_bQ5jJJl7NUyoGMfjdVncPEU7_DBQra759fLbO4wn-kKDX-iAtfxaC5tnpCRYjoczGGqGkKl6gYC_qLr-j3cDPPZGEEj809FUpf1cN9H8Da0rLwU3dzk1bDdZhskoXUtAi8BpSfDv4ChIuSvAk0TG0yz21AmykPhgyftHK5Kqy4ejmWavCjGZHN8WwtplBIgTnk9UUWclB1SEhpXqp-KvVUXi0rY_bY8wiK_D8_CNPflZnIaBybmMYlZw24zUUpPxf_Yr0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاخدااااا از این سوپر پاس کاماوینگا به توپ جمع کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102535" target="_blank">📅 00:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102531">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JknzRKYM4_5KGm2KXs9a-a2LV_dApPxOCOrkSdKK8mw9DzaynicoxDSTO-EaeD_EJYUx5moPOdy5Zx87RZ9SYXcQbovq1sA9g14siNPaoTJl_trB2xMw3PyJr5Lns77eTXst5BqVauaVl4sWeuVYn5Va8Fs6c-Urd5iSM7uF1RppQ4rnV-gU7GIP-gQoiWZ2j_fDxNkfliM8DkYsrLw0tpdWv0HdKFwoR1TzuwbV_TZdIr1Pnk_eRllfIFMnLeZ3h5OfBu4Hw_y2cxDYu7mJPwxVKlR6hWgrxPD2i5uA0cuwgHfzzjCbkh61XWIny1V7z_k6qqebUiqwryxcgAEOcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HH4fCfzuLFS1Dxaok1vh5ogWnRSjxamZUbuNaLdIT0bvgr9OTV6hwl8z9tJK8aPgpILePZNGbfiSE-dvMnWIIdQptnnFD40jk7NQbEpJ0Vmyn7JfZESFs8JsGhABX7IxOx3w6K7NeB9PO_mnsiCn03zwFW1YZ6O7cUV4cNf9F3c9HdWEX5HGc76MGZPU4GZaj1lIeBW0cYBcvzQgEn8gskWYkZIM3B2AftbLe1wx-mqbkU018gyB1p2L1TDjfPVHRREvp809ZrIWF4J4nxgMeRprgy2RTxiQAyIz-PpNszp2M7qQSkUJIGpx_2FeuMdeBaOlAEbZ1Wl3N7r9aQ1CJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iYzDJktUan2Nrwzp4tB9NQ8mT05rUxh1ZdExUzWIhRijwyp7Zp6etjZjmPbT0rtPrUQcLxQYA_DP1AQBEbrbngtfCjUfWRcBj8iNdYqNPmXlmWec5XuQXa0TSXfESfNA8deC4FIQpWKHx7t1YaIq0XJcxt0YACbkweF9Y4kMrVgm2kVB-3zqItkDPGWag4umywRn5my65UyXATlZrAqgG9Zc6RBX8RUvk_cH93qFBlmidsCJb9f_3Fc3-Mb4x5YJkG7s1csTZajPcP2WaOT5g3FNSu2xbF-4hKs1a8Suum-s65qHxmBZYBEqa9ErToWK0i0ZiF7jwMmN4yL-IALgRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nQL8tpikhzUyf3yu1vuyPD_6M85a5LZ-hmoUkVbw1dy-D_DD95WwpYPtotTkXh6lwOdL8cDtRJIVnIDtWjIZQSBsq7rA6xrOJgtCB3u_VljwLqwbQTeAE9MS76VDhSTvYVMplmjooaRuWvhXvp8YQXrtG9bjP5CPIlXjZF9SvGje1WMQVqWMbUkJzFnbhjrOxoe8nSBHeMPFG2BjZ_1cnFYoSlS8wCr4gXxau9Lo08ELtWNYgrrwzxd3E9VhptVOKiXJpBTFbcHVtd40p5_3oecO-r9P5Y5WkFf2gwtoOprGT37NG4zyUgajkGcpOCIjib4W2oS0AA-sG1kfM7cxRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
عشق و حال وینی و بانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102531" target="_blank">📅 00:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102530">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twqWlLkXVmKF1HQFMYrOnd2M8-fpmV9WSGyrIMl6hGwsBLTrn6zG70Djl1EQrcNolES4wCcRvXg2eGr657y1dtBtL3nxVtTOr0tsD5Es95fg2BvsMDrnImOIkHNARe6vD2uLjtk6nvQij2YXZuzawRhLXXf3u07Dc4vsbozYmDT_o1tmmlYpIe3SZRCC51MA1frdZhX7BhBGOgxe8fa6ECoBSzc28x7cPwhUrM6koOO-Y0wedvytFict-PAFR-LjWItuCJtWz-1awPJB8U2jOAtj9vcf843JWQi982sSWLNMrYaNrGw1z-voNym3zt6Y19A8mY0N6zz8mV15s9CfPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
مورینیو بعد از مساوی امروز.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102530" target="_blank">📅 23:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102529">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kox515Y72BUGgFGGtEmFNSzZbDrjvWxSK5rX-YSopoZD5N7Fh5amIHuZ2BjRJVyP-1d_yFQVx6Eh9QNed4JXq7T_ax_kUNB3nz7OjhpxXyhsLkBXSOvXIKGrkR6fS2Gs52MCh0G9UC_KO4soAmzkDGW50VSMPr9uB8T03MQBYHlUgRjIlkMhq8rN5ulvDPQTPmwEoH7ralFi23CdWORQ8nU9aSw-tU7JAYj4oPEYFjJXs8NJ3zOFs0sthtkUfOxb_iS1JghscVbGoeMRLswbcEErsZJfv0l5QHAqRkjcH7P1NPWOUuaSP1xTkm_I5DWAzDeblw4QBKzu-PgENQF_Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
تیمایی که ولبک در اون بازی کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102529" target="_blank">📅 22:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102528">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRVqbnNpHD82jytaMXYvPdEMMyjlnOVqez-NFRFrtKB8REuqGqT8D6_xeAfJfnqaXx3egKW-iVpUBE08_Jb0MvhG6AtPbZ96Z5DKSBA4ohfWfzbsGCBgQ9UeL5b2_Xsg15m9dxWheU-na4FyGCa4lW6gj5CqF_hQLOmlt09KZW6OU7BXB1A73SD8DakWUUOCHnolDco79YxN_Znj2ThJMz0tJRBkEvFhpjWybHzukctKwcP0FlswGoQZRDC0VgHPaxZskxVWyOYFO5qxQkXlBt5vF5-lrgHEAjrx6Jv7tsNpCMzCMCrOiH2mjMJGcwShdcNvPGAG3l7RQ73Qh_dPjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
رئال هم تو بازی دوستانه از فیورنتینا کامبک خورد و بازی مساوی تموم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102528" target="_blank">📅 21:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102527">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRE_f7iurJeg7UcLCDWdQl7HyCsig1KRk13BAUCRiiuXU7mJpdnR-dmJej0olDVOYd3e1WtcUkt3K0DR_vV77uma7jBKwxF9fYp8bINTyPaf-3w2Q7DAOItV0LRuJXeBrJ3qa3qoaGzZTbkQAiGU1LJUHlnYqbn_6BU7NoXaQPSzMLgKB8o9pz_LpWou605CaQEtKRhwaFLtyE4kEY9ggevURgkCWXu1LK6GtrK99RsDEah54TIzLK-1D1C8aQNrJ6tJYZDrSS5bk2ZcW7TKAG79ZqfZMeEPXToWf0Fc7ZI21CqKa-jLS1qXl6KBLGRwzPHBI1IMqDIlRsJ10iMJFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کارلوس اسپی:
🔺
پنجشنبه: بستن قرارداد.
🔺
جمعه: اولین تمرین.
🔺
شنبه: اولین حضور در بازی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102527" target="_blank">📅 21:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102526">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEnPaJgz3m16Vbtf754c1LGe-_CKH2KRjk4YV6Yh5NeSBqt30gkRPkVC2ugjVE1EyfVqNumHcYXRs5-cuqNIDAgw0vK8wl01VcxXNBRked29UAh-7g821rTliAGZlXWD-Pmg3pfAE7gxdcq7LvxNoM1i8_DlfNJAzmftmv7ZgetaGZSG0aM1-6Y7suXwkuVbcf_c9ooI26gMy33jD6Rxy3GfFzDD1RDfT95_FCMaB_eoGDIXD79dfJ1cm6C5YhOqDAMMP_prxIYEDnMpxLPa0PGi11MJKn_mKX-O-nYchJQg8jctIUENMkPBAqNPim-IgZdLduqU0xyhJfNW0UAmrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بازی‌دوستانه|ترکیب آرسنال مقابل ژیرونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102526" target="_blank">📅 20:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102525">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpLdDLned7CzrS_MMladjmqit0-LdwOVRcp0KaHAFWW8qRDsCG0D4Uq6DjNFGmekvc1OtKiMIx7EpQFW0r35JmUkRQPYELwztUec6OBhtYh5rcMDrjHgVy4nNEM2Md-8taupAe7kLeE3bbzC_KbHVDpYUZqE31QeMsliqOPvU1_uNmR-Gr4YJGc-AkPJDO0UUY-gRUKcK6WWYWcLPhqe_r4HjHYdjk7Z8lCxSSzNucj3vYyvith0EmrvWo8O8S-nlXT9tyO6jnMLnBUM3z7tupRNfD77kl59HaPLx2DrRr5I7q3KPOV0GzFJx3Py799fmoiRgMEUS1OPgqDZGHMVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامبد جوان با زنش چیکار میکنه اینجوری شده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102525" target="_blank">📅 20:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102524">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jl1uYlRzxyT4LaYjkNF-c-hYYGHo9f3n4JhvqGFg1KOsvwfg2mYvs0yv26GE0LcxtPIqvO_5wRxXDG6YQxh32rf61vgbBNDI9I8gW3Z5mrrl3Lw-U-Tp0M3LomiQGg4BOqYnhiSWmsDlCYDDz0y1Aeh76Gje9h0wb0UgGGax2w8qvLJ-HnEX_6bbUv-huz-SmoHSuBP8AT4xztaeATtu2VqiKJjWfCCpVzL5452sufIVJve3zC3yi7DUELxqtiKesNjwtCaccyIlsH7Fq8GnU14QlNhiGkKYDMMRzZxGB_SOBqtk3ZEhXizzTAjwHlC8Q8oayL-qrc67UVw4BKE9Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دنی ولبک رسما به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102524" target="_blank">📅 19:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102523">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glkDk1TpHpEH_xI-sRKyRRbYSdVAPGvp5uZhuaUjCA0Ni01uV68MJFhU96aInrStqNoKPKOhhFq0eQK7i2l9sK-yhHg0aUMNSyUs-slpmY4HeTUJrXvyDG1fBcg5tPXmrI6oeZmO2OQZB7haBDMKmDGtkPNXSP_mnusiyfxLVdB_zMc0ZMwAeGRj_j_bawtAAnkXc1u60CDQ25WKO2KsIGimlXNFBRNoPAzQDX6cF4BdC9a7jeJzqk6vvfzVh1fkWy7a5l98Kj9NlTx7nseurKkXooGPjghwKdNZqfKEUWPJwYtAKm3M5GnTDL8CRSq2AuojX481gmm3LNeb0WHCAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بن جاکوبز:
جایگاه اینفانتینو در فیفا بشدت در خطره و احتمالش زیاده که برکنار بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102523" target="_blank">📅 19:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102522">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFzJwqHhULAWRh4mjkvDg-mSh8MZ5CBQVM4ZuC7ZXAqMM4waIbq5heXz4ZCS5_yxzy1tjmqb8Hji9lM9yOVadbYZAltbD84z_7CeV--3EUDQ-jVUsiWGJXfxBVnnYVqtamQro03-r8ZAagzCRSxn2VAo91E1Kp-AedJlOkm5JsjWXtH4FJE1jPZayj5eWUESHEKEpmPQvvq-pDTMy4KI_ojeRtnDSchjZjRly9AU2vvfIWODFWF59xcHFufHFetmj7sg1lvmo7hdc8JUJNuaglaT1lGd0H3p0WWdiSoBbNdvcSMwk6OLt32Ll8HawAbMmmXuGZ1MWPOHiarodDleBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
🔺
انتقال های رئال مادرید به آرسنال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102522" target="_blank">📅 18:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102521">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aK3mt4c64I8ukYlsSRD0ghwoS5vi2dQtRPTmeoA1x1sVuJHDbqezeR0bYsq72FXhMiIYcIqo4wJrzLg70ibny0xXo-QKdOntZHQzTuXKzvOPKecHn9q9WaJHva1DcMQc4VDHwctheG7s1tIKSjsSCuGZxHqJskIcZWi-ys_3__B750lS5k-l-a8z_HjpEScw6h7OByq40zVac8VH8EgMDh9yLiIGIcXCsmZTJUzSvIeGg46r8WWAB-bnGkjzMk9PvzWfW9YHWTKIh1IRzetJSaW-AeboA4no0Q-LeAVrKNxlAV99gUkh5E03CuS8AGpOIP7xrgjyqz2PWXdDFOWAag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب رئال مقابل فیورنتینا در بازی دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102521" target="_blank">📅 18:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102520">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHbGciny2o4HtLespz4FhB8Y5pJIrPAV9O2yhc5IF2YCe9oEobjcNcyiycmtPjAnjC9PQrRoTz8F88rT8EYdYCRpW_nu_0Fk2g9CwFLTOTcWrcz3Z6zYCyi9WqzeQRV0LGEedEZf1R7ikJ45bm9P1PR4_tFEWWlGGltMTGM24lN9vRvf3qjtUXxAKmeGdW_4HDYpCGaU83Vv2eGo5ssP-fZA0FkcdS2nSIB9t5YDzP-7dQP39ga2CzWJtRy3XvRSiyhVbwzFcm5MKMrTQwHt1O3WPIeIw_mYIGpn5dqDxHy3rdoPkAbO600l9fpTywF-I_rBFT081gOrY-Zyin3FfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوکاسل رسما لخت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102520" target="_blank">📅 17:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102519">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDLtTZskk0arUtgRSQDD3Ged5rlHNDTgTowXMFpA_sdJuyhuEY0GYYXScMfnZitTqytHGpp5KHMjdtdKEOZJQFNAVaif4EzJjESvqy4yHGP72tLNQtrQmkXIuo62rF058KoATdrOyxsM429SkQfSwDfGDGyIvp_RzfLgspb3Y9phW9mTBuisehbLhUDMVGMhFC9xEO9JSHmsSxv94kyc3IB7V-hBLEA5P4S9Xc8_DrUnHHkzNAgftil8ta3UiTz4_LGAuizfAnx8BRMII6F3sp0Z9GMODKFrGDGi-yprhalo2c_h-S9h-5yxpeytpZsDi76yQQEvXDaymM-vFMajaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
چلسی پیشنهاد سه باشگاه اروپایی برای جذب ژائو پدرو را رد کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102519" target="_blank">📅 17:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102518">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSTe5GUpPpf36_5jQhP8745vJLVaF57zuojfzGkbXRmgI5YzLacmSCxsiR16b2PW3lLkVLvm6RgxL5s36Tqzk1lqEnRvlUo1eUwidvhMmSnEpanPd4diDL0Rx3Og6OdaJqabekdc2_rU7cb52qIUaT1ZeYHOXuC8aD0oB5NGoMvxusU8ofM-iIstOq6Hibxbi7WblZv810pSaCYGIMiVzmDf3-kIIoK1C0j4d0K2B37EM2BTZ233VmewSsXLIZQYswrENwwbDAdPh6ILJ5wiA3YRz5uUFatoI-qlEa4m6QIO08HPyN5dAJaIYjwh9ox1Yxg5XHR0OmTn-NxxIbx8XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس طاقچه بالا میزاره و ممکنه بره آرسنال؟!
من یک ایده دارم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102518" target="_blank">📅 17:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102517">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb462e454.mp4?token=Jx5uPb2Nyl_48mk66BoRJeD7YsjMeNd3W9kDJp4_4glTi7Xzh9yPVrkr6MwF2oqgs_EBThO4KlrRQULCu-Y1oXPScnqpoJlNQll4dA7jSbt3L3Tunalef1Oo4cbmy3YL7GWCCTJC9H0dPznSMV7s-ukKlD3LfTEs6HF9Ay2tIH_7BmAqW7GB3GlenEmH9AgNrqcI0NTo_RRE4MB5LhwAylLslLu73UihjIQLZKM-XKPDRkR2bEXlXgdPEbp4sx0bVm3IB8sWXcg6_58YTU5TcXJio_qVQ-TTx5-pPCxHlnJXr-c1edIETTxivVprrIBsEkUPJavqVjJNeezOKO7VgyjT91wW6SSiC9v2PfrKyo7t2ywUe29hWjEfUCchfHhRkSna2gQhdLKZacEZOPu-qICnV_8ziebjPW89r6zzKJMXDm3BLqXW7f5sJ-O9Dp37dKrnJZNxUoSTzo2H1ZZsf_wryuitA8kQcP1e2Dt90C5eP1NAdXecDipDzZ2Nab-b4_lPU4Ic9gTVSwrA_mt0WnEnjCrUhwVklFUGMaVIIVZLfvSLazbtiO8fpRIQc_MXT91ZMs3KJZp_3BVWVyYlXjUBy0W8gliKhaBCGcTXSxCHyHPNSA6T1SUlpAlSwPHmKwz02eXL1bF5V38CfaRf8Q1jaDlsIB6B6McIcM7JmDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb462e454.mp4?token=Jx5uPb2Nyl_48mk66BoRJeD7YsjMeNd3W9kDJp4_4glTi7Xzh9yPVrkr6MwF2oqgs_EBThO4KlrRQULCu-Y1oXPScnqpoJlNQll4dA7jSbt3L3Tunalef1Oo4cbmy3YL7GWCCTJC9H0dPznSMV7s-ukKlD3LfTEs6HF9Ay2tIH_7BmAqW7GB3GlenEmH9AgNrqcI0NTo_RRE4MB5LhwAylLslLu73UihjIQLZKM-XKPDRkR2bEXlXgdPEbp4sx0bVm3IB8sWXcg6_58YTU5TcXJio_qVQ-TTx5-pPCxHlnJXr-c1edIETTxivVprrIBsEkUPJavqVjJNeezOKO7VgyjT91wW6SSiC9v2PfrKyo7t2ywUe29hWjEfUCchfHhRkSna2gQhdLKZacEZOPu-qICnV_8ziebjPW89r6zzKJMXDm3BLqXW7f5sJ-O9Dp37dKrnJZNxUoSTzo2H1ZZsf_wryuitA8kQcP1e2Dt90C5eP1NAdXecDipDzZ2Nab-b4_lPU4Ic9gTVSwrA_mt0WnEnjCrUhwVklFUGMaVIIVZLfvSLazbtiO8fpRIQc_MXT91ZMs3KJZp_3BVWVyYlXjUBy0W8gliKhaBCGcTXSxCHyHPNSA6T1SUlpAlSwPHmKwz02eXL1bF5V38CfaRf8Q1jaDlsIB6B6McIcM7JmDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه چرخ تو اکسپلور میزنی میبینی پر شده از کلیپای عروسی ورژن ایرانی رونالدو و جورجینا
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102517" target="_blank">📅 17:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102513">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S9mPog6CqJWD24_nDW0t33EgqaNDkRe-MvIEKqSIqiOc0IFz8L1Z9zG1tLSwds4igbXmL33RpwsBm-d6iaR3J5id3QbsBmBeHartAqaZX5s_MlX0brRsCPadrmmPTW0CK5R7s4wfKDZqcFv3rV3jiifiTTE0Pjtau7SlgyX28w83iTRVW8OP5I54aHHPmHC7ghlHBCA9TBuHQDL5ezlUnfxCm411HBTvpKYl_QTPtbVtXwzH8Xgeq-bJV_ZoOkrARc9LhB4fyomXuvso7JxN2jUi5dFS7JTvgxWlMTk397Vc_GhyKba0TAWWqTian2by4uXew5LQpS3OfloyUFaI9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/et96n4ctRLLvGR_7CTPF97BW5lp2ZDUzRG-KaQANdhDWICDuvSrQJdW5bIE--bBD4wsU4iPKlkhtnT_155WvQXd-RQESbam2hvs2tAAfA00H4Cv1NDbAoT6U9HnMbyAK0aQkx7PYszDQSBu_K_ayFG1WVqhL5q-Wt9AV3gueQyHcGltHjeFAJTCvCLG_BPpjO-NBNktrlHQmDgUw6rpec3BlyHxvNQwEG3vqj7Mc06bNsQPREQLCUUOo88q64VylLKNooMBSULqxdkrF6UEEIVzsw0hb3tZn7aCqH117gAjx0abtWb24MibNYGjk_RKgW96DX5eRKFgY7ZDsK4XmOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z2zxW45bJ-6YE8gVkIj46lJZSheQOEY0WA3VtNyw2fDfTtrnI0QIEHZwTcDcndeLIVBLzcg8jL3ZdyDvgMjjZmEBXSyGgmku0_X2boZlqdIn0BPjdZI0i__Su42zsbb6IM-bjD0s_nWpxJHRCZ2ezEYfUJIjgVBPLn9ZsSz7lntTZNv-HtUljoT3YXouU5yEBzAzuYpPVDuV3dlVK46avhvMHOY_GwSBOgkcwtI476nqwbINrTB1CrOxvyqnV_syBjbTg9UhH0f09G56D3lA5BLxoi0wJKLnBsYwTbimDzt_gN8R-PkWEiYYyo_VJOLsYnWqWbZK-OiUXX-Jfw44Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l61Lkd8Uz-GcPmg-QHGLj23gRPH0XPKsYSTpMCe5_JK3nnMDswdc-3eRYccL_ibp2IQwkKIp0h5XbW1a1MN2jUH5vDm8OhHPPgJzYcVVLGka2MmDEYXeXLuq1RsDlOfPLxK8wPrfz6ob5BEq9g4DFyy1LFvQENqktkzyih8a78G5hEUI-4GTQ5wE7wyhJQUOdAwRpzMbULwO-ciW18rNy-UMGmCaQm_sfOjdAgVlRWN4uVOWfo8m3gd0AwHigP7QM1xC4J5i4ialRb71d9GXxWB6Kd2oGOLSYSbwyHxwukEDg_vca4odq5a1M_YjvcH4eEa9GMDa0Ornn6s5gotQDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پستای جدید جورجی جون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102513" target="_blank">📅 17:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102512">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LF0ozzzbzSoPRX8D-DFhceHe4U158gTJNqe1q0gEP8nimrbzEua6XoFu7kC1uBf-_5cjsyYwXrHJH5b9y7pZR2ZgaEdBRzwTNZaa8zWEDz1hOOxT0LVjfPQZgH4Xyc1mucCkI0TIuL3eugFV9lBOWvT43nuQKmBBsdXhhCUCexmEqhSxCVCd1VpOfcbCza6OlEMBNBRUN6_uAclh1IpHV7NBwa9IcshcNsliLBWTmWZdZWQHLpmoF-dsc-H6wpEiTq7OssVi9rCitF3AJvs6XTr9wtsZKrT0QdZ3HhJqcyi1PBjtMYuV8DDEZPQlGmtxgk_nDyHice2sEaH17BAijg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔵
اینتر با نتیجه [3-1] در ضربات پنالتی مقابل منچسترسیتی پیروز شد. بازیکنای منچسترسیتی سه پنالتی رو خراب کردن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102512" target="_blank">📅 17:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102511">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f1ded84b.mp4?token=vKrMMnb0bUQgs82qoy-dIzJU35G2R4gW1OSGZXfCKgbD8uJhZDVmTXWXLOpaHD_YnIXKDHSN5mRz_qpZe8w3I9Ed0UC3vx-fzQhIPNbdefh8jSYKRFAS91rIPDWyM8V2PPNxipxNhf1HylcXdgAbMqEqg_oXtRYelVYGgL497yGmVQJDqM59fMOQq5OltA6J4QfAWiM0SPCdnU1jgPq7pGT-cX1M0sJMD7pN1Gp3AKC2e7iNP_j9RCtIeWRmC4j8uM3p5ZoA3m35rOTbYBa8LOZ1PnXIkErffK_l7gvARV3yHK9lCx5jX19hw6mw0lhiXNAxz2vqz-IbPuLuXTZFEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f1ded84b.mp4?token=vKrMMnb0bUQgs82qoy-dIzJU35G2R4gW1OSGZXfCKgbD8uJhZDVmTXWXLOpaHD_YnIXKDHSN5mRz_qpZe8w3I9Ed0UC3vx-fzQhIPNbdefh8jSYKRFAS91rIPDWyM8V2PPNxipxNhf1HylcXdgAbMqEqg_oXtRYelVYGgL497yGmVQJDqM59fMOQq5OltA6J4QfAWiM0SPCdnU1jgPq7pGT-cX1M0sJMD7pN1Gp3AKC2e7iNP_j9RCtIeWRmC4j8uM3p5ZoA3m35rOTbYBa8LOZ1PnXIkErffK_l7gvARV3yHK9lCx5jX19hw6mw0lhiXNAxz2vqz-IbPuLuXTZFEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
اگر پاس گل پوشکاش داشت، اوزیل بیشترین رو توی افتخارات‌ش میداشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102511" target="_blank">📅 17:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102510">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GK8fXXuEYGP_r2-UEq176jm0BFwcZ8ygKyjH3YK07C4UdzdXXZYsaNCK8_AvPJmOP8d1BRRRJTpcnl2DqqDcasD4z4_bs3yy1vlHu9D-9_e9ltwYxuCwJBhWbxVRXOyCr48sM_pfr4NyzC1R3C5oIanTcbuV4TWHbFddGPOY45DY_L-D39AgyYpuRam43CHW-HDbEutFkxMq1eY7M5yhRmiCEmFzHxhwEQ2oMoCv5Nc3YJn3oa6Cv2guthKF0-6sntIxShL4q7A9847JtVyb7nGOocEgp5V2NrQFArmaWMAvb2oT_bgKwclN7dpL2OlOUHX8SK7XClsnI0-EhbJAww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اورنشتین | اگر وینیسیوس با رئال مادرید به توافق نرسه حاضره همین فصل به آرسنال بره.
ماریو کورتگانا: آرسنال ماه‌هاست که برای جذب وینیسیوس به طور مخفیانه حرکت می‌کند. آندریا برتا، مدیر ورزشی، با اطرافیان وینیسیوس گفتگوهایی داشته است. چهره‌های کلیدی آرسنال نیز به نمایندگان او اعلام کرده‌اند که او مهره کلیدی یک پروژه مستحکم خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102510" target="_blank">📅 16:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102509">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzcNNldFcRO37RtUz2tcIwp3nSSb9hLmeez-FoGIMHSEkWnDSm00A6LTb9kWagrmPvN8VHRUataONxhwZF2RXETRRQgyzBtNJ7Fs6Lz0ON9EIbReQfID1w3c84_Ix3vcxiecx0DW7N1s0OXE_auB1icgfP314sxuRgwpLikKNbmPd0gfyb4g4jUlFjDiS17fkUJtchKZSNKZoZawFX3dqZAycmIVqXmR-6Ucx5US4WaRoqSCCeM6RUokzWiBkOaXP2FJOLgBZzQ3mmv2f6r2Y4HmTLg_HoZfbOqG-ErmJG7BwWF-UAKXrORN96qi2jRTreEc0PGsBKutmNpFJZa-XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رودرا - ESPN:
طبق اطلاعاتی که به من رسیده، انتقال یان دیومانده به رئال مادرید با مبلغ ۱۲۲ میلیون یورو + ۱۰ میلیون یورو بند پاداش نهایی خواهد شد. همچنین انتقال رودری حدود ۶۵ میلیون یورو هزینه خواهد داشت و باشگاه در حال حاضر منتظر نهایی شدن انتقال بوعدی است.
⚽️
@Futball180TV
‌</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102509" target="_blank">📅 16:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102508">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDK3XyaCOYOh_Nki8LUYkP-O_Tsa1meXZRuVmd-3dGDNztCiJrpJ1zDBGnauhPFySh1eey4UZKOEcyZqRLZXTL2nQ0fXQGDPxlG-86z3VXjzByz9zT6_TSNwlhQ0QBU-IzRACZ6eYA8xRNeDVVZ-Xclse_8mp-_gDO70FE6bu6pcDqimSMcFqlmuJvdrOHbPUrtRrIdWHT0HPv4sa6E35nAgGS7F8yJ7aTAfA7o1VaP3q_WlgjCmaKfgyBWGlYZHmPO2qLGSEXYxOCf5O1aBCzoVlOOpfLC-52cbrFqwMuXPwgDnbVdoN0wg67emi950zvK7q9tQhQhnWj9O02GpxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین شات از عشقتون وینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102508" target="_blank">📅 16:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102507">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qC3NNI4nfvTJ3ScMGpePfWP_Slvtaj-3lwdfl-llb7agLlRBLfvh9q1xxhrTwcnpHT8ERkwqhEptynD598-_KzveJUjw0dRwLWPB36ROzQHr1KwSJZXZLtI-hbAi5cBLOdHbf2DLhFI23bhzDOu0U7iyybMiHgjRbtwtnlzt1BKy5LtNDGOzFBTcLvwkwemssK54ydRsz3ijCgjsm4Ca-OAklRSo9zfMGtO7VshmSeVUyhhdoTMZ66Mjm13S4VW5iOeRe-FF0ENWLhs6S8AMyxiJ08aijYarJz2_7Z1AX6xqf0AdUcHhfomRnZxNcpgs2z5TX2FGlkGg3ceQAHvNpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚪️
چلسی در یک دیدار تماشایی موفق شد به تاتنهام 10 نفره 2-1 ببازه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102507" target="_blank">📅 15:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102506">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WO9vUjGapsWCIWXRupkCvy5Rt35EAvfvxudd6BAZGz60IRsT7vqwTwW8Gpe4pnzlyfjkrcU1flB_wRLH3hpg5axaj0BklTZwj6KzWyQVKFLOkQvfmafGke4oyCe318rgKa3Ji70aM8SYnsRfyEosvJq4pzFipL6GpGB-RAATR74zgbe6W-avZzB7zAemf7wdIgNwmAuPULlNFZ67QEEdyGfT2f5niFd1Z9B6OPJ_GliooaUAYu2532BB7-GsIeH7RqCzMQ0ZvlyXMWJAlqT6Gm8estDgglMpPLcj3Q8V19XD2sbNIlBz5eqbv1eXMoN4GYijzF5NfuC3cLKHm2zevQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
تام هالند:
بدترین تصمیم عمرم که خیلی ازش پشیمون هستم اینه که طرفدار تاتنهام شدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102506" target="_blank">📅 15:07 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102504">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a1fTku8wXouns6Mo_HDXaJEzmQaxqI_1vWgkHxiITZRzBISgpPmErvuYolpHQlAJCaZvY18XE8btor6ZtH2ZjoB1NQOJAYy01m73cxXnO6qZmiiQGtWQi-CKtByFUKS60mARMXdJVog6Xjh5haUcBa8_oOL2Uu26rklt2AnL3rUYrhTQT1o6OtNHLHZMyyu3ZGvxt1Jj7zM1g1bIzq9rdZfqFEk0XRORq3fqLAvrYqSISJE3fIy-l73rZjUXnhpQQv5_tFU_WBHbwewvwloTsGh2oSYaNlxliFW2G-cCfESsSbUZEfYQP_cZ20918UAPey1VGDv97kzU9QdDPFloag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c8hRvbnrxQ6JicqOV-REYPrUXFHeTGCbT6aOGmaFD5abVYlSqRZreCk981cRB6GRBcg3EXrhGgMJzoBhiJAbaU-uIO7sMM-tFQNlVOKM9gDb1u5HZC3sKd3C2IrEwwxK_EWSluI2vf0JytYTJfkh02SQpKelu_mFiXcs8lDg3QQ9EKTsNrVkKlb-uz7Otvu1e18Arj-SEYfzB1c3TulZPtk1XaaB_Ha7qESiipxTnnRx6PeCSX3t0PebIrjIv_yDOzP68IeP_C1vyUvypl9xqaIk9kiq_kSoh7krSHKt5rADd3mBbksFCVYLiW5zpsK5gfMD68Cdbh5P3CAJAC8Wkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
یه پستچی رفته بسته‌ کوکوریارو تحویل بده که کوکوریا نه تنها باهاش عکس گرفته بلکه بدین شکل یه عکس هم با مدال جام جهانی ازش گرفته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102504" target="_blank">📅 14:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102502">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rySRZayF4adT-0-oh0JNzBjdI-FfAX0BlTBHthvJp9cQ-gFIqmwEKXX9hgkBKRMmZB4HIPTKGFBx_Li_95ZGmEaFg1u-EfuhpLnjDWq3LubQDz-KSyfKFnwa4Z_EiVs1FhbwT7m9IE6nKit8MkEIwpSM9QYzY5O-s2DJXD-x6vW2yTbfNmd2y5aGQ8JnmiLBO7_hCKZCorkIhXBnHddkhteMmB2lxvg5o0V8MJFE_OripxdOY6eNmAVqPxibxuanS1oTt-taDukTl7LvyQ1lRUdie_Y-EI6R7V12LGLJNtU4RArqb2YUFAlbJI3d2B8Q5_BoPDanFrzdSESHK6ol_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Du80yLNkx_Q7p_wgn-PwHpOhnBWTopFUGhaKxi59HValggMwMhz1eIu5cEcm5Jjr9ziGAjx_hUemx1_mpphuRMxtpbZ02bMdJKaQIcUC7Rr_xnNvDqu43f3UJC7lxfuNzIrBQaN6yaqPTTDW_AJ0rRiNfjvfFFvmaUHstColpHQFz6FXjmK1vAz9_St8DsC7eXEE8nRbtuJGyTU1H7lXXL20z_sruyifNWcQ5rBUH2x6fsPqlihW_dwUWXuKSf9VxTdzrhzuYWRIs_hY2ZYtfOAFfkBC7SzUJahtX0gAOrRsE99og_DuSI46v9f7N-jHBXHU-Vf0I1f_EwSIDnuINA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
⚪️
نقل و انتقالات بارسا و رئال تا به اینجا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102502" target="_blank">📅 13:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102501">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaXnKbdocshkc-On-fxFtgWsEX0lgOCgcDWVukQjoUhwoy80Kf8xq9jzO7uJNNp4Q2CtftxRP4ZnTZXA6hOZaEi5Q1aFnonxOPLGUBhSoSDbwIqI4T8vAwXqzi0KrnqVoY33cPQICiJEEcuJ1Wf-cIC0OTswrIJSPul2nvjJfEC5BqcrjGySmoYKCD-0SgXBscMJojNZOKoNfFjWWqUgZqnDNM1RAz9C8UZ3WdntT11GJoYuA0_9CFlDziyiBiuLknYOKqQmNpzANgulAiqD7W0TOdxOVOt-MaGv5roo4_S6vDYshbUjELFvvUF7bAEMD17qtytw2q7Fkbt_bm1jwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رامون آلوارز:
اطرافیان وینی هرگونه توافق بین این بازیکن و آرسنال رو تکذیب کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102501" target="_blank">📅 13:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102500">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sf8w7pDq2_8_iBSSw5wv16uoA9yT5S6kXwFj3SzB9CIKis46zEBUWTe0Rjd2EM2lGWbuNV1RKl50NYMWH11UtJtshaLIZ719Wvtm6Rfi6C_y0Tf0eSu6qntsHQtS-2gpHVTLRFEremGlfyxKKTk7SUaHgNdQSaMH5AtOXR5GurqiezDJPR3RewaCCIZ_5YIxYlZTY4nvs90m_6-UIIRAXHpPeS1VbnhiDk7VzS5gcwFdoV3sRAol70mTciHq9nhsadnENZeFxGptaY6lZW9k8RqxTIP7c874gwhif5ZxbxRgQvahv_d_fq6BT8U0h8-cG08pChTizNuQUzwg7avobg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
• کریستیانو رونالدو به یک ویدیوی کوتاه در اینستاگرام که او را به عنوان مشهورترین ورزشکار تاریخ معرفی می‌کند، پاسخ داد:
"خیلی ساده."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102500" target="_blank">📅 12:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102499">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29d00a9ff8.mp4?token=kRDFI1XbrD7ZKKY10-StZrkgwlGRuAjkL1NBf6UoiInEP-KqCNIrGy0ywIQxr9lTzBkpEeU_H2D4XDEsE4CuXlIhqX8-_tG4LM1y9XIGbero581uxrlIm--2R4Mx_RalrTIrys0QyxPF9cUA0ypvCCU9HwMBS9ULqLsd3h9i7iv84_U8uTec4RY_v8xTEADe2-WLbeBj_CB5V8zedf6TqL0PuwtSUiww1RIl6nziOlW8lXBAHNebIoqiS76DSOx6XTZTOafOYYRmXkLP0KH3D_FmYssM_xiBdd-a_gau7AMTNqoxFY_lvK-h-7hjzVMAl1jCxgM4TOeEGGb4eLBJrKcVL8FE_xUB4LwoUXfczFauze_qw6dUeYg7Qzep4gTdaC4uIRp8P7PDDInC2uGH0tXuj9sw5QV15NTsfQKwkxjvcMm0g-AvUd3nLm8ApnJ13nU3OAF0NO4ioo6yzBCZhiBHwSlzelQjcG3rkWQmWWA_5cHPpPra6nz_rdF1DnlsbUbCxbywltfTA7iBLDwiLcdPpz8kS3ExA37eM6I8jPvENs8Ku5QalzzoHZ0m0EER202r_SkDAR1LzSJW8QANdBGcznRR3ToA7jQCm8MQ4rbjLzA1LUgpVmtGnzJ2XtRGYBrqkQHBFP5mfTRBUCQAEEHeXd03s1EdIKbGIYcSxPI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29d00a9ff8.mp4?token=kRDFI1XbrD7ZKKY10-StZrkgwlGRuAjkL1NBf6UoiInEP-KqCNIrGy0ywIQxr9lTzBkpEeU_H2D4XDEsE4CuXlIhqX8-_tG4LM1y9XIGbero581uxrlIm--2R4Mx_RalrTIrys0QyxPF9cUA0ypvCCU9HwMBS9ULqLsd3h9i7iv84_U8uTec4RY_v8xTEADe2-WLbeBj_CB5V8zedf6TqL0PuwtSUiww1RIl6nziOlW8lXBAHNebIoqiS76DSOx6XTZTOafOYYRmXkLP0KH3D_FmYssM_xiBdd-a_gau7AMTNqoxFY_lvK-h-7hjzVMAl1jCxgM4TOeEGGb4eLBJrKcVL8FE_xUB4LwoUXfczFauze_qw6dUeYg7Qzep4gTdaC4uIRp8P7PDDInC2uGH0tXuj9sw5QV15NTsfQKwkxjvcMm0g-AvUd3nLm8ApnJ13nU3OAF0NO4ioo6yzBCZhiBHwSlzelQjcG3rkWQmWWA_5cHPpPra6nz_rdF1DnlsbUbCxbywltfTA7iBLDwiLcdPpz8kS3ExA37eM6I8jPvENs8Ku5QalzzoHZ0m0EER202r_SkDAR1LzSJW8QANdBGcznRR3ToA7jQCm8MQ4rbjLzA1LUgpVmtGnzJ2XtRGYBrqkQHBFP5mfTRBUCQAEEHeXd03s1EdIKbGIYcSxPI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
ویدیو جالب و وایرال شده از رقص امین‌حیایی بازیگر محبوب سینمای مملکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102499" target="_blank">📅 11:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102498">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86343d5e54.mp4?token=XdwSfD6dNBMR2_OxBaDXyzAcNumdMAIsJPQ6LJmlqzslHWUSt6gK_fPCjZQ-PUNKg2NirMCcjyXvKucbcuXVhvwaNbjNda-uW-lc4o-aD_si8vtO1Ri23ahk8rRzVo5kXXu0OpMfgzNRkIH9LCks4UzhzXDJ2qCUb4hOqRYGEib_m9gfgViDX_t30cDFj1AQzI6I7n9Hv0mX7fkQCLKo3eTkYK2dBt9rrJGrXD5TYyAMD2mIKQOMRbz7K0_rfrGhjdkZUNjd3llAKWvkNC37W7VuP_fhl39Bo9WypeM8fkC0UOfPKusehcL-IGLYqL1hL02GZbSmK8E7Jt5z8kEysRVmFT_E6XL1YZHi3znjOvpAaGqR1qNjOKkjrtmUNIb7InRGmkXWvQVIatwqRE_lH_wEBuTCLGLO8u9TdTBBW49k74PryfJBNeGcOJxmXZhXZkd18lN7DmQaqL6u6pT2R3nZFyfRmUQ_pQZ0e4nZPMLWuh5vruPikwt4ExiLUfotNE85iwDLKUGu_DLExAZHubpFILbK43RSh-9R6GJnEmbKzHJ8rcOM_eZ-RYZbLcnniRJoPqmDuYiCc8Hz6tSzMHo5qMTVXrrUdipa0vI3bas7Dq7HCWZFgUEBp4Z5Jd0Vlbv6WQMmYKFWETMXASPVXt7DLwujtMR2BiPOszW6Jmo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86343d5e54.mp4?token=XdwSfD6dNBMR2_OxBaDXyzAcNumdMAIsJPQ6LJmlqzslHWUSt6gK_fPCjZQ-PUNKg2NirMCcjyXvKucbcuXVhvwaNbjNda-uW-lc4o-aD_si8vtO1Ri23ahk8rRzVo5kXXu0OpMfgzNRkIH9LCks4UzhzXDJ2qCUb4hOqRYGEib_m9gfgViDX_t30cDFj1AQzI6I7n9Hv0mX7fkQCLKo3eTkYK2dBt9rrJGrXD5TYyAMD2mIKQOMRbz7K0_rfrGhjdkZUNjd3llAKWvkNC37W7VuP_fhl39Bo9WypeM8fkC0UOfPKusehcL-IGLYqL1hL02GZbSmK8E7Jt5z8kEysRVmFT_E6XL1YZHi3znjOvpAaGqR1qNjOKkjrtmUNIb7InRGmkXWvQVIatwqRE_lH_wEBuTCLGLO8u9TdTBBW49k74PryfJBNeGcOJxmXZhXZkd18lN7DmQaqL6u6pT2R3nZFyfRmUQ_pQZ0e4nZPMLWuh5vruPikwt4ExiLUfotNE85iwDLKUGu_DLExAZHubpFILbK43RSh-9R6GJnEmbKzHJ8rcOM_eZ-RYZbLcnniRJoPqmDuYiCc8Hz6tSzMHo5qMTVXrrUdipa0vI3bas7Dq7HCWZFgUEBp4Z5Jd0Vlbv6WQMmYKFWETMXASPVXt7DLwujtMR2BiPOszW6Jmo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
پنج گل برتر فصل‌گذشته لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102498" target="_blank">📅 11:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102497">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qndSKeYsu6bF70fWISQ7EEXvKvn9ii0TZSXVXCMpH55RqIUPWR0qCg9De3ulxGQc9GiUbW3nXitMAXl9o7qkiBKaJspQL6AS2VHM39KOUFmqUJO2EJU4XCBptqe5LLlATpZQqjCOHUcJfOFRricBGbuvtnX_oCi9b6UbLlNf4EYnfGahssa2flsq_nyBVQNl3PGo_dOD47OIOB_jsBRQyjY2yXyJKAzfIluJoF-IDNd682_fpTkBPkNIlncAAZ74UVSvYvOKNju4WIxHCBEdAahateki4_AFYUMWJBoLsfuyJAVxXeo7xJUXqD-Bhy0GdhfU199un5rtYIAgrdEh5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
اینفانتینو با انتشار بیانیه‌ای اعلام کرد که طرح فروش بخشی از سود جام جهانی به شرکت‌های سرمایه‌گذاری خصوصی، به طور کامل لغو شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102497" target="_blank">📅 11:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102496">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e324940235.mp4?token=DkI2uUeAGDgNbkpive_C4yUV8qdWJIglS6AGH5GDsCxtsDA2T0R69FQ2S0QzAHR8yQ1AWFSTLMQPNxXUxziRtVIgBrvxuuNmRgnu4KNSUDQ6r3wvaaUyN9O2K9-uVSwqOb2czaRDBIl2QaVZpK4ME9P3LcgDtPoQ9En9Txkpg0Hel2wuVcrJ-6trnhUq1EvTQARQLb0_9O6VUQYucaHvfrdcOaUCYlqAxgGB5nkoiHR71RTZoEY2ivsRFHjMGMhXJaY2C7chyS55kmIbjCJfxHaKJxMgspslDInaeBQy0klTF4qvTMLjlE6UzTdfiyd6ZJMMNdcMp74048j6MpQAkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e324940235.mp4?token=DkI2uUeAGDgNbkpive_C4yUV8qdWJIglS6AGH5GDsCxtsDA2T0R69FQ2S0QzAHR8yQ1AWFSTLMQPNxXUxziRtVIgBrvxuuNmRgnu4KNSUDQ6r3wvaaUyN9O2K9-uVSwqOb2czaRDBIl2QaVZpK4ME9P3LcgDtPoQ9En9Txkpg0Hel2wuVcrJ-6trnhUq1EvTQARQLb0_9O6VUQYucaHvfrdcOaUCYlqAxgGB5nkoiHR71RTZoEY2ivsRFHjMGMhXJaY2C7chyS55kmIbjCJfxHaKJxMgspslDInaeBQy0klTF4qvTMLjlE6UzTdfiyd6ZJMMNdcMp74048j6MpQAkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
و بالاخره تحقق رویای دوران فوتبالی کاسمیرو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102496" target="_blank">📅 11:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102495">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👀
🔥
هشت سوپرپاس‌گل ثبت‌شده فصول اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102495" target="_blank">📅 10:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102494">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSxtz1qeNJoNqK3Z9zP9fiU-0oQqPeM2DztBPLNWtaNCcBqGxDM_VcDlpXs9_S1efTiK9IUuc7FgO3HoEdXZc4lKwe4dc6OVE4LkotKdUY9Quo64sNqBd7k8wTD5yf7aNuzygf_Dijj267l-TARSR3xoLwwkSCGebHSIgWHKgf12IT3mycY0TLwK-PqowQi05KWVnoJmZozHP1NWVG9T2iiZKMHWbrJTKZE0YWp_ca8cUHMyh3sj-Z-i0XKAtmAecAeK2EKgj4h9OKsDnfYHGBXUKGN0ZQd41Fk7aKZyziiHr2BIHNNY_5kqk2lrbXD5dKo11N7cF98b-ZuiB9Tt6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه آمار مسی و هالند زیر نظر پپ‌گواردیولا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102494" target="_blank">📅 10:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102493">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bv4GrqDx529r2Ct-w5NGjpl6KaEo44jyDKgkLPLeNYM9IYtOUba-hVCEcTTCV7jdxMZ5dxHhFg-uzWZFd4RqZ5RCYlidXIIMkthp2FwP4xPBvkNGwwun4EBwyBHKxNpzgLNdXhzYAS5PnNSXIL6rdNNCQuQzIiit3XkheNWLAl-tZiOmBBsGRcI57Q7fZy7IOz5oEmS-QPjc2jcOdbN0zd6yQ3jqHeHQ5MIHphkpVwoTJ9XdUTcauLv0xtpEZSbMVsYBnF-CyGNawxdr2fYVR53mzuZj7T3KhxcCTl2-18ER45tP4gSiuZs7Lz0JlB_kjxAqhaUW_gej4RCOSdFepQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمام قهرمانان ادوار مختلف پریمیرلیگ ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102493" target="_blank">📅 10:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102492">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1s8sAJIsersJ1yLARKRSWZ_XHOLKLJ8mtNE8CICLK5ffBbeyfAR-sAIZgeQ4uDS9GwA3odz0Ax_HsEb1l3FJ41DX_4WhMod2l7WZqBHv-JgL8g7IAlD7q3GYMpPEY6wCZDCem-0goPdMFIAUkbIqF2f-pd2dp5VVpMR2O10j-YBQyjiHruhAkub5KA7Hg3CPK3cdW--nLqW0KWTXpZwBCr1qCIKgRVYY6CKfff1S9iw3-xGVdc6ywxtI8epV3CEpTRtZb12AY1Kf2kFMAZTymOHEDirIJxQlSw4DxFvmt3ZY52rXCuGkwcvSmQmVL-JzILepArOEzBt-JoEio3jmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
باورنکردنی است که برخی از زنان چه توانایی‌هایی دارند!
💪
ژوستین وانهائورمات، هافبک بلژیکی تیم زنان کریستال پالاس، در سه‌ماهه سوم بارداری خود همچنان در حال تمرین کردن است
❤️
او ۷ ماهه باردار است و همچنان با تمام توان به تلاش و فعالیت ادامه می‌دهد
👏
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102492" target="_blank">📅 09:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102491">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnaZecuy1ETUkbZqPKy_3eJqeZzlrhOnox0D2cSz1AmHCZOf156F2lyi3fD63E1gHVZGwlEr9XXUTQCBxlx_a5UNr-XxEhNNovxRTBUzwVj2Ey6R5NihTQbj2fiQsrtUk1Mo4hgrrPO7BxTCcIGvIqc98Vz-jCbTh-IS0FloEA2o-QDBsnzmr7dJTHbdLpw6Z5DOpVZqczyUhRj0BWW1iwO27bK_c2Zpx1cmv9OE9N3keSkIesbPFVeuBcruZsLnIDMahDm6-SnkdOujyLxxKTm7Ryj5XLuJ1dHG5lmeNPjNRtKKIoKcG3wxRCYQ_ChT74A4tkBR7eLNBZfxXtlJEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🇫🇷
فوریییییی از فابریزیو رومانو: پاریس بازم وینگر خرید! مگنس آکلیوش، وینگر راست ۲۴ ساله موناکو به پاریسن ژرمن پیوست. مبلغ انتقال ۵۰ میلیون‌یورو و تا سال ۲۰۳۱؛
هیر وی گو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102491" target="_blank">📅 09:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102490">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b17b2ecad4.mp4?token=OrmQ6H3JssX6D3ShGV4awqhxY6M94V8QAA7vuSV1hn0quL5geJ-lDspcWsBLHpxJZl8AJFpJHx-kuNjadUoH5hw1IDvKU9VUAVkeqsCUfysrqkGxx0ug1P5KuNIu1sv0OmKTlIa6GT-55hmIA5zcYGGAUoTGL1CTQSOiRN5kHYRCJXFpXTVxAVlgxdtIE1He07Izecx-CJf6ObzAWkmThLM2Y29FJ6_CueRdBxmP7ndBZGfplVnEZFDQ19x3WytqbThvksnhd0t5l1wFYxdq8OBYcDvHeU332j32hig9jdk88Q_EZYRHaF0aNDGlBX125H8UTR2Dw4Uf7ceNz85Xp0nPvggtyRIaZ0_nTf9dTFGOycXXTF7t6qXPkMNaIjM3dwS5rzsc7vPctQcf0_9C5N9KqKAJnqUtwwjVRIBZQAxGn3yOWMFSCtz1gQIIcP4NKqCozvsCtbLNY2ISbAYOkzdaOXLCJ7cvlCkhTjvcP6R5gb1yPR8P825I7XuOy8MUCTxCKMwwj8dCyU6i3P8iHUOqNv5npbl1aeSeXwpZKsxp1WBtBKCQtFE5r_NdGfvIW5UNeP64WHlXYGW3DvCGfbw6wzNfhUW-1KgHYTqAhYwzs2uQLIOz6zjCpF1czpzxO1My4860JNx6MYOjG3F347jG3cRGnqiDEpTUM3J3Zbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b17b2ecad4.mp4?token=OrmQ6H3JssX6D3ShGV4awqhxY6M94V8QAA7vuSV1hn0quL5geJ-lDspcWsBLHpxJZl8AJFpJHx-kuNjadUoH5hw1IDvKU9VUAVkeqsCUfysrqkGxx0ug1P5KuNIu1sv0OmKTlIa6GT-55hmIA5zcYGGAUoTGL1CTQSOiRN5kHYRCJXFpXTVxAVlgxdtIE1He07Izecx-CJf6ObzAWkmThLM2Y29FJ6_CueRdBxmP7ndBZGfplVnEZFDQ19x3WytqbThvksnhd0t5l1wFYxdq8OBYcDvHeU332j32hig9jdk88Q_EZYRHaF0aNDGlBX125H8UTR2Dw4Uf7ceNz85Xp0nPvggtyRIaZ0_nTf9dTFGOycXXTF7t6qXPkMNaIjM3dwS5rzsc7vPctQcf0_9C5N9KqKAJnqUtwwjVRIBZQAxGn3yOWMFSCtz1gQIIcP4NKqCozvsCtbLNY2ISbAYOkzdaOXLCJ7cvlCkhTjvcP6R5gb1yPR8P825I7XuOy8MUCTxCKMwwj8dCyU6i3P8iHUOqNv5npbl1aeSeXwpZKsxp1WBtBKCQtFE5r_NdGfvIW5UNeP64WHlXYGW3DvCGfbw6wzNfhUW-1KgHYTqAhYwzs2uQLIOz6zjCpF1czpzxO1My4860JNx6MYOjG3F347jG3cRGnqiDEpTUM3J3Zbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
بازی‌خاطره‌انگیزمیلان و یونایتد در UCL 2010
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102490" target="_blank">📅 09:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102489">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">هایلایتی‌از بازی‌جذاب الکلاسیکو در فصل ۲۰۱۲/۱۳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102489" target="_blank">📅 09:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102488">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BX3OSkCfk2t2h9NBtjmwjCYM_YUE1KEdH2WX3GB5E0PMbpkJjPDY_ntHsPTdBCbL0kondH1gKVZkeYQBc8pkC_A5wPsCKhjrlkDngDdA7jHo0KhKadfSWzpremONv7IcJ8d7Nf4I5dR91NxLZb-wl1ndFcQlLK58pG3AnyrO65R3Ki7a1yWcmqtpQi-kL0vyYngJgB1dXWlO6IKeg-a5z8QEA6eROBBXBPGQrwlezd8NceBQPTlxLxZUTNGfAHr182LrVZyZhTur9s59Y3vb-RqAr8-Dp5x_ozxCG1NQ8boWDBbtZmETh-JyyZLQ1P0CFENZE4LlreiJkLfRLuAiRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنای اون ترکیب لجندری بارسا چی میخوردن؟
مسی عالیه :)))))))))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102488" target="_blank">📅 05:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102486">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_l3p3IzIfG_-4H7VarvMccPGLQ5XxfFm2NiWUIlVZoByTI32mKegGqTPW9DaMJQTK5yoJFBmf6UuM8A4tko4SDwGCf4JClT0pCxvtZUShvhKahRSFbtf9WRGo6EISiiftLrgP9OCDsXeHVOip4KtQnftbemHJgikkvOC9ZZBaI_upJ9UI9P-Za6Oc_KRHlngHomlX5krRLGcUWjSMuyg9A-dvrYL3nzv--ASdGZ7Z2D21rNp0BGQtLfZMPAqSZg91w4wFNCoNaKiwmkPuV5ueEkjdMGSAS_8W5vZby7X_4cHAr4G_jh1HY-7K4iYlwwSMPC9woPVdFJGofppDSfug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
گوئدس ستاره باشگاه آژاکس با رقم ۵۰ میلیون یورو بزودی به psg ملحق خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/102486" target="_blank">📅 02:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102485">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
🇮🇱
کانال ۱۲ اسرائیل: نتانیاهو در دیدار اخیر با ترامپ موفق به راضی کردن رئیس جمهور آمریکا برای بمباران زیرساخت‌های انرژی ایران کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/102485" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102484">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrzKPGnu0cARLbTExcCC88j886TvR5LSZsCiHmII5iWxh7UYMsXXVIY11dnWVL89ToEblN09O-CqoyhbTjFYfysacjNpHQhSwAyPvQLVzRWbI6GEAjH9uV99WpURbCnE7TrGe-WzVRoT9DKV3qdZpan3szMhlZBhCsNOshaATfJvoMKaXhAtwp3M3coq2QQ2ivc_LggaUwgX753vJ_0wi06tyW1a_ds8qF_Sa1vd9LLWRWJ02n5uL9gNcW9BfDMLaWVfNbWN3XVgbMd3G9TgWMGLoD0p9x_MHVXDw8v_b7ggFO7k9Ylfmfv4oZ1eJHKRBGgObEe5F1bS6LkdOgc19g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب بروبچ محله تامی شلبی حسابی واسه جود سنگ تموم گذاشتن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/102484" target="_blank">📅 01:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102483">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔝
وال استریت ژورنال در خبری فوری از صدور فرمان ترامپ برای آغاز یک حمله نظامی جدید آمریکا به ایران خبر داده که می‌تواند بزودی در این آخر هفته (شنبه و یکشنبه) آغاز شود و چند روز طول بکشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/102483" target="_blank">📅 01:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102482">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vO6afepZvyPqBNUov_WqY81DQUyL0X-hrmFSil_FzD7HYknSDDyWq9xDodWNay2NrBUtwIZSi7kHvMbQBRcY5P83i-k2m1nFCDgQVEefxgz8xnmqosr9P5QDq6Qa4SJgkraRImyAxWVj02Z9S8gZg7dY4JnOxfA9FYideTPdbTn8a9KJZ7Li5KsXbHFcyGiqLr2erZPSsKQF41xyOovO1dEZ592MmhqaPD7MZ2VHi0AmZ1n1ZUGKs0WJCZHZ-iwTKz0Dhv1a9ZzZnPVT4XZSl9ueAV_b3Zq9Dguxjombz2bi1fIg7yV1uYGrnFiBekyAgrZDaj4_DqDrL_RdcwtGog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔝
وال استریت ژورنال در خبری فوری از صدور فرمان ترامپ برای آغاز یک حمله نظامی جدید آمریکا به ایران خبر داده که می‌تواند بزودی در این آخر هفته (شنبه و یکشنبه) آغاز شود و چند روز طول بکشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/102482" target="_blank">📅 01:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102479">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kkc1stNtzWl9rsylzMCjqUJz670HgiV4f3tYX7Pv8dpCasntyedhCpuzkv12lm-Knw_OQPRbc3YBJ4zsdXcpwv1oQIQ4Ll3FZckJHxMKM75WbKvXspMTX9-NHg2trJmVm3bUn3rM_khEUumTclX9x4iiiR9O7dIIEl9nN5nML_T32hVl3pseWy-E-sgWPX78DjnYSaHNI0la1S_WNoT_IIyV_PzxJbH-BrTYWd_EeERB4tghov2zblV-1R57PAg0EVyBPjQ72zmpxkw5YIckKbSRKJnSfMiOx24Mvyq82VBYe5fnheXna6mTh_auZgMEXRiZQR8jcMOHQRKunxJ14g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/udy3YDm5shqPpRSKfa6eNY0nJY3InmF5Ef8GQ_TkqNygFqfZDQHei3nzbXKljpzW-7mhxTH4cMK7w1wdqfvJkgd5G6Zw6zOIEhn8Ym5pvvqPXAPXU-LOdrjWL6JIHPoeS9FbVAgmv2ZKjlYOADlpm73PJNeMnltkseEfdth7dTFNlFgAbNdyshJ0pmm-x9zv31KQSb3JIA1oo9G99z2oxEXZ4NHaq2NwvQ5ZwsTFvUgKqG6xP_lzUsdwFN3qSXr6yVSGEeegVWtrWqw6984NtilmmehpP6ww-gQI0Ykleq7IYE13ZzAx1lb79XBpZErLgAT2dAN1brW2Yu8ARfy46w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L-0H5oPwNGzo3KOiRMPvXqas-yiB7KDduOAuFCBZZ_jjgAYRzZBv02bhRBDquSLe4OJ8gzubbg2-ZvL-6L77r7f5EijEaowVwbqJVw3_jBgWflSC2IkRIlB3kFD5tO7FhrBYQkkLLJy1ejesQYwuSkRlHvLfzXSn3CZUyGZhMdlPHFK4jAOsOEtVxz5JAhMkyG4w7w9ElBsRu5JATT79x4cqJDvsR8IaMDgBNfktzDhCjIDduyG6Sryed6U6_pV7niI5fs045sG7N_fXtmE067OVJXNQD7B39-SdP4L_ioQmEMq1WHJxKFUKdON9CuzjZdaTOsmUyy6cYcrrOlMXcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
باشگاه فوق العاده محبوب آگزبورگ از کیت خودش رونمایی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/102479" target="_blank">📅 00:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102478">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2QrDul1pgDyXv3PFoLkT9ZDLu9JET6tnqt3je8KGE9SS28IQgm-26AMVwLrIcQP4m2AZWA44BlV7HFVOSfhJMPTk1pEATLEYii2muUOuehWV0DXE8JJH7kpyj7800GV9WaskZSWxG_CqUH0N-b3_JQT7KrdEL3UGt02ORNJghp_2PQr2lo83gECnHSiKLOxL_rDiF0RKeK1x7YW62KlALr4cnp0GZDYJHTjffc0_T7Jq2JrATaaHW_6LEpymwsMGF6rpFiLezG1QfXdcdXi56S0WuaeySiqq-TdW2Uez4tthNEPHb7mIWp4El5NB-lPDtvd4K1PX-km8lwHW9WcmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
هندآف آرسنال رسانه نزدیک به آرسنال:
وینیسیوس شخصا با آرسنال به توافق رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/102478" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102477">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی،…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102477" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102476">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=Sqb76giEnFEMMHRywcHGBh148DuliBATIE_qQKvRtwUdMUox0oxb3863OAe56nvatKDdSKYwZEBUDqxPhhtkhRK4fRa5Mo7dfTdyMFskM5Oor0mXklPPhPcXqwoJpqzfJUdFlkYC2u7XDrO5NCyOIR2MfkB0l0-eHAsvgxKV1L8IUUZzPiQElRmB4lx0xHggzfBo3_oUKi6U6dkYYxqExzUQr-3sDwqls8pT31eicsiXHHknwlgiNH9g5bwBy0CxEq71oKtMXT-9xrwk4lxHeN5MsQjPN0Z4j9mDNb2G_wUnUKgrCa42NEEMc4glR2OElBSDieyKVKjMM99DPJHgQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=Sqb76giEnFEMMHRywcHGBh148DuliBATIE_qQKvRtwUdMUox0oxb3863OAe56nvatKDdSKYwZEBUDqxPhhtkhRK4fRa5Mo7dfTdyMFskM5Oor0mXklPPhPcXqwoJpqzfJUdFlkYC2u7XDrO5NCyOIR2MfkB0l0-eHAsvgxKV1L8IUUZzPiQElRmB4lx0xHggzfBo3_oUKi6U6dkYYxqExzUQr-3sDwqls8pT31eicsiXHHknwlgiNH9g5bwBy0CxEq71oKtMXT-9xrwk4lxHeN5MsQjPN0Z4j9mDNb2G_wUnUKgrCa42NEEMc4glR2OElBSDieyKVKjMM99DPJHgQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی، باشگاهی و دوستانه)
🔹
پیشنهادهای دقیق گل بالا/پایین (Over/Under) و گلزنی هر دو تیم (BTTS)
🔹
بدون ادعای واهی ضریب ۱۰۰! فقط سود مستمر با مدیریت سرمایه.
آمار ما در ماه گذشته خودش گویای همه‌چیزه. فرم‌های امروز رو از دست نده
👇
🔗
[
ورود به کانال و دریافت فرم‌های رایگان امروز]</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102476" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102475">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GC599jkIGJX1-QzQ0iP293sqGM9ZPI2S3b799DCbIlm7Foj-P0d_uB5GzO8nfKE_hYut2-k0mwT38Mo7z7BKwn07afE02Y6bLz6GdiVozzTnwb5NubcY_d82yBlhNk3fN8aAdNrfYNRcH60gIYyJbaR-FaJ1EVlwErLiyturZpYQG_4R-3wxt0V6sV-Rz-6HEo8lqKFGaf3h-CePim62NBQqfalxpLGXVt7UaxiLIx-tOWmCxpJgnlPJIVXv1VZyLQTB1_rZRIWxPg5Y-3oNBrTCW3MGDDNOBIr5MUSrcGfGzdolQ7P4W6mKQ9ReGfYSuDPNM7DtntLyVNeUrI5n9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بارسلونا در یک بازی دوستانه مقابل بیرمینگام شکست خورد. بیرمینگام با نتیجه 3 بر 2 در ضربات پنالتی به پیروزی رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102475" target="_blank">📅 00:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102474">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nm0_xK7wpIdPgxf8x1VGpIBXCoR5X2GYaAhfSsv76yefr3qy39sa8A4pM76TBXRNj_MP_p5jPSq7Butp-iK_8BowhyocrMc-hZojTMMeqUWH9wiJZf7ZhEDZAic5XRBzVA-dx5lqnl5bu-nWT2uJ6yZWR2pf7PQTMCcgjMBjdZuIVZk2pt6KWjL8URYAEr1tvNYXG7ZHjC5hwumkYuc_tb6xvNhorNI11K-xwmowl8a20DbmVsCwfBNvUTjBrjC_ZA0F-4Xfc2aoxK5MfweglfpgcotLKRp6uznx9H5-V3ZFs-DBGM-12x6wl3U96DmzCKVogAzxW2PRzy4nH7bETw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری دوست دختر یامال
😦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102474" target="_blank">📅 00:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102473">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-lMAPoMObvaTlE0GCkHluUNXdRU0PzkXF65AdFHFzf4VymoJ4Rk8ivS2-WPKygdx819D3PG-wJjRgXEX3hlGuUskuLnKWxPVE1qsC3y4A_6HUAqcmp4egcyFfRtwcuKx0WuPvQQDVXravO4OckUF4_Nw1dTZQ06SpBYAYkwpKraWfCyz4rJX8oFQ6Y6BkPjotWc_QJOKhQmkGgot45HD8W7q52UyKn_T6rW64Syjy_-z1N9MedJ399pCR22LiykL8GHJ1NHnPFiGY5X54h7ydrPViFAwBsLPDApqPVz1y-E_EGT0X5Tnm4JxCHvs-8qy7vCVrr_n1YKxXqyk8dQNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟥
🤩
خداحافظی امید عالیشاه با هواداران پس از 13 سال حضور در پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102473" target="_blank">📅 23:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102472">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sl8NfEyC6RAbj0x5GoVWyntO1w9NV9A3vBVHZjFa3LVlzh5asccVy8-y_kuJoqopxNS83GTaJ02vgLePhwtmhLDEjQ2qKeGtcGQDf3CNzlHp0H3PgJypox1p09gL79WzqqAqb_eaBm6MUwLAZfu80jdJZPwav4pNpayQbwxABq9Yp9DoBbE_vsMTbgJ_TCpmwUL5AMdqV3gUUiwDy5KWOgDwZM6EU_GddeJH4hCVa5PjCU1v-t2pzwrgi03D7T4n8uyu7Sv_2yL65AL05KAOoz2Ouju6MykX2sJxYyWhF0KohVva8Iqi0PpAfO11FdoubqsBR10VetMJeY0yBYRLWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
مسی و کاسمیرو تو تمرینات اینترمیامی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/102472" target="_blank">📅 23:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102471">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c665525c.mp4?token=qIBPbUS5Y5rhNPfItmdcwO2aQx-BxPcfogsmhY73joKOuAKdL0hOrEnrimWbv8TI-8UTFRK4ubCPUCUhmiuGA7ZeszNM-6HJnnPO7AtPUbXB5QfnFP6Y4Deo0jomXWTQRNO4Jds0SPfkab7fU-dt9XXKO1ciQT1S2NQmCG7Ga4KWMCYTqejRFhWe50sEQqmiYbgfWG-9mt4ViSik1Qr5BqhucfIsudp-RyUlzfeLL_lADJZi2EfmPNG-rvcpoQRoeJsFLTgiDBfaDmL1toIhZnz-UVvdJn91r-q4S0zPaZL9sRmttr9mhrwnbRb6KfoNpevlVNUXclmEUz8WpZPCAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c665525c.mp4?token=qIBPbUS5Y5rhNPfItmdcwO2aQx-BxPcfogsmhY73joKOuAKdL0hOrEnrimWbv8TI-8UTFRK4ubCPUCUhmiuGA7ZeszNM-6HJnnPO7AtPUbXB5QfnFP6Y4Deo0jomXWTQRNO4Jds0SPfkab7fU-dt9XXKO1ciQT1S2NQmCG7Ga4KWMCYTqejRFhWe50sEQqmiYbgfWG-9mt4ViSik1Qr5BqhucfIsudp-RyUlzfeLL_lADJZi2EfmPNG-rvcpoQRoeJsFLTgiDBfaDmL1toIhZnz-UVvdJn91r-q4S0zPaZL9sRmttr9mhrwnbRb6KfoNpevlVNUXclmEUz8WpZPCAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین ووزینیا که تو جام‌جهانی تک تک تیما رو سرویس کرده بود، جلوی علی علیپور اینجوری فحش خورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102471" target="_blank">📅 22:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102470">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpeGs3nx96bvmOx8f9GFjcFC8y1JtVXkjfRmXIvWA56bPTPjYTJRBOslQf-VdoBrlY2WseCUIVNPh7Ius80WwyWihwimB2izgJX9K0hjw_jROPrrcaDinLMRFU5zIRnCNpUaoobyvOSP93OHEBn9FpHLwj35NjKqud2s14RWqgjqVGokH4pDSP0nN6jdsOzkWxRSqPubqGa8x6q6c9vce716axmT-UJ-MZp0cuUy0u6Wfx1ueX1qtu52FDiHDtBW-9xjMoteUt6LWs5RDwig_ysxxBphjYZJWI-2x9XurK4dZQ01Qj3ZZY8iIzkZoaInVmdBXSrxc8HBE3FYJEP_2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ار‌ام‌سی:
مندی تو وضعیت مالی بدی قرار گرفته در حدی‌ که مدال و کاپ جام جهانی خودشو 54 هزار یورو فروخته.
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102470" target="_blank">📅 22:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102469">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/261dc7eb19.mp4?token=GjUZJ9s9RIHQjmNkkFxdkBwqe6scYKa3bN-kZ19HNmzTxrsHzjp-qKDkCQef6DbimN-45Hz5JjvbN__AfaJ3gGEQKXLgC-H3rUkgBidWdR74WLqVfFfjV85wtXGkaQlLYDLZms3Hta4mi6PbqsWdKYppe7uB70PTEL0J0qEW73YtL5cYmZSVmjCDfjG7svXiwpeXctTYWeuyl8OXSwiIDMK4sNuK1krDro4NVFU9XGdZa_RpePdVg998gQywD7YURJyal44Q4HHgxRF0gYMif4uL0ge58xXjtT6W0aT_gu1D-Eg8rEeuMXCf1RvKWp314B3H0oipJyAsTVv_i7ax4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/261dc7eb19.mp4?token=GjUZJ9s9RIHQjmNkkFxdkBwqe6scYKa3bN-kZ19HNmzTxrsHzjp-qKDkCQef6DbimN-45Hz5JjvbN__AfaJ3gGEQKXLgC-H3rUkgBidWdR74WLqVfFfjV85wtXGkaQlLYDLZms3Hta4mi6PbqsWdKYppe7uB70PTEL0J0qEW73YtL5cYmZSVmjCDfjG7svXiwpeXctTYWeuyl8OXSwiIDMK4sNuK1krDro4NVFU9XGdZa_RpePdVg998gQywD7YURJyal44Q4HHgxRF0gYMif4uL0ge58xXjtT6W0aT_gu1D-Eg8rEeuMXCf1RvKWp314B3H0oipJyAsTVv_i7ax4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
تام هالند یک‌بار به ارلینگ هالند دایرکت داد و از او خواست به تاتنهام بیاید، اما ارلینگ اصلاً متوجه نشد فرستنده، بازیگر اسپایدرمن است. بعد از اینکه ماجرا جنجالی شد، هالند برای تام پیام فرستاد و توضیح داد هیچ قصدی برای بی‌احترامی نداشته و فقط او را نشناخته بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102469" target="_blank">📅 22:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102468">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYlVgGcv53AcpZ7iKSKnrlWjnmAeXSpsuQZvluymRoIKAAO650dr5I0GHbkJFWcrHRLYFria7_5DmYVlqnnalIKCflHS4SN8oC4LPikOm-FB9_v8ESZJs5IJDqlrC-GXS9YGKiyjxET1J7SDeXZntWkN34_u-EpsrDNs6H03Sdbi2gwgZ7DD6lOI0PDDBNlquG_YN2xzL6mFSp08ZicBMxN_pYUJk95JPxmvF71VF4HSzQfBrXnl_jIx30MCAZGdlRuE7adgo4HDM3ykW5JXpxJfVavIhE8Pt_qSSCJpwwcUQ7MOSIqeRIYakLkKfjjUE4ET7_4ZpBBoquLs5j666w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💣
بمب لاپورتا ترکید:
جسی بیسیوو، وینگر بلژیکی کلوب بروژ،
به بارسلونا پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102468" target="_blank">📅 21:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102467">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyo8UcXpjQ55V9PP5ZrutaCdqfFbXNB_oHmjgYQHhkJnsC6o_vQz4IeukLvl-0xGKRAI2hd-rQrHLfCvthUfdzL9Yehy_ksPHNgnlVtkezQq4qwNr6LdGc41vZ5NtNXqElj9TnmRnLc9uEp9LVUl9HUcG77arUYZYE-ta8MYc5b5MKEkjOOevC_FOyBH_QysM6A4xHgRg037WAM9sTsguPRwTLkvqQYd8nMiK28plaSsyh6l-tsE-ArRxPN-y24jm2cbzFx85ZYxuntPZq7ElXbINNGbklsPJen7fa2f-i9FJzl6YlxfPyIqtGMzvb8KakTavqEav6eUf51IP29TLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب امشب بارسلونا در بازی دوستانه مقابل بیرمنگام‌سیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102467" target="_blank">📅 21:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102466">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f4d6d3d7.mp4?token=hQgln05_-P5sloELBP9-9UcJKF4kEw2UYgAGW5JO1rVqZFMZijqia0J8hC45dVT8eWrF4XwEDUIl0Qr1mNm-ZqEuXaeeuvq1WaRgNA1dYf3DdYK2s7-Dwv9lTmN9NJvl-csVPrEcX4LKwH64BXZd7bnaTrIkx_84cfPEx3XFv19PtA0KOhl6iT8EsFqo9yNeThQkaFdbYD_TXe1hEnNXjc9XFac1S_8iXkg9jObN0JUXIQqCj8I5IM91pra8coInKJZ13t42pLUZSlABoX3hCtAE75mMb5ZvDPOG6mKy0CevN79kWIUPK27X2SaeSmMoBt9w7jSLh44hQWhUBWUOPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f4d6d3d7.mp4?token=hQgln05_-P5sloELBP9-9UcJKF4kEw2UYgAGW5JO1rVqZFMZijqia0J8hC45dVT8eWrF4XwEDUIl0Qr1mNm-ZqEuXaeeuvq1WaRgNA1dYf3DdYK2s7-Dwv9lTmN9NJvl-csVPrEcX4LKwH64BXZd7bnaTrIkx_84cfPEx3XFv19PtA0KOhl6iT8EsFqo9yNeThQkaFdbYD_TXe1hEnNXjc9XFac1S_8iXkg9jObN0JUXIQqCj8I5IM91pra8coInKJZ13t42pLUZSlABoX3hCtAE75mMb5ZvDPOG6mKy0CevN79kWIUPK27X2SaeSmMoBt9w7jSLh44hQWhUBWUOPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔹
وقتی منچسترسیتی حریف پیکان نشد! سال ۲۰۰۲ پیکان با سرمربی‌گری ذوالفقارنسب برای آمادگی در رقابت‌های لیگ برتر، یک اردو در انگلیس برگزار کرد که در بازی دوستانه مقابل منچسترسیتی موفق به توقف این تیم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102466" target="_blank">📅 21:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102465">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bcb0e2d66.mp4?token=W7VPM48h6RXsbVzgB1dDSb0DmB7nxrocrzeOJjcfuvCb2wIx2aUA1-aJt_F682rwmC9RLNZ-rlS025Ii8tp0_EfM1XmyDsMMEtKGacj93X11-LW4ItVuqZ0q6tGM1_8OINGE-BuCy0HNzE2WfpW63q6_0q98HsQuQ34KjMGGYWB2bjn_VFyI01dE_ZiOWMIGLrwQN2u9Q9R9F65ab6dNCPBYbRfOKaagKlgZveFclo244rtL7ICCCH8pV2ousI5CkAE8tlE9PREYQZWJcg2WijrM563ytRT-Wb0l9L7hI8TYX-LYUwKO9ztLzWxfDW-vjhCDHrjYF4yZRM-LKSg1lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bcb0e2d66.mp4?token=W7VPM48h6RXsbVzgB1dDSb0DmB7nxrocrzeOJjcfuvCb2wIx2aUA1-aJt_F682rwmC9RLNZ-rlS025Ii8tp0_EfM1XmyDsMMEtKGacj93X11-LW4ItVuqZ0q6tGM1_8OINGE-BuCy0HNzE2WfpW63q6_0q98HsQuQ34KjMGGYWB2bjn_VFyI01dE_ZiOWMIGLrwQN2u9Q9R9F65ab6dNCPBYbRfOKaagKlgZveFclo244rtL7ICCCH8pV2ousI5CkAE8tlE9PREYQZWJcg2WijrM563ytRT-Wb0l9L7hI8TYX-LYUwKO9ztLzWxfDW-vjhCDHrjYF4yZRM-LKSg1lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚪️
رونالدو چرا رئال رو ترک کرد؟ شرح ماجرای جدایی اسطوره فوتبال از زبان خودش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102465" target="_blank">📅 21:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102464">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ed94c011.mp4?token=AHn0d1TAZ97qFLFog_xj9-qMT8TTbnGwi2u52klfANtonJwwsQFQoUrrFUAG3KPeCSggNj2PcHYrIZ3-Odtm6MuvVuKQzRc6AMbcK4o_gtKFYsZJCM8lfIK8s2sku0UmOy9zKDProV0TbJClms6zQhOXdk1F3lKW0-RXgqhN7EPwZhipHpW29vRoztJUkqX9oyzPeu9mzalns-vWBQTLMQBguBJEwgRbwKBR0vib6OVE6HCqWd9bwVwGZwSZxDmpyOucJ_NrTy4BIZ5fJUC0N2nfNBv044k2fOf0v73Yq3iP-6D9AETh7Zu1WCV8dyr6vN28fEL9nts9i70Yjeeuaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ed94c011.mp4?token=AHn0d1TAZ97qFLFog_xj9-qMT8TTbnGwi2u52klfANtonJwwsQFQoUrrFUAG3KPeCSggNj2PcHYrIZ3-Odtm6MuvVuKQzRc6AMbcK4o_gtKFYsZJCM8lfIK8s2sku0UmOy9zKDProV0TbJClms6zQhOXdk1F3lKW0-RXgqhN7EPwZhipHpW29vRoztJUkqX9oyzPeu9mzalns-vWBQTLMQBguBJEwgRbwKBR0vib6OVE6HCqWd9bwVwGZwSZxDmpyOucJ_NrTy4BIZ5fJUC0N2nfNBv044k2fOf0v73Yq3iP-6D9AETh7Zu1WCV8dyr6vN28fEL9nts9i70Yjeeuaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یک تازه داماد پرسپولیس را حذف کرد!
از ماه عسل برگشته بود و چهار ماه حتی توپ به پاهاش نخورده بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102464" target="_blank">📅 21:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102462">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102462" target="_blank">📅 20:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102461">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f8b6948d3.mp4?token=DZjyyoA8SkiZ2z9waIPxhK0wt0PaXGZtH-Xo8MvzvSbQsLy9E6wJqzsaZcZQNckDtHScoWqPFdNSTzit8VqgPJQhlRDL1GHy-06MH7jr7_bOm1nZP5ctbsx-ncJ2uIcBpxwdJfqcg9SPYQ1fjVw2JoaJS205KfLRvICSq9xvVbGKmrQ_9bbj_CwsGFGOi0oh5oxattBtT1WnM2I7T2MMa7rnySQfmxJdLgHPTJVMGtv8oqKMVx2y6Bc8GMx7lZ34dhDv_dYHsKhUdmO3BiP6JpPfRIBwTDePwscdxg-bdd_uPLjOLeJA51OiWm2CJvmy5bQr2jwtwJH51tKsrPv7Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f8b6948d3.mp4?token=DZjyyoA8SkiZ2z9waIPxhK0wt0PaXGZtH-Xo8MvzvSbQsLy9E6wJqzsaZcZQNckDtHScoWqPFdNSTzit8VqgPJQhlRDL1GHy-06MH7jr7_bOm1nZP5ctbsx-ncJ2uIcBpxwdJfqcg9SPYQ1fjVw2JoaJS205KfLRvICSq9xvVbGKmrQ_9bbj_CwsGFGOi0oh5oxattBtT1WnM2I7T2MMa7rnySQfmxJdLgHPTJVMGtv8oqKMVx2y6Bc8GMx7lZ34dhDv_dYHsKhUdmO3BiP6JpPfRIBwTDePwscdxg-bdd_uPLjOLeJA51OiWm2CJvmy5bQr2jwtwJH51tKsrPv7Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شزنی جنس رسیده بهش و مشغول دلقک‌بازی تو تمرین بارساست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102461" target="_blank">📅 20:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102460">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace3163b65.mp4?token=rB3X1aC1zZs2sajzb9vIO36QgwRFiKV_2mQuwMOw7_0ryXgJrCD_bcLAvW6anLALYJojDx_9GgLaBIO4LfFtvBDoNqCYgh4MtqSNaiZ1jAdEayKYpDLAjE_7kMoD83JvjZh3-h9gkfRwBWYVe1ut7jpq8ztwc6Pz0skf89UTT6FJjQfUhG4SZydRmFwSsMybunYpMr-usO__f6cZxFwBfAXOaqIMBXrkFpB-1cSKygNTMnBtn3_nUMy07pnDB9KRXdNNbANw-lVm0xSc2d2HDUObkak98LWnLVr0lo_R6My_v6XC7laQyKeWWCnHjOrnTfYyilgkgmGabJkYTXma1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace3163b65.mp4?token=rB3X1aC1zZs2sajzb9vIO36QgwRFiKV_2mQuwMOw7_0ryXgJrCD_bcLAvW6anLALYJojDx_9GgLaBIO4LfFtvBDoNqCYgh4MtqSNaiZ1jAdEayKYpDLAjE_7kMoD83JvjZh3-h9gkfRwBWYVe1ut7jpq8ztwc6Pz0skf89UTT6FJjQfUhG4SZydRmFwSsMybunYpMr-usO__f6cZxFwBfAXOaqIMBXrkFpB-1cSKygNTMnBtn3_nUMy07pnDB9KRXdNNbANw-lVm0xSc2d2HDUObkak98LWnLVr0lo_R6My_v6XC7laQyKeWWCnHjOrnTfYyilgkgmGabJkYTXma1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کول پالمر:
برای بازی مکزیک - انگلیس بیدار موندم، ولی بین دو نیمه خوابم برد!
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102460" target="_blank">📅 20:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102459">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QutsOgFNwnd8SkHdQV50J8tIVkU0XxYHuVQJT4kIW7y4d8iLAAQtp1BlMI3cUaUaB-9q_IKkTk5zda3t6A4l0y1gZaYFnvjHUpXhgdlyFSELFxOq0CgWYzUS0kvD7fkkfIFE1yD0luxBWaL0Vvf9iAAmNBoaHGA_vEqrxRzR_-luFjUv5y4ieMXcLlqW_U5ztFagNjLKHoqJ8GGSPOf8J7R39fUjhHuLHOISGaY9V7GB_Ya30yOHjlVZiVnT5JwXEegKWDsCb8EfO6UVduRTifZX6WNoj385YX2icp5CnhS6jW1KUAnP-zOmnGKNXjgzxrzWiP3ilOg3iSI6dxW58A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
دیوید گرافسون دبیرکل فیفا تصمیم گرفته که علیه اینفانتینو کودتا کند تا وی از سمتش برکنار شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102459" target="_blank">📅 20:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102458">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2TSEWI8NrQNzym2sCvKEhc1QswyExKA68fEgvhZYQ0EYS-dGMB7mcpaRWzl0327gAhlHhvyXZmjJ4cijoX61jrPusnZ5vK9gUt3PubOsJnQNb0zjMmfdASYkPX2-S9M5y8mM0UGtU1v_8R1icqm7xQg_vXKiiuxFmBL1J6fGVAR7eBimd52GSwtdFgeBf4i7EMhl_iInUFEVZMOKySo3DyRgcV6K2Yd_1z9GhkveJW5H1Un-B8UkWxH51Leu_NBO2ysgMf7QSuRufYWIEt0PfAJRBeR2LUfWEsN60Xl3oUXkiqIwyj0K7o9VnrkTCDUfTdFRDV3AANo-IcVYIlN2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
📊
فقط سه بازیکن توی ۱۰ فصل اخیر تونستن در ۵ لیگ معتبر اروپا هم بیش از ۲۰۰ گل بزنن و هم حداقل ۵۰ پاس گل ثبت کنن:
😀
محمد صلاح
🇫🇷
کیلیان امباپه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هری کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102458" target="_blank">📅 20:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102457">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiCapO_EykylVsgTGJY3j2oSREQATUZKOOkvlfgKjSK_2xMvSGkisgR57bwcsaXGJnB9hRoFAKujq1r4gDXOVHd6UU53aGgfoI7tEjbLs58uDCEk8ctSbLF3U6NtOKnBzEiT783HANWiKZlm8SVZlW4fjxZJl3YgwhF7kIG3URtTg0mxijV9hb3RVPMxVM7QmD3SQlCfGpef6yIOGs6-rHG9MzxbBNiMx57CWvxKow9djDulU5-nUtOopZn3FioArecIiUYf10Bgfm-Ct2DJ4khqAnb1tlRSUryfgQU0Ot98hDdVMa-HOe6rpMSob2NGkL5T5lx6Od5JukXnC7f2WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
دیوید گرافسون دبیرکل فیفا تصمیم گرفته که علیه اینفانتینو کودتا کند تا وی از سمتش برکنار شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102457" target="_blank">📅 20:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102456">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102456" target="_blank">📅 20:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102455">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlPZPdShsKinYEhokjJoLiFKWLxZmdQtngm3zrORBz8oUuHlFL7045xiH4LZmwfVedUXaizI4wnjewaEbdCIe62pN20aWjks42iYzDZNT9vUfKU8IeBqo0D-msOhiqoqp8M8P8iapwdjkpKbFKGcKHHMr1yncUuTntelJAJcA3YThX9XWazvdsp1_ds7c3PUp2l9ABHZcga5edDXng2f1qx-PuRobDCBILb9kZ12FgadD99iAOJtYSzFgAeUvTWU0NzfHzsPHHAnGZGkw1JXbJjEtECMw0oZrD7ykBMDGe4gpToHRHUv62PxrlovAZ3kYlEOZistQkL_OwVq6YwHIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102455" target="_blank">📅 19:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102454">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdTani4MP0u8FsC1hFkzmQ_JMS05a4JHbKx-VIb7ipnzVMajMibmapYZxSsdWNrh-eDD-MxUy6u0q1WT-V6Ml1PQm7qUMbm5i3jX21xtze_iwzzlH6xiLgT1tm5lT7z7zuI_9Aw5OtO5ivBbEBg2gGS566aCDLgXGmCuh5oM0kYrYC4kjipaHrsAG4XLMooRAqZvsFjwXj1Wx_Io581lHsfiyWyiRhR9TzjYKeHnrOS_zWbrNfhEtJkmLrCJxmxiNeBgrx8lyp0GqRhQvo_r5Y9m_dGWT0FXVg_Pg0aGfNMRUgIHPwbHv0ViOsYE83UHrpFmOiJZiuDyCnatmBChRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇯🇲
وینی و عشقش تو تعطیلات در جامائیکا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102454" target="_blank">📅 19:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102453">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
📹
🔵
🟠
پخش زنده بازی دوستانه استقلال و فولاد ساعت 17:30 از لینک زیر
👇
https://t.me/+E5pLb4kNVJZiOGI8</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102453" target="_blank">📅 19:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102452">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کاسمیرو به همراه خونواده که دیروز به این شکل بعد از معارفه عکس دست‌جمعی گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102452" target="_blank">📅 19:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102451">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWoLOXPamDcPte4fsjCyYzUUEU-xZv9GC85RMOxg1rnwm8kAsCvdQu1WLElcJzISdBuzKOrnmaa0MCo2BZ69uqvCGs_QVJotucm0WEqMS2f9_kCJstAsy9O0y6oZfm6BeZZQTvuGTb5OhQVwnakwIFhD-Dd7beed_9ohnSnWwkCdrjjkbXC9n3g8xTGAUW7Q8gCRroml4a1gNssF-rdQF7AssAPYBNoD_lW8jq08bO-UwBrWaREzeLq3qE5K1pMM89yeRgJJ1HFyxTEXu54m2OWpjxW1mdYc86ZkILIcLgnu930xE-mstz1MVTvJrfAwL7CAD8jHI_C9mpLMVrC-xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
رسانه ESPN برزیل: رئال‌مادرید هیچگونه افزایش مبلغی در پیشنهاد تمدید قرارداد به وینیسیوس ارائه نمی‌دهد و پیشنهاد فعلی همان آخرین پیشنهاد تمدید قرارداد است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102451" target="_blank">📅 19:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102450">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjCFZPfns6FhwfZrFEUu3Qce2E7UdhZYEUe4rZwzqOEI1L5aZ2B2uOsYxCwkReRBtQG8iPS5dZ7C5SAsC0EYUeirIF-0jF87E6OxGh9VKAr8GpH1hK5GJj6xJcvL89DdMpWQfUf9u6f9MP5488zitM9_KQghPikvrtV0kMa2s6O_f66kXogSuO_5wpP9WeekYwycpDfZPp5pIatO5hwV8p9f8zPVdS8i4h-RBshXBoiif0up8-aS3cr2lC-Eeby7AHwlJ54c0g9XxPrV4UG7fZtePg2cvcxyfLkg77BEzT7hLd-qUTMu0o7fIbf7K-gNiffLylsZ5w8L0w1qWjelMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
اینفانتینو: جام‌جهانی ۲۰۳۰ بهترین دوره از تاریخ این مسابقات خواهد بود چون در کشور زیبای مراکش برگزار می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102450" target="_blank">📅 19:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102449">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LklpAocuzIMmoAIcKpRO4qKlv58XIp3ghXyD7QJP9LrIdLm41BoS1229DvFNshjq6qtmGRjbksq3bYjZgTTAhTxd1XdF3lHciZ8zXeYboJY-1nZfJtypvTAAplhMxMklJ3ZkrNSQnQXMvLgDYQM24ybiFsAE6BKPIzxIE_OvzZHY68XrRxpoKmoLeH9Roii9XACOC11-s3lhPMniDyMNiFMLKDQ7umBcC-JNoa1jSF4mVECs5jIPt-KC8okLNn1P5qaWVe0YcNVWRcJ-w5RMVNoNcvK-CmJY-BJuL1kA_bcW9OgBYNKdD3iixXSqD0XEuVPSnzIXtXb93GBXOM0-Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوفیس تعدادی از بازیکنای فوتبال
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102449" target="_blank">📅 19:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102448">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTJs9Lo0my7oOJeliMg-lELla_GMh_NCNMIbAnt7LQxpKTF9NUJ4Qj2mZN8YE4LcMJlzKk1XwxpObYEcGxB3rLCgb07PW4DD3ghaevmEXbdZooSfRpf63c8qbBq5h93lx9frhgK_HMc4ADasG0SDNcTWgnRhOALYWYZffSuIdan3ItV2ZEzUECMqmogpBCMzgsaeo_P3ZkRNLHVFFk3gRUnyVx7Q6hKNmGRq32ADl0yujfNUL-dp1eGwgiYaYYYXWdjbbFiggFn1QnD-U9dHPEc5BErddrB4xvp4wjWXKwIcOaqONjlb47YbVX3kongJYtOrs0RsQbiQFttcO8LgrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
اسپی:
انتقالم به مادرید خیلی یهویی اتفاق افتاد و همه چیز خیلی سریع انجام شد، رویایی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102448" target="_blank">📅 19:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102444">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R6ztVrawqVPtPgPnP9Fsxmghua4QZB_Jb5RjPppEDJxsgB3ndTDzT1roueLrh3nAed5GlH9lYVjxGhfMCPpfL5fkV4R9-hVfjWIZbI1i7am1-CQZ4421jBJtdfnK1lWXD-5AmpL_Dv9nRrjaSYMx_beb2erz6Wghxpd_bbiEZrmp_6h0Gir35k6dWxQnp4X7a5zI8Gs01e0JXeIkXQXXh1anTU0zGtKfM_D-cl-Zw0x1_POn5FzEgE9zw4kiMf2IA9iU64vyNER4hT_heo02c__1HBWdv703zxZ0DnCG_3p5K-6K9_S4I5riqBEI-4n8s9l9xmkiM1aFOPidSuBB6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TiiAbAVTPXc6OYvx9jK57lWqlW0WYyCIDkeiCAb3CWLRhlsDCeXXh4zauEtJ5B740CPyeCfKma1X5RvrKIwbqWu5PVpPXDjE1ZLVirn2gtDCmqWbLnTSj22g-fMK2h27FW4U81vQEE72UHZKNLB6Zia0opezNrRTc3Y6S3ujn8K2-Pg34bHpUuvYBoLOZ5pVgS72l8gfWIms3W19fgTkFxg_Ex1tZTa4wG_ZmR3qvIG1Jd3Sl643Cv5f3Shu69hRRgM870192sZfRy7AVtwiYo8OT-6bDM_09m4yFvy6_LkgY5rjOE01TzM5PKOOBNX3Wpn7icRqqaUOXsBWjp212Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u1Z33CdOAn20Ahv4NTReUAURZq8vIaJosLAjU8akoQErQZBPaKNWQQQlLyyJ1vAJFzjTORCmJ5bLyL5a9KhHM9lMSYHrgz85Xb86p_jrji9wWkssj_rHJpbE_x4MuMy_ZrYkKbfEuoWmq3d-yT-mnkRtz65S-QFMre8Ykduna3AlITppKS-WQ8H-M1zcE4FpGx9_-Es9CJKwHwUqHk07e7Dbc4KG8XGYBM16X9MsAl1aIV9CNjkEUjDUKF3y4JBDxxVh0IlkM3k0jeqlw2FL44t01vlqGTsYD849j1nTBgHiseaQYNIMEHKy5jWbI9PWNpGBrHQt7ttm65hnUkpaQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y5XJjcRte4T84H8NRzsYIafSCfCz60dhxqLNMIhTr1TES3grBqIgr-t3Rg5XOHr0luuL9NGIiV0i9vJz3HkhyeOyZa3Lys-k8q4wOYJsckWo-BkmT_EBX_bhUlw1xszpCHaxk3h_AdFSvSRs1_4I7QMMayxANwPQmHBsZcV-TjnRBKUJ6NDYoJ-XRrDymaGyGwUEnk7tp7bRNC7i_xx-OAsZUOOFTbX8eFsQIVxffY6w9Ij-Qoth_ibLimk3W3M_-NbIInXz2GlnaJOy9m9uvmMHjP_eNzF_PiYd5eki9KfPVT1FCuUT9g2WsQ1lPiNDSiFYay7VndNFNwcx_hVw5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
عشق و حال لامین یامال با دوست دخترش اینس گارسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102444" target="_blank">📅 19:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102443">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BY1OCs1HB2Ef0H7YafDF3od_Rlp8WI3ij0HJdY4tOpq5Sl6Opbj0JVhVzJjZvda9Lq1hk5HNHMS3ipfkr3LfwYEmrQOkrbDoJQZU33-4ej7Wr5p4CQA2EO55CBZ4R_ByiPhz2rNzpmMDZbJ6TrFEDffxWiBqSc4VzYjQBe61kQczf6cs2xh_BU15rMmxGcS8DK7KkLDXOJN7ewY8qOjQQRPImARJjc19FR-xk5WZYKh0epUf3DjFvGoQ2el1ByPlkFor72vVReFIWyKdhfMERwXTicdmQIWFyBcQ2eRzW8Jt07baCWqhndi4-4hzgGF2kAHPd-kT57u6VADF6yR9mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی دوستانه مقابل فولاد</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102443" target="_blank">📅 19:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102442">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6Ee2AcHz9Al6NZKGsJ1xBgIMUPq6SVpZME9_hSJ7qtqQUEvvW49zzFJ1ewrFSaeWmpNF2KBh6mhCb1nIYWtKQqLQLaGzPTzeRwuq8OfUOViq7DAq11urFLhscPyQbHQxOq03Wgt5PC6WYQPbrirasgt1junFYqQcfQ-KTcK0cYAncm-ORxgINprhGHaHtQ4Y73bXvPvnUhD5rMkn29bJ7WlTGW_W9mZt2RMhthudJzvj_YNM5wW8venzl6CAcmHo7iBVt7pX-yFUqh0wHik5Iqf1sRSQ-GnE87dbqI6InPgY1axjZozUDfaMptAB_NpZoqZvBh56CpF5JmVp82Lxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فوووووری محرومیت دوپینگ میخائیلو مودریک لغو شد و او به زودی به اردوی چلسی در هنگ کنگ ملحق میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102442" target="_blank">📅 18:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102440">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ujwtCzxTFO_QwoXlFvD9Rw9HvtzcgXEj4Z0j0Xu8k4cJYsbpl7jhglbISA-8FKIjKSTAUZzCVmTqOUryd9ru6A11owKiHIcfThbV_HMQmgJ_8qY4zEDq8UuV3oXqqmal4IcTaqz8aQaO2LZ2lt5QWmPZUQGMvwh7vE_GGEfvUHRsnnQFOFiC12UflZAclZ617mJbNSz3gn1EAogbkXhy3BJ1vgAoXXOob5DrivtJYZC8mnAVpu9s5huL2zEQ6wLkqBBh1ReU1GEEfzzU51KVrhstE4EoFNpPxmaYc8wGW-z1td3ThLkA1h1Xrs9X1QdE5NfIWV0ByLE7YggPkmU0sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AwcAMXnedoMUDQRuh2PhDJq56epm9ymi7-lTKoNX6IhoTX5foTgvXfJjvWYxNHx1qhxyefbMxTqsMlqN29onWKpYLFvdb3x9rqV36EOKnNvQP35zYdFjj-mAZG9tqUUn080hNFoalg7NLExCma1nNZFgxaHICw_gGA6gTfgZlcY11bW2D7ics96rG3JsjE_cUOZ5dcCKithY05PWEFwL8Og32XF8TtyAI1_vHI7DA6FjJddRfmMmCTu3qExnEyDHXXHkP5hOP_Efq-JUdjAE6ZZ-jV1Eke1-TVn0jCYtPwryI_aPot92V2N0jpZOLTq9nocTCL1kaIk226aCZM35Tw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیر شدیم و خودمون خبر نداریم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102440" target="_blank">📅 18:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102439">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5d65b7222.mp4?token=NL_bosH61kRC2OliQOKGXbnz_xk0GVXwl9yJ9NrbBPlhsmBQmC-hItNhSEYs2tuEbzADxJ1uBF12f0Ou7qJ2yjglFsKD64XkqBRABV6jgaY88yh8F_myjzaj2deIC9SoHp_qqT6eMvXNHXViVA-4pEA4EPaP300M5ypiykZVAkgxAuCkADlmWFRy9sQadwi0hNPIrpGTDCywg1p5YPjl8rdw3WAgauf1u7dj7MpR-tvaw74Zf8MrDrW0plLXtAPEupRDGdCtN1NqBvpGsXT3kakoiywEUKRq-KXFhH6FSxEieuUZhPJqLm8mxfeeXxk7OvzrGn__xn3nVPMLX1wyPkqRLN01Fk0W4VZZfxdkej4GKkCQzcU1UX9q7L4MG0lb26yOcNFxBNHfjxAuwbJnrgHDUiTnYkmaXkHURg_aul9AvfmeFoYMD6MJyVUBqkDwP_NRBg4faBWKFZuhJhe_PmzSDekjaqd3pGHC_ytlReNr9USNGr4l1BKIyAC5FH06R6piwSUZ2QwLZyT5cKIyh_XakGDdopxn9JaNdTIuGmzqeyDK7Tr1wDV9G-iEsyJsBuZMd5g2p8gP5aBksYv_UU0jPEHM78kXNday8CG07jMuYJa7oWVLdhm8UqW93f1QWpsjeUZmc_59ozy07GG2rg65WxY9LJMV4dDwaieA4Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5d65b7222.mp4?token=NL_bosH61kRC2OliQOKGXbnz_xk0GVXwl9yJ9NrbBPlhsmBQmC-hItNhSEYs2tuEbzADxJ1uBF12f0Ou7qJ2yjglFsKD64XkqBRABV6jgaY88yh8F_myjzaj2deIC9SoHp_qqT6eMvXNHXViVA-4pEA4EPaP300M5ypiykZVAkgxAuCkADlmWFRy9sQadwi0hNPIrpGTDCywg1p5YPjl8rdw3WAgauf1u7dj7MpR-tvaw74Zf8MrDrW0plLXtAPEupRDGdCtN1NqBvpGsXT3kakoiywEUKRq-KXFhH6FSxEieuUZhPJqLm8mxfeeXxk7OvzrGn__xn3nVPMLX1wyPkqRLN01Fk0W4VZZfxdkej4GKkCQzcU1UX9q7L4MG0lb26yOcNFxBNHfjxAuwbJnrgHDUiTnYkmaXkHURg_aul9AvfmeFoYMD6MJyVUBqkDwP_NRBg4faBWKFZuhJhe_PmzSDekjaqd3pGHC_ytlReNr9USNGr4l1BKIyAC5FH06R6piwSUZ2QwLZyT5cKIyh_XakGDdopxn9JaNdTIuGmzqeyDK7Tr1wDV9G-iEsyJsBuZMd5g2p8gP5aBksYv_UU0jPEHM78kXNday8CG07jMuYJa7oWVLdhm8UqW93f1QWpsjeUZmc_59ozy07GG2rg65WxY9LJMV4dDwaieA4Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چند تا از شوت های کارلوس رو ببینید، زمانی که فوتبال تا این حد راجب کسب و کار و پول نبود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102439" target="_blank">📅 18:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102438">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d5590fc67.mp4?token=pogqyBTbUw3rCeXfIaRlTVwiGiW11E1Du6G_LS5RGRDJQIs-cgyjdRqmzlqFi8LIoPZ7BWZwXQyPas0mTky7Pagvp3ClUkuZNdm_nwKvGIojs8IWLnrWiAJSMaO9SIoBKjaPi8wa5XCRgqP6ZgkJcXPvFKlWoZqwe5sYxQ-HciJ7P6Iqo0RpZFNeIgjYUaeNDJS2RxkkWAFHogUYnc_abD1zy6549Cbe4m7HE8E76EAKJMdBopUoimzc0tY3QQlAknwgIEFRLB1juQdAuqhrM-bRp5535DlrZxg-8FPABU6f10tCrHILibF3ULBju2XzvQ7Qx1BfqX5CNk75c84C7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d5590fc67.mp4?token=pogqyBTbUw3rCeXfIaRlTVwiGiW11E1Du6G_LS5RGRDJQIs-cgyjdRqmzlqFi8LIoPZ7BWZwXQyPas0mTky7Pagvp3ClUkuZNdm_nwKvGIojs8IWLnrWiAJSMaO9SIoBKjaPi8wa5XCRgqP6ZgkJcXPvFKlWoZqwe5sYxQ-HciJ7P6Iqo0RpZFNeIgjYUaeNDJS2RxkkWAFHogUYnc_abD1zy6549Cbe4m7HE8E76EAKJMdBopUoimzc0tY3QQlAknwgIEFRLB1juQdAuqhrM-bRp5535DlrZxg-8FPABU6f10tCrHILibF3ULBju2XzvQ7Qx1BfqX5CNk75c84C7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی‌از وینیسیوس‌جونیور در سن ۱۶ سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102438" target="_blank">📅 18:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102436">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hrFTregZig5-R0e5_jtB4gY0UKSDsUVjg5DQxHD7mz71i3cvh_QO76hz6ulb2ZPfIcFYX5x3yde542x8ANro5dsAYgRBaNEnkr0G2yTNS3poBLGV4ej3DseeC_rNUn10pj5OQh7UEIRc3Sjm-RwxELyM0fQIGKUiLGU0IhfJOKdzYVthJzyzIk7eJ7Qqxbx78-Hca4rLprliEhnO2yntkcbTUtm-CybGAa_xawOX07bUxu2wEL5x0a8htPWeEl0DHs2pzG3Nu-q-x1bGeG10xmAgR1QFOdb0OmzjAEn5N1clT6wRfOflXECOZTdGqgQ-YqRRm3RUnmg9usZrWcgI3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gJyZpU9C94ScixBF6tWWfuXKiWC75zz0MD-EygPCF0RIcpAR9ciQoztvxD_hFATFrH0vo1rMmJdCTZnNQ2CB_-NT62TvpMIAqobqB6QwVzaqW7nYp7U2ikqxwAUPDjR3lSFRr4zGhRuleenkPQJPv1UArKctkgAVkJDEiHCsR-9HGcIDT3WTnCB5tKHsA9Jjpe1ahR-1fPVJn5MpFBWfzQxTKgAegcJiObrhGdvuZ_FtlpyWLkS25ajrKLR38oI6anhzccQPldoAz2qLZs_o0xo-kMfl1HNRbK-RDPDUQgpJ-S-CSnMYNknAQ9a0tRmfZivu5mCNcnl5qfGtDKXQRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
فوری، محرومیت سنگین چلسی:
🗣
باشگاه چلسی به مبلغ 10 میلیون پوند جریمه شد.
🗣
همچنین، به طور تعلیقی از ثبت بازیکن جدید در دو دوره نقل و انتقال محروم خواهد شد. به این معنی که اگر بار دیگر خطایی انجام دهد این بار پنجره قطعی بسته خواهد شد.
🗣
در ابتدا 6 امتیاز از مجموع امتیازات چلسی در فصل آینده کسر شد، اما باشگاه درخواست تجدیدنظر داد و این رأی باطل شد.
🗣
این رای بخاطر تخلفات نقل و انتقالاتی در دوره آبراموویچ مالک قبلی باشگاه صادر شده است. مالکان جدید این باشگاه خود این تخلفات را گزارش دادند که باعث تخفیف در حکم نهایی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102436" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102435">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68f9e38a71.mp4?token=JbBlOe56VZrWdjuQDbg7y4Y8ucT95k_yA2wR1fQAELI594XyQr0DSBPgq9Ih0IhgaR54qj2siwc8s1jPXfCZjySX2i09axLf02iefJkzjI1ad1D4DsLriXIVrCpmmXg-AubLju-dXVI5Anroz6phh6IfQoBhXIp5Tvawb4ccz8UJ_ptFq-CkkhmEW0rtPSm_klWv5Ak_rpWjWafG4OmzsmIJxrUlCyh5NVyoQ-ikqCIr0k8cKXzT27DCyxTWVlPlYQfiGVHGZ7-vy4J72BikAyTKNGAEr-SWc8SCqYMVXEGbwxuF8I_4tEx6XoxLXv-X4mjqHi4zt5elDHXyDZmv0YU8gIHGMXSDRzcB6g0clia-8hGlmIMlFv8kkbhSRfBiT3VJLlzLD8hU4f78LgUYwh2q9zRj1f1lXgnWRcW1qqyHwXnMcmOA0U_FG3i_sGaiH8C62A7TCYWM9pTCSxO_EvCZrIPDKMB7q2JgIFLijXYkeXOxIJJU8S4cmc3thJFIX11ZD_M1SNXmdG83DjnX63bAtplxRbE2fN5ZJErY3bUWAehTiXRxR7BEVH-d1TdjBm3oNjs6STjwwDjdkkUOMkJfMmm75BnBaF6Gx7-TG7Go5GrTktomjJj2AI8vdu5sF_6quD7JCfbKjncMNNPq76UQ06YFFJftCyUMC8zojdI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68f9e38a71.mp4?token=JbBlOe56VZrWdjuQDbg7y4Y8ucT95k_yA2wR1fQAELI594XyQr0DSBPgq9Ih0IhgaR54qj2siwc8s1jPXfCZjySX2i09axLf02iefJkzjI1ad1D4DsLriXIVrCpmmXg-AubLju-dXVI5Anroz6phh6IfQoBhXIp5Tvawb4ccz8UJ_ptFq-CkkhmEW0rtPSm_klWv5Ak_rpWjWafG4OmzsmIJxrUlCyh5NVyoQ-ikqCIr0k8cKXzT27DCyxTWVlPlYQfiGVHGZ7-vy4J72BikAyTKNGAEr-SWc8SCqYMVXEGbwxuF8I_4tEx6XoxLXv-X4mjqHi4zt5elDHXyDZmv0YU8gIHGMXSDRzcB6g0clia-8hGlmIMlFv8kkbhSRfBiT3VJLlzLD8hU4f78LgUYwh2q9zRj1f1lXgnWRcW1qqyHwXnMcmOA0U_FG3i_sGaiH8C62A7TCYWM9pTCSxO_EvCZrIPDKMB7q2JgIFLijXYkeXOxIJJU8S4cmc3thJFIX11ZD_M1SNXmdG83DjnX63bAtplxRbE2fN5ZJErY3bUWAehTiXRxR7BEVH-d1TdjBm3oNjs6STjwwDjdkkUOMkJfMmm75BnBaF6Gx7-TG7Go5GrTktomjJj2AI8vdu5sF_6quD7JCfbKjncMNNPq76UQ06YFFJftCyUMC8zojdI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
درگیری کورتیس‌جونز، سیمیکاس و سوبوسلای بر سر بازوبند کاپیتانی لیورپول در بازی دوستانه اخیر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102435" target="_blank">📅 17:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102433">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RNEhqqNf6A1_vhdB2DDWY2yVM_GGW9hr0CcMC9n51jSAsMamtw2w15LpGK0KxocPUFzv3MMxgFV5IkwIXn71ZplpBEo-KwYEV3K5YqwEo-epbSaqnbo--xzQ8LvBKdshKEvGxvuECm-QldVokFFKYQETYmKfLcb70opuxGfja-kzp6SOdFzqfvftN_nZl1eBYdedixuvgcZaA32G8M2KojJBPt5fBrN39mOxX1_kJctqqF8Nfw7rRUv99BrUCN4BhbKkmzd2EIjCiIuAs2ik6JJ_HHref7XgA-_ROcDnckSr_YEt9PC-9Hhyt-Wy6gal2UUDSmLckbSlnv9OFao9-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LeUvXR58uywhPZ7Id9t6lSs-d_EseFCycR1XPBgnysDXkqhm41X3AxShoTwxeveX0lVnscfN6p1shRD7LjCjixL-iL9CSzPNqu5mo1sdqmBr9Zc-fskYIWZ_dqdST4FgODVwYtAp4cmJRDxMbz65OiEH53QDMfArHfas7il5Wj-YExurE76TYS359luLgimbzZhvE07CIaGXBy3T5M3WlCeVtTSEN9Qe7uMdft_kJRmwPF2kRvGpLZT9dDhW0kQ-f3_nX7r6DQbv1RRDO8b3x7wDCNotf72asaSc0ukq8rEBXQtzq6ibcXCe1DlBsyg6NZFHHko29kR8o6gYqLj02Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
ال اسپانیول:
پرتغال و اسپانیا اعلام کردن اگه اینفانتینو پیشنهاد خصوصی سازی جام جهانی رو پس نگیره از میزبانی جام جهانی 2030 کناره گیری خواهند کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102433" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102432">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96363baca3.mp4?token=vMsU_AOlraaiMkZ4rMvrSeojLw206PdaQ0eVT1_1_peBX46tUz2HRkz1pa0G1YZV1nenD_DU-G7rpeyhEM7mc26MLzaaOmo5nG15pPir-x2wGQQ53_wBO7cwXcsXcTZw1quh454PaJiB5tKIkLXqmQpxPcA4xY7XysMK9eJ6l5tyNI4kVv5er-iZIlpcjzrmYtffM0_005G8nQj3p_0ckyM2YDqsE9tQglufnWRdL4ODIlDGMJn5CBf4EkIRYMmkKEJKyTdw9qA0Re-CYW2VL3DDS9JgDRPx_QTp5LyAmPJl0Ov_hvt3soiKLtwiXCCXBWKdmv6t3HyN6dt4hpOZiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96363baca3.mp4?token=vMsU_AOlraaiMkZ4rMvrSeojLw206PdaQ0eVT1_1_peBX46tUz2HRkz1pa0G1YZV1nenD_DU-G7rpeyhEM7mc26MLzaaOmo5nG15pPir-x2wGQQ53_wBO7cwXcsXcTZw1quh454PaJiB5tKIkLXqmQpxPcA4xY7XysMK9eJ6l5tyNI4kVv5er-iZIlpcjzrmYtffM0_005G8nQj3p_0ckyM2YDqsE9tQglufnWRdL4ODIlDGMJn5CBf4EkIRYMmkKEJKyTdw9qA0Re-CYW2VL3DDS9JgDRPx_QTp5LyAmPJl0Ov_hvt3soiKLtwiXCCXBWKdmv6t3HyN6dt4hpOZiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
مرزها برای میزبانی از زائران اربعین آماده‌تر از همیشه
🔹
در آستانه اربعین حسینی، پروژه‌های عمرانی و زیرساختی در پایانه‌های مرزی کشور با هدف تسهیل تردد زائران اجرا شده است.
🔹
در مهران ظرفیت خدمات و زیرساخت‌های برق، آب و روشنایی تقویت شده، در شلمچه بازسازی و نوسازی بخش‌های مختلف پایانه انجام گرفته، چذابه با توسعه امکانات رفاهی تجهیز شده، باشماق به سامانه‌های هوشمند مدیریت تردد مجهز شده، تمرچین توسعه زیرساخت‌های خدماتی و ساماندهی محوطه را پشت سر گذاشته و در خسروی نیز سالن‌های مسافری، پارکینگ‌ها و فضاهای خدمت‌رسانی توسعه یافته‌اند.
🔹
همه این اقدامات با یک هدف انجام شده است؛ سفری ایمن‌تر، روان‌تر و آرام‌تر برای زائران اربعین
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102432" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102431">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">💥
🧐
رونالدو، پسرش و جورجینا درحال عشق و حال در گرمای تابستونی اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102431" target="_blank">📅 17:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102430">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e703311f9.mp4?token=fUtFUrxVg2n8BHI4IKr_5gEKJ7-iBKgLLaX5W-MEzgteFbkSkE2MZdOkJgkPygfAVYAtgzO2B0HTmyxcDzf3gw-EbuRv160MsqtiFvaKh7Twt3hdIvqB6JzZCjK3h1tFpMlqiXfm7OWHMMy4Nu-drQD7DHNQpbKC2PQUz_uyf9uhuCfGvH3ML6mYaju3kMqeIg9FnfWqw9PI6G38mNuUrhlPpfEqZf165GLC86Q6KzqthbkKR2a6W6seraERT-plmBDzJRjGGG-1nsA_5Pdzrqor4RC3l_zHRp_jz0BG932tBTx9YBc2faniIvbnmDBPXj-vB1F3ERlWTtW3nUUwsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e703311f9.mp4?token=fUtFUrxVg2n8BHI4IKr_5gEKJ7-iBKgLLaX5W-MEzgteFbkSkE2MZdOkJgkPygfAVYAtgzO2B0HTmyxcDzf3gw-EbuRv160MsqtiFvaKh7Twt3hdIvqB6JzZCjK3h1tFpMlqiXfm7OWHMMy4Nu-drQD7DHNQpbKC2PQUz_uyf9uhuCfGvH3ML6mYaju3kMqeIg9FnfWqw9PI6G38mNuUrhlPpfEqZf165GLC86Q6KzqthbkKR2a6W6seraERT-plmBDzJRjGGG-1nsA_5Pdzrqor4RC3l_zHRp_jz0BG932tBTx9YBc2faniIvbnmDBPXj-vB1F3ERlWTtW3nUUwsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
🎙
تمجید جالب کاسمیرو از لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102430" target="_blank">📅 17:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102429">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b472a6619e.mp4?token=ocC96I5aY8gsnqiUO0KQCJ0USWqrMvIgZcpN0X9k_Bp01LVentvUIPlYPRipX6FakF_DadaNwyKgfAeaSCF3MrwDdiE9rkYcXJpKqeylmBNDvHs9YhKLN6vxSPJNC9a9bpZxczJxG1IAng5TST2xUESJu6_F0x4m8fCvfhGyjojnfzaEeuqCY9iq_ts7xkFzKbSiGYx_7gSTLGEKLwnsnjjYpmqIPEmxp_2w4vklmMmUgFzxTnxhnGhOVlEl0e6QaMWwPE9FcHacNbco8i0Ix71XZ2RA733sqBtWTDwMF1MKwhSfSSQEVgapNzICU47xd1dg0eF2E98mYVJkIRL6bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b472a6619e.mp4?token=ocC96I5aY8gsnqiUO0KQCJ0USWqrMvIgZcpN0X9k_Bp01LVentvUIPlYPRipX6FakF_DadaNwyKgfAeaSCF3MrwDdiE9rkYcXJpKqeylmBNDvHs9YhKLN6vxSPJNC9a9bpZxczJxG1IAng5TST2xUESJu6_F0x4m8fCvfhGyjojnfzaEeuqCY9iq_ts7xkFzKbSiGYx_7gSTLGEKLwnsnjjYpmqIPEmxp_2w4vklmMmUgFzxTnxhnGhOVlEl0e6QaMWwPE9FcHacNbco8i0Ix71XZ2RA733sqBtWTDwMF1MKwhSfSSQEVgapNzICU47xd1dg0eF2E98mYVJkIRL6bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
یادی‌کنیم از بازی تاریخی ایران و قطر با گزارش جذاب عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102429" target="_blank">📅 16:40 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
