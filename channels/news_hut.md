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
<img src="https://cdn4.telesco.pe/file/PH5jacSICzZKzBiPDv2r0mlDQ_Y_904WdWPvpCREQnv073_t-ocS4bMwqbqjvecaYtxToqbU5usJHXP3Le0nythdvwkQUwdFrH5k2UvsRq-mqaDWiDL-CdOq3CWVkJ2kSdqBrJe9NGc_wsky-GA_B3yq-RiSpjYcrOkxZM-AMzg5ZVVgi-ulG_MKjD1RP7veQen3JNrPN-0PN_piGvxa8TzXwA8_ZcbSAr8ZJa0ryjr_P6Jjtt7aXXN76_z5jEwysvnRF4cb56DHh0Dno61WrA4c79PzW21OaYu5vJLFsXCyKg1aPw_G01hpgVV5hzo2ZwmWz6uHaNrpBKNP9hyAxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 112K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 05:39:11</div>
<hr>

<div class="tg-post" id="msg-71119">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71119" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/news_hut/71119" target="_blank">📅 01:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71118">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLuXNtH3SxQKdK4xMw9Qus0bXok5Z21iEoyMTRz9wpFNZvc4tHOo7EMrrMOClkAIOle7FXLXasgy0LVLgSo4QoK22g89XAZ_psy5KG4lawjtPLCPBIxgHp2gcQNzby98jrmYrxZXk86cIclMgdCssMWD_XTFQ1SeyaQG_me_Xh5gFFIU3SXIAUo0uSV8ne7FReIeKH8bGSUTQ9sT-c4J-BN4GUVjAuVeQBy77miyOlEhmJx4mzE_Eesfzb-UidoEsCW1ncZmhB6yy0nIcBldAiDx-CwGL0Utu7UPeBnJ8SekGfC_l0KuO4uWgVJi82dtQJ6z_HRrCGpTTIpSB2iccA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/news_hut/71118" target="_blank">📅 01:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71117">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59487b6d80.mp4?token=ZH-eWDhOoYBnrTa6vKr_Es06CihAy9Y6ZVW7sM9i_WAfPap5MO7KEbKYw8hePLStInb4ZHfN-z1NUu2FwJNPCDRsixZHtzvI2Y6IrlyU0Ot3IqGUXU27S7ezesbt1W1RVy7NV02ftgN7dIQ6AJUbn-PrBIMOVVvia8_tCylJiEsx023zGAFjS8pcA37_SRN0ro2y3K5sR7xXgmg1hLYPE2i8RiMgWvEwD5a65ArZeXQor3xUvuRQPhGVihfUaYeri_1ihwuksdbljRuZg-4lW60hLPBCiv4GEvwH6vZj2zE0s_QRoOaYZueRJAnJ-o229CfT2cqIraqWtlos7Jt2dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59487b6d80.mp4?token=ZH-eWDhOoYBnrTa6vKr_Es06CihAy9Y6ZVW7sM9i_WAfPap5MO7KEbKYw8hePLStInb4ZHfN-z1NUu2FwJNPCDRsixZHtzvI2Y6IrlyU0Ot3IqGUXU27S7ezesbt1W1RVy7NV02ftgN7dIQ6AJUbn-PrBIMOVVvia8_tCylJiEsx023zGAFjS8pcA37_SRN0ro2y3K5sR7xXgmg1hLYPE2i8RiMgWvEwD5a65ArZeXQor3xUvuRQPhGVihfUaYeri_1ihwuksdbljRuZg-4lW60hLPBCiv4GEvwH6vZj2zE0s_QRoOaYZueRJAnJ-o229CfT2cqIraqWtlos7Jt2dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
مردم آمریکا چه زمانی باید انتظار تعیین تکلیف (resolution) در مورد ایران را داشته باشند؟
🇺🇸
ترامپ:
انقلاب(Revolution)؟
🎙
خبرنگار:
تعیین تکلیف(Resolution).
🇺🇸
ترامپ:
تفاوت بزرگی است. فکر کردم انقلاب(Revolution) جالب‌تر بود.
⭕️
🗒️
به دلیل تلفظ نزدیک دو کلمه راه حل/تعیین‌وتکلیف(Resolution) و انقلاب(Revolution) ممکنه ترامپ اینجا به عمد کلمه انقلاب رو انتخاب کرده باشه!
@News_Hut</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/news_hut/71117" target="_blank">📅 01:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71116">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ef0c44cf.mp4?token=Sjbo6WJ6Rw8hiFjZCjd5EjgF_cgvitDDSV4bYj2Plcbdh6G10E9N5jkFsQp4Z7xzt-2TL61GMyvCdp7xw2uxd35jYX8LGnZetlXQ49uM2abgHWqm7kJkUiC_d9h5lKZpem2pdHiGXG1HVT_2d34iGCFk9KfG6m8VB1LC4JoXgYg-KpU3ZVqriCNkA8B2DIbSAyZ6wzSfgYCV1mR8IhEP1db-0iWIDuPbFR7SAw4j4idy7v2gEeYmIzUWROvElP5lKMzRl1we0eDPrdtt6qDKVH9r-8b2YNuUeU3jTql_ml3RjPSLdBzpsb0xOueUZ2iLuywp2oQL2KX1TDqVcNDTGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ef0c44cf.mp4?token=Sjbo6WJ6Rw8hiFjZCjd5EjgF_cgvitDDSV4bYj2Plcbdh6G10E9N5jkFsQp4Z7xzt-2TL61GMyvCdp7xw2uxd35jYX8LGnZetlXQ49uM2abgHWqm7kJkUiC_d9h5lKZpem2pdHiGXG1HVT_2d34iGCFk9KfG6m8VB1LC4JoXgYg-KpU3ZVqriCNkA8B2DIbSAyZ6wzSfgYCV1mR8IhEP1db-0iWIDuPbFR7SAw4j4idy7v2gEeYmIzUWROvElP5lKMzRl1we0eDPrdtt6qDKVH9r-8b2YNuUeU3jTql_ml3RjPSLdBzpsb0xOueUZ2iLuywp2oQL2KX1TDqVcNDTGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو ایتا و روبیکا از یچیزی رونمایی کردن که حتی خودشون هم نمیدونن چیه
😳
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/71116" target="_blank">📅 23:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71115">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1e4d7b78.mp4?token=NW1HGq1uHDrCFu5-usfpivvdx7qlV12H5GPlQtzeiYO7K7a6dbVVGoDXrc7ZbotVMNld8Xf8SypKcVSB12yRxLejKVt9iGExDjvwF-R62dBRfYXbJ28ucF-uNECizJriwFUPjDAVl8T3uEKZjAWA74P-VniZHJAQqijAHycQxb1tUan0hl0nF_jybosfWxt2480lrCT4omHAr2tvH6Ht9Aa5B35OdgTIRzI4d3H7WJ1DTk03h46jgb-QD6Sx_Ra_bqloH9ufD8z6J6J1Rrb9gveHc3btnkL7EmM87FwTDALzGcJl3J0R4NyrV6ptkSHjFaSMB-eRibw_9KEViIdndQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1e4d7b78.mp4?token=NW1HGq1uHDrCFu5-usfpivvdx7qlV12H5GPlQtzeiYO7K7a6dbVVGoDXrc7ZbotVMNld8Xf8SypKcVSB12yRxLejKVt9iGExDjvwF-R62dBRfYXbJ28ucF-uNECizJriwFUPjDAVl8T3uEKZjAWA74P-VniZHJAQqijAHycQxb1tUan0hl0nF_jybosfWxt2480lrCT4omHAr2tvH6Ht9Aa5B35OdgTIRzI4d3H7WJ1DTk03h46jgb-QD6Sx_Ra_bqloH9ufD8z6J6J1Rrb9gveHc3btnkL7EmM87FwTDALzGcJl3J0R4NyrV6ptkSHjFaSMB-eRibw_9KEViIdndQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
طرف اندازه یه گاری پول جمع کرده و الان آورده تبدیل به دلارش کنه، کل این همه پول نقد شد فقط ۳۰۰ دلار
!
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/71115" target="_blank">📅 22:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71114">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/05f93dafa7.mp4?token=hiwRwwhq3Om7IiFHWeH0HH2Ov6xsf4SbVmpYV_nK1gkhINBWHn6_3K32MThN1mdPuHrEIM1rVwjSdUOj_RekC3Y2ZpTWEM_7QgIWFjwQU4OEGYqls-Is6sMPPlO8bH3NUMv4307FaH6Ps2gSwsVDBw_59MjBFMUODOoDW3c4VCUye3yInYRinbF3tozawxgwA-4Oqg1bD9gBpX2gtizgBuBrdtMhhT0PXqAqq5OGM55m6yKpnBgrFj6BiQGPlb3OdEPtUtUWVlDAl_JCBxRy0T07tKKtGjzKOaj7xkrYMEQ1V-ZZYM3M6ahz3SacbrqijmgL3hHRSa0AqGE78NGxC1xLvULcNZQNfSNt8dtG134uvzgUcCsku7ERyvL5jldw4ya5ak6WZX7mkqmpcpLzsrRBPflm4vhlvkJh1U6sPHFkAZl_86jT-mr1EGh6mFTTkh-tF9k_ylyN_eB9ZeI8FrnN4pejvRJpLZqdq0PgufsYLAKDRFbBWmdE-vvx4V2MAUmmY-5RSs9Cy2Wai7_toSAR2FYvj7kootMa4MQewE3zV2TLj6ypG5E3o14SIf26AvO4rBvxSB4FvFCXFCIt3Lat8TdZUYhAypG-hAiwq2qp4UnbxzLIuULPtEcEi9RYX-Q78ojb89dz_oW-f7KMCtBLHHqelIDlZSaxRGOfpV0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/05f93dafa7.mp4?token=hiwRwwhq3Om7IiFHWeH0HH2Ov6xsf4SbVmpYV_nK1gkhINBWHn6_3K32MThN1mdPuHrEIM1rVwjSdUOj_RekC3Y2ZpTWEM_7QgIWFjwQU4OEGYqls-Is6sMPPlO8bH3NUMv4307FaH6Ps2gSwsVDBw_59MjBFMUODOoDW3c4VCUye3yInYRinbF3tozawxgwA-4Oqg1bD9gBpX2gtizgBuBrdtMhhT0PXqAqq5OGM55m6yKpnBgrFj6BiQGPlb3OdEPtUtUWVlDAl_JCBxRy0T07tKKtGjzKOaj7xkrYMEQ1V-ZZYM3M6ahz3SacbrqijmgL3hHRSa0AqGE78NGxC1xLvULcNZQNfSNt8dtG134uvzgUcCsku7ERyvL5jldw4ya5ak6WZX7mkqmpcpLzsrRBPflm4vhlvkJh1U6sPHFkAZl_86jT-mr1EGh6mFTTkh-tF9k_ylyN_eB9ZeI8FrnN4pejvRJpLZqdq0PgufsYLAKDRFbBWmdE-vvx4V2MAUmmY-5RSs9Cy2Wai7_toSAR2FYvj7kootMa4MQewE3zV2TLj6ypG5E3o14SIf26AvO4rBvxSB4FvFCXFCIt3Lat8TdZUYhAypG-hAiwq2qp4UnbxzLIuULPtEcEi9RYX-Q78ojb89dz_oW-f7KMCtBLHHqelIDlZSaxRGOfpV0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
یه بلاگر ایرانی رفته چین و ربات انسان نمای چینی رو به مبارزه طلبیده؛
حرکات ربات به قدری تمیزه که انسان واقعا از آینده جهان خایه میکنه!
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71114" target="_blank">📅 22:16 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71113">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66a864cef.mp4?token=CxdFB43ay-SGPw1JWB382d-xLrIVENNUXO3JRU4s7bL3nV0LLkRaeXHGmracmDGaCmtHBra0x2yvzr7Egfel2ycheMDQEqUzJabUy0tpvn4py4ctPXtf3_2HG8eu014rznO9dA4lGhBIDWUjqoSZDaFeAuu7C6EotX56h9AW3zpTf1ugHf6-hF31Jz-w0lS1SrapcbZNrpalpeepGw5jNKQ8uqHAYeHhAbXKVnv4Yu4RXlAzp_LWV5WpeiTXAkZGuvR9fn6_CGGomz0KXQPQjS5qVc0QM49yzRFJ1qDPmnBmNIOrRMeGjn95jECnzgHXeWUxg5t5Yyht9fti37Kxig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66a864cef.mp4?token=CxdFB43ay-SGPw1JWB382d-xLrIVENNUXO3JRU4s7bL3nV0LLkRaeXHGmracmDGaCmtHBra0x2yvzr7Egfel2ycheMDQEqUzJabUy0tpvn4py4ctPXtf3_2HG8eu014rznO9dA4lGhBIDWUjqoSZDaFeAuu7C6EotX56h9AW3zpTf1ugHf6-hF31Jz-w0lS1SrapcbZNrpalpeepGw5jNKQ8uqHAYeHhAbXKVnv4Yu4RXlAzp_LWV5WpeiTXAkZGuvR9fn6_CGGomz0KXQPQjS5qVc0QM49yzRFJ1qDPmnBmNIOrRMeGjn95jECnzgHXeWUxg5t5Yyht9fti37Kxig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اخیرا بعضی دخترا طی یه حرکت فوق‌العاده و زیبا، دارن هرچی ژل و بوتاکس تو صورتشون بوده رو خارج میکنن تا نچرال به نظر بیان
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71113" target="_blank">📅 21:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71112">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEj7oGqDsriQVIOS7bnZ8sC2xLccwoKf0FYZRvf7MIczUi3tqmky-_nb5QqUf1-fx5uJDF1R3fYWbJk2GnuDQIvxMlyyvNvw2PejR7DI1trnMS_Rem8gcBKX4eyDsATFrI2-UiaAlz4HHY3pj7qgfEP7OvXF3mKpkhIKyDKu6_3oH9EdynVu19SBCKz_K4qdNKymmhvjLQ6ZK9Aj8uUvAsmAHqskvwfBOp50rC7QPX617Mpe2fsVAOLIO5GT74vvo9VMd_3-Z2nUb-Z5d67tBQufwwpzKHhGtnBDXLF0LYZ3pSHgQwiCZe4xS29iJ8xYz7Ju00Cnb9FJsBGv6ytdJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👎
قرارگاه خاتم الانبیا: حملات پیش دستانه علیه پایگاه آمریکا در اردن که در حال آماده سازی برای حملاتی علیه کشور بودند را انجام دادیم!
❌
خبر بالا که بطور گسترده در حال انتشار در رسانه هاست فیک و نادرسته، همونطور که می‌بینید سپاه پاسداران و قرارگاه خاتم‌الانبیا هیچ اطلاعیه‌ای مبنی بر حملات پیش‌دستانه منتشر نکرده
@HutNewsPlus</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/71112" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71111">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcZcph6ic5KNvZ1NjU1--krUOSHdLfuuc8R_KgDiZlNUc5_CYv41yfFLmGWZmOkLIS5YEyhQcM7tWdY4gYX4YZgcAhAIVmxwKDwm7sNqic0feLwxw617lv7vvqr6siXHNsBrdYC56j1FoE8xV2pRD8amVsvCOm64BGZY_644iXfHSryDnHUQL2FThoFocwVy8tOnCseK-5w-SErZC7JGy8VftQSyzoFbyl7VbErEYSZX2NF4OJJsnMuG5-UkC8yd3LgDLhuyuinTShHTL9Z_PREcIRWwv67Q8uSJYcX6ICaWsmYtgDNc-L6SP-K9zVkksxL1rpsj7VuToGoE_4W-iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام ارشد آمریکایی به کانال 12: در حال حاضر هیچ اطلاعی از وقوع آتش‌سوزی در پایگاه‌های آمریکا در اردن وجود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71111" target="_blank">📅 21:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71110">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c74f1d2d4f.mp4?token=iat0vwfu4gqFJv2-gHCyJlWZq7e91NlNJxljrnBNIrreuTw6WYOtc0FU2rBsqb0Qz-_r-6zhlGcRgYom8YdDftqOjA_pgHpjtXOsf0rMApX1vzOMjFc7LlpqgAGR7lhywAA_OgV_nymE4n7uKmgJgR5xz9UCxybzhByNk6-mAgS4hhofVRR70Hn_37PxPBifGTORHcFpU3L2NZJumBJuoIcbS1JqTXLIfUAPogKigUTOFO-9lwwWcJeLH6MIA3AHJUaXin9GeUovGpWQV5jPI--wlthuStbHiJktBmoaQgVdbhmvsOgwbyPRtjm8mWflkLLmYvT66fadFSYtKaEzFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c74f1d2d4f.mp4?token=iat0vwfu4gqFJv2-gHCyJlWZq7e91NlNJxljrnBNIrreuTw6WYOtc0FU2rBsqb0Qz-_r-6zhlGcRgYom8YdDftqOjA_pgHpjtXOsf0rMApX1vzOMjFc7LlpqgAGR7lhywAA_OgV_nymE4n7uKmgJgR5xz9UCxybzhByNk6-mAgS4hhofVRR70Hn_37PxPBifGTORHcFpU3L2NZJumBJuoIcbS1JqTXLIfUAPogKigUTOFO-9lwwWcJeLH6MIA3AHJUaXin9GeUovGpWQV5jPI--wlthuStbHiJktBmoaQgVdbhmvsOgwbyPRtjm8mWflkLLmYvT66fadFSYtKaEzFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک ها از ایران به سمت اردن
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71110" target="_blank">📅 20:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71109">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
منابع عربی:چندین انفجار در اردن رخ داد
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71109" target="_blank">📅 20:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71108">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbf8f1e1a9.mp4?token=nd6ShmUtgWq_vZ69tHA6q0wu2hAL5QOYNKJW2redoWs9zuIm7e6DUSc9rM_zTVpFQ9oxHYLLx-CzCtKxTTfadjFrs-SRBKWXSaTURaLLX3mAECENYkvjGbzRCZ1zeEsJ-va03JTSw6xTULrCVT6_MSRNa2_oJY8w6RfA8HAaSGOnlTSRDEv9LRTkZ1VoipNrOtZdQ8XAhbvh18WQ_RcBjjmK0EYP0bYElWLnonZhldmaoERnw47jcmp9xi4TADIP36EVkDvDbMRMlU3L094Djh-kj1JVatkHK5UYPz33lP8363vri5ur6SChRssBS2fo-Tadwbxe7UqRrtnWixmRXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbf8f1e1a9.mp4?token=nd6ShmUtgWq_vZ69tHA6q0wu2hAL5QOYNKJW2redoWs9zuIm7e6DUSc9rM_zTVpFQ9oxHYLLx-CzCtKxTTfadjFrs-SRBKWXSaTURaLLX3mAECENYkvjGbzRCZ1zeEsJ-va03JTSw6xTULrCVT6_MSRNa2_oJY8w6RfA8HAaSGOnlTSRDEv9LRTkZ1VoipNrOtZdQ8XAhbvh18WQ_RcBjjmK0EYP0bYElWLnonZhldmaoERnw47jcmp9xi4TADIP36EVkDvDbMRMlU3L094Djh-kj1JVatkHK5UYPz33lP8363vri5ur6SChRssBS2fo-Tadwbxe7UqRrtnWixmRXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇨🇳
بِسِنت درباره ایران:
آن‌ها محموله‌های نفت را به سمت چین روانه کردند. منتظر اقدامات مربوط به این موضوع در روز سه‌شنبه باشید.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71108" target="_blank">📅 20:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71105">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64aa07a7bb.mp4?token=PxsbEvaFISn2JyUC7juY3d2ir6Ch2mo4-C05wwyUe4owBORotnUyFWgDqKF1sYj-vPIaOz6nMRMt0nxEY_LBrniRZKQRc8J1T4s5_tQ4kLG4xHgdHbPOvJGtPbK0CqaMLA7PPBCNJD8UhyKwqFS6aTOliMTCd9aoJAKXDhvTI_6sq_UfKWMdUp9m1z7bkJOzAfdliRFmGD2Ti61n7Rvw_PkPCOYjlt3YePeq_t7qn9HODF-32_WkAKvUvdgk6-vi6CoWTmsr0HADo7zmU4ji7Ou71F3XxL372p82L81HaKa6HWONEH0r3FZJwKsUOo15thHchDOxph0PTVrO8Pyz4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64aa07a7bb.mp4?token=PxsbEvaFISn2JyUC7juY3d2ir6Ch2mo4-C05wwyUe4owBORotnUyFWgDqKF1sYj-vPIaOz6nMRMt0nxEY_LBrniRZKQRc8J1T4s5_tQ4kLG4xHgdHbPOvJGtPbK0CqaMLA7PPBCNJD8UhyKwqFS6aTOliMTCd9aoJAKXDhvTI_6sq_UfKWMdUp9m1z7bkJOzAfdliRFmGD2Ti61n7Rvw_PkPCOYjlt3YePeq_t7qn9HODF-32_WkAKvUvdgk6-vi6CoWTmsr0HADo7zmU4ji7Ou71F3XxL372p82L81HaKa6HWONEH0r3FZJwKsUOo15thHchDOxph0PTVrO8Pyz4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بابک زنجانی: دلار رو بدید دست من تا یک سال رو همین قیمت نگهش میدارم وگرنه با همین فرمون کشور تا یک سال دیگه نابود میشه.
من رو ۷ سال بدون بدهی انداختن زندان و همشم تو انفرادی بودم. همه اموالمم ازم گرفتن. وقتی آزاد شدم حتی ۱ دلار نداشتم.
با چند تا تلفن ۱ میلیارد دلار پول جور کردم و چندتا شرکت تاسیس کردم.
من میخواستم سایپا رو به قیمت ۲ میلیارد دلار بخرم که نشد ولی خودم میخوام کارخونه تولید خودرو تاسیس کنم
من توی خارج کشور بانک داشتم پولای وزارت نفت تو اون حساب بود. اونا تحریم شدن پولاشون اونجا گیر کرد گفتن تقصیر توعه و حکم اعـدام بهم دادن
تمام بانکای ایران بیان جلوی من بشینن ببینیم من بیشتر میتونم سرمایه جذب کنم یا اونا. فقط با چندتا تلفن. تا معلوم بشه کی اعتبار داره
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71105" target="_blank">📅 19:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71104">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf31ca2a30.mp4?token=dLu2aQC54dwBeQw0FS1mDV5SnvV3IAByulZO12_dGoQ_wImUPS-JAappoI6BUznmgxGOxjF9LohuSCa2Zk_QaYrxu9_Xu3jXDmkjsvYlx6TvyaPbLhpggr7gL_YJN9oSHwC70b08EXZGPzyf8_pt8p1HgzSDRBkdB6rSoxvtLuPPrO1dSaqhllRDoR_bb8MxWhZqaATrynoKpS2ZyDHMX6q327smBcU7c2atCsI7HiMNsvC6AiMS9hEa2b_ASWwNCcvWJ-iaB4uFcxBr8e6J8l9udu56amkNcakGReUOj1rDWYL5j7F35iA1FGFG_ofbX1vfyYO3Wg9U7-W6W8KPtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf31ca2a30.mp4?token=dLu2aQC54dwBeQw0FS1mDV5SnvV3IAByulZO12_dGoQ_wImUPS-JAappoI6BUznmgxGOxjF9LohuSCa2Zk_QaYrxu9_Xu3jXDmkjsvYlx6TvyaPbLhpggr7gL_YJN9oSHwC70b08EXZGPzyf8_pt8p1HgzSDRBkdB6rSoxvtLuPPrO1dSaqhllRDoR_bb8MxWhZqaATrynoKpS2ZyDHMX6q327smBcU7c2atCsI7HiMNsvC6AiMS9hEa2b_ASWwNCcvWJ-iaB4uFcxBr8e6J8l9udu56amkNcakGReUOj1rDWYL5j7F35iA1FGFG_ofbX1vfyYO3Wg9U7-W6W8KPtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
بسنت درباره ایران:
متحدان ما در امارات متحده عربی در خصوص این بانک مستقر در دبی همکاری بسیار مؤثری داشتند. اکنون ما برای متوقف کردن تمامی این جریان‌های مالی غیرقانونی، با آن‌ها وارد همکاری شده‌ایم.
ما برای رفع این مشکل با آن‌ها همکاری خواهیم کرد، چرا که بانک‌های متعددی در سیستم مالی آن‌ها فعالیت می‌کنند.
ما نمی‌خواهیم این بانک‌ها را نابود کنیم — هرچند اگر لازم باشد چنین خواهیم کرد — اما اکنون همه کشورها در این مسیر با ما همراه شده‌اند.
این پایان کار برای این رژیم است؛ آن‌ها یا باید [رفتار خود را] عادی‌سازی کنند و یا با عواقب آن روبرو شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71104" target="_blank">📅 18:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71103">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e7eb93ff.mp4?token=S92OCLHwMxB6R2tnTg8Q49YulMAAVZl8vw2bnBzAOJNXu0mkrl6uA67fW9po1YTrqV51hLh2slszWMv0rNlAZoMxUtM9wKb7SyPWK8Fnv3v7NUABcBj2Ofjrv4Eny_9RvZCDGs_-YoXyAhznVOl2JTUFKPpD1c19IFKax5gCqR8WP1cXW6GIPfu4_g-EqrZBQZOUp6-lvvnO6wxVvecpZ5wyfwsy7aAV5TKEmdcmYsT-OPdOsDHTVVIKgUZI6cDLujRBZnrf8QISDr6b718jP0bVOwloFm7dfvd2FJdPWqCS0PNJ-scE1Uqp2sQtxS53a4u3qO86_br2T-5_sWtjVWDOswl4r6BVIKI-6IZ_BWPZBhUMuk5i9URVftKxoyuNm0ttyYj9XLIpR94jm2zQ-CrKLiLk5FPi-EQ2oLHr5_QH5U-jLyJ9fvJdqW9JFVTyJVcoUWewrO0FAnCbQn6HCxFDgw-HxIZ1K0Spho5AmXCxn3zrryqYpFAhO0YZ_Ab4aPjcrQxA-ctO-YhE9VkrmgPHA4yyndZVrTCUbLS7clJRzCvDfTlQ46gJAfpCUTWU7MgEgMrdevUUPLbwB1zZLXZfjrCO3CEVA2H1MhavYeSzPmc0byRgtUC0TB42nwZnwDfnlkF6BUQbi0w-Sk4C3GZjrv_aySSILahIIRJcj-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e7eb93ff.mp4?token=S92OCLHwMxB6R2tnTg8Q49YulMAAVZl8vw2bnBzAOJNXu0mkrl6uA67fW9po1YTrqV51hLh2slszWMv0rNlAZoMxUtM9wKb7SyPWK8Fnv3v7NUABcBj2Ofjrv4Eny_9RvZCDGs_-YoXyAhznVOl2JTUFKPpD1c19IFKax5gCqR8WP1cXW6GIPfu4_g-EqrZBQZOUp6-lvvnO6wxVvecpZ5wyfwsy7aAV5TKEmdcmYsT-OPdOsDHTVVIKgUZI6cDLujRBZnrf8QISDr6b718jP0bVOwloFm7dfvd2FJdPWqCS0PNJ-scE1Uqp2sQtxS53a4u3qO86_br2T-5_sWtjVWDOswl4r6BVIKI-6IZ_BWPZBhUMuk5i9URVftKxoyuNm0ttyYj9XLIpR94jm2zQ-CrKLiLk5FPi-EQ2oLHr5_QH5U-jLyJ9fvJdqW9JFVTyJVcoUWewrO0FAnCbQn6HCxFDgw-HxIZ1K0Spho5AmXCxn3zrryqYpFAhO0YZ_Ab4aPjcrQxA-ctO-YhE9VkrmgPHA4yyndZVrTCUbLS7clJRzCvDfTlQ46gJAfpCUTWU7MgEgMrdevUUPLbwB1zZLXZfjrCO3CEVA2H1MhavYeSzPmc0byRgtUC0TB42nwZnwDfnlkF6BUQbi0w-Sk4C3GZjrv_aySSILahIIRJcj-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
همه خواهان پایان یافتن این وضعیت هستند. ۴۷ سال از عمر این رژیم شرور می‌گذرد و دنیا دیگر از دست آن‌ها به ستوه آمده است.
مردم ایران مردمی عالی هستند؛ اما رژیمی سرکوبگر بر آن‌ها حاکم است.
یا رژیم از درون تغییر خواهد کرد، یا مردم قیام خواهند کرد، و یا باید دید چه پیش می‌آید.
ما آن‌ها را از نظر اقتصادی خفه خواهیم کرد. آن‌ها در وضعیتی قرار دارند که من آن را «آرواره‌های مرگ اقتصادی» می‌نامم.
ارزش پول ملی‌شان در حال فروپاشی است و صادرات نفت آن‌ها به صفر رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71103" target="_blank">📅 18:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71102">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13cf8fb01d.mp4?token=OxhTy1yM9PlKiDhnzTWom3lWc068kx-p56_CfUlEKmPBtj3HUhoUl2yQAAYT1-716ocisQOMLU3ftaODZL8sNTa1y34h3UWWrNfhS8qKzmEZBUYN8LQ4GddIJYFokrzVz4SLy-Y02mo8s2DGfExKS75BQTpZVFrKLVJsAQGqCvDJtNk6i5IOVF04Gmi4ZWnT6oSzokHb6up12RPOE0HIVf9_S9HlX7-t8h0omPhrmxRObBrXPyHS6Y6cQ_B5XF3tpCBpv8LltC8Kc69V4GobH-Ld8q_P3SEjAIH2W_ut7WD5ZdCTfFLNrlyio7eJVgL1LSFVQLmx0EGxMNoEqR6WcjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13cf8fb01d.mp4?token=OxhTy1yM9PlKiDhnzTWom3lWc068kx-p56_CfUlEKmPBtj3HUhoUl2yQAAYT1-716ocisQOMLU3ftaODZL8sNTa1y34h3UWWrNfhS8qKzmEZBUYN8LQ4GddIJYFokrzVz4SLy-Y02mo8s2DGfExKS75BQTpZVFrKLVJsAQGqCvDJtNk6i5IOVF04Gmi4ZWnT6oSzokHb6up12RPOE0HIVf9_S9HlX7-t8h0omPhrmxRObBrXPyHS6Y6cQ_B5XF3tpCBpv8LltC8Kc69V4GobH-Ld8q_P3SEjAIH2W_ut7WD5ZdCTfFLNrlyio7eJVgL1LSFVQLmx0EGxMNoEqR6WcjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
ما بانک دیگری را که با ایران مرتبط است، تحریم کردیم. هفته گذشته، یک بانک مصری را که پنج شعبه در دبی داشت و ۱.۸ میلیارد دلار در اختیار این رژیم قرار داده بود، تحریم کردیم.
امروز بانک دیگری را تحریم خواهیم کرد و احتمالاً هفته آینده نیز بانک دیگری را تحریم می‌کنیم.
ما به سیستم مالی می‌گوییم:
ای عوامل مخرب، ما می‌دانیم شما چه کسانی هستید. خودتان هم می‌دانید چه کسانی هستید. کارتان تمام است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/71102" target="_blank">📅 18:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71101">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
⭕️
🇹🇷
🇮🇷
وزارت خزانه‌داری آمریکا سه نهاد مستقر در ترکیه را به‌دلیل ارتباطات مالی و فعالیت‌های مرتبط با ایران تحریم کرده است:  Golden Global Portföy Yönetimi Golden Global Varlık Kiralama Golden Global Yatırım Bankası
⏺
هم‌زمان یک مجوز عمومی برای دوره جمع‌کردن…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/71101" target="_blank">📅 18:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71100">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
⭕️
🇹🇷
🇮🇷
وزارت خزانه‌داری آمریکا سه نهاد مستقر در ترکیه را به‌دلیل ارتباطات مالی و فعالیت‌های مرتبط با ایران تحریم کرده است:
Golden Global Portföy Yönetimi
Golden Global Varlık Kiralama
Golden Global Yatırım Bankası
⏺
هم‌زمان یک مجوز عمومی برای دوره جمع‌کردن معاملات (wind-down) با این نهادها صادر شده است
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/71100" target="_blank">📅 18:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71099">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372294672d.mp4?token=q8iHCu-d_vu-gvVakUAfSBqIwpZPdIauKN0EXozp9gCFr5IcSNiDS8hgoFOvV9K6OHNVZpD1Sa356P282dEUw4uekkQjih_ocPVNggsyQcH831jlh4ISc38zlUkm10Q3u_-gZ94dog-5e-9MjPeZAABeKLUtaehR_L5mfOSpdCKB-X1FDaVHeecT2cEjQTM-n7kF_cT5UAo-NPI_gO5lo_yTKZIEauA6Kj5DOrJ6wmJuIzToidq8e_vEOmLQK9z_B5qX3XPOW2nKHZmVj5MpaGMdiul6lBQLNx58nQRmoDlroP1ki0glhWiEJnuxb6nYZCdpicMsQMQIIqp7OaXSuFbG4LEMTV5Ft0VVrnOYLVNOfu_6E2Wyb0lo5V12h5BoMwBA8-hJ7kaytIxAOkhKgn2vWzrt9L2AaZpFNprfz6Z7Tllsy2lBt3EuzlHMcvJ_7v09oCEN0b94WiPNw1xDNSfz-YkKRpaqZhKLIYvYnwq9OvczM_YPsp2JkZ-y9ID3QZiEuHf9gUY0TqDIf3mCVbOnjENjCwb7s3fBsE4H9jdufL5P2i732vPy7Ba7LPtz3TqRbd6TjuVfNbgPJ6cwN1IYCVwISjZXJC1eKCvGpxqAPc0WhpUsskErBVV9gdrQWblC_91NiAEeBVh_mDkZ1LaJaDoFVPdVpUS7Z0LhRB4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372294672d.mp4?token=q8iHCu-d_vu-gvVakUAfSBqIwpZPdIauKN0EXozp9gCFr5IcSNiDS8hgoFOvV9K6OHNVZpD1Sa356P282dEUw4uekkQjih_ocPVNggsyQcH831jlh4ISc38zlUkm10Q3u_-gZ94dog-5e-9MjPeZAABeKLUtaehR_L5mfOSpdCKB-X1FDaVHeecT2cEjQTM-n7kF_cT5UAo-NPI_gO5lo_yTKZIEauA6Kj5DOrJ6wmJuIzToidq8e_vEOmLQK9z_B5qX3XPOW2nKHZmVj5MpaGMdiul6lBQLNx58nQRmoDlroP1ki0glhWiEJnuxb6nYZCdpicMsQMQIIqp7OaXSuFbG4LEMTV5Ft0VVrnOYLVNOfu_6E2Wyb0lo5V12h5BoMwBA8-hJ7kaytIxAOkhKgn2vWzrt9L2AaZpFNprfz6Z7Tllsy2lBt3EuzlHMcvJ_7v09oCEN0b94WiPNw1xDNSfz-YkKRpaqZhKLIYvYnwq9OvczM_YPsp2JkZ-y9ID3QZiEuHf9gUY0TqDIf3mCVbOnjENjCwb7s3fBsE4H9jdufL5P2i732vPy7Ba7LPtz3TqRbd6TjuVfNbgPJ6cwN1IYCVwISjZXJC1eKCvGpxqAPc0WhpUsskErBVV9gdrQWblC_91NiAEeBVh_mDkZ1LaJaDoFVPdVpUS7Z0LhRB4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تیزر دوم فصل اول سریال هری پاتر که از کریسمس 2027 قراره پخش بشه
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/71099" target="_blank">📅 18:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71098">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71098" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/71098" target="_blank">📅 18:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71097">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vvr6oMgslXUb7XxTkOscCaffFxsqKavV9H9wls7uNKlo-7_e_T13Yiq3sY22CtuhYSFUGr56M8laV3o6c3xemmrKtVQPrV8Yc80wD3s9S-m7o_edBW0w1YEo_g0jW1UK1TNakgj9bPpXaJJGeJZV-dBg8JedPxkx6AhTcUxHcp-8iOxKFKmVbN2I2EYtXUsYTvVTmWMruixCWUzpmzPRAXYe2a_ld6d1gVDEd6aeS8DBjnVCqO8QE5-q1ym2RqI5RYUyaPFh5IzWpHfRSlSqGVL6mhnqBJrW1Ol-ttecKjbNB3W5uKE_HkLAcIJpRaKfdcF0FCwalJ107BL8vdjPFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
پاری‌سن‌ژرمن
🆚
موناکو
⚽️
را در سایت بین‌المللی
TrexBet
پیش بینی کنید.
📊
مونامو ۲ برد | ۱ تساوی | ۲ شکست | ۹ گل زده
پاریس ۲ برد | ۱ تساوی | ۲ شکست | ۱۰ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/71097" target="_blank">📅 18:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71096">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">〰️
سنت‌کام:
بیش از ۲۶۰۰ تفنگدار دریایی و سرباز نیروی دریایی آمریکا، بر روی ناو جنگی USS Boxer (LHD 4) مستقر هستند و این ناو جنگی در حال حاضر در خاورمیانه در حال انجام ماموریت است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/71096" target="_blank">📅 17:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71095">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fcc841fe5.mp4?token=HoY2VmkIu7bG-56WzyeG92oSLVvbPgvoKiw6eziJT6tub2ly-QPG9k7mHrho3DyznwPS7zLfEQSZnoolaM5arn9LGNih7vzD_d49jFc3QHM8Rb8mgrOEbOiLmyMcyaUt0P-8zznu09h4MwCt-wtDoSNA0N21LQH5S6yOq5BrxVhNqelx0d1kmgFq1raE_hwt3BtKKoLqC2Cj0zCxLdaV8qfSQB2aeLJMfa0k6psXzSYG5c9coi1Ah8CaWxmId1Rt76lJkSkKCjpS3lefW4QlbNL3kJlclKP5iSv7XDUQZiGcISGB-jZwPu6BxnIT3SBRkxXrhO0-AZEHvViWJnN7ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fcc841fe5.mp4?token=HoY2VmkIu7bG-56WzyeG92oSLVvbPgvoKiw6eziJT6tub2ly-QPG9k7mHrho3DyznwPS7zLfEQSZnoolaM5arn9LGNih7vzD_d49jFc3QHM8Rb8mgrOEbOiLmyMcyaUt0P-8zznu09h4MwCt-wtDoSNA0N21LQH5S6yOq5BrxVhNqelx0d1kmgFq1raE_hwt3BtKKoLqC2Cj0zCxLdaV8qfSQB2aeLJMfa0k6psXzSYG5c9coi1Ah8CaWxmId1Rt76lJkSkKCjpS3lefW4QlbNL3kJlclKP5iSv7XDUQZiGcISGB-jZwPu6BxnIT3SBRkxXrhO0-AZEHvViWJnN7ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ببینید از خانمی که داره از تجربیات رفتن خودش به تور کویر میگه...
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71095" target="_blank">📅 17:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71094">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf229661bf.mp4?token=ZljWjFMjZJgEB1fKBQqhh7qJjfScYvg1j0WJYWj9pDimo2XaWRoH5Hk0rgm9RFX6z7u_cDWGxuPUJYihTIfIC5gU_rmNpQQJUyA6yhAIYy9PxJSeQYrKv_zwl8l6q0bs2pmgHniqp6goDy9zSPb5YB2Mu447wMuCWsETuI1ngC1dzW90KtHryLnJITtG3M-EKRwRx9f-XAQ3DQsjZLXA3uMUEHsUOe80ZRq9TbRwpOuy6c5h0YBA0FT5xzukZr52SD7syV0ItzgLGEkX0ZPabhDsuXI6Us1X0lgXV4zRDFJIuz7jk14LSRkWh0hyJfRSrrrDLBVEAbwu_uJXQUpmVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf229661bf.mp4?token=ZljWjFMjZJgEB1fKBQqhh7qJjfScYvg1j0WJYWj9pDimo2XaWRoH5Hk0rgm9RFX6z7u_cDWGxuPUJYihTIfIC5gU_rmNpQQJUyA6yhAIYy9PxJSeQYrKv_zwl8l6q0bs2pmgHniqp6goDy9zSPb5YB2Mu447wMuCWsETuI1ngC1dzW90KtHryLnJITtG3M-EKRwRx9f-XAQ3DQsjZLXA3uMUEHsUOe80ZRq9TbRwpOuy6c5h0YBA0FT5xzukZr52SD7syV0ItzgLGEkX0ZPabhDsuXI6Us1X0lgXV4zRDFJIuz7jk14LSRkWh0hyJfRSrrrDLBVEAbwu_uJXQUpmVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
سامسونگ A17 که یکی از ضعیف‌ترین و تخمی‌ترین‌ گوشی‌های بازار به حساب میاد، قیمتش به 100 میلیون تومن رسیده.
البته این قیمت واسه دیروزه و امروز احتمالا گرونتر شده.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71094" target="_blank">📅 16:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71093">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc7b61838f.mp4?token=m3JaoJQg5pj53Jl9vuL-S9_ZuZgnDO6i09BqBP6K5aaOYej5ejNDl3fHhbOkLv2TkEpR--1W4o7F0yEbu1qkGiG1sqYXUZZaOFZQI1VfZFRDQX0rykG1A7ls4UKsABppU7N0R2lU46lYOahtzwo3VxV4ASut-p0yG4_MTKtCtBi8iyHNX4owoa8eVd4q2TMspD5QGlvaAg1odwrbKVRNIpGGZSirovD-UnE6gz4MBE09Y6FVKTrTTwvvapVsPGd2fboHd3C56yeV60BrLMr8z0jXUjEUznbqEuB3AreRn2DQPe8yd2esP7f6bDCtspNuH289s3EmQn4RzN628kgSCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc7b61838f.mp4?token=m3JaoJQg5pj53Jl9vuL-S9_ZuZgnDO6i09BqBP6K5aaOYej5ejNDl3fHhbOkLv2TkEpR--1W4o7F0yEbu1qkGiG1sqYXUZZaOFZQI1VfZFRDQX0rykG1A7ls4UKsABppU7N0R2lU46lYOahtzwo3VxV4ASut-p0yG4_MTKtCtBi8iyHNX4owoa8eVd4q2TMspD5QGlvaAg1odwrbKVRNIpGGZSirovD-UnE6gz4MBE09Y6FVKTrTTwvvapVsPGd2fboHd3C56yeV60BrLMr8z0jXUjEUznbqEuB3AreRn2DQPe8yd2esP7f6bDCtspNuH289s3EmQn4RzN628kgSCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یک راننده کامیون:
الان کنار مرز پاکستان هستیم میخوایم رد بشیم اجازه نمیدن.
رفتیم پیش رئیس گمرک میگه طرف پاکستانی اجازه ورود نمیده.
پاکستان گفته به ازای هر ماشین باید دو میلیارد تعرفه بدین.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71093" target="_blank">📅 16:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71092">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45bdb5a184.mp4?token=Zto5xFimVJtZRFIH3Jo07xOAktW3e839kBIz_TrKSvYv9uIWC4rTObIEPSiYznpqR8OaIpcLGmO3am3smgmq1gZntfLpPT-RS0VeWeg4O6H4vVaO-ek-MF-VFAK4tlYsZiBgoi2puLC68AHXvfeuWpZ8Oa-lfKKhmiFZraFn1zAaX78rMtRvWwyNjQLC7f4ndTBxgbdwizDNsvMFUCcVKC5VrpgwEZ5qItJHjJI3WdgApVl1cPSmvrzqb61qkv2KktyS3RwBgJh1DxL8rl4qBtmXBpX5iobqOSvhBpMRpU66fPqUAsaLfzIxYl83-IfzTbPKleoey8ayvcq5o9GOsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45bdb5a184.mp4?token=Zto5xFimVJtZRFIH3Jo07xOAktW3e839kBIz_TrKSvYv9uIWC4rTObIEPSiYznpqR8OaIpcLGmO3am3smgmq1gZntfLpPT-RS0VeWeg4O6H4vVaO-ek-MF-VFAK4tlYsZiBgoi2puLC68AHXvfeuWpZ8Oa-lfKKhmiFZraFn1zAaX78rMtRvWwyNjQLC7f4ndTBxgbdwizDNsvMFUCcVKC5VrpgwEZ5qItJHjJI3WdgApVl1cPSmvrzqb61qkv2KktyS3RwBgJh1DxL8rl4qBtmXBpX5iobqOSvhBpMRpU66fPqUAsaLfzIxYl83-IfzTbPKleoey8ayvcq5o9GOsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه دختر حامی حکومت:
فک کردین اومدم از قیمت دلار آه و ناله کنم؟ نه اومدم پاره‌اش کنم!
رزق و روزی دست خداست نه آمریکا، دلار قیمتش عوض شده، خدای ما که عوض نشده.
قیمت دلار هر چقدرم بشه، باز روزی مارو خدا می‌رسونه، منم اعتراض دارم ولی ناامیدی تزریق نمی کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71092" target="_blank">📅 15:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71091">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2be4c50b6.mp4?token=Mcqm1BY8A87LAm3G3VfkJJxUu7rhFnHYZlLcOJDxtQYbMfLTxuS7FAtbBAmcNhZX-Xo8Nec0kTAkNwPaD2RgTB-riL5Y0KG_MDak9pBwLWmL7Hg4TceB9ofJHGWd0Uq4nYIF4xqOv7fx-_w0ijbcM3iti7b-obUZxHcPRlC8hVK1TjxgBBa0-ZkKx3bCmvIjCNSRIpR0JuVl8M166zk96PDGarjpmlc6JcEu4goRDimeVvVvsMBNtp_JvYg4GEeIxrcoYNaV5d69QMIqf5BhwtNH2YS5j9GAL9Ikg7T2ZColY7Megp37lvW9nzTT2N-lge-i23jzNQb9BOGSG6ep8TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2be4c50b6.mp4?token=Mcqm1BY8A87LAm3G3VfkJJxUu7rhFnHYZlLcOJDxtQYbMfLTxuS7FAtbBAmcNhZX-Xo8Nec0kTAkNwPaD2RgTB-riL5Y0KG_MDak9pBwLWmL7Hg4TceB9ofJHGWd0Uq4nYIF4xqOv7fx-_w0ijbcM3iti7b-obUZxHcPRlC8hVK1TjxgBBa0-ZkKx3bCmvIjCNSRIpR0JuVl8M166zk96PDGarjpmlc6JcEu4goRDimeVvVvsMBNtp_JvYg4GEeIxrcoYNaV5d69QMIqf5BhwtNH2YS5j9GAL9Ikg7T2ZColY7Megp37lvW9nzTT2N-lge-i23jzNQb9BOGSG6ep8TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🚀
🇰🇼
روز گذشته، یک پهپاد انتحاری که توسط ارتش جمهوری اسلامی پرتاب شده بود، یکی از واحدهای برج مسکونی الدیره در شهر کویت را هدف قرار داد. این اصابت باعث آتش‌ سوزی و تخریب کامل آن واحد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71091" target="_blank">📅 14:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71090">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a0b6b730d.mp4?token=aSr_drfDtyuX4YbN1fewDea1kIx1Nko6BD_rT4GCN6Fw5B_FviBkvWHCR7kcWg9HkCuxp-DlYEdUWWNFZTUuerIAycrmD_2Z0k5l_mBTyxEyPZUXgUPOLTBGbQGxOhkszlPrh7c6xEXVK9UcE32SNXjKJF5buZcjMfuy3a3nT2uigQb-BU7akKqbaA7H4c-K3BNKrjqYCxsMCX2qIb-hJe0kIZMn8aklDFckJWKVYu2u_xeOOiXdtsK1ni6T46c_VhRNWekyEZlThqyqi53c3T2dtSLJRXAkMlRzK3pw6q_1QLQEt4vhUxExxgfd5nmyAGHCw4R_eltR0moAVX10Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a0b6b730d.mp4?token=aSr_drfDtyuX4YbN1fewDea1kIx1Nko6BD_rT4GCN6Fw5B_FviBkvWHCR7kcWg9HkCuxp-DlYEdUWWNFZTUuerIAycrmD_2Z0k5l_mBTyxEyPZUXgUPOLTBGbQGxOhkszlPrh7c6xEXVK9UcE32SNXjKJF5buZcjMfuy3a3nT2uigQb-BU7akKqbaA7H4c-K3BNKrjqYCxsMCX2qIb-hJe0kIZMn8aklDFckJWKVYu2u_xeOOiXdtsK1ni6T46c_VhRNWekyEZlThqyqi53c3T2dtSLJRXAkMlRzK3pw6q_1QLQEt4vhUxExxgfd5nmyAGHCw4R_eltR0moAVX10Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
❌
🇦🇪
با افزایش تحریم‌های آمریکا تجار و بازرگانان می‌گویند امارات از بارگیری لنج‌های ایرانی خودداری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71090" target="_blank">📅 14:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71089">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28ac9cc9fe.mp4?token=b0x04bmp4m8Z1eqhqZYkbUaNml6Mxl55jzZrCyRt1RP_pjgnPSUxZ9bNM4w9MDzC8AfSHyb4TniEjAxJbmTMxRrKRI7xFaGLhNHdTcfrl3WSGUYA-yM7y47Bx4jPxg77gazXhMJxpft1fzV0ihH8eV_V54tG3xpt1vghQnnorvv9qOJW6n3u806fofjt1ROfqSxLx1xy1Xhuzwmde8Sdl0sUQ-GmRBvwoGceiod6i02jHAxeHvRTGpV0cPqaxo5qOPy7DJU7ew2vfva8qiAA2IT3r1cMrglc1nBraQ7ehdnu52N98WguVDA5kXv9Hr_-Bpe1WNDwy_6qxGILHIX1RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28ac9cc9fe.mp4?token=b0x04bmp4m8Z1eqhqZYkbUaNml6Mxl55jzZrCyRt1RP_pjgnPSUxZ9bNM4w9MDzC8AfSHyb4TniEjAxJbmTMxRrKRI7xFaGLhNHdTcfrl3WSGUYA-yM7y47Bx4jPxg77gazXhMJxpft1fzV0ihH8eV_V54tG3xpt1vghQnnorvv9qOJW6n3u806fofjt1ROfqSxLx1xy1Xhuzwmde8Sdl0sUQ-GmRBvwoGceiod6i02jHAxeHvRTGpV0cPqaxo5qOPy7DJU7ew2vfva8qiAA2IT3r1cMrglc1nBraQ7ehdnu52N98WguVDA5kXv9Hr_-Bpe1WNDwy_6qxGILHIX1RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇱
🚂
برخورد قطار با یک کامیون در گذرگاه راه‌آهن در گدانسک لهستان.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71089" target="_blank">📅 13:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71088">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b60a6b68b8.mp4?token=jLYEMFsMuse95PU43lQhJctRszPYbIeAJIq5wzj9_hzZwriRA5-K1Gx6xXjrlzKB6f66QpLpIccWqM7N7nZLgkh5TDPWTmW8hmOK4sxOb4eLDcpl0TwAPktqLmjSHrUev_5I1TlikQFfyc3iYkx3t7FR_J0Oy9mVIV-KcBGljXFpMOgwnWj33vHQPJ4i3qT1HnIf0s-Xc5cxQFUCL7cpXNdChdqe3gTNIyFzqoD_VVl_i7JgHL-GMG9N5R-eJ9U8Sat-w4_vWBBZg4fsr5vdG1bV0s_OEJaYsNv7Dj8aBG9cqa5dq6jv-rIq9a2AAmKeQ75d01l8FT8JB-AGgWwVFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b60a6b68b8.mp4?token=jLYEMFsMuse95PU43lQhJctRszPYbIeAJIq5wzj9_hzZwriRA5-K1Gx6xXjrlzKB6f66QpLpIccWqM7N7nZLgkh5TDPWTmW8hmOK4sxOb4eLDcpl0TwAPktqLmjSHrUev_5I1TlikQFfyc3iYkx3t7FR_J0Oy9mVIV-KcBGljXFpMOgwnWj33vHQPJ4i3qT1HnIf0s-Xc5cxQFUCL7cpXNdChdqe3gTNIyFzqoD_VVl_i7JgHL-GMG9N5R-eJ9U8Sat-w4_vWBBZg4fsr5vdG1bV0s_OEJaYsNv7Dj8aBG9cqa5dq6jv-rIq9a2AAmKeQ75d01l8FT8JB-AGgWwVFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف با رفیقش رفته دور دور الهیه و به یه دختره شماره دادن،
و حالا اولین پیامی که دختره براشون فرستاده
😟
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71088" target="_blank">📅 13:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71087">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71087" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71087" target="_blank">📅 13:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71086">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFwY3ftK1H_R5d8xSc3Em0s24auOwrNDq44QapJ4zHZLw-7HyECbXB-uSMWFZUNL89kgf5kvWgE6Baa7xLXv9POBRHXK0pSs6OABLgpM10mIgDjDJ2r5vjA025Jx0qSJy-3TX-KZJt2LTE79MgOVmcHw5xQW9g_thncOywjYCBK7rz_EZ6nZnxipfH-VdZaCOkr1kH1uuJZPsTLOKFwDNrvh6jc6E8SKVfYbqQoTxcjy6rdeJRxPDhrm3E1HRsjSJBB54_RU4qo6H8FaLMz5Ew7mhHRZ1o_x1hvnZvBwDuaODP1xhk5bu0nXRmX0jkIlx2HpHv_Dc8OWe0iaARy9CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب رئال بتیس
🆚
رئال مادرید را در سایت بین المللی
TrexBet
پیش بینی کنید
📊
نگاهی به آمار دو تیم در ۵ بازی اخیر
رئال بتیس: ۲ برد، ۱ تساوی، ۲ شکست در ۵ بازی
رئال مادرید: ۵ برد در ۵ بازی اخیر
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71086" target="_blank">📅 13:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71085">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4843999275.mp4?token=Gr902Y1AKpgY9KOgzrW_FnCMx-KMjftGOzSCy-8ih2RD36mS5RrmOpd896T4H_9yfKApowpKHnoVTpVmzWAxg9RhVcotW5qUlfhOcqaa6XUh7Kqt0qtmkxXLfojVkshlNIh08niaEFo5R7aG3IHmRJUyEBtjztBGbYyh1X-yrPkzJz5Lyh4JCKHrRh2H5TvFbaCLPFjR2mz9UAwiRqcJ84jReG9QbqI67qx1fXGmWXskeg-nteIhO0VPZQ33hwHTnXpj2dKBq0uiYN_SzdbKLLzHUiQ0KLODUWzW9ZP5XiZlFmpvVKA8ZdlYrvr3pZQBbfNGQVYdJPxu6FI-v2mpuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4843999275.mp4?token=Gr902Y1AKpgY9KOgzrW_FnCMx-KMjftGOzSCy-8ih2RD36mS5RrmOpd896T4H_9yfKApowpKHnoVTpVmzWAxg9RhVcotW5qUlfhOcqaa6XUh7Kqt0qtmkxXLfojVkshlNIh08niaEFo5R7aG3IHmRJUyEBtjztBGbYyh1X-yrPkzJz5Lyh4JCKHrRh2H5TvFbaCLPFjR2mz9UAwiRqcJ84jReG9QbqI67qx1fXGmWXskeg-nteIhO0VPZQ33hwHTnXpj2dKBq0uiYN_SzdbKLLzHUiQ0KLODUWzW9ZP5XiZlFmpvVKA8ZdlYrvr3pZQBbfNGQVYdJPxu6FI-v2mpuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
پرزیدنت ترامپ در رسانه‌های اجتماعی پرسید: «مردم ایران کی قیام می‌کنند و می‌جنگند؟» آیا دولت در حال بررسی مسلح کردن یا ارائه، سایر حمایت‌های مستقیم از مخالفان ایرانی است؟
🇺🇸
ونس:
ها ها ها... مگر پیتر دوسی امروز صبح این سوال را در فاکس نیوز نپرسید؟
سوال خیلی خوبی است.
و چیزی که رئیس جمهور گفت(درجواب به این سوال) دقیقاً همان چیزی است که من می‌خواهم بگویم.
قرار نیست درمورد این سوال صحبت کنم!
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71085" target="_blank">📅 13:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71084">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IQ6y9Co5kf_pkFfLMf4KyGoOs3JGbh0YGo1vR3IRHG1w8X8cRXvXtkcQQITt-vjDYwLMYZjuLHgQ90Z6Aea3_OghsZWGeFIYoWt_o1jSNVTncfBturrfabeUKhVCtdH6kA3u3rFFI5uS9rdk4o3zco4IEz0R6GODRqnM5bIxLAYYbIDpwCIXvwLDipn2tjFya9TwNIJYUD7mJjfnYy2Sr0MunHzCnq1wuMgrC0BmNYfUvzfsH9aJgteZ4cAycqq_nebOnuXuvtWGxorA8qfiY1G6_LEkLKUb0oe49sFfh0WHMLPDM0opPpQ_dZGxmMpd2SxCFa29LfCoAoanM1yY-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرزشی با این پست به شدت میسوزه
😃
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71084" target="_blank">📅 12:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71083">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0edd50344.mp4?token=n4IQYkMJFhjFZmo5TQP8lhyqnxA_k3tWVihR46gJX-6hVWwJJ6RJ-yT_V8m8XwB1vDLty_vjDtGYkcS3XcpRCcJR_EjtS8CrsZa6PQV93CNCnKmn-XzUdxjXkKxb0HknpSjwN89kprOFt654jwdGd5yB8TWmHuevbJ57NRSeVlNJid1fPnqUTyracfOP2vGjsB7sBz2886bnqAGWy3Ao6PnkjwZut29fqc-qiHIcxFWmHl06Or2PhgK3Py8-pUb90rW6UIEGhGB2AIsOZyJG5UjzdDE6K3d68rfhngepVMnlGrhr_yIie5jDoEoRDDnsLUxKhVgRyU62usw-Qo4XNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0edd50344.mp4?token=n4IQYkMJFhjFZmo5TQP8lhyqnxA_k3tWVihR46gJX-6hVWwJJ6RJ-yT_V8m8XwB1vDLty_vjDtGYkcS3XcpRCcJR_EjtS8CrsZa6PQV93CNCnKmn-XzUdxjXkKxb0HknpSjwN89kprOFt654jwdGd5yB8TWmHuevbJ57NRSeVlNJid1fPnqUTyracfOP2vGjsB7sBz2886bnqAGWy3Ao6PnkjwZut29fqc-qiHIcxFWmHl06Or2PhgK3Py8-pUb90rW6UIEGhGB2AIsOZyJG5UjzdDE6K3d68rfhngepVMnlGrhr_yIie5jDoEoRDDnsLUxKhVgRyU62usw-Qo4XNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو وایرال شده از طرفدار حکومت
🎙
خبرنگار:
از قیمت دلار خبر داری ؟
🇮🇷
طرفدار حکومت:
بله شده 200 و خورده ای
🎙
خبرنگار:
با این قیمت پس چرا اومدی اجتماعات ؟
🇮🇷
طرفدار حکومت:
دیگه باید قدرت تفکیک داشته باشید تو ذهنتون و قیمت دلار یه چیزه و بیرون اومدن یه چیز
اصلا اگه امنیت ما نباشه شما میتونید راجب قیمت دلار فکر بکنید؟ نه نمیتونید!
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71083" target="_blank">📅 12:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71082">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">⏺
ویدیو وایرال شده از اعتراض یه زن کارتون خواب:
به عنوان یک کارتون خواب که 20 ساله دارم این زندگی تجربه میکنم!
شما مسئولین که مردان خدا هستید شما دیگه چرا؟
تو دانشگاه رشته حقوق خوندم
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71082" target="_blank">📅 11:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71081">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18ffbfe89.mp4?token=FaaPxyaAk3FRBRUI2o3kXWTYxiDrqwXV1UJMuzLxXXrfqpazC31wm1CLUHI2Mhn3gnpgDTqx0SMriF5I0t18AXb7pQltpuZAU1MxNmWzooTpNTSbMigkOMCvzaydg8TqbsKz9urgx_6sxAF8bS7uaonoIWX2IfSt7ZUFvNd-wAmrkFh12JqHtZNRCPOu-U1bK86wlfA8IByF-G6RxUWijxR-MWRrJEV-yycdSauzDi9hW1eRoYkOpZ27zM77NfqH1HZrSXXd9R3VukiD3LHriCvcM2_oSnOnQhpQuT_58HtwE6bpcmwKf4odOfgs58tS9Evk_KJRHpCpuGLlDt1N5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18ffbfe89.mp4?token=FaaPxyaAk3FRBRUI2o3kXWTYxiDrqwXV1UJMuzLxXXrfqpazC31wm1CLUHI2Mhn3gnpgDTqx0SMriF5I0t18AXb7pQltpuZAU1MxNmWzooTpNTSbMigkOMCvzaydg8TqbsKz9urgx_6sxAF8bS7uaonoIWX2IfSt7ZUFvNd-wAmrkFh12JqHtZNRCPOu-U1bK86wlfA8IByF-G6RxUWijxR-MWRrJEV-yycdSauzDi9hW1eRoYkOpZ27zM77NfqH1HZrSXXd9R3VukiD3LHriCvcM2_oSnOnQhpQuT_58HtwE6bpcmwKf4odOfgs58tS9Evk_KJRHpCpuGLlDt1N5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پسره دوست دخترشو برده تو کوچه پس کوچه ها بهش رانندگی یاد بده
آخرش هردو غافلگیر شدن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71081" target="_blank">📅 11:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71078">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bc34fe3de.mp4?token=YyoVO1P2GtH24jESJVaaIy_eP9tnr3CWrCOWCDK9PuzaZebUFpInYS5VGe6PgAe6IbySFK4eFRYDP2hd4q-vOf3QKMM-JD9sBBpP_GTYphCLsB9cctUv7Hm2sRW3wzS_kiqyeIudzFBXVKXn7H2Kzzk7LzLURewQe6p5CjwrVxP5V1qPsk4zeTO7UH0KY-CHYtKuXD-o-ufQx0rjQeHXRSBvmQ-8qZSROzvVGC0CuVCmhKRlHpeAKTAIo-ekGCcGYJkU8WaF2K72ul00gdYpZLqxVhvV7xkfuBZjbN5YJhlDm-_e2YsFt8SUAZ5wH5CXxj2T820Wxs3o50m5tK_N-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bc34fe3de.mp4?token=YyoVO1P2GtH24jESJVaaIy_eP9tnr3CWrCOWCDK9PuzaZebUFpInYS5VGe6PgAe6IbySFK4eFRYDP2hd4q-vOf3QKMM-JD9sBBpP_GTYphCLsB9cctUv7Hm2sRW3wzS_kiqyeIudzFBXVKXn7H2Kzzk7LzLURewQe6p5CjwrVxP5V1qPsk4zeTO7UH0KY-CHYtKuXD-o-ufQx0rjQeHXRSBvmQ-8qZSROzvVGC0CuVCmhKRlHpeAKTAIo-ekGCcGYJkU8WaF2K72ul00gdYpZLqxVhvV7xkfuBZjbN5YJhlDm-_e2YsFt8SUAZ5wH5CXxj2T820Wxs3o50m5tK_N-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
توی دزفول چند تا دزد میرن توی یه خونه مجهز به وسایل ضد سرقت و 3 کیلو طلایی که توی اون خونه بوده و قاحب‌خونه قصد داشته باهاش طلا فروشی بزنه رو میدزدن!
صاحب خونه شب قبلش توی اینستاگرام گفته بوده که میخواد طلا فروشی راه بندازه که این حرفا رسیده به گوش دزدا ؛
فردای همون روزی که این حرف رو زده وقتی صاحب خونه خانومش که باردار بوده رو وقتی میبره بیرون یه هوایی بخوره دزدا میریزن تو خونه و طلا ها رو میبرن.
حالا صاحب خونه گفته که هرکسی هر سرنخی از این دزدا داشته باشه و بهم بده ، 10 میلیارد تومن بهش پاداش میدم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71078" target="_blank">📅 10:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71077">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0def551e36.mp4?token=V6RnHP5wpked8QWEnvRCkCkkA8FBcHianBdLu53zX3gZS5woaP0WQmAsEPRyN_zvLiAupQMctJAO6vYTAVCKBD6r_EXsRoEUJolCpa4hBvp7ksiPC3BpvJuXLHdGRybJv8_ksSVuxI8Btp46jKUjKDb1iKCqKkaiNuN3Wz8IzTp9KcMaMshkAJGjDs7JC6I4fu4OTFleG1MCoG3le5EbasPNKUmyphcrkBw0YlN_-ktaMcvvPpxPg2f4dSqWimRaO3FQ5feWkiJj4ZkJLtaBVToul3xU22ApOvnrD5wbIdgNLU5KDhyIe2Gg3c4GaD8SrZgfe0OSio7OoGjFq5BhHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0def551e36.mp4?token=V6RnHP5wpked8QWEnvRCkCkkA8FBcHianBdLu53zX3gZS5woaP0WQmAsEPRyN_zvLiAupQMctJAO6vYTAVCKBD6r_EXsRoEUJolCpa4hBvp7ksiPC3BpvJuXLHdGRybJv8_ksSVuxI8Btp46jKUjKDb1iKCqKkaiNuN3Wz8IzTp9KcMaMshkAJGjDs7JC6I4fu4OTFleG1MCoG3le5EbasPNKUmyphcrkBw0YlN_-ktaMcvvPpxPg2f4dSqWimRaO3FQ5feWkiJj4ZkJLtaBVToul3xU22ApOvnrD5wbIdgNLU5KDhyIe2Gg3c4GaD8SrZgfe0OSio7OoGjFq5BhHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز یه دختره داشت تو قزوين واسه خودش قدم میزد؛
که یهو یه پیرمرده خواست مزاحمش بشه ولی بعد که فهمید طرف پسر نیست، عذرخواهی کرد و رفت
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71077" target="_blank">📅 10:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71076">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4ba13b0e17.mp4?token=CByrzygJ4u5E7SiR6f-o36EE0OqYiK2wwHfwif7aXmG-O4J2EXTiCl1D4SCuO3bHm3669w4oxBhxxKvN8HwOKYEn3sCnbKr3EPEfHUyEccXqmZSDEFlFexA9NhqlgXC2EhnxMH8WiNF5i1LfF2wn5pCuI7OSCrwCSBEz7pOagz0rH7_CIN_kN6IGNuBAFt_iu1hGqqs7bDP3TRQwDOm_aLS1dpzaSyKMby8DVnwUBYJUYSB9owuTVdI3FJbgU8wuUVHVNwAc8YaDxOOGWN3hqGN2HKi7PA3bOo6X41R4LoqoZqHt84z5dSMUsFhNwy72-dFZVjfoJeplFi11S9xykA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4ba13b0e17.mp4?token=CByrzygJ4u5E7SiR6f-o36EE0OqYiK2wwHfwif7aXmG-O4J2EXTiCl1D4SCuO3bHm3669w4oxBhxxKvN8HwOKYEn3sCnbKr3EPEfHUyEccXqmZSDEFlFexA9NhqlgXC2EhnxMH8WiNF5i1LfF2wn5pCuI7OSCrwCSBEz7pOagz0rH7_CIN_kN6IGNuBAFt_iu1hGqqs7bDP3TRQwDOm_aLS1dpzaSyKMby8DVnwUBYJUYSB9owuTVdI3FJbgU8wuUVHVNwAc8YaDxOOGWN3hqGN2HKi7PA3bOo6X41R4LoqoZqHt84z5dSMUsFhNwy72-dFZVjfoJeplFi11S9xykA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه دستگیری یه قاتل فراری در ایرانه
:
قاتل با چاقو مامورا رو میزنه و داشت فرار میکرد که یکی از مامورا عین راموس تکل زد و طرف افتاد.
بعدش یکی دیگه از مامورا ویلچر برداشت و میکوبید تو سر و بدن قاتل تا بیفته زمین، هر لحظه این فیلم عجیب‌تر میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71076" target="_blank">📅 09:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71075">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAGmCb9KrFAy8vmyjxqnW0h66cW2MT5Oz8dAqsKbYVGYksFTcwW_BqFQ6OPIrfP0eFPYW5YkokLb_Lumr4vSz8ByLj3MO7yg673ayponkyTvnUb4ygJNu0gpIf5zedERX3p1epT5i8W-pYF2U6qWBI8HrHnuhibdFZ-1TU26bOV5OtRCkXacvnWJ-B9ku_0InDBph3tCV-_MNQVCfweeXtBAeKkeP2hgcxcbYVoG1aMQxpOisDdfqh4lBLxtwllfzmuJQeeWfCw0Q5xguWbmIVDFHgDCxWmXx0vILC_DbZJ4vXYevt9xq_OnqAnJck07DWG9lbi2uSH7UqtDDgN1ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
⭕️
#فوری
؛اسکات بسنت وزیر خزانه‌داری آمریکا:
اتحادیه اروپا رسماً به «عملیات طرد اقتصادی» (Operation Economic Outcast) پیوسته است و ما از موضع قاطع و زودهنگام آن‌ها قدردانی می‌کنیم.
ایالات متحده در کنار متحدان خود قاطعانه ایستاده است تا اطمینان حاصل کند که رژیم جنایتکار ایران نمی‌تواند از سیستم مالی جهانی برای تأمین مالی جاه‌طلبی‌های هسته‌ای، برنامه‌های تسلیحاتی و نیروهای نیابتی تروریستی خود بهره‌برداری کند.
جهان پیام روشنی به رژیم ایران می‌فرستد: ما تا زمانی که آخرین شریان حیاتی مالی باقی‌مانده قطع نشود، از تلاش دست نخواهیم کشید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71075" target="_blank">📅 09:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71074">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71074" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71074" target="_blank">📅 01:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71073">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OChWvb539HNlx6FuTlbEAtdPhEIgd8CCbWlh42_OXoGgTOIqhYLS2pEPl5a2xsRn0Q0tjngnBNRp8H_4UtrSOcdx7qU3Ya-GcTudLbUkAl_jW7FrjElvKwu4JdyfjWj43mTluyM2Vjf2QhtLcBQgRVNXLhvsJgCDbjaonJofbPY1-zUUx7dqe5Ma0tGLRcg1PMCNl1yvC2LrgM0dehmbxlTYWt9OVbiAMo4rpdbn40MrVMqIm7rxng59ipM7WXGOzpyT_ubxHR9pgtsS2OdQUH7B7hG1_awpqnK5YCEpEZBv1QXcDakQOmFMFTScRQg6BbQ43Ncri5ptIlGy-m2t0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71073" target="_blank">📅 01:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71072">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🇮🇷
نایا:ایران چندین موشک به سمت کشتی ها در تنگه هرمز شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71072" target="_blank">📅 01:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71071">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c46c090035.mp4?token=Dg5XZODUq76AGY8a2og2L80kXPddXNZLUBpEUFF7erwk-PV__sYsHpr5DHlPL24DjH5-TfzoB6TnH4GKjBIZxRy0yy_VjgYycHeJt_wgyjBCYQwoG1nNz_ulXd9Hit1npdqZ3LYgXSWV9E7Gm6oVJxCA4oWz2HDFNijg__1QPCXZug_iFqWHcSwNrcWNe-ZipjHX2Ijpnsnmouj98ZRQk_lUhs49JG6-ehHpnTiUsoURnh9mG7ocfzsTD0w8el0U8ap47HhYfWpM-AnbLMmcU2X4wo2-q5S6njJ3WUA9gViFLb8AxwjZL5dqsV5GWxy_5qCsi6W5SnKfRTOyWzySCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c46c090035.mp4?token=Dg5XZODUq76AGY8a2og2L80kXPddXNZLUBpEUFF7erwk-PV__sYsHpr5DHlPL24DjH5-TfzoB6TnH4GKjBIZxRy0yy_VjgYycHeJt_wgyjBCYQwoG1nNz_ulXd9Hit1npdqZ3LYgXSWV9E7Gm6oVJxCA4oWz2HDFNijg__1QPCXZug_iFqWHcSwNrcWNe-ZipjHX2Ijpnsnmouj98ZRQk_lUhs49JG6-ehHpnTiUsoURnh9mG7ocfzsTD0w8el0U8ap47HhYfWpM-AnbLMmcU2X4wo2-q5S6njJ3WUA9gViFLb8AxwjZL5dqsV5GWxy_5qCsi6W5SnKfRTOyWzySCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پورمحمدی:
انسداد تنگه هرمز، برنامه‌ریزی شهید پاکپور بود.
شهید پاکپور پیش‌بینی کرده بود که جنگ با ترور او شروع می‌شود.
شهید پاکپور برنامه‌ریزی کرده بود که اگر جنگ آغاز شد و او دستوری صادر نکرد، فرماندهان ۲۰ دقیقه بعد شلیک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71071" target="_blank">📅 00:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71070">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46300e7107.mp4?token=KQM9A3GNIaPmTWsNRoAyDxWvShdkqCJPGnP5rZJXegQECHHKSFuaigbSGCwwWpO1B7VCP-e3TJAVZk0RXrBzQ_5-sPRpRz9ZIrAz4qPAo4mEqkZPkJPRLKOv_8ZWEQmSFetWKv4JfL3KcddgIEob5jfnByersn-ld1_xrjekPZZ0Nanu8y0VooYCl7x-5chB2VngsZ3dJypn0DyNeGfEQYwwMhajL5H4-RSguMDlTkAnd7bsaF4B1AcUzS4p6cJ9_SoFb_KmZgyi92NkIOPOdY3gQGwfP4u-XVaMuqogKz4nSwcGAUcmWjb1P124s41YwoTc8YFBl_NYkeIdnpzQYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46300e7107.mp4?token=KQM9A3GNIaPmTWsNRoAyDxWvShdkqCJPGnP5rZJXegQECHHKSFuaigbSGCwwWpO1B7VCP-e3TJAVZk0RXrBzQ_5-sPRpRz9ZIrAz4qPAo4mEqkZPkJPRLKOv_8ZWEQmSFetWKv4JfL3KcddgIEob5jfnByersn-ld1_xrjekPZZ0Nanu8y0VooYCl7x-5chB2VngsZ3dJypn0DyNeGfEQYwwMhajL5H4-RSguMDlTkAnd7bsaF4B1AcUzS4p6cJ9_SoFb_KmZgyi92NkIOPOdY3gQGwfP4u-XVaMuqogKz4nSwcGAUcmWjb1P124s41YwoTc8YFBl_NYkeIdnpzQYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
چندشب پیش تو شیراز یه دعوای عجیب رخ داد؛
دوتا دختر با ماشین میزنن به ماشینِ دوتا پسر؛ بعد گفتن ما مقصر نيستيم و داشتن فرار میکردن!
پسرها هم گفتن چون بی‌ادبی کردی، باید بمونی خسارت بدی، بخاطر همین پریدن رو کاپوت ماشینِ دختره که فرار نکنه!
این وسط یه پیرمرده هم خیلی بی‌دلیل از دختره کتک خورد...
تهشم دختره گفت دیگه این موضوع واسم مهم نیست چون زنگ زدم شوهرم سروان شهریزی، الان میاد کون همه‌تون رو پاره میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/71070" target="_blank">📅 23:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71069">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/876466a913.mp4?token=oq56lDWkhzSk0tzeFMqEQYzet1cdY9fkybUEaZ2zAg5cbGAZFyjeDskN0Up3yawXYSPtzduBJ6kzwsh2hPdhgLx0B8QOeaUY1YBtk9GPyNxltTyZGdiJirDxMYVK1xc_LWouj9hL8Te81L25GVC_U6fN7MiraDsuMJAgW7RLH_UVOdrcEVkFmn-OApjFLdcGCTRVMIGJ-e4T4BVWLsTMBL8Jr78AojZBvk0vQXpzh3RJSUh29HbDoFjmdaTIiVU09xFqXhhHspfDRdCLvMEkLnH2h7n1_kbEEtwZK3XCcmw7A_AX3CQc1FKT4AmxJ5J1ZsvonLyqGg1h9_lJP1Xprg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/876466a913.mp4?token=oq56lDWkhzSk0tzeFMqEQYzet1cdY9fkybUEaZ2zAg5cbGAZFyjeDskN0Up3yawXYSPtzduBJ6kzwsh2hPdhgLx0B8QOeaUY1YBtk9GPyNxltTyZGdiJirDxMYVK1xc_LWouj9hL8Te81L25GVC_U6fN7MiraDsuMJAgW7RLH_UVOdrcEVkFmn-OApjFLdcGCTRVMIGJ-e4T4BVWLsTMBL8Jr78AojZBvk0vQXpzh3RJSUh29HbDoFjmdaTIiVU09xFqXhhHspfDRdCLvMEkLnH2h7n1_kbEEtwZK3XCcmw7A_AX3CQc1FKT4AmxJ5J1ZsvonLyqGg1h9_lJP1Xprg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق گفته خانم دکتر؛ دیگه خوردن واژن خانم‌ها نه تنها دیگه نباید باعث خجالت شما بشه بلکه پر ازخاصیت و فواید زیادیه که تاحالا درجریان نبودیم!
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/71069" target="_blank">📅 23:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71068">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8g2sdqBqX6QC6SI33ktaRETt9Kbo57P3ZlHIyDsuk5Yv6yjFq9LNIMaSxWJx8R64LGMPGQmYHHm7jHOk8f-wannmPsu5hXC_vNhgEJHcjeYx7FV0I3vblOQJcTrbje4YkFmvwTvdLJG0dtRWS7em9sQpnbq2scUlBK4t2T0mY3gHWyCUctmqorVuBEbzzeVV9tFr2phqvFEka1QkdHiNiD06_u3geyv94TUC6qMTCwh4B5AdAbNrGUnLvgoHa2Gawv5qjhlTDAEnvnDjO7zedCJCi4SYI1sUpH1DbU0pRRn4Rnd-QNtRaFEBFZFQ4sXN9JiPe0dR82yTPGnbl3EUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیبافِ:
قهرمان، محکم‌تر «شورت» (Short) کن؛ طوری که انگار آینده‌ی شغلی‌ات به آن بستگی دارد (چون واقعاً هم همین‌طور است).
یا اینکه سطح ذخایر را به زیر «منطقه خطر» برسان و فرو ریختنِ آن حفره‌های عظیم (و البته نابودیِ شغل خودت) را تماشا کن.
یا هم به درگاه خدایانِ نمکِ «برایان ماوند» (Bryan Mound) دعا کن.
دنیا که از همین حالا بساط پاپ‌کورنش را آماده کرده است :)
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71068" target="_blank">📅 22:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71067">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f701b5944.mp4?token=kLP_towy6V5HzBll2gyRohG6URrVRZWzt7tyif3qwJNw_MxWjjz5vB_r59oO0ADxggiOqwXTkrHDzaxFWu5y7LN9E243Yq_Q4-6K3iaFzJPi1ONIYe9wNTdm07sESDJpeEcJToXLc065a9mjOLbiNzw-cNCtMusDPDA_mQOGuQIbbdANihPGW8h3e1XES-OEtUkW2eGtSpKqr0tFZuvWOIs30dwi80KBnVy8JTCc9lCccXjjzQinB5fktTarB84m5NfhonJD0dbdhMfxRLUk_8V5--movrYM4vgKJSy_-xob6TMwbWBU0Cs2aKMP0DOh9b32plRCHaxdXXDND_F0WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f701b5944.mp4?token=kLP_towy6V5HzBll2gyRohG6URrVRZWzt7tyif3qwJNw_MxWjjz5vB_r59oO0ADxggiOqwXTkrHDzaxFWu5y7LN9E243Yq_Q4-6K3iaFzJPi1ONIYe9wNTdm07sESDJpeEcJToXLc065a9mjOLbiNzw-cNCtMusDPDA_mQOGuQIbbdANihPGW8h3e1XES-OEtUkW2eGtSpKqr0tFZuvWOIs30dwi80KBnVy8JTCc9lCccXjjzQinB5fktTarB84m5NfhonJD0dbdhMfxRLUk_8V5--movrYM4vgKJSy_-xob6TMwbWBU0Cs2aKMP0DOh9b32plRCHaxdXXDND_F0WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
ارتش اسرائیل تپه علی طاهر در جنوب لبنان را فتح کرد و کنترل آن را در دست گرفت.
ارتش اسرائیل پاکسازی دو مسیر تونل زیرزمینی حزب‌الله در رشته‌کوه علی طاهر در جنوب لبنان را به پایان رسانده و در تلاش برای خنثی‌سازی آنهاست.
لشکر ۳۶ کنترل عملیاتی رشته‌کوه را در بالا و پایین زمین به دست گرفت و آن را از وجود شبه‌نظامیان پاکسازی کرد. برخی کشته و برخی دیگر فرار کردند. خنثی‌سازی زیرساخت‌های پاکسازی‌شده در حال انجام است.
در داخل، نیروها مراکز فرماندهی، اتاق‌های تسلیحات، اتاق‌های ژنراتور، محل‌های زندگی، دوش‌ها و یک آشپزخانه را یافتند -- که به شبه‌نظامیان اجازه می‌داد عملیات جنگی را انجام دهند و برای مدت طولانی در زیر زمین بمانند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71067" target="_blank">📅 22:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71066">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeACgX-vaEwsChlYu9iEfUZg6cmjdzCwZOCcenbQkWkz41SjW6Keyz9yRAjouSiArmt4BvNq_JuXytZ31ELFjV51TCsU38g4Br_gtozCUtmsvJQ3teW2SHbzGkyOaGWnmMKfZCDvReQ3JJIsTW5DrcHJaf3Dek0DclEJl7us-9JAHHcidupbRwH2qkA413ncLx9BhIge3e48cJSQCP-Pu_3pjXzuLUnbczctvKzQ7DAF56jtoU_ch0Uns8OFj-0UD9Fh4ANCTj4aSQY49gJp4RkvCmoY8IWoFD39mBQVlD942TG6wVYY3NySjyTmmaA9ukbrwN5e1-FSKN08PHZtLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خرید حضوری با اسنپ‌پی، یه خرید معمولی نیست؛ شانس بردن BMW داره!
😎
🚗
با اسنپ‌پی می‌تونی از بیش از ۲۰ هزار فروشگاه حضوری خرید کنی و هزینه‌اش رو ۴ قسطه و بدون سود و کارمزد پرداخت کنی.
🎉
🥳
همه‌اش همین نیست؛
۵ هفته، ۵ برنده، ۵ جایزه در هر هفته هم در انتظارته:
🏆
۵ گرم طلا
📱
گوشی Galaxy S25FE
📱
گوشی iPhone 17
💻
لپ‌تاپ MacBook Air M4
🎮
کنسول PS5
این شهریور، حضوری خرید کن و شانس بردنت رو بیشتر کن:
👇
👇
👇
https://l.snpy.ir/iozfb
https://l.snpy.ir/iozfb
https://l.snpy.ir/iozfb</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71066" target="_blank">📅 22:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71065">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af33ae7319.mp4?token=v_RfSbSY6KwVCQWTNAacQnbyI26t9CMQyDA-NOOaePPCrJ9T0VDaY4651fn6KjUnR0cymi1_jNcnje7U02X3Yu5aZEsqOsshqX3XlE5zgGK4gWno9tv7SbGF2RW95p4Dec43EO_JAIZYzN28ZKzDLnNEzL31gxEjhdfk5vR5A1rjsOBB9vJmQsuHFkx6Ki9RpVfgKnVujUWLROboZLaZLk5N2DtOqwTNqJBvqwOzwk6dkGxGSa-XdM2x8Gi_bmgOq1HqoXk6YlNioyA-IjxWd4Odv1HevS1kRKgpmXZFpYFyWW1lazqYpJjQdirud3p414295zTuGgM3oT6H9kMd8JPPIzVLm5nBAW5SCCoK3fyfeYmlrm3fhJdijwWOpGtr5x-4QyRd9qrug2hpUJ1fFDFz3s72BxMwVsu1WsHxxDZ7_or9lS3h133QBzSfvuoTz0gxkfNFa6GKVp8azFT-Tm1oB-6DcEUDf0TMcK_w9Xy4plwa1BU7LgTrecuDRal2acCg4ixskGZmyvdhNzqE18pcovmbJLfo1O-5w7Oz5g1PFHp-z0tXBWbXsm6a8pPotixgIOim6FORywYAweU-xwRqk5MmVrMHYm0dHxa34Uax8y-S39vDJrA_WodLs1RtehSv4ITrY9-jpa7h7gFg2fawCAY-WQaF3_-A1Vbk0vk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af33ae7319.mp4?token=v_RfSbSY6KwVCQWTNAacQnbyI26t9CMQyDA-NOOaePPCrJ9T0VDaY4651fn6KjUnR0cymi1_jNcnje7U02X3Yu5aZEsqOsshqX3XlE5zgGK4gWno9tv7SbGF2RW95p4Dec43EO_JAIZYzN28ZKzDLnNEzL31gxEjhdfk5vR5A1rjsOBB9vJmQsuHFkx6Ki9RpVfgKnVujUWLROboZLaZLk5N2DtOqwTNqJBvqwOzwk6dkGxGSa-XdM2x8Gi_bmgOq1HqoXk6YlNioyA-IjxWd4Odv1HevS1kRKgpmXZFpYFyWW1lazqYpJjQdirud3p414295zTuGgM3oT6H9kMd8JPPIzVLm5nBAW5SCCoK3fyfeYmlrm3fhJdijwWOpGtr5x-4QyRd9qrug2hpUJ1fFDFz3s72BxMwVsu1WsHxxDZ7_or9lS3h133QBzSfvuoTz0gxkfNFa6GKVp8azFT-Tm1oB-6DcEUDf0TMcK_w9Xy4plwa1BU7LgTrecuDRal2acCg4ixskGZmyvdhNzqE18pcovmbJLfo1O-5w7Oz5g1PFHp-z0tXBWbXsm6a8pPotixgIOim6FORywYAweU-xwRqk5MmVrMHYm0dHxa34Uax8y-S39vDJrA_WodLs1RtehSv4ITrY9-jpa7h7gFg2fawCAY-WQaF3_-A1Vbk0vk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیر ترامپ هم اومد به بازار
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71065" target="_blank">📅 21:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71064">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40c15e0881.mp4?token=FapjoMiCKh26vpRtNh6I-IHmIl4b01gcWpOv5ngEL8zk703f-w81A1OgA2QPdAWt1THic5INdxeja22iBr5ymkm0llFkX2Ihe7NP6dW_KFaUcRAhO8LVDfufjPqb3yLmc37ZxXCJzdAahWt8zbhfG14hqcWeF-ktJJe7w7tSAIUD_wwmWVJQ9OuI-5dOovSgtEUwTqh9e_on5euFz_NXj3JmBiSN9tHWQgTDM9G1xEQacN5qhrXDLqz5c_fi4vwyakcA_TYHLhckhTvuqli_QBkGIg8DeidoFdfSfnnqxUPH3V0dTVV1Wa7h2MtIRdPEPrEZyuDUmG4uOHeY3M4h8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40c15e0881.mp4?token=FapjoMiCKh26vpRtNh6I-IHmIl4b01gcWpOv5ngEL8zk703f-w81A1OgA2QPdAWt1THic5INdxeja22iBr5ymkm0llFkX2Ihe7NP6dW_KFaUcRAhO8LVDfufjPqb3yLmc37ZxXCJzdAahWt8zbhfG14hqcWeF-ktJJe7w7tSAIUD_wwmWVJQ9OuI-5dOovSgtEUwTqh9e_on5euFz_NXj3JmBiSN9tHWQgTDM9G1xEQacN5qhrXDLqz5c_fi4vwyakcA_TYHLhckhTvuqli_QBkGIg8DeidoFdfSfnnqxUPH3V0dTVV1Wa7h2MtIRdPEPrEZyuDUmG4uOHeY3M4h8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
رقص عجیب «حسن حسین خانی» مداح نزدیک به حکومت  در حالی عجیب  و  با شلوارک! تو یک  ویلا با آهنگ شماعی زاده
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71064" target="_blank">📅 20:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71063">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0392122fc9.mp4?token=cKcy8CpC_n6kVOOnWtPZkbY1QGg2AeygIZApNIcTudlPekzyhCpC0DEWk-vg57-PBas3G9ORq0iwqVAgsnTor7ILjpPaUa0GqMXZI94wpzFMUdriuyvQqFgurCyegj2vMaIC54ic8EOX1Z-nJVZ9SpCklH86VaK7Pc3wVL7z16JopAZS1hEPVkPIWdnUYdB5yusKn1OkMNhtEY10j5AMmQTgj3L97wrqhtXeIfIe5b720atUs8UR19a07HpE0aDJQn6BzLipXewxwDWVcO666YzB2b4jBwnExlMocbb2kyvlAmyKGl-3_cxigaaHVKXIcRwbXGKbFpPP8OR4Y8ebEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0392122fc9.mp4?token=cKcy8CpC_n6kVOOnWtPZkbY1QGg2AeygIZApNIcTudlPekzyhCpC0DEWk-vg57-PBas3G9ORq0iwqVAgsnTor7ILjpPaUa0GqMXZI94wpzFMUdriuyvQqFgurCyegj2vMaIC54ic8EOX1Z-nJVZ9SpCklH86VaK7Pc3wVL7z16JopAZS1hEPVkPIWdnUYdB5yusKn1OkMNhtEY10j5AMmQTgj3L97wrqhtXeIfIe5b720atUs8UR19a07HpE0aDJQn6BzLipXewxwDWVcO666YzB2b4jBwnExlMocbb2kyvlAmyKGl-3_cxigaaHVKXIcRwbXGKbFpPP8OR4Y8ebEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
#فوری
؛نخست‌وزیر نتانیاهو درباره ایران:
من به توانایی‌مان برای از میان برداشتنِ یک‌بار برای همیشهٔ این تهدید ــ یعنی سرنگونی این رژیم ــ اطمینان کامل دارم.
این همان مأموریت اصلی است که همچنان پیشِ رو داریم، اما به تحقق آن نزدیک شده‌ایم. این کار غیرممکن نیست؛ بلکه کاملاً دست‌یافتنی است.
آن‌ها بی‌دلیل از حمله به ما پرهیز نمی‌کنند؛ آن‌ها به همه حمله می‌کنند، جز ما. آن‌ها از قدرت ما، توان بازوی ما و عزم راسخ ما آگاهند.
من خطاب به دشمنانمان به‌طور کلی می‌گویم: با ما درنیفتید. اگر درسی گرفته‌اید، بدانید که نباید با ما دربیفتید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71063" target="_blank">📅 19:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71062">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
شلیک موشک/پهباد از سیریک به سمت کشتی ها در تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71062" target="_blank">📅 19:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71061">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdLcw1PewVc8Yf7hzDvJ_fQuWueAjFW4UmW5VjJ-dIAVAZ7NDL_ag2xp3S6xe8zn-qexbfpdqHU1mZDnSk5f_3ExmjMXp5RszIL3VN93QdYbVtBcoGmtUNx0d-EwDbTlemHSBXJx2sBZ04qiHcS5u8TM2ffwsMPrPYBt5g5RKOdCEQehzYAqfKyqeJgn_JNyWx_tnIxu0jYUlUIJSyZ8q8w4yJTGS9C69KUgDZ0yU3YuM0dkY9l7lGOEN42lf8V_xFMz2EPjDF0XNRhoeyOAWLMSQPUQHNesG8btd1A2pda-fxvDEstc3DEMUSq9zaLbyeNmJLHq9xzBsqnQ6cKAiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ در تروث:
برای آن مشتی خائنِ پست‌فطرت که از گزارش دقیق عملیات نظامی ما در ایران خودداری می‌کنند، باید بگویم که ما ذخایر تقریباً نامحدودی از مهمات با کیفیت متوسط تا عالی در اختیار داریم؛ بسیار فراتر از آنچه ممکن است برای این عملیات یا هر جنگ احتمالی دیگری (که وقوع آن بسیار بعید است!) نیاز داشته باشیم.
علاوه بر این، ما در حال تولید مهمات با حجمی بی‌سابقه هستیم. ما در حال انباشت و آماده‌سازی برای مقابله با هرگونه وضعیت پیش‌بینی‌نشده‌ای هستیم که ممکن است رخ دهد.
ما این مهمات را برای خودمان — یعنی ایالات متحده — نگه می‌داریم و فعلاً به دیگران نمی‌فروشیم، هرچند فروش به متحدان به‌زودی از سر گرفته خواهد شد.
همچنین، لازم است بدانید که دولت بایدن حجم بسیار بیشتری از مهمات را — بدون دریافت هیچ‌گونه هزینه‌ای — به اوکراین واگذار کرد، که این مقدار بسیار فراتر از مهماتی است که ما در ایران به کار گرفته‌ایم.
صدها میلیارد دلار کمک رایگان به اوکراین و ناتو اعطا شد؛ هزینه‌هایی که اگر از اروپایی‌ها خواسته می‌شد، خودشان آن را می‌پرداختند.
با این حال، ما آن پول را مطالبه خواهیم کرد، هرچند با کمی تأخیر!
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71061" target="_blank">📅 18:52 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71060">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d21cce2e5e.mp4?token=th_Gs5pS63hpsthhAbX8_JQW3tU_w0qW80zcJIXjY7HVSnKjuNRMWAOSyzTmILpZ_I8LsK9aJ6ddXWEXrY0ZlsIo6CptM4Jv1932cIOWn9qe3Dtu4xaDWQ7_euAxG8j1Ux5hwoDzGhRz7O-q8U_KYNgV3cBem-odbIBp5o7o0TAgpdV6p0L5skOjZfrwaJAZVv7oxhveeMabIWhVibhhsQB5RBzWj6x4z96_PRcs1NAtEh0FSSh3THfJrim5TjRKjtlxhGPJEQ8E8ipa1PFHhEKwRUTZBYpZXAdbep6yZfYYbn8p4eiYUtM3OQztV6RJ9GJ8v-S8M_MpzOWTvSvOrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d21cce2e5e.mp4?token=th_Gs5pS63hpsthhAbX8_JQW3tU_w0qW80zcJIXjY7HVSnKjuNRMWAOSyzTmILpZ_I8LsK9aJ6ddXWEXrY0ZlsIo6CptM4Jv1932cIOWn9qe3Dtu4xaDWQ7_euAxG8j1Ux5hwoDzGhRz7O-q8U_KYNgV3cBem-odbIBp5o7o0TAgpdV6p0L5skOjZfrwaJAZVv7oxhveeMabIWhVibhhsQB5RBzWj6x4z96_PRcs1NAtEh0FSSh3THfJrim5TjRKjtlxhGPJEQ8E8ipa1PFHhEKwRUTZBYpZXAdbep6yZfYYbn8p4eiYUtM3OQztV6RJ9GJ8v-S8M_MpzOWTvSvOrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
کسانی که دوستتان دارند، شما را فردی خوش‌برخورد، شوخ‌طبع، سخاوتمند و بذله‌گو می‌دانند؛ اما دیگران می‌گویند که شما سخت‌گیر، متکبر، مغرور و حتی بی‌رحم هستید. به نظر شما، کدام‌یک از این توصیفات درست است و کدام نادرست؟
❤️
شاهنشاه آریامهر:
بی‌رحم؟ گمان نمی‌کنم.
متکبر؟ قطعاً نه.
مغرور؟ شاید کمی. اما در مورد کشورم—و آنچه به دست آمده است
نمی‌توانم شخصاً دچار غرور شوم، چرا که انسانی مؤمن هستم. من عمیقاً به خدا ایمان دارم و اهل عرفانم؛ پس چگونه ممکن است مغرور باشم؟
انسان در پیشگاه ذات ازلی، هیچ است؛ مطلقاً هیچ؛ گویی اصلاً وجود ندارد.
البته با نگاهی به دستاوردهای این کشور، قطعاً دلیلی برای احساس غرور و سربلندی وجود دارد.
اما بی‌رحمی؟ این ویژگی من نیست؛ این نهادهای حکومتی هستند که باید عمل کنند.
وظیفه آن‌هاست که کسانی را که قصد آسیب رساندن به این کشور را دارند شناسایی و خنثی کنند. اگر نام این کار بی‌رحمی است... خب، در آن صورت باید بپذیریم که در این مورد با هم اختلاف‌نظر داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71060" target="_blank">📅 18:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71059">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/259e330a05.mp4?token=EE8QHd7bePjf3_aJVMz0LkYThFEeGzDpTapbZSdouLkkZMGpD9ZbNNb01-O-XWw1WaAdyJeVgV2uJsTeD_gYia0Et85iAGp0NQ9irU5cvdkOarOFFxVm2FHdBgzheuiTxakxKvtRejJJB82UbZSS9UddSg1iPscLmdQDg7t3tIJlBRlE-EUXbJDYgxczKOJxiuNYej4E-WoQNXE4VBDMhdyX9rN24V8tAKOnM4IPqdIuR_9nMrgvyi5VNQXY4mgM8hD5fsqc1gtY2KVbkzcZimy6_Ce3mJhbcnGqUGFXTENdvA84ty_A7doKUWHyC1_1z_bEmWUl7ztAWnjqkOa_JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/259e330a05.mp4?token=EE8QHd7bePjf3_aJVMz0LkYThFEeGzDpTapbZSdouLkkZMGpD9ZbNNb01-O-XWw1WaAdyJeVgV2uJsTeD_gYia0Et85iAGp0NQ9irU5cvdkOarOFFxVm2FHdBgzheuiTxakxKvtRejJJB82UbZSS9UddSg1iPscLmdQDg7t3tIJlBRlE-EUXbJDYgxczKOJxiuNYej4E-WoQNXE4VBDMhdyX9rN24V8tAKOnM4IPqdIuR_9nMrgvyi5VNQXY4mgM8hD5fsqc1gtY2KVbkzcZimy6_Ce3mJhbcnGqUGFXTENdvA84ty_A7doKUWHyC1_1z_bEmWUl7ztAWnjqkOa_JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبت‌های این پسر درباره‌ی اونایی که میگن کسایی که ریش ندارن کونی هستن رو با هم ببینیم:
کدوم مادرجنده‌ای اینو باب کرده که هر کی که ریش‌وسیبیل نمیذاره، کونه؟
شما برو فیلم سوپرا رو نگاه کن، عمو جانی کونش هم یدونه مو نداره، چه برسه به صورتش.
ریشو کسایی میذارن که ترس از کون‌شون دارن، اونایی که عقده دارن و بچگی کون‌شون گذاشن، ریش میذارن.
خیلیا ریش دارن ولی صد مرتبه از کونیا بدتر هستن
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71059" target="_blank">📅 18:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71058">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71058" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71058" target="_blank">📅 18:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71057">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxXQy_ubF6XSFLdpiak8IrPnaqdr8IIketZFr9KzTwtdIfns8ZkMktyAUERuAQaqU6lOU3oOmphkoUNIjQkmKBfNORmr4zm6FDQ096jTl_HUgAAa5ELiBOYvqPxWXJJLX6wd--lU7BSBNP0tqgEpHp6mQA6lxBm6kukUewfpPM7HkCFePgGFAcJRjZ6TYXdsr989ZEk1I1NU2DBVi5vuzC6rnnKTW193QJp9TJwc4_drTdPhQelPLehF1ZvZQjEQqQEigRC0eDwUGtJSbi5i44xm6T8oiUlvTpSVktvI0Wts71NmoUKr2OzP60VGoyllAIBng28px9N4Ir8iQVWa-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان
US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71057" target="_blank">📅 18:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71055">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGdUT2tmJFCO0i7VBd4htYGiCFITRDHgXYFLf2A_8tCnLwR4mfRc7lLkz-BOaygp-nz4kwCglX62GDhC4yy5G9UFXi6AzwplkebowbRKSt_5PBz7SD7-yRIll3IRe5r5vc4bxFUtElGxLXuV_9W8m3_QluZ1uusU6zxvpw4JO3gI0oVB0_jawbE2U6EMV9_nTi3WKSdLI5AXwSyNoJgCKz1IDph9llxaxIu2C4Amj8qRes99xgRGyfWg_DNr3ElUfopDTjDSEfaJE_uu8VhBIGzcIT_2c89jTSj2-XrZOC2qyztrXdYYTVt8OaX9WPe4MPKNWuC8QgzCgnRLEJkSJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
💬
🙂
پست جدید تلگرام در پلتفرم ایکس:
حس و حال بامزه‌ای دارم، شاید بعداً عکس‌های نودم رو منتشر کنم!
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71055" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71054">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8VWCtTdfWrc3MGWXTrb8HXz-ZWqewIq3udkgQ-5W4wZ-6-rIwCCnKyB-1rkLXyiLi9YcfG1ZliJo7zy2OpiGsxSy-8b8VkncwUNjMY6U7cCzU7yrF2S4enPwvS7PMGjRB-tmsphRAZEOCjcDzH_2dMQJIj2SMseSF5iAMCNPMOFxrfPGM0jrGIl8vVbvdoecpAGLAxRsBrQQ2fzcrZAlSGQcEjJXno6P-LxAB2ghjkZuB4F1f9HEG2tojZLNgePJoEo6AfXFx-5hocp2NfE7gy0PD5czQ95_LrgzvyuKXcCb7Ycx6STQ-eITTNHJ1lRAVgo9c4cwR5p_Zb6EKsMWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
جمهوری اسلامی کشته شدن سه خلبان نظامی در حملات آمریکا در دو شب گذشته را تأیید کرد.
اسامی: مجتبی باقری و حامد اوکاتی (خلبانان هوانیروز/هواپیمایی نیروی دریایی) و حسین مهدویان (خلبان نیروی هوایی).
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71054" target="_blank">📅 16:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71053">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03924aeb44.mp4?token=rf2JB4z9i8nKIODZN5Eze2bX7JPUTVWoCVeFm3sDFhEiVm_7iAfp9G5rpNXUu5zItqaDF_c14BYCTiRukaj7zGe90cKa0baTz3KCIJYreN6zENsdnj6OOKlj4sNZg8MkzeWGnpavMe4o2Mxys_DGbmUPdmPDBRsUeaZn4lc0I4XGOR4yTA7_WNgCuWFT2K4dnP2MVMV-cp7ltLEsVyEFa1Xn4MLPxZKX20XHeg6bsfxR3bMPka2LSsFZ1M4VBe-RurD1Nh2c81jUigCLCS31jl2Tj9gbd5V1CQJEIHI3X52icbh1fmnnkrs_PEygmr4CIST_1Ifm7QrKSBaXqyHeww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03924aeb44.mp4?token=rf2JB4z9i8nKIODZN5Eze2bX7JPUTVWoCVeFm3sDFhEiVm_7iAfp9G5rpNXUu5zItqaDF_c14BYCTiRukaj7zGe90cKa0baTz3KCIJYreN6zENsdnj6OOKlj4sNZg8MkzeWGnpavMe4o2Mxys_DGbmUPdmPDBRsUeaZn4lc0I4XGOR4yTA7_WNgCuWFT2K4dnP2MVMV-cp7ltLEsVyEFa1Xn4MLPxZKX20XHeg6bsfxR3bMPka2LSsFZ1M4VBe-RurD1Nh2c81jUigCLCS31jl2Tj9gbd5V1CQJEIHI3X52icbh1fmnnkrs_PEygmr4CIST_1Ifm7QrKSBaXqyHeww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تو ایتا و روبیکا با انتشار این فیلم نوشتن سامانه پدافند لیزری جدید اومده و همه موشکا و پهپادای آمریکا رو با لیزر زده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71053" target="_blank">📅 16:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71051">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94edb900f7.mp4?token=kTS56VuG5L6lWY3AnzMKD4v7Lt2AWAc8iF0ercKq_e51nNsozQGmWjFIPBJRCIKAxxj4ZCnT0-3AvrM9pjn0EaCOce-_9_DxOSYMPfr2JEJmQzJd0O23_uVHwHO6dr1PSlYXLWKLZ0cLFB-SD5DJHWrZNJQODZnjKklL1Z-MMHlAL7eRt0IBANUuuFTf5zc530qCbNp96m3Olb4J99AjIGUdxExhzke5CiTXleqW9d4HPVJAfaY5OxT7clSyH1dhGoF48i3OHrU4Wo1IhSPGgeRnizKytNI3N7G1qzUnHmOJn0RaNR5-YQd6SKqK9Po-oG6znqaLIJwvz-tjaqV8hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94edb900f7.mp4?token=kTS56VuG5L6lWY3AnzMKD4v7Lt2AWAc8iF0ercKq_e51nNsozQGmWjFIPBJRCIKAxxj4ZCnT0-3AvrM9pjn0EaCOce-_9_DxOSYMPfr2JEJmQzJd0O23_uVHwHO6dr1PSlYXLWKLZ0cLFB-SD5DJHWrZNJQODZnjKklL1Z-MMHlAL7eRt0IBANUuuFTf5zc530qCbNp96m3Olb4J99AjIGUdxExhzke5CiTXleqW9d4HPVJAfaY5OxT7clSyH1dhGoF48i3OHrU4Wo1IhSPGgeRnizKytNI3N7G1qzUnHmOJn0RaNR5-YQd6SKqK9Po-oG6znqaLIJwvz-tjaqV8hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این کلیپ از یه دختره که سر سفره عقد، آقای داماد رو سورپرایز کرد و گفت من مهریه نمی‌خوام و فقط 14 شاخه گل بنویسید
؛
هیچی دیگه پسره دیروز طلاقش داد و اونم با 14 شاخه گل رز طبیعی قرمز  یک جلد قرآن برگشت خونه باباش...
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71051" target="_blank">📅 16:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71049">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/01429c982d.mp4?token=ZZkfmqMCWK14eR6PfukjO3zPSrL6IHkYyGH4PV2jjdRwIBeKcNqzwqvwIXLXodfhh9VzUPTKfimLUrAfCz39P26rljLsWeK_VRQzrBAGvOXaek1uKsGOh3oj9RSZExuwY7YYZd-j9mvlTslCUQeYsf9IVseVYAYsm_nOHCljo9S2sicNOmSkc_mi69hfiii9sPADtTSXK2rlb8Q7cy0gUrPQiZdGOQMyD6HCGognUmCGe6LxMOXpXDM9kPiuxZ4S4M1hnjJoAD11hQRinOayhqGxKV60TFXiNqGx69wQR6MAr6p04K1Ca5NWExHxOHxC0nRnOfxqcmCsy0PyDFm1DA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/01429c982d.mp4?token=ZZkfmqMCWK14eR6PfukjO3zPSrL6IHkYyGH4PV2jjdRwIBeKcNqzwqvwIXLXodfhh9VzUPTKfimLUrAfCz39P26rljLsWeK_VRQzrBAGvOXaek1uKsGOh3oj9RSZExuwY7YYZd-j9mvlTslCUQeYsf9IVseVYAYsm_nOHCljo9S2sicNOmSkc_mi69hfiii9sPADtTSXK2rlb8Q7cy0gUrPQiZdGOQMyD6HCGognUmCGe6LxMOXpXDM9kPiuxZ4S4M1hnjJoAD11hQRinOayhqGxKV60TFXiNqGx69wQR6MAr6p04K1Ca5NWExHxOHxC0nRnOfxqcmCsy0PyDFm1DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز، اولین ایونت مد و فشن توی تبریز برگزار شد و حسابی غوغا کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71049" target="_blank">📅 15:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71048">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7913d873f1.mp4?token=reOwbCn5TRNG4un4G0vG9PXGSjkqDOBw--9pNabrepQ6oFCMSnl9AjXLc3pUYJxLR24ejydOxHknM2hSPsljOfklF4icNzua6D2BK5-QRZvHEVHzrhHNxfzt6aQA25ad_qII82UdLcDb198F42-9lCH7IC_1SceKWAqug0VaY8j0HKmDI3B4kqSuQ1hER02Vd4NRflXHMXgUAYdmThK5JVinEMbE1WEWMk01wlQdgxjy9zYtlJpVwlJAge99usrRNhYlROlFBQ-j1YSNPKnQwyG7_iND6Kb5A6w4NpCVBrrzOOUG8tYWX6dvQ_S2GRHWJ6BxN1_WT8SFzVSIcPgT9g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7913d873f1.mp4?token=reOwbCn5TRNG4un4G0vG9PXGSjkqDOBw--9pNabrepQ6oFCMSnl9AjXLc3pUYJxLR24ejydOxHknM2hSPsljOfklF4icNzua6D2BK5-QRZvHEVHzrhHNxfzt6aQA25ad_qII82UdLcDb198F42-9lCH7IC_1SceKWAqug0VaY8j0HKmDI3B4kqSuQ1hER02Vd4NRflXHMXgUAYdmThK5JVinEMbE1WEWMk01wlQdgxjy9zYtlJpVwlJAge99usrRNhYlROlFBQ-j1YSNPKnQwyG7_iND6Kb5A6w4NpCVBrrzOOUG8tYWX6dvQ_S2GRHWJ6BxN1_WT8SFzVSIcPgT9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این کلیپ در مورد پسرای زیر ۳۵ سال که موهاشون سفید شده، در حال وایرال شدنه
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71048" target="_blank">📅 15:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71047">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKVE2FiyqVFTzEx8B2YqzJeTNgj5jnym1g3Fzbww7HUW6ePJHH-46QsqeYKrqdVGw_BHWcL1sHBvgKsgr5t-kcqIp7tRuVz4TmjKSvCcJ6oLgI62vp6EdJ30gQA3okmT2szDS2hDUx0h4c6EUj38nbT0VAk0w6v983kGawOtWfbgc2zOCNOEOURSwah81xMLQLRotoEBAtcuuN7Mqefbq4xe5zScBKP8Mx2GncdkeorJ5-6tCIhQ05qptRIHOI8PLFXhOtKwmiTkrnJ_TGwvzOzVekGae5y_L4Yizm4CjVcffckJd83Ja1JAtLAcJeRWF90syE-e8Dxno__4cmCkjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
خبرگزاری میزان وابسته به قوه قضاییه، روز پنجشنبه ۱۲ شهریور ماه اعلام کرد حکم پرونده صادق ساعدی‌نیا، فرزند محمدعلی ساعدی‌نیا، در دیوان عالی کشور تایید شده و او به ۱۲ سال و ۶ ماه و یک روز حبس تعزیری، مصادره کلیه اموال منقول و غیرمنقول و محرومیت از اشتغال به شغل کافه‌داری محکوم شده است.
مرکز رسانه قوه قضاییه این پرونده را مرتبط با اعتراضات سراسری ۱۸ و ۱۹ دی سال گذشته دانسته و مدعی شده است که متهم در «تحریک اعتراضات و ورود خسارت به اماکن و اموال عمومی در استان قم» نقش داشته است.
صادق ساعدی‌نیا، فرزند محمدعلی ساعدی‌نیا، کارآفرین و نیکوکار ایرانی است. محمدعلی و صادق ساعدی‌نیا در جریان انقلاب ملی ایرانیان در دی ماه گذشته دستگیر و اموال هزاران میلیاردی آنان مصادره شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71047" target="_blank">📅 14:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71046">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:  اگر ایران به دولت اسرائیل حمله کند، این اقدام اسرائیل را از هرگونه محدودیتِ موجود برای حمله به ایران رها خواهد ساخت. ما به تمامی زیرساخت‌های ملی، نظامی و غیرنظامی ایران - از جمله زیرساخت‌های انرژی - حمله خواهیم کرد و ایران…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71046" target="_blank">📅 13:58 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71045">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7750e2ea67.mp4?token=VsGVmZEolE6IZyUwOnYEFTVoqTIpjGq6Kei5pQPWQTzMskGitvR-2PjCma0_ukB6cGVHcSeKZPsj4MXz8rRv29cRF6PkmL103bcLmf_uF5mx0PGsB7xjCG7p8nZWRfRVbILyjFEgvOp8kdcoRGUyXvToZhY2ickThNiZ0yPnc2t5Nlt194Vg0DtwlvMMBUQ13Od-2lK8QdSDwT8qRaOKRHKM0KcK9XUcTopzr3kcWuMlSLX0iiEfOMrFj_li4MXwj1qzZGQKqoFzBOgue8qUBjoauxsQXZ1i1ZPmDvYMezncdrgzDtfGwOnqDwE9HIJUrjdt-TnOa_7-4IfoX_I7SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7750e2ea67.mp4?token=VsGVmZEolE6IZyUwOnYEFTVoqTIpjGq6Kei5pQPWQTzMskGitvR-2PjCma0_ukB6cGVHcSeKZPsj4MXz8rRv29cRF6PkmL103bcLmf_uF5mx0PGsB7xjCG7p8nZWRfRVbILyjFEgvOp8kdcoRGUyXvToZhY2ickThNiZ0yPnc2t5Nlt194Vg0DtwlvMMBUQ13Od-2lK8QdSDwT8qRaOKRHKM0KcK9XUcTopzr3kcWuMlSLX0iiEfOMrFj_li4MXwj1qzZGQKqoFzBOgue8qUBjoauxsQXZ1i1ZPmDvYMezncdrgzDtfGwOnqDwE9HIJUrjdt-TnOa_7-4IfoX_I7SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
اگر ایران به دولت اسرائیل حمله کند، این اقدام اسرائیل را از هرگونه محدودیتِ موجود برای حمله به ایران رها خواهد ساخت.
ما به تمامی زیرساخت‌های ملی، نظامی و غیرنظامی ایران - از جمله زیرساخت‌های انرژی - حمله خواهیم کرد و ایران را به اعماق دوران حجر و تاریکی بازخواهیم گرداند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71045" target="_blank">📅 13:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71044">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80b05262cb.mp4?token=g0eqdA65TedwK6JCZcwD7HB9CPB_4J16Itq2qc0DJ8CwArLKYalzPtpzgH_epKwgEV8kNVkc2zGWwnB-S1ln9dRF4FyCnL_Le-z15XolYKXlPXsO2GEKwb-QObzPVMwpa0IuVZo7PhhjbMZ7aZX7zs84sFU2xLDeeDd7cwl3v7YofVM50CdbMoPSagnw3sLtmIj110ZRrJvl-hLhkN-vHn7GlGFGATqcf7lhpeADGfdk68MZ0J0kdjspGq_gNzpJ3QIjOoqVX3JwsUOqtThR2sX346iAu53XtYBPBZtei809Ja3hZGEveL4jtBMf6gkjSFxxGbjET7xN0IKDtqp3VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80b05262cb.mp4?token=g0eqdA65TedwK6JCZcwD7HB9CPB_4J16Itq2qc0DJ8CwArLKYalzPtpzgH_epKwgEV8kNVkc2zGWwnB-S1ln9dRF4FyCnL_Le-z15XolYKXlPXsO2GEKwb-QObzPVMwpa0IuVZo7PhhjbMZ7aZX7zs84sFU2xLDeeDd7cwl3v7YofVM50CdbMoPSagnw3sLtmIj110ZRrJvl-hLhkN-vHn7GlGFGATqcf7lhpeADGfdk68MZ0J0kdjspGq_gNzpJ3QIjOoqVX3JwsUOqtThR2sX346iAu53XtYBPBZtei809Ja3hZGEveL4jtBMf6gkjSFxxGbjET7xN0IKDtqp3VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
جنگنده میگ-۲۹ام‌یو۱ اوکراینی یک موشک اس۸۰۰۰ «باندرول» روسی را در ارتفاع پایین با یک موشک آر-۶۰ منهدم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71044" target="_blank">📅 13:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71043">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/162568634d.mp4?token=hSMv_ilHv9cPIB8x98-2Q7enfsd1wRo7BrK4yhMxYxX0TuHC1HeGmqf73L2AyJUH4wiqpdw8zAef6F-noulg1mhnSMMCnaTYBybMZFM7qR8xAAQW-WnJpjMfsYYhXqyiln1kFsjH4kNdDui9dNrEL2KkHeRxKsJJNvxSDG12girPn1uPqsajxPBPhIMRQcgmiHii54bZBBXpCZCQjTuFFAPwXjqRbqAQM4UeKRuyo01_WkAgqShoCE00L3ag1pVe_MkdsOZEvcoj5MhgkDdElDJoE1d3VsiHXGKSJZjO5auX6Jd7PFzCwatWQ78Q_PHl2Z7XPWPK0UBTLhV9hd1QyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/162568634d.mp4?token=hSMv_ilHv9cPIB8x98-2Q7enfsd1wRo7BrK4yhMxYxX0TuHC1HeGmqf73L2AyJUH4wiqpdw8zAef6F-noulg1mhnSMMCnaTYBybMZFM7qR8xAAQW-WnJpjMfsYYhXqyiln1kFsjH4kNdDui9dNrEL2KkHeRxKsJJNvxSDG12girPn1uPqsajxPBPhIMRQcgmiHii54bZBBXpCZCQjTuFFAPwXjqRbqAQM4UeKRuyo01_WkAgqShoCE00L3ag1pVe_MkdsOZEvcoj5MhgkDdElDJoE1d3VsiHXGKSJZjO5auX6Jd7PFzCwatWQ78Q_PHl2Z7XPWPK0UBTLhV9hd1QyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
روابط عمومی ارتش:
در ادامه سلسله عملیات‌های صاعقه و در مرحله سی و یکم،  در انتقام خون پاک مردم بی‌گناه و دلاورمردان نیروهای مسلح، بامداد امروز، ارتش جمهوری اسلامی ایران، «سامانه‌های ارتباطات ماهواره‌ای»، «انبارهای تجهیزات» و «آشیانه هواپیماهای جنگنده» ارتش تروریستی آمریکا در پایگاه احمد الجابر کویت را با موشک‌ها‌ و پهپادهای انهدامی، مورد اصابت قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71043" target="_blank">📅 13:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71042">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71042" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71042" target="_blank">📅 13:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71041">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b754CeVmeSV7kehXWuQfCC_AUyLPFIeDTpZOMOmUCFtsc7LM0Bx7YRZ-OIr9Mn6Wc3cEVuD3DkYr9mbIfYDbFq0ZzfnYmZEiSB2nrIfiuzKhKJXNdQ2EN-xpbUdIGGm6YI-_tc_jx_jc3Ebsh-1ZE5MYkaf582koHKI71io4YCa8yBAvgduyNDRlRUbOjlAz4EHasL8LrLnFkK2kiq_J5KvcaVUNVGR-JVFK8yQsiOHSWp2XSdA_HfEY01K3Uf6OIB_eum8b2RpUrBXGQYiJRg2onLJ0gFghyUI8dRoLFHY0mFtUSTq6eNAj0nSnac0FksXnYU8_o7HS2OTpnFg7BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71041" target="_blank">📅 13:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71040">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2218c2694e.mp4?token=ThcRRCnkTZrGi8CGCDKMa-67oqOJlYgQxXco-MHkfqK7yWBPe_NlcXdcK3eFlrQjarFwrx-3MaVn_yRgLd5PSz3hKFcUmhGPOuS38_F0qmrnSfFBVcacEWZvcYAJDlwgYbQwhX-5_6AMEUWkgWslheZN50nCoEWvDg9t_0u5FlCzKDWdv32kurfLrjCY5zxunyA3Vihb1fPh0ay4_XxML1Z37FjLeCGi3oNKbdb6VUsNbOQ4vf7wX_RCmMFJ7whYOcDoCZo9Ey80Dr21fP2fjLQ0Kasy0m2yuuWGuKRliRXzgSjBgxZri2pG3YfmmWt8lAdC_ZBz85HdydzPk43eTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2218c2694e.mp4?token=ThcRRCnkTZrGi8CGCDKMa-67oqOJlYgQxXco-MHkfqK7yWBPe_NlcXdcK3eFlrQjarFwrx-3MaVn_yRgLd5PSz3hKFcUmhGPOuS38_F0qmrnSfFBVcacEWZvcYAJDlwgYbQwhX-5_6AMEUWkgWslheZN50nCoEWvDg9t_0u5FlCzKDWdv32kurfLrjCY5zxunyA3Vihb1fPh0ay4_XxML1Z37FjLeCGi3oNKbdb6VUsNbOQ4vf7wX_RCmMFJ7whYOcDoCZo9Ey80Dr21fP2fjLQ0Kasy0m2yuuWGuKRliRXzgSjBgxZri2pG3YfmmWt8lAdC_ZBz85HdydzPk43eTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تو میدون تایمز نیویورکِ آمریکا، یه خانمِ چاقو بدست بعد از اینکه یه مرد و یه زن رو از ناحیه شکم زخمی کرد، بعد از اخطارِ پلیس‌ها به سمتشون حمله‌ور شد و به این شکل بهش شلیک کردن و کشتنش.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71040" target="_blank">📅 12:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71039">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f52d28bc.mp4?token=HhvX7iVqB07bHfLtUEFMm4gi_9PoVMT1_pqJinkpDpkaqlb6GQ65IK3I5PsSR_E6sZ-v1a7T3E1RLFC2DKSIeOzJ0-6lAigYM7osMd6Xu8E-BBjreTVIZTY93zGDHYHeKq0QCBW7cp4mKZS3GB_n79BRyheUYgxzxUAD7vezycxRx-p3sBOCPj5qvO8EBPf1tumUMNoM4Z5qdaDfJ101CCkV7MErCO2V43YWdp1HBeDl3M2jnOOiIZQuLebDlD1WvFBAD2kmbU__q1qkjPO6cG7jeQdZfzM-NLWy6cIoI3dBtyepmyGV27VdECJ9R4SQCbMstoXswjvnC-Z1ceAKAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f52d28bc.mp4?token=HhvX7iVqB07bHfLtUEFMm4gi_9PoVMT1_pqJinkpDpkaqlb6GQ65IK3I5PsSR_E6sZ-v1a7T3E1RLFC2DKSIeOzJ0-6lAigYM7osMd6Xu8E-BBjreTVIZTY93zGDHYHeKq0QCBW7cp4mKZS3GB_n79BRyheUYgxzxUAD7vezycxRx-p3sBOCPj5qvO8EBPf1tumUMNoM4Z5qdaDfJ101CCkV7MErCO2V43YWdp1HBeDl3M2jnOOiIZQuLebDlD1WvFBAD2kmbU__q1qkjPO6cG7jeQdZfzM-NLWy6cIoI3dBtyepmyGV27VdECJ9R4SQCbMstoXswjvnC-Z1ceAKAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سایپا تو ماشینی جدیدی که زده ماشین با اینکه راه نمیره ولی براش کیلومتر حساب میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71039" target="_blank">📅 12:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71038">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffEQ2Bj-3EZnnOjSSfTdvLW_WtQ1CtU63CyYgojdVk76Sw9ctKSncGuDG58hKlOcztSuhb6dZ5fk2WL3DmF64cupsQ36Le3QfW_O09kA_UCHDax7hK4JK6QhHSrENYmnNWTuFz7YKMnRn3P6mWI2NxFhVZghbH-4BE3-escWrJ0SLVXE8BH_jkWPqaEyTHiEeCx5OBIsHnP-zqpUDmANtAxi56_UmtVb2PXDoVi1YEyIc9OQNG6p9Lw0B-yrLFEK-h7qdof7CZkM4zoLNTgaIYa-VZTc_oBclHHkJmO48yNuJ3vR8nCzkPtqaHldRnKkXUXFOVZr9kptHlzYqWwAwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
📰
اکسیوس:استیو ویتکاف، فرستاده کاخ سفید، آخر هفته گذشته در ساردینیا با شیخ طحنون بن زاید آل نهیان، مشاور امنیت ملی امارات متحده عربی، درباره ایران دیدار و گفتگو کرد.
این دو مقام درباره گام‌های احتمالی آتی بحث و تبادل نظر کردند؛ چرا که دولت ترامپ در پی بازگشایی تنگه هرمز و هم‌زمان افزایش فشار اقتصادی بر تهران است.
امارات نقش کلیدی در تلاش‌های تحت رهبری آمریکا برای عبور نفت‌کش‌ها از این تنگه ایفا کرده و در راهبرد تحریمی واشنگتن، کشوری مهم محسوب می‌شود.
مقامات اماراتی به دولت آمریکا اعلام کرده‌اند که هرگونه کارزار مؤثر فشار اقتصادی باید شامل تمامی کشورهای عمده‌ای باشد که همچنان به تجارت با ایران ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71038" target="_blank">📅 11:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71037">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی به بندر سوچی در روسیه حمله کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71037" target="_blank">📅 10:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71036">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef77017317.mp4?token=pt8Rb173ADdGtyGJcnwDbUgBifM_m6yw_XNzX3h0eoJ4muQex8ZIUpdO3lr60nDAb_agRrPt-yVavJ_c06gVTVP7E7dsP0hRu5EyiQEuR8tRbt9YwhumZ-zY90wPv41vbI_JzNHU1MhL3zCysDzQdhCoDCYTG1z2LvMj8aocKjgkfLiK-XJ2EMe8R3Ss4orwGzJBU9_VT42EDCRr5dSkzmB_PIjAZzxUywny_SMYlkZTM4TSK_Shg5izWe6oWex4SOH3KimbwRINYRi5nT9eLSFXAyyhC8tZ2x8y_WmUkzKHcrOvNuGRLqFjTp4Bnv1lyVr4g18L73F6n32YFQHZDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef77017317.mp4?token=pt8Rb173ADdGtyGJcnwDbUgBifM_m6yw_XNzX3h0eoJ4muQex8ZIUpdO3lr60nDAb_agRrPt-yVavJ_c06gVTVP7E7dsP0hRu5EyiQEuR8tRbt9YwhumZ-zY90wPv41vbI_JzNHU1MhL3zCysDzQdhCoDCYTG1z2LvMj8aocKjgkfLiK-XJ2EMe8R3Ss4orwGzJBU9_VT42EDCRr5dSkzmB_PIjAZzxUywny_SMYlkZTM4TSK_Shg5izWe6oWex4SOH3KimbwRINYRi5nT9eLSFXAyyhC8tZ2x8y_WmUkzKHcrOvNuGRLqFjTp4Bnv1lyVr4g18L73F6n32YFQHZDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی وایرال شده از پسری که چالش گرفت که تو خیابونای شهر از مردم درخواست پول کنه(نفری ۱۰۰تومن) و اکثرا قبول کردن و در آخر هم پولی که جمع شد رو رفت به نیازمندا کمک کرد
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71036" target="_blank">📅 10:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71035">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7de7f7edfa.mp4?token=EV9QhlFGkZU6bLL52yAb8Cuh_oBa3Hn66d8Y5SGHDYNJ6zHDvgb-izIp1sxKQ9zZNz4k8HnEWVI9--rHMzEMKDORO1tGWRgXMr283FkzGbOpRCbmvCulaTyZhet__BrJOoJpbgySHSsw-UH7PcAkfQdjsmQl-8pWY5ReUAIktDksWbmB5dlbTnaZh0cLJ_EDZt1GE7O2g52EJHx62pFUX7uWTTv2K9_qA0Ov3hSirPVAeROYK4y3EQbVTQqkFjaHEyABIEPY9kKeITPpZ-30QgdcT_172c0HmXPN5n6do8saNumxcYS8Tkl90-S34ztKSuctW5LvV0oP-QVa2smp-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7de7f7edfa.mp4?token=EV9QhlFGkZU6bLL52yAb8Cuh_oBa3Hn66d8Y5SGHDYNJ6zHDvgb-izIp1sxKQ9zZNz4k8HnEWVI9--rHMzEMKDORO1tGWRgXMr283FkzGbOpRCbmvCulaTyZhet__BrJOoJpbgySHSsw-UH7PcAkfQdjsmQl-8pWY5ReUAIktDksWbmB5dlbTnaZh0cLJ_EDZt1GE7O2g52EJHx62pFUX7uWTTv2K9_qA0Ov3hSirPVAeROYK4y3EQbVTQqkFjaHEyABIEPY9kKeITPpZ-30QgdcT_172c0HmXPN5n6do8saNumxcYS8Tkl90-S34ztKSuctW5LvV0oP-QVa2smp-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
ویدئو جدید از پرواز هواپیمای HC-130 Combat King II آمریکا در ارتفاع پایین در عمق کشور به دنبال خلبان آمریکایی جنگنده F-15E
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71035" target="_blank">📅 10:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71034">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad58d044a.mp4?token=vgAvHPHaF-hAio3gPWsQTM5NF6gwQBCIRHJXf2moSxhegfZo72cgsJNU7l170yo80_U_xZBhItcetXzuUYVHU8q2DWYCubYKgIr9VTvgKPU3EXVNDPK2T5DGM-bVtcimsdxTzGx09FI68P7OI8BCu28LizvDvXkN4KclhlExhscafwmhAxUgY8iy4eKOIps82Hb-vQt8R-AL83aeqCsOyQMZFkCVItJaZlDuD9TLCa_D7IZiosQQsV_z-6hiAwLlXtOxvgZF0dJsXj1Urk1vWfkSpw8T_YuDW2CA8tYLmqmartravEsw6qXW4OBEGOEHyGMZLe8OvyRKJwj3yljALg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad58d044a.mp4?token=vgAvHPHaF-hAio3gPWsQTM5NF6gwQBCIRHJXf2moSxhegfZo72cgsJNU7l170yo80_U_xZBhItcetXzuUYVHU8q2DWYCubYKgIr9VTvgKPU3EXVNDPK2T5DGM-bVtcimsdxTzGx09FI68P7OI8BCu28LizvDvXkN4KclhlExhscafwmhAxUgY8iy4eKOIps82Hb-vQt8R-AL83aeqCsOyQMZFkCVItJaZlDuD9TLCa_D7IZiosQQsV_z-6hiAwLlXtOxvgZF0dJsXj1Urk1vWfkSpw8T_YuDW2CA8tYLmqmartravEsw6qXW4OBEGOEHyGMZLe8OvyRKJwj3yljALg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
تو یه فروشگاه تکنولوژی تو روسیه، یه ربات بعد از اینکه مشتری هلش داد، شروع به دعوا با مشتری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71034" target="_blank">📅 09:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71033">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e73b2179fb.mp4?token=T82I8TYuDLBPEI0JMkcOH0wRHjKlCHoxifPiDN5oicKIFJXCB-RzbpgmTGqdAJY3suyDwpecEWnljzyXwn3ZQir-XIEH4IXT7HeYHjK0jsUbQWu9iAm0Xxy_L0rHxUUmpgfjASNAKA9b5Jo_Jn-LBHP_U729FS4etYTMh555BksRlUQRFJhgtlFhTCC8J0j8ADKky5wlZohE7ClaXggvV_qzV8TNGNa6jTBo2Yy8folR6McWPVhUCoTN9cn2vzj1FoGSHK8izHPYYXdhMp3DEz3m7jGavk234P2CNxntgwaCiKTKjp_8gIf-7VwtuiKBzmvjZV8-Yy_ob_HEpYXOAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e73b2179fb.mp4?token=T82I8TYuDLBPEI0JMkcOH0wRHjKlCHoxifPiDN5oicKIFJXCB-RzbpgmTGqdAJY3suyDwpecEWnljzyXwn3ZQir-XIEH4IXT7HeYHjK0jsUbQWu9iAm0Xxy_L0rHxUUmpgfjASNAKA9b5Jo_Jn-LBHP_U729FS4etYTMh555BksRlUQRFJhgtlFhTCC8J0j8ADKky5wlZohE7ClaXggvV_qzV8TNGNa6jTBo2Yy8folR6McWPVhUCoTN9cn2vzj1FoGSHK8izHPYYXdhMp3DEz3m7jGavk234P2CNxntgwaCiKTKjp_8gIf-7VwtuiKBzmvjZV8-Yy_ob_HEpYXOAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
توضیح عباس حیدرزاده مداح درباره‌ی وضعیت مجتبی خامنه‌ای :
تولیت آستان قدس رضوی گفت که شب دفن رهبر؛ مجتبی خامنه ای ساعت ۱۲ شب اومد حرم برای دفن پدرش و تا ۷ صبح اونجا بوده.
وضعیت جسمانی ایشون هم عالیه، هم از لحاظ ظاهری و هم از لحاظ جسمی؛ حتی مسئولین هم پشت سر ایشون نماز خوندن.
همچنین ایشون نیم ساعت کنار قبر پدرش دو زانو نشسته بودن و گریه میکردن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71033" target="_blank">📅 09:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71032">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71032" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71032" target="_blank">📅 01:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71031">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIueV-_x19yUc3geH7CFfAPYyLgBbWh-RqF14dP0Q2RYnmFy8HbFVICrh0jBme6xnaVawXvnthp0OkviMvsyZRtFnnXIYo2OYKd7K2ElnxQkizyK5cfT_RdHzeN6PCr6QGhV6kBu45t5vOBnDnHTDew-l369rqrAkDyokz_B1OhTSfnZBwS2n9-gQNZwI9-nNZcUoLHKuEVZgZ3fna86gvaEef_a02vlIgmMJVJzkfLNjK2XwRD5D4MsHc8j2fsjfruoPTXWf_6CvthGpPRxB9ABoKJ5sQscllsYd_E0a0UlqfVlusqV2snAOLFM5iKcyLVdWFf6dCoo2UvmNf_F9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/71031" target="_blank">📅 01:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71030">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
⭕️
فوووووری/ همین الان با شروع مجدد جنگ دلار و ارز منفجر شد
😳
‼️
همین حالا چک کنید
👇
https://t.me/+S5Mn2k3LOf0wNjJk
https://t.me/+S5Mn2k3LOf0wNjJk
فوری برید ببینید
☝️
☝️
☝️</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/71030" target="_blank">📅 00:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71029">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa78544f7d.mp4?token=iTU-C0k6QW2OGt0uJJvAtImEDeChrNqVq_haAf6GOWyU5lUGTXau0FGDWFPxRahF0KkhBPMg6Txc6Vun9Yv-Ap8kJFnXHJaMJGurVwqgEIyQH_U6GnuboP1Vh-sTybkPkBat8y2UXWJMoShkfkALr2FxbEKDqKP9jjCO9VcmPxiezxd3KgT1rJNAF2UWH9vjcRiYeBlIVAHn_L4cDEIjyZ-lWnOgQEODxeexGksakwvN-UfDYzxrz28Hmb9p3198hMU1Uwy4vYyHQgjcm99CYm3kezfSKtOM8wakJMgI3XoZGO1-61CqtaULd5UBywCpOrrme_hc8POzc9ATNUziUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa78544f7d.mp4?token=iTU-C0k6QW2OGt0uJJvAtImEDeChrNqVq_haAf6GOWyU5lUGTXau0FGDWFPxRahF0KkhBPMg6Txc6Vun9Yv-Ap8kJFnXHJaMJGurVwqgEIyQH_U6GnuboP1Vh-sTybkPkBat8y2UXWJMoShkfkALr2FxbEKDqKP9jjCO9VcmPxiezxd3KgT1rJNAF2UWH9vjcRiYeBlIVAHn_L4cDEIjyZ-lWnOgQEODxeexGksakwvN-UfDYzxrz28Hmb9p3198hMU1Uwy4vYyHQgjcm99CYm3kezfSKtOM8wakJMgI3XoZGO1-61CqtaULd5UBywCpOrrme_hc8POzc9ATNUziUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇹🇭
ناو آبراهام لینکلن تو پاتایا - تایلند پهلو گرفت و ملوانان و اعضای این ناو برای یه استراحت  کوتاه مدت پیاده شدن
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/71029" target="_blank">📅 23:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71028">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14a1d4faa9.mp4?token=tHKcjadfaEqR--T0wYy9HbBJoY8c1-gaejAdchU5Jdt0OH2fiAamthnUonlY4f5-7QhuM3ozIBewR4zCpvNDPN6SQDeLuPS8F_xD6iZggtKdAT9Z1caLdqmxkSlsVb53D7UrpZ8PnMNuKVuc1GktIeYqrCdMSWlUuilQZs4e5lT3OgCiyXPtwAFDcbGWhCANIDmxtYUTuaJ0N3rPwL6o5f2EJFhtnoT77BXL6TdpejK3cSMF9yOLjyORNLBWpNLu5pBeFoircxQrhA5gurqzgiOhCyIsxBJzC1w_RuuTgBOGtwkqhIAcqN0vRcyd4TRKkyke6psN8tJ1oUNBAGPPiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14a1d4faa9.mp4?token=tHKcjadfaEqR--T0wYy9HbBJoY8c1-gaejAdchU5Jdt0OH2fiAamthnUonlY4f5-7QhuM3ozIBewR4zCpvNDPN6SQDeLuPS8F_xD6iZggtKdAT9Z1caLdqmxkSlsVb53D7UrpZ8PnMNuKVuc1GktIeYqrCdMSWlUuilQZs4e5lT3OgCiyXPtwAFDcbGWhCANIDmxtYUTuaJ0N3rPwL6o5f2EJFhtnoT77BXL6TdpejK3cSMF9yOLjyORNLBWpNLu5pBeFoircxQrhA5gurqzgiOhCyIsxBJzC1w_RuuTgBOGtwkqhIAcqN0vRcyd4TRKkyke6psN8tJ1oUNBAGPPiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان خطاب به پوتین :
قدرت‌های بزرگ صرفاً چون زور و قدرت دارن، حق ندارن بدون توجه به چارچوب‌ها و قوانین بین‌المللی به بقیه کشورها حمله کنن.
حمله‌ای که آمریکا علیه ایران انجام داد، نه مبنای قانونی داشت، نه مبنای علمی و نه حتی توجیه منطقی.
ملت ما با قدرت جلوشون ایستاد و اگه بخوان این مسیر رو ادامه بدن، بازم با قدرت مقابلشون می‌ایسته.
ما تو اون تفاهم‌نامه چیزی بیشتر از حقوق کشورمون نخواستیم و الان هم فقط دنبال همون حقوق هستیم.
ما همچنان به تفاهم‌نامه‌ای که امضا کردیم پایبندیم. اگه آمریکا هم به همون تفاهم‌نامه برگرده، ما هم طبق همون عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/71028" target="_blank">📅 23:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71027">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/180c2bccea.mp4?token=VdwMpOkAO872qkbYbDc0mNIvLRbsegCSA4nKTMW3ErX2M7mTxEwL87TywTZVcWGZ934t_Z154NWGotbvNMXJh24iyNJaMKrVyb0tpQCKLQ0SsTW_Fku6XO0fBzuf-ZQthjWm2LI2fXctHEGbOz5SBqdfcaGNOt2K9PTTr5ZLat47OEPfd4m-TlSqETEZ_10gGM3yy6iGKZrtbvkAkwTtaFeF7-KcMTM2psgMfHl2iPBnypObSq0lrMNLgIcoacbFpMIxkqG0aglONNCVo7gnXtQ4z_aacKU6A3H3_MtMgY6QXmDL0vOsTQiAkIUzmx7oKUsiOpXnqFTXGJ9V-H2mmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/180c2bccea.mp4?token=VdwMpOkAO872qkbYbDc0mNIvLRbsegCSA4nKTMW3ErX2M7mTxEwL87TywTZVcWGZ934t_Z154NWGotbvNMXJh24iyNJaMKrVyb0tpQCKLQ0SsTW_Fku6XO0fBzuf-ZQthjWm2LI2fXctHEGbOz5SBqdfcaGNOt2K9PTTr5ZLat47OEPfd4m-TlSqETEZ_10gGM3yy6iGKZrtbvkAkwTtaFeF7-KcMTM2psgMfHl2iPBnypObSq0lrMNLgIcoacbFpMIxkqG0aglONNCVo7gnXtQ4z_aacKU6A3H3_MtMgY6QXmDL0vOsTQiAkIUzmx7oKUsiOpXnqFTXGJ9V-H2mmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره انتخابات:
من تحت تأثیر انتخابات نیستم. خودم نامزد انتخابات نیستم؛ حزب من در انتخابات حضور دارد.
به گمانم حزبم به این واقعیت احترام می‌گذارد که ما اجازه نمی‌دهیم ایران به سلاح هسته‌ای دست یابد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/71027" target="_blank">📅 22:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71026">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53f1ce3ca7.mp4?token=HrwIoAhFdjZZeBgVBRv2WDsBpPuh-lv4IZG1dDpSH1wH_WljjquHEcxyx1hjIHGvyQRZC9_MwtWnygQ63j71Co4BkoSAKOc8T5YmGpU_fPZXQ09NWR5Nkm4fhrsIGjnjA2-oZW6Uo7YrmSxyi8OJpjCtF1wd33vWJf1GVuEeWcauGjl7MIAYHVlTVPxs0tA9g-I0z4PK2fBiIKZ28mU7G6W7WsXIUP4cHk8tuOTuv6qm8dFXQuZ5m6ECciVUvAxRgdgdwggnimY8F0ddCUVOfxSGFZ1TBrUjBzaRwOnOq4mRctSvoh_y0wwShNXq4JbuMgq6B67ivElapR-SXpydGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53f1ce3ca7.mp4?token=HrwIoAhFdjZZeBgVBRv2WDsBpPuh-lv4IZG1dDpSH1wH_WljjquHEcxyx1hjIHGvyQRZC9_MwtWnygQ63j71Co4BkoSAKOc8T5YmGpU_fPZXQ09NWR5Nkm4fhrsIGjnjA2-oZW6Uo7YrmSxyi8OJpjCtF1wd33vWJf1GVuEeWcauGjl7MIAYHVlTVPxs0tA9g-I0z4PK2fBiIKZ28mU7G6W7WsXIUP4cHk8tuOTuv6qm8dFXQuZ5m6ECciVUvAxRgdgdwggnimY8F0ddCUVOfxSGFZ1TBrUjBzaRwOnOq4mRctSvoh_y0wwShNXq4JbuMgq6B67ivElapR-SXpydGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره ایران:
دیشب حمله بسیار سنگینی صورت گرفت و ما آماده‌ایم هر زمان که بخواهیم، حمله دیگری انجام دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/71026" target="_blank">📅 22:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71025">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a230c24bdf.mp4?token=W5ap3DZS4iNLeTtdiEnu5YG97pdnqOl0bni3zihPQPI5rloMDlzKj63MuTFK5eBoRrwY9cwoHmifqDNBS8XQBBhQnTJ8G9DaJS39CtRZgKkoyzQCZRH9O6p-DuDYyHChYxdiFaKAIOQf_2t1YQHzlBhXwaW6OJ10oc4Iy2OCw1bNBX8nCbZMYAjvLCT3RTIlD5HaQuafXGd45y8ktd-rMZir3o89OAaXbt59hvSqJ91Zw8ZIfUxWU0fXXKT1U8VjTZmNpCACmG6RyPfbrHIt-hd7Otld2kn5Wyl0CVhcuKylB5g7HARTaVHNzJL9-64AvtyiuCd008C0M0SUiO9S9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a230c24bdf.mp4?token=W5ap3DZS4iNLeTtdiEnu5YG97pdnqOl0bni3zihPQPI5rloMDlzKj63MuTFK5eBoRrwY9cwoHmifqDNBS8XQBBhQnTJ8G9DaJS39CtRZgKkoyzQCZRH9O6p-DuDYyHChYxdiFaKAIOQf_2t1YQHzlBhXwaW6OJ10oc4Iy2OCw1bNBX8nCbZMYAjvLCT3RTIlD5HaQuafXGd45y8ktd-rMZir3o89OAaXbt59hvSqJ91Zw8ZIfUxWU0fXXKT1U8VjTZmNpCACmG6RyPfbrHIt-hd7Otld2kn5Wyl0CVhcuKylB5g7HARTaVHNzJL9-64AvtyiuCd008C0M0SUiO9S9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره ایران:
یک ضربه کوچک بود، اما دیشب ضربه بسیار سختی به آن‌ها زدیم.
ما تمام تجهیزات جدیدی را که سعی داشتند در امتداد تنگه هرمز مستقر کنند، از بین بردیم؛ تجهیزاتی که برخی جنبه تدافعی و برخی جنبه تهاجمی داشتند.
آن‌ها تلاش می‌کردند موقعیت کشتی‌ها را رصد کنند — چون همان‌طور که می‌دانید، قادر به دیدن کشتی‌ها نیستند؛
ما تعداد زیادی از کشتی‌هایشان را نابود کرده‌ایم
آن‌ها نمی‌توانند کشتی‌ها را ببینند چون راداری در اختیار ندارند؛ چرا که ما رادارهایشان را منهدم کرده‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/71025" target="_blank">📅 22:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71024">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991fb05c67.mp4?token=B2qw9O5JUHPQdsg1VHPFZFuFAJ6t9ahG8hGHu7PwUMv2q36Pu7lkJReghG8Ew3IHRPPD-frESTdEM4XBQvUq0AEGNgYKYi3WBfPknZC1ncubHNrFlCZ5xkjibW5QHsXaZ7tI6DZviIQeKtwAVbNCnxIGgl0luR2qVIX2JKISba5ps9Y96yRZB4KWhhTh6LHkHcTOtr__dtMMQ67hdmji4Q6jgljKHdZ1__JMCVf03UnufYo3HIdqy9Cvajuq_tqrtb111V-CZIQ06cQZaaRlSUFlTZI18XZTzSSzqe9vrvcBp41neJKedz3mrYoqiv7ZbAjI0Zt356LD5LWZRkClbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991fb05c67.mp4?token=B2qw9O5JUHPQdsg1VHPFZFuFAJ6t9ahG8hGHu7PwUMv2q36Pu7lkJReghG8Ew3IHRPPD-frESTdEM4XBQvUq0AEGNgYKYi3WBfPknZC1ncubHNrFlCZ5xkjibW5QHsXaZ7tI6DZviIQeKtwAVbNCnxIGgl0luR2qVIX2JKISba5ps9Y96yRZB4KWhhTh6LHkHcTOtr__dtMMQ67hdmji4Q6jgljKHdZ1__JMCVf03UnufYo3HIdqy9Cvajuq_tqrtb111V-CZIQ06cQZaaRlSUFlTZI18XZTzSSzqe9vrvcBp41neJKedz3mrYoqiv7ZbAjI0Zt356LD5LWZRkClbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
ما هر کاری که آن‌ها انجام می‌دهند را می‌بینیم.
آن‌ها حتی نمی‌توانند به دستشویی بروند بدون اینکه ما متوجه شویم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71024" target="_blank">📅 21:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71023">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/504db2064f.mp4?token=Xfy4FdsIme3v3KANaKPTcGIqNTchueK6rNKK4w5WiyhlhMHBMNmN_Y6-9KAFF722Pd1lqoVINBlNyulkm0INRnTORKzeCdiuCXoWSQmzGNbckaE20pVjGcFpy-YPxcAF_HcCqr9_mLHQrkMqODAvKjRO8YQMyQBu3_cqhVkADkEvTICvgK_Hqiqj-VJs6Am_HQ1s5SCSbaBxGd6tVlczB-v8Eg0nKK_j2Cv9tNnJ3z0S5XCDkUIxCmNB5j5u0xpaIe2YwsC0w6WMUDRnBbfRx0X2y3N_Bhm8DhLc_6d6jP-xQqtfKzKaZXL6IKA6blmHCdNFN_kP2gu_xZhDVHv5UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/504db2064f.mp4?token=Xfy4FdsIme3v3KANaKPTcGIqNTchueK6rNKK4w5WiyhlhMHBMNmN_Y6-9KAFF722Pd1lqoVINBlNyulkm0INRnTORKzeCdiuCXoWSQmzGNbckaE20pVjGcFpy-YPxcAF_HcCqr9_mLHQrkMqODAvKjRO8YQMyQBu3_cqhVkADkEvTICvgK_Hqiqj-VJs6Am_HQ1s5SCSbaBxGd6tVlczB-v8Eg0nKK_j2Cv9tNnJ3z0S5XCDkUIxCmNB5j5u0xpaIe2YwsC0w6WMUDRnBbfRx0X2y3N_Bhm8DhLc_6d6jP-xQqtfKzKaZXL6IKA6blmHCdNFN_kP2gu_xZhDVHv5UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
بیشتر مردم نمی‌توانند به این شکل آدم‌های خودشان را بکشند.
بیشتر مردم سعی می‌کنند منطقی رفتار کنند، گفتگو می‌کنند و بعد شاید کار به سرنگونی بکشد.
اما در ایران، آن‌ها مردم را می‌کشند.
وقتی مردم برای اعتراض بیرون می‌آیند، آن‌ها را می‌کشند؛ درست وسط پیشانی‌شان شلیک می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71023" target="_blank">📅 21:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71022">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c319507bcf.mp4?token=fBTCTDLU6QOO6JGMhKnidLqpxv6NXlWfUECkeXksegL5fuD0ep-nO8qGPzXrBSjtHq9qVJyD1bImC3YzXD9toCLNL3E5_lA_3zLL98lBzivTYkC3l_O9WrRBVXZ5i3B1TvP6huA42WLpUejKzqi40cFEip-MCChc8GREQ_2JWrFLIm6TwFboyHRlEJyyDBtWqPLtpPbqitu5p7AtpEzHxChqudPnDAzTKbzn8eP8EvVj3IoFrDM3OU2tV4Iyl1bgvv_ZZxM9oeB35g8vwO5vO2pFKexvbnAjhQntVIbsT7HiQRSPZBnvTB-k2KL0ZK7J5wN-6B_jDS8zCGQq2P2Wcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c319507bcf.mp4?token=fBTCTDLU6QOO6JGMhKnidLqpxv6NXlWfUECkeXksegL5fuD0ep-nO8qGPzXrBSjtHq9qVJyD1bImC3YzXD9toCLNL3E5_lA_3zLL98lBzivTYkC3l_O9WrRBVXZ5i3B1TvP6huA42WLpUejKzqi40cFEip-MCChc8GREQ_2JWrFLIm6TwFboyHRlEJyyDBtWqPLtpPbqitu5p7AtpEzHxChqudPnDAzTKbzn8eP8EvVj3IoFrDM3OU2tV4Iyl1bgvv_ZZxM9oeB35g8vwO5vO2pFKexvbnAjhQntVIbsT7HiQRSPZBnvTB-k2KL0ZK7J5wN-6B_jDS8zCGQq2P2Wcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
تا سه ماه پیش، پنجاه‌ودو هزار نفر از معترضان کشته شده بودند؛ می‌توانید چنین چیزی را تصور کنید؟
و حالا شنیده‌ام که احتمالاً بیست تا بیست‌وپنج هزار نفر دیگر هم به این آمار اضافه شده است؛
یعنی شمار معترضان کشته‌شده به حدود شصت‌وپنج هزار نفر رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71022" target="_blank">📅 21:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71021">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78e478b4b0.mp4?token=S-XFg9UVewvt_uREGqFX7wDNpOle6CksjZY7Dl_tWOXjPFhJ5ZViPYSM_kw5TFsIkrus0VwLtmZ8IHWWKcC4Y2MUHfE1c5sKx7SGlfjlM4sRJbWu0fYzIoowGDTvARa2r5dTwuXXxpuf1PSmZ4ZTQO90myTFxIX_-tSZwMM7xpStl7ZRM7y_oGtWUIOSSKGU8ujlHkDpxFVm9HiEz6erfVzpFVAtM1qMuqpaLFhjksMdANv9E4HNq4mzUEvgR7fnz6swnNxKPVZvIVv16PpRrxRJl60xFrzTdMyhMJ8UNJo9OpaHekmMuU-0JRsDCymA6nByO8n1xFZDu473L71bmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78e478b4b0.mp4?token=S-XFg9UVewvt_uREGqFX7wDNpOle6CksjZY7Dl_tWOXjPFhJ5ZViPYSM_kw5TFsIkrus0VwLtmZ8IHWWKcC4Y2MUHfE1c5sKx7SGlfjlM4sRJbWu0fYzIoowGDTvARa2r5dTwuXXxpuf1PSmZ4ZTQO90myTFxIX_-tSZwMM7xpStl7ZRM7y_oGtWUIOSSKGU8ujlHkDpxFVm9HiEz6erfVzpFVAtM1qMuqpaLFhjksMdANv9E4HNq4mzUEvgR7fnz6swnNxKPVZvIVv16PpRrxRJl60xFrzTdMyhMJ8UNJo9OpaHekmMuU-0JRsDCymA6nByO8n1xFZDu473L71bmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما امروز در «تروث سوشال» (Truth Social) نوشتید: «مردم ایران چه زمانی قرار است قیام کنند و بجنگند؟» خب... اگر... اگر این چیزی است که شما می‌خواهید، آیا سیا (CIA) را برای مسلح کردن ایرانی‌ها اعزام خواهید کرد؟
⏺
🇺🇸
ترامپ:
خب، پیتر، من نمی‌خواهم چنین چیزی به شما بگویم. خیلی دوست دارم این را به شما بگویم، اما... اما گفتنش مناسب نیست.
ولی... منظورم این است که من وضعیت دشوار آن‌ها را درک می‌کنم؛ آن‌ها هدف شلیک گلوله قرار می‌گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71021" target="_blank">📅 21:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71020">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):   گزارش تأییدشده‌ای مبنی بر درگیری یک نفتکش در یک حادثه امنیتی دریافت کرده که منجر به دو مورد تلفات انسانی شده است.   @News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71020" target="_blank">📅 21:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71019">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8edb01b99f.mp4?token=e67GI4fsDjLl8AV5Iuhf-HaesldS4NHuWBf8eglNpDrx4Sm9jE2IU1NOVVCE8ey1ZPP8dFxp5NWL6-gC4SXstDc6DyCiZZSON8OOijRC1uoJ_NKNOJiK4eAQspTQHCShN9TwtuerDNBMyBJ7ZOKkzGo3gl2AarxL5ielKWdEVZfqE52mtaU_40k9wOwX4Beug5_u2_88SYSNcXvH3k0fHxTYyH5rm-9E1enAItz_vZ7aRPAUH2j_yu7PXeNm6QVf-Y46Rv8bJi1w2qy_fHYqvpjigb2X9MTT2wGUV8eAQRGznPR8dF8IAfK0T3LxXd4RPDqCMDX8dHuC9InSGOKrfaBSTccvzUoK6SbQzZcyOfhr1aIId5QXFsWpIH0DNc8fyK60KowncoRJxjc1wvHKfw34itll0WVp1J5DdcdnxzUPqbQlED-g49AYZa14DKt8974POzQn5t2ZAQ5Wqc3Zj_59gFXP1Ga1r9AlT8S_O1igdNtnsyT4h9c9eDBM7RnzgxiawQ0nDXq0BX5ZOpSV-ucB_TCUCgA1Dohezyko-FRDfhDNA2hlXzhemZJtsUqJzYdtSTWOERoqyNrjk1rQtBlE3Kr1KIhQ7k7vepgyVOdNeacjLl1W_9eVSTxuZkW52reRhavrvx8X3cjqOVjyxpi6FAqoVIMlI7EhpUkUZ2E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8edb01b99f.mp4?token=e67GI4fsDjLl8AV5Iuhf-HaesldS4NHuWBf8eglNpDrx4Sm9jE2IU1NOVVCE8ey1ZPP8dFxp5NWL6-gC4SXstDc6DyCiZZSON8OOijRC1uoJ_NKNOJiK4eAQspTQHCShN9TwtuerDNBMyBJ7ZOKkzGo3gl2AarxL5ielKWdEVZfqE52mtaU_40k9wOwX4Beug5_u2_88SYSNcXvH3k0fHxTYyH5rm-9E1enAItz_vZ7aRPAUH2j_yu7PXeNm6QVf-Y46Rv8bJi1w2qy_fHYqvpjigb2X9MTT2wGUV8eAQRGznPR8dF8IAfK0T3LxXd4RPDqCMDX8dHuC9InSGOKrfaBSTccvzUoK6SbQzZcyOfhr1aIId5QXFsWpIH0DNc8fyK60KowncoRJxjc1wvHKfw34itll0WVp1J5DdcdnxzUPqbQlED-g49AYZa14DKt8974POzQn5t2ZAQ5Wqc3Zj_59gFXP1Ga1r9AlT8S_O1igdNtnsyT4h9c9eDBM7RnzgxiawQ0nDXq0BX5ZOpSV-ucB_TCUCgA1Dohezyko-FRDfhDNA2hlXzhemZJtsUqJzYdtSTWOERoqyNrjk1rQtBlE3Kr1KIhQ7k7vepgyVOdNeacjLl1W_9eVSTxuZkW52reRhavrvx8X3cjqOVjyxpi6FAqoVIMlI7EhpUkUZ2E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
#فوری
؛نتانیاهو درباره ایران:ما رژیم ایران را سرنگون خواهیم کرد.
ما این رژیم را شکست خواهیم داد.
🎙
مجری؛
«شکست» چه معنایی دارد؟ آیا سقوط خواهد کرد؟
🇮🇱
نتانیاهو:
سقوط خواهد کرد. ما آن را سرنگون خواهیم کرد. این رژیم به هر حال در آستانه فروپاشی است.
🎙
مجری:
آیا رئیس موساد، رون گوفمن، برای سرنگونی رژیم ایران تلاش می‌کند؟
🇮🇱
نتانیاهو:
تمام نهادهای ما، تحت هدایت من، برای سرنگونی این رژیم و شکست دادن آن تلاش می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/71019" target="_blank">📅 20:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71018">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5723b906.mp4?token=M9hZe6UecaDhkHlrSMMxv3Zc1JYqP5Zv9gTZsEE1okjxd3pc4Agx6SxutPehLUzGsBW9SqRhHaonZ7iK_1MM9rXXCagOjCkjfLxprwL7vI5ENN4dBX5zUf4F3YwknoNIoenMkmtQVePwI1vfQHI2kR_EGgkKslb8zOWKNdDRgbOksWKUDbOlPgK0lZPGNLnSAWS907OQxVFvz9CXDTjwCd14zeRHq9wBbpgEHEJToZpfiBJZ9_c5arRZqK-6fJGWpKim5sQoIJIAtRiL_Qhu4_DicSFovavuzc51KiooTA0ghKX0XA_VKOZ3M-W4ru9I8eNxZexCickmLo3nL8Uo1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5723b906.mp4?token=M9hZe6UecaDhkHlrSMMxv3Zc1JYqP5Zv9gTZsEE1okjxd3pc4Agx6SxutPehLUzGsBW9SqRhHaonZ7iK_1MM9rXXCagOjCkjfLxprwL7vI5ENN4dBX5zUf4F3YwknoNIoenMkmtQVePwI1vfQHI2kR_EGgkKslb8zOWKNdDRgbOksWKUDbOlPgK0lZPGNLnSAWS907OQxVFvz9CXDTjwCd14zeRHq9wBbpgEHEJToZpfiBJZ9_c5arRZqK-6fJGWpKim5sQoIJIAtRiL_Qhu4_DicSFovavuzc51KiooTA0ghKX0XA_VKOZ3M-W4ru9I8eNxZexCickmLo3nL8Uo1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از دیدار محسن نامجو با مجتبی خامنه‌ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71018" target="_blank">📅 20:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71013">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vOgydSK1sYkRgOWQi3k7D9jDeWbFq1SNE57aRvHqpjq_TggirpIo2eh4g9k3eIYp6XqCEJaAG3Pg4QnE2D8nFCVksMiTl-xdPjAZ2_XvCGQaM5r1xw4wP-6tftxkmofGEFf2NAHtRKVSTYXJM6xnXsEn0sR64QkgkFKnbDLpTkYQY0rUcnYGvwTOi6uDc6ilCkP5wPSc3Pqqzckog4AkgWJHvESzaUxHNn84knV2kRq2yPyjuN63mo4karo8CH7Hu_2v4xgmdSX1PZJOoH_ItuPFuzC6y1YNzLFs6gfrq3B0sHyl_19XZCw43yR-XQ8jLbQNUQ0dUFFEug9btlXsbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dNwVDVNTfOaPCJ7PotaIocLH_9omtr25V_K_6uVdwxH98a1sWfrIBSUCSgJUVExxkgA4HriDboP3UvILB9QP6E1EVzbhkZpu8rP7bWIu6VJ0gGb-5WQ0BcHfBjocBIWnGTDQHkdXSKuemGCXdVlRET-lb7jwqfhUm-QZfB8HcTwYLOkkFDsi57nlGJ2Ia1aYkpTWnSrGWgTCOvmzzehm8qPEBNpzpPaCqoonD_z1O0bui1467ytFcGuBl95t7VkhPyJMbTRq5MZcEYAOqzCz0sLi1fYknzPzMIaELc6PF5t-sWrQnA5bji53xzbz-WziASuMbnuYgoMDO3XDaiwgpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21e8023466.mp4?token=YLlkwXijYPVo77N9Q-2ay6QFUklW7zndQ-VqzNymiFZHNlhOGU9kWHI-XmvD8T7y7Gxom3k2e7XF6QCKbFKG8aMzzQpgERDS9WZc-42brpDIZ9DaWH_8sn7mxIs6mcmcvpJOSpxM50bOuBuMExtNjpYViR-GqgAYihqhN6RRaoHYPNpEtBkcDcl-PP7kN2fHv1LF8-ORmZOL-QvhhiJMWHOnpmpsRtL6wrusm6o2bx2cKvky9NqH8YfU9DY2queC2B3NnTfXFtfGQShuEgrkBBhGSr0MRcdj1Cn8S-044XgHhvAubTYiJAuLeHcikVtjTAQFyS3UVj44dCnKLM91mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21e8023466.mp4?token=YLlkwXijYPVo77N9Q-2ay6QFUklW7zndQ-VqzNymiFZHNlhOGU9kWHI-XmvD8T7y7Gxom3k2e7XF6QCKbFKG8aMzzQpgERDS9WZc-42brpDIZ9DaWH_8sn7mxIs6mcmcvpJOSpxM50bOuBuMExtNjpYViR-GqgAYihqhN6RRaoHYPNpEtBkcDcl-PP7kN2fHv1LF8-ORmZOL-QvhhiJMWHOnpmpsRtL6wrusm6o2bx2cKvky9NqH8YfU9DY2queC2B3NnTfXFtfGQShuEgrkBBhGSr0MRcdj1Cn8S-044XgHhvAubTYiJAuLeHcikVtjTAQFyS3UVj44dCnKLM91mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
حملات جنگنده های اسرائیلی به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71013" target="_blank">📅 20:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71012">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/600c9063c3.mp4?token=mZFZmlhwMGpyTm_NPGKV-vSWciDnXLH0LtGxiFh5g0Y0mVCd6OOYJepo-hhKifXqs21Uc_h1_PqsbVvWHjnpMN5aEunXaeOVvPpN9R9p3GW84lwlzZZ1789eWvCofQvpHMNZBOiVvTCBRou2DLu4LGLkQukTkDHZhV393cFeijWn1jyaqXCik1zhm_SRLQ-dSLClDdkJr96IkZ1ZkHjZBepGRsJny-tN2Qp8AxSQWCS33Q9j4O7clze_WLwzbQTBR_f-B-h0OEKRVnMw_Gwf2gzX1WVD3rDdAIAy2Of5cTK27UXe1tT8hbB4BJqxrFzaxqdtyPDEfsSaDKWa0PiC8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/600c9063c3.mp4?token=mZFZmlhwMGpyTm_NPGKV-vSWciDnXLH0LtGxiFh5g0Y0mVCd6OOYJepo-hhKifXqs21Uc_h1_PqsbVvWHjnpMN5aEunXaeOVvPpN9R9p3GW84lwlzZZ1789eWvCofQvpHMNZBOiVvTCBRou2DLu4LGLkQukTkDHZhV393cFeijWn1jyaqXCik1zhm_SRLQ-dSLClDdkJr96IkZ1ZkHjZBepGRsJny-tN2Qp8AxSQWCS33Q9j4O7clze_WLwzbQTBR_f-B-h0OEKRVnMw_Gwf2gzX1WVD3rDdAIAy2Of5cTK27UXe1tT8hbB4BJqxrFzaxqdtyPDEfsSaDKWa0PiC8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مردی در نیویورک آمریکا پس از برخورد مستقیم صاعقه به پایش جان سالم به در برد
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71012" target="_blank">📅 19:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71011">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kmxg76Ebh34zXLoAQIi_YWiWStxklrcMEqsgygr9NxD668A1pTAF5SPZvfKDi83u2-idTbkZua_GFz6_opAUODZIU9PwHod9y0bjWGad4QctklOtBhrB3PAPpV-l_1D-D6aMUQRAS7BdRuZDvWHXWI96nBq-NGgyyu2h7uCgTYwhIfX0pybSNCUTyGYme2ZyJMLOEEqFUcf8MonntDyKXluvBuNZqpZ7R6da55qkVxUQ1KmLYN0jIMAJFbEI-MuU-358mYKqSSb-wOIgMay4x8dwJ7kaFEHkqZOVPqRYyqS4wrCVsvyB-L33EfO3J688CRoHiJ-USJKYNuZ-1XLu8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ در تروث سوشال:
حالا که تنگه هرمز تحت کنترل ایالات متحده است، آیا باید نام آن را به «تنگه ترامپ» تغییر دهیم؟ این تنگه هم درست مثل خودِ آمریکا، «داغ‌تر» از هر زمان دیگری خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71011" target="_blank">📅 18:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71010">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اسپویل:
سپاه دوباره موشک می‌زنه و ترامپ هیچ گوهی نمی‌خوره
#hjAly‌</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71010" target="_blank">📅 18:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71009">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f635b0ff.mp4?token=SXrweZ6kveXY49xnsiXE8B6HWgHtuERzecg60Zvu8-Gbref5YAGNuCB_L6K0FH_qPm7Fhq48JRWmtd5OpLLq3aUyz0U2At-W5q3WuDPHcyG9EkKvv4EbzOa_LLAb76y81ovUGQGw5DlAX0A767rHup6kSzw92ygy8OjfV42zFX42GN_R03Q7QYpe_PzsNW0qegXUIbPZj9rHH71UcKN1AS-qr015F3MrA9Wk-ZtMVELYTUybhaT8CMKIcHCZ0S5v5ww-9EhXiXCH4U1XKrfLjSNTnsaOoXVdcLDu1JbfmFGRhw4mtQkS1ma0WaXFFp3U4K6OVhbDl1eslxe3r-QaXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f635b0ff.mp4?token=SXrweZ6kveXY49xnsiXE8B6HWgHtuERzecg60Zvu8-Gbref5YAGNuCB_L6K0FH_qPm7Fhq48JRWmtd5OpLLq3aUyz0U2At-W5q3WuDPHcyG9EkKvv4EbzOa_LLAb76y81ovUGQGw5DlAX0A767rHup6kSzw92ygy8OjfV42zFX42GN_R03Q7QYpe_PzsNW0qegXUIbPZj9rHH71UcKN1AS-qr015F3MrA9Wk-ZtMVELYTUybhaT8CMKIcHCZ0S5v5ww-9EhXiXCH4U1XKrfLjSNTnsaOoXVdcLDu1JbfmFGRhw4mtQkS1ma0WaXFFp3U4K6OVhbDl1eslxe3r-QaXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ما اکنون کنترل تنگه هرمز را در دست داریم. ما آن را کنترل می‌کنیم.
دیشب ۲۸ قایق و کشتی را از کار انداختیم. ما کنترل آن را در اختیار داریم، آن‌ها هیچ‌چیز به دست نمی‌آورند و ما آن کشتی‌ها را نابود کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71009" target="_blank">📅 18:51 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
