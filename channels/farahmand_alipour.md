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
<img src="https://cdn4.telesco.pe/file/cbU3eORFKmYNVSaWUlIQMdEaNUhjNftOgBwQ1h5nHZ397Szdl2nKaEWa2E3WS0-f5klnTNxrnEtX6ckcMQJ_mlvM5exD7qdh9ILCj8PgAZD8xcT3e2a4BewtfomKlz9maQQ8N5hsJ67-cOHiMZkEw_-1f12kU4f8OllskMgvBPTouWNppR1eDfpIuOG1jr3yYpSqBjySfmHIhdUOjZ5M-k08rUcUq6GHZ2UFgrbnplzhFKqyNkCbj-PEDdbAjH__6FZfCWZGoM1GW5hxcatieEb-AAHpFq6mIYMVoyZptkXZlPY3AjvTVZ-LvjSeAD4U86Unv89fLJ1N6Kf9m9nQAQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 08:10:41</div>
<hr>

<div class="tg-post" id="msg-6198">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5132059c16.mp4?token=FRJB6a2DWt6nOid-BClhhjow_-KrFCMvrZ8ntDleTUI4kPj5xLmah5CK-XhLIDEEjcJQV0MFH5kOqkRisK2BV0HG3adSVr9MN6qkGIIbTuDO0C9uGBMTUJphzoJec8_wWJ3DbjWmteOhTnv_ltUA7ZIEZENaeWRU3i2PtgLPH1nESxKceg_tl0D-e_XDG1LqJhkbwRDkABJ2YlWhCl0blYcmE_gxnyt_dCsIkULSZF3knbr1ptjS2yS4ftSznN-AgVy72UYNTeANy_WkcrciErfDabJUsEtsz34umBU3w3tcSHxQPP6gk_MUAamA7qBZ3lhDt0DPnFJ1NfjlMjWE3WBUrDGCS3hAXLA0sNFqOqHbgm47Gp9fpmOVHN-9WofqPIMPi3k_HsHmCEX_am_ipYOlW1egvF6kGtUxn107Q3pQV7xhxwde6SIMJMa8pq_ZNTDxltSS3YYIL9_WFcSX4tE7ur6-OXbsY4DpKhoaP5lY9dy_ZXo5DJFLUQDTtWGLOOnahLteGMUKlIC7oFKIsGfUH8Pa6SvDf4VlLUaY4O0ykaoNYz8_vH1IlFN2DIiNtapZli-bqlBGVt2JB6qdanbHV6ytIf277AB0VpcHsLLUJgGd6q2e0H637Vg0XuUo2AXzUgdsm3g6V0aE1sjrXzncNO2ZLHEcPqpX49vL4to" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5132059c16.mp4?token=FRJB6a2DWt6nOid-BClhhjow_-KrFCMvrZ8ntDleTUI4kPj5xLmah5CK-XhLIDEEjcJQV0MFH5kOqkRisK2BV0HG3adSVr9MN6qkGIIbTuDO0C9uGBMTUJphzoJec8_wWJ3DbjWmteOhTnv_ltUA7ZIEZENaeWRU3i2PtgLPH1nESxKceg_tl0D-e_XDG1LqJhkbwRDkABJ2YlWhCl0blYcmE_gxnyt_dCsIkULSZF3knbr1ptjS2yS4ftSznN-AgVy72UYNTeANy_WkcrciErfDabJUsEtsz34umBU3w3tcSHxQPP6gk_MUAamA7qBZ3lhDt0DPnFJ1NfjlMjWE3WBUrDGCS3hAXLA0sNFqOqHbgm47Gp9fpmOVHN-9WofqPIMPi3k_HsHmCEX_am_ipYOlW1egvF6kGtUxn107Q3pQV7xhxwde6SIMJMa8pq_ZNTDxltSS3YYIL9_WFcSX4tE7ur6-OXbsY4DpKhoaP5lY9dy_ZXo5DJFLUQDTtWGLOOnahLteGMUKlIC7oFKIsGfUH8Pa6SvDf4VlLUaY4O0ykaoNYz8_vH1IlFN2DIiNtapZli-bqlBGVt2JB6qdanbHV6ytIf277AB0VpcHsLLUJgGd6q2e0H637Vg0XuUo2AXzUgdsm3g6V0aE1sjrXzncNO2ZLHEcPqpX49vL4to" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا قبل از جمهوری اسلامی
ایران همین جغرافیا رو داشت، همین تمدن همین مردم و همین نسبت جمعیتی،
اسرائیل باهاش دوست بود و آمریکا پیشرفته ترین  سلاح‌ها و تکنولوژی
رو بهش میداد و اسرائیل برای کشاورزی
و آبیاری به ایران کمک می‌کرد.
شما اومدید شعار محو دادید و پول و سلاح ریختید توی لبنان و فلسطین و…….
🔺
همون روز ۲۲ بهمن به دفتر اسرائیل در تهران حمله کردید !
🔺
اردیبهشت ۵۸ رابطه با مصر رو به خاطر فلسطین قطع کردید!
🔺
دو ماه بعدش روز قدس رو راه انداختید!
اینها میخوان مردم رو فریب بدن و بگن «مسئله ایرانه و تاریخ و تمدنشه»!
نه خبر! مشکل جمهوری اسلامیه</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/farahmand_alipour/6198" target="_blank">📅 08:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6197">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔺
سپاه : به انبار دپوی قایق‌های بدون سرنشین آمریکا در بحرین حمله کردیم.
🔺
حملات ج‌ا به کردستان عراق</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6197" target="_blank">📅 01:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6196">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
وقوع ۵ انفجار در یزد
برخی گزارش‌ها می‌گویند که حملات در پارک کوهستان یزد بوده (منطقه سایت موشکی)
🚨
گزارش ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6196" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6195">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=dfaAKyRCDXSJtwQ2Kp52tYSddR5rfJwsp1vtElLD50iMuuTJHcgi3NmSjdk934oFPpGpNOgF8qO_F6ueFJydedzHuoV4wGOcU70-jzt1wHpNkKzJHa1xwctgxRHgyxjvfOI7m4amCW-X2zvd33lr97jN1WfiiRFJG1OwO3WEPaCusBlLrXl6cTHewG_Q3u7KYUihDB9q6VHpGmnLSdqyxaM0dERSom19dUYN6QyBpXDa53zXYbIen8-IaoirW65W86yUhkxyzYl_RDYV19dJ7s-WaMeEFL49spKu2DpJh4f7nMbhT8VLDFISKTMlDMIGBHYAQXxb74TifeYkg6ADWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=dfaAKyRCDXSJtwQ2Kp52tYSddR5rfJwsp1vtElLD50iMuuTJHcgi3NmSjdk934oFPpGpNOgF8qO_F6ueFJydedzHuoV4wGOcU70-jzt1wHpNkKzJHa1xwctgxRHgyxjvfOI7m4amCW-X2zvd33lr97jN1WfiiRFJG1OwO3WEPaCusBlLrXl6cTHewG_Q3u7KYUihDB9q6VHpGmnLSdqyxaM0dERSom19dUYN6QyBpXDa53zXYbIen8-IaoirW65W86yUhkxyzYl_RDYV19dJ7s-WaMeEFL49spKu2DpJh4f7nMbhT8VLDFISKTMlDMIGBHYAQXxb74TifeYkg6ADWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گزارش چندین انفجار در لار
برخی گزارش‌ها از حمله به سایت موشکی لار خبر می‌دهند.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6195" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6194">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbBppC3kE4yiqvn1rPHo5LlwHBLSmaHvizSpBZGLNUz4gRKpxGzCOHkieTXV_mtXVmjA8iUFweBq2r_sO6aWBrzIUP04nKaaLvtIlzuYj_T33P6VB477eSUrzcfNbex07FxYKIvTm923ZWUCjQ_93cESQVKHSjPIcG6ZLG-uy4SVEsWn3jzpKo3FLv5GoPxQIZGWWxZHS6HAf_q0wNHP5j4C6Zk_B-wARPr6-kGZkylyPopWt8eL_7fO_hX5d873A1jCUqrPWjsA-ZQqOHlAJq5d_A6PJ4mb-Sd6oeHtXvna7lWiOQq52OF4-22STGgayexXHILpktMYVIw1eh-bVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش حملات ارتش آمریکا به بندرعباس، قشم، سیریک، بوشهر و اهواز</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6194" target="_blank">📅 23:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6193">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
سنتکام: ‏امروز ساعت ۳ بعدازظهر به‌وقت منطقه زمانی شرقی،
[۲۲:۳۰ به وقت ایران - یک ساعت پیش] برای هفتمین شب متوالی، یک دور حملات علیه ایران انجام دادیم.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6193" target="_blank">📅 23:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6192">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029791358c.mp4?token=G_Ar6iRCUc11R-46msXg1j-h30ffm98JIWUM_SzpGtvGP2VSkiH6v26FzQLGoQY19KhOYidUnba8ufzYCyub_qzKLU_VhhDWvLbzOtRSLaYy-oWiReFzdJnQQMIb0TWkK1-PQgH6MOujJtIB58jmQNUtAp6ptaHJ_0XIkwPaWjEzzOjbWWYy2t1mBkNtFBCflgIu8CmJa2q2UlzV7VapKHbxNU-dQOz5_gMR6WptDNsw5asRpCNsXTlh-OcMLpCvpFWhP1fWA1_HzotEvuN9vfYrg5NHY4i9IEj_A8PMgUMv3MgM4UbrK6UmYpiFSOPwwWC6ekRm8mAZcKArcqP6YLd4RXvOh05J8a6kZIWNJJsVMeLY07jgEWShJl21f7IZLKp3D-6D0vJk-MW5LK87cryhTE8YTqL8przbAL2ZzG1sFF_HQuP-ABDoMvbXgS0d8_dGZphfJdUVjYmS1UjCrPgUELzEPEfzUPupwyzMRaA_LzFCtb5KJV1w3PPSwmqAW8pMuYrig_MN8XItauN08_2sCoQ03OKrQnv2aUstJkNH87yYWd6uezQRyi4jqjmmpzvRbklmTyNBVe_RgDiOJ__flx_kb1NAh45LnFFfvgx63ieag599La85voJ5hef5Ogw60Jyx3rdAf3YVfXqULA9NN3Z__PFGyg5QlxNbMQs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029791358c.mp4?token=G_Ar6iRCUc11R-46msXg1j-h30ffm98JIWUM_SzpGtvGP2VSkiH6v26FzQLGoQY19KhOYidUnba8ufzYCyub_qzKLU_VhhDWvLbzOtRSLaYy-oWiReFzdJnQQMIb0TWkK1-PQgH6MOujJtIB58jmQNUtAp6ptaHJ_0XIkwPaWjEzzOjbWWYy2t1mBkNtFBCflgIu8CmJa2q2UlzV7VapKHbxNU-dQOz5_gMR6WptDNsw5asRpCNsXTlh-OcMLpCvpFWhP1fWA1_HzotEvuN9vfYrg5NHY4i9IEj_A8PMgUMv3MgM4UbrK6UmYpiFSOPwwWC6ekRm8mAZcKArcqP6YLd4RXvOh05J8a6kZIWNJJsVMeLY07jgEWShJl21f7IZLKp3D-6D0vJk-MW5LK87cryhTE8YTqL8przbAL2ZzG1sFF_HQuP-ABDoMvbXgS0d8_dGZphfJdUVjYmS1UjCrPgUELzEPEfzUPupwyzMRaA_LzFCtb5KJV1w3PPSwmqAW8pMuYrig_MN8XItauN08_2sCoQ03OKrQnv2aUstJkNH87yYWd6uezQRyi4jqjmmpzvRbklmTyNBVe_RgDiOJ__flx_kb1NAh45LnFFfvgx63ieag599La85voJ5hef5Ogw60Jyx3rdAf3YVfXqULA9NN3Z__PFGyg5QlxNbMQs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت شانه خاکی موقت کنار پل بندرعباس</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6192" target="_blank">📅 23:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6191">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏یک گزارش محرمانه که برای رئیس جمهور ایران تهیه شده است، نشان می‌دهد که تنها ۹٪ از ایرانیان از وضع موجود حمایت می‌کنند و تقریباً سه چهارم آنها یا اصلاحات ساختاری عمیق یا جایگزینی کامل نظام سیاسی را ترجیح می‌دهند - فاکس نیوز</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6191" target="_blank">📅 22:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6190">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:  ترامپ به ما نامه‌ای داده و صراحتاً نوشته است: «بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6190" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6189">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a688590cec.mp4?token=BYNnG-pdOr6bHjKx0USJi0hTO3AIs5zo4_QOAjigxDJ7gG6C0jzVbhUY_SbasafwINjNw4fqVnxaYM9PmK5FpxA-ZDg4OjR0MWuIh6dCvTpnU33XgxvNRTcGMoZawBf9YBuCvIPLmn15ORWcu1943N550l0hH828CV7hw5QzulNcmVUPbHxexXf7Wn3v2kvBNdvqwEMM155nQpu3x35OPIcgvJMC6nYlIAIRP0KSdcINoIydKeslQjx5uOxacmYrKKAYYK-2DA--qeIWG4SrdsAOx8potK-7uWFknXzXDcu8n9dipPtGU7DV_ZpwnduuBGsi-ulCNDaM1VLMz0NjZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a688590cec.mp4?token=BYNnG-pdOr6bHjKx0USJi0hTO3AIs5zo4_QOAjigxDJ7gG6C0jzVbhUY_SbasafwINjNw4fqVnxaYM9PmK5FpxA-ZDg4OjR0MWuIh6dCvTpnU33XgxvNRTcGMoZawBf9YBuCvIPLmn15ORWcu1943N550l0hH828CV7hw5QzulNcmVUPbHxexXf7Wn3v2kvBNdvqwEMM155nQpu3x35OPIcgvJMC6nYlIAIRP0KSdcINoIydKeslQjx5uOxacmYrKKAYYK-2DA--qeIWG4SrdsAOx8potK-7uWFknXzXDcu8n9dipPtGU7DV_ZpwnduuBGsi-ulCNDaM1VLMz0NjZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:
ترامپ به ما نامه‌ای داده و صراحتاً نوشته است:
«بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6189" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvDYAVxq_VcbEn0jaAtD5W0oDdCv3M8dmdxBphtzQ5ZwVVirnEuae7sQDY784gBK6BpZHGygBOPw0ePCzEjP8oa-y21b_C8vFWf_neLyAqf_Wbd7azZZUTfH89ug8shTlr8FOJfiyueNVS0BNi_E9sxOtFj-Zr9WdrRH6t2Mx6NALQBEyBifA83N9-w67rDqsQ-p0ZkWtPrVIBSdzYdbAZQSA8jNCx7-m0U0c5ubeMLRs6Ek-tOMEEqhg4k1z2U1vhP8aJsrJfW_zhBQbml2fRWDupFkGydVYyYxuDsrZrSNuy8hEr_6_uBv2KdiOOzC0chxlBOYOHNbuxHcbjYmzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ایستگاه مترو در تهران با مجسمه مریم و عیسی درست کردن (که عجیب هم نیست،
نصف قرآن داستان‌های مریم و عیسی
و قوم یهوده) و پروپاگاندایی راه انداختن
که ما چقدر احترام میگذاریم به بقیه مذاهب.
بعد همزمان کلیساها رو مصادره میکنن
و صدها نفر به جرم مسیحی بودن
توی زندانهای ج‌ا هستن و اجازه داشتن
یک مسجد به سنی‌ها رو هم نمیدن!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6188" target="_blank">📅 18:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6187">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o23JcAiz3J-Icg3U2M2NzvMMdb40oPmFoaBYdlEUwYBjyhuN5b7h2IyB8XgQrGu_Dq7InpDe7TcU2ZambOI_wXSGPPLisXRqSm0xPvHzpWORotmFzWGypHPDRcs28w5fgyeAPgPX9tmcEit4U8j9ZNBkqD25XpgTKaBzyczAQNroCMUmhkA_u6H04mdQtYeTzyX2ghvNenOWyuC42uvE645ZfSEQuwM6bftXXPSROfKTqucxUJy8Aa9k8LJWwmH-QDEjrouQMl89LJ258sbqW6S1tVKp-PMIp46gh9b6vqZvF-z-Z8kH5YlZDHes4FG4ujPhCMiuflxA-C9mAuAtDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب طلاقش بده :)
چرا اینهمه کینه؟</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6187" target="_blank">📅 18:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pj5r17LvhYKZPKH_z4Yr62thpiFHiUk8LiH26S0LqfbzRr4anLt-I4ZlHGmLLLokjaV7l3yCbMbH_sSwpzpoZRl_bN13-AuNvNRSDhRXn_0pWfAMFXI4j00iMQrdXOrrZlNW__UkxJ6YAYYDdIKuzjK2jXSON60UJVXKLGpSiLQs7ewG1M34omN483pt1bgKdxYdtLJ4MBnsrZGMgPCBlKZyeS0uSstBfzav_2qmMuBExOvZT22uS2fGMWylDiqDPF-rg6O1gBmACv9_Vtg-0tRr1_lFJMPu0svI6UoBFTlaJtH_Ay8aPYXXW4r5GwjOUXuhxMzY67FHpPB16lEb8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل عرزشی !
من میگم اینها شکست‌های تاریخ
رو پیدا میکنن و به عنوان الگوی خودشون معرفی می‌کنید باور نمیکنید :)
تنگه احد! که نماد بزرگ‌ترین شکست و عقب نشینی مسلمانان در تاریخ صدر اسلامه،
رو شباهت سازی میکنن با تنگه هرمز
‌‌میگن همونطور که اونو در سیطره داشتیم
اینو در سیطره خواهیم داشت.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6186" target="_blank">📅 17:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6185">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7JiqJqye3zdqbbRe61tMDRcNRd1HRUc8lwStEdbQx3VVCEWyoVq17TPi-MSLx_37Wk7962pQr0S4OxJ2-XvASxtp7NIqc-E7JezT6ns4DQnxD5uhBsTg0bVd7RW3am31cclvv04Dt2y4WnbYhwSsDG-AX6qNaIcFxcydkS7L40vrePM66G5ChtNGeybD5D7xlld9u0XZP7w3ZHcv6SEa7zjHlu2EWCtEA6mxikm7Ux77QHLAfxeZN4bmdoalyYF1j902Dt_OaFkQay4ODUaKCofw0gLn0U2ls930_94RLVk95vfPBB50OdPHPiRglhSM_HTEwMZ3i0PQTxJjXc_4dd-I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7JiqJqye3zdqbbRe61tMDRcNRd1HRUc8lwStEdbQx3VVCEWyoVq17TPi-MSLx_37Wk7962pQr0S4OxJ2-XvASxtp7NIqc-E7JezT6ns4DQnxD5uhBsTg0bVd7RW3am31cclvv04Dt2y4WnbYhwSsDG-AX6qNaIcFxcydkS7L40vrePM66G5ChtNGeybD5D7xlld9u0XZP7w3ZHcv6SEa7zjHlu2EWCtEA6mxikm7Ux77QHLAfxeZN4bmdoalyYF1j902Dt_OaFkQay4ODUaKCofw0gLn0U2ls930_94RLVk95vfPBB50OdPHPiRglhSM_HTEwMZ3i0PQTxJjXc_4dd-I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیا بودن شعار به زبان عربی میدادن؟
چی میگفتن؟ میگفتن  سرباز ایران و وطن هستیم؟
نه میگفتن «سرباز دین و عقیده» شون هستن!
و کنار لبنان هستن! و مسیرشون همیشه مقاومته!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6185" target="_blank">📅 15:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ijt5NRK3bltsYCoHkEWDkhrcfi5qZ--8GXUF5P3-8IK0TPqriYcGaj_rju2tJ7vUgwYsS5u9HmUMtsvwofBpwQIY_G8VauO1lhDEPE79BAXOnZcWgApkjZp8GP76Nxi2zQQ9wVFiPyWCkbhC-9yvd0w_1ZnHvvy65JIPelk236nzSTkWZJOOo82ttchl91wf8Wqd9mCD7pIa5mPzdbLXD1iNMUNym65cPe24AyUPfo20PC1xb_MnWNYdf5MmiJ0HfjfWiWjCciXf3-nfQwoVq71WQBin3R_7y7TWbh_DZcycgfxnLxzhmpI6d4g18W17wla0suaespRUpAdDgjiyJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی به تاسیسات آب‌شیرین  و تولید برق کویت حمله کرده.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6184" target="_blank">📅 14:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6183">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=JYCCchxyPd6A7ilQkz80EaXyVs2eEsT0foYs0LNA-hNCrlVX8uDIyd-GqnSj5S2pA-NoJCWDs722GN6rh_Ulp8FaQ0otBJuAQbmpJQ708RODUIsw74MXBXvtq7PL43Lw1-UcXriz7sjhxUJ_-S4b-ut0y0jgQ6bDNuTeQqHPL1cMhNAvReGvM30SDFNiUAhxndwwJO1AJzo07_DC2-7eu59ijUkCzJoG_7SBCDpUqnnqNyZzxS9d3tfNka8FoWGidqeZPqX2Fe-VYDqyVPpf4atEFBFm_dWFHWLR04c2eYcB5XOY4r0ClYFla4O8NDsMZLeR8uv-naHUfuY0s1njVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=JYCCchxyPd6A7ilQkz80EaXyVs2eEsT0foYs0LNA-hNCrlVX8uDIyd-GqnSj5S2pA-NoJCWDs722GN6rh_Ulp8FaQ0otBJuAQbmpJQ708RODUIsw74MXBXvtq7PL43Lw1-UcXriz7sjhxUJ_-S4b-ut0y0jgQ6bDNuTeQqHPL1cMhNAvReGvM30SDFNiUAhxndwwJO1AJzo07_DC2-7eu59ijUkCzJoG_7SBCDpUqnnqNyZzxS9d3tfNka8FoWGidqeZPqX2Fe-VYDqyVPpf4atEFBFm_dWFHWLR04c2eYcB5XOY4r0ClYFla4O8NDsMZLeR8uv-naHUfuY0s1njVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!  ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟  به خاطرش حتی موشک به اسرائیل نزدید؟  (که اونهم اومد در پاسخ ماهشهر رو زد؟)  خب جنگیدید و شکست خوردید!!! هم در لبنان،  هم ‌در سوریه…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6183" target="_blank">📅 14:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6182">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902cf63917.mp4?token=dWf6EZTzIZf3kpUPVPuf_cAJQ7CVsy6iOkabI1WMmPrMCmbCdf3PBOIlPELF9sFx9gbVeQWwfNcuLeUa4QU_BBCUd3gKmjlXvyZUZ08cBKj3nLAez_ENdXELSOpAIVZNTLgqL16rT199nbBMNVKcJtyIotZqRlVoIcu0OJ2cyfO-uznwRfHpz7MgJ0Ev7WFyG5nN24g6UmpbBqC-UR53wUpaTiq6S-XtObe077k_wLYzVjMumFAoJYCYg8FtdIrvQhkOV08qxdLb2Cq1z9Yq7_76v-YqTZSTTzJ8rXLZpwhRM6DHhgnsdNY7VKNLW7A-zQz65nNpv_7d9A2R3dhG9r3d8jVanJfe4kBsbvUeUUR7S09TeXOpP19Qu6UGBuaR30Q-QlCY9gEkKekSkEPOr2HoD88xfGyvODaPdd1H3ST_xupUfTkWFVxEadR6oOCxUqDjRLuBWsWsL3BaJu485qR-vQSJ96eaZRLdYqQ3y6phGUXEiLeVznHmfk8YdUlva7JDYRhAT8trRdobzd1OmEmQNlPP5HA1bTaz1-lNy6vBCFiuoLOOm93exEiOngC1zSziUSD6IXr0gqueGss_N3oTBj9jJliavg04_hkOhQ670MislNdEwnWkCsRPdvpyK2nPZfHcWtg7S039SnHp7EUjodPYTS1LKZRiu5vjTFM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902cf63917.mp4?token=dWf6EZTzIZf3kpUPVPuf_cAJQ7CVsy6iOkabI1WMmPrMCmbCdf3PBOIlPELF9sFx9gbVeQWwfNcuLeUa4QU_BBCUd3gKmjlXvyZUZ08cBKj3nLAez_ENdXELSOpAIVZNTLgqL16rT199nbBMNVKcJtyIotZqRlVoIcu0OJ2cyfO-uznwRfHpz7MgJ0Ev7WFyG5nN24g6UmpbBqC-UR53wUpaTiq6S-XtObe077k_wLYzVjMumFAoJYCYg8FtdIrvQhkOV08qxdLb2Cq1z9Yq7_76v-YqTZSTTzJ8rXLZpwhRM6DHhgnsdNY7VKNLW7A-zQz65nNpv_7d9A2R3dhG9r3d8jVanJfe4kBsbvUeUUR7S09TeXOpP19Qu6UGBuaR30Q-QlCY9gEkKekSkEPOr2HoD88xfGyvODaPdd1H3ST_xupUfTkWFVxEadR6oOCxUqDjRLuBWsWsL3BaJu485qR-vQSJ96eaZRLdYqQ3y6phGUXEiLeVznHmfk8YdUlva7JDYRhAT8trRdobzd1OmEmQNlPP5HA1bTaz1-lNy6vBCFiuoLOOm93exEiOngC1zSziUSD6IXr0gqueGss_N3oTBj9jJliavg04_hkOhQ670MislNdEwnWkCsRPdvpyK2nPZfHcWtg7S039SnHp7EUjodPYTS1LKZRiu5vjTFM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!
ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟
به خاطرش حتی موشک به اسرائیل نزدید؟
(که اونهم اومد در پاسخ ماهشهر رو زد؟)
خب جنگیدید و شکست خوردید!!!
هم در لبنان،
هم ‌در سوریه هم در غزه به مردم گوش ندادید
جنگیدید و شکست خوردید!
۲- اتفاقا چون رفتید توی لبنان و غزه و…… دنبال کشیدن «دیوارهای آتشین» علیه اسرائیل و نابودی اسرائیل بودید، و افتخار میکردید که  بهشون
موشک میدید، از طرف دیگه دنبال اتم
و هسته‌ای بودید، اومدن و ایران رو زدن!
هم اونجا شکست خوردید و شهرهاشون نابود شدند
هم ایران داره نابود میشه!
نتیجه ۴۷ سال اسرائیل و آمریکا ستیزی شما!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6182" target="_blank">📅 14:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6181">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=BMKZk7d4TR23meNbWRX1PGkNu2Mn9teJhV2hIIhgRKy1SYX3rYHnGJAe8gGLd8D-PtWThWt7VYClK57lxResftgq0XPtbYAL56vh_8i4GGHrZ7vk8jjA2rUykCAgxcHGOepVtRIBP1_AiCyL2QWAh5RUq-gz76N9Ndey5V3ubO5EskhcL07BziIP2yR5LeDRGNyBaCzLtY-WCf5mKaFPfxjjjm6MuKqHWf2uTCUwTD16N2PKWvztZIOSq7HKJWcB3ap0DVc5AfCgq7ymGNbcbJLKYgFlYuTVmrLWccrNTcyYjrVRnu5bzy8Q9reFPl7XebH7z-qOncChdI-sImZ6Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=BMKZk7d4TR23meNbWRX1PGkNu2Mn9teJhV2hIIhgRKy1SYX3rYHnGJAe8gGLd8D-PtWThWt7VYClK57lxResftgq0XPtbYAL56vh_8i4GGHrZ7vk8jjA2rUykCAgxcHGOepVtRIBP1_AiCyL2QWAh5RUq-gz76N9Ndey5V3ubO5EskhcL07BziIP2yR5LeDRGNyBaCzLtY-WCf5mKaFPfxjjjm6MuKqHWf2uTCUwTD16N2PKWvztZIOSq7HKJWcB3ap0DVc5AfCgq7ymGNbcbJLKYgFlYuTVmrLWccrNTcyYjrVRnu5bzy8Q9reFPl7XebH7z-qOncChdI-sImZ6Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت وراثتی بود
یکی می‌مرد یکی رو به جای خودش
معین می‌کرد
مردم هیچ نقشی نداشتن!
میخواستن، نمیخواستن باید قبول میکردن.
🔺
خودش چطور رهبر شد؟
با نقل یک جمله شفاهی از خمینی!
گفتیم بعد از شما چه کنیم؟
گفت : همین آقای خامنه‌ای»
🔺
حکومت وراثتی بود : مثل پسرش مجتبا!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6181" target="_blank">📅 13:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6180">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdWJgw0PLVMOxf50UHNevQWUOdCA1CdoPX_0z9iz-k6WtSxMwBr-aofRD7f9ll804XH6DaZJ1ELPMlMpuhOQnPKs8JyErM6SWhuaCnSujCteOBMVuvkNkNqsxjOXPXySGGOdgs5Wed63LZG86_J18AVtM37nK8R9JL2eln5jndKb_Z2F0Mk6GRCcGBIBmjQI3MHl6PmdvkwKaEc1wqoPtN2NrIi7CnCROH_ihPKlNdTdlLFiPa-EfnTyD2FmHRdh3vsEarEd2154QrYQ6vziE-pVQ7MiObpIamq4JpHZvvkfnLFujZqg-RUS6KcumrSZuy2CxkqlN2y7LDvTImj9yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تاریخ هزار سال پیش نیست!
که هر چی دوست دارند روایت می‌کنند.
داستان همین روزها و جلوی چشم همه ماست!
گروهی برای خونخواهی خامنه‌ای
دست به حمله به اسرائیل زدند،
اسرائیل برگشت و ضربه‌ای بهشون زد
که یک میلیون نفرشون آواره شدن!
و همین امروز و بعد از ۵ ماه، هنوز نیمی از این افراد آواره هستند!
۴ هزار نفرشون از جمله ۷۰۰ کودک کشته شدن (خود قالیباف و خود حکومت گفتن اینها برای جمهوری اسلامی کشته شدند)
بخش بزرگی از جنوب لبنان رفت
زیر چکمه سربازان اسرائیل،
رهبرانشون حذف شدند.
دستاوردش چی بود؟ افتادن به التماس
و زور و خواهش برای «آتش‌بس»!
الان میگن این «اسوه و الگوی مبارزه دلیران» است!
این اتفاقا آینه عبرت و نتیجه گنده‌گویان‌است!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6180" target="_blank">📅 11:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6179">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d198d21980.mp4?token=KeLG4nrvOcrqw-ecUqQOZjSOFgxI5lJUni0cj1I4CP_UmpVt6El2b4Vn5tlOU31g3IOrk0-Z1D97UPEpNklg-SHmFK6ffKyH6yeZikVerP727AvhcXT3H_Rzrhjt3aDOJrWQrXOUU_uTABlVCDUTfmU0WZ16YoDv5GwjB403ZpdvA4qBKYr0CHXbb4AOkeiDt7W10XBJtYLrlq6yKpnplbDPed3A25hY_4wtEZLLCvATOsZTMHJ1mw9I4bBu3Al9cDGz8CbHpWsyJ1-L6Lt_S9mxwk8NRLezuwltOpeIopju7RKYAx7qGxJmxvKsH1BLnygm4M_Z-f7KMSIpnJehi4EroRuWm019d0RI5KVYJ8zkTnauORUvWhE3jsZt6U3dag6wVozCG1SkHLbOwVvktRSWMZQ1CtEcwA2qQfVOuenpO0VNN3iOT2NIiWwA2k88zywPdaOew_zzPpxfx4xWQt3ZeQ35Y2TlX03zqu2uh3bRU86xKa5mRW7o2i8VuUamuXIucXM5u252JvoVGB9WupXSWZsTf1Vhtj9NfVwygQ0lw-O1GSp9L5Za6be25TK00b9gdIblzB_LWSysxnagzjyI0e2_WNsWxWyIInOl03JXnCbJOpZvh1H1xREiUia1rkNRscZmbSLcQRiYbVl_B9RdGspN1nLKsC8VCBLIlu4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d198d21980.mp4?token=KeLG4nrvOcrqw-ecUqQOZjSOFgxI5lJUni0cj1I4CP_UmpVt6El2b4Vn5tlOU31g3IOrk0-Z1D97UPEpNklg-SHmFK6ffKyH6yeZikVerP727AvhcXT3H_Rzrhjt3aDOJrWQrXOUU_uTABlVCDUTfmU0WZ16YoDv5GwjB403ZpdvA4qBKYr0CHXbb4AOkeiDt7W10XBJtYLrlq6yKpnplbDPed3A25hY_4wtEZLLCvATOsZTMHJ1mw9I4bBu3Al9cDGz8CbHpWsyJ1-L6Lt_S9mxwk8NRLezuwltOpeIopju7RKYAx7qGxJmxvKsH1BLnygm4M_Z-f7KMSIpnJehi4EroRuWm019d0RI5KVYJ8zkTnauORUvWhE3jsZt6U3dag6wVozCG1SkHLbOwVvktRSWMZQ1CtEcwA2qQfVOuenpO0VNN3iOT2NIiWwA2k88zywPdaOew_zzPpxfx4xWQt3ZeQ35Y2TlX03zqu2uh3bRU86xKa5mRW7o2i8VuUamuXIucXM5u252JvoVGB9WupXSWZsTf1Vhtj9NfVwygQ0lw-O1GSp9L5Za6be25TK00b9gdIblzB_LWSysxnagzjyI0e2_WNsWxWyIInOl03JXnCbJOpZvh1H1xREiUia1rkNRscZmbSLcQRiYbVl_B9RdGspN1nLKsC8VCBLIlu4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو‌شب پیش شعار میدادن که
:
«
جنوب ایران نکند جنوب لبنان شود»!
حالا دیشب شعار دادن
«جنوب لبنان و جنوب ایران
اسوه! رزم همه دلیران! »
خودشون می‌دونن جنوب لبنان ویرانه است و
مر‌دمش هم‌ آواره! فعلا هم زیر چکمه‌های سربازان ارتش اسرائیله. برای همین اولش میگفتن
«نکنه مثل جنوب لبنان بشیم!»
حالا میخوان هندونه بگذارن که جنوب ایران «اسوه رزم » است و برید جلو!! بشو شبیه جنوب لبنان!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6179" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6178">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=gQaoAYWVaDThIrFT6v0SMdZMNkx4TA3jclUzJzT9SgLoVyYvzuBAs6Gqhy-_N1k277GGoVX_IbMcnKXIi2CDlrcALulHj5YDfNCoc5xEiJmSd-oCVl67n9jjSyZmYi0GvVBmGcUzDtZOUCBay9OlrZL-K82Y7uepqgS64LBzJHQ9T2STfxdAwJyXZOvWXqob52USmf2qIcnLulhQS5Nx2tPylu74o9IGWjepVmiuJHO9Dm0DqB6uePJagxSEdy8Tpqe3kmyGHlbVpYfzZvIFNgyCM44qLm0sepNM26eUD5tGSKyO_EX3uoUX02PkJRi-qDv_EmDegjDMFWulTVmJPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=gQaoAYWVaDThIrFT6v0SMdZMNkx4TA3jclUzJzT9SgLoVyYvzuBAs6Gqhy-_N1k277GGoVX_IbMcnKXIi2CDlrcALulHj5YDfNCoc5xEiJmSd-oCVl67n9jjSyZmYi0GvVBmGcUzDtZOUCBay9OlrZL-K82Y7uepqgS64LBzJHQ9T2STfxdAwJyXZOvWXqob52USmf2qIcnLulhQS5Nx2tPylu74o9IGWjepVmiuJHO9Dm0DqB6uePJagxSEdy8Tpqe3kmyGHlbVpYfzZvIFNgyCM44qLm0sepNM26eUD5tGSKyO_EX3uoUX02PkJRi-qDv_EmDegjDMFWulTVmJPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی از سخنان سردار نقدی : اگه حتی به آمریکا حمله کنیم، قدرت پاسخ‌گویی هم ندارند!
با کدام پشتوانه اقتصادی میخواهند بجنگند؟ با کدام پشتوانه مردمی خودشان؟ همه جا در محاصره ما هستند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6178" target="_blank">📅 08:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=Afv26odM7cLxGkFwFP2eXTMNbbXXXwkW7pfXSe2sUNJ2sSLE8VNlytz3sE7SzwVXmlbFwkLfFvcadCivvxBJqjpz2PIGAvLrBhYGjjD_kjx9CfdUBdvHTxNdiGBILgDfo8MPqZL8aI_0K8z-rXsKIaFvHENDyyErl2ttTMGH-24TqVOZoO7F5pF6z62p2b5XqNzLjGaTvROIGtN4-oxLFFQFV1Vm292FFEY5eGcGf3ceZUaSjH5QDDAtB0nTkdScDVh9vrmTAx09oI9MyaemqJToMJVEJCm8_bkom3Lb2ulmMHIJYCBCDn9OjTYV88patIy8OjIP2Weuzm2GfjsIvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=Afv26odM7cLxGkFwFP2eXTMNbbXXXwkW7pfXSe2sUNJ2sSLE8VNlytz3sE7SzwVXmlbFwkLfFvcadCivvxBJqjpz2PIGAvLrBhYGjjD_kjx9CfdUBdvHTxNdiGBILgDfo8MPqZL8aI_0K8z-rXsKIaFvHENDyyErl2ttTMGH-24TqVOZoO7F5pF6z62p2b5XqNzLjGaTvROIGtN4-oxLFFQFV1Vm292FFEY5eGcGf3ceZUaSjH5QDDAtB0nTkdScDVh9vrmTAx09oI9MyaemqJToMJVEJCm8_bkom3Lb2ulmMHIJYCBCDn9OjTYV88patIy8OjIP2Weuzm2GfjsIvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پل  کهورستان در اطراف بندرعباس
که شب گذشته مورد حمله ارتش آمریکا قرار گرفت</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6177" target="_blank">📅 08:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6176">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار …</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6176" target="_blank">📅 08:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6175">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0U_EV03l6hN6fSBEloHRSMdXvt-AQDCrioxAxL4daN53gLeS-G7IFuIYwMoYav9-xYxxZ8R0sedGTqwv0UFQF70JII-VgEczb2WO78y2luNQF-gXaJlpsJKT-EgQzhHLg64ATmrbTb6ZjTAB0f0nqgiJWFliHaxon2Q1WooQ0fuXxqZawswNYwktM-TNXowcq8t4w8WABfe7V76bob581Kp0Ptut1kVh4zljFIQS_YZJngZ4mg1vEJGmiU3FKnnzM5LesiOR6Y3EIhmBll4IwvzqweOgWXWBDEyXHXJJYDCN2wJGCZFh6OAJV9Vgy1rhuXzEf9JkeG3xHRRYhMk1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار - شیراز
🔺
تعداد کشته‌های حمله به پل‌های بندر خمیر به ۷ نفر افزایش یافت
🔺
تفنگداران آمریکا : یک نفتکش ایرانی را توقیف کردیم.
🔺
دیشب برای نخستین بار جمهوری اسلامی به خاک سوریه هم حمله کرد، هدف : پایگاه آمریکایی در التنف
🚨
تصویر : آمریکا برای سومین بار به برج مراقبت دریایی چابهار حمله کرد و این بار آنرا منهم کرد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6175" target="_blank">📅 08:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6174">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
حملات شدید به بوشهر</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6174" target="_blank">📅 01:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6173">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=XpBiLnfUjpyUonQrj87tJR6me_hKmc4t1Rn9laehi5Iw2XKuqLGdtoxDXSSbgcLCihO2DvAlpNcUUsNALmmoXoMhVOn2ttByyCNPhUUdrya0rCc_tUOjWdYLofIlUebC8AcORRcCZirUKnnp_tuA_4ZxR4xBHlg0Eyg_rMdnCFO8m8pB6kQnaJsJ4wPVA_EDWnvgX_sOXNX1FHN2Qi2YKvQT5kepAPIfnUVTIbzJvSZ8a3sXRAB49WxnPgD_U9eFw7TUaCPpNLE7VkCiHOnVQ0PhvwpeFrG2w9RQkjKKZKDQ4He2pm-4dsWiaJvd8eFuhYXTV2BrOqZ1aFeUWk90Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=XpBiLnfUjpyUonQrj87tJR6me_hKmc4t1Rn9laehi5Iw2XKuqLGdtoxDXSSbgcLCihO2DvAlpNcUUsNALmmoXoMhVOn2ttByyCNPhUUdrya0rCc_tUOjWdYLofIlUebC8AcORRcCZirUKnnp_tuA_4ZxR4xBHlg0Eyg_rMdnCFO8m8pB6kQnaJsJ4wPVA_EDWnvgX_sOXNX1FHN2Qi2YKvQT5kepAPIfnUVTIbzJvSZ8a3sXRAB49WxnPgD_U9eFw7TUaCPpNLE7VkCiHOnVQ0PhvwpeFrG2w9RQkjKKZKDQ4He2pm-4dsWiaJvd8eFuhYXTV2BrOqZ1aFeUWk90Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏فارس: جزییات حملۀ   آمریکا به پل‌هایی در شهرستان خمیر؛ ۲ نفر شهید و ۴ نفر مجروح شدند</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6173" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnrm30qJQkqF5qApZqNl9CvmFw6K4JQ8XNs_z-bM1_fVJIMVFvEmHU0mx5SYUyFvfOZpHGknRL0P5IWPaI1sbP3Xho6XqYTHgi11vVqJfZ38Q4JoFL2tq7m2AI-CAucaOPr5Li9toCgi0m7xkXexCpPCwwooDqUbSk6xKNX48EhbK5q-vDvoqs5yIdYPbOUeioDfjVhwNAZYeTldcu1Zz7eKYhUtdt46Ucx0_9vcRNnZ8wrWOuLE8RnQOUkYcu2h6jHgH7f1vT3cxDdMck3k8zntTdpStJr4o0XogD-ibZOJIDQdLazntsAXJl1mIU6NmA2v8TUvdF6jhWFJFDeSLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6172" target="_blank">📅 00:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6171">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
صدا و سیما :دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند.
بندرعباس مهم‌ترین دروازه واردات و صادرات کشور است و شبکه ریلی بخش بزرگی از این حمل و نقل را بر عهده دارد.
این حمله می‌تواند به حمل و نقل کالا ضربه بزند و به آن اختلال وارد کند،</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6171" target="_blank">📅 00:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6170">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
حملات گسترده به حمیدیه و شوش در خوزستان</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6170" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6169">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
حمله جنگنده‌های آمریکایی به فرودگاه ایرانشهر</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6169" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6168">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067abcc49e.mp4?token=sqNtSr3PmY7yJoVOHhaYlXRzRRN7bm4JiwtwdD4k0nMoe39ZyWD5VF_RMELJWy5h7f6iRRhwjvmBDdAPlL-V_csj-Bi-FEJPn7Cfham3JKUg2G6hH8uHrkpBFUCIOiRgYRLU-ld-0qxjmbt5Fq7fwNSccF155syWBcRsnWivoV1RgxRfEkR48MQMiI03n9xMvQO7HPUHAUwt-BPR5oeD6qkT9Ivxe7ba5s4b0zvctzdFpwNgZYsQ0aplVxtAka8QKssatOGsCoe-lu_-AlICaatCocizWBYaNDYhgNi-IsKwETIx37YLVo9iXU7TqyZITgqr53E4wd5LIvnEYJ6hBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067abcc49e.mp4?token=sqNtSr3PmY7yJoVOHhaYlXRzRRN7bm4JiwtwdD4k0nMoe39ZyWD5VF_RMELJWy5h7f6iRRhwjvmBDdAPlL-V_csj-Bi-FEJPn7Cfham3JKUg2G6hH8uHrkpBFUCIOiRgYRLU-ld-0qxjmbt5Fq7fwNSccF155syWBcRsnWivoV1RgxRfEkR48MQMiI03n9xMvQO7HPUHAUwt-BPR5oeD6qkT9Ivxe7ba5s4b0zvctzdFpwNgZYsQ0aplVxtAka8QKssatOGsCoe-lu_-AlICaatCocizWBYaNDYhgNi-IsKwETIx37YLVo9iXU7TqyZITgqr53E4wd5LIvnEYJ6hBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس
خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6168" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6167">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnqzGf11pGJOqmXQtwWc6PSkNb2mAuBAiCg3OPT34Ce42CplUs4Xb1lId52ruzWJfeLWMWbzW3QkiwLLFUd56h7c61NurtHNc6ZDlS6LgMOpPOrb_izFi45R8aw09HPJKwcCSXt874GR8zuOGpNEnNhkG--yAGmTwzYUvnv7cjlRp5STXr-z7rs5bFcxcsJo2j3ONhOfGa04QSEx5yOGln6OuLoMdQAiG0d7-5w1CMqE2-6ZhPB_UxDr9bAgFhdH7PUwFslInRRrwNzRc97DAvZ7qcd37Y-oLW6IP_1-QA3ynC1tYqdFZIqxPMvADnBr9rqUK9lxHLhMsQ2I6X1PTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اهواز تحت حمله شدید
حداقل پنج انفجار مهیب در اهواز
🔺
انفجارهای مجدد در بندرعباس  و قشم
🔺
انفجار در بهبهان
🔺
انفجار در بوشهر</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6167" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6166">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=mhjMzcT4Q7SLJpy1LgOSvWs4ZBbMff3FrWWBhwidnel5uRK1TzxX0Pa0mig6gU-rWhEnRQqC1oDzz2X-HphbLycAm2qhBrFDQekGWWjz2HLFBDJzSSyU4Sfpxj1wMC3as6f9hdvZZvMTC4vpOUQ5TFRoHPX2a64HF6Acq8D861YgSmcXdnifMquhYV6PGdZVy1E3Px_1K6CSQguugV02BTqP_hJ-OAXlcYhA0XcXRO_kTjPaV_Oq5f-a1Pi9HimStEfP-yCeyG6rhJMCwaSen_Fh6TN9VhH6sTeqeGT9IxBgGn4t_XSIF0-w7GUW7BUfEmGDpAUVwws5N9kdqLguSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=mhjMzcT4Q7SLJpy1LgOSvWs4ZBbMff3FrWWBhwidnel5uRK1TzxX0Pa0mig6gU-rWhEnRQqC1oDzz2X-HphbLycAm2qhBrFDQekGWWjz2HLFBDJzSSyU4Sfpxj1wMC3as6f9hdvZZvMTC4vpOUQ5TFRoHPX2a64HF6Acq8D861YgSmcXdnifMquhYV6PGdZVy1E3Px_1K6CSQguugV02BTqP_hJ-OAXlcYhA0XcXRO_kTjPaV_Oq5f-a1Pi9HimStEfP-yCeyG6rhJMCwaSen_Fh6TN9VhH6sTeqeGT9IxBgGn4t_XSIF0-w7GUW7BUfEmGDpAUVwws5N9kdqLguSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که گفته می‌شود
از حملات امشب به بندرعباس است.
دقایقی پیش بندرعباس ۴ بار مورد حمله
قرار گرفت.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6166" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6165">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏
🚨
🚨
سنتکام: موج جدید حملات در پنجمین شب پیاپی را شروع کردیم.
🚨
مهر: حمله مجدد آمریکا بندرعباس
در ساعت ۲۱:۳۵ نقاطی در بندرعباس مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6165" target="_blank">📅 21:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6164">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=vhHMd2ZtnRZd17-tgJbWp7eAxsPA5sCtsIXTLZlNSOHNVEHCjTLOWxhbSVfyK24Gu2XrVzcqth0rPNc9zCvbWYiEcpAv1Rtvb3QHxC2gdxbeH6Q0K0AyvlcYhYOIFM7adN9Po6RtfcrmC5B5Uwbqh8FV6wUVg_aoc1GgOnzHgPqFcXLgr7-H_AH6Cb08NjKTW7FSoyaYocb407UVetbxqwaob9mXhw9X5USvwIKllNEH83GW7hhZ6GymUSonSZ7YJXXnMptCFk9oDhElT7EB442rjlRy_s4QyhwbmVqMNJGEhDCQe6-V0zZK6gAZfD0U_NUSBwJUm7MNevWcUl4oew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=vhHMd2ZtnRZd17-tgJbWp7eAxsPA5sCtsIXTLZlNSOHNVEHCjTLOWxhbSVfyK24Gu2XrVzcqth0rPNc9zCvbWYiEcpAv1Rtvb3QHxC2gdxbeH6Q0K0AyvlcYhYOIFM7adN9Po6RtfcrmC5B5Uwbqh8FV6wUVg_aoc1GgOnzHgPqFcXLgr7-H_AH6Cb08NjKTW7FSoyaYocb407UVetbxqwaob9mXhw9X5USvwIKllNEH83GW7hhZ6GymUSonSZ7YJXXnMptCFk9oDhElT7EB442rjlRy_s4QyhwbmVqMNJGEhDCQe6-V0zZK6gAZfD0U_NUSBwJUm7MNevWcUl4oew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازغدی : اگر میخواهیم اغتشاش نشود
باید با آمریکا مبارزه کنیم
(که حواس مردم به جنگ پرت بشه
و تقصیر کاستی‌های حکومت بیفته پای جنگ
و دوباره جنگ بشه «نعمت» !)</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6164" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6163">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
استانداری هرمزگان:  در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6163" target="_blank">📅 19:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6162">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDyfd2wGA7AqBk7Nu5ggVRSdpafDEKtxNF8Wnu83RgoUVtJu_PZoaqJhhqd9pJgMPLVH6azDB7DsOmzqtpnNbGWIms_Blv8JpX5WrHwDU40l799cfAEj14Xy_cH77oxnGZCGtXzHZCtSUK-ChXvQQgmnZEYva35cw9YlsWoHSyNFtkAKSEtOPjzBAdC5N3lkbfsDM0oUb4WjmF-XraggF2lIvoZXkOdZdvhQB6RBwK9etqXSFQk_YDPgdfg9aiaBu2TJrEf1GRIgbHkERmgfHmyb2uOCVUDFnOFqCaqUjE4YUIyUnHjomNa5biJXo9YsfWGnXi_dPnLRqZvqi12I7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز :
پاکستان به ایران هشدار داده‌ که اگر به عربستان سعودی حمله کند، پاکستان آن را حمله‌ای علیه خود خواهد دانست و اعلام کرده‌: «این خط قرمز ماست.
»
پاکستان و عربستان قرارداد پیمان دفاعی مشترک دارند که بر اساس آن حمله به هر کدام ، حمله به دیگری تلقی می‌شود.
🔺
برخی اعتقاد دارند که یکی از انگیزه‌های اصلی تلاش پاکستان برای میانجی‌گری میان ج‌ا و آمریکا ، نگرانی از وقوع جنگی است که دامنه‌اش به عربستان برسد و پاکستان را ناچار به ورود به این جنگ کند.
اینک که تفاهم نامه کنار رفته، پاکستان بیش از پیش نگران این موضوع است.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6162" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6161">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
استانداری هرمزگان:
در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6161" target="_blank">📅 19:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6160">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=odTYSqMApeFPY7Ws3LYwEdDtCr4PAKpc1WF1v41-WwRQj1NXA8Mawe5r73_NVLAA-ZigfSxih1AzPsgWKZ3wV-Jer8RxRTaYiWCzoqCEE-CPfYExgiAu8607-nRwlUUMl0QjSs-Iie3V4kXOr4ZTGE6ZOJJQBXEvbN5ptDZy1o5-Nv3caKCdEPT1OZFkr4wWjao8NjA9M4raaS-SrrCqyvdHvwjMu4ulWkfw18RHTMraOIjLHqbjQLEGURy8gF2JFXjEbw6GBubCwF6_s_Mx5qZw9cmuE9ApKhe1tImAqvx_DCPwA7NXWDaQ-3lKfUo75XCR3igaax7aAZVP820OawWPMIqzf65D7VhnMFgdoWHRDcYDIjoGDASpEKe-9PBriUtiCGtweOfbVaYWW_br4eA1PDxkkK5g7N7J1Aw46ea8Sfpm__XghkzZTEf1pTkbfxNHkEeEdvU4PhgSkvasQYe52PVhztC_KtjJgqghL4V9EoMMNSC1XQebYvOmamqu0pQHRrGjahLwkWV65GRWeHDKLR0W_MrO8sByBDEcsZvr7hJsaFnu7hFF69WbDlsEe5pJZ11ofwsdu1gckyCTyeCyYw6c7MJHXOqWsa7TCRDEFCtEFaPSekbkxW1WwD60cgO3wFddqMXoVqnKvH_fZQsmCPjz-vgNM0q1h9WPlgM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=odTYSqMApeFPY7Ws3LYwEdDtCr4PAKpc1WF1v41-WwRQj1NXA8Mawe5r73_NVLAA-ZigfSxih1AzPsgWKZ3wV-Jer8RxRTaYiWCzoqCEE-CPfYExgiAu8607-nRwlUUMl0QjSs-Iie3V4kXOr4ZTGE6ZOJJQBXEvbN5ptDZy1o5-Nv3caKCdEPT1OZFkr4wWjao8NjA9M4raaS-SrrCqyvdHvwjMu4ulWkfw18RHTMraOIjLHqbjQLEGURy8gF2JFXjEbw6GBubCwF6_s_Mx5qZw9cmuE9ApKhe1tImAqvx_DCPwA7NXWDaQ-3lKfUo75XCR3igaax7aAZVP820OawWPMIqzf65D7VhnMFgdoWHRDcYDIjoGDASpEKe-9PBriUtiCGtweOfbVaYWW_br4eA1PDxkkK5g7N7J1Aw46ea8Sfpm__XghkzZTEf1pTkbfxNHkEeEdvU4PhgSkvasQYe52PVhztC_KtjJgqghL4V9EoMMNSC1XQebYvOmamqu0pQHRrGjahLwkWV65GRWeHDKLR0W_MrO8sByBDEcsZvr7hJsaFnu7hFF69WbDlsEe5pJZ11ofwsdu1gckyCTyeCyYw6c7MJHXOqWsa7TCRDEFCtEFaPSekbkxW1WwD60cgO3wFddqMXoVqnKvH_fZQsmCPjz-vgNM0q1h9WPlgM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی جدید جمهوری اسلامی</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6160" target="_blank">📅 19:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6159">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=CDsKr29eJKBypqWA2eyiBIbQDUGWipMZwl0Eb5sLjisxK3Gf16K7F-Udg70vN491GDNjiUFliBLfbyf2G5o2xYHSN0zHzdobmX5zQJd19R8rPM7Pt-JtI1gNKlY5aoy3UB3V0ns7lG2znlNDMOgQZP3zj1JSEufcV2NaxYzk445u3AZUhRJ50mu4pooMjLuQw6SP11sKNZKiHFA7PEeyBc4926OaCFhq-pDWikVQfx8A8Okr3k8-vTZl-xh6zD_uq8_dB9Ix3oJno4zIGBuU4hjaT8Hl_5RaHh6HKEEqjV3juiPEFWFZWEnfhony-YmAFtuTrCEFCZRkLAzIjGL3ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=CDsKr29eJKBypqWA2eyiBIbQDUGWipMZwl0Eb5sLjisxK3Gf16K7F-Udg70vN491GDNjiUFliBLfbyf2G5o2xYHSN0zHzdobmX5zQJd19R8rPM7Pt-JtI1gNKlY5aoy3UB3V0ns7lG2znlNDMOgQZP3zj1JSEufcV2NaxYzk445u3AZUhRJ50mu4pooMjLuQw6SP11sKNZKiHFA7PEeyBc4926OaCFhq-pDWikVQfx8A8Okr3k8-vTZl-xh6zD_uq8_dB9Ix3oJno4zIGBuU4hjaT8Hl_5RaHh6HKEEqjV3juiPEFWFZWEnfhony-YmAFtuTrCEFCZRkLAzIjGL3ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، تیر ۱۴۰۳:
ما غنی‌سازی را ۲۰ درصد کردیم جنگ شد؟ ۶۰ درصد کردیم جنگ شد؟
hafezeh_tarikhi</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6159" target="_blank">📅 18:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6158">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ایران که ۴۷ ساله که در آتش فتنه اینها می‌سوزه</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6158" target="_blank">📅 17:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6157">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سخنگوی قرارگاه خاتم : هر چه در منطقه سالم مانده از نجابت جمهوری اسلامی است!
ذوالفقاری: «همه آنچه که بنا به نجابت ایران هنوز سالم مانده، یعنی تمامی زیرساخت‌ها در منطقه، زیر ضربات پولادین نیروهای مسلح مقتدر جمهوری اسلامی در هم کوبیده خواهد شد؛ آن‌چنان که اثری از آن‌ها بر جای نماند و گویی از ابتدا وجود نداشته‌اند.»
سخنگوی قرارگاه مرکزی خاتم‌الانبیا همچنین دخالت آمریکا در تنگه هرمز را «خط قرمز شکست‌ناپذیر» جمهوری اسلامی خواند.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6157" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6156">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=l5hfB8x0m8QiHmLQiScmj_dSq0b2BYRypCRkzME5zCFI3GRHTzqM4SS0287Ph4odxForhZuDOFPLlKnn4y9NChWdwk8SMlL5Vfmm3UW9PcEH8H_NcDWmAz_6uJb0H_7O-PSy0Eo-WjX4CKFqBLs3Yrb4ygMms3zkmklFVF7m6e1FggGpdQ0Zqn2_Ux1HSKp9bYfVNZmTlO1UUTK3uZcg9csbKiCx3lLMcMBDmWq7Tcj544hsU-9_dgXczfdavDpbaKzrnowHNN0gADnKM5im9rDFn_mBDWhCBsPHLwmwrtYhG-6qcfhyM3DtQi3VaXas569VHNW9bUMhUEiorwURMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=l5hfB8x0m8QiHmLQiScmj_dSq0b2BYRypCRkzME5zCFI3GRHTzqM4SS0287Ph4odxForhZuDOFPLlKnn4y9NChWdwk8SMlL5Vfmm3UW9PcEH8H_NcDWmAz_6uJb0H_7O-PSy0Eo-WjX4CKFqBLs3Yrb4ygMms3zkmklFVF7m6e1FggGpdQ0Zqn2_Ux1HSKp9bYfVNZmTlO1UUTK3uZcg9csbKiCx3lLMcMBDmWq7Tcj544hsU-9_dgXczfdavDpbaKzrnowHNN0gADnKM5im9rDFn_mBDWhCBsPHLwmwrtYhG-6qcfhyM3DtQi3VaXas569VHNW9bUMhUEiorwURMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شب گذشته ج‌ا به اربیل در عراق
علی‌الزیدی نخست‌وزیر عراق با صدور بیانیه‌ای،
این حمله را محکوم کرد.
در این بیانیه آمده که «به آژانس‌های امنیتی
مربوطه در هماهنگی با نیروهای امنیتی منطقه دستور داده شده که همۀ تدابیر لازم برای ممانعت از تکرار حملاتی از این دست، و نیز مقابله با هرکسی که به‌دنبال خدشه‌وارد کردن به امنیت جامعۀ سرفراز عراق باشد را اتخاذ کنند».</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6156" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6155">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqaiUwzzebYRJTJdLh_4-ILXZpcYnMtOYAHN12E0BGgErvG-mSidPtnTHr0zNeHhqX03o3fEJ6SeYXLF9mNCx6B4qgVa2orBREkMiezwZx4K3KhVC6IFRzwuoEfFdhrq1CFQbCD5A4gdcu7R2WM3ISkyZQK5O79hy5z0S3qgsrSQ64uXj5GMcrb8CXH30VTf7OKSXYk4Q6-Eex36D54dlXvciEIGfhvavFpUsCZTAlAs4BPZrgIUPsMLwqZ70i-OY2Rj2D8rupRYzXEWXGEeQL3wbtbT8dbxt5RlxFz6R6IVGa0JeEOb5u1RggvneUg69AsKPkUGqXeMuiktqcokHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وراجی نکنید  بگذارید بجنگند که صلح بیارن :)  مثل صلحی که ۴۷ ساله در لبنان  ‌ و غزه آوردن!  انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6155" target="_blank">📅 12:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6154">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">وراجی نکنید
بگذارید بجنگند که صلح بیارن :)
مثل صلحی که ۴۷ ساله در لبنان
‌ و غزه آوردن!
انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6154" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6152">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=ePLDZM0nyU-Uhxp9hx2b_KxRDzP5fbejFsjjHzz8QNDRnKFg-N01eWjHAx3SO0xBBk_Hfiu_2m5NFAFkKc6yDxxsZilsWWks0qm7wPNiilLR6jHz26Ms0rrluWIKhXNpD6OcHrN-DBgmJ8snTAnEkm73mbi3CLbYMxyN0N7ZOJjsejyhXFf4jRu-CGM9DQat0hD8HkhYDN7lE5y_xRwJM6dCRfXXEz3n-lGg1Y93UcGFmFfoH9llkbhao_BKI85HobxDxl2P5bPJevvPzPLCqIowUbc4JrpoE3j2CfiblMUu1fzi53Bz9cNDWas14s9n2lpzXndQISddbbPqUF3KNRZZxwrG5bWQ8a-inB2cN3VI1aT1zGhkLWKfNbLFuVVnDng2pupPLgLgBvK2r14t9qiUE5VwPwPHnIS6m4PNIpz2ECHogv_Y5PvdCGmzTsPyZTJkuIqCBuOpq7e5R7FWdEL5ycwafKfzXV6A_pEnQUqabU0zuog3kBedLANjH6PfMO7YGy9dNlgTsRyQ14GumHc9r1DQCXty03N1Mmt5p5d0WV2St-CbtVaNKSe4iO-mQd6PoAS_Fk07VSSDVDwlticTGvni1jzsnx4Bsn8_txQdSXJrp8l2YsmFN26MWuDYgyWzVbegpb3YdI9AL95ZnmyAx3WKNxtBzQWcSGz0BTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=ePLDZM0nyU-Uhxp9hx2b_KxRDzP5fbejFsjjHzz8QNDRnKFg-N01eWjHAx3SO0xBBk_Hfiu_2m5NFAFkKc6yDxxsZilsWWks0qm7wPNiilLR6jHz26Ms0rrluWIKhXNpD6OcHrN-DBgmJ8snTAnEkm73mbi3CLbYMxyN0N7ZOJjsejyhXFf4jRu-CGM9DQat0hD8HkhYDN7lE5y_xRwJM6dCRfXXEz3n-lGg1Y93UcGFmFfoH9llkbhao_BKI85HobxDxl2P5bPJevvPzPLCqIowUbc4JrpoE3j2CfiblMUu1fzi53Bz9cNDWas14s9n2lpzXndQISddbbPqUF3KNRZZxwrG5bWQ8a-inB2cN3VI1aT1zGhkLWKfNbLFuVVnDng2pupPLgLgBvK2r14t9qiUE5VwPwPHnIS6m4PNIpz2ECHogv_Y5PvdCGmzTsPyZTJkuIqCBuOpq7e5R7FWdEL5ycwafKfzXV6A_pEnQUqabU0zuog3kBedLANjH6PfMO7YGy9dNlgTsRyQ14GumHc9r1DQCXty03N1Mmt5p5d0WV2St-CbtVaNKSe4iO-mQd6PoAS_Fk07VSSDVDwlticTGvni1jzsnx4Bsn8_txQdSXJrp8l2YsmFN26MWuDYgyWzVbegpb3YdI9AL95ZnmyAx3WKNxtBzQWcSGz0BTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگر نوحه میخونن و مداحی و رجز خوانی و.. برای کودکان غزه و لبنان و میناب و….. از تاسف از دست رفتن زندگی نیست! میخوان در این جنگ بی‌‌‌‌پایانی که با جهان دارند،  از جمله و در صدر این‌جنگها،  با خود مردم ایران جنگ دارند، سربازگیری کنند! تا نیروهاشون بزرگ‌تر…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6152" target="_blank">📅 11:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6151">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تمدن اسلامی! تا زمانی که توی مدینه و مگه بود قادر به ساخت «توالت» هم نبود!  مستراح هم نداشتن !! اما دنیا در چه وضعی بود؟  ۶۰۰ سال قبل از تولد اسلام!  توی بیشتر شهرهای جهان  داشتن توالت عمومی! اجباری بود!   اینها میشینن روی منبر  میگن «مدینه فاضله»!!  حالا…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6151" target="_blank">📅 10:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6150">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تمدن مصر باستان رو مطالعه کنید ابتدا تا انتهاش بر مدار مرگ بود! فرعون از زمانی که سر کار می‌ا‌ومد به فکر مقدمات مرگش بود و قبرش بود!  هنر و پزشکی و علم و مهندسی مصر همه بر پایه صنعت مرگ بود!  مومیایی و اهرام و جراحی پزشکی و….. همه برای کار و کسب مرگ بود و…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6150" target="_blank">📅 10:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6149">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDy8Dk9bteURFe6iiUcRtu2azyAZkbXDBL7ygbZxY1Ylc3SFtBOP9612yPcUXgpe2MLMdmDVWjyfCY86HJKBIvFot83MHZWwSPyNDHshN7uSFr4Xj_kbeEFoW7eDd9AYu3trYtxVeQd_2NVMb1ZyL5QDnMeZA3z9zKAoXkwEWJyH3uXtkHWr2VTsfzqcpKnvCIg4vfB0kfztsSmkG0eL6G0nVcbCqZQrrnCOgpdMwfMFbMKQHNTVbyHGKGG3lLfDsQO3NyXxJoDl4L5OluiO_sa4YCRpcL1xbqSkU_Ls7Ulho1YipJtc2lb6bMeeY5fZepyyahfQBWYvzeItj_Hk1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها شنیدید جملاتی با این مفهوم رو که زندگی و این حیات «زندان مومنه»!  آرزوی اینها مرگه! مرگ براشون رهایی است!  اینکه برن و برسن به بهشت و به زندگی!!  مرگ رو آرمان خودشون می‌دونن و زندگی و زیبایی‌هاش  رو پست و حقیر معرفی میکنن!  و اینکه باید دائم به فکر مرگ…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6149" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6148">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..  سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند. و از مرگ متاثر میشن!  تمام هستی اینها :  مبارزه، جنگ، کشتن،  کشته شدن و….. است!  زندگی براشون چیزی نیست جز  «مبارزه  برای عقیده».  و خوشحال میشن…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6148" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6147">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=Vkj-QiV4pgcR4mAYnMZeb_bHcDb567M26waGlvM7kE3gDtglqSwpnEzthF9KZnl4t-fcbD3qj_9m9gHKZ-k2TTQshRHHg2pPN-mWdiVKBdoJc2c_JLxGtn1Om4dGJeTeIWj17h6kvhUjBVRuzGo5j2kT8kAHBA_lfq8KbJMdIK5saa28mlSKjEL5kgjzpiMgXR3zCp2WODQHo2CqlU8EB9qsbokIBg_alWEAfcxG62W0MBaI5VBiPiYKkorqquolLr_QcvVIQ_X3Tjf1PNn_uXMfFmSiJ1l-8jofVG8iM-hXp2silu5hzAX0qni3WmEnrm4N9s0kje37ISH5MXARHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=Vkj-QiV4pgcR4mAYnMZeb_bHcDb567M26waGlvM7kE3gDtglqSwpnEzthF9KZnl4t-fcbD3qj_9m9gHKZ-k2TTQshRHHg2pPN-mWdiVKBdoJc2c_JLxGtn1Om4dGJeTeIWj17h6kvhUjBVRuzGo5j2kT8kAHBA_lfq8KbJMdIK5saa28mlSKjEL5kgjzpiMgXR3zCp2WODQHo2CqlU8EB9qsbokIBg_alWEAfcxG62W0MBaI5VBiPiYKkorqquolLr_QcvVIQ_X3Tjf1PNn_uXMfFmSiJ1l-8jofVG8iM-hXp2silu5hzAX0qni3WmEnrm4N9s0kje37ISH5MXARHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..
سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند.
و از مرگ متاثر میشن!
تمام هستی اینها :
مبارزه، جنگ، کشتن،  کشته شدن و….. است!
زندگی براشون چیزی نیست جز
«مبارزه  برای عقیده».
و خوشحال میشن اگه زندگی رو به خاطر اون عقیده نابود کنن! زندگی نیمی از مردم جهان هم نابود بشه براشون مهم نیست!
چون «برای یک هدف بزرگ‌تر»! مبارزه میکنن!
پس چرا مثلا روی مدرسه میناب مانور میدن؟
چون میخوان شما رو بیارن توی صف مبارزه خودشون
برای اون هدف بزرگ‌تر !
برای جنگ‌های بی پایان تا رسیدن به هدف بزرگ‌تر!
اینها نمیجنگن تا در این دنیا آرامشی باشه
و صلح بلکه میجنگن برای آخرت!
برای اون دنیای دیگه مبارزه میکنن!
از این زندگی و این جهان متنفرن!
این زندگی رو فقط یک پل می‌بینن! یک فرصت برای مبارزه و کشتن و کشته شدن و….. که بعد توی اون جهان به آرامش برسن! این زندگی فقط عرصه و میدان جنگه براشون!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6147" target="_blank">📅 10:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6146">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSvbdmyiNayFbT2gi68ZgjZUhNZtmL1ykJCYQ0whsxZ58x3ogbsOU7y4gfe6YQiyvvLprxMM-wz5JpHdXKmQ59uX1soBwK3BEZAohY3uetfJZuAaOTFq1F4gi4s6IzVrGrxuLVTBtMByImipewGe3GRSk5t_BoCgY-IiYvfkjSQblC5Dljmf-5aBruFtKHEEwbm0j3boIc7E1hdNjx5lZdtuin1Ze70U5lQDUX1mgBt5FuB-CAFN4O2xkqCCRdMKvTYl7CntSoRALJGGTNXKtQd5dZ0_7HLqje6TncKJWLWR8nYbE3OQ2tFc6OxrA2LTLYCKClNTIreTwiuUzJkkYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران به یک شهروند زن آمریکایی که در دسامبر ۲۰۲۴ در دوران رئیس‌جمهوری جو بایدنِ خواب‌آلود به‌ناحق بازداشت شده بود، اجازه خروج از کشور داده است. او اکنون در سلامت کامل در خارج از ایران است. ایالات متحده آمریکا از این ژست حسن‌نیت ایران قدردانی می‌کند.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6146" target="_blank">📅 09:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6145">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
حملات دیشب به استان‌های خوزستان، سمنان، مرکزی و لرستان
🔺
دیشب تعداد زیادی انفجار در اهواز شنیده شد. برخی‌ها تا ۹ انفجار و برخی تعداد انفجارها را بیشتر تخمین زدند.
🔺
گزارش‌ها حکایت از آن دارد که یکی از موشک‌ها در اهواز و در نزدیکی یک بیمارستان (بقایی) اصابت کرده.
🔺
دیشب همچنین به چند نقطه از استان لرستان حمله شد، برخی گزارش‌های تایید نشده از حمله به پایگاه موشکی امام علی در لرستان خبر می‌دهند.
🔺
استاندار سمنان نیز گفته که به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.
🔺
استاندار مرکزی: شب گذشته به دو نقطه در اطراف شهر خنداب حمله شد. این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقاً مشخص می‌کند چه اهدافی را زده و نه ج.ا می‌گوید به کجاها حمله شده.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6145" target="_blank">📅 09:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6144">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">استاندار مرکزی : شب گذشته به دو نظقه در اطراف شهر خنداب حمله شد.
این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقا مشخص میکند چه اهدافی را زده و نه ج‌ا می‌گوید به کجاهاش خورده.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6144" target="_blank">📅 08:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6143">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اطلاعیه  ارتش:  سامانه‌های راداری، سامانه پدافندی پاتریوت و مخازن سوخت آمریکا در پایگاه علی‌السالم کویت را هدف قرار دادیم.
‏ رادار‌های سوپر هاوک، تأسیسات و سامانه‌های پاتریوت واشنگتن در پایگاه شیخ عیسی بحرین نیز طی حملاتی، آسیب‌های جدی دید.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6143" target="_blank">📅 08:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6142">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
استاندار سمنان : به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6142" target="_blank">📅 08:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6141">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhirCBq94DZ0U9ZwhhIN7dcZ6SMMX--oWjh83anhnXnaFjvjERPEnVjG9miC0WRwBsrQwz81mGSR1C8ehH_2gH08y518evy6hqLLT-3txT8RtZSCxGHjUD5zm8MbbD1RRAcZSoSYM8kVmvV_J-sGykQ_f0o-ituMjGYo60pPY9kua70QxJ3Rm5V6NaWTOpRUfeUOn2yxG827DMug2xTW2ktog34J7F3Bs9PYQSTRZT9uYMvrljEpOb790SZOvpXtGbr7oGPT_UkBNyPpHveuHfTdiC1sAm5nGuoo4_P9Z_ECZPK5XYKi8rXkA6tIVcEEko5HKCpTOolr5Lk4KyGhrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین یارو خودش از دست سپاه و نهادهای زیر نظر خامنه‌ای  فرار کرده و به آمریکا پناه برده!
و آمریکا رو خونه امنی پیدا کرد برای زندگی و نوشتن از اینکه اسلام چقدر زیباست و خوبه و سعادت انسان رو میخواد!
حالا از همونجا به ج‌ا میگه مبارزه کن با آمریکا! مطلقا تسلیم نشید! تا انتهاش برید!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6141" target="_blank">📅 08:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6140">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">برخی گزارش‌ها از تداوم حملات به اهواز خبر می‌دهند و اینکه تاکنون ‌۹  انفجار  مهیب در شهر شنیده شده.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6140" target="_blank">📅 23:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6139">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
چندین انفجار مهیب در چابهار و بندرعباس
🚨
کویت : امروز ۲۱ پهپاد و ۴ موشک شلیک شده از سوی ج‌ا را منهدم کردیم.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6139" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6138">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای ۲ یا ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6138" target="_blank">📅 22:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6137">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWMMrTu7cD1A3nTrRrD5fZ5ZPTwV9sGXTDDgxDvP7I-v6lVFWZs7N4Ta0nYCNy4RCCN44CtqxplZe48svodUhM4NA9kZJ-vMKQWJd8fbJRnagAWME7IMw00iW5ICmX2oFX5eGolIbPWdy4G1BrvNvUGLz3zvNubT7Hx9Lu9HPXVlStlPjoJeUy8UlOAYB83nOkCRwlT6X8PsMRnpx3FIA0bPftKHTOMbM1bfEL0OUgPVD--HrgYeMJ54eVL8oaVapfeC2W4cTRjmKl1tRIBasGtosdu722JNkqfQqSiWptfKnTsHa5YiSMOjmJWys_n9Js2L_3aTak-9u79wtDQ7tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما دیگه جرات حمله به اسرائیل
رو ندارید! خودتون هم خوب می‌دونید!
این ۴-۵ روز هم به همه جا حمله کردید
به جز به اون کشوری که بیت‌رهبری
رو زد نابود کرد!
و نشون داد دقیقا کجاست که سست‌تر از لانه عنکبوته!
ولی هر چقدر دوست دارید شعار بدید!
اون حزب‌الله تروریست هم رفت انتقام بگیره  هنوز و همین امروز هم نیم میلیون نفرشون  توی محله‌های مسیحی و سنی لبنان آواره شدن!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6137" target="_blank">📅 20:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6136">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">آنچه شب گذشته در بمپور رخ داد و موجب  کشته شدن تعدادی ای نیروهای ارتشی شد، قابل اجتناب بود.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6136" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6135">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e615d142.mp4?token=NeBvukwHtxldh40KIdK2TUWD05OoqZnKwi86gSv-eG-EQgP8sWx8tW4v4kuxCNafRCoANPbu9uk6rnfX5wNQuiBqbg9RBegT84hJAS7hwkvDs2OCK-xSjbEGktdTS1s8FFMhKYbXjRFE2tpUQi2HEez_NXQ2EznfMkzXhNIozsxY_X30BODa3ZtPrMG6bdKkW4J6KL9TaG4DY7OS0MV8NUha0TX_WtWoQl4WZja0n9g6leyaETsL4BUI1Pbf6Rc6s6Xs5uVqj7YXyE6PqhMp6W7IEbn7NwJm6ZN5A8q3TPvybeBmhDRWwzphCFEVy4xu-HBAnip76TQeT50aPS6XGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e615d142.mp4?token=NeBvukwHtxldh40KIdK2TUWD05OoqZnKwi86gSv-eG-EQgP8sWx8tW4v4kuxCNafRCoANPbu9uk6rnfX5wNQuiBqbg9RBegT84hJAS7hwkvDs2OCK-xSjbEGktdTS1s8FFMhKYbXjRFE2tpUQi2HEez_NXQ2EznfMkzXhNIozsxY_X30BODa3ZtPrMG6bdKkW4J6KL9TaG4DY7OS0MV8NUha0TX_WtWoQl4WZja0n9g6leyaETsL4BUI1Pbf6Rc6s6Xs5uVqj7YXyE6PqhMp6W7IEbn7NwJm6ZN5A8q3TPvybeBmhDRWwzphCFEVy4xu-HBAnip76TQeT50aPS6XGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش بینی تاریخی بختیار
در دو کلمه، برای مردم ایران</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6135" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6134">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=heBYvznXLkADTeglJ4dGkjBSgJbFf8r8kNU_6KZexxk4ljQxU0nBkNluUUJt5h-1k-W9IXZAd2WCB50ssFUaTOWhHEWKDV7o-JPHZmO3z2igKGLE6vcWolQMctkASMWUj75-AIWlwU3HwOtJUF9UVHdVHLDt95WuwL2gwsHrCAZI_JWMSZah6ZDnNrY51hxrK8qxt_5zc7r6_YhdlMcMkWncWPYOYu4FF-5Vw6ROhEsrjAh9E62AsZUC-_4f30wIJfr0kvz2BXEqyEcgEVGI-dA1TLDXANB8hiHR4RG7xENmigUEBj-u-f7_aZEol4a3525nN0s0Phk9TR0F6nP_QIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=heBYvznXLkADTeglJ4dGkjBSgJbFf8r8kNU_6KZexxk4ljQxU0nBkNluUUJt5h-1k-W9IXZAd2WCB50ssFUaTOWhHEWKDV7o-JPHZmO3z2igKGLE6vcWolQMctkASMWUj75-AIWlwU3HwOtJUF9UVHdVHLDt95WuwL2gwsHrCAZI_JWMSZah6ZDnNrY51hxrK8qxt_5zc7r6_YhdlMcMkWncWPYOYu4FF-5Vw6ROhEsrjAh9E62AsZUC-_4f30wIJfr0kvz2BXEqyEcgEVGI-dA1TLDXANB8hiHR4RG7xENmigUEBj-u-f7_aZEol4a3525nN0s0Phk9TR0F6nP_QIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی که فرمانده سپاه بود و سالها فرماندهی جنگ رو بر عهده داشت
اینجا میگه مطئنم که مسیری که در ذهن مجتبی خامنه‌ای است، بهتر از مسیری بود که شورای عالی امنیت ملی رفت.
مجری ازش می‌پرسه خب اون چه مسیری بود؟
میگه : نمی‌دونم ! نمی‌تونم که ذهن خوانی‌ کنم!
فقط می‌دونه خوب بود :) یه مشت چاپلوس !</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6134" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6133">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9M_YUZGueQqm0ixH_mjoF0hRFaP_VCg4R0tXN4JS4I0yo_H8xKl9ae5qXm7PkoChrqIiIcBzuy-W2bnq2vn8vKSbdIOXHkfZVC4EXeTV2VPKc5NESCGLJkgIPXtpUK1Vl6Vffzfg9kYsyvT3L-RwsqKEW8q637KpTVLZd6EimFBDpOx80WhtzwDwvmlkxUMMAtNyTdRcMdUxmop5zkk9bwPFrjXUXOBBe54Ju72asFYH1G91yhixJiWhXiDUUDFDHIG1uT2SeRMrNFdFeDcxRRYhdDlBGSeeC2fdTHlZATQ18bGVeesXwplVuJVh1dcNt8QGprOL-806kIcmeb2JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی از اجرای حکم اعدام محمد امینی دهاقانی، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، خبر داد. مقام‌های قضایی او را به آتش‌زدن فرمانداری و کلانتری مرکزی شهرستان دهاقان در استان اصفهان متهم کرده‌اند؛ از روند بازداشت، بازجویی و جلسات دادگاه و … محمد امینی دهاقانی خبری منتشر نشده.
براساس اطلاعیه منتشر شده در خبرگزاری میزان، ارگان رسانه‌ای قوه قضاییه، حکم اعدام محمد امینی دهاقانی پس از تایید در دیوان عالی کشور، بامداد امروز ۲۴ تیر ۱۴۰۵ اجرا شده است.
در این اطلاعیه آمده است که امینی دهاقانی روز ۱۹ دی ۱۴۰۴ با پرتاب کوکتل مولوتف به ساختمان فرمانداری دهاقان باعث آتش‌سوزی شده و سپس یک کوکتل مولوتف دیگر نیز به سمت کلانتری این شهرستان پرتاب کرده است. مقام‌های قضایی همچنین مدعی شده‌اند او در تحریک معترضان برای حمله به کلانتری نقش داشته است.
دستگاه قضایی جمهوری اسلامی بخش عمده پرونده را بر اعترافات متهم استوار کرده است. در اطلاعیه رسمی ادعا شده که او در بازجویی‌ها پرتاب کوکتل مولوتف به سمت فرمانداری و کلانتری را پذیرفته و همچنین گفته است قصد داشته از یک قبضه سلاح کلاشینکف، که به ادعای مقام‌های امنیتی از ماموران گرفته شده بود، استفاده کند.
محمد امینی دهاقانی همچنین به «بازنشر و ارسال محتوای تبلیغی علیه جمهوری اسلامی، تشویش اذهان عمومی و برهم زدن امنیت روانی جامعه» متهم شده است.
او همچنین به «درخواست ارتباط‌گیری با حساب‌های کاربری» مخالفان جمهوری اسلامی و «درخواست ارتباط‌گیری» با صفحات مجازی مرتبط با خاندان پهلوی هم متهم شده است.
مقام‌های قضایی هیچ اطلاعاتی درباره نحوه دسترسی متهم به وکیل مستقل، شرایط بازجویی یا روند برگزاری دادگاه منتشر نکرده‌اند. همچنین مشخص نیست اعترافات منتشر شده در چه شرایطی اخذ شده و آیا متهم امکان رد یا اعتراض به آن‌ها را داشته است.
اعدام محمد امینی دهاقانی در حالی انجام شده است که نهادهای حقوق بشری بارها نسبت به افزایش صدور و اجرای احکام اعدام برای معترضان و متهمان پرونده‌های امنیتی در جمهوری اسلامی هشدار داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6133" target="_blank">📅 15:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6132">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
سنتکام : به تنب بزرگ حمله کردیم.
در جریان این موج ۹۰ دقیقه‌ای از حملات، با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی و محل‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را مورد حمله قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6132" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6131">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حمله امروز به چابهار</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6131" target="_blank">📅 14:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6130">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
ارتش: «آمریکا بامداد امروز با شلیک ۱۳ فروند موشک، آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور را هدف قرار داد
دشمن به مهمانسرا و اماکن نگهبانی پادگان حمله کرد
‏ ۷ تن از کارکنان پایور و وظیفه تیپ ۳۸۸ ایرانشهر شهید و تعدادی مجروح شدند.»
‏</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6130" target="_blank">📅 14:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6129">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
سنتکام : از نیم ساعت پیش موج تازه‌ای از حملات را آغاز کرده‌ایم.
(از  ساعت ۱۳:۳۰ تهران)</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6129" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6128">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcR5trkK7SePkB1YiE-eVCiJiwqvs8Y8c8yqO0Izj8qjId3mxonBhVkz49ukL_4Md2UqjlcLkaY-0lsNq9l-X6QR6OJ5kASXkm4kcAZJEiBKkqOyShyRQjE7yPyDmA-4egnYOCsj1-FFkZjYlUmuozLxt-6F9r3goMt4RzH8dmFhlHv7UCNpIja50x8mKYBs3kc24-TkE5zqfPQSw7_l8FFvUEjGnB9tzRm2bZvhOK1-nrblP4d2RDxYptt1xmOZGLlJtw-MPTV2Qp-HgF5_BzzFIXXa5mhzXhf_e4EoQ3fluE2sJvDvVDvurIbeSfNyGGvDO6ZdM4htGmVTLHvyZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابل توجه ساختاری‌های محترم
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6128" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6127">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=TRjp6l-dY_hK9tQ5fd1xgBSIvKozC3KYN3LNhaUwmnfrplLwEXw6anAEwFauco9HOAJ0uy5F2yYRP-bz3-sMvjHgGvSdUBAJfqbpj1q5kyVmWh2j6E4s3diC6labX-OPuC_MkJaQmUU0I0mgY_NGeEOwS0XQmKpUhsumnx9-jpNu7qIgqxBwjkHTtFBCLsVPWemLV7C85DVnu6mGoCwt77EvwMTMHkBRp_S_DsGpq8-ecK1WrzN9ANfc8jw_GTm0DCS0GIhCNUSlkfF2PQZFb8_QIe8SQjko8K5yqR_oRKr7bXg0B3zsc6lDwFttcP0ZKuQ7RMh2A1wvAqh2fdeQNn4kCU5RdOP6Qe9T3D6e_1KIEQDHwSsYiyXp4VDwc89Grsj6t-h1ceSI4cvq1nmxvYXVqqTStIbLsYnQeC54tPtgJRrGxmc57HH5etjoyGT5HDtnT0Cza91Pwbt80P6llChdfrJQjt5d5DK0N-DTxVafeyh_W04ZitvM-wnSYlpvxRLXm6pdcRyzunF-v1arMpD2SyhdpB1Yt0RQD6i2j2nBG3P2FACt8COtTJLgYKWZr_i9FVYpFrEmoi8cbvuWnDdGb1t_POPiF-H7L8Hl-FZ7EBtzLaIf2bwXzf2hB8kOGlFMnQqsRUSYvKwUx6xERFNJ8biG76KMS1LeQcoIqWc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=TRjp6l-dY_hK9tQ5fd1xgBSIvKozC3KYN3LNhaUwmnfrplLwEXw6anAEwFauco9HOAJ0uy5F2yYRP-bz3-sMvjHgGvSdUBAJfqbpj1q5kyVmWh2j6E4s3diC6labX-OPuC_MkJaQmUU0I0mgY_NGeEOwS0XQmKpUhsumnx9-jpNu7qIgqxBwjkHTtFBCLsVPWemLV7C85DVnu6mGoCwt77EvwMTMHkBRp_S_DsGpq8-ecK1WrzN9ANfc8jw_GTm0DCS0GIhCNUSlkfF2PQZFb8_QIe8SQjko8K5yqR_oRKr7bXg0B3zsc6lDwFttcP0ZKuQ7RMh2A1wvAqh2fdeQNn4kCU5RdOP6Qe9T3D6e_1KIEQDHwSsYiyXp4VDwc89Grsj6t-h1ceSI4cvq1nmxvYXVqqTStIbLsYnQeC54tPtgJRrGxmc57HH5etjoyGT5HDtnT0Cza91Pwbt80P6llChdfrJQjt5d5DK0N-DTxVafeyh_W04ZitvM-wnSYlpvxRLXm6pdcRyzunF-v1arMpD2SyhdpB1Yt0RQD6i2j2nBG3P2FACt8COtTJLgYKWZr_i9FVYpFrEmoi8cbvuWnDdGb1t_POPiF-H7L8Hl-FZ7EBtzLaIf2bwXzf2hB8kOGlFMnQqsRUSYvKwUx6xERFNJ8biG76KMS1LeQcoIqWc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سفیر اسبق جمهوری اسلامی در روسیه: مطمئن باشید اگر ترامپ را بکشیم نه تنها هیچ موشکی به سمت ما شلیک نخواهد شد، بلکه عقلای آمریکا با خوشحالی جنگ را تمام خواهند کرد.
کشتن ترامپ هیچ هزینه‌ای برای ما ندارد و با کشتن او جنگ هم تمام خواهد شد.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6127" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6126">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟  به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6126" target="_blank">📅 08:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6125">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qggd54izZ42UdpAbSo1vJpxVed7B3AU7VHZLW7xR2hmZk-UvQ-6PLE330cPhYm9dlls7R52AQ9U2apcUAyCF1okEjNZWHDIgBSQZdyau9dzfDPQFr8f-LAqnZWFt8VWYchqNpb6sZBkbDjVZQzi_cbcgYY3siYjBnG9hBAk6LFnKqwIaqXZyEwa7BBn0HtDxiNe8p05vh-iS8J4WbJQX5WyZ3j901a_0PMn4LH3sTrtDVMEzJZ4ETDI-Jk4_S4gl3VWpcE5oZssOCtFmHQCmb49y8BDWoYbtuq9YXqFkk3GK82zUz6apjVRwkCy5skbDKgm5uk6DR-fNS6YGnngErg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟
به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت کاخ سفید برگزار کرد.
به گفته سه منبع آگاه، در ابن جلسه که ارشد‌ترین مقامات نظامی و امنیتی آمریکا در آن حضور داشتند در خصوص گسترش حملات صحبت شد.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6125" target="_blank">📅 08:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6124">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=ftzrVPCGUjms8upJYiWhbV53NCWlmh2E6IG6fZ_NW_OHHTjKLiKddKaFZS99j6g-r_GeKAOdaFpUjuNia7HtL-_vsGMTnC4_4RaFub23HtHQdJP_nbsR6JLDoJPdY8zQOZGfPjBflU3MR87JAZQm_z3Fn3ctAO2E5FGjNGkpnYvTYmApLoFQ1JK8BV9TT8lj_eBpMukV9vciPrvbI-3ukFeDj2_KtzErZaI6mqchhW0qTtEB_-2ykwLKpGpe-w_nobY5GrhEerDGWtt3o-90mStvZXNdBy9ibX2QxfuFa5y4AxTqAK_1uynFRLBquSUUrNtfiQSxM1-rTGOhFV7AlZ2CgA_D2UIINU_3abBMruEL6xkEtBR7AhrMfDGaBJknMHe3O2xDIh8iQuCsYGy2sz42ptS1OCBHL88EBCKPu6OQY_VgbVQ0bpw500yBP1ovv_cC3wb-G7r9Hu7RLVnPpSiHfi9kpKyFQF_3ofjkis2kdRC1zLFs-ohNL2cTCwPptg2f61bNejBEEuML1P0P-3BpvR3vbrP__LzoNZfK6cGo7SHwooUo0mymvSSzlrAdjNLZ8Vs5lpfx2zRhgWgRmEDzle64lbWz2EBt3SfEgWKHo5O8p0x7054azfANLZp4wYcWUbIk8pJmJU5ZrfSLKI0RUNyenNro2NRzfiufpyE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=ftzrVPCGUjms8upJYiWhbV53NCWlmh2E6IG6fZ_NW_OHHTjKLiKddKaFZS99j6g-r_GeKAOdaFpUjuNia7HtL-_vsGMTnC4_4RaFub23HtHQdJP_nbsR6JLDoJPdY8zQOZGfPjBflU3MR87JAZQm_z3Fn3ctAO2E5FGjNGkpnYvTYmApLoFQ1JK8BV9TT8lj_eBpMukV9vciPrvbI-3ukFeDj2_KtzErZaI6mqchhW0qTtEB_-2ykwLKpGpe-w_nobY5GrhEerDGWtt3o-90mStvZXNdBy9ibX2QxfuFa5y4AxTqAK_1uynFRLBquSUUrNtfiQSxM1-rTGOhFV7AlZ2CgA_D2UIINU_3abBMruEL6xkEtBR7AhrMfDGaBJknMHe3O2xDIh8iQuCsYGy2sz42ptS1OCBHL88EBCKPu6OQY_VgbVQ0bpw500yBP1ovv_cC3wb-G7r9Hu7RLVnPpSiHfi9kpKyFQF_3ofjkis2kdRC1zLFs-ohNL2cTCwPptg2f61bNejBEEuML1P0P-3BpvR3vbrP__LzoNZfK6cGo7SHwooUo0mymvSSzlrAdjNLZ8Vs5lpfx2zRhgWgRmEDzle64lbWz2EBt3SfEgWKHo5O8p0x7054azfANLZp4wYcWUbIk8pJmJU5ZrfSLKI0RUNyenNro2NRzfiufpyE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مزدوران حکومتی شعار میدن
«جنوب ایران نکند جنوب لبنان شود»
عجب! شما دیگه چرا؟
خامنه‌ای میگفت «جنوب لبنان الگوی پیشرفته
و موفق مبارزه ایمانی است»! سالی یک میلیارد دلار از اموال ملت ایران رو میدین به گروه‌های تروریستی اونجا  و تبلیغ اینکه ما اونجا پیروزیم و …..!
ولی ظاهرا اسرائیل در جنوب لبنان چنان درسی بهتون داد که الان خودتون هم میگید نکنه بشیم شبیه اون «الگوی موفق»! معرفی شده توسط خامنه‌ای</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6124" target="_blank">📅 07:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6123">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=B0m3hKy_c2BJxPm-ZZKdntKcirvGEzi-FYHxOmYQUPpTPMC-daY5XcR6k4CvVMGbeq43UNtkUWmRT2SctuMNYLsIdOGIXCH3O2TWKk18rdeKVAFnd5QHmU9wxXV2O6NgxKUp03cs7Hh-lfJs2ICy0E-evSuDBJbmZAhTplpxXEQFGGA2Ucxus0FbCorPH8QiT2g_o-S_GZIzjTBMgdYGHi3uAnLjR7Mnt1T8ceUZZxl3mbUG1SZkVGE46gsi0D72Hyu0pXfA2EFYz_SUuNo8VwB7dsCxlrbJ3M2pOs7DerlZzAlz1PV0_Nl9TIkey0q2HSNUccpJAq5X1lMJ8atdbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=B0m3hKy_c2BJxPm-ZZKdntKcirvGEzi-FYHxOmYQUPpTPMC-daY5XcR6k4CvVMGbeq43UNtkUWmRT2SctuMNYLsIdOGIXCH3O2TWKk18rdeKVAFnd5QHmU9wxXV2O6NgxKUp03cs7Hh-lfJs2ICy0E-evSuDBJbmZAhTplpxXEQFGGA2Ucxus0FbCorPH8QiT2g_o-S_GZIzjTBMgdYGHi3uAnLjR7Mnt1T8ceUZZxl3mbUG1SZkVGE46gsi0D72Hyu0pXfA2EFYz_SUuNo8VwB7dsCxlrbJ3M2pOs7DerlZzAlz1PV0_Nl9TIkey0q2HSNUccpJAq5X1lMJ8atdbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6123" target="_blank">📅 07:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6122">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=AHgfNLgiizWVvsPwxE32o02N6uVJiguwZb0LiapOAHzFJFHX6b-sGBM2OcoCfFN7m2QHF2b9W3wS_azi9qgdWOBiFnnBW1eSGGmkIQlKhgAFn588Dx-7_eJ4hsK2dYBPQ6dW9DVCyrYR3MCD0nK5gX2Zb9X-XWehuB8WFbBjVsTGActgkfL2UVceouMr_6fxuaecCrR1qElrMteD2KQX-fnSg539W9KPUpOaP7P8GkXme9bnLGlJWaE7NSBYnwKURuln5-zeyS3j5muVHYgzritHC-7aGu78NytZyslEMO0xhlI0X8hBOcz8QHDjFvAa-wtQXSQI3G2ADf37wglgjoeDnKlMRJHc9oEj-z6hi9_iJNt4GYIAjJ4m6gKbKN_DgHvnz7Y_qhkOXu3cak_0XXQxTsei5sCwTxovXnUqH8RcuHTlLB2a1H3uwsEPMNel8jwE50FxmQnujjijxQ_eeKpa9MqX6lqD1zOiVAZOZo1oD1gMadBoNfgqyOKhXIaH7bF_XoC8Cs7YYAb0LN8neh9V1kRFmg9UVXIpfN_HSpbs4ue6MHhTE7znyKRARuarBoHq9xVS3vGsT9Dibs2IG5kCuRkd5PuyVUtCif-qV1WkBajfeea6SoW2Er1WkZXTsWQprTMJGcZiXi4SP9req018_8TJsdaufuHq2WN2wCU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=AHgfNLgiizWVvsPwxE32o02N6uVJiguwZb0LiapOAHzFJFHX6b-sGBM2OcoCfFN7m2QHF2b9W3wS_azi9qgdWOBiFnnBW1eSGGmkIQlKhgAFn588Dx-7_eJ4hsK2dYBPQ6dW9DVCyrYR3MCD0nK5gX2Zb9X-XWehuB8WFbBjVsTGActgkfL2UVceouMr_6fxuaecCrR1qElrMteD2KQX-fnSg539W9KPUpOaP7P8GkXme9bnLGlJWaE7NSBYnwKURuln5-zeyS3j5muVHYgzritHC-7aGu78NytZyslEMO0xhlI0X8hBOcz8QHDjFvAa-wtQXSQI3G2ADf37wglgjoeDnKlMRJHc9oEj-z6hi9_iJNt4GYIAjJ4m6gKbKN_DgHvnz7Y_qhkOXu3cak_0XXQxTsei5sCwTxovXnUqH8RcuHTlLB2a1H3uwsEPMNel8jwE50FxmQnujjijxQ_eeKpa9MqX6lqD1zOiVAZOZo1oD1gMadBoNfgqyOKhXIaH7bF_XoC8Cs7YYAb0LN8neh9V1kRFmg9UVXIpfN_HSpbs4ue6MHhTE7znyKRARuarBoHq9xVS3vGsT9Dibs2IG5kCuRkd5PuyVUtCif-qV1WkBajfeea6SoW2Er1WkZXTsWQprTMJGcZiXi4SP9req018_8TJsdaufuHq2WN2wCU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا میبینم راست میگه …</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6122" target="_blank">📅 07:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6121">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1VAijvUWWsUgLDuuhNfM5J5qIqPgznsuYjjuX2QUwaJn8HHFbpuIROFCb-hfpw_3jjCIy8VQjnrOUEFnCXMRtCJWPpF6Z9OmaaYoWoOzyRsGMlcxr7U4mH7Qhf1GQjmymzDgGEzFWbfzOps_xk-WVkUUS3_KiKBSGi0mzMXs-39PkCZPzLcgg9jNid1smvqTtwMpCROLE1MAFiS3A_728RrRvRxlPrYsSCQgCdTByDdmOMKhK9PQRe5rM4D6ByQwrVBXEWgIUfE9yrhCZ7720hClix6a2IpdIvndemRoTkA0qs75bGcsxC08yuUaJg_X0nDSYKb49iTwgBhEjs9-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6121" target="_blank">📅 06:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Grxnna3nn131lNWCHxF9Mh3eSpyWLs7H-5rR__AOtZm4Sv3wrCzvsngJdXVm9XzUTy5a4KF4JMFNoK6QlpQOuV5LaiEkvauaiBCYaElDRdd8diOaQ-ReTYKKvP7ZjoDzBRyygnNFqBhUR1QomQQq_Lx23f5fbrXHB3Ds0l-4_Ha30AFN5_Ax4aZiatB7rt76extI4TzEyrv3nxIYtpi3IF5s_0jiyFdNb6yxaCvjrM2Kdm4gIbf0B07rD5mDjvkdI2CmlsGXTmMoc6FlCZevkHmjE5C3ZIfxcU_BakAdnCp5C2kdojX2onwfsYIE_c2kJKISS4AAabIXSzSrYPB00w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6120" target="_blank">📅 06:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6119">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=mMt_vZjzuRcYV7mKiEMeVmsLuF8i2e0RnlleDFxGXLo4jOf7k-jegOos1AjGKcXIaMjUI708BrLaKW82hXIqmfqTTVAzdfiHwsQm-7zGWY63qdgUCCNdJQrQqW2GKZDT32n-X_PuFpuMCgDm2un13kI1c9hOHP8J6nUP8oUmcGtZxlTv8-qlkVQGGRrvpDHbLk8EpOA64wTICNDHE9iL2SmkZtIIfijb9CtLyOJuyOcElhlHsx7YhNsjyxLfQ7Oy8xDSYRpZ5MJS4nUIUEZWyC4Fg9JVZfcwsbU7CM0BAwWpiRLVso5W4XLplNJLrqkTtBIFmdZaAETN19JuZcUlnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=mMt_vZjzuRcYV7mKiEMeVmsLuF8i2e0RnlleDFxGXLo4jOf7k-jegOos1AjGKcXIaMjUI708BrLaKW82hXIqmfqTTVAzdfiHwsQm-7zGWY63qdgUCCNdJQrQqW2GKZDT32n-X_PuFpuMCgDm2un13kI1c9hOHP8J6nUP8oUmcGtZxlTv8-qlkVQGGRrvpDHbLk8EpOA64wTICNDHE9iL2SmkZtIIfijb9CtLyOJuyOcElhlHsx7YhNsjyxLfQ7Oy8xDSYRpZ5MJS4nUIUEZWyC4Fg9JVZfcwsbU7CM0BAwWpiRLVso5W4XLplNJLrqkTtBIFmdZaAETN19JuZcUlnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام فیلمی از حملات خود به ایران منتشر کرد.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6119" target="_blank">📅 06:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6118">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=ex4SGO-29JqSlhGV-6QPYSk64r4QaeXVJRYTfIW6oxseVwSQr-Bbx3IDstgFz87ax9FSEA8QkRCbSSGrbejSgnwHdRaJr-s14A8CDl6cwNw5PdLME5NqbaXwL02EWZ2RHaK0UGBd7TZJ4x7WM6LNAksl0TjwDcDSmyeOd8h6X2a7GIIT7Lb1lM9ZS3EPLORrDhraYWEdTZ3w5z8wALxvS1E5SiUsP_P9C4LSUiJbL101qUtjgQck0cyuCNETb8AO8GKk2W-hOEsXg8iiYCHnirRKWiyPo4QasLeaOSSSIgzVVnOys3k7J22uJGMRkeAwhx6thySAhXcV0R4ttElM_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=ex4SGO-29JqSlhGV-6QPYSk64r4QaeXVJRYTfIW6oxseVwSQr-Bbx3IDstgFz87ax9FSEA8QkRCbSSGrbejSgnwHdRaJr-s14A8CDl6cwNw5PdLME5NqbaXwL02EWZ2RHaK0UGBd7TZJ4x7WM6LNAksl0TjwDcDSmyeOd8h6X2a7GIIT7Lb1lM9ZS3EPLORrDhraYWEdTZ3w5z8wALxvS1E5SiUsP_P9C4LSUiJbL101qUtjgQck0cyuCNETb8AO8GKk2W-hOEsXg8iiYCHnirRKWiyPo4QasLeaOSSSIgzVVnOys3k7J22uJGMRkeAwhx6thySAhXcV0R4ttElM_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : امشب، فردا و فرداشب به سختی به آنها ضربه خواهیم زد و هفته آینده پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد، مگر آنکه  مذاکره کنند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6118" target="_blank">📅 06:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6117">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caeb092620.mp4?token=eyYbv7bnh5myzumfLlKTkbdld0mHqgu4iPfAuF0KNuNHlADNwnkj3cz51BZrwSSxroZpDuk4tJ_ozlnWF4b-CiKA7Xb2uTpQLSDFxNHY97AovanXdmLNNxBJGLceHjceUEcZ0TEtDvK1-9zDV6euHZ1-n13K3mNYQzdnQ0NB5iahGu-YjtdBVYiCgSDSiYgG4Y8W3XYWeddxju3RHjWXfB_iocPTUIW5M5CCTKLi-jNPPw5NZoBzPV43Q44INvSpZY1HWPJnyojwYhWK-P9pPcnHDIyWJ0h3GiwhFEE-gw1O5Zas1fIyOndkPjmdd4672nvcdGzj_0l4BMxftcJIBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caeb092620.mp4?token=eyYbv7bnh5myzumfLlKTkbdld0mHqgu4iPfAuF0KNuNHlADNwnkj3cz51BZrwSSxroZpDuk4tJ_ozlnWF4b-CiKA7Xb2uTpQLSDFxNHY97AovanXdmLNNxBJGLceHjceUEcZ0TEtDvK1-9zDV6euHZ1-n13K3mNYQzdnQ0NB5iahGu-YjtdBVYiCgSDSiYgG4Y8W3XYWeddxju3RHjWXfB_iocPTUIW5M5CCTKLi-jNPPw5NZoBzPV43Q44INvSpZY1HWPJnyojwYhWK-P9pPcnHDIyWJ0h3GiwhFEE-gw1O5Zas1fIyOndkPjmdd4672nvcdGzj_0l4BMxftcJIBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ناشی از حمله پهپادی امشب سپاه به کویت
گفته می‌شود مخازن سوخت ارتش آمریکاست.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6117" target="_blank">📅 06:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6116">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360d24e506.mp4?token=NlDg_CsoBEqc8xP_aydq1IH-04KgJP5DRB7moFW-IySDlnswlMhuHi57SlCMBcc-Dzdfk-wxa9_FaiP73cGlXoKuAnjBw0U1mbLHKj6UjnkFUeHCScftxdNf0wfxLDAflJhOggS_tovp8v8drHTGaD9k8jKOvktcjjdk3MlqlxV22_s1rcxsYgT-O4iwkm45TcG-WToVZpMgdkPPaFTMp7GBJOlEnrnVMSAhNBMqWAwUTX36YfWLz45P7IKwmQHaJyFXX89ufOxwKMRNn4Blg5zuJNg4mZeTj3Ujewe9z8GNOXilqP1a2bddvUhv8_Nl2Ff0wtA_U-4xFdLgBr-Hdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360d24e506.mp4?token=NlDg_CsoBEqc8xP_aydq1IH-04KgJP5DRB7moFW-IySDlnswlMhuHi57SlCMBcc-Dzdfk-wxa9_FaiP73cGlXoKuAnjBw0U1mbLHKj6UjnkFUeHCScftxdNf0wfxLDAflJhOggS_tovp8v8drHTGaD9k8jKOvktcjjdk3MlqlxV22_s1rcxsYgT-O4iwkm45TcG-WToVZpMgdkPPaFTMp7GBJOlEnrnVMSAhNBMqWAwUTX36YfWLz45P7IKwmQHaJyFXX89ufOxwKMRNn4Blg5zuJNg4mZeTj3Ujewe9z8GNOXilqP1a2bddvUhv8_Nl2Ff0wtA_U-4xFdLgBr-Hdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی با موشک‌های حاوی بمب‌های خوشه‌ای به بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6116" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6115">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
ارتش : به پایگاه‌ها اف ۱۸ های آمریکا در اردن حمله پهپادی انجام دادیم.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6115" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6114">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏امشب اتفاق جالبی افتاده، به محض اینکه خبر انفجاری در شهر و استانی منتشر میشه، مسئولان جمهوری اسلامی سریعا مصاحبه میکنن و میگن دروغه و همه چی آرومه!
‏اینطوری مثلا میخوان صورت مسئله رو پاک کنن.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6114" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6113">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5cCJCl3Ei_c7NiPeyjfIBvE_r6OC916TWoZ6M8U32sk4bwQPEKN0JGoq1c0gaoZ54V7_TdHQ8BByvxx5Sy648Acl0zhK8r8JLIkTPuydNQgX9v2ZqFLpr6t43SmYE_fFvBhak-A2JnMdNEu09u6eAs2HTM1r9m2mOgrlntNmYBvkkhJkmd0KjM1UfTIPE1Rw0NKz51eSWcpUSax3ewA8nOOw1sHbIKLCq9LTTFlqxhv4xccp_5ATnZRCC8he1xOsQEcxTJIZzqS2svhYjQGYq6UmMtBPuthnwRcaBM_GoJXGDRJ2pbq9ujuXwtGrV_q-eltcjvH6eI0SmwhBG0cmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگارهاشون می‌نوشتن که کشتی‌ها دارند  از مسیر عمان رد می‌شوند، تشییع جنازه،  بریم و کاری کنیم که  کشتی‌ها مجبور بشن از آبهای ایران رد بشن  و شروع کردن به حملات به کشتی‌هایی که از مسیر آب‌های عمان میرن.  به زور حمله میگن کشتی‌ها باید از مسیر ما رد بشه.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6113" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6112">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJhI9eVc0jy11PVWbn2PCl-1fBo2AQ7oxFu49G-R3vWULleqkh-rjYIIZ4HjMb3Ge3CDbJxw-B_IsE1-Qc2j14qnfCcehgZrZWZ2y0oY7_90I7s-DRKj9Hc0SbBBWv3fDsjz06g29ZF38M85mp5Zr3Nm0S5_PklzRjb1_5TOph-Ztt5AAzwf6gPSlEYlRTaP1P3x6pXwuGlfFKSzZz4zCEv-JdEAD3BUCapjKCBR5JBAUL0T05HfFjokV4v99BJLSuxHS3Sjz40Ou0XpOJK5phDRtHmTUhsq2oITyTSinKJ8NFvHxZRsY1tP8LvgQPP5lEmQaMtI8WWoeW5Y3vATcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا در حاشیه خاکسپاری جسد خامنه‌ای و جلوی قالیباف شعار میدادن «مذاکره با دشمن خیانت است»  هنوز به سه کشتی حمله نکرده بودن و نزده بودن زیر تفاهم نامه</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6112" target="_blank">📅 00:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6111">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=H83kYye5_a-ZMAJfMWkyR_Fqw2B26w-W3IKu1WDL99GS2q7jmLM3AegwhGPZULL7uGtmKC2SI_7J4HFjRX8UFMANOI07qPbrZHU6CwbXrUPkzehlyDgD55nUjyNqpWkgGJaFaxeA_nJnzIZG_E0AkwsmsIpdCCHXN6CUgPR3DJS3nJGri2tyPXrFzKjSwamXHhsbsKb8wyyy9bQbMttZRpuCkXURiWqDkPauz_NReJLb1kj-Ih7M2LUtGpHxKuDx0bsmfaR914xprSxCq4MsfkpZSmxiWcR66DY7T_LA5B6c-G6l14kdPxvsp1NG76yOFYHWuu1bLgaMC7efYK0SPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=H83kYye5_a-ZMAJfMWkyR_Fqw2B26w-W3IKu1WDL99GS2q7jmLM3AegwhGPZULL7uGtmKC2SI_7J4HFjRX8UFMANOI07qPbrZHU6CwbXrUPkzehlyDgD55nUjyNqpWkgGJaFaxeA_nJnzIZG_E0AkwsmsIpdCCHXN6CUgPR3DJS3nJGri2tyPXrFzKjSwamXHhsbsKb8wyyy9bQbMttZRpuCkXURiWqDkPauz_NReJLb1kj-Ih7M2LUtGpHxKuDx0bsmfaR914xprSxCq4MsfkpZSmxiWcR66DY7T_LA5B6c-G6l14kdPxvsp1NG76yOFYHWuu1bLgaMC7efYK0SPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این استوری رو ۶ روز پیش گذاشته بودم  میگفتن آمریکا میخواد آتش بس حفظ بشه ولی جمهوری اسلامی باید «کار دیگر» بکنه!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6111" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6110">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550f13e765.mp4?token=tvRUVEt2Si0sVbksWXMMiy6YMpd1t99QCx79j7c5Yc5WED2UfDQ_lXfpjKzLUU5OypPynOPeM3FeFhYQViJus9MCzqybiTDdfzoCshCZrcFfLcKxSm1xbmdcHmxmfUCvDSb4sUpb8svrhmlV4u30IaW9kidWWQ35WhIrD71K4uoHs-6l_9K1QhqTsPHntFakAV24C5rOzqO_u4J8nctzzdE_ZdcDHInQyWIkfhH1m3HLUI5EAjmTmM7cvRl1Wa1caNZq7Miiat5JqhfCEELQnTAVrDZayEJA0wme4kfaOhg1fwGJ8P33Q0BYz0QyktyEM4vEZy6nqwwYEPHzGpfhW4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550f13e765.mp4?token=tvRUVEt2Si0sVbksWXMMiy6YMpd1t99QCx79j7c5Yc5WED2UfDQ_lXfpjKzLUU5OypPynOPeM3FeFhYQViJus9MCzqybiTDdfzoCshCZrcFfLcKxSm1xbmdcHmxmfUCvDSb4sUpb8svrhmlV4u30IaW9kidWWQ35WhIrD71K4uoHs-6l_9K1QhqTsPHntFakAV24C5rOzqO_u4J8nctzzdE_ZdcDHInQyWIkfhH1m3HLUI5EAjmTmM7cvRl1Wa1caNZq7Miiat5JqhfCEELQnTAVrDZayEJA0wme4kfaOhg1fwGJ8P33Q0BYz0QyktyEM4vEZy6nqwwYEPHzGpfhW4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو رو دو هفته پیش گذاشته بودم.  معاون سیاسی نیروی دریایی سپاه اینجا در جمع حامیان حکومت بهشون میگه خیالتون راحت باشه، حملاتی که ‌ آمریکا انجام  میده «واکنش»  به اقدامات ماست!  «کنش» نیست!   تمام این ۴۷ سال همین بوده!  یه کاری میکنن ، تنش راه بیفته،…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6110" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6109">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6109" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6108">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=mTpM2XFmISj72R2nGGHdks3t0LMhAq89VG8_x8DaiW7SYpebSgCsl-5glukWM1HBMhGBv2o_nYu1Ha79Eb_iNGvCU2zNyglnxEd7n53yiudNRQH4-14nRiHURZ6yhKetDAdZLgfMHvJXVgotknckOc3BU-r8mTEDp_t7HpXAdOZwc2QdiztAUBhBh9CqY7p0_LIK1k_DOxpixfiOuCUhiWi2Nx6Vd_0M-MHmSeGsvgcvVl6IjjyMdydx8ddMqyCJoFsyi_5I7owlKrGt4yqVUZXfLiKC-PIqGHKvSOa2iqRim2rEZ7v8OUHlvApSbub2ypkLlRA0s9shA6HayCKU0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=mTpM2XFmISj72R2nGGHdks3t0LMhAq89VG8_x8DaiW7SYpebSgCsl-5glukWM1HBMhGBv2o_nYu1Ha79Eb_iNGvCU2zNyglnxEd7n53yiudNRQH4-14nRiHURZ6yhKetDAdZLgfMHvJXVgotknckOc3BU-r8mTEDp_t7HpXAdOZwc2QdiztAUBhBh9CqY7p0_LIK1k_DOxpixfiOuCUhiWi2Nx6Vd_0M-MHmSeGsvgcvVl6IjjyMdydx8ddMqyCJoFsyi_5I7owlKrGt4yqVUZXfLiKC-PIqGHKvSOa2iqRim2rEZ7v8OUHlvApSbub2ypkLlRA0s9shA6HayCKU0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گشت زنی اف ۱۸ آمریکایی بر فراز چابهار</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6108" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6107">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا : محاصره دریایی ایران وارد فاز اجرایی شد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6107" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6106">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
چندین انفجار در بندرعباس
🔺
چندین انفجار در اهواز
🔺
پنج انفجار در قشم</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6106" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6105">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xj2tyxYJUz3dcpxyt65-n-NCc0RS7zZ2jbF1v-HyuwobhMMzDlBunJ5-F-rfgSuC2_btTnnVHGMrEkqoNVBtV5QZ9fmEp7TrNGNVDOLmfOwG0whK2HeExt7-vcFN_EOOfCZP2-WQazk8x-IQfyp1I-nqlAax0zGOehSzjAyao06z7RcDqrl3hU6bUdIMugFDqYZp6EW4uy_vLUob7TMUKQV5MK37BqcPq3_8sAFXuv8H8dfV7B3t6bTDxFUO3HQDJ-XU2fTS9IKb-6nPutt7tjLxvX-ZDGeV_-eXS98cyaLyxY5xZKqjI3h-TmjhEr8mjEDsO0Q_m5EuGiPI0QotNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2077085449948938568?s=46</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6105" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6104">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
دقایقی پیش : حمله به قشم و شنیده شدن چندین انفجار
🔺
حمله به یک نفتکش اماراتی در سواحل عمان
🔺
فعال شدن پدافند در کویت</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6104" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6103">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
ترامپ به فاصله ۲۴ ساعت، از ایده گرفتن ۲۰ درصد سود از کشتی‌های عبوری از تنگه هرمز کوتاه آمد.
«به لطف نیروهای نظامی آمریکا و همه اعضای قدرتمندترین نیروی نظامی جهان ــ با فاصله‌ای بسیار زیاد نسبت به دیگران ــ تنگه هرمز برای تردد همه کشتی‌ها باز است، به‌جز کشتی‌های ایران. و این هم به خاطر رهبری دروغگو، خشونت‌طلب و شرور ایران است که این کشور را به سوی نابودی کامل سوق می‌دهد.
بنابراین، ما
یک محاصره کامل
اعمال خواهیم کرد، اما
تنها علیه کشتی‌هایی که به بنادر ایران رفت‌وآمد می‌کنند یا هرگونه محموله مرتبط با ایران حمل می‌کنند.
بر اساس گفت‌وگوهای بسیار سازنده‌ای که با رهبران خاورمیانه داشته‌ام، تصمیم گرفته‌ام
کارمزد ۲۰ درصدی بازپرداخت به ایالات متحده
را با
توافق‌های تجاری و سرمایه‌گذاری
که کشورهای مختلف حوزه خلیج فارس در آمریکا انجام خواهند داد، جایگزین کنم.
این سرمایه‌گذاری‌ها عظیم خواهند بود و در عین حال برای خود آنها و آینده‌شان نیز فوق‌العاده سودمند خواهند بود.»</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6103" target="_blank">📅 18:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6102">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LA58kYe0lpohWbGgjhxl-C-xdeuyRqDMqeUGrq5E5NHx-0ETgmwBf3TivRFDrizwL6v-h2tfskFz0y9DyOuRxrh9dx7OEw99M1_8LvyVaBnTAg8FwQwXoVSvBLrUIHB1gFMGCslMgtXKadq51PSeTQdEWv8xO91FFitYghEienRU3apTNh5OYtKs7Nvv9rgvz32HOOsdHiD_MnSF_WWUUZW6I_vN-AD8mlh8DYpsskecWcQu-fwK6M8KTGzid3x4WXfrXFHiOi7g0AI9NcqgHb7TGPkNtDK8kM4Z25yFd33RkKHPTVGh22vdXnw8-FJw1dNj_q7IbgSP1JUBOaaf1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهپاد‌ها (قایق‌های تندرو بدون سرنشین) آمریکایی این مدلی به یکی از مهم‌ترین مراکز نیروی دریایی در بندرعباس نفوذ کردن و حمله کردن.  گفته می‌شود که در این حمله یک زیردریایی ج‌ا را نیز منهدم کردند.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6102" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=dlaVh_NQPbZ4XQoI5_y2liZCMFcdYOKBtonc9WqQplQFfnOAkNIWGWGd7nENArp_o_0wImIqZayV0rCrhqhOVWhNs4pQjjCo6pJHNB0FDJIQCtiZu9USjKETi0UBdfBn9_p2J8KI9n0NDibMXSEzGGoMjt_ySNMyqrw2aq1LaoB384sw0rUbSNlev1_kzwTPxVSSZgDdYyjJnUpR-jMUP4C7IxSkFg_5MdV0XlMHfN5xM3Bci9MFVsFJCqJEgTM-fKvTMjCmDFPo0VcAMuEzOSOkmytmVPLBcQWQgJAl5I_VI7MJQZtYbOyOIJyMpKeGZLvov1aplcoTwPf1yI8vNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=dlaVh_NQPbZ4XQoI5_y2liZCMFcdYOKBtonc9WqQplQFfnOAkNIWGWGd7nENArp_o_0wImIqZayV0rCrhqhOVWhNs4pQjjCo6pJHNB0FDJIQCtiZu9USjKETi0UBdfBn9_p2J8KI9n0NDibMXSEzGGoMjt_ySNMyqrw2aq1LaoB384sw0rUbSNlev1_kzwTPxVSSZgDdYyjJnUpR-jMUP4C7IxSkFg_5MdV0XlMHfN5xM3Bci9MFVsFJCqJEgTM-fKvTMjCmDFPo0VcAMuEzOSOkmytmVPLBcQWQgJAl5I_VI7MJQZtYbOyOIJyMpKeGZLvov1aplcoTwPf1yI8vNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جنگشون :)</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6101" target="_blank">📅 16:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoIpTOPqCayZ-x1F7ye7MzXFwVVNrPo8wmrFeAvoL6R4ONYSIDdJqp0itrv6cRS74cnezEn_neHxB9392nLk2lsG5ceLAtf91PfbjVW2gme69WfvbHctmHH-MJUQ3nC-TtC5JZSl8lIs3urG9qkrPw8Z8CY-HD6SzdwLSPFhLvC20uCNrKHaW0GMFH1T1sRdenO4GfwUod0rJqxJSi7U9SY17uEeunNx3ZF-cbaOtP6xFZzbr2MWxamEd_-M9SVfcb_sOwYLJagQMR-k150Uu6YWok3EDIyVp94XUpiDtsUSr8sSgOFy23jGVkEtk4Jjh5Le1Hx-FK3Cfc_lBCSQFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.  این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6100" target="_blank">📅 16:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6099">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">۴۷ سال رژیم اسلامی</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6099" target="_blank">📅 15:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6098">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPTu7YbcU8QlYhOeXFCcbAx-ZAu6JnxdT9xOgdTgpnctQnfdwi2EYJaojyhROt0mps2mM5K9V-0B9yphAc1zabcFvkdJ83IJKAIR27JYymsGl71sFCqsgPHavnKQXSN0PsZE1XU711-OJOtqcj_ZLN8gFy6J_cp7Os7rqVnvRouZnGGs698TdPd3yqsbVxHLkp-qKC12Fg-i6WDizD58SSqzZn7uTvIDlEdSQGrsGXxLoJhdsJNL3GFwRIo5K-K_HxFfug0WfhtdTFZZSENsVSTbyxGE3bklf9ukdnPKZkw2noMLRUcIbsUmC-yRWdCceir4nEVDGSQxi7OaVnqgaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
تخریب ساختمان مرکز آماد و پشتیبانی دریابانی نیروی انتظامی ⁧ بوشهر ⁩ در پی حملات هوایی ⁧ آمریکا ⁩ به مراکز نظامی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6098" target="_blank">📅 15:42 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
