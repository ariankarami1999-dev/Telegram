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
<img src="https://cdn5.telesco.pe/file/YY4PXxtnkFfUcBm438lPy88QxJ3ZB-XJtLVlCG_lRKQSEBd2FqDRQcc-sUXUprEtIgE3MPjP0iwB9cN8eDkvkwCzqFeArgeuUOnYLwvzOi6YEDTSjuj4SPH50psm_53PwGglGnnpbSH8ohTwHkmMrMP02yMWvr_BLHtnjeoaqL9fptQo6W4XhdQBz_xVMYlEPODUDd4qYDYOyEZUm2_CSVAd8NkmRKga-_tnE7fcZ8BSOoDbd6nekoCjqABj7ziGRuUxQvizQvjK0BXixec0B73jzrED1j8WbdybKgOYetKlH04szBqXt_Z-x9EEeNQpBaHjKN5TKwAMw0tjzp2xZg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 515K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 18:55:34</div>
<hr>

<div class="tg-post" id="msg-102260">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DtDY_N04Sz-pAwXzip2GFDjJbWZay2W7ISJPMqFWFbDoiFE5E_WtZMHfnawaQY8Q3qwiCx3F9-K1LBljKFiTpNLko5OqRlniBwxeLV8ep1nBf8Mhp6L0h88mVqqDQ6aEoPQYqXgpAOl8W3LrDuH5l4QZ_aTFe8FH5T8vOEU9uqpS3Sws2wqMGmv6FXVPx5QUzA6TN87DZAfu9Rbwl2r1wx8heWzKFbMmCAR0C6XOzYJwisXmE7r9b223LQvZh0I-9XRpGTvPsqFFzeWE_DbuagpJtLWLYzr09e-CsmiIFK9IGiQemwkvGnTmeWLYoklbIKewCPuaWyE2ENHytZV4Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Brp7PoXsq2oiFhkV4PejyTw-sOemhLzn600pROQNT4-bZjOXNC7m59o3pI39QnT4vtnWFCralPI19fApask5j_ObJOnY816L7tGO4styhkaIrNBbVLjRK4la3NbGZkVwLlqu0RSBluyK61alEq6WVa8m86otNoe2rD6J18GxlIQdTCY7LsIYtqINoJhel1LDdWoSM50yMI7AZ-oMm2azQ74lainMizuz0UMK7GPpkoljM33ynmpbdH-F8n_tUwk7-ik3X9Beo7vWVQvU2kKBbnWq0L9ktls3MuvHAGvzZwEH4gIjx5jy9MiiP_iybKQLcS2oo5p3iopvVSgkHWA7WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lnmV2aKlbA3NKaeOdHUM_MifGbLfgjBaBwq5csaEMESSF-gCFrhDC1JzUxiU0WdYZdMk6jxOJ90QjhA1cnc07bARlQ4IEFcE5QaeTyOQtqDzf7oikZ_ERoA4zeWICfI_Djysoho3OpdVyyAQ26zMnZFLQvx_CMD5iCg8gK_cgxV3RK4BKSkMNnCpWOv1894pNm5Fit8Ju8Bf13IEd-bubIsmUmItqBN9dgi4NfST6Jeb0vhaWw-nBmkZqIhmUJP38mGVsoWQDLSn-A6JKjiXVsBX8P91ADxbLa8hanox_hTgrcqOVuGfej9-E9dUqCzDo6C64f5Ok8Y30TLRiAkM2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FCNNoRMsZg9NmogMF3s-6qEfDY4PT0QcOMv-y78mLPGmezigkFQ4iuQ85UFx880s78nVqF18kroF1145urY-iL56Er23hAA8T_4rKhd9cjcImirmPJ26-q3hB3Ikw-Oi2MymhFUIY2myBywk94K9M0-LspxpyE8_-gppd7kBmZESqOw7-CDdmoQiHDg5lCvnuvxCTsuPBDrCQw61GY5_-PQZtClt0nH5hPJkAd3cuImXSl2bcA_CFNJVAUxoSyS6DIU_qVdewPOZBwDhlFBQVWg_abi9G8C2Rdo18FWYXLoQd7M_fNqzFJKwb0AaJ0ZdtSF-fa1hB0MrvDDs7N2_QA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امباپه و استر اکسپوزیتو درحال لذت بردن از تعطیلات که شکار دوربین‌ها شدن.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/Futball180TV/102260" target="_blank">📅 18:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102259">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMj5LnjhZDgTnm3otnzXSTdAwbR7COjnT_xz4O1qYbmU6b3G1SPnOpKnoyGlVtzCt-9ykjY3qJ8f1WGBJ9fKhEjiscfM5XycAN0gF_UG2Ja2ABpsoealEB3jE_HastBhyasJIaEysUhroauGCt4IQTiQJx6GjmcSWp7DIT7fcyM_OfBBpmhKTY6xhepgiRmmj2sAIY-zT2CIainp7QGxUzlaXgdo4slHt32fJBC0JQgbFmrIS598ydCGDunCMg6Jdubx1spcDdZOyMz93FPiT3jEeXR-BXbbbXTX6zk_26Jcr79W0qMDsGXPP2KcmLLLGVVqCw1ydWRnYjSrB5qsuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
می‌دونستید؟
چلسی در سال ۲۰۱۴ با ژوزه مورینیو به جذب لیونل مسی نزدیک شده بود. گفته میشه آبی‌ها آماده پرداخت ۲۵۰ میلیون یورو بودن و حتی با اطرافیان و وکلای مسی مذاکره کردن تا او رو به لیگ برتر بیارن.
اما مسی و خانواده‌اش تصمیم گرفتن در بارسلونا بمونن، چون این باشگاه برای او چیزی فراتر از فوتبال بود. تلاش رومن آبراموویچ هم در نهایت بی‌نتیجه موند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/Futball180TV/102259" target="_blank">📅 18:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102258">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b74b82c7.mp4?token=Je1CiC0t29W2ABU0pVsfts5_lKsRQa8TEsE5f0Iyj7AzFtH6K1BwBtGoY6QnW7EtsTP-Lnwt3wovjYN5SuDQv0gJ5ppiCc9-IMu3VhF52-8g870NnyorHaB1G-PjHzipGrietd1khd2cjDaLyJC2h_IhCOETChtY2mkiBUGDvlHb32-yPcm7kXL27Wk08UvKY9RVtpVkorEtE9Jeng7xO_tVsKpe09HLAJoSJcRybpU2l8_7WCKFcy66djoDdqWaNP-qKLDERrrQdFxB9JdA4fLqaSoRtgFTZGHVznXlnrH0QNqaUHwwNRcaV37dwFZZldrzN6pVlHXTBxxfLB7bsrj3v1Z_f1YXVUJeqS2bEIHgO8OMl6eo1NRS8WJs4hNQx4KObGSSWsrQk2MUg9urzzvwX5Zi9IrCBjGyQL610BUvtS-mk6rRHRrjUVtjqz8M6R57RZLqZSUwMFS8fIjj9QAlET7uiLCHi5pm2gUJWaEElGmnQCR9_8pL3lDSi-phCDBfFm2BBih7FetbMn5nW4wCeN6fMqvvQdBxb68kxwAq9VPK_07GPP3KMuKVYmp2u2q3q5iDE2i15ac5dnm5oaU-y769vbxjc3CxwMA3EGSbvzUlmPtfrbpuOz1N1jGmtBA_QP2ztRkWBQCuI35sTlaV2tmQsLiKcLyqqgIEdmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b74b82c7.mp4?token=Je1CiC0t29W2ABU0pVsfts5_lKsRQa8TEsE5f0Iyj7AzFtH6K1BwBtGoY6QnW7EtsTP-Lnwt3wovjYN5SuDQv0gJ5ppiCc9-IMu3VhF52-8g870NnyorHaB1G-PjHzipGrietd1khd2cjDaLyJC2h_IhCOETChtY2mkiBUGDvlHb32-yPcm7kXL27Wk08UvKY9RVtpVkorEtE9Jeng7xO_tVsKpe09HLAJoSJcRybpU2l8_7WCKFcy66djoDdqWaNP-qKLDERrrQdFxB9JdA4fLqaSoRtgFTZGHVznXlnrH0QNqaUHwwNRcaV37dwFZZldrzN6pVlHXTBxxfLB7bsrj3v1Z_f1YXVUJeqS2bEIHgO8OMl6eo1NRS8WJs4hNQx4KObGSSWsrQk2MUg9urzzvwX5Zi9IrCBjGyQL610BUvtS-mk6rRHRrjUVtjqz8M6R57RZLqZSUwMFS8fIjj9QAlET7uiLCHi5pm2gUJWaEElGmnQCR9_8pL3lDSi-phCDBfFm2BBih7FetbMn5nW4wCeN6fMqvvQdBxb68kxwAq9VPK_07GPP3KMuKVYmp2u2q3q5iDE2i15ac5dnm5oaU-y769vbxjc3CxwMA3EGSbvzUlmPtfrbpuOz1N1jGmtBA_QP2ztRkWBQCuI35sTlaV2tmQsLiKcLyqqgIEdmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🔴
۱۰ گل منتخب تاریخ تیم منچستریونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/Futball180TV/102258" target="_blank">📅 18:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102257">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEJMNlow4DcwW_9119Wz1nFaHdTkgP-wjRKoD1boZ8n4Ch5BJrEZYQMkjhul1mh3YvgTejVG2oQ-sL62JF6myyxiVy5nk_lv3cpB1QRQDDyWB3v9gzrIFdU0oTeEKMkb415yOdug7BLF536S-iywHTUTCpNK0NknO8HwTSPBrspEx1ioxtKw2x9bYfHHlBqdaE58ST-4LXu_vqgNv0R3lYZHF7YZX1JDcfTvbcKNFsUVQLaUxeKLJz55SpOz_nWZXhWaydStiONsS6EG6GzFLtnSP45BID4j8Y3yYDafc8ei7RYUAtDmhB6ks0zJxrNTFEu9nIkjrY4TvgKJVkxfkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⚫️
#فوووووری
؛ فلوریان پلتنبرگ: کریم آلبگوویچ ستاره تیم بایرلورکوزن با عقد قراردادی به ارزش ۳۳ میلیون یورو راهی یوونتوس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/Futball180TV/102257" target="_blank">📅 17:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102256">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzzwbTTBo1JCNNmBAGlbnYMcJrbu56nG9IHBFr241r8xobnuGxV3ZTQMhRzKiSpM-PIPdyCSivgcehGt2d-WvRKBOMnYsS63bzg0Nx583wX0rk6g2EcfHB5p4bbwVLdd88DIQY6x12PZihTJdLr986siX2TaEMnSbjIcey1bNUjAUGaqnlAER1l53gnQNC5Tk85D6Dnqpm1DIVI4Vi8cwpb5T_SubCb_bgU5zcYFuopWdSxugzgFGBFZ7Z2fl8zZVclLnl4QMCzI91tQmgFGazUnYhDMwd8fyoSgV6Yyg1w2ODtvd_iEIbKv_HM-jUE7oHXW2SdHTPAr2KRT3kkNig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
رونمایی‌رسمی از لوگوی جدید فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/Futball180TV/102256" target="_blank">📅 17:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102255">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qErXcoTLANmqxBBWHQpuV3P028prtp6qLYy8zvrSKB7xVgNJwBtFl9el15ny2Agv0HO-e4U2WahZWAQRBxiU810naDWOw6bvLm4TdlcwB-R5uiuewox_J2jVvnP8oyat2FcFq_zWSWeYKMcyyFM72Kg1_SgHQcbskndtz4MSJf7SAigy-CA0IM9VfEqnJMz6cADJE5opsWHZhfldpWI_XVYVC44u_QdSJdBr5Ze_ic3uEupKcXfSRz6fMVU8BtLW56SDK7kTImYDEQpt-V_2JnRtXDCk4_pSTGTBhXfEErx-DFMaVn2CLysdzUWvKdtnVdF9TBGwz7hU9gdf1ZyZCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚽️
مارتن زیگلر - تایمز اسپورت
🔻
جیانی اینفانتینو، رئیس فدراسیون بین‌المللی فوتبال (فیفا)، قصد دارد بخشی از حقوق مسابقات جام جهانی را به سرمایه‌گذاران بخش خصوصی بفروشد.
🔻
مذاکرات با سرمایه‌گذاران و چهره‌های نزدیک به دولت رئیس‌جمهور آمریکا، دونالد ترامپ،…</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/102255" target="_blank">📅 17:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102254">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d715de39.mp4?token=u09rJruljSEHI2rsRrUPsCfLxHW-59mhrG9nLL4dwhBSs47fx9X0Z3sil2QhjFoq6TwipJjgJdlDSbQ993fzoQQtQuvgaDtOyqVx1KSjzWZZ5Ay8ZErwLosYruLb1iR7Detdl0oz7pWDMDcyHvRaGt88eXpO-HOl4Im4b1A2iZap2XYcxCoN3l-8B24mb7sf9VmySHQIzKnpAVFZub5fP4s7FrIvLMoOtMpTzmG51Y04gY0CeXDFOe_u-Y8x3CkuOB44kKJ-ZfKrFqc4bMDNBr24uC6hceDjVQ6KoBfqbnM-rzS-itjKva2xIUwZ3P4oVqZqWwQKVMHjSDfFvKStkoLnhkAID5pMS9v5iZ5uYf1ITPjPGoGnxbwqMw68ZO3Y6cEKaAR_CytiaGptPO0m6GUaP-LoxxF-RBaukNWpab997LBWHMNaNSLZElN0ZLR4qxroWoOECn-uK5Rvx_6OaDJnZ-rXh6BlojqyWHH_Jo9NH9jeuf1QROp0Mz1918UiD2PvcA7O9UCkerMs34Bc4MX3wIBa6NlcRqI83zmk0iwRVwei51HG3_B_RYncsKsMkKKfIMiFeYLKfyJOmPrMT3SmmfM2TaFY4G5B9_CYwF_1EcFfI8g4EeRobJqbP_BiUqCWlkG-lqSP14NNejBLqfG8oEtd1KPS6JPFS4MJWeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d715de39.mp4?token=u09rJruljSEHI2rsRrUPsCfLxHW-59mhrG9nLL4dwhBSs47fx9X0Z3sil2QhjFoq6TwipJjgJdlDSbQ993fzoQQtQuvgaDtOyqVx1KSjzWZZ5Ay8ZErwLosYruLb1iR7Detdl0oz7pWDMDcyHvRaGt88eXpO-HOl4Im4b1A2iZap2XYcxCoN3l-8B24mb7sf9VmySHQIzKnpAVFZub5fP4s7FrIvLMoOtMpTzmG51Y04gY0CeXDFOe_u-Y8x3CkuOB44kKJ-ZfKrFqc4bMDNBr24uC6hceDjVQ6KoBfqbnM-rzS-itjKva2xIUwZ3P4oVqZqWwQKVMHjSDfFvKStkoLnhkAID5pMS9v5iZ5uYf1ITPjPGoGnxbwqMw68ZO3Y6cEKaAR_CytiaGptPO0m6GUaP-LoxxF-RBaukNWpab997LBWHMNaNSLZElN0ZLR4qxroWoOECn-uK5Rvx_6OaDJnZ-rXh6BlojqyWHH_Jo9NH9jeuf1QROp0Mz1918UiD2PvcA7O9UCkerMs34Bc4MX3wIBa6NlcRqI83zmk0iwRVwei51HG3_B_RYncsKsMkKKfIMiFeYLKfyJOmPrMT3SmmfM2TaFY4G5B9_CYwF_1EcFfI8g4EeRobJqbP_BiUqCWlkG-lqSP14NNejBLqfG8oEtd1KPS6JPFS4MJWeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⛔️
تعریف ژیلا صادقی مجری صداوسیما از بازی پژمان در عشق ابدی !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/102254" target="_blank">📅 17:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102253">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkwZHE4IK-tosQtkmuXrA60s1FoxjccGyT25oTN6VLiGVbvIrs9J3jiHepZ1AyT8rgM3ow3kWKO92XYTqq9D31O9bExB9m_mRYzPjiP1FOi_gdOtTym6r_DQG5Ygg0bYzUalPDpWH5p7gG2xMFUorAXVPQFeEg6GZN-Mbi_jNiR9JdKghwSmzHbgC_f1K0pZtQWLtqpE4pLVAUyiNzTZ-TQQxZ6umv8IBSHvifaP_L1WhlWbOS2GwAF1UEKTHP8dmC_jS9YEqTy4mJjK0U7Lhf33IOhu9JjGbVxwJloWoju1qsPEr6YKFqmojvmQ4K494mdjtpQrcG_s731Ww4HHoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
از فلیکس‌دیاز: رئال‌مادرید به احتمال فراوان معامله رودری رو فردا نهایی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/102253" target="_blank">📅 17:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102252">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syXeCFbI8YaiJhKiuKBO_I_xbyIBoEDStEyPwOtfyr8hBkBoqX4yCJzJUwpbdLY3RT9QZSyO42jvAwfp1CIOS-RgO0SAkgeFAZNFR3itc-87HyOm7nR4DOk_tIzyy09DezEdmtU7JGjKLit9v5Mus0QESu6je50pxmlE2_zvmBBdF4u99q6KLXN4Ad_Sxu9UZqRDNAm5X2f3Omw4MCCv40GwXAkOp0-N0faHPLh6i1XVGOIPkmpM2Hw1zpUa6pnGJA7oYW1Iwa3nxWhulEcvnJx9hc8O8zmN4AXpROHTEFSe_3wlOiBTb_8SlUdfeOEZ4bi863GwbDy4SXI9tcjd_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
ساسا تافولیری:
بوعدی با منچستر سیتی به توافق رسیده است و قراردادی تا سال 2031 امضا خواهد کرد.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
✅
🇫🇷
لیل امیدوار است که 100 میلیون یورو از این انتقال به دست آورد، در حالی که منچستر سیتی می‌خواهد این انتقال را با 90 میلیون یورو به پایان برساند.
💰
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/102252" target="_blank">📅 17:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102251">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTPdY2MZZtpZL9mt6iY7NYc2GA5RIkhGG5DRwgRrXBCdnwvqgFFPtI_2dINaAh7S3MFwygjex9Wz4vKdkvBM1qizkKEY1roKata5Yt7vR9CtZTtLyiQI6B5Qw9SH4ewBpDXlzIdc-f2Ltcy3zHpXPbVS0kLpY0N0hvBMGbBB715pENz4PrfOhGlomBMs4XnuCo5IZDUjAY4Eieo1VmflPMeKovfmKeq4nWV9Neaa3nRiNiwZrppTxo7EJDzl-fEoOUPCyyHCIISKRLPsJd4xRE4RvJPy1oQTyeMcUE-IQWXmp2GUli09tWVUsuhckO3PIEj7v82w1tXPz2xAxTOa-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
رومانو: جردن هندرسون با عقد قراردادی به مدت دو فصل راهی چلسی میشه
HERE WE GO
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/102251" target="_blank">📅 17:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102250">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eb71ce498.mp4?token=aOoaKdp0oLdPrhrSQ2l2KmApGePVIkL1YZrk1ckW9UyNHosZNZeotCjQzVc4H5A4kjAexsop83J0KNUT2t-1MRJwhUYU-O8dZsTWPaIR8MWGkb46VU4TVtPlfS0sZXLXUsrgdTyWrnRY9iQ-ERLMqiEqOzKvBRbW_j4V29xp3Xb74D-FhfIDS-N2YjwrAjWgAxcaMiZaPh8fN4xAtsstqRvJEuOmxgk2b-HMK6SZtGjwPrfbKYhS_AO870-QWqlBMqFn9neY2aslndnrTlmQER4_6slIvyDnfN0mK2glcw61eJ5ZvQruf-AzHeJYLfL0cT7p4e15J2RumLhEbyGuQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eb71ce498.mp4?token=aOoaKdp0oLdPrhrSQ2l2KmApGePVIkL1YZrk1ckW9UyNHosZNZeotCjQzVc4H5A4kjAexsop83J0KNUT2t-1MRJwhUYU-O8dZsTWPaIR8MWGkb46VU4TVtPlfS0sZXLXUsrgdTyWrnRY9iQ-ERLMqiEqOzKvBRbW_j4V29xp3Xb74D-FhfIDS-N2YjwrAjWgAxcaMiZaPh8fN4xAtsstqRvJEuOmxgk2b-HMK6SZtGjwPrfbKYhS_AO870-QWqlBMqFn9neY2aslndnrTlmQER4_6slIvyDnfN0mK2glcw61eJ5ZvQruf-AzHeJYLfL0cT7p4e15J2RumLhEbyGuQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
لامین‌یامال و زیدش در تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/102250" target="_blank">📅 16:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102249">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ebe18939.mp4?token=VXCX2hjLHqOO8HYnBAkn6AZtNlZdWPTPJrasqAa6LktS9KtH345IeSD6OSgQg10IRRcKI7TDeg-jSX7wgKyMO4QCxLRHfyZpr3CZy2NDxG-ztfaii6KY6MTLk7atNpH03Iv2aDhVScsQZ70rbNfs5_Urd0hKC0JsfOp_aNB5oQ_YorfMRYxmJLGDV6tdCJM6H5S9QzuPBECbhU6LS6pYCLgsxHHdUleS_zJlR81SfD27uIIl4yvgw4TL1oBkEC2khEeQUHfVG25L4kvwfqpZSGwBvnTmSLNNDjJCAPRQG-1v-DYqSuQaSDu6KxIJBU02J2uoegEYF4QB37L8Ttc-MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ebe18939.mp4?token=VXCX2hjLHqOO8HYnBAkn6AZtNlZdWPTPJrasqAa6LktS9KtH345IeSD6OSgQg10IRRcKI7TDeg-jSX7wgKyMO4QCxLRHfyZpr3CZy2NDxG-ztfaii6KY6MTLk7atNpH03Iv2aDhVScsQZ70rbNfs5_Urd0hKC0JsfOp_aNB5oQ_YorfMRYxmJLGDV6tdCJM6H5S9QzuPBECbhU6LS6pYCLgsxHHdUleS_zJlR81SfD27uIIl4yvgw4TL1oBkEC2khEeQUHfVG25L4kvwfqpZSGwBvnTmSLNNDjJCAPRQG-1v-DYqSuQaSDu6KxIJBU02J2uoegEYF4QB37L8Ttc-MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ نادان وسط مراسم ختم گراهام آدامس در میاره به بغل دستیاش تعارف میزنه
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/102249" target="_blank">📅 16:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102248">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGgEm16p8HTipBefpW6HiJH38wJnHVezuS2KLmo9B3tCzCgs0SaLThFoq8puCYgQrqn-kF-ttwucGD_GDJAhJYFifo-nxF1FtfPT_adVyNaQYVw8dwM7vcLa5uKMOcLjR_1YWRfVJWSul4gbtciwVZ7lqyvUHVIOaRsTYIIzSloXFhz5hnk25HXxBiyrJSsZLFheG5MRrhsaCkpvYCyt-iRWu9KVUj1yXdD7XO7iyXB3bCc1AX-h2gB7meHALgPhtBIiKTMpYqX5ZWUO1BIiLtJjbREz8OYkZah6037iBT_pN3WrPqXLOOeubgQvUJukRHBu1_hXWjOa743PEyS4hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔹
رئیس باشگاه الاتحاد فاش کرد که بعد از جدایی لیونل مسی از پاری‌سن‌ژرمن، این باشگاه یک پیشنهاد تاریخی به او داده بود:
ما ۱.۵ میلیارد یورو به مسی پیشنهاد دادیم، اما او این پیشنهاد را رد کرد چون خانواده‌اش می‌خواستند در میامی زندگی کنند.
چیزی که بیشتر از همه ما را غافلگیر کرد این بود که حتی یک لحظه هم برای تصمیمش تردید نکرد. میتوانست خانواده‌اش را راضی کند، اما خانواده‌اش را به پول ترجیح داد. ما کاملا به تصمیمش احترام می‌گذاریم. خانواده همیشه از هر مبلغی مهم‌تر است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/102248" target="_blank">📅 16:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102247">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
ترامپ در مورد حمله ایران به اردن: حملات شدیدی به ایران انجام خواهد شد، آنها شکست خواهند خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/102247" target="_blank">📅 15:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102246">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2de7978a2.mp4?token=aGoA2xS5RM3qAE1RgG0owqcp3KhmhWdAECJrYCOnLK_1SC67cuenNLFsT1Wgt0gm71fRUrDi9enj6NIhVqQWMiiZ1rwzB9D2hpb4eY7rtfdwAcIc-8-nWxxdsQ5sWuDJ_kDaHXESRlBNFXkaH8TAF-RMR2Cr4iZWFZRAX81638uHE_iv2YUSES6c9HcotTXXy4gFTA-4sos3bRLapalKgQdXk_wr1gVi8FvLfNO7BcAaTKt6D3nmyaK5inJXNWmNaWcKSrpyHo3VIZ8DZXDLQu02cg4bMhFnCWAfLFjAcWgqI1wDZSE239nW59d83dE85GMn9856sJHS-3SYQuqPhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2de7978a2.mp4?token=aGoA2xS5RM3qAE1RgG0owqcp3KhmhWdAECJrYCOnLK_1SC67cuenNLFsT1Wgt0gm71fRUrDi9enj6NIhVqQWMiiZ1rwzB9D2hpb4eY7rtfdwAcIc-8-nWxxdsQ5sWuDJ_kDaHXESRlBNFXkaH8TAF-RMR2Cr4iZWFZRAX81638uHE_iv2YUSES6c9HcotTXXy4gFTA-4sos3bRLapalKgQdXk_wr1gVi8FvLfNO7BcAaTKt6D3nmyaK5inJXNWmNaWcKSrpyHo3VIZ8DZXDLQu02cg4bMhFnCWAfLFjAcWgqI1wDZSE239nW59d83dE85GMn9856sJHS-3SYQuqPhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
✔️
🔥
هادی ساعی در المپیک 2004
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102246" target="_blank">📅 15:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102245">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33130fd550.mp4?token=QPG19AOf23FWaq3QuEd0JfzdtiDhcDzl3FsjQrhSynBhl0TJYoQTRe6Cg98bq9SyXgaac1NzjXIl-KYO2YmhCbzogXn9rDDyQ5htetEfmVqxBojTMENc1bGWvtghrUb8cfkn1fRUsYGyoiOvqB4CCbuILbGdUwJBx6DEOguyNbqwrCDhOTo0H91QpVvDh57d0B0J9FJ2u9Mot2rxZ2eBW-xMC2VtTk5geFGEbiRd4PCas2FjeMrD6g66z1qbSEg7Pp5hLKIuas6wMmDhvmGv378gR4KIiEuE1BPaxGPUfVxxcc0nx6woy5p9HN1En13YsvZKUltDBp97rzz8xjToF5lDlFuGn0QmIGyMWGcBh2VBSn7dIJaX0BWyqKGibbH8-lM_nbHUhLSoytQkTsT7Ih5VQK8Gst8Nl9fsKHw6Dxa9qMORfeHrSdKm3k0zsjlvnnGAnqDTEGzkoOnqXuoqfLpRRRfUM6BAKrR9SAZat_8A9WmowKYfubr-cx4ZUD6Xs4m6gUxuJzvwQBUxcZfiJqdkM1mVkpqy7tVUEG87BDzsgaNBdKjrF8_73wkqcwDv-bWM5l_jMDWF25g0aKx91Qykv5OVfZjJqy7GvAemyNxeM4pC-A-WU4eWxAEWx1uYv-o0Wo1WV4CsBe6sPLWBiVLAeYjQsjMwVTQ6EO5XBjo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33130fd550.mp4?token=QPG19AOf23FWaq3QuEd0JfzdtiDhcDzl3FsjQrhSynBhl0TJYoQTRe6Cg98bq9SyXgaac1NzjXIl-KYO2YmhCbzogXn9rDDyQ5htetEfmVqxBojTMENc1bGWvtghrUb8cfkn1fRUsYGyoiOvqB4CCbuILbGdUwJBx6DEOguyNbqwrCDhOTo0H91QpVvDh57d0B0J9FJ2u9Mot2rxZ2eBW-xMC2VtTk5geFGEbiRd4PCas2FjeMrD6g66z1qbSEg7Pp5hLKIuas6wMmDhvmGv378gR4KIiEuE1BPaxGPUfVxxcc0nx6woy5p9HN1En13YsvZKUltDBp97rzz8xjToF5lDlFuGn0QmIGyMWGcBh2VBSn7dIJaX0BWyqKGibbH8-lM_nbHUhLSoytQkTsT7Ih5VQK8Gst8Nl9fsKHw6Dxa9qMORfeHrSdKm3k0zsjlvnnGAnqDTEGzkoOnqXuoqfLpRRRfUM6BAKrR9SAZat_8A9WmowKYfubr-cx4ZUD6Xs4m6gUxuJzvwQBUxcZfiJqdkM1mVkpqy7tVUEG87BDzsgaNBdKjrF8_73wkqcwDv-bWM5l_jMDWF25g0aKx91Qykv5OVfZjJqy7GvAemyNxeM4pC-A-WU4eWxAEWx1uYv-o0Wo1WV4CsBe6sPLWBiVLAeYjQsjMwVTQ6EO5XBjo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
احترام به هواداران به سبک لبرون جیمز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/102245" target="_blank">📅 15:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102244">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34dd03fd29.mp4?token=ZQQbj5arf2mgDpLVYGuCYEl6NUxDQzEPss92UUe-Ku6CFs-WI6V7R1-cY4nt3MTKSlos3z7IoBL43g8IhcLX8EXvUp8Gl0WbXbRL5BD8T_bi6VKkGydyn8Z8QGtAzSxuB-9LYG11I_JPBSgCRGNEJui7SVUtM-ZQKpjdWvaCubKcxpH-NekI5hMUEoxrNwVg0YQwL7m2r4uMNpqcYRPvDvMEH0dRMIodH9UXnp1wHSRBlgjkdjG3D95TfTthwuIhmOa87e4-M0OHoB0oozMtgVyc00nNGugT-Oo6_GLoQG7H_wuFXjMKSDLd1ojgvp8Te8ajmuI9R6r1-yRaaI39jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34dd03fd29.mp4?token=ZQQbj5arf2mgDpLVYGuCYEl6NUxDQzEPss92UUe-Ku6CFs-WI6V7R1-cY4nt3MTKSlos3z7IoBL43g8IhcLX8EXvUp8Gl0WbXbRL5BD8T_bi6VKkGydyn8Z8QGtAzSxuB-9LYG11I_JPBSgCRGNEJui7SVUtM-ZQKpjdWvaCubKcxpH-NekI5hMUEoxrNwVg0YQwL7m2r4uMNpqcYRPvDvMEH0dRMIodH9UXnp1wHSRBlgjkdjG3D95TfTthwuIhmOa87e4-M0OHoB0oozMtgVyc00nNGugT-Oo6_GLoQG7H_wuFXjMKSDLd1ojgvp8Te8ajmuI9R6r1-yRaaI39jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
یادی‌کنیم از تیزر تبلیغاتی با مسابقه رونالدو و‌ بوگاتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/102244" target="_blank">📅 15:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102243">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a4c493f3d.mp4?token=iRGfv_VjCL19MVjVKw9TdFZId1_7NjK_CvBRawgm-uxL5GnP37pltNmaXR5GJK0ZFXhJBInkDYdcf7tWWBBHXYbByx3KMAHPHg5H8ficZ9O065iIIZD2PQqA8OVAFEll4XmR09a1s_Rtm9VdNct1OZbl0Vf1zoSnsS5iTcvxmSXhev8K7p--Ls29nQbLjiZ-nsnMoYjyG9mPq-2z4q2__vZjeD7L7eTAMaCfvfrnHMI7oXcjkQNTjAWtsUhadJ0al1M_MY57IvJm9gWpXThMFYktIdjDxUd2GovHf0dFgfpCXh4YEQjDaomiy2gzg8m4gUeaIJVZyXu3SAq4e0jrdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a4c493f3d.mp4?token=iRGfv_VjCL19MVjVKw9TdFZId1_7NjK_CvBRawgm-uxL5GnP37pltNmaXR5GJK0ZFXhJBInkDYdcf7tWWBBHXYbByx3KMAHPHg5H8ficZ9O065iIIZD2PQqA8OVAFEll4XmR09a1s_Rtm9VdNct1OZbl0Vf1zoSnsS5iTcvxmSXhev8K7p--Ls29nQbLjiZ-nsnMoYjyG9mPq-2z4q2__vZjeD7L7eTAMaCfvfrnHMI7oXcjkQNTjAWtsUhadJ0al1M_MY57IvJm9gWpXThMFYktIdjDxUd2GovHf0dFgfpCXh4YEQjDaomiy2gzg8m4gUeaIJVZyXu3SAq4e0jrdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
▶️
یادی‌کنیم از مصاحبه سمی محمود فکری
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/102243" target="_blank">📅 14:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102242">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ed8d40d9.mp4?token=Q0rNQeB0vpheGkrHJCbJe0I553gOe080Hz1bDQd5cJwP45iexHDJEi1t1YRHIpgc8SOogW-3Aviowgdn6RxEq1RGoRW3j5_m9E8caGdVqwTr-BuxCAtthysoNAGfhcxukR_DiM4r6bixPFi-nzzWV6nWPsZ7OurGakCDjvygz0JltJ3XdIPZfwd6SGNfuzcsh3DfqU8le3MHfNar2Wxk-ufBeI9F0AXmwj_PiExwCWihWYYGNbTgoFjBS65gntRfeRH2TqEJnj6_ajg5yzutLs2D6zcb7ba-POCXIFZdxOGQPWKojT7KO6CJttpT8SCjoMe0lRF53c6H9mXAcxOUkIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ed8d40d9.mp4?token=Q0rNQeB0vpheGkrHJCbJe0I553gOe080Hz1bDQd5cJwP45iexHDJEi1t1YRHIpgc8SOogW-3Aviowgdn6RxEq1RGoRW3j5_m9E8caGdVqwTr-BuxCAtthysoNAGfhcxukR_DiM4r6bixPFi-nzzWV6nWPsZ7OurGakCDjvygz0JltJ3XdIPZfwd6SGNfuzcsh3DfqU8le3MHfNar2Wxk-ufBeI9F0AXmwj_PiExwCWihWYYGNbTgoFjBS65gntRfeRH2TqEJnj6_ajg5yzutLs2D6zcb7ba-POCXIFZdxOGQPWKojT7KO6CJttpT8SCjoMe0lRF53c6H9mXAcxOUkIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دوازده‌سال پیش در چنین روزی اوریگی زننده گل تاریخی لیورپول به بارسلونا، به جمع لک‌لک ها پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102242" target="_blank">📅 14:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102241">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9073a1aea.mp4?token=LTQ2a4LMVDFqXkSVUdDqUxSI4M-6VWqVcrl9to2aKM3kFW8SgCi87364exmK8QR9V8z6PDZAA2L5HinR7W_mR_Yt9FIZzpluOcb6xmspf6hJvmvaEc8JkbOthvnBHjDYVravojPzNOyA5J0iiWsH9lB0TuvgXSq_xUX0BdKG4hOA_7wBPRPHwCG6jZsAMypl61jH8zev7eDT46oQdTAUWQFZae_D3THFhDl5KhZHJjZDPeeMYvyBLS7quRJpx-YzcRrPntTjlI1388J_8dugJBs_4k9Bp0X7PtuiSztZT3YwaZUs2D85QDUxYerb1rffT8WoQ2FwXeju_-XapMM1QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9073a1aea.mp4?token=LTQ2a4LMVDFqXkSVUdDqUxSI4M-6VWqVcrl9to2aKM3kFW8SgCi87364exmK8QR9V8z6PDZAA2L5HinR7W_mR_Yt9FIZzpluOcb6xmspf6hJvmvaEc8JkbOthvnBHjDYVravojPzNOyA5J0iiWsH9lB0TuvgXSq_xUX0BdKG4hOA_7wBPRPHwCG6jZsAMypl61jH8zev7eDT46oQdTAUWQFZae_D3THFhDl5KhZHJjZDPeeMYvyBLS7quRJpx-YzcRrPntTjlI1388J_8dugJBs_4k9Bp0X7PtuiSztZT3YwaZUs2D85QDUxYerb1rffT8WoQ2FwXeju_-XapMM1QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو انگیزشی با روایتی‌از زندگی مایکل جردن
💚
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/102241" target="_blank">📅 14:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102240">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_-ROEaU9hJfHo6Mi39lkj0RsxtmxlsyX9TZhFXpqBsvIQj7jWiOilzJCL6rzkBmosTwwTsp9dxy9dV-IMpoOXYwjhZfIjtduLvEgVhHJrEnHR1AM4kYQOUyDcVkMucaKY-M0KgSfXeYwo7hFQVbfdceirUFyvRdfR3r4EvVrviTMfxAg4mqGRt60tWZErI1zoqnRxSAzbqQrzUmp2_aLXZfOmGIrqzm8lxJCUxC8Ah1FkpQbW2tgQ5jsjgGFukqIgfvvPW-6dR_Icvf5HQOpZOZcsYr0DUE7psCZ9o9RHg9q1zGX4n_LVvuKQKPRnCU1kKCjF_mHWImFpylFV1D-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🚨
‼️
پاول دورف مدیر تلگرام، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفت!
و اما واکنش اکانت رسمی تلگرام توی توییتر:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102240" target="_blank">📅 13:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102239">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🏴󠁧󠁢󠁷󠁬󠁳󠁿
همراه باشیم با بهترین نسخه گرت‌بیل در رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/102239" target="_blank">📅 13:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102237">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KxuOi-iRHNK2hYvec_yOxonjXvsFg9cQWCmGyMWgz7ZwNqZ_LvTndQfisDsCR_SZy4itFIL54z1hUxicRgUvEQqpdcHOBYjfcf6qun7O7MW8ArlN7A4EiVbqWvCQRhpV_O_2xa8QfzCay5qdY7XIaHzFI0tJ-GDV72jZKp9i0tNPQcDFEpj93KxfeGYwBfm3cfN1oz4UCgoKJYNzRjec4DcH7a4b78uV9FAOWylwG8uF-ilV6AZNTB4ULMj7Fsw-5HFCkEJwAr5jhz-I_INy_r3xf4y9dFpkd-2Y0kCjnPSkY1Rsgj5zjnpYFOP3VA_PyPKtYZIlzOvdah8QGlQCmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EWTP5x2PZ5MPm1QZ7W2xZoyrqAAaaczL1pqrkkxii4zqcDut56F2Qj1jZ4LsumQcaVLjXAEw92NwcukbrxkBE6PblLOnTfkn3xl8dYFIPu3yILyg3UCItBOPYTH068gQ7jJZd5CxKBv99CVNsvBGe9zuahRoB6vERHVra-ShwVaL4rA0f02TNQ24CBJOvM9JltBFgTDShOblCEdsnHNX8kr_6ODHizU6sU_zrD7Ez-1t01qpjlrGIi73Yr3tmLfbRJ6YnYbpMWq4fM3dMcJbEcYqVwYv80toc2WIOd5fE_9kdtWVU5oos7unMtcR-orQKCvDxBJBQTjkWF3-K6-nHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گابریل مارتینلی هم ازدواج کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102237" target="_blank">📅 13:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102236">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxZ50GBxrOAub7attGb8wiUBPIyDX91D1cZaqW_JolU1kzQmvN1mtIyDNExCkK2IA38Fb7uBJvxfObmtONIYMLKyW42S91m4lM28WYTOK3obeaCz1p9oZBfuCfF6ekdWElC9pIUomZcnxcRyRxmv62ViPYBaT7bFA83rxuQ2CzvNYiOOGJveY1Ad9SwFOyr4cWkp1XPYz9jZ-9lyeZgTtN2v15O5pXSR8LMM_zzPHdrdWZ1E8KKwo07THTfRGnTGwlMtYXxIVwwqae0-iNufTYJCShRYHdJFoKGd0iWdNur4HJ1ZPLbqbDM2UM_5DxWaSRs27_QfMsKNrDlIujXx5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
⚽️
#فوووووری
🔺
اینفانتینو به فدراسیون‌های فوتبال اعلام کرده است که در صورت موافقت آن‌ها با فروش سهام جام جهانی، هر فدراسیون 40 میلیون دلار دریافت خواهد کرد.
🔺
در صورتی که فروش سهام رد شود، هر فدراسیون 10 میلیون دلار دریافت خواهد کرد. یکی از منابع گفت که…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/102236" target="_blank">📅 13:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102235">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUA1Krx_TXeOcPuThIbtGq7v26kmT7duuzuSpZyAYWq2UMi29ONOj4UkRvdXMy0wjGYblFPtUkShd16Ea8uRLpb1b_LIyLKGwoGz0WHJNmAHRhHBfe6SLd-_POyZbv-ZdDxHcl65hAnpbksHuwCKPpJedJ3fmOF1j2FwjJqmmF5YWngj3n3rt1rFU1q9eSU0vi1S8tU9Mad-ZxHnk68M7K5oLscvvHjj56rjwDCTT8Tx-HpNmgdiiJaF3LkilffRn5X_jdASTlxmQPii4Jzx4crr5ufZSUnBV_lm3HVZXM-V2BEakA6YG-KkCT7GMrjS56JwDGYGTcjO2aoEfQNuTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
موندو: باشگاه تاتنهام انگلیس رویای جذب کونده مدافع بارسلونا رو داره اما کاتالان‌ها فقط با پیشنهاد بالای ۵۰ میلیون یورو امکان فروش این بازیکن رو بررسی می‌کنند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/102235" target="_blank">📅 13:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102234">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6YAIKT-RPc988efvD5aLAJbVDROvoySyv46pg2QX_4dZXD36EWxxlwwrcbuwfkoloxqj5zhJgfX98MZTZ1Ob2V16WQV2mGmkCpYqiTqQ_vwp1iLX0Pfa8iG5IKXcjuGYzUttpmAWE22L8MwhZKylLCV7zmb53x0We5ZVSkV_RM4lMwuaYH5wAZxT3ldW5L5_zYLJ61t399KJX-NJSn1DmIhq11ENAQdNy1Mw7mbe868VbnnKOZQLjFMTGqKVFokQm18prl6HHhLBFPMOf1roFzjRahAyDYw2TjkPYmgihh_dDNg8A1Azvni4PC8VVDmley2bvPt83gGreLyoH0krw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
#فوووووری از اسکای اسپورت:
🔺
🇪🇺
یوفا به کشورهای عضو این اتحادیه در اروپا اعلام آماده‌باش کرده که اگر اینفانتینو بخواهد جام‌جهانی را به سرمایه‌گذاران خصوصی بفروشد، از حضور در دوره‌های آتی این‌رقابت‌ها انصراف دهند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102234" target="_blank">📅 13:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102233">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad75895bc.mp4?token=sVRs8OXO1bIPmHIDtAF5l2ccWXt70eJ8_szac25X7rD70qZFfPwNIUDz-lttWLaSmPNVodG4pkFj97h6-VqntdMut7ehAYYXr38GmQv-yCKaWTCgh-dYVLDo63AtWXLv5I5UEWBso2S40Wbef3r34-koVPqGE-eqKWZgNqtea6YY_V-V6YbGBF36L3xroKg99PzpuE7DZArEUmxcpkOD7chIikH6-v-TO5F3DUhO70v4eaDbpwKQ8GUluVCClgMtSZvcZNdsq51Aqf78ByvFKSQ_FmOFTVl4-AE42gN1HjgzSc_71UrODDoS9z4yuqFFRX4QPBI4MRqyEjrSWE2fjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad75895bc.mp4?token=sVRs8OXO1bIPmHIDtAF5l2ccWXt70eJ8_szac25X7rD70qZFfPwNIUDz-lttWLaSmPNVodG4pkFj97h6-VqntdMut7ehAYYXr38GmQv-yCKaWTCgh-dYVLDo63AtWXLv5I5UEWBso2S40Wbef3r34-koVPqGE-eqKWZgNqtea6YY_V-V6YbGBF36L3xroKg99PzpuE7DZArEUmxcpkOD7chIikH6-v-TO5F3DUhO70v4eaDbpwKQ8GUluVCClgMtSZvcZNdsq51Aqf78ByvFKSQ_FmOFTVl4-AE42gN1HjgzSc_71UrODDoS9z4yuqFFRX4QPBI4MRqyEjrSWE2fjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
دوران prime مردم ایران:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/102233" target="_blank">📅 13:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102232">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96ae46afa1.mp4?token=dHOr-jIqZhf_oNa5hjrLUpv11ZlbAaj1xtmbmE7HVa3FxgZYnGmkevdu_JbGaURMugJU0XKJdvNSO248kPB2Zo_G71TN6pDXKpmwUuguBr-QEBG0aRxr4hHCxlbDmFRp89-Lb_Lg9FbQj4a2EIeBJtkrUgz01gr7qruUeutiFau2h3gLV2y0C053S4ylV-6yFSzYoVU7P_J-mXIAGimB-FQwctca4La69SHeL_wZIES9omGyIOvmgpq8BiHTIC-c-suiQJN1yoWEbUAECm27xm9c7mxTu39NTg9HrdU-ry5Om_pFwQp2D6uHez2Iuj_3ntFn9bvQ6DUrTLQyhIDULA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96ae46afa1.mp4?token=dHOr-jIqZhf_oNa5hjrLUpv11ZlbAaj1xtmbmE7HVa3FxgZYnGmkevdu_JbGaURMugJU0XKJdvNSO248kPB2Zo_G71TN6pDXKpmwUuguBr-QEBG0aRxr4hHCxlbDmFRp89-Lb_Lg9FbQj4a2EIeBJtkrUgz01gr7qruUeutiFau2h3gLV2y0C053S4ylV-6yFSzYoVU7P_J-mXIAGimB-FQwctca4La69SHeL_wZIES9omGyIOvmgpq8BiHTIC-c-suiQJN1yoWEbUAECm27xm9c7mxTu39NTg9HrdU-ry5Om_pFwQp2D6uHez2Iuj_3ntFn9bvQ6DUrTLQyhIDULA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
دنی آلوز به روایت عادل فردوسی پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102232" target="_blank">📅 12:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102231">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fa9208342.mp4?token=E42LU-i9ZOpLB-GldP_lLMwFzyfkbLIKzV1OnhatGFd1gAzuqs_mauoTxQ1HuL6Kc3cmZbe6VOCPbUHvAs7BQeTHZpGo4K9mdH6fmU6iTKxwcweLDBosM8Bo9pTSYa5DS2FS9Yjn5lCxTwxQYeUjbX1oNqolmH4ExSZ6ZexZnJ7IPfqjNdmADgR1AT7JCEO-tuT65mrbKczu2UW2oIdOntkB5rj55WlCy6i8VhUaapV2ySOR93DlLVQktJpICRbRrRX-VBRjMg6TAM1A-3VaO86JV1opS-7rtsEhx0Jgeibu8yDhvYDMnBE50GWmXdmlTyvfVohADsUWmQU0qPqpNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fa9208342.mp4?token=E42LU-i9ZOpLB-GldP_lLMwFzyfkbLIKzV1OnhatGFd1gAzuqs_mauoTxQ1HuL6Kc3cmZbe6VOCPbUHvAs7BQeTHZpGo4K9mdH6fmU6iTKxwcweLDBosM8Bo9pTSYa5DS2FS9Yjn5lCxTwxQYeUjbX1oNqolmH4ExSZ6ZexZnJ7IPfqjNdmADgR1AT7JCEO-tuT65mrbKczu2UW2oIdOntkB5rj55WlCy6i8VhUaapV2ySOR93DlLVQktJpICRbRrRX-VBRjMg6TAM1A-3VaO86JV1opS-7rtsEhx0Jgeibu8yDhvYDMnBE50GWmXdmlTyvfVohADsUWmQU0qPqpNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانسور کردن در صداوسیما این‌شکلیه :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102231" target="_blank">📅 12:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102230">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1c-5FYF0tnKzQFS3ZE9b7JwJLtl-o284VGw2D6PPEN-NvUwL5LdlJLPCRuu42SAkEl0B6hmP3Z0kK5e8TwUEfv9Trbtwqb13UoTaQDtov8pdf-M6QprAghANjzW5w39BolPHdj2kNllXTXBwmA0I4S5Y6qj4BNcLsFv8wVKabRBLygpGVbdP_y9_ccehLeNl71gXAobDvOzToc0uYnMLP4xTaRW950aDCd7Fs9Ew8nq85aXnVESNpBDV22UdOlpMkrId_ceYZEcI7OSfoKm5gEc-XbeCV46KuVBnpr9FUZOepk_VtVBAzaqRyDSrOpeOhkvqx9O0cKlw9C5JbPIFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی با مالکیت تادبولی تصمیم‌گرفته که برای چهارمین‌فصل متوالی نام هیچ اسپانسری روی پیراهنش قرار نده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/102230" target="_blank">📅 12:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102229">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
🗞
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خبر فوری از فابریزیو رومانو: برای اولین بار و با موافقت فلورنتینو پرز، مذاکراتی بین رئال مادرید و منچسترسیتی برای جذب رودری در جریان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102229" target="_blank">📅 11:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102226">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/focP4ZvXg9pcI9YNkmkUREW_PthfwYalGfixxZAjvUK8i30dD1NK2pAwhfD1CLTcT0fQ6XvqUfAelGmWqVd7SzMvbiCx0kcgd8jSv-R2WBKI7ld5zXIvF6c3CXUA2hUORWvgx7j-M-GxN-4SaBjWSlm-3vzfom_sVwAR0_FJjPHWhIWv7UXvq01qBkZiPsC0Yu8lkXShecnmvQxSTfSuShIsYVrkVnhD3NdMKEY2cik2qa1CSr2WTpf0TO-Xvdpv8s8MV0QGw6AFqxuRs-hIoKcBhgxv2uY4nDpP2sbcV6meSyZNBFwTNiaBGBjNRKNqx4-9R293QrTPlHzQgANWOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IH8OZErzAFjZEFkdOTFsBbCd6Q32TP1yMma7_Y3YYEreCTYGRd7abgy8UhZAUCGX8eGR2LFrfwSBpS6lBVHgGSSZRpI1kjD__2vftaEVsqY_MUp3xjNg0aqtJkNm2Bjklm7o_wh77oUPfT9GnI8JVIz4E9gxmsX9DFdQ1HWn6U_xAFbRu3rtDNAleoUhf-ZOzzJsP1jnC4Fw7lIaEGwU8HFc7eCwo4NRBJr5wn_bCj-qDapVJ7Mf3dOozidVS5PIn-9uMJQN1cnFiuSpmZK2erElCtxKGh4HcPdv8UwDtgqVn35LlruHDMpn3mjIV-5DTKvu6sRWzXkFfsAa62qMGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XseDqgTJgh5gFPsxX7MrNMs29h7iYIxcHASRltdS7bS6fh0nKyEukwawZfc08d3Uykvv-8VOiuOlv-BhM6eYmtPy94zHFHccYaKE_-CmgNEYt6ezaO1T2FaN2kyngavxOv1o9CvZbvRuIdCuDRRziozj4k-MfIh_WMeIthgexN_U3axWDGKKr-YaYW83a_Koz_Zzz8rwFCGPnWiFdWpBlmePUCI7nBE2nm_XYSnmvvD4omRoc41OxolZkzO-4aiU_zCuZlHP4bRrNH3BmIP8iOPcWzlLJ-ppxzj3wU4K5OZ2PyAaAanirrYsM8pm29utgg3-7ge7PrRG-rR6qP0L3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
⁉️
وضعیت سرمربیان تیم‌های حاضر در جام‌جهانی بعد از پایان مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102226" target="_blank">📅 11:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102225">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhM-ElbXC_S1Inm-jezDLMl9EpBRX-JmDCpEXr2_ch7RxkGNJ5GFqWscC_o2pMoqm2XB2a2OZLOnznRUfbSfYnQe6z-L1iiOUk3QKB_C2A1aSEqs8vs_aQpRk2dRlDMcHUkVFa1PlDL_gPvcskdSHt-ijP8lb2bMZXPzjYAp0BCKIHtmpVNrUog9FySNyNyoxyQDKK7rDDOcWrANiZ8-VfzVKo8Lghp565gTHT2j7GOBgLf6ZPSRj6zuAzlTJRaEQNGfwqTLQ-GUkfJGy0NpMxaa4aBVoElHN8OJJKwHYODaPkVcX1VxlOIsoYWtE3aAT89v7VCqatuMF9jj1DhIJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
▶️
رونالدو داره یه سریال به اسم "Day 1s" درباره پشت‌پرده زندگی و کار ایجنت‌های فوتبال می‌سازه.
غیر از خود رونالدو، چهره‌های معروفی مثل تیری آنری، دیمین لوئیس و یه رپر به اسم دیو تو این سریال بازی می‌کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102225" target="_blank">📅 11:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102224">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvGWCx6dPjqUuT_DH_3KdwDolMhRS0YrnjYyiMJpcNFzHmXvnvVaVaKiaxclCWVkPBxwCXkkvHnvMAj5DlFmWWjP-AmZwM0IdKP8FSivnzWm1EeM66G5iJJwARRdXwZ-Rpsr6UEMIqnMufxGFDtuyulBV0PcT1j-VVtgWruRE0fmBP7EYLmzIP8OLH7k4THCPnpgS8KEEjnF0z0QEl4GO8m4zdAH0jlTnb1x0fnBtC3hSq-1K8P91cpY3YMDAroUg7-saGMHCBqKjOu6sUw-7mT0SMQ33yolQKUtbz3sr9cPfQUeZ9AimqrPd-kYS0qZjo6DVPFvZ7g9zVpfpCduDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب احتمالی فصل‌آینده لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102224" target="_blank">📅 11:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102223">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2wwm5hFLgYAgPqc-e8dUPJiHUYf9Dy0S1DXMR0vOBliRvGW7IYZHw5UHoFKROAB8vh6HRjiES2siHj1MFPkYaPfsxNFXp5VEX1qrnx-WPAOxdkyt_-Oe6vjEHwHbnCQG_a9x17akp1gD79x7JVWM6T_MItoHc-W03c9wM3-HpoUIibQ4IOegtvIXPPauQWraFR0yMz77bRlizGIfiPLYgVkfRK7PjyJesEFrZ29SiimXs1fABfFhxOvxHY1pUvVNWmgkUgVXo1qMT8Mzl3kkvElsDkFTXOkqUxlyzalyHUzOj-yBkwD3f5df8KpfAJL4rrJTn7eHpf8dGIZ8yVeqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خبر فوری از فابریزیو رومانو: برای اولین بار و با موافقت فلورنتینو پرز، مذاکراتی بین رئال مادرید و منچسترسیتی برای جذب رودری در جریان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102223" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102222">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WP6jdflHl9r6bCqGIWBLfXz7jouAd3fPROdIREaBMuLqjfkMPlDUwsltejINs4w5m9AsPQVHCRL-FT4JSUTmj9wf1kDbfJ10W840aWSVZ7ftZkbBVb-PM5GR2Rp6qKNV-iuLdeg_dZoe2naRp44Cc2tg1DMZ_OAZeQzJ2ZOZA3cY57EMDo1H48I8zhYh1gB74MG7WzUeHqiExq-icj-n1qR4Zq7jKFNRLlahpb3mpDF5uCBAB23mZ4Ggei3p6QqFaBFgtPQ38j6CVXbCqHnQ6KgJl1FzZkPRjJK7WXSJ75Dh6Euu0mcu0t6Vhqq1z15BCsTnKLmnYRimVjlfLimJeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
💥
تعطیلات امباپه در کنار اکسپوزیتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102222" target="_blank">📅 10:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102221">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1876f5buA64fSuncZR5w1Y6sdM-JPgA-g-W7VxFUuGK3PGiAEBVp4O75POngVVGsonU_whFBhspHJG0cojf8ZbKkxwpQgAwV6Yb6jMhdazzgP0J3Kel_9O5NOXYZDsV15FO66FOuQuqsOjhu1ITFqlIzmxbkUvE6q8uYjimtUge1LqOoTR14r42op6NY1dPCr4214Eq0sReiWgIga3tBWXthkv3gXiRGU8Ru1vbk8WbdUJNtDCT4E0tFjpuo_ViVcxjfeHzfHO0NEF7xFc156cDS74snFJGYjKV9WMs20mSSh3vlT-1y7UoUhz_-pM_nuPhMCadvilkWCFahn0fqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
6 سال پیش، هالند 20 ساله تنها 71 گل به ثمر رسانده بود، در حالی که در مقابل نیمار افسانه‌ای قرار می‌گرفت که در آن زمان 375 گل زده بود. این اختلاف 304 گلی، مانند یک پرتگاه غیرقابل عبور به نظر می‌رسید.
🤦
🗓
6 سال بعد، هالند 290 گل دیگر به ثمر رسانده و به رکورد 361 گل رسیده است. در همین مدت، نیمار تنها 84 گل دیگر به مجموع خود اضافه کرده است.
😳
یک ماشین گلزنی که به طور متوسط بیش از 48 گل در سال به ثمر می‌رساند، در مقایسه با یک نابغه که به نظر می‌رسد سرعت گلزنی‌اش به طور قابل توجهی کاهش یافته و دقیقاً 14 گل در سال است...
😭
و اکنون، در سن 26 سالگی، هالند کمتر از 100 گل با مجموع گل‌های دوران حرفه‌ای نیمار جونیور فاصله دارد – یکی از نمادهای بزرگ فوتبال.
🤯
واقعاً باورنکردنی است که هالند با چه سرعتی و ثبات فوق‌العاده‌ای گل به ثمر می‌رساند.
⚠️
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102221" target="_blank">📅 10:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102220">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f225d20c69.mp4?token=WSTsDshLWP5fjkGcEcfOdaaiP5KuSPMDcvfO834Pt57hVJGQoCy_TU2KCtm_XtVY6_qq7piOH5UjpmJNpJlpwwkdR8fvVJOlfdrAnQq-AB8P5AokkTDFZME5a3uQ3NiZOc3TW-ia1gn4nO_i4VcB026Nww8NN4S7YxBnAgiHW1ozhtEtmp3W6UCYND5AIJ_C6QSq8jk1Y_7LWjv5teDqMF7ywdS63mybfeE8LDf3avT9RwJ7iqgrgkdmN4saxizMufTqXw_RnfdWb1__J0944E1HIOdbD7IiXtffpJJLjNBl63ENa9W0p_PSDcMOo8UuVJ4mmuQADuUjeZ07ZxiGGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f225d20c69.mp4?token=WSTsDshLWP5fjkGcEcfOdaaiP5KuSPMDcvfO834Pt57hVJGQoCy_TU2KCtm_XtVY6_qq7piOH5UjpmJNpJlpwwkdR8fvVJOlfdrAnQq-AB8P5AokkTDFZME5a3uQ3NiZOc3TW-ia1gn4nO_i4VcB026Nww8NN4S7YxBnAgiHW1ozhtEtmp3W6UCYND5AIJ_C6QSq8jk1Y_7LWjv5teDqMF7ywdS63mybfeE8LDf3avT9RwJ7iqgrgkdmN4saxizMufTqXw_RnfdWb1__J0944E1HIOdbD7IiXtffpJJLjNBl63ENa9W0p_PSDcMOo8UuVJ4mmuQADuUjeZ07ZxiGGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مروری بر برخی گل‌های اسطوره کون برای سیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102220" target="_blank">📅 10:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102219">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33ef87c459.mp4?token=Btrq7tbn8c0i31drlALx734lFbRr0Jlt8UfFNo6HyrzkgU0fLU7qCmpPBHN7eRRIOtoUfVfzC0hHr40vD_LpAngEt2vPkGsS4tqqT-qSYJQTuOx0r--Kvdvdhn3kI1ShA2MG3frL-uKZj49q3Ib_8VV82ZMsINlx5loBBzAKAFAMQDd5hi8BzeMzd_4NBNnSfdchcJ2gnc--b_MtUr8RI3z1lM936Hp-I4KXDg0edxGQvu9G1g8kC27FYsrbxeaUSFzb8Fp8idFLeXdVR1JZsudjvn1G4umcbNyWhScm-kpTxZXJ3egrztKW0Adf6eGNx9xsb0lcf3fTcxllMFuW_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33ef87c459.mp4?token=Btrq7tbn8c0i31drlALx734lFbRr0Jlt8UfFNo6HyrzkgU0fLU7qCmpPBHN7eRRIOtoUfVfzC0hHr40vD_LpAngEt2vPkGsS4tqqT-qSYJQTuOx0r--Kvdvdhn3kI1ShA2MG3frL-uKZj49q3Ib_8VV82ZMsINlx5loBBzAKAFAMQDd5hi8BzeMzd_4NBNnSfdchcJ2gnc--b_MtUr8RI3z1lM936Hp-I4KXDg0edxGQvu9G1g8kC27FYsrbxeaUSFzb8Fp8idFLeXdVR1JZsudjvn1G4umcbNyWhScm-kpTxZXJ3egrztKW0Adf6eGNx9xsb0lcf3fTcxllMFuW_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا همه رو شکست داد جز ...
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102219" target="_blank">📅 10:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102218">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-SS4X-7yAHhnsALF4-7VjC5dGpB4oBfuzb6e--Ur1HlPhbgacWoMNcg1v5HsVFE3_k7cPkWkrpoMtrPh5zqPgrEspJ7JsUyzWvg1dUm6tRp6obvHIenMgk0j71XRsiLeEcKmAPLFrBiU53H1Wnb7gOdxkMnc6Va2QprCOkKQ0I49zooEYzNL-5DUlZSVntyIdfl7nQkEvcgcnVwMBPDsAM4b6fmyZT8TDZoQnQa0dIEs0A7H6vmoCffGILoZHCUamcP9dCCjIR_ZZS5CPfypJ73FYGeoskp-tAigPEEOm8i5Itt2Z1Bp4QhGxXfxHQFDpfnIsdPqz8hOHXKeo2ufA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
✍️
فابریزیو رومانو:
بایرن مونیخ در حال بررسی تمدید قرارداد با هری کین است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102218" target="_blank">📅 09:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102217">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5802c51b8.mp4?token=hdaGwudbd1GR0VQdPkIWVZKI675oapNzhcD_sgQ5gP2VBv27E1c9-7WVa1tQSIV-JrZlpsWab3X_vyQdpsBE9jEvinR7SpLWdMQ_Ys1C1S-3AXFDpOQzz7sMwAPAFbOenPf2C3uMpLF_pVV0iX6JyahEOVQQ-VktfzqbBfwvofmlcd9IrPsRoWIFtv431cYrK7eHZXgb7uywvvesf1M3Z1vCoyO1gWh9eWLeC1hl3qeGZSqP42of2lyPt1dSfGOB64mMmhCWSJTWyJ-zUmzfzGGCg3bBqfLQC9YmekboxpqVrDVLLVnLH341UmsqfJaajoELqSnyUNC9yep7D7-pwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5802c51b8.mp4?token=hdaGwudbd1GR0VQdPkIWVZKI675oapNzhcD_sgQ5gP2VBv27E1c9-7WVa1tQSIV-JrZlpsWab3X_vyQdpsBE9jEvinR7SpLWdMQ_Ys1C1S-3AXFDpOQzz7sMwAPAFbOenPf2C3uMpLF_pVV0iX6JyahEOVQQ-VktfzqbBfwvofmlcd9IrPsRoWIFtv431cYrK7eHZXgb7uywvvesf1M3Z1vCoyO1gWh9eWLeC1hl3qeGZSqP42of2lyPt1dSfGOB64mMmhCWSJTWyJ-zUmzfzGGCg3bBqfLQC9YmekboxpqVrDVLLVnLH341UmsqfJaajoELqSnyUNC9yep7D7-pwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
کاماوینگا بخاطر همین سطح عقلیشه که مورینیو میخواد دکمشو بزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102217" target="_blank">📅 09:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102216">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBxdVPfr0IR72jWx0BIAI7do1nv0KamJZtQCXluhmaN1NaBXFo8eeG0SfUa2oh_LUw17xkDJRGz_Ifsxqz2MfRR0ALBKyW3lYk_YFU8qWtEpT9mWLZMC8eE1f7v3iXa9cupsPqK7zcefUOzQQP15FXdQH00FXopYNcgdHoOCz5nB6THdX0vgr84wsAvCQJIQStx7kEVL2eGEtU55w3-vS-4bqSFdn5QVDsZW-HJtnE_-2PwF_jdkAXZ_JkD-eJU375Uaxl64oVJW_yWkP8JHdcB8zL4zMBdl9DcOcvUK2EyIIfo7L-j0-IUSrrKqam22jv2XkEkZxxWqK3xiMDknWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرف رفته زیر پست ویتینیا کامنت گذاشته که ناموسا تو جام‌جهانی 2030 به رونالدو جونیور (پسر رونالدو) پاس بده
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102216" target="_blank">📅 09:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102215">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4792b1fc1.mp4?token=BCH3jCaXz_KnTtUkwYgYTJ9P3lcLs0VXM3aYIjaXypiH9pHUM1mG_hNaj-dI2zIIlQep-UznCsGjBTX_fbFXPtAlTLoWxihOln6kow3OFm2xrTrFLMceOtCM8HoSZr0ackHqH5bvQbuN75rvBT4Z63eAL540QEqDuizf4P-2e7Z1ED_P-Rg7irBxrHa6xhrZMH9Lc-fHL6cZDXpeA8fngC3JSCG-rTBfGirtAGL6-wjF9_uX2CjKXGZ38WwWKoz0Nr7DqTXMb6C0zsQBp3BDVqOXpj7s4IWy7War3z2nVZ3sEv1F-d4PZldlk8hLUnlK14_Nqoi2H56Z5d1gY8Sz8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4792b1fc1.mp4?token=BCH3jCaXz_KnTtUkwYgYTJ9P3lcLs0VXM3aYIjaXypiH9pHUM1mG_hNaj-dI2zIIlQep-UznCsGjBTX_fbFXPtAlTLoWxihOln6kow3OFm2xrTrFLMceOtCM8HoSZr0ackHqH5bvQbuN75rvBT4Z63eAL540QEqDuizf4P-2e7Z1ED_P-Rg7irBxrHa6xhrZMH9Lc-fHL6cZDXpeA8fngC3JSCG-rTBfGirtAGL6-wjF9_uX2CjKXGZ38WwWKoz0Nr7DqTXMb6C0zsQBp3BDVqOXpj7s4IWy7War3z2nVZ3sEv1F-d4PZldlk8hLUnlK14_Nqoi2H56Z5d1gY8Sz8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
جانفداهای عزیز درحال حرکت به سمت مرز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102215" target="_blank">📅 09:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102214">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c8836d3c9.mp4?token=OBIY07wzqLKOxh6xkdZvJrPxp75rr5k82GFdXRUIkpt_nxbcfzscKGFXOZx-4CtvZWVb5R_FhlnMkUSIqPGBqFrxcBu1iWLfJvi2ijSWF5AdLygOQrSQKgQymWwWvjGEEN2Epozn9ZU-yGHiuP9ODikDIV55Xo5RwqA-IvTeOqI4zbVureZvZAEynSeGxz4dBW9YIMiudK8CQ3996RqJsiTYZNK1F4KzdF51MJxZ05MvYPbgKaQTlMZpx08Xwf8bO8mhhqg7tGT-uIwmjyvu00VFlxK0k35aQ84zz-hh82FIg0ZUc6qqSdMvih4TXumMXi6LMcPREqcvyf95u8HcbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c8836d3c9.mp4?token=OBIY07wzqLKOxh6xkdZvJrPxp75rr5k82GFdXRUIkpt_nxbcfzscKGFXOZx-4CtvZWVb5R_FhlnMkUSIqPGBqFrxcBu1iWLfJvi2ijSWF5AdLygOQrSQKgQymWwWvjGEEN2Epozn9ZU-yGHiuP9ODikDIV55Xo5RwqA-IvTeOqI4zbVureZvZAEynSeGxz4dBW9YIMiudK8CQ3996RqJsiTYZNK1F4KzdF51MJxZ05MvYPbgKaQTlMZpx08Xwf8bO8mhhqg7tGT-uIwmjyvu00VFlxK0k35aQ84zz-hh82FIg0ZUc6qqSdMvih4TXumMXi6LMcPREqcvyf95u8HcbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇪🇸
پپ گواردیولا: "وقتی به بارسلونا رفتم، یه نظرسنجی گذاشته بودن که حدود ۸۶ یا ۸۷ درصد اصلاً منو نمیخواستن! نه هوادارا، نه رسانه‌ها... چون اون موقع از دسته چهارم اومده بودم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102214" target="_blank">📅 09:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102213">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEnx3poelLvysPTaiFRXwGukerLUCXVAjulBOjIE9SAq4E-3FqELxK9G_Jb9naooO4L7Kgwfi7Y9x6WHjtu2PpchB7fIH2uW5z5jIgswhAgWUuLcQhxk4fJ06c9GkBKMVXmZ8RCBa_hPR6PK68K7uK6pZRGrhA5H_X3Qqh7Dn4HRy_9996-4IbAlV2iZpw04p0fibpvYfLfrxQRrkfNqA_12EnOcrT6dSDZRFrPtjax3V3u2mXxNyi8EURsMm_hBWUBdoN0Hg7RUpCqjFIm-v97YrJ87FfPm3p1ictaDiaoqagnk-8HyIqpWaaqhcfu2md1gYuHykGKtOt_Vhy0lTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دنی‌ولبک از برایتون به چلسی
Here We Go
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102213" target="_blank">📅 08:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102210">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AhVltqd2rNP-xk6TknlwTyoBVl2G63w79_YLVst_gYzwDY8IyGasokzMDLkplFmzIo5UiHKDzbx0PXlO2pUg5yxP9OIzujkknUAMk02VkfUj1K27mab9Wl_0WtqxkqXivdb18x6r6mB5ysqGLo2Nd14Rf0wIVT9l6YGMdLY_xC2y1dIsx8DFoX--6ptJH9-LEGsYNbtE8JvrwbQmdcuQFlstRFdnbkVvFtVXQHzbqkqTU87WRauEuCd9_UpIxd_yf-EV7fELk3QDlICxpAfBZ5stJCHJoJh2b1ye5MbL19kulo4xY_wIKubHHbfUaOymrxz4U6b-r-BtzKNBL3RctA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hjmUqUD7dz-R0iF4UJVaxyuc8CtwLleVpRnRBOvjrI5SOTP5KrHhuEo5WVlCiCWEHKDr7LGgIJdJHeRc7OhdcNCdObBre8qzCC3yNa--CbShihCZBd2kY4EW6ZEKO_V01ets-mfAggwApxePJY_jbC5bMFoQR8b99RQylJc4CTZyr_7-lMIfyMbdQ4KQE3FiwOJQQCWEeQthAzUlB7Rq2K5Ry15n1p1HcJ7vlXKo0uxfqEREkhnaibCoLU_ZuM_2fsetQ_FihN1maxg7e_ZFCGpsPqPV2KjkkX27bIBXcrwtk3IQSkjGVfiGJswQjAfwstQ8F9Aes5INIT1lSO2drw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uyzm0NB4YB61sHpXxfUdKh6dGd1sb8mC80lqhHfne0-XO_iQi2_6rCwNF9EZW_WBml_SELYen6U9gqs99bfpw6N4pL-B8E9X7FysXJ4471LIsy3fPcALOmAS0tP5xDMq4DbVtfDRIzy12ZwsUhCYhfrbZIbuHub26cSDynDslh3KsS4cZaiFcnnCE7b1G8g8HIklvw9tUYi7jYxnZ_rhAnUe6Wbo0l6xka6U-QaUkZ_-nsoAi8CqmNNnWjzbagvDxI41Isrc62hy2P9KXAjltOBO4SJj62F_UpCyWaYfASkJLrczeuUltAf5CKuJSnn4P-nxtmui8CxnFPXFvjkbsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚽️
- کیت دوم فصل 2026/2027 باشگاه لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/102210" target="_blank">📅 03:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102209">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsurxKG8Q0nHg2qPv3W37NWDn4q-6u-oPt1db8cNDk_3VBfzKxO6JAtQtrM1h1114w1NeMppue0Zq19njWpaoYgAPtcbhJSOclL2U-UUPIk_gCgATAl78IkoX0ZqLgNtCOeeiAeciob2tGcHQ9tIyc6obC6AkErtQWtQbW9u2NHjJDoVOHaQUy7KJl1l4Wj-_A9kZz0OQylRgjfXTe6tB9fI74BYp-Mk6ERW5uoLYD8opYvg1L2k3gZgZxYc9oKc3CtQEbxwDuT60_BrDjrVXxpRV0iu_NTG8Wj0h1RHFq3OGoaXiS1rZ8h0vs2MwUWdEuzWdKPwQXlKjLyqnOL0vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛ سنتکام: سپاه قصد انجام عملیات غافلگیرکننده رو داشت که همه‌ی موشک هاشون رو رهگیری کردیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/102209" target="_blank">📅 02:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102208">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-1UJWQUYrwxBQqBy4NhDfn0FnCs3hTf8pJvGftHJQsrIJD0MN_ha8w3dMdZfuFMGmNs80jPNw-cdHLvgZs9fs9w6rjHI2dG70hOy_MdARiHTOyir3y7RGeD52TTHvrOmU6ER_M8ZO4AXwgJlrd7KxfIHtFvpyNs_VDumTczafN8UMfTK6iiYTu-zJc6jlKK4TN214gqR9iHGylLmPEEzoUPDk38VyX5DhVEHY0mSKgTa5NgMQH51hye2sN4nmpmx9nihvwQgSCYCQDO9RQcGFPEJxHJWYTF2b_c8RM7NubsgzrmCmo5mRi8XRYgH2uUA_e7y72LEZfWlWuV0iWHZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
رومانو: هواداران رئال‌مادرید آروم باشید. روند تکمیل قرارداد دیومانده با سرعت داره جلو میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/102208" target="_blank">📅 01:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102207">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95f6f50330.mp4?token=LJKLlKrsEAvVu_WDzuC0ZGYuF3tPkHuEB_o8R8xaxd8diweqcAHqdYKVEToK0Rhne4eSxyzP9SfJrM29x8I8YcguqeM-7OU-U3P9-oXMcoMnO1k69KLHn7bFHk4tf4sQsW_XGiTqZvlb2Vs16-UV2CGFn85WXudHy8G3jJsmB4DO-gafoKo_lKR38AFuO8vJvcFOFGrJM3TetcOkxMKBKJ5CqW7odwgMsO93O1PGg5wijAioen6v8ZrxTf-CE_i9Ta-8XKqF75gzFDwjGvMe2qm6G3QvhTNQHtP4eLZIS2M9xBpdjUjqYPzHD728Mm_4ilufIoggwSunBBPDXG499g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95f6f50330.mp4?token=LJKLlKrsEAvVu_WDzuC0ZGYuF3tPkHuEB_o8R8xaxd8diweqcAHqdYKVEToK0Rhne4eSxyzP9SfJrM29x8I8YcguqeM-7OU-U3P9-oXMcoMnO1k69KLHn7bFHk4tf4sQsW_XGiTqZvlb2Vs16-UV2CGFn85WXudHy8G3jJsmB4DO-gafoKo_lKR38AFuO8vJvcFOFGrJM3TetcOkxMKBKJ5CqW7odwgMsO93O1PGg5wijAioen6v8ZrxTf-CE_i9Ta-8XKqF75gzFDwjGvMe2qm6G3QvhTNQHtP4eLZIS2M9xBpdjUjqYPzHD728Mm_4ilufIoggwSunBBPDXG499g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
انفجارهای شدید در اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/102207" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102206">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZlB6ga59H50VgfW6AzQRla2ssv6DzBk63dHD6B5D1hKORaj2FceA4V1IpC4ANOI5wHwcsNhGFcYa9Px5_1ZwX3Ic9xpCb3cUvpDWoDfZujMOZR-p824XkxxTHVsMyMfgAKZ91qiQ85t8uWlyJyvoGl5eKD3adx1sGfNOc0hr-dIhBTAbYxPzw-y2veVAW4iKo3Yl44Q0yKpBLIdTocWVZrGIACxDRhkMl2sXFwpogTFNrN-SJOWGcOHpOUS9GMqjAOdbJQZ0CwM9AukuvfzGCnJG45IxKN18KXAHnzlki9esXEACJNtRvPcPn-yo3N7qEEwO2bhzQnaSrUyoy97KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گویا ایران از چنتا شهر مختلف موشک ول داده سمت اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/102206" target="_blank">📅 01:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102205">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7lwWNkOvwxUgV9ZofiG-KyffwH_8wXvNWsBdmD1HfRFtns3zUvE8ruNQD8Wjd77PntWaTuardYRQHxoW5FqR6jvBpD2hsfxY4tqCESMNDzBQiFbgX5O_--xRCP234NhfUfO0KWkGPdFurW5q2E5OvrbjYk7ttBQdOGn0tKVtw5jkvE4QUHG5kE-9Mz0E2RG6Er0N6pVrcpL4R2h7d-wJx-9tpHYt62ZQNJwkhXgtoqlwalx3DCFg8y8sl36CClxomPxE80QS4lRQH_zmaWBWJxmem-OK1CNoKDj3uQqMfVciNO1AtQro2wIhLU9bmbOuAE73HarYZO6CgBpA_EkWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گویا ایران از چنتا شهر مختلف موشک ول داده سمت اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/102205" target="_blank">📅 01:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102204">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tF38QELtY-jG7G6OXejWbXIJaYF5nxxMGRCcEXX0zNIjSlwPKAZHtd1HEmUyUc_QgyVAb7sZO4K67uJV5tOJhQFBVcEta90d9tfgJre4YxOXqSW_fq8iMKpk8bsCqvwcIcKOxdh7TaJ-4qTnhpo-zc_IC8cysXAY9uhc38RzVFPgAStYh_HUM8RN4S4-pNjWQGioIergJW3ybb943p1FagyYGVnIJaIac8tEnwqb573UGKvO3CiRQy5kRyzSf7qjeSVoRC-crYJ46zkHnxpA3NDJ26L6D0v8XkubRavD8K3gBwiFZ3bcfenDB4lpb7PrhM89jYZLtewoUdM7glGrCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
🙂
👤
تعطیلات علیرضا فغانی بعد WC
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/102204" target="_blank">📅 01:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102203">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7274faec3.mp4?token=ZpSinLJX2FbUyZ_WEVQ3j52dymQhg5ZLHxrPYkzFgDmvlHERE_Na3n829ZGNyXpneZXvqK3H_14xx9L1LohfwSbKyCdJKCO02X1_ELvf-SJ5zev2jnIZ-RWziy-7_fmVV5NWm0PxsuOkcWFXwSuNSXknOSv3OFIOrWOinnan5pdWPoETp8NPT2DujASILGUSRM7jr865753rwGCVRr6oM0SlZ2gN2NVVnQOkQf6O7MNkvhPtzWCMKkwmm9yhrIEBcb9D5u4484kaljqOCITbgdK8GMkhJPIQ3PrYiRUD6ll7f5bt9hxprH1p4DCGSEhW49ktcYEQ8yDmn2Pe_GuKCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7274faec3.mp4?token=ZpSinLJX2FbUyZ_WEVQ3j52dymQhg5ZLHxrPYkzFgDmvlHERE_Na3n829ZGNyXpneZXvqK3H_14xx9L1LohfwSbKyCdJKCO02X1_ELvf-SJ5zev2jnIZ-RWziy-7_fmVV5NWm0PxsuOkcWFXwSuNSXknOSv3OFIOrWOinnan5pdWPoETp8NPT2DujASILGUSRM7jr865753rwGCVRr6oM0SlZ2gN2NVVnQOkQf6O7MNkvhPtzWCMKkwmm9yhrIEBcb9D5u4484kaljqOCITbgdK8GMkhJPIQ3PrYiRUD6ll7f5bt9hxprH1p4DCGSEhW49ktcYEQ8yDmn2Pe_GuKCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
بترسید از خونی که به ناحق ریخته شود
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/102203" target="_blank">📅 01:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102202">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6cm9gZu2FDsgQOx9NQpQLXfKPIiR6sz5XtiNe7a91_q-oU9Ke9CV93UKsvYIkFwizQ_tnC41W33UbkE3w7CIIObDGEA7ZET8NBlE1BmYe1sKRfBpiIYlhN4j5oWdO_zYxESbUFH7W-GlAAkod9vXKC_NfSzOe3ORxOBOL1Uo_bWa7w_lgcx4iq5MVVHu_2_roqft5n-jCPES44slzl6tI3bmxnPxbbGFkYN8IEwJzbCOrM62r8JkC5sJEiB6PebtTWnDj0V0iiyPrhoanpJlWLKUxXLCfPMi8qXk88qFAA0D26Au5UTzgZfBESzFBcxuuQr3DvzNSYkg_5fRSt1Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوفیس جدید بوکایو ساکا
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102202" target="_blank">📅 00:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102201">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم: تحلیل تخصصی بازی‌ها بررسی فرم تیم‌ها آمار مهم قبل بازی پیش‌بینی مسابقات مهم نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای اگه دنبال تحلیل واقعی و بدون حاشیه‌ای،…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102201" target="_blank">📅 00:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102200">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=lzYIQuaChJA9OH3RHyFASoqvReXq-Eb0eePu81mqwy8F2vLVJHP9oCsT5syOUidqvrxl4KAdEW_nHvsPZQSCNUZDtY1HxQT5kUhmbeSCy65Fs90BtpbatjDui1eAQEPVHkzgd3qywqsA34cMrSWXnkBCqL-5G5rlprYtuhsX2RaGH4vbgqep_wHffzJkY0yKNh_mHn9mScvMC6rJMA21k61fM0ev4Vf9dXf7W6Edw107KWXaPo4AavkJ1_3Vz0bym96_rp2TW0jHETXQFlrGfzAwLFfrMNZKcYmCWKTNxipLoqy197DxygMRM_eFdVUNQIYx6iX83FwB7GwOceDQ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=lzYIQuaChJA9OH3RHyFASoqvReXq-Eb0eePu81mqwy8F2vLVJHP9oCsT5syOUidqvrxl4KAdEW_nHvsPZQSCNUZDtY1HxQT5kUhmbeSCy65Fs90BtpbatjDui1eAQEPVHkzgd3qywqsA34cMrSWXnkBCqL-5G5rlprYtuhsX2RaGH4vbgqep_wHffzJkY0yKNh_mHn9mScvMC6rJMA21k61fM0ev4Vf9dXf7W6Edw107KWXaPo4AavkJ1_3Vz0bym96_rp2TW0jHETXQFlrGfzAwLFfrMNZKcYmCWKTNxipLoqy197DxygMRM_eFdVUNQIYx6iX83FwB7GwOceDQ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم:
تحلیل تخصصی بازی‌ها
بررسی فرم تیم‌ها
آمار مهم قبل بازی
پیش‌بینی مسابقات مهم
نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای
اگه دنبال تحلیل واقعی و بدون حاشیه‌ای، همین الان عضو شو
👇
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102200" target="_blank">📅 00:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102199">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQtXQWWuJvFagfE5LNWF9GDih3A5Hqu80Ll22gm-JCqQcs71QW7UyOdyXll2gk098F7coyEcE9SZ_evNsfr7SUXow_DwEdnkqm-QRMfY0AT8ktPMlcU0Tn_Zq27oO1JZrlHC8hbHlfUgu3VwhU6LnrlsziGzaSKaljmf_bqVqZjaF-a0wgARnYA7McLY5-4w1fwNvRXt0Rs2IqyXrjrvwBr20-wT-S3IG8rbflH16-mF7QNcBAZw7cSNa9Zqe0SLeMAsA1vxuMgviRiJE3Y-6GlcAKqloIMO9zfynelWrMHlHJLn2TGzAxHZcBZO65OSUTZrroq7GNBuuQDrG8JWig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
رامون‌آلوارز: آسنسیو به سران رئال گفته تنها در صورتی جدا میشه که تیمی پیدا بشه و معادل حقوق‌فعلی خودش در رئال بهش دستمزد بده وگرنه تا آخر قراردادش قصدی برای جدایی از کهکشانی‌ها نداره
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102199" target="_blank">📅 00:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102198">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJaACwMz9V3N5G87PjxLZvA5W6Jcq7DkdYVpJWuBqd33NzEfFm0aqCVeilTcbp1H0VwvexquAsFlEmG6gh_GKFRtZW-EWiHM94HOHgXcWe-vf3YWJqUaubKbrZz1tmzHeJbAh9zCH0mB2cXSm3fl9E-RVbwXrSCY53-AY2puTAeLf8g2BvaYyVnWXgO-xB1ss9G-ULi8QsTyV4CbTFM7BZN_7griz9m8aUI26d5JUk5i4DJybhXvDCDiV-JA0e2jmREFnlkl8CoYOm2Y1FmlW_Ow-o59Nl914-DvEz-ltE8Fu7ud6wilA4z3l3iZiPJk7NZzp_rmJiIR4GFMVJztmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
😍
دلیل آرامش‌خیال بارسایی‌ها در تمرینات:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102198" target="_blank">📅 00:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102197">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔵
▶️
ویدیو باشگاه استقلال به مناسب سالگرد دومین قهرمانی آبی‌پوشان در رقابت‌های آسیایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102197" target="_blank">📅 00:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102196">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKfAw7MyZIjiJB0rkEo76q_KO1h2wIVLVIe78Wy0Vhw5drynEBoBDlQ33r1fvDmdcfBtDhXDCu25yRh_vagvIG873dDrvGmr4t6Ak2Y2oawQAep7scCNtkj5najmfziT6mhbGDEFNG_aOQxY2A3Kn2y2oUA809SXIYVSvsLbOxVTq1i-az6fXxjyMzu_C405Fa4YlfhcdkFy9-owSPJzZiYTECXwhNjp9qrEh_yp_VA882p85dzlBYwecxMDM1LZdWzvGJVKI80otQ62T4sqlmBwnJ2lt3-mOr4od7aa5i_5b-gbwxI0xi4mt1tToav2UMeGBFAdMZWDc-p7mDzELw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
#فوووووری؛ اینفانتینو تصمیم گرفته که حق برگزاری مسابقات جام‌جهانی رو به سرمایه‌گذاران خصوصی با بالاترین رقم بفروشه. کوشنر داماد دونالد ترامپ از خریداران مطرح طرح اینفانتینو به شمار میره
❌
از طرفی یوفا به فیفا هشدار داده که اینکار نقض آشکار روح برگزاری…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/102196" target="_blank">📅 23:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102195">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBRrf2fhTbyrdbRAOaZlyUGU9ydBfKgj30ireQe2c8RrW-fzUPqz1llZzYtFTbV4HnWMQgQPiQmz5m_mVd_uRCDyvg-0gJ9CvfP3NJk71KZ16EAJY_bZaHNAly6JzmwSQcm21IX3g8CSdiTWP2mSpaGZuYe1uq7-K49aOGo2DJLlFS35IBn2Rzm_Fthpt1WSl0gf45hIk38X0WXsnea4fdXHCgEvoNj-m-yCLHmlYMQbPd8xpk6xWeeCEZQTdGIpWBSlDJXUqiSG21cwSkDXQ9H0Kz285a6quPgyk2AbWVEqJc1hNWxDFX-eNhDe9cYw_6bletTZSzuV8ieVse0AkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیلد:
نویر پایان فصل از فوتبال خداحافظی میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/102195" target="_blank">📅 23:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102194">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgB-vb-RSRePVL0KziLG2bX-DC_cNnn4t7O9DpFk8qQ5-wk31Nt84h12782A-epc6Mnp3fVhz1Fk-pti1rZDOVtu_7UU-5Uw5Mw1fi2UqgxvKkaMgNitcG4cbRtZ_p5DkvGvn-NAGL4gKemfSuFWZpuW7Ta5CzpR3KhatJcwHvatX4I6C3FL3EhKTbuX62i5BVtBkOw2HVTVH4irz0JVMmIHXb0ULu387EbuI_OPTPwaWVt9NYp7AhpMl0PxQ0K33q_GVyFULg1O9KWAOKjeqBlncMBNNUoz7_buscvy-lZq6uU4Lbg_rduxU9VDjoONCGe8m-be2F9BJ0EYehm5wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناموسا یکی جلوی گذر زمانو بگیره
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/102194" target="_blank">📅 22:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102192">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af48b4918a.mp4?token=MdyDEW-yj-YlJO3-dtkWvfneHu53SrSoH-l3UHBzNmfKVOTLhFxxFa27ZPildjlaDNFtX5chnr-GWeQlv8hrjkpXI-bhi7FQxmhw5nfArpfMVmoSH4WEkHcvb9eV2bfX6ZSvUFqMDGE5WQEl1iLORlZaldUNXcgqofxZOYhwBqBs5IujdL3CxI4B3xSiND3doszmTUmPH0u9KGdas7L8bvuxMbMyvxP2Ub3E3sUuIQsjSHu_Arg3BqMAqmfIWPT9AkyJkYnuvDs3yr7ARTYQRgPFWmISltkQht9530rc0K-ceJSsQ41Z5iCZrxV8ChQgBzM8zCUsk5QihmK8Q09WJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af48b4918a.mp4?token=MdyDEW-yj-YlJO3-dtkWvfneHu53SrSoH-l3UHBzNmfKVOTLhFxxFa27ZPildjlaDNFtX5chnr-GWeQlv8hrjkpXI-bhi7FQxmhw5nfArpfMVmoSH4WEkHcvb9eV2bfX6ZSvUFqMDGE5WQEl1iLORlZaldUNXcgqofxZOYhwBqBs5IujdL3CxI4B3xSiND3doszmTUmPH0u9KGdas7L8bvuxMbMyvxP2Ub3E3sUuIQsjSHu_Arg3BqMAqmfIWPT9AkyJkYnuvDs3yr7ARTYQRgPFWmISltkQht9530rc0K-ceJSsQ41Z5iCZrxV8ChQgBzM8zCUsk5QihmK8Q09WJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔥
کافو: وقتی پاتو اومد هیچکس نمی‌تونست تو تمرینات اونو بگیره؛ کالادزه، مالدینی، نستا، هیچکس نمی‌خواست اونو مهار کنه، دیگه ببینید چه سگی بود که می‌تونست به راست بره، به چپ، سر بزنه، با هر دو پا شوت بزنه، سرعتش به طور دیوانه‌واری تغییر میکرد، به سرژینیو گفتم یکی از بزرگ‌ترین مهاجمان تمام دوران‌ها به میلان اومده اما یهو همه چیز عوض شد...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102192" target="_blank">📅 22:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102191">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R95I7qka5dg2vgdNtbO6NFbRtpY0En-kndnjWSqsX_hBQG0PsEsT7EsBLdGs8R5QBsmZZWPWv5FJe3o6alegwA87IqRkSIU5SGd-_FLwc007pluanjnMxmFklldhFX4BwPYC04ZEiMlTFtJ7k-4_GuKHar0g6yi02mYBxPya3uFQKvXCZw6mbfJV3awUcjI7elLb3e-7hANO1WSAIKlABJ5r5nr7fz708zGxY09WBKOl09XFGxrLNceaoeQCi994Ze1NAPK13Uw3r-HTkqzMtzhAALAlIoU6bK5LD1tA_KFsEbxwfGmjEVGNviyk_HAaQ09R9P_uQA7p_RmKZlBZ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کریستیان دریسن، مدیرعامل باشگاه بایرن مونیخ، درباره اولیسه:
هیچگونه ارتباطی از سوی باشگاه رئال مادرید وجود نداشته است، نه تماس تلفنی، نه نامه، نه فکس و نه ایمیل. بسیار شگفت‌انگیز است که چه چیزهایی منتشر می‌شود، در حالی که خودتان حقیقت را می‌دانید. این واقعاً حیرت‌انگیز است. او هنوز سه سال از قراردادش باقی مانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102191" target="_blank">📅 22:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102190">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b8f5f5029.mp4?token=UocgucrkxnjSJMvDknvqjLezHAVn5APypbCQMGC-xJ1c-tIdUcf0tvShhB8PLI2Ui58p7D2lfoSVhBe2NpMSSTpAMIQwrIepPlYnxyWEZuX4NdXRfHq-uvz9Pe34o2rKR_iy9pcj1ODxlvXNr46FX_aqgNJT7PO6l3oDWvxSlZkxtdgAHx2C9OqC9oHycBJ3BKPJ3PaQ5Jgw3mRQjIffA_krf3JIpJSaUjVDRlqhSyHuOhw-TtGiqQuU6s0UsQt8pW0xdgiXKNxG-mCWMWvtpDpf7ROQSUA246-44NOYrd99fAoxWZfJVj24CRydZgZEmqKKU0VlsfSG7TTx5sDMDQdC-Wsrsim2uZrLoDdXtCSkPzFknMNYeXbSDdNtRQFztJfP0Dk2fmQtDym6dWvKPMw7rT7GNGdrDoN41urvO9it03aXD3jkQkT0vjXhMamA1YidxCenwWmK6t6EWrJgpg3v6Ya1KSLJOIVAwkM3I9iGPkJOhom9kAkUpXslwHugfqMCWRnyrh5YJo851FMQ5oswsZCi95fqq7Qu2uhh4_S8_tlWdJ9NChp_v4wgS8l032w4VdaiXXI8r3Dx6zasC9JI_C9xFEh3VNKLcFvlfpNu7CcLXT2Lz8WS9NPj029IS4VNJy8rcxfXbiZc0G-Hphp7F_SDRU3R-M58mta-bOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b8f5f5029.mp4?token=UocgucrkxnjSJMvDknvqjLezHAVn5APypbCQMGC-xJ1c-tIdUcf0tvShhB8PLI2Ui58p7D2lfoSVhBe2NpMSSTpAMIQwrIepPlYnxyWEZuX4NdXRfHq-uvz9Pe34o2rKR_iy9pcj1ODxlvXNr46FX_aqgNJT7PO6l3oDWvxSlZkxtdgAHx2C9OqC9oHycBJ3BKPJ3PaQ5Jgw3mRQjIffA_krf3JIpJSaUjVDRlqhSyHuOhw-TtGiqQuU6s0UsQt8pW0xdgiXKNxG-mCWMWvtpDpf7ROQSUA246-44NOYrd99fAoxWZfJVj24CRydZgZEmqKKU0VlsfSG7TTx5sDMDQdC-Wsrsim2uZrLoDdXtCSkPzFknMNYeXbSDdNtRQFztJfP0Dk2fmQtDym6dWvKPMw7rT7GNGdrDoN41urvO9it03aXD3jkQkT0vjXhMamA1YidxCenwWmK6t6EWrJgpg3v6Ya1KSLJOIVAwkM3I9iGPkJOhom9kAkUpXslwHugfqMCWRnyrh5YJo851FMQ5oswsZCi95fqq7Qu2uhh4_S8_tlWdJ9NChp_v4wgS8l032w4VdaiXXI8r3Dx6zasC9JI_C9xFEh3VNKLcFvlfpNu7CcLXT2Lz8WS9NPj029IS4VNJy8rcxfXbiZc0G-Hphp7F_SDRU3R-M58mta-bOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇪🇸
یادی‌کنیم از هافبک‌خلاق دهه گذشته بارسلونا ایوان راکیتیچ کروات که زیر سایه مودریچ دیده نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102190" target="_blank">📅 22:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102189">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHM6jXRc0qwK7VctsXLDhMnHZl_7GmVbvoTyIyZgPqJVyUTKy9BDt9Ix_n83Z2Uir6DhO6WJK4DteOTg0ke65bf2Anuigg7Dgu-6C7kRvmHZDreovmxP_W5bl81W9mQTPVYa8pVo2JFsUHCKHpo1rz_k0Y6gk9HYP_HctFc7wHEB0lq7jBIKr10zFsMOSyzufZxKfUxLv09FoTyFEauXjmlKYfQBZNpfOtDDlV-OEcJB8HxtANKPV4Bz9zKI6It2tWLQT-l6EidPWrdTILyskvT0tuAQDyviL67_OMxKSDNM9z_gLkmBD48LQOc197747za4j2XiqquQ82771rhjdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تیم‌ملی آلمان قصد داره درخواست میزبانی جام‌جهانی ۲۰۳۸ یا ۲۰۴۲ رو به فیفا ارائه بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102189" target="_blank">📅 22:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102188">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappPay | اسنپ‌پی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtQhyU78fhhDB_f_yA6bqjJFohzQuQLl9no77YyrD-c8YeJi7vOl38CssedTMQmgqA1AFvbKd1jdhkw5RWgve7NdgodbMOEL0WDN7jzDdiskNNIakEQ8q2dQxdRsNk_gjvqe-0aLgN7FrGBeqDkZRgD2to_gcI-36026mSiV2Hx5vBWhQIklE3DPmBdIGBtX1kjehWi8-0C1KCJXUubXOFgoDsQzjYOt78N1_GTxcdknWYD0nbzNHi9PiXKWgcA5qwWNYbX97LpExy-STWXGWfMm6An4LSFxM4ehENODJ2afWyERpRlF9qXsOSpxwjAz5QKTzPJ2JTOFgvNBJNykAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
از برند‌های محبوبت،با تخفیف و ۴ قسطه خرید کن!
😍
🤔
می‌دونستی می‌تونی از فروشگاه‌های فعال در شبکه‌های اجتماعی مثل اینستاگرام و تلگرام و سایر شبکه‌های اجتماعی، با تخفیف خرید کنی و هزینه‌شو در ۴ قسط با اسنپ‌پی پرداخت کنی؟!
🤩
🤩
کد تخفیف ۳۰۰ هزار تومنی: PAY3SCP
⬅️
از طریق لینک زیر لیست فروشگاه‌های طرف قرارداد با اسنپ‌پی رو ببین:
👇🏻
https://l.snpy.ir/v06dj
https://l.snpy.ir/v06dj</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102188" target="_blank">📅 22:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102187">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L22WCqJnbetGz-nK4of_MSra_6j4JOdO-obBAQF6yOI-iV88ajRqOksZMPpC6-ulDjsQrJhjwxKTrNCGk4LxSSzniZ2wcG24Z86RxiQ8xa9lVRA16P4Xx-ybVoFfSEaJbLP42h5uLjJDyNV7vc8hGXr3GnDX1ks8GOpgDUugRQ9ups0t49YIq7I__zvIlo7P02NXWaBVy-5oYhRwMNjW22sk9v_u8r-XFt1X_aF5uiTCA7aT0Bb56ZGrCQHg2_N1_cnwuKHvqPjERoRwmxEABTtSlcnJ33twFGYIDJridZ6bjjPZLpGX4VVD84LIK5zlNd__iqThDGnmoAL9v8lhmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🏆
زیدان و بازدید از افتخارات تیم ملی فرانسه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102187" target="_blank">📅 22:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102186">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDPn07Kh2cB8z0Dt4jfO5J-2Lfioz0fRBdaNuvhGSmeMYqW6AzuzaGk7SbuTm32BNFit6uTJw7HX6Ftlmxwro12tyN_Kt7wOTQKxXyA6iE5DRC3ERVPDdv7OCVKjn07XaXcpmBoxKjumDA5MpmVFPbsmar2636UXsfG1IQxnFpBwX86SlCBbUKSppQqndL1Xe44H-vPOY7Ozp0bOWNZ4eR7ebKlPrEHDcoRqdNXRFYYZ1mVu0OdLgCEUb90okB8Eeb5wrOmz05DmY-XppkrWnyqasZaip1GprrVl0S52XcTayL4CySfk3MeSxqnaXFaGJfSFGvXYEMkrBX3IJJBESA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔺
در سال 2020، بارسلونا تصمیم گرفت که دیگر به لوئیس سوارز نیازی ندارد و او را تنها با 6.5 میلیون به اتلتیکو مادرید فروختند.
🎙
سوارز : «تماس کومان برای گفتن اینکه روی من حساب نمی‌کند، 40 ثانیه طول کشید. این روش خداحافظی با یک اسطوره نیست. اول گفت در برنامه‌هایش نیستم، بعد گفت اگر قراردادم را حل نکنم، مقابل ویارئال بازی خواهم کرد. شخصیت کافی نداشت که واضح بگوید خودش مرا نمی‌خواهد یا تصمیم باشگاه است.
🔺
سوارز رفت،21 گل زد و اتلتیکو رو بعد از 7 سال قهرمان لالیگا کرد.
🔺
و وقتی مقابل بارسلونا گل زد، اون تماس 40 ثانیه‌ای رو فراموش نکرد. نه جشن گرفت، نه ذوق کرد. فقط نگاهش رو کرد به جایگاه مدیران باشگاه و با دست گوشی رو گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102186" target="_blank">📅 21:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102185">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f91Uu5-NxzHmEj3o-aKGmUetprWtTXdOJ5LW-4osmJNgTLQzFoDNnjZy7Tq9OVKNiBIQNIUwQCjmP3nEoNpVQiJXNHIPkChlCibQ_iRhONIOI8KEsojNcWtD_S6Whz78VIYeAX7hwNEI4jcAGOjBoqUIz1AsGpiyrpsiKiXwny0uCQBVUAXMfzGx1x9k41hfH3R8fkp7-MdnjNz-hoddN-OaVdmzxkrhqaYNMJL9SZi4Pq8eLss-L2jEgJZnSlLUl_uFFXaZfi9g-NQX59vMSyHfW_XOpe0sIMx21BfI-2_TdxCTb5OtGDqPkZP85TvUNwNtESvhZMqbJOAYT99iow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب رئال مادرید در اولین بازی تحت هدایت مورینیو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102185" target="_blank">📅 21:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102184">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CM9a7NZbNB1fSa6YyOsBpxSTNLAcyZ7IXHxgiGWhBb1wF7mTiXod2w9B8PWiDgFXafN_Ppg5aJBOneoRdAxA8IkhD7bxzNwe_aZGdULhs-1zPjzOe2dZIjwlG5sIOvNVSJ3tgqt4bfw0w5P5_nbnhkGxKFI9i1ESxe16G5UayJmJF49LEnSV1tbjdNyDnC2Sgz-5xeucIzn0clVCP2il1qcib3yQSfHOypv3Y-wWP7M4SL5QC2sKalb0xFBOGore7cc0O_VvOLgFHjFSmn9HO5YafPjHpzOQQutOtOEdF9XIGP4oVBHM8B-0Ty19cpMo-LZ1V7r5upkOFg0o8oS8Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#رسمیییییی
؛ کسری‌طاهری هم پس از مذاکرات ناموفق با پرسپولیس راهی نساجی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102184" target="_blank">📅 21:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102183">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1j8GgrSEi8VqFfb5_2xVdu4nCv71EwZBqmUu6TqFP_pGfODBIlb9fmqotroGdQ4Q-F_RM5EX5D42all1VACuUmhDKwgNo_25KC6SU61db7tizBkIFtZHxlg1hDtr5W2Asn2fm91sgX6HL96_K-v18tygVoB8x-7oi58cgXHYrxO8HeaH5bVNETrGFH8MYPzkWdGjGdYD_SKyzZARWJnByC5JtjD71C95yuqx6L9siJQX8-wEd3xrUhc-oa9weh8vKRbRh_a0kl41CuDyUu7quYEmK7Q13fC_s5Mi7Z9eV-RaJNtMDNCGw14e1COfgSYmd8bo_YFOfjvXQloK0E7fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست منچسترسیتی برای تور آسیایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102183" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102182">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b71e2610e.mp4?token=aQtbPckP7PxrzdWNw-cDZqKeuFhlosuy57bpP7eYwrF-UTYsB7ezbDn0fRUYneqyPpa3eUnPnEvbPSgH_3316SHcJvtHD_Xg-Cjk4nfajrevxgIEOaN9Kqkae2viFPyNjF0R6et_tWlj2JWHV-KahZzuASsas_Vu5s8SN2pp8KECDEr68m5CJoKRJ0wCBgVFoiR5htmQC0qW-2euGLPbhq0piECepqf2979EUalCS0VTb-Q2ES1DZOI-P-bmkJJAsNYe3j9b41c1lS8vD4wN1IHafMNKeCB4AHb9JE1z-NyW9Hsi5kOe1Z0DvxLXZY-h0Z39M9crt2kcUxjWLMyAng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b71e2610e.mp4?token=aQtbPckP7PxrzdWNw-cDZqKeuFhlosuy57bpP7eYwrF-UTYsB7ezbDn0fRUYneqyPpa3eUnPnEvbPSgH_3316SHcJvtHD_Xg-Cjk4nfajrevxgIEOaN9Kqkae2viFPyNjF0R6et_tWlj2JWHV-KahZzuASsas_Vu5s8SN2pp8KECDEr68m5CJoKRJ0wCBgVFoiR5htmQC0qW-2euGLPbhq0piECepqf2979EUalCS0VTb-Q2ES1DZOI-P-bmkJJAsNYe3j9b41c1lS8vD4wN1IHafMNKeCB4AHb9JE1z-NyW9Hsi5kOe1Z0DvxLXZY-h0Z39M9crt2kcUxjWLMyAng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
وضعیت صداوسیما رو؛ چهره شرکت کننده در برنامه عشق ابدی، مهمان برنامه صداوسیما شده و به ژیلا صادقی میگه شما همیشه با معلومات صحبت می‌کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/102182" target="_blank">📅 20:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102181">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilSCBnfMTLpWOziQ_xmzLm278Eq6ohiPWLsarprAydjil-XhP6CCBSEBHS2qLrSBWxk0IXY1_novkSXQQoCdg4SpcV9dTawzHrw72rzqJmIEz5SINiaFU5knJCJB25tTULV7z-2nv-bzRGTndzHXXADYwkXa1wNwnhnqWXCAQ214GMEnTIXJbOkY6pRQPgTDu3zNd425eQi0lOFkElu4_iE1A_QKokFUEuC2XiTYVbkWu4bg7U5VXguF51ZUyFA8bxi0cWzlAjcJhMr3g3j3Frr1N21S2zueUrV-7q_xxZqOk8XKVI-wfy6ZPakH2NLrvwTmBpmD_ikGmUBkj2ufFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/102181" target="_blank">📅 20:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102180">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be1bfab961.mp4?token=BIwdiG2jX3d3cs9OdSMfrzvhWPD1EELCqr3xnQFydluneN7KgsmEG2YEyVnfRDDJLa3qyF-3w3JOKbASpvE2zRfFk_PMpO6ynu65Onx63j-kTOcP9zh2mL4W1dkCtyDaLO6P42-GgGD4nF5bDK_1k9wKaV1A2eub2Ujum0LNxQJYki_FcUE1p6P2h1aNgp791hEicb3h6-saeDlkLOYsd3pgeugEMEtibdxEoqKLU88vl-P13O7us03a638aApYHuswBKlpk2T1aph2NnHRn10j45xQHB27tOVmUQY5iBedDrYYWJ1BeTiXrRVO3YbW_Bh-uleCsfoYEV4pTxjWq_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be1bfab961.mp4?token=BIwdiG2jX3d3cs9OdSMfrzvhWPD1EELCqr3xnQFydluneN7KgsmEG2YEyVnfRDDJLa3qyF-3w3JOKbASpvE2zRfFk_PMpO6ynu65Onx63j-kTOcP9zh2mL4W1dkCtyDaLO6P42-GgGD4nF5bDK_1k9wKaV1A2eub2Ujum0LNxQJYki_FcUE1p6P2h1aNgp791hEicb3h6-saeDlkLOYsd3pgeugEMEtibdxEoqKLU88vl-P13O7us03a638aApYHuswBKlpk2T1aph2NnHRn10j45xQHB27tOVmUQY5iBedDrYYWJ1BeTiXrRVO3YbW_Bh-uleCsfoYEV4pTxjWq_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادارای انگلیس با هر پاس گلی که آرنولد بده قطعا یه فحش حواله توخل میکنن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102180" target="_blank">📅 20:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102179">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a5b1e0f9.mp4?token=j9hKY-yZltTAj1LMQ7XAx8z89dvn39L5e8TnxoNn-HKDAwwcC95fCQ0aXNjKsoDXRJUxLLE_zbHS4q0P_GD7YPEbDXNjigg5Hb4cg0n_3LaM70MYDTe0bPJGtoeRu41zIIMmYGZihFFLHcWwK8Tocm0nhpsn7-VON8Zz3rDB2tMduTKKiTOeNiV4jR0Aw7hOwdtHcm-YV1a-xq_3YZ8ydNd6kNstMlgsUsX_2q7PXRv8gGEcMYFiTtq51fWt1atEN2qmybH70aulAso8Fa1tvb7O4O219KhKR2OsFl_7xRTvj_ipV1-Cv63zqwsfy5E4bFgQT2UP12UjA213CLFQiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a5b1e0f9.mp4?token=j9hKY-yZltTAj1LMQ7XAx8z89dvn39L5e8TnxoNn-HKDAwwcC95fCQ0aXNjKsoDXRJUxLLE_zbHS4q0P_GD7YPEbDXNjigg5Hb4cg0n_3LaM70MYDTe0bPJGtoeRu41zIIMmYGZihFFLHcWwK8Tocm0nhpsn7-VON8Zz3rDB2tMduTKKiTOeNiV4jR0Aw7hOwdtHcm-YV1a-xq_3YZ8ydNd6kNstMlgsUsX_2q7PXRv8gGEcMYFiTtq51fWt1atEN2qmybH70aulAso8Fa1tvb7O4O219KhKR2OsFl_7xRTvj_ipV1-Cv63zqwsfy5E4bFgQT2UP12UjA213CLFQiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😐
کصنمک‌بازی مجری تلویزیون با تاریخ ۰۵/۰۵/۰۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/102179" target="_blank">📅 20:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102177">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/edm1G1n43zLuR5ipL-5MFN_8PsdQmJMuovdPwg3J1YEamjG5JpXEwzcAmL0YdUWy78YxadfpVu1Il1xN68LHUaASYRAAKAxdFSQhBdwmPSk-ueeOt3NHvVKuT7sX3BWZGCUq7DMrkTHhW82yJbWzGJll8UyxDpVsXq4JWLk0ANA-ZiF2qZzkFotBAqNutG_kPv4bnjWroN0HcjftaKymrZZOqBsNtP3Mety1L8gwM4SRjGaLP_hleO5aWB3qBznsW2_hX3m2rPoE0kyFXFF8L701kjnbxz8kZHCyTr0DpAobxu-vnLATkTiwa0HTNcKjOFyBjbtQLsVOsd_NvK_Nbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bfN7K3i8tsCYHXNVrnjiNpv1hHm4i4HaGlbAkAgv9YQAjF9qXYM1l6pS4q4dR-u6XkcSJt6t-0jlLcPoAnfGFYX2tFDbok6vX31bt2DGlP1q7zBU0qkUfAhH9pgQ8q3HMUFn2QU1mgBqhGKPFCVT6zhk9iumXs_wau9CKo5wWA84VMleX5REAQzx-ECcUkGNzeZ8_tarQKqhQT7q6lUUnt5rm4sy3G_besd42oJaKWDTbLfbupBVZX4xvCW3HS8usmYBo7fPagMQ6KCHQDSl6rS824scMp5dujUWyPHCv6Gxt_719AEgJmiDhU3mcadVRfybSENqf7H_C3R6U_0ZfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/102177" target="_blank">📅 20:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102176">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZhwCiMffCjh8J1HBrK2tVeYp4yoh-GMy9kZe1MisCnJt6Dm7v_INI9DmiLpKe2rVvMAVU_xd7_aoZSiM8KwbpA7pLXTftE7urZGZsxzT3iAD9aKIFEMNCf_R0W1NJxY9BFSMHYWHwdx0dXPkMErKGy6TGMTVJModXDgQtV0M2Bul1CT47FrBM2S6oUchkCE4x1qt4R9USDRnfv9NE_iceFSMogNsRNfW0Ft38CO441eNXFT-vNuUka3-eHL6b3M0aU4Wrwd_ReDb3GG5KqEIP5aBcWUD8c8qlewZC8QsHC2H7WzMQXCeaptejEUqYuTyT7LsiEbh3_2-ZcbWLHM8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#رسمیییییی
؛ با اعلام باشگاه نساجی، دانیال ایری، مدافع سابق ذوب‌آهن و ملوان به جمع شاگردان مجتبی حسینی اضافه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102176" target="_blank">📅 19:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102175">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oANu0ZQJLCQbeIM--En_lKdVDXe8hY8nNiDVt6YsitZWvghl5obHZrIFeL2ALr_onFgCH1jh3VLhda78Tmfg1UhxSeJDNGWjyh5IdUkiE66c5mreB88hu758whmWCE8JKEB0TyqsM8lLURGUIjIQEQcuzLq2E2WXmaQmrjPHRU2tzUQxjV-xlBa-Ho-3MWUmTMMVaGCPqXZgZZBP2TGy0B0CDOVI-3sNDeAdpsjH86Ptk68xg9JreVtm-2dad1NS6ZN60Zat04RAZBdUuFlO4cRDJ9eNX4gHnX0BR3adt83Dx_AtgIZbl47nfWO4cduHIPErojj3hk40-FgnDQVgyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
#فوووووری
؛ اینفانتینو تصمیم گرفته که حق برگزاری مسابقات جام‌جهانی رو به سرمایه‌گذاران خصوصی با بالاترین رقم بفروشه. کوشنر داماد دونالد ترامپ از خریداران مطرح طرح اینفانتینو به شمار میره
❌
از طرفی یوفا به فیفا هشدار داده که اینکار نقض آشکار روح برگزاری فوتبال هست و باید به صورت جدی با عوامل این تصمیم برخورد بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102175" target="_blank">📅 19:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102174">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzCaQka-2OG5jBEqWDty0OznC-trL2dANOcwl1xSc0s0252ZTc1obffD2VJClNZqRBsfia7C5k_laeH6M7hN1qRFJ6e0MrBuo71TkOzoqqo4vu4nqMRM-j7WtPhhz51KHO6EeP-x01i0mlNf38-c-uh7t2FgVhh7BwWz2Qi-0MrQJvauA4-ZxH0x-gvcovEHkUqVdDZ89zfdEsUkKlpuzxlxRdhJAMLI2QVlYw7mEgzbFsfGDVcuX8UAJsXDz1AGqMXPhbfLUSUCWmk5oCJAwY1vyCYNp-UcEbIqmDolBo7D6bWGk68mPlK8PqiqgmQ2LDHxONvkixTS9hJjoZ6BYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
اسکای‌اسپورت: رئال‌مادرید به پیشنهاد آرسنال برای جذب وینیسیوس جواب رد میده و هرگز اجازه خروج ستاره برزیلی تیمش رو‌ نمیده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102174" target="_blank">📅 19:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102173">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cb3c3fae0.mp4?token=oMl4i3-2NkMpJAB-_AJo6OCfuzOnFpnIneFru9C3_IYcCf3a4lPdLM5hUZu1G6X7MIAL9jCIwcYOq4OvGTgh_opTFAyrAVsKiLkMFFc2OjB52No7xEA1PfXEPSnnF-Gp1ehlI2lFp_2BrHvl4PRdkc5UhP814Rrxd-yFIcZWswlQZbzyaVuyWNC1P33d7OavafCNDGRa0Sf3rLV1JbAj49Tgls2IqQ91TygrRGZnrbRcjF9ROyaeqBS-XLDX5qd9o1B9X_1wl7ALGpyf4-uNxN1mz31CSP94ZA4eNxmGOCUnv7QInRq1cBUIkH5GJZzjKHCp8gvQSQvvZsvq6o1bZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cb3c3fae0.mp4?token=oMl4i3-2NkMpJAB-_AJo6OCfuzOnFpnIneFru9C3_IYcCf3a4lPdLM5hUZu1G6X7MIAL9jCIwcYOq4OvGTgh_opTFAyrAVsKiLkMFFc2OjB52No7xEA1PfXEPSnnF-Gp1ehlI2lFp_2BrHvl4PRdkc5UhP814Rrxd-yFIcZWswlQZbzyaVuyWNC1P33d7OavafCNDGRa0Sf3rLV1JbAj49Tgls2IqQ91TygrRGZnrbRcjF9ROyaeqBS-XLDX5qd9o1B9X_1wl7ALGpyf4-uNxN1mz31CSP94ZA4eNxmGOCUnv7QInRq1cBUIkH5GJZzjKHCp8gvQSQvvZsvq6o1bZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
😆
تتو دلافوئنته روی بدن کوکوریا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102173" target="_blank">📅 19:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102172">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/blQ8KGyOBnOcchjrNu8XilqTbMqRwk5PahZTjYPTIR0n0Pst5pVZDkz1qHQbvT9OqbumR5aqBt-G8sKVWJJdpXLLqx5IGae21tEOVvIBrqGeyxfYowal-BSiZcHFaxco38OsRkGMJ_-anxdsqUwrgjGiOb9eMweH8W6MT-9gjXW_sey_Q-VnwZ-cuPVyLQYFpcTcg1raNoT6Axi0uHC52qUNjAN-1NTxxEJ2VIYoCXXyXZ3U5-31EIKx3adEGmNNawLYNvox0mKGoicVVZoOXt86ga_DZY3JrFfrAUGVByAnPuQY1Wc8FDU5XmR9KjxOxQG9z8jyhXTu5L7a5Iq7vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب رئال مادرید در اولین بازی تحت هدایت مورینیو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102172" target="_blank">📅 19:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102171">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/164942a925.mp4?token=RWZcTkNpsb6ynbR8oyRYvDaOTYRHBF88tiR4ur0T2inLn5BMcwyFyjdRHVZ8YYdb-_AbSRyQ7csuLJn2jS7j-vNsBHv-v66tAkbCwoQzYHhGudqDEKlNT7mvxTYXT3-qicF6kyvK40Ks7kozyjW3qoW9M5AZLsd_9SpTpAE_g58bkD9osSADDXZj7v0McPFt3VUWg7ESk6XjXLdbjz0KzhEwD_2CLCJM98yyQrTiGvY6ROA9YKs0TaH79ErhawLRP1uvuzGWNnajDmHhmSx24FvhtHasTCyGidY6d7JnbBFUlfS7bFpG0tS6pP57Uem_US3O_y5rN7IHSiksjqbhVJNoWIHFoh_QwW1Uz0VaFYcPhFfoOseEeBAFzq1ScRsj5QozSHi5YqOR1o2BhhYOKSqG1UWFLSXwWMtm_-pjm_mFkBtNLWY6CgSe6YMFJzxV5Ehjz01XaH-hfq7kyoi1XeIaAQ75r1ZbBQj8BHUlCpc0KouxTbF3ZleoBMKjmJv8Cs5HKMV8Q8nzcGUfaQtjdTXoophp7HKP0tTFbQcK6cF2wftYaOxujyh7hN8rzYfC_H6RxI8e551GEzfNMtvwr9hOd7LYE_a3qQPAP90AA91BK814_OvZ4mwjCrqzKaGI3VIJMYHgnHjr1cmkyISmp5-37p8FOUQ91ihWb-ydor4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/164942a925.mp4?token=RWZcTkNpsb6ynbR8oyRYvDaOTYRHBF88tiR4ur0T2inLn5BMcwyFyjdRHVZ8YYdb-_AbSRyQ7csuLJn2jS7j-vNsBHv-v66tAkbCwoQzYHhGudqDEKlNT7mvxTYXT3-qicF6kyvK40Ks7kozyjW3qoW9M5AZLsd_9SpTpAE_g58bkD9osSADDXZj7v0McPFt3VUWg7ESk6XjXLdbjz0KzhEwD_2CLCJM98yyQrTiGvY6ROA9YKs0TaH79ErhawLRP1uvuzGWNnajDmHhmSx24FvhtHasTCyGidY6d7JnbBFUlfS7bFpG0tS6pP57Uem_US3O_y5rN7IHSiksjqbhVJNoWIHFoh_QwW1Uz0VaFYcPhFfoOseEeBAFzq1ScRsj5QozSHi5YqOR1o2BhhYOKSqG1UWFLSXwWMtm_-pjm_mFkBtNLWY6CgSe6YMFJzxV5Ehjz01XaH-hfq7kyoi1XeIaAQ75r1ZbBQj8BHUlCpc0KouxTbF3ZleoBMKjmJv8Cs5HKMV8Q8nzcGUfaQtjdTXoophp7HKP0tTFbQcK6cF2wftYaOxujyh7hN8rzYfC_H6RxI8e551GEzfNMtvwr9hOd7LYE_a3qQPAP90AA91BK814_OvZ4mwjCrqzKaGI3VIJMYHgnHjr1cmkyISmp5-37p8FOUQ91ihWb-ydor4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
👀
برخی از سوپرگل‌های بیرون‌پا رو ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102171" target="_blank">📅 19:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102170">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yok1F9UVgpIt_3DuFMz8oYxLjrTAJbWsfg5fVctOX9aOcW5MuGpiZBoKWEMiml4sBYOEURwt4chcMrQER2el4WjHMA1tCMzviZ7XLdqmqvb8uNvsNEbPSpEMzZEe-RGOCWfsBQIcb113YxpCofiH2bCL_W-mcP4WhudU7s0RXxZw2QYALmPTGNkOb_Zyo7UUIiFVHHO4s9nlYaOTqtL5Wv9aC885yPSQCCUdiITJjBlHl_uqCtmeq4ocOHRa8oyeCurN0GVHoH3pIjLeLwv06782Ee711XJmV1SzA8w3Of0Cy0M3JcYRu6iHT01-NtJ8OwbS_jKksCzc-PpMQXE35g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
‼️
منتخب بازیکنانی که در پایان‌فصل‌آینده بازیکن آزاد می‌شوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102170" target="_blank">📅 18:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102169">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-ZmYPq-SuJLFv1IUAR8d6JfBVhvzZnwd1u8rULI7wZpC9196RwNxKYG0R5cl6lbe6qsyo1dr_9k0PZ1OQBKFvcabLmW8ERmDzwP4_gSg5GNr4AOt-PgoHpVdxgQRBq79TVO3rcW9lXqqz6tdTaFNEDdJRaqdduWhHKFAVL3UfvQzYtKfy2JS-IDgkxqR27Xph3nlx1R6Q605Muyw4Dnuy3Sfs2IxiVXFuDH_0KoObrykDDjKyxE1Xp_Y39uYLCqyqUtolsD_RYFl5x2STIa9mOjmddlEMyc18CP5mwWIOrnuKtR7v2YP0FUEqvGrsZzb5fST78sQGguG-DnRX4u1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102169" target="_blank">📅 18:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102168">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMRAAGocQvzHW6JWlvSju0zlq-RJjbLyKXhVz2dcf6Nf5u2wMksT1fXeJtYjiUzOUIvPdWvTyVszuCrD9WwqLEV5MPKi2cIsTNupDbtAYspRSWU0-uhMT48ZvgPvC1ntru5MktZQkKfcL4-rHfCtLpSAinYnBIFgz5GV8ewDCuvLNpinnU6u__L7_VUPEIErKklNn_pnP_ibXdO5YdLgl3gwoCVz2aKN0pjYnvDg2uAORAjZeGkpDx6V7k4vmbn9IzPb1-LzLPXFr2A1JU6i_loOLAB1b0byiACD9mJBqHZtrr15ldnQy1gAvZmtVUsTEIJrgWedm3vIKkO-NmBdMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗞
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: ساوینیو به منچسترسیتی گفته که میخواد تابستون از این تیم جدا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102168" target="_blank">📅 18:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102167">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOwiz-5olzFriFThuNbE-3ObaQ1pF454zsJUoQO6-8wwHA-8HkeMFEL_2plXdhos2gac7utGKMeY9UNEQ5CTEWAHp1hbbuLNgVTXRI7csSLVDNc6yZmVDtRmefgnTWgge9LCKd66Jnrk719qG6DXbP3Z-w_-Hdo5jfbuoXA9_puurNEmEkW7pLEnXiBAisFF2kadYIC0xezYqayWV1DFamCDUXa9xItM8ghGTDgGbUALTelmrNCWp7yyFfD__kOyAIIPWUuw3Q4XeO1clXj91haPZqEEXGRF4XU2h9-MrPd46QH6TX9rXG_7rtZ4TDmcgMBSeBol28OpyDCgPvqRfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
نیمار جونیور درباره لیونل مسی:
من کنار مسی بازی کردم، مقابلش بازی کردم و باهاش تمرین کردم. باور کنید تلویزیون همه‌چیز رو نشون نمیده. سخت‌ترین بخشِ مهار مسی این نیست که جلوشو بگیری؛ سخت‌ترین بخش اینه که قبول کنی بعضی وقت‌ها واقعا هیچ کاری از دستت برنمیاد. از زمین بیرون میای و فکر میکنی خوب دفاع کردی، اما وقتی صحنه‌ها رو دوباره می‌بینی، متوجه میشی که اون کل بازی رو کنترل کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102167" target="_blank">📅 18:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102165">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H7j3vak948GrREEX2xPCHIaDfL6A86BHyLIiNAipS91DHJaD9KLZ103Ec78SMwqR-oKSXstxV8oqnyLgXe3NULIphQUEQGWFDZT2QjHwwO0ABW8xtw4GyPfZI534h7n5fuWHLAdY-1fyF-v0gFGE1QXB7ySoBsG0OtR5vGBtcj8nCYOSkneHlcU4wcXnMwujzvIUzss3g_JJVufVpG5WNSD-rwDJVbn0tRSFQJHFjIH8Ysoj0jHRYUYItvaPyu6HqEwGCT2LHHuj5Nf6YrwzutpFsXTPvB76piUy-1k-jbWbshnlhSDNUfM6N9Qr62PFwCUbWTnB1NIAAZQzVa1BtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dq-vUxcayQ4MY54Hm5CThW60hJh_vy3j6DOC2ll595eS57aPj-TwJ4vh6quVmN_5X0HMl7F8JcyOf_l-ETNQgPkd6DWtTGNE79KKovTNHqxN-mNjYepq-8fBcLK-uGpvNKBlU2FURxh9vC00dCA6EDidnVgZTaU2MUvNLkGKyCy9ipxw5kUViXo9L5ZW6s7pEWE6cV5uPXEdhIoNiLfONySzd_4JvlbiU4Af7D42KkYfIqqfRXrVJk3MEFz27o9MVSnNVIkn2n8lQMJPOc93SCAQREtidKdwbDJyjYxFF0eR9v_3bA48TpXoYZM5TkM9DXGy4viuLTWLLZ8SZdmFyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
🇦🇷
رودریگو دی‌پائول درباره اینکه کریستیانو رونالدو خودش رو بهترین بازیکن تاریخ میدونه:
این نظر خودشه! برای من، لئو مسی هنره. کریستیانو رونالدو یه ماشین گلزنی فوق‌العاده‌ست. اما شماره ۱۰، هنره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102165" target="_blank">📅 17:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102164">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ft2qJtYUXauaJg2qOIEL9slEaEIysXPk6Qie2GYqwE1nStk8koPz_PRn9NdTeJONu8fJGQIqmwmo70UQeMuuLC_-fMsWGan1Wd5YT4RxcvwUT2CEF7-UaVlGmdyo5nb1yDiZlrV5UV-JcT8ipYspPHUVaEHJ6sG9dWGecBa_OXXNcJnG7N9rHpKNiP5eQsNIRfRRnt2wMWoUDXEH0dY8C9dl0HjRwUFvP5yfXUTtK8YM_lQ_X666BXn5niotDK4ymGKAL364SsLVye9anr1Kah63dVFMmofj65R3Eo1Wwqk1DN86EfMCGAjVnRoLsHAFjhhw9aW3KLwGBksZPuV6gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🤩
محمدمهدی‌محبی بازیکن فصل‌گذشته سپاهان به پرسپولیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102164" target="_blank">📅 17:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102163">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102163" target="_blank">📅 17:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102162">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102162" target="_blank">📅 17:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102161">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102161" target="_blank">📅 17:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102160">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dixNRMTFjslWCSakhKJzTNaHwFo0JZMLFU466H2SU9_UneaYQlo2Ab4Te23W0n5rXUlYtXNzX29uX9DFKy4aouhXXXqD_fqUbgNxDp29wJpGX6BwCp4_BSfzm--RUPHaPCcsfFZwj840WjWLzPjCm7AFqZdqEpnZh4de0BKLGCFKEynpoklAlBBvajzOaMSIyGwmHHglNhFjYJvVfGsCorxustRglyUP2kobx7YIIiQt3tGQg5NC7nI3YyszJO5vFBue4rVXx_xTu4K9Vn_t5W3dRscLVQ8oyDWH-S4CXciwPOzHDnaW_DD7gb9YmS5QFC1euHb60RlqfpjlAGfubA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
روبرتو مانچینی رسما به عنوان سرمربی تیم ملی ایتالیا انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102160" target="_blank">📅 17:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102159">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_egxKVnjlWxKLTQjlJl0MJ_vuocsNRzAENeDu8z3zHqnf6l7qrN-pjTDDyiyJWbIJ13-SVGZoenQS4-l1bjXXtvgiqgYPZgbSuV7ApPjOXotH_0DS2CCZ-Eu5PPIrBRWAiTutfL6WLdIhKqWpRSr0C53NQbhjeryxL4Vr536pJvDLQGXLaEjnlKsJWekoJ2kWoD3PGpgMKZ1v7AdLdFQ2_N3BJr4RBQU6HeSZxA8p6PJBMBj-uu6mqpL3cjeY4MKpOnigXwVMhB6NDCcwVaxIRdvINt0RKP1O10m7MzXXt27IsxWUgulvZzlydXrmJteXx43lXik5kibmrKDPtJWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗓
برنامه هفته‌اول لیگ‌برتر فوتبال ایران
🔵
استقلال - مس‌شهربابک
🔴
پرسپولیس - شمس‌آذر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102159" target="_blank">📅 17:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102157">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZatVgcanNWjyG2mJmLTkcbpBDe-ZevcaHJwat0ep2wmOfOFGwT-EeV1ck9HG6avandN-it4Cu9WoKjhA-255BGejGqDj8y14HzJhfDDYRcddRWDxFWQn7UGFy1xl6DMed-A5gEJw29djGPhf8DNYDOt9pa4dqzvyfilxlhknpZ-QMRwAdx_bkxFvfDbgwht5lgZLU5EJ9IyS0V5s9Z_RCd6fBmUUlTYQXjTzdquVYvlY0A1HJXOWlclyItUaKuq-VpRUXYVhfq84V-xD_-ZDJ0nOQ3KmfHj2P_j7WUdDpD3ZZ56nH7otUQ_RaqO1BgEapXUKbEW6IcOZxDAMU0KiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c787f96db6.mp4?token=I3d-Okov-iJCFbNsM7pi2YbRHQ7_kNks36eX2eRdX3mGX_tVAo1Zf_DSnDFBuUEaWQXzF1vhm5Bx82UDPGPYEZq18siKqfkD6mIUq2BqInMQ-g2xLrPqwG8XZYNMN-XdDh37AUJJx5BG1HAMIflt-qkXvCid2djYGJvDMDhQas1njlYw3S-jBZiLEDKcSWMetrA9ZJqoJClIIq8r88y1NyYWC58UbvGho6_qJt4CE4QjWAThyhFFXBVZ86susmvzo7QVMFPH9aNhEwY809VAhJDRZQ0eI7W08_ZwkBu73QuKRv3It9gHVDdnZv7S30-aZ-w4GeIxJFFhsymby-PF1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c787f96db6.mp4?token=I3d-Okov-iJCFbNsM7pi2YbRHQ7_kNks36eX2eRdX3mGX_tVAo1Zf_DSnDFBuUEaWQXzF1vhm5Bx82UDPGPYEZq18siKqfkD6mIUq2BqInMQ-g2xLrPqwG8XZYNMN-XdDh37AUJJx5BG1HAMIflt-qkXvCid2djYGJvDMDhQas1njlYw3S-jBZiLEDKcSWMetrA9ZJqoJClIIq8r88y1NyYWC58UbvGho6_qJt4CE4QjWAThyhFFXBVZ86susmvzo7QVMFPH9aNhEwY809VAhJDRZQ0eI7W08_ZwkBu73QuKRv3It9gHVDdnZv7S30-aZ-w4GeIxJFFhsymby-PF1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نیکی نیکول درباره جدایی از لامین یامال گفت:
من قبل از لامین هم توی کار خودم موفق بودم. این لامین بود که اول بهم پیام داد و با وجود اختلاف سنی ازم خواست وارد رابطه بشیم. حتی گفت ازم حمایت مالی میکنه و هفته‌ای ۲۰ هزار دلار بهم میده. همه‌چیز خوب پیش رفت، اما بعد از مدتی دیگه پیام نداد و منو بلاک کرد. الان با مدارکی که دارم، میخوام این موضوع رو از راه قانونی پیگیری کنم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102157" target="_blank">📅 17:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102156">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
⭕️
🔵
🔴
دربی پایتخت در هفته پنجم لیگ‌برتر برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102156" target="_blank">📅 16:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102155">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaaN1mZQ3McM3-UoXpVsezMbWWWw9da6rW_pfeb610st8dzQCQEq8kODxTRwLm6-TYMmxFKIZ_6_CN9bVIkelSFtzAwEtM_IjkulLBCP1c-nWcu4PepGcy_5oXHpqtAbmY3IK35fy4Mu0lsk9yfAr3fuZ5L4FkNcKLHfa81phM7VIFvuUqqqtGzv_LA_rmPJwWf8Gaq_SRi8f2AhcwnY0y9Hlfv0ANeP7lWTBa9c2j4F_HBtqcvU-gH_pYIuNKxS6CR-Sn9G9waoW8kAKwG1p2ZlIEUBrzFYBZx7WtEdWFiv2YvcnEXsovHLcaCVKjgOqj_lDv3T9g07gFFKLVQxxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از نشریه لکیپ فرانسه: لیورپول با بردلی‌بارکولا به توافق اولیه رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102155" target="_blank">📅 16:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102154">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbg5RvfKzBWq-eL1p2YxDTElzGjHPtu4lj7hl1TAKBlPbKj70k7wKuU4wlR8H0p5xhoU8sPSEfIdPYua0Um3wgP0aadYiVuStpqmgcIQI-UTaEER4NpcJLAZxnKxM0jCnxor-6EFI8u55cHNKu2nEnhIRACpMSBNQGJk6RCpavyQtbuZuWBgXDa6y8wQ0eYkY-eKS9o2epm3hehSJLW-UHZp2lvWB3W6u20s35Q4oKkA_9E8USa4h9fW40GmxgzsgMx9kcYPtrSDuHY52dTliLXPetFP_WP0Nlfm_BktsA0XlTpRL3aGwOZP23smeGMC-v-lYmDjKE51ww0FBakdDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🔵
🔴
دربی پایتخت در هفته پنجم لیگ‌برتر برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102154" target="_blank">📅 16:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102153">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUZWnTm-wwPVgzdqKEhH-thEItsVgVuK73fdNuIeRos-j5zAMzATXH6Psmq3__3d_33rH97ebq1WMTsgu_Ijkao83TMymT3fQzPunuT3xztuL2cjcF14lMNTGtoryn3ZTKB_Tw4vNCcJDkiSiIPjpIiymXFQoPdSZ8bsDeb4jhe5hLFUJSl9Ozvsx88IcPVmmjK_iLrmHY8zGgA7b5j0WRauGkoydHAvpCpzyjA7wC2r51_IasJoeXx9IycZbcGUHmajxwyxRwC3KneKTOmUx0oWCExanYnHG7Fihods56wZeCJhL1ENDuH0JP_ho298NcA-xcc_2kBtmrHyXKOqSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🤩
محمدمهدی‌محبی بازیکن فصل‌گذشته سپاهان به پرسپولیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102153" target="_blank">📅 16:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102152">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHW-n9ZECLKdlW020qpxgAv0b_yun_Xh0KfTiGvhMOUkQoVpjmIDO3ygLVk95Y7570LTfk2mPPtzXmi7_tkguy9LBrDA6dtPvX2z4rzKWW_JNZGeXEL6yEvdnbN-dUCe9VRtrpkXinEruRZvhxNjHLjYPFImMrTEPSD4Kbn_mUnT_kA4Rhf0O8ICTIGt5vFRCIPY2fX2zxWdD7uQbPWKn65GZ6d3JkVivPSTPwn9M-cx1uDuhwuzzH4-VXUxiuv-3PLb5e_77ZyaTRd118gymB9NMP6Q7h6SWbCXWsAe69doq6YBpWXjTahSJjaWmAK5Cb87eTYT1e5UQzfLtNl5MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
#فورییییییییی از رومانو: مانچینی سرمربی تیم ملی ایتالیا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102152" target="_blank">📅 16:34 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
