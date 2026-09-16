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
<img src="https://cdn4.telesco.pe/file/O3qqrC_VM5RdPJcUjat4xUugGxfuysmQvU1ou6z5q1gHTt_1Y5B8vGHxlxocbX05x7GXzNNlcOk9oU-64XOe2ebxHeaSscWf03NmPrujQWo7UuMbraMDhOSlWlg6EhKyiZT7Wct-9UK1Z05Sj6zlqWCN5F4X-jQQAdo9lFqcLH18mKrfIFAep6bhJfiAmCXprVMd1dnLIgBLqczxYc8b_t18W3QlkUpaHS7FqmRDrqgJop__ywuWgytNogpcSCBSwdqt99a-uBTU1eo5YagceRxGUg5V-5Dl0T1U5h9ea_9oDhOxdC6obm71T4AnKwaWPpVK4stsm2GrA2mPB0Mfzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 18:42:55</div>
<hr>

<div class="tg-post" id="msg-462488">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19a56430d0.mp4?token=aRejoE4XwQ0j7m1EstZ87glOQOpu8ZpaUvdTeELmI2xnRapxvd24j3Hi2BXJiO6D8OOb0EkDOw0N0_WQ4E3BeMNmGwIHSjt83O3cj0_cnckf374HJS9tF4ksFta8412tvC0lWj1Oiwo8KchiTtJTZVEInThfZqD64kMWrDst06WLqKc5Ajjwv053Zi6OTdtyhMAKqvU7pjL-Sq-ck3xKOSW4NUGzyr6HNdDj_m_0EE7vf_yYAiFEntn7INa6SNZBhNmzuHl7Gd5Z8kbWW_R5lhA3HxoK3o9jZU-af17Nv-AleYq8N56rM6ALiAaWUoCiV7td-4jtWN-2h9WkggEDtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19a56430d0.mp4?token=aRejoE4XwQ0j7m1EstZ87glOQOpu8ZpaUvdTeELmI2xnRapxvd24j3Hi2BXJiO6D8OOb0EkDOw0N0_WQ4E3BeMNmGwIHSjt83O3cj0_cnckf374HJS9tF4ksFta8412tvC0lWj1Oiwo8KchiTtJTZVEInThfZqD64kMWrDst06WLqKc5Ajjwv053Zi6OTdtyhMAKqvU7pjL-Sq-ck3xKOSW4NUGzyr6HNdDj_m_0EE7vf_yYAiFEntn7INa6SNZBhNmzuHl7Gd5Z8kbWW_R5lhA3HxoK3o9jZU-af17Nv-AleYq8N56rM6ALiAaWUoCiV7td-4jtWN-2h9WkggEDtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پویانمایی لگویی دربارۀ پیروزی‌های جدید یمن
@Farsna</div>
<div class="tg-footer">👁️ 378 · <a href="https://t.me/farsna/462488" target="_blank">📅 18:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462487">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRD-nOB_XaqWTxpIRR3QUyR6YlnEL-4y43hMjXM92UI9v_AxDsE9H5jPt9EAByK5-jcSfbqaua4qPxbTonuNY-c48DC2oDKxxFQrM5F-RVc38KcLGA352e2Z7DU6sjlY9xg4sbJEr1uRLssx7dlGnHbSM5QuaNue75mKwzFbkFYWT48MxdCzrTh4H4F-WCNmIFcudhZyRVNCmkiO339jKhm4wXUyaAu0jwXacAkmXuMUyUNhPbOkJf-O78vqdhjVsO1U_5NW2jBzWECdjSaLQ0OqdvY1ubiiKI-pr057DjZjpinZS9QlpA7PEl6-67vaCTRifdTNwNvdSOl8Jni7iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمز بلای صنعت اروپا به اعتراف رئیس کمیسیون اروپا
🔹
فون در لاین، رئیس کمیسیون اروپا: از زمان آغاز درگیری در تنگهٔ هرمز، اتحادیهٔ اروپا ۹۰ میلیارد یورو (حدود ۱۰۴ میلیارد دلار) هزینهٔ اضافی برای واردات سوخت‌های فسیلی متحمل شده است.
🔹
این وضعیت بار دیگر نشان داد وابستگی کلی اروپا به سوخت‌های فسیلی وارداتی چقدر پرهزینه است؛ اگر قیمت انرژی به‌طور ساختاری بسیار بالا باقی بماند، اروپا نمی‌تواند به‌عنوان یک قدرت صنعتی باقی بماند.
🔸
بر اساس داده‌های پیشین کمیسیون اروپا، هزینه‌های اضافی انرژی این اتحادیه در ۴۴ روز اول درگیری حدود ۲۲ میلیارد یورو بود و تا اواخر آوریل به بیش از ۲۷ میلیارد یورو رسید. کمیسیون اروپا در ۱۳ ژوئیه این رقم را حدود ۵۳ میلیارد یورو اعلام کرده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/farsna/462487" target="_blank">📅 18:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462486">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WiIVBq8yGjZ6L2z3ii2fOFV5N9OOSFmjkgxhqw3Lj1DNsNwnx-i5J_qndNcAXW2s2lYCNgRi0mmmOTFq8JtNIIzUiBaa2MI-keadVtrK8fek7bFoac5_h4OthJsJY6-Ekn9H91Dn_08Ju2MBOlvlCMIPrXQIXT0Z-ff4dJrTjQf3nw2Asi08IBPhVYhJi6MoQT0LKIdysqMS3dRJgOOSheF1NWtKsPwxmgW3QL4PRM2fZb3NKs_7kOtIhGITA-LIPtz6OSe2RrVY42_MPee1O73qGao_RhgF2LiND612_aMhKR_IECry-BxXZwvTI7EfHSa547oQSrvSnXqq9cTptQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قائمیان: نتوانستیم جنگ ۱۲ روزه و رمضان را آن‌گونه که باید روایت کنیم
🔹
فرهاد قائمیان، بازیگر سینما و تلویزیون، با تأکید بر ظرفیت هنر برای روایت وقایع جنگ‌های اخیر گفت: این رسانه عظیم باید برای انقلاب و مملکت فعالیت کند، اما ما نتوانستیم اتفاقات جنگ ۱۲ روزه و جنگ رمضان را آن‌گونه که باید در مجامع بین‌المللی روایت کنیم.
🔹
هنر در دوره‌های مختلف تاریخی تنها ابزاری برای سرگرمی نبوده و همواره یکی از مهم‌ترین بسترها برای ثبت و انتقال تجربه‌های جمعی جوامع به شمار رفته است.
🔹
در همین راستا، فرهاد قائمیان بازیگر سینما و تلویزیون، درباره مسئولیت هنر در شرایط فعلی و نقش هنرمندان در دوران جنگ و پس از جنگ در گفت‌وگو با خبرنگار فارس، اظهار کرد: واقعیت این است که در رابطه با همین مسئله، باید اتفاقی بیفتد که بتوانیم برای نسل بعدی و حتی الان، در وضعیت فعلی، فرهنگ‌سازی کنیم
@Farsnart
_
link</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/farsna/462486" target="_blank">📅 18:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462485">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۳۵.pdf</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/farsna/462485" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۳۴.pdf</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/farsna/462485" target="_blank">📅 18:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462484">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یارانۀ شهریور دهک‌های ۱ تا ۳ واریز شد
🔹
یارانۀ ۴۰۰ هزار تومانی دهک‌های ۱ تا ۳ به حساب سرپرستان خانوار واریز شد.
@Farsna</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/farsna/462484" target="_blank">📅 18:14 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462478">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9ni-QI3UjuLSi4AuJwBJ7YUm9Z8DBPlY1SY_Y1ht_ylHng76nuHLwHzcd3uRK-nUQPtyUBCApaxPc4H2qOzUj_gPTTfmvIWpKynKb_rkoAcH_Rt-qNfA3JEB38v6gp5DycSxuVLgQsIAAGNzNTl8bsMoBCvNh4jIa-x38OFcdZRMD7hKje1BHB2pq5-Knfmr0c4-OFwYtCAM5Toe27NpKu-Tn6qpoyHLCD_2AIZwPG7LSynNUswmQSf0Sjt8Bns7YJQhEVEov8kBCZk7hfjp7yzO-LG3JkoJDLdQEysYxkCfHMm7oEmjq9yoA_MzttmiL1bfxO1tG8yeihe-xzjJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصاویری از لاشۀ جنگندۀ اف۱۵ سعودی ساقط شده توسط یمنی‌ها  @Farsna</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/farsna/462478" target="_blank">📅 18:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462477">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d59ddcc549.mp4?token=qI5HyMYk-JqeRq_EJRBqMtaxZc5_OXs7AapGWqsBeelT6tE0Gyl8F-FrMfNlJi7RFnUbwjCM4RxD6G-kO8M4Yg1-Cv9uT2hmGyk4lQtvsEAKhgsfcfJKJENjGCzHVZcCVlIEwTuct7iNxXHvGfORqj6KMN_-N54CnLtfIZ9tsoye368x495iX_xMLGcUrWSlqAaMl5hZMvDZTy8nDSVnU1gygwZRSsNC9VpMUyj_-alI5APrV8RNoUIEDv_sr2UTI4v38FE43M7BC9Fk2PBOp5GC6dd9tkM1zFUkwSwpc3hIAwWqsXRpv1TrPKvtV9-LCI0n1ENhKQXAjqSgXR543TJzWO0AGdrVgF6Zui1pF6kpuiM-q27Zv900SscnUonojrypjPzTaPG5E-6-z0lEZ_At8hxjwy1VPkendDLuYmQs0c58KibLBTJQ1v2hvY9Sy-_TuYKDjykhjrj3ion5xwYYufGZtCZMY0O0qZdOSByWE3F8nc9FLr9UNUV0XkReqUr2C6ZOSdNcp9zsBY-8vKA8HQNq6xUkvQ1RzNnmFrjMaFYKRNbev7TALNTmEiCjBlgmzEkUJ4USkBCEr4-zzNK2B4We5iaEliwyR-7H-Fg4ux9lafcKf8SnImBktF43_Pel61r6yHonQPLgU-4SsV85cB0RCBdxoVthHVxvIL0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d59ddcc549.mp4?token=qI5HyMYk-JqeRq_EJRBqMtaxZc5_OXs7AapGWqsBeelT6tE0Gyl8F-FrMfNlJi7RFnUbwjCM4RxD6G-kO8M4Yg1-Cv9uT2hmGyk4lQtvsEAKhgsfcfJKJENjGCzHVZcCVlIEwTuct7iNxXHvGfORqj6KMN_-N54CnLtfIZ9tsoye368x495iX_xMLGcUrWSlqAaMl5hZMvDZTy8nDSVnU1gygwZRSsNC9VpMUyj_-alI5APrV8RNoUIEDv_sr2UTI4v38FE43M7BC9Fk2PBOp5GC6dd9tkM1zFUkwSwpc3hIAwWqsXRpv1TrPKvtV9-LCI0n1ENhKQXAjqSgXR543TJzWO0AGdrVgF6Zui1pF6kpuiM-q27Zv900SscnUonojrypjPzTaPG5E-6-z0lEZ_At8hxjwy1VPkendDLuYmQs0c58KibLBTJQ1v2hvY9Sy-_TuYKDjykhjrj3ion5xwYYufGZtCZMY0O0qZdOSByWE3F8nc9FLr9UNUV0XkReqUr2C6ZOSdNcp9zsBY-8vKA8HQNq6xUkvQ1RzNnmFrjMaFYKRNbev7TALNTmEiCjBlgmzEkUJ4USkBCEr4-zzNK2B4We5iaEliwyR-7H-Fg4ux9lafcKf8SnImBktF43_Pel61r6yHonQPLgU-4SsV85cB0RCBdxoVthHVxvIL0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر شرکت توانیر: حداقل ۶ ماه حبس در انتظار اسخراج کنندگان غیرمجاز رمزارز خواهد بود
🔹
طبق ابلاغیه وزارت نیرو، محل کشف‌شده از برق یارانه‌ای محروم و به مدت یک سال باید تعرفه آزاد پرداخت کند. @Farsna</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/farsna/462477" target="_blank">📅 18:00 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462470">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pbp1QEK5C1QHKkNXs-CBPiW-eAWX5GVouw13CatgTOrolEJDs4n5ahIiVVFZTSwYrjXVjC5RqeWx7B-Lwpn84Uk-cz90GAQoQTFATcFuWBtYt2Zf4KPEgpAuiybAwmnfkuCXnQTFl-vZSzh4ze1gObsNUfNGI9b6SSbba9hgjD0BpctdsfArBnr1OZff13E9F9v52MIjwpikZLOZmpQgJGDVvPwKIgxgVRuFi-dJl4aGm9_z5d2ElOsNNRKfYgIIgPyePqbypedffpINjQHtZclMjJMZe3IitsmNf9bG4eCO7TvTPjr5duMPBdSIpy5lkp89EqAJOI5uZHg8d39KZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eGR2OwJCxEeZPCCxuw9B2GobP7velspDg1YIIh6D_xh4crU5RBTV3b1lmn66X2pZBncXAyGhN7gJofAn_RhHjZKEI_1xu_y_l99xz8w_xpVLFp-3BUUdzMoVyDenZJ5-_FFjBx6Mj_5hCS_MCyr7EDmsrT2mZhyWW5GjE_VuovCwXQ99MvnZQWcN_nu-tgaTLdvHpydfyQmuZwtzHKpu5loJcVCi_NMtEFKjfy4oA-bUCgOeJGQClbiagVVxW34x3-45ChtM6ifWkMGGSdOQQi5NJweD7PQ_LLtFAzLxtYNfgYVnRO_q2QmRGhLh8p2uTaApLPET6afJ44MMohLpEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dyUxVJKMEAwuTygalD1qsLpDWKIKg23w6lx4ydrsDuhBgHFMdgAeAFKjAXOj8L5NWq39yJBGvSBaRd9XCO3UtBh6EIvB0dj9cGs3QWkxERbUCPZh9y33qSwfIKR7LfMVgRNN92Uhh7njFxqEQRS-CkFTP80KzxaJX41XpbCZwNblGmPZVCSzCVqmxb6VOA4zmaU42yWmA7X393NiA0geC-0aE-V3oIOMquQbyo-0a5b02vEaceS-i6r8oC_dWeUhlpcD2CaQPUJxf2n2DqYPmyBcp6UEaKDCUOETJS7buHEPcCc6Z4rCNVbdow8hRJk0ZrpTdXTNGU-L5Mzl6oAu8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QtCWRXHVUKGbR6yQcgq_hm8Z47eXs_WNfp-G3wD6QBeM5X8JHmn53GaDifglqICiY7wCgtxX2BlV6WXjTaISAv0EOh5i63R53fI1mFzGXUZ7kvGtFrqiLsFNaHqkxzZJ6aMfpHX16ChWiX6JD1eLvmfyo94MS8-lJZOG203JKGrLUIETKEahMGSnj6WjJvUnxwwb-zDHucIYbhMW_EJi6WrXXZ636kG-vSvefzJl8-y8TnDJhZuIlp2kQLK_DQQV2s8oMxjhL7BCZ1hUaNC3fraTaU_2MEVxyrtqxUfr2yljFCkXW3QouaaPjfluzcDRNGs8H34V9ADXaBGvaNr1GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bD0YCkvcygHJX-F9aYscbb7VAlr3MtiW4usM6uH-uygBT79ijmmrGW8UvE-ffn5DJxXRsKqmLkbOvBtajEAvuaEDKkq87p6Dd1cds5jUeqlf1a2xzrjKAVZ_H_KboeUsAPPRO7bV8cQIauslRpUPgjeuIkV3CLZzAUR_2enF_fveGWu4OT_vgf2iwfYWbBr7tw0JUcDVZ3Zf7FHL6TPURIaQ_WHCF2NlZ5iHiXkb5AQlRm4rKZ4CvI52JtEjTi-FiWU3uv-PiZW3tN38kHgrVmutcpfNf7T2uxTYwaC74KvWXqv04W5FIJoGDgS9m5tPdrVzidSlsKPRZbJsEoiSKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/edpL7R9Mxpu69Oi-Wfhmb4n2AJ2QlIA4kwU3I8cmsKFcQSnvE6-KjPZgToHWZJL2NSqy0Zs5IBKkL5GYbX4OP1IKzKep81afb0fXGz6iy2uPka2pPw7H13fJMVzHp-fevKqqQZTPJvzsDxeOn-ky22KNfvHVlVzX1eEqhflbV5-Uxe3sx3f4hvrakooZ-rYH5TkER8Fnlt7WpxnAcP_yTAAOLF1qjaMpYhoWuYX-qES3balVOPjlw8cPVomSgL7fL_D4NLGBuoTBDD774krB0LzsT8bD_IKBNKMz5dc9GurL__yIWvw7bFPNUZiEOm4CbuaSKPctbD1-QoGmdTFl3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/knfLLwAYwziRHU2ZYrJod_9GxEeqqCvfzhEQe_DgVn9JaLIj5NKBZVeAcD7y0xYKOIerejc6kFKPjKrLggs2tc14Bgsll4FR_AYkQdKaSIXBxXv-jQl0njvH6VFiXb5v-xCaR1LLYgdxyUaJursB5MIRYQcropbC2vN1D2LjMHrMOxXeqUJCqipwEuWVPfGuGBwu4JAFPhc8_S9mI3sF-KYGPOs-gMQI4AN_L2XOyaL9AoZ21yZtVeLHkvj8szvATTZ4oy9_p5vTVSSe3eSDwvEixNve3TGlYCQMBkcNAOM-uRef41A0GMUft_sQus4xEv9LB5ERiJkiUuYWzIFBMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
تصاویر سرنگون‌شدن اف-۱۵ سعودی توسط یمنی‌ها  @Farsna</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/farsna/462470" target="_blank">📅 17:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462469">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مدرسه‌ای که قابش از کلاس درس به رقص و قمار رسید
🔹
انتشار ویدیویی از صفحه رسمی دبیرستان غیردولتی «صعود» شهرکرد، حاشیه‌ساز شده است؛ ویدیویی که در آن صحنه‌هایی از رقص، بلاگری و استفاده از ابزارهای قمار در فضای مدرسه دیده می‌شود.
🔹
این تصاویر این سؤال را ایجاد…</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/farsna/462469" target="_blank">📅 17:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462461">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/438df848a9.mp4?token=go4miVcsi51CwJ1_5Lneg-NIkZyRcmRmjoGNYpK_N7CQhCkDzPotG6dEI0vYefW3Ak9K2WEZ7KbgIwfmLBji4si7mep2VoOV225Dq-cUnL_rVg5lLiiK51PQ_oFkVsW4EgKf7w6LKM4iwO_nTVXX7M5qeNkkzqif8nAjd3DjjmKDu4gh_HkLGKDJnVje5KegFpn44czK0eNLA_aG-k0iX91lnkWIuPyrYGfAJUtDbxU3-QcsXmxI8EpRRYdLzFHCEs4Lmhl_aHK1nVRNGdw6sapqWTgSCOic7-MnfFrvWMVpj3gT3WEG9IgYneO7tA2UH_uw8ONjAu4in2tTyOmOOxAwdoQBA6y95f-6i9pgJ2XXcumu0fWjdv9gqwXyyibh4Xrlwtsbyo86T_oF27mbKxtZTIp6y06Dc1RDneu2q-wnE12xz8jVOJKMGaYLtbOVGlUHbjs26u91KvWgYzTwvDRjs_qRAenBdAGiwPDFGDdIfabz34qa5Xf7xxAgTIRP_EXA8ZG1jrRbsml_MWo3HHq5VbX_aofAHbJ81__ITy2XZ7TSxf9jHCqXEYUPLIC4hN2Gb_IRNGiSZKGqQ4HHVfVKEdH9DaBPu28pKyWVPxsSjkeZG6BrcMt-qjS1rsZV_zyawLd1lsD2QREK4RUFzjgxOU_mDzgyDz2WSTmca0U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/438df848a9.mp4?token=go4miVcsi51CwJ1_5Lneg-NIkZyRcmRmjoGNYpK_N7CQhCkDzPotG6dEI0vYefW3Ak9K2WEZ7KbgIwfmLBji4si7mep2VoOV225Dq-cUnL_rVg5lLiiK51PQ_oFkVsW4EgKf7w6LKM4iwO_nTVXX7M5qeNkkzqif8nAjd3DjjmKDu4gh_HkLGKDJnVje5KegFpn44czK0eNLA_aG-k0iX91lnkWIuPyrYGfAJUtDbxU3-QcsXmxI8EpRRYdLzFHCEs4Lmhl_aHK1nVRNGdw6sapqWTgSCOic7-MnfFrvWMVpj3gT3WEG9IgYneO7tA2UH_uw8ONjAu4in2tTyOmOOxAwdoQBA6y95f-6i9pgJ2XXcumu0fWjdv9gqwXyyibh4Xrlwtsbyo86T_oF27mbKxtZTIp6y06Dc1RDneu2q-wnE12xz8jVOJKMGaYLtbOVGlUHbjs26u91KvWgYzTwvDRjs_qRAenBdAGiwPDFGDdIfabz34qa5Xf7xxAgTIRP_EXA8ZG1jrRbsml_MWo3HHq5VbX_aofAHbJ81__ITy2XZ7TSxf9jHCqXEYUPLIC4hN2Gb_IRNGiSZKGqQ4HHVfVKEdH9DaBPu28pKyWVPxsSjkeZG6BrcMt-qjS1rsZV_zyawLd1lsD2QREK4RUFzjgxOU_mDzgyDz2WSTmca0U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: اف-۱۵ سعودی را در آسمان مأرب سرنگون کردیم
🔹
یحیی سریع: در مواجهه تجاوزات وحشیانهٔ جنگنده‌های سعودی به کشور و مردم ما، نیروهای مسلح یمن با کمک و فضل خداوند، موفق به سرنگون‌کردن یک جنگندهٔ اف-۱۵ سعودی حین انجام عملیات خصمانه در آسمان…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/farsna/462461" target="_blank">📅 17:48 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462460">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgts4IKoDOdUVwHoKjBALdCAN41Jnwiwt2ijKu9odDoQBHEt5wbbMpwB3qU2O-ZMZtFuEQLWrxGLzamhDWGBNmC75XWriBVYge-gN---SoMegWp7bU3gxGhCGxl8u35HEC6KfP-LWvMfqzYYJh6RDodmN7cLos_5BlC5mT3c5zzCsj0bAlVwyalCyEsloZX32Zj9Ii_27dTQVPmZQ7yQftItIXyiYFA5GeDmO0_76wNigFx43XgDjS07blIEB8EBcfPeip4EGaAROVzEpp-U05nW-nbbChvmHZt5SggglBgOb4DXa7yfuf7Su_zjSZYwze2XFFASYFIaagftbXnnrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقایی: آلمان نمی‌تواند آشکارا از «کار کثیف» پشتیبانی کند و سپس خود را قهرمان صلح و معلم اخلاق جا بزند
🔹
سخنگوی وزارت خارجه در واکنش به ادعاها و اتهامات صدر اعظم آلمان علیه ایران نوشت: صدراعظم آلمان از جنگ ایران، برنامه هسته‌ای نظامی آن و نیابتی‌های ایران سخن می‌گوید.
🔹
این، یک روایت کاملا تحریف‌شده است. این آمریکا و رژیم صهیونیستی بود، نه ایران، که جنگ تجاوزکارانه را آغاز کرد. آلمان حتی از حداقل شجاعت اخلاقی لازم برای محکوم کردن این عمل تجاوز هم برخوردار نبود.
🔹
مردمانی که برلین نیابتی می‌نامد کنشگران مستقلی هستند با آرمان‌ها و محاسبات روشن خودشان. آن‌ها برای حق تعیین سرنوشت، آزادی و کرامت در برابر اشغال و سیطره‌طلبی می‌جنگند.
🔹
ایران هیچ برنامه هسته‌ای نظامی ندارد، ولو این دروغ بزرگ ساخت اسرائیل را بارها تکرار کنید.
🔹
منطقه ما نباید بهای احساس گناه آلمان یا عادتش به تمکین در برابر قلدرها را بپردازد.
@Farsna</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/farsna/462460" target="_blank">📅 17:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462459">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a090c47eb.mp4?token=TC7ZOFfQEIGKT0sQk3z2HzjnS4y95t1pr7XhNgPY5zrUiMznwwH5zNdn-Nc8AG_rlKuc98kl3u9PaHSdxTkaywsH9XB7P9yOd3ufHcNmWzXTy2QsVQsvgdh5KDibE1NIoKXHi3yBbEs5u0q6q8iwSlu6PYWryYLE1kqzs3I67LwcaTEQObxldJF4-1sjm6iXxcjEwcFzF94dFdrOwNv0ijjeNZj5i-qdmwCFCnj8bJCTDUTjYpHkWzWyrGuVjuFpQI6FqPHg5KWaP_dlBRpNak8bD04pl7evLnjqWYTyUduFIjYoMhC7xxSbATq21eL-hJvq4p6qfiVbkeGyMMmTNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a090c47eb.mp4?token=TC7ZOFfQEIGKT0sQk3z2HzjnS4y95t1pr7XhNgPY5zrUiMznwwH5zNdn-Nc8AG_rlKuc98kl3u9PaHSdxTkaywsH9XB7P9yOd3ufHcNmWzXTy2QsVQsvgdh5KDibE1NIoKXHi3yBbEs5u0q6q8iwSlu6PYWryYLE1kqzs3I67LwcaTEQObxldJF4-1sjm6iXxcjEwcFzF94dFdrOwNv0ijjeNZj5i-qdmwCFCnj8bJCTDUTjYpHkWzWyrGuVjuFpQI6FqPHg5KWaP_dlBRpNak8bD04pl7evLnjqWYTyUduFIjYoMhC7xxSbATq21eL-hJvq4p6qfiVbkeGyMMmTNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مالکان ماینرهای غیرمجاز یک سال برق یارانه‌ای ندارند
🔹
مدیرعامل توانیر: با دستور وزیر نیرو از ۴ شهریور امسال، دارندگان دستگاه‌های غیرمجاز استخراج رمزارز تا یک سال از برق یارانه‌ای محروم و تعرفۀ برق آنها تا یک سال با هزینۀ واقعی برق محاسبه می‌شود.
🔹
مردم…</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/farsna/462459" target="_blank">📅 17:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462457">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac83f5d453.mp4?token=hyg93MUdc-Nbzk3aWiNoTkrhAiCx0gBLWE6UUmCjldid4qUoLGBvHdMx3bo8C06dh6yLli9Rk-rT3FjsTAMAiiJLqgdIHCDLfyjZIn6wSUckFnUnrCiUokLUGlXG2Lu4xpwXro5naFw2xHWrS-0rvHVCqAafk7c4j6Vov-CT5fJCVdAQKOVnNY01_DWqDxXk6M8dyfNeahRO8NVg7DG8UB1UbVjJJnvLXSkqcmuv1Kkv4LyBAM88yrj36zrvvJ0mvUWWMvIZy56gFgRBwimaA7edkdE4IkjpPU13NntJ3rNx4FiDX2R4ZsX_iT4cmDnELlieOGtPjlV4O6StjLx_17lz3_zKDbLsg4nyCPMPBolpPehXp8hKjIBE08JzIQ9IpSb5RDuyblhkYstHYJOrvOWjiDQBCUrgi6fIALID8gLCys9v6mzNnqf1XTze8X9UXEDYFwwSelupw5hwFz1KQcEpj25avZ05HKrSUHKcQZCC24XgY_bIKeCMdoYrks7I4zFFLVKkCGSZ0W4f74JuHTPshSe9_6rW4AkP8KZOBb7RmV5eqgUO1U2vUQWbRseaDTnEYM7OTLkqHIhsgy3Xss-pEe_l2YnAX41xr7t3RMZHz3mUolaNiZ5swo7I64fZiqqzGjABzSIK0QWsBHdGYT2jW4ZVL_DIdhFtV4bnH5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac83f5d453.mp4?token=hyg93MUdc-Nbzk3aWiNoTkrhAiCx0gBLWE6UUmCjldid4qUoLGBvHdMx3bo8C06dh6yLli9Rk-rT3FjsTAMAiiJLqgdIHCDLfyjZIn6wSUckFnUnrCiUokLUGlXG2Lu4xpwXro5naFw2xHWrS-0rvHVCqAafk7c4j6Vov-CT5fJCVdAQKOVnNY01_DWqDxXk6M8dyfNeahRO8NVg7DG8UB1UbVjJJnvLXSkqcmuv1Kkv4LyBAM88yrj36zrvvJ0mvUWWMvIZy56gFgRBwimaA7edkdE4IkjpPU13NntJ3rNx4FiDX2R4ZsX_iT4cmDnELlieOGtPjlV4O6StjLx_17lz3_zKDbLsg4nyCPMPBolpPehXp8hKjIBE08JzIQ9IpSb5RDuyblhkYstHYJOrvOWjiDQBCUrgi6fIALID8gLCys9v6mzNnqf1XTze8X9UXEDYFwwSelupw5hwFz1KQcEpj25avZ05HKrSUHKcQZCC24XgY_bIKeCMdoYrks7I4zFFLVKkCGSZ0W4f74JuHTPshSe9_6rW4AkP8KZOBb7RmV5eqgUO1U2vUQWbRseaDTnEYM7OTLkqHIhsgy3Xss-pEe_l2YnAX41xr7t3RMZHz3mUolaNiZ5swo7I64fZiqqzGjABzSIK0QWsBHdGYT2jW4ZVL_DIdhFtV4bnH5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطرهٔ قهرمان پارالمپیک از رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/farsna/462457" target="_blank">📅 17:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462454">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hw_PrYnrH9U0tAdHTUpNGwYKnPMYdNWuGlZ5YdA64Uucjtck0d6YphqKlmARgMQB0Egu7ZBIgU1rBkpKKYbjqGeZbtQ4J9VBwn4nnC9m1No4ABBikCPE5c3EZ81632DhUMXJeL30-uLa9qSp3dcmYPZGojUJtf_hBwL7y7bP70Q2wAqnoqF5rFae5FVFQHvgdPitX9W6GuFxDwAAHLNo3LKLdJjBAT1DV1M7QpoW-3pIyf5Is9ly36MZP6ifjCHzuRKmEntBlKLe-L_sdIN2R7zuSlpq-7OsJeMsVpSjHXZhp1oaR4Sd1Keat-P-26tLtNolvjoLsr113wbUvc2m6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YD8N0u6dVtEjVZhCgk_S7qg1TqucC2VwrTem1Nn6dq-nsfwSia8UaNDM67d0x0j6JegKNm7t-LFOQvcFOGKX_kiQjzCvg9tuvWGKpBV6DXHZsAfi3kB_tS3SmFKRD0287xYEI_AmLXz1_l5WYnGE2COXJSuuO5BdfOMbOyVsAr8vlUo9kcZmjLT3t5HlkzogH9Vx10suv5M_UWbou00r__hDUq6FR43ydraXuDw64Ltl_d2rzoIRRGSzrroAW_LguG97_GHhf3lNnCbVIlKdK99s2X3Uo1gq5CzMkjVmKddwMvDZi2QLBd7ATXECFVebAfQ3kA6vuV6xGuGE3qsCrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qDOd96SGHPCznR33JYaQI2-_rdyiPRGRb8DQA5tIeyCI9OKLhKruSE5Ie8ocAT_Euyveb7zQniSY8QRmkRTFpPPhifPo1Q5HvP0dFmOKd0oW0OvbeloteE5FejK1QN92iPZm8L-b3wtKi-gQuu41MtlmOO-lO5tCQoxuU4F4AzxwHlJJHT4AoWFtGR_z59Wm7BJWJjrGx7wx9HwmIdK9BrOIcHOjfFFnrsDHEfdAGR1zlr4KqbQZNgnx_vx4l0hZe5YlpKevXpNiL577TbYRdZWgIclsIyzBfbkDbTAYv5cgKlKYbybxLP1k3gDqOenmnFYMQuXLznbbUC8tn1W7ZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیدار رئیس اتحادیه میهنی کردستان عراق با پزشکیان
@Farsna</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/farsna/462454" target="_blank">📅 17:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462449">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LQ18vBq--8f8h0jJj2CKp4FzryffQHUu0aG1-h470sJpFf0119JCUwh2hIvp20Nqf6L935KS95VfiDho4gK-6RhFuFWQbs3k1WEcMeHu6QAV9sr_pDDdR-1qndbvoyCnEgb3amVo5M_vesciXC2_ySvTVUrRmwQVJK1Wwz9nvaB-69uaEnGKrzTBNLDCIZLp9qPGqEuSf3p_F82NC2JdIySHjWqWvYpe9m2SvpRitGZMXyF4kUw0qFmQo7l1qJN1iXMpHMBIt5wZukWk_69uwRD1a8tr9BczbKDJWPbHJFdn8LsiYJUFGNXZ_gXUuiShNoCIhHVt2hch7AGm3zvB7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qOh1k3GCeAUkcHZv395TW81CXP8WYSChSsMflxGBNUNfj1uhUMB1QDUKnILFXi-UYpcBebWpo5_kvgEUF88SrYaOxN99ec92G6tNJCjTogRHgA-OgKTLPS7LthzEV_AveyP6JoZwl8VFV1aD22zJ7qsEaPt6ce4gCMB_E_ukm3g1dBD_NaR5LoQcDv8p1-X_SGcqyL3j9sFLKP_jXOuuIaB9eCuMS3k-bUcISFiNzgT5toLQJD8yjhWOWkg92_ZIwwtwYLO1PYrziZIv0jsCgninkJGJ5XS11jtHH7H_NovNoppltDXVPkcx4cAD12AdxRaYaR9EF_N8cppz19_pAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QC6grhHofRuXM9dHeLGvkFuRCIIDzKKz1GacQZEKQW49uOjv5iasHUA0YlnK4pnjMcWsWjMk1b2hcVPfx5Xf9usFnGID6E1S7yVI2xALw71223akHHhTWHdhK2Ny_f0SVD7H9GmwXZVBgs_VISkTzuqwb-eytEqvA71r3PrK9lYMQlsjHAa4H5elCGaprzGNEr12KOabWN_WB7SCCUA8BfdWe5zfpERB5XJ3hHvpWnWymSsEd0vWLQRQUTP9M3gXAIIzWYEWzpa72R3KvQhhEFbmvfwM-4SRh2b12nk9cLle0wrLfudXOBskC8RO5gERsgZIR8y4qQusv_mV3h7FEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tB6tOLqnIX06pgg7WQlGgOOdBkrWVHIQniJnd_GwQm9wjBei5vTL6Y2IGQDwLFnD84dPhMDeHH_Jo-X_fTMQJF2k6hjNl6cIMRCfmzcm5Pm9yjStVl2derGXIYA0AijKG8gTAg9wN-H4WNP5sYKNCQV8rQWWN9L7n50-J5QHDZCiTVNGITrgONrpQG2f4Ugoe4SyHh2ZTRPjQPmB-nGIAuzOr2sGEYRvKNlTQC7sqi4x1xnMpxUXqSrRXFv7COHPIbcs3Ao79CxASt49CKJpLeDVFIicgc4kMVNKZhNGWVFE65Ydwr9tmhERyGAOb7sgCPJNRegS443byjBU0D-M8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/saACTVhYJvCm2WnEmWra2JmF9u1xCbgUhgWCO0-c0HyYyf2twGrnsj39l-TzpagwGqC_z38SjmtQ2QQGKO-a9pFlNe-SrrOwlR8TGkdR-sKMdGOKui_XP0eTt185MiMwnlBMxX1V2QuJ0Gom6Rtp1XqzweR2EccmwsJLpGRblyZvkY3lP8b6olKyoe6ngfUhMOEQ1Kf2iasz3k2cskDAPN2d-o-b6-6IZb4gXHNOx36uCQApFgpkmgr2xSwhGzLqz57YYje-rXkVsLH05Zi23ozohvqQoGE0M0XdCRKtOmtlRfHbpO2e_x6pQ4ZXOtu37ZHAiQysxUwuGSbUuKbaEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نمایشگاه خودروهایی که نمی‌توان خرید!
🔹
هفتمین نمایشگاه خودروی تهران با حضور ۳۵ شرکت واردکننده و تولیدکننده در شهر آفتاب برگزار شده و بخش عمدهٔ غرفه‌ها به خودروهای وارداتی اختصاص دارد.
🔹
برندهایی مانند لکسوس، تویوتا، مزدا، ولوو و مرسدس در کنار برندهای چینی و خودروهای لوکس حضور دارند، اما جای برخی خودروسازان و مونتاژکاران داخلی خالی است.
🔹
با این حال، قیمت بالای خودروها فضای نمایشگاه را بیشتر به محل تماشای خودروهای لوکس تبدیل کرده است؛ قیمت برخی خودروها از حدود ۵ میلیارد تومان آغاز می‌شود و در مواردی به ۸۵ میلیارد تومان می‌رسد.
🔹
برخی بازدیدکنندگان نیز با وجود داشتن چند میلیارد تومان سرمایه، خودروی وارداتی متناسب با بودجهٔ خود پیدا نکرده‌اند.
🔹
طبق گفته‌ها نمایشگاه امسال با وجود تنوع بالای خودروها، برای بخش قابل‌توجهی از مردم بیشتر یک ویترین خودروهای گران‌قیمت است تا محلی برای خرید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/farsna/462449" target="_blank">📅 17:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462448">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سوئد کارمند سفارت ایران را اخراج کرد
🔹
سوئد در حمایت از رژیم صهیونیستی، یکی از کارمندان سفارت ایران در استکهلم را اخراج و سفیر ایران را به وزارت خارجۀ این کشور احضار کرد.
🔹
به‌تازگی وزیر دادگستری سوئد، بدون ارائه شواهدی، ایران را به انجام «رفتارهای خصمانه» و تهدید منافع اسرائیل در خاک این کشور متهم کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/462448" target="_blank">📅 17:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462447">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Venj2OIiSfoX2Rc_GG1ojDXrikL7Ov487srIG3R-CHoMAwEx2VgC-GLCjbXjDTH_opWiPztiyz7Qe13TVlZhkSm2k8xOr39OobSM1ApFM0TXN2hkbEXN7WHOD_ZDMx6KCEE4CTVObypl149AbweKt30jgSnOaxSuxhXpenodkPstxZB2H0yGjgqED1fpZMu4ntiC5uJ63RcSvZSLw-UH13m9NbXWgSDFRuFVt2y0pSmy-wASWwTU5qa7gQ3gi9NXy9mTzNz2Ft9LUUCN2L0Au62nKX9Cy6N0MlYXjtsw7u1-fWKeIqnV5BepJwTj-RIgtVK-05BFPW9opq7uoQ8bzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرشاخ‎‌شدن آمریکا با چین باز هم بر سر ایران
🔹
وزارت دادگستری آمریکا خواستار مصادره ۶۱ میلیون دلار رمزارز تتر در ۲ شرکت چینی شده که مدعی ا‌ست این رمزارزها حاصل از فروش نفت و محصولات پتروشیمی ایران به خریداران چینی بوده است.
🔹
دادستان‌های آمریکایی مدعی هستند که این پول‌ها از طریق شبکه‌ای از کیف پول‌های دیجیتالی مرتبط با شرکت بایننس در ماه‌های می و ژوئن سال گذشته منتقل شده‌اند و بخشی از بیش از ۱.۵ میلیارد دلار شبکه تسویه درآمد نفتی ایران در چین هستند.
🔹
نیمهٔ اردیبهشت ماه بود که وزارت بازرگانی چین با اعلام یک دستور منع حقوقی برای مسدود کردن تحریم‌های آمریکا علیه ۵ شرکت پالایشی چینی که به خرید نفت ایران متهم شده‌ بودند، اجرای تحریم‌های امریکا علیه ایران را ممنوع اعلام کرد.
🔸
حالا امروز هم وزیر خارجهٔ چین اعلام کرده است که پکن آماده است تا «قاطعانه از حقوق و منافع مشروع ایران دفاع کند.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/farsna/462447" target="_blank">📅 17:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462446">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13ed0cc5c4.mp4?token=PU31enobzmyavxJO60t47gk162aaQ0YkXL73AcUFLfPoNl_9PwRUlMss6pJ71mY8AV_3tNehNPskBkMy0udYA46BowngiUIChd_TjWC7fC4EUD2d5Uf94Xx3N11t9ReUT-RCkWPbSomCcMAZ2_zNbbaodngh-_wpQ-axxwtM5eV9xGCT-Nr1_ewY-Z66xay8IxxCYM426pfUN6HhkbuBfL7_gfJG7qrMl3ERCB6yVgTDt6Qhx_dR5w3qcONEu63Uldyuq8UN6XFu0b2LXV4CKjcVQ6EK_IWiWoVClTnorRUiws_gH3GRNzargD9w6obHIA0pZdK6tbtQP4Nx7DFVuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13ed0cc5c4.mp4?token=PU31enobzmyavxJO60t47gk162aaQ0YkXL73AcUFLfPoNl_9PwRUlMss6pJ71mY8AV_3tNehNPskBkMy0udYA46BowngiUIChd_TjWC7fC4EUD2d5Uf94Xx3N11t9ReUT-RCkWPbSomCcMAZ2_zNbbaodngh-_wpQ-axxwtM5eV9xGCT-Nr1_ewY-Z66xay8IxxCYM426pfUN6HhkbuBfL7_gfJG7qrMl3ERCB6yVgTDt6Qhx_dR5w3qcONEu63Uldyuq8UN6XFu0b2LXV4CKjcVQ6EK_IWiWoVClTnorRUiws_gH3GRNzargD9w6obHIA0pZdK6tbtQP4Nx7DFVuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای راهبردی روابط خارجی: توقف غنی‌سازی هم فشار آمریکا را تمام نمی‌کرد
🔹
دهقانی فیروزآبادی: اصلاً به آمریکایی‌ها نمی‌شود اعتماد کرد؛ آن‌ها قابل اعتماد نیستند و به تعهداتشان هم پایبند نیستند و حد یقفی هم برای آنها وجود ندارد.
🔹
آمریکا در مقاطع مختلف با طرح موضوعاتی مانند حقوق بشر، تروریسم، صلح و خاورمیانه و مسئله هسته‌ای، ایران را در یک گفتمان مشخص «تهدیدانگاری» کرده است.
🔹
من تردیدی ندارم که اگر موضوع هسته‌ای هم نبود یا مسئله هسته‌ای حل می‌شد، در گفتمان دیگری ما را امنیتی می‌کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/462446" target="_blank">📅 16:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462445">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVkWh90VojEX563F4Az0JLBOjzNZDHUyyFCRT2cSkwFr4RPQFo66Sjy3DrppbnsmiN2sqeZ_1oe_Y2tFAhtHb_rh_Ntjis5VChZaJTsVIsHzmJQYSzlRJ7B8J64_LkpTavLeoQRPPalu3aRHzDYxX1aN3iJ5c0_ihEOmZpKPpfg4-LUoA1zkSYYZaFKjgjmJ0psye8usxAZC9WiXoH3HoyCXJ7lJvmshLAN0uqhGQa0TT_csqgum54O3u7U-oi8jm6lWcmD8a2Enp4qNnHZc__--ChpFuXcYqSaKg_mGMJJOvLL7YvCbD-ceCp5aZdZFI_TtwJgzOxgS4_aBliDtLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درخواست فعالان دانشجویی برای تعیین تکلیف پرونده‌های انضباطی دانشجویان هتاک
🔹
نمایندگان بسیج ۶ دانشگاه‌ تهران با حضور در میزگرد فارس، به بیان دیدگاه‌های خود دربارۀ عملکرد وزارت علوم در رسیدگی به پرونده‌های انضباطی اغتشاشات اسفند پارسال پرداختند.
🔹
مسئول بسیج دانشگاه خواجه‌نصیرالدین طوسی: وزیر علوم در مصاحبه‌ای از اتفاقات اسفند به  «جنب‌وجوش دانشجویی» تعبیر کرد؛ این نگاه نمی‌تواند توجیه قانون‌شکنی باشد.
🔹
مسئول سیاسی بسیج دانشگاه امیرکبیر: اتفاقات اسفندماه از شعارهای رادیکال و توهین‌آمیز تا درگیری و خشونت، فراتر از یک تخلف معمول دانشجویی بود و برخورد با عوامل آن باید به سطح بازدارندگی برسد.
🔹
معاون بسیج دانشجویی دانشگاه شریف: از ۲۴۰ پرونده ارجاع‌شده به کمیته انضباطی این دانشگاه، تنها ۴۵ نفر به کمیته دعوت شدند و در نهایت فقط یک مورد به اخراج رسید؛ سه پرونده دیگر نیز همچنان در وزارت علوم تعیین تکلیف نشده‌اند.
🔹
جانشین مسئول بسیج دانشجویی دانشگاه علم‌وصنعت: هیچ‌کس نباید بالاتر از قانون باشد و پرونده‌های دانشجویان هتاک باید مطابق قانون تعیین تکلیف شوند.
🔹
معاون سیاسی بسیج دانشگاه تهران: برخورد با دانشجویان هنجارشکن نباید صرفاً با عذرخواهی متوقف شود؛ اگر اقدامی طبق قانون جرم باشد، باید فرآیند قانونی آن طی شود.
🔹
معاون سیاسی بسیج دانشگاه شهید بهشتی: در حوادث اسفندماه آنچه در دانشگاه‌ها اتفاق افتاد، صرفاً اعتراض دانشجویی نبود و بخش‌هایی از این جریان تحت تأثیر عوامل بیرونی شکل گرفت.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/462445" target="_blank">📅 16:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462444">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a92e547cc7.mp4?token=lFSvHSv7ey6vmOJ2TOmGsMWilVjFI-F_hsPyWP7KAoygp9lWW9-Daf6JXhd1G54kyy3hk3ZCHnD1VgES8vIve-veUPKqMgZ2B4Uq3BpWmnu29PCZH9VYF_x8YurSQfFVwOosAV-chVc4i8Hcw-MzPhxnyMEMExYjgoaN4C1zg9u7ReAIgVWZgjkxPLQCTIsJ3bu7N5bRsJwuVcvAQs_wSqdrR0QODioJ6gj2BnJWiBpRwFyLAgyJ9eWrzlnDDEMXxW5yEI0wICaPF5UMGEMoePT-hoEVS8PTMjYajKZZs6UP6itvUWAFqwoPecXckqAaaLlYssr_KhamaIDXm82pFgm5JZ3AugG6KbziZsPy_whaEL3dfUmSJuHEjzdCgpgQHHDkI1iqfvuVI5Te2-NkAQ7RGYJMJhinPebAJ85rIq6R-aWFkW61fK0tdKg0Fy37E_YkAlOJ2qsoNpcxtaDzkkpcgvwtS5kiP3q9j-kmjHEmxycCrVJHx-UtfvSWWzJBk-ACHQaaaxSBVA50zmadhUuadCIAC4DASLIdDvwKcU-wuP5CRJnbqd15CViXSlPez65_G-RXCC_ZG2drkxYs2moxUbcV058vXHEXI9Lu58QCAPj8bystwevZmaz2JFm_q4CVYhbYdTOYm834x34fEYR7hyQGJ-lb2EFPjhKsGaI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a92e547cc7.mp4?token=lFSvHSv7ey6vmOJ2TOmGsMWilVjFI-F_hsPyWP7KAoygp9lWW9-Daf6JXhd1G54kyy3hk3ZCHnD1VgES8vIve-veUPKqMgZ2B4Uq3BpWmnu29PCZH9VYF_x8YurSQfFVwOosAV-chVc4i8Hcw-MzPhxnyMEMExYjgoaN4C1zg9u7ReAIgVWZgjkxPLQCTIsJ3bu7N5bRsJwuVcvAQs_wSqdrR0QODioJ6gj2BnJWiBpRwFyLAgyJ9eWrzlnDDEMXxW5yEI0wICaPF5UMGEMoePT-hoEVS8PTMjYajKZZs6UP6itvUWAFqwoPecXckqAaaLlYssr_KhamaIDXm82pFgm5JZ3AugG6KbziZsPy_whaEL3dfUmSJuHEjzdCgpgQHHDkI1iqfvuVI5Te2-NkAQ7RGYJMJhinPebAJ85rIq6R-aWFkW61fK0tdKg0Fy37E_YkAlOJ2qsoNpcxtaDzkkpcgvwtS5kiP3q9j-kmjHEmxycCrVJHx-UtfvSWWzJBk-ACHQaaaxSBVA50zmadhUuadCIAC4DASLIdDvwKcU-wuP5CRJnbqd15CViXSlPez65_G-RXCC_ZG2drkxYs2moxUbcV058vXHEXI9Lu58QCAPj8bystwevZmaz2JFm_q4CVYhbYdTOYm834x34fEYR7hyQGJ-lb2EFPjhKsGaI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر جدید از اصابت دقیق موشک‌های ایرانی به پایگاه موفق السلطی
🔹
یک حساب کاربری اوسینت  با انتشار تصاویر تازه ماهوارۀ «سنتینل-۲» نوشت که نشانۀ دست‌کم ۴ نقطه اصابت موشک در پایگاه هوایی موفق‌السلطی اردن، پس از حملات موشکی ایران در روز سه‌شنبه، وجود دارد.
🔸
بر…</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/462444" target="_blank">📅 16:17 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462442">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOUlWdQvlfiafCJLmirX9lDl8BKa4Qv7BnXI1qPRkej_lghwQ6KXp8tmecU7q7W-Z5qUeUos595xerA6kyOOLmPncmrvBpst9Rsd819x_jIVsuf6zvcgJjRWxaidFCLjg6X-aJmSzjTgqPcYGIihwUf-aXeltop-0ii8x-V9xSkrTwOL_x5K0ZY3lexuRCB9nbrvx1cjnG86R2mosMPtbzUqFqq1TShpG6fJpVCleHc7OlbnnBzWEUEgLyByGM-CgnU5lzkXRK0qDQ_SNxqq4wS50j4-5PxHS1JYpQkgR9BOb_NHxVOPrgCRlQyeKS3PM_XqRfdCQ8aTcppzl1rLug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرانی بنزین یک سال کوپن غذای آمریکایی‌ها را سوزاند
🔹
آمریکایی‌ها از زمان آغاز جنگ با ایران حدود ۱۰۷ میلیارد دلار هزینهٔ اضافی برای بنزین و گازوئیل پرداخت کرده‌اند؛ یعنی به‌طور میانگین روزانه بیش‌از ۵۰۰ میلیون دلار!
🔹
قیمت گازوئیل با رشد ۶۰ درصدی به رکورد ۶.۳۰ دلار در هر گالن رسیده و بنزین نیز با افزایش ۳۹ درصدی از ۴ دلار عبور کرده است.
🔹
بخش عمدهٔ این هزینه به گرانی گازوئیل مربوط است که با افزایش هزینه حمل‌ونقل، قیمت مواد غذایی و سایر کالاها را نیز بالا می‌برد.
🔹
برآوردها نشان می‌دهد این افزایش قیمت به‌طور متوسط حدود ۷۷۰ دلار هزینه اضافی به هر خانوار آمریکایی تحمیل کرده و قدرت خرید و پس‌انداز خانواده‌ها را کاهش داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/462442" target="_blank">📅 15:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462439">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">مجمع هلدینگ خلیج‌‌ فارس این‌بار به حد نصاب رسید
🔹
مجمع عمومی عادی سالیانهٔ شرکت صنایع پتروشیمی خلیج فارس امروز با حضور ۷۶ درصدی سهامداران و نمایندگان صاحبان سهام درحال برگزاری است.
🔹
نوبت دوم مجمع فوق‌العادهٔ هلدینگ خلیج فارس با دستور انتخاب اعضای هیئت‌مدیره…</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/462439" target="_blank">📅 15:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462438">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCNjc9thfuxbUGrR7eMwr_Nv5XMo6txRtqTHAAfltv48seyvr7e10gSFWqjSzQHigUH-ryt2Eec0jBYc1e4HBkuk2jcW5eKJW7q5uYL_YbaERhCFI4gKkO9nzvIuY7aJiSkSi4a_Dl4RXnDXkNFkeWhM2WCRBujS2h-vgleMvuHfoftmcSvbDKaD0k3FHcJZnXPri6IQ_jno87M0vnJU5djrcF26CeiNxUQsaR65ogVyKKYYrZW5XeZeutopMpQxZ9tVMu81P1qvZN_3dSlmBat9jbZsLKqH1-gdrlD4ZjL6C4RNgIe32wpVVCPVsvqi_b2yKFzBVFVQ75xzY760-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن: تأسیسات آرامکو در ینبع و پایگاه خمیس‌مشیط را هدف حمله قرار دادیم
🔹
یحیی سریع: در پاسخ به تجاوز وحشیانه به کشور و مردممان شرکت آرامکو در منطقه یَنبُع را با ده‌ها موشک بالستیک و پهپاد هدف قرار دادیم و با لطف خداوند، اصابت‌ها دقیق و مستقیم بود و باعث آتش‌سوزی‌های بزرگ و خسارات گسترده شد.
🔹
همچنین پایگاه هوایی خمیس‌مشیط را با چند موشک بالستیک هدف قرار دادیم و با لطف خداوند، اصابت‌ها دقیق بود.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/462438" target="_blank">📅 15:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462437">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0880aaa698.mp4?token=C6kjuvmcL03Op0Ird5hT4ew-TEZzLB_orlJ-EMWXuT9sw-LVN1Yzwc-3DwHqpd2N1mapMtMFMXrR4sQ4CeEFzbuVtgEqObEn-xXQN5k0RTo0hRSAOAAjJDRQmDWikpLzP8uwm1UCcPu0kFHtmZlji1CCsfRzp-KKbmpG7SdwVFtfCvHAnG_8qeIdc3NchHlyq7JQqm5xn0gifpT-Yl1RWQDHbRpZRQGMjHZ0AxX8Iy8cT5VeLVcM27ulh_51NXAo1SSyRnR5bXCLs3QKkXmUJ_lGCt9xtxbC_4u2AbGN_B2RVJQko0jyj198uSS0YKVPK54bAuynidLVgb5StAW8xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0880aaa698.mp4?token=C6kjuvmcL03Op0Ird5hT4ew-TEZzLB_orlJ-EMWXuT9sw-LVN1Yzwc-3DwHqpd2N1mapMtMFMXrR4sQ4CeEFzbuVtgEqObEn-xXQN5k0RTo0hRSAOAAjJDRQmDWikpLzP8uwm1UCcPu0kFHtmZlji1CCsfRzp-KKbmpG7SdwVFtfCvHAnG_8qeIdc3NchHlyq7JQqm5xn0gifpT-Yl1RWQDHbRpZRQGMjHZ0AxX8Iy8cT5VeLVcM27ulh_51NXAo1SSyRnR5bXCLs3QKkXmUJ_lGCt9xtxbC_4u2AbGN_B2RVJQko0jyj198uSS0YKVPK54bAuynidLVgb5StAW8xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جلسۀ شورای امنیت دربارۀ وضعیت «باب المندب»
🔹
منابع دیپلماتیک می‌گویند شورای امنیت سازمان ملل متحد روز سه‌شنبه جلسه‌ای اضطراری دربارۀ تحولات پیرامون تنگۀ باب‌المندب برگزار می‌کند.
🔸
تسلط ارتش و نیروهای مسلح یمن بر خط ساحلی تنگۀ باب‌المندب و عجز و لابه‌های رژیم…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/462437" target="_blank">📅 15:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462436">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34aa499ac9.mp4?token=M1qyUqsmQqisI14YCGEfQIH1S_aUGKeBpcZ2w249H802AhXYy4JDiZlYHmSCvVC3d4dzSonSWhU2dk07W0fiDgPqiISNm02bcEFE1sXEGaYabl5yTnOy5ODRvEDqmJn2apGFhn4_6rVdF-5668nvEH5WAR1VYsjGiWLw0DZnye6DITGKJKVOICYcN3CcAU4Z8XiR28snOqA9krCj1kFWhmhiLyijX878yn9ky-qBcwZ2WD2APRBza4Jo8EwO8lCnN4hcU2l1bQxVqQ01Gwhb0pmTU4Oq32hAj6iN_WHRrcULULgLnjEQZ3ZbmHRq2ZkUbgqEvhhSYsdUtNiadqzSSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34aa499ac9.mp4?token=M1qyUqsmQqisI14YCGEfQIH1S_aUGKeBpcZ2w249H802AhXYy4JDiZlYHmSCvVC3d4dzSonSWhU2dk07W0fiDgPqiISNm02bcEFE1sXEGaYabl5yTnOy5ODRvEDqmJn2apGFhn4_6rVdF-5668nvEH5WAR1VYsjGiWLw0DZnye6DITGKJKVOICYcN3CcAU4Z8XiR28snOqA9krCj1kFWhmhiLyijX878yn9ky-qBcwZ2WD2APRBza4Jo8EwO8lCnN4hcU2l1bQxVqQ01Gwhb0pmTU4Oq32hAj6iN_WHRrcULULgLnjEQZ3ZbmHRq2ZkUbgqEvhhSYsdUtNiadqzSSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۶ میلیون دانش‌آموز یک هفتهٔ دیگر سال تحصیلی را آغاز می‌کنند
🔹
وزیر آموزش‌وپرورش: همه‌چیز برای شروع یک سال تحصیلی خوب و حضوری آماده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/462436" target="_blank">📅 14:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462435">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cec4abd008.mp4?token=Gbw3HgOFApz0_zawoKfxXLRBG0d6E3H8p25xD0BvKWnSGO17d6Cxx9DeTlox6opTveK8hHXGdhg0W-Mgf4nlqwi8do0Lp1jTuIjCBzP13g9jF8FnYnOZt9Mz5W-cO3MJMJhClfprUEDFp55wO-drJDweOzC6rEDvBz30vdCbPf50YV9lThNGkmUlsqWEQ4zqrBNv46RlftZls1xVEnYZh8eqTMdTotGpmTWgid5p9dnFi1pRIV4yvWNnGqS-Ua24cCH-WiGsMM2-2Wv8ecm5njb58Z6SFI69g0VZvc23Mc8RD_CiqIDzpCA170jJiA7qav11dpVVr0InOrf0Uog-dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cec4abd008.mp4?token=Gbw3HgOFApz0_zawoKfxXLRBG0d6E3H8p25xD0BvKWnSGO17d6Cxx9DeTlox6opTveK8hHXGdhg0W-Mgf4nlqwi8do0Lp1jTuIjCBzP13g9jF8FnYnOZt9Mz5W-cO3MJMJhClfprUEDFp55wO-drJDweOzC6rEDvBz30vdCbPf50YV9lThNGkmUlsqWEQ4zqrBNv46RlftZls1xVEnYZh8eqTMdTotGpmTWgid5p9dnFi1pRIV4yvWNnGqS-Ua24cCH-WiGsMM2-2Wv8ecm5njb58Z6SFI69g0VZvc23Mc8RD_CiqIDzpCA170jJiA7qav11dpVVr0InOrf0Uog-dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نتیجهٔ گزارش پنتاگون دربارهٔ جنگ با ایران اعتراف به شکست بود
@Farsna</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/462435" target="_blank">📅 14:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462434">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🎥
یک شب مانده به ۲۰۰ شب حماسه‌سازی ملت ایران
@Farsna</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/462434" target="_blank">📅 14:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462433">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4b8df15dd.mp4?token=Yx-comXsY6t5Sc8Six5HdLOVbxAKks8OEBkD2KVpFvdX26DV07TU0IHjYzce9mRq847b4zRCn2qMBsovmfclddYvJgPbjDyCpon-Il2Uu89bDYYvCnM0dw-FXBKWFHTUbSwhlfAS_webvYIIPnSDZgGLJVWroN8-suY8U2339aV47nCRw1gwXdjLrlesXLbtqO0XKDQXBnW4noa45xDj9pxEunpq1ZK5Pd9V7NGSeXvYwIO2_JZAMPbtkEmG5QxXCkzVaLUTgj8SZvb6c5Kos4lEslRP_ztk6GvFTMZq13ufCFX_2_PK-Gk5uj_A6tDTUNV16Li1zVdqW3UXZQxfYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4b8df15dd.mp4?token=Yx-comXsY6t5Sc8Six5HdLOVbxAKks8OEBkD2KVpFvdX26DV07TU0IHjYzce9mRq847b4zRCn2qMBsovmfclddYvJgPbjDyCpon-Il2Uu89bDYYvCnM0dw-FXBKWFHTUbSwhlfAS_webvYIIPnSDZgGLJVWroN8-suY8U2339aV47nCRw1gwXdjLrlesXLbtqO0XKDQXBnW4noa45xDj9pxEunpq1ZK5Pd9V7NGSeXvYwIO2_JZAMPbtkEmG5QxXCkzVaLUTgj8SZvb6c5Kos4lEslRP_ztk6GvFTMZq13ufCFX_2_PK-Gk5uj_A6tDTUNV16Li1zVdqW3UXZQxfYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در ۱۰۰ دقیقه ۱۰۰۰ گردان جانفدا تکمیل شد
🔹
با اعلام ستاد مردمی پویش جانفدا در کمتر از ۱۰۰ دقیقه ۱۰۰۰ گردان آموزش نظامی و امدادی جانفدایان ایران تکمیل شد.
🔹
افرادی که در ‌ادامه ثبت نام خواهند کرد در لیست رزرو سازماندهی خواهند شد.  @Farsna</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/462433" target="_blank">📅 14:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462432">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kn9xk-3FqxAMvIKXcJWBmSs4IVkwzsvXWvJeAxJeE7mMcGPtMi-RqkBH4zvmbACQYy9F3T_AZPCI7fNCASa97a5_0sIlWyjiT97v4OQfJTpegQGONp7pY9Z1eJFW3bXGMwzGg4Fmzg9ku_80FGADQ-wuFIJvsUSkp-TnZI9U125ogfNUGV_novBOjgziAbH2S9j_CGeNlLal3W_-kcrhtLaNTAjT7r6Ene012IDi6njXGQ_6FESlBZ6lXbdsK3sA2eGqnc9Yg-KsJxLsS8FXQO73hcVHIT5EZubMA7rn4gNE8F9fmR9aO6qxp_w7c1Rm7lpUfwdFcTbVQcLa2nLuEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ آغاز ثبت‌نام نخستین صندوق سرمایه‌گذاری ارزی
🔹
پذیره‌نویسی نخستین صندوق سرمایه‌گذاری ارزی کشور با هدف جذب بخشی‌از سرمایه‌های ارزی و هدایت آن به بخش تولید از امروز آغاز شد.
🔹
سرمایهٔ اولیه صندوق ۱۰ میلیون دلار است و هر فرد حقیقی یا حقوقی می‌تواند حداقل ۱۰…</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/462432" target="_blank">📅 14:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462431">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiRhZ5iTUeevxg0JpGwbhgI4EC1-MbAAl-l0e-2vRI4jRsNTyfsRJs1LvLIJRgo9zbw8q1_KZX7036A2MLq0MAgpXCKuDa4-OK_n8uzm9AiRF0elzSAo3hdRnhWTnpfcSQW16bWvINDYcn1tqgx3IZ4tOcQDFD2IxWjqcsLpOLTuVbLYnU2GgXa3LchPjv45JxuT3z7RfYj3M-A6O3HdR-cz80IFXuRZ8GaN8Mi6V5wpHw5HBQtGTP30CuK0QUthCaeK3crb2vG7w13O7g-LKpUgdy4UMyL8MG9phURBkDNpTkmWzgSMkMgBWzWfvfo898WVmr_uO30MTXVLmE3CZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ جزئیات افزایش کالابرگ مشخص شد
🔹
پیگیری خبرنگار فارس از وزارت تعاون نشان می‌دهد رقم افزایش اعتبار کالابرگ درحال بررسی است و این افزایش در بازهٔ ۳۰۰ تا ۵۰۰ هزار تومان خواهد بود.
🔹
وزیر اقتصاد هم امروز اعلام کرد که ۳۰۰ هزار تومان کف افزایش اعتبار کالابرگ خواهد…</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/462431" target="_blank">📅 14:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462430">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CT_oqm5pGN6iHGWYFcxincq8-Rh0IpL-s3-uHezvV0D3JyeLHvDfTzX5CSFk8hCK1agr_wi52pPPzTpqPnpdiyWZS8nYDaepr94QnwE8zhKw0blaJDbWUwzH31PlKJmbSBGjM3ii40mxdyCXmk6tBy4dEaR8ASeHD88kT5trAmAujs7xcy3Fr-a391_idaomjOlEPbvqxoJMTBqckipxRPukv9xmw6gI6PlYIhzHsSPro6KAYSUrOzoM3PKSGTzg2vrh-JvVUI44cKRRoHjr8hXxcT2pz2gRyxATGf1hfPxEPGDSec40Cm6NHvdh8HUFMnxdZHqB9OQkDCFOXLQy3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه‌شنبه‌ها روز بدون خودروی کارکنان دولت
🔹
رئیس سازمان اداری و استخدامی: به همۀ دستگاه‌ها ابلاغ کرده‌ایم که تا حد امکان، روزهای سه‌شنبه را تا پایان سال به‌عنوان «روز بدون خودرو» در نظر بگیرند. @Farsna</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/462430" target="_blank">📅 14:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462429">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سخنگوی دولت برای چهارمین‌بار: کالابرگ افزایش می‌یابد
🔹
سخنگوی دولت امروز گفت که «در حتمی‌‎بودن افزایش رقم کالابرگ تردید نداریم و حتما این کار اتفاق می‌افتد.»
🔹
روز گذشته رئیس‌جمهور هم گفته بود که «رقم کالابرگ حتما افزایش پیدا می‌کند.» این درحالی است که قرار…</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/462429" target="_blank">📅 13:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462428">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bS4zxt6Xefi8hYsNk0b9Ldm_0qq01YI_0G1V4e253E2T_w70RMu5XTO-BA5Xy7WnWMt-sBvL5BAdp2UgSMqKHO4Qzd8NkQMQVvOq-KHzucGPHOGpk19zz9Fa8dgpaXyuTjwoLMa_xpngmwZ1DNQz9gjqCxOv9etP73ODqzEJJahTbSjtyVnrdpV9ld6YgvAPih8CzNCcdkEZvgnXJQHs4qkMi5rzljnVnkudlhZBmjv7p5iqOMtddVCmaw6FvBV5XLt3ibSOcWsnjLnBcH_q7MNPxjCMHhNRfvjUcH5y1L7e2Z6xho3ZS3zfGHHd8HWxsCcsNn5GHUdFtp1gmJmEag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز اولین تولید آزمایشی گازوئیل یورو۶ در ایران
🔹
پتروشیمی نوری برای نخستین‌بار در ایران تولید آزمایشی گازوئیل یورو۶ با گوگرد کمتر از ۱۰ PPM را آغاز کرد؛ ظرفیت متوسط تولید گازوئیل یورو۶ این واحد حدود ۲ میلیون تُن در سال اعلام شده است.
🔹
برای اجرای پروژه از سال ۱۳۹۹ تاکنون حدود ۶۷ میلیون یورو و ۲.۵ هزار میلیارد تومان سرمایه‌گذاری شده و ۷۰ درصد عملیات آن با توان داخلی انجام شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/462428" target="_blank">📅 13:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462427">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diAJtMDfRTIagx6ISkZRL-e55pWuvGpZpkJjVWQAFoG3Od8-0Face0PwGB8QBntai6-iVRJcrBihGdxc7P8x9iKqT-bFeEWaDzwoecn-T9whXRF2m474kEmD5qXwLKXJBC52shQn513QUtmIdBTddUy-ketXYNOsgPfy-uZFUbjRJ5m40-Ppb5EiiTH61jZEgpN5PMSioUuJW4CiXXbC-x8fJkvlICCqzGC7BOKMjOzTF8aGiJkOxQVM2oK4sELtOef7UxgWRMTC8dGaJM85p3H2MTZLlrTEbWJ563TpFnO5lnGqeXj_zSK6HDzwH0xYWtHLSFSYOD5nod-TplHMlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر حیدری: اگر آمریکا جنگ را ادامه دهد این‌بار نیروهایش در آب‌های منطقه غرق خواهند شد
🔹
جانشین رئیس ستاد کل نیروهای مسلح: قلۀ توانمندی آمریکا، نیروی دریایی و ناوهای جنگی این کشور است؛ اما چند شب پیش موشک‌های ایران ناوهای سنگین و ناوچه‌های آمریکایی را هدف قرار دادند و آسیب‌های جدی به آن‌ها وارد کردند.
🔹
آمریکایی‌ها در این منطقه دو سرنوشت محتوم دارند. اگر جنگ را ادامه دهند، قطعاً انبوهی از نیرو‌های آن‌ها، همان‌طور که تا امروز به درک واصل شده‌اند، در عرشۀ همان ناوها به کشورشان بازخواهند گشت و انبوه دیگری از آن‌ها در قعر آب‌های منطقه فرو خواهند رفت.
🔹
امام شهید ما فرمودند که اگر ناو سلاح خطرناکی است، خطرناک‌تر از آن، سلاحی است که ناو را به قعر آب بفرستد و ان‌شاءالله این اتفاق خواهد افتاد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/462427" target="_blank">📅 13:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462426">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ثبت‌نام نخستین صندوق سرمایه‌گذاری ارزی از هفتهٔ آینده
🔹
رئیس‌ بانک مرکزی: ثبت‌نام نخستین صندوق سرمایه‌گذاری ارزی با هدف جذب منابع ارزی، تأمین مالی پروژه‌های ارزآور و توسعهٔ ابزارهای مالی ارزی از هفتهٔ آینده آغاز خواهد شد.
🔹
براساس این طرح، دارندگان ارز می‌توانند…</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/462426" target="_blank">📅 13:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462425">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0d_nXiyebxQlIGBX7KRdsFZj6XCWiEy9vUMbQCLq2Gs3lmLcW-7gGtYiXBhhM2WIl0x8KorhZoe_nOAkuPb9PSmSkCkhoO4bDo45rZVhUahsywWeXfegTvtetygbIVQrn9FZDZ7hqC-9foT3H_f4ffHSJJw12-5tvhlk6nGDv4qZLrRkKzFWa5vKBGuftNVT4CExn73-8CCYvL-CkwHsOqs5w9__JFA_pl4ktmDVtM851MOmPg6d5MIaet0tl78LI36l71oLkZBGvsDNymoSwlNl5YlYtm9yqqakX17tNtWp_FcaTh_3YI2OkoM2l3qXQppSzPj-iC0vYeIR7PSXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رایگان‌ماندن مترو و بی‌آرتی تهران ۲ ماه دیگر تمدید شد.  @Farsna</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/462425" target="_blank">📅 13:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462424">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqBt3vsU_uElTKM8DdShCFtuYibLFOV_IcOyqVQ7-JYcVxgMOwQjHtb3nfXISZStim2CtshzReiZGB9XmyXpzxgOk-nurmbpA3K_jwltwtu_bGK3oqSctS81f6ihYYiO2KpORxYd4003jQYBJ3VNa67n5rDpw7T4FjAmEWpx8XeorT84MOOXPAJyE8CTmWVM1ihFZ4_ra7oTvsd6Jpe3nMonBat_hOUZpfuCDN480PBHhtKaAeBI7w6h1a3afK06D5eX1wLyq78YYfX92MMOYfz1mxla6EopKZdy2Uuab7pwyfJAzDHa9UeOEQt2ROG5aHSayLrjtPo4HY0lrZnZCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی شهرداری تهران: ۳۱ اتوبوس دوکابین در دل محاصرهٔ ادعایی آمریکا وارد ایران شد
🔹
محمدخانی: این اتوبوس‌ها دیروز وارد ایران شده و تلاش می‌کنیم با انجام سریع فرایندهای گمرکی، در نخستین هفتهٔ مهر وارد چرخهٔ خدمت‌رسانی در تهران شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/462424" target="_blank">📅 13:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462423">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAYE4g7_grIT9wM6KJ-Sxgl25bQY6KxO48aNDjB_K_ipdiMKUDVrjQNJsSFurQD2cio-xAUU6293qD483S19D9GMV1EMZhJhmhcL_XfRDvBo-a4wInSvbKNVfY9OLorntDtfw4g_DsKe8hxLGARYH68hoq2plpKoTKnyv-6NU_92zoqbt8QJNRlBs5-jGcZBlUUeRPlQs8PDDoUZK_QkEih2lLbF_YpT58j5-hMy5nJAx1FfGhWjX8HBOdVUIU7icYb9xEp9HO70zOmvgP7-jqvBG4h1p89ao3rG6N3cOaTycP9ZCgBIh8UgvwmT-vtxssRWryOh6cUrR6gEedc-QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردشکنی مصرف CNG پس‌از تغییر نرخ سوم بنزین
🔹
عظیمی‌فر، معاون وزیر نفت: یک هفته پس‌از تغییر نرخ سوم بنزین به ۱۰ هزار تومان میانگین مصرف CNG در کشور نسبت به نیمهٔ نخست شهریور و مرداد، تقریبا ۲ میلیون مترمکعب در روز معادل ۱۱ درصد افزایش یافته است.
‌
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/462423" target="_blank">📅 13:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462422">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tliKV4XL-RQvtAb3_1i8I095pHy-E2fDbPYLz8WVBRy1D7QG0oxNpzyDSkRfJn2bAU_UPYNtnXfexD2Teii1_1v2mshtM60EhLGRXhbMdjo6cfyX0JOAyXBMaSITiReYVZG-CKMHq3kNsAMXpYFNyTr4fw7qsNYZDWhICSQPgxJiESZhvNaE3FuW83yoahuZI9zZ-h5dYh86D_D_CC4CaiyBqjDEauFTT_P2MrkgwvsUZPFreFGk2DoXJGy50yyfi87gia-SbOKvZsGq_IeW9Bxa8e8M_Y4dqLVUi9Nh_SS55p7STrpivmou88ykl-BU090ev3EBEQP_LjR1ezIz7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین: آماده‌ایم قاطعانه از حقوق ایران دفاع کنیم
🔹
وزیر امور خارجه چین وانگ‌یی امروز در دیدار با عباس عراقچی، همتای ایرانی خود در پکن، با تأکید بر شراکت راهبردی پکن و تهران اعلام کرد که چین آماده است ضمن تقویت گفت‌وگو و همکاری با ایران، از حقوق و منافع مشروع جمهوری اسلامی ایران دفاع کند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/462422" target="_blank">📅 13:16 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462421">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQoDhpl1lV3Xh7r9x5hRQeZ2JgWDdF8CydJrSSFihEAOnm-AzYV6uWfpD-_4bbatMIfO3TXk0al9GcPUFMBJobi57ZwjDdXNrc7iuIM_zAMmYByGRbNQOr1Vh1OTndeUjtouyMa2Gj1mdHeDuw46MxG1Fp8lAQwZLFwgj-rS-dnUYua0NXpeASrwm3AQVwSAw2wmt-8IALpgEfz456igUEzgPX2y7j8BhL3YiOK1G3nJTRZzTKTO6eWFpa2YuNW8ZdYnrhnuo4DuCsVUvIyvIXD8SoGoHXIsKCqMfcv-c3_2vNXCe7t4VOA6MhGH5mhuC0jeFImWXY9JCI7ay4ayeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: آمریکا به مونتاژ تصاویر و روایت‌سازی هالیوودی عادت دارد
🔹
سردار محبی در واکنش به روایت رسانه‌های آمریکایی دربارهٔ نجات یکی از خلبانان این کشور در ایران گفت: آمریکا عادت دارد روایت‌های هالیوودی ارائه کند. از ابتدای جنگ تاکنون نیز رئیس‌جمهور آمریکا بارها در خیال خود و در فضای مجازی پیروز شده و ایران را شکست داده است.
🔹
آمریکایی‌ها برای جبران شکست‌های خود، بخش‌هایی از فیلم‌های مربوط به مناطق و حوادث دیگر را کنار یکدیگر قرار می‌دهند تا چنین صحنه‌هایی را خلق کنند.
🔹
هم‌زمان با انتشار این روایت، تصاویری نیز در برخی رسانه‌ها منتشر شد که نشان می‌داد قطعات جنگندهٔ F-15 هدف‌قرارگرفته در همان ایام، در داخل فرغون جمع‌آوری و حمل می‌شد.
🔹
آمریکا باید بداند که این‌گونه روایت‌سازی‌ها دیگر کهنه شده و نمی‌تواند واقعیت‌های میدان را تغییر دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/462421" target="_blank">📅 12:59 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462420">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">امحای مهمات عمل‌نکرده در خارگو
🔹
بخشدار جزیرهٔ خارگ: درپی انهدام مهمات عمل‌نکرده از ساعت ۱۵ تا ۱۸ امروز در جزیرهٔ خارگو، احتمال شنیدن صدای انفجار ناشی‌از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/462420" target="_blank">📅 12:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462419">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGAprHb_xA1UMB-0nJ7DEMwUy48Pjsale6j0PcX3ltbX3MfDmst9HtJyGx0shiFe0c_oXGn1-3akpmuNNFAmu5WdvdE_xQDzyCnfwWdHif05RwvpOWckkbAiAZuMfwcTYdvCSyd20_6DPyil8d2erCzZjHCmZ706yWr90pZ6rRQp2znhMYpa7X1dZmTSbwVmE9rIc3fCS6-ykj5AefmmsVJGvNWg0jkYWXJnY8gI4TgiM8FoWuluEov42ykun6TKztHfazAqvc8oP_ofwqMymhs6fCfcbWcb4r3P3xlISY_uL1eCfj8xHjt49fAw_rxLjh3j8p1_ynfQPPRm8nOqgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با رشد ۳۶ هزار واحدی به ۷ میلیون و ۵۵۸ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/462419" target="_blank">📅 12:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462418">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fx69Z9fbhIXB3Eu3CvelOV4KwUvMMYN0OdbQjZT1qE3w_LTuOWu6tsG0orL02Ystqw8Y4Q3Tnih7dfVostJmGoH8S3pejMuZys8VjCyY-npBwxrwco1BEbpraWbK9TaDAeU2wIePQZ5Jic7z19g42A3M21Bdm8iBKMG-sDjKJaaVgFpvRC2zhFULgmdzW_cSGSJhs5Js7xR4ePK0VYmq3pbBLaqKt61vT_FpCZYWOmPVuo9UGNsBVXXmw3y35ICgXMDDEQ4x7wKIHYpecEe7-2xpSnxhbsA8m_ieVExzn3is9c3Q0WqdcuqEOjgndiAe1yLHzNIet8-UaGXY9F0eYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بریکس؛ فرصت ایران برای فعال‌سازی دیپلماسی معدنی
🔹
اختصاص یک بند مستقل به «مواد معدنی حیاتی» در بیانیه پایانی اجلاس سران بریکس در دهلی‌نو، در کنار تحولات مشابه در اجلاس گروه۷، از افزایش اهمیت راهبردی این منابع در اقتصاد سیاسی جهان حکایت دارد.
🔹
در این میان، ایران می‌تواند با تکیه بر ظرفیت‌های معدنی و زیرساختی خود، پیشنهاد شکل‌گیری چارچوب همکاری بریکس در حوزه مواد معدنی حیاتی (BRICS-CMCF) را مطرح و همکاری میان اعضا را از سطح گفت‌وگو به پروژه‌های واقعی و مشترک هدایت کند.
🔹
با توجه به ریاست چین بر بریکس در سال ۲۰۲۷ و تأکید این کشور بر تقویت همکاری در حوزه منابع معدنی راهبردی، فرصت مناسبی برای تبدیل بند ۶۷ بیانیه ۲۰۲۶ به یک دستورکار عملیاتی فراهم شده است.
📌
دیپلماسی معدنی می‌تواند یکی از مسیرهای جدید ایران برای نقش‌آفرینی فعال‌تر در بریکس باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/462418" target="_blank">📅 12:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462417">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🎬
پیشکسوتان سینما‌ از اهمیت حضور بیمه دی در کنار خود می گویند
🎥
گزارش ویدئویی از   دورهمی اهالی سینما در هفته بزرگداشت سینما با حمایت بیمه دی
#رونمایی
از آمفی تئاتر و کتابخانه خانه سینما</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/462417" target="_blank">📅 12:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462416">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/462416" target="_blank">📅 12:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462415">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">محدودیت‌های ترافیکی آخر تابستان در جاده‌های شمال
🔹
تردد موتورسیکلت‌ها از ظهر امروز تا صبح شنبه در جاده‌های چالوس، هراز و سوادکوه ممنوع است.
🔹
در جادهٔ چالوس، محدودیت مسیر تهران و البرز به‌سمت شمال از ساعت ۱۴ جمعه آغاز و از ساعت ۱۵ مسیر پل زنگوله تا تونل البرز بسته می‌شود؛ مسیر مرزن‌آباد به تهران نیز از ساعت ۱۶ یک‌طرفه خواهد شد.
🔹
تردد کامیون و کامیونت در جادهٔ هراز نیز در ساعات ۱۲ تا ۲۴ امروز و ۸ تا ۲۴ پنجشنبه و جمعه ممنوع است و در صورت افزایش ترافیک، این جاده در روزهای جمعه و شنبه به‌صورت مقطعی یک‌طرفه می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/462415" target="_blank">📅 12:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462414">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e2c10ff6f.mp4?token=XUYJtJtYx3Y0_aYs4lFi6uQ5AJ8fT0hmbnF4iatBxQ9J2xv4LsVySfXpoyraJam3rMHSvaa_3cSGIJMMYgUWZCyKS-YhOkoh8trLFOIvvT-Zn86QrDnU6BL9lc5A0vNTlmWXuqMMwxdpYi5TM3oz-WhUwSKxWbTF_j_8TNot2Pz7LhgQYr7oPRDsxaEyh-k4MxxBqDKLROVEUXokzM7Z9V-j6FZbHyExWUvob1eZgm9WTeR_fPsavj-bcagB1UdaXOvdUZ2RZcL2Cau57njhyoUbSYBSmGP2184duMAr1H39anHaCdXPpND7Iiq0Zs_9RsT3PG30pyvGeosvfpYmEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e2c10ff6f.mp4?token=XUYJtJtYx3Y0_aYs4lFi6uQ5AJ8fT0hmbnF4iatBxQ9J2xv4LsVySfXpoyraJam3rMHSvaa_3cSGIJMMYgUWZCyKS-YhOkoh8trLFOIvvT-Zn86QrDnU6BL9lc5A0vNTlmWXuqMMwxdpYi5TM3oz-WhUwSKxWbTF_j_8TNot2Pz7LhgQYr7oPRDsxaEyh-k4MxxBqDKLROVEUXokzM7Z9V-j6FZbHyExWUvob1eZgm9WTeR_fPsavj-bcagB1UdaXOvdUZ2RZcL2Cau57njhyoUbSYBSmGP2184duMAr1H39anHaCdXPpND7Iiq0Zs_9RsT3PG30pyvGeosvfpYmEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خسارات جنگی آمریکا «رسمی» شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/462414" target="_blank">📅 11:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462413">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">استانداری اصفهان: انفجار کنترل‌شده تا ساعت ۱۳ امروز در جنوب استان انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/462413" target="_blank">📅 11:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462412">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشکده خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7-tHDgkzbbOR5K6BdnNNgV2Bz43LjaTl5k2l5R9XBdT59bLMS9g0PbWWLRzrJgtTVSuWzzW5lsa9vll8wC9xFD2pKPi6oNRnGWuPg2iClnVE4q9gJsnrit52db2by5stTJQKN8kQffsKTQle7AgymCdVrL8TMCyU7gX0Xj5u_ytAw1gtzFyftASN0RcdycLK1I2Mguw0cLiZEgzoVbdpKQp5qFDcdTKIDHggs5ZllA1Xq_e_avbYw4fKOWuPbSo1SWeSXYLU7aea1d4JXloRDn7SqdCw7UpIWjnOAacMcsWZHGIPH9pBhyZlHAW7ITfeHHDzAQ7TFo_LwioxY_enA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
ثبت نام بدون کنکور در دانشکده رسانه فارس
رشته سینما و تدوین، ترکیبی از هنر و تکنولوژی است که به شما این امکان را می‌دهد تا داستان‌ها را از ایده تا پرده نهایی خلق کنید.
در این رشته با اصول فیلم‌سازی، فیلم‌برداری، تدوین، صداگذاری و جلوه‌های بصری آشنا می‌شوید و مهارت‌های لازم برای تولید آثار خلاقانه و تاثیرگذار را کسب می‌کنید.
✨
مهارت‌هایی که می‌آموزید:
🔹
فیلمنامه‌نویسی و داستان‌پردازی
🔹
فیلم‌برداری و نورپردازی
🔹
تدوین تصویر و صدا
🔹
جلوه‌های بصری و گرافیک سینمایی
🔹
کارگردانی و تولید محتوا
💼
فرصت‌های شغلی آینده شما:
🔸
تدوینگر فیلم و برنامه‌های تلویزیونی
🔸
کارگردان و دستیار کارگردان
🔸
فیلم‌بردار و مدیر تصویربرداری
🔸
طراح جلوه‌های بصری و موشن گرافیست
🔸
تهیه‌کننده و مدیر تولید
📞
همین امروز قدم اول را بردارید!
⚠️
مهلت ثبت نام تا 26 شهریور ماه می باشد
☎️
تماس: ۰۲۱۴۲۰۸۲۹۴۱ | ۰۲۱۴۲۰۸۲۹۴۲
📱
ارسال
عدد ۱۴
را به شماره
۵۰۰۰۱۰۱۴
🌐
لینک سایت ثبت‌نام
🔗
futurix.ir/go/rxDxXO
🎓
مرکز آموزش علمی کاربردی خبرگزاری فارس
🎓</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/462412" target="_blank">📅 11:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462411">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fce0e6f6d6.mp4?token=AHn6-PjgOvhL7v9975-T8yAxdWcui-14HsczNO7ChnkuUWokeSzmZwBnLlCn6KmhamvwjWOKCNhTcIHgntWDzdbqHjWOMxz4epqEHxOSy3TmKAozsxI6pfvKnirrRIBQ_aWKZ_wkvUlwkPi-xMW6Gkl1QB85i4WHstcaJ-eRm7DvB9f8rNID34oPlqzayu4in7q1rVJQVkFrGvZr03BOb2XteXSyqv9d6S76NH1bKzTrH3NITkE7Bu2qdsdO-wIY9GXUcx3XciHV4540j4eouxviMeiPQUxl8L5JAZXaPXRkZpk_zPnLO7kXJ1kazZ1EwztqPghmVbOnWAgEpld4NZC4hE45p3ye8EOMPcTtkQwR20iKjQ3DSRdavkM1QiNcYMpf_srFaUKaFyE8AR7fgitgpkke7rlaErn2uEHaud2paQ42BN1y-v74JB6Fmzj9KClSG0Z0qPRlqBKLDHEl0Zz0zFvbyZfNF1pTg6cr5uTLV7eCkBHqxZem-TiDsUWTNiYjor92xKYLic3hwUWXRQOST5Y-PqVGGWagO3f9iN0oL2pzE589LZhQgQcxxE8r3QPZqZB6eaM2mT5OPS7TGY4_a_aOtPmXus8ETNwL5OQHZuvhCrPaWuFQID3cyN1p_Fu_7qdxMMSYBP8giGdXOd5HJX-Dm4TFQ6J6xSd75tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fce0e6f6d6.mp4?token=AHn6-PjgOvhL7v9975-T8yAxdWcui-14HsczNO7ChnkuUWokeSzmZwBnLlCn6KmhamvwjWOKCNhTcIHgntWDzdbqHjWOMxz4epqEHxOSy3TmKAozsxI6pfvKnirrRIBQ_aWKZ_wkvUlwkPi-xMW6Gkl1QB85i4WHstcaJ-eRm7DvB9f8rNID34oPlqzayu4in7q1rVJQVkFrGvZr03BOb2XteXSyqv9d6S76NH1bKzTrH3NITkE7Bu2qdsdO-wIY9GXUcx3XciHV4540j4eouxviMeiPQUxl8L5JAZXaPXRkZpk_zPnLO7kXJ1kazZ1EwztqPghmVbOnWAgEpld4NZC4hE45p3ye8EOMPcTtkQwR20iKjQ3DSRdavkM1QiNcYMpf_srFaUKaFyE8AR7fgitgpkke7rlaErn2uEHaud2paQ42BN1y-v74JB6Fmzj9KClSG0Z0qPRlqBKLDHEl0Zz0zFvbyZfNF1pTg6cr5uTLV7eCkBHqxZem-TiDsUWTNiYjor92xKYLic3hwUWXRQOST5Y-PqVGGWagO3f9iN0oL2pzE589LZhQgQcxxE8r3QPZqZB6eaM2mT5OPS7TGY4_a_aOtPmXus8ETNwL5OQHZuvhCrPaWuFQID3cyN1p_Fu_7qdxMMSYBP8giGdXOd5HJX-Dm4TFQ6J6xSd75tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد «تو جنایتکار جنگی هستی» بر سر وزیر ترامپ در کنگره
🔹
جلسهٔ استماع بسنت، وزیر خزانه‌داری آمریکا در کمیتهٔ خدمات مالی مجلس نمایندگان این کشور با اعتراض‌های پیاپی فعالان ضدجنگ به تحریم‌های غیرانسانی علیه ایران همراه شد.
🔹
طبق گزارش تصویری شبکه ان‌بی‌سی، یکی از معترضان خطاب به بسنت گفت: «تحریم‌های علیه ایران که غیرنظامیان ایرانی را به‌کام مرگ می‌کشاند را متوقف کنید.»
🔹
معترض دیگری گفت: «اسکات بسنت! تو یک جنایتکار جنگی هستی. تحریم‌های علیه ایران را متوقف کنید. شرم بر همهٔ شما که اینجا نشسته‌اید و اجازه می‌دهید مردم به‌خاطر یک جنگ ناعادلانه و غیرقانونی بمیرند.»
@Farsna</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/462411" target="_blank">📅 11:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462410">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qczRWaJeGY1ayVaTkT__ckhtRi2tGUddGbz44qwcUHAYMUXq1ZaarCagROQZpZ3pXaF3LPB9_wXS51ZVCkEkPO4whYsP-efAv7gXY49nDOmtk3ioTAspZW5W3Z4yFPVIu_hkVZDyiZWTVUUe9U6Du8CpynYvTDHk8lQliSiuU_VZbd1QXssjxTYCNeFn__gi66zpO38A8q07lNms2wIOLzNN37TV1iilSoWn_INFLVR0maOu8kvvDEQti0cfxLPmjOoYch1YWdDckQL-XfFcVYZXtSebPl7thvx3FcQKfxnnGXLrbeaRT1LFejL5Ws-BVCgGFR2qc7GO5PA_V1aOdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردشکنی قیمت گازوئیل در آمریکا
🔹
انجمن اتومبیل آمریکا اعلام کرد میانگین قیمت گازوئیل در آمریکا امروز به رقم بی‌سابقۀ ۶.۲۷ دلار در هر گالن رسید؛ رقمی که حدود ۲.۵۸ دلار بیشتر از قیمت گازوئیل در یک سال گذشته است. @Farsa</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/462410" target="_blank">📅 11:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462409">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDIphS7z8XQDlEC-VB8Lusq8tNEm1aP9UUeUPW9s8eTo6av8_XDdSWByPUV1CKSl_SueTpYTnqrMA1ihLBm91r8vP3Ks3DhTz3by74P-0yLbCW0Q9ukWmWUGaKbKeReoBpgtcU0ifZq2jM1KWWG6Sc5__vbrfiCcbCi5JRVun6EvR24V0PZ07wS44bg7qQVR_9V4Jjb5Ss9jN57_BxRAJZVG8RTkkULFujW9tPBwZ07I2jR_RL01H-BdO0wGuksPOuNRDhwmJNVJ-Clz6LUz1eQu6ZpfZwCVJxquqvevMx5mmP2Lx2NEwbfZ5byY5WqCxNjUeyfdwNYvvJ9IQaHwiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر وحیدی: تداوم حضور آگاهانه در تمام عرصه‌های حساس ملی تنها راه پیروزی نهایی در این جنگ تحمیلی پیچیده و مدرن است
🔹
فرمانده‌کل سپاه در پیامی به‌مناسبت دویست شب میدان‌داری و حماسه‌سازی ملت ایران نوشت: دویست شب ایستادگی، دویست شب بصیرت و دویست شب تجلی «بعثت ملی» در میادین و کوی و برزن این سرزمین اسلامی، در حمایت از رزمندگان اسلام و نیروهای مسلح مقتدر کشور، حمایت از ولایت و رهبری معظم انقلاب و خونخواهی امام شهید خامنه‌ای عزیز(قدس سره) برگ زرین دیگری بر تاریخ پرافتخار انقلاب اسلامی افزود. ملت بزرگ و الهی ایران اسلامی در سایهٔ این ایستادگی دویست‌روزه چه از حیث معنوی و عرفانی و چه به لحاظ سیاسی و جایگاه بین‌المللی در افقی بالاتر قرار گرفت و شخصیتی بسیار والاتر یافت.
🔹
در این شرایط خطیر و سرنوشت‌ساز همدل و هم‌صدا با خیل فرماندهان مسئولان و رزمندگان غیور و تاریخ ساز  سپاه پاسداران انقلاب اسلامی، خاضعانه از آحاد ملت مبعوث و هوشیار ایران، از پیر و جوان، زن و مرد و از همهٔ اقشار، اصناف و سلیقه‌های مختلف سیاسی و اجتماعی که در این شب‌های تاریخی، حماسه‌ای ماندگار و بی‌نظیر تاریخی آفریدند، صمیمانه قدردانی و سپاسگزاری می‌کنم. مردم بزرگ با این ایستادگی تراز جدیدی از انسانیت و شرافت را به نمایش گذاشتید و تمدن جدید مبتنی بر کرامت انسانی را پی افکندید.
🔹
ای مردم آگاه و ولایت‌مدار، شما از همان ساعات آغازین جنگ تحمیلی سوم آمریکایی-صهیونیستی و شهادت قائد شهید امت آیت‌الله العظمی امام سیدعلی خامنه‌ای (اعلی‌الله مقامه الشریف)، با حضور اقیانوس‌گونهٔ خود در مساجد، بقاع متبرکه، مصلّی‌ها و خیابان‌ها و میادین سراسر کشور، نه فقط سوگواری کردید، که «نمایشگاه عینی حیات و ارادهٔ ملت» و « نماد وقوع تغییرات بنیادین در معادلات اجتماعی-سیاسی» منطقه و جهان شدید.
🔹
این حضور میلیونی، «بیعتی مجدد با رهبر معظم انقلاب، حضرت آیت‌الله امام سید مجتبی حسینی خامنه‌ای (مدّ ظله العالی)» و «تجدید میثاقی عمیق با آرمان‌های امام کبیر و رهبر شهید» بود که نشان داد پیوند امت و ولایت، نه فقط ارتباط سیاسی بلکه، «پیوندی ایمانی و عاطفی ریشه‌دار در عمق جان‌ها» است.
🔹
این میدان‌داری هدفمند و راهبردی، بزرگ‌ترین پشتوانهٔ معنوی و عملی برای نیروهای مسلح و رزمندگان اسلام در خط مقدم دفاع از حریم امنیت ملی و تمامیت سرزمینی است. دشمنان که گمان می‌کردند با فقدان رهبر و شخصیت‌های کم‌نظیر، ملت از نظام و ارزش‌هایش منفصل می‌شود، در محاسبه خود شکست خوردند و اکنون با تمام قوا برای ایجاد خستگی، یأس، تفرقه و فشار معیشتی متمرکز شده‌اند. اما این «اراده جمعی» و «سرمایه اجتماعی عظیم» که در سایه وحدت و اتحاد مقدس ملی شکل گرفته، اصلی‌ترین سد در برابر توطئه‌های جنگ ترکیبی و شناختی دشمن است و باز هم به شکست بزرگ آنها خواهد انجامید. این استمرار مقاومت در میدان و فوران الفت، معنویت و همدلی بزرگترین قرینه‌ای است که به یقین ما و پیروزی این مردم بی‌نظیر، می‌افزاید.
🔹
ای مردم بصیر! تداوم این حضور آگاهانه در تمام عرصه‌های حساس ملی، از جمله «اقتصاد مقاومتی در سایه وحدت ملی و امنیت ملی»، «تولید علم و فناوری»، «حفظ آمادگی همه‌جانبه دفاعی و تهاجمی » و «افزایش هوشمندی و هوشیاری در برابر جنگ رسانه‌ای و روانی جبهه دشمن»، تنها راه پیروزی نهایی در این جنگ تحمیلی پیچیده و مدرن است. پیروزی‌ای که با الطاف بیکرانه‌ خداوندی و استمرار و تبلور عزم و اراده جمعی ایرانیان، قطعی و حتمی است.
🔹
سپاه پاسداران انقلاب اسلامی مفتخر است که به عنوان سرباز ولایت و مدافع حریم امنیت ملی و منتقمان خون پاک امام شهید و دیگر شهدای اقتدار ایران اسلامی، با تمام توان در کنار شما ملت بزرگ ایستاده است و از هیچ تلاشی برای صیانت از این وحدت الهی و سرمایه راهبردی نظام که تضمین کننده غلبه بر جنگ تحمیلی امریکایی صهیونی است فروگذار نخواهد کرد و به فضل الهی با هرگونه خطای محاسباتی و تهدید تعرض و شرارت دشمن اهریمنی قاطعانه و پشیمان‌کننده برخورد خواهد کرد و یقین دارد این مسیر نورانی و تمدن‌ساز تحت رهبری حکیمانهٔ مقام عظمای ولایت و رهبری و فرماندهی کل قوا (مدّ ظله العالی)، با قدرت، حکمت و بصیرت بیشتری تداوم خواهد یافت و همانگونه که زعیم شهید فرمود؛ این شما ملت نستوه، شجاع و مبعوث هستید که کار را تمام خواهید کرد. انشاالله.
@Farsna</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/462409" target="_blank">📅 11:06 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462405">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fYi24Tk6uNZ0fArTpUzkkquoPpo1ggv53WPPRbZS7kUxfhvjUM4iNOXdv4wUGIILS-hozmu4REy_m0n2Kz06vxocffWBOZiM3fcsBb07eG2ZvOnhA_XJnWtWguemioHdcBRhodBPPahJTN_UKtaHzKkAzFEooK-7W5bhCZXRzp6DPtn9EKYvwGyEwmO0flL3c_lr8t4b7YQJLFr1XUEEPHNZisqFHm8gOBT4W5ER1U2L9lnW1Y5qRkdwl6-xgy-x90ITI7S3KkcXK9n1X-UgFJITDx-9JO7yZuZW1JyZMOua2n5y1SP7brBRgDz9GF9wqCDAvZvGDsn9RNsx9Th-PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NIhIUu2lfMPYLWhUV4fXxbhhDlIunVzhQ7tOeZ7dNW7lM_pX09XPLroSYmXOmTPWzRv6JU6p15GqcN76R6yjbhDNhTOp4RBj63OBfKSXwejhl3gFerfHuyKRyizrlhOk6nCeGn1o6h3fgCV-Y4c_oz7ymqBFWspx-3FOdkbawZYIHXArzwQzZvZSiw8HhNuCs6wRlWUHYqKqZp8rTE4pQ6k22cU0jDl_MGEsTbcfS86irFW1A-ykqVlbB4-34kK9PGkORTGNalTTVS2yVGpOtaV1N_NnQv7-P_NdBG7vU28-qxKQkMBPaa0o9zR_aQIHZqvMvHEgpOL0wJLtnmtknw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DSttPwDpMKieN2w8AzV8ZrojeWDaI0qYsD5MLPG5-okdfHJ06DA4BPvn54j9xTveEkAfx7IBvDjZFSwNYtPMIqyGqIJ1AMd4iYU7uGyt7zwBW_fu-wffyZyoT2ZvB2IjZYWPBMuRYD6edk2c4aVTxB5nIoJWLzY4hTKZaWtirdxi9idJXi58OY_i5lh9WzILnwkaaGrfcN_c9ypXve51kCC2mD6yKh0_e4uO9_74G1lx7H9gbwnCr-CVhaoYjh7N1HoZNZPxJZkKHZZ7kPYngjBNWJxHmTz7K3rBqRZgx6_fdOvV4WtCCd9XV2YzJiVh_Enw68BU9i22_pCST-AVbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2135f1e48.mp4?token=cAzGkKm38k5b-plZIfbcxHVkUWfW5tHmBTUvfmiYYnFQmyoPmFWyo6wD_o8evjTZfd8o1fbn_izvau3P7P9Lj0oJhK_4srAQt9pWLDDAK_X2i_RxHibSw0se99xrZ98nSOXDMMAsf5__YgbjrPJxXypx4wQ_0Fmy2VDVlReZTLY-ef6lOn9wHFygNfZkcZoOJ9kEip_UwYq2pKvltVdICBR0MnTAZQvpyFFu5FeEQERBjm5OEkV4ONDOZtKH3Z1Ih5dWur2uU0QDJo57WTfh7k6mqp2DDYkrcfaQmAXk66soFJUvVFg2BVA56eBMKc431BfHKw9VsROZKjyxIpxFuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2135f1e48.mp4?token=cAzGkKm38k5b-plZIfbcxHVkUWfW5tHmBTUvfmiYYnFQmyoPmFWyo6wD_o8evjTZfd8o1fbn_izvau3P7P9Lj0oJhK_4srAQt9pWLDDAK_X2i_RxHibSw0se99xrZ98nSOXDMMAsf5__YgbjrPJxXypx4wQ_0Fmy2VDVlReZTLY-ef6lOn9wHFygNfZkcZoOJ9kEip_UwYq2pKvltVdICBR0MnTAZQvpyFFu5FeEQERBjm5OEkV4ONDOZtKH3Z1Ih5dWur2uU0QDJo57WTfh7k6mqp2DDYkrcfaQmAXk66soFJUvVFg2BVA56eBMKc431BfHKw9VsROZKjyxIpxFuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سی‌ان‌ان: گرانی سرسام‌آور سوخت، اعتراضات جهانی را شعله‌ور کرده است
🔹
به گزارش سی‌ان‌ان، معترضان در نقاط مختلف جهان به خیابان‌ها آمده‌اند تا خشم خود را از جهش سرسام‌آور قیمت سوخت و خاموشی‌های پی‌درپی ابراز کنند؛ چراکه جنگ چندماهه آمریکا با ایران، هزینه انرژی را در سراسر جهان افزایش داده است.
🔹
در سوریه، معترضان در یک بزرگراه پرتردد لاستیک آتش زدند. در گواتمالا، معترضان برای مطالبه اقدام فوری دولت، جاده‌ها را مسدود کردند. در پرتغال هم شماری از صاحبان کسب‌وکارهای محلی و کارگران در مقابل خانه نخست‌وزیر راهپیمایی کردند. فیلیپین هم شاهد اعتراضات گسترده بوده است.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/462405" target="_blank">📅 11:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462404">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZm00cM2yfzExwCU4DT1Cw-TPYWiIoK0e7OjUIi2nvHcUkxDqmJ-6EqLIAwU62yIW8GDOVusm816Wl66TXHi6QQToZve-TolAy8labch4SfNDM2BtmxIees4DFKvW9E_nIFp0yYKCSJlT6VXh1VbFy9HpcURFs2TG8Xh3Iff_oGoZzzSJS1FFrCguqGzuPlzfW-0A2VKWeejB8usI_K9U9OTDvbFU_setY3SCsvkxvCKXmwoDGvd2n5Fvdx8TfLHC5iAm-OtpBjYu00qGVz-l3S1vORyirs3B2xaw0_08urNq3G9jN6U3Gm7IRP0a13_Hat0BlVyHip1F7BIpos-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه فوری پاکنژاد و شریعتمداری در آستانه مجمع هلدینگ خلیج فارس
🔹
طبق خبر رسیده امروز محسن پاکنژاد وزیر نفت و محمد شریعتمداری، مدیرعامل فعلی هلدینگ خلیج فارس جلسه مشترک برگزار کردند.
🔹
پیش‌تر رئیس‌جمهور دستور داده بود تا مسائل وزارت نفت و هلدینگ خلیج فارس از…</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/462404" target="_blank">📅 11:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462403">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b7303b54.mp4?token=MUhVOdR9TyAuneLHp-FEF0Y58A1u1SEcKfvk_Ep45JQEkkBa9N0EPdvMcmlXHacMiv0dUw8xTFM54gqUbgqoPGJc-R-Q-EySGq-MjaubZVm22MhgToPgyG3vuvDF0fMBuEuVKKMYQW_vQcIYx0gaIyHghfjBFjqieZ8oOSTEK-Tl-OPXoYT1iKJ0wBr28ueCsYmc1NZNvhRHl6J58a19EN67aZzHgR1FNsrbmhek9NDiXVJPnfGPACL8TjxYXlWq1zcmcn1HyE7QKqGqdyRP9cEKwqgxLDmLMJDB4VC9LEJcRiwG19JasEmYjg_6muOWB4FIQECxeAxMDgjAivW_sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b7303b54.mp4?token=MUhVOdR9TyAuneLHp-FEF0Y58A1u1SEcKfvk_Ep45JQEkkBa9N0EPdvMcmlXHacMiv0dUw8xTFM54gqUbgqoPGJc-R-Q-EySGq-MjaubZVm22MhgToPgyG3vuvDF0fMBuEuVKKMYQW_vQcIYx0gaIyHghfjBFjqieZ8oOSTEK-Tl-OPXoYT1iKJ0wBr28ueCsYmc1NZNvhRHl6J58a19EN67aZzHgR1FNsrbmhek9NDiXVJPnfGPACL8TjxYXlWq1zcmcn1HyE7QKqGqdyRP9cEKwqgxLDmLMJDB4VC9LEJcRiwG19JasEmYjg_6muOWB4FIQECxeAxMDgjAivW_sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گنج‌یابان زیر پای سنگ‌نگارۀ اشکانی را خالی کردند
🔹
چند روز پیش یک کوهنورد در مسیر قلۀ یخچال همدان، متوجه حفاری در پای یک سنگ‌نگاره ثبت‌ملی دوره اشکانی شد؛ حفاری‌ای که احتمالاً با تصور پیدا کردن گنج انجام شده است.
🔹
حالا بررسی کارشناسان نشان داده حدود ۱.۵ تا…</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/462403" target="_blank">📅 10:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462402">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYfewUUwsVSYu6QSxzavsO0cNecd8XHIGf9zZwiOgpTYCxJpZ0Xi38D9iN2E4Y9iJMMJ1FpALhPWbHEOnYFypirOBMrNU20DJksk0W9lswWT8YXEXdkv2qxu8BktcvWcRSFpbP5y8uAOB5VKo7cH-BJmm1l4I0O5e15ILPEQcCAHBB9j8bCCuxuLBPVrmiIQegW5T4BOmgSBBHg3eybzqUq_tJ8wJi918GaaXEDvNB1Yt7gdbYVv7PEeLHIELDnDUfwJgrz4CzNgdGfJO_P1-qUKMfRh6hJM0RVDjdmlq2ct1PIKgrigoUodfqJ8VPXbz1f-jgjNDRs6wglx99-t_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
یوسف مزرعه گل سوم ایران را زد
⚽️
ایران ۳ - ۱ امارات ‌@Farsna</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/462402" target="_blank">📅 10:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462401">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tswhwVKrf7l-Bam9Bbgfm15ZoCHOuo_1FIiJYX7OdoABrVyxGi3oQQbBM5moXnTsoB8wLvd7gwU8It6F4qqFxOKzeK4IIZj1wh2icm3u755uNReW-47T2mGqH-D53i0XVXO62CR2X8NHi8TJieK_l6v5QGT9mfZi8h1cSuBK4P5129dZdNDVN8fPyOohNoun2Qwcve71YXH-co31Q-NAvlpx4coCRigznKz08stIKN7ddcAHi_E3gVM0-AdejmnCT4ZR83Rj1jV4JS1JXe-qpixwHAs8CWgUyFzSi8m69P2hs2YX14SYM01U6BvE2UZh9fHUnBuZQXA9-ZnrO1eEAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به‌بزرگی ۳.۷ ریشتر در عمق ۱۰ کیلومتری، کنارتختهٔ فارس را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/462401" target="_blank">📅 10:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462400">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dec8b30492.mp4?token=kmlIG9lYEqv_bfuK9UAKZf-pOiv__7DaHwL9NE77Uxq6f-REJYp4M-8tcNnyER2SB7Abj8qf1_085z6AF9rdJRjhvL5m-ACACKKppVWLD_ofnrQuR1mZc06dVSg4lDzQQbP7HXyxrKjY5P28bYC8L77C3mCObuqtQhGHbXhF7nsAf_NdYZb0BfTEW0HpwsQ3Bz3lk5Zxb5KRm2FJF-Z2dEzoIlPwizK_l_NXheJJArvF56AI83DB4Gw_PvllP9YjoV37I_3gbwPNKCd3eYo2_qQdsDmPo17seWcG2gchLSpJnUolLsK_cnqPVXDCvM2Pnx7_uT3U7-QOJFROR-A--Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dec8b30492.mp4?token=kmlIG9lYEqv_bfuK9UAKZf-pOiv__7DaHwL9NE77Uxq6f-REJYp4M-8tcNnyER2SB7Abj8qf1_085z6AF9rdJRjhvL5m-ACACKKppVWLD_ofnrQuR1mZc06dVSg4lDzQQbP7HXyxrKjY5P28bYC8L77C3mCObuqtQhGHbXhF7nsAf_NdYZb0BfTEW0HpwsQ3Bz3lk5Zxb5KRm2FJF-Z2dEzoIlPwizK_l_NXheJJArvF56AI83DB4Gw_PvllP9YjoV37I_3gbwPNKCd3eYo2_qQdsDmPo17seWcG2gchLSpJnUolLsK_cnqPVXDCvM2Pnx7_uT3U7-QOJFROR-A--Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امارات در دقیقهٔ ۵۷ یک گل را جبران کرد
⚽️
ایران ۲ - ۱ امارات @Farsna</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/462400" target="_blank">📅 10:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462399">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0HOoabQeiCmILnMQOX9qK-4BXxhNCHpqPTpUQ6Mt_1HVXwUDe82H4YUasUs3wzjnt9rocDD1X72exB0ewtujTSLQ8mFPgfS70pmBPL9GPXFubZPHsqOjq9Ebjdbpf_mOfk236cmgn5PxeEOeOKj51gls_umrS4OYOVlWcF5vKRzd56NVDOu61ihigDjadFdrYZ0QpFEqYiQl4V85_zobzmhgu6oYG-_nm_F2-jD4wHCAasNPdx5Ooe4ElkP8Pzb1m7Y6L0FMmifsb7n-NPhWFtXnN_rV01sUQp_8zbFWZHh3siiQT486Dbr0nESwRLShHw_x2okntSkd6vjImMqJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به‌دنبال اعمال تحریم‌های جدید بر روسیه و ایران
🔹
مجلس نمایندگان آمریکا قطعنامه‌ای را تصویب کرد که راه را برای رای‌گیری بعدی دربارۀ لایحۀ تحریم‌های جدید علیه روسیه و ایران هموار می‌کند.
🔹
در ماه آگوست بود که مجلس سنای آمریکا با اکثریت قاطع، لایحه‌ای…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/462399" target="_blank">📅 10:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462398">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe18d81e4.mp4?token=CrPMeQHIDVTSrRvEtqf3KpO3ATSJf-esN4Ya3zfcg5rbf0-v7ssBnoA8sXtXtDEAL0f-I72J4S-zG2uM_Em0aWbNIuNjAgs3KV7yDiMcq0ZjDeYcrESw4vRIUjZW85maEPjvYN9XexFsIA9u-FVzr1sG7HSuPTdOBSx9VhcAxNzoIR6Mg-Vv8ZFLtdbv2-Bjn5fD_e4hyxJmZdsWW7f-UQGJCTGVz9B7hvfqYPwimZM1oNeSqN8UrivSexo1cWrWj4xld4OIn-SdiwMigCi2YpvTrQpEuy_P9HwtDKMiggXT2prP7NKBPN86-YV6SCLmFGvc3WPQcffIQBlIdoIRDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe18d81e4.mp4?token=CrPMeQHIDVTSrRvEtqf3KpO3ATSJf-esN4Ya3zfcg5rbf0-v7ssBnoA8sXtXtDEAL0f-I72J4S-zG2uM_Em0aWbNIuNjAgs3KV7yDiMcq0ZjDeYcrESw4vRIUjZW85maEPjvYN9XexFsIA9u-FVzr1sG7HSuPTdOBSx9VhcAxNzoIR6Mg-Vv8ZFLtdbv2-Bjn5fD_e4hyxJmZdsWW7f-UQGJCTGVz9B7hvfqYPwimZM1oNeSqN8UrivSexo1cWrWj4xld4OIn-SdiwMigCi2YpvTrQpEuy_P9HwtDKMiggXT2prP7NKBPN86-YV6SCLmFGvc3WPQcffIQBlIdoIRDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهرآبادی دبل کرد
⚽️
ایران ۲ - ۰ امارات @Farsna</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/462398" target="_blank">📅 09:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462397">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e7bf963ea.mp4?token=vYCko5zqXKbnRyFrbT_5hP3Xi5Kla_dWNvQPpP9QfH3EQC3MeiRY4dA65gX4rkur1Z9rctWiR0MVHbyHIyWKmV9LdI8i_4dtGE36kDmhfjbdHHR7zS1XGKgMctJ-C3swagIXivQrufC95IKKSGIewBPMAnvrO-LQLo1rV-byJ-ROj6CqvMga1kHYgOri9tRQFOqE4SIc3Rlyz_NyTy08f7KyOo6RMtnaQdBoNM7BKIddGTNZkimAuK8Blg2iPjzwPuMTxRCcCBUHcPfZiWbtbNHZaSBbqNhNfVD443Rl9QK93-aATYWCK4l9IAoomypzstKbakkhz0R68Nj9cD6rAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e7bf963ea.mp4?token=vYCko5zqXKbnRyFrbT_5hP3Xi5Kla_dWNvQPpP9QfH3EQC3MeiRY4dA65gX4rkur1Z9rctWiR0MVHbyHIyWKmV9LdI8i_4dtGE36kDmhfjbdHHR7zS1XGKgMctJ-C3swagIXivQrufC95IKKSGIewBPMAnvrO-LQLo1rV-byJ-ROj6CqvMga1kHYgOri9tRQFOqE4SIc3Rlyz_NyTy08f7KyOo6RMtnaQdBoNM7BKIddGTNZkimAuK8Blg2iPjzwPuMTxRCcCBUHcPfZiWbtbNHZaSBbqNhNfVD443Rl9QK93-aATYWCK4l9IAoomypzstKbakkhz0R68Nj9cD6rAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهرآبادی گل اول ایران را به‌ثمر رساند
⚽️
ایران ۱ - ۰ امارات @Farsna</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/462397" target="_blank">📅 09:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462396">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfrLq_BknAADjGF0sbLv_PAgz2KR9J1tvxfEBhYKmIkrpKDE7kUUw9ZZvrzjRMajxNJq4IKf1UYJn0Boy0h-Sae153fVFHFspiInWZcpiJDZNkfFlKrvg9LEqhrG8XnBDokfK7Iv_Y7K6queIXg5DGkhuqaSKN5xiRGNjRJv7I_lTqmgmUb6w3b6RNYpiAvC5wgeydJRHT3pUTEXUD1kZsJwCKPry_Od8YHhHx5XYTLBoatlEBEQkxuWGqAUj1z0_6qoHRiT0lZ_oEf2p40yaOOqvaBQdUfAfmblR-xl24dp4jg1n05okqO1hm8meSHLVPi8pARcLXolGC-FC8XQCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسمان ایران وارد فاز تازه شد
🔹
پیش‌بینی وضعیت هوا برای امروز نشان می‌دهد ناپایداری جوی در بخش‌هایی از شمال، شمال‌شرق و جنوب‌شرق کشور ادامه دارد و این مناطق در ساعات بعدازظهر و اوایل شب شاهد رگبار و رعدوبرق‌های محلی خواهند بود.
🔹
آذربایجان‌‌شرقی، آذربایجان‌غربی، اردبیل، گیلان، مازندران، گلستان و ارتفاعات البرز در کنار بخش‌هایی از خراسان‌شمالی و خراسان‌رضوی مستعد بارش‌های پراکنده هستند.
🔹
در جنوب‌شرق نیز جنوب کرمان، شرق هرمزگان و مناطقی از سیستان‌وبلوچستان احتمال رگبار و رعدوبرق دارند.
🔹
در مقابل، مرکز، جنوب و جنوب‌غرب کشور همچنان تحت تأثیر هوای گرم و پایدار قرار دارند و بارش گسترده‌ای برای این مناطق پیش‌بینی نمی‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/462396" target="_blank">📅 09:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462395">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGaidMjhRcQHxyS6dhNBhc1YIl00Ur5Nsuhli8pBLQ7HbVBh3TAxOFFVxTSXIt9Uv0_jR4tvwX6n4rAK6Bk9P-l6KCbEHADCtnkT3JeOWejaCmIt8tBei-AiOfBo8oktkN1zDbi0L1rpzttpR9Bpk96dp0wssuabm_oB3DL7PcVSvmLkk4NMl2Q-ulpw2phZFfRHf8-8BVzdXcLroTgK_YdyFsPrcd7_-yHyaZ24ADOUyqwD218Fts_qxw7Tw5WRUXSEnw16bYODJFX1v5affXg-xsOgLOiTmTee-J5uIVgKatrYSo12axJpbrjNyKe0bf-TGyhenQDXVTY9dJlWKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/462395" target="_blank">📅 09:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462394">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🎥
پیکر شهید مولوی گرگیچ در زاهدان تشییع شد  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/462394" target="_blank">📅 09:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462393">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e0d2dd5a9.mp4?token=aqCAqyDB1Yll3-wTsKXIUUHc0fwF03o00vto7w76EsDZ9ZYLL9m_oPLQgotMbR_W1XK86TbN8rDKnift20lC54y_kXBwB3vlPcSNJrARDCzkasy-kOoeCm4YQtlKjityHUEeHUnLYIGRTwJEPDRVv8fXIPUuBIHdRj8-a2njgDSpWk74NjhNlhfY5zrqpzLFDDwmyK7Svk3s7pDB1Ngy3nrsE3L7xhK-GiDzaro15Q-3O_0pChoEIu224VS4O0aKBjEHfLF-Fmo12whM0opksJxrV5UNbVVS077JiKrOa5Qe6-_cZGYAaawu1TfTKMbis0Z-Z6ft89qyBgxtywjqUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e0d2dd5a9.mp4?token=aqCAqyDB1Yll3-wTsKXIUUHc0fwF03o00vto7w76EsDZ9ZYLL9m_oPLQgotMbR_W1XK86TbN8rDKnift20lC54y_kXBwB3vlPcSNJrARDCzkasy-kOoeCm4YQtlKjityHUEeHUnLYIGRTwJEPDRVv8fXIPUuBIHdRj8-a2njgDSpWk74NjhNlhfY5zrqpzLFDDwmyK7Svk3s7pDB1Ngy3nrsE3L7xhK-GiDzaro15Q-3O_0pChoEIu224VS4O0aKBjEHfLF-Fmo12whM0opksJxrV5UNbVVS077JiKrOa5Qe6-_cZGYAaawu1TfTKMbis0Z-Z6ft89qyBgxtywjqUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیدهای فوتبال ایران زیر باران شدید ناگویا برای بازی با امارات به ورزشگاه رسیدند  @Farsna</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/462393" target="_blank">📅 09:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462392">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c265180dd3.mp4?token=X2eLRKXkOo6aHSahn-5r4Wrx05o69VPoPpdzBSxWOzbRNLfftmxJlNFqAmt7W-vzpLPfv5g6eR_XHZ181X4El_7Z0XdxbW9WR9QsPX1aH9ON8gJD-mTEbGGWPFSCob6nTGT8JM5M70Jbftt35T44rZoVn_XoW-XlTCFN6HfQJ-ouCx9wEPxD5-7p97WbG2iUqfPMeyO7JV-6-b1z3Ul-4FoXWncTXwYucnekn0R4cvOrb155j6RTxG71CG1uGOhDhMhoiF90VTRrnzDBWYfrdCKNecRZJCfWziObz9bHXmPbn0Zt2V2YIg2dam8seFBRxqdEdJJQzzb04h7vCYxfDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c265180dd3.mp4?token=X2eLRKXkOo6aHSahn-5r4Wrx05o69VPoPpdzBSxWOzbRNLfftmxJlNFqAmt7W-vzpLPfv5g6eR_XHZ181X4El_7Z0XdxbW9WR9QsPX1aH9ON8gJD-mTEbGGWPFSCob6nTGT8JM5M70Jbftt35T44rZoVn_XoW-XlTCFN6HfQJ-ouCx9wEPxD5-7p97WbG2iUqfPMeyO7JV-6-b1z3Ul-4FoXWncTXwYucnekn0R4cvOrb155j6RTxG71CG1uGOhDhMhoiF90VTRrnzDBWYfrdCKNecRZJCfWziObz9bHXmPbn0Zt2V2YIg2dam8seFBRxqdEdJJQzzb04h7vCYxfDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی سپاه: ناو هواپیمابر آمریکا را در فاصله ۵۰۰ کیلومتری هدف قرار دادیم
🔹
سردار محبی: ما امروز مصادیق قدرت را یکی پس از دیگری به نمایش می‌گذاریم. نمونه بارز آن، جلوگیری از عبور و مرور هرگونه شناور بدون هماهنگی و نیز ممانعت از ورود جنگ‌افزارهای دشمن است.…</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/462392" target="_blank">📅 09:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462391">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVFVfH7zO0aZVyVC2Nq_Yld4-blyiTDQCDeyyCqhgwxCF0u4X9TBFyA9crDq_xSMxX7B-aRtChw9jYO2RmwnD6BFSSe113S8UWsukP2mNEKDYdcHVZjStHa2CgRghmJVM6wd2h1FkXDzxtwTXccKewXiRHN337K3R6bXjVzF8nhfKzt9EkmKMHF_YYm1R78WNy-mG_04MFOW5K0rc3eGPZ-HDbnYREHl-MZXzAWmNnYzEAfX6nli7ordRBRHj4h2mBm4msE-n3wNxQ7xSD-CekWyNH6-qyhdmU3H0kOz3m59695DaE5cPen824QJqqbncaLx90UgQkWmn8FhhBWSuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صعود تیم‌ملی بسکتبال با شکست اردن در ناگویا
🔹
تیم ملی بسکتبال ایران در سومین دیدار خود در مرحلۀ گروهی بازی‌های آسیایی ناگویا، بامداد امروز برابر اردن به میدان رفت و با نتیجۀ ۸۱ بر ۶۸ به پیروزی رسید تا راهی مرحلۀ یک‌چهارم نهایی این رقابت‌ها شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/462391" target="_blank">📅 09:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462390">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eae733e101.mp4?token=lhsrHuhFvglmkA_voHxYAisvalzdakxuZrdVi8I-vDKJz7do1CUNpC7tMbWBMj6qRHBrLe2E64Im-RzDP6m7n0vjPpFU-tulkEIKlWOmRS-Cnm6tLEQYeaRklSS-DjfsrV1D5Iknb6hKksCXVOrznq6iOz1addDSWZ_KVR4zNFzDTsVUYBjtQEVR8ZjVOWruyBGGHxzyIu7FuPl6rE2qKB9TIYVa9-2qSLIFbCpDQfKGXr-Ewx5rVoADhazDm8stlJw7LuQYNwTis00s7TJvxCpgNjDut4PiNduSyFilRGxdugC9y-461gQJmte_1z4VHLPUsgQvsF8h24zOBWB0cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eae733e101.mp4?token=lhsrHuhFvglmkA_voHxYAisvalzdakxuZrdVi8I-vDKJz7do1CUNpC7tMbWBMj6qRHBrLe2E64Im-RzDP6m7n0vjPpFU-tulkEIKlWOmRS-Cnm6tLEQYeaRklSS-DjfsrV1D5Iknb6hKksCXVOrznq6iOz1addDSWZ_KVR4zNFzDTsVUYBjtQEVR8ZjVOWruyBGGHxzyIu7FuPl6rE2qKB9TIYVa9-2qSLIFbCpDQfKGXr-Ewx5rVoADhazDm8stlJw7LuQYNwTis00s7TJvxCpgNjDut4PiNduSyFilRGxdugC9y-461gQJmte_1z4VHLPUsgQvsF8h24zOBWB0cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیکر شهید مولوی یوسف گرگیچ فردا در زاهدان تشییع میشود
🔹
پیکر مطهر شهید یوسف گرگیچ فردا صبح از میدان امام حسین تا گلزار شهدای شهرستان زاهدان بر دستان مردم شهید پرور زاهدان تشییع میشود. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/462390" target="_blank">📅 09:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462389">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jz8yul4YDtXIXvq0JnJSZglDYKn2Cj6xu-H3KCd9jTrsENwMejKV8xyz3OR3U_SWOQsmhT6xu4Vj-aJBpQs-NDApuCUlUE3sRtdBsPO-23ejxOQYn9W1TARib8KzvATZsLv1LpdKgFy3yz12oRR0mGpDnV6He5XKviwt8q7A7zoBffwDnojiq09WUiU-rq9SXvGjmFDOZvNQWubgrICuRHm8NDUxDBoy6OXZW1_BcbyBRByCUlEcNwVN4ILazGd9JBFu4qHBwUK2VZeqTFz66b5d2Ya8ZlD6YRlLeTpXK0JygAracVn33b-GIhj1O2fvl8qN09Gyivtx9wm4xjtptA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ قالیباف: پاسداری از ایران و وحدت ملت، مرز و مذهب نمی‌شناسد
🔹
رئیس مجلس در پیام تسلیت شهادت مولوی گرگیج: ترور ناجوانمردانه روحانی مجاهدی که عمر خویش را در مسیر دفاع از امنیت مردم، تقویت وحدت و همدلی مسلمانان و صیانت از عزت و تمامیت ارضی ایران اسلامی سپری…</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/462389" target="_blank">📅 09:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462388">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🖼
عضو ارشد انصارالله در واکنش به خبر سرنگونی اف-۱۵ سعودی‌ها: دیگر بدبختی‌ها به‌صورت جداگانه بر سر دشمن سعودی نازل نمی‌شوند؛ یکی پس‌از دیگری به‌سراغ او می‌آیند.  @Farsna</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/462388" target="_blank">📅 09:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462387">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4501b71d6.mp4?token=kiFtLEKZvUmppSC73QQ740kPvFkDDIJzppRE8MN7XUyn3yrB6E5BAb6VoYcpzZZjO8ow7ZjkejBNDPdPpT8uoWEgLiTW6_AS65leYnPkysuw8kdTFzPEWvrTPUAU5LcE-ZosunMas8n8KLJPdcj0W_Om4Fad39HrYmBkBnpz4oMuGZSrmEhbpVkJbsS5fbQm4mvDn2JbVIOtNxIsK5-GZleapcggl_hqutwQFpXbN9byu0d8AQwCVg84wB7A0ToTiriukKfqzGUcklTxbJmkxYJ5tF6MwcZlJJmQ6nRG4_j2kH2ZQuBf1nPFFUdU7nmF83-qk4io1E9-iPrdmxKjYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4501b71d6.mp4?token=kiFtLEKZvUmppSC73QQ740kPvFkDDIJzppRE8MN7XUyn3yrB6E5BAb6VoYcpzZZjO8ow7ZjkejBNDPdPpT8uoWEgLiTW6_AS65leYnPkysuw8kdTFzPEWvrTPUAU5LcE-ZosunMas8n8KLJPdcj0W_Om4Fad39HrYmBkBnpz4oMuGZSrmEhbpVkJbsS5fbQm4mvDn2JbVIOtNxIsK5-GZleapcggl_hqutwQFpXbN9byu0d8AQwCVg84wB7A0ToTiriukKfqzGUcklTxbJmkxYJ5tF6MwcZlJJmQ6nRG4_j2kH2ZQuBf1nPFFUdU7nmF83-qk4io1E9-iPrdmxKjYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پکن: عراقچی فردا به چین سفر می‌کند
🔹
سخنگوی وزارت خارجهٔ چین: وزیر امور خارجهٔ ایران فردا به چین سفر خواهد کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/462387" target="_blank">📅 08:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462386">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">رأی مجلس نمایندگان آمریکا به پایان جنگ علیه ایران
🔹
مجلس نمایندگان آمریکا طرحی که خواستار توقف جنگ علیه ایران بدون مجوز کنگرهٔ این کشور است را با ۲۱۴ رأی موافق در برابر ۲۰۸ رأی مخالف تصویب کرد.
🔹
در این رأی‌گیری ۴ نفر از اعضای حزب جمهوری‌خواه با دموکرات‌ها…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/462386" target="_blank">📅 08:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462385">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
سپاه: ساعت ۰۲.۲۹ بامداد امروز پنجاه‌ودومین پهپاد MQ-9 ارتش تروریستی امریکا با آتش سامانهٔ نوین پدافند پیشرفتهٔ هوافضای سپاه در آسمان جزیرهٔ قشم رهگیری و منهدم شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/462385" target="_blank">📅 08:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462384">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe6080617.mp4?token=lhRpIR2giVZdZGIZG4Hqg2cuQkKh5pswa7oGlR2ds0dNRwZtniyk98TN2gIhlzAl_Xt_TE4Hs_VN3No8T56p9MCvZewOq0OYA-SfSevfBZPn4AKp46XSp3jqyYwyitIcDyE47ULTzce02zQnLsBoh0twt_7pyFHF5B6Jp1829nB09kKRycZP_J9jZsNOQ937LkMnn-uDkZ8SiglDhqfIWYvBLd1JdtaZrgS4smtpBov-wlLEIwKbAPrn1S0BDjvEErNlWtq1ikbFNXTS3lZncPL7gTebsBvTcCjNjTlb4tN9RWqunYbRUtNPw1d9iGygI8QAOsSiFJKEoDGsqfyUPruYtvUK4yJ57iWNeBqJ61QsqbJg-uPLKos3WTSEsB_Zrw-04x9mJHlT_8BOQZ_0eiolC21cxxHJjn2riX-d6N3TY3v3Tlb7lr7UcjhPAoU7OLoFxuQT3q8XLwRBTq8ZEuq07RruU0_kXBKnQVv8xYIb6VMH1yu1A9e5xBi4RNbDl7lr4YFpgqWDpFN-iVF3-wscW6b9XzmAi-wnu3gijhwd93rop8GBltw7Qui-9DsrQLc5AWnzr8h6Vx5nILRVh_a-_-cUxQ_QNrY92oemuta6_QbCSycByKtrLoMbehAGP_l884sBG5t8MxYRoMs1vL2BZA08QYwr7nqEtQZK95Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe6080617.mp4?token=lhRpIR2giVZdZGIZG4Hqg2cuQkKh5pswa7oGlR2ds0dNRwZtniyk98TN2gIhlzAl_Xt_TE4Hs_VN3No8T56p9MCvZewOq0OYA-SfSevfBZPn4AKp46XSp3jqyYwyitIcDyE47ULTzce02zQnLsBoh0twt_7pyFHF5B6Jp1829nB09kKRycZP_J9jZsNOQ937LkMnn-uDkZ8SiglDhqfIWYvBLd1JdtaZrgS4smtpBov-wlLEIwKbAPrn1S0BDjvEErNlWtq1ikbFNXTS3lZncPL7gTebsBvTcCjNjTlb4tN9RWqunYbRUtNPw1d9iGygI8QAOsSiFJKEoDGsqfyUPruYtvUK4yJ57iWNeBqJ61QsqbJg-uPLKos3WTSEsB_Zrw-04x9mJHlT_8BOQZ_0eiolC21cxxHJjn2riX-d6N3TY3v3Tlb7lr7UcjhPAoU7OLoFxuQT3q8XLwRBTq8ZEuq07RruU0_kXBKnQVv8xYIb6VMH1yu1A9e5xBi4RNbDl7lr4YFpgqWDpFN-iVF3-wscW6b9XzmAi-wnu3gijhwd93rop8GBltw7Qui-9DsrQLc5AWnzr8h6Vx5nILRVh_a-_-cUxQ_QNrY92oemuta6_QbCSycByKtrLoMbehAGP_l884sBG5t8MxYRoMs1vL2BZA08QYwr7nqEtQZK95Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیدهای فوتبال ایران زیر باران شدید ناگویا برای بازی با امارات به ورزشگاه رسیدند
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/462384" target="_blank">📅 08:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462383">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPPEGUVFoAOv82FrjVJefDQ9SlNC_W6U3_wK3HgVqa3cFwEY-qIB3U3pkiOWu0y-YeokqXPZk6gPp9c6eGvF2TeBkOilbKdGgSFieMwplWxqMNwrZ6T3FjQw4eICpJMPfs4Yfw0d6Ef_UH2nPg2MpV6quOhuQlNOSjhAawuS6hoHRziM00CtD7wEu2YDK8S2pyMHZAQtQ17go3PrallZBcYmvKVCJ7RDFnQooXsm8A5XavH3LF9cAu-HdSQ4yeA7s6_-kE0gHMfpnaeAbdkxjXLbgNURLnKZ2ZR9S8GTAm1gs2Z-BWr1J_hsQRteucoSga_8JEQ0OV1p4KCCu67oKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش‌‌های تأییدنشده از سرنگونی اف-۱۵ در یمن
🔹
شبکۀ آی۲۴ رژیم صهیونیستی اعلام کرد که گزارش‌ها حاکی از سرنگونی یک فروند جنگندۀ اف-۱۵ عربستان توسط نیروهای یمن است.
🔸
تا این لحظه، مقامات ارتش یمن و جنبش انصارالله اظهارنظری در این‌باره نکرده‌اند. @Farsna - Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/462383" target="_blank">📅 07:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462382">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گزارش‌‌های تأییدنشده از سرنگونی اف-۱۵ در یمن
🔹
شبکۀ آی۲۴ رژیم صهیونیستی اعلام کرد که گزارش‌ها حاکی از سرنگونی یک فروند جنگندۀ اف-۱۵ عربستان توسط نیروهای یمن است.
🔸
تا این لحظه، مقامات ارتش یمن و جنبش انصارالله اظهارنظری در این‌باره نکرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/462382" target="_blank">📅 07:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462375">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XMkBCwxxEXLLdWXGcWLwMjpU66K4ueXODUDPWQsAWGTgeo2X7eZHnmDQSs7d6OMh-971XAlAce9esPMBJ316CLUE2iGS4hge0m6yfUfWww_bN8i41Fgjj_kUKmyxAIAZZsP9nTGONL2iFS_i5JJdjdOV45MxGxAvBv32PW4BT_TTDTdZ4eshUtbz4VhosKalUylr-3fDm3J2ztjh2fgUW5iFPyXw-OE3S98z5r8wTelCM880euoPwkY7eQI5RZwxMj4ql1MSD8j37VYYLTiVLQ9BC4NVLDL9h7uuhHIJCfJKuDIdu6YkVkBV5ZVv6YBdGy_GKDKx51B3oFD9MOv2_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mv2nI6Rpb4PHX88ipc9B2mN3ZQ4z2IE_u8mpwe9vrrllHgAyRMP-BhgIX3y0PUhm1zgQWRclf3Fpo0dgjYxebPqhOdGudahKwWbdGdPnfnQ0bu7Z2WJnAfihTm8IKFa_Wunnh0FoTjsb-E5ITNi4SQIIqU8bd4DCX_dyFBK2kaPOoKebcZQKu-U-ZmBvXpf4dddLaOg5WIHPeaMv16tclY2x4VNW-krlYnFXCkIWUqHzt1mopVNlAlxuSSUj-dLyHQwX_Khx79AiHOylT42c6Zzc2fhfWnzIU21FwIiRwlcpsqK-QEkIaPZTzZNMjUqPhnmyAW3nGAmzXAQUxcfPvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lhqdkKhHBYv5iRa7b3yCAqV_K45wMsM4aOyAerBgzfbrwuoU4nPXFdcS4IxntGTn5vNoMrwJMlQRULMjnlg9ndkDRxRa1MEnsViAq7ewYDVa7pz9G-CfMjdGQR1LPrSo3PSuYgHp-sQP-LiLvgXoRH8UW9o1ab8pRWL6InV87wIzlC7sliHgmDqohG8fosgC5RO02KdlK95pZDMu3VZbinvLJ3jCXCMrIp5mBiPChVki1cQYKNPx3F-CfC7_UvWdPCltsBnI4zYpcH6RoGLhZbrBPFNiqLZ7BFC0fLjm0gPkg87rk-ymGHT-j0b87Gc048OeJ6LUeDDlAbfNkDOVyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q3W-8ccVF97WAvuA0YHmrSRkSGoB2mj70EeWSx97SixVLhNjpk8-5WvgYxE2ndZ593bben2ELyZkl5Bcfqy_OPZMASr2JXrBLRbSriPxZEZxmwrV9Cg0H5S6Y5Jb9znFovORfhj7hYDibab4sfWjxU6_di05Z-ujMVNByoIR9x0Fe7Iau046oPquGgOle8XHh1PQ69ine9bf1WoOUGnvo7o_XYYQks-rPvGhWf8LwudzSR06v3GihqncZE2L9ObSjLhhxjHZmbjmF0ur0rX744oSs_qgRURI1lOQuZ7nJfzBwAD6y__JI9elZbGx1rrk6SjF_GmCoez61XsoidpN1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D_j2ScEnieYPFW_Hk3-7lJtFxx-l-LX6-LTsDZ240LR2L0ZtaWJmr2gyJ-JaCp_FvZD0nVQ_WMSgbjkE4uMp1mson2IvbiSdmQSWB-_do6DvNnaZh3R5DTP4F_L8FBsTNVPqOamPyDOxNZQMCZfuQHTBj1G5OuCDwI6KOTGk3zHYVXdiukJCOFtc0za3TCDNhdUXKZygs8PVHGKVUfK2X8N4_4q4IiVQOySI47-enBptQcQSIVIK-BVRw93ISMLqm9MK895mbknG7xAaj73SW7Mbv5lFLNgjsP0IlNJ31-t9SjsVB6u4VNWCXVCiBHgu0fJSVi771P10hH_YnBNKhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D5zmIsB5bdUbRt48KfhaLHQ_VD20o09vA6UPwbkhyGMi1eVDslJveVL83NJt42AElqPtChPUuwyv_cb72HWVQcBv0AcKao6FH_miA7rvy9FwzSqxvQ0xfYOjasE_jicAjknzh2hi21LfNalNN6jFI1Q6hDSoYXQUXjLpQnGYGs7CTvUqVkUKaH4rhkEl7Nff03Hw50fb6oQDHAK3TvUMyOxlEnQizd78AZdWFQbUWWJv45EiJJ0N8Hz4N_nGwDn2Fa0bvvGZZgHP_26n8MqPEsC-XRdHSK5cj7oxHI7Er-5JVBUxzQEJM6jnF-mQFvU3klx9TNyJSaL2_jssiX35Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HRZt0DGsCDe_jqUM1K5xQZ3y9nMsOJewlDvNm91ti0KwSObWQMh_mwg3eHx_VDaPsjrKtjNIeEZQ7U5dPbH96w9m4GTOAG_sod-sSNht2ik9zB8qjkUTk7n511YN60kln6Loh0u86R4JLdn0i4fnVOdDNJ0mSf1rwNBnTZdJeOoUiaV2fJCN3WJ1ZTehai7XdsTBYiZhXkxJo4hYm-QXzxbWoIOs91MojTsbbxuOft_EanIE-wgHsTbELtq0IQ-kwLhohVdxMt5gnX672kAtLi72AFvqfaOWiUseKZ7hgZ21iMHiQAngEEaR1N7_oB8SI48-XInBug7jIBu-6o2hvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پایان دیوارهای بلند زندان رجایی‌شهر
🔹
عملیات تخریب سراسری دیوارهای زندان سابق رجایی‌شهر آغاز شده است؛ مجموعه‌ای که پس از تعطیلی زندان، قرار است بخشی از اراضی آن برای طرح‌های شهری، فضای سبز و کاربری‌های فرهنگی و آموزشی مورد استفاده قرار گیرد.
عکس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/462375" target="_blank">📅 07:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462374">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">هوای تهران «قابل‌قبول» است
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۷۳، و در وضعیت قابل‌قبول قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/462374" target="_blank">📅 07:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462373">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0oFo-IOCKBNloMWFIgl0GKp7qqKpXiS3Fb3IiSEQvRlZRy2bHAAy2RQoh67oBOT1LYCSRI80wqQN9cmqPr_MuKJ3QOktPlRkTQ37zM_RoT55s4mNgrBPGJTfV8pYFPBJyIZphOivH9LUXxku9VMuteL_HOzlWSM36VNdg126yzfPJ2UY9CVijYCzuCnc-gdGbRl4TKfQkKeQm8fXTsSDzWx5riabXt1Odh2wW9War7OhDA_JQFFDjERdnuTpx-dkeTsIpj6zENZZnYxBLZxePvpgYG-oI1FVGMnxhrmDheLaATBqv9S43DMEGY2Y5CSsrmaRoLxjhkzKcoq2GUARg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رئیس مجمع تشخیص مصلحت نظام: ۲۰۰ روز حضور در خیابان و مجاهدت در تنگۀ هرمز، ضامن امنیت و سربلندی ایران عزیز است.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/462373" target="_blank">📅 07:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462371">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9277a1ee9.mp4?token=FQQO_uPGDCnc5MTSYo1_qEnMYCj5QPK12aQ9v7rYl3TsV5NgVGoRN-ioWXODpfS5WTaY0NTsRjywyWYrSwPJVZhNMrEFEkgeV7bSCScGgC-SU93kYfzznFlXPiTTjmDNDMnRfAYtIKISfmVwMj1dTQ1VA7vj4f0uDMqthFmiuocQRkOH3b8gaTU1vHTOIFNqqs4Bz_ZiJHuBJaH2hfQTj5En8Ub2XXdA20y6MoMdnLPQLoe04KRUFv9CsD5FnJQWUqetayfjHYvb3KmuXIfRtEKjADjZtgtDiJV1ymgxmQGMlNz5CUYcBnMhQgEynnNLwiwqu_o9hqElDEhJYDoksg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9277a1ee9.mp4?token=FQQO_uPGDCnc5MTSYo1_qEnMYCj5QPK12aQ9v7rYl3TsV5NgVGoRN-ioWXODpfS5WTaY0NTsRjywyWYrSwPJVZhNMrEFEkgeV7bSCScGgC-SU93kYfzznFlXPiTTjmDNDMnRfAYtIKISfmVwMj1dTQ1VA7vj4f0uDMqthFmiuocQRkOH3b8gaTU1vHTOIFNqqs4Bz_ZiJHuBJaH2hfQTj5En8Ub2XXdA20y6MoMdnLPQLoe04KRUFv9CsD5FnJQWUqetayfjHYvb3KmuXIfRtEKjADjZtgtDiJV1ymgxmQGMlNz5CUYcBnMhQgEynnNLwiwqu_o9hqElDEhJYDoksg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سقوط مرگبار بالگرد خبری آمریکا هنگام پوشش تصادف
🔹
در پی سقوط یک بالگرد خبری شبکه «ان‌بی‌سی لس‌آنجلس» هنگام پوشش صحنه یک تصادف مرگبار میان یک خودروی شاسی‌بلند و اتوبوس، ۳ نفر جان خود را از دست دادند و یک نفر دیگر زخمی شد.
🔹
علت سقوط این بالگرد هنوز مشخص نشده است. قرار است هیئت ملی ایمنی حمل‌ونقل آمریکا (NTSB) و اداره هوانوردی فدرال آمریکا (FAA) تحقیقات درباره علت این حادثه را بر عهده بگیرند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/462371" target="_blank">📅 07:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462370">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZdAenUKUNjIzUDgXouN_blIMzKHvnggq6qqwenN0E2dsAg9ogb41ZRS9sPv87RC9Vd8CxVTOU2F_iLcZ8X8QdcORsbwNctM-VGD6yXAxNZZvGDEH3fRv5PeN5MHq6DBNy2jVwSk0h_aaQrqYWG1mdDvZmPIzVAyAckBPYLuyEVlZE_DM4ddRDai_u9_ktBuV6CYb_HgOhvf7T6Fx2qjE-PhpZXidm9yYiJ-r81GcNDOQ6mh6bzdSnVg02BBrcl3NEyd6EkX96KSomIYQOnPIDqSNhUGPchE7DBgITLrBYtW_755clh0N0qhV6yawDZWrvOs-r2HMe-iekjxXOjhOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرعت بالای مصرف ذخایر پدافندی آمریکا به دلیل حملات ایران
🔹
وال‌استریت ژورنال به نقل از مقامات آمریکایی و منطقه‌ای نوشت: نیروهای آمریکایی حدود ۷۰ موشک رهگیر پاتریوت و بیش از ۱۲ موشک رهگیر تاد را برای مقابله با حملۀ موشکی ایران به پایگاه‌های اردن در هفتۀ گذشته که شامل حدود ۲۰ موشک بالستیک بود، شلیک کردند.
🔹
استفادۀ گسترده از رهگیرهای دفاع هوایی برای مقابله با یک حملۀ واحد، تقریباً معادل مقداری است که می‌توانست در یک هفتۀ کامل قبل از جنگ استفاده شود.
🔸
پیش از این، شبکۀ سی‌ان‌ان به نقل از مقام‌های آمریکایی گزارش داده بود که حملات ایران به پایگاه‌های آمریکا در منطقه، باعث خالی‌شدن ۸۰ درصد ذخایر رهگیر سامانه‌های پدافندی «تاد» شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/462370" target="_blank">📅 07:00 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462369">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRS-StmFjv7hEhMUMrNFS11NLfbRTWnj7vtRhV_v8xGg74NC2vOyze77fQMY7q-4X7m3Qefm337zeX-Lk03M7G_WBZ-zACBePCGhjSFK9vl00vuylgOKobUjP7ThcoEw7tDFP-kCfCbUa6X78qdIojnvuW0c1oUT2aEjy82YG1YLxhob-RQ3yJBNxNqgC1WQgv1If5nOOgGP1Nux5YSfAQVCogm2F3NA21MyTEv7PHG8DDU7Ks4m-fMukqJMJ4-LIGICu87MGY7xF9IthYmARC4MUzHnabFvDuhXJ6r6e5qn37wUz5EALfbTzd8L97_la7aSKGn_zkzX7ODW0gFhAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کالابرگ سرپرستان خانوار دارای رقم انتهایی کدملی ۳، ۴، ۵ و ۶ شارژ شد، و تا پایان مهر قابل استفاده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/462369" target="_blank">📅 06:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462368">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXR68lkpaAGXhWkvO6UsclHklsYm-o7W16EZLJr_Qdi6mtuXbp8pamDwKlyjJ4DYfYQGpUVBjvxx44rY5pECr0D2zFsYmE0wyJ0cwdIE6K2Bm3JRDTWRQUaGnAUB5gqbGtsd9XY7pu6Z1r_E88ThDnih_lSuiPbDnK-J9Ra9_KnXPksECebhN2v56p5p4xlnD8Scb9_24pbuITThp5_FUqZbDqDl-OYy2oNYlJCtguMCll5DsJB5yOGQLzNi0ReVqrkkxRSv83PzoY8aZcmcVJlyMli8GRsO2kRAU1PvCg77Y2ZggKPQ_vPXhIKxxMcqP6DSQBNwg27fOC28VAtCtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ونس، معاون ترامپ: بحران انرژی جهانی تا زمانی که ایرانی‌ها به شلیک به کشتی‌ها ادامه دهند، وجود خواهد داشت. @Farsna - Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/462368" target="_blank">📅 06:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462367">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6uER2Jq9sQ6zm9NWDsyIZqrn5UI31g9gZ3SMbFauXEoahFkSg2NimNawWDRkx3HWIce4rbk-fYl94ozv3TgyCCF-M5XBoPfAUVHSsl2OWC6eizd3nwCHgsFJqBx2CXossO4qytQNb2kLVs1kHEILFdFz9HB4HuOA-DLj8R52W2yWbqDkFns-0Ya-PB_8pWjMD_2jHyFhWWDNcttbqdqWT35eqJAEbUIEYWBWm-DkCUJaVEfGHlgyCiyujFgcCdQxgLnEiUGOcNwxCGCOZ5jibjVDs5IVpgNHPClsdD-3Reb9H5M5ehkFyj8WmKz9gW8uyKLRT3usZIzLoNl8BPYgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ونس، معاون ترامپ: بحران انرژی جهانی تا زمانی که ایرانی‌ها به شلیک به کشتی‌ها ادامه دهند، وجود خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/462367" target="_blank">📅 05:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462366">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">هوش مصنوعی برای اولین‌بار دست به نفوذ زد
🔹
برای نخستین‌بار، یک نهاد ناظر اروپایی از نفوذ واقعی یک عامل هوش مصنوعی به یک سامانه و دسترسی آن به داده‌های شخصی خبر داده است.
🔹
آژانس حفاظت از داده‌های اسپانیا اعلام کرد عامل هوش مصنوعی با استفاده از یک مدل زبانی بزرگ، پس از ورود به سامانۀ هدف به‌صورت خودکار به جست‌وجوی ضعف‌های نرم‌افزاری پرداخته و پس از شناسایی یک آسیب‌پذیری، توانسته اطلاعات شخصی را تغییر دهد و سوابق مربوط به صورت‌حساب‌ها را مشاهده کند.
🔹
این پرونده همچنان در دست بررسی است و جزئیات بیشتری دربارۀ سازمان قربانی یا مدل مورد استفاده اعلام نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/462366" target="_blank">📅 05:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462365">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4149d238d.mp4?token=VnIP7fXTQySqT17HKpV2-6WZ8BsULEudy42BEIEdDUJl06FQhGAAV64C0pWyH4Nm6rP7V2Iq0sM8x_ekp6-CRKaPrvSzijKVHf0JOC-ydb5cqu9WZ_XmbTy5kkPJSadhzFlKsyDD9SsCjzleXZ3OVSxMR3nv57wbye3kam4jAMYtUe61bYpovrQe7ghfEqb-OAqZpFFt_fR-IRWCCnhGDVa0x4uVOoF22WQZ08IjCwU0gpb7ir4qFHOxRYH9SG6H8FfolmsO9Q9Zb493jP4QsTY8Tnz9JGECVui-qbS2NujF1r5Yc6VnkAT4PhEE1GPO-JtIFAQ_kB3i6NurIL02sDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4149d238d.mp4?token=VnIP7fXTQySqT17HKpV2-6WZ8BsULEudy42BEIEdDUJl06FQhGAAV64C0pWyH4Nm6rP7V2Iq0sM8x_ekp6-CRKaPrvSzijKVHf0JOC-ydb5cqu9WZ_XmbTy5kkPJSadhzFlKsyDD9SsCjzleXZ3OVSxMR3nv57wbye3kam4jAMYtUe61bYpovrQe7ghfEqb-OAqZpFFt_fR-IRWCCnhGDVa0x4uVOoF22WQZ08IjCwU0gpb7ir4qFHOxRYH9SG6H8FfolmsO9Q9Zb493jP4QsTY8Tnz9JGECVui-qbS2NujF1r5Yc6VnkAT4PhEE1GPO-JtIFAQ_kB3i6NurIL02sDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اگر قدر هم را ندانیم ذلیل می‌شویم
🎙
رهبر شهید
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/462365" target="_blank">📅 04:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462364">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ok-L1vtsy_aqAs1mk2thxjC2pivrhGKsFqG5H93pDwH7mqekS6PUFY2rqF2aRoCWwU8Bg9d-zEOyiE-d784WjKRx_96uPdulziG-aBFhT84BcSykmnClYCTHyw4AWS0ykRH_-ykDCLLUd4Bx99sdPNqGFiKl4EM1kfEz6KckMM4NmO2Hm5RM5JthGCc7KXzqxIqqz7mbHaKqEsACkwd0zJ9J7aTOL6luqQArrt4QLWEWadScBUXGYsbE9fNGEZA_NJJ_Jo629JvQYD4XT3mDQSEBZ-lpznFEtXXnKIsKOgvcjQShb9iFs_3MK8DXbXwC9CxRZmXVTOI-6bVB1haFxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۶۰ درصدی ثروت ترامپ بعد از بازگشت به کاخ سفید
🔹
نشریۀ فوربس: ثروت ترامپ از ابتدای دورۀ دوم ریاست‌جمهوری در آمریکا، به میزان ۲.۷ میلیارد دلار افزایش یافته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/462364" target="_blank">📅 04:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462363">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">آمریکا به‌دنبال اعمال تحریم‌های جدید بر روسیه و ایران
🔹
مجلس نمایندگان آمریکا قطعنامه‌ای را تصویب کرد که راه را برای رای‌گیری بعدی دربارۀ لایحۀ تحریم‌های جدید علیه روسیه و ایران هموار می‌کند.
🔹
در ماه آگوست بود که مجلس سنای آمریکا با اکثریت قاطع، لایحه‌ای را درمورد تحریم‌های جدید علیه روسیه و ایران تصویب کرد که توسط «لیندسی گراهام» تهیه شده بود.
🔹
طبق این گزارش، این طرح خواستار اعمال تعرفۀ ۱۰۰ درصدی بر پنج خریدار بزرگ محصولات انرژی روسیه و ایران، و تعرفۀ ۵۰۰ درصدی بر تمام واردات روسیه به آمریکا است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/462363" target="_blank">📅 03:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462357">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D0bDlpwiQKuTN-sihB_i1tsR-RYPU9OGXa-mBpCnXyKTeWB6qrv0e5isYzCHIXG1p2G_pTmT_Lg9bao5dEvXOtcMO7esBlI3N7cYuD__m-nb5KBgQrn0XeIsf-7HN1gicU-yEik_FA2-qzcgjtvMbNr6j1qBQMAL0rTzRx69makk8wuPxULIDikdpLeMuFZQwtYqmc7eY6NmKp_fyQvyYVaQRI7V1bsQyj_efTCInEIUrreocJPIcyIHn5qqljzaGEIww85q9jAGxvtnypVcJ5dHha0HIK1R8uJBN4vQBAkpCpWNeh-fpxrtb9TpN3cxjx0Hs_oLiqa1azlNxILsAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fbrAnDtxEGuqhezARsgPLKUbN34nezBmPrBg9UwRXiUF8JcJ8b77cwtsdZISvgQIArdSqzHyJpvgH845Gv6hgdkZMsk0jguICIDsJ9HQsG-NEc87Eo046qe8U2-qWKqXtipQ6Zo2o0A12-2MOGanYqedNESkT8SUTHbOw3fv7DjJ24RCCnJMBhdBQ5dtY3quIXDUXFYiZwHJlDNAWqbDTPrnONWqnDpQ6rLH0EM7RuTMPU1vWggUxKwXJoov0cdRd0zv1nVeezYqxdtCTDb7RSdORakp03DbE_G3mrjWXaD6Rlx7Us_FbLAzE5QHs_EWu8PJ42VnR0D_d8k8GcyInQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XugT6hWIRF2BS7KMn5TkYC_WbGyCgkoOlpcDcWPO13IX06cUnJdTToYukB0HHn2pTVJm1jfBPdsjTHw3ShRFHdnOM54K2gyQXKmtRISDXpsoyVUogmq1LpoOfQB9IOBW8eP198gk9hUbISsEPeNCGmptUrdyQRj0X5F8dpT3eXTDUEtVgjZc1Y5dxGLLvYrYraUwIE_EJQrWrU9zKOB16gnoMt2jATFAZoCD43rgriL4jwa4IMxy2p9imPrd7UD4PhexPzs6BgLhZ4O5d-xt52QA0jdUdylczMv3QEHbfJHTQNDTfYMboED68EvTOW9kYz6ytEiOm7g25CwEBkBzEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZfAtA8zdCHkHx85GC2Kol03E05yA2cHHDvThkhBz9TZthpXak24aj-hTvcD4MENh8AG6eAon-AXAGaM5N-MgMF45Yw-ImLs39uMg97LQVHHQ7k1yCGxOMpDt9u-VAOaFQjG0n_vwbO0qbJ7klH_xubw5uIRjxmtSGg4pUtGgFzU7L9ESyCyVOJ3wS-6kUIdRRK-kanJRMhSlksGHUfTgh8iZnZDI_VQWRuiWv60aDMFKcc-LkHs3bgOe2aEeArZfk_ECeL4MknMHwNbIqSwBTfSYS0Qkvtn56OdVE96JLZhTAvE9TXbLGp8v5A6pjBuYjl7Zx5kUWEE6mNpv4JCweA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LRNkR5kz6VGENYQOHx4U7lQUCx4KlWmBEY0R7yTcaR3_7K6Re62KixraQlqmjzn1WEB08dZTv_35NfBQV0d3HVrDrHwBunITHnAmteHkmPY7xvD-fN_Vomw4hZ-CRHMzFO26QlX8ayYRNuNkwpf5z9mUG7LaYEOzvuo1ICFbllQK6gs7qy1J6NYFgm8_KwARvuBA2Wx-u_wsVObEZCXI_9Zo-CpLTiBVJc6hB8AjeG__Xf6q0lXyBgOvouHfh0i2pQVvR5jMipH8kLelwDHRCbhu8pWPHpjqix_XOpOZy50pEKmjdyr-jjBRPjNjEeM4m-5bbarkqE3MkNmuKrZCRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شب دویستم؛ روایت مردمی که حتی در روزهای سخت، میدانِ خیابان را خالی نکردند
🔹
۲۰۰ شب، روایت تداوم یک حضور است. از روزهای نخست جنگ تا امروز؛ خیابان‌های بسیاری از شهرهای ایران در ساعات شب شاهد مردمی بوده‌اند که با وجود فشارهای ناشی از جنگ و دشواری‌های زندگی، صحنه را ترک نکرده‌اند.
🔹
جواد بخشی‌الموتی استاد دانشگاه در گفت‌وگو با فارس می‌گوید: ما شاهد یک پدیدۀ تاریخی نه تنها در تاریخ ایران بلکه در تاریخ جهان هستیم. هیچگاه در تمامی بخش‌های یک واحد سیاسی، حضور هماهنگ، مستمر و هدفمند با این مختصات را شاهد نبوده‌ایم.
🔹
این حضور مانند یک معجزه، ایران را از نقشۀ وحشتناکی که برای آن طراحی شده بود، نجات داد. نخستین مولفۀ قدرت ایران در این بازه زمانی حساس، مردم بودند که تا پای جان به میدان آمدند.
🔹
اعلام آمادگی و ثبت‌نام ده‌ها میلیونی برای مبارزه و ایستادگی پای ایران و ۲۰۰ شبانه‌روز حضور در میدان تمامی معادلات را تغییر داد و شرایط فقدان رهبری در یک بازۀ کوتاه که مورد طمع متجاوز بود را به حاشیه برد.
🔹
سید محمد مهدوی استاد دانشگاه نیز می‌گوید: این ۲۰۰ شب صرفاً به‌عنوان شمارش شب‌هایی که مردم به خیابان آمده‌اند نیست، بلکه روایتی است از استمرار. روایتی که نشان می‌دهد جامعه تصمیم گرفته حضور خود را حفظ کند و پیام خود به دشمن را از طریق ماندن در صحنه منتقل کند.
🔸
حالا ۲۰۰ شب از اولین شب تجمعات مردم گذشته است؛ قصه این شب‌ها بیش از هر چیز دربارۀ مردمی است که می‌گویند در روزهای سخت، قرار نیست خیابان را خالی کنند، این شب‌ها در خیابان های شهر با هر کدام از این مردم که صحبت می‌کردیم می‌گفتند تا زمانی که لازم باشد و رهبرمان دستور دهند، پای کار خیابان خواهیم بود.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/462357" target="_blank">📅 03:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462356">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7VRO2ILpFhhfFeLN-Wk82pW4mWXiEAYNXOA5D6IqB7swx7oOQYCEiYTwLKUqInMsXBD0Hdhv-LhA82v97-_lAY2-kw24XoH2hB0Robzn1B-ul6ISq3AnJZXMhbquxwuAwAiEwgMmL9fAzxv2CQyvJkuD_6HWsyTc8PbrHKN0NWvBL192g7Un3Jyti9SKaWvAyK3ZoAu8ZTYxyZOt3QkGUYpDCI-xQVgZq8RIdp_uL5uXt6GLqC-Pgmxm-VdWrDSCx617hcf2d3s8SqO1YE7U7qQXWQiq-llU5A7ilW38ne3rrCpp8ImhxmzGdHYpExWAgR4pmDNrptOVEq-auUS5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائب: باید با زبان هنر، مظلومیت مردم ایران و جبهۀ مقاومت را به رخ جهان کشید
🔹
رئیس سازمان بسیج: جامعۀ ایران اسلامی تجربه‌ای عینی از مقاومت و ایستادگی را پشت سر گذاشته است و این تجربه باید به آثار هنری تبدیل شود تا بتواند با مخاطبان منطقه و جهان ارتباط برقرار کند.
🔹
هنرمندان برای رسیدن به سطح حرفه‌ای، به آموزش، فرصت تولید و پشتیبانی اقتصادی نیاز دارند. در همین چارچوب، اقتصاد هنر باید به‌عنوان بخشی جدایی‌ناپذیر از سیاست‌گذاری فرهنگی مورد توجه قرار گیرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/462356" target="_blank">📅 02:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462350">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ebzNuHohtCB6WhorVFnhEz9xGgFzKOcNAKLH9LHqdrXJO8DutkQk5ZPRMkcYNLO7PgjvSfRak70LP-HmH6VFZgpgn3Nw_NkpdfIjnghtASzFfJrnCCUWBonezNnCxP6ULlXyN1DD0EvZp15iRPdsdENOsFIZRNu3choLWy8VXBUjQY0Zrea5J6AQyOzJ_RbIgmNJF9O9aW62xyNZEJhHbvouX09LKaUKefuAFVBSgmlbpKLDNVXoAit6vP-aWlRkuyly0I3okafoIbrbnSMkhkZUtclLehyHh__VqPyGkTKcK8tjavOvOQJHA-lPlshVVgdYXs9umpJ9i_sPGintkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D9psNJICoD7S74sPWhsVfI2rIkITgl_Chj6moL8b3Pejt8U1XbPc4Ob9BEuLR0bN5xUFI7NYSQ9E6_7RshlECbbRZYAbQealqN3XyKMm7zKtUrpqVevehev6XZQLCbixEkCNTLMMJE-zQmATXch0Qk9feyeoY53ROkHqP7a84a50_wT7ig6TsQ2DjwiUuo5GsEFgc6d-mDi60HGHtwUOqFuHQxU7Vh-wKsG4xMm_oJ5jrjJdvQG_TTGO02sDc9-JCYGEbBwKLP696EQHOqQAToLNP-hxZz7t5QDCMPgDykl7ikOdey6WohrZBge9ju8qYIu9NYWQXM4UHmKYXiOKfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KRgiTOx5MWp80r4jULhqFNf1yrRXgN6M3xtKovgocte02DvyKMukUG9mceD5D0ZKSn9wy_vM84kNY9YGFoXW23t5MbcyQomSDa5BQ5cyAtczqlGga6S3biqRK7zWzFXwN0_nTbLKdwKrhjRUZuHWvDOiXCCBcdgN4WO5Z8tFm4WZ6VPxDQYUxlLU32pmSJG3Nq3Eh6mIhfW_4Es4yJzu03P8lXjBlyF6PqJL8uzPJy4LX9tbPTxOE8HtRUuoq6VFpOfHDF720_mig-0MZ6DmzPovTYzQLBWnHGyOs6IcfWOpGUVBg7n2pgbd7uXLUSrh1QdPFthEwTGY9xSMfAKYQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l39KqBGmr75iJtIwTTzTcl2EXpnqLI5k0H5fvw_pZcRsgMrExQV1b4BLdcPSG8fslCHnNhm9qefM_v8UB1vhkz9UD9UvNkdXfUeNqttcadLmaYF40LstJ0v5Q9eTAiXLbJq8aRtRMJOSseP3MsjObT6Ky9BtJVIysMYRN6EhyBtJET5UVwQ4T4Tj6XXy9eKhHjYrNrLBk0wY9TfHGjKAdK4HPVFuldYbKsOVmVWWbwoGjcd15z4wLUVpBfUCAuVgIwSXQmFtXWkliKmlZ3Lmm4qOpdJEFsgE87rGqQtpA8YVWVAdjf_425Lz7-pINSGjdDqQd4FYTBNrdDQWjtV79Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/slXKXVCycxdad3MborYQZZPLV4_p3QcBppnUekzl4cemNUmIql7076-RE6ve3x_CN4QNovctyksglmd3i_0Gc3rvruOZkRqhE5YDqCfk3nlJcG0CM3mcrx4LVz6LFmOi-_Sx8nZPlAHCKzlXIx1I-lfcj_0Yn9H4htbmeBynaJgrLnQ0IcSLAdR8W0e651gC20PuTZ-ripD6AvFoKzvpY0zYvrgzyYne3jlrgsJjCKV4Iw31ADHe5sPBnLMXgh-5QQ9DZV0B_UdXnNQs-iUoHt1O5Dl-iUsHQLT2yYg19TCKiz-y5PIafmh-MYxXC27tu92mYZpq4wQyTQggmYZstA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AbvHrhVwH3hlxO3tKsNhMPbvJQ565Y1Hr9wkKsSI0KDyBaBLbYItZo87MGcuXVwnTghnT7dQ7z8al0m-WfEzTDyAHXMEVkNVP0GitaLOZl1V0yWDCPrR3AvbCqnKc7r9YuvckrCS39cPQSmaChV5U06yBkNQrN6RI4hioVabGZQhHlg9nmzjY_7YJC1A61M4vCiyPi1Ntvfu2lIK0F1m643LQvDd8tH7kis50uNvyyyVReTAomL4niaGMntdDwmkijENGPz4IhOZmUsngM7IGkBONGKznANC80jr1YUcMHK0gkgSkbThSv2-g-QB8qw649I_x7RnBxsG8znWdnpwoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر اختصاصی رسانۀ آمریکایی از آسیب ایران به پایگاه‌های آمریکا
🔹
شبکۀ سی‌بی‌اس تصاویری اختصاصی از میزان خسارات گستردۀ وارد شده به پایگاه‌های آمریکا در غرب آسیا در حملات ایران منتشر کرد.
🔹
این تصاویر که توسط اعضای فعال و ناشناس ارتش آمریکا برای سی‌بی‌اس ارسال شده‌اند، ساختمان‌ها، وسایل نقلیه و تجهیزات تخریب‌شده در پایگاه‌های این کشور در عربستان سعودی و کویت را نشان می‌دهند.
🔗
شرح کامل گزارش را
اینجا
بخوانید و ببینید.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/462350" target="_blank">📅 02:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462349">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">انفجار در مقر گروهک‌های تجزیه‌طلب در منطقۀ کردستان عراق
🔹
منابع عراقی: مقر گروهک‌های تروریستی تجزیه‌طلب ضدایرانی در منطقۀ سوران استان اربیل عراق هدف قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/462349" target="_blank">📅 01:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462348">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwKxgc3iimL4YxpUhSMdQINgD1k6tEhoyUoLYV2IFLFKlg7CZ_Vj1sRiXYBLKn1RXCVecVh49LbxBZ42o3pHmyak4BLF6vGVJitI8-DW23m0gfuuq1uaxCk3dpTEj9mNsxUcVeDDCvOPYhydxRlDOcVgDNfwHViMrrGTIcTESh2wlBnhmEQe57fB8uE4spy3PQUVF09yti72vVZzM82T5GwG-cfnKnYv-lwhrzbGlAyykfXTcX0p8SlchI2_N_YM7kYAYnZJIrF4qnFydHfS4i0DIG4Y7tmR5lRQuHatt3S4DRGy_u4NzIgGkmsf2A1sUremR15m_49gG6EprnqnjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جابه‌جایی موقت المان «مشت گره‌کرده» میدان انقلاب برای مقاوم‌سازی
🔹
سازۀ «مشت گره‌کرده» که در آستانۀ مراسم تشییع رهبر شهید انقلاب به‌صورت موقت در میدان انقلاب اسلامی تهران نصب شده بود، برای انجام اصلاحات و بهسازی جمع‌آوری شد.
🔹
این سازه پس از تعمیرات، بار دیگر در میدان انقلاب نصب می‌شود.
🔸
به گفتۀ مدیران شهری، این تصمیم با هدف حفظ این سازه به‌عنوان یکی از نمادهای شهری شکل‌گرفته در جریان مراسم تشییع، و پاسخ به مطالبۀ شهروندان برای تداوم حضور آن در میدان انقلاب گرفته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/462348" target="_blank">📅 01:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462347">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/462347" target="_blank">📅 01:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462346">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b596013a4.mp4?token=ZFD1tgdf66_3C4wOiKjWYjlRGyrmjEbOl_0TIOUC14IdIamLkANQQWLDigC4eIuxmhEB1_E2jEHfXYtTkGJ1oDr1tISLeV2I_yS4lwyUnR87Yv-_0t8zG-bnV2HOyuXSjkiE5hwBWt3gzoyh8mHnjhu9mbAlRLHOoYylAbIgOpfHSwOcLo7-qTLxuQytdiYgHPEXUijJJBGsqL4IwCx_kbluZbyyC9aBrxqigcB8M9oEAgGw_wOCko5TLDrRqJned5eQLkRdcWNXeqO6W-Fd3jCUnpsgzz2Vpy9x3T_fZOF7gDB9a3nTI5ZlbKYqgwvppe7_Q4LiPWF1qeEl0ogzgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b596013a4.mp4?token=ZFD1tgdf66_3C4wOiKjWYjlRGyrmjEbOl_0TIOUC14IdIamLkANQQWLDigC4eIuxmhEB1_E2jEHfXYtTkGJ1oDr1tISLeV2I_yS4lwyUnR87Yv-_0t8zG-bnV2HOyuXSjkiE5hwBWt3gzoyh8mHnjhu9mbAlRLHOoYylAbIgOpfHSwOcLo7-qTLxuQytdiYgHPEXUijJJBGsqL4IwCx_kbluZbyyC9aBrxqigcB8M9oEAgGw_wOCko5TLDrRqJned5eQLkRdcWNXeqO6W-Fd3jCUnpsgzz2Vpy9x3T_fZOF7gDB9a3nTI5ZlbKYqgwvppe7_Q4LiPWF1qeEl0ogzgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایندگان آمریکا برای سومین‌بار با طرح استیضاح ترامپ مخالفت کردند
🔹
اعضای مجلس نمایندگان آمریکا در رأی‌گیری بامداد چهارشنبه، با آغاز بررسی طرح استیضاح رئیس‌جمهور آمریکا مخالفت کردند.
🔹
این سومین طرح دموکرات‌ها برای استیضاح ترامپ طی دو سال اخیر است که ناکام می‌ماند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/462346" target="_blank">📅 01:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462340">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qx2mAXf0vv0xTI_inv9Gywas_Pk19xHvpTqOsH4edB0_WZoW0dYLHOkzPl4sB5T1eZS5zyczfa6ukiFHn3wndfXVb7dYBHNm0apmNquMXlS1VnHUdtJbdm8S377p1xQNU_NMbB7BrFJ4SgrfXffUbjHrl9tNHrwxG0snoi8hjRFCWvltnXQNHrwo-r4H4N1WMgvRq4x4giwqWXgZCuwMW9aZKTtLlznb4ZE5iXPXju2Y0bxU-4Iqi8zvMbUgHvW-4pafb9LqquPD3kUqoy8vNP6T0vRRFejP-eF-3CWRoBa8B6wUqZtyTCI-mhdEcm0nG0YEhxiI0vh3-NEKREUH3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hsjAWUX6LYUPIPSLt31CN7CY26VpdZVaSlu5iDWLi9zstqLLlH41423I9peKrRJMCFjOOkcr6g0Ew4wheVmUbUqP4zgna9TsZchnKRmTlgC4UCdFOCIRYOPHCceoaiQZAbmUmfFNbAwb7_ePyw5AziGZHp_ORXJt0vsuJSQvOkJZtZ-0dnStfbfk1r5hb_yuB2F2LYKo3t65xElT42Ty4yidil-qwXg1KW0KcIcCUnhTnzZ6Ntp8xpStcEHVxiTS3SSu1JOx9DqCwv8T6nh73I4q5_DNufBTtqYssogmOlUS7JLTCeC5Mb3MSQPzV23jkLZahgq7df3EwUmE-cs47w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lZsAf6e-C0lnR9neTKzmh8pqSWx824WDxrf5B0oRcEwZ8Wz4qZvzxcJRtj5NzpGaDFIYKZqrCyIQoSTG67FYye4sAeomQKVkFVFFNkf-cfrQi-Nx-mQfv6rOJ0PfQdwggNtq8r-DKPG13tdA3m4cpp59q4vL48QxDCV3IxM2ytdTGQV5TX0jmotBF7JSwnTEdoGvi3BI5CksQiRVoogr_FyNofANYQ3WMr8KPXIWP1raTL8FL9br8HV2ersF1i6Jnr48BO5C1vkFoN7E0UmjphRjx7absBVz_gz8qm9y3Xa4u8PMmAwnsbIp9wjGvISuFs_1_uHWKXk5mGGGuSwTEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hVRVsJRpRiIbnITggMNbvy4azNB-nsk1-Db-d94KZh4Cp5hHKG8UN_TZ02w0C58m-vms1dLQHZL--MfiweSf0WaN-Si7oYiTQgixZZvQ-k9CrGK2mGm9m70_VcWDQjCuECmdu8M8TWzPFsQtyYXn1vDhIGrEHNzP_OlStIBXciMTK1hB2c_WS4LFA-b-POK7f3twlXIJa17qbcdGt943YZ0-lFl-C_6sbFvN1Yz8aSGNcMdhHlSAwPo-MGw7LASXPGYmuMLWLGXogCGV5zOrUV2NjLQzYxmYH8nA2toAD_xvrcqeSX-A7LNCj1N-R465hFIcM4f2clv-FELEz9kfoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GddshuTUlLTwk9h82VgS_xfFSFuH0eaOx5AfvXuOvXDyipknqU7LMYUFxgHYC0gl0sdPiZ5_gb1HNoup8Sy1nE9jVMHEsLMp9332cO5kLjGDkee8_l6MaJibwrNf3BPwW-Fr1jhcO3bNIo2VEQj0naJdGeah-IzbRaShT3Se_3m8rMLnrzdyrsaG_rJFTSTOeqLgNRhEgR-yLJUa_s6nFiMeHKfMuzoAfEpLS_7l-boq4LbYHAWMD4RQ9lGaODNnzpM_CozDq6T4EkwbUi4VsYDTdwefM7HaOWMQYUbPdM1-gbiXkEOnVShp6F4W24TQSqTxr2zlNBOQxMH37q64aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cp_2uwn0vgOvKTfWtkg6oMfUd1FP35t20Sknkja_DcCUuYmS7Y2jWu0eYa7TLuZlJQLZMjutW2mrFByoXmexjK0BybhkvC18Rc5ofp73_9WuDdjtEvyVJBfkVp57fzH307fMIzIAYG0N6i31XFrEiUEfd9vyc47Nnd9Ud8q1-E3OeTP1x2Haj0FXl7tyzYP0PRtI1uhb58kUWVGSFKD89w1lE5vE8GWsmNwqNI3yITGBZwq0vvWwwJf4Zzn3EbxljSIxaBKQc44z7UV08OAPM3_V5Ad6_PkQ4QseIclBatu3a4fYm0Y4F9enG9s04RqYUdd9gUeZVNTy5O-83GQ2Pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشن ازدواج ۱۱۰ زوج تهرانی
🔸
جشن ازدواج ۱۱۰ زوج جوان تهرانی  همزمان با شب ولادت حضرت عبدالعظیم حسنی علیه‌السلام در برج میلاد تهران برگزار شد.
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/462340" target="_blank">📅 00:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462339">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آخرین وضعیت تردد در مرزهای ایران و عراق
🔹
تردد زائران و مسافران از مرز خسروی بدون مشکل ادامه دارد، اما در بخش تجاری، حرکت کامیون‌ها و تریلی‌های صادراتی با کندی انجام می‌شود؛ طبق بررسی‌ها افزایش بازرسی عراق، از عوامل کندی تردد کامیون‌ها است.
🔹
در دیگر مرزهای ایران و عراق نیز روند ازسرگیری فعالیت‌های تجاری در حال انجام است.
🔹
رئیس اتاق بازرگانی اهواز گفت فعالیت تجاری مرز شلمچه نیز از سر گرفته شده، و بخش تجاری مرز چذابه هم از صبح پنجشنبه ۲۶ شهریورماه فعالیت خود را آغاز خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/462339" target="_blank">📅 00:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462338">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">منابع عراقی از وقوع انفجارهایی در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/462338" target="_blank">📅 00:16 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462337">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AE40mv-vEGEiuQuMDyU_4Hw9_iOyHphVS66Ysl8A-Z5pV7DXCP7v_MXJtr-9Wa8XMNDWYtaiXpOZUVSeHDZZhSBX2XQRkuYQ4CPl681Sl4GasUtyUkTGy7SKdjKNLB-kBtxouF_6DkyI8TwIV6KOe2fg-NF0K4irbR-EPz9zBKDfi4iWsohoS0YBptxAzlBRSvW1B2AfQZGW1SMvs_JFB6oAXil91ukORLdu_YwdHznBCuf0pKRNez6oifxWoNpmkg9QN-OThJvgcOaCK4RRNhAX1p9YK1GZr6SgbHOK-BGPl2cvWFp0R2ibfvMzFWoHzuWrAe5C9gkIK5sBUj0raA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترور یکی از فرماندهان گردان‌های القسام
🔹
حماس در بیانیه‌ای شهادت نائل ابوعبید، فرماندۀ تیپ رفح را طی عملیات ترور رژیم صهیونیستی اعلام کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/462337" target="_blank">📅 00:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462336">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff12330ede.mp4?token=J3ntQAGGKqsL3ThFnM-BWRhRs0iP6sr5DXVP-eGvk3b8WWvLmbczXmfP5bmooGimQkmBNe3DBm_UVirKHATpvVqSWlgND2tHa-cteWMn8utPYfuEpX1EAqVJ0WFcIIbreORvZ-a_QoC5RvoMAlpo1aWZb91MgzNH1lwFaQnk9jie2FoHkUC_vc5vZ0xhRAfFUMYouxhE0evSFrumotHg7hIAd5oexlziOgjwmt_9t9rAhvfFt2xjYH76zx4T99KCKAiR1Z7UsF_v5ItDAANeUHZchlgwg5SOPVpdYdmlvwJmQecO0si9zS2hfHbWYRdKC1xHWgWU8lJizQlkJ69ZlbTkBSW26xAqb9uolLTXaPnWq-e_vpR-omGTzLLQB0cqodh63tzMOe7BT_7JIodd978eC9ajjxbPSmbPhNJ53wL8T1v763I6S-mAlkTvGpTfp11Uflc-VP0eJ-FRyr9hDu3QRjmjpRKRP8C4Ab92UAUEq5dV0lBtlKCmKJ38NVx1wOGgrtyFlhHVHiwc05V-GQtvWtt-GGRY8F3BKT59GXpHYyWHJH_2rodngUQ2IkfLSU7hfn7F4y3tGE4Kfg8P-RnKSDi0QhqX3ITXxuYNwlFpCDD2Km5VA6JqBiHA5s1CeB7rjjoNONjzFjiToRpdO5TWHhu7DdImWILOqscaQ8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff12330ede.mp4?token=J3ntQAGGKqsL3ThFnM-BWRhRs0iP6sr5DXVP-eGvk3b8WWvLmbczXmfP5bmooGimQkmBNe3DBm_UVirKHATpvVqSWlgND2tHa-cteWMn8utPYfuEpX1EAqVJ0WFcIIbreORvZ-a_QoC5RvoMAlpo1aWZb91MgzNH1lwFaQnk9jie2FoHkUC_vc5vZ0xhRAfFUMYouxhE0evSFrumotHg7hIAd5oexlziOgjwmt_9t9rAhvfFt2xjYH76zx4T99KCKAiR1Z7UsF_v5ItDAANeUHZchlgwg5SOPVpdYdmlvwJmQecO0si9zS2hfHbWYRdKC1xHWgWU8lJizQlkJ69ZlbTkBSW26xAqb9uolLTXaPnWq-e_vpR-omGTzLLQB0cqodh63tzMOe7BT_7JIodd978eC9ajjxbPSmbPhNJ53wL8T1v763I6S-mAlkTvGpTfp11Uflc-VP0eJ-FRyr9hDu3QRjmjpRKRP8C4Ab92UAUEq5dV0lBtlKCmKJ38NVx1wOGgrtyFlhHVHiwc05V-GQtvWtt-GGRY8F3BKT59GXpHYyWHJH_2rodngUQ2IkfLSU7hfn7F4y3tGE4Kfg8P-RnKSDi0QhqX3ITXxuYNwlFpCDD2Km5VA6JqBiHA5s1CeB7rjjoNONjzFjiToRpdO5TWHhu7DdImWILOqscaQ8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۹۹  شب؛ روایت ایستادگی مراغه برای ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/462336" target="_blank">📅 23:52 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
