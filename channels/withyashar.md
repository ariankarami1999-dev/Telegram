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
<img src="https://cdn4.telesco.pe/file/hWV4OsRIDT73jXn9pV8uRHeN8fLNdlSkujKgBDV0kOz2afg5Fxp3CtQPZnUXMxGEcuQJrSw38TRZ3bkEQRFoXLxLz612hU-bqRnDgzm1-UomoYl3Q_Dys6EwBF1sRErRPpjWj7XPEpioTiXu33ei1aiZTRd7EsH0QmGdOF81O65GTJ9ajWGLunFobda_rcYqAS7YVpEJ_tHCYEPgUA-4iRh4tKARKn6RIgombdQksn-Sgv88CpxdG9FBm4VUtTGdQOcJJJcbWOO9YW-z7efg5_7X-6P1rc7wcDH8orqAmOFwE_f_zw0494aPrGksT_znazmziS_-CEOgaFR2tquHPg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 276K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 09:41:48</div>
<hr>

<div class="tg-post" id="msg-12624">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">گویا موشلی رو جمعه در تهران و شنبه در مشهد تشیع میکنند
@withyashar</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/withyashar/12624" target="_blank">📅 03:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12623">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/withyashar/12623" target="_blank">📅 03:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12622">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/withyashar/12622" target="_blank">📅 02:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12621">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/12621" target="_blank">📅 02:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12620">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/12620" target="_blank">📅 02:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12619">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/12619" target="_blank">📅 01:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12618">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/withyashar/12618" target="_blank">📅 01:52 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12617">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/withyashar/12617" target="_blank">📅 01:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12616">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/withyashar/12616" target="_blank">📅 01:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12615">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/withyashar/12615" target="_blank">📅 01:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12614">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/withyashar/12614" target="_blank">📅 01:29 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12613">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">کارشناس صداسیما :
وصل شدن اینترنت متوقف میشه و دستور رییس جمهور اجرا نمیشه چون خلاف دیوان عالیه.
@withyashar</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/12613" target="_blank">📅 01:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12612">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اتاق جنگ با یاشار : شله داوود @withyashar</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/12612" target="_blank">📅 00:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12611">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dl0MsYV127XLmO4oZrRE7RX3GXsUqGT-CdwgrTMooRQjBwaQiwvansU_stPpr-FuVA65MycdnFEiv_QSDBmaalifKe2qcVCkG7lgeD6NhJbR-5Ct3nyisRMdihibTf9eKMA5MvsTOK0OyLbxj9JOH9CVSIqxSxjQpU8NBOgYVfQmLZ43EA4khrkL_LbtWpQWuyC3fvk1sQj31PLE22YR-qGHi1e_9x9DNcP0Wqc2Y0ReDtFu6gw2YNsQ_BAU6HcwkIfe-5A3tJwo_n7HO3dzPoDCK_qjQPJqYjapkkOAJzqgORdU53AZQ7WS4PqiUuGgNRZxXyKKWwBIcheRjSp1rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیما تصویر جدیدی از مجتبی خامنه‌ای را منتشر کرد
@withyashar
خوب پس بدل تکمیل شده نتو وصل کردن ولی اصلا شبیهش نیست !
🤣</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/12611" target="_blank">📅 00:46 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12610">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6ZwLJq2WFK27QTOu3McC3sny9MTBo-fM3iYyn7QQUeIs8rcQ914GCqEvqsdJbldYnLunKS0MwEnl2bHqgBwaRNC2E5ultXIby_ec-M_twHxVLSBsjl5loHvw_lAayuKI7dGQyiOtitu4dM_UIhiVer54z1r56O4rkilKb2tN8ZVCBrW-sWXbpW1dXnVjESfn2QJEQE1pHyqxZ5n_FDHfeQGxXquxK5W-1djnFo0KxBzjWOBopqwnDzZoW8zfEvaNVGOyLHUo4txT8mcuRp7qR8iDkVZ9TxHp1m8csgHOhcjEQJGYaDPV-_W6QXpPVf54tgubGnX-D-GY64mN6EzpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با توجه به شرایط نامساعد جوی احتمالی فردا، جلسه کابینه را در کاخ سفید برگزار خواهیم کرد و سفر کابینه به کمپ دیوید را به تعویق می‌اندازیم. از توجه شما به این موضوع سپاسگزاریم! رئیس جمهور دونالد جی. ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/12610" target="_blank">📅 00:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12609">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/12609" target="_blank">📅 00:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12608">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دفتر رسانه‌ای شاهزاده رضا پهلوی با انتشار بیانیه‌ای در واکنش به صدور حکم اعدام برای چهار شهروند ایرانی، نوشت: «صدور دوباره احکام اعدام برای چهار تن از بچه‌های اکباتان، میلاد آرمون، محمدمهدی حسینی، مهدی ایمانی و نوید نجاران، سند دیگری از ماهیت جنایتکار رژیم جمهوری اسلامی است که برای حفظ قدرت، جوانان ایران را به قتل می‌رساند و از خون مردم برای بقای خود تغذیه می‌کند.»
@withyashar</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/12608" target="_blank">📅 23:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12607">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نتانیاهو از ترور هدفمند خبر داد :  همین الان محمد عوده، از فرماندهان شاخه نظامی حماس و یکی از طراحان حمله ۷ اکتبر رو در غزه هدف قرار دادیم  به حساب همه‌شون می‌رسیم @withyashar</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/12607" target="_blank">📅 23:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12606">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b685af254.mp4?token=tFTNaKql646ueAOjaKwyqWcQNiHDPU9l6YQbe-zp03MS_j_qkExaCiut6UTtI7j71RNqwWHzoD_DU14JGHBQFx9FT-UERYGcx-qBY1lsZN5_WjXXYOcIS8Oal4nOXChu0-a-0GuhBYo_IlDSl2Bnh05NAjUHaMHwut7kdRwdo6eqoe3P3niV2oMxZttR74SnmtsX5aerEQbamBGI6LC8PN7UdlY4CjTTdVta1woHTlsGbgwXn_DrWLcR0rgyKenY6ig_3Ph37swj2EaoJgWO27XE_weDOt-6HI4pMYfxxL8Sr60aFOjh1_bejtPx-EqyOwqrl-UCG7mC6zOWhdKYJq12H4ubJEDkQijZ1hPksUIqGF0jlXYTqPcAcGwducM0ZEZFK8gcDLQudTUQUQlnI2kMKavUvFWT5uhtlFHopcDmlcC0yuiMQsHDjJXpNBmX6Ilb-VSDBn_bwvRYunWhxROFhihqTBLSttagwzENyqWDxok1Y34VpOOmxPExHALn3qymvOQY7bFLn1GdZhIGLr43RaCFmMEK29eb8EdA8FzYmJJPHV4tzCjsN-zJewjT4nIWxAzCmnxKjCfYblMSMdXr6QlY3T3b8151fOf84tS_AD5_t0xbnrVNwvNV52p_yGeePSiZrjCMT1jLAjCSRc44Mn8HTj9-aUUjfkDZGYY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b685af254.mp4?token=tFTNaKql646ueAOjaKwyqWcQNiHDPU9l6YQbe-zp03MS_j_qkExaCiut6UTtI7j71RNqwWHzoD_DU14JGHBQFx9FT-UERYGcx-qBY1lsZN5_WjXXYOcIS8Oal4nOXChu0-a-0GuhBYo_IlDSl2Bnh05NAjUHaMHwut7kdRwdo6eqoe3P3niV2oMxZttR74SnmtsX5aerEQbamBGI6LC8PN7UdlY4CjTTdVta1woHTlsGbgwXn_DrWLcR0rgyKenY6ig_3Ph37swj2EaoJgWO27XE_weDOt-6HI4pMYfxxL8Sr60aFOjh1_bejtPx-EqyOwqrl-UCG7mC6zOWhdKYJq12H4ubJEDkQijZ1hPksUIqGF0jlXYTqPcAcGwducM0ZEZFK8gcDLQudTUQUQlnI2kMKavUvFWT5uhtlFHopcDmlcC0yuiMQsHDjJXpNBmX6Ilb-VSDBn_bwvRYunWhxROFhihqTBLSttagwzENyqWDxok1Y34VpOOmxPExHALn3qymvOQY7bFLn1GdZhIGLr43RaCFmMEK29eb8EdA8FzYmJJPHV4tzCjsN-zJewjT4nIWxAzCmnxKjCfYblMSMdXr6QlY3T3b8151fOf84tS_AD5_t0xbnrVNwvNV52p_yGeePSiZrjCMT1jLAjCSRc44Mn8HTj9-aUUjfkDZGYY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تری ینگست خبرنگار فاکس‌نیوز از اسرائیل گزارش میکند : رسانه‌های حکومتی ایران ادعا می‌کنند که برای هرگونه توافق با آمریکا، باید ۲۴ میلیارد دلار آزاد شود.
تیم ترامپ می‌گوید چنین چیزی قرار نیست اتفاق بیفتد و “هرگونه کاهش فشار مالی فقط در صورتی انجام می‌شود که ایران به تعهداتش عمل کند.”
ایران باید کاملاً از برنامه هسته‌ای دست بکشد و هیچ‌گونه کنترلی بر تنگه هرمز نداشته باشد، تمام.
@withyashar</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/12606" target="_blank">📅 23:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12605">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اگر ایران تسلیم شود، بپذیرد که نیروی دریایی‌اش از بین رفته و در کف دریا آرمیده است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر تمام ارتش آن از تهران خارج شود در حالی که سلاح‌ها را زمین گذاشته و دست‌ها را بالا گرفته‌اند و هرکدام فریاد بزنند «من تسلیم می‌شوم، من…</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/withyashar/12605" target="_blank">📅 23:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12604">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QeefxX22Z95R-Mtkq4jRqX3T3OAqMXJVf4wPlWGQH4G4G_kkiD6JnxCa7z9W9qxFuqVY9ABDMKEWBPxuhFpAgjQHdnmoAVZ1MCObgLf1tF7XMOCyPnrg8Xji9sGBNWsKt0QqqixrlNk2Dx3H_lrr-rrDysnaOQN0-mQbXqjt8nN1xoztSNjhWcmToocpq2WMqYYcvZkYqJRPEOpQpwi_xlr_HJ6eeog57bdvKlKicHivpn7nDD4RgKHrfOexWYz_-erfGE8ktShl7V2rGF7i1qWjUkjrroct7_fP_CfHm-v8bRhWnN-sphheFJLt5K6hSBDt69JeYKdxGaTAxDXunQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر ایران تسلیم شود، بپذیرد که نیروی دریایی‌اش از بین رفته و در کف دریا آرمیده است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر تمام ارتش آن از تهران خارج شود در حالی که سلاح‌ها را زمین گذاشته و دست‌ها را بالا گرفته‌اند و هرکدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم» و همزمان دیوانه‌وار پرچم سفید را تکان دهند، و اگر تمام رهبران باقی‌مانده‌شان همه «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت بزرگ و نیروی شگفت‌انگیز ایالات متحده آمریکا بپذیرند، در این صورت نیویورک تایمزِ شکست‌خورده، وال‌استریت ژورنال چین (!)، سی‌ان‌ان فاسد و اکنون بی‌اهمیت، و سایر اعضای رسانه‌های «اخبار جعلی»، تیتر خواهند زد که ایران یک پیروزی استادانه و درخشان بر ایالات متحده آمریکا به دست آورده و اصلاً رقابت نزدیک هم نبوده است. دموکرات‌ها و رسانه‌ها کاملاً راه خود را گم کرده‌اند. آن‌ها کاملاً دیوانه شده‌اند!!!
رئیس‌جمهور DJT
@withyashar</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/12604" target="_blank">📅 23:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12603">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">عزیمت ترامپ از کاخ سفید به بیمارستان @withyashar</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/12603" target="_blank">📅 22:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12602">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">منبعی آگاه به «اتاق جنگ با یاشار» گفت که در شروط توافق این مورد تأکیید شده که ترامپ باید ختنه کند.
🤣
@withyashar</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/12602" target="_blank">📅 22:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12601">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/12601" target="_blank">📅 22:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12600">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تسنیم : فروش نخی سیگار ممنوع شد  اتاق اصناف ایران: فروش سیگار نخی و فرآورده‌های دخانی بازشده در تمامی واحدهای صنفی ممنوع شد. @withyashar
😐</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/withyashar/12600" target="_blank">📅 22:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12599">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">تسنیم : فروش نخی سیگار ممنوع شد
اتاق اصناف ایران:
فروش سیگار نخی و فرآورده‌های دخانی بازشده در تمامی واحدهای صنفی ممنوع شد.
@withyashar
😐</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/12599" target="_blank">📅 22:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12598">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رادیو ارتش اسرائیل گزارش داد که دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در حال حاضر در یک تماس تلفنی هستند.
@withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/12598" target="_blank">📅 22:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12597">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نت بلاکس : ۸۶٪ اینترنت ایران برگشته @withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/12597" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12596">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نیروی دریایی ۳پا: کنترل هوشمند تنگهٔ هرمز با اقتدار درحال انجام است و هرگونه تجاوز با ضربات کوبنده پاسخ داده خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/12596" target="_blank">📅 22:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12595">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نتانیاهو از ترور هدفمند خبر داد :
همین الان محمد عوده، از فرماندهان شاخه نظامی حماس و یکی از طراحان حمله ۷ اکتبر رو در غزه هدف قرار دادیم
به حساب همه‌شون می‌رسیم
@withyashar</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/12595" target="_blank">📅 21:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12594">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGnsv_juExKGTAHduK2I5emDmb6ITX-rUmi6kaGL-gX1nTWwWnJaJcuOH24XjSsDSNKC0Y30Tkj2jtV7IHDQXrhatbtSh8NAToT_uDP55DgSRD7Yq9aklIJJPkpeqFeQ4-zvhRQSg0j0Hm0FNUE-lqCnjzXKE8Qv3kodiZsZH3aHQFdcrtKb1DS4Tltq-Cq9A8VCek2Rz-YbpNnF_N5VcUSpzcTPSsSilxTkUKU4Lnxgw3lhjpHFoTE34TSCTeqebtNaN_sRU_FCnMdv5qVx5VJb5Q1J4pPxnwdQjL5k4bIIjjGv9xisKpNzmhr7VsNtu5hx4RkMvRjA9eoH1MBnlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت بلاکس : ۸۶٪ اینترنت ایران برگشته
@withyashar</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/12594" target="_blank">📅 21:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12593">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نیویورک تایمز: ایران با چندین پهپاد انتحاری به چند ناو آمریکایی که از سمت دریای عمان، قصد ورود به تتگه هرمز را داشتند حمله کرده است
@withyashar</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/12593" target="_blank">📅 21:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12592">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/12592" target="_blank">📅 21:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12591">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کانال 14 اسرائیل به نقل از منابع:
حمله به ایران پس از دریافت «پیام مشخصی» از آمریکا، در این مرحله از دستور کار خارج شده.
@withyashar</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/12591" target="_blank">📅 21:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12590">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3faocj7v4znazEXIDYGryb3vt1BV4G3X55Uld1e_2ZaefeKSZ-64hnB9If9FkqAbpsQY4qwDlOUWX1c9HdIVKa3YFjmcnGanDtspY2-Iqn7rrBZgQCyDSzI_WvCEsNdBy8W8Lp3eImqR5Z4gw2-cfDlFKS0guhMVAeCopZhGmQ3Br7ury_VwhJiyWvPZdugNS1VDOYGgC4sDdH-2j85E6Jg5DY5QWvDGuJVLYvwD78sc6aFWS2ynhec-gUJuzE1H4E188cAXdYKjEf7Z2Ja9KpqB3HjFtAYiPtcam7AaCDa0ukluyB5p2dyj-fHmPz82rWu0JLpe1lthPlJdn91Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارک لوین : «بی بی، برو بزن بترکونشون!»
@withyashar</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/withyashar/12590" target="_blank">📅 21:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12589">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نت ها اوکی باشه لایو هم شروع میکنم که به امید خدا آخر هفته اگه زد زنده زارتان زورتان رو بگیرم
💥
🌶️
این ۵ روز‌آینده بسیار روز های مهمیه ! ببینیم تکیفمون روشن میشههههههههه</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/withyashar/12589" target="_blank">📅 20:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12588">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/withyashar/12588" target="_blank">📅 20:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12587">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/withyashar/12587" target="_blank">📅 20:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12586">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نتانیاهو، در بیانیه‌ای اعلام کرد که نیروهای زمینی اسرائیل در حال «گسترش و تعمیق» عملیات این رژیم در لبنان هستند و «در حال تصرف مناطق وسیعی هستند»
@withyashar</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/12586" target="_blank">📅 20:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12585">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کانال ۱۲ عبری:
آمریکا به اسرائیل هشدار داد که به هیچ شکلی به بیروت حمله نکند.
@withyashar
😐</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/withyashar/12585" target="_blank">📅 20:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12584">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qahqBiQboY8_JKBTrnZYyFCURTpUC_0nmrFqOSKVt-R4Np4zGCEbBxkfNXAlaGSTh6GWRiorqjiADDN6BfXAEjiCdh96Msgn-qM1YURDFyug7a4yF2IYb3TRI79AjHHkA_UunsKe60GviFGcFhxj63JZVvwKbghGgi0GnWcelRaRQ5URksV4UdnzNlI-zqsCLM-1IwCL30bn-exMM3VEgqfyB9IOkEdGJmNqiKZBTzdkTjCH7Cx1m63fOdZMnwrvfX14zraPD5pVia1-Ilf2iuMgkBTBZxlZElH0Ve-WQRKow9TIZmbF4SFH5wbN2vAb2tDsq3EmEQZAs8X9jvGdng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : همین الان معاینات پزشکی شش ماهه‌ام را در مرکز پزشکی نظامی والتر رید تمام کردم. همه چیز عالی بود. از پزشکان و کارکنان عالی متشکرم! به کاخ سفید برمی‌گردم. رئیس جمهور دی‌جی‌تی
@withyashar</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/withyashar/12584" target="_blank">📅 20:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12583">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">معاون وزیر ارتباطات: سيستم عامل، مرورگر، آنتی‌ویروس، اپلیکیشن‌های بانکی و ابزارهای امنیتی خود را بروزرسانی کنید
@withyashar
چه دلسوز شدن.
🤣</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/withyashar/12583" target="_blank">📅 20:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12582">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">https://t.me/boost/withyashar
بوست کنین ایومجی و استوری اضافه بشه ۵۴۴ بوست لازم داریم
🥲</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/withyashar/12582" target="_blank">📅 20:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12581">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سنتکام: پروژه آزادی از سر گرفته نشده و نیروهای آمریکایی در حال حاضر کشتی‌های تجاری رو از تنگه هرمز همراهی نمی‌کنند.
@withyashar
پروژه قایم موشک گویا شروع شده
😂</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/12581" target="_blank">📅 20:11 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12580">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/12580" target="_blank">📅 19:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12579">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bf840f209.mp4?token=Z5jGJriF3doNghpB2_rxrsx8OQHvgzHdCk8jbfF7HNjfevHQN2F9UjcZnvVkAeQzYy6pBVVuN8XKYmib4gBuDnEHOdeV22NsU4AbygP8yDjGUQLsq3fCf1bn9e9UOyaPlL_ugSoDpodUs1dooFc7JcSFKRtwvHbaNwG5qyUC_RPMMX_untlM0k46FB6kTw45zuzA0iU3WPMDGq6qiI6JJdXvB0bmz-qVINt4bz4e3yXWoDg6VPYFSpnspQuXIDZOH8-0k2OLA10EcGL5Qmvwxtvtwn2veGtPwNseG7s24qK1Rj5jKR20ShkUlL0ZJbn3gy0sQyJ5vOgJ1OXG6v_THw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bf840f209.mp4?token=Z5jGJriF3doNghpB2_rxrsx8OQHvgzHdCk8jbfF7HNjfevHQN2F9UjcZnvVkAeQzYy6pBVVuN8XKYmib4gBuDnEHOdeV22NsU4AbygP8yDjGUQLsq3fCf1bn9e9UOyaPlL_ugSoDpodUs1dooFc7JcSFKRtwvHbaNwG5qyUC_RPMMX_untlM0k46FB6kTw45zuzA0iU3WPMDGq6qiI6JJdXvB0bmz-qVINt4bz4e3yXWoDg6VPYFSpnspQuXIDZOH8-0k2OLA10EcGL5Qmvwxtvtwn2veGtPwNseG7s24qK1Rj5jKR20ShkUlL0ZJbn3gy0sQyJ5vOgJ1OXG6v_THw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عزیمت ترامپ از کاخ سفید به بیمارستان
@withyashar</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/12579" target="_blank">📅 19:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12578">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1513fcd1a2.mp4?token=ZtkBVJKrKtPj6VoRBoMsrI6mRdYUlxdoWYovb7c-Z5O8wi4nFvXPXLKSWu1Wq1dC2pLY7YXnz_d-nsQp-VU_MpKGsHGSWVb5Cn70JgvWf5eMDuf5bDEPKzSoNOmIGNcCoLU78osMNv1mknbKJofb2WeMGV2tpBf-g5C-I2ZBUC7m63K4jqO0-EiE7bbMcK1NQjDMUVaMlCTQDlNVJcuY6NnANcZ-rrUROCG8dvcbFW6_DxthD1BDJeI59dnTvYD47ZmZZzcW8zvtdomoev6QmobYN8e6xYtv8CFMM_0Wvx6u5GLhPwLaht9Ee1nFM8JfFRamXWlwCSLiNeNmoa4QWlCyYPnGbpbkL5IUKpWJ8F-cGT-cfh06ysLbHRD0nw74IOq7Dy-Bxy7NjxBhI-uJ0-140dLMpjTo-QLLV2Z4yZp6eKS0q9kijnCPY-okq9rAvh6gxWs5H3vI_H_uOIQQfQS_CR2dgSVhlUYRekEgGdjSvbDC64jYC-g6NEsUPmpGVxxjJTeF23GIgofHeUURqcUUmpwYPJG14NfGI6kQg8XwaeNoxXrtUOBQZvI7OAJxVy0-oiszIQlr1wrd9D6r7YcQv8ucb-O0ITO4-5FlX1IM1dv34b-cnrW0bW00SJbhgFwCa7v60q2dOB-tY1-m0Hg9asWQkEfZIPiRVfjYK94" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1513fcd1a2.mp4?token=ZtkBVJKrKtPj6VoRBoMsrI6mRdYUlxdoWYovb7c-Z5O8wi4nFvXPXLKSWu1Wq1dC2pLY7YXnz_d-nsQp-VU_MpKGsHGSWVb5Cn70JgvWf5eMDuf5bDEPKzSoNOmIGNcCoLU78osMNv1mknbKJofb2WeMGV2tpBf-g5C-I2ZBUC7m63K4jqO0-EiE7bbMcK1NQjDMUVaMlCTQDlNVJcuY6NnANcZ-rrUROCG8dvcbFW6_DxthD1BDJeI59dnTvYD47ZmZZzcW8zvtdomoev6QmobYN8e6xYtv8CFMM_0Wvx6u5GLhPwLaht9Ee1nFM8JfFRamXWlwCSLiNeNmoa4QWlCyYPnGbpbkL5IUKpWJ8F-cGT-cfh06ysLbHRD0nw74IOq7Dy-Bxy7NjxBhI-uJ0-140dLMpjTo-QLLV2Z4yZp6eKS0q9kijnCPY-okq9rAvh6gxWs5H3vI_H_uOIQQfQS_CR2dgSVhlUYRekEgGdjSvbDC64jYC-g6NEsUPmpGVxxjJTeF23GIgofHeUURqcUUmpwYPJG14NfGI6kQg8XwaeNoxXrtUOBQZvI7OAJxVy0-oiszIQlr1wrd9D6r7YcQv8ucb-O0ITO4-5FlX1IM1dv34b-cnrW0bW00SJbhgFwCa7v60q2dOB-tY1-m0Hg9asWQkEfZIPiRVfjYK94" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : شله داوود
@withyashar</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/12578" target="_blank">📅 19:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12577">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">منابع عبری: در ساعات اخیر نتانیاهو مشاوره‌ای امنیتی در مورد وضعیت در جبهه های لبنان و ایران با رئیس ستاد ارتش اسرائیل، وزیر دفاع و دیگر سران نظامی ارتش اسرائیل برگزار کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/withyashar/12577" target="_blank">📅 19:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12576">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بچه ها تلگرامتون رو آپدیت کنید سریع تا نظر سنجی‌ها رو ببینید</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/12576" target="_blank">📅 19:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12575">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">فک کنم ترامپ با پروژه آزادی پلاس داره کامبک میزنه
😂
💥
@withyashar</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/withyashar/12575" target="_blank">📅 18:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12574">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نیویورک پست: ترامپ برای انجام سفری به کمپ دیوید است در حالی که تنش‌ها با ایران به دلیل حملات آمریکا افزایش یافته است  ترامپ چهارشنبه به طور نادر به کمپ دیوید سفر خواهد کرد تا جلسه کابینه‌ای برگزار کند، زیرا مذاکرات صلح با ایران به زمان حساس خود نزدیک می‌شود،…</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/12574" target="_blank">📅 18:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12573">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">شرکت مخابرات: اتصال کامل اینترنت بین‌الملل مشترکان برقرار شد
کاربران سرویس‌های پهن‌باند ثابت شامل FTTH، VDSL و ADSL هم‌اکنون بدون محدودیت به شبکهٔ جهانی اینترنت متصل هستند و امکان استفاده کامل از وب‌سایت‌ها و خدمات بین‌المللی برای آن‌ها فراهم شده است.
@withyashar</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/withyashar/12573" target="_blank">📅 18:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12572">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آمار لحظه‌ای اتصال اینترنت کشور:
✅
مخابرات (منطقه ای)
✅
آسیاتک
✅
شاتل (منطقه ای)
✅
پیشگامان
✅
مبین نت TD-LTE
✅
صبانت
✅
پارس آنلاین
✅
زیتل
✅
افرانت
✅
ایرانسل (TD-LTE)
❌
ایرانسل (سیمکارت)
❌
همراه اول (سیمکارت)
❌
رایتل (سیمکارت)
❌
سامانتل (سیمکارت
@withyashar</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/withyashar/12572" target="_blank">📅 18:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12571">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ارتش اسرائیل اعلام کرد که زیرساخت‌هایی به طول 11 کیلومتر را در در شمال غزه منهدم کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/withyashar/12571" target="_blank">📅 18:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12570">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">فک کنم ترامپ با پروژه آزادی پلاس داره کامبک میزنه
😂
💥
@withyashar</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/12570" target="_blank">📅 18:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12569">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO ) از وقوع سانحه‌ای در فاصله ۶۰ مایلی دریایی شرق مسقط، پایتخت عمان خبر داده است.
به گزارش این سازمان، ناخدای یک نفتکش گزارش داده که یک انفجار خارجی در اطراف این کشتی رخ داده است.
@withyashar</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/withyashar/12569" target="_blank">📅 18:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12568">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ادعای وال استریت ژورنال:
به گفته مقامات نظامی آمریکا، نیروی دریایی ایالات متحده کمک به عبور کشتی‌ها از تنگه هرمز را دوباره آغاز کرده است.
این مقامات به وال‌استریت ژورنال گفتند که یک ابرنفتکش یونانی حامل دو میلیون بشکه نفت خام، هنگام عبور از این آبراه در سواحل عمان، توسط نیروی دریایی آمریکا هدایت شده است.
@withyashar</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/withyashar/12568" target="_blank">📅 18:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12567">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خوش اومدین ولی‌ لطفا تک تک پیغام ندید که  وصل شدید
🙌🏾</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/12567" target="_blank">📅 18:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12566">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/12566" target="_blank">📅 17:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12565">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSoheil</strong></div>
<div class="tg-text">یاشار گفتی میخوای یه کمپین راه بندازی همه باشن ؟
بیا نتو هم برات وصل کردن
صدات تا کجا میره مرد ... میخوام فکر کنم که پیامتو بالا شنیدن و بهت امیدوارن که نجاتشون بدی</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/12565" target="_blank">📅 17:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12564">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سخنگوی وزارت خارجه قطر: اینکه گفتن قطر 12 میلیارد دلار از پول‌های بلوکه شده ایران رو قراره پرداخت کنه کاملا کذبه و از این خبرا نیست! @withyashar</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/12564" target="_blank">📅 17:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12563">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تلویزیون ایران:
رئیس مذاکره‌کنندگان ارشد ایرانی قالیباف مذاکرات خود را در دوحه به پایان رساند و به تهران بازگشت
@withyashar</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/withyashar/12563" target="_blank">📅 17:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12562">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ارتش اتاق جنگ داره بر‌میگرده
😈
💥</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/withyashar/12562" target="_blank">📅 17:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12561">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نیویورک پست:
ترامپ برای انجام سفری به کمپ دیوید است در حالی که تنش‌ها با ایران به دلیل حملات آمریکا افزایش یافته است
ترامپ چهارشنبه به طور نادر به کمپ دیوید سفر خواهد کرد تا جلسه کابینه‌ای برگزار کند، زیرا مذاکرات صلح با ایران به زمان حساس خود نزدیک می‌شود، روزنامه پست مطلع شده است.
محل برگزاری جلسه ممکن است به دلیل هوای نامساعد تغییر کند.
@withyashar</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/withyashar/12561" target="_blank">📅 17:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12560">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">عارف: گام نخست دسترسی آزاد و ضابطه‌مند به فضای مجازی برداشته شد
@withyashar</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/withyashar/12560" target="_blank">📅 17:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12559">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مالکی: در قطر توافق شد که نیمی از پول‌های بلوکه شده ایران پرداخت شود
فداحسین مالکی، عضو کمیسیون امنیت ملی مجلس:
سفر آقای قالیباف به قطر در راستای موضوعات مذاکره، مسایل دوجانبه و موضوعات بین‌المللی است و آخرین تحولات بین‌المللی آنجا بررسی خواهد شد.
از آنجا که قطر مسئولیتی درباره پرداخت بدهی‌های ایران به عهده گرفته است، یکی از موضوعات سفر آقای عراقچی و قالیباف، موضوع بدهی جمهوری اسلامی ایران است.
طبق یکی از بندهای توافق‌نامه، قرار شده است که نیمی از پول‌های بلوکه شده که در اختیار قطر است به جمهوری اسلامی ایران داده شود.
@withyashar</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/withyashar/12559" target="_blank">📅 16:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12558">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwGNE2cLqBF8CHOWGQtbQ6ATtzYv2x3X_iPlzQMYGUvL_-u-OPR_5GeAzyQP5-qJz2-i86tx2NitxaKoAg2-47-ce8pdz2ebQl3yIRGI7ejcAlVZXNh5Ql8VG0gcM1qJq2TZ1hyRVKuOQpKhEWHnKMoXpxSG8d0oM7MCPjunvPA-p4tpqvAArPAhRWOwA26MOMx6dTo1YzFMg8UuzI2f1bJAZb1zppZaMHXFuKUUulvJCF-LQaqrl5XwC9cR34obVam_wbpY4hDUb9pC7WHquE7OrOe3OoJ3AZmlYxtC9spU7J3tlYG-TAjdqjHE4lmjJi8PdKUdzCszl638RKDbdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش نت بلاکس، بعد از 88 روز و  2093ساعت خاموشی تمام عیار اینترنت، همکنون نزدیک به 35% اینترنت ایران وصل شده.
@withyashar</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/withyashar/12558" target="_blank">📅 16:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12557">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وال استریت ژورنال: قالیباف برای گفتگو درباره پایان جنگ برای دومین روز متوالی در قطر مانده
وال استریت ژورنال مدعی شد مقامات ایرانی و میانجی‌گران عرب گفتند: «محمدباقر قالیباف» برای دومین روز متوالی در قطر مانده است تا درباره توافق پایان جنگ گفتگو کند.
@withyashar</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/withyashar/12557" target="_blank">📅 16:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12556">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02157fdf30.mp4?token=ZpXxhYjTLVnyPkAvFF2ySvrEAghSQt-lFHKE3Ey7mCqyHxr2LBgFsbHcd5mlnvicqRS9OCYWhD44Y53u1xdis1DGG6LdwLjquA24t-DW05ypKuBvWJRUK1gSpaUJBxfndiSZ-A0lA41xQjmSrJkazBo0tvmVTwfC-BCgv-Wxo95I6eEUvXnNZeYZnKP2-MU1HzfK0wDJjTgvG61UWOvSGt8UBx0sxW3qMQLTQ5PSLwwSFhCAiBAWK--lxbj7a4cowDpqK2iFW1wPUkfLYs_uTVPIIDJKJzN1jIxZkv4FB9RRqpHnKaEDkaQhqgQVE7s8s7muzedHxNLX1iB4BELMvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02157fdf30.mp4?token=ZpXxhYjTLVnyPkAvFF2ySvrEAghSQt-lFHKE3Ey7mCqyHxr2LBgFsbHcd5mlnvicqRS9OCYWhD44Y53u1xdis1DGG6LdwLjquA24t-DW05ypKuBvWJRUK1gSpaUJBxfndiSZ-A0lA41xQjmSrJkazBo0tvmVTwfC-BCgv-Wxo95I6eEUvXnNZeYZnKP2-MU1HzfK0wDJjTgvG61UWOvSGt8UBx0sxW3qMQLTQ5PSLwwSFhCAiBAWK--lxbj7a4cowDpqK2iFW1wPUkfLYs_uTVPIIDJKJzN1jIxZkv4FB9RRqpHnKaEDkaQhqgQVE7s8s7muzedHxNLX1iB4BELMvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو ساعتی پیش تو مقر کریا با وزیر جنگ اسرائیل و رئیس ستاد ارتش جلسه امنیتی برگزار کرد
@withyashar</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/12556" target="_blank">📅 16:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12555">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23fc7f9f78.mp4?token=uoY-nWy7bt_iQtVRVS6a5-CH12ei6Um3sWwkzon-NFFlkLj_T_oxdneai7dd2om5de6o4Fro5TrD0g3E32ueag3nAb2_rULvyMot6YWfYyMUQgcGxXpQgPcv0aw0e9gDMniXdLCWOfl6gpv_D1ItlN9HWc3iwSnGeNgFo4q7ooxYZZ2Zw3ED2ctnpoBzIb7V9AZtNzaf8HjEwheM8U7X2pseWry6wR7CZM82IetS-fysJAaZuyM_8QeD4LSFnBhzP9LPj-xlOMyC6TNlOeCj9B0XKarW-wNVAAATndGH0NP3jwvv77De3HJRfK18bL6MavbMxLTjKjuIegJyPQz0vGlsev0k8-pVU2ScB5OCRTvgJ-HAzB1lujSvs39xAZekedfsFujwWKKuxcAXZncEbQ13iwS-N4Lfn7f2qppmlAyx47mbEhhlcjPL9B86hIH6Qs4qYb8XZnNbVcV0yXgYwpkaHB0Fykbq-qYDnmkhx6Umbs5A4Fq7qcTdCpej_ulvA4WnR2gPZVwejaoXJg7WIYZsmvyr80K26GooC0-qtql7dLr3qEbrHIZetGWUmikiN9IUhtRc08hprvIA3owI5-jgyEUBh_v_4PdSOOaq9nXmuFqKQ1-qv-TtZI1F3N1W0XNXyLAXGU7ay9gqSvfZ2D1-Ch5GtLBcai0HHdm9fWo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23fc7f9f78.mp4?token=uoY-nWy7bt_iQtVRVS6a5-CH12ei6Um3sWwkzon-NFFlkLj_T_oxdneai7dd2om5de6o4Fro5TrD0g3E32ueag3nAb2_rULvyMot6YWfYyMUQgcGxXpQgPcv0aw0e9gDMniXdLCWOfl6gpv_D1ItlN9HWc3iwSnGeNgFo4q7ooxYZZ2Zw3ED2ctnpoBzIb7V9AZtNzaf8HjEwheM8U7X2pseWry6wR7CZM82IetS-fysJAaZuyM_8QeD4LSFnBhzP9LPj-xlOMyC6TNlOeCj9B0XKarW-wNVAAATndGH0NP3jwvv77De3HJRfK18bL6MavbMxLTjKjuIegJyPQz0vGlsev0k8-pVU2ScB5OCRTvgJ-HAzB1lujSvs39xAZekedfsFujwWKKuxcAXZncEbQ13iwS-N4Lfn7f2qppmlAyx47mbEhhlcjPL9B86hIH6Qs4qYb8XZnNbVcV0yXgYwpkaHB0Fykbq-qYDnmkhx6Umbs5A4Fq7qcTdCpej_ulvA4WnR2gPZVwejaoXJg7WIYZsmvyr80K26GooC0-qtql7dLr3qEbrHIZetGWUmikiN9IUhtRc08hprvIA3owI5-jgyEUBh_v_4PdSOOaq9nXmuFqKQ1-qv-TtZI1F3N1W0XNXyLAXGU7ay9gqSvfZ2D1-Ch5GtLBcai0HHdm9fWo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو استوری‌کرده بودم دیروز خیلی درخواست بالا بود که چنلم بزارم
❤️‍🩹
🙌🏾
@withyashar</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/withyashar/12555" target="_blank">📅 16:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12554">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/withyashar/12554" target="_blank">📅 16:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12553">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/withyashar/12553" target="_blank">📅 16:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12552">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer"><a href="https://t.me/withyashar/12552" target="_blank">📅 16:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12551">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مملکت دیونه خونس یکی پاشو میزاره رو شلنگ بعد اونیکی میکشه …
خواهیم دید چه خواهد شد</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/withyashar/12551" target="_blank">📅 16:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12550">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اینترنت بین الملل روی مخابرات کامل باز شده
@withyashar</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/12550" target="_blank">📅 15:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12549">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سایت دولتی سیتنا هم که ا‌ول خبر وصل شدن اینترنت رو پخش کرده بود فیلتر شد.
@withyashar</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/withyashar/12549" target="_blank">📅 15:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12548">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">️ایسنا خبری که مربوط به متصل شدن اینترنت بود رو پاک کرد
@withyashar</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/withyashar/12548" target="_blank">📅 15:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12547">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">موشتبی خامنه‌ای : اسرائیل 15 سال آینده رو نخواهد دید!
غدّه‌ی سرطانی اسرائیل به مراحل پایانی عمرش نزدیک شده و به فضل الهی و طبق آینده‌نگری 10 سال قبل پدرم، 25 سال بعد از اون تاریخ رو نخواهد دید، ان‌شاءالله.
@withyashar
😂</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/withyashar/12547" target="_blank">📅 15:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12546">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وزارت خارجه در بیانیه ای گفت:
نقض آتش‌بس توسط آمریکا بی‌پاسخ نمی‌ماند.
@withyashar</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/12546" target="_blank">📅 15:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12545">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">زمان انتخاب.pdf</div>
  <div class="tg-doc-extra">822.7 KB</div>
</div>
<a href="https://t.me/withyashar/12545" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کتاب «زمان انتخاب» نوشته
شاهزاده رضا پهلوی
این کتاب مصاحبه ای است که میشل تبمن با رضا پهلوی انجام داده، گفت و گویی است متفاوت، بدون تعارف و رودربایستی، و آگاهی رسان! در گفت و گوی مورد بحث، رضا پهلوی با نهایت صراحت پرسش های مطرح شده، پاسخ های مفصل و قاطع ارائه داده و اصول برنامه مبارزاتی و معیارهای استراتژیک خود را در مورد نظام حاکم بر ایران، وضعیت اپوزیسیون و بسیاری از مسائل منطقه و جهان، ارائه نموده است
🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/withyashar/12545" target="_blank">📅 14:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12544">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">معاون وزیر ارتباطات: دقایقی دیگر اولین دسترسی ها به اینترنت بین الملل ایجاد می شود و رفته رفته مرم شاهد بازگشایی تدریجی اینترنت خواهند بود و تا ۲۴ ساعت دیگر همه مردم به اینترنت بین الملل متصل می شوند./خبر آنلاین  @withyashar</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/withyashar/12544" target="_blank">📅 13:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12543">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ادعای آسوشیتدپرس:
ایالات متحده و ایران دیروز در مورد مسئله دارایی‌های بلوکه‌شده به تفاهم رسیدند.
میانجیگری قطر با موفقیت به تفاهم آمریکایی-ایرانی درباره «دارایی‌های بلوکه‌شده» منجر شد.
به احتمال زیاد ایالات متحده و ایران امروز توافقی را در مورد «دارایی‌های بلوکه‌شده» اعلام خواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/12543" target="_blank">📅 13:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12542">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6so18zb8kx7W69HjcSTV9hLcCfjjlosDs7ulCWhshm2OUew-5deTxL8NMImyg0W4RSCKKT7C63T3Dm4p8VZ91Dl22e3goTA6G8DYNmieP9NTWl70XaO6nDCY6peyduSPjxE8RKBYBfDq2Ubm_Jnss0vTxLfnt7HcSgCFDyoFwir0WpdFu_kFEigWKo6AowxNTCqKxLs7EGzvyD0KdJKy4xeXiwGzgEtlI78peC5SEbJh2UEiqW_twZyDiorPYall7CIPvFfxb_-9KOf0IosdJigHJhCnYC04yB50mVMO0nbK1mHV2hMV70bgeVjdBgGTk3vHhJU9QlIcIuX1mo_Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : «رئیسِ معامله‌گرها، به ترامپ اعتماد کنید»
@withyashar</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/withyashar/12542" target="_blank">📅 13:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12541">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RecOrA9DjlPg4c3zdU_7HuttqxLIEQ2ykljOP5_D3MNXzGdXjmUvUIvA-MGmR4ggCbgY_kaaBREiyNKplSTsWo4_AmT2jf2IKeXF9B853PbYHXn21IRtL0bdZNugg7l9YXFgez3Rv0XvmVWX1p-4Vh-SNHpkhzANwqjDVR6MxANbANx6JOtIvr-6BMb4XhP8zZ3nkiFm480DIs1RKBDrWM46Z9oScwhwuA4NmE0_2YsEAR3VWvrc-zAtF5H5EIESxUTfAGbQq2hbYbdyiqLCPdLPj2TMg-KDbSaj0TWwGLQTVK_oYdz5PHGO8otCAaqQFDtWbJSUQDfOC4s2y7NqPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : توافق اوباما با ایران , مقدار عظیمی پول فرستاد تا خیانتِ برنامهٔ هسته‌ای را تأمین مالی کند.
@withyashar</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/withyashar/12541" target="_blank">📅 13:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12540">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">معاون وزیر ارتباطات: دقایقی دیگر اولین دسترسی ها به اینترنت بین الملل ایجاد می شود و رفته رفته مرم شاهد بازگشایی تدریجی اینترنت خواهند بود و تا ۲۴ ساعت دیگر همه مردم به اینترنت بین الملل متصل می شوند./خبر آنلاین
@withyashar</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/12540" target="_blank">📅 13:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12539">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خبر خوب</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/withyashar/12539" target="_blank">📅 13:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12538">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/withyashar/12538" target="_blank">📅 13:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12537">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA.sh</strong></div>
<div class="tg-text">داداش انرژی که واسه انتقاد از ادمای بی لول میزاری به جاش بیرون یه قهوه بزن یه چرخی بزن هوایی عوض کن بعد بیا اخبارتو چک کن به زندگیم برس ما ایرانی جماعت کلا ادعای فهمیدنمون میشه و تو همه چی میخوایم نظر بدیم
بخدا اروپایی من ندیدم بگه همه چی میدونم یعنی تو ۹۰درصد مواقع بدونن هم میگن اطلاعی ندارم اما ما کلا همه چی بلدیم کوتاهم نمیایم
برای همینه یا تند میریم یا کلا یه جا بی حرکت می ایستیم این خصوصیت</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/12537" target="_blank">📅 13:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12536">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سپاه: حق پاسخ به حمله دیشب امریکایی رو برای خود محفوظ نگه میداریم
@withyashar</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/withyashar/12536" target="_blank">📅 13:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12535">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">@withyashar
جنبش صهیونیسم</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/withyashar/12535" target="_blank">📅 12:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12534">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">منبعی آگاه به «اتاق جنگ با یاشار» گفت که در شروط توافق این مورد تأکیید شده که ترامپ باید ختنه کند.
🤣
@withyashar</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/withyashar/12534" target="_blank">📅 12:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12533">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">@withyashar
ماجرای ری اکشن</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/12533" target="_blank">📅 12:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12532">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/12532" target="_blank">📅 12:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12531">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">فارس  :
امشب ساعت ۲۱؛ ملت ایران فریاد «الله‌اکبر» سر می‌دهند
@withyashar
ای کپی کارای کثیف پس ما هم با جواید شاه میشوریم میبریمش ! من قبلش‌اعلام مانور دادم
😐
😂</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/withyashar/12531" target="_blank">📅 12:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12530">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اتاق جنگ با یاشار : از امشب ، برای فراخوان اینترنتی ( ارتباط باشاهزاده و شنیده شدن صدای ما ) در دوشنبه دیگه هر‌شب مانور میریم و تقسیم وظایف میکنیم !
💥</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/12530" target="_blank">📅 12:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12527">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کابینه امنیتی اسرائیل امروز تشکیل می‌شود
کانال ۱۳ رژیم اسرائیل گزارش داد که کابینه امنیتی رژیم اسرائیل عصر امروز در ساعت ۱۹:۰۰ به وقت محلی تشکیل می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/12527" target="_blank">📅 12:11 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12526">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یک منبع آگاه اسرائیلی روز سه‌شنبه اعلام کرد که ارتش اسرائیل در روزهای آینده خود را برای گسترش عملیات‌ها و حملات هوایی در لبنان آماده می‌کند. سی‌ان‌ان : این منبع تأکید کرد تحرکات نظامی اسرائیلی قریب‌الوقوع «با هماهنگی ایالات متحده» انجام می‌شود. @withyashar</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/12526" target="_blank">📅 12:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12525">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">@withyashar این پست به درخواست شما منتشر میشود</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/withyashar/12525" target="_blank">📅 12:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12524">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tj3Eb-2N4oAdbic7vLPfw3ZogO2urCsITRhaU_yENQmzkZRo5zPnqH8ba-sIuwiOSMkDDlEWD46eYTh1SJCvLn2Oz8bSKgjTBCT_eHA_pR_j_7alKBrysMxuGmGA0BXVIaLB_xGIm87AT-TRhwWvYWoMx16V52zL45haVkEZ49m1iI_NhwfX8HYwiQFL6V4O3C7gtx7N93EKEIKxH-KJCj_hEtDyin5sBZsR8Fw7dJDr__6Az-HNSu5J40A7tYA9OtUgizDqLv2Ffc8KENvjrfxC8LohUXEY0RGFtP-Y9HYlC1kSDNmQpF0p_6rcb7bKsN9kDmcYuSmGtVDxM9nspw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید علی کریمی
@withyashar
یاشار : کاری با انتقاد ندارم ولی ایشون باید راهشو از پشمک نادان جدا کنه…</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/withyashar/12524" target="_blank">📅 11:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12523">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سخنگوی وزارت خارجه قطر: اینکه گفتن قطر 12 میلیارد دلار از پول‌های بلوکه شده ایران رو قراره پرداخت کنه کاملا کذبه و از این خبرا نیست! @withyashar</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/12523" target="_blank">📅 11:55 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
