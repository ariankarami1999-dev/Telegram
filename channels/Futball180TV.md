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
<img src="https://cdn5.telesco.pe/file/Yg0vjgrv1Ox2Ty-ArkAxqB_5TKLeR3ZWGpdFSEFx6-OIZDkKfrwy_0R5jnVa_gzUpsOWUK1dVV-5JgBxsIHP_VTVbk73YU1FDTmCTbYpuWa3Wu83z46eCsORyolQ4irgm_pQlnFoPnG_4YpcFoSmzEtYJGq93aRc-nqxYFZMyVMCMtXFUBv3Ow1G8E9U-Q-3x09DqIX3WWNdcRdFZKnCvy76Yq0Xy92x3MeCVKzYrr6A3HpWAKHUkwk1cu2HM3Tf5YuRcUnAbQbbxhs-eXPx-Xo4j6IPSq7fHMJ_tZN5FOtJEs5HlSsliEI3Xexc0fEB_n-BMTxjqCNHAEIoXn_fhQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 653K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 06:02:13</div>
<hr>

<div class="tg-post" id="msg-97817">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbkEaH-lDotqflb7_ExgQcmtqgoV4Z9HxIE3pBgsQB7e9gygcg9--eP4UjY2u2Xp5lfw9d_ol7UtuTrFc-HP-ij_4jNGs-PCv8eaUW27YcgzehOyUkohDPN68RSC28UjNF5KrIa6tvUlgcsDykmfoA1l1JNCUM3yBzuFPe8QgPEgyyuGXOC2nfEVor04P9_5VmivcJMgTli1M-WqDGXHZ7bqm_r_WVGYoMZxqHy4YQB6eEhM_RtEszxUVlLwvBqYI0OqGnITqJElelL8AFgzakueSqN7Fb6HGScwgv3b-zCVCoMZk5TYg5ymO0KJPN8uVmaGSx6HLmdETFuJhUtbLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"حواست باشه بعد بازی کامنتای اینستات رو ببندی"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/Futball180TV/97817" target="_blank">📅 06:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97814">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LMzx4ne8s92BFzy8KcCWDa2SI3E0GWyx6kt8BFY_0c7__U7rhoEIJ_swWa-AGyQH7pwVNl8rzK4J9iQzAHZHqVg8BMQHWUPdU-NF0UiTv2pA-AiUiA0rFBuCrLLifsaXC5fJ56Xp-gpLfRDvmZOYxThprjy-CaZsybgRywP7BmceyKg-gCesHWBI1QuFme0QbMo4RPaMdcWH5d5ZXXU7X0EMDG1Svsw8_SminSQQwVoSCxwvbr8us_G0W_FNIr-gYuvEh5QCYcPA3m3IsBtR-KHLRcuttqR-29DXC04ww4geqVmEsJmTi-MUcIK-mDNCyQNvw7IU3__stEuRLuvoZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RMTkmn2T46TzglaQjjiDBsIwv0TciZMszfV42aKha4M9-n5nN90qss1zEWsgDahzq1sxatd0dIKa59VZvnFlBggQMQpfG5PRUjOvZlVdA43d0c9J2Gsjz-73zEb932whqa8_KCDmYgMCEPv7OGPfh71UcfUqMTFvuxZxKCShoa1FNCEqg_LRlwit3Q8AI7aF4cEyevFbCpCBn1Jn0B6uu6r5aHgQaPYUJeMjnunFmtAikdJUUssTtBrlXjfepFQUhTE9_9apDv_PL-tin9wUJLkkC3s2Af0vgCX7s7bIMlMf_3I9rgLVSgjL2RFS-yiAssjN-VNLkYlpiFxioldBEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D2LT5bSMDG1gkgU__-08h8-2B07A1psZG9AFJH__AtVOjB-yDp5PspTuOLhxuMZmPoI5EvqVmW88sJgpMk6mJHh5-Br_eV9O3g2k9sHhKR_mjvdDUHXQd-CJKLrybvQ3g_0HCSpjAWAnnnDFgoTxwYks8EZ8Zyj6AV_KP_qlwYFd_D7OfrxCy821ArQhkZvlr0wZp1Y38wXDo7dudFdHfhkh4q8qZS_1NenYEPn4YI3snpyFXChVeRGhkp5xorDXgqLmKV_7mauXV-3k8HLqBmmNX7_1WkK2pxNeTukHqAtjX6l46nBzNPJi_DLzkZeRVDa3pbbFGEZ1nQqcLk4urw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
از دلایل صعود پرتغال در بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/Futball180TV/97814" target="_blank">📅 05:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97813">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKQCdzist201NPkFxVEWNfb_bxNajY43RP2rK-P-wUmhU4DI2TUwlFulEjLev41dBPIeAuYlJ6q7MxZcDqaKjqHw9zHLWotMXKlqttS5s9vgvbQUUIb5pDc-4Ugbc4PYW_pZ96-S6tTCy9QO7ASmxwyzbKZ7T9Tmc7B3T21xPlvonZn_GW8NPVNJ3InGWRzOXdjpAP-YZrqdPr9GDTPRpkgZEus5bYDnHaCelC2xKMyfCBoVk5xQ0Ug0QxN298GbfQWNcm6LBLqRGbCutwaJ0r1sATD6vakExqlzv86Uv8fe5NQfL4oOwFTChFvJMH1Mul8bVsgf5CjkrUUJS4R1KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مارتینز کسمغز امشب هم با هزارتا مکافات و کسکشی تونست ببره ولی در نهایت این سبک بازی محکوم به شکست مقابل تیم‌های قدرتمند تر از جمله اسپانیا و فرانسه و حتی مراکش خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/Futball180TV/97813" target="_blank">📅 05:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97812">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTEZ7ZqH-NKDHUI1GFJvkg5HT9PL-El0DpcbWU-iZPtWgs6Ry0rHY_nwz-Qm-7K65OxrnOzMm0zzZSgBQq-gBcX6KmpF0uzQybl9x_imRl4GF1Y02HJLH4GdM3R9PNf8YSB2aIHdmvtj0kTbJ7Ns9pqBjxlVvamc_CYQmvVd13lsH1A53FlO389AxJ7cuMu8jidQwikmkqQ2T3kcvncvMxC3RgENyawvZ9ljnFM4WeUdoASr4seKN2C39qcAsl9rf-NBBlM6t3ejIgds7It79LwIGhNvPi_HJ-g1-lm01_1907MT5O7cHUU91BQQrDCIRUIgpFhht0KhxoIzbli5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
قیافه لیائو قبل از پاس گلش به راموس:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/Futball180TV/97812" target="_blank">📅 05:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97811">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owxbNOmbrkWXV9hKZeghqNu07NuIJK7EBJy4kG7hsKwP7yAaGyR6D85ucnUyEiaGgQ-UUmaGcL5WZvNAgIseDenzw2pUwNmgRlQIoVrSYaNnLw2HyJ-B0bJAT959bRR6UxfghhxP7jXz29Du1Vb_WMP8Qrn_kiBNbokNg9umh5sv_6tNIRaBocLu2YnvtPZ7HbcIPeFBCQZ2JjLdYVDKMNRYG33hQIkm2gz0sdXA3IycUIiEJ4FKRH9Xu_srlzbkhekzMAmqPDGHNNeMzQnbcEWwdQ2SQ5UoFtDYzlioV3XmePOe6wpzxRNj3PTYDHIEPfl21wJqveE_rBS77NOGtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد برونو فرناندز در مقابل کرواسی:
❌
0 گل
❌
0 پاس گل
❌
0 خلق موقعیت
❌
از دست دادن 2 فرصت مسلم گلزنی
❌
0 دریبل موفق
❌
10 بار از دست دادن توپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/Futball180TV/97811" target="_blank">📅 05:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97810">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kz8r1HP1qwcwx5xT4kgq6Xh_3nNj3r8jqNXejVbpNjEpof1FAFlUte30cC7ALdbTJrpxsAxZqjggzfOcCbDO45_W4Hu19U8FegU_xnfir_v-6UHFj3k0ulsOqqert-ce6dYLJfDvVSzdxyDZWImOjoyArhl-iN7LiLsEaKDNj_YsrJKLuBTEwQjJVlssAHlLYHL-SodGM29PD9swCpmWV7rYf29hFDfxtp7S84ghOF8Fmu3UObGtnmzxcP457lte_L2tGyibDnxetT6Q-BU_PTa5U30I-2lpLqQVYhC98rKWc2cQsys2R2MphaEON0jI_qPkLhMbexVVMlqXrSWrOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
| کریستیانو رونالدو مسن‌ترین بازیکنی است که در مراحل حذفی جام جهانی گلزنی کرده است.
🔴
کریستیانو رونالدو: ۴۱ سال و ۱۴۷ روز
🔴
په‌په: ۳۹ سال و ۲۸۳ روز
🔴
روژه میلا: ۳۸ سال و ۳۴ روز
🔴
گونار گرن: ۳۷ سال و ۲۳۶ روز
🔴
ایوان پریشیچ: ۳۷ سال و ۱۵۰ روز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/Futball180TV/97810" target="_blank">📅 05:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97809">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">از اون عکسا که دوس دارید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/Futball180TV/97809" target="_blank">📅 05:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97808">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZyS7Q-1Ilu3buu9CIpxUYS7rOcylAUjahn6xYf5R1MK_C9jFdiO7RvNgO-9g7l30FJh6vKiFS6KnSEkoc1TyOxiJGJCBXFCi3Nzb7ig-Lg1a067jhMPt1PBZjVMtFtw95P-ibN_L2JdmxOV5Bl1zlyMDu7aC74OWLcubMRicA9s4QG2uUFZquD6FgyxLxt_W58V-QULA384rnuXzhVLaeV_mtdYiawQBqkp8FSE1TnXArxX06y6ON2UiR34-mSk__Y2XlIxBD8sAE8a87D1-RBFXo3aJhwxXcfyfEnSN_HmjP6pFELORIQ082t5qtS3SKrz2UwspjLuhuTWzhoseg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
خواهر رونالدو: رونالدو بعد جام جهانی از تیم ملی پرتغال خداحافظی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/Futball180TV/97808" target="_blank">📅 05:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97807">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e979b7d1cc.mp4?token=dun18YQQi6KulhEeweTvWQ53V3cUfWy7tK5xCuMJwTsymc8jPI38iavKSU4RYIP7cFI__DcatcAdPeaE3sT3pxuqZV5_aVc61IzLtKs7DCNUElb-N0xeYWvcfV0jkvmVRhqNKOHFWF4HRwWpxbr7N90dphahS7gLWm8jtn9WBWlHCAzQktw-W_wNjE90AoNuYGBWc0v-AeiXuBxiJSsf-3iX_VwlqB4GA3SkxL4H6vFGpZOrXz8ziqfUW1h7HQZGRKxwguITWQHfE4FjghhukDxk7ZHZzmVy_4M-bt2GA2O0K27m_duXP3qgzayYIaDFe6pehJ_YAelETJbG3mnQVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e979b7d1cc.mp4?token=dun18YQQi6KulhEeweTvWQ53V3cUfWy7tK5xCuMJwTsymc8jPI38iavKSU4RYIP7cFI__DcatcAdPeaE3sT3pxuqZV5_aVc61IzLtKs7DCNUElb-N0xeYWvcfV0jkvmVRhqNKOHFWF4HRwWpxbr7N90dphahS7gLWm8jtn9WBWlHCAzQktw-W_wNjE90AoNuYGBWc0v-AeiXuBxiJSsf-3iX_VwlqB4GA3SkxL4H6vFGpZOrXz8ziqfUW1h7HQZGRKxwguITWQHfE4FjghhukDxk7ZHZzmVy_4M-bt2GA2O0K27m_duXP3qgzayYIaDFe6pehJ_YAelETJbG3mnQVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همینجا که دریک رو صعود کرواسی بت زد دیگه آخر داستان مشخص بود:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/Futball180TV/97807" target="_blank">📅 05:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97806">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‏
🚨
🎙️
اسطوره کریستیانو
🇵🇹
:
🇧🇷
‏همیشه احساس خاصی دارم وقتی درباره برزیل صحبت می‌کنم. ‏من خانواده‌ای در برزیل دارم و مردم برزیل را خیلی دوست دارم. ‏چون آن‌ها همیشه در طول سال‌های حرفه‌ام از من حمایت کرده‌اند. ‏می‌خواهم به همه آن‌ها بوسه بفرستم
😘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/Futball180TV/97806" target="_blank">📅 05:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97805">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
📊
🚨
🇵🇹
#فکت؛ گونزالو راموس به طور متوسط هر 47 دقیقه یک گل به ثمر می‌رساند. او 4 گل در 187 دقیقه بازی در جام جهانی به ثمر رسانده است و این بهترین آمار گلزنی تاریخ پرتغال در این مسابقات است.
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/Futball180TV/97805" target="_blank">📅 05:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97804">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5L29lqBffXoRqfOhSQv3SXSWiSiLBOulnz93lx-kb0CcxdhFDOpcCa__4Wd7YzySwt1nemtoKFpy0xhc1odBjwbXaaPtsHnnhDglKQwErdtIAsHK8eaIwMeFFty4www8WaJbxFf40Kbv1gY3iNue4Mnb737PD8GX51EbCMvSKj6FAG9BitI2EKaOniTW5EfI_Jw7a7G_e_0Mk1gE0PCPIEA0KPQEZRH6Jcmv7Q24iq_NLB6tZ0Uk3sbF4gveUqUawrE1VXS7d33rKE1UaZX0UYAXnDtDus8r_1SwkdSKbiVZsLf7PpcAKsj3771YlPVRE9xDwA1rsQAumj-mtdjxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇿
🇨🇭
ترکیب رسمی الجزایر و سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/Futball180TV/97804" target="_blank">📅 05:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97803">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0YPBYX1FonTxNTSXNfdpitKVE8CteIsj20bDJXDd99QYpTn4ZsgNic283REzRPzjI4ZqrkMKu5jyomKaJjcD6uDNIzAyLgGICZns7CIRmjliHOrmNIGyRdzhmApnM5mdH1Mi714JaqlvgnAyxb5Zq7HlRA97ZUc0VyPhrX_MgUcz26JCu1GN1usL4wkj1C841Gs8BHLGXDRYXyx8ptY_BEltFS2a8zQO1ylEAkV_I4YOJ1bGUUlujeWUhX4Y7OJSxPOhAN2aI4c4zXJqrHxrBzk8Tn1eR8IPXiAbf-AL-x83L4LfvmJPRaDm9gjdU-UAQO0ZSGNLCdtCEly8XWPEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🎙️
اسطوره کریستیانو
🇵🇹
:
🇧🇷
‏همیشه احساس خاصی دارم وقتی درباره برزیل صحبت می‌کنم. ‏من خانواده‌ای در برزیل دارم و مردم برزیل را خیلی دوست دارم. ‏چون آن‌ها همیشه در طول سال‌های حرفه‌ام از من حمایت کرده‌اند. ‏می‌خواهم به همه آن‌ها بوسه بفرستم
😘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/Futball180TV/97803" target="_blank">📅 05:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97802">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLPwxi3Fhq-cpQFhV-XoMJGmmJgd-rETZcHaRgtn_Dw1qeFdC7sQQ6BLOmBzjxzBMMKZqFaCn4nCHQLkOnp-Ns_RbEEhpa68sqPHXyrPcS9WdIowBsiB5FaGK8qL7Sw2fD97CYMiD3P4FOVwiNO_JLjjOORXPv33Wl_6m81djrgHsyn9IKPpzuZGIVjFGklmVAslwIL-myjAX6J1eiqkG174eyqUDxb0V1r3CbQdWjFceyv_OPrwrP5xg5I4xrF4cnm9wGkb5b-1PUDiQlg9YSRQHKdqJVYzWvi1Z6NtvZiYsPVsgnAdj5apvoSddWFpFh-3lwp2tZHObRYMxS74sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🚨
🇵🇹
#فکت
؛
گونزالو راموس به طور متوسط هر 47 دقیقه یک گل به ثمر می‌رساند. او 4 گل در 187 دقیقه بازی در جام جهانی به ثمر رسانده است و این بهترین آمار گلزنی تاریخ پرتغال در این مسابقات است.
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/Futball180TV/97802" target="_blank">📅 05:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97801">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qip5di9OzCm-6F9R8J-erxymhhh-ClOZZNMKMHt9SRWNfb_vWFf_J_i0Bq7Cso9Yc_J5i7vtz8rUKHBf0P22cWSjBqM9_xcncqWgTrcw2qflG5RbXe2Jbjs2ZNdAA0Upp9NC5VwGN0ro4vj-V-msKI9c4r14B8MqUxfGAU3eVAcEy8Sw460Gl0iP3ReHywGgdJ_2KEKB6MvIaYWi0EjGYR7X6k8jd8UPqCeZSemOFAimY_sCNOxp-5WVHh8gqzSiXijtbs5Qxgc6B4h4z9FBGTF_JcXyuScUl78u0TM58vfU1vzH1SJCLMWBaMZf2F5iNCRkxNXZDv41Ij0VhC0i5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشک های کریستیانو رونالدو بعد دیدن تصاویری از ژوتا
♟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/Futball180TV/97801" target="_blank">📅 05:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97800">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👀
آخرین تقابل اسپانیا
🆚
پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/Futball180TV/97800" target="_blank">📅 05:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97797">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PElYiG7YAxl_v9Y8hg2gueMdnKOnFWYMPdYZ4JlIdkQ_OUimrK8b5E6aXpDpAEHYeBdVuF-F0tnI62Moan91V2XOeBywL-vhLr4-TYqlwMv1DHKxKgGyIDnb4hkpWJDdF3eRhakbsuqqfPJEwUvtPkBgS1c36E-hslLsA7DyLuuDF3nhmpxRfEXTAdh-zYJ6EdeaVzIxOstuo9_wFxiKCzd_lnWC_V2LgOy4qeHjwUcFNUyiUQ8TJh9cBoL4RbO0T69eSSqoWX1bv0Vu2thMrQJ4F61Xhi6xcpXCHP_C_AOwFG0yKdZVW46OXXfgv_Lo6A0j2PSADU373ZP0GmTWPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BGXJrksF47jt9zJK0nxX9YnADcgyTpLaY-sIc29I8xz-pjpcBab3iXR_UJF1sEFghKuKcSv0n792yFGZ7dkYOHUGu_eXmhtKhm6AFY6KifhTGzcf3CWct3EZdqC4lLoAf_DMprm-qPMBM2yMpAOZSEnxj-mKzx22cSPTSMlbkDogZrDLwdo-S4hakntRP63ZuO2Ae-B791T7W2xOU7bGGS8d0W1c1oNeXu3I16GdRCN3YHnj3Fw9ujBirHZHN1ANdJGEP1z20gN3qPV1IHhqWlRCwK7co8g3YUw5EW_5zbunnQI9sezZ71ipoGm_Mldcu2mFFPJk5DWqE4U35cjvmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به افتخار دیگو ژوتا.
🇵🇹
🇵🇹
🇵🇹
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/Futball180TV/97797" target="_blank">📅 05:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97795">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3MNt7lsx0no2a9loJMmxG5hbP_tqEXGNkuGcbccK3bJQ_qI68FUVH8XMd3jJmBvaD3OOubrgMjh4bG4k7IOvEnEBPV1ZA8BMGls0LD-0CO5_IJ_3eY-6ojXRjxdrUcNmPBnxh-d60KQEwKL48ncuwXfrCiACec32kzRdWX1Rk9V0OknYs-uDomIeUA3NLixmiJCz9ZYvqjjQMZYwNIUzLPTXto_kjPGsEVb-fvjOOCR09qrQoldGhb4MDu4YUQ-galewKzTYSoe45JYrAgKx0MW6riTwueGf7bYrmuWsyr2p7i3_xsTUxvsCVFxNh9lzJWEpDHmIL7c57oBEMEQ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اون عکسا که دوس دارید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/Futball180TV/97795" target="_blank">📅 05:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97793">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZVwiAVGDWb-EJI2jDy0p5p_pgYTWGGRA96gP9TY8U-nbh65tR5-XkaIuskn52bhUzGzHYQba5JlLZeLPGm81golMeByJbiZksLE8VoUe-L2luaxX_ZLQ9cja8e_YY30LMUWJCesv6FHUK_u323zRScRskhqvv91PM-uIMkUg7qpjzTB3gWkJEp5l55UXZwuC-hwp0xwdXP9ksxkcDuAjaJthjOV-xbAwviG1UiOliMsb2NxlpoeBBXYAngUwI_csIQlX_if_WqI8IGFjRYgiZcRv2c2sh5CcF4S3Eq0Z00k2JGRWq3AiDMbnLDBKni1PC5nEmKoeJiIHIqsgYz3jEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GfGEpJKVrc7E24q4jj1oXReFsD8O9RXOxu2Xyez3aWShbjAH6BdcBZRizGMgyfN3ZDt8_leYAgbRRojZ_QFh_ZTEJtixxQSx1eS5GGEYKfze6sXi-RCAKhnA5cECXVzbTWOS-dA04ivHk9b21B53RNd62VVlvEPx3nmDCTkHJeji7p1MsZZqG3_R0BG_p9FrBE20KBEM6m8PptBSl0b2Y_0AN0D56ZZGOhZQIYRe8W0y6W4G5Wk_6cBbM2io0nREUD5D4ix-B1O44N6MACYijO0h4dmQZzy8OJXBRwBv2vAiCKZ07JnUNPvkwdMI_B0VCA3Rf7KeqS4doqqvWp6dVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تقابل دوباره و این بار در جام جهانی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/Futball180TV/97793" target="_blank">📅 05:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97791">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWCpHriRU_L_Xb0Y5xiwW4iVNRh1iUX5Kt-9z7wQKCbDHR7MkOrNuLFtmArUxLPbiDMPWPIoMF5BxSxKgQ2cezRhPYepq9c54R-HRp0hUdikBde-MWEgZgIgRZTeleowIEs7N3bHioCbqPHRBpT_IDgWM3Dw3efNuiiYewzJxReJS0TQQ5iylJDaFC2QTkUKVa5oXJKT-ONC8IBE4CL-r3Vkl983LlcGFWvDM1Zi-7DnK8TTsPbgvUcu14fDyLaffYyPDj9QpozjNDXNP0TTBSPKIZ_CMjRborGtpMawqULHDxXP5Rm5nKZk8RbeNvQY8F5Ow-QOochA0gyFfqxy8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
آخرین تقابل اسپانیا
🆚
پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/Futball180TV/97791" target="_blank">📅 04:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97790">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hqQvXDm1B3PzZndhOJSoc_CdGCeKVNogc0PIeugYcxGMos3ytnpNwdgkosx6sMz3wzarDaFQB8DZ6Rsn7zBYaq-nGLKa2NMIgCvqn4BF1JEMKcq75K7D8WHmj89DfzF2oHccMe3WNI0UFKvt__GilbmAkHARVnrYAFRWDVdwyfcZVyIE1C8TiLXnbsCutYWgac7vNLHDSNuZ4jntFkzzC5fl-us2es05Zyt8AcX48i08saUXNza813V7OxLoqkn2YrTYKsDzSU4s9hlnU9WB1OwSpeUaSAEG244w51YllqSqK6JXk4KkTwFKfUY3-Lp7fWo2iJaN0nGZ-D7zdmNJZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مارتینز کسمغز امشب هم با هزارتا مکافات و کسکشی تونست ببره ولی در نهایت این سبک بازی محکوم به شکست مقابل تیم‌های قدرتمند تر از جمله اسپانیا و فرانسه و حتی مراکش خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/Futball180TV/97790" target="_blank">📅 04:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97789">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqy8fWWbwVAQxeJM8ycXrO-9MsBjl3BMtawlpi18fUGG4yTXgXTTJPOy4YmrlKw5G1DsmU-KUZ7OoZQS2vFaMm0gUzsv6ULP7KOHyLr_LZEc0PuFPAmEP792Ajm02bYAX4wZCv7u_HzCVka0dWCVkheb17UimNiIN68-NtjZh7ro3EaeQmsgsryt8GUP-8k0Ru1VmtzR8lFGhhYO8e-I8AYN_rzeMvrVwq9JqrZ3M3QmqB2lY5lrenGBjQzgocDrtw14Y_ZO8i2GhWCycHTYP3F9jV11V1qy7eF9szJAMU5HPIF4u9uWvNDffFk1YVX4h7_Eas7mNFeHq3CwRXWZFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇵🇹
• کریستیانو، اسطوره فوتبال، اولین بازیکنی در تاریخ شد که در مجموع مسابقات جام جهانی و یورو، 25 گل یا بیشتر به ثمر رسانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/Futball180TV/97789" target="_blank">📅 04:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97788">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWh8ieVnQQhD6nRwqbVEXRJ9KUE4xwJ7twfzpXiufXboK25zVjbENl6d5oatZ9d2gmPWBEZPlIzYMiaxdHpNKAUTsZTWVuoiRwP_46ArBiVv1n9kYgH-BUpYNuuBEawvRuTcrfRYrcEDnXzEMdRT61k8PnDVSgaHTM_HXIa7-qoXS6YlEaYfguxgGuPiQxcLNHQ9xn0GyjN6fwR8CWpSR5IC21rXsqdHP6XwzU8732-6X2eql9iB7n_-P6szDzoe9FXxnINHEXif55Yy4YoHJCwIyT9iUcCBQfF4EvDExh647nv8XH5NEB5FHKNf9XFclgD6wI2N0dAM9BUHYiqjfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مرحله‌ ⅛نهایی جام‌جهانی فوتبال:
🇵🇹
پرتغال
🆚
اسپانیا
🇪🇸
🗓
دوشنبه 15 تیر ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/Futball180TV/97788" target="_blank">📅 04:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97787">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/li1jy8Ypt5GglHuHu7EPV5v70BJFqK8O6wBpdHMf4ScMaSq1LKwMyuZ0zsRt3615kTXVFwaCKt4nbEkKGpW3secZj64RsXziD-16jOUDyzpHpWl8v3kxJgYA6-qWre7QEpTyGgVTusRrs9qU1HD8eW1KOH9qzCnOhQqANOac48-Byu7JUIeyfQJ3n8lZWf7kc57gBctYILr-gxs3x4VzdhQoVsmtQ9B4pq-g0yrsiUDsdW2bCh5Tgw9EngNGc82HxFHGFVLDQj9MIkd08zspnEQLZR3anr7fK54mBIQ3lbVZqGK_fI1yzQOKs79T8NsM-08-HMFB4A3hQ3B0RvRwaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ مهاجم جدید میلان نسخه مودریچ و دوران حضورش در جام‌جهانی را پیچید؛ فرشته نجات پرتغالی‌ها بازهم گونزالو راموس شد
🇵🇹
پرتغال
😀
😃
کرواسی
🇭🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/Futball180TV/97787" target="_blank">📅 04:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97786">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqwR9o31U6uWX0Nhcqq1dFvKHmV8Uhs5ax8iQ2I0tubaheZvp41jdD0MWH9FgaeaVt5-47IKbDEWy_-6ETIocsTY4PaaeKduPxcgAUI7DfZmoRR73JQOmrlslM8WcjPU0Bnytj1AMvSD9g_8OoG_MprwC-Qq9wQpElWVeo04Fre_xFSEbLv9057uJrvQjR9OVlfNo4M4XtIcmPpPJWOWCnvZ6G8PxlcZNi9-Eq3qQRrI-QhSiaKT3INILSI-HI_Cz6yMKnam8MuWdIo0bSQUD5OuerqI_8DZNtApW8NFQZBIYKM-C87_5FOomV_zjJj7DGAPYjwkVexTb4-8kNNZzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار مرحله حذفی جام جهانی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/Futball180TV/97786" target="_blank">📅 04:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97785">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAS2XVSdqQ-6wXPTX_AcURP7xAeL3SJUbVTbhRi5D4JVQPz1kvgEoRFpXBoxqGOQnRDWUPOAevku7F0BbbOZavSVTjkgtuwwM5rmo0XVoYKeyp-GUjnpFh9xrRQjY3eGwYHi2Yz_QgeOwhG009hZvhfXJ3GhGvgNl8VAyrTQMM20SkRvmsqFw8JJ_e94xP4f07LpxeWpMMJX1qQw5CJ3q5dLzg7ooh_aHyfnObLKLemYoJO9Gf8CDcLZ8FdJpWH-QUQv6Iv_Mjop6peLO-sE8OEBPPwouTVUkpCY3aqmCbYZMX2kAb4rCIFV7Om5t6TMq-VWChZWoudrgMLIvmXBUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ مهاجم جدید میلان نسخه مودریچ و دوران حضورش در جام‌جهانی را پیچید؛ فرشته نجات پرتغالی‌ها بازهم گونزالو راموس شد
🇵🇹
پرتغال
😀
😃
کرواسی
🇭🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/Futball180TV/97785" target="_blank">📅 04:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97784">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHFseliwTbn_fsSq_fE6exdC5GgU8-ndg8dyhwuExsfIZXzvCc2KgWe1SXRCA1xFSCEEGJj4q8WuB4Ihdu-cQWVQAk4hDTTcS8vtcBaDrPGVlHmLlRol_BgYJk9LK5F_nBoE7qFPEqvgAaCqIREULX2x0grSp-nLuwx2sbCfTnaS1hpfGnobsXfJdxcTggvPNI6NOpRT8F20yX8HBtF9BBnVI-H2Td63rfL7Pk3UogL7Udv8RPp-MLIr7t90xLS9sD_eDGQmhZFq4pGTSOh1AV3X8iEmvmxy5br3g1iPv7jXTVeNLFlL9HFJr-HeDwYkLa3r3XCY3tnWk8wQcNLQmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ مهاجم جدید میلان نسخه مودریچ و دوران حضورش در جام‌جهانی را پیچید؛ فرشته نجات پرتغالی‌ها بازهم گونزالو راموس شد
🇵🇹
پرتغال
😀
😃
کرواسی
🇭🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/Futball180TV/97784" target="_blank">📅 04:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97783">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تبانی اصلی اییییینه
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/Futball180TV/97783" target="_blank">📅 04:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97782">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">تبانی اصلی اییییینه
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/Futball180TV/97782" target="_blank">📅 04:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97781">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7xSEc17Lyxwqrd_5e7y0DCEDMpRStGO_YRKs9Uv3nhynbMHTt4GNYsxu1PHegb_viiy3Y0XjveMXKK3GsrZkbyfgB-UT0NPPjGBqKodSkZWKBBg1ZE1CqU0MeyZjkykq5U7N13JPBf-odIeIQ7IKMscdVNG4RcFYpyRvHPSQp4Qy9rZEYjxXAfZE63WynWTK9biu4dvhcdM2ONKxB_wKqjhLAraSCQXewwphg6AevEDGLc7_wvnN1FG6kamDMxd1RYFOY0fkWtB6XWKJ_lwLU3UJxiny1MLID8Z2ASa-UTAcuNjtJHQN7Y7Jpj0A2hu2HZPvo3RQyaNL5gtFSm8Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ مهاجم جدید میلان نسخه مودریچ و دوران حضورش در جام‌جهانی را پیچید؛ فرشته نجات پرتغالی‌ها بازهم گونزالو راموس شد
🇵🇹
پرتغال
😀
😃
کرواسی
🇭🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/Futball180TV/97781" target="_blank">📅 04:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97780">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owRqAAT8KXlXrsDkGiCefsOdYeYv6VgO40_YZLPnIwN0mLpZ86Btu8TXCqiEuScrycULd5_V9WXfL5Imv9GXCPnvGmY3X9L-JgwmFpGuMMzUgb-EmXqxxMSPfKHCVnd7cbZezuPwtOuLCPDfbcrBz3vmx5LiCDY3jhoGyTLmTeuGJ_OOPjbiDi-HAoy8NbYADC--3JGizY_omYtUcIXZF4AUZ-L4iEjWiReuM7X3_993odJeh1AsjIsD0K3ID_sdPyNxTQtKSY1NaOhx77tYuK0KySB2HE8JR18yQA-iUW444ZLm53_9u8uq63DHIR45dwSVKw5uiag0AHVTvaWGfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درد دل با کس نگفتم درد من گفتن نداشت
خنده بر لب میزنم، هرچند خندیدن نداشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/Futball180TV/97780" target="_blank">📅 04:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97779">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">رونالدو باز خندید
🤣
🤣</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/Futball180TV/97779" target="_blank">📅 04:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97778">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">از کووووون آوردددددد
😐
😐
😐</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/Futball180TV/97778" target="_blank">📅 04:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97777">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گل ردددددد شددددددد</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/Futball180TV/97777" target="_blank">📅 04:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97776">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رفت خودش ببینه</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/Futball180TV/97776" target="_blank">📅 04:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97775">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4x72aV7c0YRq98chBbKlTl0k2Xpg_YPrsmsot3Kzss_nXJtcnPzGQUuKSNfAUqTbRWKCq9dfzhyXBvZBZyh7tIoFv2NUFV4Z0TiGLyJxVI6P0tvhoEaqSFNHOpPek-5oGcXpuJ3H5eXD-sD5CcsabNRV8irtZToyRx2D5412T6m14lyuL_qkPFR0NtBWujT62WzG4llhjTUtD1Mx8g6aIf3mneDCOhV92C1J_obyY--bQa1ZwBH-cS7OurfsA5wRNEMaTDx_zsL5O2Oo1yWD-8zkm34DR1TbKdaMP7KlWf3HySY5_VK7GA_R3gHh9IJefp2bt7m4_sn1mqe5BQICQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/Futball180TV/97775" target="_blank">📅 04:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97774">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">صحنه رفته واررررر</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/Futball180TV/97774" target="_blank">📅 04:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97773">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">رونالدو ریده به خودش کلش کیریه</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/Futball180TV/97773" target="_blank">📅 04:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97772">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">صحنه رفته وار</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/Futball180TV/97772" target="_blank">📅 04:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97771">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvCv9KV_T-VAGzF8EQoLJ5yX6MpJu7ZuRd5bssWKFn8fotKkUHdYl9L6nUJb-7jO8S3vfOJDHWWt0dLU9vOFL1TVNuGxiHubE7pcWhcJOLF3zoLF_fL7xO41jxHCRzsCReDfZv3Oso-sR-4XlxtAKoX4w6W-39_vyPD64hI9w2OONr-nxV8FiYXl23h3fcSjEGF4sO9old2T5qyB_YBezAhOqmylH8i1eVd5aLYuGIaLCQU9tU0KJUOWI4sdE4kNKcjIZxySX9JVCETsPnC0uJ5gq4-qakyg_bQ8yF0AFiRibmAmSiZ8hnniN1t2v3MsmsiDWzp4qwoJG9nvWrw2rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه اوه رونالدو رو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/Futball180TV/97771" target="_blank">📅 04:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97770">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">احتمال آفسایدددددد</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/Futball180TV/97770" target="_blank">📅 04:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97769">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وای وای وای چه بازی شددددددد
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/Futball180TV/97769" target="_blank">📅 04:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97768">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">چیه این فوتبال</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/Futball180TV/97768" target="_blank">📅 04:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97767">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">یا خدااااااا
😐
😐</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/Futball180TV/97767" target="_blank">📅 04:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97766">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کرواااااااسیییی
😐
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/97766" target="_blank">📅 04:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97765">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مساویووووووو زدددددددد</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/Futball180TV/97765" target="_blank">📅 04:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97764">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گلگلگگلگلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/Futball180TV/97764" target="_blank">📅 04:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97761">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/06d72aaac6.mp4?token=Z1HLbQFn-cXt6LmCqo8bGV4Ouxp1T5uLAKNSuX_NQ0C4AEOEACAMioFM1CJg4_9izN6jR5J9HnRnFdvkOnbvL-kGU30e34Rw1-rLKfmQpgCL1OAZ8PPG_rXX3i_7Jzf-38_AA9g7eVk9KYOGsQHRSrPXu9OYEDhhs--uxXGULxN3Dw-iJzBDsHvI3vfBERJ4SeI99nU5SFEPDkQrs-M1js-MI4zSjocaSgm6AM0EE_CiyAvk0tLuLV-TtiV9uq04SaNBEYCCy6ErL9wFHTqQDGw9RknRxKOXBYlAMg23vVTEjOouUcUslGlfbYSFe5gwKS9l4y6ozFjr2umsKS8Nwoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/06d72aaac6.mp4?token=Z1HLbQFn-cXt6LmCqo8bGV4Ouxp1T5uLAKNSuX_NQ0C4AEOEACAMioFM1CJg4_9izN6jR5J9HnRnFdvkOnbvL-kGU30e34Rw1-rLKfmQpgCL1OAZ8PPG_rXX3i_7Jzf-38_AA9g7eVk9KYOGsQHRSrPXu9OYEDhhs--uxXGULxN3Dw-iJzBDsHvI3vfBERJ4SeI99nU5SFEPDkQrs-M1js-MI4zSjocaSgm6AM0EE_CiyAvk0tLuLV-TtiV9uq04SaNBEYCCy6ErL9wFHTqQDGw9RknRxKOXBYlAMg23vVTEjOouUcUslGlfbYSFe5gwKS9l4y6ozFjr2umsKS8Nwoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل‌برتری پرتغال توسط گونزالو راموس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/Futball180TV/97761" target="_blank">📅 04:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97760">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vh1riLepf69huk84P84iQOHYPjcCfIfRd53TpBOfhcug0NPrSHsXUD2pDeyR56eV7PWA7Gm2H1N1VFuJGHdY_DXRn3LoEDIAyQa5Cg_Y2DGjtjQyMo64CE3Grx44qQ_eQ2CSb7sFAmw4uNwsLE97gmOCiwAmmKNmy7Me7sO9gGJcz3ydbNcjh8BNfF1BCvUVR7fpkG3a47zBGoELjlkKUYLFuhL_wflcmfc88ncU6I_DxTI-ffiGYhudHbB9ZR1uHCpa-EOzH5KnVqRf5ZPpPwALzo9Xv03VTm5ROXr7bBNZ0Tp65PDi4kXo_p0GgOBL0wq2pTFkByhyWw38ZUvsIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇵🇹
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/Futball180TV/97760" target="_blank">📅 04:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97759">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">همکاری مهاجمان میلان
🔥
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/Futball180TV/97759" target="_blank">📅 04:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97758">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دقیقه 94</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/Futball180TV/97758" target="_blank">📅 04:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97757">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">چه دقیقه‌اییییییی اللللللللهههههههههه</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/Futball180TV/97757" target="_blank">📅 04:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97756">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پشمامممممممممممم</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/Futball180TV/97756" target="_blank">📅 04:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97755">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گونزالوووووووو رامو‌وووووووس
😐
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/Futball180TV/97755" target="_blank">📅 04:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97754">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پرتغااااااال</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/Futball180TV/97754" target="_blank">📅 04:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97753">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گلگلگلگلگلگلگاگاگگاگاگا</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/Futball180TV/97753" target="_blank">📅 04:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97752">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">داور کم لطفی نکرد ۱۰ دقیقه وقت اضافه گرفت</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/Futball180TV/97752" target="_blank">📅 04:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97750">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/849a19bd98.mp4?token=ki43fv4JyURtjJj1FKKTIiUjBrwMjDaoknJ7Kr3YlFzpkQ3DDxn8yOxqQx5NSIHQfvQnNTgtO_VKYF54Cy0m-TStSXBFqyE3kKSL_cnHxEsBPP9ozQrCf-_9vb-a8mAp37MRLr4OU4l0WCOsrOoMjHK9ISQKdH_9iTeTM4qg2rLSKYj1fItTxs8RfgjPB23RH3bGqOc7KfhsLq38eYQ6OwPbJIIY-agcE1dmFddZB3D4t9uzHBg5v7MO2ie4YvLgzN5DAK75cAGED6QJS7Rf0evMnWQHRSwhtGGbde9QWVKvEv-ASV2DJ7wtEbO-dkBPM2jMeZNzuVv_kgyYM0rGDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/849a19bd98.mp4?token=ki43fv4JyURtjJj1FKKTIiUjBrwMjDaoknJ7Kr3YlFzpkQ3DDxn8yOxqQx5NSIHQfvQnNTgtO_VKYF54Cy0m-TStSXBFqyE3kKSL_cnHxEsBPP9ozQrCf-_9vb-a8mAp37MRLr4OU4l0WCOsrOoMjHK9ISQKdH_9iTeTM4qg2rLSKYj1fItTxs8RfgjPB23RH3bGqOc7KfhsLq38eYQ6OwPbJIIY-agcE1dmFddZB3D4t9uzHBg5v7MO2ie4YvLgzN5DAK75cAGED6QJS7Rf0evMnWQHRSwhtGGbde9QWVKvEv-ASV2DJ7wtEbO-dkBPM2jMeZNzuVv_kgyYM0rGDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسم الله گفتن رونالدو قبل از ضربه ایستگاهی و پنالتیش
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/Futball180TV/97750" target="_blank">📅 04:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97749">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSqXUXe4mJ6dT43V7vqq0ps_p_zWA88bAOnksLTVHUiJg76WJTFyO2OQ0JrXKDzS2AIXUoJiTKwQ5IpSFLPfZNfuRt9RzNcniuB_-4QV1sGqC4rmJSUwAFhcXjDTAcf5s3HtKXH6WaekcB8OYH0xwy5Zvv8_MuKTGrVSlpUKi8DYJdBY_29fqd0C59SpflOhJH0kMiqSZH2M7uJ8CNhz4LnZBOFrv3J2F9QzDiHuY9rFm_d7oLcYEMl-sMj-TAweokDFCZc387cOKWNhPe-IAsvSHIy1m2Yb9-lhAOrlTCUmmV_feQ6g3SlBuimM8sOwDw82P49gknc8HM3qtLhNtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین قاب از رونالدو تو جام جهانی؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/Futball180TV/97749" target="_blank">📅 04:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97748">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">رونالدو حسابی کلش کیریه از تعویض</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/Futball180TV/97748" target="_blank">📅 04:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97747">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
رونالدو رو کشید بیرون</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/Futball180TV/97747" target="_blank">📅 04:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97746">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">برگردید آفساید شد</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/Futball180TV/97746" target="_blank">📅 04:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97745">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دومی کرواسیییی</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/Futball180TV/97745" target="_blank">📅 04:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97744">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گلللللللللللللللللل</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/Futball180TV/97744" target="_blank">📅 04:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97743">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdiMLLRSqCM6pSWtRVJfEoxAGa0hyJhpBJmvsLGQ15T3v9BJzToUtYfiEMFw5EpvEpD91xWT_4DCAzOZHOeIlheZs7pUKOdOp2PgYV1M3mLFQxvNzb7qjTBVvjNHFvpZ__Q-JvmpY8DrvdARuzWCeCQCiQseR_MBPUBRm05nCJiajCnyJSJ6PQCLYfrX8SNdm4s1wN8iXfAwlR8QJ6LX8cs90OkKJIbN4bmBIp1NC-xBAcBjBm1VUOVnDb2uR0Hxr8gpkN1HXA0f9R9RrL5PVk1Ddj7YS86grkCAiy20i2N3yNvYeRuUvJFc7OM5NU_VpYeTsJZQOecApoUQkvrmAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به، هوادارای کرواسی رو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/Futball180TV/97743" target="_blank">📅 04:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97742">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کرواسی تیر زد</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/Futball180TV/97742" target="_blank">📅 04:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97741">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پشماممممم چه خبره</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/Futball180TV/97741" target="_blank">📅 04:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97740">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPvO8tnWYO0mGq99c0piRnXuqY4WaLm1wCV9DC-cwE18bEDyNfTy7ruA4R1yXgc46Lz8Zq0p4EWBceUMd4zwh0W675GhEyoSDHbImsLWub8QDnM0ftu_CN0DkLDPA3e-cKx5DPwD_tVJWAyS0rEMTva0Vk5nj3f4uIUvUMqawZeCXrUtFo-_oEfCExcrmR-YrQfX7nRdUTluDed-z_eluWO_km2Cuq4e6sq_IqV1TOJYruZxlnLj1m4DOflil9FTvRv6KcdNUvCYNUwtRc4OO2SLjdcEzjZRhdj9rKrTBZQ1IYDAcrL0_cQhmWHZmM1ilMiyu1qKMbwRnCruolyg5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریکم اومده استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/Futball180TV/97740" target="_blank">📅 04:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97739">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00963d39c6.mp4?token=H5CVm9w_NrkalVTzwxM0qrOe1O8_LGaXZi2tcXlaYcGWH0cOG35G6OlgooaLOS8j6JtunbrY6Be0zoDd02hwhnhgItf1Hmlzr-ct92brntPaPX1CVjsYgEajMkMBiwiEXS2zmb3Lmo0ErD_-O8vAkSOzkI6Rx1R2RgrFZTNXyTqVRHR3GHpC3JpE5rzWUt0d5LedI2UJ8D9L9-VUPLastMnvzVJJZ_5f1YS-57ioJ1u8w5LWMmoZQQeiWCpbKEPpZnHdOsZUHy2V5jetJnfb93vZzsv5OD7tdbOC_RBVEpmVPfeI_wGswa88gSema0xoe7oW7KAS9zNr5qSMuAB_1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00963d39c6.mp4?token=H5CVm9w_NrkalVTzwxM0qrOe1O8_LGaXZi2tcXlaYcGWH0cOG35G6OlgooaLOS8j6JtunbrY6Be0zoDd02hwhnhgItf1Hmlzr-ct92brntPaPX1CVjsYgEajMkMBiwiEXS2zmb3Lmo0ErD_-O8vAkSOzkI6Rx1R2RgrFZTNXyTqVRHR3GHpC3JpE5rzWUt0d5LedI2UJ8D9L9-VUPLastMnvzVJJZ_5f1YS-57ioJ1u8w5LWMmoZQQeiWCpbKEPpZnHdOsZUHy2V5jetJnfb93vZzsv5OD7tdbOC_RBVEpmVPfeI_wGswa88gSema0xoe7oW7KAS9zNr5qSMuAB_1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اسطوره به کرواسی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/Futball180TV/97739" target="_blank">📅 04:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97736">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D8OdCi3DgGTUqWhbghrN2LBlT4QOyKkXiVzQ8iwy_j5cOGWfwcDXNss-IrqbqdVkEiXh0dTS0I0apbczntSBHl5wFo-4y97Wvu7OmEdxzV-Or9Bnc8HoE-3P4pf5_fDZs6UDpnamJvhAqGSzOGDOTQ5friwtLMmOzfQ8Hc3JgrH8ebNRsJx6Or6fow6NnS63B0ZGeYhB3M1E9SuIRS4q_VCz34up1s_jcsCvPxDoC2EOEJdFLyeA2AkdcDASdRD1sNfHtoyQ7XzI8XiEE8tOl_hv23IBz12AdRPGl05Y43jQsTKXstkjCiOZVoGGZMufqs3NXNCHdgNxEVxF9cdyoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ji7g8iwOBea_du9S5JOBuXpDv8mFxB56_x5Z5FQA7RfLWRlHiglOFIezsCJKheB8kYW89Gr9HBQqYf2_FjPGAm_5Qwa4mVgi-sWOIYYcvfJqatj2r4_98n_-tvNtwJpaXzpckr1yhxSxKSYhDCEDHjy6H7mRCZSy1yvu0O6lrWsRmJy0nzOI5O_Z2E__WJlw4ASuMcThJdFxbYhK0Ckk6B3IRgb95JkyWbaZE0xeu7MJ_3-pxDzVxL2anDIuGtyrGyQkGghifawaE9sOImeRW8nMgJ6ipYxG_Z1gXmgnkYTKOPQuLZFdMZdwSq4tNui2C3-32G0agS0y8ytNs5CLhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IKtMj-ffyQYYlePknLCw-70wt_Fd_cpQ-sOnIbUsVjSwSgyhCXURqwSM5KAFEp71opA09jK50TGExCgNsXWbKLE_dimzdc7YxQI0wkY2kztTk4YoRuOaV2FIM5HcNEkNWLOtPm0FQxcZk4ED4PMHdeCgF-9p2WDWnNAZ10W40a-eXMwNr9KAWGAmKqVhdwx3ahb1j5YAEk6WbKDkoSryFlM8ZOW_76pvaZ0xwUlyfI6L8TrkK7iJ_sdgaEEET4zaYYMES4DoOllQpEpIkHvHTgpr-JAzH6tjI0DS8QqHtfc0WzhnZKjzg2WZ7JmctK3flQfCxVaNq9YDeXohKq0f1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از ته دل
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/Futball180TV/97736" target="_blank">📅 04:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97735">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsooF9MNWwZIR0MQSPK_JKtFM_i8TLsiATjjYtWZkeM16lnl8-5q-qj-95QglS2AOBU9D15wqhVR2TcCmuT2k8QzyrV6Tut3l-IjnnwDWZha1jPIJPvqd6lIgi1M4LFXbU5XwQFeJBwG3K-fCZCLSrVKbX54e8m1fkRIE_tHxyFK4H7YTQLvZQTtVGA9vbPMg0g271uEdVjFw-7O4s3yGacHkG_ovyKVrZIVQReqRgKf-3W8HTYBXzjSUaHbFZoiM4jy951GnzkkwYDJBQI4uf5SLUTffDnWjda2N-VkIj1SJ5h0FpTV2BeH6P1_FyGBnEYkN_gcheoJEIoeqUQUvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو، اولین گل خود را در مرحله حذفی جام جهانی به ثمر رساند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/Futball180TV/97735" target="_blank">📅 03:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97734">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">بالاخره زد
🔥</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/Futball180TV/97734" target="_blank">📅 03:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97733">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رونالدد</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/Futball180TV/97733" target="_blank">📅 03:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97732">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گلللللللللللل مساوی</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/Futball180TV/97732" target="_blank">📅 03:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97731">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">رد شد
❌</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/Futball180TV/97731" target="_blank">📅 03:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97730">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jM2RIYM1Z2bsi--sD2lrv3btxatuIdJNbG0EnBUtvEMUcMP8jxGpTZKEnK5IfDTVrQOZDPakvXmdlFwQDcYl70M7F1cwWcZDGXhQj-qJ2EVkgnovdid4xCD1ig0ho6fqZY2N0SyhJAXCO95d3vWeWpOxXuAWrU69-k4uQkKaqu6RK4rZYGEbSFvz-TY13zJ2ZbG0PyOPMwbtJHkT8h2f6T16i1nBH-ExZHVNOKGCTx0votCfb0MHbWrEOBd7IIJQPuy_x07liAR7kP6oo_i5r4guqBJYDY7u8vFs3RZbrl3sDN-Ycsx5XqQI-FXwA7LX7nxSUk5An2h8xdnXZSyCdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/Futball180TV/97730" target="_blank">📅 03:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97729">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">داره چک میشه اوه اوه</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/Futball180TV/97729" target="_blank">📅 03:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97728">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بختتو کریس</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/Futball180TV/97728" target="_blank">📅 03:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97727">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رونالدو زد ولی آفسایدددددد</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/Futball180TV/97727" target="_blank">📅 03:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97726">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11e00d9024.mp4?token=gi22tBQjI3eWU9xrz6KtOIpzGf-y2-0d7wV1kjqI7aWJDAP_qORVHWZPGbx4D1O_zjUp25xMyK84O8Jb6uEJLOlPiXaeVtPrF3mhnQ_xePR6CcJJtGOanBPMG2M3yzJp0xS7yj854OFk6kfmJIBICBJEjFN-0MUHTIJsrkpCeAbQkqfgYQLcR1G8W-xqt0fBppuQuaNrjWbMmYo5b94jGN3t6iTqkne3_guHYBqd4G8q0aIrlwUN-5f0Ida3_vnaOwUx8whtaxLZJhAGtBG-Jg1cDdkreZ1pLE52QAnyjL682oszOn5vxNM_rm0AAu8cMpA1X4HkamTMSJ6vBILNng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11e00d9024.mp4?token=gi22tBQjI3eWU9xrz6KtOIpzGf-y2-0d7wV1kjqI7aWJDAP_qORVHWZPGbx4D1O_zjUp25xMyK84O8Jb6uEJLOlPiXaeVtPrF3mhnQ_xePR6CcJJtGOanBPMG2M3yzJp0xS7yj854OFk6kfmJIBICBJEjFN-0MUHTIJsrkpCeAbQkqfgYQLcR1G8W-xqt0fBppuQuaNrjWbMmYo5b94jGN3t6iTqkne3_guHYBqd4G8q0aIrlwUN-5f0Ida3_vnaOwUx8whtaxLZJhAGtBG-Jg1cDdkreZ1pLE52QAnyjL682oszOn5vxNM_rm0AAu8cMpA1X4HkamTMSJ6vBILNng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل پریشیچ به پرتغال
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/Futball180TV/97726" target="_blank">📅 03:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97725">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پشمام لیائوو تیرکککککک</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/Futball180TV/97725" target="_blank">📅 03:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97724">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">چیکار میکنه مارتینز</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/Futball180TV/97724" target="_blank">📅 03:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97723">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دومی اما آفساید
😐
😐
😐</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/Futball180TV/97723" target="_blank">📅 03:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97722">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پررریییشششیییچچچچچچ</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/Futball180TV/97722" target="_blank">📅 03:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97721">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گلللللل کررروووواسسسیییی</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/Futball180TV/97721" target="_blank">📅 03:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97720">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkvYvI0Qv7ALJ5CqcrQydzDsuA1EHUZcBELTEafwjFnHMnA9cDZjAzVxMKjAdivgHufh_vSkXmoe1EtmFlEYVawycGTf-pkFB3t59KMXnM2i24QRQQFl9ZC85fn8a_uHBlIcpdB40Qg6TmhGsXUfeJOBvxXT393gHNMhtW6gqEYpJ0ComZHOUS6_wMZJ6r90JPlOALpzlXRYIMPDcDM8839RAWa-OD9SNM2UsySAGA8pOgvCSGiPtQ7mgRdLfQ0yZZmNJqFVJsjUMOZeOxR22uXsKNhe7pYklnlTTmy2znkY4L96pfTS4PmXFhdbIiMnzFiElnrtwouTl5lT8j0fbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو هدف درستی رو برای شوتش انتخاب کرد
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/97720" target="_blank">📅 02:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97717">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ro3FsnLBIXLt_Yp6Q8342hJud7JNz22sFnqhNB_Tm5r-cpCMrNctsyXC5muhHIgOD8lyrcbVb94DiRZsEKlnRw-J1ttOORlYcsmFs85stTe6_Gmd144bK6NY-NOao7GaFZqJOyZeYeug2Iq2y62HvwAqDSAcTy1PMgz9Bg-U36LVlOnZAomvaYJbfqY3AScYC3WZe9OAJAAQtZO0JJ9H51c3yYkD73cXaWM4dNgsxukIJZBNTTKyNv6vLMLBkyH4e3y0iEBZt0XVmQNZajL-S1I9vHTpyqSfqVpjIS00_bhYVTXJaXEoSL6D2fM2CcE71mw0Ppos-boZqvBmBkMTaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e2dA-hEGaq-Ttw34PZ0KLsjonDYs1Zij-v9CIh9T6saZPCM0NvUC2zIDyj8gQS7u-i7dypnnpG2kPNzvFDRfEXnhVmGVItuirYFOjHsJaWRzTHCHUPAFvhgstDjp6QgN8JSEpRZyo5zNueYZb-E7qwo0JZQDfW93mk-K58PLwi905a_gFYzTjvACRcYfZtTFeniu8PWOrytQWFGJQ0r-dN9cq3_esvbTDXe5KvuIFsuHD_nZ9wSG8XaQOWR89oqvITLMHgBdgo3s-p7LkdhVR0t8JGZOErocPhmJu2iO1x4xWdMcwIiWXr7XvpL0s5_L8VLMahFa6HlMj2iyFiBPPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">The Last Dance
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/97717" target="_blank">📅 02:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97716">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf30b3eba6.mp4?token=KqJHIYTfMAzu5W_du4TkoegTVTCDLQV8tMu-4mGSbCE-E03yA1Rzhat7n4eAt4pi0TNr68lelc2ML4fVXRsbOpbgWzDUM66rWUh7dngjKez8XL_eGDIptYInqRXufOa488tq0uCdx7jEDecbNGx9FarLAPTUZEv5feoG94kVGaocLt8UQeyF7KEY3rxf56ytcL4kPTVEwtRnCmSrb8xFFgxF3fsc9vlLN2Z2c_5-J0jMg2nOXN2nCJlMTSf-QDXMUAgMg-rBda-Q7P_Vw7T94Lb26Myfy6EUJDnLFXDdVRcUvk0jQDi12jA-fhicGYSSuB5q3bm3esadphN3PBKIUjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf30b3eba6.mp4?token=KqJHIYTfMAzu5W_du4TkoegTVTCDLQV8tMu-4mGSbCE-E03yA1Rzhat7n4eAt4pi0TNr68lelc2ML4fVXRsbOpbgWzDUM66rWUh7dngjKez8XL_eGDIptYInqRXufOa488tq0uCdx7jEDecbNGx9FarLAPTUZEv5feoG94kVGaocLt8UQeyF7KEY3rxf56ytcL4kPTVEwtRnCmSrb8xFFgxF3fsc9vlLN2Z2c_5-J0jMg2nOXN2nCJlMTSf-QDXMUAgMg-rBda-Q7P_Vw7T94Lb26Myfy6EUJDnLFXDdVRcUvk0jQDi12jA-fhicGYSSuB5q3bm3esadphN3PBKIUjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک حمایت کوچیک از مردم مصیبت دیده ونزوئلا یا نادیده نگرفتن یک خبرنگار دارای معلولیت؛ هر کدوم رو در نظر بگیرید جود از این آزمون نیز سربلند عبور کرد
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/97716" target="_blank">📅 02:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97715">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کم کم بریم سراغ بازی
🔥</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/97715" target="_blank">📅 02:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97714">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQRFrUEk4UoJwF1T3DrOqvWKiq8bQO3DW5qmPWNdLlpfipZJFTJXtglPk3VLgQ1pFApSVbZpyfftAA14il81YxZbRE9fcNePVc2y1-wG_9IFoYnZE22TGZLvR8TR-HSwP9RM-6aPgJkaELJfz8YL-DSkzd_olbPqvg0ThzjQc9sFg6lvgdfoXegFtKb3WVqtVQ3OdMmFywKGm4ECupuHzM5lVJyT2msgdrKcfJ24T5B4WUqViS_TwDrF-XwaWzzYF4lk1ju2EVJfdy-rWgsdlelTKtGmPH4k2MMyhPXIZc8W9LUlbg14ZR5cLHs9nvumNPvj6HF_jSjSZvazJJPpbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستیانو رونالدو به مسن ترین بازیکن تاریخ تبدیل شد که تو مراحل حذفی‌ جام جهانی بازی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/97714" target="_blank">📅 02:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97713">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/97713" target="_blank">📅 02:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97712">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFuck Bet(cheGuevara)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uD1wsEhARGeFj0X_n10v7iooZ-jolC9KT2s8u4nBwDPbGfCIhn6bNyPKFL6vSsLgKkueWMeoSG5dwUL20_CUfzwKPmX0OMsZ8pdPTfPjQxVjnxPs2cOYyqeH4dnYLsTtpnKPkkIhFajlDMplaYzfVPgsMy_LLMdvkVb5qVwRx7r452JepuXb9TVdR5XigfyIPUifDhVJoQl5jMEvZzrJykQtM048KM2KWmi_rSOkUY8X1a5yo0-XrCxoSxiE7slmeGCuSBpr1OhqtpyKhR_0gEBOEE_T8r6p5R9vltcjbgeiogseczBpeoYb1tQ3vN2munu3ynmtmIPIGMV6e3KUoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/97712" target="_blank">📅 02:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97711">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🔴
⭕️
⭕️
⭕️
مارکا اسپانیا: دیگو ژوتا ستاره پرتغالی لیورپول ساعاتی پیش در سانحه رانندگی درگذشت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/97711" target="_blank">📅 01:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97710">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
😐
🤩
پیمان حدادی مدیرعامل پرسپولیس:
اگر قرار بود نام تیم گل‌گهر به آسیا معرفی بشه چرا تورنمنت برگزار کردید که تیم ما ببازه و تحقیر بشه؟ الان پاسخ آبروی رفته مارو کی میده؟ به آسیا شکایت کردیم و حق ما هست بریم لیگ‌قهرمانان!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/97710" target="_blank">📅 01:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97709">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e8bcd50e5.mp4?token=UODkvwS3mil9I9uRMB5sQkk3pcIaDzopH6v1QuC4sEKqx1mHoWYfX9Whmfrzll4N3z2TlArTswTX9pPXDaQ76P3cdHYOhwspdHS8oeuM6BlJLRtCg0l96E3lTjF2mOLhIaP66biHeSyEPexbisjq-uIP-C5slHn1aiV8X26kmFhYbj9CZkLlHJw04-7XZhhHCo9STwa94C0pXXeXi0vNWimRnw1_VfUO8UYeWVdmgqQEKXXkXjGKWzGmA-KgFpw9FSqsR0Q83tzM_DuzkckvqbyRhVuyRUeU9kSyqofTvt_Wp33baLUTzZ7WFlJAIOTLR0UhRDNMR3ZYt2atkfWRMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e8bcd50e5.mp4?token=UODkvwS3mil9I9uRMB5sQkk3pcIaDzopH6v1QuC4sEKqx1mHoWYfX9Whmfrzll4N3z2TlArTswTX9pPXDaQ76P3cdHYOhwspdHS8oeuM6BlJLRtCg0l96E3lTjF2mOLhIaP66biHeSyEPexbisjq-uIP-C5slHn1aiV8X26kmFhYbj9CZkLlHJw04-7XZhhHCo9STwa94C0pXXeXi0vNWimRnw1_VfUO8UYeWVdmgqQEKXXkXjGKWzGmA-KgFpw9FSqsR0Q83tzM_DuzkckvqbyRhVuyRUeU9kSyqofTvt_Wp33baLUTzZ7WFlJAIOTLR0UhRDNMR3ZYt2atkfWRMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
خواهر رونالدو:
رونالدو بعد جام جهانی از تیم ملی پرتغال خداحافظی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/97709" target="_blank">📅 01:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97708">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRgZa_S13M5CuIx7rnNY0n564qkMTNFmb2srhMW4gZFivd3EYYLqR0XAIhD60FsS5dSzOpj0m-DjJZZcOF0r9g33chDK_qGdaAcouu5DBiQofu3VMRiwRQrK9ETwPzZtik16ID0NOdFmAR21VSSf0ci9yjoydKi_C_5SgNJshn8sln_l00qEvw84njsh0A_nhmQyfLDaZpSvgii0_OrOBb2Xg75PZRPJWgZRZBTWEq5P3ynD82nT5fuE1a_iEdGS8uHBhVvBJqoTyG1pLbGjl5OYRwDuc5fbCRCrFoIv7P9EgFp-b6QPlbWwnOAY2Jp4vkIBYpEeDYGal7yuqpscuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
لامین یامال در مورد احتمال رویارویی با کریستیانو رونالدو در مرحله یک‌هشتم نهایی:
«مهم نیست که با پرتغال یا کرواسی بازی کنیم، اما افتخار بزرگی برای من خواهد بود که مقابل کریستیانو رونالدو بازی کنم. در نهایت، مهم‌ترین چیز پیروزی در بازی است.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/97708" target="_blank">📅 01:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97707">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esQZkyFDoG7iAn4VNFtTIqAePExtmmCid-sNrvjfrG1YpS-J_tcJ41UUnmtg6qwVhtf8IidTLVsi_TzHzqMX-YMUHr61Cpt1n9PNlDndhOsJ52RjNb6gul3piulbn-gUpIF8GtVOHPMzSz0f5dXj3XNugSo03D9a8pypnMaVvBaahEp-II66jWYNror-yRlGFTd7jx2-PgecCagKZ4RMMWsx4LWw27TjvddQdoV6R1fS_0lTgx3Beyye0WQieS5oEWH5JaI22vxUsEs1cL-z0cJr2uCi4CpJfgYIaMqEKBKTPC5RL-HQHGHZYHykIZmkUnLUVhSCrgO521gd0U8Z-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇭🇷
🇵🇹
ترکیب رسمی پرتغال و کرواسی اعلام شد؛ ساعت 02:30 بامداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/97707" target="_blank">📅 01:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97706">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tghNrJMsMxhafrG0KhbLhIr8rTiuPlxWSoII9nxkoD8ZM7ZdVrUDQcrFa5ePHlOtE5-N7z3kM-Y-0SHsw17AHTxvZ0P9bOr3m3i_WluxqE74PqBBk9XFvwnkDzKzAwxDkb2dmmp52-7qRI1nRmN-Ozf3Js_9KhmYoxMINlF3UqAgiJxirRy-wf5TGaWnvCadObMu-VJJNGdQRpsAR4rcJw1B8zVkvIXUV8c4rKbGI0zG_J-5biciPIpkk4hG9pezRiPOXztm4BPqxSQ5CaBz7fGKYUVFJ_MpyXv6BhINnzoggWfh7i_mcRSWo8yEriae0Yh-G1cs7Yo6OiFd8nigRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇭🇷
🇵🇹
ترکیب رسمی پرتغال و کرواسی اعلام شد؛ ساعت 02:30 بامداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/97706" target="_blank">📅 01:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97705">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4FTyr1bHQG7fysTuIcJDWITLl5qoUmI6yD1xYEO6_LVS7NKk1eq2P1POzXSBkkpZ0AbMveZu2TZQfS09WVY7kFAEcVm7TFJt0dng2W-rI8iLTcNX9ldHzwblG9KhGoKKxB_VYfgsvuDmBIC3U5zKM_DlkfI1bwQ2SPW2ivr1TMP-OVVJdu1gTfgeYmjII5NfyIzezDNGgukcVBJ2_M8KPnpwxeSWHc2wu1BlQ73k4XoT0klVRFi_ydLFwcsy-dqfpFtH5um3K7oBxtP4Fk_nea4VPwihscD6eHHqBnCtJ9s8cmUTCeXyjjCnk83uBDlhpFirELZ5BzlJJDB1ik6Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
میکل اویازاربال وارد لیست گلزنان جام جهانی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/97705" target="_blank">📅 00:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97704">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adfzGnODDvNw9Kpdl4s9rH4gYaSTzWaEImsC0nqD-roLI4pu32jUHgoCz1ML2lNGqmzpEL5RiON5ltzuhzE3DIeEea6LGC-vshjAx6zw-YJsGiKJZijYeypU9cklfNkR2IekZPqavJSWZ1o9tFwk24WJk8lsWWkeuemCRRCYWc_6TUCMkWxsXQKJXiUgYLXF4nrGz3D99699IvzeC7S6WYWcmblKwE7K2fJBTMQAHjJNBe9annTJ1XhD92pG-BGZJdzO-b9FrkBlaxXA6GfH4Xwnm5lNXy6JlHQ_2QF8rvS-shpE-JauzgRbT12bGnNLNvfz0LhlBSFSr9AAgGQvtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥
🇵🇹
آب زنید راه راااااااا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/97704" target="_blank">📅 00:54 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
