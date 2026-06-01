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
<img src="https://cdn4.telesco.pe/file/Jz4z5M8k1pk9wKee8DeZy6w8rwrMfuafvIx5P5GLcaMxqFN4IIJDst0u_RsQC1ZPWs59w065FZ4Bq2ZRMmoj2x-MqrYyw8i4t5jXeS1i2GOC2Ixt4lKY8aXFJe6WPKl7lKqjewdocHRaCDbSidb0FN6N-Um0G_Yn3kZWDK3dl9Q5IsrAXCeoEzCllELzaxMDixKQuzPblSQYZp82QXI1m6VZFD-BWvIyH4Yanh1qm8slSe1ORS4h6IC6jS_yu2eN87xuK7s6t8RcVzKRjllR-YtwdkiHmi6EtMR8c708VAu6_gXN4CdpasAN10jMJdcEthw6wB6pClRJbCem8PQdqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 13:09:42</div>
<hr>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=ofRC9OrhP8lB_2HR-rgwYj4qpv1CD4SMoNa4SdJYCRQ7CEbqrZ0A8Gq6vn7MJzEuYATVevKd7yT-hvfsBIMtetWllF_7YNtw2Ppx7cFWQ8y2uKXR_JxCoBNda7SkV_QAHGueA1-zyZXxPvqVtULruIghOBPrMSLf9qFcLBLxfxYVrQxBGj_NKNZix2CbIpvhZisKuDkgpF2-3x9VFOUEqQNp-4ZZ4N8LWFDCGbXPbLjuCATAaPut6lDeadHjn59qrGI47UfBwSDk9DMxQoXkNx8PU3FNwkRsP3f5qx4dqCGGSirBRCvosCHjhhBx2IuxGIlN7m6yo8zCNVkC7uNv_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=ofRC9OrhP8lB_2HR-rgwYj4qpv1CD4SMoNa4SdJYCRQ7CEbqrZ0A8Gq6vn7MJzEuYATVevKd7yT-hvfsBIMtetWllF_7YNtw2Ppx7cFWQ8y2uKXR_JxCoBNda7SkV_QAHGueA1-zyZXxPvqVtULruIghOBPrMSLf9qFcLBLxfxYVrQxBGj_NKNZix2CbIpvhZisKuDkgpF2-3x9VFOUEqQNp-4ZZ4N8LWFDCGbXPbLjuCATAaPut6lDeadHjn59qrGI47UfBwSDk9DMxQoXkNx8PU3FNwkRsP3f5qx4dqCGGSirBRCvosCHjhhBx2IuxGIlN7m6yo8zCNVkC7uNv_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال «پاریسن ژرمن» قهرمان شد و پاریس و فرانسه رو به آتش کشیدن
قیافه‌هاشون که تابلوئه!
توی یکی از ویدئوها شعار الله اکبر هم‌ میدن!!</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tu828bLFPXf7z-tcJe449HY559hg0RUwyXlDRmQ-BKy45KaQaUk6EBQr_W5eW9NtALOUsWc69dnBpQe0UiYTUQQOirzA3kn6fm_il65NeldEDSViolkUc3gJgJFX3cYDbnqvJVCe1sX2Oww1JOGdktPYzxnCVwABUXmO33q9BVKMLZwMdNfl0m2gDoFL9PauExbCuUt17gFfOukqoQwBNPyZ--3mcpdvW_vx_9K5-N-OFrF985HPARJ_jXaC8Yt5Yynb31ORw4EsnXwLVMZYDA0TO4iaJCo2_xV5MGvJzv03A2x096ukvjTe-K_0UCJBjipnlkyEE0HZqr57STgkUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش آمریکا رسما اعلام کرده
که چند حمله در دو روز اخیر به قشم
و گورک در نزدیکی اینکه هرمز انجام داده!</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farahmand_alipour/5230" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=YgbzeGn1qQ0o1qYU-Ke_qh4EOQXvlspelG8atwPESOS8o67qvVOwmXbjivXyNWuQ8q5S6mrbKS96DBKfKaZR9xC2161GZ1T46amFISPZfCZAeDK2AzoPrC9tXWfacPZ5mqYVq1AJe0CTGTnyPZRlJbJjFo0OvmbBwR6J35BipZBwNfi-Y7-haLpmnBjLuLSXMjSocZZotJjnu4TdyHzw1xx2t_YcdcCiLybIAWYcrdvGYX04F47u6YQDB8y4gNQ08X-s2de4P_2Wr8xNe0M7V8aCvZDEZmpObPtknHhTzxWjq3goCfwURvjA-3kD10tILarM3fC2rFzBvG24cLRQQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=YgbzeGn1qQ0o1qYU-Ke_qh4EOQXvlspelG8atwPESOS8o67qvVOwmXbjivXyNWuQ8q5S6mrbKS96DBKfKaZR9xC2161GZ1T46amFISPZfCZAeDK2AzoPrC9tXWfacPZ5mqYVq1AJe0CTGTnyPZRlJbJjFo0OvmbBwR6J35BipZBwNfi-Y7-haLpmnBjLuLSXMjSocZZotJjnu4TdyHzw1xx2t_YcdcCiLybIAWYcrdvGYX04F47u6YQDB8y4gNQ08X-s2de4P_2Wr8xNe0M7V8aCvZDEZmpObPtknHhTzxWjq3goCfwURvjA-3kD10tILarM3fC2rFzBvG24cLRQQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=LBNE1BoqZfrUT4bq7nDoHO6YuzfS5HOSqkXqiXzuFoNqoQSEpy96gP8VSJ8R-_OxbQ2ghl8POA83h1KK2e_5IssyIOP3obpDYbt8qfY289ucsd81xFOD0gyv8VHshy_-_ARZGLir3yJ-6uLWPlHK1aMH-XGNO3F7MmE7pPn3adZBU52FFQPO26P2upsjQ-OcLtj43IhVFsLKghGhXgCn7Pn3B0sBa_P0pHQUTW4MpF546a59x0svhkmCbym70axKAalBAF3TITYH6UHR-_ycs_gNZKIcI7O11nmWg_oOgHstQOHJ5pk9B41zkdf8Gn7ElfwylzssLqS79QMDstRB4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=LBNE1BoqZfrUT4bq7nDoHO6YuzfS5HOSqkXqiXzuFoNqoQSEpy96gP8VSJ8R-_OxbQ2ghl8POA83h1KK2e_5IssyIOP3obpDYbt8qfY289ucsd81xFOD0gyv8VHshy_-_ARZGLir3yJ-6uLWPlHK1aMH-XGNO3F7MmE7pPn3adZBU52FFQPO26P2upsjQ-OcLtj43IhVFsLKghGhXgCn7Pn3B0sBa_P0pHQUTW4MpF546a59x0svhkmCbym70axKAalBAF3TITYH6UHR-_ycs_gNZKIcI7O11nmWg_oOgHstQOHJ5pk9B41zkdf8Gn7ElfwylzssLqS79QMDstRB4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDt9Xz2ojJd3VEd6382cXrw2FqZdtGCX23CDSmAWq-pyVrvQ5gc0Z9P0u6gybZ2pf3vjurC-Pd7B5Yp0VdA2Bza0JzHfrJM5H_HeFxf7Ls3KrKimQkl-v5XcQaIqtMWon9C3HiTVREL6_OsD4CNovy7Gz2ycduzHJf-RrRsLEsfn6hhAO6ULlAvsSOXpfc3IJMsFfi_kP8AN-32oXggerhaQUR0Yld1Ezq-lz_OIZKADPNfrijJP7GzIUPNNEvXm9x3s5ORGYlrR62SneUdPRC57Y8w2SElnDcNJevLjldk92qgeMNrhbFN47iYoTbnygSdYdx2iAM1hJu7Ta5LE5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما
از دولت لبنان خواسته بودن
که برای آتش‌بس، مذاکره نکنه و…..!
به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره
(که بعد بگن دیدید، همون کشوری که به ما پول و اسلحه و….. میده، آتش‌بس رو هم آورد؟)
ولی الان می‌بینن جمهوری اسلامی توان چنین کاری رو نداره!
ترامپ اساسا داره لفتش میده و سرزمین‌های تحت کنترل حزب‌الله هم داره می‌افته دست اسرائیل پ یک میلیون نفرشون هم آواره شدن!</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farahmand_alipour/5227" target="_blank">📅 11:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5226">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.  به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.، مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!  یا شهر‌ نجف!  برخی…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/5226" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=urkoZdd6dU0ywLypBHalpTb1juRd5oefXk50CE7pJ4JHrFvqJxoQeEwWcFc7jv0kfcUUj-mnjh0f3BC07za7ZUZSW_shegh_Zm7hHKxkCRRUxyPdZv50l6NwC1uxAZ0O3O1--NzatBL97kVeY8NRkzgS8jAPS-QLOuJ6gRpmCQCfKbEn1LdO6kpjixQ7NgT3JzuD1w6FRrxxtI7NTQZRed58emJjQQAh2pJDPz5vcVWS5BjuGD8JktFjExQCCw6UFUwFm8TbOikzvugytNiLBw0Eu7tHxVI1nmPKwe5l-h8oLS1VHS-PkgDL947zuXsrHnDEORod1H-a8I-2WKtWuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=urkoZdd6dU0ywLypBHalpTb1juRd5oefXk50CE7pJ4JHrFvqJxoQeEwWcFc7jv0kfcUUj-mnjh0f3BC07za7ZUZSW_shegh_Zm7hHKxkCRRUxyPdZv50l6NwC1uxAZ0O3O1--NzatBL97kVeY8NRkzgS8jAPS-QLOuJ6gRpmCQCfKbEn1LdO6kpjixQ7NgT3JzuD1w6FRrxxtI7NTQZRed58emJjQQAh2pJDPz5vcVWS5BjuGD8JktFjExQCCw6UFUwFm8TbOikzvugytNiLBw0Eu7tHxVI1nmPKwe5l-h8oLS1VHS-PkgDL947zuXsrHnDEORod1H-a8I-2WKtWuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.
به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.،
مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!
یا شهر‌ نجف!
برخی از شهرها را اساسا به صورت شهرهای پادگانی عربی در وسط مناطق فارسی زبان و ایرانی ساختند،
پادگان شهرهایی چون : بصره و کوفه!
در قم اینقدر عرب ساکن کردند (از قبایل یمنی اشعری و از کوفه)  که برای چند قرن یک شهر با هویت عربی بود!
اصفهان اغلب یهودی بودند، یک شهر تجاری، عربها حتی بهش میگفتن دارالیهود
عربها شهر «جی» رو کنارش ساختند و اعراب رو ساکن اون کردن. تا نیمی از منطقه شهری اصفهان عرب باشه.
نیمی از قزوین، محلات عربی بود.
این حجم از استقرار قبایل عرب در قم، مرو، قزوین، اصفهان و… اغلب به خاطر قیام مردم در این شهرها علیه حکومت عربها و مسلمین بود. قیام های قم بسیار معروفه، اما اینقدر عرب ساکن قم کردند. که شهر برای قرن‌ها هویت عربی گرفت!</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/5225" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SI9CYUUbwLxx9LWIdoESF2vBjoDmQtNLiZIpccSjtP-YF5eGfUa3rX6W6G8tLmIAOUGREBArNTF5pYyDW-KKMnedia21jvt5EI5sZZZ51YKmFGutbYL1g4kthmxgVN7zQoyvTX2-qKwFucwANiqTMWd-KTcmivj9YiRChJuemsgql1_Tt70YBt32OIKYsJjlL-B-iP6NHGz4RG_frJw3_dg2HFWQR6uow5VqWf4c03DdMxsaVCMtzKQlLOHE_k9th7YmTDzt1vjb3AlWvBA3oVuSRkQrkuBCdI4tOLgGs7f1dIasw9eFgqU7UxAc8U0-FLcDJB7F1B6hEeNomMga6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطور تریتا پارسی در آمریکا
متوجه یک «طرح پنهانی» برخی نهادهای امنیتی در تهران شده؟!
معلومه یا این طرح رو خودش داده
یا با این نهادهای امنیتی رابطه داره!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5224" target="_blank">📅 02:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
مایک والتز سفیر آمریکا در سازمان ملل : جمهوری اسلامی با حمله به کشورهای عرب همسایه‌اش اشتباه بزرگی مرتکب شد و تاوان آن را خواهد پرداخت.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5223" target="_blank">📅 00:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqA0YJraytWtV6rAzmAWG58GdXEVQx1-Nr8ruktgtnljgq0zzjmJiffUgb7-gwV8yUZ9FH75MEneitnhqZ7sOQWlgyl5f8981oyifM8_dk_35Ww2Mk5IvNFsuuM6RgFvIeBSkEGHxkQXXZwQy7UCaXjtUtELMTvekkSNphqZ2CzxbndOP5przQERwjLT16alrZhV4yTcJEQtcaP2NSxEgmnF8X9uTMDSIwUIFrGT7XN1TcF-Ke1R6YP9HUd2ozpus_WjwEPnfz6_lTN5j0TVnKoDWWWdrMEtcjCYMgz0OaVdxWeWU4HF0LvC7iqPVXhFNE9IvdPNtoPYbrTxwghpyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌های ضد و‌ نقیض از استعفای پزشکیان از ریاست جمهوری</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5222" target="_blank">📅 00:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gpy1JM5fwzJjJGWrKp-Q7z92eGk3OSmukfPNypFYhNW58uf2uFFjxK29nvFRhTcMgLUkLvHL8-2VQQxAih9r1YlvpdC-tV-vRbfjcpyVFfZ5k0FMW2XHMgoeUATlHuy4cZFF3fpV9mE3WZjk4RLFcuWZkDdgZs89tWdofTOskqgzd4EXniSM0gh7y4mfrr3HAIzW0SYk6am2zKVRuvzO64OL4greRiK6s4U1JMeWgPPrknYux72PLhmzfxeiixN5n2HqrbBWPtehxBqEBKA1zT5dd-WN4AxKSKTF0DaNxn7YdmAmoVdU2FmDm0hbKkRxmffEupG6pTPY99Od0KpV_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KOhBBYuoneVwKMxHPANxiEjP9jaZktLo3vZxVazHcK9li-O7iOWaLWXxrJqLm5RrRKPdsGbDDQKAA2o1oopnghuovtXFKfG-D75OWqMvLk44ad893VN-yajEFXil3lnDBq0efQbhnjoncW8GdsrUKrehOXGR85Ag9kWaBW6Rz9rkuLde4a4-2_VndJpmryRWDl-B5w_AQVH8xy1Rklj_K1XB-fn_lAQVN8AXD82WeMbRMkLaCrmS_wP6rBocpr3uHxCDZInbG7YgwPiB9sXb1CXxcQyGu1_5f9z1-Bamv74t5R3Kk9IPaP6p1dP3iEp9jtbnxTs6sRDwGU972mTBfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VdYHPuhZq-3_DC_K-fsLWy3y76dHzSe5aNTIfxQbxU_n5OTn2RVL9_3zsUY2lCljEnNKlHWSez2ATNo5N6XPWtRT4WWbcVbscW5mFiO_KUbbncrX0VP0ApMPLsmuAXFk7yU52bD4aeXAXBUwx9CZxbx_OmAcj8qmk8J2KFrtZ7yLzFhHVt_WUtrJxmXICM_zJ6pzDv1O6blQbU0wp_prl1iWI4VJmGHNx95NyTWwC7rA15wjeNMSss5hVv-9paHWl95xMR377-boNzoLDDhZKmTuU23ASoyodtVegyjBFeDztmL7n4C36colcu2LxYVA2-su1FsSntayau6lNVQL9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتون رفته میخواستید برید
پشت سر خامنه‌ای در قدس نماز بخونید؟
که شما تاریخ خوندید نه؟
تاریخ جمال عبدالناصر و صدام و قذافی و بشار اسد رو لابد خونده بودید
که همین هوس‌ها رو داشتن!!!
و به همین نتایج هم رسیدن!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5219" target="_blank">📅 18:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5216">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b0siclmglcX21YxQDq0gz6PxSoDcpuHH9r8Mp9tbejNHBY8bPJxhPFO7F2Zlxg_X6XOFPu13MApuMMIXuwrrgtwZKPoRTYNCjg0MBdB4t6bYctWy9n-hkM5BjpT9B-7PrhXvMyqXt69kdFCFzUTcDsiXUdnTkAQ6WyB-fjutBuMvt_9T0t_Yv7eJiej40IeEH5ERtHn0cTFgH1bNunG1zvcjLHo3fQkwWMDI0xtUIu8NUk_LuIX5vvoItS53POF9fJn_qPKr3HPuwHYhU9drmSNJEhgNwOJGaoccgMmtxXB1QQxspiqqKwkNTBTQGJ6uyn7_TCjpecJ85uKcq39yqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nsRdiJ0pik7_sIxIw_8yaxBf0w-Jw7HU3updWbujd6NyztnsBNCl528m4pOpWIRB5HgbraDjqMRh6uuuP0gcVDW7f_IAagHZFjqhlKTNGYWpI-hnOdWf2_erxi_krgRqlrDjeAYcqM4He4xlBXSKSBFINb3V9auSuTt1mfC9ZGG0-0-dYkyM5P-DB8alG_MEeyXyeTV46Iv4R_3oadY3WzdTzRc4yMJliJ7vaAhah1PhEOzjqZrECmM2fKsjZYaO1b99auH1_WEtIK0Su_lv-Z_SLgzAsd4jYD4f5NHa0bBDxgAPIvELLjbj3huSAE_RJW_fAlpUltH1pUyo1AeXSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N6V9GavrQG6nzumLG598vdI7ibpWJCv5Hy11Ay0hguuQYQnM3ag9FTrzv5UuCU_G6_qhn-8RuXR9q4xf931OFOKiCsfdSr_WiYT9nf_IFGI7p6xJv3L8l0YkN-VB-8_wyrmJchSsA12fN2nwLJzzDD-ih3bOP8x0G9n9Wh2y_Kv3_WefEJ43Ov8FMLhSeF_jWsZSXCY-wFnoAHzVyDb0kDYvMfxeZ9EgIwoLYaoo0iQarrfKeJiWpc4id5vm9ZzACkFC3U2Eill9w2kjTH3P-Y43yV95C85thC3nUMVVojxIuPEiP6ONyvaijVwnlUyKGE29zJ0jsuMfQILPEL3QUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=q1zaCiCLK184XTAMOTnnm88m3eRKWFjXSS721j98HBGiQijyR1wAq3gfwBkQt0b0t2uBohP_wInAAoJAG-3sjAiVEYEGUOVa0Box78ysQeN9jlaGFafMHfoOuUeJZhyVzdGvzBT2PoL5obJE3M14x2QjESQtdANcMXbo97HGg0qoLU3ODxvZ5SnT6m4oUitLHS-Pb6TIEcCK2rpsxN_sOzXIlsD4Th8DWSvvBMzT9vtdeNzFkGNKPhdvitUkLVdMXCoH3g30tHfCe84u7XuD0zqpr-HssNDXevV32RL-bNaJTmWigtQOpHHW4HWS9sDTyu7NYsIvhnKG0QNkySmX7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=q1zaCiCLK184XTAMOTnnm88m3eRKWFjXSS721j98HBGiQijyR1wAq3gfwBkQt0b0t2uBohP_wInAAoJAG-3sjAiVEYEGUOVa0Box78ysQeN9jlaGFafMHfoOuUeJZhyVzdGvzBT2PoL5obJE3M14x2QjESQtdANcMXbo97HGg0qoLU3ODxvZ5SnT6m4oUitLHS-Pb6TIEcCK2rpsxN_sOzXIlsD4Th8DWSvvBMzT9vtdeNzFkGNKPhdvitUkLVdMXCoH3g30tHfCe84u7XuD0zqpr-HssNDXevV32RL-bNaJTmWigtQOpHHW4HWS9sDTyu7NYsIvhnKG0QNkySmX7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=EOdOSg05Yi5cZxi2gwHUr_1IXJFEqy1bJUTkxkgfTtqbLRj6uKXKzOei_vdKwY7AEX8YnJGF6HryUtqfJhjHs-mSC9hfU2Cg1hqPyfMr8CY_IYojtKy-nDsxVX_UiHLgIav9zK8gLz0G0oBDMLPmHBPLeBNiW665UNlxrXq7RtKyYraiSp4rMHXU5s1phltN--euve1lUb142br9Mc98qGARZD80HFK4c6p9st0rxLYgNtk-2a_q_wPLhRmltGTBOkY7Q7aZhA7WHLX3sbfVF6U_vDkClgViXtrbt54oO9jE5sd4w6cU3FAP0SQgEDLAYomVdyI-Y_0uOApN6GowoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=EOdOSg05Yi5cZxi2gwHUr_1IXJFEqy1bJUTkxkgfTtqbLRj6uKXKzOei_vdKwY7AEX8YnJGF6HryUtqfJhjHs-mSC9hfU2Cg1hqPyfMr8CY_IYojtKy-nDsxVX_UiHLgIav9zK8gLz0G0oBDMLPmHBPLeBNiW665UNlxrXq7RtKyYraiSp4rMHXU5s1phltN--euve1lUb142br9Mc98qGARZD80HFK4c6p9st0rxLYgNtk-2a_q_wPLhRmltGTBOkY7Q7aZhA7WHLX3sbfVF6U_vDkClgViXtrbt54oO9jE5sd4w6cU3FAP0SQgEDLAYomVdyI-Y_0uOApN6GowoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=XaGLMaH7Y33Ip_hysDM-olVUUcT8Y3rz43ETnqwlZxxVO8-EYTJ4aCfSdKh6R6CIRZ2QTPKEBCRJzCDYj8qkOiHDDJ6XGzO3QL5FvEJL-9wAwGQ5RDZ_1TEIzC9kkvJ6JENn2-Yd0ua1hu_QmQWLpz4tz9uHDpTmc1Hs2aeqCO9qTeYNwmZSzXq2DAqtJCygV2pmJUY2sVnCBAhx0SQIn4a-MJGiTcYCWaljo5cih6Vfl8N3eoqgrvtq1yqPJfGkd9Fn56SnxBWyEQfwAO9PmnrKgpxGNE4FPhkjHsDISguAQO01zLF8xAkEziuhIf29MeGPL2xnqF8deHRDXTjCYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=XaGLMaH7Y33Ip_hysDM-olVUUcT8Y3rz43ETnqwlZxxVO8-EYTJ4aCfSdKh6R6CIRZ2QTPKEBCRJzCDYj8qkOiHDDJ6XGzO3QL5FvEJL-9wAwGQ5RDZ_1TEIzC9kkvJ6JENn2-Yd0ua1hu_QmQWLpz4tz9uHDpTmc1Hs2aeqCO9qTeYNwmZSzXq2DAqtJCygV2pmJUY2sVnCBAhx0SQIn4a-MJGiTcYCWaljo5cih6Vfl8N3eoqgrvtq1yqPJfGkd9Fn56SnxBWyEQfwAO9PmnrKgpxGNE4FPhkjHsDISguAQO01zLF8xAkEziuhIf29MeGPL2xnqF8deHRDXTjCYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7hEb1Ixi08niB3wUx3nUshwrLU6Dig8Ppg2KZdrTHIytZ7fAoNCNo2oH4eKJJJZYJ90AjPbqMX1vLrtxaWCC5tA6am7bOq7NqI1eGiRgJyT2rM7zomxz3abH5d_OtAilUIsGJiNYm2ITDnpge2s8HjSDDKPoxzRc4owzGHjOHK9tQbYNyTerkNCO4L1XDEYJQD9fR9XuYoaoKf6BCkBGL77XM2WtjAEqcOwV9NBMCbkyEzjPsochity-OFvTpCxdtcOUBxrH4xVb_MVqKl0qeAsGO_fIj9eCwNjMXLsp64ZOal9OuqvNCR9CN2WTnbAnwJBstEt4Ai1hjdTlFT-rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات و دعوا سر اینهاست!
خوش به حال آخوند که چون شمایانی رو داره! هر بلایی که سرتون ببره، آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی و کره‌شمالی رو نمی‌رفتید! راه
صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5212" target="_blank">📅 17:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmKdX7iAAV_0FbKT80yAN7DArHTlFDRi2T7Si355aHREG03VFU6YTttO3tgxQa4A30MvuBPVqNWFLoY-cD8zfNSrw1wYSuMG2wI45ND5qrlReDh_gGJoGh2I65w5V20q1bCOoR_VmMm1ER5GW_Cz8fNjUTXCNgx7NLBsgfecrMysgv408tvMLERo51bVS51lJEdIwLWOManVCa6Xf-JCX5KFu7Kwxd3c-uqqtV7Wu1tMCc8xMEbIeydTCCkT2a6FNFsaueQShwzSn8sdrRJdiezxEF4eob7HU7JHonWozfdjoR32dBdaEJf1Q31pmbC8eF9zXCt5rmxwDrlG6U2udQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ  ۴۰ روزه به خاطر ایران اینترنشال بود و‌ دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های
ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های
جمهوری اسلامی  و ۴۷ سال آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات
هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات سر اینهاست!
خوش به حال  آخوند که چون شمایانی رو داره!
هر بلایی که سرتون ببره،
آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی
و کره شمالی رو نمی‌رفتید! راه صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5211" target="_blank">📅 17:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmIvLdkJtJ-H4ashSsXFRPIF2CkWhQsvVcP72lPeieY88PM3NITPXi_o5ftMjwS0DAEThjv4hrDjv7-mBOIPN6xOENUH2SIVs5LRnBb2y510ZDXWul07shbE8j7h_46PJUWbZdC7NlKcKNGjiVqq9YsynGehqkp2LjVyzukxyu9P9fmE5sefN60AVu2SUx38mq6O-JzeKJIqZxAVxpIIyR4Z8DloYWRAuSn4W6z84JtzUZtf832B8MpJXLHq87KBTooL4t61EtXtSC9-weuyK6Bz1I5go74PyCH4oUO4P71WgyPftKVlHwvmmb0R8srtWUl4-gpXBbdiKLrMaIka3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6IeE3iUF-ZlvDuyW8DSK-ttAOOvfYfH7R4uXWtJCXQE5ybF98yLUnV6O8cWKvtCr8zKATCSZ0tqwfGr_8z4w4VVoNErJr3ARYdueS5T3-9hZhnLMdk1kzxvuii2_VJsizv0x_RHii5ZK-F2tNpZdg2w_fbf3n2DjCBlmoKFz4G40Q7uik6J9EstOMtA-SvHrY3Y1gYQimJ-3nBFm8BbhXFQ-NUrxrxsP8WxelVUk48CQ-6cI8vncpELFMBarZRnENU4aFfaa33AGaG_mbPt2E3ji59QxWhGYI8F5xWseiOxbkcIe3eO4jjzg5tfFGcK_7R9WzWKdtNOaOQssByZDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل قلعه شقیق در جنوب لبنان
را تصرف کرد، این مهم‌ترین پیشروی ارتش اسرائیل در جنوب لبنان از سال ۲۰۰۰ میلادی است!
گروه تروریستی حزب‌الله لبنان،
بدون اجازه گرفتن از دولت و مجلس و ارتش لبنان و در خونخواهی خامنه‌ای،
به اسرائیل حمله کردند، اسرائیل نیز در پاسخ دست به حمله گسترده به مناطق شیعه‌نشین لبنان زد، بیش از دو ماه است که حدود یک میلیون شیعه لبنانی آواره شده‌اند! بیش از سه هزار تن کشته شدند!
چند هفته پیش دولت لبنان قصد مداخله داشت و تلاش برای «آتش‌بس» اما این گروه تروریستی و حامیانش مخالفت کردند و گفتند که جمهوری اسلامی باید این آتش‌بس را برای ما بیاورد!
(که بعد تبلیغ کنن قدرت ج‌ا بود)
جمهوری اسلامی نیز توقف در جنگ لبنان را در صدر خواسته‌های خود از دولت ترامپ قرار داده ولی هنوز به تفاهم با آمریکا نرسیده و اسرائیل هم داره کار رو ادامه میده!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5209" target="_blank">📅 12:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=dXJWdwYAE3GBEvQj7DFlBl4Qi5w2Kyp8khCEqrmW1SqKVYQM7SRU24yWRkJ5E6Vsy7-dus85wUA4LYCAZDHpDNxK9_OeXvr6-fXMkX1vVVFzRdyKWdOr907lFTRLLpYsKJtEfM6gygndhIzXVoINptThsZual7ALgup0N8R7QrWcPrwas2iZHix9z5_txW1k0WgJfPGN2XHGMF7HxtonOAohrXGVcwArh5nx9KszG3cjKTiP6cmCZuGg-_Q0jz6oIHfLF7PuPyyOXzW3Pi0-ij9qaguaC-34OT1dvj5bNIbDFkCcGqZNod2zngAkPpoaP9Jj4weXCjXqw8Fcrnnefw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=dXJWdwYAE3GBEvQj7DFlBl4Qi5w2Kyp8khCEqrmW1SqKVYQM7SRU24yWRkJ5E6Vsy7-dus85wUA4LYCAZDHpDNxK9_OeXvr6-fXMkX1vVVFzRdyKWdOr907lFTRLLpYsKJtEfM6gygndhIzXVoINptThsZual7ALgup0N8R7QrWcPrwas2iZHix9z5_txW1k0WgJfPGN2XHGMF7HxtonOAohrXGVcwArh5nx9KszG3cjKTiP6cmCZuGg-_Q0jz6oIHfLF7PuPyyOXzW3Pi0-ij9qaguaC-34OT1dvj5bNIbDFkCcGqZNod2zngAkPpoaP9Jj4weXCjXqw8Fcrnnefw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، ۱۸ دی در جریان اعتراضات شهر قدس بازداشت و پس از ۶۰ روز پیکرش تحویل خانواده داده شد.
امیرمحمد ۱۸ دی‌ در اعتراضات ناپدید شد. خانواده‌اش به بیمارستان‌ها، سردخانه‌ها و پزشکی قانونی مراجعه کردند، اما هیچ اثری از او نیافتنند.
پس از دو روز و در ۲۰ دی، تلفن همراهش روشن شد و ماموران حکومتی از این طریق به خانواده اعلام کردند که امیرمحمد زنده است.
خانواده پس از این خبر، پیگیری‌های بیشتری در دادگستری انجام دادند و آنجا نیز به آنها اطمینان داده شد که پسرشان زنده است و حتی برایش حکم صادر شده است.
امیرمحمد دانش‌آموز مقطع هشتم بود و خانواده تلاش کرد از طریق آموزش و پرورش نیز این موضوع را پیگیری کند، اما در آنجا نیز با پاسخ‌هایی مبهم و با برچسب «پرونده محرمانه» روبه‌رو شد.
این بلاتکلیفی و بی‌خبری تا ۶۰ روز ادامه داشت؛ تا اینکه در نهایت پزشکی قانونی با خانواده تماس گرفت و اعلام کرد پیکر امیرمحمد شناسایی شده است.
پیکر این نوجوان با کد «ناشناس ۱۱۷۵۴» به خانواده تحویل داده شد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5208" target="_blank">📅 10:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=PZmA0qixw3GXghrdp2s000s7a6LSVAqQUa3ldb31z5FMDSO3EDpsyiwc76x11s5kVRoMjxbR5RDhPwspb2ssgu3Cq-w-0Q2d1Ne70Y982JLBrN8rdh5B5Eh0fm4C1dM6oblpXWaNIaix2Wg3oVzcRa_eVLb_BkVJyXh2qTlwXtwxSVSTnjep5JuJIaMtOKYpmFB-KIqBguNMugCvByApIo5r_QGZA35M7Km8-wUDOOESvnILvS_bD-SNFFbHTWGIPDRzwrPjUGifpViqSstLDYwZhDeaWkiTJ0RrL-K39ZP4lApWf94WItct6jLNdgR_xe8ceOK4Nbs8_kd6w58N4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=PZmA0qixw3GXghrdp2s000s7a6LSVAqQUa3ldb31z5FMDSO3EDpsyiwc76x11s5kVRoMjxbR5RDhPwspb2ssgu3Cq-w-0Q2d1Ne70Y982JLBrN8rdh5B5Eh0fm4C1dM6oblpXWaNIaix2Wg3oVzcRa_eVLb_BkVJyXh2qTlwXtwxSVSTnjep5JuJIaMtOKYpmFB-KIqBguNMugCvByApIo5r_QGZA35M7Km8-wUDOOESvnILvS_bD-SNFFbHTWGIPDRzwrPjUGifpViqSstLDYwZhDeaWkiTJ0RrL-K39ZP4lApWf94WItct6jLNdgR_xe8ceOK4Nbs8_kd6w58N4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dV0c4EBFhVP6XOk3yur43wwWIGhcJN1gYdZoWJQ2y68yewcTpdysN92BWIQr6NFCCQfjqIzeJJ7ycEW2VawDFMsKFo5MFMx1Q6Vgxh12y5AuT2MWYzNbAXBy_MRbheteZLjo2bzZ5xn98A5FhfTuqAZcuPs1xlQje5kxWfl1OOssZrfMX9piKuzXnzfFdXQH-OrjQu1fdX5Xl0T2A7QF-76eh2S3SwK6FnbCfFTHkWUv_MkYSP7RSlUgamk0r3-wuX8F7ayJHsOi2wvTAT00NJXUv7Te9ai0NlumRJLHCt1urVTbsg0XGik81eHXC4-vaL6SB6VdhKffuSZA5cS4TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی با آب و تاب می‌گفت
به امارات حمله موشکی و پهپادی کرده،
حملاتی که ۹۵ درصدشون توسط
سیستم دفاعی امارات خنثی میشدن!
اما امارات در عوض پنهانی با جنگنده‌هاش
حمله می‌کرد و جمهوری اسلامی هیچ سیستم تدافعی نداشت!
یعنی اگه به ایران ۱۰۰ جنگنده، یا ۱۰۰ موشک حمله می‌کرد، میشه با اطمینان گفت ۹۹٪ ماموریتشون
رو انجام میدادن و اهدافشون رو میزدن!
کما اینکه اسرائیل ۸۵۰۰ سورتی پرواز در آسمان ایران انجام داد حتی یک هواپیماش آسیبی ندید.
آمریکا هم ۱۳ هزار سورتی پرواز انجام داد.
آمریکا همچنین ۱۰۰۰ موشک تاهاماک به ایران شلیک کرد، جمهوری اسلامی قادر نبود حتی جلوی یکی از اونها رو بگیره! یک در هزار رو هم‌ نتونست!
جنگ با امارات رو جمهوری اسلامی کلید زد
و هنوز هم کامل مشخص نشده چه آسیب‌هایی
ایران در این جنگ متحمل شده!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5206" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfITlRtSvEC1OTDiV05ti9nTfEYIO9cYxBjfQwRK3riRC94lDbYdwsYofNbbXMiCSj3uQw21iP0d3Ae49X3tANRTh59CIbr8F9mKM2ntMTgckdMBfeljAmFPvuzbas3ZiY-15yCcaPexG2ZusPMui8dd3EKpi1k5As6v7rKXcCy2LpWHxDmNrDRqfqL8E_6jT9jy5c_sVSOfNL1O822V418o8HjXFXXSE5z1nVw5oaRe73oaIJyTa1YXr_HMdsA-oaozHUoMC9U0s6_mnsqGQ_TJMKn2apRR-aF8ylvknOidlkVTV4x8H3yna-bpb-33rW_VOf2tU1-dSvL6s3J02A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPefUQjf6dMVaMYOgNpf5jDdMLcodSZ2JCiYCIE15Wg5FNpZnjA0cujPR0iTuk7Rd2UKEhXWWa0xe3hgtnka1GRcnw9DGstrKvj8A77POlxnoipGb8148zwagScf16oXPOqkT5KcsYpKV-lBCHdMXvTAMs5VRuBjns7Z-IUOhgJ0FJVheE1UIaTvbqWmQzRtCHhpXQhxB4j5LK1iZLb3S6HdYyYilf3HyQTkOczIaCiJJIyNu5HNo1kOg5Kdf_lvCFFfYVNJEutjBo1jXcfSvZH77TuDhOfzD5T0HWNJxF0MnRCL6BVt3nGeCM8PqLMx997dcInAWhNQEfvW5cdFSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i65N0pdqWbbB4Qswk9nzx-u7KzlhvwgKTK2Pmwyu1i9u65RX0U94FhFkiQU0dTs7UJhglgJ8uanya_pD0IyNkZVZlsFcFldN-G6dmEtq_Wf3aaPXXcjbY3z6sjW3lMGFV6ZpReow92FnMxPVkhoU0fnawt6S96DqBLDJxH2VpI1EEOryskVwvUgUOM6KiKpNtL9-gWhbYnZ81OsYEHzWqPU8LuqLT3ee8ZBCHjG9wbrVIPzFmUg0ZKTyWDtTtD_9gT7AyExHKe_g6B6QxeMuRozkSKeTpYCN_Ng_zwBUDT_nNag8567g9c7_qxVrbFsz9dDCmZKjORwO90B0R1JpUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : برای اتخاذ تصمیم نهایی اکنون به اتاق وضعیت می‌روم.
«ایران باید موافقت کند که هرگز به سلاح یا بمب هسته‌ای دست نخواهد یافت.
تنگه هرمز باید فوراً باز شود؛ بدون دریافت هیچ‌گونه عوارض یا هزینه‌ای، و رفت‌وآمد کشتی‌ها در هر دو جهت به‌صورت آزاد و بدون محدودیت انجام گیرد.
تمام مین‌های دریایی (بمب‌ها)، در صورت وجود، باید از بین برده شوند. ما با استفاده از تجهیزات پیشرفته مین‌روب زیرآبی خود، تعداد زیادی از این مین‌ها را از طریق انفجار نابود کرده‌ایم. ایران نیز باید فوراً هر مین باقی‌مانده را جمع‌آوری یا منفجر کند؛ البته تعداد آن‌ها زیاد نخواهد بود.
کشتی‌هایی که به دلیل محاصره دریایی بی‌سابقه و فوق‌العاده ما در تنگه متوقف شده‌اند ــ محاصره‌ای که اکنون لغو خواهد شد ــ می‌توانند روند بازگشت به خانه را آغاز کنند!
از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدر و مادرها و خانواده‌هایتان سلام برسانید!
مواد غنی‌شده‌ای که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین دفن شده‌اند ــ زیر کوه‌هایی که تقریباً در نتیجه حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فروریخته‌اند ــ توسط ایالات متحده از زیر زمین بیرون آورده خواهند شد. (طبق توافق، تنها آمریکا و چین توانایی فنی انجام چنین کاری را دارند.)
این عملیات با هماهنگی نزدیک جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام خواهد شد و این مواد به طور کامل نابود خواهند شد.
تا اطلاع ثانوی هیچ پولی میان طرف‌ها رد و بدل نخواهد شد.
در مورد سایر موضوعات ــ که اهمیت بسیار کمتری دارند ــ نیز توافق حاصل شده است.
اکنون برای اتخاذ تصمیم نهایی به اتاق وضعیت می‌روم.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5201" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UwCR13FZhHPFtlxmUcZH6eyoEzfQrtJvVzMPUBiQ75YyLfOccJkSMEx-qcpwfxyyaWpN5QujQNSm-6OF-GXlzHCpf4AuH6AP9upgoR4OQLFyHucdISNvSO3m9Bo3nJrNpYPcDZvI6IY5AXCbsVVZAt3pRjdoZJxXn2LOTnkZsCx6Cj0zMWxLxCZiBU4ZzyOdEgdhyK-T7CDSKR5TrSZtVpo2kj3m9EncdODcshjmXaWGN6kThuS7bHzA-VlaS8ECXXyYKDUt7LU2ll4nGkW8UwSskF6JInOhX2diRjVJTH9SWoO5sRnYlkZ_WaoQCw-yANJYP7-QnlOuUIxnt874PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lAKTJPDiafaKnYoN7YnL10engjsurQoCoCU9V2qfSCzNGLRMwdRJBlvg-g2hO7SacUETqrb-9snDJzKesRNnd0Tl5oGJvohK0U5f9Fs1Rzi3iC6bkMlBmYU4earX1sxXfPQ0wEsU4hJ7lZn-L1kur4a0szSw6OroeMjg5F75GhKXmk6kFKVyxc5kjQqg_KHxj0v_e_t1IWxvXTAy7LKvl0ySUVdP6e9gdE-AebUnKMJknPcUdsrUFbfKefgVmzwIN521K0Dzm80T2pIVjj2iKu4AIFjuuSRWoNy6QNwnBqHrR-UdeifmAVyHpg9eF871N4VCXIZ7cCdNKiql9xKw0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
لبنان سفیر جمهوری اسلامی رو اخراج کرد!
گفت «عنصر نامطلوبه»! گفت که جمهوری اسلامی عامل وقوع جنگ در لبنان شده و جنگ
رو به مردم لبنان تحمیل کرده.
اما سفیر جمهوری اسلامی در درون سفارت خانه موند و گفت برنمیگردم ایران!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hhc1aWzUQRJdfj0-WfndOfmYzVmt147o45tLgLB08jclml1NZc7zHAJhLehiOiFaetT2SJhbtLKZV8C8mw2NkM8nS0qoAINOR_vVaqRns4Xl76Q26cLyZxdmtLox-tKzOdyCfgJSnhPIqq9_mTHjuBrF_f2uiSsI5LtCZb9b3hFAcAC0cnheaJxtpuX66aD5aUlLcCTobjJu9tNNdRbpvY68OoBQLog_9tRb7SwYWqKAsCkDWN7sX3KgD5bMAlXC0ex71RYlOI_4HDmGDJ_U7Jn2A98CLzf3fnad28w_UgMitCuDT_Rgc19EEiw4UOoevy4JWwv2mcDD7KZP-fLZ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MnHZqH8kHoVhlOyux2pUf7o4P90jkzwRgRfYtcU2M0slRhfVuGJAFAo9q-KMBxYIoHnzIGFJd_kE8FMD8lPl4qxsM1FB26wCSrl-fN9tFPqDR-Fwr_oDknhRoiPhjPhnIGB4Alyt-9JvmefZuhaQfHBTHOyusPY6nKWvBEdJ8XLaeqhLDu7C-1y9MR4V1Wb4HoYoGXYDaoCL209tXqKDW1PzFgvGWJkI3Xlh9ARbSwVMar2UsAFcwn1AyqNiWDF7J_y_iOzRV0ZqkoN1aVhYmb5bil_AQuGFzonsPzRwT3lf8PgA7JfzGKzv4oqfISGcwyThanwUym_c9ql2xY0WMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
درسته هر شب توی خیابون‌ها بزن و برقص و عروسی داشتن اما در افغانستان گدایی پول میکردن :)
سفارت جمهوری اسلامی در کابل در اواخر اسفندماه رسما تقاضا کرد که  مردم افغانستان به جمهوری اسلامی کمک مالی کنن!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=rw_h1iSPEkjuL4YAU3Dn8tmvkwFjfo1UIj5ley8w4Ci92ckgxvMUJOKW7sG2r2io6xMXVNNUvlqOnIh8zF5hY9HIuaXlPAgYLyt0MkG2rlKkRYyBhNq-xU429tyef25Q4f0e-DjbtHK0NA-LlToHstYfVtypDgdSiTpFd-I5SBQPYXjzahiAYACnJ2tuu1vGaNuc9bx5gVe5PiXvIJsYRyICu-w9f2nbmKnBvWLeor-v1TiOTv_8eQfwz7eNklESKGyIG-QtOR1Fyo_quHTrC3bpz2BLZxLSaVh02Lkelv9043Qg9vlartC2LmNYsWPLZFYexH2FfzhqxH7rlq_a1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=rw_h1iSPEkjuL4YAU3Dn8tmvkwFjfo1UIj5ley8w4Ci92ckgxvMUJOKW7sG2r2io6xMXVNNUvlqOnIh8zF5hY9HIuaXlPAgYLyt0MkG2rlKkRYyBhNq-xU429tyef25Q4f0e-DjbtHK0NA-LlToHstYfVtypDgdSiTpFd-I5SBQPYXjzahiAYACnJ2tuu1vGaNuc9bx5gVe5PiXvIJsYRyICu-w9f2nbmKnBvWLeor-v1TiOTv_8eQfwz7eNklESKGyIG-QtOR1Fyo_quHTrC3bpz2BLZxLSaVh02Lkelv9043Qg9vlartC2LmNYsWPLZFYexH2FfzhqxH7rlq_a1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=IYLFtWAIr0_nQgxd8k1K7aqRxx_p6YcfrlGHeFAhNGfgEPthLAWOmEQATPrxvy3omDV3i-LkF7n1BxEq4MaZWVAto7SVDuYfKdkis0wWoZApJ-9MNBMNau14ibSmUnGxT5HNK8EmFC60CPQdcIAAy4QVLyT0ieBiCOQbK097z9A02g_seLo1vfLaX49SIkbT2OdO5RkgQFY4RiSnx-4xe5qHKe2lsPW9HM-Irmm2rXrQ8U-KZbXmwYJA59oBngh1bCZ5-Mjpdv4gkG4CJAZVyK950OnXztgpOrO4sc3CRCqrE2PVsUvBpLzDF4SWCnezGmEcDX16eNO_MFIL24IB-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=IYLFtWAIr0_nQgxd8k1K7aqRxx_p6YcfrlGHeFAhNGfgEPthLAWOmEQATPrxvy3omDV3i-LkF7n1BxEq4MaZWVAto7SVDuYfKdkis0wWoZApJ-9MNBMNau14ibSmUnGxT5HNK8EmFC60CPQdcIAAy4QVLyT0ieBiCOQbK097z9A02g_seLo1vfLaX49SIkbT2OdO5RkgQFY4RiSnx-4xe5qHKe2lsPW9HM-Irmm2rXrQ8U-KZbXmwYJA59oBngh1bCZ5-Mjpdv4gkG4CJAZVyK950OnXztgpOrO4sc3CRCqrE2PVsUvBpLzDF4SWCnezGmEcDX16eNO_MFIL24IB-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید
در اجتماعات حکومتی شون
هر شب عروسی داشتن!
«صیغه یک ماهه»! در برابر «یک سکه» :)
با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tr7osKa49ntlM860nlE6oWc5mqyFoTYauRXOPVOTfAP1PCHbeSyRQymeTjRCidJFSxPAR17vyF5ndKVB00bncPnnKp8NSm5TnQTVHhtlPQVzV5pUiET4sy-JgLzBVM0RtBDGpq9t5P6HiIUJWE5Vj9zfAijtBqtg0emZl_19kt8LxDzVsudnQqaP5QPoQ2o9DU74R1E8yLanYH6n99JdJgBxg2qEcD7KHykuSHkBQcYUG4PJlob41bV2KLB8L5JtTFFJBlrxTb2NCm22izDz6H1r6aH8SrH6cGlWPx36AfnuI_puNgeGxPx5A7FeK60F-tyI4ML7ESFVTVf0yl1Mfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NeOketDOBTGePO8kU5tNhlt5Nb0Ouo0DsV5NS_r6xtQKcwhIWt6BnF5MMmuBjYPmwzsN7ViglN75QnyoUoQHj9Jc6QP2FPNQVVPFgJRE-VJYI6VfZDobW4fKHKB3Ym0LcbRtJKblLJpb-hu6g-wvx3QBMcPQYS48OWIPzd5rGsLh3aKNQ4JGAThAi2kTLg-urB23dmndnovk0j6oyTEiDjoyyiVyd63I7edoXDafhfMAgHjfXWuYi0pIBrUxEpf9tLThRPHYqNBg5lMxdbmbD1MbRpxYpHDtbA1YVHtgIjlSBRhra1bs8cBPaQXtDZh33K8atCeEbqQcxRI_EYNCHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،
پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!
حتی زودتر از پیام‌ شهردار تهران!
حتی زودتر از پیام جوادی آملی :)
پوتین در پیامش نوشته بود :
«اطمینان دارم شما راه پدرتان
را با افتخار ادامه خواهید داد.»
پوتین راه پدر مجتبی خامنه‌ای رو دوست داره :)</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5192" target="_blank">📅 12:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=jjmyjMJLz2DBO24S5AmJ8Y0najuDV1d-_pVYXDwRa12a_eLTwX1hTUi_L2o0FEw3Q7Dz3OnaxRb1gH63nvacTcLb2ZqfaWlNIQRLmzNpbSIMi2ENpYSL0aPnOYzB8ZWciU2AtEos_nrVT8VPoQDTwMURjX81OosdE1lG3mm0dlPZmaFX5u-xq5MuPSoMaMGUsCP8_N3FkaCP9Xbeqhp8ImdNZ4BouQL8yKFpvSOvcAw2HAzDQ8NzZ9-KAFqJ9ouAXSh7uzB89uV6WKljFVDC-mVM5XExsH1BxIhg4uRnuXg6houb5c982F884baHyc41ejAAN1WT_SeYP0FNHHmWZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=jjmyjMJLz2DBO24S5AmJ8Y0najuDV1d-_pVYXDwRa12a_eLTwX1hTUi_L2o0FEw3Q7Dz3OnaxRb1gH63nvacTcLb2ZqfaWlNIQRLmzNpbSIMi2ENpYSL0aPnOYzB8ZWciU2AtEos_nrVT8VPoQDTwMURjX81OosdE1lG3mm0dlPZmaFX5u-xq5MuPSoMaMGUsCP8_N3FkaCP9Xbeqhp8ImdNZ4BouQL8yKFpvSOvcAw2HAzDQ8NzZ9-KAFqJ9ouAXSh7uzB89uV6WKljFVDC-mVM5XExsH1BxIhg4uRnuXg6houb5c982F884baHyc41ejAAN1WT_SeYP0FNHHmWZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ount6vYY2poy69g3wZKcXM2ftOQ4v7dzlP1JupD8b-VJIEs6JQ-V2bxJTusHnwEPuXbqHVMvSxKKk2gvf6AhVIzecMnABcwG5U9TKte7UKxbidi5mY4q-H033OIhZe8yGciwwUxZT_eqjoxUEYTMimhCWgPbUZjIr7_MUjtqm8tdvDX9F3-elfxV2vjaOYpAcaxOXW6kXFmzNAcr359lJt-MTeAcjqW7bDpuKbwDm4_aV4yLIooDP_EofiIu1p1Y3i9GhUywqmyM6XXdDnpZoQAO4dc9IMG7NniniJFp475uWUA01njd91rCZQPDNWNoTulYJUfos5pdPSjb_7XlQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نکته جالب :)  امروز ۲۶ روز پس از کشته شدن خامنه‌ای  در کره شمالی هنوز خبر کشته شدن خامنه‌ای منتشر نشده!  فقط اعلام شد که مجتبی خامنه‌ای،  پسرش جایگزین او شده،  اما اعلام نشده که در طی یک حمله نظامی  خامنه‌ای کشته‌ شده.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5190" target="_blank">📅 11:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏حالا که تشریف آوردید:
‏از ۵۷ کشور اسلامی، فقط ۸ دولت کشته شدن «ولی امر مسلمین» رو تسلیت گفتن و ۴۹ کشور سکوت کردن!
‏عراق، آذربایجان، تاجیکستان، پاکستان، لبنان، الجزایر، عمان و قطر تنها کشورهایی بودند که تسلیت گفتند.
‏بزرگان جهان اسلام چون‌: ترکیه، عربستان، اندونزی، مصر، مالزی،ازبکستان و… سکوت کردن!
‏تروریست‌های طالبان هم حمله رو محکوم کردن اما تسلیت نگفتن!
دولت فلسطین حتی حمله رو هم‌ محکوم نکرد! سکوت کامل!
فقط تروریست‌های حماس محکوم کردن و تسلیت گفتن!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5189" target="_blank">📅 11:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
امروز : کشته شدن ۱۴ نیر‌وی سپاه زنجان بر اثر انفجار مهمات عمل‌نکرده</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5188" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5187">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های جمهوری اسلامی  از بستن تنگه هرمز خبر می‌دهند.
🚨
🚨
🚨
سخنگوی قرارگاه خاتم : به ۱۴ پایگاه نظامی آمریکا حمله کردیم و «صدها» ‌تن آمریکایی و اسرائیلی را کشته‌ایم.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5187" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5186">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پایکوبی مردم در تهران</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5186" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔺
شادی مردم ایران از شنیدن  خبر مرگ خامنه‌ای
🔺
بیانیه رسمی دولت اسرائیل تا دقایقی دیگر</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5185" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">حمله به بحرین
😅</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5184" target="_blank">📅 10:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">شاهکار جدید صدا و سیما  اینها رو باید تلوزیون‌های جهان در بخش سرگرمی نشون بدن</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5183" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5182">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">«دیشب مردم تهران در کوچه و خیابان  کل می‌کشیدن» مرسی از بابت این اعتراف و این مستند سازی از وضعیت تهران پس از انتشار خبر مرگ خامنه‌ای</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5182" target="_blank">📅 09:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5181">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=DuxJQxW6rzlw-OM-WiJ43a11y7YCScQa8luTOtRnoHWpGQf_--kYj6qeLdAu0xrO6LP8dnGRFqxxmXK3RKkarazoHDhHIkXEX3hHJ5MWNB8kioUMdJ-71DjjCBA3T1_Fr_Rz0UP4kpk7mmNeu8dvX--fjHxQzPLqSHDNu96pKFcOE0CmZSECY2eiuvyZd8kd6Yn7HZ2nctMzSR82MJG8RuLLX_yYLEscnT86IHGMb-hsYN6dQt_VOC3dEK29wYntpEGk8mkNHrVytVnKt431Kr2i9252puESo616iCLkI4eUXmqdxLjRwmRAr1Gikn_EHkrsy6roHmr9XDMNV-SSag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=DuxJQxW6rzlw-OM-WiJ43a11y7YCScQa8luTOtRnoHWpGQf_--kYj6qeLdAu0xrO6LP8dnGRFqxxmXK3RKkarazoHDhHIkXEX3hHJ5MWNB8kioUMdJ-71DjjCBA3T1_Fr_Rz0UP4kpk7mmNeu8dvX--fjHxQzPLqSHDNu96pKFcOE0CmZSECY2eiuvyZd8kd6Yn7HZ2nctMzSR82MJG8RuLLX_yYLEscnT86IHGMb-hsYN6dQt_VOC3dEK29wYntpEGk8mkNHrVytVnKt431Kr2i9252puESo616iCLkI4eUXmqdxLjRwmRAr1Gikn_EHkrsy6roHmr9XDMNV-SSag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس پاکستان داره عزاداران خامنه‌ای رو با چوب میزنه  دیروز هم پلیس پاکستان ۶ تاشون رو کشت.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5181" target="_blank">📅 09:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5180">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بخش خبری ساعت ۱۴ شبکه یک و تکرار ادعای زدن ۳ جنگنده آمریکایی  در آسمان کویت و تکرار این سوال که چطور در آسمان ایران به این پهناوری نمی‌تونید ‌، در آسمان کویت تونستید؟؟</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5180" target="_blank">📅 09:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">فرماندار جم در استان بوشهر، می‌گوید که یک «پهپاد متخاصم» منهدم شده و وضعیت شهر به حالت عادی بازگشته است.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5179" target="_blank">📅 00:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از شلیک موشک از منطقه جم بوشهر به سمت چند کشتی که در تلاش برای عبور از تنگه هرمز بودند.
گفته می‌شود در جریان این حملات موشکی که از سوی سپاه صورت گرفته، به سوی یک کشتی آمریکایی نیز شلیک شده.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5178" target="_blank">📅 23:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5177">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=fV5T7TzeWMBm_4kcR5ZRqlAKcQm6VTeaQJ0oIKZVc_IHHOIKvvAbkcoFSV7PneCVF9Ffxq61Y9rCj2ArbMp1vzJRJrNeURm-87hT5_mddUzIZX6MFlkdZ3BUPHzORQbhDihXy0UPmPaYZil7voqQdCtRT_p4ACsxlteCmjz6vAYcAQQR9g50U7QpI4YOf1JOMa8y14GTmFijz2TAWYjz1kYCDS3yaX0GWpgDG6UmM8fYnkwFKObndH_X_NhBTA_-v4QN2qtd6rwzhaqhO0pjDvhiZeX1OHISS_O7HlyYeNmHlegivyX0za6USdLvkIDDgn5dcW11psExzfhQ9sT_vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=fV5T7TzeWMBm_4kcR5ZRqlAKcQm6VTeaQJ0oIKZVc_IHHOIKvvAbkcoFSV7PneCVF9Ffxq61Y9rCj2ArbMp1vzJRJrNeURm-87hT5_mddUzIZX6MFlkdZ3BUPHzORQbhDihXy0UPmPaYZil7voqQdCtRT_p4ACsxlteCmjz6vAYcAQQR9g50U7QpI4YOf1JOMa8y14GTmFijz2TAWYjz1kYCDS3yaX0GWpgDG6UmM8fYnkwFKObndH_X_NhBTA_-v4QN2qtd6rwzhaqhO0pjDvhiZeX1OHISS_O7HlyYeNmHlegivyX0za6USdLvkIDDgn5dcW11psExzfhQ9sT_vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف رهبر شهیدش رو پاره کردن :)</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5177" target="_blank">📅 20:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=P49EhqLzdaKhTttsIQRz8IM1uz7PPHGZ8YI1NcTRYflRLD-hJMAVE5ZL3mR5zr78G6IeL2pSbokImCtvUxupHd8dSRkuUS_0fPOkvC319vGRfGF0O1Nj_iWfePdgm3BeNcO-bA3qGxI_vl1wLBRtENyBtjX8g66tj2aD6Op3KOREtWsPFachymHDl5BeatC_EKUQ2XJHeYl8OPsFCF2GLad124T75O8Pt9uY3nYOnkRWlQybzyP3o7Xm7J9-qtHCgj-a9kBVGXGCWNonWwthCR2h8YZYswnQfDV4yiHMSzwf88BiaLE9Vwx9629sKL8yNmJXgzJDWTlWRGpiL_AW5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=P49EhqLzdaKhTttsIQRz8IM1uz7PPHGZ8YI1NcTRYflRLD-hJMAVE5ZL3mR5zr78G6IeL2pSbokImCtvUxupHd8dSRkuUS_0fPOkvC319vGRfGF0O1Nj_iWfePdgm3BeNcO-bA3qGxI_vl1wLBRtENyBtjX8g66tj2aD6Op3KOREtWsPFachymHDl5BeatC_EKUQ2XJHeYl8OPsFCF2GLad124T75O8Pt9uY3nYOnkRWlQybzyP3o7Xm7J9-qtHCgj-a9kBVGXGCWNonWwthCR2h8YZYswnQfDV4yiHMSzwf88BiaLE9Vwx9629sKL8yNmJXgzJDWTlWRGpiL_AW5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از ۹۰ روز صدا و‌سیمای جمهوری اسلامی می‌پرسه در حمله به بیت کیا کشته شدن؟
کمیل خجسته، برادرزاده منصوره خجسته باقرزاده، همسر علی خامنه‌ای، میگه  افراد خانواده خامنه‌ای که کشته شدند، همه در یک نقطه نبودن! در جاهای متفاوتی از منطقه بیت رهبری بودن که به همه اون جاها حمله شده.
این همون حمله‌ای است که پسر عبدالرحیم موسوی ،
رئیس ستاد کل نیروهای مسلح میگه ؛ ۳۰ روز گشتم و جسد رو پیدا نکردیم!
عجیبه در این حمله فقط مجتبی سالم مونده باشه!!
چرا خامنه‌ای در پناهگاه نبود
!؟</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5176" target="_blank">📅 19:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
آمریکا و جمهوری اسلامی به یک توافق ۶۰ روزه رسیده‌اند تا آتش‌بس را تمدید کنند و مذاکرات درباره برنامه هسته‌ای را آغاز کنند.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5175" target="_blank">📅 19:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/208f980645.mp4?token=uc0iTTfm_5ItExsueCVEjcpbXoGKfiPphIAtydNbn7XWo7vRRU7H3qimJD2s5KJthLqTL5QOTawW9-sih2Sq667LrJRr4_baYFLwlNs3F-_zQNOtPiIjOaZZserWn0B5qHwsWGd3nEbevYfMxnnfzVFNOqaDG_EcF6GjFeMhKVM1ZGg_UA-a9s_DNscWUMHP_-KMa4t2DWggoZsHcD2rnRB9zvJeUiu7EaOKLQLjbO7C-fIwwZFGofSqjy7mSEYyXd78BBEOIaILOoCBfHSJqWLv4mxsYsl6R5oA4OhuCi3RVzeeI95dLOKE3h1pI3ak4e9VbbtW7vuEl5v2DObuMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/208f980645.mp4?token=uc0iTTfm_5ItExsueCVEjcpbXoGKfiPphIAtydNbn7XWo7vRRU7H3qimJD2s5KJthLqTL5QOTawW9-sih2Sq667LrJRr4_baYFLwlNs3F-_zQNOtPiIjOaZZserWn0B5qHwsWGd3nEbevYfMxnnfzVFNOqaDG_EcF6GjFeMhKVM1ZGg_UA-a9s_DNscWUMHP_-KMa4t2DWggoZsHcD2rnRB9zvJeUiu7EaOKLQLjbO7C-fIwwZFGofSqjy7mSEYyXd78BBEOIaILOoCBfHSJqWLv4mxsYsl6R5oA4OhuCi3RVzeeI95dLOKE3h1pI3ak4e9VbbtW7vuEl5v2DObuMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش زدن ظریف :)
نوبت عراقچی هم میرسه!
این مسیر رو خیلی‌ها رفتن!
از منتظری و بنی‌صدر، تا موسوی،
خاتمی و روحانی، احمدی‌نژاد و…..</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5174" target="_blank">📅 19:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=ZnkdGmZCcyX1zFNys1AdKe7zrYUUyNz_YKz38AU4FpuNEmRCfJ2OO47FL8BlVP5JI1Bjsp2eZlDxH0VgGq-_WBgYK-lNbQQ9NqVdLbwi5ybJzmzU11DLNFNnZZh-tCK4mctKrA2B4sx_S9Dcp5V1UIamkv88-q2Ww6BO9zAWEy-FELP_OeXso7YuZb8yvgyYC6qzitOp_tKScnszjgiyxOYFQvfGUxyBBswmngo1hKO_mMThcxqbq_nhJwdynbwq92tvCukD5kJLTEUVSMvIx4dBKpj4aqLZWumo1HP61RjD320t2JscfgErU-OpMlVgL0vnq2JZpIMA-LUlVD0XXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=ZnkdGmZCcyX1zFNys1AdKe7zrYUUyNz_YKz38AU4FpuNEmRCfJ2OO47FL8BlVP5JI1Bjsp2eZlDxH0VgGq-_WBgYK-lNbQQ9NqVdLbwi5ybJzmzU11DLNFNnZZh-tCK4mctKrA2B4sx_S9Dcp5V1UIamkv88-q2Ww6BO9zAWEy-FELP_OeXso7YuZb8yvgyYC6qzitOp_tKScnszjgiyxOYFQvfGUxyBBswmngo1hKO_mMThcxqbq_nhJwdynbwq92tvCukD5kJLTEUVSMvIx4dBKpj4aqLZWumo1HP61RjD320t2JscfgErU-OpMlVgL0vnq2JZpIMA-LUlVD0XXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک مرد مسلمان چاقو به دست در محوطه یک ایستگاه قطار در سوئیس موجب زخمی شدن ۴ تن شد.
او با فریاد الله اکبر دست به این اقدام تروریستی زد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5173" target="_blank">📅 14:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=bRxiSiR0cOsLimIt8Id9MxLNxzO8oYPvf8RhXtxrN5DNjcNWL8OHcfQ43WBQ93fXdU-3o0wo0Q_7WFd0P2Wc1IL4Wg4gblZI1TcH8GjFrrEHBtBzlzgkdyNJbvzzURjRAVelgloYPBiTQRdlD72K3LejYWG0ZzmmBq1m1kAx44-17qqwwQBC5F3ft6696GslqW8Snm6TIQclCsXVOCX5-KlMCMsp-xXO5DpmeMk3hCEj_pgg1FqA-2aApT52Qry7YSBXO_5hbS4rTwCJMc485WvegM3RYt3ehSl2NhScoxvR2Kr6I-qU00yoibIwob_9RpFRl2N5ZjnxWRTsUj--bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=bRxiSiR0cOsLimIt8Id9MxLNxzO8oYPvf8RhXtxrN5DNjcNWL8OHcfQ43WBQ93fXdU-3o0wo0Q_7WFd0P2Wc1IL4Wg4gblZI1TcH8GjFrrEHBtBzlzgkdyNJbvzzURjRAVelgloYPBiTQRdlD72K3LejYWG0ZzmmBq1m1kAx44-17qqwwQBC5F3ft6696GslqW8Snm6TIQclCsXVOCX5-KlMCMsp-xXO5DpmeMk3hCEj_pgg1FqA-2aApT52Qry7YSBXO_5hbS4rTwCJMc485WvegM3RYt3ehSl2NhScoxvR2Kr6I-qU00yoibIwob_9RpFRl2N5ZjnxWRTsUj--bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله هوایی اسرائیل به بیروت
🔺
آمریکا از دولت اسرائیل خواسته بود تا به بیروت حمله نکند
🔺
گفته می‌شود که در جریان این حمله، «علی الحسینی» مسئول ارشد موشکی حزب‌الله لبنان، که در واقع یک عراقی است از «فرقه الامام حسین» از گروه‌های نیابتی جمهوری اسلامی در عراق، کشته شد.
🔺
اسرائیل دیروز هم در حمله‌ای به غزه، فرمانده تازه منصوب شده برای «گردان‌های قسام» (نیروهای نظامی گروه تروریستی حماس) را حذف کرد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5172" target="_blank">📅 14:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">علی الحسینی‌ از فرماندهان ارشد و مسئول واحد موشکی «فرقة الإمام الحسین» حز‌ب‌الله عراق در حملات امروز اسراییل به لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5171" target="_blank">📅 14:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZmHJQwpa4VtERz6NeGCXjGU5zx3XD2cwwRAUsNrSVQJKiiOUQDHpZccHNg3zLoGLNXjprLBNK7-3UIzeGZcERVJ3iTeQff6T9E0Ye1LJ5LxMwEsEEF_dYkSgMNM0zkjfL7WeHwWDycbCv9hdYe7vmLL9TzTrSXtUv7r0NeGvLZYA-sKAHhXIcf3SKXzSb3azQu1WCN3yOXTlxGnrzrbGSmz2r6ibqTXjZWPSm-NXOXoIA29bG0qj1kkJ7YwQNkv9Sb6hFT9OfISdHpXYmOi1pvM9C7F723iMYGOi1uhpunmIW7-7tr54v7QyKevOig6Jll1cgUi1aF1B5PbT9Yo7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام:
ساعت ۱۰:۱۷ شب به وقت شرقی آمریکا [۵:۴۷ صبح ایران] روز ۲۷ مه،
ایران یک موشک بالستیک به سمت کویت شلیک کرد که توسط نیروهای کویتی با موفقیت رهگیری و منهدم شد. این
نقض فاحش آتش‌بس
توسط رژیم ایران، چند ساعت پس از آن رخ داد که نیروهای ایرانی پنج پهپاد انتحاری را به پرواز درآوردند که تهدیدی جدی در تنگه هرمز و اطراف آن ایجاد کرده بودند.
همه پهپادها توسط نیروهای آمریکایی با موفقیت رهگیری شدند.
نیروهای آمریکایی همچنین از شلیک پهپاد ششم از یک مرکز کنترل زمینی ایرانی در بندرعباس جلوگیری کردند.
فرماندهی مرکزی ایالات متحده و شرکای منطقه‌ای همچنان هوشیار و با تدبیر عمل می‌کنند و به دفاع از نیروهای خود و منافع‌مان در برابر تجاوزات بی‌توجیه ایران ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5170" target="_blank">📅 14:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=eSkjZ9rIUeQZdJhE0ZnGmMSmO45DEfT1jTt6DENkavMEqkpBzJ879Tp7ndhurQnOXTIFFRIJsO-r0dTPsogzC9wir_BiOtoTGdTHnDAtWvwYsDEtxPZs8-EkUwBYyoagKq_qff3Nrx0GQbaI_F-Q4EXZoDKiISIXFn6wI0xQ1ckHjsJ0tuHtL4c6daJcS9902RaUedJLY_CphGWrRsqLZGWLTcr4VgQu1Md98LmKqc5UMXPVADAWTguA4bXWu46pJgMJ_BU2MBJvioYQPIOgxulCvOMeYEHnhX69Vm4PkQenYl9yqbYBndopjYevxNmi_v4iGUaFKL7VZfBEFUtorw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=eSkjZ9rIUeQZdJhE0ZnGmMSmO45DEfT1jTt6DENkavMEqkpBzJ879Tp7ndhurQnOXTIFFRIJsO-r0dTPsogzC9wir_BiOtoTGdTHnDAtWvwYsDEtxPZs8-EkUwBYyoagKq_qff3Nrx0GQbaI_F-Q4EXZoDKiISIXFn6wI0xQ1ckHjsJ0tuHtL4c6daJcS9902RaUedJLY_CphGWrRsqLZGWLTcr4VgQu1Md98LmKqc5UMXPVADAWTguA4bXWu46pJgMJ_BU2MBJvioYQPIOgxulCvOMeYEHnhX69Vm4PkQenYl9yqbYBndopjYevxNmi_v4iGUaFKL7VZfBEFUtorw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلام یک دوره کوتاه از رشد علمی داشت،  که همیشه هم سنگش رو به سینه میزنن،  ولی حتی اسمش هم گویای همه چیزه!  «نهضت ترجمه!» رفتن شروع کردن به «خوندن» کتابهای دیگران!  کتابهای ایران باستان و یونان باستان و هند و روم و……  خوندن و ترجمه کردن و شدن باسواد !  اونهم…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5169" target="_blank">📅 10:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8iVVgrD4dqWs_K_-Ko3lEcNIBXIgSgkn0Ajr_-XYcUIdh_UlrRLEECHhoxyQzqowaXd3hPe2X8X5Ru9n_7VJJCc3A6UGgaaYjuBs3L0kKBMJ858c4yj0YYhS1LRJttz-94KqxzjLv3EBteQ_BJiAr-03-haweTA8kc9fchT38hRZRST-Jt3ZJbcW3cT0b367m3ykeZKwgf5j9L6Z78Vsg2QxC3nTLu75ZkHdN5QnswgPlY6L10NDBoR959LSQ6vP6EGqLIpvExfTEKaqUPDZMEnw9KjIYqiYiJSoHHGu0souBkE5iFmtYBwZGwSnJNwlKdB4ksdYff6dfr5u9xUaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !  جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،  انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5168" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5167">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=fPhb3me5UVroM3GjYX925R2mjs6EWQxwvhFMC7p6EkWhbtjsYY_D0VGKhzz5Kz7QmWPhlRSs9V6vbkH-VihUXJ661fRFOqI71pqUo8OjauKUZ0J9kPUgUVWEPP41YDDJHdJwM6XnnEIJnJRZyv-5h8xTNPeGjRZeX5Z3F8iwQLQxcnk84bPK3A-dq0Wjb6R50gZOsd1tBLrPQITx6vLTq6Pjvuq46RnPXsZc3TGmKzcZyODvubyutPTmYPkQSTBbAbUhje0BLGCsAPBO5YApnqpT2TVhWsuobLIrQF3KhJ1JGVrGLgTUrd_VGrWBjKnQz0e0b7iMdW6cmEnlIk8dLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=fPhb3me5UVroM3GjYX925R2mjs6EWQxwvhFMC7p6EkWhbtjsYY_D0VGKhzz5Kz7QmWPhlRSs9V6vbkH-VihUXJ661fRFOqI71pqUo8OjauKUZ0J9kPUgUVWEPP41YDDJHdJwM6XnnEIJnJRZyv-5h8xTNPeGjRZeX5Z3F8iwQLQxcnk84bPK3A-dq0Wjb6R50gZOsd1tBLrPQITx6vLTq6Pjvuq46RnPXsZc3TGmKzcZyODvubyutPTmYPkQSTBbAbUhje0BLGCsAPBO5YApnqpT2TVhWsuobLIrQF3KhJ1JGVrGLgTUrd_VGrWBjKnQz0e0b7iMdW6cmEnlIk8dLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !
جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،
انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره و مفهوم «شهروند»، دادگاه و وکیل و حقوق مدنی، پزشکی و بیمارستان مدرن، بروکراسی اداری، مفهوم حقوق فردی، مفهوم و ارزش آزادی بیان، مفهوم دولت و ملت، سرشماری و شناسنامه و داشتن فامیلی و..
صد مورد دیگه!
مسلمان‌ها در دنیای جدید چی داشتن؟ هیچی!
هیچی!! لباس سنتی بپوشیم بریم توی خیابون هاشون نماز بخونیم و بگیم خدای ما از خدای شما بزرگ‌تره!
با نخوت بگیم ما خیلی از شما بهتریم!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5167" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5166">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
سحرگاه امروز ارتش آمریکا به ‌منطقه‌ای در اطراف فرودگاه بندرعباس حمله کرد.
سپاه نیز در اطلاعیه‌ای اعلام کرده که در پاسخ به حمله آمریکا ، پایگاه هوایی مبدا این حمله را مورد هدف و حمله ‌قرار داده.
بیانیه سپاه اشاره‌ای به محل این پایگاه هوایی آمریکایی نکرده.
اما خبرهایی از فعالیت مقابله پدافند هوایی کویت در برابر حمله پهپادی منتشر شده.
🔺
برخی رسانه های حکومتی نوشته‌اند که یک نفتکش آمریکایی قصد عبور از تنگه هرمز داشت که مورد حمله سپاه قرار گرفت و در واکنش ارتش آمریکا دست به حمله‌ به اطراف فرودگاه بندرعباس زد که ظاهرا مبدا حملات بود،</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5166" target="_blank">📅 08:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5165">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ  به PBS News: «جمهوری اسلامی غنی‌سازی را کنار خواهد گذاشت و «هیچ» تحریمی هم برداشته نخواهد شد. هیچ خبری از لغو تحریم‌ها نیست. »</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5165" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMiGmReWj_L3he7H4G2fNn_tQ8Qw01akq1i64ZdnG_C0AaEO_ix6pVNNERfg9QvvtzKsXSNhjVbh_YwUtNmBIjCPkMuZCi3auAio4Uay_nAhcbYPVfC1EiTBoTAJ0UiJwI572pNds6E7BnulMwimKb2hrJSBTziNrURcIT3QWKZirW8yYIlBIt6hUnw4Z7bm7Rw19Lu8Yuf2-VHrNT1zFJvIFD6R_qTG7njFov2d8Op8IO5tr7uuag-syvkvfjrXWl2_ognWCg7ybAIgMj2YjXqPL9Umq42epaWON5wVSWMVU1vANlFPmY9LJFxhnVc1Hnq-WKImaFosnT-Dba4NJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۳۵۳ سن  حداقلی ازدواج برای دختران ایرانی از ۱۵ سال به ۱۸ سال ارتقا یافت.
جمهوری اسلامی اما سن حداقلی رو
به ۱۳ سال رسوند تا کودک همسری کاملا قانونی بشه! جمهوری اسلامی اما ازدواج زیر ۱۳ سال برای دختران رو هم مجوز میده.
فقط باید دور زده بشه، اول صیغه جاری بشه
بعد برن دادگاه و قانونی اش کنن! به همین سادگی!
در بهار ۱۴۰۰ ، حدود ۱۰ هزار دختر ۱۰ تا ۱۴ ساله در ایران شوهر داده شدند!</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5164" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUVMWjnZ2JT-eHlBvtGuW_zyKargUcFJgbOH4oKJVBY3174j-iWEfWhO7mSipFnnawDT3s6nwNl3hwIbnkR3VvJFBOQG74zi5_Lw--ze_mlS5C-pqJd-_4d2R6l9r-m1WM586f1aD1rhCgWUxutAgn6sWBtQIUOYROv0d6feaFWsSQDigMrWYx2AukPkcqpR-TgZ7bw4yE3GBnh0-FCovnWoyWigfKqUkWC7RIp0mAQdORUoKrGnZH7vl3cu2ICc7LKCsxBeDrqg-oP_fk9LF8AULspJQ1uaxtptfZNH_4d2YN2qmJty9kTaPI0ji2ngVVu2grHvKc7-lfWHqLoTKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5163" target="_blank">📅 11:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xgv6AGtpiKQCM6zf4lcQVqYYk3Z6r_gqt2f8GIRDnnDcBr1N-vsF-CRY1WqSdhMGwaVxyc9leF8Rk9xUI4nafO5_mPF3SmXpY9rG9-zAqAL9cSHL1M4vPrC0Gj3gx_iRcK4Z9iwhFuVjIVbZSdRAHoOxgHW8tErlVfM-yfq4VKyUA7KyxovKVHKPN-84JCmczxkmFkeMnh6iFzn5mhqS3w-IX_ivP31tnRINedWR4PwO9YmYLpjMeTRpYAPWpPbxZhWRzb5ieUvHp7sBgZ_pGFsGijBI4SblnaxdLtmYXXXGLVwPmTmoLViOL8CoSzzhPh1MwrKfxBinwVz5AkYR-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه هم که فکر می‌کرد زرنگی کرده و با حاتم بخشی از خاک چکسلواکی، کشورش را از ورود به یک جنگ رها کرده، هزینه بسیار سنگینی پرداخت!  به قیمت تصرف پاریس به دست آلمان نازی!  آلمانی‌ها دقیقا با سلاح‌هایی که  از کارخانه‌های عظیم نظامی چکسلواکی  به دست آورده بودند،…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5162" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0by8P4NUcWVwLXA-w98WpRwhKeVjPQCP5wTyOwQYQRAy9c3ZJP-DpsE3jzEEMqKTlZizPQA_RHt9YDgQZmkQXYvexbtD_saowSGOGIhNiy2gGCXb0aissUogn0vCIUo1EtnuMLafeBk_RpoBUcvgI966ka0iq_wuZRX23zLOvtpMV4xj13W4tgtz37OXOVZ5HVrZcGtPRR07Wy7rZMSiL2Fm5Oxf1SLnL3i5Y97SfB4h-7d3h0uVpUciG2BYwgGErOobbFXsW0vKzGURw4XArrV_52yLMW1jKvXYXzqglcRlvrbh7o4C-4X1tZEyCM5180ptyxoltlaCBnNZm5gpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرچیل اون موقع نماینده مجلس بود.  دولت چمبریل رو سرزنش کرد و گفت :  «به شما حق انتخاب میان جنگ و ننگ داده شد. شما ننگ را انتخاب کردید،  و با این حال جنگ هم خواهید داشت.»  پیش بینی چرچیل خیلی سریع به واقعیت پیوست! آلمان این مناطق چکسلواکی را گرفت اما دقیقا…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5161" target="_blank">📅 10:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uagrWWM8jCsU7f_ItBG0gkZWvXVQJj8cV7jUeYSzoAOPILlUqie4NF9QBQviaCrwEWHuc9y7KknJlFLtm72tzHSVaxE4RzmJEDcEl47ftfpvPq_YRWvr_GJZTtLssGPlxBdUjn1ySentG4WgaMy29fuI-Pqyl_jka2H1QZi5ezbxVzO_01MvBBSay_BU0J_yX3qU0-g70HYo9PdFJegH_5mM1G2rbEDQ_Mv18PQ546LH7TFCqeexHvosxfVM7uiCKmWeMmgmZwLD9u9JC1UvUdz3L7bLtTjdwiYvaz8cOIh1obSpJfNSOOyUZou6arIxomVQc1xHESe6hY5mfrWPYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمبرلین، در صدر دولت بریتانیا،  به همراهی فرانسه، قراردادی را امضا کرده بودند که بر اساس آن، ۳۰٪ از خاک چکسلواکی به آلمان نازی داده می‌شد.  مناطقی که مردم آن آلمانی زبان بودند.  هیتلر میخواست همه مناطق آلمانی‌زبان در آلمان باشند .  بریتانیا و فرانسه، عامدانه،…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5160" target="_blank">📅 10:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4ODOPqoFZWka6OKaqDqZELrvwyVMsUJ9Elj2HrV2lRTmLaw9oCDAvk9zCsCSO6BdsNlK9rsUa8oKP3-YZJHnPAtC3iBx8I9Y24EZ6WtENnVpxe4ZJfZZ45j1KcSdVnCDbsbQaTXBAX-CqGOba1FqQkCoNUMM3vaMW-2N6Enwt0EEck1buega5yo9p-uqPtxiDN5QfZFK8N1Y9N3luJoguIo9uUcsi2BTgVvgZAbdDN5MZKVvNVrWmppjc7MAbHut6D8u07Tsz9zMtqJbUMs88Rq8tnZlpdGVifg7JsVa076eYQhEyexQrdjDWgTWKn-aqmxXYxzpkmV61eQ-zzvWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس  با این تیکه کاغذ به لندن برگشت. کاغذ را پیروزمندانه به خبرنگاران  و جمعیت انبوهی که جمع شده بودند نشان داد.  او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5159" target="_blank">📅 09:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baGhNWsepBB5DcpeO-wrTCOcwKYW0GyO5eCrJAk4gAkOVo9mNCGRtNxgMvyO_ClpqI15dPKFAQOdYp5aJI5uBtuQ3GwKbh6FWa3xzYYeUKP40z5JgODga77JLT1uIYvvBVeK-RAXXFfTaABAoS7Tgi2Cd7RnhDWNi6gKdPrA0NHtaLDEDQx29QdZE0SVZtd8Hm77wDOkC2o1TD70G0cumMItO4iNURqB9EKmfvFivYNI29pe2bMGlrbUX4p9k_pPZp4m2dOBafthI-sMVlXfUJSsRn32-3zDKBMcHayBgTocsF8kd0XtQH0B5MkXKh7zrziiOBGmd6z7sga60ZgriQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس
با این تیکه کاغذ به لندن برگشت.
کاغذ را پیروزمندانه به خبرنگاران
و جمعیت انبوهی که جمع شده بودند نشان داد.
او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات داده. این تیکه کاغذ اما یکی از «خیانت‌بارترین» قراردادها بود.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5158" target="_blank">📅 09:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQHP2MbUm4gCBg-fiNzxcmGf9dH423OzzYE-EmQJbvtIblqj31s8ua8OdYAYFjOAJdYVfipbneiM24ySNhQlbOXQZj_z073LOb7vOPAz1qOVb5h43IaVMEYASwmph5nENDv6UjhcHvyMMyvM9jGnZUrucYNuEV9StL-2JxR4itnsmw-e05qKIpW04jfyun34BudQ1Cb4Tu1KDpZ0lTfxg9gmEWcbKFIeNWTiwh5RGig2krXwFGqO1FGHoRLamadjgDtC87bu0sXtgzmzagRrgAntSiNxQpipcApi3LzmvF6rS_Yllu6YRkgOJEXYb1x2YGe6MphD9LNae1SdliKGGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما دیشب بعد از انتشار خبر شنیده شدن صدای انفجار گزارشی تهیه کرد و گفت : منبع صداها مشخص نیست!
بعد صابرین‌نیوز و خبرگزاری دانشجو و… حتی اسامی کشته‌ها رو منتشر کردن
بعد سخنگوی سنتکام رسما گفت حمله کردیم و زدیم و…!
دیگه صدا و سیما در همون مرحله « منبع صداها مشخص‌ نیست» موند که موند و داستان رو ادامه نداد .
«مصلحت» نبود!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5156" target="_blank">📅 23:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=vaMoRDIGpwDAiUYPNV_6a_yAYG6Bitr56WBo9mOOvfjJrEeVQhqy6XunARwRoLjio03biM6_K_Ko9izn2SeAuhPjx4WXjcDy2IaxdfpCBjWyyv3P-ynpD11GQRzV6U7gI-sOLU2pjddHH2TxzB_VB9ecMkkJDdDOca6T5_Ms_1kBOzjx-drr656cWRqzr2iPx2GOtryERN8-fQMjvHo4cEQBYbM1mg3hPU9yxJA7qV9QYIBCNrTxkHApMvxP-t9fUfsqpauVRlOHRaa7n-lsRVQpuFRy-1r6q_su8qv7iDVpfoObyrXFWmXraXHZIkjoQ1irLxByrg1pmbqXsovbBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=vaMoRDIGpwDAiUYPNV_6a_yAYG6Bitr56WBo9mOOvfjJrEeVQhqy6XunARwRoLjio03biM6_K_Ko9izn2SeAuhPjx4WXjcDy2IaxdfpCBjWyyv3P-ynpD11GQRzV6U7gI-sOLU2pjddHH2TxzB_VB9ecMkkJDdDOca6T5_Ms_1kBOzjx-drr656cWRqzr2iPx2GOtryERN8-fQMjvHo4cEQBYbM1mg3hPU9yxJA7qV9QYIBCNrTxkHApMvxP-t9fUfsqpauVRlOHRaa7n-lsRVQpuFRy-1r6q_su8qv7iDVpfoObyrXFWmXraXHZIkjoQ1irLxByrg1pmbqXsovbBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا دبیر: کارمندان بهایی من‌وتو می‌تونن
در صورت بیکاری، تو پارک دانشجو مشغول کار بشن
مدیرِ تراز جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5155" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULYpoi3EnSQmjKXVv1jDDmGu_ERnlG0njJjzPipFCLzIdMIFlzR3qAS-OxHDXxtAwgYAMpic29z_GBVWr4FTLGfzTlCP9ldMAZ1RgMoUHTthsQchI8FGZmcxki6JdtgvQceGLH1hH6Pqst6kdX_yweauRWGxxHtW-ycXMls5xT36x45RMfkKaiLL2fSg8Kt-0iG_ekjyNj8Gv_o_H5q07fE4vZsmOkk0opysAqqxJgNcrxgIRfP_QmfTOKXI5zPEed4vJ48lKZR4rmRFwDuinQcLhqj8vBunjRywIY7J3KXgFIDXg3c0tdSoAjlT3ghf4wMjKFJioQNPllEnC0OsFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاریکاتور شارلی ابدو
از قصد جمهوری اسلامی برای گرفتن پول برای عبور کشتی‌ها از تنگه هرمز.
آخوندی که میگه : به نظرت
چقدر کاغذ توالت بهمون میرسه؟
اشاره به پول ایران و بی‌ارزش بودن
ریال ایران که ارزشش در حد کاغذ توالته.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5154" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏پیام منتسب به مجتبی خامنه‌ای به مناسبت حج: رژیم منحوس صهیونی ۱۵ سال آینده را نخواهد دید.
باعشه!
بابات هم همین‌ها رو میگفت که باعث شد امروز ۹۰ روزه که معلوم‌ نیست هستی یا نیستی، اگه هم هستی طوری قایم شدی که گویی هرگز نبوده‌‌ای :)</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5153" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbczbTsthfFoGoWw_qwIgb6WikYzn7at2vp_Fcim9i6GeOmJcnMMF_pnT9JCaOO80Q9rLCsicdYjRTHsq2t9wb70-EsX_NLeq7QH1idoJZIrLeoNSiVR4OnBMz4NwvrH6vT_gyw0kTemzIEmGmA01E0eRYB1LG3MuooyQ_DZL8xvOQvRuSXtfkTMQMGzlGDEaN_0YiJ04FNCDtArf_IbfZdmgMWxYn0Qmnu92-61-B8YYMwJ0Cx0EKyJa0VlvZ48djnxdmXxMlSbWu0P-FhqEB0AfKz4cIVvJXBbqCQs6XZoNJEOQV6WIL8QGcxwoWt-YyNSpIn__6WCiGu4Xlo0eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر دبیر شورای عالی امنیت ملی، میدان جدید رو معرفی کرده که هیچ کس نباید حرفی بزنه که وحدت شکن باشه!
دستور خفه شدن همگانی تا رسیدن به پیروزی!
اسمی هم از مجتبی خامنه‌ای نیست.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5152" target="_blank">📅 05:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akeFaliVXXpJKbyM9_3_fN479_jjlyrqXYSopvWnIkp-TGdfwQ8vIQE053JTv4RO1QITItIL4GTGSEdVdzOJE-MS8nGZoZe09Taal3cNTRXt3tlQiILjhIUrHJcy53Db8O7CLa2U8gNDvuR0LZNNyksivS7dfwehv8Ts2LieqAaSat7nXXEqXVjgeVeVHvzjRZ3b9ZW_Z0ufawibPgfZMVKLV1lyki40rOzL2QkBS26lAUCO_D5rF57HeND1N_gh41LNIcEzl1TslGi2fIDHDWCq0pE1kZ3wTwpzd8z5pjeIy969BYOdapD_rqzfMxAtAypzXg8zuqD-3N5D5kKaig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه.   سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است. خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5151" target="_blank">📅 04:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeoHDTIqrmnBVIZDVy9h8zWmfQzgrIFMg8F4lF6RK81spAbIY6t2W1Q-B8d80bwOgyriz9Rllf5tBI7mxXtrR_0yJclT6-XZlrmfyvU9MS9ZqhJ8dcLge_V9TyGYcv0MMyJncb5s9_vUAjufAMmVmkQ2Zc9JFubUmC1xA_qME9VSmVJzDMkNo3w2MVqo-g1ZhJgocfsQXurqijtW-w0KHxIbm4LLR0Sdhq58tm13ggSocYK8j2XtiQn_3-wg4H3N8DDkGH3JvtWuUv7Tu5sFV0fS46u1AZ7Gjsv3qFRV8W0939NFJDeuyUQuGSYAar8hIbEY0iiSdxoA6cXzCH4oWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه
.
سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است.
خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها را نامشخص اعلام کرده اما اسامی سه تن  را نوشته.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5150" target="_blank">📅 04:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ : یا یک توافق عالی برای همه خواهد بود یا هیچ توافقی نخواهد بود.
اگر توافقی نباشد آمریکا به جنگ بازمیگردد.
کشورهای منطقه باید عضو پیمان ابراهیم شوند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5149" target="_blank">📅 17:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">قیمت نفت : ۹۷ دلار</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5148" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PadBaw6qxjEqfZYdWNVOiP70IR28SPqF3KvdKODzTAanh1iKE9TnTKF1e2oPHhjt-p1TpB2XRiMW0pDXiiiWZFfBZCHFX00S5XBxkxpsKYcAmNF3tNXISPFI6L9_M8e4ZOrkkvWbnu5LuhRSAVtZBFxMhpbzIbkv_YLbIAIgmwOZHO-LtH0h3CGBXzoqBVefLefeAvIsm53zdXnZi8b2AtrY_X6fgKiwqbFVhtVg16qFoO8qFICnM8lxqE1QesgXFWUYKOvbWCCNsV__NPBbP7Yz_IWaZh_gOvA1lFrbQPxJ7sTBj5ozmJusriyx4jghl7CpIaZoXNHQZZw5P21KDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که صدا و سیما شیپور پیروزی میزنه و از موافقت آمریکا با هر ده پیش شرط جمهوری اسلامی میگه،
سخنگوی وزارت خارجه امروز گفته : کسی نمی‌تواند ادعا بکند به توافق نزدیک شده‌ایم!</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5147" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔺
بقایی، سخنگوی وزارت خارجه:
آمریکا به عباس عراقچی، ویزا برای حضور در سازمان ملل نداد.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5146" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b6861470.mp4?token=vYR-rnWKSVZV-_F_jz3pTDrgS9DjOA8TXBoG1pqRwbZ00vb4eR_wi-1m9NeEjEwy87wDQRwP2ZuKYPeAjhHKXI6jpcu1t1df79XwSYaojo_2L2wXp4pBA8s3ZNhHNa61IVkbjJbfSMFNFlwHp3PVEGvlrxyVJcNnLUvr1cgLTzx05xnYYdieTN6vWtSaxXdXV5W2-AOTQGyPcBsW3aluJN-0p5Kf_GNMIu5xaTMnskVYQL_fYAK47ih0D6ziI0kmkquLNRz_Lxa8GzxjN-W2nqkQCwMPAzrcTRp2yOs_caeu5hw7exEWNyszAtxsK1KsJHIF-dw85PFb8VXmDN-WMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b6861470.mp4?token=vYR-rnWKSVZV-_F_jz3pTDrgS9DjOA8TXBoG1pqRwbZ00vb4eR_wi-1m9NeEjEwy87wDQRwP2ZuKYPeAjhHKXI6jpcu1t1df79XwSYaojo_2L2wXp4pBA8s3ZNhHNa61IVkbjJbfSMFNFlwHp3PVEGvlrxyVJcNnLUvr1cgLTzx05xnYYdieTN6vWtSaxXdXV5W2-AOTQGyPcBsW3aluJN-0p5Kf_GNMIu5xaTMnskVYQL_fYAK47ih0D6ziI0kmkquLNRz_Lxa8GzxjN-W2nqkQCwMPAzrcTRp2yOs_caeu5hw7exEWNyszAtxsK1KsJHIF-dw85PFb8VXmDN-WMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایی از شهر رفح در نوار غزه و پیروزی‌های محور مقاومت
قبل و بعد از  حمله تروریستی ۷ اکتبر</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5145" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل - توی این مایه‌ها -  گفته: «در پاسخ به هر حمله پهپادی انفجاری حزب‌الله، باید یکی از برج‌های بیروت رو هدف قرار بدیم.»
حملات حزب‌الله به اسرائیل رو یا دولت لبنان باید متوقف کنه، یا اسرائیل.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5144" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXjryrAQ66BADT47D9kTqYx9X5rKjuO4PHMYqJqKBbY3f-aXY_UwU_aQwkFRdVSRIAgZbFp0g6pU7vB0nYeimj4-Cpb_UUeUZiIDxEd2Ax_c6lUbWi8IVXf_SmAO-G8yR2daYIMpiE8g8KbDzAMS4v0vXwjXjB7YpDb-XFK-2kb_OxpT6_eDtMH4zQWbQvgDdMV_H_ixLUyjdtMKZBwKzWaDUPJ9NyGr-FFfLcIPJ34o-873UTwqtm5JIrIcO0O3zHv4ZQZpNDXyyE0VSbhOZ4UDiFmzu-_w4OGQTfsY0jJiF6mNuANGK0Uf36jwc-9tviwdDjfpN0GnSYlY8RNPSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=q61xLfJ0wlVK5pp3y6vmQe3wfcq4rAG3-64n5KfxqofYcMcds7DNDy_hIMRipKKS9DgIWu29_l7tsL8_u7XcfYca3pTbD77i5Dbkt76XpE1XcGyacPz7oG1d3e7KLWYYxZUVpKjzyy3uXL6Ipz-7xZU9BciJtfYY2ywSMNQNYTGLRDt5HdQ-fofjsvaQ2g3qMXrT6D5WV7V8TyAawIt-pmq_rgHhtZU1hGuogOuUWLruoOV913CsJRPdNqtZxBZWlzWBMCe3X9wHM4qbV0yxDqaI474K38_qqFS9ArqqG0027PtOZ-IcLneNGlv_ZqaTa7vuuP0zEFZKOAuoc31LaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=q61xLfJ0wlVK5pp3y6vmQe3wfcq4rAG3-64n5KfxqofYcMcds7DNDy_hIMRipKKS9DgIWu29_l7tsL8_u7XcfYca3pTbD77i5Dbkt76XpE1XcGyacPz7oG1d3e7KLWYYxZUVpKjzyy3uXL6Ipz-7xZU9BciJtfYY2ywSMNQNYTGLRDt5HdQ-fofjsvaQ2g3qMXrT6D5WV7V8TyAawIt-pmq_rgHhtZU1hGuogOuUWLruoOV913CsJRPdNqtZxBZWlzWBMCe3X9wHM4qbV0yxDqaI474K38_qqFS9ArqqG0027PtOZ-IcLneNGlv_ZqaTa7vuuP0zEFZKOAuoc31LaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخلاف
گزارش صدا و سیما
۱- بسیار بعیده آمریکا و اسرائیل
به جمهوری اسلامی حق غنی سازی رو بدن،
۲- غیر قابل تصوره که آمریکا
کنترل تنگه هرمز رو در دست سپاه بگذاره و چندین کشور ثروتمند عربی
رو بگذارن گروگان اینها باشن.
مسئله بزرگ‌تر از جمهوری اسلامی است
مسئله سرنوشت منطقه است.
۳- غیر قابل تصوره آمریکا تحریم‌های اولیه
و ثانویه و….. رو برداره و دارایی‌های
مسدود شده رو بهشون بده!
🔺
اما اگه این حرف‌ها ۱٪ درست باشه :
۴- فاصله میان جنگ ۱۲ روزه
تا جنگ ۴۰ روزه حدود ۲۵۰ روز بود.
ترامپ بعد از جنگ ۱۲ روزه گفت بود :
« جنگ تمام شد، ما پیروز شدیم و تهدید
را خنثی کردیم! »
۵- ۱۶۲ روز دیگه در آمریکا انتخابات میان‌دوره‌ای است.
ولی شاید حتی پیش از ۱۶۲ روز دیگر،
جنگ سومی در راه باشد! و شاید پس از انتخابات.(با فرض اینکه حرفهای صدا و سیما درست باشه!)</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5142" target="_blank">📅 11:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5141" target="_blank">📅 09:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=pK21wQVzase_uT7eCBBsKhxIYeyBrAWBi_FjNohq7o1VBwjD2WEOuGMVcjMAI3X2wKtFKC6SG9fx9KqMi48CyAEJ3gJRqblkHuPrrr7EWAq-1WBGgTxncONN3Bs-hrmYP97bQHSakynybBKI7SVTuQcj6z3MWfF9awiZNBbMQXJYu-ICUUTb_6bx1tfgen_V_roAOvLdpMU5J6Z-OcttJQx4-RUuVGouGH4HkUf6A2zeEF3kgv_Z1HvNuKaXqG62eQSDknEnE2nbzaVo5YsUpJqX_HhAZny1iPIIvGISF3XprpKWk4K-jfOBVjx1idOgkqS897nwAKswPWmAQTdzOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=pK21wQVzase_uT7eCBBsKhxIYeyBrAWBi_FjNohq7o1VBwjD2WEOuGMVcjMAI3X2wKtFKC6SG9fx9KqMi48CyAEJ3gJRqblkHuPrrr7EWAq-1WBGgTxncONN3Bs-hrmYP97bQHSakynybBKI7SVTuQcj6z3MWfF9awiZNBbMQXJYu-ICUUTb_6bx1tfgen_V_roAOvLdpMU5J6Z-OcttJQx4-RUuVGouGH4HkUf6A2zeEF3kgv_Z1HvNuKaXqG62eQSDknEnE2nbzaVo5YsUpJqX_HhAZny1iPIIvGISF3XprpKWk4K-jfOBVjx1idOgkqS897nwAKswPWmAQTdzOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدا و سیما:
آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده
‏۱. آمریکا متعهد به عدم تجاوز به ایران شده
‏۲. استمرار کنترل ایران بر تنگه هرمز
‏۳.پذیرش غنی سازی
‏۴.رفع همه تحریم های اولیه
‏۵.رفع همه تحریم های ثانویه
‏۶.خاتمه تمامی قطعنامه های شورای امنیت
‏۷.خاتمه تمامی قطعنامه های شورای حکام
‏۸.پرداخت خسارت به ایران
‏۹.خروج تمام نیروی آمریکایی از منطقه
‏ ۱۰. توقف جنگ در همه جبهه ها از جمله لبنان</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5140" target="_blank">📅 08:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">برخلاف خبرهایی که یکسره از احتمال توافق می‌گویند، فاصله خواست‌های دو‌ طرف هنوز آنچنان زیاد است که بشود گفت :
توافق بعید است!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5139" target="_blank">📅 01:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5138" target="_blank">📅 00:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5137" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدماوند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcoAiXyT8YQVoQ5t3PyfSbSbsAe1WSED_3QAoy6HVDrVadHZ-tBktP3YgMKz-EWnuyHN9EdLHx3IxqNons3liwHECvU2YDGxBFFw4zEFlkBPKsWeCdz_Z84snunI3ICNjKc__o0hbIdLTtHyAGddKAGEuLRGrpwnyCnWaH7Zh29FiyQnEW3l8WINjs-V8Z7WOqzzLy3isoBtfDIfoeurlk_yzFeALjHaGYctFRwn4y1pmaAe4k4-6HHSMg-iFWyBTmhzjqJyNUMahmttygDjOSB7C6qrtI0uoMd4IeoIRjCfYc8qyMpotP4Z-EmZxxRQyLP64N7fvVSrqtyFbN5xDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗
یک اعدام دیگر
مجتبی کیان، بامداد امروز و همزمان با اذان صبح، به دست جمهوری جنایتکار اسلامی اعدام شد!
جرم او را ارائه مختصات صنایع تولیدی به شبکه‌های ماهواره‌ای اعلام کرده‌اند؛ انگار که اسرائیل که اتاق خواب رهبران رژیم را می‌داند به اطلاعات دیگران نیاز ندارد...
خبرگزاری سپاه نوشته است: «وی در پیام‌هایی به شبکه وابسته به دشمن، اطلاعات محل شرکت مرتبط با صنایع دفاعی را ارسال و با قید نام نخست‌وزیر رژیم صهیونیستی در پیام ارسالی به عوامل این شبکه تأکید می‌کند که موضوع را «به بی‌بی آمار بده»!
T.me/irdamavand</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5136" target="_blank">📅 15:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">️
🚨
🚨
آکسیوس: یک مقام آمریکایی گفت که پیش‌نویس یادداشت تفاهم شامل تعهدات ایران برای هرگز نرفتن به‌سوی ساخت سلاح هسته‌ای، و همچنین مذاکره درباره تعلیق برنامه غنی‌سازی اورانیوم و خارج کردن ذخایر اورانیوم با غنای بالا از کشور است.
☢️
به گفته دو منبع آگاه، ایران از طریق میانجی‌ها به‌صورت شفاهی به آمریکا درباره میزان امتیازاتی که حاضر است در زمینه تعلیق غنی‌سازی و واگذاری مواد هسته‌ای بدهد، تعهداتی ارائه کرده است.
- ببینیم چی میشه. بعید می‌دونم جمهوری اسلامی اورانیوم غنی سازی شدهاش رو تحویل بده،
خبر هم میگه ج‌ا به یک میانجی (پاکستان / قطر) شفاهی گفته!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5135" target="_blank">📅 07:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‏
🚨
🚨
ترامپ :«من اکنون در کاخ سفید هستم؛ جایی که همین لحظات تماس بسیار خوبی با محمد بن سلمان آل سعود، ولیعهد عربستان سعودی؛
محمد بن زاید آل نهیان، رئیس امارات متحده عربی؛
امیر تمیم بن حمد بن خلیفه آل ثانی، امیر قطر؛
نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی و وزیر علی الثوادی از قطر؛
فیلدمارشال سید عاصم منیر احمد شاه از پاکستان؛
رجب طیب اردوغان، رئیس‌جمهور ترکیه؛ عبدالفتاح السیسی، رئیس‌جمهور مصر؛ ملک عبدالله دوم، پادشاه اردن؛
و همچنین ملک حمد بن عیسی آل خلیفه، پادشاه بحرین داشتیم.
موضوع این گفت‌وگوها جمهوری اسلامی ایران و تمامی مسائل مرتبط با یک “یادداشت تفاهم” در ارتباط با صلح بود.
یک توافق تا حد زیادی مورد مذاکره قرار گرفته و تنها نهایی‌سازی آن میان ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلفی که نام برده شد باقی مانده است.
به‌طور جداگانه، من همچنین با نخست‌وزیر اسرائیل،بی‌بی نتانیاهو، تماس داشتم که آن هم به همان اندازه بسیار خوب پیش رفت.
در حال حاضر، جنبه‌ها و جزئیات نهایی این توافق در حال بررسی و گفت‌وگو است و به‌زودی اعلام خواهد شد.
علاوه بر بسیاری از بندهای دیگر توافق، تنگه هرمز نیز باز خواهد شد.»</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5134" target="_blank">📅 00:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5133">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t23_C8EVUmFSKFfRJXa12X5RSKdXccSs0pe0MKJRBvn-O0ZbhyKWDagOhNnARENQrdgVlPiiQmvvlgGNSkJlGioVzOVxHqtsXF44eSyqboS76MN21gxw1yCPnl2C1nrOtSadBWPsFzm_7XoDCQJBSyZVMVGz0QLoM0mp5EAw1nyzhrbUSWZE_RPlq7XJCK-rXB99RbcpvfYI2x6drRxQlaX-tOlFQLbmAvbdjpiGecHTfpRwbBOz6D-NvN6yuSXys57MUmbPN5RQItMv_p-5-p6sd4jUNPPBAD6IrFUY9gKvFSIMz9XiJM7k9kJshmLRxwEW-h0R3wbpVo7BricJFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با هوش مصنوعی طراحی کردم.
گاو : نماد فراوانی و ثروت سرزمین ایران و منطقه.
تن زنانه و نیمه عریان: نماد پاکی، نماد لطافت و ظرافت ، در نقطه تقابل با خشونت و توحش و درندگی
بقیه هم‌ که معرف حضورتونه، آشنای دیرینه.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5133" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5132">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ به اکسیوس  گفت که درباره توافق با ایران یا بمباران، «کاملاً پنجاه‌پنجاه» است. ترامپ گفت امروز با مشاوران ارشدش دیدار خواهد کرد تا آخرین پیش‌نویس توافق را بررسی کنند و ممکن است تا فردا تصمیم نهایی را بگیرد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5132" target="_blank">📅 20:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5131">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
آکسیوس : ترامپ ساعت هشت شب امشب ،  در یک تماس کنفرانسی  با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5131" target="_blank">📅 20:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
آکسیوس :
ترامپ ساعت هشت شب امشب ،
در یک تماس کنفرانسی
با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5130" target="_blank">📅 20:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=TU6kz2UUq_kMTCO9u3sDPOsg-li70zIg-9FBg8mCMk-fcTjR4esLHUP9Lw8lj8kcm9xWbdY5b9_6aZ9tU1KwfwlDWnF8wkjZO5w9fNj6n6IdWETUEj0Td9FsKuufoBHIvP7Q6800u0r2iCTpEfUGJbhRXKzBupGv99fe7Q3-JsEGM_STfDIcolXmGQErlARNOMaE0bQSeGz4ms_4btPCjo8pnqoiao-LzY-WzubjOI2ezKqI2BLyca7P-Mw8l-MIqCfzOah5lBbIusV4J92_eBeXFK1pT_JYwAKMBRhcaniKW0rhV-jlki7dzNWH5wiT4EnZoOr1KYz1y-YRlHf7jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=TU6kz2UUq_kMTCO9u3sDPOsg-li70zIg-9FBg8mCMk-fcTjR4esLHUP9Lw8lj8kcm9xWbdY5b9_6aZ9tU1KwfwlDWnF8wkjZO5w9fNj6n6IdWETUEj0Td9FsKuufoBHIvP7Q6800u0r2iCTpEfUGJbhRXKzBupGv99fe7Q3-JsEGM_STfDIcolXmGQErlARNOMaE0bQSeGz4ms_4btPCjo8pnqoiao-LzY-WzubjOI2ezKqI2BLyca7P-Mw8l-MIqCfzOah5lBbIusV4J92_eBeXFK1pT_JYwAKMBRhcaniKW0rhV-jlki7dzNWH5wiT4EnZoOr1KYz1y-YRlHf7jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بعد از صدها سال
مردم شمال مدیترانه و جنوب مدیترانه بهم رسیدند
الجزایر سال ۱۹۵۲  (۷۴ سال پیش
مناطق اروپایی نشین
و مناطق مسلمان نشین</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5127" target="_blank">📅 19:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7qKR67RYzLDJBKXoNkjiO3u5oFAt4NEDhJ6XXQYbd15KOuUexNUEHqGv1XtH-ZYiaGqpbFAkE2EK8GJG65odaywhMdbFznB6CutePvyw_K7VlJwLqbupJeo7vj8qSeaEk5e_laYtg3ud54XghoZQRKSEvdPdamxg7gL52fYF8IwJkooV4Dt0_bjNsGS9iJhzKsJy9_Yo5qfWsEfxj_SASnis9MDB-Mv1GRxTNPd5c8nhPcVgsBHa40u71TnriYA7Q9M2q35IrNcuzLD2fZq3fX3vucyOB8xsaWVihTP4AZ0wGUMjna2a1Tn-jC9TIS7pRt_3GCP2CFDrMOGmc4uUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمال دریای مدیترانه، اروپا، نماد پیشرفت
آرامش، ثروت، هنر و معماری و….. است.
جنوب مدیترانه، نماد فقر و بی‌ثباتی
و جنگ و سیل مهاجرانی که
از این سرزمین‌ها می‌گریزند و …..
مصر، در جنوب مدیترانه، برای ۹۷۰ سال بخشی از جهان یونانی - رومی بود.
لبنان و فلسطین هزار سال، لیبی ۱۲۰۰ سال،
تونس و الجزایر و مراکش حدود ۹۰۰ سال.
تا اینکه اسلام از راه رسید
و تفاوت میان شمال مدیترانه
و جنوب مدیترانه شکل گرفت.
و دو سرنوشت متفاوت، دو چهره متفاوت گرفت.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5126" target="_blank">📅 18:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5125">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zzp2YK1szGH7V7NQ99EN_D7Y40cz7v3u1N-Ls8Kp4J8pd_YVJQzzkc9gXngSQgArorvhSDzrmGa2rKEP1xzF0a213opOzG-puTKgn0PwKZPQUWDmj9by1ASIOUTTWDYB87FC9OPBmBGQwX1KtZZCfVS1efci4bM9OJYHEGE5s_BkYQ0XU_DyVkB3XMfhpSa22xA0bMTIar1nMuV3gBjkkTCLFC_l8sVFT1Wt4_8YRRq-SOEwCvN5Ez_90mnmRh6fihd1QfTdkAMoytiUpeBPS6aCqBDzxBBuw7BVAITJKSOerzy6edftuckX-vXnVxzwNMs0HtUA0V6juwKIQCjyyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که پرچم آمریکا را روی نقشه ایران به تصویر کشیده و تیتر زده «ایالات متحده خاورمیانه؟»</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5125" target="_blank">📅 18:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5124">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:  شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته. شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.  جمهوری اسلامی باید دست از غنی‌سازی بردارند.…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5124" target="_blank">📅 17:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5123">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:
شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته.
شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.
جمهوری اسلامی باید دست از غنی‌سازی بردارند. اورانیوم غنی‌سازی شده را تسلیم کنند، تنگه هرمز باید باز شود.  ترجیح رئیس جمهور ترامپ دیپلماسی و رسیدن به یک‌ توافق است.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5123" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5122">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kub63AU8UG7_SnDig4EdX2ul-gdZct3w0Bm8Z_dY9sTz6nQljyjbImYAQmfOlfGsTJkpKp5xbljUfEm7uf-gUN2koIUUk7qrXJmfUwhpAA5g0u0OHYZRbzx_L_Ebc985jkiJf34UP_QYKLXsHUjoCtnIzhVAUr7iA9lTl-9SGW460zwiXZqYUBRaLtQRfy6K1zHjwP2SsrevbLyJTExBxtx-_8CLLlOkGw6JAnfgaxC0ZtVmoRp366DbGM2e9jCJY_Vxv0ofXpnYXsmk9IQRvi7Bx3u4lkL6XYNvjtlxRiNFQpuvYOjqHdFR6xInYtHMf0-XQTFjzkYDvX-dP7pS0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقدر ایران باید هزینه بده برای این گر‌وه‌ها
و برای این جنگ‌های بی‌پایان جمهوری اسلامی با آمریکا و اسرائیل.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5122" target="_blank">📅 17:18 · 02 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
