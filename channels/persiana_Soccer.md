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
<img src="https://cdn4.telesco.pe/file/t__wUD5960hfXh1yJzC1VboECe33bVVc130ScU6CzuLMnVPSJ1z8_IElWBps-Ya-jwkz3N-gF55iFyySrQSHJFl4XnWK8TUP-4TV9B1FXWUozqNLN0UW1BiXlXh5PvDY5i5FzPrCUgGUkInFiGcjmwSpJAMMfu5mkyOl3ixhfmbnYSOQxh77fdbFeexTdvgRUGl-n94PUl_BwykOCNRB1jqTfl7Po8aY7OU6oXwjej0mMqQdliB4KoojOuPbKyuq9gSEQM0kJd76mINUPOWVbehrU3VzpVl3nqFsi43_t1IPketbQsb3eea_J0a-UjZT_avp9lx1MddaDI4GNRWb-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 514K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 18:00:25</div>
<hr>

<div class="tg-post" id="msg-25864">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpZlYrGSPXmzxUemkMHD0mvjBC3J-zlrpBculJ1asBANbNVp4n2qO5ok_8RIITfZC1xrCI4dUPIUwPEwdl72kYWvTwbFZmODO_aa8TUCeKAJyd6Nei0gvcsVI4EMWEUUq2wZEBdUX6f0pLePa31cGezEszEJ3xsvMRLs_2dcMOoAb04JdSsJEC3S-bnZbmghC1BoZoC0a-otYTE5EvhhY6CpBIv892fccaT4yb3SZWsICHL5y0VFxzPqa5dvPp4I8nloJNEmMtlYG006WmjcqZOllfSWaYyvFmnuVmuq5o4pSlBuxn8Mechlqc2q9o43ZrgRJ9TqQWP2SwcUSyBFfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه‌نهایی‌جام‌جهانی؛ صعودتاریخی و دراماتیک یاران لیونل مسی به فینال‌جام‌جهانی بابرتری سخت و نفسگیر مقابل سه شیرها با طعم کامبک.
🇦🇷
آرژانتین
2️⃣
-
1️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/persiana_Soccer/25864" target="_blank">📅 17:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25863">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed064d5f2d.mp4?token=OIzd_qy9IT9qzXW7ddyZpTz4GNPxjHtQ2FYUwTTc_vkFfdmNAj79sBZB39UMnRSIFLnK2yws5BkW5jKd3bq4Wpkyfem-qh_6aHI8S_9pybnrYmaoC9eQuCxFUi4Idwj8V0Lhh8yRm5pjq3c0XYc1O8dhRg-LEdgprwP_ZeL3WLwtl5Stg62dObgWWiXZVxnBcy2aOUyVeUbQFWGtaojUdAKHuG_WWoQRU74kBhJSOx_S4cWQ61zbseu0mn9RsATPB8r2JunlhGnwRaDyjvu3-0n3h9aEJhqboNuBtHtXWsqfpuXzIU3PzwqO42YasMhXUnVv0M5CYHbdRdUJV20Uwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed064d5f2d.mp4?token=OIzd_qy9IT9qzXW7ddyZpTz4GNPxjHtQ2FYUwTTc_vkFfdmNAj79sBZB39UMnRSIFLnK2yws5BkW5jKd3bq4Wpkyfem-qh_6aHI8S_9pybnrYmaoC9eQuCxFUi4Idwj8V0Lhh8yRm5pjq3c0XYc1O8dhRg-LEdgprwP_ZeL3WLwtl5Stg62dObgWWiXZVxnBcy2aOUyVeUbQFWGtaojUdAKHuG_WWoQRU74kBhJSOx_S4cWQ61zbseu0mn9RsATPB8r2JunlhGnwRaDyjvu3-0n3h9aEJhqboNuBtHtXWsqfpuXzIU3PzwqO42YasMhXUnVv0M5CYHbdRdUJV20Uwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/persiana_Soccer/25863" target="_blank">📅 17:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25862">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TC329C4PkdJ9QJsIzVxeAkbY3G4bDjkeV4lTQjo8f0garbB5q-NrTIIv3zRtTD517qOZbwQY3TMpSIHfVfwjSmFj0lwxHEnXm4lTlDW6b3-1mWcSxic_sstlp_Opb4qY6MF_BvQeF1R9scfzVmOrKFKX3lcOtDiZoEN88Rk78OniyZxaFBsgkXobsGIp9D6rCTks71NWfGuq1ZcVXZGO_JJ442xCN6UqEkvpFSr4qslGMK0_QT9t9HH9c36LcMztyR8cCazzwj1KcPyxsdt-VIukppWDpM4WmKNwR9RRIcHYdI6yULUeBf-R1femigkjQEYc5brvOeO9wrW47clm3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت؛ تو ۸۸ سال اخیر هیچ سرمربی نتونسته از عنوان قهرمانی خودش تو جام جهانی دفاع کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/persiana_Soccer/25862" target="_blank">📅 17:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25861">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXClf3SE5oPpS8Nf3kIu8tl2oG3cyNAnoZWngsvaoJu8tOsgGDgZw0BcgvMFboDWbDj9841y0waKxl9ZFtGarq000YtdI9JaRrAn0tvahFVczfxYO-m17mpDSacl3qeXlqN8zpecrm0AJq0FstzYpq4rqJxPjtqBvwgVW4eH2cZqFTBzBV0X_lZvTPdL1BqoLJGtwLt8PknJbrJBdb_QTcOyBXTJhNkWFxsvlli_-wBgEcf-JrUDasRZ5i6CI6T_forpCkRQUdH3Q6Mo-tWuHajDQwwOl0kyHKYCTsTUGg9iRFSB5khutU4gwjpwa6mERRY2OtPvKuN5rsK-EwiUmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیش بینی مهم ترین مسابقات امروز والیبال در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
بونوس 100% بونوس اولین واریز
⚡️
بونوس 100% ورزشی یکشنبه‌ ها
⚡️
آپشن های متنوع با ضریب بالا
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/persiana_Soccer/25861" target="_blank">📅 17:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25860">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlQnAIy5QRMl8YdKYdvnfvFfcgoPIDbCW3z7aX_iPC9ubuT43uOzRVmB9SSMNNQomVNfswXysmO65vyS_57tL-uOOWu4A7gj_RFZeMk-2n53vp5CYg-aDDiupGS5RD6E3WReU91S_N7kgpxPcNk0FNdiXP4tzkBBFPCEr440lp8KpKRt3ocouf5gaGuAhir-_DZTZRrJ5ygG-XuSochTYo1oUD3NNKkdMILBeVKR_SVFEVEnew4rShjAxKwVb-gMeSehDd4wD7M-wEX2ZBUSwHvRkWkrt1ObLQO6OLSwtZ-38gkIlOF2thrak6UswXTZbyRwgNcaWaWl33R3f2CYMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/persiana_Soccer/25860" target="_blank">📅 17:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25859">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orT5BhV9JypTjcXI7rC_nm83Fp16pv9ugnVK4993wz5vz1MTkywzhDuHH0Gn3fIsUoEDt8Ri0O2tDguSi5iVBY0_tiPyl7lgB5P8jwtHeaHSA5oecBml3TFScN3telQ-ZIrymp6viIJvHUYI2fLc40Wnacq0bEMrvwh4okHy1i7tSP6BnVJzOjLpLHzAPdF4awFEACnlAOTAAQNqQ7NfCtYmY1XQIrMzR5H5tR1zgFHMgAXPMUVB4kV48WlOn8vNJzgcDM-3A4aQ_VrljZC252ltwiRHEo0s448XpNzhiw8uFTQTBc0-hbV0wnTIUvgwr7H3dWNS0omI0zx6v8zGqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
جادوگری و هرنمایی لیونل مسی 39 ساله برابرستارگان‌انگلیس؛ این صحنه از بازی دیشب بود که یه لحظه کرک و پرم ریخت که چجوری نتونست چهار نفری توپ دو از این پیرمرد دوست داشتنی بگیرند. تهش هم مجبور شدن روش خطا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/25859" target="_blank">📅 17:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25858">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLwk_Nx67jgfhr9aPurVZE2HJj_tt9a73xYuy5mp4Q_OzAuoWdd7YTlXlsbfQTpnQKHYmoZxSRY8Xqou08bTRf43weL4kwtB94OEz-v_cjG21pepC8MKy4tLgMZ4bk2kzNYYu2m_2K5Z58EDI45hJL3PkvpcWAFi4TDX_LVU9fPmmnZ2THIII11npRgEcIjJz6HSJmXfEymm4MHCF1EfDCk0-PfqjCUQrFqhEQrnQjsskK-Tgs2ovOeMW0QhWnEnvL_JWwMwa9boc-jFfgwCMMxRnr3Pcd7Fwq96ROtMW_Gi1C_KLb8zulRjbkLrXZ1D8JWruMpY2Z4lx3jHojZdLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/25858" target="_blank">📅 16:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25857">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7bm-2gMgjfnEZ8SXV8OskO19KOPhjr5X72sYUGDI325cv51-Qb_BBT0Tme0IJtrLQRXicn3BneBKboRyDjjdLAFWA5J5FJzcOKNQP5Zn3dBfIMd75GCuWe9mQJtKQIWn_6yKwj6SXqA3NL7r7rAGnCILKhY__WspzbABYpipuwgpSfAK-pkY5IubsFZZIXSAuP1Ed8RwNiQoJzp9otgwjFPasT2Rrli9aocF3X8SBa4YHgXdWuzMMzpSzIDRLrnB-FBRAEwX6xb9TomMXlcAXsuAqh4e3Z0CMnLk6nKioz0Ry5K9qbY65jC1M61WCkDfBSBrkIfegPVTtFti4QEBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا
#فوری
؛
مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/25857" target="_blank">📅 16:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25856">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOnxfhVRZODyRfRhUpR2rFKhSVLGTiEmvl63cYh5k0HdmcYBcdelx-XWoEwp-MRKZv3aWhq1-_MMcF40fmCYYrF6Vw_8Ku-azJGz-XpSswe1yKWGuXbD9_QVryiLw-h5Q97RL8ESG0SW7Bvlrl-6aJVnonYZg-7P0hpwc-STtokGAdSjvKYFvMOuhXuUpFDEueDdF9NW9dxKGKW76WoBKbnvyWYVsj83O3OA9A4wAt1AZneNxdAHRRZrUgZp7lTVPEjhVnlDUjjhflPqfoS5YsSSfHROuD1gpg0smMmSABFEMNpqFz2g7NrwyLlq74rqjyaE6vPAUfr7BQbpIJSUgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛بعداز بالا بردن عجیب و غریب رقم رضایت‌نامه دانیال ایری از 100 میلیارد تومان به 190 میلیارد تومان توسط باشگاه نساجی؛ باشگاه پرسپولیس امروز مذاکرات جدی تر روبامدیران باشگاه خیبرخرم‌آباد برای جذب مسعود محبی مدافع میانی 22 ساله این تیم…</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/25856" target="_blank">📅 16:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25855">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4hXJ_W-HuuvSMsOCcQ4huBfch6dtOjRy8ZIc0l8V6NKB5pHOWFbkyHBHphe3ioUTI7_HUJwIULrSLtg1Ojul2x0wIyF4q0KdGFLPP4r2QBEk1eOl8kC_FVUPZIF74ryiJAFVwbB8PHch320XLaZFwc-DbMeUw5S8yNTYxPypPD83Bw8QVu460wveY5HqP5lj4_MZUVgXjj6k62QOGiadr4Alxj-jmLRGrPxF_0ishVlL1RJcGFlALhEjq24u0pxzWtPIGw2216-ciDkui6V8O6dC8rWHOxchBkpAS1lru6FSMtSpuTeUlcGv9_lRjG4V0yKFrw27dXh5bEDagbKug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
دریک رپر‌ معروف‌‌آمریکایی‌در دیدار با کریس رونالدو به او اعلام‌کرده‌روی قهرمانی تیم ملی پرتغال درجام جهانی مبلغ 5 میلیون یورو شرط بسته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/25855" target="_blank">📅 15:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25854">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38af4244ff.mp4?token=CXQavJ_SzknC4g2R_7U4vh1SoCcftMSocRpKW2CT3drOhDYvGXpSXdT77mb80i8939oG7V0PFAcO7VIxrU_f3WUc-9WERPYFuJVWoQXsg4IiUH58lwd1Q72jl7cRw25pWOvU-Bo3j725Chp6oMPSFnm1FosHZY9hkMrZC08WUJBa8r9YlqSZsOvmQNfSXyVHs1xrHEfWF0S3vu1SwOlF8uMT7iOIpVgxsvz85LcGP7ERGDrCw3wHLr7ATnGn0UM4uD13aDfvvHwLP_wtqkzSxpxgKW6IYJM12a_GwJnSXfgFS3NIeDi1QQzFuJ0wFH7xaYKmUVq9GJuNGpjFhmZIxDbIbChLS4Mx_M2DCgkppf09HnysYWA1TcyMkMteYZucWSxRupYEMyUqoXJ0I7z8rlUNRlyHeK_FMJ0CQ3qkxXeSlMxh7d2-JHHBjri8vcRASOuV9WkSu4rCDhAdZh-cKWOzrPKJHUu0g9Bw-97xy5vNadxcKIacHZkaAjjFy-ZI-l2K2plmMxJ1aN-F8xu-oK6dkx_z589sP84I47mdbakyxyM-q5B1cZXyLnyjmAFkMR24k9KfA7Rs0iTx1SWJburaUuTq80yd4fwq1OI3r2bC6D2XvGnSVFYVIEwagpdJVy1wPzJuWI7xzclrpIIN3NASdq3BjwsB0Phmh3eVkeI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38af4244ff.mp4?token=CXQavJ_SzknC4g2R_7U4vh1SoCcftMSocRpKW2CT3drOhDYvGXpSXdT77mb80i8939oG7V0PFAcO7VIxrU_f3WUc-9WERPYFuJVWoQXsg4IiUH58lwd1Q72jl7cRw25pWOvU-Bo3j725Chp6oMPSFnm1FosHZY9hkMrZC08WUJBa8r9YlqSZsOvmQNfSXyVHs1xrHEfWF0S3vu1SwOlF8uMT7iOIpVgxsvz85LcGP7ERGDrCw3wHLr7ATnGn0UM4uD13aDfvvHwLP_wtqkzSxpxgKW6IYJM12a_GwJnSXfgFS3NIeDi1QQzFuJ0wFH7xaYKmUVq9GJuNGpjFhmZIxDbIbChLS4Mx_M2DCgkppf09HnysYWA1TcyMkMteYZucWSxRupYEMyUqoXJ0I7z8rlUNRlyHeK_FMJ0CQ3qkxXeSlMxh7d2-JHHBjri8vcRASOuV9WkSu4rCDhAdZh-cKWOzrPKJHUu0g9Bw-97xy5vNadxcKIacHZkaAjjFy-ZI-l2K2plmMxJ1aN-F8xu-oK6dkx_z589sP84I47mdbakyxyM-q5B1cZXyLnyjmAFkMR24k9KfA7Rs0iTx1SWJburaUuTq80yd4fwq1OI3r2bC6D2XvGnSVFYVIEwagpdJVy1wPzJuWI7xzclrpIIN3NASdq3BjwsB0Phmh3eVkeI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیانابعنوان اولین رسانه
🔴
محمد مهدی زارع مدافع 22 ساله سابق گل گهر با عقدقراردادی چهار ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/25854" target="_blank">📅 15:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25853">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7_t8YG7nHgkimNhHNwdHjUWZrUDdsnIZ6W_-jCeJaktN8N5Hbu1wIvnyNyizEtzMEGsrBo2B1TJ6Kd75hMO6954Nuf9PoubPyYRKxl-oQwr_A72TKCbstsrPdqV3JHhAufSItx50GnrIfFo3ezeXsQn2wih8W3qqfJ27MCFB98engGR-mTL0GZGAZFEj6NJ69cNMCMyzhAwSRioHwpNyR6H-Pdkn3ncU6Yqni7kOVSh481lNFv39UleeM60APx3RbwWpUWOY6zZaYQTH85KkfM_HG1ZDO-EV9O5cKpzAYbmyG0MgeOlxHwbzeKGs1oKKgNbjwRQt8jSt7Kv5b0vgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
#فوری؛ اکثر خبر گزاری‌ های معتبر خارجی خبر از قضاوت علیرضا فعانی اسطوره داوری فوتبال ایران دربازی‌فینال‌جام‌جهانی 2026 بین تیم‌های ملی اسپانیا
🆚
آرژانتین میدن. امیدوارم‌نخوره‌تو ذوقمون وفیفا هم به زودی پوستر رسمی اش رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/25853" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25852">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTxws3QLMQeKMoY2cEldVLlBmTsFiX4przQjcoqTNEQKzYTMk6xguR0GnscwpmtFt5RmBOaFLm5cjqv0DTxqD3dbV_sKX9d9n_g5nss2fyR0mc7soG8dkjMoDIxrcJSt0ucx2seDnpKI-mFX5r8XC-3yoaM4gXLGgBP4QdZ0uxTPrKh-VgdOHVBufklxxfdRxoynrXk1IVS3UwxQc7WZHDuk4SOz9ivBhNNOuuqXg830l-4gNFx3NN5fX_pvtSfCPlSwZHF5jYZmaWu2F6kiwKa2KOFydZzHhNQ2zcyjcPkNdJgzZqrfxCQW9ijpdCUl80PYlOZkO0hojePB-UEZZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
پوریا پور علی هافبک سابق تراکتور و گل‌گهر باعقدقراردادی دوساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/25852" target="_blank">📅 14:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25851">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYtM0AjHfsqWlE7e1a8x1HWbFWbEcoZDqwgoBKvlFr7iqUjJq0r3iIeA0nPV3gJYeJWobw7lg31yNTZscy9qQ46pslm-dWs0ay7kYZlGldgpv2bwVOaYyqnGF6pNNo7c6Co1IbwbfTZsXvp-ygCuVp5pelOicd8mJNUwRGkuPwEOqOAOHpHQdfqOkWRrDjyqq3VuBGEilI72sgHVzeAq1ew_48KlV1ixWs15nZr4k1LA81WeJ7Bkj11w9PQ_RqNQaBcBgjVXK58bLBUaeCZWc5GhvqZ_h866bZ63_U1dW4G3LLPIMc56G9BShm2I0gfR2JdVI2hy663ey9FTE4xoVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/25851" target="_blank">📅 14:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25850">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLyYY9jpUt0IG1JhSmEO8iNm1ZytGtG7afvI8xFj2VlR9FMlGO9D3YOqrVgChsJX1XpO6yVyzY8F9oL4v9lqIutpwH89ENz-3zIcXiWy81FxzW-uFhoHlaD2B9VbyjvFjhhrzm09yOxfirNoyXS1DDMk-mGyYZ9MiJhtbulo2IJBPmVWhIXnpKt9xw9UwZUYs-USDVJxFmNuGUzxxomPt26DnMxGURSooZd3K5sAY2gQIEE6cgFQK3n7AVK3PH4DHTnIRLxX_qM51hyPEWb3MLYfGrielnfi7WtaFdIUILhjKKWit5LxJRO4ET2MsnCT-1o-T5PtBja897hript70A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیانابعنوان اولین رسانه
🔴
محمد مهدی زارع مدافع 22 ساله سابق گل گهر با عقدقراردادی چهار ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/25850" target="_blank">📅 14:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25849">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txz9Ynn8NcXlKa21Et12mBb70pAMD2DR4xRDt4azFLAecI282_K2Wj5KaS-FxbhJMdIB7aQ43-NeRrL3pCLXYn9Hi4G5nq9SMzC7FNP-D3uRzsyLTAj8xwdiSaqOPxSssu1kkS_PE7TdNA875x8OcTirHo9OmcpvujA9neQ8yfm-BtpGFUBSA97yiH1Y5TvFvzxhmGxbQfflu7hrzF3ZvFlWv11hlFWMRsXAAz101MvfvycuMiZdXx337n4OwqmoNSbF5x2wH8FLCgmX9M55qqf_ETvxFCfm13LTNMbeqU32vPk4r6nNtoWQqrita4qvDXhGVAElM8Xf9-0edjS58w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/25849" target="_blank">📅 13:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25848">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfKXy7vXCCDd20FIc-ay6vDfgNY1EpC2OYjHcgKDLgpuO1XqMvKOzU-mcq3QCaNEzD-nWPZI3zAJMfURXfcCsn8LBGv5A76b4diPHk-PTVuKLWmbFgWqpnJ5KBeVFXtXcXKcmI7OPKCAN8k5zPqfjKnd3vA0nbqIJBbFIi-3Ywev2HgS7W1OqdE-YvJTyiQc7jGaIA-55FAENkq0eQ4Cw-4ScWAQdeRKc9PMU8frtGzoUKAmALFECnG1SToz0OAYWXk0qaUtDFnBu2Az_GNEsimoRevI_ng9TM6_7es4sC8oHLXhx4RePGikTysj_xjOCWqtcxNavbSShKnLRztJ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مهدی تارتار سرمربی پرسپولیس امروز عصر جلسه‌ای‌سه‌ساعت بصورت ویدیو کال با مهدی زارع داشته و بالاخره او رو مجاب کرده که به آفر باشگاه پرسپولیس پاسخ‌مثبت بدهد. مهدی زارع به‌تارتار اعلام‌کرده رضایت‌نامه‌ام رو بگیرید می‌آیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/25848" target="_blank">📅 13:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25847">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oY5bEj-6XX9dSyhVPdDoHkFb020y9SJtR8uX4ZzgCYIS8_LP8VrIL339aMRDeEREEoRqHnwR3E1NyvFxRZDFmHv31tEVxT3wE1XP_LUEwYDAqs1jV5XugAxzwUBRMW-iwh8TRGoTNUxQ2mwG-IPVTnA3PF6vLp9htxFzu9-WBNNCTTW7PIxs4Q4coCCtQHVrqeALmMnUPNDQsury1h0GC8VQalavyrTLEMGaz-EhV3zeuLuIsxGdTfXOXaqBKRcPS88dkT2uMoeAHbvm5V1BEmRZsp2axOlDRQv4ou3VSSTP3aoW_D9cctFxGKd-BMv5fZAu2pWH-K7haC-WO7QJVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/25847" target="_blank">📅 13:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25846">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uhm584W51J6op5PhOet63zlB3P8WagwQqTZ1wyEDrxHuxdDoa6q2rZpzT4-t_-HSzd0YSU717EBDzBbvbPheHKB5qCgH4a9iS23TfxccZ2AuW8ydNHIxnlp5Vk24Ycquo-THL2KjmcaQq590Zae4cntJ5BcDertPE6mEtC6KyanBnHb83zJ32cRcD2XtWujPMOzp6cu-PiFEwONM6nTwRSTP5E5YCNLXaHHD4W7Ii30a_eueMpwugW1ah6FmUuoSw5OF5wnAQn3XCaTMXABEdyhlndVYZLnKppym1xDLDwBuR2_pN9YcNmWwIgKQWwHBzP15lGl_2dfPCOsg6pqj1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
‏دلیل موفقیت‌اسپانیا مشخص شد! نهار قبل از هر بازی آنها را یک سرآشپز ایرانی برای بازیکنان تیم ملی اسپانیا کباب کوبیده، جوجه و چنجه درست میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/25846" target="_blank">📅 13:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25845">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4018fc48ba.mp4?token=GIdPTYySYNat8_puWK4c3JzbfarPNJRDV2Ux7Kd80IegegeT1l3GXoTK9Xp4DvSs3I9GqazsK2Irrr9tVQ8veyyhU646bL64WWmF2grM5f5hN_sERqdRb61dAv6hCSrPtWpaH8OVt5vDwCY21_Kf4EblT1DaQgKN-5vZ98gXJLxONw3VIgF3y90wIHF9Sy14WHFPto7pvQ4D2USQgZGI1g7pZHT0MIBkCMFqkMkYulu7OUTxIEuelZZVgO0gTfWNlvDWFtGdv7gJZQXc9k-DT6znOFI4e1nDsOaGzAwIklDE9aWc_YEQTzkWDFbRX8WOmyh5qLoVmpEEZsltAvjfFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4018fc48ba.mp4?token=GIdPTYySYNat8_puWK4c3JzbfarPNJRDV2Ux7Kd80IegegeT1l3GXoTK9Xp4DvSs3I9GqazsK2Irrr9tVQ8veyyhU646bL64WWmF2grM5f5hN_sERqdRb61dAv6hCSrPtWpaH8OVt5vDwCY21_Kf4EblT1DaQgKN-5vZ98gXJLxONw3VIgF3y90wIHF9Sy14WHFPto7pvQ4D2USQgZGI1g7pZHT0MIBkCMFqkMkYulu7OUTxIEuelZZVgO0gTfWNlvDWFtGdv7gJZQXc9k-DT6znOFI4e1nDsOaGzAwIklDE9aWc_YEQTzkWDFbRX8WOmyh5qLoVmpEEZsltAvjfFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇪🇸
تصور کنید توی اوج هیجان و استرس فینال جام‌جهانی‌بین‌ تیم‌های آرژانتین و اسپانیا؛ نتیجه بازی دو-دو مساویه و بازیکن ها رفتن برای استراحت بین دو نیمه؛
همون لحظه بیژن مرتضوی وسط زمین:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/25845" target="_blank">📅 13:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25844">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9hT6NWKkTiruRxQv-aUHKSCjcWMD7UdcDXdlIi2IQFSckuMJf9qyZQjHn4jjM8LTHnTap9MFqKyxwxBQK9YgeCOuZA-RR9JZDFLuje3eU0typ3crgu_WqbQYyV8wiGm7OHy1iFFubth5KtS6PU4IfUqtRKAbh2HEhyddoWaEaeub6hGtzuTndO8YZyDR3UvuR-UsjvwgwOgN1B3MFH20S5FYL0TvCRxg-xDAZgriMjf1n81fHxDzVfcfT1WtLtYjEOfvL4T94nUOaFYsLuPpuoRJfS5XnuoLwnowWnUNL3Hxey7oED6x_2dKrD6VwhNcy9ATEz2LrYtpLONB7N2xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های‌عادل‌فردوسی‌پور درباره‌قاضی دیدار فینال جام جهانی: شانس علیرضا فغانی بیشتر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/25844" target="_blank">📅 13:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25843">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c31e28929.mp4?token=Fu8ABEpNHu_q8zLNrv7hHyOK0fPcVCtSH-r1y4NwEo7BsBunyIqx2fkM1c9vrhzlTlLi9lqQ1Tlf_QT5R5Io3SVmOcPSAtEPkw1K7VEun4oTVWXTwwR7xTNSgvCmvpDl8gvsPKq3TcKPIzkKLWkNL-JTgnmLCizRRW9TJv3Dy0pTv_uBBODdE8ucEwzc10c-A0mRwWx73I7KXkk_cMS-6ByGr0jSn5BllNO6RdvDF5IXcmH0uqKWsfbY4erUw2V0M4ssNPboqQpQFfx7WMeAh0FBFtrmN5sbtuko7hrhs_NB1qXUD4kDe2lhtIIsjI1zl1islcao1ptnb4OnDmRB-V_EkWnEzaemhU1FRNdq-w5ZSQ3PN94aqqEW0s_rv9BJJcLJ3GCYIYuMR_aDNQL8Ovbzskv3x3ejR7u8PizT2atr7pcnepvLylLHpzPepQR6XywPZIjpT1FvaELRS7epbmGWd9PmCA1bHuTIo7rPMZ5H9K_kBgKqdB_C9RsNtzoFb3bLzcd4_TkcE94SbGlWiN-lwbvc0tgUNsD5BZ_Aoczxsy9x9-eqRkZb28BFxGJv7CzU7StlgDqI3AlGgDre3ddsY0fFNuCCg1isnzfgVjsxNLwCi4NVtsBeJkAm2NVjHaGkLY_zPJpvFYxUx7idoMKeSGrfXRTRuuJtqhSoVNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c31e28929.mp4?token=Fu8ABEpNHu_q8zLNrv7hHyOK0fPcVCtSH-r1y4NwEo7BsBunyIqx2fkM1c9vrhzlTlLi9lqQ1Tlf_QT5R5Io3SVmOcPSAtEPkw1K7VEun4oTVWXTwwR7xTNSgvCmvpDl8gvsPKq3TcKPIzkKLWkNL-JTgnmLCizRRW9TJv3Dy0pTv_uBBODdE8ucEwzc10c-A0mRwWx73I7KXkk_cMS-6ByGr0jSn5BllNO6RdvDF5IXcmH0uqKWsfbY4erUw2V0M4ssNPboqQpQFfx7WMeAh0FBFtrmN5sbtuko7hrhs_NB1qXUD4kDe2lhtIIsjI1zl1islcao1ptnb4OnDmRB-V_EkWnEzaemhU1FRNdq-w5ZSQ3PN94aqqEW0s_rv9BJJcLJ3GCYIYuMR_aDNQL8Ovbzskv3x3ejR7u8PizT2atr7pcnepvLylLHpzPepQR6XywPZIjpT1FvaELRS7epbmGWd9PmCA1bHuTIo7rPMZ5H9K_kBgKqdB_C9RsNtzoFb3bLzcd4_TkcE94SbGlWiN-lwbvc0tgUNsD5BZ_Aoczxsy9x9-eqRkZb28BFxGJv7CzU7StlgDqI3AlGgDre3ddsY0fFNuCCg1isnzfgVjsxNLwCi4NVtsBeJkAm2NVjHaGkLY_zPJpvFYxUx7idoMKeSGrfXRTRuuJtqhSoVNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
#تکمیلی؛ بازیکنان آرژانتین بعداز بازی بطری آب جردن پیکفورد پیدا کردند؛ بطری‌ ای که روش نوشته شده هر بازیکن حریف پنالتی‌ به کدوم سمت میزنه.
‼️
خنده‌های‌انزو که‌مقابل اسمش‌نوشته شده بود که “وسط بایست”یعنی پنالتی‌رو به‌وسط دروازه می‌زنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/25843" target="_blank">📅 12:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25842">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3ZkAtoveEhhRVQV5kd06YMu8FcrHimQzz1lboRO6ksc-e1A3qBBkmi1d2N_ITaBwLgeEovP9f1AIiXYMukdVsT29FrZWtcbcqM49k__lRPN3BJv-ZhGULF2G_AkqmPVuduXY3qFtf55DnrqmU9ZhXt6gNWiO4py4P9MHPI-Qn6xgqXnlpyWjU-GM7CJ9rn5Ev85VcwejkOR-inJ9LIo5yNR0zlSAQbSwaI-r__Qy3x-1tdQrXTMdiV6R_39d_pxcgU7P07bvTI_ri12Rj0q_ucVVKhhWhORvB7PK_b9pZJ6wIVDlY49GzbOa6abeFPIIo3VjvyRpptrMM7jaIwr7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/25842" target="_blank">📅 12:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25841">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZjT1p6dZVHhKgCdYBLiC8VU_40q2Wg7ihPwT_cuiLU5LQ6b1mq8zfeqkL6oKr80IjyhhF0wQSSo8TCvQcL9CCbP_1Vte8KjYMnqzWy5Eq5hsNik9tYtoAV-S9hy1IoDw9kztAusjiIpK9VsGfoTjLiZ-uVRZ4a4l5Z9TN_fOrVf_XaAc2WWy9FaFZeHsUK6la-ZDXudgue4iLVgJZM-6-K2tvQlZRsWWnKa12_5OsaYLwEkekd4n2lPv9Mr1hfE4XpqcLGom1FiO6PzeRlyNbdMCRcjyITfxUIZT5wY4C7PIrhortk-gJ-ncyAgWemSnKWbm0kmwRCZ6RjN_6-0oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/25841" target="_blank">📅 12:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25840">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSXzOGkKsDDbL9EOxh6QdHi1tk1w3fBYbhVk0-SyiBY50x-fgcmXMACaIdDy0YS5s8642-p6Z-KG4rTByOkoqXm20N-rfOXwt81Y9YcUbfqJk49ChHGPNd6AOy0DMamzmd2IDvianSpPVf2jpqxeI-Q7vAkYxnlJk4n6fWK975VoN9GdJZ3n14sX0NGEcLAHNAzqVaZgLqOH8MsoaTlbQI8E2WafU5FhWExVfhNZTLyBHX5z2I8L5s4CNhIvyI_2EYwDqJErsa_2cYy7-FoNUr14PRjc7TIIKbk_HBR3VGxG_-xIGjkcl7uU-I0UTArGHYWmqOyU10pHTIdnBAzdcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/25840" target="_blank">📅 12:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25839">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8168388efd.mp4?token=cryYCxLW5oU9ijXeCAm7MFD8Olh_XACHYzWXzTgsWSzjWFdJIz9lQzpjTJIs7jKFzW0Hp10ooEEc5bIN0vvXSSK5mlc92SRUGW_t83n_RpahOdVHUxGn61MrR70ArtHN-lY7qzY8hL0bMrG3biOaq17hJUWjhd2ZBsSPfK0oUTrUXiSKENoKp6yiLVpCdVMB4NsvPZ8Od-fd3qyXh0HhvFF3PP3CpHMlprTuTkJAmAwc0H9GHUcwDNxDwD7hFWY7EpmTZjLx2QrtbMge0biOQTCDpkuolKRd74oulJkdXUATyVs2nLsC9pQ26H3-uI9y0hjxl6s_B2YDjBgKOSRinIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8168388efd.mp4?token=cryYCxLW5oU9ijXeCAm7MFD8Olh_XACHYzWXzTgsWSzjWFdJIz9lQzpjTJIs7jKFzW0Hp10ooEEc5bIN0vvXSSK5mlc92SRUGW_t83n_RpahOdVHUxGn61MrR70ArtHN-lY7qzY8hL0bMrG3biOaq17hJUWjhd2ZBsSPfK0oUTrUXiSKENoKp6yiLVpCdVMB4NsvPZ8Od-fd3qyXh0HhvFF3PP3CpHMlprTuTkJAmAwc0H9GHUcwDNxDwD7hFWY7EpmTZjLx2QrtbMge0biOQTCDpkuolKRd74oulJkdXUATyVs2nLsC9pQ26H3-uI9y0hjxl6s_B2YDjBgKOSRinIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شش پاس گل تاریخی و حساس لیونل مسی در شش جام جهانی که در ان حضور داشته رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/25839" target="_blank">📅 11:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25838">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IeKQ0Ejvp0YIeLWK195OLoOUCH7D4Z5J-mOBzH9X6Zwl9M5j7pDCIS24e7sMADx_pJ5z1fj7Gyj0cPAg-gO-Rbh1DiYK9UY_ITJiUPqjOWorZ-rmVfQOIJVeUCFncBL7-S-UQFRXhpmHR-D4x3zpNYmOLgxi3g3IO8ibTs5gElc_TM3HYdoDBjbf005G1w5KcDCHPhDzdm5sxvRICbNW_-ofxqID3CMSB7EU7s1PRQp_BlOVc5fINRC0Gj08j3yxr1VuGiB1LH6bqlxasGwTv8kGStAvK0vX-zpFPZpcltlNKOACz1wRFvTMUfAtRixDsCtcD_y-5S7l6aCmvczoxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ داستان‌از این‌قراره درسال ۲۰۰۷ در یک برنامه خیریه یونیسف خانواده  نوزادی برنده raffle برای یک‌ویدیو و عکس‌بامسی برای یک تقویم خیریه میشن! این نوزاد ۵ ماهه لامین یامال بود! این جوری میشه‌که مسی ۲۰ ساله لامین یامال ۵ ماهه رو حموم میکنه و باهاش عکس‌میگیره…</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/25838" target="_blank">📅 11:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25837">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇦🇷
شادی‌کارمندان‌خبرگزاری آرژانتینی در طول بازی با انگلیس؛ دولت آرژانتین گفته اگه قهرمان بشیم یک هفته تعطیلی رسمی در کشور اعلام خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/25837" target="_blank">📅 10:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25836">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89c12ba90.mp4?token=AOPAVyoatbtCMAQFPci_tBnQHe0H4gfWtB0yXakR-9M7mgl_yMqpHHKNQ3pZG7zrvy_IDYhgCbNrTQbuoTczeF5hfIgT5iW7omwbXkWavu3YMvOSjo8jEz6wE2LqzTl98iEBhHPxtF4dYWKbZrJMFxWLkoLG0w-YmMA4VzvV35iZj3q9jGwQPZ16mEUEQQ4EnLYNChYuHkr4IOcsuSr-YILKhKJRAK-phCMsDKrOntR6duQc8C42QZ41wug0glZBPMnkw7Vnw4Qg7CL998QTL-AsLRIThMllQKA_OWWqyd3IQ3kV1_in2TGy0UqbUM953iSSO9pd-8aLxzRAzobwlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89c12ba90.mp4?token=AOPAVyoatbtCMAQFPci_tBnQHe0H4gfWtB0yXakR-9M7mgl_yMqpHHKNQ3pZG7zrvy_IDYhgCbNrTQbuoTczeF5hfIgT5iW7omwbXkWavu3YMvOSjo8jEz6wE2LqzTl98iEBhHPxtF4dYWKbZrJMFxWLkoLG0w-YmMA4VzvV35iZj3q9jGwQPZ16mEUEQQ4EnLYNChYuHkr4IOcsuSr-YILKhKJRAK-phCMsDKrOntR6duQc8C42QZ41wug0glZBPMnkw7Vnw4Qg7CL998QTL-AsLRIThMllQKA_OWWqyd3IQ3kV1_in2TGy0UqbUM953iSSO9pd-8aLxzRAzobwlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی‌توویژه‌برنامه دیشب جام جهانی پدر تشریفات‌ایران رواورده میگه تو دیت اول چیکار کنیم طرف خوشش بیاد و مخش طرف رو بزنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/25836" target="_blank">📅 10:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25835">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlHEZ2BU8gHW554_9dxDtQRm80dMH1UXyQf39ZH_jwJ9Phy41HSOrnZhFru_HaUt2Ku_ckGA1Fncvm4g0jcZ-OKO7GNt7S_xQ6eKVaIee13JkpB6trA7MAFuCsHNMTJbQmA5FSM2MGoxwwoAaFygPQzQQcctcqbKsIoDN0q-ybVJoL2OOr2XW9MMI2fUYo9KTYnCouvp3Am_BEhn4MiKyCFtX91FKLowPaPKPY-DY16XMWbM0e_KiCT_FeT_4pHn0Vy9q86DTljNhVqMay9BTapd3w6jNCOl2h55z7V0jeWpoFDaNRJrIvFFAlmYG2GjiVWIsUAbz8wHANxbZ9kPig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درآمد تیم‌های ایرانی از جام جهانی
2026
🔵
استقلال: ۱.۱۶ میلیون دلار
🔴
پرسپولیس: ۱.۰۶ میلیون دلار
🔴
تراکتور تبریز: ۸۸۰ هزار دلار
🟡
سپاهان اصفهان: ۵۲۵ هزار دلار
🟠
فولاد خوزستان: ۱۷۵ هزار دلار
🟢
ذوب‌آهن اصفهان: ۱۷۵ هزار دلار
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/25835" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25834">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/892cce16f4.mp4?token=DI0ERWI5rGqVuNd_nmd7j5zFV0TGNrDgw6WidperlUbFqHSgwOsJsURO9DLjXTR0N3GVlHA9_NeyQrTbNmEgkYPJkpymZP1WYq3D4CmV4FffuWQd2V9IFmcpRC6YTBTcj2dT7s-zw4wKLDjY1Hj1aXN8Ico-XP_KTUgyQk-Im93P1JcQja2D2hnDG3e58URZWseBaz4fzJQ24Xfr5oExeyea3__hJvu6xYosqZDAmcXscOuFnhgHroW75OqW7ut4bPO2qJepgp9s6cyJKmcdFdpc3GJQKe-vo0GeHKC_6vcfKBjViGX42e_fNY1LoYNX9oWf1LI9xNWJqdfNO6OfQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/892cce16f4.mp4?token=DI0ERWI5rGqVuNd_nmd7j5zFV0TGNrDgw6WidperlUbFqHSgwOsJsURO9DLjXTR0N3GVlHA9_NeyQrTbNmEgkYPJkpymZP1WYq3D4CmV4FffuWQd2V9IFmcpRC6YTBTcj2dT7s-zw4wKLDjY1Hj1aXN8Ico-XP_KTUgyQk-Im93P1JcQja2D2hnDG3e58URZWseBaz4fzJQ24Xfr5oExeyea3__hJvu6xYosqZDAmcXscOuFnhgHroW75OqW7ut4bPO2qJepgp9s6cyJKmcdFdpc3GJQKe-vo0GeHKC_6vcfKBjViGX42e_fNY1LoYNX9oWf1LI9xNWJqdfNO6OfQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
مقایسه‌عملکرد لئو مسی 39 ساله در جام جهانی 2026 با لیونل مسی 35 ساله در جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/25834" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25833">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03c6d437ee.mp4?token=vq7baF_jmKQ7Wi3NLdxaWGWIQ5Y1JPIe3GRVjiNC95914g9hb0qObZyv3ejdMLPxNnCgTOjYKT1Yzmia3iDFWmdiEGG252fiJR_E6ZPFgaSFmqnaa7aq9ephXVHlwWnspEAMWgSZpYgsA--JNPgLRP4Ne4RNflcYcZ4UuTqzqApcCZqyo-35T01NXVJbujW-ENSxPgADUi_gUdy72WsS1j3Ni3Hrz-G-ij0LZQV5Dx2mxuL0ALz9kuMPi8hSk1mV7dXwewO_HN0bJSxOLsTF0LmaluAG90izH2Xag3jgJn4A_47NBy1dj2S8-QAOhA0ADvMOAKchJFz7iw1mMZe8Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03c6d437ee.mp4?token=vq7baF_jmKQ7Wi3NLdxaWGWIQ5Y1JPIe3GRVjiNC95914g9hb0qObZyv3ejdMLPxNnCgTOjYKT1Yzmia3iDFWmdiEGG252fiJR_E6ZPFgaSFmqnaa7aq9ephXVHlwWnspEAMWgSZpYgsA--JNPgLRP4Ne4RNflcYcZ4UuTqzqApcCZqyo-35T01NXVJbujW-ENSxPgADUi_gUdy72WsS1j3Ni3Hrz-G-ij0LZQV5Dx2mxuL0ALz9kuMPi8hSk1mV7dXwewO_HN0bJSxOLsTF0LmaluAG90izH2Xag3jgJn4A_47NBy1dj2S8-QAOhA0ADvMOAKchJFz7iw1mMZe8Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لئو مسی توفینال‌وقتی لامین یامالو می‌بینه: تو پسر حشمت کی‌مرامی؟ می‌دونی چقدر رو هیکل من خرابکاری کردی؟ امشب دیگه‌کارمون‌رو سخت نکنی. به نایب قهرمانی راضی باش قهرمانی برای منه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/25833" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25832">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-wxsrMvoHxUvf-71q7NKtCTbAJEPCurChmghrIrb0t2WG2JPTxtrhNmRzE6_JDWUwEg25Ye27BUfOGL5SV7xrUlY5dS89FwKe9zey2ZRbstfzS_sl0tLwLzKGWYDbZz48q6kK6JZkkU7cByA_za0_K1y6RjJ-FSCVbDGuv2wK9vcrxks5Fvaco9AwafgIIHoLA55mMFFLy-wCNnvhXA-L8baMUe-Ie-nREPk4tcm9CChNjJB0lp5CU-JKcS8L1b8GqdWtTg6N_rauzPYfWFqwVDgRFxSghsvenulTrbWG-bbtbZP-NimXP41ggOX1_KXpSdxU14JYGAKXGj6kFyIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😈
لذت رقابت های والیبال با بونوس ویژه ی وینرو
🏐
🏐
بونوس 3+1 وینرو مخصوص والیبال
🏐
🎲
با وینرو همیشه برنده ای
💰
🎰
با ثبت سه پیش‌بینی میکس با مبلغ حداقل ۵ میلیون ریال برروی رقابت‌های لیگ ملت‌های والیبال در طول مسابقات،‌ درصورت پیشبنیی اشتباه مبلغ 5 میلیون ریال‌اعتبارپیش‌بینی رایگان ورزشی از وینرو هدیه بگیرید.
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده!
📩
Winro.io
معتبرترین سایت ایران
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr25
📩
@winro_io</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/25832" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25831">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxN7ur9a5kGRZfX3oKfvVESzRdYp2FgRCBpiImiSWKQvEnJEl7OuyfpxdJnKcEPUqegLX8tUx5g2qZeY1osOC8tNR1k5up7WEoFyLV12u9ByFA_36WFbBPVr59tqYWHajhPf9g8Y5aTFYzEcvpU1Y0zDBZsLpnrSs39TyQo04YVmo6FJcYD0RJbSid3Ymp_0cZJumc89gGY-iH3lr3ifSJ-hQgld8jtbtNfcY4aPohNPhfYlck4jwIqIwB7yz0VionxGHQqkm1VT5upUfoR2dLB58siXUttVQ4ZMz39L_-9x2tTDzYYafYFFRYzS7sl4k6Gy8x1rzti0aVaQZSV-kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الان‌مسی‌داره باخودش‌فک‌میکنه که کاش همونجا تو تشت خفش میکردم که الان برا خودم آدم نشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/25831" target="_blank">📅 10:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25830">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/25830" target="_blank">📅 09:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25828">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CNtAdh3bGZl3fMS_dx-QNlSR8Iv0I7hE2E7u8zYOPpnT5Wl3SgbWvzUGFltaJzW0Ax-WBkhggiiBMWr66AWsvHE4wz9doaMp6IrInWPx1u8EJ3RmIDHT3DIIs2LLZKj6DqxjqyTBW6o0ipxT0aWyTIL9LWxrLaaMwY174NoL8mSADK6rYX_CBtYKoqfzi7NRm6XTApcxgkQqjcgxw8ybdRZgWSbWyySWtl2SHFwGmzC98sXKlRveZhD0jzhGSWoGlrznSUNa_TfkcQVsospDW1UcXyK_9LOttyIj5DF2tk93hhfhGTsvylIbHOzjNh1yUK5JrUgLWhErqFDwOGOWEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iiAuQ3BaIq9hKiF6RGR3TcTNdx0zD8dd0GeOisXYVgFIV9AvynnTOQHlQZiGkPboXjjVN_GxYOjQ_RjZaODgJhjqqCEgh_wdzSwcRu5RLGeGuZUEwgPb1AZ-L-zoZSlWxkn--5tHM7Npkt6jcxobbF3FMdXYuqNYAVMK4mh2hBohPQIAgRpUyvHkjz21yoe1XEbSrQj6jmwlvxNk03Ae8kB_lzyCNYbDq-LL0pk2bjWu6LPIEBt5tNGEGe3bDmPfe76buPjQ0nYKrg3YjjjDPrbUE8v6QfUYmzqKTWjeSs5t9HbET0h8VOqfUkmyF0HEWU0Y4LFCNscCenEFGvg9Jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رده‌بندی برترین گلزنان و پاسورها رقابت‌ها پس‌از پایان مرحله نیمه‌نهایی‌جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/25828" target="_blank">📅 09:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25827">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdia6c20Ki5-Afnam729_DG2azoxNYEY_1gGk84LV_UAHCB1T3Y_tfx0MVFBNYgUzV64wg3aB4a9DG3OWqAIeLedHojl8mk53nwC-xjaecRcZq77FGPLnWe6VoWgooke4xB_KEVDbFHcdZTKK3-N7gXpuC1OuvwHH-LQs8U0H1GL44XyjMHHGdDDQ2vYxNK5OvcTX9K1SK9sRssBT8owReR45y4UCsF9OIBh2KJBeqBlLGe0U99UNepCSThMmmceDxioD2Gt8Bz0z5sPbseGSPhvm45lKp9K5ryo3fBAPIPiSHqVZIX8EdPaMj_TuZT4cKQBFBfu-sN3YAni1XpV-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
هری کین:
باحذف‌ما من دوست دارم لیونل مسی برای دومین بار قهرمان جام جهانی بشه. من طرفدارش هستم اون سزاوار قهرمانی دوم هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25827" target="_blank">📅 09:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25826">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa7c3766c7.mp4?token=n964TUpWq9opqFOvCBWFqpACldHOdPULumBR6lv1RgKN4x14wnZ5cLj_qtlGdcNNsNu_L356qJJ5vGjYb6cGyGgd-lImXXF7aYfu4bLThSKdshn72f6XmtnljjagQQa2m8g-D-_QQ6Z4qKvtRMXyncdFS7_F9PDjcQ65-RusAE_tVWQSnWR3iq3ng1aeCplhtyuRApLhWBI_8gIut51Q_lnsePWFEJOgzfLVXccd_Xnvicn-FwNbhUUxmlRS_A38GgSIl8b7NMbuKmNWtoAltrihhWiQRFBdP2Ov13FeDQ1ENPVa6s1s-NQy4zN3kOFgp1E0IqtisohA7--LsiawlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa7c3766c7.mp4?token=n964TUpWq9opqFOvCBWFqpACldHOdPULumBR6lv1RgKN4x14wnZ5cLj_qtlGdcNNsNu_L356qJJ5vGjYb6cGyGgd-lImXXF7aYfu4bLThSKdshn72f6XmtnljjagQQa2m8g-D-_QQ6Z4qKvtRMXyncdFS7_F9PDjcQ65-RusAE_tVWQSnWR3iq3ng1aeCplhtyuRApLhWBI_8gIut51Q_lnsePWFEJOgzfLVXccd_Xnvicn-FwNbhUUxmlRS_A38GgSIl8b7NMbuKmNWtoAltrihhWiQRFBdP2Ov13FeDQ1ENPVa6s1s-NQy4zN3kOFgp1E0IqtisohA7--LsiawlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های‌عادل‌فردوسی‌پور درباره‌قاضی دیدار فینال جام جهانی: شانس علیرضا فغانی بیشتر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/25826" target="_blank">📅 09:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25825">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9lXZvcrh075sKUa6sam2SEk_czKY6v8eXq1JnhDkr253GTl-0dWKjcdCga0DlQv9V1cvMLhBL8szKtQIOMNi2UbtyxV9rZskq_FWcIxVxMVSJMcrHgd4_hpuv6_rT5FmqXjo6n7pGmVccSeE-HaebmlGZHb7NrkPquD5RSGY_5T-OBPLsZRskyTCRB1XtBX3m7p9op7FDQ-3iTTcHKMUkTG3YSn0rH17E-Ro9U99DRRjMsk9KJ0YiguFEenlFWmz5OIQq1LcMlGCPzrkjYAaEg66dCyxnz6IYoi1uT091TUBLdyAk8QgSiB8S3eiyVDNcr7Qj1HT2FciS9-f_BOtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
#فکت؛ تو تاریخ بنویسین، مسی 39 ساله، پرایم هالند، امباپه، کین و بلینگهام رو گذاشت تو جیبش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25825" target="_blank">📅 02:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25824">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UeBOCqL_BuXGyJ-X4FtlDE5cNujQjF_dHr83Zw6cWjuHcl9SVJ0Fh18yRddl83MpCWS8X-McZNHVxyZBY9v2YJcQfK1dyretF0P_uX_UiubSRZm92_SnWIUXwsU8l9lxvSzsqEmK-L0G1Q93rRn6dWX-9fus5-gUpyArKY7s5Byr4dqDumDHf-3TVHeScb9YtBM44LXCP7t0BMyAoq1mtjOcnkE2PLK2-BXSckMcQ70X5QrcxZS3bYNUoivMs_SRioa4H4_lQEghDBYEO7UwWZSQ5gHje4-barPalkP1Tr7tRw-P1dUK20MEsiHR_0L6NWgmGxbWso5X6qxSJXCxrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه ‌تنها دیدار‌ دیروز؛
کامبک دیوانه‌ وار آلبی‌ سلسته مقابل انگلیس بادبل‌پاس‌گل لیونل مسی؛ جام جهانی 2026هم به‌آخرش رسید. روز یکشنبه 22:30 فینال و قبلشم بازی رده بندی. بعدش یکم استراحت و آغاز داغ رقابت های باشگاهی در فصل جدید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25824" target="_blank">📅 01:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25823">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e18a8789.mp4?token=ilKLh1qY5_zybsyE4-CEYaZ6FjYKOczF8qGHINNOB2EhP_1hM4V1Bi5-6BMY9Kyh21cbPRVdwtyrNKojiKFoj5xXbaW-UMRyPPbwGJM1IVYnnBsM8h6C-udzj_blUrxUemU4q5tlymLAsWH_IjCfRAH8WxG8mWOvmNh8HMLgmKB1qKLuo2PkPJ8kzeIfCyKtvlwlvm8nO2sGUHEdNRxaRfm_pGS_gcD1oKagXxVTaXllJ525dCtEdfEvei67N7AaP8RNeXMTCLNyG1zCDlheCCCWV2YyqTiQhBQN7rZnlZj6rYyFanO8o3ah8mPZ8FhmSlsuz5rF45R_s9F9i_rvYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e18a8789.mp4?token=ilKLh1qY5_zybsyE4-CEYaZ6FjYKOczF8qGHINNOB2EhP_1hM4V1Bi5-6BMY9Kyh21cbPRVdwtyrNKojiKFoj5xXbaW-UMRyPPbwGJM1IVYnnBsM8h6C-udzj_blUrxUemU4q5tlymLAsWH_IjCfRAH8WxG8mWOvmNh8HMLgmKB1qKLuo2PkPJ8kzeIfCyKtvlwlvm8nO2sGUHEdNRxaRfm_pGS_gcD1oKagXxVTaXllJ525dCtEdfEvei67N7AaP8RNeXMTCLNyG1zCDlheCCCWV2YyqTiQhBQN7rZnlZj6rYyFanO8o3ah8mPZ8FhmSlsuz5rF45R_s9F9i_rvYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25823" target="_blank">📅 01:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25822">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🏆
تصویرجالبی‌که ESPN با عنوان " لیونل مسی و بادیگاردهایش" از بازی امشب با انگلیس منتشر کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25822" target="_blank">📅 01:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25821">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f50m6cHBtXJWTXWSHgZ7UCVoHxwDVv8fMWy_1SXP9wcF5m1fVLVArMCYI9qtnKILEufiG5tGcCYbE4mq30BSl6WOVM-SpsxzVRTSsvAmZNVeciT7yWioGwlunYBRNXRX5WfFe_BV3_SURnL8YffcEMml-xh8tdC0DI7jpoRIu0JkgIPEKGHACM8EGU7X8gVR-MNgBS-cIveaS6u9iSZXDoHhcfzkhYYEqy1fR2lyPxFLtxu1Ya91NHmH_3wW3dt5fsiyvRHL46PGXHD7gwAT2Iiwy24JGj57C99A-YYPebKOaHPaxRPUdHry1vAvmG1EvRvMgHM2zBRFTxGGb1T3eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
انزو فرناندز ستاره آینده رئال مادرید با این شلیک دیدنی مانع حذف آرژانتین از جام جهانی شد؛ دقایقی قبل هم گل دوم رو به انگلیسی‌ها زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25821" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25820">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efd102a0a9.mp4?token=klQZEnODpgP3eUGJNrLhZezuQJbZnqM-XF0_V3lKNKnavIkorNZRSka-ORy8971LRlWN8x_AwyQy4Sy7KwJIwli94ElUgvcCwy_x7XGez20bb2M9TKTG8xQjy9ugUZTdWs5o6uzeteLplz45eJlC5-4xmM53C4uTaElehNjyJ32CwCi2OxIS08jGwSsFhsVbQrM4GZ144R7q0xkKbetDTpKoRuFlbvqPmQSIFapE3D6gvGLankYq55JxL9Z-duvfh8VwOxwl1RfZuFxMZc3XczSTizXt7KPLT5_3sX2cV_I0MbXfZC55fyzZx8nK_4-V7wks-AN2EVWb4v2PB7Bo1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efd102a0a9.mp4?token=klQZEnODpgP3eUGJNrLhZezuQJbZnqM-XF0_V3lKNKnavIkorNZRSka-ORy8971LRlWN8x_AwyQy4Sy7KwJIwli94ElUgvcCwy_x7XGez20bb2M9TKTG8xQjy9ugUZTdWs5o6uzeteLplz45eJlC5-4xmM53C4uTaElehNjyJ32CwCi2OxIS08jGwSsFhsVbQrM4GZ144R7q0xkKbetDTpKoRuFlbvqPmQSIFapE3D6gvGLankYq55JxL9Z-duvfh8VwOxwl1RfZuFxMZc3XczSTizXt7KPLT5_3sX2cV_I0MbXfZC55fyzZx8nK_4-V7wks-AN2EVWb4v2PB7Bo1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
سرخیو اگوئرو که امشب بازی دو از نزدیک دید گفته اگه آرژانتین‌قهرمان‌بشه به هرکدوم از بازیکنان این تیم یه گوسی آیفون 17 پرومکس هدیه میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25820" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25818">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2iwRwMJlCVSF6652pgc6cLYWd7BbT5qZrwbqwyxWPyqnwKdYNMqg1x_iRW1yPbfDPUk8GfHa0yyx2Imj3J18Cu_0viZaqGSx8iDL9dn63OWUAbKl1hQbVlj4P8QWKYGdwUhvnt5b68zm2DvwUUmPA4Aymx7T1uu7QL46FktQ8nxg6hgLnq37MEyzo869Ef5_QWJj5-6hBu9zaBQuf3lOaNNGXSu66nZmbNOw1P6Zw84QJeOGaMRfME6gsUoFkYAF9NKROmk5AFcjP_Q7bJh_rgq4oZFejofXNzImisw9tj71oOpCk_pf6gj4XIGXTtMAwFvxIqtinkV_ssjVhQihw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگلیس‌دقیقه۵۵جلو افتاد و توخل درجا تیمشو تا منتها الیه باسن‌جردن‌‌پیکفورد عقب کشید و ۶تا مدافع گذاشت تو زمین‌چون میخواست تاخودسوت پایان تو محوطه خودش دفاع کنه. تمام این باخت گردن خود توخله. حتی اینکه بعد از عقب افتادن هم میخواستن سانتر کنن هم تقصیر خودشه…</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25818" target="_blank">📅 01:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25816">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-hs7O1glCCaULC8PljxyTHw0x5hAL8Qc3mSF1zG9-zv-Ewrjthh1jn8qFAT0gXjfWeVAXQO8jjOkg14QWG-FonNDYsvkvATEqLuxNjNU-TKa2QZTEODx1dIYqvlzHJAnZseEBstV23WJuaHpkJbfuE6UWhZ6ZLpIi2KlEovq5YVZ6tMl09rCl-jfJbBGg7KlMzGlV1CTILPwc8ZOxJ561BZsryuWZcjjScY7EPVIXaUYY63vdnwWlPp2n-UIKIYUJlx0CQvjjhxEVxCT2XSJloyOEvTE2oPEhCzhAuiOdrYH1zeAoWUpP_RljvuID14cISJ0rC23xJqnQQCpU3fiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
بهترین‌بازیکن‌جهان؛ اون‌حتی از جام جهانی ۲۰۲۲ قطر هم‌قویتره. لیونل‌ مسی همچنان به نوشتن تاریخ فوتبال ادامه میده. عملکردش رو ببینبد فقط.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25816" target="_blank">📅 01:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25815">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHXeCs1qSo394PHibhf0u4z_RUAusX0FzaIiqF3gIS1sjp3OfCdagyT6QpiatJ-y0O6HhL9W39sDjW65EybigbV1X3-5zfpoKKvydbkpcq2ny4R6_i7Wu-lJGKBNb61RTT2qD_RJm4clcpY9NvxPhjR0YEQi89qcRqxEBVeV-DRV0fBPGGB-BcNYMP60Ekwh0EJ0UidmujvcFxB6lz5JYSabSIank7PQT8XXUBV2p2DfJvCbHJQFLXlRlj9AAJsuvkLfgkQ26Tym24sCaBBW8fejiGwBy8mh8d5gGMhOvD3ilNblgxa5Xvp4xYjQvcahnCcSDnCV51wqBVYNmgVl5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال‌جام‌جهانی2026؛ روز یکشنبه بین دو تیم ملی اسپانیا
🆚
آرژانتین برگزارخواهدشد. امیدوارم قاضی این دیدارحساس علیرضا فغانی عزیز باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25815" target="_blank">📅 01:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25813">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhWqT5ubf6XyLfAzsBaaC36Vz_1HGCHG6aSWWn-Rho4wX2E9rzvCOSkgv68XmYY4kxQS33cG24c7sumi6RrXdmFf3tOa-hdboX8u8sNZON95u7ku7YrZiRlFddMPeD2kxZI2yko4LwLNaMK5l_JaX8_Q1AORMRO8TiwmAkNU5bAcpzzBN0NGW-B2eQWD_RFGsAfZeqQUHvcVaqbQkJHr5RqAeDz3DFe3-PGWtD7ktdRbjhCBIanDxj6aSAeAASklWFveefCYX3znkorl76qsWnblK0msQ_YYpWE-PBAPL0hEPvTdMQz1f1VtENX-eX6Zt7E-U0jS7WwwZlfzjTibPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25813" target="_blank">📅 00:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25812">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMgmXdAsXO0h9-Npuk4A81FGA_aA0tjPaZh3upstSiYPjSbmDBmG_1ll2EVOabLjhj9Aw6SZa6kK1MvugpiPbjiQRs-aAhxNxBwySkB88y61AreVdtAbQ3Vb-yRrfitUDMkP3kOib9vGOIehk2-9IYjN3UG3rBPqyjo1IZDF6BtSwxecNjUsG7HW-vRHiVZTsB0igAYxh2wNXJgqk4J-PMmQgOR_b4on0k1e5lo1z1bOTzmmohjwMgJV2vr19rTG0qgmpNMvBXHDdaWghQ05JYXIYuaYQP0iGh1BRMNxCX7CcaFf7KvdboxdkAbjSb8sQ7VZwPx7Tn9t38SmFihLVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال‌جام‌جهانی2026؛ روز یکشنبه بین دو تیم ملی اسپانیا
🆚
آرژانتین برگزارخواهدشد. امیدوارم قاضی این دیدارحساس علیرضا فغانی عزیز باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25812" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25811">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKRsj77SW58weZ-aGFni8nJYHHe5DU82tkoMp9OoqdSeAQdp4y0o3bIMeXBL4vIvZ8eca0oV9rffGKVWQ49EzCGM4Ooj_fdcUVMcZJBwsPj86RIef9oZ3WAf09MWCi3v8Nv8OyxY-dpBwth28tfKB7zS-31qf81PFFjSzShWx_V5v_Pco2dvJLmhmdUUQ4xJC_1ON18kE8eiW3j3iZpp7yQ8TAXsvoB0gFUfImRuOht4wpZeTDPbASWzlVu1uKwcXxgJCKN6PVAG_GVO7m7fBpG3Uazc0S-bHHoneqOkyAd2wr78CfPdmaDVGeOf6I4tDgxB1rYhuzA_cAdivSSgHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه‌نهایی‌جام‌جهانی؛ صعودتاریخی و دراماتیک یاران لیونل مسی به فینال‌جام‌جهانی بابرتری سخت و نفسگیر مقابل سه شیرها با طعم کامبک.
🇦🇷
آرژانتین
2️⃣
-
1️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25811" target="_blank">📅 00:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25810">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldqP8a3HP6vI3XGPixbbex8Ti8wLlDtRhlC0SgHMBSNskw_O9fn4Lcno6x0qQdCWtqXFl0nMRRm9dsxYQp29Co3Pz2B_IiE-D3fnERJeWLohIMJGIOJzg_sSRSPzqU6FsOYNwAiueXUVyGWxhpDtQGlbS_0EkM3ZM6g46bexo3EJke-W2FDuwqFE5569pNJap45ZNQbdfrRY6u9K37RHtBAQhIPy72cvrmVHlLK5Md6MwXlAX-EjQPPSy8fYCPQex3unU4xXzeflSEX9PdTd05EPji840H6Tst0QddpoXSVtEwiOq0QV_9ZRZdKYes73OO_gHYsDoiREkNGeIfwz1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی 39 ساله با دریافت نمره فوق العاده 8.9 بعنوان بهترین بازیکن زمین انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25810" target="_blank">📅 00:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25809">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8chFqgshgy9yqc_z87C8vxVX9RNflKHloQx5fW_nQ4ugOx0XAAC8ovqYaRlXEL2e5SccAp9rUK37pm1oA7u-uy8ghVLBVBgZHDbJH4cyVT1-d6xiwC5IPlj1LsYp_mHM09UFSRmObzpmlYPeIqmDRaCtfzfqObXjYzfLaX0srQlvvj0VCvvcoGJQZay_km8Jmr4VAPuZNBH5bh0-VXtcfoz7pAPCetEV0l92vHjHvwcW-BGQcgYIK9ERvnHGK5c97iJ0AZeqj7yZTwK-8i7_HHjOL_HfSitF_Ay8xzhfFfZYSFELlhY-QiJP3OKKHvQ4tj4LXU4ORjML4qmAeXLlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی 39 ساله با دریافت نمره فوق العاده 8.9 بعنوان بهترین بازیکن زمین انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25809" target="_blank">📅 00:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25808">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0O5DzjrNyQppXdfeXPgRWzEdQ3jE88eBtt1j_8nAA7jKupDPpnXVTQILPBQQst5RQSd4sYUQiGN20cFWNzvkLx2TTMMsWtuub60L3hOF3F2MYNcC_zRVL7fSoovbjMfqVKDRK_JygWt503hIUrTOfCZdwHRO-Wi_rIdypy83-Cpg7WwLXHowoQHozsLtwgPXwYkyM09KOgX00QoNwLExvan5l3PlOYY7gB07Q4jPI3eXr9hfksom6vZBcBFCGcsrlHKm-gasJ6mlxdqFC0iqnC-Cz0aSoYETCmU4w2bEtuU4lKRKSz2CX7E3EYU5n9ibYo9DSAcGH63lnnQH8iFAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه‌نهایی‌جام‌جهانی؛ صعودتاریخی و دراماتیک یاران لیونل مسی به فینال‌جام‌جهانی بابرتری سخت و نفسگیر مقابل سه شیرها با طعم کامبک.
🇦🇷
آرژانتین
2️⃣
-
1️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25808" target="_blank">📅 00:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25807">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4Gj_1DYneEPpNTJzP3ERbkRxvF2bpLgq5tYU2m6ZNLNAkPRKARqSJT4d5QUEKXqYo9wmXhdpzRcTrFDtpUL-QlDv_O2Z0yI0Pr1GQWSNWWcxM9RGAPKvtXEa-8mAinSVk6Lq1-kujTYcUnQv6qWmxKhFQkAlwr8n1yozzgxlaKuTgQtZ8Vlu6iQUNEbll1vPmPjHEZHhfNqD-ffJzJlLBSkkDMxS0SXByX6aP2oJrQvbbqUftXgF8y96XRercXTpMhNtybQWXcOa2uowB2SW_1yPOfYPgwOr-njm4n-50fPlTOCewK7DVz5mEYNhPl-1K5lkTrvMvShaUSM68d3Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
گل دوم آرژانتین به انگلیس توسط لائوتارو مارتینز روی سانتر فوق‌العاده دیدنی لیونل مسی؛ این یازدهمین پاس‌گل لئو مسی در تاریخ جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25807" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25806">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d89d4e5750.mp4?token=Sz57cEqqWkMKu1ENkup-mZ9GCVCKhyTQKVInTmcPFA3s3Rau-T3pDDF69CQantzgoME_EXp7Wo40cS0NCNXdZKJSKpZ7wvKqUYVKgQMDTfdTOP8Y3r1RDjqxxrm38YBvSh7RwpG27lf2QR6VnqfmgPSRzn-vA1mJNJRx1rfR1mOclAj_MDAy8KjCBpJVLGK0HDtfQVDLAAS7-14bRrB_M0zEEfNoUibX2ZRHMcBAJqM9XS_6l1R9-uNK1p7oQCTcLh_bYG2K30x_MmRA9GHTVA06bIy1QBTjtcCv4KeF_vI-uI3sh2ShbhT8wd437tziBuuIewrxFJaKO7tWci4ubw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d89d4e5750.mp4?token=Sz57cEqqWkMKu1ENkup-mZ9GCVCKhyTQKVInTmcPFA3s3Rau-T3pDDF69CQantzgoME_EXp7Wo40cS0NCNXdZKJSKpZ7wvKqUYVKgQMDTfdTOP8Y3r1RDjqxxrm38YBvSh7RwpG27lf2QR6VnqfmgPSRzn-vA1mJNJRx1rfR1mOclAj_MDAy8KjCBpJVLGK0HDtfQVDLAAS7-14bRrB_M0zEEfNoUibX2ZRHMcBAJqM9XS_6l1R9-uNK1p7oQCTcLh_bYG2K30x_MmRA9GHTVA06bIy1QBTjtcCv4KeF_vI-uI3sh2ShbhT8wd437tziBuuIewrxFJaKO7tWci4ubw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
انزو فرناندز ستاره آینده رئال مادرید با این شلیک دیدنی مانع حذف آرژانتین از جام جهانی شد؛ دقایقی قبل هم گل دوم رو به انگلیسی‌ها زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25806" target="_blank">📅 00:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25805">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0c717972.mp4?token=SFo_BqbKb3kgZofhdWQ2QS_HKgPqpvVELJ5cfd4YjquR1Qiy_N-WGNHEqZkW3L4H40e6WVQZRHvgL1RALVcqPjUs1wNCP6S6DX4iu4ojF3lXLVOhYihnkdg4lFCKWueDnRMNKDRPgt0LbUYy25r7PXxenblh12Hc-pWyeT99rlvdOGPtElH2gBZZjVU51gp0Td0khNkZahOkngVha7cUfriuZUSzrgxnn-5GtViihuCHI1bLY4_t56OQo7SzVik0rj-HcA-CP5Nh5dHilMgqxRknFjndKQmfIZ43hwXFusCG9myI9ljc3lr47I5i-o45ABM5LakV3CfUzYs0FYCs5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0c717972.mp4?token=SFo_BqbKb3kgZofhdWQ2QS_HKgPqpvVELJ5cfd4YjquR1Qiy_N-WGNHEqZkW3L4H40e6WVQZRHvgL1RALVcqPjUs1wNCP6S6DX4iu4ojF3lXLVOhYihnkdg4lFCKWueDnRMNKDRPgt0LbUYy25r7PXxenblh12Hc-pWyeT99rlvdOGPtElH2gBZZjVU51gp0Td0khNkZahOkngVha7cUfriuZUSzrgxnn-5GtViihuCHI1bLY4_t56OQo7SzVik0rj-HcA-CP5Nh5dHilMgqxRknFjndKQmfIZ43hwXFusCG9myI9ljc3lr47I5i-o45ABM5LakV3CfUzYs0FYCs5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نیمه نهایی جام‌ جهانی؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25805" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25803">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db22288ce.mp4?token=kmbbikU0WTnjhJL_YKF0jtbMKPt_W2LplON_zwEKbL0XLa394PdbQDZ3GfppjqX_99PQIcFRv_DYNqZqyAoNnV4OX_VS8K5BDy8yN_oHiNNMJ-yAzKfN0oE3TP88l3yp8ikVNrKEE3-6PNa_ZzHi9q-b9o7CPKuvstvWNc3ZBal8hkCk-lBXhZ3X7B99jE580Gm8Hdcw06FrKSeJmMgIPySFZbHfZYLI8mlELrzMUtDMaNF9zhSJdKnwYmiqgAnCPi_h_0Ttw59n8585U70ORh4QDASQeDv9XoqaIv_hNDWD1d0Sc-PgxxEj93V0tLY7dz41QxhHWOE21VSutEmtdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db22288ce.mp4?token=kmbbikU0WTnjhJL_YKF0jtbMKPt_W2LplON_zwEKbL0XLa394PdbQDZ3GfppjqX_99PQIcFRv_DYNqZqyAoNnV4OX_VS8K5BDy8yN_oHiNNMJ-yAzKfN0oE3TP88l3yp8ikVNrKEE3-6PNa_ZzHi9q-b9o7CPKuvstvWNc3ZBal8hkCk-lBXhZ3X7B99jE580Gm8Hdcw06FrKSeJmMgIPySFZbHfZYLI8mlELrzMUtDMaNF9zhSJdKnwYmiqgAnCPi_h_0Ttw59n8585U70ORh4QDASQeDv9XoqaIv_hNDWD1d0Sc-PgxxEj93V0tLY7dz41QxhHWOE21VSutEmtdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بیرانوند: چرابعضی‌رسانه‌هااومدن‌گفتن مصاحبه‌ های مورینیو درباره من فیکه؟ اصلا فیک باشه وقتی می‌بینی همون‌مصاحبه فیک داره به من روحیه میده چرا توهم نمیای همون مصاحبه فیک رو پخش کنی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/25803" target="_blank">📅 00:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25802">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Foll489KR0HQTxJLJ_OlI4mbl9X9Rh8Uc_qIFGviQ-Jd_W_cjQX10smKmB0xm6fynZ1-mQ-VdvTWpmZFVmGinWs0nKs0acZHbn4dATX1IA-tjKe1fHvixcrpD7kQ4pdalLnyTm0pe2fAI5Q_4DmQtSI7N4r-CK_pohSZEF20Fkc6ZBO3vfqk_VYKi__LbnetHfSP5YWVzI72yeka34bRdcEL8XKxYbzX8_h1yuIQO1ds_2s_ZX9iGB9KD0olCsec7eqy-z5ePMB4108JV5OHjve_f_CqUOGbN0rXaCU_d1YaLHcBdui3Nwv7y_Q2uKLL4YkrM90Szeqcf25tLTtl_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25802" target="_blank">📅 23:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25801">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxeEkNoPohcWz-4QXLZnA-r23zCpQ0GAwF4hAuScrfLqlsQr0fbVdtcEH6OQE7gqr2y77MdYGYhrmfyVAJlEaSz42RGjKsg6-KM_gbEGuS9z25HApVtVPZpzxe4yF472WUeOMlg5GSbsj50nEQrdKW7lw7CCRK3F3G7iF1dKmeSOlyu-SNylWbGRWqkJVdTlYz-6788Dz6nO2wqpkxIYbDpDzjl1pqa5nz9VHB4ah9IVwWf5lbRXpQCezG_1DfLi15oO2DkBysk-85cuN0smeo8rKVoSx89m08pyW1ykXCy5wfQy4sXvD290Gc3W1_oakp_FZ0TnFHeCRZt9dw9wwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/persiana_Soccer/25801" target="_blank">📅 23:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25800">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3AOH2I282S789yK75BUW-hRwWT78nPSaJaUBoPeL3LIBVISLa67Sf9E0ROhxBSloH3EC6spaxQkzz0oMojyEzPpx4a2R1XjFWlPt7AeCqmM3l6gQiuwgz0WWMrJlHeGw2clEM7Kcy9QuZ1bUs4UciB23-lKYe1Y_H4HZztlN2ZXjawwZzCyUowITB4tAfjC7Y7CmbvhVuMMswjMTI_H7-Bwk-CjzyvYexOtn_fwDBsZdkkLRF-sRtfiITlAbTLuL0MQ_HS2sMPaSqOX3RanDf1aDSBP2uStyLrGHOTMJOa_y4JyXOjg31XROJrnFpSgrOOD4yWzvH67hSUfhLR5fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/25800" target="_blank">📅 23:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25799">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30d2d3139d.mp4?token=TgQCgZQ0E03Li4bNAYaGcnk8rRQ6X2lxwbJo7De6otXZQMwFMZX0ugqtGSTWZKABj2hG5YWv9lMtf7OJEzU9gd7MKuNPdgjOyaNPRjswquoYMuFHEtcWef79ibu0c2sxWeFD0VN1oqqlqUrBwMRVkQn_gnf4Xubr_es6iNxFr_yM06koiGSPCxDZfx75Mlb9573twAwc01B8f9ufoXe3pUayE8FF3-NoJjilhWgC45KWnWBdI5q3sktktJX4oylW3LQ89a1rTLdAoRUtYwhMNfAya_eph0x9IfCeH3is0vT0uEAPe-sjDOu4Dm1ZIoqjQs-FpS5ltmvw42VJkSs1TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30d2d3139d.mp4?token=TgQCgZQ0E03Li4bNAYaGcnk8rRQ6X2lxwbJo7De6otXZQMwFMZX0ugqtGSTWZKABj2hG5YWv9lMtf7OJEzU9gd7MKuNPdgjOyaNPRjswquoYMuFHEtcWef79ibu0c2sxWeFD0VN1oqqlqUrBwMRVkQn_gnf4Xubr_es6iNxFr_yM06koiGSPCxDZfx75Mlb9573twAwc01B8f9ufoXe3pUayE8FF3-NoJjilhWgC45KWnWBdI5q3sktktJX4oylW3LQ89a1rTLdAoRUtYwhMNfAya_eph0x9IfCeH3is0vT0uEAPe-sjDOu4Dm1ZIoqjQs-FpS5ltmvw42VJkSs1TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/25799" target="_blank">📅 22:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25798">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwKVUtLntgUzjvsR0Uhvp6HjgSaUsDozBY-9c3l4zpT8a8zrOTnqGxduunePUWg_HMGFDdrUDIMsTGXlTQAYxFmLAtq5vBBl1G3EmR8_USXQB5OX4RJU5tca_1Zl8L-RM6D1lUqLoj6gxZRa0I-MXFFM66ZOHwRHJ13SWODh75wzVMhXzIPmyJOifczNIF0if0W34YYf9IFAS3Xth2Kh5rnKlUbRpukKxvkyHn78w5WWV-zkl9tuJMALfhiwOktCWfov8VV6FBNRvx8RvpBucbvEltg0smc4k4Cjyn52TiK25cGx8nRgppMF5xWJlQbeAHmyD-SoqZf38YyNsnVaIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معرفی زیبای عادل خان فردوسی پور از مهمون‌های ویژه‌ برنامه‌ امشب؛ علی دایی: تیم ملی ما وقتی‌حذف‌شد که سردار رو خط زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/25798" target="_blank">📅 22:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25797">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c436909609.mp4?token=E-piLUgx4hkLPjKLIp8bqdwbdta5ppnVxZuVIKfxpoi0rzUSyQXFSuEyfYqpCiALbAJC3lbIYUC9e8eCCuhfBK9jm4wBea8y6IY8f_dGNAukL_WWrI7GoKgHPqrpouP4l9jVAKiyuK7W5MDjnLrf8j3E008tOtX_KyDtcqFqGW2e8QMgykUpTBlNYrxH8jF03S3RkSZ6lQUF-71Haht36ALNM8wswGPjJ-hGNl8NPWvdzhyoZjv4KTYJ634aMwKYq9YQSAyOcpri23O4ZjnMQsJf4pHxm4pNx8BD214htGvdDJS-26zLdjk1NWJvILhvzkGV_6o7NGSOEZqTuvsHRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c436909609.mp4?token=E-piLUgx4hkLPjKLIp8bqdwbdta5ppnVxZuVIKfxpoi0rzUSyQXFSuEyfYqpCiALbAJC3lbIYUC9e8eCCuhfBK9jm4wBea8y6IY8f_dGNAukL_WWrI7GoKgHPqrpouP4l9jVAKiyuK7W5MDjnLrf8j3E008tOtX_KyDtcqFqGW2e8QMgykUpTBlNYrxH8jF03S3RkSZ6lQUF-71Haht36ALNM8wswGPjJ-hGNl8NPWvdzhyoZjv4KTYJ634aMwKYq9YQSAyOcpri23O4ZjnMQsJf4pHxm4pNx8BD214htGvdDJS-26zLdjk1NWJvILhvzkGV_6o7NGSOEZqTuvsHRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق دستور علیرضا بیرانوند مجسمه امیر قلعه نویی درمیدون‌ازادی‌ساخته‌شد. بیرو دیشب گفت هر مربی دیگه‌ای بجزقلعه‌نویی این نتایج درخشان "سه مساوی در ضعیف‌ترین گروه ممکن" رو گرفته بود تا حالا مجسمه اش در میدون آزادی زده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25797" target="_blank">📅 22:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25796">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7lyLZBdBaaMvDxJSxggb4k3poqhWCBlxixo5oX5vMK7fNcX6fOl3Ge_daZO71H0e05i7iG9fnCgvg-UTAWXHbMb8XCWBPthXQn-kzAkQGVTazdRAIPzHk25we4ek8dvein1oaJb3_y8lJpaVC--s3fBiNa2acrjjEPqkd0aGzuc0rSVQKXD6RnR8kjfxmJ1uCZQHrHGyCo0tmzfXq9M7QsxTYLrMacSB6n3NJjECh94BqjwgL98cBe5MvlK_jLXeqKbg1t706mOcg5_lrBnKFz_577CjenV7PtFaf7yPdN17MdbRoYrWGCuPyWyIgfpI83H0MztdUKW3-FsJSgReA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هفته اینده هلدینگ خلیج فارس؛ تغییراتی مدیریتی گسترده‌ای درباشگاه استقلال ایجاد میکنه و بچه بالاخره از هیات مدیره رفتنی میشه. شخصی که تاثیر زیادی در جدایی ستاره‌های این تیم داشت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25796" target="_blank">📅 22:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25794">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113eaa3d5a.mp4?token=UvbGIVBYkpkWcKUmD0BeMMDGEnFQUOzCqoQ6IH2DGuKLTcXb_UM0t40iQaZguKWfsmqNrQBbLJDjIK-6EjlhYoRwJYMCdcoQ7eRCCXVgeG4ADhZervA-aEKT-89Bi_S0TvRJnBtS9MX_FZ582FO3NvJQON6o1akU0zedutk0q5vAXbyYv61UyCRdX97dzn7g6wRXqSrstNvGl63Yu7F8rHrWmH7kxL21LrR2-c32d6hq9SqsTH_qtj1kqSq_lHQ9aPS6GsdPyHV9V1lY3ksi8-zH4AZ3794l-ZRv5rK7cuMMyBT_YHMGdIS_NwnfHVGBQsq893CTAokvlHiE2iHVEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113eaa3d5a.mp4?token=UvbGIVBYkpkWcKUmD0BeMMDGEnFQUOzCqoQ6IH2DGuKLTcXb_UM0t40iQaZguKWfsmqNrQBbLJDjIK-6EjlhYoRwJYMCdcoQ7eRCCXVgeG4ADhZervA-aEKT-89Bi_S0TvRJnBtS9MX_FZ582FO3NvJQON6o1akU0zedutk0q5vAXbyYv61UyCRdX97dzn7g6wRXqSrstNvGl63Yu7F8rHrWmH7kxL21LrR2-c32d6hq9SqsTH_qtj1kqSq_lHQ9aPS6GsdPyHV9V1lY3ksi8-zH4AZ3794l-ZRv5rK7cuMMyBT_YHMGdIS_NwnfHVGBQsq893CTAokvlHiE2iHVEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
قابی بسیار زیبا از سه مرد شریف و عزیز ایران در آستانه دیدار امشب دو تیم آرژانتین
🆚
انگلیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25794" target="_blank">📅 21:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25793">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/558fc696a6.mp4?token=PXK5NrYmzaRBzA3okw4KOq7MlXCTABQ1qmqBi6BPgLsiy4qDlQT_-cYgOjOHurr0JRq4CjcGbyidwZCu2XQjDpkRDOUAq2OUhzRzmHel1ccsqoajmuGMCEu3ZEX3gGt_x3Ak5eVq2esRJDFUv2lzbcpoA8E6L_68cMqK8xb1K8YXCCvkT8XpvnGrxWeR59LcugcwKQayRW52sP-wMLZNHI5nwjmD7yNNd9ReY2Mw9mEtW3iVIm9Dv9TX7ekqFOifE_6mJay4mqkXqmpC2vYdHetlcK5OZ-ncBLHQLb55zf7zll7znNwPUZLWltZZa05WTExafBtKvnGFwgBSdM38KjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/558fc696a6.mp4?token=PXK5NrYmzaRBzA3okw4KOq7MlXCTABQ1qmqBi6BPgLsiy4qDlQT_-cYgOjOHurr0JRq4CjcGbyidwZCu2XQjDpkRDOUAq2OUhzRzmHel1ccsqoajmuGMCEu3ZEX3gGt_x3Ak5eVq2esRJDFUv2lzbcpoA8E6L_68cMqK8xb1K8YXCCvkT8XpvnGrxWeR59LcugcwKQayRW52sP-wMLZNHI5nwjmD7yNNd9ReY2Mw9mEtW3iVIm9Dv9TX7ekqFOifE_6mJay4mqkXqmpC2vYdHetlcK5OZ-ncBLHQLb55zf7zll7znNwPUZLWltZZa05WTExafBtKvnGFwgBSdM38KjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
#فکت؛ ‏بیژن مرتضوی تو فینال‌جام‌جهانی حضور داره، اولیسه و امباپه نه؛ تعز من تشا و تذل من تشا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25793" target="_blank">📅 21:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25792">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGFWdNDfRzLa5MAktyVW-pA0Z8oQ2csvDFpghqOyuXR-vAFO4_TwGyLNpNDkRKFdtfQcY66FzW5yU3zNbyn1i7U1twVYVkV0sxKRslnF4wkpd2uO_wAwU6nN1_ELrD07qmYIQCTiO9NNPnvsdkOg1QUPlfatW61Ik4vMvjOuw0P124nzLY-vLssq94jRwMCDVvp1H2fIke8gdTxP6gWuXvhuX3RkG9LL1YwtWqLJEc8a2nNR5jBNUoMFNqkpBTM95wuXjAa14xH56Xsay4aarrbagEMeS-IZOFSTvHcQyhYQiLKVzPN0i_C-HlC8vGkAjDvGuel0D9qfSK0iqpGiVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇫🇷
🇬🇦
#فکت؛ با دبل‌دربازی‌امشب مارسی؛ پیر امریک‌ اوبامیانگ برکورد 400 گل‌زده در دوران حرفه ای خود رسید. امار فوق‌العاده اوبامیانگ در این فصل درمارسی: 18 مسابقه، 10 گل زده و 8 پاس گل.  گرینوود هم که در منچستر سرنخواستنش دعوا بود آمار خیره‌کننده داشته: 15 بازی،…</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25792" target="_blank">📅 21:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25790">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nGN6IZs3l9NCAi37xSJ8WYwt5B5sjr5MTOQxX3WUUl2jSB9Vc6gsvsKBmXawOf3pXCmFb_1VQK1r42Bn7nKxKOWSmlTGT2y0XHBEPPDC0Pn4hP3hpYssjaE2STr3QUHoYDuwj9MLxzC2vnwZ-x2fl-NEYB5L2Ygj_vk3Bo_t7WYvJFQl4AStB3Dn4OuHOHB1gcL2N1PUs1pYDMxrsbADQXmV_pdLHnRN__pjRHq0IC1FM2pHlJGMziLEDn6uab2vpUISXkWljyI3zpxR_TORhSpXwhYvIWDBoAUtZUQxQqRpH4KToiHAf5cGvRf2-ih_lB8FwZE_wgAoLQq_c5Bq5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cjbsVejLPsd8XAf8wxvGjPtBxkUUO0DomCOq5jnElBLT-eLKRPHEiZ6zBGD8XG8AjxAp2RDZ36BQwt8uIw5PmZOPtUGBfDcyu1MchxazB3f3aiAP4urWCLi8L0Fe_gDtWHYh1LkxM9FDJqZp0otQSzaFO_QhpkYXdaOHcP-qrvCyOCKrs7ZoCLfUmvZNG7R_ok2zTgLnbtHLoVRQhAQHzDsavzkjHqfluhEta2dLq9MwpbJcabA1R6KgyEEy7-xwc6G-WY-nDQJsX4gr1lIouvW-2DgMDv62C21rZ7AqEtOe4nITYmK6wBq4uBqrCvscMdTra_CDP5AMZFa8n4RbNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام‌ جهانی
؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25790" target="_blank">📅 21:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25789">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmxbdO8iTlUNZxZtf3cr2bV7bQZOJWqk0FFBAvnY5hQYWnT-TtcNKT3502m0PhhzDNU67CQ3gkrBFSnE7nbsXEZh9VC2xwcFjat2IJ_8Tiq4eN-CWwMhrOTrW7i1-hp_6FkXZ4zQYu9CGS5xcw6An4fsWJVnz5OnI1lMpTIKRMt9UNBQsyVZY2HMo3Ij0CGk9U4WHGXSs8RXOMSFDdKMslwkQiK2nUHCt0H3-u8FqHBkgpJ4WEy3G6hCOThVo5xQNVf8dHpbARiPApiUUouHJb9ImqTwhrPj7mfJtcc_2jpk2pz0WHxLIIo34q2G5ntpstGwWrYpS1xCEetZDrCwMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فکت؛ تیم ملی اسپانیا با رکورد تیم ملی ایتالیا برای‌طولانی‌‌ترین نوارشکست‌ناپذیری در تاریخ فوتبال ملی مردان برابری کرد. 37 بازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25789" target="_blank">📅 20:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25788">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9pJIaU1syrulkmls67rN05FZ5Gpzmhq157aMZOw95waIH25K4NZL1GvzjCPK-M_w_z8B36FYtAKbHoSrXfDMw8vSbjyOf7XZGLSAi5XFPTRCLYVVhMTtqAgMQ5dZVFJz6G5xywE1JMuuBuSZTPbuCJVUFpnmr43XLljuQdZ2X6DKGrSaCi36wrPZKAhlYaamuEOR9aoDT4M-P47oSrSDkLYCyvCQF020nDioqsfBbsAMR-RtReaXZdFuPkmk52OqPmvLmMIJ63ga4tdQ-M5dv0SCN_rrjUHRklTqXbW9bmo5zTsOUHzkyW8BdYcIXS4Jz1L3DdnKh_sUKXp-a08fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لئو مسی در نیمه‌نهایی‌های جام جهانی:
دو بازی، یک‌گل،یک‌پاس‌گل،یک‌برد، یک تساوی؛ هر بار که‌ مسی به‌نیمه‌نهایی‌جام‌جهانی رسیده موفق‌شده راهی فینال شود؛ این اتفاق تاکنون دو بار براش رخ داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25788" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25787">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b4c95cb5f.mp4?token=MeOd3L0CVZboOEcacBmDsM5SpSpoen2m6Uvm8gZqUkknOsxEbRI5ZYcK2tKyJrrss080-g_qycVxUNWwfEq00Q7PbJmrrrfRfFcdzwKJyP_zhradbZtCYjMYGVdQggfrlBc7WXABedhO5EuLRZgxZc7zOF03l9ZVWsnBKktgmBd9CfqTm-Q8lucGyas08Ol0nb4zSz60e5gET0_p9XyYGvz2aQx2KuKESzfcX6MfgvKzikuRDQFzqXPb7_PE8NIkM-N2Xev7rdOMXQsDqIjAPbkbWzYguVhom06mv9Lb0XCER-hiL4VRyniMFHMbrsV0LNHevsUr0_kKw4112II9wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b4c95cb5f.mp4?token=MeOd3L0CVZboOEcacBmDsM5SpSpoen2m6Uvm8gZqUkknOsxEbRI5ZYcK2tKyJrrss080-g_qycVxUNWwfEq00Q7PbJmrrrfRfFcdzwKJyP_zhradbZtCYjMYGVdQggfrlBc7WXABedhO5EuLRZgxZc7zOF03l9ZVWsnBKktgmBd9CfqTm-Q8lucGyas08Ol0nb4zSz60e5gET0_p9XyYGvz2aQx2KuKESzfcX6MfgvKzikuRDQFzqXPb7_PE8NIkM-N2Xev7rdOMXQsDqIjAPbkbWzYguVhom06mv9Lb0XCER-hiL4VRyniMFHMbrsV0LNHevsUr0_kKw4112II9wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇭🇷
چالش ترند این روز های اینستاگرام این بار با آنا ماریا مارکوویچ ستاره تیم‌ملی‌کرواسی با خواهرش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25787" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25786">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXSgtTKuo4wW_8xykOLMWJ17oydRAbQFRfHknUBBbxZAQIS-jxC9Qz_i5mvN6h2mOJzdfL4A0wl_PBIV5Jxkc9gkJuC67Nsg9Lj7tFtlQN4ZKDt4HmPHmXEmeFr8X0ybwLs-94jHARybX9SYuFmfEprFGhaYslBM4G4QAYbZ8N4UMXVEu6u-ZfYixxEyHm9kKaatiQZxv-sq8fdiUB_hwEgPb0sLzDWujkIrl18gOG1KBlXZq8G4PRNF1tYPsdRMGIrJebASrok9yOdOBwAiYRWrLfjzQP3WKWbNiRIEayKDARJczqD4sSnN8xrgxFYxnPAJQwgOuQP56EzOqIZg8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
— آرژانتین
🇦🇷
🚨
۵۰۰ دلار جایزه + ۱ گیگ اینترنت یک‌ماهه برای همه پیش‌بینی‌های صحیح
نتیجه بازی را تا قبل از شروع مسابقه ثبت کن.
🏆
مبلغ ۵۰۰ دلار بین برندگان تقسیم می‌شود.
📶
هر برنده یک گیگ اینترنت یک‌ماهه هم دریافت می‌کند.
🎁
جوایز به‌صورت
FreeBet
پرداخت می‌شود.
👇
ثبت پیش‌بینی:
https://t.me/betegram_bot?start=p8_r4EF37DCE</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/25786" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25785">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YP7y08DE_wfN3bdFDxW5P91yIjfocMtzRCbnkrJj6mxWlgMWYyivGeVMskO7r_v9kNntsfs-Cp61i_9B1cic_jaVPWVKpE-bLy0Rs2-kahz4yizQ-O0pB4n2U9kimXPApNVYvxrIQge38d7-IUqNNWBQPiiDMDHkD0GNZDFtsFnYRI2IW3pcsXmFzUavDAmQmcq0KPlb-sdMz8F2QnRoaDo__TVgOiUKr32vLBbIhrRpsHwnXBZ7xKJ7QlkVzDkpgcDNfs7yrzsRb8mvi5jUHiPiQh7Hn4yWwzGCCmvLnORQCL8PIavbToGBZvyBd6TLOobQusryu25_WvKMHm_QMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی‌دایی‌ و کریم‌ باقری دوتااز اسطوره‌های بزرگ فوتبال ایران مهمون ویژه‌برنامه امشب عادل هستند. ویدیو کامل برنامه رو در پایان این گفتگو میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25785" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25784">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mx0k8HI_alI3lnT-MKWy5D1gsIcQLtOYULmuXVC9Z1sWf0ykK-Pz163V3zVB7Oa69HGF4AGrIwv-_f9JcJBbtCAtY4IDdISefXiNPqaKvW5axWUa6epHqH_VsUSzuQHd8tEtSLqmDdB-ZjIdhXQ1Oz5SztHpUWN-bvh6m2sJWLPutaSmUJT9MpFN1y0G1X5XfmPV-1Lt7aEwi5jiwvBVfRmSxgxF54e1dM6eITeY9o0wvv0BXXDVa7wNdk6tQRjwlk2oyBPV1vV-4Ly8SVhojbFAO0LAoBRq0BH6rDqMnLPic_Z8MNwelJXMzaSmHIZxiPd2Y1K6dQmITLO-f_yTFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرویس برگ‌ریزون بازیکن جوان تیم ملی والیبال در بازی امروز مقابل تیم ملی اوکراین؛ خودشم فهمید خرابکاری کرده زد زیرخنده؛ اشکال نداره این همشون 17 18 سالشونه جوونن. اونیکه تو 33 سالگی و اوج فوتبالش مفت پنالتی خراب میکنه اون درد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25784" target="_blank">📅 20:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25783">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeZq_LtWcXy3uHpNKGerf0MD_Um-3PsvTHOJ8x9YGzZzdl2zi4hZccTa1kpyd6Q94XB712xhJcZlO_y4kx4ShBURfyHFAaXFeqRU5h7IRDTnnj82r2DJaIYRu4doLaVp4cSU2FdKdNRA_eaxDJbvTwjQ4MnknnvtskTkP1N-LL8YNcbDTohi5oQ1khOqxgr9RPCy83MXIBVpNc7OI6iyJTYZjcENGgvGmgRZYHar2fzCGVmi3oRpHrSK-EUxRlNTifatB1nm-gim_1n4o-tniCvgejzfvLozbFz2_NZvE0DKv30scklqVX817tRM49BRqJYJ1Rn9ZrmvHac-XDWLvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
واکنش جالب ابوطالب به انتخاب بیژن مرتضوی بعنوان خواننده بین دو نیمه بازی فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25783" target="_blank">📅 20:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25782">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87ed733fb0.mp4?token=NJKCFZ_AxQ3eNn7u4nJ43BGLX3FeUgTV5JOJOZlyMEVHFcruQvAm_iNsQVlbxjFV-rOEUiVRwKruK-3qXV91Gs4xmIHl_SszTD_uG8MPe3US_vFFhP2pMsS_T6TxVKKb1enq9avf5HnRyZdPRa768elLnj0hLj8hEFGnWR5X8Tt1aS21VlOnFMlwF4-zss9QjkBjG1ulZNwAs0FmizNOY6xxL3lv3Y-J1T5lBerbyn7MTXAVdC7hG1WB-spTWVCkP3NWqdRC9pmFM4uCU2mtN5jqtHYyUr5V7uc07M2mcn2poijS78ZD-tE2CkgfxIua8rI8RdFIOxJzYeC4wU6jBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87ed733fb0.mp4?token=NJKCFZ_AxQ3eNn7u4nJ43BGLX3FeUgTV5JOJOZlyMEVHFcruQvAm_iNsQVlbxjFV-rOEUiVRwKruK-3qXV91Gs4xmIHl_SszTD_uG8MPe3US_vFFhP2pMsS_T6TxVKKb1enq9avf5HnRyZdPRa768elLnj0hLj8hEFGnWR5X8Tt1aS21VlOnFMlwF4-zss9QjkBjG1ulZNwAs0FmizNOY6xxL3lv3Y-J1T5lBerbyn7MTXAVdC7hG1WB-spTWVCkP3NWqdRC9pmFM4uCU2mtN5jqtHYyUr5V7uc07M2mcn2poijS78ZD-tE2CkgfxIua8rI8RdFIOxJzYeC4wU6jBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه بازی‌های تیم‌ملی‌والیبال+جدول رده بندی لیگ ملت‌های والیبال قبل از شروع هفته سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25782" target="_blank">📅 19:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25781">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5e427ee9.mp4?token=l6-pSA-hBHVCsN8F_bfHk3BxSf3oshJKa2VtvmOmKh_LBzCcqfcB5mIm-gKc-II5gawF40s9Fpn0NFsyP__Ji0ZTt4lIxb2Fwmtby0pgl9-CgwapuUiRhVRzu4lkLJbHkoSC6PSQct7-z-cxYbMwSe76OUbmh_QoQazfJzYMM2xgkjYQwMUhiZ50-6yQrENy2VGA_oRafmMizNHhspqBJqpuv-vfEQCSww-4v45D2xytDqm5jl1WSciv2LA8WLyL-x-4J4aFsvssKKFhXMGacdT1QxBXTMuNr9Qo4P6VGJegud1XmxVw23Ax0GlqX6hTjZQNXWZUHVOtu-dWmVbtYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5e427ee9.mp4?token=l6-pSA-hBHVCsN8F_bfHk3BxSf3oshJKa2VtvmOmKh_LBzCcqfcB5mIm-gKc-II5gawF40s9Fpn0NFsyP__Ji0ZTt4lIxb2Fwmtby0pgl9-CgwapuUiRhVRzu4lkLJbHkoSC6PSQct7-z-cxYbMwSe76OUbmh_QoQazfJzYMM2xgkjYQwMUhiZ50-6yQrENy2VGA_oRafmMizNHhspqBJqpuv-vfEQCSww-4v45D2xytDqm5jl1WSciv2LA8WLyL-x-4J4aFsvssKKFhXMGacdT1QxBXTMuNr9Qo4P6VGJegud1XmxVw23Ax0GlqX6hTjZQNXWZUHVOtu-dWmVbtYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیوزیبا از حضوراسطوره‌های تاریخ اسپانیا در حاشیه دیدار شب گذشته دوتیم اسپانیا
🆚
فرانسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25781" target="_blank">📅 19:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25780">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f78ae3e4c.mp4?token=Tlxg3FdbrdgrKv0Cq-oOqsj2mCmxwOjBm_wFpaS_z06ISEinBmhTFhHAji7p-EFX4L3AJSLDNuAVYiMMpeVo839zCQ2ggFmXCYzaSxtEQWlQCvUkQrqlXwSQEl6YH8g_mKiXfyuIC820-GvJnM257BCGeIA6EiIoiWWQTsC5IWgJmDZ1RRgD5bDAW5n7Q3WdM4eRT0SAL6a1-5YjaoSEIPUaOwdKEZKng3X_eWCw2Y5esL7ZO62Rh8RazFysfG5tIPBICNeFvzCBxjPzXrvWqwdTdtseKPEJ1pKI88i5ENopAwmv6M4owz0yaB9vDMu23fgNEurozNB6jsy7T89mRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f78ae3e4c.mp4?token=Tlxg3FdbrdgrKv0Cq-oOqsj2mCmxwOjBm_wFpaS_z06ISEinBmhTFhHAji7p-EFX4L3AJSLDNuAVYiMMpeVo839zCQ2ggFmXCYzaSxtEQWlQCvUkQrqlXwSQEl6YH8g_mKiXfyuIC820-GvJnM257BCGeIA6EiIoiWWQTsC5IWgJmDZ1RRgD5bDAW5n7Q3WdM4eRT0SAL6a1-5YjaoSEIPUaOwdKEZKng3X_eWCw2Y5esL7ZO62Rh8RazFysfG5tIPBICNeFvzCBxjPzXrvWqwdTdtseKPEJ1pKI88i5ENopAwmv6M4owz0yaB9vDMu23fgNEurozNB6jsy7T89mRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
#نوستالژی
؛ یک زمانی میلان تیم نبود مجموعه از سوپر استارهایی بود که همه جام ها رو میبردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25780" target="_blank">📅 19:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25778">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KgEnRBIyKIVUIRJD1sPj8jOAwdCr2yCdJ0ZPArs8rbuNuujkhZlaydXcbeiCglQDZxchM9K1xZezHzhjlpbQHa48-xBAmnJSlz6DLe3GYNjPlKu7y9tmmKnPgIRgtcWcATHaUwRPrzkOdQ6AR-z2JzZ9aVwMvRIVOzLAoIeklOdhPLSpwdSg6tUDKEjNzEoKHo19yPoBZCqEQH1BDs03lPXtRsmf8VAfL0-F4_h4Rz5x-Q1fH8H3Yp_dwn4ChUzN_YNQ_xjZTqlkEx0tFVc6rLx91U_IiQFvPfhBRSOtKjkvfR27ImXob_jY7_wUafXzB3nJ9ld1Ig3n3MSsDsFH5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CWZ8GYtNESMGNf3uwJWOnjMNp-srJRnEFn8EpK48tREQcynbeyDo8F8QzbSVOcEbCHF0M9oLzQ3NGk6hJPGQzmdrzJAf7XK5-mJJaAFaHK9mRTzNC00F7_RcVEhWxLdY-BtObbXBnQpfML-_telB3RgIgcHNkaGmQud_buAhHsIa6cniifoNhbFPRQhh9cF5jFpHAeWqBs9Z0uwabXY_xoD78Rdv07IWjkmUu3cu3h51Ps9YJn51uZg4Ia9DAZiPjWNJS-HDAnUnepYVc-NfE6haIa5cg21wo1RpdLi4n_X00VSqZ6oDWKw8DWWMxkXto4vW9a8tSOG9AZSGOnIVaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
👤
مدل موهای جدید مهدی قایدی ستاره ملی پوش النصر امارات؛ اماراتی‌ها رقم فروش ستاره ایرانی‌اش را 3 میلیون‌دلار اعلام کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25778" target="_blank">📅 19:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25777">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kynV22R6Sie1tG8s8EQHGUTZ8HsaMOBOp9vWA74VIUEyo1FFVpHYT6Ei1vWM9XctzVZ0m9dZxNI5G2mVLVbPQuwjhXTlOR0FR5v9l4kU6OJvoO7yxOqI4S22W54NfyuixameM4FfyLoPb0uKaai1EEQpyyWxbWHLIXWjBLTemFOx1dJLOVeEfL5gzdtvGtqRSOuOLa_B5SIMpsuKf1wzD-VhVTaglS0kKQfuLCXeh6_m8YLfmn7wLMZ7Cp5tCwPJOM4psA95o8VKtudnSMQL8jmv_ThbZjq9KJ9tvxMJvtG3R8jQbkYjfoSI944WXBYe0IxBK_msYKrqRdigIBNy5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛ جدال تماشایی انگلیسی‌ها برابر یاران لئو مسی درنیمه‌نهایی جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25777" target="_blank">📅 19:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25776">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4hihjrJMjfmOliOYfvSj9Ro4XGm6DFewzxC4r1VgCVRwR_z1mUVkmKoPm-zBdvBsakM2iqWGiqTsgHvHvBM3Xw7uc1d_Yjb7b19cD46zhPWYpVqwBbj2zu6vJLy9gsVbcgVeQ_ENhjkzVxWIBx-U2OMyqgEAn8V_QBIygjCJVW-HQSzTfeEyXDJpBaLuwcOM65dlnrWN5NEUscs6jMP-kjkucUfILD73hzO8M2FvRST5hyzS8ps1gXhv-nlOU2hMrZjNr-cRu_6Ikre226ixVj2TqK2Dlj9BjDJd6pMBrcSAnX1zuiyKnv_DhAz1DMjWbyuO_u4NaJaYl76stLONA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سانتی‌آئونا: باشگاه رئال مادرید اماده است هزینه بسیار هنگفتی برای جذب مایکل اولیسه بکنه. بایرنی‌ها به‌احتمال‌فراوان با 220 میلیون یورو موافقت خود را با فروس اولیسه خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25776" target="_blank">📅 18:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25775">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJ_fklgOPybdvf_P2ykF611SmGe4VkPKBZyLZpGCLZxNFq8_oNu4AU7hAGczUGIpq_Szf82BLBVc0n4O23LmSAb6X6r8uDzmUWQpF8eUSfxQzYPAsgKAqQLR0cU3I6s_sCAmjgtl7xKlHuHyPynulTtLQxxceKz1WXUa0SgK0tyCO8Idw-dC-Sz2SZTeSX8JEdP8GiEsu5IBJi1_FVH91fl5yW5RWPAxrV6EwEW_ky3SmLyDWep8VvyC0Q57Cci9n7iyndW7u80ADuzCjx6uR09nM8cVqUQY1Y5U3XLkh2WNlxfGsy9SYmt6LUh-4EfHM2GOQ_0pOUZm2llDx3B4fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
👤
طبق‌‌اخبار دریافتی‌‌پرشیانا؛ احسان حاج‌ صفی قراردادش‌روبه‌مدت 1+1 فصل دیگر با سپاهان تمدید کرد و تا 38 سالگی در این تیم خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25775" target="_blank">📅 18:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25774">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkAzpkvEf1D6faCPAff1G-TdLsVfbmTts4bccUrrkLHk0naUNanlDmoxXUPPQMmztyNYCSVYmA0LoMvx3NYwfw_Xr1pwFG06sBy9y7H2yjpv5U-NILmMhB7ZnIK50smBGnsytmz6lX7WcEqoDBeGJKi47ozobkNuPNeyAX5jhsvLFUKQFAfMhLOUOS-h0GJ4qWfz-9GnT-Dy-1KnR2e39Ize1gdZq4b2dlqwPGhJ_tYhOY41Wbi0On_--BlllQg8XzBv10QEXNlO-YMgqlh9mKPQ7KEUcgY3qu_WQI6I3fKyyX5zmm1D7RY0khTOp6jzT4-Of_SNqSdS2AgQPOOpEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#فوری؛ سانتی آئونا: مایکل اولیسه می‌خواد درهمین تابستان به رئال مادرید بره و این موضوع رو نماینده او به مدیران‌باشگاه بایرن مونیخ اطلاع داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25774" target="_blank">📅 18:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25772">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZE3dDzHmazvmWczDm7sZqVztglsN-7iqp_VUOL00Q5naZwiO294T5Gd9qovW3HB3JU5dBge8-BsNNu0wxnq5O-tl1cn0GyEdRvq3m2UihRqQ5nDE4YSpNjogGo2_gg6R0hoPSjGdaua8g9VoNxIaC0p7MT6e0DM4PDDbMEwtpK2SK5JMnDEKHtNsjEcglbh-ThoWtgaDYadE4_FxepRiusc7i-_8isalOeGOHRp8ZY05hPgUKvTuFzL2ktY-bTANVHxz44MujBz8MvUgW7D3072wuNptOEmKMOc8gWT79Vp1_9xUz_vfnJQ32kyRJagJhg2cM4htrfRm5Vsy3qPx6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
فابریس هاوکینز: مایکل اولیسه پس از جام جهانی دربارهٔ آینده‌اش بابایرن‌مونیخ گفت‌وگو خواهد کرد. اگر آفری‌بالای ۲۰۰ میلیون یورو برای اولیسه ارائه شود ردکردن آن برای بایرنی‌ها سخت خواهد بود. پرز رویای حضور اولیسه در رئال مادرید را در سر دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25772" target="_blank">📅 18:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25771">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6SeoU1QSl5ds2qEhIBXeUxXawvdwLdTHxplhzOUVwF4TvusJfvEPynzkXOlTCrJvZ7UuL-EAirTzwKpsTSuz1Ok8cXCTelttRhUZkSOuB4JQD-qlG1r34p5ezSlRgLqqhI1YsYjz8u6qlutqqkfQNSE1Q9YpbeXLcXzbi8lmyH6uA76jbnQoHBGkQFdL_Mt_BD2oINLux1rU6VK0OA3LoT7hbt_xiyZS9Sk2Y3kCPa5bpFCXNtkzidX4bBbOqSW6x8D6egBnLvrS2_QsLmpsCGcggYQwYB4_IvCXyHbEEJFOxaexe4brFHz87-gW1JyBRy5x0X-PUZcL9r9inG7YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحالی استقلال پنجره‌اش بسته و دوفوق ستاره فصل قبل‌خود یعنی یاسرآسانی و منیر الحدادی رو از دست داد که فصل آینده نماینده ایران در لیگ نخبگان آسیا خواهد بود. کار بختیاری زاده سخت بود سخت تر هم شد. ممکنه حتی بختیاری زاده استعفا بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25771" target="_blank">📅 18:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25770">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puDDSB0pyoP1FhtAwbGam0ggdp27HBGFrkRREYHYoS-lgJLkHFdPwPCFo_e6vMbUVx29S0rfBDfpOlUynHBdiFp88rVx34PlKn-yPm2v1hGj_fqB-OCzBS7bVHeemJ4UcWNjiE-ar_lgRJSNhsrom1Qi9__B5xtJ3LqONbcTPi2hz5b4ynX8xk9erHqQaDUEP7w09Q2ZrOVbTDUlfcIhRb3upRpb2kkCxASd01Z6ONPKmv86Q6mOnisZ2DnuzoFNA4cQVL-xfT6jxv-Lu-zRfvjUrqAHBirkl89-vBhtZ4oCM9Pt-UIROWsaKTucgNAjEk-n2DYI-YMOozFmcDrjnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیشب‌بعداز بازی فرانسه و اسپانیا درنیمه نهایی جام جهانی؛ خونه یامال تو بارسلون مورد حمله قرار گرفته. دزدهاداشتن‌از دیوار بالا میرفتن که نیروهای امنیتی بارسلون متوجه‌شدن‌وجلو دزدی‌رو گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/25770" target="_blank">📅 17:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25769">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VO-vB6NiWtE_5qBXHtQBAqYOxmSapOLsP4We_qCieI-X-ei0VkFVmStSlS3lMvG0XoAuQD7Fd8wYafonXDlwnq__yappUbunNhr52geWrgI_Fq2n1S-vxz_ix_ueewD4xTsxqIamkgeR4B9V6sXGPsgi6lDdR_6fbWGfl-VQGI6r82kxlbOcuqaUc36NRFhGhuCTYzSKn3JbI8bLkfK7mpY1MCW5mnsFiPfvhuO5DyHTinsh2uLG7HE94EPvF-jVZ6oMwBcjWyfI6XnrBuznAqUT8AZifNlqbkCWZDa4FXjeePlNt-7AoUC7xEIR60SddkWJQytnqIL7utNTXp_7yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعد از باشگاه‌‌تراکتورتبریز؛مدیریت‌باشگاه‌ پرسپولیس نیز با ایجنت ایرانی یاسر آسانی ستاره سابق تیم استقلال تماس گرفته و از او خواسته که یاسر آسانی رو برای پیوستن به پرسپولیس راضی کند. حدادی به ایجنت آسانی اعلام کرده حاضره اون رقمی…</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/persiana_Soccer/25769" target="_blank">📅 17:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25768">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JG2fsC_lHBciUZdNj-aDA2fz7NFfMkNXCkNkeFrl74jmOLf3Sq-1YWZMuLat7Z6soLEnOxBWa0XYCdWG4zYf075EcKkLd3mWvlgI9t8OAy_R5nRGhInfsiWt1nP5CBYc8vu-XM9voIsy9so95xePd3i_v2EhBKrCvgEn2P7cAgvzJveX21buz6ZuPBrvE2JSrpPe8j-WaKoKMa7JdRwTINlzjbEDSZNw4C7P6Z02qobchOEepEw7vpQ7So9UMr8HsQAaWVrdAIqHHv5oMzgg5J1x5tV0L0kBO_eAVbIGytRHWH-0HZ4ijI9c6ecxePwGVDCKQTSHP-du6RUtG8B1Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های بلژیکی مدعی شدند که جرمی دوکو ستاره تیم ملی این کشور دیدار فرداشب مقابل تیم ایران در هفته دوم جام جهانی رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/persiana_Soccer/25768" target="_blank">📅 16:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25767">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gO2exv64PLQeOp4byD4IZnAg-nFdjbVjOT46g02uJ9Gh3sTTEh36Nq18mNmSZSrVQlPlnHtT3-PlpWYNswmmgl5lFDAZlB74m5QizzzLXL9rJHvnBljXxR3d_tJadV3Qca405nCTb0dQ8swQnYdsKyYKE2RB8oq52_rzABaRKShHLb7t5GLNr6Wkb-EI-5IE1I1K-xtNQYoHUKmF8uvZhYzz__j3u2L9-z_MDdSZblA8Mas4JUHXRJvT_LGrbY1M9T6FcnfsaIb4VCkFBtalVPhqV7TrUKbSuzBySO-WH5Y7pgBUM9KQo2o36uL8jR6VFmxJuyQCbq_CLQ4UPia2Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های قطری:
باشگاه الغرافه قطر به دنبال جذب منیز الحدادی ستاره سابق بارسلونا و استقلاله و مذاکرات رو با نماینده او آغاز کرده است. علاوه بر الغرافه یک باشگاه مراکشی دیگر دنبال جذب منیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/25767" target="_blank">📅 16:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25765">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb986dc0f7.mp4?token=Ddy6Kyblrf2fV5h5r9A0lvSycJIILYZOahjt-ZpxbTZ0hqWNapi7SQbaxTxH9nvw3USp6Wryz_qUyaoILZi9B6AExjOZ9RHyf0r5tOpmjox04BPRGthCPgZRZk4TjmJarIZJ_whR9ncCVQayp0fRUpSBQNVCfve90ObKCKsmlEP8ZIH4Z7m5aPO5qRT-lVGqbrN1Nf5bdTesGR_vFvYpCcfFQsKN0zuz1hHS4qC3pXD83G2TS4Y2EiAe2s91bx_sO1HUkn5JkaFEBbcZhT5igCzwT2Txza01yr7FiIN6_rp6Ly5_lkoAdeKtX88dlYS9ojqdJFY7SLt2w0kUo0LZ3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb986dc0f7.mp4?token=Ddy6Kyblrf2fV5h5r9A0lvSycJIILYZOahjt-ZpxbTZ0hqWNapi7SQbaxTxH9nvw3USp6Wryz_qUyaoILZi9B6AExjOZ9RHyf0r5tOpmjox04BPRGthCPgZRZk4TjmJarIZJ_whR9ncCVQayp0fRUpSBQNVCfve90ObKCKsmlEP8ZIH4Z7m5aPO5qRT-lVGqbrN1Nf5bdTesGR_vFvYpCcfFQsKN0zuz1hHS4qC3pXD83G2TS4Y2EiAe2s91bx_sO1HUkn5JkaFEBbcZhT5igCzwT2Txza01yr7FiIN6_rp6Ly5_lkoAdeKtX88dlYS9ojqdJFY7SLt2w0kUo0LZ3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین‌آرزویی‌که مادر عمو پورنگ داشت. فقط اونجا که میگه بالاخره‌آوردمت. عمو شما بلیت بهشت رو با همین نوکری کردن مادرت گرفتی خدا بهت صبر بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/25765" target="_blank">📅 16:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25764">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uy03cCezafv-M8I0XMj6aJS_ch8G5_w9Oxmbo9z43W8uYk7uXyxAJLHITZoO2PQgfP3dAzrhMV77jmbtB55aCuord9eE5GAeqmnu1nxBQlhUtWIUI4tlPKjpS6bk_XJlmFvLmXhjN2y1l7Mbm3PVKYJEHEB3EPdweM55ZNb1_-dnmJs9Ex3qosiM7qfoByW_HZENeLltfygNlVkNE4YwyurdJSSEx1lMiWEP7URu0wct3SvaYmV6EX3t4Bte87t7wXhBQKXzNAKZVbpox4POziByyKNl3dTTwKhbIY1gX_Ra_vGiFFAny8KOU3qPlg4DRvYx5Vj_RanDmesNrgvLVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
بااعلام باشگاه فجر سپاسی؛ فیروز قربانی سرمربی جوان‌ونسبتاموفق‌ شیرازی‌ها از این باشگاه جدا شد. بر سر مسائل مالی به توافق نرسیده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/25764" target="_blank">📅 16:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25763">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5InqBbx3H7-dk4Q2ULtV0ANwTmH_t_shSVOda6d4dY9xJDF-fGUaUMlCxyuzpu2smWyits0bPj-tRuY9F-mLRK_7gJ7I9-yS0sCHOswROoejqoDzKe_d3eXoAv2oA_taAmeI7wOywvZ3XdcfEgh4vRnGIx--4yNu6QhKzdJSaOfYwFZgmoN_TOpk_62FJrEPaEpm8oZG_vClMNHlNI-bKMFaPiHXQyPvd9bywINVoKK7WwFd-YzIgrXe23ulHv6QVy44WVh6cvmW7vcqIZ45nZVn5CXXqYh8JxxXxyHoulLgnm0Q74-KhuHo_TT5MR76jaYNmXT61Wcd3yk0uLSeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛باشگاه تراکتور از شب گذشته با مدیربرنامه یاسر آسانی تماس گرفته و آفر دوساله‌خود را به ستاره 31 ساله سابق استقلال داده است اما برخلاف‌رسانه‌ها توافقی صورت نگرفته است و تراکتوری‌ها منتظر پاسخ نهایی آسانی هستند. ولی پیشنهاد مالی خیلی…</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/persiana_Soccer/25763" target="_blank">📅 15:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25762">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V79cJdLYXR-OJoitwKkYwpVsFB-nsqSirpI8DPUAWRuIlEoQRpZpTvoIgN_3e0HMp9JCBLdlowAGBQZPOoHMMuDla23QJ72i4Dx7KhZPqIGhPmk5JmZkcsNCQCEuDFbr5RYwDsrAJYt6hCCNgHDTpqS35y6bsIQiCl53z6lpG5fGMrkk5aU24pvOxOD_iGmD533hmjnK1xucTyb1bXTC2SLBYGkljMKB-XUy-afuKMyTyUmL0JSJ0C7sN8iidRBP5DKcI990AhoPHTFRdqeFnwsJD-3oemI1a3cUNPwCq8EsEIJute0_NQLSyKghEGw_6h-ip5rZXDMbDDmdmyqEHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛باشگاه تراکتور از شب گذشته با مدیربرنامه یاسر آسانی تماس گرفته و آفر دوساله‌خود را به ستاره 31 ساله سابق استقلال داده است اما برخلاف‌رسانه‌ها توافقی صورت نگرفته است و تراکتوری‌ها منتظر پاسخ نهایی آسانی هستند. ولی پیشنهاد مالی خیلی…</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/persiana_Soccer/25762" target="_blank">📅 15:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25761">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33fde3599e.mp4?token=TWKVBGq8LHOUGEn7OJrVC6oxLbd3li5xBikUPCCIg4JvquN_K-TGbcLF2dpROKIXjH_lsSU0c4ygfNypdAhZTZfV4HYCBQ7aLfu6WB_2x6aSVOz6zHZtqtfox5a_rohRqtZSGwbsFForLOTePlAUfhlXEtEMffTORA8yQLYycc4NdQC9Yxb9gMI2cFzTWxQciTyPUf_VItIiHYpC5viwgaivZ61eYR_bvy6psp2uWx2uSYOZJDP-FmDC5F7t3Cbbl65ayFhbn-en8whbZr2Lwkz4b-0RTXEJHhQBiKVIyo1179IN2yAk0n3BhVgjKUjSrFNoKL4f_5dIb7bBlsm9HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33fde3599e.mp4?token=TWKVBGq8LHOUGEn7OJrVC6oxLbd3li5xBikUPCCIg4JvquN_K-TGbcLF2dpROKIXjH_lsSU0c4ygfNypdAhZTZfV4HYCBQ7aLfu6WB_2x6aSVOz6zHZtqtfox5a_rohRqtZSGwbsFForLOTePlAUfhlXEtEMffTORA8yQLYycc4NdQC9Yxb9gMI2cFzTWxQciTyPUf_VItIiHYpC5viwgaivZ61eYR_bvy6psp2uWx2uSYOZJDP-FmDC5F7t3Cbbl65ayFhbn-en8whbZr2Lwkz4b-0RTXEJHhQBiKVIyo1179IN2yAk0n3BhVgjKUjSrFNoKL4f_5dIb7bBlsm9HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
حماسه‌ای دیگر از جواد خیابانی در ویژه برنامه دیشب جام‌جهانی؛ از خداداد سوال میپرسه نمیزاره حرفش تموم بشه دوباره یه سوال دیگه میپرسه:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/persiana_Soccer/25761" target="_blank">📅 15:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25760">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxAFkQkhPSKKvGPzgXjFwp23BlXc2jTpfdLOWHajmK0auTkAxH_oX_oiEGCeE3qfpF_b3KM4SVERttZ0OZHOmXyd7cOELEp6PBgRKTVw9nTOcYILtlqxtXftHX05bSiNsN2et_5xo_mq1jKObpPrTjCJjysSkJl2_kC7xDM7hKTSbSDcqcZxSt0ubd84zvVH58QEXp5bW2Mr5FbaP_SE1AAjG6bhABTlwyAJJibO36_s9WETarruu1ujxbtNbIlHmlFLERMxy9trMsQ5iBiphmdCNvVGqm3BoTr71pkidIIQjkzbaBHiYptiNHyI1OJxafGafl7-2fm16PHNxy23bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#نقل‌انتقالات
|اسپورت:
سران اتلتیکو بدنبال جذب رونالد آرائوخو مدافع 27 ساله بارسلونا هستند. مذاکرات باشگاه با نماینده آرائوخو آغاز شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25760" target="_blank">📅 15:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25759">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvLzVh3IRPjXGuBETZsAyx_fpm0F5WFz4Ecu9qYTxAb8jlnoKV1qiyZyy66psqisUikTMqmSahW4EPgZkyprcEDk0yZCnY7u41BmQxj5Mc3fb5o8ukaim8HtcKK-574RsXDk63VO_yvB_go_syZOtU_ujihh9uOs1hHvXZEP_996wprP1fAG3T97-VNAgKHMOIh5__Gwv_wHvyRu5bdn9emLp29xbs17V8ytClo6OtDvrmCJhYMsQeQCo-p38e_ztssRl4ySPF50g2WgxlNQGXGyZ0UygyPua7KVJRdIqTC0VsyoZjTeVHCBJUMDpZqm2Co1V6VBa8AymEo5nk6-CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25759" target="_blank">📅 15:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25757">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXZoQFF23QByRYzGhV1rnQqDi6i7lfS4vyMgUg5DdApqScLeK96dLgR-wz-7D__OJQn975B-KQdmq2jdYa7UDVd5Gml3XcoRrozlD9I0f03K1NR6gdg5tF1fQWsfDyyErTdeGLq3TWHduA4Aq6xcAV1EXcaO5z-m7p5Dbab7plhfscduAqk8UcaVys_8VFJ25FtBlJfja-jsyf4r_9bPQqd-ET5t8IHue9Nh1wXnITYNBNOtgHyQKTztuGrwQap0yuGoOtmR9J7Pr-r63Aabqy48OEu3MNRopx689-D9P4vSGyvJa5rMklBHpKlymjx1TCDZgmzFSCvjHnIqAcgEOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق‌ پیگیری‌ های‌ ما از ایجنت ستاره‌ سابق استقلال؛ قرارداد فصل‌ آینده یاسر آسانی 1.2 میلیون‌‌دلاربوده که فوق‌ستاره آبی‌پوشان برای تمدید قراردادش1.5میلیون‌دلار درخواست‌کرده که مدیران استقلال با این درخواست مخالفت کردند و به مدیر برنامه‌ های او اعلام…</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25757" target="_blank">📅 15:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25756">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTJ2J2WNuSTOEZhWNWXXOT5jx-TjsN9XwISjgi5a5Nrqf64Qhx8dhAI3WXErvlF6o4A-nyhbYGWmIg5DbDy4PHPpVk6iezvDGibNuaZ_1S50c62XEharnPfRxgyPxK4zKkyxyV37Zwb5huACzKt_Ap5fDAjXx7oTpo3MsGeau57QbCTFUBPExMvpSTpvasdWM_TWzPD2KjyCBiGLiua0qsJhcIbeVl4UCqDawF0OFPkfseaggmLRTyoGRXXxyGVnjso9tkMFn57faJdPXNpbaC39kGU5e1N6bTfECxD8R_6FOUS06z6nQW_9EFMRi7luP3KIDjFSS_nERCmpyDv9fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نیمکت‌های جام‌جهانی 2026
؛ چه کسی ماند و چه کسی‌رفت؟ از 48تیم‌حاضر درجام جهانی 2026 برخی سرمربیان همچنان هدایت تیم‌های خود را بر عهده دارند و برخی هم از سمت خود کنار رفته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25756" target="_blank">📅 14:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25755">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R17ZoW8fdRHg5BF5WjKZRDRUp_KWll5hC3kKcDTeVcGerhdo7xtqOn8e7zz_VaAjf6AGp7LQFOOstHZTT6aXOF3UsHzpD5eqvSOqyW3f99LnPeP1mT-_eYSFOkH0v6mR6kLO3j7-LsglbDrpi-GfMyXWzRsvlDM_wLO9HECGEFVHQsifSgp5BomfBZfy9FnNn5HEnOSFQXhTqYBfYbLAR5zPqv97S7vmp0pUZDBD24Vs09T4bs6xxx2A3dPwqegpfUVdaL4gSre8PeDMOrCDSd8uDIKeVNPVTlIJsOn6PD7sVicXH8ppz0mB7_qZf5U7Y06DMUSULkDxXAstt2Q9HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
همانطور که دیشبم گفتیم؛ سهراب بختیاری زاده قصد داره درصورتیکه تا یک‌هفته اینده وضعیت استقلال سر و سامان نکند از هدایت این تیم استعفا بدهد و این موضوع رو به علی تاجرنیا اعلام کرده. سهراب بختیاری زاده به تاجرنیا گفته با این وضعیت اسفناک آبی‌ها از آسیا استعفا…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25755" target="_blank">📅 14:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25754">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUDk0WGtt5awwVgv7bf4VsSzLEpxBANCHRP4TMnkY627uFqE81rDOM-iE4EopqdJDAG1eerOeKITSkdcwfR1RFX9AH6RE0O40394gqDKB3ZMkE0LWveqr_2wMyzg4a-SzayKRX2Vxj9upF7ophDKOKed60Dfu0oT5wnN9EpbbsHP_IcmcX5yRMHu7uojjGfIkgGoyllQWyK6WB6zCo2wCKfDaaQWbV40_0USYehPUHgeQVgsaM912xu3weO7SeESnzIwfzuWgbTrd312P7rIYSUaM17_r8ys1cXGO3HkFvcyXTpPnFXy1d7Bwu90W1oWkav1BJxJVLx2AWwXyyJBbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
خبرنگارمطرح‌باشگاه شاختار دونتسک پیش بینی کرده آرژانتین میره فینال و اسپانیا قهرمان میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25754" target="_blank">📅 13:52 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
