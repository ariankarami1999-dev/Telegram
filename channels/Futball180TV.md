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
<img src="https://cdn5.telesco.pe/file/E8_LYLo-hCQryOrexXvw3KDvoPxcmP3YV9muPtyQ3U0fJywo3m848TXcePVBZUoZa3GSQeF9NbqOxV79NawiaoFphVQ26FdmVky-SrhnMi5-29KgDtf_rv3Okqk5qclU0sk67pc-5QQl-9mEVEHgweL91BFcqx-vDsEdHCTISe7LbYRfhUDjv0aUuCoFzdRDo3U0vxz6UIfqFfEXdhsbaiEvum07yVhpza0HARGh_JA3iCxutFjMw8_umTT3DvizO69MuHvyCKRg4UL9BO3MuhU3Gq7QUlJ-aCOxhPaRCHSutPoqyQfeGQFNn-qXwB9T222Yz71ohE8DtvGCsMunrw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 518K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 20:25:31</div>
<hr>

<div class="tg-post" id="msg-102181">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcRobxhuJr7Icc_Z5uXZM1Oi2JZZppFGG3PhP3Au0VmKGNUYA9fhalR_p27pg6RU7GlF3s4yB9Ix_1fV1zjW3QjuounzVCd0cOZS-emrwlPkIyzaMRAu7dn9NuRU6bhYON2rQ-SlCflDzAo6oddNJTEfOTsV-Vlq_udVbCH_F6vQ_MT1JWzVHw4b3zVXsvEFAFw6xY4cgCstutUNVGObE7hY_merN195ovqqrJ2QWWfL4a7DuxrfqVuucP8vhdx1j8W_T49Ad1jip7VWRxVkiUvo6TzxknWitEMlDJJrivqceTHk84t_Az2LVoK6Hbgyz_dKhn9xHTzASrvmFqOshw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوری
🚨
🚨
🚨
🔴
🔻
باشگاه لیورپول در حال آماده‌سازی پیشنهادی به ارزش 94 میلیون پوند + 35 میلیون اضافات برای جذب بردلی بارکولا است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 615 · <a href="https://t.me/Futball180TV/102181" target="_blank">📅 20:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102180">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be1bfab961.mp4?token=CyXEJLafMMr5SP1Wbf7d-rR-eiQrVIKTzXtA6KDazNLj1zywfOV4e0ZqSD4xMGX2uqtolrN_6gI7n8mTFfDdkmpIVHy9SJaE1X5ItCySbh5yOczIKpmbEyNFbixEDm6HrUIW2XhvlVcz-0FesoMq3YON2U_ItEl1GyPRYcOz72AlnLqn1Biw7-kc8GAMbKsZZKutZYrmMC6fWvsEy-1GsilPrhrhr4nByv16DHSurCdM5B2cYqhQ2qzkDJTMXeW7g_79d9lc1ammMqBnTt1VhBoua-hbUjXk1GfMQChfq7oYbiA31FJZ8UIpdOM3l8IpUjBElHLcMN2IqaHFGoEx3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be1bfab961.mp4?token=CyXEJLafMMr5SP1Wbf7d-rR-eiQrVIKTzXtA6KDazNLj1zywfOV4e0ZqSD4xMGX2uqtolrN_6gI7n8mTFfDdkmpIVHy9SJaE1X5ItCySbh5yOczIKpmbEyNFbixEDm6HrUIW2XhvlVcz-0FesoMq3YON2U_ItEl1GyPRYcOz72AlnLqn1Biw7-kc8GAMbKsZZKutZYrmMC6fWvsEy-1GsilPrhrhr4nByv16DHSurCdM5B2cYqhQ2qzkDJTMXeW7g_79d9lc1ammMqBnTt1VhBoua-hbUjXk1GfMQChfq7oYbiA31FJZ8UIpdOM3l8IpUjBElHLcMN2IqaHFGoEx3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادارای انگلیس با هر پاس گلی که آرنولد بده قطعا یه فحش حواله توخل میکنن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/Futball180TV/102180" target="_blank">📅 20:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102179">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a5b1e0f9.mp4?token=HnF2FKnQc6SKV_dFZbhLNJbeGmgsmBQfMFerp06SH5b7t-JSgllCK2sNsT5rAbeK_jPpmRCrMRmbjPGyXuYUNRcXDOUgajg-RgS5s2NY3Ygc-hwDacMu0N27NHB1DoJUy7tIUERT8fXjw2WHISvmI46n2zLI6bjn4F9a-3oeFK2iR920eRiQ2uHU1t2RX0rA8PAOEaaijCs51nYg3pBtGTNEfZGRK891A_fZZOzUGo5tqZ_yROnGH1aG8Dtg94DjbJjKAZp4cXoc4axScnm1EK_I3JFD8UhRMDN7q3JtckwBKEwnGmg7lZUDiwhxR1HoyFMHraOb0NjF2zVur8Xb0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a5b1e0f9.mp4?token=HnF2FKnQc6SKV_dFZbhLNJbeGmgsmBQfMFerp06SH5b7t-JSgllCK2sNsT5rAbeK_jPpmRCrMRmbjPGyXuYUNRcXDOUgajg-RgS5s2NY3Ygc-hwDacMu0N27NHB1DoJUy7tIUERT8fXjw2WHISvmI46n2zLI6bjn4F9a-3oeFK2iR920eRiQ2uHU1t2RX0rA8PAOEaaijCs51nYg3pBtGTNEfZGRK891A_fZZOzUGo5tqZ_yROnGH1aG8Dtg94DjbJjKAZp4cXoc4axScnm1EK_I3JFD8UhRMDN7q3JtckwBKEwnGmg7lZUDiwhxR1HoyFMHraOb0NjF2zVur8Xb0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😐
کصنمک‌بازی مجری تلویزیون با تاریخ ۰۵/۰۵/۰۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/102179" target="_blank">📅 20:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102177">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E9rrKcRZvlMATc9gx3uXanPggC8oPdY46-1Qr0KfNpvmEgGrLgKtAe6IPuSV9BoS3ezqkUk4S0ffpXX6WDhljwl9UTz4-GGLaz4h_VoRoPynEZn1R4u1GhSs_wqFZcO59LCGr2_w-hvD6UyoS0f193ZqzK_jrUQtQjYidgYwxjeNTwtFSxDHCsb-BweQ5r4GNOkWdkAAd-QJ6Nfny8oZ5JkoAXOg2LZYvOLgRHIIUdvOew-iOzT6wFEzCZYGk6FO576NGRm9u_RBRsk9f7m_vHKBlw2morLNUDgKW-GfRMjuyVhuG6NDKxy1Irj5q4yDqH5Y_kh3hQ0Esp6VXqq1zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qsk-WUsHWM7uLk0Naao3XQ5hUPDUmdwlEAjwc-zsgCZlaa5j1ieXRa4L0EbQwpU3txcbK7zBIE53-BrJIOr4WYDmAynkA1VYGKkLpKrpxHVCq_8nasLziWmjB1q2Irzuce_Q32Sh7Wivo39KwZI-TZibt9LEEdwyiHjZMnxaOrdkHTI2ioA5Jr6LygN12jXzftZ3igpk74h1kVTiHLgfKUl_-N_FTDBgEpxd0Un1v3KVgrL-h5Fzl9xEJDqt4k2VXL9S825OBWMrdWRI98-1ztxQmI4BqgbxGUaQOAtKcf8xaEsvtIx2yB5iKng5A2VqQQ2WDwKjUnS990TJFSGZxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
🇪🇸
فکت جالب: چلسی برای قهرمانی در جام جهانی باشگاه‌ها پول بیشتری از اسپانیا برای قهرمانی در جام جهانی گرفت!
💰
🏆
قهرمانی جام جهانی باشگاه‌ها: ۱۲۰ میلیون دلار
🏆
قهرمانی جام جهانی: ۵۰ میلیون دلار
یعنی قهرمانی چلسی در یک تورنمنت باشگاهی، بیش از دو برابر قهرمانی یک تیم ملی در بزرگ‌ترین تورنمنت فوتبال پاداش داشته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/Futball180TV/102177" target="_blank">📅 20:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102176">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Of6oXoNr81IHWMPOOk7-70LS-eI4LNQX2Q9muAsMbxFQ_aChvp9_WKgJDM4zzhzyhD2ZH_bGI8iVI50SQ1OFnBOwoVD285kP1q4-PDqd1wCEX0JS_xtqXB-dTEBaC2ax7f2ypSWb6O0y3lAz83ghRbNbvlrp7UdO45-UoasISwg4ZbNochJ3IouSIZFxihGNGH5LlKOc81BuA4t5HfmX-bBH-AsP2HSDFbqfDPnsjKaBAtqYq0EXqs0V_O0O0ynxmuDekJ0xyxZsqKJV0Sd-HtU7flkFC7wxPoh-GYLZXG_f4kI4001FBvP_Y5r6vKOJsF9HWJf_swh2o8SqJKENhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#رسمیییییی
؛ با اعلام باشگاه نساجی، دانیال ایری، مدافع سابق ذوب‌آهن و ملوان به جمع شاگردان مجتبی حسینی اضافه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/Futball180TV/102176" target="_blank">📅 19:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102175">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMGBECrsWuYesRGX3JKZh_Ky2M60XGhCl9KBP4U3Lmdml-UHKxe4azKG704Afwr0bHMQ8gQUOHvkoIbIkZqLnhEGWOrBC_5DfNMSot0KH87oSo2b2ZQ9bzRRf6fZuA9YF8C_SgQJqYdtW1fr5H2aWp42jNrYbgrIpBLCwgDbuncYrIjiu58WMwGYOBrRJ4Gm-n-TuLcKvIR7aL_28h5Y5P0wU4SJISmFwRZdbdSUgCucaL9VE5uPRVFCiIk6ux6D0bb4KyH9rNY3ppqQDMF0tjce5IWh006WyfjRUgT63t-ThdEMl87sI0LIRzsiBtS_qj-ZCFzpgJFgsMTNa7zUHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
#فوووووری
؛ اینفانتینو تصمیم گرفته که حق برگزاری مسابقات جام‌جهانی رو به سرمایه‌گذاران خصوصی با بالاترین رقم بفروشه. کوشنر داماد دونالد ترامپ از خریداران مطرح طرح اینفانتینو به شمار میره
❌
از طرفی یوفا به فیفا هشدار داده که اینکار نقض آشکار روح برگزاری فوتبال هست و باید به صورت جدی با عوامل این تصمیم برخورد بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/Futball180TV/102175" target="_blank">📅 19:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102174">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kl4Xejz0tKUkZ1XxAHcL_so9UL94fECmrr-irsJBzmLU_tFFJTgDEsXhDyxyScs86QqWhkZNvQ9dmLjyNc2QkgZtMLkkq3ujsxVKD0O_B0aaqQAp2YsWXGdTsb2AgUGFWRBv1kIsTQnjgVOW-0t-a3QrsnLWZxnSNhpnSY7LQbzgcmiry1qAAAN9YSVO9GyQzoqAH07n_FpXWDJXy8v0VQgyUzOVE1WmtD2Of5TnSzHgP7gne4NFqiJFViEeSCqXcAXGXDgiqgQbNEmC2MPlQSBB60rZ-jBQet3DJxLhYw4XLNhDkXHWqoSP3U6Tnu8J3nUb-oPPcTQ1549dYkEmPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
اسکای‌اسپورت: رئال‌مادرید به پیشنهاد آرسنال برای جذب وینیسیوس جواب رد میده و هرگز اجازه خروج ستاره برزیلی تیمش رو‌ نمیده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/Futball180TV/102174" target="_blank">📅 19:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102173">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cb3c3fae0.mp4?token=kg_VaQp-YO6BbSys14rqrkN3LlYmXH7fqR8IC4QwhLHifiusWUWpBSSfzD0IjJ1qY09IdHzHC_1DBvPk-Rvcf6yi7A8yuihLHM_GTXhrC6yoHvw0NG-138Lv5fpOiIvT6xzEKXM4iMxixnyrabsgGb-skdn2KO5pU7uZThti61E1sMn4K3ao1o0wr00KBDwodOkuH6K0PgOa5zJsZbDXyHut3v63_r3oO7hJfzfGX9wtdoOuD333_J7wY5_shIOb83u88BQe7VxX7BmEyb9aZg-3KFe7HRNudqyyCcQiKa16CQdDVyodrJSz2QhdHdorYRmVt1QyoGfZp9OICCzDHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cb3c3fae0.mp4?token=kg_VaQp-YO6BbSys14rqrkN3LlYmXH7fqR8IC4QwhLHifiusWUWpBSSfzD0IjJ1qY09IdHzHC_1DBvPk-Rvcf6yi7A8yuihLHM_GTXhrC6yoHvw0NG-138Lv5fpOiIvT6xzEKXM4iMxixnyrabsgGb-skdn2KO5pU7uZThti61E1sMn4K3ao1o0wr00KBDwodOkuH6K0PgOa5zJsZbDXyHut3v63_r3oO7hJfzfGX9wtdoOuD333_J7wY5_shIOb83u88BQe7VxX7BmEyb9aZg-3KFe7HRNudqyyCcQiKa16CQdDVyodrJSz2QhdHdorYRmVt1QyoGfZp9OICCzDHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
😆
تتو دلافوئنته روی بدن کوکوریا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/102173" target="_blank">📅 19:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102172">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QitpTL6fOT5Hf_RaRhedpE8Mpu66Z6xFBS834CXbwW7YrZwzJu5Kijt_kiZ3Ndp3RJqHiJyzFSHmyjYXGx6M-dOySpyfxxBQB_U470YUgrjK5Bnc_auptC9RoFov25Ok_TiUFbxkvSRVPHSw7i-ZugtDCsFl1H7vjK3xbqncpq3TDn1TQ9AagW78hEFOaTsCmdqRGtqEfdZvTXZKorGIjyVAsPvwayoZguULvOKFqc0yAFHdQml6w9KuR9ys4NYcEXswGWWp3WJbw6g4mhlwIkJ1WAPYjvgBjMMAUm3e3DpZJiS_1gBlXE-yOFYiprIZhDD-HNLorWD2xmI7vJJ46Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب رئال مادرید در اولین بازی تحت هدایت مورینیو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/102172" target="_blank">📅 19:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102171">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/164942a925.mp4?token=DPsAwkIYQP0L3sMg6jlVim1IfxUuzrSNX_nD6I3GjY90kbNI1iXWYPIgpphwvXcbeym_lxJTQJX9HzAvcZacf4GxWnn6iTH8HUQam0zp2_gxXGiTLp2hMgPc0KKFYUkU8X-7zCB5TJ6HtJYhsWK5Sj1HWhIYmGZZJnw86lZLFqHGLZq-jbU37a_VNqU0fRqjtnh7OYtImAUi_SFCo9hbjM_6nEnvgrMMCDzukbqnFr1RkaAXe12vdWm0TwlhSyQj_sbJGTmPG6kJLItcsGJ95Z2eLcbncXMIioBlRVB-9-iry4wZ-jKXvYve6nfDCoH6goQVUMnQlgIAxgd9GodkijiHYzKFAesmAR5xX7yiSVkpv1PUtRWCEEeOgNikVaoRdQueaS4m-83JBH5CeloguGTzo1qPyswwiWIg1iWk6UQLh6KpFm986CiDtkQnIFPGqwDCYiHMps3lNUZNYhOmt36u0afDLtlM5G8u_75zOWMmfwWz-whoYuPcHvxUezPNmLnqyVulgscLH6z4RsyuP4ir4aLLXU5lnVtxBq6W924Q8BNGqX2ADOrFoGS2lZiq4sgf1EYLtT4gygLqJTjAGa-RtkJn27-mSe4J138Uz2L_br46aWAgzvCXeA-yqoCRDr074xISvRxBGFKla7sAbB67h-CEjw1GeS6B5OzNQ7E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/164942a925.mp4?token=DPsAwkIYQP0L3sMg6jlVim1IfxUuzrSNX_nD6I3GjY90kbNI1iXWYPIgpphwvXcbeym_lxJTQJX9HzAvcZacf4GxWnn6iTH8HUQam0zp2_gxXGiTLp2hMgPc0KKFYUkU8X-7zCB5TJ6HtJYhsWK5Sj1HWhIYmGZZJnw86lZLFqHGLZq-jbU37a_VNqU0fRqjtnh7OYtImAUi_SFCo9hbjM_6nEnvgrMMCDzukbqnFr1RkaAXe12vdWm0TwlhSyQj_sbJGTmPG6kJLItcsGJ95Z2eLcbncXMIioBlRVB-9-iry4wZ-jKXvYve6nfDCoH6goQVUMnQlgIAxgd9GodkijiHYzKFAesmAR5xX7yiSVkpv1PUtRWCEEeOgNikVaoRdQueaS4m-83JBH5CeloguGTzo1qPyswwiWIg1iWk6UQLh6KpFm986CiDtkQnIFPGqwDCYiHMps3lNUZNYhOmt36u0afDLtlM5G8u_75zOWMmfwWz-whoYuPcHvxUezPNmLnqyVulgscLH6z4RsyuP4ir4aLLXU5lnVtxBq6W924Q8BNGqX2ADOrFoGS2lZiq4sgf1EYLtT4gygLqJTjAGa-RtkJn27-mSe4J138Uz2L_br46aWAgzvCXeA-yqoCRDr074xISvRxBGFKla7sAbB67h-CEjw1GeS6B5OzNQ7E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
👀
برخی از سوپرگل‌های بیرون‌پا رو ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/Futball180TV/102171" target="_blank">📅 19:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102170">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoj9O8u2w1hi1S9tQztRtwls3r-Stm04PBqjsKwg6HP07zJcRC2L_IAgRHRIwFBg3KvMfXRym0-MSzUhG2P7SdOFpvDE5s4TnMgONX1PjFHopNEPn3E4DW3sO8HKnIuY_GBSMoPE7u3OGxT0dm80xTAQOj5ynkQKN6BbvCTyg4lzmbqmxEULmEEIg0iOc5AWCjIfQQvmgPhJKX4-BSddT2sKvJgHT3QfVkXNcIAZE4wHzrS3NpDjW-WtaGWC_IhPDNVAIWUE16GsHtZqRb0x3yoAccrixXQzeYqUbp2QkxuxJGcU_ITenpMlD2_EyHQFtvEKSM7T2ThKWUKhZ1I0Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
‼️
منتخب بازیکنانی که در پایان‌فصل‌آینده بازیکن آزاد می‌شوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/102170" target="_blank">📅 18:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102169">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjb6-pnzDmprmuJk3LPiBPFtcL2cPuZU9SV5FkcUCfUfkMdOZ4zwgO5mL4fCkg67G3evqQdiCaCS9c7MEGzSOoHq5M8k5g2R8jCgMX-XHOG5ELhbkM2oj-wfBwntKToZIGkMPkaMeLFS9DwybAowiSBOu02CW86Fi8UvDQPK1fZcawtQOr7YwAjWSkuZFzIzeC9hx1hqXapSJeVJUY6tcw0Xop_h84JpWn6Oh4OQjbgdYC9ZW_85trPMt95sRb8-afWRYnxHAtYSBGZnpGu2lsbavCxB6PqWflzlWk1bLhu8MkwkrPKFtT20yTrQfm_Aln3gdQT-9WJ6Bwt7OMqhWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔎
🔵
ژابی آلونسو بعد از دو هفته حضور در چلسی سریع متوجه شده که تیمش برای قهرمانی خیلی جوان و کم‌تجربه‌ست.
‼️
اون گفته به بازیکن‌هایی نیاز داره که تجربه و شخصیت برنده داشته باشن.
🔺
جردن هندرسون — ۳۶ ساله
✅
۴۶۳ بازی در لیگ برتر
🔺
دنی ولبک — ۳۵ ساله
✅
۴۰۰ بازی در لیگ برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/102169" target="_blank">📅 18:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102168">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYoBhxsxdKHAONZ3jtq_svla7rdRx1cSitgfTM4bXNxgaAX4LRw8A4VKYqAvIbH-HDcMrYUUmP_Qqh8LN5ZwPqO286BlyNgHOqj95M09AOG7lhP9JOnsvB5GPa62vN_fltwWJ-pFM1gnRxaggija6Ob0G-Ph9dIe5_ukw9fp-MaCTNyTAPczOy-rbCMW0qs-9gapCc7nWCeztL5spSudHxYm_8M4mTnKxSA0IC9m0LzNZ1HuEcVpYyfWdMjYoweNHm9ZjCPYeqbDzIY5HFaGyCDyx7twAeO592RKxwDFtFhL4IM6taQJ5fS4Ve4BSuuX5-tFVezVJ79StsF1hriFTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗞
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: ساوینیو به منچسترسیتی گفته که میخواد تابستون از این تیم جدا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/102168" target="_blank">📅 18:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102167">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVNKw5JVl66Szvb2AkjuukNI7zu_4_qDBxj6SEPkFRl-ecUQKSqIA09x7kh0t_5m0CUbTqWT8moSgjREbKKlGRdr3uqZwATffMISpJXunUjaNSGC1aQTjZuHgb_qZlP3kL5Isfn7bMytT0AaR8g4JWIlvalyrtq1znXVgeNnjVcYm8phHU2y75gdrsk7wHsqwp2U_gb5jfh4L6qjOX93Qsb6FpfvqL-UMLoVtES4e9JIKx2hfNV6z-AsbMXVZ3B97jamQBDGicJgXGnsWnMjTe0E2r4P0b--QGXd143fD0dJzO-gC-oAer_x_O8NapB6NbhefS_lF0yv2S69ZgVYTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
نیمار جونیور درباره لیونل مسی:
من کنار مسی بازی کردم، مقابلش بازی کردم و باهاش تمرین کردم. باور کنید تلویزیون همه‌چیز رو نشون نمیده. سخت‌ترین بخشِ مهار مسی این نیست که جلوشو بگیری؛ سخت‌ترین بخش اینه که قبول کنی بعضی وقت‌ها واقعا هیچ کاری از دستت برنمیاد. از زمین بیرون میای و فکر میکنی خوب دفاع کردی، اما وقتی صحنه‌ها رو دوباره می‌بینی، متوجه میشی که اون کل بازی رو کنترل کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/102167" target="_blank">📅 18:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102165">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vq0iXaaicdVpXAmuSld-PH3gH3h0pTysAdTFHR49jFwKC12aMFqcTRiw4QRx-CZqfvaA4e_1yVK9YJTnTbwujJyWWmMTxDS163rPcbFUvMWksQ2NQiWnjPlWQ1rD6ew2G3wpGuOdyHeBLdeDgAwdIJFeN8sMnRVGWrdzvybHN8MQaCdSJLhZ2cQMumeavPjg-97LI3nEtp7u04LsFZSD_U8Tb240-6ERuLUX3eWjr1AJ0WybnPHJ5gvVOxb9yh1ExdJeNN4YHMQZmIwd0twoRqlw1PhLIdrVyqhCcUMiF-R0gDQxVj0qTfnnrAe3Pyg2aLveumUsfOa4ki8I1Otjzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LD5ka-4F9pbmf4NfyxziuDhsldzHyeHdzv4vuzChAInisz0dTBMIwJ5ehhtSk8uIxVj48f8XhjlCO8GGTIONfADkmbWeYq2Jbc4goxc7uHdAQ3SnJozbPQTb3pX6UkqQGNacKYDPzhRYO2rKHvZKEzTz0nAE9uy7V3y0M-2Udd1nmUJ99aaPd8IUZzX27GoiSGE-pafIZcaE14CctrFJ1bVtq1vC1-8mXx9gnsA_Ih9Q9DF9ih6DZFa6TqAKP7z-621HHEfYhj2cR5aN7EGMNZyopzsrFomoOGmKalw7g95r6O5Ydn0jrcsjOoTTEE-iolNRfsyiaS3t_k4EI-ZpGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
🇦🇷
رودریگو دی‌پائول درباره اینکه کریستیانو رونالدو خودش رو بهترین بازیکن تاریخ میدونه:
این نظر خودشه! برای من، لئو مسی هنره. کریستیانو رونالدو یه ماشین گلزنی فوق‌العاده‌ست. اما شماره ۱۰، هنره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/102165" target="_blank">📅 17:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102164">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WagISHqPqPD3xBhl3TjGbm53-h9acJ32rLFhXFHNSa328c3whBqZ2GnSaq7Rnzcne7Sa8vkl9ZgCeuokY7OWXxZj5Z1EwtU-ldNhQCxrJ_v_XvCfetbVntQfSyG4i6Xzo4b5Ut5N0PeXPU3FcMwmGuIABHSpAavpU0O6phUfk5g1Ro4iOIuSsWE-Wx80GZF94U3cR1U2tf4tIeZ30ktJMuuzDsnR1HkknEfcd3oydi7pKTEeHyWLbVaRLEy4onMa_pgpvCy4M1fV-MSw7hXjqxtQrDZ0-EHGlXW0uQVPJgFKPCovxsO3OaQegsAvamVOpBHza8FLG1SF_aVFLRIv1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🤩
محمدمهدی‌محبی بازیکن فصل‌گذشته سپاهان به پرسپولیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/102164" target="_blank">📅 17:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102163">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">برنامه کامل فصل جدید لیگ برتر.pdf</div>
  <div class="tg-doc-extra">34.2 KB</div>
</div>
<a href="https://t.me/Futball180TV/102163" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚨
✔️
🏆
برنامه کامل فصل جدید لیگ برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/102163" target="_blank">📅 17:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102162">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🔵
برنامه بازی‌های استقلال در نیم‌فصل اول:
🟠
🏘
هفته اول: مس شهر بابک
🤩
✈️
هفته دوم: نساجی
🟡
🏘
هفته سوم: سپاهان
🟠
✈️
هفته چهارم: فولاد
🔴
🏘
هفته پنجم: پرسپولیس
🟢
✈️
هفته ششم: آلومینیوم
🟢
🏘
هفته هفتم: پیکان
🔴
✈️
هفته هشتم: تراکتور
🔵
🏘
هفته نهم: گل گهر
🔵
✈️
هفته دهم: چادرملو
🟢
🏘
هفته یازدهم: شمس آذر
🔵
✈️
هفته دوازدهم: استقلال خوزستان
🟢
✈️
هفته سیزدهم: خیبر
🔴
🏘
هفته چهاردهم: صنعت نفت
🟢
✈️
هفته پانزدهم: ذوب آهن
🟡
🏘
هفته شانزدهم: فجر
⚪️
✈️
هفته هفدهم: ملوان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/102162" target="_blank">📅 17:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102161">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🔴
📊
حریفان پرسپولیس در نیم فصل اول:
🟣
هفته اول: شمس‌آذر
🔵
هفته دوم: اس‌خوزستان
🔴
هفته سوم: تراکتور
⚪️
هفته چهارم: ملوان
🔵
هفته پنجم: استقلال
🟢
هفته ششم: ذوب‌آهن
🟢
هفته هفتم: خیبر
🔴
هفته هشتم: صنعت نفت
🟠
هفته نهم: مس شهر بابک
🟠
هفته دهم: فولاد
🔴
هفته یازدهم: نساجی
🟡
هفته دوازدهم: فجر
🔴
هفته سیزدهم: پیکان
🔴
هفته چهاردهم: آلومینیوم
🔴
هفته پانزدهم: سپاهان
🔴
هفته شانزدهم: گلگهر
🤩
هفته هفدهم: چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/102161" target="_blank">📅 17:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102160">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlObJskKKrx9Po9y6OLvAuHxfaDQxTgMkQFPJpEzv0eh0OZzfoMe593-zbYYSc4tB4Q5RU_Ay-yiA4JfK13zvZp6g6m52QWZYjwsiWp7heWUhy9TUJeAXJMp0tHEQBTI8Hz5jT07zo3FdQhyoUGnICczv90ReCIf9qVmlBodaSqBT0TVM272ad49hCYIKBo0P6xpMyphU7wfm6XcqSvY1md4Xi5uBziPokSvWrwlssVIAq14lCCL_Ll_s7233AzOiJ5DM4Ap0nYt1kgYc6mvkSelHexOgX1GMDQrptPtqC4AgHltcKN_ds_4ROCxx6ekw-HnWfsSEmluUgTtonmINw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
روبرتو مانچینی رسما به عنوان سرمربی تیم ملی ایتالیا انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/102160" target="_blank">📅 17:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102159">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzgFRUA5qXGmmHLHiXAW08HIMbtoYgI0e2KZuCqz0dOoTqIYu90EiQwq5vm7kJkSnwAuzV-H1f03WzM5QJe9yR-VxTXCl85OWQ5R2sgTXnubwB3w_mNgenyp-sBKytrAwu2Mhjdh2jZLyvuovGEd5aTI2cRLKMS25O1icqgj5j6BWfP-Rf78f2VCByj6wUkCTEdJimRwsjaTz0fyoMlqGrcoMpZNguucCUmDqx0nJ9T-OvC7aQJKas900-t9TJbrGULd5y3AECyDiEpPRUQlEuudv9cp-LE5hXnuaQ-xjvT2k0FPL97FwAZ6CxmAuhqyl1PbPMOAWqvkFwslMRklww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗓
برنامه هفته‌اول لیگ‌برتر فوتبال ایران
🔵
استقلال - مس‌شهربابک
🔴
پرسپولیس - شمس‌آذر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/102159" target="_blank">📅 17:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102157">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpC2eyjADYddrM7ryjTL_td8U-X2R3McUhiQXIBqwcdjaz1H_P7mvQCnaBKG3n8vzixOOl2jqKrPMnOhtqcrLoGyS0mVn8-BIMBqAYYVHUDQLVkYsiBqgEQeVKUXXN09lU6tmCC3SpfvtqtvLki56qrXXJAgTjsjMr1iamLOtbbULVp2vQvxcyDMw9SXge5Hj2sl1rQeRUv8zm5i5iXrjRR65dg_7EKOLZpr48HqjJZmE3h57vrfTuBdolb1jCbaXQEje8D_dbgfPN7AivMJrgikNtp6dXfn7CTQPosJSXqNnlH9UpQ2nu7jSjC6KmmRolHI2K7VPwaHEhLZ7irdmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c787f96db6.mp4?token=V4PRM22_jO0J9r5eS2qVoN4cjflvaI_qdn6SAKkuuvGPVM9d9QSnZ-lenqNFqBvuKAU0Hk-18ZuubErXp42nQkS_4MLSkMDDs_4lqBrXtFpt4F-LTSrTOheRcZ7vFP9xoeCat3zXy5IvWh4-DEJAnl2YxzyuHdjVt-lL47JI-kspMCt8hU5QF_W6eu4Vhy1BjTMyXIw6y_up2WuX4b5w11DYMLMuQuWOqCv8GZZwoji5b1Uex0xRDURm0nFU4ZjH5hYl0YxwKFn6r3B8zTKRNJNvPW7kRv4giH1t0y3GIlBppVREsXOQEG-fTlf19tX5JFcN530MiKMxvxNEbZj_dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c787f96db6.mp4?token=V4PRM22_jO0J9r5eS2qVoN4cjflvaI_qdn6SAKkuuvGPVM9d9QSnZ-lenqNFqBvuKAU0Hk-18ZuubErXp42nQkS_4MLSkMDDs_4lqBrXtFpt4F-LTSrTOheRcZ7vFP9xoeCat3zXy5IvWh4-DEJAnl2YxzyuHdjVt-lL47JI-kspMCt8hU5QF_W6eu4Vhy1BjTMyXIw6y_up2WuX4b5w11DYMLMuQuWOqCv8GZZwoji5b1Uex0xRDURm0nFU4ZjH5hYl0YxwKFn6r3B8zTKRNJNvPW7kRv4giH1t0y3GIlBppVREsXOQEG-fTlf19tX5JFcN530MiKMxvxNEbZj_dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نیکی نیکول درباره جدایی از لامین یامال گفت:
من قبل از لامین هم توی کار خودم موفق بودم. این لامین بود که اول بهم پیام داد و با وجود اختلاف سنی ازم خواست وارد رابطه بشیم. حتی گفت ازم حمایت مالی میکنه و هفته‌ای ۲۰ هزار دلار بهم میده. همه‌چیز خوب پیش رفت، اما بعد از مدتی دیگه پیام نداد و منو بلاک کرد. الان با مدارکی که دارم، میخوام این موضوع رو از راه قانونی پیگیری کنم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/102157" target="_blank">📅 17:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102156">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
⭕️
🔵
🔴
دربی پایتخت در هفته پنجم لیگ‌برتر برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/102156" target="_blank">📅 16:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102155">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcXt6VHpJyLQD6AVmFxHgIgxN6YLXGgoWSHVkWv--bTYLU4_AIbgOUWlvku2Bzrc8KQnNRa4pFEZava8iKd_ONWsXeYEj8ZoD-qZfLZL8uh5KegKFOCnxGBAdktxf_MlkpFNwWUpJqHBatW1mSphbinC-Nd3h5EpqknL-3a7Y54W69lxy6e9tcoYUq2HP70jCrKGWwp63voK5CHOJQW5_aBylvUMTzV1NLGEzGkX5D9iBOKTNt1OqAIiPhRIEquhZ7jQ2EkYQOzqZ2jZ8WfY8Xa1gA6vex-vOrDpnSQ9zdJ0lJL1gLfuLq2oP4kLL93CxH-5KFqPTLeiCR1FrLLgow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از نشریه لکیپ فرانسه: لیورپول با بردلی‌بارکولا به توافق اولیه رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/102155" target="_blank">📅 16:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102154">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1LMa9Q66cuGTRuOfthPVQRdr9OIo3EHmWq3WAqZv4QgHnRGDqn9A7jReKVqQ-3ZPXsjS3LFjZDYfbiL41GU8AUa0zIa1UFM78nlS6bqu3Ke1hHD07WlFGpL8EQOorekG_7kiMVn5T6GkmBIv7rtlxeDgoaYiVcK45Ij3EbbMKytcLL96Clov4Xngai_jynHHvMYvsRVzVe_Ge48Yb2jgJxDmlhBlDLXUi5R7ylcGgCUDLyCeNMeOeS35XHbfiRW3XqZxQ_3vOzOUo12oaIAThlbuq9kTZFfNB8i-GfSRnOPPywuG94tovKMrm_ixsVWaiCJn9oNFowA8EZYFyHL7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🔵
🔴
دربی پایتخت در هفته پنجم لیگ‌برتر برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/102154" target="_blank">📅 16:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102153">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urtWxM_KkDonZGYAM74oSMQgeTGhfkIJOoLc1OUTP-MEjvSyb4qrtJcpUvU_z1LI567ZYNyxFD1URVUUV1VHBetxp8f1CiH8OGqSoDy7-jVFXyDkRG0hHGhO4MXh_E8vKB1LyOmd4sC4NcUFQGlf0-AE3ikG1hSCfF1ZyHloRt299Vg3x6LRxSjObvw7rtD6RVGAf7-e__-8CDfXHzATyaGHOEBGqzlYjV7lmaqmhwyXjtgEPMS9lWfirkV4rwqTpSoLzxDYS5AwLlV-PNReCVNE5KKHG05dmabcVKG6nw9vNUEqJgGkjOjvpOeIxzdVceSbPYI5H9rtn-851lBvpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🤩
محمدمهدی‌محبی بازیکن فصل‌گذشته سپاهان به پرسپولیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102153" target="_blank">📅 16:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102152">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5WA6Qk8QfdVGPeUEAKyjV7yZ3iFYE9TgVustaZfook6OX8Sj5SUn8idSXJYsxT828dFIS_xkwUDhaVsgSMvsGKlH7Nf5sRwhlscMqnP1MESIhAdkKhXjZLgU_ieFEva7EpGSQGCOIQYkMrnSGSutJuimsvUsH7alDMvcrI8577j6Padc8lcIMUXb27t-QDdsEmr6NMAHwuVzjtiz-yxfFlAfA95C7CdSqlZGVYq2KiwbfR4q9e36g_y1uQ3yhcsJkeaY6vNEfkaiWLaKskO8i_eNfkCO01Ql2iLveNuLOGKNU4JvS7PKd6PLbV_4p9fGVNARyTciMLwAc_4yH4g7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
#فورییییییییی از رومانو: مانچینی سرمربی تیم ملی ایتالیا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/102152" target="_blank">📅 16:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102151">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmnOI1wHHLZ-DSvIVIib3E-LbipKc9WShrOJ1tXWaqtmI19mFp8bwQcYx3BtWQ_PhyNi7Dt-eoCU_iDOwIJ9We324jGAWBCaAE6OIeY74Hb-jZuG2n012xH-AxhnbCelhb9H7mfYpk4HVZJ3vaSzY00qX8CEYpMGTGcRNA1KQ8687w47ZhV1L2prrrkr4LNhzdjXR7Ha4le3nhx0b7v1_n_Mu-L7quy3eprUlbt0aRXK-AXkh59ZXbebrAQIEWEa5YrWOiujFobZos2L2Dd5APq37PFRGV3oL6N9pfhZdqnPe6xASkuEV6URtQG8_zLUQtBN2hUTJBr9YtP112vn0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینترنت سیم‌کارتتون زود تموم‌ میشه؟
چون ایرانسل و همراه اول اومدن روی اینترنت بین الملل ضریب 4 اعمال کردن! یعنی شما 1 گیگ استفاده کنی 4 گیگ از حجمت میره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102151" target="_blank">📅 16:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102150">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/881c68dbcf.mp4?token=t8Aui_UJRHfbOjkdB3-H087DGTzWZ29p038iNQFUXtvKmmQRkGWg0H9Bl5d3d7sD13hItCaP_pN-2fGxQVnnzMvTKDgh4DtFB5a1BTkzsZIsBjBKn5e08CXLuCNYTdzXDuucdmbl5cIoK-rracUIRsd7v-bgdVYNPr7iMhOBFVsZQlJAZYta9X2c_ktIY_XmdxF_DpOqbcwyvUdW7gjjiuHNW_b1fEqdUQR7Jq58Feqh3OJkkLEOmlYI2VIpnpoxchP5crlO1VelsDHq4NyFdPKgtu9ez3Ck4VCugDBMH69VG6-OurytDzJO8_YTOa10OEMMi8GLdjGfRym70tlEDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/881c68dbcf.mp4?token=t8Aui_UJRHfbOjkdB3-H087DGTzWZ29p038iNQFUXtvKmmQRkGWg0H9Bl5d3d7sD13hItCaP_pN-2fGxQVnnzMvTKDgh4DtFB5a1BTkzsZIsBjBKn5e08CXLuCNYTdzXDuucdmbl5cIoK-rracUIRsd7v-bgdVYNPr7iMhOBFVsZQlJAZYta9X2c_ktIY_XmdxF_DpOqbcwyvUdW7gjjiuHNW_b1fEqdUQR7Jq58Feqh3OJkkLEOmlYI2VIpnpoxchP5crlO1VelsDHq4NyFdPKgtu9ez3Ck4VCugDBMH69VG6-OurytDzJO8_YTOa10OEMMi8GLdjGfRym70tlEDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
من بعد از اینکه توی مستر لیگ PES برای دهمین فصل پیاپی بدون باخت قهرمان چمپیونزلیگ شدم:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/102150" target="_blank">📅 16:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102149">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmba4M9vSkL-k4zOEo7LSrwY9V3jrGWLtEipKeLy_nKDTQZz6ZSq0s1OyEHA0cjI9c_zrL5NkDjgiDLir-R0C1RRmIjAEfU0umD3cZvPyVzAWifnlaIAkecKNucr2eJhVG-n4Dw9rE_SCMSutkmqjBrYJJt6MlvhZ4EX3cfnAjf056bYTW-gYpj7yNoN3aV3Y2gESLL6Np6fT_p0_J38zzTsPBbqNzMr6DFpVLmNO6-GTQywInex54IrDfoKkoJyOQ8Tk3ggRFJIngJaYTe_lFwxDJ2ezEQGJyZxHVXOTwLWUkDmvC3dmoNLO0YvsDB9o8V3tzWuCTOvok1myXYyUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🙂
✅
کوکوریا به قول خودش عمل کرد و بالاخره عکس دلافوئنته رو رو بدنش تتو زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102149" target="_blank">📅 15:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102148">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyDUNfHCSIIgkHAuh-k-XcXJQn7HJvZfrlsBH9QM4-QnoOg6G1t7IA9rWaViKq0xcEeVf0PVt2priac4Qy1mrHiMI-9A5uoRYm2WJw8LGyeflohxJhNCU6s7nml-oIUcnVkdPb15vGUSsEsI3G-2sCb5sIDCtvQGJY77M0-MBRtvO92O2C9jbFvradES2vzTDEUE1msa16fTf36D6oVX7mariygXrcva4Id0ksuoS9XLWkEF4m0idjhrpYMRWicfkta1FJKUu3gcllyeaW_oUDSnRVNEJ80HfWe2SMv5fLK4XtjsQzMu-Y7ETZXvEjABS_3qPGDcZSYbIcVzY_Bhzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🔵
رسمی؛ قرارداد یوشکو گواردیول با منچسترسیتی تا 2031 تمدید شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/102148" target="_blank">📅 15:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102147">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f242c0afa.mp4?token=he-LiNg6_9T17biursuiLERmgdjkZTxlY21EF4-2fc9d5FWI90R-BV24FdZywm0HbYRIJHuhGJCeqRtAnrBOKdvLML1fNG8krpHlsXMqcvNP-ZjSmrhWwcDySRvU3w66A3eeenVuKym67rbmGWiVsL30-9D6FMrpsXcTP9-LsyxQsny4_eUgspOshF2n2EJ5hqZ4a64WI7XgqRA_ie9MKuydT6xAlsTEXRmXekZ7oxR7Ao7nvZe_8IiCg75lSw4DRvfTNIJvM7SI27N21ud8zhK8647FBdPXL3_W4Fm4UBzhJTZt3okRMdP-MD3rnDgiAH7iGBwaXjczZZHR_iunIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f242c0afa.mp4?token=he-LiNg6_9T17biursuiLERmgdjkZTxlY21EF4-2fc9d5FWI90R-BV24FdZywm0HbYRIJHuhGJCeqRtAnrBOKdvLML1fNG8krpHlsXMqcvNP-ZjSmrhWwcDySRvU3w66A3eeenVuKym67rbmGWiVsL30-9D6FMrpsXcTP9-LsyxQsny4_eUgspOshF2n2EJ5hqZ4a64WI7XgqRA_ie9MKuydT6xAlsTEXRmXekZ7oxR7Ao7nvZe_8IiCg75lSw4DRvfTNIJvM7SI27N21ud8zhK8647FBdPXL3_W4Fm4UBzhJTZt3okRMdP-MD3rnDgiAH7iGBwaXjczZZHR_iunIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال به دنبال جذب وینی.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102147" target="_blank">📅 15:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102146">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea2f2fd87.mp4?token=XSutlN2LMt9WSYCjrJ2-fg5eM8uyby8Q25c0xgbuVds9yXm2DjgNo_xzgfI2gEGip-5nZ-DvwlU9wEUW9FLTSwQ1HS4CFuTTjXDp2uiKGe7r0U4qz8G3Lv8AaZZmyr9fRC0tpnQDbh2hGpR_CqV95nLkH8bl1zDgATRSeDaLSq5TMwU7gXb8BeM8Ui7NcciEMG80KgeVBr5PVGHnNJ38Avjh5uOeUthbrVf67BGRIa1HmNhLQFtHr1L1ZwZsbhxa571qGF_m0eLszX8E0EUQb61EHjD2mkruThqDcNNamF8VUWz7wHUBJxapEY46ZpND39zYrcBkKVyM4kjCPMbowA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea2f2fd87.mp4?token=XSutlN2LMt9WSYCjrJ2-fg5eM8uyby8Q25c0xgbuVds9yXm2DjgNo_xzgfI2gEGip-5nZ-DvwlU9wEUW9FLTSwQ1HS4CFuTTjXDp2uiKGe7r0U4qz8G3Lv8AaZZmyr9fRC0tpnQDbh2hGpR_CqV95nLkH8bl1zDgATRSeDaLSq5TMwU7gXb8BeM8Ui7NcciEMG80KgeVBr5PVGHnNJ38Avjh5uOeUthbrVf67BGRIa1HmNhLQFtHr1L1ZwZsbhxa571qGF_m0eLszX8E0EUQb61EHjD2mkruThqDcNNamF8VUWz7wHUBJxapEY46ZpND39zYrcBkKVyM4kjCPMbowA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇹
اولین‌بازی روبن‌آموریم با آث‌میلان:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102146" target="_blank">📅 15:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102145">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfBgxnBuEnK1aFhxzYI1ydQGfF6b5KpzFtpsqUXy99ecr651qbHYvvWpBJfghX42SGgzTKhJA02n88LIqttLWfYJI7eo4v8mWgTIu6X4D5La4sWT9c6UBLZGOAwDUF67TZGMNdBcJ92CXnc1Higrxdezz8pNwbi4rc-v3s2BKaJIdyAI7S6Nj-sr3yX9lfLBnwY5fqUGSKVHVy41qtSqpgXkh6w5ZHCXKyekCvYl2y6P04bq8jF14XjlBtmGDzcVSkqT3VJC7PQ4_xXC4rk7JC-C6dqNjcGmBA6YOr8EhHdti3GS-WhWqzTFEpf5n7tt_KiSOT-GnX7QM1HjpVP-xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بازی دوستانه|ترکیب تیم‌فوتبال چلسی مقابل وسترن‌سیدنی استرالیا؛ ساعت ۱۳:۱۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102145" target="_blank">📅 15:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102143">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EOsPkChsUeRCu01aoiCtAWvm5doPpnhoScF8EigadQHHG3hRX4FpEqbtBJnhz6Hm0jKihnC6NDWIBPy3_qZb2w-rQOQVJUuukQOudCICuhTbPXrf9EDytEdPsC3tit-_jmTUB25NIvOJuv1BOV72HtUX8EKVbRYpcVk5Yy-7CWwgpAAKMvWw_jbrSpmwVjC7ytmTz_gk4IHlQXvYBPqcud99smLPGn7MkZ9ZaLTYduqd8biQeac0uvXDwu3Zvb0yjuDS7BHU0sYBRGXOQ7_r9h_R2L5OVT51rarNQZxRgPe0az2xflZkLd-ylgN2z1edeCdFvqa4Gy4rpN65kQQF6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LVoIofhK-aXnxWKvYDk-7j4sr4Buqi8g25osgx_BSBvcQ6j2IWS69cmhqDxUN0uCyBpdT91yhHkGOWFVliS6LT9edajnaSA8Zn7eAr-BWDE7JDyYMaxMHuBepc1q9e9Doo4k7TzH8p8WkPqcKgoBjZ4_G_x4kW7EkWVkygPTxD3qC_oKzYfhyJZYa21jAagyKV1HPMJVwBaPvkjhYpHbFrC3fKRIV9ZbKtzH1ZTSPsfggGsCdIssLnWMhWgZXSgWGM38DBPAErvBzcHyGjkfHYkYOghqepX3lZDIxk7eJrUkovsuSqfWFSkl9PGUmBFtjny4KJMLqUopdquY7eIPyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
👀
مائورو ایکاردی گفت همسر سابقش در جریان طلاق درخواست کرده بود:
💰
۲۵۰ هزار یورو در ماه برای خودش
💰
۶۵ هزار یورو در ماه برای فرزندانش
💰
۱۰۰ هزار یورو هم به‌عنوان غرامت طلاق
اما قاضی این درخواست‌ها را رد کرد و سیستم قضایی ایتالیا هم درخواست تجدیدنظر را نپذیرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/102143" target="_blank">📅 15:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102142">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btKPgOiakNKl53N_qnR4PubCQ0NNZfoGA2v0SFO7aQIwGCd0YPgI6DNTzke_pvg3HWnuX0SKz6O1nqjNtwoOJQ351uWanMcqQ3hYGWDjH1Xc-YYQjqPqNPbM4AveJgB42NhAOFjS8-DfSpSADOk47N2_fPulN2W-aWWhP0sv23RPt6h236jVTOyDdDV-peK1nATxE5Kt07DRoN8IM17dpTAi_zl1fwQaLy9QMSLwWPPgfISP6m-8021_iwmY7iLR0LKEHEJeV7ZGBZuDDIS9BNL_PX7WHv8SQ3cMWYjyYE-0MnqtDp64htpfmDZCFYEtC27no4_tna985woq9lIWRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
نیکولو شیرا
🚨
🚨
🚨
توافق حاصل شد: کلودیو رانیری، مدیر فنی جدید تیم ملی ایتالیا خواهد بود.
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102142" target="_blank">📅 14:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102141">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbGYpkD1jDEFQrZgnMmyLjxGDYmuF13BxasyhjYiQbMMvqQic-HYG-G6A9hrH3Xh77_crjvsNHJhe0Y2IHc-cilYwqZxaLoiIFmY_JMDAEsFzu7y4zVlzMdtqCjQbgrisoZaBUFvV3MUoB3fyF8repY8HgLoYfp9splQrl3NQo4525V8i7_n_zqq4BEr_EmdcWka5hahPswmXjGW13Bxi8_kBymtVsu749uswA7ooTqrMSjL3sb5hkMNZJma0nKH89mAFteEeCKPxBo65ydKIr8CXdGaK-OEIgy9dmtxIeD9-uqV4NpSL36E-3iUQCP2pxWQuE7EnheINW6o6MrunQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
#فورییییییییی
از رومانو: مانچینی سرمربی تیم ملی ایتالیا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102141" target="_blank">📅 14:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102140">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/922dff29be.mp4?token=YVWni33M-WNfTQHdgixQEEghi26eiRGIwVI54je-OwT4CDeu3TnVx6uQZNUQqogEB_QN6N3SWNXS5sHiTcuyBygbYEpECm4qcK5TMAQpJ47VvxvBbiXmJdTL-nVvUYgBnEB6Pnzk7mPTOwI3m3Idg59gPXUTmNa1b4oxkQxdZslEchcBet3ajoV7WP9LwVt43IZaeAQIePpzLU_B6BanO62yPyFKns9aBvAhepr8JUJ326u56wTtfCsIy8PUoGnF6X3S1KvhWQF3J8YQ-CNDqJ1NqN1i6n2V8VLV5KBQ4I3si4HUhYdejcDR6nm6IXeTSzP1oubBdhDbaTwfQyv3Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/922dff29be.mp4?token=YVWni33M-WNfTQHdgixQEEghi26eiRGIwVI54je-OwT4CDeu3TnVx6uQZNUQqogEB_QN6N3SWNXS5sHiTcuyBygbYEpECm4qcK5TMAQpJ47VvxvBbiXmJdTL-nVvUYgBnEB6Pnzk7mPTOwI3m3Idg59gPXUTmNa1b4oxkQxdZslEchcBet3ajoV7WP9LwVt43IZaeAQIePpzLU_B6BanO62yPyFKns9aBvAhepr8JUJ326u56wTtfCsIy8PUoGnF6X3S1KvhWQF3J8YQ-CNDqJ1NqN1i6n2V8VLV5KBQ4I3si4HUhYdejcDR6nm6IXeTSzP1oubBdhDbaTwfQyv3Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
⭐️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برخی از سوپر‌گل‌های معرکه استیون‌جرارد اسطوره فوتبال انگلیس و لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102140" target="_blank">📅 14:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102139">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👀
▶️
💥
هایلایتی‌از تقابل تماشایی سه‌فصل پیش نیوکاسل و پاری‌سن‌ژرمن در لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102139" target="_blank">📅 14:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102138">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90f94a2bbd.mp4?token=N0XBRLfmZfI8Bbrfxc92G2F6xMNRdqBZLkOXBIMeLH3msz26E9csj2X68gVb8j2eVB6juofaMB842YhT-SxRHTKrthq69USXVCb79-FoN3D3PuGqObTJvFFND3zAyfhWrXYlhp8GAiL1QAU0R2vRN6663MYTI1dHu_e4tHVGzXfZIKjlnUUDKSG49AAdfToH_NPCI7DL88n4fyNwYnwXMEGU6bkeZqv3vsCJ1LC7UeOcvcFFryKika-tCbuq-3LVbZpDHyhgQOiTpQSoMZsl79yk0ic5pfiponUR_u3WqQwZMm_3WLIFC-EJNUCPnmfhztdFpbuPw544Z32lINGnEIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90f94a2bbd.mp4?token=N0XBRLfmZfI8Bbrfxc92G2F6xMNRdqBZLkOXBIMeLH3msz26E9csj2X68gVb8j2eVB6juofaMB842YhT-SxRHTKrthq69USXVCb79-FoN3D3PuGqObTJvFFND3zAyfhWrXYlhp8GAiL1QAU0R2vRN6663MYTI1dHu_e4tHVGzXfZIKjlnUUDKSG49AAdfToH_NPCI7DL88n4fyNwYnwXMEGU6bkeZqv3vsCJ1LC7UeOcvcFFryKika-tCbuq-3LVbZpDHyhgQOiTpQSoMZsl79yk0ic5pfiponUR_u3WqQwZMm_3WLIFC-EJNUCPnmfhztdFpbuPw544Z32lINGnEIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚠️
امیرحسین صادقی: از وزیر انتقاد کردم، به دادسرا احضار شدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102138" target="_blank">📅 14:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102137">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rZySUpoedLvmValKfuRzVO4_ywSpLcv1IxkIU7w_llg-lYT6zveoEe5kKzE8b231KRSxTl9cQX6Fyd7RAsrx8nhl8xRsfpPj2PaTqF1Z0HNj8QRyxcvvT4WaWWwJm1LtshCMzApAaNTRWdGS0CaQlCIi2nm5kM7mBq6py4B-lMZxquuHcfDpKxZSni3ROBI_WbfTcfCwdJGmw3Yj7_eUc8ZAj9O9FNXakwu4cnPslYXJW04ulorb4QWP15A6Q4EKViv3ldtiLHQ3zcRWPFekxZ-nnLdaWOCYfr_sm8gsCW-q6nhaRIYGK7Kfc4IdkCpRRUYfaCN43GFiiNpt18G1Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از دیوید اورنشتین: وولتماده مهاجم نیوکاسل مورد توجه بارسا قرار گرفته و به صورت قرضی در دسترس کاتالان‌هاست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102137" target="_blank">📅 13:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102136">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔥
کنترل‌‌توپ‌های ستارگان که منجر به گلزنی میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102136" target="_blank">📅 13:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102135">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iLiA7rKCKMSyb88wfeHFDBDLu0NvWpAG8WAGyYLr333ZzlvZ2efoHZhc8VUDi_bbiaNdj-CQarCbvCW-A-9T6seGWy3g5Twwnsy0ul-ANtgRQ9nJ1uvr8m0nirMn2W03kn7tT6NNZwoo08AxoLWnX4DP2n65sUBhCBIL_LU0KuxnRJCL91sFzbnLss2PMiewLvTkmCISEY0kKNHFA6Apc3YVUKic8-gsUlQGsUYGXeM0e_xNe0WISrfZ1CiUIDfm5sWYqe5Kjzo_bJ2F3Nu7tVoE11crd5lG4XO0U9DNPqRsmbMlF2enRKQfeyxHW4SVtJBfKAQAJ5WPz_ZNgWpacg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
باشگاه بورنموث علاقه‌ای به فورش جونیور کروپی به بارسلونا ندارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102135" target="_blank">📅 13:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102134">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/792acb1bf3.mp4?token=HU5xeRkFhQJYTScjssOMLWveWDXYSXY6iFQUgXBhlmi-i3Jn_0NaaEys_EOBknkCcyDD7HqbMg_K4QNLei_V6p5D0pCABEMyCL78BC_NOhRj1SokEX1JQSyBXpSX-FU_8DbKU_lLXo1VsHri2A4dfubtVw1yobjA4QbUjEafUkjRRJsfzLUV6l7455bQOUn6pu2zJUMnsXUkS1uAbb64n6WPqxqU3Kl8Dr79TvZsyl84mlj0CLWBhrkWCTIj2zlwffBvbhoJRwu7t8vCCvk-rTSH8CbXkkwq_zG1RBVxoF6ZKNzDSnHyDOk0BAdIOfKVx4T-mCsqkSqL47bdJ9b_egji9M3qztq35_bVM7_ldChygf20QG-StAkTrTSKS5mHUB1z1kqE5uW_yHcXlpsQYlo-N36mN9eHyjwtcmUc_yxmRZKhRGd494aCMDSPmjkeJTfeQa5s22D2ouaOQaFuZD7pneA7kKnCez4u_yKU6FtL0laFOs8uRpPTmBYuSUM0axx6nBwCTT0t3OwK0qvFqxXAtBTjhQP010-cFeVCZg7bmf5dSu7QPLNNfiluqpNtLcsNEnSkjaHO97GvxvncBEZgpMdhj_lTSwG9iSFfPiYEn0NXvdT2iPtBWY_aGrCb52UrmZzA4NCyba3PemXDBv6a3SL8GPZ0HN7_Eo5bIo8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/792acb1bf3.mp4?token=HU5xeRkFhQJYTScjssOMLWveWDXYSXY6iFQUgXBhlmi-i3Jn_0NaaEys_EOBknkCcyDD7HqbMg_K4QNLei_V6p5D0pCABEMyCL78BC_NOhRj1SokEX1JQSyBXpSX-FU_8DbKU_lLXo1VsHri2A4dfubtVw1yobjA4QbUjEafUkjRRJsfzLUV6l7455bQOUn6pu2zJUMnsXUkS1uAbb64n6WPqxqU3Kl8Dr79TvZsyl84mlj0CLWBhrkWCTIj2zlwffBvbhoJRwu7t8vCCvk-rTSH8CbXkkwq_zG1RBVxoF6ZKNzDSnHyDOk0BAdIOfKVx4T-mCsqkSqL47bdJ9b_egji9M3qztq35_bVM7_ldChygf20QG-StAkTrTSKS5mHUB1z1kqE5uW_yHcXlpsQYlo-N36mN9eHyjwtcmUc_yxmRZKhRGd494aCMDSPmjkeJTfeQa5s22D2ouaOQaFuZD7pneA7kKnCez4u_yKU6FtL0laFOs8uRpPTmBYuSUM0axx6nBwCTT0t3OwK0qvFqxXAtBTjhQP010-cFeVCZg7bmf5dSu7QPLNNfiluqpNtLcsNEnSkjaHO97GvxvncBEZgpMdhj_lTSwG9iSFfPiYEn0NXvdT2iPtBWY_aGrCb52UrmZzA4NCyba3PemXDBv6a3SL8GPZ0HN7_Eo5bIo8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
امیر حسین صادقی: قلعه‌نویی هم مثل علی دایی جر زن است؛ کاش آن حرف را نمی زد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102134" target="_blank">📅 13:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102133">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9afeb8a4ca.mp4?token=Rpq06E-dnaF5Os_670zH6ivdVpY4kveHT7icSqpnU-sEgEVcO34Du_lxRWdQ2gzbmiL8Y4Aq9i_d9v9wuk8ngzaoRbEWsrUf84Y5l9Ur4J3PETCk9WVN0FWozZ2NMZNWS0_D7arGo_XYuYjUkxMU981Lakn-zll0Lrk1RkCek2BLIc0TzndGqDqfEIw96tvu2EecpJF2eaRBeSh6sBgZUvIJRh2lEjGOQzvIWagxIG9iNrX3Poq07PZcxNxv6iBSBxnfl8hrj8K6ZcqwRrl38a6KqrHQPTbYu1R3vV8zWB6S-pjnIaC3dTU_rhy1AtI2zUuxT8a6mm2GkNQfK5c5v37gTD_TyVHZBsanewtTgGTfkCNc4UQ8_RXCoofWmGaRD06S8e6hOE5NMTvgajK4XtsHB1qV0Btb95SL-FzvR-jNywHZU7Iw01b-x56fkDEbs0EpfS7pEFJb2jo5POZS9oBn5oUmdBqPw5FwefaLld4BOYqihZ_FXq1aIjtdBverDxjyb9sqThprlZWMIWYOE6NuYdBu9-1SV-52yRWZUHx4a5q_zVQuUvf-RDPDnkTgGp_3Uwi8aa9EqdE9d0Y7MZyfNDVFFWgG0SoqevciEgXChL4BG9zDyVxKGmvWPEvlQPCiGGXsdJuiMI22XIlYUqrK3ZEn2muL2Jp9KX3N9Z0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9afeb8a4ca.mp4?token=Rpq06E-dnaF5Os_670zH6ivdVpY4kveHT7icSqpnU-sEgEVcO34Du_lxRWdQ2gzbmiL8Y4Aq9i_d9v9wuk8ngzaoRbEWsrUf84Y5l9Ur4J3PETCk9WVN0FWozZ2NMZNWS0_D7arGo_XYuYjUkxMU981Lakn-zll0Lrk1RkCek2BLIc0TzndGqDqfEIw96tvu2EecpJF2eaRBeSh6sBgZUvIJRh2lEjGOQzvIWagxIG9iNrX3Poq07PZcxNxv6iBSBxnfl8hrj8K6ZcqwRrl38a6KqrHQPTbYu1R3vV8zWB6S-pjnIaC3dTU_rhy1AtI2zUuxT8a6mm2GkNQfK5c5v37gTD_TyVHZBsanewtTgGTfkCNc4UQ8_RXCoofWmGaRD06S8e6hOE5NMTvgajK4XtsHB1qV0Btb95SL-FzvR-jNywHZU7Iw01b-x56fkDEbs0EpfS7pEFJb2jo5POZS9oBn5oUmdBqPw5FwefaLld4BOYqihZ_FXq1aIjtdBverDxjyb9sqThprlZWMIWYOE6NuYdBu9-1SV-52yRWZUHx4a5q_zVQuUvf-RDPDnkTgGp_3Uwi8aa9EqdE9d0Y7MZyfNDVFFWgG0SoqevciEgXChL4BG9zDyVxKGmvWPEvlQPCiGGXsdJuiMI22XIlYUqrK3ZEn2muL2Jp9KX3N9Z0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🔥
چند ضربه کاشته تمرین‌شده و تماشایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102133" target="_blank">📅 13:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102132">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVf77KjXtwBH9q6JF5AsNT90x9Prs4Nes91JWtfpTKE8kd76X4c9ya00aVopC-1Ya_4uLExJnG_dQGze2ga_8fXQ2n9FmWiGyBhCTa6phJEJ1eP8KNCSLesHBUzlXsn7oCvXoE9c9PmcE-EqmYxN7F5NhO-SoOZWaZ4WEQeQiGSt4SIg9E53nQzlqpO6wVuVBK51hmRkRlAokCKUquodhNGnRvegGUyTixZCtSuM3QBzcVvAWMT4p5mlRR-L5Hi0GpcMqJjN8HETchmCi5u-61M4BlDtZMgTlT48fkVRtvkMl2LftBgkW-Qa2WLLZ4PRLat5t9Hh0h07f0squgKvwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دنی ولبک خرید احتمالی چلسی در فصل گذشته پرمیر لیگ بیشتر از خریدهای جنجالی تیمای بزرگ گل زده!
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دنی ولبک: 13 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بنجامین ششکو: 11 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هوگو اکیتیکه: 11 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برایان امبوئمو: 11 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ماتئوس کونیا: 10 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102132" target="_blank">📅 12:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102131">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
✔️
#رسمیییییی؛ زین‌الدین زیدان تا سال ۲۰۳۰ سرمربی تیم‌ملی فرانسه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102131" target="_blank">📅 12:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102130">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKPGpCIyeI0o5nrw2pQ1OKWnUUBgAAv0PpOoLcbR_U0k_IBHzyBQWemXH5wm3BMZGDCE1CuN3QL-4Vj1dDlCMGEd9KKjZsZvIUg-eQ3uW-aqNpgaJ6cu7fEHm2cu8CDvb9KqfTtweSkyzknS6iuStj4RwMKN6rmPV2hPfmtkNkAQRNEboZgEWyDsNGk960jaSXIlsKkwbQ9u1SibmPYX868k_zy_5eEDmLJ2mVT4nErcqd2_Lecb9qpc4e8oKPoqKQrGQ_OOs0s6iGK3Koq4Q7QJi6y4S1SQ-UDSTTX_MXDWMDnv54zNChGrPbSEsea3MbwzIMnjqyYn0pKPxzubcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
#رسمیییییی
؛ زین‌الدین زیدان تا سال ۲۰۳۰ سرمربی تیم‌ملی فرانسه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102130" target="_blank">📅 12:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102129">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/496ccbf92e.mp4?token=ZI0jhzCxfye7AKF8zcVgoqEbfGSTNisUxQerRi1jIWC4u_IsVGQO_DAfEPSMVrMQvD-70uCExwFM7S4FQi9ax__to90pWVnPyh7M9wD-stb8032QTF1LyxWLTJJPpW9k-1goImJUILFlhfsFct0LQ-_Sl5gkcgp3b0TR2YiDVSjQO2E2Tga1V8SBo3WEB95H7yDBY3PSUa9TSZUsIZXKSLA_azZISy9FIIF59kdu6KyawEDOPF_qZm7cmHNmHvSuHsYJ6DkxKR-TQRmh_W5uVKUu9pWeSOSFc2ZEvb9dC_CkxQdi-aaogeoNeLqrX-FyDK_QK_Q_jucthF_R4-JGmLeQh6J9Q6mzQNptqYL7tskSdlwNNokx5KEzo-V3kRTnIITXoFBEkHpPK1lmSUFRKxGbsgWb11JeHkuN_WObFLVfiXhnsjLKVRbGoBABDzzzOf6jmwLQlxFdEOs3QGijP5r3M26fkaEg9ivJZGxp7DFn5LqYwdRRqriV4LJUZ5C0bULwGu4XeGOtdKQuLqsbhZ_kyWrdpyuFxoaUbC3gtxQG23htifrgWRAGLk8zkzyu_PHBQOqycSxESSFpVD3l_fHRCyJ9EZgDtDtiy7GFGAb3HNts_W9UPDwleFFd4MGI2MsT4VllLWSgHWCl1JbRXjEesR_Kxiq-XNVvYD1l7qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/496ccbf92e.mp4?token=ZI0jhzCxfye7AKF8zcVgoqEbfGSTNisUxQerRi1jIWC4u_IsVGQO_DAfEPSMVrMQvD-70uCExwFM7S4FQi9ax__to90pWVnPyh7M9wD-stb8032QTF1LyxWLTJJPpW9k-1goImJUILFlhfsFct0LQ-_Sl5gkcgp3b0TR2YiDVSjQO2E2Tga1V8SBo3WEB95H7yDBY3PSUa9TSZUsIZXKSLA_azZISy9FIIF59kdu6KyawEDOPF_qZm7cmHNmHvSuHsYJ6DkxKR-TQRmh_W5uVKUu9pWeSOSFc2ZEvb9dC_CkxQdi-aaogeoNeLqrX-FyDK_QK_Q_jucthF_R4-JGmLeQh6J9Q6mzQNptqYL7tskSdlwNNokx5KEzo-V3kRTnIITXoFBEkHpPK1lmSUFRKxGbsgWb11JeHkuN_WObFLVfiXhnsjLKVRbGoBABDzzzOf6jmwLQlxFdEOs3QGijP5r3M26fkaEg9ivJZGxp7DFn5LqYwdRRqriV4LJUZ5C0bULwGu4XeGOtdKQuLqsbhZ_kyWrdpyuFxoaUbC3gtxQG23htifrgWRAGLk8zkzyu_PHBQOqycSxESSFpVD3l_fHRCyJ9EZgDtDtiy7GFGAb3HNts_W9UPDwleFFd4MGI2MsT4VllLWSgHWCl1JbRXjEesR_Kxiq-XNVvYD1l7qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🎙
رئیس مرکز ورزش و تربیت بدنی دانشگاه ازاد: علیرضا بیرانوند سال پیش فارغ‌التحصیل شده و الان دانشجوی دکتری نیست
+سربازی در کمین است؟
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102129" target="_blank">📅 12:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102128">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxX90uO7T6MshIvu7FOR3gU-ovvc0yVVPM32mteDbyVundhx44bvYPchc5PCZ9yEm-sjn0IVEsPVOabRfCnaqGsSNNJVNSNrUoyiijWyn_QqIYPM1V3s_HxcvivH4avCkZLcedJ8u0-RrZpVOH_XqssHBDXOrl0ZGA4XPf-lYTDqyq9VFEnBAZQL8xJDY8DZ-gWbQTm2vtx9wsphjgJaoeTib4Z891QODX3FybZ4bpTS67iWFaxOiDPHBQOug9jR0KY9eabC_0FK-EIU9BP-FlcZsGNPvASxr056xh7nfISccQz6AMuwt_ywrd3zl6KS94TTFqt0jpBXMxaotcK81A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بازی دوستانه|ترکیب تیم‌فوتبال چلسی مقابل وسترن‌سیدنی استرالیا؛ ساعت ۱۳:۱۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102128" target="_blank">📅 12:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102127">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04499b20cd.mp4?token=Th0LdFgnXKGiTfZZAd45W2uQHt49Z7J5X06GU9vaGM3mfmaPYb08NbuEpCC5fC0bQdojW-kHsqYN5ZaUrGy-w4VGmrmupfQ2TBZus-T9SQcLzkdhoMjBx_VZWSjwFV_EViDdnVcwDFInUaBkyY8-ellfoU4HSKnW1lxtIVuZ5ia-WbMuRfDs2o1iV66qklpsbwHtf4LRxiIYbEOK9gCCO__MA4BhJ5hmyIKZu5aIqS9VRPUXglrF7YcbkosgrJEt5KhnDvPNg5Xc_Mb7j5B1hfMOAlWC-03mxz3i2_ZyiOfRgulJaTM2IbuSBI4xQm2oye4XjF_2gA2Nyjw2FcYxPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04499b20cd.mp4?token=Th0LdFgnXKGiTfZZAd45W2uQHt49Z7J5X06GU9vaGM3mfmaPYb08NbuEpCC5fC0bQdojW-kHsqYN5ZaUrGy-w4VGmrmupfQ2TBZus-T9SQcLzkdhoMjBx_VZWSjwFV_EViDdnVcwDFInUaBkyY8-ellfoU4HSKnW1lxtIVuZ5ia-WbMuRfDs2o1iV66qklpsbwHtf4LRxiIYbEOK9gCCO__MA4BhJ5hmyIKZu5aIqS9VRPUXglrF7YcbkosgrJEt5KhnDvPNg5Xc_Mb7j5B1hfMOAlWC-03mxz3i2_ZyiOfRgulJaTM2IbuSBI4xQm2oye4XjF_2gA2Nyjw2FcYxPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
خلاصه که نگاه کردن زیاد آخر و عاقبت نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102127" target="_blank">📅 12:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102126">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-X8xnqfWVgskM_qz3Y2Aa8OBr8WvYO08UIh3iSXXufuZUOui9wB0Ug2bkiehnMcorCEaP8oAzolDJ0pF9iS_m2-HJaT3sSmeefKtsfIpqg77dXFkw60aajQLxV7lS3NXQkPJTPuiLACzW7cHMcxzdBXEuKzY1BUWB0vZm1JBtXNHjMNc2ugXEWCQZPxQVv4OltlGGscGNKpc29VuzntQ6AQOJuzXknxq9gZ3MwOEvcdbs-fwPJeLbn30sDWwhuzYyLiaB-GPjAez9ZsWeGTmwnaddNs7czckZyakBUdhl2_JwaHIxhT34D91VW7AeZZSteS8YJKgbr6LkxKOtGbDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
‼️
آپدیت جدید و عجیب اینستاگرام که شدیدا مخصوص ایرانی‌هاست..
شما میتونین در قسمت «یادبود» اینستاگرام یک نفر رو مشخص کنین که بتونه بعد مرگتون در پیجتون فعالیت کنه، و توی بیوی پیجتون هم میزنه «صفحه یادبود»..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102126" target="_blank">📅 12:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102125">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKGmlC5OyxO4AcjgRs_1YZ376tJwB8okr8aqyE5Qa33nOGBPTt0iyl5a8UjfDCDyoS4vJdDAq0WloGKjut3NSctXAncXOfsVpaDtgEXSy8gwgKqzXChYd6r5TkrrMlUAaNOCbtPHwZj29L67ors--6ACZh60kMETMMPpRJceT6Niu_CuVFWouWrzFQGQLqr66sXTk4Vwx9yD4gIHSNGEdEp7IhI668Vp9l3nPiQB2QiQqg74avcSeGMKPL96Gcwp800fRbgJ54sWsfGw4KHzaSIgku4rHgy6XEMzK0_pKqk23JAz1n7iM1r2uyW6VQm4gPb5DHn8vITxQX8Dm2JHaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماتون بریزه که یامال تا الان که 19 سالش شده با همه اینا یه دور تو رابطه بوده
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102125" target="_blank">📅 11:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102124">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/07378b8b26.mp4?token=Gdv_on4BwfjkDyOCX6iu2J-1NbwwFOIf6SzEi4n6KotQlDG5mR4ZWxWjCkEkzx-F45Zac2hrbHJ3-3JgtG3dTxXv4DsoFv3gFoUMiorpjWV-rRj9qQ1ZpCfM2BNyW46ui1deOvTXKJipJmxBrzdCISN28oxoRuscLAh2_5B74qv9DbiYGlicztYKsCHmmRzqWkYPCtoXd1VECMFCuRmC5KU0UIaTK5l6lNr8kMDF0AwKvQyTHeZsF-6RozKuCFy5fD07-_q3j5WwXaebyfreHzlKZZQs-j2gRF6NAwVN34TJx548K0gVEwyD-15674MDoQXY--zFYpUY71hrOIoUqA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/07378b8b26.mp4?token=Gdv_on4BwfjkDyOCX6iu2J-1NbwwFOIf6SzEi4n6KotQlDG5mR4ZWxWjCkEkzx-F45Zac2hrbHJ3-3JgtG3dTxXv4DsoFv3gFoUMiorpjWV-rRj9qQ1ZpCfM2BNyW46ui1deOvTXKJipJmxBrzdCISN28oxoRuscLAh2_5B74qv9DbiYGlicztYKsCHmmRzqWkYPCtoXd1VECMFCuRmC5KU0UIaTK5l6lNr8kMDF0AwKvQyTHeZsF-6RozKuCFy5fD07-_q3j5WwXaebyfreHzlKZZQs-j2gRF6NAwVN34TJx548K0gVEwyD-15674MDoQXY--zFYpUY71hrOIoUqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو با کیلومتر ها اختلاف آندرریتد ترین ویدیو سم تاریخ فوتبال ایرانه
دعوای علیرضا منصوریان و فیروز کریمی در یک قاب ، منصوریان میگه فیروز کریمی داره بهم فحش میده یهو فیروز کریمی از اون طرف داد میزنه :«گه میخوره»
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102124" target="_blank">📅 11:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102123">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeee92fd86.mp4?token=sbDg3g9iSp3ThAc0L1TwODRbrG7ptTKARmA20_Fq7UW1oyVF540kf-p_mF4V0YUHghtEp_J6dAZBczN53XLoRXkiUpqPIOJRwQQCE-7nIWWq3VLuk43oIngkrvxVLB9AN8fAism-pHX_IdiwAUBcU_va0NRUmDFVNaFvjO0yFWLsy8RsBJx3Rv_qDacG3gcBludyaKqXyTu062BBrGdvKsvRvc0oSR09YSxs0bDiCoztUG4NsAqoNTrE4hPOc3QkTjPGfreLR442ZOiybg_n55EO9-9tIe9T6u6LKwPMP49xFsvPp55vm8y8jhmDqf64zjnk5Xckm77zoZgTqBjfZg2RYaIBsZU5tBJ7vKF76rG9f1ftMZwjcrQX84SRES2bXHnoNPoDICRwRkft74DBln39W-pRBXNOdUF-jjhdqS4VgNnfJbdB9FkEDow7CF_DyXTmxTgGy7n0W1Nun1Xr9xYQoopqZUAD6KGz5zW-NQUozipu7gPDNguCP7IJWUQhNmei4cPSdcOI17zggGqhMcnmnaTjjZQxeAUe6-PqDfo4WyeRGFLLG_wVU_rzbJi6gBH976SgAFML05SxlCNPDoosod1kB7FCq2SLaTCUHphSroZZe-Iho8D4PUMsMTbZ6aGCKU5zEKVIiwHH0DBm5Cgmi25L4VQeIykmggjW3GM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeee92fd86.mp4?token=sbDg3g9iSp3ThAc0L1TwODRbrG7ptTKARmA20_Fq7UW1oyVF540kf-p_mF4V0YUHghtEp_J6dAZBczN53XLoRXkiUpqPIOJRwQQCE-7nIWWq3VLuk43oIngkrvxVLB9AN8fAism-pHX_IdiwAUBcU_va0NRUmDFVNaFvjO0yFWLsy8RsBJx3Rv_qDacG3gcBludyaKqXyTu062BBrGdvKsvRvc0oSR09YSxs0bDiCoztUG4NsAqoNTrE4hPOc3QkTjPGfreLR442ZOiybg_n55EO9-9tIe9T6u6LKwPMP49xFsvPp55vm8y8jhmDqf64zjnk5Xckm77zoZgTqBjfZg2RYaIBsZU5tBJ7vKF76rG9f1ftMZwjcrQX84SRES2bXHnoNPoDICRwRkft74DBln39W-pRBXNOdUF-jjhdqS4VgNnfJbdB9FkEDow7CF_DyXTmxTgGy7n0W1Nun1Xr9xYQoopqZUAD6KGz5zW-NQUozipu7gPDNguCP7IJWUQhNmei4cPSdcOI17zggGqhMcnmnaTjjZQxeAUe6-PqDfo4WyeRGFLLG_wVU_rzbJi6gBH976SgAFML05SxlCNPDoosod1kB7FCq2SLaTCUHphSroZZe-Iho8D4PUMsMTbZ6aGCKU5zEKVIiwHH0DBm5Cgmi25L4VQeIykmggjW3GM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
نوستالژی خاطره‌انگیز از دربی دلامادونینا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102123" target="_blank">📅 11:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102122">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aafdb5637.mp4?token=HJ_46zTqfvEkIfUqZN3v0NZM0CTJQIVeyg3EZqbsXVvTW7t9NpXKEeBGAsVtF61Urmly9Z1dlyk4YKTKXHPXvXv9cHMdkrT1c1_WaJFEYnq6kosgajtjFBwsWHwnclqnl0iNTM8jnm5jTrRgHi7x6qjE5Pf1E2TW-VLTew9CG623v3nJ24M0kRi5rGbnZ7UNcOoXRRRoIn1efFAJEt8UFE_3-IWX4VhVGda-19Lg0wdoATzOJGqq0bV4-QUqwgHrvVIe6fgWdMvu04RDh2XP1dE2SOuf4qmbzMJ6evBVxPNKwH8yUOrC-pWBQ6JasoXCFKBsB0ceVEIzGJU9X6wpczzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aafdb5637.mp4?token=HJ_46zTqfvEkIfUqZN3v0NZM0CTJQIVeyg3EZqbsXVvTW7t9NpXKEeBGAsVtF61Urmly9Z1dlyk4YKTKXHPXvXv9cHMdkrT1c1_WaJFEYnq6kosgajtjFBwsWHwnclqnl0iNTM8jnm5jTrRgHi7x6qjE5Pf1E2TW-VLTew9CG623v3nJ24M0kRi5rGbnZ7UNcOoXRRRoIn1efFAJEt8UFE_3-IWX4VhVGda-19Lg0wdoATzOJGqq0bV4-QUqwgHrvVIe6fgWdMvu04RDh2XP1dE2SOuf4qmbzMJ6evBVxPNKwH8yUOrC-pWBQ6JasoXCFKBsB0ceVEIzGJU9X6wpczzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
۱۰ گل خوشکل زده شده از مدافعین فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102122" target="_blank">📅 11:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102121">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd7bc32139.mp4?token=GcOciqUO_yowhHhLrDTEltvDga4ee-1S2Hc-pv6tuo5zvxoPAiFGn-B7BwZNx0HGeZA3pd3hFtrZGJKv7q8jhpoNXtFVmROtY5vS86q6im3WkYsQyrGQ5b2JqejiKiDYBJtqSWvKHTxeLpFi4Q7BrypiRnfgRj-ppCXfsa-3bQmfp6dUnjExyvChmtT_HjTUUpzY6Ca8jh1-LBqeHbNCgENzSG89ktc8lqdG09QgMgceI3OmtNvYfaPBSvnlErt938cY1prlBdraZhiYzy_503Tmxdr02AHzXzA_lYx0vVytpd2Mi9gUaBXmGJKfUxOJ6eROabP0fBbBZwLNqMmuZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd7bc32139.mp4?token=GcOciqUO_yowhHhLrDTEltvDga4ee-1S2Hc-pv6tuo5zvxoPAiFGn-B7BwZNx0HGeZA3pd3hFtrZGJKv7q8jhpoNXtFVmROtY5vS86q6im3WkYsQyrGQ5b2JqejiKiDYBJtqSWvKHTxeLpFi4Q7BrypiRnfgRj-ppCXfsa-3bQmfp6dUnjExyvChmtT_HjTUUpzY6Ca8jh1-LBqeHbNCgENzSG89ktc8lqdG09QgMgceI3OmtNvYfaPBSvnlErt938cY1prlBdraZhiYzy_503Tmxdr02AHzXzA_lYx0vVytpd2Mi9gUaBXmGJKfUxOJ6eROabP0fBbBZwLNqMmuZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
خوشحالی‌گل‌های عجیب در لیگ‌های‌فوتبال ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102121" target="_blank">📅 10:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102120">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">▶️
رضا نوروزی؛ یک فصل طوفانی، یک عمر سکوت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102120" target="_blank">📅 10:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102119">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_Gzzdeiz9DEMoIE-3gYqt-kJXm0yJHv8_PNIuuyZUD2TO8h_ItQm5OIu1dMBEqgsVP0piNR-IRI7Nwc4c8mi-o56OkBI0kWJxYUF0tbo8SINkMNTGUhlXdSFyoU5jEB-MynZKmWe5hp46rl-nyWizVYceWtRetzAcBEYjrdJ2SsjRNsC9vDQ9wofADE5qqgtHBWj4OhQmFAHTwjS_8YRWv0VbRlXkVEx-Iinf6A7nP2a9oiAbTO2HleNm4h9Q7ZGQvoddmHwk3IigJU5EnG8_6txcrKVE4r5X1B22J5noI2o72fOD39q-5sg5pxsPabwghrNKEpuuVbFobzvjzbOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
😟
اینتر میلان به توافقی با تاتنهام برای جذب کریستین رومرو به مبلغ تقریبی 40 میلیون یورو رسیده است.
✅
⭕️
🇪🇸
اما این بازیکن منتظر بارسلونا است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102119" target="_blank">📅 10:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102118">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad2348e726.mp4?token=NvhC6PwTv5rR6CP1tXZyDSMkSJKvBYxG39zLxJ3TBVpQA2FOZ5xNyXw3xJk2ZhKwTkRcNJc2H_J9iMCv5xZmEu8PjTk9IX5QwNJbZNu7TcHXGeTPNrjEMnbuDMkK5H7KbLhUHUYHYxr9fGxTnDtYLxTayIBZEzgoDDQMTsN42qbdMXNWHhRjSN7gLiGvmRcn4qQ4CicPhXfEe1tROI2Po1E4rLDJakIKyEwN-vUEUnQjy_Gsxlv3WPPauxl5UGiBMQUAQNQp4U2hQE2oQYPlh05ITs-Ed4kwBXrqc6VVPSfhkQXGuDATHFnjRlQ-1PnY701_ahW-U3OWJhW4J6ay-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad2348e726.mp4?token=NvhC6PwTv5rR6CP1tXZyDSMkSJKvBYxG39zLxJ3TBVpQA2FOZ5xNyXw3xJk2ZhKwTkRcNJc2H_J9iMCv5xZmEu8PjTk9IX5QwNJbZNu7TcHXGeTPNrjEMnbuDMkK5H7KbLhUHUYHYxr9fGxTnDtYLxTayIBZEzgoDDQMTsN42qbdMXNWHhRjSN7gLiGvmRcn4qQ4CicPhXfEe1tROI2Po1E4rLDJakIKyEwN-vUEUnQjy_Gsxlv3WPPauxl5UGiBMQUAQNQp4U2hQE2oQYPlh05ITs-Ed4kwBXrqc6VVPSfhkQXGuDATHFnjRlQ-1PnY701_ahW-U3OWJhW4J6ay-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یادی‌کنیم از تقابل نوستالژی نیمار و ریورپلاته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102118" target="_blank">📅 10:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102117">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3115e0e757.mp4?token=VBxjel_UU0Lc8pELGlBSIX4vgDVhBKCVPma93eJEhxZjgIyP6wVe1hQI1XpbZ3ghtOR9i92eziJPrQxH0pXSDZ5tl4-74fv5nvbfrRqb4sfMpPREZv0cEr3eLBI8oDIYmFgUa-SISG_kRGaLs-2O8xXTNesSD367mS_tCm5bzhBS7dx9Ta9Nt2RESCQdWXeShupkEM0dBAqbz_lYf9Abi8bnaRy7o2mepFbnaqkroLd2NCefp-3zG9mTF4BkZtFWHxwtBHerNtr-24Y7xY3KGR_HKodHhOES-cqBEuNm5h0Lxkp74EKZxL5ETQLJeooQkBRflzBgI6Jqm_u1zLgWQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3115e0e757.mp4?token=VBxjel_UU0Lc8pELGlBSIX4vgDVhBKCVPma93eJEhxZjgIyP6wVe1hQI1XpbZ3ghtOR9i92eziJPrQxH0pXSDZ5tl4-74fv5nvbfrRqb4sfMpPREZv0cEr3eLBI8oDIYmFgUa-SISG_kRGaLs-2O8xXTNesSD367mS_tCm5bzhBS7dx9Ta9Nt2RESCQdWXeShupkEM0dBAqbz_lYf9Abi8bnaRy7o2mepFbnaqkroLd2NCefp-3zG9mTF4BkZtFWHxwtBHerNtr-24Y7xY3KGR_HKodHhOES-cqBEuNm5h0Lxkp74EKZxL5ETQLJeooQkBRflzBgI6Jqm_u1zLgWQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
▶️
این فیلم مربوط به سال ۱۸۹۴ هست و رنگی و اصلاح شده. حتما ببینید واقعا جالبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102117" target="_blank">📅 09:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102116">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52dd0bc973.mp4?token=fcODPA1aLTpet0GoWcqPsol0LbkZsU0Tnj2e9b4aHbR6d6Qbc3EWnU79u45Axt8ofWnCuHyBrU56Oeqy7JTs3qs1xDq-9yfPF7ybG7gu53mvgpYOsefORNwZKLwzqrSoBeuP6Lvd1_VzBvNSeNpxG9NMxW4yQ3v3Vs6A7NlV66bLo2LDWjULNqo_a1TedIM8W1H0Qn7oput2L6CpQmOvl_K2pOMcLXVXn-_vJP95mWkUDOrUkWgpyulOfSgK_oVZi0Gze8hBpcdt0dAh74AGbjqLFA9mIreHNWU41tfu1OTRvzFTSUDQ7S2qFmNypipRQulsX6710CD07Dqr0YQmwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52dd0bc973.mp4?token=fcODPA1aLTpet0GoWcqPsol0LbkZsU0Tnj2e9b4aHbR6d6Qbc3EWnU79u45Axt8ofWnCuHyBrU56Oeqy7JTs3qs1xDq-9yfPF7ybG7gu53mvgpYOsefORNwZKLwzqrSoBeuP6Lvd1_VzBvNSeNpxG9NMxW4yQ3v3Vs6A7NlV66bLo2LDWjULNqo_a1TedIM8W1H0Qn7oput2L6CpQmOvl_K2pOMcLXVXn-_vJP95mWkUDOrUkWgpyulOfSgK_oVZi0Gze8hBpcdt0dAh74AGbjqLFA9mIreHNWU41tfu1OTRvzFTSUDQ7S2qFmNypipRQulsX6710CD07Dqr0YQmwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ذهنیت برنده بودنه که آدم رو به همه چی میرسونه
🔥
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102116" target="_blank">📅 09:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102115">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffacd8024c.mp4?token=VADo2pxfC3lz3WyAOZTokqKVMsAPDoDz1YUbMMY14RpbYBhuoMsx5gq1eFyaSdmJxTVrz4XvXaLOfpFPduFXHHTDwL7AtwgOFFLkU04aliB2QyFAPJp_68ZIQl-MCLFGJcN_GQ7MuRpc03AXUOQXJ4id8RiZmLYiPlN0pfUvxj7TMegm-xyZxTSPq_3L9vzdra9HyHY4cHVvBP2ofqatOVYhWJrst_EN7waumuxT5pBoaVSNjlPF1q1vfg9z6dsWKdBpDW5DfVz1hG0Sx5xaAIgAc-mGt3fRJmncoaWa-lcL1q8W0dVODdEyJ8mfH65oKLw1-GSuz09n1wlWOvjY9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffacd8024c.mp4?token=VADo2pxfC3lz3WyAOZTokqKVMsAPDoDz1YUbMMY14RpbYBhuoMsx5gq1eFyaSdmJxTVrz4XvXaLOfpFPduFXHHTDwL7AtwgOFFLkU04aliB2QyFAPJp_68ZIQl-MCLFGJcN_GQ7MuRpc03AXUOQXJ4id8RiZmLYiPlN0pfUvxj7TMegm-xyZxTSPq_3L9vzdra9HyHY4cHVvBP2ofqatOVYhWJrst_EN7waumuxT5pBoaVSNjlPF1q1vfg9z6dsWKdBpDW5DfVz1hG0Sx5xaAIgAc-mGt3fRJmncoaWa-lcL1q8W0dVODdEyJ8mfH65oKLw1-GSuz09n1wlWOvjY9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مایلی کهن و پروین و کفاشیان در خنده‌بازار
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102115" target="_blank">📅 09:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102114">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7e0420a2b.mp4?token=QnnttOXlDqDdxt1SHa47gUAd99h8oJPyHsYeOBn85udmiLJc_z8zme2rv7_Tfg_dCd0FN8ORthf_u4XlkIeQVuihYKiWIRZpda0rJerajZU12WwS5_Bv_7KRKP5Vm3FelyIeiEqI-CvVnyXFKP-e7ftqMc0oPUp86GunSs9tZGXfI_mDVsbp4S7ai5NzN2t5wBm6DTneTc64_uFQhR_V9xjI4DqRFCySBhrzj1iI_n-EFSd68aRI_OLf4lCLh4EkdONoi2_18Jfp1Js7voOyBQTymmoX2WnMfXeYPNXmBkn8DkV198eJRYU_mLW_EjLJiUVUjociwFMOwctRqcokBXuzpyhGANizCjYU4CNb4pMbBk15mHykjavO2QTH-pB13DwDZhKNC-ZjeNcf42Pdau2HON_7HRmYDPoirY9HLR37RVsI4lrezQBLD0uEnlZPl-MZ-rsqc83WJcARHXgQsgI86wralyGA9C5MiDkv8fPy27O_ISzlmz91AmmD1XtJS-_7hstpF5oFpz9WkJrJ1GeWrIxA8iy-PdWzBWNzKszl1F5F9UeUlS0a076Cb1kvNEGpS8J7tu2Sk1elK_yEjfgX50XHrCsJA5fc_lHGV8idVW5pjU9Iap3V6GpJ_c8bnBrfjuU_mWMpiyewOqSuJhRiYxRKrLIZaLj-8Leq6IU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7e0420a2b.mp4?token=QnnttOXlDqDdxt1SHa47gUAd99h8oJPyHsYeOBn85udmiLJc_z8zme2rv7_Tfg_dCd0FN8ORthf_u4XlkIeQVuihYKiWIRZpda0rJerajZU12WwS5_Bv_7KRKP5Vm3FelyIeiEqI-CvVnyXFKP-e7ftqMc0oPUp86GunSs9tZGXfI_mDVsbp4S7ai5NzN2t5wBm6DTneTc64_uFQhR_V9xjI4DqRFCySBhrzj1iI_n-EFSd68aRI_OLf4lCLh4EkdONoi2_18Jfp1Js7voOyBQTymmoX2WnMfXeYPNXmBkn8DkV198eJRYU_mLW_EjLJiUVUjociwFMOwctRqcokBXuzpyhGANizCjYU4CNb4pMbBk15mHykjavO2QTH-pB13DwDZhKNC-ZjeNcf42Pdau2HON_7HRmYDPoirY9HLR37RVsI4lrezQBLD0uEnlZPl-MZ-rsqc83WJcARHXgQsgI86wralyGA9C5MiDkv8fPy27O_ISzlmz91AmmD1XtJS-_7hstpF5oFpz9WkJrJ1GeWrIxA8iy-PdWzBWNzKszl1F5F9UeUlS0a076Cb1kvNEGpS8J7tu2Sk1elK_yEjfgX50XHrCsJA5fc_lHGV8idVW5pjU9Iap3V6GpJ_c8bnBrfjuU_mWMpiyewOqSuJhRiYxRKrLIZaLj-8Leq6IU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
ویدئویی که صداوسیما جمهوری اسلامی تحت عنوان مستند شوک از پرونده خیابون علیخانی منتشر کرده که ساعاتی‌پیش به سبب اون سه جوون مملکت اعدام شدن!!
+ اتهام‌هایی که به این جوون‌ها زده شده:
- بستن مامورها با طناب به تابلو
- سنگ زدن به مامورها
- آتیش زدن مامورها با بنزین
- روی زمین کشیدن مامورها
-  تیکه تیکه کردن مامورها با چاقو
- فرستادن فیلم از اون لحظه به رسانه‌های معاند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102114" target="_blank">📅 08:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102113">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/508992e992.mp4?token=eX1zVJn-z5CvsdmemePey2_kt9HZpudi615t40OmF2nqF54HHbTbs6H30zQdjKx-OyajaIE1Cxm6VYjaf_VLNxc4Pub6-PON2dI3sdoHDjI5IFMAon3cwOJ1ENbIHYPsVZ_d6Ly3qXEYMdZDSxBS0KODgbkYNc5rZLyHPXeO6_h-BLAxC0KUgVd3KnzmSGP6KBeNxhRzQN7c8cDaPl-VNwHoxhe-PjJt3HhScO2EJlKWITtuPb3L6GuShIVZmeP6BNERoVN6NjZLLQ3AoXQdVSia62cy4vP9XVivW_oGyDDtgHV6UVG31vtH8lMCSJTQRRJuWNRH3KU8oq6oOhB67w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/508992e992.mp4?token=eX1zVJn-z5CvsdmemePey2_kt9HZpudi615t40OmF2nqF54HHbTbs6H30zQdjKx-OyajaIE1Cxm6VYjaf_VLNxc4Pub6-PON2dI3sdoHDjI5IFMAon3cwOJ1ENbIHYPsVZ_d6Ly3qXEYMdZDSxBS0KODgbkYNc5rZLyHPXeO6_h-BLAxC0KUgVd3KnzmSGP6KBeNxhRzQN7c8cDaPl-VNwHoxhe-PjJt3HhScO2EJlKWITtuPb3L6GuShIVZmeP6BNERoVN6NjZLLQ3AoXQdVSia62cy4vP9XVivW_oGyDDtgHV6UVG31vtH8lMCSJTQRRJuWNRH3KU8oq6oOhB67w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپیده دمید، اما روشنی نیاورد؛ گویی خودِ آسمان هم داغدار بود.. صبح آمد، اما هیچ‌کس از آمدنش شاد نشد؛ انگار خودِ سحر هم به سوگ نشسته بود.. ای صبحِ غم، مخند که امشب هزار شمع، در ماتمِ عزیزانِ خود اشکبار شدند...
⚽️
@Futball180TV
| Quf</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102113" target="_blank">📅 06:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102112">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAu8CJCBMFz4FxTZuKEsTwytamChZeZW4871eW-X_pLeQRviS-QQtIYos0P-1P5a0UQDk348UGiB779xf83_700bkq8SV2fLEbN81eUCWWPZlD0vNmcnEI8D6g3sGINp-_Cwb5KJ9GzDlKE1S3JIHDbjGvLMFWxzA24uTUhrkgBA5DSGbJRWbTHVB4SWU4N--ULD-m7MGLSz5n30EWBwebJYmkKfD92JsH6SesJe90atuSnwXY_i1lOmg9nzcklsg3Y4K_Bcm5FvaMxvu0IOygSiYjqbJfhRno9rR73pBqHFtXQo_fBi6ASRaaBmR3B57mLz7cPLIBtNZ4zsEsG1Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوووووری
از رومانو: پرز مجوز مذاکره و عقد قرارداد با رودری رو تا امروز صادر نکرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/102112" target="_blank">📅 02:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102111">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkN10hv8tVVVkeMt99QE37VxGDxzL0wXuN9o_-Je8l6wXp4pBcV-Oo_Lv2srfogyFy4U4uXiIkcsKZpIdlZfyZ3Hdnowdf9-u1PR9sHHlsotFSLhYCHcKpNjAr3gcdJs5s_6-rNvaVwmDnzm99rS3LQ_-PC12KjwzGmjZV4PejWz08CMbactyecaUAnae8WL14yYA_ghOUQ9QGs_gBA0GlTNwHnrfyq1e60A6O57tjYAbV5ePI-JofTK74S7646n8Wp_IdLJC36hxfIGLsb8a3lwrZ_VNfKQ_bV71og6cYvZp_LOCm7YdOMNV9Xe7pE61Pm37MN-gffht44UKm1aFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇹
افشاگری پائولو مالدینی از وضعیت وخیم فوتبال ایتالیا و دلایل استعفایش:
یکی از بزرگترین اشتباهاتم این بود که اصلاً این سمت را قبول کردم. سطح فوتبال ایتالیا به این حد سقوط کرده است، و دلیل آن فدراسیون است!
وقتی منصوب شدیم، فهرستی از سه نامزد برای تصدی سمت سرمربی تیم‌ملی تهیه کردیم. پپ گواردیولا بدون شک گزینه اول ما بود، در حالی که آندره‌آ پی‌رلو گزینه سوم ما بود.
ما مذاکرات خوبی با پپ داشتیم و به توافقی با او رسیدیم. با این حال، وقتی به فدراسیون اطلاع دادیم که به توافق رسیده‌ایم، به ما گفتند که نمی‌توانند هزینه دستمزد او را بپردازند و گفتند که باید گزینه‌ای ارزان‌تر پیدا کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/102111" target="_blank">📅 01:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102110">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c83412a5e5.mp4?token=H_wOmFj--zCLztf2-hxdoom36d3MOrhFE-sHlo-MMP5sJqAFi_ZFw-68G4XXzyqqxi70Mj6q3tWCz_f74jbz8eQmqmsOO-cCTXlDt7pCmJlIjJIufdUDjv9MtRhcCCtzE9IpZBrh1fzKoFYb26LYVGTBBuFuKooWind72ZCXayIi8HiKUrem1xmEHsKa9LrLGchliv8hFmd46wi0OzZ5l5AeT1kL2QM2io1dfItJcoGGH44ND5hgARdOy9M9jD8OrJ64RALop-B1oyyLYT6nfpuNl5TFhPBAEV4ZVZCIZJhbc2WxOWLki3_yKA_QY5iNUzls694QeIXmkYz3VscQ5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c83412a5e5.mp4?token=H_wOmFj--zCLztf2-hxdoom36d3MOrhFE-sHlo-MMP5sJqAFi_ZFw-68G4XXzyqqxi70Mj6q3tWCz_f74jbz8eQmqmsOO-cCTXlDt7pCmJlIjJIufdUDjv9MtRhcCCtzE9IpZBrh1fzKoFYb26LYVGTBBuFuKooWind72ZCXayIi8HiKUrem1xmEHsKa9LrLGchliv8hFmd46wi0OzZ5l5AeT1kL2QM2io1dfItJcoGGH44ND5hgARdOy9M9jD8OrJ64RALop-B1oyyLYT6nfpuNl5TFhPBAEV4ZVZCIZJhbc2WxOWLki3_yKA_QY5iNUzls694QeIXmkYz3VscQ5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✨
روزی روزگاری ایوان زایتسف بزرگ و افسانه ای در خط سرویس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/102110" target="_blank">📅 01:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102109">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cF0iURgXajXM_73XFTGKnqqXdcbZBIwxbV6o8FFISNhalwX-e1I2MUeMEZaO_nAi6RvrtlIZzs9wips4UszzndJe8EVGP-7st0TX8ipLfr65SyfGl_tZOMLd0xNb7yEEyIgu8H5A7kDHALENa_FcUwdcOe2N6k0WY_deqvxSpS395Kbyhzvc1QRctx4PKr0x95-TITuT6pm-7TD5et6k4vPEwbTuSa3V94Rs3TmMEMVoV1YBUQ8ZlGKaIAKiFkGGB4Y7lttKaMeNpJ4PiO4xt8wPUfvOSK1pmo00Vy9vZvXWm84rYT0d-UvwZUliRtjlxjfENKaqaoPVxQVdNLxPJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
‼️
لیست گران‌قیمت‌ترین نقل‌وانتقالات تاریخ که ۵ موردش مربوط به امسال هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/102109" target="_blank">📅 01:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102108">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6Pf7RqTDgBou2TG2bE0ZNGuWuMABZrBHyELw2RVTeo5e2sDdZTMMx4OYggTHMGzgA3dK4f9UzuGNN3FmQsy_vcvqOYrWFz5iUjr2R0rQwnFwbZ4gkyD_1wpo3XQPenO1fTs1bvAdeC0J9ildW1W6Cd7nIwjdrdPTDBHoBpp8q8OSze9zfuUUtfkn5Y4EIpdwN6CZX4aMqfHScLnVcwxiK1iREoGKAJJiSmE4zumEzUv4a4nw359YzO4KByGAy33cfw2PAP9spZijrlW3Mv6P-NGsMXmxuvYg7h5-GGhWyLWUL5m2ej0GobiiQIfeif0u4PmO-H3R9Er7y6VQwOCKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پینی زهاوی ایجنت لواندوفسکی:
لوا برای اینکه بتونه برای بارسا بازی کنه قید 200 میلیون یورو رو زد، اون پیشنهاد سالانه 100 میلیون یورویی از عربستان داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102108" target="_blank">📅 01:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102107">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=JmQVm31Mn6nNGGASoVcxjRhtLdy6w8G2zd0zQVJPxvMYy9EMKPybxQd8FFDcxd0406tkCp_qya0yKLJHOCVYSXfSkxkkec92aTA-ndga5iEoITJCSL99oOeNj6trQk7Cy3RhLTWe0T4IIQiOZ7Oek5hGKfgMO7WAvHfVvSDHKstNfRguupfQWAzzJr_373ubvN-kdYBSIykTPopM53KPeONeGbe7xWvhwNSClHLkJBc-4a9TulkrL7or7LNtx-uC2wwoEBjJafMXEL3kqAOLWCL72K83TekmkOg_7l43N4AXScu_7EZPKYpqdPQ3LAVb8BNkSlhyMDhX6s5Uf8W5sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=JmQVm31Mn6nNGGASoVcxjRhtLdy6w8G2zd0zQVJPxvMYy9EMKPybxQd8FFDcxd0406tkCp_qya0yKLJHOCVYSXfSkxkkec92aTA-ndga5iEoITJCSL99oOeNj6trQk7Cy3RhLTWe0T4IIQiOZ7Oek5hGKfgMO7WAvHfVvSDHKstNfRguupfQWAzzJr_373ubvN-kdYBSIykTPopM53KPeONeGbe7xWvhwNSClHLkJBc-4a9TulkrL7or7LNtx-uC2wwoEBjJafMXEL3kqAOLWCL72K83TekmkOg_7l43N4AXScu_7EZPKYpqdPQ3LAVb8BNkSlhyMDhX6s5Uf8W5sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از آمار تا پیش‌بینی
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102107" target="_blank">📅 01:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102106">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b085DgYzBfKEcvbCcmV11OMja2lM3DtAnXwFEAjPpItWU-wno-taOqP8EV0zp9EYoweyLxRsZ8vYIfLpeFnxs6hjv-U7BAecRxdp_whw7rqvqm3taCh4s4N85jt7kngVtLNFCwWQ6DuBzGJk-x1lz-h4xAqhCzdKPwEhAOVyCQ_DjeMQk6CPoG2YcxKu8aoks_WeF60xJmtfz3JARaHLoan5uTrGObK1QSJkm4A85OVw1MyqywnTuSoy0QI7pEeBXnCRe0kRF-qaNLQTdjPaN9TqbvQgVVGM0Yh6XeGhQJH0m1LNRkmaHJ_2WiJvZThBQr39fyeza6ut-mRJvdVO0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🤍
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فلوریان‌پلتنبرگ: رئال‌مادرید از علاقه آرسنال به وینیسیوس مطلع شده و اولین پیشنهاد رسمی خودش برای تمدید قرارداد رو تقدیم ستاره برزیلی خودش کرده. از طرفی آرسنال هم آماده ارائه اولین پیشنهاد خودش به رئال برای جذب وینیسیوس هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102106" target="_blank">📅 00:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102105">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLamU5UwJ0B5Jx-wKTDd5sMjVNh7WfWmTTey5ZloAMyZlb6o2uQV5JKU_9yPeXNBhO4L9G8ARFxWlYzp3zjKV5qZZfrDDYBliUYyopezPWU8zgpX2aD1xSa79N0tnAbf1N9fyKppYOrbDZ8aoRlHbcVY8YtdD26b75ewC62h0jDC8minncKOrONP9PU7a_sNZYi7bHjpKpxD4U7CHrDjDWFqXCseTBN6ZN75lnD-8q8uaotXz5REV6ES0yeFbkGg8XuBpQyC3x650SU_r-Y0RUCVJbIB15DtNpR-XXWeUrFnGMVkXvd2gr-BXJ0tU4YLee8I0RFuHeD5iJvhAwazzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
رومانو: باشگاه چلسی موفق به توافق شخصی با جردن هندرسون و دنی‌ولبک شده و بزودی باید شاهد عقد قرارداد با این دو بازیکن باتجربه باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102105" target="_blank">📅 00:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102104">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CHsMGu-BDLirHCGNBhJWcPLF2TQ_QYd3JR0Kx8bRKRve_NlkWq_22wnrR-9Hd-9ek6LMgfDhUZCsFfsv9HSyIyZHbj38Jf6UdADa_dzvrgemF9GFpVPQ15vVQPzeYAsN7lksBmmRoY3e7iByk5vS9S_r9Alau4zi6OWK7XHzVtrsBKjdpiVRK7HeGnhQPoVJKZWVocgoDtRoGk0_d5BH_wt5MGPQAyxb7hdG5w7CtB54L9bbUc8ISpWH6c7ecZqDB6ep0g0JK4hp6a_LfbFGAVelluEQXMjUDIRoB9H2S9ptaogy7Cn32lYpfwFlyEnqyQ0PsBb8XHQ1GYvLT9pBuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇩🇪
فلوریان پلتنبرگ: هیچ توافقی تا این لحظه بین رئال‌مادرید و لایپزیگ درباره دیومانده صورت نگرفته اما مذاکرات به صورت فشرده از فردا ادامه پیدا میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102104" target="_blank">📅 00:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102103">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edoiSOfj65Sdi0ErBDmUIkqoDDuqncplcztz5FyE7iol-5DzNJJNo-VhYNB1CwSC2f-VpQACyXZHt9VG8oqsz0vg7QIfblny2s1jKW0BjN_PrU2J3YgcSJrW3FoMXA3RfuH4jiFiNdhhF89Td3VLl_tWpAzoZry3xiIGvEedccVQhPfBWhHnPUZ7SjMxoJZ60uYcvV5ONkVgbCTPOo-3jovZ07IBqGwmdzq79XLj2NOyJyYBmcXTQzLdNIG7KA3B-20-KLYwiShWGZWarrrqCqrwALfaWTNnR4wMDpYmTXskiiNQSIjswMoZMdLwprAyoCmc7z_pQ6RAzotG7hsbKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
مارکا: مورینیو درحال تلاش برای قانع کردن گونزالو گارسیا برای موندن در رئاله. مورینیو به این بازیکن قول داده که با وجود امباپه،‌ دقایق بازی مناسبی بهش میرسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102103" target="_blank">📅 00:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102102">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1pBgSJc-uJ-Gd65vg0tlWcvXcHeLlaA2WItRT6_5ASqnmpNjPs68k2z60zuJ9v-CQdpWhH60SoOf0awZMDQyhk7v0j1t8y6AO3HaZpn6Fd_4vBH7kTfhNbHUe33CvsxBroCKNlsBh9r7vZjmU9j8I6qb623djEvxajbC_hxhBv1HrwT7YVuzrwaPn5rXGKVbOl3N4nU7yPumY1Y-MK_qOGuiPVRICyzEAtEpQB16FUr2OoX3pNvoLwOMRdPVo9Esp9bqxF1QfmqHp4xBqkoZCeVdvINKm2fwcE47QinbVAw8dWIw_50WCIy2VDmJKG27dmm_8f7xChyruiouJ0cKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
✅
لباس سوم فصل‌آینده رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102102" target="_blank">📅 00:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102101">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52dfeed19b.mp4?token=L6Z9kkZj5twk30Mbh3tNGXI7lRRfbnjh-E44hfj8VK8oTrU2N674TmCiEjVQT9c0Yn6dvMVTrDit_0nm_txV5vrupCxAeQOQFiMCl9i_ue0ki0bQX3mZZjYzl1Ee_paRxFpFQFdPoSqxoNZDiBUEotZhNVJYnv_gsL-iOiSq0IS409dUC74GkY2zOCtpmQOKASY8_C6oJTnLf2n75ELdbgY-OMqzu5cBK734cDKDNWkfwhAFxQ4tXMQhVEwjxLTfNRTFbza04Ga13T4zywR2OMVrZhQHogkvp2CORxZBj3vq44RvcdRkFqdXdeioHO4Qno_X_Uo5JdrLLSypDfMZaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52dfeed19b.mp4?token=L6Z9kkZj5twk30Mbh3tNGXI7lRRfbnjh-E44hfj8VK8oTrU2N674TmCiEjVQT9c0Yn6dvMVTrDit_0nm_txV5vrupCxAeQOQFiMCl9i_ue0ki0bQX3mZZjYzl1Ee_paRxFpFQFdPoSqxoNZDiBUEotZhNVJYnv_gsL-iOiSq0IS409dUC74GkY2zOCtpmQOKASY8_C6oJTnLf2n75ELdbgY-OMqzu5cBK734cDKDNWkfwhAFxQ4tXMQhVEwjxLTfNRTFbza04Ga13T4zywR2OMVrZhQHogkvp2CORxZBj3vq44RvcdRkFqdXdeioHO4Qno_X_Uo5JdrLLSypDfMZaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تموم فینال هایی که بود
میرفت تو نسخه (پرایم) خودش
و تو اون نسخه دو تا وینسیوس و یامال رو میخورد.
شاید یکی از دلایل نتیجه نگرفتن آرژانتین مقابل اسپانیا هم نبود آنخل دیماریا بود..
🥃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102101" target="_blank">📅 00:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102100">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f39b79d0a.mp4?token=J7qlKtS6GAwiirgo-nMbE8PIO2VszLFWNyIHRc1kML4-X3qCEd2zMD_c6YLnqz0oWZVSq3ugEGQFD4p-8dzjOGFLYX9by8s6bbrU4FTQrK0TlIuAyS8aiEgcpjrOXoaFVCkgdCu62dbTwedZ32Pwk_3sB25YddAJZu-JRucrIImzvs_nWJTRYDSnPv9OY6Use6Mvu9wkZtQKgB8G2sEDIJXzLPTJT4rm-o3DiqC5GcUGVJ_dJz79AREa3FEgTmpozUYMyNutKfH5I9ppWB8JOVSo6T49ZIZEIhISpgU3RVYqPIQ2D3kkAVK5xZsLMLh17NIiMYA9lC27z0fZNEE_rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f39b79d0a.mp4?token=J7qlKtS6GAwiirgo-nMbE8PIO2VszLFWNyIHRc1kML4-X3qCEd2zMD_c6YLnqz0oWZVSq3ugEGQFD4p-8dzjOGFLYX9by8s6bbrU4FTQrK0TlIuAyS8aiEgcpjrOXoaFVCkgdCu62dbTwedZ32Pwk_3sB25YddAJZu-JRucrIImzvs_nWJTRYDSnPv9OY6Use6Mvu9wkZtQKgB8G2sEDIJXzLPTJT4rm-o3DiqC5GcUGVJ_dJz79AREa3FEgTmpozUYMyNutKfH5I9ppWB8JOVSo6T49ZIZEIhISpgU3RVYqPIQ2D3kkAVK5xZsLMLh17NIiMYA9lC27z0fZNEE_rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل سیدنی لوپز به آرژانتین به عنوان بهترین گل جام جهانی انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102100" target="_blank">📅 23:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102099">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTI7n7QVTuliZsxNDdA0i6U7eOQ2TrgV24YMidU02r1JAFVrToXyV739tmkBjiOPJAzAjaenh18wcH6xeDs3m58tBRCFQXe83Zl6rxPrMi5CKtmJ0Q8CebDsdr_Es4u9rdkG1qpSH_ywmkM_KCYN10RCnd1VYhYVb5UrO6d8vygxOEOg6NElrLPxGx5ocJhDgjr9C30hJGX2QOGDn33x3MLlIIDgvukcIsbkckVZTuUTHreFF4i_qNHjvS-5gRSoQByO_ZlxscFf_iRAyWqq3O1fclYSZPQq0Gn595rjYwvy5a7RAldQqYXppWlYeSzWJo5YJg3CF6jsoZakglS_aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رومانو:
جان استونز به اینترمیلان
HERE WE Go
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102099" target="_blank">📅 23:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102098">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBA-659-5cFvznRpfHfxAEmHOgf3S_Eta9cdIXDEB6iztkdN56gjYUpnSD1f5vIP5vehWkZ-EyNgx584ZaqYUA-uLssacR37g2RLbCHMBsdC7eWovocCEO1gvs3Wr9Zz9LrA9HParneawgfOUkdii2vkT1voUVfwF9NE8pk13Osgv0ExIQ8sQ5BaJTWTvx1rywxhQYzsPYeqHElVN3Iy2W8G4I6WuqIB-HC7f8NPT7PW629BzYVnkoF5fqq95nM-va8AYgsylFWlF7PUjaxGJ5YCJ7uCYzE-BJ7Ez5JDLuoObDmhGCM3Vhl4q09JO4OykV0NMiY0R-IXVC2hzrVRPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندریک و خانومی و بچه‌شون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102098" target="_blank">📅 22:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102097">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THa3cmo2oG2FimHPH1cTHtBpQGyUTlzwQ8WYTpK7HYAl-EZC1WRXq3pOy1v4iN7kIxWBAuZTW82ci35G9giVwXuyyZO1AVsRvD17JA_CuQUxTT2vDFW9R2093SmBGUybutBWzZaDAtzsWAQsc1_uW8JNSVQWGMZ748DDI8MVJpws6qvFAMc6LAsXoo2DzVM3PGZr1Nk1LhiK6uPLJtYfCvTKzJVFD2Vl_T2dbwll1jRH-UeyV-mEqGif2JyKOZLo8Pht0cIGZY5DUEdypJO0ygbtY3j8fFOtY1cH9zND9wYs3h5yO7SP8NR6pCUxu4a5b6JtgdrhkK1g1J9sVrCv6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فابریزیو رومانو:
جیمز ترافورد از منچسترسیتی به لیدز یونایتد پیوست. جقی 3 بار ادیت زد تا تونست درست بنویسه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102097" target="_blank">📅 22:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102096">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnasdi9vPMvKFNqjem1NzqJ5djmALnKBAMJIhB7cnbUhAy4nHiB3-WAVOavLQbgW3QpNzWI5N0CV5p3JrvYzWMuZ2dplrcwWsp5p6-uf3mMFDnwFUliNSyFDvVzx_MrOvf4gzAD2_8H_rh8AgAGNzxAydS-5k1J6faDKSUSvAlP9X_yzpf1UmPsQKa5OFac-tcMkBYKjWbhdkkGRoKr43M9XEOBsN3EFLAmNyPP137_R1-ObSm2C8uk7GkzRhrxEEQlowfsHfP4iFCN_b4u-toWQfNB41Aj8RYBwqCS8V4C5nKWlOkET7IPkb1mAJ4l4dBPiKaH7ClAH-7NGUlUGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
👀
تیم منتخب بازیکنان آزاد در تابستان 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102096" target="_blank">📅 22:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102095">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🔵
متئو مورتو: جان استونز در آستانه پیوستن به اینترمیلان است. دو باشگاه در حال نهایی کردن جزئیات این انتقال هستند تا آن را به طور رسمی اعلام کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102095" target="_blank">📅 21:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102094">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ze5IBMMKPzXIIYIGFyRVTEEGrIXQkTKWRQRKFY9z3hFKhPKJ0uAS0edv9xjINlGBGozzYrYtjuKP8RLe95Bp4H7g08Q9DhAELJ1T9OMi2HaFWEDAg3mIxCgWKqcajeYU_26IEMci5Ntf_Vx5v2XfbD8OnWHeqZOQsWzD9qMrpJDXRB9yls_0NpP8aqGhRsu6vMXHe_RpEIpt3FqpmuT0B2QEDAHysgvYZJKHnRIMBR6TD5d6SgJGGWtSr43TP2p5Bfn2RN2f-6KUAagVU1PQITztMS9T0IyDUXNg5xnpnIKhg3cQl1VpHDaJjQjxZqoXXiO5hUhDyyDjJU9tpCIjdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فلوریان پلتنبرگ:
لیورپول گفتگوهایی را با مدیر برنامه‌های برادلی بارکولا و باشگاه پاری سن ژرمن آغاز کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102094" target="_blank">📅 21:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102093">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAWE3e6BEyzhWNwm5o--tD8rChtPkiu3MI_J5lAS5vicXFsib6gkgbQluN0aYkmbIzcG_MDiQ9rZqyDcraI20xleoWWMFisMunVbJTmUAmwsAmneUIVpheLC2-zjSw8sYJSqpuVxLdqn0K0H2EhcW3iZCnMusOsHh7eCv6dO_YTBzSiDcslo1EvGS3Tgw8gwJn-piozBpidcQRH-o0_FT86L5JYiFNpCsJ10Kid8K5IuwCK_BPAkWeF-iW9MQxseQkvzqSqW5sSURIirlEnPPfg7vOOcpzikRUA3PA4AQIdvkpoRKZwSroquGfT1iuEx9LFn-pL-petlIKMjFDqv6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رومانو: چلسی قصد داره جردن هندرسون 36 ساله رو به صورت آزاد جذب کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102093" target="_blank">📅 20:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102091">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agtOQlaGFBBG9SxKi-6xOJCoaIkZdMqjsGhf-DWoc9BbR4hdSXfNc6-i6w5ctMmSJpSbndhbIUTaOfCU1d0hiSB_Jfy_nBckpokN8gHh0twzFqs2e0gpnELugaXvDTgOrT1YgiuI8C0v3-7eeqqt2Hpfwat5usyz1B00iyGBFAMYFQkgrFXYgSdAM1raQVt_ubkQCWT-EV1iJPIynDRzyztlyc85Qsp4id89iczT9YBAp9DYvwO9JsL8INS4vooPEuGjhIXkdbDXwZkeOLJRaHWrKF4J-G0iNFMAelaBLahgT_7vbhr9IR2MCkjOMMFi1ZCKLLBT6ZZrra9rP0oKgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇮🇹
فابریزیو رومانو: پائولو مالدینی و لئوناردو از سمت‌های خود به عنوان مدیر فنی و مشاور در فدراسیون فوتبال ایتالیا استعفا دادند.
❌
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102091" target="_blank">📅 20:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102087">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jf0Ktfc_ZlRBprj6-MgkS0mArTXn5Q-ftrhGZBSivjz5r5L4m5Boe1YOJYkJw6jnFCfeI-ySgBOARL4zKpfo6HHosKvV5rPtZbOrEFhoI2zkcWSWgy2lC6vnhJntIftlMutcCIndx_Q69GUJuKkhWy5p2fDddK1XcZdGrenjjlBFuwO62DilbZH27IwyjOKV0urZXe-YGguY2dE8m01HXUwX-SHyZUhS7CRWoY3rrqdInfM2d6_FCQ6qtwf230yttAgZhaxY0gV2KGY7iTDpc1bRRQpvD_xYOBj3gwbS1qGl58u2E7bM3vySvjoxPi0aJ7tK9xk9dpZrkReYQ43D5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gzf73VHeAN9yzNf8IIdYq6nyLlKjgPK-DdStAgSMDYdRXL-Ftcmp4TrQRDaUo-_W0IojmGeqJjpfZs3b0zzYZwcJDw59NzHC8jpIOftPbeMQ-uifkcYUtVRLg2VL_ca71CT0pbpXri0N320ZU-4MGtFr99RM0yHFTHiUurEOkYXX4T7Fq-_fUga2Cfe-GyIOqS-3uqhG8dkedmpl-D_guk6Z9zWp6khZaxMRhSTFoWpb0J-dggekxOtpfYW2cc8LqOzMliV-zUZFNI57LBPgYRK2u6n1oHX6dkLpY3T1wTjYXWkh3Ln3V5xpOT7y0YJieKiVTx7_PegU4Ng3A3GFPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZDbI3qyPfx6ky9a7WBGLNstvZdSTvW7nBl8Cp_OzV32R_Iw4WlYP3OpLXXL6K7A3bcoBK5v8eTTU8Rqn-QhO98ZSX44zbxfx0z2co2X503GpsjbTdlUQF3ocomjBJ_Z9TgmUUZBsb0c62Cbw3-wtrtBr15xa7CpjicLqis0EOBpipbb7Ap-lPzDWAfuvOeVWH9fNaFpIEbcNbIIMc9YMNbOcO5pauJRuyiFaSHzf5f4MUYhWLPbJSODVkBXC_3ExwL6NOiJT24hX6t-TLuZ7SqZ_fvPLHauR3bHk-AGKyeLCsU47OdzpWmSbxzE66QTOACfZMt-_5F-kxF8Dfnbdfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WVdfCov5A4cYWdgaeIYJ7DLg54vLU_eheJMdvEjvTe37-W8_8CNFii3Hvane99ipXHwcXiGhu0GFQL_CzhwSDejtAoq8CvrZti5nsnhBkZSpelubGlBar9a-QrHlfLj5a_qBZ_HLItGUs828FTXnjZ5_Dy-eDpVDubvtgNPykIlQ0I7M_2wjfJyKhxjXzdyCam7wKrpi5ka3YZb-8JtePEEo-Vw2D5IJKDEgRI-lbKNC7WcAfuvKgXMf_2x8KqPzdfhitvLwkTpwVAViAIe0sn9Qgr-WsNYC1x5fWkpUhYTCqi1soGyOjp7ysSJD6i2Hooxt3kkG5267czVW33UQeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عشق و‌ حال وینیسیوس تو‌ جامائیکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102087" target="_blank">📅 20:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102086">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZAJc1YRLLFOsXaCuERE3wSqGtq1XIL6y8YMT2afiPV6UHM0g-h7pXLd5j0bV-G7aSa-4W5chIYXdnpSVq7nIJZoWiVkJWMRf1LLMEdtQF86QuaQOMNmxAjnPf-ElosAuiJGQRjyl9jpVAa9QEEtwNgjrVjFcmAn9cgNcyvCI1rgxYZDwCBPAdWf-Wp0lnWtBqFdMaFGdnuJCgC-FPKLjNriMzNs83yDxWRG2LbCxzr7-NNSk4tE7onRgC75U-m6AKC3FuWIDz9_vhAyjdcFg4utmaykCw4Y6XR8ESxor9xXlRNkoakE0LvfTTp9bFkhTHRu25oVYgHUNlp07qRxGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
گلوبو برزیل:
سانتوس قصدی برای تمدید قرارداد با نیمار نداره و این بازیکن در دسامبر جدا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102086" target="_blank">📅 20:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102084">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/igsMlBMHL7-66UzE_JO2vKbdzNsQr_SZpIVBorTB02q9SnQ91DBr7ZDvc3nlKZEMqCJoTf0gOxLhFw03f11QxfTDY7gOLAN2Gg4L1vBglCI0vRGYScgvHfXkitWztps_ADz7x0uepr8ZTezULHvcJE3NnUrh-0SqfLg4VDWtDhzZzKp4q9PBHrPQ_P4cf7eTEETiOWazAtURtqdsNxU4UtRcGixvbJHvB87zwHp2Fq9VJDxzv7VJhKegPgqVKBxCqw01Vmnkhnza5Aes9ffBjNLG6_OcRmnWtO4eVqmlm4Tex4rnBaMO8DokeUC7l0munnlsgbEjdS93Ov1ii8tn3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CxWZB1z5s7gD0jtuz1CqCxb_7CkgRiDaG8a_w2sAR41jbfscN4CkAFI1QXnCqlETCcF1-DAeIfTU0CaqwaBi3u0GtBnysunN4DgUiAXDGiKMoViRF3ATFf-SKnFr2zm91vb8gCqoZoZXnJIOCbgEtPm39W-ij-s9xVtzFtE7BxSCql4O2mVv50jjEZE1d_wMPcdZ7BYsw84pEwWqiprV9CFRFEgqMcs6_YJQo7RGEyNByhXPozR9Qw6wgqNWbl8GogzIQsDuFhnL1eaPptzVD5yoN72fqzGbKDUJB6z3BRZFuM0VQOAPh4SOeiCkPEhwvsuf8k-jyZg4qQ6Xz2177A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی درباره شایعه معروف طلاقش گفت:
اینکه همه اموالم به اسم مادرم بود، هیچ ربطی به ازدواجم نداشت. از ۱۸ سالگی که فوتبالیست شدم، مادرم همیشه مسئول مدیریت پول‌ها و دارایی‌هایم بوده، چون کاملاً به او اعتماد داشتم. حتی الان هم قبل از هر خرید یا تصمیم مالی مهم با او مشورت می‌کنم و این روند از همان اول همین‌طور بوده، نه اینکه بعد از ازدواج یا برای فرار از تقسیم اموال اتفاق افتاده باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102084" target="_blank">📅 20:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102083">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzA1DHRLYj385CKQN4O2ks41r80o3Zp3AXyLgZ3FOVnReo7jekaErO0W-oMYNMFuXObVLnOcpFYS-MPwlTx66mOj_Fc8gAgNzdSFaJSJx2XrLIQf3RSU1QZt5ZNMMEA53F_PcSaODu17OS7XwXIljreSW7hY52n56jNXpZgvdZoeu7o-DG8KYtoNdmt9HcN8xVvDvczJ69LnB21sc653H0oziMqSpwQnfezzP2hDo1uyn2WgMe2EzK2WY0Cdm3iBXHp3lQsyZ1T_IQc0j2iXZtHbFR-k0qce1tnzahPx073qi9NO_pTUeb_OG2v_2eksNW1GLzp88bXOOTmGiZT55w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
⚽️
امار سه فصل اخیر جونیور کروپی که ظاهرا گزینه دوم بارسلونا در پست مهاجمه
جونیور کروپی ۲۰ ساله متولد فرانسه ، پا راست . پست اصلی پشت مهاجم ، مهاجم نوک هم میتونه بازی کنه.
💸
ارزش ترنسفرمارکت ۵۰ میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102083" target="_blank">📅 19:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102082">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQWOHAf_HtnCwN2vvznVl-FMcHIBXWDH-dcjI2sQQ9YW43xxoI8SdPctLwD0k6NhVpZB5mFuyZFNO6SqArzrHGB2STb3tydOpDsINqjVtc4PJkk1Q9ExbNI6L_nMiLF85AwTYw4VaVUypCXHOYpCptgXdhEuyCPleXyvkvQ2Ubb6I1p2DOiIdXVx4FarfIHUrvAb6j45AksFf3uhamGnQXAS3-NpqVN2pTJxkNU5o22v7wjaHx2mMRB7OXDAM8tsggnQmO5k6GFlbxqmGZSpuN3guCdxDzBmXqpeNykfmnypnWg7BgcDmLshy05Ie_NNAsNhw-4LqJ92ocLo0m1C8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قدرتمندترین باشگاه های جهان از نگاه اوپتا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102082" target="_blank">📅 19:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102081">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e948c535d5.mp4?token=WwF2hJIgm5mfkQ2EgtaHx51NGFuEATMazlSp837Rq8mAtQFzU9uqguJfKjMnEmD7ZUwvxrybnTkEYLpUOq2meFO0SWPeEuvmINTqhnli9m5nfEjlHHeJkOUjK8gNwnRIAi2BApQXjR3hrFI5cE3i7_eqsMZtrNiZkG8Ky0QUYmN8mBZDPnAJgSfx9u8V6NOALpls7pfXEhpJ1FLGpMKiyLIDrwAr7-OW23TL5hT-xwhMYwkq-XX4XO2Fqjn3vN_bjJBl6CrwqHM_71owyifPypDMG-HQ99M4ii2i851BjndlYFctASm3cHOCEjYZ7lr4t4LMV4hEV6YeZsOkE__z3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e948c535d5.mp4?token=WwF2hJIgm5mfkQ2EgtaHx51NGFuEATMazlSp837Rq8mAtQFzU9uqguJfKjMnEmD7ZUwvxrybnTkEYLpUOq2meFO0SWPeEuvmINTqhnli9m5nfEjlHHeJkOUjK8gNwnRIAi2BApQXjR3hrFI5cE3i7_eqsMZtrNiZkG8Ky0QUYmN8mBZDPnAJgSfx9u8V6NOALpls7pfXEhpJ1FLGpMKiyLIDrwAr7-OW23TL5hT-xwhMYwkq-XX4XO2Fqjn3vN_bjJBl6CrwqHM_71owyifPypDMG-HQ99M4ii2i851BjndlYFctASm3cHOCEjYZ7lr4t4LMV4hEV6YeZsOkE__z3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان کریر سرمربیگری دلافوئنته
از اخراج تو تیم دسته سومی‌ تا قهرمانی جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/102081" target="_blank">📅 19:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102080">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
فوری ترامپ: به درخواست واسطه‌ها ما در حال انجام مذاکرات فشرده‌ای هستیم. اگر این مذاکرات موفقیت‌آمیز نباشند، به اقدامات نظامی قوی بازخواهیم گشت. ایران فرصت کمی برای توافق دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102080" target="_blank">📅 18:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102079">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghbmq9yqixkcJ7YrVD5Hhsj37ju58lYh_63raN_fVdSLOdnlPTHwSoTy580EcmE2hlLFgH0WFxZnfdj0LXq77r6Vf6udcDK4yan5o3WbYVGoLoNfgL5q8tgIGmbtzTQy-lrwhWI9MuP5B2Pr9jsfeBuI3gga6PGYwb48h9DKludqaepPPzy8ETAaN6DZNAUpdiAloLOeIMfEYHyLeo3i3KOK0IcA7vTb-3fpxzOmn2ZU2_E-GImkba4NMI10fbAhxqX9bw5Grd2KU-SdXpBLNPkW1HJriNMcOEH4qVhnEvMhNBt433lRIWBqlAKc3QdijX4lhMvrAT3mlH3ezpKWZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
👀
چند ماه پیش الچیرینگیتو توییت زده بود بارسا به بازیکن های بالا نیاز داره، و حالا همه این بازیکنا رفتن رئال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102079" target="_blank">📅 18:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102078">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0eUAPo6_P7IG4fgr6t2d2zB1aFLO_fDmIgoJDKWTvnHbZAfB-3jA9ptqZlhmUh2dhJRX9Idn9M5_FNzzZUoiqSWo69j_ZQom3ALUBrsNGGaWyi9CY26p5JDsa8YFzWkuC6XqGHDjyqCdc9Y2mLCkTYHXjFoPYYMvt3xOS4NN0y7A9R8Hc_Y5ZSwE9aIf6-p32Q62oOhHkhFlO6mU61cHOxDwuVHAM8UJJPZ-vcEaCE-sdfCVwtlSyL7S1ZXN48emXU1twsTOSjJPLdbWg9AWXxHN2loVa3fdpXJ2JBggmezmH3Hb6qrfSnvMEbJmChmd04EhzADRXAT4MOtw_wPog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
امباپه:
ازم میپرسن ممکنه یه روز سرمربی شم؟ نه فکر نکنم، من تو تجارت مهارت بالایی دارم و میخوام که تاجر بشم البته بچه‌های تیم میگن تو میتونی برای ریاست جمهوری کاندید بشی ولی باید بهش فکر کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102078" target="_blank">📅 18:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102077">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gr9CP6iPBqH-GLnh49gVs15FS6tjpsf0B9tKxu_480pd7P2QMSB_nedrrUsByNrhb1m-zLT-V9MrtU_Mciqd188tOKk2zS5HWctcKkdNyoSBCf3Yh9JD5de9l-6fRUhuZZ56c3cTtruHXjzKd_m3WN7QzZMXgw7kmW0OBO3c0IKQihxpAYffzveylA1UVUHcxEs9l9TpAG3eGV0BuXrv2GTtHMcTuPwzO9o-bEMs3nlmXszJ7HkygpkBDuXokeE-6c6TKX6Z9tBXBsXVjM3syONq3zn8kXssQwJ0YNG64FCydYEVTopj2RbPBJZeM_ZDJLNjv30zYUgstiuP1840Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بی‌بی‌سی اسپورت
:
یک قانون جدید در فوتبال انگلیس در مورد مصدومیت‌های دروازه‌بان‌ها اعمال خواهد شد.
اگر داور اجازه دهد که کادر پزشکی وارد زمین بازی شود تا به دروازه‌بان مصدوم رسیدگی کند، مربی تیم 10 ثانیه فرصت خواهد داشت تا یک بازیکن از بازیکنان حاضر در زمین را انتخاب کند تا به مدت یک دقیقه از زمین خارج شود.
در صورتی که هیچ بازیکنی در طول 10 ثانیه انتخاب نشود، به طور خودکار کاپیتان تیم به مدت یک دقیقه (خروج موقت از زمین) انتخاب خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102077" target="_blank">📅 18:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102076">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKRHon6TBR7InAJVPe82s6Isbmd9Z4Ym4dXcUZFbUrUMuc9vMyNhrQ4BWktYXROmEJQ4Ijiz0iNapUIM3ayRhwfJvw49Gqwoj-QoHnr14AW_szkPOOZOaWXC69BXNNMd_cqHN2_AOAwCdFsl0F795Yo08EZYVHGb___XAYie_bmofPK3jZXztfV_LTWKkYl6i_PQ-vCdpLLM5Z64uCjBFCQXSdNtabsUthYBCfCoaj-MTJypsm2fzEMPxlGosKz5pZWL5jBu3LkfwRKT-eNBCntUEUqFlSaRvuO0rvbYq80vz7-jysSUkvZA4f2QFgq3dE2cQaba_iah0y5tdcX23Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🗞
فابریزیو رومانو:
‼️
بارسلونا با افراد نزدیک به کروپی وارد مذاکره شده.
⚠️
بارسلونا با بورنموث تماس گرفته تا درباره امکان جذب کروپی پرس‌وجو کنه. بارسا یه سری اطلاعات درباره شرایط بازیکن جمع کرده و چند تماس هم داشته تا وضعیتش رو بهتر بررسی کنه. کروپی بازیکنیه که داخل باشگاه بارسلونا خیلی مورد توجه قرار گرفته.
❌
البته این انتقال خیلی پیچیده‌ست؛ چون بورنموث نمی‌خواد تابستون امسال بازیکن رو بفروشه و منچسترسیتی هم بهش علاقه نشون داده. بنابراین، این معامله اصلا آسون نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102076" target="_blank">📅 17:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102075">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1Q3Q2yQrQ4Mso2Jsy_xnytGDKRP5UBCqjMpGHIBCNmTwzWDtdRxDqnl8WnJIHscLLzhavtPJ6QenJbLWyGgvx246-zk5QxWAP3vf1sRKnG7pMJi7SEobtDQcAaCpVFw3NEz_6z5pIIq_4T7CnGLDfgzSxGaTTI5eaar7ZMS-KAQXhRg6LLMWNJR9VFtodFCo_DwSLaTCtfv2zK27ulED-kB7g6PmAGZ4Zd9fePe7DIPnTRxxXZN1KO_3rG-SSDOYam1gzI33gswQQCdJJBaRTsSlQh8f6k_EqsQFvtWTSitkF1H6_pJJ2oRB-aQSVd_s_C7FkcROzKe9UFqiciGNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
فرانس فوتبال اعلام کرده که بردن توپ طلا حتی بدون کسب یک جام بزرگ تیمی هم امکان‌پذیره.
📊
این اتفاق برای این بازیکنان افتاده:
🔺
جورج وه‌آ در سال ۱۹۹۵
🔥
🔺
لوئیس فیگو در سال ۲۰۰۰
🔥
🔺
کریستیانو رونالدو در سال ۲۰۱۳
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102075" target="_blank">📅 17:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102074">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sK42QrsLKGsahCWfnS4IiuTwHzSrgMelEDXXkUKqjIP7kbHz_ij4EkmmU8lpJzZPXd1xZ2_NmqvD3LlaG4IUnKlLAKMiNTNQ0E-v3STTqfNvbcQ6Iu23h8WnbxbAq8LCNofxTzmQvTVF1opUuY_OFymoHiZL2L_dNWYg_OVjMbRzztH6vgdrnkkb_-6FItzcuD13RI_nyad4P3HRyBJk87XCOPsArxfFIf4Wa_QI0zbSQI16L_ngYkOUiJIHxIbubH9MjACQbZTC7BGNatr5ZxSK09TvmtX6YOmAPis1UmwyINWWpaqA7WnQqxPu6WI-XXxBjVuMw-sOBEpmiG3NnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
یوونتوس و پاری سن ژرمن در حال مذاکره با سوزوکی دروازه بان ژاپن هستند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102074" target="_blank">📅 17:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102072">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JJC084Wc9Sy9fqIacSsmHTaP0iymM7diHGPxeAKfr7u3ofvBlZCXna19UOSnmUIJQfN4Qv1EQZzVeKmcH_NrsnWK6mxYzL5KdwTTY14daCYuZBM0jEyB99DdfiSUJqxIUKeRbEjig0SwhQlzF06gPVMRx_iz1UvCICRkyI9GuWyXFaFjaKbF4U0Wlw2cD_lcZ_xcMYaMKa6GwzXjZ4EktXIRxlyhaus_I-rohy1lNmU3FKr-C7e2bTtTEkwUnbt7bA1mZxtEWzXLCycQ4azv9cW0DRQBg128a4B6SsWTaYCjdci6U0cKIJ-UEqM39MAT6agYsLJ2c6Z_fG8DNZnjpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fX-YuL3dDdB8IrYI_HLhRPUdCEcpC1XoriYkl24QJR2uFNwA4--ezJ3iIYhdVbt-gGf8aXr_Q6MVYhhd0bA_Co_IO-E6S2cbHzIh8-C7Ek4Iijfn40SZip2F7-334TZcCY6wb2PWv_-tmxep626t6TtHNB1-86WPTJkmPrDmNkSyYj3dSBsEL7YhUhVAV3b6poWzvjj-gIUYm1bkix4eC8c1VyDYr3o_tElf0aZHc-TI_HQ5VV9VS_1zhfFBXN4b32WWQxM9WWAEwSP_IfeL9nRcr7olAWSQKZYgGx00TfOmX_femA_8YraN8FIS-MPGpSF5elFkG4GyJZ9RrsgYtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی درباره بهترین خاطره دوران کودکی‌اش:
روزی که رئال مادرید با من تماس گرفت و من را برای تست دعوت کرد. آن روز بهترین خاطره دوران کودکی‌ام بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102072" target="_blank">📅 17:01 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
