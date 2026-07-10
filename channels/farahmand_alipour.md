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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 16:09:05</div>
<hr>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=mDQjlTRqRN0zJeGqSL6LOwovQK7wW_eITT_cqHnlvI_cYaSgjM8iqFfZiCpHrMO0Au1zF2154iIZrnn06Hu05hQgJzHweYyyMausGGrREkheIVMemnuQ97ARaPUlE1wTfY0Sk-RFUINlz-su7NvVOvki1w3MSPN2KD8INpPBYTckOVUsNEVh7oN2UGIXgdfD_w7_6RbAXLFs8Qhc4cKc--EOrLS5vZMje4ARQxlGsZi-IAvQdYjK6mqRqWyGFm3UNv3Bcg0mdutireIPzcj1Us-N9oaKlFd3CoONXfOioQFiiCNeYvg5LblW4ZectUeZDAAYMFI-8o58J7T8vit3Q4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=mDQjlTRqRN0zJeGqSL6LOwovQK7wW_eITT_cqHnlvI_cYaSgjM8iqFfZiCpHrMO0Au1zF2154iIZrnn06Hu05hQgJzHweYyyMausGGrREkheIVMemnuQ97ARaPUlE1wTfY0Sk-RFUINlz-su7NvVOvki1w3MSPN2KD8INpPBYTckOVUsNEVh7oN2UGIXgdfD_w7_6RbAXLFs8Qhc4cKc--EOrLS5vZMje4ARQxlGsZi-IAvQdYjK6mqRqWyGFm3UNv3Bcg0mdutireIPzcj1Us-N9oaKlFd3CoONXfOioQFiiCNeYvg5LblW4ZectUeZDAAYMFI-8o58J7T8vit3Q4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/snnzMcz3inFmx6TanG6GRCd7O9p-D-ITlYAnw1PO4pKhyTt9TcHO75KRhdMUBBV3y-9h84lyQeZQ_bQEydzSFmi8B2jDyz3vaIPy-EY8vtx7mkIG6gTtgjxrlkeW6I7OX7JK56UMSD2r88bFsy_EguWzvxYwAVvYh2o0XJDKWlksI-VTqaurAUMFvbWRXI1PVjAWQ4eLDOW75Y9WmMcYtM9y6WD78p5DmtVEiZsMzRn6MJA6HQJ-Kh5qmTwvEErLU96wwVkia6sSK-_hYlFGbOfQwtghUEQFPOoiLt6NjA9vgHY7UBswCXnUmifw0ulJoeXN_rXsy1AXxJSnAI8Gow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f2581pEOawJV4mFu1HSOkfAfRRmx88xCqz9n_xBfcTZIT6BqUIwdK-sU5_zsA1F5lqeIc05FAY1PqR5RdLZN7XeSfaMtSI8rhEpb8eY_iMU9FkEv8Evfws39KOLkyAO926Lqy-jhTG3dssgp1yfEkNPMJl9-WDUG9aVRi59IDnausAglgx1DN9b5xf2Q1-6qZnZSyY5IfUDSES9TKJX-5UUDfQ83HG5dtv-6bcyiEAlnYS2HEFXPmkOYGFYJkyhenBTO-MiHCsav0ZwU1hiwiGeQm9URhdH4NoKYQpMQbUw7V8nzk_YgMxJ1qdtWaj9PeoDrm5c9d8jgdHg0DiCoHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6000" target="_blank">📅 09:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=qKuTfaYk5kX3pTKxI8VAA2VouOmw55mnpsNSda0nEw-KC7gQpCkt9rj3cNvJbUDno_ymPfEtyf8BvL8XQMbX7nnWn3EoNavZbpCEVmWO5d8LMdf4SaHYFWimSQM6aJ3fO7MQYOxVvAuOzY2OnvkBpPW0nkwrmw_VT1qIvJ_0_UwSkB4ld_2cIo-4D0iFo6bvNf9eyVxguwZSQPnVxRwKraiFFcZOXTYk8Rlz38Bbq1F1HqrHHIigqT3KnnbhiKLjSIXOeYatf9tZKbioMhnaxCdXkbXCO5yUrxxjtfctaaO9c5T53Er3V7XMhBVu1vnrci9klhoRGNybHaNQzad_bxf_M3bkOuM-jE11yUAJ9-qmIvMnttSXlbFghOOwfKvAINnNVpeAr-0_M-fmgS_eBAJfeim2R0P5SXTE6_gH-HuRs1v7EOwDLZa9fzbOZoFuS-Q8-EUwlFPQT9VXY5lQRPjAOaeo0o4zeDMvhtbv4Pg9mgx3slPFHZ1zTJWOq82z5J7PtC6WHRaPryeOGha4pB_49SUklw18muLievnm9GQiHKHjNkS6nJ47GwLsf7My9CaYeusmscjKUMkqzsQD4aMGcsTQm6TuNnc02WQfxx_TuUpWeWFWuwbGuswUvrhWB3-vn30NuVc2qjYtzuSd9kOysyWnbM_96Uqvrp1i5eY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=qKuTfaYk5kX3pTKxI8VAA2VouOmw55mnpsNSda0nEw-KC7gQpCkt9rj3cNvJbUDno_ymPfEtyf8BvL8XQMbX7nnWn3EoNavZbpCEVmWO5d8LMdf4SaHYFWimSQM6aJ3fO7MQYOxVvAuOzY2OnvkBpPW0nkwrmw_VT1qIvJ_0_UwSkB4ld_2cIo-4D0iFo6bvNf9eyVxguwZSQPnVxRwKraiFFcZOXTYk8Rlz38Bbq1F1HqrHHIigqT3KnnbhiKLjSIXOeYatf9tZKbioMhnaxCdXkbXCO5yUrxxjtfctaaO9c5T53Er3V7XMhBVu1vnrci9klhoRGNybHaNQzad_bxf_M3bkOuM-jE11yUAJ9-qmIvMnttSXlbFghOOwfKvAINnNVpeAr-0_M-fmgS_eBAJfeim2R0P5SXTE6_gH-HuRs1v7EOwDLZa9fzbOZoFuS-Q8-EUwlFPQT9VXY5lQRPjAOaeo0o4zeDMvhtbv4Pg9mgx3slPFHZ1zTJWOq82z5J7PtC6WHRaPryeOGha4pB_49SUklw18muLievnm9GQiHKHjNkS6nJ47GwLsf7My9CaYeusmscjKUMkqzsQD4aMGcsTQm6TuNnc02WQfxx_TuUpWeWFWuwbGuswUvrhWB3-vn30NuVc2qjYtzuSd9kOysyWnbM_96Uqvrp1i5eY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مداحان اختصاصی خامنه‌ای،
که توی هواپیمای اختصاصی که تابوت خامنه‌ای بود، از عراق بردنشون مشهد.
نقش «مداح» چیه؟ مدح قدرت رو بگه
و بگه شما بزنید توی سرتون!
اگه یه عده از شما نپذیره بزنه توی سر خودش
هم حکومت میزنه توی سرش و سرکوبش میکنه.
اینه وضع جمهوری تباه اسلامی</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5998" target="_blank">📅 09:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5997" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLt7piwegmwr9yR1tpqHsuMNyxHBTpGQt9S0Hg0hPfau8WfCLj_OTwIe5NuvGIFxRpe6CjLfCSk7zH7aZScDOmpMbhae7RK7mYyzhn3mILofWCix87ipyc5DmupNSND5WfaBPMwB5qSnjjblsiBeMbmIfM2tGVVzCbGAMPnWBPdukf0dhi2EicwTNi2FDGyTQyCMs8kx3UQmDvJqgLClzYHPu94U7m-Lp174GmU7LcPmlp_CW9tIM48uc_efUW4m-tBY_foioNAdztHrTmBM5XQ3LWY7iXfrrN3ijETGAtUpZkd9nIjUfq7BCKL_cXMKBtU6tat31cfG-Xv5c3Cruw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام - فرماندهی مرکزی ایالات متحده:
‏
🚫
ادعا: رسانه‌های حکومتی ایران ادعا می‌کنند که عبور و مرور از تنگه هرمز فقط از طریق مسیرهای تعیین‌شده توسط  ایران مجاز است.
‏
✅
حقیقت: ایران تنگه هرمز را کنترل نمی‌کند. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از ۸۰۰ کشتی تجاری و ۳۸۰ میلیون بشکه نفت خام از طریق این کریدور حیاتی تجارت بین‌المللی کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5994" target="_blank">📅 00:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5993">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pabgq-du6dDgLFpsDNMCzU5VShy3qM5jEn06jg-3MbuepfgVd7fuTEIi5hUwXjKM9_1MFa5fBZStC8APTW7m77xLob2kSXU8Ujvz3kkXZ8wezDDG8-9Nac7Yl9HMsIwNWQXGHrOp2eqArf6QEgYoGhn5g3Hq7-BEOD8ByLc07dpAPt9wjfjBbgOeitYWYzgsA8Jt3k7ReChTcOhdkWJ8dPPj3GMKxv1hBnxqneZZpVut6EoUe-2XW6GwQZVKYaZ7k0QrrQ8JPEFDQKK60jDlgwpydHoIWvC8IPpo4dygreiKJ62t1ujiRuQNPWxzhCN35khuuhgq55S_JP8GpOB1uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5993" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5992">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فرماندار کنارک از وقوع دو انفجار در منطقه نظامی نیروی دریایی این شهرستان خبر داد و گفت:
این منطقه شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">صدا و سیما : هیچ انفجاری در شهرهای بندرعباس، قشم، سیریک یا جاسک شنیده نشده است.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5990">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
گزارش‌هایی از یک ترور هدفمند در اهواز.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5990" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=quRvkxBN-Xr-wOx4666BodHr-JIZ-AkArTAv7Ob0DaVZYl4P7VqxXPpRBYPQL0NqN_mKyQlnT930riRGJJ-K1dvEIWwP3w1S0iV_dUSVeJbEn_pY8MOih8LDWO4xSG1tXmwtg5eT0iM604W1c-mNjAFCgefmPgYWq4NZVEL1pdrgx_WX0FSl0VyGp9m1hH87wTxA7ICaeKc9BDjem6Ejr45t8ywgAUaPBJe3evlKGxrZidzZ02ULbzomHLGbDOkaGmxwTBflgAb6-L-4rLy0zDKjLb3iH7_CLAWeI5tiGoPFzqzTnmo4M0GlsUtw-YimFqtrW6YjHMFc6DwuiJAZ_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=quRvkxBN-Xr-wOx4666BodHr-JIZ-AkArTAv7Ob0DaVZYl4P7VqxXPpRBYPQL0NqN_mKyQlnT930riRGJJ-K1dvEIWwP3w1S0iV_dUSVeJbEn_pY8MOih8LDWO4xSG1tXmwtg5eT0iM604W1c-mNjAFCgefmPgYWq4NZVEL1pdrgx_WX0FSl0VyGp9m1hH87wTxA7ICaeKc9BDjem6Ejr45t8ywgAUaPBJe3evlKGxrZidzZ02ULbzomHLGbDOkaGmxwTBflgAb6-L-4rLy0zDKjLb3iH7_CLAWeI5tiGoPFzqzTnmo4M0GlsUtw-YimFqtrW6YjHMFc6DwuiJAZ_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIpLlTI0pELFXOsNeFkZw5ajMZbyea7hENTtUPJQpK7rD4cqzItgPA8iR8ItnUvuhVuvAgH7jxbhBcTZN3eXjPTJLgcstdANXgCfoK0ZpniCxfJdxOFNUlftaaBcpkoeLYy7mRYnH_MJOK-ARIWvQal1GomGdPcpcYKC9lPU0pxunj7KWeykYuFBBU1BmH6IAVsrCY5q6cTfyyY3_FIUatv7Wb6AuO3qvIFlbiGK0iGNIkR7zRzwO-K0blK5YxkxqovFuOEP5N0CndrQERqAugZUHuKoZeNG_XDCu8jw7bLKO1y7l-8w8g-luImbBe6tcCK9wWGRKdbg0zxs22WlvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه‌زنی ‌برخی رسانه‌ها:
حملات امشب احتمالا کار
کویت و یا بحرین است و احتمالا
حملاتی موشکی به ایران صورت گرفته.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5988" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس و العربیه به نقل از منابع خود می گویند امریکا امشب حمله ای را به خاک ایران انجام نداده است .
ممکن است حملات توسط کشور ثالثی انجام شده باشد یا صدای شلیک موشک های ضد کشتی ایرانی به سمت اهدافی در دریا باشد .
یک مقام آمریکایی هم همین موضوع را به سی‌ان‌ان گفته.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaUBk9pZ9UvVotNIiAIjzQJw_bIUpcVgKu4lGMh7vVPY6Ysa0Acoh8MntL2vozf1tCPoWFAkXFzxWxCOjWwMFvuVNb_T37K0Zz6fXbPqXftT1aFYJNnpOsYC2YDHe0ZW86VHcfm7fxxx5EbG8_QzeWojQ-A42RJVbNfR6tJSxXqG_KvZeQKRt_Q3XP5jUBYjl3uQo75U_iiqwl7PVBU-pK4vyWDfF72hA-ZTCWwzs7h2DlRGk6mvSVFXJb5BEJgy_JbGsB6f5qs5aPo5HAiu1vZN-91eQhmsGFf1Sy5IrjZ9gzA7WFUR_f5LvxLjUMNYMmagxPNJHDWfqOOO55EtVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0OSoAmonqWrDQA5ggyuZ4_JP7tQ_WBhINom9jQ60yW4SL4thaex33JJYpwuCE14JTOqQBlAU6U1W7YW5rzO34TdpGgIxvha2IC-nTZLdSqTGng3sVGL0tY5Nk9dvpa4QtPV8Gn0UJjYSCjCBIboGoOdJazBUXqjw7lZO44Cf2jsEYi_JlT-D2QK0s4q9oAIxGNb9uJIjKh6cDopGI4e7nHZ37uoKMiiCjgR0oB7fYqsexd0RjO5QEejOAoO4_MoQCl-ur6MI5wzfFtav2_RehJLzjIlAU-dc0j1hCHEs8_i5MCPoQ_BoHOfVE77AuVUrxgsUnS6ArcVF5QJRHLURw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=Ty6LZtqnGhIeX7LUC2hRE0KBgexB93E6KADfh1_KHlELa7r7-AoS7_jNTh3XIdPhDNWFizDR1EFj130mc7fm2kXNSlEwQCmOEXe3vtcJZL_e29WUNu-tRmAg-rz1sX5G3cnBhXsTL0MPOdHszgVZux2QK1YRkjez2G0ik-wY7HqaYvvURKoyDCNoS4eupoXWzVZB3h3ke4p_ZnrLkCEQbpTGY3z4MJcNZvOpWbFbOQtmOFpgU1R-yst07teJQVQxDpDpwJRb6GexG3uMj8Y8WLyifiwQbk6IKuERiAps-bllwW_fdFBIKr066smLZLfIU2AooYfZrN-x1eB9MdCWPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=Ty6LZtqnGhIeX7LUC2hRE0KBgexB93E6KADfh1_KHlELa7r7-AoS7_jNTh3XIdPhDNWFizDR1EFj130mc7fm2kXNSlEwQCmOEXe3vtcJZL_e29WUNu-tRmAg-rz1sX5G3cnBhXsTL0MPOdHszgVZux2QK1YRkjez2G0ik-wY7HqaYvvURKoyDCNoS4eupoXWzVZB3h3ke4p_ZnrLkCEQbpTGY3z4MJcNZvOpWbFbOQtmOFpgU1R-yst07teJQVQxDpDpwJRb6GexG3uMj8Y8WLyifiwQbk6IKuERiAps-bllwW_fdFBIKr066smLZLfIU2AooYfZrN-x1eB9MdCWPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=HWNGLGqGN3YYWYHoT4SXwK0fRSG2-6Nv_ICzsseJ3MP22-x9qVk0GUXEQtu7wImxAo9IVu3fg5AdKr2KOPVxskapMlsaKVccAqrqAaV7wdaA_oxALCMwW_PEbITluHF1KSQV9b9MIq3bZ9_3vHNfuJvZJ8nOtlPbhsTvskEUFNLITuBtaXkyJM9SGOQYKiLDnbpTcQ4kDIdcjLhRTEvci6X-ToABnaLLDn8VVf0srINHHzmwc_pqHBaZzKuD-op03KtiMpycanTOM0IUhc820e2Njrc_u4X27210AsjbHQwNxE4Rm87sbSIR_H_sBCSwIY6FG3qiospJYUF0uZC6tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=HWNGLGqGN3YYWYHoT4SXwK0fRSG2-6Nv_ICzsseJ3MP22-x9qVk0GUXEQtu7wImxAo9IVu3fg5AdKr2KOPVxskapMlsaKVccAqrqAaV7wdaA_oxALCMwW_PEbITluHF1KSQV9b9MIq3bZ9_3vHNfuJvZJ8nOtlPbhsTvskEUFNLITuBtaXkyJM9SGOQYKiLDnbpTcQ4kDIdcjLhRTEvci6X-ToABnaLLDn8VVf0srINHHzmwc_pqHBaZzKuD-op03KtiMpycanTOM0IUhc820e2Njrc_u4X27210AsjbHQwNxE4Rm87sbSIR_H_sBCSwIY6FG3qiospJYUF0uZC6tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش
برای بازی امشب مقابل فرانسه
امشب چه فرانسه ببره، چه مراکش
مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=F2-vEsjQeGPjsx-GrG8nx-KDiEjiKIDPn_RAwDLMA2owJSYj5AijqJcZbdFNXBQD4HJt3456e_2FrGQ6xpkX51Ny7laJo6Qu8uSrK4Vj4iL9iL83_CYJBi2ANIeGRxX11hxEpSWXgNsfO8pHPG41jEGVr2SvNzK_zIGN1AoGXzyv1xAmSSQAf0YfQZT2PskM2Un-z5Iqql0ujIqtjdRj0PLr8RlclfV9HK7zTSK4kpODWSD4kaUloTzD8foWuG7OM1vPt-iXkJRbTKJ1imxlZO3A38PbwGBJc_4zr9aIZeEX2c2Mhy-iq0ZdS4XuLNGkuColI9X_QwZWhjk_gksPmRujeci_UBDDut_RJ8HLHjPNTalq7gaDZh_EsVyngx2Zla9Qn0rBDYPAo_j7FQX_PIU8hWcVvsqm9eeq40HsFcpAKP-sKhaag6Lq_Sas20FX1lImrZxpGnHm5MUnUphWmnyd4d47v6x3aGjG6aCDEY3R7v6eCKC041K5M2uEhB-wqHRlwBltSlEe96UNQ-GsaTnyav9gShTALZ93egPrY1dJUY7AMO9Ty8jZv7ScP044gZnDPzqKTUtgtoljKg7vx98YcTnZlPc6kq2nc5zDBO_AZEj0_NwceJvddtn91NXV3h3UyJyIUgexsrZH4wPUIpJBqJa2T8WII3UM6mTg0CE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=F2-vEsjQeGPjsx-GrG8nx-KDiEjiKIDPn_RAwDLMA2owJSYj5AijqJcZbdFNXBQD4HJt3456e_2FrGQ6xpkX51Ny7laJo6Qu8uSrK4Vj4iL9iL83_CYJBi2ANIeGRxX11hxEpSWXgNsfO8pHPG41jEGVr2SvNzK_zIGN1AoGXzyv1xAmSSQAf0YfQZT2PskM2Un-z5Iqql0ujIqtjdRj0PLr8RlclfV9HK7zTSK4kpODWSD4kaUloTzD8foWuG7OM1vPt-iXkJRbTKJ1imxlZO3A38PbwGBJc_4zr9aIZeEX2c2Mhy-iq0ZdS4XuLNGkuColI9X_QwZWhjk_gksPmRujeci_UBDDut_RJ8HLHjPNTalq7gaDZh_EsVyngx2Zla9Qn0rBDYPAo_j7FQX_PIU8hWcVvsqm9eeq40HsFcpAKP-sKhaag6Lq_Sas20FX1lImrZxpGnHm5MUnUphWmnyd4d47v6x3aGjG6aCDEY3R7v6eCKC041K5M2uEhB-wqHRlwBltSlEe96UNQ-GsaTnyav9gShTALZ93egPrY1dJUY7AMO9Ty8jZv7ScP044gZnDPzqKTUtgtoljKg7vx98YcTnZlPc6kq2nc5zDBO_AZEj0_NwceJvddtn91NXV3h3UyJyIUgexsrZH4wPUIpJBqJa2T8WII3UM6mTg0CE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLfx3jCFGV5QspFuvfymKMA46Nu3yXW6gpSJbrPDC8nPVwnyBHRnGstEXULE7yMloWarZtMdJ8LhOlY29ORBh4DDea-IN6zxerbEiL5HP_u6Vnl_J_5L_WehBI7eNKyy135FU-Ejv3xW9atXNiagqZf2Z1hYbJ8nXS-WJahPWDYVkzyOV8FO-8Exf9iipdZ2kW3cTcCs31DC5gCB85-_1THAFvotjTHRA1-c8KRwBAeUa31ZGw6jxtSOppGdACXpY4ukOhPcQHT_J4DNHzAiiClR1GuuAc0fh48jIPKvb4sCX44OXbaRhIFpstcX4Bu-vgwtg29OWZybYOmcUV5jAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6zbZ6SqycDWEia6ZV8bs6mz0sxns2FDiOjP54SvjfSBwFztLeXgAPWpuVQ5Vpi8LCthzrdvqd9e3dxbBxlgn9ZQUgEceHbZ7XUdgjUwjIwN9tYvPAHJ1ZBRz-GQK_8HUErUfIYBsfN9ZweEDMJkGx2smwPZHcravPxbsyIMnH2ioRfwoBQ882aa2EX-tNqj7bzpWUXlloDTIORvu2W1jW8o17M1D8A51RtUR2CF11uHveBDqJVxYkQ5rqFpD5T1LVXgc5QYxSgxGwRqSifADlYLKL6Cpp__vmiN5RkKlpdSTPoyPquqoCE1UL8xhjrzHZxpQI-u8p0hZVAH9qbHEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب با اینکه حملات متوجه شهرهای جنوبی بود، به یک پل راه‌آهن در شمال کشور حمله شد.
در ماه‌های اخیر، جمهوری اسلامی حساب ویژه‌ای روی این مسیر ارتباطی باز کرده بود، هم برای ارتباط با روسیه و هم برای ارتباط با چین.
حجم مبادلات هم ۶ برابر شده بود به ویژه پس
از اعمال محاصره دریایی توسط آمریکا.
فکر نکنم تعمیر این پل ، خیلی زمان ببره.
بیشتر یک اختلال چند روزه خواهد بود.
هدف آمریکا هم بیشتر ارسال یک پیام بود
که جنوب رو محاصره می‌کنیم و می‌تونیم مسیرهای دیگه رو هم از کار بندازیم،
اگه قرار باشه شما مسیر تنگه هرمز رو ناامن کنید.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5974" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5973">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3mLLR7A5OzFH1j7_2ptJjNWCXzLcOiEawilizNxTSZkHBdxiRWQgcSq7eAh0YOur_4M4-TJ8ab9wlGZTePUnX6K13xup4cOfQm34WcDtNWcQl18banfdYNXdknRxO-3c7XDcRvKddxT_3ePHKs3fk7mB8xuNcwSnbTe07jBCuLnh36w-mDdNOQewS5fYkPadXGsAOyPBhSEJJcuJHpKMsTksUYfT9PQB5-6v-K7yI8ANcj8LaZYdMgn_LQ_XHA047KaBCw43eSNrjKoOa-pyurUs31PKGXj-KvcSvTjJVgoVOAA1S4bKtcGYfz8YPaRCMXTIjy5AQ6OW57qxycKdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=QbXazUGEnN-Ntt6JCHzi8AGBsK4CBzlbUQbV3O6lORe043YItQi2LBnVxkfxLBpgaQfPdjqFV0KFSjGgDiE-lM5vr5UwALfUZBi5jlDBc9TACv00w0u3cQzavLVA7AjTG3t4iHknxrV6HeGy2gTfmBRVrOI_HcNtnXjCBKsAobdZ7bqyeRPEm4YJn8mY-oeRQm-hrys0IAJ5nuHpBCy2eSYQbekxfaccfgE_A0OrVAIsEBk9XK-Vd1uXRt-xAXkCKGhtLotZFP2RwbCqlCj3jtUSQH7BLJOjYJoGcSaOvULYTNV3tJfIvV9tsv33ui9qwhs_C-CButkAO2Rsmlr-cjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=QbXazUGEnN-Ntt6JCHzi8AGBsK4CBzlbUQbV3O6lORe043YItQi2LBnVxkfxLBpgaQfPdjqFV0KFSjGgDiE-lM5vr5UwALfUZBi5jlDBc9TACv00w0u3cQzavLVA7AjTG3t4iHknxrV6HeGy2gTfmBRVrOI_HcNtnXjCBKsAobdZ7bqyeRPEm4YJn8mY-oeRQm-hrys0IAJ5nuHpBCy2eSYQbekxfaccfgE_A0OrVAIsEBk9XK-Vd1uXRt-xAXkCKGhtLotZFP2RwbCqlCj3jtUSQH7BLJOjYJoGcSaOvULYTNV3tJfIvV9tsv33ui9qwhs_C-CButkAO2Rsmlr-cjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=jEHu01nhiuDat_cFxYIiS_gnQK8ktTFKrdGjVK3hI-4TDTWHJiCFJjtr0DSwX9sOR0ks2jtBz-tFwAf3xT8d63taASVu6UmfhezcZzaUFheWpjFiKjNbFQ5QUDBkkd-kLN0ZxAulk_XhGfGNVN1z5VjdfSnBPe1OIxwpEfsW3P4HWalM5A83PK7L4QcwyzGu3A_UzJ_LhKyAAkjwu9X3M5iivxiN12RGdfTNi3KLjvAbD7Agf8LYvnJYwygSMn4O-SFSZ46UTcSa19O4gsF1I3h9VjTiwgNTuU-Ra8wP-7Is_sKQEbi3Ys5Xi0beQjkp_BRwdIe9zZWVHN4JnhFlGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=jEHu01nhiuDat_cFxYIiS_gnQK8ktTFKrdGjVK3hI-4TDTWHJiCFJjtr0DSwX9sOR0ks2jtBz-tFwAf3xT8d63taASVu6UmfhezcZzaUFheWpjFiKjNbFQ5QUDBkkd-kLN0ZxAulk_XhGfGNVN1z5VjdfSnBPe1OIxwpEfsW3P4HWalM5A83PK7L4QcwyzGu3A_UzJ_LhKyAAkjwu9X3M5iivxiN12RGdfTNi3KLjvAbD7Agf8LYvnJYwygSMn4O-SFSZ46UTcSa19O4gsF1I3h9VjTiwgNTuU-Ra8wP-7Is_sKQEbi3Ys5Xi0beQjkp_BRwdIe9zZWVHN4JnhFlGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت خامنه‌ای، پهپاد وار به پنکه کوبیده شد
و موجب آسیب زدن به اموال حرم شد.
یه تشییع جنازه برگزار کردن، هر ساعتش سوژه‌ای داشت.  گویی فیلم‌نامه‌اش
رو رضا عطاران نوشته.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5968">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=HDBR1AXgTiVh54Pq2_Pd5CWiUgXEDvNlC4K6GjvNFMK2CFvGBGOuDMvjP5MISDWKs4TzCwYIq183fedkeJL87PpGVSpg1bdB53zc7cpZxPEWD3og2XXQQFioOvmXr3x_ZJSQt63JyxTTSvAy7DS318CkvGy3HNuCtvtublEUSxvMxcHMwayttN2ZDQt0GA78_b3NGjhgFIP69EN6ZccMZ_17U2nMPt0XHx1P0HWOCziUwljFmG9vBm6knYhNfNTunH5yfO0Uf6rqgSJCWQcKLgiSPDqFx3o2xNw-PeUsKWdHJNWmC43LlYCRS7tzazLIaWzYnItePJf4kXxi-GHQRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=HDBR1AXgTiVh54Pq2_Pd5CWiUgXEDvNlC4K6GjvNFMK2CFvGBGOuDMvjP5MISDWKs4TzCwYIq183fedkeJL87PpGVSpg1bdB53zc7cpZxPEWD3og2XXQQFioOvmXr3x_ZJSQt63JyxTTSvAy7DS318CkvGy3HNuCtvtublEUSxvMxcHMwayttN2ZDQt0GA78_b3NGjhgFIP69EN6ZccMZ_17U2nMPt0XHx1P0HWOCziUwljFmG9vBm6knYhNfNTunH5yfO0Uf6rqgSJCWQcKLgiSPDqFx3o2xNw-PeUsKWdHJNWmC43LlYCRS7tzazLIaWzYnItePJf4kXxi-GHQRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=j8cWD8L_UH1WO8QUBNvf_CwF3wwpfYSBqZnWhtv8lO5jnxlKlDQFBp7CjdoHBs39mzprrjnfTvYE4Uxyd-uKgBowvB54GB7QLgApDMdu7cjF_NXUUR_EabuC7IUyXUiDyaGyXp7KbP13LfVgl6kidjLJywq_EDZkmpXgHfbdHkIvve8T_apPZEyhFm3yB9TecyOo_07BHg6BC1CFe5Y7Wih95uav_Q6DB3I-lNgCUGv1TFtB4EOthZgVAMMVXr-MoFYFlhjlkTUm-df5Abn8TpHEgoKoiFAcqqHSv1buKHAbLOUivzAofbcTAGn9gt_m5iQXsevenGFqVKXU5oCvYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=j8cWD8L_UH1WO8QUBNvf_CwF3wwpfYSBqZnWhtv8lO5jnxlKlDQFBp7CjdoHBs39mzprrjnfTvYE4Uxyd-uKgBowvB54GB7QLgApDMdu7cjF_NXUUR_EabuC7IUyXUiDyaGyXp7KbP13LfVgl6kidjLJywq_EDZkmpXgHfbdHkIvve8T_apPZEyhFm3yB9TecyOo_07BHg6BC1CFe5Y7Wih95uav_Q6DB3I-lNgCUGv1TFtB4EOthZgVAMMVXr-MoFYFlhjlkTUm-df5Abn8TpHEgoKoiFAcqqHSv1buKHAbLOUivzAofbcTAGn9gt_m5iQXsevenGFqVKXU5oCvYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwagcNE7-DRoBpQiqoAjZ8kkElg2WeDlSo6c-kDJ20K_1KeysK4D4Es5npy53MwP6CU28OenqkUiUe94dW4GrP_ofIg3mCWTobPq9WkVlxyoIHJLSjzhX3kaYLk4CZeTKM2DvtclW4xJ5mRJtRWu7cnnyhXgXR5NTY1Hqxhrci-piE6rVDN0b1bYjAGbvbpGYlx-mGBn4fd1dX-qGjJbPn7IfSdIOjmtDpeERj4GmmvGX2MED6PJGjklCiDE9aV3u5iW4bHLHj_wvIq_HIZkE4MoC2u64wcQRYttrt6nx9agoqTZTrKz18yvlUHM8l9K18d4tByteXF5mLeLd5G6bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=mN1bNWAJB8NRKsPR30rJw7CVzisaGd37HX5bjh_nMLoBcGSPnScJ1fCbcTiKtJDOxbPOHXOOtV0_Gl0K4PnkfU7QNUQL4Knm9ueRmBirPZHoN3jSYrd7TwiX6TCpOjTwRUi-3qS_UuBt0yr7pYq0PbnTCQEib2AOUrtFheAfEelGVDH1JxmE19dbNPRb1VHcFppBkazTebVqmP5ygb58UwcSGfkX4l1nkqXnJJCRNJs7_fsHt3G7-vfIHJmQ2i9gnfx3L0MJch7Jie60vzP6jfC4jxhww8O-7gTQVdZOMn4nWV9FABVI2xEUfAXAWdQqdDHOYoq9BiXUPsUrp4rAzX8m4qcAwHWF6_n-8BAuwU5nRQJe3DABC_0cJl_9JvJLivznztCUsApPfkgkvHzHjOFlvE0yS-WkRHu6OS164ztkVjeyeoPLIQpDgpdpvkPKRmwEMpyEAY0BNcJzQ3YPO8IB4-AMTLtSTrG_51Ah1npi3V8PVy5fCZflPesDMCYniQvrDhu1oAJiF1SmxhYZu_J_RxJb7QIQ4pjlOa1QBZ-ZH949fx4SN9R5QxwowTs1zdONDNcux7THGEiPZq_c0h_s-sPEGU7__rz3Mu3zVbGUJAClMnkB8oMtZWOgFThlU4z5mRke1WiqS3k70V9Rsb0QY6DLiFFZkiW0B92khbU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=mN1bNWAJB8NRKsPR30rJw7CVzisaGd37HX5bjh_nMLoBcGSPnScJ1fCbcTiKtJDOxbPOHXOOtV0_Gl0K4PnkfU7QNUQL4Knm9ueRmBirPZHoN3jSYrd7TwiX6TCpOjTwRUi-3qS_UuBt0yr7pYq0PbnTCQEib2AOUrtFheAfEelGVDH1JxmE19dbNPRb1VHcFppBkazTebVqmP5ygb58UwcSGfkX4l1nkqXnJJCRNJs7_fsHt3G7-vfIHJmQ2i9gnfx3L0MJch7Jie60vzP6jfC4jxhww8O-7gTQVdZOMn4nWV9FABVI2xEUfAXAWdQqdDHOYoq9BiXUPsUrp4rAzX8m4qcAwHWF6_n-8BAuwU5nRQJe3DABC_0cJl_9JvJLivznztCUsApPfkgkvHzHjOFlvE0yS-WkRHu6OS164ztkVjeyeoPLIQpDgpdpvkPKRmwEMpyEAY0BNcJzQ3YPO8IB4-AMTLtSTrG_51Ah1npi3V8PVy5fCZflPesDMCYniQvrDhu1oAJiF1SmxhYZu_J_RxJb7QIQ4pjlOa1QBZ-ZH949fx4SN9R5QxwowTs1zdONDNcux7THGEiPZq_c0h_s-sPEGU7__rz3Mu3zVbGUJAClMnkB8oMtZWOgFThlU4z5mRke1WiqS3k70V9Rsb0QY6DLiFFZkiW0B92khbU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=rH-7e1HptUNLa6_aKo7SzAsmVI2giQ6KxRot1BVdQ9qOmHF_TpAJ08Hw6sQyjy3PwOTzl0BPouyJCTbVf1lbMUJSBeCx1NhXbJmPw4dVlNJgwrnoPYRpEgMlKEiAdgpqcNnpvJkQpAdc_FIx_cEEz_16wM7pAegICGP9230WajTMmBcBdG4uV7X3QXkzyDtAvpE6-5t4_YBJkMoinhyGMgcy2WlEXTB3snnGyTWkmGLh-ulHSFzD1OXTjEGfL2k_Uqu9SYGsYUk1n0KtiZbGnaZMk535EpfqwUpZ5aV_n-_robobL4DoN0oadM2AqH0EJyXcdxA44o7b0PuOdEEpZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=rH-7e1HptUNLa6_aKo7SzAsmVI2giQ6KxRot1BVdQ9qOmHF_TpAJ08Hw6sQyjy3PwOTzl0BPouyJCTbVf1lbMUJSBeCx1NhXbJmPw4dVlNJgwrnoPYRpEgMlKEiAdgpqcNnpvJkQpAdc_FIx_cEEz_16wM7pAegICGP9230WajTMmBcBdG4uV7X3QXkzyDtAvpE6-5t4_YBJkMoinhyGMgcy2WlEXTB3snnGyTWkmGLh-ulHSFzD1OXTjEGfL2k_Uqu9SYGsYUk1n0KtiZbGnaZMk535EpfqwUpZ5aV_n-_robobL4DoN0oadM2AqH0EJyXcdxA44o7b0PuOdEEpZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkLyoPH8x_JNQ0M1Rq6CeLraUXZo30LxKqSAGLHff78gsVs2r5MyX4zwK12Ob_t3q9j3nW2U3WyGulNXXML3OmEtpSbLdmDuz06RxUiBW7ZB084SNQusk8ae2z1Vkft3CCIctaKBZNGfvqwxVPearq57tCapHCdsDClngQA3bcdOo0sd5ScnqHGL-4b6vpsiju8lzlUn8E3OsrFJ7jYW_xFWS1qOvHml2lCUTePYiWrbQaJCVAKrV5qX-awtbaN9ZAW6eedUMKusTM0KL76qJJs1DrP7qQ0BIFAqFlbS5UsjniticFkxiv9EMUfFSKf5cL3O1YVkxF_T1Mx0QFY5zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=Evjat6EjIW9ap3a8XcSum1onmXP2XNgRF2kAIWfrndJ0R6MDFs85fgw4EGE8jz8NMJ8Xpw5JaVOt-_0yDDm3jFfFvXY6QVjZpSdPA21eGicNQDA62uglQ93K_Enc9EvBfT6OSxPFtj94Xp-tO1mgOFBVTGDeqvyvgcxsGo6OuZFbmGwUD1RVyhN2TKjfwiQkUBvp872IPB3IP37DTlWr0C5e9A7K2nrchtoTTaQR4dpMtOYbQwpC64okJplrKHG4-pkDWicN9_nLrvNZ-W8U8M77In4P0FVox3tf9qYj83zVPmE4SEVxYzzLxH8m-k8Ahr7Tkoo01PBKjpVaQJPaow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=Evjat6EjIW9ap3a8XcSum1onmXP2XNgRF2kAIWfrndJ0R6MDFs85fgw4EGE8jz8NMJ8Xpw5JaVOt-_0yDDm3jFfFvXY6QVjZpSdPA21eGicNQDA62uglQ93K_Enc9EvBfT6OSxPFtj94Xp-tO1mgOFBVTGDeqvyvgcxsGo6OuZFbmGwUD1RVyhN2TKjfwiQkUBvp872IPB3IP37DTlWr0C5e9A7K2nrchtoTTaQR4dpMtOYbQwpC64okJplrKHG4-pkDWicN9_nLrvNZ-W8U8M77In4P0FVox3tf9qYj83zVPmE4SEVxYzzLxH8m-k8Ahr7Tkoo01PBKjpVaQJPaow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله و برج اسکله بهشتی در چابهار</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5958" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
گزارشی از قطع برق در مناطق گسترده‌ای از بندرعباس، بوشهر و چابهار</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5957" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=HHKSUR2SakxxFDVy33Fwg1BR4G0KZdtrbyFxaWapj3wCuz4vWIlBJvUIyYFVaMeKIHhcxqv9j9GDEBS456btOQLLdW6sbfFXjMani4MYV9-BtoFTPZg6fuTyZUDZwftxxGq5Jj1iUCFMCFGDwfr91XWY2sFRLJsi2g6Rb9vQYRDfMm0CX3rVAFqtxumcZyjZqn82t0n0nEaOjkwoiG0nQK0Zj-IzSXb-7a7yul0HMyBTkAqr-GSHWvz45DG56b2tC607JmGrhlYjCi1fWZ7j6xO1BiCV8x5WLjvdheXE-V-eAe0XjOiL9jjLLuPkYyrw9goSIfmm1kJQ87o34llc-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=HHKSUR2SakxxFDVy33Fwg1BR4G0KZdtrbyFxaWapj3wCuz4vWIlBJvUIyYFVaMeKIHhcxqv9j9GDEBS456btOQLLdW6sbfFXjMani4MYV9-BtoFTPZg6fuTyZUDZwftxxGq5Jj1iUCFMCFGDwfr91XWY2sFRLJsi2g6Rb9vQYRDfMm0CX3rVAFqtxumcZyjZqn82t0n0nEaOjkwoiG0nQK0Zj-IzSXb-7a7yul0HMyBTkAqr-GSHWvz45DG56b2tC607JmGrhlYjCi1fWZ7j6xO1BiCV8x5WLjvdheXE-V-eAe0XjOiL9jjLLuPkYyrw9goSIfmm1kJQ87o34llc-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی گسترده در بوشهر
🚨
کشیده شدن دامنه حملات به جاسک و ابوموسی
🚨
گزارشی از فعالیت پدافند بر فراز آسمان اصفهان</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5956" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vS72DUONZkM6ExCztgaCi7y2qVdB2BTbF_iprVEKvlcRBD-cRPuTJEqMg9IdAwTwhFH3RWecwBchbEfzSwpjItjvdAOiNMpEZVT_rneRW-4qoWtv3U1Cykpy6AsZukJm27nfB60lnZLqDVwWqWoznP9hObMbGkWQrZSkg4RLHWIA4dEh7TpNOqRJUSgZ_dlbanjAHGVqiFys4LtI8_JxGhWlpeYlXD1xSUFyDGSYtNh6-wl4bbStCMlW3rW0QckQerqxrgH4xNMg0m5_I5oWP3a7IJumVYhDG_n1NyoeHPLRnGLLA6spJMHX0OtU9wuJcVG9Kxj8EvhjJNLHbx4Mhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت مجید موسوی، فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5955" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
گزارشی از حمله به یک پایگاه بسیج در بوشهر</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5954" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5953">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=ZrFYtQS0Kk1g3V9aH5X55zPl-XJqY7wSe2X0jvMvI-qie8x4C7XTGQ1YGlaipzJ3myFjkFpa8UtlFMSEtHetqIT9EXZRJCHyynJxP1sYLe3oMq1mYLs2KzQVHHrFoajQPTQTYVEOCWYxldNfEou35endPPjoXxR_oRnEP1Uu8Us0CbsFpzPJUxlUHjfx-z8PEofZQ30u9qMQahZjT_DOYuW0hoSNJPaJm-3gDC3Zmsq6ZhOqMOBIZ89ZR2mHeNLEAWFWE_7-S5FZjwGria8PU4ckgyVKpKgDB8XWbA0_ouX81pS-GWTUW42cghqNFESe3lcaQb-gU4PhuKW07lG5Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=ZrFYtQS0Kk1g3V9aH5X55zPl-XJqY7wSe2X0jvMvI-qie8x4C7XTGQ1YGlaipzJ3myFjkFpa8UtlFMSEtHetqIT9EXZRJCHyynJxP1sYLe3oMq1mYLs2KzQVHHrFoajQPTQTYVEOCWYxldNfEou35endPPjoXxR_oRnEP1Uu8Us0CbsFpzPJUxlUHjfx-z8PEofZQ30u9qMQahZjT_DOYuW0hoSNJPaJm-3gDC3Zmsq6ZhOqMOBIZ89ZR2mHeNLEAWFWE_7-S5FZjwGria8PU4ckgyVKpKgDB8XWbA0_ouX81pS-GWTUW42cghqNFESe3lcaQb-gU4PhuKW07lG5Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب - چابهار - حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldywb3fXIuR4jlFvhCX0GzG5p1okD9Ortda31H3MT6SKW25VVu5siKU4NG-mWO4Ee8aREsEqF5S5mTwNwY2m8V26D8MUC7-cWYn0Y_cdLQv7kmHsPQEll-_ecJRDrNS2k99RU32_uFv8noo__dQ6htBr2ne9i4JLvDfXxG9fah1cWDA2O3F8ImMXkhlwXarneK6AQtOcjIOzK7FV2LZ1CAkijtpBG6XiV4_D191TPbbzDyeRfewkNzsikJjZQ4vEEZ3VU3UI5JBIwph0lg3OrhvvdFTgrVfyGV-rS2dd2n6eP9tAssaD0YwwML2G_kykjfDmThpkokl-HpotCsMZgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک سیستم راداری ضد هوایی در بوشهر.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5952" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5951">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حملات به قشم و بوشهر نیز کشیده شد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5951" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5950">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏ایرنا: صدای حدود ۱۰ انفجار در چابهار و کنارک و قطع برق قسمتی از شهر چابهار</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5950" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=A6faYTV0uIyaSGYz8g2QtKEJujzYJLBJWpRpfr7v2DLc9DWzfcbJWfzRfLFos5ENMTLM92xQ3wVZf4-jFfu-pBTptI6sqeDpq0hpC8v2Hvnz7328iJTuiu43LvYlxQXs13wL3rLgOMq_AhPVSs1OgihzIzO4LZZyftaYN-T2Wf1SjXIJI91H0WJM2wr1-QqGwHJ8EBmFxDl1hcaT3OXubxsMl-F8Ptd3C-Drm70YsSWB0ptgX2VLwab88wmsnIrYrWWvcHmYFYKeQ37SSf98BG8vDL-6kehMrVIPWoBpSGq--QcfSEafn2pam8m6n0Gtffc4hQ-SqTvk2YcWp6sRwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=A6faYTV0uIyaSGYz8g2QtKEJujzYJLBJWpRpfr7v2DLc9DWzfcbJWfzRfLFos5ENMTLM92xQ3wVZf4-jFfu-pBTptI6sqeDpq0hpC8v2Hvnz7328iJTuiu43LvYlxQXs13wL3rLgOMq_AhPVSs1OgihzIzO4LZZyftaYN-T2Wf1SjXIJI91H0WJM2wr1-QqGwHJ8EBmFxDl1hcaT3OXubxsMl-F8Ptd3C-Drm70YsSWB0ptgX2VLwab88wmsnIrYrWWvcHmYFYKeQ37SSf98BG8vDL-6kehMrVIPWoBpSGq--QcfSEafn2pam8m6n0Gtffc4hQ-SqTvk2YcWp6sRwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات امشب آمریکا به چابهار</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdFQ0BBxrP05W0X_yyXBUjMkMMnoAYpJ0DagrqE41W-tN2RHpV4fr_-It_esMqx0NBJDtOY8-ZoaFk-FjdBHQT7CNsGFHdzaUGwifPhAaXnWRzohpENx0Lm1qX5mSMOeeSB9Hcv71Zb9ecRZNDRqRhTyTLWQ3g7KJ7A6KoyyDwRv3on17yacuUypKn9H-WtCxJWtiLXXz_jsziyd8GtWh1x2RdL-yWhKkBsXbstlfHXE3Curs2UgXcE-IkdpPpjszlUwrtonJLHjuO5sYzWbXHjdgLt3zxXXF6piI7biRu46OIA8o95C6NmxGpLBKISbpTXaihg1bwPnEB7hhxjFYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به اسرائیل اطلاع داده است که قرار است امشب حملات گسترده‌ای به ایران انجام دهد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5948" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5947">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5947" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5946">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5946" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5945">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">جی‌دی ونس که طرفدار مذاکره با ج‌ا بود:
قرار بود ما محاصره دریایی رو‌ برداریم و اونها هم‌ دست از حمله به کشتی‌ها بردارند. برای یک هفته خوب بودن ولی در ۲۴ ساعت اخیر شروع کردن به حمله به کشتی‌ها.
بهشون گفته بودیم اگه
حمله کنید به کشتی‌ها باهاتون محکم برخورد می‌کنیم. نمیخوام بگم امشب قراره باهاشون چی کار کنیم.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5945" target="_blank">📅 22:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5944">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=KQSggpvmtyOPJBtQBcExBWKBYC_s0KFVLon1e56py0Ze8EEV1l5sv606QWikWxb7iMOn3ZJTg5mfBsaSZXPPrqeU_Ujh5Rgncdcly7o4RReOG2sXFNeHkihRMLsDHsXjjCDm8J72bAcPqCSv7b0VX-ngUw4yw3ydiZvBthExpD0kDhdz9SCYfaa479JaxZeklVX0BRG1ld2nleOaPx_Ov7qcCJU8QwZbohQep3N1d5JH6ymzrSf6947Zl75XA9WVx34e34HMFsO0D9_T_0tZ5mJE-druKctd9g3fmvmd43yNNWjARNw78eAyknXodzUaWAf0e893JEsyuuUfuFSCUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=KQSggpvmtyOPJBtQBcExBWKBYC_s0KFVLon1e56py0Ze8EEV1l5sv606QWikWxb7iMOn3ZJTg5mfBsaSZXPPrqeU_Ujh5Rgncdcly7o4RReOG2sXFNeHkihRMLsDHsXjjCDm8J72bAcPqCSv7b0VX-ngUw4yw3ydiZvBthExpD0kDhdz9SCYfaa479JaxZeklVX0BRG1ld2nleOaPx_Ov7qcCJU8QwZbohQep3N1d5JH6ymzrSf6947Zl75XA9WVx34e34HMFsO0D9_T_0tZ5mJE-druKctd9g3fmvmd43yNNWjARNw78eAyknXodzUaWAf0e893JEsyuuUfuFSCUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/5944" target="_blank">📅 22:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5943">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=KkkseBSes2NikL4SONuUUVQzS8T4vy3vBnjL1RD-JqmMnmyLB_1JHwpsCzWLkVUnWcFuzg4GVlA9wMb1e1NXsiS3Jnd2LpGRlWI_vVRAG1dDtL4mEtt-vYFOEhrf0ma27BD23VK-iRqb5S0n3ntdFJY5sr1XFJqIJCGsAJTt5gGLOANvsjAt4GQ8IfNR7q0sHOTWTPUnEiUWwKTk2JErKEBFO2OjAHMARO8SovUY7jaqiFloO43wc0_h5Nc8PYNWbp6vEWSWsUDz4DVLlVVLEccm5WZKl7n1LEe7KIJiIBntikf4jVqOy8-eweNcIMYbjVM6kyr9SXzLxXZOFzllJwkpHLDZnRF06HOB61BmPnryX3l5ZSoNBkFNzY_JGz82ywX61H40fY3VqffziRtmSFoiuycMh1pV1XhYUPVIVHZlZCOBO4voZiajuqHMKkKnRs6Bq1fcj6jU7q9idslNcBKj7DdjJ0hQx_PDxyMoKPIve2gabDGpWxaAds503mq4Uv7ORJPiR7L7YCyrqVXu9gbZedeEthdlomYqRgtiK4cpQoG6-4uWbhTCJGFshAw5fhTOdpRMy1ldffap0b-lBt7e-rQSoT7LFavj8pFsNHsnU4q68o_F9e9wYx-zzRJ7Q5jlti0-nQ4mRvlUcd2lXg5qiuEpt6aiwG0c9xdPmeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=KkkseBSes2NikL4SONuUUVQzS8T4vy3vBnjL1RD-JqmMnmyLB_1JHwpsCzWLkVUnWcFuzg4GVlA9wMb1e1NXsiS3Jnd2LpGRlWI_vVRAG1dDtL4mEtt-vYFOEhrf0ma27BD23VK-iRqb5S0n3ntdFJY5sr1XFJqIJCGsAJTt5gGLOANvsjAt4GQ8IfNR7q0sHOTWTPUnEiUWwKTk2JErKEBFO2OjAHMARO8SovUY7jaqiFloO43wc0_h5Nc8PYNWbp6vEWSWsUDz4DVLlVVLEccm5WZKl7n1LEe7KIJiIBntikf4jVqOy8-eweNcIMYbjVM6kyr9SXzLxXZOFzllJwkpHLDZnRF06HOB61BmPnryX3l5ZSoNBkFNzY_JGz82ywX61H40fY3VqffziRtmSFoiuycMh1pV1XhYUPVIVHZlZCOBO4voZiajuqHMKkKnRs6Bq1fcj6jU7q9idslNcBKj7DdjJ0hQx_PDxyMoKPIve2gabDGpWxaAds503mq4Uv7ORJPiR7L7YCyrqVXu9gbZedeEthdlomYqRgtiK4cpQoG6-4uWbhTCJGFshAw5fhTOdpRMy1ldffap0b-lBt7e-rQSoT7LFavj8pFsNHsnU4q68o_F9e9wYx-zzRJ7Q5jlti0-nQ4mRvlUcd2lXg5qiuEpt6aiwG0c9xdPmeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برگزاری مراسم رو
انگار غزه است! با بسیج کردن اینهمه ستاد و پول و ارگان‌ها و…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5943" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5cRFtCIStJ3eZwmg79RKA65J4mwBIaArDAPhSxtzWC9gQKktcQMn6tINmi-BwCqFdkYVjHL5cCbabsk2x20DvYiRepHJ9e_yFdCjlwMeyJ2BxwsASBABKrlg8c521GdFIylBn9j9Jy8IYRZY-n8aettiTQxjFZspE_6uLlm8_tO6xp2LKChbxzWKLb2UEweir03Pk5cSNwAyBL1wikLgdpO8466Bx8PqG8pkinWwpUEHlEsod7ee6jLXkQVdCOxyhIotUjZeaD-6Vrr4Bz5ObqQGAuJ29vLFPJlZX4hiBVuQi2FW8i6tJISQwvm1Reo80Qvk1qNxvPt5KXVXLeOAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: درباره جمهوری اسلامی کارهایی انجام می‌دهیم که باید ۴۷ سال پیش انجام میشد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5942" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=ZNNgDadxd33LkG2o_to8rriY0w3XC0J55PYkTGBv4YbR2-G55KcePkTgbQl-7GjcyKOAas3T6rVj-W24QXEgSUjE3ne9Uij1TXLmZzsGsY9BECCj4WZfPm7KbpRKyVNmdB0yNDKGHP-HTLYuwTsjTsGtdrlL0lc_ZNdhbGpa5DS7ij9wWWTElnTetN-r7fy5lkWpk00IJ3dN1M426X67GouQBFNpmpwSOjeQi6q6VkKijEX3rFm4sJH0wCXiUFyO7Mv6Ov-JRkz51XnjNIkPAE4HsvJpx44duURpO_kRAKr4vbOKJ7ElL6DMJCW-3Po6ykksHyd7w3pDeLDDukBIeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=ZNNgDadxd33LkG2o_to8rriY0w3XC0J55PYkTGBv4YbR2-G55KcePkTgbQl-7GjcyKOAas3T6rVj-W24QXEgSUjE3ne9Uij1TXLmZzsGsY9BECCj4WZfPm7KbpRKyVNmdB0yNDKGHP-HTLYuwTsjTsGtdrlL0lc_ZNdhbGpa5DS7ij9wWWTElnTetN-r7fy5lkWpk00IJ3dN1M426X67GouQBFNpmpwSOjeQi6q6VkKijEX3rFm4sJH0wCXiUFyO7Mv6Ov-JRkz51XnjNIkPAE4HsvJpx44duURpO_kRAKr4vbOKJ7ElL6DMJCW-3Po6ykksHyd7w3pDeLDDukBIeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - اسکله بندر عباس
زیر حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5941" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=XdiFnAY8cx-8Fv25qRvBB7t-04v2x-XygU4e8FjPBR5CFNIrZtAQ_xQf-fEQDJyVsvythdlpq5tN7FstdChi_hlNAFh_LPXCAuR9PPGcWipwtgEFldKnSU3ytDB02tzU_uAMLMxm2ak20XKeWFDb_Ba3baOUpJ3QuhvE62U4coyiVkx0_0TtqqtpgsSoTIwnsyjedMvzrb6N0xcuyZfGxoNmATeP0OWMF2mg_JybBQi2UEHeGDNRGqVwOjJFk6OMfcZ6qWK0dRijVfFNKAoVtdXUKqITTmpuWO2w9lJ6ekmZGgeszCmMmkatiO-oWWYDC-M8-C-HQmlhJHLPH1b-Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=XdiFnAY8cx-8Fv25qRvBB7t-04v2x-XygU4e8FjPBR5CFNIrZtAQ_xQf-fEQDJyVsvythdlpq5tN7FstdChi_hlNAFh_LPXCAuR9PPGcWipwtgEFldKnSU3ytDB02tzU_uAMLMxm2ak20XKeWFDb_Ba3baOUpJ3QuhvE62U4coyiVkx0_0TtqqtpgsSoTIwnsyjedMvzrb6N0xcuyZfGxoNmATeP0OWMF2mg_JybBQi2UEHeGDNRGqVwOjJFk6OMfcZ6qWK0dRijVfFNKAoVtdXUKqITTmpuWO2w9lJ6ekmZGgeszCmMmkatiO-oWWYDC-M8-C-HQmlhJHLPH1b-Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مراسم برگزار کردن … ستاد برگزاری ، هزینه هنگفت، ده‌ها ارگان و ستاد زیر نظرشون.
بعد کارهاشون رو ببینید!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArQtJ73WTTYijev9DR7CKbsz899g5GDIGwROQpJ8VERHN4BCpeBkcD37t1cZevnan108atfIs2Q8R8KiVaP1_tE6ruRXmF6TlqYxwKZT1hzx_9MpzsdMkECFKs6H-uo8g4cZ6uaj_Ka27uEEpx_ch65UWI-9h46cBVRa5yhgV8rsG9Fh-5h1RtB-w0qX50-sS56Q_jULgOuohYayUv2isWVmZYlz-q26TSxOiMLnF3tNYC1w3HVEY5SDgwiKa4UFqjeSQJO5sH3hEhYcOnvf8h42AKWQnRgkkRw4JTLncGByZCxJ2ZJ-bSBt8ahMVDeylZI8yBbz4i56URI7uxuBaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کشته شدن ۸ نیروی ارتشی
در جریان حملات دیشب و صبح امروز آمریکا</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5939" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ: اومدن خواهش کردن زمان تشییع جنازه ما رو نکش. بعد وسط این مراسم حمله کردن به سه تا کشتی.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5938" target="_blank">📅 17:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=jPkQhUimNyNz-9O6eUuzuc3mDMTKUS7n2aFzCDQE00Ndlfrrr-3aE0LoW-hIdx2JsfAMfkWr3_cuwvCdCyfIJc36HL1C_zOBc8trovreF6F7nJlkY-MeIeHWZmIG600C-yoKMk2ygK4SRC2D3_sZU5kAj54v9peqVJOfe0yJfUnNZWZxH8cCslAcP8w5JQGsk0Hh53NdPO2E5N2iQLBMGlhLsuS7TzdxWLqs3LuOuahqZAUAa8GAgUtUMVbExyeGuHuWis3UeeIIcpeGrzEBGC16V4RLmBWxRgaIIYfgpP1zmvqzgHfHenmw3KYjD08y9qQc5ChL6mk-_BLPJR4a0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=jPkQhUimNyNz-9O6eUuzuc3mDMTKUS7n2aFzCDQE00Ndlfrrr-3aE0LoW-hIdx2JsfAMfkWr3_cuwvCdCyfIJc36HL1C_zOBc8trovreF6F7nJlkY-MeIeHWZmIG600C-yoKMk2ygK4SRC2D3_sZU5kAj54v9peqVJOfe0yJfUnNZWZxH8cCslAcP8w5JQGsk0Hh53NdPO2E5N2iQLBMGlhLsuS7TzdxWLqs3LuOuahqZAUAa8GAgUtUMVbExyeGuHuWis3UeeIIcpeGrzEBGC16V4RLmBWxRgaIIYfgpP1zmvqzgHfHenmw3KYjD08y9qQc5ChL6mk-_BLPJR4a0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=jtcTOJiuG4aIYBDmF08UNtDL9Il_6Ha9rQ6WTNzJX4zvUT-_cycXMxQcQWRH4Uagn_ZI2JhZtaExpvdLKj9MGL_PyBLxu1ZDAx46RUoxdvMKiQOBxx7p882zRPd_xq6LDmkMYba4p9LdMQwlMB3gKXW5xUJ8ubkUzkdaemXxtdN_i5uPtGsgk-gy2i3onywuA661SzIOMHHLlzqKnIU5OV__xn-TR46-cp-B4uQhqdccgMSCG6XAR9VSRrr4x1q0W2oRbdD_a0mmgnm3tTIL2sUVyb8HP68JCAdXIfSpExf6UuNuEifHJXp6pqlpnqCjy9zIPy7gz_x32laqiY-RJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=jtcTOJiuG4aIYBDmF08UNtDL9Il_6Ha9rQ6WTNzJX4zvUT-_cycXMxQcQWRH4Uagn_ZI2JhZtaExpvdLKj9MGL_PyBLxu1ZDAx46RUoxdvMKiQOBxx7p882zRPd_xq6LDmkMYba4p9LdMQwlMB3gKXW5xUJ8ubkUzkdaemXxtdN_i5uPtGsgk-gy2i3onywuA661SzIOMHHLlzqKnIU5OV__xn-TR46-cp-B4uQhqdccgMSCG6XAR9VSRrr4x1q0W2oRbdD_a0mmgnm3tTIL2sUVyb8HP68JCAdXIfSpExf6UuNuEifHJXp6pqlpnqCjy9zIPy7gz_x32laqiY-RJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هگست وزیر جنگ آمریکا : همونطور که ترامپ گفت امشب احتمالا اونها رو عمیق‌تر و محکم‌تر می‌زنیم.
ترامپ : محاصره دریایی رو هم احتمالا دوباره علیه ج‌ا برقرار کنیم.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5936" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=EjMG1Bl9sFFaW3H1SkbjUmawHj83fLK9apsTeuHbxKLyvW7pBC5wVXEIq7IpQZ-4Z-I8TiGBwJnWXH-o8JPPap7Qm9usXqHvvsDrRYqUB-SFdZuL_GAFS2AlG3wV5Clrcvh-ampESfbmRAqXYTicsJsTQrVul-hMAGO3hx80uEalVVqCg-hNYk7tH0AIG_OJXs6JG1WWUZbpmDT9ZWVKavUe_0UWjDl_R3f_o_IadiWs2wX_TBtUB5p2Zm1KL48qzcadAmvvHfZHLsieI2be9Rz-xE6fYSuOkz3iY2thib9NAcXUESHXRis9vuMsVD24H1C79dUR8vR9_JvEUEiXkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=EjMG1Bl9sFFaW3H1SkbjUmawHj83fLK9apsTeuHbxKLyvW7pBC5wVXEIq7IpQZ-4Z-I8TiGBwJnWXH-o8JPPap7Qm9usXqHvvsDrRYqUB-SFdZuL_GAFS2AlG3wV5Clrcvh-ampESfbmRAqXYTicsJsTQrVul-hMAGO3hx80uEalVVqCg-hNYk7tH0AIG_OJXs6JG1WWUZbpmDT9ZWVKavUe_0UWjDl_R3f_o_IadiWs2wX_TBtUB5p2Zm1KL48qzcadAmvvHfZHLsieI2be9Rz-xE6fYSuOkz3iY2thib9NAcXUESHXRis9vuMsVD24H1C79dUR8vR9_JvEUEiXkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونها تحت یک توافق هرگز به سلاح هسته‌ای نخواهد رسید، اما شاید بدون دستیابی به یک توافق هم به این هدف برسیم، اصلا شاید راحت‌تر هم باشه، چون اونها دروغگو و‌ شیادن.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=EtqF_0It0Awc-h99--Nvx2QZvetLX95kUTuCcYiQ5xC-DDetGXf1hpO-fbNZhnVnr6VODgUD3V2BEcOGrsCL7y9C4ky6lTpOO4De0pzN-ezQ1eGOP_hcwRZ3p9AhnR9ag7XpsNqL8ovY-KgBIJfEydFJ4IfBg7y0zeT287GVm_Ds7QvgNwEQTQXE5QeIaWDHEX3tMSGlcwErqrAQL9zRb3_b3BkTB-y1aAj0cU0ZDZtcLpeB30DqxiH2GOPg3_BUfI5u9PWvkE2eA2PoR2dHzzNZyMrYzED7TtqwbQ0-DQ-biHfrZ45jKUUYlk3AE3DXBFw1Ws1PEBomTOc1lXCkoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=EtqF_0It0Awc-h99--Nvx2QZvetLX95kUTuCcYiQ5xC-DDetGXf1hpO-fbNZhnVnr6VODgUD3V2BEcOGrsCL7y9C4ky6lTpOO4De0pzN-ezQ1eGOP_hcwRZ3p9AhnR9ag7XpsNqL8ovY-KgBIJfEydFJ4IfBg7y0zeT287GVm_Ds7QvgNwEQTQXE5QeIaWDHEX3tMSGlcwErqrAQL9zRb3_b3BkTB-y1aAj0cU0ZDZtcLpeB30DqxiH2GOPg3_BUfI5u9PWvkE2eA2PoR2dHzzNZyMrYzED7TtqwbQ0-DQ-biHfrZ45jKUUYlk3AE3DXBFw1Ws1PEBomTOc1lXCkoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ساختمون همون جایی است که خامنه‌ای حامیانش رو جمع می‌کرد براشون می گفت :« کشتن بد است، اما فتنه بدتر است.» (پس معترضین رو راحت بکشید)
و اونها هم براش «حیدر حیدر کنان» می‌خوندن : لب تر کند امروز سحر قدس شریفیم!
ولی داستان یه جور دیگه شد</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5934" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=bQhmYg1rzQU-6I0Zu233TruiS-6f0zUDI-MfL0cbHpA7bGj7Us78BmW_7K4OfOL4qVu1vxYFl7u2JCF0wAWwPsyieK4tMompffwoxbSpM7z-w5VZnXGoQrTdjlB5uC5F4bn2BKSU1RoYCpwhdRUfuiCLxSRtSMUkD21HDThvgZ6xMXRj472b_YLFe-ZnL-BMpzjw_3BTYhY7SMYDoOaFlPfS4w3IxDZESQkF2--xP0FnaEHA7fbGOpmOpPnRcLXBl_dvcT3SUoEM3NoRLuBVnTo6xah83DBEgNPq9ekhyKuEQ07fkT0rwmLwbS5BzG2mBR5HfbUEoppxdTDQ2qXeFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=bQhmYg1rzQU-6I0Zu233TruiS-6f0zUDI-MfL0cbHpA7bGj7Us78BmW_7K4OfOL4qVu1vxYFl7u2JCF0wAWwPsyieK4tMompffwoxbSpM7z-w5VZnXGoQrTdjlB5uC5F4bn2BKSU1RoYCpwhdRUfuiCLxSRtSMUkD21HDThvgZ6xMXRj472b_YLFe-ZnL-BMpzjw_3BTYhY7SMYDoOaFlPfS4w3IxDZESQkF2--xP0FnaEHA7fbGOpmOpPnRcLXBl_dvcT3SUoEM3NoRLuBVnTo6xah83DBEgNPq9ekhyKuEQ07fkT0rwmLwbS5BzG2mBR5HfbUEoppxdTDQ2qXeFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : احتمالا امشب هم اونها رو به سختی بزنیم. فقط دارم یه هشدار کوچک بهشون میدم.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5933" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5931">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">هزاران نفر که اومده بودن توی خیابون‌ها رو کشتن!
صدها نفر رو اعدام کردن، هزاران نفر رو زندانی کردن. اومدن با وقاحت میگن ما اومدیم توی خیابون! طعنه هم میزنن!
شماها با وعده امنیت کامل رفتید
با پذیرایی و امکانات. حتی خیابون رو تخریب کردن برای تجمع‌تون، کولر گذاشتن براتون!
خود گدا گشنه صفت‌تون رو با جوانان شجاع ایرانی که جون شون رو گذاشتن دستشون
یکی می‌کنید؟؟ طعنه هم میزنید!
شما هنوز نه این یکی رو خاک کردید!!
نه اون یکی رو می‌دونید زنده است یا مرده!!
هست یا نیست! توی چند سوراخ قایم شده!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5931" target="_blank">📅 16:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5930">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uyz8UtjEqu6GEmjs-nN_PvpvZzrMb6Pl35kgYp64HgM8LGvqVFIVe7AQxc5atmy6Dby-MJOI4WJfwyKxzbQHdmg373a7kndQV-TTu42EASKbBCs91yukoNwaRx2Ze4v2C9LHgi7gneum4KsIlbt4YCjm2kRCUSGmxBOfqb3VflOSicJ_JYm2cQNzG7aNTq_6ZbTfS1i7XNjLLJG1nipL_YOsV_AmdFizQog1IZBj9cj97RUo174gHl2t8t1J2mCZ_DSf_VumxF2oxFikROE3_mLtVBZ35F-Byrq2FRqw9PeQv6KqegjHW6uCeSXADm53AMb81bWrguvjTbktyVo3VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه کیهان زیر نظر خامنه‌ای در دو مطلب خواستار کشتن ترامپ شد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5930" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5929">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6MQF6NZ99GXhRL4JUWySFgo9ECBzDZazIdAF695GIGgYTkVz9ibZojS6zyzigrp3t83ODbczMOyaXjHefo4DXwkPm6BKl69q_jOQhpdsrT8UMbO-jxybdu7MvqPijTHoIP0NP0Rzo_w4Dfju5zJTXwpgXCWipGvRzkVMXvJ5uOBxspZkU1RRPBFGWh6HIpkg_XMYOpAQxukvh4jFSkv5JfLy3izBWwoXd1zeesmILAjYs9lUMNT8MbIsYePjHdXUoV7ZbbIQT83j9YhENKIojg6UAxnrUrcBfBrIKk8Z8G93-CXiYErAM1tjmSMQjg4u0E0XWkUy8OzS0zL_AtxrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوش دولت چپگراش رو چنان بکش
که درس عبرتی بشه برای بقیه اروپا!
برو جلو! دعای خیر ما پشت سرته!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5928" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5927">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5927" target="_blank">📅 11:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
دبیرکل ناتو : حملات آمریکا به جمهوری اسلامی کاملا ضروری بود.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zgfzy6urmVnt_33HVR5p6UknW-3TQXflCg9g5-boaax6zkpSQul8Lzpi2rCQkqRZNadqvfNd6sQi6t2msJGvlRFQwtw-sWLBBJhtjn2ifyGbFvsaHzrh3WxHZBdcQ8EREV61CTJv7liIohZdIZKsy552T5pG8ZYyGrIKH874RExFJwalXHrwMF_Ba70nso-Ee1vf34Mj8OUnQHuiuU04-2kNmaKPhbSh_6R5djSQRA_IaJAFZM_P9zxV903pp3Pi6drvEBCSI9YEK8O2J1Kdiu0R4yjnnTiDTIuvWtF4imxKbikk_9YibVwzL1KSAMrUGxN1V96QFljpo7lGQH8ZWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
سپاه : به ۸۵ هدف مرتبط با آمریکا حمله کردیم.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5923" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=eJafRe1Kjur2NogOtOcAN3FNPNz1XM_bLn-VkLbSHxjO7nrnRhRwQUhSkMqXcJ8SVfRMC1t19guqlgVut2entSMXNAcwnq8z6XWBNEGznqquOTEL5JEw6X9SRa-SaBQYXvX5iH9wKX6sEA_auRbaKTPnqd0gg08GEUxGZupWZxrZ3bfWpKOpd91Pw2Pu0pVM9jaVnVqKySznfC425DqBt5ipky3D8R6mi-ndEDgjybRcNrBuDobQGagVgwhkCrYICE2Zo9Z331W4bjn8qYVDPxbm1ysXvQA1BAnoCoSOYo0Q7aG3afypK41t0rEjGXJrQ558jqjxi7SfyqF6td-dnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=eJafRe1Kjur2NogOtOcAN3FNPNz1XM_bLn-VkLbSHxjO7nrnRhRwQUhSkMqXcJ8SVfRMC1t19guqlgVut2entSMXNAcwnq8z6XWBNEGznqquOTEL5JEw6X9SRa-SaBQYXvX5iH9wKX6sEA_auRbaKTPnqd0gg08GEUxGZupWZxrZ3bfWpKOpd91Pw2Pu0pVM9jaVnVqKySznfC425DqBt5ipky3D8R6mi-ndEDgjybRcNrBuDobQGagVgwhkCrYICE2Zo9Z331W4bjn8qYVDPxbm1ysXvQA1BAnoCoSOYo0Q7aG3afypK41t0rEjGXJrQ558jqjxi7SfyqF6td-dnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس - امش</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdGavoIGGJ74K8pVc4VB5Li2msjH4eXSdeICni-35A19S5XPoPtEkh3kLgZ2qLRe-WdVUJYZFzrZiDURDAwbJmIzQ8tvHktKza7jJkWZPcdrPoaZ-ckQSQNdu9tts7IIjVLtum0OkSXYm2a26U2YuVgY5RMtGxiSXNv6h2iWHeX7LfGSJMGNNSfToGgmcyQh9tYaLR0rLRyHhOjuNYdz7yGTvBLbkUOmWYn94RDVCydD3RatSDztBDgMkP9aN_XXNl_MX83nvvmns2zGrxOantNXG9gWLd1dFQJPr9uOs_JrncHsO2Nv7hwY359uVyD8hLTbj4fw0O7t8dqb5bRunQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش ها از شنیده شدن حداقل ۳ انفجار در بندر عباس
تصویری که گفته می‌شود آتش گرفتن یکی از قایق های تندرو سپاه است</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5921" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا: نیروهای ما آغاز یک رشته حملات قدرتمند علیه ایران را آغاز کرده‌اند.
‏حملات آمریکا در واکنش به حملات ایران علیه سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5920" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در حوالی قشم و سیریک!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5919" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5918">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=ojl_-ZjXh-dLED2jO1tcPKzSzNWAtT4LVhm0TfNW1J6JbE4BA2-TZkTiLc02jvbcSPtzgizzUmUHClrU12fR9hf3g0hEr97IQsc-Z_B0GPpmzFJWeAwCCVEIe2ibqpG_NH0tWwhe83ZQCC7LgHsYABOa_WtComzXEAkbNpUnToKBOfn7mIpUUSoVQKvHIyAINX2IYo9FQNuc_pnb5siwmAwLG7-GIxhfqVWu3IZd6bp0JWwQ6gkboDAu-4wwJa1aTu-s4UqhqsHqIYWgan0FxuNhbONvIU14RVltESYYna4AmyCKM1hnPHZCLKpTfSLlsK6bQm3ssMjgJRCjh9pUvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=ojl_-ZjXh-dLED2jO1tcPKzSzNWAtT4LVhm0TfNW1J6JbE4BA2-TZkTiLc02jvbcSPtzgizzUmUHClrU12fR9hf3g0hEr97IQsc-Z_B0GPpmzFJWeAwCCVEIe2ibqpG_NH0tWwhe83ZQCC7LgHsYABOa_WtComzXEAkbNpUnToKBOfn7mIpUUSoVQKvHIyAINX2IYo9FQNuc_pnb5siwmAwLG7-GIxhfqVWu3IZd6bp0JWwQ6gkboDAu-4wwJa1aTu-s4UqhqsHqIYWgan0FxuNhbONvIU14RVltESYYna4AmyCKM1hnPHZCLKpTfSLlsK6bQm3ssMjgJRCjh9pUvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی این ویدئو دقت کردید یه نفر رو به کامیون جنازه خامنه‌ای وصل کردن؟ :)</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5918" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhOjycV_xo-_tDXrx_5JzG2HeKqvJ7jPZlW0-qTSW9EibULP-apxRtTWvCFdh08yi7eurdL88QFHe_KuvAv0UT9GzCTQ1NEExVD_TR0cSbvWD0LsRkwCqBUEMdHr_ALefhpjNEjFdHmuoQB1FJiVoXWnLcKQmc_QA_vq0mnMPjjkp6HJY3LbS_hU7BJoawSrLoYQG56bdhsvDnRABcS5Mspz9bBCRZVPnA-B843VTu5MWKP86E2kwf_rux0jeWTGzlYBuP0KA1uVxNVV5pULDJZN67avHQXtnriZiVou2V4WOIxv-Jm6SnpC2PPFRZN7ntgnRgSP50jaU8FY2sbtGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)  دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5917" target="_blank">📅 00:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5916">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qejzJQt1y8AjuplBALiClOGAjxjSC-Y77silh0CwMGwtlXAt5GgU2nvOuleYKj8x2DPGPZqZWx9RApnJzRTMFZdGyOyQTm5SKks8OF2PGKYpU9m3PMC_Jb6siU51_7RJXOrs3Ycap81a6tNkY9zvG50hBZhRUhHY2U5K198rA8bU64QuyYt-p1fg2awA20WtXeAtbBUl3JuukCo80aDyWIqqg5xpKxKCaSeEkfkBoMta8xvM-cLfwvij4OihOvSmgInOKiY86QtuTEmXUb2363SUKy5RXYwi-uN6L4L_GT16LDCBhvG_Hel6Oejw84ojRjMdLol-VRU7UHtQFMf5Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما موشک میزنیم بر اساس حسن همجواریه
شما بیانیه بدید اعتراض کنید
مغایر با حسن همجواریه!
کشورهای همسایه هم تازه دارن می‌فهمن
مردم ایران از دست اینها چی میکشن</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5916" target="_blank">📅 23:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5915">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=BdXuyKBwqzJkbfMiiBmv94PGO8oQcmN2x469vBFiz7qTMjMXONu-rFJ4QBD4o2qJAqJPWn_YRYh9t2_S9kjCTup-rP66Ixlgzk_IUY2vZZ6ebya6H7_Wuv7DEFK7VWzFypu8-WUnfU__ExiwtpU152TGP8tgphNGhpE2GT43KPPixejigQZyLv23NRQ6G2981ljxX8DV13jzJZTCjLieTJ8bOOMSWTdPEk0ejnC_Z0vqwnIzdmhhUdpPFP7yVLqv6pI5FlmSGSfIYBQle_SQpBaQnupmibrJ-Akbgm4SnXewW8nkJi8qU_kCVANQ9v44o6E8f3B_ZygqGkUDVkyFPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=BdXuyKBwqzJkbfMiiBmv94PGO8oQcmN2x469vBFiz7qTMjMXONu-rFJ4QBD4o2qJAqJPWn_YRYh9t2_S9kjCTup-rP66Ixlgzk_IUY2vZZ6ebya6H7_Wuv7DEFK7VWzFypu8-WUnfU__ExiwtpU152TGP8tgphNGhpE2GT43KPPixejigQZyLv23NRQ6G2981ljxX8DV13jzJZTCjLieTJ8bOOMSWTdPEk0ejnC_Z0vqwnIzdmhhUdpPFP7yVLqv6pI5FlmSGSfIYBQle_SQpBaQnupmibrJ-Akbgm4SnXewW8nkJi8qU_kCVANQ9v44o6E8f3B_ZygqGkUDVkyFPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه حمل جنازه خامنه‌ای</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5915" target="_blank">📅 23:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5914">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5914" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5913">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)
دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5913" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5912">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hu7VRgShUIAvIDML_FDaaWv7S9DNVEynldZmupWtQoXkf6dRcYA7NkNJZR3gSBmhROAMglqrjnCQZeHc3tHEGfyjncKzDqJjxd-Kl5eqEg0BQIIl009Vmllwjr5_5XQO7qWT2iw8XxFbAMupf_-p3hjZlHzsGxOEYqEmnUNYtdbBjDdanS7kdzzoddfLhuJIkmQx44QuLmDaguCppFgw5oARL1RaJJY_tu1GXk43rXPxQwYoplH9tMhJNQvKoLHzcRbQZMbJ0TbrN9zSNr_Af_MP1L1x2uGL-PMDmIz3sn8FTxYGWuOtH017ieGC7nVIRfRFeOJ6Ry5aGjR3BqzFKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQJ1i9Z9Z1SNloQoRLOCINAwVRWnfVmPmUYOCce81w3txyyalIK2S99e9Ry4t53XDudwE5ULeNCFBl1hRk74DM1t0pI2vE1Kv2YPUAB1wSb2DUZCGnZVX-e6B3cgDLn2ITXWa4gRL4KZASVB0nGPsw6o3Oefb4W_PN-IWZns6BZW97WTSNKt-UXgAnE0tBeUg5WJIwSBl1NSleUHRR-VERh2-E1Vg8hW9ePrsJ3clx0S1zxLCR41sAJP2c9ppxuJ5Nd5IliiV0rBfczpea4r3sKLfwgHxN1gUxW1hZ78epU20UCTidWst5SfKYVX5tVQIq_btd5soaYQku3-625d4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمریکا مجوز فروش نفت ایران را لغو کرد!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5911" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5910">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TD3w0KwmIypZh9GU7B8SxQc459qBK26dg46dSbxKRtAKd3WJaTIl90u6tiTF0TV6aPWaqFZ3jYQ-73JAMV6vY6x7hoEtFCTqhFu7raOsteY9o5dcb8j-OrRLzDJPqGDh7nRBsxwzDNFyxqIURzPhBqB7um4aEzdS93Q-Ns8ClDZvkxqqAPhL6en5a6-qWeBtFNNw2foRKRSj5jepU0Ax_UCaPBk4POeFes3FJSW9tB5jPnZV1F0sqALiPwvmqpRYSLGpJ-H_t3F9gd1Fx20xEAOqjBciqf7fCOByUpEElOU5EMNYY_sOOWphP06PNi-BpQEl3_rbxEun3koS3XCgdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد حمید  رسایی :)</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5910" target="_blank">📅 22:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5909">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند.
‏یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
‏ این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد»</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5909" target="_blank">📅 22:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5907">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oy55LMO6rwIo7hEEIKqUv6MdSnSF_e8kNJXgDBrft3_nlkxDj4s_CQUtSOE0f2sf1JQJF6SO1Pnshbh60tLZ8rVMF1LmVL7tagPg8mtKEYPT-MoHouvSbwcpwllsh_ecMLslhzs7tNWYZM0bleXI3Jxy2AesOmHekbdD-jG_FQkL_Az8wZOE51kYqJXy5BlH6iGmyJJVr-oRmM9Wr4sjiapq49p0sBtX1CNX3StqZAgThyiciTNuSlkXAfugZHJcS2BhA8QIanm174bXS2Fw6C7qjwKMuOmf1mdIfUqiAGFJi694bOKtjsN9sD9NEIxB5dkras00KokwKiX0UbDcyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GzGqhqRdVrVPs8yXWcIATTewy-w5PbL_tCxeQqJmkk_n3Wph0nnWfPlqoCyGw3PZZ-3lmUOCQII6gdQTfPzBwy8IC9-1jnRg5CWTR3ggTjuhhV26oCZ-e18ZpJUzjU6tFxKYzAaULYSVlgI9wqkP5ycCVBlBVaZq9WN6yqbyF44URQAedC33QlMvsV5ySsk7-CWIUzWsxjSNg5XhViWzru1cBboHGLvOdh30Hfq_LT_CuiBSXIVGpzUOSB4S_bpLNL_wrxmueq8p2P9IrM0NUBGWbsEu6W6Ab-CaUzkqezmr_JR3C-F20ZDl0tOjn-Z5r_9yTgodrdE1z7GtSZcaTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تا پارسال می‌نوشتن گنجایش مصلی ۶۵ هزار نمازگزاره، امسال نوشتن ۶ میلیون نفر  برای تشیع جنازه رفتن :)
به ریال می‌نویسید؟
خمینی گفته بود که برای حفظ اسلام
حتی دروغ گفتن حتی شرب خمر «واجبه» :)</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5907" target="_blank">📅 19:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5906">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FA9L46238aRHETCqewhOyzkXnsVQl1PdjXuKVMWRyjdhguZsj6rMuVUa1IoWcTEcXgy4zLyiZLO-919D2qLJOwid__M99Xyrp8BmYAmJmGY7gOSlANhO4r4m96iuuEBcVMejIf_-G-qnP1th_yG4xkKTjCm-9wAUS_lYROSYxBKo0mIgyCb1lD5QPjj6fwoe1E63fAfJOpeW8Lfeht6nRdjIvTKt17e1UojciFv3wJChnZBaGrjVmSfFhZ-kVsxyodm7c9zvKd6JZtdRVUO8fATtXlpjDeC0p9n4A39JP5tqtjomfQpxauJ8zwoVZQaFoPhjLo4VPxBfQRE97j_A5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=d8rjo_9C4aaKCoJBThwpBc7CgeQMmDfsheNfXse3x8LQW0yNAUWAC0rSsMYeBij3qIQETw-_nwaqUYwWzH4c537rMpzm9UzhrWjI3TNQOjBe5gcnBWd5CWs2X2pPL5sTgFxt88Gj5PGMQ8bMsAqHAUc1iFoZR_rtD5LbYeK6jXKGcd-kv2LQDRX1o1t9es5tWlRZYtlAGFTScQ0kJQNN6KBOtPTyaYd8nXu_BD-x0-MVIpche0pLGxibw7CEQEyYPJCDU0Q1l43QCCKUGFVxMMUEdHRARy4qvuIXndwOppMgmu4sFvt1qUuoOSX3rfk467FjQDkmUFZsMXd1txETvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=d8rjo_9C4aaKCoJBThwpBc7CgeQMmDfsheNfXse3x8LQW0yNAUWAC0rSsMYeBij3qIQETw-_nwaqUYwWzH4c537rMpzm9UzhrWjI3TNQOjBe5gcnBWd5CWs2X2pPL5sTgFxt88Gj5PGMQ8bMsAqHAUc1iFoZR_rtD5LbYeK6jXKGcd-kv2LQDRX1o1t9es5tWlRZYtlAGFTScQ0kJQNN6KBOtPTyaYd8nXu_BD-x0-MVIpche0pLGxibw7CEQEyYPJCDU0Q1l43QCCKUGFVxMMUEdHRARy4qvuIXndwOppMgmu4sFvt1qUuoOSX3rfk467FjQDkmUFZsMXd1txETvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک داستان ۴۷ ساله در ۲۴ ثانیه</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5905" target="_blank">📅 18:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5904">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
یک کشتی دیگر هم در تنگه هرمز مورد هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5904" target="_blank">📅 17:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5903">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skn_1eOfYMIdLWDCcJD5IaocqgszhYhDOgHpuPuCLGVfwCQptXjdSbl8IALEdS7UHhrK168KDvITv2BdWo9r34jjaW-PvGEAzsTEEWBJLZbish-jJ6F6eQzIf20cNiD1PIMVSxHPjQSwoCgSXQKT5u7Fl4EauH2mIDNOcTLC3LEuCxXIhAfk3iZnc7Ojq0XwlM13rZ-w-vjEYrLFnmKDFM1UV4ELtmsZybxUCR2ZzqiqzAjNXJv8wTArlbq3MtZkYVvIOlvFInh5elFbDvYbax6Ue38mnGbsc_nHfUKQJmNhD4gDTGGdmVrd-pipG0_h-4wVikOpcrn-YeQivd_oWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر:
«هدف قرار گرفتن کشتی قطری «الرقیات» هنگام عبور در نزدیکی تنگه هرمز، حمله‌ای غیرقابل‌قبول به امنیت و ایمنی کشتیرانی بین‌المللی، امنیت تأمین انرژی جهان، و نقضی جدی و آشکار از قوانین بین‌المللی است؛ به‌ویژه قواعدی که آزادی کشتیرانی و عبور امن از آبراه‌های بین‌المللی را تضمین می‌کنند.
ما از جمهوری اسلامی ایران می‌خواهیم فوراً تمام اقداماتی را که امنیت منطقه را تضعیف می‌کند یا ایمنی کشتیرانی بین‌المللی را به خطر می‌اندازد، متوقف کند و از به خطر انداختن تأمین انرژی جهان و منابع کشورهای منطقه در راستای منافع تنگ‌نظرانه خودداری کند.
ما جمهوری اسلامی ایران را از نظر حقوقی، به‌طور کامل، مسئول این حمله و هرگونه خسارت و پیامد ناشی از آن می‌دانیم.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5903" target="_blank">📅 17:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5902">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=doLArRbP30Iv4XBpvzxmvh5DqgpdhHv8d1iVU8Eb78aNsjXPhfXuRjrKNH0YPDJerBYPHJGTXyKZvIw7Q0gQT707PzPNjRzL2W4ljc7yCKpaNlGCg8qCcmMPRCxXrkhVYjn4tXkbmgGMv-skG5i5Q8nKVIrZgODtx-4RN7aWCvRFBmgtCiEVwJM7QcfaFsy2PIWFmcAukqfUHmb-mdoZO9dMGmxanotJSEfqOLOhAPzoSPnU3PkYwvx19fyTUBpQus8onl-30V4SR0HCj62MhIlc5vUrIQkndDgeXHznT4g7AxZ6i0exNaO01WgR2KBQHIOGRUEtb_oPUz5x-VP2oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=doLArRbP30Iv4XBpvzxmvh5DqgpdhHv8d1iVU8Eb78aNsjXPhfXuRjrKNH0YPDJerBYPHJGTXyKZvIw7Q0gQT707PzPNjRzL2W4ljc7yCKpaNlGCg8qCcmMPRCxXrkhVYjn4tXkbmgGMv-skG5i5Q8nKVIrZgODtx-4RN7aWCvRFBmgtCiEVwJM7QcfaFsy2PIWFmcAukqfUHmb-mdoZO9dMGmxanotJSEfqOLOhAPzoSPnU3PkYwvx19fyTUBpQus8onl-30V4SR0HCj62MhIlc5vUrIQkndDgeXHznT4g7AxZ6i0exNaO01WgR2KBQHIOGRUEtb_oPUz5x-VP2oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5902" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5901">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=H7rzhmLhzblRywmYs3qcIaXUXNld_I77w6nq9B8NGOaQDGqNfGC2A8mG7El_gVUlMdxqTIxPXIbOrn7pOS0PFDarZ6wN1f3jzOdj_8X0reghTAJLP8HLvKhbhcQE6_UjIWmoCgYsZpAWq3f4PQWgPc4ih8-T6Xi6UloPtg63hnFvs-Y5ePFybwgB_aRs7xtMJ0AHjE7Xb98sSmqT93_c1fsxL2XUcD4RV1fk-sfS9iNjWdw6M-hwzkCIymDiEPgoyxq6DDUSNPLKlIgkcpENZkvOcMFYG-ogKtKj517Xv4bZmYjvrMaFOYta7Vjc_FOXQJ7lWEQ0sFSQElBS8_7csQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=H7rzhmLhzblRywmYs3qcIaXUXNld_I77w6nq9B8NGOaQDGqNfGC2A8mG7El_gVUlMdxqTIxPXIbOrn7pOS0PFDarZ6wN1f3jzOdj_8X0reghTAJLP8HLvKhbhcQE6_UjIWmoCgYsZpAWq3f4PQWgPc4ih8-T6Xi6UloPtg63hnFvs-Y5ePFybwgB_aRs7xtMJ0AHjE7Xb98sSmqT93_c1fsxL2XUcD4RV1fk-sfS9iNjWdw6M-hwzkCIymDiEPgoyxq6DDUSNPLKlIgkcpENZkvOcMFYG-ogKtKj517Xv4bZmYjvrMaFOYta7Vjc_FOXQJ7lWEQ0sFSQElBS8_7csQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سالاد الویه و گریه آخوند</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5901" target="_blank">📅 15:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5900">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5900" target="_blank">📅 15:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5899">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkbF3f1Rp2TZ3hWurLybcO99ahVI6tEwscOE-aMbMWmLecq1YxYcuoXIJdQTR1gnQhj77qkASjHzLGdngMBz8dJ5BLbhG4_b6978ybWg2uACeDiLOq5-jPxSYCz5Hu6cZ-myC4Cu46drvlOM_ocHaKRIq5vg2lZ6mrLetPyW9hiRb6Ow_OD8yiVK2K830amHraox_ds9CNwt1Q4DZH9Y1yrly7rvYHGvOoSJrcv4D_QojZqDS6bVdpLm09YKw44_7eqiehzBqEG07rS4-huQW7-QkA9cifp1699mGHIekFLdKlsXcOce3JDi8YE8hQ7EqFHQOzvAkRCNytcY_qfIBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان شرکت کردند، از جمله رهبران ۶ کشور اسلامی! (برای خامنه‌ای، رهبران ۳ کشور اسلامی!)
برای مراسم رابین حسنی مبارک رییس جمهور مصر ، ملک حسین پادشاه اردن، زید شاکر نخست وزیر اردن، فیلالی نخست وزیر مراکش یاسر عرفات رهبر فلسطینی‌ها، حیدر علی‌اف از آذربایجان ‏و چیلر نخست وزیر ترکیه در این مراسم شرکت کردند.
🔴
برای مراسم یاسر عرفات هم ۱۷ تن از رهبران جهان شرکت کردند. از جمله رهبران کشورهای اندونزی، مصر، ترکیه، عربستان، پاکستان، الجزایر، سوریه، لبنان، یمن، آفریقای جنوبی، اردن و…
فرانسه، آلمان، بریتانیا، اسپانیا، هلند، نروژ، دانمارک، فنلاند، سوئیس، کانادا و چند کشور دیگر اغلب وزیر خارجه فرستادند.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5899" target="_blank">📅 15:21 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
