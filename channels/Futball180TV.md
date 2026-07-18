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
<img src="https://cdn5.telesco.pe/file/LJ5LzHDk-F89vV2ZrM8FrPBTz9I-WH3D28j78MFidbk1xrygZzcTtVO34i5TUqPWhaQY7s1joMUN2X3VEcwzp-aRCMLjhN9r20xsDX-Ilxe7XmxWUSmcXV5XMZXnus4AIBT_nswhmW9ZjijtXULLMzLXVL5sC4RzRGDxVI-aAkqPX8N8x9S3mxF-TuCVTPanZOuBOzQaX4EvFoRI3kHUl0U1iYmBRs0Czo74N2bTAGXsLUqS0q0FcSz_8TmzXQ-WMFqWt1dXEAKD_8Rc7yoOdaVLmvkHSIDrEyrDLs9RehCKnn7VkD1pLI6zMHRkajb83GF6_SeT1GhtnWvHssI9eQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 560K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 20:15:02</div>
<hr>

<div class="tg-post" id="msg-100770">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D9XppHfVa1UfZ4Gwlq8PMDUJat_9EMxtdM-uOp6OFQDbejz3vegf5vr02s8Pdbq13xWLirtuwiB8zwpQAxVjr25szhn0B9Z5z8Xk4PLYU_D2X8IP6IayCBvcUH0dmN3BiuvjEkfBcyHVNXfAxmroB47M9oM2VS9sptzl-okflta5UkinlV6u7lDhjl65YQdA--DvUBMhCHY2jbC75xaq8BzNWrpY3iTu6OgI719Xp6ENx2Ni-DLBd1CSdhWmofyZ87XD0ncrPd79McBufFNN1IEBbiEzxo9vXKozar6OozP-4OUlhvHmTGZnhWSSBXjPUzxT_jQAT7JdJOTfiZFEKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/smDcpSiSYq5prCq1XSWf-IF6neG8yShYMajWZskQqz5TDt_D3xBQDpLoBsGnrcAcqUhOdKxbn-ZRPoQYOP6wZ4OmGD9pIm6bMiLtno9I40XhguGh2QxIvTGCKhJ4z8-F5P1ko_v7kghh1W7DjvWXPRhIlRLBbENAkbeSKQsiQK6_KV8rmS3-0n9xKTq8XExycKR4lL35qP7V92ipPIEQVZSlKSsONQLxl0WEBBOCDkOcmQpnbZ1mA6VX5t4JypzyHvb23sA9IJe6J0Hn7lNu0fm4F_1cdunzAVTyKIbNfSNnUmTjIaN1Q4i8-jWP9ttWLJFDR8xSrYOYrgUqyJUkXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vTmgsbmVUrl8PcwW69PcWhO51YQwmqPdCOlGL0XeOjOWoWAoJo1yE0eQYFrVFE352QTOSdLewwzlfjEx54yfBxbwftigNdgvfS1Qx4L9PJ9xLbRSK9Hgim2heqiXWz32ST88_OL2fVOy6z92tvK-r-0QXgBD6e2_dQ8MiOd7sK0bADlzcZ_2xum9xtMW9b-N4Em9K0RAvUOUhYYvn8bWi1bECBBy7LD1uW6RfxyW3S6K_ypSew2Udr5Gqg6JwvHQLjoV5ZiDucTqQ3k3_Jg2oXKguVImjoN1hV6j4-BYSEX3BXvGZJlbLSnRU8WEf5CFvJPgDeKx9gfy7TRlDHUcgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I13pJeeP6HYF8xhdh3Gdk71zZbRiOIXTatl1le1HBsUqlvHCZq0suEP44gnsIk2p7TSIHSltznSfGHqZJkHX1ev9sVeH55hYfgiIRga9pt3FE6KNl_2QO0HcdaEZnHK0zHz7ZCE1wwAQ-ctVw9D4dr9rpAHB-XYf8VWOjN535BOv8e6B3yXSPrCUJJI2PAFU4ucEK2NX05kxEOyHYGwU1lZEsUgD6Owb7sxSp83agcje3TRAiHwjvqLz9XHPmktRA-pBwORxchvzbP8nUlau4vr1wwJeX-wcueLz_R7_WZFeYb6yHjgH055Isbge0vlEdpw9f2JNFWlMD7c2jr8xWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
🇦🇷
تصاویری از اسطوره لیونل‌مسی در آخرین تمرین امروز تیم‌ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/Futball180TV/100770" target="_blank">📅 20:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100768">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A86rOd1uZxGJOfJ0oHd7npssVWsfQnceXb55oy8YmeqA1RrDB9L9u6mRA27IhYvNJUb9XHks_u0eOBLAzYNC0NzMxtjPRxREsrBBB3-Qy14TNTAcgRSROXR6-JHcNLBAriB2oMdAeFLV6ilhbn4JE1aULnoLPtd0IuVG4KZlGacAWVoL6lEBKwwIz-drOsRJt36I5Z00xO5L6FsXyorbrfoGG5xJmMzzUIic5GTr4tjfMrqvwTx7VuvnMTcho8YInNJhmSkP40shMDWePTy7Ef94aCLwPc_S2jxF8dMqkqb_9JqqNiJP3lsL5oTdpwZgFp6iQQVRksD-NdYDIMNSng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/io_CI3YnafVXFQKYDMg9OkZBjTFeayIx7twqPXat0BFWkaXKVwsXMAIJYdSU6lqgfj7d0wlCghjZoyGy9XTJWV9-6MusGlNN8uXNve56B24J5dC47k7fxU8HmtiDXjXBAXxchFMsCq40X2YClFtcJ5n23j5oAS75Kc-rdn5EKL0hdxsHF81Cq7rsEYvXIsG5XhzqL19hBmjFWiCHe6yfEOc3yo3Q5eGUMTgzLcDEFK8uYxW4bWGFt-qTqTjVKHz85L9-5_YxfQ9NQV8esUiLpfS0O8pEHO9M8ZfC7PcU5-3bZBjSNzoKhtIXgQDL7kSswS-yPg3NgmvIA-BvhgoCtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇦🇷
برخلاف پروتکل‌های فیفا، آرژانتین تصمیم گرفت که در شرایط بد جوی نیویورک به تمرینش ادامه بده و با آمادگی به فینال بره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/Futball180TV/100768" target="_blank">📅 20:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100767">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/871184ae5c.mp4?token=Ml5QMnG2xcfYrk6t_91GXS1bKlw2PrKA1HRGDFPj-Y69QF2Kd_LEUcJvdCneCoh60x7YvK5SaZAhfT9_9d-uXyz0PYdYGYhmp2VMS36epQJoj1xnl6Ua6uCld8RKtta1L5pVVj-suEXeDZtfrRmSzcqNFeSQ3hzEC4zGAVcq8SK4MVVGxvH38gFRULfTi3a0F6PcFkMFoqUuG33uT9HLYio_aQs-7sS0qRjNnwpURVmevPsYz8B0zBAALtZQOj8k-jSW3uSc9cxiJDdyf2dkxXg6IlEpgtgkztIKI7KBb4TZWCeC6IRYwwUIeWEWbuVP2TkLJScpcvOxm2yU9WiuPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/871184ae5c.mp4?token=Ml5QMnG2xcfYrk6t_91GXS1bKlw2PrKA1HRGDFPj-Y69QF2Kd_LEUcJvdCneCoh60x7YvK5SaZAhfT9_9d-uXyz0PYdYGYhmp2VMS36epQJoj1xnl6Ua6uCld8RKtta1L5pVVj-suEXeDZtfrRmSzcqNFeSQ3hzEC4zGAVcq8SK4MVVGxvH38gFRULfTi3a0F6PcFkMFoqUuG33uT9HLYio_aQs-7sS0qRjNnwpURVmevPsYz8B0zBAALtZQOj8k-jSW3uSc9cxiJDdyf2dkxXg6IlEpgtgkztIKI7KBb4TZWCeC6IRYwwUIeWEWbuVP2TkLJScpcvOxm2yU9WiuPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
این دلیلیه که مسی تو این جام جهانی انقدر آماده اس. به گفته خودش یکسال قبل از جام جهانی برنامه منظمی داشته و صبح و عصر تمرین داشته و سخت کار میکرده، دور از چشم رسانه ها. واسه همینم وقتی هری کین با مسی برخورد کرد نقش بر زمین ش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/Futball180TV/100767" target="_blank">📅 19:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100766">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNaPHfHpjg4vQAqsqz6TkdXkQsZ1NmslYqJA62c-gTkGZJCT2VTPMLG59E7Bn8y3FzQSCxL-by5-qv1YeTWnQS8h4cWkUFfhIZMug8cUiYyVlZmwJ8mZO-7qxBcSOHgle9dLAi3az49cu04xG0Fl0gxak9xlD3xQF5M7FHOtNhlYxeWtvj8B8WLgvXKNlTz2gnk0BoGSseFRg4lDEBcIKUBVzVjYz-JUzcygJAr1VzS9JDDKgxWQ_NIwjsM6XeIOYy_UmnL85getNksvSwD8cick4U1i_NN9RkMXujpzU-5MXUC29dtIsNf6mg-bN9lijrxLA6iNgmPfTRl_WGhbuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
#فوووووری
؛ آخرین تمرین تیم‌ملی اسپانیا پیش از بازی فرداشب مقابل آرژانتین بخاطر شرایط نامساعد جوی لغو شد!! ظاهرا تمرین آلبی‌سلسته هم در آستانه لغو قرار گرفته!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/Futball180TV/100766" target="_blank">📅 19:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100765">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiZsuc3yQtMotYQvwY4Aa6gIgO1rjVia2L-xW63ZAHNYAI_IoA6-a0zmO7n1bIr4d1amp8UHRyLIZXB82Ehm-S4pfkmUgj0PKi2kfqzAAn11uFEQhFQINSKRrH9p2Sf5GvkN7__5O7dZvgi6YtJ01PjCtBO7BEpmML6J8Cyfxh6LKJR-iNjfthSQh-OnDOIZZE8V9fBKXHi4ZqD0jPPJG7Wm9x1yL-X-yo6mOIj3W2_4kD_vjfzd5eyHiGD4-PCDnCf8qNdKcSWmpdc4cH5Lj9l1ftBHdSllyjJK-dJYzC_tgsffkeZQVBxiTivrdMgc7mLoZe3RdAwhnYn7hv1n8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😃
🏆
دوتا از رفقای ناب سعید عزت‌اللهی تو باشگاه ردینگ انگلیس قراره امشب و فرداشب تو رده‌بندی و فینال جام‌جهانی بازی میکنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/Futball180TV/100765" target="_blank">📅 19:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100764">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6fa8f4aa0.mp4?token=mtX-AcenUpzwLE65W81patCUJeQ0gkr_c-_gMyyVpv8sUu74QaQAaTR1y0KN5cAFDDJ7hDLbJOqtXrPDtei1V1ixAj01NKzIFaPHo6DL6Lv621KtDRrw5QOZ01tAzw7jRyqYi5i0vMhAueF_xJLkjhkBz6rQZlqUzL2aEP5K17ieoanZlqM1meFFSGrg_C2W9AxNrY43c0fuQskVODWb7Znkj4zBEVulRDcCPuw4nbJolv-_9tODlz06DV6e43KmKrk8itM_zzLP3QGLpd9EegRWUTVGsU39pmn33wiBgw-Ae9VgL64PmrU33vO8xxyHDomDdpx3fG2MOw2ZC0BkVHIZ3RP8NnW2yhQAfjwV_j4DInwMbVyulv2Tx53UkYbAzPodT7E6ZDoz1_ya_QWsPZhqbCP4S3kJnHFa2vXeQzO8cKMkmSqVrwwat9_arsjQLwn7QzgAKfqzz7NicZW9LeKZQCHJPYaXKisXCvZUBvmNx89XOnQKPtv_o91ttAy2nOzNynJmhQ1ydIsJbcFnmLYvvBBNlHs9KFltCUAQaaw5VGGzD89-69T6XOSmFfBHAJe01H5mCiBTJOt_UNLlCv4Jq00FLVb-jExzjq6L-Yy_a8lBiV9dDK_8T-4d66ONPnYXK-xozQDgsQozzMe7rVEEsyRiLBiEnQh2yPv12ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6fa8f4aa0.mp4?token=mtX-AcenUpzwLE65W81patCUJeQ0gkr_c-_gMyyVpv8sUu74QaQAaTR1y0KN5cAFDDJ7hDLbJOqtXrPDtei1V1ixAj01NKzIFaPHo6DL6Lv621KtDRrw5QOZ01tAzw7jRyqYi5i0vMhAueF_xJLkjhkBz6rQZlqUzL2aEP5K17ieoanZlqM1meFFSGrg_C2W9AxNrY43c0fuQskVODWb7Znkj4zBEVulRDcCPuw4nbJolv-_9tODlz06DV6e43KmKrk8itM_zzLP3QGLpd9EegRWUTVGsU39pmn33wiBgw-Ae9VgL64PmrU33vO8xxyHDomDdpx3fG2MOw2ZC0BkVHIZ3RP8NnW2yhQAfjwV_j4DInwMbVyulv2Tx53UkYbAzPodT7E6ZDoz1_ya_QWsPZhqbCP4S3kJnHFa2vXeQzO8cKMkmSqVrwwat9_arsjQLwn7QzgAKfqzz7NicZW9LeKZQCHJPYaXKisXCvZUBvmNx89XOnQKPtv_o91ttAy2nOzNynJmhQ1ydIsJbcFnmLYvvBBNlHs9KFltCUAQaaw5VGGzD89-69T6XOSmFfBHAJe01H5mCiBTJOt_UNLlCv4Jq00FLVb-jExzjq6L-Yy_a8lBiV9dDK_8T-4d66ONPnYXK-xozQDgsQozzMe7rVEEsyRiLBiEnQh2yPv12ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
تیزر جذاب الهلال عربستان برای معرفی کیت‌اول خود در فصل‌آینده مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/100764" target="_blank">📅 19:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100763">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OT2qJq9IrTDCvbgrWHzLwvkaS-TkQTHQ-XuOPh5uTPCeCZv_6XdPzraQoGa1AKxJRXwu6m7YISBJIGq5DxbrnqDzVWHMnctA6qtOFVlGes3PyUP-17o024bSeBHXFtKv9nQRdja8iigvq4JYzco3KZgJjDvwFUrM-Ur6iGoWnc0cbLXuJfkORf0KMhQZyW4V0dKYCbEg3HOYDVixoGmFafLGibnQk4_jzfROurPGLXQkw4dYiFmhdr3VgdmBSAbO8MMwZ7doOdCoFUTljLVCu2LH1wBuik6CNeyhDJPoac1nEiN0-jqhloPSQx3oqmBSqIms5way-1BVlhrj0asBQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔵
کیت‌جدید فصل‌آینده الهلال عربستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/100763" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100762">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3cj8w8qDpvY8HfINKFkrWkruqSJA5UKSDdmfeQpoKXfRsOQTDB5JzyT81A9HAhftQpOYcSW253KDqilM_JqvN2090Y9zu3NPS7aWqmvVQBmiljDQTpPyB2nc0W1OIIfmNHpJiGVVhMkyGwJSk70SaY7PDIXRfqv8pjenbQtCSraWcDvCVMutJ0TPZLitDiGa_eBrQLb8AQXN5qQlfq1cV123R8de9nom6ddqu-UManGJ95u6auEz2ZrRddrrxdJAdYtwFjVAmR4QaB5XroSpMF0l9-R_FptL__N0XaLezTsllGhumTZm-nMegllQk_r7TdsVYwKzmG7IOKrNBKjpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🏆
جوایز فردی مسابقات جام‌جهانی که فرداشب به بازیکنان در ۴ بخش اهدا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/Futball180TV/100762" target="_blank">📅 19:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100761">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/778c75cfe0.mp4?token=EP1XhvMyqd97Y60ouzcZzpQwGeZzmlz1pTb8nxAviSmpVRiLucMJMm9gVeACsgi84z_z13nZCItvW-8-ZMgzv9vq3MM5yHIbr5kgT4RCSpV08LOXwuxZmMsJLDdg3XWk8ZO1Au0iqs7wCwXDuADXU1vtNvu080iHoHmMEXjcowX5_0Qefhe5s5AG0zhxwq6BYsa3yHhP0AKxmXykPMwXQb_z3UvOdou5Kx5nCxoQa-gUheKr6AeCgszA1sxKbEJ29tdQORv3MdUMBpYwEwVPFHERUkbqo5Ko2wiQlwD31UIPi7H0hImO5H27zgoDiG7fkk0IgHyjkUyUwD5FO82FNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/778c75cfe0.mp4?token=EP1XhvMyqd97Y60ouzcZzpQwGeZzmlz1pTb8nxAviSmpVRiLucMJMm9gVeACsgi84z_z13nZCItvW-8-ZMgzv9vq3MM5yHIbr5kgT4RCSpV08LOXwuxZmMsJLDdg3XWk8ZO1Au0iqs7wCwXDuADXU1vtNvu080iHoHmMEXjcowX5_0Qefhe5s5AG0zhxwq6BYsa3yHhP0AKxmXykPMwXQb_z3UvOdou5Kx5nCxoQa-gUheKr6AeCgszA1sxKbEJ29tdQORv3MdUMBpYwEwVPFHERUkbqo5Ko2wiQlwD31UIPi7H0hImO5H27zgoDiG7fkk0IgHyjkUyUwD5FO82FNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🟢
تیزر جذاب باشگاه الاهلی برای رونمایی از ستاره جدیدش فرانسیسکو ترینکائو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/100761" target="_blank">📅 18:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100760">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCA08WF3CQaAAePUDc56cOIBwHQljvi-1lmKzmp5h3_bNHmaoefstE1qoJpRw0pEp-8cPQQDBONKWvvER7x6woOLSIyPsUSI3SIpkc75cJFnMr8KfQsamchIqbSWzpDekN2cEHs-rmru5Ct6OaWbLafyxbZZKUpIbS2-85RD8tJ3jRDaCdZk4KD3JEZx2_LUtzwJclW1z-qgvLe-LGJ4QhWS2oXpaSBSn9f5UFHYX_U7u5699kTwFcNA1HLarLSr1qSeebPk9yXI9Uit8xoFKFwE_ByzVfWYgbChYea4GVmIh1y4f970xetONOJ8NSGcYAsWygFRxcd2HrO-RiggYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
#فوووووری؛ باشگاه الاهلی عربستان با ترینکائو بازیکن سابق بارسلونا به توافق نهایی رسید و رقم ۵۰ میلیون یورو به اسپورتینگ لیسبون پرداخت خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/100760" target="_blank">📅 18:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100759">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJGfkUu35HqfCvuYSb5h38UFU4QwXTxT4L3WkmIjF1qL2A60ohaL8Pzbqycw5qhDpA68DmWVbDEguPR6TNH4gfUE6Wn9vkcNoAc_WIQAye8KfHy6UHXuXia69Tb0_yC6PwY7UBrS8rnL8j532__Ll79ZRSLf-DDFiGqT58JG4U7euKLPRcZOk6qhi9WYO5oPj0jHTWOD5GMs57_VXntNW2PdgcvuqOnktKyXMIWpwwlo3Owl6jNm1XBf5FNO-KIEWp3lUf2bCpKSV6Pn0-rePKMHFe308vnz37_flZZ7_H_XRinuAA5cqu0Uu93YMlZZ4n9b39ooxydp64jgZBM1zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🏆
نوادگان یوهان‌کرایوف در آستانه فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/100759" target="_blank">📅 18:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100758">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLsV7r-TN1XINgBOL5Q6OiMxxq1Ob9k4v9zP4cTIWnMVDJ7vHBVf64pcWPfDHYeycjY7D6zsM-53jggCoAFoTofbqGHw4rjPIC1xVTFt7OYZrzzOfpjdY2q61Jitp3Vm43svejUb6AXVZSxxxmQ4r6jHw3oHDmkPF8Ur--FqjK7SErMa5X6NnVyMf3iNuUCjdna0R7DVw_uxIUND5yaX8tMzRdXJmZdio3RyozhQxQYSOBlau1Hz7hsgwPf5GJEQHOB8Bjhv6g5xKbIN9NRfCw0O94dBRALYR_45TkNavlaaQ682XzFR9KtQEfUwKQvHN5H-TDC8oxv2xeJwy33x_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
ترکیب دورتموند در اولین بازی پیش‌فصل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/100758" target="_blank">📅 18:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100757">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jV4YByk4rlQZSO7_Una20MJcr6AjdTGOItOy95ZU2KFdzdoNdw6TsS6w8Bz1o3x3-ntyPrVcX76KXLh6n0nMlHzMAZgSu8j42wjfm-SXRPIN2da54v7blNtAGH_y_R8xBM7oNIeNzlArFLD6C8uPVXZkJG2c5fGj_G_Hw0u3MQK2wU8S4_Ic5yU-ixegBzND4KAB1XJJI-gPoAqGih8MKkvjfkKXJAiboaf3kwzzpYXyBxG7m2bVLbiWxO_pAmTR7LrriZE-FhCC4Tm9agpJCNIotWnQ593QfFxu21O_JXexujCegLdee56NAQSqdrncBrZv2untgCDG6JhPyW5K1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب احتمالی رئال مادرید در فصل آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/100757" target="_blank">📅 18:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100756">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/Futball180TV/100756" target="_blank">📅 18:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100755">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=Q7djhk_Gw2KKkAWeR27uWaivVRk8tvUdoFO3WUgbyKWSOtl_ul2RPn7eNcwBEbjxSTbO91B1d7smN1sKTSS5YchiDcTziR5O8Vp0nSlurmB5WJsu9i9JksoDh_CDGpkN8zh4lugrl4fnlzPdUfPtp3f17f3vnJ5d4JLyBlr1uBG8FlOtyYHwpKolD5wLyAf-QG3Q1nE2Eiz2Yf6JFG5P06mLpj76pEuoIe_6NYZlAwGn1O_70knP6NZXBlEYdErglsCcGV7URQBKacttNv8HhMuMg6uXu9sIDcEbHeUE-O5jCbPAuLE1ZMnEJMpFmSsOgOGVFl14sxvGC2Lp9pdrpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=Q7djhk_Gw2KKkAWeR27uWaivVRk8tvUdoFO3WUgbyKWSOtl_ul2RPn7eNcwBEbjxSTbO91B1d7smN1sKTSS5YchiDcTziR5O8Vp0nSlurmB5WJsu9i9JksoDh_CDGpkN8zh4lugrl4fnlzPdUfPtp3f17f3vnJ5d4JLyBlr1uBG8FlOtyYHwpKolD5wLyAf-QG3Q1nE2Eiz2Yf6JFG5P06mLpj76pEuoIe_6NYZlAwGn1O_70knP6NZXBlEYdErglsCcGV7URQBKacttNv8HhMuMg6uXu9sIDcEbHeUE-O5jCbPAuLE1ZMnEJMpFmSsOgOGVFl14sxvGC2Lp9pdrpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌ جهانی 2026
⚽️
فرانسه
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⏰
شروع بازی ساعت 00:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.000.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/Futball180TV/100755" target="_blank">📅 18:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100754">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fanhDA7-nG8YXlalKEYZgrjEKTrGeVUm6jeMvCUHXYAhvBJDpY7KipS4w7-q5vCwnN2IGqqIev1zj5G1Hx75EftIEs3hkOeVo3ru8rHPNvzhfHCI3gRl_mBzReaIEmu63fjtn2_oPRxFDb2XS40NrlrTXhWKPc6yoLxv7yy6YKMFP1-U1viwPDgB6sELw32S6f5BEFjSkzGqaAjv_z-k2Ox4a6hfmB7HHNTWPlceLL72s6FIF8XXaldbtoxvksNGNedcLxeeUGOoullgwmaSbY91293MxVSHvp_32wHhQg79o_O3q_3ICf0luOISmX6FH33eO5_s9d6rnbD-JE1Pig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فکت
؛ از سال 1986، قهرمان دوره قبلی جام‌جهانی اگر به فینال صعود کرده باشد، همیشه در بازی نهایی شکست می‌خورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/100754" target="_blank">📅 18:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100753">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqDXUchLyPmM0pF49QO6BG1Y0kc8BuH1T0zmEg7PBCY3rruQrj6qEUb1TlaUQVHM1mLXveGyjhiz0GKUBbzk5pJrvLO2NB2O9P8VLVBV5OL6gEeX-010wKh3BHXiPbzdQ8bZNJ7W1TnmeFNt3IESFl-eE9uIzQjuJHe3MlHFyuofZ7ObISk7zgjGv5dlLk9LvJlKi4RRjEDxRhvbRjEysOxvLznkk-uld8xVBZokM2x922rDiHXPLGWH7Ddqu2X3ouPhQZ4CnJnN0qwK7KH5PzJB12egGSdeSbpNTaMM9TR4H6eG8zkMmva0pVUWNBAeaFS0W7Kawb7gTKqeUJSs2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارش جوایز در «جام همراه من»
واریز ۲۶ میلیارد تومان تا پایان یک‌چهارم نهایی
🔹
پویش پیش‌بینی جام «همراه من» فراتر از یک سرگرمی، یک جریان پرجایزه است. براساس جدیدترین آمار، تا پایان مرحله یک‌چهارم نهایی، بیش از ۲۶ میلیارد تومان جایزه نقدی به حساب کاربران و برندگان خوش‌شانس واریز شده است.
🔹
در این میان جزییات پرداختی‌ها جالب است؛ میانگین جایزه برای هر پیش‌بینی دقیق حدود ۳۸ هزار تومان بوده است.
🔹
البته موارد خاص هم در این لیگ پیش‌بینی کم نبوده است؛ بالاترین جایزه برای یک پیش‌بینی دقیق به رقم ۸۵۷ هزار تومان رسیده که عدد قابل توجهی به حساب می‌آید.
🔹
این پایان ماجرا نیست و طبق اعلام برگزارکنندگان، ۴ میلیارد تومان جایزه دیگر هم تا فینال در انتظار پیش‌بینی‌های درست
جام همراه من
خواهد بود.
🔹
با داغ‌تر شدن تنور بازی‌های آخر، رقابت برای کسب سهم از این جوایز میلیاردی، وارد مرحله جدیدی خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/100753" target="_blank">📅 18:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100752">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D8FjAXviWtUBbYf7fMtKRVpjLudQhk7MbVYyRc74vFgDvCN48lMIa0D140nsZWfOJ1_t9wY6rF6B00g0tufnh8-W4hXrxtGhRW7Ob8SvC9dW4UKpUj7uSMbZCav1NDrfGpt74yqVjYiESVzB4e9rwEwH59dNEJHOTAnc5va8JYkioXdVm5-PAHobhp0pKgFnC-y1sBJlcLamYa3G4uOfnP3sIVrvE2DOBGBb9DkmCaT4SxLAVmIwal5IRSqPKgg42FC9IUrhWsQi6KZGDTxrVc7NkcluHmW5lKZKkbvTZ6FqfgYNUqbkOB6YQokQfhR1W_Zl96qSYt-W3Ft_IDurmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🔥
🇦🇷
استوک‌های مخصوص اسطوره برای فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/100752" target="_blank">📅 17:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100751">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVu7FV3I0ZDUbKf9zqHjHhgaLzMkml-FJrvEl7iDv4hzgCZumUVY-bvCpa8pe5RT__b6Gh916kkPTM7Cp0yUg0hEJZEKay4BOWwbL2SUf0r8JN3PUjRNQeDFkfFvTAWG1AqWFVGxWO0ySLQL4SH78EotK3Fi_EplfTmF-MQlD2f_Xbvr8JX7E21a20maeq8G43Gdq8QMBACroZGjMZGlnqghivcrVYKcAGtIRew_fk8N9qiz9wvRjZ1tUgqD761EsHlWkzEpgXx-ENjNQqrLLF6FLyNKFogyH1iqhSXPksU04fq-V86WXjLMXmAaV1u_IlpqRhdF6mC7rULlNGQykQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مسی از نظر آماری بر تمام بازیکنان اسپانیا برتری دارد، به جز یک درصد بسیار کوچک در دریبل زدن، که در این زمینه لامین یامال از او جلوتر است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/100751" target="_blank">📅 17:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100750">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qj_jvljXqt5EOnDDDhh9RNuKz7jToseO2DYZGLk3BPrxeex235hLR-6SH27ttdAT3FKO_UW6cOrinHn1b8ZDGn-ZzMwusBNtJaQPAGIRQID3QWe6mF4skw4v7VcaWHTHAMhbFqcCsWaKXTYDAGTdDlybzxrjTgpx6fydgdkiF8GIzpxjcySSLwLTG-Zj7lepk1aK1hF-Y165Ae4zWI-j1Ns_IL8ocT36uIiutZNezhawgyWj_BaUeNxyMq2DL0VTPzq9kYq7c3FldF_Kdt5wyAXUlnsO5RH79QgD691X7WiW7GD5ngkYzkilziLOjxlW_BvwXZpAQeLb58BaoED_FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مارسلو:
من اسپانیا حمایت می‌کنم تا قهرمان جام جهانی شود، چون آنجا زندگی می‌کنم و برزیل دیگر در جام جهانی نیست. فرزندان من در اسپانیا به دنیا آمدند و من 20 سال است که آنجا زندگی می‌کنم. علاوه بر این، پسرم در تیم ملی اسپانیا بازی می‌کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100750" target="_blank">📅 17:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100749">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WX0-HW6FhUM2RcDjazy6eIiEXF7NjFleSPOez5hko8hxbyjwS-PgDZ_3hC7ekXHfOViAUU2t5mexKhmaEnC9iLuc-y0zd6pZUhgNGOPtn0uUzW8-XXHyyLxDDOuNG6dWu12a_BYVbsJfzLjCg8g0ooS8ZUjy933BdA7YwNk0e9KRsyQgl6lWzJnd7nmrEX4RGnd9v_v97Fx-4LLmHMiw3A06daSQiNM1vJGXTJC9Q70lVOMBBTkavaj6C8qd_SSwVji6lSeZXAXYjw58rDrZovPvhz_QyFztVv0z5y-Q9U25NUyCfv82uIZG0sAEQIIdwTwA9GLzTNT5r3rdgLx58Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب منچستریونایتد مقابل رکسهام در اولین بازی پیش‌فصل شياطين‌سرخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/100749" target="_blank">📅 17:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100748">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaDkDE9dUp1u5_WqtAUcvATw1nHteWgrZZFHtfcFUWT7-fLboaR5ikeOmy48ABObPF7ntIQj02R5HbbyXw9GFfYEibvswGQF8Z2aABH3PbbYfmEnxmd7xMkAk17VefqMi6wLqk3eQvTcTRHVBHzhCMV2rTbG8I5--YPuZJJFeIFcgeIuNS5IvYvmODcrW9AJyglmzpf9jG1pl8UX493kEyC8uWfW3MzxhFWBHgLEjXfLfRQbXVWnpMv_Wq13-vWQW5ywvf1SyCNzJR-v7HWJUFmWS-Cy4LcxTkpLIDtnPi7Q1_oSK-3qlIyMvAMPV4ryfKYeRt4ZxooAEUu223DI5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_فوتبال‌180 #فوری
🔴
🔵
برخلاف اخبار منتشر شده در دقایق اخیر، باشگاه پرسپولیس تا این لحظه هیچ مذاکره‌‌ای با کوشکی و اسلامی دو بازیکن استقلال انجام نداده و این اخبار برای بازارگرمی و مختل شدن روند تمدید قرارداد این نفرات است. گفتنی‌ست که آبی‌پوشان…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/100748" target="_blank">📅 17:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100747">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2480fbbbb.mp4?token=MRwg1v1vQO5YkeB5izGiO0I69xP6YUH2XLIW2bbVCSSyAsUKSWq1nALxUIrJl8hqLY0611wGpax5oj7hcFXFzFmYPEFlBE8X6lyt9dGBVxHVuFXeblFqSxY29FoQpuXZwWQqmLTbUcO5596eCpDCWbUDWxPQ8glP78j3BZOdEt9fCI807mTMOutRpH0LUhdEcEM-LF8wmYxDCSVUrgQz94TSN6qMvSvDkmpVcXlPB8Jq8jN8gW0irStg8q_nMUAf9S2knzqWcGKV165JZBXYxvskcmlSEHznpyJjDb_J3_ONW-Qio1VgGFrFRex0dY3XpnUewBv-tEaFmG3QlgICJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2480fbbbb.mp4?token=MRwg1v1vQO5YkeB5izGiO0I69xP6YUH2XLIW2bbVCSSyAsUKSWq1nALxUIrJl8hqLY0611wGpax5oj7hcFXFzFmYPEFlBE8X6lyt9dGBVxHVuFXeblFqSxY29FoQpuXZwWQqmLTbUcO5596eCpDCWbUDWxPQ8glP78j3BZOdEt9fCI807mTMOutRpH0LUhdEcEM-LF8wmYxDCSVUrgQz94TSN6qMvSvDkmpVcXlPB8Jq8jN8gW0irStg8q_nMUAf9S2knzqWcGKV165JZBXYxvskcmlSEHznpyJjDb_J3_ONW-Qio1VgGFrFRex0dY3XpnUewBv-tEaFmG3QlgICJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
انزو فرناندز که حسابی هواداران آرژانتین رو مجذوب خودش کرده
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/100747" target="_blank">📅 17:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100746">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc579a6c5c.mp4?token=CI8Lcq12DyGkwkazArXbqLSwrsTj9Z7DJwJ5XPXg_rgbeMEdfnQ40b9I5s4OGrFpaO8ZHKcQAxuVpw2PJ8mqGYQ-VU6B6N5rcvSWHB63kaUPQ1DoJC3t65-iCAngsZ3CDKpI5bJCzi0Aifb2OD3gIp9CAnrS2EfuQXa1auGHOU7w24JV6d9fo4R-IkHmdRknQ963vZqNqakGYEVRJAoBaFd2N8HxsyIHa24sCQ1a-DQWYjqTqHoxfgACwi43anmBFPZrGO-XcL78sehNczwgQw64uPFDX6Kauue38AmoSKG-nrEWL0d_Ps3VcTBXCcJl3VxvMZapDjvFrvm_WzEYuZTnQGsfF3diCRRT5X931mxWzbcUABZDdl8n6Z_SRoiQkMaOywkfOwkvTSd-iO0oEE1RXroqIBrN3gzvFbYzNvsaWTnrDf3O0XLrYSut6u6ndpXhdzsW24b_BjNRpaRNg0BHffQAz-NKas5Wd5teYrr8uZT5jG679xuvgSNxKkvkZMcC4dxW-RMEeO3fVmt3i27x_G2wr_3BW-cLdIq83kF-6zCX-dx1PaafnNaewljKrIJlv2d6Boy_CaHyZOiVwssMnem3XaI0hIQtbyeDlOhtSK1OjJQaPssVp7HWwbyW4E4B7fQvRdKy4km__GiZ5q27AhDSv6hDZB9H8bP8Kik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc579a6c5c.mp4?token=CI8Lcq12DyGkwkazArXbqLSwrsTj9Z7DJwJ5XPXg_rgbeMEdfnQ40b9I5s4OGrFpaO8ZHKcQAxuVpw2PJ8mqGYQ-VU6B6N5rcvSWHB63kaUPQ1DoJC3t65-iCAngsZ3CDKpI5bJCzi0Aifb2OD3gIp9CAnrS2EfuQXa1auGHOU7w24JV6d9fo4R-IkHmdRknQ963vZqNqakGYEVRJAoBaFd2N8HxsyIHa24sCQ1a-DQWYjqTqHoxfgACwi43anmBFPZrGO-XcL78sehNczwgQw64uPFDX6Kauue38AmoSKG-nrEWL0d_Ps3VcTBXCcJl3VxvMZapDjvFrvm_WzEYuZTnQGsfF3diCRRT5X931mxWzbcUABZDdl8n6Z_SRoiQkMaOywkfOwkvTSd-iO0oEE1RXroqIBrN3gzvFbYzNvsaWTnrDf3O0XLrYSut6u6ndpXhdzsW24b_BjNRpaRNg0BHffQAz-NKas5Wd5teYrr8uZT5jG679xuvgSNxKkvkZMcC4dxW-RMEeO3fVmt3i27x_G2wr_3BW-cLdIq83kF-6zCX-dx1PaafnNaewljKrIJlv2d6Boy_CaHyZOiVwssMnem3XaI0hIQtbyeDlOhtSK1OjJQaPssVp7HWwbyW4E4B7fQvRdKy4km__GiZ5q27AhDSv6hDZB9H8bP8Kik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⛔️
علیرضا فغانی: اگر ایران مانده بودم، صدبار خداحافظی می‌کردم
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/100746" target="_blank">📅 16:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100745">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e993550cde.mp4?token=I6V7MdgF5oSAkQDx8AjQSJp5iltqtfF7ZPbQqrwX14TgDgi5LMsdyHUWj-bs94qkIsbbercO8Glmv7QwfUfZj-SiyEe-n9nPO_akqMFufWVq4190BEQKNVU7ne8RS7lVib0jU6jbCtnH5pSJm-K24ktO5l5vfRcGRK5CGATDVqEBbffenda0YXVOC1EiNcQ0YlXwMI2qhJaZskQsYLUfhOnHmbn_UEHexCeovR4B1CEspnYEIANRs-5NqWRa4O87UEdJI2Uht-A547j4iXcONs8-rAgYe6zPxyuXIy8-cAt4gimgH9li8zCV5vmvaZTLz0P_PJAjtHrcLHKca_x7BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e993550cde.mp4?token=I6V7MdgF5oSAkQDx8AjQSJp5iltqtfF7ZPbQqrwX14TgDgi5LMsdyHUWj-bs94qkIsbbercO8Glmv7QwfUfZj-SiyEe-n9nPO_akqMFufWVq4190BEQKNVU7ne8RS7lVib0jU6jbCtnH5pSJm-K24ktO5l5vfRcGRK5CGATDVqEBbffenda0YXVOC1EiNcQ0YlXwMI2qhJaZskQsYLUfhOnHmbn_UEHexCeovR4B1CEspnYEIANRs-5NqWRa4O87UEdJI2Uht-A547j4iXcONs8-rAgYe6zPxyuXIy8-cAt4gimgH9li8zCV5vmvaZTLz0P_PJAjtHrcLHKca_x7BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚠️
خاطره‌جالب سرمربی تیم‌ملی اسپانیا از تقابل با مسی زمانی که سرمربی سویا بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/100745" target="_blank">📅 16:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100744">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d4aefcaa3.mp4?token=e5mQ_0SXv6pLRMxVRy1BbCCYJRr0WgpajNSVzQs0xhz71_Lpomkm3A-tYdwNQ7a6LIZqmxlNoA1Qsz7CgjRm4qYWXdqpMAtEPce-_KBVYRQlvmSJ7ZZva7uaYCpmSbqhcJjHqD27d5jRreLNXKdf0ZD5Poy-oO7b5ZhNeY3DCXZkk7RhymOkpkUudHP2EE-5npu6G-LVHdK0sqGnTgPCz8N7dEs8-Qesi7DoR4ZGgWEUh3w_ZLSTK2mnX3lc6ZJiPV3erkfuFQW6kat0skIrxyJcVcnZtiGS3DPz3-yhogAq571Rf-0rAND0pDW8fuwOEtOKU5Yn74ipugg0Dya3zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d4aefcaa3.mp4?token=e5mQ_0SXv6pLRMxVRy1BbCCYJRr0WgpajNSVzQs0xhz71_Lpomkm3A-tYdwNQ7a6LIZqmxlNoA1Qsz7CgjRm4qYWXdqpMAtEPce-_KBVYRQlvmSJ7ZZva7uaYCpmSbqhcJjHqD27d5jRreLNXKdf0ZD5Poy-oO7b5ZhNeY3DCXZkk7RhymOkpkUudHP2EE-5npu6G-LVHdK0sqGnTgPCz8N7dEs8-Qesi7DoR4ZGgWEUh3w_ZLSTK2mnX3lc6ZJiPV3erkfuFQW6kat0skIrxyJcVcnZtiGS3DPz3-yhogAq571Rf-0rAND0pDW8fuwOEtOKU5Yn74ipugg0Dya3zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
هواداران اسپانیا در آستانه بازی فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/100744" target="_blank">📅 16:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100743">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34b9470b1.mp4?token=a9yQxRbGVM8TbRh39_r8e7gX03xo5ocO-n6ViCQWL8kLR9-aB7Kew_QYFgZlVAsetN3yNg_Sd_SRPToUxVNlRlKhfPeg_UIIGx7zbbczPfa1IABNS2KKuP0FVxNB6rDkDmPwy6X2Aubt1bx3s_Th7vCaaWi1Hp01O3R9o4l1bkBRGTlrkI7icI42oznwpVw00zfhFc_LDvRVuAgtbsp5d2R084UMrQihpRN3_fz66PH3OXe4W8JuaxdiFGEaS45xddbvxpeedDc95K3WdyHcO0l2kAG6NflIxZrFZKkhFYqtE0Po0IjCnFrC5GibOYDUaAJxV7WEug6dGlh-PRjbFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34b9470b1.mp4?token=a9yQxRbGVM8TbRh39_r8e7gX03xo5ocO-n6ViCQWL8kLR9-aB7Kew_QYFgZlVAsetN3yNg_Sd_SRPToUxVNlRlKhfPeg_UIIGx7zbbczPfa1IABNS2KKuP0FVxNB6rDkDmPwy6X2Aubt1bx3s_Th7vCaaWi1Hp01O3R9o4l1bkBRGTlrkI7icI42oznwpVw00zfhFc_LDvRVuAgtbsp5d2R084UMrQihpRN3_fz66PH3OXe4W8JuaxdiFGEaS45xddbvxpeedDc95K3WdyHcO0l2kAG6NflIxZrFZKkhFYqtE0Po0IjCnFrC5GibOYDUaAJxV7WEug6dGlh-PRjbFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبت‌های پیمان‌یوسفی درباره چرایی عدم‌ گزارش بازی‌های جام‌جهانی از صداوسیما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/100743" target="_blank">📅 15:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100742">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94776f3b42.mp4?token=bc-VVU_8o19laN29ll8NbfLXDWhvM-AxgAY3teuN2vQ8rG6LkCTeRnTP7FbXH76KDIFaZ_NBDww9_3RBYg7AJvLJDxQQ-zHK-AzSGb-UwcZVZyyVlpZ7ULmM66y_KjeYWNUsYTw2z_D_ihyDuW96lvXxEcHJ2txgZaCZdlFe8hVs4lxEPtVgBD7tE57yfClswrOLYU4nxs905E8N0uyYtIgyCVQCHJe3JLqTmyTAN9Ax6KgziK203vlvHzGhydsR-iAcvQBx5JKSBNqhPo-OqA6ND2toJDdeysJZsoavN_-YbeHj0RPNTQnwWgkxiHstbmOT4PNozSVNU991i9dLcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94776f3b42.mp4?token=bc-VVU_8o19laN29ll8NbfLXDWhvM-AxgAY3teuN2vQ8rG6LkCTeRnTP7FbXH76KDIFaZ_NBDww9_3RBYg7AJvLJDxQQ-zHK-AzSGb-UwcZVZyyVlpZ7ULmM66y_KjeYWNUsYTw2z_D_ihyDuW96lvXxEcHJ2txgZaCZdlFe8hVs4lxEPtVgBD7tE57yfClswrOLYU4nxs905E8N0uyYtIgyCVQCHJe3JLqTmyTAN9Ax6KgziK203vlvHzGhydsR-iAcvQBx5JKSBNqhPo-OqA6ND2toJDdeysJZsoavN_-YbeHj0RPNTQnwWgkxiHstbmOT4PNozSVNU991i9dLcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😔
انتظارم از بازی امشب فرانسه و انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/100742" target="_blank">📅 15:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100741">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJuE4lErvwBka7qS79oWXgyEPavJSW9MhDCxm7MLNm_o-JisLwuK4ehdGj8gF3SL4kevCQfJsyhGVrV5D5-Y6HQVi5eqaSCiVFcJGv6tVbWSpK7FHeWtjZiJBi52DgaIfqHXtygplqBjMvnjhlvLwyo5XN2OT6lpVm7OgMFmtRF-aH2tglPKT8a0iXfM3kYzLK-VU33kFrJoD4q7196FPWzFk3Wf1GOvB7LIdyyjGE__gskS34FQdnTyhrxGW9avegMCyvfl1uAMp5jMLSTQqRqGbGKR-ZBy_kB6BoJrtAt5zySE8C_WCwkeDvjA7Ld_w-9GqPJPWwPJbPuuIMmsdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری روزبه سینکی که بیرانوند و نابود کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/100741" target="_blank">📅 15:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100740">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtKWfEvde-ay8D8S0flZ0jHHC6Gdor3OFWw78UKtWSL1HmsnMRH4FEZL3Z736ueE4-jWOaQrSqrgq-kKRCt63GRcyN68DazzL2BJYr_JB9vYSUZkyJME4oR5wPM4lMGFigXanBBzn5HRg1O54UjJonOQCUETHEok3yFE1f-T-ZlOxiCr-WKjTbaHbooTf4MX3oToomkVxUiiZOrXOErrBlKabC-EJ6AAzd7IHIe8sRLy6eDBzVapsfR_27oHEkgSjKpYg7DhcuKm9IQCzzk927925adyQV4am9E3_u1yFQCELHkk2yhqpyrXrvzNdKSiU-Jj-tF1slTxjGWSY1ePFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100 روز تا مراسم توپ طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/100740" target="_blank">📅 15:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100739">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/100739" target="_blank">📅 15:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100738">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=bCwte3RW8Uo-9jVld1DYu-BOege90u7GhrA-Ts47U9LZSfGvx-1_mLpSqD2ztKvfTvQXUs0YIF571peo-eBUwvaB1UwFQMsC5zx1DjeAKfA5TXprh26oTLloUtK0gbsTKNcvH5eSk3dlZjYOMXJfY8ArAGnguT8T_kuUGIUUv2SPFKC1ocWmGql6LkFagBtQV4I_dnKAkhD0ElXPiMwqy4kQrMJvujgV0wnZ7md52CW224XAw9QG5__qdqFsTqdqf7Gmr6kNl8FUs1w4khKlw09yoF9sZZqIpqvsJ1yfIuwyRRfdEk5P1wySDuu5b5QUgZmc6vzNn4bwQKgJV0ENQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=bCwte3RW8Uo-9jVld1DYu-BOege90u7GhrA-Ts47U9LZSfGvx-1_mLpSqD2ztKvfTvQXUs0YIF571peo-eBUwvaB1UwFQMsC5zx1DjeAKfA5TXprh26oTLloUtK0gbsTKNcvH5eSk3dlZjYOMXJfY8ArAGnguT8T_kuUGIUUv2SPFKC1ocWmGql6LkFagBtQV4I_dnKAkhD0ElXPiMwqy4kQrMJvujgV0wnZ7md52CW224XAw9QG5__qdqFsTqdqf7Gmr6kNl8FUs1w4khKlw09yoF9sZZqIpqvsJ1yfIuwyRRfdEk5P1wySDuu5b5QUgZmc6vzNn4bwQKgJV0ENQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌ جهانی 2026
⚽️
فرانسه
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⏰
شروع بازی ساعت 00:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.000.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/100738" target="_blank">📅 15:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100737">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9511ead233.mp4?token=RXpHaeMMPCifXHLGPKhT1Cciwgc11H3okY0ynGCgBmwNq-bejDmXWRimFIcIitGh2J-PQj8ZztAs27KzsVNdNK5HG3-AZW-isUQYvPq_DTGHcQGOTcCSiJay24bjnK6594XD5WD988F7sORbFwmFPvjzkhuZNkSMaqdlzYAgE1TayEJ5-P2wvdd3O2E9S-D8EdI9dMoJ_3uqH5UoCRu3OXVDTZED8FjJhtZ2Y55_7QbWPJMDxsDrVITH9-M-MX5_1G7Xy097FMW8eeLaI2WF_d2T9-Mb1OyMIk3LSlfeF4zCL3GfCbZXMoQJ4U3z7HG5BhetT7eBGIsPgIRA7tvaBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9511ead233.mp4?token=RXpHaeMMPCifXHLGPKhT1Cciwgc11H3okY0ynGCgBmwNq-bejDmXWRimFIcIitGh2J-PQj8ZztAs27KzsVNdNK5HG3-AZW-isUQYvPq_DTGHcQGOTcCSiJay24bjnK6594XD5WD988F7sORbFwmFPvjzkhuZNkSMaqdlzYAgE1TayEJ5-P2wvdd3O2E9S-D8EdI9dMoJ_3uqH5UoCRu3OXVDTZED8FjJhtZ2Y55_7QbWPJMDxsDrVITH9-M-MX5_1G7Xy097FMW8eeLaI2WF_d2T9-Mb1OyMIk3LSlfeF4zCL3GfCbZXMoQJ4U3z7HG5BhetT7eBGIsPgIRA7tvaBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
▶️
پپ گواردیولا:
جام‌ها خوشحالم نمیکنند، تجارب انسانی آن دوران که در بارسلونا، بایرن مونیخ و منچسترسیتی کسب کردم، حس خاص بودن به من میدهد.⁣ در حال حاضر هر روز صبح از خودم میپرسم: آیا دلم برای مربیگری تنگ شده؟ و جوابم منفی است.⁣
⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/100737" target="_blank">📅 15:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100736">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b0b7dbaff.mp4?token=j3WPh8QH6eRdJUSBGMEmli_1_arlRhTihvd4aPwo2UD54InNR-mKoVdTaS4BYPCM3bwtZQk4vqyXDg8mt2lVTzZ9S0bTpMZPymGD77J4-AmLetoww-sFpxyCpfAXrUu6ETlAvFjazAosLs7uE5FLlFwnjGfuQdtqP9G9xFjyvZ6mcXQFYwb85UM2wiOhJgL_Sua8EKjALE-9BMsoOYej0PtyZODVcDxsQM7mQbW_IrrO8e45ZAwKt4ARS63g8WG3xcIGXQHVbpySkHrZXGwdCJZmY9ry6ZD5mdTu1vSq2AWgfnrT1noO32WdM-4g0BFOSZYQpVhgH20VhKkn0FkUKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b0b7dbaff.mp4?token=j3WPh8QH6eRdJUSBGMEmli_1_arlRhTihvd4aPwo2UD54InNR-mKoVdTaS4BYPCM3bwtZQk4vqyXDg8mt2lVTzZ9S0bTpMZPymGD77J4-AmLetoww-sFpxyCpfAXrUu6ETlAvFjazAosLs7uE5FLlFwnjGfuQdtqP9G9xFjyvZ6mcXQFYwb85UM2wiOhJgL_Sua8EKjALE-9BMsoOYej0PtyZODVcDxsQM7mQbW_IrrO8e45ZAwKt4ARS63g8WG3xcIGXQHVbpySkHrZXGwdCJZmY9ry6ZD5mdTu1vSq2AWgfnrT1noO32WdM-4g0BFOSZYQpVhgH20VhKkn0FkUKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
فقط یک نفره هنوز داره به تنهایی میدرخشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/100736" target="_blank">📅 14:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100735">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4652c3d86d.mp4?token=AN-8rxOKwBrfzJ5XK2STAVuyu4Du4zHhaRz9eidKVlB397A91oLXz_MjYkKqNWMmvU3V02-9FxOM06zndBhtxWSbSC8z7__onjQt737ZDLJUN8yCVXEeXSrUnBiRBb8UPGHo3WahZoTn6oJVlaGwxipPzHsEpV8aDChuP3W3BcALw75WNaqYVWI2TLdbC2kO6uyTf8j2hl1wG9Wr_6st4bPQ7lvLsWpSwhIuIx2ax6K3IOKHqB43sZDMyH7fyMf6dYI50yNOWf7HWHFBuSxsVwi5-iNjKcc5hGjYL4sDyHKlBgi9bQ2TXdFe_V3GQG7oBDemghou8Tn56gq4ipBlJjIIqqEy74lAbFJtlrK9FYJtyI6i7TkpfhRLjwttcEoC1cdwFHDN8ZegCB6JBB-ynjXYEoz4F9Tf4DPvQVGSak9uAreMGzq6fruUwsq1rDGRybp7DRt4v3hf8VEAtmBhtJDipmb49OUe4b818Pk-GRm7CAn-tI9KnxId8-yLNQSbBN-iZrlg0CyYsoSuvidg4UHgEAjKiHO6PLuwA7iP41dqXXKJUTzXyx1uNk8QhRSZJRs0JGcljLScRSqcgeSNIb7u0ChPAetn24C2E7LB8h2K4cmiLEl5vhVM0ha-3sK9tSrmiYpV5vPjSEfp0KL5433A8-EmlRLfnd87WQw1MXU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4652c3d86d.mp4?token=AN-8rxOKwBrfzJ5XK2STAVuyu4Du4zHhaRz9eidKVlB397A91oLXz_MjYkKqNWMmvU3V02-9FxOM06zndBhtxWSbSC8z7__onjQt737ZDLJUN8yCVXEeXSrUnBiRBb8UPGHo3WahZoTn6oJVlaGwxipPzHsEpV8aDChuP3W3BcALw75WNaqYVWI2TLdbC2kO6uyTf8j2hl1wG9Wr_6st4bPQ7lvLsWpSwhIuIx2ax6K3IOKHqB43sZDMyH7fyMf6dYI50yNOWf7HWHFBuSxsVwi5-iNjKcc5hGjYL4sDyHKlBgi9bQ2TXdFe_V3GQG7oBDemghou8Tn56gq4ipBlJjIIqqEy74lAbFJtlrK9FYJtyI6i7TkpfhRLjwttcEoC1cdwFHDN8ZegCB6JBB-ynjXYEoz4F9Tf4DPvQVGSak9uAreMGzq6fruUwsq1rDGRybp7DRt4v3hf8VEAtmBhtJDipmb49OUe4b818Pk-GRm7CAn-tI9KnxId8-yLNQSbBN-iZrlg0CyYsoSuvidg4UHgEAjKiHO6PLuwA7iP41dqXXKJUTzXyx1uNk8QhRSZJRs0JGcljLScRSqcgeSNIb7u0ChPAetn24C2E7LB8h2K4cmiLEl5vhVM0ha-3sK9tSrmiYpV5vPjSEfp0KL5433A8-EmlRLfnd87WQw1MXU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
صحبت‌های میلاد‌کرمی از کارهای عجیبش در صخره‌نوردی که میگه هیچ‌ترسی نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/100735" target="_blank">📅 14:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100734">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf5731dc1.mp4?token=OKCQA1oJanT3uPh7mTcXqbhq1J0wc-Vr3p94EBfOZr_WusEo-53LOIy14NCT28Mx7DBWTxOBvtWw21M4fQvxuUxDMYfvg3DPFmK2jS-nDRv-IN0oW6qu5XzApx7BnDxIWwglN5FLpqBJVxTPwYpRUlTbcPjIDT8rF-svG2SgzpStIUDMfDTxIqUC2aNyqioGA0REVLCx31PkATRMo3DIAmWirAbSmbX5_ql3PZSMHIJE-t-hSlnWga5heFA5iDVxMqeD9ksqy4M3UgQKv2dJcdW-EojLtVxrhBiyTKdZaujozGlctcshjFElexnFhnK0Hl0Jl3FlY0-_-yAZ3etP4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf5731dc1.mp4?token=OKCQA1oJanT3uPh7mTcXqbhq1J0wc-Vr3p94EBfOZr_WusEo-53LOIy14NCT28Mx7DBWTxOBvtWw21M4fQvxuUxDMYfvg3DPFmK2jS-nDRv-IN0oW6qu5XzApx7BnDxIWwglN5FLpqBJVxTPwYpRUlTbcPjIDT8rF-svG2SgzpStIUDMfDTxIqUC2aNyqioGA0REVLCx31PkATRMo3DIAmWirAbSmbX5_ql3PZSMHIJE-t-hSlnWga5heFA5iDVxMqeD9ksqy4M3UgQKv2dJcdW-EojLtVxrhBiyTKdZaujozGlctcshjFElexnFhnK0Hl0Jl3FlY0-_-yAZ3etP4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب، قلب ایرانه
❤
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/100734" target="_blank">📅 14:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100733">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80daff883c.mp4?token=G3NAvRRgs9rWHX3XbJKl2TMgftitm9BY13YosZo2lmxdqZQ-ciHZIckWY873fw2KjfiuDCKEfsUxhwg7JMO3xI381fcXd4_rRujLqwPA34-llT_ryYmHsCcHxC8phODZWJijfuhfwqTDzXg8jTc27LgA_Po80kSMvkFv2-Hz60Ch6-ZJ1r2EmVH11YNdVms07_ENP89mStuMlqEwCqTm4puhidtjYZpGiMigYBhKf17vB0F4tIuI_Osr_V7yiWwKpnX7IsykkFV5j6O40LUBb3D21V73OBgPwBqWADqlaq2GdIe4ala890NB0Jt568v-CPmbU_vtzsxVhf8x3nRq9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80daff883c.mp4?token=G3NAvRRgs9rWHX3XbJKl2TMgftitm9BY13YosZo2lmxdqZQ-ciHZIckWY873fw2KjfiuDCKEfsUxhwg7JMO3xI381fcXd4_rRujLqwPA34-llT_ryYmHsCcHxC8phODZWJijfuhfwqTDzXg8jTc27LgA_Po80kSMvkFv2-Hz60Ch6-ZJ1r2EmVH11YNdVms07_ENP89mStuMlqEwCqTm4puhidtjYZpGiMigYBhKf17vB0F4tIuI_Osr_V7yiWwKpnX7IsykkFV5j6O40LUBb3D21V73OBgPwBqWADqlaq2GdIe4ala890NB0Jt568v-CPmbU_vtzsxVhf8x3nRq9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نکونام حرف دل میلیون ها ایرانی رو زد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/100733" target="_blank">📅 14:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100732">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f306dcec7a.mp4?token=PMIC_VludABHU6_BdeUPF6UgcKGlxlGysVxXd07QCRXYhcDD_crminismRA0NqVCWf_A5c20W58znqifk0dTCqEaHhyl31GQMCMhyg-26CpaousIHpq-PCnEdSfnNX-zIAWC8Qh0vhZh0IB5LGcHT2eS7UHlruWG2oPeg5zC_h9jU80MwcyoHZyBRWAhJHsuL1zg0pLWVzdJSLz2GSH3BRTW1i05v7TROagNP3l9zXtsvJNoA9SysrQevDzROBXmnh2WuSNYbbuDNsk9bwTCdTbj-SxY3ulJEjguoBs-921ki37LeFMLFT4d-X5yEfqGtL_3SGaQvaHKrn3-8calySY3vBj9-Ys9JodsSBWqLxrY9KN7QKxCIEhjp6u3JKTSeh-54JeIRvtzOYwKpzL51K49r8WPsMJ_VKrzjZZN5yjhs_WkdN14DtntOlr1Yj-fieDPXhutuMktNivIug7_Jaj-t1NffNTF2jpwHVzqaX6EJp0bfoSGryffS1Frf2qKKxPfvGlvz8Lxn15Jfaiw2xekS-OJFcI9_1MkDgnMvjZJkqfOcLI9UQiATRAKe1n7EwZmEtK-L4dg5JVKGk1sjj6v8EcMll8wMf42Ynv4kasYDV737WTkWzfpIGKJYeu8txbEK2IDZtAsUecwQdGvj2zzeAYr7HbOf2NcocsBg-0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f306dcec7a.mp4?token=PMIC_VludABHU6_BdeUPF6UgcKGlxlGysVxXd07QCRXYhcDD_crminismRA0NqVCWf_A5c20W58znqifk0dTCqEaHhyl31GQMCMhyg-26CpaousIHpq-PCnEdSfnNX-zIAWC8Qh0vhZh0IB5LGcHT2eS7UHlruWG2oPeg5zC_h9jU80MwcyoHZyBRWAhJHsuL1zg0pLWVzdJSLz2GSH3BRTW1i05v7TROagNP3l9zXtsvJNoA9SysrQevDzROBXmnh2WuSNYbbuDNsk9bwTCdTbj-SxY3ulJEjguoBs-921ki37LeFMLFT4d-X5yEfqGtL_3SGaQvaHKrn3-8calySY3vBj9-Ys9JodsSBWqLxrY9KN7QKxCIEhjp6u3JKTSeh-54JeIRvtzOYwKpzL51K49r8WPsMJ_VKrzjZZN5yjhs_WkdN14DtntOlr1Yj-fieDPXhutuMktNivIug7_Jaj-t1NffNTF2jpwHVzqaX6EJp0bfoSGryffS1Frf2qKKxPfvGlvz8Lxn15Jfaiw2xekS-OJFcI9_1MkDgnMvjZJkqfOcLI9UQiATRAKe1n7EwZmEtK-L4dg5JVKGk1sjj6v8EcMll8wMf42Ynv4kasYDV737WTkWzfpIGKJYeu8txbEK2IDZtAsUecwQdGvj2zzeAYr7HbOf2NcocsBg-0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
صحبت‌های تند پایان رافت پیشکسوت پرسپولیس علیه علیرضا بیرانوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/100732" target="_blank">📅 14:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100731">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa83d99e99.mp4?token=cKVgnYyktirG7oskayB93BAnZ3r-0VvsF5wsMBAG8WWI3YVD-m-YJz8v1Y2GD1xBbAJia-PQsSKhpQD6Z1esPgIdukzHGkOW33rqVav2mrdUs6rS_B6s3k42-wMjIRPc5AX9Cr_thA2v9xKhv7UCT1la-mItThiP6Uap9YBsOc4zVvdWIu8-jIYqTQuQZwlun9jSJV266TxLNFsEmY8Pa1vJXpEpqh3nVyQBHr4UCZQV2AvI0nufUoI0Tyy_4wbCMYFbkPQise-YEYjzZ73ryOllcIzGDJaVd_zTTX-C7v10QbFvnLNoPsN3pdsncyvUSfEJEBht4RHC-Bf4LXqxSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa83d99e99.mp4?token=cKVgnYyktirG7oskayB93BAnZ3r-0VvsF5wsMBAG8WWI3YVD-m-YJz8v1Y2GD1xBbAJia-PQsSKhpQD6Z1esPgIdukzHGkOW33rqVav2mrdUs6rS_B6s3k42-wMjIRPc5AX9Cr_thA2v9xKhv7UCT1la-mItThiP6Uap9YBsOc4zVvdWIu8-jIYqTQuQZwlun9jSJV266TxLNFsEmY8Pa1vJXpEpqh3nVyQBHr4UCZQV2AvI0nufUoI0Tyy_4wbCMYFbkPQise-YEYjzZ73ryOllcIzGDJaVd_zTTX-C7v10QbFvnLNoPsN3pdsncyvUSfEJEBht4RHC-Bf4LXqxSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اسکالونی درباره مهار یامال: بهتره توی رختکن حبسش کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/100731" target="_blank">📅 13:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100730">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d64bba4d4c.mp4?token=SECiJBREK9B8RoLWgFTVGSqjNJIEZNLigV1MVQeWozSXeN9oQx1fZL9indROEcR4LBajB7g5G6yWQ6RzXpycSuveJ_4Vta8HvVzEXe6tv4ChLBcmVmiAy8MK1Qn0fByCFh4siKma6r3nNMmnGnFh2jP65BMLDyx5i7BPNjmVRyFDHAF4thuypqBqoa1UaYRJLrSkf7BlnBo4DQk1C66VLyf167NbhxS_w591dTBOzCiWOTld0gv9uM-adOOUXZb71STOFLiGA6recoh3o2LRhzlc50oV0PQyPhNeNyIMNDs25v6v9JHEDSjruVjbjYsufLacrkwkWh2YjDVu8MFTOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d64bba4d4c.mp4?token=SECiJBREK9B8RoLWgFTVGSqjNJIEZNLigV1MVQeWozSXeN9oQx1fZL9indROEcR4LBajB7g5G6yWQ6RzXpycSuveJ_4Vta8HvVzEXe6tv4ChLBcmVmiAy8MK1Qn0fByCFh4siKma6r3nNMmnGnFh2jP65BMLDyx5i7BPNjmVRyFDHAF4thuypqBqoa1UaYRJLrSkf7BlnBo4DQk1C66VLyf167NbhxS_w591dTBOzCiWOTld0gv9uM-adOOUXZb71STOFLiGA6recoh3o2LRhzlc50oV0PQyPhNeNyIMNDs25v6v9JHEDSjruVjbjYsufLacrkwkWh2YjDVu8MFTOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🏆
استادیوم‌های جام‌جهانی یکی پس از دیگری درحال کندن زمین چمن‌شان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/100730" target="_blank">📅 13:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100729">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_r0AtnwUSXcQ5E422YydksIEmMA8qlNzaQUOte9e7H6iZt_NKg-VCjt2a2k7a6z3F_QdriwfwND4tlJKYN67WekFwGrIIa2RpmIy6gnhnJeuzLHvlml3EaaHKy5SXqKL4yE05Q6Z5zmNp5mJcPHfwIai5aIkMnEQMiMPOi_Pa2qQX2TXQ2_PClfMRw42eNP9IbOTvikz6DqALDdJd7HXT7UAFVZsdviI_w8e9xkJi8mwEV3jD8kWNtJ7l7Nm20CdPZZAhllhXOpYHf0UkVwemeioJqDuVG0XZ7q8n6i9S2tGlQVKmd0n_fi6snuSmsrc4PD2-SoLzNM7beIKUoPuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
طرفدارای گلزار کم بود بلینگهام هم اضافه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/100729" target="_blank">📅 13:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100728">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6593b1cf82.mp4?token=etJ1X-69yr3WE6sJwZax8wQWvEDGeM5oZLmnHcf8e7xPkb0hha5nN54i4VZhjfp9Pz3aj3Tp0qRIx_jNiWQe66_mGCE8WElK110KnAXqTytohORkTkm5EOGsjZAkVyqOhJ10r1jasPNIviIJ0fEbRkYWetH7d02--oNyetjoPMgUzYUqZ8zmJUY71kM4TMM8fU3zx3jXnd3N2rQ8sX8WL3OSthgouRf_pKQFk8IMa7jON8BCrNRg9pfp2TADP_LGCtFHglDuuEXyHih-o3lCMiA3LevCbgadDOhjbO9WOMYr7nDzQf_zWe1W3pCCiaNIi3LPi1cbIWHo1_kgqSrmmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6593b1cf82.mp4?token=etJ1X-69yr3WE6sJwZax8wQWvEDGeM5oZLmnHcf8e7xPkb0hha5nN54i4VZhjfp9Pz3aj3Tp0qRIx_jNiWQe66_mGCE8WElK110KnAXqTytohORkTkm5EOGsjZAkVyqOhJ10r1jasPNIviIJ0fEbRkYWetH7d02--oNyetjoPMgUzYUqZ8zmJUY71kM4TMM8fU3zx3jXnd3N2rQ8sX8WL3OSthgouRf_pKQFk8IMa7jON8BCrNRg9pfp2TADP_LGCtFHglDuuEXyHih-o3lCMiA3LevCbgadDOhjbO9WOMYr7nDzQf_zWe1W3pCCiaNIi3LPi1cbIWHo1_kgqSrmmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🎙
جان تری: "برای من که اصلاً هیچ‌وقت بحثی وجود نداشته؛ من هنوزم معتقدم مسی بهتره، فارغ از هر نتیجه‌ای که تو فینال جام جهانی رقم بخوره."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/100728" target="_blank">📅 13:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100727">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cdd66519b.mp4?token=lZM66hKKaR8BvHYrpFfDpJ9rbcj1EgEidJrhP4OyKucbV7Hev4X5BCBVXj5l0nqhBzupCQzeboALzFaFVBqOg7EOkMrnlP8tCg92WCaVoHiffu-ARkvTZ9pw9NBpc-i8jE_9MJ9fAVPgyhAixryIMnGqX1EWRD9rsaH7q4d4-6iRk1tVaJly9v8TdemHhSTrUyjF2wibm3dUjb1ZGIj2OFg8QyQF6N_RMIH5sTWGD3zqczkHrerSH5MQVSnh34XtRuvJJFd-aazSOrBaHZcSjgIKYPbrGokqBAVk0k9Xa8ssnkoxyolZEwvRAFF5Ian9aAlwbkuUKYpBSvYWP7l5AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cdd66519b.mp4?token=lZM66hKKaR8BvHYrpFfDpJ9rbcj1EgEidJrhP4OyKucbV7Hev4X5BCBVXj5l0nqhBzupCQzeboALzFaFVBqOg7EOkMrnlP8tCg92WCaVoHiffu-ARkvTZ9pw9NBpc-i8jE_9MJ9fAVPgyhAixryIMnGqX1EWRD9rsaH7q4d4-6iRk1tVaJly9v8TdemHhSTrUyjF2wibm3dUjb1ZGIj2OFg8QyQF6N_RMIH5sTWGD3zqczkHrerSH5MQVSnh34XtRuvJJFd-aazSOrBaHZcSjgIKYPbrGokqBAVk0k9Xa8ssnkoxyolZEwvRAFF5Ian9aAlwbkuUKYpBSvYWP7l5AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
هواداران جذاب اسپانیا در آستانه فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/100727" target="_blank">📅 13:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100726">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVGinc5dm49l9YEd0OUVutMV41Z_A7Efy8LcwOzfRGegimR7wlGcJqn5jUL-c0zXNN_OjKP8RpJJ5DHONUEdKmarm8_PKDliiJuzZ1p9-WGrIp03aynDtm3qe4dZ2WmM6E3P7nSHl49HcYKITuJOUv6QNCQXrcjlwJT8e34xpjG1iluv21rqhZCvHp5Si102jygY_mjGsJrF1-GH1Fcx0YhPaSl8gjyuiuykx7J2JAnpStGaxW0DIwTsNoKRzBtNRygMnhM7WtYcYe4XbbIj5m3Q7WauYRGhVS0QvNE0h1GfQ5lvWvRYx5kAIY8gAqsAQ8Azg-k9GmPr87Z_r1ON-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🏆
رئال‌مادرید قهرمان جام‌جهانی نمی‌شود؛ در صورتی که کوکوریا با اسپانیا فرداشب به مقام قهرمانی برسد، نام این بازیکن در فهرست چلسی ثبت‌خواهد شد چون در فصل‌گذشته برای تیم‌لندنی به میدان رفته و جزو تیم چلسی به حساب خواهد آمد...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/100726" target="_blank">📅 12:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100725">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32d7d110aa.mp4?token=Y3rnh7L5r2QE8yNVpFe10feNsXA_N5zof2_c4msqmvHI3F96allrOrXT3jm50XuAnRD4KouP4DUrsWHgxQ59RT2uqa5k9mbPoWjxxYL22XV3F0w9UWhxLRo6teZWSfAYOfwvrw6WECR63w_y4Gy6isnjUfAJ2JXjih8hZ6b1cWDJHCx8xOpgAoTdcgPsxknRx-MM4g0_Ikpx1rEZX2TGST_VdoZQhfhFb7kIw6cyf8osXBr0cNeEkzaUsQfRT1kLDsuv30ORgSYUeRIk7RqHENG75WWbIsYz8r2xFGZWHULDHRmadszj1olAqwbdzRZH1Xb9d757QK-rYpClHbN_qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32d7d110aa.mp4?token=Y3rnh7L5r2QE8yNVpFe10feNsXA_N5zof2_c4msqmvHI3F96allrOrXT3jm50XuAnRD4KouP4DUrsWHgxQ59RT2uqa5k9mbPoWjxxYL22XV3F0w9UWhxLRo6teZWSfAYOfwvrw6WECR63w_y4Gy6isnjUfAJ2JXjih8hZ6b1cWDJHCx8xOpgAoTdcgPsxknRx-MM4g0_Ikpx1rEZX2TGST_VdoZQhfhFb7kIw6cyf8osXBr0cNeEkzaUsQfRT1kLDsuv30ORgSYUeRIk7RqHENG75WWbIsYz8r2xFGZWHULDHRmadszj1olAqwbdzRZH1Xb9d757QK-rYpClHbN_qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
خاطره سوپرخنده‌دار علیرضا فغانی از پیروز قربانی؛ بهش کارت زرد دادم؛ داد می‌زد، می‌دونی من کی‌ام؟ من کاپیتان استقلال پیروز قربانی‌ام
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/100725" target="_blank">📅 12:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100724">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/050e680fa7.mp4?token=nOpw7bnurmge1fFaOZeIvOiW90W3_48-VJfGenDrZVbJsEQwXZspHLUpaTSokIsX8XrwjrUBuZ91iTXBAnqzR7HBtCamlcpu9hpyzCcgHA6qsqvivv9hHaWFpyFIUfn5LSytfmndcKIWKYrgQOKJ_sTGWDQ0m6oP9n6uv1m9OqzSpppW-0Ghj2VV_TGmLtVBN0FOHP507YxKfyoRBgyZbswehY_A1V4I04thv2VtD_dvyy7lUH9poDpV9x6iJXD1GvaokeWBMV9Cg5M6hwWt2evFEjUEbL22hA65udUPUfmx7r_GG_Lteao7pPljUeiz4XgQfxej21W8ZOz66Z0NQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/050e680fa7.mp4?token=nOpw7bnurmge1fFaOZeIvOiW90W3_48-VJfGenDrZVbJsEQwXZspHLUpaTSokIsX8XrwjrUBuZ91iTXBAnqzR7HBtCamlcpu9hpyzCcgHA6qsqvivv9hHaWFpyFIUfn5LSytfmndcKIWKYrgQOKJ_sTGWDQ0m6oP9n6uv1m9OqzSpppW-0Ghj2VV_TGmLtVBN0FOHP507YxKfyoRBgyZbswehY_A1V4I04thv2VtD_dvyy7lUH9poDpV9x6iJXD1GvaokeWBMV9Cg5M6hwWt2evFEjUEbL22hA65udUPUfmx7r_GG_Lteao7pPljUeiz4XgQfxej21W8ZOz66Z0NQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
👍
لیونل‌مسی تو مراسم‌ شروع بازی با اسپانیا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100724" target="_blank">📅 12:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100723">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38913219e4.mp4?token=FbXtNADPOLa-53iQp2mmDE9jIKB41jVhV_tz0Td0y9w5jlNMrqOIdWXLjSkCVqNsoYI7GzEmGMdxhN8gXXAaSExwZ442gcKIqHTtO_u0I1v-NlTAATuDaG9lnDl0T5tL9NJoyaRsX6Ykz7qcs2KjpKMttoQpM3dfFl-B3WBGAOxj_kwRGuIq275l--33W6WtvQzlYNwCfUh7ECgLZpInj-rysiZZJYgN3ZjyRb72A4UNmtMD1PmhdQtT4NA73dSSnyqf8nmSjgdfl5s238yysjniupVE6jK9I0SWULKyZuOG_qyXAvQHesVf2l76nX_cyxSrolapt-SOl2tmt_tpNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38913219e4.mp4?token=FbXtNADPOLa-53iQp2mmDE9jIKB41jVhV_tz0Td0y9w5jlNMrqOIdWXLjSkCVqNsoYI7GzEmGMdxhN8gXXAaSExwZ442gcKIqHTtO_u0I1v-NlTAATuDaG9lnDl0T5tL9NJoyaRsX6Ykz7qcs2KjpKMttoQpM3dfFl-B3WBGAOxj_kwRGuIq275l--33W6WtvQzlYNwCfUh7ECgLZpInj-rysiZZJYgN3ZjyRb72A4UNmtMD1PmhdQtT4NA73dSSnyqf8nmSjgdfl5s238yysjniupVE6jK9I0SWULKyZuOG_qyXAvQHesVf2l76nX_cyxSrolapt-SOl2tmt_tpNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
زندگیت مثل گیم شده، مرحله به مرحله داری پیش میری. الان به فینال رسیدی. آخرش چی میشه؟⁣
مسی: من این گیم رو جام‌جهانی قبلی تموم کردم!
😎
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/100723" target="_blank">📅 12:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100722">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e94327741.mp4?token=vxBIDwFaCWhKhWppsutCtvk8jEhKb9Pf4sporukyqc_sAlgA54_s4n9TIArpT15MeSDW8hjwuAp3ckmN7LbrnnKLKJic7REQ9yroUu24ivc7gFFFPIH1qfK3S81Neaqxc4aOJBZuBWDEEVBS--1kJHDe_DMyyhji0BAUbqVr8wEs-c-sZxr2kmhnDaoe0AUAYXc-wW_H9ZRZcVU_ns4clnE30C3d-uqDbQ9o2bwrPkadUhxcVk4WPHdsUG8FSHv2ywUJIi6buceppsBBh6jjBb5UwenPhCF6nM7sr5R3HbKfGkvqWB9VNpDlX7uD6nrF0cB1S62YO4X8DX9SwwdKxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e94327741.mp4?token=vxBIDwFaCWhKhWppsutCtvk8jEhKb9Pf4sporukyqc_sAlgA54_s4n9TIArpT15MeSDW8hjwuAp3ckmN7LbrnnKLKJic7REQ9yroUu24ivc7gFFFPIH1qfK3S81Neaqxc4aOJBZuBWDEEVBS--1kJHDe_DMyyhji0BAUbqVr8wEs-c-sZxr2kmhnDaoe0AUAYXc-wW_H9ZRZcVU_ns4clnE30C3d-uqDbQ9o2bwrPkadUhxcVk4WPHdsUG8FSHv2ywUJIi6buceppsBBh6jjBb5UwenPhCF6nM7sr5R3HbKfGkvqWB9VNpDlX7uD6nrF0cB1S62YO4X8DX9SwwdKxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحنه‌جالب از لیونل‌مسی در بازی با انگلیس :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/100722" target="_blank">📅 12:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100721">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXBiZPZj7MmHEhhZ238xYOSbZl3TlQVZOH_kvyR3RnsvJEZ8_V3Jo_yMqUdrweWABYxw245lf9tBZpugqWcyxL-YmLsTMwMO5xl1zNPNePf_n5HBeTl38YSUU88nmzt4tQrLtKnMAb4BzgndK4u5BP6lDaRyxKaOjZLDRRmZj0k8DZbfRZ3Y0AgMGuBdn_gsspl5S9gmv_HQV4BeBwGSPiMHTPBvfkMPFxoVlWqEEg98SPf4H0zSMLoYqz8Xk1jROQSYEB6gM2oL759He8ETW0hXICmAhpgNVKMAcgzAcFSP2RbfV_DBR16QBOTnepfGYF03cD0tBT0XpAmNCn9zwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇪🇸
نمایش هوایی جذاب در نیویورک پیش از بازی حساس فرداشب فینال جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/100721" target="_blank">📅 11:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100720">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBBEQZp4aIS-gEHbiO8pN2PW-xwV8mk5K-ubSmLnRFxL3sTAWvxUhhK3L7H_hAEbZMxOP-UOU5ZR-MjPa0a6F7qKqbzUmYXIovVwruKqK23wLghQSQQ84B5O1fOqsfSMdtuxF5WSJwJeP_mSff6xBXwzw6W6x0EDc0d4SDMYzAUhk-4yc6srMx-bm0LmrPJvb6JpLMkAyWX1GIX6Vg3zT6JqoYYiVha9mUjSre1EsW7arfW8LHB6Z8BWRXw3ZHPLho_TqsNy7MWZARisp6UeehTBVqf7MU2z6cK5MTNQNqWnWcf7vFYZ0ZiRy-BwrY-XHk29EoEseZB8shWXwfnyXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپید نحس
😂
😂
تیمای بازنده عملا قربانی اسپید شدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/100720" target="_blank">📅 11:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100719">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/474e4374db.mp4?token=gjIqC8eYUZ11a7VrmLuhiy0qxtfGeJ7gt6ry56vwBBtfjqFGweD7gDvGLOgYJCOKtT47mijDl96Pjwe90IwYVd0PrFyshI6Xy65-10OJm22ZbAXAdq5yKgcOCC-df_mn8LUe3PJVWwtFcsqrZ-y0QsbIKDvSgC5jRkAofxQL53aefltlk6QzEtXhuoF7VhX-WXDaKWAWVHc9HXplk2fW1wrM5M-LVXDORD2mmZdKjx2dJ1ywfWTEg6_-nmHIkdeQMokeC6bW_FPrYkap8qGP85ofznrDoN1Ynn7LI6Xezl1x_ecQEsyrHwltqkVFETUQBw4e1P9WT756GQPe-2nsTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/474e4374db.mp4?token=gjIqC8eYUZ11a7VrmLuhiy0qxtfGeJ7gt6ry56vwBBtfjqFGweD7gDvGLOgYJCOKtT47mijDl96Pjwe90IwYVd0PrFyshI6Xy65-10OJm22ZbAXAdq5yKgcOCC-df_mn8LUe3PJVWwtFcsqrZ-y0QsbIKDvSgC5jRkAofxQL53aefltlk6QzEtXhuoF7VhX-WXDaKWAWVHc9HXplk2fW1wrM5M-LVXDORD2mmZdKjx2dJ1ywfWTEg6_-nmHIkdeQMokeC6bW_FPrYkap8qGP85ofznrDoN1Ynn7LI6Xezl1x_ecQEsyrHwltqkVFETUQBw4e1P9WT756GQPe-2nsTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
سوپرگل میثم‌تیموری بازیکن نفت‌آبادان در لیگ‌یک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/100719" target="_blank">📅 11:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100718">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEclZgKB5oGg21wAZVWgNlZVre2NSaMNQI-uqXAWLhNWWTOiZ0irdIombHeu_SSRYkjzKkKAJuQnUJGhr2ljIwgAqtnjT-Bbr-E0u-caqlz84sljYrlXjQulLbXbsIYPSAd8ArF9IxHTQJG3TT08wtz747lp6Rn1VsuVc50YNmcRl2uFc3sBvqj8XPbE9aJU0kV_WjWD706MmvRpJkS4ZXybq6SbQAxNgk8j2aOd8LkTUBWBV1HtWpzLspeXH_57CTusH8ra6iUWO4T6KiZUSVxYJOnNq-VCdcs0zCn5tcpLfr7n562wbZ_xzrPlNsXQBrD6VJgHOTVhEmUm_zRoOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووووری
از نشریه بیلد آلمان: اولیسه در تمرینات فرانسه به بازیکنان کشورش گفته که فصل‌آینده قصد داره راهی رئال‌مادرید بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/100718" target="_blank">📅 11:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100717">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5c0ee7122.mp4?token=p6h17OJlKVrvGIrRuvtEJfJ_T8xhD6xRVLEcWDMIZI8Rn7OMpyQfj5ADK_un-1y-Q413JlzgmRBoNSRnJLaqZ2HB3gh6RIkYw-rXUcJ95issYFmxOIKxVnR09ubgRG5QeZTkYqlTUXFYEWGA-2LA906IOMD6wyOTn4GGXGSD5-JtaX4Gn4S-Vn_denMie1fzxBSW6TahKY9dhvnq4hGQPHfJrOUAL9mw24DyNrmbhvdq3qQOUZbNwIkQsI2baOapHT31RzNsYEgqh9RPjnjTC8NVYX-wUpZlMzk4w89-PdkUV2O-0zyGBoszIHBG9K5v2leU_ViChAhmeJzmPi7_YIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5c0ee7122.mp4?token=p6h17OJlKVrvGIrRuvtEJfJ_T8xhD6xRVLEcWDMIZI8Rn7OMpyQfj5ADK_un-1y-Q413JlzgmRBoNSRnJLaqZ2HB3gh6RIkYw-rXUcJ95issYFmxOIKxVnR09ubgRG5QeZTkYqlTUXFYEWGA-2LA906IOMD6wyOTn4GGXGSD5-JtaX4Gn4S-Vn_denMie1fzxBSW6TahKY9dhvnq4hGQPHfJrOUAL9mw24DyNrmbhvdq3qQOUZbNwIkQsI2baOapHT31RzNsYEgqh9RPjnjTC8NVYX-wUpZlMzk4w89-PdkUV2O-0zyGBoszIHBG9K5v2leU_ViChAhmeJzmPi7_YIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇵🇹
علاقه شدید پوریا پورسرخ به کریستیانو رونالدو و عصبانیت او از تیم ملی پرتغال بخاطر ندانستن قدر این اسطوره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/100717" target="_blank">📅 11:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100716">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71ebbda285.mp4?token=sUT5MGR-tYxm3x52H2Wpk5UvY2cgGF50dgvyp6iyvumLWl86vaQgEgT3chq_b2WT54opTY1alsJYxiW89KpHnGi3FsM1C3UprCCMtMWPyDh_R_tsPpmltojjh3D_J6KRMWDN3D-VW41_teO-UJimMnI_IgQ8NMUbijyBCuWlp-ZtIqXYbR5kGVp7_Z4vPh0944I0cUM8Gn7Fo7tLVnBmDqluUxcbA2t5IswkG8FqZfSRfpezSBpwzAvmF9nb7pXIJhPxtpr3olZahebgIOKVc1_OU5GL0uI7IwF7f3IO3hBgDqA9L-pyI-B5fdNBAwXMB9fSQdXZycR8XUue0I3oqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71ebbda285.mp4?token=sUT5MGR-tYxm3x52H2Wpk5UvY2cgGF50dgvyp6iyvumLWl86vaQgEgT3chq_b2WT54opTY1alsJYxiW89KpHnGi3FsM1C3UprCCMtMWPyDh_R_tsPpmltojjh3D_J6KRMWDN3D-VW41_teO-UJimMnI_IgQ8NMUbijyBCuWlp-ZtIqXYbR5kGVp7_Z4vPh0944I0cUM8Gn7Fo7tLVnBmDqluUxcbA2t5IswkG8FqZfSRfpezSBpwzAvmF9nb7pXIJhPxtpr3olZahebgIOKVc1_OU5GL0uI7IwF7f3IO3hBgDqA9L-pyI-B5fdNBAwXMB9fSQdXZycR8XUue0I3oqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
🏆
کوکوریا در انتظار تقابل با لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/100716" target="_blank">📅 10:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100715">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3GoyR8P6lAGWkxU5K1FoVQP8oJpG4r53GoP5bLkYuldy1RUUlYz1JM8U2scCiot5Fv6qXi3yGbrRyduR7YENNlSvJ_DoiKba8CnC6VN4UuKNMkPRBLtDgCB64fz87qhnhzLZBJZ1CQYL4caSsyL-R3oD20Jod6tg-ToR8j3V5M63hIMU1LiOq0VROVi-5j1HCVfunA6Tik19gUiV3JbolrVM4ZUnfspo_sBOGbLcm1miFOzsS4PG9garFcwxzhlC4mudnkVM8idWIoW85vWlP8Ax4wLdR2iOlkpU_VLE3CZkfLow_xRpEsiQM4S9_93DPafaF--gzd8Mx4o-xLKWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جان‌دوران انگلیسی از ژانویه ۲۰۱۵ تا به امروز در ۵ باشگاه مختلف بازی کرده
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/100715" target="_blank">📅 10:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100714">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/638800ce9d.mp4?token=jenRR6XxTCSIfhRbYHexVqnVArJ21LlklDQ8cjTzkD8IGL73jwhwJJ7ytpv_gbOc8FneF0uwUMhskkmeLEq_DZpK4hYT1NWQyuby04BlINOmZ5oCiWe_P0ht6BzBcEAud4Wrvih0rOuq3CVDS6tsAjK5Y_lyq5qwwf_s0LjAY0zO4xBMS3ACkSw1pyY90qRAhuG2fqSu40-6il9ENmEbrYXExbkbtieNfoa3RgLOnwyPDW3L7T5baU6ZninqUa3W6YMF51nxs0seEn9V-hssWWZJNBvACTOPMWkvozaUQQGvV7tZkg8qtur2FUjdTzPThGwABPqbrcC3gmCmZtVM6l55OCV2HS5ird87-C0flwUY7JSCQ_EMwzbbnsqjmeScbyx-1SX6-chKtqGu0PjeenZaabSRoysuG3hSSw_B8H3aKSQpKuLo0zDZzOc1kXvwUkjTE_johE4tb2nDPZlPBYxGrzqo5xx9SeCQu2GFN-dyk4VhDgmYe5zF5VIgt2-L948-9Ou5lGj8FxrGXWs_lLtzFQQ_8tSgUnh6YRxzNN-KYD5WApNP_4OSUFJIxEk6BWp8FvuyhGi33KCJ_CAFLnE6bPVm8Dea21V2tUxTYPiuz98pmwK66a0YwkmLlCElZuRwZgnLnbJrZQYqsJHfH9-5ooBKvrhttsUzXTyOQ7Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/638800ce9d.mp4?token=jenRR6XxTCSIfhRbYHexVqnVArJ21LlklDQ8cjTzkD8IGL73jwhwJJ7ytpv_gbOc8FneF0uwUMhskkmeLEq_DZpK4hYT1NWQyuby04BlINOmZ5oCiWe_P0ht6BzBcEAud4Wrvih0rOuq3CVDS6tsAjK5Y_lyq5qwwf_s0LjAY0zO4xBMS3ACkSw1pyY90qRAhuG2fqSu40-6il9ENmEbrYXExbkbtieNfoa3RgLOnwyPDW3L7T5baU6ZninqUa3W6YMF51nxs0seEn9V-hssWWZJNBvACTOPMWkvozaUQQGvV7tZkg8qtur2FUjdTzPThGwABPqbrcC3gmCmZtVM6l55OCV2HS5ird87-C0flwUY7JSCQ_EMwzbbnsqjmeScbyx-1SX6-chKtqGu0PjeenZaabSRoysuG3hSSw_B8H3aKSQpKuLo0zDZzOc1kXvwUkjTE_johE4tb2nDPZlPBYxGrzqo5xx9SeCQu2GFN-dyk4VhDgmYe5zF5VIgt2-L948-9Ou5lGj8FxrGXWs_lLtzFQQ_8tSgUnh6YRxzNN-KYD5WApNP_4OSUFJIxEk6BWp8FvuyhGi33KCJ_CAFLnE6bPVm8Dea21V2tUxTYPiuz98pmwK66a0YwkmLlCElZuRwZgnLnbJrZQYqsJHfH9-5ooBKvrhttsUzXTyOQ7Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
آخرین وضعیت پل‌‌ها و تونل‌های هدف قرار گرفته شب گذشته در استان هرمزگان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/100714" target="_blank">📅 10:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100713">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e91953d632.mp4?token=Upxe01j-C2CClkZyPUPN9gKztpwEgGhCMv3MTB9b2WUquIwJq48XXfcX42C5ZDVlLBy2rr3A3hou-Pptk1n11y7RWvm2HJhGx7FUzAWZry5mnIGmcLHfN6aYBZVCsZwooISjEQsGJd1G21n_3VL35TwyNOqi4bG-HkKKcF0LkQ5Mv9SudDeZBPt9mkP89oewC-Ooehq0qeifH1OKqDpuLCbKX77Jl47TxT1lhOIyfSMQq11fcnho0uPZUePlNov-jQth6KmKPDiEXjknFJkxB9srkI2ttpjhsBJsDxfZmu_olhEL2MqGWwUUcJcF8P4pN8Esl2z43Y2NyEoLNeEq1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e91953d632.mp4?token=Upxe01j-C2CClkZyPUPN9gKztpwEgGhCMv3MTB9b2WUquIwJq48XXfcX42C5ZDVlLBy2rr3A3hou-Pptk1n11y7RWvm2HJhGx7FUzAWZry5mnIGmcLHfN6aYBZVCsZwooISjEQsGJd1G21n_3VL35TwyNOqi4bG-HkKKcF0LkQ5Mv9SudDeZBPt9mkP89oewC-Ooehq0qeifH1OKqDpuLCbKX77Jl47TxT1lhOIyfSMQq11fcnho0uPZUePlNov-jQth6KmKPDiEXjknFJkxB9srkI2ttpjhsBJsDxfZmu_olhEL2MqGWwUUcJcF8P4pN8Esl2z43Y2NyEoLNeEq1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یامال رفته داداششو برده آرایشگاه قبل فینال موهاشو رنگ زده
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/100713" target="_blank">📅 09:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100712">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2382f600b.mp4?token=MkWPpRArSPSrxqMK1My-2YX0ikqyKF_BbY4khiD1-8UEMJFpVg-Uz9esgnzjV5ctV4ERPmq8mYh5xuQ3xr7PiIEcdDLodNpsv5DiACHjdq14-JzKVSkl79APvFxvq9hycC45F7-BjIavRauhhMC6kjOFCLr13oOn_SRYsOyIWs44FxCLz7hTHVlQYc6Vr8jfpXdZMW3OG9FlrLCG6OyCM7dFqQrmkzkkCdrGeTCxluVZ3uXvOTQd0de0odxrFPEI-kbo6XG55twbfPBT65Xmn8IGMaQaAcP8vL35oF1QiWJmjXD-336wMhWnGH7mJ9UPXOFUgIifBKRROCgj6qqOUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2382f600b.mp4?token=MkWPpRArSPSrxqMK1My-2YX0ikqyKF_BbY4khiD1-8UEMJFpVg-Uz9esgnzjV5ctV4ERPmq8mYh5xuQ3xr7PiIEcdDLodNpsv5DiACHjdq14-JzKVSkl79APvFxvq9hycC45F7-BjIavRauhhMC6kjOFCLr13oOn_SRYsOyIWs44FxCLz7hTHVlQYc6Vr8jfpXdZMW3OG9FlrLCG6OyCM7dFqQrmkzkkCdrGeTCxluVZ3uXvOTQd0de0odxrFPEI-kbo6XG55twbfPBT65Xmn8IGMaQaAcP8vL35oF1QiWJmjXD-336wMhWnGH7mJ9UPXOFUgIifBKRROCgj6qqOUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚫
افشای مکالمه مسی و بازیکنان آرژانتین بعد از پیدا کردن بطری آب پیکفورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/100712" target="_blank">📅 09:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100711">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dccbf84030.mp4?token=HTrFe0JFtLPpVojc0LSInKGDM3aQ-Dgo7yiwvm5gePm_pMubeQLy15LVWvRRttccS5jjkIreAuGEnvDLG56ZMV8DnZxJ45auInLrWnZvvc1cP5bFlUgnHCGwdLQTUtCyorC-WnBQNtHYlqM__UMiDezy6iCecF4_lYSnbviFuLMjpzHIAKMMlihE89qGnEPBgytEgZNmI4O-yxdMeg7ptA5YK7DBR7oN2TLwcuPtQUBx2snrDjuD3plPg1ib2EZXwUR_I58bkwW8xfHorOHLsKGmj6QopBuijjtlIaESqY0sbYNbL9ri5YniWAGsObxlnbL0ZpCZQw_CYobwlC1X0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dccbf84030.mp4?token=HTrFe0JFtLPpVojc0LSInKGDM3aQ-Dgo7yiwvm5gePm_pMubeQLy15LVWvRRttccS5jjkIreAuGEnvDLG56ZMV8DnZxJ45auInLrWnZvvc1cP5bFlUgnHCGwdLQTUtCyorC-WnBQNtHYlqM__UMiDezy6iCecF4_lYSnbviFuLMjpzHIAKMMlihE89qGnEPBgytEgZNmI4O-yxdMeg7ptA5YK7DBR7oN2TLwcuPtQUBx2snrDjuD3plPg1ib2EZXwUR_I58bkwW8xfHorOHLsKGmj6QopBuijjtlIaESqY0sbYNbL9ri5YniWAGsObxlnbL0ZpCZQw_CYobwlC1X0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
صحبت‌های عجیب وحید قلیچ کم‌عقل علیه عادل و کریم‌باقری و سلطان علی‌آقا دایی!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/100711" target="_blank">📅 09:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100710">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrZfVWpAp2RqbMyRAq7olAZfT8OANzXol_8WZsUDcNsRKgDJk3nNvpM1836_UcgzXXCKaJP2R6ptNrlSt4MNpVaAZZtgxXMEUzgnQuBtOAaQG4OihHmR6lWV1ScXUvRmnZbOogRwUTavqFD5QNYyUzV7k0Ziqmux3ZVHeHWSoA6d6Vpwn2HuLkSyyNxyLN_Oi68Pkax6p_6WIHYjYJCAw6tryBCkhxvvHSqIeFbGVFIM6k_-LEgAIXDqT6Z_tnpHYKRtIaYogWMabQmBVfLxm3zT7BNUTOijGPzjeJNpW7dyQXsHJF_TnnCBs0cMqKpq_NW4UUySQZuS1yEqteJqcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⚠️
وینچیچ اسلوونیایی در جام‌جهانی فقط یکبار برای آرژانتین اونم سال ۲۰۲۲ سوت زده که تیم اسکالونی مقابل عربستان شکست خورده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/100710" target="_blank">📅 09:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100709">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnmwHvnpohJVVqL87NrZeaLN9jCEAU3TG-9XcohHQOieMaL6My-K4FlIosuqIPihsaqLxOjioSxKaBlSY0788bojHbFMj7wGBbEshJ9myD2sXhifZDVSqgQgM18RxbK63pKD-rkC4IfexnP9e4g3ksEmYmkqOQnN7A20uOY3sW2VJ_vZaKEpeFHHbVUvXEll-XiqeeDE2xUGLxmA76-_92NLBsNSWqHwKMCBQxEL-IoWdDLSWBbEiSxVpHrspJZNjC3TzqbXS15JmnLVuZC_zdA16idlCrM9WtUlf1KKVh2MJrm9n3HvH8RhmCOYwYnqlLp5_Z67DE75qHStI7JCGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐
⚡
تو این مراسم همچین قابیم خلق شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/100709" target="_blank">📅 07:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100708">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/136aac8a04.mp4?token=t9r1qPdEeu7fCF5GotPKRpgzdEKEyRYRXTqe9IA_sfjxm-x6yvNAU7PRPBKhm4eznXdUikVQG-Cy31MQXrtgeVS8CFsalh_l_8sbtXJ1QDRnb5djvQCMFwmg9-s64SZlTYF8tkPVYAc9lKrkX3JJftS9Fqp08C9ma0JfKLgygPUZcRf-C3xHLicwzpBJET-DYxk9RNy-1yaXuuQQHLYYRTiZ6KPCazAvbdFP-81sGGEBqMC7kVkafT3GWpzH23oGyRi7N1h5X4S5TuIQsH4EgbzS9BJyx6LZaQlPbvSbzqVDp4_T49Jx97sygDnTWD58JEYOqrOpT0q7m8NTcdRjXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/136aac8a04.mp4?token=t9r1qPdEeu7fCF5GotPKRpgzdEKEyRYRXTqe9IA_sfjxm-x6yvNAU7PRPBKhm4eznXdUikVQG-Cy31MQXrtgeVS8CFsalh_l_8sbtXJ1QDRnb5djvQCMFwmg9-s64SZlTYF8tkPVYAc9lKrkX3JJftS9Fqp08C9ma0JfKLgygPUZcRf-C3xHLicwzpBJET-DYxk9RNy-1yaXuuQQHLYYRTiZ6KPCazAvbdFP-81sGGEBqMC7kVkafT3GWpzH23oGyRi7N1h5X4S5TuIQsH4EgbzS9BJyx6LZaQlPbvSbzqVDp4_T49Jx97sygDnTWD58JEYOqrOpT0q7m8NTcdRjXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی پور بی خیال آناهیتا درگاهی نمیشه
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/100708" target="_blank">📅 06:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100707">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htk9Ew4rmr4lN92Z1zvJcMg2WHcPuXzIm83Oh5uCdv3wxglgH3jnA0zNMMkyJLE4-OEbhs7ULxTVzuatxZiN1VBQGaxwMlbGzXfOiHA6mEJoRgdClGBErQhXS-YWmaNbglrtcGMkyAm7L6G7isckFdSWAuFsVt8eI98BOJAzYvk8MP3ttOY8vvD5JQiQJbMDF-PBa_PMdU9jU41WRnTSPc-yhYNfGaBxhKytW57yF22wIKtxXzD1nPjmiIrori20SiHXydsUbDGRJpbHue3RQ14y90xgwhlgF5qnp9_gboAaGnQohhqs1hTOenamRUHkwLwHj7kOScttipi1E7B5FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
👍
لیونل مسی: از بچگی یاد گرفتم و فهمیدم که آدم بیشتر از اون چیزی که می‌بره، می‌بازه و فکر می‌کنم همینم بهم کمک کرد تا چه به عنوان یه آدم و چه به عنوان یه بازیکن بزرگ بشم و جا بیفتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/100707" target="_blank">📅 02:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100706">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdiJk6manYethXKxADFM4MbPpjheKQTNrH171chwR7MO4d_U82pQbNmvxAcS5iA6PMXbDZZeXNAkJC7WYHFbxhhuhNdc6_Mmjl3JCvThTd2fBs-yj8jchLEq26VrAVQMCyWJFlf8S4u2WNbeBY9w76oBwos79wwk2waIjhgHWUQKwrlELbx0yEcu7YbZnEEy8vH-KalKT2HsEpaD95ThQvIsWZ-nmDEurzORDEZx3S22Aar252SculPwP3hVcmWgC668P2OgE5wCkyGmrbB2CL3HDMAzhhcWXVnO1fuJlr90ttxFzwOMkkH57Nw-TpO-zOjAhQJOl62T1aFs8XV6Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🎙
اسطوره لیونل‌مسی: بدون‌شک لامین‌یامال یکی از بهترین بازیکنان فعلی دنیا است. برای او آرزوی موفقیت دارم زیرا باعث پیشرفت بارسلونا نیز خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/100706" target="_blank">📅 02:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100705">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🎙
🏆
🇦🇷
اسطوره مسی:  ‏"ما اشتیاق زیادی به بازی کردن و لذت بردن از آن داریم، انگار که به جایی بازگشته‌ایم که از آنجا شروع کردیم، زمانی که کودک بودیم. حریف هم بازی می‌کند و نمی‌توان همیشه برنده شد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/100705" target="_blank">📅 02:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100701">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fGax634jMFrlLcWF1-H7mklNVBW2XTkZC4fdao6PjqpcDcmuf991toUlXJtkPcTnQ0iudQIblHErgacED8rXp2Grqy9K83nsS3MTnJsM0Ny47qx8Vis4eB-S1dUb_dcAtRlEblmh0yJt3O8Of5UNDbtHbhakpr8np7yRtw1ZqWWEJalKY4m8x9_wFfB5Z519J2FrsnnG1ezNVbh43AIYdwXpGjiq5xjyPedwiykFid7q-_YsyX4gdORuNf7_LMPDU1ZDZUV0-1xbYHdIVNJeY-lDx4kzt0cPjIUMXhgD3qB5qad1DPnRdam7vE19E8nf7XPV00TNonupV7hYWIvHXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cWNwek2Q_iEIlSSsPY6syj30gNyKzGbgCLKGaxzBBOhOp5zE1YEY5Z5R9P6z4x99qqfZv9b9i5L94jKd-WCesJtO6dlObJ7JDxj2DoaPY4lqa2WqSVjhOjySwQ7n_-yREIdOkW-knhdx-cD0shWBBA5EZezISXw8d198WStd5rEAZ4_3SloNcw_BzwNrHFQ_2gyfNNwniDSqOCJgQpa4Qa5nFhUUdRS0kdxHBslgv74OKW9_N2rPdOZnLdp1p9OEkshEOU3vQo8-B8AcPxvSuQr_b1ADb-jSIaWRUcS38Pz-drYHR6dEb56JnxSHX5Av-7hiVso_1LeUuNISmiyrAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CbLgfYPObGE8JyC2nAzEVklJCOMyTc0BdCx-_rJGbXVulSGowAPxCX_nOgZMQckT78n8GdQDflg3od2DjiZM4nefw8RUPa4Lah5OeytJ08UeI3xdKUg_ZYIBAnq4NLc028LfqaY0zkWsOMyPoa7u2DyDBj_ifYBGLtzgQiy_-3fAeq3E0WZz6j-I-NpJ2gSryqsst1avMvYB8UaE-K7CaC55WiF-_m8ZatAKIKYJRsBFIjun-TMSwJqL6icSL6V4RbsWlqKZ6-XCZ8PSTqDwPKFkK4kPywVOeCcrK7XiSmWVnGTOYKqvo84TGEsVtBd3IIImKecXNMrv9KT4JHa1lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TJCcX2dKE07iOT2Fx_13Vb15fMdkd4_Xs2trbCh_XwMzkF4nX7K-mg0WrN4aEsSqcsvj_2KWCsTTxf48sYzsZGM8UmwdSP0QApmeZiggPC9IdjBMrWDb-_tOPzQN03c40cYudJu73MlyjPhVBk1aI8C84iL6gPiMpe4REAjJmXW9JFv7cPeW88jH1L3HIQ1RPTbdWc5XqBJzqqVDwFt3fMwYu8hfHTRj05DtYCrMUs2gmIXOxxWS-uI27MucEJR3bRP_8lqmXJe7C8kfkYYzrd52viNHzc7chyDY72uRwe1wK86rxrZ6lcQA8p_Ijfw767w4cgxq-5ccHHi2Y4zMsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇺🇸
📸
|
تصاویری از مراسم استقبال اعضای فیفا از دونالد ترامپ در نیویورک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/100701" target="_blank">📅 02:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100700">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVAx74rAn_YjrWSfUy3_O3nXn3_SbVSEIvpY7g0iAdZAFqLzlDBkRRuWKyOEY1k5YKlHWQtlgtWa4PmB-X2wWuXCM2lIj2ZtXj_luX_wBoiX4edRAWV7RCIN_18xiiAcPktnXOwc-MpX2yzTvFh3JlhURwyHfXh8wNrnmY9g2Nn9WdVeimYRGd0ubmsV9xdNyt6mLzq1XknwL_GX5tTcGgzjC7H9aexb3dHTzkk0MyMWvfNA5MsTFhVGaOTlLKuw55r0YOff3VoZ-etW63RU-0wOf651bXu4qI5FooCUo7e7Wc3wA9wUmSrXARvvw_QvfKoVnp4miIsLaTjQdCNfGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
چند مسیر اصلی در استان هرمزگان بدلیل حملات و بمباران‌های دقایقی‌پیش مسدود شد
❌
پل محور رفت در مسیر سه‌راهی میناب به سمت رودان، پس از دوراهی سرز
❌
پل «شور»
❌
تونل شهید میرزایی در محور بندرعباس ـ حاجی‌آباد در هر دو مسیر رفت و برگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/100700" target="_blank">📅 02:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100699">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-e_4kUeTQXIMc9R4BvV_om96MeHujE5mKcf35vC9FI7EGoVb172GKXR2h8CJwaQ-r-6ctzT_kIrrfUg0y6G0jAsqqZgU9YQrEMXqSY7Cbv4ic8USLyP7s3iiibpRDi78km0cwJbnF9M6yTjA6C939cMtt88McaJlTYep-x58zqTBL_3X0iIfMVFADoQwqjOZvDcVnJXk3HNgDh0J6vLvJsr0LLHUG9p7g2LEE9uXg_yrYdlBFsnhQB89dz9bQ9O0o9w52kklSkLBh_K8cWcgl1zyTOWsiSSDp5d9810yyxUbbbkJ_Xq_K-6csOeWrtmnmrBOqTgReI41d5KL3wU8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
🇦🇷
اسطوره مسی:
‏"ما اشتیاق زیادی به بازی کردن و لذت بردن از آن داریم، انگار که به جایی بازگشته‌ایم که از آنجا شروع کردیم، زمانی که کودک بودیم. حریف هم بازی می‌کند و نمی‌توان همیشه برنده شد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/100699" target="_blank">📅 02:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100698">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1fj24xZTjzp4VUR4czoMY6d3R4pPwa0EX2diKIuSRcmEpvszVERVus9luCWEa0FxBXulmCavvWnRg2Zhuy5pFhAReP6PPSBZuSZHU4M_fws0pij3FRxMvVstwQxCZYI2cUzBuc6I2crR_KALydqXxQmAZUtirzHYxTOB-dimUc97QbrAzqbxoy_-RwMQ_hHThymaR-gaXPy_JqJXNxHPVczQms3DML1rH-L0-Apo46zlfplVK2Rod9jzD1LvZOn68e3LmvvAKCnYMhfNZfWXDYmD06GM5HFf5SyVXktVYRcOojuDzaJxeb15-OvoTfawnZpi8KJSw5sVkbUyByqOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
اینفانتینو: بنظرم جام‌جهانی ۲۰۲۶ بهترین دوره در تاریخ مسابقات فوتبال بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/100698" target="_blank">📅 02:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100697">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
چند مسیر اصلی در استان هرمزگان بدلیل حملات و بمباران‌های دقایقی‌پیش مسدود شد
❌
پل محور رفت در مسیر سه‌راهی میناب به سمت رودان، پس از دوراهی سرز
❌
پل «شور»
❌
تونل شهید میرزایی در محور بندرعباس ـ حاجی‌آباد در هر دو مسیر رفت و برگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/100697" target="_blank">📅 02:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100696">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfoOz1puQcPu0PFgayco7lzwtKBBuP6Bd77eq6Qc24i9EA-ehwtYmQOw7KKEB53CZJBK8kdoB8f62VOipfX3HAJqHkoSI8i_9lYkGAL_Dz8RUbtT0y-C0zOXUzrt_MvxxDhHI5i8Bqp9Az3EXqxMfxwKyrwXQSu_Lpfo_fp1GKGspPOBvr6fK1sLEBXMOC-_a70rC19FL3kfIoftALTiiFeEEYfus2b9V5yZMlYiX7ABt4E25PazCtkL1x-8Lp16ngpHEOs5-0XuQv1R6fG3Cccnos0r_XtEOoLGfbilE8eCzLXef6TnkQo4sD7cKDxPaPKNgjROsGJDxO-fin7Zww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😢
🇺🇸
ترامپ: دموکرات‌های احمق در انتخابات تقلب کردن اما من در نهایت برنده شدم و میزبانی جام‌جهانی و‌ المپیک رو برای کشور گرفتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/100696" target="_blank">📅 01:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100695">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🏆
🇺🇸
ترامپ
: امیدوارم یه روزی برسه میزبان مشترک جام‌جهانی آمریکا و چین باشه. چون فکر می‌کنم بازیکنا از مسافت پروازی که طی میکنن کونشون پاره میشه و جذابه برام
😂
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/100695" target="_blank">📅 01:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100694">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/900b057c2e.mp4?token=shlm0GWKz6yTex_tzROeAi53bSaiEqR8BesBSZ_cZo9fLZP7X3JI_r2nIkR_LAqVVVIR5I9j2iQloUDW9YTbRVUelCapaXW2azFkGKSRRvZA6IG3t7jUjyspI2PSTdXWp_xMKVhBvhF0SE_OW-H88Zo5wpCQEmg0Z_9oCfLNpUbM1CeKsuBNFW6bBGLl30bglHPoV_90QUpiHbITrELjSVkRMz2dstQVSjYuS4Fuzacz4CPypnoSYN7WW1Zj7q6VIGy3MGYbilsd4hkBFTA1qd2KokhHEgCF8-F-rW6HNmEc1On2zT0FRiOq3HEY6KGNCpHFHSf7W_fmucRyIP4a2TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/900b057c2e.mp4?token=shlm0GWKz6yTex_tzROeAi53bSaiEqR8BesBSZ_cZo9fLZP7X3JI_r2nIkR_LAqVVVIR5I9j2iQloUDW9YTbRVUelCapaXW2azFkGKSRRvZA6IG3t7jUjyspI2PSTdXWp_xMKVhBvhF0SE_OW-H88Zo5wpCQEmg0Z_9oCfLNpUbM1CeKsuBNFW6bBGLl30bglHPoV_90QUpiHbITrELjSVkRMz2dstQVSjYuS4Fuzacz4CPypnoSYN7WW1Zj7q6VIGy3MGYbilsd4hkBFTA1qd2KokhHEgCF8-F-rW6HNmEc1On2zT0FRiOq3HEY6KGNCpHFHSf7W_fmucRyIP4a2TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترامپ: هری کین بازیکن فوق‌العاده‌ای است، اما شاید در پست اشتباهی بازی کرده است
به نظر من، شاید آن‌ها (اشاره به تیم ملی انگلیس یا بایرن مونیخ) اشتباهی مرتکب شدند وقتی او را به عنوان یک بازیکن دفاعی انتخاب کردند. آن‌ها بهترین بازیکن خود را گرفتند و او را در خط دفاع قرار دادند. این موضوع کمی غیرمعمول بود."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/100694" target="_blank">📅 01:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100693">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c16c25f51.mp4?token=Q1U2PFwyR8jgYKhRprPce9eMcITLBnwkuXabNNCt06V4vx2Rgx_FzcTk8YzJ-XD5oaZrPSKYtppfjDHfn_VLAH0VI8B5xF8wKTfP5faCl8tFzFI__1Kj9arG8yD7AOANm0V29gWdxqmrjgZ3Pu2WCzqQEJIqFL7o3hZ_vLFbbjVrrvkRWbvd_XdYOfK5ImuU56yC2nrvKp5LNE_wPSsxB-U0xHZrdAcratnUIJ9Zjh0_zIo44GhR21reBvHJMefvTm89hYncIbM29FLGtfvobuyh_YIS9ICjalMdFSqBa_-03ig5OgJzAihwiitHSwLfTI0kdlyf1dZqXWc7tTbuxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c16c25f51.mp4?token=Q1U2PFwyR8jgYKhRprPce9eMcITLBnwkuXabNNCt06V4vx2Rgx_FzcTk8YzJ-XD5oaZrPSKYtppfjDHfn_VLAH0VI8B5xF8wKTfP5faCl8tFzFI__1Kj9arG8yD7AOANm0V29gWdxqmrjgZ3Pu2WCzqQEJIqFL7o3hZ_vLFbbjVrrvkRWbvd_XdYOfK5ImuU56yC2nrvKp5LNE_wPSsxB-U0xHZrdAcratnUIJ9Zjh0_zIo44GhR21reBvHJMefvTm89hYncIbM29FLGtfvobuyh_YIS9ICjalMdFSqBa_-03ig5OgJzAihwiitHSwLfTI0kdlyf1dZqXWc7tTbuxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🇺🇸
ترامپ
: من فکر می‌کردم که ما کشوری علاقه‌مند به فوتبال نیستیم. اما مشخص شد که ما یک کشور علاقه‌مند به فوتبال هستیم، و من فکر می‌کنم که این وضعیت همچنان ادامه خواهد داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/100693" target="_blank">📅 01:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100692">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d154c16b.mp4?token=AFl65YyJb3hNzNRM5zAmq4KEMppBzsG5fYne5-U6ET4BVistz5kiECeYmZyOY45E1gXPacW1m0z7mO3AN-1esYQDgMO9hHBiWdFqlqhAbFm_RUfSS2FJ69Z0pWFEWqGzuoUo_1XsxtqY0hSqxrwPl4JBa3KXlioY7TUmCUTpD8jp1URXM31OQf9zGLlAKwUr8O4zUo3eMqKGf3npwLIiPk89Jbovb3QLul4tyjotE4_joOAJngKKE-gVju5JDGsZDNA95f-jXIhbWqxjxvLHc6ejPYr4Kx8cXX6MBxkEJcCX-XVd1d1mrmKwB8N86DzY9R285ekgJgioo5UYgMqY3H9dcXLeTNKTftgo-lQV3rNYTL4raL4dkKFxk5O3mLEh-xGrT5GWAXVu2VhwPAdrZAoDj3xj4Py1V6EJz1Rszb7CJ0MA1B8DUBad_VxVEhGEyLpO5j_fLppYqhevsHXG2PS6PyzMNilLCMdDQYKYKv4_tj5VUGe_XXwPpAvzpQG4XAmbeA8HCkA3NieyMnWDk4y_G-yIiV6N1H4OtSXFUKC75Zbg5I2vGdEmWdtUw0ey5XPDMQ6VowO5W3dYZUVijXn2_nG9-5O_TmN6DfZxY0XTTfYW-IopIlaLBMN_J-dxlGUAZn2-1KJBc1LNJSYOhg9GkM0OtqIu8086ucepi4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d154c16b.mp4?token=AFl65YyJb3hNzNRM5zAmq4KEMppBzsG5fYne5-U6ET4BVistz5kiECeYmZyOY45E1gXPacW1m0z7mO3AN-1esYQDgMO9hHBiWdFqlqhAbFm_RUfSS2FJ69Z0pWFEWqGzuoUo_1XsxtqY0hSqxrwPl4JBa3KXlioY7TUmCUTpD8jp1URXM31OQf9zGLlAKwUr8O4zUo3eMqKGf3npwLIiPk89Jbovb3QLul4tyjotE4_joOAJngKKE-gVju5JDGsZDNA95f-jXIhbWqxjxvLHc6ejPYr4Kx8cXX6MBxkEJcCX-XVd1d1mrmKwB8N86DzY9R285ekgJgioo5UYgMqY3H9dcXLeTNKTftgo-lQV3rNYTL4raL4dkKFxk5O3mLEh-xGrT5GWAXVu2VhwPAdrZAoDj3xj4Py1V6EJz1Rszb7CJ0MA1B8DUBad_VxVEhGEyLpO5j_fLppYqhevsHXG2PS6PyzMNilLCMdDQYKYKv4_tj5VUGe_XXwPpAvzpQG4XAmbeA8HCkA3NieyMnWDk4y_G-yIiV6N1H4OtSXFUKC75Zbg5I2vGdEmWdtUw0ey5XPDMQ6VowO5W3dYZUVijXn2_nG9-5O_TmN6DfZxY0XTTfYW-IopIlaLBMN_J-dxlGUAZn2-1KJBc1LNJSYOhg9GkM0OtqIu8086ucepi4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🇦🇷
ترامپ درباره مسی:
مسی به خوبی تحت مراقبت بود، و ناگهان او در سمت راست ایستاده بود در حالی که بازیکن بزرگ که او را تحت مراقبت قرار داده بود فقط آنجا ایستاده بود. مسی شوت زد، و آن پایان بازی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/100692" target="_blank">📅 01:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100691">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0f23fa81d.mp4?token=Bb9kbFmQq4UDEKzl4bQYoDqhz5bxPjhkJip61swf1WHzcnGHO9WL_mf0Czf_vd61YXz3I3TjLLR0y2UdQvoUQgepPKaELMCzNV_x294nUxf_7rGLG2Cqv2pcljDnFcVj3lWRhqiOlkjkAMxRpHdGgrfWkH7CA5Bjnlbt-En8MktDFpudDAZs4haNQu-k4MoNLqyz3-nOy24BXJPiz5FKUgH9U-XHJmXx4ixtqzTIxJs7Kj8ddrGzZNEvp1WPEEw6s4WScZXC4LnD4nO6QXl8O66ZG1SzhLUSQ_nxadNpfzmnUJkWi83VxzgkaYIwz7ovrlSnWUDmRUaxCuxABVjQjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0f23fa81d.mp4?token=Bb9kbFmQq4UDEKzl4bQYoDqhz5bxPjhkJip61swf1WHzcnGHO9WL_mf0Czf_vd61YXz3I3TjLLR0y2UdQvoUQgepPKaELMCzNV_x294nUxf_7rGLG2Cqv2pcljDnFcVj3lWRhqiOlkjkAMxRpHdGgrfWkH7CA5Bjnlbt-En8MktDFpudDAZs4haNQu-k4MoNLqyz3-nOy24BXJPiz5FKUgH9U-XHJmXx4ixtqzTIxJs7Kj8ddrGzZNEvp1WPEEw6s4WScZXC4LnD4nO6QXl8O66ZG1SzhLUSQ_nxadNpfzmnUJkWi83VxzgkaYIwz7ovrlSnWUDmRUaxCuxABVjQjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🇵🇹
ترامپ درباره رونالدو: من رونالدو را شناختم، و او مرد بزرگی است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/100691" target="_blank">📅 01:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100690">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reNdrPGXa9Nw4jyTmkISC9g7EIzLa6U1jXT2q9DCXFQb1aAW_Nw3SrBaWmKrXIz_Q36MqCpUoAX4ztAxdc1uOmxpiceo51u03hNYilsznxtdZd_8a7P8y7lGJlUn4Zb3GSPG93kedn9jy3mBPSee7QsVMzzOyrQl3iWtcRiD7CB1m9HQzAzTFM1Pvvs9NFK8HXrdbyVFmlq_d1yyz0rEuRQyrEhs7LOAT2KnLnh-azzGg-WyjjEuqvc112PS8rvo_7L9yB_aNZR89ndzu3z81YGAW4LCjIr5vYZpWbdYeK7-qLPdfET4Jm2YSfrYLx9T5FAppdOK4weMdXFQKEsxUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اوه اوه ترامپ و اینفانتینو نشست خبری گذاشتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/100690" target="_blank">📅 01:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100689">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1PwdwY6cHa_cno7gDDvrr5hJ367Z-mzJNMBMEZ2iJY6V4nmVFky3cAsvsIqHY5F1UwkQYvdjfZGSq1NYqk9rhlm4OWBv8i6e1XpX-uShOvESIEQ3FogSnUzs6jUxpQj-HZJxOEr8U26QztbtdIBkcWY7T9_yqSJoCDpESmp7A9Sns3NkNQn9hJmhGQTohAjLtCgdHiM64au81nZlqD0G5kxbyqFFKCrndhsgeriVVQ4tIzWM_S-yqtzpOloIWPi2P7EIdVfc5eK7SkUjGvg6F7n18ORgoF2DSmaA-l34aZejmYcVjPfAVytu4MEwc5ctx6gQ9pNPUUQRlNPBd8OIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🔥
رودری کاپیتان تیم‌ملی اسپانیا: لیونل‌مسی بهترین بازیکن تاریخ فوتبال است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/100689" target="_blank">📅 01:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100688">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آغاز کنفرانس مطبوعاتی اعضای تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/100688" target="_blank">📅 01:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100687">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhatkGArBuWIZ72KEQ--AnigmO5zYB_fomXgESB_sIG7_xN07gVFF9N5megmW-2oFVd7CwXLBuFJVFE1f4QpNuhk1G4d7Gkw0foMHDXkcw-lqDOhbeL1DLyEKlTppBdCOgc-5yaQlIQ82lYx47J4zh5y6YF4GBUhXz6N0LF26KoaiETFc4LzIh1mekJQ5glsP2PqH3iSQhPxXBG5bxzTxXz8q2VVTsT1cnBKgC-ukrZKnSR7zQ8dQtn_pA6Ohc37GPu4CGleskJ5envMdjb2FKmJ-ga6SmOkAcZcAEP-3cmClc7t1JQkl04x5QbUm9iu8QiCGI9H1DyCCnfxvgd2sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز کنفرانس مطبوعاتی اعضای تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/100687" target="_blank">📅 01:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100686">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9F2KXJeRAKtMtTpJUPz_0c0Hlyh_DbL-Vqc4NRQ9XZipKz18q6QARhNxdnhFwd3XKEHny3LhVvkAHMnXrt434Ky_fkxiNQoAX4L57z8Cmxshs9wrQWy8M2Vr8x1aE7idb_oFmpdcMyNZzJWU_Bg6ZEp5qaAjTUX4kBtjplvp9l4c6TgwFTxMnMsXSMne-NPv_4Se6Dk-z8QhZClD2AdysvUDwSR6Dpy6lAHOA9l1BhMX17HlqAmsjLp51ImQvVKfh8_05TD0bzw8LJj-pImPokrKUXYw0EOTf4VjKUzIRhnSLhgovAkdsMYLlDCfPfAv6Y9T3_ehkqb_O2-aEEzKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب‌احتمالی فرانسه مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/100686" target="_blank">📅 00:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100685">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/50fc7e043f.mp4?token=kdrogahqUFYw0NmmiLvZWU9Ua2m6dhU5Nge_uaqa4YLb4QPTovPH9bsaHjs6fnWl4UYNHBfh2Gi1z3IdtkCBtKjhkFupPkTMbdddFgP7syZ1UpHcRvffgjkgUDMOtkh_z7w0J1KZNf0YjGWvfzhTVoVf2kPQ-AgP0jq8aagnJs4xyyeJKcCSOiTi6twceifKomkjZsNL5EzAb29lOgtUHheByEeX-2-UFSCsSipNRR4gGRJZb4WljC-HBI9-pidfZ34NJVjy-s4Lb5NUonmQ3t6ju2ic7_z12b8a98NjP0DXI9aVN-lf1ExLGuiKk8TcmlsSuacitNb6j92RBJGShA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/50fc7e043f.mp4?token=kdrogahqUFYw0NmmiLvZWU9Ua2m6dhU5Nge_uaqa4YLb4QPTovPH9bsaHjs6fnWl4UYNHBfh2Gi1z3IdtkCBtKjhkFupPkTMbdddFgP7syZ1UpHcRvffgjkgUDMOtkh_z7w0J1KZNf0YjGWvfzhTVoVf2kPQ-AgP0jq8aagnJs4xyyeJKcCSOiTi6twceifKomkjZsNL5EzAb29lOgtUHheByEeX-2-UFSCsSipNRR4gGRJZb4WljC-HBI9-pidfZ34NJVjy-s4Lb5NUonmQ3t6ju2ic7_z12b8a98NjP0DXI9aVN-lf1ExLGuiKk8TcmlsSuacitNb6j92RBJGShA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حملات موشکی به اطراف شهر یزد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/100685" target="_blank">📅 00:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100684">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0TLYvedyg90K3kE8ZTVwgv15rgP9Ini0yvkzh7axf1cdRDWif72xYq9QAxHBB_8OwS3K5cTNLxVUe7ORiiVrf4nMMIlHLoyG7WtpVAPUtuELI0NlQTxQmyqErnK13rKgkPUSvA3lvmLt70ThUQkylXAyruet1r4ZBDsao2ot-obiVVb8C0N-nDhlHbY-adaYCLkR64gkXPUVRTCPdNCsd50YEjnyiBLdV5guQW-ufjVgpxuiaUgrTY3DDeMtsIF_3YwB_0cHQ5Y3gq2uuqc6Kx59GIY-IK2oPBe-Bx9T9sCF7cidSnFlv6uQAEWmydE1hbV4PLIlxZzwmvu5wQVCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
آیمریک‌لاپورت مدافع تیم‌ملی اسپانیا
:
از رفتار فیفا با بازیکنان آرژانتین تعجب میکنم‌. چطور ممکنه یک تیمی اینقدر حاشیه داشته باشه و‌ مجازات نشه؟ امیدوارم در بازی فینال هیچ مماشاتی با این تیم صورت نگیره و در زمین فوتبال قهرمان جهان مشخص بشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/100684" target="_blank">📅 00:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100683">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/901c95f7ea.mp4?token=D2DirjOoZZmfE6QeUg-rzkaU7xUbsZ97nRky1V9Z_RjE2iHnHnkGKXfJp_wO99yKu24RFiEB0Vm6FvYiRulO3L3a8MkVDEShtS16UEpSpMHgavOI6rX9-8AEWDX_fP7a1ziRYlPdxFxdo1HV2DZhfckDIOJpWHYylGxYLG7zv2lunSisWwmMK5p4_Sg80qVgVRiJ0qNove1uBbORjtKuNLcR80cqcS5gLd3zgVpXswag3Lx2ke9fmkLhZFv9eOQk0zuURrzzPBjxe5lznSYYFmlLPSC5rp6rzJbphJH1g_mwl--lpNas3TAECJMwMiyTqf0AxOxidrohwpSNpfwhqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/901c95f7ea.mp4?token=D2DirjOoZZmfE6QeUg-rzkaU7xUbsZ97nRky1V9Z_RjE2iHnHnkGKXfJp_wO99yKu24RFiEB0Vm6FvYiRulO3L3a8MkVDEShtS16UEpSpMHgavOI6rX9-8AEWDX_fP7a1ziRYlPdxFxdo1HV2DZhfckDIOJpWHYylGxYLG7zv2lunSisWwmMK5p4_Sg80qVgVRiJ0qNove1uBbORjtKuNLcR80cqcS5gLd3zgVpXswag3Lx2ke9fmkLhZFv9eOQk0zuURrzzPBjxe5lznSYYFmlLPSC5rp6rzJbphJH1g_mwl--lpNas3TAECJMwMiyTqf0AxOxidrohwpSNpfwhqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدئویی منتسب به حملات دقایقی‌پیش به شهر موشکی لارستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/100683" target="_blank">📅 00:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100682">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/100682" target="_blank">📅 00:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100681">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPKHgR_OFj7R12YorHARABUXonZt-1ycHmjx7RFyttO5eSDUqCfePYNt3Z_Ny9uN983dVGfLV8iyG1Tc9ZsMcemcTkzFQAqbTSQNdnaXsM596kEyAt_4oviXAjBvZQNcT5Nh1NuicJPP1xLR6Nkd9t9pBpqGKX1yBYn4YFaiL5e4KQWBg-ev-bk6HFMJDFFq-8kne-Dl5DwH3SeEvL4c1teQBt-zo6T2catIkb6WWPXv8Bb_XaB7L4wAFAOEf5OzehZQHIPLJ2i22npjh-1Lah7s3L34OOBC3KDtb0FgLuF1gC0WKAyeRa1SBHRSM4xYFvheryhAk_mrYUCfyhY_9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/100681" target="_blank">📅 00:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100680">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmJiZQYYrc2MXY60lKnAszH5Hd7yaO0uS5yLLZsZSvr_GmTZk0OPvegM6BGGivMZyywRiRzfF8iJFVbAbPDwTWPfV_Zr9YVk5AzD_5dz-o-WLK1O4Lr0FpgzwoPk6TSuJ8qwoEhg29iucOZAbWL64Vsa22Wmfy92YH0Gj8bfSEVTV1HMyV1KmM0LH2oINhKBtVx0au1ugRysRGuh6_7FRLlukrF2p7z8mMie618Xck5C0PeqlgfZu7XWePc3WotKlxOeKOQPA3SuTIVc85ai4Ph-IEk-pfzCJtxqdpDCsv6ExXSBXMElJzv8e_oDKyA6PVHPmqH94T91GJ6MmKJv7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚬
🙂
شرکت تروث سوشال متعلق به ترامپ به مشتریان خود اعلام کرده که میتونن با پرداخت ۱۰۰ هزار دلار ماهیانه،توئیت ها و حرف های مهم ترامپ رو قبل از انتشار چند دقیقه زودتر دریافت کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/100680" target="_blank">📅 00:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100679">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87a84e45b5.mp4?token=IP-fyy16HbgBQOP8YGv1JCFzW8astESdOm1rZa0IMvD0COo_Hmt7U7eQOEN47-nrxbmhTYLl_bwO-Ugvkmx68x1YReftQWorP-xnruJQ3dU-nBgpyM2zEryqSA7kaBfK3eMe7hqnv7dkHIKMCZHBV7Rnd32rqdhR6p-U_U51-QzUMnwVAhcZBEeZi7Mh5dEH1eJLyNoQ5xolqNskJWh3xe-cAVOVJBkpZjhbPphim22Fs9T17R6ov_H20saFUfn2ugjDVUFs103o4hObxjuqAFrFKfF0D3xVMSE3xYqG7kxcC0ehcMJKFcYJj2sEUJdW9iMZnxy2P_wd_aRwaq5Ofw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87a84e45b5.mp4?token=IP-fyy16HbgBQOP8YGv1JCFzW8astESdOm1rZa0IMvD0COo_Hmt7U7eQOEN47-nrxbmhTYLl_bwO-Ugvkmx68x1YReftQWorP-xnruJQ3dU-nBgpyM2zEryqSA7kaBfK3eMe7hqnv7dkHIKMCZHBV7Rnd32rqdhR6p-U_U51-QzUMnwVAhcZBEeZi7Mh5dEH1eJLyNoQ5xolqNskJWh3xe-cAVOVJBkpZjhbPphim22Fs9T17R6ov_H20saFUfn2ugjDVUFs103o4hObxjuqAFrFKfF0D3xVMSE3xYqG7kxcC0ehcMJKFcYJj2sEUJdW9iMZnxy2P_wd_aRwaq5Ofw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلد مارشال رضایی
با نظریه جدیدش دنیا رو شوکه کرد :
اگر فرضاً دشمن توانست در جایی پیاده شود، چطور می‌خواهد فرار کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/100679" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100678">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAYC7G2-_YoyvTgtnbKZQZYRyyHWNqB3iau7avu6PGTkxfpXXW_fnDm7hPnpela0QWyPIYgqlvFbNOjGGQIe9UfeO3PXdxYqs17OlC_8VW87PGojc9F0rsrRYBgJX_yanG1e7KIudU0n_Vyd18Opo9YaKQnqr8_uaFpByHmCIudGnLPEB4DuSB8aRzDaeVogeoJOwxGtWHwtje4nNM6LeNk9TPlqd3Rv0JvyDE34gBPqBQPvLYj4My5XtoByLI3BI-tNt76yCcY9akP6wSV7VozqM97IXljoJYPaHNsCO7opGKf4OZUxBN3ZeKVCjJom9vZXD4D-bmkurYRW3qpQ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
✅
😍
یادی کنیم از استوری رونالدو سال 2021 برای علی دایی: یک قهرمان واقعی همیشه قهرمان می‌ماند. افتخار می‌کنم که این جملات مهرآمیز را از الگوی بزرگی چون تو می‌خوانم. ممنون علی دایی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/100678" target="_blank">📅 00:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100677">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnGGcdlp7yiB70EborBVjswLAqzNKAaud4SfPQG8faVuWBjZNBO4pFlpRUIZ1Pl_0W3WcHc1zQ2hd8TjyzYDXJKa5LMiyi1o4jQ2Fs-euE3_JQXSnXjKkMY9539NTnwtko6qR1DX_QBbJVl4X_SGNH3csN6o7UmJxl0gD7-LIAyfqQdPsJWNSD82f-fJ-pk1sy-GKTajzsPKjuybVrpi-D9uOM8q9JYqGO7Tx_l0s11eyPyXnPSc6NZpnlnmjeVCe6xJA0Yh-I3jk-IEYwstlugy2St2z5k0yHzJgwrpHhUdvxtZEkzPCzNTjbzAsZK13DBBt8Gfi_zaNQs2US5hIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
#اختصاصی_فوتبال‌180 #فوری
🔴
اعضای هیئت‌رئیسه فدراسیون فوتبال در جلسه خصوصی روز‌ گذشته درباره اخراج امیر قلعه‌نویی صحبت‌های مفصلی کرده و خواستار رایزنی با نهادهای امنیتی برای برکناری این سرمربی پیش از جام ملت‌های آسیا شده‌اند! چند تن از اعضای هیئت‌رئیسه…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/100677" target="_blank">📅 23:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100676">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFNPCITLB1pe9oL8vtw5-m-dVoMuOlj_vCv05CY4IlfyTPDpT_1r1LfHqoCk_dGoGaO82KcMY0htGPqwQoLDr6qN_2_0nMQO9cTT_RzhWTl1l7XD2MHUIp2yytASwZ2xB-jReVJnWPAruQa_-MKOPPY2L4rQrFd93nnOzLwtLEwoMKHf0KuWr-_u3ABO9qq6ZE95UTgUeNjdoXFNSy_bJE8ADAxhi9nJ2TFTaofcSZEwoggJi8R25AwdvMysymUXh3BpjsJijMGdpEGKuNeQPN34EoALD-VWsJsn9EbFhDmi4vVFTYmvlRYknyS202buuSByBEPaFUaFCQidbohxdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
رونمایی رسمی لاکرونیا از اوبامیانگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/100676" target="_blank">📅 23:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100675">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
سنتکام: دور جدید حملات ما از الان شروع شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/100675" target="_blank">📅 23:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100674">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdO6pfy7H4Fmsq3hgbRr_hKm-YRpqaqRM3PlsseQg1FhX2cNTHIf50Xm74p2-6EYl1I8ziNpIa9v5vYPbbEpBxZG9hmUn4fmx1_BClGZN4Y-gk1UCGRcDgp4MCNCBQ79rfW-irzM6M1Vhm44RDlPK3Ul6bfy1mz1d8ydDPVz7EUiBmmYoypJyOJO24HGW-d3-9ZSjD6j8FzjbPaz_4hb0N1Hb_4kTq0U3rNXrV01HmsmPfwbZfBP5kTC0WpifFok-8O7BzXOEAMWRp6qHjTXycAGPaYkiMRWxCh1xsCqK9VsS-VCeiD7GZU3N2MmCTHj-7XlALWdmiImM20pFrVuSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سنتکام: دور جدید حملات ما از الان شروع شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/100674" target="_blank">📅 23:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100673">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cA4T8-3cX4LoT5x3b3zLxbaNf61WDTa1iKrVe3rC9UnKWn7tXk6jkBE56ny07yG_VZ90fPkfCYd_wfmSY2UbI4UxB3DKqitOhzD4DkDey5u_dDuVr7BAMK8_nQuDjbCxk1AW10SEC7UhpTgw83EYSUXmloIGJ4UzJH4uIFAFPqp274RykigM6nObhJoZpxsqD4itvzJQyVQLwMO4DV7itnPDFTTUH8AA6cDHOKOETciF4mDJRoviuPw6EWDwTOrFnf3nDp2qyN2YiGULkKqKvEf42eoVU47_-CMi-IRLOrX-tdaIe2bqXqQ0GD-KEavB10iKUuIgzrOADzq9xIsW3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
🔥
لیونل‌مسی: اگر حضور من در جام‌جهانی را به یک بازی رایانه‌ای تشبیه کنیم، من تمام مراحل آن را در سال ۲۰۲۲ تکمیل کردم و اگر الان هم شکست بخورم برایم بازی در‌همان دوره قبلی تمام شده و تفاوتی ایجاد نمی‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/100673" target="_blank">📅 23:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100672">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEDqNvYLYKd-M868xN6ro9g3rHcMMBwO9_6oxHcJP3D77O6cNmqd2hhDDLFl6_JYdbX5IT5powCokoJON-Kb_NHLlE3C2GbrFFaI-P1oBzJm5X_Aaqy8rfMb5fhXepK5WZYBR48EQdjUL2jCQp4ywklPz8Ju5L4Cr39-Wq1DjsBvORDOO8l7kFMdDc2JCzbzHiOYyyneYZdowqNRndI4Ry47ZSWGgQEj049W_7kzLcO6Ef4RXo0IRKYZTaQW2zPxTU3TYgQVjOnyMD2zBAeBP2nrWT97q1C9-QBsZU6NatB59-DB738gB1avKAzKDr1lKKboN-jI6StAFEH09OyQvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
🔥
لیونل‌مسی: اگر حضور من در جام‌جهانی را به یک بازی رایانه‌ای تشبیه کنیم، من تمام مراحل آن را در سال ۲۰۲۲ تکمیل کردم و اگر الان هم شکست بخورم برایم بازی در‌همان دوره قبلی تمام شده و تفاوتی ایجاد نمی‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/100672" target="_blank">📅 23:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100671">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe058d325f.mp4?token=HYSrxt6k2J8i3H3QuB_iN0Jcs7LheL8L01SUCQSnsGZIj4963Q00QyYCLMBWv06g1AxBXSCSvTJ-o5peKCkNSvH43j4TJ_e1sCvym668InODxEk2m8ukmR4-gsNIqBm_imLLWEgz56KxyJ9Ovmm4kFmzMXIlz-CeivWVD2D16K5O-wmCkHzpWXbBNioXS6CrjjeNYBzKPS78QQ5GMerttlPOLq6r1XaRIWkzxLXG3rNHiOf0uWz8LZHDTy2pd6fjGwHurF0LRQFOzXp7C-Tssdv0bkt-77RLJnby4CF8rPmnYQMVMNWMnr1BYJHEVWszwHIiWCO1ks8_VoRAgBGKfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe058d325f.mp4?token=HYSrxt6k2J8i3H3QuB_iN0Jcs7LheL8L01SUCQSnsGZIj4963Q00QyYCLMBWv06g1AxBXSCSvTJ-o5peKCkNSvH43j4TJ_e1sCvym668InODxEk2m8ukmR4-gsNIqBm_imLLWEgz56KxyJ9Ovmm4kFmzMXIlz-CeivWVD2D16K5O-wmCkHzpWXbBNioXS6CrjjeNYBzKPS78QQ5GMerttlPOLq6r1XaRIWkzxLXG3rNHiOf0uWz8LZHDTy2pd6fjGwHurF0LRQFOzXp7C-Tssdv0bkt-77RLJnby4CF8rPmnYQMVMNWMnr1BYJHEVWszwHIiWCO1ks8_VoRAgBGKfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
علیرضا فغانی: بعید نیست در سن ۵۲ سالگی در جام جهانی باشم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/100671" target="_blank">📅 23:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100670">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19b30c0069.mp4?token=u9n_vGkXRKnuxoPUQ1qQ3jMJnESFxv-30Cu2oJnjPhkQ4U8pPO4I9GcJYj5Yp3-QWTs0R-9q8lH-fJ9UI-T8pjCYd9OjJWetfr8nIuSFHXVdW6OxVaPAVYbOy-ADPEJK0UiMLcJfmm7IV5jMEDuFGAPbEUalIUIe8ziuoYgp2ncw7MpTY7b0GO9nxQAf15YW3BVMb4YrM_-oo1llgnYuX6bbDtq-oHVonMtdIdDG9Xw0lIlfDgNvGY9sGSqbtKjT-0QEYVaAdz-vd8FCO949LH2pVAoU_21VKKg41kiHMXirMluXwqdQodQ9EXrWRYtihoigZLTeq1fnmDPXKcG_WIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19b30c0069.mp4?token=u9n_vGkXRKnuxoPUQ1qQ3jMJnESFxv-30Cu2oJnjPhkQ4U8pPO4I9GcJYj5Yp3-QWTs0R-9q8lH-fJ9UI-T8pjCYd9OjJWetfr8nIuSFHXVdW6OxVaPAVYbOy-ADPEJK0UiMLcJfmm7IV5jMEDuFGAPbEUalIUIe8ziuoYgp2ncw7MpTY7b0GO9nxQAf15YW3BVMb4YrM_-oo1llgnYuX6bbDtq-oHVonMtdIdDG9Xw0lIlfDgNvGY9sGSqbtKjT-0QEYVaAdz-vd8FCO949LH2pVAoU_21VKKg41kiHMXirMluXwqdQodQ9EXrWRYtihoigZLTeq1fnmDPXKcG_WIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🏆
علیرضا فغانی: برای اسلاوکو‌ وینچیچ هم خوشحالم، انگار خودم داور فینالم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/100670" target="_blank">📅 23:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100669">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4P3pkge5k0dKAy2LpmiG3mq5gNzNZ-rqAAdU6Q3vkTL7ZzwlDrdJ4yXclfizx0S10Op4U55jIR_dbT9NnBQvFZo06bqZME5UdU-1H5T2uOYwJgD5mHd8ljtCKne5khhji0UInGTI8mRzF0JX7f85Q5Nyu5XiVyWaFDb3crMSJj7FgnYbImO8BL3tteLiXgcMKs6dIa13IE5BCkWZNG9UndObiQh-l54kBuhEq1P4-i7Xk-T53nI3H45KIeHPKn9KNtkj-c0xZNO0psMUB0c0VYUW5R7lu4HuGHKi40By15Ak9SztOCWrGnw9E8FVgVGaIp7Ad3qJWYO4YrUOpx-Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
✔️
رودریگو ستاره برزیلی رئال‌مادرید پس از گذراندن دوران مصدومیت رباط‌صلیبی خود در اواخر ماه دسامبر به میادین بازخواهد گشت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/100669" target="_blank">📅 23:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100668">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3Q0YK-6mLglyAbuCsfZf6l64c5t3gu9t01HKueuLvo75KYhvxPRM87Ekz3eu3ibjHxOKRNbpJDNcGHcPnnuoXe_zxqCa0ZUBrHt0p7rpfWtJMXvOTx_XiaBDybijTn9iBOybLqEWmbLJRn_1ql0sAo9G7NKZW1Ww2eGZDjiABo4544g4FOlRNm5Fsd6RkTFAcrwujQPRA7EP7vLln8aD-tHtFtAW9baqthSg3CrrxXZ78ANS1JXtDFxAgNa4ALkrgKC19ufzWhSzxWNEjEajL9Van11VWzmwg9f80PmVgRsqx9ZfG7RMp2pZb-D4VsYb3dNI0HW9e__AF4lgsFvCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مکسنس‌لاکروا مدافع کریستال‌پالاس مورد توجه آرسنال قرار گرفته و مذاکرات ابتدایی میان دو باشگاه نیز آغاز شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/100668" target="_blank">📅 23:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100667">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">لطفاااا فیک نیوز پخش نکنیدددددددد
خبرای دقیق رو اینجا پوشش میده براتون :
👉
@khabar
👉
@khabar
تهدید سنگین آمریکا برای حمله شدید به تهران!!!! نمیخوام بهتون استرس بدم ولی این کانال رو دا‌شته باشید
👇
Khabar
Khabar
اینجا موثقه
🖐️
🖐️</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/100667" target="_blank">📅 23:18 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
