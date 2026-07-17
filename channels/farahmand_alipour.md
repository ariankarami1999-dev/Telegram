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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 22:01:32</div>
<hr>

<div class="tg-post" id="msg-6190">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:  ترامپ به ما نامه‌ای داده و صراحتاً نوشته است: «بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farahmand_alipour/6190" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6189">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farahmand_alipour/6189" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvDYAVxq_VcbEn0jaAtD5W0oDdCv3M8dmdxBphtzQ5ZwVVirnEuae7sQDY784gBK6BpZHGygBOPw0ePCzEjP8oa-y21b_C8vFWf_neLyAqf_Wbd7azZZUTfH89ug8shTlr8FOJfiyueNVS0BNi_E9sxOtFj-Zr9WdrRH6t2Mx6NALQBEyBifA83N9-w67rDqsQ-p0ZkWtPrVIBSdzYdbAZQSA8jNCx7-m0U0c5ubeMLRs6Ek-tOMEEqhg4k1z2U1vhP8aJsrJfW_zhBQbml2fRWDupFkGydVYyYxuDsrZrSNuy8hEr_6_uBv2KdiOOzC0chxlBOYOHNbuxHcbjYmzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ایستگاه مترو در تهران با مجسمه مریم و عیسی درست کردن (که عجیب هم نیست،
نصف قرآن داستان‌های مریم و عیسی
و قوم یهوده) و پروپاگاندایی راه انداختن
که ما چقدر احترام میگذاریم به بقیه مذاهب.
بعد همزمان کلیساها رو مصادره میکنن
و صدها نفر به جرم مسیحی بودن
توی زندانهای ج‌ا هستن و اجازه داشتن
یک مسجد به سنی‌ها رو هم نمیدن!</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6188" target="_blank">📅 18:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6187">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o23JcAiz3J-Icg3U2M2NzvMMdb40oPmFoaBYdlEUwYBjyhuN5b7h2IyB8XgQrGu_Dq7InpDe7TcU2ZambOI_wXSGPPLisXRqSm0xPvHzpWORotmFzWGypHPDRcs28w5fgyeAPgPX9tmcEit4U8j9ZNBkqD25XpgTKaBzyczAQNroCMUmhkA_u6H04mdQtYeTzyX2ghvNenOWyuC42uvE645ZfSEQuwM6bftXXPSROfKTqucxUJy8Aa9k8LJWwmH-QDEjrouQMl89LJ258sbqW6S1tVKp-PMIp46gh9b6vqZvF-z-Z8kH5YlZDHes4FG4ujPhCMiuflxA-C9mAuAtDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب طلاقش بده :)
چرا اینهمه کینه؟</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6187" target="_blank">📅 18:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pj5r17LvhYKZPKH_z4Yr62thpiFHiUk8LiH26S0LqfbzRr4anLt-I4ZlHGmLLLokjaV7l3yCbMbH_sSwpzpoZRl_bN13-AuNvNRSDhRXn_0pWfAMFXI4j00iMQrdXOrrZlNW__UkxJ6YAYYDdIKuzjK2jXSON60UJVXKLGpSiLQs7ewG1M34omN483pt1bgKdxYdtLJ4MBnsrZGMgPCBlKZyeS0uSstBfzav_2qmMuBExOvZT22uS2fGMWylDiqDPF-rg6O1gBmACv9_Vtg-0tRr1_lFJMPu0svI6UoBFTlaJtH_Ay8aPYXXW4r5GwjOUXuhxMzY67FHpPB16lEb8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل عرزشی !
من میگم اینها شکست‌های تاریخ
رو پیدا میکنن و به عنوان الگوی خودشون معرفی می‌کنید باور نمیکنید :)
تنگه احد! که نماد بزرگ‌ترین شکست و عقب نشینی مسلمانان در تاریخ صدر اسلامه،
رو شباهت سازی میکنن با تنگه هرمز
‌‌میگن همونطور که اونو در سیطره داشتیم
اینو در سیطره خواهیم داشت.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6186" target="_blank">📅 17:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6185">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6185" target="_blank">📅 15:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ijt5NRK3bltsYCoHkEWDkhrcfi5qZ--8GXUF5P3-8IK0TPqriYcGaj_rju2tJ7vUgwYsS5u9HmUMtsvwofBpwQIY_G8VauO1lhDEPE79BAXOnZcWgApkjZp8GP76Nxi2zQQ9wVFiPyWCkbhC-9yvd0w_1ZnHvvy65JIPelk236nzSTkWZJOOo82ttchl91wf8Wqd9mCD7pIa5mPzdbLXD1iNMUNym65cPe24AyUPfo20PC1xb_MnWNYdf5MmiJ0HfjfWiWjCciXf3-nfQwoVq71WQBin3R_7y7TWbh_DZcycgfxnLxzhmpI6d4g18W17wla0suaespRUpAdDgjiyJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی به تاسیسات آب‌شیرین  و تولید برق کویت حمله کرده.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6184" target="_blank">📅 14:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6183">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=JYCCchxyPd6A7ilQkz80EaXyVs2eEsT0foYs0LNA-hNCrlVX8uDIyd-GqnSj5S2pA-NoJCWDs722GN6rh_Ulp8FaQ0otBJuAQbmpJQ708RODUIsw74MXBXvtq7PL43Lw1-UcXriz7sjhxUJ_-S4b-ut0y0jgQ6bDNuTeQqHPL1cMhNAvReGvM30SDFNiUAhxndwwJO1AJzo07_DC2-7eu59ijUkCzJoG_7SBCDpUqnnqNyZzxS9d3tfNka8FoWGidqeZPqX2Fe-VYDqyVPpf4atEFBFm_dWFHWLR04c2eYcB5XOY4r0ClYFla4O8NDsMZLeR8uv-naHUfuY0s1njVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=JYCCchxyPd6A7ilQkz80EaXyVs2eEsT0foYs0LNA-hNCrlVX8uDIyd-GqnSj5S2pA-NoJCWDs722GN6rh_Ulp8FaQ0otBJuAQbmpJQ708RODUIsw74MXBXvtq7PL43Lw1-UcXriz7sjhxUJ_-S4b-ut0y0jgQ6bDNuTeQqHPL1cMhNAvReGvM30SDFNiUAhxndwwJO1AJzo07_DC2-7eu59ijUkCzJoG_7SBCDpUqnnqNyZzxS9d3tfNka8FoWGidqeZPqX2Fe-VYDqyVPpf4atEFBFm_dWFHWLR04c2eYcB5XOY4r0ClYFla4O8NDsMZLeR8uv-naHUfuY0s1njVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!  ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟  به خاطرش حتی موشک به اسرائیل نزدید؟  (که اونهم اومد در پاسخ ماهشهر رو زد؟)  خب جنگیدید و شکست خوردید!!! هم در لبنان،  هم ‌در سوریه…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6183" target="_blank">📅 14:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6182">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6182" target="_blank">📅 14:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6181">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6181" target="_blank">📅 13:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6180">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6180" target="_blank">📅 11:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6179">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6179" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6178">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=gQaoAYWVaDThIrFT6v0SMdZMNkx4TA3jclUzJzT9SgLoVyYvzuBAs6Gqhy-_N1k277GGoVX_IbMcnKXIi2CDlrcALulHj5YDfNCoc5xEiJmSd-oCVl67n9jjSyZmYi0GvVBmGcUzDtZOUCBay9OlrZL-K82Y7uepqgS64LBzJHQ9T2STfxdAwJyXZOvWXqob52USmf2qIcnLulhQS5Nx2tPylu74o9IGWjepVmiuJHO9Dm0DqB6uePJagxSEdy8Tpqe3kmyGHlbVpYfzZvIFNgyCM44qLm0sepNM26eUD5tGSKyO_EX3uoUX02PkJRi-qDv_EmDegjDMFWulTVmJPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=gQaoAYWVaDThIrFT6v0SMdZMNkx4TA3jclUzJzT9SgLoVyYvzuBAs6Gqhy-_N1k277GGoVX_IbMcnKXIi2CDlrcALulHj5YDfNCoc5xEiJmSd-oCVl67n9jjSyZmYi0GvVBmGcUzDtZOUCBay9OlrZL-K82Y7uepqgS64LBzJHQ9T2STfxdAwJyXZOvWXqob52USmf2qIcnLulhQS5Nx2tPylu74o9IGWjepVmiuJHO9Dm0DqB6uePJagxSEdy8Tpqe3kmyGHlbVpYfzZvIFNgyCM44qLm0sepNM26eUD5tGSKyO_EX3uoUX02PkJRi-qDv_EmDegjDMFWulTVmJPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی از سخنان سردار نقدی : اگه حتی به آمریکا حمله کنیم، قدرت پاسخ‌گویی هم ندارند!
با کدام پشتوانه اقتصادی میخواهند بجنگند؟ با کدام پشتوانه مردمی خودشان؟ همه جا در محاصره ما هستند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6178" target="_blank">📅 08:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=GXFlQQbFMPL99OuKitmuYM7_gpOlEx2qvvIZ7PIOj8YGh4HIcm7Qf9a69gzckHFe2P6Rybhsfz85WWpn_UYp4cVW7Rl9b56DHYLZDncL0Faokm3P68zdXk2GDl8lju5GUM8ZYPRXODiqbeJojQDpsoS49r5oL07Gu3sQ_kciZ96BimKoCZnS-ciA_qz1mF_86f_hO-Jcorra3AJ8-nsM2eRkUGgFB2pjk_giCybNORsGxvGwwGxWkoiG1hpTKxYs__RiD87pTTElgON6_LsxkvLS1nohQtEmgs4QwKdwG5uS9_n6RIKT5PPvOgpRaX8uecZdxrTHU7CpjWftT5smiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=GXFlQQbFMPL99OuKitmuYM7_gpOlEx2qvvIZ7PIOj8YGh4HIcm7Qf9a69gzckHFe2P6Rybhsfz85WWpn_UYp4cVW7Rl9b56DHYLZDncL0Faokm3P68zdXk2GDl8lju5GUM8ZYPRXODiqbeJojQDpsoS49r5oL07Gu3sQ_kciZ96BimKoCZnS-ciA_qz1mF_86f_hO-Jcorra3AJ8-nsM2eRkUGgFB2pjk_giCybNORsGxvGwwGxWkoiG1hpTKxYs__RiD87pTTElgON6_LsxkvLS1nohQtEmgs4QwKdwG5uS9_n6RIKT5PPvOgpRaX8uecZdxrTHU7CpjWftT5smiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پل  کهورستان در اطراف بندرعباس
که شب گذشته مورد حمله ارتش آمریکا قرار گرفت</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6177" target="_blank">📅 08:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6176">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار …</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6176" target="_blank">📅 08:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6175">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6175" target="_blank">📅 08:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6174">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
حملات شدید به بوشهر</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6174" target="_blank">📅 01:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6173">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=rd13S5pp3Kce2cy9fpX1B_3zEhMs-C1kBcIzJxS1W10WbsOI4Zl5yMm6F_yeys6DbAZEWPTSeHC5tQZj208lKrKKqpufGoLsElX9B44vrWhqGk_2emnFfS1GGMgXrNpIKkOP4CA0Do1etuFX_ITx412w9AeVaNzJEkEKCuEYOibKHDvYJggvv18-gu78UagO_75uaTEVCABDih44ovev7qxpfBNLdXktrjvNFLfLKv5AAi3ZSoiruio6xY1VtxnvTGdSFbxwqs0B1ZW1V8dqhlvHo8CE5uxYGm48SfztDYa5QdB8XbXUIKunTFMFOmh4OxNKB-QZrEohR_8lqFrS3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=rd13S5pp3Kce2cy9fpX1B_3zEhMs-C1kBcIzJxS1W10WbsOI4Zl5yMm6F_yeys6DbAZEWPTSeHC5tQZj208lKrKKqpufGoLsElX9B44vrWhqGk_2emnFfS1GGMgXrNpIKkOP4CA0Do1etuFX_ITx412w9AeVaNzJEkEKCuEYOibKHDvYJggvv18-gu78UagO_75uaTEVCABDih44ovev7qxpfBNLdXktrjvNFLfLKv5AAi3ZSoiruio6xY1VtxnvTGdSFbxwqs0B1ZW1V8dqhlvHo8CE5uxYGm48SfztDYa5QdB8XbXUIKunTFMFOmh4OxNKB-QZrEohR_8lqFrS3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏فارس: جزییات حملۀ   آمریکا به پل‌هایی در شهرستان خمیر؛ ۲ نفر شهید و ۴ نفر مجروح شدند</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6173" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYCu8XrF-1WqfnO07o-fr9OaKRkYH1w8FqQMzfE9ZZDlMdXe3zyxME8VlPcIdomEPmFYv6E6wgnaYe7qNwZ1AyBqGhZuogz80itTU6NtXBkS0y3gAjYL9gwZ55u7zFKCD9SOlrEVg1hYxeeZexZNr89hUAV9Ifaeqa2MaFh0Q6F_h8Cp-J3H_r2I_g6ZwkFRUt1kWI6L1SKqFJAv_IbJMHdEt9vwTzRYkyv6bY55NmmA_mcih6bOVpyK58g9LTH4SEY_vNrImKx_28PZV2h7RRdQsvVwPblwpLzBdEeugkG3pRXNeHeyQ1oHW1hZBvzV8IVIABR6U_YGDiHuKssflA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6172" target="_blank">📅 00:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6171">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
صدا و سیما :دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند.
بندرعباس مهم‌ترین دروازه واردات و صادرات کشور است و شبکه ریلی بخش بزرگی از این حمل و نقل را بر عهده دارد.
این حمله می‌تواند به حمل و نقل کالا ضربه بزند و به آن اختلال وارد کند،</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6171" target="_blank">📅 00:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6170">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
حملات گسترده به حمیدیه و شوش در خوزستان</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6170" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6169">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
حمله جنگنده‌های آمریکایی به فرودگاه ایرانشهر</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6169" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6168">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6168" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6167">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvN6mGH82G3l3PXloMB1deKH32fNRjlO05S1bsHHvpbAwWT6urCpo9gOW-RcSDjPp8gY2IcNSU5S7HKWmv6bJpZOaZM1paSixFfF8ontgJGptXEyo8j94yVaTWKFoyqMj1OTyRhl1izkrtzzwZR2N_epZKDaDwZTWE-FZi0eCYuKbVjBCdr_1VO9tkju-p5jSUlMJ8BqPihnewVciKZf83D6F86TYmAHqj3lcb7U7cTT2q16tZkK-e3w8kT-VZ9qtX6dKLHHJhyurk6ODrXPn27nrRaN5v5ZMYtr_xiZpkcyu81dNY2stJyJnGkUtSmtGDbHhSdTr0LSbWcUc5LLDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6167" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6166">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6166" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6165">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏
🚨
🚨
سنتکام: موج جدید حملات در پنجمین شب پیاپی را شروع کردیم.
🚨
مهر: حمله مجدد آمریکا بندرعباس
در ساعت ۲۱:۳۵ نقاطی در بندرعباس مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6165" target="_blank">📅 21:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6164">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=gfbXEY5ZxR3ypvQKnm1S83cxl3zpWnTtxnn-HlnRDwu8pn33c9T_bbfkckBwBi8FuLJLIyyVgkZr0hAL368L0GNYNje1GzZKjY9DRyVP9Mp-NK3glkqqn6RGApiOHRTnYdblv_HRxRzz3wK7gwM6bLU2XeRgiLwXiZw7OwzQ7nxLyRlS519T2EAzJ620OEoTV92z7Xyz7qD7XnA1Qdx_hrU17sxREk5nYPvlVc2QCN3PMDMVDyN4-IRj4gzYQ6mQfOPbqGdsuSwGAduuxoeIrLLr4Qdqk5nr15EaWSJ7zCYN565vpcuUx_pDTYvi-OIIBTpCcaV6g7qrQ9CnZghInA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=gfbXEY5ZxR3ypvQKnm1S83cxl3zpWnTtxnn-HlnRDwu8pn33c9T_bbfkckBwBi8FuLJLIyyVgkZr0hAL368L0GNYNje1GzZKjY9DRyVP9Mp-NK3glkqqn6RGApiOHRTnYdblv_HRxRzz3wK7gwM6bLU2XeRgiLwXiZw7OwzQ7nxLyRlS519T2EAzJ620OEoTV92z7Xyz7qD7XnA1Qdx_hrU17sxREk5nYPvlVc2QCN3PMDMVDyN4-IRj4gzYQ6mQfOPbqGdsuSwGAduuxoeIrLLr4Qdqk5nr15EaWSJ7zCYN565vpcuUx_pDTYvi-OIIBTpCcaV6g7qrQ9CnZghInA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازغدی : اگر میخواهیم اغتشاش نشود
باید با آمریکا مبارزه کنیم
(که حواس مردم به جنگ پرت بشه
و تقصیر کاستی‌های حکومت بیفته پای جنگ
و دوباره جنگ بشه «نعمت» !)</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6164" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6163">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
استانداری هرمزگان:  در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6163" target="_blank">📅 19:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6162">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0FeRv4Tlfm8EAHk8vUTvRsxIjVU263ebOLwkweTZk-Pmguxb9CKrTslGmhysMf-XrzGvCUmac3G9hkGNJHyf3n8BbYPwZpBZykg1ed4wrYtz3A3drP1mLJoarujKn6jsPI5ub43frjQqiGlk1-WgKYgGy-gwxa8Bl3Z2qLmz1t_Lj-5jDk7F_EiDYH77Y3JWwQN2JYJFZTavry8YL2VxjTNWmYBd46gkqHkg68UvfH_1Ixr8zYgcXqwGaL4RVYKO1lVzgojZYseK3sD3r0A7HXu9q3ELFLed6DEXwBXEEzhBmJYwxIFSes4Q7Pz7CaHxVpHjxR3DJc9QawmOfzrkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز :
پاکستان به ایران هشدار داده‌ که اگر به عربستان سعودی حمله کند، پاکستان آن را حمله‌ای علیه خود خواهد دانست و اعلام کرده‌: «این خط قرمز ماست.
»
پاکستان و عربستان قرارداد پیمان دفاعی مشترک دارند که بر اساس آن حمله به هر کدام ، حمله به دیگری تلقی می‌شود.
🔺
برخی اعتقاد دارند که یکی از انگیزه‌های اصلی تلاش پاکستان برای میانجی‌گری میان ج‌ا و آمریکا ، نگرانی از وقوع جنگی است که دامنه‌اش به عربستان برسد و پاکستان را ناچار به ورود به این جنگ کند.
اینک که تفاهم نامه کنار رفته، پاکستان بیش از پیش نگران این موضوع است.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6162" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6161">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
استانداری هرمزگان:
در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6161" target="_blank">📅 19:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6160">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=jImyMp-059WAcGn1XBh77Z-ypxcO5RsOppGVegn-I1UznT3UYMBIlE4YfQml8P2acQD5FIv6-lpI6f0IYn6dXORZBQ-y3lte-vKFR5i3vkKErOiXF_gIWIkV4V1q52e7lmQsz1SjZMxA7AvfiqUMGnpRsHEFaagzcOxoIQZsXCFKhkxPP5qVlyf8f4s3VCiKZfk_QLuXKA7YwqHZD76ku7CyOxK8UNnPvwM04SxC2WM1aFDxPFMuglqkEbLvmmvbPE0b_aOY3QoW6Ok1L8OXg_FxoAgPRLv2BMmavgMWGaK6kUMKnghlkrAYRnslePkQD3YDI_NB7ZfNNM1udxdS-3q5x2m4KL1yMTG327VLnmuecvvEPp78eK__5OXfQENUaNlzwSER1WU-xGDa6KGcgJ4x2M6nfbFuI4x2V1XnAclqT2DE1X7e9396I3G6hjr_5t8dkV6PK3wQVnKErdRCywgB4l7pSoKDmjoPr_N9HUUqILXcvSthZYWzEoYmf9om73yiXwe9yEwI_nyxpPnP7iKzi0WoirgzcrEOT7EtlHTxwOsTqbTOqfSH5XVpe8_J3vN3fxjanXmoBwsdVtpw1y_3VK7UFhmUoKEYAVEtzahNtH1hpknzLCba--da5lWtK6JF_CSJ4SGhD_qtS0cbweadJyMdF1UzDJb_ELvnIpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=jImyMp-059WAcGn1XBh77Z-ypxcO5RsOppGVegn-I1UznT3UYMBIlE4YfQml8P2acQD5FIv6-lpI6f0IYn6dXORZBQ-y3lte-vKFR5i3vkKErOiXF_gIWIkV4V1q52e7lmQsz1SjZMxA7AvfiqUMGnpRsHEFaagzcOxoIQZsXCFKhkxPP5qVlyf8f4s3VCiKZfk_QLuXKA7YwqHZD76ku7CyOxK8UNnPvwM04SxC2WM1aFDxPFMuglqkEbLvmmvbPE0b_aOY3QoW6Ok1L8OXg_FxoAgPRLv2BMmavgMWGaK6kUMKnghlkrAYRnslePkQD3YDI_NB7ZfNNM1udxdS-3q5x2m4KL1yMTG327VLnmuecvvEPp78eK__5OXfQENUaNlzwSER1WU-xGDa6KGcgJ4x2M6nfbFuI4x2V1XnAclqT2DE1X7e9396I3G6hjr_5t8dkV6PK3wQVnKErdRCywgB4l7pSoKDmjoPr_N9HUUqILXcvSthZYWzEoYmf9om73yiXwe9yEwI_nyxpPnP7iKzi0WoirgzcrEOT7EtlHTxwOsTqbTOqfSH5XVpe8_J3vN3fxjanXmoBwsdVtpw1y_3VK7UFhmUoKEYAVEtzahNtH1hpknzLCba--da5lWtK6JF_CSJ4SGhD_qtS0cbweadJyMdF1UzDJb_ELvnIpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی جدید جمهوری اسلامی</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6160" target="_blank">📅 19:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6159">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=e63uwXAFcA7EDhXiaKj6cIrqMuXwqfb06XTKPtMlLgmDZEcUQm7iWFh3GsXpJiRvgyTXRHBHbVClkF1dPmOCstt4O0dfj_gLHP13tdRNZW5eURRPVyNwAK5is2kKwLMOkK7-Bm9woH5hynsWYorX-SIHYdTMwO7qwGXlgaQ48yEmpXwucTuZVmpV9TY9uUSkps_4OMDAKmJOAM9xb1V_t1WF1ocSIBeOD0Nr5tpokMGWv5IFREwdqo8oOsA_8v3_tSB_pnkpEjoCwvrKb4nkvJjh2BGv13aFwTeT062t_ID_oGU477yFd2d9kuayMEKuQG7zpNaAlvSN_8a81PkIdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=e63uwXAFcA7EDhXiaKj6cIrqMuXwqfb06XTKPtMlLgmDZEcUQm7iWFh3GsXpJiRvgyTXRHBHbVClkF1dPmOCstt4O0dfj_gLHP13tdRNZW5eURRPVyNwAK5is2kKwLMOkK7-Bm9woH5hynsWYorX-SIHYdTMwO7qwGXlgaQ48yEmpXwucTuZVmpV9TY9uUSkps_4OMDAKmJOAM9xb1V_t1WF1ocSIBeOD0Nr5tpokMGWv5IFREwdqo8oOsA_8v3_tSB_pnkpEjoCwvrKb4nkvJjh2BGv13aFwTeT062t_ID_oGU477yFd2d9kuayMEKuQG7zpNaAlvSN_8a81PkIdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، تیر ۱۴۰۳:
ما غنی‌سازی را ۲۰ درصد کردیم جنگ شد؟ ۶۰ درصد کردیم جنگ شد؟
hafezeh_tarikhi</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6159" target="_blank">📅 18:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6158">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ایران که ۴۷ ساله که در آتش فتنه اینها می‌سوزه</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6158" target="_blank">📅 17:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6157">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سخنگوی قرارگاه خاتم : هر چه در منطقه سالم مانده از نجابت جمهوری اسلامی است!
ذوالفقاری: «همه آنچه که بنا به نجابت ایران هنوز سالم مانده، یعنی تمامی زیرساخت‌ها در منطقه، زیر ضربات پولادین نیروهای مسلح مقتدر جمهوری اسلامی در هم کوبیده خواهد شد؛ آن‌چنان که اثری از آن‌ها بر جای نماند و گویی از ابتدا وجود نداشته‌اند.»
سخنگوی قرارگاه مرکزی خاتم‌الانبیا همچنین دخالت آمریکا در تنگه هرمز را «خط قرمز شکست‌ناپذیر» جمهوری اسلامی خواند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6157" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6156">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=S2tHCGZk9j0WjC5K1w0nk9mRddS55wpxQemwKEcjKZVZcRG0jnqoq7T5Nikl1_QyHxHBfzEmKo5lAS4S32OIKpIibEk2rp5yBcGCI12_q42Zk2beLSM-TdyBU2UDxcbNixnhl1tmo_ExXUBPRAr_EEesZeAg3dHPiRYUQAvWe7L-U5gGWo3tGl3lOj1oXlcYyo_l6R7xpJyjQVYKyhqy0I4LzYcQylcM7wn3hKcMriMv695JRPj3xsuNDdd1PSvNykGEETKUObF67fWmlMcl9jmQmBUp-wGSxJHX2M30IsTJz1coXs_Ia0-C_8qLIJH6x5FpGLReboKYdlolg6QXTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=S2tHCGZk9j0WjC5K1w0nk9mRddS55wpxQemwKEcjKZVZcRG0jnqoq7T5Nikl1_QyHxHBfzEmKo5lAS4S32OIKpIibEk2rp5yBcGCI12_q42Zk2beLSM-TdyBU2UDxcbNixnhl1tmo_ExXUBPRAr_EEesZeAg3dHPiRYUQAvWe7L-U5gGWo3tGl3lOj1oXlcYyo_l6R7xpJyjQVYKyhqy0I4LzYcQylcM7wn3hKcMriMv695JRPj3xsuNDdd1PSvNykGEETKUObF67fWmlMcl9jmQmBUp-wGSxJHX2M30IsTJz1coXs_Ia0-C_8qLIJH6x5FpGLReboKYdlolg6QXTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شب گذشته ج‌ا به اربیل در عراق
علی‌الزیدی نخست‌وزیر عراق با صدور بیانیه‌ای،
این حمله را محکوم کرد.
در این بیانیه آمده که «به آژانس‌های امنیتی
مربوطه در هماهنگی با نیروهای امنیتی منطقه دستور داده شده که همۀ تدابیر لازم برای ممانعت از تکرار حملاتی از این دست، و نیز مقابله با هرکسی که به‌دنبال خدشه‌وارد کردن به امنیت جامعۀ سرفراز عراق باشد را اتخاذ کنند».</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6156" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6155">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnTey3qGc0fcgVAoZ40Fpe1JWLcsFNvAMTpyoTGJorcnkOd9VTDAek89i41r9ELG90YHMvtCygyGqg7HZel_Q_06VQAGTjzX9jhqy9GQplJrasyRosod83zBKlhgeUYOpsNfC8aw24N99clNl8aIgByoPH-bYskPdBnfc96vfjJWzN5HJVQsN_5DLrtERtuqMBCs023iyVU1yPd1nvDqYkF4qqPLBYp_oLC8nQYh9muC2r6AjNVTphSSwU8RpvMFO6fFUoAkX0q1f3TYHRkOotkYo6stcZ3rgbHY_kNSkPY5FQt-gH4IT_ntUeQXeQbycP99sSQtLiZlW40OEelikA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وراجی نکنید  بگذارید بجنگند که صلح بیارن :)  مثل صلحی که ۴۷ ساله در لبنان  ‌ و غزه آوردن!  انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6155" target="_blank">📅 12:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6154">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">وراجی نکنید
بگذارید بجنگند که صلح بیارن :)
مثل صلحی که ۴۷ ساله در لبنان
‌ و غزه آوردن!
انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6154" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6152">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=uBO6pbIgV_rhoR7CHnSxxjRUUQ6dhcEtAZ4Wa6IS2NvepEfgGLAaVEZVA06G8NFb7mWHMHQJiWiO5pd3tEpiDUFPjqx5kU2WKFBFy9zxkmzAqbdUFqhkuRZRVs1FgnXU6rkWovc04H4eGOKQ2hoSzT4Ji_Xrl5QDKcv_-BdjMtM1_vD_vfpzSbDFzAT8vdfP9U5Z6hctd2Hx6yXZLHKW2R8NqRzx-DdYjadcjL-2l-QUfvDV89izWzbRzoW3QStB6HS32lAwq5U2bfisLAdGzRnUegmWXp5lg74yXmrWigFIMcCqlH6oSQGTkKg0fUaqtPRWxKRC8YAfBrh7qktG7gbkoNCPVTvvBcpnWjMvhkX3tJ9EHfhmQx6pvIT9CIVNu-b79MRu8LPmqlmCDsIQ3lKOqLbSuKGKFG-2M0ZPqNUMymRIbU9SbBPyst8yLIT8LZsu3kIqy9wHiR-TZ_xgUjUiKZfAw75guBK8apHZDnSjHYCDry1GMSom8yCZ_Qm1YofsFxgDHa1_jd_2o82G0STBhLyl-IN7TlcqdacI1J33aV3tDf9Lwvl54PnCQzf5duWS9eBwJF7j-ZD4QG59LKf7JPcZdowt7hykkkZXCN_V27wgsArT73Xprjkg4BlGWuyH6auPDqBdsu0eZ_gT0wh74LddJ052KcTHbPPVfUE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=uBO6pbIgV_rhoR7CHnSxxjRUUQ6dhcEtAZ4Wa6IS2NvepEfgGLAaVEZVA06G8NFb7mWHMHQJiWiO5pd3tEpiDUFPjqx5kU2WKFBFy9zxkmzAqbdUFqhkuRZRVs1FgnXU6rkWovc04H4eGOKQ2hoSzT4Ji_Xrl5QDKcv_-BdjMtM1_vD_vfpzSbDFzAT8vdfP9U5Z6hctd2Hx6yXZLHKW2R8NqRzx-DdYjadcjL-2l-QUfvDV89izWzbRzoW3QStB6HS32lAwq5U2bfisLAdGzRnUegmWXp5lg74yXmrWigFIMcCqlH6oSQGTkKg0fUaqtPRWxKRC8YAfBrh7qktG7gbkoNCPVTvvBcpnWjMvhkX3tJ9EHfhmQx6pvIT9CIVNu-b79MRu8LPmqlmCDsIQ3lKOqLbSuKGKFG-2M0ZPqNUMymRIbU9SbBPyst8yLIT8LZsu3kIqy9wHiR-TZ_xgUjUiKZfAw75guBK8apHZDnSjHYCDry1GMSom8yCZ_Qm1YofsFxgDHa1_jd_2o82G0STBhLyl-IN7TlcqdacI1J33aV3tDf9Lwvl54PnCQzf5duWS9eBwJF7j-ZD4QG59LKf7JPcZdowt7hykkkZXCN_V27wgsArT73Xprjkg4BlGWuyH6auPDqBdsu0eZ_gT0wh74LddJ052KcTHbPPVfUE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگر نوحه میخونن و مداحی و رجز خوانی و.. برای کودکان غزه و لبنان و میناب و….. از تاسف از دست رفتن زندگی نیست! میخوان در این جنگ بی‌‌‌‌پایانی که با جهان دارند،  از جمله و در صدر این‌جنگها،  با خود مردم ایران جنگ دارند، سربازگیری کنند! تا نیروهاشون بزرگ‌تر…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6152" target="_blank">📅 11:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6151">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">تمدن اسلامی! تا زمانی که توی مدینه و مگه بود قادر به ساخت «توالت» هم نبود!  مستراح هم نداشتن !! اما دنیا در چه وضعی بود؟  ۶۰۰ سال قبل از تولد اسلام!  توی بیشتر شهرهای جهان  داشتن توالت عمومی! اجباری بود!   اینها میشینن روی منبر  میگن «مدینه فاضله»!!  حالا…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6151" target="_blank">📅 10:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6150">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تمدن مصر باستان رو مطالعه کنید ابتدا تا انتهاش بر مدار مرگ بود! فرعون از زمانی که سر کار می‌ا‌ومد به فکر مقدمات مرگش بود و قبرش بود!  هنر و پزشکی و علم و مهندسی مصر همه بر پایه صنعت مرگ بود!  مومیایی و اهرام و جراحی پزشکی و….. همه برای کار و کسب مرگ بود و…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6150" target="_blank">📅 10:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6149">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRjbZ2TVwFXZfAlfLDxgzviZcVEQqusN0BvmgPQWCqn11vsp5Z5AT2p8vqObHSCXo8-mLjRycufiwwNDt-EBPPI_eTud_ny_b9k0ycdGBLJUoFDbWyFnKlgXWah4XV7lQsqqRouF1cmH60JhHsKEogWT8Bc4pbXtRTzDQv7jIT8lhH5emr4hAwofCVvqFKZ7xin335BFA70lKwL2lSYUBcLSkQyoG0ekFOPxi6CCplhwO5T0yKN4Q5kEdNV5GwEgIFeSlehHctL_JKYoyl75NSxm4EVTdcg1LzTeeRkdSlqVDo20ISn5HauxcV8LUjDmo0TbYBcsTwJSOPnNNDNiOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها شنیدید جملاتی با این مفهوم رو که زندگی و این حیات «زندان مومنه»!  آرزوی اینها مرگه! مرگ براشون رهایی است!  اینکه برن و برسن به بهشت و به زندگی!!  مرگ رو آرمان خودشون می‌دونن و زندگی و زیبایی‌هاش  رو پست و حقیر معرفی میکنن!  و اینکه باید دائم به فکر مرگ…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6149" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6148">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..  سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند. و از مرگ متاثر میشن!  تمام هستی اینها :  مبارزه، جنگ، کشتن،  کشته شدن و….. است!  زندگی براشون چیزی نیست جز  «مبارزه  برای عقیده».  و خوشحال میشن…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6148" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6147">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=AIaI8gUO2dB0o4rihu1Q4I4pCumJtz-M9D2raU8DZIGcVkg4RDheA7LMLiN2ZFqp6RmoYq8dAG1ppZWpBKAzj32JKXWIrpfeP62xVQDf-n2_W_w5MxcZ2QJEK4ElwBss3ohIjXIF2FjBsxeGWQdJ7iUPg_ndMDY0_GkfnCsVhBOGD5Au54D5r1TalMFD1x-T-tEhwLaRO-kDCXSYOJU50okKujIKoSd-HQW9ojbGbeDbwtgcj5WE6zOJsDBEuqJeqDTVorfpnCW0YtZkaKcYV5CPZaAg5J4q1nEpuTZ1Z8wnEow-35M0pQn82BMvczxJlu8T4w7BkIa32DLVRqx38w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=AIaI8gUO2dB0o4rihu1Q4I4pCumJtz-M9D2raU8DZIGcVkg4RDheA7LMLiN2ZFqp6RmoYq8dAG1ppZWpBKAzj32JKXWIrpfeP62xVQDf-n2_W_w5MxcZ2QJEK4ElwBss3ohIjXIF2FjBsxeGWQdJ7iUPg_ndMDY0_GkfnCsVhBOGD5Au54D5r1TalMFD1x-T-tEhwLaRO-kDCXSYOJU50okKujIKoSd-HQW9ojbGbeDbwtgcj5WE6zOJsDBEuqJeqDTVorfpnCW0YtZkaKcYV5CPZaAg5J4q1nEpuTZ1Z8wnEow-35M0pQn82BMvczxJlu8T4w7BkIa32DLVRqx38w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApUSxSlc1HJyF-3o0sHcW3hiDD3GKIZU39rgqdVh8_52InIqN5_4n3HCwpVw1ptTWKalzvRiJ_y761Sca9vvMcXwmWvFfuwGMMiAYyfn3YjLO3C6COc5IcWG0VnU7HJSdw2Rja7z-tF49jgHxRzqwItxLCO2fQpN5YTHmmRsiiZ7X13FCvmjgDHHxjMdRd3nfXMXEsORXs0fYved0TB8cpUGrx6Yn3yIo6ZUsAjU6HvO3In2lAv_F1JIg0jmidLqZ2f25m6HwRcc0b4By48MinlpOqLVYubRYwJD36CTWP9XBNF1kacilsh14jBu5pFCZ1EZIul4jLBOgK7tYzUJKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران به یک شهروند زن آمریکایی که در دسامبر ۲۰۲۴ در دوران رئیس‌جمهوری جو بایدنِ خواب‌آلود به‌ناحق بازداشت شده بود، اجازه خروج از کشور داده است. او اکنون در سلامت کامل در خارج از ایران است. ایالات متحده آمریکا از این ژست حسن‌نیت ایران قدردانی می‌کند.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6146" target="_blank">📅 09:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6145">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6145" target="_blank">📅 09:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6144">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">استاندار مرکزی : شب گذشته به دو نظقه در اطراف شهر خنداب حمله شد.
این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقا مشخص میکند چه اهدافی را زده و نه ج‌ا می‌گوید به کجاهاش خورده.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6144" target="_blank">📅 08:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6143">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اطلاعیه  ارتش:  سامانه‌های راداری، سامانه پدافندی پاتریوت و مخازن سوخت آمریکا در پایگاه علی‌السالم کویت را هدف قرار دادیم.
‏ رادار‌های سوپر هاوک، تأسیسات و سامانه‌های پاتریوت واشنگتن در پایگاه شیخ عیسی بحرین نیز طی حملاتی، آسیب‌های جدی دید.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6143" target="_blank">📅 08:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6142">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
استاندار سمنان : به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6142" target="_blank">📅 08:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6141">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUdb2yGlWr3wFQ9NHL3S_dC08wEKlubpwYJ-7PYqmCWDAhTHILEfJoAxmajbH9RcYO4br5sHKZ-MGhHEDb_JFFdSzZ3y-3f26i_-7OuhW0LmZRNaj7411f6cg1sged6T9J-Et-Se3W88BdjUSEzXsIvMx_WFAa0vdoUUrdc1eAiE2RVH6rQ-TPz8-d3H9ZhU5OO_ea7Si3W8tMdaCUNLoAfShf4MWJ8Cm_nYogFLtjW7n-nx4Ukt8fEe9mn5o4_a33QWSXjoz_PN-3R30BHv5i-xgY5SNuDsCgqdcteikJaa_bK-Su_Bd2mnMGw8ZQ22E5k9_et_vGr9zxOVfHdgqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین یارو خودش از دست سپاه و نهادهای زیر نظر خامنه‌ای  فرار کرده و به آمریکا پناه برده!
و آمریکا رو خونه امنی پیدا کرد برای زندگی و نوشتن از اینکه اسلام چقدر زیباست و خوبه و سعادت انسان رو میخواد!
حالا از همونجا به ج‌ا میگه مبارزه کن با آمریکا! مطلقا تسلیم نشید! تا انتهاش برید!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6141" target="_blank">📅 08:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6140">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">برخی گزارش‌ها از تداوم حملات به اهواز خبر می‌دهند و اینکه تاکنون ‌۹  انفجار  مهیب در شهر شنیده شده.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6140" target="_blank">📅 23:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6139">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
چندین انفجار مهیب در چابهار و بندرعباس
🚨
کویت : امروز ۲۱ پهپاد و ۴ موشک شلیک شده از سوی ج‌ا را منهدم کردیم.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6139" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6138">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای ۲ یا ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6138" target="_blank">📅 22:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6137">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-5utGYOIZkT5Buy3R8w1hbN1i8iqr6K0k-gYyNE94OesXwDcewYnDyE_DG6LuCSz7v-GNSPcT5i6PJOqNH4T6e3vuOe_8WICwjWTnGgIlWc8UoOPREyiSpIhOvc2mlkrLvSnFIuYQXFdLc1bF8pAXIrkqeZGcPgHdcgAo5NGXEDzuvKW5qv79ZM0Gp4v4W5X09KKdEO4w3D3Y_ko1XfpdZGVnea6T88RNpgYyzJ0fyHL_XlT2BvOSE9sUyKr4-OmPrNZCwSR2uDZoF6ygjuuNM_6AyfcPkmiFdSxEnzIBBbLBXdLjDzRJOHsGISfPZ__a6yr3MzDueBB40gB8qibg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما دیگه جرات حمله به اسرائیل
رو ندارید! خودتون هم خوب می‌دونید!
این ۴-۵ روز هم به همه جا حمله کردید
به جز به اون کشوری که بیت‌رهبری
رو زد نابود کرد!
و نشون داد دقیقا کجاست که سست‌تر از لانه عنکبوته!
ولی هر چقدر دوست دارید شعار بدید!
اون حزب‌الله تروریست هم رفت انتقام بگیره  هنوز و همین امروز هم نیم میلیون نفرشون  توی محله‌های مسیحی و سنی لبنان آواره شدن!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6137" target="_blank">📅 20:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6136">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">آنچه شب گذشته در بمپور رخ داد و موجب  کشته شدن تعدادی ای نیروهای ارتشی شد، قابل اجتناب بود.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6136" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6135">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e615d142.mp4?token=VwR7ych6d4t44iz7yc8tBq_65S2rPcm0Pc5s7mY-njifDXD4VM8xrbvMQwYLp1X2jOyuHIkutMVOld-LOk3ZjhHZPvgB_bYIhrgh4CXeouXFVNQK61IERznks7z-wp4ASiDe5WTGq55cLHImqwRD5QnoSWxOMZqhOa-OBQyfRBb8YU9yF5V1p2tZbutnhJHwA2GMOuiscBV7T3JqyPDYhfnCrRodiOwHwYgSYs1OQ6GC5qgRvgPpaTA3O7vv15AUuWAjcySu7yJLNgZQ_2cisAFkPbn49Exjfc9uYNNmJZaUsJ0t-33mgL5nyACp61ZS3OY1jRytq4q9tQk_nWqCKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e615d142.mp4?token=VwR7ych6d4t44iz7yc8tBq_65S2rPcm0Pc5s7mY-njifDXD4VM8xrbvMQwYLp1X2jOyuHIkutMVOld-LOk3ZjhHZPvgB_bYIhrgh4CXeouXFVNQK61IERznks7z-wp4ASiDe5WTGq55cLHImqwRD5QnoSWxOMZqhOa-OBQyfRBb8YU9yF5V1p2tZbutnhJHwA2GMOuiscBV7T3JqyPDYhfnCrRodiOwHwYgSYs1OQ6GC5qgRvgPpaTA3O7vv15AUuWAjcySu7yJLNgZQ_2cisAFkPbn49Exjfc9uYNNmJZaUsJ0t-33mgL5nyACp61ZS3OY1jRytq4q9tQk_nWqCKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش بینی تاریخی بختیار
در دو کلمه، برای مردم ایران</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6135" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6134">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=IdIMGf-qRUYAomyiGlhvXLulr4I9M8n-nEo_5RgShg6Nc6izyc8AbIFGlGZ4SO6rCAgtJ8dGVL7MOjmbQGeqnoGmdF4MPfal-We3kYU5aKpkfDSQHI8F3EBAE-we8Sv9-r24NQ1LivgK1BugnLcusWhrdVF-6PKAUrWmRmGNO639EtuvISMy4w2bnwn66NIPaUu03bUFWv9hjddYMH1zQzS0DNNX7ri0v1r47XZ70at_Xyr0epVvfX1ueqzr6wS-zn2O6UXnQD4-ChY_8Nqg4ZqQjOzTDDbwT2QBO1qhrk_a2crCMBwp2PhH_DYcUiW_cjDs4Q5XWMVlFdpuALkNToi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=IdIMGf-qRUYAomyiGlhvXLulr4I9M8n-nEo_5RgShg6Nc6izyc8AbIFGlGZ4SO6rCAgtJ8dGVL7MOjmbQGeqnoGmdF4MPfal-We3kYU5aKpkfDSQHI8F3EBAE-we8Sv9-r24NQ1LivgK1BugnLcusWhrdVF-6PKAUrWmRmGNO639EtuvISMy4w2bnwn66NIPaUu03bUFWv9hjddYMH1zQzS0DNNX7ri0v1r47XZ70at_Xyr0epVvfX1ueqzr6wS-zn2O6UXnQD4-ChY_8Nqg4ZqQjOzTDDbwT2QBO1qhrk_a2crCMBwp2PhH_DYcUiW_cjDs4Q5XWMVlFdpuALkNToi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی که فرمانده سپاه بود و سالها فرماندهی جنگ رو بر عهده داشت
اینجا میگه مطئنم که مسیری که در ذهن مجتبی خامنه‌ای است، بهتر از مسیری بود که شورای عالی امنیت ملی رفت.
مجری ازش می‌پرسه خب اون چه مسیری بود؟
میگه : نمی‌دونم ! نمی‌تونم که ذهن خوانی‌ کنم!
فقط می‌دونه خوب بود :) یه مشت چاپلوس !</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6134" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6133">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrPsfyIvVUEHImd3ScwO8cWLFC2bh2Uc4JfIXXpAw0Gte1JOzO_brzzNC50lSD1pzJCKZ0hLdhAIr_caCeO2RfbZ2JRDoWnZA9dzGMsloUX7i3CLtfI7R2ue2m0tGOyhNSD1hBVvSNWiefpxtrZ8TigpuvSx1XGpg8BkF7t_y24HyNf41hkP_V9oHSnUaKyACRY4oW24-yJoRFHG6gDWXqd-6cVARu4KtORQIYmzw2g-PfOVPWRUrfcJo_8o8aUny-gCzFIBEEP-TRz_CZbEP9OYPufXxGJKrAkYWBBn7fxW2_nQi7g2YAZH3vfbBA2TnxHxPjsT54neSbcXo3cBpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
سنتکام : به تنب بزرگ حمله کردیم.
در جریان این موج ۹۰ دقیقه‌ای از حملات، با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی و محل‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را مورد حمله قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6132" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6131">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حمله امروز به چابهار</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6131" target="_blank">📅 14:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6130">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
ارتش: «آمریکا بامداد امروز با شلیک ۱۳ فروند موشک، آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور را هدف قرار داد
دشمن به مهمانسرا و اماکن نگهبانی پادگان حمله کرد
‏ ۷ تن از کارکنان پایور و وظیفه تیپ ۳۸۸ ایرانشهر شهید و تعدادی مجروح شدند.»
‏</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6130" target="_blank">📅 14:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6129">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
سنتکام : از نیم ساعت پیش موج تازه‌ای از حملات را آغاز کرده‌ایم.
(از  ساعت ۱۳:۳۰ تهران)</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6129" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6128">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGN_csLQZhEGarBxpMY5klzsfe7XnucG-iaacdMet2hl-EU1eHhYWaUu4F2ELsPkYGNstDj_NAVfvSKMtDemECzYwJnNjOxNLk_FC0yge9KLRoK0nHnKV9xxngPz1UPSPiCoRe2D9-decCTqUvbWHA-6gExOEEZWvEeCv2h-hmo7jcQ47deyPopHMnxy2gRBhvExdUB12lanl7kcN6uD2x5VTFH4mN4rPave0wHYaXfNHv1__4MKqJxk3b-icxHStiWuG3iyJd8QOCKnYvoSAAGzwZx05HtIJQAIrote-GsUhfd1mSsEROY7q7MOK45WUJDeDC9TbySUiOybIOdoJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابل توجه ساختاری‌های محترم
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6128" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6127">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=tp_Gz5WFxGQ9U93VIhD4QJssoW4Zg1ULRgV9p-SdeZSKJz2Nw4nRFF2bsW0Z4AGK6BiDj13ANb3Hb4HTQKKcO9_ygTyrUD-wxlqNd4rtEXwFsXNEDO9Gn0V9_vHNebhrSWUJ6roijxW0Nq1GM78IQWozAAGqIISFCyNqaAU1e-sewYJ-Xx2NEooXORGUxNA2f5hjDCYBs-itWo-6eT1jO6F4Mi83mrqbfljbOlCHA5hcqoO3Nu0jOFC6ySKAdACUbPez-A2x9kgSoT-GcAZGDlTbFns1RcwfwBaLiWUkRPGql9czSG_r6t01pqyZLVm1xXBzm5yY5R3ycH2HuMpI80Xax2-O0zVM_ljWl-SvNJc0jpVLrdZ32Q2u0OBuj9xmaPyUV8W344G6UbLJhxIdzVw8GKdKbaLomYeZ4Snvix-2tQW4UfgjlOocfz4niJcOZBFtKM67V9czIVPo9qmri8ZXuN_3mhcvq7zmbuN82TWwayUMqVnb7dctWOY6KAN9uputuj_a4fZM76jRYTU5U6OAsZ7h5Gdw2mBmGF5HOXHkcnKqhGgGftpflPoOrD6-HHCBkRMIisovj2db1Jj2H_QTA0idOLFWagaQFKCiT0RYhD4B__vb5ZQjitax7KI5K1mBI75RA0OO0CNKoMe7qPLu2QwCcU0o8QtNFuxdey0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=tp_Gz5WFxGQ9U93VIhD4QJssoW4Zg1ULRgV9p-SdeZSKJz2Nw4nRFF2bsW0Z4AGK6BiDj13ANb3Hb4HTQKKcO9_ygTyrUD-wxlqNd4rtEXwFsXNEDO9Gn0V9_vHNebhrSWUJ6roijxW0Nq1GM78IQWozAAGqIISFCyNqaAU1e-sewYJ-Xx2NEooXORGUxNA2f5hjDCYBs-itWo-6eT1jO6F4Mi83mrqbfljbOlCHA5hcqoO3Nu0jOFC6ySKAdACUbPez-A2x9kgSoT-GcAZGDlTbFns1RcwfwBaLiWUkRPGql9czSG_r6t01pqyZLVm1xXBzm5yY5R3ycH2HuMpI80Xax2-O0zVM_ljWl-SvNJc0jpVLrdZ32Q2u0OBuj9xmaPyUV8W344G6UbLJhxIdzVw8GKdKbaLomYeZ4Snvix-2tQW4UfgjlOocfz4niJcOZBFtKM67V9czIVPo9qmri8ZXuN_3mhcvq7zmbuN82TWwayUMqVnb7dctWOY6KAN9uputuj_a4fZM76jRYTU5U6OAsZ7h5Gdw2mBmGF5HOXHkcnKqhGgGftpflPoOrD6-HHCBkRMIisovj2db1Jj2H_QTA0idOLFWagaQFKCiT0RYhD4B__vb5ZQjitax7KI5K1mBI75RA0OO0CNKoMe7qPLu2QwCcU0o8QtNFuxdey0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سفیر اسبق جمهوری اسلامی در روسیه: مطمئن باشید اگر ترامپ را بکشیم نه تنها هیچ موشکی به سمت ما شلیک نخواهد شد، بلکه عقلای آمریکا با خوشحالی جنگ را تمام خواهند کرد.
کشتن ترامپ هیچ هزینه‌ای برای ما ندارد و با کشتن او جنگ هم تمام خواهد شد.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6127" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6126">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟  به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6126" target="_blank">📅 08:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6125">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwJe6Z2zuhGmZ7xjcR7IkaZE6Tz4KX0Gj6fe9h_PPkd7P1Tx_QrvKlAp4WKKnUNfkmK5Wsfus9AScwvcZuLN9uMI4_D0EIsEyNIa15W2RZtAjuK6v3RA6RkFMzLQdb5c0byoLANGteTynGzUp9yCykV1MaHCGTwBnHryHOoDAklzglM7_MA_5TC-BgND32gohMKgjqviVFBSILfIuKLWPxCMjb62dH6CDoW2DhhKA71yrou9u6As43Kci0ERpWuWx4OqkyLmYq85eGbxq2xXTBQzl4dC_Xeuq1Nic_RRlZq71VOlRJc_6wU6BXqK1tOkGhkvT-IiSv-RDcJQuZ2GKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟
به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت کاخ سفید برگزار کرد.
به گفته سه منبع آگاه، در ابن جلسه که ارشد‌ترین مقامات نظامی و امنیتی آمریکا در آن حضور داشتند در خصوص گسترش حملات صحبت شد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6125" target="_blank">📅 08:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6124">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=ftzrVPCGUjms8upJYiWhbV53NCWlmh2E6IG6fZ_NW_OHHTjKLiKddKaFZS99j6g-r_GeKAOdaFpUjuNia7HtL-_vsGMTnC4_4RaFub23HtHQdJP_nbsR6JLDoJPdY8zQOZGfPjBflU3MR87JAZQm_z3Fn3ctAO2E5FGjNGkpnYvTYmApLoFQ1JK8BV9TT8lj_eBpMukV9vciPrvbI-3ukFeDj2_KtzErZaI6mqchhW0qTtEB_-2ykwLKpGpe-w_nobY5GrhEerDGWtt3o-90mStvZXNdBy9ibX2QxfuFa5y4AxTqAK_1uynFRLBquSUUrNtfiQSxM1-rTGOhFV7Alb_oW-CNQlpXYW0nwk6wC66A4WUWwlBixCxZpcbsKMEeA_Gtdzr1QJoTSoE_4O5CxS7mH5F9WSUiUDE4yPNLfGJoXzP9j8lrjq00nRpC-1gI1tyzt917kiJMH-N-ZugsohSW8N6x4sGlIpdeW2ocyVoTpqJvxPrDI0S_3prRTxYfpTMyd29Z-JAyG4C6rJh8HIw5rA7YUsWYDzbenszIhNVmeePXB_s3aJ_00dKPRT-RYt_8aX2wPT45q5zzZ_o-r85LZnrPHu2hmiEsBV16bq8ykSy_bG5CmC5-uX5yhot1Qi4fGCsD8mB1g05qG7-gX27Oeh-y4Fi_uZiaaMPTjPM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=ftzrVPCGUjms8upJYiWhbV53NCWlmh2E6IG6fZ_NW_OHHTjKLiKddKaFZS99j6g-r_GeKAOdaFpUjuNia7HtL-_vsGMTnC4_4RaFub23HtHQdJP_nbsR6JLDoJPdY8zQOZGfPjBflU3MR87JAZQm_z3Fn3ctAO2E5FGjNGkpnYvTYmApLoFQ1JK8BV9TT8lj_eBpMukV9vciPrvbI-3ukFeDj2_KtzErZaI6mqchhW0qTtEB_-2ykwLKpGpe-w_nobY5GrhEerDGWtt3o-90mStvZXNdBy9ibX2QxfuFa5y4AxTqAK_1uynFRLBquSUUrNtfiQSxM1-rTGOhFV7Alb_oW-CNQlpXYW0nwk6wC66A4WUWwlBixCxZpcbsKMEeA_Gtdzr1QJoTSoE_4O5CxS7mH5F9WSUiUDE4yPNLfGJoXzP9j8lrjq00nRpC-1gI1tyzt917kiJMH-N-ZugsohSW8N6x4sGlIpdeW2ocyVoTpqJvxPrDI0S_3prRTxYfpTMyd29Z-JAyG4C6rJh8HIw5rA7YUsWYDzbenszIhNVmeePXB_s3aJ_00dKPRT-RYt_8aX2wPT45q5zzZ_o-r85LZnrPHu2hmiEsBV16bq8ykSy_bG5CmC5-uX5yhot1Qi4fGCsD8mB1g05qG7-gX27Oeh-y4Fi_uZiaaMPTjPM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=uQhNMIDIZoYh1avRn_FD_CBwFfHQL9l7tOekk0beyNyjveW0XyruQHMpNLufo0GT1SG_7J_AI7FU5wdS7r4rDjiB4zd77JpqCMdgnvXHSuHpQULXW_2djTNXbGyY_N5k7LGzkYQmJasC3sFj2WBoslbyZsVEKvcgYy5uCM2-BCogVjyKRRNt2Glt6jlIoK8sEMAOqYQQ44PCmnSQxcWQwdqPWnWgUO7ij9DxW4_pik1btqbR3YhqOlEfMTEmyhHQdF4mptC3WHOLqhMmud5qXj9FVLJCuo1ErtLisBnWCe74pOIK0Yp--XZYV1feKbGzT8e6Xsyq3ARHBqiT-B8yXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=uQhNMIDIZoYh1avRn_FD_CBwFfHQL9l7tOekk0beyNyjveW0XyruQHMpNLufo0GT1SG_7J_AI7FU5wdS7r4rDjiB4zd77JpqCMdgnvXHSuHpQULXW_2djTNXbGyY_N5k7LGzkYQmJasC3sFj2WBoslbyZsVEKvcgYy5uCM2-BCogVjyKRRNt2Glt6jlIoK8sEMAOqYQQ44PCmnSQxcWQwdqPWnWgUO7ij9DxW4_pik1btqbR3YhqOlEfMTEmyhHQdF4mptC3WHOLqhMmud5qXj9FVLJCuo1ErtLisBnWCe74pOIK0Yp--XZYV1feKbGzT8e6Xsyq3ARHBqiT-B8yXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6123" target="_blank">📅 07:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6122">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=QUg-ccugtEw7zpXoO7Xiu8bhvm4ksGsBExtC-n5sHPl6hyCm4oaUVE-7zLGV3ONP3K-B-5YRnXqer-hA5kD4bW4tG_7xRjnlREV6vPdI7AoUi4v7FbLwUoPt5oAv0MrkpvkRRWrjmYdFJ1N87XRvQwMP3CM0T_-c73rjThiAT1Yxhr79-e6KSfF5QL266-1CbQDXtcLew3aWoEkUJ3GHip5NcFaw6ZQJ4vMB38TxRVdRpZFKdCVKXdVUtr8xc5W2n8Wret7sSjloTqPQeuH0aZYvllHIZu1f3S4q4rebhHHVp-YKmGmLpteE9h8qFLnS321-YhZ78x1pIhH8wXaEfWVm8-yGbI8i7LB0kDHBywSFh1OqNRDSALEdI-Bq9rIMGyFsRKl28XhJw_u5vO3cn3tlc6fHR0UE7LPoPqZ5qsNXHL-G-26G-iHRquV5wCp3l4XAwIAlo8Y_p4n-VmjKAJOOnGobo8UisKhnOTeR8UWIDDbKa5Wj46jGOiuLwTS5YeHWKj25Fpi5PlYXsVjq6UTvc6koVG4YQ9vKko5vpWtfmx1lxN1vmMpXwc0K7IpuXmbZlAMoDbEQW9t3T4tEGtgd-sODGIwMNoq12hCg2lmRLm9Rgr-ZKBARec3TWUnvjw8s-knFfI2siNAS2zJFS6ocknhtxXHdTjARsarirTY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=QUg-ccugtEw7zpXoO7Xiu8bhvm4ksGsBExtC-n5sHPl6hyCm4oaUVE-7zLGV3ONP3K-B-5YRnXqer-hA5kD4bW4tG_7xRjnlREV6vPdI7AoUi4v7FbLwUoPt5oAv0MrkpvkRRWrjmYdFJ1N87XRvQwMP3CM0T_-c73rjThiAT1Yxhr79-e6KSfF5QL266-1CbQDXtcLew3aWoEkUJ3GHip5NcFaw6ZQJ4vMB38TxRVdRpZFKdCVKXdVUtr8xc5W2n8Wret7sSjloTqPQeuH0aZYvllHIZu1f3S4q4rebhHHVp-YKmGmLpteE9h8qFLnS321-YhZ78x1pIhH8wXaEfWVm8-yGbI8i7LB0kDHBywSFh1OqNRDSALEdI-Bq9rIMGyFsRKl28XhJw_u5vO3cn3tlc6fHR0UE7LPoPqZ5qsNXHL-G-26G-iHRquV5wCp3l4XAwIAlo8Y_p4n-VmjKAJOOnGobo8UisKhnOTeR8UWIDDbKa5Wj46jGOiuLwTS5YeHWKj25Fpi5PlYXsVjq6UTvc6koVG4YQ9vKko5vpWtfmx1lxN1vmMpXwc0K7IpuXmbZlAMoDbEQW9t3T4tEGtgd-sODGIwMNoq12hCg2lmRLm9Rgr-ZKBARec3TWUnvjw8s-knFfI2siNAS2zJFS6ocknhtxXHdTjARsarirTY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا میبینم راست میگه …</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6122" target="_blank">📅 07:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6121">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLWZqYj72dc8AQxaVRfujYrPu2FZJmqOgA26lExqpl_QDghrX2hbXF1FFImeGXTiz56xNpL1AhhMMvdiDDVHq0nSqtMchBew0oLd0lBbMCw9Pkbb2oGVybT68Sdgp05uWYhQ3vZS5rfrFaFo41bfECRclsOCoJsnWsl601bdTu0EeXbMFo2De5Q9Zik0bZycOMpOt2no7a4kUgLToBR3Zk6MWH0WffURijXCnrDbPplgR5lAO_vaAy50RlPhtUdiSgw63X_tk7bKrfl_lPFLVjmhDhsT0UobcknKFxmsSNw-HYmqcOvvsGTl4J4HyIgR3YE217Pw-9JueXHN5ScjIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6121" target="_blank">📅 06:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cjww9ikSQ0vSv9czwtfHHnzjKFdoXmSxvFI4301I01HBBBlBUMkkgTD7QP6mhTGi65eYU2KM8wGVKyXHDSyffe_gADAOh9tzpUHltblwba3vEWGz_1DZY_NSSSe7Ln5nMBy1GuiU3JJWb-8QRxTfUmWwesTFpENCFZocWmVF--875UzWHdvygaQh3TSBWH5IxPzxegq4fFT2hljMgvzZRIzoNEC70qvcXnajq2xuZL_a07m5qJDqTJcwPSiTTL8MwB9yrCkX5O2Irq_5Gugc6SZPs_grrz6cQUlkKsrAWoqH4KIjcBY0lVTtlBQaPMy2Xau7FQn74FLhE_s6oaWa7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6120" target="_blank">📅 06:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6119">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=fXQTijwz9semyYfAh7IA3-vvPfiDtCpu7KZLNSpXrhes0_sFU5Tq68sbnkWVPEQWs3cFuZkHW0wvoouPbEPJDlSPfKKfv07exyiYia3lmTOdI0g8fzV-WkVzjzbdUQ-S36Z2YDgxOUZ64vviXcXJxunWB5EJUdDIBCJOUuyjr1uHUX5YDhRjnQiUZxdFsBPLeWPuJPm3J6mIcyD4fgeun5cgbwRHlRjb4A0RJD1nCz6KmC4b6TmBg-fGh0LHLZkLPSscz3uHGQDN9ii83Rbee5EJjmEBZd85F887wqJ0caMFIQP8bclOxnfKnuifXLIV6aiE1DVOAR0hOCd86wQLRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=fXQTijwz9semyYfAh7IA3-vvPfiDtCpu7KZLNSpXrhes0_sFU5Tq68sbnkWVPEQWs3cFuZkHW0wvoouPbEPJDlSPfKKfv07exyiYia3lmTOdI0g8fzV-WkVzjzbdUQ-S36Z2YDgxOUZ64vviXcXJxunWB5EJUdDIBCJOUuyjr1uHUX5YDhRjnQiUZxdFsBPLeWPuJPm3J6mIcyD4fgeun5cgbwRHlRjb4A0RJD1nCz6KmC4b6TmBg-fGh0LHLZkLPSscz3uHGQDN9ii83Rbee5EJjmEBZd85F887wqJ0caMFIQP8bclOxnfKnuifXLIV6aiE1DVOAR0hOCd86wQLRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام فیلمی از حملات خود به ایران منتشر کرد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6119" target="_blank">📅 06:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6118">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=kafBjtK7hREdR0985pNUzuEwu7AoQAIfpMZnaP9gI141NAJQ6LH2uNmcI4UbfoGa3EvA-4qtFrCPGO95gNV-ZkEACqYN5XDovfWj_xURx0hoWQrI9BDvzxnfOyTy98TIRZBQrDfUCrdUQkPxNO4dtJLGQvw4fp1o4cWq2HVoxUxjq7RQektLz69xmWuSv5WUnLKxz4P4pEC1QYiuYaDNLAl-H-zAQL94N7JppCDdkWdRamsBxAetMne160qnuHfaiPzvNQewyN2asf4WFDBzs7UM4AjrW5j2tmU0aCJd3OQsNDkaasdgdv7JlVGbCRmtHzg6QI8bfivvSEwj143Ibw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=kafBjtK7hREdR0985pNUzuEwu7AoQAIfpMZnaP9gI141NAJQ6LH2uNmcI4UbfoGa3EvA-4qtFrCPGO95gNV-ZkEACqYN5XDovfWj_xURx0hoWQrI9BDvzxnfOyTy98TIRZBQrDfUCrdUQkPxNO4dtJLGQvw4fp1o4cWq2HVoxUxjq7RQektLz69xmWuSv5WUnLKxz4P4pEC1QYiuYaDNLAl-H-zAQL94N7JppCDdkWdRamsBxAetMne160qnuHfaiPzvNQewyN2asf4WFDBzs7UM4AjrW5j2tmU0aCJd3OQsNDkaasdgdv7JlVGbCRmtHzg6QI8bfivvSEwj143Ibw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : امشب، فردا و فرداشب به سختی به آنها ضربه خواهیم زد و هفته آینده پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد، مگر آنکه  مذاکره کنند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6118" target="_blank">📅 06:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6117">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caeb092620.mp4?token=BqFoULtpkcXgNvAOK0B8mHzlNU0gh25OsGrDm2Jo0myyMJeZxKAoYWwP48axSREP_xLKCI59ewOVLvmqnaBnvi6CKlpSyK_Vxz2zE07xubULvk_GQEmDs1TzRly-QUtms2Tv3-Kvqe9dSz2EKfsvhQcMAt2RhJzwT6gFxORrEDZyhewGtOewGrHOATAuYkhUu-LVNhvIqxbqLoz9yhPPaaeKbihotR5oOzS-A2LDvqIp-7P9gf5o7s47kUEifQL95hfnKld-ROrR2LhdaulUz_3hZ_v1dTIiZQtsfdAC3eOciBTv6ETLcpPNYGroT-1XhXOMCkeLS3MfPHHzgmsdKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caeb092620.mp4?token=BqFoULtpkcXgNvAOK0B8mHzlNU0gh25OsGrDm2Jo0myyMJeZxKAoYWwP48axSREP_xLKCI59ewOVLvmqnaBnvi6CKlpSyK_Vxz2zE07xubULvk_GQEmDs1TzRly-QUtms2Tv3-Kvqe9dSz2EKfsvhQcMAt2RhJzwT6gFxORrEDZyhewGtOewGrHOATAuYkhUu-LVNhvIqxbqLoz9yhPPaaeKbihotR5oOzS-A2LDvqIp-7P9gf5o7s47kUEifQL95hfnKld-ROrR2LhdaulUz_3hZ_v1dTIiZQtsfdAC3eOciBTv6ETLcpPNYGroT-1XhXOMCkeLS3MfPHHzgmsdKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ناشی از حمله پهپادی امشب سپاه به کویت
گفته می‌شود مخازن سوخت ارتش آمریکاست.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6117" target="_blank">📅 06:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6116">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360d24e506.mp4?token=tPj4BihAijm9fwcAUZC4V07a14CxRHBeFi9d34Oxf1PB81iInQHaFAufYOoGbXRyOw8t4LzS1KE7JpvwREYTK1HQvujq7i2Z1zwGJ_TQLmux3gtgFnPzMqaEut95eqsdgDED5wfUmUxSaDo-HgCfAKxCvf4hA8YfxKIVwKHOvW-K7l4e-ze4v01QJ8nmgkHKyOFPuA9fpUhRKiHZqKMFUpy4vAOJe3VDyBgxcdWyocM__PnxSMOkNzZilltL35wfyO5FbDqYqlIP4Q_qVDU8P8IwJDvHymvbsMZwsxUp4NYB4X9lJfGCYa4qaNN_NVG_I3v-IAYFhp5MwY4mbABkIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360d24e506.mp4?token=tPj4BihAijm9fwcAUZC4V07a14CxRHBeFi9d34Oxf1PB81iInQHaFAufYOoGbXRyOw8t4LzS1KE7JpvwREYTK1HQvujq7i2Z1zwGJ_TQLmux3gtgFnPzMqaEut95eqsdgDED5wfUmUxSaDo-HgCfAKxCvf4hA8YfxKIVwKHOvW-K7l4e-ze4v01QJ8nmgkHKyOFPuA9fpUhRKiHZqKMFUpy4vAOJe3VDyBgxcdWyocM__PnxSMOkNzZilltL35wfyO5FbDqYqlIP4Q_qVDU8P8IwJDvHymvbsMZwsxUp4NYB4X9lJfGCYa4qaNN_NVG_I3v-IAYFhp5MwY4mbABkIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی با موشک‌های حاوی بمب‌های خوشه‌ای به بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6116" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6115">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
ارتش : به پایگاه‌ها اف ۱۸ های آمریکا در اردن حمله پهپادی انجام دادیم.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6115" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6114">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‏امشب اتفاق جالبی افتاده، به محض اینکه خبر انفجاری در شهر و استانی منتشر میشه، مسئولان جمهوری اسلامی سریعا مصاحبه میکنن و میگن دروغه و همه چی آرومه!
‏اینطوری مثلا میخوان صورت مسئله رو پاک کنن.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6114" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6113">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZpotZE_7ckTcsU6g2nYZH6g_mg6J5J5MFll6Pg1L5ghPdsBpj4LaN9a8GnTCR1B0zTUN9tUohfigk81A7-Vp6UrgEZQvr8L8iZYviD8az1y8UjnOnG3rfUzLdBIe4o6Le0-pxh2_Q1dP2ptfvpeYXHQH6YB2GNg7_olgTDJZeSRzCOycbwxi9ztAeD1cT7YmqpB2hywf44Nz6Oj9OL56-HffqgU2opMoz-VcpfpeDEMLElno_mIuZ13Y3eW8JJLR79uw7pi7fmnj8B9eIVkhWETlDH6jZhgj7bmkMA1U_TImOzyjRtvx7Rq9xbrJBIghKJs1wJdYjg-Et3ZAhkDWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگارهاشون می‌نوشتن که کشتی‌ها دارند  از مسیر عمان رد می‌شوند، تشییع جنازه،  بریم و کاری کنیم که  کشتی‌ها مجبور بشن از آبهای ایران رد بشن  و شروع کردن به حملات به کشتی‌هایی که از مسیر آب‌های عمان میرن.  به زور حمله میگن کشتی‌ها باید از مسیر ما رد بشه.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6113" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6112">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6KgD-cwkAGM8skAImMdOEu9inWf2-DARQ3aI7Qvsm5uXLu7sbFu5rlI6FUE1eEIMRNXeIh51WzgIZcZJwllObgKpJB1Uho3i6UWqDJAjZwuzDHkzIQb_mDIshGTXewcvEoQaCN1Wjycht_SgL0rCw_k_ITk4HqIIC9nPuzhqRRuwCP_WLjLoS0nFnShSRLb0RWxGLo3lgYD3khPrJEh3eCEUgWLfiBHcdzgaVKrJa--vK0fLD69Knwvl_ebWt9cwz9DPslei8j3KESn1YXrq6G67pzZU0EeZ7jrypjUzXDN2UkkfgKG2Jl4mJ8Nnb0KvK4yyDsq9yCGE8oWDjbSlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا در حاشیه خاکسپاری جسد خامنه‌ای و جلوی قالیباف شعار میدادن «مذاکره با دشمن خیانت است»  هنوز به سه کشتی حمله نکرده بودن و نزده بودن زیر تفاهم نامه</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6112" target="_blank">📅 00:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6111">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=R3-s5gU0aIgp5IKLQsMhpazxjRMcrqB52PH_dYunLUroL0EI6-MoCLcKx9-PuLmb8KQfstundeBrGU5P4Z8KwRMYsHoI05F87BMKxmhune5xq4D8ecbpgt1o1iRjMCpF_IWKH0TYsiN3rscCL5jXJb3K0ZYY8S7GSBC29PMTM0DLv29k3JQkTLQUq_CykURm9Iss0K-G2_9Xrd5G_SvNE_LxF0AKrrRjGFSs9_cZutUkQEa0Hh4ige8l4f8gtbg3lA424bhz6ID0iyjnYsnNWHVLqLnTUfb_6vxUSCoCu-c0NeRf8RzBXEBpDZRGUkVExzimNLz98sbbxwmk-cHV6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=R3-s5gU0aIgp5IKLQsMhpazxjRMcrqB52PH_dYunLUroL0EI6-MoCLcKx9-PuLmb8KQfstundeBrGU5P4Z8KwRMYsHoI05F87BMKxmhune5xq4D8ecbpgt1o1iRjMCpF_IWKH0TYsiN3rscCL5jXJb3K0ZYY8S7GSBC29PMTM0DLv29k3JQkTLQUq_CykURm9Iss0K-G2_9Xrd5G_SvNE_LxF0AKrrRjGFSs9_cZutUkQEa0Hh4ige8l4f8gtbg3lA424bhz6ID0iyjnYsnNWHVLqLnTUfb_6vxUSCoCu-c0NeRf8RzBXEBpDZRGUkVExzimNLz98sbbxwmk-cHV6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این استوری رو ۶ روز پیش گذاشته بودم  میگفتن آمریکا میخواد آتش بس حفظ بشه ولی جمهوری اسلامی باید «کار دیگر» بکنه!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6111" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6110">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550f13e765.mp4?token=HZirn2hKPQ0KGygoy6eeAVjGmFbnC6LzKm-FI-DEWFApLN1UtEaukLLfB2YODDdBo6t9_arCMjfPDHo1tbtc8PjHUAZFuT5D6VPCtzx7_MrCBi3okeEk9uPMKR19dva_zu2tFL5slrr_14pO187dHMlNi7TVlLbjkSYoxgMRFzhrgKpzzRWVHZo6MNWtj4DE22N1wlEBM4f4TaiHG0AT51qBcjEp0D5WDqUMX-UdJ8jXVREUbUxeWTX37JoZpuYyItHgE7w5Ofx_TdfoDrgCNt4ygWi0nmLAt5jRrqBsug-u4ZKop2znK_PjvigaoMiEoK_zncHcHwb2GLvvqOjQckR_nKWT0VLkdJ1PJl2tdMRpSHf9NUqVAQ2pzUyMKDhC-P-fzQwN-41HRusgAEBrQCwvH-vcnojy9xnxsXYDzSKUUaaJw2Vrd01KIBlnAY2ivgwExWAasMPO8yAaJxy0tK7r5ZdNr0EJEF79ScAn4Q4TUX-BJfP3JyDCblabMAqeyRx1IpUJSDIrzl0dmwnKdhn5jLXk7xPWLOVmCxDPycD45G_mUaMl4CE5m9Pem1a0EveItUEj-MkAfCZg1iqYxqdVvAxZ1ncMQIZvEVAqKdK3PqYj6kVsQVS2pdNfDSlFb4cLZJnClRmEwTcs2EQvobOujDAu1vHa5ufk5gAktHc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550f13e765.mp4?token=HZirn2hKPQ0KGygoy6eeAVjGmFbnC6LzKm-FI-DEWFApLN1UtEaukLLfB2YODDdBo6t9_arCMjfPDHo1tbtc8PjHUAZFuT5D6VPCtzx7_MrCBi3okeEk9uPMKR19dva_zu2tFL5slrr_14pO187dHMlNi7TVlLbjkSYoxgMRFzhrgKpzzRWVHZo6MNWtj4DE22N1wlEBM4f4TaiHG0AT51qBcjEp0D5WDqUMX-UdJ8jXVREUbUxeWTX37JoZpuYyItHgE7w5Ofx_TdfoDrgCNt4ygWi0nmLAt5jRrqBsug-u4ZKop2znK_PjvigaoMiEoK_zncHcHwb2GLvvqOjQckR_nKWT0VLkdJ1PJl2tdMRpSHf9NUqVAQ2pzUyMKDhC-P-fzQwN-41HRusgAEBrQCwvH-vcnojy9xnxsXYDzSKUUaaJw2Vrd01KIBlnAY2ivgwExWAasMPO8yAaJxy0tK7r5ZdNr0EJEF79ScAn4Q4TUX-BJfP3JyDCblabMAqeyRx1IpUJSDIrzl0dmwnKdhn5jLXk7xPWLOVmCxDPycD45G_mUaMl4CE5m9Pem1a0EveItUEj-MkAfCZg1iqYxqdVvAxZ1ncMQIZvEVAqKdK3PqYj6kVsQVS2pdNfDSlFb4cLZJnClRmEwTcs2EQvobOujDAu1vHa5ufk5gAktHc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو رو دو هفته پیش گذاشته بودم.  معاون سیاسی نیروی دریایی سپاه اینجا در جمع حامیان حکومت بهشون میگه خیالتون راحت باشه، حملاتی که ‌ آمریکا انجام  میده «واکنش»  به اقدامات ماست!  «کنش» نیست!   تمام این ۴۷ سال همین بوده!  یه کاری میکنن ، تنش راه بیفته،…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6110" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6109">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6109" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6108">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=WeBzoR-DPH3jb6dl3AvHQI6mr9Xv4-i0sCJRceBoDYYOZjIiWPj8tL5hITWeGTFKqNTn4lSWjrZIOzbUg06IFHa1RmdjMKBmfDNOhxQhgpiwCF_8X9zoOn0PrLB3kUbiXHef4txf9dYLpxCuW2wuE3nDAd30iI0jDj_h1p0FZ_UUHZ0adtUFBe7aSV2HX9JiLROszHhXS4nO7uyo6d7-qT01p298eHdeY5GRKF6JrdfXxiXcB-RrNF_StuaSUcg2TP0zw_CLHWx1m_gNpTOy5I0AW0A89rA8Ha06QgttnK0ZXVMqnpORJWgkSkyUUE6FKh3t7P3yweImGDBSzrk_9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=WeBzoR-DPH3jb6dl3AvHQI6mr9Xv4-i0sCJRceBoDYYOZjIiWPj8tL5hITWeGTFKqNTn4lSWjrZIOzbUg06IFHa1RmdjMKBmfDNOhxQhgpiwCF_8X9zoOn0PrLB3kUbiXHef4txf9dYLpxCuW2wuE3nDAd30iI0jDj_h1p0FZ_UUHZ0adtUFBe7aSV2HX9JiLROszHhXS4nO7uyo6d7-qT01p298eHdeY5GRKF6JrdfXxiXcB-RrNF_StuaSUcg2TP0zw_CLHWx1m_gNpTOy5I0AW0A89rA8Ha06QgttnK0ZXVMqnpORJWgkSkyUUE6FKh3t7P3yweImGDBSzrk_9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گشت زنی اف ۱۸ آمریکایی بر فراز چابهار</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6108" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6107">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا : محاصره دریایی ایران وارد فاز اجرایی شد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6107" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6106">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
چندین انفجار در بندرعباس
🔺
چندین انفجار در اهواز
🔺
پنج انفجار در قشم</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6106" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6105">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTnAvSwUsGPO76ngioFCtjRJIh2aBvM4gbYWVNFqc3AvkAKyW8inymlPPczb9TXoHhd2LtId13RuK8dkrpy9u5z5Z3tDlQt-cubN9IgLWBB0-EsvRGCiohsU7_0vcevBL-LnBAgQ98DVvwmbJS4WXWzjLRxudzZUu0uwgZAtB27mxzxhwBx-BjfiHUEEux6L6gYnY-Wmif1m-F4eUaYi9N4VeeREi6Bi6DPpRoKCnywD8jtUDFkK0xC9KtLzP1j0NxReOH6UomVpPxeRkunywkOOgaB7qShMYvnmy9BceVPrzQl_DOo3dH2HNL6sFOvmdr7T7BICQEiQ4qwOcfDONg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2077085449948938568?s=46</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6105" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6104">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
دقایقی پیش : حمله به قشم و شنیده شدن چندین انفجار
🔺
حمله به یک نفتکش اماراتی در سواحل عمان
🔺
فعال شدن پدافند در کویت</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6104" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6103">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1y6LsakCgW6rv7wwEMJ96SUPGEe1qzbmti_TKdvEgw94SQcV_JLrkPME5aa7LyFruLtwnQVFxhD6Rw599FoNl2GYfJXqpsrII6JunYEz-qttEdjsxRIkuleSskU5gaV2aIdzXRrlJoT8MVKl5xG_Q8mic--45sGiZ4HaNg9MteoGn85sTyWpX3iKhoq3MFulOI6zOBLG_3NXvpaR_WtMe5ekglKn7CfB37PWZGrNUMZk0rx7SLVU6tNRRn5h-tD7GojC_KN7SaVmuWfUz7p0PoizTWShGxY_cOKA6PwDaorYIZLK0LCNQZZHIYHkmDobGO6iqdDeByA1nXlC9-N-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهپاد‌ها (قایق‌های تندرو بدون سرنشین) آمریکایی این مدلی به یکی از مهم‌ترین مراکز نیروی دریایی در بندرعباس نفوذ کردن و حمله کردن.  گفته می‌شود که در این حمله یک زیردریایی ج‌ا را نیز منهدم کردند.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6102" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=hUiw-WUBo1pR9DLQ0C9LMhzZ_CTv9ZXmjAR5oZk8YvYQwXGE38C-gW-FaYG_IlTHtgZnn3LEdIqHnQGAJa4B7_MY6G3aCLh4KQky8r27h80QZU9AnBOlqc2g5kiEp4Mb-XWzwqlVeibvBYRtl7Q2d1o4M95jXZMiBWtXsJ4kTYSmN1NpMu2of6oMsG3r8TkGn1xddt9qnATdd2OYGbPqNAFLEWbPkd0cu4_-u3DiRNzBn7kPpHJpZUz17s842quKIk0brwE5uTWn40z4KjbucWnY5QN4TN3cfoV22saH9LGEyseZ-mTze9CJQDc5UYvC4ddx6cgW_AhuEMKjSgKLhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=hUiw-WUBo1pR9DLQ0C9LMhzZ_CTv9ZXmjAR5oZk8YvYQwXGE38C-gW-FaYG_IlTHtgZnn3LEdIqHnQGAJa4B7_MY6G3aCLh4KQky8r27h80QZU9AnBOlqc2g5kiEp4Mb-XWzwqlVeibvBYRtl7Q2d1o4M95jXZMiBWtXsJ4kTYSmN1NpMu2of6oMsG3r8TkGn1xddt9qnATdd2OYGbPqNAFLEWbPkd0cu4_-u3DiRNzBn7kPpHJpZUz17s842quKIk0brwE5uTWn40z4KjbucWnY5QN4TN3cfoV22saH9LGEyseZ-mTze9CJQDc5UYvC4ddx6cgW_AhuEMKjSgKLhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جنگشون :)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6101" target="_blank">📅 16:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXATprell5a4udXrEgLmm0UdFZ_fLlFAQilScDYxPL8w4z4wegoWHBgkBQZcWF0WXMOUyYkmdICKNfYvQBcQexugaMujZlhHlSRjvo3EYuc76ku44AWBmDVWfP1cKUQAQjvr6sgAEvoy0VM7YMov6jkrxn3XVSoZ2UfR2qa6vozN-sbOSc4H65RzFvD0ZN5uWZwPMP4CCF9Dd-PLDxRuvABa0d_Nr77HyVn4RWLxRi5i2zgVijPa4uqSITrkxUJ3sZ52Syf7z-w3VDe1xqursSQ49uemu7ES0ePl2bkAUBPoofiOFE_Mh1pUO4qU8V4iK_D4AVs_QK-F5MOpU3nRiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.  این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6100" target="_blank">📅 16:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6099">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">۴۷ سال رژیم اسلامی</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6099" target="_blank">📅 15:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6098">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jl5-EfZkn3yXncPwuHCXfdtQzFGZ-MFKAs_GaF4D1amo4ap15VE2wfyNkyugzzFFasuIp8QiUKX_g9w3bqlcTbOEdAR_jPNzfxzdwNKbjjwWNPB0uZoOkxUjTROqE1E2-YoLNsDzvtBK21V10-8awn7lvr6W8eg4ySTdWyko5qFUehIAKoK2ViZudrTFmXHRWADRx0xHlmlNBGHtqmWIMWlkul3kje7yg5VBXmOczS1ABPkDQnhQV-jWa8m56KGW78DOp20fQC0Q7G9zDoo2IZ0uvHlQhkTUF0kkRLCRrBK5zwv--ua9YpEnPeq2iV4fni5JKZ-VSKB40EaFoo5gKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
تخریب ساختمان مرکز آماد و پشتیبانی دریابانی نیروی انتظامی ⁧ بوشهر ⁩ در پی حملات هوایی ⁧ آمریکا ⁩ به مراکز نظامی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6098" target="_blank">📅 15:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6097">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6097" target="_blank">📅 14:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6096">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=JWMQv1hix0cX_l55WgyQ_kvzvjWeCrvb7NVIyxlrTQ8tErZJEURczI4ocS1QRtaEjihIfYefbwf-5waQ083DWSoMnLhWv6I9_CrNg-q6FTbOoc7XzLql8T7ba8r2uwZKqY4HPmGWyH1eISiyaIXknGd5l0ZbNbIwHn2nd-WGsPTg07DcgquhD0xFZeBzO8IxtHWS-hwCd2nLHvM6uy3XaRqB_Jjur3oQsqtD_Oj2U-6__LC5IedM_ndqTcFvMhA0B8ewlRrl79KXXwUK6LpyE9su0k8XgNA3pQkYhpub46CxmIHY88M0Q600c64YcrxHJYhrV6tyP6JKUoc-lMTZew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=JWMQv1hix0cX_l55WgyQ_kvzvjWeCrvb7NVIyxlrTQ8tErZJEURczI4ocS1QRtaEjihIfYefbwf-5waQ083DWSoMnLhWv6I9_CrNg-q6FTbOoc7XzLql8T7ba8r2uwZKqY4HPmGWyH1eISiyaIXknGd5l0ZbNbIwHn2nd-WGsPTg07DcgquhD0xFZeBzO8IxtHWS-hwCd2nLHvM6uy3XaRqB_Jjur3oQsqtD_Oj2U-6__LC5IedM_ndqTcFvMhA0B8ewlRrl79KXXwUK6LpyE9su0k8XgNA3pQkYhpub46CxmIHY88M0Q600c64YcrxHJYhrV6tyP6JKUoc-lMTZew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌پرسه نظرتون درباره اینکه بدون هشدار قبلی برق رو قطع میکنن چیه؟
‏چمران میگه:
‏شما اگر بدونید پریروز چند نقطه برقی رو زدند دیگه این سؤالو نمی‌کردید.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6096" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6095">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnB0p7oPLxkT9B69m6HRCe_ICTjit6gLdt1HTNYcpOHMHgVWaaMPVHkPK6RMMhK_oZxlNQWLqDhZenUBnCEyvwwafuitpy9VvVzOpXv1XzR9T-ejtvkUXzLn85qiwsHxvSwgxy2i_mRjhtIuyAuUvUPBiqjATWVTS0pFQJFGnWrVa0zW7dq48qT69gIBTARQl9aAm7GNyFEepWvTbHiUltxpELPLVO6NNrzpUy3TezOiX71FkH2CMqtlhlKlGQTnjP9rScsZNrH8Sostgs8kbTCnVm-AiDcdtqvRthk5cVy3KEroGCNpcwTw_9g3JNfS9AUCs6IpfEGjPEg0H7i27g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ترکیه، دیروز جمهوری اسلامی
رو با اسرائیل مقایسه کرد و گفت
رفتار این دو شبیه هم هستند.
(کاری ندارم که ترکیه خودش چه افتضاحیه، اما نشون از تغییر رویکرد ترکیه نسبت به ج‌ا داره)
یادمون باشه فرمان حمله اخیر از سوی ترامپ در ترکیه صادر شد! یادمون باشه معاملاتی بین ترکیه و آمریکا رخ داد، که آرزوی ۲۰ ساله دولت ترکیه بود.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6095" target="_blank">📅 14:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6094">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.  در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!  مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی)…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6094" target="_blank">📅 13:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6093">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mw4e8-37e9uO9r5zqRkz819vJuvf2KbIEp2mmNlgZUSM0e-eLsKae7iZPWVIBrbiae-4OV_VBUVaxRVgzSspydL6OUVl4s3KpGhFOkMZMvGPu2FbtuDhCQF2GWnt5HYxiwEE7MtscHBalIEB2eoLE6wQA37bS9mBPueSgzaNnk1EV4z-zlKQY9zargeDZ3DqvOvp79Rm_Q1C2_9hyVgYsS3VYg2-m6WmJLcUp0efLvqapPOqJ70ZMDXI1yLEPOp2uNYlmgAjBJom8CUn7UDaX6MOyf_MbkixnlSw4D8uiA2wBlJvaOvz75UF6t-Esd1cWVaANoivVKt7jlaYIIgBOA.jpg" alt="photo" loading="lazy"/></div>
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

<div class="tg-post" id="msg-6092">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=KBfdPNegAGJ3UvT2bmxUBPcQPsmHmI-4sFq3ByIFz6I2V-w1iSkHrcOz7G7ZHDP2bXJDwmwftiUU2Gd4QP0lxOxNYUkyK9MkUZ3R2vooTV0rQg6xHfkw9gzHqrCsxRkc-1coyWdBQGbN_KU9En0dD7c8qV9Vvlow3LuZBnKQ86gCoxGNtenvOGrObW63xMu_OBhegyF_L5E_sFw8tTzJ_0CuII0P647enw3CQEDksR4oNaCLHDsvSrd8LXWihXkfgWpFGu3LBxwHL9DIkoekhYO0apLc_3Hx9-PKgrq8WX_0TTRTwpLlAEkaK5nWU3vWmDjbZjmj949i-VpzTMyV2FuagG5otpa9ww3I4dB8Ct-ebwHUZz_fNcjw18CJD7VPyhFcOFiOZxz1PYl_ISa8UUeRbKPK-RwhQsMASn6VYyA3wn6jb-59bW3Y2vFzRLMeT5l28ZsEa4rsWHqnOvsfutZAG_RD8C_R8NHmb3oZVXzr-wUzXOLyRp7y8C3C2xhWWTR9mnABjhJRvRHUu6nOBxkhGJ1p3YEYYwg2qmP_p4_Hz2mviMzrprzr_Tdj1Zy2y1GwDaXcKuebgEALVTpEpzn61tWyaRHPPvC88pOB-craiHdYGhOiAYCzF0y6v00xJQUc1mrRhkc1ytsxdoxwdRz9nNgx_0J6_2UQxMNdp2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=KBfdPNegAGJ3UvT2bmxUBPcQPsmHmI-4sFq3ByIFz6I2V-w1iSkHrcOz7G7ZHDP2bXJDwmwftiUU2Gd4QP0lxOxNYUkyK9MkUZ3R2vooTV0rQg6xHfkw9gzHqrCsxRkc-1coyWdBQGbN_KU9En0dD7c8qV9Vvlow3LuZBnKQ86gCoxGNtenvOGrObW63xMu_OBhegyF_L5E_sFw8tTzJ_0CuII0P647enw3CQEDksR4oNaCLHDsvSrd8LXWihXkfgWpFGu3LBxwHL9DIkoekhYO0apLc_3Hx9-PKgrq8WX_0TTRTwpLlAEkaK5nWU3vWmDjbZjmj949i-VpzTMyV2FuagG5otpa9ww3I4dB8Ct-ebwHUZz_fNcjw18CJD7VPyhFcOFiOZxz1PYl_ISa8UUeRbKPK-RwhQsMASn6VYyA3wn6jb-59bW3Y2vFzRLMeT5l28ZsEa4rsWHqnOvsfutZAG_RD8C_R8NHmb3oZVXzr-wUzXOLyRp7y8C3C2xhWWTR9mnABjhJRvRHUu6nOBxkhGJ1p3YEYYwg2qmP_p4_Hz2mviMzrprzr_Tdj1Zy2y1GwDaXcKuebgEALVTpEpzn61tWyaRHPPvC88pOB-craiHdYGhOiAYCzF0y6v00xJQUc1mrRhkc1ytsxdoxwdRz9nNgx_0J6_2UQxMNdp2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی خامنه‌ای «علی الاصول»
با تفاهم‌ مخالف بود!
و نوه خمینی هم این چند روز گرد و خاک به پا کرد و گفت هویت ما در مبارزه با آمریکاست!
اون‌هایی هم که نگران زیرساخت‌ها بودن
الان سکوت کردن  و صداشون در نمیاد!
آغاز دوران «علی الاصولی» !</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6092" target="_blank">📅 09:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6091">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سنتکام ساعتی پیش
از پایان این مرحله از حملات خود خبر داد و نوشت :
🔺
جدیدترین موج حملات خود علیه ایران را به پایان رساندیم
🔺
در این عملیات پنج ساعته، به اهداف نظامی در بوشهر، چابهار، جاسک، کنارک، ابوموسی و بندرعباس حمله کردیم
🔺
سیستم‌های دفاع ساحلی و موشکی، سامانه‌های پهپادی و ظرفیت‌های دریایی ایران، هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6091" target="_blank">📅 09:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6090">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flfTMyMtR-5baKdj3Dmtyf_MljrnLK3zzVQjJlRoZ3P5xvm1c8NaO0UpF3iQ0w4vBsWWmwnoXkQMBTxFqwcMgbUkk8280DwmV0rOVig4xVa_ZSTXsOESa9Yk9GXVeetpfDvQMCxM_Li2own9r0t6puy344G2YvfaH4LUu4AUnXqRT7-62vxGrNYBANBGApljkQppp_BJw9RWd_UMDOy48sAmDzkNLzu8TZrgy8qgPAj0_mHuTSHfFuf06ZA6di1nO9vQKFhcypBdKVeeDDm-bD9dpzZsI9yE1lu4xFCKZ2X0W4KvgPYk-qih1E3WJvOOkLiBaL2gxN0tbJhHaYtYmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته سپاه به دو سوپرنفتکش (در سواحل عمان) حمله کرد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6090" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
