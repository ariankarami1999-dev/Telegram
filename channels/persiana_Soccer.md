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
<img src="https://cdn4.telesco.pe/file/ggOCrvNvDE5j0DMB5dGuqTehws0INAGFDQKvzlvr67gNyIls9BuZo_s5-JRQnFqhxBG4eZo0SC8tvW4fxfQllPY-oeM6M_e5GwOTJPbd0Vh7abXwM1cpHeVkkJRNAp_1JhisvWg-Aq4KhcAr5oTY-yblDX-JIECAm3r_Ix_X0LLnC3XrqMd5NztkuXYk9Pcrls6CBnABviY2zmWKEWXt2Vd7Np6D9n5kTFWn3hC8YkujL_u5lAq7qOYRo15wE3DZs14nfNLj3z4_S7f1bObrkU7o2_YEMrwSCGT7YU7OIeEKd9Xs3JWaLf4STPEwauXMUs5UDTJqUjOYPbWsYx3vxw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 637K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-17 15:58:41</div>
<hr>

<div class="tg-post" id="msg-27329">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgOL2Iuc9501dvRa_z2cmuBf2SklB7E_v_dHGknWQRI7mLhEgl3_58qXJ4mDPmd9k7vpLDxv6CHyIj2t8sqoVgcmRNDMftOfGvblJZxECjsi_I9O1fjKPdEHbyIaFdT1KaG0lSQuWeFoJR3pirK37QCNboSaBtRIB0vyEYYApM6QGfYD4XUzard8T8KKtrejCeL8T_GGGHP8EJ6LwsJX9xxBaDv5xcifjTh27xR1OrWvQ9Q8rZA3hjXaJjdyxYBnuxFSfuxaLZNKK-CJnnISrnYBjOtDmpmfraxpqfv350cL70ADqZKxJDknej6SrWcZISV7ggg-_5gDKrzeTXL0Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
🔥
فقط و فقط ۱۱ روز تا شروع بهترین لیگ دنیا و رقابت‌جذاب تارتتا و سهرابیولا مونده؛ برنامه دیدارهای هفته اول رقابتای لیگ برتر خلیج فارس!
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/persiana_Soccer/27329" target="_blank">📅 15:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27328">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LICKAVT01DG3aCk9yxj51vrSp1rsVq1NSHGWieXuzzM59Tsd6IONlqNYfZ_7wSSbY-zvsy42qiAGJhH2Z2zSZo0ozGgsutIK_V9vCNOg3Uw_2B20pP4Q5Do0EclsIqVCFCui9GJkWzmH04idP6KcLn-bdz8X7rFIgXZH2BJXr3tDKOi25k0tLntpUs8kvbwXF6QGKSwIxGCb24CnD4wYhA7NKhb4g5A0g_g5skCxLrRIPT7v-no-DRyE5BvKRWmGQGVla22-cgGyyHNWC_9h2K03pO05f45iw0rr-73JXa1ggUhz_Ezw9ZZpN4D4wy-g0bCfYFEs4vCfLPhamqTb9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پیغام باشگاه بارسلونا به سران پاری‌سن ژرمن: فران تورس رومیخواید؟حله 55 میلیون یورو بدید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/27328" target="_blank">📅 15:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27327">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsJjbyD46bhRGS1jsvPvmQMoCyJqiP_NdceO-U0edQ5phMnMU6ZJH6NfrT4cSnyQ4iLvPic0hhcZW1oIxL5xDR793nFqcyJx7DONTv8UsocWHjqh42YdRGawqDNexxGeeoRcQK3-ConS0DIMED8YX_XHyGZNfkAmg3kls03MLv2NFiJMmXbNq_MtKI-5Pu4vGlrF3Qmb0ObA2BkvXXJ29RaU9tddlV2NGrnO9mOXYgjnRcs19bgm0SnN8Te4AG5yifr4i2b-WFm_Mu40_12FYJnqgJ8UhOd-aUndCTqzA9Ef_iULWlqYmWSbX6tseYkunMW83AhVFllWmifH90sbEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ سران‌بارسا قصد دارند بعداز نهایی کردن‌قرارداد رودری برای‌جذب‌کریستین‌رومرو مدافع میانی 28 ساله تاتنهام و تیم‌ملی آرژانتین اقدام کنند. رومرو برای پیوستن به بارسا چراغ سبز نشون داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/27327" target="_blank">📅 15:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27326">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B95ozO62Wx--TFWA13PYl7BqDjBZXkU8dM2JkvaEEmdJKhvmQrdTRMTy-3j1oYu0zWApejlwjle9JBmd3AXMdMNOtJRUQ4HHE3ivo-F9SGNRtu3tg-Gxux2OFciMZMF-GiiojlMBWkQY0h7aQqquC0NeEiPCGKBN7Jz3L8JtrxhETQlo4hSZIx8sF65uLVw_csEJo_gDM8qXmgXfjOX78i8TOt6q3RcewyrHrn-_ml1GKAujywp8CziFNuCkZZFTx9UqofvkDV1JY00AcuIzNNiHWMp-HHaI2C07SBbNvWPsezHtgXoa-pcXXHs3HaX_jCWsK7IiChxK2o4ciZ005A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
باشگاه‌استقلال‌اخیرابدون‌مجوزو مدرکی 80 هزار دلار دستمزد به اوزجان بیزاتی مربی ترکیه این تیم داده‌ و بیزاتی چند روز مرخصی گرفته بود و به ترکیه برگشته بود که بابت به همراه داشتن این پول بازداشت شده و باشگاه درتلاشه‌ مشکل رو حل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/persiana_Soccer/27326" target="_blank">📅 15:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27325">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVQajxavKZYDZWkf55QiDEz5fm1ur0aYd46sVtUbd2kMCTlEe8MLg4Iq56nkGfD79bGEOgr7hlqBx-mblWEldaZixIHaJ-a198ZOd2A1DNSld1DEAexEd3F3c6ElVBt3CDgjuoax_GvW7BSDtd154sC49Knq3nARmwJI-P9kfgYVS8ZSmdhYdv4JQ3MSDjHIlXPBK42nzfjmXRK_47qFQphRiU587HvikadcUCckXzXmoG5XVrZ-D7X1IjpvzpdShkAvR3U04nZ95TbsPLihzDF4DNj9lg78pWWjgaorNtGvxzLoYgo3492yN1YvnVpZl8duZrLmyaVJfhWL8HbgmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
#تکمیلی؛ هفته آینده مراسم عروسی کریس رونالدوعه که اتفاقا لیونل مسی هم دعوت شده بود. حالا با توجه به این ضایعه بسیار تلخ باید ببینیم لئو مسی دراین مراسم حاضرمیشود یاخیر. البته ممکنه که کریس رونالدو مراسم عروسی رو عقب بندازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/27325" target="_blank">📅 14:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27323">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iqv4VOOSdqJJscAX-xNQUbAKQwcn1ABgv5Sjx5Yngr-2kDjOUpg7_F8M6aPqlnZEyqvjnyKwTaFZuoF-EsmQajz-euOgjS3WYHYlRAjvW6pP26mkw-QPs61jB4fc4d87XbC-ailyTttjMbqR5QrLSgkRd9ZLrHAy1SfJpoYMK8J7IybDzpPbdttOyDWcrP4JPjZmXjsBy7145oj91MNRn3hKcEYAQfPcI6FAFSmS6SwUm-4PNYPuIZ2nkbKd5TQQ_NhptxM-h9WIPbm9th1XSACojVEOQX_bOtqLgHUvFne3i-VciSFGuqTEhjkocvSPNIkOqJySPCwUS07s2qYONQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PXMeo6yFzIa8WAxVuq-1q49nx8SGQqUUc-oyFIL3G68QfSQjhDmsMb-U6XSa8ZzRbZu1JmLd--FxuSavqD2cP99MW8p1rWnSsdYp6azQq44FrMEh2wCQgCdE2svNDRXL_vwZpSLM5HyurvDxwgviutvvUD8HewIGol4DbujnC6hh858ZGICxaWmyC8V-RDMunK52-7sCg88YQm8S0I1t46sHszAkFspbBhuSkWSQCFqVbUEFFxyHSER5R0iOpN2KdYFxkrLT6N_GaijzKWcCOwuU2-vanWmW83hI4es0mRzDdRzFAWAnhklmWa1JJAi-nVnqZ8cQC5pMQ_Pm_eK49g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚫️
🔴
🇧🇷
رومانو هم تایید کرد؛ باشگاه آرسنال 75 میلیون پوند به باشگاه‌نیوکاسل پرداخت کرد و برونو گیمارش ستاره برزیلی کلاغ ها رو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/27323" target="_blank">📅 14:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27322">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnKhidycyBdDKy6_6ekfEASAqPPJLQVBKrDicQf_9RYKgWV3g0YA2vdrzvMk_0yc2VFvplT1KFOERzlFtajnumfZjaUz56KX4XRfrSAelPc458jtNI8O8IWtgYvNK7kmWsCLzn9Lr_ASfBsQOpEymIxAfWvI5Mb4CSC286_u3RVx7hbjYQXhAiEYpI8B2cPthUp1t9iH9wfd15pQUiHT1FTRvWz5ulivvCT9ERfpxd6Z_pgGQOL-P62qioIU0_7BWYlPUz21frZ_VOTUMXuEU6zLCOvaVQF6KbA4GZkLtBXbE29NfsVE5N4UzIBBA0ADVJJJlSARxwZH6yNAEjrwrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پدر لئو مسی فوق ستاره آرژانتینی فوتبال جهان ساعتی پیش در بیمارستانی در آرژانتین درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/persiana_Soccer/27322" target="_blank">📅 14:28 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27321">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUpBfIFBB4DVph3NpF8qqHA2w2BkinKHbLnazIrBBdHgQSanz1WFqOx0Q_E5lvrsSttICRJfeUKhe8Fd5UVuBLa3YpQPKNjc_suevEslq7G-bXKEqC_asz31ILghBuhDWDDlYhKHNrzFmiWh67wjyZDEfv3IRNsohScvrTDeWEqaITZT0RwkpH_hCLoLTTJkYFSY9U1Nv7iQ47fqkYPa7blfAJxTNWrzYwM1llbUigtrnP7YnHwWgcWWfdhoO1eOHbQLPJb-WQpNje0OaqzV6TSPl48JCOcp7XkWcgnJ3ZRmDC9N1YP_rqfVlwRhGlVrVUfqu0bsA5HraxmCj_VgWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پدر لئو مسی فوق ستاره آرژانتینی فوتبال جهان ساعتی پیش در بیمارستانی در آرژانتین درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/27321" target="_blank">📅 14:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27320">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUB6LKFIZFkVwQuXe7akgRmVLHFUfhzRBwEiklAwd-33rEEPqTrwp7hNzTLA9fCFJhoHQHNS9875hYtjF4xsbe0Zn5U4E8kMxzY30q1w4RXMkc2rqA83WWiCbK3ujN0f4tno4JTNeaIkOJkcpkXQR11aJjDJ9IFSCdwAi5WEQYEhVRf_VvPDMM9TtFCaw_li959cMjzL4L46iSmzmIYXYI7UxGhIgPu9t6gv9ob1fuGmZJbyV-nWX3GbSY7wYAYCCkWo7OV5dUJ67s2_ub0thutEupfpGpNtsxg0HnQiTeqciOOXV3PiCdSI81oCGq3y8-8qnA_fswQ8902CNshaZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ بزودی فابریزیو رومانو خبر پیوستن قطعی رودری به‌بارسلونا رومنتشر خواهد کرد. تمام توافقات شخصی صورت گرفته و توافقات بین دو باشگاه نیز در مراحل پایانی خود قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/27320" target="_blank">📅 13:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27319">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fa190d851.mp4?token=kH8kQRxvIeUFr1dEfWSvVFwXemnNAHlazp7x2eeK2ccH7gp9VG8pOmSt5HJc2F3G6mn-SkhcAMZ1mtPrkHMgNaDFxNt6Kh2hljh4mIYlp5Klli4nG-f7kH6HmtWXqkwRI9ZqfTQYdlJQkYRFsUADFSWyK2z6RVNTBERqBiemJZKGn4tBz7hj5pgI9KRVcFXZHJ3dmjUG0NkGn3CorMZEzCbKVbV1AwkPUeOOt6PjDuPrYI36f6mEX5sY_vuS61F1jFyqmHW1PfOhg0dH-ePdWlLVmgXBGYR-pRL629dHTScq51a9KxInqMg0-3thKs3preeVtlQJ3LVaiWTfwJsCCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fa190d851.mp4?token=kH8kQRxvIeUFr1dEfWSvVFwXemnNAHlazp7x2eeK2ccH7gp9VG8pOmSt5HJc2F3G6mn-SkhcAMZ1mtPrkHMgNaDFxNt6Kh2hljh4mIYlp5Klli4nG-f7kH6HmtWXqkwRI9ZqfTQYdlJQkYRFsUADFSWyK2z6RVNTBERqBiemJZKGn4tBz7hj5pgI9KRVcFXZHJ3dmjUG0NkGn3CorMZEzCbKVbV1AwkPUeOOt6PjDuPrYI36f6mEX5sY_vuS61F1jFyqmHW1PfOhg0dH-ePdWlLVmgXBGYR-pRL629dHTScq51a9KxInqMg0-3thKs3preeVtlQJ3LVaiWTfwJsCCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
ویدیویی‌ از خداحافظی چندفوق‌ستاره از رقابت های لیگ‌جزیره؛از محمدصلاح رودری‌هم رفتنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/27319" target="_blank">📅 13:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27318">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKiO3k1d-37dBRftXcU39jh968qQLrdaGttR5Kw9vGlcn7jeH0gnEAlls7wqvtdmcOFgXJxVLmZQihDAIPGHwKrahNH16eCDyyYLohFz3xuCei_ylvi4znL13658MrPi08EkUNF1oHjg0fdxeiLjAk9yLechlh7CNQ53Kg7VD2CAXqePFXWMNMmI_3tXNqeJ_8vXYty4rOQlpwrSpxbrykcXgu2DDrNBofR02gZx4ZSJGjHe3Zsn6bjzkj1ELq-T7wxu6eE1Ib1wyi9W880bU9cEnrFEzDIjghtHzSLLgJS_xOkaADmlFo67Uw-z3uWa4Dzykfwt999oNIKDL9efcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ محمد جواد حسین نژاد دقایقی قبل ضمن تشکر از باشگاه پرسپولیس آفر این تیم رو ردکرد و به‌پیمان‌حدادی مدیرعامل‌سرخپوشان اعلام کرده که فعلا قصد نداره به لیگ برتر ایران برگرده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/27318" target="_blank">📅 13:04 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27317">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🎙
زلاتان ابراهیموویچ: وقتی 20 سالم بود با یکی رفتم توی رابطه، الان دوتاپسر ازش‌دارم، توی این 25 سال حاضر نشدم باهاش ازدواج کنم چون میترسیدم اگه بعدا طلاق بگیریم نصف دارایی و اموالم رو ببره. بعدازحدود25 سال یه شب کلی تدارک دیدم و فضای رومانتیک درست کردم و از…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/27317" target="_blank">📅 12:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27316">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/So6LLea47z0JX_NXrqT3chSEAa8cy5anKduYQDLOxHk9k_2QPotiBF2AgF_pZmIvt6gUkoDwzObodZPudNK-DsVJdHzAm35a21fVmbCvwMOuFyIjCf8pONaYcA7nPs6oB6wTIV6phJN0pO1wFqsH6VzrAT3MPcAzKVjFZNzTbwW2kQI5cjd4m_YIZ5_7_3R0B3F6XjiMasdn2bXgfxrUrDA2D1tWprRpNwxaMg3dgH6rs0BSNae7Sp-jUg86Z8ofO128DHsofVaZKIMaeudndmjEHu4gfZd0AWibzZNy1TQV1xwVmqNDfa_Z7joaHJd_DKZNbjg4QrZbwr7QGmwa8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریه‌مارکا:
رئال مادرید و بارسا به احتمال زیاد در الکلاسیکو رفت‌لالیگا که روزیکشنبه سوم آبان ماه برگزار خواهد شد با این ترکیب بازی خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/27316" target="_blank">📅 12:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27315">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M07lIuuGMQEQLbUgaX75yLlvD9HzXsig12hXptpFMrrNEGqcwf1F9UqSSiGVtPrJuZ_NKU3QyVc9zL1Cvd5vg_7MrpkQrpXy5O_oT2JO7VS4nfWFt49PCrTmt1qCZ-ERoEBpaVnfaj2286BeMfPol3uqDlbz5eTkJy_P6QT5f5ucCKoRyvIqL5myvFQezQcRgs3Aeu1mtrfK1MDhjP3E2a6ZkciHfCT2niOcR-bIFco_z7H3hQnl9LP5z7po6wE2_7246GAjDR1b4tqzjOeak_ksrhtvUEgnkYfYjXvTsBMUZSxQMlwduOzUtqwZtCGKpkbOTQN_V2WBaljoxw_C-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
⚪️
#افشاگری؛محسن خلیلی بدون هماهنگی با مهدی‌تارتار با امیرضا افسرده مدافع میانی 25 ساله ملوان‌مذاکراتی‌داشته و قصد داره تارتار رو راضی کنه که بجای ایری این مدافع رو جذب کنند. مدیر برنامه افسرده همون ایجنتیه که با مستر خلیلی داداشیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/27315" target="_blank">📅 11:42 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27314">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdgfOnBcnjlsZtjrfnYMMzgnamMOXJQ-k-F9P-ednFEy3KjYgQ5zVCaeN4R5aWVcwej0rlNQ5ZrYTudHrQyNH2QjZvX7p6jDhy4n5CWvoh-wvShlFJqDeIeP0lecFpovaRzYhN-hSvOfDGglWN-vhwhymztv1i1-vKhWbsJ8T51TzRMDOgrz1qaucFmAhAotkND78HA0HiSt3sLsWT4zqelS8lg3H1xi6KxOLkcGDum7W5RHGCSNJuKwWslzragK_8FQ4uwZt9JV_2ZaJU6uQ5FBuCSNt8JpBC5VbPePfxqvBva98Xe6GNCHtyr98KCJ6f12CGtlWE3pFrw5M7ac2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جایگاه‌جهانی تیم‌های ایرانی در رتبه بندی قدرت اپتا؛ تراکتور تبریز درصدرتیم‌های ایرانی قرار گرفت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/27314" target="_blank">📅 11:42 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27313">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHp7CaAzAejFniT9kqv7yIA_r2S9m_qqkUL-LFC9TzXfHwXYR-xvw_i6oz9mKKnk8WbXoidIA7BN2c7yYnwqfkbBjHSA9SctmQtfNzn3Ji1H4sbsaiyoZsy7pxez06s23Vrr75UA31NGYHqGK-aMiD45BDyfQmZO9DIXxozDYONLa0327YLHYiSKhF7-8nwfznuQjPMlnHzpokBQ1Xv1xrQldLfTuNHm8h7UTrRBt4DUgxAiliTFwsNJmTj01f3-ksi4XBaGgBD40ShO4qdMRiMsgKAsUUYt5F63HMsNpbF27sNxe3shXtrqpO375Jyrfu5zZ0nHRwn8uj4Zw3fiBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
🎰
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/27313" target="_blank">📅 11:42 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27312">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Af0i41LpmqoMPysVLHwkBYrV6bPv45L4F-6HcnUThMcnmyKIPd2BxgVOWbLx3K7FEhBRIYCBD03rXwqhr5zyY2ZUGpUsnPg6mAOVPUjMtkELWzhsFadVTOe_zy1uZ4B4SjhY37OENUYujmYyxk4SOhmVheaeBPu8uwTmyAuYGDEEJAkoIqMDoN_C0oZ0TJ3zjikCn3vFtoAHZWSUByPPpManwtCRaX_uiLmajalpZEc23SKpl0gdKdmzbdSvBasK9MXUUjoohfmyNB36-GadyH_GX9G1ePogK3_iMpoI-MMhW6ARSNBQy4ijfZ8kZW7TMmasW393m-7xQ0ZKFoqAGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی پرشیانا؛ احسان پهلوان هافبک تهاجمی33ساله‌سابق پرسپولیس، ذوب آهن و فولادخوزستان‌مذاکراتی‌باباشگاه فجرسپاسی داشته تا درصورت توافق نهایی شاگرد رسول خطیبی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/27312" target="_blank">📅 11:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27311">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8uVtEVs0gQAoS4zgNGpgoewgMXd-56Ns3M0QEedUVC1se3qXzDlN8AIsOo8AHVYLAbd3Jt4aSIdCM8_VH01s6GY0f0dZRTs4fLeVlyVT2SpzFw9YHQEairEXUSG3s8qBspyymPSM81TtNqDW9A_KqmxRLiQualQgfmdyEvt49ZwCj2i3SoCiz9gbFp5P_yokirj358m_BcXVJ3jde5UiVmmr0Yj6DkBtVfKhyS1ffs2dCRwjEUvYfwAwyxOZSFSyQVcW81qYdqZrw8cpNoB-KZhuG-YK1c281YIvAkzOQVCcmH4yKufJz1nT4jHRR38yujpbHFPsDYHkR2SCI3-8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔴
🇺🇾
با اعلام رومانو؛ لیورپول خیلی شیک و بی سروصدا رونالد آرائوخو مدافع 27 ساله بارسا رو باعقدقراردادی‌قرضی‌تاپایان فصل به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/27311" target="_blank">📅 11:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27310">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a095528f2.mp4?token=CCsy3o4Q4eOYcLl-iY914LW_lNEfjyV3ag-Y6iWvE2s7ucy0Iykll4K_PI4Ysm6DAE6x1PoMEa1bHbuajKvzHbKOrAdMEgVfciNdX3YEEChZzDTREiCA9jsPicSqmGz_1HCSBV6mfovxnKCvEx1vHmgOP2bi96C8-PQWyfHF76QkdZycAG1Yr4im_smeLitRoilhn8CpdYekYEWuhIh6LzDDe14m5YC9EX402dXtjtu_r_lwvaqgZ32t3s4LHEmCWzSatAIRmxw_sC7AMoYVJLBo20v83viSl6mk_4_3txXZHFsZ_J1GYes3vqdSqdjs49oKCN33wKFSt1v7agsAiWPLvbFSLfzvBk31kN7T6ucCIHlRE05gUsQoA_-nTTCTJDj9GNW6Xtgyz33Uf4z98gc92v2afXRAvi5RzC2YldhX6QfpYybydpwuMoRcYyRq02r5iAluwBHhFBi1C024J180asCRW0eEzIqukhFgNKLyQqggQ2Kc9KHoXiXP1HcdaP8YcpsxhsX_YeXHh1fcHYwjdFUuBrwXfY_-cpnFrSjTgC52FBVwrjzNiDgrmY6MFxqY5vZ1hV3BFHZqDGI3SUxtI7J6Xovp9Uj7_zg2AQGBRu8GuE_jWsjmYS6dV4HK0THlf-BpZOkRHAtfo8_l1IIIC_OiaxmEN3ollXeq-Yk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a095528f2.mp4?token=CCsy3o4Q4eOYcLl-iY914LW_lNEfjyV3ag-Y6iWvE2s7ucy0Iykll4K_PI4Ysm6DAE6x1PoMEa1bHbuajKvzHbKOrAdMEgVfciNdX3YEEChZzDTREiCA9jsPicSqmGz_1HCSBV6mfovxnKCvEx1vHmgOP2bi96C8-PQWyfHF76QkdZycAG1Yr4im_smeLitRoilhn8CpdYekYEWuhIh6LzDDe14m5YC9EX402dXtjtu_r_lwvaqgZ32t3s4LHEmCWzSatAIRmxw_sC7AMoYVJLBo20v83viSl6mk_4_3txXZHFsZ_J1GYes3vqdSqdjs49oKCN33wKFSt1v7agsAiWPLvbFSLfzvBk31kN7T6ucCIHlRE05gUsQoA_-nTTCTJDj9GNW6Xtgyz33Uf4z98gc92v2afXRAvi5RzC2YldhX6QfpYybydpwuMoRcYyRq02r5iAluwBHhFBi1C024J180asCRW0eEzIqukhFgNKLyQqggQ2Kc9KHoXiXP1HcdaP8YcpsxhsX_YeXHh1fcHYwjdFUuBrwXfY_-cpnFrSjTgC52FBVwrjzNiDgrmY6MFxqY5vZ1hV3BFHZqDGI3SUxtI7J6Xovp9Uj7_zg2AQGBRu8GuE_jWsjmYS6dV4HK0THlf-BpZOkRHAtfo8_l1IIIC_OiaxmEN3ollXeq-Yk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
ویدیویی از عملکرد خیره کننده و تماشایی زوج لیونل مسی
🆚
کیلیان امباپه درپاری سن ژرمن؛ تیمی همه چیش تکمیل بود بجز داشتن یه کادر فنی خوب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/27310" target="_blank">📅 10:52 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27309">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🔴
بعد از جذب کوروش اژدهاکش؛ امیرحسین طاهری مدافع‌ میانی22ساله فصل قبل نیرو زمینی که عملکرد درخشانی داشت در لیگ یک برای قراردادی 4 ساله بامدیریت تیم پرسپولیس به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/27309" target="_blank">📅 10:18 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27308">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCZBrFbs2ZUi7PQ8qRUTiajc50o3sIydWdZdKel1Chw7M_kTo9vyR6aYogAG-jn9anNENqB5EDWMwYpdWlbZyFD573Awp5SNVFmReJ6cIy7MruGOOd3TmkXRiwlbSBRaYkkYd2xAnXzqcle2SeV0TZ8rGOt9cEAl_rk3OHv_d2C25dneSUmstWvzGztqT1IFZijVesWJoXz26k-3LsHzvTKeeWEMusVCidV8TSlhQXkOUctn6efKEvbHlKwoGYso-GHHnyjjPDigsdkx121wGWbFJtiwkWevzjnOvlO2TjBUJ5eO2YXHP3dgyswe8W3OOBZmHn4f1ei37qVtiTq41w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
کوروش اژدهاکش ستاره 18 ساله فصل گذشته آلومینیوم اراک برای‌ عقدقراردادی پنج ساله با باشگاه‌پرسپولیس‌به‌توافق‌نهایی رسیده و سرخپوشان بزودی از پدیده فصل قبل رونمایی خواهند کرد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/27308" target="_blank">📅 10:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27307">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pe5ClllPoci1j1_QyWKo5_JemJf4mMvk2UEaNYLbLHSZSlvcUBuAOovxU7LLGcajEBR3xmbJC1G88S8XZpF4tPlsmRGqW2vFSVlvU7ve-29jEITk5pmSK2uT1GzuZGplicVbphkQBvC8d5Nb-s4H0k5h3nPhzlJ3Ui63sRIbPk--C1UEn3Lb7ocE5czQuuE5uFSa4FWKGeRkQZFif97GIM2xJkEOMmOa-KTFuNGvwOd5KGA_KI_w6jsTZvo0jLvhbin47Mr0_Dp-xMERdrxLaZAKbQGCh6sX36yMmXnONDJbdwDPRW2Y_4y8m6e5irv2oU6bImOZxHipDloMjd9EjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔴
🇺🇾
با اعلام رومانو؛ لیورپول خیلی شیک و بی سروصدا رونالد آرائوخو مدافع 27 ساله بارسا رو باعقدقراردادی‌قرضی‌تاپایان فصل به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/27307" target="_blank">📅 10:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27305">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_UGgnKpNB_hxkrFXtzHssTIAGucHrXnhJCOrXN9wN8Lqft5Y9e0E1qpQpevSkZm67OTcfXtEfkN8cygXliSczvJrE40Qu2LnjVVNa1ZJ1L5CxYkKxWAgu7EJy_X48CCXU2xlwtxlP15cCbALFWozVntlnYlRAj9vdY1lPXAtvWaZA09saiAlU_Ii5LKx09LIjSs6Dut0K88j5oNkXbVa1AcpVOvgTo3QKavZkHGOkOn0OIZ2FIWfwLORdFVoBxodtx9bUyodJNyUNhbw5YGIhepYu3zgGXRoH4S_pgJfX5BLy4N1at2aciRzSn2d5lZByJHDQZPBcxOJX4v4D6etA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
با اعلام باشگاه فنرباغچه؛ اسماعیل کارتال با عقد قرار دادی دو ساله رسما سرمربی این باشگاه شد. ارزش قرار داد دوساله کارتال پنج میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/27305" target="_blank">📅 01:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27304">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVM6uYB2uFXenTiv2meCjPpi1h1cT4tjL4MAixAuv7Q23PzAdJf8lAXiLCoQIl8hqMSvfn9x8gpYP38xLftOm-c2OQrrw5wuSD5GK0czosvYSlAGrZ9LDDIDDCN6NSeNIwvDZ9g_msiuXGYOHWESZS9gF7dr734WpP1GsJlY0HguwoAxOuhiri1f_NCUMuFIEGVCwp9Aht1R0Cme-C2bJ6zk2sbn9XELlY2zOWYKdxUHkTHbpekaACcwyRZJH8v0pchohY2I7h4phqi4dMJZ3fLlD4boggwP37dSiXY7by6GIlcTqPeBlaV0EESbIortwvOWHtAInOgmp451LBiRaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
کوروش اژدهاکش ستاره 18 ساله فصل گذشته آلومینیوم اراک برای‌ عقدقراردادی پنج ساله با باشگاه‌پرسپولیس‌به‌توافق‌نهایی رسیده و سرخپوشان بزودی از پدیده فصل قبل رونمایی خواهند کرد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/27304" target="_blank">📅 01:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27303">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc07f33275.mp4?token=jgHjh9MpRzVh3QHWpq5h9PngDEG-h1CVk4nzIQKugQwh0SVNNzF9veg-FPWxIEfboyakxtzQ-0cc_8qAvG3_nvmtkgDS-uy4dmosdqQdrhK36PxE6ZLft_W1ruvoP_NUybQf_KX5P05xDJjFG9q4sUJWXM1WlD5TU3qqXxfQrrNMn1LbTo0apmnrRgV5RMB2jZyrtX1nfyCJDWosFBRBAXW7ZQ7xdkB3BvQOmQTy04QfNCitzVzgAQfAR98WcFUXDxoHISsqZehTM-1yZ4byFCBrV-ghM_KHwrgre-l9YhQAUqiAWZ6ZOCZ23XzG_H6ap-EzONZBoZdF4lq79jaIfDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc07f33275.mp4?token=jgHjh9MpRzVh3QHWpq5h9PngDEG-h1CVk4nzIQKugQwh0SVNNzF9veg-FPWxIEfboyakxtzQ-0cc_8qAvG3_nvmtkgDS-uy4dmosdqQdrhK36PxE6ZLft_W1ruvoP_NUybQf_KX5P05xDJjFG9q4sUJWXM1WlD5TU3qqXxfQrrNMn1LbTo0apmnrRgV5RMB2jZyrtX1nfyCJDWosFBRBAXW7ZQ7xdkB3BvQOmQTy04QfNCitzVzgAQfAR98WcFUXDxoHISsqZehTM-1yZ4byFCBrV-ghM_KHwrgre-l9YhQAUqiAWZ6ZOCZ23XzG_H6ap-EzONZBoZdF4lq79jaIfDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ویدیویی‌خاطره‌انگیز از تکنیک‌ومهارت‌های خارق العاده لوئیز نانی ستاره‌پرتغالی‌سابق منچستریونایتد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/27303" target="_blank">📅 01:28 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27301">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwK75PVRnqLEys-AqyJkyKa5NruLcGFy9N98_ZaoH8Vd8a96Azgb6Alu_yypDGYmewKNyNTlCqQheWLahG1r5q85sEWc-2DkxO07DXAM6mDx7sAQ3NvahEs73kxlIrE74qkneuAOdd8JgzwWLMwLywsA6Dp4UyyP7igv5ZF_n5FuCZUNHj9a5IlxJxi-kT56KmlvqBxvZOG2r6TYKdnbxUTQ1RkXpr1679Ppow0uXahR8qRqy7pI4IlOjkWmCS-a9IURmZWunaa0vmgxLtns-iTI2FabjLN_12i4GX7MBwiFTfMvYNpGhiflJwWsZrdBT-yLBLTLzJMGlinXur8oXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔴
🇺🇾
با اعلام رومانو؛
لیورپول خیلی شیک و بی سروصدا رونالد آرائوخو مدافع 27 ساله بارسا رو باعقدقراردادی‌قرضی‌تاپایان فصل به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/27301" target="_blank">📅 01:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27300">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4LK1oWDVgU6eRi8WMVSGaGQ85wwjLAUXX0zPkJ4L2cFikm_oF8q5TId5CDVFfHj11eUBzKQ3TQnwaTySAbltapFGmyFKPIQ9JH7KEk33timv2mkk5gnMlezvNsZFp_SUnZ--g7Xknjh6XioyerweLypGXBIrjHhiVPHLB_aPwf-b6XHBU6Zau3t6M6-eWWZcgvxkJVELRXibskyCRUtVJcWAo4WDM08h9uEuSkRQTsphMPaXvmGm3OcF_hzVqtKlYCzc0M9PsDAtVEvfd9E_J_Sflt-o-V3JyGkIZUVE4wfvL4hWPGKS6p0ppprzaDXnDBftxEIk6sqnS06aUSCQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مهدی تارتار امشب‌باردیگر به پیمان حدادی اعلام کرده اولویت اصلی او برای پست دفاع میانی دانیال ایریه. باشگاه‌نساجی هم اعلام‌کردیم که منتظر است‌که‌باشگاه پرسپولیس 120 میلیارد تومان بابت رضایت‌نامه‌دانیال‌ایری پرداخت‌کند تا این انتقال نهایی شود. فردا…</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/27300" target="_blank">📅 01:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27299">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiMHNfRnloP41EHLmS20GMRs543dG9HccVMy9ZX82pi5JBZvz9F297WJlpOtCsa5BBl2rxdllWaxq7WZLFck7SNTzDH1bv7f3yYLlxO55tZaRX-IIrTlxSze9odN3ch7vt5PAwlkv-RBfqAscXxRXQcvg2Ors2io1LgmsOXQciOvnyj3qpG8jIwBID4it0bUkxEPT01QoQiVSrEwwmLmrZQmD0ChLQuiLloMN-Rw2zbHUXIMCK9r_sumGAqmGVtSn6Lleld38eK_qChu_7ED00ashQxhno07nbm8gAqKOG9EIGp8vtlS34VdBKAGqa7fESE5QCwrBGmvtUu6jVWBsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
⚪️
#افشاگری؛محسن خلیلی بدون هماهنگی با مهدی‌تارتار با امیرضا افسرده مدافع میانی 25 ساله ملوان‌مذاکراتی‌داشته و قصد داره تارتار رو راضی کنه که بجای ایری این مدافع رو جذب کنند. مدیر برنامه افسرده همون ایجنتیه که با مستر خلیلی داداشیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/27299" target="_blank">📅 00:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27298">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZqbgES4uai_HhdKpu7gDu06wNjx3TNpakbPqkWSpnQU_Gej-h1DYpog5LlRARlHskseAa1frwPGhRrKH7qb99ZRT-65-n6VaEwa38Z2FyLtQWCKQk9x1vxbLaeHD_OHLit4ZBQAC8OBkurNpmVe7IBUNE7LVi_dtOsVkjxk1qI5z-wMggwedUd5QZeW--GN3d0AfWlEA5y2M1a04GzInEVycfzdAkSDyyGP9rVfmm94lDzF4UsjXr2Be2G_9LHxKHoM4eV-zCbjKRQ1jNNQ5FLOrofs8oGgqeQKlQ0qa-GQDneXJAHVLnJcMsQLdkahja3gkvY1cdgOUmvrrlXfxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌ امروز؛
از مصاف روسونری با آبی‌ های لندن دراندونزی تاتقابل دوستانه یونایتد و PSG
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/27298" target="_blank">📅 00:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27297">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVvCt9n0eX87B_FP_hbIkLxpssviD8zbdvumw__Utcizxbvk5q81p5MBfmKGQfrGRSZ6ZSiPhrZ6NYb7S0EE11wioEK7ON3ve91OoOhPAKYmSvtUi8CtJ4xe7oSZfvL6Mj-jLHU30McRaGTYiRvJoy_5Pr5ZUkwsKyKF4gb8nP5DgpC3Z_FOn1wvSrqmdAQDM7-ah3L2RLYA8oQ9b8Y61F1iDChtQkHIZJUNdQxFAeWNOVrDf4tWQue-8dV43VXQ1HjOXTfUvrUSBvYlFL78ovveYwbZMUB_JKwO17uCT0h0iuNaB3hQyGiM9Zxu5F2zznUgaQzzAkiZEekuKUotMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه تنها دیدار مهم‌ دیروز؛
برد شاگردان کمپانی مقابل استون ویلا در اردوی پیش فصل باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/27297" target="_blank">📅 00:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27296">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d08bf5d5.mp4?token=bvsRR-keewrabFNkEoR3VMPFIuHKjYX9lHRhksDxHIaFv_1bK0LfEb6mPzwiJyQuiCO6CxCHafn_kjq28l92rxopjNCoCDyLRauSMGZyMlu3blPgWNP6DC7HNiZyuqaHpWRhFY0o2CsZVfvDW5uEFBodw_x97EG5C-iT1yoRClgmEA0ER1FGL1-utnYCfj00vPajB3gFzBzAyPNCj1C9q99V_6JCwW6x-3zeKfSvmhzsajKyUaYFif0jJHvuSzvhwo_jJ0BiyUHXiLub_UZdnm4mjPVrPxDsTALaffODrRfjYlRvxnvZa50Bao4YJlYJaKM8UVek0MsyMBMKo1ZKSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d08bf5d5.mp4?token=bvsRR-keewrabFNkEoR3VMPFIuHKjYX9lHRhksDxHIaFv_1bK0LfEb6mPzwiJyQuiCO6CxCHafn_kjq28l92rxopjNCoCDyLRauSMGZyMlu3blPgWNP6DC7HNiZyuqaHpWRhFY0o2CsZVfvDW5uEFBodw_x97EG5C-iT1yoRClgmEA0ER1FGL1-utnYCfj00vPajB3gFzBzAyPNCj1C9q99V_6JCwW6x-3zeKfSvmhzsajKyUaYFif0jJHvuSzvhwo_jJ0BiyUHXiLub_UZdnm4mjPVrPxDsTALaffODrRfjYlRvxnvZa50Bao4YJlYJaKM8UVek0MsyMBMKo1ZKSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🟢
🔴
کوروش اژدهاکش ستاره 18 ساله فصل گذشته آلومینیوم اراک برای‌ عقدقراردادی پنج ساله با باشگاه‌پرسپولیس‌به‌توافق‌نهایی رسیده و سرخپوشان بزودی از پدیده فصل قبل رونمایی خواهند کرد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/27296" target="_blank">📅 00:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27295">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/198183711e.mp4?token=g_md-SH3WbwLYYgZzMhhWlRdxCWvTZt-DGOISQLcSb2rEJv8hQwzo7cpA_ZFGj66jGJmv3oqzXmcz49nzDkqWzjUe2P8ZRyXC_t_DaJiVvOaQyi9AMs2gIzLWToLKQ41ZgXMd57JLL0DlW9KsaZUyXupE_E805AwfNCpeps8JsqI2kmnZ2CXsU0rkF7czT9DzlYy_saE96J5WSLjKVM0TljEP4gRzVjST_f9IFkyIh00WyVgvOubwfLIw_g-bT-kMfsIZPFcnoIF0DMkMH-JaNK76ket32a9yIaNe8a3u9KRkMYAr30jPovXk0DiLlsvetEq8aumhiE6YkB2B0Mqow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/198183711e.mp4?token=g_md-SH3WbwLYYgZzMhhWlRdxCWvTZt-DGOISQLcSb2rEJv8hQwzo7cpA_ZFGj66jGJmv3oqzXmcz49nzDkqWzjUe2P8ZRyXC_t_DaJiVvOaQyi9AMs2gIzLWToLKQ41ZgXMd57JLL0DlW9KsaZUyXupE_E805AwfNCpeps8JsqI2kmnZ2CXsU0rkF7czT9DzlYy_saE96J5WSLjKVM0TljEP4gRzVjST_f9IFkyIh00WyVgvOubwfLIw_g-bT-kMfsIZPFcnoIF0DMkMH-JaNK76ket32a9yIaNe8a3u9KRkMYAr30jPovXk0DiLlsvetEq8aumhiE6YkB2B0Mqow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برسی ثروت و دارایی برگ ریزون مایکل جردن فوق‌ستاره سابق تیم ملی بستکبال آمریکا و NBM
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/27295" target="_blank">📅 23:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27294">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBRe0Th6xY2jzLv8GKborvFRPrN3nXt0eUS5MZoC2QrUyuhJn1hs4Kh5E_cB8IkhT0c-cMUeTQ9fa8v6LnCcdDN8ebm25bq4YRUpA9UtNscOcvC0tqNzOgnbK16OesBcddLj9cWNvg6uWRrgU2pnmwblMP48IOsUpMmvlU4yaj3bbYvDqYaoulZLb4ho09nVOn-h4DsIT_dcQJORYynPPpMR-sQyTc9Tb6-OTt8olUejFXrxijsTfPENkMXmaUmxgXRsDDsSxARrP-Ved9sZOl0ccG56sf7BqQX8Smd_kYvk92ySjfMaK3HqEcnkxCOCPBqWwQVtyF8Gm1rwGFi15g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
#فکت؛ هانسی‌فلیک ظرف‌دوسال حضور در باشگاه بارسلونا 55 میلیون یورو کمتر از مورینیویی که فقط دو ماه است به تیم رئال آمده هزینه کرده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27294" target="_blank">📅 23:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27293">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcL8HdNatJgKKtlPJm6xYNeADQ9-GTJTcd1ZD1bwrTm80wsGFRo5JGsnUtWnrXiGuFE8MWusqfUMP128G-uMv4jZW_Imr5PVRzZcWXIQPvxEsxeesRR3S9M7Trd-RvTfwoNqXPEPsi0daitNVAxeP3vc9dJNOSJivZcuUqUCFILqUXAbpSf5JnqY4W0AyKYeI-kmdpNvpojDdgGZoa2I7rRPqaILS36HAaW-rBniSJK_G_H96kIJjHhDQK4_9g5lDdKDWdGIBeCj6i6HbhSlfyr_BBnzGHrmHXYLrlkhCmeuezCSYK9L8lY3Wk09zVykSFR2EJ1HCQbwj45gLXp0XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زلاتان ابراهیموویچ اسطوره‌میلان در مصاحبه‌ای جدید از دوران مدرسه گفت؛ زمانی که یکی از معلم‌ هایش آینده‌ ای برای او متصور نبود و تصور می‌کرد این شاگرد پرجنب‌وجوش به‌جایی نمیرسد. اما زلاتان مسیر خودش را ساخت، در بزرگ‌ترین تیم‌های ایتالیا درخشید و ثابت کرد…</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27293" target="_blank">📅 23:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27292">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sz_DOJyxk4PfQdAfkl6QKvryQ9utqTumdMIst-7fSecE_uf2me_XbU8izTsKNV-Dc_BEFvRtRf2RvcPsVFGrNnUcvUmJKK-IrLDCaDPRrsb0-4g21S4vhhHdhRKgdIV9vJWHGZmqH9uHUy9rWglqQizpNbqGqFZZ7Zj740VoSB7T-iUOuHs_453Xqo_Ci_QWk3NgGsJRWqnKIfMy5hP6NTOdhrN0rouaf-LiJK5J6YygpCFyboWR6GlihwgpwrfHc9t-HByiDWoMSVEQxgOgBVG_K8NSjukbfS2gSnTmvSZn-ZhbO7Jt0GVSm7BULBOduM6UwqYjPdWeCWbuRzdgUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی پرشیانا؛
احسان پهلوان هافبک تهاجمی33ساله‌سابق پرسپولیس، ذوب آهن و فولادخوزستان‌مذاکراتی‌باباشگاه فجرسپاسی داشته تا درصورت توافق نهایی شاگرد رسول خطیبی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27292" target="_blank">📅 22:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27291">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cdzu7M9uvLJnNcEHYBhqAVGAd4RZvQPIaV2oUpTA5PSAu9xfDJQ1iUahW-57oqlVcLCQOidE9SOXsRWrMWkGa4uDvvKucpl9K7mbPb3PBbdZ5HyNG5jePpqZGyTyOU-gfoavfiaAXLNWBk39oQ-Q9Rnl0NLqO7l9tXGTatb4z039SM_YxagU4iS0lFUCgyBXly8n2CyL_NWZxSsROMDeEGOOa7Va8kYXIZVWoF9Ge22JUSysfb6xgDMvX184JPJlfi3diEbt58N-UgfZWXb728JfVvL4Zu-7PgGhIBU8UtBwfokOTTqI3JpVCumVzkVhgW2Y5j7xmV5KtbCWEHwb_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
پوسترباشگاه رئال‌مادرید برای یان دیومانده ستاره جدید خود؛ قرارداد تا سال 2033 امضا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27291" target="_blank">📅 22:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27290">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6EliXihIS2wt4YewWS4im7xYtNyAQivKkME3rvD0px-3czZTRY1HuGDrkm2pzSrKuSSv2o5Ax3YNCkYMRLIJIc6dtOi8MFq1P4Gm-JDNSPAxCRkb_OzSQQ_413E3DfU2mzfWhi-QYGTH5JZcu7CLrEWOZiN1SoDSj5SUXnwRjUGTd82jGTZyiUf_1P6S1AxOaNmZ7_kl24KSr6cnuI4wd4JN4HF5q_yf5uTBaCrYZrdgnwowrhScFInyTiz4QVm5NFXg_Hoq-nk0yGpJ_coJXfoYd98fKfzdrmNDmYumcipvvsdU7veZdSyS3D08mogotk7onbiwznvzp46aaZOBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
آنتونیو آدان زمانی که تازه به استقلال اومده بود با الحدادی زیاد حرف‌زد تااو رو راضی به پیوستن به استقلال کنه حالا مدیریت به آدان گفته‌‌ اند بار دیگر تلاشش رو بکار ببره و با منیر و همسرش صحبت کنه تا شاید آن‌ها برای بازگشت به استقلال راضی شوند.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27290" target="_blank">📅 22:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27289">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HiRaQxfWOWLJ7HROpKL5eggDbB06CUahRl12gx9MLHUtZnxs1nDPB3p1PUrngOjShXNMhCLzxHzkcqR7qC8xs37afoJGr3GoIdcetAdvrSw3z_8k36XTuQ17j5bTmKFUzogYgYi8puI1O23jOrIliL0AgTz3J1VuzNLmpJiTROhRWXeX6UB6gQni43YMpsvRFtRBHzeeMt3mpy7x9jbbF53dBGJZ8cr0_FrMmFfrJsMxw4hAzlqZz-ZxPcxGVBVYNpDfZvusPxPdVolILhNS9cqtJTPhBqSi7bn6P5bPlqv2kJcf-RfJVDdPbvTVoS7kIoKQ-g3lxPNxOqSqR8L1Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
به صلاح دید کادر فنی سرخپوشان؛ مجتبی فخریان و محمد حسین صادقی از لیست پرسپولیس برای دیدارفردامقابل آلومینیوم اراک خط خوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27289" target="_blank">📅 21:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27288">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRtPnNedkICph0YH92bROFtbH45Yj95DADK9b7ZuOM0iD59xIbzmE6uognW-7WBrd3u6vmuNHoE3iBjns2xW79IiK8snAu1OyZSk6P81Y5Hfo3w7L4qA45nZ3r3JKuYpCsxJgWmv_HXpoyDHZGad3syF01BlEc2NxlHijfRtJYn_x9p8SlgF7qdMj523L-ww4HmEV8QdttRTygvDvIddJliLzpTj7KViwXB_UYcuFM7pv56Vr_IEI8lgLxj8pdixNnXglpclakRwB9OFYbgCo7t7b6gCn_1D-veJJzVQzm7QTbYZpv5JCc8pK10QbgJset6LYdfKB_1kbelVIvrnKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه کوپه: انتقال رودی به بارسلونا نهایی شده. او دستمزد بسیار بالایی در بارسا دریافت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27288" target="_blank">📅 21:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27287">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3BoeZoeSMj9FGESKFAPIyQ1Da3kfYMtHOCff9Z-YVIg0k3v_QcK5f-3gsJrUa0mqfEpotl4QjCik106RuieGUH8iBwvRVpVFDBz6huirKHaQloLITe1-OxlndVBcKH3NXnqjNvHy4n57PIe2_IfW5725Q4tcQMpfvxojuZrbD9w_8b3V6Tw538kWn8DbbGh9Vp_UU2WYPzspfj_rAbNl-mS30pRBtiu6TyeDv3bXEmsDFNdqghDHGk0GtzR2Ttf288XQb3Cwxl8S-0nNgKfNFaJGldG1TUg7dBaLINplfLkkmn7OCx6VK0CUl3T8DQzo-Cd5NWgSw7vr9TjPCJnDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیریت تیم‌استقلال باایجنت‌های دیدیه اندونگ، موسی‌چنپو،داکنزنازون و آنتونیوآدان تماس‌‌های خود را آغازکرده و اعلام‌کرده‌هرچهار بازیکن‌رو برای فصل جدید میخواهد. اندونگ، آدان و نازون آمادگی خود را برای بازگشت به تهران اعلام کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27287" target="_blank">📅 21:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27286">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqSkewNppa4kDS0QpVHd5jFBL8cAIyXyLFgTl3g7Xy7uzFoiHjqEZ5aNmtCygq5yJfErc9F4SyqL9SLJUya56WcQBR5SejE4Vfus7K71RZBPm9N7GSlC-YcF_GFUfvmUmi34oZGPNq4cbJD2i9oYslrcZBB9AcIMv8xlnWRaFSGUnrgsgT29dpgpsKgYNZy96HUq-ulEwY9T46_SxwIZyLbMnvEKWrRvAPZmqkla0uso_zQ0jDU_rzbwtexX4961r3mJr2VvoUOjRfp-m_4dm6hLYJ9VX0I9SLDaijlixn-Xdwj8JEq4qfmy0uZKkGRTu6XxQgCPEupkSXd8qzunCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
⚪️
#افشاگری؛محسن خلیلی بدون هماهنگی با مهدی‌تارتار با امیرضا افسرده مدافع میانی 25 ساله ملوان‌مذاکراتی‌داشته و قصد داره تارتار رو راضی کنه که بجای ایری این مدافع رو جذب کنند. مدیر برنامه افسرده همون ایجنتیه که با مستر خلیلی داداشیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27286" target="_blank">📅 20:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27285">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiwbXNXy6RS9lbmokLDE99Y74kHiITvVxOSgyMp1ac_Ve31VxWbf7Mk03M4qcuYwzs6HA31uD9BwiKeX4ceIiF5gl_iL2SjBBluLOJpukx9NQcZkeREin1nSqzh0TiRa3SOJsk73QqW0DZ3yEc0J3_bz3aNu47FdAOrkzgZEvp_N3av6faaB4ivQg7KYEugSX8OMRsEQGDKGcXqorK7zfg9q8oFqD-EDobjQp3SS-uZWubOkC4cSomaGpmfnDPnqCW0n9S1WOlp-hNfAwjrQYBBMutIJpeq8Vj46RwWCzr4LeuNl-sEKJOQUPeV8PoPKoOvf_-rPMJ_Hig8OZaE_0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زلاتان ابراهیموویچ اسطوره‌میلان در مصاحبه‌ای جدید از دوران مدرسه گفت؛ زمانی که یکی از معلم‌ هایش آینده‌ ای برای او متصور نبود و تصور می‌کرد این شاگرد پرجنب‌وجوش به‌جایی نمیرسد. اما زلاتان مسیر خودش را ساخت، در بزرگ‌ترین تیم‌های ایتالیا درخشید و ثابت کرد…</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27285" target="_blank">📅 20:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27284">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-YVOyyqXEtlHYXJh10essL3ag7Pxge4vyGlwZCYx98PIzPW2asuayxgGlLnabkTGMDUOK585gnKCIAs43K-bttdMthsI4BUiNs7zEW0caQPtbbQZdyYXjWlTEz9EFIGPaTtCy03TTBGjdL5vZ0aJiPEHAAujuD_gFb82PtUwXpsofX3-41vFGRZAX9VixTbg4YCwJocCkh4uxZVgsx-CA7fmxI8t7O0358SrpaWokagV3jTYBgBdWhr8L2b2rKpvmM6Gvsu99WufAdzEKwyPuGJ7c4vIiz_hRxfDKSnJkMUYiJbx_gJMvOIXUi6xtmtGvhpm6ZNC2p0JFTkNtfLWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ آنتونیو آدان موافقت خود را برای بازگشت به استقلال به‌مدیریت‌آبی‌هااعلام کرده و این گلر اسپانیایی بزودی به جمع آبی‌ها باز خواهد گشت. باشگاه در تلاشه تا نازون و جنپو رو نیز برگردونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/27284" target="_blank">📅 20:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27283">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be754a68a.mp4?token=q79jF34C8q_nYIV4QDhoqrpW2D0KdZROx0Q0UARNOQzvJLcOCTjIr0qxkP7K0ZPqj2K7M6yoqvg1kHEecdAjGEe8CKdeeBhI5-NgFhDYb8BJG4BHrf6Vf0QY-eplXMklscStZK3LWPF3o8GRvGkU5-7Sgq10s25Y4km9WDHZImDpanLyJQArQeHaOyoY1LB-uQmtR0zC-R5DBwHDaFSmKzq2SODDvXfrVVszGpbwZRZ3PmWwqdqc1zM1qCps9N8Xh1mYUKz1hJtzfay2QjER1wDPBYzK84MTvsxmipkut32QKdwdK7Xqu_IljApstz7XA5vRJ_G_utZ1brgEW16kiFFPld9zEKVtuyn0s7nNzJvgjZ5BZ2ZAxvJQC656PMW2330ucYtpbhBnEjZw9k5o7Xh3gi_XfRqrT5Imp_KtIA0Gl6jGKlKNcU4ud9ErT96ZcWjP3HWl80wV322EZSt88ndL5e_w9SbWpcSLpo3t6OUS-CiDSXdA-TR4FzhA8p4gVXLSVV7ElBySAS2gHpPeui-64hHDF5bTsYHJXBE0v4-_Z7sxHeJGHC2meYxjIUwLbM48oh1NIgTYcMdwqYjI-1QpBNVfi_DqcXACgqWgCg1TS-FkvZR4MiFIqnSUCnhXlbLC2HjPt2GxOgZooVoZlasWmALSU6WvUWp2Wl2S3jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be754a68a.mp4?token=q79jF34C8q_nYIV4QDhoqrpW2D0KdZROx0Q0UARNOQzvJLcOCTjIr0qxkP7K0ZPqj2K7M6yoqvg1kHEecdAjGEe8CKdeeBhI5-NgFhDYb8BJG4BHrf6Vf0QY-eplXMklscStZK3LWPF3o8GRvGkU5-7Sgq10s25Y4km9WDHZImDpanLyJQArQeHaOyoY1LB-uQmtR0zC-R5DBwHDaFSmKzq2SODDvXfrVVszGpbwZRZ3PmWwqdqc1zM1qCps9N8Xh1mYUKz1hJtzfay2QjER1wDPBYzK84MTvsxmipkut32QKdwdK7Xqu_IljApstz7XA5vRJ_G_utZ1brgEW16kiFFPld9zEKVtuyn0s7nNzJvgjZ5BZ2ZAxvJQC656PMW2330ucYtpbhBnEjZw9k5o7Xh3gi_XfRqrT5Imp_KtIA0Gl6jGKlKNcU4ud9ErT96ZcWjP3HWl80wV322EZSt88ndL5e_w9SbWpcSLpo3t6OUS-CiDSXdA-TR4FzhA8p4gVXLSVV7ElBySAS2gHpPeui-64hHDF5bTsYHJXBE0v4-_Z7sxHeJGHC2meYxjIUwLbM48oh1NIgTYcMdwqYjI-1QpBNVfi_DqcXACgqWgCg1TS-FkvZR4MiFIqnSUCnhXlbLC2HjPt2GxOgZooVoZlasWmALSU6WvUWp2Wl2S3jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمیدمعصومی‌نژاد خبرنگارسابق صداوسیما هم فهمیده که نون تو فضای مجازی و ویو گرفتنه؛ حالا ببینید چه ویدیویی گرفته از مردم شهر رمِ ایتالیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27283" target="_blank">📅 19:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27282">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a5e9dd3a.mp4?token=pZF0olDcDpe5a9uyaT80L1HBW5bjpE9y5jXmw1_KUnKGhCGu7mSyoNwfVCDQXqmKBPFpIaI2vSF76PyRxuF7ntunlsoH8FWNpqpvzZMFzjDl2EyHJ6xjhvZ8Gle6Qv7ocaPwUWoopEpfe35Yg48-iwjXjdgScPgMG3EpBq9ty9rUgXCfPe30SIas_5vkCth3pnhO0R4CpmK4e3z--Ckhh2dBthE9QTiBsWUacXhOVio9kmI9e2pC3Fuf1LEUk-1bZ6Y6QR0cdPivc3y5EQhyuVN_dFVRWIht5abdNaBa0gKaBvCiXPjOo0OElCyIJDnWz8oOT8gVbHfxhV2a3E6X9ZVe9sdW5JQFuVGX5LO_lof_lF7cZ-YJxRn9WzzazhYbbT4xYJwl810NnhKOF4x0o83JMwFGJUw1dSxRYJ1M_O3Ha5RpOgtAd6R_7r_OrWC2nT1sBdxYD_c4CFSGk-CvPQk4jSYvDUii5XXaQ9ufWlldPilv91W6FcMZKEP05OuAilxUTaMni2dTTSxW4TrZgIXJalVPQpVRMG_64bD8d5Q48-wqC0Pdp7eHljLKW7iI5a-ebQjhXjXfjHSVFXM8iPj-XkOxh2dVdAc7sKdkfFR_lkukz0grJ9_ddC0J5lmKZwMWbLFRR8NN9OPCeIk4N75dve7Cu8zqMBzlwz7sOx4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a5e9dd3a.mp4?token=pZF0olDcDpe5a9uyaT80L1HBW5bjpE9y5jXmw1_KUnKGhCGu7mSyoNwfVCDQXqmKBPFpIaI2vSF76PyRxuF7ntunlsoH8FWNpqpvzZMFzjDl2EyHJ6xjhvZ8Gle6Qv7ocaPwUWoopEpfe35Yg48-iwjXjdgScPgMG3EpBq9ty9rUgXCfPe30SIas_5vkCth3pnhO0R4CpmK4e3z--Ckhh2dBthE9QTiBsWUacXhOVio9kmI9e2pC3Fuf1LEUk-1bZ6Y6QR0cdPivc3y5EQhyuVN_dFVRWIht5abdNaBa0gKaBvCiXPjOo0OElCyIJDnWz8oOT8gVbHfxhV2a3E6X9ZVe9sdW5JQFuVGX5LO_lof_lF7cZ-YJxRn9WzzazhYbbT4xYJwl810NnhKOF4x0o83JMwFGJUw1dSxRYJ1M_O3Ha5RpOgtAd6R_7r_OrWC2nT1sBdxYD_c4CFSGk-CvPQk4jSYvDUii5XXaQ9ufWlldPilv91W6FcMZKEP05OuAilxUTaMni2dTTSxW4TrZgIXJalVPQpVRMG_64bD8d5Q48-wqC0Pdp7eHljLKW7iI5a-ebQjhXjXfjHSVFXM8iPj-XkOxh2dVdAc7sKdkfFR_lkukz0grJ9_ddC0J5lmKZwMWbLFRR8NN9OPCeIk4N75dve7Cu8zqMBzlwz7sOx4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خون ‌دماغ شدن شرکت‌کننده زیر فشار؛
اتفاق غیرمنتظره در جریان یکی از آیتم‌های فینال «مردان آهنین» درجریان‌یکی‌ازآیتم‌های برنامه مردان آهنین، یکی از شرکت‌کنندگان در اجرای حرکت دچار خون‌ دماغ شد؛ اتفاقی که برای لحظاتی روند مسابقه را تحت‌تأثیرقرارداد بطوریکه از ادامه رقابت بازماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27282" target="_blank">📅 19:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27281">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRun6J75UFSWoFQQPWlwwuLcOxPirzSypGpbz-0g-d9jYWzOVcYBSDUnxEk9IEsd6I65VbjFxhgmpwnniUYEB2NzwhMxOzKIWmt7gSN1AEL54oRoT9jQQB553XGBGQ4YmpjLFv00ioiiaGf5D-eI9PNBmb2ZWWvNcPGIgQhHCBzcUBQiWDFsFA5XK-PSezVJZavT_Dv_exyA7ZdrHEdbVZntZQdAEKuf8Ax9qeIgCP5TPGgDRrKdAh0VejfGaQsEGvWE-WF-bjO_yvG1I55i_0np6jmIzSI81ko1PM21kMddaHYYD7R1p-AMn24KnROa78pbikTQ_8ogRppDzm6LUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال با نیما اندرز مدافع راست 20 ساله لگانس واردمذاکره‌شده تا درصورت توافق نهایی قراردادی پنج ساله با این بازیکن آینده دار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/27281" target="_blank">📅 19:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27280">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/335a6e2e8f.mp4?token=iTBl0mD6f4oWYKhI47JER3uk-kGQpcWaWx9R66c8QmJ0S9P7WyvTHzXusQxgJwGdnrHIIfC5PTwXhJWrnkwu6xn_sdcrjDYv3B-nc4AF8GYTDVMeqwov1FH3d0yYgKjyFy_DeXyGoElCjIjgfEW3I_5Cwyt5cc_YsXwo2-gsjsiGPjTakUajWJRDMUH6eUsPRMe5NkAWdi2Fc4NpU2NjfUMEw-hVJv_1vju6rPCM18qABTMfOTMPnfgXkI3-cA-U1Vlq0ImibJYp4PyPM68NhOJ0iP-fMK8cSGP6P20awJSr4ZUBINx-B8icLFI3MdCM0sBATM4dAvLQEHOXqKdCnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/335a6e2e8f.mp4?token=iTBl0mD6f4oWYKhI47JER3uk-kGQpcWaWx9R66c8QmJ0S9P7WyvTHzXusQxgJwGdnrHIIfC5PTwXhJWrnkwu6xn_sdcrjDYv3B-nc4AF8GYTDVMeqwov1FH3d0yYgKjyFy_DeXyGoElCjIjgfEW3I_5Cwyt5cc_YsXwo2-gsjsiGPjTakUajWJRDMUH6eUsPRMe5NkAWdi2Fc4NpU2NjfUMEw-hVJv_1vju6rPCM18qABTMfOTMPnfgXkI3-cA-U1Vlq0ImibJYp4PyPM68NhOJ0iP-fMK8cSGP6P20awJSr4ZUBINx-B8icLFI3MdCM0sBATM4dAvLQEHOXqKdCnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
از دو شهروند بلژیکی پرسیدن که حاضر بودین به جای زندگی در بلژیک در ایران زندگی میکردین؛ خودتون پاسخشون رو ببینید‌. چقدر تلخ بود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27280" target="_blank">📅 19:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27279">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gx-bFgFBHXDFZQvDtcv9iWgBBBJ0Uc3KMFGO1Tkqjep3uGtFKsK_gQWxSt_IsSbELesxBJb3M16QqWoWg0GoPUP-_ElAnm-u0WUHCe4JuPAGYJVPLS3fPDKXvWlrNoOUBNhHbdklH4GTME1H8bm4B0OWgoyvo3XLRNTQ6qY6v4q3lSSpweMx2oTNoPDIUQy2fqc4GEd1Gbrbv5Q92cRY0vUHPkpdJlLzy4jVyhGT4yVfqbC1uph3w8SHGv69fv-aSMzNKLXqyuHkV8wRC-uA2AL250WvGc4kImEvRhelo6Y1NHzfd2eHxUr-5vx0ijikwX_3iO6p13PEvgXHxSRCBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ باشگاه بارسلونا به‌ زودی با پرداخت رقمی بین 8 الی 15 میلیون‌یورو به الهلال عربستان؛ قرارداد ژائو کانسلو مدافع راست پرتغالی خود را از قرضی‌به‌قطعی تبدیل خواهد کرد و قراردادی جدید به مدت سه فصل با این بازیکن امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/27279" target="_blank">📅 18:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27278">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcLEaK-BDCP42Han_ZcVJc5QR_EuaGcZC5BBMp4I5Hnd9qLPo77Cyy6DTvgzeIJfXr-5u34kSV9LL_CiJTq-_zWwrrUU3R1NlD8RwkLzQg3WL5G6hIgRKM28IC5E50Z0INMJUAMM-dDMJIrDKU6Qfm6AXctFB4_yS2808fsPBUgETZA2rHiXhzvXU3FBFfkrQAl6Hns4s2gfkoSW4KtpyPLVWQo5Uh2pDM_Dp_kOpc1FDawxpb8-0CcFsIQapBfv8cGxky5CANYblGzuzJwtbTnyBpHBQqP8dWciNUBkadb6IqlavYLICC8LGNAkK-An0dEGJ6vXSlr83YgDOO0xTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار امروزظهر درتماس تلفنی با پیمان حدادی مدیر عامل پرسپولیس بار دیگر تاکید ویژه‌ ای روجذب دانیال‌ایری داشته و به حدادی اعلام کرده که هرچه‌ زودتر رقم رضایت‌نامه این بازیکن رو به باشگاه نساجی پرداخت کنه و ایری رو به پرسپولیس بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27278" target="_blank">📅 18:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27277">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZDWptqnEjfojfm0lezkw92-KgqYQJTCL_FlFkOAjERB08_p5MyJdHr0JIMk0bwzfiVxsw8FDs7ZQYdYCwEnnPOR_IdQmCtvGxKBNgZqxIme1srJs30tufNuKPeM62zsN9by57VT0_OmcorX585sq_hrlXzS5mCD1tlTrqSmrARjWDmyazxBOdZzE_1fZaSZd34Yaj2VL64jneYy-17PF9SYoG6q_qU-J54D0r-Mf1m-eo0NYZN6O4pPcTONIYXo4quLhne41dsOuBE0-cC399rvzkk-2aHLmDC_tOhA2CQEapds0Rl8L_N_PD8vRvKuQIjmA071SfegzhslYy9DKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#اختصاصی‌پرشیانا:شهاب‌زندی‌مدیرعامل موفق نساجی در گفتگویی کوتاه با رسانه پرشیانا اعلام کرد منتظر دریافت مبلغ رضایت نامه دانیال ایری از سوی پرسپولیس هستند تا این انتقال این هفته نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27277" target="_blank">📅 18:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27276">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwdQ3LesPkl1hRQ-p-NtUVpl7Io2B1d56ykw18G0bLVveoBVMDT0QYQ8q11DxLTvfpV0psnxT6UkFSr9KQsJxdvp2H0TrbkLP0-QtuzCVadD3vAd_JHgXATq9-f38OkeM3MrVap1igv7cAZ1R4caDlIusHBBRTwegn_Knw3dJ9e9r3TFJV_FiL0iy3-XgyuqQIfCuyKihgEuYmF9ocO8EdrGHAMjJQI4O_fbhCLIfQ1DPhjDNkizaZoADAvn4eo9BN_7VJVDpcYc_IKB5N_8Y1xBjpvwsFxi0JlRH3bDKsl_uR0EjCTmFYwSOduFMEVPPdTK0DOTeX_t1ukfa8GauQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرانکو ماسانتوئونو ستاره آرژانتینی رئال مادرید باعقدقراردادی قرضی یکساله به فیورنتینا پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27276" target="_blank">📅 18:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27273">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s_u0D-VeRE7XzfnjKwUakQ7pAN-ulungxrJmLiKMibwbSWhE88VEzu80-HTf3F2onb4ViphpU4fG2LCBmCs8FmoP8YiHgezrJQmQ05gyDZNCSqg64PhhlY3lJnfCotf2eBDPe9fUiOLh6pj0oK4t_XNcZdgRKiR4aaXIy8Ul768EpZ7hkuPsDmpo9CZXw-NS43zL8Ss7j3ZJOrf67gTuxvLSTUzAcAJWQFAonbPwRsloRf9ecgunyGyIUZfNxGA_P2kEJYhRdYUFqE8Y-E8SFq4tPpH2Lrby1wTV755FQ4PRHTH-Jraekh5vsu0FBHPTncL3pU1eQtUMC8SW6iLjDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fvxBw7_fFm8hwMxoSaWlGrEbHqdAlXrovjiD3VNsI3j24iMeBpM2d98LPg1B4sK4Yi6xIRpQw3xlJBS9wFY5ZeKg2uIJmxBN0xGDs2LnSCGGEHGqMswDuHsokVuGA6H_5BRfv-gd6x-KmlBMto6lFPNOP5TqSx-858xGURTSWzk8c0_LG7yhctBKp4dHUQHBIVl6fH_QJTB-EFx1kIUsQTnQXhZh1INEsppR9dFcLIDRZjwxLergDF6SRvtArbLGpBqoTTUjWUq6soz8jhYI8iiim86zkQESiJ3OFsB5qC35tWS1q1g4eYpJ5dSXzyIeieCT5Y40bq7g14AUA7gOoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
مارک کوکوریا مدافع چپ تیم اسپانیا به وعده‌اش عمل کرد و عکس دلافوئینته رو روی بازو‌ش تتو کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27273" target="_blank">📅 17:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27272">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMffyLNJNJ5PYp8UaH7u82Dr4tPP4G5V5UnfE-wzAutRDniFa0JkgmyrgQ43kKF-r-sDRt0o1cx8xqUVn2-txPq5kErsFDtB9H6bxi4rD7InEazmTgGbM8Avi5ugacixSihydLVGRdFzQXa9l48GQgfC3_JHP2hHbrISRfXT_X_cnuTjn3qoSaCD05-Qod99mZJqWPVersaA0zi6HqZiZTJMsvyd5CTNyrvk9bOEfBF-XgCQtngM6i59UzAbComKegPg1AnLjrEFF3q4pBZEl7axahPqO0dqN097Ax10ytUz1ATUm2NaaZHPILeISfdyG-ezdh_ztK9u1h75RQ0kJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سردار دورسون مهاجم35ساله‌سابق پرسپولیس وفصل گذشته تیم کوچائلی‌ اسپور، با قرار دادی یک‌ ساله به تیم گازیانتپ در سوپرلیگ ترکیه پیوست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27272" target="_blank">📅 17:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27271">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNCu64jQz6PzF-cm7HyiNoU4ONNkKUOSUYHatkAFKLOYpNqo30FAKY7i-kOuy-rnHgJY5VMs3eNdaJtde7Qym87BWp3jaIJ_6cnN-hP1cwpbdNe2rSRRRQ2VNSTwKS7wDEycr2Kc8hN09PQQIis5GRGMCZ1RQDAd7eQscuQF5N0Nv_2FOIYEAuKgKZbG_Ch0t9_Chsld8PE3nSdu3YlQs_qW882tbYf-T9RMN1sKOgUeujt4KXomcmXrFXR-es1jhj_DyZZiWnT791llFH4Pt4Lnzoalr-pnamGeO1JMItXU2eQwcK-JkjHLf5lUI5ssogJSNLnshpfM6xVpn6ITpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ مهران احمدی هافبک تهاجمی تیم استقلال به دلیل مصدومیت دیدار هفته اول با مس شهر بابک رو از دست داد. باتوجه به این رقابت های این فصل بسیار فشرده‌تر از فصل قبل برگزار میشه‌. اگه‌دوره‌بدنسازی‌خوب انجام‌نشده‌باشه دهن بازیکنان لیگ‌برتری سرویسه‌. هرسه روز…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/27271" target="_blank">📅 16:48 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27270">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ib8sSh6DT1LXzPfdP1weCUfh05F-oEArfQdjUyzYUyO7VVMW0I2i3lprtV0erItATVFqCw5dhY3WU7pAGHO7ET1HWMCerA7yJ1J03FjHZuTgdkBwOut5Ah3391HpV3TlldrgarGbVDgE8eHToSwBiMtxhJQTg9Ye_j1M79amFPk64c6ZJ65HfTrW5F8_aw1EeSYmCBgEkpKtWGBzmX4SN6vmImzyanvFPqzVMvcBVbwdGv7Q8fKISIiYlcrRSR4MVmCXtjOCUQbyj_Wn2gxSDv0bJKJ2TzS9NRglBsrZE1kCY54i4N6c3Gu0n-udeXfdw-0NRXYW_oe4KD0GspByJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
ازابتدای‌فصل۲۰۰۰-۲۰۰۱ تاکنون، منچستریونایتد و منچسترسیتی باکسب ۲۶ جام در صدر پرافتخارترین باشگاه‌های انگلیس قرار دارند.
چلسی با ۲۵ عنوان در تعقیب این دو تیمه و لیورپول و آرسنال نیز در رده‌های‌بعدی قرار گرفته‌اند. این آمار بر اساس مجموع قهرمانی‌های داخلی و بین‌المللی از فصل ۲۰۰۰-۲۰۰۱ تا امروز جمع آوری شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27270" target="_blank">📅 16:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27269">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2Vfgj42l2Lc8Eb7cUbT_FYyF6IFyNGiMe2UP-cJJTCnzMMV8JY0ZO0NG8t37PIAq9MSHqKYMTRxWMO8TdmgxSixeTuzf4mTDUsitwD8BCtu1vC1hgzz_tfvnzAd71V9lo-eDGVEXayv1aNyEzQSn4G_v8fv4ATWcrwfNCFX5M4G7_50TgGlplUu3KmRYiaW2H0hTRqlDEOqWXkBZWkTA953-ox_qnDPnbKM2DmCj5mOCOY1-otVkx73V5dh2NvfX4R1ZyUPZuPhiprt71qnN-5KO85hztWI2zBR6L6Ptzwqn4Q3Otnbgymzfyl3TLbIGUxA6FD_c-2wKpNUPMZVpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ محمد جواد حسین نژاد دقایقی قبل ضمن تشکر از باشگاه پرسپولیس آفر این تیم رو ردکرد و به‌پیمان‌حدادی مدیرعامل‌سرخپوشان اعلام کرده که فعلا قصد نداره به لیگ برتر ایران برگرده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27269" target="_blank">📅 16:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27268">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LF1vcvjXOLuQfsoNhjSoPCiVCdfQwEHM0MZl3m-SQYb6qoZZxDWUwQJe9Zifgy1f7pEqdgA-BPKJQ1d7sClBc4w4_ypkS3gjyJunIDRR1psbAOukhzE-oZR6BQpwL8eJ2cQ5pR0c5RwpGlcp_dwoNTZT7aelMI3l1jiSp1XE4q7lM2jicy3HvGijqMJrny5E3D44rU_GLqbV7dCPznEJCSm9s5laJOVWDxIUVEhsOg0_0cRJIbvB28igDAfRN7bs0HqH6LQWAUTp6ySUUgyRApLmk8BKlAmUCyc5zFwc7m9_b6Sy5QdPMQ0VBUYPcO8w-iDWaFgUMk7KIp1yu6gVaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی‌پرشیانا #فوری؛ تلاش پرسپولیس برای سرخپوش‌کردن‌فوق‌ستاره‌ایرانی ماخاچ قلعه‌.
🔴
طبق اخبار دریافتی پرشیانا؛ مدیریت پرسپولیس ساعتی‌قبل‌باارسال‌ایمیلی‌رسمی به باشگاه‌ماخاچ قلعه آمادگی خود را برای پرداخت رضایت نامه دو میلیون یورویی محمد جواد حسین نژاد…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27268" target="_blank">📅 15:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27267">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsYjvG8oi1JvaLkrlxDpIDvYtruYfcJgPILmTt5iulBOrwx5objThKLA8pdP5qmmMF_jXL8II04AhWY41iVAQEqhEVn9h6AwdQRT_g5xfBVKUUBB5q-lfeipvm92Wq9gAnupLY1Z2RllUM9Cnxe9zly0YFYBkmL8RU8UCWahLJ-0GQcpxBxshXG2OH_IaBdEDoi_-2GPWNTFNdPHWw-h3KGME0JizbliKj5NdIe1kAMeDygEn28nbZhK-WaNt6UJeQesjyjekAPisF_6CQu50PSNLRovfhRENBlFJOJlIOS_NpbyNlmHSZAh6yoFNo64kD3Zpffn2cYb5OoYVMG9nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تفاوت برگ ریزون و عجیب پاداش قهرمانی در سری آ ایتالیا و پاداش صعود به لیگ برتر انگلیس:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27267" target="_blank">📅 15:46 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27265">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tcRMZMGHUfwTcHzdEzmd1yOHbzkMWuWcr57zCMjDdXdCWrrf0rw6jZ0IbUnk640dg8ehpUCssaDtN6hs3IBkrZ4BqfjLKHW4jGKW8kbZmuy8lfWviqfnHaD0vxOP4Ivng2hiPbQTws7H5SmkIlmJzLrvTJ9txfLNTUXrpDjwG4n_lSePN_7lOB-LUpVwOqA8NuRAdzx96FVDGZbYwcuqQuMrrKiOzl9-ERgTUn5aTRXT6KsDfPkrHfpeQhjKUxeTwDscpamsOJceBx2edaKbDh3zaAI_OcYI2Zzji6D89iX6bjdB-7EiKm2MLHP5vd4ymlDLuyJ8iha7ppx9eI7QGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fEHfg0uUG0m77_8gy-C4XoANs6rXGivXZ1lflIxpKxtxsv76_o-GQ-X2hRIzzycduDfMvaEoSehMv4Y3HtTt2-42pjopssalFRc_-1hC8HyNTkFr5OKH1e6ELJ-e7d_Cg1kVcIWawRdzVKL11_uzs32igqEQ3m3IVCjSywsE_BfY3AbDAJRjN5kw5eoGAPHFb1tMhpUETV5_8OCVNUdOjE5Ujr4Y071TvQVJIHhBoTBI17heBWKWV2Zdtu3bRk_N50fY6CcckCQTlDDd_bETbz0ReokGOxCV9XVC7guyiT9uR7Et50toBnYPmUiipr5xtnwjD9tCAq-xp5QUrZ82aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ژائو فلیکس ستاره پرتغالی تیم النصر: هر آنچه چیزی که یک دختر در یک رابطه میخواهد در اختیار مارگاریدا قراردادم امانشان‌دادلیاقت من رو نداشته.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27265" target="_blank">📅 15:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27264">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9fBi9EvUv8RZOeXCdfvW5gCf9I1XU0q4lpxwP1d4D1ZoTWSdscv-VXEjSm2vB3dVniRk7OEkJDQ60XbF0LF7qIIQscVfwFxQNIRrH3-76F0R2Z0O0QBLIQPCF4qM-uLgzY4fEYxbJrhewbyhb-aPka2JSFCkIkEhRXV-KnSXgus5PirYw24Myjp9NxI8R23rffBMbkjYEsdTUxdfh0MZ_OEYa5a2U44Polzm0M5pWNzSx7WnkzlmzzQlrxUXjX-lkOmgKAL0TeSn4YO9vUOmHORWG7r3QNyyMutgSk6HLJtlXk2IOzu8mHMlV3gXG8OV1ly3ezG80NqEIhb0qvr_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
سردار دورسون مهاجم34ساله‌سابق باشگاه پرسپولیس: شاید در چند ماه آینده دوباره به باشگاه پرسپولیس برگردم. من عاشق کشور ایران هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27264" target="_blank">📅 15:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27263">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWfiN7eVI7XuKlYJfsKE8YxmbOsvbhXM3XHXfIGSipLDXDZzf1087I2fk3Gk2fO-2zDDnuqNMRfy9sonELpdiyYGZBZe5o14u0wa103fhutHLlu_x8FPHQXTfuZ3MJJK9NMGNyEybj8D1uu18pQh0ygb7aD4bQiSgfPTsWgRWun5elI70Za2XDpR9xlM6M9bD3ZnB-au2m3UZA9UZaSVvbY0JlkAK6BGEFbEUihFr-YGCgeYChomHezs3j4GxkGVTSDvIGUacCLcMIsEJz-w73KO1K_Jeu9p_7CDrIKnEptyr1teo4Tv87e_bcvEuZjfjrOFxz2fdzKe-QqJR2paRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟠
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال در تماس با مدیریت فولاد خوزستان آمادگی‌ خود را برای‌پرداخت‌رضایت نامه یوسف مزرعه وینگر چپ تکنیکی‌این‌تیم اعلام کرده و این بازیکن بزودی با عقد قراردادی چهار ساله به استقلال خواهد پیوست.
🔵
باشگاه‌استقلال پیش‌تر باخود…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27263" target="_blank">📅 14:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27262">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMr-2PFr3LNSUHSthGZk7sL1fd7zFK0tUxLSG9IL01BDmfh-j-pEaGD2uu8TtiFU0ji_Zs1qAYbiPDdxCvFoOMQaqKz2X0X381J4oyGz45gll5KhGya9_Whd5OHKml5HAwT_fPd25WHsA6gidxyCxYft-f8TnHbJw94ssp4DVrzLnldHOtwy9d8Hy-QqX9A2Fr9S6q7wrI_39A760wA-ZEsmL1eZzhXxtY1JMFTyuMvO4Zl73K8g8F1D7AoC7hBxLLO7QL3HyRtZ8dtm-PJQgHOkoGfB1FA6zbH7thI2iaYTC7Xpcv1XE3WLAzuyvuZw1Fuba6-yDYq0IhiwI9wEtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛ رودری ستاره تیم‌ملی‌اسپانیا رسما با فلورنتینو پرز تماس گرفته و ضمن‌تشکر از پیشنهاد این باشگاه اعلام کرده که برای فصل آینده بارسلونا رو انتخاب کرده و راهی این تیم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27262" target="_blank">📅 14:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27261">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTVJPvu6-JGEcf3XkG2RXRJWxRnpybdIXVFNexAuu3kdPJbwgNoAXCP-dcFXxolImcoJssHNWydXPBgjC7zbyipN1HCSRPJZtCWfrFMr_lG4Aema_-J4Oc0TB2q-IANJos32OMw_GR1HcV6iIrgJg1YKfZyYDGtiX4ZN8i2KoUj57RI4S0gP6MPUdxLNaA7LZ7XpCQB72hc6ggWCwR1nnnj5RGuYaaa_rNSgyoXJXYMEK0AXl-FGoxT4DoVhzOsNukcezLxF6HhIhqwr2xwc-ly84rl1NrvF1vcwppck8PJq7M8f556dInTohAiEWCuEk5SIR77L6kAp0qGh78piiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌تارتارسرمربی‌پرسپولیس باردیگر در تماس تلفنی به مدیریت باشگاه اعلام کرده نیازی به حضور تیوی بیفوما و دنیل گرا ندارد و این دو بازیکن رو در لیست مازاد سرخ‌ها قرار داده. اورونوف، سرگیف و باکیچ 3 خارجیکه تارتار سبک‌بازیشون رو پذیرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27261" target="_blank">📅 14:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27260">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FomJUnjr9xJD1Psc2ORspslaP_PpKN-CHJr3O6ghfoWMIkdi26cOJ-I_tNah6RiNXPgVArQmXh8CkiwylBcHr1284MjjBfN5qEvQMaengBDQ7HX83KpKtiMdxjLX0V74jTaaUztvIqeXX95GLIEczmJ3Yk05WTMRueb4Up43NmbbwD8niliyH6p2GVSMctMUTwWQcfjvj-cokutoQiK_Wiqv7yiwD7OxJAsG8ysj2hseDVCSzGhmAdFIsNzPMvlK87dO9sbg1nUAsQKRKdOnTVvzdUQPAmCnYKwgtGQlLInW6uwccPEGAu3EN7OTUV-doKULL2uaXXDuk13fILgVbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شایعاتی منتشر شده که آقای فران تورس که با زدن گل قهرمانی اسپانیا حسابی نونش تو روغنه حالا با خانوم مارگاریدا اکس ژائو فلیکس که اتفاقا ایشون در طول رابطه‌ش با فلیکس 3 بار بهش خیانت کرد وارد رابطه شده است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27260" target="_blank">📅 14:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27259">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cab8b5b02b.mp4?token=AynERFrywzcdLxqyDbVMR-rk6sVUNJ38z0T8RiB3GYsqfVaAXb4lqHXEg7DGz0u5c1Om5rg6UF3SaNYS35Dgw3TSgJ3caeemaTZZ0iivl_uLLDiGMRjWK3C_mwvJ8eT7EDEWe2bT6Gw-cQ0_ir4joO-h8CIkixXMOY7XRoYkt3CmSGugw99e_2vekLNx5lOuZmDaR4tsCXg9JpEiIF1xEL2MRamgZynFrpRV_N3wusuArFPmZ_o13Ws-CpSgdqaue0qhy8QjeyB4-tlIS_hk-RGCQkiorW8xqoSiZ3hrYPlKgUKGyvNllYjx7xe3halxQcmm3lONQoW658_vG3kv06s-ASkJ2GoSQuPY1o0QzLwrhSa0WxSEYn_KVt0IXvFrfXHJ7yFSDy1Ld8f0eb1WYAdQwi5ugKJ8z9si-ErzCHyuDiXSISOjD9QwsEhAmZvGCRln_sZ9YDCdFrRQeX7dxDtKHVj4J9Ic3tHZlzlBQc67OU2WHXPw4vqfS4Dir0g_gNWsZuUOU-RtdtXvkZk6LmKapipXOxTk9jfnPwS3y3COKuWvqO3aOp5QgrYX7ISBvyzVVL5VDZ1oWl-XMGZGN0ZZF3RopmkYmS-Ime4nrJAxMXNqtCcWSrVIn7QQup43rOgyCgxpYfKNcEW8DUEU_hoFILUYcAuNZ3qHROAM94k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cab8b5b02b.mp4?token=AynERFrywzcdLxqyDbVMR-rk6sVUNJ38z0T8RiB3GYsqfVaAXb4lqHXEg7DGz0u5c1Om5rg6UF3SaNYS35Dgw3TSgJ3caeemaTZZ0iivl_uLLDiGMRjWK3C_mwvJ8eT7EDEWe2bT6Gw-cQ0_ir4joO-h8CIkixXMOY7XRoYkt3CmSGugw99e_2vekLNx5lOuZmDaR4tsCXg9JpEiIF1xEL2MRamgZynFrpRV_N3wusuArFPmZ_o13Ws-CpSgdqaue0qhy8QjeyB4-tlIS_hk-RGCQkiorW8xqoSiZ3hrYPlKgUKGyvNllYjx7xe3halxQcmm3lONQoW658_vG3kv06s-ASkJ2GoSQuPY1o0QzLwrhSa0WxSEYn_KVt0IXvFrfXHJ7yFSDy1Ld8f0eb1WYAdQwi5ugKJ8z9si-ErzCHyuDiXSISOjD9QwsEhAmZvGCRln_sZ9YDCdFrRQeX7dxDtKHVj4J9Ic3tHZlzlBQc67OU2WHXPw4vqfS4Dir0g_gNWsZuUOU-RtdtXvkZk6LmKapipXOxTk9jfnPwS3y3COKuWvqO3aOp5QgrYX7ISBvyzVVL5VDZ1oWl-XMGZGN0ZZF3RopmkYmS-Ime4nrJAxMXNqtCcWSrVIn7QQup43rOgyCgxpYfKNcEW8DUEU_hoFILUYcAuNZ3qHROAM94k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
👤
شکسته‌شدن‌صندلی کنعانی‌زادگان کاپیتان سرخ‌ها در حین مصاحبه با رسانه باشگاه پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27259" target="_blank">📅 14:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27258">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccbbedc5a9.mp4?token=aUgvkz2wcpnvrTFfuYyAcEZcoN5_fOcVC3EJknop0E6oAeEdsWXQU7HFRGIuVRLu8TQ3l41cg0sB61AegEtUaKycPV95hHTB5yC6k_Q-uNY_BpV3dktqVQbi1g1-PZJF9xRzLJCvie70aP5aUB_R8K6wld2BGji9pgpYRbXoK78ODXLHOnGxKRkowuy88JySAmyCJPoY-2YAYzW6ZmmdzBhv0rTWUPW9X6V38xES66dHR2cUkIrcmMo1u4kRYqVQrMEBORWVgqOJjnStPpkIuguviH-JTUPRycsWG0gyIh12_6Z_d-Q_1BxTjLDrDEgyoCK3bJlbOySrwu1H7B2r8h73ynZt9ioHFCkNceb87k0xd_lEoCvyd6EDrLAkNGwWbxR2OF7ngPg70XyGzzONeltFQTECNU_esPFHHVpEflxb50zuHfBu_IVyrRCZhWnFRM_L4yMLioI5WsXlcwko769eYsQpL8RT33yoticjT79YvZe8PsgIHEB3TNeivRIZsymLrCzl7AZxfz5HByJ84dL8mmpmsbt2yCGbjW-X9cjZDeorbv_KlSHeEQjo3Wh7cHzcElFA9-nauDl4A0oi1ubXdvhfd7Grmj085J-lknJrcI_U1l7LTtP2ivNwnqmIpHuNkUELGMERYykTPbnq7WovZOWzHWAp9NZB8DIcldI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccbbedc5a9.mp4?token=aUgvkz2wcpnvrTFfuYyAcEZcoN5_fOcVC3EJknop0E6oAeEdsWXQU7HFRGIuVRLu8TQ3l41cg0sB61AegEtUaKycPV95hHTB5yC6k_Q-uNY_BpV3dktqVQbi1g1-PZJF9xRzLJCvie70aP5aUB_R8K6wld2BGji9pgpYRbXoK78ODXLHOnGxKRkowuy88JySAmyCJPoY-2YAYzW6ZmmdzBhv0rTWUPW9X6V38xES66dHR2cUkIrcmMo1u4kRYqVQrMEBORWVgqOJjnStPpkIuguviH-JTUPRycsWG0gyIh12_6Z_d-Q_1BxTjLDrDEgyoCK3bJlbOySrwu1H7B2r8h73ynZt9ioHFCkNceb87k0xd_lEoCvyd6EDrLAkNGwWbxR2OF7ngPg70XyGzzONeltFQTECNU_esPFHHVpEflxb50zuHfBu_IVyrRCZhWnFRM_L4yMLioI5WsXlcwko769eYsQpL8RT33yoticjT79YvZe8PsgIHEB3TNeivRIZsymLrCzl7AZxfz5HByJ84dL8mmpmsbt2yCGbjW-X9cjZDeorbv_KlSHeEQjo3Wh7cHzcElFA9-nauDl4A0oi1ubXdvhfd7Grmj085J-lknJrcI_U1l7LTtP2ivNwnqmIpHuNkUELGMERYykTPbnq7WovZOWzHWAp9NZB8DIcldI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
موسی جنپو وینگر مالیایی استقلال که بلافاصله بعد جنگ اسفندماه قرار دادش رو با آبی‌ها فسخ کرد باعقد قراردادی به پانایتولیکوس یونان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27258" target="_blank">📅 13:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27257">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkCcuDLEg1Wa6bXQFksFVuFrjXbe9z32vSSg92sdFhY02YQe6h7kGQtzTHI6PCaVNFtilnNzgGNbwc7mtttAJR0GbCb8knau7O-kEUp84e9CDOS0Xzr1u7OG9n0Vo7CbzjmWd2SbWtQp4U99C7RTP3QBv4YWcufxjkrB2sgFvbJe_gd-VttGvxkFg9kYucbJrztI6s9TRp8KhKmpFZ6jTKv3KymtjyJdug3JaiJxb-A2kshVP3eTgCGedlv4IuQNjD0hKQydC1848Zvjh4-XwXhNCftET26kdQ7iKLHRQ83XLsKL8SO_IzuufwLdU_ri8TOjvl9bwJ-9-dkOIYK_wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد...بااعلام‌ایجنت‌موسی جنپو؛ این بازیکن قرار دادش رو با باشگاه استقلال فسخ کرد و رسما از جمع آبی‌پوشان‌پایتخت جدا شد. باشگاه بزودی 350 هزار دلار به حساب جنپو واریز خواهد کرد و پرونده این بازیکن مالیایی کامل بسته خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27257" target="_blank">📅 13:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27256">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5SVl0x58Ur442s08Cne85u5UHr5cieAOzB2zI1WSpBk_kLeEWKv8pF8MrmwMERUc6rqvHmCnoECnKp0JNHQzMMrLmJes_UzsLhRcrpjZIeNhyKVAKeF3sJ0zUr_7jePped2t87kdG9rScH9nzCiYeUaVBlj_9jolJUcSJREPR-reZkzleOTxQCDH2MlfvJNOW7QR4pHHqmS53uqE8m-QczHthYhV0hk8Vb-irPxdpKqbTsAPGAnTZv7qmOYUUt6O4RBtJ1uwRxA0CNMKKEnEGk_ETOF20ifMFIl9Bzz3WonV45jgFIbZQsQY_x7n6ik-Ru98xTOdqtQgdZvYvxhyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی پرسپولیس: از مدیریت باشگاه خواستم که سه بازیکن جدید جذب کنه تا تیم برای‌فصل‌جدیدتکمیل شود. درپست‌های دفاع میانی، دفاع چپ، هافبک تهاجمی بازیکن جدید میخواهیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/27256" target="_blank">📅 13:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27255">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cc9f95afa.mp4?token=Swz6-Oev1-mkCv8t7Gw-MLj3UsnhgeKlFA56C-fvOHAXJuVU6VwA2Sa91uLMJhvLN2KuC5cu6aKCkNTccptOP1BK2dLUKr9CnqFEviIfBXolXc1RE_JMMVFdaj_8lcbU_OhS0bohl5oCEnOjeDzMqYs86pgoFHdhGptLj7qTE92ay-5tUCRhvVxvOSRCMmVNtDUofW4pJ5OQVYEXvI5cmGcNkPvxH5oFApIf7ySwF0TbvuTCD1l2NDdOx6wlwggiRXD-cICYNhmjx8ZoJlbqZZN1O5YNGkBPE2XEY8Gfs6vB8ZK7VRSTu_UtQgaF0_fHdneIg11O28eSC1kGG5jGtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cc9f95afa.mp4?token=Swz6-Oev1-mkCv8t7Gw-MLj3UsnhgeKlFA56C-fvOHAXJuVU6VwA2Sa91uLMJhvLN2KuC5cu6aKCkNTccptOP1BK2dLUKr9CnqFEviIfBXolXc1RE_JMMVFdaj_8lcbU_OhS0bohl5oCEnOjeDzMqYs86pgoFHdhGptLj7qTE92ay-5tUCRhvVxvOSRCMmVNtDUofW4pJ5OQVYEXvI5cmGcNkPvxH5oFApIf7ySwF0TbvuTCD1l2NDdOx6wlwggiRXD-cICYNhmjx8ZoJlbqZZN1O5YNGkBPE2XEY8Gfs6vB8ZK7VRSTu_UtQgaF0_fHdneIg11O28eSC1kGG5jGtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
ویدیویی‌کوتاه‌وخاطره‌انگیزاز سوپرگل‌های دیدنی آنخل دیماریا فوق ستاره آرژانتینی سابق باشگاه های رئال مادرید، منچستریونایتد و پاری سن ژرمن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27255" target="_blank">📅 13:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27253">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7MF1wTA_-jE0ZuFITdRrHPqTw0JFjvCbK2h_2C50xy3n1SJvqrtOw-g-npXOEG5nKzg4-iN35fp0LKOMjRNq6Wkz_IJ_pFI4BmoxuZr0YxozvOg6g4tWSY1tw4Xr5Rnq1kRLe8k3QvVWAPs3F7O4FmOSHbvM3hbf8HsjmSUH59KBvr3mdktcV0Q_Jh4T-wfenJBuLBq54IvwZ1sXBDdPoxyc6XWZL_Bn_kaQIXVImyuxTVbxpZvDkX7JaAhgRbipdpzFmEGrKqU-f-ZBgRmNqBvIxPhoNI32vIDMy9sHqHYsY6sNhUIy_J9FR2lOOzCre2SsRuzeJtdjpZtlD-i0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
طبق شنیده‌های پرشیانا؛ بعد از استوری شب‌گذشته محمدجوادحسین‌نژاد؛ سعید سحر خیزان مهاجم‌جوان‌استقلال به‌اوگفته این همه صبر کردی یه نیم فصل دیگه هم صبرکن اگه پنجره باشگاه باز نشد. استوری دیشب حسین نژاد نشون داد که پرسپولیس آفرفرستاده اما اولویت اصلی این بازیکن…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/27253" target="_blank">📅 12:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27252">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLCjLzlhDo-MQyAiJvTFKNjaUh1YeDdk5H_2CbMY-T7xM5MXwrKG2V2tl2oYgz-eBDzF2eOD8Rk1QC9R7iWUPOsFMmhN1SHKV6ESNhpcDukqeEFXmlQFXj4TdALcFXCujFV95vngAc5fTHfounyPj6KHxG5axbGG_dVQ-OP41oILzS4KB-wRjzeluSWMKTzQMYJmzgm0t22KVBPO-5LRtG_nB17rGw3EnSAp3-DQVOudI1Dcj9w7Aan8o-klvvrGUJrV_7cMYU8URQmsDtoLIr370JNlHugyX8sknqjW1p2uh749_boAqgueuDeugxjnZs6XFBVCjaUxevs6pTb2tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
#تکمیلی؛مدت‌قرارداد محمد صلاح با ترابزون دوساله هست و هفته‌ای 325 هزار یورو دستمزدشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27252" target="_blank">📅 12:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27251">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ce1lx8VFXPxh8FuujTr3L7CibUD3hbzjsU4C3VNtThTuaRqz7j1nv4MfbCi3F4Cle9xgEA84lEWUbqTqdxEriWdKHWmvmjGvL7taSCXbXVuJ0tTc0_KxYy3Nx7tUG3CHmlpgSCTRskFvLvOLkZIZHI6gZ50IHvFP0otgAq5Cp8yjcraVxBsOdmSg_RdoN6ufR4QpEfadWseWANK33jKN5dzxalBPdZU3jRmxWm0ZGKQqhfnztKMONywG5uv_T_Pq2By-1RCHAXdyQdJtVFg01UqCro7FcV3o0GjPZhGjjt4cJpOdmWIRFjoo0RErE72m05NYp4lMOs297pE_8RBgyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ به‌ احتمال‌زیاد و اگه اوضاع کشور ملتهب نشه خواکین گیل اسپانیایی به عنوان دستیار سهراب بختیاری‌زاده دراستقلال انتخاب خواهد شد.
❌
مربی‌اسپانیایی آشنایی کامل به فضای فوتبال ما دارد و در کارنامه او همکاری با تیم‌هایی مثل الوصل، بنی یاس، بتیس، پرسپولیس،…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27251" target="_blank">📅 12:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27250">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">📹
دانشجویان فارغ التحصیل دانشگاه الزهرا تهران هم روز گذشته این ویدیو ساختند و منتشر کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27250" target="_blank">📅 11:46 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27249">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YD0IeEZ65STumyuySdcquXvnK390Wu-lCUCnvtZdna7Je0Ln7-h10LYKknM78oMfkAMHmG_q9nTbcKNuCg8ZUMdQQbY4a3ZmAylC0Ku_tl7kb8GJ9S0-3UrSNwav5QEmbq_lTAaiDt-xGEVmEe-lqsj97NhYHCN-8NsLvwmH7SeRiBZColdE1q_vqr9E4B2_eoYDcLcAFP2ERtgAR6aSgAwvD_U94Tm4buwtg4PsabSMFK_XSH9V6NQoIrMDeQRDt3SUf09o4dq4Bm0ob-nvruFzZXopUqBwyaawbOXDGEL1gH5DWV0gKTMGkc9NROzDBDo8r3t1NlTAvq7O-1vaog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/27249" target="_blank">📅 11:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27248">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mINXr1NTs_U5jj0bs26O2lb00wli7g-2x_B5KN4svoq_JaewUkuBSHL3cmfHCGXhf5X_4Os3HuHOQrObzIGv2ftOdsWAK0dgnNCYVAYej5CPWDUYVfh0eo0yKPF2eRxS6mtM1glTujkUy90rm9l9Wab0QVUzfTme2GsQcNAVy7Z3tdiYlXQoAAQ7THm_gWKhZxrWaIxCQUTrL_ycsdlTRbOxe0WhXfDw7K5Qbp46Z7B8ZbElZ3TRts-3A9wuS8MV3OV7hqAE6UDK8RLj3LFVckXhI3l50prZR14bPN7o0RNPSDiuIpiCe1ZDOdTOO-lFrW6Nm3HgZKpA64EMe9pBQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ بزودی فابریزیو رومانو خبر پیوستن قطعی رودری به‌بارسلونا رومنتشر خواهد کرد. تمام توافقات شخصی صورت گرفته و توافقات بین دو باشگاه نیز در مراحل پایانی خود قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27248" target="_blank">📅 11:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27247">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfOLwFhDuQZWrt8BdFd48CpXyG0yapNHVVhxK0Hke_dx0Gn6anKeEVgCcFX1RqscnbaqrrG_VUiT5zrisUfcpMWjjH9GYSu35SUY2Gmltthg8JKaEeUTUvSnsN6_ptuiFe33jeYnB-Yf30RMD8oWenuuMyAlPKw7dAqur9Oxo2VKZVCBdLqK3IUKBECIXBj-qn5Vgkw6CVa5fC7JXrxsko-8JM9cLlX6AJey7flZjWH6a0I8NBaN9Fzs3wRkPbAYAsuGJzvGy6h5aTD3f0ocUCwtKwl35er9ZsvUAW9sGrM_nNCe2Ilybfaf1xQkscOhBeVn47p797rpmCPNyywq4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبرتو مانچینی سرمربی تیم ملی ایتالیا:
🔵
ماجرای‌من و تیم‌ملی‌فوتبال ایتالیا مثل داستان یه‌رابطه عاشقانه است که به خاطر اشتباهات تموم میشه. متاسفم به خاطر اتفاقاتی که در این سه سال رخ داد و تمام تلاشم رو خواهم کرد واسه بازگشت تیم ملی ایتالیا به جایگاهی که شایسته…</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27247" target="_blank">📅 11:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27246">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ae5Wn1I6cq7tMF1AlM2iBFyMbt5hfELBwd3g5dX05Vc0IFhczQYMHKq9wcuQWyrfUHiibJLgT9xGQmBnyo0tcoBn1yBIkMqikSEY5xGvhM6ctF2a1_sbDezxjZIs8QEEaX2GbzIZPDTk0ygvdyK4xspXyzENrwOm_manxfZ4dQE8gPEoGmvBtdKwbKINwunuE3iSLCwUpG3GByluIajHpd_NTaE-JAU8QbPRwLwIOkq_0ajEJEKSHL1bMqzIDldvFiYdGQtW3yDCCqn7OY2H2nnK2dMfHMN13J-N5WFaLTozGB5887NrmZffohGQpNa7rk6AfJ5n8EU_-eOJJBUJeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه کوپه: انتقال رودی به بارسلونا نهایی شده. او دستمزد بسیار بالایی در بارسا دریافت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/27246" target="_blank">📅 01:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27245">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvyYocTWLliSyj17PC-TxG2a4L9NImm_EZUDAIpQURJF69OSsZ7QSDiLjBkGo-8f9qshYqRHfuPYTH-JajzQkSYJQO6pqnFppzZL5DqlTWrzSSOua_eMzsHn8WfjR_OQh8WsIeO0j5_gGf0AATfjzeogWej1CiowoKV-1DFsv8EO77FzSvsgarNQ34_MhaC2_y9y3uwaFE6mu3Tzoo-BLqlVQ2F6FsMxJMTCTbCKhoj0gV4FUMUqODRXAKwoZRBvCfkoK4rmyMbuvybVBCnUhV8FMmJcWWVgrp22SsHjjjOLpBiVbObSgYL9_tr54osRpWi8otV5OoQMpTEvZEEY7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
🇨🇮
نشریه‌مارکا:باجذب‌یان‌دیومانده و تمدید قرار داد وینیسیوس جونیور رئال مادرید به احتمال فراوان دیگر خریدی در این پنجره نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27245" target="_blank">📅 01:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27244">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1a50e09f5.mp4?token=JgkQzzXBj2NcRqPhNnMBpIq-Ib6oDR5khmVQ9zwCKNEV45py0lgAdC1eXAQ0rd_G2ryjkmp7PlVWfUED_qwIS1ZbVFt7xmaRJToZx_vqdPtlV1w2RdXBHw30ZITpIV7-cst-IGHcQ3-YYsjXVm4vKYM0eTInIvS5U8cLyfbkIUjWINiWbqc_9PETjsvlD1EEp2q6i1CrYmQcunvFxJWreuuY46tMPuGLS-u7P-UiA-RfYSJFi9TGjpofQWfYebx_yK2F2ZAra2xSNLc__KJUAAhyQXhDdwfRBhJ5C_qujd3igfpvYv3Efw5DgaBLe7092wIr9l3T4tCKUDiVItzgcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1a50e09f5.mp4?token=JgkQzzXBj2NcRqPhNnMBpIq-Ib6oDR5khmVQ9zwCKNEV45py0lgAdC1eXAQ0rd_G2ryjkmp7PlVWfUED_qwIS1ZbVFt7xmaRJToZx_vqdPtlV1w2RdXBHw30ZITpIV7-cst-IGHcQ3-YYsjXVm4vKYM0eTInIvS5U8cLyfbkIUjWINiWbqc_9PETjsvlD1EEp2q6i1CrYmQcunvFxJWreuuY46tMPuGLS-u7P-UiA-RfYSJFi9TGjpofQWfYebx_yK2F2ZAra2xSNLc__KJUAAhyQXhDdwfRBhJ5C_qujd3igfpvYv3Efw5DgaBLe7092wIr9l3T4tCKUDiVItzgcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌فراری‌قرمزی‌که‌پشتCR7 می‌بینید، یه فراری معمولی نیست. حتی اگه پولش رو هم داشته باشید، لزوماً نمیتونیدبخریدش. این‌مدل بصورت اختصاصی توسط فراری برای مشتری‌های‌خاص و خوش‌حسابش تولید شده و تعداد خیلی محدودی ازش وجود داره. حالا اینا به کنار، نکته جالب ماجرا…</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27244" target="_blank">📅 01:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27243">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABucf7ka_JOLhen7VcXd9EFi4xYipabIUsrdPRRcTVgCdKW9qoNMv-dzUujESgcHNwCHcGyhkpl9qDICi3zpe1hNGnvZTsApEIXxFoiCPAJhlE6QqHANN8OaJQbghS6DYge5U_xu5fw6dbRkoP__YIcbhWzMQ41HRryxl8EsDP79mAyxr66uhoM7tMA_Ajewwrpd2xjp8NIElw40Eews70Wu4JV13dOEPTniWmFcEWuFPZzRhL_4apTqaxW8oO8qLsGXAdr4ryRNqF1_6bpS4e9LnGNqAf-xpq_d-gm454ynWTt4N3_VnIb7uYZjZOObzl5wchtFefF5XKtvhlf2cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ بزودی فابریزیو رومانو خبر پیوستن قطعی رودری به‌بارسلونا رومنتشر خواهد کرد. تمام توافقات شخصی صورت گرفته و توافقات بین دو باشگاه نیز در مراحل پایانی خود قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27243" target="_blank">📅 01:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27240">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aU4DonF3YOJFezMFowYD6ef_e2KE6UqQxAS3mRrSk4KvXwUtT4y8hupZG1P2XEf7C0sEV_1IugpGZxumO58DkoJapZRdfIS_L6vdJyz3GVhyngjamAkpII9i055xeTDrc5w1LBjoExhiXhgy8FHBpGp-gs6Nj-I8knsWz9JqaFEep1olqu2fY3FTz1ugrP3ME1EFS-1zs2IIpET0Y3ZF2WmKVNugH58Ih2wuXZ08QnO5A6l16L__qMzszczJ0RhAt4dkbymdKmEDqhwdYeVets56nIKiDDEVng2VwadQtyaZiTmFkgfYKAiuGJismWhlKNri_st_pAcX56d5uilcXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه تنها مسابقه مهم ‌‌‌امروز؛
دوئل دوستانه و جذاب شاگردان اونای‌ امری و کمپانی در هنگ‌ کنگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27240" target="_blank">📅 00:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27239">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtyzHcf7xy5KgbVZimNfmbfeeKsiQhlnW84nnV5gdhQC7zhpoBDbPterukFllapAZdU9VGt64d6-EcYFN-2_S4ajfvGWCdYVmIYqfw0BOLZnX51fYZMbxHDRr3PtIkA1gzY7LBsLmFfh00FiK-4UAXa_fHixqEWDs6xaLxK33amkQV9vGrQwU1TEvsiteTfOHwE6z_dy9BPtqi2jv1us2o9Bq4cHzw1z1fcAZryr00twN-f_XpoAjzOLf9JiXKeLk7O8QvLn2oLdEja_tBIMUPn9_UhNpjlQ0EoE0RVN0Uzw94Olf9uxE9nJHT-UwREd034E5ladBydRzwfl8cXIQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای‌ دیروز؛
برد اینترمیامی با نمایش درخشان لیونل مسی و ثبت دو گل و یک پاس‌گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27239" target="_blank">📅 00:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27238">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBST-c2xH9OjKhmYQKaM9FZN78gNRO_mW4kN-Is5Ih9t5F5KYo6Fu0XCTgf-ssyKRctzK6SlSFGa9JJa1YWCm1R55yFnQG7Z26dORCEMzjoUxUHwPtw_mmX9KadSQpUnuzpspUdsu29VS5d5C7v07kp00fmekPvl1JsX6VlTn65Hv4YzR01MX9LC-DuM5eYaeZdE3pTRFlE_6QFen3Ru1E89eQgDj0KbSj9w799WBRE0u96QYccjM6vGCPkvQ0uYfo0S0vdDUFR0rrEhdEHaHYniOCGC5_Mx9isQS6oPkBwpsQpZSmMVZKnPNXXWu4rWM_VPiivOBwZlZ87OrZ2LDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بریز بپاش‌های چلسی طبق معمول ادامه داره؛ بعداز جذب مورگان راجرز بارقم 137 میلیون یورو؛ حالا سران چلسی باپرداخت 60 میلیون‌یورو با عقد قراردادی‌تاسال2032 ماکسنس لاکروا مدافع میانی 26ساله باشگاه کریستال پالاس رو خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27238" target="_blank">📅 00:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27237">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uk0KbAQdv9osKhHRoxdS10g5eTZsX80MI5zEKSIbHaYocRoCKiRLEpkJGvQQ7xn98959b1vYIISWOqjqLkqsGVeOpkdwjp-e1SawS4Up_NnvfSkIaqxrfx5vDyHZ-Z53O6xEB1WqClFleyxIjJE-2gz69aV_uqc1UbYN5clUfy7AvQ2IUSMsZbw1jv04q92ktfr1gQP24gs-JoLjiOGYEjivLIPHMudnsHas030uU_iARUwCq7cOrTWmiP0xIg1hMHyyad_aNJyU_7_Ctvo2xOCo3F3-JCSe4qFzyaK_0iokorlx4M0f-DzIEA2a6tv3kEzBrJCGHdbuO9p2-kPCAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
وینیسیوس جونیور بعداز تمدید قراردادش: هشت‌سال‌حضور درسانتیاگوبرنابئو برای من کم بود و دوست داشتم شش سال دیگر در برنابئو بمونم. شاید اگر شرایط همینجوری فراهم‌باشد تاابد اینجا بمونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27237" target="_blank">📅 00:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27236">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XH_jEdEqUiHUuYarrZdgMSdVI0I8DLBP6Mw1KNnTUAIpptvH6dLYR8VuSTrDeyI3Nw-tj0Srndsw6kUTBYdrDbTFoQ3MjLs6w_asbnLOAy4KEnztfCnglvednjY1fxPX75BL5UZgcZTUlhTaYe-o1CIPvLhqMLqzaOeX88afsgqUmK_OstWDdSgu3SoIjHPkQjhiE0O6kGvO_qqCwB-5JTHUFbxcjnY9NJmQch_KWPpl6cnb_viDWY52s9bdw3txn3CNbePT9k7DV2IzmZzHZmp0vB9Nx0kzoK0CkdjC59sGJokSr3PA8ZYMntKzt_ipbtyVcBkVaeCE4gjBr1NwtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
متئو مورتو: رودری ستاره لاروخا از صبر کردن برای اینکه‌رئال‌مادریدبامنچسترسیتی به توافق برسد خسته شده بود. بارسا به او تضمین داده که مذاکرات مستقیم با سیتی را آغاز خواهد کرد. هانسی فلیک با رودری تماس گرفته و این بازیکن به او قول داده که قید حضور در رئال رو…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27236" target="_blank">📅 00:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27235">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPW81R8f3cgwj_7pJaAwMxZasr1Zh5tehZjQOuUPBL7RhtF1ETTUH7GfWOb0buKhCfUm3KOO04YehS6Bj2fMH8K7XhukrfgnXDdnxX4VPp6HsIzChWUWRplratCX9HDqwABL2-vbcpzl3XfrQMbQ8gDSgjvPZfKJWgkE7752R7Y-gmDgTNtI5nnZKoMzznV9t0yuCkmrQbSkODxCtSoI_imlXy09mjtm7KY83goFVM1pfjWBOv1647r_4aLmtTU8cLTK_8bfDF61L8trxhwTQsXQfa8ih83ehcWgLWD3gVNX3Z1Ybadnrl6BQq6dRBQdFVnNGVHOcVYi54SXnNMyYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
وینیسیوس جونیور بعداز تمدید قراردادش: هشت‌سال‌حضور درسانتیاگوبرنابئو برای من کم بود و دوست داشتم شش سال دیگر در برنابئو بمونم. شاید اگر شرایط همینجوری فراهم‌باشد تاابد اینجا بمونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27235" target="_blank">📅 23:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27234">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jE49erFzcPGiwdwW0N1rQpqx3m25-tPjJY277kDctmhNvNxfc6UJa4Ri6a2Ihjm5nMndABoaOh4fym5-b2zi5uA9jALqHL5PYVrCi9Qk9TLFU6HURpD-P0Cr5ibDi_2ECd8hSmgAas0Pi93Obe5oA55cF1afugJQ3o3447vzg81y82A9kEXx97C0n_e0HeAS1Z7KH5ZhuJsqqopzIeM5zbX6kqJBSS5L3B8TrSIgJteC97PleapdB0GSudG3PR0BC_ZC-GtCv5e4ciZae6kA9SLY_Y2h7TKIDhrrb5qHcWA5KMSOZHTHIvd3pPyg33yxEG_XLSZMA4sBf1qU1r4v1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛کادناسر:پرونده‌پیوستن رودری به رئال مادرید بسته شد و این انتقال انجام نخواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27234" target="_blank">📅 23:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27233">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e40f288f69.mp4?token=o4jLHFs0V0qDZ7QAjdErxYmHtNXtahaxbtGkBtW8DFrcwRcl3XjLQ3BmO_XjkoTNVEfh28WSvLlExLZU6Gv4_kGM8Hf6gWwM_l8a8GnszfosxVtoijeaJik_2GL5SpA1O5YWqOUzquzOLyIBmFEflwn7LsZUtT8ClxAmOhpfrt6w87r__XESC37Q3u7m_sOd4Febj9UGD-TqmETEun1ycFsaKsClnTsfVGAZtd82pxo_DBis2Z2F_OCLBxECuiP508aoqNNy5wdRK5LI3SV6alf5GrVA19ncCnxrOi3pzzdvqm1KBO2WgaIogWB0cws38AR8ZUbdKJB49HWl9wgU6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e40f288f69.mp4?token=o4jLHFs0V0qDZ7QAjdErxYmHtNXtahaxbtGkBtW8DFrcwRcl3XjLQ3BmO_XjkoTNVEfh28WSvLlExLZU6Gv4_kGM8Hf6gWwM_l8a8GnszfosxVtoijeaJik_2GL5SpA1O5YWqOUzquzOLyIBmFEflwn7LsZUtT8ClxAmOhpfrt6w87r__XESC37Q3u7m_sOd4Febj9UGD-TqmETEun1ycFsaKsClnTsfVGAZtd82pxo_DBis2Z2F_OCLBxECuiP508aoqNNy5wdRK5LI3SV6alf5GrVA19ncCnxrOi3pzzdvqm1KBO2WgaIogWB0cws38AR8ZUbdKJB49HWl9wgU6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
میلادمحمدی‌که‌ازابتدا در ترکیب ویتبسک حضور داشت با دریافت دو کارت زرد در دقایق 21 و 33 از زمین مسابقه اخراج شد تاویتسبک که 1-0 نیز عقب بود، ده نفره کار سختی برای ادامه بازی داشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27233" target="_blank">📅 23:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27232">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700f42e1af.mp4?token=veGAx0uvmGdiyfMgruaEHvxnUeijwnDt-eiMkArhQscKGE-5SxkXMwhsLmOBxvUUHzP7UsP8me6e0d7c3O-oDmG9mjlGJ5tK0Mn8fHoU7BIh-jqbWJEx_qDYGW9b0YmnCnLuIlt0CYAojgdZVGoNPeeIFBG0vJyJAD3RR8vXEMOMKTjg8SyhgHOpne6WcFrNEEYquRI3OTMa3nzTkgUg0Xj7PYYukMdSD_0fAgBCmJHM4opSz0PDr-_ZLk_7ubsGcTbQ-WbKo8DKFfloCnz9bjIPQUtYP7vtGo0yYlGPAdkpv4gKkrtAWjmnjtx1VJ4h4EfhUI68EWbZKt5GO7MI1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700f42e1af.mp4?token=veGAx0uvmGdiyfMgruaEHvxnUeijwnDt-eiMkArhQscKGE-5SxkXMwhsLmOBxvUUHzP7UsP8me6e0d7c3O-oDmG9mjlGJ5tK0Mn8fHoU7BIh-jqbWJEx_qDYGW9b0YmnCnLuIlt0CYAojgdZVGoNPeeIFBG0vJyJAD3RR8vXEMOMKTjg8SyhgHOpne6WcFrNEEYquRI3OTMa3nzTkgUg0Xj7PYYukMdSD_0fAgBCmJHM4opSz0PDr-_ZLk_7ubsGcTbQ-WbKo8DKFfloCnz9bjIPQUtYP7vtGo0yYlGPAdkpv4gKkrtAWjmnjtx1VJ4h4EfhUI68EWbZKt5GO7MI1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زلاتان ابراهیموویچ اسطوره‌میلان در مصاحبه‌ای جدید از دوران مدرسه گفت؛ زمانی که یکی از معلم‌ هایش آینده‌ ای برای او متصور نبود و تصور می‌کرد این شاگرد پرجنب‌وجوش به‌جایی نمیرسد. اما زلاتان مسیر خودش را ساخت، در بزرگ‌ترین تیم‌های ایتالیا درخشید و ثابت کرد بهترین جواب به ناامیدکننده‌ها، تبدیل‌کردن همان رؤیای دور به واقعیت است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27232" target="_blank">📅 23:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27231">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-rCj1x0KYVqchIezYyw9Tdg3OyQ2qGnQOKcYU9tdvTP6pGuq0wv-xK4UVYFCn16MDr0nyHFAl1CYzYUVUWPZNsXzUHt5EvfxdUrauJOgOsLwAkgnmRj2w43osHWTuklhbVjDv8IAZPPoHmx_MeIxrfi6O9GiiKzq6CJ82Ijj5JIARz6R9ssSRvS7xvyBHxa9FGsePZF2rr2vdXqwyOckshgCc0_aiPom46G9pEOgFJfHyKNLsxpbcfa3vid05_eTNsZ-mFMqr7-vDHAEshTKJT9klCpegQFujVd45_grRQhKmyBbb7dagt2f2-6_c4_Msi3maGRHQgKr5kJLHUY0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلطان‌میلادمحمدی‌متخصص‌اوت‌های نامنظم تو یکی‌ازمهم‌ترین بازیهای تیمش تو پلی آف اروپایی تو ۱۲ دقیقه دو کارت زرد گرفت و تیمشو بگا داد:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27231" target="_blank">📅 22:59 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27230">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902ccfdccd.mp4?token=sohxooMDNfXfqdsNjnh3gUqfwW_IFo5PBOdNplL4HgiivSrH48HQlGswJ-w8XfbvP06EtaR1B3pg95tbj4xFrQwyiJgc_VbqjpqXEwtEZ_cUrevySTN7kV4rYYt-RhCpIlWMIBOi6BljipaTsr-4rkwrbVe6ITKr0BD7T3bimB32QEel9ilGGxtiKS3nELV88v29q-MzM4_5ltIl5TYPSf7Xv4OQZMfZgXOkOnPX_fh7UYVv4tDHmhuQQeuHH-5D6wYUDr5p3OOCl0BgQIfVpjVn-PVkVRxOPu9Vvibbuo87RoDtAHJ4twiRmoi-SpxH-wp9jgWvmoEKXYWIHlRTXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902ccfdccd.mp4?token=sohxooMDNfXfqdsNjnh3gUqfwW_IFo5PBOdNplL4HgiivSrH48HQlGswJ-w8XfbvP06EtaR1B3pg95tbj4xFrQwyiJgc_VbqjpqXEwtEZ_cUrevySTN7kV4rYYt-RhCpIlWMIBOi6BljipaTsr-4rkwrbVe6ITKr0BD7T3bimB32QEel9ilGGxtiKS3nELV88v29q-MzM4_5ltIl5TYPSf7Xv4OQZMfZgXOkOnPX_fh7UYVv4tDHmhuQQeuHH-5D6wYUDr5p3OOCl0BgQIfVpjVn-PVkVRxOPu9Vvibbuo87RoDtAHJ4twiRmoi-SpxH-wp9jgWvmoEKXYWIHlRTXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇪🇬
دوویدیو برگ‌ریزون‌از استقبال هواداران تزابزون اسپور از محمد صلاح به محض رسیدن به ترکیه و رونمایی باپیراهن شماره 10 ترابزون
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27230" target="_blank">📅 22:43 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27229">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avTB0GQqyBV9aPsVDTlacIwBQVQNWKg5cIpQHIb9somqRJFVxZqK1cFOpXMxr629DVTJf9mta5cf7_IN3VcTGdcQrhREOVrdiKzLXtUgu0XhVcM_escsyqFb8yKQcSKqu5mFxhQFKN3X0shAFzocE815911pYmcjuVIsvNoF_kYDlSpJBWsa0BPvvhU-6VIJkaM4ua_UEheaIW140rfi_QR96lRaL-HNsYdG9tOUkpygktDw4SOc9S_-DJUb02d_GGqiU3LX0S8eUPEf9L-KSL71SUNVZEEpEApe8m3ykkoBVXDVzaDNWLlaUf73Yk3egtbeIXIf2MCet4RMoVAqbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
رونمایی رسمی رسانه باشگاه رئال مادرید از وینیسیوس جونیور؛ وینی به سبک یه گلر ایرانی دو هفته رئالی‌هارو بااخبار رفتنش به آرسنال اذیت کرد اما بالاخره قراردادش رو شش ساله تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27229" target="_blank">📅 22:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27228">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86333d6363.mp4?token=ZNj64KZdljXAmMs1xPmSuJpm0BxiQ6KH4R4qxPdnQ9PjjIpHc8nGCEquzkvoZaYq9a1sVm1po4WuyzaFd5GDyvLI8A7PLIb2D8i6AlsgjCn26a1jNvB8zgPPNbyk8Ljs55Xs8TEebx8lIXZa2t2nyxLL7H0BVR0WHENGASHIueIA9G5iZ-jZf0uRR5Z7VxTvYE7SKSb6VsxyRGPS475LMP4xDz7B6VQGb6KzjqJIxliYAued4x3S8FMIPJax3eL45bWNTWPJpiwGTeG0xi8AXjjZhCAyZBu5fiHR1ZW3tP_Kh3l1lnaH6kHt-7Dl6peZz3m4dOsW2euuLNhKysomiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86333d6363.mp4?token=ZNj64KZdljXAmMs1xPmSuJpm0BxiQ6KH4R4qxPdnQ9PjjIpHc8nGCEquzkvoZaYq9a1sVm1po4WuyzaFd5GDyvLI8A7PLIb2D8i6AlsgjCn26a1jNvB8zgPPNbyk8Ljs55Xs8TEebx8lIXZa2t2nyxLL7H0BVR0WHENGASHIueIA9G5iZ-jZf0uRR5Z7VxTvYE7SKSb6VsxyRGPS475LMP4xDz7B6VQGb6KzjqJIxliYAued4x3S8FMIPJax3eL45bWNTWPJpiwGTeG0xi8AXjjZhCAyZBu5fiHR1ZW3tP_Kh3l1lnaH6kHt-7Dl6peZz3m4dOsW2euuLNhKysomiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇳🇴
دو گل استثنایی و مشابه هم از ارلینگ هالند غول نروژی تیم‌منچسترسیتی درلیگ قهرمانان اروپا؛ باباش گفته‌شاید درآینده‌نچندان دور این فوق ستاره نروژی رو با پیراهن باشگاه رئال مادرید ببینیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27228" target="_blank">📅 21:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27227">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🟡
👤
وقتیCR7 از اسباب‌بازی‌هاش رونمایی کرد؛ كريستيانو رونالدو با انتشار پستی در اینستاگرام از ماشین های لوکسش نوشت؛ اسباب بازی های من.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27227" target="_blank">📅 21:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27226">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0Bmq0zRO3Pz5Au4oBGHY9RonUuup04sx8cPgDfNXyusz-jAXghiPHnf2yVtQ35KbS1-FnEQwqVrmkGQCvPvY5S-FykpVgrJnpT3jj0TZnYpuzErxT8atTAQmFvTB5PaxXd4sg0DR89eankkWAIj02bQziFFJQEXXQEb5lZ6nmO3hPbCj6WJgH49ljpzioF_UKlIU0asG7aJIeXSAlF-t5blfTA_VHC2KozKgTSFPjP3tReSycYxdfCLUY791wH5_DkCOZkCLFHHtL6U_MQEuTyaUNkkGDVYM3WZCZuNV84-MptL2nbCKTW_mQjPnkZfPDKrnSicb83Guj57Ot9TRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
رومانو تایید کرد؛ بالاخره بعد از کش‌و‌قوس‌ های زیاد؛ قرارداد وینیسیوس جونیور با باشگاه رئال مادرید به مدت 6 فصل و تا سال 2032 تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27226" target="_blank">📅 21:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27225">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8-htmKUeUO2JcRiX5PlYBOfIiqn_krEbRShwMh2_4xYUlOmoCWkN_Lz7JQUh7nZNPRoPWOwemRqf9FqYJEVJlzItZyif1xz6zHvJm18FFsuaV68bZSxZH_6Lvo56SOQIDO3gBfzDE9j2AleEUWOs9-cQI1maliRqnYORgcvJs7OUQtpC331HngseSdAbcPtWynlj7uR9E7lVELwxAaTIEW893Uwug8aZB6QbCz5JiXPpq-QRw-jadFXCpdhbx0xzkAT5PMIHo7e8qlUWd4A003NP_BcwwQeEI6opl-sr5xo4Z9JDj6L8-mr7Zi36BOz-aQBhAqv6hKr5rAxxnymQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هونگ‌میونگ‌بو سرمربی‌کره‌جنوبی درجام جهانی ۲۰۲۶ مجبور شد دربرابرمجلس ملی کره حاضر شود! او توسط نمایندگان مجلس کره جنوبی درباره تک‌تک تصمیمات تاکتیکی‌ اش بازخواست شد. از تعویض‌‌ها و دعوت بازیکنان گرفته تا ترکیب اصلی تیم و سایر تصمیمات فنی اش، همه‌چیز زیر…</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27225" target="_blank">📅 21:21 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27224">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clL3hzUYiryO4fU4pu39pE6TE_uopPftgjK816RJ_a2NgYPMM8_g9ndMPMp5wEOVoVsXZCnO5G4Gn73HLINBQ8ynf2OLwro2tO7-vYqqFl-KQtGMFnYau-2gbcNA-4ujUVUEDo4-Eu3305_Jb45b0thHzl7fH8Cu4_uzOKkLMYbHmb_kXnTR-dPdnpPJbrZGMuA02bzcOacCSPouXwT279lzOmEPvP3hA8CYP86bMpkqeSq6zjV_GvDJ-BrB0sP0NSDDAbWiDrCi8nRBs3WYyd1MeW7K61qpbdlKHyMrj_QUJ9wh-vkO8jGFzRLL7dtTMVQphBbN7aP4nWjfnqSYMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
تیم استقلال امروز دردیداری دوستانه با دبل سعید سحر خیزان و گلزنی یاسر آسانی تیم استقلال خوزستان رو شکست داد. حردانی دو پاس گل داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27224" target="_blank">📅 20:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27223">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r188gycIaO_Mk-Vrh4T154qosT56XI7pjfgCWTpaKMXLJcSioWh80aCmGn7aG8Gx7w8IjdAsMdS76OmACR5B8dE7jbH2edU_fJqc049_bgZwcDFP3Ne5DhUm99UE1OlB-X3G6M2haNUblu3uXEi_eh8RZBvgNgK4T9nLyJhicrXebEmqZFX1fhq7Hv9FAoOFInKjYL34LQ-wLqWmht6NXbOvKCZ-67ZALxKaIUCiew61FNF0Ag4LxqxLFf_eTdZX5EReRNmnmQp1iqvpmuS83D-STPLA3zA9_E0Hnrj2BC7M-OP02LL-wExFjVKUKpuK82pnbrrXwwp8e6mfivTYcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇧🇷
#فوری؛وینیسیوس جونیور ستاره برزیلی رئال مادرید دقایقی قبل قرارداد خود را به مدت شش فصل‌دیگر باکهکشانی‌ها تمدید کرد. باشگاه بزودی خبر تمدید قرارداد وینیسیوس رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27223" target="_blank">📅 20:51 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27222">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/883695a5fe.mp4?token=d65gl9lr9pVuiv9OSk4FbqUFiIClq-zWmic2eTQux7-SAzBUa5539Foreas90QQpJIKjogkfBcJkH3RHHRVLHsLI67MYlSZ6rlG-rT_5opBwD2dmGwiVsOcwdLCGkIZhDpJiJZ1lMqYISQCuFw7lTUPjn8gTHJl5ZOOkOCYJyYUqPaSBAHrg8wvWAXKnp_qL2CpBVcO15LEIRQom9JHoZuiSUneoIIEE4UkrLYhcvtq90U4u25C83GXhG4z7MEI2VKi7Ven1qu_QQ1Wn7qvy_wabbh27rpdnYGP29stZaFOv4MJID1id04f4umq-jKzQiCHnu0PE8To85AxyUIG50A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/883695a5fe.mp4?token=d65gl9lr9pVuiv9OSk4FbqUFiIClq-zWmic2eTQux7-SAzBUa5539Foreas90QQpJIKjogkfBcJkH3RHHRVLHsLI67MYlSZ6rlG-rT_5opBwD2dmGwiVsOcwdLCGkIZhDpJiJZ1lMqYISQCuFw7lTUPjn8gTHJl5ZOOkOCYJyYUqPaSBAHrg8wvWAXKnp_qL2CpBVcO15LEIRQom9JHoZuiSUneoIIEE4UkrLYhcvtq90U4u25C83GXhG4z7MEI2VKi7Ven1qu_QQ1Wn7qvy_wabbh27rpdnYGP29stZaFOv4MJID1id04f4umq-jKzQiCHnu0PE8To85AxyUIG50A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه‌ای‌جالب در بازی دوستانه اخیر دو تیم رن فرانسه
🆚
گالاتاسرای که‌موقعیت استثتایی داگلاس سارا ستاره گالاتاسرای به طرز عجیبی به گل تبدیل نشد. این‌صحنه سوژه تموم رسانه‌های خارجی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27222" target="_blank">📅 20:36 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27221">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hf_1cTwyQpC11F7oLD8adFVK3fczoZ2nboJNjtfM_OUEtqRC8DGjtQCV4k6vWJkACEqFq1EB9AabopTDUWf5dLm3ggTB-E8D0ng02ydA-2kGCC7LGxe8htFt4yDIaY4YKzRKQeJYto3jCJXL-jh8eB2pFnfoYlVK6NvlWWfIrCxEbmWJFDUMWD20oNChH9KHwch9U6qnUTT7zgXiNWxLpPsoV629vl9Lsicvu2osalK1A4hPtS6OcKHeutFd7C6J0IEadxLbaFe2a0X_iO2-pFteE-XaNHd_hpyq6QrHWRAubQ5sa8zaK4Kw11y8Pc-llTkXxQmCNPBRswZf4vAziA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌فراری‌قرمزی‌که‌پشتCR7 می‌بینید، یه فراری معمولی نیست. حتی اگه پولش رو هم داشته باشید، لزوماً نمیتونیدبخریدش. این‌مدل بصورت اختصاصی توسط فراری برای مشتری‌های‌خاص و خوش‌حسابش تولید شده و تعداد خیلی محدودی ازش وجود داره. حالا اینا به کنار، نکته جالب ماجرا…</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27221" target="_blank">📅 20:24 · 15 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
