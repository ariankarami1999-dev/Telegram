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
<img src="https://cdn4.telesco.pe/file/TfjLwu_097OoJnoZ44M-Ji9pmihqQz1FjWjyseytQvM5kXS0ZGqnn8_cutxsxKo6T6jJgf8vd2CqPQVoj6t-G1NA56-GIdEWYH1wDV9JldK01dIJNphvdxIg3vvpd61JYlqgIg_Gf7JDWbSoqs_G652deWwyUjA1SbvITEbBfccgT0Pfnr7TpOKj6RTbp2kwHiIMl1nuBEMp63atZWC1zdiPSjMDDhJzf0JsL-yguXDWXTHpT_Mz89dRXcJtPqMadMYZlayostozdqb3OBK4RX9dO4Q0tmcVbIDtIpksecISNeSEsH4JrNXhk_4_GzGKJ3iolp7co1zWyncW9grGhg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 134K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 21:31:18</div>
<hr>

<div class="tg-post" id="msg-69590">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPaw0qx88yQMq1jxFX5FY-nOAHIG8Gxx5aUMmCLDDRekkKKMOtLXhLl_C7HE6lzRfiGJTlfu2VgMizad0KFi7jkKvQ1honHiSLQmIzDtepNfoDoWg-W_xml1R7mJGi45kF5av7OR7icUBGSZ7Qrjay0YECSGn6pmGB0tKUm-0IJhnrUxM7fU-ylyP5xgH8T0SVQZrwKABnZiQ8Z-DVHNWoUdFd_ZAdRPonYFp4wnO8cDufZWYwUma_JFVISsRNPd8GiqrubIS1cfDMbtfgrab-_KXBCG19TltHPlTzZbOvFEiBYkgzKz4o5YPrUfnq8MvN4xQCcAkR95x-M9ijnM8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
غریب‌آبادی، معاون وزیر امور خارجه جمهوری اسلامی:
ایالات متحده تقریباً ۴ یا ۵ روز پس از آغاز دور جدید درگیری‌ها، پیامی مبنی بر درخواست مذاکره و حل‌وفصل مسائل ارسال کرد.
هرگونه توافق در خصوص تنگه هرمز باید صرفاً میان ایران و عمان باشد.
ما هیچ‌گونه دخالت خارجی در تنگه هرمز را نخواهیم پذیرفت.
با اجرایی شدن توافق جدید، مسیرهای موقت فعلی در تنگه هرمز بسته خواهند شد.
بخش قابل‌توجهی از مسیرهای تردد کشتی‌های ورودی و خروجی به آب‌های سرزمینی ایران از این مسیر عبور خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/news_hut/69590" target="_blank">📅 21:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69589">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca751f3e8.mp4?token=GQAuoe0pmBOIdAIPeZY8E0BSjVrZWdT8_0ihmgxCcjz48n4-NQRWsPGK23_as7Q1zvwU3_tcc7Cileb3b-14fC1I1erQogllKPncSUF1dXBz481cieZ1UBF4NuTBtjMK_bCZwrEFXe4jle9qSU6Fqm3IZIJIoRZmXrflF7Pf-ldrgNoYl6uHpi6yUBL7w-9TrkQ4XPwFd0XsmCLm3rPsuiCBDhnFm0KYzou9kDdus0_8bQ-MB8eSg9tXy7bSnRafSJAnrk470bE5qDTs6EH2VJKTVzpDO9I5W6kl0ahbnJDo2pq7DlBc5sb1LsjGMz--DmKxsrEGVN5h2U-fze4jVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca751f3e8.mp4?token=GQAuoe0pmBOIdAIPeZY8E0BSjVrZWdT8_0ihmgxCcjz48n4-NQRWsPGK23_as7Q1zvwU3_tcc7Cileb3b-14fC1I1erQogllKPncSUF1dXBz481cieZ1UBF4NuTBtjMK_bCZwrEFXe4jle9qSU6Fqm3IZIJIoRZmXrflF7Pf-ldrgNoYl6uHpi6yUBL7w-9TrkQ4XPwFd0XsmCLm3rPsuiCBDhnFm0KYzou9kDdus0_8bQ-MB8eSg9tXy7bSnRafSJAnrk470bE5qDTs6EH2VJKTVzpDO9I5W6kl0ahbnJDo2pq7DlBc5sb1LsjGMz--DmKxsrEGVN5h2U-fze4jVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
❌
🇮🇱
امروز در پی وقوع انفجار در ساختمانی تله‌گذاری‌شده در «مجدل زون» واقع در جنوب لبنان، دو سرباز اسرائیلی کشته و هفت تن دیگر زخمی شدند.
حالا قراراست بنیامین نتانیاهو، نخست‌وزیر اسرائیل، و یسرائیل کاتس، وزیر دفاع، ساعت ۲۱:۰۰ به وقت محلی نشستی امنیتی برگزار کنند. محور این جلسه، حادثه مرگبار امروز در جنوب لبنان است که منجر به تلفات متعدد در میان نیروهای اسرائیلی شده است.
به گزارش شبکه ۱۴، انتظار می‌رود مقامات سیاسی در این نشست درباره انجام یک واکنش نظامی قابل‌توجه گفتگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/news_hut/69589" target="_blank">📅 20:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69588">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12fe6dbab2.mp4?token=ZAaeXpxz60vGRalSsCHIy0s-IOwhgcDnX-2PIBBDaIwSl8VgtQfIGYx64OATKB5_JDizJcoXhN2N02WFMa7Egi5Ah57wktDlkb3AIECHlvjXiFK-KyLJ1qZiDszFRkTpz9B3a8fQWJLa4g_q-11Q-6cR_n6_UBI1Ih7gs1SJIY9POC3UC_Ad54n-BgIuzMo1lrbQIVNUT1sFdG8D_B4i2G9qRZ-bmBYbK03fHJjgvf7pBvqM_wo8i_awAd6vqvEylsDMDj9fAd1O_rJlUCIQWNcmANt7xXGNoaEc8bOQgZOUYyKa15klI90erX9JDsrQQhoVzNpYZzDgTk_9oNtlTarrJRbJN6wckK6Rkfk0iK8pT-VU2PM3ri5FVOLkahQt4ZWRlNXa7_eNBeDfJRGncFT7U7X26kh6WHZSfaznAaKPsKferyX-gLT-rsf3XP4sYcpZ7Xyj6WpNvAlixepDX9cfc7xjQDFgcu5JemsQAItZ-D2eeDrdTlOY65LAGZIhZ5__08vBiXLonxu0T_aMeh2fPamNAexFtr4Tozo_wFbg-vDNbro-isi2Kwt7AXPtMKoZtUZHhEPreooHNkD4Fvxc5DfDW9PwiTLnzBYBxYwgP2OuNMmZAZHYtGL1-94Z7RHaMxBM1_A_CrWMKD_WK7D3vLQtT96tCeeHcWH8bPI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12fe6dbab2.mp4?token=ZAaeXpxz60vGRalSsCHIy0s-IOwhgcDnX-2PIBBDaIwSl8VgtQfIGYx64OATKB5_JDizJcoXhN2N02WFMa7Egi5Ah57wktDlkb3AIECHlvjXiFK-KyLJ1qZiDszFRkTpz9B3a8fQWJLa4g_q-11Q-6cR_n6_UBI1Ih7gs1SJIY9POC3UC_Ad54n-BgIuzMo1lrbQIVNUT1sFdG8D_B4i2G9qRZ-bmBYbK03fHJjgvf7pBvqM_wo8i_awAd6vqvEylsDMDj9fAd1O_rJlUCIQWNcmANt7xXGNoaEc8bOQgZOUYyKa15klI90erX9JDsrQQhoVzNpYZzDgTk_9oNtlTarrJRbJN6wckK6Rkfk0iK8pT-VU2PM3ri5FVOLkahQt4ZWRlNXa7_eNBeDfJRGncFT7U7X26kh6WHZSfaznAaKPsKferyX-gLT-rsf3XP4sYcpZ7Xyj6WpNvAlixepDX9cfc7xjQDFgcu5JemsQAItZ-D2eeDrdTlOY65LAGZIhZ5__08vBiXLonxu0T_aMeh2fPamNAexFtr4Tozo_wFbg-vDNbro-isi2Kwt7AXPtMKoZtUZHhEPreooHNkD4Fvxc5DfDW9PwiTLnzBYBxYwgP2OuNMmZAZHYtGL1-94Z7RHaMxBM1_A_CrWMKD_WK7D3vLQtT96tCeeHcWH8bPI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فاصله ایران تا آمریکا با موشک فقط چند دقیقه‌ست، اما پیاده باید نزدیک ۱۹٬۳۰۰ کیلومتر راه بری!
@News_Hut</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/news_hut/69588" target="_blank">📅 20:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69587">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0660a7fbd.mp4?token=BKgwkZefWWmNU_pEUzwVR9uWLzELLsOTDfauAyCXg1mh6UlmoKugXza6OexcTq6B1oT_Z11V6QkerukZF_LSAHvkgOVjtOsTOzw2Zo79koYvNis64nbDzosLBr-rth2zlT-YQcb1wW9SJcZ1uQamm-CKoY-CtoHOftWLWpF4zCWZcwTUvBWRXuEYzwixaXOteo4I03LgWKwnm68nDLqUexkZQxp2VVNjaiqc-FJ5klbj2gcbnZojiDKVMdAvH8yrphM7DNU_E_ZWpErqEGhf3rZQSCg3FllmU0vv-Z93Yk3C4D6rAnqnWiOzywKm8e1YrBlsTtXKmr4Azjw1Cutn5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0660a7fbd.mp4?token=BKgwkZefWWmNU_pEUzwVR9uWLzELLsOTDfauAyCXg1mh6UlmoKugXza6OexcTq6B1oT_Z11V6QkerukZF_LSAHvkgOVjtOsTOzw2Zo79koYvNis64nbDzosLBr-rth2zlT-YQcb1wW9SJcZ1uQamm-CKoY-CtoHOftWLWpF4zCWZcwTUvBWRXuEYzwixaXOteo4I03LgWKwnm68nDLqUexkZQxp2VVNjaiqc-FJ5klbj2gcbnZojiDKVMdAvH8yrphM7DNU_E_ZWpErqEGhf3rZQSCg3FllmU0vv-Z93Yk3C4D6rAnqnWiOzywKm8e1YrBlsTtXKmr4Azjw1Cutn5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو:
ترامپ بزرگ ترین دوست ما هستش اما به صراحت میگم وجود اسرائیل قابل مذاکره نیست.
با توافق یا بی توافق هرکاری که برا آینده مون نیاز باشه رو انجام میدیم.
نیاز های الزامی سیاسی مجبورم میکنه این مراسم رو ترک بکنم.
در حال حاضر توی یه رویداد بسیار مهم نظامی سیاسی هستیم.
این جنگ موجودیتی هستش.
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/69587" target="_blank">📅 20:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69586">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">خفن ترین تیپستر های ایران با هم جمع شدن و TRUST BET رو تشکیل دادن
👍
هیچ سایت بتی دوست نداره شما این کانال رو پیدا کنین
رایگان بهترین شرط هارو براتون میذاره
حتی هزار تومن هم دریافت نمیکنه
سریع از این لینک جوین بدین کانالشون
👇
(این پست پاک میشه)
g14
https://t.me/+cBQ8n7zLQiUzN2U0
https://t.me/+cBQ8n7zLQiUzN2U0</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/news_hut/69586" target="_blank">📅 20:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69585">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1mVBnOY9Il_iowEyHWyypryntWUbv4xZG88JfOx5l82PU7NxP6LNl0T6UcoyZIqvwpvo7SwYBoi8FXN3KxZSpCE7qhyZS4pqjBHELpJTkf9cnvTp-tMSjTGpH8QAe-nIvmuyxzZoNWbtK8xZBGnmJIs_KEqOhvUbS0Wbts4F4ghFaXN_AfnGUmKSBQCGIn4BvU8yfAv2iI35kVRJaNQo7m3hGxWXD82eQW3iBtFLg6QuCPJamSikHcljwBqe5zv5fPkhNGxotQwPGEkYNSQtxV20hkEF9-Xy2wSanjTQ0H9q8b-XcXKiZgcfjrEFt6tz_dIm9jFX3kLLvi5nWp6UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">40 میلیون تومن برداشت روزانه ی کانال تراست بت
🎁
پول دراوردن از بت تجربه و استراتژی میخواد نه ادعا
برایند ماه تیر توی کانال تراست بت: 78 درصد رشد سرمایه بود
✅
40 بازی اخیر 34 برد
📊
💠
https://t.me/+cBQ8n7zLQiUzN2U0
g14
💠
https://t.me/+cBQ8n7zLQiUzN2U0</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/news_hut/69585" target="_blank">📅 20:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69583">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19fc284b17.mp4?token=GgpTwNeM3J9akqUFNh-tqJc3SM1zGMrp627DForFApulrT8XpLskmUxoz2ErJUp0B92DdOXIQ7qIDxDcL_5bG_1Dz8T4QnNOwgY44-kGl5km6LUFUY1OlnaUFiTaCwZIPkUjbUDtQV5A2_SbpH61uYWu9rj-i_Z3ayLnc6G329_OiNtwtcU5UDaE9VT1DaEdsz7_2ZtjNXYrjnE163Fhay1pWfQ9DkwvOrgIS1ntlpEnMgditxSnV7XPHO-jYgfxJ32waS0HTYcKMuu87_FTR7jgntK_csbgFRmCcoyyhHGClWiCkNj6kmAoJN-DhPe7zUt2cVpjmVr7KGsqGEnGhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19fc284b17.mp4?token=GgpTwNeM3J9akqUFNh-tqJc3SM1zGMrp627DForFApulrT8XpLskmUxoz2ErJUp0B92DdOXIQ7qIDxDcL_5bG_1Dz8T4QnNOwgY44-kGl5km6LUFUY1OlnaUFiTaCwZIPkUjbUDtQV5A2_SbpH61uYWu9rj-i_Z3ayLnc6G329_OiNtwtcU5UDaE9VT1DaEdsz7_2ZtjNXYrjnE163Fhay1pWfQ9DkwvOrgIS1ntlpEnMgditxSnV7XPHO-jYgfxJ32waS0HTYcKMuu87_FTR7jgntK_csbgFRmCcoyyhHGClWiCkNj6kmAoJN-DhPe7zUt2cVpjmVr7KGsqGEnGhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
پلیسِ رشت یه ون آورده وسط خیابون و شروع کرده داره به دخترها اخطار میده؛
بعد واسه مشروعیت دادن، یه مصاحبه از این خانم رشتی رو منتشر کرده که‌ با میگه:
گشت ارشاد رو دیدم احساس امنیت کردم.
امیدوارم این کار ادامه‌دار باشه چون اصلا از وضعیت سطح شهر راضی نیستیم.
چهره شهر اصلا عوض و زشت شده.
الان همه فکر میکنن رشت این شکلیه ولی خوب‌هاش رو نمی‌بینن.
گشت‌ارشاد دغدغه اکثر مادرهاست نه فقط چادری‌ها!
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/69583" target="_blank">📅 19:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69582">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
منابع عربی از حمله موشکی سپاه به بحرین خبر میدهند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/69582" target="_blank">📅 19:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69581">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d659457195.mp4?token=LXxipzIWjFSgs5T6CDLXzcGO65-p-fmh8IGu0KITLh_p1Lxj-FBJ3NPs9rzx4-SKi9XGushnNu5o_QGMPjUta-4zg8CfQmuNxI9t22Hzvcz1xhE_M5HFpvc8P1QJ_8H1XwGJH9myFnJuuuzwKX6ssVheEX-e7Ymy3CrM21OnGJ_G2bFfQXo0yUOOptKJHQx-xR1sGvJmaboAX2gsfGmtQly5KWW_jZKvLfYbfhyYjIN_dSAsmgFrX26Pu3W9LLdUL4rI0f3LQ0Y0ZjwjsaMXpVHN5GM3HUh7xJR62RmVAoN4oXYppRuNkATzxQMjK_ipCC3PfRSfVW1_MbKdhE2fTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d659457195.mp4?token=LXxipzIWjFSgs5T6CDLXzcGO65-p-fmh8IGu0KITLh_p1Lxj-FBJ3NPs9rzx4-SKi9XGushnNu5o_QGMPjUta-4zg8CfQmuNxI9t22Hzvcz1xhE_M5HFpvc8P1QJ_8H1XwGJH9myFnJuuuzwKX6ssVheEX-e7Ymy3CrM21OnGJ_G2bFfQXo0yUOOptKJHQx-xR1sGvJmaboAX2gsfGmtQly5KWW_jZKvLfYbfhyYjIN_dSAsmgFrX26Pu3W9LLdUL4rI0f3LQ0Y0ZjwjsaMXpVHN5GM3HUh7xJR62RmVAoN4oXYppRuNkATzxQMjK_ipCC3PfRSfVW1_MbKdhE2fTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مصاحبه تاریخی فیلدمارشال رضایی و خنده مجری:
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/69581" target="_blank">📅 18:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69580">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tky4zdmcB9VE41RQnjhJ6if7DzftinFqm_thjZMi7skQPtLA1Z3EDd6oRel9xfwlbjUUPBSF6lHykH3VGZkPLmtHLOd3rnreTsVTK_rFuK-S7xNiKQHsfqEvfJ-vZ1l6HEDblr9n1q1Da3uCkdqH4Uiw__KpvpkaETpMcoq7FXUEejds9Mx5-kqR4vqlJUTrWPtw8DGhgJNnPXA8uX2sHTcUm2X1nW39RZpoi71BsSR456VNeNU9UZFjtDYHryGxxCe37Dvt30l1nYKMzlPEbZfZaB2M8TnoljBoLBs-J6K3ZZfvbTpPh2h8UR9qlGKTc_W5Ad11mG4A-8v1iJYBsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پهپاد مافوق‌صوت Quarterhorse آمریکا به مرحله آزمایش نظامی نزدیک می‌شود
واحد نوآوری دفاعی آمریکا (DIU) برنامه توسعه پهپاد Quarterhorse شرکت Hermeus را برای ورود به کاربردهای نظامی دنبال می‌کند. این هواگرد بدون سرنشین با هدف آزمایش فناوری‌های پرواز مافوق‌صوت، سرعت بالا و قابلیت استفاده مجدد طراحی شده است.
مشخصات اولیه Quarterhorse:
⬇️
نوع: پهپاد آزمایشی مافوق‌صوت
⬇️
سازنده: Hermeus
⬇️
طول: حدود ۱۲ متر
⬇️
پیشرانه: موتور جت توربینی با فناوری توسعه‌یافته برای سرعت‌های بالا
⬇️
سرعت نهایی Quarterhorse: تا محدوده مافوق‌صوت بالا (هدف نهایی برنامه Hermeus رسیدن به سرعت‌های نزدیک ۵ماخ است)
⬇️
قابلیت‌ها: پرواز خودکار، استفاده مجدد، آزمایش فناوری‌های پرسرعت
⬇️
کاربردهای احتمالی: شناسایی دوربرد، آزمایش سامانه‌های آینده و مأموریت‌های نفوذ در محیط‌های دارای پدافند پیشرفته
پهپاد Quarterhorse هنوز یک پهپاد رزمی عملیاتی نیست، اما آمریکا آن را به‌عنوان یک سکوی آزمایشی برای توسعه نسل آینده هواگردهای بدون سرنشین سریع و کم‌هزینه دنبال می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/69580" target="_blank">📅 18:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69579">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3689824738.mp4?token=ljTaYCX2qiRYAkBpqgAKfiQHwdqYAwUyFysrDHWPtbaBcZIHUi6labNPJsZdCv0I6VcVxPnJJ-WxYTcOTxtCm-iRYzUZ1bj_NGkz1mcXu__zO-hzE6R1lHoX30sDGfr2Mr36t3SvZTT9jAzscMnLvc-FyKnqPat5aZKCR86ueQezoNeVod9Ep6beO-YlnQBSQbaCDKRzSCs9kcphDQ4CJVuM3U5_kQi6-Qsn5zRGKVUxFUy10vuVSU39t6xWIaxoIb3SV7Zb8bJpU5R1b9nSA-oNMIh6gDTX0NwFhV9iyDos7MH-clXE06QkyKDDczUmEEdZK_9-5xu79y3j7Jno9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3689824738.mp4?token=ljTaYCX2qiRYAkBpqgAKfiQHwdqYAwUyFysrDHWPtbaBcZIHUi6labNPJsZdCv0I6VcVxPnJJ-WxYTcOTxtCm-iRYzUZ1bj_NGkz1mcXu__zO-hzE6R1lHoX30sDGfr2Mr36t3SvZTT9jAzscMnLvc-FyKnqPat5aZKCR86ueQezoNeVod9Ep6beO-YlnQBSQbaCDKRzSCs9kcphDQ4CJVuM3U5_kQi6-Qsn5zRGKVUxFUy10vuVSU39t6xWIaxoIb3SV7Zb8bJpU5R1b9nSA-oNMIh6gDTX0NwFhV9iyDos7MH-clXE06QkyKDDczUmEEdZK_9-5xu79y3j7Jno9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
یه سرباز روسی توی دونتسک اوکراین لخت خوابیده بود و داشت افتاب میگرفت که يهو…
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/69579" target="_blank">📅 17:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69578">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5fdacb808d.mp4?token=Z8dg-Qx0OSbSFlT9LFhE0AYm6Py9IIbJbqPLnY4ORoENUS59po2so73tCinX_CfTzRbFQ0DIu7bAXgxD92Nry5C7mjYfPVlLClwqpcXbtPpCMMl8VPhlvhs8MY2I9Nf209WRECM7YidR5Kw6XCEElzOlO1DPV8gLdCF_KaYc6vuln3LzVVUNeRBD8BrAciTeo05Q1GAHA-nqevKTCUEnZUb6g7WJg5gsFrWuLH_-KX5z3dXWPSifQO5vT5qjT6y08f6pD77pqZnTodiDNvpkzYYTwgvaSLTOie6OW2ynUlv4OkUyc9V37qdV1GTkolOfDDBvtjqfm2UcvvFxJ1WZ_g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5fdacb808d.mp4?token=Z8dg-Qx0OSbSFlT9LFhE0AYm6Py9IIbJbqPLnY4ORoENUS59po2so73tCinX_CfTzRbFQ0DIu7bAXgxD92Nry5C7mjYfPVlLClwqpcXbtPpCMMl8VPhlvhs8MY2I9Nf209WRECM7YidR5Kw6XCEElzOlO1DPV8gLdCF_KaYc6vuln3LzVVUNeRBD8BrAciTeo05Q1GAHA-nqevKTCUEnZUb6g7WJg5gsFrWuLH_-KX5z3dXWPSifQO5vT5qjT6y08f6pD77pqZnTodiDNvpkzYYTwgvaSLTOie6OW2ynUlv4OkUyc9V37qdV1GTkolOfDDBvtjqfm2UcvvFxJ1WZ_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
توی مراسمات اربعین امسال آهوی ایرانی کباب کردن و به زائرین دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/69578" target="_blank">📅 16:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69577">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yu2t8zjQ699wLlxessi_d8uj-0P7Q84GicATwCZDgeLDuPZurMdZQ08ErbJJWGiFikXSgX8e9lNmFvEZ5Aiqg5TlKZ3yPENSLZl_WbWaLP7LRFEcmpfiW4RX5ck7N3sD5nEt0ktwPijyHvNorm_FIjZJ7KPbHUHvNKMfKwGn6iz-cMJhABd5JtgA7cGtAVABKFut8IqiwROtMhuwW-AHkQhhzJ3Q6n1b1HC5gLisb1id7wMIPk9ZzUY3S6ZX6X1q0ey4jo79FJGikHiKyZ_emU3MfGhbZyoRTjxtfSqjNZLBPOaTk1BTx3m209liR8-nTswSnBdic0Hab333N0Tt9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
#فوری
؛ ارتش اسرائیل برای شهرک المنصوری در جنوب لبنان هشدار تخلیه صادر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/69577" target="_blank">📅 16:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69576">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66218d020e.mp4?token=ml2PrSx-0DZIjlXhT3z0o7URLgv-771a1UXxNa-IL4XsVf1ZXcJ1r-GZb5F2NQ_vcBzQzJnDnXzK3N-_VfJTxZQxqG1VwuqgVPOjq7pIWg7kufasSlcjUUzMRB1ZOj1rfAKZlqZgPpPguUApFDfNQpCsVtLIr9ZbyEUnu-5jInhRzB-Yq3A0AQWWzUI8ONww2zS5BsgfPMQjdduaMYw05PNVZ7PhbArxCW9uUxQ1Tb56PI3aeSYwK6gKeqKr2NitWdKvs2tknJalWajViSI7hiqGkEWQnTkHkQinRZ_-nTMDEPrK3Xmi3kvqPI-Hdf7EX_svG4ykb_3NuswwwpHcXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66218d020e.mp4?token=ml2PrSx-0DZIjlXhT3z0o7URLgv-771a1UXxNa-IL4XsVf1ZXcJ1r-GZb5F2NQ_vcBzQzJnDnXzK3N-_VfJTxZQxqG1VwuqgVPOjq7pIWg7kufasSlcjUUzMRB1ZOj1rfAKZlqZgPpPguUApFDfNQpCsVtLIr9ZbyEUnu-5jInhRzB-Yq3A0AQWWzUI8ONww2zS5BsgfPMQjdduaMYw05PNVZ7PhbArxCW9uUxQ1Tb56PI3aeSYwK6gKeqKr2NitWdKvs2tknJalWajViSI7hiqGkEWQnTkHkQinRZ_-nTMDEPrK3Xmi3kvqPI-Hdf7EX_svG4ykb_3NuswwwpHcXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
وزارت دفاع روسیه تصاویری از حملات پهپادهای جت‌سوار گران-۴ به سه کشتی باربری در دریای سیاه غربی منتشر کرد.
وزارت دفاع روسیه ادعا می‌کند که این کشتی‌ها تجهیزات مقصد ارتش اوکراین را حمل می‌کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69576" target="_blank">📅 16:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69575">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/474cba356d.mp4?token=f_RSnj2iP326U5dXMUV-51ERONSboqSfR1s-nPOHj_DxXuTDAJUtOdyANJZtQXs-2HPvE3PFqzNo9Lu-n8QYH5TlBEMnEytvazVKNGbGfbi6J3UpeCYn-eXhP4KnoRvgQYzOz6qTCZvPTO7WkZOXTQXFcVtz0JRg7xdZmxC6o1hoXxV29mP8XzB2Ze5QO8vX-Ofe4xtoPyJsfEiY-J6VvxHVsOm1tzm1t-QIZlrivFNkdYqtIYlw3VTjOGeaGTS5l1Kjwf6JUDu07d-ydl6zEWObMN8VFT6Vdo3QoSojWEzklIjsfjKIPdzai0J7KgMIcoiHbEH8Si4DI0g8bnFl4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/474cba356d.mp4?token=f_RSnj2iP326U5dXMUV-51ERONSboqSfR1s-nPOHj_DxXuTDAJUtOdyANJZtQXs-2HPvE3PFqzNo9Lu-n8QYH5TlBEMnEytvazVKNGbGfbi6J3UpeCYn-eXhP4KnoRvgQYzOz6qTCZvPTO7WkZOXTQXFcVtz0JRg7xdZmxC6o1hoXxV29mP8XzB2Ze5QO8vX-Ofe4xtoPyJsfEiY-J6VvxHVsOm1tzm1t-QIZlrivFNkdYqtIYlw3VTjOGeaGTS5l1Kjwf6JUDu07d-ydl6zEWObMN8VFT6Vdo3QoSojWEzklIjsfjKIPdzai0J7KgMIcoiHbEH8Si4DI0g8bnFl4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی صداوسیما خبر کشته شدن ترامپ رو تمرین کردن
😔
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69575" target="_blank">📅 16:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69574">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dd7b_blE597c9V18S60V6KV18xaU2tgBsAhcL1z7icMSs-GIV1gfKogNqtbAHYj6JcFof4Gv21k_OWNiLjpHFIhfeZT7MDWTf7XXCOikGYEJ44tcSigW2b-dxVyqfmNwz229h2338vSfbH5Gcq1xSNTnYctxWV5ozx3U1Pt2hPMsV8OKykWuyYwGlc8kIzbF-qCm4WyRxDmace9hy3bOg8_rwZcM6HNfZ1Fg8Y62YneND2LnFdKuuUWYm15iJsIjiMd_sTRnob_GKfSgsOdvzjcR9AFpK_eJMsnPzmmBC-2iAK4q-3wRiZiyOTCX4PvZhXR4fvn7Uze5wNQRxP78fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💢
📉
قیمت نفت با کاهش های پی در پی به ۷۶ دلار رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69574" target="_blank">📅 15:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69571">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uqXC0b22XjlDhzWHAASMitc0FIlfUu7N2cMsZvX0F4SZSIhm7_CrfTZOvgGMfXnAmw1Mx0LoqtAC_Ez8ZOHZU7TIfYqUK3DdJN_lLAUQ9_GWHh1jp3dEDHbfGEjZwhaGMlBB5fDXYFGJIDVB3i26Y3mWJ_DaASeHXWvsMRw4AdYIyhDoI2BNmkPLX0GxDIw5e8xinLYKSSrF0Nr2FbWjaHSY1ublWHjzjN-sieAuqBmz-70l39On8ly_sNLtrB04i1SyWChQgU-7iyZOVSKIh2mJW7f365R-tknJjgcMUo5Q5xVkPOQDW59V9UFXMFBtbHvZg1HhBaWvpKQ9n-yBCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q177bzmUaAbbQ9U-sERREHRwvhXz4ZDpONDivU_OsEg_NrYATL1C0MwN7vYH3idtQWbKcAqdHfINxMcfcYsgkqWm_HepLpDw82-NW20AJ9a5Gkb8tKg9LG_Wsog4SgVwdulpDuqzbjk6xSVi_8V80yNbNoO4a2K21YXmI5eWXP2ZhsoNUBzwaOExj7uDd3gsdiOF4lxlfSZrrBhe_SzeM0tlDOWHQuIZSCr3gJqwnNbJoKOHp5uIrc1RHRgAiV1QiIWoON2X0vb88h3lBdnv5cf7OQ_ym8DiWL4QBlMzKKkzrOngfVaXnyTTSiN7Yp7XiAjIx1Ul9OSCsAz3mKYJLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NePd2AjrG-qIKCOGEwSRRJRBu8QPtCXKTg4Jr5xd-M6Al2hvwDNX_KJhsRUYgOP8lPq20xSjliPUH6R3r2mavzA3uHPQWlWiIbOziLmdg3MU65s01bBES8PdA-RlVKKIj9mhZPt0YdpkIPQebwRSo_8H7X1YdHL3-B_4t8EpFUWld94wWP-jENr_-aIvxqaWXPIFKojew1wGpCUUCaH2LII7m_XBcdQOgaHv_0r6XNAnhJLYVnM-OJq0NQb8W70dbbzjo6wnECG-xTuNNJSq8bxuX-vffIRjvyEKXSX1ZGFNThYrgJu2B7kSx6lvqW_yzfT2i4TL5w7siqgbFTgPzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
پست جدید و لاتی کریس رونالدو؛
"
اسباب بازی‌هام
"
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69571" target="_blank">📅 14:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69570">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GF5vycuiAZPED40pdet7bBmTMcJXa81xLU0ujb_9OwYuw2l18RVpAJTw3pGWBAOW_vS6DDym5AsCa7z4yPc5xtuSv3EkFeRK__zSEjx6Y1zXuH4xlJH3lv5B-cfeYj5CMlOmdjHKTE2y7Z7tp6sn4Ab85K63Q1DOcZjJyWISB05dTR4w657y5-o59d9usF05uVyvptI5fJzZdAHaGUEgw3ywo7OJZ_CLnkyXGRbFk7m_jDpX2uXWckpiYG-ZkLyVKM8p7hbyWUJp9LWNT5clGI-ZC9SmC4fEaR9BT0uc3vjEjdfpNn-K1HCU-SW_zbfAiQGCLgqQ6xsrohkVS6ICZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
دسته‌ جدیدی از سوخت رسان ها برای مذاکره وارد اسرائیل شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69570" target="_blank">📅 14:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69569">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Db3cnonA-aY3BBQ-RTrETMfG_Pb2Z2pS4P6NAkg2UrswauH9cakLKHhJSf2L4DsoJmXIMt7Ws8y0Yck9jCroTPb1nPvPTxeBKfQozhhGSX6FUj2WMzAKmAhSUGlLWyXZuVp8B-g1ooH34eRX8VppN77TvYAh13dwNSe4cw2ds9xwNNF6DtyX3ROcTD1Ao1-6m03qggxuDdAy5btdZ9n06aW_ieldvBYoduR0IO_qDwjFjEHHewjP1Xz0pwoBj4p-_qoHM7GylzY8M5JDgksTMZChzCjaPzL4rW3q5yJJAGCDl5iLbdml46geB170ySNLIE9QMT5ybOlZHkLVi2Z19Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
❌
حمله هوایی ارتش اسرائیل به شهر المنصوری در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69569" target="_blank">📅 13:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69568">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f4b05f8c.mp4?token=j5y7JDSbRIrjWznonCRx63zZgN6JwdDjwHZ5B8zNh1YMNet2chFXNDyeOMd5cMQCLMVh0N1f95lgfgbUojQyC9jvh5pgGIGX75_iQfboiLIgnlQa0euPNLHqf0JUy8cIGWMrDRfi5PPKmyStfatAJSbNimGXZU-2EEPCFAVFhLAnyz4XMz3VfrpuQcuyc1pciWUCOSDGQsl_p5dhEzXXqVZh1XyGRjqjNmJ9rdZQ64pwXfWXhWELby_Zjt5bJ5fUs6iLjOJ3f1HiwSej7gaITKESyMCDCxeBMR8OfI-6VjfaFV66-yGN21gpx4E6_lfpEc-S4kPOywbMInOtsrxgXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f4b05f8c.mp4?token=j5y7JDSbRIrjWznonCRx63zZgN6JwdDjwHZ5B8zNh1YMNet2chFXNDyeOMd5cMQCLMVh0N1f95lgfgbUojQyC9jvh5pgGIGX75_iQfboiLIgnlQa0euPNLHqf0JUy8cIGWMrDRfi5PPKmyStfatAJSbNimGXZU-2EEPCFAVFhLAnyz4XMz3VfrpuQcuyc1pciWUCOSDGQsl_p5dhEzXXqVZh1XyGRjqjNmJ9rdZQ64pwXfWXhWELby_Zjt5bJ5fUs6iLjOJ3f1HiwSej7gaITKESyMCDCxeBMR8OfI-6VjfaFV66-yGN21gpx4E6_lfpEc-S4kPOywbMInOtsrxgXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇷🇺
دیروز طی یه مراسم تو روسیه، یه چترباز از هواپیما پرید پایین ولی چترش باز نشد و سقوط کرد و درجا مُرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69568" target="_blank">📅 13:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69567">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phgihB6RglSJEha4QerpHlyF7p4wA69xQj7mxULcANw9pyKATSBWbsUgQDwymmPuLRNMWL5WCUfIUW0h1zdefrJSnIIv3TDs4BbCNiryvZqhaBPnyVfCQNlfK4ZZ2SRLDAcO36FoG5lw1NeKFbaYhmSsF7QxGb9DR-ZKxWx5JAz3NdRi7cvjrvaD-7Bab_8yT2FLsfqa7cXx-woF7M0ooZCWF01otCxDTjBTjD2d05lFirweHToUSNCEffFaFxu-1XivNwfR6yEl9UWc4oj333htIwmiuiHW2wLdOPgJx1Fp6C9nGemcqBoIVKsHiW2QAXZzqSBpvu9X5JJYlMTfdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
دونالد ترامپ تصویری با هوش مصنوعی از خود منتشر کرد که در آن با لباس نظامی در کنار ژنرال پتن و ژنرال مک‌آرتور دیده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69567" target="_blank">📅 13:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69566">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cc20a5985.mp4?token=LGcZOONBYTnbLzFwfeB7G6rmAhhxoTQpKExgZ0oNY9wgacToIDTzFLmGQF2Mpx0kDKrWf4gmy4DUfnt_puedoLl4stAO8FxdmTAf-AlUOY_PozX7f7qOzUC-NFvya8YgfYK7MfTNIYmo_6Pevg9QFnZMBmriRDSlR3iBM3QQWTBs4R1VsmtV253jpDohTXFjRc3j55LzrlpkUtRHbq8WDwRT2P8YllBrbzP-HxYgTKCiLiIyFbxUnoAESHmY4HD1w9cF3pNfoYHJELRvxEW0tXqw0cYV-B7Ha3W07vKzj1n0jkDgwRZrKIduaZ1iEkIov3pzwVQ1arE_VTsQKDm1yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cc20a5985.mp4?token=LGcZOONBYTnbLzFwfeB7G6rmAhhxoTQpKExgZ0oNY9wgacToIDTzFLmGQF2Mpx0kDKrWf4gmy4DUfnt_puedoLl4stAO8FxdmTAf-AlUOY_PozX7f7qOzUC-NFvya8YgfYK7MfTNIYmo_6Pevg9QFnZMBmriRDSlR3iBM3QQWTBs4R1VsmtV253jpDohTXFjRc3j55LzrlpkUtRHbq8WDwRT2P8YllBrbzP-HxYgTKCiLiIyFbxUnoAESHmY4HD1w9cF3pNfoYHJELRvxEW0tXqw0cYV-B7Ha3W07vKzj1n0jkDgwRZrKIduaZ1iEkIov3pzwVQ1arE_VTsQKDm1yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درباره ایران:
خب، اگر دوباره پا پس بکشند، ضربه بسیار سختی خواهند خورد. آن‌ها این را می‌دانند؛ آن‌ها این موضوع را درک می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69566" target="_blank">📅 12:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69565">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336dcdad36.mp4?token=bHmnylogERl_BMeF5eW-nw2OSS5TIhsW1lq5vd3sMGnIXW6W3DFHxqAS0veeVb8XSEUD7cJFKAuwt9pCQFj9gmOOTh3IVNlcE6NimJ09UJadYqaA0Bi8P3oZBm5UsDjd4GCZMXK6OENQXfPpy5JltBpBrTr3XsSt_3tZQJl1J-LBMThLpmBZ7Ssz3uD_luRecoL-f_3XPcH5ob8_YDJJKCMLruAb--tX9URgkQsFlIxDaU5E1jn7vd0qbgEd0Otgxfp6jlNYaV0uTTsNJRM6LWvVc3Qy9EBR8lAXp3TgNgeDuUMsNwzhjrWzv7RQWexRVBj8H0AEO9etZn8O8flnzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336dcdad36.mp4?token=bHmnylogERl_BMeF5eW-nw2OSS5TIhsW1lq5vd3sMGnIXW6W3DFHxqAS0veeVb8XSEUD7cJFKAuwt9pCQFj9gmOOTh3IVNlcE6NimJ09UJadYqaA0Bi8P3oZBm5UsDjd4GCZMXK6OENQXfPpy5JltBpBrTr3XsSt_3tZQJl1J-LBMThLpmBZ7Ssz3uD_luRecoL-f_3XPcH5ob8_YDJJKCMLruAb--tX9URgkQsFlIxDaU5E1jn7vd0qbgEd0Otgxfp6jlNYaV0uTTsNJRM6LWvVc3Qy9EBR8lAXp3TgNgeDuUMsNwzhjrWzv7RQWexRVBj8H0AEO9etZn8O8flnzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فریادهای مجری کشمیری(هند)صداوسیما درباره تنگه هرمز:
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69565" target="_blank">📅 12:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69564">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/69564" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
R14
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/69564" target="_blank">📅 12:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69563">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoUC7Nr72cbFM3f1p-UCG20K_XicwfYhKgR8hKnPz6QJ-MPf3GyS4w8HRDL1mPx57AVXvykj7j7pHl_V8YNBB7XZIhZQCOUy7icqMpXkyZXOJdyKDub2F2xq-P7xYzH5QibjUcf8fLl2M2P8qWfjclFfIyIzwDN1VKOu9w_EGd05T6XVW-bd_vYHKxP2bH4xDZGHQq-OtoUHBu_7mxesPM12eWSGrjx52M1bSLFo5LNkzBz0yoU2YhiK7TKn85cfzo8dvsDVaqJ34aV46KVm3SO0MR_ORuiNr6Vp3_S_AlMjtqYOaEdduszIi-n1S_WxVIaSMR3bE6Vx85Rc20NkCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r14
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/69563" target="_blank">📅 12:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69562">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aba5ea669d.mp4?token=gEaNg3PNy9RWfRpqRCHes4ImAjT3A2FFxp3Amx4xiOI0SjJF41JoG1h1OwzIoODJVZCWmDTiIf1upYQFqkhfqCOgb3q4X5zt6NaIfBhWe8V3QdFwJkkyI4fyZqUQnFTiSucdafl3HgdA_So_GQ6QWIUH1wgMeZD9fzDxwCH8MIbTS3LzDwA8_F4d2hScRicQG3-0j4i8jgLJBkdF5-21tk0nJ_XeMqIiQqlGSiVBTwsb7gfb0tl_Oon-1A057-Ca0jrRFMyGkjxvgOtASHhq6vD7B6d_zPT-tyZE0sPwh6h_v6GKDD0bSHSbCFwPJ1u-WMWvl2WyeoIc7MacAIwAAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aba5ea669d.mp4?token=gEaNg3PNy9RWfRpqRCHes4ImAjT3A2FFxp3Amx4xiOI0SjJF41JoG1h1OwzIoODJVZCWmDTiIf1upYQFqkhfqCOgb3q4X5zt6NaIfBhWe8V3QdFwJkkyI4fyZqUQnFTiSucdafl3HgdA_So_GQ6QWIUH1wgMeZD9fzDxwCH8MIbTS3LzDwA8_F4d2hScRicQG3-0j4i8jgLJBkdF5-21tk0nJ_XeMqIiQqlGSiVBTwsb7gfb0tl_Oon-1A057-Ca0jrRFMyGkjxvgOtASHhq6vD7B6d_zPT-tyZE0sPwh6h_v6GKDD0bSHSbCFwPJ1u-WMWvl2WyeoIc7MacAIwAAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محسن رضایی :
به عنوان یک سرباز از‌ همه ایرانیا تقاضا میکنم یکمی دیگه این شرایط رو تحمل کنن. چون ما داریم در کنار آمریکا؛ چین و روسیه به قدرت چهارم جهان تبدیل میشیم. این شرایط گذراست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69562" target="_blank">📅 11:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69561">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1729d69d0e.mp4?token=m8C7Si_4AhXbNQBt3OQsG0hVtOGDz2qEhVYCLb8INbthhVaZvB6pBh50DkjHgACXQyCKkT7L6iXIOoMt9RaCrKBAVPCatKX6uWTVmDwScrSZ8ftXkF-bo1juUelcPmCItRVCs_LBfKTyJKa1ihxQQ0N4BuQsuEC_D3JBNBkcCAmyoLzcK4h_c4evQDShdhmFJyR6hg9nA5gymlDXJUwA85cHAFkmx3-_dy0y9Zr6vlbbSVtF7Vg7ykE0TTdxVLzFWBjMOrzdIX_rlYG0jXifwTe2DHaJPWWPXK46beYOzDo52u8fTQ6ODTjfYK9GPBhg78KMw3Ln4EeoBVopGqaf3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1729d69d0e.mp4?token=m8C7Si_4AhXbNQBt3OQsG0hVtOGDz2qEhVYCLb8INbthhVaZvB6pBh50DkjHgACXQyCKkT7L6iXIOoMt9RaCrKBAVPCatKX6uWTVmDwScrSZ8ftXkF-bo1juUelcPmCItRVCs_LBfKTyJKa1ihxQQ0N4BuQsuEC_D3JBNBkcCAmyoLzcK4h_c4evQDShdhmFJyR6hg9nA5gymlDXJUwA85cHAFkmx3-_dy0y9Zr6vlbbSVtF7Vg7ykE0TTdxVLzFWBjMOrzdIX_rlYG0jXifwTe2DHaJPWWPXK46beYOzDo52u8fTQ6ODTjfYK9GPBhg78KMw3Ln4EeoBVopGqaf3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
املاکیه دلقک:
تا ۴۸ ساعت آینده خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69561" target="_blank">📅 11:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69559">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XEDM5oHWl4cW5nSgvlcwAen7eFoFZsTRsE5gEuFjJUFJ-uSGHb4WQ4sT74_COwOWoGLk37eJeSsOnARqtnNlMryNgHSJ1qulGc3h_miaICWgIf6Lm4FnwXzDpfHktPn_hl4tr7u5pNSz0RkTf2LaG_FyJf4NKzm10yNdkDUUdn9a5mbX3CX4BafvoK73XsF_j8f_O5bl9Ijpiseek6VvVMqJTSZSe6MPTd7T2E2wO5MrtLdGteZs4H0vQGLU5JCNquxPQ4wMFMfHcDH0F_OZX0M3RtXy1W5GazIVLltKMHiZ_xOQJNzQGldWKx7FXPGiAYnFfDLzCK6zuYjnZpGxSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e2fe475d0b.mp4?token=oF_5cDvwRJ0B1_HvdKz0ewfUZCbznk7cfSDfm8dUgH5_XRvf_ont5RT3hMazhSOja4E6yqSjId_ABjFxQ-erXuzTGsDrpnsRar19NYIjfvJhsbCnGGDEPrXuDbDI8q731gkvpjcUzES0bay8xxnhsP-MU2EUAa6mUFVCZEdms4Wvw0pXsp_qu5uN6BzduEvDOgMoAkEZUy7TvT2RDELnQIzL1S_8Y6Z0OEyEgqQ8pBBNNh7pByzH6FbaiKNxqu4cpSYhudP0IBJLGsK6YFBO0ySfTOmygLWz13fF-czfXD8wqnkiWhYwGwHNe1GXkBYsHjYoQU38meodzuWt2xwzaw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e2fe475d0b.mp4?token=oF_5cDvwRJ0B1_HvdKz0ewfUZCbznk7cfSDfm8dUgH5_XRvf_ont5RT3hMazhSOja4E6yqSjId_ABjFxQ-erXuzTGsDrpnsRar19NYIjfvJhsbCnGGDEPrXuDbDI8q731gkvpjcUzES0bay8xxnhsP-MU2EUAa6mUFVCZEdms4Wvw0pXsp_qu5uN6BzduEvDOgMoAkEZUy7TvT2RDELnQIzL1S_8Y6Z0OEyEgqQ8pBBNNh7pByzH6FbaiKNxqu4cpSYhudP0IBJLGsK6YFBO0ySfTOmygLWz13fF-czfXD8wqnkiWhYwGwHNe1GXkBYsHjYoQU38meodzuWt2xwzaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی:
🇮🇷
جمهوری اسلامی دریای خزر رو فروخت رفت!
در تازه‌ترین قرارداد، جمهوری اسلامی دریای خزر رو تقدیم روسیه کرده و یواشکی دارن میبرن مجلس و تصویبش کنن.
سهم ایران فقط به ۱۱ درصد رسیده! شما ایران رو فروختین و شرمتون میاد بیاین به مردم بگین.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69559" target="_blank">📅 10:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69558">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6f67c295.mp4?token=TBa_qY67ZEomzXrsan7zrvV1qTDjm6crJxZnbVj9FzMhdgukcUc_JSTp1tKzPonjS49RROGr3632ZXdRBUyzzXcMeK4LxLLjaf122NPFkm_yZbrbF57kdar296mErUvPn3k1sD7hq92yeKJfvL9Hp7da7NBoi_xJJ0O-jvo_9ObSderdTkQpVGC6Y65X3cm7BOxC35Q6MIKYLk_csuzRnf7kxWnrwvG06jkxHaJCM8FoF-5906TZlVMeehEMbGdEivkrjXXpQqgkiBJtzTBBE_sdP8LXy3baHBdMKbe_OR-zPViqe1Ovn24-gouIoxi4nUneg_B4K3ZwCSu0Okb1GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6f67c295.mp4?token=TBa_qY67ZEomzXrsan7zrvV1qTDjm6crJxZnbVj9FzMhdgukcUc_JSTp1tKzPonjS49RROGr3632ZXdRBUyzzXcMeK4LxLLjaf122NPFkm_yZbrbF57kdar296mErUvPn3k1sD7hq92yeKJfvL9Hp7da7NBoi_xJJ0O-jvo_9ObSderdTkQpVGC6Y65X3cm7BOxC35Q6MIKYLk_csuzRnf7kxWnrwvG06jkxHaJCM8FoF-5906TZlVMeehEMbGdEivkrjXXpQqgkiBJtzTBBE_sdP8LXy3baHBdMKbe_OR-zPViqe1Ovn24-gouIoxi4nUneg_B4K3ZwCSu0Okb1GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
پرزیدنت سابق، جورج بوشِ پسر:
مذاکره با قاتلان، گزینه نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69558" target="_blank">📅 10:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69557">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQ5EA8cqCDZrn7PB6kWSaRmNC7oGCKZhRGPsBnBg-WF7vXp7oX1-X-od0v0oXJ2QxxClotBxx4Q67CCthooHldxvdx4Sf_TP7Dc22hfA_OwZJo8kVv_G472gYYjuTgE4rsvWTueE9MGWk0nwrjb8UN3cZm78jVdVWRt9EJt7Y-HFPmhxRXf6PjRTtDm2hx_atFK8g6gZBbHbkDAQUvNTSgBB7-TYS5wSAVibp2Su7Q-EsF74IDpyjvVwEInG2j50otmD4ZOiyVen9jlA9gYixXhm1gZgxkSMlnVBVnravbQAPrbnK6U_LcLT2Y1EFRJ4nZAlZ5I5xhRu4Bdi9Ol_4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇴🇲
🔝
بر اساس گزارش آکسیوس، آمریکا، ایران و عمان به توافقی موقت ۶۰ روزه برای بازگشایی تنگه هرمز نزدیک شده‌اند و احتمال دارد این توافق روز چهارشنبه از سوی آمریکا اعلام شود.
🔴
مفاد اصلی توافق:
- کشتی‌های ورودی از مسیر شمالی در آب‌های ایران تردد می‌کنند.
- کشتی‌های خروجی از مسیر جنوبی در آب‌های عمان و با هماهنگی ایران عبور خواهند کرد.
- برای عبور کشتی‌ها هیچ عوارض یا هزینه‌ای دریافت نخواهد شد.
- مین‌های دریایی در مسیر مرکزی ظرف ۳۰ روز پاکسازی می‌شوند و سپس این مسیر برای تردد دوطرفه باز خواهد شد.
- پس از این دوره، عمان و ایران درباره یک توافق دائمی مذاکره خواهند کرد.
همچنین قطر، پاکستان و عربستان سعودی در میانجی‌گری نقش داشته‌اند و کاخ سفید نیز مستقیماً در مذاکرات مشارکت کرده است.
طبق این گزارش، عباس عراقچی با این توافق به‌صورت اصولی موافقت کرده بود، اما تأیید نهایی باید از سوی رهبری جمهوری اسلامی و شورای عالی امنیت ملی انجام می‌شد. یک مقام آمریکایی و یک منبع منطقه‌ای نیز مدعی شده‌اند که این تأیید روز سه‌شنبه نهایی شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69557" target="_blank">📅 09:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69556">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5c55d9f368.mp4?token=J6EJGpXiaiS1Put3zbsiILRdkt7Uz1_M9EavW5ELJ8YMPXeNeRj05tItvTiK1icevCKr7h3TjwA8rg-1AKE-tE4B3j4SNa7UAOfD_CugRet_BacKkF34_OWdqSjZzqWcqXPPXiqsuDxsfXYCMqPkr5xluDg409SmTr5Ju7W1NYmryBHbCi6Yxc_gK0Q1MQiNMochJhwMFiCyv07S2m8wN2Rgg8rje5UrKsRj3bd_LfY-afT3o9OAl39Y4iLeguO12RtuyJHCNVAqN0lecF9ugCY9KgDTCbkqw4I06U8wBqQStLxHNQPt9EX4Ua--LA7uPMZ9qXtG7FVZc9EGdSkc6pn1mcVuyAjKXi_aJmAkXnc8vOn8hLIgLkc1TVXCgH-fW7qfn5oNJ3FsWkfA2H8amnUeI3KwdM-oHMjOcP25igMjRe2s22LlQbgC0hM-3ujV8LexTmO56e8bXXGPDiB18QS8yFrpbCXqHGLHuhTK84U5lKdiA_r64S5QB9XH3ktlN9XolRE0kUwtwJcQ86vobpZZMr4CV4kpTPBebXz_EVD6HvalaeEdXNGiVI3ZYBZF_yrXZqmPvB1SXSQ575aL1nJVb3wra78arzaosFwoXZfdwej6lMfffHoDoda7kQfak2pHitGOxG99Tk0oESrOl8oO9Go3qKBiNXjvrpQmHE0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5c55d9f368.mp4?token=J6EJGpXiaiS1Put3zbsiILRdkt7Uz1_M9EavW5ELJ8YMPXeNeRj05tItvTiK1icevCKr7h3TjwA8rg-1AKE-tE4B3j4SNa7UAOfD_CugRet_BacKkF34_OWdqSjZzqWcqXPPXiqsuDxsfXYCMqPkr5xluDg409SmTr5Ju7W1NYmryBHbCi6Yxc_gK0Q1MQiNMochJhwMFiCyv07S2m8wN2Rgg8rje5UrKsRj3bd_LfY-afT3o9OAl39Y4iLeguO12RtuyJHCNVAqN0lecF9ugCY9KgDTCbkqw4I06U8wBqQStLxHNQPt9EX4Ua--LA7uPMZ9qXtG7FVZc9EGdSkc6pn1mcVuyAjKXi_aJmAkXnc8vOn8hLIgLkc1TVXCgH-fW7qfn5oNJ3FsWkfA2H8amnUeI3KwdM-oHMjOcP25igMjRe2s22LlQbgC0hM-3ujV8LexTmO56e8bXXGPDiB18QS8yFrpbCXqHGLHuhTK84U5lKdiA_r64S5QB9XH3ktlN9XolRE0kUwtwJcQ86vobpZZMr4CV4kpTPBebXz_EVD6HvalaeEdXNGiVI3ZYBZF_yrXZqmPvB1SXSQ575aL1nJVb3wra78arzaosFwoXZfdwej6lMfffHoDoda7kQfak2pHitGOxG99Tk0oESrOl8oO9Go3qKBiNXjvrpQmHE0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
تنگه به زودی باز میشه یا ضربه شدیدی بهشون وارد میشه ک باز کنن
اونا با من مودبانه تماس گرفتن گفتن میتونیم صحبت بکنیم؟
ضربه سخت ایران تو راهه ولی قدری دردناکه نمیخام ازش استفاده بکنم
خیلی بحث هایی خوبی داریم ولی اونا نمیخان اعتراف کنن چون یکم نگرانن
شما میگین مذاکرات فوق العاده داریم ولی اونا میگن دروغ میگین
اونا میخان معامله بکنن و بشدت خواهان توافق هستن
در عرض ۴۸ ساعت خواهیم دید چه خواهد شد
قیمت نفت و گاز دیوونه وار میاد پایین چون سه شنبه مذاکرات فوق العاده داشتیم
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69556" target="_blank">📅 09:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69555">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d290294320.mp4?token=qOwo4gdaIJmISBKaGfhL9tiLpIxs5zBOdzGVLnoCHMeePg3qBz2PIYTqFl0nJleksfzyKpeOqZlnkcIOV99AehYkSCQRJUcuhqBgwT6GOrdaOERIFlZFGohuLZUOklbNsSn7JR4RMLb91wmAuGOb_5_RTqapp_03_FxWwyvL2yDdRknTP441zS66WqWMzSQZjk6K-46WapeWEp2nMaSk_NxXug-VeR7cJ2xuJdE97tcSQ84TVnt6OaWdVvlo8tGlek-3fUaBnaNHZncFK7LqaE63VGTc0TddCNjFNWdeEdEVmtf-2KeR6C99NyUbLgQCvsICrswpPMn5j7OlSuY37Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d290294320.mp4?token=qOwo4gdaIJmISBKaGfhL9tiLpIxs5zBOdzGVLnoCHMeePg3qBz2PIYTqFl0nJleksfzyKpeOqZlnkcIOV99AehYkSCQRJUcuhqBgwT6GOrdaOERIFlZFGohuLZUOklbNsSn7JR4RMLb91wmAuGOb_5_RTqapp_03_FxWwyvL2yDdRknTP441zS66WqWMzSQZjk6K-46WapeWEp2nMaSk_NxXug-VeR7cJ2xuJdE97tcSQ84TVnt6OaWdVvlo8tGlek-3fUaBnaNHZncFK7LqaE63VGTc0TddCNjFNWdeEdEVmtf-2KeR6C99NyUbLgQCvsICrswpPMn5j7OlSuY37Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
اینترنشنال:پزشکیان و مجتبی خامنه ای باهم دیدار داشتن و این دیدار تو یه ماشین بوده
؛
مجتبی خامنه ای صندلی عقب ماشین نشسته و تو یک مکان نامعلوم و پزشکیان صندلی جلو نشسته و حق نداشته عقب رو نگاه کنه فقط صداش رو شنیده
.
پزشکیان از مکان هم بی خبر بود فقط برده بودن ببینه اونو.
پزشکیان قرار بود از فرماندهان سپاه از جمله وحیدی بهش اعتراض بکنه که زیاد در دولت دخالت میکنه.
مجتبی اجازه مذاکرات رو بهش میگه ولی با هماهنگی سپاه پاسداران.
پزشکیان کلی مشکلات اقتصادی رو بهش میگه و میگه که اینطور بره ورشکست میشه دولت.
پزشکیان از این دیدار خسته میشه و میگه میخام مجتبی رو ببینم ولی به هیچ وجه اجازه دیدن رو بهش نمیدن.
پزشکیان که فوقش یه ساعت میشد فقط صدا می‌شنید چهره ای از مجتبی ندیده بود.
پزشکیان اصلا از این کار رضایت پیدا نمیکنه وبه رئیس دفتر اعتراض میکنه.
میگه این کار جز خورد و حقیر کردن من نتیجه ای نداره .
بدجور عصبانی میشه و جلسه خیلی کوتاه تموم میشه.
تصمیم استعفا از این جلسه شروع میشه چون پزشکیان احساس میکنه دیگه قدرتی نداره توی اداره کشور.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69555" target="_blank">📅 09:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69554">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d7b56246.mp4?token=FPnQR6tHi9_OauIrIF6aLV0ZxQIgkocNvEabsrTh9CyR3knGFmVY1jYOnTo6NdiWFn-98Al1zu81QjyajiRWxQoaCZPvwP5HZ0emnIYJIh38N7mwNhXZmntx6FKvIsfryfMl_t716R3bx5JIak3Nf_Vdurbvh7MaMSScpvwYOakLsP4iHa575qYC4pMuf6tRGnxgDLdjA4Ep7NxM9l4ayKKMDiyrCHKLe75plInjdlRgH2B8VR295YUijuUR-Tn9nqlWXc6_uvb8LAe3zTf72xBWKEuTrchfQpKnoQgy5jb9u1HOzTHEp67Vjgu1HjhpI2tQMDiywMJXU9Az9A_sKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d7b56246.mp4?token=FPnQR6tHi9_OauIrIF6aLV0ZxQIgkocNvEabsrTh9CyR3knGFmVY1jYOnTo6NdiWFn-98Al1zu81QjyajiRWxQoaCZPvwP5HZ0emnIYJIh38N7mwNhXZmntx6FKvIsfryfMl_t716R3bx5JIak3Nf_Vdurbvh7MaMSScpvwYOakLsP4iHa575qYC4pMuf6tRGnxgDLdjA4Ep7NxM9l4ayKKMDiyrCHKLe75plInjdlRgH2B8VR295YUijuUR-Tn9nqlWXc6_uvb8LAe3zTf72xBWKEuTrchfQpKnoQgy5jb9u1HOzTHEp67Vjgu1HjhpI2tQMDiywMJXU9Az9A_sKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
بازم ترامپ از ترور جون سالم به در برد:
⏺
فاکس نیوز؛
مقامات اعلام کردند که یک مظنون مسلح به نام «جنین جان تائله»، ۳۸ ساله، در زمین گلف «ترامپ نشنال» دستگیر شده است؛ وی متهم است که پیش از سفر رئیس‌جمهور ترامپ، تدابیر امنیتی را زیر نظر داشته است.
پلیس اعلام کرد که متعاقباً از منزل این فرد، یک قبضه تفنگ مدل AR که به‌طور غیرقانونی تغییر یافته بود، جلیقه ضدگلوله، خشاب‌هایی با ظرفیت بالا، مهمات و دفترچه‌هایی حاوی «مطالب نگران‌کننده» کشف و ضبط کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69554" target="_blank">📅 02:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69553">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">#اختصاصی #فووووری
🚨
ملی‌پوش پر حاشیه در آستانه پرسپولیسی شدددددن  https://t.me/+FgpywJWoBXVmZGU0</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69553" target="_blank">📅 02:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69552">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v8GjKeDsmjXIxxnFEomLQ-5ykilfp_a4WJNOuAWdP4ngAIGHJEa0qn9za8M7x84s7oL2IlSu7tBjrrpDRPc_smDrH3TrezIqKVeX53XNdz3c05f14jfzDxxTfc73WJwBgXTFimdqZ0PlTi39if4ml8ed2PAFMcYhl4QeP33wAoxbSNkfIINRdsGaSHRv43Lzp6UwAFd4h2ELbfvScTj7pEe-k8VzaLQw7Q3sD6038gaQcyY5l9-IIMgIiDXmkddy9mYswHIGvk-QHBXxIG3lBG55YDXpKAlcrGPU8hWE38EX4cUtrnD1t10ELk1po6-3pkfIoBWeHAbnzA_1tZQ7dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و پرسپولیس هنوز هم شانس رسیدن به هم را دارند!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69552" target="_blank">📅 02:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69551">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjhTbHSzWrpmmcqdvLYpogz5smzlz4xVlqJArkjTZPcDxOk0AGcVth3XAUyPA_M94LfNyPLNZHG17AqZrJwW0gVWyZesVHOeoeIVjpK1mzgrcjm2fGN02eQ2-WyVSNy1lZY_0ZDsGrzMdQ9q1ZwZNq3hoaaBx3EgcuV_HZ1jTs-uvbunrsTv4PD44sXKOmmgYTGYhr7OghcHFehqGjulNt8rRJNJFdZRsr4TiI0BFinwaHGr3TSncbf-G1qZPTv7z0z_LlrmYcnck8ZFosvZjEdKWwV53D2euDaZxS09pZoE0sCemtNi9oGZywXtFLCHhvKQ-g5bKElrnHwrtxJPYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیزارم اینو یادتون بره
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69551" target="_blank">📅 02:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69548">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VSpbY4Bn7879deH84mNvbQG6eEY5xp8YLtbpWlTY_Y7i0cNlWwI0EgFY3lpPilI4TvtI1lG_zpIQOZfcl5Rg3iPuiGDHYUkJUZp02BJ1d81gCMUhhNmOFz5PO_aLy3_89wgxnnQFHe8FSjLjuXUD94qPcWGFOOeECLwlgtcCYsMaSRpsYH8VnPVR5iJZ4zk45vTD8xaEzRQ9lF49xb9GjEZ2j7GV9Yzl8XqvL1volnmbTLdiDJP6fmn2b4vfRzW097i75HRR87LCo-QeTTfeogAsgEq3kG-tQZGVaXHNY2dxhcu24vfWFoITJsQPBflWrGhzs2FLYl56z4Hp7mF3_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RI9qXqxAS-W5IjzCRJbc0VhJf0UkgZUBJFu_6KyEF93fBFENUWLTI2MfpMBom6UBOmkK8ZMYzGYjfl9H3hIwltjIftU7NxhPvqbbCSctnyUHvBsZawSEKOA4xOHp5MmgxSab01T1_cnkPm9Fi3X8qC5G6OjQnlnVN9GPY97dOm6MJnZX2iEFRoW0k6AmPFMfNh_lJXmD7rWweKfP2BabbUngtA-WeVjxkuuX_6ftpiM7H6ZcLTNqQio3JOVGeDUvNcsVNFuUUSzYg9rk8f9aruKdJu3SnZ6831cErQjxT__lp18asxCZPTQwrxJ_12l3Mr-csTWTTkeWdoSM6E9u5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d579f85e4e.mp4?token=XZHZ5NSTXUnyHX2TlNo-tRpdz0X2wV3wFRfosBHEFa1bGv059av2d7JtkR3yhaZ1ZVFxnJ8fJ153G1rAjDrDI8vvEYPI0_-jCsuG5_GoCqo3WhHCgNDDtJsicAs8fRL7Aoxu24svb8cQyxUejMAX7fSQt_CyPnAgSWLwTEnUCrvs6An8uBjrcTcjhe_TT6zhZQ5j6BJCBAB-ExW7tjPQCohAfa6Dj5RUDTrX5osXqdzjIw-pNKYngY2STstAmg2d2MnVSVDO1LY5XKSQxMbDlaPpGdQnvFonKfgrP-HPAqF1InK0Y9jS2uaA2vLWNJJKeuWEo4o1iAEJNFiFmgKxvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d579f85e4e.mp4?token=XZHZ5NSTXUnyHX2TlNo-tRpdz0X2wV3wFRfosBHEFa1bGv059av2d7JtkR3yhaZ1ZVFxnJ8fJ153G1rAjDrDI8vvEYPI0_-jCsuG5_GoCqo3WhHCgNDDtJsicAs8fRL7Aoxu24svb8cQyxUejMAX7fSQt_CyPnAgSWLwTEnUCrvs6An8uBjrcTcjhe_TT6zhZQ5j6BJCBAB-ExW7tjPQCohAfa6Dj5RUDTrX5osXqdzjIw-pNKYngY2STstAmg2d2MnVSVDO1LY5XKSQxMbDlaPpGdQnvFonKfgrP-HPAqF1InK0Y9jS2uaA2vLWNJJKeuWEo4o1iAEJNFiFmgKxvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
حملات شدید و سنگین روسیه به کی‌یف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69548" target="_blank">📅 01:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69547">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3uetkTOm1NqPWjDJQx-fwUkSg910lw7c9fr60zQYeIyURsaAfIh-3IX-S_bDwHcKonSK3mJvz8yqoH1xcdmubLqCGkzXFqx5NFY1Yq5JaESYklvzm9jpflZVlmSruPlK0Ww-2pVF8sXvNQLcXOHIhBPFytZWd4Kbh9zkVzbcc8jrO56mUzDmCZ5WsH0CGtjMEK3yXp3wJwlpEwX_DudlCFOiPLGNh0-YPnjIyZIsq89eeYRyLfXAmiP8FimFJokfElNzcMc8iBfeOJaUFltbZiIxk4ogOiXaiIP5Ygc0fkNoSNL2R-L4eUILI_PtxOebjVgbge64ikRNwNLig-83g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
علی قلهکی:به نظر میاد یکی از گره‌های اصلی مذاکرات ایران و آمریکا، ماجرای تردد کشتی‌ها توی تنگه هرمزه و هنوز سر جزئیاتش به توافق نرسیدن.
هنوز مشخص نیست کشتی‌ها دقیقاً از کدوم مسیر باید رد بشن و مسئول امنیت و هماهنگی عبورشون کیه.
ایران می‌خواد کشتی‌ها بیشتر از مسیر آب‌های خودش عبور کنن، اما آمریکا و طرف مقابل مسیر عمان رو ترجیح میدن.
اختلاف اصلی هم روی نحوه مدیریت، امنیت و کنترل تردد کشتی‌هاست.
هر اتفاقی توی تنگه هرمز می‌تونه روی روند مذاکرات هسته‌ای هم تاثیر مستقیم بذاره.
آخرین پیشنهادی مطرح شده مطلوب ایران اینه که کشتی ها حتما مسیر ورودشون، مسیر ایرانی(شمال)باشه و مسیر خروجشون حدود ۴۰٪ کشتی‌ها از مسیر ایران و حدود ۶۰٪ از مسیر عمان (جنوبی) عبور کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69547" target="_blank">📅 01:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69546">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKNadVKoMJvUOBHv1cdMsdv45_D4I4Db54hi7DvcmuqGrfz32sWoxNzS6yvCsvTXAhC_CWOo6lx9-xVZ3n21RYj81Ehpy_Ah2D7LixZ2aUpaXQ8u5ybZ-9Lk_4NtbpN8C-uVvZmlUXUozhUFWnzVcQlXpundYy8fHkvO_4W-sb2mnqurQQhzSpcC-ZUSXbpgC0DZwUdth5VaSatZsTd5nukTjt2qSntXShh8h8SfG5e2ie0a1tlbinczIFsh2lJe5xyVaXHiBlk0H71n36YuX4-H_Qa2IznzxoHDYolJK7h7bSmRnRZKKTtosE4dhIAXULB4G81dUFybIo21I8VauQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇺🇸
بازگشت غول‌های سوخت‌رسان؛ بزرگ‌ترین آرایش هوایی آمریکا از زمان جنگ خلیج فارس ۱۹۹۱.
پس از پایان جنگ جهانی دوم، جنگ خلیج فارس در سال ۱۹۹۱ با استقرار حدود ۳۰۲ فروند هواپیمای سوخت‌رسان، بزرگ‌ترین تجمع هواپیماهای سوخت‌رسان در یک عملیات نظامی به‌شمار می‌رود.
اکنون نیز در سال ۲۰۲۶، با استقرار حدود ۱۹۳ فروند هواپیمای سوخت‌رسان در منطقه برای پشتیبانی از عملیات علیه جمهوری اسلامی، یکی از بزرگ‌ترین تجمع‌های سوخت‌رسان‌های نظامی از زمان جنگ ۱۹۹۱ شکل گرفته است؛ آرایشی که در بیش از سه دهه اخیر کم‌سابقه بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69546" target="_blank">📅 01:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69545">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOtVA9SXgZTpcKpebpq70qLfnxzJA0h8cM3UwMLFDmmHJMuNOOidUGelnvwOrma2uzCU588e_i9WKNtoYTUiTwcLKeA5P56f13zUGf6KE_xQYa2FMf8QaCZUFFV3XBy4pvnkNYpM2tXkNu5hMBYvEVipIRD8O_rDXCZvMcMtalhZ0FiIdyCMK7K9AMK3-33r08MiJ40TtWZts1q9y1SYS0aQgrYPwkPFRoVfMLesjrAuXcLwf5qfWzHGLQyZJ3HfA0FSTzPEK_OKpmTnvPPTne8J17zTibrD4p-HWp69drIthbciroHkhDy5zp2PKDOVk5AGRefPn6HU87Z9QYCMgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام:مسیر جنوبی از طریق تنگه هرمز برای تمامی شناورهای تجاری که قصد عبور از این آبراه بین‌المللی را دارند، همچنان آزاد و باز است.
طی سه ماه گذشته، نیروهای آمریکایی علی‌رغم اقدامات خصمانه و بی‌دلیل ایران، به بیش از ۱۰۰۰ شناور برای عبور موفقیت‌آمیز از این تنگه کمک کرده‌اند و این ترددها همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69545" target="_blank">📅 00:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69544">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31eaaf6719.mp4?token=NF8r_k3izn7kM5-PnxUIThmfeLFPbBf2iVGbm0fgpNaG3doGaSXjaUkRvV2pDuUjYrWkBMcRFhgaoVOT5v299wDLbpK8q6xzH6TvgOYyQeEfcOfz3M4YYK1dzYsj1-VPcD73f5VYKKvN8RMJ1wARO4bQ7a0y1rzQAEGgPY0ddgE1j3tDt1_UEl6TgxgqlT7erpa-JbifGHHklzYb613MtGavgLEK5rWkY_ZXJsgHChyShbDT7WOkx11gGVz-R4MNCiL7giUMUfnhg9Rz5ATyd4MMMMvSmAEkC4Ktp0cobeAeiLt-AaY-3Ugg4VcoxE2L3DU6TRY8Xc-0pClAKzkgxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31eaaf6719.mp4?token=NF8r_k3izn7kM5-PnxUIThmfeLFPbBf2iVGbm0fgpNaG3doGaSXjaUkRvV2pDuUjYrWkBMcRFhgaoVOT5v299wDLbpK8q6xzH6TvgOYyQeEfcOfz3M4YYK1dzYsj1-VPcD73f5VYKKvN8RMJ1wARO4bQ7a0y1rzQAEGgPY0ddgE1j3tDt1_UEl6TgxgqlT7erpa-JbifGHHklzYb613MtGavgLEK5rWkY_ZXJsgHChyShbDT7WOkx11gGVz-R4MNCiL7giUMUfnhg9Rz5ATyd4MMMMvSmAEkC4Ktp0cobeAeiLt-AaY-3Ugg4VcoxE2L3DU6TRY8Xc-0pClAKzkgxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان:
اگر استعفا بدهم، رسماً اعلام می‌کنم؛ استعفا نخواهم داد و خواهم ایستاد
ما با نیروهای نظامی، کاملاً هماهنگ هستیم.
می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و این‌ها یک چیز دیگر.
همه مردم برای ایران سختی‌ها را تحمل می‌کنند.
یک عدد سه هزار نفری را سی چهل هزار نفر گفتن، نشان می‌دهد که این‌ها چقدر نامرد و وطن‌فروش هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69544" target="_blank">📅 00:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69541">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m_gC2XLxCRtHV6VKf56tbS3hkp5T4rVehUBvbOPAeHr2r0ibfPLz5vwzB4HIMYgcNbNNj6Hg9ptmzXdQqaiS_c18oF6HJrr_PpVTOxF9c_vJiqvuoeOM59bGSom2PrWMiRMYXfYVxm8ygiQpRzx4ZD9aNQGmoi6ZRCJDv2nEg6hxdooOYR0kPsBH1NTO7jnR7XB_dJv18o94Es9vvLUAP80PbMdOdnszLpgZOdjIe-AWg9THX9v-jhqeJocNZLeuw3MX7Nbkl7qDxOlEQUNMBZGN2oyFQ2w24hc5IZqpE7kOFfMAqS-2I9GwSIPkcXL2ybO-DzmmVKnzfWRyGv933A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDcAJj83dpyguPL4FBPAOZdgUndOQ6VsWc5tXXeClpHoRL-ycL05g82fyNe64mOCmGKKAd8ghKybSfIeFJmjjwOrSf5Ki25YREC-JnHpi2Vtvmz33g7Fvag2FIQ_oUDm7IwFoDisleN3u0xEH5DbwvkDM3x49lmU1AaHWhq-0EpB9W7jVkf3P-FzUES5ExCfJnwh0HJ9bEaT3RoyUzt5QiXRcYt53Rb-3Tao75xVzD0-_dHY1epjek4608ZL2pPr9AebwUglOk_Cr3n5YpNXGu4xfZan_cLFbeucQkPV61UXnhmkUDHFHzsiEDtE8jyHKT8OVnpzArlc8SYs8tw_sA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▪
🇺🇦
رونمایی اوکراین از ربات رزمی «Droid TW 40»
.
شرکت اوکراینی
DevDroid
از ربات زمینی تهاجمی
Droid TW 40
رونمایی کرد.
این سامانه با حداکثر سرعت
۱۳ کیلومتر بر ساعت
، برد عملیاتی
۵۰ تا ۷۰ کیلومتر
و ماژول رزمی
Wolly
مجهز به نارنجک‌انداز
Mk-19
کالیبر
۴۰ میلی‌متری
عرضه شده است.
برد مؤثر این ربات برای درگیری با اهداف
۱.۵ تا ۲ کیلومتر
اعلام شده و
Droid TW 40
می‌تواند در حالت آماده‌باش تا
۱۲۰ ساعت
در میدان نبرد باقی بماند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69541" target="_blank">📅 23:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69540">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rmu3CkjsoTkKY5L80YCUWMzsjlOpcnnxEXCSYkBtOKZvYmSaZxsXuau8KRdpkkrS3LEAilUVqGKER2wNy469z2o7DSDdxHXmYoRwi3Hbsi7DIV-nXwhPMJc_uu3MD28OCcBZuKUI-mvbzhU-Ruvh99bSzPZizTwfowiHlM96KTfPpzMj3RBquAzcrvHyGQopdSifsmzlZqWPCWSpovldkCTVIvPLF2Kb6PkIXEbut3DMVivjFXguoxem0y1eKUWhc6cdQDiRDfxPLiZui1ouAgPOOAqqhmRYXMbk-MMrF3AArIHnes_zi6Q9MWXsz1-BEK_WcmSdJN7o6QpBek2w4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
نقاشی وایرال شده از زمان قاجار:
در زمان قاجار زنان روی یک وسیله تاب مانند میشستن و یک زن قدرتمند، اونارو بالا و پایین میکرد.
شاه یا یکی از سران مملکت هم اون پایین دراز می‌کشیدن تا زن انقد روی آلتش فرود می آمد و بالا می‌رفت، تا ارضا میشد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69540" target="_blank">📅 22:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69539">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c9b5938d.mp4?token=LR7o__CGEpdk8LZwFIZde86ViWWzK7sPjXiY_89EImdWFfR2wM3ILdLOviL2EEsYk242ZW5asJ4jfu3IMdtILA_FiCxgXsQrHIzHrfLVQhn6uMK-8-sS2-Yqqgo8JtLynol3MUT-_HXpDxu9xUNdaTYnEoCaptMVGvGD15ijDowVRdvHfPrL6CcHGt64aWecyufNZzTOqgixiJmXhQhANj3qySRILRRINgpxBlwCE6OCCyX9qNE8uBZcOsx6G-bKe_NlzaOdFraDbb7pLBjBazR81cGaeHLVTyasdnX4cKP8I-GYqIOIqA_x18k62l-n2LjGEm0dHII7BUdSsclT9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c9b5938d.mp4?token=LR7o__CGEpdk8LZwFIZde86ViWWzK7sPjXiY_89EImdWFfR2wM3ILdLOviL2EEsYk242ZW5asJ4jfu3IMdtILA_FiCxgXsQrHIzHrfLVQhn6uMK-8-sS2-Yqqgo8JtLynol3MUT-_HXpDxu9xUNdaTYnEoCaptMVGvGD15ijDowVRdvHfPrL6CcHGt64aWecyufNZzTOqgixiJmXhQhANj3qySRILRRINgpxBlwCE6OCCyX9qNE8uBZcOsx6G-bKe_NlzaOdFraDbb7pLBjBazR81cGaeHLVTyasdnX4cKP8I-GYqIOIqA_x18k62l-n2LjGEm0dHII7BUdSsclT9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیو ای از یک پهباد روسی که یک شهروند اوکراین رو تهدید میکنه و در آخر هم خودشو میکوبه به طرف و منفجر میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69539" target="_blank">📅 22:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69538">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3447971507.mp4?token=ljBNS4rOPLqTPFgjA0yvu8l6-A3Os7nRYEvwUlgCIHCXqtXW96Qrci02mCdKv4YMG8UY-_Dqr_WQtB1XH2gw-k55M4G6xCIeN0aJQKdSylVGyy0JIN9h13gW4xMeYs-fjQvLXjy1Dck8wRPQBYM6HABDg0RHjLCHo2Zi4GgTbngBJhdeOgYbcF82C41IjF4ObM6ZZmFpLHP_9-kjtu-qN6dpFTh4Gtt_z1ryMo2hG2HUh-mgPwZ1wp5ayvICEZan6xj6beEQ8-55XhPru3Y-drHo4K_CEs5WQ8A-TjbuSEI7pSVRMKu9kaUO9Vayskaob0jtjXhaI2sxLL5NFI-_Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3447971507.mp4?token=ljBNS4rOPLqTPFgjA0yvu8l6-A3Os7nRYEvwUlgCIHCXqtXW96Qrci02mCdKv4YMG8UY-_Dqr_WQtB1XH2gw-k55M4G6xCIeN0aJQKdSylVGyy0JIN9h13gW4xMeYs-fjQvLXjy1Dck8wRPQBYM6HABDg0RHjLCHo2Zi4GgTbngBJhdeOgYbcF82C41IjF4ObM6ZZmFpLHP_9-kjtu-qN6dpFTh4Gtt_z1ryMo2hG2HUh-mgPwZ1wp5ayvICEZan6xj6beEQ8-55XhPru3Y-drHo4K_CEs5WQ8A-TjbuSEI7pSVRMKu9kaUO9Vayskaob0jtjXhaI2sxLL5NFI-_Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
چهار سال پیش در چنین روزی، یعنی ۴ اوت ۲۰۲۰، انفجار بندر بیروت — بزرگ‌ترین انفجار غیرهسته‌ای در تاریخ معاصر — پایتخت لبنان را ویران کرد.
هزاران تن نیترات آمونیوم که به‌شکل نامناسبی در آشیانه شماره ۱۲ انبار شده بود، دچار حریق و انفجار شد و موج انفجاری ویرانگر ایجاد کرد که چهره بیروت را در عرض چند ثانیه دگرگون ساخت.
این انفجار دست‌کم ۲۱۸ کشته و بیش از ۷۰۰۰ مجروح بر جای گذاشت، حدود ۳۰۰ هزار نفر را آواره کرد و خسارتی بالغ بر ۱۵ میلیارد دلار به بار آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69538" target="_blank">📅 21:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69537">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8eaaff36d.mp4?token=MXekHXz3KebBU53S8sr9JIg8LV_RbBzKuibwoxpVQC3PMiLR43GdOd7HLaZ-BI7mQ2hST_RSuZHOH4YhU2mGLGt5rGo89hHQJsjPn_wD_m0uTA4SseDJD5jH2MyDHGPG_E-aCSDcSpYM83x2SQ96mLh3x5sr_CLMzPNjYfpeAL88HUtvuoz_n4N_yF2sZ79DpWpD78kz54DbsXiOJsp7fMdLEpXATiMSIw7OxHQZh2IoySGP6EeO8IVthGFbCQIOIwzaeW9zo40gATXV6Deoh7MYGZM_NCJmPpmbLKAzqukA3gUKrVElConOyXR0SybKUhbdjdIdnkjrSBaonBaIfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8eaaff36d.mp4?token=MXekHXz3KebBU53S8sr9JIg8LV_RbBzKuibwoxpVQC3PMiLR43GdOd7HLaZ-BI7mQ2hST_RSuZHOH4YhU2mGLGt5rGo89hHQJsjPn_wD_m0uTA4SseDJD5jH2MyDHGPG_E-aCSDcSpYM83x2SQ96mLh3x5sr_CLMzPNjYfpeAL88HUtvuoz_n4N_yF2sZ79DpWpD78kz54DbsXiOJsp7fMdLEpXATiMSIw7OxHQZh2IoySGP6EeO8IVthGFbCQIOIwzaeW9zo40gATXV6Deoh7MYGZM_NCJmPpmbLKAzqukA3gUKrVElConOyXR0SybKUhbdjdIdnkjrSBaonBaIfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
ترامپ و تیمش تصور می‌کنند که می‌توانند حماس را به خلع سلاح و غیرنظامی‌سازی غزه وادار کنند.
آن‌ها پیش‌نویسی برای ما فرستادند که ما با آن موافقت نکردیم.
این پیش‌نویسِ ما نیست؛ ما نظرات خود را ارسال کردیم. ضمناً، ما نظراتمان را پیش از آنکه شاهد هیاهوی رسانه‌ای پیرامون این موضوع باشیم، ارائه داده بودیم. موضع ما همین است.
و ما بر سر منافع خود، هم با درایت و هم با قاطعیت، ایستادگی می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69537" target="_blank">📅 21:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69536">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hydD33UeOAhxWMN6FpstO4ycrURIKijsnkL4ol9snvtfYI24iD4UOBfbdcMjbqMN2LJLG97PAF1uYIOAhtM6EiIUm33YT4qBnglF9x6gzarMlCe3KRWEvMMgsRUIWPK9kbnyx08QXHe8WsokTYq6LIfXvguCJtHOaDb0LGeRzIw3MU6icLHXkrrEiFDJBSy8uKLS0ZWVe0KQ8mmZwiW7jA7UlA3y-aAGBYmTeCG-kiJpr4atFCHgD8lShLYpnR8KAz-8xCbpPEBF7ZeBWTC0PkkktiFdzEeo9sla2aJixmm-qht6O76bDmER0cs1P7idu1-7ViKTlbkA12tvSEnIhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
وال‌استریت ژورنال: در حالی که دولت ترامپ بر نزدیک بودن احتمال دستیابی به توافق تأکید داشت، وقوع حمله‌ای جدید به یک کشتی در حال عبور از تنگه هرمز و بروز اختلاف بر سر مسئله عوارض در جریان مذاکرات برای بازگشایی این آبراه، چشم‌انداز این کریدور حیاتی انرژی را با ابهام مواجه کرد.
به گفته میانجی‌گران منطقه‌ای، بر اساس پیشنهادی که هم‌اکنون در دست بررسی است، کشتی‌های عازم خلیج فارس از مسیر آب‌های ایران وارد می‌شوند، در حالی که شناورهای خروجی از خلیج بدون پرداخت عوارض از آب‌های عمان عبور خواهند کرد.
میانجی‌گران اظهار داشتند که اگرچه دیپلمات‌های ایرانی در ابتدا از این پیشنهاد استقبال کردند (زیرا تا حدی کنترل بر تنگه را حفظ می‌کرد)، اما تهران خواستار حق دریافت عوارض ــ که احتمالاً با عمان تقسیم شود ــ و همچنین دریافت تضمین‌هایی در برابر حملات مجدد، پایان محاصره دریایی آمریکا و کاهش تحریم‌های نفتی شده است.
مقامات ارشد منطقه‌ای اعلام کردند که آمریکا و دولت‌های منطقه با درخواست دریافت عوارض مخالفت کرده و خواهان تضمین‌هایی هستند مبنی بر اینکه ایران و نیروهای نیابتی‌اش، قلمرو آن‌ها را تهدید نخواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69536" target="_blank">📅 21:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69535">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtTBqr9Y7cJXGgnVFOy8H_sdB1-MaofDDq0z1SwI483rFyFyZyGAeGjC_d5p84ZkzcHdEGScrn-WzoPYHlFBthgEB0nXQPZuKkqCw5ZJ4eWeuAFPfzWUkDONwYtVTlHjqHYjrVJII7ScgQZZUWW10aH3KabXyAAmlCxclaKUdNbmqJJSP9bjqimh1jErv5tBkbsGX0dZFLoaSqYc1qZvfaQOYuI27pJNbhqD_J22mafhFP75zdSTpOVQz8gu66UStk3a5UkuSH5ZMM3ZP-A_1WGuqtkvzJOvyqGvAx-RJKTKUT4lT--Vl1EzzWLCIaUeXZ1TDre6SzwB7XwEciiGYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام:یک ملوان نیروی دریایی ایالات متحده در «مرکز اطلاعات رزمی» ناو «یو‌اس‌اس باکسر» (LHD 4) مشغول نگهبانی است؛
😃
این ناو تهاجمی-آبی‌خاکی در حالی که از محاصره اعمال‌شده توسط آمریکا علیه ایران پشتیبانی می‌کند، در آب‌های منطقه در حال حرکت است.
تا تاریخ ۴ اوت، نیروهای آمریکایی مسیر ۴۵ کشتی تجاری را تغییر داده، ۲ کشتی را از کار انداخته و برای اطمینان از رعایت مقررات، وارد ۲ کشتی دیگر شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69535" target="_blank">📅 21:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69534">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19c9ea7021.mp4?token=YXUIqEmlANW7R3PJ0uO_mxc_NEmurAiBX_VKsJTAVwi6wv1RFs1NcBYFVFzflsATgT3t87ovmoVvq3aGV5plrmiyuOwCgE0KIvlT5MQ7vgXjp0yjOT-q7EkR5jGOphrmq5nLCR1selLQDb7RsRHS-ds6iQvmTrRKKuEhXRbIMZnxz5dr9uRosJ_XMtvZUOuhWdhDFFvsUi0I8s4mwoRgUQGw_Z0t6z1nMmo-wXF8DEsxhjkeXn2uMM7MYYTr3taODhpgPieBR-ywwt6qsQukviqXpyNSErc767XclgNncwqH_FzMAZxZRNDWc-52Sk7Yuq_hNOdlN1FhSZKYLKBCrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19c9ea7021.mp4?token=YXUIqEmlANW7R3PJ0uO_mxc_NEmurAiBX_VKsJTAVwi6wv1RFs1NcBYFVFzflsATgT3t87ovmoVvq3aGV5plrmiyuOwCgE0KIvlT5MQ7vgXjp0yjOT-q7EkR5jGOphrmq5nLCR1selLQDb7RsRHS-ds6iQvmTrRKKuEhXRbIMZnxz5dr9uRosJ_XMtvZUOuhWdhDFFvsUi0I8s4mwoRgUQGw_Z0t6z1nMmo-wXF8DEsxhjkeXn2uMM7MYYTr3taODhpgPieBR-ywwt6qsQukviqXpyNSErc767XclgNncwqH_FzMAZxZRNDWc-52Sk7Yuq_hNOdlN1FhSZKYLKBCrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام:
یک جنگنده رادارگریز F-22 نیروی هوایی ایالات متحده در آسمان خاورمیانه از یک هواپیمای سوخت‌رسان KC-135 Stratotanker سوخت دریافت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69534" target="_blank">📅 20:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69533">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkDjNG6otkfmSas_QlCms_u1i-n2JRwDWJIN6bZyB4-yWOHnskRa2DHSbtaOTzN8p-5WOGYuBlWvuJb2qnFqTUjpjBbaKOFiOTl3nwha9f9WQHdCljKtdV2cWr8myCIoaxCcf9C5gbxiDjD0PZxyudLTdsIoxlZ_RRMc3QsgRgYPfvB3xpDcB7JcebX46FWeeOMwFvscnm9DBSt8hSXLPcFZvWlu6UuEgt-I9DZYB7hb0cA05D5edOHZb7WYz7NqfTcgH4Wn-3HWgCKiwbY0_iHAaA0ytKgqLnMzjhThh_QVegaXjtTjfzu96RDQ6GQir4l_NZI2nyGA4xRp4FH8DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
بلومبرگ:
ایران در حال بررسی امکان مشارکت کشورهای اروپایی در عملیات مین‌روبی در تنگه هرمز است؛ اقدامی که نشان‌دهنده احتمال تعدیل موضع پیشین این کشور بوده و می‌تواند به تلاش‌ها برای ازسرگیری کشتیرانی و پیشبرد مذاکرات با ایالات متحده کمک کند.
تهران پیش‌تر به‌طور علنی با هرگونه نقش‌آفرینی خارجی در مین‌روبی این آبراه راهبردی مخالفت کرده بود، اما در هفته‌های اخیر و در چارچوب گفتگوهای گسترده‌تر پیرامون عادی‌سازی تردد دریایی و کاهش تنش‌ها، انعطاف‌پذیری بیشتری از خود نشان داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69533" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69532">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3030125dc6.mp4?token=FM-RQ_P8fV3ByFuw3HcJdWpMfjqYfOkaD1kotXdIVw0Ks-l6VaA-nXgArmqY0bCNdxIeGpf9ewSzGYeJ_yBnqzcdIrFuSZXjrF7LjOiElKJemuy2iGMwGH6hhNc9Su3uqDGPbVFNQ2Bv8nhTAOp-h9StjVx3NxpxTaWlwXSQ43cOIZM8HUh72-_lh-1bZcEHACsDMxke3ZQanKmo7KJocVRpUxrS0sGrtDPdV-4E6z-WwB7xGdedrEbEN1KuGAz55rEZrZKVlzF5YUgltvwMe9oB_w1n7a3nAxNTXky0NCq3JcNoAHsL1b_mcoellbJ0C5xlXE2ZHZl34sCCEeqoHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3030125dc6.mp4?token=FM-RQ_P8fV3ByFuw3HcJdWpMfjqYfOkaD1kotXdIVw0Ks-l6VaA-nXgArmqY0bCNdxIeGpf9ewSzGYeJ_yBnqzcdIrFuSZXjrF7LjOiElKJemuy2iGMwGH6hhNc9Su3uqDGPbVFNQ2Bv8nhTAOp-h9StjVx3NxpxTaWlwXSQ43cOIZM8HUh72-_lh-1bZcEHACsDMxke3ZQanKmo7KJocVRpUxrS0sGrtDPdV-4E6z-WwB7xGdedrEbEN1KuGAz55rEZrZKVlzF5YUgltvwMe9oB_w1n7a3nAxNTXky0NCq3JcNoAHsL1b_mcoellbJ0C5xlXE2ZHZl34sCCEeqoHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حسن عباسی:
زیر جزایر و سواحل تونل‌های موشکی متعددی با امکانات متروسازی شهرداری تهران ساخته شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69532" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69531">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتبلیغات</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBE-WMpuuPmUPuy2wmajzGMitkB7B1m_0S0OYCiwdXVqUpBtF1kihEYoknEaY7DrqYOqp9zg2oUQNNMg3tcCzgFHq_-Csuak0cH4Gsu_G_ZJidtqbMDM-SQgYGZP7wNOB_xpgZYuy2MrZ8yYgVYPfiHlkS3__crWt677nFAdceXWDglhy_JArPfD8mUssLbu3UFqXzB1Ywn-K5LEReKbtBpXh4dHtDAq1l2fs2jypFy95eEjMFPR4oiMZiKhatPZqr1xP-IiIqf6Xfh6tirPEynaqBVx5bOgwjtLTrHjfDE4T8zS2xvBSBPk24ii9SvzxN3asViRjVTALH31l1Shtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
این حساب دوستمه تو ۱ ساعت ٣٥ دلار یعنی ۷ میلیون در اورد
🥇
گفت یه روش که با گوشی انجام میشه
💎
۹ دقیقه اموزش میبینی سرمايه اوليه ام نميخواد تا ریسک نکنی
🚨
بعد ۹ دقیقه میتونی روزی ۳ ۴ میلیون با گوشی در بیاری
رو لینک ثبت نام فوری بزن اموزش ببین
⬇️
⬇️
⬇️
🆓
ثبت نام فوری
🆓</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69531" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69530">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca94237dda.mp4?token=G9Vr5L9z-FlvoMBulbWG9arRTYlzBrD0s2OqgrX8x-8a3wApdrR06dZbAfJho-dDuTH-4QGW8KS-NKaTNly-k3HeUYKoDfaNRZpoJDFZIwzIZNx6YprJDBOQba7TKDlE4atybL1RROfjZV6cDm6UIK2ONjug9yv-9NIpwIa_rxF06LLU099tEV2ahPKCBKGQ9_ZPioerif-MBLCCVHPLFmvQuwhh5t32ROZolU1tF1xjnMfofiacpPLtBi2mEZWDIaTxswgY9ckTm0y-psvWuUU4dVFdFMOYf2unP9JYqB4vkAMuK2oDOQUz_dnbxVxPSHgiMC1g-vtc-i5U-MyKHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca94237dda.mp4?token=G9Vr5L9z-FlvoMBulbWG9arRTYlzBrD0s2OqgrX8x-8a3wApdrR06dZbAfJho-dDuTH-4QGW8KS-NKaTNly-k3HeUYKoDfaNRZpoJDFZIwzIZNx6YprJDBOQba7TKDlE4atybL1RROfjZV6cDm6UIK2ONjug9yv-9NIpwIa_rxF06LLU099tEV2ahPKCBKGQ9_ZPioerif-MBLCCVHPLFmvQuwhh5t32ROZolU1tF1xjnMfofiacpPLtBi2mEZWDIaTxswgY9ckTm0y-psvWuUU4dVFdFMOYf2unP9JYqB4vkAMuK2oDOQUz_dnbxVxPSHgiMC1g-vtc-i5U-MyKHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
غنی‌سازی اورانیوم چطور انجام میشه؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69530" target="_blank">📅 19:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69529">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mebrboGxXUzRngWsc4Oj3M4WyhIZReaKYp8w8-tzIGaUOUnIwc-qzpo5KLB3mKFXnsZCLzbY3Yz-SCTXbFMDtgIOdE6y1nnDxlf8ds76WcoU1GokInunxHT4I0vRUD-iT6vM_enisnQyGlvchTAGiAk7xBqAOiN-70bzV9wHvwj-GsY1dDyf40D7UBAxOkK3TKD3B8AmHn1dnlAGkT2A5b5D0z-hNE2LqHpGKLztt9u83_3JDj-VwC1sFwM8R6eJpnQrV6ayJW9H_BGII5Lyjw59JtFKkOA2-TvOoL97M4QI3ZiJIhX9y5J96rGR4hcyp3-m59w6HlHNrVJh6POLTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
"توافق قریب الوقوع است" با از سرگیری مذاکرات با ایران درباره خلع سلاح هسته‌ای و تنگه هرمز.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69529" target="_blank">📅 18:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69528">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو، وزیر امور خارجه درباره ایران:  کشتی‌هایی در حال عبور از تنگه هستند. هم‌اکنون نفت از طریق این تنگه در حال جابه‌جایی است. تنگه باز است. ما درگیر گفتگو و مذاکراتی میان عمان و ایران هستیم؛ موضوع این گفتگوها آن است که چگونه می‌توانیم در کوتاه‌مدت…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69528" target="_blank">📅 18:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69527">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1eaa69fa8.mp4?token=OT4zhjbxqyJNWX1fNFNgtNoHLYyG8LmEwB6WH7fKVUyRZJuY7e7jWgnXzQjdioKFnmqRI72PLaNPvh50q6c-y4aU-pB8uQN7JsEzPs4GXSm_mbdhQL6pGo0qduaLoQavixBJFP1uHaFHKse5_5iqOiwBuNCKx75vogvn5wO3dGzut-IqQYlcqTCxucAt2dEBcnD-DwwfFYg6-tWh2a3S4ERiSJh6W4TJhlbdRpdnms_AynyllKdFaoRwIWNtq1s_6ucsKp2ruZ6_5CkhJ357t4nT4-3hMNTR-d5SiIkmAbAqadiaD8Wn4iE5QsNwibZMFWw_wK9u_-G2L8UoZrLHyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1eaa69fa8.mp4?token=OT4zhjbxqyJNWX1fNFNgtNoHLYyG8LmEwB6WH7fKVUyRZJuY7e7jWgnXzQjdioKFnmqRI72PLaNPvh50q6c-y4aU-pB8uQN7JsEzPs4GXSm_mbdhQL6pGo0qduaLoQavixBJFP1uHaFHKse5_5iqOiwBuNCKx75vogvn5wO3dGzut-IqQYlcqTCxucAt2dEBcnD-DwwfFYg6-tWh2a3S4ERiSJh6W4TJhlbdRpdnms_AynyllKdFaoRwIWNtq1s_6ucsKp2ruZ6_5CkhJ357t4nT4-3hMNTR-d5SiIkmAbAqadiaD8Wn4iE5QsNwibZMFWw_wK9u_-G2L8UoZrLHyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو، وزیر امور خارجه درباره ایران:
کشتی‌هایی در حال عبور از تنگه هستند.
هم‌اکنون نفت از طریق این تنگه در حال جابه‌جایی است.
تنگه باز است.
ما درگیر گفتگو و مذاکراتی میان عمان و ایران هستیم؛ موضوع این گفتگوها آن است که چگونه می‌توانیم در کوتاه‌مدت و هم‌زمان با حرکت به سوی مذاکرات بلندمدت‌تر پیرامون خلع سلاح هسته‌ای، امکان عبور ایمن تعداد بیشتری از کشتی‌ها از تنگه هرمز را فراهم کنیم.
در مذاکرات برای بازگشایی تنگه پیشرفت‌هایی حاصل شده، اما هنوز توافق نهایی صورت نگرفته است.
ما امیدواریم که این توافق به‌زودی نهایی شود
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69527" target="_blank">📅 17:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69526">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78294ca69a.mp4?token=kdyhnAcJqv-CIu1oIqVLpyGY5hrCejV9TY5pR3fY6KJ8PuylIQLxQWLIHyEMvdae7BClnn9h7vi4yz9OjzBwsVkAYOtERD_0v7UZfWx-MdJ-k35MhwuiT4uKFxaawtqhC_jdJGxH6RNY2u7Veow85XJ5QhZ2yytYRctC1eSJlrzVHM-WN4GtYWRgr2tZakdbizUJwDpj-RKFS6qJSfhIjChaKSHNs3UafwTGif7xEiqKJqmK1L5Nd6ZswL2G0IXLDisnNcxI3Lz9uQrLz-AwIMTqybLWTrCErQm5julbJddeGvxcUqZb_moG3-Ww9tiNRpqiCCespMX3ZmEBhHTOtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78294ca69a.mp4?token=kdyhnAcJqv-CIu1oIqVLpyGY5hrCejV9TY5pR3fY6KJ8PuylIQLxQWLIHyEMvdae7BClnn9h7vi4yz9OjzBwsVkAYOtERD_0v7UZfWx-MdJ-k35MhwuiT4uKFxaawtqhC_jdJGxH6RNY2u7Veow85XJ5QhZ2yytYRctC1eSJlrzVHM-WN4GtYWRgr2tZakdbizUJwDpj-RKFS6qJSfhIjChaKSHNs3UafwTGif7xEiqKJqmK1L5Nd6ZswL2G0IXLDisnNcxI3Lz9uQrLz-AwIMTqybLWTrCErQm5julbJddeGvxcUqZb_moG3-Ww9tiNRpqiCCespMX3ZmEBhHTOtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو پاکستان، یه تجمع ضد جنگ برگزار شده بود که وسطش یه گروه جنگی اومدن انتحاری زدن در رفتن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69526" target="_blank">📅 17:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69524">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57327c22c5.mp4?token=E6LKi0P4ARTO9yLJ1OK_G5190KvNfS6Kb5fRp56Fg6AWNpounoTvlDd67Vwf_cQqLRLPwCk0lULquxg6XrwKec1kAZPUMkdZDF0Pwrw_gTgJSlws1F3mYZoMD4iOIDEhoTgR8S8AIeVFs3ILJct4XOvmUdMn93bGC8HshK1r6YAWMeodM29OegnQnO0COVBQut0O54TZiUQ7BhNQedpyTk9Dd7hv-wT7InbaTm06AukKNaCVwczHyjFYQNbx-MavHQXgXicUlu4bOaiOvMYT-dH1zSDcm5xuMgR4HB_T54nT4Eex5ZWa1dhbf_nC7auSohSUoGBj76dWuWE_leIBoKNpTi4trur1H7GqBMVHE_4vdPnVP8w0f_jlMCq28p0B1lyYd539JpCLznIE9DKECIS1Rbwmfsfri2Nod6xV3zrHkE_a-wB-6WqQoH9ybwapmIEa0pIJcqgb6x4LOJuXXHrUl69HlhyeZBAY3Hr60FPOHS0y5U4K39QVsSlrIFQXTbqhFf3VFqvprPUi8B8a2BRVWUnnppdaT8d8CfY5aHkGfK6ntsVgRcNyBhwFcz9-617d6E3QSuGiQjBEI6k2mA5VMncSL6c4uBgaZ8CdB0Wt_FTR0R4AZmA5zD5PCYZQOwuonUMc9xfXXyuZp13MD0IplO7A_VCURY9w2tQUprw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57327c22c5.mp4?token=E6LKi0P4ARTO9yLJ1OK_G5190KvNfS6Kb5fRp56Fg6AWNpounoTvlDd67Vwf_cQqLRLPwCk0lULquxg6XrwKec1kAZPUMkdZDF0Pwrw_gTgJSlws1F3mYZoMD4iOIDEhoTgR8S8AIeVFs3ILJct4XOvmUdMn93bGC8HshK1r6YAWMeodM29OegnQnO0COVBQut0O54TZiUQ7BhNQedpyTk9Dd7hv-wT7InbaTm06AukKNaCVwczHyjFYQNbx-MavHQXgXicUlu4bOaiOvMYT-dH1zSDcm5xuMgR4HB_T54nT4Eex5ZWa1dhbf_nC7auSohSUoGBj76dWuWE_leIBoKNpTi4trur1H7GqBMVHE_4vdPnVP8w0f_jlMCq28p0B1lyYd539JpCLznIE9DKECIS1Rbwmfsfri2Nod6xV3zrHkE_a-wB-6WqQoH9ybwapmIEa0pIJcqgb6x4LOJuXXHrUl69HlhyeZBAY3Hr60FPOHS0y5U4K39QVsSlrIFQXTbqhFf3VFqvprPUi8B8a2BRVWUnnppdaT8d8CfY5aHkGfK6ntsVgRcNyBhwFcz9-617d6E3QSuGiQjBEI6k2mA5VMncSL6c4uBgaZ8CdB0Wt_FTR0R4AZmA5zD5PCYZQOwuonUMc9xfXXyuZp13MD0IplO7A_VCURY9w2tQUprw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی به انباری از Wildberries در منطقه کراسنی بور در منطقه لنینگراد روسیه حمله کردند.
انبار اکنون در شعله‌های آتش فرو رفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69524" target="_blank">📅 16:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69523">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/523118296c.mp4?token=u38wBvkBxqe_XUcVqM2wzuZCdfY6hpbst1UAF6MAkmr7venZOrzx1bWULhp_xqFXWS6byewKwxy1XLGBsz7QnX8aM31W2mZx-KifXEu5zEWWfMGEOowEEaW0gx-CqyB4yXv9JcYko2zty7lA6f0ECDAn8VKq7C2UyH3v18O6QnQ8KDudPQB-90faTQ3XPTODuIjATfmruqXrToDOaoY7y2mabS4M-3UpermqWZSTmAVTiULJQH6NbmVvNlJ6NyukqzQsNjmNR7Lni1J9toyUDqducVt55fpv8Z-RDvM6jZlGBI9_tVEft2hTNegy4fompz87DSWPyrN7SdFbTzAt8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/523118296c.mp4?token=u38wBvkBxqe_XUcVqM2wzuZCdfY6hpbst1UAF6MAkmr7venZOrzx1bWULhp_xqFXWS6byewKwxy1XLGBsz7QnX8aM31W2mZx-KifXEu5zEWWfMGEOowEEaW0gx-CqyB4yXv9JcYko2zty7lA6f0ECDAn8VKq7C2UyH3v18O6QnQ8KDudPQB-90faTQ3XPTODuIjATfmruqXrToDOaoY7y2mabS4M-3UpermqWZSTmAVTiULJQH6NbmVvNlJ6NyukqzQsNjmNR7Lni1J9toyUDqducVt55fpv8Z-RDvM6jZlGBI9_tVEft2hTNegy4fompz87DSWPyrN7SdFbTzAt8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی:
خرازی برادر همسر مسعود خامنه‌ای افشا کرد مجتبی از استعفا های پیاپی پزشکیان خسته شده بشدت و در صورت تکرار اونو برکنار میکنه.
این اظهارات نشون میده جنگ قدرت بی سابقه توی باند های مختلف سیاسی امنیتی رژیم بالا گرفته.
بحران بدجور یقه جمهوری اسلامی رو گرفته.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69523" target="_blank">📅 16:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69522">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/800e043d01.mp4?token=N3G-cqQ7mfae7aJ-r4SFd2kX3AW-guCbfyj-frANFMnX7Go567tGcWftg0Isl6o5VdA1PnMdUUvPCRJ4QXk_aJbN9_7o4f6hBPzTZgFRvahP_9sXnx7fcYMFqFOtbwCOAONsL_sbioleJbUtrz-A9F4-6nJhqnmxoNCG0ujikKGC-hQG2UY_gNXkmDtUBBRbed04nQtOjaRU8J5BF-WY1qoOxuC1TJqQlA4nJx3OKzwrDDQGu-gtXCIhntq0bxKP3O-gK_t9cLl_TQ12M_gGlgPM4MKqLyfG7vD8HkCK5oU-Wvq70yek042pIrNr_B2XKLKVFcX1bGXJxVkv-3_Xqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/800e043d01.mp4?token=N3G-cqQ7mfae7aJ-r4SFd2kX3AW-guCbfyj-frANFMnX7Go567tGcWftg0Isl6o5VdA1PnMdUUvPCRJ4QXk_aJbN9_7o4f6hBPzTZgFRvahP_9sXnx7fcYMFqFOtbwCOAONsL_sbioleJbUtrz-A9F4-6nJhqnmxoNCG0ujikKGC-hQG2UY_gNXkmDtUBBRbed04nQtOjaRU8J5BF-WY1qoOxuC1TJqQlA4nJx3OKzwrDDQGu-gtXCIhntq0bxKP3O-gK_t9cLl_TQ12M_gGlgPM4MKqLyfG7vD8HkCK5oU-Wvq70yek042pIrNr_B2XKLKVFcX1bGXJxVkv-3_Xqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
محمدباقر خرازی درباره بمب اتم:
«در اقیانوس اطلس بمب بزنیم و سونامی ایجاد کنیم که موجش به سواحل آمریکا برسه!
تنها راه حل نجات ما ساخت بمب اتم و شلیک آن است!
«با اطلاع»! میگم ایناهایی که با بمب اتم مخالفت کردن اون دنیا در عذابند»
وقتی ازش پرسیدن که حاجی زاده گفته ما بهتر از بمب اتم رو داریم گفت: «جدی نگیرید این حرفها را»
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69522" target="_blank">📅 15:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69521">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXMkwvwuoXnsmVJNtX12EZdOXjrTkUraWa7yqCMiLVlKpYksZbf1nDiSkWsSeHuqK0GnJQ1WLUtRoRyZf3G9DlY_xtfj2ib2xSlmB8g4DtAJYTyFUwG3vbYcKoaBvWF4B4f7-p7CZRK0ggT64KF6-PTlZvKStyEWn2Sex7C5WfzK5bIC6_MI493bHM3SOQzWzZr2cAjoDnscY1iY5LUe1GtHxd6pl7sTVximOB2N61u8BPD4pNbhBJHiKL5pDJb5jSzpmE35uEcWk8kR2DqDwxTyS06OFjh9ybN_rNAk8y90NJz7zaESyCRqwHGITO_CfVScHHuX_1G4rAuLDOvf9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
بلومبرگ:
ترامپ به ایران مهلت داده است تا سه‌شنبه با عمان در مورد تنگه هرمز به توافق برسد، در غیر این صورت با حملات هوایی ویرانگر به این کشور روبرو خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69521" target="_blank">📅 14:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69520">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🇺🇸
🇶🇦
🇮🇷
سخنگوی وزارت خارجه قطر:
تلاش‌ها برای دستیابی به یک راه‌حل کوتاه‌مدت میان ایالات متحده و ایران در جریان است و متن توافق احتمالی نیز تدوین شده است.
این پیش‌نویس هم‌اکنون میان طرفین در حال تبادل و بررسی است، اما هنوز دستور کار مشخصی برای مذاکرات مستقیم میان آمریکا و ایران تعیین نشده است.
تمرکز دیپلماتیکِ فوری، حل‌وفصل تمام اختلافات عمده نیست، بلکه هدف، دستیابی به کاهش تنش در کوتاه‌مدت است که بتواند راه را برای ازسرگیری مذاکرات هموار سازد.
برای بازارها، این تحول سیگنالی مثبت محسوب می‌شود؛ چرا که هرگونه توافقی می‌تواند خطر تشدید درگیری‌های نظامی را کاهش دهد، از تنش‌ها در تنگه هرمز بکاهد و فشار بر بازار نفت را تعدیل کند.
با این حال، همچنان باید جانب احتیاط را رعایت کرد: اگرچه پیش‌نویسی وجود دارد، اما هنوز مشخص نیست که آیا واشنگتن و تهران هر دو آن را خواهند پذیرفت یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69520" target="_blank">📅 14:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69519">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xwxy1J_aBiF0kjfamd5deitK1gYHfqXyRfghP2RejlncWlk6qExc1dSbT9-NM-OKW0X3dZnIeuMJfEclOOGYEXaWINHKkykT95Zv3L_NEvIo1fKriKpvt4bxp_Dnx3ZUrNT8mED9gP5K67FVa874o_rQDSaJm3Zg2ryTRoPjv9Q0nP-jitKrCOzlz8_N6MCiuXIwLgfeOmNi1FrL8IH9NXt274WpdT8KW5v2p0b3Tsgsx8yV0JaCEnwVq1ST1DOwE46--uGf7K34FFoAIwDXdA4IuFAZU7dlBv59LhDB-sMppj3LgwgO9PirGUby6z6OPEYtfI1tcR2ipEV6_gBpAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
هیئت مدیره شهرک صنعتی شمس آباد:
دقایقی پیش یه مخزن گاز توی یه کارخونه منفجر شد و باعث صدای انفجار، دود و آتش سوزی شد.
هیچ حمله‌ای صورت نگرفته و مردم نگران نباشن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69519" target="_blank">📅 13:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69518">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8fbdc7b7.mp4?token=WhrJj2L_J6UvFSPrNN7vexVyE6ZsFMHREAEbYmoM47J6V7ScuJkBIpQ5YTwk1ytXpTP-sHvm8xq_JNtoDLQ51_dbBb-rXni8z0KFby-kHCxzyKNSyFFtQPU94J-T4ka0roOd7a1SZGaa46I6Nj7nChAQxdRihKp-LkF5_bwbFSwFkCdyTHqMwNvuWNVDaat4wHXMmJQDCCpXh57azrUBD4UlAiZRlZMbhn66jRmkuRD7AnoO57mutl9MUVjOBT1dNks12tGhaaQ75Zg8cJF9zXcV6Nsrl_gEjoxvHh-VTiE1lsWtGrQR2Kw_dTRBpQ_9Fh2nUDUJrvOWtQ07OasDHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8fbdc7b7.mp4?token=WhrJj2L_J6UvFSPrNN7vexVyE6ZsFMHREAEbYmoM47J6V7ScuJkBIpQ5YTwk1ytXpTP-sHvm8xq_JNtoDLQ51_dbBb-rXni8z0KFby-kHCxzyKNSyFFtQPU94J-T4ka0roOd7a1SZGaa46I6Nj7nChAQxdRihKp-LkF5_bwbFSwFkCdyTHqMwNvuWNVDaat4wHXMmJQDCCpXh57azrUBD4UlAiZRlZMbhn66jRmkuRD7AnoO57mutl9MUVjOBT1dNks12tGhaaQ75Zg8cJF9zXcV6Nsrl_gEjoxvHh-VTiE1lsWtGrQR2Kw_dTRBpQ_9Fh2nUDUJrvOWtQ07OasDHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
تهران
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69518" target="_blank">📅 13:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69517">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⏺
یک مقام ارشد ایرانی به رویترز:
طرح پیشنهادی تهران به عمان در خصوص تنگه هرمز، اختیار کامل بر تمامی تردد دریایی ورودی را به ایران واگذار می‌کند.
علاوه بر این، بر اساس سازوکار پیشنهادی، عمان تنها پس از اطلاع‌رسانی به مقامات ایرانی اجازه عبور به کشتی‌های خروجی را خواهد داد؛ امری که تضمین می‌کند تهران همچنان بر وضعیت نظارت داشته و امکان مداخله را حفظ کند.
این مقام ارشد اظهار داشت که بعید است ایران جایگزینی برای این توافق جهت بازگشایی تنگه هرمز را بپذیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69517" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69516">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pk0I42hnwNEG_gZDUOom7h-Ie_GjSLYblTXfH1ceTo4nq8m6WjRAhF-gpmhCMyq8SvYjM38d1qSDJE-mrqZx4ZeoSJtULaf2f-Bx49IlUcGw4vGOaDClI-OfACWnIVi-avhq-MsG0rsNql-mtzOZvwPnArG1VET_6HO2rzdGUQqZgSXLXPC4AAdkW7FVI9kOluc2pkQIxYXFUBgbDodeTf-TkQBk6fU4WaiHXQNFLzWLST36CohmWZJ6zudUBhFPY_BQ4wyPXy1SSZ-Onf4Bnnx7ckYDptvhhoWuWvlm4X19AxtTofmPTSxiwJkWZVnSaWiSlUY3zlYX6JdDIHsVHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69516" target="_blank">📅 13:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69512">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HskDNwaO2MRYcaWFlsMvtNO960P0pEQNBt7WSWAqlAHZS7lmwRbDsjxB9VzHBQVRgIkVBA1VAr89KCB_hjXxQCzsicForlBGe1MoORNvJcQrDyCExP2ewlrClU8jDsk3FR2UZnrKGkkxnmfWq0v3X1ZazX1BMRpM5SRcwaKuH5AG786yJ5Oh7XGvQ6xvvBIVnMkE16Qb7IJqHvZiXUCaNjl4E6a4SOd-VvFYbf2YQZU2Xy_Gu54I_HE5ivZRwZn0GyKggNd0xD-s8bWdab6z16JwhrEhVymO6slrhWJ-rJK-IXrk58Ajg_UdkBSe8jwP_rzs9PiEwdddjHmWqO7mUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r7FVs0SDx7LcC9WuyDELr9pQs82EPOaBIIbE20Kybv1KTMFs_JjSZoKbwhAfHd493OqUtwoGMYHfz4ni6ETsuWd_kpt6ibWwery-YM1_ubGSlmQF32VxSVBv5n219dn6hANsr6RB_G8LfxNjPL5PjIbbvSBJK1pKGfTTsjsr349z4u4ytJ-VLevVEtVRkO6C0UZ39D93TDrspCwooz4aunpX7zgh-y2EG70_ACQ8QTqf3GzIoRxl0rR1rp5zA_ROFY8_t50lA_1WreZ2IKxoTttOO-z4qhXptZgaENOgzn02fy2kVMVbcTY0sJtDo86lY12Yhf8YkESZ_t-B_YuKCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ffPfzfBhXRis34aH942JYALyanCsjkY98R9tFTddqtjXU93g9MhHXE-Cfqnt-UAQ-Bd_cStbDZTzIs4-nRtT6fyfxFmn8TRBxm9V84Oqs5xKSv10CR87OLozdKOxZyjqJJ9yJ45qyT2bpSTRMxXDxPDYOKwCypPfG82XNXmWki3yK-HW3akwVKSZ796_RFjZ5HlwcBd7GIJE8k6nuV21d0KYJtvy0M8037I6VrfUAeYWacGSe5znLSVvOUzbQs62b1ts9Th_7gN-unQXPo2F6TsD2xS5G3-bJHdPuNx41XO-eEW8XAB0OtZhPndf7qNnEclLFU38a8yV53P5NhKoKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/trjCxbsYK1I2TZjGU6DYOyJ6ZAPa-ogxummyTUzOLVGMxt8DbypkY4xl-R63mCzpSli0SqLoDPCKXWr9hYQwdIxBM3Mcttjv27bzHCikAQGHxTVnQVv46f0k4tujJVw71cHGWMFfKCPjOzjrIZ8hZXPnKB1rPiEvLPgTGueqdXoh3F-xEquUjxcRuyIyQxZOfE5VIIV4GgnkVMtOOQW5Hj355nJ-D_-FZfKu9W-YDr7NPT4A9xZSwDQ4z_znsxX24bqvcyL1852yCUzE4sBZzhUrmjmW8E5LUMUM-5umcN7iOpQ-8Pl_Zx-eQCBYvFUrL5pia3WzUmCX9q5x0qRwNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
شهرک صنعتی شمس‌آباد
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69512" target="_blank">📅 13:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69511">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ecbf36384.mp4?token=JW84bhkMxSP2-PxW4yHRdfjCou8l82VAY28gc15cygvT_Ha7iKfcVDnbCqV9YXe2RKgfL79SYPQLiZV2sX_CBipDUBgi_XyfrStJvhzmjML8utNS5Zu3AdVDLlVMdywyp60KGTgxZmL_0zoI3dogjTBP9-Rwk1v6AWMfy2L-3U3ttCUFBuF_OeHG5RJBqmp1rW336cBd7mZO-UEzw641NLaoa3khc92lqouC1eX7jtjlBoleIa-ab1eKKkAUEo0yyNBnkH0f2cXfsu9ACCFN3ahey2Zq8wnXPQaEqnZwgicV5bfcdLLXt1Raa_lxk3EjsfgYJK5nGkPiTJLPlL7sHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ecbf36384.mp4?token=JW84bhkMxSP2-PxW4yHRdfjCou8l82VAY28gc15cygvT_Ha7iKfcVDnbCqV9YXe2RKgfL79SYPQLiZV2sX_CBipDUBgi_XyfrStJvhzmjML8utNS5Zu3AdVDLlVMdywyp60KGTgxZmL_0zoI3dogjTBP9-Rwk1v6AWMfy2L-3U3ttCUFBuF_OeHG5RJBqmp1rW336cBd7mZO-UEzw641NLaoa3khc92lqouC1eX7jtjlBoleIa-ab1eKKkAUEo0yyNBnkH0f2cXfsu9ACCFN3ahey2Zq8wnXPQaEqnZwgicV5bfcdLLXt1Raa_lxk3EjsfgYJK5nGkPiTJLPlL7sHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ستون دود در شهرک صنعتی شمس آباد
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69511" target="_blank">📅 13:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69510">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
گزارش های اولیه از انفجار در شهرک صنعتی شمس‌آباد فشافویه تهران
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69510" target="_blank">📅 13:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69509">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfb1d4db65.mp4?token=hkYEohTxEWhP9OWFRfVG_3wjvF-jaqp2wMYPRdnxDWwYP_RWcKqQ2wjsUUAG5KuPbGz5lTxU_ovAVhYiiNQntwY_uC7_pJdX6bh0IlphDvDGgbIH5W_LZCXtwW8IF4_tGDO-FeUU5sHkF98Wu2kPpDtdTxFkHTnua8h7yuFKcPf3MgEBFlCoLOgowGf2_XQVblGFbi1wfRa-NTGCaz1CGrDNQJpTf_DUMiA0al9KAGllC9ywrhg5KOdi7zO9oDSSm6qRo0zI4pJyRG_IgZ5AcaZNwq64jWip5__IX5pN_jk5mx-Ki-gx5ihUGuwWPfaXKIn7xFUoChY24wXrE4slDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfb1d4db65.mp4?token=hkYEohTxEWhP9OWFRfVG_3wjvF-jaqp2wMYPRdnxDWwYP_RWcKqQ2wjsUUAG5KuPbGz5lTxU_ovAVhYiiNQntwY_uC7_pJdX6bh0IlphDvDGgbIH5W_LZCXtwW8IF4_tGDO-FeUU5sHkF98Wu2kPpDtdTxFkHTnua8h7yuFKcPf3MgEBFlCoLOgowGf2_XQVblGFbi1wfRa-NTGCaz1CGrDNQJpTf_DUMiA0al9KAGllC9ywrhg5KOdi7zO9oDSSm6qRo0zI4pJyRG_IgZ5AcaZNwq64jWip5__IX5pN_jk5mx-Ki-gx5ihUGuwWPfaXKIn7xFUoChY24wXrE4slDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرودگاه رامون ایلات اسرائیل، پر شده از هواپیماهای سوخت‌رسان آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69509" target="_blank">📅 12:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69508">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca3c95000.mp4?token=ccGgSPpgyjPvTqPNhPm9SA4gtcLYuTPc7vdmK2gHEp1amK04BlKPBslZGlk0kVIMAECMN_oVR5UN5nQYA49LBvPOMlaesmRTNlLvARS-kmUBEsx4KfN_mxbzU1OVRt3V5prmmavjYhlCMv6-HHcUvqaKVZzUeBC27VoRUW-B0XyhWqTagS53Kc_zR20YHjyuO1aXEdREi34W_YTvDkBK3C1PmLcU0sKvH22DRqQHZZHJWncGK8ijS5Zo3xcUchBTtFeLMPlJ-7LAPotP-3thCAyiyqVSG4ubECVE4fHvsnWuOg95G1ljQlKUMnhmv2-d-wR4IZ25GF-FbQg_IX7CYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca3c95000.mp4?token=ccGgSPpgyjPvTqPNhPm9SA4gtcLYuTPc7vdmK2gHEp1amK04BlKPBslZGlk0kVIMAECMN_oVR5UN5nQYA49LBvPOMlaesmRTNlLvARS-kmUBEsx4KfN_mxbzU1OVRt3V5prmmavjYhlCMv6-HHcUvqaKVZzUeBC27VoRUW-B0XyhWqTagS53Kc_zR20YHjyuO1aXEdREi34W_YTvDkBK3C1PmLcU0sKvH22DRqQHZZHJWncGK8ijS5Zo3xcUchBTtFeLMPlJ-7LAPotP-3thCAyiyqVSG4ubECVE4fHvsnWuOg95G1ljQlKUMnhmv2-d-wR4IZ25GF-FbQg_IX7CYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توی روسیه بدین شکل یهو یک پهباد اوکراینی اومد خورد وسط مردم لب ساحل و 6 نفر کشته و بیش از 40 نفر زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69508" target="_blank">📅 11:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69507">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⏸
مستند از شب های تهران قدیم که در دهه ۵۰  تهیه شده:
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69507" target="_blank">📅 11:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69506">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=OTTXMsf3uEHnFtUURRrdf5TB2gBwn09ygNyJvd_yRn3cVQa1JywlVIeifp8N6giQWHYcGn_hLZFUQaYsmFqTPXWqfJARKBBFZbTvf8UsZr8EVHnGIICqHrbCHrRnX3omMjK6C35OlkVCjwUERFBGKRM-IxKdJ4RUzeVFDRARJQaX7AcQ7SUZ3Zsjj2aLMIHNag6aZzyT74NWdYCzG6noO3JcS0ZHywud4_8FGCo-wayAd2_xbdu2-kwTpc_M5GV9YrTwjpNxdt4wa5GV8eNm8UDG-u2SerOrr9LQwDGsN82xElXkwLA-8-9oD7LSl6KjhQxETx_hiG5jpz4YQ46Bw5FX_62X7sQzOvc2tQFMr1td3l8bSvo7DHfO7uzMfz64-vA4gzPBhGZIC_gbQmaUW6cK1WceRYbuLl7fueumHu74RtFYxG5iGL93axOuX_Gh8ZfhtyQFiBCoQVS0_n5XLyHbGijjPI4KgNskCuIU7BxRoXEvunvC18ph8m-JmLn6MzN569oNLC4mUf8KfznMYVKXwrw0CY6xeuh27l4Y9EIKEWOK8kh9J9XBzrhnlgSO-jLthOa57e68eUVQMAYxe9Owyt9ETYdRKGBQwUcpjaUXh1zgnHRku6ixyZaHnHIfVZJIDHGKR6RRbEZCdhjMaKAw5vLXKaGaI1obUS-4Wlw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=OTTXMsf3uEHnFtUURRrdf5TB2gBwn09ygNyJvd_yRn3cVQa1JywlVIeifp8N6giQWHYcGn_hLZFUQaYsmFqTPXWqfJARKBBFZbTvf8UsZr8EVHnGIICqHrbCHrRnX3omMjK6C35OlkVCjwUERFBGKRM-IxKdJ4RUzeVFDRARJQaX7AcQ7SUZ3Zsjj2aLMIHNag6aZzyT74NWdYCzG6noO3JcS0ZHywud4_8FGCo-wayAd2_xbdu2-kwTpc_M5GV9YrTwjpNxdt4wa5GV8eNm8UDG-u2SerOrr9LQwDGsN82xElXkwLA-8-9oD7LSl6KjhQxETx_hiG5jpz4YQ46Bw5FX_62X7sQzOvc2tQFMr1td3l8bSvo7DHfO7uzMfz64-vA4gzPBhGZIC_gbQmaUW6cK1WceRYbuLl7fueumHu74RtFYxG5iGL93axOuX_Gh8ZfhtyQFiBCoQVS0_n5XLyHbGijjPI4KgNskCuIU7BxRoXEvunvC18ph8m-JmLn6MzN569oNLC4mUf8KfznMYVKXwrw0CY6xeuh27l4Y9EIKEWOK8kh9J9XBzrhnlgSO-jLthOa57e68eUVQMAYxe9Owyt9ETYdRKGBQwUcpjaUXh1zgnHRku6ixyZaHnHIfVZJIDHGKR6RRbEZCdhjMaKAw5vLXKaGaI1obUS-4Wlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش‌هایی از گفتگوی ترامپ با خبرنگاران درباره ایران به زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69506" target="_blank">📅 10:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69505">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca6498e72.mp4?token=EaXrGCPj0eghK8ccBFdAqqq2PBREUaWljSj-pGbKbiANFOT-kQKqKjEWB_aKVMbrxpa8xz7imz_qZYESRz9x330vGdBvJ6KwXWHoS0M55__JK-_3fHLId88vP0Xl4uJbHozG6kJw3wYrelXrIbhJsBhEH1yA1gy3tZ_P5bwf6gFW0R2moLoB4XSovByK-t0fmboVvohjhEJuYHa3TNdH2rD72jr3dwYATDdc8_eEKfDUk25ERlppLciKyHxJJ3JAka6nZZQYdaA11-2TDGDRj_CulwMljL-gkDt4pDFlp2wWNCz6FuqtA_QFVLT2NY8OExcemJZFsSABCnJBK2fUuQYk_CfG63NQHlhFIMnTagbYnLlifuka_oUdjAvu6Bmnhqf2M6fzUY6ACDiWJTmg6HMpdRca77cU743S_8GYiBdkjWHJsoMReZUKGtu2OBGRGFSuBrftemIc_-0YJLyC8xIHeqC6mar7grJ7ibQYab5oQa8n6ZP8Ni6MKQ-QfnU-0ZHaY-cbnUhZ0DmbdEH-MwczL4HZ7aOohA4GlrV7sLJljjiy9Yf5BRCpqX3_mVO9EFFnvPOiEkJjn7kN0-spOirelGSNqG3zIzCZPk8MZJ9708OzC8RwYNyR8akk0qPflzC5g4bA7gLrUnrVLtgyndLTrbGrmCLD_jybfa5AjOk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca6498e72.mp4?token=EaXrGCPj0eghK8ccBFdAqqq2PBREUaWljSj-pGbKbiANFOT-kQKqKjEWB_aKVMbrxpa8xz7imz_qZYESRz9x330vGdBvJ6KwXWHoS0M55__JK-_3fHLId88vP0Xl4uJbHozG6kJw3wYrelXrIbhJsBhEH1yA1gy3tZ_P5bwf6gFW0R2moLoB4XSovByK-t0fmboVvohjhEJuYHa3TNdH2rD72jr3dwYATDdc8_eEKfDUk25ERlppLciKyHxJJ3JAka6nZZQYdaA11-2TDGDRj_CulwMljL-gkDt4pDFlp2wWNCz6FuqtA_QFVLT2NY8OExcemJZFsSABCnJBK2fUuQYk_CfG63NQHlhFIMnTagbYnLlifuka_oUdjAvu6Bmnhqf2M6fzUY6ACDiWJTmg6HMpdRca77cU743S_8GYiBdkjWHJsoMReZUKGtu2OBGRGFSuBrftemIc_-0YJLyC8xIHeqC6mar7grJ7ibQYab5oQa8n6ZP8Ni6MKQ-QfnU-0ZHaY-cbnUhZ0DmbdEH-MwczL4HZ7aOohA4GlrV7sLJljjiy9Yf5BRCpqX3_mVO9EFFnvPOiEkJjn7kN0-spOirelGSNqG3zIzCZPk8MZJ9708OzC8RwYNyR8akk0qPflzC5g4bA7gLrUnrVLtgyndLTrbGrmCLD_jybfa5AjOk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
مستند جزیره خارک(1345):
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69505" target="_blank">📅 10:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69504">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb81b5812.mp4?token=cRswl4KPAOgk-NnoCieVFFija5rloP0o88rLnBu8ZGrp0McIgAGcshU4nil5KlFW5RCpO9fqwu60b-rjFF8rwjNh1vYqB0BjpG75MKR-HGucLV0pwczrIGgBsWUwKrT0xYZgqKJUGsXm_DjmLCDkxgE84V73jGDPPoF2Qj_7qn4GBw1AcrhLNE8w7lzP9VoUBM2r-LIXAM-mVQuWajar2BnSA6dtbLB4CgqsIbIwjoyYzl0bF-WV_ErIZQWXbMYHmQlfqNHAy5a-IolvDImEUOIArFluSclVfoOU0r3ZApY7cSmItMAFO2Vd77Vx-Psfg1WTjGkFDa5jQqVxu3fqlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb81b5812.mp4?token=cRswl4KPAOgk-NnoCieVFFija5rloP0o88rLnBu8ZGrp0McIgAGcshU4nil5KlFW5RCpO9fqwu60b-rjFF8rwjNh1vYqB0BjpG75MKR-HGucLV0pwczrIGgBsWUwKrT0xYZgqKJUGsXm_DjmLCDkxgE84V73jGDPPoF2Qj_7qn4GBw1AcrhLNE8w7lzP9VoUBM2r-LIXAM-mVQuWajar2BnSA6dtbLB4CgqsIbIwjoyYzl0bF-WV_ErIZQWXbMYHmQlfqNHAy5a-IolvDImEUOIArFluSclVfoOU0r3ZApY7cSmItMAFO2Vd77Vx-Psfg1WTjGkFDa5jQqVxu3fqlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
محمد باقر خرازی:
اگه پزشکیان یک بار دیگه استعفا بده، مجتبی خامنه‌ای موافقت می‌کنه
.
مسعود پزشکیان تا حالا نزدیک به 28 بار یا استعفا داده یا تهدید به استعفا کرده!
قراره ذوالقدر رو از دبیرکلی شورای عالی امنیت ملی دربیاره و محسن رضایی رو جاش بذاره.
مجتبی به عراقچی هم گفته دیگه به هیچ عنوان حق دخالت تو مذاکرات رو نداری.
همه اینا همیشه تهدید به استعفا میکردن ولی از وقتی مجتبی خامنه‌ای تهدید کرده، دیگه فیتیله‌ها رو پایین کشیدن.
ماشالله مجتبی خامنه‌ای خیلی سفت و بی‌تعارفه ، پدرش یکم تعارف داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69504" target="_blank">📅 09:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69503">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-VJ7rMZBVElFQXGNTU0TwTCP5-t2ERdqwX8q9DAwDJZ7NofXyfzlij7aamuDExNo97q53TBYFrjNMFutt55bklqHmslTLe_fgdV-ekqHxhCqVNy9wRO2-HvdjsbnnoL_Ixkhj7OU73NIOqYsNCzLOe97xFzJqXtnVBe63txtq4krzs2Eq5SwZEy-p92M7bGe4i5OwFtlJhEFbcb9QvbFUjRH8nQivHhOxStGxye3sH4RUKATt6AMmnNp5Ua1z0r1AxPzB6qBj9JYsj0H3_0qbzs-Hg0TGiQvopS5gxlj8QqThFbgY6bkctvAuGW059TOWHALoNCqY5BHrBwrx6pcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
یک کشتی باری در فاصله ۲۰ مایل دریایی شمال شرقی «الخصب» عمان، از طریق کانال ۱۶ VHF پیام اضطراری مخابره کرده و مدعی شده است که مورد اصابت یک پرتابه قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69503" target="_blank">📅 03:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69502">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
رسانه های حکومت از حمله به یک پایگاه آمریکایی در شمال کویت خبر میدهند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69502" target="_blank">📅 02:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69501">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db881c0183.mp4?token=MbAsvaW97FPZBGQB-9nkf70mVZXiSAbRkDc75aHq-18n4VpTLOkZ9Bw4twbdpKK54shNBheIhCEQwI3lcBYn3-Zpn5HlnoBuwIcD2YLaX1LdBZTLSBf0jfXdnsXsYTxT2XTeqPDvtG5rvGUUK5dYJEgb98pZrPT595L61Uw726ugjOoMlqL8pZ6d4Be4xHI-fcKoBzz_eZwGe0-LeI49iLgZRG4Uq4kQ1POs9_707-Okihm-2L8O3BbNCnnYoZW9pSvvp8aC1CBtW3H45TjYvbGLBx7lgJc8pPIt2OkJDOeuMCsJMx6TElx3aumG79n_SaAEfWluGF3g4dPSXTN_CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db881c0183.mp4?token=MbAsvaW97FPZBGQB-9nkf70mVZXiSAbRkDc75aHq-18n4VpTLOkZ9Bw4twbdpKK54shNBheIhCEQwI3lcBYn3-Zpn5HlnoBuwIcD2YLaX1LdBZTLSBf0jfXdnsXsYTxT2XTeqPDvtG5rvGUUK5dYJEgb98pZrPT595L61Uw726ugjOoMlqL8pZ6d4Be4xHI-fcKoBzz_eZwGe0-LeI49iLgZRG4Uq4kQ1POs9_707-Okihm-2L8O3BbNCnnYoZW9pSvvp8aC1CBtW3H45TjYvbGLBx7lgJc8pPIt2OkJDOeuMCsJMx6TElx3aumG79n_SaAEfWluGF3g4dPSXTN_CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69501" target="_blank">📅 02:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69500">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
منابع عربی:
شنیده شدن صدای انفجار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69500" target="_blank">📅 02:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69496">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjqhCKOJqcosSOFsahYvkxYgsApU0nwXMMQp0PNydNjcMD4sJllfuHehjqPlSa5il3UOGnt3EP6q56eW83DVB77cNsIL5C-jyyZTPlqasqdgfKkfkmeq7U2z5bHDdg1MQB0uC9vpREzPdApTC3s8nFdPs1G8jF6_LofIpTv5OnIuG6VBfC6hRYVlLXef-trZYe_Kjzy1ISeEjh10soIyX8nlOe5F-qjOW9HMhdmda1m_Wcl_Cz2B-302YLG0MlwShJQS5PmBrIpI5CloZ2tlqcM7BnMnjbFVO6fAv0AWz4-E_k1Len7-443fl2ifoOb2K2OJ_74TkavPrZMzTjj-7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967a0aa4e1.mp4?token=usO6gwTLBTCMJtS0QXC9rxI7_KayyuW9PgM61ohW9LGMiqxhxeXlFFFmeQegmIgbrREgvkJ0MgTpbLIHvpCau61NCXuCMcZf0defXoQbbBsjrOQjFU7vkCxqYkD-P1E6toSCOBgcyMyvKXfu0F2_ps7JLZEvYUu0SVclppN5Ook98DXS77AI8Aokx9mTz-iNniUX6FcoYX1Bqz5kqHG0010uU9wRqa85RtpaGAmZFNsC2Isz0RmQd8SuX2YkxdOJxp05-Gkv3r27msKD0vqsaTmehzDf2V3b6tBCfwrS9GNxzoOo9yFfI3FOq_71pAWQko_4Svka-JcGKLueTiGq-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967a0aa4e1.mp4?token=usO6gwTLBTCMJtS0QXC9rxI7_KayyuW9PgM61ohW9LGMiqxhxeXlFFFmeQegmIgbrREgvkJ0MgTpbLIHvpCau61NCXuCMcZf0defXoQbbBsjrOQjFU7vkCxqYkD-P1E6toSCOBgcyMyvKXfu0F2_ps7JLZEvYUu0SVclppN5Ook98DXS77AI8Aokx9mTz-iNniUX6FcoYX1Bqz5kqHG0010uU9wRqa85RtpaGAmZFNsC2Isz0RmQd8SuX2YkxdOJxp05-Gkv3r27msKD0vqsaTmehzDf2V3b6tBCfwrS9GNxzoOo9yFfI3FOq_71pAWQko_4Svka-JcGKLueTiGq-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این آقای سیاه‌پوستی که تو تصویر می‌بینید، رکورد ویوهای تیک‌تاک رو جابه‌جا کرده
👀
حالا کارش چیه؟ میره به شهرها و کشورهای مختلف و دخترها، زن‌ها و دوست‌دخترهای مردم رو بلند می‌کنه و باهاشون مثل دمبل وزنه می‌زنه!
جالب‌تر اینکه تو بعضی جاها، دخترا حتی صف می‌کشن تا نوبتشون بشه که ایشون بلندشون کنه
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/69496" target="_blank">📅 01:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69495">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b93335655.mp4?token=hP6gLBzwPmdaVW4sFVshWkswDw1TxCCW4oEBIoQnZ09uxE91Tkd3CTALt71E7_NR2l3c7vQqiphF_RhVK3Jx_eljrfeFUyJirlwVQKOMqKScA70rv2E7yQ7XXH8AqpxMEzBlYdvhZhXKLdYpyPucshDJU7n7ntCs1z3oZnIZquPb4wZ-LIOwSaRXUmAHy2VLAxnyMEcVAaWCRoc3e32K3c1cJly4Ei8psx1UWojQSi3rHETUVnSOJXr_NDNd3uU1LBVDCSbW0qX3Gvp9Nljjig6jm34F96mOl-0HvA6R1bTfauyTYrb6bwuwLOm1nHawj_Q-ZHF8uJEq0_Ux-7p-Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b93335655.mp4?token=hP6gLBzwPmdaVW4sFVshWkswDw1TxCCW4oEBIoQnZ09uxE91Tkd3CTALt71E7_NR2l3c7vQqiphF_RhVK3Jx_eljrfeFUyJirlwVQKOMqKScA70rv2E7yQ7XXH8AqpxMEzBlYdvhZhXKLdYpyPucshDJU7n7ntCs1z3oZnIZquPb4wZ-LIOwSaRXUmAHy2VLAxnyMEcVAaWCRoc3e32K3c1cJly4Ei8psx1UWojQSi3rHETUVnSOJXr_NDNd3uU1LBVDCSbW0qX3Gvp9Nljjig6jm34F96mOl-0HvA6R1bTfauyTYrb6bwuwLOm1nHawj_Q-ZHF8uJEq0_Ux-7p-Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دست فرمون پشم ریزون اوپراتور اوکراینی
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69495" target="_blank">📅 00:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69494">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzwZOvJWrg6sm375wt0FPdtbN0filypFaFb8eHXjT2yBXqRsUaHatVrJBO6GVA_P3YbwvCJEV_j8WIEZN5opdlBITScGVH9sHG6nYoYo5Uo_KXVOpgVHN1yLdsEACsEamFg-7mp1U7EqJrnIAHt7lqOo32_bHSKOCBNz4V2L4xQ8osCfodYE9CL7PUIH6ZfZUxRg7dOjTz1kD7x121b8wahApGvnYxJ-K74Z4m60wkGHUALFSXiXFWPBbH-9WMa8-_zCTsQOhElirvZHZ1euoC1AkcUFk6IXpdIJqc067FSt8T3cKZX0c4N9qmiuQmRWtdZRKrWVIYP7KAwVF5Dstw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرندی:
ایران هیچ‌گونه قصدی برای مذاکره با رژیم ترامپ ندارد. هرگونه اقدام تجاوزکارانه با پاسخی کوبنده و قاطع از سوی جمهوری اسلامی مواجه خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69494" target="_blank">📅 00:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69493">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffffb49aab.mp4?token=kHOGCJsibbgbQO1WWa9RTv13R0gue7cxqn3pwLutpZvzPvgbV4lLFqOBj2ARj5vtH4aRh5bP-MouZAYjgvLU7fPDc2Oy8JUoQDgaAgHWhnqRbqJWkd2IEsus3L5Ywd3eeL6tMjFQVukJMskiJ9-c7-8S_z9ENCKPTZHyinMyFvmO0jvIz6Jx0maUquRu7i0sl1i7gmLo6aa9Rom-gB-l45r3qySD4hvFFWVxPI9ru4AAMviCijiEXLdC3JuvKwAL9Tn3NAjUsgGnIue31HKPvhAGQkzeMOQ4sQm-XaMjr6IPwceO1f9qsbYuVU_Oz83DKSI5eqpzsGhaE3HP-kdQjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffffb49aab.mp4?token=kHOGCJsibbgbQO1WWa9RTv13R0gue7cxqn3pwLutpZvzPvgbV4lLFqOBj2ARj5vtH4aRh5bP-MouZAYjgvLU7fPDc2Oy8JUoQDgaAgHWhnqRbqJWkd2IEsus3L5Ywd3eeL6tMjFQVukJMskiJ9-c7-8S_z9ENCKPTZHyinMyFvmO0jvIz6Jx0maUquRu7i0sl1i7gmLo6aa9Rom-gB-l45r3qySD4hvFFWVxPI9ru4AAMviCijiEXLdC3JuvKwAL9Tn3NAjUsgGnIue31HKPvhAGQkzeMOQ4sQm-XaMjr6IPwceO1f9qsbYuVU_Oz83DKSI5eqpzsGhaE3HP-kdQjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محسن رضایی:
آماده بودیم به ۳ نقطه از اوکراین حمله بکنیم ولی عذر خواهی کردن کنسل شد
پل های منتهی به هرمزگان رو آمریکا میزد که حمله زمینی بکنه ولی خب طرح هاشون ناپخته بود
تو ۱۷ روز با حملات شدید موشکی پهپادی ترامپ رو مجبور به شکست کردیم
آتش بسی وجود نداره داریم حملات معقولی انجام میدیم
تفاهم‌نامه با موافقت رهبری امضا شد
کویت رو ویران کردیم و فرماندهی سنتکام از قطر به اسرائیل منتقل شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69493" target="_blank">📅 00:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69492">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571743cf02.mp4?token=XtACn-PgO83C6MexNDBUnCqLAdhTRY0Qsm3jvL2X8V1kzQEXOPGQqAmJDNOm_jmxIWiIfZpT73Os1syqlLI0mL_-dcQ7nLRVCZ7f8fBAQtU_YQpfXQa20ssHJ5S5neHdXfww7nVTw_K31lHSCPm44RzGJ-JFpX93vOS-Qc6KTdqnagCPztBaeNYlgG94LafXBM-DbwXR5ir1dm0zPQXsUK8kl4UGsIVy8ilqjV9JP538V4lI_rT7Kv7b0uQX_5ac4Bzqkcu9QJ7u09iAoJ4ju3wTIyQ-NMRb11K_XuKVfIiuJJ-r95uPj89dqF-IEELMaS02cByTn1eACOgkAPUbKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571743cf02.mp4?token=XtACn-PgO83C6MexNDBUnCqLAdhTRY0Qsm3jvL2X8V1kzQEXOPGQqAmJDNOm_jmxIWiIfZpT73Os1syqlLI0mL_-dcQ7nLRVCZ7f8fBAQtU_YQpfXQa20ssHJ5S5neHdXfww7nVTw_K31lHSCPm44RzGJ-JFpX93vOS-Qc6KTdqnagCPztBaeNYlgG94LafXBM-DbwXR5ir1dm0zPQXsUK8kl4UGsIVy8ilqjV9JP538V4lI_rT7Kv7b0uQX_5ac4Bzqkcu9QJ7u09iAoJ4ju3wTIyQ-NMRb11K_XuKVfIiuJJ-r95uPj89dqF-IEELMaS02cByTn1eACOgkAPUbKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدویی وایرال شده از موکب خدمه ام‌البنین که به زائرا آیفون ۱۷ و آیپد و گوشواره طلا میدن!!
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69492" target="_blank">📅 00:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69491">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدنیاکالا- کفش ویتنام و اروپا در بانه</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQLAxIjvqymg3Ra1C6B8eN1HEKBwb82t98BBj3oRBoL6OMwG8GwaOV4OPUk6M-UGkJYKdeISHKMvf2h9n9qJZ_A48QFaPZj9X6BIj9i7JxGIJS_OKaJR42_t7ORrjPEdXLUz3DGbW7LmABdGdYCliaONkHXZ8BU_orDIo6RIIpG8Kh5jF4iRBDMJ8XlOdNichV7jdkM7GPrLZ-VUS4Vu3_DtjTRRsYm3u22l13FMjNmCsTNh9f0vgtJYswO496CGFq2dYrVsLtVF27XTXk0fw76AOujk86GpUqmqTHZNxSHoMXxul7_oecsFDvNPV6bJ3DHefTD0R7rpCI5lJPFXNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتونی
ویتنامی و اروپا
رو از شهر مرزی
بانــه قسطی
💳
بدون ضـامن
بخر
👇
👩‍💻
https://t.me/doniakalacom
کانال تلگرام مجموعـــه بزرگ دنیاکالا
📱
https://tlgrm.in/doniakala
بزرگترین
واردکننده
🚚
کتونی در ایران با
سـ۳ـه شعبه فعال
💊
کاملاٰ
طبــی
ضـد زانودرد
🦵
کمردرد
🩻
اینستــاگرام
مجموعـــه دنیاکالا
📱
instagram.com/doniakala
✅
ضمانت
کیفیت
💸
قیمت
مناسب</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69491" target="_blank">📅 00:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69488">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AaVBKfvhOSQpQVbzD4jA5zT4GG2SDtqDpm-r6XHuP1ZLO_ClUZhy0mhkS4jUJAgkdozGXSOFO1XtncwD01YzzjZvPKk0KqP3qdzSJOAd0pDF3HVMigHFq8IlYdQuiWy7mfO3TAatQa260dNXMTO3vGmas4JH4YPZkvx2KFLR8FxjngC_089d8e-TR1nN7zp3sTaW5A90yrBkfi1dl6SAqONG_zvX5bAj7wWR-Rkzl9ukek8JNrGXKwACJUGRRvopbF7tqjgXZeHfnEyVdAaZCXPoB3Ys2UVahnmaAEoq82HFKDqz1RcbuKKF0sLw0CPrtxZIoFdxNreyslZ0MPhIPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X2mFht9_wykdi4WxolFz96HgG1h4myJze7JNFBC2uf-PqBmJtissbW-ufOREXvOGSYc93XSXi-S8fEkplX8MoaS8FcLtOP7bf0z6CZH32Kyiqc-OVJvmEAHmJbW9WCeDK8BdJswCRNjlVruviwISNaeJfemhSl_dMKKF4kgIuclRIh2wpxvBprOx7SPsG9FngbGnFPXMTa3Gf_DLQv_TiasyR_7o9VsMczRlOZHSq6PxpYkMYzLKOUe-JCnNDa7QV--_tmZqqcjjO5aiF12S6X69hcpPRJrz3LF0tFJX2icSbbVuCQEM2EVStfucunQj0AaJmLfDbyyfxNHEjloBIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LjDr4T-l14IIZQIRkC9tLtY7rmw9KXHfdMeteWqLsXCu1OmXuo349uMcrL_y09T9jSmyROsZB7yxG3SOkhU1jkjIkV3SgBerP8F2IPKiG_WG4dJV7POta7G7clxLka0xNtM6NXf0M6dDRdiVn-XPutrkmqfpEKYGzbUVotUtyb6YqxNDcmUgEtk056MGp4NPrVUj8tfsZ19Rz1EW3Kzl28S45x0V7fi9zYGyrfqTdWmLULKa8gu5WdyMFZ3qCk6rs3GibyPRY1Y6DhHdU8BvgY7s_IRjohSVg7bS2DAIxGDAo0JlSblo-oDTNeOujLzHtt9umRA09S8xAoSDokIVQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
کامنت های دردناک مردم زیر قیمت PS5 تو سایت دیجی‌کالا
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69488" target="_blank">📅 23:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69487">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ea32ba7fc.mp4?token=uugLMDCymQxXSR0SGCGJ60T6PadJbJ_r_hH-AfHYuxq1Bgx8tOOPh6Rw1qWqDrh1Rn69dA8-U0rYE2jfDQNIVDP3JFYn7lIr9FD3naP4kITXGUJq2JfwoP9XoR-lffIhD9RxbNrtYHgj2B0XoC5mb7K04vOhv-mePsPGLz219nBnTO9N7e81mdgg_eO7QQvH-szJWmn4wWt2Gqy1jHT4OA4Bff4mjrNQcfWdvC62oBEn4RTaHCSNRuC4d_vOwwotORIz1Y5b9InxuaO_4HXiiLbMyqh6CdLwaNQJGYUbX5zewZqUhmRHy3cjbZWp_zjIri9WtmRZ8ZkhTu6CXy1vxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ea32ba7fc.mp4?token=uugLMDCymQxXSR0SGCGJ60T6PadJbJ_r_hH-AfHYuxq1Bgx8tOOPh6Rw1qWqDrh1Rn69dA8-U0rYE2jfDQNIVDP3JFYn7lIr9FD3naP4kITXGUJq2JfwoP9XoR-lffIhD9RxbNrtYHgj2B0XoC5mb7K04vOhv-mePsPGLz219nBnTO9N7e81mdgg_eO7QQvH-szJWmn4wWt2Gqy1jHT4OA4Bff4mjrNQcfWdvC62oBEn4RTaHCSNRuC4d_vOwwotORIz1Y5b9InxuaO_4HXiiLbMyqh6CdLwaNQJGYUbX5zewZqUhmRHy3cjbZWp_zjIri9WtmRZ8ZkhTu6CXy1vxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
✈️
یک جنگنده F-16 نیروی هوایی اوکراین، یک پهپاد انتحاری روسی (Geran-2) را با شلیک توپ ۲۰ میلی‌متری ولکان (M61 Vulcan) در آسمان اوکراین سرنگون کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69487" target="_blank">📅 23:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69486">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22887d7155.mp4?token=iFuOGcytcIP9QjnIH7pMZ5HC4MAU0tHyXT9sAUBTMYX1TCqt0d58GMgWxKXgaoZCLYBhPXYlSD1P_7B4pamhPJ8ZmWsXTdC5s6eVrJOhZPk0BmBX9Atn-LFW8nNVSOdJI8590gjLPRMmZUbkEZOfJC6phD1rBGGLp1N_nealCte2ezyvHylXXPsERDEcuVWPmQvruQ3MF1XpUAIhJOSJ3ZWZXBeMW2H9XLZomL3Oqd7R260fIKzQzysezsLSer-94JerM6y4k23cPQKF7GDQ85ktV56fEKIK0cXA7roiApRFt_G_BMF5syzez0v0eqJ8EDizzCzguA3f7H1KGUL13g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22887d7155.mp4?token=iFuOGcytcIP9QjnIH7pMZ5HC4MAU0tHyXT9sAUBTMYX1TCqt0d58GMgWxKXgaoZCLYBhPXYlSD1P_7B4pamhPJ8ZmWsXTdC5s6eVrJOhZPk0BmBX9Atn-LFW8nNVSOdJI8590gjLPRMmZUbkEZOfJC6phD1rBGGLp1N_nealCte2ezyvHylXXPsERDEcuVWPmQvruQ3MF1XpUAIhJOSJ3ZWZXBeMW2H9XLZomL3Oqd7R260fIKzQzysezsLSer-94JerM6y4k23cPQKF7GDQ85ktV56fEKIK0cXA7roiApRFt_G_BMF5syzez0v0eqJ8EDizzCzguA3f7H1KGUL13g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این خانم که میبینید ۱۲۶ سالشه و اهل کشور برزیلِ؛ در زمان پایان جنگ جهانی دوم تقریبا میانسال بود
این بدبخت نمرد تا جنگ جهانی سوم رو هم ببینه و دبل کنه
😃
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69486" target="_blank">📅 22:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69485">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
آن‌ها با من تماس گرفتند و گفتند: «لطفاً حمله نکنید. ما توافق خواهیم کرد.»
این حقیقت محض است و همه آن را می‌دانند. چه کسی تماس نمی‌گرفت؟
کسانی که اطلاعات را به بیرون درز دادند کمک کردند، چون شدت حمله را فاش کردند و ایران هم از آن آگاه شد.
آن‌ها می‌دانستند چه چیزی در راه است.
قرار بود دیشب [حمله] انجام شود و مدت زیادی هم ادامه یابد، و [در نهایت] چیزی باقی نمی‌ماند.
اگر فرصتی داشته باشم که به افراد زیادی اجازه زنده ماندن بدهم، می‌خواهم آن فرصت را فراهم کنم.
بنابراین، هیچ محدودیت زمانی‌ای ندارم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69485" target="_blank">📅 22:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69484">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20068f370b.mp4?token=JUBpVkwOuy9agTfXK92F0Q28iW5TjN3P1QVExeqsMEMtxm9uPD0GIROXkQWk2aZAwyY66V1MvIlhVY4iJgYGUC3eyuR1Jq0jruBxi9BxteJpe6kjtfYbg1wQVtGnV-Spkk3zwtvgY-c2JvuuRIEPnQpv0nABGM6w_R6HUFs6MoX0fm3C0DFv4blsPbwds7Aq3H8OYEUSIcdoWW9p8CQPLF67yj606HXughPVNS_LzwEmoolkVcGlR1WiXXZZN6ybI9svIMErORRKgvKtQh-6_hp-Ja2ZzFNun4o66FbQZwLf9aY0NFcmue9mdoSdaoRcjmcAUkWOS4vfe73aLhHokQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20068f370b.mp4?token=JUBpVkwOuy9agTfXK92F0Q28iW5TjN3P1QVExeqsMEMtxm9uPD0GIROXkQWk2aZAwyY66V1MvIlhVY4iJgYGUC3eyuR1Jq0jruBxi9BxteJpe6kjtfYbg1wQVtGnV-Spkk3zwtvgY-c2JvuuRIEPnQpv0nABGM6w_R6HUFs6MoX0fm3C0DFv4blsPbwds7Aq3H8OYEUSIcdoWW9p8CQPLF67yj606HXughPVNS_LzwEmoolkVcGlR1WiXXZZN6ybI9svIMErORRKgvKtQh-6_hp-Ja2ZzFNun4o66FbQZwLf9aY0NFcmue9mdoSdaoRcjmcAUkWOS4vfe73aLhHokQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛پرزیدنت ترامپ در مورد ایران:
می‌خواهم قبل از نابودی کامل، آخرین فرصت را به ایران بدهم.
امیدوارم سر عقل بیایند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69484" target="_blank">📅 21:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69483">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec7ad13cc1.mp4?token=RbvjJ3yxH4s9G2yOPXqmXSfOHSVh0-wqbgDKaCZfQ0vmp3AWMhPbp2qtvFzrLPB_YAPLetQz2_x5ZfIhot9kkm-TYgtwDv5fRKYG9oNlTWzIhVhNxPPhi1VL6V_1uUc-Jz472GjyC1cciHbtJPFWL9zhSVK9A4IEmF0mvrvAb0CiSJRVWrnY8qCJTBaoEIixWOAVV-4AreoslvhjrjecCm_65X9go_eQ0fNmz4nnVS6nBfT_95Lpi1V1v51iYgl43Bbax7MMItcsNbeYYhMOw5SlDFXyuTvHCO4aSfwcI9PCJc1YQXX2vQm3vUAksQL8TewFkcHrzqY_8paI4wn3T0nE-BlqTiZihfja0QzlJKcXMe3czrSETJkNWR5nA5uXBwYyRIQhI1rRKHXawV9v8Y1h3NOUmdCVNcV2xVlFjD94suVLtcJWUY20nNuyVmD9AYXCgFMEUuD3_1cDoZSgDZUEHMnlKKgAtHGReyo_W1RA4QzmaiiLtMQv56UATUw9PBGpm_ZpUkFmUp34kAs4e-vV2VT566rHs_MU97LNoy4Gbjtbo8RU1UfLdMUsd2pDGiiTZe_F3hDSwMPK5bHlKJGGGxA3duiwWbPS-nAsMjRslAc3tLRlFTMgR6lSHEaMyQtAvimQzIg2kryMkjrSkOvoaJ_z8BC0lZobA5ZBLSI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec7ad13cc1.mp4?token=RbvjJ3yxH4s9G2yOPXqmXSfOHSVh0-wqbgDKaCZfQ0vmp3AWMhPbp2qtvFzrLPB_YAPLetQz2_x5ZfIhot9kkm-TYgtwDv5fRKYG9oNlTWzIhVhNxPPhi1VL6V_1uUc-Jz472GjyC1cciHbtJPFWL9zhSVK9A4IEmF0mvrvAb0CiSJRVWrnY8qCJTBaoEIixWOAVV-4AreoslvhjrjecCm_65X9go_eQ0fNmz4nnVS6nBfT_95Lpi1V1v51iYgl43Bbax7MMItcsNbeYYhMOw5SlDFXyuTvHCO4aSfwcI9PCJc1YQXX2vQm3vUAksQL8TewFkcHrzqY_8paI4wn3T0nE-BlqTiZihfja0QzlJKcXMe3czrSETJkNWR5nA5uXBwYyRIQhI1rRKHXawV9v8Y1h3NOUmdCVNcV2xVlFjD94suVLtcJWUY20nNuyVmD9AYXCgFMEUuD3_1cDoZSgDZUEHMnlKKgAtHGReyo_W1RA4QzmaiiLtMQv56UATUw9PBGpm_ZpUkFmUp34kAs4e-vV2VT566rHs_MU97LNoy4Gbjtbo8RU1UfLdMUsd2pDGiiTZe_F3hDSwMPK5bHlKJGGGxA3duiwWbPS-nAsMjRslAc3tLRlFTMgR6lSHEaMyQtAvimQzIg2kryMkjrSkOvoaJ_z8BC0lZobA5ZBLSI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا ایران حاضر است به وضعیت آزادی کامل کشتیرانی در تنگه هرمز بازگردد؟
🇺🇸
ترامپ:
اجازه نمی‌دهم آن‌ها [بابت عبور] هزینه دریافت کنند. اگر قرار باشد کسی هزینه‌ای دریافت کند، ما خواهیم بود. ما کنترل کامل را در اختیار داریم.
ما سازوکاری در نیروی دریایی داریم که نوعی محاصره محسوب می‌شود؛ آن‌ها به آن «دیوار فولادی ایالات متحده» می‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69483" target="_blank">📅 21:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69482">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fd9c3c056.mp4?token=lsM4AOH-u0upkWwNXzv5hssTT1W1IvyLbMfyM-0loxuOLr1LgZ5DUOObBB7v6qx9LxrYWXTUc1_Pq2CD0z8VQd8LLxYcJyOkiYPRD23mw3lAJqgTnQC4ClBNypgf7vVMkjg63m6hg_1A4F2YY9PSgfUR-CnYBtZA-mZSv2tedy-yjZkc4m7D1Aa0_m0_oBnhnFrRSxz6wnvOQOO-s1mbbRxan7P7lj8_UUfRFmVQP2kj22g1JHhSllIZYo5zQuoBsQtqJNAZGcjkMqXDbeaABU8wVq00CT771nrGuAdn7nkDlq0NkmnW3RVmoYD-CLmKSTRH-iA_jOJVq1uzRh9jSY4HDTxIlxRHou92mji1GQ4qeaGetvnrC-DPEGhSoAhAidEdjHhIjvtVIxOV76nn9oKpPKc1BfVn4QsrAtvK95N-JI_U_44u0OTNCfrPNbzF2RrYY9dusGjxvq5Oz9Ty_tV1HHirAV-BLQGGrBYOCFq-xrKGDCsU6hVFk44EsUk08TrzxV9s9kM4nPC9bagWNPa8a453l11fXqx0YFEmSex8jcVo27AgegV1B8TKvzMK8ZWvVWks3zNsg-yv71AoVY53RZ4Zs2WnXqHYmgFxCAu6igBo41Rq_g9vQpZsk1sDsT2zb27tVrrEhj4fkg1QfUVHZmxD2Hp8Vl8gXizFHF4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fd9c3c056.mp4?token=lsM4AOH-u0upkWwNXzv5hssTT1W1IvyLbMfyM-0loxuOLr1LgZ5DUOObBB7v6qx9LxrYWXTUc1_Pq2CD0z8VQd8LLxYcJyOkiYPRD23mw3lAJqgTnQC4ClBNypgf7vVMkjg63m6hg_1A4F2YY9PSgfUR-CnYBtZA-mZSv2tedy-yjZkc4m7D1Aa0_m0_oBnhnFrRSxz6wnvOQOO-s1mbbRxan7P7lj8_UUfRFmVQP2kj22g1JHhSllIZYo5zQuoBsQtqJNAZGcjkMqXDbeaABU8wVq00CT771nrGuAdn7nkDlq0NkmnW3RVmoYD-CLmKSTRH-iA_jOJVq1uzRh9jSY4HDTxIlxRHou92mji1GQ4qeaGetvnrC-DPEGhSoAhAidEdjHhIjvtVIxOV76nn9oKpPKc1BfVn4QsrAtvK95N-JI_U_44u0OTNCfrPNbzF2RrYY9dusGjxvq5Oz9Ty_tV1HHirAV-BLQGGrBYOCFq-xrKGDCsU6hVFk44EsUk08TrzxV9s9kM4nPC9bagWNPa8a453l11fXqx0YFEmSex8jcVo27AgegV1B8TKvzMK8ZWvVWks3zNsg-yv71AoVY53RZ4Zs2WnXqHYmgFxCAu6igBo41Rq_g9vQpZsk1sDsT2zb27tVrrEhj4fkg1QfUVHZmxD2Hp8Vl8gXizFHF4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درباره مذاکرات با ایران:
امروز یا فردا متوجه خواهید شد که وضعیت مذاکرات در چه مرحله‌ای است.
مذاکرات به هر طریقی که باشد، به‌سرعت پیش خواهد رفت؛ موضوع پیچیده‌ای نیست.
ما درباره بازگشایی تنگه [هرمز] در روز آینده صحبت می‌کنیم؛ بازگشایی کامل آن.
سپس درباره توانمندی هسته‌ای ایران گفتگو خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69482" target="_blank">📅 21:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69481">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f121f698a.mp4?token=kuOIrtjMLq2wNm-nSuazVU1TQfV7em4GbYhMU0j5UwouHI76Xpeq5lwypuENVjbSag0HSQ-sw4Uy5XMCjxfXH6YlCYnEN0FnSGRvGfkFtU3OFaG3fFrtD2Sj8ak6raj4GrdPoZ5vYkEwJPlamuPyu0rpPlPBs_qSIfmTpT2Zb6lqRTIcxDF2lXY7ighVXKAiSKRWuH5M7BwT5_7EiiLffNwrT5Ly2CLCdA5nMAvqOwHgT6skCP4FYWCqAwW_vxfgxBOWtW3QstzswmS-M0Y-b5btqmaqAqOgOvlcvGy7Vq3BoGvzm26UY4o4q17dxnP2IgUCev6YZjVpLH12VAbtJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f121f698a.mp4?token=kuOIrtjMLq2wNm-nSuazVU1TQfV7em4GbYhMU0j5UwouHI76Xpeq5lwypuENVjbSag0HSQ-sw4Uy5XMCjxfXH6YlCYnEN0FnSGRvGfkFtU3OFaG3fFrtD2Sj8ak6raj4GrdPoZ5vYkEwJPlamuPyu0rpPlPBs_qSIfmTpT2Zb6lqRTIcxDF2lXY7ighVXKAiSKRWuH5M7BwT5_7EiiLffNwrT5Ly2CLCdA5nMAvqOwHgT6skCP4FYWCqAwW_vxfgxBOWtW3QstzswmS-M0Y-b5btqmaqAqOgOvlcvGy7Vq3BoGvzm26UY4o4q17dxnP2IgUCev6YZjVpLH12VAbtJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
این آخرین فرصت آن‌ها برای امضای یک سند خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69481" target="_blank">📅 21:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69480">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b85a0d41a8.mp4?token=iOapgL0dtdd0quzt9_vtAMrjiHxqTmIDxPHNcGQWGDpD2XwjKY5Lsidnm1SzByK-8Y1nngNAq0TsDqhDqf64awSk8j5ObHZOuyYSAd2wRkaW8cE1CGLoFOWq9RbcuSKynbW62Dy5mdUT0YQEwMnvmN1_76bIsjk1NJSqP6H0qw4u__tPMoLq5eBmeFiVP6i7rb6mjuWfgOe6_V3rfcfKDjEvxWTJD81ayGHKFCkEM_DnK3sceG5ZWtHrkw74jxleIEk7UqAqBxyTm9VvKcqoW_2gSxyNdX7JwOFZLsimPW7tqp8k0aygzIwiFico0Z-b4i1U7bbtbs7DpEgdlgoKWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b85a0d41a8.mp4?token=iOapgL0dtdd0quzt9_vtAMrjiHxqTmIDxPHNcGQWGDpD2XwjKY5Lsidnm1SzByK-8Y1nngNAq0TsDqhDqf64awSk8j5ObHZOuyYSAd2wRkaW8cE1CGLoFOWq9RbcuSKynbW62Dy5mdUT0YQEwMnvmN1_76bIsjk1NJSqP6H0qw4u__tPMoLq5eBmeFiVP6i7rb6mjuWfgOe6_V3rfcfKDjEvxWTJD81ayGHKFCkEM_DnK3sceG5ZWtHrkw74jxleIEk7UqAqBxyTm9VvKcqoW_2gSxyNdX7JwOFZLsimPW7tqp8k0aygzIwiFico0Z-b4i1U7bbtbs7DpEgdlgoKWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره ایران:
قرار بود دیروز ضربه بسیار سختی به آن‌ها وارد کنیم؛ بسیار بسیار سخت.
سخت‌تر از هر حمله‌ای از زمان جنگ جهانی دوم. این اقدام بسیار بزرگی محسوب می‌شد و ما کاملاً آماده اجرای آن بودیم.
در حال حاضر، به درخواست ایران و با حمایت عربستان سعودی، امارات متحده عربی، قطر و بسیاری دیگر، مشغول گفتگو هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69480" target="_blank">📅 21:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69479">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2e110a924.mp4?token=ImROWS4dzBpEv6XoQragmKTtsjqeqAer5XZISsALLoQnuLRkRgvngC8ibwwOcw_sZnfs9_rotYm_D5JrpuPEkxafyElU2JM48_VlkigP7_OOAdJdPT6ujJQNmIb3dh62fL-TflIwx9r9BV0HdY9LFDGQV0GBs2xniCDTwti6vxnFqvStrWX_3NjuV_gTDzQ76X2WJ9l6Yb940RDVaUbvRFu-Q6a9v1yhznnMGYtg0BrDnZK_ybfm3k4wr7hSK5CXSX4JXr3LxuDCWjHTAu15Ptjk7x4BgcWkK4SWC546x03VtIvwSxwLO5_ePTE8ga7HVovzfUxZpO8oiIDMDDd3YSm4isu-g9lxx4F3LCxAgaDONaHIYdq6OHxy-ScltDQYFxS2NCCVDKCCLGDSFsClJvkSLYRAQyeN_LghkzbvoqM5ebvON0xwNf0et2ssVJ0-5WB8435Flj98_ajc4j9SonnjXfjgK7F0wGJwWqs4nv9Ijs_8kx-eqaR1m3zHhM92WmeBpq1wb2fg_O4rtJfe4DoNMpgznDe-UmCyA7pE689fPI-jcAMMhVrDcr7A20HS4BGP1CG24gXCpi6Xql4YOBpGtIyr19mtvG2incSiPZgis_ABtNIX7-wIFAkTNtpHAHKFsTfw6rwjKRMaOd6vZbWEZ5zI4P0wItwCVj4L5Y4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2e110a924.mp4?token=ImROWS4dzBpEv6XoQragmKTtsjqeqAer5XZISsALLoQnuLRkRgvngC8ibwwOcw_sZnfs9_rotYm_D5JrpuPEkxafyElU2JM48_VlkigP7_OOAdJdPT6ujJQNmIb3dh62fL-TflIwx9r9BV0HdY9LFDGQV0GBs2xniCDTwti6vxnFqvStrWX_3NjuV_gTDzQ76X2WJ9l6Yb940RDVaUbvRFu-Q6a9v1yhznnMGYtg0BrDnZK_ybfm3k4wr7hSK5CXSX4JXr3LxuDCWjHTAu15Ptjk7x4BgcWkK4SWC546x03VtIvwSxwLO5_ePTE8ga7HVovzfUxZpO8oiIDMDDd3YSm4isu-g9lxx4F3LCxAgaDONaHIYdq6OHxy-ScltDQYFxS2NCCVDKCCLGDSFsClJvkSLYRAQyeN_LghkzbvoqM5ebvON0xwNf0et2ssVJ0-5WB8435Flj98_ajc4j9SonnjXfjgK7F0wGJwWqs4nv9Ijs_8kx-eqaR1m3zHhM92WmeBpq1wb2fg_O4rtJfe4DoNMpgznDe-UmCyA7pE689fPI-jcAMMhVrDcr7A20HS4BGP1CG24gXCpi6Xql4YOBpGtIyr19mtvG2incSiPZgis_ABtNIX7-wIFAkTNtpHAHKFsTfw6rwjKRMaOd6vZbWEZ5zI4P0wItwCVj4L5Y4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: مذاکرات با ایران حالا دیگه متوقف شده.
🇺🇸
املاکی: نه، همین الان هم مذاکرات در جریانه. واقعاً اتفاق عجیبیه.
این بار دیگه اصلِ مذاکره رو انکار نمی‌کنن.
فقط نمی‌دونم چرا، هر وقت دارن مذاکره می‌کنن، دوست ندارن بگن که دارن مذاکره می‌کنن.
با ونزوئلا یه درگیری داشتیم که خیلی خوب جمع شد.
الان هم با ایران درگیر یه پرونده هستیم و اون هم داره خیلی، خیلی خوب پیش میره.
شما هم دارید فوق‌العاده کارتون رو انجام می‌دید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69479" target="_blank">📅 21:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69478">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a7f23c0a5.mp4?token=QdKUrBh73t4y2gdDRdYgTeHrzDsVDFKNgkgz8fJagwisnj_mRwUEOqbP6LvA5xZ_wNDhXfOy2G7B8-wm-AKDeTlrpCE6ZJAn8eQTWi9SmAWVqRLou6MKUg3XfP2Rx-cokfX8FowyjuVxTZYmQq31MXU4xZRrSQsI2-ajuraA99-HEaEEpcj13xnXXVQKDLyMkNpyHUS-bKuS6ibr8RGsWOgLn5WTP72KRang6CJiI6j88uf_i0t4q3t85RIuP_cXyspo-C4i4RUOFlTYgt_mrqI58Nwxb0F9iLX8QFZ9xWEqvn4oHz5oo5OhT48ds1_6htBW_SafxD28lhv8qHEO4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a7f23c0a5.mp4?token=QdKUrBh73t4y2gdDRdYgTeHrzDsVDFKNgkgz8fJagwisnj_mRwUEOqbP6LvA5xZ_wNDhXfOy2G7B8-wm-AKDeTlrpCE6ZJAn8eQTWi9SmAWVqRLou6MKUg3XfP2Rx-cokfX8FowyjuVxTZYmQq31MXU4xZRrSQsI2-ajuraA99-HEaEEpcj13xnXXVQKDLyMkNpyHUS-bKuS6ibr8RGsWOgLn5WTP72KRang6CJiI6j88uf_i0t4q3t85RIuP_cXyspo-C4i4RUOFlTYgt_mrqI58Nwxb0F9iLX8QFZ9xWEqvn4oHz5oo5OhT48ds1_6htBW_SafxD28lhv8qHEO4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
املاکی:
ما با ونزوئلا اختلافاتی داشتیم که به خوبی حل و فصل شد.
ما با ایران نیز اختلافاتی داریم، و این موضوع نیز به خوبی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69478" target="_blank">📅 21:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69477">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/34a1d1b391.mp4?token=r46IT14V-7bFt1XCWi-AW0gSTiUn6EddCAI-mcl18x5qqy-Ks34PTu6Tp4ttm38o7D0K4UUFoOWAJmkBwR3jidMSJAU_wT4-sxYoAanTGqosKE3X6L89QFUMhR1b9k3VgSNTZgEtyMR2P4nSamtE4mAUv6J1dbWhwLNsacqoVbHM_tvlRyh15a9WvcQSZyiIdEQt3zVxHV06hm47wQcjfPZpSZlO-tZD3rFQXB1IJcVs_AOmcGJJzy-E0YczVwTQBsotBPk3-1npnsFYw81cZSgJnXgv6n2xwCWs34H4KTpof_Y_S8DTF2NBp3N8Cl_Vj3_gGaZ34-V6L29-USgthg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/34a1d1b391.mp4?token=r46IT14V-7bFt1XCWi-AW0gSTiUn6EddCAI-mcl18x5qqy-Ks34PTu6Tp4ttm38o7D0K4UUFoOWAJmkBwR3jidMSJAU_wT4-sxYoAanTGqosKE3X6L89QFUMhR1b9k3VgSNTZgEtyMR2P4nSamtE4mAUv6J1dbWhwLNsacqoVbHM_tvlRyh15a9WvcQSZyiIdEQt3zVxHV06hm47wQcjfPZpSZlO-tZD3rFQXB1IJcVs_AOmcGJJzy-E0YczVwTQBsotBPk3-1npnsFYw81cZSgJnXgv6n2xwCWs34H4KTpof_Y_S8DTF2NBp3N8Cl_Vj3_gGaZ34-V6L29-USgthg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
فرماندهی مرکزی آمریکا (سنتکام) فایل صوتی مکالمه ناو آبی‌خاکی USS Comstock (LSD-45) با یک شناور ناشناس را منتشر کرده است. در این مکالمه که از طریق کانال ۱۶ رادیویی دریایی VHF (فرکانس بین‌المللی تماس و اضطرار) انجام شده، به شناور دستور داده می‌شود مسیر خود را تغییر دهد و هشدار داده می‌شود که در صورت عدم تبعیت، با استفاده از زور وادار به اجرای دستور خواهد شد.
ناو USS Comstock به‌عنوان بخشی از گروه آماده آبی‌خاکی USS Boxer (ARG) و همراه با یگان یازدهم اعزامی تفنگداران دریایی آمریکا (11th MEU) در منطقه مسئولیت سنتکام مستقر است و توانمندی اجرای عملیات آبی‌خاکی و واکنش سریع به بحران‌ها را در اختیار نیروهای آمریکایی قرار می‌دهد.
بر اساس آخرین اعلام سنتکام، نیروهای آمریکایی تاکنون ۴۴ کشتی تجاری را که به‌صورت داوطلبانه از دستورات محاصره تبعیت کرده‌اند، به مسیر تعیین‌شده هدایت کرده‌اند، دو شناور را برای اطمینان از رعایت دستورات بازرسی کرده‌اند و دو شناور متخلف را که با وجود هشدارهای مکرر از اجرای دستورات خودداری کردند، از کار انداخته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69477" target="_blank">📅 21:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69476">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDegfK2sL_1Ww-xpkRpKfIrtPSaW2IyjLnGDiIZbvkAAxOcpyaNHoTbAVljrOwbB1S2VaXu5RDDL13NKAp92nHilvZvlrkLjgE0L5VM3rCYpURAv3m7zcc3knDmYX9HfvrECt7p9K4TXvZAXBEJTyz9ykjyxjPo0AYvlNwA1DJnjbiY-hF-TOcT-YNV0PhUVlLPf7XEEfQIsIz-1hrxObZXUyoLV_GeJ3u6-F_C11Wv1rRgd_QH_CYQ_AgjcDkmOihOwJvGik6h9qNocYD_tBd8_J_JYq9OF2katvON2ySt2skdW3btVOGGfA7WOcUs7aQLrnp--wW40wU1E6PHigw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مارک لوین:
من از اسرائیل حمایت می‌کنم.
من از اوکراین حمایت می‌کنم.
من از تایوان حمایت می‌کنم.
من از مردم ایران حمایت می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69476" target="_blank">📅 20:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69475">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6RT7SP9aiJLlMEbTsLGvXz6cFO4jV_EN4PIldoNjAn0yNtRKlnhFhh3iRgLA3TbcYNI3rqI5EMwbUtE4wiE08ntOUVd4MJfigiBB-8-oLcXFbOyoiNs9tH74MDuP6GnUg2ScitxtkUpy_XvAOzxTSFIRdk3z8Per0rdRxHfZcRvkSxhVSwycTHDGb6aX9nNnvXAGShIuVbSFqiWqyJoQ03l-0fnnDgBVGRGaCl5oaQl356sBnv8QKd12N_x24wb4uSzIcwfjPLK0Vi4t5FdVvdtQYbS9Z1BLMIIkysSB0Y3aspwPs08cW3Oxygpbam3HlHMgqlOtTcqOWOYnWlLeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ : رهبری ایران واقعاً یه جورایی دو‌رو و ریاکاره که باورنکردنیه؛
خودشون می‌خوان مذاکره کنن، بعضی‌ها حتی میگن التماس می‌کنن، مذاکرات شروع می‌شه، جلسه بعدی هم قراره به‌زودی باشه، بعد علناً و با افتخار میگن که هیچ مذاکره‌ای در کار نیست، هیچ صحبتی نمیشه و فقط با «عمان» کار دارن!
بعدش هم همون چرت‌وپرت همیشگی‌شون رو تحویل می‌دن که می‌گن تنگه هرمز رو با قدرت خودمون اداره می‌کنیم، در حالی که از قبل کاملاً تحت کنترل نیروی دریایی آمریکاست و همون «محاصره» یا همون‌طور که بعضی‌ها می‌گن «دیوار فولادی ایالات متحده»!
هیچی به ایران نمی‌رسه مگر اینکه ما بخوایم، و هیچی هم نخواهد رسید مگر اینکه یه توافقی بشه یا اینکه کامل تسلیم بشن.
فرقی نمی‌کنه ایران بخواد قبول کنه یا نه، واقعیت اینه که ما داریم درباره‌ی راه‌حل مشکلی حرف می‌زنیم که خودشون دهه‌هاست ایجاد کردن، خیلی ساده‌ست:
ایران هیچ‌وقت سلاح هسته‌ای نخواهد داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69475" target="_blank">📅 20:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69472">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4129d878df.mp4?token=JgMnpRvfmQiK1iA1wUN__wZUJYiMCN4Yu6RM79x1dBS5IG2LxUT10LGgwqMPWR0yfXx_IBOCJBBx7ZIgnJoQhPwAqVLVkDOzR1Osk7bRGwrMT-ubmVFId8Rq8CT0Ov1mtJ6fu4S9ELzqngBUPTZHNzgeLcnn-o03AQVdbgBQhKvkuAxg52glptMady47Lb1yLNqQn1fs9ZjBJzHA86rBj3T2LengYxVfo0ClQr2e0xL-mmTHqB_codcWIe_EeAp93l-L-Ybr1gi2pWuzpSCbWKISGJ_5cGallVztRRXLZ214CHkYcM_nNymlW0ZFPD7dEhvnAKcFyNxuiAY6Qy4sJA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4129d878df.mp4?token=JgMnpRvfmQiK1iA1wUN__wZUJYiMCN4Yu6RM79x1dBS5IG2LxUT10LGgwqMPWR0yfXx_IBOCJBBx7ZIgnJoQhPwAqVLVkDOzR1Osk7bRGwrMT-ubmVFId8Rq8CT0Ov1mtJ6fu4S9ELzqngBUPTZHNzgeLcnn-o03AQVdbgBQhKvkuAxg52glptMady47Lb1yLNqQn1fs9ZjBJzHA86rBj3T2LengYxVfo0ClQr2e0xL-mmTHqB_codcWIe_EeAp93l-L-Ybr1gi2pWuzpSCbWKISGJ_5cGallVztRRXLZ214CHkYcM_nNymlW0ZFPD7dEhvnAKcFyNxuiAY6Qy4sJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
درگیری عرزشی ها و پلیس عراق در کربلا:
توی عراق یه روحانی به اسم صادق شیرازی، مخالف جمهوری اسلامی و خامنه‌ای هست، اون معتقده که فقط باید گفت لبیک یاحسین، نه لبیک یا خامنه‌ای.
حالا عرزشی‌ها دیشب افسار پاره کردن و هجوم بردن سمت موکب این روحانی و شعار مرگ بر آمریکا و لبیک یا خامنه‌ای سر میدادن.
عرزشی‌ها شروع کردن به کتک زدن مردم عراق تا اینکه پلیس وارد شد و با شوکر و باتوم عرزشی‌هارو کتک میزد.
طی این درگیری بیش از ۱۰۰ نفر به بیمارستان منتقل شدن و عراقی‌ها میگن دیگه نباید ایرانی‌هارو راه بدیم، غذای مفت میخورن و مارو کتک میزنن!
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69472" target="_blank">📅 19:54 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
