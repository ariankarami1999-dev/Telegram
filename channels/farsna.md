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
<img src="https://cdn4.telesco.pe/file/Sd_fsjzUosmXMZvdJJhhA8gUobCRP5iRKyBH-L1od2wbnx20LYYwe_OuSCGVtx9pE_fbfa675sIsHnpu4DTy1iPIT3g1p_PEg3Dg0mpGW_RZ7rf0nDz7PRO33ydNNjD9M8EomfZYjz1XNdnDEG-ihCiVBGCpwt-vpFQNj4_ljAQXkTBTXyEes5CjGbTrq9vohY8E8XYmMBY2Rlk4eUA8mUZJ0RkRnBWRPamghgNSCth1QKe4B2MBeI2C6DBf2e6oYvKHvb7veoqJeh3HOGz2xePNpz6NHXSMBnQwAHvIebj23bYalqvPOHtiMtKa03LExxX8b7bCpXOS01AQ0dtwNA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 04:45:03</div>
<hr>

<div class="tg-post" id="msg-446924">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf236411b3.mp4?token=trpKHSVm9ejaKKE3gARz-ssU_27iHyCiKcvzIzcztiLPIVgGKMAwBBOEhzI1OA2tbalDLJ78rE-MNmuphjgPWcZopQgF8Zp8O5q8NuSjUzTr-CcLVQTsGiX1EyJcb1_0MDZSmWEPQ-i8CFncloHUjLwMaa80aIMfWLVJIiLuEVfOAdJ9qSyHNj3Qns2nIbjdXC1AyTVQakuPJLoZme-QU4iWVzjWHVf4h2Ks-qq1rl0HMyX3aFTHmueuQ5wGodIfkbmToRGAwGd9qkt60w7AyspdbaX4hiYvUHjI_ot-KVJYddSDN4Y2xn0zYtylVjd1mWjSwqEClrBIf2f9rT-DFZhs1k0HCpA6lPThylWHHGpHTRs3Xt5efQxqR9ePt0u_v8oSbhGALUqZ9xJrXSld_dTrHHa1pGuLH3-VnQVhQfZlTB54mtaB8Ouu8qlNQWN7PMTKULc2u2lO1nmyzrcZHtEc-_XwOxkDqqhZm-z9ldo7WvIuVx6qUZASHwyuZmVHSE24P5umhTkBzs9lpLvwWMWt0C5CRsSAg8dHz-8hy_34fO74_WYvZstIvVn7PP4iYgHp_aWTreWA6Qp4_2c6Qn2Q8XsEABQc9nHhxMw0Pblky9B54vcmK9RYaZp0GMhSnCQaWhnShugejf4mnICkTbvdF4h6Q3uxM5fXjbrizFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf236411b3.mp4?token=trpKHSVm9ejaKKE3gARz-ssU_27iHyCiKcvzIzcztiLPIVgGKMAwBBOEhzI1OA2tbalDLJ78rE-MNmuphjgPWcZopQgF8Zp8O5q8NuSjUzTr-CcLVQTsGiX1EyJcb1_0MDZSmWEPQ-i8CFncloHUjLwMaa80aIMfWLVJIiLuEVfOAdJ9qSyHNj3Qns2nIbjdXC1AyTVQakuPJLoZme-QU4iWVzjWHVf4h2Ks-qq1rl0HMyX3aFTHmueuQ5wGodIfkbmToRGAwGd9qkt60w7AyspdbaX4hiYvUHjI_ot-KVJYddSDN4Y2xn0zYtylVjd1mWjSwqEClrBIf2f9rT-DFZhs1k0HCpA6lPThylWHHGpHTRs3Xt5efQxqR9ePt0u_v8oSbhGALUqZ9xJrXSld_dTrHHa1pGuLH3-VnQVhQfZlTB54mtaB8Ouu8qlNQWN7PMTKULc2u2lO1nmyzrcZHtEc-_XwOxkDqqhZm-z9ldo7WvIuVx6qUZASHwyuZmVHSE24P5umhTkBzs9lpLvwWMWt0C5CRsSAg8dHz-8hy_34fO74_WYvZstIvVn7PP4iYgHp_aWTreWA6Qp4_2c6Qn2Q8XsEABQc9nHhxMw0Pblky9B54vcmK9RYaZp0GMhSnCQaWhnShugejf4mnICkTbvdF4h6Q3uxM5fXjbrizFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرائت زیارت عاشورا توسط سیدمهدی حسینی در مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 892 · <a href="https://t.me/farsna/446924" target="_blank">📅 04:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446923">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🎥
حال‌وهوای لحظات ملکوتی اذان صبح در مصلی امام خمینی تهران  @Farsna</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/farsna/446923" target="_blank">📅 04:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446922">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🎥
مردم حاضر در مصلای تهران شعار مرگ بر آمریکا سر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/farsna/446922" target="_blank">📅 04:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446915">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k9uK6YaepZC7pIEsO5gDZhpoahc5tODkuI8VAJD3wYwFJC1Vo693yxPSx5jHdzxu1coGRuiIxJquoGDVh2gYa52ldQF5lUoX5jW0s2pvfydgFNVVw5kUZS7rtx3jTWSEs4aq_937b1wGsa9Ii05d2JzXHVGZq2nwqS6Q9QoaMeSPrugxqASZIFs6t3keJarPq1-09tTZnFrb4u-GPpV3St4OQ5VyJ-Hj3Wzk1saxC0_GQ0JH9-NDUAEBEQApxM-h8_ZwO_RO5Pu9qXnxnFKG9JiL97vJ2wHFDPXh6p52-xWaxnrPD465xDb3FdbPEJ-sbsRCyAJip1STQ2O30v9Kfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dfxWXhkHW-Ks2FekLVzvuhW3gs_yepx87EA0fWY1iWfmgvIosz3_sOZjdhOAoeKjz91GCl-lZWB8fBPNyRxGbcdLvuue5jGdvlj0bsQ_Q0H-AOKKtE62z0biDYnPjPk4y1QR3ByU8QjISV1v1HSjy_j3JWp_FSp-rddBEVZop4ZfjHI5U6kYYXIapxOMnvecf8yzN3FsA77JZpfUTj17kcfSkFtVj8uGpCHiC1xh8s0fimqBqT4sMm-6eBFC3r-zzi2S4Pi5VyxBIbQmBqaMFmNAWNN0yitVSBFlTCBofuQ5MNXzbXLfHTkQluCT3Jk5dngf9Q0OUzhlRyZKSV7L9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kae4YLYY-RXU6eKsbhv3oESJggyQVrkcdnFF1gI644md09zBzkfecCW5AybzTa8dhT14PQoQ7bTQZ-B5i3tmPc_KK6mNako74KMH8DToERCyX0Pk-ivPvyU-AjFlkju2Zrtea4pK1y-ffVIaTfvnDcf7JpTI4cqr2c-1ADQpHNpWck1-_wozcwwomDqO00nTzoB6T91TcWHs0B0Ogk2Vg8c5k5AtrWo5iYPjBnqFTWYNqQ_uxbWhRqxP2mG6LHz1k20-hXZ02LzB7AyXTMPZe0rdqTX7bjgzMUfZT3hrR-zl5TBcb34ad3GgWIXqPhTUa0RJE8nqSOJxCpbnd2AWbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kbKCbxYE4BObFEsEbvdBzv0RoVIBd7bO-nhhSlrDcjDaCIMm60vSsm8O5U1QHMDuPXlhkcLM89qfipKO66q94mQe3J51tXJ3eUDigjX9NaGWhcXTsJ8RBZ8ojZIaZCjKIauhx_T0WeDwVGUxe-uYKEA4XamzmQIMcPcSq-W7sRGdVL4Bssz1ZQXw1l2rnn-_VB_hn2qwj4WstBk26Tu6-w57-cyuwjQDOheeI9R_qSoY7HiCjX8mSY3cEVXavX2OPo-vxaLIATf7eLEIUFZuymlCgmju_py5YkNgedaNnOcpf60ShYpkYQAC7wbKfFe6g2JaD9PAd76VZA5AMqhzeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EQKYfCHPbanKwwx-wDGEEA3vu2k1PSRQ6lYKvHa90JTw2zGNHiMH_XnbDb_7SOlSn1AZunEmuIg4PasN7GY9ugSdATK65_QjQ-e15rmeOj8G4D6-xYmnSIuwTyxO_aELtGPp6ip2IjCRMUOSY_BfVuGd4_H7eGf1I5gFQaFfNEzkMSLe_w0HB1D4JXMzhJjcM2Qtz0Hy9DVNL7a5pi3w7XKg-XxOWtQtS3TVEoEl-aVmmQR6o1eggNcXuhqor0I9jtp7LYDV1WGV_qZvlI3mYcqD_wpJ8QdbYdGl4f8bVdM4b9DYA6psgh0tPNPJaOYYDl46qksDBuI3D8qYEeQ3RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BNSjB6Cd_Yg3CReEi2TEy1ew8waW8LvKDhVOmKG_lBpPu42XTGOWMRV2rKOMOvuqHCiH9IIe2YuzJu9jhna-DQJlNpVzVldnrr9_BO4p4jyULO5luu9apX3p6DPT36XhuLIuNJelaPRQ16vBfhijdoRTcRm-vZhRkSdVfpyN2bE57EahAJwItFgWhIYEt_cwNbmAmkW3_SRTKoeuBn-rcV5IE3w1A5oIk9ZRXUZhiYXXjkxw8Yc_8qarXTKN8EAB34edpmmw922Y4VtVhroVZBUlEQm_ko_aMxeRtvxbKFsyteMkWUGQaNFDE2ZdMqagRw8vM-uDO7SUvoXKv2QrzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dhAG4rsionej3YLCiH0GmZVgDexNuuFT-WeMvgTfUz7gN8FG_hlvcP9UUmNDEjF_F3czeYnwBOtqrlKlR-5UIGaktKJ-2syuLokKD9x8zB_mxFsO4P4-2IwK8DQuqh9Ug7_DEGmBlTWs6TRpYNktjd_Bct15O3vm7IDG6mdnaiqElXxSWSXNDxvVGu8Td0sHe_3wVH5NJg0u2te3N1aJnyc2P9zclObWhk80yMJugIo0KP_YnOtqUhf2SLwHu3UHDoX_qI1Jxej1OS4pl8WZYgYdlqShGy16kMFL7Kgx0mCd9QMF61brPgrBJLMY6k_11WuY-7mv3f_PlbglOE3U_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📸
وداع با رهبر شهید در بامداد روز یکشنبه
عکس:
زینب حمزه لویی
@farsimages</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/farsna/446915" target="_blank">📅 04:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446914">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🎥
حال‌وهوای لحظات ملکوتی اذان صبح در مصلی امام خمینی تهران
@Farsna</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/farsna/446914" target="_blank">📅 03:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446907">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QNpTmjUBWK55HND2XtKN2M0bvAGqVBQlM6Dn8NMlukbrFy3PbiAmruVC9X_8RHNsp4W0Ou2iX2KuNq6QFlIAFVBx6i9nuQpdEFUWa3E_uKbAPdlOxwXLn5jJagLn1oPmyorS4kVQM8BqZbXpJyuSikNvRUJtjM_-hMNvDmWYPhZEUkiTvIyXwvfEvOhbUwrQbm-vzy0eHZM79YyyiRZPWEQ8hanEYkJs8FNw-064Mcq7G2_76M5YN_PNiJuJ57TL00Bd-3rKmW8C0TWB6Yhjxxzmf-Pmtz3DNzBqnMGinhtdQmCmdvM6sLGKBlZ00OJ1XuAn7qClZM74wsUJhvrKxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KcsNffTruWG1qhphOk8wiU4Ovt2AZcKgtoERUM1WtjIeSpi2hB2MTyQGZfn3fDny36gn1PLTdEGogPpaeFeDKt9-NCbfHOIw4RkMEtstVUwi5GRJAics9wFDwgpFrEWRHrBd5xy6ZbSKQglx5ierEv93YrbC1E3cS29P7MSskqMJDiM-wq_3WnqXSMACSCILxb5uv8ZrICCXgZD9kpfJ3WovCcc8VHTzhU3zrsg-7PH76BbNN_X2hLH7dwp4watyKm40mKpwBRoJ5DbOyrMVKQsll9Z1GDADSSY4gt3pu6D7NOML2vlwKcCaiM2OpaH4Jl3cxG3lOqKdlyh8U1g2NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FtvpvzHVKbw0VsiURP67djrm3BtYCsJ02XAMSoD0ietOctsbw1TAyca8YGKASx9MfrV4jpJ9dD3gJ_vFhN6XYc7kdg7CbVvYEMr261DkMDVdDfdV9IxU-ALQjztXBgJKe8QjQTocmEgK0_KZwGPKN-mGMiVV1GWXgNTQGs3ZJBLwq3YZz4kxu3KBua1ev72_JPATA0Y1eBPCkPsPoUuFdlNwIfQPcypGwH99V7Tg1ayPbN36PFpYqgh7DPuBjjrKkazQSGzRTMDPwy-B9nhDW7ZZ6L4KL-J_kS9G05HtS1aFQr-fJL1hERB4CNIOP5uzADq2Ij7mFyv3pm84L0qcSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3-9z640mC7SWgpMdMaAMG5ZMb4BMNoxXnzfCRmPvNE2jkUqtPmzrjLmuc7SkxSqGqLgP-dO4qHqsmbXXVx4LOwhEGxChuAEi5n1bwuPcBbgMpz5ABbPcuMmzo2nKhBwoybXd_JHXxvyzdxsxSJFZb9Qh95lbSiKll6pCjL45vgLLtCy3NVhoNNgvU6LUsCYioVlpYtPy0MfGRd4ZORzsqb-eWyrrZv5VzHOMwOppnhomb36BZuNPc-7kNBSzV7orMxX0cLczzAvfG34GiGqth-mHO979-cNYIjDvbofmyxqWolHqd7iSGk9hia-thxtOeSHLAjf0bma14FTFWaRhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vVRBIMy56Ht_uppYDSe2kzDd1ZRZav39KBKRbbOZSo7N70Fysi7LeoRiV20l4aYWd57H5lIYtJjuDCHhztakdwVp5y3ysXg7W4mTiP7jkz3_Pd7eCAcWNKfvD6dSZv9m4wA1l2MtSHPhTpqwbUecxgQWTSt4uPODRwiulKVSA-xZ9Uwq2cVpwS1DHlj809Lr9BaGWXwA0V-kzm0WSBMTgGZ3Iw64-7OjpF9AV38lL-S6IAaKJL4XR_EpydaTOIsBv2wOBPKFrfLBu-5fvAbkC-pAqq1CoTB0annVUajBJI0EQciCni8j1gDO19IrtWurvAlVg3Ysn5CzhUu0RLho2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M-yy-OHdqXus9jRmhYPQUMXxsEoCeQBH0qfCUkEkD1Q8kAI5WiCvEcwBHwS3RrDKpZc1y-QKMwVsCZs-Q_YNPwPA5FPRwt5oQEjDLIZX8HMaocy8eDdd_mxbv4B5r9rK8WSp2MSkkVWwNUHm5T2kntxUDD37kSlmTUrn1vM1j-cuyxNMNyBw4BmtfjJE5lc6l8CM82t2kOl6rGkqLIStXlOMFPQc2YKhhe2LV51t3ZQOHh8tzZDl5RpsZMXTMi2dwyHiHNI0c3d0SZht8W5kB6_SOvx5I56n8jsSvQOFBTIqVLhGUrj-gytyHmOPmELOIGvJIg1OriSGF8z_nnOk3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/djCFF6jWp8iXkk2TFHxOGJbAIa0MuDaPwaagLqshHQ3YGiuVqxanRRw-L57hCsRdFDGfadTJLlO1-42Kl464Io_09feclTozsQuT4KQLnklcB8Wy_3BwZe8eNa2esUeWuaEEOus3-tEL8rXuKcnk-xWWfMypf8h2vURMOBkZfTbRlgf4bXZoTqae5AOKcJ87t7IoL-2lsi3HXiJzRf9z3W7KCOlj8oW4xPnwyW3hk19vbZtpNi1aieR78YuaAXszA2TDUKLXGzL5acBtZYx7NTjuIq-A6QwVlAHBi8bk4knWx5sIGc1-x6BjuaAHuO04-gJKPwjWfxIlvhviM997wA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شب‌زنده‌داری مردم در مصلای تهران
عکس:
عادل عزیزی
@Farsna</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/farsna/446907" target="_blank">📅 03:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446906">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e42455d13.mp4?token=FwrQO0Q9DsPBM3yOlvQNiVp7X39oNUvsZzEVIai2vXZdrLckit7SXwPi8BZP3RsWnUXf7TNOu1zBdmjpXksqg3Fpe0lxC7hxY1kPwx5vMSlbV7h72bUzVAGfCII1VZHLAJW-bwrxMhXKXC9j2Lh0VmA7N40VJDki6T5hqF7jAC3THWHTlDQvc6z8ON-n4Btm7LO-kEU2bT4r-Wi8jCrG29_o6g963U4DTcJzvbcXBW8IoHRg9teuYnVoWDugwNPezflYTWwxu9lv5_pbFfbuulHMn-T0PP-K3YdTMwJLiJ4FoSht7tDQus3UdHIHafNLb5uRf9hxTo4Ee9z9Yv9z7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e42455d13.mp4?token=FwrQO0Q9DsPBM3yOlvQNiVp7X39oNUvsZzEVIai2vXZdrLckit7SXwPi8BZP3RsWnUXf7TNOu1zBdmjpXksqg3Fpe0lxC7hxY1kPwx5vMSlbV7h72bUzVAGfCII1VZHLAJW-bwrxMhXKXC9j2Lh0VmA7N40VJDki6T5hqF7jAC3THWHTlDQvc6z8ON-n4Btm7LO-kEU2bT4r-Wi8jCrG29_o6g963U4DTcJzvbcXBW8IoHRg9teuYnVoWDugwNPezflYTWwxu9lv5_pbFfbuulHMn-T0PP-K3YdTMwJLiJ4FoSht7tDQus3UdHIHafNLb5uRf9hxTo4Ee9z9Yv9z7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بین این تابوت دارد جان ایران می‌رود
◾️
دودمه‌خوانی مردم عزادار در مصلی امام خمینی(ره) تهران
@Farsna</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/446906" target="_blank">📅 02:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446905">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifC5brto6J-1z0b74XRy--QP__bd1iO5FeZqxPoOXvcmel-CgRIwgSe8HYcZGrezlEF2cgljjPbJtrvosn8cHUXtMRVQAmM25FLfPoQMEJGBmGHgTVh59naOSROwjoW0XLB3Jczn8A952xzazgTDw6qMVtCJZRB62K2mvNdpWKnOnLzAf1hSsIlhTItvGnwcJYUGo4Sf1cadAsOoo0q-BVLY3rr2lyciflMKTtn8kP_1ZQ24kP6m3jZ2lemaZ0J56wI6Rvv6hjevcjjc9ZKc_Wua6A8FuzjYbtf1YZhStgRbp_jHMqAnEZmndgtHA4usZCrM191mGEA2EMX8V9jmrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
هم‌اکنون؛ قابی ماندگار از وداع باشکوه مردم با رهبر شهید انقلاب در مصلی امام خمینی(ره) تهران
@Farsna</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/farsna/446905" target="_blank">📅 02:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446904">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LqoyMPPwrlqVU7YzwTQ46DxNCxrTiEATIJxCxu9XVu4c0-Btp3w9czb5StI9os8FoFNRnqD7kkMqvTmmXJKeg_ZQuudANEbdF7O8rwSjYk-HLCPFawEHZP-GijERrI6zWAPAGFrkxxfOJD5bgf6ndibVHtDNMLe83uIn-5GwqeJ3_Mbr7sCcycvlnJt0JcBT52GFe_ucVHIMpEWnvLYchpHqNrBFzSNh3ti12SnWv-vYq4bN1xdOsmsYLXICz1TWIOog5Bqp35XBtrgruvtY5kDlj6FZdZSRkeuqSuOpPxmqvLqIr20pPntfVI6AHtX8gNYSUXwePhEnsdHZtm-tsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمده بودند بلای آلمان را سر فرانسه بیاورند
اما آن‌ها امباپه داشتند
خیل مانع گلباران‌شدن پاراگوئه و آقای گلی امباپه
فرانسه ۱ - ۰ پاراگوئه
@Sportfars</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/446904" target="_blank">📅 02:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446902">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e1554e3c.mp4?token=rsz_3QXHbeoZ68C1_WGGyqzGCo06vjfLx4wmRwrsy_XrjejsRFW_--yJCD5E2_riNxq5wvHuOvc3KnO3pf4WKhiOvZK2M6S5y9rVBAY3F__74k2FeQEL6CGE7NIsCzykFlEOIOx57y7LeHUxaX2r8OqehdtzBvIa9LcFtc6nvBaEBgNw-r-Q9zpPXyJ1gwxNiaGQksdqdP8kPsIG1Og_a6H43OHdzEc2zZV0esJidrrgcxIiaWACQJC2TePlCez15DuKYJUGhJGALle-_Sh7n32Rodhpbsq3efy1I5Sy2XwoaKnCnFB_tRpDAZmErSivRvyCJNNZ6h88gk8q_jn2OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e1554e3c.mp4?token=rsz_3QXHbeoZ68C1_WGGyqzGCo06vjfLx4wmRwrsy_XrjejsRFW_--yJCD5E2_riNxq5wvHuOvc3KnO3pf4WKhiOvZK2M6S5y9rVBAY3F__74k2FeQEL6CGE7NIsCzykFlEOIOx57y7LeHUxaX2r8OqehdtzBvIa9LcFtc6nvBaEBgNw-r-Q9zpPXyJ1gwxNiaGQksdqdP8kPsIG1Og_a6H43OHdzEc2zZV0esJidrrgcxIiaWACQJC2TePlCez15DuKYJUGhJGALle-_Sh7n32Rodhpbsq3efy1I5Sy2XwoaKnCnFB_tRpDAZmErSivRvyCJNNZ6h88gk8q_jn2OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت حاج منصور ارضی در مصلای تهران، از توصیۀ رهبر شهید انقلاب به وی @Farsna</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/farsna/446902" target="_blank">📅 02:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446901">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87fbe4868c.mp4?token=VG3NSFI1A4eOGWuR8lt3PE5BoDuI-8QPwkfFvEghujdrcCfM8HaS8ALbAY97ejtyyQvxqFwdToXFL5FydabWIzvT9RsV_cVWLLjLwgyI-0IaEkhEEmOL3kt4BA72E5clfxRDBaR-c_JZhbwtXUKjqYnG3SPJ8ZZOjzsAD7q_jc-vHwlazNZoQ8WnMLPRRMp8CFs1wA2zfatkvLfnG1nz7QicclAdsUdB0SBAUWRNeV8ICcBTlbQmrgrHVQAhCeiufoWdTZmz5DhrIcymxa-XPNwhEXD-r-4LtdQTyJJdr05fplU_yV15vW9PU4azoWhXeGUmreSh4xeriBvaufbpwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87fbe4868c.mp4?token=VG3NSFI1A4eOGWuR8lt3PE5BoDuI-8QPwkfFvEghujdrcCfM8HaS8ALbAY97ejtyyQvxqFwdToXFL5FydabWIzvT9RsV_cVWLLjLwgyI-0IaEkhEEmOL3kt4BA72E5clfxRDBaR-c_JZhbwtXUKjqYnG3SPJ8ZZOjzsAD7q_jc-vHwlazNZoQ8WnMLPRRMp8CFs1wA2zfatkvLfnG1nz7QicclAdsUdB0SBAUWRNeV8ICcBTlbQmrgrHVQAhCeiufoWdTZmz5DhrIcymxa-XPNwhEXD-r-4LtdQTyJJdr05fplU_yV15vW9PU4azoWhXeGUmreSh4xeriBvaufbpwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورودی مصلای تهران در بامداد وداع با امام شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/farsna/446901" target="_blank">📅 02:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446900">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🎥
روایت حاج منصور ارضی در مصلای تهران، از توصیۀ رهبر شهید انقلاب به وی
@Farsna</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/farsna/446900" target="_blank">📅 02:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446894">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vLM-fRxX0s1wr4Z1DcUzlsdxhVAtMvLmm_Vr2nuZ1wBoUic6MAgIyD6IgqOe7GphpuO4brTPIKCu4IbEOWMoYhvd5NLjcCsmrg3ascMYDpbtW7NXq7x5BQ9RCn0U67AT-AmyQhxiwccLK-3mV8e6JwDUP3TMWC1YRqDRQ9WtyoLvgpshjBpK_Zy-vckrdBRnwK-z8C2yi5H85_R1u73a43epgWro1pcGMhm3RwdrQjft4Q94bKYHVdUe9aJXIqFrOkTyjZTd-0O0FVVV7_0IHXb7R1ZneYhPTrubx0lNHRiqpDnUhMMo4aGivypI7fI-E3lUadeJqwMv_OWJyCei9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mytn504c249E2V0CDERY8t2i03zPF2hfnpZtuoNcOzNXYsV2OZyTo6buy9d_sJYdHhpFrNdqlnhzucvNTvQt-bLj19InL99-fpMMr_vaWPGiFkp0lp89K43owWDZ96B3kCg5D77uuQsOUjeEnjGGzLActg7GwO9Ik5tocUApA95qnSqd4WdfRG8HyMQVXgdOvybJMIgY0wBrU1ou09mjO5JIty3XjtS_33Pl8fIvIBRhrqqnxB8fj_Jr0qoLLdypvU4qjVxZ1VGfo9boddZQziuU3dVCT5D4d9uWXLcbPmmqFwD55pHZxXpLQ7rTvMLbSrkUiRZqHONcobkjAhbfcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S86ZE64jMgsW-TR12iq8mIMrv3yaxJ1fEekpIlM5cyna5_I9368ZpXfNy46FUvlrngI8N9BEP7gEuYNWEQFE14RFbBiourEmBUCBjGQcgjVXbh_GtZuVmibJ1D7WOKxEYJV0xToq9yuPtwmNL_9VoxgepEVVoKXpCJu8ubaqLQqAVVdF4fL-kPU_UFi7cQnaPLG2O9DDJm_cf8tI4w0Mlv--mGsS-9LoKXHij9r1z0efpacs_fLdjmFNTCpe60Fwnw1FXwqRptv7xwCXjzYKRSAsUpReNnj_0_T-U8uZfIGwXOi72yrgr7hf5-GNOPE3IGNkdmUuNqHLK-VaCfiXQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FBpehx9K5S45n4qMbczVGxmntFWQ9o2bgRPQMvgYIQUYwW-Bssahe74gp8IbFtBni3nNqotHOFe_c5R4aeFVSxypGp6U9Q6QlB8L4B_pYxRn79hKe5-dmvkbG5yyCqi_yYx5Z72qWauXjyK-MIAO1bn1BI9PEUL1tHkm_Fj2p7ahv9cJsGAxa7dpbCJwaQ1ugKpgBqpWfHHYQeihMW1Wk4L1RSHwcE2W7YZfhtEBipfXGx6VlpNkj6KFglRUFuZmTJVkrAxXfOhKkBaiRuL2FUhHl11TgUMw0jYyHe7mBP9DppGUqrQlZB8B01uo8K-gQSu4EwgPPI0ByueWwq9l7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dvPb2S_qXte0SomkZYXcECYx3v-NODe2xNbfuyu3jaPaUo-a0PKzZBoNBlhBgsB8-N21DbDA9pdw5VCF6V3FBy2s8nk2pTx6ymA18VoaKeuLLAeKcCZDWiVtbMbBh87iR-r9j8AUoBFN8KeBurKE0gt0qxbV83EIJ6N9ZmJdb_gwjQ7kQWvCmX_EyETaF4lTkiQPN33JEGux9ODHRkZTjudgQwHKZ-YRsbljcUSnFup4jX5xBnmhQRP8SKh1hGrLtQeGitxmbj6W42XuB-J5fDHDLrk8hUTeVP6fX0CvnLWmS6wNhUbCbjMLikf5H2_PPgE4bP0h8fRDdzX4zgZnog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cO1NiV8wrt86nCpDbjECRMvbNteQNWtZ2V9TbAl3KABYfDeE7wkAVhLvrLD5z4I97ei_e6lUL6MPG5nwKdOmKbS72SSbduKC9M2D0-tGotWdaknKtvnJVxf_B7tGWBaG9Je02X7C5TZbmO6qJOfz0gOnYWUtyud_Y2Jb3PwtmRv3FuTXntWsv0igeZpFMnvm7L3EWKlCuQes_FIQNH14j3wueMO73xivrj83Zw4TPp1Vl-0n8Qi__rUmkxVJ0rOQbWbi6Ld-kUeeuZwpxMUHOCpSgoMabQakMC7GOeBuG2_ui4Op8DA9pKZ-Wiu6Oz7JoxtImqWCHPBYrPms-1FbQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دلنوشته‌های مردمی بر دیوار وداع
🔹
دیوارهای حائلی که برای کنترل و هدایت جمعیت در مراسم وداع با رهبر شهید در مصلی تهران برپا شده بودند، کارکردی فراتر یافت و زائران احساسات و دل‌نوشته‌های خود را بر آن ثبت کردند.
عکس:
مرتضی مطهری‌نژاد
@Farsna</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/farsna/446894" target="_blank">📅 02:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446893">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be7ff4ad8.mp4?token=Q_K48Sy3i20WrsWDr6EUIoeuQoOm7md_tMDP0NWup4_kXB2wNDB25AM2cfRMcHvynndeQgPfIw_Nuz_ZB7I2SA4Dh_3x7x1QR7pzJSQ89AqClG5Sa8LJ0Aa3J67QeZX0OtuH1M0Vuk6FXNrCjzwpbWW9TghxHQ2HJpXzTBNnJ1Uw_xzRUBV-xiPGttEuic5BKtq9NcuC1Pe2ItandFXNhffKj_5CcvTvda6OIDZZ1kkGS9rRFk_r4E-3-89T_0VR0taeGvS_U4pAnJrbM60W0U0Nz7h6ccIVw_Igsad_SDHrSkul5Z8Wjvsz-oNE5eTmALwc3Tu615d8PBlqc1i20w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be7ff4ad8.mp4?token=Q_K48Sy3i20WrsWDr6EUIoeuQoOm7md_tMDP0NWup4_kXB2wNDB25AM2cfRMcHvynndeQgPfIw_Nuz_ZB7I2SA4Dh_3x7x1QR7pzJSQ89AqClG5Sa8LJ0Aa3J67QeZX0OtuH1M0Vuk6FXNrCjzwpbWW9TghxHQ2HJpXzTBNnJ1Uw_xzRUBV-xiPGttEuic5BKtq9NcuC1Pe2ItandFXNhffKj_5CcvTvda6OIDZZ1kkGS9rRFk_r4E-3-89T_0VR0taeGvS_U4pAnJrbM60W0U0Nz7h6ccIVw_Igsad_SDHrSkul5Z8Wjvsz-oNE5eTmALwc3Tu615d8PBlqc1i20w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد یاحسین(ع) مردم حاضر در مصلای تهران، ساعاتی قبل از آغاز مراسم اقامۀ نماز بر پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/farsna/446893" target="_blank">📅 02:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446888">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MxizpY-vzeshj2pIxF5CsECRBXHToErtyO0nevoc0MdmbsZ-lQryQPNWrQvvv-Q7lw7ah_Ip7CIlJcbIgG320-L9haOssZfkKMA1RZy0rDi86L_LfcNz-P-9neUlPq7nRdYdzgzBu957PrJAUzX05NSU0tQhyYB3QX4GYgl68IPML9m33iNEzh-uYZq_zpx-aYAHUZiPIvx3mUGklnuy9hJxRaJEy7ZwUw5gmBTBhi-PYPUtRNtYQMZnh3YSUNJT67BiAPgmtsQUBu0d6yHQ_YQ_4nqbiGBv1m7ApH_qzvxjfCX-znOFQZfRRvU5LAtpQmrcv9Vg0FK_pRNgrUma1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GcxgZglDUc4bOVtc8YPGxhxfyUyIT76180w7I_DNYJo8VjQN8uIMI4cn8P5T79YkeJMNzQzXElVCv_YQsO-d6SBLtbYnV2qI3dQuiW8lzmjfkSJ9JEWS55H43t0eS8qnRdCctUMIh3yID-We2RjrCliqWMSF5YCd_7QBY0S1lmyDoesYOX7PHIJc2VLFh4cAGQvXTKfnCQLsCQXkNpe-Y-4-ydiPjZutKlMnMSK7dtwG5NXLaoKVgQAm0RathgV70vfRWxgFtO5vEGkZzgdb3ohXLqLW5jyc1DC41P8OIrOFtzb78Y28TlM4VP5uUT4hIvFRjxvGkwkEPgFKB6kn6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mlT54oSD1zIZJ2rVX9HGbtdniX4aM4pN9J4undmuWO59hQj4LIwqEXlBEyRHdh3iw_izL1f0W-qBsP8ihuAfahtC5qfSuOr9hz1EVqDQgU9NAy53dt6Ma-C9rM0OW4QuHXANdV8S_zaRpFkGgyaAnCbZbsep8e_wu7AKCk8ZLgxjMIEPjsoCr19v61stzIzCvZQW5lCFLxcLHBdgALbwvrE1Rfeo2lUTRTqtVteu-PWo25soxndWKqMye6EhitlJdhp_sler2jOhrtFLLP-E9wOLbP5ylRQ--Ea6-8TD8-V1YwJVGWqYa0Ldn86Uk_cwyBwmiNVz_54yQu1hMAS-uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kk3W_EP-P7Ko_oaCSXHS5y7ZwKjD99K6uLVRfmcg1csiRllQiPYMMWuyqm5155EXxdpPrYx03WqexQjN6hlhuYSWCPCH6LDiJHfz7wmZZ5lK8xfNGkidHwC2S8VciqdU1znDIHHfzZtCKPqQ8nHnyUklP0CxkVT2nBUcHiEDJHpooK8q_7LADzuzi7uQXAcSTH-qANTesV_CCgQ7AAvxcGbX1Xy2iNr-FqEw16Qn2_56AoM2z3rdJrj6uz80f8qJ9qgc4HncC38Kkc5oq95svK5sz-ks_-kIimMDP-nY9OssRoPWyCBtCPKU6qwkm_S923ysX-QgaFmFY8hBu06PKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iX59xZh-J9MnlqI0_L-C6W1nreJ1a2BdYAgqKz__rkaMDprpKHBMucH1ovNVZvOFYK6ick63BkOTsi6dVIl6Ty55LnnsJaRLcBSlp_Td89dTicCRCLT3KnouVNbYhTk8A7QsW7ZLeKuk3HMq4QN1aADouJmtwGpcymNBdVcHn80QDUdLDoLdUHy6BeQ5nWeZXJec93At-4uZR8C0fWqTdbcBsT3dpnkkCvAyPzUeECz128fi2khJeJMtRr_ITJIgmOAnJyRXeJGUephkNZpU-fTQiPMtJBicaLUJztj8tfS-zd_SrBpGsyoUPFQzwd2qPC2CFANIRDqk3aA5-apHXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سخنگوی ستاد بدرقۀ رهبر شهید: مراسم وداع با رهبر شهید انقلاب تا نماز صبح ادامه پیدا خواهد کرد
🔹
از جلوه‌های ویژۀ مراسم امروز حضور خانوادگی و وداع خانوادگی مردم با رهبر شهید انقلاب بود.
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/446888" target="_blank">📅 02:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446887">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/050925a26f.mp4?token=uqBc2vGCMxRqT7qbcvXGNiWwTPkqAS49qHtNak-p5k_dYCD6Vbmwk0_tBXBCTSQ8tQHhX9HsqVMyx44fS4kbHViAiE-3PM4Xt1r3PWV5I7fjUvcg5hwBOtiGgqXb7FnnYlQdP6s2oydrS1BMJ88msP9M4apVwYq_WGEnJ7DXbG98a2SQwIAGZjE3KCNERc39h5UiFs0IVoZZ593qUexoH9ZOyBlQCMjjSOtdDtE6glU45OTdkA4emdgsrUzsgdBHo51U8DG3V1rxKQjh9AFIT9NGGLtO45peFhFyNgEoPFeYpzXiF1Umz3m8XUUZaomCLUDm-PVnq8KpOcNdcsGuHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/050925a26f.mp4?token=uqBc2vGCMxRqT7qbcvXGNiWwTPkqAS49qHtNak-p5k_dYCD6Vbmwk0_tBXBCTSQ8tQHhX9HsqVMyx44fS4kbHViAiE-3PM4Xt1r3PWV5I7fjUvcg5hwBOtiGgqXb7FnnYlQdP6s2oydrS1BMJ88msP9M4apVwYq_WGEnJ7DXbG98a2SQwIAGZjE3KCNERc39h5UiFs0IVoZZ593qUexoH9ZOyBlQCMjjSOtdDtE6glU45OTdkA4emdgsrUzsgdBHo51U8DG3V1rxKQjh9AFIT9NGGLtO45peFhFyNgEoPFeYpzXiF1Umz3m8XUUZaomCLUDm-PVnq8KpOcNdcsGuHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای بامدادی متروی تهران  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/farsna/446887" target="_blank">📅 01:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446877">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f2Nqixbc-wCFtc-c8z_lz7nivl0oD-AQj-mXTa2lMUAjWjfEQsmzunTR4-H8LvUJ2OhHNxV1x8gEoi_75ye-JAGJCWlL0q-LITXmNfblbmFaTUjIdRyMDFop9-TkGio_A00-Qt6HeXnL1fwYBOmRsFX8RFwKJdEB23LV-okWM7nRpGF3DwAHAibFxfwH1mMJ-dmm10RqZ-bgYrHEIuzEiQFFUgwuwlVPzuWWc4FlxMMuDmD8C7_9c1SPtJlaKGhC1L2O5FHuRSMnlKsSBMFYcdcsfFUTXrmp_T2zvv_MXvPeTpLMCCzCJrUxI4ziskASc5tZS_hKn1vGFgR-dGZF7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rZ07LNqs7yqFIg7g9_NIwz4h1j6ZFInLc70XbR3RFI9zEFeVZQZIAdq6NaLTJV7mIuznXykoIJ6F3nx3CiSquuxAI9pDiWqf_7-oCTJgZRlsD-QeQ2t0R8qF7DTgiDgbmdp3dLCrNUzzIiMp35BWgszE4q8PDzQ_d7pbhoPJImLxo8Ct0zm2iEWRoIehVN_9z1Tup1WdjYOcNJPvGK73p_515NaBcxsaPKAu-qh_YzS0FZHbvwr6wFmp_ZjbHLoIO4goFsPgZCoGBofTo01oLSSfj24zSAs59k-Et5eCNv6PLWEveqUuKVMV2Tfrb69EQPRVBoOPQsEpxXC9FyBRNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o5SsLoqxJ9QBKdup7E6z7wCkLNP12hX9oZ9SfQjsIq_1g5Xpa5M8mNHb7Hfy-cN78HUdsQOurkg4SzOpnNFn7XlbaryNyGldsEWUSxIO4cHg9tJR-s6A0b1GJfCvzxVspVmdh218BdtqMSD9pwUBU0X-fqap74ZJZbK_F83Q5XrrAxIhAJeOxmOk9BUwPNHbJnQ9yMwaBgLstvOAuWvcTUd97XbCTaBIxZPXn8Ywv183Ve1Z5XfthofPSKZ9LsFk3hmxe4N7ffv3F0mMDgtctrjICRCGIPEppJaOhyHzWN_qS6NZGMD1I07QG31RwZqMup_DmVxaxsjQMyWMAaWXxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qmETyGuXjQJVQFZukWRXOMszb3hlfojTbNxlZKeQL3HqdGgC6NOnqLAIqUjYJIcroHfRDBEW2HFn4uN876sGDDzVKUE3eMJC7tqPDv3_gyRISI_GaWJDFfCQTMgdGkkFbW_JUam1pujb09Y6nxhC_ourNfCYHeqhhnsGeVnbEP8QvnaMQftUR4o01_c685h3sRTE32tMwPUzi-ix4-jMJOi3JRpxxpukMal-3heKX1PLIsSdJ9C3OEioBCg7MYvwzwKUst6icCJLLyKMY7JnMOdzYE25nzSju2l-ffdLYtj_Waw4egfvtwJ8omvXfYTRRaPYLMVE0EVNmQjOfiWWjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LrdHHI1J_R3ZdpGHVwCaZW6RGMtyLCg8KrhqSgUErT_ZuwbnjLoOL87OC3GaMCoW1StAgSkgtocsISEsTb-W9LWD6iA_RnJth_yYIWwfg8vCYDemTbI92W7WQYg1pr-QERrQQjy9r7e-m4TG3tSP2gR2LySbWlxWSIpbcbZvJWr875l5WoSgVrKOKJQj8DR_FZtOtOKvTKFVhUVqXWJJjHO-u4qEKPypklQ89jAAEFh2Q5eFRFaYkNZA1aB4ibPurX3DXsqsszPgc2HyzWSUFu9A9Uhpx_CEOgkgdGafOgV5w-Ge3-mqRqRJV1sqhyCqBaXHjHt9pyIU7cZHsPqtlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FzY03Omc8Ao69hPpVOBE0IKgqye_HXb8ur4Qm2xOCeYxF7RYJ0x0xm_GX8CQrEVXarmwRYzSwXhGFH5Dndyb4zxe53hGE2hu9LB0vzjLDpxEeAYieHTuITestXEjw6utu54Vlzj2tn68do5LFvtYocssJiqWfdyg_nlMRnEpfIOoXMdYD-LCbsWjpUY9e4H-IX3LCSeNWzVwhM0lCKRvaA5BU7N7Hoh76oGxNXXAn0IWk8FJ941GTsg5RGtuPdr8PQKZS6PIluRJAtWhWJqqQYfs-_lqxDNolahAzoJ-YPc20qeVXm49aq8vd9ObBBJE_4dAVX-Dmk3Na9fooKe6KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SQpx0Vkh-IgisnWXo8ElyoTSOH1X7gMwsha9dZuRrDApiMfb4hS-x6yOKkBsZ3kalK8YKGp0u5SItaxp2Fp3HZHtM-Q4TdFSuyGr7QN_PTXEt22sDLerqqJnC_9CRcv_qJ7_E0BJbDJgSZi0OKpDBuRC51CuQ0ewCwTy8XIVh4Ra-IZnD-sQVFc-pODEY9T0cB3o1xS60cmylBesk0bo0asFbbqqesYIPp4nOgZwMMoIcCLmI3uvCg1X6SpUIbIKQwhs6dwof-hLjq_TnHDp8KNGaKvRMZeKYJuG-v1zRrkzBhFc7_KbV6DQbeKoQjgYVUE1yuf9INwZzAgxBH3WOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bmzgNNuX-APrrRzQx6x8pVjfxXeQIyv9OvRMVTsPlDY2WBN5OC9F8HQ2f4OAF6Wstczh1ACJtGnHHYHVwoRFy0YhA7u7_TB2xIi-MLR5S7Tktu2z1PrLgRWr_9b6mVr5mv-zRdzY7MQpuF34-a666pntXlGmxaCirVhofKmMd5ZXYZF0FnM9FRG6N3yLKreJ7oFs1mBrycNhCpp6w-9950yZecuKxIDoPoUgLW1Q4fIe8S7RmqhFeufHF6mVfEsgp0itXN94At0-Y6Q1ZY4DExZeAQv6_F9PY8RFaeirPaKJur8nWw_BnFYjXGlqEVwVaewer4OzZAy62YXwU7F71g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nCujacazkvxO0dJUZ3f7haxM2e_lef4LfWazw7xyeUqO8PbaUVNJmkueJMJI51hu5X7b2yURPxuaSnv11oPHF1ytxMG-w90nIeZhXw9ArPO-IueZuNeG3ghQzmmwYlYztada5kEh8uuUUW5wAvtIh4jrmOWMdhGPkCbkGJw_scQIMOD5AKnvVOFuez8oz4e0TD5D71Ci-PP3B3EDlUvynaaP-LBOrCAYlt4AH9-mKbPXA1SB5m4hY-N_ISecsFH-pNdoZHKKG3XfUilxedlxf-SABdE7ujIfIuKU2bc9VRcE71ELAvY9dJhjb5wnAOCo3Jm5y5Z-cy5lSRZjNOtI-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VtJ30nYcSPL9nR0shjEGtDhO3avHLpA_Ksf91352R190K5RRrFFCKg6j0ZMzwOIazJgL5SeMxlgYbSJyv0h2NTYnGafQuvJmagab6VxkIWMNJspoRwgGyd0801p7Vmcy8kJbcySuUUN89_mU6qWrgcTe8kGYz40jPUBUPTrU6-iVaXDinE8nIJaVxg9qPEvvJpvMyU3I92Lh61ZRKgj57fZZhEKmnzGqPY73w14cjf6c94aPjlPzniVXwVzdFA6U8tC3zMuauvBMqssosffw33PuCuX5dMk8f6NYT-IX8dv2tCV8_Eh8LKD6GX9o-e7FVL46EXjgeUghqTkHdtCdyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حال‌و‌هوای وداع شبانۀ مردم با امام شهید در مصلای تهران
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/farsna/446877" target="_blank">📅 01:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446876">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3BRFnzc00kPfvmKZSHavnOfRXGSTzoQ-bbC0ISXbictxStYTNqg_vVoZ9oNXORT6s3Zx3dZUgGb0GTQxECCFFDH0-YtDCF5wo_2HK7eXffcCzs3ZPZJ6-joJwEcy9aUFMBxvWMmZLXKP-fnuJICU8M1EhNbNANL8Hc_MtiVw4qmIXMtbPHgbtmNHGQC4J5stKaCMoey47Lp-4kmrR6k5VJ6mkuCcl6aScEGZDQsC6u6PBicwrMBnYJRTbXzVxHZo6aeUAdFAk2tbKhG7Y9P9666c4jwH8AbbVtcKIZSMV_3EvF6uwC6K5HIaKLr27Zen8xdVcb7O8FJyKS8jKKFTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاش زنده بود آن‌وقت هیچ‌چیزی دیگری نمی‌خواستم!
🔹
«اگر رهبر زنده بود از او چه می‌خواستی؟» کمی  فکر می‌کند. شاید در دلش صدها آرزو داشته باشد که حتی رؤیای رسیدن به آن‌ها را حتی در سر نپروراند اما خیلی زود با لحنی مطمئن‌تر از قبل می‌گوید: «هیچ‌چیز نمی‌خواستم، فقط می‌گفتم خوشحالم که زنده‌ای!»
📎
حرف‌های ساده اما تکان دهنده این پاکبانان را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/446876" target="_blank">📅 01:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446875">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🎥
محمدرضا طاهری، مداح: رهبر شهید با مشت گره‌کرده آخرین پیامش را به جهان داد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/farsna/446875" target="_blank">📅 01:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446874">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
تداوم حملات رژیم صهیونیستی به غزه
🔹
منابع خبری از حملات توپخانه‌ای ارتش رژیم صهیونیستی به مناطقی در مرکز و جنوب غزه خبر می‌دهند.
🔹
منابع بیمارستانی تاکنون شهادت حداقل ۴ غیرنظامی را تأیید کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/446874" target="_blank">📅 01:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446873">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e10ca3a6d9.mp4?token=NbbkE1x9p7xgDPN9_pglT6t7BaAPw2TnC21pq4d1CDKf964YGAt8qoJmhcAF55wwDqF3_tKXE5APOppJWMNn0uZvESCJ28L-FDJm_JqwV1qj1COxdGdwUsg3kdpM_wln-d9BblE-m0MCJXgvzwoZLRQpe47dhykWemhNw4oFLRsti3HMDN0TONT0R4x7H5_kyRO_wiYbWexhKpuvPg47jzS7vUyHUjZY016UZZLQeGLcYHogbP0pza5sDGiFJjVbMMSmsFebzhu4HzEBEXajej8MsbYBaBr_yAeDjBvO2LVNgvQu6Pd8_TmxGkX0pVpsj_h6mOJaE49fWmH--KtEBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e10ca3a6d9.mp4?token=NbbkE1x9p7xgDPN9_pglT6t7BaAPw2TnC21pq4d1CDKf964YGAt8qoJmhcAF55wwDqF3_tKXE5APOppJWMNn0uZvESCJ28L-FDJm_JqwV1qj1COxdGdwUsg3kdpM_wln-d9BblE-m0MCJXgvzwoZLRQpe47dhykWemhNw4oFLRsti3HMDN0TONT0R4x7H5_kyRO_wiYbWexhKpuvPg47jzS7vUyHUjZY016UZZLQeGLcYHogbP0pza5sDGiFJjVbMMSmsFebzhu4HzEBEXajej8MsbYBaBr_yAeDjBvO2LVNgvQu6Pd8_TmxGkX0pVpsj_h6mOJaE49fWmH--KtEBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقت تشییع رسیده، وطن گریان است
◾️
لحظاتی از نوحه‌خوانی حاج محمود کریمی در مراسم وداع آقای شهید @Farsna</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/farsna/446873" target="_blank">📅 01:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446872">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🎥
رئیس سازمان مدیریت بحران: زائران برای هماهنگی اسکان با شمارهٔ ۱۸۱۱ تماس بگیرند.
🔹
زائرسراها آمادگی اسکان بیش از ۳ میلیون زائر را به‌صورت هم‌زمان دارند. @Farsna</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/farsna/446872" target="_blank">📅 01:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446871">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc081dd2ca.mp4?token=XrPsJ3eVi3PXfTzb9wWGlvgdX6ouF8QAUEe-gA17WPUls89ZzUPAb8FImI-cDHg5YG8ZypQXMl3jQFHV-_yAkejB1HcXAvCYuQY1WKrgCljb18KwM5BF__7VHLAqb7z_EwD0S-pBrsagXSr5DilaVpu0Bz9ledsaupfuiYcuH63y2Ni7fTXrs761T-450xak68t348liFI42eo2uJh6eIi6i37HDropE2BRBxkFEe-tLnQZQ4zRnfadq-g83M__l9TMVycMzX-cHQjBEPwa_vdUr59q4fxOwuwXLuueaYlzWEQvPhyNLfWAXyuIHbh5opWYu4qfmArELT7Cc-oUcwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc081dd2ca.mp4?token=XrPsJ3eVi3PXfTzb9wWGlvgdX6ouF8QAUEe-gA17WPUls89ZzUPAb8FImI-cDHg5YG8ZypQXMl3jQFHV-_yAkejB1HcXAvCYuQY1WKrgCljb18KwM5BF__7VHLAqb7z_EwD0S-pBrsagXSr5DilaVpu0Bz9ledsaupfuiYcuH63y2Ni7fTXrs761T-450xak68t348liFI42eo2uJh6eIi6i37HDropE2BRBxkFEe-tLnQZQ4zRnfadq-g83M__l9TMVycMzX-cHQjBEPwa_vdUr59q4fxOwuwXLuueaYlzWEQvPhyNLfWAXyuIHbh5opWYu4qfmArELT7Cc-oUcwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای بامدادی متروی تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/farsna/446871" target="_blank">📅 01:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446870">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d344f6e1a1.mp4?token=MueY0me42SwUH01-QbBU64Gnb3ENwYrxdB6dNqx0ZxRpcfa7wt7lYdiJoW9Kq-a3fq1CfLmZAvqQkcxdOkMT43QyGOMw_ckUxXd8pYyuGg4WH5Tu2GE7rMKqIR3K7CGWSzESO6bh65luHVYuitZm7NnFVORwo-kLdx_H9FXwFVUfJuf37GBEet3xzqNu5rWYEwkdmLjO2TjWGKIQLBdJC5MpRle1-2bAfipLVvJR2mPpYRtOcnvb8JwVoaoPhZYmVU6RHjjfbUwVc6z8jJkx6T1Aa7kynRDiEVlC9h1n_a3g5g-WACfEFidsGr-d4JzZp33VLpUslTy_bi3-O9tAUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d344f6e1a1.mp4?token=MueY0me42SwUH01-QbBU64Gnb3ENwYrxdB6dNqx0ZxRpcfa7wt7lYdiJoW9Kq-a3fq1CfLmZAvqQkcxdOkMT43QyGOMw_ckUxXd8pYyuGg4WH5Tu2GE7rMKqIR3K7CGWSzESO6bh65luHVYuitZm7NnFVORwo-kLdx_H9FXwFVUfJuf37GBEet3xzqNu5rWYEwkdmLjO2TjWGKIQLBdJC5MpRle1-2bAfipLVvJR2mPpYRtOcnvb8JwVoaoPhZYmVU6RHjjfbUwVc6z8jJkx6T1Aa7kynRDiEVlC9h1n_a3g5g-WACfEFidsGr-d4JzZp33VLpUslTy_bi3-O9tAUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چه شب‌های دلگیری است...
◾️
حرف دل مردم عزادار با رهبر شهید انقلاب، از زبان محمود کریمی در مصلای تهران  @Farsna</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/farsna/446870" target="_blank">📅 01:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446869">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🎥
ورود پیکر مطهر شهید زهرا محمدی گلپایگانی، نوۀ ۱۴ ماههٔ رهبر شهید انقلاب به مصلی تهران  @Farsna</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/farsna/446869" target="_blank">📅 01:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446868">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1230b5d8c3.mp4?token=DiV7LfI4Zm7CnQl1YgnYSEW7Csitg1AIJzVyWCVh9aLsZPxvgJFDme9NIGZ4r3z7t5eJkld24-AyIZbjeuRXLnJahm4j8fG3NXlsQ6KeuTa_BAZKhafaVlPWj32uL2DIR2yUC5fnqicOjYKI4tiQWMIvICBDeBlJs5BItKC5abBXPSBG4EVMf37ALrkB8DpikoPFf1JMKhdpsKZXpwYjZ7t1tbuKgc4ADWVoal_UdqbYmhS-RBpTO_TjFC2ppumHPyhX9nsLb3VqjCt22Nh5NsYUnv1mQD0DAN86rVzVSAaj-xtoOYTuJBV_kf_w5_J_hUGhvNhIQ261GNsoSy1ytQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1230b5d8c3.mp4?token=DiV7LfI4Zm7CnQl1YgnYSEW7Csitg1AIJzVyWCVh9aLsZPxvgJFDme9NIGZ4r3z7t5eJkld24-AyIZbjeuRXLnJahm4j8fG3NXlsQ6KeuTa_BAZKhafaVlPWj32uL2DIR2yUC5fnqicOjYKI4tiQWMIvICBDeBlJs5BItKC5abBXPSBG4EVMf37ALrkB8DpikoPFf1JMKhdpsKZXpwYjZ7t1tbuKgc4ADWVoal_UdqbYmhS-RBpTO_TjFC2ppumHPyhX9nsLb3VqjCt22Nh5NsYUnv1mQD0DAN86rVzVSAaj-xtoOYTuJBV_kf_w5_J_hUGhvNhIQ261GNsoSy1ytQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چه شب‌های دلگیری است...
◾️
حرف دل مردم عزادار با رهبر شهید انقلاب، از زبان محمود کریمی در مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farsna/446868" target="_blank">📅 01:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446867">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d3ac92c4d.mp4?token=tjy0iEWKR0-ClvbAzKgVX57y8EbBvXpkZUW-3tQDK-nD9BtuZytOB356LKsFh156erBVGKBh6uVPzFHs0vFvyjTZbUakuTVaB68RI-6cpFY-wo3mP9066AmnL6LjTG0s7V-aGj6VNyUUbGotBoVdN3E1tN-Hl6EcocjLyAxrOAcFEOYu8hJ5mOp8OAbZcHpqcrHdYnFQiquOsEZ2z0oEHuHsm9YMtGKxBcZj0N2K-fy2iEYh4SWI59y_wX4bL7stHt3FIpUxvnlgpXdXGCd-ir2i2tlY-bM1I7YqGq_8m7YSFM6jpCcZXmsKkoTEsyHjngLjHmOT2Fd8A-gosK4QGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d3ac92c4d.mp4?token=tjy0iEWKR0-ClvbAzKgVX57y8EbBvXpkZUW-3tQDK-nD9BtuZytOB356LKsFh156erBVGKBh6uVPzFHs0vFvyjTZbUakuTVaB68RI-6cpFY-wo3mP9066AmnL6LjTG0s7V-aGj6VNyUUbGotBoVdN3E1tN-Hl6EcocjLyAxrOAcFEOYu8hJ5mOp8OAbZcHpqcrHdYnFQiquOsEZ2z0oEHuHsm9YMtGKxBcZj0N2K-fy2iEYh4SWI59y_wX4bL7stHt3FIpUxvnlgpXdXGCd-ir2i2tlY-bM1I7YqGq_8m7YSFM6jpCcZXmsKkoTEsyHjngLjHmOT2Fd8A-gosK4QGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعرخوانی افشین علاء (شاعر) برای رهبر شهید انقلاب در مصلی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/farsna/446867" target="_blank">📅 01:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446866">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b287a0e2e.mp4?token=jObEa2vzYi0UYRf7IrgLswMSXfuP2Irx2gE2UElAjb2YsQ3NN6uWt6Sq5IiUGQHYED_zHz50_IpcwmihjZn05Xn_cEeCwVq5fkDMh7DGLCpz6ORToKhUVkSqVU6XQ-884FQNNGJB53nu9kJzjGKwNHx3lwaZwmo5QEa52YPsWrbPxAg4axKwbKBUJ1dCx4mqRFBfREpUzmZ6uLgSn6VGG3K_rTSDKDxItpYFTFIKJvhT00rD1UvQGIAXQiEwxY2t01avnGoVrYkTFWhzrdfEjKyZVgH6sCws6rIMvw6t3QeXvjm-dhm8IMpH-ri8hJwJFPva8r_TAonAo8eT7Cpr8heiPQI7fisudVc4AelSP3n3uuqbANfnpDtXPKGD966lr0WmTjtkZH_R67_StpXDtjKo1SylPBsF87q0_3FOlmZzjw-pAgMBAwJZkmtBS-vo6NkoEZ6KdzQIc_Tfb_Cbb3-2bs46B958GyInlL55e7NJABreeEJ6ml-FS14aF-klbX7q8wqMxkbRohhFXC0sZ0aabita-gn4Qq9yKERLGbj8SM4DS_6og7X9aBSFO8qfuuK2iOC1OSZsIxWK_lhJ-EzCzDMyfGiOeMbldnJoRivjwDiTy4bKTsOntrtwv_qsaa8asBM93w1VSsj1DMV3ulP_18FJ-zZ73-50-Cs-vQ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b287a0e2e.mp4?token=jObEa2vzYi0UYRf7IrgLswMSXfuP2Irx2gE2UElAjb2YsQ3NN6uWt6Sq5IiUGQHYED_zHz50_IpcwmihjZn05Xn_cEeCwVq5fkDMh7DGLCpz6ORToKhUVkSqVU6XQ-884FQNNGJB53nu9kJzjGKwNHx3lwaZwmo5QEa52YPsWrbPxAg4axKwbKBUJ1dCx4mqRFBfREpUzmZ6uLgSn6VGG3K_rTSDKDxItpYFTFIKJvhT00rD1UvQGIAXQiEwxY2t01avnGoVrYkTFWhzrdfEjKyZVgH6sCws6rIMvw6t3QeXvjm-dhm8IMpH-ri8hJwJFPva8r_TAonAo8eT7Cpr8heiPQI7fisudVc4AelSP3n3uuqbANfnpDtXPKGD966lr0WmTjtkZH_R67_StpXDtjKo1SylPBsF87q0_3FOlmZzjw-pAgMBAwJZkmtBS-vo6NkoEZ6KdzQIc_Tfb_Cbb3-2bs46B958GyInlL55e7NJABreeEJ6ml-FS14aF-klbX7q8wqMxkbRohhFXC0sZ0aabita-gn4Qq9yKERLGbj8SM4DS_6og7X9aBSFO8qfuuK2iOC1OSZsIxWK_lhJ-EzCzDMyfGiOeMbldnJoRivjwDiTy4bKTsOntrtwv_qsaa8asBM93w1VSsj1DMV3ulP_18FJ-zZ73-50-Cs-vQ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آقای مظلوم خداحافظ...
🔸
مداحی حماسی امشب حسین طاهری در وداع با رهبر شهید در مصلی
@Farsns</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/446866" target="_blank">📅 01:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446865">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6490810c42.mp4?token=GC8_pQ1RO-WQUVB68PiA5sA3snnrrfOLnRtHhCW3bCPaSGOynccgxqdHGwUZ0UKpPHGOEwXm0A-E8AlderrGxc0Zi19iZ5zzxqrCYcYE5ijvAyqfZFX7T7PfPCyzulpV5ILf864ss3VeGKiau1kq-LG1mAd0pzdpor3XaAHPRj3NHSAh0u1fKxcj_KsnN_JDANFfSRsx5KenLlixMHxfXUtuT2hkA1gXcPb0i3B4CftxrvM_qWFvFOplZtHShsw3Q3A7QP1ZKRKq-kZRYjixtkKk8KG7BxlQZpcMs9JJrgSp-XwRppj5rgT9NaiyXMcAS8LySupAz09Qd2pHbRjz6XqQrRn9lB3dtqMGInKyMzW-6xyp9nF2lXsDUS0d15VBileW0Npjc8FA9ctBpPGukIef8Mx9OPFD54miidigzE4Bs3g1TUZfxsqiW6KxbOoDF19kuKaZEITLNRtxiFIpf7SeyFUETY700MZe9KqK8TXNvDRtsKwh5aII5iKAHfEya62tkSQyH2ADiVB2T5MtCm3u7OtIrbrVFHpDOV895rLXRTFMPzCH3GFSbFiPRYAavQv1FYhFe5Ok3HsX9Dvv8eqIDt8oIq3d5LuUkX-RaOPFvXXeViSyyHLPCWV8XxBYrD3JazJ-r2TWQz1SfnrwyVe_O3HdAqrjOCC68-YG3QY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6490810c42.mp4?token=GC8_pQ1RO-WQUVB68PiA5sA3snnrrfOLnRtHhCW3bCPaSGOynccgxqdHGwUZ0UKpPHGOEwXm0A-E8AlderrGxc0Zi19iZ5zzxqrCYcYE5ijvAyqfZFX7T7PfPCyzulpV5ILf864ss3VeGKiau1kq-LG1mAd0pzdpor3XaAHPRj3NHSAh0u1fKxcj_KsnN_JDANFfSRsx5KenLlixMHxfXUtuT2hkA1gXcPb0i3B4CftxrvM_qWFvFOplZtHShsw3Q3A7QP1ZKRKq-kZRYjixtkKk8KG7BxlQZpcMs9JJrgSp-XwRppj5rgT9NaiyXMcAS8LySupAz09Qd2pHbRjz6XqQrRn9lB3dtqMGInKyMzW-6xyp9nF2lXsDUS0d15VBileW0Npjc8FA9ctBpPGukIef8Mx9OPFD54miidigzE4Bs3g1TUZfxsqiW6KxbOoDF19kuKaZEITLNRtxiFIpf7SeyFUETY700MZe9KqK8TXNvDRtsKwh5aII5iKAHfEya62tkSQyH2ADiVB2T5MtCm3u7OtIrbrVFHpDOV895rLXRTFMPzCH3GFSbFiPRYAavQv1FYhFe5Ok3HsX9Dvv8eqIDt8oIq3d5LuUkX-RaOPFvXXeViSyyHLPCWV8XxBYrD3JazJ-r2TWQz1SfnrwyVe_O3HdAqrjOCC68-YG3QY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زائر عراقی: حضور در تشییع رهبرمان کمترین ادای دین به فداکاری‌های اوست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/446865" target="_blank">📅 00:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446864">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04b969139a.mp4?token=lq2XSmt7Y3yKc_OHBn9J3WzsOfxRuU1ZXL34obxb-HoUYC7xw1nTyfg9p7ooiKLamZV03m189691EmZtUROulCfW1aZdsYa95Pq08abnSjVzLT67hMOF-Doa8p2RU3TNVmqxgS6CYxvT_jPwRvVVLo9a_Gg4hE30IIXk661N-pvI0e39yUC-Z_jvXNf9qyQFD2a6KOB-PnGzUa8tvBZfZs5jxCLuwpQzU1YzfR4LuSiJGqPDla5sr7_tQzIsSYD7T4BK0QDA19QiPpM2C7hX7yn3_mhmmBagxeCbsLT3tPwQ5RGYfivkxBv00j1AkZRDO3a6ujoZONEPRBmMUQWt91kB5UfZRD4JwZ09PzKyL1qimQG46oWTqN7wvtPUSmZwqovTSIZ9DbE3QfXtFFGZX7v4bgLoFWEBH7ajZFMMCTWS_ZKJ6OF03k9OoMztnjoda8pJ5b4eIHGIxz3JwLpyn_D2EEqKDxakMs_YVeLlv0T0kBbgDK9E1ZqMcOc8ShePo5W6O20KBIntjo8WuELdJeFJ9xb8fi5r6D_I-nX5VyM4cpakdd01YUQ76gB1d5713ElxFzGj3rqqKIKZX_uYhjlqXoVWVoo8Q7hQ-RkyVlrfQIqa28-flwvnqKJwB3CBmEabuY6MY6mqt4ZwOK_cIfURVeAJf8sL0FqdhhwNDgk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04b969139a.mp4?token=lq2XSmt7Y3yKc_OHBn9J3WzsOfxRuU1ZXL34obxb-HoUYC7xw1nTyfg9p7ooiKLamZV03m189691EmZtUROulCfW1aZdsYa95Pq08abnSjVzLT67hMOF-Doa8p2RU3TNVmqxgS6CYxvT_jPwRvVVLo9a_Gg4hE30IIXk661N-pvI0e39yUC-Z_jvXNf9qyQFD2a6KOB-PnGzUa8tvBZfZs5jxCLuwpQzU1YzfR4LuSiJGqPDla5sr7_tQzIsSYD7T4BK0QDA19QiPpM2C7hX7yn3_mhmmBagxeCbsLT3tPwQ5RGYfivkxBv00j1AkZRDO3a6ujoZONEPRBmMUQWt91kB5UfZRD4JwZ09PzKyL1qimQG46oWTqN7wvtPUSmZwqovTSIZ9DbE3QfXtFFGZX7v4bgLoFWEBH7ajZFMMCTWS_ZKJ6OF03k9OoMztnjoda8pJ5b4eIHGIxz3JwLpyn_D2EEqKDxakMs_YVeLlv0T0kBbgDK9E1ZqMcOc8ShePo5W6O20KBIntjo8WuELdJeFJ9xb8fi5r6D_I-nX5VyM4cpakdd01YUQ76gB1d5713ElxFzGj3rqqKIKZX_uYhjlqXoVWVoo8Q7hQ-RkyVlrfQIqa28-flwvnqKJwB3CBmEabuY6MY6mqt4ZwOK_cIfURVeAJf8sL0FqdhhwNDgk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
ما اومدیم دیدن تو، این آخری‌شه
🔸
عمود خیمۀ حرم، حلال‌مون کن...
🔹
ای غیور ما، سیدعلیِ صبور ما، خدانگهدار
🎥
لحظاتی از وداع مردم با پیکر امام شهید انقلاب در جوار حسینیۀ امام خمینی(ره) @Farsna</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farsna/446864" target="_blank">📅 00:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446863">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🎥
اوکراین مدعی انهدام یک جنگندۀ میگ۲۹ روسیه در جزیرۀ کریمه شد
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/farsna/446863" target="_blank">📅 00:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446862">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BonKzkrvlH_RMxb1ctTj1fZ3lzgihaZT4UbyhMr3J4gjK8Q6VLjHIeZLRnatI07qS7CX5EM5mNsAlpU2Qb9lUIeSnFRMIiP35-a9otZmQeYYM2fmGAIU6P6ELXwiKTgWljPx-yLAy3FNoobQAUCoPYnZ5bqjzpsEdnuBCvJ7uj_nIdb3JzeYRu3xPct3axj4m5r-AtvNWudajP83m0WMpIPjgzixREQFgP-1_wT9-wFDplYvsnhUk6yNin2lw8G64wiJQ8TT-nY2sOXcJqry0PQ9KNH0qNWiSmnMq2U-Z5jjK0iPDHP6YZA2kG4rSF9f-74YrHbRDq9JY2jcMFJnYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی جملۀ رهبر شهید مسیر زندگی یک شاعر را تغییر داد
🔹
۲۲ سال بیشتر نداشت؛ نوبتش که رسید با همان شورِ جوانی غزلی خواند. رهبر انقلاب با مهربانی گوش سپردند چند بار "آفرین" گفتند و حتّی یکی از قافیه‌ها را حدس زدند و بعد فرمودند: «ان‌شاءالله پیش برید با همین شتاب، شاعر خیلی خوبی خواهید شد و ...».
📎
اما سرنوشت این شاعر جوان بعد از تحسین رهبر شهید چگونه شد؟
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/446862" target="_blank">📅 00:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446861">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/defa80062d.mp4?token=RGMiiYJbPohTWl2pxlmepER1xaR8JxlbeEwoFodTzXREKfBMcM0gpvX9-FcztJfeqgMU_KZ9QHQXsZdJUpj7rD4BS76lh_GgW6VfLG3OZl57aEozgUKcxNUwr7Q4SyCxNdEk01BNCkAUc3OrNZxGmNvbKiJ_UsFIeqlCefN22UZLjtrSDu2ZNrDGZjLjgkCrS3GKKiWG6kRy1uIFtM1TR9IDx1gyjoG3yPMRNEFm1MrCunZBfVwsiOqqOsTChVv3hruFxo5pRX0zx5BZLGe2dCvZY19sPhGyTfC__HBvjSbvpxU5LH9HqGH6wuq34nA2wYOk56AAnuo7OsxZxXjEOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/defa80062d.mp4?token=RGMiiYJbPohTWl2pxlmepER1xaR8JxlbeEwoFodTzXREKfBMcM0gpvX9-FcztJfeqgMU_KZ9QHQXsZdJUpj7rD4BS76lh_GgW6VfLG3OZl57aEozgUKcxNUwr7Q4SyCxNdEk01BNCkAUc3OrNZxGmNvbKiJ_UsFIeqlCefN22UZLjtrSDu2ZNrDGZjLjgkCrS3GKKiWG6kRy1uIFtM1TR9IDx1gyjoG3yPMRNEFm1MrCunZBfVwsiOqqOsTChVv3hruFxo5pRX0zx5BZLGe2dCvZY19sPhGyTfC__HBvjSbvpxU5LH9HqGH6wuq34nA2wYOk56AAnuo7OsxZxXjEOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری شبانۀ مردم در مصلای تهران
🔹
با وجود فرارسیدن شب و تاریکی هوا، گروه‌های تازه‌ای از مردم، به‌ویژه خانواده‌ها، خود را به محل مراسم رساندند تا فرصت حضور در کنار پیکر رهبر شهید ایران را از دست ندهند.
🔹
بسیاری از حاضران می‌گفتند که ترجیح داده‌اند شب را در مصلی بمانند تا در ساعات اولیۀ بامداد و مراسم اقامۀ نماز بر پیکر رهبر شهید نیز حضور داشته باشند.
🔗
گزارش فارس از حال‌وهوای وداع شبانۀ مردم با آقای شهید ایران را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farsna/446861" target="_blank">📅 00:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446857">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PN3K3-HDTikud-w9iFjY2XxAQ5rwc3Ytisv4jM9zh3Hn7fMAWjbBAUQEdMsZ2mj5TqXDMylnUNzDSGkWsO_c3xxIBLIWKZd3uBKch6uWDDrQRtzlCjJZnuJFrdKWmnMLY5j3TzOvVpXo8QAwK087SC94yKEbiWj53xM4OaL34ULR3MIRfP3qvfcb7nG3stjuSTme8bcYByR7viooekW3k0pWAAZdEHNhtgDpHAZ0kdf_s-oAXPLOWIBCBT_tMJ_uldUJ7fycvD20hlIGrMIWWqBrKNtRurmUid_RbfjKPNz51V1GkGzBj7XJJUispwBlTSI2fN8DTs2gI1UOnrDyJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P9Hll_QLKLSL5LoWoxq5Ba20qpN4pliLzoA7rIzLCo8RDM-4EQXX77inB7sDmxuLp-vSJtjDUa1g6GUP_TWyzzqo63jZt7f1l2S80VlsJoWD-W_swfuKqf2H68PyRaEeKFdkNWaE0LC-ghDeAQmyIbhr9rkwkMKLBoFyzjL5ZgLEHap59vw8uyNsroXOGr40HZvrzNkKdeUncg5rCd7MClLBMj9gvUa4iYeGj9FZeu9LOOIYbFVuTQplt2QB4EQDER7oRH0vowRhhYtYih8YKY5w2f38jcewgg451OVsuo09s-ec3iSRSj58_aB9Eql6ou8sXZxqYYKVzx4-KIgU6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qeoLaszvzXNPXsEPxKLxmJr6Sj3cgkCIumpuFlIBRekRQU-Amcw5bVexf6nwAlotzphOZ8LghvcpWDQa1f84ET-2uIe2J3zMce_BNjEl5pJu7fIGHcyjd-IPVg3m0mczJlWEac1OzTRBilxCTk-px3RUKnPCYbyCkBWa9_P2eLpWIuRQgn2cTPmqyXFqlpLjeWGECe7fczxeCOOP-pydSQ7Wy8iapX5ALUPDb5L6GsULXKrE53i3SDrXAIMDX_dP4gqPw-pEVsiu9YJkVTpiMjcxPfnla2zI__JW3oZ1S-HFkNmkPuAoXeqgEL6HDgNmCtJaFwadfor3oFsmA-hyfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZfcywWOKXZzMqaqfAdPxvkiCPlHgHc5YTmiBn9ig5cOSRz_ZNi09qOYlyFH9zIpeHflQbb7AQTDgeQxf1qThcHVP5RxqxTpYYMZqJsnI6BHJlhQhLGHZfe3LrEqGCmii527YjUYmMZxIbbw-SBja5Axp36cZW1EYO-5CIhi_GLI9aAT0pxvFtD6L-BFFfEZ0F2zVvVuFLGF7_BUDJPKAd6qImk42-7rTtMHdxoCXSKboqt2NZhocVOoTVlKA3pxjh0PgiqJEzY4MGufrtUfJWU3u4gd2R9XNNe31CkthgbZDpGONTM_SWQjPnPbyK5uD9BD3Jjxwl-y4oPOFpyg61g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | یکشنبه ۱۴ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/farsna/446857" target="_blank">📅 00:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446847">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wkrx450RsqVLXUXGHZvHqn6RTwkfdZS5TKfPcUGAOLkjYtyDJM_oa1p4H-L9RUmWsIUh6pnN0iVwz9Lic8gh8f1sn6osXuOPjaxulqrh5m-LBMgqijr5hEISnLLTuoCqv9FK7rhSg_9E27eHaJr3Ho6L4EtpkJRM4egVUSW93sntMwuQRP97gI0nmO-VVbsn3Ajp-KrKLOLgFBs0LZreWWWfbwKDVYbgo1XCspfX93GdgZSeoW4ksnGN8Fcvfoe1MDgHo1pEanSG759AgRQYvzbIretGJTptjJRWwvSpxDLLQ4kIShKir2vpEFiyb2epAlwwieutIIB4T4leJrfN7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H8jPm8zdrLWMsROb5Y7nmZZXkpueFVLHMXWsUxGcRA3z3xdTJvsyqkUZkBSIT-afKNOEQupa8cNb9EXpMCGdeZDZ9pHeguaL7ZIecV2YMAgg_isbxJKEgYZqmfowpDZ0QowJRbJ_ROwwTD0hgqJrtno1yTIqOk_gS_EU4ytxLoWRYu20BfnwpTsef74CnBXVkvOwTLrfVKmauFn5pXgtrbV7vBQXXakp7AO4b59gjoI9P4kjPLU1KTIMduNVDHyk1OxVA4Kr-beHgRJ0oBV0dRH5Kq_K8BH1nljFJVRlteU8G7ERHsikpCWFgDfZLpgnojyKsXImeqFSELYKHINZaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u3fIkhwrz8GWPZcPO89lTn3HWWacOW5LAyNdVP3GJhDxpGWKJRJ3NKU5CwIng2LZeBLRol1y5urTbL9KMhGMRvNC7cl4xwEslnFe30hhHuiThFevnf9qXd6oceEIzr6xdSEmzRwTSN_DhzlMYTCDeRX7TlOY-iGPxGOAV9YWiCq0LAU1ZeayxZanls4eepuzJxAd5MMVLEuFSOO-v5PB3cL8QFxEJldZzj1FkuMtx0xGoRv8Jp-qdpJaDWJhocvSQeYk6oS3m8X3HOI24JUN9DczlhP09hMePnhZkQ_htTuVfvA0eGQANlaCB2-4Koo89Xe8jONwPjKL9tgXRHiFPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cnk5_lY9l1JAQ-xRDDWfuHxJJoLOy9wCZK3BabZJic7kbiRqSa6gUF5waGJSAzkrbAMqPh1AtBU1EUY8isD50JWdEwuNKWFNV90WFBz5zSOQ0e2Uwwe2CucLt_Enzp-XQINAwgXiYTpIMUVk8fT0wztwncKdsFAfIWw9D70n2WhUmGS5KPYdygolLPVxa9cqt9WTNl6wN4KB32CAlepNpdCv-li_cUvIMqxy_iFuBnlGxAWgG6jqkGGOWH_wd5un7WjS_ZtNaVcqYFA_TJOcIGY7PQ_T0QT_JnGid1YX8yR3aKlzfBbf7_UmHCGoNH6RcprQxD_rTyksKwVSwj7QhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HUEaL23_5JMoN0y3Rt1vbVnnmT8fff-lRkybOkUebod6jpi4l1inWSKNmLHBB06qmtTDXKBzCK2Ozx2951-U11BPemQG2GDSkToOFTsspU9zu0V9MPOxpicFfY8-iExMnWEKzfn9DjKyqf7Y8TC8dLE8xawdAmFI45irRjOnk_kU0Jsob2_mMrdZcK4BnBCECNtFJLgcUmNCxO1jPdZCWFfp1nW6G6wdSrvfsVZEwDzk09FQaEzEHgUtcPXNm2m5dzMrOqnza56ycpi0_1HHc2IOpjEcD6AqeY34OwsYw1xDkhHdN56PSV2zdNMkHPCNq4OPedaezWmuCnbnmxXlOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CctRLzvdY99KEQX79SbjfV0guP_h5J8EgZvzDUTJWiteF0RBWhvbjXJXI5jicGhObJ5IGAYffChhUa6xmXWb-si-3So7AuiMHUJRiH2XAOhxYdCoBQ_73ceUPUgvGG4vkjs_n2NjGTxy3oGEYRKl-yYtPwCGOt-XuwST7tPtPY1a0hHMZFyIa94MiEIf51DAXL6bX-YhLTLY1ja-c2h5ZDmtVyjTUnOlN4RTpOTFAPa9G95mp2s4BLJCqcUPNJEcQOtLKrCtSM1ddi9rE5o7w95faD307OIcNGT2Q_oQOV9N8h4YOv6oz04aYQaFqVMgQzjQH2knlnaowG3NVKKN5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZaAknzsunDvudSzzhT7JaCbG8yeAIXvhCEzcuHf5a_K4Sb_mQ2Dy_YVHnmux3AHSd8iRjKn3WDiR1PGIYG1CoVy6P1yvV6jkSkqzTBp7ILAPeMXB8tkas2FdrufSuvnh8cNafg-AHqvvvz9cnOfN2MzQJPYHwGkcHkSrEGzzfLr35VHAmDvDSi78wJUdgudJnANZ0JGtMocFfOI-sytExSRWAdHI6pXxLqpSkWURKv_x1gjoXm1FnG3DgMi4dOp41Qiw6QuIUA3NofYMgC4ZDZi0U64R32EkBVbPy_uec05lTSZW29i7_h7iOglME7cxofnj4U0YidSxXKBduW0QAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g_H5zt_nM2G0Ss7JDwCEzZeyJfvLZ-NyVh90UyOx7Fg__hGRiPf0QPMjHjr8WhPDZEszZFl78hEoHqJsxwi1k7p7pbuIGVlByXbjGIIxXHrvlMce9Evw8dhbb2d98Ttk6T101-VREvAfYCGUwSZ5QFyh1SsUCWxBmBj7lipxApBJXQrbQBqGC-McK-vBQm4SyS2kzAquZBGqNOGda87vKyiwLdWuJpNvtAJllh24u3a0nHhSZxI1fCBZy-6HAGmKG3_Vj72VRyWjup8gyP1TwDFYrbXDoebVauFx3WgBCSl0lSDLD0_1YgPTyTyVxMt9q_BCOQvZW4maXleFcsOaJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CY20VSfVwRsMDIYykRmMjBqyPzMgM_Hh5DDw5i9vNQyxeBvRBr6gAlAEgkCH9BNxsi0AXQ23R1wnYciAfQS00vePStpUrnqObYFTMfr6FhiX1OyDV_cd37lLxpdFaxywiC9X6C24S4BVmf3cKrT-x8QE6hbDpLMjerFPTHX_O_TW6UTwcHNWnO7vRTX0Idi7iLBoNwJj3p3oK5C_qAmfYpyU2MrDb96mayxG_Dw1Zxb-CrGpS2a6M95jnJ1fJVSE0xsNZcJW_-0GOlLbSya0xawApT4kn3bHSvKv36FMiZPkCa8NZpYJn5fy58LWx3sHKsLSFjAV2bUqiR5IxJnH0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rdNGkWOzjDWlqg9M0r7A9Ucpd62EORA-IJaWu3Eqe43mO2vq5boToFV2c4yVywVQS81T-uH5nN36kMgC1-eMN9tpCEbRHOL_TZnMBTuRPX0ov8W2nbgCb5KRk3pjP7AqcBoBVeyrqq2rAQtGLnBJu26_fOHa-Ada99ie3GWfbgiGS5gOEq8w_KBRH0HoQ8f0AzZdVFWFmO36urEZQuU_dqs8h53p-nPIrDqFrXAtjD9LWV6ZstDdydGquTOwsM_fq0KGJGV5zO0EGCf3840aHaaFRsQoHoTgNnFWT-Qg4Wk4bxTUueryUMuvSVVHNiFxhT_wEqPHayl0bIVeTUVuSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/farsna/446847" target="_blank">📅 00:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446846">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b394f0e431.mp4?token=L1S5fOU3crY9vVKzlXzVBLjt6XjUCtzrLmRJ_7zBChI7urwNE8UcD_YkemG4c_GQOpZtWVAGVDoMTLHz9uLxrQqorKCMs1KbPwQVMkfyDHVTGONsCl9VWLnF1AQqD0z4SVqRXTr1H8QXMrFKaCkhDYYkVh1xXati26zzK6uLSG2UrhYwtLFwv8ediMN9cLh82E2fUwvUKf_lywvVmx8ZAQg3Aee_nXCpqW4Ao_iw-eke3JW5OUgodgTF8OJXhbhuYzal886O2L6XtshF8RqOkkgIYM1ZFxn_INeCucLGgzngjbAD9VlwTpbEbjLPoeqqFP6NTmEloBY0CNnM7ZQWKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b394f0e431.mp4?token=L1S5fOU3crY9vVKzlXzVBLjt6XjUCtzrLmRJ_7zBChI7urwNE8UcD_YkemG4c_GQOpZtWVAGVDoMTLHz9uLxrQqorKCMs1KbPwQVMkfyDHVTGONsCl9VWLnF1AQqD0z4SVqRXTr1H8QXMrFKaCkhDYYkVh1xXati26zzK6uLSG2UrhYwtLFwv8ediMN9cLh82E2fUwvUKf_lywvVmx8ZAQg3Aee_nXCpqW4Ao_iw-eke3JW5OUgodgTF8OJXhbhuYzal886O2L6XtshF8RqOkkgIYM1ZFxn_INeCucLGgzngjbAD9VlwTpbEbjLPoeqqFP6NTmEloBY0CNnM7ZQWKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رفتنت هیچ‌وقت برامون عادی نمیشه؛ رهبر عزیزمون….
@Farsna</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/farsna/446846" target="_blank">📅 00:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446845">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a261b441a.mp4?token=dkYs3Q2RdWVmNBnDhGoSy8_t2F2W7dlr8FP_9IhaLoyt1VxvfCdx397yVWmh0dXKb-cTywLm73p8GHHkVwlUVqxQng9AWlvMbrfa5_jvrUFVNLr7J9HrrzlfmD04PStsNMqFgS7icmr029xogRZfTtdmGuW2_9eVvr6DdGcnbqgK0vrP6Syvn_GRIQGUoetG8PhogqPmMnMl8oHbyCsmQGhnr-O8Q5TM9cQdFJCnGusUx4R_a2mHz7QWN612sMyGWVyEnvkHZvSwOZ_nRG6ZjFG9V4x1WIFq_5iDEfFRKq5wgrOA73D_kI1zPe0qo3p72kG3m3umTZX5w42WRZooV1wYaLiQ2_BD9h5E9Dd7FJTSkxFRHOgyrjOFhLhkJVoMLuRR_tQnJ4MCwpEYPqBxLW-BJaR8LK7-drOYTrc1xh12Oqqucg6suxipjCBTGIw1nBrrjsuVn022kAYNsDugScZnkw2vDiIZRGxvzccPqJg-0GWQ8gXaVeik2G1CORNsQtKmGcO6fqFBqsFbQ6LQMFyQaEvDPdwcy2v-w_7NKHEx9atKE7cELNnC53hY3gw_CTTRwyE5PeZH0-SZbG28TlVTr6HLvVLBV2uc2SUC2x3sXgG14T5U0fUnV3oypLRb_vhuHWghYZnvS2-OJDUAW5xSGeOey_m41_Ddq3es7OM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a261b441a.mp4?token=dkYs3Q2RdWVmNBnDhGoSy8_t2F2W7dlr8FP_9IhaLoyt1VxvfCdx397yVWmh0dXKb-cTywLm73p8GHHkVwlUVqxQng9AWlvMbrfa5_jvrUFVNLr7J9HrrzlfmD04PStsNMqFgS7icmr029xogRZfTtdmGuW2_9eVvr6DdGcnbqgK0vrP6Syvn_GRIQGUoetG8PhogqPmMnMl8oHbyCsmQGhnr-O8Q5TM9cQdFJCnGusUx4R_a2mHz7QWN612sMyGWVyEnvkHZvSwOZ_nRG6ZjFG9V4x1WIFq_5iDEfFRKq5wgrOA73D_kI1zPe0qo3p72kG3m3umTZX5w42WRZooV1wYaLiQ2_BD9h5E9Dd7FJTSkxFRHOgyrjOFhLhkJVoMLuRR_tQnJ4MCwpEYPqBxLW-BJaR8LK7-drOYTrc1xh12Oqqucg6suxipjCBTGIw1nBrrjsuVn022kAYNsDugScZnkw2vDiIZRGxvzccPqJg-0GWQ8gXaVeik2G1CORNsQtKmGcO6fqFBqsFbQ6LQMFyQaEvDPdwcy2v-w_7NKHEx9atKE7cELNnC53hY3gw_CTTRwyE5PeZH0-SZbG28TlVTr6HLvVLBV2uc2SUC2x3sXgG14T5U0fUnV3oypLRb_vhuHWghYZnvS2-OJDUAW5xSGeOey_m41_Ddq3es7OM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خطاب محسن افشانی به ایرانی نماهای خارج از کشور: شرف داشته باشید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/446845" target="_blank">📅 00:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446844">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8ca0b1e88.mp4?token=TXngpQgJC4xo5-U3vt6avZGPNzMDD_BCOcVEob5KXToxhhOnAwTV4H5odGe0juEp5Y_FljCq_4RcpvFJGUWCeOKbPyH9y8xYaifj8a0HGcQMtotDS5j_RmHYIBzssN7HjyqDhY1qyt4X6_9XtPfLmoCcncMKrrUgkUY6ZV5NVHZtSqHiV7IMyi3C347QVqgoT11myqEFB9mG-Z4EcfjA5_Y1a1dba6ra-zRPDHCMY5Z_n4W5XyVBSYZiQ9rQpWjM8roQnjid0Lp5jCMF7wMBQ8dY9z-0pJIOZDqEuZ1MkV1-HYyTFyqyCiqfhAFn1VgNYtZEzH56jyd9u0MArsniXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8ca0b1e88.mp4?token=TXngpQgJC4xo5-U3vt6avZGPNzMDD_BCOcVEob5KXToxhhOnAwTV4H5odGe0juEp5Y_FljCq_4RcpvFJGUWCeOKbPyH9y8xYaifj8a0HGcQMtotDS5j_RmHYIBzssN7HjyqDhY1qyt4X6_9XtPfLmoCcncMKrrUgkUY6ZV5NVHZtSqHiV7IMyi3C347QVqgoT11myqEFB9mG-Z4EcfjA5_Y1a1dba6ra-zRPDHCMY5Z_n4W5XyVBSYZiQ9rQpWjM8roQnjid0Lp5jCMF7wMBQ8dY9z-0pJIOZDqEuZ1MkV1-HYyTFyqyCiqfhAFn1VgNYtZEzH56jyd9u0MArsniXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پنجره‌ای به حضور پرشور مردم در آیین وداع با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/farsna/446844" target="_blank">📅 00:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446843">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/724ad07581.mp4?token=WdAD_XBt7Vu_jn_t02yxgtyuy7gdZ08HFH5URJu9ZtZED0PSpFSIWmyQceL1Z7Lk_-NcloOv_-fNlGNXjUBrfcZUSGCpHj5ag-XhJ-_ocVzo9pYPg2sLawWsp2inpJSaa6wUR1dLL1KsnbBSMPI_rOFm5Squz_QrG4FEHcCh5-LJb9AsBIlw_iWoVZYGQLy9TY0tjWLe8q9wIE6yN45mAaYjCcLVTG2NT2dxDKNlO7YTpnLQKKCzZDYlq7ev2tveLlfpnoYU9LSnM_75yeWxaJuVhm_o15JI-C0CGYbSHCfAEC0eKsmgP6FuxIbVEFGgaILiz3qGRcENLzVNQulJuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/724ad07581.mp4?token=WdAD_XBt7Vu_jn_t02yxgtyuy7gdZ08HFH5URJu9ZtZED0PSpFSIWmyQceL1Z7Lk_-NcloOv_-fNlGNXjUBrfcZUSGCpHj5ag-XhJ-_ocVzo9pYPg2sLawWsp2inpJSaa6wUR1dLL1KsnbBSMPI_rOFm5Squz_QrG4FEHcCh5-LJb9AsBIlw_iWoVZYGQLy9TY0tjWLe8q9wIE6yN45mAaYjCcLVTG2NT2dxDKNlO7YTpnLQKKCzZDYlq7ev2tveLlfpnoYU9LSnM_75yeWxaJuVhm_o15JI-C0CGYbSHCfAEC0eKsmgP6FuxIbVEFGgaILiz3qGRcENLzVNQulJuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیشابور در سوگ آقای شهید ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farsna/446843" target="_blank">📅 00:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446842">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec580c6f6d.mp4?token=C3iNkgoUE-1lH83ZyBEkDL59nz0xThBRSV-qU_kHF3sioBBblHXmCrJIqo01RQ9jUSLZj278Yqi9CKS0_VgkBrB8eXMEhYdHTPVxJ7nDHFi1yEhuJ-egZeCjiLHCZYG5QdTvkOgthytiZuxEnndswEb9W1Sko_njGOABMK6wctaXYJL99Ju1w-LzV9quOTa2w77lB52MjKVFHXj3NCx2P4cUbaz-pZ-wsAcE5Z4MwIU4_Pf_OpBr-iIpFNXF-X3PvmSMWZWVI_bIcPvfU5AHeCnCh9C6SWF79b3GThveAWEnFv0CIPWDyenx0JFyKhRIucXFF6sONFZWf30i6OzS7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec580c6f6d.mp4?token=C3iNkgoUE-1lH83ZyBEkDL59nz0xThBRSV-qU_kHF3sioBBblHXmCrJIqo01RQ9jUSLZj278Yqi9CKS0_VgkBrB8eXMEhYdHTPVxJ7nDHFi1yEhuJ-egZeCjiLHCZYG5QdTvkOgthytiZuxEnndswEb9W1Sko_njGOABMK6wctaXYJL99Ju1w-LzV9quOTa2w77lB52MjKVFHXj3NCx2P4cUbaz-pZ-wsAcE5Z4MwIU4_Pf_OpBr-iIpFNXF-X3PvmSMWZWVI_bIcPvfU5AHeCnCh9C6SWF79b3GThveAWEnFv0CIPWDyenx0JFyKhRIucXFF6sONFZWf30i6OzS7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خداحافظ آقای شهید ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/446842" target="_blank">📅 00:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446841">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0zwEwHQD3rQoxfupugc4kXWv0RGgNBg08GT2QUPda4Rhz2nsbCc0ooiIqz37M8EzXwiSC69C8rmv03lVhjYZU1IXPgZr5md-zyFlItS92jVeMPYlsi-cDsLOjGQCJvLIRsiWlesbuLJ9ytLC3T1_JLtiOz_Nc2EnF-TzUScmA8WrLMmSAF-unl2CweXZHyx5nAB6XtisNlBPtjmR4Qw2hylyhN6ztg9CLKWaBciH7vW91ZHYOByJ63DNM8fI3fAs8vjYth9d3VFGDqxmgj_CxoyZMvzGMmbxutybDH-Jj9voKwE8tuPa4aw1V0zX_Gs9PERVqGy75REitQy2vTlqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از
احتیاج دیگران سودجویی نکنیم
🔹
مردی سراسیمه به محضر امام صادق(ع) آمد تا خوابی عجیب و ترسناک را که دیده بود تعریف کند. او گفت: «ای فرزند رسول خدا، دیشب خواب وحشتناکی دیده‌ام.
🔹
در خواب دیدم که شبحی چوبین (یا مردی از چوب) بر اسبی چوبین سوار است و شمشیر برهنه‌ای در دست دارد و آن را در هوا می‌چرخاند. من از دیدن این صحنه بسیار وحشت کردم. تعبیر این خواب چیست؟»
🔹
امام صادق(ع) کمی تامل کردند و سپس رو به مرد کردند و فرمودند: «تعبیر خواب تو این است که تو دنبال مال مردی هستی که به‌شدت گرفتار و نیازمند شده. می‌خواهی از احتیاج او سوءاستفاده کنی، مال و اموالش را به قیمت ناچیز از چنگش درآوری. از خدا بترس و دست از این کار بردار!»
🔹
مرد با شنیدن این سخن شگفت‌زده و شرمسار شد و حقیقت را اعتراف کرد. او گفت: «به خدا قسم راست فرمودی؛ تعبیرت کاملاً درست است. یکی از همسایگان من گرفتار شده و پول لازم بود.
🔹
او باغ خرمای خود را برای فروش گذاشته است و من می‌خواستم از این تنگدستی او استفاده کنم و آن باغ را بسیار ارزان‌تر از قیمت واقعی‌اش بخرم. اکنون که خدا راز مرا برملا کرد، توبه می‌کنم و هرگز چنین نخواهم کرد.»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/446841" target="_blank">📅 00:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446840">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یک استان دیگر عراق روز چهارشنبه را برای بدرقه و تشییع پیکر رهبر شهید ایران تعطیل کرد
🔹
استان مثنی عراق، نهمین استانی است که روز چهارشنبه را برای تسهیل مشارکت مردم این استان برای بدرقه و تشییع پیکر حضرت آیت‌الله العظمی سید علی خامنه‌ای، رهبر شهید ایران تعطیل اعلام کرد.
🔸
پیش از این استان‌های بغداد، نجف اشرف، کربلای معلی، بابل، ذی‌قار، بصره، میسان و واسط نیز روز چهارشنبه را تعطیل اعلام کرده بودند.
@Farsna</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/446840" target="_blank">📅 00:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446839">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eV_uC8vRlu6Um_Rda6T-gr2QYVbhAhRmtA4yhMKHrzm_nKs6f7qWaDdFTK0JOjbWQWfFkfu5IMkEJ1eWMudkuApsU00ayy4h1Rbvq3bt5JH829hHsNFuSzvU_Ka1q-CYzSfvvqgwKVodDvqNyOdNxu5HrLnhkkBC6lihBtJtJRHM2gfibefYCkuoMjljcFuRvpKEeWOyB-BpCdR4VP8CnnKwoQBjo4bNCBgMnl7H2AjaA26RtSIxlmkcqpedVwgz4L6njWyRC813C-wLsrHwtSQG1z0MZQgq3bDP8sLWQjdaF7BT1vaIR17-7LAJ23Qazmvoc0ChOruPUkTxmdxK_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفری برای آخرین خداحافظی
🔹
«از طرف من هم از آقاجانمان خداحافظی کن...» این جمله، آغاز سفری بود که از خانه‌ای در تبریز شروع شد؛ سفری که در آن هر کس، سلام، اشک یا حسرتی را به دست یک مسافر سپرد.
📎
روایت مسافری که با کوله‌باری از پیام‌های جاماندگان به تهران آمده را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/446839" target="_blank">📅 00:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446838">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MlORBdoXiGbvPJsFbgue323wC4W5S71in2LxZqMGT2rexPjJ_M769fIYP5oXFq1esf8_ayEZamcRsRbTeMP940HTW83Iu91QPIJbukgs7tEiNMze9P5yT60gbeyiH0OhledSl6uor2AgkJr6TtqRD7Vtja1r_X-ddt0_N0MMku25wIqpleZXRtzlY5w6PJcmevr2jZNjec9qyrULeJ4baEQYSLZqYmuuz-PUmsN9VQYZ5CVtmnRF45p8HXxIxXUSTEktrR79K8MJRL5_yl-UIGZ6tP7Sf4ClaunbuxzUGwahomR93jfSMJPLDsPEbEjZ2CZNgXBQC-oUteTSp2RmMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
| یکشنبه ۱۴ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/446838" target="_blank">📅 00:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446837">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d2d2c1542.mp4?token=fk5AAEDA8XEynNjnBLe2SO5HLkOagSTQmy_cnTfe264lK6Dcu8ebQu0_lPwCX1NaJbYgPVUwp-PR3PaerulN6SKHJaSXn_Ela59K0RA1JjKX70xGq3JsG0le7qRDI1C20SI5y3-oGDFbd-4M3MF_83c5BHa8IH_SIgxHmO-8GXqijt4FrJuxyqRfef1PxkQurw78ZS8a0n-VYI9S4ejJY0vYbv0BKkDHoCq_l7S3qExQX2u7h-7fvDb_vJbBAKGugf_OkMnl0jUSw9lacmreZJePbrSaELwGUwo5yQQmVo7kQrfwj4n7U8KjCHuaHoLBoKLrDah3bVtB6VkIfU3ffqBN2xkCws8g1X2JMJVygZPRUuwbVTV-TyjeI1ADufG1NzgvQPHWuqQq8okklLyAxiow8aGYxKid3UQ604p-7TK5EjVXksbdg5qwIob1wR6LToiiuagL1AA9lKNHayF21UfkYY9fgATW_2PEGvWWttlcjE5nV71WqQmaWg1f8f9S_aq4uJEpWFjfBXHRI4-k5iRpgHkOYpey9fQb2J_6u-vu-NjhJAJL_a8ZbmXFIjMTA3ZJStPHAft4o_7f8cackFxrxPec85m0mn24XH3VJckCmSTINeBqCyE9pYWHgHvqi8ASRgXmZVV9IN3OhduS8ekAc2IlekviGXQaMnBaqOo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d2d2c1542.mp4?token=fk5AAEDA8XEynNjnBLe2SO5HLkOagSTQmy_cnTfe264lK6Dcu8ebQu0_lPwCX1NaJbYgPVUwp-PR3PaerulN6SKHJaSXn_Ela59K0RA1JjKX70xGq3JsG0le7qRDI1C20SI5y3-oGDFbd-4M3MF_83c5BHa8IH_SIgxHmO-8GXqijt4FrJuxyqRfef1PxkQurw78ZS8a0n-VYI9S4ejJY0vYbv0BKkDHoCq_l7S3qExQX2u7h-7fvDb_vJbBAKGugf_OkMnl0jUSw9lacmreZJePbrSaELwGUwo5yQQmVo7kQrfwj4n7U8KjCHuaHoLBoKLrDah3bVtB6VkIfU3ffqBN2xkCws8g1X2JMJVygZPRUuwbVTV-TyjeI1ADufG1NzgvQPHWuqQq8okklLyAxiow8aGYxKid3UQ604p-7TK5EjVXksbdg5qwIob1wR6LToiiuagL1AA9lKNHayF21UfkYY9fgATW_2PEGvWWttlcjE5nV71WqQmaWg1f8f9S_aq4uJEpWFjfBXHRI4-k5iRpgHkOYpey9fQb2J_6u-vu-NjhJAJL_a8ZbmXFIjMTA3ZJStPHAft4o_7f8cackFxrxPec85m0mn24XH3VJckCmSTINeBqCyE9pYWHgHvqi8ASRgXmZVV9IN3OhduS8ekAc2IlekviGXQaMnBaqOo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایندۀ اهل‌سنت مردم کردستان: شرکت در مراسم تشییع، ادای دین به رهبر شهید است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/446837" target="_blank">📅 23:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446836">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd59919123.mp4?token=Xg8Mls9B7NTiiXR1R_9SNzgchbAUA2l73tjBFyo5QM2EkCks-46_fxtgRfJBlzK-YZnQslP2p2iv1L3tkEuRcTLSCqwtaGqXZ4S4qnWBl3JgzyapGcsai7yF9OEOHaZDbQ1MFnV6mBNjmP9MzH09fP8A-M6vSc4cnQavRWaMJtY8V4-nRnVQ-mgCtKrLUlTKvkyyAoWvw0JFwDQpLP9X5Un1aLUdBX-epFqTotju__uJeB2-UNXNfA9Z6HLlaJrC33tIZoUMkooVUyTWjs5fRppqGWc6i0KZ-vgtLXD3PTlSH5Dkq2Fd_LOionOU3uK5VHtEwYBiH_qih2m9OfcaZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd59919123.mp4?token=Xg8Mls9B7NTiiXR1R_9SNzgchbAUA2l73tjBFyo5QM2EkCks-46_fxtgRfJBlzK-YZnQslP2p2iv1L3tkEuRcTLSCqwtaGqXZ4S4qnWBl3JgzyapGcsai7yF9OEOHaZDbQ1MFnV6mBNjmP9MzH09fP8A-M6vSc4cnQavRWaMJtY8V4-nRnVQ-mgCtKrLUlTKvkyyAoWvw0JFwDQpLP9X5Un1aLUdBX-epFqTotju__uJeB2-UNXNfA9Z6HLlaJrC33tIZoUMkooVUyTWjs5fRppqGWc6i0KZ-vgtLXD3PTlSH5Dkq2Fd_LOionOU3uK5VHtEwYBiH_qih2m9OfcaZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین یکتا: این لحظات شب‌های قدر جمهوری اسلامی ایران است.
@Farsna</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farsna/446836" target="_blank">📅 23:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446835">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0530b61b0d.mp4?token=qmJ5EP2OZXWvPoSCvmnZTEPvOdV1h36kKr6Q2PvIyj-RfZNjEywU9zFypT2ekBi3w_XZ-ZSoEe1wzDr37UprivFu-i2Yc2Qs04njhC7QCBMQHGlQK6y4AEQnL9e62o1n4jOaQpXiQC0EjvO6z37_HdwiA9fCuF52P65_7IyMtTegAAOUg28p1BpXaPux4L22ckR5n_Mgc1CL2fzc6ufDeH3UbBJ5sOcjorDRA6eiiawgPCgpgSJ-f_B4e3MtAUvrUCL89ASZu59GAndXF5-FwlaJMyJYfna_GH2CC9RMYDQXMOwUsOyzJpR4FzoSBuuESj4grTCO6hLeLWZfWjOq-BF-320oPWNHG21oKQY09pjxjK5_3-u_CGNcTjhHFi12qFEzeV0l1FHFV8LQdFQc3UXsjAVCndsFsnCAD4a2ju10H21R-znFBYdR92oxJKFtC7fmCJDMXOj-SgxORv4uZUIJgDv7WfOTCxFIpxfXT9thQCbucOksxA8XoLbWr9c2goxtJ1TkHHAGzIkbmnV8wmPoHXg5K1m2Vj5ra94GXm7RfMg_iJ9ujAyMPyo30p6OI4BPuk0AtXoP1g15OxlMYSQiEAN5awuEKjQWuLyYD3_52vRIZ0N59kAQcmTatjeakkWfUhk_O3qhLWETVOt0RRfrnRnlsFadCQkAhXLXz9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0530b61b0d.mp4?token=qmJ5EP2OZXWvPoSCvmnZTEPvOdV1h36kKr6Q2PvIyj-RfZNjEywU9zFypT2ekBi3w_XZ-ZSoEe1wzDr37UprivFu-i2Yc2Qs04njhC7QCBMQHGlQK6y4AEQnL9e62o1n4jOaQpXiQC0EjvO6z37_HdwiA9fCuF52P65_7IyMtTegAAOUg28p1BpXaPux4L22ckR5n_Mgc1CL2fzc6ufDeH3UbBJ5sOcjorDRA6eiiawgPCgpgSJ-f_B4e3MtAUvrUCL89ASZu59GAndXF5-FwlaJMyJYfna_GH2CC9RMYDQXMOwUsOyzJpR4FzoSBuuESj4grTCO6hLeLWZfWjOq-BF-320oPWNHG21oKQY09pjxjK5_3-u_CGNcTjhHFi12qFEzeV0l1FHFV8LQdFQc3UXsjAVCndsFsnCAD4a2ju10H21R-znFBYdR92oxJKFtC7fmCJDMXOj-SgxORv4uZUIJgDv7WfOTCxFIpxfXT9thQCbucOksxA8XoLbWr9c2goxtJ1TkHHAGzIkbmnV8wmPoHXg5K1m2Vj5ra94GXm7RfMg_iJ9ujAyMPyo30p6OI4BPuk0AtXoP1g15OxlMYSQiEAN5awuEKjQWuLyYD3_52vRIZ0N59kAQcmTatjeakkWfUhk_O3qhLWETVOt0RRfrnRnlsFadCQkAhXLXz9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مادران و کودکان نیز برای وداع آمدند
🔹
مادران عزادار و زائر به همراه کودکان‌شان از شهرها، استان‌ها و کشورهای مختلف به مصلی آمدند و باوجود امکانات مناسب اما سختی، گرما و مسافت راه را تحمل کردند تا با رهبر شهید امت اسلامی وداع کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/446835" target="_blank">📅 23:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446834">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-CF9JCKM4Sr6gFTdDHkzsN43L-jGVsGxwk9d-z8IlYvwZoOnFxCn3PRCtYB2o792Bv21WIOL8xbkR_dm_tu1GB_EHnFg5J4kRGXHbYj_MiBjIzCTy99qfMghkN6y2K4M81Yc11CJX2FSzXU-1O61JCepgPzaRqWD8ADKtXWat2_bR5gzM5AH4TffIJduPiMdaRAsHgZkf2MaK0a-Jy3MjjpGkbnOUclYs6uTE5Kt9gZ0ZJncr3_mGZQpTokIH7bQLvyez4qCgOw61P2AXCdMc91jKlJjAKh1xtof9syP9NkawV_yIuXRl_OMfynIc7IAFQpWvnX0c0_WHFXytRDZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ای قلّۀ سرفراز ایران بدرود
@Farsna</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/446834" target="_blank">📅 23:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446833">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4225985517.mp4?token=JuDDdu4GwzvdISRbhSoQpms_eDeCzDrls8kRrvBQyQ0KqgrpvSjW7gqYOf6hJJOkTmR36cYl6OhQ7yuXk3UXDvzE9tDG44xCke0skEEob0MvDaT6yTvke__gQubp_w6eFqloLMLKxRVp8YTIGiBB2kmfwczIyOS_6RQ-wCSUBYs3KeF6anLo1iTDGXEbyh3Jcx1Nuxj-5WV2Eqqz4-V_hzTw2EpqjAipE6serQnNI8aXbMKwEzXTrTfOEby_B7B5kaJ6MF_7wQ2yxOMiUi04PRvR1Sv-RSyTZWlwe0rsrczz87l6ZwqwOVWdJMmSRYnEZQltDIYh6DSCNwvQaOV22w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4225985517.mp4?token=JuDDdu4GwzvdISRbhSoQpms_eDeCzDrls8kRrvBQyQ0KqgrpvSjW7gqYOf6hJJOkTmR36cYl6OhQ7yuXk3UXDvzE9tDG44xCke0skEEob0MvDaT6yTvke__gQubp_w6eFqloLMLKxRVp8YTIGiBB2kmfwczIyOS_6RQ-wCSUBYs3KeF6anLo1iTDGXEbyh3Jcx1Nuxj-5WV2Eqqz4-V_hzTw2EpqjAipE6serQnNI8aXbMKwEzXTrTfOEby_B7B5kaJ6MF_7wQ2yxOMiUi04PRvR1Sv-RSyTZWlwe0rsrczz87l6ZwqwOVWdJMmSRYnEZQltDIYh6DSCNwvQaOV22w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای ورود عجیب عباس موزون به بیت رهبری برای دیدار با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/446833" target="_blank">📅 23:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446832">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuZJ87-i0NgZsTwBokYJwKu3Yz6AP3u75GonEBpEemUN9Vl0tZ707fUPKT1NNsvxHFqjd6ZWZ1-CD0BKj8DFaiiuYu5TcLqwMqPmVdxPFwCAs9rCzWxXR9mCrUQV7gMtHH6HeMOq0H5T5pxueVhtL1jR-O1lXTzD89j77udCSp0dWfWYLc3xIrVcBNraC4stxNCFR9yhLcqo7tPR16AHrHR-jjP9ULB8Cc4A_TPenffgX_SIMGepZBc0KRSahPvnaMurhpTZDdPtnrJBUmUFog3ARHFFzGq2zIc6ZN4bfoYfe0-f6zViX9KRoKUIXBx4goUZMx2TEOU85hGfws-Mzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا دلش نیامد شاعران را حسرت به دل بگذارد!
🔹
می‌گویم اینجا چه‌کار می‌کنی؟ آمده‌ای برای پیکر آقا شعر بخوانی؟ دیگر نمی‌تواند بغض سنگینش را نگه دارد، می‌گوید: «بالاخره بعد از سال‌ها حسرت، امروز شعرخوانی، رزق و روزیِ من شد! انگار آقا نمی‌خواست شاعران را حسرت به دل بگذارد و از تهران برود! او نمی‌خواست آرزوبه‌دل بمانیم...».
📎
روایت شاعرانی که امروز مهمان آقا شدند را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/446832" target="_blank">📅 23:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446831">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fb608438c.mp4?token=uryUaBITTV2Ie7VQPUnQH8u2EHCr_M1AZUiXCZbctlQtjTtLeDcO27Imd-DVWeqlqCZtPmc31Jbac-GLsAf_fWkzQzl7dpoJwDDb2kv_1Z_MJ2Ed8nV22QJvDmkTw04ntX-cOpMaF40GKD_7toOb__gFFzGnFNe_I2CoiKao642y7FIUod8-Ask8NJ1HgVWtCsjXlK8fRyHJ-tEmRLYrYhZURsJ8NO61ahF0EeGZjqMhjsdI3mo_duPLq8o_5JD0sgBFDgpmViTqhjMCXatsZWWiguRLIn_Hq6zg5ASSSufkrkWsMpC5MtBZd4Pnj_UDN-bSsO9a3s-MkgG_sSZr5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fb608438c.mp4?token=uryUaBITTV2Ie7VQPUnQH8u2EHCr_M1AZUiXCZbctlQtjTtLeDcO27Imd-DVWeqlqCZtPmc31Jbac-GLsAf_fWkzQzl7dpoJwDDb2kv_1Z_MJ2Ed8nV22QJvDmkTw04ntX-cOpMaF40GKD_7toOb__gFFzGnFNe_I2CoiKao642y7FIUod8-Ask8NJ1HgVWtCsjXlK8fRyHJ-tEmRLYrYhZURsJ8NO61ahF0EeGZjqMhjsdI3mo_duPLq8o_5JD0sgBFDgpmViTqhjMCXatsZWWiguRLIn_Hq6zg5ASSSufkrkWsMpC5MtBZd4Pnj_UDN-bSsO9a3s-MkgG_sSZr5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله اعرافی: رهبر شهید، ایران را به یک نقطۀ اقتدار جدید رساندند و معادلات اقتدار ایران را تغییر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/446831" target="_blank">📅 23:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446830">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🎥
نیکزاد، نایب‌رئیس مجلس: راه رهبر شهید را تا تحقق عزت و اقتدار ایران ادامه می‌دهیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/446830" target="_blank">📅 23:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446829">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88b96217e2.mp4?token=ZUgoYb5qnLin13NC5XYDhpTFOnxv2jfisdx4uM4-ZtAF1D7E1dms7A6PPuQ76bfjv314HB6FoHXtK10tD835xPbfmRdC7kDhJsTJA7hgMZySHC5BmDrp1RV1amwd_N_k0ybJC4QteiS6JPsv8StTfbRjlpgep4ik8GtNVhA10zAd68ywAya3KAiJAJM8IPLO2xMkDuKeFTwQe0ni1ShB9XxoNaDOwu06WgirqDSMnnWndKMxFIuwB4jaRv8oo3oZln3go4OKi9wOkSumMpSoVXcU_LwkupObk1ny8Beb76fD7F-4lR35ITen4_lCkXAyOSwMbvtqhsVt3XNbHT30Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88b96217e2.mp4?token=ZUgoYb5qnLin13NC5XYDhpTFOnxv2jfisdx4uM4-ZtAF1D7E1dms7A6PPuQ76bfjv314HB6FoHXtK10tD835xPbfmRdC7kDhJsTJA7hgMZySHC5BmDrp1RV1amwd_N_k0ybJC4QteiS6JPsv8StTfbRjlpgep4ik8GtNVhA10zAd68ywAya3KAiJAJM8IPLO2xMkDuKeFTwQe0ni1ShB9XxoNaDOwu06WgirqDSMnnWndKMxFIuwB4jaRv8oo3oZln3go4OKi9wOkSumMpSoVXcU_LwkupObk1ny8Beb76fD7F-4lR35ITen4_lCkXAyOSwMbvtqhsVt3XNbHT30Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور شبانه مردم در مصلای تهران
@Farspolitics</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/446829" target="_blank">📅 23:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446828">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22e9711db.mp4?token=CHV1NwY47lIxrlAkBJIRoWfXo9q_nLoM4wEZ5-eef_eoWAdKGVZA-0AHwqTRHObYMUecyLA2nlQV6s7PY7N8UgkyHK5NCRtx_nOFhZyfQJc1e-hIYhys0Nuqppt4vL6s0smHE8XnAdGW1VxDC2jvQfjwj63IXdMiqmgCYVerAIaXwUeP-6q74x9OJ66MYoWftqFN5jLfGi_1xEABl-RmRHe0DDCWgXonAnV26tr8h4D7te2rZyip1NoKg8eg2rZ1Rhn0cRc4irYD6Lve6VfbMW99oICY274Nl0_VUOwI0lRXFsEx2av_Gv5_46t6_vMTiwHcPDytN5AjJP5nCfOomg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22e9711db.mp4?token=CHV1NwY47lIxrlAkBJIRoWfXo9q_nLoM4wEZ5-eef_eoWAdKGVZA-0AHwqTRHObYMUecyLA2nlQV6s7PY7N8UgkyHK5NCRtx_nOFhZyfQJc1e-hIYhys0Nuqppt4vL6s0smHE8XnAdGW1VxDC2jvQfjwj63IXdMiqmgCYVerAIaXwUeP-6q74x9OJ66MYoWftqFN5jLfGi_1xEABl-RmRHe0DDCWgXonAnV26tr8h4D7te2rZyip1NoKg8eg2rZ1Rhn0cRc4irYD6Lve6VfbMW99oICY274Nl0_VUOwI0lRXFsEx2av_Gv5_46t6_vMTiwHcPDytN5AjJP5nCfOomg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین یکتا: وسط جنگ جهانی در میانه بازی‌های جام جهانی، در ایران یک اتفاق تمدنی درحال رقم‌خوردن است.
@Farsna</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/446828" target="_blank">📅 23:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446827">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5f384d1a.mp4?token=dPUcuY-E0qzEjMyPtHK6iBDr-6q0GgxRRA0Kx5ZVEXLXuFIBkETzVIyafLZfeITxWjigZdLD5p-Bb1w7nMlUMwjdUUtSG36XQom2O5JY6Og2tHSOmPj-KY2uZ5FXm6XzdWUGPdp25HcejfcGEffgLrL5lTIOeCj_O8rj2H_6LTeJgjJHwXTwTiqBl35LjZqrLd1sRh_DoyuSroG8lQKsP2dW892XGcEcftycexb5zzOngyQ-ROloqjTG_-MhEWUCo4yWfGaecGDmpqvl5LwfjR4rzVX2OtvltefjwoRWe-M-aWI9B80C2D7Wu4VQs5z-gYFLudrhP4qvkN4Ifv0LZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5f384d1a.mp4?token=dPUcuY-E0qzEjMyPtHK6iBDr-6q0GgxRRA0Kx5ZVEXLXuFIBkETzVIyafLZfeITxWjigZdLD5p-Bb1w7nMlUMwjdUUtSG36XQom2O5JY6Og2tHSOmPj-KY2uZ5FXm6XzdWUGPdp25HcejfcGEffgLrL5lTIOeCj_O8rj2H_6LTeJgjJHwXTwTiqBl35LjZqrLd1sRh_DoyuSroG8lQKsP2dW892XGcEcftycexb5zzOngyQ-ROloqjTG_-MhEWUCo4yWfGaecGDmpqvl5LwfjR4rzVX2OtvltefjwoRWe-M-aWI9B80C2D7Wu4VQs5z-gYFLudrhP4qvkN4Ifv0LZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات حمل‌ونقل عمومی تهران در روز دوشنبه
🔹
معاون حمل‌ونقل ترافیک شهرداری تهران در برنامه پرچمدار: در روز بدرقه خط یک BRT مسافر پذیری ندارد اما مترو همان مسیر برقرار است.
@Farsna</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/446827" target="_blank">📅 23:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446826">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cac88d5370.mp4?token=QrcwCbsOdZceyWzrcF1-jMTZsqcvycPwmlybzAvmnMbwwIFSZkZ14b9J6gXRaXy2fs4ZNgB8Dtn03-4CvcnCpMa1CigRnojYiIeSYjHHNzdJHGNurTgDZ5vYypih_Rm5VXipAFBN9z-FsSIOKf7AhlSN2n69auS9CfMH1BLzlGRZowQ8IRGzCzp4FzdQ7uk6vI4I41JAnvaY8UggZbRfBASRVh6sL3DeQfVcfNF6EuPpVCE7f3JprCHCeyS7JaCQ_RzOYPOuwksLF_4KgsGr4g_65PgYeh-2kJFlSiXC5I2AwNNl_nedvrNycTAFKMFhGo3pKgR0g29POYusX2w-Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cac88d5370.mp4?token=QrcwCbsOdZceyWzrcF1-jMTZsqcvycPwmlybzAvmnMbwwIFSZkZ14b9J6gXRaXy2fs4ZNgB8Dtn03-4CvcnCpMa1CigRnojYiIeSYjHHNzdJHGNurTgDZ5vYypih_Rm5VXipAFBN9z-FsSIOKf7AhlSN2n69auS9CfMH1BLzlGRZowQ8IRGzCzp4FzdQ7uk6vI4I41JAnvaY8UggZbRfBASRVh6sL3DeQfVcfNF6EuPpVCE7f3JprCHCeyS7JaCQ_RzOYPOuwksLF_4KgsGr4g_65PgYeh-2kJFlSiXC5I2AwNNl_nedvrNycTAFKMFhGo3pKgR0g29POYusX2w-Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
داغ علی اگر چه روی قلب‌های ماست؛ امروز ذولفقارِ علی دست مجتبا‌ست
@Farsna</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/446826" target="_blank">📅 23:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446825">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f2df4beb.mp4?token=DsGlelKvB0RlN9hkF6zbgITlpBgLkRKES-zPh47pnbkK_iye9GPMpHRFteLen7plin4UpoNCSIRbuACe3fdOIlrfCenZ_voW2BqMGskkrl40WDzEO8Rslzs1S5KC0urdmSf1_9LzSh5fsGfcyPAaY-bYCEEYa1pZr4zUFcgz53uhDcCIh9PGKU6Bk3GtQD4o0Wd7khF7HUV6FZnYNbSIuusBOVhqAZQIiCtXwGm6zXu3hvUWm0EXsZPrhbUhQAKhXJanDaSh1zMgF9HHqk7gU0wfxOmLG2kOV71hDEIUDtU0I0JnLGuuHYPLgMFAt6NGnxiBsa5S6UfbyiZLhPNyRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f2df4beb.mp4?token=DsGlelKvB0RlN9hkF6zbgITlpBgLkRKES-zPh47pnbkK_iye9GPMpHRFteLen7plin4UpoNCSIRbuACe3fdOIlrfCenZ_voW2BqMGskkrl40WDzEO8Rslzs1S5KC0urdmSf1_9LzSh5fsGfcyPAaY-bYCEEYa1pZr4zUFcgz53uhDcCIh9PGKU6Bk3GtQD4o0Wd7khF7HUV6FZnYNbSIuusBOVhqAZQIiCtXwGm6zXu3hvUWm0EXsZPrhbUhQAKhXJanDaSh1zMgF9HHqk7gU0wfxOmLG2kOV71hDEIUDtU0I0JnLGuuHYPLgMFAt6NGnxiBsa5S6UfbyiZLhPNyRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال مردم از مراسم وداع توقف مترو در ایستگاه مصلی را لغو کرد
🔹
به‌دلیل افزایش ازدحام جمعیت، از ساعاتی پیش قطارهای مترو در ایستگاه مصلی توقف نمی‌کنند.
🔹
برای مدیریت حجم بالای مسافران از مسافران خواسته شده به جای ایستگاه مصلی، در ایستگاه‌های شهید بهشتی یا…</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/446825" target="_blank">📅 23:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446824">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fb1dcd259.mp4?token=R8vudZJ6LtjIFnvqn3bPTrdtlQSivwa6PgCF4KnInsgDbWvzEgSnxPzi4fu8kY2k8tR16M4asfe8xHc3v2s0KWXI6mzlI_alJl2Pc8QhdVcRbf3GnqD-XRVXEsj1OlwAUuZiJSG7ZqYYUeaK9PTuSrW3hjoxhzGEq-Z7Oj6DXRQLsOhG6IMg283jHM202Yjx8qEcuM4Vzs0efIIhQYzkKZcfuH19-5xUlAE-p2aKjId4AmmVFxyiai29VBwueX3h-kJ_zPLywwSVvTiU2HBUgHbkE9k3we2MKzB1GA6qTJYuFj4iec4anly99EVZICEZUWUKHhhk0gRXoiz63gTxqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fb1dcd259.mp4?token=R8vudZJ6LtjIFnvqn3bPTrdtlQSivwa6PgCF4KnInsgDbWvzEgSnxPzi4fu8kY2k8tR16M4asfe8xHc3v2s0KWXI6mzlI_alJl2Pc8QhdVcRbf3GnqD-XRVXEsj1OlwAUuZiJSG7ZqYYUeaK9PTuSrW3hjoxhzGEq-Z7Oj6DXRQLsOhG6IMg283jHM202Yjx8qEcuM4Vzs0efIIhQYzkKZcfuH19-5xUlAE-p2aKjId4AmmVFxyiai29VBwueX3h-kJ_zPLywwSVvTiU2HBUgHbkE9k3we2MKzB1GA6qTJYuFj4iec4anly99EVZICEZUWUKHhhk0gRXoiz63gTxqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین یکتا در برنامه پرچمدار: مردم عزیز! خدا به ما رهبری عنایت کرده که برادر شهید، فرزند شهید، همسر شهید و دایی شهید است.
@Farsna</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/446824" target="_blank">📅 23:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446823">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/363ab4d421.mp4?token=mtR_qjI50nHaYRmVNVWYgd33hO53olpqsTzIcW-P5nlA6tY0C9QGqROXRd1htZJnPsOLbYL5i3E2mWoPe-5GRJW0e4jRxD1J6RKLCMKQ57RfCjtkQGEkJkkhTf1EJU7fsRqIBjOAeESvkcErvfEbhbHmukEq5r5BVEsfpd82fallj5p8B6PkNhhMxTM4wq3uoxVLQBvnynmjg3f4dd_HjZYPVmynDuPHNB1WGBuDxAZmNqkv819sbo3UdfayNz4J1BCCOZAnIGOTEXROPFQzn0l3iQXVOCedYjcVEq7EOEsQkbw3IYvUyOEUffPgct0zGlEZN4Se74vCJXKziqBa2VHFQbtaBEBkbkWwvaPIU3nEU3hzksd0L46AuAbtLwheCLA-faBZTCI1iDmnclk7RanGHcZrybNuOoodr1mgeeSgRerprtlnk9BiSge2XtaSEtVOF9RlUKdzbhxzpF86DfI-pilzT37f_3CRxxVz2fBe3Ecutnrrn3z50EClgCpDG7FDk4VeP_tUKeIuVS8XtByYZhdMoF5R6bFaAzwsJNH1emUJJdL5ohRcbPNE3jB5dR_OKssYYLocEhW9rt5kfXpbqeTaEeX524Ri2KR1q1Fp8v-G0E_eCSUnaNLk5-vs1EBBzuaar2qJQ7EAUVeVpec1CtyQBMb5eT38-YHRuxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/363ab4d421.mp4?token=mtR_qjI50nHaYRmVNVWYgd33hO53olpqsTzIcW-P5nlA6tY0C9QGqROXRd1htZJnPsOLbYL5i3E2mWoPe-5GRJW0e4jRxD1J6RKLCMKQ57RfCjtkQGEkJkkhTf1EJU7fsRqIBjOAeESvkcErvfEbhbHmukEq5r5BVEsfpd82fallj5p8B6PkNhhMxTM4wq3uoxVLQBvnynmjg3f4dd_HjZYPVmynDuPHNB1WGBuDxAZmNqkv819sbo3UdfayNz4J1BCCOZAnIGOTEXROPFQzn0l3iQXVOCedYjcVEq7EOEsQkbw3IYvUyOEUffPgct0zGlEZN4Se74vCJXKziqBa2VHFQbtaBEBkbkWwvaPIU3nEU3hzksd0L46AuAbtLwheCLA-faBZTCI1iDmnclk7RanGHcZrybNuOoodr1mgeeSgRerprtlnk9BiSge2XtaSEtVOF9RlUKdzbhxzpF86DfI-pilzT37f_3CRxxVz2fBe3Ecutnrrn3z50EClgCpDG7FDk4VeP_tUKeIuVS8XtByYZhdMoF5R6bFaAzwsJNH1emUJJdL5ohRcbPNE3jB5dR_OKssYYLocEhW9rt5kfXpbqeTaEeX524Ri2KR1q1Fp8v-G0E_eCSUnaNLk5-vs1EBBzuaar2qJQ7EAUVeVpec1CtyQBMb5eT38-YHRuxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ذکری که رهبر شهید بعد از شهادت شهیدرئیسی به خانواده ایشان گفتند
@Farsna</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/446823" target="_blank">📅 23:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446822">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571b14494f.mp4?token=cYtIJumP7vcUr7yMCHEDLwxwt1mbv4MdtIpfkR7OvyN5CN1AE3g3SpnRhrqucKeTAjIoMD_QapnLw71Sq0j7L5VNkO1w1zla4JGAkb5ihlG8gkpaX-ygjvuisFfcjGb1f_dh3Up86I6ny3o9fSFp2MiFi9UJJmoZEWkLejYxR96U7tvZKkBSnJECYrrtzGWCfu1YauQZlGi7ABDbtEebqa7q2VwlH8rmSv43Qu3wORidnjEP-FZ4w5TOe1UZ6pWfh7NrXSee6_ihwV6zg5tnEWRsnngo4ToEvdIKwV0Mftqjvb9-ZhQR1NWAn3RHvAgkf4baG59cizlIuuEcojQW6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571b14494f.mp4?token=cYtIJumP7vcUr7yMCHEDLwxwt1mbv4MdtIpfkR7OvyN5CN1AE3g3SpnRhrqucKeTAjIoMD_QapnLw71Sq0j7L5VNkO1w1zla4JGAkb5ihlG8gkpaX-ygjvuisFfcjGb1f_dh3Up86I6ny3o9fSFp2MiFi9UJJmoZEWkLejYxR96U7tvZKkBSnJECYrrtzGWCfu1YauQZlGi7ABDbtEebqa7q2VwlH8rmSv43Qu3wORidnjEP-FZ4w5TOe1UZ6pWfh7NrXSee6_ihwV6zg5tnEWRsnngo4ToEvdIKwV0Mftqjvb9-ZhQR1NWAn3RHvAgkf4baG59cizlIuuEcojQW6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرایی که از کودکان شهید میناب نمی‌دانستیم
@Farsna</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/446822" target="_blank">📅 23:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446821">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62936c652a.mp4?token=Tc1TwQD0PIqTB7QKjklD7K2Sr2sIM_LWcL5cPHKKQ-IBId-i9ho2vz8gxm6Q7hAVhMEIM3l6jBVLUM_rLrcoyRSqBmhCRooofuSc-bsG0bFY4tZTzuCHrmdenfJJqkQtUbCEnd9TZrXVGlRmicsDRQWh0U_CsxASb_iOQGtsWCEsLHx6WtHD5dEbIZ59yKDpXTvd2EXwrvdMsRqwgVpksjtUnbdU2lSLmSjTZDLQVAm_r9IX_mPPpoXRam-Ulad369oeVIGAzvbzu2eAAtKV6c9wRHCj5Ub0_Lf3bf8B1-mbMyruGTKhXh2U_q4hhauHEbhErEO66G3_N_5jyuMwFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62936c652a.mp4?token=Tc1TwQD0PIqTB7QKjklD7K2Sr2sIM_LWcL5cPHKKQ-IBId-i9ho2vz8gxm6Q7hAVhMEIM3l6jBVLUM_rLrcoyRSqBmhCRooofuSc-bsG0bFY4tZTzuCHrmdenfJJqkQtUbCEnd9TZrXVGlRmicsDRQWh0U_CsxASb_iOQGtsWCEsLHx6WtHD5dEbIZ59yKDpXTvd2EXwrvdMsRqwgVpksjtUnbdU2lSLmSjTZDLQVAm_r9IX_mPPpoXRam-Ulad369oeVIGAzvbzu2eAAtKV6c9wRHCj5Ub0_Lf3bf8B1-mbMyruGTKhXh2U_q4hhauHEbhErEO66G3_N_5jyuMwFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خدمت‌رسانی وزیر علوم به زائران تشییع رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/446821" target="_blank">📅 23:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446816">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YUZYSyYCkJIoDBl_PV-sP_1ohfPiCaSlsD3ybyPGNxJYkL3nXMQOx5td5-8hkLGWFxy74xnAMgfFxQq10OygQ9HDAdgkW1udgXfcq63YICaYsWA8hjpXn36qJl5P2d18SfDWOv4Z4WWrOLnKtZAmx5f7z6V-BdWqojcnwSa99ozVjlDqSTwV61glWgUYfadhKxmvaFv1Pz18ZGrVEMr3ErDNX_Q_yKbKj0biokGIeFcLnj6JPrl6B5OUJlH5EXQlTxZHnRuU9UDBNsmnuSr3uFZHbPExOwDo2oAIJNOYaAveoUmweLnFfh4wZ11o-d71HWD89hw6_HjEGbjHgi07kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q0r6_LBkOP8SRnxL7gSQgtsMPdIcPyylqvcy9fAxXNkf18NP1EzoSggBQ_VxyVNt5ArzMHsfr7QXB712FQDWxPqmLX60jn1VdBZY-0vb5V2BvkaN1Rv65EvYG-JW0DucXYDyv-cuL46lKPLbtJ7KHhrccSrM6hPBy0jtsbFscTqo-2lqzV_br69_AlWgbzyoofAKU-boM-LCN1bA7LKbAye3oelH3qDpLD_Mf-IfatGoo0skFC4GrZM0MmsL5YcDjRYwC0ZiPecYStkVlEORyKv1uMWZazdnQh76R-OhPWefjNHq8ifiE0ju0LxaMQN9Rhg02zSrmWnrNXmkuqJGqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OAY6498F3yKBwhD_7baOQCji1lVo82wFcpv7Alo0ArKpgvX8cqr6psZuWf_zyBOIT3Gawa2jCyhFaJhkMJ4ei67pkSVa51qinXGraS2q7BmISaGAmnZHPa_1H0Zuipc-WUUZA1eQlxSqUMdPUBSJM9ED43y8jCH4phTLuJWjv0TT_wA3yz-M8vGIyAEnwtsV_o2ocX5EIhwhiyvEyjrSlZb3p0CBFBB4aOe1CM-6AhwIl6jPaNqFZnfg-rCxYhhGg7bZUM9pYTz8uc4O5FX3KsB1OM2NXlzb-AL9FIEH1alw4wvGP6CBpSEbHat0lM2ypnKUgT0fBgYgiivl-qRC4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ObmTSzqhxHhgwoc0pB44yhHC_GfkEIT9p8VPNdEqkQEaiZoln8JDznSTJJDHVptNDr28iU2R5dNDp5JjgPQTEmhSZLd5ALL4QZ4fvm7ofhvZo1S5gUdxViUMGTY0DDdDrCp5B3iCLdpKHMjEB9X7Y6vSEltQQ8PHjhwtJVBt-thQXhKXNdtZLpnGK5XLYyLEzKcoKk_qaHpY2RgcQ20YpNdZPHzR9RqZtpNQT7LlbnU0kB3tLot3weMRLoQo5FNAAcaBVu74dwxZnLSdXb9WkFA8I3EjQaABX2dSqUNMi0S72I0hkfRFuezJ7qcGCq1RTgTN_9m5rlQgZbYMgBM3tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q4kfzEpeBF3dFrdtRDMKZYtuDfuIx1ir_z9FaVUT_N4r3Cr3hBRqeH7zcIiYdPYXjeXS6AGu4lBomh1L13VMhZkplxca5Q5esTw-BXzawlpNcHkmevHYv_SYlVx7pdRH-1EVj6iN5wwCrV7ZkrJ92YzNUhNo05TPSsf46nA1c06zp7X1ACUT3-xxJwEL1KWZoN09KNkYrCwBqeKRIysCsfkJ0OpnXMEVqRxyxS6ir8Y8lZZGJGYkExQVBTkmUm02ttvSeIHHHu4F-Spf95jfDYta50fkMbHVGvpS5g6RcTqGJf2VzSmVBC7tXgjVHTKOK-wh3Xo-g6jiA05zXeMzzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خانه‌ای که آشپزخانهٔ زائران قائد شهید شد
عکاس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/446816" target="_blank">📅 22:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446815">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4PXjoshNkwqb2qbPVSZNjBhazEDhG7oCDilk_fL48jt-mPu25bLPQNzY8FF1P9izbvtQCmAcnkCI0yGdXCLFcrf64PsYCK-bqTnZQGlnIVjIXYqkOQbKTrQ_-E2H7D6RgeB50OGzYMFtnLcyV1OgtDi31QIblWY1Am72V69YK9udxWBJkhWL-39dmbMvAEm2Q33A2xe3m5gaDBO9qNQrebSkfdWCJDUzO3qcqGWywNgtnFCW_nH02ySdOa9qQQIwOkIGeQ8w2nR7WzOqBVOT6NFAi2vWdyRbEq8VsfgStsUZe0vT3qcvfd4XjxrEajerI1fZ42tu9HjbNuWW7H5ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراکش با عبور از کانادا برای فرانسه خط‌و‌نشان کشید
⚽️
مراکش ۳ - ۰ کانادا
@Sportfars</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/446815" target="_blank">📅 22:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446813">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxW_eofD_o-gEKI2-wf9ykdq6omW0SH1okj8gOmPpi6YrCi4YH9ILavB4iifxUClLsLjHN5waEnxi-J8WJKOv0PHiVEt74TMlttAfYwm1dG6_9ctVICWfkhQqocQpFjBECOwqPcDgrdHmGucym7nRzUA3sd6pw5MZy_oxYupIl2VQ-8yXyIuEJVQ5lN5cP4AezMzcLXoU2zks0DeSE03btwWwt8XowXt4yIlvXceksjYtObp4CajCSz5F_dWJBV6L0OxREg4HgP2j0b-rzPJxm_x1rXx1dXOu81KATDvZSxl2uCkxwPjs2yfmtLvu4EKPOPvvNgel9H_-JYoqhUikw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آزمون بزرگ مدیریت جمعیت؛ کارنامه موفق تشییع رهبر شهید در روز اول
🔹
با وجود تردد لحظه‌ای و هم‌زمان ده‌ها هزار نفر در ورودی‌ها و خروجی‌های مصلی و تخلیه و پُرشدن متوالی فضای مراسم، مدیریت جمعیت در تشییع پیکر رهبر شهید انقلاب امروز با نظم قابل‌توجهی همراه بود.
🔹
از ساعات ابتدایی صبح، ورود و خروج انبوه جمعیت بدون ایجاد گره‌های سنگین ترافیکی یا بی‌نظمی در صفوف دنبال شد. آنچه این روند را متمایز می‌کرد، تدارک گسترده خدمات پشتیبانی شامل آبرسانی سیار، سیستم‌های مه‌پاش برای تعدیل دما، استقرار نیروهای اورژانس در نقاط کلیدی و جانمایی سرویس‌های بهداشتی کافی در اطراف محل برگزاری بود.
🔹
این تمهیدات درحالی اجرا شد که پیش از آغاز مراسم، اصلی‌ترین دغدغه و توصیه مکرر ستاد برگزاری و مسئولان شهری، کاهش هرگونه آسیب جسمانی و مدیریت ایمن جمعیت با توجه به حجم چندمیلیونی شرکت‌کنندگان عنوان شده بود. با توجه به مشاهدات میدانی، به‌نظر می‌رسد این تدابیر تا این لحظه توانسته است از بروز حوادث جدی جلوگیری کند و تجربه‌ای کم‌نظیر از برگزاری ایمن یک رویداد عظیم را رقم بزند.
@Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/446813" target="_blank">📅 22:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446812">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5076b3127a.mp4?token=kkGpYDN-Sy6qXuITToqGxl-tJcHiviu-VL7MOSmmGHo0D7DjmTuZn4zzMNmdXzFB98_NaTivFyNIobaSbul5r_8yyKDnDAwhr-OD_Q2NnLZzClTGibmKY5omiW914YtMLt9c7bLVz6AP0TJBBD1l8COMNBtQ_3UUcCk8uT1Y_-08wxMYdNSzJ8JgUemlL8fi9oXoiw55p-NR_S5MG4mzMYf44DxXimsJW65pEO0kk70-ove-KqylVPpEZFkTGDIfIJs825ZlHReFCaTwHXDOAtXDpwU0EaN4uUQDTqsuharzd3Scblzqwiy0T6g1eRhjcYCSFmVa4AWr5xsn5I66vwIC3KB9gk7QJm2whMa6I_BKUnme003dfr_edcHGgPr-YDWaEpTbTs0mKKZ3DT1EnHyznmQKEujiOX1T50h5wIrab27vsxkS9ODjsImvZaSQGKXIvjdwK3ZVGSb25hd8MlV439VUiyZKRuOiEH6EB5OKKzEDPxUs7A45gkY6tTbayvhpzHjvYqauTSK3mLBoWMy-vCwpXjohqkGocoEwyg0oKDgj_85PlNbba2AWa36ihJRURqpiFA-rnnEgSCC9VlSRpmDsrBdFDvR_QMQDnrxGFgzkdaGVwGy-O4g1HavpxDSeGEDHp4hYpLITIrikmnSgtjv7drtPM1Qffxgbj0U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5076b3127a.mp4?token=kkGpYDN-Sy6qXuITToqGxl-tJcHiviu-VL7MOSmmGHo0D7DjmTuZn4zzMNmdXzFB98_NaTivFyNIobaSbul5r_8yyKDnDAwhr-OD_Q2NnLZzClTGibmKY5omiW914YtMLt9c7bLVz6AP0TJBBD1l8COMNBtQ_3UUcCk8uT1Y_-08wxMYdNSzJ8JgUemlL8fi9oXoiw55p-NR_S5MG4mzMYf44DxXimsJW65pEO0kk70-ove-KqylVPpEZFkTGDIfIJs825ZlHReFCaTwHXDOAtXDpwU0EaN4uUQDTqsuharzd3Scblzqwiy0T6g1eRhjcYCSFmVa4AWr5xsn5I66vwIC3KB9gk7QJm2whMa6I_BKUnme003dfr_edcHGgPr-YDWaEpTbTs0mKKZ3DT1EnHyznmQKEujiOX1T50h5wIrab27vsxkS9ODjsImvZaSQGKXIvjdwK3ZVGSb25hd8MlV439VUiyZKRuOiEH6EB5OKKzEDPxUs7A45gkY6tTbayvhpzHjvYqauTSK3mLBoWMy-vCwpXjohqkGocoEwyg0oKDgj_85PlNbba2AWa36ihJRURqpiFA-rnnEgSCC9VlSRpmDsrBdFDvR_QMQDnrxGFgzkdaGVwGy-O4g1HavpxDSeGEDHp4hYpLITIrikmnSgtjv7drtPM1Qffxgbj0U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد خون‌خواهی رهبر شهید امت در تجمع شبانۀ مراغه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/446812" target="_blank">📅 22:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446811">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2d6a8980c.mp4?token=BeQonWe3qESvUQlbXGUR0SJ-wDohnKKIdXmaMIEerfJozTZlOyRSy087QbnPjLnz97WPk0Jjs_YxtAHHQwU4r4On8z3PYofFA3WST9TWH884oq_zmE4a56xi1odkbxe7_DBfinKvWZgqs7I4k7vsjBVuuI3kRTLOOysZb6PNNGKz5T0r7CaG2rEt5tasmR7RXvdEaZPGApjhDKGaK_pLcFVR2U40fXuiTzISdf_qUkRsu5ExRpUkThWu9W38yequzo2d_4aSiaRAsaQB0tJmdFw7kbA8jFU-NNgVRP87i1nOGoSPoIx-APGlJmjGO3SKX4hT_fYP9jr5m5eMQtNOfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2d6a8980c.mp4?token=BeQonWe3qESvUQlbXGUR0SJ-wDohnKKIdXmaMIEerfJozTZlOyRSy087QbnPjLnz97WPk0Jjs_YxtAHHQwU4r4On8z3PYofFA3WST9TWH884oq_zmE4a56xi1odkbxe7_DBfinKvWZgqs7I4k7vsjBVuuI3kRTLOOysZb6PNNGKz5T0r7CaG2rEt5tasmR7RXvdEaZPGApjhDKGaK_pLcFVR2U40fXuiTzISdf_qUkRsu5ExRpUkThWu9W38yequzo2d_4aSiaRAsaQB0tJmdFw7kbA8jFU-NNgVRP87i1nOGoSPoIx-APGlJmjGO3SKX4hT_fYP9jr5m5eMQtNOfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام عابدینی: رهبر شهید انقلاب در ما باوری ایجاد کرد که امروز حتی کودکان ایرانی نیز ناوهای آمریکایی را به تمسخر می‌گیرند
.
@Farsna</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/446811" target="_blank">📅 22:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446808">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4045b92706.mp4?token=PmZsI-J6C4dqC3JHzOGUHUCKr5erwgnphxDIyTlKg27Q-oNupSs2vpWldXe0QZarB6hByrBCrgrP4Y0eLcIuPM_aM3MR_YBXzZdw4gQYjLomUKgdJYXx0kOp4E5wdEPZru3NoH-ldbCBDAJU79rulRUkqrJMVu99_vhDSvhOGJwhWz-t8BtfCqeEvW2uF2skTV22x4DGP8ZZO4V5HkY2AwgzydCS214nKenvWPrPkncfZrmUkRPk1tlkuJtfBsKjMoDBrK9bBElyfAZcwI0w6xpZ0GFmE9ZK7lh-AGzPm_VEGyTV_yeZaCOTRfJLGUeEaoqU6gWN0ZbH4Vy3aSYHCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4045b92706.mp4?token=PmZsI-J6C4dqC3JHzOGUHUCKr5erwgnphxDIyTlKg27Q-oNupSs2vpWldXe0QZarB6hByrBCrgrP4Y0eLcIuPM_aM3MR_YBXzZdw4gQYjLomUKgdJYXx0kOp4E5wdEPZru3NoH-ldbCBDAJU79rulRUkqrJMVu99_vhDSvhOGJwhWz-t8BtfCqeEvW2uF2skTV22x4DGP8ZZO4V5HkY2AwgzydCS214nKenvWPrPkncfZrmUkRPk1tlkuJtfBsKjMoDBrK9bBElyfAZcwI0w6xpZ0GFmE9ZK7lh-AGzPm_VEGyTV_yeZaCOTRfJLGUeEaoqU6gWN0ZbH4Vy3aSYHCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلاش بهمن‌موتور برای تغییر کاربری ۱۲۰ هکتار زمین کشاورزی
🔹
گروه صنعتی بهمن طی ۶ ماه اخیر ۳ مرتبه برای تغییر کامل کاربری یک محدوده ۱۲۰ هکتاری زراعی در جوار روستای دانش شهرستان قدس تهران تلاش کرده است.
🔹
طبق گفته شاهدان محلی این شرکت این‌بار به بهانه ایجاد…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/446808" target="_blank">📅 22:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446807">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🎥
نریمان پناهی فضای مصلی را عاشورایی کرد
@Farsna</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/446807" target="_blank">📅 22:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446806">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/0764895667.mp4?token=BsOE_YeI9uH6Ir6XlU6RF-91ya0cnfGG3wM6jDKNbMxWCv0DrV5Q0seGYxVyi-F0AgZB5e1OSTuyveXLGevT3sp-ztj7YtHdDsu6kPRTGsVIycPls8iT1Jp0IRWI7tOXxi2B0XWl2t05w6qeH6Kyebxtid9XIj-3o9taVAwJGcOAhbIrZBNSGWCPNU-HquyS6IDM6dDzOCD4MBvENDWKQkXBNravB2fxnW_yPdEvZFB1f6fiE8xseqW90sHKWBQ2NhrDz5pPCFwzNzXTX1fHOPyteQbzQSuK2EbNz_Ib2NYphZdMZJnFtuIzwlw6cpa4jg5BH2v2djXHylPz9FwSrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/0764895667.mp4?token=BsOE_YeI9uH6Ir6XlU6RF-91ya0cnfGG3wM6jDKNbMxWCv0DrV5Q0seGYxVyi-F0AgZB5e1OSTuyveXLGevT3sp-ztj7YtHdDsu6kPRTGsVIycPls8iT1Jp0IRWI7tOXxi2B0XWl2t05w6qeH6Kyebxtid9XIj-3o9taVAwJGcOAhbIrZBNSGWCPNU-HquyS6IDM6dDzOCD4MBvENDWKQkXBNravB2fxnW_yPdEvZFB1f6fiE8xseqW90sHKWBQ2NhrDz5pPCFwzNzXTX1fHOPyteQbzQSuK2EbNz_Ib2NYphZdMZJnFtuIzwlw6cpa4jg5BH2v2djXHylPz9FwSrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انفجار تانکر سوخت در آمریکا
🔹
پلیس شهرستان مونتگومری در ایالت آلابامای آمریکا روز شنبه از انفجار یک تانکر سوخت و آتش‌سوزی در محل حادثه خبر داد.
🔹
این انفجار حوالی ظهر به وقت محلی رخ داده و علت آن نقض فنی اعلام شده است.
🔹
این حادثه منجر به قطع برق چندین خانه در منطقه شد. پلیس از مردم خواست تا از ورود به این منطقه خودداری کنند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/446806" target="_blank">📅 22:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446805">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36cc42a03c.mp4?token=Ib-s6e0SxCav5hMFIXzCdJ9Sq5qulpRL5qB1Oxv-_pHxZo0x42tiBmAA5t1-XgR90UvQYnZ0YkHu7Nh5q7QoUeTjdmtS8DHRVmv31H-ysK6TE3nu_U4-nltp3odumyy20Q9GI9wEaz4sZSrLxFzu2rKpr7jA5a3Ma1eF3PeLcWQe8VZ3N2MX4sWghasqD3j4A_1udnCuKJfFcVs68KsaPbVVOJrdYngcdU8M-l2IMAxuZ9dfbDSebq4rhS6lpac2HhPdtMFj3OdlXDfAy-xZ5Zo-VI-VavvTfcC7J8dCqVkeSPr9Gv_flbGmqSRcsjwNEMugoE6hw4h1Pbed-dozM0aBjjFnd2LdfagX7SMZe_AgE8l6kKNyuGHMCeHLV7IA3NKKPd2YcImlYO-dol55N9EUA3FH1BHvakDQLj47-qQ3FPO_iYuuNtyFGjnaIAqxOkrZ4341uKJqYTb6VWGvtCJics0UXl3t51B2_nPyfTAkNrCmWLgMBRq68xEqCaexVxErNmvTYAVbWiZy8vBhkCL34OuuBbOIDTWdaS5SANCx-Ox6NR8Luo07v_q_eYwchiliCBVXoV5PtnBJCopAPzeOqM_Vfh5FUGqP8eEaLr0vJlQdh5VbNCs3GYo-FkHMALyTWZcne05a2p4dTVBDqTCzAOqpqBTOCXzMJ5issco" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36cc42a03c.mp4?token=Ib-s6e0SxCav5hMFIXzCdJ9Sq5qulpRL5qB1Oxv-_pHxZo0x42tiBmAA5t1-XgR90UvQYnZ0YkHu7Nh5q7QoUeTjdmtS8DHRVmv31H-ysK6TE3nu_U4-nltp3odumyy20Q9GI9wEaz4sZSrLxFzu2rKpr7jA5a3Ma1eF3PeLcWQe8VZ3N2MX4sWghasqD3j4A_1udnCuKJfFcVs68KsaPbVVOJrdYngcdU8M-l2IMAxuZ9dfbDSebq4rhS6lpac2HhPdtMFj3OdlXDfAy-xZ5Zo-VI-VavvTfcC7J8dCqVkeSPr9Gv_flbGmqSRcsjwNEMugoE6hw4h1Pbed-dozM0aBjjFnd2LdfagX7SMZe_AgE8l6kKNyuGHMCeHLV7IA3NKKPd2YcImlYO-dol55N9EUA3FH1BHvakDQLj47-qQ3FPO_iYuuNtyFGjnaIAqxOkrZ4341uKJqYTb6VWGvtCJics0UXl3t51B2_nPyfTAkNrCmWLgMBRq68xEqCaexVxErNmvTYAVbWiZy8vBhkCL34OuuBbOIDTWdaS5SANCx-Ox6NR8Luo07v_q_eYwchiliCBVXoV5PtnBJCopAPzeOqM_Vfh5FUGqP8eEaLr0vJlQdh5VbNCs3GYo-FkHMALyTWZcne05a2p4dTVBDqTCzAOqpqBTOCXzMJ5issco" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
به رهبر شهید ایران سلام / سایۀ سیدمجتبی مستدام
🔹
دودمۀ امشب مردم ایران در مراسم وداع با آقای شهید ایران.
@Farsna</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/446805" target="_blank">📅 22:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446804">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/174a13c993.mp4?token=CP67thvSsRUDxI8-cIAc_aWMqbzp_M3_YGPOr_Z41kk491gi5oqKWf20uobBeiXLnPp1mLHG_MnIoI4hIuIuEoq2r5HTtrf1lVQHZsBgM_Rbmd-WAnytKHLMgtc2VB3H2HY1T7RdRhsDOfkFkagpbrR_VvWvkOhbPhVfzQrnwE7kVJo-_KhO1dnqQT0OgsxdCfrwY1FvtAZtqLU76cKcG56pkeNhyf9AvSNlFZBZ8-6eydrFSaTFfmSSzPFUFwY4Zm7cthfKKrn7FIZZ_GHk0-e_a0Nc1KftSaXTAx1L6V9thEFuvn1jNYcXLjwlJGWoYEN5r-VsDdOPwoJwz6yobg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/174a13c993.mp4?token=CP67thvSsRUDxI8-cIAc_aWMqbzp_M3_YGPOr_Z41kk491gi5oqKWf20uobBeiXLnPp1mLHG_MnIoI4hIuIuEoq2r5HTtrf1lVQHZsBgM_Rbmd-WAnytKHLMgtc2VB3H2HY1T7RdRhsDOfkFkagpbrR_VvWvkOhbPhVfzQrnwE7kVJo-_KhO1dnqQT0OgsxdCfrwY1FvtAZtqLU76cKcG56pkeNhyf9AvSNlFZBZ8-6eydrFSaTFfmSSzPFUFwY4Zm7cthfKKrn7FIZZ_GHk0-e_a0Nc1KftSaXTAx1L6V9thEFuvn1jNYcXLjwlJGWoYEN5r-VsDdOPwoJwz6yobg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محسن محمدی‌پناه، مداح نماهنگ «باید برخاست»: ما مدیون آقا هستیم و نتوانستیم حق ایشان را ادا کنیم
🔹
این داغ هرگز در دل ما سرد نخواهد شد و سوخت موشک ما برای حرکت‌های آینده می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/446804" target="_blank">📅 22:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446803">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/699642a8c6.mp4?token=WtM1dx-Yfew3uJf1TA_i_oShdcgO0bPcQkw9SO_KLvxqIlncdNn00H1m96jo0hbcuPrh4kP0TwAnbkWQnGvfZPipD7SjONKecUuZ1nVgsWONqJU72wDxovWrL3GnFX1UF5kznDeZ9uXBPrYKA1-uE2frOIzDzOtt0virFU1cWUEjNT3nr3srwAYDYO2A7LvMqhvmmVeq4MIEvtrRepOi3biFPgqSmeIrceSI_SyM6qJ9cppl2oO7kEQgZuatF8cgGfU_1WnVbHzP8rLjjQCFoLiw7a5itRC64gVQbQ3tSRM50Rz_XcsG6WzWeoQCBEEdKPy9ZRO4h8rnf8NoXzNz7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/699642a8c6.mp4?token=WtM1dx-Yfew3uJf1TA_i_oShdcgO0bPcQkw9SO_KLvxqIlncdNn00H1m96jo0hbcuPrh4kP0TwAnbkWQnGvfZPipD7SjONKecUuZ1nVgsWONqJU72wDxovWrL3GnFX1UF5kznDeZ9uXBPrYKA1-uE2frOIzDzOtt0virFU1cWUEjNT3nr3srwAYDYO2A7LvMqhvmmVeq4MIEvtrRepOi3biFPgqSmeIrceSI_SyM6qJ9cppl2oO7kEQgZuatF8cgGfU_1WnVbHzP8rLjjQCFoLiw7a5itRC64gVQbQ3tSRM50Rz_XcsG6WzWeoQCBEEdKPy9ZRO4h8rnf8NoXzNz7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار مردم در مصلای تهران: ما همه خون‌خواه پدر، گوش به فرمان پسر  @Farsna</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/446803" target="_blank">📅 22:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446802">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815c9ff5ee.mp4?token=iszYpICYklpTY0shg2mHcPouqcHAd902yofJ9ExlQlQHY-Iot6d9rNo23D-c-_3eiwwuM9SWoj_rtKsPJaLG1XzEmONGdhquXr4DBb451y-Vruf1j2NsIHbQHkRHLa_ujzi7CP1uSfkUXIx8N3vwHzdKrL4xzquX9PqhhmJY2UtFjwSauXzmYgt5bWL7s7AvQoB_vq55OpxIXgv7gG2nIn1yCd-Sjk-5bp5OlQbjwIDr359nJLNHQ6cvejOBnCi3yiCEpp67MusaokV2_tk-B7c1xVPkr4JBLCklTrOstZILcE7Aq4DkDGnVO6gIUH9RJsXEQYkhb4zvc2tUBKYRmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815c9ff5ee.mp4?token=iszYpICYklpTY0shg2mHcPouqcHAd902yofJ9ExlQlQHY-Iot6d9rNo23D-c-_3eiwwuM9SWoj_rtKsPJaLG1XzEmONGdhquXr4DBb451y-Vruf1j2NsIHbQHkRHLa_ujzi7CP1uSfkUXIx8N3vwHzdKrL4xzquX9PqhhmJY2UtFjwSauXzmYgt5bWL7s7AvQoB_vq55OpxIXgv7gG2nIn1yCd-Sjk-5bp5OlQbjwIDr359nJLNHQ6cvejOBnCi3yiCEpp67MusaokV2_tk-B7c1xVPkr4JBLCklTrOstZILcE7Aq4DkDGnVO6gIUH9RJsXEQYkhb4zvc2tUBKYRmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایی از حضور باشکوه مردم در مصلای تهران  @Farsna</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/446802" target="_blank">📅 21:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446801">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46bb4f1f81.mp4?token=NlO4bsU77UxRLObKbfanonr2p8QT9ZxaHMf4t3WiflN2DI7har644cvWR28BOZUjY-27KhL6bnJdqSIX2WU4WIjpf5_SbeSzbxQD074kNNC2b_PrKB_Q6TrLYf99F_21LzMu7PW8oQCFWpS9Zda8V76E1P2EujBvhRXKhsYTszzX5zp8rVTvE659EJg1CFv1-Dul6UeYTKPZJBFfjvWRqkdc0JXrOULA9IVCyibWU2b0xZfLV9u5RRhZrF6SaZX3dUz8Yo06yz_-9qQ1YYreDRmjBbXGKXyW-CqU-Ch2hB9iCw9M0DaFwIFiMQBU_AudX9OLSK9WHwb2u0D1m9HOjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46bb4f1f81.mp4?token=NlO4bsU77UxRLObKbfanonr2p8QT9ZxaHMf4t3WiflN2DI7har644cvWR28BOZUjY-27KhL6bnJdqSIX2WU4WIjpf5_SbeSzbxQD074kNNC2b_PrKB_Q6TrLYf99F_21LzMu7PW8oQCFWpS9Zda8V76E1P2EujBvhRXKhsYTszzX5zp8rVTvE659EJg1CFv1-Dul6UeYTKPZJBFfjvWRqkdc0JXrOULA9IVCyibWU2b0xZfLV9u5RRhZrF6SaZX3dUz8Yo06yz_-9qQ1YYreDRmjBbXGKXyW-CqU-Ch2hB9iCw9M0DaFwIFiMQBU_AudX9OLSK9WHwb2u0D1m9HOjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فقط همین خبر آرام جان مضطر شد؛ پدر که رفت پسر جانشین و رهبر شد
🔹
شعرخوانی امشب محمدرضا طاهری در مصلای تهران. @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/446801" target="_blank">📅 21:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446800">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5762c89eb4.mp4?token=vq0qU7Xp1oT1uaA8lPeLIR9pfDnDHhv9f2QV_G6uwL9FbgnNHv5qMO7KjudlJtJRKKbwQRkWivPWSivvl2xdjs4VwxLvri2YyXOwP4yGJTndpAfuVKLNLMAyd6cpHlvsel15Wd8KnujAR3PG2RADY4byLiIzsFv_Puhmu9kWoAWdr8r2tNU7LG6CXclKG3D22bapCiTmnynMHtyssuxsX58nZH3NZZKymc-KkUUOkVbbbpyd3jlV18UoGBAxrPy_rA0p2N5dfEZw-1s8EAkvHmnZ4mn9Aen58FLKVItLP6YAbbIi77W5tFYznARC2cWZc611zThOodpxvYwESXFkrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5762c89eb4.mp4?token=vq0qU7Xp1oT1uaA8lPeLIR9pfDnDHhv9f2QV_G6uwL9FbgnNHv5qMO7KjudlJtJRKKbwQRkWivPWSivvl2xdjs4VwxLvri2YyXOwP4yGJTndpAfuVKLNLMAyd6cpHlvsel15Wd8KnujAR3PG2RADY4byLiIzsFv_Puhmu9kWoAWdr8r2tNU7LG6CXclKG3D22bapCiTmnynMHtyssuxsX58nZH3NZZKymc-KkUUOkVbbbpyd3jlV18UoGBAxrPy_rA0p2N5dfEZw-1s8EAkvHmnZ4mn9Aen58FLKVItLP6YAbbIi77W5tFYznARC2cWZc611zThOodpxvYwESXFkrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دکتر حسن ابوالقاسمی: بمباران بیمارستان‌ها و کودک‌کشی‌ها و افتخار به آن توسط نتانیاهو نشان می‌دهد که دشمنان رهبر انقلاب چه کسانی هستند.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/446800" target="_blank">📅 21:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446799">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMKul-UQ8pLaXjXuMYtvuoCpOZp993jV6S6OAQ5LcJ6HtUkzAUtIQ-1PP-wmn6KluuKD-YgEjWoNCNmblagmFccuarcvJLLZhoZaxJiGlKzYJyZ24vg14iW0DvY6msJu8Am9sxcfEl2LTZRLRmPWTBR5YDrnpgd8aJ0kQX13avD58fGtdKxKQ8DNHP1bLXw69anlxXjACjXhxu-x193lksLcpffy7Gxhd2evy779oNrYWK9UmQx9kZvW3lhgstw3FnvnpvNAPsBXO7g3odJbQWuuNifTuS3hIIXESLeGxm1Z9RzHIoX9plcu7Y5wHiEPt-6a4Igw2R-f6rqv3NrbwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بأمان الله یا شهید الله
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/446799" target="_blank">📅 21:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446798">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/578d03d029.mp4?token=bDpPYDjz3mVH8pAAzHZCIIJ49IM2hG4Sx6lmuepBRtRngshMzoyHC_kdZH-Y2F820sX8fOsRcerngwzqsNLo0uU1-6ObaHyJsSHVGOXHS3XULwTs9i8u8FBYP_BwRvplpAgVeQiyc5BXAAe2mYznNyp-0z36u8A5gDg29y7G215bmojzkmTfQeMPCMOC1CDuY4gjY2GgR2HjN07qBzOBCy6gaBkYWe6zN9WDJjwrRa6_rIlCELTluApVuGDoMfCeFakAZELV2Ooc8LwvhREadUjVR4dICPBMZoPiGF7rl1wG3-8vfS2KqtEly_GsuJrL9lxl1Kh4PC5hEBDobo5sT2ZkmJ5iaaU6ruB6JP4xQuEthRRXqDQcMHzQEjPQjL9if4GnJSFNl__-kFgdxTCQmgFTEJhXMesqedqQ2iASKG2q2rR9UgmA5W6rrh-chc6UN-cqw4RID5aUqHghEJaVFmSgvUXBLXKGXL41jSFdfCoOrtmhQs9x0f8HmaCUHicgzobqHUsVjon_W21bIMYNUAHyL1BpAMrGm_sNhhaJA26eQTmJZUH9R6CQRMRRijryowP1SWaBjatdmOpO9dZQeVRwZxy1-BSKSDo-S7DtuhyCB9PKX7fR27q3H32IykZgWFCmywLNwJuMB6PMgShusMRvjkIjK3QZm9QCwvvl2Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/578d03d029.mp4?token=bDpPYDjz3mVH8pAAzHZCIIJ49IM2hG4Sx6lmuepBRtRngshMzoyHC_kdZH-Y2F820sX8fOsRcerngwzqsNLo0uU1-6ObaHyJsSHVGOXHS3XULwTs9i8u8FBYP_BwRvplpAgVeQiyc5BXAAe2mYznNyp-0z36u8A5gDg29y7G215bmojzkmTfQeMPCMOC1CDuY4gjY2GgR2HjN07qBzOBCy6gaBkYWe6zN9WDJjwrRa6_rIlCELTluApVuGDoMfCeFakAZELV2Ooc8LwvhREadUjVR4dICPBMZoPiGF7rl1wG3-8vfS2KqtEly_GsuJrL9lxl1Kh4PC5hEBDobo5sT2ZkmJ5iaaU6ruB6JP4xQuEthRRXqDQcMHzQEjPQjL9if4GnJSFNl__-kFgdxTCQmgFTEJhXMesqedqQ2iASKG2q2rR9UgmA5W6rrh-chc6UN-cqw4RID5aUqHghEJaVFmSgvUXBLXKGXL41jSFdfCoOrtmhQs9x0f8HmaCUHicgzobqHUsVjon_W21bIMYNUAHyL1BpAMrGm_sNhhaJA26eQTmJZUH9R6CQRMRRijryowP1SWaBjatdmOpO9dZQeVRwZxy1-BSKSDo-S7DtuhyCB9PKX7fR27q3H32IykZgWFCmywLNwJuMB6PMgShusMRvjkIjK3QZm9QCwvvl2Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زائر رهبر شهید: قیافه‌ام غلط اندازه ولی دوست دارم شهید بشم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/446798" target="_blank">📅 21:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446797">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kORR6Dom_SSUXdTLK4i8oznSULhbkoJhSfz6ezoz6J-KFj541xOcx6DQhFwU1IjVO1Yw-F0MS1W6T-SJKprZ-NEbuKFaoByf6zOQIkIJKVdaz7zJAlMF8PqRr130WGDBvSjO27VoBIGAZtuR3ehhYlU898AS1Cn0Hr_UYC4R0pTaJkM7oRCUkkZJqctrV9W8dWoA2nDLV0ysNXE2iAvhwM7A9qlSxDQ8Fy_c9gh4Nv6V9wEYoeNQPIj5lU2mibBiHQ25vxoi1UdSkVFUxTY2wElMvLNDFKw2jcaOPClhDXSgKdN9Zo9VLgS_n-ZxO7G-THV6rXbn_ZdjYBIcG9Nrvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🎥
ستاد وداع با رهبر شهید: نماز بر پیکر مطهر رهبر شهید انقلاب رأس ساعت ۸ صبح فردا در تهران اقامه خواهد شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/446797" target="_blank">📅 21:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446796">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dcfc0ede1.mp4?token=qzsIzbKxqPFm5O7QLTvKTe7L2sK6v5pmCiRsub6Wgf5aB1CFdCi3S5y4EukswFnHLOtg-AwJWjjv3x9EBIUBKv3opCX_TrtAMtSotzpZANgznFYoH2sg_xMip2gwvoHgLGspuhm9faEDvuRTTHxSQuS1pbji9jj5kOeT0PTpJ9OP_QGVPRa8CnDkh_peC94d04BqjKBNm_U6kP9NO8umFqwoHVFFYy7ZnPPnBEWWxBGPRupWiuPnveMNlzhEGnlGpUqV9NGY1PBiyMXPK5B33vYXbjqF5tdjhaAOFEPLtOXOSc2dQbzLDnUqIcmHvxP3DUNoWQxWRXRozKjiCMEdrS2UzdeA6LJiMQduZ-wv12lMDgx6mwVvd_a7uc_skEaHr39uBXrMSH88P5QfdQm_VN3KeoFp8CFpl2A2n0rgaB3_W7kAbMUw4ij4oRKu_8_ozCSi4f1xckV9sKteblX3zXYRBLDWZ3HfKKLLooO3k9sMyuwEHN51Er0IbhF3MFWTEIJTQAe4VCzNx3hwmrJt2t_Lts9lOVARdyJW-aucbZlzHMkv36HQx_eFA8cH1UFdY9U2vhmr8WPN_yKNDNZpE_0pX6lJgOHjUgPydCPGGcFYUk7UK1ROGZPkGSovnpBGbjX3PWgx99aJ6m6R-jYYUQng0-N01lMQXUmD6gRsD7k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dcfc0ede1.mp4?token=qzsIzbKxqPFm5O7QLTvKTe7L2sK6v5pmCiRsub6Wgf5aB1CFdCi3S5y4EukswFnHLOtg-AwJWjjv3x9EBIUBKv3opCX_TrtAMtSotzpZANgznFYoH2sg_xMip2gwvoHgLGspuhm9faEDvuRTTHxSQuS1pbji9jj5kOeT0PTpJ9OP_QGVPRa8CnDkh_peC94d04BqjKBNm_U6kP9NO8umFqwoHVFFYy7ZnPPnBEWWxBGPRupWiuPnveMNlzhEGnlGpUqV9NGY1PBiyMXPK5B33vYXbjqF5tdjhaAOFEPLtOXOSc2dQbzLDnUqIcmHvxP3DUNoWQxWRXRozKjiCMEdrS2UzdeA6LJiMQduZ-wv12lMDgx6mwVvd_a7uc_skEaHr39uBXrMSH88P5QfdQm_VN3KeoFp8CFpl2A2n0rgaB3_W7kAbMUw4ij4oRKu_8_ozCSi4f1xckV9sKteblX3zXYRBLDWZ3HfKKLLooO3k9sMyuwEHN51Er0IbhF3MFWTEIJTQAe4VCzNx3hwmrJt2t_Lts9lOVARdyJW-aucbZlzHMkv36HQx_eFA8cH1UFdY9U2vhmr8WPN_yKNDNZpE_0pX6lJgOHjUgPydCPGGcFYUk7UK1ROGZPkGSovnpBGbjX3PWgx99aJ6m6R-jYYUQng0-N01lMQXUmD6gRsD7k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فقط همین خبر آرام جان مضطر شد؛ پدر که رفت پسر جانشین و رهبر شد
🔹
شعرخوانی امشب محمدرضا طاهری در مصلای تهران.
@Farsna</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/446796" target="_blank">📅 21:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446795">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de484748bc.mp4?token=JWA2hy_h_VrD3uD5qfJI7aPD5g3GMyoylZ6yeaJiRFkN1MITq0fvvDurfWDd9-ZR0CdjhSNbDQBbTNg8p_80tEULLHuHGIB0hEFVe8mAmgk8JoC-c-A0jZhlPXJdRK0mSGoRc7s8-jxewFPjaI2-vaHdjzer6YzmIysHnFn85e4iCLVYsMjV2kAn5ZcebnfpYXXPjRks8HJg4_QB8LKlaFnfoYSbktfdflvn1RUj9fc_u_gnnWxo5HdxNyqQ-IcXADzW67o8XSLRVYw3PZtKt99aRXEBeQJPW1QWwEYcdoflFR0ReehLR7ZwMkOfUk-xyOcQiH_KfjOmqptRRLDvig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de484748bc.mp4?token=JWA2hy_h_VrD3uD5qfJI7aPD5g3GMyoylZ6yeaJiRFkN1MITq0fvvDurfWDd9-ZR0CdjhSNbDQBbTNg8p_80tEULLHuHGIB0hEFVe8mAmgk8JoC-c-A0jZhlPXJdRK0mSGoRc7s8-jxewFPjaI2-vaHdjzer6YzmIysHnFn85e4iCLVYsMjV2kAn5ZcebnfpYXXPjRks8HJg4_QB8LKlaFnfoYSbktfdflvn1RUj9fc_u_gnnWxo5HdxNyqQ-IcXADzW67o8XSLRVYw3PZtKt99aRXEBeQJPW1QWwEYcdoflFR0ReehLR7ZwMkOfUk-xyOcQiH_KfjOmqptRRLDvig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایی از حضور باشکوه مردم در مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/446795" target="_blank">📅 21:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446794">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e8c0f03e5.mp4?token=UT_bb6poMy7NFDY8GTPz7paux7BH0v7Frzd1FMU7uk1L_SxmToXUcmyiaDujpjwvWKwuhCQeUaztivBD3xjGM7Z7HKBz2SOJVDEbQITvmXmdlJ9vSTSfq1CyD6UhGmQiLd_t7sknK6s-C-FhXZvVnorQiM6ZFMZtp1E4muQjzc67r8iLMxvL_gfOI-5J8FD2-GS7wvuBanRudx_isoyfFOytpdA42WYUqnbNH0EEWLo2XwVihnq-bH_SG9ttAPoKa6zYXAsy_LhoM2nBUgCEirrni0UbBik33Bs67p0JjNgvyNo4edU-3l18xohpRwDlOZ5trF5eBfEoG9dPt_Zziw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e8c0f03e5.mp4?token=UT_bb6poMy7NFDY8GTPz7paux7BH0v7Frzd1FMU7uk1L_SxmToXUcmyiaDujpjwvWKwuhCQeUaztivBD3xjGM7Z7HKBz2SOJVDEbQITvmXmdlJ9vSTSfq1CyD6UhGmQiLd_t7sknK6s-C-FhXZvVnorQiM6ZFMZtp1E4muQjzc67r8iLMxvL_gfOI-5J8FD2-GS7wvuBanRudx_isoyfFOytpdA42WYUqnbNH0EEWLo2XwVihnq-bH_SG9ttAPoKa6zYXAsy_LhoM2nBUgCEirrni0UbBik33Bs67p0JjNgvyNo4edU-3l18xohpRwDlOZ5trF5eBfEoG9dPt_Zziw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پخش صدای دل‌نشین قائد امت
و گریهٔ مردم
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/446794" target="_blank">📅 21:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446789">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcDhE1tpALIxVii9Ww-2pugHFexTx1ziqiq3FYnUef0uFgvh0ymgrv5gryAnYH1ogkO6hjMSZ7TRI5JwGYU8Bzvz-m39G8r1tJrmYmNXduM4GMi3BqnRN87IoMnyBv49vb-MGVygwjpflD6aBu9fuFCpSBNZxvzVdIRDIDnKrp6Vfg00rTQ_1XWzdSVEyEQor2VrEICCs6Fxf0-MIsj5JTZqMdIS_7koeIL3FlJ5llfn_g4UcdOSIl0_cN8Zec-p2zy3NYClxao4_aVppYMumwcXo76TcU8X6Me6F_u-sfVrdrU3jE81NIodHZ7iIAh6K93dU8bBPJ6cet1i0MkRwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YipwaviyE50WK_ectPhUCSZkR2KlsY1bqJuj_IZ02AKzUiwMT7dshh4V-RtgD_jFi5A6kxTjcDYbPRmQ9O_wqSNN3aGKOQe-o9esIjudDcingL0XVFNEbe0FvgnsvSL3FifFhmwWMi1QtBc-FVOXI870Pi9UXXqJhCUrgUDt6nmpu6sn0UZWUYjR9TJLHIKr17BiAI6bRj90VpQvy6A4IwSRIyG2_PZkbiNJ4xOxunI8yh14Jgla0ZuRpLGspSzDbCh2UhNA6dWrCu8BCR-LCFc0w_Wf0zQff-oWqYEeAckJsJZbktffspyUokLv_enYi3XjbmseKDfNrX2_BuIWIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pvViTeiJn4qutlZG09M29EEuk2M2VAKwdGG6Ha6wr_30jp5v6irOcKAyAbw1NLZXREUlEII3aJjaNzIXQ1a4u_QV15b9X2G5OVNLs5XCg94lvj502FmQNxiRov5IyC6HPsHi9dJS9ZXeHXbAKBCxyaZ4-AUt-r4Ge5H0lY67I3s-BAjm7Vj5NY0fDsrbqPRMFDKcu-PvV1RFZOA_fIMzu5XzaRWSaVcAAIc2WrzbPgqnlzOaF375DpS-Vbx58LGdh526Q3sMfLeSEQhmoGBCxoAtC0Qpcxu4LpeDk8auMX5x0jkbqxaTT-u6AZY0R2rmW_QffE70-t-hjrXJ8QKrLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iImp_dI_6fSqbhG7ogpi67W-7WctoFJNfFiYMtnsi4FwEk1heoLZ_Z7_F3dK72B4XdYxwtCyb9L9pPExNs7JZLyrlPXjQ80wm2eb6W2wpg3cPEoq_sU9_U0yRte-lcoV7bevNR06eXlBHJvY2zQ33m1TXQYARw74az4rrE2BpL1jFlNC5IWUEQulmeOzhX3vNxsrj6tslOTcfvuRCWh95Hc40tAglA6y64fBB05WoQqMmKGxHqxt2vfdMm5iVzjSz7hcu2g5NIhFCT4KO7Pkm2MhuzQTNH06nwQeQPSfRRAdR_EAPBDPMiPI28afanIOdYFlyv7XmLf1AsYKCFn4jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rPuH3BiwrA2SS20PicfcrHIE0olN0rfDMkOJ2sD6JkPXCLfmKhmiLxx5H5EseADyeEvjpb79WMrdN5PyLtuKWxvPi4cZVxoZHRKECgVcNbUkFU8znrjSgN9pqImzBgff-SD3hQC-y3Oc9GvfGYLGyyWzF0Pv5zR7-OrfdkYsq954wm-TdTKL8vrchTxjBGeAvAOgDCvpbGrmckFRCpIoBwvckUMyJ2UL90q4RnE-1T3cPPQzr2Pna49mpwq7NI9AXQpv7iVFVFVFgGBe_XMWb3J_vnumP_Y9x9HXUSZYWFDTN9ZRMRM0wGREeIwAt9R6PSY4Fv-u07wKRQRiAvQWOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر خبرگزاری الجزیره از روز اول مراسم وداع با رهبر شهید در تهران
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/446789" target="_blank">📅 21:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446788">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔰
موکب خدمت در مسیر «آخرین دیدار»
🔻
موکب شهدای وزارت صنعت، معدن و تجارت برای خدمت‌رسانی به شرکت‌کنندگان در مراسم بدرقه و وداع با رهبر شهید انقلاب اسلامی، با همراهی شرکت ملی صنایع مس ایران برپا شده است.
جمعه ۱۲ تیرماه ۱۴۰۵، وزیر صنعت، معدن و تجارت به‌همراه مدیرعامل شرکت ملی صنایع مس ایران و جمعی از مدیران حوزه صنعت و معدن، از این پایگاه خدمت‌رسانی بازدید کرده و در جریان روند آماده‌سازی برای میزبانی از مردم قرار گرفتند.
🔹
این موکب در روزهای پیشِ‌رو در حوالی میدان ولی‌عصر(عج) تهران، برپا خواهد بود.
◀
️ لینک خبر در مس‌پرس
@mespress_ir</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/446788" target="_blank">📅 21:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446787">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGguYkqIHGxN1n3OrepGcMW9SObEH2JoC8zEOS9pR6tTzCyLhicLENppPK92WcjxpBpPGtu1IoKMDFnHYEjnIATh7WQ0Y2K3CnkA2Gf9PNnx-jTv6MGZ-qhmz34OQyKf1xVUUV84kI4mZFdXqYGccnwU4IP6Ikmz4YWI9O_jULKO73SwphM9j7xITIT445VKB9oe3dISyKseOgtqAfDgty76C2ZmKI-GtCUKGulQq5mujwGi5_nC5QLNJm8DvdJIJLSima5VslbqEczp-9lXzPhohCjhenRgQpgyQtO_wOkecJJpwBBdrwcdaKrXhi_vax8NcOT7ws-HQFPhlTrK0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/446787" target="_blank">📅 21:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446786">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/446786" target="_blank">📅 20:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446785">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/117b776f6d.mp4?token=HOHObq32y3zy5XVjrKHVjYCTtX-8SrCpOEg7JN_51F-jo_Ngf2SlPFj8zdZzXPjUQU7pmbwh9NY6qsSdF9xYap9Ji5rozQtc8CwW7pRd07AN4K5T3rEyYmBjI9YcJKLCMwzPolUNWwlgj7uM9NaDuOWX-PTKRUfeP3AqhVXLMQvCoVMF5dI_MqsLmpGeCdOLf63vxVM_9kMXwmogfr2xqiKsQrUByuzIShBUobk56Jify_BjHxjjk61EEn1TuEVO8FjVna0ufx_-RhSxbXchIggyHDBwjwOzSNKQa7wgnJfbsAScEwsRexbvFdKcJh1ACg_fe2Rwu9iyC58NutTZ_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/117b776f6d.mp4?token=HOHObq32y3zy5XVjrKHVjYCTtX-8SrCpOEg7JN_51F-jo_Ngf2SlPFj8zdZzXPjUQU7pmbwh9NY6qsSdF9xYap9Ji5rozQtc8CwW7pRd07AN4K5T3rEyYmBjI9YcJKLCMwzPolUNWwlgj7uM9NaDuOWX-PTKRUfeP3AqhVXLMQvCoVMF5dI_MqsLmpGeCdOLf63vxVM_9kMXwmogfr2xqiKsQrUByuzIShBUobk56Jify_BjHxjjk61EEn1TuEVO8FjVna0ufx_-RhSxbXchIggyHDBwjwOzSNKQa7wgnJfbsAScEwsRexbvFdKcJh1ACg_fe2Rwu9iyC58NutTZ_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
احترام نظامی مردم هنگام پخش سرود ملی
@Farsna</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/446785" target="_blank">📅 20:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446782">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApjDbfpYGoAU9xKiRecgCwNLhobsMCt8PigiEJYNjQ1S8CoSU32pTAIZ_sj_JxPrJJmjsNxR4KyM6wnIBVpOATDNMiIlANeTh_0Np194NqUzpVY643i63rOtBlJLh4wQPBHC_Iq1k_s5bw6hFkjIS0WdWTwZbMiTA7sCbj64pAc23VVbDl7tUKjstzYSACIU3wCdM2xatBuge__yjBH5YkhoL__eHAacGM4HgiwcRJuSc5mg-YgdnaKqDKNc1xJ4iN-qxKnDXEyoBO83FTQYXGYkkShOsZ_T3agSMUO0x8ubS6ugxdEWQcBPycmYaMN27Xfy6NCZHpz7Wj0HJICpXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: از دیدن گریه مردم ایران در تشییع [آیت‌الله] خامنه‌ای غافلگیر شدم؛ چراکه فکر می‌کردم مردم از او متنفر هستند.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/446782" target="_blank">📅 20:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446781">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea15c58a8a.mp4?token=F9c3p6LjuGydDxXqcJJyJi-bcv-06O-0MQwsxqUBiMB_koF9wQGHxzfuKmKhyj-eafBYOnOJcijai6yY27GEtXDesGDaE0zxXDqmwI5RBm7atF1jhM5K2qge8whmOSaV6TDg0laSJW4m8QbKO3q3STJD2WTSHB1wIwOOfWKDuZUOIEWYjLEaZJ-hIm2B1ueSX-wFnJxu1kMzq7ZU0FezKMz0nSEN7VsEuz-T1hwrdts-WOC8oxSywTyay5kGa11lC50QtldZ-OOrULq1s7hCiw-7NHrdl_aQi6wcqVvGvlrXIIipZGJ6eK8OEhlo2gQRhrJUQEaO9AZcnlSKfe50ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea15c58a8a.mp4?token=F9c3p6LjuGydDxXqcJJyJi-bcv-06O-0MQwsxqUBiMB_koF9wQGHxzfuKmKhyj-eafBYOnOJcijai6yY27GEtXDesGDaE0zxXDqmwI5RBm7atF1jhM5K2qge8whmOSaV6TDg0laSJW4m8QbKO3q3STJD2WTSHB1wIwOOfWKDuZUOIEWYjLEaZJ-hIm2B1ueSX-wFnJxu1kMzq7ZU0FezKMz0nSEN7VsEuz-T1hwrdts-WOC8oxSywTyay5kGa11lC50QtldZ-OOrULq1s7hCiw-7NHrdl_aQi6wcqVvGvlrXIIipZGJ6eK8OEhlo2gQRhrJUQEaO9AZcnlSKfe50ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گریه بی‌امان دخترکی که با ویلچر خودش را به وداع رهبر شهید رساند  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/446781" target="_blank">📅 20:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446780">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc2bd6befd.mp4?token=R_mPEPmCMxthIvUnNbDo7GfPA0m1OdaA6SrJyK-A3t4VrsJaXSEowNMgY0hzy2Hby31igzZRQwdsa_sZV8spO_DFDpYkOXP2jBS292kkcnS1i02se6b568u87cHDEzeHimifFGLP9s14VUBLGKNYS4rCOfR148EvhYuzu_VQ_rJG8pFNxZncFl4rrgaLRtpJh695gavjQ1aBeI4j6iDaC3hWx-nEHDr8-eJOXzeHS9k6OKzd_i78NrWsqEhWRlKf8M5r_sX8lGgi9z6gGnY7WxXBd_xytj4srHUa-qRVxr3WgDeCSZd6NvaXpHKsGf7CTPJwY2SAkybastwvng9A0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc2bd6befd.mp4?token=R_mPEPmCMxthIvUnNbDo7GfPA0m1OdaA6SrJyK-A3t4VrsJaXSEowNMgY0hzy2Hby31igzZRQwdsa_sZV8spO_DFDpYkOXP2jBS292kkcnS1i02se6b568u87cHDEzeHimifFGLP9s14VUBLGKNYS4rCOfR148EvhYuzu_VQ_rJG8pFNxZncFl4rrgaLRtpJh695gavjQ1aBeI4j6iDaC3hWx-nEHDr8-eJOXzeHS9k6OKzd_i78NrWsqEhWRlKf8M5r_sX8lGgi9z6gGnY7WxXBd_xytj4srHUa-qRVxr3WgDeCSZd6NvaXpHKsGf7CTPJwY2SAkybastwvng9A0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آقامیری: مردم با حضور در مراسم تشییع، غیرت و شرافت و هویتشان را سر دست می‌گیرند.  @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/446780" target="_blank">📅 20:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446779">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfef33bb16.mp4?token=DM7UjanzTNkcIJRBiWPdpe6x-j_PtENHoZiABrllF6yItl1-PswT0sH4AUBQfovJlB95fIlbxYBVvZE219_HsVb7xINlXOVlkMzuoCTb3hUb3_T5tUV-Su1N4oy2moY2CJw0ERUXY1BwP2x7KsFDatW1BugKp5q1AHsTlen-JgjE9gJu6dvdZ40-EqZjNk-Ny1t-StQsZ8JnreeftP4v8Ptp5bKadzkjaYMUWJw75bV8CmmYhUMIRgGso0626UmW7wA1854UIYyxIDNJMmyxvQ6TJ3hVZIOUMJ-IJ2YpJhTffKBwOMSIJeEor2wKmvsUOiQG5NHj24qCHR_TAiFqpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfef33bb16.mp4?token=DM7UjanzTNkcIJRBiWPdpe6x-j_PtENHoZiABrllF6yItl1-PswT0sH4AUBQfovJlB95fIlbxYBVvZE219_HsVb7xINlXOVlkMzuoCTb3hUb3_T5tUV-Su1N4oy2moY2CJw0ERUXY1BwP2x7KsFDatW1BugKp5q1AHsTlen-JgjE9gJu6dvdZ40-EqZjNk-Ny1t-StQsZ8JnreeftP4v8Ptp5bKadzkjaYMUWJw75bV8CmmYhUMIRgGso0626UmW7wA1854UIYyxIDNJMmyxvQ6TJ3hVZIOUMJ-IJ2YpJhTffKBwOMSIJeEor2wKmvsUOiQG5NHj24qCHR_TAiFqpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آقامیری: مردم با حضور در مراسم تشییع، غیرت و شرافت و هویتشان را سر دست می‌گیرند
.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/446779" target="_blank">📅 20:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446778">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e2c32acf1.mp4?token=MU6ur9NHrVUk0P1-6uz8ht1O9JF1kC3UzorJdSB-BMgj4bjMTWi9U80Gs02kvwfWbzqyFuFQ0RK2Wwl0WYniJmcXkBlaAfCaAGope6sYQ9C08tX0Yn-7YG8Eb6YwvOHfd19tiRwTEJ6pPt5XEOTdT-PJOBvNEF-eYbXBAMYzaAlZ4vAzlVE5slWJokiVO5ytzthgDaNlGQjWm_1G2PyrpN-ePCS4mvMWXyfxbmDwHWOipz0iZFTXYQAkas5RcPdawPAre779n_D-F557p-19AB6VFZ3ZPqplnXH8jy4b2EEAqcGzi5JjGKJ3KI_wQ9OnQejGoYU3bwoAnm6_g72hBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e2c32acf1.mp4?token=MU6ur9NHrVUk0P1-6uz8ht1O9JF1kC3UzorJdSB-BMgj4bjMTWi9U80Gs02kvwfWbzqyFuFQ0RK2Wwl0WYniJmcXkBlaAfCaAGope6sYQ9C08tX0Yn-7YG8Eb6YwvOHfd19tiRwTEJ6pPt5XEOTdT-PJOBvNEF-eYbXBAMYzaAlZ4vAzlVE5slWJokiVO5ytzthgDaNlGQjWm_1G2PyrpN-ePCS4mvMWXyfxbmDwHWOipz0iZFTXYQAkas5RcPdawPAre779n_D-F557p-19AB6VFZ3ZPqplnXH8jy4b2EEAqcGzi5JjGKJ3KI_wQ9OnQejGoYU3bwoAnm6_g72hBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زیارت به نیابت ۱۶۸ شهید دانش آموز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/446778" target="_blank">📅 20:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446777">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3AITPwbjTHCxgrd9uFYHzGJUC_lFT4sy3f95nOhqwq1h-IOm7lwQcv3YdC6GbPaqDGMPoMVWDWDJpEdVXLxbAk771riEb1bJRPVUSqMlRwLBGhtQpnZGjkx-Rv7yJqySLKHLPfVhZ-_lW-ReHLxOoQv3PkoIEkEN-DkecOztgTrihfDrdsYO0AuVho4yDVZ6TjiKVxMFng4AmYYjqwNJhHhMdWC3rq_qchZ21OhPoYrulcbMnuIg2jPv8ZBu2dIMh4tjL40Bd1k0HT2M7go1geJNx4JVGm4PqZUhmDNpGoYCSoglV-75RMcBhTnH-CSROpmbCoJuqTEbrHQH3cPQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخاب جالب آیات قرآن در مراسم وداع خارجی‌ها با امام شهید
🔹
در عرف دیپلماتیک جهان، مراسم استقبال و بدرقه سران کشورها معمولاً با تشریفات نظامی، نواختن سرود ملی، احترام نظامی و قرائت پیام‌های رسمی برگزار می‌شود. اما در مراسم وداع هیأت‌های خارجی با پیکر رهبر شهید انقلاب، این قواعد با هویت اسلامی جمهوری اسلامی درهم آمیخت.
عراق؛ استقلال سیاسی و فکری با جلوگیری از نفوذ جریان نفاق
🔸
برای هیأت شیوخ عشایر عراق، نخستین آیه سوره احزاب انتخاب شد؛ آیه‌ای که پیامبر اکرم(ص) را به تقوا و پرهیز از اطاعت کافران و منافقان فرا می‌خواند.«يَا أَيُّهَا النَّبِيُّ اتَّقِ اللَّهَ وَلَا تُطِعِ الْكَافِرِينَ وَالْمُنَافِقِينَ ۗ إِنَّ اللَّهَ كَانَ عَلِيمًا حَكِيمًا، ای پیامبر! از خدا پروا کن و از کافران و منافقان اطاعت مکن؛ همانا خداوند دانا و حکیم است.»
ترکیه؛ فضیلت بالای جهاد با جان و مال
🔹
برای هیأت ترکیه، آیه ۹۵ سوره نساء قرائت شد، آیه‌ای که مجاهدان را بر قاعدان برتری می‌دهد.«لَا يَسْتَوِي الْقَاعِدُونَ مِنَ الْمُؤْمِنِينَ غَيْرُ أُولِي الضَّرَرِ وَالْمُجَاهِدُونَ فِي سَبِيلِ اللَّهِ بِأَمْوَالِهِمْ وَأَنْفُسِهِمْ ۚ فَضَّلَ اللَّهُ الْمُجَاهِدِينَ بِأَمْوَالِهِمْ وَأَنْفُسِهِمْ عَلَى الْقَاعِدِينَ دَرَجَةً ۚ وَكُلًّا وَعَدَ اللَّهُ الْحُسْنَىٰ ۚ وَفَضَّلَ اللَّهُ الْمُجَاهِدِينَ عَلَى الْقَاعِدِينَ أَجْرًا عَظِيمًا، مؤمنانی که بدون عذر از جهاد بازنشسته‌اند، با مجاهدانی که با مال و جان خود در راه خدا جهاد می‌کنند، یکسان نیستند. خداوند مجاهدان را که با مال و جان خود جهاد می‌کنند، بر خانه‌نشینان برتری داده است؛ هرچند خداوند به همه وعده نیکو داده، ولی مجاهدان را بر خانه‌نشینان با پاداشی بزرگ برتری بخشیده است.»
عربستان؛ یادآوری سنت الهی در پیروزی مؤمنان
🔸
برای هیأت عربستان سعودی، آیه ۱۳ سوره آل‌عمران تلاوت شد، آیه‌ای که به نبرد بدر اشاره می‌کند، جایی که مؤمنان اندک، با وجود برتری ظاهری دشمن، به یاری خدا پیروز شدند.«قَدْ كَانَ لَكُمْ آيَةٌ فِي فِئَتَيْنِ الْتَقَتَا ۖ فِئَةٌ تُقَاتِلُ فِي سَبِيلِ اللَّهِ وَأُخْرَىٰ كَافِرَةٌ يَرَوْنَهُمْ مِثْلَيْهِمْ رَأْيَ الْعَيْنِ ۚ وَاللَّهُ يُؤَيِّدُ بِنَصْرِهِ مَنْ يَشَاءُ ۗ إِنَّ فِي ذَٰلِكَ لَعِبْرَةً لِأُولِي الْأَبْصَارِ، بی‌تردید در رویارویی آن دو گروه، برای شما نشانه‌ای بود؛ گروهی که در راه خدا می‌جنگید و گروهی دیگر که کافر بود. آنان مؤمنان را با چشم خود دو برابر می‌دیدند، و خدا هر که را بخواهد با یاری خویش تأیید می‌کند. بی‌گمان در این ماجرا عبرتی برای صاحبان بینش است.»
لبنان؛ ایمان در میدان آزمون
🔹
برای هیأت دولت لبنان، آیه ۶۶ سوره نساء انتخاب شد؛ آیه‌ای که می‌گوید اگر فرمان‌های بسیار دشوار الهی صادر می‌شد، تنها گروه اندکی از مردم از آن پیروی می‌کردند.«وَلَوْ أَنَّا كَتَبْنَا عَلَيْهِمْ أَنِ اقْتُلُوا أَنْفُسَكُمْ أَوِ اخْرُجُوا مِنْ دِيَارِكُمْ مَا فَعَلُوهُ إِلَّا قَلِيلٌ مِنْهُمْ ۖ وَلَوْ أَنَّهُمْ فَعَلُوا مَا يُوعَظُونَ بِهِ لَكَانَ خَيْرًا لَهُمْ وَأَشَدَّ تَثْبِيتًا، و اگر بر آنان مقرر می‌کردیم که خود را بکشید یا از سرزمین‌های خود بیرون بروید، جز گروه اندکی از آنان چنین نمی‌کردند. و اگر آنچه را به آن اندرز داده می‌شدند انجام می‌دادند، برایشان بهتر بود و آنان را استوارتر می‌ساخت.»
حزب‌الله؛ ولایت، ستون پیروزی
🔸
برای هیأت حزب‌الله، آیات ۵۵ و ۵۶ سوره مائده تلاوت شد، آیاتی که ولایت خدا، پیامبر و مؤمنان را محور تشکیل «حزب‌الله» معرفی می‌کند.«إِنَّمَا وَلِيُّكُمُ اللَّهُ وَرَسُولُهُ وَالَّذِينَ آمَنُوا الَّذِينَ يُقِيمُونَ الصَّلَاةَ وَيُؤْتُونَ الزَّكَاةَ وَهُمْ رَاكِعُونَ(۵۵) وَمَنْ يَتَوَلَّ اللَّهَ وَرَسُولَهُ وَالَّذِينَ آمَنُوا فَإِنَّ حِزْبَ اللَّهِ هُمُ الْغَالِبُونَ»(۵۶) «سرپرست و ولی شما تنها خدا و پیامبر او و مؤمنانی هستند که نماز را برپا می‌دارند و در حال رکوع زکات می‌دهند.(۵۵) و هر کس خدا و پیامبر او و مؤمنان را به ولایت بپذیرد، بداند که حزب خدا همان پیروزانند.(۵۶)»
حماس؛ وفاداری تا آخرین نفس
🔹
برای هیأت جنبش حماس، آیه ۲۳ سوره احزاب انتخاب شد، آیه‌ای که از مردانی سخن می‌گوید که بر عهد خود با خدا صادق ماندند، برخی به شهادت رسیدند و برخی همچنان در انتظارند.«مِنَ الْمُؤْمِنِينَ رِجَالٌ صَدَقُوا مَا عَاهَدُوا اللَّهَ عَلَيْهِ ۖ فَمِنْهُمْ مَنْ قَضَىٰ نَحْبَهُ وَمِنْهُمْ مَنْ يَنْتَظِرُ ۖ وَمَا بَدَّلُوا تَبْدِيلًا در میان مؤمنان، مردانی هستند که به پیمانی که با خدا بسته‌اند صادقانه وفا کرده‌اند برخی از آنان به عهد خود جامه عمل پوشانده‌اند و برخی دیگر در انتظارند و هرگز پیمان خود را دگرگون نکرده‌اند.
عکس: محمدمهدی پورعرب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/446777" target="_blank">📅 20:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446776">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a1aaf91df.mp4?token=ZZU4ZFTMqy3DBbO64BntgchbPCM95NI8mSJzHX9ERWPh6rJEvBzfXAPFGLPyTcdaqPN_z0YviH7PMfV9FU94MmpxCqKbPSWzcV-2Esn1BloYf6OW-qXsKZEztsOq_c3VIWXdBz8-9ZEwFR3OMdo3jYfbs8zXBMADniIx5s7ITqCncsOVOJ7hgKFT3yq3QM3a3tBhIt4LVlwx46nHoGP6F3E-yKNlW-gm7JEtdg26OfSI3Ly11_uxQ6gBYVWL5hbw42F6v74dyInJG7YKdRJoNs83zNqvBhQCatWKQ3mEm6UzEFFlUnwLO6SiudwAxp32rDN1P_zIdJMpHW6XRa_Q5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a1aaf91df.mp4?token=ZZU4ZFTMqy3DBbO64BntgchbPCM95NI8mSJzHX9ERWPh6rJEvBzfXAPFGLPyTcdaqPN_z0YviH7PMfV9FU94MmpxCqKbPSWzcV-2Esn1BloYf6OW-qXsKZEztsOq_c3VIWXdBz8-9ZEwFR3OMdo3jYfbs8zXBMADniIx5s7ITqCncsOVOJ7hgKFT3yq3QM3a3tBhIt4LVlwx46nHoGP6F3E-yKNlW-gm7JEtdg26OfSI3Ly11_uxQ6gBYVWL5hbw42F6v74dyInJG7YKdRJoNs83zNqvBhQCatWKQ3mEm6UzEFFlUnwLO6SiudwAxp32rDN1P_zIdJMpHW6XRa_Q5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظات ملکوتی اذان مغرب در مصلی امام خمینی تهران
@Frans
-
Link</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/446776" target="_blank">📅 20:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446775">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0dcad2aae.mp4?token=qqvyv7_uwjJVf9MCEC3FIf6JIq4PxVr-KSrDPPbkRbIMiNVQM00Gh1mdOaogFO5u2VnHgijTTzVXzxSsoYaPGzFaSIDQKNxvs2dJUaEy7d3TKCtp4HlE_gtOfALkRYrVNuMk26TNKEm7giNvo6AiMmxDe1jnUSAjyuImICjzapqTqWpls329PapL5cRgP9AKj3bt-LS9sRGyTxXZN0jvqnIM_ZM8TGLswrf2fXAac5I2FRTn1v4pq_f2UiBbW4FWVmJSOkbiPE5wxarnU7YDfGSFTLgNtv-OSD5fiDU3ZMBNLTEt0DBJCRUXiJwttoiRrDvmMbm8WAERbg9LQZpqcQxOwDnhGMoADUsVcF5cfe33fTjed12fgoLQskhkMcpYWbBTJYt2JMPYhx4JO8Rvzy68A5QDDaPktPEld20xa5cN9u22nTvny0JJFfp153pBHPwZnhp5D7PxO0wkybdoCwshiuAdATFuIOoTVrFuPPzapPhApPyOSnSE-qZ8Og2fUqy81bRFJLTLQ7QU6hfpdrRVophodZ3rbUJMmcmqyc_vCCleiwJ-2s381NLmEopww_A8YLcXPX8sfxIhV7y1RlJ-Ls_ibtfx7x3_M8Cm6CQzryf1pbIqMagdN6JccClbXvyEX6h3xRA1xU5pl4GKFoJnU1KPA_N7-E4kRAk5mJ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0dcad2aae.mp4?token=qqvyv7_uwjJVf9MCEC3FIf6JIq4PxVr-KSrDPPbkRbIMiNVQM00Gh1mdOaogFO5u2VnHgijTTzVXzxSsoYaPGzFaSIDQKNxvs2dJUaEy7d3TKCtp4HlE_gtOfALkRYrVNuMk26TNKEm7giNvo6AiMmxDe1jnUSAjyuImICjzapqTqWpls329PapL5cRgP9AKj3bt-LS9sRGyTxXZN0jvqnIM_ZM8TGLswrf2fXAac5I2FRTn1v4pq_f2UiBbW4FWVmJSOkbiPE5wxarnU7YDfGSFTLgNtv-OSD5fiDU3ZMBNLTEt0DBJCRUXiJwttoiRrDvmMbm8WAERbg9LQZpqcQxOwDnhGMoADUsVcF5cfe33fTjed12fgoLQskhkMcpYWbBTJYt2JMPYhx4JO8Rvzy68A5QDDaPktPEld20xa5cN9u22nTvny0JJFfp153pBHPwZnhp5D7PxO0wkybdoCwshiuAdATFuIOoTVrFuPPzapPhApPyOSnSE-qZ8Og2fUqy81bRFJLTLQ7QU6hfpdrRVophodZ3rbUJMmcmqyc_vCCleiwJ-2s381NLmEopww_A8YLcXPX8sfxIhV7y1RlJ-Ls_ibtfx7x3_M8Cm6CQzryf1pbIqMagdN6JccClbXvyEX6h3xRA1xU5pl4GKFoJnU1KPA_N7-E4kRAk5mJ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیرکل جنبش جهاد اسلامی فلسطین: شهید آیت‌الله خامنه‌ای رهبری متمایز بودند که به موضوع فلسطین عشق می‌ورزیدند
‌
@Farsna</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/446775" target="_blank">📅 20:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446774">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/368a6b7cba.mp4?token=S0VBuXaRRoHl7jvSlSAe-RJcolRNam7p7qcY-zF0jdf7SbPR7lGtDOCKx06Lt__GVqR9RDy49nCLLT8C0mklvnw6sVbDh7AjLbJS6VNR9s1EHPAIrWX5ckZdezs_Sw26HD8dSq5lZjGp5r0UMfNifAxUupNbSh2GAcbY7FExu5AYOMC3IcADMO7MAEuOMBvNT_UNV_lSJd2fvT-BvvRdRMi1kOxlxA5ENJOjpNT0QIMeFhooDuLEwgRfMIA7pNznBUqdrfTmECEhsuDVW4SFWPqdTmk2IVCTzZ7o_tioLbYb11jR7OB6qOYMxipvWCBObG3IBckVGtq1D1CzTSxetRgONtANEwOhNHUs_RxBT3ShX3vdxzSiyTK0EHK91Xj8T3s-pQ6cHb1DJ-p7NZVj3SdJ4cQP5-g9wlSGajwAAT1o-X-FH12VW7EVz71JVPtLIpxhGhEvDNRCr7B22SU1iJbC3X6jBRhUzW8pN_GQlN-GLz2NhOVrkTnyLl-kkKHgYJp-KNl1PiOzeKLLMmvioOr5ozj11-j0NJ0-Q3ShThzWsyWxPviBahbWTitlQvOMKqxeZKw7xjXwnwfjLC5hcKNF_o_HflLb4PkefFs2iUmIOJ41a4ctKlVQvzFSbWiZOTsHRVqKqInxNfItpkbIHLm5b7636WVBfpQn-3er_HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/368a6b7cba.mp4?token=S0VBuXaRRoHl7jvSlSAe-RJcolRNam7p7qcY-zF0jdf7SbPR7lGtDOCKx06Lt__GVqR9RDy49nCLLT8C0mklvnw6sVbDh7AjLbJS6VNR9s1EHPAIrWX5ckZdezs_Sw26HD8dSq5lZjGp5r0UMfNifAxUupNbSh2GAcbY7FExu5AYOMC3IcADMO7MAEuOMBvNT_UNV_lSJd2fvT-BvvRdRMi1kOxlxA5ENJOjpNT0QIMeFhooDuLEwgRfMIA7pNznBUqdrfTmECEhsuDVW4SFWPqdTmk2IVCTzZ7o_tioLbYb11jR7OB6qOYMxipvWCBObG3IBckVGtq1D1CzTSxetRgONtANEwOhNHUs_RxBT3ShX3vdxzSiyTK0EHK91Xj8T3s-pQ6cHb1DJ-p7NZVj3SdJ4cQP5-g9wlSGajwAAT1o-X-FH12VW7EVz71JVPtLIpxhGhEvDNRCr7B22SU1iJbC3X6jBRhUzW8pN_GQlN-GLz2NhOVrkTnyLl-kkKHgYJp-KNl1PiOzeKLLMmvioOr5ozj11-j0NJ0-Q3ShThzWsyWxPviBahbWTitlQvOMKqxeZKw7xjXwnwfjLC5hcKNF_o_HflLb4PkefFs2iUmIOJ41a4ctKlVQvzFSbWiZOTsHRVqKqInxNfItpkbIHLm5b7636WVBfpQn-3er_HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین حرف شما با رهبر شهید چیست؟
@Farsna</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/446774" target="_blank">📅 20:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446773">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cW5HvJ4En3jw4ftX1gzs_P_j2S8G1P4ReGUdmM6RDhBYad1dv6zh_Kvdf7HcVwEM4q2cpSJMORfnDi_WPiffaYW4b5ABlgXUKaWTwOtYh1MNdxMrNQc0XxEuXRP1vnWbrp5F6xrElfHsh8pnNoupnb5lXvWKjf8fym-3LvNQa-L5T4wRUUpBM0SmEa4TqiWto3qZw5xWj9cQi5RZfouCkUj-6feynKamXdIvMeGqB4HnQv1WtjkJ_odsNxhAU5yC_ZKzzccSgeWtZAOnSoWMNutfpQVsRCEIH50AYV-_IAeuP_jnQHoNn9mGHgys6k2UeELq25IEot8B5LPXh-0Upg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
راه‌نما
@Farsna</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/446773" target="_blank">📅 20:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446772">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d60c9e7d5b.mp4?token=K_iXc5sdqCoXkzIzGPWXBZDtrHMrSs_CQlDSxE7ZbXcPja5rhgI9c2E2CeD2N59BlpH0HcZ5Shp8MQkd9tmKYNwCP7xZGxHZ6KtTvGwyrZ2QjZcjM68eV3FeSGJlojtZxdTRupO45I-Bchz_-KL3fdvgjoK6qwV6TY6kFMqwy06z8s6P5p9O6n3OgdlARiDloohdq8n4Kp_VxM5y3GDJHjXESkcxKBOh5_bqoLyIWpgecsE98GbsUOtPuhSY04ZgTGF9s5tCah0HE_w80UknuADvc-mZKVWA89Kh5W243msI2IV7I9gCVAt_Eo7vSIrMiAvcZIT_U73YAbc4BAUJ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d60c9e7d5b.mp4?token=K_iXc5sdqCoXkzIzGPWXBZDtrHMrSs_CQlDSxE7ZbXcPja5rhgI9c2E2CeD2N59BlpH0HcZ5Shp8MQkd9tmKYNwCP7xZGxHZ6KtTvGwyrZ2QjZcjM68eV3FeSGJlojtZxdTRupO45I-Bchz_-KL3fdvgjoK6qwV6TY6kFMqwy06z8s6P5p9O6n3OgdlARiDloohdq8n4Kp_VxM5y3GDJHjXESkcxKBOh5_bqoLyIWpgecsE98GbsUOtPuhSY04ZgTGF9s5tCah0HE_w80UknuADvc-mZKVWA89Kh5W243msI2IV7I9gCVAt_Eo7vSIrMiAvcZIT_U73YAbc4BAUJ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این پرچم‌ها حرف می‌زنند
@Frans
-
Link</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/446772" target="_blank">📅 19:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446771">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40143b2f69.mp4?token=GXNs-9I7Ssicw7NyJreikJ0Jz210zKl6jC01lP4KfcU_iE7LAOqE-zTrkwIRVY5Dsfrkm7UFHoA0496-ZPjGSs8gsOssWd8H6PYVv6yHaOB04BnQGCeFTbyjfHO9aL7DTPNch0OTPzKg_uavMpWaj4e9HlE5Os2vHa-YAyC73Ar8_RUb2HqtjKgrsKSjReXpR8XeIgVROL8L7UdzYOITj2verNobkQSlN7nepeYGary88dLKuGQ_ekFCDaEx1c7EO1IWlPzONR40uWW6phDjRGSz1qFlq2rR_qgQOCyuqraHOI4D9mnRZRJIxwFmi9mOUpJcSRRcOkyCn1LvgOmVf4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40143b2f69.mp4?token=GXNs-9I7Ssicw7NyJreikJ0Jz210zKl6jC01lP4KfcU_iE7LAOqE-zTrkwIRVY5Dsfrkm7UFHoA0496-ZPjGSs8gsOssWd8H6PYVv6yHaOB04BnQGCeFTbyjfHO9aL7DTPNch0OTPzKg_uavMpWaj4e9HlE5Os2vHa-YAyC73Ar8_RUb2HqtjKgrsKSjReXpR8XeIgVROL8L7UdzYOITj2verNobkQSlN7nepeYGary88dLKuGQ_ekFCDaEx1c7EO1IWlPzONR40uWW6phDjRGSz1qFlq2rR_qgQOCyuqraHOI4D9mnRZRJIxwFmi9mOUpJcSRRcOkyCn1LvgOmVf4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عهد می‌بندم سرباز رهبرم باشم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/446771" target="_blank">📅 19:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446770">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-k9GN00TkpNcHjwaVmVkiHbZQyKLB_nZitQvkzmF8RRWj2jfxUAJbvCLQFjhwaTqJjkk2O6Kv6RPhw5FS8coBrKvFl-0uJOEMmp3Nc2Cx21fqcu1yyvfuGos4dZeebfoGO21MHvwvSg_pJTz0HKu7IjstlSq-U-wkET8MUHaynqrIP92wgJpZgXujADWuhdN0_WktuTWPaEi3NoonpDc7xgs6ilnnXT5LRHGj1Sc5gsybLeXoPFrh0Lqt5J7H8aUwrexowgjo1XgfUYXcy44VXqe4tBS1y-onAnUhTcd5jXUoairV1ghZ0Ncei-u2NxnItnY_TK_tCmJzzdX4qdKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجتماع‌کنندگان میادین امشب به‌سوی مصلای تهران حرکت می‌کنند
🔹
شورای هماهنگی تبلیغات اسلامی: امت وفادار و عزادار ایران اسلامی، در بیعتی دیگر با حضرت آیت‌الله سیدمجتبی خامنه‌ای، پس از برگزاری اجتماعات و آیین‌های شبانه در میادین و نقاط مختلف شهر، در حرکتی باشکوه و سرشار از شور ارادت، به‌سوی مصلای امام خمینی(ره) رهسپار خواهند شد تا در آیین وداع با قائد شهید امت شرکت کنند.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/446770" target="_blank">📅 19:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446769">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60781e76a6.mp4?token=TV9T84VLJZuK1qtxrJh-8zpYQe7LpFIgFcN4B_A-_XFo-suq3qQml7e_5iT7TkDYTWt85B_J5KqVFCZEEQsqGkkCvVmFTAxVcZ1nItSqYodU6gQkesyde2cE4YFTQ-6todbaVVL7VdkVHdBEWuect6_8UlVfyQVaaixP08yQJ841gOdB662Eo51QzXWIDv29OCu8G9F9xuvaew2Nhk-DHGO5HxoUxf2wg4hyOXNYvo1Oy4rYdTE_P1HlzevJqzEwBdCWP2NTr0WcVzKIriWKss4EHGoKJrJ9TfLtPQZgzqJWwjiCX0UEOc9TTxYElVdo9j31rULm1mLhsEB60q1UHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60781e76a6.mp4?token=TV9T84VLJZuK1qtxrJh-8zpYQe7LpFIgFcN4B_A-_XFo-suq3qQml7e_5iT7TkDYTWt85B_J5KqVFCZEEQsqGkkCvVmFTAxVcZ1nItSqYodU6gQkesyde2cE4YFTQ-6todbaVVL7VdkVHdBEWuect6_8UlVfyQVaaixP08yQJ841gOdB662Eo51QzXWIDv29OCu8G9F9xuvaew2Nhk-DHGO5HxoUxf2wg4hyOXNYvo1Oy4rYdTE_P1HlzevJqzEwBdCWP2NTr0WcVzKIriWKss4EHGoKJrJ9TfLtPQZgzqJWwjiCX0UEOc9TTxYElVdo9j31rULm1mLhsEB60q1UHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای مصلی در حضور عاشقان رهبر شهید در هنگام غروب آفتاب
@Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/446769" target="_blank">📅 19:50 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
