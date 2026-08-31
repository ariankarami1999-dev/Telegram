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
<img src="https://cdn4.telesco.pe/file/Cum2mwPgF9KxX5VDzk6YfkI2Alko0A0-SwsUJgLx2E6OSplcX2U3lc4rGHNBiYU0Sfje0Ol8C_Vjm2TM-rHX7q9xuI_ANC1AY4jamcjmj3pm84VNicdkAZZSZ2D9DJFRC6nctZyr80BnRCKIM8fHGXEpmdFUkuxYesG9G5YAMOFiuWaOBIrNDCzFhPSSc2c5-v5JB84kG7gMgi11bfbOVFvS7Ml5xNm6ZkA8w_95KkDWfF_CYXrHJrf1Gh95SQtJwWxcKPJxMIB6Sb87nfWkh2dHFn7AlBT_teQ8XW1I-zeYO3hmFLQGrdPGbcaX77EjCETJjZbIX8E-qPXAYz-ABQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.46M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 12:35:56</div>
<hr>

<div class="tg-post" id="msg-685808">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
حمله یمن به کشتی‌های عربستان سعودی در دریای سرخ
🔹
رسانه‌های یمنی گزارش دادند که نیروهای مسلح این کشور کشتی‌های متعلق به عربستان سعودی را در دریای سرخ هدف قرار داده‌اند.
🔹
این منابع به جزئیات بیشتر این حمله و میزان خسارات و یا تلفات احتمالی آن اشاره‌ای نکرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/685808" target="_blank">📅 12:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685807">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1ytiHGjhpN-rnAtGrXvbbTzoeJNau-_W__t7PMgVqaJ4xgTX5bV8sMigzW_vSZRAxVAWdzcUiXRkrKoPWdBNVtoA9cyYXXXctLF_dO30F4I2zkU1nQMFfTth4nulMX4J_aS21rW4wYJJdcAzsebl0l-ppN4mJdJZu4FZXUlGwGCfOT7212mLZVySRvTSr187Cc1eT_Hz_2UeXbv_E-yf_wv0iHxBRg7JbajNoUJHxAnLjj8Z2-cI4wQFCWOOwMZkz8Hgh4ldUQFvKPlcV7T8ILZjh4j2M0STByRCMPr36jYyz2XTnMZeYgylXHvEePFcEq2_tdr1_Os27FEXwMNMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیدار پزشکیان با نخست‌وزیر هند
🔹
در این دیدار، طرفین ضمن بررسی آخرین وضعیت روابط دوجانبه، بر ضرورت تقویت و گسترش همکاری‌های مشترک میان ایران و هند در حوزه‌های مورد علاقه دو کشور تأکید کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/akhbarefori/685807" target="_blank">📅 12:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685806">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ترخیص خودرو از گمرک طبق روال در حال انجام است
🔹
براساس پیگیری‌ها از گمرک، ترخیص خودروهای سواری از گمرکات طبق روال قبلی انجام می‌شود.
🔹
هیچ بخشنامه رسمی مبنی بر توقف واردات خودرو از گمرکات کشور وجود ندارد و گمرک نیز متولی این موضوع نیست.
🔹
اگر کسی مجوز واردات داشته باشد امکان توقف واردات آن وجود ندارد./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/akhbarefori/685806" target="_blank">📅 12:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685805">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be0321ba89.mp4?token=q07SYpeLxk98xDc4bTHNvIAD7vwn6f5JPgCI50VKqnuF0I9C53s20eU_F0ln_N3H5GID5bqibL9l6UMPbyxncoeE6wWUwq-R07SJQJVzOBu1lEFbuHvBo730EbddHFsudFp5_UabrGewKjhP7OKIaHpMEYTGjfIQI9Lq2H8KUi1z2849VIbBNR0srdI-OvDmq5YtZqJ89IKV3MPRkNiVBxDWjuG81YbCM6N94s0_15bV-wL9oO2z7Vpa7aIlkC2jBg62oP471wQTAC0HO4wA61RAKv1hDuMQ2CZx-OepUOXvdDCrtctGyDNoOOI_EqwX-FZHlNOF6GO3pGZKa4RghQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be0321ba89.mp4?token=q07SYpeLxk98xDc4bTHNvIAD7vwn6f5JPgCI50VKqnuF0I9C53s20eU_F0ln_N3H5GID5bqibL9l6UMPbyxncoeE6wWUwq-R07SJQJVzOBu1lEFbuHvBo730EbddHFsudFp5_UabrGewKjhP7OKIaHpMEYTGjfIQI9Lq2H8KUi1z2849VIbBNR0srdI-OvDmq5YtZqJ89IKV3MPRkNiVBxDWjuG81YbCM6N94s0_15bV-wL9oO2z7Vpa7aIlkC2jBg62oP471wQTAC0HO4wA61RAKv1hDuMQ2CZx-OepUOXvdDCrtctGyDNoOOI_EqwX-FZHlNOF6GO3pGZKa4RghQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا حالا به این فکر کردی که شعله گاز چطوری کار می‌کنه؟
#موشکافی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/akhbarefori/685805" target="_blank">📅 12:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685804">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANPoOLuWH8k0dZZLOpg8KUPvPijSErG8wfbM7teLr2JA8IBOOyRMqm5UhxpSbJK84Gn9uG-AX8EHLiIKHVTDEFS3HI6_bm1utZvyYC1utKIdilHmiWi51tPKVudYAQ2SLPjMBSLJbQCiklTSH1QTczwZSEGgvBjQ7zlX980ixRJ7UG_mFC3Qc9TTw3MwfH9d6NIqz056hfVw80JN7ftTE8YcpFDcz4m1TrqCpk_t751yVf-dmdH4Nl_jBnk1f7qbFwRmJzJMwcwYyINuDdVUjT8GySBR2SJRUje21LVN1tx0G9-LOvvgJDp0ZW5PgvRDjBfnL-vx0N46cGqwa4RMzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استخدام مخفیانه اینفلوئنسرها در پنتاگون برای حمله به منتقدان ترامپ
واشنگتن‌پست:
🔹
پنتاگون چند کهنه‌سرباز محافظه‌کار و اینفلوئنسر پرمخاطب را در سمت‌های غیرنظامی به‌کار گرفته تا از مواضع پیت هگست حمایت و علیه منتقدان دولت ترامپ فعالیت کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/akhbarefori/685804" target="_blank">📅 12:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685803">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea281b5ef7.mp4?token=UmeEr9CMrcoUkTNIJhmCOEw-qYYEwpQPO8qB8iqxvae81JNa3qV7IsQqyGhGLAp9v4ycV5EWYgg8vgIdaNBKfezF0h4I7tOm9Oxht7sXsUpAGAZH3uTIDuUSzSPzUolcKM3AgicbtdYBfccFnD5jTf2p1DrOidCBKZ7c0QcegOoN3xK_v63lWxamMWZXqtjqh1T5zFaGZ8zrolRBoNJygPEHwVeJC3sexhuvG70A8VaPKbgMxiqAvuPcFnj1p0N16epU28XS6myZIEvxVteXmzdCGOKqlv6gXLA9GvbSOZ1S7Kdmi7SM9z0PT33aDTBAoxm-PByfzR2JuoA12265qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea281b5ef7.mp4?token=UmeEr9CMrcoUkTNIJhmCOEw-qYYEwpQPO8qB8iqxvae81JNa3qV7IsQqyGhGLAp9v4ycV5EWYgg8vgIdaNBKfezF0h4I7tOm9Oxht7sXsUpAGAZH3uTIDuUSzSPzUolcKM3AgicbtdYBfccFnD5jTf2p1DrOidCBKZ7c0QcegOoN3xK_v63lWxamMWZXqtjqh1T5zFaGZ8zrolRBoNJygPEHwVeJC3sexhuvG70A8VaPKbgMxiqAvuPcFnj1p0N16epU28XS6myZIEvxVteXmzdCGOKqlv6gXLA9GvbSOZ1S7Kdmi7SM9z0PT33aDTBAoxm-PByfzR2JuoA12265qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بزرگترین قرارداد دزدی از نفت ونزوئلا/  نفت ۵۰ دلاری به ۱.۵ دلار فروخته شد  دلسی رودریگز رئیس‌جمهور موقت ونزوئلا:
🔹
با ایالات متحده توافقی تاریخی امضا کرده‌ایم که تأثیری بزرگ بر شکوفایی کشورمان خواهد داشت.
🔹
طبق این قرارداد آمریکا صاحب ۶۵ میلیارد بشکه نفت…</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/akhbarefori/685803" target="_blank">📅 12:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685802">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ذخایر گازوئیل نیروگاه‌ها برای زمستان افزایش یافت
🔹
ذخایر گازوئیل نیروگاه‌ها: ۳.۲ میلیارد لیتر
🔹
مصرف روزانه نیروگاه‌ها در نیمه نخست سال: ۷ تا ۸ میلیون لیتر
🔹
مصرف روزانه بخش غیرنیروگاهی: حدود ۸۰ میلیون لیتر
🔹
مدیرعامل شرکت ملی پالایش و پخش فرآورده‌های نفتی:­ این ذخایر برای استفاده از سوخت مایع به‌عنوان جایگزین گاز در دوره اوج مصرف زمستانی و پشتیبانی از تولید برق کشور در ماه‌های سرد سال در نظر گرفته شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/akhbarefori/685802" target="_blank">📅 12:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685793">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QHuPOLNk-9B5F2Azrsm1mt4vF4tvuLcdNqfPND5oqIvGxR_4bGYmKiIVEmRZkys4LtaHFhOVC6MOdi0AIG6qGqK9q7aXtGJvki0C4-Xs1Qxk2OA2IUuCwwPmXw_shBB4vvVTzYd9vZl-wmBqbXsVoGy4mwZd7QlVQ5Cv5aGha2Cv54oUe2EP9GDV4YEydGWKyQaFooq-K3Qix-3TrlmaGlHMUJwzdoqVyLQBgsz5-x8JG8bRiks1OWjUXZR4-Uf63Q-CNMX5HTe_7wJnvOR5QNTCHXuxmlQ55-OPhmjfK8drCeLTXWedQEO_rX0q4xEnhcPyDe0TUPgy0-78aeoR2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C_NvAHxJ0pyLUXdSor975LpnN6mA3WJatITnzAUrn5GlT_XIBYW1GbF3aFbk5JN4x3xWaRaOF0yPEAK9P-xpui1LWlRtAe6LuRmT0RyyK4r4OGU-vqg3qu1RM_cFOrwTK1qK31y2lXq0Jh0PyqHPVE_ASCCdsVIzLyskb8Ia4NQL1MMznSxETm4uy-19KwTbodJVEMWZvC0Aj07rLADudmgJm1ADkbvk0V6Mhg7ISrzXiWZgrfU2Ib3_kaPUQ5biKSESIKPZuGEnTE33lxGF_5yc2NU1A94g6dGMPKZsKZl5ol7azmjn0EGIxgEspdlY92d-dsJDUCiWVs2ri3VEuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/plVo6X6ZVtrNfIe5GeduJV8Iwhn0d6jt2FU6QorTBH0nlEE9iAjix0pOvT1xZl2a9qU8aqplx9v_dNrSD53DMH2TA6QDjDkUVWsAKYXGk1UThAuNyhtHj_E4_m0nyLj_u51mvUCtpkmoPm_Iq5bNrIlFEzDkr1zS3LvH2KwB9lMlp7bL1641o9r_sZMhQytVASEr2qfSqo1JRNnW8MQA-OTauKArp9RYebQoN9qdRe23CSE2aCeNPJJlcLtxbXKsEZ9bLBs3HbbPO1UIZBqj-GQ16ApHrifW6hw3ggvWVS2bkvlrvWOtOHRrsFK50td6O2IUPEEe44ygtblXRlvwhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LdQ_76OuyUvUc2t_Mfl49uhAMqojvfBkjKRLJ7E7ZNIjYngCZP3pm9xecvkGjEfI1G1Wz7PwPQAnf_CNm5Ga89zFvQ_ZmQlIvvnfQxfyes2PkeccurNUxGPhReKDBDgwAL5lc0EIQqlNYwjxCPyPqTMELaEB4zC-FYqwmCQzqzmkcmpncY24nMCYsjcfuuIWQE5YQUrwFmOsEjQcw_JT-5gyFfZctN-gSefIgxhv5hf8ItFmCj3BbpHsr9F52aLfNInAnsnjBZc-6gs_yANHOP576PmPdktBkvNSmC5OkBI4_0j7s2beSlqKQyg7fQLl_gD7_nALwqJutn0nrS4hWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XJx6EWsLLpMVC9AMFUPqYd2QaCRGAKBJ68qFA6ogns0R1ozagXzAg6MKD4D_hYrF4ppTH_T6FZObL3cN0SGyzsW3LDDbG28O-0M-jjqDAqBBhcPltSb_Zdti13EgZrolYOzkJAuNBXwVnOx4iYYRtQjqoc_QvwOvmdyVhBHckDjCwi_KWdCFivb_BswQl9uvyVIc_nR3DXRdrlwDJMWJF2x_bK4zgTKjWhIfvvsfquCrFx0y3mRO6IN-HFSQqou_GB3l1aK6l8rZY1bY77x-Ii_OVYurGCL0HpkbO8MwiFdaGGbjmvBJBpihWw1DMLu3_ND97GoXtihJZIL9eYwdKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZJAXjIDFzmM48JhNWUKnRQNB807jQJazs2uYhou6JmJXArqgOjC2BAgTWnsXCtY1B5jQjgVRmlqPGYdbhFLq8HHKd7d1vhgqGUahW71VB2-PimVnO0DMMT8BmM_5-u8LeDg0IoxOkmm8Z-wrXBy6MK-IUQpY2qaDk_V4Nw8cUcyEDU4SCTcY3e0fqe2m6MiAhs0qgUCKD1W80lFLPeTnSKDJQKAzKV3FnSf7X8VdghfxB3rgxqmlbVtTNCBYIuWZRSi6yQxxWwkh234mRblmiSgWZRoYhSLPv0RfzmOJ21Mg72Nhpknwez6Y14ZK5IiN_zxLk4L2Ts9B7AFLG14Mtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g3b03B-EsLTiygfy3pXz3mW6qm2j8q7xmNBjNgIpEYUAwUaukR9DirnrZIm40O-AQghFgtds-jW6hFGT_AQ6KZriL52s1gmoPH2UcQA-3hAaMP0wozIx3HGdhIwZMhbGmjNhIfwCaIDjWOaIfwYSWd4Bnkb--RS3KfGpTZ3GSmNLVXNEb1WqyOn3o6fg9_O9dLMARI-RvpfamLVnBeSs4MH6y-5GHCGQeSobReRzlxruIS3QV8tkGD4Lf5DxnvxNY_2x4ebkzVYjqBWfxrypMGlglSm-ol6UtUm8UytJxCLHX1OxZ--YTAeUzc2h_vYEYi94XoD26FPLTHmaJtPa5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kCzf3gLIYZ0vXfmEX6vdL6CSYWtgjDodwuCvJ7gJ3lKI_fg_NoMslPI1mgFyxqIHOgu34AKZ9Roandz4VVtpyCq_A0D-sbIcpygee5G_M9q_AmLjO9st62d3P9c2PJbUzJ0trlAxLD6AudxCaHVFqjKP7y6zo6xLEroEvZK8IcDBdokO7-fz5zV7O7xNvT5Lgfd72FtSuXK2VorrhAoYnm-kYYryV017Wy8FRvZjEsSH8X2NuHh7HNtsxrkJ3I3M9D4neiLvQ6AkgNOywNsNnlzbCilpl86DWDZcJNEhSkxDqsXeyy1y6Va1oGFeKMujUNnLWZD_mWUfvhcsoa7GaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v4zN_0uySPINWzsIKwuqbmg8TMIg2Y4jTAGpgiaALl4jaMpNnNzZbQd4t-O9dH62aR_nX4mDOGWZxfBy2R3ww7MRE8F5vV6m4AZOZym--66kBolX-keDtb5Sh7RLCvXnKGVVwZn8KpcqUlasETSy-rOF12WOvUQhnTNUruo1AgNwZY8MDF_Ehtd9Mg8o3qmLzvR8Hi9GO8F1wzNTQDJM-HFMgtVw1h8JeCgVo3IwPt3xRJeQdni7pAeBos8LkWWFFctOxZQ0th0ExZbFlgbKGf2yqWkP-z_s4q_m6Q1-xZAhKMGHaz5OvtIgzoMPZGK6AIw7Biww-n2IB6IG3bneXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درد دارو
🔹
صدای شما از رنجِ مسیر درمان؛ بازتاب   تجربیات شما از گرانی، کمبود  و جست‌وجوی بی‌پایان برای تهیه دارو.
🔸
پیام های صوتی خود را به آیدی زیر ارسال کنید
👇
#درد_دارو
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/akhbarefori/685793" target="_blank">📅 12:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685792">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d276f7f30.mp4?token=e_9VxmZvdnJ3w1XVOEgNSTBY25m7JeofB7gEdUTGaJZqFZMppqowTYAJsAWbMzE_7tioKEU7V4ikBfy5iQmODU9VUyfSarJG1_mFVfvupQrNUldt8Ww7Ff2niBcepsuITPYsRJVXN-QlBjBisKJw65-bW0_aGVHV_ZL9g0TyUZFJujNoqBCRY044B1DDT9ZcOjP1W_udipMzL5a2epe_L4m3WGWk38J6IKRwNEFc5RFchN227P6TXWCS10phwUxSxLzJLdGPOw-wZddV9NFpHeSm2O8ZVOJP9fy0AqxpSrjD_u3EN0b7O0meInZ9VpTRuKjDe2Q_hfwrTL4Zhj9Xqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d276f7f30.mp4?token=e_9VxmZvdnJ3w1XVOEgNSTBY25m7JeofB7gEdUTGaJZqFZMppqowTYAJsAWbMzE_7tioKEU7V4ikBfy5iQmODU9VUyfSarJG1_mFVfvupQrNUldt8Ww7Ff2niBcepsuITPYsRJVXN-QlBjBisKJw65-bW0_aGVHV_ZL9g0TyUZFJujNoqBCRY044B1DDT9ZcOjP1W_udipMzL5a2epe_L4m3WGWk38J6IKRwNEFc5RFchN227P6TXWCS10phwUxSxLzJLdGPOw-wZddV9NFpHeSm2O8ZVOJP9fy0AqxpSrjD_u3EN0b7O0meInZ9VpTRuKjDe2Q_hfwrTL4Zhj9Xqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/akhbarefori/685792" target="_blank">📅 12:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685791">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4ae1f3038.mp4?token=COT8eZlqGgMTkaBhyHabar-1VU4kjddV2T0vZw-WVj7jPfFr6dVvY_YR8km1E8y1vStH9YmI9gz0GMEjIcCuMH4MBqBVy-vuqyyBTFnZumZ8PyLtWYmo_Sgxr-S7Fb39qZCgpB4Hx_mpMKHQFJhy95UWyoABplaRzqHFvMHS0fEwC3dyAkBHqOb5mHmVUd2r4BM5YBYMupCz54rLEAFiVC8VlRFbgjOQVnBEz8LC6jaMkpcXxiVKG-GNr48cplOzzmH6ZAXnF7ILZUrqTLrOnguU7gVTxs0riaJ3rI_0k-XOGg0tPhmM-olSGYPs2X5gQDIa6jaaxbRP3lSt8-G3Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4ae1f3038.mp4?token=COT8eZlqGgMTkaBhyHabar-1VU4kjddV2T0vZw-WVj7jPfFr6dVvY_YR8km1E8y1vStH9YmI9gz0GMEjIcCuMH4MBqBVy-vuqyyBTFnZumZ8PyLtWYmo_Sgxr-S7Fb39qZCgpB4Hx_mpMKHQFJhy95UWyoABplaRzqHFvMHS0fEwC3dyAkBHqOb5mHmVUd2r4BM5YBYMupCz54rLEAFiVC8VlRFbgjOQVnBEz8LC6jaMkpcXxiVKG-GNr48cplOzzmH6ZAXnF7ILZUrqTLrOnguU7gVTxs0riaJ3rI_0k-XOGg0tPhmM-olSGYPs2X5gQDIa6jaaxbRP3lSt8-G3Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قزوین؛ شهری که هر گوشه‌اش قصه‌ای از تاریخ و زیبایی دارد
🔹
به مناسبت روز قزوین، سری بزنیم به یکی از زیباترین بناهای تاریخی این شهر؛ خانه تاریخی امینی‌ها.
#اخبار_قزوین
در فضای مجازی
👇
@akhbarghazvin</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/685791" target="_blank">📅 12:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685790">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
تبلیغ خریدوفروش وام ممنوع شد
🔹
بانک مرکزی با ابلاغ دستورالعمل جدید تبلیغات اشخاص تحت نظارت، تبلیغ خریدوفروش تسهیلات و امتیاز وام، سپرده‌های بانکی و اجارهٔ حساب را ممنوع کرد.
🔹
همچنین تبلیغ خدمات بانکی و فعالیت‌های مرتبط توسط افراد و مجموعه‌های فاقد مجوز بانک مرکزی نیز ممنوع اعلام شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/685790" target="_blank">📅 11:58 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685789">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeeTCLLWwc01HsH6OkTVPlTTTQ2yIjtIhDw_5KP_dy2kC6z6RNZC8YyE-oIrwwyoWy5I3woPSTvt8jxdmJI28e55SqyldXHNldT4ERjZq9OxmJwne6LiyA_q2bFGQ6i_ot0Bl4hjoKT6j2QOiWZ1Vc6OVeacU836N-eap_FHPSStKJ6yaKnz46dOWqWYteYKhtIDCWBxA0v6hHnSOt9Fh0W4g-Xag3TRwzs9Wkw62IWugMIb4SEbDzp9n2U-uzIC0Xtucx6yQZyeiJkcKoAY4-Vd-JkVzQaHSdfm8h6fFQ8yJ3qUqHSNpVQdhBpAlMCFYK9Yp76HO_qN1ukCrpr19A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: نتانیاهو فریبکار است!
وزیر امور خارجه:
🔹
نتانیاهو وقتی به زبان عبری صحبت می کنند با افتخار می‌گوید که دولت آمریکا را فریب داده و آن را به نیابت از اسرائیل وارد جنگ با ایران کرده است.
🔹
او صراحتاً با خنده و استهزا می‌گوید که چگونه از طریق هزار ساعت حضور رسانه‌ای در شبکه‌های تلویزیونی آمریکا، بر افکار و سیاست آنها تأثیر گذاشته است.
🔹
اما وقتی انگلیسی‌ صحبت می کند، او از توان رهبری رئیس‌جمهور آمریکا تمجید می‌کند.
افعی!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/685789" target="_blank">📅 11:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685788">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f0c60e7bf.mp4?token=oGIrVFziL-0BgblIeHOTjW13CY85LR5TDuWNXokBW95Am-nLgjJ1e90wRpk0x7izuvU5NJsd3SPYPvVUHPyIJ9PEDcUmabbFv_k7ZBwOPFTEf6O7D7RR7quvLqNrtnrrlrThPDqFAmrzSU7SihZgzEAD2ka94ccDi1jvHC-ZG6Kk5KU0Z1lUcX8MkIf9607bGy7hLmC9JbbBKdlGzgYoEHZSI47WssSJuro6YXeBEtFYPCa8k7tiwPYg_vQ9aHAigDz8_MCKxo1a5n0svuAdWPkIRJCV8fTtVuFC4XmuxyAwnc8GuLVVF2XI3ori0RZ6zObxmXneSm4K0bKOdNk3RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f0c60e7bf.mp4?token=oGIrVFziL-0BgblIeHOTjW13CY85LR5TDuWNXokBW95Am-nLgjJ1e90wRpk0x7izuvU5NJsd3SPYPvVUHPyIJ9PEDcUmabbFv_k7ZBwOPFTEf6O7D7RR7quvLqNrtnrrlrThPDqFAmrzSU7SihZgzEAD2ka94ccDi1jvHC-ZG6Kk5KU0Z1lUcX8MkIf9607bGy7hLmC9JbbBKdlGzgYoEHZSI47WssSJuro6YXeBEtFYPCa8k7tiwPYg_vQ9aHAigDz8_MCKxo1a5n0svuAdWPkIRJCV8fTtVuFC4XmuxyAwnc8GuLVVF2XI3ori0RZ6zObxmXneSm4K0bKOdNk3RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ قمارباز: اگر من رئیس‌جمهور نبودم، اسرائیلی وجود نداشت، دیگر اسرائیلی در کار نبود و احتمالاً خاورمیانه‌ای هم وجود نداشت
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/685788" target="_blank">📅 11:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685784">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38ac8adb3c.mp4?token=TMK1GlzbSx4zHikDTjskHTbDiyGqnzXEopL9n_w32qY5oezO0Rxj2saut8Zct-JxOZE6Dbrq60Vpf44GX5yV76TntoO6p-VhLPmTUj92TTl7Ye9kEb6cqfqv4wdqpkGJcha87egiL6aywEo9QWpvSlYd7Jz4hqilTj3ydlO4mlDX7E-KRtIG8YoDQtdX6PMq3mice1paNyZw6tBsCpDjcDFvALmZQV9__0dcfsDKG4iPi3AeQafpGHZjacgcIGUsa2exBirgMSXBW_cXWLWtys8xdJau71yYgWK5ZLfUUA2qI3w6Vi3tXD89VRN0OfSwxaiHBd2MCcS2zrJcB1046w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38ac8adb3c.mp4?token=TMK1GlzbSx4zHikDTjskHTbDiyGqnzXEopL9n_w32qY5oezO0Rxj2saut8Zct-JxOZE6Dbrq60Vpf44GX5yV76TntoO6p-VhLPmTUj92TTl7Ye9kEb6cqfqv4wdqpkGJcha87egiL6aywEo9QWpvSlYd7Jz4hqilTj3ydlO4mlDX7E-KRtIG8YoDQtdX6PMq3mice1paNyZw6tBsCpDjcDFvALmZQV9__0dcfsDKG4iPi3AeQafpGHZjacgcIGUsa2exBirgMSXBW_cXWLWtys8xdJau71yYgWK5ZLfUUA2qI3w6Vi3tXD89VRN0OfSwxaiHBd2MCcS2zrJcB1046w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون وزیرخارجه در واکنش به حملهٔ دیشب آمریکا به لارک: پای بیگانگان باید از منطقه قطع شود و درس جدی‌ای بگیرند تا تجاوزاتشان را تکرار نکنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/685784" target="_blank">📅 11:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685783">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGZPdNgpvO7BqGr_axEL-lFrSIEsmuLQA-x5LwaDtj9GWCiVZM82sd3occtQkoBVpzFBqhc_JFPgQQjVRTvZowd4l6SBTroJKBzfMkx3pVEKKl30BEbELYEsSwt-zCZKoEvzZe5w2r_dX9Bt7OIF-Pv-L-UogrLK8Pz5L_dgvZghyCyDeYZ6ri_BVSqEhHpwqoqP5pXj_9J8nyWxVyJWZ01mMbWqSR_lqIvBe4G95gA9wPtlEk_NU9uhzufNHUyiEtSrOjpymtIZ70L8DtlnYvJqLNG5z9z2eD7F0eTfez01MBHvHLibdhsZ0fa3eBEBae_82v03Sqxi8xMqunmVZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهم پول نقد در خریدهای حضوری چقدر است؟
🔸
سهم پول نقد در پرداخت‌های روزمره ایران تنها ۵ درصد است که آن را در کنار سوئد و نروژ میان پیشگامان حذف اسکناس قرار می‌دهد.
🔸
این در حالی است که میانگین جهانی ۱۵ درصد بوده و در کشورهایی مثل آلمان ۳۸ درصد و نیجریه ۵۵ درصد همچنان پول نقد محبوبیت بالایی دارد.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/685783" target="_blank">📅 11:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685781">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZnXE7_kUflOqJFQEKAZh8heXOtfiZCuoA4Z4X1hVOSnMzDzwVhgCFvgc8b1C8wJZZ-9aXXbEhnMo2dt7RrXr5T56O53cyOOoGYRDQKSsTKtYEKWoMvgJfS7nY-_T9ElqzT0yxobr-bOcMTUo0Qv2_pD_n4cTD7yoSUTy6gjBxhMW0NcbEvQJm6AwCnz5IoSJUDbsjWyAHHxALeLAWmoQ3sReHnt0TuqEtd5FjqqA6hqguwFFwrjSmPu--T5qI7EqaLZKq4v4uotF47PXXrR9sI3Zi78UNx83LKcl5EDaQQekdOkHSeaU114HmW7V8LMA7o__sIHufU13dyaA7iojEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C8pwfVMVsQbB0cHegMfl99XbXTUCxDYdF3bRHKx6Rjh7sXXAFo0LsX8gFnUK2sPGbjnaAPDi5tHRV2SKPbOSKqjMhMCGy2LRUAWNuPOUhAUnHK6JjxrJ0Ple0-6c59Ne0shLF6gYAEScs2XiNktO8IRzlaz2_IXDeSTMG_lvh63kF42qWEDP8UL_nAqePUYgHLT9ZergJWzvt_VVRhuwUn_3X2O-JojSHB--mMYympuDzwjBd7QqVyYF4pXoFMbUEFOAAAflnJvgL5cSjpwZ6-9QVr09-oASE2Is8qRxYoyUL29y3oe-UxMFUeIZou0lLCWMSLYsMYy6ffVk1KJkTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مشکل جدید نمایشگر گلکسی S26 اولترا؛ ظاهر شدن نقاط ریز
🔹
برخی کاربران گلکسی S26 اولترا از ظاهر شدن نقاط و لکه‌های ریز روی نمایشگر خبر داده‌اند؛ هنوز مشخص نیست این مشکل با آپدیت اخیر سامسونگ برای رفع هاله قرمز مرتبط است یا خیر.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/685781" target="_blank">📅 11:19 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685780">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a43d12927f.mp4?token=XOFGOtTtpxN2Ksoav9RqPWi5KyN2wBaD9oS4cxjQFZdBynUbyF_ji9xtZ11ypPM3Z7Q3BP2ZsXiqjohk_opPbbRZ1HKF4CdU5DN9vXfJwVVKee-4MLgG_SguJ10ARNQJIwJMwzxpg_xiCA0vhMrhOmTN1kuPLp7QBgAvOTVdLLrI-B_YhjDzgeN_pcYwRgL_lBEbHdi_1TeV80DSD9FEoXbFfljavMbtEenr1W9PaGXd3HvuzbJG7WKcGYohYB8unxOdcAE9NOpGGX1k4sd5J_psl2gg5GBpiJNfsfdeo70s2joyojoYn6SIoUDHIMsObrOp9O2z-NhKg1DS6G9NOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a43d12927f.mp4?token=XOFGOtTtpxN2Ksoav9RqPWi5KyN2wBaD9oS4cxjQFZdBynUbyF_ji9xtZ11ypPM3Z7Q3BP2ZsXiqjohk_opPbbRZ1HKF4CdU5DN9vXfJwVVKee-4MLgG_SguJ10ARNQJIwJMwzxpg_xiCA0vhMrhOmTN1kuPLp7QBgAvOTVdLLrI-B_YhjDzgeN_pcYwRgL_lBEbHdi_1TeV80DSD9FEoXbFfljavMbtEenr1W9PaGXd3HvuzbJG7WKcGYohYB8unxOdcAE9NOpGGX1k4sd5J_psl2gg5GBpiJNfsfdeo70s2joyojoYn6SIoUDHIMsObrOp9O2z-NhKg1DS6G9NOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امروز دوشنبه ۹ شهریور ماه، خبرفوری در مراسم افتتاحیه بیست و نهمین نمایشگاه الکامپ  در سالن ۶ غرفه ۳۲ همراه و میزبان شما عزیزان خواهد بود
@Tv_Fori</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/685780" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685779">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2405fdfefc.mp4?token=j2RuAhcucwuNfU39h8dASJlQMd5hDZwUjAzWQM5V-uBCXkudXltdVWeBMY2ozXFlgzUW1dKrKfvupMaYTXkahwjy41e5b4DoJu0IGmXCINbOly3hR5OBMNuJJLtp6I9khWolDHnrBRkqG2if8rAR5EfHsMBW_ABGbpdZGTRKXWfnu5UHBV6M3D9GdBKJZgIxXIN6GuYjo5gNhCOiIoNtIgt0T9Q-6ba8lA60bDlBsmts0cvbwL-ntUrkGQR0fYcSm7RJ4UGAJCY5_R0Xto-p1F6AUSIDPmXINxMx2APrOc2x7IVERXHtb1N0OUxxMnehK-0OcFIu4fSFTLQrNj-5Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2405fdfefc.mp4?token=j2RuAhcucwuNfU39h8dASJlQMd5hDZwUjAzWQM5V-uBCXkudXltdVWeBMY2ozXFlgzUW1dKrKfvupMaYTXkahwjy41e5b4DoJu0IGmXCINbOly3hR5OBMNuJJLtp6I9khWolDHnrBRkqG2if8rAR5EfHsMBW_ABGbpdZGTRKXWfnu5UHBV6M3D9GdBKJZgIxXIN6GuYjo5gNhCOiIoNtIgt0T9Q-6ba8lA60bDlBsmts0cvbwL-ntUrkGQR0fYcSm7RJ4UGAJCY5_R0Xto-p1F6AUSIDPmXINxMx2APrOc2x7IVERXHtb1N0OUxxMnehK-0OcFIu4fSFTLQrNj-5Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هنگام خرید دلار، این نکته مهم را حتماً در نظر داشته باشید
💵
👌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/685779" target="_blank">📅 11:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685778">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
ادعای نیویورک تایمز به نقل از مقامات نظامی آمریکایی: نیروهای ما تنگه هرمز را زیر نظر دارند و آماده حمله به نیروهای ایرانی تهدیدکننده کشتیرانی هستند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/685778" target="_blank">📅 11:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685777">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
امارات، حمله به پایگاه هوایی منهاد را تکذیب کرد
🔹
وزارت دفاع امارات در واکنش به اطلاعیه امروز ارتش جمهوری اسلامی ایران مبنی بر هدف قرار دادن پایگاه هوایی المنهاد در جنوب امارت دبی با ده‌ها پهپاد انهدامی را رد و ادعا کرد: آنچه در رسانه‌ها منتشر شده مبنی بر هدف قرار گرفتن پایگاه هوایی المنهاد با موشک، صحت ندارد./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/685777" target="_blank">📅 11:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685776">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
الجزیره: پزشکیان و پوتین در حاشیه اجلاس شانگهای دیدار می‌کنند
🔹
بر اساس گزارش الجزیره، مسعود پزشکیان و ولادیمیر پوتین قرار است در حاشیه اجلاس سازمان همکاری شانگهای در بیشکک دیدار و گفت‌وگو کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/685776" target="_blank">📅 11:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685775">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMubQPoFXBNyWT_q1qbU1JfRqe_G-CvVlrxGlrwBpTA_mBb-gHGk0_ribNDq1mie2-Msd1c0EYanXXFE3IexfaLwft2IaUtnQsondIH0xu3xutvBXYcO6gPNeFz3f6LsiJzUmVrG9Rjoa04sJQf6I-QhDzBwdn2t0BvR-fOXzO2r2a6X7_Dxa5w7jJb4Q-XutNIPSOeiR8BJvuu95D3Xudwqgftb2jee36VAyzlJe5AiAJ3vdrLMc52VgX_ht694gCy3-1R0wlCeiXj3hB5yj1xNGJkwCB9uV63PkkyiPfqCnHbb-XE6oUm6MyDMfV2Cb8qTiILbMTM77csD1PEYbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستبرد ترامپ به ثروت ملی ونزوئلا؛ غارت ۶۵ میلیارد بشکه نفت
🔹
دونالد ترامپ، رئیس دولت تروریستی آمریکا، در جدیدترین اقدام خود برای تاراج منابع کشورهای مستقل، مدعی دستیابی به توافقی با ونزوئلا شده است که از آن به عنوان «عظیم‌ترین معامله تاریخ جهان» یاد می‌کند.…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/685775" target="_blank">📅 11:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685774">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
کشتی آلاینده خلیج فارس در آب های هرمزگان توقیف شد
معاون دریایی اداره کل بنادر و دریانوردی هرمزگان:
🔹
به دنبال تخلیه مواد نفتی از یک کشتی در خلیج فارس و آلوده سازی محیط زیست دریایی، کشتی متخلف توقیف شد./ ایرنا
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/685774" target="_blank">📅 10:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685772">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a77071702.mp4?token=JWca1nL7CHBZyNbrcb0GF_2keNsBkjS-LKpC3EM4Xcl4yeQWgP12rvT4ayZF0GSCwwTHYdmk3pP7XrtS8t6IOTOOKh4Owa3BOXnOtFwd119liElR3s3ldQP947hCiBCYnERTBtN9_U2x86vW56q3e5l-eAxpIoVu--cDPtAkZ_W06C6rOPd88bh0vFoC554-RKCUBQx_bEH2l15MDQXDiekkWEpIUPbt4v1UkP4I1B9ybPKotSScSS6jsRUjuceDrx3KyeHtPVZVKfisugJNfvmzf6Vd8QWx99-W1oi5h9GXqZPqh14sGibK_BgCy839nWDVGhpBsHyGTVMNMVQC8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a77071702.mp4?token=JWca1nL7CHBZyNbrcb0GF_2keNsBkjS-LKpC3EM4Xcl4yeQWgP12rvT4ayZF0GSCwwTHYdmk3pP7XrtS8t6IOTOOKh4Owa3BOXnOtFwd119liElR3s3ldQP947hCiBCYnERTBtN9_U2x86vW56q3e5l-eAxpIoVu--cDPtAkZ_W06C6rOPd88bh0vFoC554-RKCUBQx_bEH2l15MDQXDiekkWEpIUPbt4v1UkP4I1B9ybPKotSScSS6jsRUjuceDrx3KyeHtPVZVKfisugJNfvmzf6Vd8QWx99-W1oi5h9GXqZPqh14sGibK_BgCy839nWDVGhpBsHyGTVMNMVQC8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حادثه گویانیا؛ عجیب‌ترین فاجعه هسته‌ای جهان!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/685772" target="_blank">📅 10:39 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685771">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
افزایش سه‌برابری نرخ ژتون غذای دانشجویان صحت ندارد
مدیرکل دانشجویی وزارت بهداشت:
🔹
افزایش نرخ ژتون تغذیه کمتر از دو برابر خواهد بود.
🔹
بر اساس نرخ‌های تعیین‌شده که البته هنوز نهایی نشده است، صبحانه ۶ هزار تومان، ناهار ۱۳ هزار تومان و شام ۹ هزار تومان خواهد بود.
🔹
اجاره بهای خوابگاه‌های دانشجویان برای مهر امسال افزایشی نخواهد داشت./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/685771" target="_blank">📅 10:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685769">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
وزیر کار: امشب معوقات بازنشستگان واریز می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/685769" target="_blank">📅 10:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685767">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
موافقت دولت با تشکیل جلسه کمیته بازنگری مزد ۱۴۰۵
«باقری»عضو گروه کارگری شورای عالی کار:
🔹
وزارت کار در نهایت در برابر مطالبات جامعه کارگری انعطاف نشان داده و موافقت اولیه برای برگزاری جلسات کمیته مزد حاصل شده است.
🔹
هزینه زندگی که در دی‌ماه سال گذشته حدود ۴۳ میلیون تومان برآورد شده بود، اکنون به بیش از ۸۰ میلیون تومان رسیده است./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/685767" target="_blank">📅 10:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685766">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1e9478c7b.mp4?token=BY-TpaIkZcNwUiZ47Iqv4j69o1ZNduPrT7aMBvnX8ANdnOTQ1OwsKLPH4p3zLxaKm0Fh6Q0hO9zrfxT49HdkvuWFZNk4AHtkeWKdm49iF542DGNbHCWpWYyR7wmTLJAbJ_wsbgj0zSq5u7_cGiV74nis2V8hGwkR057KHok2o8Qa3DC9daewmgoNj2PlxMvEFxQ2yfOkOYTgHwbrvnVvym1qKf4AIGnBZIlrtwedPYYYoOQqpsCu2ws7hSaTBP_7NuzimOiKgYj9ktG8-jA5ltFgaaZFjItjDXGUIqbMFWmG6gw1uwIl44uRx-uTy8o_cfBPC1EH2oHQcsV0ufP7mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1e9478c7b.mp4?token=BY-TpaIkZcNwUiZ47Iqv4j69o1ZNduPrT7aMBvnX8ANdnOTQ1OwsKLPH4p3zLxaKm0Fh6Q0hO9zrfxT49HdkvuWFZNk4AHtkeWKdm49iF542DGNbHCWpWYyR7wmTLJAbJ_wsbgj0zSq5u7_cGiV74nis2V8hGwkR057KHok2o8Qa3DC9daewmgoNj2PlxMvEFxQ2yfOkOYTgHwbrvnVvym1qKf4AIGnBZIlrtwedPYYYoOQqpsCu2ws7hSaTBP_7NuzimOiKgYj9ktG8-jA5ltFgaaZFjItjDXGUIqbMFWmG6gw1uwIl44uRx-uTy8o_cfBPC1EH2oHQcsV0ufP7mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ژست‌های بامزه دانش‌آموزان تایلندی در مراسم فارغ‌التحصیلی
😂
🎓
🔹
فارغ‌التحصیلان دبیرستان Satit PSU با ژست‌های خلاقانه و خنده‌دار هنگام دریافت گواهی، در فضای مجازی وایرال شدند؛ حتی مدیر مدرسه هم به آن‌ها پیوست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/685766" target="_blank">📅 10:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685765">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ab76c6421.mp4?token=NDN8tFt02j70NnBZNXcBRNEN37nw6vwXyV__V2MeR5x6IHlvNSZDE927TDdtguhB8SuszwI-_9OGZWkt5z2tBFua5YU2N8HPchIf9LyYerdbOjb-2kwGX1ZDMEwusZqT_MlsU9E-QDgNwBJy5hgTV4qwZn6VsQh15hHVjMX_FKEdmc2Y_5T41NWEz9ko852pMmBLSQIkd-IPMCMpzcTKJRXSlgICeOElTTPSI9oq40IzCaTcnSiuIX7lFgXTE9zxnQFvcva-WyDmUyBgKfRIt__JoKonfBh3tlPTjPmlYWQlRWB3N8uCw8sodEJt8LgfvHahtMIdNMjq5Zqax7UAJbiSyVfbwn89JlBBfR_rPF3jELJh0wwv_CxjhEEjH-o8zzqizGMr1jA8qFOB0LY_wTLcoF_JomsoXQKRg3TLm51v9phmURhzoqi_go3_AUauCpcPxWNIQ3Fr9LmDby69YsQjWY5QatDac_Me9dGos8rO5-X5L_1_fv1NZsHttPeXzSoSYvvG9iE5tdodOmOnvyOX4nqxVb9Lb742mlYsP726DJxnQl7AMTeVZzkLJxcxtWr5yk_c0iRimJ7xK90jv_lLzQDSWHaxqSaYkAV43kVRhQTV8FeiCHa7zYGKtlAqiR3YTHUmVvY3lVmQI2rO_wN89l_DNRu7IDcqO8taqUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ab76c6421.mp4?token=NDN8tFt02j70NnBZNXcBRNEN37nw6vwXyV__V2MeR5x6IHlvNSZDE927TDdtguhB8SuszwI-_9OGZWkt5z2tBFua5YU2N8HPchIf9LyYerdbOjb-2kwGX1ZDMEwusZqT_MlsU9E-QDgNwBJy5hgTV4qwZn6VsQh15hHVjMX_FKEdmc2Y_5T41NWEz9ko852pMmBLSQIkd-IPMCMpzcTKJRXSlgICeOElTTPSI9oq40IzCaTcnSiuIX7lFgXTE9zxnQFvcva-WyDmUyBgKfRIt__JoKonfBh3tlPTjPmlYWQlRWB3N8uCw8sodEJt8LgfvHahtMIdNMjq5Zqax7UAJbiSyVfbwn89JlBBfR_rPF3jELJh0wwv_CxjhEEjH-o8zzqizGMr1jA8qFOB0LY_wTLcoF_JomsoXQKRg3TLm51v9phmURhzoqi_go3_AUauCpcPxWNIQ3Fr9LmDby69YsQjWY5QatDac_Me9dGos8rO5-X5L_1_fv1NZsHttPeXzSoSYvvG9iE5tdodOmOnvyOX4nqxVb9Lb742mlYsP726DJxnQl7AMTeVZzkLJxcxtWr5yk_c0iRimJ7xK90jv_lLzQDSWHaxqSaYkAV43kVRhQTV8FeiCHa7zYGKtlAqiR3YTHUmVvY3lVmQI2rO_wN89l_DNRu7IDcqO8taqUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پلومخلوط رو به این سبک درست کن، مطمئنم عاشق طعمش میشی
😋
مواد لازم:
🔹
شوید خشک
🔹
لوبیا چشم‌بلبلی
🔹
برنج
🔹
سیب‌زمینی
🔹
سیر
🔹
زردچوبه، نمک، فلفل‌سیاه
🔹
سینه‌ مرغ #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/685765" target="_blank">📅 10:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685760">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BT3oNQT2U56rmcS17aCS4SBttRj7bI6oI4b_Ji2wWLlpJh1XnFBXFyUlVUo2jYPQkUYLigGwVJFc66dhSCtunzZmMdP1t5EK3dx7lhoJmnVHlg3qQ9xz6yI2BZqh7zeQ_Dps5XQq7tyino1AQrZYGDnQ6V7_534w2-OrNAJwptW6vhA3JavzsuGoQtUwE7Rfj13RaXmukv7zw0YkleMErT4sSi1WqG8qs2Yrdnf-OV1c86COlBaRgS4gmzs5R7ytwMS-grLAtQjICXtYbM8h4h4ANaXEGnkRvyFkumqrcqRwUh_kAgYqxht9idd4HaJO2vOsyO3J5yya98jrPvf7Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت یکی از کارکنان نیروی دریایی سپاه در پی حمله به جزیره لارک
🔹
شهید علی فیاضی، از کارکنان نیروی دریایی سپاه، صبح امروز در پی حملات ارتش آمریکا به جزیره لارک به شهادت رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/685760" target="_blank">📅 09:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685758">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/452d494968.mp4?token=I7XVD04GKwjBM0DCbtrtRD9D6rgbEWP4B2BWEZRfW2K0bWv_99hMbgdTrRd_C3fShHunnhLCODnBwWSDbTd_xednifkBSp9rWGKvzNSOWPIsHZOQXnsQ1m8DrWavfc1FuWddglI6abN2XUBlCZucjFs6fc_NrRMLOizqM_XnqpAj1BFLv4CLgZI0ZFV2E-m1LgpPIqg5hPfKDuMytVevjgwEH1BOrK3tn8v1u5FpTfBk_zS_gD_wGnGaizgcNNJ3RLUwuuuwss2Pm8yHoGvcn0uk17j78mnJB59XPiuhlAJueRfedudZYJTavg-CDFG1Ln_p-mu31gd4o9fU6ajjKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/452d494968.mp4?token=I7XVD04GKwjBM0DCbtrtRD9D6rgbEWP4B2BWEZRfW2K0bWv_99hMbgdTrRd_C3fShHunnhLCODnBwWSDbTd_xednifkBSp9rWGKvzNSOWPIsHZOQXnsQ1m8DrWavfc1FuWddglI6abN2XUBlCZucjFs6fc_NrRMLOizqM_XnqpAj1BFLv4CLgZI0ZFV2E-m1LgpPIqg5hPfKDuMytVevjgwEH1BOrK3tn8v1u5FpTfBk_zS_gD_wGnGaizgcNNJ3RLUwuuuwss2Pm8yHoGvcn0uk17j78mnJB59XPiuhlAJueRfedudZYJTavg-CDFG1Ln_p-mu31gd4o9fU6ajjKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افسر بازنشسته آمریکایی: هیچ‌کشوری نتوانست جلوی موشک‌های ایران را بگیرد
سرهنگ دنیل دیویس:
🔹
وقتی ایران شلیک می‌کند، موشک‌هایش معمولاً به هدف اصابت می‌کنند و هیچ سامانه‌ای نتوانسته جلوی این حملات را بگیرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/685758" target="_blank">📅 09:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685756">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4b19e7a78.mp4?token=qkEODRMHOgTtla-gPWcurmuJ1d4o31nVZFcmDqizPJh2v_8kTLzlSMNon3iwhvQtOpo0vPiKr846F2DM8CdO9yRoKG8_0eYevcIUc0dEpDsSLwEevs4lxE_Ax4hMRxF6wAlczTpgAXa5ev5TTDCoZJLkJz39isp_PHMkfCoYUrc_dmRT8QrZp18wnWCJt6KuDErzlZw7LY8wNkAhEXMvb_KvEN7p7lLkhff5nKj5Ny_QC38EdBKueasTgTQ9u1LKezoJtZqRfi-eGPl6dRJsbZEy0CehSbmMTkb50CGxXB_RD60_MhIt9qg1NfV8OPx6mrAzNAmE5x-bBHcohTRu6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4b19e7a78.mp4?token=qkEODRMHOgTtla-gPWcurmuJ1d4o31nVZFcmDqizPJh2v_8kTLzlSMNon3iwhvQtOpo0vPiKr846F2DM8CdO9yRoKG8_0eYevcIUc0dEpDsSLwEevs4lxE_Ax4hMRxF6wAlczTpgAXa5ev5TTDCoZJLkJz39isp_PHMkfCoYUrc_dmRT8QrZp18wnWCJt6KuDErzlZw7LY8wNkAhEXMvb_KvEN7p7lLkhff5nKj5Ny_QC38EdBKueasTgTQ9u1LKezoJtZqRfi-eGPl6dRJsbZEy0CehSbmMTkb50CGxXB_RD60_MhIt9qg1NfV8OPx6mrAzNAmE5x-bBHcohTRu6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نحوه‌ کارکرد داخل سشوار
#موشکافی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/685756" target="_blank">📅 09:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685754">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
فردا آخرین مهلت انتخاب رشتۀ ارشد ۱۴۰۵
🔹
داوطلبان مجاز به انتخاب رشته آزمون کارشناسی ارشد ۱۴۰۵ تا سه‌شنبه ۱۰ شهریور فرصت دارند انتخاب رشته خود را در سایت سازمان سنجش ثبت کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/685754" target="_blank">📅 08:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685753">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c764ecaa0.mp4?token=QOrnTt0jjZ0wwKzHlrvMg5XI_8x28jQHGKh4EKU4cdI8d0pA549HrWRblDLjmUUblKxUkfvNO3DtZosRK-OoZ3uwCAFBDiWCXsUOH4Xn1oBz1EG9UsY3sMRIlgOVjJ8UeUUu7uCEZcqXgA9XQ3LVKRnqa-b4Iaf1J3Yq0TI2lSGoWh0ovKijrVNqJN5RWBjMLydKGQBA_GrxSWXoJ0Rf_b_aMbu8wdPwC7dlZ1NJBtlTvIXio0jGrb5rK44tbOn8oRCtpEyNv1Gmf5jA5EwL8etvvuQfSsNoORJv0cCjfO2fvjb_zOBIUP2tL0aVkghu17wQiOobIw1RUWUU46hPCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c764ecaa0.mp4?token=QOrnTt0jjZ0wwKzHlrvMg5XI_8x28jQHGKh4EKU4cdI8d0pA549HrWRblDLjmUUblKxUkfvNO3DtZosRK-OoZ3uwCAFBDiWCXsUOH4Xn1oBz1EG9UsY3sMRIlgOVjJ8UeUUu7uCEZcqXgA9XQ3LVKRnqa-b4Iaf1J3Yq0TI2lSGoWh0ovKijrVNqJN5RWBjMLydKGQBA_GrxSWXoJ0Rf_b_aMbu8wdPwC7dlZ1NJBtlTvIXio0jGrb5rK44tbOn8oRCtpEyNv1Gmf5jA5EwL8etvvuQfSsNoORJv0cCjfO2fvjb_zOBIUP2tL0aVkghu17wQiOobIw1RUWUU46hPCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای پاییزی با کاهش محسوس دما و ادامه بارش‌ها در نوار شمالی کشور
🔹
بارش‌های پراکنده رگباری در جنوب شرق کشور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/685753" target="_blank">📅 08:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685752">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyIKpymZ_8fg4rDNWvuV8RbRGszpLNJImkPR5tOhyzgUOT6LMQFHl3cfmsJ1_5EwOOek2ekLhL1z-PJCTRMCl9UNp8tXWx8bf3hO8Z11E2ykZbNL1m4cY3tmA7SpgiuwLeCBCII2sqcw-WWPx7YCwmI2_EymjNY39WU9uvElMomXEyTvwOl_ila4_W5V6V0cRPEtVNB_nSuCNpVHFOjlMKTGLTMGU5WENc4-DsOkVxtMLaTOkgpIwAPycfdrcHlOul7xGAgh0MYH-wjTXdhv0vhpz3_D_vt_RDvNUB2eBSZ_1x69YuxtrrbC4cgo5OocnunEJN__EN4oXBctl9aUdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آلون میزراحی، فعال رسانه‌ای اسرائیلی- آمریکایی: پیروزی ایران کامل و تاریخی خواهد بود و مسیر تاریخ را برای همیشه تغییر خواهد داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/685752" target="_blank">📅 08:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685751">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc74a6ed5f.mp4?token=bwZ9XsNpxnZcPyGbjjXUMbLDx3JfWyw8un59FXo3_XAIOWwmNeS4jXoWvKK4Zj4wSyzfLDgFzxSp7QzB0dTZwkkrfobvhvqvlCFk0byuaufnGG22w0HNsZvPdSQXgqOA5ZpgOX1_FThNJqMtVJ2bKZKQCFiUqnXD3j2Z_kZRzpgc5unrhy0A80vDbS4unZA1AdK6xUvM7C64GVxArNrG6pXp39ys1hwcSAEvtFS2SxmH_DyofQl_rHUXuEK2_uoPxIXmeWjbl_ovUkRGvFvMD5m84qzwFtQ3Lm3nlGMQBiRXU379_klhBDyVkitrGSXWsgjoKYwYeJokdNaf_or-qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc74a6ed5f.mp4?token=bwZ9XsNpxnZcPyGbjjXUMbLDx3JfWyw8un59FXo3_XAIOWwmNeS4jXoWvKK4Zj4wSyzfLDgFzxSp7QzB0dTZwkkrfobvhvqvlCFk0byuaufnGG22w0HNsZvPdSQXgqOA5ZpgOX1_FThNJqMtVJ2bKZKQCFiUqnXD3j2Z_kZRzpgc5unrhy0A80vDbS4unZA1AdK6xUvM7C64GVxArNrG6pXp39ys1hwcSAEvtFS2SxmH_DyofQl_rHUXuEK2_uoPxIXmeWjbl_ovUkRGvFvMD5m84qzwFtQ3Lm3nlGMQBiRXU379_klhBDyVkitrGSXWsgjoKYwYeJokdNaf_or-qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار کره جنوبی را تهدید کرد
🔹
رئیس دولت تروریستی آمریکا، در واکنش به خودداری کره جنوبی از مشارکت در جنگ آمریکا علیه ایران، تهدید کرد که واشنگتن ممکن است در تعهدات امنیتی و حضور نظامی خود در این کشور تجدیدنظر کند.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/685751" target="_blank">📅 08:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685750">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hImtKv4xkHIqEDtMrG0yXBRU_hSBs8JndHSnuFnK-50fZfQ2jbFjf0AcW_le5oCXUJR1YNAIl0fg1ash6s6Hx6MljjjTlsS8fkjuiagxd71y7VmSpQou4PKLu9X_WZgNPT3kdAv7yh2b6JPcCPdAGB-r0wzKOLK5UUNYyPHdixriBGyTXKrw2zTiJc3ovaU5fjOGSe__meppnF-0swq9yx4DnYem3KE9NIpVvRX3socUeaX5JiG1cVliTOBgEGVg0J3mMxCOkBfaRQhCcOgfWJyNg-Me1VzftES9pHLcjZE7ZjZKSs-FMh4SCNQDf_RXKlLA6JgwFKnlIXrIpQt3kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنینی که قبل از تولد، یک‌بار از رحم خارج شد
🔹
پزشکان آمریکایی در یک عمل بسیار نادر، جنین ۲۳ هفته‌ای را برای برداشتن توموری خطرناک که ممکن بود قلب جنین را از کار بیندازد، به‌طور موقت از رحم مادر خارج کردند و پس از جراحی دوباره به رحم بازگرداندند.
🔹
بارداری ادامه پیدا کرد و نوزاد در حدود هفته ۳۶ بارداری به دنیا آمد؛ روایتی شگفت‌انگیز از پیشرفت جراحی جنین که لقب «دو بار متولد شدن» را برای این نوزاد به همراه داشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/685750" target="_blank">📅 08:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685748">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83c220362d.mp4?token=UfL4YcZMccPQix5yDyXZbA53HAa7inxeVbHwGPK-IHhYXmKXBl9muJYz36BROjbhXfan9xO_I_-n2K8IwHvi9p05_Ap7mZrCS9P3U8R4Y78OZFlgLSJeyEonRb_3B51x5zc8DgJk77e7zfPaSYeXSnyLlA1s6zdDtRBSDb8gltg5h_XuelGoqcqqjNT-5OUEkyxthywaAyUFvtXJjKEAziYX4n8oW-DoyngaA-vgxhUkLj60_gjiqRzpb3kcoE106z7Ar1gGYbLEgNfX6AHk9LBFYMpQ8a0nveXrUoIxTY4b5Nmx5X9iEl0BZS7t3aFj1XxS7zrgqQPs9DmcIVRgmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83c220362d.mp4?token=UfL4YcZMccPQix5yDyXZbA53HAa7inxeVbHwGPK-IHhYXmKXBl9muJYz36BROjbhXfan9xO_I_-n2K8IwHvi9p05_Ap7mZrCS9P3U8R4Y78OZFlgLSJeyEonRb_3B51x5zc8DgJk77e7zfPaSYeXSnyLlA1s6zdDtRBSDb8gltg5h_XuelGoqcqqjNT-5OUEkyxthywaAyUFvtXJjKEAziYX4n8oW-DoyngaA-vgxhUkLj60_gjiqRzpb3kcoE106z7Ar1gGYbLEgNfX6AHk9LBFYMpQ8a0nveXrUoIxTY4b5Nmx5X9iEl0BZS7t3aFj1XxS7zrgqQPs9DmcIVRgmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم با «حمله خیالی» به خارگ شاخ‌وشانه کشید
🔹
ترامپ در تازه‌ترین نمایش توهم‌آمیز خود علیه ایران، ویدئویی ساخته‌ شده با هوش مصنوعی از انفجار و آتش‌سوزی در تأسیسات نفتی جزیره خارگ منتشر کرد و مدعی شد: «جزیره خارگ دارد با خاک یکسان می‌شود!!!»
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/685748" target="_blank">📅 08:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685747">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c52c75ad9.mp4?token=vZN_RjmvS09vOAOou4lHR33JGTRbJsTLexi3meDoadrgHwqS7bjvYymlDxb_LaWyPnEvLl7jyr1q_z2_Y74FbVyPS6CmALjbqNArfoXlZw5AjG_BMzhogSLQAx4xPHuJDRr2JSkUjXPDbsSeYu87olOKA16QL7UOliDg2dgbfDFWLdM_foYHJFT8N_R2WQctfOuqgmtV5IYedbwO6iYN5rpRSbkF1hwiixBCzA3f0bpwST-BnWMSC1DmkUUSAXQYv-QTz1J9Cz83fKQVU9t4u_S12yV_Usr8yswxM7fN2RSH4fjqAdRKzVzHeBzP0r78Pxrf1FozPPmODTL03B8JiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c52c75ad9.mp4?token=vZN_RjmvS09vOAOou4lHR33JGTRbJsTLexi3meDoadrgHwqS7bjvYymlDxb_LaWyPnEvLl7jyr1q_z2_Y74FbVyPS6CmALjbqNArfoXlZw5AjG_BMzhogSLQAx4xPHuJDRr2JSkUjXPDbsSeYu87olOKA16QL7UOliDg2dgbfDFWLdM_foYHJFT8N_R2WQctfOuqgmtV5IYedbwO6iYN5rpRSbkF1hwiixBCzA3f0bpwST-BnWMSC1DmkUUSAXQYv-QTz1J9Cz83fKQVU9t4u_S12yV_Usr8yswxM7fN2RSH4fjqAdRKzVzHeBzP0r78Pxrf1FozPPmODTL03B8JiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکات مناسب برای از بین بردن چربی زیر شکم  #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/685747" target="_blank">📅 08:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685746">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
نیروی دریایی سپاه: یک فروند سوپر نفتکش متخلف در اثر اصابت با دو مین دریایی دچار آتش‌سوزی‌های مهیب شد
🔹
ساعاتی پیش یک فروند سوپر نفتکش متخلف که قصد عبور از مسیر غیر قانونی جنوب تنگه هرمز را داشت در اثر اصابت با دو مین دریایی دچار آتش‌سوزی‌های مهیب شد و بطور کامل متوقف گردید.
🔹
نیروی دریایی سپاه مجددا اخطار می‌کند سرنوشت کشتی‌هایی که از مقررات امنیتی تنگه هرمز تخطی کنند جز این نخواهد بود. رعایت مقررات ابلاغی نیروی دریایی سپاه برای عبور و مرور الزامی است، شرکت‌های کشتیرانی فریب تحریکات ارتش کودک‌کش آمریکا را نخورند و اموال و جان خدمه کشتی های خود را بی جهت در معرض نابودی قرار ندهند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/685746" target="_blank">📅 07:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685745">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
دقایقی پیش زلزله‌ای با قدرت ۳.۸ ریشتر در عمق ۸ کیلومتری پردیس در شرق تهران را لرزاند  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/685745" target="_blank">📅 07:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685742">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
پایگاه آمریکایی «المنهاد» در امارات هدف پهپادهای ارتش
روابط عمومی ارتش:
🔹
از بامداد امروز در پاسخ به تجاوزات اخیر دشمن متجاوز و در انتقام شهدای دلیر سپاه پاسداران انقلاب اسلامی و مردم بی گناه ایران اسلامی در جزیره لارک، ارتش جمهوری اسلامی ایران، محل های استقرار بالگردها و نیروهای ارتش کودک کش آمریکا در پایگاه «المنهاد»  امارات را با شلیک دهها پهپاد انهدامی، هدف قرار دادند.
🔹
پایگاه المنهاد، یکی از مراکز مهم پشتیبانی و جابه جایی هوایی نیروهای خارجی است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/685742" target="_blank">📅 07:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685741">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
دقایقی پیش زلزله‌ای با قدرت ۳.۸ ریشتر در عمق ۸ کیلومتری پردیس در شرق تهران را لرزاند
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/685741" target="_blank">📅 07:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685740">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZG7fJV93_NkcNw6oVekfmjUl_6XcwIspw4B1u_a-iemHB0wm-GmKmgsgUulORInGVU3x0jHi48dR-isuaLY53Kr1NXhwqUEaxkCp4-DVczKK61Wj3NKTJGsnXS3mM973XXXhUQIBCDrph-ezbZdSmcEHkEWNx2RVb6PrQdXY0efSrPxLgglMRRUKm4_egBof7Br77PDbL2FY41OvpncnbkfSoIhRTngz5O1JtLShwOC6ZGz9MzlmAWjT4uOGM0XW68YiRIpzxUVcbgdMTAqW_ltGe_9TAat35p2ZMCswTNMm065Z6IGmPj75KMxZydXAiPgDN4YXXc1xMkp6MipXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز دوشنبه
۹ شهریور ماه
۱۸ ربیع‌الأول ‌‌۱۴۴۸
۳۱ آگوست ۲۰۲۶
دوشنبه‌ها
#زیارت_عاشورا
بخوانیم
⬅️
متن و صوت زیارت عاشورا
@AkhbareFor</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/685740" target="_blank">📅 07:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685739">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
سپاه: یک فروند پهپاد MQ۹ آمریکایی بر فراز تنگه هرمز مورد اصابت قرار گرفت و به داخل آبهای نیلگون خلیج فارس سقوط کرد
روابط‌عمومی سپاه:
🔹
دقایقی پیش با آتش موشکی رزمندگان همیشه بیدار پدافند هوایی نوین سپاه پاسداران، یک فروند هواپیمای بدون سرنشین دور برد MQ۹ آمریکایی بر فراز تنگه هرمز مورد اصابت قرار گرفت و به داخل آبهای نیلگون خلیج فارس سقوط کرد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/akhbarefori/685739" target="_blank">📅 06:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685735">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUKM92CKleZqMgKN9PW6EoHYovNwr0EyQEOWUD3VSSzXwRNPNQHhmTd0NcwJk3XjP3mjR89TvUu4hr5kv5ZFyNzESaZGxTRgNbzPKTquUgTgK3krXkn_a-zDdnCSDtOG0rBzcbfjk7hcOvgbveZyaaZhQ7DKTZ-_65FuSJzD1DknNEYCqkmuLBT2C5rZjf8Fz7Otbh038w3fwW0JfX2ns3nkZ9VA_gDoYviLQIYHTEnqyB1YoXSjo7dHOFoW-T_tWxxWFpFDX7S3N38i9lC7A_f0IzvtVaHgNIfF6xCDLYFt9u1Mw3GqBwSQxOLLVbN24lbnH0lA7WzsRmOh20Qf7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت والیبال مشهد به لیگ برتر با پیراهن استقلال
سید حسین علوی مقدم، رئیس کمیسیون ورزش و جوانان شورای اسلامی شهر مشهد و عضو هیأت‌مدیره باشگاه استقلال:
🔹
با پیگیری‌های صورت‌گرفته طی دو ماه اخیر، بالاخره مشهد پس از چندین سال وقفه به لیگ برتر والیبال باشگاه‌های کشور بازگشت.
🔹
ورزش خراسان رضوی در سال‌های اخیر رو به افول و نابودی بوده و امسال نیز موقعیت حضور تیم‌های استان در لیگ برتر در حال سوختن بود، اما با پیگیری‌هایی که انجام گرفت، نگذاشتیم این اتفاق رخ دهد.
🔹
از نخستین روزهای حضورم در باشگاه استقلال، دینی به گردن خود برای خدمت به مردم مشهد احساس می‌کردم که به لطف ولی‌نعمت‌مان، با ثبت نهایی تیم والیبال استقلال در مشهد این مهم محقق شد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/akhbarefori/685735" target="_blank">📅 06:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685731">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7489b53543.mp4?token=pzZznHOBHtoy-KYzeDQEDfpbRSZ0KB50fo1atjNED4TpE7mDkw3htTAprPVxjdn2Iy55Bgnvlh5pkvybfUZ61skhn0tRJl_-SjcCfjpBO6_q6oIyE_Ax7ufpJFBG6UxkN07k6mfamWLtnZC2-HMkfC1YadRPwFYzRCfm0526hW6dQ-iT6GXIYiv_x51swwIV6YOryUrNtlNpx1jDaLN9s1LZS9jJQ8B4F0jisrHUqJLcIDxSYiIA-c9Wq6JROYinWKuy6K9dnvJgLfPdkGHqRvRVhFkRUx4tXz3-mGcPMjQ2aFx8z1MrTHsB5hsXp2FP-LzeE6DR3qWBcwEJG1Qn8zX6HCrum54KdNjENsU8HXyxbEYP5aenqM4I1tQmDw5PflADBnxxeaqKyaWEXdizTDXAghNHNZdIPA2CYtRuLgK38bUPvLlLpHDK7tD0yjTX-ga-DqytWOL5cbGQWNfFPv1NWkChiAQnsb3EJlh29tJoRDdb2XaMmk__PovsOABBLz6KgayT1Rhhl9o20QX5vFFxb1UonBywCKrx8gEN-xYePhETKrh9G2Rntg6MS4mYnZfw62Qz5IRiOLcIUA2wDSTGU7gA5UxgbJRL6hMVzw9llEueBBXVCy4ErIJYLoRWdEiy-oNgA_4K-Thw_emR9ORrFGVHBOx1KOdxlmrc-wU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7489b53543.mp4?token=pzZznHOBHtoy-KYzeDQEDfpbRSZ0KB50fo1atjNED4TpE7mDkw3htTAprPVxjdn2Iy55Bgnvlh5pkvybfUZ61skhn0tRJl_-SjcCfjpBO6_q6oIyE_Ax7ufpJFBG6UxkN07k6mfamWLtnZC2-HMkfC1YadRPwFYzRCfm0526hW6dQ-iT6GXIYiv_x51swwIV6YOryUrNtlNpx1jDaLN9s1LZS9jJQ8B4F0jisrHUqJLcIDxSYiIA-c9Wq6JROYinWKuy6K9dnvJgLfPdkGHqRvRVhFkRUx4tXz3-mGcPMjQ2aFx8z1MrTHsB5hsXp2FP-LzeE6DR3qWBcwEJG1Qn8zX6HCrum54KdNjENsU8HXyxbEYP5aenqM4I1tQmDw5PflADBnxxeaqKyaWEXdizTDXAghNHNZdIPA2CYtRuLgK38bUPvLlLpHDK7tD0yjTX-ga-DqytWOL5cbGQWNfFPv1NWkChiAQnsb3EJlh29tJoRDdb2XaMmk__PovsOABBLz6KgayT1Rhhl9o20QX5vFFxb1UonBywCKrx8gEN-xYePhETKrh9G2Rntg6MS4mYnZfw62Qz5IRiOLcIUA2wDSTGU7gA5UxgbJRL6hMVzw9llEueBBXVCy4ErIJYLoRWdEiy-oNgA_4K-Thw_emR9ORrFGVHBOx1KOdxlmrc-wU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار صداوسیما: موشک‌های مورد استفاده در عملیات بامداد امروز از نوع بالستیک سوخت جامد خیبر‌شکن بود.
جزئیات کامل حملات امشب
👇
khabarfoori.com/fa/tiny/news-3241587</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/akhbarefori/685731" target="_blank">📅 03:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685730">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
ادعای اردن درباره رهگیری ۸ موشک
🔹
ارتش اردن در بیانیه‌ای ادعا کرد که ۸ موشک را پس از نفوذ به حریم هوایی این کشور رهگیری کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/akhbarefori/685730" target="_blank">📅 03:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685729">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
رسانه آمریکایی آکسیوس حملات موشکی ایران به پایگاه متجاوزان آمریکایی در اردن را تایید کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/akhbarefori/685729" target="_blank">📅 03:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685728">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuOABiwvBDlqVsY1dX5gxsv6cWjV0mdBnUNgie2zWFMnakaKG7E8hkuY-da4GWYJlP7gIKAuBdXZNe4AON3hvTJKG3yLBrAG-koEasGnCYqdNlbnFZRRhgf1WkPSrSGJQTMUxgRKr8EiZeTqPyT3Rc7XbgwfmpLWn-0V8yKEm0dmbCEbUaRkxlBkKXeaha51hA7HB_oq6ltyXGhtcrgjOXX3d7Mp3DodS-NDzlKX9yJiCEZ3VRhv2w-82DHsDwfek8Xzq5f6iFBuxkuEeUcVqd8v_5_MLaZggCON-luxHVqNhFtnVrx3yh2EoRKgP8JTQkwnp5uVBiwuJNaKTlBxBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هراس مقام سابق آمریکایی از پاسخ ایران به تجاوز این کشور: نیروها را [از منطقه] خارج کنید
جو کنت، رئیس سابق مرکز ملی ضد تروریسم آمریکا:
🔹
ما همین الان اهدافی را در جزیره لارک در ایران هدف قرار دادیم و ایران پاسخ خواهد داد. اگر می‌خواهیم چرخه تشدید تنش را کنترل کنیم و اجازه ندهیم جنگ شدت بیشتری بگیرد، باید نیروهایمان را از منطقه خارج کنیم.
🔹
اگر ایران موفق شود نیروهای آمریکایی را بکشد، دوباره به جنگی کشیده خواهیم شد که این بار ایران شرایط آن را تعیین می‌کند.
🔹
نیروها را خارج کنید. ریسک را کاهش دهید. تمرکز را بر فشار اقتصادی و دیپلماسی بگذارید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/akhbarefori/685728" target="_blank">📅 02:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685727">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLbksmmq48uBw0RutI1lATdKb_CpVxAiABhSzgGoMCpg14qzgHSu2-WhH9bL40NPY2EVWmb746SPijwyanFiEXh81ZuDUF9JVKAQeyNvOpeUDvNQGe0b9WImVJ-5gJiihFj7WsTwnODv1KV8-E1QXP741a0M2Vi5hoEnthFZiPYJEoasP1ti3WESDEKSW8YwpFo7BUtDadmN6Z340NV5SOFdzzKDAtMwa7NvZElpKwFHv_U3OVG6FNdM7yfmN1awYB93EiKW4BmxpfGQ6NEQXRE7Mk1WKi5grDL5MmEXVPlVWFk3_6kpebytgufjwKMYpvdHvFy1Yw6_O9GKJVz28g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موشک‌های ایران؛ آنتی هیستامین برای حساسیت آمریکایی
سفارت ایران در غنا:
🔹
ایالات متحده به ایران حمله کرده است. ایران در حال پاسخ دادن است. تعداد سایت‌های پرتاب موشک از تعداد اهداف آمریکا بیشتر است.
🔹
برای بینندگانی که تازه به ما پیوسته‌اند: نه، این تصاویر آرشیوی نیست. این فقط یک حساسیت آمریکایی است. موشک‌های ما هم آنتی‌هیستامین آن هستند.
🔹
هر وقت لازم باشد، مصرف می‌کنیم؛
و ظاهراً لازم هم می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/akhbarefori/685727" target="_blank">📅 02:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685724">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2778f9c330.mp4?token=rmVAJHVQNwgHkepwFONCqpY7SF3srzS8xHUphXCTWND5A4E71UX-5R16UKCqH-Zpqf6Zx33NQTRP7ok6hdcqfXKx9NI0_5p7Y7Q1TB4UlQAS7h6_oeuTyJxeXb2Mkqj5_peVEuUQ8DMK7y5BbQWZIS_dpACuUU_ealMAUh1-vofRs7-Tbri7srxcTuV_fr6No7y39PiH_tjZzNIL--xrdBmE7LwX_XolDcFK9_5X7RQ-FhbZSgOQpxU7N0vfimghCEYzCAd32nnwDOiLMDKVHAniKrqJSaevnwmvWWMSF-jdsUdTlAOw_iPzF_M8uZqjusR8CCXna8pZ8zQ7hmj_8ELsuMVql39R2Q1thYuEn9orXIELIIVN1qRvhU99-M3gscXhvbc9Y0PtfCz6mgtvuxarlbHNoCOhMVKucWeTpdLG54uLdv16W3zmXc-0F7fL9c0G0qLkVxi37gE8XJMDHQq_xwyUDmi6JgCA26NDW5InjjzNeeBITWs8z6tF9h8oowN6i9n_NROp3Gf6YrZoPetXefyfm5v39OsoJK1tjPjF9eBUWSlPezCC7gYmpwBjTPmoFQyXByHyR7cPKrhxd_yYLujZYN14FSVi8Xd1YWCl-mOJW4Nhx0hHSfV1orY-c_a3ZGDHJUxbVSoancdygWmXXJ7MM23bZYL8kbHosdI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2778f9c330.mp4?token=rmVAJHVQNwgHkepwFONCqpY7SF3srzS8xHUphXCTWND5A4E71UX-5R16UKCqH-Zpqf6Zx33NQTRP7ok6hdcqfXKx9NI0_5p7Y7Q1TB4UlQAS7h6_oeuTyJxeXb2Mkqj5_peVEuUQ8DMK7y5BbQWZIS_dpACuUU_ealMAUh1-vofRs7-Tbri7srxcTuV_fr6No7y39PiH_tjZzNIL--xrdBmE7LwX_XolDcFK9_5X7RQ-FhbZSgOQpxU7N0vfimghCEYzCAd32nnwDOiLMDKVHAniKrqJSaevnwmvWWMSF-jdsUdTlAOw_iPzF_M8uZqjusR8CCXna8pZ8zQ7hmj_8ELsuMVql39R2Q1thYuEn9orXIELIIVN1qRvhU99-M3gscXhvbc9Y0PtfCz6mgtvuxarlbHNoCOhMVKucWeTpdLG54uLdv16W3zmXc-0F7fL9c0G0qLkVxi37gE8XJMDHQq_xwyUDmi6JgCA26NDW5InjjzNeeBITWs8z6tF9h8oowN6i9n_NROp3Gf6YrZoPetXefyfm5v39OsoJK1tjPjF9eBUWSlPezCC7gYmpwBjTPmoFQyXByHyR7cPKrhxd_yYLujZYN14FSVi8Xd1YWCl-mOJW4Nhx0hHSfV1orY-c_a3ZGDHJUxbVSoancdygWmXXJ7MM23bZYL8kbHosdI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر لحظه شلیک موشک‌های عملیات ترکیبی موشکی پهپادی تنبیه متجاوز با رمز یا محمدابن عبدالله(ص) به زیرساخت‌های فنی و تعمیراتی و محل استقرار جنگنده‌های دشمن در دو پایگاه هوایی آمریکایی ملک حسین و الازرق در اردن با شلیک موشک‌های بالستیک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/akhbarefori/685724" target="_blank">📅 02:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685722">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اطلاعیه شماره ۲: زیرساخت‌های فنی و تعمیراتی و محل استقرار جنگنده‌های دشمن در دو پایگاه هوایی آمریکایی ملک حسین و الازرق درهم کوبیده شد
روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
مردم شریف و بپاخاسته ایران اسلامی، صد و هشتاد و سه شب حضور حماسی بی وقفه و تاریخ ساز شما در میدان، دشمن را در بُهت و حیرت فرو برده، امیدبخش مستضعفان و روشنی چشم رزمندگان اسلام است.
🔹
دقایقی پیش رزمندگان غیور نیروی هوافضای سپاه در پاسخ به تجاوز هوایی دشمن آمریکایی - صهیونی به جزیره لارک، در عملیات تنبیه متجاوز در یک عملیات ترکیبی موشکی پهپادی با رمز یا محمدابن عبدالله(ص) به زیرساخت‌های فنی و تعمیراتی و محل استقرار جنگنده‌های دشمن در دو پایگاه هوایی آمریکایی ملک حسین و الازرق در اردن با شلیک موشک‌های بالستیک در هم کوبیدند و خسارات سنگینی به آن وارد کردند.
🔹
سپاه پاسداران اخطار کرد؛ تجاوز و جنایت، استیصال دشمن در تضعیف کنترل جمهوری اسلامی بر تنگه هرمز را چاره نخواهد کرد و هر شلیک با پاسخ‌های کوبنده‌تری جواب داده خواهد شد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/akhbarefori/685722" target="_blank">📅 02:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685720">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa3991a0eb.mp4?token=cGEcmI1dh-THcpTkn3VcfWwwdICWRBniw0w4acB1qcLDeYmjpE4E_ad51Q3I5i1SOTlWmKBfzK4Mp60VRdLjtHcikGvMODxNEtslnme_OeN4LbfnuEBedf1ediT37VVyT5qO-owEcaovI3hsiQGbmxSUJYoIQpJnb_sFOWB8KPmo23z2eyN5GVx-Vi9paw4YIRuto0ok20NvLmZvqFkdGF4UR5Mw7LUpBY8HcMX-sHl7pCge8CIvCeIYVhr_QJxYaOagFKfvTVXHlKpGEd3bzs9uCM9-bMU5FC_vGKQVjv9lPW9SxJ115MfMjLgim1pKYC9CVLgLBiPBCb1VHZq3Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa3991a0eb.mp4?token=cGEcmI1dh-THcpTkn3VcfWwwdICWRBniw0w4acB1qcLDeYmjpE4E_ad51Q3I5i1SOTlWmKBfzK4Mp60VRdLjtHcikGvMODxNEtslnme_OeN4LbfnuEBedf1ediT37VVyT5qO-owEcaovI3hsiQGbmxSUJYoIQpJnb_sFOWB8KPmo23z2eyN5GVx-Vi9paw4YIRuto0ok20NvLmZvqFkdGF4UR5Mw7LUpBY8HcMX-sHl7pCge8CIvCeIYVhr_QJxYaOagFKfvTVXHlKpGEd3bzs9uCM9-bMU5FC_vGKQVjv9lPW9SxJ115MfMjLgim1pKYC9CVLgLBiPBCb1VHZq3Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لانچرهای نیروی دریایی سپاه برای مین‌ ریزی تنگه هرمز این‌گونه‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/akhbarefori/685720" target="_blank">📅 02:19 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685719">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
مبدا حملات آمریکا به لارک کجا بود؟
🔹
داده‌های ناوبری هوایی تایید کرد حملۀ پهپادی آمریکا به لارک، از مبدأ اردن و با پشتیبانی پایگاه‌های این کشور انجام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/akhbarefori/685719" target="_blank">📅 02:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685718">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
برخی منبع از صدور سطح هشدار برای حملات موشکی در امارات خبر دادند
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/akhbarefori/685718" target="_blank">📅 02:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685716">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
مقام آمریکایی: هدف حملات موشکی ایران قرار گرفته‌ایم
🔹
یک مقام آمریکایی به شبکه فاکس نیوز گفت: هدف حملات موشکی از جانب ایران قرار گرفته‌ایم.
🔹
او در ادامه سیاست کتمان و سانسور، مدعی شد که «خسارت زیادی در پی حملات ایران به نیروهایمان وارد نشده و تمامی موشک‌ها ره‌گیری شده‌اند».
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/akhbarefori/685716" target="_blank">📅 02:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685713">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da9fa755cb.mp4?token=Mk5FFnr28PFMND-2NGtbZYlw7-AwCHlT_um-qEchodt8M3qzRirMGZk9d-C-Sr_H1rj8PNOTEIhKO0tYLOzHb_M7H37MOR09uA7DB5XcnUlRa9Wc85W3U1OHSsT8IQeCUPRduaxT3bOv42ZWo_q__lExdRATFHp-CXWS4Lv5fXLLJGcx_9HiqMWpe8fEg_m3LBPy5Bs6nS6CJpwLflJIJ1dtt3R_oAuH7oq_rg3f4yWK8gBzAfxGf8k4O99WFnCIDjcuQoHoUefhIqklcRITDGNyxOz3SMZVyeW3AtSaxtTsegQ1WdIxznWgcPH62xPWecTk6WME1J_bUzRf_r6oXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da9fa755cb.mp4?token=Mk5FFnr28PFMND-2NGtbZYlw7-AwCHlT_um-qEchodt8M3qzRirMGZk9d-C-Sr_H1rj8PNOTEIhKO0tYLOzHb_M7H37MOR09uA7DB5XcnUlRa9Wc85W3U1OHSsT8IQeCUPRduaxT3bOv42ZWo_q__lExdRATFHp-CXWS4Lv5fXLLJGcx_9HiqMWpe8fEg_m3LBPy5Bs6nS6CJpwLflJIJ1dtt3R_oAuH7oq_rg3f4yWK8gBzAfxGf8k4O99WFnCIDjcuQoHoUefhIqklcRITDGNyxOz3SMZVyeW3AtSaxtTsegQ1WdIxznWgcPH62xPWecTk6WME1J_bUzRf_r6oXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موشک‌های ایرانی در مسیر در هم کوبیدن پایگا‌ه‌های آمریکا در منطقه هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/akhbarefori/685713" target="_blank">📅 01:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685712">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e60316bfc.mp4?token=G5f2IRSefjZ6mVj6ueqwjDidHynSZzBKDVoA_C38E_6ur2SyNlkfYeRatc_6-u4rRxr8HJTOGv4JjFQe1DHkOPau7VhnuAI5nvnvMMgfqUkZ8T1Bu--Rd_zCtEd8uW-pcsQkxieQ3qGGG4amfGBz5NJIbtjQ9YBELLlhxkJtZXkbaUM1xYWWT2wUYCTu6r5AHs-4c3BjRWIBqzoKvzWSX7bElfqSITM3p0hdzowgARGqxMV4ZDBr9uxrKMmZoEp6mlDr45sKqKwvZrGr3d-XzV27K_suNRm876t2UeVBrbp7KWD3bGsW6xq7hixXsvMgmp0V3iHRZrTvoxeHjmXZn1CiXTQkzGERAZhT8OTTUJML0uOgwYAy_xRSdPWCscWUYy-53NQyauMMzuJaS0yUgp6gFf7N2Ht28s5yhdj818aP8ZSdtba9g0NciDJX-MHSi6Som3jiptEoB9nLFz5qq-WMYPjgcOQg1rDkv5Jgxq56vpWTUa5fKMKSRNxVSI5CzXE9VZgVIaxYSjdRyE2_wv6CUFc3cRbeZr7FjhgsFOloOb9U20BHFIHMBuXzFka3320LEKnkp3oEfO0U42Ym_5WUmSxd096or8ZdIHwkUM1Smo6Ox8HGzhU91X3WOmLsYjMA2IZh33-4VB215ed31O-QwVGfrfDrzAYOdTf-gHE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e60316bfc.mp4?token=G5f2IRSefjZ6mVj6ueqwjDidHynSZzBKDVoA_C38E_6ur2SyNlkfYeRatc_6-u4rRxr8HJTOGv4JjFQe1DHkOPau7VhnuAI5nvnvMMgfqUkZ8T1Bu--Rd_zCtEd8uW-pcsQkxieQ3qGGG4amfGBz5NJIbtjQ9YBELLlhxkJtZXkbaUM1xYWWT2wUYCTu6r5AHs-4c3BjRWIBqzoKvzWSX7bElfqSITM3p0hdzowgARGqxMV4ZDBr9uxrKMmZoEp6mlDr45sKqKwvZrGr3d-XzV27K_suNRm876t2UeVBrbp7KWD3bGsW6xq7hixXsvMgmp0V3iHRZrTvoxeHjmXZn1CiXTQkzGERAZhT8OTTUJML0uOgwYAy_xRSdPWCscWUYy-53NQyauMMzuJaS0yUgp6gFf7N2Ht28s5yhdj818aP8ZSdtba9g0NciDJX-MHSi6Som3jiptEoB9nLFz5qq-WMYPjgcOQg1rDkv5Jgxq56vpWTUa5fKMKSRNxVSI5CzXE9VZgVIaxYSjdRyE2_wv6CUFc3cRbeZr7FjhgsFOloOb9U20BHFIHMBuXzFka3320LEKnkp3oEfO0U42Ym_5WUmSxd096or8ZdIHwkUM1Smo6Ox8HGzhU91X3WOmLsYjMA2IZh33-4VB215ed31O-QwVGfrfDrzAYOdTf-gHE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کویت، مشعل‌های چاه‌های نفت را خاموش کرده و به منظور جلوگیری از هدف قرار گرفتن و در واکنش به احتمال تلافی ایران، اقدام به کاهش روشنایی‌ها کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/akhbarefori/685712" target="_blank">📅 01:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685711">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
اخبار غیر رسمی از انفجار در پایگاه العدید قطر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/akhbarefori/685711" target="_blank">📅 01:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685710">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYRIJm1aA2eI13t9YoIZgVFhdJUb-sTzUU4wOvENMBLnVXoS2KzyatHHafDo1BaXX7vPSDXC60UNZGKg3hkKH0ztiWTVbT6Oc3OimG9GEav54Ln0pNgG_1c5KBgW7ouYeTwJMyJNMJpIkGdvD8Rzs5zBVNqA_81H5utLC9RZxflUGPl1_NMKVzdh0-pTE4XI5SmtEOO69T9j23ACfRfOhGdnh8z2yQ84qmdyqTXpyblPaQvKSfSSYIhn1h8eXTes92FcFE-GC-rsQBfm_pztTPuxbrRDsxgLY9O6KRQYwWIYMFWPt6B6Qlhdmh2VCEMmklL97pV5BkgpvlADhYRChA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش قیمت نفت در پی حمله آمریکا و پاسخ ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/akhbarefori/685710" target="_blank">📅 01:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685709">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPHSPid7vO0yZxPI2U8zPwjyz6vPzjoq_vHIb1z-hS1K20CQCfGOqpHiAO9hcj3zkfLvMHLAVWzVny5vaCqEyEyPqHvCK8EAJ6aCTlgSV1so7HjxxrEVqGSscjuD2nUR-AYV8cUplbg9kO5MloPCQuKldqN765qQGzBM2rfJ8HCt4WRYqPFm-PyjVCQa12xd19JWo_tonXNiPjw4KcpxKIGA14NdlHRJ-0XlUOrXWW6akW22dxYbpfNC8JBZZDBXpW44LjlkDYKzOQlAtkrIATKefVuTlJYRQNCMqu1i29DqiPrjdzp_uArUBn8fSUAy5qFWrebV3TZ_emJQfkQN9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زیرنویس شبکه خبر: مشاهده موشک های شلیک شده از مناطق مختلف کشور به سمت اهدافی در منطقه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/akhbarefori/685709" target="_blank">📅 01:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685706">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f04fa470bb.mp4?token=gwB_jOF38hCnAXGG60kIyIsAQKfWlizVdBUXjYkS2NS7RKeJM6H8-Gs-ux-vOB8xAq50qJWaqiwVclukTZygTC587J8bDLm9jOWYPv5O7GSRlZyzxmicM7Qeov8sFAMoQbF-rE_X7c1zgCSL6biVw1KUmgOj16zrmgTBp0NMzreCRZld4_kCSRdt2ixM_OYekej6d5ngVfDmiOkhllZDyiD2VP5nKUf3zPNAQMbqtoAdkA_zKoC6_o5L25k1Lan6VqePwViXbmLJ9tdXdaR1xEd8n_QbKyMVN8Vrc5B0QKP0T8KLk-kUoyBRLEXZW4G-WLkVynW8OdEwB7-oXrBKiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f04fa470bb.mp4?token=gwB_jOF38hCnAXGG60kIyIsAQKfWlizVdBUXjYkS2NS7RKeJM6H8-Gs-ux-vOB8xAq50qJWaqiwVclukTZygTC587J8bDLm9jOWYPv5O7GSRlZyzxmicM7Qeov8sFAMoQbF-rE_X7c1zgCSL6biVw1KUmgOj16zrmgTBp0NMzreCRZld4_kCSRdt2ixM_OYekej6d5ngVfDmiOkhllZDyiD2VP5nKUf3zPNAQMbqtoAdkA_zKoC6_o5L25k1Lan6VqePwViXbmLJ9tdXdaR1xEd8n_QbKyMVN8Vrc5B0QKP0T8KLk-kUoyBRLEXZW4G-WLkVynW8OdEwB7-oXrBKiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم اکنون| آسمان اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/akhbarefori/685706" target="_blank">📅 01:39 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685705">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
تحریم‌های خصمانه آمریکا علیه یک بانک دیگر ایران
وزیر خزانه‌داری آمریکا مدعی شد:
🔹
ما این هفته به عنوان بخشی از تلاش‌ها برای تشدید فشار بر ایران، تحریم‌هایی را علیه یک بانک دیگر اعمال خواهیم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/685705" target="_blank">📅 01:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685702">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQ-tVdc0N3GTK0EEfb8NlMRAyaq8dWcEr-4iFXg9qUyy9sWkgu74m_0ZVDpBq7eyLwIYWlwoFlFBnHNQpr6tCyToy5_14XIXk9-I62gYsx_pUlCwr5E6Pm1cv4UWSYPb8c7jmS2oM5Lkaz6uyWij-RjHvfmFOZ8ebKVWQff0SgtpF2I8FCbFyPaP8yxfw5Tka6R_wpi31K4UCp8CxOmJYOST4jThvYHq9nPpMPc4JlTsr-kR9qD8kFaJoZq54aBVpj-tA6INWa6cS8tPbf6Py5extp9XmEjU4rWTQ7WcWymFeh5OF-6cPV2_jAwkUbyFbHoWe59wM0qPgvToObo5GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرار سوخت‌رسان‌های آمریکایی از ترس ایران
🔹
پس از اعلام ایران مبنی بر پاسخ به حملۀ آمریکا به لارک، سوخت‌رسان‌های پارک شده در پایگاه‌های آمریکایی کشورهای حاشیۀ خلیج‌فارس، در حال دورشدن رصد شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/akhbarefori/685702" target="_blank">📅 01:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685701">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueLmd_CvWxxHczD79Wwvwe-8m5HsKGciVXatvuRpXTPpGng1y4qFZr7ZGwQ9GTfdBZ_KoIovILj-2kG4eB3RpQ7OhSSSoeduRWUDWQVnSNJrfX1Ewk_1z7eUqXwE-fbSSuft0zXo26TAFm0ICdinJOdcN_2jw5ix4MjHwilVEDBTYxCt1tWfA9ZwE77HruhXVxJ4BfyFENLD2LR0-YUioZim301jaSm2lp_iReJV6jVfT3kP9imPZUcnprSwBn39KwRtu1zSXI3NPs1dhSQzkfeCmFpavN7MRUHDE7bSSSij36Na_d0NOu8_ZfoNswe8n5fKUZbQfQYIvtKjEG0SZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۱.۵درصدی قیمت نفت/اوپن نفت برنت ۸۹ دلار
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/akhbarefori/685701" target="_blank">📅 01:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685699">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
سنتکام: محاصره دریایی ایران ادامه خواهد یافت
🔹
فرماندهی مرکزی ارتش تروریستی آمریکا اعلام کرد که به محاصره دریایی ایران ادامه خواهد داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/akhbarefori/685699" target="_blank">📅 01:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685697">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/217965451b.mp4?token=g3-v3Nr4u4u9hDQgSJVLoNsufpwkCJQZ1Os0Lh3fZ1valZbnJM8jYIUlOWC1mdVtbg_NdzI5k9mrlC1Wwgj37y5KBa8jcJAF5HVAoV5LveiCkCGIW4s8tLLCZezxvuy2C1pKMiAVpai5GLc3gTmsuzjDW2Ok0mRQ9PXjLvNvShr67ahpRK5dlXgFmyqymQjuG74_qbzQose5PLK_hHOOy6f1-9PMPgqvWTgdhpGYPlIczanze29luBLB96Wk7sr8walNgr2Fq100ld7L1bJANqzTX9GGz4ZSPkfqszOgOrukRXYoOqWpGEy_9BMfAKlF5BTNtnss5NkWBmf0HA2foQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/217965451b.mp4?token=g3-v3Nr4u4u9hDQgSJVLoNsufpwkCJQZ1Os0Lh3fZ1valZbnJM8jYIUlOWC1mdVtbg_NdzI5k9mrlC1Wwgj37y5KBa8jcJAF5HVAoV5LveiCkCGIW4s8tLLCZezxvuy2C1pKMiAVpai5GLc3gTmsuzjDW2Ok0mRQ9PXjLvNvShr67ahpRK5dlXgFmyqymQjuG74_qbzQose5PLK_hHOOy6f1-9PMPgqvWTgdhpGYPlIczanze29luBLB96Wk7sr8walNgr2Fq100ld7L1bJANqzTX9GGz4ZSPkfqszOgOrukRXYoOqWpGEy_9BMfAKlF5BTNtnss5NkWBmf0HA2foQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آسمان اردن و تلاش پدافند آمریکایی برای مقابله با موشک‌های ایرانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/akhbarefori/685697" target="_blank">📅 01:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685696">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41d2eafbec.mp4?token=D-Mc6FdKwBshv8tXhf8tJA1dIf2v3x1GmgPQbJJeIi1WfXaKeqgroVfTZgngl3Cud_QPjzhR5IgazsyMBZRK8PH4rMLJL3rtmYW3mN63X8g0-3OrsMundOfPAiNp_16FwdWot_NO8A4YYTnGQmZcLLvSa1taI3wrPavvbYRySRjYCFF2xJ1tQjbzWA_svx7YSihARjAXo83b3MOd0K4cezT-Y8UYEo213rdp319jTTGMnSwWmrPKq3-aAtgWPFcXpSSo1_MXHaNCrczpMTjcMV-tbh-rDtB07lubRx9FcGFts6quOCBUXdQxHMV6atTcIF6exqzZr6tVd6TvEedq0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41d2eafbec.mp4?token=D-Mc6FdKwBshv8tXhf8tJA1dIf2v3x1GmgPQbJJeIi1WfXaKeqgroVfTZgngl3Cud_QPjzhR5IgazsyMBZRK8PH4rMLJL3rtmYW3mN63X8g0-3OrsMundOfPAiNp_16FwdWot_NO8A4YYTnGQmZcLLvSa1taI3wrPavvbYRySRjYCFF2xJ1tQjbzWA_svx7YSihARjAXo83b3MOd0K4cezT-Y8UYEo213rdp319jTTGMnSwWmrPKq3-aAtgWPFcXpSSo1_MXHaNCrczpMTjcMV-tbh-rDtB07lubRx9FcGFts6quOCBUXdQxHMV6atTcIF6exqzZr6tVd6TvEedq0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه شلیک به سمت پایگاه آمریکا در اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/akhbarefori/685696" target="_blank">📅 01:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685694">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f10d866a7.mp4?token=QY1nYa4qbz1kko7a4NnCO_jyIgGI7kGvvpEKZntJN553VvsObyHlSrLHk8n_Gb4EDieg-9MOLM_zuJwUFsf3vftvpajvIX23uFz5lfv194kRGyGK52W9ua_9ZaV2dp7Dl0bCXUwt_9Sbd7Ky0m5tNpEe67aExHXA9b3cLx6hwyeUBYqdZEUOKirNOCXUyLgbqV2Mwe-cJkSypzOZXv1h5XLe9wPARzJlb0AP1NMZdkB89sSgAb2SqwC4rYW4jeUbMtM0ncFQm_jB4vYOmrNOjnSOzoCZFqow40Hb15iOjSbVEMYRtCHnW7_VHkBtc9eFVYoHG5q0QTJkS70vUIZw1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f10d866a7.mp4?token=QY1nYa4qbz1kko7a4NnCO_jyIgGI7kGvvpEKZntJN553VvsObyHlSrLHk8n_Gb4EDieg-9MOLM_zuJwUFsf3vftvpajvIX23uFz5lfv194kRGyGK52W9ua_9ZaV2dp7Dl0bCXUwt_9Sbd7Ky0m5tNpEe67aExHXA9b3cLx6hwyeUBYqdZEUOKirNOCXUyLgbqV2Mwe-cJkSypzOZXv1h5XLe9wPARzJlb0AP1NMZdkB89sSgAb2SqwC4rYW4jeUbMtM0ncFQm_jB4vYOmrNOjnSOzoCZFqow40Hb15iOjSbVEMYRtCHnW7_VHkBtc9eFVYoHG5q0QTJkS70vUIZw1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موشک‌های ایرانی به سمت پایگاه هوایی موفق السلطانی متعلق به آمریکا در اردن شلیک شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/akhbarefori/685694" target="_blank">📅 01:19 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685693">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خبرنگار صداوسیما: حمله به لارک در ۲ نوبت نزدیک به هم صورت گرفته است
🔹
حدود ۴۰ دقیقه پیش صداهایی در سیریک شنیده شده که مربوط به دفاع ما از مسیر ایرانی بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/akhbarefori/685693" target="_blank">📅 01:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685692">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/871be82be9.mp4?token=IjnsNdqlAPax2tgQBKCddLFhzEHbvVve3pI2tIYmiwEwN6ZnIuUkeNVRoEvvTBmqa_eMhmnkKV-q9tmZlwccLqW5BXKGafTL7V-wkMJ7y5jC_ayoaAA9xQhYYshRgxVic2KOiu8A5gHd7ZthzPxK_yCyr_xR2BpyzRIzz6bbU78M4UDxDQ2xPY7XI8cOBiL4yFuaylr_Y62P6D-nYnWhy3HhEfNLUolUoSUTtCa8FNEEIiVS2vZpeeIpN3iWshKkFK6M1pWD_JgtBN0Bb14CM8PRwnDDhn6t3pzE9ke5QCb7rM5v9ZTnCMOZHwhqqb9yTf3y_qPkZeDfSB1FNCiGQ4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/871be82be9.mp4?token=IjnsNdqlAPax2tgQBKCddLFhzEHbvVve3pI2tIYmiwEwN6ZnIuUkeNVRoEvvTBmqa_eMhmnkKV-q9tmZlwccLqW5BXKGafTL7V-wkMJ7y5jC_ayoaAA9xQhYYshRgxVic2KOiu8A5gHd7ZthzPxK_yCyr_xR2BpyzRIzz6bbU78M4UDxDQ2xPY7XI8cOBiL4yFuaylr_Y62P6D-nYnWhy3HhEfNLUolUoSUTtCa8FNEEIiVS2vZpeeIpN3iWshKkFK6M1pWD_JgtBN0Bb14CM8PRwnDDhn6t3pzE9ke5QCb7rM5v9ZTnCMOZHwhqqb9yTf3y_qPkZeDfSB1FNCiGQ4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش‌های تاییدنشده از شنیده شدن صدای انفجار در اردن
🔹
برخی منابع صهیونیستی گزارش داده‌اند صدای انفجار در اردن شنیده شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/akhbarefori/685692" target="_blank">📅 01:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685691">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گزارش‌های تاییدنشده از شنیده شدن صدای انفجار در اردن
🔹
برخی منابع صهیونیستی گزارش داده‌اند صدای انفجار در اردن شنیده شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/akhbarefori/685691" target="_blank">📅 01:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685688">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nsXyCNhouWCZ3LGb_oEF5s8t_y8ZbrGWN6HbaFfRrGOuPaGRc6GP50DWtXRjOqgVU0h-DJephChlY-4FpsfFDUTPG3bv8MWGlTyImXP2TPIsVLBRsSJHK3RV2OGA2dfSH-Kw1QAHurKV43aNwKVGde8dMfGyN7Xpb5_eRfyvtQbW7al1IIs6ZWnJFM12jnjkeFigjVAAIruZDffcvRDpgYhvmmW02IJSyhyDiyTvaWfqr6FwgloeDYfLQAXENjc5LGAmMNm7N-O6nc_R_WjZcQttdOEygXyoz6LYMkmNLpZzJytRcv0Rma6zCC7JuZ7BnNGyxHz3LiLcaJSXDXiDwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c6oaylQs5du2-E1RM8G6PT1s5TsFIMMC2h0-g3aWlJ7Ukk5Fs_orXynZ8TFSh4pYJfoKou09lkT-i8uUCzj3lxGJvSsiT6frjPIc9L0DXOyjvlrAAi52jBOMXH9EkV6pJDcQQP0XIaLHdqEsbsyN_4KbjVoqDvOhV1zzUsmKzajRHIH0SC40sCg0GJtisJEb0KjYwrI_Rhqap5vICjwl-7h7giOirEMkZ22ZMmXaasTtt2V0jU3-gD_WVLZoGA73UiUUEXYTAhi22hpgObBIyyeX_Zd6ZqrqqFWyEokpqGmFBQrMk02tieTpB2o3sfo3vvAHhsqYRy3cRAljKHck0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امشب| تصاویر شلیک  موشک به سمت اهداف دشمن آمریکایی
@AkhbareFori</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/akhbarefori/685688" target="_blank">📅 01:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685686">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
انفجار در اردن
🔹
منابع عربی از انفحارهای متعدد در منطقه العقبه واقع در جنوب اردن خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/akhbarefori/685686" target="_blank">📅 01:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685685">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
ادعای
سنتکام: از زمان ازسرگیری محاصره دریایی علیه ایران، مسیر ۸۳ کشتی را تغییر دادیم، ۳ کشتی را از کار انداختیم و ۲ کشتی را بازرسی کردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/akhbarefori/685685" target="_blank">📅 00:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685684">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏
♦️
گزارش‌هایی از برخی منابع، شلیک موشک از خاک ایران
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/akhbarefori/685684" target="_blank">📅 00:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685683">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
تکذیب تعطیلی موقت فرودگاه مهرآباد در پی حمله آمریکا به لارک
🔹
در پی انتشار اخباری در برخی رسانه‌ها مبنی بر تعطیلی موقت فرودگاه بین‌المللی مهرآباد تهران پس از حمله امشب آمریکا به جزیره لارک، سخنگوی سازمان هواپیمایی کشوری این ادعا را رد کرد.
اخوان، سخنگوی سازمان هواپیمایی کشوری:
🔹
شرایط پروازی در کشور عادی است و فعالیت فرودگاه بین‌المللی مهرآباد تهران نیز بدون توقف ادامه دارد.
🔹
پروازها و فعالیت‌های فرودگاهی در کشور در شرایط عادی در حال انجام است/شهرآرا
@AkhbareFori</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/akhbarefori/685683" target="_blank">📅 00:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685682">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzDgHG8STUDSVpwWrcGIF0e2e_xMiitKhvjMkIf5vQYPNigOOrq8XvEBGdaT5wIaxWMb5Tlt37NDis8Eko4Z7P2w_Ew9PP7NurMMTl8rMtBRd83zrG9QUeg-MANWMk0WBQ-gJgk0cg8Zojedx4ZGYgEIBXsr1XlKDlYVXb6rN5A-gG4YnNHWTkq5WEhU6uYWyyn-Z8goGn7p4LdNOAg4ct5k9dmDYOUlOgMD3dNymuJaLwKnieeTwnjBklYdcfIkXe0GNk0N1SstT4l-YgFlNognuzHgQVZ87P-AF5eV1r1ZFJua6WcMJU8AEuErB-2HAnGahALU0UEBUESThwF4_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست جدید ترامپ در تروث سوشال
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/akhbarefori/685682" target="_blank">📅 00:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685681">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kn91uhpSZxenvibnhS8pfTh0Dh5PURu62NZo7VZmR_6HqyphV7LaFJguGIwFOu77IBo3Wf5Uqyq-U7HbpDBN-qaL7hddGDFXH8XTei9rMUROjSvMZz0COQeLSt00O61AG3gN4dPtP2LTerLzakoXKxpYniC53_N16gi1sP18qj3Mgh1hNU4Iy8z0OSBN0cfqHvKGBqJ25UTmd3MuhVIpJd9ZVoxRpSfdGT73UesTNnWP_aHKhpS1GC8LwQF2fSkCTzkzfCHn2bRVBi_eEADFNsdfYkspOnsfR5d36cv36lW8Q_kyzb6M46X26Jv8Yh8k39_59gWvbBha7hftohjZFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی: آزمودن مجدد ارادۀ ما، تنها هزینۀ شکست‌های خفت‌بارتان را سنگین‌تر می‌کند
🔹
بی‌تردید هیچ جنایتی، در هیچ سطحی بی‌پاسخ نمی‌ماند؛ پاسخی ویرانگر، دردناک‌تر و عبرت‌آموز که سلسله شکست‌هایتان را کامل خواهد کرد.
🔹
با ترس و وحشت منتظر باشید
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/akhbarefori/685681" target="_blank">📅 00:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685680">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df8fa03f85.mp4?token=l4RqQj3irK0AXQiCYTT6RuTz-wWwLRRcSk6aoAVCP2mxTDTVIgR45BYKmCODW9tx9rlJiL-kNj8iufac4kbgQ9iJMN-aPsQlmQycxj04uOxsq10C0a4wNmcpUHa7xUD_pN36zf9Z5aeOIBcavlfEp8z_dmvXmZH89Qxb2pwSxU_1GcHdTxNjz3EDyFnprs4uNOTz_fUneWArhcBCARCySHY43A9AwQoohRq9mWR4TH9N7VM9KsyT17yOxLsuE0hzj2vYzudusSh1_vmOnDPgfCTorZ_WFDmGvJJ_UTq-EimRmHEyrCu5hXPFzw7b5LE0J6GliTjKulN48qOFBzk2JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df8fa03f85.mp4?token=l4RqQj3irK0AXQiCYTT6RuTz-wWwLRRcSk6aoAVCP2mxTDTVIgR45BYKmCODW9tx9rlJiL-kNj8iufac4kbgQ9iJMN-aPsQlmQycxj04uOxsq10C0a4wNmcpUHa7xUD_pN36zf9Z5aeOIBcavlfEp8z_dmvXmZH89Qxb2pwSxU_1GcHdTxNjz3EDyFnprs4uNOTz_fUneWArhcBCARCySHY43A9AwQoohRq9mWR4TH9N7VM9KsyT17yOxLsuE0hzj2vYzudusSh1_vmOnDPgfCTorZ_WFDmGvJJ_UTq-EimRmHEyrCu5hXPFzw7b5LE0J6GliTjKulN48qOFBzk2JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو کودک کش: آنها از برنامه هسته‌ای دست نکشیده‌اند؛ ما آن را به عقب راندیم، اما آنها کاملا قصد دارند برنامه هسته‌ای خود را برای تولید بمب اتم از سر بگیرند
🔹
بنابراین تهدید از بین نرفته است. ما این سرطان، این غده سرطانی را ریشه‌کن کردیم. می‌دانید که…</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/akhbarefori/685680" target="_blank">📅 00:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685679">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
به گفته برخی منابع از شنیده شدن صدای انفجار دوباره در جزیره لارک  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/akhbarefori/685679" target="_blank">📅 00:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685677">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
نتانیاهو کودک کش: آنها از برنامه هسته‌ای دست نکشیده‌اند؛ ما آن را به عقب راندیم، اما آنها کاملا قصد دارند برنامه هسته‌ای خود را برای تولید بمب اتم از سر بگیرند
🔹
بنابراین تهدید از بین نرفته است. ما این سرطان، این غده سرطانی را ریشه‌کن کردیم. می‌دانید که اگر سرطان را ریشه‌کن نکنید، می‌میرید. این کاری است که ما انجام دادیم.
🔹
اما سرطان همچنین می‌تواند متاستاز داشته باشد و اگر متاستاز وجود داشته باشد، می‌تواند دوباره به یک تهدید جدید و بسیار واقعی تبدیل شود.
🔹
ایران می‌خواهد برنامه هسته‌ای خود را از سر بگیرد. و من این را می‌گویم - من قبلا یک بار مانع انجام این کار توسط آنها شدم و تا زمانی که نخست وزیر هستم، مانع انجام این کار توسط آنها خواهم شد.
#Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/akhbarefori/685677" target="_blank">📅 00:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685676">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
به
گفته برخی منابع از شنیده شدن صدای انفجار دوباره در جزیره لارک
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/akhbarefori/685676" target="_blank">📅 00:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685675">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ushf9tJZyDENJqvyRd49T7GpqBH4QNs93MZ-g4lRm7SamYYlSzteIwnoTo8Mk2QuK8_WfwjqvPeegBX5fiL2TklHEPHTRemNujCGKog4MHUNzNtbYmqfB5a5KwaeVUR6suo5McT_V_xt8NjaE8SV_6EvPo9G52MdfNfnvde7UVLlKhULxbw1n_EBJBNobnwUNU4_NbxSnAuMP2wS5Q96TMAvz4Q8QKh7ZsknFeSj8kCEbFBGvASHbWdFjFvWOWIKT5iqa-ESEX5UGuR0CNLCXVDrnq07JHq8CPDCL78gVnb1JNi-Bbbp-PtS3xowJA5kJpZPdHdpz1BChYwYcyknSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تجاوز دشمن تروریست با تنبیه متجاوز همراه است  سخنگوی سپاه پاسداران انقلاب اسلامی در ایکس نوشت:
🔹
تجاوز دشمن تروریست در جزیره لارک همراه با تنبیه متجاوز پاسخ داده خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/akhbarefori/685675" target="_blank">📅 00:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685674">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ld6iHbWwmkFz3a4ycmESesS912z1jSj84a6wfk-nvyzSfxhN0BNB8V70rzR0laQeheF7tutSRBxQXpwpTV7nRTVuSnYSDvaxo1jKwuSxU6W-SNGvNcpectwT1x-6vj466tpQbSmeJTH9Pb9DvIehq-aN_NkCl_lJ5K3nLEtm6kicOx0ur15obWmfCaiJd6d3NGs_xjU6Dh9iXUUu1uY_ZOriEf7VKNIK3g_UMF5hJumZW7wWlm9mtHZItbnex_0HSOBWq3uxyzF2uZAkLDuDzFlsNRkEaimjYL4UcaqrYpbWfObwePE25lmYntAlCs4yW8HYu36N9omD_4msV9eBNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/685674" target="_blank">📅 00:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685673">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xd8AcCtgVQ5diEgR0ouYEsZt5oMtu1QVYFwpHuSzUfL2SjY9u7aNaxjnYOwU-IzbQvJ-u7unj38EmpnIJOiwirCOc6O1JIOirJg72Ayh6xF9jsbtv_Ka-KbWFoQrJJ4UzWQ_0pqhm9ZjkJJYBI5kARr6sxCtgjEf1d5H_LZQoSm8JmUnwMJbkjRZR8aErj1tpI660wZgW9ff5eseuJ-2is_V_e_SfruYTaDUhixcntYn6RH3XuINDqFE856MfVu2SOayYmdSs2gq91Fc280bBuFzR7w1yxYPi3x7avbdUnxxiZvvEkRm1qZK_G4nfIVXQ57_g9xbJqxhlL6bdrCi_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سپاه: تجاوز دشمن تروریست در جزیره لارک همراه با تنبیه متجاوز پاسخ داده خواهد شد
🔹
روابط عمومی سپاه پاسداران انقلاب اسلامی:  بسم الله الرحمن الرحیم  انا من المجرمین منتقمون
🔹
دشمن آمریکایی - صهیونی بار دیگر بر مبنای استیصال خود در حل مشکلات داخلی و کاهش اعتبارش…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/akhbarefori/685673" target="_blank">📅 00:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685672">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
برخی منابع خبر شلیک موشک، از نواحی مرکزی ایران را دادند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/akhbarefori/685672" target="_blank">📅 23:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685671">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ادعای
کانال ۱۳ عبری: رژیم صهیونیستی برای سرنگونی جمهوری اسلامی ایران هزاران جدایی‌طلب را آموزش داده است
🔹
رژیم صهیونیستی به عنوان بخشی از تلاش خود برای سرنگونی جمهوری اسلامی ایران هزاران کرد جدایی‌طلب را به سرزمین‌های اشغالی برده و آموزش داده بوده است.
🔹
این رسانه مدعی شده سه روز پس از آغاز جنگ رمضان علیه ایران، پیامی از آمریکا به صهیونیست‌ها می‌رسد که طرح اجرا نشود.
جزئیات بیشتر
👇
khabarfoori.com/fa/tiny/news-3241556</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/akhbarefori/685671" target="_blank">📅 23:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685670">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
ادعای
آکسیوس: ارتش آمریکا در خاورمیانه به حالت آماده باش درآمده است و برای پاسخ ایران آماده شده است
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/akhbarefori/685670" target="_blank">📅 23:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685669">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
حمله آمریکا به جزیره لارک / ۲ موشک‌انداز سپاه هدف قرار گرفت
👇
khabarfoori.com/fa/tiny/news-3241579
🔹
درگذشت ناگهانی یک سخنران در تجمع شبانه/ ویدئو
👇
khabarfoori.com/fa/tiny/news-3241569
🔹
ماجرای مرموز فرار پسر نتانیاهو از آمریکا/ چه کسی دنبال ترور «یائیر نتانیاهو» است؟
👇
khabarfoori.com/fa/tiny/news-3241559
🔹
ماجرای اتهام جنسی به محسن نامجو چه بود؟ | شاکیان او چه کسانی بودند؟
👇
khabarfoori.com/fa/tiny/news-3241480
🔹
رونالدینیو: همه جام ها را بردم، اما یک حسرت هرگز رهایم نکرد
👇
khabarfoori.com/fa/tiny/news-3241450
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/akhbarefori/685669" target="_blank">📅 23:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685667">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4949575f84.mp4?token=Quf1KU87zCLftsgSi6ulQrYcYZgO6NplpJ-nP2iCtrvP5TuvDR2H-yJLn4hytVRVJzrtNERGrhdbDO3FUcflpz6noXi77d3Cua3OpN9_PNysYKyBE1MApB-N33I36Sv1qSbfE13z5aAew8XjR3vqJEcDYP9PL1oy6nFnQO2eRnE6F0fhVe67bILqytdXZHMLFapzRQhkQ-q_avvpHz3EHwOvqsePgb7keZ-xBsryd7D7xyhfYi-mzPXFn7kc6czVuzSbZpfoyfimcHcpl_xfbf-Nu2JUwQl2f6b9DAEYujdZ8QG-GyE1u_9ZrQ18vc_trW4T_MPniZvJ4c_V1s_dXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4949575f84.mp4?token=Quf1KU87zCLftsgSi6ulQrYcYZgO6NplpJ-nP2iCtrvP5TuvDR2H-yJLn4hytVRVJzrtNERGrhdbDO3FUcflpz6noXi77d3Cua3OpN9_PNysYKyBE1MApB-N33I36Sv1qSbfE13z5aAew8XjR3vqJEcDYP9PL1oy6nFnQO2eRnE6F0fhVe67bILqytdXZHMLFapzRQhkQ-q_avvpHz3EHwOvqsePgb7keZ-xBsryd7D7xyhfYi-mzPXFn7kc6czVuzSbZpfoyfimcHcpl_xfbf-Nu2JUwQl2f6b9DAEYujdZ8QG-GyE1u_9ZrQ18vc_trW4T_MPniZvJ4c_V1s_dXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امکان ضربۀ مستقیم به اقتصاد آمریکا و لزوم دریافت غرامت از کشورهایی که مبدأ حمله به ایران بودند از زبان کارشناس مسائل منطقه‌ای
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/akhbarefori/685667" target="_blank">📅 23:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685666">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYtsxx9R3Swp5Jl56fLGxP5aGGB7IAjWwPDyd9yjF8qG71Ep-wfJUAOInlBqi1YxlN9o1EJaecGhxcL8OdfriH8zCnieK2velFDRH_AiIvZicWvSvqN-HuMHUgpuyFM9abs-Sp1erWaqpXbPuIpqbiwY67FONFWV_sprGQE6Jr66oZzOdt4SOPp4uxN9g_eWwkVG7x90XpZZkGmfmtXeUASwp1QzYQkdJQjQRWXdQ6XDVvlXOc-wuk3P6Z2_QYgulhpK1AVG4rYguXTySl7wTx6e1hLxl12s8jnYNZga8EpetUTA5lpunlrtYTmxQfHumI-RlvCcawVddfFvd_wIOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش‌های اولیه از حمله دشمن آمریکایی به نقطه‌ای در لارک
🔹
بر اساس اطلاعات اولیه، ساعتی پیش حمله پهپادی دشمن به جزیره لارک در استان هرمزگان انجام شد.
🔹
برخی گزارش‌های اولیه غیررسمی حاکیست که بر اثر جنایت دشمن آمریکایی تاکنون ۲ نفر به شهادت رسیده و ۲ نفر…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/akhbarefori/685666" target="_blank">📅 23:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685665">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e280c856b7.mp4?token=Mq1_9oK-jj-o7pxydOjDTIg4yO1a0wLiSndcgxOw3wJZdX096cdIW4FIzbBZj1vTaXDO0Y-z7P8Aagn22S6YMs0vkN2fIhnQsVj9awDs_3fyK2sjyzoPqGmp12uFKxwxGDxHDi0JWbsutSPrTCefDFXKaLNSTL1Zvcdou3A_P-GQchzA8FVq_cPUg493I_yN1H4qvpxfnjrSY-VaAWo_AFnciHNB7evdMslLDlKXmUyfyn6RQTFbwrdDXaq3Cqe264pEEeoiAUTZr3M4oldJmPQ5lhlp-u7y3k_rCoVn7F900UIb3NPHjkWJIGAzsKeMwayXuv-N9bNNFYCQ0JEZKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e280c856b7.mp4?token=Mq1_9oK-jj-o7pxydOjDTIg4yO1a0wLiSndcgxOw3wJZdX096cdIW4FIzbBZj1vTaXDO0Y-z7P8Aagn22S6YMs0vkN2fIhnQsVj9awDs_3fyK2sjyzoPqGmp12uFKxwxGDxHDi0JWbsutSPrTCefDFXKaLNSTL1Zvcdou3A_P-GQchzA8FVq_cPUg493I_yN1H4qvpxfnjrSY-VaAWo_AFnciHNB7evdMslLDlKXmUyfyn6RQTFbwrdDXaq3Cqe264pEEeoiAUTZr3M4oldJmPQ5lhlp-u7y3k_rCoVn7F900UIb3NPHjkWJIGAzsKeMwayXuv-N9bNNFYCQ0JEZKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیشب در پرواز ایران به کوالالامپور بخاطر خم کردن صندلی میان چند مسافر درگیری به وجود امد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/akhbarefori/685665" target="_blank">📅 23:28 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685664">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
انتقاد بی‌سابقه مشاور ولیعهد سعودی به رئیس امارات؛ القحطانی: بن‌زاید یک «رئیس باند» است تا رهبر یک کشور
سعود القحطانی، مشاور محمد بن سلمان:
🔹
ائتلاف ابوظبی با بنیامین نتانیاهو (که وی از او با لحنی تحقیرآمیز یاد کرد) با توهم تسلط بر غزه صورت گرفت، اما هیچ دستاوردی برای این کشور به همراه نداشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/akhbarefori/685664" target="_blank">📅 23:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685663">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulki12YR2Vqg-tw_fCjURw47IrznqxxbGwfLaP_cXHfWhfY8EybQ-JhdfpGtFezWM7OqG0VdIpukLFm50th7xzjk5p09-S96q4-g2KVbfYICeiVxS-dAhThmo6vlkG6ZHqpA1rkeLj44ZEZSxoutqEPACuTPlczj3DDAvqC1vwXjZWhwJt9cLh-hbia-QtKVDCl82hoIcMLJJHTPXDb2vbMUb7LVHaZMEG04rBkUfTk5ZBAMgIRzi-SPjgSEvTCXHAFTLeat5op8HS4lhcw128AZhDebus0U35WS5tpXVTrLB5v2FgNZLDZljfNyqpysAoO79k6zomEn95sFFv-_8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرندی: رژیم ترامپ اشتباه بزرگی مرتکب شده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/akhbarefori/685663" target="_blank">📅 23:23 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685662">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
شنیده‌شدن صدای انفجار در جزیره لارک
🔹
مردم محلی از شنیده‌شدن صدای انفجار در حوالی جزیره لارک خبر دادند.
🔹
هنوز محل دقیق و علت وقوع این انفجار مشخص نیست و پیگیری‌ها برای مشخص شدن جزئیات انفجار ادامه دارد./ فارس  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/akhbarefori/685662" target="_blank">📅 23:14 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685661">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
یک نیروی امریکایی مدعی شد: نیروهای ما مین‌زدایی از خطوط کشتیرانی بین‌المللی در تنگه هرمز را به پایان رسانده‌اند
🔹
نیروهای ما از نزدیک منطقه را زیر نظر دارند و آماده‌اند تا از جریان آزاد تجارت از طریق تنگه هرمز محافظت کنند  جزئیات بیشتر
👇
khabarfoori.com/fa/tiny/news…</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/akhbarefori/685661" target="_blank">📅 23:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685660">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zp1ws7bSTdaR5OsDDveOD8XLnrJpeDcB7HLa8ASACc4bElHOaCA_K1RITB3t6ENeBN3H8yxJzfwzU2lkzVDzlZx9wyYVPz5GOP2Ct7JE4Q6Ctgc8f1_CGytwRAs2AIUj_i5tyoSTNvPhPT5ntPPqcqDem1_D6iqbUuoSKng8DI4rbx7B85jSzerzyZori5mfTscj_v99JH9cj9A8eGJezw180Pf0Z56AUx8ubwqR9BSDdX0kkkBbX-wXxQm3LEn7lHSYGZhet-5sy2IQs67VH3HPTWIDI-q6TUOUdfjTkyA_BG71xs5Q_8VN0IYZNzAlJTrd-n_n3BfcPGwcY0qb0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مهم: انقلابی در کسب درآمد با هوش مصنوعی
🚀
اپلیکیشن ایرانی‌ای رونمایی شد که تمام مسیر را از پیداکردن ایده تا جذب مشتری و فروش داخل یک سیستم انجام می‌دهد!
دیگر لازم نیست بین ده‌ها ابزار و آموزش مختلف سردرگم شوید؛ این اپلیکیشن با کمک هوش مصنوعی:
✅
مسیر درآمدی و پیشنهاد قابل‌فروش را می‌سازد
✅
محتوا و مسیر جذب مشتری را آماده می‌کند
✅
پیگیری مشتری و سیستم فروش را راه‌اندازی می‌کند
❌
بدون نیاز به مهارت یا کسب‌وکار قبلی
📱
قابل اجرا با گوشی یا لپ‌تاپ
💰
برای ساخت درآمدی واقعی و قابل‌رشد
🎉
هم‌زمان با رونمایی، آموزش اپلیکیشن و دسترسی به سیستم کامل آن در این نوبت داخل یک کارگاه آنلاین، کاملاً رایگان ارائه می‌شود!
همین الان ثبت نامت رو تکمیل کن
👇🏻
https://monetizeai.site/57
⚠️
ظرفیت محدود</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/akhbarefori/685660" target="_blank">📅 23:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685659">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dc749d5ad.mp4?token=OG2K5RVGbL9QmgfB2wh6g-2zmvANDGSFCpdZ8_GqmQHcuqTLihKvMfiSvF0bfXg7y9IeQhtUAzwP4NgidXX4KwHha0853sLttg60vJO7Nlu2yZF2re31DtmBI58CVP_JGQbQA2A5LaBjlV3MVX1nhCmjzxiPHRsCiASqpUdlokANvkoj26HKmYB4vGYDHO2PvVgdaTZTZZC1Y9oni7rwwW-_mLVztxBQBWb_t0QvvzdMFEpg_0t7RGh_m3qZUVS8Y2I3MlTRxsx3sxhAFS_2FeYRVXTY7ezJuVNLzpD63gFyYRaLV746AAqRZ_6Jsk8B5aDEdEBzhDmavZE2mqya_TaRB1EZ29NazP1Q3JzW4I-n83d6VxJtsA1cPPYsSmk54x8CI1qLH1RgLMeLSIbfQsbkgc9eu1Gybh9jZIsaGoxG-kXLHQoD4zgCKVMeGC8ai6846ONxu0W9xX2glvoeeXgap2iHi9O93j_VCs9lCs1YEcOKXQKqzlfrKhwSM8Cs2Pq79emUIeqf9HEzXVOc9bxQlmJ2WtaMh1oJ0a0PXKGI7rty3cAFVPFTLwrbF3nc7luzb_zaI9fP8BXs0i_xylBeLnUCQmFZUeqR9lPps4Yre4wONOSApk-jMk5pkjFmnqyPv2S3CGrmtmetc9U74t8U0z1P_aNCsok_LLtDOpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dc749d5ad.mp4?token=OG2K5RVGbL9QmgfB2wh6g-2zmvANDGSFCpdZ8_GqmQHcuqTLihKvMfiSvF0bfXg7y9IeQhtUAzwP4NgidXX4KwHha0853sLttg60vJO7Nlu2yZF2re31DtmBI58CVP_JGQbQA2A5LaBjlV3MVX1nhCmjzxiPHRsCiASqpUdlokANvkoj26HKmYB4vGYDHO2PvVgdaTZTZZC1Y9oni7rwwW-_mLVztxBQBWb_t0QvvzdMFEpg_0t7RGh_m3qZUVS8Y2I3MlTRxsx3sxhAFS_2FeYRVXTY7ezJuVNLzpD63gFyYRaLV746AAqRZ_6Jsk8B5aDEdEBzhDmavZE2mqya_TaRB1EZ29NazP1Q3JzW4I-n83d6VxJtsA1cPPYsSmk54x8CI1qLH1RgLMeLSIbfQsbkgc9eu1Gybh9jZIsaGoxG-kXLHQoD4zgCKVMeGC8ai6846ONxu0W9xX2glvoeeXgap2iHi9O93j_VCs9lCs1YEcOKXQKqzlfrKhwSM8Cs2Pq79emUIeqf9HEzXVOc9bxQlmJ2WtaMh1oJ0a0PXKGI7rty3cAFVPFTLwrbF3nc7luzb_zaI9fP8BXs0i_xylBeLnUCQmFZUeqR9lPps4Yre4wONOSApk-jMk5pkjFmnqyPv2S3CGrmtmetc9U74t8U0z1P_aNCsok_LLtDOpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیست‌ونهمین نمایشگاه بین‌المللی الکامپ، فرصتی برای دیدار، گفت‌وگو و همراهی با تازه‌ترین جریان‌های فناوری و تجارت الکترونیک.
۹ تا ۱۲ شهریور
ساعت ۸ تا۱۶
https://t.me/ElecompOfficialNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/akhbarefori/685659" target="_blank">📅 23:01 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
