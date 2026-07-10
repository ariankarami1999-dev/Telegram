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
<img src="https://cdn4.telesco.pe/file/bxX24fpGpzD1IT84ZjRrbyD-jykMfcUgvVZGEjfUtKwW5SIY16NYAt5U11e6g5XdYE1DyagqT9I0bACtNzhjZqZNWscWfzQFQ-jTYgYDSbZkmKKegUunDxnSIhJVyfJoiWK_bHacvjY0Fr5b0wHF394syS6h9vkJhpHJElYqVFTTB0L2p8ywwzZZYjU3c4LSmlUwMJ7qFyAPO_Cej1iYGkBKp_VXPml9uoFUnJ0EPT70_woxeWjDFo0v1dVoy02ew4F-3FX3hnU5vDKDS6e5fFumCiXaMQcim2K_bxHvWsXN5FzChEKjTFwtEKrpxBjWHDR5hCPKeX4450-Q6PhfZg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 13:54:21</div>
<hr>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/snnzMcz3inFmx6TanG6GRCd7O9p-D-ITlYAnw1PO4pKhyTt9TcHO75KRhdMUBBV3y-9h84lyQeZQ_bQEydzSFmi8B2jDyz3vaIPy-EY8vtx7mkIG6gTtgjxrlkeW6I7OX7JK56UMSD2r88bFsy_EguWzvxYwAVvYh2o0XJDKWlksI-VTqaurAUMFvbWRXI1PVjAWQ4eLDOW75Y9WmMcYtM9y6WD78p5DmtVEiZsMzRn6MJA6HQJ-Kh5qmTwvEErLU96wwVkia6sSK-_hYlFGbOfQwtghUEQFPOoiLt6NjA9vgHY7UBswCXnUmifw0ulJoeXN_rXsy1AXxJSnAI8Gow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f2581pEOawJV4mFu1HSOkfAfRRmx88xCqz9n_xBfcTZIT6BqUIwdK-sU5_zsA1F5lqeIc05FAY1PqR5RdLZN7XeSfaMtSI8rhEpb8eY_iMU9FkEv8Evfws39KOLkyAO926Lqy-jhTG3dssgp1yfEkNPMJl9-WDUG9aVRi59IDnausAglgx1DN9b5xf2Q1-6qZnZSyY5IfUDSES9TKJX-5UUDfQ83HG5dtv-6bcyiEAlnYS2HEFXPmkOYGFYJkyhenBTO-MiHCsav0ZwU1hiwiGeQm9URhdH4NoKYQpMQbUw7V8nzk_YgMxJ1qdtWaj9PeoDrm5c9d8jgdHg0DiCoHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2naEIcL2NC_h6Fjt8sDJBD7SUb03fbu2o-Z0nrEx2xvNue8iRggYWC70qMOVVxYl86wxs39FYSHBxsIuXkXQ1VLoLwYU1vtRyBYW-Z-SyYX-PNdvdbFdOp26X1f9hB57QOkZKzD7tIzifSZOTkvJx29mVIbJhv36r70qC4JjlgeeYqGNbLzfrRWehBLGNty3Eqe2HFydwGdKPLLCaswJ9Gfs0QsaygkGUF1JDbne0Ees3ztu46L0o6FzNzqHBl_yODLEjdhAnRQH5u98Whn6mvIoKyg_k0W8fhabRSDxx5BlqbNjRix5hf7sV9bbC2SwrmxgdHuh8asSqpTWNKQzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177Fqli2_fLbB2uW6Q92rWo33maiZp73yFMdtvOTMCGwVKGzE7rYHJx3yXXCpOONc_pxA0OoN-TcRu6rQC0yucnz6pCSFmlRkUEjJYkojg7OvgwiCPAlnAzWM-FpDO2PGdJcJDmul3mlPkGmJweyBILOBnFhLXmdixaTm8ZGonO_km7-ZcE_aL5fILWrtLxyLshlzi8znL3dyrXjlOEdXKsuvnCodgEJF6wxSOmQJLiuzt-t7dmqOd1vxfKy5WMcoD4AZzdGYHdGlz_Y3hOZrb7Cw44UklTSg5JCDNeCERw5EBOFdohp741o6ajUW_zPZsnTNi3WpnN3p-BXfM585zbVjsuU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177Fqli2_fLbB2uW6Q92rWo33maiZp73yFMdtvOTMCGwVKGzE7rYHJx3yXXCpOONc_pxA0OoN-TcRu6rQC0yucnz6pCSFmlRkUEjJYkojg7OvgwiCPAlnAzWM-FpDO2PGdJcJDmul3mlPkGmJweyBILOBnFhLXmdixaTm8ZGonO_km7-ZcE_aL5fILWrtLxyLshlzi8znL3dyrXjlOEdXKsuvnCodgEJF6wxSOmQJLiuzt-t7dmqOd1vxfKy5WMcoD4AZzdGYHdGlz_Y3hOZrb7Cw44UklTSg5JCDNeCERw5EBOFdohp741o6ajUW_zPZsnTNi3WpnN3p-BXfM585zbVjsuU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما
که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!
همونجایی هستن
که بهش گفته بودن
نفت آمریکا در ۲۰۲۱ تموم میشه امروزه
در ۲۰۲۶ آمریکا بزرگ‌ترین تولید کننده
نفت جهانه!!
سال ۱۳۸۷ گفت بر اساس محاسبات کارشناس‌ها تا چند سال دیگه  دلار و یورو نابود میشن، در عوض و در عمل این ریال بود که نابود شد!
کلا محاسبات و آمارهای شما همیشه خیلی دقیقه!</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6000" target="_blank">📅 09:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=qKuTfaYk5kX3pTKxI8VAA2VouOmw55mnpsNSda0nEw-KC7gQpCkt9rj3cNvJbUDno_ymPfEtyf8BvL8XQMbX7nnWn3EoNavZbpCEVmWO5d8LMdf4SaHYFWimSQM6aJ3fO7MQYOxVvAuOzY2OnvkBpPW0nkwrmw_VT1qIvJ_0_UwSkB4ld_2cIo-4D0iFo6bvNf9eyVxguwZSQPnVxRwKraiFFcZOXTYk8Rlz38Bbq1F1HqrHHIigqT3KnnbhiKLjSIXOeYatf9tZKbioMhnaxCdXkbXCO5yUrxxjtfctaaO9c5T53Er3V7XMhBVu1vnrci9klhoRGNybHaNQzad_bxf_M3bkOuM-jE11yUAJ9-qmIvMnttSXlbFghOOwfKvAINnNVpeAr-0_M-fmgS_eBAJfeim2R0P5SXTE6_gH-HuRs1v7EOwDLZa9fzbOZoFuS-Q8-EUwlFPQT9VXY5lQRPjAOaeo0o4zeDMvhtbv4Pg9mgx3slPFHZ1zTJWOq82z5J7PtC6WHRaPryeOGha4pB_49SUklw18muLievnm9GQiHKHjNkS6nJ47GwLsf7My9CaYeusmscjKUMkqzsQD4aMGcsTQm6TuNnc02WQfxx_TuUpWeWFWuwbGuswUvrhWB3-vn30NuVc2qjYtzuSd9kOysyWnbM_96Uqvrp1i5eY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=qKuTfaYk5kX3pTKxI8VAA2VouOmw55mnpsNSda0nEw-KC7gQpCkt9rj3cNvJbUDno_ymPfEtyf8BvL8XQMbX7nnWn3EoNavZbpCEVmWO5d8LMdf4SaHYFWimSQM6aJ3fO7MQYOxVvAuOzY2OnvkBpPW0nkwrmw_VT1qIvJ_0_UwSkB4ld_2cIo-4D0iFo6bvNf9eyVxguwZSQPnVxRwKraiFFcZOXTYk8Rlz38Bbq1F1HqrHHIigqT3KnnbhiKLjSIXOeYatf9tZKbioMhnaxCdXkbXCO5yUrxxjtfctaaO9c5T53Er3V7XMhBVu1vnrci9klhoRGNybHaNQzad_bxf_M3bkOuM-jE11yUAJ9-qmIvMnttSXlbFghOOwfKvAINnNVpeAr-0_M-fmgS_eBAJfeim2R0P5SXTE6_gH-HuRs1v7EOwDLZa9fzbOZoFuS-Q8-EUwlFPQT9VXY5lQRPjAOaeo0o4zeDMvhtbv4Pg9mgx3slPFHZ1zTJWOq82z5J7PtC6WHRaPryeOGha4pB_49SUklw18muLievnm9GQiHKHjNkS6nJ47GwLsf7My9CaYeusmscjKUMkqzsQD4aMGcsTQm6TuNnc02WQfxx_TuUpWeWFWuwbGuswUvrhWB3-vn30NuVc2qjYtzuSd9kOysyWnbM_96Uqvrp1i5eY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مداحان اختصاصی خامنه‌ای،
که توی هواپیمای اختصاصی که تابوت خامنه‌ای بود، از عراق بردنشون مشهد.
نقش «مداح» چیه؟ مدح قدرت رو بگه
و بگه شما بزنید توی سرتون!
اگه یه عده از شما نپذیره بزنه توی سر خودش
هم حکومت میزنه توی سرش و سرکوبش میکنه.
اینه وضع جمهوری تباه اسلامی</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/5998" target="_blank">📅 09:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qnekhk6G9gitDyPDZAw2NtW9oXaN22gYXz_9JlkcBegjoOEBqadvSBFdUQJfTJ0-UJZxlHKmBzLlGmZoMtlv1t7BPC-ES53uHwX_jEq13hbRAa1nraD2StHvYPWuK3hPvfj0SRcti8HsqhJir9seQdWRe9X3MPcbHfCC_3E16L1xe_boi1Wzqhpq73fVsTT4RpwsXIdtEAv6VgSSXlFeoFtQigT1l6wqiP5o0rkV8dwfcsMwOX4flNoA76YLVsCgVKnzSgXyfeM9d5lzJuzM35zo1BPLFpgOLV-fteiuLdCZstd9bAEc5bAwGkyCh17FgWByH_xEmD81g9c6xKuChQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان : اسرائیل اطلاعاتی در اختیار
آمریکا قرار داده که نشون میده
جمهوری اسلامی طرحی برای ترور
ترامپ در دست داشته.
(این چند روزه در مراسم هم پلاکاردهای
بزرگی به انگلیسی در دست داشتن و خواستار این‌ کار شده بود، مجریان تلویزیون، مداحان و روزنامه کیهان هم همگی صراحتا خواستار این کار شده بودند.
ترامپ نیز در ترکیه، زمانی که از تفاهم نامه خارج شد، حداقل ۳ بار گفت در لیست هدف ج‌ا قرار دارد.)</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/5997" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLt7piwegmwr9yR1tpqHsuMNyxHBTpGQt9S0Hg0hPfau8WfCLj_OTwIe5NuvGIFxRpe6CjLfCSk7zH7aZScDOmpMbhae7RK7mYyzhn3mILofWCix87ipyc5DmupNSND5WfaBPMwB5qSnjjblsiBeMbmIfM2tGVVzCbGAMPnWBPdukf0dhi2EicwTNi2FDGyTQyCMs8kx3UQmDvJqgLClzYHPu94U7m-Lp174GmU7LcPmlp_CW9tIM48uc_efUW4m-tBY_foioNAdztHrTmBM5XQ3LWY7iXfrrN3ijETGAtUpZkd9nIjUfq7BCKL_cXMKBtU6tat31cfG-Xv5c3Cruw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام - فرماندهی مرکزی ایالات متحده:
‏
🚫
ادعا: رسانه‌های حکومتی ایران ادعا می‌کنند که عبور و مرور از تنگه هرمز فقط از طریق مسیرهای تعیین‌شده توسط  ایران مجاز است.
‏
✅
حقیقت: ایران تنگه هرمز را کنترل نمی‌کند. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از ۸۰۰ کشتی تجاری و ۳۸۰ میلیون بشکه نفت خام از طریق این کریدور حیاتی تجارت بین‌المللی کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5994" target="_blank">📅 00:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5993">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pabgq-du6dDgLFpsDNMCzU5VShy3qM5jEn06jg-3MbuepfgVd7fuTEIi5hUwXjKM9_1MFa5fBZStC8APTW7m77xLob2kSXU8Ujvz3kkXZ8wezDDG8-9Nac7Yl9HMsIwNWQXGHrOp2eqArf6QEgYoGhn5g3Hq7-BEOD8ByLc07dpAPt9wjfjBbgOeitYWYzgsA8Jt3k7ReChTcOhdkWJ8dPPj3GMKxv1hBnxqneZZpVut6EoUe-2XW6GwQZVKYaZ7k0QrrQ8JPEFDQKK60jDlgwpydHoIWvC8IPpo4dygreiKJ62t1ujiRuQNPWxzhCN35khuuhgq55S_JP8GpOB1uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5993" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5992">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">فرماندار کنارک از وقوع دو انفجار در منطقه نظامی نیروی دریایی این شهرستان خبر داد و گفت:
این منطقه شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">صدا و سیما : هیچ انفجاری در شهرهای بندرعباس، قشم، سیریک یا جاسک شنیده نشده است.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5990">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
گزارش‌هایی از یک ترور هدفمند در اهواز.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5990" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=quRvkxBN-Xr-wOx4666BodHr-JIZ-AkArTAv7Ob0DaVZYl4P7VqxXPpRBYPQL0NqN_mKyQlnT930riRGJJ-K1dvEIWwP3w1S0iV_dUSVeJbEn_pY8MOih8LDWO4xSG1tXmwtg5eT0iM604W1c-mNjAFCgefmPgYWq4NZVEL1pdrgx_WX0FSl0VyGp9m1hH87wTxA7ICaeKc9BDjem6Ejr45t8ywgAUaPBJe3evlKGxrZidzZ02ULbzomHLGbDOkaGmxwTBflgAb6-L-4rLy0zDKjLb3iH7_CLAWeI5tiGoPFzqzTnmo4M0GlsUtw-YimFqtrW6YjHMFc6DwuiJAZ_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=quRvkxBN-Xr-wOx4666BodHr-JIZ-AkArTAv7Ob0DaVZYl4P7VqxXPpRBYPQL0NqN_mKyQlnT930riRGJJ-K1dvEIWwP3w1S0iV_dUSVeJbEn_pY8MOih8LDWO4xSG1tXmwtg5eT0iM604W1c-mNjAFCgefmPgYWq4NZVEL1pdrgx_WX0FSl0VyGp9m1hH87wTxA7ICaeKc9BDjem6Ejr45t8ywgAUaPBJe3evlKGxrZidzZ02ULbzomHLGbDOkaGmxwTBflgAb6-L-4rLy0zDKjLb3iH7_CLAWeI5tiGoPFzqzTnmo4M0GlsUtw-YimFqtrW6YjHMFc6DwuiJAZ_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIpLlTI0pELFXOsNeFkZw5ajMZbyea7hENTtUPJQpK7rD4cqzItgPA8iR8ItnUvuhVuvAgH7jxbhBcTZN3eXjPTJLgcstdANXgCfoK0ZpniCxfJdxOFNUlftaaBcpkoeLYy7mRYnH_MJOK-ARIWvQal1GomGdPcpcYKC9lPU0pxunj7KWeykYuFBBU1BmH6IAVsrCY5q6cTfyyY3_FIUatv7Wb6AuO3qvIFlbiGK0iGNIkR7zRzwO-K0blK5YxkxqovFuOEP5N0CndrQERqAugZUHuKoZeNG_XDCu8jw7bLKO1y7l-8w8g-luImbBe6tcCK9wWGRKdbg0zxs22WlvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه‌زنی ‌برخی رسانه‌ها:
حملات امشب احتمالا کار
کویت و یا بحرین است و احتمالا
حملاتی موشکی به ایران صورت گرفته.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5988" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس و العربیه به نقل از منابع خود می گویند امریکا امشب حمله ای را به خاک ایران انجام نداده است .
ممکن است حملات توسط کشور ثالثی انجام شده باشد یا صدای شلیک موشک های ضد کشتی ایرانی به سمت اهدافی در دریا باشد .
یک مقام آمریکایی هم همین موضوع را به سی‌ان‌ان گفته.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=UyQLsBCVamwq3loJaiTHy8csFuQJ1PSmS6M9XrOEZ1tLdKaxdlSa68uGReD59QyVy_YCXuTe9NfxkEMJx3TcdtdSAqvZFX1w5xQNg7ziZJtRswHQwL7_3y3RojY6hQijVHUZBWKHdPnsX1E3HXrh2l4MtzRPrdbONOv_-eRcURpQZSza5GNlWRibKSLxBrotb7OzIv3IGURtFv23SnSHcBKeJK1faw7OCGWM366XgZ4AYTXQz2bR1WlAT5D2EA5BGvKTuA469g_I_bcebkP5bycCvJCtFoY5Z1ucAv9u90rfR7WuN-pG7cJuK_F32VuosgT0FxHuzjU1mo5V8pbR4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=UyQLsBCVamwq3loJaiTHy8csFuQJ1PSmS6M9XrOEZ1tLdKaxdlSa68uGReD59QyVy_YCXuTe9NfxkEMJx3TcdtdSAqvZFX1w5xQNg7ziZJtRswHQwL7_3y3RojY6hQijVHUZBWKHdPnsX1E3HXrh2l4MtzRPrdbONOv_-eRcURpQZSza5GNlWRibKSLxBrotb7OzIv3IGURtFv23SnSHcBKeJK1faw7OCGWM366XgZ4AYTXQz2bR1WlAT5D2EA5BGvKTuA469g_I_bcebkP5bycCvJCtFoY5Z1ucAv9u90rfR7WuN-pG7cJuK_F32VuosgT0FxHuzjU1mo5V8pbR4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا در مشهد هم دعوا شد :)
چند بار زیر این تابوت دعوا شد؟
توی میکروفون به نیروی خودشون میگه خودت رو کنترل کن!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_m-JmRV_fHXU7mn1sDvWA6PbwZgoIM1cevwaU4Ok_2Hm7dkYIFU2NIfj7gJwFlIfnrRxqLMLORZGihSiBw0F2AspfLDKzWU-uM8zkt2e9O759DWDxw-k_ZCQ3rx3JQPK6whqfNmLRMB7jizFbrZaqBpb7us862M15TtYhExtxmdsFtvXoSI7ks_D8hU3o6mrAEHQc4rIJntvwTQ5Dy-68fm1Pul0NZwP1u2H-KeTYXtjUjF0XGCJbw1cj9h7d9_Y0frc9rw94vPkthmHHJT5c22i7Cg4Cb68f00fRvQlRFNecr-7oqGZemnkrWpGpSJDIs9GMYhSknnS0xtog59uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jml0TeZ3T2Eu_E3dvu2omykCqQEjPIqgR4KEaFwJfYlCK1_VcOYJWk1Tkmuk2da5PyyTIyQgk7KwzGvVQtF6DSieE_4Or5Kj8igscYyOQQ7GUx7bor6zBJ0VwbwitPLgUeGOViwp_z1RA_T792aqrYS5DGGaSncYUC5UwYsxjg7Vk75BAUfPj4hTQvFH2W564npjcXpkumN4-hiecdWU6Yq3OwAe0kav593xBBYumiGNaGxufqpjgPS9mPfGEZ7XcZ1bK-6OKucgAdzE-npkXy35XyJAWf6D8xkc18aHl8e87PZ8BqlZvDk9Byu4unOjW-Dz1OBdZYK-BBJdViGflw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=ZNUxZftBRfzD14ilWw0kBE6ZTb-IOHzI21m-yTyv2SFRoQ6r9ARVomWwzqXVjiUkIv-jgK99U21MYafpScixYEajxTUT-6ygdVjO_xIuuZWAV0wGW6jbf1JHsOTVDM57opzu6gdtVoMFVJJ0epwDuoBbu5SwihhiwTe69o-engpOoLKKoTq-AJa2g5hBCb9qDg-b8I_idnqjUHRShqmpdSLRg5-2p8TZRaLaO4FJErEYXPz1WCJpYjO4dpqkqpXoGAqm2l-K-sCJpgsUs1fr2mmwOq3uyMBXjKkCEUCeEJaZwUIaqkpXjEP4vZzdk36ok8WIFtLipScvzNx4Xr-F8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=ZNUxZftBRfzD14ilWw0kBE6ZTb-IOHzI21m-yTyv2SFRoQ6r9ARVomWwzqXVjiUkIv-jgK99U21MYafpScixYEajxTUT-6ygdVjO_xIuuZWAV0wGW6jbf1JHsOTVDM57opzu6gdtVoMFVJJ0epwDuoBbu5SwihhiwTe69o-engpOoLKKoTq-AJa2g5hBCb9qDg-b8I_idnqjUHRShqmpdSLRg5-2p8TZRaLaO4FJErEYXPz1WCJpYjO4dpqkqpXoGAqm2l-K-sCJpgsUs1fr2mmwOq3uyMBXjKkCEUCeEJaZwUIaqkpXjEP4vZzdk36ok8WIFtLipScvzNx4Xr-F8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=PyQmjT3-NLIGXGkCgh6NMM7nBmH2xRfCeV55XuhaqG0FFYMx1HoRpNCWBZ7akowDm78b4XvTmBYda-iueZiyIAB6RcnPi-JAUlT15sYmcR4vWFkxIHGZ-_xb6mCETJqTkEJ2NfYrs_OKeatfS2OQvuJ7tg0H5h45ugh1swwR8BC9dMN9u0yhMMs6MDJckZNttaeqCKLNPWn67XYjn0mKB-T1TsaM1HB0TdSTE_V0lisVrDtleL9jqR-B2TVtVase-P1rNHIru7z7V-r4Auea8t4u_JAjs5eh3fHX-fhPlfs8aWQj8l9HY2Y0zk9XkIjr9cragG-zM6bBPnWsp2wdzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=PyQmjT3-NLIGXGkCgh6NMM7nBmH2xRfCeV55XuhaqG0FFYMx1HoRpNCWBZ7akowDm78b4XvTmBYda-iueZiyIAB6RcnPi-JAUlT15sYmcR4vWFkxIHGZ-_xb6mCETJqTkEJ2NfYrs_OKeatfS2OQvuJ7tg0H5h45ugh1swwR8BC9dMN9u0yhMMs6MDJckZNttaeqCKLNPWn67XYjn0mKB-T1TsaM1HB0TdSTE_V0lisVrDtleL9jqR-B2TVtVase-P1rNHIru7z7V-r4Auea8t4u_JAjs5eh3fHX-fhPlfs8aWQj8l9HY2Y0zk9XkIjr9cragG-zM6bBPnWsp2wdzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش
برای بازی امشب مقابل فرانسه
امشب چه فرانسه ببره، چه مراکش
مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=XrxcGphh1uOZY6mwCSJwDEYn9irZP4Vok4Wl35sgCQnArKP9SKx3oHm6cSvoNKt7wmUD91C5ZuYAMYUDVl3f6hvGXoTOG7RqMJNnu-eOgtqfeD8cC5hacbVbVsIvRyGveCWgIGwiYw0oo8TyuuvEpE807lKsABRqp3wlCZoGpljkRAqJT_DoHYh7GhGGGMA7daPe4ghBT314EdLOzjTS8HJSTtk2qi9ZPE0AoO4Tah2fZQaHBL8DCqcclHLd-pyse3woXPW2FlGp_QMsP3dUv57K2UV-Za9J2CThxo0I6JZwdkIBbupuP4ZlfnRNu9sBPVr2uYkmjYL7aqPGv_8t6ikGKhAzaL2jYAaATtNKsrOi4bylRV5G1mMka_rVs6n1usjYTxm_WZc1qupQNUtPEl2gQss590IK8UgvKyqrO8-RbwSrlH1pJWQnd_zWeCUOUY4snAD89na8-jrQgJgJ-umbOOlUdU93OOJBTnkH5YsXQs6wZAY-hV9Yn0XXwIrQDPbZUOvPOtljmkLNUWwcGMi0xZw_E_BT7GiNcaHmCklr8ZKZc8Cbeqdp9nqp8kmSsHNH9rfp1rpc9Xg6zSGaE5n1x5rpTSNbJyr8oCd3aHCOxU1rgXDuvF-dsGROcS7Y9GGCyidfwp2-VvjqcKAx-cu3GLNdzgYQ2zQ5e7QW9AI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=XrxcGphh1uOZY6mwCSJwDEYn9irZP4Vok4Wl35sgCQnArKP9SKx3oHm6cSvoNKt7wmUD91C5ZuYAMYUDVl3f6hvGXoTOG7RqMJNnu-eOgtqfeD8cC5hacbVbVsIvRyGveCWgIGwiYw0oo8TyuuvEpE807lKsABRqp3wlCZoGpljkRAqJT_DoHYh7GhGGGMA7daPe4ghBT314EdLOzjTS8HJSTtk2qi9ZPE0AoO4Tah2fZQaHBL8DCqcclHLd-pyse3woXPW2FlGp_QMsP3dUv57K2UV-Za9J2CThxo0I6JZwdkIBbupuP4ZlfnRNu9sBPVr2uYkmjYL7aqPGv_8t6ikGKhAzaL2jYAaATtNKsrOi4bylRV5G1mMka_rVs6n1usjYTxm_WZc1qupQNUtPEl2gQss590IK8UgvKyqrO8-RbwSrlH1pJWQnd_zWeCUOUY4snAD89na8-jrQgJgJ-umbOOlUdU93OOJBTnkH5YsXQs6wZAY-hV9Yn0XXwIrQDPbZUOvPOtljmkLNUWwcGMi0xZw_E_BT7GiNcaHmCklr8ZKZc8Cbeqdp9nqp8kmSsHNH9rfp1rpc9Xg6zSGaE5n1x5rpTSNbJyr8oCd3aHCOxU1rgXDuvF-dsGROcS7Y9GGCyidfwp2-VvjqcKAx-cu3GLNdzgYQ2zQ5e7QW9AI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVznlUjjEJakcOlPAyzXk3rmdfKSdlwgHPfgVyOGhqC2fNlK29sY02Ts2Ad8RQSEsTYHEfKj0Do624n_K3cY1Xf8R-BGQHWeN1GgZF8PcxzKEj6zPdgh6AGFEJmBNoKIKfOEkW6vv8NkkGbnPdJGiPcLqNuireZ9j-o8YP9SdmQTuvBTwrLXsHD3HHd28xCE_3a6bODMWNDxMzo37OkXLniqrWiBRmkS7At5Nxx2zmd8Un7rlIy_KUTHzOfOStWV3uYNG7lG_881RKRf-w_Eee3MvtsXuqevZ0CIwBp3N9isxGp9oGqoUE3zL2kFFeQjukVwIqniKHKOdZibBzI4Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvTBwGwFSHyxWnxCHtuTg_fWthHwAkc6TPvZoA-qwRTdpO0C30PyMnhkRvwJwU8L619gU1IMHQdTCNKwQdcI9d4cLsb5y2HjudohHxC7mHrLE-i0BZ9pGB__mO3szUp73PpRoghN63Y5qG6z-f7KbnCrIOWyACP8vVeaLkz4amBvEDUXXRWg_8utuv0pV95W5KIk7AvVvyJT_idQVmZq6L0QbdbmhN0V3E__ZrV2P3NFq_IjeNP6iPcHJQZ3j7e-rbke2f0kn8WD57gC3KSFi8v7KkaRboY62I8XL97XD5PNv7nHK1c-0VEQ5HJGr98fv1e8r5aCFJJB3Y9ifCkdRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب با اینکه حملات متوجه شهرهای جنوبی بود، به یک پل راه‌آهن در شمال کشور حمله شد.
در ماه‌های اخیر، جمهوری اسلامی حساب ویژه‌ای روی این مسیر ارتباطی باز کرده بود، هم برای ارتباط با روسیه و هم برای ارتباط با چین.
حجم مبادلات هم ۶ برابر شده بود به ویژه پس
از اعمال محاصره دریایی توسط آمریکا.
فکر نکنم تعمیر این پل ، خیلی زمان ببره.
بیشتر یک اختلال چند روزه خواهد بود.
هدف آمریکا هم بیشتر ارسال یک پیام بود
که جنوب رو محاصره می‌کنیم و می‌تونیم مسیرهای دیگه رو هم از کار بندازیم،
اگه قرار باشه شما مسیر تنگه هرمز رو ناامن کنید.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5974" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5973">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEXb9B_1x-1DNTbHrxWeL90NpzogDgTjaNc5MAUDkEAulsZEVA6kHAJIva5TlmfkkIg2A8kTEv8psftxv_mxQbLwCUwK-zUF8HzyIhyKJRC2NlvZbBiDTf5Kw1p_N1S3EWW_ASgX5n1L-DDzUppG90bRhqEuQWDS6qFu_TDgELc_-rFitNYlHfzZc9Oh27EJTPs9ANs6YdgHanWLnGRB6l4K_DXoEft5RGTXuy1QvzSUcfX6OxyCJMgzUhU07QpLD6sz3_G9lAFqIClRcpVf-387bRVo1Z6hcGWOFtwWNswawmqk80UnrIkTATyYq8Svlpbf1GdPzXMyzQm93ICNhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=bPAm712jZcLn9_vJoEpmHubKYyZ2GGtyDCO4gPW_x9_HX3qVS-uCC6PsSIsGDe1s15povv8pirMvi7RZZUXgZG8Td8F8AUw9abPqVS2xikEkfpuPxci2TKCxguLBR0fDPBEuWXn4kv0LFLyzIbFN_xGWxWJpRWcjJSkaEUtkDkKNIElttXbKgPTWC0X-FXzsHOba1imRj0Lmnn0NT6FPHd7RjP7vm7TTeHb-MXa1fgLkUOrh9BiOoWE9jPnIaQHzp_V_ArFNiy9dWl1tQLuKWa07zmxAz_BjzHk6suFhdiJH_mhinzA9T-veupQcSIpp2tUCkLtFdLGbIIprzHun24WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=bPAm712jZcLn9_vJoEpmHubKYyZ2GGtyDCO4gPW_x9_HX3qVS-uCC6PsSIsGDe1s15povv8pirMvi7RZZUXgZG8Td8F8AUw9abPqVS2xikEkfpuPxci2TKCxguLBR0fDPBEuWXn4kv0LFLyzIbFN_xGWxWJpRWcjJSkaEUtkDkKNIElttXbKgPTWC0X-FXzsHOba1imRj0Lmnn0NT6FPHd7RjP7vm7TTeHb-MXa1fgLkUOrh9BiOoWE9jPnIaQHzp_V_ArFNiy9dWl1tQLuKWa07zmxAz_BjzHk6suFhdiJH_mhinzA9T-veupQcSIpp2tUCkLtFdLGbIIprzHun24WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=SO1rza4VRjiGd8u5QLqOT-xXbR_huZJOWFjuVwregghN6-CTPbtN-ktoSY4Y25OmS0_oC4FvLCyHxLtuw6ZSPziP12LRX35Du0kE_ZYwupiSTs2Bb64LxpnUhCvbKM91Uh2qRMJAf2Dn4PgTlBssSdnoGejou64FEoyvRYZqv95QobXgHDd-B3BfCUsZPQTrB6ayAyD2b3RptNXSgqqIudPFxrQh7F0fDhBmXQLwbLa3BqQ3ac3mxFrQ238ZD10bk8qBzseJiPm6zm437wVcOpDOuYfKKKD388geaQjrdEEPOb2y1538DHF6VHPRnhlJsD03MzHygd0VbMAPpmsXqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=SO1rza4VRjiGd8u5QLqOT-xXbR_huZJOWFjuVwregghN6-CTPbtN-ktoSY4Y25OmS0_oC4FvLCyHxLtuw6ZSPziP12LRX35Du0kE_ZYwupiSTs2Bb64LxpnUhCvbKM91Uh2qRMJAf2Dn4PgTlBssSdnoGejou64FEoyvRYZqv95QobXgHDd-B3BfCUsZPQTrB6ayAyD2b3RptNXSgqqIudPFxrQh7F0fDhBmXQLwbLa3BqQ3ac3mxFrQ238ZD10bk8qBzseJiPm6zm437wVcOpDOuYfKKKD388geaQjrdEEPOb2y1538DHF6VHPRnhlJsD03MzHygd0VbMAPpmsXqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت خامنه‌ای، پهپاد وار به پنکه کوبیده شد
و موجب آسیب زدن به اموال حرم شد.
یه تشییع جنازه برگزار کردن، هر ساعتش سوژه‌ای داشت.  گویی فیلم‌نامه‌اش
رو رضا عطاران نوشته.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5968">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=hHYzq0RqGFkeRHeZDtK_hIh2gayyVuG2h7xWllcVyCSyWvyaTxER1qvShxZs3d5KS-B82YKt1touEbbOPbTh58vq-aiZg01h327bIr45CPcGJ9wrvu4HDlIuMEIiACOsT5WuvAVgty6BhrS8qHtQptv4BlbGXHxU4JHUCe9wcqgj66IRa-PH9RC743Tjoj4Q9AtIwAucsHf3Fs5K4jWymDjEHxb3hDYQqAnft9nHdyhpBlJehbYNNwS1-RWchbodEr4UwN0sMMq6STCRz_hq94y01Lpr-f8f6uR5fNcvugsEp0pCUv6A7rMBIsT_Eaoz5XQLjo0dQIMVn_t0V4Gqpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=hHYzq0RqGFkeRHeZDtK_hIh2gayyVuG2h7xWllcVyCSyWvyaTxER1qvShxZs3d5KS-B82YKt1touEbbOPbTh58vq-aiZg01h327bIr45CPcGJ9wrvu4HDlIuMEIiACOsT5WuvAVgty6BhrS8qHtQptv4BlbGXHxU4JHUCe9wcqgj66IRa-PH9RC743Tjoj4Q9AtIwAucsHf3Fs5K4jWymDjEHxb3hDYQqAnft9nHdyhpBlJehbYNNwS1-RWchbodEr4UwN0sMMq6STCRz_hq94y01Lpr-f8f6uR5fNcvugsEp0pCUv6A7rMBIsT_Eaoz5XQLjo0dQIMVn_t0V4Gqpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=MugPvfNa5hjDV2XbWpBj3uimcW74R5zRY7uqWmhIMQgu0o7N61mAa1U0VR4hxUfIhJzK0dcfwtCAyav9y2d7REjfauWSnhatCHqDfHthc2mc7gsBpC4dnkdFNI5fYm35YzOXYA3Ctwv421c0pNKZhwJhCi0mBGtaa74iMeR6fJN3-Uai1RMp64M_M5d3hiW1mjf1M4DrL4duDFxKR6Ifwa0e3nyowGJy46S0LTNSWu6cc1SSrgXmOtez67fdUQNYNyzX11nkIpHZUHkyoNiljLJlic4G5MFc-V4-Ii1EDrLytuzDfT29Nlhf8BODTxm1DZsypV6VrywMfvj7DEnRtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=MugPvfNa5hjDV2XbWpBj3uimcW74R5zRY7uqWmhIMQgu0o7N61mAa1U0VR4hxUfIhJzK0dcfwtCAyav9y2d7REjfauWSnhatCHqDfHthc2mc7gsBpC4dnkdFNI5fYm35YzOXYA3Ctwv421c0pNKZhwJhCi0mBGtaa74iMeR6fJN3-Uai1RMp64M_M5d3hiW1mjf1M4DrL4duDFxKR6Ifwa0e3nyowGJy46S0LTNSWu6cc1SSrgXmOtez67fdUQNYNyzX11nkIpHZUHkyoNiljLJlic4G5MFc-V4-Ii1EDrLytuzDfT29Nlhf8BODTxm1DZsypV6VrywMfvj7DEnRtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-vp1iTEOsS-2xVwAtwdJueDHRIYsY0ESv5noRsVz01YHDGqMONnikVPiH06rQlZBePeOBEGsHwrYitsP9JNaSl0zIlbQfA1wH-9-oNDt4_Jj4Vd7Y4rw4bMnMCQXYi-DwLWBl99D-SeQifVs2zsuEOtF2WPv003WDXCakZkbjUu58vIuWrb2Xo9EI9SfXl76gob9_fGQ5vKxAQN14aUshiy91tKGLaItyz_-FHS5-FrwJkAtSfaoTVa6eywzlkbl8_V-XVsSrXYWhUp_YM1HUPBHli_YpNXIv8INFl8dRGWGOiCK_w1A-pz5tV8CflhKMtjlZ-APYB2HsdVKEyNPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=ENf1rN5bdw1jlOyC_kc_btKMkbMpINZsaHZE3G4mJHoHCSafEZryZ5XYUbD8MRcXqpyKxrRUTEFLxxQWh3YWYib4YNNVydI0fDdWoJtjaWPS8nAWd56atJ94gRj6ztoW2WQ7Azeg4trUgVbiguLQiYR9ubXCOBLfzzYr_hbVCRkAKLQJUZbPUNP1OuxbU8hDkUA0FM5x449QXJ-q1ksTZ_vBUUQZo3fXCsCcbdHmN1Gq_5hTXHN2goQnuxIGMTapdv6As0dbHwI4hrkW7myA_U8WliEsSwYBdGLPfobr3P4-8JYkYVltEDA9huOSbGvNGqTpYSN2lhO5AOZ7M5vB_EBDtCqE_HFjNjedNBpkhssgNftKAbE4YNSRqb7kMcH_kQEuPvSgUXulDuEAj5vXPN_UPSs-A0iPrsKgirRs0GA35AnqhJJrBvXqwqxObe2PiMuSf9nZK2bOHsomp-r7V-Do401Lj7fsm4hlDtyxPn-SQy685Tu15vFcSSuVjYKSByJ1ToD9hOwnckwc-VPWnqKe3EbGVrwLtwkEIn7HHXRXc049S83Q_QfHxrynW4noDpw92_z6nAlgN4W7_3anKEw-zvSdYIMfzVIFCdYBIfhSqn-q0U9spc3wMPLGmKvtaZ0bFbnT4hakVEBAOMHD2rLUddDEgqR97poiMMeS3tY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=ENf1rN5bdw1jlOyC_kc_btKMkbMpINZsaHZE3G4mJHoHCSafEZryZ5XYUbD8MRcXqpyKxrRUTEFLxxQWh3YWYib4YNNVydI0fDdWoJtjaWPS8nAWd56atJ94gRj6ztoW2WQ7Azeg4trUgVbiguLQiYR9ubXCOBLfzzYr_hbVCRkAKLQJUZbPUNP1OuxbU8hDkUA0FM5x449QXJ-q1ksTZ_vBUUQZo3fXCsCcbdHmN1Gq_5hTXHN2goQnuxIGMTapdv6As0dbHwI4hrkW7myA_U8WliEsSwYBdGLPfobr3P4-8JYkYVltEDA9huOSbGvNGqTpYSN2lhO5AOZ7M5vB_EBDtCqE_HFjNjedNBpkhssgNftKAbE4YNSRqb7kMcH_kQEuPvSgUXulDuEAj5vXPN_UPSs-A0iPrsKgirRs0GA35AnqhJJrBvXqwqxObe2PiMuSf9nZK2bOHsomp-r7V-Do401Lj7fsm4hlDtyxPn-SQy685Tu15vFcSSuVjYKSByJ1ToD9hOwnckwc-VPWnqKe3EbGVrwLtwkEIn7HHXRXc049S83Q_QfHxrynW4noDpw92_z6nAlgN4W7_3anKEw-zvSdYIMfzVIFCdYBIfhSqn-q0U9spc3wMPLGmKvtaZ0bFbnT4hakVEBAOMHD2rLUddDEgqR97poiMMeS3tY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=BL76puAAd5i-VUyOB9A0Cc_cORT_-fxikiirlOU8_Vm6EkkeyNq2j2bclAHm6LEoP8ToM5h4tJ3lf7DkHOdsoHuhGJF1EJ9uMLDKz0y7a8S2x8Hif1U3SHd1Csm33J6SGfw8Hn-OPgmKtWEEq6RK-IUJlno5HlVhmZs7W44pl-IbgFAWguL0jdFTJffw0uHod1ldINBQgZD7gMG686jt6jOGgsgy0AW7u6OkBAVXEJQkwcsDjhKLf3Ot8sUH79QH2p-cXH7t6FhLqqxsa0T5I7-xTu-CusvuNrcWax9mMTP-UIZCArfDOA_vI7ZAuz_TKMuV90V8UUQV9DT_RIbKag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=BL76puAAd5i-VUyOB9A0Cc_cORT_-fxikiirlOU8_Vm6EkkeyNq2j2bclAHm6LEoP8ToM5h4tJ3lf7DkHOdsoHuhGJF1EJ9uMLDKz0y7a8S2x8Hif1U3SHd1Csm33J6SGfw8Hn-OPgmKtWEEq6RK-IUJlno5HlVhmZs7W44pl-IbgFAWguL0jdFTJffw0uHod1ldINBQgZD7gMG686jt6jOGgsgy0AW7u6OkBAVXEJQkwcsDjhKLf3Ot8sUH79QH2p-cXH7t6FhLqqxsa0T5I7-xTu-CusvuNrcWax9mMTP-UIZCArfDOA_vI7ZAuz_TKMuV90V8UUQV9DT_RIbKag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaBL7i2gK2tKkCqv9RIUwWxkmsM9Yndq2oUnEJjob2Tnhow1Gg9VhoF4E-2ySUKaJwfUCBm0XPzLTibi2KN-g_eb9xPzSwBpVVxxvAmH4CCyKG7fRR2vj0zUsmoVw2fq_2drDENe9cBqziVvqwrJio2SnYfZjJ-lCQr_N_8H-fL_Gd0cMafVHLsjk5jdUhfJa6F8iSykkQJ6UNosyXl_rh8nD9FWufJ-TdLZyi4uKKB2MVrXdkcFGqHT2fPD7bEVXd04icMbTop6zIBX0JKW4DnMmd6D6RPJYh3_khgumFcOLZ0xmpHnPJwt3su74zbHv_sDXIBvauKotZmq1ztWjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=NtehEwTB3j1CFK6HEi13-ZPohLQuiGSIUrd9RiCGRAExcqmtABV8FJ6lf1nQIwqM18gS1GO1U8FeIcsF5sY5evv8aSPy-Rlji0IzSzLznYio_xkl35FZ5MnT1cKjCLQ8jNpUXQiZix_twybsUbvOsaBYUkRTfUc4CaPpcg_sL1HQvhyY2GkA8-OTj1LxIPpE1ZCLY-_PyoIu_E74QZFIJinx5KltevlVi0oJgei9BQxueXWdS_FQEjQqxitU1or3A9N97PmiEqoT-AOTOIdxV2XdOVzBv6VG_G3nNb0xHYjK9v-4PTekA-c9LtifZZXrQB7Z355Sl-EJ389uVrAVmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=NtehEwTB3j1CFK6HEi13-ZPohLQuiGSIUrd9RiCGRAExcqmtABV8FJ6lf1nQIwqM18gS1GO1U8FeIcsF5sY5evv8aSPy-Rlji0IzSzLznYio_xkl35FZ5MnT1cKjCLQ8jNpUXQiZix_twybsUbvOsaBYUkRTfUc4CaPpcg_sL1HQvhyY2GkA8-OTj1LxIPpE1ZCLY-_PyoIu_E74QZFIJinx5KltevlVi0oJgei9BQxueXWdS_FQEjQqxitU1or3A9N97PmiEqoT-AOTOIdxV2XdOVzBv6VG_G3nNb0xHYjK9v-4PTekA-c9LtifZZXrQB7Z355Sl-EJ389uVrAVmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله و برج اسکله بهشتی در چابهار</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5958" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
گزارشی از قطع برق در مناطق گسترده‌ای از بندرعباس، بوشهر و چابهار</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5957" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=BLyB6zNNzkHEYSdPElqaOa2ql9Vu48dVmqXqPl-YOvxyaDBbz-Vj0bylXRK5xLVA9sFq1_QKZpk-_hel5D7PGUg05G6nYhadUzcjaxPQnl7cI9cyIaBN0PpP3tweKdootO06uSBf3jZHvkell6au5vrwre0532IXDCEnQ4AJnRz6hCCVQtChaI-WIDivolXkdwyjHYM6ptiF406dqSuU-10dRQz3R7_Km6YPwbbm2MdQeJa6LmPr1dNPwTG4eSNyjUQGf8Cff1PenKKVnVf1HruEKbHgZZ9w9d16ih8idj_bhUHF4J1sI1jbmlWMNXdNhUob3Ru_NhHy7T9fNAMgiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=BLyB6zNNzkHEYSdPElqaOa2ql9Vu48dVmqXqPl-YOvxyaDBbz-Vj0bylXRK5xLVA9sFq1_QKZpk-_hel5D7PGUg05G6nYhadUzcjaxPQnl7cI9cyIaBN0PpP3tweKdootO06uSBf3jZHvkell6au5vrwre0532IXDCEnQ4AJnRz6hCCVQtChaI-WIDivolXkdwyjHYM6ptiF406dqSuU-10dRQz3R7_Km6YPwbbm2MdQeJa6LmPr1dNPwTG4eSNyjUQGf8Cff1PenKKVnVf1HruEKbHgZZ9w9d16ih8idj_bhUHF4J1sI1jbmlWMNXdNhUob3Ru_NhHy7T9fNAMgiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی گسترده در بوشهر
🚨
کشیده شدن دامنه حملات به جاسک و ابوموسی
🚨
گزارشی از فعالیت پدافند بر فراز آسمان اصفهان</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5956" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZ-xxn68DXQMUDiaX3lscMw_qYcGTc73ze-3y84gpmqJOxxaO9dswSCyIYXhObMVrOU9ug32fG_tDKcESG8NCsj1q4kNo4r6HvyBRL2RYgaopVREHzFvJ7TvZLvh6KjiArEtJqDhNXqpqFtaOf_bxx4OwyNtP-LpqATLqt_1XY1l4_YEpmjquLC5-9zb4DCYNW5uW13bobPfzB0IZeXu7zsDswEYCd3NSm-bjWGSHRhCDg2xC4gh3m2nHnBeFmRCLIlEi0lrVG7-kHwwVjQ1SQDF-JdpYF9tZWgLwAaykSXbBJvH6JAEaO28lPIBFRcTj3_7YwXDDOeI6Gpqn0Mi6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت مجید موسوی، فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5955" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
گزارشی از حمله به یک پایگاه بسیج در بوشهر</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5954" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5953">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=H82JVoPWtaJCmlHjBRGNYUPa2-m9Aio9ZWWcNPBDJR9H9mv1rJpYzuCklBM7Stt2kmcCK294U8qg2JeMcW3dxdQzoC4g2D4yA1Q_Adl8ftkXhRR9aA-GwFMsdEN5Qfko6okyL04dMhMNRpHxIh5oGEwxUVHynVNcdZeb7qTVtNGaN7rAE11n6nNAK2pUAeOgb1Ox85kxtSDpR6MnJDEXeJLMQ3G3i7eIRvh6rQvor40was4ioxkm1DqitVfzX0LjxCz-NXwMZgmzTRn0w4ld4aWBhh5aFtESPGeVAG3MlSTIvdh0Fu1rObNdV9ErbkXEFIOlwl7LB-1ZeuVE5UtblA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=H82JVoPWtaJCmlHjBRGNYUPa2-m9Aio9ZWWcNPBDJR9H9mv1rJpYzuCklBM7Stt2kmcCK294U8qg2JeMcW3dxdQzoC4g2D4yA1Q_Adl8ftkXhRR9aA-GwFMsdEN5Qfko6okyL04dMhMNRpHxIh5oGEwxUVHynVNcdZeb7qTVtNGaN7rAE11n6nNAK2pUAeOgb1Ox85kxtSDpR6MnJDEXeJLMQ3G3i7eIRvh6rQvor40was4ioxkm1DqitVfzX0LjxCz-NXwMZgmzTRn0w4ld4aWBhh5aFtESPGeVAG3MlSTIvdh0Fu1rObNdV9ErbkXEFIOlwl7LB-1ZeuVE5UtblA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب - چابهار - حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARSCTFG-sIW7DsAiRhdYxa8bRWp9SkdFVE_j18jO9QSKL6gVpyfZi86UYUofDxhSOvA9Ori2RDLa5KqtCKgV2jZsVQ1TkubVJ1oApXm_pRQl_VGUla7GrrlloaoM8oAxQ6x-QNPp11yKdSHJ_w8Sn4xOrh7HRRyhGvm4lZF5xfi6aKukNCIQV2geOTY6nKswPTnWohDz1v-bdwuWVcsm-uTJW4BQ8fSkK0LX27w8qjzjuVwUy13DCIaDnY3WcNs0ht0BIbqXQWqZpHsgSWCjeAMvQ0g6doqlHeiacyCXKxD9f15dqwVH2TpA4ys474cIna0s8EiG6Ru2UVN10cBzFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک سیستم راداری ضد هوایی در بوشهر.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5952" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5951">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حملات به قشم و بوشهر نیز کشیده شد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5951" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5950">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‏ایرنا: صدای حدود ۱۰ انفجار در چابهار و کنارک و قطع برق قسمتی از شهر چابهار</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5950" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=nPy3Y-51WO4787wPmq1MFjLOcMR4vCCm0ObHTGrKW0-YLw6icM9Mk_54Y25niovUDUf7JqrjM3QtlcNufHbTEDPef2lXrlO9U3bsGd1BM_v7T65tAfXVBzDhmy8lNoU2nJ7gHSfgXHS4CtKl-pciPxAzqqVm5YGAqkKpfvr7jSQ8MHKHKniuPtcwn4QJDWOnfWdEscEL5xOATT4kiWKtwPPAyRTTpVecln8QmZHjX9yDYiQmVDApfsSEK-_LjjnHLX5hOpEZi-iN5XFhLxgP88hrw-SXBqpBkEyffRXIq_zKW5ejU_MWA7KIqr7o6FDO5Sz2G5lG7GL7RmPbHQXAmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=nPy3Y-51WO4787wPmq1MFjLOcMR4vCCm0ObHTGrKW0-YLw6icM9Mk_54Y25niovUDUf7JqrjM3QtlcNufHbTEDPef2lXrlO9U3bsGd1BM_v7T65tAfXVBzDhmy8lNoU2nJ7gHSfgXHS4CtKl-pciPxAzqqVm5YGAqkKpfvr7jSQ8MHKHKniuPtcwn4QJDWOnfWdEscEL5xOATT4kiWKtwPPAyRTTpVecln8QmZHjX9yDYiQmVDApfsSEK-_LjjnHLX5hOpEZi-iN5XFhLxgP88hrw-SXBqpBkEyffRXIq_zKW5ejU_MWA7KIqr7o6FDO5Sz2G5lG7GL7RmPbHQXAmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات امشب آمریکا به چابهار</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vB2deWl786-OeiJEBoZ0v5hvwKCFlHQoAr0A013IQEUeH9Ip3-XYRQp6eEYnaHuG2WSkNJ1fP_--JbtzElcA6t-lLC_SSAdIQxMf2eZ-864l0L6gwjA7L2hesKL9HhDgNGk-x4SiIIllxwnhWkcDOd3HfjPHrKizl79zPp8gnar8HItsM2msTWrrlHfnHXcjnlvVpi62Z7aA0NUfqcYkAo3wc1O001QMGUxgId9SCkMXeBS_1rkKzTEjUMFuFySyjtrAJQV3sfJi8uuBphYVHEG_g3Gz5G0AwB_gp0xGcN3VKhTUzoC1Kl9Dn7E40r_rSRSDBznRyNPAHHpkFv-MWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به اسرائیل اطلاع داده است که قرار است امشب حملات گسترده‌ای به ایران انجام دهد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5948" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5947">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5947" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5946">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5946" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5945">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">جی‌دی ونس که طرفدار مذاکره با ج‌ا بود:
قرار بود ما محاصره دریایی رو‌ برداریم و اونها هم‌ دست از حمله به کشتی‌ها بردارند. برای یک هفته خوب بودن ولی در ۲۴ ساعت اخیر شروع کردن به حمله به کشتی‌ها.
بهشون گفته بودیم اگه
حمله کنید به کشتی‌ها باهاتون محکم برخورد می‌کنیم. نمیخوام بگم امشب قراره باهاشون چی کار کنیم.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5945" target="_blank">📅 22:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5944">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=Xnz6xnTkT_IlWxzZstxVlry_m8tL68eD5Pr7HDKrv3ef_eQLnoncsjEbSNQKxZx4lbkDN0mWwm8Axc2oRNW-zyVpxlmdIO2V9n9QvFkbvz0Aisu1W_z-ZB7cWuKZ7GW8hMzMT4HQURZqfV-xELLzp9Q8PBi091WmpJpkxkFjDZlgnQuv3mxeRIoiZigUGoazTYD0t8ZuKB11K-ygNqBSGW4DtVU97vbik-XuSSFC5uiEq8e49QjKI9P8dN_Pmki2DUKv0wMno1bxlqM5fNKfzy8h0cBiEQPXym3b_UFtux3dPf6d7CrN1JNCUdoF66oSsgDOpGwrM7ILlouwiKLCnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=Xnz6xnTkT_IlWxzZstxVlry_m8tL68eD5Pr7HDKrv3ef_eQLnoncsjEbSNQKxZx4lbkDN0mWwm8Axc2oRNW-zyVpxlmdIO2V9n9QvFkbvz0Aisu1W_z-ZB7cWuKZ7GW8hMzMT4HQURZqfV-xELLzp9Q8PBi091WmpJpkxkFjDZlgnQuv3mxeRIoiZigUGoazTYD0t8ZuKB11K-ygNqBSGW4DtVU97vbik-XuSSFC5uiEq8e49QjKI9P8dN_Pmki2DUKv0wMno1bxlqM5fNKfzy8h0cBiEQPXym3b_UFtux3dPf6d7CrN1JNCUdoF66oSsgDOpGwrM7ILlouwiKLCnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگفتی سران فعلی ج‌ا آدم‌های باهوش
و منطقی هستن، چی شد امروز گفتی
که یه مشت بیمار روانی هستن؟
ترامپ : شناختمشون!
و لبخند رضایت مارکو روبیو
[معروف بود که روبیو ج‌ا رو می‌شناسه
و ونس اینها رو نمی‌شناسه،
ترامپ امور رو داده بود دست ونس،
که الان ظاهرا دوباره برگشته به مواضع روبیو]</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/5944" target="_blank">📅 22:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5943">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3Zqqr4_yFJC-3bvwUD7axQGlAZIYFqgy5bXIeadIrpiG9ZMYmAUos8FQpyqyxcA13JVy44B6uTzz7HtZDgFj3W317DWxCFi4caltK5IeHTNaSiK7xBENt8psEey3O_j42fIXRnUeQ7h5DYWYQ5n_vzxotoF282vR2qd4rph4Z8qd7Y_BjgJ7AEAgpmZ4OgxlbPg1Dx10pDQSxEoO_YNLzDAyRlNbhPY9oHfGGFZ_89jOXGsotjbHZm5giFyK87tpAxImsQUtwSNtOQmgdnIxL13IXz3kaaeDkTpqS9jH-4wqo23C2w5Y88gEHjR-JY7Odyvih0-5fUOEPC9UafOJ0Kq-3E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3Zqqr4_yFJC-3bvwUD7axQGlAZIYFqgy5bXIeadIrpiG9ZMYmAUos8FQpyqyxcA13JVy44B6uTzz7HtZDgFj3W317DWxCFi4caltK5IeHTNaSiK7xBENt8psEey3O_j42fIXRnUeQ7h5DYWYQ5n_vzxotoF282vR2qd4rph4Z8qd7Y_BjgJ7AEAgpmZ4OgxlbPg1Dx10pDQSxEoO_YNLzDAyRlNbhPY9oHfGGFZ_89jOXGsotjbHZm5giFyK87tpAxImsQUtwSNtOQmgdnIxL13IXz3kaaeDkTpqS9jH-4wqo23C2w5Y88gEHjR-JY7Odyvih0-5fUOEPC9UafOJ0Kq-3E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برگزاری مراسم رو
انگار غزه است! با بسیج کردن اینهمه ستاد و پول و ارگان‌ها و…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5943" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDnEbHvTsAYza8wAR0PPORPpJrF8HphpXkaXuwu5v2cq4aZUiqLs0fca5ybngJ8wfzNTL69ox2hUqhN-Oh2_hCcaN7Hi1gUMC9soJrRCWXsvGnu-j4cYqWr5qKj0gW1cjbNmZWGx08m76qzOuTHw3EI2eQVGqQCEpPf14MeQnFa6LSw1zYH1eY3oRLFcZ1nXh2xKcZ6EMjXghR1ecgC9OKW4KIpT0YmFQ_ibffynAD0S8y3xnVWyzd1cqqPCI7r-HMJDDS5xw2FxY76M2kKca8W5Scn3ZhwNBTnqgPa48z2GU7gKY6ZLOG76WPQq4Wce72zDtS7ZCMSgNnpwE-s61A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: درباره جمهوری اسلامی کارهایی انجام می‌دهیم که باید ۴۷ سال پیش انجام میشد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5942" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=ZrrwhC_AWjdbuIaLXg24megul8I6_DgOSbY3eBp-iLSutMKOafJa2CndMOug_3Cy2SX5aflu565bGPb9ULUJoAN8AlPqntOzHJTwB3dIPdQCI5wo52qw-72cFeavQEjr7P5ZswWTO-tJ3T13KQmbxaNEQtrkgMMJ0emME3gm5X0eMCDAWjhNJWpHrKjLyQYNFmBgz4-tVr0YtcPT9RJmltkJIeHnMru7sjKgnUL7QqaXblQbxFnzo4jBMfHBK9CtUWIthdZX7GF5LoT7L7PsVx6KgBZV59nTD12AwD-h9Op8v0pS-0nMpa2Xon0x7cJfqLxBIOtjZS8HTp7BHHYS0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=ZrrwhC_AWjdbuIaLXg24megul8I6_DgOSbY3eBp-iLSutMKOafJa2CndMOug_3Cy2SX5aflu565bGPb9ULUJoAN8AlPqntOzHJTwB3dIPdQCI5wo52qw-72cFeavQEjr7P5ZswWTO-tJ3T13KQmbxaNEQtrkgMMJ0emME3gm5X0eMCDAWjhNJWpHrKjLyQYNFmBgz4-tVr0YtcPT9RJmltkJIeHnMru7sjKgnUL7QqaXblQbxFnzo4jBMfHBK9CtUWIthdZX7GF5LoT7L7PsVx6KgBZV59nTD12AwD-h9Op8v0pS-0nMpa2Xon0x7cJfqLxBIOtjZS8HTp7BHHYS0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - اسکله بندر عباس
زیر حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5941" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=nqAdY8x1hMhELaHFOj2Ap-vGh9QDoMxTMqNIlyAQPS-s0lQC2h6-PaBOOMWpbNKYUNXeG0u-RwBhefkUUT_1qsvDWF10Ax4T_JAxMwWJbUFCcPaRa4mTHqg8kVsbiI7tDeOzghmSfeIAdLezNrZGiJEoYeoehDu7qw_2QRCgxC-BJnO1KUMFHDJsLqql-AuXZX72cjbEVg5EuShfPp6pfoquQqSSjH_keRaOODVD5w2zKqpFnmxIuKDDREQ0rRKbpH_uaqIFn1WIiV9zT6jakbVLfRIhw7EeAmHgD-SM1mFz4DvybAzpfVUSsnNiKXM79TzGWRynwzdl9QKlvw92_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=nqAdY8x1hMhELaHFOj2Ap-vGh9QDoMxTMqNIlyAQPS-s0lQC2h6-PaBOOMWpbNKYUNXeG0u-RwBhefkUUT_1qsvDWF10Ax4T_JAxMwWJbUFCcPaRa4mTHqg8kVsbiI7tDeOzghmSfeIAdLezNrZGiJEoYeoehDu7qw_2QRCgxC-BJnO1KUMFHDJsLqql-AuXZX72cjbEVg5EuShfPp6pfoquQqSSjH_keRaOODVD5w2zKqpFnmxIuKDDREQ0rRKbpH_uaqIFn1WIiV9zT6jakbVLfRIhw7EeAmHgD-SM1mFz4DvybAzpfVUSsnNiKXM79TzGWRynwzdl9QKlvw92_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مراسم برگزار کردن … ستاد برگزاری ، هزینه هنگفت، ده‌ها ارگان و ستاد زیر نظرشون.
بعد کارهاشون رو ببینید!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMPQd_ilLznV0j_CYJyxvk8ddXuYapHgq0eQh933A3ouv8sTIVENgdH2JKgG6H7p_JlZcB8zsCWsnEBFMerhGY8j7JAXYK9Hi_7ITAihyyRZLj_CS65iBcJiAiQnjKvSOy-9PG2SJM_aTRaZMKoxymfUia9NRXUaCHBfWTzPdx7uZSwHqoW5LxdJj1Iue47ZYa94ryEVbYyueowkJU3fAicAU9UCJBpaVv-eYzQwGo17fAbfmxhiOXXxJMsj8GMKAUpY0HosLv6Pk94UsO3MLo1QOhJgu1FyOWl_TRh2PG8vnJeUVmoV6Gs2EVSJiF0YB_IP5Cpl_WiobAbkqao9Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کشته شدن ۸ نیروی ارتشی
در جریان حملات دیشب و صبح امروز آمریکا</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5939" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ: اومدن خواهش کردن زمان تشییع جنازه ما رو نکش. بعد وسط این مراسم حمله کردن به سه تا کشتی.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5938" target="_blank">📅 17:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=L8a7Nw_309jYYczwZwaFd9roHSyBIerwcZq9Kk8VpOjkVC4noFyHC0WMZg6Frl7pYjZK4Y07Yigj9GjNj92MILhhoxOCnJbZYdjvOrdxhMS7xbxTW8iQmEbBUaHjs3r9W6gQ3bt8thvqbw8eCO5NTp3HgMmN6bFBxK5AnjDRT1qkOjOGRlYiSo6uap-DND9cPNsxT17E48jF-L-9fWr6hMnu0Y2KC_DebrKSU8XABJGbePzSiXm35s0mAckREIiGP93wnLRcxZQLqQtxx2UEQrG2xHU0ZtZs9vQWUMFb6SebCPtgULxvhObw8rMhMTeN8-DC0f5vkDv7lCU4n43ABg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=L8a7Nw_309jYYczwZwaFd9roHSyBIerwcZq9Kk8VpOjkVC4noFyHC0WMZg6Frl7pYjZK4Y07Yigj9GjNj92MILhhoxOCnJbZYdjvOrdxhMS7xbxTW8iQmEbBUaHjs3r9W6gQ3bt8thvqbw8eCO5NTp3HgMmN6bFBxK5AnjDRT1qkOjOGRlYiSo6uap-DND9cPNsxT17E48jF-L-9fWr6hMnu0Y2KC_DebrKSU8XABJGbePzSiXm35s0mAckREIiGP93wnLRcxZQLqQtxx2UEQrG2xHU0ZtZs9vQWUMFb6SebCPtgULxvhObw8rMhMTeN8-DC0f5vkDv7lCU4n43ABg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=rbNRxGI8BfjVgRmnKpvrA3YbsUdnoBZxegMOq51sjpX0DVaF_OxTQ-9gG7MlsvCq_LFt6x3qrhKcpcJvI3YMnzaBRwitbmM3tkaVBm3HEoXKfFdfoo6E7jsn1NFVtseAGIQ6VnMsE6XFO8DeR0hOWNKDR3-F1bysxlLejScsFsz_5XWjYe62xq6cqg7QtQsCHjvVUm22W9WqBqrf2f8se-lpXvNryPRDetQwAfpReRCbQKj6jLKnnOwva0EeVa2LiKnU89mRWuQh4mSpKjTe7fpW1RWaxen0Zqjsa5CEnko4b5OCtnWTv_Enl1oJecoSrRTrjaHBiV7n3x-jACMapQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=rbNRxGI8BfjVgRmnKpvrA3YbsUdnoBZxegMOq51sjpX0DVaF_OxTQ-9gG7MlsvCq_LFt6x3qrhKcpcJvI3YMnzaBRwitbmM3tkaVBm3HEoXKfFdfoo6E7jsn1NFVtseAGIQ6VnMsE6XFO8DeR0hOWNKDR3-F1bysxlLejScsFsz_5XWjYe62xq6cqg7QtQsCHjvVUm22W9WqBqrf2f8se-lpXvNryPRDetQwAfpReRCbQKj6jLKnnOwva0EeVa2LiKnU89mRWuQh4mSpKjTe7fpW1RWaxen0Zqjsa5CEnko4b5OCtnWTv_Enl1oJecoSrRTrjaHBiV7n3x-jACMapQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هگست وزیر جنگ آمریکا : همونطور که ترامپ گفت امشب احتمالا اونها رو عمیق‌تر و محکم‌تر می‌زنیم.
ترامپ : محاصره دریایی رو هم احتمالا دوباره علیه ج‌ا برقرار کنیم.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5936" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=Fny2ztPn1aWlNQkCBnotaBARZ4XWDZjNJnLPpgH8PkO3MkMv7l6zI8keCAApwL47u7KpK69I_RxfemDEIb9bxq2FOSwUaTgecW5Q9Fo4GWIiFLjMiLZYFkoln7iIm_mGrz8E0Wy0CZD5MSzs6CbwvwIO5TYmu32zFbxX8_Bgs_gFMJP5WrMFbEFRbfrNdYfPzCH37T50ofn8ndSo_xtdPxde1xaw5rKi9liwNbP6vlp-a4N81t0M0gsZQbx5xLM8NRAlbiYxu0XuB3Q3_W4SmTsp2aSxjzFtOZvjXquahYfEemDLErOGbGNPGNXbF9d6WSo0BUvxJaifIz9YAWe79w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=Fny2ztPn1aWlNQkCBnotaBARZ4XWDZjNJnLPpgH8PkO3MkMv7l6zI8keCAApwL47u7KpK69I_RxfemDEIb9bxq2FOSwUaTgecW5Q9Fo4GWIiFLjMiLZYFkoln7iIm_mGrz8E0Wy0CZD5MSzs6CbwvwIO5TYmu32zFbxX8_Bgs_gFMJP5WrMFbEFRbfrNdYfPzCH37T50ofn8ndSo_xtdPxde1xaw5rKi9liwNbP6vlp-a4N81t0M0gsZQbx5xLM8NRAlbiYxu0XuB3Q3_W4SmTsp2aSxjzFtOZvjXquahYfEemDLErOGbGNPGNXbF9d6WSo0BUvxJaifIz9YAWe79w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونها تحت یک توافق هرگز به سلاح هسته‌ای نخواهد رسید، اما شاید بدون دستیابی به یک توافق هم به این هدف برسیم، اصلا شاید راحت‌تر هم باشه، چون اونها دروغگو و‌ شیادن.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=bW-FxYuB14_Rjc7XWRi6Bh_JUQTkjBcHmhOGEVBibQpgPujNSk33cDxEAbOj4nIv5m8CP4ToRK5qvTcby7MTHAM41oSULc83tuqG9t2igMDsnCyOHLwjaxOhhZRXx7YsvEd4NMQVJX1Dbfy4gQvQOcEOF3pEZzbVwRnadTnaELQ4ZgZxp5LGBmQX_-yYl-6qlU67xXZZPT1Tl_MAalNvo1dDEmyCoszDQZucNgzsLMzkp4ATAks5ph-o6TzbpGSblb4HnSn_CmmWvbbMvqUNG8YqdqAZkngiYhwaXqjSpQwbdyze0kBv_XGuRgwceeoduckWlQXa_m43gVNUtAY-BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=bW-FxYuB14_Rjc7XWRi6Bh_JUQTkjBcHmhOGEVBibQpgPujNSk33cDxEAbOj4nIv5m8CP4ToRK5qvTcby7MTHAM41oSULc83tuqG9t2igMDsnCyOHLwjaxOhhZRXx7YsvEd4NMQVJX1Dbfy4gQvQOcEOF3pEZzbVwRnadTnaELQ4ZgZxp5LGBmQX_-yYl-6qlU67xXZZPT1Tl_MAalNvo1dDEmyCoszDQZucNgzsLMzkp4ATAks5ph-o6TzbpGSblb4HnSn_CmmWvbbMvqUNG8YqdqAZkngiYhwaXqjSpQwbdyze0kBv_XGuRgwceeoduckWlQXa_m43gVNUtAY-BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ساختمون همون جایی است که خامنه‌ای حامیانش رو جمع می‌کرد براشون می گفت :« کشتن بد است، اما فتنه بدتر است.» (پس معترضین رو راحت بکشید)
و اونها هم براش «حیدر حیدر کنان» می‌خوندن : لب تر کند امروز سحر قدس شریفیم!
ولی داستان یه جور دیگه شد</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5934" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=pCE10VEu2EjPfKxm_vOCgRJLeRyOzpImApbQzQs1Cu87vHTOntemk2VE62iQdUqRTFdYa7beNc1RolEG7rdbLIWYgYHkEeBJgEOkuouf1Iu6MLYK6e8UXh6Qn6-k5xW5icmZi2iiuGCjCRRHRC-MAtdI3xnzh36dN-RFOL2siVPmO6c-FZLvgN569bWw2KmDP2ItEd6oy928wcv0vKiS3NjS6zj0axR415QigA9jXTMCejsJ5M1YREflnhRLweqXD3Zc0WP6flbxaE6IQavm2ueuOzCATJq617Qp3ZK5d5BfpFSKAHFhY-JjmrCrqMwDIQlya11JPKcjkJ9tZNek0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=pCE10VEu2EjPfKxm_vOCgRJLeRyOzpImApbQzQs1Cu87vHTOntemk2VE62iQdUqRTFdYa7beNc1RolEG7rdbLIWYgYHkEeBJgEOkuouf1Iu6MLYK6e8UXh6Qn6-k5xW5icmZi2iiuGCjCRRHRC-MAtdI3xnzh36dN-RFOL2siVPmO6c-FZLvgN569bWw2KmDP2ItEd6oy928wcv0vKiS3NjS6zj0axR415QigA9jXTMCejsJ5M1YREflnhRLweqXD3Zc0WP6flbxaE6IQavm2ueuOzCATJq617Qp3ZK5d5BfpFSKAHFhY-JjmrCrqMwDIQlya11JPKcjkJ9tZNek0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : احتمالا امشب هم اونها رو به سختی بزنیم. فقط دارم یه هشدار کوچک بهشون میدم.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5933" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5931">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">هزاران نفر که اومده بودن توی خیابون‌ها رو کشتن!
صدها نفر رو اعدام کردن، هزاران نفر رو زندانی کردن. اومدن با وقاحت میگن ما اومدیم توی خیابون! طعنه هم میزنن!
شماها با وعده امنیت کامل رفتید
با پذیرایی و امکانات. حتی خیابون رو تخریب کردن برای تجمع‌تون، کولر گذاشتن براتون!
خود گدا گشنه صفت‌تون رو با جوانان شجاع ایرانی که جون شون رو گذاشتن دستشون
یکی می‌کنید؟؟ طعنه هم میزنید!
شما هنوز نه این یکی رو خاک کردید!!
نه اون یکی رو می‌دونید زنده است یا مرده!!
هست یا نیست! توی چند سوراخ قایم شده!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5931" target="_blank">📅 16:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5930">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsQ5e0vkOPCm03RFfcQw_Twi1U4TRl0MyInu4-dbRiY56O8fLDjxOfHrATdGjdQC30GOb1dqCM4XyE3TFdhOaxuxhGjoevZL-778pgfvKlWAOVhdckjmpMNGEodtgcOlnRd4FoTvbeKvXODZQ8HlbEg-j4VCFiKeTy6Gl6X48Dz4eInY2ayB-kmgun-vPgj7iO3qH2Cwn-bc_Ga3gloexF50NxoDtPFXxH7Yn-Vfshe5rw6DIAVlS-D5Du2HCum2ScvS3Qc8ZZIpQxqVUcWgfmsV_7hVXBc3YsCYlc7X0bPva5zL4sHGnmnWxnXmQLNQBc5PvST5HEA5bvtnppdjaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه کیهان زیر نظر خامنه‌ای در دو مطلب خواستار کشتن ترامپ شد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5930" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5929">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : «آتش بس با جمهوری اسلامی پایان یافت. مقام‌های جمهوری اسلامی شرور، بیمار و فریبکار هستند.
آنها مشتی آشغال هستند.
به آنها یک هفته فرصت دادیم برای مراسم خاکسپاری، ولی در عوض دیروز به ۳ کشتی  حمله کردند.
آمریکا زیاد از حد وقت خود را با اینها تلف کرده است. اینها شبیه به یک غده سرطانی هستند. غده سرطانی را باید سریعا جراحی کرد و دور انداخت. »</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5929" target="_blank">📅 15:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5928">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnwpMndy8VrsGjrll55YdGAtS6QF5E0CKrrFYApI4DTKrUEtAGBJZLY0uAadseFQlk8lAzPZoBkfHcfPm9XQIUvZYxOjK1wcLWh3opui8WDEyn95F7X9ugZj2ISOOVcQWS0m85yvYjrsMD8_fMrpMa5nTWWYzcEaOAsW-vYIJkwtSsDdXhfd7heLSTQgYfvfCnJFdjqj6eCa2_4meVx-cTRnUTkJgWiEdPOFBt09tcWhziVxvOAPAkSj0cQHNPglZIt0a6igQfM5dEfHxSsncscXjHdfO7XH1Jzc_BVWkQQoXfotETOVhgXjdTvVbvGUB3XxtEBRCnx_xeYAoX2IMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوش دولت چپگراش رو چنان بکش
که درس عبرتی بشه برای بقیه اروپا!
برو جلو! دعای خیر ما پشت سرته!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5928" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5927">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5927" target="_blank">📅 11:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
دبیرکل ناتو : حملات آمریکا به جمهوری اسلامی کاملا ضروری بود.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYHHaKyLSqqpYzj2X-TDOpO1K-sBVZUZmBFNRY2UU5uGvFCcr4hVExOGZ9KBoXwSVNeEAIx98tmIevs-HBugm_D0H0Fq4cWCDuocjScAN9pTc63mBQ21_cn9lXztZoW4X31w3Z_n4pay820eP37Kkco0WSBgO_x-ZrZcVNXInFGtQVppAQpx5dYnCWEXmcgr6voF9wxN0Si_2Xx4AGeaWx7NV19g_xNb7R5Hbw1kXV1WZG3-vK72aZXpcAiX6HnbfvC_3wDzRblo4-gcKHTfBw1ERnEEY12-JadKyPmJk7ff2HVSYepTxNb7SnKC4ftVOfph-KuaFcVVhq-N0dcPHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
سپاه : به ۸۵ هدف مرتبط با آمریکا حمله کردیم.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5923" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=oM74bPnpzeNFg0kRcMd_2fq9WkOnzUo5b8ISZ9QRjbgcLQHAphbVpyyVhLxZKWCwvUx6TLihi1UgYSABQxfu04GL0LMQsH1NH2d3173zrAB_sZqyEGbqcxnfwkPuruwy8s6gcGwPZUakboku9bBONMuuU2nEdEhH7tcv1UnCWndNLwC-XCUNA0rLTOnjVBOyK5iRn78Mp2VuuP8_VX7dJv1ae52bsyeF8bJ5gjJTc8Y34ui1o16WMu-Gs-OC-h8v3xSYi_s63TTO7usqWcGkmaAL0X-omT8YmOrwRMucVfDOf-RRvZaPsI7Oj0Pj5qPTwGBoqn4gZdVXe6VGhgCpQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=oM74bPnpzeNFg0kRcMd_2fq9WkOnzUo5b8ISZ9QRjbgcLQHAphbVpyyVhLxZKWCwvUx6TLihi1UgYSABQxfu04GL0LMQsH1NH2d3173zrAB_sZqyEGbqcxnfwkPuruwy8s6gcGwPZUakboku9bBONMuuU2nEdEhH7tcv1UnCWndNLwC-XCUNA0rLTOnjVBOyK5iRn78Mp2VuuP8_VX7dJv1ae52bsyeF8bJ5gjJTc8Y34ui1o16WMu-Gs-OC-h8v3xSYi_s63TTO7usqWcGkmaAL0X-omT8YmOrwRMucVfDOf-RRvZaPsI7Oj0Pj5qPTwGBoqn4gZdVXe6VGhgCpQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس - امش</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbTMZy96x-70jT7_sA4Qeg67BvLG1xxSEXSxoRlpx8PaggrVSxfveLNGg4jh7tJampZZ0YHStWnUeNzDdDcCFChZbsJ8l5ugarA4oyfOSGJ8Y1Toz_O8XsCdJQzi8rhLgyj8uSV0YGpTq-1BekGCmnwKXyLF7yLVQej2tnfDD_zhWk7yxeoUPg2JklowI9O5gZLHbRD7z8Wi7uOluXffh6CVnTQrIE3tjD-8CblPcnQQ3OIUPolOoGb5m7LMfacZjKt4eubCUSWQPBFUXdhyxIJSXWbW9xFybk9kJ8fi_hh-M146LGlEl2xb2aA6KHN1Zzea4aGam8TyssxtWGuOlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش ها از شنیده شدن حداقل ۳ انفجار در بندر عباس
تصویری که گفته می‌شود آتش گرفتن یکی از قایق های تندرو سپاه است</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5921" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا: نیروهای ما آغاز یک رشته حملات قدرتمند علیه ایران را آغاز کرده‌اند.
‏حملات آمریکا در واکنش به حملات ایران علیه سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5920" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در حوالی قشم و سیریک!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5919" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5918">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=q6ciZi69X30XG0-wGZkSJWTn1BeiG5AMBMvPJcCwK2TejfbevN4NV-VyJLBlJYDiRZ0Z8GtL10o3TTZbjr-rQTCD0Anv7sYtIKxJdiThgR93Mv4AXMFf8mVAcDE7oBbSYt83mp6txEG0HZvMbvKUpapvUPXlqoGbO2RPv3ZSgN0fsRYPx-WX0J2nBuJQ4fVaUFoMaPYQuuyLjuI4gqxh4mxJWdlOMzAYAQw5wjCxJOqCK7oTifAVd-PrizwtgWp93TaTEF6ixTZgQ3uQu8kRVdRPdymrHJV5DS0cNMefjzXvdWH1NG1xP1iNXATjEmwb2UcZnLQkh40Y2OwuOh2eGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=q6ciZi69X30XG0-wGZkSJWTn1BeiG5AMBMvPJcCwK2TejfbevN4NV-VyJLBlJYDiRZ0Z8GtL10o3TTZbjr-rQTCD0Anv7sYtIKxJdiThgR93Mv4AXMFf8mVAcDE7oBbSYt83mp6txEG0HZvMbvKUpapvUPXlqoGbO2RPv3ZSgN0fsRYPx-WX0J2nBuJQ4fVaUFoMaPYQuuyLjuI4gqxh4mxJWdlOMzAYAQw5wjCxJOqCK7oTifAVd-PrizwtgWp93TaTEF6ixTZgQ3uQu8kRVdRPdymrHJV5DS0cNMefjzXvdWH1NG1xP1iNXATjEmwb2UcZnLQkh40Y2OwuOh2eGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی این ویدئو دقت کردید یه نفر رو به کامیون جنازه خامنه‌ای وصل کردن؟ :)</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5918" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0EppF_05HaBYz5NTiSmrqMjY4Xo69SJ_n4w2I2ul2Jssx6LK8dnTwi8GJz5Qn9vNpsEjvLZshvy6L7pCriiMZWeqvmcWsi3L6W3Mk5gA-Y8LzM4ZjQ5am9nMlH68q9I4NO9TKQLBqnl4mpL-7kFwPq8Fl_bY10VYDZqAmV04QvsYb7QzXWBpS09I3vH_lTPt7gPVUB5u42VWiitKSdfgWcEnvwVnbHDSQwKOowalImOoko7tBwPGVOjt3vWhzzS2KeVm9wzzpdf5kQg4aJ7AzqJ8xxk7JGuiLrkdOvKrPbkjBtHY0oXQfNbQfNRjxejOImv-jLGyREdkmDVpIv7Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)  دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5917" target="_blank">📅 00:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5916">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQhqeYFZDLgWOKk-H6k6uvEC46vXgePlxzGrZmpxyv1bUjp3Sj33Pqqn_DkvEv6rvZuGnLiD8_FXxqwGvKC3TCB8wPl_9NCyHBIS3E5y--7E75bJLeRandkQuL5-UzO0hgHASZRS6varajmYqa1vYi1GJJr_vX2PH4em_PUj-J3LboGyV4HxOkD6VFD6JkXJ5pGlSJopTL5_9m5gNCpAixI_4wCp96PcbF98niLof1PVNtafKZi4N6hbJ-gdk4_zrkZ6NSHyQlsbBKxA2RyNVgIKyr2muylXWLx25cFYSebwe09u6qCC2Y8rvvUitxpds-LJ3o8euUKWxv8g27WmXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما موشک میزنیم بر اساس حسن همجواریه
شما بیانیه بدید اعتراض کنید
مغایر با حسن همجواریه!
کشورهای همسایه هم تازه دارن می‌فهمن
مردم ایران از دست اینها چی میکشن</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5916" target="_blank">📅 23:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5915">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=FL-IHc_srYsgz6Mkn5K1MCxLWoLeV_yZKAevJt4cQK8yo6Qpc1VnXEJuqs1kxp2Mao_pqbtHydrUvNTI5HAUdDGhwdnQaZh2brKciL2856rvi-L0RWbKzYNiKAFbC2NZUhAtiqyMyLhGMoOzmMIqPsdk-8zOsOnCTr4gg-T_s3-VocevcqSfuvP2khp2neUte4ByAY1PKBKP_GxCVcMI1qfkLc44F7W9MmxqgwxskFh4j93u6SlkUthGc5py8uJLrSNJEubfgY08IFhIJiI1X6ZvHPJceXpcihj2KCzuqZ17rtuuPRSOWWnGr9sRW4UY8uGIXdpBsvI0DApbx-YTQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=FL-IHc_srYsgz6Mkn5K1MCxLWoLeV_yZKAevJt4cQK8yo6Qpc1VnXEJuqs1kxp2Mao_pqbtHydrUvNTI5HAUdDGhwdnQaZh2brKciL2856rvi-L0RWbKzYNiKAFbC2NZUhAtiqyMyLhGMoOzmMIqPsdk-8zOsOnCTr4gg-T_s3-VocevcqSfuvP2khp2neUte4ByAY1PKBKP_GxCVcMI1qfkLc44F7W9MmxqgwxskFh4j93u6SlkUthGc5py8uJLrSNJEubfgY08IFhIJiI1X6ZvHPJceXpcihj2KCzuqZ17rtuuPRSOWWnGr9sRW4UY8uGIXdpBsvI0DApbx-YTQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه حمل جنازه خامنه‌ای</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5915" target="_blank">📅 23:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5914">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5914" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5913">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)
دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5913" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5912">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvUvPhqLPllWsdL3D-7Ag3k62GCyqe6iPT9T4J5LBdjrH_2FsVoM3TSzFXt7Z_l4-JkfEhc42kPaUaoAIPXegJOrx3VtBmIhqDg1qJ401ki73_6cynB6em6Y1TpY2mHGpLQ0qhTf9s6fXNm3j50MCJNK-vvXDPbyqylvX5UYV8HlJ6aQFvglDiqKo4Bqx5hs1b0qpsMh4FfcDO0o_BGsrFtE7zBycjejzppJNHApKJ9LORz2o81a03VnuT0EoPbYcHWv8aD9BT0pb4uDbNCrVz6OK5ORTJe_Qwiab_jh3fBfPfF_ejdjqy39paYb81dr7AkDxXmpUmKV944bSVFU7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط امروز به سه تا کشتی حمله کردن
بهشون که واکنش نشون میدن میشه نقض!
جای ترامپ بودم یه توییت میزدم خطاب
به نخست وزیر عراق،
هلی‌کوپتر از وسط راه برگرده قم!
بیاد دستشون!
برای آمریکا خرجش یک «توییت» زدنه!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5912" target="_blank">📅 22:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5911">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIfvCC63hztb30QsocexxYv5mIJcAtUy2DOShE78k31zWBcQ7ixu3NAI5VE0HvWADPV1UIVKe6R_-BsXXi7j_TJ0J8Fb_UsiUzTknTeOYQ68V20ImffparsSuqUHYgcci355VOeEcn4JW9mzn1m0QXTY9c8BYhQtfyAw4Cn6zsLc9pHQ6hSozmfdycnQpzMXQIUoHNL6JDu2fGmcHr-1w-RxeeUbI6MAqS33Eq749ZBuFQk-tTyv0RAJ_CwNa2fsRlY_alyBx-QtFMAnmAgZE1Pmrah7P8KZOtbdrOS0u81PfPuPyg4I3L-pHyA-vR63AXUo6muPYsqqYUGyF_V7Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمریکا مجوز فروش نفت ایران را لغو کرد!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5911" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5910">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rK_sJWDuf6vh6I_1vpbU8ZNeh2_Hu4t30uDUl1J9fifBtyOYJwH7acpjN22kTwdG3wC8NXswZx1afiJMcRNufgD8GWsdTdkC2c99Hx-ZO5iMuFpRDxbsZYtNsJ5IlA0R4lFnjwB_cMzATiJ1cju6zuIflU7-Kb6ho9qwqTN0MZSnECDgAYhGItE7U2m39vV0OUI07DY6uTEfQy-Gr5SgWN5BL8FwDOKxFprnsrMySwRaL1swvh3zhdTDG-pNlbEF7gBOgCwHWqaTv3O4eV7wibOeLnkd6TSDl82ww1fFkzCvZnDB3F2Y4YNz0HDlh13FQpD-QJLhyaN67ayzrm-ujQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد حمید  رسایی :)</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5910" target="_blank">📅 22:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5909">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند.
‏یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
‏ این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد»</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5909" target="_blank">📅 22:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5907">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vG7WcReM5OT6aiq8YSmZJGXZqo1l0EP7KwMLx0s72Q7dgCTKqhreqzlPUNuLGv45j11JigIwnDHew0uvw5LLK6nWDcfzbSFGIEthWbVzeISBlPhVv4rZqLmtDwhalGhu6aX1SB_rUKESrhZhKU2J3LMZqr9AsTl8LupW0NcdI3iuHAtVa4swPesRz4Fo26FspZzE9aei11GIigqbeHeK-fpY6YWD_Vt2rzMYEknQ-KuyOXra2atC-micHBUQLiEUHwLQZOY36FjK99-_aEt3zTA59Jt1yX2DZc3cVWD_lgfuoumq6O8Onx6_PnT8PGR0QB5HvrqGW8-nM5IXBeKNfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lrq1CI0nLQqNOX0sfMjmMKyWNuy5_otfvcr35iYQ_amE7VjsHkvDxVmrH3raNtd574dYxT0Y1XBw_WvS9pe2BjRC9_WmM6Am476umPXMRkspd4rHquqj2TuQVEY4LdfEz-YdYs-OpMnQySRrHhHhIUjb04_VhSIYjtNTK4omhzMIiRefgqGo0ss3TrjXVUhQ6qylXXFeIiHkzgtSU55bAM9WZ61pIH4L88QpVs-fmdSNMNsla_426Pp4BG8SsmzfROa0GLOYsxUWojGgbAUNo9u3cGameXJVgmSgMV9_oj5PMubuq3dtTDn7yCeBl31ycpNgLrKgZK4R6XCn_Arp9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تا پارسال می‌نوشتن گنجایش مصلی ۶۵ هزار نمازگزاره، امسال نوشتن ۶ میلیون نفر  برای تشیع جنازه رفتن :)
به ریال می‌نویسید؟
خمینی گفته بود که برای حفظ اسلام
حتی دروغ گفتن حتی شرب خمر «واجبه» :)</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5907" target="_blank">📅 19:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5906">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u__cq5_XH1MP3rIHWCBuUz-JtZIMNZ5s1rDmyIM44S9ZyeWKv3C04eIEx6DGFaLl51OnQnTmdhokQ5hPzSPKvrTcRxJAAuWV0n2WAwJ44UamPFuQd945f-634WanJtOoKJ_CbVEbSDAD4EFKQH_FHSX12ApNqMtd-7Y2V5Hyeo1D9cH_p-xNJs88PpfR0jZsh-J3TWuZIsda-7spd4lMPAH_3F3d4HmUJ5UKIYx7JnqdGmasSldhKmt4M2afGruc_rvg3zYyN2-OMeK6NIgnr8B34kyRAF0ESyoYcWXkXEWW-wA-0Ljg27ao66UGlfH5-LZai0MIw9vJ6G1HIzSQBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم پاپ فرانچسکو
رهبر مسیحیان، روسای ۶۴ کشور
شرکت کردند.
برای ولی امر مسلمین جهان
رهبران ۴ کشورِ اونهم داغون!
خامنه‌ای سخنرانی کرده بود و میگفت
سرود «سلام فرمانده» در سراسر دنیا میخونن
و گفته بود :« اینها عواملی است که می‌تواند
به قدرت کشور کمک کند»
که منظورش نفوذ جمهوری اسلامی بود…..
دیدیم نفوذ و جایگاه رو!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5906" target="_blank">📅 18:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5905">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=UvDkJJqmekFmIGyqbbM24L5sArFMmY_ywc2OOYajRXO8AlMMokUC8eqVhIFKC183O60lwAdl9qNHVwQA4Yce52pj_5T9g6A04tbfFKTkQBcMJdP1F9Q1q7o3qyEiYCXaS9MmYlKu44jYMP7pG5W2xA4U9yVacF76FMP2_As5NJxac8nOF_5m_D2IsIbG3A3QQ3memCITFPJgZPYeWWZ9Ok6OMOxjZHsYXw-3AW2g0tqxXlD1nCX6vy970lOrLIWmhnDK8DMO_9F61anPX9s8-dUQYDcGZtEOmJftCob0lrsreX1MZa3v9JcqVkozJwnmwxRNPT8e6FrP4E10s29_QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=UvDkJJqmekFmIGyqbbM24L5sArFMmY_ywc2OOYajRXO8AlMMokUC8eqVhIFKC183O60lwAdl9qNHVwQA4Yce52pj_5T9g6A04tbfFKTkQBcMJdP1F9Q1q7o3qyEiYCXaS9MmYlKu44jYMP7pG5W2xA4U9yVacF76FMP2_As5NJxac8nOF_5m_D2IsIbG3A3QQ3memCITFPJgZPYeWWZ9Ok6OMOxjZHsYXw-3AW2g0tqxXlD1nCX6vy970lOrLIWmhnDK8DMO_9F61anPX9s8-dUQYDcGZtEOmJftCob0lrsreX1MZa3v9JcqVkozJwnmwxRNPT8e6FrP4E10s29_QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک داستان ۴۷ ساله در ۲۴ ثانیه</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5905" target="_blank">📅 18:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5904">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
یک کشتی دیگر هم در تنگه هرمز مورد هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5904" target="_blank">📅 17:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5903">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CktiwpFtjll2lct3azMaa9NI1s77FUWttrwcL_bVlroTS1smfCKmtqJqJax4AVagyd1Vnef8ODDnh-39E1_mmddyzpUutLTlcHE_WPu9SS-42J7-Yw0dYfuxe5srJAsUbIfrnQP2dWvxaepUW9tzJSIKjy4ftN9WZHioG9T8F8s-0rQRJLo3W781eAinoe-k3B14wWasQicMH4QbFc4vz5i_fBR4he-sYdZkQZm0Vyme59zkDTUPLy0q2ckyUv1Lgd36ODvM18sU-bBkAdDTW0w8kLPtIInHaefIVwlb6qnl29YIFhdzpH5EQJ2Q9KRx-OVHVtpyf_zfjMD_-zgArA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر:
«هدف قرار گرفتن کشتی قطری «الرقیات» هنگام عبور در نزدیکی تنگه هرمز، حمله‌ای غیرقابل‌قبول به امنیت و ایمنی کشتیرانی بین‌المللی، امنیت تأمین انرژی جهان، و نقضی جدی و آشکار از قوانین بین‌المللی است؛ به‌ویژه قواعدی که آزادی کشتیرانی و عبور امن از آبراه‌های بین‌المللی را تضمین می‌کنند.
ما از جمهوری اسلامی ایران می‌خواهیم فوراً تمام اقداماتی را که امنیت منطقه را تضعیف می‌کند یا ایمنی کشتیرانی بین‌المللی را به خطر می‌اندازد، متوقف کند و از به خطر انداختن تأمین انرژی جهان و منابع کشورهای منطقه در راستای منافع تنگ‌نظرانه خودداری کند.
ما جمهوری اسلامی ایران را از نظر حقوقی، به‌طور کامل، مسئول این حمله و هرگونه خسارت و پیامد ناشی از آن می‌دانیم.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5903" target="_blank">📅 17:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5902">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=mo10mhQqhTvTZbl8QjMUH2wxnXOx6PW4vpFoywg8n55grhtOLls7gIF753HjkpvE8g89GwrvUGvdbEJwwnNbPhzmrTRk9gx4tI7grEio8yVRr10gmaOx9jvzZ92aijGZphCixOvIyEu2H5_iQH1MR-AC8RM16qStNy4kNAILOINLwVCR7aXNHoIe8JtvGqwAnvDbtUgZCDUP4YVCLiEfZPKuV-07CLIOfFDSVfTLRJL4Wkrkw1DpV7VRDZHkJzaJ0-vcf7V4WmVTmrDTeLGlLMqbPD3wT5AyqM4XaFqwwO4ZlWiYQxc0y64yn8-UEsuT3k39K1UYZxV6AfcMTKBhjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=mo10mhQqhTvTZbl8QjMUH2wxnXOx6PW4vpFoywg8n55grhtOLls7gIF753HjkpvE8g89GwrvUGvdbEJwwnNbPhzmrTRk9gx4tI7grEio8yVRr10gmaOx9jvzZ92aijGZphCixOvIyEu2H5_iQH1MR-AC8RM16qStNy4kNAILOINLwVCR7aXNHoIe8JtvGqwAnvDbtUgZCDUP4YVCLiEfZPKuV-07CLIOfFDSVfTLRJL4Wkrkw1DpV7VRDZHkJzaJ0-vcf7V4WmVTmrDTeLGlLMqbPD3wT5AyqM4XaFqwwO4ZlWiYQxc0y64yn8-UEsuT3k39K1UYZxV6AfcMTKBhjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5902" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5901">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=QTgU3vrAdExcUhgPtpTMbPq4s6p3DEIYQM1hH_xI6gwK-LQowyVodlLVZHGqIWH41Avu43wiww6lPxJ0CLaLwbkdDr1i3D0LE06hBP1nx1MzWv_SbE1H_836_7FHyM_7BttvPo6Ir6_3ZMY3fg6a2Xp00C6vq3E9hxMqnQ--_fUQ-SxaGKMqd1w8EhoQXktzKuIow9WsOeM9mJNsk1S1QpaufQK1HmPyy3yW6z_kLUOek72NTJKzOwenFnoDtfCYsQWyRR2D6H5FETzI8VKTIrqFXHormwXufStkOGOQeF_WseKuVXWPUaMfGnL4u6pMEWs58SyZjcWfC4MjLwboeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=QTgU3vrAdExcUhgPtpTMbPq4s6p3DEIYQM1hH_xI6gwK-LQowyVodlLVZHGqIWH41Avu43wiww6lPxJ0CLaLwbkdDr1i3D0LE06hBP1nx1MzWv_SbE1H_836_7FHyM_7BttvPo6Ir6_3ZMY3fg6a2Xp00C6vq3E9hxMqnQ--_fUQ-SxaGKMqd1w8EhoQXktzKuIow9WsOeM9mJNsk1S1QpaufQK1HmPyy3yW6z_kLUOek72NTJKzOwenFnoDtfCYsQWyRR2D6H5FETzI8VKTIrqFXHormwXufStkOGOQeF_WseKuVXWPUaMfGnL4u6pMEWs58SyZjcWfC4MjLwboeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سالاد الویه و گریه آخوند</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5901" target="_blank">📅 15:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5900">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5900" target="_blank">📅 15:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5899">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5aRqKxefb8Cp6YqQ3TbS-10UiEFTjP1SSrSETjZASk5Aoh-xb9ZmwP7g5eHHmCjUSn-cCQ5GYc34E3tv8yXF1vqvjUzrs2DygyQIS7QR_HQKxMxuOI1QLPp9SkF85h-RiXD5E0-BIZOEnd1pjiPCDcbBI4w9AHSJTPKtMzBSoyMjAEIXYDfwD4R4iQ5sdbIbpJUSPyN6-6yQkqcf4qX6JaJilFes7G_dQZvM0pW9PeVlOE59kKEJOIzE4VmRJrtia7jVKHjOmQQoKdddtMFSC48UzqQgUNiSih7gvoxrdJokkvtFAjt8UmvQLRFoOpefjypnKTXhSsdjpsHmSnFdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان شرکت کردند، از جمله رهبران ۶ کشور اسلامی! (برای خامنه‌ای، رهبران ۳ کشور اسلامی!)
برای مراسم رابین حسنی مبارک رییس جمهور مصر ، ملک حسین پادشاه اردن، زید شاکر نخست وزیر اردن، فیلالی نخست وزیر مراکش یاسر عرفات رهبر فلسطینی‌ها، حیدر علی‌اف از آذربایجان ‏و چیلر نخست وزیر ترکیه در این مراسم شرکت کردند.
🔴
برای مراسم یاسر عرفات هم ۱۷ تن از رهبران جهان شرکت کردند. از جمله رهبران کشورهای اندونزی، مصر، ترکیه، عربستان، پاکستان، الجزایر، سوریه، لبنان، یمن، آفریقای جنوبی، اردن و…
فرانسه، آلمان، بریتانیا، اسپانیا، هلند، نروژ، دانمارک، فنلاند، سوئیس، کانادا و چند کشور دیگر اغلب وزیر خارجه فرستادند.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5899" target="_blank">📅 15:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5898">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=XHJvQyMyDko5g5CQQgEFLK5NQvRA0eGoxr_oSEPETF1375UAzkkO8iMexBeyhxgOa4FBeoBaPKXXY0zxZlzVpPI1emMbKSy8p8Fnsrj-wMOe0gnA6eVRt5i3RvQ9lzvV__lZhFHxtcuW8Pfmo6EYvAZVuAOsHFd86oGcT3ujfDf5MGkAx83w_8igFDqsL3FkU5mBfO-WgdENvOUt85xnZ4he-ZkskWvQMnYCMWQpoOY8-S4EZ11fTV33Ox2isnUKLrrrlWQr2Fm5XkGzq1vXGwhAqwsp1qd3m4lkuq82gv27rtL3lRHfGkjARaWuP_WmNzMuTBPOZxJ4kEKaj22XAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=XHJvQyMyDko5g5CQQgEFLK5NQvRA0eGoxr_oSEPETF1375UAzkkO8iMexBeyhxgOa4FBeoBaPKXXY0zxZlzVpPI1emMbKSy8p8Fnsrj-wMOe0gnA6eVRt5i3RvQ9lzvV__lZhFHxtcuW8Pfmo6EYvAZVuAOsHFd86oGcT3ujfDf5MGkAx83w_8igFDqsL3FkU5mBfO-WgdENvOUt85xnZ4he-ZkskWvQMnYCMWQpoOY8-S4EZ11fTV33Ox2isnUKLrrrlWQr2Fm5XkGzq1vXGwhAqwsp1qd3m4lkuq82gv27rtL3lRHfGkjARaWuP_WmNzMuTBPOZxJ4kEKaj22XAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیل و انبوه جمعیت
از دوربین خبرگزاری بسیج  :)</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5898" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
