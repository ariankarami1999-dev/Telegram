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
<img src="https://cdn4.telesco.pe/file/a2To2rU4OGHu5F6psTQpCCJB3kR6F_d95r6UGIGyyOUj7tZooyO9L6A_THi6SsNirkOQKny-dssVH85FGyZDJusGL3rMlMNdvWT6t6VvU6fXalziRvILgwWlEKscEIdrDk3-nPtakxIkwduXXtfuvr_KuNfGMe7CmbrLZlksOWx1lysnddaMalrf5_6J8NFpYzxWtb1Mlig0wqtj8GKXYTQaM7xPbP0G_4BMn7e25J9aE0QIk2R_S938MJJPmIPehrytzU5aXHXufXYtOlAanVjkOFyQkcknNZ5qByTTHaFShSWkOpFeI-8czzsKjJ-j3arn3vctNLEz5eEBYskVxg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 00:28:36</div>
<hr>

<div class="tg-post" id="msg-6195">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/farahmand_alipour/6195" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6194">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbBppC3kE4yiqvn1rPHo5LlwHBLSmaHvizSpBZGLNUz4gRKpxGzCOHkieTXV_mtXVmjA8iUFweBq2r_sO6aWBrzIUP04nKaaLvtIlzuYj_T33P6VB477eSUrzcfNbex07FxYKIvTm923ZWUCjQ_93cESQVKHSjPIcG6ZLG-uy4SVEsWn3jzpKo3FLv5GoPxQIZGWWxZHS6HAf_q0wNHP5j4C6Zk_B-wARPr6-kGZkylyPopWt8eL_7fO_hX5d873A1jCUqrPWjsA-ZQqOHlAJq5d_A6PJ4mb-Sd6oeHtXvna7lWiOQq52OF4-22STGgayexXHILpktMYVIw1eh-bVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش حملات ارتش آمریکا به بندرعباس، قشم، سیریک، بوشهر و اهواز</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farahmand_alipour/6194" target="_blank">📅 23:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6193">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
سنتکام: ‏امروز ساعت ۳ بعدازظهر به‌وقت منطقه زمانی شرقی،
[۲۲:۳۰ به وقت ایران - یک ساعت پیش] برای هفتمین شب متوالی، یک دور حملات علیه ایران انجام دادیم.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farahmand_alipour/6193" target="_blank">📅 23:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6192">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029791358c.mp4?token=G_Ar6iRCUc11R-46msXg1j-h30ffm98JIWUM_SzpGtvGP2VSkiH6v26FzQLGoQY19KhOYidUnba8ufzYCyub_qzKLU_VhhDWvLbzOtRSLaYy-oWiReFzdJnQQMIb0TWkK1-PQgH6MOujJtIB58jmQNUtAp6ptaHJ_0XIkwPaWjEzzOjbWWYy2t1mBkNtFBCflgIu8CmJa2q2UlzV7VapKHbxNU-dQOz5_gMR6WptDNsw5asRpCNsXTlh-OcMLpCvpFWhP1fWA1_HzotEvuN9vfYrg5NHY4i9IEj_A8PMgUMv3MgM4UbrK6UmYpiFSOPwwWC6ekRm8mAZcKArcqP6YLd4RXvOh05J8a6kZIWNJJsVMeLY07jgEWShJl21f7IZLKp3D-6D0vJk-MW5LK87cryhTE8YTqL8przbAL2ZzG1sFF_HQuP-ABDoMvbXgS0d8_dGZphfJdUVjYmS1UjCrPgUELzEPEfzUPupwyzMRaA_LzFCtb5KJV1w3PPSwmqAW8pMuYrig_MN8XItauN08_2sCoQ03OKrQnv2aUstJkNH87yYWd6uezQRyi4jqjmmpzvRbklmTyNBVe_RgDiOJ__flx_kb1NAh45LnFFfvgx63ieag599La85voJ5hef5Ogw60Jyx3rdAf3YVfXqULA9NN3Z__PFGyg5QlxNbMQs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029791358c.mp4?token=G_Ar6iRCUc11R-46msXg1j-h30ffm98JIWUM_SzpGtvGP2VSkiH6v26FzQLGoQY19KhOYidUnba8ufzYCyub_qzKLU_VhhDWvLbzOtRSLaYy-oWiReFzdJnQQMIb0TWkK1-PQgH6MOujJtIB58jmQNUtAp6ptaHJ_0XIkwPaWjEzzOjbWWYy2t1mBkNtFBCflgIu8CmJa2q2UlzV7VapKHbxNU-dQOz5_gMR6WptDNsw5asRpCNsXTlh-OcMLpCvpFWhP1fWA1_HzotEvuN9vfYrg5NHY4i9IEj_A8PMgUMv3MgM4UbrK6UmYpiFSOPwwWC6ekRm8mAZcKArcqP6YLd4RXvOh05J8a6kZIWNJJsVMeLY07jgEWShJl21f7IZLKp3D-6D0vJk-MW5LK87cryhTE8YTqL8przbAL2ZzG1sFF_HQuP-ABDoMvbXgS0d8_dGZphfJdUVjYmS1UjCrPgUELzEPEfzUPupwyzMRaA_LzFCtb5KJV1w3PPSwmqAW8pMuYrig_MN8XItauN08_2sCoQ03OKrQnv2aUstJkNH87yYWd6uezQRyi4jqjmmpzvRbklmTyNBVe_RgDiOJ__flx_kb1NAh45LnFFfvgx63ieag599La85voJ5hef5Ogw60Jyx3rdAf3YVfXqULA9NN3Z__PFGyg5QlxNbMQs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت شانه خاکی موقت کنار پل بندرعباس</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6192" target="_blank">📅 23:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6191">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏یک گزارش محرمانه که برای رئیس جمهور ایران تهیه شده است، نشان می‌دهد که تنها ۹٪ از ایرانیان از وضع موجود حمایت می‌کنند و تقریباً سه چهارم آنها یا اصلاحات ساختاری عمیق یا جایگزینی کامل نظام سیاسی را ترجیح می‌دهند - فاکس نیوز</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6191" target="_blank">📅 22:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6190">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:  ترامپ به ما نامه‌ای داده و صراحتاً نوشته است: «بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6190" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6189">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6189" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvDYAVxq_VcbEn0jaAtD5W0oDdCv3M8dmdxBphtzQ5ZwVVirnEuae7sQDY784gBK6BpZHGygBOPw0ePCzEjP8oa-y21b_C8vFWf_neLyAqf_Wbd7azZZUTfH89ug8shTlr8FOJfiyueNVS0BNi_E9sxOtFj-Zr9WdrRH6t2Mx6NALQBEyBifA83N9-w67rDqsQ-p0ZkWtPrVIBSdzYdbAZQSA8jNCx7-m0U0c5ubeMLRs6Ek-tOMEEqhg4k1z2U1vhP8aJsrJfW_zhBQbml2fRWDupFkGydVYyYxuDsrZrSNuy8hEr_6_uBv2KdiOOzC0chxlBOYOHNbuxHcbjYmzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ایستگاه مترو در تهران با مجسمه مریم و عیسی درست کردن (که عجیب هم نیست،
نصف قرآن داستان‌های مریم و عیسی
و قوم یهوده) و پروپاگاندایی راه انداختن
که ما چقدر احترام میگذاریم به بقیه مذاهب.
بعد همزمان کلیساها رو مصادره میکنن
و صدها نفر به جرم مسیحی بودن
توی زندانهای ج‌ا هستن و اجازه داشتن
یک مسجد به سنی‌ها رو هم نمیدن!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6188" target="_blank">📅 18:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6187">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o23JcAiz3J-Icg3U2M2NzvMMdb40oPmFoaBYdlEUwYBjyhuN5b7h2IyB8XgQrGu_Dq7InpDe7TcU2ZambOI_wXSGPPLisXRqSm0xPvHzpWORotmFzWGypHPDRcs28w5fgyeAPgPX9tmcEit4U8j9ZNBkqD25XpgTKaBzyczAQNroCMUmhkA_u6H04mdQtYeTzyX2ghvNenOWyuC42uvE645ZfSEQuwM6bftXXPSROfKTqucxUJy8Aa9k8LJWwmH-QDEjrouQMl89LJ258sbqW6S1tVKp-PMIp46gh9b6vqZvF-z-Z8kH5YlZDHes4FG4ujPhCMiuflxA-C9mAuAtDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب طلاقش بده :)
چرا اینهمه کینه؟</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6187" target="_blank">📅 18:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pj5r17LvhYKZPKH_z4Yr62thpiFHiUk8LiH26S0LqfbzRr4anLt-I4ZlHGmLLLokjaV7l3yCbMbH_sSwpzpoZRl_bN13-AuNvNRSDhRXn_0pWfAMFXI4j00iMQrdXOrrZlNW__UkxJ6YAYYDdIKuzjK2jXSON60UJVXKLGpSiLQs7ewG1M34omN483pt1bgKdxYdtLJ4MBnsrZGMgPCBlKZyeS0uSstBfzav_2qmMuBExOvZT22uS2fGMWylDiqDPF-rg6O1gBmACv9_Vtg-0tRr1_lFJMPu0svI6UoBFTlaJtH_Ay8aPYXXW4r5GwjOUXuhxMzY67FHpPB16lEb8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل عرزشی !
من میگم اینها شکست‌های تاریخ
رو پیدا میکنن و به عنوان الگوی خودشون معرفی می‌کنید باور نمیکنید :)
تنگه احد! که نماد بزرگ‌ترین شکست و عقب نشینی مسلمانان در تاریخ صدر اسلامه،
رو شباهت سازی میکنن با تنگه هرمز
‌‌میگن همونطور که اونو در سیطره داشتیم
اینو در سیطره خواهیم داشت.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6186" target="_blank">📅 17:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6185">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6185" target="_blank">📅 15:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ijt5NRK3bltsYCoHkEWDkhrcfi5qZ--8GXUF5P3-8IK0TPqriYcGaj_rju2tJ7vUgwYsS5u9HmUMtsvwofBpwQIY_G8VauO1lhDEPE79BAXOnZcWgApkjZp8GP76Nxi2zQQ9wVFiPyWCkbhC-9yvd0w_1ZnHvvy65JIPelk236nzSTkWZJOOo82ttchl91wf8Wqd9mCD7pIa5mPzdbLXD1iNMUNym65cPe24AyUPfo20PC1xb_MnWNYdf5MmiJ0HfjfWiWjCciXf3-nfQwoVq71WQBin3R_7y7TWbh_DZcycgfxnLxzhmpI6d4g18W17wla0suaespRUpAdDgjiyJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی به تاسیسات آب‌شیرین  و تولید برق کویت حمله کرده.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6184" target="_blank">📅 14:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6183">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=JYCCchxyPd6A7ilQkz80EaXyVs2eEsT0foYs0LNA-hNCrlVX8uDIyd-GqnSj5S2pA-NoJCWDs722GN6rh_Ulp8FaQ0otBJuAQbmpJQ708RODUIsw74MXBXvtq7PL43Lw1-UcXriz7sjhxUJ_-S4b-ut0y0jgQ6bDNuTeQqHPL1cMhNAvReGvM30SDFNiUAhxndwwJO1AJzo07_DC2-7eu59ijUkCzJoG_7SBCDpUqnnqNyZzxS9d3tfNka8FoWGidqeZPqX2Fe-VYDqyVPpf4atEFBFm_dWFHWLR04c2eYcB5XOY4r0ClYFla4O8NDsMZLeR8uv-naHUfuY0s1njVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=JYCCchxyPd6A7ilQkz80EaXyVs2eEsT0foYs0LNA-hNCrlVX8uDIyd-GqnSj5S2pA-NoJCWDs722GN6rh_Ulp8FaQ0otBJuAQbmpJQ708RODUIsw74MXBXvtq7PL43Lw1-UcXriz7sjhxUJ_-S4b-ut0y0jgQ6bDNuTeQqHPL1cMhNAvReGvM30SDFNiUAhxndwwJO1AJzo07_DC2-7eu59ijUkCzJoG_7SBCDpUqnnqNyZzxS9d3tfNka8FoWGidqeZPqX2Fe-VYDqyVPpf4atEFBFm_dWFHWLR04c2eYcB5XOY4r0ClYFla4O8NDsMZLeR8uv-naHUfuY0s1njVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!  ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟  به خاطرش حتی موشک به اسرائیل نزدید؟  (که اونهم اومد در پاسخ ماهشهر رو زد؟)  خب جنگیدید و شکست خوردید!!! هم در لبنان،  هم ‌در سوریه…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6183" target="_blank">📅 14:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6182">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6182" target="_blank">📅 14:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6181">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6181" target="_blank">📅 13:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6180">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6180" target="_blank">📅 11:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6179">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6179" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6178">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=gQaoAYWVaDThIrFT6v0SMdZMNkx4TA3jclUzJzT9SgLoVyYvzuBAs6Gqhy-_N1k277GGoVX_IbMcnKXIi2CDlrcALulHj5YDfNCoc5xEiJmSd-oCVl67n9jjSyZmYi0GvVBmGcUzDtZOUCBay9OlrZL-K82Y7uepqgS64LBzJHQ9T2STfxdAwJyXZOvWXqob52USmf2qIcnLulhQS5Nx2tPylu74o9IGWjepVmiuJHO9Dm0DqB6uePJagxSEdy8Tpqe3kmyGHlbVpYfzZvIFNgyCM44qLm0sepNM26eUD5tGSKyO_EX3uoUX02PkJRi-qDv_EmDegjDMFWulTVmJPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=gQaoAYWVaDThIrFT6v0SMdZMNkx4TA3jclUzJzT9SgLoVyYvzuBAs6Gqhy-_N1k277GGoVX_IbMcnKXIi2CDlrcALulHj5YDfNCoc5xEiJmSd-oCVl67n9jjSyZmYi0GvVBmGcUzDtZOUCBay9OlrZL-K82Y7uepqgS64LBzJHQ9T2STfxdAwJyXZOvWXqob52USmf2qIcnLulhQS5Nx2tPylu74o9IGWjepVmiuJHO9Dm0DqB6uePJagxSEdy8Tpqe3kmyGHlbVpYfzZvIFNgyCM44qLm0sepNM26eUD5tGSKyO_EX3uoUX02PkJRi-qDv_EmDegjDMFWulTVmJPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی از سخنان سردار نقدی : اگه حتی به آمریکا حمله کنیم، قدرت پاسخ‌گویی هم ندارند!
با کدام پشتوانه اقتصادی میخواهند بجنگند؟ با کدام پشتوانه مردمی خودشان؟ همه جا در محاصره ما هستند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6178" target="_blank">📅 08:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=GXFlQQbFMPL99OuKitmuYM7_gpOlEx2qvvIZ7PIOj8YGh4HIcm7Qf9a69gzckHFe2P6Rybhsfz85WWpn_UYp4cVW7Rl9b56DHYLZDncL0Faokm3P68zdXk2GDl8lju5GUM8ZYPRXODiqbeJojQDpsoS49r5oL07Gu3sQ_kciZ96BimKoCZnS-ciA_qz1mF_86f_hO-Jcorra3AJ8-nsM2eRkUGgFB2pjk_giCybNORsGxvGwwGxWkoiG1hpTKxYs__RiD87pTTElgON6_LsxkvLS1nohQtEmgs4QwKdwG5uS9_n6RIKT5PPvOgpRaX8uecZdxrTHU7CpjWftT5smiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=GXFlQQbFMPL99OuKitmuYM7_gpOlEx2qvvIZ7PIOj8YGh4HIcm7Qf9a69gzckHFe2P6Rybhsfz85WWpn_UYp4cVW7Rl9b56DHYLZDncL0Faokm3P68zdXk2GDl8lju5GUM8ZYPRXODiqbeJojQDpsoS49r5oL07Gu3sQ_kciZ96BimKoCZnS-ciA_qz1mF_86f_hO-Jcorra3AJ8-nsM2eRkUGgFB2pjk_giCybNORsGxvGwwGxWkoiG1hpTKxYs__RiD87pTTElgON6_LsxkvLS1nohQtEmgs4QwKdwG5uS9_n6RIKT5PPvOgpRaX8uecZdxrTHU7CpjWftT5smiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پل  کهورستان در اطراف بندرعباس
که شب گذشته مورد حمله ارتش آمریکا قرار گرفت</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6177" target="_blank">📅 08:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6176">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار …</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6176" target="_blank">📅 08:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6175">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6175" target="_blank">📅 08:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6174">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
حملات شدید به بوشهر</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6174" target="_blank">📅 01:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6173">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=nh3jIqHg1P_ecwrCCZEUNfrz0bBxUjZs6ZM2M0JySHanbgfLTpwX4l_sh5D4_SrtMyK5i4shdB7BJr3oXMRQUEuDXEtOqZcAlTfETE1mpTd4IAAK7xnFeTbpuyImko-Gj9lMuFKNQlf4WIdu45QLD4ccwqoLSHdJInPdO6XOJhI8ozJmQC04_iiOzFoCSHeQkufogEi3jfCQ5ITqbZaVpnIYBiyNClkZ1OJUOFWoo6eNmbI-FvUDduAeaVPMZp1cKRyDWbF2LB3R9hkcUSO0JVwNFem3wLteVhmrYyLV9hCB02Z5xQyyJsZWKy0q_CnISixPX9_iWwbG_Pd4TU004Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=nh3jIqHg1P_ecwrCCZEUNfrz0bBxUjZs6ZM2M0JySHanbgfLTpwX4l_sh5D4_SrtMyK5i4shdB7BJr3oXMRQUEuDXEtOqZcAlTfETE1mpTd4IAAK7xnFeTbpuyImko-Gj9lMuFKNQlf4WIdu45QLD4ccwqoLSHdJInPdO6XOJhI8ozJmQC04_iiOzFoCSHeQkufogEi3jfCQ5ITqbZaVpnIYBiyNClkZ1OJUOFWoo6eNmbI-FvUDduAeaVPMZp1cKRyDWbF2LB3R9hkcUSO0JVwNFem3wLteVhmrYyLV9hCB02Z5xQyyJsZWKy0q_CnISixPX9_iWwbG_Pd4TU004Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏فارس: جزییات حملۀ   آمریکا به پل‌هایی در شهرستان خمیر؛ ۲ نفر شهید و ۴ نفر مجروح شدند</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6173" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnrm30qJQkqF5qApZqNl9CvmFw6K4JQ8XNs_z-bM1_fVJIMVFvEmHU0mx5SYUyFvfOZpHGknRL0P5IWPaI1sbP3Xho6XqYTHgi11vVqJfZ38Q4JoFL2tq7m2AI-CAucaOPr5Li9toCgi0m7xkXexCpPCwwooDqUbSk6xKNX48EhbK5q-vDvoqs5yIdYPbOUeioDfjVhwNAZYeTldcu1Zz7eKYhUtdt46Ucx0_9vcRNnZ8wrWOuLE8RnQOUkYcu2h6jHgH7f1vT3cxDdMck3k8zntTdpStJr4o0XogD-ibZOJIDQdLazntsAXJl1mIU6NmA2v8TUvdF6jhWFJFDeSLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6172" target="_blank">📅 00:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6171">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
صدا و سیما :دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند.
بندرعباس مهم‌ترین دروازه واردات و صادرات کشور است و شبکه ریلی بخش بزرگی از این حمل و نقل را بر عهده دارد.
این حمله می‌تواند به حمل و نقل کالا ضربه بزند و به آن اختلال وارد کند،</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6171" target="_blank">📅 00:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6170">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
حملات گسترده به حمیدیه و شوش در خوزستان</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6170" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6169">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
حمله جنگنده‌های آمریکایی به فرودگاه ایرانشهر</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6169" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6168">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6168" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6167">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlQ44xYnu-5pGRQPlO5hThZgZ60nAsnktx2nz6BK0KVpZa2mmoB9exOiak9r5tk2kujh1b90qyq0V1RtBvbHEVSyy9L0he_s12DAoSQ5pj01ilkf3LLA_CdqAbnQTqZPopVrXj3sb8jJW6dJDimhelnuWadF-XlQ63FJVeMAgJQbmffcfpch4LzWrXepMahUNMJDTc44SFGEK92o0AZf6V18QWQ3dqGBe-3K9q14WYb9vvGI9Zd4zfzgNotsm9mwsoCT1wIeZANSy7xRptmDAIxvbVmK9BojpBN3qejKHN3zKL1feA9Sb88w3g3oZqzI5MIK0amtXwykFAJnH513BQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6167" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6166">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6166" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6165">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏
🚨
🚨
سنتکام: موج جدید حملات در پنجمین شب پیاپی را شروع کردیم.
🚨
مهر: حمله مجدد آمریکا بندرعباس
در ساعت ۲۱:۳۵ نقاطی در بندرعباس مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6165" target="_blank">📅 21:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6164">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=se8BLxz96lkH2E-QA4r__LcsRANM1EN9aTs_aPWGr27zjQxks8e6i9H0gaGR_5J_J6LkuxQijTVLbyw-u_m8_WR8Qe64CuiFYtjpc05is5U_cjYwn6WgOBZG3hAcGXI6pe4Sh-2YZjI-GzUoB8Z1C5eEDmE5xLatoRDxS5ZYrMfg0E1mNVPJFhrQy8AbgLvTcLMba31sdb9XhAfdyAIn-2Sqce9H57k2E_wABYyIpswoFTJh9UrDKgpvxN6JeN170e2lq8GGmbHGB_UkhagA0PWM7NrKuJsMp6podFar-qXGQS0EzfCQh83qEbEuReUzC0HObQSePCM3EPSphf9LGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=se8BLxz96lkH2E-QA4r__LcsRANM1EN9aTs_aPWGr27zjQxks8e6i9H0gaGR_5J_J6LkuxQijTVLbyw-u_m8_WR8Qe64CuiFYtjpc05is5U_cjYwn6WgOBZG3hAcGXI6pe4Sh-2YZjI-GzUoB8Z1C5eEDmE5xLatoRDxS5ZYrMfg0E1mNVPJFhrQy8AbgLvTcLMba31sdb9XhAfdyAIn-2Sqce9H57k2E_wABYyIpswoFTJh9UrDKgpvxN6JeN170e2lq8GGmbHGB_UkhagA0PWM7NrKuJsMp6podFar-qXGQS0EzfCQh83qEbEuReUzC0HObQSePCM3EPSphf9LGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازغدی : اگر میخواهیم اغتشاش نشود
باید با آمریکا مبارزه کنیم
(که حواس مردم به جنگ پرت بشه
و تقصیر کاستی‌های حکومت بیفته پای جنگ
و دوباره جنگ بشه «نعمت» !)</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6164" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6163">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
استانداری هرمزگان:  در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6163" target="_blank">📅 19:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6162">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmHs8l77QPrYHBvNAVLZWsIXxUeZW8jqNCft_oHdt1hHIxAUn52e5ZjV4Ush3zQxTF0ql0OLVW355OAqtveUoJsVDItmlglTN9pObjWpQsQT0jppUZK4zFhfh7q5s3K-DqffpjgeTKM4-r_M80Eckoyls7GibNufVxBoT_MdgF86Bin3dUh1xcdz-xTnukM0kkgc5gNn9ldHFezLRfIGhbGuQ1jxKCUE2kQxRRRRnfzSNhTab392tK1a2nsS3S6M1tDoqqOE4nqWsAU_zWVWxaGzNd7LQepEQvfdATiqZ040CcMQc9qMfHZ1soadR5jZat3IqTVCIUi9rTLAVIhj1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز :
پاکستان به ایران هشدار داده‌ که اگر به عربستان سعودی حمله کند، پاکستان آن را حمله‌ای علیه خود خواهد دانست و اعلام کرده‌: «این خط قرمز ماست.
»
پاکستان و عربستان قرارداد پیمان دفاعی مشترک دارند که بر اساس آن حمله به هر کدام ، حمله به دیگری تلقی می‌شود.
🔺
برخی اعتقاد دارند که یکی از انگیزه‌های اصلی تلاش پاکستان برای میانجی‌گری میان ج‌ا و آمریکا ، نگرانی از وقوع جنگی است که دامنه‌اش به عربستان برسد و پاکستان را ناچار به ورود به این جنگ کند.
اینک که تفاهم نامه کنار رفته، پاکستان بیش از پیش نگران این موضوع است.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6162" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6161">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
استانداری هرمزگان:
در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6161" target="_blank">📅 19:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6160">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=odTYSqMApeFPY7Ws3LYwEdDtCr4PAKpc1WF1v41-WwRQj1NXA8Mawe5r73_NVLAA-ZigfSxih1AzPsgWKZ3wV-Jer8RxRTaYiWCzoqCEE-CPfYExgiAu8607-nRwlUUMl0QjSs-Iie3V4kXOr4ZTGE6ZOJJQBXEvbN5ptDZy1o5-Nv3caKCdEPT1OZFkr4wWjao8NjA9M4raaS-SrrCqyvdHvwjMu4ulWkfw18RHTMraOIjLHqbjQLEGURy8gF2JFXjEbw6GBubCwF6_s_Mx5qZw9cmuE9ApKhe1tImAqvx_DCPwA7NXWDaQ-3lKfUo75XCR3igaax7aAZVP820Oa0jERIDVfS8DLirgxpQOxPKiVsAU-N3KhPNMumyS-U2ML4fARGqkWe0JufM85LwaJ9bDMlN53LNtCMnathftCywCWg8M-Tk1LnhozY5iy3-UB-C7go9SRsoFA6gKZpzNuhII1ag2XX5bszHCE-3CDl6MoBu2_GDaYS0g6Xj8og1y5ZI783EWs-WpU2voPIUyoeQ1EvUkdAgpdAJPLaxMB0AQ5DhKcTwjPyAClmQcEGD0OOGx7Z5ZxpPhe8mHU67n8A_RRtWVYZzh9IGBIWINkP5Kej5TsMsroIgptiImiCc0i-qCsZp6fRQKOwRyKJ3OPVj0uunl_DYNZcBUmvak-eE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=odTYSqMApeFPY7Ws3LYwEdDtCr4PAKpc1WF1v41-WwRQj1NXA8Mawe5r73_NVLAA-ZigfSxih1AzPsgWKZ3wV-Jer8RxRTaYiWCzoqCEE-CPfYExgiAu8607-nRwlUUMl0QjSs-Iie3V4kXOr4ZTGE6ZOJJQBXEvbN5ptDZy1o5-Nv3caKCdEPT1OZFkr4wWjao8NjA9M4raaS-SrrCqyvdHvwjMu4ulWkfw18RHTMraOIjLHqbjQLEGURy8gF2JFXjEbw6GBubCwF6_s_Mx5qZw9cmuE9ApKhe1tImAqvx_DCPwA7NXWDaQ-3lKfUo75XCR3igaax7aAZVP820Oa0jERIDVfS8DLirgxpQOxPKiVsAU-N3KhPNMumyS-U2ML4fARGqkWe0JufM85LwaJ9bDMlN53LNtCMnathftCywCWg8M-Tk1LnhozY5iy3-UB-C7go9SRsoFA6gKZpzNuhII1ag2XX5bszHCE-3CDl6MoBu2_GDaYS0g6Xj8og1y5ZI783EWs-WpU2voPIUyoeQ1EvUkdAgpdAJPLaxMB0AQ5DhKcTwjPyAClmQcEGD0OOGx7Z5ZxpPhe8mHU67n8A_RRtWVYZzh9IGBIWINkP5Kej5TsMsroIgptiImiCc0i-qCsZp6fRQKOwRyKJ3OPVj0uunl_DYNZcBUmvak-eE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی جدید جمهوری اسلامی</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6160" target="_blank">📅 19:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6159">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6159" target="_blank">📅 18:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6158">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ایران که ۴۷ ساله که در آتش فتنه اینها می‌سوزه</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6158" target="_blank">📅 17:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6157">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سخنگوی قرارگاه خاتم : هر چه در منطقه سالم مانده از نجابت جمهوری اسلامی است!
ذوالفقاری: «همه آنچه که بنا به نجابت ایران هنوز سالم مانده، یعنی تمامی زیرساخت‌ها در منطقه، زیر ضربات پولادین نیروهای مسلح مقتدر جمهوری اسلامی در هم کوبیده خواهد شد؛ آن‌چنان که اثری از آن‌ها بر جای نماند و گویی از ابتدا وجود نداشته‌اند.»
سخنگوی قرارگاه مرکزی خاتم‌الانبیا همچنین دخالت آمریکا در تنگه هرمز را «خط قرمز شکست‌ناپذیر» جمهوری اسلامی خواند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6157" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6156">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=EroCSYZMXr_0ljjGj1tUgu_95-8GlpNE8aeeiNAez6s-p6bZiZI4bxoeZVcI4QjacdY5fDe2b135GlaDXaI9lR3uxIY-pUFDXMdYHACZ8-hle3NO27AIb-AVBAnt4YUGUyjX0dVvwvReLgqV81WqqPcmr0Mc3Lyh-RiZAR6Vn2qmJ8MToqaPYCJf-21tQMx9tynTQ9FmtI0inkfDNmllyf6OZBoMaifryNtqOertqxCLKHK1oz-2kAOIbMdItSvPpV__fJPCkM4UujxPmkD_H0yv1s-hYrC5oXSMVhJfpI4lnC_XPTd9S-GoeuNiW3CTUfqfahNI_t6KKqY7lNkLAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=EroCSYZMXr_0ljjGj1tUgu_95-8GlpNE8aeeiNAez6s-p6bZiZI4bxoeZVcI4QjacdY5fDe2b135GlaDXaI9lR3uxIY-pUFDXMdYHACZ8-hle3NO27AIb-AVBAnt4YUGUyjX0dVvwvReLgqV81WqqPcmr0Mc3Lyh-RiZAR6Vn2qmJ8MToqaPYCJf-21tQMx9tynTQ9FmtI0inkfDNmllyf6OZBoMaifryNtqOertqxCLKHK1oz-2kAOIbMdItSvPpV__fJPCkM4UujxPmkD_H0yv1s-hYrC5oXSMVhJfpI4lnC_XPTd9S-GoeuNiW3CTUfqfahNI_t6KKqY7lNkLAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شب گذشته ج‌ا به اربیل در عراق
علی‌الزیدی نخست‌وزیر عراق با صدور بیانیه‌ای،
این حمله را محکوم کرد.
در این بیانیه آمده که «به آژانس‌های امنیتی
مربوطه در هماهنگی با نیروهای امنیتی منطقه دستور داده شده که همۀ تدابیر لازم برای ممانعت از تکرار حملاتی از این دست، و نیز مقابله با هرکسی که به‌دنبال خدشه‌وارد کردن به امنیت جامعۀ سرفراز عراق باشد را اتخاذ کنند».</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6156" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6155">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqaiUwzzebYRJTJdLh_4-ILXZpcYnMtOYAHN12E0BGgErvG-mSidPtnTHr0zNeHhqX03o3fEJ6SeYXLF9mNCx6B4qgVa2orBREkMiezwZx4K3KhVC6IFRzwuoEfFdhrq1CFQbCD5A4gdcu7R2WM3ISkyZQK5O79hy5z0S3qgsrSQ64uXj5GMcrb8CXH30VTf7OKSXYk4Q6-Eex36D54dlXvciEIGfhvavFpUsCZTAlAs4BPZrgIUPsMLwqZ70i-OY2Rj2D8rupRYzXEWXGEeQL3wbtbT8dbxt5RlxFz6R6IVGa0JeEOb5u1RggvneUg69AsKPkUGqXeMuiktqcokHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وراجی نکنید  بگذارید بجنگند که صلح بیارن :)  مثل صلحی که ۴۷ ساله در لبنان  ‌ و غزه آوردن!  انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6155" target="_blank">📅 12:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6154">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وراجی نکنید
بگذارید بجنگند که صلح بیارن :)
مثل صلحی که ۴۷ ساله در لبنان
‌ و غزه آوردن!
انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6154" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6152">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=Ld2KzccG-h9yEkdev1Dkna4vqIocLfI2SHzCPfZ6yQqEGs7K0Hk0P1sucpLOvORgfdTAifOAASPDUjo4Q-NcE52uweTfbWuVhnBOXGEElHhUYKohUpTyAYE2bERVGzuOSZl1jFPmsYpA6fKVW9EfC_nSDD5786C4CIWckeei593OZ-O_2CyvPVEy-9JvJ9Eezy5xViwqa7xMJuDVE7gsH8wYUjY1i6ZKBm3Lqt8oadvtMlYwaJbWqgGWwjTP0VF6n_pz1mNHEigt07ZZtWEfABCKcZIxhZh6lLqJQIPX85LKrkyK4Y8vfeM0Cv7aa3VMQvqWZgM404iR1txGm-HRAA2ZqA6X-_2ZuOir9_h82GCeMHf6nIV2KKvyadc1pCdoxpUdIK9A3sQ2b5FtZofES8M_v8yVyq-3S1-Q1WSXwbREiIjVwslovomf0rM7lB8SVGJknITjHk2R5IGjdeh7HqiWhhU8CDVOk4pmUEVyHrihmfkGJ36qqMpRSEMpjKpfyrLbdcpFzSCQhf_XQZlkYNB65FRDbNKfu9S6UkoPiH9IDJSXaYpeZwbktGtQFY4wBxQUqmA2Qk1-SoPxfp-aBxt0TNA-KRqrK6AuLaz083FIa2dSz7CUl-il6sjG9RImucsnRGfh1OaQB3VsE_BDSSL4r2Q7St5Q9GcPlQ6NE74" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=Ld2KzccG-h9yEkdev1Dkna4vqIocLfI2SHzCPfZ6yQqEGs7K0Hk0P1sucpLOvORgfdTAifOAASPDUjo4Q-NcE52uweTfbWuVhnBOXGEElHhUYKohUpTyAYE2bERVGzuOSZl1jFPmsYpA6fKVW9EfC_nSDD5786C4CIWckeei593OZ-O_2CyvPVEy-9JvJ9Eezy5xViwqa7xMJuDVE7gsH8wYUjY1i6ZKBm3Lqt8oadvtMlYwaJbWqgGWwjTP0VF6n_pz1mNHEigt07ZZtWEfABCKcZIxhZh6lLqJQIPX85LKrkyK4Y8vfeM0Cv7aa3VMQvqWZgM404iR1txGm-HRAA2ZqA6X-_2ZuOir9_h82GCeMHf6nIV2KKvyadc1pCdoxpUdIK9A3sQ2b5FtZofES8M_v8yVyq-3S1-Q1WSXwbREiIjVwslovomf0rM7lB8SVGJknITjHk2R5IGjdeh7HqiWhhU8CDVOk4pmUEVyHrihmfkGJ36qqMpRSEMpjKpfyrLbdcpFzSCQhf_XQZlkYNB65FRDbNKfu9S6UkoPiH9IDJSXaYpeZwbktGtQFY4wBxQUqmA2Qk1-SoPxfp-aBxt0TNA-KRqrK6AuLaz083FIa2dSz7CUl-il6sjG9RImucsnRGfh1OaQB3VsE_BDSSL4r2Q7St5Q9GcPlQ6NE74" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگر نوحه میخونن و مداحی و رجز خوانی و.. برای کودکان غزه و لبنان و میناب و….. از تاسف از دست رفتن زندگی نیست! میخوان در این جنگ بی‌‌‌‌پایانی که با جهان دارند،  از جمله و در صدر این‌جنگها،  با خود مردم ایران جنگ دارند، سربازگیری کنند! تا نیروهاشون بزرگ‌تر…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6152" target="_blank">📅 11:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6151">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">تمدن اسلامی! تا زمانی که توی مدینه و مگه بود قادر به ساخت «توالت» هم نبود!  مستراح هم نداشتن !! اما دنیا در چه وضعی بود؟  ۶۰۰ سال قبل از تولد اسلام!  توی بیشتر شهرهای جهان  داشتن توالت عمومی! اجباری بود!   اینها میشینن روی منبر  میگن «مدینه فاضله»!!  حالا…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6151" target="_blank">📅 10:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6150">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">تمدن مصر باستان رو مطالعه کنید ابتدا تا انتهاش بر مدار مرگ بود! فرعون از زمانی که سر کار می‌ا‌ومد به فکر مقدمات مرگش بود و قبرش بود!  هنر و پزشکی و علم و مهندسی مصر همه بر پایه صنعت مرگ بود!  مومیایی و اهرام و جراحی پزشکی و….. همه برای کار و کسب مرگ بود و…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6150" target="_blank">📅 10:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6149">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDlr7muK2a8gjKYjXwCVUm1eMBwFeZuNyBbTxKXYdaoBVxx8M8odL_EGgTs8BPQNvFq73NtI1vJw45UpLBqibyGBSigtzAHECtc0z7-VqZ8ksjjHfbA3u7N4NoSL3LegGWAM8QRHh9SBw7eaWY7eH54StMpdkYTYxMmX9CFtUEgS_fF45On87SMABuK_AZYqyl3i8wZqCyXb0x3qkNwQL51Z8uAogyIH9xsFU7ELy1Vkz0cmxFzKZOOw8Gq3vPOLzYRB813Z6Ag8UERXmS0xDejhL_96S8VAHkfVOVfoQJXA7f4ld-CTdbepEuMMaHipFgujxGGHUEinH7SjhnH9JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها شنیدید جملاتی با این مفهوم رو که زندگی و این حیات «زندان مومنه»!  آرزوی اینها مرگه! مرگ براشون رهایی است!  اینکه برن و برسن به بهشت و به زندگی!!  مرگ رو آرمان خودشون می‌دونن و زندگی و زیبایی‌هاش  رو پست و حقیر معرفی میکنن!  و اینکه باید دائم به فکر مرگ…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6149" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6148">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..  سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند. و از مرگ متاثر میشن!  تمام هستی اینها :  مبارزه، جنگ، کشتن،  کشته شدن و….. است!  زندگی براشون چیزی نیست جز  «مبارزه  برای عقیده».  و خوشحال میشن…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6148" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6147">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6147" target="_blank">📅 10:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6146">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jH6EphBBPh6U0DPzJZ58lF-4QD9nnqqgkn8fUf3EHTTswgy6Jvc0D06o8vdEGIBmhjEzE-2oZTjtySXByQvYjzj12h5xgaODLXvKX93yQyh79rhiekShgWGp-IDm0f2dAs0s_1P__AvpKoCiZOqz34zk7ubQbnouZmN4fa15Fywwkr1AtoNkwQDclM1Y8uRQNtrU6Jse10BZki3gdf86tTwL4eP2RC178-tEQL-oViNsgETNSjneAX_o2eBbEEi0MpBisevi1K1GluChodyJMHGh3lmmJgKPsP8tfsYvGVijpKrFx5hf1Rq4nrMtxeeRZpl-wNO_l_hip-8hHFDZZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران به یک شهروند زن آمریکایی که در دسامبر ۲۰۲۴ در دوران رئیس‌جمهوری جو بایدنِ خواب‌آلود به‌ناحق بازداشت شده بود، اجازه خروج از کشور داده است. او اکنون در سلامت کامل در خارج از ایران است. ایالات متحده آمریکا از این ژست حسن‌نیت ایران قدردانی می‌کند.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6146" target="_blank">📅 09:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6145">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6145" target="_blank">📅 09:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6144">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">استاندار مرکزی : شب گذشته به دو نظقه در اطراف شهر خنداب حمله شد.
این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقا مشخص میکند چه اهدافی را زده و نه ج‌ا می‌گوید به کجاهاش خورده.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6144" target="_blank">📅 08:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6143">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اطلاعیه  ارتش:  سامانه‌های راداری، سامانه پدافندی پاتریوت و مخازن سوخت آمریکا در پایگاه علی‌السالم کویت را هدف قرار دادیم.
‏ رادار‌های سوپر هاوک، تأسیسات و سامانه‌های پاتریوت واشنگتن در پایگاه شیخ عیسی بحرین نیز طی حملاتی، آسیب‌های جدی دید.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6143" target="_blank">📅 08:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6142">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
استاندار سمنان : به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6142" target="_blank">📅 08:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6141">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhirCBq94DZ0U9ZwhhIN7dcZ6SMMX--oWjh83anhnXnaFjvjERPEnVjG9miC0WRwBsrQwz81mGSR1C8ehH_2gH08y518evy6hqLLT-3txT8RtZSCxGHjUD5zm8MbbD1RRAcZSoSYM8kVmvV_J-sGykQ_f0o-ituMjGYo60pPY9kua70QxJ3Rm5V6NaWTOpRUfeUOn2yxG827DMug2xTW2ktog34J7F3Bs9PYQSTRZT9uYMvrljEpOb790SZOvpXtGbr7oGPT_UkBNyPpHveuHfTdiC1sAm5nGuoo4_P9Z_ECZPK5XYKi8rXkA6tIVcEEko5HKCpTOolr5Lk4KyGhrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین یارو خودش از دست سپاه و نهادهای زیر نظر خامنه‌ای  فرار کرده و به آمریکا پناه برده!
و آمریکا رو خونه امنی پیدا کرد برای زندگی و نوشتن از اینکه اسلام چقدر زیباست و خوبه و سعادت انسان رو میخواد!
حالا از همونجا به ج‌ا میگه مبارزه کن با آمریکا! مطلقا تسلیم نشید! تا انتهاش برید!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6141" target="_blank">📅 08:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6140">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">برخی گزارش‌ها از تداوم حملات به اهواز خبر می‌دهند و اینکه تاکنون ‌۹  انفجار  مهیب در شهر شنیده شده.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6140" target="_blank">📅 23:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6139">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
چندین انفجار مهیب در چابهار و بندرعباس
🚨
کویت : امروز ۲۱ پهپاد و ۴ موشک شلیک شده از سوی ج‌ا را منهدم کردیم.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6139" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6138">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای ۲ یا ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6138" target="_blank">📅 22:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6137">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3MO-Jxl0regXnegzxugYBrzbh8bwrLqtLPwf2frMjMX_Z0EdOZcv2qavUmGR3dYsdR6MIxZYCHYIfTE9OD9FIuajeicKJG9Kst4v9lpHU1yf7VMq2i0ATu4LbqCN9RgzVGMA1L5tYgm7QRpI9k7m5m2cRs_ZTUFBvDZ-4ZfUJvJo1UkhfU_DE_WapP5cdW0kJjCya8U-umpr5yTNaiONJ45Ro_6iw6jABmZmXkQ34dAmxBSnSFTHmXi3jvcgubrUCJJaSdLOQhJhuSKQDRNuXMK-0CG5l8tMTx1BA0GX-gTfskURVs3z3bY_tUnAlNGObuaoq5qWYWotkoKNm1Lcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما دیگه جرات حمله به اسرائیل
رو ندارید! خودتون هم خوب می‌دونید!
این ۴-۵ روز هم به همه جا حمله کردید
به جز به اون کشوری که بیت‌رهبری
رو زد نابود کرد!
و نشون داد دقیقا کجاست که سست‌تر از لانه عنکبوته!
ولی هر چقدر دوست دارید شعار بدید!
اون حزب‌الله تروریست هم رفت انتقام بگیره  هنوز و همین امروز هم نیم میلیون نفرشون  توی محله‌های مسیحی و سنی لبنان آواره شدن!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6137" target="_blank">📅 20:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6136">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">آنچه شب گذشته در بمپور رخ داد و موجب  کشته شدن تعدادی ای نیروهای ارتشی شد، قابل اجتناب بود.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6136" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6135">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e615d142.mp4?token=tdd3HmhuLo4KFJavfwuKSf0zAvXATn9bHfbm_Lox_Lk5x6p28pcA2zDVg15Ua5To4xFWG90OOFJm0VXcUTvyKZsUBUdayBHPFb6wff6XKpHsOrlRGKyZ_wgRENyhs7-0dOW9p2Srablk4D32K9oAqBebFWNpQPDrueBSWt3zIlsDuZdfuXPAzEgFKPGq6ZGdvg6-ZrSKwFUc8fdvPg75d9ZwykikTfxrcg-WVz2hagyCP45ZvuDa2xiTBGZkuET2si6cx77b535__YRMT8fw4WJlSb0oAiqcp4LjqsWOR6-6ap4nlcjL7pwxfnxISLC0ddzhPApLEIkPYiZM1ICEDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e615d142.mp4?token=tdd3HmhuLo4KFJavfwuKSf0zAvXATn9bHfbm_Lox_Lk5x6p28pcA2zDVg15Ua5To4xFWG90OOFJm0VXcUTvyKZsUBUdayBHPFb6wff6XKpHsOrlRGKyZ_wgRENyhs7-0dOW9p2Srablk4D32K9oAqBebFWNpQPDrueBSWt3zIlsDuZdfuXPAzEgFKPGq6ZGdvg6-ZrSKwFUc8fdvPg75d9ZwykikTfxrcg-WVz2hagyCP45ZvuDa2xiTBGZkuET2si6cx77b535__YRMT8fw4WJlSb0oAiqcp4LjqsWOR6-6ap4nlcjL7pwxfnxISLC0ddzhPApLEIkPYiZM1ICEDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش بینی تاریخی بختیار
در دو کلمه، برای مردم ایران</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6135" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6134">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=lCLjXHWt9iMhzdvkAUX2zYbbZBUcHUCAsqQt2ycg_NQAhilxIeix5AMWNLgNxcf3XKkBsVP7Vjz-PwtBdtFFbqliu-Gha6RHdYRrABI_CVrNkkrNwYf4qc8O_zWb_odTcuUco9zQgLHnMOHA9hiiR75-VlhFF7S--2wzR0ZkRFhI2ws6jQ-kA2uGq4TOqJr-yHJsQ4Y8HuDTm10VxY5OMbnM0VohB4ztFeLvaGPUdTXFXeupZiro80FSxxzXMe-j_u1rEE5yWdQqoR44mJc4PC3ptA2WFtRLUi6lOXGOrIgBlL95WFUezaWeC45IAeoWRhdClWVo4w8aCEe9U2HmO4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=lCLjXHWt9iMhzdvkAUX2zYbbZBUcHUCAsqQt2ycg_NQAhilxIeix5AMWNLgNxcf3XKkBsVP7Vjz-PwtBdtFFbqliu-Gha6RHdYRrABI_CVrNkkrNwYf4qc8O_zWb_odTcuUco9zQgLHnMOHA9hiiR75-VlhFF7S--2wzR0ZkRFhI2ws6jQ-kA2uGq4TOqJr-yHJsQ4Y8HuDTm10VxY5OMbnM0VohB4ztFeLvaGPUdTXFXeupZiro80FSxxzXMe-j_u1rEE5yWdQqoR44mJc4PC3ptA2WFtRLUi6lOXGOrIgBlL95WFUezaWeC45IAeoWRhdClWVo4w8aCEe9U2HmO4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی که فرمانده سپاه بود و سالها فرماندهی جنگ رو بر عهده داشت
اینجا میگه مطئنم که مسیری که در ذهن مجتبی خامنه‌ای است، بهتر از مسیری بود که شورای عالی امنیت ملی رفت.
مجری ازش می‌پرسه خب اون چه مسیری بود؟
میگه : نمی‌دونم ! نمی‌تونم که ذهن خوانی‌ کنم!
فقط می‌دونه خوب بود :) یه مشت چاپلوس !</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6134" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6133">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYwJRrFM_VP3radkVlzHIDg8s455nEZZIMax2XKI6FX_Gngb-rUaoBnWPJCPIsbhtL29yROZdW6ljblDgaIPzsA0sWbtQUramQgvxNV_B6NSB8cOsFRyPivsFofS-Nmj-Z6-gK4vcm8EhqMRjUmYZ5b2rLeK0mjoYewKBuagQxqwvhSMjsS1HAwfUAKAjYX7QyZDF6P6_t_cdjPhmS744LYPckditmsUp3Kv6k4JNBXeu_AKzH5t5UA-G50_CBLlYfAhxOX3mQi5-oZb1S24d08-tAnFjpXqW4tNBDf1IhRQMq_L4fBkW6bVt6Chk37kXbsb1FaqL5kAhoW9-Gm2nQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6133" target="_blank">📅 15:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6132">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
سنتکام : به تنب بزرگ حمله کردیم.
در جریان این موج ۹۰ دقیقه‌ای از حملات، با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی و محل‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را مورد حمله قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6132" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6131">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">حمله امروز به چابهار</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6131" target="_blank">📅 14:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6130">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
ارتش: «آمریکا بامداد امروز با شلیک ۱۳ فروند موشک، آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور را هدف قرار داد
دشمن به مهمانسرا و اماکن نگهبانی پادگان حمله کرد
‏ ۷ تن از کارکنان پایور و وظیفه تیپ ۳۸۸ ایرانشهر شهید و تعدادی مجروح شدند.»
‏</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6130" target="_blank">📅 14:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6129">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
سنتکام : از نیم ساعت پیش موج تازه‌ای از حملات را آغاز کرده‌ایم.
(از  ساعت ۱۳:۳۰ تهران)</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6129" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6128">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiI4bw9YV-GauCyLrauwTdPQLLgPLWMO2MLHGfMUI9_L1ciWowqebGwpxNS62W8_i1UHu7lqHB49rIox0aT6L6hiYr55ki9dwRtawZV7d80rBcmhRhVFm3ujZxXrNGgZsEhpZB22EI_El7k9I7HC57EPC62mELJS1bzBN94Ny6I_QEr2oRgq0b3eq9N2uepEZT3GKVaUrwH69lTzL4C0bJWuaWuu4bQkpnqueRkcDVzlrDMR5CJHXBxgfOAvp8KkCjGhFWBy80tFNUgMR0yRjXtYDcnEy7mLcXHiW2DzCeDMhCs1HAySNZ78a7RgdqXE4EQw_5_ELOYG14rx4bCZMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابل توجه ساختاری‌های محترم
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6128" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6127">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=BEiRom-jyVo5cnT0wPPzDgYTPaLIk8EiVTwKQQP54G2h2df7JYbknhLfYxKlutDLDWwDjHKZ7Lt28D90Vs_ZfAD9c8kZVUiHkA5rxAHhYdaIH5ZmFI9ZtOrTcLRblbrP80SkRrsqvIW8Ld3DvmyQVA5byvebruAj3BzFB8STt1gqt-cS4y4a0AoLae8WroBtfIzElE_tesUHcY9E4SLILN6Si86q0QNKon-IqftR7clKEQ7VCR6vsOr12HWSotwutLRaujgmITK4OGPgMhycNYwf_qBYdfwaHQgL-ANwPeU9ou76EiqYWrnAnNUAiRySBmXTANrNUuKJ-XHCSCjdZwrQ15d02s0aQPHQm6wjfFx5yDimg9yWSQi8Fj0xBhq4-KqXdGE-qwQLODVmXAvkg2dMYAaaH2bWgOjaxVHGpv5fV-ZmWME0bOWy1r7gCQG5Wwz3256Fwpi62qv0qyYCqemw7vMm0CIc1-vNJTslps_HE7OGvsUZWu0ZEpScX--vo3yRqjIWnMvCEr4MOkAjwpRPSY4vkNzo3QTppFASXhKDILdN0xSYXQfuHsHiIXUCnxnG7wmKyZ8paLoelT5a7ulmoRVR0pK3L0TZFbLQ9dxrtycRh8CvFu-5BucNky1FoZn5txt9aeCSyFh8xQR4DOoEwjYNht4I2fjaPd5MXTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=BEiRom-jyVo5cnT0wPPzDgYTPaLIk8EiVTwKQQP54G2h2df7JYbknhLfYxKlutDLDWwDjHKZ7Lt28D90Vs_ZfAD9c8kZVUiHkA5rxAHhYdaIH5ZmFI9ZtOrTcLRblbrP80SkRrsqvIW8Ld3DvmyQVA5byvebruAj3BzFB8STt1gqt-cS4y4a0AoLae8WroBtfIzElE_tesUHcY9E4SLILN6Si86q0QNKon-IqftR7clKEQ7VCR6vsOr12HWSotwutLRaujgmITK4OGPgMhycNYwf_qBYdfwaHQgL-ANwPeU9ou76EiqYWrnAnNUAiRySBmXTANrNUuKJ-XHCSCjdZwrQ15d02s0aQPHQm6wjfFx5yDimg9yWSQi8Fj0xBhq4-KqXdGE-qwQLODVmXAvkg2dMYAaaH2bWgOjaxVHGpv5fV-ZmWME0bOWy1r7gCQG5Wwz3256Fwpi62qv0qyYCqemw7vMm0CIc1-vNJTslps_HE7OGvsUZWu0ZEpScX--vo3yRqjIWnMvCEr4MOkAjwpRPSY4vkNzo3QTppFASXhKDILdN0xSYXQfuHsHiIXUCnxnG7wmKyZ8paLoelT5a7ulmoRVR0pK3L0TZFbLQ9dxrtycRh8CvFu-5BucNky1FoZn5txt9aeCSyFh8xQR4DOoEwjYNht4I2fjaPd5MXTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سفیر اسبق جمهوری اسلامی در روسیه: مطمئن باشید اگر ترامپ را بکشیم نه تنها هیچ موشکی به سمت ما شلیک نخواهد شد، بلکه عقلای آمریکا با خوشحالی جنگ را تمام خواهند کرد.
کشتن ترامپ هیچ هزینه‌ای برای ما ندارد و با کشتن او جنگ هم تمام خواهد شد.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6127" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6126">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟  به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6126" target="_blank">📅 08:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6125">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUZkQZBi5DQMgAq0Ak43nuz0XteRvBG43-EGBv4lRiEMhwmtxkyzZCp-bZSFCg2Ju32YQHL2ffhVRZyp4RQE4F2Yb84ChLIxeaMmLB9DEccGeZYfr82ohnWWQOqGzLhugWnHQPA4Mnq2xYyEVdNQJw72eKolPw7x2hbmLw4I-p62dlOnf5rai_bB7y0ViOXFImsFccffvn7jt44WKbLt2OBxtgmlDyWoNvvZ3sN-Djxul0xLAzydQJwnsKYdmeAChrp87irdqLhrkEffErlLpKG35ou5LA9BcpKfwFsHmyFV74ydA6ujxCLp8m4Zirbxag5Ce-ubrs1YpY9UgHAu5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟
به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت کاخ سفید برگزار کرد.
به گفته سه منبع آگاه، در ابن جلسه که ارشد‌ترین مقامات نظامی و امنیتی آمریکا در آن حضور داشتند در خصوص گسترش حملات صحبت شد.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6125" target="_blank">📅 08:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6124">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=ftzrVPCGUjms8upJYiWhbV53NCWlmh2E6IG6fZ_NW_OHHTjKLiKddKaFZS99j6g-r_GeKAOdaFpUjuNia7HtL-_vsGMTnC4_4RaFub23HtHQdJP_nbsR6JLDoJPdY8zQOZGfPjBflU3MR87JAZQm_z3Fn3ctAO2E5FGjNGkpnYvTYmApLoFQ1JK8BV9TT8lj_eBpMukV9vciPrvbI-3ukFeDj2_KtzErZaI6mqchhW0qTtEB_-2ykwLKpGpe-w_nobY5GrhEerDGWtt3o-90mStvZXNdBy9ibX2QxfuFa5y4AxTqAK_1uynFRLBquSUUrNtfiQSxM1-rTGOhFV7AlYVeTnK3Z7RXJBPl9ATyfIG-9jMCcqCAZ8gpt4T__JYs2tiaT2OlVBYcnoYWiuy1of0rRQfzvcJ5JYduJjnW4oIVnmK9doriXrCVU1dEmKypWfs-T54Rv3Ee8TSurzuSrMHKk2HD4s0HcWUr4-Dvd_7lNfnBasvD2TAaF2Yj5lFk1KwfBXMrxLeHjiz_dnLKQKtxzBufQJ6qceK3eyqeA9j9Qx5oTpyHrQhs7MK-M9-osUJPrSu6P5FwyPf-JRt5ZxHzS79SEbsf116li3Gj-VpP__gA0Ay5MWyOxaQR41tETgXLzxafu841ZTHI5BHq_WEljIgSxen10G3d2N8o9kE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=ftzrVPCGUjms8upJYiWhbV53NCWlmh2E6IG6fZ_NW_OHHTjKLiKddKaFZS99j6g-r_GeKAOdaFpUjuNia7HtL-_vsGMTnC4_4RaFub23HtHQdJP_nbsR6JLDoJPdY8zQOZGfPjBflU3MR87JAZQm_z3Fn3ctAO2E5FGjNGkpnYvTYmApLoFQ1JK8BV9TT8lj_eBpMukV9vciPrvbI-3ukFeDj2_KtzErZaI6mqchhW0qTtEB_-2ykwLKpGpe-w_nobY5GrhEerDGWtt3o-90mStvZXNdBy9ibX2QxfuFa5y4AxTqAK_1uynFRLBquSUUrNtfiQSxM1-rTGOhFV7AlYVeTnK3Z7RXJBPl9ATyfIG-9jMCcqCAZ8gpt4T__JYs2tiaT2OlVBYcnoYWiuy1of0rRQfzvcJ5JYduJjnW4oIVnmK9doriXrCVU1dEmKypWfs-T54Rv3Ee8TSurzuSrMHKk2HD4s0HcWUr4-Dvd_7lNfnBasvD2TAaF2Yj5lFk1KwfBXMrxLeHjiz_dnLKQKtxzBufQJ6qceK3eyqeA9j9Qx5oTpyHrQhs7MK-M9-osUJPrSu6P5FwyPf-JRt5ZxHzS79SEbsf116li3Gj-VpP__gA0Ay5MWyOxaQR41tETgXLzxafu841ZTHI5BHq_WEljIgSxen10G3d2N8o9kE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مزدوران حکومتی شعار میدن
«جنوب ایران نکند جنوب لبنان شود»
عجب! شما دیگه چرا؟
خامنه‌ای میگفت «جنوب لبنان الگوی پیشرفته
و موفق مبارزه ایمانی است»! سالی یک میلیارد دلار از اموال ملت ایران رو میدین به گروه‌های تروریستی اونجا  و تبلیغ اینکه ما اونجا پیروزیم و …..!
ولی ظاهرا اسرائیل در جنوب لبنان چنان درسی بهتون داد که الان خودتون هم میگید نکنه بشیم شبیه اون «الگوی موفق»! معرفی شده توسط خامنه‌ای</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6124" target="_blank">📅 07:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6123">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=by_PbSzWvtCgbuj-hw2MMKkJmn1sabZhUjNwEkwt-YpnpCAp2W8pfYoLhYtEMrJBc52MMMpxQehkVdDSLZ5IXqTA_uB9-e4u-tkDg9KLSPnuMlpLKFGid7L_viQvo3DGPulilJf_xEI9b1-IXg_QmbJcQaBqpBSdvLhJagypVbEdqc1oWoP1YexENE7Q8OC_tEyEtzM6JdwlHOQ1d9iFwV9fnDBlh1-HoO271wYw-8hpfPJ697iuRamDdPG35lI-Kft-v4cUB5pnbz0haiKC1TaZiP0oIecFJu63OopcMfpBiqvSy5DYXApT57HVV3Bn4jqr3Xrn_kRdvaLjmt2bTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=by_PbSzWvtCgbuj-hw2MMKkJmn1sabZhUjNwEkwt-YpnpCAp2W8pfYoLhYtEMrJBc52MMMpxQehkVdDSLZ5IXqTA_uB9-e4u-tkDg9KLSPnuMlpLKFGid7L_viQvo3DGPulilJf_xEI9b1-IXg_QmbJcQaBqpBSdvLhJagypVbEdqc1oWoP1YexENE7Q8OC_tEyEtzM6JdwlHOQ1d9iFwV9fnDBlh1-HoO271wYw-8hpfPJ697iuRamDdPG35lI-Kft-v4cUB5pnbz0haiKC1TaZiP0oIecFJu63OopcMfpBiqvSy5DYXApT57HVV3Bn4jqr3Xrn_kRdvaLjmt2bTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6123" target="_blank">📅 07:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6122">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=dKkGQlsVnoz3OVnK5XXw5F8Nl9MCpXLVQRr6_JsWD4R62sGCDy6HH0xXIegf8eWQEtVEz6ZocyWE5MKqVi9gP9k5hkOUCRa45eEmgRhG3nTF9EXSWPCkEZObDdhE8S4h3lYimEUseHjkP0ImVuio065QAwglMz3lB6UmWeO1KiQKGoUVhatviXwVq3fAxi7MNbXk5iMbmVrE-7aFJcP_T_1PJ21UIAJ5wvvMuZY7ridugOUZEBiiIS4R6RwFagnIdywJ3wIbVU_P-L6UC-Lyc_lifqYPQcmVHeivx6GyGbaw9g5ZxwmpJ8SKCJSpdkCGlLbLy2P0AYN_vUbcot4qP52E4Ljpw7kUsovOILhmmy87zqvipH-WpeQawj324IFc2DZeitLB6qvXTWImXrlytxioOAqYdSo-jciyLE1qDlg_QIC3orAWCd8CQ4wgd2z7xtP6Yljb5WNWJT01qhcH9sg8AWO1NYQVybESX_mXDdZ7C9HP-4ZDLVN4Y6YyroIIzCWExCLYNh6hoQkf0f8I0j5bLocoaHnq7e3jMDJUjH2MgKq58SEjsJolRIbsVwqWaSI2QIE_vmG9K1mqHZhfbHWedRSvFr0mMWDIplS0rSb1FQRhV7q2RGFnQvJEDR1GgtSvW65d6MUvM7rMHyqhVnAtDBFNFTzUB_2ct4MvMXE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=dKkGQlsVnoz3OVnK5XXw5F8Nl9MCpXLVQRr6_JsWD4R62sGCDy6HH0xXIegf8eWQEtVEz6ZocyWE5MKqVi9gP9k5hkOUCRa45eEmgRhG3nTF9EXSWPCkEZObDdhE8S4h3lYimEUseHjkP0ImVuio065QAwglMz3lB6UmWeO1KiQKGoUVhatviXwVq3fAxi7MNbXk5iMbmVrE-7aFJcP_T_1PJ21UIAJ5wvvMuZY7ridugOUZEBiiIS4R6RwFagnIdywJ3wIbVU_P-L6UC-Lyc_lifqYPQcmVHeivx6GyGbaw9g5ZxwmpJ8SKCJSpdkCGlLbLy2P0AYN_vUbcot4qP52E4Ljpw7kUsovOILhmmy87zqvipH-WpeQawj324IFc2DZeitLB6qvXTWImXrlytxioOAqYdSo-jciyLE1qDlg_QIC3orAWCd8CQ4wgd2z7xtP6Yljb5WNWJT01qhcH9sg8AWO1NYQVybESX_mXDdZ7C9HP-4ZDLVN4Y6YyroIIzCWExCLYNh6hoQkf0f8I0j5bLocoaHnq7e3jMDJUjH2MgKq58SEjsJolRIbsVwqWaSI2QIE_vmG9K1mqHZhfbHWedRSvFr0mMWDIplS0rSb1FQRhV7q2RGFnQvJEDR1GgtSvW65d6MUvM7rMHyqhVnAtDBFNFTzUB_2ct4MvMXE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا میبینم راست میگه …</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6122" target="_blank">📅 07:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6121">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzbh6mEwnfBLE2xXub2t3vNlqyJvjSGA1pJixFpnyhZ59sx3xwzqEsSJl1Wmo-lEK35aXGLPYu2rpW9orowSrFDUsHhHyRN9MsOi_ETLjNWRmQ4mu8z4j-X8Dqnl_h_R0R73YcJP5FfUifK1Ky3XtIL_rXt5H5O1ovKF2XTaOP5aFeOx-SCuolKMbSgVLKaKyJ0Z7cF08BfIsu5JZ-P4G5VgYpJen-rXXZadV6jXAT4UuuJBGZX6E9xZmKwR8jOyRjkuyqASIS0nqaW9Vq_8H00x71EWEWflYYUfO6z3R0Idj0aG5OuO1LrFfhlFcBdFL8PGm87W2MSgHI8sZdOjjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6121" target="_blank">📅 06:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3PiGPasAdd644PJDgYOPNGCa-wrDwl4dTc5vUN9PYlwqKXvFDkDfIrHRzXVLH6TW6IzMf5umQUmTlsOd6q6OjNKLxqk7nFylIOs7lXzQAF86v14RgISrUJdaV8pWpzLTaNX8yl36PrIoTiN3q5vhYo7kQIMCA39IlDPIANejdviGTKm-QiGP6AEMDQXyH_OwYceluv563q-q2nrKBmRuHdumT6HVpmR3PWkSBb0wCgGh5gLuiyxlBnk6X-GnoWlYRkT91tum0JpKaBMUMx05Sg_6dhp0uBmaSLaxp-eYpnECk4Zeo0576mbWnV6kkAI2c5VdCClNvrRaMVzC_2-ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6120" target="_blank">📅 06:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6119">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=l7NUdm5Sb5SLLpc-i9ghKHIp_zY-NJv5rVcpcpeY8SKEWOZe5KymsKsE0CVDzgfg_lo2JyKlg-NBf7NsXu52A-gqUMXzbkMNUJwWydW1kzAoyKupPuzSDSaF7XaCMH1euPLujRfH2qH5BkMa_8Uhb6eBrMMj09SI2Jb5o8X99e95AxYB5rJ89q_oPRFi0mbZdTJRZg1d8PxAvCTXKzHuGTkUGUj2Tv8XTUD3BdCCwpwgePXR1uVLzymFEHFmDEm9SwbP1l92Vj1A9cWPIyfA3gdHnUcGnpc5-nM8z66O8IjyI5kYL5o9YqFeN565GC1w3t2srrvbx9245KttaKPTGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=l7NUdm5Sb5SLLpc-i9ghKHIp_zY-NJv5rVcpcpeY8SKEWOZe5KymsKsE0CVDzgfg_lo2JyKlg-NBf7NsXu52A-gqUMXzbkMNUJwWydW1kzAoyKupPuzSDSaF7XaCMH1euPLujRfH2qH5BkMa_8Uhb6eBrMMj09SI2Jb5o8X99e95AxYB5rJ89q_oPRFi0mbZdTJRZg1d8PxAvCTXKzHuGTkUGUj2Tv8XTUD3BdCCwpwgePXR1uVLzymFEHFmDEm9SwbP1l92Vj1A9cWPIyfA3gdHnUcGnpc5-nM8z66O8IjyI5kYL5o9YqFeN565GC1w3t2srrvbx9245KttaKPTGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام فیلمی از حملات خود به ایران منتشر کرد.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6119" target="_blank">📅 06:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6118">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=fGKF4BpSN4u_qHIV4Q-ujFCmIVexbMTUl8npn6LSfFnkQr26JzKqbiLeD9yYgvCulEu0R0ZDX2uYl8Ww2AwvwUpT8scxUjy5HkUDi5HT-T8BLeQg_HFQyVeX-vRQpAq2Oz8_7knujHf51Cb_mLFcRQXPlELD2dIqd9omBPf0bO095qEQTBOsSp_1gPNwkUmm-dZOXWyHUFPzPStvl5Tu5vTJ4Cw4RSYfEiczOpNxGzq6exPeM4vW47x77UW6hj09T2NlylH02e2eEvjM9eNjco60O6wTZvG3yfrV3sw1JfRX54MRbvsHcS0YtHOvE-Pry1oFHly74nLuqTOGjcQdwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=fGKF4BpSN4u_qHIV4Q-ujFCmIVexbMTUl8npn6LSfFnkQr26JzKqbiLeD9yYgvCulEu0R0ZDX2uYl8Ww2AwvwUpT8scxUjy5HkUDi5HT-T8BLeQg_HFQyVeX-vRQpAq2Oz8_7knujHf51Cb_mLFcRQXPlELD2dIqd9omBPf0bO095qEQTBOsSp_1gPNwkUmm-dZOXWyHUFPzPStvl5Tu5vTJ4Cw4RSYfEiczOpNxGzq6exPeM4vW47x77UW6hj09T2NlylH02e2eEvjM9eNjco60O6wTZvG3yfrV3sw1JfRX54MRbvsHcS0YtHOvE-Pry1oFHly74nLuqTOGjcQdwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : امشب، فردا و فرداشب به سختی به آنها ضربه خواهیم زد و هفته آینده پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد، مگر آنکه  مذاکره کنند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6118" target="_blank">📅 06:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6117">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caeb092620.mp4?token=lKjXW17bxmrwABVBdmukm0wtGFB8lC12_l5B2n-mEXSJ1dh1WpQtA9I9Mg5D5l-Q6YRgoG5ChOlSgXt_uIZZzVoF-gOYYiu5iYPlbCs5OQezERRGAWW5H6AKjFhfcm6ZgtRZmfvThN2sPvbcHe4exU1mbt7ChRiOvnfVqZMRv73bsHtsQ007syTSSBs42zd5dWKgbu4WLz-5Pjnz_dn326pgmXZEwzk3X1DTHMIlTiBvoLWoxUOsoJUNc8cC-itr-J9kfhQzIcoKdHPzlxfPh57aanvu6PV7obaZ6GMT4PTIbEtL0PYxXy52osO6wZsn1oHQbfAkAHMkwH5dGxx4gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caeb092620.mp4?token=lKjXW17bxmrwABVBdmukm0wtGFB8lC12_l5B2n-mEXSJ1dh1WpQtA9I9Mg5D5l-Q6YRgoG5ChOlSgXt_uIZZzVoF-gOYYiu5iYPlbCs5OQezERRGAWW5H6AKjFhfcm6ZgtRZmfvThN2sPvbcHe4exU1mbt7ChRiOvnfVqZMRv73bsHtsQ007syTSSBs42zd5dWKgbu4WLz-5Pjnz_dn326pgmXZEwzk3X1DTHMIlTiBvoLWoxUOsoJUNc8cC-itr-J9kfhQzIcoKdHPzlxfPh57aanvu6PV7obaZ6GMT4PTIbEtL0PYxXy52osO6wZsn1oHQbfAkAHMkwH5dGxx4gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ناشی از حمله پهپادی امشب سپاه به کویت
گفته می‌شود مخازن سوخت ارتش آمریکاست.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6117" target="_blank">📅 06:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6116">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360d24e506.mp4?token=UqFecKZ279YnABbkNxUGZtIPKUolm-rIoLWPXzggj82AtuVkPNsmmIM_JHZffz-cPUx5FQypJz9XKKV-CtSB7oe92k4Xe71L7LQCy6Nw_Ytj3tpbqcNtZ4_RxsWyAN4KLCQqtYqeQvlcApbfgar7R6Fc3YHi2mFIbW2K0Dwccg5pU28YPqU2dPcCAPRuC0qj8wugh0l5SfJiXlcB_HyYHzbFit5wLmptZhYxpkmjN9Mgqqrpgkz2BGMq7uUBkNB7I6HDqI5xNKG5SkX8inRuZOxIK0rKZSgdIwk8hOwlTocvNIER51R-H3BmAyUisK8UxAAtPXatk9j7fy4ZoE-m6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360d24e506.mp4?token=UqFecKZ279YnABbkNxUGZtIPKUolm-rIoLWPXzggj82AtuVkPNsmmIM_JHZffz-cPUx5FQypJz9XKKV-CtSB7oe92k4Xe71L7LQCy6Nw_Ytj3tpbqcNtZ4_RxsWyAN4KLCQqtYqeQvlcApbfgar7R6Fc3YHi2mFIbW2K0Dwccg5pU28YPqU2dPcCAPRuC0qj8wugh0l5SfJiXlcB_HyYHzbFit5wLmptZhYxpkmjN9Mgqqrpgkz2BGMq7uUBkNB7I6HDqI5xNKG5SkX8inRuZOxIK0rKZSgdIwk8hOwlTocvNIER51R-H3BmAyUisK8UxAAtPXatk9j7fy4ZoE-m6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی با موشک‌های حاوی بمب‌های خوشه‌ای به بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6116" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6115">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
ارتش : به پایگاه‌ها اف ۱۸ های آمریکا در اردن حمله پهپادی انجام دادیم.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6115" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6114">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‏امشب اتفاق جالبی افتاده، به محض اینکه خبر انفجاری در شهر و استانی منتشر میشه، مسئولان جمهوری اسلامی سریعا مصاحبه میکنن و میگن دروغه و همه چی آرومه!
‏اینطوری مثلا میخوان صورت مسئله رو پاک کنن.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6114" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6113">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adqpVTvkznsfGiyJh8r-5_jmKOZMjYSa5UL9wBJ5TcH9jibTIC-8Xxb4imVBU1liJOHTCt97XWB9sD77tp2PWhw0-mK-JcHuLia_4B2SjDFS6_KBNrYf0X8oCkxn1gIKzB7f_qmEhg7BZYcHKcZj3eWilqussebnZ3JMfxs91B2-kRCRn9iL3qkeUeCQs6QhI5x65GQlWyFGdjOCIlZ32yMUcv6mic4JRgqtBsIuLY9-FqFPZ_Xqy2zMop-I5mp3FJPNrSWI6svLFlVy62Xsz5JUD7ox6bga2m5AL8DQoS0QFByeNjIX6XSSZXm6-fCGxiKyvkbNGYLOIPujmPELmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگارهاشون می‌نوشتن که کشتی‌ها دارند  از مسیر عمان رد می‌شوند، تشییع جنازه،  بریم و کاری کنیم که  کشتی‌ها مجبور بشن از آبهای ایران رد بشن  و شروع کردن به حملات به کشتی‌هایی که از مسیر آب‌های عمان میرن.  به زور حمله میگن کشتی‌ها باید از مسیر ما رد بشه.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6113" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6112">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6Er1r3G0tGThWiGVM9UesdgEGBm2eI68NFGVBAm3ERZEc-w69ommhIa91ZAHMIt28kmzG4woWMvKJ7LS8-PrUW50OBDKNuQyy3IGBdDtBXiaXtHHXleldx-OblWAg9J0hcF_Ijg8QNnsW-g225n0AGFMcE3fNoo2VxtJ60OuEtW7XjVfpTo9Vjy5xlFLOCg_XkO37KINEUWTfHu7pQo8GZ4aUQO_obaJzk4aVO3k0qMMDx7msZEZhV4o31WR7EAGmoThXd7E6X3_ijMdYzgpKfFNbG6i85ArNS41R4v49ihnsoWaowJ6n1TvAmDBmNP-qQNW_874FMO674ttQ9KeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا در حاشیه خاکسپاری جسد خامنه‌ای و جلوی قالیباف شعار میدادن «مذاکره با دشمن خیانت است»  هنوز به سه کشتی حمله نکرده بودن و نزده بودن زیر تفاهم نامه</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6112" target="_blank">📅 00:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6111">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=Haws84Wx6gYwChD7zexvMnLzsGBIXxGYGQ6nPDRqrXrj7qGlPHhZgN4xw7xciCJWnjc4SXtq9KwvFLAm8fy6VFBDUz_QcyyXokLXoy7EL4d8ksYR44CvCmcgmEd-bmayN1hEF6_pOp0-InSPnrPdkCPvglnNrUjkXI_-2SZl1J1j4yApKfkPXtbuWlcDKodR0uqDn4SbdmRThf8Hd2s-I4GUTLaZ73xdyWwwhaUNHWmRE0WQZ5Wb3a1hoe_Qcaq1CeGdinTyFaAOp9Up9W7LpAaAzPsy9Hot2V3w9Pby7keyb6H59_Zaw-oSDwAVZmVGVjjdQQDguGiQihZnw1ESlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=Haws84Wx6gYwChD7zexvMnLzsGBIXxGYGQ6nPDRqrXrj7qGlPHhZgN4xw7xciCJWnjc4SXtq9KwvFLAm8fy6VFBDUz_QcyyXokLXoy7EL4d8ksYR44CvCmcgmEd-bmayN1hEF6_pOp0-InSPnrPdkCPvglnNrUjkXI_-2SZl1J1j4yApKfkPXtbuWlcDKodR0uqDn4SbdmRThf8Hd2s-I4GUTLaZ73xdyWwwhaUNHWmRE0WQZ5Wb3a1hoe_Qcaq1CeGdinTyFaAOp9Up9W7LpAaAzPsy9Hot2V3w9Pby7keyb6H59_Zaw-oSDwAVZmVGVjjdQQDguGiQihZnw1ESlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این استوری رو ۶ روز پیش گذاشته بودم  میگفتن آمریکا میخواد آتش بس حفظ بشه ولی جمهوری اسلامی باید «کار دیگر» بکنه!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6111" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6110">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550f13e765.mp4?token=tGxGaWTSlXFbQOLEX0K849xuasiakmEbsywayj0O2omUaI-JCjf0eGoJAdi6GyoXTI7UX8gfdeXjPFvEJCQKls4xNlag7RpG_rOPeDr5A5VEJc1W9YghSbm3GYIPZUGrBY_8ULYs1FzxUqsyOVUNU9va-QGELuNy3W7kSKmU6rLWQLT5QmcrGKkmX1S8_qPbMZiIDqxqkVCU2DHX0cDVn2hsfynljD13U0SO8xR3LwrEGJ7VQdP0JVnalq7eyDmT4bfH9ksYMbg9-vZNZF03V4nVk-Kv0N-QWCnAP62wYmuVdKOx9CTbIBKIBhvDRAghqJz176Bx1Zlhem9F4wSvVKoDgsQRBo3lCLHOIW-eisNa_DRq4_HHuAk4ou01IPydU7TTl_gcB5_g9tFlyhyDNYdl0DR5Lcfr7irpdobpk-p1XUv53jaMoGhANfomJiIMG-3mY5AINjNf8aqixDpvir86oyqtpS5_Cf-YVHRSLX4LuwG1XiQFNS1WYVHVnRxGNGbWB69y_WXPYWEpjfe-b4irGBpvyuR86HwRFEXk8qcEdL56HkQl_3P_sVBUpm7b8HTLpBTNY7yIL87vVZuA33Nib7oNeNOFqVPUieT4GkRNkAjeafdzO_zVF3begKuWtGAvXmYmEofiaoEz4wYufp9t_d3hwr_xggE04QCvk0M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550f13e765.mp4?token=tGxGaWTSlXFbQOLEX0K849xuasiakmEbsywayj0O2omUaI-JCjf0eGoJAdi6GyoXTI7UX8gfdeXjPFvEJCQKls4xNlag7RpG_rOPeDr5A5VEJc1W9YghSbm3GYIPZUGrBY_8ULYs1FzxUqsyOVUNU9va-QGELuNy3W7kSKmU6rLWQLT5QmcrGKkmX1S8_qPbMZiIDqxqkVCU2DHX0cDVn2hsfynljD13U0SO8xR3LwrEGJ7VQdP0JVnalq7eyDmT4bfH9ksYMbg9-vZNZF03V4nVk-Kv0N-QWCnAP62wYmuVdKOx9CTbIBKIBhvDRAghqJz176Bx1Zlhem9F4wSvVKoDgsQRBo3lCLHOIW-eisNa_DRq4_HHuAk4ou01IPydU7TTl_gcB5_g9tFlyhyDNYdl0DR5Lcfr7irpdobpk-p1XUv53jaMoGhANfomJiIMG-3mY5AINjNf8aqixDpvir86oyqtpS5_Cf-YVHRSLX4LuwG1XiQFNS1WYVHVnRxGNGbWB69y_WXPYWEpjfe-b4irGBpvyuR86HwRFEXk8qcEdL56HkQl_3P_sVBUpm7b8HTLpBTNY7yIL87vVZuA33Nib7oNeNOFqVPUieT4GkRNkAjeafdzO_zVF3begKuWtGAvXmYmEofiaoEz4wYufp9t_d3hwr_xggE04QCvk0M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو رو دو هفته پیش گذاشته بودم.  معاون سیاسی نیروی دریایی سپاه اینجا در جمع حامیان حکومت بهشون میگه خیالتون راحت باشه، حملاتی که ‌ آمریکا انجام  میده «واکنش»  به اقدامات ماست!  «کنش» نیست!   تمام این ۴۷ سال همین بوده!  یه کاری میکنن ، تنش راه بیفته،…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6110" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6109">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6109" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6108">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=N_h3GVVyYbocx0aI_Wd18V_O40sUcbkQ3e7oQVIV6tL3-5sbHr2zfADN-Y9MbY0WE_4nDQciV63aKKaPm-9jxGTrlOXA6WnccUZZvbTZrOMcLESpTYMglRN8rBX63ILXtfPOb7XhKLk0SLkacN5E84VyGTo9a-RiCpibJCiNCWvR3EPhVRGxiofOsHr8jVnKB9mpRDz2SgEmhIG_Q4BozbeH5qdkYzOsAHXNNkeFZWpUWAmIbGeZnZBtw4Xriw0--iRgP40_Sx3qZCzTePBr5uqta5BgTIhWRhYJ2jzJpAzI2Yv6mwupp-Ojs17-w7dLW5xadfSRqgaiOuSxGt5_2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=N_h3GVVyYbocx0aI_Wd18V_O40sUcbkQ3e7oQVIV6tL3-5sbHr2zfADN-Y9MbY0WE_4nDQciV63aKKaPm-9jxGTrlOXA6WnccUZZvbTZrOMcLESpTYMglRN8rBX63ILXtfPOb7XhKLk0SLkacN5E84VyGTo9a-RiCpibJCiNCWvR3EPhVRGxiofOsHr8jVnKB9mpRDz2SgEmhIG_Q4BozbeH5qdkYzOsAHXNNkeFZWpUWAmIbGeZnZBtw4Xriw0--iRgP40_Sx3qZCzTePBr5uqta5BgTIhWRhYJ2jzJpAzI2Yv6mwupp-Ojs17-w7dLW5xadfSRqgaiOuSxGt5_2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گشت زنی اف ۱۸ آمریکایی بر فراز چابهار</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6108" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6107">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا : محاصره دریایی ایران وارد فاز اجرایی شد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6107" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6106">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
چندین انفجار در بندرعباس
🔺
چندین انفجار در اهواز
🔺
پنج انفجار در قشم</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6106" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6105">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyJnj8LSlnuG_Jtm2Ax_EQRGFXoJD08WVA6YguZ5l4slrAfmxvDiqnq4gXPMljIAEiWWxEGFywvwUWIim2J3-kInCMfpDDhNaxGfMPmMXFMnkeZ6TVwX6yS7So2DxxoJBOMOPvT3n9zyQkPezAtfumpMbn1ZPs7Cz5GshNtLQvBjOzkyaEhYG9VVtHvvyMHQz-doDxecQZGwWOBw3_p_L5WsTIlPH3jaN_XjMhUQo_HU39fspfUASqoYtgQotKEN4RwY0lAu2Wk2qr3o8laR2H0nYa-Qu5U2PhDMrU0KFkBNzn7k1yOrULjaUxXtZ-IlvKcsW0kzYa7pBHZ_1D7e1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2077085449948938568?s=46</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6105" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6104">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
دقایقی پیش : حمله به قشم و شنیده شدن چندین انفجار
🔺
حمله به یک نفتکش اماراتی در سواحل عمان
🔺
فعال شدن پدافند در کویت</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6104" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6103">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkGKtDGAqDknshi2ey9dSoN0eRdBkcejUjMSbY6q63J31AiycP3QryT3V_ZqQw4xdd2AuUrzHzs_4oH7eZ7u7JzYJYyFuTPNbbKXaq2xwMv3re1AQlZShxMzkCk4LcxGkjWHGJ-6tReNUp5ACkofMCQavfrXwHl6rEywpf2vIwo906Vhigy3Vpgz_5em0iltByaO_5xQr02p4xZE2Ip2_olnxEjUt_Y7kGF90MeYi-1AQZdwVAqz9NIpbrSLcZVk6YWqoy5qipPuneyBT1dME9E66zlCqI3P35DFChCIbMZNuZ2bAdYO5DPV-71upzgsOpWNTlljZi9FQ1fr6TsZcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهپاد‌ها (قایق‌های تندرو بدون سرنشین) آمریکایی این مدلی به یکی از مهم‌ترین مراکز نیروی دریایی در بندرعباس نفوذ کردن و حمله کردن.  گفته می‌شود که در این حمله یک زیردریایی ج‌ا را نیز منهدم کردند.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6102" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=q_uHxsMZSUFOtmlT4cK-31NQFxsV3ZhyYSeQXYM4JhRKb1XrbmSdqh837HX1yOSdg0vr-7cPC9c3LZ-ac_zVdf-lEu8ZzO2bNWOwyxfd-AXFNS1Qu-3vge6Ij-DsIoVfSEJgF0RvGaUqTAkrR5Ec4tAkFn-9AlsAvNa3zOP1colMBIMPBWh_uspKYb7qYZhsOCNPLePhFwHNHIMSFoaKnAkd8EJ4xmcVA2Yvmok9yCPq46mroTLyMiDKIK7lo_7-Qu7KHKPlIoUG2G-3d95LVNIKvzgLlVHxEJtjwzSutRhXDk2lRlDuOa6Ox8W6hE4jqs5qs-df-xx-0l2cGpgo-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=q_uHxsMZSUFOtmlT4cK-31NQFxsV3ZhyYSeQXYM4JhRKb1XrbmSdqh837HX1yOSdg0vr-7cPC9c3LZ-ac_zVdf-lEu8ZzO2bNWOwyxfd-AXFNS1Qu-3vge6Ij-DsIoVfSEJgF0RvGaUqTAkrR5Ec4tAkFn-9AlsAvNa3zOP1colMBIMPBWh_uspKYb7qYZhsOCNPLePhFwHNHIMSFoaKnAkd8EJ4xmcVA2Yvmok9yCPq46mroTLyMiDKIK7lo_7-Qu7KHKPlIoUG2G-3d95LVNIKvzgLlVHxEJtjwzSutRhXDk2lRlDuOa6Ox8W6hE4jqs5qs-df-xx-0l2cGpgo-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جنگشون :)</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6101" target="_blank">📅 16:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJ67k2u7vvDRjeLbiRUwlMQ_Xpc3-RvCmJZnD9FHzqJO8kR8ROmsRxCnhi6r9kn4fbASifOnJEAsbEhQEfSRI5vgkbwhOevnYvc7x-UPacGX4B_2oD_j_46Zq-cZpp1JFk_8ypY1-wEMjqQJp0NXe-SnsZo67G8cxtu8u9MK9ftyrEcn7ePAUtlNapJb8F3Vcl5lf2ekvTDat3NyrZRs3ec4-dYCtlV_i0zpgRRAHabyq_-WrVkj3MHfrczXg8Y4R5sdwEJrXs9GdJW6zFqDu6SL-mhoFkuQ4NeHSRD-oDbY0ZkvR-D8gGNYcWE2V94nfi3Nzmpt1lusuU9pFY-OGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.  این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6100" target="_blank">📅 16:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6099">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">۴۷ سال رژیم اسلامی</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6099" target="_blank">📅 15:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6098">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yg5dnWv4HYIEdnWMyBh8iBTY4YaFkzJTmMVf9jZ5KmoG1Qu2YSjQF7JpAjiEkGccFPSE9_k-T9VLog-0RfjBYjIemCdhBwLwCq7BVVsazuv_Ekayr9Y6u49quYqC6VXHZhwC8OO1jibL8INlgCwWOFtj_eVanBOgLTOC0eQD1z8yOv88-Al6Y9XZxONCChNzPT8I4tIwBuG_r8bYZjExatCRTozGFccEq21vcBtMwO2kbH2WY-gMHCMmsS3ikAaUqmiTVc3JuZXM-r6n5nA_wgIUCa7w26MNeitAFRA3WBR91ptEzMriy-wAgwIvERd8SEr4kGyHattYhYENr90GTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
تخریب ساختمان مرکز آماد و پشتیبانی دریابانی نیروی انتظامی ⁧ بوشهر ⁩ در پی حملات هوایی ⁧ آمریکا ⁩ به مراکز نظامی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6098" target="_blank">📅 15:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6097">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
حمله به آبادان و ماهشهر
معاون امنیتی و انتظامی استانداری خوزستان:
🔺
امروز سه‌شنبه ۲۳ تیرماه،
در ساعت ۱۳:۲۵ نقطه‌ای در شهرستان آبادان
و در ساعت ۱۳:۳۰ نیز نقطه‌ای در حوالی ماهشهر هدف اصابت پرتابه قرار گرفت.
🔺
حادثه دوم به دو انفجار شدید منجر شده و جزئیات تکمیلی پس از ارزیابی‌های اولیه
اعلام خواهد شد.
🔺
جمهوری اسلامی در این ۴ شب و صدها مورد حملات، هرگز اعلام نکرده که چه تاسیسات
و مراکزی مورد هدف قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6097" target="_blank">📅 14:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6096">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=evm2ohP3NNd92JZoS2P6F3_GZDvRn7GQW55T-haG2aAH1wJm4lxDdmF7vdG5VxPjWpp7UzPIETWgSYZbR3lh-4m8OzciHbXd8q2-z1pSsRWn5IKeVX1GUlbcvryug91SxakZKe6YuzxqNwmLLVK50F6UdxLMRO453Jg87GIQwkI2gzan1-3wm346alOfeAJk8EPaR_XBEnQv8QI-ffanWrCHYcxck0ntFo2Fj-kwJXd76nam36kSulOyovcFMeX8_AYh1H4w_E_xgsJuNpdt-kZDZLXNNdpnGoYDwjnQwmKm1FpkqAyilI1UtkI3NHPt9HQYrJrNlsnVpHUTM--O0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=evm2ohP3NNd92JZoS2P6F3_GZDvRn7GQW55T-haG2aAH1wJm4lxDdmF7vdG5VxPjWpp7UzPIETWgSYZbR3lh-4m8OzciHbXd8q2-z1pSsRWn5IKeVX1GUlbcvryug91SxakZKe6YuzxqNwmLLVK50F6UdxLMRO453Jg87GIQwkI2gzan1-3wm346alOfeAJk8EPaR_XBEnQv8QI-ffanWrCHYcxck0ntFo2Fj-kwJXd76nam36kSulOyovcFMeX8_AYh1H4w_E_xgsJuNpdt-kZDZLXNNdpnGoYDwjnQwmKm1FpkqAyilI1UtkI3NHPt9HQYrJrNlsnVpHUTM--O0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌پرسه نظرتون درباره اینکه بدون هشدار قبلی برق رو قطع میکنن چیه؟
‏چمران میگه:
‏شما اگر بدونید پریروز چند نقطه برقی رو زدند دیگه این سؤالو نمی‌کردید.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6096" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6095">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTXnEo6jRex8S1pzgD_0Foe9C6wJJVlOdIWm8fVS88rqVWECz4SBjTUYvil0aIMu0lUl7Fu9ViPYwB6fR4NJVPPl3ydjaYHlMFYHp8J2e7pKLbcPByNpdqrtbbV62MtcmZH0aVnWJdCevIYi6BToU5HuJIF9QwuAmi9QAOOp09_XUtQgHlnhHq29aCjQlxAOFj6fsy0SI5cX0bbhwU8ZZ9NriyP3gWRW-GNXUd2b9hpjqT_w9CMtzlL_edfes11RDnVN1ffXO9MDFxO53PZ_mHoZx8GppAcEEIaBd5Y2y5MAr0X13xWit5usCr6RFk_wRqwRflqlI5elas4N_gE4XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ترکیه، دیروز جمهوری اسلامی
رو با اسرائیل مقایسه کرد و گفت
رفتار این دو شبیه هم هستند.
(کاری ندارم که ترکیه خودش چه افتضاحیه، اما نشون از تغییر رویکرد ترکیه نسبت به ج‌ا داره)
یادمون باشه فرمان حمله اخیر از سوی ترامپ در ترکیه صادر شد! یادمون باشه معاملاتی بین ترکیه و آمریکا رخ داد، که آرزوی ۲۰ ساله دولت ترکیه بود.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6095" target="_blank">📅 14:29 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
