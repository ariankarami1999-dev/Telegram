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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 10:29:07</div>
<hr>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/snnzMcz3inFmx6TanG6GRCd7O9p-D-ITlYAnw1PO4pKhyTt9TcHO75KRhdMUBBV3y-9h84lyQeZQ_bQEydzSFmi8B2jDyz3vaIPy-EY8vtx7mkIG6gTtgjxrlkeW6I7OX7JK56UMSD2r88bFsy_EguWzvxYwAVvYh2o0XJDKWlksI-VTqaurAUMFvbWRXI1PVjAWQ4eLDOW75Y9WmMcYtM9y6WD78p5DmtVEiZsMzRn6MJA6HQJ-Kh5qmTwvEErLU96wwVkia6sSK-_hYlFGbOfQwtghUEQFPOoiLt6NjA9vgHY7UBswCXnUmifw0ulJoeXN_rXsy1AXxJSnAI8Gow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f2581pEOawJV4mFu1HSOkfAfRRmx88xCqz9n_xBfcTZIT6BqUIwdK-sU5_zsA1F5lqeIc05FAY1PqR5RdLZN7XeSfaMtSI8rhEpb8eY_iMU9FkEv8Evfws39KOLkyAO926Lqy-jhTG3dssgp1yfEkNPMJl9-WDUG9aVRi59IDnausAglgx1DN9b5xf2Q1-6qZnZSyY5IfUDSES9TKJX-5UUDfQ83HG5dtv-6bcyiEAlnYS2HEFXPmkOYGFYJkyhenBTO-MiHCsav0ZwU1hiwiGeQm9URhdH4NoKYQpMQbUw7V8nzk_YgMxJ1qdtWaj9PeoDrm5c9d8jgdHg0DiCoHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farahmand_alipour/6000" target="_blank">📅 09:35 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farahmand_alipour/5998" target="_blank">📅 09:18 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farahmand_alipour/5997" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5994" target="_blank">📅 00:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5993">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pabgq-du6dDgLFpsDNMCzU5VShy3qM5jEn06jg-3MbuepfgVd7fuTEIi5hUwXjKM9_1MFa5fBZStC8APTW7m77xLob2kSXU8Ujvz3kkXZ8wezDDG8-9Nac7Yl9HMsIwNWQXGHrOp2eqArf6QEgYoGhn5g3Hq7-BEOD8ByLc07dpAPt9wjfjBbgOeitYWYzgsA8Jt3k7ReChTcOhdkWJ8dPPj3GMKxv1hBnxqneZZpVut6EoUe-2XW6GwQZVKYaZ7k0QrrQ8JPEFDQKK60jDlgwpydHoIWvC8IPpo4dygreiKJ62t1ujiRuQNPWxzhCN35khuuhgq55S_JP8GpOB1uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5993" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5992">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">فرماندار کنارک از وقوع دو انفجار در منطقه نظامی نیروی دریایی این شهرستان خبر داد و گفت:
این منطقه شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">صدا و سیما : هیچ انفجاری در شهرهای بندرعباس، قشم، سیریک یا جاسک شنیده نشده است.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5990">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
گزارش‌هایی از یک ترور هدفمند در اهواز.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5990" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIpLlTI0pELFXOsNeFkZw5ajMZbyea7hENTtUPJQpK7rD4cqzItgPA8iR8ItnUvuhVuvAgH7jxbhBcTZN3eXjPTJLgcstdANXgCfoK0ZpniCxfJdxOFNUlftaaBcpkoeLYy7mRYnH_MJOK-ARIWvQal1GomGdPcpcYKC9lPU0pxunj7KWeykYuFBBU1BmH6IAVsrCY5q6cTfyyY3_FIUatv7Wb6AuO3qvIFlbiGK0iGNIkR7zRzwO-K0blK5YxkxqovFuOEP5N0CndrQERqAugZUHuKoZeNG_XDCu8jw7bLKO1y7l-8w8g-luImbBe6tcCK9wWGRKdbg0zxs22WlvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه‌زنی ‌برخی رسانه‌ها:
حملات امشب احتمالا کار
کویت و یا بحرین است و احتمالا
حملاتی موشکی به ایران صورت گرفته.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5988" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس و العربیه به نقل از منابع خود می گویند امریکا امشب حمله ای را به خاک ایران انجام نداده است .
ممکن است حملات توسط کشور ثالثی انجام شده باشد یا صدای شلیک موشک های ضد کشتی ایرانی به سمت اهدافی در دریا باشد .
یک مقام آمریکایی هم همین موضوع را به سی‌ان‌ان گفته.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fG7p1iTApU8POpzzXFlUrTr0X1yZwmkgDED3tUJWhV_i-_jMW-SOCPM2P4F9Jd3nhZDkHvJYrketdp_1svGQIJwvTVbTFVJLD1ujWu7JQmPS3rMgdtnnibnwqkTDAFFK7gnbng8e8uJ_NTwuz4ueQDuEGIY9RhhyADsjC-YtXZG9amek3d-JHSVD_3P8C3V32NKyZVf4AlUgojymZMyhR36NEsEzauGIAkVSGqsOkI-6041CllZdWgQFu9x0G_22z0Cugsub_NrsZPMurOeqFzkCpAoZV2HaND_sUpfWbSbwcS0NY02_HFbOsvtdsmpLxM-Uve7oMgCRtr_0Qy9_2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhv62mcsOOLL0ete9XfnCRObegtjel1jQtta3AHlgSz3re9QZ9fYTmus_WoPanpD78E8DxIrxCQq6GmkmthwXUWO4TxQTkUuBLqbzj3_UpOxakhMPpQf-2ArkU_TazLzwCoe4hGm2catc2RnwXdRCwCdkK2QU0xEdUI3n_A6KUasaTWOjM9AocRVEg6MGGhoeYxlq-VpoLhvXqQQtOdAHXRuLwLnrs5Aecx-UMn9Pw1U0zMcWdPP37txErsNC5EyFGvIEvVwLmQ4CET7HTGpYlFavr0YdJb1jynC_S8MVKTqtqSbjuEjBx8e2iDA1unVueQCpRVXZMkhLOuCVqOaUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=RyxmPD98pdd-V0E_FwW8_08eZBF5h8r_MRTqzB6VdbDEezYIRqVWnwSmxnJ6ZcLPiWBiBTw0mTbgcvfYtEVoZJB9eUPDm-MAFEpKL0qHu7zbjRbBE2BD16CmDvjHKhg8zLxUgYYfH-W9MTD_ss1xC5pFqUL_Viac6pWvetmVimijLkM0AeMqaW-OgmjjTRydTdN1GtHAEY_Jh_-ucHRbjS_j4fEiYm_6P-U-fwYSxNCIjZ8qNlKPOIcDvlx8XWMOk1IHBcatH7vv-PNviQ2NDOL-ofiECehXZQq1BqIarvN5fIEq_xKpiZSknfKvYkmCE_FTF6Wo6cv_Qgmtb1bCzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=RyxmPD98pdd-V0E_FwW8_08eZBF5h8r_MRTqzB6VdbDEezYIRqVWnwSmxnJ6ZcLPiWBiBTw0mTbgcvfYtEVoZJB9eUPDm-MAFEpKL0qHu7zbjRbBE2BD16CmDvjHKhg8zLxUgYYfH-W9MTD_ss1xC5pFqUL_Viac6pWvetmVimijLkM0AeMqaW-OgmjjTRydTdN1GtHAEY_Jh_-ucHRbjS_j4fEiYm_6P-U-fwYSxNCIjZ8qNlKPOIcDvlx8XWMOk1IHBcatH7vv-PNviQ2NDOL-ofiECehXZQq1BqIarvN5fIEq_xKpiZSknfKvYkmCE_FTF6Wo6cv_Qgmtb1bCzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=XRti1S1qSjYwISwhbvpNONb83M9ZFB8AUxfwQAqyJl-YFxIrB0Xo-9nDIdKkOTF6JtpTRgcwgdB6tMexerQK_GLWXC50Itz0WcAIdaxdZ0vx6uDZHqb2V2HpVXvJEpphnazUBkbxRbwC31LnJprmK-YP_g0MaJlOGlU0pELuwQZNBnmzicvSjdestqU83zQlvvhp8XxquNlMBFLHIDvQMACJP8hGIW2Ga6Eyjj_VUM3h0UTX3VkxYhQw9tt30FU6Ad8Z06-82sLv6cedpHMuH0uSYjRkDwXwAi0lzUDtnFpxquufzHcAf-UWerJ_AT5yXg-h1-SgX8wirSH7VacvDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=XRti1S1qSjYwISwhbvpNONb83M9ZFB8AUxfwQAqyJl-YFxIrB0Xo-9nDIdKkOTF6JtpTRgcwgdB6tMexerQK_GLWXC50Itz0WcAIdaxdZ0vx6uDZHqb2V2HpVXvJEpphnazUBkbxRbwC31LnJprmK-YP_g0MaJlOGlU0pELuwQZNBnmzicvSjdestqU83zQlvvhp8XxquNlMBFLHIDvQMACJP8hGIW2Ga6Eyjj_VUM3h0UTX3VkxYhQw9tt30FU6Ad8Z06-82sLv6cedpHMuH0uSYjRkDwXwAi0lzUDtnFpxquufzHcAf-UWerJ_AT5yXg-h1-SgX8wirSH7VacvDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش
برای بازی امشب مقابل فرانسه
امشب چه فرانسه ببره، چه مراکش
مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=Ja1CxAR8F-I8oMVGJma9AIRwT0h4EaPDKvZ-PsDGnIxc59zQ-cc2vtnUuJ3RCM7CcAfcbSCe74o64NJPMZestxYMD_ShrGYsxGWMYn79-S9SBK1EFCG1Y6jesHvFvLBsCiJxqgrLnDNdULV1pviTMRQHTPpcYvqPghz5EUIj9FgJGjixfwX56Kg_BS8FnST0hiylJ7Na5yw8vUx8uR62g0Reaaa-udhUMW61Saf5YhzCjaJpDHTvsSm-8AAzLlX2CN2dhAzgN0qvw0_kFPGcqt3mCUBYLYtW6p5F71bYxXr3KxufLHFrmow5ezUWj3vHIooi-_3OP6cMxdD3YKAswx1XfBJ6BvxtkjWr_c_MWgL4Ojma9Z85HnPHqUMaHUTO3LcOt1bzlgA_oSQOIesNdzXUnbg4s9_nOYFEJKCNuDLCarZDFzgXUAK3ShfCVY9SYbnIVttRXL2iGvA_ihouiZa2ow8OSTzjjNF2IHlkp79MqCVBOY5LshrmXgGEpKi6OPj5UCKtOFEZjOqLTg5bVppYD7FU-bqCyoUfgVZHmwXOO5SMz-SSucN5OWezcHBD0qJnxyIkhFw_C0KXivcdQH-F8lMBMJuBp1JejDCSI7G6P5tY2PhTI8DwHTQ0NcU9p2tAUhGf8jjZMJT927u37nb36nhqFjXH0_2p0NAWmJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=Ja1CxAR8F-I8oMVGJma9AIRwT0h4EaPDKvZ-PsDGnIxc59zQ-cc2vtnUuJ3RCM7CcAfcbSCe74o64NJPMZestxYMD_ShrGYsxGWMYn79-S9SBK1EFCG1Y6jesHvFvLBsCiJxqgrLnDNdULV1pviTMRQHTPpcYvqPghz5EUIj9FgJGjixfwX56Kg_BS8FnST0hiylJ7Na5yw8vUx8uR62g0Reaaa-udhUMW61Saf5YhzCjaJpDHTvsSm-8AAzLlX2CN2dhAzgN0qvw0_kFPGcqt3mCUBYLYtW6p5F71bYxXr3KxufLHFrmow5ezUWj3vHIooi-_3OP6cMxdD3YKAswx1XfBJ6BvxtkjWr_c_MWgL4Ojma9Z85HnPHqUMaHUTO3LcOt1bzlgA_oSQOIesNdzXUnbg4s9_nOYFEJKCNuDLCarZDFzgXUAK3ShfCVY9SYbnIVttRXL2iGvA_ihouiZa2ow8OSTzjjNF2IHlkp79MqCVBOY5LshrmXgGEpKi6OPj5UCKtOFEZjOqLTg5bVppYD7FU-bqCyoUfgVZHmwXOO5SMz-SSucN5OWezcHBD0qJnxyIkhFw_C0KXivcdQH-F8lMBMJuBp1JejDCSI7G6P5tY2PhTI8DwHTQ0NcU9p2tAUhGf8jjZMJT927u37nb36nhqFjXH0_2p0NAWmJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSIAZkCu7D_u3JFD7n67dYERcvEaGHgRduSbKOdMnXrJY8pLG6uuUBM8hjZYBHTnBZVOEgpe2xjDW7_hvB6eM8OOXYVJHE3p6_a6IVg-_YjQJME9gie4pr8hsh03yNAwMg3oQ6jnxHbIMdybXMdLIcA_zdqlIxE9Jb0zTFJYOovSHJZXdUSaN-PbnMPv7EDAU4HjvDl0wm57IOIM_GFNXf9CUMdgAAa_aZRCfIG9UgleEhF3CXBi6OjRoSRq-doq3wT4K38MI9GR1PilueCJ7gjnXKhQxRPS2VrobaBUnmdwzRg96D31dC2rqPmmG86IKn2AuvTsayQ0g4hRk0DJSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIYcEfq63Uo9c9Z1_LHweI8A1cAmmGwqIDDWczDTnPNJbSz51Nctmvls9aqrz5MGbz5tGFMOiLRu61BQU3zzNuCYqP4JMebCouQQHBcz4SIb-zTFLsMFNFd6M_hl5QXIuO-Zzb4WLzp_299-Luin-JbkdhYCKZ9IkWtn8PcfcxI9RcMWKcRBoHHodFNl95LG2MMPD0j_hrlAq-AXBipvdfFodt3VKzl6NsL-V0Mp3Clh666xYlKmMXK15r2Sqitfn1sdsN0deT7XHt4DAyJQyUePFpAeQiSkEbHvJvrrG9Gic71yxIUBOL_p0lcvEI7EmQdXZbwewp3yKocZ_4zh0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب با اینکه حملات متوجه شهرهای جنوبی بود، به یک پل راه‌آهن در شمال کشور حمله شد.
در ماه‌های اخیر، جمهوری اسلامی حساب ویژه‌ای روی این مسیر ارتباطی باز کرده بود، هم برای ارتباط با روسیه و هم برای ارتباط با چین.
حجم مبادلات هم ۶ برابر شده بود به ویژه پس
از اعمال محاصره دریایی توسط آمریکا.
فکر نکنم تعمیر این پل ، خیلی زمان ببره.
بیشتر یک اختلال چند روزه خواهد بود.
هدف آمریکا هم بیشتر ارسال یک پیام بود
که جنوب رو محاصره می‌کنیم و می‌تونیم مسیرهای دیگه رو هم از کار بندازیم،
اگه قرار باشه شما مسیر تنگه هرمز رو ناامن کنید.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5974" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5973">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYQnJ8R6ARv3ZE702m8HhCeUnBx48l5_7zyiSzVLV0OmK_u2zE6mPgLL6ifQmEiXwECuMiWpWJFIQWsGClFGOstxrS27KRb39ysrikdsM7HzarF-92kJCPG2B99Cy-h80n-XuBlNMGg3hsC_N0zpUypug8tBEnsITXGvDJw7jPW1A53ccanj01f3e1E-gCAdxaLruqVZbraPXcN3zKaWGFF8BYaare1lFw4ZD_7QNiSlUbYmiD7T49aCxfUvWCivj8lVeQtpPj-AT9TJyW5Yj8wRvwCL0g8o1zhGCv1JES5FBZLpusrsProspeoNwgaTatugbYrbZ3aQokXnQdyi0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=t_obvP5Jaj2ffOhoIhCmthUroJ9HK74VmBHAcX6KstNYo46TpnD5NGaYcJXl7nj9KbIJDDb75NGIiMRMwu92iuFSQVG3Exkgtlyl4nZq-1xbmjU7wmyvwIGRZ5AyWkkUCm9rwcxWdKp5PwU-xwynBXEjqD2_VMORmp63o6-UMnczT7gfWpzri4Ww-uCfr7fF_gw6-luELmztyEknX6j8BNVMfjHk2F0h54Q7Sh5x2XKm1_EX3-EeGzSOjMVzcGBda9QrTbcImw7OlQqB_9I-CfjfQfIUYOa2FCZeweFJhBLz9K4bQFC1eQ8mXa3XeoNXGHB6N0zuLd6s-H-nI2Hw0jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=t_obvP5Jaj2ffOhoIhCmthUroJ9HK74VmBHAcX6KstNYo46TpnD5NGaYcJXl7nj9KbIJDDb75NGIiMRMwu92iuFSQVG3Exkgtlyl4nZq-1xbmjU7wmyvwIGRZ5AyWkkUCm9rwcxWdKp5PwU-xwynBXEjqD2_VMORmp63o6-UMnczT7gfWpzri4Ww-uCfr7fF_gw6-luELmztyEknX6j8BNVMfjHk2F0h54Q7Sh5x2XKm1_EX3-EeGzSOjMVzcGBda9QrTbcImw7OlQqB_9I-CfjfQfIUYOa2FCZeweFJhBLz9K4bQFC1eQ8mXa3XeoNXGHB6N0zuLd6s-H-nI2Hw0jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=TJ6l2QglbggCdAc3ekdsECcg_IdRIY2sk3lXutZ5bM_pTa2xr3Hga0Vvc-3fsCVYFVZUhYr-W29H2TTPH_m_h_Eq4hV9cqxCl7FY_0xN_JqiUTN4wDZPcrUIVnHTSmpVj68i_uhvwtJsW5CTd2fWTAu7DYNdhibUy36mtVcrICZSuyb1UKrPWL1Wk3151erBlKvAf_DKvN5RAhkhm6Zssig7heYnodA5zBBcajzl_eWfQiVJ0I5_wnnsaJlscDd_3odSKvHASxaaFGHG_wsV1xAty65wT9TMH10OzYVWjEAU7TmuMAhHadCtVWNT6BOba4xqLEtzzvODffGqB8f-Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=TJ6l2QglbggCdAc3ekdsECcg_IdRIY2sk3lXutZ5bM_pTa2xr3Hga0Vvc-3fsCVYFVZUhYr-W29H2TTPH_m_h_Eq4hV9cqxCl7FY_0xN_JqiUTN4wDZPcrUIVnHTSmpVj68i_uhvwtJsW5CTd2fWTAu7DYNdhibUy36mtVcrICZSuyb1UKrPWL1Wk3151erBlKvAf_DKvN5RAhkhm6Zssig7heYnodA5zBBcajzl_eWfQiVJ0I5_wnnsaJlscDd_3odSKvHASxaaFGHG_wsV1xAty65wT9TMH10OzYVWjEAU7TmuMAhHadCtVWNT6BOba4xqLEtzzvODffGqB8f-Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت خامنه‌ای، پهپاد وار به پنکه کوبیده شد
و موجب آسیب زدن به اموال حرم شد.
یه تشییع جنازه برگزار کردن، هر ساعتش سوژه‌ای داشت.  گویی فیلم‌نامه‌اش
رو رضا عطاران نوشته.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5968">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=eqhS_Nchtj5d-qVl9D8yMUJyTY7otfbtWZI97EvBK43Mi84k3Fq9PeRzEDb94kToDzw1syc0lp-1zn213AqbZfc3MwKWMOI_EncL6ZwtZ0qsTXM7uNz6yoeEMxVdc1wbaetGYSTe892OxZW5pDVHkGdwWfZmBKtpYUZhSglMIauCRiJEiqmOsHD9jwY03I3IlMvTjakISTT1KkK8RgFYiyg2X7UJC-cjTeri4-b-5LNq5XJUEea_ePoNoNoIkbkKLYLiPmxJBt3U6unaZ1oKImaq75zIhASULCdieax57d0MtDdqr70eBixTaZLr0HjYVmDXqfhNrACOW8-gq1tIyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=eqhS_Nchtj5d-qVl9D8yMUJyTY7otfbtWZI97EvBK43Mi84k3Fq9PeRzEDb94kToDzw1syc0lp-1zn213AqbZfc3MwKWMOI_EncL6ZwtZ0qsTXM7uNz6yoeEMxVdc1wbaetGYSTe892OxZW5pDVHkGdwWfZmBKtpYUZhSglMIauCRiJEiqmOsHD9jwY03I3IlMvTjakISTT1KkK8RgFYiyg2X7UJC-cjTeri4-b-5LNq5XJUEea_ePoNoNoIkbkKLYLiPmxJBt3U6unaZ1oKImaq75zIhASULCdieax57d0MtDdqr70eBixTaZLr0HjYVmDXqfhNrACOW8-gq1tIyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=lU9BI7HifyIr7srBWgfVG-I9degQRS8PRsqinvhNlhqpd6t2LX_1BtUO-WoocwvCYkMuWl7ROyPahsY3sGF521mRE0wZxVZWo6TKc9CdyyYGBdoUioWXcMHkvDZfBGI1IisomeRBO4uk-pKSpkV7vnSugay_Zzl_KNBzgguzIffB409HUpyidZ6mjUr5FoThQb_JBvt7Va1DqBrxMWmoOP3T8eOWmYBQYVia0SNbzwHnjWyVKJKhq46LMF2L9LJk9WeaTNh154Uy7oDepAM1A9Z_U1nRkymEn0efGRBIaXaH1vS5SQGZ8Eve7ac5n5uzFSBloA-_8bYiNZPbbNOskQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=lU9BI7HifyIr7srBWgfVG-I9degQRS8PRsqinvhNlhqpd6t2LX_1BtUO-WoocwvCYkMuWl7ROyPahsY3sGF521mRE0wZxVZWo6TKc9CdyyYGBdoUioWXcMHkvDZfBGI1IisomeRBO4uk-pKSpkV7vnSugay_Zzl_KNBzgguzIffB409HUpyidZ6mjUr5FoThQb_JBvt7Va1DqBrxMWmoOP3T8eOWmYBQYVia0SNbzwHnjWyVKJKhq46LMF2L9LJk9WeaTNh154Uy7oDepAM1A9Z_U1nRkymEn0efGRBIaXaH1vS5SQGZ8Eve7ac5n5uzFSBloA-_8bYiNZPbbNOskQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJyiEyb535oLMVyDu-dV1bHcsQZU2pR3QY0lJjrSaPVGbibKAzQ_s_rNP2Q2LY5YzT46XJ5BbRAhtcqvd5oBhILGQGP66mV_J5mY59WrtZI6CWy6I6rf7f-EHAbU6B_7FNqOwjWL2XBl4of4iNdGv-Nff4ZdouBlTgQ7BKv-O4SbCqQi30_WlwOXdZFCnJ4tS1OkyyXWqawMLbnH36ckmj7SpbKEZRR_K6DbBJqOE-jP7wtCki9whnAGnLPqVZd2Cde1YwEZnY58wopU1UoBMTLDmlx7K8hbhhJeYZV2x85peEol-0lmUX9fxu_3w192PXcFkA5P50az63OSbFfSRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=umHKIm1Zb1tFRS6k17AZOr3PnkzjvDIo6NasfdlOgGnI_ZKRhFtwxasnVq3zwiBFLe0hYbYrC90WWk-QYvTeMO_77Ae7dw7xG5LpILb_UQXiOoJdIxy7S8VIC50x2LLVJNT6km5VW5PHNP-nmyWuRV5T61UjEGo8hdZF9UdZXqzt7vE8-fWTFKEi4I1oAwWCWvqPyy2K6HuJAuwjPmXt2J8YDJ-LDmpvlFSLa3F3NFbUwDpf7QWosKU9PzRBKt33W5C7MERGzeC7QxvP3du8_jOPXQQyyAxj0VPL5T8O3qk830BJSoZizcw6LXWzxOxxulx-TAI_afkXQJxE0SvkB2NfGOuYPZG4OZQB3RXh5g07LRWEjjW31TixR0_BxyXGmdTso_IzQnaZXUng5rLqSxV75elrp9d2lRwaWgXbvvQbU0rHwOH3AvW2AvqqCyIvhnY0VCduLjr-2CwOXdPfXLOGP1K-E3x3YJnlm9hDcweIleR9FzJ1zSz0ObC-uQYa1EChzyGtdSnExoUA__CI02PjZ1AD41y11eu_L9DopPgnQwgNfPqMIM5Q0dq9D4Q1ixwLrcdaw3B8Hrhd-t3su98fTfqZRyaUCVAS5DUyy7mBUnJtRODrYce5Ur2kFubQQELsbQ70txvzZeUqiHKWC4XMOa-Tdfem-mU0Lf5Iz4Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=umHKIm1Zb1tFRS6k17AZOr3PnkzjvDIo6NasfdlOgGnI_ZKRhFtwxasnVq3zwiBFLe0hYbYrC90WWk-QYvTeMO_77Ae7dw7xG5LpILb_UQXiOoJdIxy7S8VIC50x2LLVJNT6km5VW5PHNP-nmyWuRV5T61UjEGo8hdZF9UdZXqzt7vE8-fWTFKEi4I1oAwWCWvqPyy2K6HuJAuwjPmXt2J8YDJ-LDmpvlFSLa3F3NFbUwDpf7QWosKU9PzRBKt33W5C7MERGzeC7QxvP3du8_jOPXQQyyAxj0VPL5T8O3qk830BJSoZizcw6LXWzxOxxulx-TAI_afkXQJxE0SvkB2NfGOuYPZG4OZQB3RXh5g07LRWEjjW31TixR0_BxyXGmdTso_IzQnaZXUng5rLqSxV75elrp9d2lRwaWgXbvvQbU0rHwOH3AvW2AvqqCyIvhnY0VCduLjr-2CwOXdPfXLOGP1K-E3x3YJnlm9hDcweIleR9FzJ1zSz0ObC-uQYa1EChzyGtdSnExoUA__CI02PjZ1AD41y11eu_L9DopPgnQwgNfPqMIM5Q0dq9D4Q1ixwLrcdaw3B8Hrhd-t3su98fTfqZRyaUCVAS5DUyy7mBUnJtRODrYce5Ur2kFubQQELsbQ70txvzZeUqiHKWC4XMOa-Tdfem-mU0Lf5Iz4Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=F9LrLDyTFEsCVzxXpixB--zfyXE47ZglfllaClCpYSOAo32c6x_SEjpgaA_kuSm7Ly9tuKsmrse-WCCOSNfErfs9Um5ha0llgvS7ZLIxIzay5Gerxkqu_6q7yO5LU6MclS0ZdBpelByvLONmymQh-aqLZD8pdtVi6Xy9XGsPwXnZL7yTuIpWy5YWlXxF_VgiFo7PKDqc2wUoI0gRFcyM0aFT163uYMaV9gb9DoJSLyag0ik4pYIjPhVVBFnbVkgaJIouoFMxfTZ35ukdB4qZkaNxXzD5hxKDHLoGkp8gofMGqVtaFZvuoTGp-IZnWtoyZqM3xdZvLAAPW_S_ygaG3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=F9LrLDyTFEsCVzxXpixB--zfyXE47ZglfllaClCpYSOAo32c6x_SEjpgaA_kuSm7Ly9tuKsmrse-WCCOSNfErfs9Um5ha0llgvS7ZLIxIzay5Gerxkqu_6q7yO5LU6MclS0ZdBpelByvLONmymQh-aqLZD8pdtVi6Xy9XGsPwXnZL7yTuIpWy5YWlXxF_VgiFo7PKDqc2wUoI0gRFcyM0aFT163uYMaV9gb9DoJSLyag0ik4pYIjPhVVBFnbVkgaJIouoFMxfTZ35ukdB4qZkaNxXzD5hxKDHLoGkp8gofMGqVtaFZvuoTGp-IZnWtoyZqM3xdZvLAAPW_S_ygaG3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjdjoT90DCNhdHgXqEr1LHKybicknZZD9qcWPhiUP4ociOt4wwJmKceQlLA4Eu9P--zekG7yN3q3_21f8slRX9_Pr4X3jmL3o6jevEzzzMFO2uqWLSiE6oa_GuJX_fnW795Otai6vJugCvkh5fkwfvoYfwHgTI-vcaoSr_ruirVZ4fv9vSoX0Saf5oRs8TgUPXwsdEgAoCGDiVR4mI0aXI9Zfj2BFAoJhDd_yZndz4CMKtB_hJDGRm9B6AI7j3KwvdB_X9hKltZmXYwbbjaREOU6o-GjObzL1XVTzQ_TiB4VLMvU3-_1L7Pz-hh1JcNRw74TmuHkmvR3oYes9bdz_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=tWl4PDT59vWI45p3hz8h36y5Fhn_GGx8jufl5VdCrOLz-lPOP1H24j-4UxRre6_ymbj3BipI2xSR6wByuIopI29kBof_1Nedv8PIOZ4TrhdRZ89_FkMumXMsqEB6cAZzfQGnrasuOlVucyZtgZduy9UmcEMFjqOElR9Z-Vlo3RG_7fYyy-JY7IzXCKGmVIV6c0m2QqKpKpMVXngSIRFXN1yqtBfM9-SEP3EH1ZtiFnU7GvXXkYj8wXHG1HfbsjguIpTADQcKGMdXO3MMKuhH66-HTWXirjOA3HHmp-K3IjxtEkXPfB2bw7RHL8OkIYLe3mt-up-XTAVUsEKXw1RBrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=tWl4PDT59vWI45p3hz8h36y5Fhn_GGx8jufl5VdCrOLz-lPOP1H24j-4UxRre6_ymbj3BipI2xSR6wByuIopI29kBof_1Nedv8PIOZ4TrhdRZ89_FkMumXMsqEB6cAZzfQGnrasuOlVucyZtgZduy9UmcEMFjqOElR9Z-Vlo3RG_7fYyy-JY7IzXCKGmVIV6c0m2QqKpKpMVXngSIRFXN1yqtBfM9-SEP3EH1ZtiFnU7GvXXkYj8wXHG1HfbsjguIpTADQcKGMdXO3MMKuhH66-HTWXirjOA3HHmp-K3IjxtEkXPfB2bw7RHL8OkIYLe3mt-up-XTAVUsEKXw1RBrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله و برج اسکله بهشتی در چابهار</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5958" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=Mk_Lxpfl0K94SYxHC_lxWlEEqfyXQXJI0IY6l3xoaDpczg83IW-SdZxbO-5oVWHvjO2xUuFI-SeeqbO1MtdpZBaCGxoBtGM15ojwdA29B2Mz1coaG18EAmBTVnWNo8gEjTIyfdK0BVR9hopoueZIuSzsvMobbPuzoAIRhPc1RfujwbmjNftOLKRLMebbVNr9ixxy0FXe5jvIhj8HIcoFwbLhEdpnJseg0lT4HXGgqXFk2ozRJUVgl-RH1jZlHR35deYgXVlKSfZV5TU0cxlrB7-zT1NdEogm7IpLQW5KMHrvn2-M_q3EayaI-5wc_t4gekWLngKwM1NYkmk0vPQ_Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=Mk_Lxpfl0K94SYxHC_lxWlEEqfyXQXJI0IY6l3xoaDpczg83IW-SdZxbO-5oVWHvjO2xUuFI-SeeqbO1MtdpZBaCGxoBtGM15ojwdA29B2Mz1coaG18EAmBTVnWNo8gEjTIyfdK0BVR9hopoueZIuSzsvMobbPuzoAIRhPc1RfujwbmjNftOLKRLMebbVNr9ixxy0FXe5jvIhj8HIcoFwbLhEdpnJseg0lT4HXGgqXFk2ozRJUVgl-RH1jZlHR35deYgXVlKSfZV5TU0cxlrB7-zT1NdEogm7IpLQW5KMHrvn2-M_q3EayaI-5wc_t4gekWLngKwM1NYkmk0vPQ_Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WImQfv5R7RzuAxz8JyKyX4vjkMcTYiLhwkZS4x0suZVxmB5sciy_UIHEKjPNAV-713D0WXORPPUNbVh4ruMRq6gRLpOrYGwwYFE1agnsOZIfwLJEoH5lUHsxUlAtE83ysBEqsjxrx5QKvEHg4fcEnboD0_ftPDnuQmqmic3HT6yEyt5Qo2P_J2DpRhliLotat_PK2kM-_PDbAhduLJZihm-V08yLLSFc_su3KmWT0uDre7qzGuv8ZMrafG3S7TD3mgnDr8XRzrEXoAASS9KfCPkWc6qELig7fLYHhAlZ_YBcQg9BvEkX_422LypaIC9XW7jvywG73xh5tY_CmFE5xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت مجید موسوی، فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5955" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=Yd3XCR0sbZmXxlc1Y-w_8358fhnHxpk4fNRQwNaGl_1G3c2M_-YwSa1bHmQmCGzD2Pn5YT119due7G9LlmFq3WUdLpz64M-vPgclFrWbgEdkGD3Dnd_ID6e07AjwHRkVCNs37EcO8DwbI4d4Y9OBfD1SzyACmo5sNf_004rpdLcBz2bVWTrY_5Ybl_TJk_W9JNCScVtI0-ZuVTstSMnXy_v9O2XoUPsdVWypL0dGhNNF_S768Dvlq2b8VqRDwEaS23jYjfJdh0SCejUOk_xx5SMow-Rj2n999SHp7j8uevdp7PUSMmEh5hsi92CQPDDi4TgthsAQTZm5aPHLoujdbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=Yd3XCR0sbZmXxlc1Y-w_8358fhnHxpk4fNRQwNaGl_1G3c2M_-YwSa1bHmQmCGzD2Pn5YT119due7G9LlmFq3WUdLpz64M-vPgclFrWbgEdkGD3Dnd_ID6e07AjwHRkVCNs37EcO8DwbI4d4Y9OBfD1SzyACmo5sNf_004rpdLcBz2bVWTrY_5Ybl_TJk_W9JNCScVtI0-ZuVTstSMnXy_v9O2XoUPsdVWypL0dGhNNF_S768Dvlq2b8VqRDwEaS23jYjfJdh0SCejUOk_xx5SMow-Rj2n999SHp7j8uevdp7PUSMmEh5hsi92CQPDDi4TgthsAQTZm5aPHLoujdbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب - چابهار - حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_7dN32hwsrW3Li3J55h98Dlz_hfiRBb0DAb2-EwgBbOjhpj7SRkX7ZzeG-xUpnCqcWmfLfLoJu38G5TIoNRqIw27He3pZMQS3zQcAwtUnRG81IMylTckQEDSXtGqEzjqVjKKz9wfSZVZfM0oVG14lTbGwOzbNZo4H9O1cuaE9yHqDFwK4D49FzIhJaUwFc4EAVlVBpVB_PLsHtsqYu-0TZzIHn2OwUBVQ2-tD3ROzcvpondbIv-zrXs4uHgDOKAengGyvtBf4fpMOxVydLLyjY_bZZsGseNxIYQVIcYHFjoeBiyUIotTeDDV0aH_YYeHB_oHE9VyhR3tpii6MKyAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5950" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=RXGOGb7oW5hQWG-quSToeO-iO7af8WJfUzzzv9pxulACcFJOhs9KXl39YRaI4E-u3a5sMMoqZ42l-ZGVtBbyVd4FyTJF6cfMrWPZDJZwHVha0QVDFsAlFX05FxUrBP6LpstPBbGZVD92BHUyP99zBdXbgR7opgb5LjfSrBDOU_BZUChTCbIbNku8qa_hVvad7rWrPKnqGsrk4dadXnxHrLABLEJgUNNPzpiejSaRDutQzvcc4j12Tu7jfObs0PxfZuHdKxDasEpALdORxGo_TkaGtIISwy1NG1pR8Nt9sfh3CSQKj0rgPz7pj4Gw_umi-iRBT0p-mGbdA-NudcOTAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=RXGOGb7oW5hQWG-quSToeO-iO7af8WJfUzzzv9pxulACcFJOhs9KXl39YRaI4E-u3a5sMMoqZ42l-ZGVtBbyVd4FyTJF6cfMrWPZDJZwHVha0QVDFsAlFX05FxUrBP6LpstPBbGZVD92BHUyP99zBdXbgR7opgb5LjfSrBDOU_BZUChTCbIbNku8qa_hVvad7rWrPKnqGsrk4dadXnxHrLABLEJgUNNPzpiejSaRDutQzvcc4j12Tu7jfObs0PxfZuHdKxDasEpALdORxGo_TkaGtIISwy1NG1pR8Nt9sfh3CSQKj0rgPz7pj4Gw_umi-iRBT0p-mGbdA-NudcOTAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات امشب آمریکا به چابهار</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gysGKqPxaxqMsQhpRcN1CeNXsatuna25ZIde4V20UvZqoF1FX6VhpZePEwkZTPpUco6iAYi-GT51rx-9E870dQMugo_rCbAKwuoqpAozgys-pjox_82b8B3rJqUn-E8yZVNABTq3KE8MZown31IW3-kjkctDHL8NNyzjvOt-dQvL-a10MKlPj6IS3C7ZIRRx6jcyVN6MQpSoKr2lmeqV_LlBbDu8Qa5IwZHpCZDir4KsrvmnsNk0_WD1FDFa6ssKap4zu-4ktbPaT29_D3133fkj9FRbjyMo29cK5ePuv9Wo-nMT4_BJkiLy9mohBdZQqc4DZYdXo_rvl5X70TiKWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به اسرائیل اطلاع داده است که قرار است امشب حملات گسترده‌ای به ایران انجام دهد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5948" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5946" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=fhlf6yrSbS_reUvQ041l-gAkBVgcKGIrpVvMLMz55gA7Pr_t5DtIPC63-elnGH3tb3Oly0hMHxX_ShsYiCPukehUxbJJCY7XG-YwPa3M2Av-rXajCNIsNoVybIsXBjbclIHAJNIyfI6ZLHRubpLEW9AguvT5DL2H1ujRCJFx20fo6UwYk3yKGPtMiBZL5MxK-DPr8IPVCK4RpC2MlUXnGLKcimyjw5_GGjTEl0OJJYBYGzKJmyMWoZ2WwT83v8G-SgsXVQ_OgdPPkKVWTXUSA4VU74IDWtFdbBm5P7hKJNAeYKwpfT8P2ZA7GiU6yjP4MvloBppMYzCin8hD_4I6dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=fhlf6yrSbS_reUvQ041l-gAkBVgcKGIrpVvMLMz55gA7Pr_t5DtIPC63-elnGH3tb3Oly0hMHxX_ShsYiCPukehUxbJJCY7XG-YwPa3M2Av-rXajCNIsNoVybIsXBjbclIHAJNIyfI6ZLHRubpLEW9AguvT5DL2H1ujRCJFx20fo6UwYk3yKGPtMiBZL5MxK-DPr8IPVCK4RpC2MlUXnGLKcimyjw5_GGjTEl0OJJYBYGzKJmyMWoZ2WwT83v8G-SgsXVQ_OgdPPkKVWTXUSA4VU74IDWtFdbBm5P7hKJNAeYKwpfT8P2ZA7GiU6yjP4MvloBppMYzCin8hD_4I6dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/5944" target="_blank">📅 22:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5943">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3Zqqqz3N2YHWqTq-M7qs-ZXzDMv-Cmhe7lVNzuw6EuRO1_VP8_J-V-ycKcwEFP4KuQh0cdy4GVxNu8jUTs46Li97625Czz_CgTfrMS1ljuFzK0WWoX1B955gQeoYLCMoGKXPmwEE03dXGTUkDfkIo7TkLr6zapvAOd9OppFySgyL7Z_ai9DWd3P1RWq4pv9fizLX2NRLNheLAG2gw8fFJBXep7I2DXCmWTXHN-rKb-I2rbrxyRNd6TtnBRB8B8c81wC7ZadPgrSjBQb-XtlhgKMM-dNmMMSotF34REn5kkb_9SGpjkW9wrSz-F5Y1Y3QVf9FibIgPWTg0vssu65YDTAHtc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3Zqqqz3N2YHWqTq-M7qs-ZXzDMv-Cmhe7lVNzuw6EuRO1_VP8_J-V-ycKcwEFP4KuQh0cdy4GVxNu8jUTs46Li97625Czz_CgTfrMS1ljuFzK0WWoX1B955gQeoYLCMoGKXPmwEE03dXGTUkDfkIo7TkLr6zapvAOd9OppFySgyL7Z_ai9DWd3P1RWq4pv9fizLX2NRLNheLAG2gw8fFJBXep7I2DXCmWTXHN-rKb-I2rbrxyRNd6TtnBRB8B8c81wC7ZadPgrSjBQb-XtlhgKMM-dNmMMSotF34REn5kkb_9SGpjkW9wrSz-F5Y1Y3QVf9FibIgPWTg0vssu65YDTAHtc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برگزاری مراسم رو
انگار غزه است! با بسیج کردن اینهمه ستاد و پول و ارگان‌ها و…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5943" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTsoZKVaSwkxLup6XtXsEGq6hXFb1BlshOTAPaMAtPhQ0VIaU5pz7gWBlMrVGqQ8joD_0kn9wm8FAehH50oqTvv8peqwdIaO8OWA2dlBoKxKfwYEmUC4s0TZF000M5HOex_dsqP8q1qXjZm37YLYxirCJey5J7M6kNdfEmcnN0lD1J6w2riE-OW0qm3p0OR1eGaend0iCBxSLPrgkhAQLXakcl_I3qdaYOB1jq1XoOo-FgXCJT8wglJaYnjNwCJmkv71wpZO8mkZBafHJwWbHnEiIcsmWiee9W8nq8BYeb-bwNw-UFODfa7U9T-IXXfEA6lt1B1LSddrz8DDYscoiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: درباره جمهوری اسلامی کارهایی انجام می‌دهیم که باید ۴۷ سال پیش انجام میشد.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5942" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=h1ad3rFz9450SmjKtN5ZvA4gzZhU9LrVzLpTyttW2ug-ksWcvFMyuq0wdO50kPHkn0HNjMVE1VHRqDWKu8xWF73kCvdAsVAy787PC5I8ifQwt3Gx5a5DeG2Gsdi_puBPrM8URfiAhKShWzQtfCak2RqFFXKeh9JjM3AZTMrsCAfvvT4Mp_OD9v3BYPG2Wcbr0jSCfh2Ul8lqf4cNlJQxnEZRm8yeeJ-7yKY6l1NOSVwqVupHcbVLczVvphKo35Skrjaq0kayNeStSBr3tbJQIs4emg8kh1jhvdlFPdZg6gNCA74Gn3poJeK97IKDOK_1LDEOvonzZfbD0rmQsfSeNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=h1ad3rFz9450SmjKtN5ZvA4gzZhU9LrVzLpTyttW2ug-ksWcvFMyuq0wdO50kPHkn0HNjMVE1VHRqDWKu8xWF73kCvdAsVAy787PC5I8ifQwt3Gx5a5DeG2Gsdi_puBPrM8URfiAhKShWzQtfCak2RqFFXKeh9JjM3AZTMrsCAfvvT4Mp_OD9v3BYPG2Wcbr0jSCfh2Ul8lqf4cNlJQxnEZRm8yeeJ-7yKY6l1NOSVwqVupHcbVLczVvphKo35Skrjaq0kayNeStSBr3tbJQIs4emg8kh1jhvdlFPdZg6gNCA74Gn3poJeK97IKDOK_1LDEOvonzZfbD0rmQsfSeNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - اسکله بندر عباس
زیر حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5941" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=kEvxLrKyogaqbLaoQJ-H46pQ5do3NPLtYhHE6FH3tDxwFq00ehtzdHTkEvM5ZRsXe6FH4MpUtn4b_IxM6vZtdSfwrsHjx-TW9PIljcNWxGHv9PHca0xCDVuZSeKZoQM24jq14zfC30OS6HLwbri_z00XQSjSsLLsF-9bxc0LSM1ZUPL-4qMW7IuNC2tya1WSjlyMfux0yU6lfAfz4K1akkVjojKNq4oF5SygP14dRcx5BbENpbWiYRBbk470AwXKTpsgKZVqQOvQRHVOilz6IQDj0dTRnU74adOC44g5qbPcNSwZkfpj6ZU-T7wNqDj2LWQhbdHTSK3gPnITIxxzDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=kEvxLrKyogaqbLaoQJ-H46pQ5do3NPLtYhHE6FH3tDxwFq00ehtzdHTkEvM5ZRsXe6FH4MpUtn4b_IxM6vZtdSfwrsHjx-TW9PIljcNWxGHv9PHca0xCDVuZSeKZoQM24jq14zfC30OS6HLwbri_z00XQSjSsLLsF-9bxc0LSM1ZUPL-4qMW7IuNC2tya1WSjlyMfux0yU6lfAfz4K1akkVjojKNq4oF5SygP14dRcx5BbENpbWiYRBbk470AwXKTpsgKZVqQOvQRHVOilz6IQDj0dTRnU74adOC44g5qbPcNSwZkfpj6ZU-T7wNqDj2LWQhbdHTSK3gPnITIxxzDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مراسم برگزار کردن … ستاد برگزاری ، هزینه هنگفت، ده‌ها ارگان و ستاد زیر نظرشون.
بعد کارهاشون رو ببینید!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaX9EaNUsfpztQsZK3o1VEqkq4jhMOU5DhA9OpVJ5R72Om_NjNHisOTTo7DVL13jp46o3VYdsH3KZ-P4ySFgRfvmK8UwNy87SIoJXYr_V6b6RqFYOgT5iur1E8ko2KCciT9CpuPXzjA17_BpReTETwdVNGydgy1lGrm237WwNr2LJwjnd1nC28C3nSUZCpdtemyX9_d7-_u_cWK3zlzWPXDGHsay6thNaCwW6iUhlek6VxdP0l5YYWeauS5bd6jSOw2pzzwzjCi-inBtGgFgCFOuEiC6XsnoSubhqdTxOaap_4kdL3X7CSmPiMJyZeHifvM898DzBB6lC3s-OP7sTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کشته شدن ۸ نیروی ارتشی
در جریان حملات دیشب و صبح امروز آمریکا</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5939" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ: اومدن خواهش کردن زمان تشییع جنازه ما رو نکش. بعد وسط این مراسم حمله کردن به سه تا کشتی.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5938" target="_blank">📅 17:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=LJBM9CLXhQyBv5BLUBrkkNYmqGpvZctGV7KSEcBE0ruN6NoZkvRlx5VYobG03MSqMnWTtYNB4yCvC2dONyP4r9jq74NooAnd0VGid4XEg3HMR1aN65aoJuKGgD5Njn5q05yUHofY6bal2e54uS2dQ6fEKX5wtXf9vQ0HusJBfAPRSxwZhoZHovuMiNV4WMn9llDhnEftj9PhF06wIlBN0wOFydyP5IDIQ8vHFjOKXTqBJ6LIoNeHn7n2js7gRQNsuaO--LIFjDz1B4mz8E29i_HkBXSFlHCz2YPzoVt6RkC9ix5Qr7ZqQYWxBrs8-KbDqfE962c0FNw-COhePDf71w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=LJBM9CLXhQyBv5BLUBrkkNYmqGpvZctGV7KSEcBE0ruN6NoZkvRlx5VYobG03MSqMnWTtYNB4yCvC2dONyP4r9jq74NooAnd0VGid4XEg3HMR1aN65aoJuKGgD5Njn5q05yUHofY6bal2e54uS2dQ6fEKX5wtXf9vQ0HusJBfAPRSxwZhoZHovuMiNV4WMn9llDhnEftj9PhF06wIlBN0wOFydyP5IDIQ8vHFjOKXTqBJ6LIoNeHn7n2js7gRQNsuaO--LIFjDz1B4mz8E29i_HkBXSFlHCz2YPzoVt6RkC9ix5Qr7ZqQYWxBrs8-KbDqfE962c0FNw-COhePDf71w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=am6xNnTLNVavuKoUZtjc2gh5Gx1Qrqdq69Sma7jX52d8lAbt9p12NkAn8j1iQxvgvgPvraZQ0-gdnMayWreCLew_XW1WQMf2C_NWG1f4eSo42wMgGcJi3rQhQlpZ89SNnf78VAPmAb6h0AlmduLzeB4yTJNyRcK0OsZY6_Mqhq8H1suGICjyIXLxEVcTkKf7Bt7AQckNoOAbPFQcApoflUbEwYrnm-51ouBMK1LFhBUY_ThR6DAZa7P7V6DFMiPuf3zcAp4kToobNpTw6RltCreBNlU18AKCP-QkKugQ393M8XddkJ2Fou1NH47qM7eqGb2lUPdriiFSgLjw0m18Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=am6xNnTLNVavuKoUZtjc2gh5Gx1Qrqdq69Sma7jX52d8lAbt9p12NkAn8j1iQxvgvgPvraZQ0-gdnMayWreCLew_XW1WQMf2C_NWG1f4eSo42wMgGcJi3rQhQlpZ89SNnf78VAPmAb6h0AlmduLzeB4yTJNyRcK0OsZY6_Mqhq8H1suGICjyIXLxEVcTkKf7Bt7AQckNoOAbPFQcApoflUbEwYrnm-51ouBMK1LFhBUY_ThR6DAZa7P7V6DFMiPuf3zcAp4kToobNpTw6RltCreBNlU18AKCP-QkKugQ393M8XddkJ2Fou1NH47qM7eqGb2lUPdriiFSgLjw0m18Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=SOi3KCiSJmpqVqdvUmobZh5B3uZ5FyY891X495opQzlP9rLueFa30fs5mUIDLQ4IReaOEO8jsdWGiGdXbwM1dFwKrCiCXNF1ujSxcskruc-YgbC0T7jEgP-buTuVL1AJjBzv3yUNajuiAD6LyLbwTiTbWsCoz9GaP8mCYqHV5XM5LHSEq7RSRMHZzp4IM5GmCPhouQSHrYZgNLSvQKtsF5hDB9HZEsSePoBzsShXiAZ-wpekzb_CFaQIveH4IPXcw6uyrhHbH4pD2LWay12voODm930IAE_jGxETbYmo37kmBAMOWyhMeDcZlHcs7_t4xGpIawT8m3Nn6XrdWPljoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=SOi3KCiSJmpqVqdvUmobZh5B3uZ5FyY891X495opQzlP9rLueFa30fs5mUIDLQ4IReaOEO8jsdWGiGdXbwM1dFwKrCiCXNF1ujSxcskruc-YgbC0T7jEgP-buTuVL1AJjBzv3yUNajuiAD6LyLbwTiTbWsCoz9GaP8mCYqHV5XM5LHSEq7RSRMHZzp4IM5GmCPhouQSHrYZgNLSvQKtsF5hDB9HZEsSePoBzsShXiAZ-wpekzb_CFaQIveH4IPXcw6uyrhHbH4pD2LWay12voODm930IAE_jGxETbYmo37kmBAMOWyhMeDcZlHcs7_t4xGpIawT8m3Nn6XrdWPljoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونها تحت یک توافق هرگز به سلاح هسته‌ای نخواهد رسید، اما شاید بدون دستیابی به یک توافق هم به این هدف برسیم، اصلا شاید راحت‌تر هم باشه، چون اونها دروغگو و‌ شیادن.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=RbI2ypVcJckyL0Vj5FMNmPen5wdl_VQfH1DLdnsqcSdofQ1v98HH-kYWsFUo82uKihgPPStDacMbcKqntf08kje-G-W7MZorJEHK-aIN5mUFz16dowCYnbVH4BwJPvpdvEKi3ehGP3ngIg370FvjyYIJv8nnubBYGDjL7Fu8hvx2WkVhgJrERaxC0Tp0hhN7HXJV-dZ2YIbHVM8-2BKNZhoWeZoWXvQmsqz71LZo12b7r2w-SabbSkt0B_qBHUVSZy2NXFO65-33xy1t408NzRzy8v64iaPSOHElGMYCbtOPboh2OLCm5IsxaAPgchJGwsF54QherDZROz49Zos6kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=RbI2ypVcJckyL0Vj5FMNmPen5wdl_VQfH1DLdnsqcSdofQ1v98HH-kYWsFUo82uKihgPPStDacMbcKqntf08kje-G-W7MZorJEHK-aIN5mUFz16dowCYnbVH4BwJPvpdvEKi3ehGP3ngIg370FvjyYIJv8nnubBYGDjL7Fu8hvx2WkVhgJrERaxC0Tp0hhN7HXJV-dZ2YIbHVM8-2BKNZhoWeZoWXvQmsqz71LZo12b7r2w-SabbSkt0B_qBHUVSZy2NXFO65-33xy1t408NzRzy8v64iaPSOHElGMYCbtOPboh2OLCm5IsxaAPgchJGwsF54QherDZROz49Zos6kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=Lq72tn2mHEgJj84saCSHmLW0pu4yGbt8ExlGD7LUvmsJU_IC2Bj0cUz5f_dNHqChlle8oJikJuzR0Lo0OBY1C3F5c7J6v1WZKBa5aE6jawWp68g4gWU4LjYQnMYUoJN7AfGIhrUlMZaar4yN9jb4nJ1JCDLNFuMvsdbQRRbeNjP5xChvxoSzpyUQ93KBCGe_kfakXU-h5fLoeaUNh0KPVLM8Vaogsye3MQkJY2t-MqIYrpCr1GRx7mwiUJufCtXQtxKw5x9O4UE2IBccJtBsmFRmVWBHWPur17QrmYHewsRT5BKZo8GdBbsO8hpRatclmuLE8Pi12jSKSK_w-13Nnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=Lq72tn2mHEgJj84saCSHmLW0pu4yGbt8ExlGD7LUvmsJU_IC2Bj0cUz5f_dNHqChlle8oJikJuzR0Lo0OBY1C3F5c7J6v1WZKBa5aE6jawWp68g4gWU4LjYQnMYUoJN7AfGIhrUlMZaar4yN9jb4nJ1JCDLNFuMvsdbQRRbeNjP5xChvxoSzpyUQ93KBCGe_kfakXU-h5fLoeaUNh0KPVLM8Vaogsye3MQkJY2t-MqIYrpCr1GRx7mwiUJufCtXQtxKw5x9O4UE2IBccJtBsmFRmVWBHWPur17QrmYHewsRT5BKZo8GdBbsO8hpRatclmuLE8Pi12jSKSK_w-13Nnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GN4Fr0sfzX45iQQLiDyTA4t3vW6Q0QGc_h07p5rQa42_fkf3Unb6rc2hqLIJFe6LRRaITTqjvQWc9Gkgt5OsflVK3Q6Gy19q-o8ErUeYt3KxhRoXYxBApBwoODcLK8jf_K1kDMwcnEbr717BWDysiF2i81WMtY8ZY32qD6e32toff3Ec2Rt8wzgCyVERvSNjWa1w8Y0oBH_PlLLvDnOAbOWM_apa9DiqBY5oCNpH9kC81rPR7G_jPPhrf5kcWdcj-zNuE_kIW30OIdYJxNJd9z4P9lrtco0v6e6t9GaUiGEsa_BOIi-f8WcCLBQ4bmkaO9qdVU11837V67ttL5WywA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه کیهان زیر نظر خامنه‌ای در دو مطلب خواستار کشتن ترامپ شد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5930" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5929" target="_blank">📅 15:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5928">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEtUcAgSZjePJyfSVviPNd88KyZsNjX0suy01mFmozXjEVUIddrQaluSYFwnnB1SAzzKWUMSIS5AkBGc4QtXnQu6pHTUYxmNgTSKA1IBLOH9lSYua57czS1PvSnGMfdCOnnDYDkPXvIErnV7KkeglmMUUW8kthl-ZJTqSLGfKgj1zgHFSBbbold539gSAZ3UbASc7b_EnU9iGpDzF-kgN1j1SNFOOL36sMNuZH3wGzwDJQbMbyyTOLeP5A-Y6__6HtPCocVkXjpjcJlSHFJLru96tpFQBfRKLY1Ge5j2zbBv2ZJvsHFdMUwiiCr-fGC65UqGDTWy9RHHPIzHI3oyxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوش دولت چپگراش رو چنان بکش
که درس عبرتی بشه برای بقیه اروپا!
برو جلو! دعای خیر ما پشت سرته!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5928" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiItFn4NxuYXdI9at48U59XI6UDmdxsMzaqoKzNmfZFuR7RR8Fq-Lf-4sPqcbBRi_D7Ag-N_xuafmzaXg83pDEVU95MY8Pf7k2S7SHcJsIfrGWtjip1vStxL5ZcI1ls9WXrNUthISe-A9IyT4FCv4wsX_TDPWDIHy0Gb-Znu8Sm7NTczik-CJxftEGzPsiDPCftRNyhsZ30Mc9Ao2MCdUiNeJScrYLO__bTZU97PIPYUdqfZ0Wyp8886zv4G9k-ahB6qUsZqSSrdDTJl5CgB6YLhGC460zI7fOcubv13q9QMCxGpkcd8lyu3iJX48EsdsrNH0TjQbJA90RDctEL4HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
سپاه : به ۸۵ هدف مرتبط با آمریکا حمله کردیم.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5923" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=ChqyR930UXltGuo-YuWeXbt9AAxBvDCng5ZYQlyFBbAyg1rG5CKRZBvC0zAmDMiwJ3bIliHGaYd1jCTcG91pxrerFnZat66oo4gGdA85o2L75BQWc5OxRu2-umHLI59DK1NnPJyO8usChSbxbWHH-1nPtLoMXcR48Rx4TP5GU7uLG5iG9RS3_PComzsFY_frtsTWJZYsoqzxbFpEqWlarUXC0ioGHU7il3mxrtd7ZQ3nnLAeA7nN5Ky7LD2Uot3dsV2rRaDhL4njmiPJ8XBLlNPUJlNbuklq7auxnN2OvJ8HpDh9waf0eb6bdcSzo9-KFdF51Nmup_s0TIU5r9DbJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=ChqyR930UXltGuo-YuWeXbt9AAxBvDCng5ZYQlyFBbAyg1rG5CKRZBvC0zAmDMiwJ3bIliHGaYd1jCTcG91pxrerFnZat66oo4gGdA85o2L75BQWc5OxRu2-umHLI59DK1NnPJyO8usChSbxbWHH-1nPtLoMXcR48Rx4TP5GU7uLG5iG9RS3_PComzsFY_frtsTWJZYsoqzxbFpEqWlarUXC0ioGHU7il3mxrtd7ZQ3nnLAeA7nN5Ky7LD2Uot3dsV2rRaDhL4njmiPJ8XBLlNPUJlNbuklq7auxnN2OvJ8HpDh9waf0eb6bdcSzo9-KFdF51Nmup_s0TIU5r9DbJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس - امش</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3s3MMfkM6UlnkoGY4qGFlMVn2aSM0WkDJc-VolpncavzR_mYPQKpF--1s5TmhHiqMW94AyTd35NON1xtdXeZ3sYNZOOSdTAnIIqbDha1WGeCbT8YuytOhO9xJ4adb-imsEVeeJ8ti2vv9H20uEzCKMtFCbQQ6izPkJARNMaIIo7SPJkgPtJ5oKrkSXu7p7V19JbbmNlMrax9XLKGB-u7E29lmitvL4Dwbk-5Z0O_O4A-8dEdbz0JT_B2blyg9AJfcm5RGKnyCEZb2H31KaJoRdbCC-yV94fyFbiGmFD0KSoJ2jNv6qkoiTBlCgnbffzWhGFVz_5BIskBLx0kenvbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش ها از شنیده شدن حداقل ۳ انفجار در بندر عباس
تصویری که گفته می‌شود آتش گرفتن یکی از قایق های تندرو سپاه است</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5921" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا: نیروهای ما آغاز یک رشته حملات قدرتمند علیه ایران را آغاز کرده‌اند.
‏حملات آمریکا در واکنش به حملات ایران علیه سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5920" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=Y7-YxHI-VkRfBrgG41KUs9PtiQKYeQwCiNhs1jgCzZIf-UuakiR9F_7ONUzqrJv4Y6GY5Nad9KlM_kWsOQy9bLxsSLEWYgDEUH4JC4g2AK_Lnq9xw0xtDdfGBz2fvIWj7meELIp9VBJzbGJoXORb_VAnReZVV9yRsHfNhDr7LLzISTxg55J5w9rXYBoims8cKTJqkzqO85GkmF28nk71UOl8mmzXLTJWaLY7GzJK_v3WkWgZ8oJGd6X2aLst1lQMPmuk4T8JvRUvkLrMYSWCG41VDjMiAh-xc07hK3b6NAfClY366NUtjniHEW14Kx3-e1TgBMs4gpn8lVJBEIxqkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=Y7-YxHI-VkRfBrgG41KUs9PtiQKYeQwCiNhs1jgCzZIf-UuakiR9F_7ONUzqrJv4Y6GY5Nad9KlM_kWsOQy9bLxsSLEWYgDEUH4JC4g2AK_Lnq9xw0xtDdfGBz2fvIWj7meELIp9VBJzbGJoXORb_VAnReZVV9yRsHfNhDr7LLzISTxg55J5w9rXYBoims8cKTJqkzqO85GkmF28nk71UOl8mmzXLTJWaLY7GzJK_v3WkWgZ8oJGd6X2aLst1lQMPmuk4T8JvRUvkLrMYSWCG41VDjMiAh-xc07hK3b6NAfClY366NUtjniHEW14Kx3-e1TgBMs4gpn8lVJBEIxqkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی این ویدئو دقت کردید یه نفر رو به کامیون جنازه خامنه‌ای وصل کردن؟ :)</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5918" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CggwvjjfiDpqGJ_WaxK1YazBsqZp1lMi-1OTUDgzQ_DVxfAZUlqeeXq-fpJNufNVGJ6bJ2UFEDq0W_ChaVzPsHfNpmF_mW6iyxxiEhIERWaMochGKr3CU8DvL8uH2y9ccuId_GMGlUICKVH1Khnlg6j4kr31_vRIJxA9bNo_VkOcz7TwouuFke4P8eZCBQH4bLOBeTe99ryy_XefWXGFM6HAdTUnOM-4Aj80i_4i1yu_iouWWZPw4mHdG4KS0FQTWGxEw52aTuYLSReJLIiLo5_x6ee8blhA4ULiWVO9U7AbwbW26di3F1lKBY4CoQmxyEsaU7_eaDBT7-cykrnQxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)  دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5917" target="_blank">📅 00:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5916">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ry64lKOtEmwHQaRCzj0ysxuXUYiDECWwmNrC4hJox7ljPQ6mQi-zE8PJRnjUOPBc7wkxFj0ayWRzKLwLdEWfQCx2N1jfUqkcd0_c5lPj_omswRc6EG47UIOMffAGzok7nJJGTN2Kufjimlv9FPTHhzXuTZku0Kkf6RSlH_HV-uriabvK8woLdks_Su_etCgvmLiOCM57mx6Gm2w7L_iI1XeOGPJvKGvbqQd-vah5JT2IIqGOJXE_3F-zWmo9RiJbxil0kc_exfHas_GwJnDwke_3wOfFfehuiZfQLSPL9FSCeC9nT2p68WUG_5_pZaVwrowKr0jcmJZ8w8DlNhe7Yg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=VEztoXmtitVf26508sC8sWCSd4DbrgWqgZ5CW1TEYJC5Hxrnfx4S2iO6KFuityG73FrvGGqg4SHrRIo7qNfFwfSnCNWk3Q9qQw9P9n5rCKU8o-5_dfaqa7RfK7SpwIXzhyx1aa0hk0j-7h4jYy4vIlkWV10tqJhshdaa1qTmTMFgVOdPlou0CErk2F7NjIE8m8SqMRV44xQNWVJAXpj-23C1rzFWEkoK5lRaM1DO68FRk3rpIN9Y0WXcQpsvZfiiqjg1ZPmjNWds-HctFkqsQl0kCzkk1iUD8vOwi82yAq0siEmtmjNd665ECrfyU4khN03q9u-jG5D11WunGi58NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=VEztoXmtitVf26508sC8sWCSd4DbrgWqgZ5CW1TEYJC5Hxrnfx4S2iO6KFuityG73FrvGGqg4SHrRIo7qNfFwfSnCNWk3Q9qQw9P9n5rCKU8o-5_dfaqa7RfK7SpwIXzhyx1aa0hk0j-7h4jYy4vIlkWV10tqJhshdaa1qTmTMFgVOdPlou0CErk2F7NjIE8m8SqMRV44xQNWVJAXpj-23C1rzFWEkoK5lRaM1DO68FRk3rpIN9Y0WXcQpsvZfiiqjg1ZPmjNWds-HctFkqsQl0kCzkk1iUD8vOwi82yAq0siEmtmjNd665ECrfyU4khN03q9u-jG5D11WunGi58NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWt5ifwZJzkUD6_WW4mCdBWFz1tCDteCuJKGVaoUxz1VbQMkOUaDW41Mhcbz1VrTKvRTyYPExNttudpEGRYx-ho34w9WJ2WXxGUtZviMmASmzBbkfCn-1x7qA5xr56JGb0CYmpyydiMDnIza2TEa23M5KwrGg3-x90sEfXmQlh-481UHTrlvK616MCpYAAuoh7Prmxv2bmpfi-C7PDRFHCHLGRc7urykfYOdDPclzMMsGFTdNjVLGBvUFQl8NjfXtQEjxkALMOwQJd7b3CuerE2uBcm_V8lkoR_W35v-hqAYxyTbNgaX6pQ8ZlZDGUMkZBCZLn-pi9VSJWtAgkQETg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط امروز به سه تا کشتی حمله کردن
بهشون که واکنش نشون میدن میشه نقض!
جای ترامپ بودم یه توییت میزدم خطاب
به نخست وزیر عراق،
هلی‌کوپتر از وسط راه برگرده قم!
بیاد دستشون!
برای آمریکا خرجش یک «توییت» زدنه!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5912" target="_blank">📅 22:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5911">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxoXyMnNm7hyMXraZwMJERIvDCQXToEZ26f4ftjyBaEy2M-s3vGBgQHycS-fToH6_hWdsLEOxT3Loy0qaROhxh-g8I2r7j3lTvOOrnRZ_Nx0BzvY0WiyWDnatc_CVmsaDbViqhgYXXQb_QAmuOtoAzyZIhXVZ0hSvHnrRziIKGSflT70zDFswhau0Gkq3WFirWw9jXAUoN_EBb7CZdpwTIdkoRdlLGF5Cc1ELJN9BMmSBCXTThHdzHE15IZ7u3PA-5u83yhlBFbqYG7_QzbF5jFVmMSf7swxo5CStPGtAH2u2f-WsA5KDel0VIbDKHAk206fvfXgpAglNxZrmRfdew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمریکا مجوز فروش نفت ایران را لغو کرد!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5911" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5910">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nq_1Osmcg0ZVlUnkVyPe311a9WljaL7K2yIQvRHuCYDPU9rFa5Kjz9ep03pJKMeV41jJp7N8linJ9ExnwjDqKMPuXSirAXtCIgK87kCfMYhXu--dwr_3Ztr39rNHPJZio_jsisXhF-EAlnZGReRwSITbhji8hsOPul2lyu_QMTUOnUnN1k-a_PwLBxMhf6_tNTUdeCBL-oK8vguWgFyKixOvMtAX7T-If032fE9O95WW7nPUoBDwzW2C4EAjQ0zigU5t821NH-jSm0spx-OBx-9sRmCUwTngeXXC2QQPAI4i3oODktRTSw6B0y3rKhmH5z2BJQvLpPVcmCIw4TDB5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fGuc9AiDW359cD0G_ACfxRojzzb4tTK_g0eqEgZwBhfjuBUCjSijsN2aO2U2IERve1Z2YMFK-eXLmVwfL7SDeuTWlNiweZh6N_63IaLdNiwSlJaIgDVKaZcNIQs4tSPuvc8H0m7Ox1EZGDuoKT3AGczeEXlxWNUX3anxkICkF1z106zcowoEJHOKAxUT6zSCa89Y-7Wpcf7z0S-GRF3LM-KN2VKVtjL8eBzPAqxwQyW4iOkYRXrvNyOa3e4fgMXff7BDxOPziYVBxrVOjVXQTqOBKwqPFyR-FRplS6K9Cm7oNWJnm4ulT5F1ulP59arLaYfACcipt_-chMqSn4wdNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sm98WVPSSRbnCuBfBm16cT9zbneXSlDq4WO9_cfFfmhshQBpZg3DTrNJu7NfisCQVptkeWiqTJWbMSvGKyp0OC0GI1kqWG7h-uJCQRyN__MI8_qrpi-2D6LCmJAwkRT5RUlnU6sIrUIczBSSYQ2zMhDjSaDy0IHyxiVZZH4FrneflZdMmVtigs1hkjoZYGhSKmgPiOxOILCkK-LkDdmP9KeyZ01eKPU8Hj_HYuBqMLFxKmzxC5t1w8DyG1TOm4bTKeAnMrdrUlRMrK961ya4VzSVLtn6KWTbOu2EAa_udQTEIZBtcxIpzStIEQax-htEqrstCLEu3O5By01MybkOPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تا پارسال می‌نوشتن گنجایش مصلی ۶۵ هزار نمازگزاره، امسال نوشتن ۶ میلیون نفر  برای تشیع جنازه رفتن :)
به ریال می‌نویسید؟
خمینی گفته بود که برای حفظ اسلام
حتی دروغ گفتن حتی شرب خمر «واجبه» :)</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5907" target="_blank">📅 19:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5906">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EA5gATKFnwfEdg5LUQV2ckvAuAIRwE9cQuTwr4YZI9HF_lOIkWF2oJ6jqeBZiRIfyLCTNv8-aPrz5VO2QS0MgQxZxxi4DFhSo7WUbspkYZs8HDJDcRCs5UMTa7EGwZASFblOhWQIU6hgT5L8pouWfViw_WAp1xjcGFSLgZbx_8xK6rh9Fxvw_LGAidsz567HFEsORve8tzERcspV6p8Z8Xolr-Kp17BnNswOON2X9KN1uyNFcxQhXaeU36nfUv5VI2PHf0JO5OQn-3wGPacqf1NCLlmnHDjO8rh6I3Vo6GvaYKE5g62czPUFUvfhxg7JcLjlpkrMxG9DpY2QtUI3Aw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5906" target="_blank">📅 18:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5905">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=iRWCjXoXTEmfjTACLMAWqzIOnnzVC2jkHcorvIHaMxBBc8AmivzVHCpOa1n375EqMIGz6TJDNyZzAmfTslP74nNyWDEVuobVdra2Veau3ivocVP70SVInrHSrL7WeiGmOYAovMThdL1HR9DUxtW46IIPJ3DZJhkeRjOCk75RWYHcdgwxK5EOgbRIp_ZIzfquyPAC6JeKEXH0l9kgJZrTxVvkH0XMMld4mw6d2udMjVnUddo2aVKfmutIeUB3nWGXAGl4V7ZJQMNymG3qfEjj9cMgGCLLDekfZVLIHn4JliMSig0Ut9A8nqhCFm9mG8s7BJD2-Dv2eyGzAbqyISQ0WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=iRWCjXoXTEmfjTACLMAWqzIOnnzVC2jkHcorvIHaMxBBc8AmivzVHCpOa1n375EqMIGz6TJDNyZzAmfTslP74nNyWDEVuobVdra2Veau3ivocVP70SVInrHSrL7WeiGmOYAovMThdL1HR9DUxtW46IIPJ3DZJhkeRjOCk75RWYHcdgwxK5EOgbRIp_ZIzfquyPAC6JeKEXH0l9kgJZrTxVvkH0XMMld4mw6d2udMjVnUddo2aVKfmutIeUB3nWGXAGl4V7ZJQMNymG3qfEjj9cMgGCLLDekfZVLIHn4JliMSig0Ut9A8nqhCFm9mG8s7BJD2-Dv2eyGzAbqyISQ0WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYADIT1f9SIEF8tVPg8s2KPmQIcIq8BGDITBTB9FLMjNsfR2hi0057S0aAnQ02PqhqG0fN2MD0ZD8AHN2pnZyY0PxalUGPqK0hJGHIFaRFhCgRgbm-ytj-6R13ORkMjcm-KnDmIAFmdQ1aMD1tmITFqMLOiDfN4g845gGW5czOoSatbhGwXE1MSbgzR5_RpAAhJaMQQwKcAno0Xa-I25EFWdmSD0Jl5YSfBw2d5gC-D34Xs4l1p-r4fSiBFsw3rEUHokyawIucRasP2uqsS4gn0Tli7DLVRYWsF2rzMqBrZbnH-zNFKuiEVLqOtY8Vdr4ZMvaa0sAadLNvJDx0PLEQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=GXfgExj_8t_GS7NocnZNXjDYPxhAwzjTNC4GoSbKDmrgT3p7F7RO9jfQRRrqGKg3yyoxXmulIkSg-w8oph-HwlRAf4mPodBRtFREADlOwdDdTnJKj26P5m8ms-920Xse_sDQTf_iG_3kAz9t7Js8FYVt5JHrD_pC8MOhJBv1fPGPlrBwnXUu69PwLuDDj7PhC9ssIGny8irGOVQoEYjRhMbCkZMh5yzw_IKosA-xXVWWADg3GgWC_Q9zsqiOngKV4ZIdgj79VhF7KxiJBuqEged9489mOFdhUGxS0wdBYVVFn8L0un7XOOBNPXADibh0fS40W-uwoJlH1Epu_jtKMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=GXfgExj_8t_GS7NocnZNXjDYPxhAwzjTNC4GoSbKDmrgT3p7F7RO9jfQRRrqGKg3yyoxXmulIkSg-w8oph-HwlRAf4mPodBRtFREADlOwdDdTnJKj26P5m8ms-920Xse_sDQTf_iG_3kAz9t7Js8FYVt5JHrD_pC8MOhJBv1fPGPlrBwnXUu69PwLuDDj7PhC9ssIGny8irGOVQoEYjRhMbCkZMh5yzw_IKosA-xXVWWADg3GgWC_Q9zsqiOngKV4ZIdgj79VhF7KxiJBuqEged9489mOFdhUGxS0wdBYVVFn8L0un7XOOBNPXADibh0fS40W-uwoJlH1Epu_jtKMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5902" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5901">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=Q-CmT-LjUq3MEL7T9r3SPs7YsIhcJB7NkkSgUPvQ-Bg_Qd4je3scUGxlLKVieIIT-Ve4yqNaBb6U0qnb9QOOskbRTJ8s1yr0FVF-ZJQT5eYUXxscOpL4WzxPB6XWzemPq15saDDIwUnqArncOR16hI3Dz7hWiy5Wmax4bd8_3cGIzrYkGqcYWY6u1tTjcKdhWsRZplGlp5dciFO3sDHccYMEqqRUK7FHNT2X7hLqJr78X-yW4KvslVeiJybPySAmQy9zlhqARNxE0w00xI0wwJAxiMr0L6nQwa9XwSFoyobsTUi4wWKLzVy88vgaEq1AHtLeQR_uAvp_03QOzFUi0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=Q-CmT-LjUq3MEL7T9r3SPs7YsIhcJB7NkkSgUPvQ-Bg_Qd4je3scUGxlLKVieIIT-Ve4yqNaBb6U0qnb9QOOskbRTJ8s1yr0FVF-ZJQT5eYUXxscOpL4WzxPB6XWzemPq15saDDIwUnqArncOR16hI3Dz7hWiy5Wmax4bd8_3cGIzrYkGqcYWY6u1tTjcKdhWsRZplGlp5dciFO3sDHccYMEqqRUK7FHNT2X7hLqJr78X-yW4KvslVeiJybPySAmQy9zlhqARNxE0w00xI0wwJAxiMr0L6nQwa9XwSFoyobsTUi4wWKLzVy88vgaEq1AHtLeQR_uAvp_03QOzFUi0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrxCP4mi0o3UTC74oMvtvbwUxyAEXRnz6tSY-OvjjtXZzw7d5Dx2ePqQwAhBediTs7-yGgDOSMEw69gThb-QpuQWt9Rlsu7TDGKEfEaydfhSy7JffA11Tl4_qB3x17xVj87mHFy3f3260n0E5GZBBTDQMM_MDCFjAbENrkbBswQt4ilny4Vjigbkq6z9iSC3oh4M6NauDR0KV8vnoyPvMXUk6MVjWUCQ_uitzHGAGkfmHp_TpNauKS7M4nrMcrSCcEnoi_65TTC-pf-C8p3CwNNDM4r7xmX2Fy9ugfQEaJp4bK7u59RfqPgUfUk_8gPHnHOtr2Qv_0KAlbc6i4yz8A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=ZbsKYaxhfGtcm2m67XcI0FQHdFAtP0f2z7XC9hV1MPqhI1CA9Ipc5vRSo7HzJR7r_gAuREd_7pLSbsOik8vR-3AiFQWdIDnqTbql7DN8N0B1exSBx9GL5WmqYBt-0QK5cvTwB0zpgVg4fSmpvFRHZ3adAD2X6SFCynBWlULAzo2Fg_KH21FGMUR9VuCFUN-uvsm4y3Sg5fv1lrWwO08es9M_npU8CkWU19BcS2jJiFqN8PUVUZt_CqpXgDay-t89LOpYUqZb8C9JRuGXnp-Fx7qjQdJowQYvMsRHLNpMMpZncmHSWDLRstXSvgfi_V7a8WSURPHuCaZVVkyLcsAfkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=ZbsKYaxhfGtcm2m67XcI0FQHdFAtP0f2z7XC9hV1MPqhI1CA9Ipc5vRSo7HzJR7r_gAuREd_7pLSbsOik8vR-3AiFQWdIDnqTbql7DN8N0B1exSBx9GL5WmqYBt-0QK5cvTwB0zpgVg4fSmpvFRHZ3adAD2X6SFCynBWlULAzo2Fg_KH21FGMUR9VuCFUN-uvsm4y3Sg5fv1lrWwO08es9M_npU8CkWU19BcS2jJiFqN8PUVUZt_CqpXgDay-t89LOpYUqZb8C9JRuGXnp-Fx7qjQdJowQYvMsRHLNpMMpZncmHSWDLRstXSvgfi_V7a8WSURPHuCaZVVkyLcsAfkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیل و انبوه جمعیت
از دوربین خبرگزاری بسیج  :)</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5898" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
