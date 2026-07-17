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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 23:29:19</div>
<hr>

<div class="tg-post" id="msg-6193">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
سنتکام: ‏امروز ساعت ۳ بعدازظهر به‌وقت منطقه زمانی شرقی،
[۲۲:۳۰ به وقت ایران] برای هفتمین شب متوالی، یک دور حملات علیه ایران انجام دادیم.</div>
<div class="tg-footer">👁️ 131 · <a href="https://t.me/farahmand_alipour/6193" target="_blank">📅 23:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6192">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029791358c.mp4?token=G_Ar6iRCUc11R-46msXg1j-h30ffm98JIWUM_SzpGtvGP2VSkiH6v26FzQLGoQY19KhOYidUnba8ufzYCyub_qzKLU_VhhDWvLbzOtRSLaYy-oWiReFzdJnQQMIb0TWkK1-PQgH6MOujJtIB58jmQNUtAp6ptaHJ_0XIkwPaWjEzzOjbWWYy2t1mBkNtFBCflgIu8CmJa2q2UlzV7VapKHbxNU-dQOz5_gMR6WptDNsw5asRpCNsXTlh-OcMLpCvpFWhP1fWA1_HzotEvuN9vfYrg5NHY4i9IEj_A8PMgUMv3MgM4UbrK6UmYpiFSOPwwWC6ekRm8mAZcKArcqP6YLd4RXvOh05J8a6kZIWNJJsVMeLY07jgEWShJl21f7IZLKp3D-6D0vJk-MW5LK87cryhTE8YTqL8przbAL2ZzG1sFF_HQuP-ABDoMvbXgS0d8_dGZphfJdUVjYmS1UjCrPgUELzEPEfzUPupwyzMRaA_LzFCtb5KJV1w3PPSwmqAW8pMuYrig_MN8XItauN08_2sCoQ03OKrQnv2aUstJkNH87yYWd6uezQRyi4jqjmmpzvRbklmTyNBVe_RgDiOJ__flx_kb1NAh45LnFFfvgx63ieag599La85voJ5hef5Ogw60Jyx3rdAf3YVfXqULA9NN3Z__PFGyg5QlxNbMQs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029791358c.mp4?token=G_Ar6iRCUc11R-46msXg1j-h30ffm98JIWUM_SzpGtvGP2VSkiH6v26FzQLGoQY19KhOYidUnba8ufzYCyub_qzKLU_VhhDWvLbzOtRSLaYy-oWiReFzdJnQQMIb0TWkK1-PQgH6MOujJtIB58jmQNUtAp6ptaHJ_0XIkwPaWjEzzOjbWWYy2t1mBkNtFBCflgIu8CmJa2q2UlzV7VapKHbxNU-dQOz5_gMR6WptDNsw5asRpCNsXTlh-OcMLpCvpFWhP1fWA1_HzotEvuN9vfYrg5NHY4i9IEj_A8PMgUMv3MgM4UbrK6UmYpiFSOPwwWC6ekRm8mAZcKArcqP6YLd4RXvOh05J8a6kZIWNJJsVMeLY07jgEWShJl21f7IZLKp3D-6D0vJk-MW5LK87cryhTE8YTqL8przbAL2ZzG1sFF_HQuP-ABDoMvbXgS0d8_dGZphfJdUVjYmS1UjCrPgUELzEPEfzUPupwyzMRaA_LzFCtb5KJV1w3PPSwmqAW8pMuYrig_MN8XItauN08_2sCoQ03OKrQnv2aUstJkNH87yYWd6uezQRyi4jqjmmpzvRbklmTyNBVe_RgDiOJ__flx_kb1NAh45LnFFfvgx63ieag599La85voJ5hef5Ogw60Jyx3rdAf3YVfXqULA9NN3Z__PFGyg5QlxNbMQs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت شانه خاکی موقت کنار پل بندرعباس</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farahmand_alipour/6192" target="_blank">📅 23:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6191">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏یک گزارش محرمانه که برای رئیس جمهور ایران تهیه شده است، نشان می‌دهد که تنها ۹٪ از ایرانیان از وضع موجود حمایت می‌کنند و تقریباً سه چهارم آنها یا اصلاحات ساختاری عمیق یا جایگزینی کامل نظام سیاسی را ترجیح می‌دهند - فاکس نیوز</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farahmand_alipour/6191" target="_blank">📅 22:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6190">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:  ترامپ به ما نامه‌ای داده و صراحتاً نوشته است: «بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6190" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6189">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6189" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvDYAVxq_VcbEn0jaAtD5W0oDdCv3M8dmdxBphtzQ5ZwVVirnEuae7sQDY784gBK6BpZHGygBOPw0ePCzEjP8oa-y21b_C8vFWf_neLyAqf_Wbd7azZZUTfH89ug8shTlr8FOJfiyueNVS0BNi_E9sxOtFj-Zr9WdrRH6t2Mx6NALQBEyBifA83N9-w67rDqsQ-p0ZkWtPrVIBSdzYdbAZQSA8jNCx7-m0U0c5ubeMLRs6Ek-tOMEEqhg4k1z2U1vhP8aJsrJfW_zhBQbml2fRWDupFkGydVYyYxuDsrZrSNuy8hEr_6_uBv2KdiOOzC0chxlBOYOHNbuxHcbjYmzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ایستگاه مترو در تهران با مجسمه مریم و عیسی درست کردن (که عجیب هم نیست،
نصف قرآن داستان‌های مریم و عیسی
و قوم یهوده) و پروپاگاندایی راه انداختن
که ما چقدر احترام میگذاریم به بقیه مذاهب.
بعد همزمان کلیساها رو مصادره میکنن
و صدها نفر به جرم مسیحی بودن
توی زندانهای ج‌ا هستن و اجازه داشتن
یک مسجد به سنی‌ها رو هم نمیدن!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6188" target="_blank">📅 18:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6187">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o23JcAiz3J-Icg3U2M2NzvMMdb40oPmFoaBYdlEUwYBjyhuN5b7h2IyB8XgQrGu_Dq7InpDe7TcU2ZambOI_wXSGPPLisXRqSm0xPvHzpWORotmFzWGypHPDRcs28w5fgyeAPgPX9tmcEit4U8j9ZNBkqD25XpgTKaBzyczAQNroCMUmhkA_u6H04mdQtYeTzyX2ghvNenOWyuC42uvE645ZfSEQuwM6bftXXPSROfKTqucxUJy8Aa9k8LJWwmH-QDEjrouQMl89LJ258sbqW6S1tVKp-PMIp46gh9b6vqZvF-z-Z8kH5YlZDHes4FG4ujPhCMiuflxA-C9mAuAtDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب طلاقش بده :)
چرا اینهمه کینه؟</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6187" target="_blank">📅 18:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pj5r17LvhYKZPKH_z4Yr62thpiFHiUk8LiH26S0LqfbzRr4anLt-I4ZlHGmLLLokjaV7l3yCbMbH_sSwpzpoZRl_bN13-AuNvNRSDhRXn_0pWfAMFXI4j00iMQrdXOrrZlNW__UkxJ6YAYYDdIKuzjK2jXSON60UJVXKLGpSiLQs7ewG1M34omN483pt1bgKdxYdtLJ4MBnsrZGMgPCBlKZyeS0uSstBfzav_2qmMuBExOvZT22uS2fGMWylDiqDPF-rg6O1gBmACv9_Vtg-0tRr1_lFJMPu0svI6UoBFTlaJtH_Ay8aPYXXW4r5GwjOUXuhxMzY67FHpPB16lEb8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل عرزشی !
من میگم اینها شکست‌های تاریخ
رو پیدا میکنن و به عنوان الگوی خودشون معرفی می‌کنید باور نمیکنید :)
تنگه احد! که نماد بزرگ‌ترین شکست و عقب نشینی مسلمانان در تاریخ صدر اسلامه،
رو شباهت سازی میکنن با تنگه هرمز
‌‌میگن همونطور که اونو در سیطره داشتیم
اینو در سیطره خواهیم داشت.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6186" target="_blank">📅 17:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6185">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6185" target="_blank">📅 15:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ijt5NRK3bltsYCoHkEWDkhrcfi5qZ--8GXUF5P3-8IK0TPqriYcGaj_rju2tJ7vUgwYsS5u9HmUMtsvwofBpwQIY_G8VauO1lhDEPE79BAXOnZcWgApkjZp8GP76Nxi2zQQ9wVFiPyWCkbhC-9yvd0w_1ZnHvvy65JIPelk236nzSTkWZJOOo82ttchl91wf8Wqd9mCD7pIa5mPzdbLXD1iNMUNym65cPe24AyUPfo20PC1xb_MnWNYdf5MmiJ0HfjfWiWjCciXf3-nfQwoVq71WQBin3R_7y7TWbh_DZcycgfxnLxzhmpI6d4g18W17wla0suaespRUpAdDgjiyJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی به تاسیسات آب‌شیرین  و تولید برق کویت حمله کرده.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6184" target="_blank">📅 14:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6183">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=JYCCchxyPd6A7ilQkz80EaXyVs2eEsT0foYs0LNA-hNCrlVX8uDIyd-GqnSj5S2pA-NoJCWDs722GN6rh_Ulp8FaQ0otBJuAQbmpJQ708RODUIsw74MXBXvtq7PL43Lw1-UcXriz7sjhxUJ_-S4b-ut0y0jgQ6bDNuTeQqHPL1cMhNAvReGvM30SDFNiUAhxndwwJO1AJzo07_DC2-7eu59ijUkCzJoG_7SBCDpUqnnqNyZzxS9d3tfNka8FoWGidqeZPqX2Fe-VYDqyVPpf4atEFBFm_dWFHWLR04c2eYcB5XOY4r0ClYFla4O8NDsMZLeR8uv-naHUfuY0s1njVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=JYCCchxyPd6A7ilQkz80EaXyVs2eEsT0foYs0LNA-hNCrlVX8uDIyd-GqnSj5S2pA-NoJCWDs722GN6rh_Ulp8FaQ0otBJuAQbmpJQ708RODUIsw74MXBXvtq7PL43Lw1-UcXriz7sjhxUJ_-S4b-ut0y0jgQ6bDNuTeQqHPL1cMhNAvReGvM30SDFNiUAhxndwwJO1AJzo07_DC2-7eu59ijUkCzJoG_7SBCDpUqnnqNyZzxS9d3tfNka8FoWGidqeZPqX2Fe-VYDqyVPpf4atEFBFm_dWFHWLR04c2eYcB5XOY4r0ClYFla4O8NDsMZLeR8uv-naHUfuY0s1njVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!  ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟  به خاطرش حتی موشک به اسرائیل نزدید؟  (که اونهم اومد در پاسخ ماهشهر رو زد؟)  خب جنگیدید و شکست خوردید!!! هم در لبنان،  هم ‌در سوریه…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6183" target="_blank">📅 14:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6182">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6182" target="_blank">📅 14:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6181">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6181" target="_blank">📅 13:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6180">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6180" target="_blank">📅 11:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6179">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6179" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6178">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=gQaoAYWVaDThIrFT6v0SMdZMNkx4TA3jclUzJzT9SgLoVyYvzuBAs6Gqhy-_N1k277GGoVX_IbMcnKXIi2CDlrcALulHj5YDfNCoc5xEiJmSd-oCVl67n9jjSyZmYi0GvVBmGcUzDtZOUCBay9OlrZL-K82Y7uepqgS64LBzJHQ9T2STfxdAwJyXZOvWXqob52USmf2qIcnLulhQS5Nx2tPylu74o9IGWjepVmiuJHO9Dm0DqB6uePJagxSEdy8Tpqe3kmyGHlbVpYfzZvIFNgyCM44qLm0sepNM26eUD5tGSKyO_EX3uoUX02PkJRi-qDv_EmDegjDMFWulTVmJPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=gQaoAYWVaDThIrFT6v0SMdZMNkx4TA3jclUzJzT9SgLoVyYvzuBAs6Gqhy-_N1k277GGoVX_IbMcnKXIi2CDlrcALulHj5YDfNCoc5xEiJmSd-oCVl67n9jjSyZmYi0GvVBmGcUzDtZOUCBay9OlrZL-K82Y7uepqgS64LBzJHQ9T2STfxdAwJyXZOvWXqob52USmf2qIcnLulhQS5Nx2tPylu74o9IGWjepVmiuJHO9Dm0DqB6uePJagxSEdy8Tpqe3kmyGHlbVpYfzZvIFNgyCM44qLm0sepNM26eUD5tGSKyO_EX3uoUX02PkJRi-qDv_EmDegjDMFWulTVmJPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی از سخنان سردار نقدی : اگه حتی به آمریکا حمله کنیم، قدرت پاسخ‌گویی هم ندارند!
با کدام پشتوانه اقتصادی میخواهند بجنگند؟ با کدام پشتوانه مردمی خودشان؟ همه جا در محاصره ما هستند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6178" target="_blank">📅 08:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=GXFlQQbFMPL99OuKitmuYM7_gpOlEx2qvvIZ7PIOj8YGh4HIcm7Qf9a69gzckHFe2P6Rybhsfz85WWpn_UYp4cVW7Rl9b56DHYLZDncL0Faokm3P68zdXk2GDl8lju5GUM8ZYPRXODiqbeJojQDpsoS49r5oL07Gu3sQ_kciZ96BimKoCZnS-ciA_qz1mF_86f_hO-Jcorra3AJ8-nsM2eRkUGgFB2pjk_giCybNORsGxvGwwGxWkoiG1hpTKxYs__RiD87pTTElgON6_LsxkvLS1nohQtEmgs4QwKdwG5uS9_n6RIKT5PPvOgpRaX8uecZdxrTHU7CpjWftT5smiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=GXFlQQbFMPL99OuKitmuYM7_gpOlEx2qvvIZ7PIOj8YGh4HIcm7Qf9a69gzckHFe2P6Rybhsfz85WWpn_UYp4cVW7Rl9b56DHYLZDncL0Faokm3P68zdXk2GDl8lju5GUM8ZYPRXODiqbeJojQDpsoS49r5oL07Gu3sQ_kciZ96BimKoCZnS-ciA_qz1mF_86f_hO-Jcorra3AJ8-nsM2eRkUGgFB2pjk_giCybNORsGxvGwwGxWkoiG1hpTKxYs__RiD87pTTElgON6_LsxkvLS1nohQtEmgs4QwKdwG5uS9_n6RIKT5PPvOgpRaX8uecZdxrTHU7CpjWftT5smiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پل  کهورستان در اطراف بندرعباس
که شب گذشته مورد حمله ارتش آمریکا قرار گرفت</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6177" target="_blank">📅 08:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6176">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار …</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6176" target="_blank">📅 08:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6175">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6175" target="_blank">📅 08:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6174">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
حملات شدید به بوشهر</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6174" target="_blank">📅 01:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6173">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=rd13S5pp3Kce2cy9fpX1B_3zEhMs-C1kBcIzJxS1W10WbsOI4Zl5yMm6F_yeys6DbAZEWPTSeHC5tQZj208lKrKKqpufGoLsElX9B44vrWhqGk_2emnFfS1GGMgXrNpIKkOP4CA0Do1etuFX_ITx412w9AeVaNzJEkEKCuEYOibKHDvYJggvv18-gu78UagO_75uaTEVCABDih44ovev7qxpfBNLdXktrjvNFLfLKv5AAi3ZSoiruio6xY1VtxnvTGdSFbxwqs0B1ZW1V8dqhlvHo8CE5uxYGm48SfztDYa5QdB8XbXUIKunTFMFOmh4OxNKB-QZrEohR_8lqFrS3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=rd13S5pp3Kce2cy9fpX1B_3zEhMs-C1kBcIzJxS1W10WbsOI4Zl5yMm6F_yeys6DbAZEWPTSeHC5tQZj208lKrKKqpufGoLsElX9B44vrWhqGk_2emnFfS1GGMgXrNpIKkOP4CA0Do1etuFX_ITx412w9AeVaNzJEkEKCuEYOibKHDvYJggvv18-gu78UagO_75uaTEVCABDih44ovev7qxpfBNLdXktrjvNFLfLKv5AAi3ZSoiruio6xY1VtxnvTGdSFbxwqs0B1ZW1V8dqhlvHo8CE5uxYGm48SfztDYa5QdB8XbXUIKunTFMFOmh4OxNKB-QZrEohR_8lqFrS3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏فارس: جزییات حملۀ   آمریکا به پل‌هایی در شهرستان خمیر؛ ۲ نفر شهید و ۴ نفر مجروح شدند</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6173" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYCu8XrF-1WqfnO07o-fr9OaKRkYH1w8FqQMzfE9ZZDlMdXe3zyxME8VlPcIdomEPmFYv6E6wgnaYe7qNwZ1AyBqGhZuogz80itTU6NtXBkS0y3gAjYL9gwZ55u7zFKCD9SOlrEVg1hYxeeZexZNr89hUAV9Ifaeqa2MaFh0Q6F_h8Cp-J3H_r2I_g6ZwkFRUt1kWI6L1SKqFJAv_IbJMHdEt9vwTzRYkyv6bY55NmmA_mcih6bOVpyK58g9LTH4SEY_vNrImKx_28PZV2h7RRdQsvVwPblwpLzBdEeugkG3pRXNeHeyQ1oHW1hZBvzV8IVIABR6U_YGDiHuKssflA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6172" target="_blank">📅 00:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6171">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
صدا و سیما :دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند.
بندرعباس مهم‌ترین دروازه واردات و صادرات کشور است و شبکه ریلی بخش بزرگی از این حمل و نقل را بر عهده دارد.
این حمله می‌تواند به حمل و نقل کالا ضربه بزند و به آن اختلال وارد کند،</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6171" target="_blank">📅 00:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6170">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
حملات گسترده به حمیدیه و شوش در خوزستان</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6170" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6169">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
حمله جنگنده‌های آمریکایی به فرودگاه ایرانشهر</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6169" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6168">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6168" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6167">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6166" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6165">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏
🚨
🚨
سنتکام: موج جدید حملات در پنجمین شب پیاپی را شروع کردیم.
🚨
مهر: حمله مجدد آمریکا بندرعباس
در ساعت ۲۱:۳۵ نقاطی در بندرعباس مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6165" target="_blank">📅 21:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6164">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6164" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6163">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
استانداری هرمزگان:  در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6163" target="_blank">📅 19:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6162">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmHs8l77QPrYHBvNAVLZWsIXxUeZW8jqNCft_oHdt1hHIxAUn52e5ZjV4Ush3zQxTF0ql0OLVW355OAqtveUoJsVDItmlglTN9pObjWpQsQT0jppUZK4zFhfh7q5s3K-DqffpjgeTKM4-r_M80Eckoyls7GibNufVxBoT_MdgF86Bin3dUh1xcdz-xTnukM0kkgc5gNn9ldHFezLRfIGhbGuQ1jxKCUE2kQxRRRRnfzSNhTab392tK1a2nsS3S6M1tDoqqOE4nqWsAU_zWVWxaGzNd7LQepEQvfdATiqZ040CcMQc9qMfHZ1soadR5jZat3IqTVCIUi9rTLAVIhj1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز :
پاکستان به ایران هشدار داده‌ که اگر به عربستان سعودی حمله کند، پاکستان آن را حمله‌ای علیه خود خواهد دانست و اعلام کرده‌: «این خط قرمز ماست.
»
پاکستان و عربستان قرارداد پیمان دفاعی مشترک دارند که بر اساس آن حمله به هر کدام ، حمله به دیگری تلقی می‌شود.
🔺
برخی اعتقاد دارند که یکی از انگیزه‌های اصلی تلاش پاکستان برای میانجی‌گری میان ج‌ا و آمریکا ، نگرانی از وقوع جنگی است که دامنه‌اش به عربستان برسد و پاکستان را ناچار به ورود به این جنگ کند.
اینک که تفاهم نامه کنار رفته، پاکستان بیش از پیش نگران این موضوع است.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6162" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6161">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
استانداری هرمزگان:
در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6161" target="_blank">📅 19:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6160">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=odTYSqMApeFPY7Ws3LYwEdDtCr4PAKpc1WF1v41-WwRQj1NXA8Mawe5r73_NVLAA-ZigfSxih1AzPsgWKZ3wV-Jer8RxRTaYiWCzoqCEE-CPfYExgiAu8607-nRwlUUMl0QjSs-Iie3V4kXOr4ZTGE6ZOJJQBXEvbN5ptDZy1o5-Nv3caKCdEPT1OZFkr4wWjao8NjA9M4raaS-SrrCqyvdHvwjMu4ulWkfw18RHTMraOIjLHqbjQLEGURy8gF2JFXjEbw6GBubCwF6_s_Mx5qZw9cmuE9ApKhe1tImAqvx_DCPwA7NXWDaQ-3lKfUo75XCR3igaax7aAZVP820Oa0jERIDVfS8DLirgxpQOxPKiVsAU-N3KhPNMumyS-U2ML4fARGqkWe0JufM85LwaJ9bDMlN53LNtCMnathftCywCWg8M-Tk1LnhozY5iy3-UB-C7go9SRsoFA6gKZpzNuhII1ag2XX5bszHCE-3CDl6MoBu2_GDaYS0g6Xj8og1y5ZI783EWs-WpU2voPIUyoeQ1EvUkdAgpdAJPLaxMB0AQ5DhKcTwjPyAClmQcEGD0OOGx7Z5ZxpPhe8mHU67n8A_RRtWVYZzh9IGBIWINkP5Kej5TsMsroIgptiImiCc0i-qCsZp6fRQKOwRyKJ3OPVj0uunl_DYNZcBUmvak-eE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=odTYSqMApeFPY7Ws3LYwEdDtCr4PAKpc1WF1v41-WwRQj1NXA8Mawe5r73_NVLAA-ZigfSxih1AzPsgWKZ3wV-Jer8RxRTaYiWCzoqCEE-CPfYExgiAu8607-nRwlUUMl0QjSs-Iie3V4kXOr4ZTGE6ZOJJQBXEvbN5ptDZy1o5-Nv3caKCdEPT1OZFkr4wWjao8NjA9M4raaS-SrrCqyvdHvwjMu4ulWkfw18RHTMraOIjLHqbjQLEGURy8gF2JFXjEbw6GBubCwF6_s_Mx5qZw9cmuE9ApKhe1tImAqvx_DCPwA7NXWDaQ-3lKfUo75XCR3igaax7aAZVP820Oa0jERIDVfS8DLirgxpQOxPKiVsAU-N3KhPNMumyS-U2ML4fARGqkWe0JufM85LwaJ9bDMlN53LNtCMnathftCywCWg8M-Tk1LnhozY5iy3-UB-C7go9SRsoFA6gKZpzNuhII1ag2XX5bszHCE-3CDl6MoBu2_GDaYS0g6Xj8og1y5ZI783EWs-WpU2voPIUyoeQ1EvUkdAgpdAJPLaxMB0AQ5DhKcTwjPyAClmQcEGD0OOGx7Z5ZxpPhe8mHU67n8A_RRtWVYZzh9IGBIWINkP5Kej5TsMsroIgptiImiCc0i-qCsZp6fRQKOwRyKJ3OPVj0uunl_DYNZcBUmvak-eE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی جدید جمهوری اسلامی</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6160" target="_blank">📅 19:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6159">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6159" target="_blank">📅 18:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6158">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ایران که ۴۷ ساله که در آتش فتنه اینها می‌سوزه</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6158" target="_blank">📅 17:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6157">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سخنگوی قرارگاه خاتم : هر چه در منطقه سالم مانده از نجابت جمهوری اسلامی است!
ذوالفقاری: «همه آنچه که بنا به نجابت ایران هنوز سالم مانده، یعنی تمامی زیرساخت‌ها در منطقه، زیر ضربات پولادین نیروهای مسلح مقتدر جمهوری اسلامی در هم کوبیده خواهد شد؛ آن‌چنان که اثری از آن‌ها بر جای نماند و گویی از ابتدا وجود نداشته‌اند.»
سخنگوی قرارگاه مرکزی خاتم‌الانبیا همچنین دخالت آمریکا در تنگه هرمز را «خط قرمز شکست‌ناپذیر» جمهوری اسلامی خواند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6157" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6156">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqaiUwzzebYRJTJdLh_4-ILXZpcYnMtOYAHN12E0BGgErvG-mSidPtnTHr0zNeHhqX03o3fEJ6SeYXLF9mNCx6B4qgVa2orBREkMiezwZx4K3KhVC6IFRzwuoEfFdhrq1CFQbCD5A4gdcu7R2WM3ISkyZQK5O79hy5z0S3qgsrSQ64uXj5GMcrb8CXH30VTf7OKSXYk4Q6-Eex36D54dlXvciEIGfhvavFpUsCZTAlAs4BPZrgIUPsMLwqZ70i-OY2Rj2D8rupRYzXEWXGEeQL3wbtbT8dbxt5RlxFz6R6IVGa0JeEOb5u1RggvneUg69AsKPkUGqXeMuiktqcokHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وراجی نکنید  بگذارید بجنگند که صلح بیارن :)  مثل صلحی که ۴۷ ساله در لبنان  ‌ و غزه آوردن!  انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6155" target="_blank">📅 12:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6154">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">وراجی نکنید
بگذارید بجنگند که صلح بیارن :)
مثل صلحی که ۴۷ ساله در لبنان
‌ و غزه آوردن!
انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6154" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6152">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=TNNPHW-d38VmrHhFwF1ADgPE9EMvuB0ydMRyDb0rvDLmMMWrkcyKUHrFwG4bmwi9ybOsb__riBDGdxX5TX7lifDZVAob_bqJtykgPX9zAcSNO_wB6IpYj4SESC00SVrnEFbP5WGa52l2WU26e_-uOem2Rlyj-0u19XXIEgWHk1Xgt1y-fGgY1EdPKql3RSGfA_wL2lkYaXGhu38ZKuu-Ty-FoyaT7679cfoAIhur10ziQC3sqkdXIJ0SmTPEGRNiGLLFc5HrYN_7FCZGLThyr1YPp_X0-pH-44xntqQCstWlRt9TS69NTPAmwLL2n3bHBMSzZIrL87rSry2TsldoO7v1hZRMSvUMND2BNdIRS8Izw5d1KUfzeVzl31Dm2-VYtjHZob64L71aIhiPAUMM1zRc67KnriAJFkEfhEpAb3EOZerBMOGqnzbASq--ia1_r9jXx3aCq9sFXO8OraKLALUqa2YzoEtQHt6E3o_d5y2cVMeha5z31nYiWRVd6_CsrTfH75skQSejlksSWcX-bD-laZAkKUt1awdtLWcRoe9D3Xi0d6m2C8J-NtU-xuRAQaHrj5U_5rpFnyZc3yUwhzE3f0-gxChHUXPBOpyB2-9kkxyNmCCfUTxWt00ohNv_9yOXo7RRol8rTbIFm2Vs5XGRVmcB2pT9iH_9v1KrV7U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=TNNPHW-d38VmrHhFwF1ADgPE9EMvuB0ydMRyDb0rvDLmMMWrkcyKUHrFwG4bmwi9ybOsb__riBDGdxX5TX7lifDZVAob_bqJtykgPX9zAcSNO_wB6IpYj4SESC00SVrnEFbP5WGa52l2WU26e_-uOem2Rlyj-0u19XXIEgWHk1Xgt1y-fGgY1EdPKql3RSGfA_wL2lkYaXGhu38ZKuu-Ty-FoyaT7679cfoAIhur10ziQC3sqkdXIJ0SmTPEGRNiGLLFc5HrYN_7FCZGLThyr1YPp_X0-pH-44xntqQCstWlRt9TS69NTPAmwLL2n3bHBMSzZIrL87rSry2TsldoO7v1hZRMSvUMND2BNdIRS8Izw5d1KUfzeVzl31Dm2-VYtjHZob64L71aIhiPAUMM1zRc67KnriAJFkEfhEpAb3EOZerBMOGqnzbASq--ia1_r9jXx3aCq9sFXO8OraKLALUqa2YzoEtQHt6E3o_d5y2cVMeha5z31nYiWRVd6_CsrTfH75skQSejlksSWcX-bD-laZAkKUt1awdtLWcRoe9D3Xi0d6m2C8J-NtU-xuRAQaHrj5U_5rpFnyZc3yUwhzE3f0-gxChHUXPBOpyB2-9kkxyNmCCfUTxWt00ohNv_9yOXo7RRol8rTbIFm2Vs5XGRVmcB2pT9iH_9v1KrV7U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگر نوحه میخونن و مداحی و رجز خوانی و.. برای کودکان غزه و لبنان و میناب و….. از تاسف از دست رفتن زندگی نیست! میخوان در این جنگ بی‌‌‌‌پایانی که با جهان دارند،  از جمله و در صدر این‌جنگها،  با خود مردم ایران جنگ دارند، سربازگیری کنند! تا نیروهاشون بزرگ‌تر…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6152" target="_blank">📅 11:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6151">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تمدن اسلامی! تا زمانی که توی مدینه و مگه بود قادر به ساخت «توالت» هم نبود!  مستراح هم نداشتن !! اما دنیا در چه وضعی بود؟  ۶۰۰ سال قبل از تولد اسلام!  توی بیشتر شهرهای جهان  داشتن توالت عمومی! اجباری بود!   اینها میشینن روی منبر  میگن «مدینه فاضله»!!  حالا…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6151" target="_blank">📅 10:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6150">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">تمدن مصر باستان رو مطالعه کنید ابتدا تا انتهاش بر مدار مرگ بود! فرعون از زمانی که سر کار می‌ا‌ومد به فکر مقدمات مرگش بود و قبرش بود!  هنر و پزشکی و علم و مهندسی مصر همه بر پایه صنعت مرگ بود!  مومیایی و اهرام و جراحی پزشکی و….. همه برای کار و کسب مرگ بود و…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6150" target="_blank">📅 10:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6149">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sH1RzYRoVHE0IDeBhwz6iDoEVDXU_NyKeSCTdXfOrSBBa3C45T3nXH9SR0qlD4t49fHkm_fN2PxmAA2UOtelzixPX1XqEb5XOMLl0QwZAkUOHNFZC6OiLW-VFYRVXYez_IhqbbKH3mmIbwGUcgAxZ9gAg4ByqTxTf_MrNj8jWQgu3MRCx6WqdO47KOlGbNvzju1G63iBrwRi_xRbF041yULlWjmUoEpxGhXzHJ_sIb9t4yfOX8eHapvvUxo8SMGL0Q6VtGKab36ZJbxGDZjCOMvsSIP-RsUxxkcSZ_7WpFkwah-cwVERJ83HlImlbp2Csn1gwJrMtAVkxTkYdPAxtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها شنیدید جملاتی با این مفهوم رو که زندگی و این حیات «زندان مومنه»!  آرزوی اینها مرگه! مرگ براشون رهایی است!  اینکه برن و برسن به بهشت و به زندگی!!  مرگ رو آرمان خودشون می‌دونن و زندگی و زیبایی‌هاش  رو پست و حقیر معرفی میکنن!  و اینکه باید دائم به فکر مرگ…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6149" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6148">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..  سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند. و از مرگ متاثر میشن!  تمام هستی اینها :  مبارزه، جنگ، کشتن،  کشته شدن و….. است!  زندگی براشون چیزی نیست جز  «مبارزه  برای عقیده».  و خوشحال میشن…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6148" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6147">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=U7UoVQiet4rvjGPRLXc6PhMQIToGaxBKQisAtHuaxThNgul8ro3rXdkOqwAs2QKBOWwssYu6XV2Hb39kxSgvzU1VZL7WJqafrvbjrrpxMWRcLjHOe4rpOLS5ytECIekmHkhsWfJTM-9G7aFxTIYbBEvilSHXDArYTWTDaI8Mmt-AJk7mUTAUQ_K-xJB7YAi5d9ciIffmr8kUfoiWzbfuEmlRH03nVGy2Usam0Cjy5D57vxGnX3RVvKgFpWo2-H33q-974i8xX1HKBeCPD1yFURIoLOdab5-42vyvTgPAoO97LvCgCue0BlNaPXitn4lLQQO8hM5pqD5mvdIeGryWcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=U7UoVQiet4rvjGPRLXc6PhMQIToGaxBKQisAtHuaxThNgul8ro3rXdkOqwAs2QKBOWwssYu6XV2Hb39kxSgvzU1VZL7WJqafrvbjrrpxMWRcLjHOe4rpOLS5ytECIekmHkhsWfJTM-9G7aFxTIYbBEvilSHXDArYTWTDaI8Mmt-AJk7mUTAUQ_K-xJB7YAi5d9ciIffmr8kUfoiWzbfuEmlRH03nVGy2Usam0Cjy5D57vxGnX3RVvKgFpWo2-H33q-974i8xX1HKBeCPD1yFURIoLOdab5-42vyvTgPAoO97LvCgCue0BlNaPXitn4lLQQO8hM5pqD5mvdIeGryWcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6147" target="_blank">📅 10:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6146">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAN2fs_UWibFgo7N6Be0NKwAfXVClMD2lS3XC1gHrV5rB8hIikxs1uFREEVuuKt88RWRi5xIXM917mTDthQ8Z3gWOZPrTZEY6ON1NkVtu2wqGA-LQpfPlVXMo4bMJCYRJfN4L8dcrNOcoIOARCqzWv9uQ8eFPDLIB9e1peGkhYvd4EfvzZJJEKJQZ6hFPPDdGZImD2-QD30GNGtdMt5NtPIKu_08vHHbZ7eDpYtuxXm2COCSAEgKi_0lAYI1ycichohmvkXfYy8rbTMD_zV1qK-86N_1CukUyy8yEoADYz904-l7E4ThPr_F0yFfRLEUVHUPgZBjvo-fD6L0tTuFSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران به یک شهروند زن آمریکایی که در دسامبر ۲۰۲۴ در دوران رئیس‌جمهوری جو بایدنِ خواب‌آلود به‌ناحق بازداشت شده بود، اجازه خروج از کشور داده است. او اکنون در سلامت کامل در خارج از ایران است. ایالات متحده آمریکا از این ژست حسن‌نیت ایران قدردانی می‌کند.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6146" target="_blank">📅 09:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6145">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6145" target="_blank">📅 09:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6144">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">استاندار مرکزی : شب گذشته به دو نظقه در اطراف شهر خنداب حمله شد.
این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقا مشخص میکند چه اهدافی را زده و نه ج‌ا می‌گوید به کجاهاش خورده.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6144" target="_blank">📅 08:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6143">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اطلاعیه  ارتش:  سامانه‌های راداری، سامانه پدافندی پاتریوت و مخازن سوخت آمریکا در پایگاه علی‌السالم کویت را هدف قرار دادیم.
‏ رادار‌های سوپر هاوک، تأسیسات و سامانه‌های پاتریوت واشنگتن در پایگاه شیخ عیسی بحرین نیز طی حملاتی، آسیب‌های جدی دید.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6143" target="_blank">📅 08:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6142">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
استاندار سمنان : به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6142" target="_blank">📅 08:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6141">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urzphoUulKT1hNfg-GMzD2o9709eWSS-5rQ_RPH9jY6aaVS9hBzKr0NNfmpCkFAKbivNsjqblSXFqN_8WRMAxalqKv9iTGE9ZmV5-lVaJ_Vf9NJ7QawtSNCys2AzR8EOWDDRqhsEt7eCCpHkcK8x5-TPHCE5armGoCIShXusaUqvg-ImrFAVV25TmkVdI8rDK28AjLWMSba6z7097XDQ7XJKKuZAJHwxTQSFpvnbcv8t2VzcIhdAqao77KAD7u-Sl5OHhnpaVAwUXHtr1NUydgR-FyRaS8S6nuNO0SAjb6iMXHuI3RhBcV2mHk625oXzn7Mymwz0e1wPVMjRX5dFgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین یارو خودش از دست سپاه و نهادهای زیر نظر خامنه‌ای  فرار کرده و به آمریکا پناه برده!
و آمریکا رو خونه امنی پیدا کرد برای زندگی و نوشتن از اینکه اسلام چقدر زیباست و خوبه و سعادت انسان رو میخواد!
حالا از همونجا به ج‌ا میگه مبارزه کن با آمریکا! مطلقا تسلیم نشید! تا انتهاش برید!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6141" target="_blank">📅 08:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6140">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">برخی گزارش‌ها از تداوم حملات به اهواز خبر می‌دهند و اینکه تاکنون ‌۹  انفجار  مهیب در شهر شنیده شده.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6140" target="_blank">📅 23:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6139">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
چندین انفجار مهیب در چابهار و بندرعباس
🚨
کویت : امروز ۲۱ پهپاد و ۴ موشک شلیک شده از سوی ج‌ا را منهدم کردیم.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6139" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6138">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای ۲ یا ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6138" target="_blank">📅 22:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6137">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LY6_-LCuYhB9Eip-vGag1q3sW3M8GqvBRo3V1Vhus0-9-4U-ldA_I08NTmNvRQxJJ9H6_onE3qDJY_cit9TFuadTZ69PHHM9u4amp4_8cxtZdYSYps28IKfiOvlTkCPxtqDop77W0tz8R-7OkSkogZhYyuEWh4aLjA2BK3DEbf4p8CsJ-rEbE0jnzgmQwVOcoeFhEQchmcEzzlU1OO8-GDcj8njN6CVkdJuqA-HnohegAJKatMPGfLP7rQ-NMCtJ3qOHER0ZQ5cYE1vbbtYmORuo9J8q6wz4yW-8eSsSl8IuGeh-L5z1H7t1nIM9fs-Lzoj2dA6cTIJWLH6zR2WlTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">آنچه شب گذشته در بمپور رخ داد و موجب  کشته شدن تعدادی ای نیروهای ارتشی شد، قابل اجتناب بود.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6136" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6135">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e615d142.mp4?token=NZ3MtWLnoELJzSqvdfbybYXe1r4KedCHK1KYD5RBBQ1pJOaj-flmxPfZTKYgoRa6-OgUEbrIV4ScoPcrsxCKVeTO2D0qXSYz-ZEmhS_p55jYATXBbfTLqyqElDKTJa2KGABPm7muKbVkpW_EO6K7MOFl8-T59jSLKqKlna7RVaLQXzd13fSuvxhc9l7pxjhyDIZot8gjojm8tOXnonGmDXbJc6UG4rT937aTVF9f6FkgdOMQf0RwHs7YxoXHVEuAbmMKaifMVU_2MQnVwSGmZfN9G0BCKmI__PsohlG13Dss8QGgeKtuJONmawpmN4t2p0-1h3TgYNvKqZritwDirg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e615d142.mp4?token=NZ3MtWLnoELJzSqvdfbybYXe1r4KedCHK1KYD5RBBQ1pJOaj-flmxPfZTKYgoRa6-OgUEbrIV4ScoPcrsxCKVeTO2D0qXSYz-ZEmhS_p55jYATXBbfTLqyqElDKTJa2KGABPm7muKbVkpW_EO6K7MOFl8-T59jSLKqKlna7RVaLQXzd13fSuvxhc9l7pxjhyDIZot8gjojm8tOXnonGmDXbJc6UG4rT937aTVF9f6FkgdOMQf0RwHs7YxoXHVEuAbmMKaifMVU_2MQnVwSGmZfN9G0BCKmI__PsohlG13Dss8QGgeKtuJONmawpmN4t2p0-1h3TgYNvKqZritwDirg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش بینی تاریخی بختیار
در دو کلمه، برای مردم ایران</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6135" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6134">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=Z2QdpA33a2iksSu-lNo6PYCWF6p9uJsxcFNqocaNJYHm_rsplKFon9iAyR-IHZuhSGBgqJddKH0f9qcWtuG5uj2huCwahnLOlEUBeiIesh3nlOVbpRUQAUhml81qTNSljVodG77Ze5YXUZVjXsF_TWeKxev76xjYiHgdxfEKC52npSk1YzPi5C_Z75ALChrZOmSgfWVe36wrynQAUOKVumb9sNG4FIqolcleTFimrcbtfzzwSgaiQNCZKv9Sbkuy_zCr6jsQXvz-RInBPAUOG10VksH4z8zPr5y55N3uueHyBShtcokDYAZO40LDjq9JagGjm9JScPTyazQ7UdNMzoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=Z2QdpA33a2iksSu-lNo6PYCWF6p9uJsxcFNqocaNJYHm_rsplKFon9iAyR-IHZuhSGBgqJddKH0f9qcWtuG5uj2huCwahnLOlEUBeiIesh3nlOVbpRUQAUhml81qTNSljVodG77Ze5YXUZVjXsF_TWeKxev76xjYiHgdxfEKC52npSk1YzPi5C_Z75ALChrZOmSgfWVe36wrynQAUOKVumb9sNG4FIqolcleTFimrcbtfzzwSgaiQNCZKv9Sbkuy_zCr6jsQXvz-RInBPAUOG10VksH4z8zPr5y55N3uueHyBShtcokDYAZO40LDjq9JagGjm9JScPTyazQ7UdNMzoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی که فرمانده سپاه بود و سالها فرماندهی جنگ رو بر عهده داشت
اینجا میگه مطئنم که مسیری که در ذهن مجتبی خامنه‌ای است، بهتر از مسیری بود که شورای عالی امنیت ملی رفت.
مجری ازش می‌پرسه خب اون چه مسیری بود؟
میگه : نمی‌دونم ! نمی‌تونم که ذهن خوانی‌ کنم!
فقط می‌دونه خوب بود :) یه مشت چاپلوس !</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6134" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6133">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5Jd86a4zRXXTPCvM2mJIYgoCcYsELcAKawjzcqLehNfPNMevhzYCXEZNK70iEIrnJy8Ivfk3uzf-cru4YrjUAzsM_NZ56bTPzt8WFpYYEsgVjykzHmdt-L63uOi-ZcifRAF9Z-niI1wsg2LPYAaJv70Cb8b9kkogAs2zPOKEVEq9y5lhzOiRAVKMI75WK_l0RvlSS4IMdJlA0t-J1h2kJqMMJDCxLulyAlbsEPtERfltsPj8xj60BmPE7ZjcEbNyxJ-cjT1gy0J5M9mK_tHABreWO0E3VVzQolTprw6tRLzMwl5GaA0tgX9VqT8aG3ZDYupLFnBskF_KvogMeDOZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
سنتکام : به تنب بزرگ حمله کردیم.
در جریان این موج ۹۰ دقیقه‌ای از حملات، با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی و محل‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را مورد حمله قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6132" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6131">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حمله امروز به چابهار</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6131" target="_blank">📅 14:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6130">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
ارتش: «آمریکا بامداد امروز با شلیک ۱۳ فروند موشک، آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور را هدف قرار داد
دشمن به مهمانسرا و اماکن نگهبانی پادگان حمله کرد
‏ ۷ تن از کارکنان پایور و وظیفه تیپ ۳۸۸ ایرانشهر شهید و تعدادی مجروح شدند.»
‏</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6130" target="_blank">📅 14:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6129">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
سنتکام : از نیم ساعت پیش موج تازه‌ای از حملات را آغاز کرده‌ایم.
(از  ساعت ۱۳:۳۰ تهران)</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6129" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6128">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_fDPbJ1XdQiWSjBEbYpL-PXdLsOsKN_gwID9PP54WcZihagt0iegY63c-0K_8niSh9FdtRHMP2VlIxiM3iH2g4ItMG3ZmpUW7fuRrq1B-2PEbGdbDZj7G0_BRoUcdr7Q73j9fQ6v4flXpqSgVl7j5Jr4LjrWNz5hp4Qkj_iBVxBg_iYA5d-Y_rbZ6WnFI-Vxn0u4Kp7jMK6gICXiRVmW7r6smjlN3QtYeQgm6beVmsiVQqG0KVppPsAOTkR_0cmMiisPu6CzC2IbR-5uIKFwFJt5MvZMXgIOEqNNsYQmr5rXWtpu18QiUgKBFax6Qn6sNPwuKq4KvkB2F0BTUJFqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابل توجه ساختاری‌های محترم
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6128" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6127">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=QM_f8yeoe0z0gSoVpzt9rMSQv68mQQIrm0OZXU9f40XmuNT7L12oZ3rcugzXYPLpJ2zJ60mWU004Jc1MCcm_lL27B8PMzIuwQSEcKc0EOLYnQAbC60Wgwj2lJnRbs6KYv6YLYt-J6EgJU3AKPmg-7-ddlmVbI3-XxPGTHbrg6MBsUw8WR30UAFbYHBT5jAONWqUuJpJcyUm1E_cI9DBmZilE7aY9fO7s4lCPFQxvvm5H9FWpSQNJ26lMdqVu-2FyNY-kxMTh_g_QFxB19IbbP5AiT3EDEf3AmXZeB8NePKIRHVfKPgMO_LegV7zx5wygjgvcRO_s_MErEU-ZOPZY_b6aQdYFm0c2H5s-wkgdTGJNMa7cY4gi5Qrfvrf2KG0Qo3P-lO9tVQHiaxv-Alk4hhytOEYC13km4WBbH5tXAozuI_ppchNI6cbZx837rPZYx6-vtVSINkzv6tRUCEJFAsnoK_qnHFsd1ZIma-8D7Uk_ZTpkjORJFjFBZi2NR3wmL3s9c_mgARE4puquT2bS7lrQNnAPCDZmyV6NyGfRHeJmcztgB5FdDKdU168YLkZK25uj-J8WiXywtYiZCXcj2gpSDX6X9BGK5Mp4XwWuP9tgx5FtReHHtXd0UkulM79mt69YcGbY7EwoBN93xnsc4YiL6V9ymwYGfiS9Wh-YocE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=QM_f8yeoe0z0gSoVpzt9rMSQv68mQQIrm0OZXU9f40XmuNT7L12oZ3rcugzXYPLpJ2zJ60mWU004Jc1MCcm_lL27B8PMzIuwQSEcKc0EOLYnQAbC60Wgwj2lJnRbs6KYv6YLYt-J6EgJU3AKPmg-7-ddlmVbI3-XxPGTHbrg6MBsUw8WR30UAFbYHBT5jAONWqUuJpJcyUm1E_cI9DBmZilE7aY9fO7s4lCPFQxvvm5H9FWpSQNJ26lMdqVu-2FyNY-kxMTh_g_QFxB19IbbP5AiT3EDEf3AmXZeB8NePKIRHVfKPgMO_LegV7zx5wygjgvcRO_s_MErEU-ZOPZY_b6aQdYFm0c2H5s-wkgdTGJNMa7cY4gi5Qrfvrf2KG0Qo3P-lO9tVQHiaxv-Alk4hhytOEYC13km4WBbH5tXAozuI_ppchNI6cbZx837rPZYx6-vtVSINkzv6tRUCEJFAsnoK_qnHFsd1ZIma-8D7Uk_ZTpkjORJFjFBZi2NR3wmL3s9c_mgARE4puquT2bS7lrQNnAPCDZmyV6NyGfRHeJmcztgB5FdDKdU168YLkZK25uj-J8WiXywtYiZCXcj2gpSDX6X9BGK5Mp4XwWuP9tgx5FtReHHtXd0UkulM79mt69YcGbY7EwoBN93xnsc4YiL6V9ymwYGfiS9Wh-YocE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سفیر اسبق جمهوری اسلامی در روسیه: مطمئن باشید اگر ترامپ را بکشیم نه تنها هیچ موشکی به سمت ما شلیک نخواهد شد، بلکه عقلای آمریکا با خوشحالی جنگ را تمام خواهند کرد.
کشتن ترامپ هیچ هزینه‌ای برای ما ندارد و با کشتن او جنگ هم تمام خواهد شد.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6127" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6126">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟  به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6126" target="_blank">📅 08:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6125">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciwbtNADqTVHy3I09vOjOGilYxV_zdqr1JeE33PyGIGGAEW14mdx4X8a9Yp66MLzPTsFlk_vq-WaaDZwsNmsft-Z6O2Z2B_KHlKRPA7xCnS3AYB050vas4u9ponHGqR5MQxiaYLkYLXn0gwBMC0fpZC5Q20CQ8m3dComFf-15GjCKWlYpI9vgPdJ1t7gQP3-Ql7U-roRDi-jRiERQYSQdaRCYc4QrZQ4V6rsSOisBr6jzyzRFf353635Uk2JPSXHSSPzdbFmdEAei6Q0PYGORJ6KmVDO0AzJjcu1-rru7X_9a92iUxr3MlBc1EuG_Ka6zCcKdka4KGw-WhJ2uur9EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟
به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت کاخ سفید برگزار کرد.
به گفته سه منبع آگاه، در ابن جلسه که ارشد‌ترین مقامات نظامی و امنیتی آمریکا در آن حضور داشتند در خصوص گسترش حملات صحبت شد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6125" target="_blank">📅 08:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6124">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=aEExiIsY1Ihv4h6-lLp_NksQyzRwuebf0RxZZeY7VF55zRnbG4ljpTAC6qZM91O5-sitamGjC1EdCo9JWgcQzsLuRgeoiE0TtAkQPWsR-htVP4qeIAwPeshtmWXRqjE7wNKt-7HLcTvsKhL0O6snqPFwuEjkWcVJQpDYwwj-LpTQJLAqQHihpDpO43_LiJUNxubcINxKiOhl7jMC4CVru1hxPAXamcXPEXDiBHfD2FbtazKyDXFJuVQWAdlFEDn-i2lH9elNlfGuSt65TPO7I-n582wNseqwtWLjJtktrI3fpkqBYVV-RIjy7mt2gPStM5oyHtJI_rXXLH4xG-EjcLBcdCNjspdE3fdssCDUQGxwXOY9c6jvn8kx7_yc0ONxGF4DRugvdCJz4fytJi3M8KZsy2UnahSAWvl25fSxvZooH-t5uAvyvXcSdjEQablQuqOOLMHz3rEjzCc8UC42QKjSmX3ffiUgsiWHjT7V7SBvtDAQyq5Afkp0WR8XKvvpij5shasTiaLoqeiqpWieH-O6HInOi1TUeB6RTHHgUDftSmMgC3E3QFhVnLNcvYF4raF3qqKQmHVroDk_OnhFSDjlKl6zVi6jGnGRN1H2yldnPuVjCZFT2qGAG2z9VL3BJfrmDmAqalmivtNf4i3Nsuz_Yerx7Y7XFsN-u7QRnRk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=aEExiIsY1Ihv4h6-lLp_NksQyzRwuebf0RxZZeY7VF55zRnbG4ljpTAC6qZM91O5-sitamGjC1EdCo9JWgcQzsLuRgeoiE0TtAkQPWsR-htVP4qeIAwPeshtmWXRqjE7wNKt-7HLcTvsKhL0O6snqPFwuEjkWcVJQpDYwwj-LpTQJLAqQHihpDpO43_LiJUNxubcINxKiOhl7jMC4CVru1hxPAXamcXPEXDiBHfD2FbtazKyDXFJuVQWAdlFEDn-i2lH9elNlfGuSt65TPO7I-n582wNseqwtWLjJtktrI3fpkqBYVV-RIjy7mt2gPStM5oyHtJI_rXXLH4xG-EjcLBcdCNjspdE3fdssCDUQGxwXOY9c6jvn8kx7_yc0ONxGF4DRugvdCJz4fytJi3M8KZsy2UnahSAWvl25fSxvZooH-t5uAvyvXcSdjEQablQuqOOLMHz3rEjzCc8UC42QKjSmX3ffiUgsiWHjT7V7SBvtDAQyq5Afkp0WR8XKvvpij5shasTiaLoqeiqpWieH-O6HInOi1TUeB6RTHHgUDftSmMgC3E3QFhVnLNcvYF4raF3qqKQmHVroDk_OnhFSDjlKl6zVi6jGnGRN1H2yldnPuVjCZFT2qGAG2z9VL3BJfrmDmAqalmivtNf4i3Nsuz_Yerx7Y7XFsN-u7QRnRk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=phqPUyDFMhBeKhaRONKdz4Vu3pcUkcu3STYWig08qDJbXP-jrJRkHZ6yRc2N6NPs-Y97hmhMvr6WX0RUzpcWCJChRkVlTc9zFijzzx_z4LiqOSwN_r94_IIgfBZLMKBsoOpPI10MhhjocNwnpmqiF3zXx-cwrRbIriuwWice5qVnLDJbF9QoDaN3Ppf_N8W54moZ8XIrdonREbLYDc5b4PORDHl283KtX7QSz9tPeYd4wmm1Y4W61mHFkGCf7ASOai9dhczUpR9Q1AAKGrfTB9u6Lqj7FxI007pzkTKdU1L3c_1D6FhWCtgGol7jBDlSLhrTzXR073jS23ZBuPQfnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=phqPUyDFMhBeKhaRONKdz4Vu3pcUkcu3STYWig08qDJbXP-jrJRkHZ6yRc2N6NPs-Y97hmhMvr6WX0RUzpcWCJChRkVlTc9zFijzzx_z4LiqOSwN_r94_IIgfBZLMKBsoOpPI10MhhjocNwnpmqiF3zXx-cwrRbIriuwWice5qVnLDJbF9QoDaN3Ppf_N8W54moZ8XIrdonREbLYDc5b4PORDHl283KtX7QSz9tPeYd4wmm1Y4W61mHFkGCf7ASOai9dhczUpR9Q1AAKGrfTB9u6Lqj7FxI007pzkTKdU1L3c_1D6FhWCtgGol7jBDlSLhrTzXR073jS23ZBuPQfnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6123" target="_blank">📅 07:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6122">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=hsc0yQkHolwWnx3M8P_VtbzNA_y3OrM-kIuD1HNMw3EvjTZ39N_I5dRg61NvLp3htkEA8oIVi4aYZ9M2JC90OV4sKyaPwoPGH9JhjLLoB2zjnXu1YBwvzElRs23o6P4iJPsj4ORaSAbFVgFWxWZQLEJaL-jYuLxBDtzw_CnBORCtcD0iKeVyjg9xcAXt6003QAMwMrgAywK-YVJxp3bQff7Xw9J0I1gQTpqoml2a2e85vrxEtUPoifjYGoUiBgtR0zmaSK0gzAv5qrZ5gLiBUBxRnbK0baAaQ7_hIEfp3TPhRDXGHkneb1lrC1aiS_pIg1eevtgtJ-GEe0fXNOc96VDMPZpTI5WirhKWQFVhX5lLgsJoi0OLpAsOj6vTSx_gGKcq_RV2YVu8xJceANTYaWa1GRfGBNtzNZ_pylBYD1JFyKeKg7L2iUKrBBr5qtt-fK9fwoEhYwvcfCseifwK4CXlrUQV1nP31q05HTmLRQey10weVPcDHBqZojvYH6ZdVowxzdk42Hm1TQb0BBGuZZK5K_g6PZmXI1MF3VcMyzpRv2H0DjMa6r8vmUKyr_dNaiPahu3EO9Atnd5RKNVC5ExhlyGDYpG6W-MMN6QnWHRrshYaWvG1VdKyJGury-BcCDk9ee8FwVExLjwoHoYqfucA3DQCor_CuRyRA8xQ_E0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=hsc0yQkHolwWnx3M8P_VtbzNA_y3OrM-kIuD1HNMw3EvjTZ39N_I5dRg61NvLp3htkEA8oIVi4aYZ9M2JC90OV4sKyaPwoPGH9JhjLLoB2zjnXu1YBwvzElRs23o6P4iJPsj4ORaSAbFVgFWxWZQLEJaL-jYuLxBDtzw_CnBORCtcD0iKeVyjg9xcAXt6003QAMwMrgAywK-YVJxp3bQff7Xw9J0I1gQTpqoml2a2e85vrxEtUPoifjYGoUiBgtR0zmaSK0gzAv5qrZ5gLiBUBxRnbK0baAaQ7_hIEfp3TPhRDXGHkneb1lrC1aiS_pIg1eevtgtJ-GEe0fXNOc96VDMPZpTI5WirhKWQFVhX5lLgsJoi0OLpAsOj6vTSx_gGKcq_RV2YVu8xJceANTYaWa1GRfGBNtzNZ_pylBYD1JFyKeKg7L2iUKrBBr5qtt-fK9fwoEhYwvcfCseifwK4CXlrUQV1nP31q05HTmLRQey10weVPcDHBqZojvYH6ZdVowxzdk42Hm1TQb0BBGuZZK5K_g6PZmXI1MF3VcMyzpRv2H0DjMa6r8vmUKyr_dNaiPahu3EO9Atnd5RKNVC5ExhlyGDYpG6W-MMN6QnWHRrshYaWvG1VdKyJGury-BcCDk9ee8FwVExLjwoHoYqfucA3DQCor_CuRyRA8xQ_E0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا میبینم راست میگه …</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6122" target="_blank">📅 07:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6121">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZ27r9uVO1OCOAyGawS6RWv9KgyEOVOBQsDFpAT6c88q5Ovjl966SUG-xjzWO2UwnbGGPKRv0CG6gNE1UUSAy-sOzqk0dxiw1hKE0eK0dgj5wEOGs-qQ5YbTl1BEw0qsiu9uZ1eC7pq2o3ugVB7gZnOqG9UkYJyoSdqjQjIjEDxS2zQJvvLiWvH9bF0SA_AsOqHQjet_jLUlImIHDMuC5se0xWqhUZcj07g8o5D8BujpELOSEnH6z57JS_Oreg2nNEtc1m8FWSfHjaNR3LIDyZkTX-f-aFk4EcXcprlUjRL-pp1iMGJUBmHRZFav0PKjYYPfUsdrsaGTRDsgvYvouQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6121" target="_blank">📅 06:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkbW4nT5U-yyEa61J5BXNkNAStE6l2TDPe3oWhEt0lOfjm0yZsqrMTs5lOxArC6yEmR6bDz-v6MvKtS0-8dhiO-Abz2p98ZX6wxJgxbQiKC7sfK3926kzj-j8iPEKWKoVZmWQyr6ucv4_rhRvkladptDuSkgQrT2opazlyXaSR91iS8oTDL8STziw2bNfsXSfkicBl6sYNGZslXAevmZ0HcaZwcVpcKVn9eMFjMG2_UbOwOiefP3xtRJkDhLe7O411ql1z0_oRoQPX5Cy4qw2qCwO2n0BLmHZoRu0i_ydsmzHdNRZHcwK6xP5cdj7MYEaxdHbFPMNTgM-zT2dhQpew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6120" target="_blank">📅 06:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6119">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=Z7q1THaquAU19a-44-_fFxBIXYGxQnbg0M9nRLp9vVMg1bDFDLKDe6vRwLQ4Yz0tsalz22CAwm01I7GeAZQGu41TCsuZ98hrYqY3GY2A2fuGVdJ1WZv3uKtIgLMy_4fnWTHtuEzNROxi-SpfRhz7NIw2dg4phyBQ70lBC5HSryvM4h0Q9G9zbJNsULJ18jXPiNvcNgBDzh-ceO_dHglwt4HsmkyGEfI5snfw_eDurN14Y9nWO5FluFkl7soLHNfALSOhPUzvjIdIX9b3eVN_ENBruuqKrE_YWGYvDhJSD9rBTaTPiHemVrfcYtKAKt2QzfKhhiolppzPStDB9p0dvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=Z7q1THaquAU19a-44-_fFxBIXYGxQnbg0M9nRLp9vVMg1bDFDLKDe6vRwLQ4Yz0tsalz22CAwm01I7GeAZQGu41TCsuZ98hrYqY3GY2A2fuGVdJ1WZv3uKtIgLMy_4fnWTHtuEzNROxi-SpfRhz7NIw2dg4phyBQ70lBC5HSryvM4h0Q9G9zbJNsULJ18jXPiNvcNgBDzh-ceO_dHglwt4HsmkyGEfI5snfw_eDurN14Y9nWO5FluFkl7soLHNfALSOhPUzvjIdIX9b3eVN_ENBruuqKrE_YWGYvDhJSD9rBTaTPiHemVrfcYtKAKt2QzfKhhiolppzPStDB9p0dvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام فیلمی از حملات خود به ایران منتشر کرد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6119" target="_blank">📅 06:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6118">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=ve68vWxBvsxg-hYaS3fVMQAt89XI8e14NhFcnrAlWT1a1WS_odXed4ZfKygdoP9FUGbUQBUXLaZuHSBIX_5IjWYT96rZGvV4k385N-8JIsCdRDiyf2G9_wvWFsmCdFa-80UhkXhpQboDCD3hYcHXKy1ESad2N0_A0nLPkTGgVPX1ifugEYhBHb59XT-CaREPzvetp_gRL7Uq2zIxdEyGnzvnu-FizpVQADtVfm1yf5K_leY7boyi9f5YaA_jgyVHALmhJrfdRThBSlUFdSWCtQpz25tUgSfZRm1I7PpD1o-1A_RuS4Fs6ARVWXcSziQ8AvVoo2XStJl6uEtZ_HHjlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=ve68vWxBvsxg-hYaS3fVMQAt89XI8e14NhFcnrAlWT1a1WS_odXed4ZfKygdoP9FUGbUQBUXLaZuHSBIX_5IjWYT96rZGvV4k385N-8JIsCdRDiyf2G9_wvWFsmCdFa-80UhkXhpQboDCD3hYcHXKy1ESad2N0_A0nLPkTGgVPX1ifugEYhBHb59XT-CaREPzvetp_gRL7Uq2zIxdEyGnzvnu-FizpVQADtVfm1yf5K_leY7boyi9f5YaA_jgyVHALmhJrfdRThBSlUFdSWCtQpz25tUgSfZRm1I7PpD1o-1A_RuS4Fs6ARVWXcSziQ8AvVoo2XStJl6uEtZ_HHjlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : امشب، فردا و فرداشب به سختی به آنها ضربه خواهیم زد و هفته آینده پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد، مگر آنکه  مذاکره کنند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6118" target="_blank">📅 06:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6117">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caeb092620.mp4?token=Ea97lGtO9Wwty9nDxhLl3jpFxtyd1o7kY8nenXCUnwEmhQ1LNU7r3uwv1uRA-ka1BG8DOxEsceOJtfJH4rNcHcwjQUnS73VhrLsADWlMQVJIA8Jssyv7jhb75atBMNsJ1YJbcdQyajOOiSUu_T4-w9ZMywUTSOO2--hlYaFWFxN5UiGkZ37ET45IYorIqe55xJ7fjG1YMgOJUwvXs18PMG355eKcwzDlJUQrPSn5AKDAC9ZpvVI6vwLlJ5-hz0ix03ooYalaEWskf7E2md8V0E7F5_NMOgUQGvxquMn4AOVqhqRuge1qRf53J1okG6OfCAk5T0EcAwgS0pjNPnNxOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caeb092620.mp4?token=Ea97lGtO9Wwty9nDxhLl3jpFxtyd1o7kY8nenXCUnwEmhQ1LNU7r3uwv1uRA-ka1BG8DOxEsceOJtfJH4rNcHcwjQUnS73VhrLsADWlMQVJIA8Jssyv7jhb75atBMNsJ1YJbcdQyajOOiSUu_T4-w9ZMywUTSOO2--hlYaFWFxN5UiGkZ37ET45IYorIqe55xJ7fjG1YMgOJUwvXs18PMG355eKcwzDlJUQrPSn5AKDAC9ZpvVI6vwLlJ5-hz0ix03ooYalaEWskf7E2md8V0E7F5_NMOgUQGvxquMn4AOVqhqRuge1qRf53J1okG6OfCAk5T0EcAwgS0pjNPnNxOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ناشی از حمله پهپادی امشب سپاه به کویت
گفته می‌شود مخازن سوخت ارتش آمریکاست.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6117" target="_blank">📅 06:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6116">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360d24e506.mp4?token=ZdeRaTJyX3TQRDExREbRyo8ScpDRt8xKZxd94zx6swJwzBfr2ufQnV1VS9jxuAHLKcNg7eyqj8JysabPHrtqw7NdjBjar0iJP4TQXTjLhIYYYu8H_R0dLSAsOXGwGtYGGF1TlYvEF_oxHuiMcj7Fqbpau5eEiJ9hTallOYQMuyAZy-E0R0kfb4lmTQOxQdNEq0XAlciDYQq0-UYKt_lYUG4sDeRrwxy9ntppdI6tyicT4512Uo7ggaWIiac3bmPJ7mAIAE7fta6VHUgGRAFQzfpm_cqz0VajSe34BALo-4YYsWEhdoPnv97Pq2YCdelQRttOM0OaK1Yd65-GpMPoeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360d24e506.mp4?token=ZdeRaTJyX3TQRDExREbRyo8ScpDRt8xKZxd94zx6swJwzBfr2ufQnV1VS9jxuAHLKcNg7eyqj8JysabPHrtqw7NdjBjar0iJP4TQXTjLhIYYYu8H_R0dLSAsOXGwGtYGGF1TlYvEF_oxHuiMcj7Fqbpau5eEiJ9hTallOYQMuyAZy-E0R0kfb4lmTQOxQdNEq0XAlciDYQq0-UYKt_lYUG4sDeRrwxy9ntppdI6tyicT4512Uo7ggaWIiac3bmPJ7mAIAE7fta6VHUgGRAFQzfpm_cqz0VajSe34BALo-4YYsWEhdoPnv97Pq2YCdelQRttOM0OaK1Yd65-GpMPoeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی با موشک‌های حاوی بمب‌های خوشه‌ای به بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6116" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6115">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
ارتش : به پایگاه‌ها اف ۱۸ های آمریکا در اردن حمله پهپادی انجام دادیم.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6115" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6114">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‏امشب اتفاق جالبی افتاده، به محض اینکه خبر انفجاری در شهر و استانی منتشر میشه، مسئولان جمهوری اسلامی سریعا مصاحبه میکنن و میگن دروغه و همه چی آرومه!
‏اینطوری مثلا میخوان صورت مسئله رو پاک کنن.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6114" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6113">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1BdQb1XAFOxnXs7o5FVGMbJl1eyXHRUszdJ35tXJpDZNdqnZW3AdQFUsm6GscHyG3Ch4WyvXIsFTkn2gzGY0mFvnBSiyyRTTMxVJFRVC-qsVX6Qsxajp3cMBf6mKmKIoq4NOI6r9gnSB6jk6eAiIySSfQTpMMcVNlOgfAyHO3mZrEuJZgjGVFV9bG5zMX0GGZY6yY_P3kC4rFhbwx6d-tXyQlipfTTUR3LtjRPWqy12DKNusyWjCJEjCW26vLobb2D0vntSVdPkWTELI9DPNAvoQcajF7tcqrTQ5W4zbrvv2V3_Vbu-Nf3XQ0lDIU8EbN2Yx5eaGppBgj6DZPx41g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگارهاشون می‌نوشتن که کشتی‌ها دارند  از مسیر عمان رد می‌شوند، تشییع جنازه،  بریم و کاری کنیم که  کشتی‌ها مجبور بشن از آبهای ایران رد بشن  و شروع کردن به حملات به کشتی‌هایی که از مسیر آب‌های عمان میرن.  به زور حمله میگن کشتی‌ها باید از مسیر ما رد بشه.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6113" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6112">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhOXyLlj9BFcEtyWOj2VbK94Su3k0RiuJ28CnCjMLNJMVRIx7Fk3681GedJyo22X35X8m6bhq6OPWhVrm_o5LqIPMEIMOEw6WsjX7IJgBzRf2uML3LmEGkBejTFOQKfxci6KyCRCBxdq0FeGfu8QuGkWZT-xPEAHwPsUdBRbXZw6WggpCmhgTfp3FfklvhvgYltDNjiuRHOHQhR1hrdBH_G6Ju3TWgy0FHvvqV6DaTrpAtMUkYsIEMv2Kn1-9bps2Ufojo9pGVyTp8c_KFXdYACF0PbpJ4DjCyAgnxQ3SP8SXZXJhCRvRRUdZWUj1DuAjrd511Pdl48qI1wGbs6_Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا در حاشیه خاکسپاری جسد خامنه‌ای و جلوی قالیباف شعار میدادن «مذاکره با دشمن خیانت است»  هنوز به سه کشتی حمله نکرده بودن و نزده بودن زیر تفاهم نامه</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6112" target="_blank">📅 00:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6111">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=B8y4kZepVuBeu3wk5g2tw_fViNnyYBGELRAYw51focOWTrIqKkZ91nuDhCi_LN30zIXFuH9ouvzncx3RpVJ8AwyUXR5d77dmwYaL3AaLXMJGGnWkRKhuxw5yres8BESx13-NH7RIV6lSsdDK7nmdubpdPBc1GHlYWJrckuTDorXSKqNhgPYtA5NDKs0Boj4IwWdkklcFtv6gMyS9sRi8OIFBbsmBeSi_VLrIFdcS3C53UPVtzKU4KLMJH0PTJzlvk0qdHd2cEC7zD3DgYZZEem4nTBdgoeQ_5hehdTvyRdGsoOBmiMise-dPdcdP9h_QKUmFOi3n0thO4ewXs7PFYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=B8y4kZepVuBeu3wk5g2tw_fViNnyYBGELRAYw51focOWTrIqKkZ91nuDhCi_LN30zIXFuH9ouvzncx3RpVJ8AwyUXR5d77dmwYaL3AaLXMJGGnWkRKhuxw5yres8BESx13-NH7RIV6lSsdDK7nmdubpdPBc1GHlYWJrckuTDorXSKqNhgPYtA5NDKs0Boj4IwWdkklcFtv6gMyS9sRi8OIFBbsmBeSi_VLrIFdcS3C53UPVtzKU4KLMJH0PTJzlvk0qdHd2cEC7zD3DgYZZEem4nTBdgoeQ_5hehdTvyRdGsoOBmiMise-dPdcdP9h_QKUmFOi3n0thO4ewXs7PFYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این استوری رو ۶ روز پیش گذاشته بودم  میگفتن آمریکا میخواد آتش بس حفظ بشه ولی جمهوری اسلامی باید «کار دیگر» بکنه!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6111" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6110">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550f13e765.mp4?token=UISsziklVbuOgYNirkJqWr4F1Ktrm-8a0b18vynVhUzGuP6W4abLOFLUCvHDF0RCkgXw7hXRYzH48XcBQHGV8NOBCj9NZozDDdnFjldDhfIna-dJljyAD3QfWQuv-p0zp_f10wXMXXkimc7Dm-y5i8rtIFza_9TJfHvaBmQmEDY1xXyv-NlRPBMsuab_pUSQiH_dlqlXWCbMZbWctqIQdhAuPv_2zTU2xO_yvJgthHvbYJA0ubtKURcmWuoGh0IEM0s9lDBNDrYOAO3Z41Oo80_4ZePMWx0Az5lXgOUOKzUOnPxinR6BAsxBG32IEKeWkyeyXXqKuRwA6qBndOUHoyBBcoKy7X4eeWXRnXaZ4hgPhljykgGRzqrz35CjfgIL36Pt-Rai-yxdJTIRLnJHaIcqtDQZg_xK5tWuQQ4p61qCnb7SH6Dky8tFHnzvBHmM1qMOOHnNsLSVmupEpUbuVf2tQQ_g4wfM8yJNug9ZJtQim_0bEZJjzz9qU2gjb4j3wjoWONaikmtDmlsiY7IBuppfOVfQEKJji6fRsorBWe1YiRCufuzVFDY2OFwqGrb_zkgVu04cGX8gADf2iteO-qLwvrdn25NQDJ9SUjesf1h27mAzt8gC2i28XaonUPIymOCJ-QDNNRuZA208Q1ntCbvCMG1ckR4Lkdbi6Qqfbek" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550f13e765.mp4?token=UISsziklVbuOgYNirkJqWr4F1Ktrm-8a0b18vynVhUzGuP6W4abLOFLUCvHDF0RCkgXw7hXRYzH48XcBQHGV8NOBCj9NZozDDdnFjldDhfIna-dJljyAD3QfWQuv-p0zp_f10wXMXXkimc7Dm-y5i8rtIFza_9TJfHvaBmQmEDY1xXyv-NlRPBMsuab_pUSQiH_dlqlXWCbMZbWctqIQdhAuPv_2zTU2xO_yvJgthHvbYJA0ubtKURcmWuoGh0IEM0s9lDBNDrYOAO3Z41Oo80_4ZePMWx0Az5lXgOUOKzUOnPxinR6BAsxBG32IEKeWkyeyXXqKuRwA6qBndOUHoyBBcoKy7X4eeWXRnXaZ4hgPhljykgGRzqrz35CjfgIL36Pt-Rai-yxdJTIRLnJHaIcqtDQZg_xK5tWuQQ4p61qCnb7SH6Dky8tFHnzvBHmM1qMOOHnNsLSVmupEpUbuVf2tQQ_g4wfM8yJNug9ZJtQim_0bEZJjzz9qU2gjb4j3wjoWONaikmtDmlsiY7IBuppfOVfQEKJji6fRsorBWe1YiRCufuzVFDY2OFwqGrb_zkgVu04cGX8gADf2iteO-qLwvrdn25NQDJ9SUjesf1h27mAzt8gC2i28XaonUPIymOCJ-QDNNRuZA208Q1ntCbvCMG1ckR4Lkdbi6Qqfbek" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو رو دو هفته پیش گذاشته بودم.  معاون سیاسی نیروی دریایی سپاه اینجا در جمع حامیان حکومت بهشون میگه خیالتون راحت باشه، حملاتی که ‌ آمریکا انجام  میده «واکنش»  به اقدامات ماست!  «کنش» نیست!   تمام این ۴۷ سال همین بوده!  یه کاری میکنن ، تنش راه بیفته،…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6110" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6109">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6109" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6108">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=CXafpaFdmApbd3IOXauUeeald8PHWuOW-sSQ3jBeBXHTZe1sb2EC_U566ED8T5QzdsJSuaoqNnj_ZWXmg_aGBcQmC736sk5cvEMf6lYXOyTpWQ_sjFWjZQUfGqD84tGxLCmIJzHuBgyA1ZFy15Sc2hPlXYXjXt8LW7C9ZMUaWfxD56dtrQMk_8hPdK_JjA0guduUohWl2ZNk2kA_tqAYbN-OGTBfgISao57N2t_LdUKbOxGG2HbOc-h1BeeOD0I_ZYed1BHDzDRsXb2Lwvj-Fhhs8bhdY9A6eQlYWfgfnmzzmeyXjuQM_Xj7Wwp_q6ZKoVbtEsvbSihfSEpgYuazKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=CXafpaFdmApbd3IOXauUeeald8PHWuOW-sSQ3jBeBXHTZe1sb2EC_U566ED8T5QzdsJSuaoqNnj_ZWXmg_aGBcQmC736sk5cvEMf6lYXOyTpWQ_sjFWjZQUfGqD84tGxLCmIJzHuBgyA1ZFy15Sc2hPlXYXjXt8LW7C9ZMUaWfxD56dtrQMk_8hPdK_JjA0guduUohWl2ZNk2kA_tqAYbN-OGTBfgISao57N2t_LdUKbOxGG2HbOc-h1BeeOD0I_ZYed1BHDzDRsXb2Lwvj-Fhhs8bhdY9A6eQlYWfgfnmzzmeyXjuQM_Xj7Wwp_q6ZKoVbtEsvbSihfSEpgYuazKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گشت زنی اف ۱۸ آمریکایی بر فراز چابهار</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6108" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6107">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا : محاصره دریایی ایران وارد فاز اجرایی شد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6107" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6106">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
چندین انفجار در بندرعباس
🔺
چندین انفجار در اهواز
🔺
پنج انفجار در قشم</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6106" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6105">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOpWAsXCEQ-bY_MuA9_LDNdJ_MwlBWBzsSZAkUEBviTEBhKMYRTZV8jeP-h4XVyA9zAIL69ovtOtYO4gbUX4nwM6yP0sCleKHLSGurXCaW2LRaH-_WororobpFZXkYeVYu2aqHnu-x7weIafr2smaj99DEiERsX9GWkHwnfwaccV0MLvCxgd5FyfQPhueANKDVKJfpcwG09Y-MLsRhogNtFOw8WX5wSCgSiYyo6LOisVzzo2CbAK59HqtNEkOCtTWfw8WU82s0KH_-PNeA8gO8LOLaWfk-mMw-UJu49vQkQqpHjUeLGp2Zzbchqez-ZaR7amVav99CNvu0tKbgtoHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2077085449948938568?s=46</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6105" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6104">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
دقایقی پیش : حمله به قشم و شنیده شدن چندین انفجار
🔺
حمله به یک نفتکش اماراتی در سواحل عمان
🔺
فعال شدن پدافند در کویت</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6104" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6103">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6103" target="_blank">📅 18:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6102">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnfpI9cVSjZzQUeN6LNRUJoWY7qELDNQlkk1D6DLXWLHviUxAq6CH755hVIV2MQ8uv015FoaCg3tQdOr1KrNHJ3_8tcr6pje4MHfgTA8C0p0NCz4VxvZHtGjcgN2RI8tzld5DQfcVPbnHM2-jgD8U0GqkmEdCvWQ9BDoQrthgOPjJpXR4IvAOk1MF35w7H_l04fC4kyMWuJvwD0YU-_rEXBsZFPjn8X4xg3dSbknboaEnUe77mHuTECK6_F6CyWPWiK1v9Fm0uIbqug8GUSeKB3s3lGizMlpCj1tZDYk9Nr9_oifdk78ej2EK7OjOQXnczwSZNhpP12ND64rJrz4kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهپاد‌ها (قایق‌های تندرو بدون سرنشین) آمریکایی این مدلی به یکی از مهم‌ترین مراکز نیروی دریایی در بندرعباس نفوذ کردن و حمله کردن.  گفته می‌شود که در این حمله یک زیردریایی ج‌ا را نیز منهدم کردند.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6102" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=ZBXcN-Gls5oDWIWdO6hUf0G1KBYcscZVQT8rdWqLvxmcPFi4QibfIxzf8Vg_KFV_sekAeMg8KUD2Sh0BmL-hUdfz0LFKdLkZoUaNN7Wo6zjANVM9YV6jh6as1n3H38HkJpW4BI88OQ6uj9rqG2NyaLMVTmLpdxkm4TbU3Jkp2fdU794H6wZQY3JmrgJtBpKEuhmeITA9kXyKsLqoN7nNPV5sNxXisxPyHA21JUf2APTobEmnLkOahw4ITG7PhGOmf2OMBvaavfleCY727SNC7dvSTBVVcUzZN4zZhXnMoRc2iacwSMm2iPFeG8UsMIamgPR2_0pT49fpC2vUbTaj1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=ZBXcN-Gls5oDWIWdO6hUf0G1KBYcscZVQT8rdWqLvxmcPFi4QibfIxzf8Vg_KFV_sekAeMg8KUD2Sh0BmL-hUdfz0LFKdLkZoUaNN7Wo6zjANVM9YV6jh6as1n3H38HkJpW4BI88OQ6uj9rqG2NyaLMVTmLpdxkm4TbU3Jkp2fdU794H6wZQY3JmrgJtBpKEuhmeITA9kXyKsLqoN7nNPV5sNxXisxPyHA21JUf2APTobEmnLkOahw4ITG7PhGOmf2OMBvaavfleCY727SNC7dvSTBVVcUzZN4zZhXnMoRc2iacwSMm2iPFeG8UsMIamgPR2_0pT49fpC2vUbTaj1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جنگشون :)</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6101" target="_blank">📅 16:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4v3GRQzqieinQ8MEgrUXuariKIdhgTFZpDGgnPaJ2Dg-DP1ZcdfU7lAn-YohJ6USjQU4aBNNUV9J4JXr3t_gtO7N3ViuTFcTf1lG0x2AO9-9RiCBd7rABWa7e5bw3yG2jhPV1QrilFi9fU8q7nXeo7ssagR8MQRkGcjU1f2HEpOjpxec-GK-AWCehaEe9z_0nxlD06okNUbmq8BvnpJ2N2j_uA28mDNRPVgOc84OvroXh5XigpeqJobFR1g82YqN2En7ZhprxibkPgsW6aPB1_zqXBYKG1lly3F_znndigLTYLqh-Ayt_IK1S_N7CnwmTGXlfxN4b-dvNxo9YGb7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.  این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6100" target="_blank">📅 16:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6099">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">۴۷ سال رژیم اسلامی</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6099" target="_blank">📅 15:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6098">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYG1m-VTXwsbkcI5FqNUOTr7FTWcaMocTCwrfc42PZjQiXNO7QUbgTC0zedIK9p7oEZ3W2I1YVDo26lYWxG31TP7npAMadTJA41u3UArl-X7GsgkXzovhJlEnjFZekljDNt5sEtokdBRmXdQ31WFOu2Q0WXq8VKkfaCTvmGB1uHQk5F4MAAtZvFP-YQ4Ng6Y-ARQxZp351H8Fj700mWteJhG_jt5RqSP62jtHbgwDkX8Of5OCBp_fjpYMgxZq3ipDZo-lomc298NiqUHlWJTNVjnI6MLPqB_yX3Y0GmDexdP0xb59aRMPgNlWroOX5qdi_M0sNgUvi-Bt8iKvKh_GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
تخریب ساختمان مرکز آماد و پشتیبانی دریابانی نیروی انتظامی ⁧ بوشهر ⁩ در پی حملات هوایی ⁧ آمریکا ⁩ به مراکز نظامی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6098" target="_blank">📅 15:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6097">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=Mnk9Bdo5yB4FHk2l4Gh3TKBcXWjJilq1s3F7TnaR7mLktoWXUt_cl-_9HPtsP6SvCqHag9OTflEhEj9LhmUH-8EbboWpxDPGQAtt3nofWBr06pMFvSvqsXEg9TdYW4R9_pV_m7PR1BPISonhFjhr_i-XVjXV54xvjYL02LMblfvOjIlWeCflnfDkX5w6mzwyF6KFMBrwMcxDlXJdRgBIEtDI8Esng4muO2Eyvm7VjTCHrZbkMuQ6PkJB98Yu3e6TimKuIr2dDXiQ1mlCG3rku4akECnrWf4EzL9WBUzQz4Oi8PxQ9prGFeR9IUnttCAT8LBX3UXdpa6ATeh1HDYWEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=Mnk9Bdo5yB4FHk2l4Gh3TKBcXWjJilq1s3F7TnaR7mLktoWXUt_cl-_9HPtsP6SvCqHag9OTflEhEj9LhmUH-8EbboWpxDPGQAtt3nofWBr06pMFvSvqsXEg9TdYW4R9_pV_m7PR1BPISonhFjhr_i-XVjXV54xvjYL02LMblfvOjIlWeCflnfDkX5w6mzwyF6KFMBrwMcxDlXJdRgBIEtDI8Esng4muO2Eyvm7VjTCHrZbkMuQ6PkJB98Yu3e6TimKuIr2dDXiQ1mlCG3rku4akECnrWf4EzL9WBUzQz4Oi8PxQ9prGFeR9IUnttCAT8LBX3UXdpa6ATeh1HDYWEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌پرسه نظرتون درباره اینکه بدون هشدار قبلی برق رو قطع میکنن چیه؟
‏چمران میگه:
‏شما اگر بدونید پریروز چند نقطه برقی رو زدند دیگه این سؤالو نمی‌کردید.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6096" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6095">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jeo6y7oVeufjVOUAkByv6Gr_c4YqnmLN76wtKsfXAl45o7Eo5RlSxJfjZC95D8blBdEDURyxWbDl_KGL92eH3C0JuknrjNVkcfq7FzyX6F_tS380mzBNoYX0e1FhdMCUeLH-dZ7XVduaacVCqT8XUEPHmCb00WnifBeIeON5cDaG7eGTB4MRtVPuWrUXqOXFEbdf5FYce5Kf1pPJKB1icZASBx3YcgwJiYSqo-zFGMauKh12f8tillo5j2iCizu_FETcobm5EQscsp0sV40nOQOO1e1zapoWQEM67pP2rTibbFnXs6yXtuR5fImbRpHfJnYIA85jHuXZEZFFV4dHWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ترکیه، دیروز جمهوری اسلامی
رو با اسرائیل مقایسه کرد و گفت
رفتار این دو شبیه هم هستند.
(کاری ندارم که ترکیه خودش چه افتضاحیه، اما نشون از تغییر رویکرد ترکیه نسبت به ج‌ا داره)
یادمون باشه فرمان حمله اخیر از سوی ترامپ در ترکیه صادر شد! یادمون باشه معاملاتی بین ترکیه و آمریکا رخ داد، که آرزوی ۲۰ ساله دولت ترکیه بود.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6095" target="_blank">📅 14:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6094">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.  در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!  مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی)…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6094" target="_blank">📅 13:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6093">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPFo2gKz-U6g1w-bNVnHU2JOB0qbzIwHXaIxiXSTpL0hYVs_pqhmtr6j7Btihk-WNt1ozrZLfxSDIGSq4yMf29aUiyafhimN8M8smLZnsuOhp1u8ceye-TlDmJ8gKZfqtMv7x0wWaKOJzAlYaLd2ayif-duzVAz12WX2RDBp2KCPMbYD8oi1P9COPV6T8kLbm_ahO2LF8oIKufJfj4uf3qXH_sBZief9qqrj9WZERvGOK8OiF6z9QV8JgsFJKIBN-gyRPxk8ZHom2HURnzy87NVh2YN7faeDwWqNQjWKC9yriA1dr-ejYk8tk1YEh22AqGW1F3Md8PlomGc3KTIs4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.
در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!
مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی) نیز در این حملات مشارکت دارند.
🔺
دفعه قبل هم که امارات در پاسخ به هفته‌ها حملات جمهوری اسلامی به جنوب ایران حمله کرد، مقامات ج‌ا تا چندین روز نگفتند که کار امارات بود.
الان هم برخی از این حملات مثلا دیشب، با حملات دقایقی پیش مشخص نیست کار کیه.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6093" target="_blank">📅 13:50 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
