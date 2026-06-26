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
<img src="https://cdn4.telesco.pe/file/BTzqOyjUJdCc5XdnxlQ7zqFf2zaoV5tgStPezha8ou2xCAp3s5f4hss6muFsAW9u5yfdr0mBp-JJQLdFvIOIGviOzHT5W8CvNnM7TpRufMPJxgb8KSLvb13QB9xt8GjNKHc4wj3WVVX8V6OBfA37juzjG9iHyxDfRdGyQT-LU87GrMi1CxR5RIyd9J4Uy1nnUmkxEJ1cE2h7mP_5zzug5hiw67Va5v8mHTv9prEOeOCoQr84_y3Bh382olVZkmacHllkJ4DCDTlnKgqAB2tBLjbjZ5o-rLe7Ajfggbj5OO6N3F6UxyHVRfAVfOTGTgo0yzc9aMIwqpw4kPqahcVKeA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 318K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 15:59:24</div>
<hr>

<div class="tg-post" id="msg-24376">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzzLm9ZnvbB9AhhFMYuU33UhxPRIq552v_mmc6jVcEY45_BO36y1OOtVzip0tHX83M9YCdtDqFBCq7NqUN0QizIWEXLzcgH8ICgGNk4q9NIJzWf6OTIb6CZ399CiJeuBSgDaRaayMxfPX76xTzZr44bQHP7Akq8DBtp9DwQtynjetvWPq5Ql7JG_vaZy2qvq-L1rmIVakMEQhgbIbKH4klywwH4s_JDFHTgX6BRwbnjmeNfX2YyLX4WlxlcdVSTxgyOIt2AkjR495LNgZJpxpxio-BcOPDoRcOko-KniQ6pNbf9m9hBMx37J6eqh82mhYhlOBApBdCTtOz2R4C_laQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی
؛ پرز از اشتباهش درباره مارتین اودگارد درست کرد؛
باشگاه رئال مادرید برای انتقال پاز به کومو 60میلیون‌یوروگرفته و یه بندهم تو قرار دادش‌گذاشته که هر وقت نیاز شد با پرداخت مبلغی ناچیز این ستاره آرژانتینی رو به برنابیو برگردونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/persiana_Soccer/24376" target="_blank">📅 15:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24375">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFlPzzGiwuhJOaU3p0QZ8b0_SuC0pR-aH6wH-7oiv-EXik-5DIGAqunYkYVH3FKZNkVnvEhM9mS5CvM3R0EkabtzIny3RtjvldDyMpwxq4QSDajkhhDdaBfZspiupd4dIRCRM61Ljxet0CQHYTnK_DMVUMdsEzifSrhjFAJ_rDBFtuxzW57WMiI9VSS4blKF2jKeLRM4LIrK5_FwQXUAoD0X_DLTKfKq6tsR_ZpfoZL99Aj4Re_OtO79scgsdxUyMTnqSZK_Efnh3ZEFDSdyuu8ji5yOFddAf9vTH-MKTKRRIhyfZcnitN7WSXzxausocyxM3KgPjk5flioG1ZOKHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
اسکای‌اسپورت:باشگاه‌اینترمیلان آماده است برای‌جذب نیکو پاز ستاره‌آرژانتینی‌رئال مادرید نزدیک 70 میلیون یوروهزینه‌کنه. پرز با دریافت این مبلغ بال در میاره و قطعا ستاره جوان تیمش رو میفروشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/persiana_Soccer/24375" target="_blank">📅 15:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24373">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfOdsDmRmhKaF6jCwS4q9_Z1HdMAKzqCPo1F1d0GvCpSSWY_XUyVnevELbCntJhTp-zrGgzpzIpMF00pATuCSPzdhMln-SRcLoHRfFq7LrsPP1qOa34WbIMNFTThsLkaEoqLAO6CI1TWhjfz0ONJD87ltZ7AJHh6kMJuJs0T1YeO-8EjhpjsJxOyHidIapLBBEHdDlurzeiV91NMZL8b6rNGzYXs1iN3vYzJ8A_oQDWv3WcvtQ6YBGoRcRsQLjatYOKmK0SxuVz8yXeJGecKdFOIwXop1Z2fy96tjVnQAAcT6ZYY5GnYV1FAIyKgaczDy4_CdJcGkbLj8rZay_ca8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cf0fdb6b2.mp4?token=aSCAek5Y8mlyk5pQ2OG6eOVMEzoCRrnZZg-O0LeOO1cB0CrJAEnUftLaSh1jhLdbjwmKnJeEqPBB7qG79Yg6Z3xpebyQ_NydbVrX7-VEe1xgKIw7bX8_bUY53ayvu8p6m39asC5sYUlxmMgleW_11EeXJtdO3-TPrSSrmtiMo-NuVfadE2IlSufYHHDmZgQvOvrtB2DuH4e4_D09_D4ek8DOFrqACKLmHH8CrDQvJcEBilRO8Z5CFn2i69t-71jiD_tlvwPjenzOj-rjzuEjbOKC-pQPS6yHH5a0DowLkHOrs7t3zKXgplTNAxxrhAEfrtsy_UWlDVkE-VZcu8qnuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cf0fdb6b2.mp4?token=aSCAek5Y8mlyk5pQ2OG6eOVMEzoCRrnZZg-O0LeOO1cB0CrJAEnUftLaSh1jhLdbjwmKnJeEqPBB7qG79Yg6Z3xpebyQ_NydbVrX7-VEe1xgKIw7bX8_bUY53ayvu8p6m39asC5sYUlxmMgleW_11EeXJtdO3-TPrSSrmtiMo-NuVfadE2IlSufYHHDmZgQvOvrtB2DuH4e4_D09_D4ek8DOFrqACKLmHH8CrDQvJcEBilRO8Z5CFn2i69t-71jiD_tlvwPjenzOj-rjzuEjbOKC-pQPS6yHH5a0DowLkHOrs7t3zKXgplTNAxxrhAEfrtsy_UWlDVkE-VZcu8qnuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سباستین بکاکس؛ سرمربی ۴۵ ساله اکوادور بعد از اینکه دیشب تونستن آلمانی‌ها رو شکست بدن و به مرحله بعد راه پیداکنن اینطوری از بین جمعیت همسرشو پیداکرد و از نرده ها بالا رفت تا بغلش کنه. البته صداوسیما این صحنه ماندگار که تیتر همه‌رسانه‌هاشده روکامل سانسور کرد تا یه وقت تحریک نشیم. برد اکوادور روی احتمال صعود ایران هم تاثیر گذاشته و ایران با مساوی جلوی مصر احتمال صعودش به عنوان تیم سوم فعلا از 90 درصد به 60 درصد رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/persiana_Soccer/24373" target="_blank">📅 15:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24372">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0edb018d7.mp4?token=UcJQx60hudCenOnC1WKpXI8VFz-_5OzzHtPg1WN47K9hMMq6xk_nrmiSEW5m9mkO0GhAY7ktnuQbxLFOr8UQyVs-sAChZl55yZx2X8rDAUvRAEJzkH7I4XhJwbt6wIKZlbiUWDgGzTbsUEpqspWFgpLF4ulJEUf1o69P7w_Mwogt7m70cnT5Zj1OnSfNp-XzacnvJwZON5uGCRSDPmVOnZVLgSmgsBHfvtL8SKzo0bJNd41WNnwTQZ3xQSUq-dbduuDUvMudphb4tcG9u46wVtZmmKbbnckPhn5gfCzKpM1Qjnfbse_gjH491DqszKzD3xfU7xL2r4EZiEqfdr5vYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0edb018d7.mp4?token=UcJQx60hudCenOnC1WKpXI8VFz-_5OzzHtPg1WN47K9hMMq6xk_nrmiSEW5m9mkO0GhAY7ktnuQbxLFOr8UQyVs-sAChZl55yZx2X8rDAUvRAEJzkH7I4XhJwbt6wIKZlbiUWDgGzTbsUEpqspWFgpLF4ulJEUf1o69P7w_Mwogt7m70cnT5Zj1OnSfNp-XzacnvJwZON5uGCRSDPmVOnZVLgSmgsBHfvtL8SKzo0bJNd41WNnwTQZ3xQSUq-dbduuDUvMudphb4tcG9u46wVtZmmKbbnckPhn5gfCzKpM1Qjnfbse_gjH491DqszKzD3xfU7xL2r4EZiEqfdr5vYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏰
بیدارموندن‌ساعت 3:30 صبح برای درس خوندن
🆚
بیدار موندن ساعت3:30برای بازیای جام‌جهانی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/24372" target="_blank">📅 15:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24370">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nz6J_6vAlYCqvIcgiBy3mKrNZwWzHrCB6D-bZUd7sHcR18TjOzrMrNU7w3dSMvinbpXPjygj2xtKi91g_Jz7T5Z-z14M3vlrrjDGc3Y02WY7bjajApzBNGpZepXQUX-yiA7BW7eumfE0WxBCDJ3pfVO6FQsMwTuVmiUqoFHPyRq1lem2-G2AMUwa8AqjXM33Z0kD6UiZmaRmsQMf0kVlOQWXqhtguQn6SfEwahzVlqlIAW8l8Zc9XV7c5eei-WnxcnJ28ZiWe0S0NNlH2WxsLT3U3UOdki107wc5DhQkJFOjwQp1L6hDR13DEEDmNTs6LHX9WccVRgyO838WDflqJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lcsGw15g6qf-_r8f6fdqwF6ncvF8-4gawkZgcmQiPHWKhoZh6ABdXPyvh3SumXiuAPXGnfFvmLSUMBjH3OW3QmbVg_AWiCS9S5NM7aJHv6rkBrHD6Jj-ZBKEMNYMZCeEqBkelU4m6CRd1xW6eSi1nTfFzuRX0GnbHQKtBIiyk9oyt625tacRfDkLWdxacXL1gtJ5Bh5arhALcgN93204fYo6qmsQ65Jr98JqmWWa25dn4DZt_t6xn1IDmVZkq6wQHG3lF8VcPDMaXTNDrDKN83JmLhSMUYwfpWJC-pYWk6CKKr_qJAKp43eSTDBF0FSxmJzjXgUtDOnSn_RfytZTtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/24370" target="_blank">📅 15:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24369">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWIujCFNNI3qoCjo9nGWt8U1FQnRqCpXXzKGGx-ex9r2DOzg56uPQ-BW3h2ePD2dcz1oDSVvZlUrTqDuVH9bKxf2atmhw8cFqE45pinEjPB4fZzCTou_O4yb1vWWqY-ec-gDrs2wIMet_0vkuiWnfYJ1oyKw_S1A80WgBOcTbZhWR2OqzgpObnoM_e5lKqXs7t-mvDXe8B78yft3E2y9hMJkknsKFO_AFONNQ8P14JMtmeqAQEqwMS6jNlo9r6Nlka7ufJI5UDOLpJs42Ri0_3Bat-OcfUqtF7Wy4wJodu9o8arsP8Bv5pIGW_ctPaZ4_Cfw2n5I_Rq0Hw_yCs_faQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سال ۲۰۱۶ سمیر نصری که‌بصورت‌قرضی‌تو سویا بازی می‌کرد، برای درمان‌سرماخوردگی به یه کلینیک تولس‌آنجلس رفت و بهش سرم ویتامین وصل کردن. بعد از اینکه کلینیک عکسش رو برای تبلیغات منتشر کرد از اکانت توییترنصری چند توییت عجیب منتشر شد که ادعا می‌کرد علاوه بر سرم، «خدمات جنسی» هم بهش ارائه شده! توییت‌ها خیلی زود پاک شدن و نصری گفت‌اکانتش‌هک‌شده.بعضیا هم حدس می‌زدن کار دوست‌دخترش بوده؛ نصری امروز 39 ساله شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/24369" target="_blank">📅 14:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24368">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ab6e00db3.mp4?token=FllIAr9-LGPkZrlZWWaSNQnwU6E4YJk3U5s8WVwnYVPsYidfbtzno5MgXoZdxaJI_HU-2h_gsxdik_WEKa7i_Lx6f07w6HYv8U43oGlY2DGBFZrMJxhK4TE9V6juQRF9Et1d0gzqmlzFYD15woLQkj0G4dpAXnfmMbXtjSrXnKnFBGvQ6f8NpkfIl8D4Qd9EctUAFGI5RIGFUzGxRNbKog2KriKt6pwRSKU81zH2rS4YMEQ870ORzuwOfE5p75vbdqaDyRtcvU5pRp61JRczDH81VGgLFmBKglQhIH_O9R314bYAJGyr62a3UoFlZajJJb0SgqluDyRntFdYcJyU2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ab6e00db3.mp4?token=FllIAr9-LGPkZrlZWWaSNQnwU6E4YJk3U5s8WVwnYVPsYidfbtzno5MgXoZdxaJI_HU-2h_gsxdik_WEKa7i_Lx6f07w6HYv8U43oGlY2DGBFZrMJxhK4TE9V6juQRF9Et1d0gzqmlzFYD15woLQkj0G4dpAXnfmMbXtjSrXnKnFBGvQ6f8NpkfIl8D4Qd9EctUAFGI5RIGFUzGxRNbKog2KriKt6pwRSKU81zH2rS4YMEQ870ORzuwOfE5p75vbdqaDyRtcvU5pRp61JRczDH81VGgLFmBKglQhIH_O9R314bYAJGyr62a3UoFlZajJJb0SgqluDyRntFdYcJyU2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیم‌های ملی ژاپن و برزیل بعد از اینکه از مرحله گروهی خود صعود کردن به همدیگه خوردند و این مصاف جذاب رو رقم بزنند مصافی که قبل ها در کارتون‌محبوب فوتبالیست‌ها پیش‌بینی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/24368" target="_blank">📅 14:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24367">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=MNVPdKR9nVycxbei2nlE_-lrmpqU-v2v1ze7d0CFH04WTTJ79e6hVOGCt5e3sMYAmby893U6p3PSdJ6NQ2AuocfT9R7XOqeRNjTrvxtf7QlqNbrxPvU_ZohOVKsVza1_oPUM20JsutT1XBdcG-sk4M8OzM2psIlZ-7ZruKKcoSOIYWeQqbtmJvw2p1e4k-kZ8pOg9VPGkdpw7kiz8Ole4LB6pBHM_qB0OrgMs6e9X1Ca6gIY4ufDs3CAqA8eeC-MCz8SL65N22tpsrWvKjNT4HuVvL_XaENuKvbKAo0hYKksZpfItst467FxhFASDSwvuyJY-AfQOvFcBUKxGEdv8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=MNVPdKR9nVycxbei2nlE_-lrmpqU-v2v1ze7d0CFH04WTTJ79e6hVOGCt5e3sMYAmby893U6p3PSdJ6NQ2AuocfT9R7XOqeRNjTrvxtf7QlqNbrxPvU_ZohOVKsVza1_oPUM20JsutT1XBdcG-sk4M8OzM2psIlZ-7ZruKKcoSOIYWeQqbtmJvw2p1e4k-kZ8pOg9VPGkdpw7kiz8Ole4LB6pBHM_qB0OrgMs6e9X1Ca6gIY4ufDs3CAqA8eeC-MCz8SL65N22tpsrWvKjNT4HuVvL_XaENuKvbKAo0hYKksZpfItst467FxhFASDSwvuyJY-AfQOvFcBUKxGEdv8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه نویی درباره حضور پرچم‌های رنگین‌ کمانی‌وبرگزاری‌مراسم‌حمایت از جامعه LGBTQ در ورزشگاه سیاتل گفت: مااینجابرای فوتبال هستیم نه مسائل دیگر. تمرکزمابرروی مسابقه‌وکسب موفقیت است. درخصوص موضوعاتی که در دین ما ممنوع است و وجود ندارد، نمی‌خواهیم صحبت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/24367" target="_blank">📅 14:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24366">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pa-n_m7pa6-qTtrMAOVZr4GYffqgEUjAMpnoP1icxD58w0bivEZoGsisa88v4lZgJU9-BNqm1D8QjKhV5JUjVadNvqHyosyNUYl1-je5E6Qtw82xxmVfWWNVBQXJSYfdVd_4xneudehYV-UP5r7jsWQ_D_eWa2lN9oFyZDBE-qMR8sFYBpqPfJ8RunABuIwdgZ9x2A2hOdttGVXYtlGLg2aYDx8rZf4d8sPxs3nzfraWHKPWSMoUo3EGR66LN_Z1zQgvrlz7tKQZlr4CIDHa4WNanlsXCogwR0Zee9775Ufryxjg0gMLY8o_9S1_k9r5Hqy0Rb0_bSbLnr4Vh4gjLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
دو پست کریس رونالدو و لئو مسی در ایستاگرام رکورد داران بیشترین لایک در جام جهانی شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/24366" target="_blank">📅 13:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24365">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjSXtlh37cBJdUY4rBftODIBTtUsVEDjNq2W2bY1l-Q_bcZ2m0rcsIQC4x5iP5keMfhTA1do1vDZeebnsMhMhIaBhCIrwN9bI3NPsGpbiywrcH10iF0vOhXWduEDfqOcjLPgHstOvrVjeyPjIQWlfArOEve_k5xVbCfy4xsRQyyFWTs4zyXkyHlCJkHbW4XAjjliJB9nIEhK-uKBQO5FHB9q_Lpxui29HiWU6aWW5Tl44ptO90WdBR0RBKrxMjaSJFOfbU98uzWrnae6D610QlPr_pDTa6QS_zRnP8cb7IMOMLWFst9I-rWm7RHRYs4He_NTD_JXUcx0PaDcM9hwpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇬
عمر مرموش ستاره‌ تیم‌ملی مصر:
ایران تیم خوبی داره بازی‌ های قبلیشون رو دیدیم اما ما اینجا هستیم که قاطعانه این‌بازیو ببریم و صدرنشین راهی مرحله بعد شویم. بنظرم بازی رو سه - هیچ میبریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/24365" target="_blank">📅 13:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24364">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aq5Q4hX3wOzjgdOFkEN0uprHZEScEvG_ke-lf51LmMXOkfSqxv1Qa1CVoz89SL4w3KMzSpqDstOqxWhcWh_nYkfVB8aQ0pP4BThcFLr8ecTd6rNXay_QC3sYk5ze4cPqlSf9tkBOvoG6EvYdlemk59F3UW2t14tKVoyPudUqtcUara68n2QFQdpvYnIMReCg9sbfWvNrlOGq0zgmzcj2JBSXCUsxRGMXPMeRL2aCJl1qo1VGBSlckdSVWO5BQJ7xNDrdmNB03dUatwKqIe1q9IaRdGx6XIa_L0RyylGOb9DRZaxjnLfmaTrMQWEcHNYSBFuTLKrXF59EUl9FDI9cLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
اسکای‌اسپورت:باشگاه‌اینترمیلان آماده است برای‌جذب نیکو پاز ستاره‌آرژانتینی‌رئال مادرید نزدیک 70 میلیون یوروهزینه‌کنه. پرز با دریافت این مبلغ بال در میاره و قطعا ستاره جوان تیمش رو میفروشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/24364" target="_blank">📅 13:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24363">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2dMDdwIu6EgJcVDzLsjWw02fVd7Yk7LVyWA1Abe9Lo_rP35Iy_C5ZbBoIT0zGxiLHHd5FnuXY2qHiBRHXoy3ifvabl091rIqpE2q1UXUb939xijOD8hMHRPYzMD0iGxn9QNaOF0x6jz4UNEg80xjMJhrevhXZhIqAVRGvBcxeBpwAvDVRCqF-GZMDjqILzx0ipP5gDmCyxwGoc6hWzgGjVn4m1nV3NIIyBBHcEK0MsUj7fP0hIsj82jyb-_4aZ_GNxEgXpZdoboOkr9-Y2eKTQlb3gVJbiRse5cUmYm-YZxVBYurEli-hCgWk3A1y6WT9GB-vKzVltw3OPmud5prQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/24363" target="_blank">📅 12:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24362">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYepwfvNvH43Q3k6SuCmTQHjV_v949qt5njCMaa3bybX3suewhu4AG1IGZQn4mJ-cYo1TskzTx9nQuuNopC4t1WIazOloLWh_S4h1WWVjpj26zh8xmalnZzVdkgoKtqt90Mi7uAicojSicC5xcci3E0Hsy1wVIbRwDINybzzOuZv2JtDNzw56qF-xRUYo7p3Iw69L7u3VuBQaVjeoLEJanh3OFdH3L004Pm45lk4848mF_ZiJfns-RWLyu0brMEMMY-HXBe_H9HGf3gFrB2UTqQWTp00O2DPd7ly0021wTtig-ZjO-Yi_vPJkJVWxzLHmVS8pZSHGgYYdlMCsOVNqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب‌احتمالی‌پرسپولیس برای دیدار امروز برابر چادرملو اردکان در تورنمنت سهمیه آسیایی؛ 18:45
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/24362" target="_blank">📅 12:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24361">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upiFSqODacQdRwNUbIJX0WGDqfz8V_tiiQiJ-e_5gIidr7rZeYZNoqKMUwiw3NB2e5xVHiLg3qVX3p0OpPQ6Qd4ZZqMP0LFuw1Bel2QFk1-mPdeauX6RR7AU4svf4lZnr6gb7TETTcbWA11LCwAB3RmKuAfjkT75yhTCuFgsAZ7P_bvxrwJ1BS91ZzReQro0FwpWlfX3iE3TwJasMrelIzszLcIBwQY0hSSyAdhg-uBVLIiPInNlRB-gBPtXbJ_vGqpigyYbAkR4xSg8AexW4JAnZUpOkyTfA7iGDNkY5ZBHwjFlmkGydYLqA6FTf4d8e37BWVblmEwY9lYAgWQYSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون درآستانه‌دیدار فرداصب با مصر بیانیه داده و گفته‌رژه‌همجنسگراها قبل بازی رنگ پرچم کرنر و پرچم‌های بین تماشاگرا و هرچیزی که مختص این موضوعه به ما ربطی نداره و به اجبار فیفاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/24361" target="_blank">📅 12:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24360">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b03de0d7d.mp4?token=bM4USfpelI7eCm6brTfHxCd9pEry6FNJUBK6K06fXhgYRuBX0YYawH8HJNIvHzsPS17JwMQStl5nIOQ6cATglJYoxHWZnFUZq6CDBYZpkYLP7ciwMQq4vftworsL571JmKIyRtuRYdTPMiiCe-BQH2k4zW_vyC83KVyWgySxHHzCv_g6B3ZYckjUaeVlQ8tezkyfIiYBvXgU4vHY48ghU2cmLWBNKKlIt1tZMX43-h_hRm-XZeu0RZzUBAkkoej2RNprxBFN2dMlI8bvAkUHBPz49mAqC-bw_lpjK_aSyfX_KnDwKmbBlVuoL0YQZGDua-1n2875ZLMHar4HFFu76w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b03de0d7d.mp4?token=bM4USfpelI7eCm6brTfHxCd9pEry6FNJUBK6K06fXhgYRuBX0YYawH8HJNIvHzsPS17JwMQStl5nIOQ6cATglJYoxHWZnFUZq6CDBYZpkYLP7ciwMQq4vftworsL571JmKIyRtuRYdTPMiiCe-BQH2k4zW_vyC83KVyWgySxHHzCv_g6B3ZYckjUaeVlQ8tezkyfIiYBvXgU4vHY48ghU2cmLWBNKKlIt1tZMX43-h_hRm-XZeu0RZzUBAkkoej2RNprxBFN2dMlI8bvAkUHBPz49mAqC-bw_lpjK_aSyfX_KnDwKmbBlVuoL0YQZGDua-1n2875ZLMHar4HFFu76w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌هایی‌که‌کمترین‌درصدمالکیت رو درتمام تاریخ جام‌جهانی داشتن رو ببینید باحضور افتخاری ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/24360" target="_blank">📅 12:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24359">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBW9jpbEUDjmQl6aS_aWpbBi8dtg2qTWpxoOi-I_yPjn_fgD0gsaeJDa63ixIliM4l6i7AQ3XpbfBG7ppbfPrqSgQPSB1xBAn2jX791ExxoZERFUNYdsyQb_zQMPzxTm1gexNPhKYJHvKW4Pksj3dupWG6u1Gj40kGLiiiQ3JzNavsIL7UQoLw_e7uFG-ZydHpbR8U3dU50zAmobMpEHQllSFxw9MH3df3kYUt16d-MOnCJMv1hK-1npSMwGdGBzTAPJs8aleth0GiwTLRtZD_Y9cKnSixF8vZ9pO3Pf55nri-oHOACYJuLI-IV3DlKE86u3WOznHb_4spIUUA53vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخبار مثبت 18 و جذاب جام جهانی رو در پرشیانا آنلاین میزاریم. اونایی که جنبش رو دارند اونجا هم جوین‌باشند. ادمیناپست‌های خوبی میزنن.
🫦
🫦
🔘
@Persiana_Pluss
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/24359" target="_blank">📅 12:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24358">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBpYhhjeAwADwu28oAyxFGI-7qnFbGHwD1drEeaZVtoL6l-1rfqvBGXLEvxtCjOOyadWm5pnnvjS56tUowBSOgVqudRxLUEoBioQTCfNfPotgE3xq3GSZJq200m5VUM0hcF78MV8RPrn6HLFFhm5CLY7fyPujpeBNxCvFE6y_QWCWzkP9KJV-jZHbdCRo7hBd15SRrQM66MO61WqxhKPd5mPqZ2oMi4oEKXx5zg1m7pG2jtkLeZOKT6j84RO-3thcjH01SOBMlT6WRdeviCG_NkQ0KHdhXvLipbq0wAATdh_M06AoUOs3F-Oc7nR3t3ukBZzlLUWGS_rvq5S2NogWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تونی کروس: دراوج‌فوتبالم و درسن 34 سالگی خداحافظی کردم تامردم روزهای درخشانم رو از یاد نبرند. موندن نویر درفوتبال درسن40 سالگی نه تنها هیچ کمکی به تیمش نخواهد کرد بلکه باعث خواهد شد که مردم روزهای درخشانش رو از یاد ببرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/24358" target="_blank">📅 11:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24357">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6tJ-Jo_OUNj37B9fvhU5LlKrOO20QJidCSx9kFSfsO4E7EzhI6OARyRMe53KiMiu96xyqqMjJCBNBwqAmb8XOb51MqTzFXOkFWglwrZFV-JjsW8S8g6_nOwPqKNJQYAU0_biJvIfXOGZ2522c3KzmeJ_JFwKXH-92r63RiF6Vm2-1alPV5Ov9fR8HrLdTbPa34YCV3imIxfSbYiws1R7qZh44P-FBqqPrCWaTBfeVspvJ_f46HXySqqCKeppQTuJSNKt5_3dSk43T9ekp-v2l_XWwlaXtkrH6Y_OnT6HA_I9EsHnWYaBcbJPNMqP6cRfYqYRClgUej-SBusxd0FxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الانگا بعدازمساوی‌سوئد باژاپن خیلی‌ناراحت بود و فکر میکرد صعود نمیکنن. بعد از بازی رفتن باهاش صحبت کردن گفتن آروم باش، صعود می‌کنیم. پاترم توکنفرانس گفت بهش گفته بودیم مساوی هم کافیه ولی یادش نبوده. بهرحال‌الان می‌دونه و خوشحاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/24357" target="_blank">📅 11:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24356">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFS0Q0-3RmZKMon64cvhrzhQYqfyvRewe9ga770RD9Ry6Ffo3J68go7yQHN1D3v-3l4ynMDvC-VlynsBYMugbcIi8xQF_JpO0coZG--Mx6TuKff0xnq5zmrs81O-k4kG9Tb_146KBA-3mLsjBX2vfcEemlRf8LNRViVArU1yXRY6IpP4R_wWlEmpMT9jlLKln1mJIRx4h328wYGTLcTVWTAK7ACC2ng_veJHdUNn5buv67FLv3FZj1OLowE5xS0RGy9XxYt81RVsyqbyDBB1I3mChRw4qzQXrqV3C02uRi1rw-B7gEKtpt4qW7bNRa9f-0F77sh_riOOo_2GLoTjRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
ستارگان رئال مادرید؛ وینیسیوس، امباپه و بلینگهام در این جام‌جهانی در اوج آمادگی بوده اند و ۶ مورد از ۷ جایزه بهترین بازیکن زمین را برده اند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/24356" target="_blank">📅 11:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24355">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8eiVy6hYsT27ASlDsh7c2GqDd_mKKPJW22DsjlzRN4TzsPGeszrafMIM6jsB2J_wiBe8i1a7sjpvojpvxCUoRjpdWH4ED4McL81QrH6JaJnqV1KkWFIVRoHirAKiuc9Y88qIhnr7i_PZFy9lGFAFPEj8wwj_9_FaqyblLFKi9xM56QuQbC4OVAsJZvJj_W3uhQRg9cPdfElcsTmVD-N8-RfwJvmRCaXQj71tIpMC5kRIF8rZu3axwbrNcizgTu6WgNtVFuzyUn7qB5NPa-pEFFrqsCRKu5xXudGSjQtzWA1IPZn5M9Crx5IIUSsGDz9wyyE1f-TDda_12Guo2ujrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ مبین دهقان هافبک میانی الوحده امارات از وضعیتش در این تیم رضایت ندارد و به‌دنبال بازگشت به لیگ برتره. دهقان فصل گذشته قبل از عقد قرارداد با الوحده در آستانه پیوستن‌به تیم پرسپولیس قرار داشت اما عدم توافق مالی دوباشگاه‌مانع…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/24355" target="_blank">📅 10:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24354">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0e3e7e8d6.mp4?token=cwxpe74IG7afhelsEtKTAXNqO1UzvtHXtdIri6CeJ4oB-a8iW6-yrYNy0ZCe89U61XoFgNjca2uAKSqsKOub5JfR8A4u2GynDsBAfs9yEq54MwPawueNvTE4Ba_bt8fLYY0pOQmb6UpkE-20G7OAV-x_4VKSclJ4BcZMgAtjXKcOX79tH8dVWggwSCYY6k93hrPSSnkBP7nezJdhf_mB5D5ZH305CrJRPK4FRf7LhAisoTLXYbV0XhLUHa53Pl20KBTSVF5VzAXOfS3wGP9QiX6PqHXmjM6r4yqVQcZKwrpwrhWu2NR6Ngbt5zGLwOHHGE4C72CsfSK6BZ-Iu4zMOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0e3e7e8d6.mp4?token=cwxpe74IG7afhelsEtKTAXNqO1UzvtHXtdIri6CeJ4oB-a8iW6-yrYNy0ZCe89U61XoFgNjca2uAKSqsKOub5JfR8A4u2GynDsBAfs9yEq54MwPawueNvTE4Ba_bt8fLYY0pOQmb6UpkE-20G7OAV-x_4VKSclJ4BcZMgAtjXKcOX79tH8dVWggwSCYY6k93hrPSSnkBP7nezJdhf_mB5D5ZH305CrJRPK4FRf7LhAisoTLXYbV0XhLUHa53Pl20KBTSVF5VzAXOfS3wGP9QiX6PqHXmjM6r4yqVQcZKwrpwrhWu2NR6Ngbt5zGLwOHHGE4C72CsfSK6BZ-Iu4zMOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇪🇸
ژوزه‌مورینیو:
من دوست دارم بازیکنای رئال مادرید درجام‌جهانی ببازن و برگردن به تمرینات تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/24354" target="_blank">📅 10:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24353">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇵🇹
🇵🇹
سوپرگل دیدنی نونو مندس ستاره تیم ملی پرتغال دربازی‌مقابل ازبکستان رو از نگاهی متفاوت ببینید؛ همشون فکر کردن که رونالدو میخواد بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/24353" target="_blank">📅 10:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24352">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HFVixNwE-im0mbX3A4fCLwQI8DGUvHK9Y_ZxP_Pn_juShNaMkZQynWgm_5_qlexZKNXSFJfNx1xuvsIur1N9_qlOzDRrPKJMB6y4q72O2lJNt7ln5P0aYFv7KA1SoCnuBz8fIjy2vxiU0b5k4xaSTkPB6Fqq4Om3rEPg4c2QbbE5SLSZa8ifTvKRCZa6s_Zvg8_1DD9i_pMQoGTcCR8gcdzNW49Fht_KPQ3PWm8el1a4XQHf5WXTO8fh-wCqZBY8DYWk2B3xPNLeJFDCUyz4ZxRU-6hz8OHDBYPCUsjyBiYs2yzsX1yltG4sTjZvJjd8ThpC5dhC1e6bGu11481dGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
بازی فوق حسااااس
فرانسه
و
نروژ
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه‌ای، مطمئن و درکلاس‌جهانی پیشبینی کنید!
برای ورود به‌سایت‌فیلترشکن‌خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/24352" target="_blank">📅 10:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24351">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIuXlL90dLiwLBLKCz4pAMtc6tEX7B6anC0dM0JxSOi9zp5FF0Hk4aFHMRUzNtd7qC5nTgmqgly5W6hiZJHFUi-Kp6B3-9263WRY45AIRfiPjKtYDAbakuyFGaVNiklP-p1DgTwBeN0XHwoSpKMrYFmSoLFajcKwSC44VxBystIvmsdd5FBj2htGO7bJzk2O8T33OqgsRdkK9lWGd6fblVemCDi42d8PW4TPhF6pqDpx6LBm2AhBAxo-vBsZQGUpV3oi0gva_m3WQbESX1e5S-6U-_mv76UY9kDdSSQoOxPu36anIlBjj-EYc-9t6tMTXW_wdIFFN1zlClcg_SlcXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/24351" target="_blank">📅 09:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24350">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkO27mitCzqnQWUZx3avSOTS41KjPa8vuzJs4n-eK3t2AwJpHQwhGdOyq_ISO6jb0SVJobTNIBFi64M4NKaFXswABLjowlZN_ylQpaaRROWRJ0JYyGdbIJBI8vMJmqDXn6dxdq9vEtSFMiuh_9CfkP7JVwalL-Tei0g4PnfHyQF1S_4hvUIP2svQgTJaCvG2OfNyrFglQITorrad9s7yKYciei3BjCHy9HrOLl-rCAwffbCae1idSzoALihyF0wmgcdoKtige0CGbpbS6euoOL9QWlDJtety6pjodk8KyR7Anr7_1ZULtrumCf4kj_r0Gisb9VKk9fhyhnZfmuZIyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی 2026؛ برزیل در مرحله بعدی به ژاپن خورد. هلند به مراکش.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/24350" target="_blank">📅 09:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24349">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=M9OcmhMIT-uLtWcqxtq3FkcNk_WQ-otaJpKYyERefIi4qyc0MWLjaryDkSg6Cqyq-FdcYo4Rep_Gh5sArEnD3mYPBKwoxlb9bKVQxU7qRastQVI0bnfIC3tQXHbywoANGgbssdESs9HiEoJl6PZ01VoT30r-ufE9uae3vALvoF5Q1hEV_TfpgkV7GcUNLyBFbXycYW1odjITXR6hrWycbEf8F2NtF5PyqgtW51B8SnTMhqQM9ADXm7VUU_41kwacj7Vx4xPrzH3b05klx34_lz6nXMdo3U7K68I1fSOkUAtojLrbFcNhd5c1nrCiJWowdBQbMfhfJYGPB9tuxeNNog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=M9OcmhMIT-uLtWcqxtq3FkcNk_WQ-otaJpKYyERefIi4qyc0MWLjaryDkSg6Cqyq-FdcYo4Rep_Gh5sArEnD3mYPBKwoxlb9bKVQxU7qRastQVI0bnfIC3tQXHbywoANGgbssdESs9HiEoJl6PZ01VoT30r-ufE9uae3vALvoF5Q1hEV_TfpgkV7GcUNLyBFbXycYW1odjITXR6hrWycbEf8F2NtF5PyqgtW51B8SnTMhqQM9ADXm7VUU_41kwacj7Vx4xPrzH3b05klx34_lz6nXMdo3U7K68I1fSOkUAtojLrbFcNhd5c1nrCiJWowdBQbMfhfJYGPB9tuxeNNog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
نشریه ESPN: بازی دوتیم ایران - مصر در جام جهانی به احتمال فراوان بازی حمایت از همجنسگرا ها خواهد بود و فیفا نظرش رو تغییر نخواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/24349" target="_blank">📅 08:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24348">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxxMYSB6_id5dOR_iiBPIhqDqHECPlEHvm61J9lDdk7sVVr5o_AvTLNJNiEp_Gpa_vnVQUnNPLUMccZkRYnoRzUIFTI8kOzKVwZh7ihKonRc88T-CuRZ9w1PhcSyuK9Wzb-yWHwURt2MhVlWx7bF_5kCjH8R7un3dE_fR_ZyVhZFWha3utPVoK9YSnjQ5kOdHTKJgJvFAEBandugP3jAVhcfRv37xNgZYpShRq-5UpmEovaLjFH4_MJKAOzftHjLVjwoJJE-htXvswF-pePWRWRihg9Dr2g3KO-UZm3DnkDvw54FMmLPuRVSlwlCufO1zybBZlT7dV1glfmNFoKpPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ ۱۲ سال پیش در چنین روزی؛
آخرین حضور جانلوئیجی بوفون درجام‌جهانی؛ آتزوری فقط یک تساوی میخواست، اما ضربهٔ سر گودین در دقیقهٔ ۸۱ همه چیز را تمام کرد. کسی‌آن لحظه نمیدانست آن اشک‌ها اشک وداع همیشگی‌بابزرگترین‌صحنهٔ فوتباله. پنج جام جهانی، یک قهرمانی، و یک خداحافظی تلخ که هنوز از یاد نرفته. پایان یک اسطوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/24348" target="_blank">📅 08:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24345">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edESG7dwlVBCDgas8LYzx4v0Tba1XU7cvS9INba38Z1s_2x6BSS19IxEAoxVAL9FeEATzRtILsD8Lm7QhMR6P0X68ee-TPnB2_mi51KyFVTOD7uNrM7xN1X_eMN6_aYjucip57kP0HXnsmXot5Qo6OKeCJ5h960P5_jewiydWdWdIBCrdHPSsof63YblGPVIWkBv6l_m8vIolsMaFWHy8zGA9ErZ2loV5U7qrhm5aS8fuxHW2O8Y9GQe19s52QOPpjM8YgK_DG1UXj8PsZjLb1YcBl0SEk82qOfIx5AnLktZqAnkLFEMM6x0IyajPghvyx1_GU6LkTCQzc5qz_DGLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه F و D رقابت‌های جام جهانی در پایان مرحله‌گروهی؛ترکیه‌بادرخشش آردا گولر سه بر دو آمریکا روشکست‌داد؛ پاراگوئه با استرالیا بدون گل شد؛ هلند سه بر یک از سد تونس گذشت. ژاپن هم با سوئد مساوی کرد ولی جفتشون رفتن بالا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/24345" target="_blank">📅 08:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24344">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFL9vMU7UJvodxekAXsJhsAOeXX_O5tUsfgMKznvGQYxDlX7CxKbLcoaScRN-jIdYMdhzM54b7u5jQSScO_MiOv5_TTlBqrp96rVdCrMmgdiJ9ex7fhNvK4CHzhvEDGaEbfOCzW0o6oBlIjWN7j88g9pEJpflsHFH5aA70JfFxkfV-dwnB34-Xwlboz9KgvX4JC_K6cNSfb4Ul-JdTcpoBk8WzxMzsKqc46iwtthySZLKWMxyXXDknqeF1LZ3GvLnpzY2NxG-wFXgBekdMdiqXgK_Yrx1uO5DiK99yNyV0q5qVGz57mGVjrBFNCsvvqAam6UJJmzFXRzbdluwD9YCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌امروز؛ از نبردآمریکا مقابل ترکیه تا دوئل فوق‌العاده جذاب یاران امباپه
🆚
هالند
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24344" target="_blank">📅 08:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24343">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICvho8ztpR6fKZ9q7pd__i0aqJ7dncwF2HTh8CS5NbfkH2fyYLIZZleCVLYmy0imqf2EIpy5GFjhAdXeDwtGSmK0W5XYACpPrcLl4mvvlQIQBPfprb5ULgTiUt27SEidshezgC1DikprGhqCI3f_3Ej9b__3jjtYYd72MGsQJ_-Fy-A1AA8HXsE4y3Myexl2P_2ttBRcers9CVycMd7GerVPnmLYOFDuQwQ6A1S4YLk52JsrR7alRP05GmjOhwSkIwCUDuOlaWKXkWuiaQ1_GownR3UzC1vE8TrmS0qdqxwidbecnB3SQXHuC12J9Nxxs4uxUYtFZK8L8r8TqyTunw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
موعودبنیادی‌فربعنوان‌داور وسط و وحید کاطمی بعنوان داور اتاقVARدیدار پرسپولیس و چادرملو در تورنمنت سه‌جانبه انتخابی سهمیه آسیا انتخاب شدند. این دیدار فردا جمعه ساعت 18:45 برگزار می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24343" target="_blank">📅 02:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24341">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhI5tsGZPWu91yjmmLTpCLf-HiWltXOdWNno69ishDxc7y04SEOUqdGQ9tu420aiUBC-cNxXWy9666ZLt11p5S0tw-5kTt8OGRKjvl-2PBdTze_XEPnuJYYF9POqqmRChNzpjMV5vUWo834IMa6fQ1VO7zSQXUGMMqipdENc44jh6alQ4Rw9mAAxizK-Bg-liCXXsZllbdPN88vG571HKfU5dkygGYVAXAYnP1tXomgkebM05kDdDIj6mz0z_oxjs9MbeQkXfd0fJtotYb6GD5O4j1aINwyZfvksNZAnDklGGSwJ53vBSRZXevnndr2GE2GDRe9Yi0LiHQGOzQKXrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌امروز؛
از نبردآمریکا مقابل ترکیه تا دوئل فوق‌العاده جذاب یاران امباپه
🆚
هالند
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24341" target="_blank">📅 02:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24340">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOXjmU7lMiUu1O-YMKpY-YF7NwSDnC04m5Fdip9lFuJtWMzz4RTGqd0D_x1AoaLhk975OeGgggo0wTcteAipoDIMuN3spOE3VJmiRWWjieZs9CnAvhBdU9vX27OVQ4sOowzQppTA16OPTXoxeroLKaZ0MgpReKgjGzm7ZTzBrAfuvsaK7zaF7njoFAy9JzjpARtsLXgtfIOpCsvIlSw2ax8Tyi9wr8cX_l7YvhDBSE2S-DOAVdvhgp7mvte2ZBY0xyZ845xlFXsMHn85Qt3EY2JymQXRJyWTnI6ix-d0Fhx2t6Xz8weScTPZtfpl2rXvbwuqlY5Yg-VBmC563VEP3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدارهای‌‌‌‌ دیروز؛
از نمایش خوب شاگردان آنجلوتی بادرخشش‌وینی تا برد دراماتیک اکوادوری‌ها مقابل مانشافت و جواز حضور در مرحله حذفی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24340" target="_blank">📅 02:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24337">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🏆
جدول‌گروهEجام‌جهانی‌در‌پایان مرحله گروهی؛ اکوادور درهفته‌آخر مرحله گروهی دست بکار بسیار بزرگی زد و در گروهی که نتونسته بود کوراسائو و ساحل عاج رو ببره آلمان پر ستاره ناگلزمن رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24337" target="_blank">📅 01:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24336">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGeKEkSOoCVGrPbDa1ab_pYUzYAAgewjfu32gthlfIVEoxEEXsInd8i9n2cFSoLbK198BpOTCS4o6_wu6c_vX5te3MbSYXimZ44CZJd310gzJsBzwbnbqnpBZW_kQvtp3ElB7P5mbb7ZuQye7QB6e9a1cPoWgosm9WuptZ5dHqVkd6J9TuDpTeDysvu21py6MksVR8FaYqz0Y9U6QW1RZ-nyeyVgxkq1C6J48ibAvktgKyyoF9AtgOGZfaI9-TVnNDAVHv6K42EqVDXwEUBiui2tPR4RFy8XDjYhEH7TKeYoHxE2Eybs4YYljlcEZoYNIl8vjs-PL_N_P4HZ4oAVjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گروهEجام‌جهانی‌در‌پایان مرحله گروهی؛ اکوادور درهفته‌آخر مرحله گروهی دست بکار بسیار بزرگی زد و در گروهی که نتونسته بود کوراسائو و ساحل عاج رو ببره آلمان پر ستاره ناگلزمن رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24336" target="_blank">📅 01:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24335">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBpiHkxFCtGHYXYiT7-Ht8Kcu_k_5Pk2WI17L8Vc1xBx5aoziK_iJZUYAWPujVb66EYC5zu56lXoUoNw-Q-n1mSZswe1OmWRvjQlEzyQgYudig-znbCFa22nBaZvDnylC1K_5E4xBk9JX-Q9ZZS-CaQdmFW8_3WCH_ZwX4aPHt4NyBF6lEFC31FJtSCfqSgT-lE9ULrmAJMxfrHPuJiK5MbIEU_CgD7xaME0l2-zHtEUu6NeZehxYMkRVra6hIlvCbGg_PAISWjwIGx99cY_WDFZrP-UIxNdtc2L-Yzz_hjMk_L2h5lyzkGx089M6-x3mno5h9G8NMXhutU13Aeu5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/24335" target="_blank">📅 01:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24334">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1e2d32269.mp4?token=olyIKOzC-93uWRHxIaoftMGxS9ncyb3hxRDczg5NbyC1LcK-rkHD4y10OLolNNHZO3Bjbm4br5GL5A1eCEdkBtyzqdMDWrnikPX33KXQyIONL4Lpa4Mk1jozKqkBq6V4S2GwHJYgS3R3a0JvYLyANcNyR2_qtjSjWSyD04lGM586JABvggpqpiEsXmRGql-8_fyywmdqXwF_C5T46AS3wjYgW1tSVj7sA42ta4DDXYz301OztPjjY7rMlhOYmmc-qeUIt5QHMTGoB7BNHn007glUC-SD2kRzZz8bpAoJSKMHsFGOsBJajINotBl0aE3HQqNrP8mJTR8QB0BAfnjzGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1e2d32269.mp4?token=olyIKOzC-93uWRHxIaoftMGxS9ncyb3hxRDczg5NbyC1LcK-rkHD4y10OLolNNHZO3Bjbm4br5GL5A1eCEdkBtyzqdMDWrnikPX33KXQyIONL4Lpa4Mk1jozKqkBq6V4S2GwHJYgS3R3a0JvYLyANcNyR2_qtjSjWSyD04lGM586JABvggpqpiEsXmRGql-8_fyywmdqXwF_C5T46AS3wjYgW1tSVj7sA42ta4DDXYz301OztPjjY7rMlhOYmmc-qeUIt5QHMTGoB7BNHn007glUC-SD2kRzZz8bpAoJSKMHsFGOsBJajINotBl0aE3HQqNrP8mJTR8QB0BAfnjzGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
هوادار تیم ملی عراق که تو صفحه‌اش گفته دوتا از بازیکنان جوان اسپانیا بهش‌پیشنهاد رابطه داده‌اند‌. اسمشون رو نگفته ولی گفته جفتشون تو بارساست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/24334" target="_blank">📅 01:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24332">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbzpESm78aGcfatwBXkmkTH-whftIAUsphdipaYJw6sPLI-_elpJfPRqI4nrDB2sJff-PSoDpaLeVyGk2L2OOwOjsn0syi3ZvRK2xDUZOplVJecBctTPBbfdPloILCGLmnbHhOoZhaPoEZZau3i5v5FloqHew59qUJusZHJkqCC6txm7m2j4nGzngPjwwhEZPKY32O7yoL9jp2p0LX-7dRbtFMu5oyWhtbs2tFbnGPHYGhqkAgi-ttwv1Xl7_FMZ4To0eWhpx1U4QPxTEYJG3cUi5z3CyPeSkpoLEHkXSnI00Fha7hCoPi6DCIZRMIstehPYSsRttC21R0Zr2d7_8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق اخبار دریافتی‌ما؛ باشگاه‌النصر به‌ایجنت مهدی قایدی اعلام کرده هرباشگاهی 3 میلیون‌یورو پرداخت کنه رضایت نامه این ستاره ملی پوش رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/24332" target="_blank">📅 00:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24331">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mws2gQbyEXBNdKZ45QZqiy7r89rUH399p5SLZPY9wktpDBJneyKMd3YrPNJ6JqnUbcf2PRLJxqIarkP5Al-2VMSlIMb8JgjyKvM5XbSOwJLz87YjgbErjxoF84J70P20Sqmpzaxbu8sY-qWk9mnPWXp06dlgiCrZtem5mUYK2S8YMfGjFJUVl45O90wue-hKYWmbeivfd-W59R5gL8G2Tnue-QZtelhCp4SauCA7x-RYdDWemp9HoCG_eD5MoQKeKtT3kOD4t_Ow8OpL8pHpPcUpTmHZ5M7aN-U2b4NZuaNNd9OgVpUEmv0hm0smxvekWPwtuXAUdGBHFz_KN5lAtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|هایلایتی‌کوتاه از عملکرد درخشان الیوت‌اندرسون هافبک 23 ساله انگلیسی که به زودی قراره به باشگاه منچسترسیتی بپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24331" target="_blank">📅 00:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24330">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fH0K1EetPd5o2_218t7bag9rsdT5M6JBxUO0B07t5MWAc-R1Uv-QNXo6Oh4WatH8mVyxtO9SULrfDNgCRhX822aes2sTp8jMPvlFya9VmSkEaCpkB5zD7pZt1xSzr6J0e9U0Opnq-rWcDqXFR-xBmMo1Z6uj-9qHkvVlbw5wXd1Uzib5uwJlxvRaV_N6dECa8tlWPUNDtPAeYDvpPEGow7LMIdtIEpAXdJ-G6LQYrjtwCpdPatS30VU3jLlUP4JXhYDqmxxOxi7V_xKvEMk5OFC5wmqcyvDGm4IfngU9SxuA44bBQD9_APtkeRsd2031PTh8SKlMS4HuffC9BNQXzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
بمناسبت‌تولد39سالگی لئو مسی یادی کنیم از مصاحبه ژوزه مورینیو در سال 2016: زمانی که لیونل‌مسی 34 ساله بشه، همه گریه خواهیم کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24330" target="_blank">📅 00:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24329">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxsQye8L9d_rrPk9cVCs_M6T9-vhYa74f8e2K6pDq_20_yY68uoFik5kIGpMYc533_hb7-1WEEYgCeGAlPp7OwwGGjAmmt_jni-ld3O8GtLvkc7c5OuKKdayhEU8UWMVxxuEw1d9B7Pyk9RtkAdNOBxMb3O6Wbru9UMeBD60LvkS6-b_DCQK_FA6yjTCbSK-oPnLHGuewZTJRz6p82caHH5LKe4S-OooyZgxPGY4-6rU8q1cyixUV8rIjeMDXfxka9qesynmG0qTf6fKmGB-KeG87baSkVeprhP7LAhh2Hw_fuoOwKqY7MHjGdk5g4PV-1wV_75VZKpTKsgPizXO8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط ۱۲ تیم‌از ۴۸ تیم‌حاضر درجام جهانی بازیکن سیاهپوست‌توترکیبشون‌ندارند‌.حضور فرانسه بعنوان تیم اروپایی با ۲۰ بازیکن سیاهپوست از نکات جالبه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24329" target="_blank">📅 00:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24327">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e5436aa7e.mp4?token=J-4Dl1AIMKu-479ebxXZEDUbSbxyNQ5RMrJpIP37-iY393vLvfi-2XJf1VcEjKDHXMEh6i__m5K3bBlySxRGzSCIDQhnI06xk_THEzK4rRoMGk6HhWEPK-t1MNWV_YsjqH9yNe0rsCf13Z8hX10Issh9wenA8B3HXEq3HBTWvQTZwnmmQJCBPJsjDcIk4I6_Y-DsZV0DsSMry-s7swXV5qQVyTXz5pMn-jAEYthM5qd43xZkgKMRl4Cfa_pMyZmIZ2atTCdVA4ilEUT7L34VHn0OinTVf73zSBI_GTp04GnirQaKloFdikK4RSXq9LOX-0SnZOGRcXVym5eB6aE_iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e5436aa7e.mp4?token=J-4Dl1AIMKu-479ebxXZEDUbSbxyNQ5RMrJpIP37-iY393vLvfi-2XJf1VcEjKDHXMEh6i__m5K3bBlySxRGzSCIDQhnI06xk_THEzK4rRoMGk6HhWEPK-t1MNWV_YsjqH9yNe0rsCf13Z8hX10Issh9wenA8B3HXEq3HBTWvQTZwnmmQJCBPJsjDcIk4I6_Y-DsZV0DsSMry-s7swXV5qQVyTXz5pMn-jAEYthM5qd43xZkgKMRl4Cfa_pMyZmIZ2atTCdVA4ilEUT7L34VHn0OinTVf73zSBI_GTp04GnirQaKloFdikK4RSXq9LOX-0SnZOGRcXVym5eB6aE_iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇦🇷
بمناسبت‌تولد39سالگی لئو مسی یادی کنیم از مصاحبه ژوزه مورینیو در سال 2016: زمانی که لیونل‌مسی 34 ساله بشه، همه گریه خواهیم کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24327" target="_blank">📅 23:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24326">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAgZRBY0X1IQy7gfRgFwT3WsqPlYOcc74aAL0ZOHLMrfpZiDeyWjyNBG2GbN2lJdhtdyzicOvfoyejw_EvG5m0rhReMbFXEYHivrEznsWZiRkS1kLauhrtNFVPUlwW-L-qQRyWobcgMyouRQ5B9HrVty3DYPJkLbwgotmwhtqrH-t4ip7-8RBZh1Yj2OKz182ivgHgTlOg9ki8JxactQS-lHHL94dBZA8YR99vZL5iruY3eMTgyofP3jRrbjAAwzkS2ninAiHFxmzLl9mXNDOVGF4EKBMMyssIRL5hzpgeHVqiNzTuDirRP8PZtHTY2SHFgvGcxyBotKSS90H1HKSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تمام مسیرهای احتمالی شاگردان امیر قلعه نویی در مرحله حذفی رقابت‌های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24326" target="_blank">📅 23:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24325">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebKTvRq2hyrygWlEmtZ1HzHMh7uMcwPsJchA0LNfl9iJjrFxTiAMkon8MChN38aNCqwOgVXJ2oCZ07WlsHiAyJGp8tvgaUL7T5IPhRICjMB5ZUHJ0YpK7-3L91WqyJOb_L-kmgnvWwlV4AZWYFn1niQWJSjxN_0Ge9036OPN6UTpoH18F_tkx-qFb7iX39M6BZEzJIeyFNSJmC5JYcZPFddcozTyN-kwafy6lTn9jkIqjQ4WHMfPIpz2lVSIvu9l0VNpK7muGLk2_uJPy_mCzY-xlEujRNALsFPowuEQlAtmNWGfpXtSjVWSu19ktudARwoul_RZ4HbiYtCqC7HWbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دوست‌دختر ژائو نوس ستاره تیم ملی پرتغال هم امشب از نزدیکی شاهد درخشش CR7 بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24325" target="_blank">📅 23:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24324">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‼️
🇧🇷
خوشحالی‌منشوری و برگ‌ریزن هواداران تیم ملی برزیل حین گلزنی وینیسیوس در بازی دیشب.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24324" target="_blank">📅 23:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24323">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKLh2S7tPWnzJRJHu2VThrO7fuHNP89wdVwM085-y3rv8riHNTYfum_vwWvFUmaXgO0CdwNelUefW4QT4A4r21oyweciKaCOuFKd2SxKG8Mftvl8-fEGnfqIOjFe9O25MR_s4J-vA7bjqGG5B8mKRgIIqWeBwW6-WUcgjH0pMh1C5kfY8pWkmGF1ex1vzU5PCPD2rLKP8eR8lNEmJFHjA-G4C5MzLOpr9mpfjqnMgPVGEQInGki_9_rAVxo9Mt4CYieYBZsTyiXuW80vbnw8u8weC52fUQz42p56dUlksRjw8AJCVkBOOGDwdvd84oCSUd9r1w3pvjcskKksco5Ivw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
یازده بازیکن برتر جام جهانی تا اینجای کار؛ با حضور رامین رضاییان و علیرضا بیرانوند از ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24323" target="_blank">📅 23:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24322">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhJorOkJ-XVR6H8wAyHBKxwt7xZhO84eiNA5hP4-HxyaZRrNlm3-Gvxfay4JW0FosVBG9yvBuNTs5UlffjRGccXXv4csI5nr6MAJYn4vIulUnpIdQBAqshdxwfSIHwIS_20GZ8ko0rTHXTHqDlb6hXd5-1rjArLRsCEpRF6fe4L2Hllhu0XpBqzgkFaNX6UJyL_tNa4a1rgz7Z4jczqHSsLdtqu_XKmE5nnrLTvlPP4lnucrZX6fXnT-CIc4_p3Oac7SUS7OLlZJYJU1dS6foHTxcoBREnD0iY1PINcVOL1_yCnfjDyvR_9VSHBXpd6FaUsjWN5eax8fBWcLkm6AgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
با اعلام رومانو: باشگاه رئال مادرید بند باز خرید یازده میلیون یورویی نیکو پاز رو فعال کرده و این بازیکن رسما به باشگاه رئال مادرید برگشته. حالا فلورنتینو پرز میخواد این بازیکن رو با رقمی بین 60 الی 80 میلیون یورو به تیم‌های انگلیسی بفروشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/24322" target="_blank">📅 23:05 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24321">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42251bbcdd.mp4?token=UcpEd_BozMH4ihXV_HZpz0cZ75ADKcY30fz99TlZ6aU43AV5XXCEq6jMTho-u83Tr2tVlkR5_KmtDn8Qp0VVU2e9OkjuH30YeGKOAtEze2s5Hfqfgku7Uy2iI-s4Cpf26sWTUpHz2SjbXbFIMJ8lsYvWbCtLSrq9LOt0q8Cm6sYj-zN1WdqcU3i66QyIeTPnziDfMwIDmLRx4WKSyp11EBJSE-U0E1bbzpx5ZFv_EU4E-RlaGW-Iu4ly5CWIfZivbvMkSyG8u52t6WW5NgkbGWcoCKxI1pQd8cdHWhP8-GFWTdJyfY07-TQzcc7-XnOXcFSx4J4PaM5s0Vk2d7ramDRb2aNYiowJvoFg1o-aOpNyy-XzvSJgreJ77B6hULtKb2ZNoy5VwZF4Cfl43F6Fohc48rx48Rc5QDlp-ZUqT1ZAvXMqFBlyBA7ZxODdg14KjyBjFaxRWu8OF1GRFIJyNwLWHq01TrM5W8L4gOtfg7XZvRW1AD4_oZ60c4-mNK3Mnx5NcRrEuYu-AUWmU69xE1wrG4zcYQnWFEokdWvVSqhnr2FGc0z3Fgz8MtDESKWKulqTmcbHGsK1XP8Emjy8_IlEETQaYc10TC-p9sq5di3XX6xa5_kv0egEBRevCtC7QK-qgtSaOF_SdvkPAR2woXeI9-G5FJ4EAyWdabnu6aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42251bbcdd.mp4?token=UcpEd_BozMH4ihXV_HZpz0cZ75ADKcY30fz99TlZ6aU43AV5XXCEq6jMTho-u83Tr2tVlkR5_KmtDn8Qp0VVU2e9OkjuH30YeGKOAtEze2s5Hfqfgku7Uy2iI-s4Cpf26sWTUpHz2SjbXbFIMJ8lsYvWbCtLSrq9LOt0q8Cm6sYj-zN1WdqcU3i66QyIeTPnziDfMwIDmLRx4WKSyp11EBJSE-U0E1bbzpx5ZFv_EU4E-RlaGW-Iu4ly5CWIfZivbvMkSyG8u52t6WW5NgkbGWcoCKxI1pQd8cdHWhP8-GFWTdJyfY07-TQzcc7-XnOXcFSx4J4PaM5s0Vk2d7ramDRb2aNYiowJvoFg1o-aOpNyy-XzvSJgreJ77B6hULtKb2ZNoy5VwZF4Cfl43F6Fohc48rx48Rc5QDlp-ZUqT1ZAvXMqFBlyBA7ZxODdg14KjyBjFaxRWu8OF1GRFIJyNwLWHq01TrM5W8L4gOtfg7XZvRW1AD4_oZ60c4-mNK3Mnx5NcRrEuYu-AUWmU69xE1wrG4zcYQnWFEokdWvVSqhnr2FGc0z3Fgz8MtDESKWKulqTmcbHGsK1XP8Emjy8_IlEETQaYc10TC-p9sq5di3XX6xa5_kv0egEBRevCtC7QK-qgtSaOF_SdvkPAR2woXeI9-G5FJ4EAyWdabnu6aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مرتضی‌تبریزی‌مهاجم‌سابق‌استقلال
: گُل نمیزدم چون یک‌گلر مشهور برایم طلسم و جادو گرفته بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/24321" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24320">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4a69cfca.mp4?token=Rxa2QXpuJmZFkF-Rbk38baJyAvAgvPvJKOlrwHDIT6jsz-CKDO2nxMlhAoO-Ctq5HgRqQvFFAGiJ_1-BpNKRlqrD8X5MZvrpNfDOSefnohUEKAxNNBGb-pEUJNyGb4DWdg-jFbhVvIrTW53VBpTidubD4UuHGzw261UBEgsriFprh40X8pgtrz3ypW6N1L67RTLVdbvyGBRbK4w-PmtsttOOxmMDMLFWPRHnCThKSqsgexyRpJZjqjnnHJAP4rrVMZYZKsoKYuOHajFPi0FzMrd4IudFIWqIW62c_m7KSdPKFVp0uuPrmChZMq4wptilh3Vap_llI10vaPDoMgxaEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4a69cfca.mp4?token=Rxa2QXpuJmZFkF-Rbk38baJyAvAgvPvJKOlrwHDIT6jsz-CKDO2nxMlhAoO-Ctq5HgRqQvFFAGiJ_1-BpNKRlqrD8X5MZvrpNfDOSefnohUEKAxNNBGb-pEUJNyGb4DWdg-jFbhVvIrTW53VBpTidubD4UuHGzw261UBEgsriFprh40X8pgtrz3ypW6N1L67RTLVdbvyGBRbK4w-PmtsttOOxmMDMLFWPRHnCThKSqsgexyRpJZjqjnnHJAP4rrVMZYZKsoKYuOHajFPi0FzMrd4IudFIWqIW62c_m7KSdPKFVp0uuPrmChZMq4wptilh3Vap_llI10vaPDoMgxaEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
صحبت‌های‌نیمارجونیور ستاره‌برزیلی‌سابق بارسا درباره لئو مسی فوق ستاره آرژانتین در روز تولدش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/24320" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24319">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFizcHI3Q8TLc6_WuRBQrkLvbldzFPZ-wCdzJSFQFLa0pknf4zewUriBLC6Bzdc-1aXjM221EWctg9C5ny_h9BbJgGzcs_ujCCk2-4qH5yQty3CHk_g4X7mpnqxEW4JFkweCJxtSKPfi50tALGba4na97dS9vGqKocS6OttWZcxSo8rh5txvx-IuBYBQQjO0BCEwgkJFckwrF0jKin6be9bSv7PCVd_01aCkXt2jp95DSTT9W1jKIt28HXCqmg6zTAeHzwc9t7H-MweYb0p-SRLrikO5_4xpWaAC8rib9jMgYezagYHPpDF1s7qlgntNKbki3UxHcRg5dgg4_rU1DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/24319" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24318">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W92GiI_y8BcaPXdBxdJ5h2Kn8cyBaN1W1qTOdo5jyVonUAbdyrqh3MNKFVhLf3PHXgLERs_cRHHePCDUTPjVjyQCR5mRapv__kgZY5uz7RFzW8K9UbIK9eM-wjJ38kNnnrI3H-CrWlL8BOqdJ8N9JZtRWM08B_x2RytExYgpc0mTTPPHOPK_8wR_r3zFhilmQJUYRpfuOC60zkJ9CfyIa9Prnby-jzeC_CfZL_RqK95wAtHvk3RGQCFouexJCM-GUvyyrrBsm9WKZrM1G5zekRaNmCuMIauFk3NAk514tmUz2hLjqyaVz2zyug6rNLwCQ7yCtMpWgpwaQTbuYiojwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24318" target="_blank">📅 22:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24317">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAxKJ5G7UrTfu_XlPxMA4mIZcoHC0N45-wnfqXI2nw4Sf6vGBkFXyztqwdLsQtWu6PcXiAxP8VEbAQrTQleB4EIkaBszb5p5amSfOeB0wxW3maOXLzgy-92LgZXzNgTWGywjnO7JU4C95JPdfFOJRvb5uBJulCGYwcx1M_-YXFJvv5VV8cKxJ1k250BScg3BH8wE6iHkkfkXWxLONiUCDm5suggddl54z84CIpkkyIKuZWKO6JCYNDeiInzm_cjNE4Cz7rJlOVL-5oOuy5UIIW0JDuwhDqrzsN9Ml_SCtmuvF6LI95rE4xMurmAczlRUcHLn6sf5AgWZVjwszjvk1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
اگه‌تیم‌فوتبال ایران در پایان مرحله گروهی صدرنشین بشه مرحله حذفی به مصاف عربستان یا کیپ ورد میرسه. اگه دوم بشه استرالیا یا پاراگوئه حریفشه. اگه بعنوان تیم سوم بره بالا کارش سخت میشه و باید به مصاف تیم فرانسه یا کانادا بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/24317" target="_blank">📅 22:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24316">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f872bbf2.mp4?token=Ib0Czy9YILSjc593mJNyAySV4Fl-5K-0LgrYT5rAy5jTCH46QvszCp260RBR71Ynf1HRg8fav4PwbB-Cg65Ct4kgiPL9p2M3otaQuXVUgUgvuUqhgF7NQKWetdmeMIdX7nRiI6yWvzBp_iAPtJiTi_HYK4IPI16-Vc3PH7TUYRpeyJMfiIeENiOMCcHjdCNDoa3ZviMUq_0p3POGgnWhniCwkaAUWZ4eTsh7oWKVrnNMtKeabQRshDpRX4Q9TsIz3MDbz1Dw6FzLAEXC5zlVMar2UE1uDuyu1cUnNugEUtLuRQH_cKQ7ZGy9yvwyzHjsqcsrE8J59kINZNIKWokFbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f872bbf2.mp4?token=Ib0Czy9YILSjc593mJNyAySV4Fl-5K-0LgrYT5rAy5jTCH46QvszCp260RBR71Ynf1HRg8fav4PwbB-Cg65Ct4kgiPL9p2M3otaQuXVUgUgvuUqhgF7NQKWetdmeMIdX7nRiI6yWvzBp_iAPtJiTi_HYK4IPI16-Vc3PH7TUYRpeyJMfiIeENiOMCcHjdCNDoa3ZviMUq_0p3POGgnWhniCwkaAUWZ4eTsh7oWKVrnNMtKeabQRshDpRX4Q9TsIz3MDbz1Dw6FzLAEXC5zlVMar2UE1uDuyu1cUnNugEUtLuRQH_cKQ7ZGy9yvwyzHjsqcsrE8J59kINZNIKWokFbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره‌مرتضی‌تبریزی‌از زمان حضور فیروزکریمی در ذوب آهن: 3 روز مونده‌بود به پایان لیگ گفت تیم از نظرفنی‌اوکیه مارو برد ویلا یکی‌از دوستاش تو کرج باباکرم میذاشت کباب‌بازی‌میکردیم عشق‌وحال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24316" target="_blank">📅 22:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24315">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixBgIfj83bgAzZ1paW82OfhtEya9IzbN2jXO9MOaWMIBZ8o7TjkB82lwzNDKm0ljHlrg-sw-7iVdQOH7LxbYhqZpKVVpw_h1GKXqihvHEV-RJ9Q65nxXQ-Kwxai-ZQAJ2zVZDCTFnSmz5_vqajP_uzeefE_3P1cvrwt33FcsbD3mqKTq9iXEyelVu0Sc_EEXgWN12ITfEXFiC6CBnP7GogRJYsFc_IG2KGMhih2BdQMXlw7kU87B8y5DeagI8aDgTw9wJwK3megJvSmb23U53qXQDzv_jtidBh207SaZxHhpfui6ofzTtfBVCAIsjtfRByacP3xKBe227YK2l_zuIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇩🇪
روایتی‌ جالب‌از زندگی سخت و باور نکردنی دنیز اونداف ستاره کُرد تبار 29 ساله تیم ملی المان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24315" target="_blank">📅 22:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24314">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksMeBcoYEKB2r3qeOX_T6u12whTVgM3vfptUDhJ38CxMJqVyAWhE2OXR5ZCsPM5g05T1NdVusYeigdkhNpZxhFgIrLuYAiJ4W1b5mvoWPokQ4ltg3OMPYMINQrPtnLNJgRaMFsVpiSBrMjLcErQQqYaWXjxmGEFE9plpS9PirUZ8W9oTgr-h0YddSiAJzZlYhLqcQoDR2ZXhrlmj0MlHxPElwpbaaLKI9d0ezCGE8Ig3Ku17SqchqfY7-MkKwNMc5wPuykcjbxFJBiaxHvx54GvUvwy90Yubpk82JaHjFN8KcCVyKh7ps9_7K3ThdtQuNqAM-a2tmugSalSsKLEfgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇧🇷
عملکرد خیره کننده اشرف حکیمی و وینیسیوس جونیور دو ستاره مراکش و برزیل در تمام دوران حرفه‌ایشون؛ رئال مادرید چقدر مفت حکیمی رو در اوج جوانی از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/24314" target="_blank">📅 22:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24313">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXQ8qeF800XXU42IsSV9MSb7yteHj1CjP87vIKc-iA8Khck_hazePQ2qfwEx5rKI_aTHgX8-i4WzoBtQvqssuLszh3892tx0WYIYSo3fu79IXwnIWTIhe_KfeP9rsIkBSDu-eTMVRbUA1ZPgF2z7VnRpl9Cy9ZGfVZuShERjh46JNlkRYaAQifbIZB6Gm9O1hSDhmk3ID1yrq-aYoGPhkjhshyPiLbm8Jx_Z8Xt2hRmvLk3iI-FtLDyAUMN9jtBszJsjj8AzSOUC4qwJD54TeEjAOD1a7rY9YEyG0JUqbZfy0h4tlucdiR21CZ22-OB9EKXN7C5-eKFngO_7bxrw8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عارف‌غلامی مدافع‌استقلال‌تابستان سال قبل قراردادی دو ساله با آبی‌ها امضا کرد اما کادر فنی به تاجرنیا اعلام‌کرده‌اند درصورت عقدقرارداد رسمی با سید مجید حسینی دیگر نیازی به غلامی ندارد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24313" target="_blank">📅 21:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24312">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tV8cydw36Z7qmnL_kf6zWhGZz9UdYB_UflKCcQXwqYaOg0uoyYNHJgfYBXJuN3wSlphG1JT2NaNN5EWlMrR91fzp0CmLXGsKk-vu8nh_hpwOLDc_mwdtfu2FC-y85cwDGogH3hns1HHcgPFaPHpwDI5miMBkOGlGiBDiO5Om0OGAP8kCJTf1Rfg-BpL3eKK0H1o7Czxr0KL4TbP8PGaHIbDx36I6yy9Soh1eyMMvbjcd3lFLGABPdY8QbRgqhrDwaiED7tYVU7eSsiB1aXTcBMFOIaWToQrBZ6qfqLhQdSkx7FkdHbL7hc87wI2YuLJMM8bqzGho3lWNDp9hSlaWNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
موعودبنیادی‌فربعنوان‌داور وسط و وحید کاطمی بعنوان داور اتاقVARدیدار پرسپولیس و چادرملو در تورنمنت سه‌جانبه انتخابی سهمیه آسیا انتخاب شدند. این دیدار فردا جمعه ساعت 18:45 برگزار می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24312" target="_blank">📅 21:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24310">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rojRV7zZdVLPQl9fZhrIhaHEm7xi6Sat0c5Jh1hjwDn0-C_mRQc-nG0_Ju5h3fHKmUkJRPnhOP8em6kifZqZ5l9kRXf0FmUijiiaAWxTg5a1nYnoqf92Gayc7KpCD-o8nvUdYQKI3nCIYvarBdaAu5PkuEeRJ1l7s6AOnmOnrG6ZSxCghDebnIOAANbjwEtbIXahCtB2mdUPMEdvbzfTtwffClAVlU-GSNN7KYs0vQFu5sg6TEeFAuAX1v8WGmyqQBMAtoBuHv825bipclQ-TJbwUL1Z5sESGkXoZ7V9U_NB4WAZVAKmiylmwAvUlMtNpjazSaJx3U7FsrJTngcKkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aKGasngMksjbc2NPxSc9RU9YyQu4cTCfo_nsUdaLLOYov9Xdrv3dkTMWSRFbTJUhICsy9E7tdtCQLT0RE5OZuhMtqmlCubyQ57BTxNdRfATzDmAoRNKvYvtT5PF9Ips0LyjJAnW5W2kf068rx9j4btiFizERu9Lbya2DzLrbvzkFbW7spBX7wramGdYgDz5wmEyDHDsGViDGRFBhTnpnNjsaJxRrPiTuhmixeq_BF0G_5ou7g1VXRgY1fpt_4Hvsbj-PD3YdMWnaByGmip-jWKee4V5w8UtzeggdgSnpV4WMnG7Z8LIqswzOBMN7vzTCwnlQgiUGIBlTLjd5qOJ1mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
🇧🇷
#تکمیلی؛ بازیکنیکه‌فقط برای کشورش خوب باشه ولی‌برای‌باشگاهش نه رو دیده بودیم. بازیکنی‌که فقط برای باشگاهش‌خوب باشه ولی برای کشورش نه رو هم‌دیده‌بودیم. ولی بازیکنی که فقط برای یه مربی خوب بوده باشه و زیر دست بقیه زاییده باشه ندیده بودیم که وینیسیوس جونیور…</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24310" target="_blank">📅 21:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24309">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juW4VxL4wGIyWLF3PRGrYgU7muSEbj2T5kkmybamz372PTYiyvRAZQze4wxncbeEYb0HWRzZoBM6ygdFrOpK45PUZXXfyS4QKBhG1hqZ-4qoCMxJvg3ylq-o5PWJ6izsAl6PCcnkhJvB0n80PCUrspKsSLX5jK2rcss9nAlJPiHDDImRqpNE9xGWH8VjPni6tbm9hYMlNaNgWNIbLb2pIx8a5dGgNgA7Ju0l1gjBavaXODJmd4wPRIM4Ee9tFbwerbV2ABUes4jgU9MV-PWf74t-9YXW-ROh20uzsjGPLNTerTf7Nz-iENQ51iyqXOdN3H7HOEzsnnjs8evay0fYjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کواکو بونسام جادوگرغنایی: حالاهری‌کین کاملا آزاده که گل بزنه، من اصلا دشمن هری کین نیستم، خودم بزودی بچه‌دارمیشم و اسمشو کین میزارم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24309" target="_blank">📅 20:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24308">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0pwdKMP3jOmCoC1OjXDiue4dHSAda-8NDYo7WoTTd-5Taw_y9UnRykGYdos4esuaCofPYpVxpDq5QLG73ZM7Skh5CmpC7qARjUKPYdNBwlpHcGGyW4HG201tg8zcH1VMnmhm3W4IrCynVqLbC-F2Sh7kP5nGeKDeHx0TNKhdIOSBs7C6ruejRSpLACKaMV5BWRen05NNRrHBQfJKnI8SRrJSyklD3BaC1N5ULxo-UT1Z4b5h-Rw6z7u_YNbBNpnRA4ed0xfXuWDPLOcIXcz6PpIPTD_XcJ20VaV1EaZo08wM_lFCAHMnCr9glUYLA7G4wlAMjBesvW2KY-damvlOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛ ترکیب تیم ملی والیبال ایران مقابل آمریکا؛ساعت 18:30 از پرشیانا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24308" target="_blank">📅 20:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24307">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhMs-OLVLHRm_d-f_2D5eRrgZoIVc5dwaRcn4rgq5I-sqFVAFRHeVi6KRkwiCvCrhLCG-DJjFmu-JRZk2nt7BM5vIxrNQi3TnSEwdJ6qD81u-T4fxztX3TR1g_XHC6RDwRGTPjMGT8uwFKkdOsBuTAViA2CB2RhcJhFXw7ySITo-nRC2N6tIMY3DQ9vUy4ul1BiScXHNmXFVJozNm_lKLB844vl3TWD1pe4Q5A3aS9dNyC-7dnqXJz06dvqRA7BzMUiGLUCRJNJd3qXCFvwId6Kiw7kRfmgHc4gAPdrHlB8eV0mX8NjR6El300dck1zWxnqVvLTCzE3WCueI-rKE3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
عملکردخیره‌کننده وینیسیوس‌جونیور در مرحله گروهی‌جام‌جهانی2026: سه بازی سه جایزه بهترین بازیکن‌زمین؛ بازی اول یه گل زد و مانع باخت تیمش شد. بازی دوم یه گل و یه پاس گل داد و سه امتیاز رو برای تیمش گرفت. بازی آخر هم دبل کرد و تیم روصدرنشین گروهش کرد و برد مرحله…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24307" target="_blank">📅 20:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24306">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/992e363cb7.mp4?token=KFFdBv6R1ssnDn37Bit104v7AFmlNYayCBPEcG5iCds74ZTYk25vebjLnIrL7cwlFhxgpbXspvLKO-edQAjoOQlEbuCK72pheL925hcq9BOyrWW3Q0kf-XdTGFeZLruEvCmCRFvEgaGFTgWqUTe9A7nTRPdoxTtdp4M8k_t6QX9apezkgvWrzSNHb-zhJ-DRSDxNNb4-iOhTF6C9JJt0XFwhjdePXTU3I0aHq0ZgDdtaWO_-88Vb-tjzTLwVP4lEP_iWz9e18hrvdENz_ABTxWIRioLTFaTnV2BmWsNZNwqphGsgFpY2HvafhdBKQf20lowsdJD5IT1pEKZpYrTFsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/992e363cb7.mp4?token=KFFdBv6R1ssnDn37Bit104v7AFmlNYayCBPEcG5iCds74ZTYk25vebjLnIrL7cwlFhxgpbXspvLKO-edQAjoOQlEbuCK72pheL925hcq9BOyrWW3Q0kf-XdTGFeZLruEvCmCRFvEgaGFTgWqUTe9A7nTRPdoxTtdp4M8k_t6QX9apezkgvWrzSNHb-zhJ-DRSDxNNb4-iOhTF6C9JJt0XFwhjdePXTU3I0aHq0ZgDdtaWO_-88Vb-tjzTLwVP4lEP_iWz9e18hrvdENz_ABTxWIRioLTFaTnV2BmWsNZNwqphGsgFpY2HvafhdBKQf20lowsdJD5IT1pEKZpYrTFsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
از زیبایی‌های فوتبال و جام‌جهانی 2026
؛ وقتی میگیم‌فوتبال‌فراتر از یه ورزشه دقیقا منظورمون اینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24306" target="_blank">📅 20:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24305">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aW29YoGDopJNM9NJjJHkoXQXQ3acjrFHa9fS8TOeFwBTOAsO8iZzFTG_F33mQqEXycE8608YIS1dMuHKUUYl5Po1hp0Sqv7hLGeygnmmDZE_nYhUc566CXMAHk7bQBOn3wqLZVnkYloFhU2qWlRzH_1HXqkPo6Z--BcbHyW55uBb1LN4-xYUyqYBV4QZYr3gGgbUzW2Eg6-4RwNFYu70ScIn_WxHQuScZZyT7tWrTyDCDF3WEv2epjcbwvdvsZGUFhhBkilQtIiQoBeBoPvaRipmJptu67FvwlgmjPhEyC9b6U9_mCK--W_GOuoeIKjpPZberCNLPtBfQbOVHJcdfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کازویوشی میورا 58 ساله میخواد رکوردشکنی خود را تاچهل‌ویکمین‌فصلش با فوکوشیما ادامه بده و بار دیگر بازنشستگی‌اش را به تعویق بیندازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24305" target="_blank">📅 19:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24304">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRVZBlcgVEGYPWtSanIoH1tivPeTiLzjJslOPcKt_9HxOs32Ha7vlke5lfxI4ZD1TVOgof3oDJZhnrE-q2pMrbMmhtr_LcwXulT_b5hNYYr-cn0MH_264bjW0DjKMoSk1YvfPM3zHQ8DSjG6HVTDQX7nUbX4vtFqAmKm9kfuilprv0Gb6b1Y8X0NH8-LjH9wDlU6e35m2Oyg9cCkQTM30nbG-vA-ikL76qGPHwL7d_5fqVn6XGW84WDHN67KdY8LmhAm6yMJtwWw_VKYzxTJA0nFT_qlWLUjhKY_O96R2ioLmI9bsXNug1efb3FIJRob3h-iBEZ1V6M4Dtourq7ZoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ رونمایی‌دقیق‌از رقم‌قرارداد عجیب محمد دانشگر 33 ساله‌باشگاه‌تراکتور تبریز: فصل اول رقم پایه قرارداد 85 میلیارد تومان توافق شده‌‌. فصل دوم رقم پایه قرارداد 105 میلیارد تومان توافق شده. همین هفته میره دفترمحمدرضازنوزی رسمی میبنده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24304" target="_blank">📅 19:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24303">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5r1kxWpZe2SSk01kLkiCcKfqvM0palaW3MZftAP1uz_HBuARH82dEmzhUudVEcXUw6yMVQvr0G7uTX2MTNN98jaBPeCF71yv0hvvdC2jvQV_Us74Wjju6av5X4jzeXO5McqSj_bRO25NoGO3eBE1c2GBdNwnqvLQjPx4d1L-RVmulowAdbj0-4bPD24Cb_4PYrpZnOp9jVabfXlBWNK7p7GKhRa533JqA3D7YvXlusx51PyCZmfDeu1oBU5lqK-0bUv5lTRWco0q2TNytdiOb9insk_cYG92krbsWmivBMTrg8eOXaxuCdJgI03EJ66XisqtQSwqWqWZigY7Wd77A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇹🇷
🇨🇲
#نقل‌انتقالات|بااتمام قرارداد قرضی‌اش با باشگاه ترابزون‌اسپور؛ آندره اونانا گلر کامرونی تیم منچستر یونایتد رسما به جمع شیاطین سرخ برگشت تا مایکل کریک نظر نهایی خود را در این باره بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24303" target="_blank">📅 19:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24302">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895e84fb44.mp4?token=Q0qb5dDU_whrbnCPXZ9-9YfD1S1ymPdw3ZHI4eKtegvsoCS1OkxgrVVjCKx7BXh1h0vDPswWheXQHhCcZ0eQ_Wj408k495GQPrQJ2Iz800OI5gI4TxKtCtPzQzUTN3rAXsy7w2T_kB2HHPEY4dfJdoVzuuaYkKxBFzNrqXM9MbUJDLXnEVJwMl-GB_xShX1sHPgAjGpTFNYeG-w0Jqni3oaAYTYeNY26uySw0Ok0S26nE997qan8yt5tNr39UHM1F6D31LRvi5_v9b8czs7PjzLXfm5KIPTUNmEWn0uBm29lNXiR-iUeABbo1jAQiegKKUFaH_ssg8otAKApwa2HJVCOZhpRVWae-yE038wD99m7_2u5TMtryrZekoUFO10gFh4rnwjgeGwX8d6h0PvWR1tGUt-lvjyBfr_zN0MyEl89K5tYUH64gQd9ty6QCKuclgSF4xFp7iFpAEr-Mxmm5l6D3B2KZoqEV8EnnRGpz5eKP58gUMnENs8ZXt0Qs8KFl9XgyfHMbHRapG4lCuT8rZXbtIv1Xt2nez5SBax9VqLG745Pr7697GYJczgnyZMsd1QeMnDMREbRXDUnCEvSxDve0a8NOAyWDyHa-r9ilGG3aFEglXiwZb8tYiHFwR8GcBej2-u8IwmKLZzGLFD5v_6JVpemfyPubL8rXyBplEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895e84fb44.mp4?token=Q0qb5dDU_whrbnCPXZ9-9YfD1S1ymPdw3ZHI4eKtegvsoCS1OkxgrVVjCKx7BXh1h0vDPswWheXQHhCcZ0eQ_Wj408k495GQPrQJ2Iz800OI5gI4TxKtCtPzQzUTN3rAXsy7w2T_kB2HHPEY4dfJdoVzuuaYkKxBFzNrqXM9MbUJDLXnEVJwMl-GB_xShX1sHPgAjGpTFNYeG-w0Jqni3oaAYTYeNY26uySw0Ok0S26nE997qan8yt5tNr39UHM1F6D31LRvi5_v9b8czs7PjzLXfm5KIPTUNmEWn0uBm29lNXiR-iUeABbo1jAQiegKKUFaH_ssg8otAKApwa2HJVCOZhpRVWae-yE038wD99m7_2u5TMtryrZekoUFO10gFh4rnwjgeGwX8d6h0PvWR1tGUt-lvjyBfr_zN0MyEl89K5tYUH64gQd9ty6QCKuclgSF4xFp7iFpAEr-Mxmm5l6D3B2KZoqEV8EnnRGpz5eKP58gUMnENs8ZXt0Qs8KFl9XgyfHMbHRapG4lCuT8rZXbtIv1Xt2nez5SBax9VqLG745Pr7697GYJczgnyZMsd1QeMnDMREbRXDUnCEvSxDve0a8NOAyWDyHa-r9ilGG3aFEglXiwZb8tYiHFwR8GcBej2-u8IwmKLZzGLFD5v_6JVpemfyPubL8rXyBplEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇩🇪
روایتی‌ جالب‌از زندگی سخت و باور نکردنی دنیز اونداف ستاره کُرد تبار 29 ساله تیم ملی المان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24302" target="_blank">📅 19:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24301">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXZ-kdFqnbDa-o77646pVqtPEW6yIq_5BB4cxR4IYfGyuID0zXaMT-7TuJQB1OBcFcqahWo_ttZYTxUW9kp6-1lLsLj0xyhVFZSlEc5tMVfzof82vtX9c10NMf5neYRB1Qbl3I7ct9yQ5oQVPkrj8tm2txZekySO8bRv_c6qFHkMmPyP2Q5alBInQ4RXqxFCOXzPXzbJVpdhn8JVUAaxzRtRF5bYA13uyl0DRLouv4n3dAS3bJx2B2Xa9oWgG82GiiaKNhXeBPJPEaCC1Ws9DAqhzx4DUkVkjRmXKT1DjnP5wSloZAQ7a02IhC_Fckth4YQBXVovgGD1EKJUJHfyjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
اگه پرتغال درهفته سوم کلمبیا رو ببره در مرحله یک سی‌ودوم بمصاف پاراگوئه میره، بعد بلژیک و اگه ببره دریک‌چهارم‌نهایی با آرژانتین بازی میکنه. اما اگه ببازه یا حتی‌مساوی‌کنه انگلیس، فرانسه و اسپانیا در مرحله حذفی رقابت ها در انتظارش خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24301" target="_blank">📅 19:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24299">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7-RJJcyEvTE1X3Wti0ChK28vWry4AyaKLvg0O0Nc8m2xxppiInF4TUGqkkgdno-5xkGUwQiqXVcdqB5g0_k9pcFINRdMUhF21-F-aziORnByRtJT7M_mNdbfyCT8-OaOevNyTsMwUTtmLllE8Bcqlz1Mu_7-LZ9H3LZrU0aiAaAApL3hNk1jruNxPw-tGpSZtY1jB0PCrTehZxSM3RW2a_IGesfx0YRqseYBh-op5unTrUEFM3l_bjIk4QtU7nlskgS-j5D6DuXcw7MX0Q-5_6KzkovCoBwJa1JKURIhuKfxZWGdqNS8xByyhdIngOgpWah7uU3YCoUevJd8icmzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
اگه‌تیم‌فوتبال ایران در پایان مرحله گروهی صدرنشین بشه مرحله حذفی به مصاف عربستان یا کیپ ورد میرسه. اگه دوم بشه استرالیا یا پاراگوئه حریفشه. اگه بعنوان تیم سوم بره بالا کارش سخت میشه و باید به مصاف تیم فرانسه یا کانادا بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24299" target="_blank">📅 18:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24298">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgQhtPXTvqJdV8m-ClTZMnwVo8Y2xfYx19YtEcRB7eEzofkwGFBEsKoO-Tu_iHnzzsLdbnsrzBL6Gf2ZVITh7QDE27Kt1TCd9ucech9-koWeqZIQiAH2fkLX3ZfDKsqaPyV3EqfA0Kx-jb6-T7VeFmj-62msfIiFiRBr-hQibs8F9QNOwKfyp0UqK5q9zcDaffj8JR41ic5W_xLGXD-s19KRHm7LvOS5w1hkMoQAuaTe6QgR86UaK8tzx2FY4LVsDrCa2vO6-xm46vdumyWikErFlF6Gv5PtPO8e0asaOB0qu6ocTXWs88AjTSssPSFnYpxyZVXLy6MHJUwrjScGlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیماریزیو: رئال‌مادریدمیخواد بند فسخ قرارداد 60میلیون‌یورویی‌ نیکوپاز روبرای پیوستن‌به‌ تیم‌های لیگ‌جزیره صادر کنه. مورینیو گفته مشکلی با جدایی قطعی نیکو پاز نداره!!! دقیقا اتفاقی که برای اودگارد رخ داد و چند سال بعد رئال برای جذبش اقدام کرد و آرسنال گفت…</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24298" target="_blank">📅 18:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24297">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtVise-uCV9wDJSZu0BOf0PJx_kPYWcm2jicu4Xni4MjrP7gwY_cI3o8pMTmSO_QS0qbTEiTVYT-PVDGXV8jcC6zYer5pi0JtH7Kq9yo8LakmlxyFUfRIz41zlPOxdoa4cTkVUWbqwaDvt92B1tHOnHrvbMfjqf2t4qyxrn1NiQ9_tWchPmn96mJbRjSEoAwBRlR9c1mrwy68YhvZRd0A9I-URk4h4lQiGfotqo5ZUcJ2UX926QYRNwDyntk41ZWXHhXpSDUDScbJ7yGianCG7lVVTdBjyrfylNJo8ytPONZIDQyJgZusXCEXob8clfD771BOE9wvSF3eiDhSakoxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کول‌پالمر تو یه‌پروژه‌دریایی تو صربستان 10 میلیون یورو سرمایه‌گذاری کرده ولی بعدش فهمیده صربستان دریا نداره و ازش کلاهبرداری شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24297" target="_blank">📅 18:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24296">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2rYoU8UG8IVnxnGWwz3mCOp1XAd9JuDK9gLrzCvfZb9MNWQs3xi_UrOdy9pNQmO-KwATfl5fxy7N7Vjdvbq1u74k9LVlPtJ9LniemUM0mHOaa0Nagghiq0tnBXwnVfU55v4kKEaNuaZQa5rH651tA4M9zN9_GT1Tbu_qT9EhlPurHyyy2Z-IK1v2TqqHT_7NBh1n_36moKNrNqdSpZS7KWF_x4lDAoV6ug5ZAnoD3KPK4NpqBw0X26ljAuUDevalH56bpOJT-iFJrqSSCGZkZ1YLMSm92TOKWTWuPa0g3gxD5QQ7w19uKQLQyIITruxHtiuyW7r1hxPbqVxtDcuCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛
ترکیب تیم ملی والیبال ایران مقابل آمریکا؛ساعت 18:30 از پرشیانا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24296" target="_blank">📅 18:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24295">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCdzUHvFBCbQqvaXqgnu93TnE__T4R6kBiXkHtnWtFCRcMDAZXq89CPng61W-gd2Gj9wBwmZsv5FykjJFRFS_sUP-Re1q_zrbgNX0LfSuEzHnQdSYFe9D36zaW33KIMuyYVdRAHlBHUqKqHuPQMl4T3qxUJJtz-_-_iaHcMxvAiXhuaxGOhFEEPCiIDfv1LK7DZIQuNMPS8qlG43iajbkZ98zWms64vusABP3ENE5uBSsDA8crddNXB7N3ndTP3PJ460eDyFiDy9sASV_3cJszVuFxKbY__iU8slWAIDdb7JD3Grd9pBGO9XUeJz-Hys0fMd8qRxdxX_fAHsSxNnCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امشب‌بازی‌برزیل و اسکاتلند درجام جهانی برگزار میشه؛ تقابل این‌دوتیم واسه ایرانی‌ها خاطرات تلخی به همراه داره؛ ساعت ۰۰:۳۰ روز ۳۱ خرداد ۱۳۶۹؛ زلزله رودبار-منجیل؛ یکی از مرگبارترین زلزله‌های تاریخ معاصر ایران در شب بازی برزیل و اسکاتلند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24295" target="_blank">📅 18:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24293">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i0Z3x3abqdCSDInS8jmAvQnp4Jsp8c4mDpXYrVtHYLjSgArlOWjzhiMJRqA5Ld4WnnN3PLeRNq6H3w6Czzd4w-GFAAfqyiPMWxhDRiPI5rBnxHXmx5gAy41cwzF98vozLuneds0nuntdYR7474_uAEVhXtAsq03RgSeGMBZKd1gRdCzv3buLgLQCWvWrO2U3mClVlcmCxAwB-zdSOy2m4VZoE9UCEgHYI20ME54UxjE6Ygak3VW5GELm3g9H_njLOQwCxhXvpMySbDDi_3Ncx2I_wY0iVXaHDe95opSvJHuwZE6vw0yH9eEB4U3iD7Mahc7gW7RyPMM011eF3N-vmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gYc0uaWqNPZZ4748y4zQrivOJHsQ7QZVQNA8YgpnJalzpdTsD7_xnN-YXqxoWBt7dEBkqmNqSf1RjhEOGSzF2xAQuzWQiBXVrptVb7IsFtEhD6XB_Rz-kFIBqasUGiHeJOjM-qPbsfBleWBtvayWm6HJ8-Wiv6aEEDAzo9BzqdUcI7CDI0UQHOYFDbq53MSLKORnk3feuTW2-NcXRB9zxpttPy21uWek1oXB4EqbFO352z7TYhIlFQ8R_YIBH0u7lVnlgw2R3gQbyzVkCmTAyhTshnh3cfaZUBylrjqDN5u3jTQkk8YMUzHvG7LqmZRnS-COSf-ewCReViJWl16HWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
"هبا عبوک" اکس اشرف حکیمی که دنبال ثروت اشرف بود و بعدفهمید که همه چیز بنام مادرشه، بایک‌شاهزاده قطری که 2 میلیارد دلار ثروت‌داره رسماواردرابطه شده. هبا و شاهزاده تو جریان جام جهانی 2022 با هم آشنا شدند، زمانی که هبا هنوز همسر اشرف بود هم دنبال ثروت اشرف بود هم بهش خیانت میکرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24293" target="_blank">📅 17:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24292">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlYWI5f7k9Cmc-F33IrrqSUwaaFvwB2qZT7PhH6p-Jej052TB4R4Rv9Ys5ZN6EbCKBYRzzhxIyKa-O0S1A8Fh-bwizeELB9BcAD5yRn2HrDrXlYR6nw9V0BmOHK20j8d_1p-cJZUvDKSHg4giVmjRJ4mijzeWoEWiaL6z1ZuvhrIu8-C5si4CmNaRywrJDXcvcaggEFYGU_oTMCaXWj_i5xMqxtm5moY0YMKSclNDd2K6-1EK0bDx6L-vv_l_5QqarLI73c9HE0cLTV09-4u14K5hEhYyl4Idr0uJwNWp_iUB0kMgz0GwcVqzccfuiYDXI22cqttxowl9i4NzsTKwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24292" target="_blank">📅 17:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24291">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOC34GmtxqUf4dO-zHnCuX04q2dwOdf9mY26Xpt4luHRKuCoF0LPWAaogcfH_v6B4A0VjQaXOUjxJ6d4Exk8QDralQ5M4q1ylYvOFbyjbg6xCn-r5-oyu-JyjnqK0m_qnV0qrq-KD5750l9sdhb1xcGO0_Ak6bx5gqDPLF9KnHDovKpXimKiOHffaLxsutlNFA_FwdJ6X-tcynreHz35DlMr7DAdurTbX94gs5As4di8NSqjDOhST3RpNZ3GZJBTYgRLDE_tNPMCTQNI4B90eT7tTv36_l5NUOY9dW5M4Mrx6uJZhvttkfux4oYSw8jJub_z5l-F5ZzIg3U7aGYfxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
استوری اوسمار ویرا سرمربی فعلی پرسپولیس درفاصله 24 ساعت تا دیدار مقابل چادرملو اردکان
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24291" target="_blank">📅 17:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24290">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d5e9c8b86.mp4?token=oTLyZS6gQnOpbxTvXeOZUuFJ9Cx8LOTyyRsseQcmxn-8iBpWIKBkyPLrdJy3uD499ORx4Cm7GduRBlgv68tdWdw3lUIAoQC4HoSeXZ0IDSTimQBXbGw8O4-o9un3rqdNqUrDfcISVMmivec-L3gMjq4HdxS8oaoPX9jM2zGEctI_8pHg4sRgOlr8F_v8XL_Y57miqQZQvkhMVP93GIjGEDlKjr0ScH77ACQfprJNLmSTCvTAnDSh3UU79iR0KSTvZE4qClNX8K2qf48gQQwIpoq94gQFHG0B0J0MgbhoaRvyEqdgmw7nqcnyb2OBQ_5dhdVggcUqgw-cB8bZv1MXTXkz2nwZSokpPmCixthbuPx0R4khSph15LOj6SOw_PPIl7vK_saGO9EZ6Du-TIT4MNwhWYvzoQ864fSxdyW40xFyHJCgnOCLYGIOaIsKsPWsMAfi0Kxq3Pkl5DwSRljJxoBOf8KtWRr7Cfia-4VFy2v1WryFkzw5JQpnSVIc_FKwPYX1Uioz7Jk6-NRghws3G2GQtqK47ceQBxkqfilP4moQSPLzB6kg5B4scmBcF34qhD4jrC-qm6fx0upM1pi-y-BviNIHBZko8p-hgKJa-_BYenR_hHhCj6vZ6bkn8DI-RNIi3AYVLB8Y9z7rW_3sltj6FelSyoGQ2vzhz23bxZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d5e9c8b86.mp4?token=oTLyZS6gQnOpbxTvXeOZUuFJ9Cx8LOTyyRsseQcmxn-8iBpWIKBkyPLrdJy3uD499ORx4Cm7GduRBlgv68tdWdw3lUIAoQC4HoSeXZ0IDSTimQBXbGw8O4-o9un3rqdNqUrDfcISVMmivec-L3gMjq4HdxS8oaoPX9jM2zGEctI_8pHg4sRgOlr8F_v8XL_Y57miqQZQvkhMVP93GIjGEDlKjr0ScH77ACQfprJNLmSTCvTAnDSh3UU79iR0KSTvZE4qClNX8K2qf48gQQwIpoq94gQFHG0B0J0MgbhoaRvyEqdgmw7nqcnyb2OBQ_5dhdVggcUqgw-cB8bZv1MXTXkz2nwZSokpPmCixthbuPx0R4khSph15LOj6SOw_PPIl7vK_saGO9EZ6Du-TIT4MNwhWYvzoQ864fSxdyW40xFyHJCgnOCLYGIOaIsKsPWsMAfi0Kxq3Pkl5DwSRljJxoBOf8KtWRr7Cfia-4VFy2v1WryFkzw5JQpnSVIc_FKwPYX1Uioz7Jk6-NRghws3G2GQtqK47ceQBxkqfilP4moQSPLzB6kg5B4scmBcF34qhD4jrC-qm6fx0upM1pi-y-BviNIHBZko8p-hgKJa-_BYenR_hHhCj6vZ6bkn8DI-RNIi3AYVLB8Y9z7rW_3sltj6FelSyoGQ2vzhz23bxZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
اسکالونی بال؛
تاکتیک آقای لیونل اسکالونی سرمربی تیم ملی آرژانتین که به شکل فوق‌ العاده‌ ای هم در حمله و هم دفاع بسیار عالی عمل میکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24290" target="_blank">📅 16:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24288">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOqvRh9k540kzKOL3G4cicVwQI1w5C2gmf6wfc-_nDPMARYTuI4Ag9eMC3oi23wuzUVH_Kj3UoQMpGU--XP2LUWTG-4TLNLFrjgPuGSuJ-PASsV1zw1Hr3_-E8fNugb1EdGO7BqmRLLa1-T2Rkz7lafeNk_ngBHXTljAyC4l9tfcOcnrWzHT9vGEZyuiMUjUVLulDU2zY3wvN_OriyggZOmOnYuftxNTdtkU7GEvxyCbJWL92YqmC-CRMp9ltmiIKDBCDgtQ74_hBe-njTi5Fuvj1QJ4gedAVEnfzJzqViooR-RSRKEK-f5l-2Olm6G36xUlMoZD_D_-jmVNyUwSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبر مذاکرات‌ نهایی‌ باشگاه‌استقلال و توافق با محمدجواد حسین نژاد که امروز اکثر رسانه‌ها اون رو کار میکنند. 10 روز پیش اعلام کردیم که باشگاه استقلال اوکی قطعی‌رو از حسین نژاد گرفته و فقط بازشدن‌پنجره و پرداخت‌رضایت‌نامه او باقی مونده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24288" target="_blank">📅 16:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24287">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fe43357c8.mp4?token=cEwvRMK8dr1zfwqyOi_5-Lq_HyVRQ6xndSR9rqW9yLtvV01eLoXnTpaf0E2AkwnEFNu6dynfSbp7-UyMZZ3xW0AuLRGcccjO1kz_eZvQqOGu2RL59NFFGuSmwWQoyS61Tu4K5gKsgXCdPutpavqPb15MiwBPJWS4s5-iXKsHHwz1vakVyQOTCHkSlbguNkVad2w2GZQ0ZC3qMIFM7MBnd_BSfy-0eWb8c_U6Tueg_rXcIy1BxJj_4gsgv9GbsSwydcLpaPnmsfdZPi7ZY-1EM2f7E53wPedaBMBIuGi6_Iu84WwtnMwoo1Ra3uy21z9o9bkc2BVIivm3ToLDVkI-lRJ9VIlJbp7H0rb0hDWpnwVtJKHDrRc1-4_Zit02f9WSOBsmwmIShmjl0F2tmu9kwVj5hTUM2gIzZ-LrxcSZfXkBAGy7FM4P4jMIE76oXw6GRJjBrxYXPUI33pirrjQzutQ5w5Qya_qIAwQH5xALuTIYM-cErVa933t4WbcDLb7Y9_Nk4AoVXbb5vm9hRlVfk2eHcBe_BjIWw4as0-Vw-2C0lufWNoqt5b-08SFJ7Nwwc8K1KyO3gf-_Jf6lGPMXauLYePGXgRfWhay7mpzP5FoDndemE8BwhAxve-kPb1KXUHg6iL0-tulXvM9DNEfzx_OuA2BD4UmlJjODQ8drqfU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fe43357c8.mp4?token=cEwvRMK8dr1zfwqyOi_5-Lq_HyVRQ6xndSR9rqW9yLtvV01eLoXnTpaf0E2AkwnEFNu6dynfSbp7-UyMZZ3xW0AuLRGcccjO1kz_eZvQqOGu2RL59NFFGuSmwWQoyS61Tu4K5gKsgXCdPutpavqPb15MiwBPJWS4s5-iXKsHHwz1vakVyQOTCHkSlbguNkVad2w2GZQ0ZC3qMIFM7MBnd_BSfy-0eWb8c_U6Tueg_rXcIy1BxJj_4gsgv9GbsSwydcLpaPnmsfdZPi7ZY-1EM2f7E53wPedaBMBIuGi6_Iu84WwtnMwoo1Ra3uy21z9o9bkc2BVIivm3ToLDVkI-lRJ9VIlJbp7H0rb0hDWpnwVtJKHDrRc1-4_Zit02f9WSOBsmwmIShmjl0F2tmu9kwVj5hTUM2gIzZ-LrxcSZfXkBAGy7FM4P4jMIE76oXw6GRJjBrxYXPUI33pirrjQzutQ5w5Qya_qIAwQH5xALuTIYM-cErVa933t4WbcDLb7Y9_Nk4AoVXbb5vm9hRlVfk2eHcBe_BjIWw4as0-Vw-2C0lufWNoqt5b-08SFJ7Nwwc8K1KyO3gf-_Jf6lGPMXauLYePGXgRfWhay7mpzP5FoDndemE8BwhAxve-kPb1KXUHg6iL0-tulXvM9DNEfzx_OuA2BD4UmlJjODQ8drqfU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇬🇭
​​
طرفدارکوچولو و بامزه غنایی‌که با جان تری اسطوره چلسی و بلینگهام‌سلفی‌وفیلم‌ میگیره؛ گفته ازکی‌روش میخوام غنا رو قهرمان جام جهانی بکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24287" target="_blank">📅 16:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24286">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3mQ792YEA0pkcdmvmunB2re10WAVd72rRLq1QeBCHE9ASQ3nMfYC_R4kpZJxTcOjDbbjdBn7C9ToeJLtI3ANntLg9D9GkEIaWA3QElKfo87kN6qDWOoU2GcYxYvhke8kiFv7crZ75vkn3zjmz75y-AIMjuhxhxxbF8FnzPFr1-FKy5rvMH2i04419PIFiJBOwiPokJAMEB8MwlN8WuZpF53I_W40FjxTTAs3HnkMjAh_szex55dQjNqODU1ksJG0DzMZGBmF6teAWL73B8PzUJxvoIYHrdnWQ42zLS9MbXiKq-yNXyCu4USKSeU0mz10-SI_YutH0yNSM6rDNGcpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#فوری #اختصاصی_پرشیانا؛جلسه بین مدیران‌پرسپولیس و اوسمارویرا برای‌قطع‌همکاری دو طرفه به‌پایان‌رسید؛ اوسمار ویرا موافقت‌خود را برای جدایی از پرسپولیس با دریافت 900 هزار دلار اعلام کرده‌ قراره بزودی باشگاه‌این‌مبلع رو در دو مرحله به او پرداخت کنه و قراردادش…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24286" target="_blank">📅 15:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24285">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLxTvTu2vbWJfc-Ev3hkETOVfBBHsYnQtg-nXADbv1RFG11bWZt7kcJVwx906jH8fIx6ykPJjEDgSoHFxwNg_-opOsR5mEMRlg2b3CORn9M5bS3yqL10NiVJHk37vBpp5Jbmpm8qGLxBij-E6v5IvEDVIYk1BZr6959i8xOIYKXr9XXLiV84JfYJruHL_XXVQWmPeObBu7El0bqmvWWy4A7zYc-G3a9DywnZoFjXy7_-L6P6pgNfPiUkMKH29EmvPdut_dMzXb5YXqkCoCmBbzxVbzgtiPEKAK-rrLRYRIMkpLEokFRN2ZNAFQxQFsKAvSg523I2PZ2DVOMdHRYCAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اینکه گفته میشه‌درصورت عقد قرارداد بادراگان اسکوچیچ؛ بازیکنانی همچون سروش رفیعی و امید عالیشاه که‌کارایی‌سابق روندارند در جمع سرخ پوشان ماندگار میشن کذب محض است. سال گذشته قبل از چند دوازده روزه کارتال عالیشاه رو در لیست مازاد گذاشته‌بودکه بافشارشدید…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24285" target="_blank">📅 15:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24284">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfsU3wiEQHpUKH1egKoLQtZtce78wGZeaX88ZIvFj2kPIM_sPu0B2blOKt37pyGk4biFrdpS5KTOYYj8WiEKf6OMhEiQVLh6iKi-IAlP9tUbPPop9O6cryTHNXBHnJisLwHNZfQVq3hJmwOYi7CBdIjSbq0dCwOL85gLm-mLq4lN2_y0vYcpPgeC9nqe3S-Hma8mJ6DQa5y5puYtXc9DgagTuy-pn7mmzDz8155YfvisE0TbqJ7mZfQWynp4RYNEsRJ_BSM5UOoX0XzKJLlnBED5xnDxhp4Va2INJa7H1iIqSKtK9unSzOx06YVSorsatK2Hf0Ggj5JnZr2D7P3mZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌اخباردریافتی‌پرشیانا؛
علی تاجرنیا رئیس هیات‌مدیره‌تیم‌ استقلال صحبت‌هایی با مهدی هاشمی نسب پیشکسوت آبی‌ها انجام داده تا درصورت توافق بین دو طرف؛ هاشمی نسب بعنوان یکی از دستیاران سهراب بختیاری زاده به جمع آبی پوشان برگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24284" target="_blank">📅 15:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24283">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYwQOOapCRjnmuItnWqfNkVdgqj86RgsvlLeS6iBx9MSNed1IkIs-CaZqGE2Hs3QbM0OuF4mrUnMJE9l8QIrZqQfoAcK-Uoi1_fxPpXLFwVKmOBkKadbPAlG2WCNxYyOnOu_zn93W5MiLI_6uzO8nt5L2byRwlZW30Zyu3xV7HnOMW2qwzcyFxz-gLU5X2IYJXH1eX-hkkX-xhtaMwJzGE3PglQIo_aJGlX8wcvjf3w7JJmHEsQ3gS-w_lqbJd0HAQMqYNRIoCghrvT0GQ0iOf3TCFovhy7VSmkOh0qWmLROdOYoQDyRWT2K1ug4zo5ozKDZr0sHv0D-nJS0yRmBkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
یازده بازیکن برتر جام جهانی تا اینجای کار؛ با حضور رامین رضاییان و علیرضا بیرانوند از ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24283" target="_blank">📅 15:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24282">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epMnmKx3YPR-6UgdUFZXeVlhyREajnie2t9fGd8Q-m0o2tnvZbvmyXmRDob8yeY-4jL4LBnSpnsBdxyLzVVZIZPijBjOqYuNhrSorvtTDv9eyBWqdi7iQcyaYQtN0_stSxpeoh076rYxRo2EZNHGFoe2XZh1dB7GNXrU2FFcG0W5LB4T4JWiQOOrjBzf1DYvU8EFWPas8S5lrggPD4K-OLa_Sw-x5GNHNDEGd1t_1wLUE8MJcpIIE68zYpcyhQG37AaiZwXKLWQwwQZZeA0moDZCobKYmUlql87_BwNJ3Ju-T-DMGMIOH47BB1zuoRg4XPfX1ioyAqfs7c2fbbi5EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
اگه شاگردان قلعه‌نویی به عنوان تیم سوم صعود کنه در مرحله بعد ممکنه به امباپه و رفقا بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24282" target="_blank">📅 15:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24281">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afba99e55.mp4?token=WtsD4N2HruE-hnpH3x756qJ1E4Z3yFqMwNhfgNMAGyE6x29xc3hCLmBLLzgwoDUREviHVDW_dM1JalCds4YZ6AD32sWv5lkGr3qCneA6uLZZuMi9rotWlq3UsfiPJGaYNDRPHFW9J-cQb8GQNPwCYy6AOd9NZsSnlfxvby0huOEI5LA5DVlrKHWnD14dGmh5l0FqryNZ_D1Vf20Ia6vBw0U2z6d53WyHiQ7qYgZMGG0AHymNCDEQtouwQFoFUMirgx5wZpAlDY8p9QAjPH7n6BpipqF1Idk-d3bkVYh7GueQCBIeoA4E-bKMHNecw2bdc5d7TbwtS-4lfimDToC_uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afba99e55.mp4?token=WtsD4N2HruE-hnpH3x756qJ1E4Z3yFqMwNhfgNMAGyE6x29xc3hCLmBLLzgwoDUREviHVDW_dM1JalCds4YZ6AD32sWv5lkGr3qCneA6uLZZuMi9rotWlq3UsfiPJGaYNDRPHFW9J-cQb8GQNPwCYy6AOd9NZsSnlfxvby0huOEI5LA5DVlrKHWnD14dGmh5l0FqryNZ_D1Vf20Ia6vBw0U2z6d53WyHiQ7qYgZMGG0AHymNCDEQtouwQFoFUMirgx5wZpAlDY8p9QAjPH7n6BpipqF1Idk-d3bkVYh7GueQCBIeoA4E-bKMHNecw2bdc5d7TbwtS-4lfimDToC_uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
⚪️
اگه‌تیم‌فوتبال ایران در پایان مرحله گروهی صدرنشین بشه مرحله حذفی به مصاف عربستان یا کیپ ورد میرسه. اگه دوم بشه استرالیا یا پاراگوئه حریفشه. اگه بعنوان تیم سوم بره بالا کارش سخت میشه و باید به مصاف تیم فرانسه یا کانادا بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24281" target="_blank">📅 14:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24280">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbWKp1iS8arTsbIwZML-zVPO_zRBuNSTbLmpwpC6PmZWIe2c5eoKIu8wGp6Dh0B4D_zB5f9eS3Y0DSU0fAf8ywdHuAAwDEXm2YhFCZHqXsI7X7C2B_PcrHs6a6GngcR8sTVeqt4kadzslZ3hkghcdakhZHwxkbcHvwcOwhQ_33WXJtZ3PoGPqHlrf8y-AfR9OcGpWQ-mDcJZSzjcPUAi_TJj1A9XOA9e06lZPjj7wDT69oLbzi5nhX87McoZAF1TgzdjPSTzXC9L4CnEjMFAgoYfPAF4pZ_ub72nixStGdA9gV-FGKwcsus5kM8mxyUt9c22EH8PBUEBVdjO5zpPQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امشب‌بازی‌برزیل و اسکاتلند درجام جهانی برگزار میشه؛ تقابل این‌دوتیم واسه ایرانی‌ها خاطرات تلخی به همراه داره؛ ساعت ۰۰:۳۰ روز ۳۱ خرداد ۱۳۶۹؛ زلزله رودبار-منجیل؛ یکی از مرگبارترین زلزله‌های تاریخ معاصر ایران در شب بازی برزیل و اسکاتلند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24280" target="_blank">📅 14:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24279">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V34EMPstgKae0PkUFBadR5nU6alJyuY5AXky8VUjFN4M27z1_GHLnAp2OxpSVyEbFtqiawx4lj6TdL_lnwq4XunB1y2BnxEmht7Ibtp-AfxyLht1xdbcnTEeqKDvhSOHINH0zi89SXxn2kTeGr3DmnxEvq__x9aNQ61azpw8IfguRKnwToJzwdEGuFp7w8iV8tC1aCkDTXpQ5Bys3Fb5J2bbsVMqUURvENUe6VD1xrcBCPvai1flui8pRInswFPTKtJ12_yRoMSO-_tsenRGOVjbrR-p3Zg_vmRcM_ZgOQUGQ8XCULkkNgRi8SjCOnAHjJkmMes5s2m7vAjRaUaqsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
جدول‌گروهA رقابت‌های جام‌جهانی در پایان مرحله‌گروهی؛مکزیک‌با 9 امتیاز مقتدرانه صعود کرد. آفریقای جنوبی نیز با شکست دادن کره دوم شد و کره نیز احتمالا بعنوان تیم سوم صعود میکنه اما قرعش سخت خواهد بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24279" target="_blank">📅 13:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24277">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNo9ZHeX81guemx4Y7bsh5BTfJupSBILwOWBXBzYrqrRJ5G91d0RlbX-oMDtZTMllOKVQJ-PxUC9CcH09J7vaSfRXIb2Tk-bx_G50Q2RRwT8-p218HSQfB9ySojbjJ0uPMVZY5UcmeuaG5t1ch4A3uPXmxMAfF0uJRphcV-sky7vuK9jfgr3lBsrBSuJulmgEMaFfZE47s5n-r5-7RBY_3YaBpXEHqENCFFm3B9PYxofecLV0Y8MG3Y-uL8eyDBwgZPFD38dY53uRJRrxK5jmtrXzKEkOx5IPumI0R44MwRbIBZ4LzCB2GuKZx6A7h_kHhDewbFqRmIb9OSNeUaaWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ فیفا امروز صبح به فدراسیون‌ فوتبال اعلام کرده در بازی هفته سوم مقابل تیم ملی مصر؛ شاگردان قلعه نویی باید با بازوبند رنگین کمانی که نشونه حمایت‌از همجنسگراهاست‌واردزمین شوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24277" target="_blank">📅 13:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24276">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0f79258f.mp4?token=EIh6bDzKFaCf_BtYk1C23MbMZe6vMaJoMkJ_HBU1GwuVTgJKERcpOu0P4FQ-aJ34GslGX1EZ9ZxfhQsqsuGtv2FfQFiR9TMMoc7_w1QNxORb4yp7IGeRtbVgmhnCUfjB9R_edoah-dRDX2QawoUkDsz2x1hARITwr2pGIgWbsyklBUOuz2hlh3YP5HdItz9AGyileq4Ga3PoI9W_WHSTnd7aVl8E12KGz9ZJL733fdEUFlotXrW9Aoase-DSMs3tBzzotRc1drGtQQldZubMydz3PkCFeGUquE2JYWuAO9CgMV1a8Xy7lorV_wVYk-JoWcMHQP1x94G4v7KSeDvlhofCsoufUUnj16BB8nrmMUGuPOUWyMPhoxs8putH5TWkn6xnv8sT8sJKW_f8Ls7SMX6Rw2oxC7MFS2UMkIo-Go4cYCwrnTtB6ZEImyFaEXBvJv4uX8drfqAHNnPrva8nhCvkdMIv52WQQ7jse5tGBXl6pZPYqeg3qwv4MD2V8eKceI9mluZ-kPhhyRlaYuL9PnUwe_WO8w9pIjO457_9V3SEjB-OEmWkFHfhG5Uc9FkucnQz7LDd4Lnl6OcGfuiRD3VZYetjutOKCtXFWR_9SOw_wdh_5NiY96g50nlzlEM50ZOM_734CuHYNXdsFeiX5uSKsOzWZAGIGS-T4hSTNsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0f79258f.mp4?token=EIh6bDzKFaCf_BtYk1C23MbMZe6vMaJoMkJ_HBU1GwuVTgJKERcpOu0P4FQ-aJ34GslGX1EZ9ZxfhQsqsuGtv2FfQFiR9TMMoc7_w1QNxORb4yp7IGeRtbVgmhnCUfjB9R_edoah-dRDX2QawoUkDsz2x1hARITwr2pGIgWbsyklBUOuz2hlh3YP5HdItz9AGyileq4Ga3PoI9W_WHSTnd7aVl8E12KGz9ZJL733fdEUFlotXrW9Aoase-DSMs3tBzzotRc1drGtQQldZubMydz3PkCFeGUquE2JYWuAO9CgMV1a8Xy7lorV_wVYk-JoWcMHQP1x94G4v7KSeDvlhofCsoufUUnj16BB8nrmMUGuPOUWyMPhoxs8putH5TWkn6xnv8sT8sJKW_f8Ls7SMX6Rw2oxC7MFS2UMkIo-Go4cYCwrnTtB6ZEImyFaEXBvJv4uX8drfqAHNnPrva8nhCvkdMIv52WQQ7jse5tGBXl6pZPYqeg3qwv4MD2V8eKceI9mluZ-kPhhyRlaYuL9PnUwe_WO8w9pIjO457_9V3SEjB-OEmWkFHfhG5Uc9FkucnQz7LDd4Lnl6OcGfuiRD3VZYetjutOKCtXFWR_9SOw_wdh_5NiY96g50nlzlEM50ZOM_734CuHYNXdsFeiX5uSKsOzWZAGIGS-T4hSTNsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شکیرا به پسرش میلان میگه قهرمان‌های جام جهانی رو بگو اونم شروع میکنه همه رو میگه بجز قهرمان سال ۲۰۱۰ که باباش با اسپانیا قهرمان شده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24276" target="_blank">📅 13:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24275">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AULJg8dcVoAfqTOHKBmHS_C3M77TOedlpHh1rwW5hjPeurQRIthZIBkrIdqdPuox0mQD71MjYYX2wMbr1p78Dmm7bs0Q4IiDPaWczS6g8J7qVQg-9eERooD8VsGEyrXccR3wdzXo2W6mfIjSfLzsb2CeHzhSNVPdZAh9BkM_Fqa7z34TP7RwvDd9iAuy884OmzvJNPSqen_v46jPkKK_m5Y7wCrPnG7Pbv-Au_tSbMaTQPotODVQNF-l83DldHVV6KFQKQyC_ipO_u2jcPZkEyIVsvZY-wuTNsOlcdU109Ic6RK2AiUajwOC9QKM3L3NbkGJ9vFrmKKj-dSIDoIsmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
⚽️
🤩
باشگاه اتلتیکو مادرید: ما خولیان آلوارز رو زیر500 میلیون یورو به بارسا نمیدیم. آلوارز زجه هم بزنه زیر این‌قیمت‌فروشی‌نیست. رومانو هم گفته مطمئنم 150 میلیون‌یورو بهشون بدن درجا رضایت نامه خولیان الوارز رو برای بارسا صادر میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24275" target="_blank">📅 12:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24274">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbac815c.mp4?token=Y7zX7rGXoQYrp2J62PwDdDV-z-Su1Cz7m6kfzYd57NOc8TxJrHDTGOdlOfxBpwpnw1skli-BD1MQgal-xLms-l5OkFf38DbLfj96JL5S_Md37EoVr24Q_lEFPebLLTw9H_v6rJNH31bSaDtgponkibV_qm1eN37cI1uUTq9IBh4FLN7kxqA3EuCXBgWOabe3ujb4K06vVgdemjzPUsdUHA-g0VX7UgCN8T7QNJc6V_KzEz-xlgGMc83kwgDHnETAK8PPfbDIu61qF5bRZXAH9KKS86KgxFz3XE5gcPtUnUMwQqBdKks0EtFBB3bOlXQMiUgWFvkG8py-xSoue21E_Xlo1qxxFLoUpRrodrYwXUJUOcMiJ648ZDdcSdZ9K_oVNZOYOiR9VUtURRxjR-4Y1D21Y-qAtmmsGAls_bgPwsUbFvdGS0oRgHqqXJKiaJww-YJ9J5ctNLeXBzMMeDQuluIDo4Muro4H_5lWpuKUmYWiSJxWNPiJX9YA9RwZbfiz5pUvh7fR4MJOYSUUAVgPVbgjP7LT_FrUVlut_zdCDMSDD2MgmEDD5iTZxV_HV082Igmbm1SxlLTr5P8ESKyyUAo0t5Te5AiH65uEJIzc4mH4PtxNGhn46wh_ZQI_ZX1sCnCST5xIY94FigcaMqmijUbVqyF1ODsNfbFZIJYdK2E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbac815c.mp4?token=Y7zX7rGXoQYrp2J62PwDdDV-z-Su1Cz7m6kfzYd57NOc8TxJrHDTGOdlOfxBpwpnw1skli-BD1MQgal-xLms-l5OkFf38DbLfj96JL5S_Md37EoVr24Q_lEFPebLLTw9H_v6rJNH31bSaDtgponkibV_qm1eN37cI1uUTq9IBh4FLN7kxqA3EuCXBgWOabe3ujb4K06vVgdemjzPUsdUHA-g0VX7UgCN8T7QNJc6V_KzEz-xlgGMc83kwgDHnETAK8PPfbDIu61qF5bRZXAH9KKS86KgxFz3XE5gcPtUnUMwQqBdKks0EtFBB3bOlXQMiUgWFvkG8py-xSoue21E_Xlo1qxxFLoUpRrodrYwXUJUOcMiJ648ZDdcSdZ9K_oVNZOYOiR9VUtURRxjR-4Y1D21Y-qAtmmsGAls_bgPwsUbFvdGS0oRgHqqXJKiaJww-YJ9J5ctNLeXBzMMeDQuluIDo4Muro4H_5lWpuKUmYWiSJxWNPiJX9YA9RwZbfiz5pUvh7fR4MJOYSUUAVgPVbgjP7LT_FrUVlut_zdCDMSDD2MgmEDD5iTZxV_HV082Igmbm1SxlLTr5P8ESKyyUAo0t5Te5AiH65uEJIzc4mH4PtxNGhn46wh_ZQI_ZX1sCnCST5xIY94FigcaMqmijUbVqyF1ODsNfbFZIJYdK2E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
نیمار جونیور در بازی امشب مقابل اسکاتلند بعداز 981 یک‌روز برای‌تیم‌ملی‌برزیل به میدان رفت و دقایقی تاثیر گذار در زمین حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24274" target="_blank">📅 12:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24273">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc9cbc45e.mp4?token=O7SjRTx-82-V-CkAgvndAsqo4dga_Ej6xHXdbX6Yxgo8V8KXNTixvpS9gOmtUbfRI_ShE7Qs2CKjL0XArGuJFRgsADw70wudd5g6PNg8rGO5k2qyXKirnm3lOqpEj0iMDdY61IzxjfNRJVdbdaJFo12KbXOvcVBoA8WKzdCfHGurbvO_pliZ1XRX90FXyTNsKhHg64weY6tAq5F8yhrLJgmQedrubA2G8ZbemtDfbTD93E3OzTtt65CT-Ke-UnAT7ZPKzRG1Lrk4NEnIW8yMP3ao8HfM2SqA8TZORqNpGU3x9E4L2x55Gk7je77ovGhJWoc-0OBjH_ENFZWnVNjdbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc9cbc45e.mp4?token=O7SjRTx-82-V-CkAgvndAsqo4dga_Ej6xHXdbX6Yxgo8V8KXNTixvpS9gOmtUbfRI_ShE7Qs2CKjL0XArGuJFRgsADw70wudd5g6PNg8rGO5k2qyXKirnm3lOqpEj0iMDdY61IzxjfNRJVdbdaJFo12KbXOvcVBoA8WKzdCfHGurbvO_pliZ1XRX90FXyTNsKhHg64weY6tAq5F8yhrLJgmQedrubA2G8ZbemtDfbTD93E3OzTtt65CT-Ke-UnAT7ZPKzRG1Lrk4NEnIW8yMP3ao8HfM2SqA8TZORqNpGU3x9E4L2x55Gk7je77ovGhJWoc-0OBjH_ENFZWnVNjdbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال قصدداره که500هزاردلار به نازون پرداخت کنه و قراردادش رو دو طرفه توافقی فسخ کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24273" target="_blank">📅 12:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24272">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCDgWVpryCWSgz6zkkDPDyPYBaGTmHjvOGHAqQZf6QqoJE1vF8sQrw6ibVzeNWLZUGKFd76S3Eux8b5ZONB-3042LqLW3N-n2MBAce401lzbnQQPdO86BjN1aTcoHZaH65dyXGPhpeNxTkGoNrzqQ4-OYBuaxvdhglvT7wBaYtpHMvHpVl5s4QhAS7Q0rR1A6xIkxNXkqDKl94aeE1cTqrO_l2EVRThXjFseuUocO7xmSbjx1kunjqq3lnAfHWM3beOTpdoInt8lNUKBldRgikBAhXV3lCZRIF9M_7E8szaah7P8CBff_GLySd0P_udYk4QsfIDjf9yrTvPZw_xyiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
تعدادفالورهای وزینیا دروازه‌بان تیم‌کیپ ورد در کمتر از یک هفته از 50 هزار به 15.5 میلیون رسید. تعداد فالورهاش از 8 تاازبهترین بازیکنان حال حاضر فوتبال جهان بیشتر شد. عکس رو باز کنید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24272" target="_blank">📅 12:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24271">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxGbINc6n9kG8noGVRNT4CE0p8HvN_iERP8_ecZP7oATfv-0uIpeIuKHzVfuGEK-_jeXazZ6BoR8iEQwjGQpHe1C4WrpFXoqW2B3VJYpBX4mdLr-LLdZ9N9XqlELWgqUaqDdcAxKaM_8H9mMAcUDllTycRqj-6NupKcah5doi8hk83KAmsE5Qoc3YtAfeFeDQ7JcbxjUrFl0xyXZfLtcXae3oJPQ2LMYaM5kQssDXD9R8pOkFwbcCFIEiOj7G3RSK8CAdStvZuoJd5-CNk48-jfNfGQV7wFQKKKOJGHs_it5xjLwOWhq4C6sRKSJtXfXw8a5eh09TKisv1UT1nVJxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌ های دیدار امشب دو تیم برزیل
🆚
مراکش و دیدار دوتیم‌مراکش
🆚
هائیتی در هفته سوم جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24271" target="_blank">📅 12:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24269">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjdTmlmj3CuqW57MS08OTFeO_J5rQqPGzWmanetftsUs3xf1DP0dQ-YhgD222zY_ZqnY0fOEDuQ56MvbBNED4XKcBUXR7oFdIvnzELoFaF-H-BXdyH2p4-Iy6UEhREG0FIrLT9-GI5qOqnHxxAybRL8Rs0ig24Vcqztsa9VjCZRV200IlBRzxQfbx5n1CZGFWGkHPmgKcupPs0-NAoHpiKufyvn5sXEXJXIUPN0ld2W-zXttPrtKkOdG1E9nCDHlZ6tkT48NvW2ulL_bSZDEUAviVM5H2XffCbAUX7dU-4DnA94hu7ErXTXEASAWMcV7Oeq9_fqlbnccXV9tQsJlsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ توافق نهایی حسینی با استقلال، رونمایی بعد از آزاد شدن!
🔵
همانطور که درروزهای‌اخیر نیز خبر داده بودیم؛ مدیریت‌ باشگاه‌ استقلال‌ شب‌ گذشته پیشنهاد مالی خودرا برای عقدقراردادی دو ساله به مجید حسینی مدافع 29 ساله تیم کایسری داده و حسینی…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24269" target="_blank">📅 11:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24267">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DybUESlJNkBiTW50C0YKFr7jDkOHmbLH4u_sJyx1HJGfY5TOjPc8XgApnHo0nAg0TdP23iOMQ2Xe1bFeCKv40mVhHlxMjTC1sXqmaUiRnUfXRz-bcmUsLN5r8wxlnMkD0YHBhmTm2v1_F9omeujQZ6Z0me0_gY89daKQ09Q2LLISU0_txtOkpcp9Njq2YKh42idOPirIyx085YkqrseyqiNV6nI9bYkGY9b7wNvmN79Sk5PDioXutm_kRodtKoxFQxADMVzQfICBwg_FlG2cqLClCPSvHm0S5-YfitvpiA7JPI4s8-quocfCGy7XeZmGmb4vmTD1fI7fNycTE-Hwog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qTzytMmtWtcIHxpsCbEoGQ6a7J6it-PfoAnSWSY3dzAScrciozfm26QDbPa51J8mTi0t8kETJ4MvNUJLIXSq0GpdhKcAw8vB4nms_yOKM8pszr8pOY0jroVH5idDjb5S4hp1r7U_C2SxynnKs_fLu3wRiVXoQblQZ1eoGWgJQ4DXjQ8rAKU31whBsDvpScHdVZlkIYpyn2cjWU8CZXeQqdlDE4zOwO36T19M5UhNLwzPmXZnCCzFByM3a1kwqLPN3kmZWCLLomOGe_1W7cgwKf0s-O6eUtE06gYbRrmDuoMsRVxnhV9hnY0HxA0ECJStdgO_2TJYgqPmt4pukLr7Aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24267" target="_blank">📅 11:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24266">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kq09T1sk98UFwwvID466GOkMbnEXQJI2WKqbeJcsL_CqSArRC5cmnvotRYTzTudimNKmiaBcWXDR5fcNZ5Bq2EM8JXd9CDZEFTqcaFgJaAo-QiVxC5l8WUiRfhAudqf1EGKwLNgML5Y0uZqC5daK3rYJymPSJvp9RrHsFuni5o8SWM4QjW_rps35qq_R5bm5JWvks0JuDFuIGSd1tqT-Nhx_8tIyOhqaEcUDeMrKvFlwI-FKgjfDnyV1rU0iRTEda8hpM28AgvrV9gzLFMNUGLFXfaKTY7mIA6QVkiNvoRtOMbpSuxda-xEaQBzIZ6FMGTD7Q6_tPRCKjKyReeRRnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇧🇷
نیمار جونیور در بازی امشب مقابل اسکاتلند بعداز 981 یک‌روز برای‌تیم‌ملی‌برزیل به میدان رفت و دقایقی تاثیر گذار در زمین حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24266" target="_blank">📅 11:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24265">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07d25b9dc0.mp4?token=ULr7vdQmWFaPS-KO0C8HMyhsasZrYNt24iU8B3aQt7N6uz3JWSqciJToODUsTzlRzpPx2HTVVsjs69gZruJEEVovIAVw9g1cQFOUC_dS2pITlrJx0TizdyMVSdlbJfsIyNDVNfCyncjbkmlIl-qLcPb5easaepfXg3nBTi-cRjH62adsaeXcfkpap40hQOJ9eVtFgZVoC0Y1C9WKVyIKtpF4hgBnRk7-rxwwMfvlkdOAnpRzGwovo7OZjWt8kstoQGmjjs0a9vHXfJc94AsgNLWdJWmcTcG2Xs_egQymkKVlHzremuMXAe_OcYH8SXtlTnGyI7ACSpbpWl3k8yUmCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07d25b9dc0.mp4?token=ULr7vdQmWFaPS-KO0C8HMyhsasZrYNt24iU8B3aQt7N6uz3JWSqciJToODUsTzlRzpPx2HTVVsjs69gZruJEEVovIAVw9g1cQFOUC_dS2pITlrJx0TizdyMVSdlbJfsIyNDVNfCyncjbkmlIl-qLcPb5easaepfXg3nBTi-cRjH62adsaeXcfkpap40hQOJ9eVtFgZVoC0Y1C9WKVyIKtpF4hgBnRk7-rxwwMfvlkdOAnpRzGwovo7OZjWt8kstoQGmjjs0a9vHXfJc94AsgNLWdJWmcTcG2Xs_egQymkKVlHzremuMXAe_OcYH8SXtlTnGyI7ACSpbpWl3k8yUmCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24265" target="_blank">📅 03:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24264">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24264" target="_blank">📅 03:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24263">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhO0cFYSoY0HunqpyBwjfrva4IPikehvxHwiR3a6_hq8pfSz4z-_Gi_7G8ra_UsbUMLFTpwafApxvBoFvajHaDzCCu-BUyDCd5QgUhnv3yNGArKTQJLJDjisJ7roVylTl1Xe0AsNFUN_TUuewsSZimskOsO_WPnvAvhYe5PuuzNi774l0MWDNYDb9FO5jCZatuCAJl9L4z1L49w0YleeJZMyfU7S6wwiyfGPZklzRihTmJKvOWjbyHBNF8_9mb1TtKMAEat5D8uRGzawFvkNNB34vSDyYhWzYo7tFMaFWlr0WSUIKoG3xykSliER4K7Oau9N3lqeulFVxG5Sz9W1jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گروهB درپایان‌مرحله‌گروهی جام جهانی؛ سوئیس، کانادا و بوسنی راهی مرحله بعدی شدند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24263" target="_blank">📅 03:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24261">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQJHX0qIqPp_75nnsZag8GKnol9m2AJlSYyapY5g9pXvf9NOcHbSx152PxnHP2ID90ILtsLNr7IJ88NS40aymj5FDPEAZdzTsjNLhWSx5xuRjNvqBl4D_AXLOSF1xZkMsV0DiIwzMxhSboMqkLZPtKvOktEHZInLRkwxu1KFawsqjtL-UU8l-_nGqfiSPon2ziEgYRNSwxDim6sINgg34n3ljNSKotqFK3gfnbDX5-MikKoaX77IF9wOYPQQ_8V97G16OmRsPMEWP9FNiR8Fu4cO40pEJ4b-PLHmiDf1Zgj-cPDWtS_KGh8O2fJ0bdiPeQYCTNqqO_Gnqyk-feTcnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a6d46fb08.mp4?token=PxIgccvH_qbCRmv92jeagbS2cR-o7V1wwHWlLoJnhRsG7xZpYg1h4nlftk1eLY1kPuX2p7uBq9n2hhs_AihMmEFe8IXx31q9Sw94ZX8LpiZe1-7MxjdlzmLObB7XYxM0d3Jt6_P2r5hvsCIZhXtjcju8UPoRNiPKO9zFGtSKlILQlQ2BNuEeM_I3_b0BuYqFilcXtQMEeR4zPnRX1s3_5awsWLYMLFTxZlegvlAuhhNIavGtYnSW03pS9EIwShHqqpRqhNVlQcczCwBSV9EAy1zp-leg2fA9cGxlz5lCcEhAhBOigRGaOpdNBKf55FYOB9Hh934b0K_m5TSzBPFs6q_MytpvDrN-PIw89ZubKXTel5cRPaaCQ-dVpoNNRcmpaoVOri29ouMM9fHIpGYLqojpeEJeoaYZddHOwDL5otv73T2mdt1PoZKMrIYe6RtRTsFznjnDM5bL2kR-wFOdOugZe-C4sx4pSZifCz6DiUSRwmVrcvGdYv8qaS64lLpuu7yXH6wreqa-ABBYv4i6T7-j7H4aiM6jNuPbIHJBGdzb1ehQuX2HGg2nqMYLFXSEQ96sN0jjNGgzrcDW7SuhfGOq1kCLEIkMLw0i4Th0n9V28Xc_A_FkiwzKugcXcrY7JOjq8TWCaVYEcXVN0uYmfQ5pYa0DwTdudQfoOVw2cLU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a6d46fb08.mp4?token=PxIgccvH_qbCRmv92jeagbS2cR-o7V1wwHWlLoJnhRsG7xZpYg1h4nlftk1eLY1kPuX2p7uBq9n2hhs_AihMmEFe8IXx31q9Sw94ZX8LpiZe1-7MxjdlzmLObB7XYxM0d3Jt6_P2r5hvsCIZhXtjcju8UPoRNiPKO9zFGtSKlILQlQ2BNuEeM_I3_b0BuYqFilcXtQMEeR4zPnRX1s3_5awsWLYMLFTxZlegvlAuhhNIavGtYnSW03pS9EIwShHqqpRqhNVlQcczCwBSV9EAy1zp-leg2fA9cGxlz5lCcEhAhBOigRGaOpdNBKf55FYOB9Hh934b0K_m5TSzBPFs6q_MytpvDrN-PIw89ZubKXTel5cRPaaCQ-dVpoNNRcmpaoVOri29ouMM9fHIpGYLqojpeEJeoaYZddHOwDL5otv73T2mdt1PoZKMrIYe6RtRTsFznjnDM5bL2kR-wFOdOugZe-C4sx4pSZifCz6DiUSRwmVrcvGdYv8qaS64lLpuu7yXH6wreqa-ABBYv4i6T7-j7H4aiM6jNuPbIHJBGdzb1ehQuX2HGg2nqMYLFXSEQ96sN0jjNGgzrcDW7SuhfGOq1kCLEIkMLw0i4Th0n9V28Xc_A_FkiwzKugcXcrY7JOjq8TWCaVYEcXVN0uYmfQ5pYa0DwTdudQfoOVw2cLU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇧🇷
یک پیش‌گویی عجیب و آخرالزمانی از یک پیشگوی برزیلی بنام «وو باهیانا» در فضای مجازی جنجال به پاکرده‌است؛ او با گریه و زاری مدعی شده که در جریان بازی برزیل و اسکاتلند در ورزشگاه هارد راک میامی، دو سفینه فضایی به استادیوم حمله خواهند کرد و در دقیقه ۳۸ نیمه دوم، یکی از این یوفوها اختصاصاً
نیمار
را با خود می‌برد، در حالی که سفینه بزرگ‌تر هزاران نفر از بازیکنان و تماشاگران دیگر را می‌رباید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24261" target="_blank">📅 01:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24260">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8236df4e.mp4?token=a9Vpror0N5sZu-hspaMw2VBVlkfS1F5JabOBL1-wMnghRvkHxb-YbAQ26xEVazmXJRUi9O36gf0YJdYAfWN5fd8MPT1HyohZdCRHJrV0WeLgJBPYvVdsYsy3cBd4JAfcSo2HHtvVEVyKdFrx-Fchb2Wa6sqvcpfBuRnOFSF2krct6BGA98cAgr7kceJQAn2qLRq_QymoNg_hSxBhAiU_HQY7DskVPyWW4U3BitzifcUaw8NiGPcYezvfwowcQmkC3DAs9PYTRTLG1TAco9A5DmtsaoiOeSpZ9LBJPQVeialaBb6qkx3I03aoEIBg3B5okSpSQ2T0AmffkXWk29MbKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8236df4e.mp4?token=a9Vpror0N5sZu-hspaMw2VBVlkfS1F5JabOBL1-wMnghRvkHxb-YbAQ26xEVazmXJRUi9O36gf0YJdYAfWN5fd8MPT1HyohZdCRHJrV0WeLgJBPYvVdsYsy3cBd4JAfcSo2HHtvVEVyKdFrx-Fchb2Wa6sqvcpfBuRnOFSF2krct6BGA98cAgr7kceJQAn2qLRq_QymoNg_hSxBhAiU_HQY7DskVPyWW4U3BitzifcUaw8NiGPcYezvfwowcQmkC3DAs9PYTRTLG1TAco9A5DmtsaoiOeSpZ9LBJPQVeialaBb6qkx3I03aoEIBg3B5okSpSQ2T0AmffkXWk29MbKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بااعلام رسمی فرهنگستان لغت فارسی:
آب درنگ جایگزین فارسی کلمه hydration break شد!
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24260" target="_blank">📅 01:23 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
