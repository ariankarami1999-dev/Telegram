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
<img src="https://cdn5.telesco.pe/file/pBv0syoDFFqmfMJotoNNyI356DIdMan_OvcVcOMlDTk2cDZcpx2lHRNfEFKQNP0yXk9S27xfAr9pOHonPBHpsWw2yYDMkL17-ZAXqSjAw0MpaZ6n9FsOm4RwzBSF0iUZJ0LtJtkNGjoFmTJHNxz3Mz20g1BEj3znowUGVArvrmWI66uEE7vrEQ0-Z5q2hWwSKKLqPgvIeU3YB0Xlcey5WgPaoM7G1URrbvqtpNrmqpzcbDLuwM3Yi11-N_jITl4J3wLBQhE8xubZFTROVvic-vWUwNCyU2uEMe1fOS6c0HQNBV8_aca7a5Xn_IFIGDA1ykIvqC46JTKhetiaUdf9yA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 439K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-06 17:05:27</div>
<hr>

<div class="tg-post" id="msg-104915">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ef920f58a.mp4?token=fLjKyT7ydhyD0WIuOnMduyOd8rXdPaRc3vEPh6ZEdKUppV0tef-teS99feZIwokMGkpOhsyZl8sj8-DuCJKc71gNzpk0ZPLI9O9ZsUV4S7HTuoKXyJc8HuaNZ-rqY-AOlaQdzTu46fvUEKhrKgKxNtPjlVMGLval9mcdJyTTcczjg6NBDCqOiqS0xCnLgJzFgnp8gcKK6d0iKcWtWwyawyB956elI97c7Df459xnasUr682QS65TVtkmM-LCYuXDWb8Mr1rrtJrp7d1jbPmPdfGpmrUDmW6Zzv7RV6fMpqRtSaWVvKkVqTbWIQlIFYgIowPWb1Cc2YWCF4GsaaPiBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ef920f58a.mp4?token=fLjKyT7ydhyD0WIuOnMduyOd8rXdPaRc3vEPh6ZEdKUppV0tef-teS99feZIwokMGkpOhsyZl8sj8-DuCJKc71gNzpk0ZPLI9O9ZsUV4S7HTuoKXyJc8HuaNZ-rqY-AOlaQdzTu46fvUEKhrKgKxNtPjlVMGLval9mcdJyTTcczjg6NBDCqOiqS0xCnLgJzFgnp8gcKK6d0iKcWtWwyawyB956elI97c7Df459xnasUr682QS65TVtkmM-LCYuXDWb8Mr1rrtJrp7d1jbPmPdfGpmrUDmW6Zzv7RV6fMpqRtSaWVvKkVqTbWIQlIFYgIowPWb1Cc2YWCF4GsaaPiBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری شبکه ورزش : دوست دارم عادل برگرده !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/Futball180TV/104915" target="_blank">📅 16:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104914">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTbFn2aCVKtZ5PAqyP2Oc3zW39HEnFI7oxBqPGaLm77SCHwJjrtJDYcAKzszsdnTriWcTMbtHRlkyke-gge10qo-2ATfNtoPJrMr49AW0VmDCJ6mBPxOpPRr68s7YlqbLnRSJ0mZcuNa4rVtf0dZdel6SFq-HS9Ib8tJjbowMth4OZ2VrRl50RZnymyOylBbsKT1nqsrlpNA212_SfgmCTdfdwUk8qFhyZV7w0OMVTdexaJTKQQQIacX53yvd9I4XxTSmSZdElyfZZ4t8zK3lWhUd4W8w58PQ85x3dUq5S2n1meE4rT8CZ-x82NXT8DUDfszYQ5bt-KlY1xLG1VXcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
پیام هوادارای اتلتیکو در ورزشگاه متروپولیتانو:
«هر جا می‌خواهی برو، اما همین حالا برو.»
«اتلتیکو از غرور تو بزرگ‌تره، خبل مارین.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/Futball180TV/104914" target="_blank">📅 16:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104913">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04262aed7d.mp4?token=GM4Kz-f9tczAtsi6PamcUjZfVYuGjAveZnYLxKY4gOWoY9J-2yhnfEku1QqdjwuUTzVuHYuXziA_HNTeeYMaBrM8TltGUU9iBdNXmd0dookJRMuanVwBeA8JtDV4mTDtrXCxKW8OZ9hpB_eOc9G065V1CXSx2FBqbKf7fhGdQucszH_E83uZKRnKvffripSgn_XEw2ER_SCc8SluJein9hQy2tH5VKFqA2Jk6mi51HT7lrvKbdlMJmO3aQtn0DpsKf1bPRo2FKOCjenfQmJQYiDPs1Ok2oZIxm3lQ7dbfwYYgp3T3BY4gyMjOLOp9z2gl3k7SqZTpyohClgCPdoE6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04262aed7d.mp4?token=GM4Kz-f9tczAtsi6PamcUjZfVYuGjAveZnYLxKY4gOWoY9J-2yhnfEku1QqdjwuUTzVuHYuXziA_HNTeeYMaBrM8TltGUU9iBdNXmd0dookJRMuanVwBeA8JtDV4mTDtrXCxKW8OZ9hpB_eOc9G065V1CXSx2FBqbKf7fhGdQucszH_E83uZKRnKvffripSgn_XEw2ER_SCc8SluJein9hQy2tH5VKFqA2Jk6mi51HT7lrvKbdlMJmO3aQtn0DpsKf1bPRo2FKOCjenfQmJQYiDPs1Ok2oZIxm3lQ7dbfwYYgp3T3BY4gyMjOLOp9z2gl3k7SqZTpyohClgCPdoE6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
#تکمیلی؛ تراکتور تبریز هم اعلام کرده که امیرحسین حسین‌زاده را به هیچ عنوان به اردوی تیم‌ملی امید نخواهد فرستاد.
‼️
🇮🇷
از طرفی تارتار هم چند روز پیش مخالفت خودشو با حضور سه بازیکن پرسپولیس در اردوی تیم‌امید اعلام کرده.
❌
حالا مشخص نیست که زور و تهدید فدراسیون…</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/Futball180TV/104913" target="_blank">📅 16:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104912">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa7be285b4.mp4?token=mhDU1dv3u9TrhWHoTHm3t9xu3y5EeWZp5isjy23PsSAEztzwa_nOXQZwMc2Qc595atkfVxIzQ4eaxhexbrJPY_F1w7HGw52FG4oL9z_F0NbQxsSqCquJa3c1VovbETHF4G6iIw82EUTje-6DfygPdmpoNvoivrOrgtds4Sr0ZQaklW5X9xzGs2RsP2IkW91-3CnlFzn58g3z4_5-KA8b0TDmXx1IXb2h08q7em7R32QIUp_vkZAih0tmhNTfwWSjVF6VXAQg6zaSR8-kMzcCp65SBkeJprIuNNLv_38xLyxVvJhoEkLnlaQEIZCvCYoLjGUKPhgqSWyrhb6F48kGzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa7be285b4.mp4?token=mhDU1dv3u9TrhWHoTHm3t9xu3y5EeWZp5isjy23PsSAEztzwa_nOXQZwMc2Qc595atkfVxIzQ4eaxhexbrJPY_F1w7HGw52FG4oL9z_F0NbQxsSqCquJa3c1VovbETHF4G6iIw82EUTje-6DfygPdmpoNvoivrOrgtds4Sr0ZQaklW5X9xzGs2RsP2IkW91-3CnlFzn58g3z4_5-KA8b0TDmXx1IXb2h08q7em7R32QIUp_vkZAih0tmhNTfwWSjVF6VXAQg6zaSR8-kMzcCp65SBkeJprIuNNLv_38xLyxVvJhoEkLnlaQEIZCvCYoLjGUKPhgqSWyrhb6F48kGzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
تارتار: زمین چمن یادگار امام تبریز واقعا استاندارد نبود و کار را سخت کرده بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/Futball180TV/104912" target="_blank">📅 16:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104911">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5141cf449f.mp4?token=usnJRJzaC6rMwTD6hSy3bzbKrT--teiTb-oYDR8Xl7U1PV5ghA9z5qAlYPHwdaoS6WXQhkilgxIyIP_RFhWBLXmLjf6w4y3DY6UBsTgfr87wvcfzE9CO65S8qZFY4_pran0SyIjJQ4-M6ki23t_eBreuXJoXd49RnbXgYMUTm8vc26mz9QaRiH0sEbWRfVQ-OtMF9qnfW3oBKOyNEzGmUmE4inYt-0tXgoCEg7ZEyVEvHepz7Tv1ly3kYZs4JWPirSUP2GJtyYjKXi4AkIcwjytPNhtoBHpQeWpgVyHshGTS_5qVjSBVzVUXBTAcchM1FSmaySBmjhs-MsyrPIC2DWE9CzO9qOpSdLcfZflVBqL5qel7Nmh-P3b9hPXtJEfiMu5wDbm06c3EkDrTnsaWlPycxX-VRiCYSyIH5X9Zc454OYV2yVRycPPO1CRvbNaPvKFjpII0m3YGZCmdrR2z-aQNS-Fht2lYUx3-dbac_ozQg-odb08f4lyDcvtewbLcZfbaB0nk885rDwEgnL3tAXwsI75rtBmY0-KvrSaGQR5DDTd3Y0wriTppUBdJSWM7jaylgQFeJlLeKkWPwR1T6rDQy8ihZB_Z09FS61TGAiWoI2Y9QZgkv0YyET66uhmWIsGQOfsvljODqoZNX7zqtX7AXQVH60wW8puBT6nern0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5141cf449f.mp4?token=usnJRJzaC6rMwTD6hSy3bzbKrT--teiTb-oYDR8Xl7U1PV5ghA9z5qAlYPHwdaoS6WXQhkilgxIyIP_RFhWBLXmLjf6w4y3DY6UBsTgfr87wvcfzE9CO65S8qZFY4_pran0SyIjJQ4-M6ki23t_eBreuXJoXd49RnbXgYMUTm8vc26mz9QaRiH0sEbWRfVQ-OtMF9qnfW3oBKOyNEzGmUmE4inYt-0tXgoCEg7ZEyVEvHepz7Tv1ly3kYZs4JWPirSUP2GJtyYjKXi4AkIcwjytPNhtoBHpQeWpgVyHshGTS_5qVjSBVzVUXBTAcchM1FSmaySBmjhs-MsyrPIC2DWE9CzO9qOpSdLcfZflVBqL5qel7Nmh-P3b9hPXtJEfiMu5wDbm06c3EkDrTnsaWlPycxX-VRiCYSyIH5X9Zc454OYV2yVRycPPO1CRvbNaPvKFjpII0m3YGZCmdrR2z-aQNS-Fht2lYUx3-dbac_ozQg-odb08f4lyDcvtewbLcZfbaB0nk885rDwEgnL3tAXwsI75rtBmY0-KvrSaGQR5DDTd3Y0wriTppUBdJSWM7jaylgQFeJlLeKkWPwR1T6rDQy8ihZB_Z09FS61TGAiWoI2Y9QZgkv0YyET66uhmWIsGQOfsvljODqoZNX7zqtX7AXQVH60wW8puBT6nern0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
تارتار سرمربی پرسپولیس: ارونوف یکی از بازیکنان خوب تیم ماست اما دیر به تمرینات اضافه شده است
.
بحث مصدومیت ارونوف جدی نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/Futball180TV/104911" target="_blank">📅 16:21 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104910">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a61739d98.mp4?token=V5KIyZdBDrK0yR-Vmax8dawe5Ra_5SNN4wlWBJ-WM1ECvakTfP711G69uPe8mSXDEZmLPnWayKkXTtq285FFzDaVdVdAc_7ldkvmeryy01-QbAFjWDN79etqQxyrucRDll9cLnQSJgCgM4OD7rupDyaLn-a0Incp4LVxF89jzQ0hFkldwcGNExSRRuzf16PmOVfUVY0yNXm2RpFxQb7SHNxStMQyssA4QUm9mzkqxjXS1AxDJ6PBh0vd9Ba_Er-gNpVemVclTSuVFLCwL3Q2gydmH4kfF7sK6YTXSV3SbXmNq7XPWi6YA2jyA_4j2zNzYhPHv70Qgc0EQ71MwIjpmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a61739d98.mp4?token=V5KIyZdBDrK0yR-Vmax8dawe5Ra_5SNN4wlWBJ-WM1ECvakTfP711G69uPe8mSXDEZmLPnWayKkXTtq285FFzDaVdVdAc_7ldkvmeryy01-QbAFjWDN79etqQxyrucRDll9cLnQSJgCgM4OD7rupDyaLn-a0Incp4LVxF89jzQ0hFkldwcGNExSRRuzf16PmOVfUVY0yNXm2RpFxQb7SHNxStMQyssA4QUm9mzkqxjXS1AxDJ6PBh0vd9Ba_Er-gNpVemVclTSuVFLCwL3Q2gydmH4kfF7sK6YTXSV3SbXmNq7XPWi6YA2jyA_4j2zNzYhPHv70Qgc0EQ71MwIjpmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⁉️
داستان پارسال ماتتا امسال هم برای آلوارز تکرار می‌شود؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/Futball180TV/104910" target="_blank">📅 16:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104909">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🙂
🎙
از سری نکات شنیدنی امیرمحمد زند :))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/Futball180TV/104909" target="_blank">📅 15:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104908">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c0c43226f.mp4?token=isoihpUZsFU1hgBRoCLMWh50GYNaWilXTsQX2IzGuxYQfOauOaoq6zRPSqEyKWfAjYoCC_FY8UfKXtvLx9NsMsqH9f6wud1xEXYIW8oppjkLwImMCQk1LQ3QoOnKuAljbh-efdwXkOvu74oYzc5cYw6OJhhSDWTUGt3hip8KgNp0BKGMzCfWFYA_yarzQCL4SwByHnpMxyDV8xGNxAtunKdYd0rVBJ8hLEX3n2rEALDhkaS_HxHTwIGrhe4H20bUCPSqZUvoL5QnJg5p_2Alyx8WIw4zzASlMOdjh6szMbdwf8P6fFp1ZC79x-MLDj3INJU4MQpxdJk9m4tEF6SMcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c0c43226f.mp4?token=isoihpUZsFU1hgBRoCLMWh50GYNaWilXTsQX2IzGuxYQfOauOaoq6zRPSqEyKWfAjYoCC_FY8UfKXtvLx9NsMsqH9f6wud1xEXYIW8oppjkLwImMCQk1LQ3QoOnKuAljbh-efdwXkOvu74oYzc5cYw6OJhhSDWTUGt3hip8KgNp0BKGMzCfWFYA_yarzQCL4SwByHnpMxyDV8xGNxAtunKdYd0rVBJ8hLEX3n2rEALDhkaS_HxHTwIGrhe4H20bUCPSqZUvoL5QnJg5p_2Alyx8WIw4zzASlMOdjh6szMbdwf8P6fFp1ZC79x-MLDj3INJU4MQpxdJk9m4tEF6SMcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
👀
هنر زیبا در ورزش جذاب هندبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/Futball180TV/104908" target="_blank">📅 15:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104907">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🎙
🇮🇷
صحبت‌های شنیدنی نوید استادرحیمی درباره سهراب بختیاری‌زاده و‌ وضعیت‌استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/Futball180TV/104907" target="_blank">📅 14:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104906">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc259d7726.mp4?token=kOCh6yOR72DJjUBclZ-ffCGrB2a5Hdcmu3ECPJ0mdVnUt-g_fPKeKpzXawZjdrGopBR9RIfDiRMykv6wmJFjTGGr7qFwUW869_2Dhyn9AENF5ihjDF3wX_orgu1GVw_6ncMlf97F9xiR3yaVtPASVcAZ4SQnAaGt0cTD197R12LlZEy2wEzh6j06vkyr2J7Jkx3lmpnMTTBDIvv53lMwNnVspuHIRVAe7S49McoLhitQsYttbwxwp0RZiWUVWqEstmgUcjIaXG2O0TAVSlLK7E1hIfvHBDjfHjpsuPQ8JouKTZixGtCOIjswUG1SGRYlMoYZ_B0E4BW543QI4XK_vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc259d7726.mp4?token=kOCh6yOR72DJjUBclZ-ffCGrB2a5Hdcmu3ECPJ0mdVnUt-g_fPKeKpzXawZjdrGopBR9RIfDiRMykv6wmJFjTGGr7qFwUW869_2Dhyn9AENF5ihjDF3wX_orgu1GVw_6ncMlf97F9xiR3yaVtPASVcAZ4SQnAaGt0cTD197R12LlZEy2wEzh6j06vkyr2J7Jkx3lmpnMTTBDIvv53lMwNnVspuHIRVAe7S49McoLhitQsYttbwxwp0RZiWUVWqEstmgUcjIaXG2O0TAVSlLK7E1hIfvHBDjfHjpsuPQ8JouKTZixGtCOIjswUG1SGRYlMoYZ_B0E4BW543QI4XK_vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما فقط این هوادار کوچولو رو ببین
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/104906" target="_blank">📅 14:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104905">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/104905" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/Futball180TV/104905" target="_blank">📅 14:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104904">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCNE8bTX53GTIkSIiWUQ0o83CWZSmNSv_kv4sdSp9apKBq0aCffdxuKGlmQEfxeIGApqlco1rZQWiF60NJ5G_ml3Ktn6u5mLhNYW7Fqgd9OUJdFKzIm1Sx7pfHb9yuYxW15iINaQ2dNvlutJ9EFAfKa_1tb7Xkl0fblVsoafnlG1-QmpD33wa9lrRZKb6hodP3EIgLhYMV6Fcz8A4f8d-07icXAth_pblK-b10xNY8cZPGYuMnWcESO9671w0T26nNulBmMslP1l63Om8i6T5Sy5cu6TuPfdPJIEVJx3H9NqTd8zKSJu3dYz2WISHf1WkA-GYuVITgYUhHwG0HKu9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد جذاب فوتبال ایران را در
TrexBet
پیش بینی کنید!
🦖
استقلال
Vs
فولاد
🦖
جمعه | ساعت ۲۱:۰۰
🦖
ورزشگاه شهدای فولاد خوزستان
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/104904" target="_blank">📅 14:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104901">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/676a532a06.mp4?token=Gwpq0tYMbY5WrzrtAhHUauamt8Vt9_g6uuuT8hzjI8qonuYzJdGcXLQEM1BDfV8NjrPDYw4rw19MXwoChlxfhASniN_PlfYwsPua9_NcF_J277-rAK_tPbTOLzdJ4zibzEMQOXhmRWK0eYbmkBzSpY9WCBWpIUxrsZsSM9EHr1vfr61W30Z4GrgwVpfcxcbVI-d5_8ZpTysbg_UuSYyYl2wvQSlBi-IbPKCZWQiMr-9eSt3_jXsuy3e1uSWDeJ278oz_k3eFV1bNkOooENChZ_HaHJM8FenpWEGpcJqNJEIinIWZLkPe9HrHr3W1s6xlO7j-ETCA9H-E_tfOgmcfbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/676a532a06.mp4?token=Gwpq0tYMbY5WrzrtAhHUauamt8Vt9_g6uuuT8hzjI8qonuYzJdGcXLQEM1BDfV8NjrPDYw4rw19MXwoChlxfhASniN_PlfYwsPua9_NcF_J277-rAK_tPbTOLzdJ4zibzEMQOXhmRWK0eYbmkBzSpY9WCBWpIUxrsZsSM9EHr1vfr61W30Z4GrgwVpfcxcbVI-d5_8ZpTysbg_UuSYyYl2wvQSlBi-IbPKCZWQiMr-9eSt3_jXsuy3e1uSWDeJ278oz_k3eFV1bNkOooENChZ_HaHJM8FenpWEGpcJqNJEIinIWZLkPe9HrHr3W1s6xlO7j-ETCA9H-E_tfOgmcfbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇮🇷
پرورش نسل بعدی بانوان ملوانی
🤩
‌‌‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/104901" target="_blank">📅 14:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104900">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f9954ef8.mp4?token=ZHthn0wg9hXDGRP0lN45sk2WTv1M35X145S0kNlz2CGXAcLaDRGrSe2lBkyRnQlWFchPj0tCc_UeWkbrWLtbreSJEz_rDE2XYk7Hk0v9B08zPH_6CBcri6_w9CJuilfc6BblEJhAinVc56SBiCEclw5Lcrm5_AWCYOK0TXQWl9EY4RWSds9KOL-kmso2RNYPnr_j2zFMQO7-Y8E9_yhLrBKPAZu5JJCLYKJb3u_091mzC4A8vQPL1Cy9vFLQXnwkwgemh7tfjJEvtTb8q-2L35fEt9c44icPOtPNKuBuvU_IibCI7QdXj3-MqhlJlkX_jjtoxaIYyaaFdWd0trqjlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f9954ef8.mp4?token=ZHthn0wg9hXDGRP0lN45sk2WTv1M35X145S0kNlz2CGXAcLaDRGrSe2lBkyRnQlWFchPj0tCc_UeWkbrWLtbreSJEz_rDE2XYk7Hk0v9B08zPH_6CBcri6_w9CJuilfc6BblEJhAinVc56SBiCEclw5Lcrm5_AWCYOK0TXQWl9EY4RWSds9KOL-kmso2RNYPnr_j2zFMQO7-Y8E9_yhLrBKPAZu5JJCLYKJb3u_091mzC4A8vQPL1Cy9vFLQXnwkwgemh7tfjJEvtTb8q-2L35fEt9c44icPOtPNKuBuvU_IibCI7QdXj3-MqhlJlkX_jjtoxaIYyaaFdWd0trqjlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇪🇸
تحلیل جیمی کرگر و گری نویل در مورد شیوه مربیگری ژابی آلونسو و نحوه اخراجش از رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/104900" target="_blank">📅 13:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104899">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuIcSpE_VNudFNk4BOaIWmmRDDIaxm_uJfht6kv-s_O3RxLJphBf8yGZarXjXx3-RHWhBrS_N_x9rn7-xrI1CCDoFz-50Mv3neTs995LwTR_DorJaPTDDUtxOZz8ovLLEOx4nOPSvwFSAFAF6zXRcOrAI5sM_UItH1wZZYLn366n759F0v6IOoF5PesbwPo_Ql7u1QPOmzynEXHqKKekpG4CWJCG2iVnoFs8Rxkry2H0kPpQxnvBjmbKaviDlJ52Kpd3Xfvlel4oUFyJDzftk9_0zWaYxFpN8J8fB3WvakgKiTYV1ktYJS_WsgN4WIdIOIWD1zHPETVvYx5DpIfNjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇫🇷
لیست پاری‌سن‌ژرمن برای دیدار هفته دوم لیگ‌فرانسه با خط خوردن دمبله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/104899" target="_blank">📅 13:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104898">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
🇪🇸
🗞
رومانو: آخرین پیام و شعار آلوارز به خیل‌مارین: یا بارسلونا یا هیچکس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/104898" target="_blank">📅 13:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104897">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_vP1LrHDkOMHgtXfcVTY8ehi0xyxPYlx1vCwk-dPk9Ndi3TVadPWr6SaVI0WwT90V4Gk2BlzbE98ja2n4TqbTEUJSx5mygHoylQxImbpaoqFh3epS2z77cpbdt-84tOiYgqQN_tkxkdNeRjnAaqBEPqdT9J9b_W5A9nRqoDuoUCDmx_MOz32ym2gTv6uuytHs32dJbGroLjK4XXxYEul5wYY3LcMny6T-OJ8JW2GC1SnwvwR1Hvim-FkghPAFgFHr3b_aREXH36dESq6nTL1h2yGnULyQAaEzqwDX1xuqiB3wpu8JSz1M3rTk4arnDtYEYWs9JsinW8NVttXAUMcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗞
✅
رومانو: موراتا به لگانس HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/104897" target="_blank">📅 13:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104896">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b74cb03b6.mp4?token=h41v_STlvc7YovLs05EE6D-5sjgIh0y_IgB9BcOGMhgT9df9vdDgWOCh0gpurfWKJyOVpc6KBu1bxv9IuTUP447zo0zr2DLJ9rTLH7aZr9moThx9pbXZkODuy3kzgx_hSQnFmx6OLeG33UjoZdY4sgREMw3K95OZDRC7x0Ciju4Lt6naFY3W7asNl1E8cbFTcuGLtHQQcVw17C0DCMI7BKW3SdwvPbcrgCekwofSBCPuWqy0uY2TOpF6Co7VjjxwxpalyhtSsIVPe3ChL4M7lBWpQ1aWoJz-f67aq4maPmr3QxkQ-YO9PN7Cd2Pfru9AOglOnztkSmaU5mxB0PL2hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b74cb03b6.mp4?token=h41v_STlvc7YovLs05EE6D-5sjgIh0y_IgB9BcOGMhgT9df9vdDgWOCh0gpurfWKJyOVpc6KBu1bxv9IuTUP447zo0zr2DLJ9rTLH7aZr9moThx9pbXZkODuy3kzgx_hSQnFmx6OLeG33UjoZdY4sgREMw3K95OZDRC7x0Ciju4Lt6naFY3W7asNl1E8cbFTcuGLtHQQcVw17C0DCMI7BKW3SdwvPbcrgCekwofSBCPuWqy0uY2TOpF6Co7VjjxwxpalyhtSsIVPe3ChL4M7lBWpQ1aWoJz-f67aq4maPmr3QxkQ-YO9PN7Cd2Pfru9AOglOnztkSmaU5mxB0PL2hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇪🇸
🇪🇸
ادین ترزیچ سرمربی بیلبائو:
🗣️
باید مراقب انتقادامون از لامین‌یامال باشیم. با بازیکنی طرف هستیم که سه هفته پیش کل بازی‌های جام‌جهانی رو تقریبا فیکس بازی کرد. پس توقع نداشته باشیم بعد گذشت این مدت کم بتونه هر بازی چنتا گل بزنه. باید به این بازیکن برای ریکاوری بیشتر فرصت داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/104896" target="_blank">📅 13:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104895">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VL1-Uvn3EcFYlK-LgYL4mo3p5gTqX5tTS8MSht1eo_HHrhbvopgde0-7Rx1jeBm0j3D0w4hEmHhoqxAVtrc2o93RyPTCOksfJ68dcaEdpo9mN0jiZxjRnISHno8t7K3adv_jG05d0pf-Tp2-qauBFxz4GH__sXyLf6rdDCFxnpnlFWTDyD9IBg8MD75R4GgkJTlHdrr6QLQ6__sIPFIxCjuA6xauO6cvU-y7uB0W90V7nOXHAqItpPHwn1CbCDIlplqojfaAbiMfyYxUrZEZKEDZVU_0xsSRY0PtcSgP-t1WISJOL5MbGZDDTtm1Tck4KC8kTxTAAJML2pq6KuOgaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚬
🇪🇸
روزنامه COPE: آلوارز پرونده پزشکی با ذکر دلیل افسردگی به اتلتیکو ارائه کرده و تا هروقت که دلش بخواد میتونه سر تمرین حاضر نشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/104895" target="_blank">📅 13:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104894">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqmn7undJglxI-iZXiycNUTVGUmK1aLw58wnHTOLCANAsPdhXbAtxtihTn203gA1S2GdGRNAo_pG9mQHmz95kocVFIKYVVgY6zqbiQMH_scma57ORf8PXqgGgYaiHu_tcjfKI8UaqDzWoDnnJClUfZYLTYf6WoVucagBzZ0pzIsqaa_u71480EtE4owoXOFgnudzWyDBzR1Ojg5HBa35GFQhsTndVTxeJdrS7539VxzCFL3nIz13Ma9t7Uxcbbbxiytj8BsjidCpG3XNj3cu0UJA1ebjBwDH1Ycck6nUJyBk9vrGGza5crl04zN7R8YUyJ0ACZqnrPROPEQ0g7LPSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
❌
خولیان‌آلوارز برای سومین‌روز متوالی در تمرینات اتلتیکومادرید حاضر نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/104894" target="_blank">📅 12:58 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104893">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d697485bc.mp4?token=sAcVAEVSL-sv6rxKjVM44I_c36sm1TgyVGzi5Xk9BEd075Zd1Pj2uK3XWFiwBYLIz8PD6AWqklRHsFMP4kdyOo9JnyPYnMedYYzd_EHL23P6DT20XJq3Xsz85Y-FwrVz2nMOPICtUZwTMMz2QnmUqWjSixXOErRLbLXFdVApA-zOHgjlx96pSlYXvPpzN1di59vegMb_Fd1jvG02xNp7pgbyyHJYkYqrC6ylj1KyndcEQo0hhZ7I9hymAfbfXkYOg3xF8RDexAFnYuqSa7vVVWCPIltmaonm5SOuYjJhrMazPW27QzcgnmVbfuP02JHfbblsPqdWCGedDgdtR87HYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d697485bc.mp4?token=sAcVAEVSL-sv6rxKjVM44I_c36sm1TgyVGzi5Xk9BEd075Zd1Pj2uK3XWFiwBYLIz8PD6AWqklRHsFMP4kdyOo9JnyPYnMedYYzd_EHL23P6DT20XJq3Xsz85Y-FwrVz2nMOPICtUZwTMMz2QnmUqWjSixXOErRLbLXFdVApA-zOHgjlx96pSlYXvPpzN1di59vegMb_Fd1jvG02xNp7pgbyyHJYkYqrC6ylj1KyndcEQo0hhZ7I9hymAfbfXkYOg3xF8RDexAFnYuqSa7vVVWCPIltmaonm5SOuYjJhrMazPW27QzcgnmVbfuP02JHfbblsPqdWCGedDgdtR87HYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
▶️
یه ویدیو کاربردی ببینیم؛ با این روش حافظه پنهان و لاگ های قدیمی گوشی سامسونگ پاک و سرعت گوشی بهتر میشه، حتما بعد این کار گوشی رو ریستارت کنید. نام گزینه :
Delete dumpstate/logcat
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/104893" target="_blank">📅 12:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104892">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cca0ed089.mp4?token=JIP3DsQx1d1evJ69F83bo2TuzQg_bbrm2xKfKHFiDgSKWOlzM-_UH2pwflE_UPNfKDvtxCFgsixEXBG1rDAL23XE8K4SrauXMth7fSUbLWgG0bi7fE_PnhwH9lxub4Bq_louilY4kKVhy_180b8Wwvwo6Hmao7rGwi-Gu4YpTcVfJ4izlbQciXTk8y3U0we69ARwnFybX28gwmPIXEowJWfpETVknFeEWmM5f6uCnFHxbl3bf_xo8iqw5JNaYj1Xp-FXQW97JJ6dGkiqMpcucNKmr8jo486K_Mr6Kia6MD_dfYPrc774YJMoF1DqRVu6ERj5AN3vOLqeckWuNwFp3kWspsc-EDUCUpMlp6j9FwRQwz9SPWRZST2Lhl_1j1i92lpLlb73v6FATxD81ksbzlCGDTVW-j6pN2pyo94KpzIvmIa4toUCILksXkr0NpS28RVDeHVa_dHxeD9w3Pl291ulHpCTZT6VJWUO4V7NpTEnJVkWwgSU4wcitoW4YQN3ZF4w5dfgQ-DKSDeJhdZSpW4r-pPtt8MT4yfTjFMkeCGKK2Dmi4PjEBaSDIM8_Cp4lprD3E3RtvgYO9K6lwrJ5Kw-GEjT-5gLRxRqcFATz29Y0DDoYKTOBCSSRHI62VTd_OkQpxDAXlYUNhf-DerIlrMv-3HAL0JZGPspTccjXt4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cca0ed089.mp4?token=JIP3DsQx1d1evJ69F83bo2TuzQg_bbrm2xKfKHFiDgSKWOlzM-_UH2pwflE_UPNfKDvtxCFgsixEXBG1rDAL23XE8K4SrauXMth7fSUbLWgG0bi7fE_PnhwH9lxub4Bq_louilY4kKVhy_180b8Wwvwo6Hmao7rGwi-Gu4YpTcVfJ4izlbQciXTk8y3U0we69ARwnFybX28gwmPIXEowJWfpETVknFeEWmM5f6uCnFHxbl3bf_xo8iqw5JNaYj1Xp-FXQW97JJ6dGkiqMpcucNKmr8jo486K_Mr6Kia6MD_dfYPrc774YJMoF1DqRVu6ERj5AN3vOLqeckWuNwFp3kWspsc-EDUCUpMlp6j9FwRQwz9SPWRZST2Lhl_1j1i92lpLlb73v6FATxD81ksbzlCGDTVW-j6pN2pyo94KpzIvmIa4toUCILksXkr0NpS28RVDeHVa_dHxeD9w3Pl291ulHpCTZT6VJWUO4V7NpTEnJVkWwgSU4wcitoW4YQN3ZF4w5dfgQ-DKSDeJhdZSpW4r-pPtt8MT4yfTjFMkeCGKK2Dmi4PjEBaSDIM8_Cp4lprD3E3RtvgYO9K6lwrJ5Kw-GEjT-5gLRxRqcFATz29Y0DDoYKTOBCSSRHI62VTd_OkQpxDAXlYUNhf-DerIlrMv-3HAL0JZGPspTccjXt4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⏸
آنالیز فوتبال استقلالِ سهراب بختیاری‌زاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/104892" target="_blank">📅 12:20 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104891">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cwo1itla7oTvDT_lcBmBsXi0YjviFdfa0eH-GPeG7NX87BQKy2DTu0SL1hyi-sgSDRgAEycQYTHDq_2Y5_ftcB_QCe9ulXCsf6evAcBGBBLY4dsZip3-zrt9NkJsmevBhIrePkjYj9BPyVsCXMTKQg28lh77XXJ6Nf5GE-YW3zHCsRkSIeiL9TeGvNLZqjTXXMdcNc8SSHkKZYTtpWs3hPdOlc0pAl9-r3FMLI380R5gFsnbqkzZd8Q43PNu8KfLYVLA2A0jb9CqZRrlnIJzawLcqoYdoi4c7SeVn4fcbTlXRD1wBeJFEcSHSb59GophUxaF0xv0QdncIwU8ayB5fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🏆
بزرگترین بازی‌های دور گروهی مسابقات این‌فصل لیگ‌قهرمانان؛ سیوش کن بدردت میخوره
❤️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
🆚
رئال‌مادرید
🇪🇸
🇪🇸
بارسلونا
🆚
منچسترسیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی
🆚
پاری‌سن‌ژرمن
🇫🇷
🇮🇹
اینتر
🆚
لیورپول
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
بارسلونا
🆚
پاری‌سن‌ژرمن
🇫🇷
🇩🇪
بایرن‌مونیخ
🆚
آرسنال
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇩🇪
بایرن‌مونیخ
🆚
منچستریونایتد
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
🆚
بوروسیا دورتمند
🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستریونایتد
🆚
اتلتیکومادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/104891" target="_blank">📅 11:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104890">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBkMZ61X2eiJQH8YXa1pzwBD-aAf5hq8XrhAbXm_XQONulOQeEhYQuUnQvSvp2RMHkh-EcYl8QDEDhttnXt8D-20XZ8EDLdKje1sYfgo03o0IvpLLOqQXX82I1HtQDscc1P81P6ePIe4-Ow5XrbDIkyVM3mTbJxroax2N-HCaYjmNPBZClDflHsa2KYrrPuYRv2wKz41XK6gWhDvuZFlBz1f-ivfQKIRFpKl-quStJyZ8ic7P_fVbCIGzRPB6RYWxFGRClpD0TN-5KWzZbZhUdFBTYuh6io1qNsm8o9-kLcNRxeYIOOUFrD70KSd571SJeVRXwVop8tHHMuuS6ttTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
❌
خولیان‌آلوارز برای سومین‌روز متوالی در تمرینات اتلتیکومادرید حاضر نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/104890" target="_blank">📅 11:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104889">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9611757770.mp4?token=bufrdPujJZJONRqddv0pPyz9ajL_naMwdvZwcFe29FIZF4SsqXZtO5ibD7B0kmdTVewJIcgy5GMKKjFOXNJBB3BpekanxheTugKtfyPaJfEhBFxzQ3_oaKV7WiJ_otC-3_epLo98jhC0BlbeTKLIy1s7kt23SJgp5xbDe8jXeRusnBRdYgkGx0T9vKl75fhyqv7cBDnPnBbBnhhgZlVM8TxNnweQrQ-yAq6KeS3SlskBEDqe8tRumUUwBuVwjduVNKj7qpQmNpPGyFfBrmQw8MW7aSO2U6KftLr-EccK25N3TAcOrSdY6kwajRejiptqaWQluW7e0I-_iz_8O5mfDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9611757770.mp4?token=bufrdPujJZJONRqddv0pPyz9ajL_naMwdvZwcFe29FIZF4SsqXZtO5ibD7B0kmdTVewJIcgy5GMKKjFOXNJBB3BpekanxheTugKtfyPaJfEhBFxzQ3_oaKV7WiJ_otC-3_epLo98jhC0BlbeTKLIy1s7kt23SJgp5xbDe8jXeRusnBRdYgkGx0T9vKl75fhyqv7cBDnPnBbBnhhgZlVM8TxNnweQrQ-yAq6KeS3SlskBEDqe8tRumUUwBuVwjduVNKj7qpQmNpPGyFfBrmQw8MW7aSO2U6KftLr-EccK25N3TAcOrSdY6kwajRejiptqaWQluW7e0I-_iz_8O5mfDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
💙
❤️
سعید فتاحی مدیر سازمان فوتبال باشگاه استقلال: موافقت کردیم  سهمیه هواداران برای دربی رفت 50_50 باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/104889" target="_blank">📅 11:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104888">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a80b61109.mp4?token=IqCwx0Q4FMFLB9QFIRSLxAiQCwVNhLd8ype_XGK6ONUHs-DVrxPMhvllvk-89CaFG5xAhyFcmcGd7HTAOlK3WehWeFhtwsI78fDbJEI9TWR9So_30uPmvRWsC2znabqiNmzsRiDnSYAMibK10ODdEmvCmeNxEOcdlqFRIqGPs-WdWM9MRD-ErfX-MJkwzdxWPX0lthCVsxxU6piPBhMkiv-a7GlJmDPSjestLIvWyS2_1Wx9C9wKciNBVMTYzrpzF3s5IIEtwSKUKENRQVidWmQusmKw-WHP-jQVKj99zfF7g5DS3rulThYspkkCKZvAEkrP3pLNVHvuIU-p2VEYgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a80b61109.mp4?token=IqCwx0Q4FMFLB9QFIRSLxAiQCwVNhLd8ype_XGK6ONUHs-DVrxPMhvllvk-89CaFG5xAhyFcmcGd7HTAOlK3WehWeFhtwsI78fDbJEI9TWR9So_30uPmvRWsC2znabqiNmzsRiDnSYAMibK10ODdEmvCmeNxEOcdlqFRIqGPs-WdWM9MRD-ErfX-MJkwzdxWPX0lthCVsxxU6piPBhMkiv-a7GlJmDPSjestLIvWyS2_1Wx9C9wKciNBVMTYzrpzF3s5IIEtwSKUKENRQVidWmQusmKw-WHP-jQVKj99zfF7g5DS3rulThYspkkCKZvAEkrP3pLNVHvuIU-p2VEYgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
💙
سعید فتاحی مدیر سازمان فوتبال باشگاه استقلال: داریم برنامه ریزی می کنیم تا هوادارانمان را هم از خوزستان و هم از تهران برای بازی‌های استقلال به بصره  عراق ببریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/104888" target="_blank">📅 11:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104887">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb886e60fe.mp4?token=S6WL4KFHygXkcuyqZ1WI_bYtkoaFo2a_B0tcMsRdsfFo3AGfecpONN7Cw63pSPjzrsgwAtTvIqWMpFVU6aj9CZklYpw5FNAlSB3ysTlbyLGcPHECtYQaml4EgP7FDyXicxRL9q-OSCGivXOutN7nqFxyefI5GrF0jeSIfX40wBvC7Smz6tWIr2m3-AeaVDsvTYXyuEO8WeB5CPbEfsM6GSzptCfvaWM-kzhIOP-IBW8JI7G8CuN24D2Q9881kxw_axDOAaKUCrGHlJ3XIduEmIGriWCTbn7FxXBJQRxVi1ztrEroSi97fnA_tZuYsGqy_5fCQfTuvL0w_ybKE5FhJjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb886e60fe.mp4?token=S6WL4KFHygXkcuyqZ1WI_bYtkoaFo2a_B0tcMsRdsfFo3AGfecpONN7Cw63pSPjzrsgwAtTvIqWMpFVU6aj9CZklYpw5FNAlSB3ysTlbyLGcPHECtYQaml4EgP7FDyXicxRL9q-OSCGivXOutN7nqFxyefI5GrF0jeSIfX40wBvC7Smz6tWIr2m3-AeaVDsvTYXyuEO8WeB5CPbEfsM6GSzptCfvaWM-kzhIOP-IBW8JI7G8CuN24D2Q9881kxw_axDOAaKUCrGHlJ3XIduEmIGriWCTbn7FxXBJQRxVi1ztrEroSi97fnA_tZuYsGqy_5fCQfTuvL0w_ybKE5FhJjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
مروری بر برخی از گل‌بخودی‌های سمی لیگ‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/104887" target="_blank">📅 11:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104886">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d3f8f817.mp4?token=T6MfVDGQNyB_M4-qKBtDFpuoHF_LyJrnTsU7SwLct2KMFLiKl1UP0zfkUJZg2cgt0gcVmKm-U8MYe4uAb9-lcj8UxfFVrYWM6T9Q4oambX4lSKGSnTWzZP9YQXYpIdeXfRv0AR_6y5qWvBZ5iw9KN3eru61sUJknxpG30i8diSMOsdrF0bjTffh0tvmowvnzqMTz6Enljv49sg1yyTsB-7Ks0-KsjRHusjQRw2HcfQ8cX9Hid2H2LtOm0TEykZ8Ix8Im0k0NQz2jI7xZUnU7xELBGkfFroHZkJyFMXu9gof3hg7QDWiT4yp14MkO4b_QatbpWRTC425ZwISyd7PZe4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d3f8f817.mp4?token=T6MfVDGQNyB_M4-qKBtDFpuoHF_LyJrnTsU7SwLct2KMFLiKl1UP0zfkUJZg2cgt0gcVmKm-U8MYe4uAb9-lcj8UxfFVrYWM6T9Q4oambX4lSKGSnTWzZP9YQXYpIdeXfRv0AR_6y5qWvBZ5iw9KN3eru61sUJknxpG30i8diSMOsdrF0bjTffh0tvmowvnzqMTz6Enljv49sg1yyTsB-7Ks0-KsjRHusjQRw2HcfQ8cX9Hid2H2LtOm0TEykZ8Ix8Im0k0NQz2jI7xZUnU7xELBGkfFroHZkJyFMXu9gof3hg7QDWiT4yp14MkO4b_QatbpWRTC425ZwISyd7PZe4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
وضعیت روزهای پایانی نقل‌وانتقالات خولیان آلوارز و اتلتیکومادرید ببینیم :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/104886" target="_blank">📅 10:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104885">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-kXP77XCw3kS5OXYRD73jesFIhY8AzLX581TNmSbBIgjB1swPd4gC8F8bLA1jwlKuyCmiliirv3uu-3J-5YNl9wQe0cIEVA3-5l83caYrSWGVl7xmJApOLHqzo4eJ3uJSxcBU9aI-m0dslD0_gXx3MBhnLSY8Gn_YBkx3d9K4x8VL6ZuIf9yJkN7XPNwpHx8fIPDpSp4xJlzjr5tSKDg-1CWSLEi34rSbafjbnZFQGSqdyur2edSlnA-yZqVitVf6gvRNd2nh4dQXlxG3wCS0I1hj1mZWZtOclY6wMX4TwZgSbCU7i6uYUQrK37dozwloK9a7ehc3Njag1BKby5nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🇮🇷
میانگین‌سنی تیم‌های لیگ‌برتر ایران؛ پرسپولیس با جوانگرایی تارتار در جایگاه دوازدهم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/104885" target="_blank">📅 10:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104884">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/347df9f824.mp4?token=vkk3G9bk-F6OmhW0mzpUbIRwCx2NSEM246mE5kLa57NWcArUrYv3A8NXYXXgEFWMAauUUUWFXai7UEn6Ln_zU90dPEsYJTC9KRWe-yJYgEho-mgOg3MPXDAIVmRdYqUsEwPYm0nWCSUJZpjHH-escO_9bjvATJ6AIKE6OmkIFymMRs1tG4CXE2T6WigppaD1t4V2O2AZB_9p1PwBmajY7uI6d5x0tEeMjG3zTpEzD64L4F2QSdC0N-nYQkXgoj-8f9MdecF2nluIPrzDwRgpoR-jBkH2Nh87nwTtGDxXKdIO7wdK2T0Q3a5sjg5u4GuJV1-LMwLGnfTsTzxoZq4mow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/347df9f824.mp4?token=vkk3G9bk-F6OmhW0mzpUbIRwCx2NSEM246mE5kLa57NWcArUrYv3A8NXYXXgEFWMAauUUUWFXai7UEn6Ln_zU90dPEsYJTC9KRWe-yJYgEho-mgOg3MPXDAIVmRdYqUsEwPYm0nWCSUJZpjHH-escO_9bjvATJ6AIKE6OmkIFymMRs1tG4CXE2T6WigppaD1t4V2O2AZB_9p1PwBmajY7uI6d5x0tEeMjG3zTpEzD64L4F2QSdC0N-nYQkXgoj-8f9MdecF2nluIPrzDwRgpoR-jBkH2Nh87nwTtGDxXKdIO7wdK2T0Q3a5sjg5u4GuJV1-LMwLGnfTsTzxoZq4mow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
⏸
باشگاه استقلال با انتشار این ویدیو نوشت:
❗️
خوزستان همیشه آبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/104884" target="_blank">📅 10:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104883">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f8d86050b.mp4?token=fYWgQgo-Crd8BTfyZZeAqgoRfNLiVZIqP85m2MIIRb3_6PnS1DDlpNIZXC7Ir1tJp9GC1SRInteUlukkGNzNZbyHMj4-Mxw_Ha4O3UXpJvDIAk3_2eQFQiq6w1SV3SfhuVoO-ZwoSrilPZO4RA9EJkQ3UguTbiHdLha9A6BQKofmNgOe4aOkJ9qZKK9cNo2mQfW2W5laHN9AI4ZCOexdDvH731tld9WofVVGPH_YgETBQDKkBR4zMEYZWM9Xlhy_JNRSPE18214Z31bqpgM74-tNzHwC0kJCsrqGjEKqCQ6xcXQRRzpQJZDkl9vjoHlSgWnd5BSz_oUZhbT8qqZXiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f8d86050b.mp4?token=fYWgQgo-Crd8BTfyZZeAqgoRfNLiVZIqP85m2MIIRb3_6PnS1DDlpNIZXC7Ir1tJp9GC1SRInteUlukkGNzNZbyHMj4-Mxw_Ha4O3UXpJvDIAk3_2eQFQiq6w1SV3SfhuVoO-ZwoSrilPZO4RA9EJkQ3UguTbiHdLha9A6BQKofmNgOe4aOkJ9qZKK9cNo2mQfW2W5laHN9AI4ZCOexdDvH731tld9WofVVGPH_YgETBQDKkBR4zMEYZWM9Xlhy_JNRSPE18214Z31bqpgM74-tNzHwC0kJCsrqGjEKqCQ6xcXQRRzpQJZDkl9vjoHlSgWnd5BSz_oUZhbT8qqZXiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
🎙
واکنش تند مدیرعامل گهرزمین پس از بازی دیروز با گیتی‌پسند: به قول حاج صفی یک جام بدهید به تیمی که دوست دارید!
❌
صحبت‌های حاج‌صفی مربوط به دوران حضورش در تراکتور و بازی مقابل پرسپولیس بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/104883" target="_blank">📅 09:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104882">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c607f6634.mp4?token=su9uYODKlvZqIde_G5BTIcii0d2ars4zboijtK8Afre7wy1Rs5fhEZ45wYqwS2wNI4VlgQhx3WFjq1ogZrfJxebPIiVnqkvLVg1ua3ByViHdEdEqbumZB_VSw3Ya8ixpFZCHKn6f0Dbb1R8QNVgABfxxPySzQSbwRIV58EoYXPSN8JERpT-2Qzdsyc_BZLOJQwpDpNKUFeaCufMpazBWqxMUijDA9pT-M2ncmFR5ycqTWVfGeo_aSvj0AX4dsA_ZiU6nY6lIXvVrR9CYn_Nb7zGkDQtWxDYRo8eyZr94YEBRcVQNXQJTNcxEEb6SASDUawHiSt7f_JSRH-UUTlSjHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c607f6634.mp4?token=su9uYODKlvZqIde_G5BTIcii0d2ars4zboijtK8Afre7wy1Rs5fhEZ45wYqwS2wNI4VlgQhx3WFjq1ogZrfJxebPIiVnqkvLVg1ua3ByViHdEdEqbumZB_VSw3Ya8ixpFZCHKn6f0Dbb1R8QNVgABfxxPySzQSbwRIV58EoYXPSN8JERpT-2Qzdsyc_BZLOJQwpDpNKUFeaCufMpazBWqxMUijDA9pT-M2ncmFR5ycqTWVfGeo_aSvj0AX4dsA_ZiU6nY6lIXvVrR9CYn_Nb7zGkDQtWxDYRo8eyZr94YEBRcVQNXQJTNcxEEb6SASDUawHiSt7f_JSRH-UUTlSjHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
رضا قیطاسی
✔️
رستم‌دستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/104882" target="_blank">📅 09:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104881">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSXSZ33j0hYYkfVR2O4DOGdQ_B5e_KROXN9jgypZT8QhkYdj5rE7muOBHkU8Q14uc8zmX6lTBTBiAvotPA32Fkn9XfA7E_g4vMQsxAGGZU9312g7GNDV46rpxvipgvdMtJYtioviNY-7eS_DN8z5sanljztbCkbL2_c8MAvGXaFgEYQpUG7TOQB9Vwy9rsoIw3SPIoYr383cIkRP64CTo4LPCw7Kwcp1XKz8ljI9pYavZQQur1p_yV2iAjqZIhWM_f4qMkV2Reqshwu6EdGBjNXTgveJdd-FGNLEu6fS-vqXj69kZG_dIWP1M8QMZ7s_g8A1WV-Eann5AKYxYL5XjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
🇪🇸
#تقویم
؛ 9 سال پیش در چنین روزی؛
بارسا باپرداخت 145M€ به بورسیا دورتموند عثمان دمبله ستاره جوان‌فرانسوی این‌باشگاه رو به خدمت گرفت.
📊
عملکرد دمبله دربارسا
: 185 بازی، 40 گلزده، 6 پاس گل، 141 بازی رو به دلیل مصدومیت از دست داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/104881" target="_blank">📅 08:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104880">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2d8d92ff.mp4?token=iF7PH8tWOHy8ZUOPCYQnQH1LuOtJLSNMRNXnB2vmSQfKL0HxIQOo36AcBrZfglZYAeSZVnxv7IJnkUBD6cP7OuaBavUl0Vi8NsFfJjBETN82AdpkB1AVNmyrQU3vn-bwoj7XhvNMkQhlvsz9F9nusqITsrmG9zOLsQXUfI7AYV-_fVJ5jRJdqcOxnO3N2fHS6B7Ukmzv4HXwYrwUawPpTUui1GTjMxm-OmQt0jEsQdoTdFqq5hinMwrRcsvn-cbYEf5k7DWiYC2_WPKuVbPdBRmayR06Fi3vII8wTQNwLb5dZYhCUdBRfSSAuIWMhpPs2GI9VRFe3XnjUmc9fpcNjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2d8d92ff.mp4?token=iF7PH8tWOHy8ZUOPCYQnQH1LuOtJLSNMRNXnB2vmSQfKL0HxIQOo36AcBrZfglZYAeSZVnxv7IJnkUBD6cP7OuaBavUl0Vi8NsFfJjBETN82AdpkB1AVNmyrQU3vn-bwoj7XhvNMkQhlvsz9F9nusqITsrmG9zOLsQXUfI7AYV-_fVJ5jRJdqcOxnO3N2fHS6B7Ukmzv4HXwYrwUawPpTUui1GTjMxm-OmQt0jEsQdoTdFqq5hinMwrRcsvn-cbYEf5k7DWiYC2_WPKuVbPdBRmayR06Fi3vII8wTQNwLb5dZYhCUdBRfSSAuIWMhpPs2GI9VRFe3XnjUmc9fpcNjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇿
شادی‌بازیکنان صباح آذربایجان از تقابل با بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/104880" target="_blank">📅 08:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104879">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVxOJxVUSipkNvCTlXo6VoHc44YhlKU9kWB2BGmLxStQnewDuahtOmWuQ26WBB8op0UPln5DnE16v8gOtRy_P8uFxQDanplf_Uxmzr85WYoFeN51O0vbtyXZs8QQAHjJ06NZEcu3VKewOnPvN92Uw3pP3RkdV5UkeER11xDMSiHJBx2ftnLcyKRSokpzbbyvbqan5-58t2LY5JDzJmo7vRPj-jNNEBpLk6yAdrYiDaYVcQQ9AEegWmaEHpwamEJqBYoj0ka2YJliWpA3QeNTCWjJR2G-Z-xEBtEzipN9q0Zf_uyEkA0-mt_bT1chSjk6kaaM8hb_eXsExDpkK5hoLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دی‌مارزیو: منچسترسیتی تماس‌های اولیه خودشو با لیورپول برای جذب مک‌آلیستر آغاز کرده! سیتی قصد داره به صورت همزمان طی روزهای آینده با مک‌آلیستر، انزو فرناندز و کودی‌گاکپو قرارداد ببنده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/104879" target="_blank">📅 02:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104878">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‼️
🇮🇷
دختر استقلالی: کوشکی امروز ۴ گل میزنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/104878" target="_blank">📅 02:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104876">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c3OW8al1NG87JO1gVknOorTteQLmqiKal-b8fdVHwmJDlvdhWcXvXLUgtzx2LxRZPqT3ob2B2lAVZyqG_HFnhV7FlF0msu1imhRLl8c-Jpv5otmmMF3vfhmdXgGeZYTIr_2OaOqCdi8VHe5f9ejyr7MJyw2ie2_Mk4HOEyTUQQXGc7Q8SnFplTaCI2iZLcQvsHSnWy8tbRRCmzIeMWbSsK0uO6nUy3eRtVFE7rUwcop5gXxEwbUIaN9Ua-oiJCLPhZDsO58WwuNgqPfbepkC-XabG0YRqWyefgnKjZuwOHzVE1R5CyqYLM__X8kf2VUVgNIXyZz8quzUDBV_Jldxlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ifzbBHlvwoQoq-M63MYY1Sb16IlTnUZPMTbP9O_CTZyQCqI6mWfJJq8i6C3G6Mk0M7lQ-CKVu-WUbBdNqX9_4Vj3VBxG0zSKlTt1YEueenXe2DA_OGWwhFWLiYUhmpweCVI9fWKsD86s-smfyreV3aeR_nxxFYU4L9LdXCdcjXdBPBLEkmuNKxrSGYigi1jzZvl4EIhmkb5BZs3Gv7gyp0ihF3gkS2-9KEXhcr7dnXB5e5d8q0z8fKWkGEVbng1wZvmswmnmFgr4tuTUaFtmwfCxXvR_3LA9EtIUf9i6CigLpCb4RrkEYezBP02bNkIMVSGfYtPNNUCDFYx1mFF_FA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✔️
🇪🇺
🇪🇺
مشخص شدن تمام 36 تیم در هر دو رقابت لیگ اروپا و لیگ کنفرانس
؛ قرعه‌کشی ساعت ۱۴:۳۰ امروز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/104876" target="_blank">📅 01:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104875">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63ad7bc72b.mp4?token=Yl8fDAd9xOZh2FY1G6f3-uS9-y2nsLNcppn9dgfScCBhAZ3RRJPPXB9DyHumIJr7U9rdzgR_JHHUCfkZL8J_s2CVV2r9CNltv5s_v2kOW9gKCXkuCdXF-kz0hZdRvrRLFFr4LDvfRNi_sUNRpIIn3GVDTgiWF0G-WUoVpGp6856u48ifQEm8LOEHPcPFKJEfctThchgm0921eZWXUyhGDTR5_DpUBqzeBZFr3qsemM0RDHWWBp3UMtD3FS2pQ04UYQ0DYKYmSZ2n-s8ggt_kg2KK0OH8218rRpgu07zMUubbkRVFCTThaIlFKeOv1Ajbzl89Rrq8-po7GbCeGqpDqQ3an47LjKljHboeNEmj6NqJssPhXMDgc6A3WoP7oHccxWH4O7AzfjVQx-0MQhx4gl4pcp1CKrTH43ry3jHcm1gVXxRHmiCWP2f0-lBQK0xPfX4HZIA7p9f3nFIt2cVVGVhVph_-dYKmXRnjddLC2vdWN_Nuqp0faKBhjuwglSxxzIfgzuhLjrRcTwwyVUedcINK1Dt_oZAlhMWCC70ntK_ki1I4mU27j8QDXZxJqz24vuegS_m147CBUwO5LTSrMx5D3YjL1Hr9VwOdXcBHzhBieNb0RnUkwH-q7Tq448cc0XierINvR_UuehR3SNifD68LExPc5BclVWvLqlZWmUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63ad7bc72b.mp4?token=Yl8fDAd9xOZh2FY1G6f3-uS9-y2nsLNcppn9dgfScCBhAZ3RRJPPXB9DyHumIJr7U9rdzgR_JHHUCfkZL8J_s2CVV2r9CNltv5s_v2kOW9gKCXkuCdXF-kz0hZdRvrRLFFr4LDvfRNi_sUNRpIIn3GVDTgiWF0G-WUoVpGp6856u48ifQEm8LOEHPcPFKJEfctThchgm0921eZWXUyhGDTR5_DpUBqzeBZFr3qsemM0RDHWWBp3UMtD3FS2pQ04UYQ0DYKYmSZ2n-s8ggt_kg2KK0OH8218rRpgu07zMUubbkRVFCTThaIlFKeOv1Ajbzl89Rrq8-po7GbCeGqpDqQ3an47LjKljHboeNEmj6NqJssPhXMDgc6A3WoP7oHccxWH4O7AzfjVQx-0MQhx4gl4pcp1CKrTH43ry3jHcm1gVXxRHmiCWP2f0-lBQK0xPfX4HZIA7p9f3nFIt2cVVGVhVph_-dYKmXRnjddLC2vdWN_Nuqp0faKBhjuwglSxxzIfgzuhLjrRcTwwyVUedcINK1Dt_oZAlhMWCC70ntK_ki1I4mU27j8QDXZxJqz24vuegS_m147CBUwO5LTSrMx5D3YjL1Hr9VwOdXcBHzhBieNb0RnUkwH-q7Tq448cc0XierINvR_UuehR3SNifD68LExPc5BclVWvLqlZWmUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇳🇵
‼️
⚠️
جان جدت دلشو نداری اصلا نبین؛ وضعیت فاجعه‌بار نپال پس از سیل دیروز!!
🦾
🦾
🦾
🦾
🦾
🦾
🦾
🦾
🦾
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/104875" target="_blank">📅 01:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104874">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEsL3wSPeYn-grwSnwGIPdcnYAR__51jmuE8bwLI7gTOIyulqo1801jhyRqDK2P5ucgLDR6akhRz0jykdmkBILjXQTA-yZKRRwLQ3U1_2uC9R6gW038Jkr4EpngdlhaXnCyHnRs55rVMoD9TvCdSRvAdEyBwIZ7rS74DGd-D96HHyCumPVV_cvNq1ZnZohHSXIaXafELp3PYEQ37rMVJtVJ3oEhDxugCj5cLBlO13rQxbC1SnPGIDD61ZR0ucOy4YkTc74gw0_1Td1j5NjzqxwGIU_Mhd6yeBgxiWbHzr9W34j056E6fOPOONpJdYTuiVRLVkdjANFxwMCElfJy5aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منبع خبری indykaila، مربوط به لیورپول که اعتبارش زیاد نیست البته:
آرنولد به لیورپول باز خواهد گشت، اما فقط در صورتی که لیورپول بتواند طی روزهای آینده با رئال مادرید به توافق قرضی برسد
🤍
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/104874" target="_blank">📅 01:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104872">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uqFCSl_aqVmysmo7cmiaEpPqNrs9Ryav7vuU0cVuRapyy4m8Muzlv8o42Ld2tRwmSMKBOHGcUbfFnIkMv6r_oVldvpbhZ5B70GBUyMnRfW6KlpUyooAxlXfzDfGFzyGicqeCBHy40UuMpuMHFDBb6583ynpiA_aTpseEEX92GQT9ZTtqFdz4ZdfxL-U1iNCzISHINn-D8Cala7Gbvz6H-N3DGRjbS4noF9jqY0TcLN_SAC6awqLRWljV4plAfDo1QSbgj-epc-y6lOFeiRp0E9RaFft-WQ5M6nzGRX31dQor1VfA5ZMYy7_GSD0y0moaJ2GyrzYJE9sqpDYk88x_Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EnaZoScs-l1xLJX-VCVktKX10ihA8sVxAoNwjmiSnP7Xf6lRIhiEJHssxpL39AEAU5nFiHvbtOAa6yyOedNFPn4E5pRMJDiuNZX6Bn27iYlolZ2ClRwXGVUZcPG7-IKRlczGt3z9PkcOtkAZRe6ny7p8Mg7V_jU-mQHXrtDqFNASdV-d0kYqV1RzUQF_QKEd73Xl7keINy3Hv2Kc8m0llu3IyHC0hK19WASgF8sBudn0xsYzBeRSsendc-Iu5JQzhW27ANo_l_Nu6kcvOAn5jVZJ4631JEr_TUfokMUFIZa2BcRDs4aB87qf3Lo_Du42jCjprG0paeekCVyYQWUrsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🤩
💔
🇪🇸
آرشیو‌وار: ژاوی‌اسپارت در بازی امشب باید دو کارت زرد می‌گرفت و از بازی اخراج میشد اما داور باهاش مماشات کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/104872" target="_blank">📅 01:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104871">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5XHz8CxRBbYigjMdgYW2gJ2X7ht8o8u-B3zwK-gzr0KRrVjNqk_m3OGzzbWatbIWFihxJ3HxuHUoV3WBmB385VnFzBJob7oN6PaEFt4OQDBcpB9M6azlhkzQqZqK0f0V7LUMdeuOQigpt50lYsDgjw12XaYXSMYu-krH4LhTE0ExsbUW0UdyGKLJ6LeMjcM0VAMEN61QHX-2DWZQ1ZMjC6BYVERC8hoNU3qo3UeBiW7-ua2DO71ssuhuQLWFtGiFgXSUuCa2aT1P8UsAzNeW-Y2_KTRI0jxGqtl7ed385h43WQtFOta0407ZlTFATJ6TSs4U2fpds2aQw_iaUZdRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
محسن نامجو از نوازندگان و‌ خوانندگان ایرانی پس از دو دهه دوری با استقبال مقامات امنیتی به ایران برگشت. نامجو اخیرا به سلطنت‌طلبان انتقاد کرده بود
📲
پ‌ن: توییت چهار سال قبل این بزرگوار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/104871" target="_blank">📅 01:07 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104870">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
⭕️
🇮🇷
#اختصاصی_فوتبال‌180؛
❌
باشگاه استقلال با ارسال نامه‌ای به فدراسیون فوتبال اعلام کرد که تا پیش از بازی السد هیچ‌یک از سه بازیکن خود یعنی سحرخیزان، قلی‌زاده و رزاقی‌نیا را به تیم‌ملی امید نخواهد داد!
‼️
این درحالیست که بازیکنان دعوت‌شده باید تا فرداشب…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104870" target="_blank">📅 00:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104869">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6OLDLBke5_mNBRJ04skOvd3CdoeX7KxxA-04lEwBPV_wtjEXvctvWSdVC3VGVVkwFV-I-SdHrO9RIGwfmC80MpR6iQlF8IOQOn0iPR3DeHPYasLufxBwx44igd0w2tJxjRl5ccFge8T92Ch8c_NQmez0jzc9jKImySy5N75jTycZONG3qLe1VUrIfEE1fqpoqKVdMNN5g6QT41iEB0gSKHwXkhtAo9mrDKyLaOOvC5Hwpk2tm-6rUz-fzdRxued-gzlCygBTHRwgmrP6RdExOX8s5xsy8OqF0X8-n_djyoLXKkEvfvBI5HnHkblW5_LlfH1GCM7TH9FDJSIz0ioxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
#اختصاصی_فوتبال‌180
؛
❌
باشگاه استقلال با ارسال نامه‌ای به فدراسیون فوتبال اعلام کرد که تا پیش از بازی السد هیچ‌یک از سه بازیکن خود یعنی سحرخیزان، قلی‌زاده و رزاقی‌نیا را به تیم‌ملی امید نخواهد داد!
‼️
این درحالیست که بازیکنان دعوت‌شده باید تا فرداشب خود را به کادرفنی تیم‌امید معرفی کنند. از طرفی فدراسیون فوتبال به استقلال هشدار داده که هرگونه عدم همکاری باعث محرومیت هر سه بازیکن از مسابقات لیگ‌برتر شده و هیچگونه بخششی در کار نیست
🔵
آبی‌ها در نامه‌ارسالی به فدراسیون دلیل عدم همکاری را کمبود بازیکن در هفته‌های پیش رو عنوان کرده‌اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/104869" target="_blank">📅 00:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104868">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAkVPKwojvof0XWlF89oZ3LpZAAqtPpNNNirkN_w6pbKOXqx_EoiEGBKqFe0kbnFkQ1qrLEiApAup5M0QYLC2QvY4_PsQ--4YcJF3W6In67-_wAh6g5JIxKm3GT1ZZYLuIWyg0RocJajO2Dt7yLkPZKhMPMJAiyqU6VUGpfSrECs3QSdV1bC7acqrZGPC01pkhi3UJsy5JnVuAVO_HatTqBg_PBbAPxg3p31pBiL3oTDaPQZTsnbbRMwQWhXEAhXhebYuVBwuQHvf2tiFJvnSuYeP52VGR-MRaDK0y_xBxELgydlvugu5Q_DJP0lPQKMX5pecdDrOeHabCINBLHOcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
بازی‌معوقه لالیگا؛ اولین برد خانگی بارسلونا در فصل‌جدید؛ بیلبائو در کمال شایستگی مقابل کاتالان‌ها بازنده شد
🇪🇸
بارسلونا
😀
-
😏
اتلتیک‌‌بیلبائو
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104868" target="_blank">📅 00:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104867">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQvUX51FxxR7cjFJjUCn2nXuW2cAsGAW3eOK2IA8088bo96GGSnSKYuIUV2nf8JZYBjyrhnw4Y923fKKoCMH9-7Z2pO32fBQTclCEkQ5DtIebyVb6eKqskKtkKxvGGKZvs7fnWqcjLhUwu5gI4gjLgDx8ELpcN-_hPBGQo5rDoJjC8swyFkUibFOAeFYVowQKDjktmYCGfp-TwXDtRfKCP6iNCx4yuqJp-ixKmM4MAeCnZVpTr8c0QhI9vynA5_XVLzafvUt1VvjK3bUrkK4z1CzkeeFI0HXYY4Wrc0KZq38EoDufkE3YW_skSbf3tGt0cCOzqFASFkVMJ95hHb8aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
بازی‌معوقه لالیگا؛ اولین برد خانگی بارسلونا در فصل‌جدید؛ بیلبائو در کمال شایستگی مقابل کاتالان‌ها بازنده شد
🇪🇸
بارسلونا
😀
-
😏
اتلتیک‌‌بیلبائو
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/104867" target="_blank">📅 00:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104866">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">فرمین لوپز گل دوم بارسا رو زدددد</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/104866" target="_blank">📅 00:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104865">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104865" target="_blank">📅 00:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104864">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یامال یجوری ریده این دو بازی که وقتشه زیدشو عوض کنه</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/104864" target="_blank">📅 00:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104863">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
رودری وارد زمین شدددددددد</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/104863" target="_blank">📅 23:58 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104862">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇷
⏸
باشگاه استقلال با انتشار این ویدیو نوشت:
❗️
خوزستان همیشه آبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/104862" target="_blank">📅 23:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104861">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fd2b46d0c9.mp4?token=Ewv5cveeaQYZ8pNQX-3O3LIAEYR1K9EU_YIUqt9AxWwqsXQxQlOyfaqkXUhjueRnpDWKA5KIwUD4at4tpMVp23gYT4BIzuyiweXoicE8j49AmbEKDoxJF6-r9iRnWfgVtXMSjk4BMG1L1BXCpw0PpvmyipNx7bAtXDPX1OyQy1PLz8ulaluue_A-7DSBjnNclG2XAwRjOdiuketlT9pRc1Ls95urP-AbMHq2rei2OIzPQX38MhulfhjJmRUDFynAUsC5BCrEWkTOeFSqFhfpIAgWu8RKCOra5A5XYt9dYFVr1Sgwj_lil2eYjrBmuCo4E9s-y5Ztt9i3rcJkbBUHDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fd2b46d0c9.mp4?token=Ewv5cveeaQYZ8pNQX-3O3LIAEYR1K9EU_YIUqt9AxWwqsXQxQlOyfaqkXUhjueRnpDWKA5KIwUD4at4tpMVp23gYT4BIzuyiweXoicE8j49AmbEKDoxJF6-r9iRnWfgVtXMSjk4BMG1L1BXCpw0PpvmyipNx7bAtXDPX1OyQy1PLz8ulaluue_A-7DSBjnNclG2XAwRjOdiuketlT9pRc1Ls95urP-AbMHq2rei2OIzPQX38MhulfhjJmRUDFynAUsC5BCrEWkTOeFSqFhfpIAgWu8RKCOra5A5XYt9dYFVr1Sgwj_lil2eYjrBmuCo4E9s-y5Ztt9i3rcJkbBUHDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
😃
دنی‌ولبک بنده‌خدا امشب برا چلسی گل‌زده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/104861" target="_blank">📅 23:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104860">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f04612395d.mp4?token=Ghxl_ZcXk60zR7pr35JX1-GDDCGxTE7pG-ygMDTY8yE28HCcDHsKQhLIXDsV9SexAoCgcgTNFjLCFYyMZ9lxVl-TzgGjApfIDD7YqPXWskqHWsI91cQZ5ohPd30u_FVvp8B8KH6xN2B3GKt38DHYkwdoklgMAURf1XoskOw7SwyibxuNL415PbgI1FfAbcms-AfGWZcnd54_hSCPafKMIvpLvho5aWYbjSxi21hMm6r8nmpoeesUjyyxlMrDLTVHt7v-Q2-n4Zq4Md_ox-RDuU8vKrHqU-Gdg9Ya8WXMpzPZOB6nEMqZ-d0qS3Kz6u-DVxz8Ws-yYR5nMERYRZY8Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f04612395d.mp4?token=Ghxl_ZcXk60zR7pr35JX1-GDDCGxTE7pG-ygMDTY8yE28HCcDHsKQhLIXDsV9SexAoCgcgTNFjLCFYyMZ9lxVl-TzgGjApfIDD7YqPXWskqHWsI91cQZ5ohPd30u_FVvp8B8KH6xN2B3GKt38DHYkwdoklgMAURf1XoskOw7SwyibxuNL415PbgI1FfAbcms-AfGWZcnd54_hSCPafKMIvpLvho5aWYbjSxi21hMm6r8nmpoeesUjyyxlMrDLTVHt7v-Q2-n4Zq4Md_ox-RDuU8vKrHqU-Gdg9Ya8WXMpzPZOB6nEMqZ-d0qS3Kz6u-DVxz8Ws-yYR5nMERYRZY8Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🔥
گل‌اول بارسلونا به بیلبائو با سوپرپاس پدری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104860" target="_blank">📅 23:18 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104859">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اونای سیمون چی گرفتتتتت
😐
😐
😐
😳
😳</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104859" target="_blank">📅 23:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104858">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پشماممممم</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/104858" target="_blank">📅 23:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104857">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سوپرپاس گل پدری رو فقط
😐
😐
😐
🔥</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104857" target="_blank">📅 23:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104856">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بارسلونا یکی زددددد رافینیاااا</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/104856" target="_blank">📅 23:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104855">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گگللگگلل</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/104855" target="_blank">📅 23:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104854">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d569393418.mp4?token=DfRJBHg2yKg6AUAUCJy_Ce4PqjAapu8ppvIKqrHol9QJSlg7R6yNWMDE9bTchVmhY6hTquubpzCxVw_TS-buGIp6OrypmLOI-1__Q_gzzpbs7pYtyROUuNyqJIBHwsWouDsCUhXk4LYvUdb8_jJbfP6JU78LjX8ISSMU0evEaiNeAyK-Qoef0UfuMK9lrZ87ICiZJPzgyaMH7Mbo3Pfq5sPrX8vBgZMuDatGceSzPC8su7ECiW_xemTreZXBbBXx58_iEeXhNiU-mq-Jb5-YKvp8SFU3NvQMuzbFLd2tmabIIzdW78BNNeyqGTy74quCdegfjSBJzbshH7MYDtFmqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d569393418.mp4?token=DfRJBHg2yKg6AUAUCJy_Ce4PqjAapu8ppvIKqrHol9QJSlg7R6yNWMDE9bTchVmhY6hTquubpzCxVw_TS-buGIp6OrypmLOI-1__Q_gzzpbs7pYtyROUuNyqJIBHwsWouDsCUhXk4LYvUdb8_jJbfP6JU78LjX8ISSMU0evEaiNeAyK-Qoef0UfuMK9lrZ87ICiZJPzgyaMH7Mbo3Pfq5sPrX8vBgZMuDatGceSzPC8su7ECiW_xemTreZXBbBXx58_iEeXhNiU-mq-Jb5-YKvp8SFU3NvQMuzbFLd2tmabIIzdW78BNNeyqGTy74quCdegfjSBJzbshH7MYDtFmqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اولین تریلر و گیم پلی رسمی GTA 6 منتشر شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/104854" target="_blank">📅 23:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104853">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBZoIiBvy-X_YfCFdDV387P7e_vr98Cxepw-4nKjiFN8H26TU2ZQ1CXlo_gzw79KGjcOfSW_jTkYqMEx3I_--S93_j4fHwqQZ5f40RF_QB4eqA4VE8OQVZ5pOFppPVjQZ3vCPmBY7OnGahuA3PiF0NS_CgSAGe5Mxk2E3z70IAo6vQP8eUL8nHHRF5IndhpZFseEYfLPieMoohEsGRY65OmoeIbKSi-rWf7EZE_CulLSp9kDZAvneFO3gDXiu6F2wdwcZJdKv5Fl3DkYWl3AUxKxmxGQc9CZrRrd1fOZyVZwCIEx-x2NJLpwsjkKcAqvW8hXo8Uvu6vQ2tz0zFD0ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
❌
ایالات متحده آمریکا ویزای علیرضا دبیر رییس‌ فدراسیون کشتی برای حضور در مسابقات جهانی لاس‌وگاس رو صادر نکرد و دبیر در حرکتی پیش‌دستانه گفته که قصدی برای رفتن نداشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/104853" target="_blank">📅 22:36 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104852">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0oDP-YP3hKC51sjinFMgUQTcDsgJ8DL3sIT3yyF4f9_Z8gPRQtruX48gzwgU2kfOR-UaZ4H5YiJvaqcbapNd-GQ1H7cj6mbYzW8gQqvA8Z6ioOnynNOgkFHKqwAh8yVXvpnh4B9YtIWxZ8MRR4Ew_uRXb-iQOg7ODaQkeuQft8defTOHJgJClkoHq8OaOFsKqnNjhW2ODkTnzZj9U-keK9y5suq6qhsmkAyW8SdhvPy-6SOgjdWDoBT8TefmgLqQOlxJqyk37u0Qd8ACsYw1I5HdqD8mZ4N9FWD4g-Y2fDJteDZTL0VgfL9h4gJy8uQFf4zec5tyJGbImK2v_R3Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
📺
نظرسنجی
رسانه DAZN؛ سرنوشت خولیان آلوارز در نهایت چه خواهد شد؟
🇪🇸
‏به احتمال 34% در اتلتیکو مادرید باقی خواهد ماند.
🇪🇸
‏به احتمال 33% به بارسلونا خواهد رفت.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
‏به احتمال 33% به تیم دیگری خواهد رفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/104852" target="_blank">📅 22:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104851">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQaQzQhmSnkvT0Ay9EAIvW97FTPOZrQ1mp7_HlMLpj6PuHval_4pzHsfnDSHOb92Y6Fp69e_S_mm8cZiVVfHJtxLcZ8WHgxv-K5iE5CjUDbfFELncmev98wdpaq_rCF_0swgYC_6d8hpcXyaV4hM_GySjgl61kc8MEshLw4ZhXDWe3eFSeCyabbQo5zko_-1vySb7L5B0HR4dus1d6_ISxUPwPoWeINYWrf4fx5VzwUidv40K5jqIgDjrbRu6L6ySghb_9m9YuLfBkbD_RKB_C7zAboCOCCsb_DyqBlvgmj81tPR8LvPo2ci-XffiBZBQ072UkWrRhMDPnimqslrHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
برنامه‌های فولاد برای بازی با استقلال؛ از مردم میخوان که سریع بیان ورزشگاه که تا ظرفیت ۱۰ درصد استقلال بیشتر نشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/104851" target="_blank">📅 21:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104850">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdfb514bfe.mp4?token=rtU9_rOWxYu47EISgoXhntrrWCJX6vSwRnY_RXjAe2wg5wZUGfyx17GPjIrQ7t_e1CqgwdDxOHPzZaeRkmtxoASn1PegiDrnsEgO2ud8KNM9axAX-e2qRXDiUIPWbE00S2RYfVj1AWgnMwgA04CPZ4W5OhZmgDgOBLEJbD28SDLQ2QoF-XeMvgXkj7bpCPk16oYtERInDi9um4RJWiBmFICmcahbvCkpmjOPwzc79JYunweQLTGG7q6YJbh3E2KN4A2piG1QLzb_NaQJXCsFz9QsUS7GR0oQ60TSnc4gkHcEJII8uzx_Bq5ghNYYM-nsSBP4ve5P2li6tew4CfyXySAreyl3nC0-vxfKV1KGGxCrpht1NBcfh-88LbqFrXXSCXOx0U-bvzPr71YMwYgbV-HZdbRRoXGRHAgbWdXY63DRjPPuumZFBJ101D9IBQepDdaAHrirzvQ1G3JNAnoP8snsZrFhZ38ejOzywPF8KDkW7R6zUCXmF5ehMDgTv199QKV0DAdkDoa1G2JbJlCy8W1ERki_azUsF8QMmzU8WsiqDGE0hsdmWDDfa10BG1XNy9fxm4v7nqfItHU6rwDw0rMBRGQWMnYx0xY1qci2DnPF9AM6sZCAy-hV_C9Dsn7P8HNf1gDOsjoiX_s-3TLdQGE9gzO5mU4VggfZN6S64EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdfb514bfe.mp4?token=rtU9_rOWxYu47EISgoXhntrrWCJX6vSwRnY_RXjAe2wg5wZUGfyx17GPjIrQ7t_e1CqgwdDxOHPzZaeRkmtxoASn1PegiDrnsEgO2ud8KNM9axAX-e2qRXDiUIPWbE00S2RYfVj1AWgnMwgA04CPZ4W5OhZmgDgOBLEJbD28SDLQ2QoF-XeMvgXkj7bpCPk16oYtERInDi9um4RJWiBmFICmcahbvCkpmjOPwzc79JYunweQLTGG7q6YJbh3E2KN4A2piG1QLzb_NaQJXCsFz9QsUS7GR0oQ60TSnc4gkHcEJII8uzx_Bq5ghNYYM-nsSBP4ve5P2li6tew4CfyXySAreyl3nC0-vxfKV1KGGxCrpht1NBcfh-88LbqFrXXSCXOx0U-bvzPr71YMwYgbV-HZdbRRoXGRHAgbWdXY63DRjPPuumZFBJ101D9IBQepDdaAHrirzvQ1G3JNAnoP8snsZrFhZ38ejOzywPF8KDkW7R6zUCXmF5ehMDgTv199QKV0DAdkDoa1G2JbJlCy8W1ERki_azUsF8QMmzU8WsiqDGE0hsdmWDDfa10BG1XNy9fxm4v7nqfItHU6rwDw0rMBRGQWMnYx0xY1qci2DnPF9AM6sZCAy-hV_C9Dsn7P8HNf1gDOsjoiX_s-3TLdQGE9gzO5mU4VggfZN6S64EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
برنامه‌های فولاد برای بازی با استقلال؛ از مردم میخوان که سریع بیان ورزشگاه که تا ظرفیت ۱۰ درصد استقلال بیشتر نشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/104850" target="_blank">📅 21:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104849">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nk8LhyR7GZokUNSEqY3YDPvkzdf7zH5e6wUAG8YCUrlQJpzX-McwQ1qagiNRwElLCIBDo6TuEFkZjAq4KeDAdE23VcpNjIyKoyeEQ53m5d7OsyqOtHm9g_pfy7fTV29pvAbtzYkJADvDIP5BKUskpT4ofXZaJLypketGWM0cJICIQh7RUtCZVWgh4pu7LHd3ehsoyd_cFXizi1IBhtqg1XtFSargMMBJUvP8INv6WdQW1eFG1IO3kFgqnb9iD5wNGZyjOr_nJx4zI0ZGcTWdNQWxQYgmiiINw5-_hxANX0DLxntPrfaQ0PYTAOUU4tN4S00wuS6t_4CizO00GXo_Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
• امیلیانو مارتینز از استون ویلا به چلسی
؛ HERE WE GO
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/104849" target="_blank">📅 21:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104848">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
خیل‌مارین: رویای من اینه که آلوارز بمونه اما اگر بخواد جدا بشه مانعش نمیشم ولی به بارسلونا هرگز نمی‌ذارم بره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/104848" target="_blank">📅 21:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104847">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/To1V0A9-mMWeiHDGNBTcZnGtdEsHG_qeYxoTKswedSoBlZVumjPgGgZhkpLdO4wARKT4ivU6A73rQdFDon8-QdojAlzfeTwLDn3PfmO2T4OzzK2ETJPIsZrC3dySlkV4EbTZcnttjj_gJjQYHhkS1BnNc4OntwINmcJyZWjlAZSkjINyU7y3v9b1Z3Spugre9sDboLqLWeHqilOJ04uVQ0allhBWutKR3gcqfHUKHCmocdzVAGnWPIPzIY6XAYwrGojsYpGpZ4oEaDj9NMNG1kfj53Q_fQYZoQk-FryD3EfxxiJz7XpTqcr4CKU-0IgCt6lea_7JkVPcbxNRbwpYvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
معوقه هفته‌اول لالیگا؛ ترکیب بارسلونا مقابل بیلبائو؛ ساعت ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/104847" target="_blank">📅 21:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104846">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
🇪🇸
خیل‌مارین:
🔻
بارسلونا روح و روان آلوارز رو گاییده. تحت هیچ شرایطی نمیخوام با این باشگاه بابت آلوارز مذاکره کنم و قیدش رو باید بزنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/104846" target="_blank">📅 21:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104845">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
🇪🇸
خیل‌مارین:
🔻
بارسلونا روح و روان آلوارز رو گاییده. تحت هیچ شرایطی نمیخوام با این باشگاه بابت آلوارز مذاکره کنم و قیدش رو باید بزنن
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/104845" target="_blank">📅 21:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104844">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3a58dbdc1.mp4?token=Vbz1FlxpGlhziIVzbs6i04j9npdc0c-Z6sgdiCXdTotTnHFF_HvDkridLPqcXzvVbtd9LNHA5-Zcig1Or5ZyMhPw5ybRzzNVwex6ChPXy-_CL3AWJN-V0tUuaBcao2MuMRWmbt_rNW_1uzZ4CEgDkz7qXIRYKPEMl28-O8MAF2vHADCIvF9O-0kC94EQ0gqGNJkTlGlGE71VR6PcTBgwtq8jh2qu8VF4i77AS94K__d_I90gx1h094pPb2cq-E0Bruro7L1Rj0frMXE_I77hF22Dq63e0BCdQrjt20cqrukNxUDtbSNhOm1Lbi3Nv1zL0KK5sk6ncaOQI5JQPsMk1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3a58dbdc1.mp4?token=Vbz1FlxpGlhziIVzbs6i04j9npdc0c-Z6sgdiCXdTotTnHFF_HvDkridLPqcXzvVbtd9LNHA5-Zcig1Or5ZyMhPw5ybRzzNVwex6ChPXy-_CL3AWJN-V0tUuaBcao2MuMRWmbt_rNW_1uzZ4CEgDkz7qXIRYKPEMl28-O8MAF2vHADCIvF9O-0kC94EQ0gqGNJkTlGlGE71VR6PcTBgwtq8jh2qu8VF4i77AS94K__d_I90gx1h094pPb2cq-E0Bruro7L1Rj0frMXE_I77hF22Dq63e0BCdQrjt20cqrukNxUDtbSNhOm1Lbi3Nv1zL0KK5sk6ncaOQI5JQPsMk1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
🇪🇸
کارگرافیکی اتلتیکو دلقک برای معرفی رقباش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/104844" target="_blank">📅 20:47 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104835">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mirBymPkkAQegzmiFX93eN98FyzWA5bgEO1pdzfkzlIaAW_BwXQLPgWJOZDKTHCTud5Ijurl6MbrhldtX5jLue1D8mlvXeLc4GsBZDl4pJmqXR_K7u0ImaJ_TwEHMl5ukebz4wZbGeBxLl7mizFECqs7SRgibYSCHfwR-HiE_0qSsB_-l85evN-VI9ETRrlTAjzhnrAfuokvmJkdfa-8UMrSOXTuQGLdo4B4T1BE1W12dTIW4w4ohEcM-hmHX6JWpPaFKUjb7eikXFHH9i6WLR-LqQAqSr9_nVo_33O7cI67k9PGymzfqNPyLXDtoHWqh6-51SFvQ-0Doe88FHujbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/geHUqoY4OGWq7qw_G-HB03JI1ejrPgDiSr-YBXiUkfnWqMTJiHrkiCGoSQqSk9fVcdj1HG3hODCHdfB-Qnk-fvmML8Qk6p_35NJwb37zc7-CofaD9lx6nsw7Ei3anE9x2UOPDcMRfIqg6Syl6fMb2h49lwxxCChIXzSG9a1_tlTZzTjI-QI2HwKT-SIbOUFSEV9VQTQb2AohKtWLqGATReP81-2oB7XRg3FVehxf4th084CZeCXVuq_NueTXfe6RfsE2DTNOCze9V2tx221ZERj8p6JXE8P6aZhfQgLO4T3haUY4PS0hSPWqHwZ1ACE3kj8iZggPOEr-rxifVr553w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BLBeK6vXeefGlor_R1UgTgPJcX8uvi-X3wZO4xYLBoMnpPA7OZQPN2H_cfIBWwjQxST4nJ1DjrFQay9WjOa6y5_YcGPwGeMgEt1Js68biXo8-WEgAJaLraZU-Kt_pI7Rhq7Od0ePSWTdt7YkjzUqO34eJUEWx8LKmg22uYU1Eegyq611AK8KSiuf3Cq-YdqjhxvViBNin_xAJTOMZXqWr6XMVdRUkv6iWmGMQ_KNxgtRQXsAuoC9jCyW3bUUAsW0diIkL9oVR6SN1fCyWKAGjQ5RVn0ohfdllWZgWN9vwc5lX_6ODIZZh_klKWBZF84bR1h54YP4aerr2pJuiig_uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c52Sd5ynHl1qZ2_A9dijr151umQehPvkzht8jdMj6PSpGZsAtnl_aKvnVMFQubGPT1nhXraujgqZmcyn077msJfPcSoqpK_OS_-MFExQRtwPM0q8V24feP-UYtbLYVF9hfBhhxdvPIiWq3xlJgDe3A1pLR5UDHI_uZpC0LM9mdYtH2S_qioF6fuv-lSf9kThx9dBQKmk6miR5PU5_AT7zo8oXOKdJedjGrG4hHALar9ghgEHOVvFVUT98y8jqw-PFOlY_wr9IYlm40kU84KCPShSYOjOKZcpiQa-HohOrQYImhTmolbti3u4ogmsUEAX4sw_LYs66NFLzdNvJUz8Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oQS9NhQV1J90H4ZLgzkPVMzkdtcioJ7sMU90BPfTk-j2k_zi1ibL0gLGthpNUGlvzNcpAFaCupSU3NhiWCiUXx4CxJwmzKUARyNInI6--TFAkPV-R_pQ0M0sKaR2OgW2S55neLTNRhzTtlFPrRpuRG_qXw7IVdYuofIHsZT6h30a53z7c-njMdKDxqnBS_KoFEOH6eRaMoAiJzQqzaW1JN_r-rWff1al27kNEWYBxV4I5jYqXH3O3_se_o969rAIOCFe0nAlTQdF4UmhOoI8jtmt1SYg_Yf7PWNAws41rnMSw-wpzYp82LNOGfc3wBLx3HzaBdNb5YGnWVzvtaK_zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHGJ34wwDM6DVgeLBqQOj01nP-8sHa9xUJcCp5Xxewemv5dughYGMW_kWDGCPgBmHAkJMcwEThVvQVQH8IhUEILbci5ASxhzEHvrpFnbFek92F5YT6EznCkDntEasC7O3Bde_zbMMnA8OnV-hPQKjydFIva1U98xDsCy4iUEI67-KcjblG2rr4db9s-K7aGzJZ0zs8j7VhfDEQz4Rrgaw1hE12QuUXwwLlSv0IG8wnuDaeVKZinRxLEejwdmzSCn9krcEBbvHnTlVpXd0UIPQB71JDPFVaLVYyjUdv9DX9DmtIS-bEc-9RSBiL2GpWmVIKHvcY04yk4zbZsvO7989g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JZbl-DrP9bjXAjBAoY6S_hWZH1j7PG85phVgFfabnDyodgeNMkVpf2MD_z3fyedSftNoEOHDJ3Bg3TjKEyDBz81GcuWgb4epr3wryIOAMeZDje4a9ArpMmWfLiAUe9bA8cgx3e_NNC0ZB1aTdSrsSUDmJwJnj1PZNrtDQF_QjKfZ1VHHnyPhVJOS2zOt9xc62XspLNYKYsjiii4zPTUTCQetNC_T69fc_hyDEbJ7dx69TbyLL_QZ_elJaLWtCwJiU8x-5RPEuROeSWSIZXnN4Gru-oj5SbrMEedvm6NtMA8H4EuPtEkkcusTlb_lGNsXCwHXnaOysdK7eLFJlmf_Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZDjtfBMH2lIx0FhMsZnGapTsXCKce7JychNOF7CKsRBYF-he460anSpF68HcEEZH0Rk4KsvL26njeRQs1B3RsbdJ8WZl7ixoniS27VzvRG8jRp1fsdYNinRgQ4NhgCqWCjkNLOpaPs2UJD2GZ8DvCP2x-RpkXSqWc2gNe-8fv_0xeIufk2h-BnD57lWzx4ERmk_nWhCwNpiq2rscUc_dJXjgZHn2Pxo63YlzEeUFB1aJzQ9kJ6psAR3QWj4ei6I0YdTkNeMnRrmDbenxE9L8dITCFKJVx5-ZOwttRu409A48x5MgThZmyCU7qiSTghvKVOyXCnF-qkWbFWpcBBDmKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U-Ld9h3sgkwM3W11c0aVsQccba-oC1F-nV5r7qxtHpKwjQ_42uP24JuQA88l8-ZNTO57SUGoxjkW2jvri9xmaoUjmebza0PW4huAfRh8k9xhmlmoV6D9cpYQt67CK5OmarPzG-j89U_49tGMG81Cp2s3_Mk07n4kYedMZhFI4bo-wzWKNSDFiDHqfsZ1xbQ4LlnunddrYY6VT9i83WOvHCxSoLR7-3R4-uLqEWOZ5TU0Mo6GrcEXfJqIE9J00KB6R6CqPRKg_d1a0FlTKGlNBOPQjm_iT8T_YkHeQ27w-Ca9q00tlMwZ55O2e1UDe9cchE0VUsMs5Rgp3rscNjnwrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🏆
📊
#فوووووری #رسمیییییی برنامه مسابقات تیم‌های سید یک در اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/104835" target="_blank">📅 20:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104834">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQG_c3tisIXfKMBnk57kSy6CBdHVgB-3uxGALT8EIUkb8FNxEjKdcmREPiFjbIILczHkyDVr6YlLF-b0tMJLIEMUFjs2GddZmfqJPal2ohvtDwwSysOqCoDzp4-1ZsQSGBdKyldZi_KS32aCJ9NFZRNgq6Hq-PoFka07qpMPf3iEyoNIhiIvvgdIgdTU2itoLfVMnnr5CsvSWxqjnZd6JZuRvytNBHc4zjwrpTKQ_alACqiwaLL8EwFiDa2_ILA1yMW_clI1LKTxAqITsOFqSdegW-I3oXHxK5nzNgs176TTAGvkFqSCReO3xV-Gh5ujgLF20SiXSKqDPO7DKzofvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
📊
#فوووووری #رسمیییییی برنامه مسابقات تیم‌های سید دو در اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/104834" target="_blank">📅 20:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104833">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilodH_DimoEUPLkwRq7xbcZYDPd_aYsok4ccQp1B0G4dokbNtnEhTrebAwm_q19JxOyFd2-16zV0-vpxYk4PpRKPPA6TPmGoaadzszv--D0DmqGVVW7WBu4iRQAjA3_R-kC1RTpjjYvH-z7GLvj4TJtV4Z1LHskcqnQWxP1AzdY4pBiDgWTaL5cCCo94bhkvbt4EbJDRVeskGBvept_OuPQfPAZyLK7HhOwIRf7Bg1LTHwn4qL_UnnPa3YhD5AT0wUij3BdASJjDfc8hI1sB94-tPj2iHTR0dNHJhTF3Ob2PWYkrf72I8SiL8S1AFtYzSfACUZpQ4DUv45582pcZiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
دیدار یوستی مدیر بارسلونا با رئیس اتلتیکو مادرید در حاشیه مراسم امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/104833" target="_blank">📅 20:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104832">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVSQYVSJfj4DK5xMNzLbQhbWCNEv-TSf5Xe3rd1SSSE6d1ix_wCzdqiii4qJZxT2NfhVKXlMPbNVOpAkb1SJ-ESwel9SRY9IXZ_CufC8PQqZQojTt7DNaNqlKVsww9MIxO_o5kemlWuKDO9BtjTKhFXkGi9BL3vrB-5xr7iignkkWr_QFHoxvnLLiqtSyjQuibPuoxhe4ZO2XYMrYJKn5Ynt6_WYwChg1ItY8yvY3oq5ujFcWqlx8-Ux1RXxcNbqaeCoqYLvLeGggyW7SKRHbvDQ2xYOx9WbtCJpKMz4kXFSZKbXXATGjYeINZ3RlVo2lWRIHN-bc2nqke0GPRNK5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
📊
#فوووووری #رسمیییییی برنامه مسابقات تیم‌های سید یک در اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/104832" target="_blank">📅 20:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104830">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3Hf5y6wBlhXktQU78hy3qGoULauanbz-V3jiOcHrcXtFiXfwSDDtXrRXIhde8Aepc0g73HfayHUlhgNTA7NyGSaZVDG41pan1Raia1KR4-c4XfLe8lS6IahSx9zvgLMUr0nwKe4GiX9d4NEXlFLOvpOPMHdYomA9JEbx2OE4XGs17vkOrfGo804ejdmwJjN59lmMqEkYIi5pIuxGoPnlIC2-XRNzupYY9zbjPw_X5BZ47OUORKIb-ujzq435c_lmOQcsmV3dot7-I9-pM1xa17AbZFu-CTaZwYV7Lxsd390D0c0NUqzWxznJkgJnoIdxRFR7C8TfpH490kWEjamQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
📊
#فوووووری
#رسمیییییی
برنامه مسابقات تیم‌های سید یک در اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/104830" target="_blank">📅 20:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104829">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtlEekQvljLzI5ru5X9uL55d_zvGnro3u4gJP6e-hNapbDc6XkgOqFQp1QopG_E0Sygmrv1gurTOnY_2FyFY2mzpSkbuQ6bfHzkDn3d0NmjGuxUWz1rf-svzC2GVaEZCnLMRFxAUCDPP8cTJnW6OoKWJajfAadc6ZgkxTJYWUMtAo7VjH_h_rEooa3yY0Ei2JSDfbjwrLCH4YqRP8-AuPti2hNzn-0QgU2iNIcjztR0wkToAx8oqZC5kaw-DECV-HyCaukNbC0qOZRcz-_LxE3SXSbEsBX_2RXpOQ8WYMYMUUAKIHKCtfuf_LQvM0_FuWFWAf30a6-OKP6lZB8u2WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏆
🇩🇪
بازی‌های بایرن‌مونیخ
اتلتیکومادرید و آرسنال رقبای سید یک باواریایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/104829" target="_blank">📅 20:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104828">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jK68VIF1smxQg7_CY6ZuPHclX2JNwAoL1PIQdeJRKcwms3TwqeOZPARizIcznPsbTLjaOrPmlYZS8OVQMLzz6QYm-PqoieZtWElWxoDHA0kNusOU0wobXLth4ZW39_7i4PiXP64-hghfYnlqFWuRXLZkhWXPN-Gt_WBy8UFbV8-yurO1s1u3IRsfpZIqGoBdbVcMNv8aJeU3lnqHquC59M8cri2rxT496jiVtOLJiZUUnWtiPC3UiNFthcn_FgsE_wLG9y74pkJxYEprGX08pytCSExUFcZsoWYRCepEcCrhVmkxcPqmSrORoq4cxiOr8pNYtYJo2KHJ2XZf2IkMoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برنامه مسابقات آرسنال
تقابل با رئال‌مادرید و بایرن‌مونیخ از سید یک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/104828" target="_blank">📅 20:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104827">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9t-Ljae_Xvl80NY3p9LH6M9QR8_ScMvvoYA_mQlvp_RRNbgWwIDiUKb0cx_1t0uMHmPvgv4sP-vo7Jh0PYcfbtTogwh49YsCRC3S96ANxGQ7uwOnVax4rMWWfRXDjVz8P_awLpKJKBNQm4CPvZSjfxxwa_H5ob_kACeNSmclg6FJogrbIaNt6g5j_oS4CEmnPT8oNbAOQAJZHWdLGquSUrlJJf2KEhtfVQQr1QY-Qei1hT7S6gQsQ70w40OHTLkoPx6HSVk-iccm40dPjMecrUUTAK8p978RKcER4tYjCrFpvN3I_lRFSjgwFUg8ahj5j7Espez3QmaXdr25o5VgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مسابقات لیورپول
تقابل با اینتر و اتلتیکومادرید از سید یک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/104827" target="_blank">📅 20:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104826">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myLEPRPTznvwHob8LgY80p5nSw63-rJwPSw9cfF-Wi0U1Zugh7znMRqkQ9KqKngu8RL3YgGtH2AAIMaGujSuc28wuPdRYDj47TnlpGOh0k_56lUKo9B4SM4UW0yeP_u6MitXJ0SMNZ_eJiKBtaSdad4ymMOyMEH83XTtV-UTkpxhM4u5LA3Xe1ovOj4ABD213joNL4u6lsvjqNODXzhTO1uyiEfE4lVjcbRCwp14iMdH2iK-pxU4rAoOzmiOHET4r-Tz7kLbDQeR-V0DzGq4XEk-tK4xTQ6wH7cah0IDf-YjT5PJjE9wEBIJWXU9cCsofoLp9YcwLQzCvqSeBOxSng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏆
🇫🇷
برنامه مسابقات پاری‌سن‌ژرمن
🇪🇸
بارسلونا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی
🇮🇹
رم
🏴󠁧󠁢󠁥󠁮󠁧󠁿
استون ویلا
🇹🇷
گالاتاسرای
🇪🇸
ویارئال
🇮🇹
کومو
بیلاسترفیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/104826" target="_blank">📅 20:08 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104825">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qU0Oawwf8gde1Ic6j-7LJQXoI3QCgcdK9N24f9BdaCG9o-oU46YAsXSPUVNtIjgR6Pc8YRjuEN05phssiLzTIgieOx-pCCyOWgxGLQjr-s0b2ChALnv4lyETQssgXYwHj-tCEiq1ALJxtwxW9wI9Y1RbjAd_T2wIzdz9yL-GfbVgKWx8w2AmCIGeUVSNOYgupqrcmNLmY16d4J3rCtjRifJo7rbr3GCtfQ5BOzi4FPUesfg7ZE73UDGqaVk42N5417tqQK_qTaDDaIv22SlhbEnlM5epwvilmWnnE7r96Y_ofV0iJUfcCx_XLuGcrllKervW-HnuJjRJKjr0sSMETw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏆
برنامه مسابقات اتلتیکومادرید
🇩🇪
بایرن مونیخ
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستریونایتد
🇳🇱
ایندوهوفن
🇹🇷
فنرباخچه
🇳🇴
بودو
🇳🇴
وایکینگ
🇩🇪
اشتوتگارت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/104825" target="_blank">📅 20:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104824">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
🏆
بازی‌های بارسلونا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستر سیتی
🇫🇷
پاری‌سن‌ژرمن
🏴󠁧󠁢󠁥󠁮󠁧󠁿
استون ویلا
🇵🇹
لیسبون
🇳🇱
فاینورد
🇹🇷
گالاتاسرای
🇮🇹
کومو
🇦🇿
صباح
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/104824" target="_blank">📅 20:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104823">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVjSSSoSKLEs149PpkkGEIYUvX3a3wkSSguwil_69-X8F8f_RuekCiAG7ndFwvFWDHCbO4EWhy-AmEWOkiEKeyezE076dIYCDp5DgnvX2csMEsZDozirSFDL40_Nx4iq_FhCm4GeF5j6nGnMtJQFHBiC3w5bkuy8hkFw9FRNqbynHGECB0D50bMxM78lOLfTznEBMHK1IZUUIu25-rAPhfH4uAD8RU2rbfZxq45ojr5s9MnddsRg9uAsaNRFA9fsWrdyyv2QLpI-1LsONGv88gT7NIdo1Vx-6vLIHaKTEcqxE3rUU_ndNr1xsTr4mh6x6IU_95QiRqubWGscSxRscA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
🏆
بازی‌های بارسلونا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستر سیتی
🇫🇷
پاری‌سن‌ژرمن
🏴󠁧󠁢󠁥󠁮󠁧󠁿
استون ویلا
🇵🇹
لیسبون
🇳🇱
فاینورد
🇹🇷
گالاتاسرای
🇮🇹
کومو
🇦🇿
صباح
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/104823" target="_blank">📅 20:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104822">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpNDatCGVp29qdHXfdYv9dk0PKnnENebnnFQ6kNFS9F1HVT1s5Suoj4_5Ljv-LwSiypjQuQwutKHqsR5inwl35z7Ikyz0kqCV-KsRR_cjMhdfk2sA1fSJ-1_KHszxTY0eBgou_wBjZcIaPhT0i6GV1cqfYpgOcyReJBKdxAxlLUhcbk3d7Q7UTKZjg3qMjrK8d_F05XNK-fVC1J3GoWi_MWCp9ntj2lOo06NuqY2V8YcLUJ-j0N-81YlNjUOnGp0CQUGcv4MBhJo78MzJLB54CuGycqRgrpCvq6dD-07zrgq6f5Uh-jkRqYQZbFj5IsZYbWb8YYafXEkRMROLm-6jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
🇮🇹
برنامه مسابقات اینتر
🇪🇸
رئال مادرید
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
🇧🇪
کلوب بروخه
🇩🇪
دورتموند
🇺🇦
شاختار
🇳🇱
فاینورد
🇩🇪
اشتوتگارت
بیلاسترفیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/104822" target="_blank">📅 20:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104821">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مسابقات منچسترسیتی
🇫🇷
پاریس
🇪🇸
بارسلونا
🇵🇹
لیسبون
🇵🇹
پورتو
🇮🇹
ناپولی
🇩🇪
لایپزیگ
🇬🇷
آتن لانس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/104821" target="_blank">📅 20:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104820">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XR31iArSsaTOhQwnl4hv6vGJnxHsK8r1FLl6Xu3ZpYZXBzJX2Ng2v2jTosd_9A_kZiICFKbWaMb2bOGTyIBfKXgkVp5Hp8yxixoMuIbxlpqe0eCWOxDhlrvY0S747w4vF-mmEEdckSreemGXdvju8gCLtjJtH5bkWEVe8jatqOquAd3ifGt3hOarY9hc_Mdeak1yXjGDNRqNflDymUoCACQp7UXGwAllnOva98YWVNEjRGYkJSYePTKXjOBYhITaPJwq9AM6YDE0I1leVG-X60KYALdVNqPyA--8qMmOxN51j9HARgv_DjDViX7GB5ii29QAzOZDXP2Rdr1j4cqSOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مسابقات منچسترسیتی
🇫🇷
پاریس
🇪🇸
بارسلونا
🇵🇹
لیسبون
🇵🇹
پورتو
🇮🇹
ناپولی
🇩🇪
لایپزیگ
🇬🇷
آتن
لانس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/104820" target="_blank">📅 20:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104819">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8ue_P_FlVDUZsoB-wctALdmf36bjx0kAKUYmHn_wI8aWiPk9CU1b6zAsKeU76sFS9gcWstK5-Jnp2ppWPkXKa0pGQawvQ530ihmT6H7cSavHnOh8cMFTI-gvtcG2DYz6iUaK_3MIs26WAG20w8vfsHPqqLeKy1CUKsJDVw5p5EDum8aZvYk92i4u6WxuK5zaEPwZsQTfcnG3KIzij6BIKG6BPRY0cBcG2vK3keqbhUNOSBtezfZ-y-HWC4OSc5IMRiqGVtJMx3mu6W6uUooJbAih7Ldu5Qttpsz1nlQj7Ca9pcVBCQYPY4ysTMKofZCnEALwBnxZz14P5groK0h7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🏆
برنامه مسابقات رئال‌مادرید
🇮🇹
اینتر
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
🇳🇱
آیندهوون
🇮🇹
رم
🇩🇪
لایپزیگ
🇺🇦
شاختار
🇦🇹
لاسک
🇬🇷
آتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/104819" target="_blank">📅 20:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104818">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
رئال‌مادرید</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/104818" target="_blank">📅 20:01 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104817">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
🏆
معرفی تیم‌ها شرررروع شددددددد</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/104817" target="_blank">📅 19:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104816">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
🏆
#فوووووری و #رسمیییییی
✔️
سیدبندی فصل‌آینده لیگ‌قهرمانان اروپا تکمیل شد. قرعه‌کشی امشب ساعت ۲۱ برگزار میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/104816" target="_blank">📅 19:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104815">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nh4I-NhgKJuvKigTq8Fk3OodvFvJlHxIyhb-m69-prmSWqEbBSZHq8tJ4fOvsG6xU7IICyeAmuh-fqWdmgK-WKzyD7oUdJN3kmv6A2a1cI0lhOl5IDjXtR7LvXTmtJcdtE6bhZXYIH7fQiAuOSrrsVXqaIX91Kt7XiDLwDGg2oGOjjDUmyEjRgPOZZzPm5PVF_UHwXTG097NPU-iGAlvYQlTtKIkMEO_EepRoNyM77GtV5ZKzPe12uVKHVJPrzrD6J68z3Uj3z2hi1vW6Zsrqrtn6Es92Ui6Ec0PPLFNLzSbG-hATaTtrW9LrxqSgG_oTeh1ni5IfiufGsuILqz8Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
شررررروووووع شدددددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/104815" target="_blank">📅 19:54 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104814">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">⁉️
🇪🇺
سؤال مجری از دیوید ویا: احساس شما در لحظه‌ای که در سال 2011 با بارسلونا قهرمان لیگ قهرمانان اروپا شدید، چه بود؟ چه چیزی باعث درخشش بارسلونا در آن زمان شد؟
🗣️
🇪🇸
دیوید‌ ویا: در یک‌کلمه بخواهم بگویم لیونل‌مسی بود. همین برای یک‌تیم کافی‌ست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/104814" target="_blank">📅 19:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104813">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5te6yaEI9v5jC2UepM9fBI2N2Htvi0-M5nQZE8LaDBYEDrVDeAoiPG_FLKeYuXeE-3ACM5NQ6nJkP8OUe2lhgYltAnOJm-2GQxn2rOyiXYZ2If9lvshDsKsTbMOnRCATsnsl--KQIg3lrDH1w4wRVG5-QOd2o2sMKcF2WOXEzwC9bHej1J9lWXC1DSN-uXVgE1opR84eXA8YYrRRa1ax5pafs12dR8EgraHI3F4fPS7LTZPpuk0uJ7LFKR1JWy9IU8hV5k3xRKU5_q0X3SZSh5Z7tqcEUzm-6GCWhXoBfEE-eZRMWf6qEVFsywQlxhqyNdBUzBqoCqgd_8j1MvC9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇺
‼️
یوفا اعلام کرد که از این به بعد، صحنه‌های مشابه خطای هند مارک پوبیل در بازی مقابل بارسلونا در فصل‌گذشته، به‌صورت دائمی از این فصل پنالتی اعلام خواهند شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/104813" target="_blank">📅 19:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104812">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mvj319x6or-gm_JXuRmUkm-kWtnU9boDFbJE9cxj01Q_S8WMc2fHhqwafRPWVJYnMIeyvsN7CR5qukG5k_QBHGYIDJfqaXVefH58r4PwINrGuAm7dPrTz7bEKahG9GWiYwZWfA2P4mLB0tAy-jgAFFtybxKxYiXMTzpMYtIWjpoQlPfwYpYPRFVEMqxl6ty5oQVu7Aij5KAiUS5glCHpPneXaVY9xhhckVd4aUivLVs30YeerHeDZTR5MzAdWIstqsmVEkIoYmQ4cclCSWEXaUO2rCKdNwo0T09Fta2nKxb-Y_0nqLypa4g90_g22Dkak0RVQQ18cfzXe4-dz_4fJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیری‌آنری هم این وسط یه جایزه گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/104812" target="_blank">📅 19:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104811">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXyLDa-65PCXaRrBbxWobmM_aJ9Zkj-m5bRWpaKJ_TbY1ijDbJplWrWCHyoRramxrVgH4VZcBQeE-OMT10vMKK7GmR4aaVoTtZpfjD919hFFZUo340ZpvZU17M1OEYt4kxZZoq8EJzgy2hns-q_ZUrGSoGJKhUKmq2YELBrIq1qjDe981BNJnQ2K3y49gMVzhKzRkjfxpIbwjYKDKOSZLUXsE4CoYR1EMVjzS_O2rBFuztiaPS2SwonlPSNMkuDGRkXVn6v-fI26m1aOxrBiV_GrHTL_DSKF10Dc1Vcqpm-AEbtIT4obcwFYuPs_5PM2xmN6sRXg-aqEXLts8VIDjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇫🇷
مارکینیوش کاپیتان پاری‌سن‌ژرمن برنده جایزه سال از سوی رئیس یوفا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/104811" target="_blank">📅 19:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104810">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ps5TMB_O6ohUQrg1tQ4TcwwZTyR_SjEgnfv2y9I2-kEOlOYDEWKr6Qj8nZRQJ0JkjpFNRcrLa69-045Dd1aSizROLVE5yLSSj8D2Rc4L4Gx5m2rE_PfNQgpeF9xDElaETSbWTkQ7d223fkX8KxSHdsO4z1hogxEGJKSzFQA3LjjMQUDUDIkA_oNjzEanslxYlx1nAbDuUcsHCpjSSjTtNwAt4PkJ9D335EYMV4hTJYD8bSdLIhavPZgwYOoGcfwD543oM_kLhY3MAR8sJ-IUwvvc0H5hGBglVdqY_nUXpwuzl3lXnxGG9giUz5BVtTq4ELATNJuft5_M7iRS0yKSrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرعه‌کشی آغاز شد. با ما همراه باشید
❤️
🔥</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/104810" target="_blank">📅 19:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104809">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
🏆
#فوووووری و #رسمیییییی
✔️
سیدبندی فصل‌آینده لیگ‌قهرمانان اروپا تکمیل شد. قرعه‌کشی امشب ساعت ۲۱ برگزار میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/104809" target="_blank">📅 19:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104808">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ffeeffdde.mp4?token=sESmXfjwBhvxJ9bWdbyd5DEhfy7v0pByS485dU83V700s1py22-cVnNiShs7Qpn7iaosJBTaBd4T6yFpx7FeR_iBNX6899JepA6oBRTKo9KFA5RbVmTclXR2niyRgFYv7ujdMKiKMyl0TvF9x5WcuggDptgxuT14k79L7Z4Mpk6faE7T7cB6tsM11ajlRaYaVE5iUn8T-B5DT893sQT7F4H1jFDm-AU8tMNfx7dnWUI8MQ8ftvObrKZ_xNWHSkRE80SeSLegrmFdA0V6rKPGQ4k_SYrZZPMPax0UPxuGcM8pRbMw0dZYgz2bNgz7DRWSf35_Upe_W5dccssB7vXo_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ffeeffdde.mp4?token=sESmXfjwBhvxJ9bWdbyd5DEhfy7v0pByS485dU83V700s1py22-cVnNiShs7Qpn7iaosJBTaBd4T6yFpx7FeR_iBNX6899JepA6oBRTKo9KFA5RbVmTclXR2niyRgFYv7ujdMKiKMyl0TvF9x5WcuggDptgxuT14k79L7Z4Mpk6faE7T7cB6tsM11ajlRaYaVE5iUn8T-B5DT893sQT7F4H1jFDm-AU8tMNfx7dnWUI8MQ8ftvObrKZ_xNWHSkRE80SeSLegrmFdA0V6rKPGQ4k_SYrZZPMPax0UPxuGcM8pRbMw0dZYgz2bNgz7DRWSf35_Upe_W5dccssB7vXo_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
تنها ۲۰ دقیقه تا شروع قرعه‌کشی UCL
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/104808" target="_blank">📅 19:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104804">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Erso91u8UqfnGzCcEJIt4gbOH3xk5sR-kRFL-GwbI9uIsFxKqu4_GVpuwM-F2uewCRGt6Xdow-2dL5qqin_oVvzwiJGUDPdmoOvdMjIFTvlnxHfa_Wk3oC3GaW__QUnfXC_UmntKeUig4aw5_CRYHTwwvAcxYrCddyEfkGcXE-QYixnGW90RbhL3QSitgaJOsoS2rvqk5PE7qTXfi0LtdAn-MqAWZGTXt9yqEDeNUrlMBGlWgQU7XWVQS-1yZvS1n5slc-2cRgmXJUqIlgsunEhSd0Ulu12bArObnKE1Qd5GNzR04Q5jjyLT8xybCjk7aPAyCj82Y1RrY0oQVdbxwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sL888ceVL5el6H-2v2DM3R7mmjQ31OKyOdIlzNms8sdC453RCOUFdxA4U9GAcmtWR7SOMBFVNV0NDRW_Y5snAj5W5ZSoLSydDz6-c85FU-XFMOu_oc8tlTI0BxC_YqCKMXQ4YDuC2U-ojvnKw6FaNBEEJz2SuETccMXbubKsgz1u-Tb4lVsruiEA4QIFXpCNkecr9IzhlEyXVDH0mYrdtCTaXwt-edtRcpIqTenb0Vtrne2oaBAX2tQTi01hBqzvMgO9wXH_a7TTcTOavn9w1FZEyTYPjZNWkMp1Ycr4Sgxl52dNS5-pNa1qooJPu2nuLwPjElYe4o7FCl4dGZs4NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mXGYFhrHcFix9Se2bhm2qvt6Ls3lm4IIsaYViOJJ3jdL855Rp9R8krsbhdF2yWQzgb1mLZk7cInbZyLOM386g0Jq5CEVfcJeYin234tdmsPz1X3d_T1NoF3ataZSZBGElmFecX_5rFS7fEsUoN8wlECuvOVzujxDm_xj3B9T_7OPsBQMKjELBmMY-wxFZNOiFC13u0NuwkIXhpukoCc5yTs6VIj2OgO71rHLwQXwCuU0xj6dZ3CGZ_fPBz4At1B98wOcC8Up2GusQFW0MQJBoys9yp9v3P2Rlkw9liQ6qr9Ng83QxaTJrVXa-0L_h3RnpkctstlaNKy2RDW_kea8bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nAxGSWCvFyuTIkgdu-47c3_h-w6ma_YejL3NKZ6xUtsQvomqS_LqkR75n-qOME_iuETc-I6-So7gOhAYgK9al0D2KvWv3oPjJuqQgP1jRoG4svK5_h7b7qGcUlu82lG8-IZTTOFqmBnM8h20W1a2aosKpEfjApFN2Yxrnck7e1v-k6RfNCkMAF9uOT4q2MwE18dYQlnOcJLb92TIb5pP68LIqIF8jC1Is8xuTlhHVcPfXYwjQPlpldyKrJBsz5OTRdnMPdZEFWviwYsJpvXZq1CFy9jylogFJB13LisyjcBdmqtI0IlcNQSxsklfmdWGlXsI1ETaAhKOWyJpADSu_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇺
بهترین افتخارات تیم‌های حاضر در لیگ‌قهرمانان اروپا در آستانه قرعه‌کشی مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/104804" target="_blank">📅 19:08 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104803">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPvZpKs_3ZoEKx0uxX8KY2XJmbGwsxqN6yV7LHj0AlKF-wyNiLXriyqjuZAlnSD7dArnQJftIAvRhGesZmqSkMCYxYBBNNzJAhv5cNqXlLGXVvRmBP0MEYpp8yVvIv7qRIJGa8xFRp7CO5DHQD8uGrT1O34YUQ00eW4uQ04me6sop-QMMYdYqzykX0DK0tuObZWUOUvsx5_1gmiJVbHxq9IxQ3Aw6eugio12lrWLjPwUwBiu53Gd_IsYj0gDl0fbMHqEsSLXKag0QME106wpIlW-B3LGQSFmEtcwpifzX8UaM-Qh2nSVd56_H3_mzTa49utYwM4wEmL--kQKZ0jo_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
بهترین افتخارات تیم‌های حاضر در لیگ‌قهرمانان اروپا در آستانه قرعه‌کشی مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/104803" target="_blank">📅 19:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104802">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac7aaf7e8.mp4?token=JF6IZiQz3hliJdbVZacu9Ma3LX2KGQbryasnGx-VsgUlzppdjtV5PsPxE6Ej3ZbjnfxHJ-OSHK9dorDrvHMHV259aW2oi1rUOzjG2ekpLoxOAL9kcl45DJBZDIz-OAHldMIawMctU685uoZ8wMQ-EUP3qwKTfF7ntsEZb1eRg7hLI5nfP9NXtNYAXahFN_rEqsghfcOT_HB4VZpS_sNUnDjyJTwLbDiOk7FrII-_SVI7_VfYRudW_5R9allTwmjD1o09AztsticO7DZlX62ghk4S_MFgNdTWH1RzEmHuvXYmkqqyv0kG2gR__dA8v9uPU7qNpzTw1XijvgwJA0ht7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac7aaf7e8.mp4?token=JF6IZiQz3hliJdbVZacu9Ma3LX2KGQbryasnGx-VsgUlzppdjtV5PsPxE6Ej3ZbjnfxHJ-OSHK9dorDrvHMHV259aW2oi1rUOzjG2ekpLoxOAL9kcl45DJBZDIz-OAHldMIawMctU685uoZ8wMQ-EUP3qwKTfF7ntsEZb1eRg7hLI5nfP9NXtNYAXahFN_rEqsghfcOT_HB4VZpS_sNUnDjyJTwLbDiOk7FrII-_SVI7_VfYRudW_5R9allTwmjD1o09AztsticO7DZlX62ghk4S_MFgNdTWH1RzEmHuvXYmkqqyv0kG2gR__dA8v9uPU7qNpzTw1XijvgwJA0ht7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
آغاز جنجال در اهواز؛ به گفته هواداران استقلال، لیدرهای فولاد شدیدا آبی‌ها رو‌ برای حضور احتمالی در استادیوم در بازی فرداشب تهدید کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/104802" target="_blank">📅 18:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104801">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
✍️
سامی‌مقبل روزنامه‌نگار انگلیسی:
🇪🇸
اتلتیکومادرید سه روز پیش به آلوارز گفته که بارسا سرش گِرده و از خیالش بیا بیرون
🇪🇸
آلوارز هم از طرفی گفته یا بارسا یا هیچکس به همین دلیل سه روزه خودشو به مریضی زده و تمرین نمیکنه
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال و اتلتیکو توافق خوبی…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/104801" target="_blank">📅 18:52 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104800">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06afe0fc50.mp4?token=RSx1zFTvrwg9oT57rbb--nMV2YkoOzixqnCkegW5V-Gd0qIx5Uf3KhJe646-JXqOFIPkRqlaJapVqZJxE94Vp4w-BwuhGNYUE1Q_V5GQu2wkAM7vA1dFdly7Yc__ltyuIacLKVxKk4orFAR_YqaUve52CapLbYv734SeSge7Na0gTC4tZXYlmNW2ZhvBwSuLSJ85FDGRL2HF4UTY5b1Gt6PJRXd8jhxMmzcl_poKre-WCaJzWWwadOxzH7X6D65VDF1BWgbikOJ87ePYLXBS7vIVbxBERk2snCApPvRzk30VP9K2rmuEFk-kQ_FNJ-6ORiY95jo66QQG9jAUfGi8qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06afe0fc50.mp4?token=RSx1zFTvrwg9oT57rbb--nMV2YkoOzixqnCkegW5V-Gd0qIx5Uf3KhJe646-JXqOFIPkRqlaJapVqZJxE94Vp4w-BwuhGNYUE1Q_V5GQu2wkAM7vA1dFdly7Yc__ltyuIacLKVxKk4orFAR_YqaUve52CapLbYv734SeSge7Na0gTC4tZXYlmNW2ZhvBwSuLSJ85FDGRL2HF4UTY5b1Gt6PJRXd8jhxMmzcl_poKre-WCaJzWWwadOxzH7X6D65VDF1BWgbikOJ87ePYLXBS7vIVbxBERk2snCApPvRzk30VP9K2rmuEFk-kQ_FNJ-6ORiY95jo66QQG9jAUfGi8qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اختراع زبان جدید توسط علی‌منصور در الطلبه
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/104800" target="_blank">📅 18:50 · 05 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
