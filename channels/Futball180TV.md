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
<img src="https://cdn5.telesco.pe/file/K6A6FklcQdvUyDXl4teUjVznMqMGXQmSQjOao1di-qatbIz8PTQdis-hhs-ZOrkoeELgBBHxrjA12DVbCS7bwC299Fn7mfxOtVSl1PkinekO5VmaEeaiT7ZkfqOsT8vkggulucVVNYL0fJ8xgr7eHlyRVTmmWEMGq4bFe_ATH39uCSmVveiqTZVQ5aY7sbpc647Kz8-Wz6AweHVdvGmzm8zvfIuP1Bi-CWeRvExajDXzA3GTsHJKWhMu2ul_FOBq3TEhhTrw35fG5VbUj617Lwa61gEaUx3r7QLzAV6CDU3FZ_Ug1CCMKTP7or7eDNH8Z582IK7C9fZXx5lS6TIEbA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 566K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 12:02:17</div>
<hr>

<div class="tg-post" id="msg-100607">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2249840ef.mp4?token=jp4ndBNqjS5cjUNjT21bNnjtb733JFLB8LMUW7ctQcE4okcEEA0-Bq1u6r4SkGBleJ_oMUTArGYHQqDai5KuS_9j_8lCeIcxB-g_zGgqYUEaijzp93ACW0ROplDlnFiK_p1aMYI5GyxuThgDpAYW83Ip59IDE9kH0HIV85v8uyOL0nQ24VTV-fybafM8nX1uFN3FblUgsyLTrc1phvnMMGKyHMvOE6evTz6k1bg468HfOmTydd4Gj8KaNaICe-8BcwDVlzpFk5Df0bHM5a2dMIy2lFUBN8AmHqOf8rpCM8YztrJAvB_ZZXGP0zkFoyxoRO84cQeu4Y1Nhye18u-aDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2249840ef.mp4?token=jp4ndBNqjS5cjUNjT21bNnjtb733JFLB8LMUW7ctQcE4okcEEA0-Bq1u6r4SkGBleJ_oMUTArGYHQqDai5KuS_9j_8lCeIcxB-g_zGgqYUEaijzp93ACW0ROplDlnFiK_p1aMYI5GyxuThgDpAYW83Ip59IDE9kH0HIV85v8uyOL0nQ24VTV-fybafM8nX1uFN3FblUgsyLTrc1phvnMMGKyHMvOE6evTz6k1bg468HfOmTydd4Gj8KaNaICe-8BcwDVlzpFk5Df0bHM5a2dMIy2lFUBN8AmHqOf8rpCM8YztrJAvB_ZZXGP0zkFoyxoRO84cQeu4Y1Nhye18u-aDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🏆
ویدیو وایرال شده از گزارش بازی آرژانتین و انگلیس توسط یک پدر ایرانی برای فرزند نابیناش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 912 · <a href="https://t.me/Futball180TV/100607" target="_blank">📅 12:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100606">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3961697c2d.mp4?token=ABigseJz6Ol9DRK_-QduetfvvmkIuw9w5PkwtWnceAU91SZTilDbceS06qOgEc7kn-SgBvm2QY4Po8tguTxZjdaNQyAD0cIpeo-q7ZHbtJmicNvtH_Fy8hgdOTECHedEYR4kr4j5grRvs0y-5t9f53wvMzfkpLVEUUVw8WKPeC58QWsokSLlJvV8o85ywunXTtk9MfudeLZqgtmyH0QqpzwagZ4O_ZmeczPh5pSFU1O233oidBzNiNs5eDHmahSqPiQAgxRb5UzdczuW933pFdHg1EsR7m8P_Sm-C221miJSwasL1rx6_Ewmc7uhqCj6Yk0vyaIsYIuh9XvH_8ODpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3961697c2d.mp4?token=ABigseJz6Ol9DRK_-QduetfvvmkIuw9w5PkwtWnceAU91SZTilDbceS06qOgEc7kn-SgBvm2QY4Po8tguTxZjdaNQyAD0cIpeo-q7ZHbtJmicNvtH_Fy8hgdOTECHedEYR4kr4j5grRvs0y-5t9f53wvMzfkpLVEUUVw8WKPeC58QWsokSLlJvV8o85ywunXTtk9MfudeLZqgtmyH0QqpzwagZ4O_ZmeczPh5pSFU1O233oidBzNiNs5eDHmahSqPiQAgxRb5UzdczuW933pFdHg1EsR7m8P_Sm-C221miJSwasL1rx6_Ewmc7uhqCj6Yk0vyaIsYIuh9XvH_8ODpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚠️
کرم ریزی بارکو بازیکن آرژانتین که باعث شد بلینگهام کلش کیری بشه یه پس گردنی بهش بزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/Futball180TV/100606" target="_blank">📅 11:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100605">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e7414ff88.mp4?token=B1-eFJVOhSdbENJ5lU2fvBiYU1_PU5uSIMirYjdvC8azjdnNk4zdIEawztaZBJQMZFMtLl_2xdVaq6edjYBYsxG3xRcnttakmSYx7UkAQvr0eZXEdwAOFuGj0fAxhj0cbJgMDsIfgprwvgnhejVWulDN0SnuB1OCdbLEmtUbODPLe7wiKxYoDaeVL8xN5HOEBSRp3qqqUtTqBU5Fh39VEgK3XjudxpNVKfHbXMX7DalX4ht96jF8FIE4Sck0DqQWkNA4KlV1ydA1uYD4GtTqG-FR70JxyL5p_1YYO1Mx14v8ATmmkZT9W4v5PpBkAWx0GTmGYcxOGiZlRsOU6kTtkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e7414ff88.mp4?token=B1-eFJVOhSdbENJ5lU2fvBiYU1_PU5uSIMirYjdvC8azjdnNk4zdIEawztaZBJQMZFMtLl_2xdVaq6edjYBYsxG3xRcnttakmSYx7UkAQvr0eZXEdwAOFuGj0fAxhj0cbJgMDsIfgprwvgnhejVWulDN0SnuB1OCdbLEmtUbODPLe7wiKxYoDaeVL8xN5HOEBSRp3qqqUtTqBU5Fh39VEgK3XjudxpNVKfHbXMX7DalX4ht96jF8FIE4Sck0DqQWkNA4KlV1ydA1uYD4GtTqG-FR70JxyL5p_1YYO1Mx14v8ATmmkZT9W4v5PpBkAWx0GTmGYcxOGiZlRsOU6kTtkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلاوکو وینچیچ همون داوریه که امسال در بازی رئال بایرن یه کارت زرد سخت‌گیرانه به کاماوینگا داد و بعد فهمید کارت زرد دومشه و‌ اخراجش کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/100605" target="_blank">📅 11:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100604">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ceef1f3.mp4?token=WvgnGmG-Qe__TC2HwJnYsCYA-0SqS--CXvzzX_hl1WLk-2QEWAo8Km73HqsskS0HT5hbK9XcIlfDptT5oT0kDxykyzvgdyXuVbcp7-SF9ufP072Xf0s5wTE96RX_NyU-Z3cxgKf7gCh2q42ubbl2IOXMRUVcD3CI3_hzQdzL47tX5tMWBOfwltZtDe144obCm_9f2jVyzX22DbcYE3QuZ2atbb07Hq3aZbvISM_pWgwvUl8gknTxMSJmRLJWY2KPAYzS9M_ZtBuzt7l44eULZsqUJ4xqii4p7G8pF9f8Gy1WByBj5vcp-lGq5gwhB0baP2E5kMk_CcfCf98XCgiuy5f0a7BzLJ6-aI9e3N02KSLc0CSK61mds733iXC9y3jx_Vkz266p11iZzu61VnFMdytNz8vmps26JlgaSALzeKoc95MVq5X_KyaNM86m-3s_yJhR-sYkpJECWTue7UG8A4p77V16QpF9WECB49c7iqcu-2N04IbuG-y5i4478Uhb5wNDJ3cVvrQse8lGiWyl_1ZOBcQgDw_3ztK0j5kACNtXtM0sFsJwvqWec8C0-ay5vp9Xpt_JskDXWDCthm_5ODMr6cdz5hLgjqbvo6lKD-ZeM1P_WCCTxDn1R-cLTOqdkPt8lVQ_wWdXdGgPS3OH8MXuFAt7W_z00aE_ibZbTYY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ceef1f3.mp4?token=WvgnGmG-Qe__TC2HwJnYsCYA-0SqS--CXvzzX_hl1WLk-2QEWAo8Km73HqsskS0HT5hbK9XcIlfDptT5oT0kDxykyzvgdyXuVbcp7-SF9ufP072Xf0s5wTE96RX_NyU-Z3cxgKf7gCh2q42ubbl2IOXMRUVcD3CI3_hzQdzL47tX5tMWBOfwltZtDe144obCm_9f2jVyzX22DbcYE3QuZ2atbb07Hq3aZbvISM_pWgwvUl8gknTxMSJmRLJWY2KPAYzS9M_ZtBuzt7l44eULZsqUJ4xqii4p7G8pF9f8Gy1WByBj5vcp-lGq5gwhB0baP2E5kMk_CcfCf98XCgiuy5f0a7BzLJ6-aI9e3N02KSLc0CSK61mds733iXC9y3jx_Vkz266p11iZzu61VnFMdytNz8vmps26JlgaSALzeKoc95MVq5X_KyaNM86m-3s_yJhR-sYkpJECWTue7UG8A4p77V16QpF9WECB49c7iqcu-2N04IbuG-y5i4478Uhb5wNDJ3cVvrQse8lGiWyl_1ZOBcQgDw_3ztK0j5kACNtXtM0sFsJwvqWec8C0-ay5vp9Xpt_JskDXWDCthm_5ODMr6cdz5hLgjqbvo6lKD-ZeM1P_WCCTxDn1R-cLTOqdkPt8lVQ_wWdXdGgPS3OH8MXuFAt7W_z00aE_ibZbTYY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
ویدیو ساعاتی‌پیش از ترافیک در مسیر لار به بندرعباس بدلیل تخریب شب‌گذشته پل ارتباطی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/Futball180TV/100604" target="_blank">📅 11:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100602">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ec89ae70.mp4?token=IsaV3mILGRbyGsFdyM8tzJy94CJpc8ao5POOklMrIRvaKz2PpfJJtNOQZkD0aDB6egbzBC6MBejgmH9DDq2hCHN95-GsTmfKADZLtTgdBrtp6Z1kH0PdukKIuIDFyeXJcosdDOPYa9BxDgRYiZYpNFLa5LfdLLQixG3cZ38fmhg9669hVk85_U88qIkZBr45UokTxd7HhvhsmYCRIy0BAPRx7F2W6ln2_WK0NvdAy8mT41dd_rar6k51t2DiTsWhV0JKRsb7mHOO79eUV6Hd6zjBaju4AIuc-jO9JYhuqmIo36H9g46RfvIQodUW-JjoEMvUI0s6hKJ0yZm_5CvFzihOkGxeBd0kbE2UAxntIpVPsQq5Q3szyNGgWnszMPWi6XW6DX__JjdVOhNL8M3R4nertVcf-z4SfTsXuOHqqJLdsg9Tw45ztLvGK8iKgKCAn3JGCFQew-Q8p7wiieP1AUct-d27d8uoGXWQGFaB_cRTp2eyf4zeJ9GIPgRYhxhtUBs1s4ut_ZTkYcWqO1eHLRObNQF5x5bl3Y_y6A26X_1gSg_VfifrGtCkAcqvKeyWv0EWboSgaRCNxaqE0gy0DzyZUQqj9ZXigcLdrADxxbZZvaiCVbDBiF4zUzY1bsgufQlBfAtqdpMc2s_DAKBE3qvhQCY8c9bUXa9MJhKtQA4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ec89ae70.mp4?token=IsaV3mILGRbyGsFdyM8tzJy94CJpc8ao5POOklMrIRvaKz2PpfJJtNOQZkD0aDB6egbzBC6MBejgmH9DDq2hCHN95-GsTmfKADZLtTgdBrtp6Z1kH0PdukKIuIDFyeXJcosdDOPYa9BxDgRYiZYpNFLa5LfdLLQixG3cZ38fmhg9669hVk85_U88qIkZBr45UokTxd7HhvhsmYCRIy0BAPRx7F2W6ln2_WK0NvdAy8mT41dd_rar6k51t2DiTsWhV0JKRsb7mHOO79eUV6Hd6zjBaju4AIuc-jO9JYhuqmIo36H9g46RfvIQodUW-JjoEMvUI0s6hKJ0yZm_5CvFzihOkGxeBd0kbE2UAxntIpVPsQq5Q3szyNGgWnszMPWi6XW6DX__JjdVOhNL8M3R4nertVcf-z4SfTsXuOHqqJLdsg9Tw45ztLvGK8iKgKCAn3JGCFQew-Q8p7wiieP1AUct-d27d8uoGXWQGFaB_cRTp2eyf4zeJ9GIPgRYhxhtUBs1s4ut_ZTkYcWqO1eHLRObNQF5x5bl3Y_y6A26X_1gSg_VfifrGtCkAcqvKeyWv0EWboSgaRCNxaqE0gy0DzyZUQqj9ZXigcLdrADxxbZZvaiCVbDBiF4zUzY1bsgufQlBfAtqdpMc2s_DAKBE3qvhQCY8c9bUXa9MJhKtQA4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اشک‌شوق وینچیچ پس از اعلام قضاوت وی در فینال جام‌جهانی در میان تشویق سایر داوران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/100602" target="_blank">📅 10:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100601">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dh0w6D6bBcnkWxPPop5S59BVBqv7aJJ5bJoyVcKeVOCaAYRg7feQmPUz0HFacayvQZiqKkUh4e4NAjjeqIW_BeYPn6GtNpt2L5UytQ6R0zJmDPobBGVf2cI_gEwNIhpaUwYaShYgUWZEP80aIEUsAEwOkTtPYPnMYU5QZ6TzYrOK6HwnAOGmj04UNgU__wJf9_rYppyH6-4KI-Szdsr47REGD7MadLsB7y6vMhnj5KbbRkihxLgwwU4-olp83AANfy9mSF0tm-FpQ-dp7zj3ndqj6b7hATO4OLIJPKnb-Ely0COVMAe17FmqHUO_KEby0GCVoBOrXtRDYv2Yv4MxeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
آخرین رده‌بندی توپ‌طلا جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/100601" target="_blank">📅 10:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100600">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfcb128fd7.mp4?token=bj619vvq0IJeg8GqIcxb9aPTmcYjuWiqYfnLmmquRAgj2FHNW66Q1CgOM9v8EliYmgmnJr5Cbujbd8iFL13SiE4QRL_gy4z95s-xvp2gRDJsvdigrO11RXQ5JjyzPdQYFJo9gkd-Jo4g8jUfT9ZQQ9gGVgNjHxnNZXOOh6GL-McAQev8HMj2AO-FCj7Dqw6zorYbM0nAeYzudsJJr_L2d2iatocHn4OnypcekfdAn0qP_8j_itMhm9H5YFdipiYarel1__KPIaIYFgv7IXWdv2TwGsO9yJPd3aBbBR-b3Yyba5pbepKpLw9v8rUefw6ledOHs8rwMOgOoTHIYdCP5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfcb128fd7.mp4?token=bj619vvq0IJeg8GqIcxb9aPTmcYjuWiqYfnLmmquRAgj2FHNW66Q1CgOM9v8EliYmgmnJr5Cbujbd8iFL13SiE4QRL_gy4z95s-xvp2gRDJsvdigrO11RXQ5JjyzPdQYFJo9gkd-Jo4g8jUfT9ZQQ9gGVgNjHxnNZXOOh6GL-McAQev8HMj2AO-FCj7Dqw6zorYbM0nAeYzudsJJr_L2d2iatocHn4OnypcekfdAn0qP_8j_itMhm9H5YFdipiYarel1__KPIaIYFgv7IXWdv2TwGsO9yJPd3aBbBR-b3Yyba5pbepKpLw9v8rUefw6ledOHs8rwMOgOoTHIYdCP5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👍
تعریف و تمجید فوق‌العاده علی‌دایی از اسطوره داوری دنیا علیرضا فغانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/100600" target="_blank">📅 10:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100599">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-hu-AgAKaqpGN6V4jOaGWnBgcEljykL7fxccrKp6VwGPO8RCmSDF9iJ6GrZAHbvUROg0J6BJnZlJQMDdmCUrNYxg_otgCyobXzyAmmBbOV2SyjW6BqsvcN6729j0lONnZNHW_HqCVE7x6LnJHkyHvEuu3cM_TVk9Gs1wbKSrnfRu-b5y9J2qEpAzOK5--0a21bcv6N2DRTDRkYImPg2G73he53gkCdyuDWHM2cmFO6of1I1QQrMpFHxLZbvBiXouaDFgGbN3Qwmxmvrc8waF89QuDyz4XfxD1P0aeZxmsNck2BLGIPuAwu27jhh-msje9Nkyw66KCUtAH8mTxt9aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
سن بازیکنان اسپانیا در دو جام‌جهانی آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/100599" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100595">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/clev_jEt-rpOi_WsmJ6uDCZVOl2anTf7Hy_nUVigH-hW61IZX4X6sQlUujw6h9yVJplAbemACvLa481dgVN83bD17UoS0DjfxTo0j8KVhZlU-e0BEXonnWJhAIPUxROmmWAaSDy3dLTQGy7EdYhw_aAUaxweEykd2IAOItE4Qlt3pfImcAynieveIS6p_o0mMNDi4qEvN21hWwTuXDHhCbDCGFS8QFfhzQ5LxZ6kAQAE72bYOQltWeYvcAdIlgusemvScFrUskuvpp1EbqQcx0Af5aDH3G4ppUce_kzm-1whOesAz-G_FhNpVlSBKPJyghAaTehKT3DX_LdbCEm0XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kZuZRRrPqGJqT7GIJe7e2qy6bRhesgJkdyiteScLT1-dVo4flCk9AidamU3z1TS1F6m86vIyG6oyTHfZhz6jqCLsR2Q2yyRDlaeIMBYvz5jDzdeJ9Qf7CA9GIqm5eoS6gUhN6o1pgr8imLNY9y_XR-g6Bpq5J5C2nfg8b6BbLlYH8limEwdX0XI36o_y10EiJmMZ3nOuZmX5F7QfVmYOoXO6CP-mTsDLmB3RYr8ksAksLmgYSK5pfUTJuXeeLRJup6g2D2DZBYNBpwD4xsxuWrCXh0p0qODImbgU6-yUnBvRvKx0RqZoinEU5C9i18GqTN-tRa9tOhCpx7o80nwRnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o7V64SVBTclIvsId_1yYdlXKGq1pBzlf7yzUOfUBIZaCGjeE7ZjFb8yzzJVBHHPQbJZHqK1gPd9GqK6INBlQP4x9l_FUrayED8jOO826PeRSNhgg-bKJsyhNC3mt_857S6UCpeSm2sb541rmMByyg3XOaeQ2_ccM6NxqFiC3jA5QVp_pcMqo434R_wyW-weAl9HM8mqUAYVppyQCgIxCvKLVBssBDxIVJQgsQbqPqH6VxicoXc-z2GaRTulvzTbvILogF8NRkRw4X95QfbkIlj-ke50KavIo7cc1ba-zZtkcykqmjeopMJHc2sM353HuoObNyLVSfZLYi7pH-xjGWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sA2l0LPH0MC659R2ooDQSER5ra-PTdpi6kvs0DGwsE7GFxQJ20MFg19VUYdw5ujiXS3eXtewNHe4RPhlPJdSzhgMBC08vOxuhGTQftvayFbXTJ1yEWC3Gvd5uMuk6L_oPHToJtEA6_Boc-x7wCx0tS-17GoriXZRnFW9zbCbvS8KQ-c_MhJiJMbjqTYGA0GzW9AGi_UivFkzrwxVdk9rENLEFWNgBmsILQr8DJIgiTUgUGMynLLBF426x4wlPf1_UXiMbBoktuWcbCt0MU2PERlj79s4FtkOFPNpOiR3lnzM7nTSHrBypi29KpJU-Xfl7pfUdFS2wUHbmAFk2EUzRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔸
⚪️
12 سال پیش در چنین روزی، تونی کروس به رئال مادرید پیوست.
⚽️
465 بازی
⚽️
28 گل
✨
93 پاس گل
🪄
121 تاثیر مستقیم روی گل
🎖
34091 پاس
🎖
974 موقعیت ایجاد شده
🎖
94% دقت پاس
🔹
🎙
کروس: لازم نیست همیشه حرکات نمایشی انجام بدهی؛ اگر با دو لمس توپ بتوانی بازی را کنترل کنی، همان بهترین کار است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/100595" target="_blank">📅 09:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100594">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4324684be2.mp4?token=I7B4XZxlyobh0KpMs8Qugo6A1srBHnPx8hBjp-igkNuGj-9u8qHHwbneIZIsNLfe9TMfysfJQcD64FZ2m9IUZh7lchXEMEo_Lp8Ma8l80aWTxaIpZCA40IVBQIoOAWK2PvmlY4EuVUAg6yjSgmJTUAMJhvnbnqeRGfKfVEucViYGPZeVVn863f5mH-LzM10glUbgayKffzKVj2qBdGI-3fl8YAttLQyxYZVvHSkAOAmkIT9ey6SfB40xQX9Rr5FnsKeNfVFiQ6WhNy35RMRFN4hIXPrLZ-YECOElLNuHeoXsX_YfHtHZFQYWRPnRookOIalH97jR9Hd-R1LOd-D1ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4324684be2.mp4?token=I7B4XZxlyobh0KpMs8Qugo6A1srBHnPx8hBjp-igkNuGj-9u8qHHwbneIZIsNLfe9TMfysfJQcD64FZ2m9IUZh7lchXEMEo_Lp8Ma8l80aWTxaIpZCA40IVBQIoOAWK2PvmlY4EuVUAg6yjSgmJTUAMJhvnbnqeRGfKfVEucViYGPZeVVn863f5mH-LzM10glUbgayKffzKVj2qBdGI-3fl8YAttLQyxYZVvHSkAOAmkIT9ey6SfB40xQX9Rr5FnsKeNfVFiQ6WhNy35RMRFN4hIXPrLZ-YECOElLNuHeoXsX_YfHtHZFQYWRPnRookOIalH97jR9Hd-R1LOd-D1ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
تمسخر مجری شبکه ورزش توسط ابوطالب و سوژه شدن آن در رسانه‌ها.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/100594" target="_blank">📅 09:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100589">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a6e4da4f4.mp4?token=Pg7zIaCO1IDI_r0gti8aw7_uHL8GhU43V9E4LgsVnNxnEzKuZ2k0qMMOAOYO7CRVqSfJEu8xLFHs1Z9rk_LTtnadwQGG6B4GN8cMvzqoNXY_STt6K6Lu-f6dnSdVLIxoth3ZnpaFTnflS_MeJYgTF8LlT9XM0laH6tqIKum8yQZSRzV9dUjK31k70R4-upeoEKSXEhOotjAj2C2inluzDCl-SGr46n7jcDAkspYWsI9FSi8CgtoVHo-wxiaBCMheEZglaRPLayJK0NnbHJCH4iI9KPKDgIDq-mT5YLFWVg9BKgsNDuXYjfbijemklybhmwmReeEz4-XOYmOuZZ1Y_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a6e4da4f4.mp4?token=Pg7zIaCO1IDI_r0gti8aw7_uHL8GhU43V9E4LgsVnNxnEzKuZ2k0qMMOAOYO7CRVqSfJEu8xLFHs1Z9rk_LTtnadwQGG6B4GN8cMvzqoNXY_STt6K6Lu-f6dnSdVLIxoth3ZnpaFTnflS_MeJYgTF8LlT9XM0laH6tqIKum8yQZSRzV9dUjK31k70R4-upeoEKSXEhOotjAj2C2inluzDCl-SGr46n7jcDAkspYWsI9FSi8CgtoVHo-wxiaBCMheEZglaRPLayJK0NnbHJCH4iI9KPKDgIDq-mT5YLFWVg9BKgsNDuXYjfbijemklybhmwmReeEz4-XOYmOuZZ1Y_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
خاطره بامزه خسرو حیدری از فتح‌الله‌زاده: روزی سه با گوشیشو میشوره
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/100589" target="_blank">📅 09:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100588">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84d54514e4.mp4?token=jVpQoonrLRj6NUz5L0Aktj1aumoT7-F7xOSVmskuZE1CyA8Pnn-3TnUOWwCQGFGJChRX_vI63V96DutjN7rM80boAEl2PxvXw1UkC_juTBGxpHpYymWmxdHR6y9-ZvOpmNVGchgL7w-N_QnsoDMGijLGiQp9cfXMWqCxZISzY5EQKl2yKJPthV3fNSTkx1Kao3wl7KOcLlZjf-BoeVUA8QgVHq7Ou6NQfYIX-Mxspp0i0rPZV_VEaw9XHwWEd6ELrUuMwX7r6jTO-xDAHSiWTGNBeH8PPXW-MwQj3WwYSyL17kIeZESwrmnk8Ef9pMq-icVSflGtLRvYaKuH5xn5ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84d54514e4.mp4?token=jVpQoonrLRj6NUz5L0Aktj1aumoT7-F7xOSVmskuZE1CyA8Pnn-3TnUOWwCQGFGJChRX_vI63V96DutjN7rM80boAEl2PxvXw1UkC_juTBGxpHpYymWmxdHR6y9-ZvOpmNVGchgL7w-N_QnsoDMGijLGiQp9cfXMWqCxZISzY5EQKl2yKJPthV3fNSTkx1Kao3wl7KOcLlZjf-BoeVUA8QgVHq7Ou6NQfYIX-Mxspp0i0rPZV_VEaw9XHwWEd6ELrUuMwX7r6jTO-xDAHSiWTGNBeH8PPXW-MwQj3WwYSyL17kIeZESwrmnk8Ef9pMq-icVSflGtLRvYaKuH5xn5ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🎙
علی دایی در دفاع از مهدوی‌کیا: با او چه کردیم که با دلش ملی بیاید؟ مگر او را دعوت کردید؟ انسان‌ها با ارزش‌هایشان بزرگ می‌شوند، نه با مجسمه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/100588" target="_blank">📅 09:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100587">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlyUUapLM3BCxH2QzkbBlzsSUtdIesNflqfPS9O7a71dIjiZIbFZ9YC-tLgPegJ1B9eXCRqJZJNZ0oW3AKa4SSeilncRQj2dwon40TDTo-Zc_hcJk6YKpvQBmz19lRBQuKjjYQC6JbicAfgKs2zdKHfpyOTnKK-qZi4Jnm7_HF6AGjJx_FZK8tu9nOGgeyE0qV-RSFr2Uof9ASPPRSiHkuaB3Un0Gn6CX-8CTjhU9Uyfih8zK57OGfHOa-zu8ujIeQ2VRqmtF-sPvFsICW9CFNvOCwtSz8HYpP97W_71KAwhhHT0d36sYJty8IM3PU73JPQZDidK8M3ZHge9xaYZRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🚨
فیفا اعلام کرد که برای اولین بار در تاریخ جام جهانی، "نشان‌های قهرمانی" به همراه جام و مدال‌های طلا اهدا خواهند شد، مشابه آنچه در NBA انجام می‌شود.
🔻
2026 عدد نشان قهرمانی تولید خواهد شد. تیم قهرمان جام جهانی 30 عدد از این نشان‌ها را دریافت می‌کنند، در حالی که 1996 نشان باقی‌مانده برای فروش به هواداران در سراسر جهان عرضه خواهد شد.
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/100587" target="_blank">📅 08:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100586">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfeWX4p-gozdJXxAUSEmIMN19aPflw0oXgsNuD734Egr-JCMec2_yY7mSnAiM4YNXX3qmXgPBDMTSDeACm0ZfWCyizI6_mrgokK0QUiavLoNl-UccUt39WVmkkWQ8kIPrKJoRucL7J7V1_dx5Cra5Vl9uuI3719-xJ5HLQT2mgoZkBGGOFcLZNzzy2innkctZCDwkGCF9Ex_5iWfC1Pp3s0TjRZCnB6fwynvZz1pbhzHBCaQpgTtf-a8nydaIfOc0eKxf3ouq9obo_xyPJRoL3x8LcRzrOyk_RK-jbFp_cfRZt9VVGgxX_lTHoA9iKGoKuCdh2SJUs05N89z8tIGFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#رسمی؛ با اعلام فیفا داورایی از کشورهای اسلوونی و ونزوئلایی برای قضاوت فینال جام جهانی بین آرژانتین و اسپانیا و دیدار رده بندی بین انگلیس و فرانسه انتخاب شدن و حضور فغانی تو این ۲ بازی عملا کنسل شد..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/100586" target="_blank">📅 05:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100584">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MNSIXIkBEnA_ZavuMhHkljJmz-9bsGkW54iZ7wGDh6CNQoZCnQu509gSo5Zqqpe8di0XX2bYqHn8q4S8DjntCOrvqlwnU5zB80f69TFFlYZUSNwNg575vdMXvdZMfMCAzSv0ZHBi2829VNYxfank8uPLHtxlq46dIm59HicXyhAfrGl-yxTn5JcsJJGea17HZ-0BES7m3izAfKJ2e7TKJgb5hrLlZMr0hFWKNOXwL7WZCoOzUeUXDm11tUbl2qETik1zLwEewZon5Bo7QpxoNQGeO1KXCeiaLZVyQdRfOAJZUiILBowmuMTuYZ_3RE0WWEK5UrTJdiZcTeela1jx-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O0fUgZUekPUBx0LpJP5GtETZ0nYnAc7dY9DPZUmmK1J2Xz8qF5Q9cdm-DM3pETTjX4JLKLcNOXkZ54Ce8WmwdcEBtwnElH-VHPzxgq50s7gWupgZ8br0hNy7cRwIro2HTUumuonlb-W0fO2hR0aa3M0eWO3SfPTG_Lw99nI2jgLoLqbI94zG6hBJPYmpiMhMdv5G3yMd7r0Zo3PYS4MgJjqRxfCGFaxcllw0wuFzei18VwVPUqa0Ge4N7FFlJuZ1xQWixuD-3t1J8-FT-w6WuQH9N9NVFbIEw_uuwHEsO3Cju0CDwh3gJBUhx7I0-j9GcK6GpCsp0sOfzuvLk8dkQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
لحظاتی پیش در پی حملات آمریکا، برج کنترل دریایی ۸۰ متری چابهار بطور کامل فرو ریخت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/100584" target="_blank">📅 05:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100582">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V9QwjrFScVlaS27inPbVt22iuRrbj1O6DvDAQPuZN4ixgIKmlWTYEMuiKJFdooDJ2C19529e1QRN770mIhE2mQ84JlNPJZaeZBPUP684d_6ErOla6qigsXkGPvfjKT6px-6KSXZ4jouazMt6TKUDABcfFcwqDojng5-YzfDn_I_MzhPBD5ilMZUM4QLWY8bmH5cRFm0r06yYRA6Kq4-B9nmm3aVLCFHkHtI_81Qf7R052Afcytg4965BjfUSWDi9femgdil3MlCpPq2QfFS116J-tpR5mOFAg2sK9Vwz0U0sw7L1-radw-YilMbbTOFogNb_727vWjFlSdW4V8e9Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hTjqE9gu0RvbZhGiN47T5kVBbNfonIBd8h4jUDS1z6tgFVYNZWAggIGvUGrZ1_V-0rCx9uWRhGJb904L7fwlYlq9VT-q0DkNR_Mn_LL8s5MUZS2fnbLvZXJf9BiswwelB_T3Na-vqbXCWULyPAg4eaHAiaI8lXGNnYI-oOJzrGFgrmtPLewA6qGS83dJtE3Mwu5wFLG2_GjqwAp5i0l6PklsGtSE61banLFJbDS4_iOvYfvQvwTkOIyYEjMeVg8cmgZ8Z0SeLj4HGd6-y02iNQ62tiD6wM4l4kbJSAgaELRKBV6n_gb71COMMDELUkosvnowm9JSamHaiRCMggKUPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#رسمی
؛
با اعلام فیفا داورایی از کشورهای اسلوونی و ونزوئلایی برای قضاوت فینال جام جهانی بین آرژانتین و اسپانیا و دیدار رده بندی بین انگلیس و فرانسه انتخاب شدن و حضور فغانی تو این ۲ بازی عملا کنسل شد..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/100582" target="_blank">📅 05:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100581">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sReM6vs0vMVzuEXLa-BUNfDef2BfXJRXS3pl2mmlq78LoCTkXs47mLmQphLza-m3sLccJ4HdAG62DkQC0VbGSI1wQBMVCXx1tdMjfVMmo0iq1OIBxoAz4gXLI103Zlgj1Bd2K2tg2h0ahhRaUV-J5RMVtmXW6jAiyaZ5WSn-oxSfxh3cK4Axb09F6aiVXp7LcfhTel01gDMi8eSBuR4761BYf-InnW0sHhHLG38NJ_amfDjtaV0kbTRe2hUTNvu_OPoJgj2dRvizO0M0fnKkokc5pSx3GIUFc8vaFG2gkAH9pzoqge8Y_x1UETPqbziv07vr4a7Nsg-3cOlx-DLQaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتا: اگر داوری در فینال عادلانه باشد، اسپانیا 100٪ پیروز خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/100581" target="_blank">📅 05:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100580">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qt9G_Mc2CNYc-f936Sh8NWx-OKXtRL25CFgtWwOqjvaMUpEO5HpAzk7HUNIJ6ZcLTJB2gX9rkp_gM2YPJ3K51FXRtjAa5n4s2VG_JE4zKJ7oYvA-Dng23uI3InkVxzbtru0bSW1PWkmhdRgBwn2OdAlFIyI3wwgxBLSz5ijoZrUer0S3ZxLH1aWFqMcn8RZGawYf-XlZFPJcb1I2KOKnARG3-hFNgPyHckC_JqtaZ1-_3NUGIDlsPmHUHgj15Kw5FJ024VuO9x1aBAxWjjHeu7Cow9voQDOSyphhwkW3We6qHCAjRrWud7LCz5jy8AFU4i0xNQvM80PWHgRnaca-mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پپ گواردیولا:
یکی از بزرگترین پشیمونیام توی دوران مربیگریم اینه که نتونستم توی دوران اوج نیمار توی بارسلونا سرمربیش باشم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/100580" target="_blank">📅 02:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100579">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOc7-eov9vUNX3-xHzqZgPNZZrx2OtCMvAr8Tqu3xl-pTXCMmYf5DokqiH_XpTc2H5pBA65MGh6Iso-1mM374JzVDei_O1Osexr8CSVah1qhrZO_tptAa6EIkKUGluVT5I_rrTnuL7yu4tb2QGx_5-F3N6-Ah1N-1WJN7jpX23eF3CeOWyGtwLnHOpEMkBTFu6mQ8CPANsWUpb34ofB_nD_qGF7mS6Hsf2XuG-3O-56YQlgOpDzKTtAQb2E65u8VBJlZv5jd5FTR2q_iLfCtYeAoRCWhsTBNV81WipNlJOzlJtQFWFV5d5Q1jLARjseCtNrUzZzLkJ41eLORTXoItg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
🔻
مارکا:
مصر درخواست میزبانی سوپرجام اسپانیا در سال 2027 را ارائه کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/100579" target="_blank">📅 02:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100578">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🎙
🇪🇸
خوان لاپورتا:
- ما یک پیشنهاد ارائه دادیم و اکنون تصمیم با باشگاه اتلتیکو است.
- بازیکن(آلوارز) اعلام کرده که می‌خواهد جدا شود، اما پیشنهاد ما تا ابد باز نیست.
- در صورت تغییر موضع باشگاه اتلتیکو، ما یک مهلت نهایی تعیین خواهیم کرد.
- ما یک پیشنهاد بسیار خوب ارائه دادیم.
- این بازیکنی است که فلیک و دکو می‌خواهند.
- اما اگر این انتقال انجام نشود، باید روی گزینه‌های جایگزین دیگری کار کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/100578" target="_blank">📅 02:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100577">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7THh4Mt5nBHx6-NTYgmFVde_GCF2T2EzzwhWkv2TnLNFr42JtodaPNmnEI2iNB1lqF-_oUFHxelr4TEM6bLZbZkuFNd3GrHojB0mO-YHqtvdtunGlhsniS1JlrrmLkLSA7zWERxAwTsMJrONpgivMKpfwLPQPCi-meP971_KAwx4L9dPyZSGrDj_IcxsMDGR-48IoBhE86UDeSX2B09zKL6kzOG9hGhafGHxxl82t72rWXJzg85_-jJgnvkWP1nxxNCjnSLixo1y5UTdoMEogttq92ydijGOrDCXAi0fVIRD8InWNPBi0xwOJkdQotSJ-UkOPDw8z7bIc1KNhniEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولیسه کیه بابا.
همون همیشگیو بیارید بایرنیا یکم حالشون خوب بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/100577" target="_blank">📅 02:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100576">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/100576" target="_blank">📅 02:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100575">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OJPqS3oCa7z0HYT2hKJFw6cZBslen1RLfuh1D1V3cjl-NxndDnns8oPW5TUONzhrtxcBJz_BmlbbHovoaPeMTxDM3Qs2tBdOCLA5Kag2yvAR-1lPK7LHWh-j_HmqoGEZsEuIrlp37VgOxwzHd7ObhbFio3Smpd1VmNTx37VMxLcrK5Bt8rtDStjjhMQG_CqgXsC9DzFm1sqiTGxoaCILpUiiKEwZUsb1-70eUUWjVrjmZL0qm1l9Ncf1Sg1nxdJF6Qi-HB-zasvI-6QpizwXg9FObKc8xu-h4qzi1oUTFLL4NFWEOswIp-kGgyIJoWntb3siPQI_vDR-0KhJAXGdxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/100575" target="_blank">📅 02:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100574">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
‼️
لکیپ: مدیران بایرن‌مونیخ از طریق اوپامکانو درخواست تمدید قرارداد به اولیسه ارائه کردن اما این بازیکن رد کرده و گفته فقط میخوام به رئال‌مادرید برم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/100574" target="_blank">📅 01:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100573">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_6mjRkZJveE7tolEx4-iuhIMwrrIR0-WtkbrQwjCZN2RUKlbu5F1p0XB3bH8PpNdvxIpXmrYuwL4sbs1bfsMukzqfMFTBkdVtIWhgmwAwdk9NXfr7Pwjkm9KGyVbQ_KxVDTEpXLsmympi3Jnv4qI0oCU7o9kQExLkcV7pDVM6a5Aq155HL4MVadZLW13IJE1RfvQkfe7GwGH-JJLedu4bsj9yhuhZGBbQC57dCSM1PbgB3WoGMfJSqQe5Iq2hBro3W1l765Hi8cY1o37uQgQPmitmen_nbzIiBuKNT7C0bMIDgn5dzYgH0hpkxVenIbUDFJIsRgLuYBby8w5pKeIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇩🇪
🇪🇸
لکیپ‌فرانسه: برخلاف صحبت منابع خبری آلمان، اولیسه شدیدا دلش رئال‌مادرید رو میخواد و پرز بعد جام‌جهانی با پیشنهادی دیوانه وار برای جذب این بازیکن اقدام میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/100573" target="_blank">📅 01:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100572">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bw1-ZdbH_yAb6wges4SHC4QtBcCexTiecU-Ox5M5u1qITdGki-0pz5_Oi8YXchEkvGB8TCRjeH_QCdA6MDD_peeJ354rRPl1e0SKJH-2LVnC4FR0GBwfMY9WyTF5SktrEXRjybQgh6NrduFsetN4nUFhlBBQ3kCsi2ayM1XIIhRcM-Xwrjca0ko0leKH2qdg44wfgApSFpi9ujxBOl5JSEUBMpNPV9dTZ4F6T8z8md2pkL90yj4X5mW-7ZLRth_y35iKEGvQ4O924DeKZBOWWV1vQyxP1OLYMnro2z5aM7MSVD-JZXAxVVZiRTphi4tCLSSOGrRlmx9ZeUNh9LrnDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇩🇪
🇪🇸
لکیپ‌فرانسه: برخلاف صحبت منابع خبری آلمان، اولیسه شدیدا دلش رئال‌مادرید رو میخواد و پرز بعد جام‌جهانی با پیشنهادی دیوانه وار برای جذب این بازیکن اقدام میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/100572" target="_blank">📅 00:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100571">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrssHWxFPMPhe2vK0kjeKDs7PA7uca3UtdJ1Pc_TVV3-YKHjaBvER1YET_-48hKkb5dEkTXnmSCMQ4uDYAcj2cz__PtV4Gq_wy65GgPC-bDjzVs4wkHTHPnW7AOQLuc_rNx2Sdwhb1UlIZtnn_pt3ThrBqoE-LA_X-cIt2TJW-BZC7o2sdpxYJgYLJjBOGRPsuU__IFWtEKu1kzKmRGPAaerbsyG44Zn2YUYSXrfAtcCMrj_Ja7XCaETBqdo3-IxC8e-P1eI9ZpYKnKes2y5BGCdm-OuYBZ4djMgwPqVoqjcnvHOUkoSANtWDIFyg7QdtqaEPTno1Jq1v9eSJr9v1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رسانه‌های آمریکایی: مطابق صحبت‌های رئیس جمهور ترامپ، حملات به زیرساخت‌ها شروع شده
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/100571" target="_blank">📅 00:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100570">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHBGfT_DzJcSsSdx5oPmw6P_zvEMsT7JJj3Hy1Xv6Pid-6x9Frb7MIkF5H8qytVu31dNa2u3hNt82YiUnFRx0x6eu5sMqaOnKkjkwyyGTcBhT5O-KqTH_MWzoVm_oOmZ9XyzzknXjuW6JkUyeTaUwrq0ughM78vBt6VbJDTvz7O9kOwAgtZ1RlAvNR3Tehmz9g_xAutLzj5aLINyy6UPhoDuvSnxjPxHKd8mKRwa7FE4KpgWl_MHWieHUZ_I1wYwC80_lXXH3gDmu404MSBPj9gmDXwyCZkPURFch5EUIGpKnVV61Kb-uXNO3aErqjgKbIZg6-D_0f8sTucPbLJSqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ویدیو دیگر از پل مسیر شهر لار به بندرعباس که کاملا تخریب شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/100570" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100569">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orSRCvQqnajs81FWFIeuOVhTeVCUBABA3Dnc9AUHlbz3jBmVu-GzKXbfMgkw0e_QuCB2ndQX8B6l1MbksS_wQO0lQ9jLwJdKS-AQPwT5G1U6eqknO6Bsc95hDbgWIt5B4LLcN_RHuacvrhzimxqMCBOeVl3_6B-yBeBJtFL_imk2j1zZJwj4k2dYdCv2VAGnPTokOhH1A1ZeixOGmS8lYQwWCQl4HNkz8jrp8SaZNNJpTPE-WX9IoRTkf30K6kLE5EcB_G5hbkLJm6BBhoANkMto6DjknrDJMWg0vwEi-DZV_ypLNLxfY5b33JO5G9W-k836PDMsDHQ18IYhjH6KRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تمامی پل هایی که بندر خمیر را به بندرعباس متصل می کرد توسط ارتش آمریکا مورد اصابت قرار گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/100569" target="_blank">📅 00:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100568">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
⭕️
ایستگاه راه‌آهن بندرعباس بمباران شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/100568" target="_blank">📅 00:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100567">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Afg6oO-ovq317_tQTOo0HxO0ggUX-lRgpM0yRmrc0WM13OZuX3D6hDfRDh5LG8vuEeWCzw0OR5UaWr5x5ly4XOyUxmPSMeAT5k-o9cYHiOxpX_OAB7x60yLW3jYxbDF14ogWhScxsY-Y4sk6R18pMXL656qR6e_1Be3ipOR4PLs4BDdC3sXHuNj6wgFe2B0Wr63WzB9SAGimMCbaL5V89OOW6gMk08U6I5OxsDpdVwOh9qJCe0s8ZyULqG2_H5roQfl4d7DRqXGAwOlHL4UA3XNu8VLhst_6mW4hWAdPUQ5wVzH7QQ62uqFfo5NPRUe4idQNVoxHhWHCxCgG0GiC7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، تو فینال جام جهانی 2026 حضور داره و شخصاً جام رو به کاپیتان تیم برنده اهدا میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/100567" target="_blank">📅 00:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100566">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMLrZ9MjbmGQ5Uw12JZF48FwGQHToWaBKn8pAZmwLN7BwJ4-rJnc07jLdIdGhqrrq5cM1YScmnNz5AyMwyrZasakkH83Wq9mS-2WjZPDHU5a8uRvdhRr-QvyvV42GUAm7vwt-pSojVDKkH4RUkgnigS_4kopyP3QQ8Q-fkqfiFBZfHAHdFslOxj9RsPmAn_kdKx_ShrL7Ijie1-5vPYa4vDjK2bcRzLU5PSEn1lyN7kKXlc0VmjwHparvuMff2I6j1IxRSSDV69hLh5bDt14UVotkGOb3CACUdrbeT0PvYWax-MqMrqnn8t4s3kSCUvepLf3hUF_0Y3RhV5Asl9Vwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
محمد صلاح قصد دارد در این تابستان با باشگاه بشیکتاش‌ ترکیه  قرارداد امضا کند. صلاح درخواست دستمزد ۱۵ میلیون یورویی داشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/100566" target="_blank">📅 00:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100565">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
گزارشات حمله شدید به سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/100565" target="_blank">📅 00:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100564">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a4bc985b6e.mp4?token=Be68sHZEO3kY9b4FOeraWGvrcnmW5RNGawVCp64gDXk5HX4QdJhNJbZ90X1sBlW5X6NW0qZGa54imOmoEY02Ivs8aGdid63JORSxGlglaP4aDwN_6q0iCghIwmLGoC1hjtkUGNk2GjW2mdpRpgQao-WP2t04rT41SU7Fb_8XDtBeAD66fTIXYpyhsfGH2trzpv5xwhbKvo8bqXxcQ8VrA02Lrqlw9-yCW5V9lYJPZ1hsmAJfWphvpsqoAWusfwwx_WSPS8fxwbwiQ3VSzPYANqxA0QiaWyiYzwcOqepsjScSEGlvPga7tvNpBqOL-9YwXDbbqThfEFMRX7aIvul7aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a4bc985b6e.mp4?token=Be68sHZEO3kY9b4FOeraWGvrcnmW5RNGawVCp64gDXk5HX4QdJhNJbZ90X1sBlW5X6NW0qZGa54imOmoEY02Ivs8aGdid63JORSxGlglaP4aDwN_6q0iCghIwmLGoC1hjtkUGNk2GjW2mdpRpgQao-WP2t04rT41SU7Fb_8XDtBeAD66fTIXYpyhsfGH2trzpv5xwhbKvo8bqXxcQ8VrA02Lrqlw9-yCW5V9lYJPZ1hsmAJfWphvpsqoAWusfwwx_WSPS8fxwbwiQ3VSzPYANqxA0QiaWyiYzwcOqepsjScSEGlvPga7tvNpBqOL-9YwXDbbqThfEFMRX7aIvul7aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صدای پرواز جنگنده‌ها در ایرانشهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/100564" target="_blank">📅 00:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100563">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ویدیو دیگر از پل مسیر شهر لار به بندرعباس که کاملا تخریب شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/100563" target="_blank">📅 00:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100561">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/110e253ea3.mp4?token=s7KfgZb4ppJ6aQlCbrKRylYS8bDAX7Iw2xD_UirlHs9mGM5lU6T-O2ue9Cm9laWQoEOkmq9mlBe-1rRhCLuG9cYmQwzL8JsTYAEpzThtMc9aJuX0OkzkVd5MaSRMXz3BbTXRZV7a4JPse_JABs1KnVUPDkjw3HyBtVI5xYSixIQwvxwVtlV1d5XkS0Vv8vhNdIYKCtN8xC_Wayo0AGuWoO4js0WvMTwvuHStkJ3sKLWHe4QisVImR_lwoGaJJzOdC8x0tuGz1RMT_7CuTkHCPPKN9QhM18C2kJza1WHB8EgUYPfZgIIl70xxCJFJdejrl28H_4AyNqtnqyk2X3ERfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/110e253ea3.mp4?token=s7KfgZb4ppJ6aQlCbrKRylYS8bDAX7Iw2xD_UirlHs9mGM5lU6T-O2ue9Cm9laWQoEOkmq9mlBe-1rRhCLuG9cYmQwzL8JsTYAEpzThtMc9aJuX0OkzkVd5MaSRMXz3BbTXRZV7a4JPse_JABs1KnVUPDkjw3HyBtVI5xYSixIQwvxwVtlV1d5XkS0Vv8vhNdIYKCtN8xC_Wayo0AGuWoO4js0WvMTwvuHStkJ3sKLWHe4QisVImR_lwoGaJJzOdC8x0tuGz1RMT_7CuTkHCPPKN9QhM18C2kJza1WHB8EgUYPfZgIIl70xxCJFJdejrl28H_4AyNqtnqyk2X3ERfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ویدیو دیگر از پل مسیر شهر لار به بندرعباس که کاملا تخریب شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/100561" target="_blank">📅 23:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100560">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=kC6G5jHPdTWIAAHcomh-KClPDSdb5G0sxPZE3NawBwlFOY7PEUwIAqVYSzGa7x0NbjqxU_W5C9f6PggYomIITHz09kWZrqhJs6kMx0Fi7oAy_3eYMEd2qQT7FLJt9jpfPRIc0FQ2R6lUQSuK81fZJHwwV9dwdEUFKtLfIK7xOpNlImN8L2LfDNRXcf7eIYWuLSpg3Oh6Wv9Kfds_BHa_LSIAy_pt_uwMtKPJaZfKQWiUMGpUzgR7IePRiIimAgZ6_O72C8Jf8vyq3Q-9wuSba57KSxQysqwurGo2ZD9PJhCiSL862YfQJysoXQmxq3oNbaezzkzx9ffnugSJp0MPJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=kC6G5jHPdTWIAAHcomh-KClPDSdb5G0sxPZE3NawBwlFOY7PEUwIAqVYSzGa7x0NbjqxU_W5C9f6PggYomIITHz09kWZrqhJs6kMx0Fi7oAy_3eYMEd2qQT7FLJt9jpfPRIc0FQ2R6lUQSuK81fZJHwwV9dwdEUFKtLfIK7xOpNlImN8L2LfDNRXcf7eIYWuLSpg3Oh6Wv9Kfds_BHa_LSIAy_pt_uwMtKPJaZfKQWiUMGpUzgR7IePRiIimAgZ6_O72C8Jf8vyq3Q-9wuSba57KSxQysqwurGo2ZD9PJhCiSL862YfQJysoXQmxq3oNbaezzkzx9ffnugSJp0MPJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
پل استراتژیک که شیراز را به بندرعباس متصل میکرد و مسیر اصلی حمل و نقل مرکز کشور به بندرعباس بود، مورد حمله آمریکا قرار گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/100560" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100559">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
تسنیم: شدت حملات در بندر عباس به قدری زیاد است که برق برخی مناطق بندر عباس قطع شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/100559" target="_blank">📅 23:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100558">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
تسنیم: شدت حملات در بندر عباس به قدری زیاد است که برق برخی مناطق بندر عباس قطع شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/100558" target="_blank">📅 23:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100557">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kouHaaLcN5VPMoIfu7PlsOJtCnsxhgtel3rAq30x_pnjrcuKj0tMgRJqAQ3tnerVQWH4awD5fZdr3JzjfNZhv0OJA4S53PERkp7zMsKN-SZFO05fuvo0qYJVBsvWNfep1gy_h0s-M5TFNp_ZIuiYPkpVWR_jjAmycAPRhM7aGsP8j3cveXY7x0hYCAuvpkRhGBaoJ3kcQs4fsTRI5e_f2IRWE4mGkPSVMjzMOXuarMqHMc9sCeA9KNMHVZXrA8URa3jlkLNA9z5x6PXhPw6L0y34FSGa9MKQrFtOMMyITF67B5lB3-2nx2c4e6RZdbrQnMFBwV6YOcxszaZTi8xqWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
گزارش برگ ریزون RMC SPORT:
ویلیام سالیبا درحالی برای فرانسه 7 بازی انجام داد که دچار شکستگی در ناحیه کمر بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/100557" target="_blank">📅 23:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100556">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyfnjCviw0ZZTc9mD6mUPT1T_NIJ-Fx5MB6zYCu4CbvjlyQzTJ-okvJXrttH81ncwN9SlOFneteAYLDw6HaKc996VhrZe43wk1UBs30VFJNego9lH5ic9pppVzDtULJUsx9TNOfLpEJiypfwKP2BLpi2D3rZ5ehgdQAwcKacSsv1NsHH2mSxLwWivJB3bKNjlv2L9q-WcM5GuWK-5eWTNarDQ2uOEWCSqG2Lkfjeyp7jQM_XQy2ymmht78L19hiX2nA0AoxL5XbF1ZRantF6KymUsoqieYBT2xWHjYqXQvf-UCQEvy9n0OevQ2rlvJYeltOAbk25ZiJ7XLqnOtemCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🎙
انریکه سرایزو، رئیس باشگاه اتلتیکو مادرید:
خوان لاپورتا از قبل میداند که خولیان آلوارز در فصل آینده در کدام تیم بازی خواهد کرد.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/100556" target="_blank">📅 22:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100555">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16fb64d04.mp4?token=trFcvpXnQqVvx3E4MgGNUys6SCZArV0cyeYHjhsx298jTA1s6a87SBBrZ1Cec-1lZ6V-MVxF4tHl8SZi-1EDEJr_8HdRihSJaqIQUy1jCgs4Ibs2OptkTydPd9EXb4hj5zSsmZ0t5yNT018bDkCQ8llFBLLux5aYRSGy4nzBQXUitRr9Up_YEq8S7udztOcgSxs37RrbYhvwXlgP4UfSSWAcHQWotBa34dDvCgJudyM9Ig0b6dIyE2X5k3ZpjToe_bNwWM2RfkCjBqTWfBLN5l4MoFMXNji2ImKR5SZN7ZveCYfWwgqQEAUSf3qDEXp8me8n5i1_JM5E1PS-bpvzOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16fb64d04.mp4?token=trFcvpXnQqVvx3E4MgGNUys6SCZArV0cyeYHjhsx298jTA1s6a87SBBrZ1Cec-1lZ6V-MVxF4tHl8SZi-1EDEJr_8HdRihSJaqIQUy1jCgs4Ibs2OptkTydPd9EXb4hj5zSsmZ0t5yNT018bDkCQ8llFBLLux5aYRSGy4nzBQXUitRr9Up_YEq8S7udztOcgSxs37RrbYhvwXlgP4UfSSWAcHQWotBa34dDvCgJudyM9Ig0b6dIyE2X5k3ZpjToe_bNwWM2RfkCjBqTWfBLN5l4MoFMXNji2ImKR5SZN7ZveCYfWwgqQEAUSf3qDEXp8me8n5i1_JM5E1PS-bpvzOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسی و یامال تو فینال
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/100555" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100554">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBwJ1MEjZYhqhfcVp8PuNAHGJR1dEyEAyRZxSwFPISdROtDhYUUg4aOo_8xn_5Qjh8ub_Wsq9GqSm7S9ik2royYQsKELF2ZuXBClW2qDijDxK2kQUfqZqBkZ8MrKM2WIXRRR6zZnQXeF1YSTDO3OaL-nDCHM8XU2nyC0IC9URy4DNTFvU-fWfLGuDBQ0Skztk3tbSf4Cmg7d_SEu_FDpT8B86vGRUCSF3WIfeYvjUJQy_UNw7RyuSt7E_Rppj_P_vh7PPnwlzYrOiOAI6kQ8HTuc7I9X6Mm-PE9T9QHtw8wEThiMpAugD21FzvZ6JyCxdS00VImTmHKn4ubXA53PIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
برترین گلزنان تاریخ تیم ملی آرژانتین.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/100554" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100552">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dVjippR3xz38UbuX-HiFI2rh4NKtpKZesiaUAqyi_Mo-HpmWiAU1Py6jnM-R5D_K6_PXT789eAVHRERnPOSZ5odtLVGhMQR7DSgBT550NIcsBNcpfuf0bjw--wR4lJD2OTD17r_kw0vTrr_lBxY7dm-ZPWltl9ti6cNxwXeS5_uAlgp_-JgJ3hGKvPJzmgLZqeLNUuCzD9DeDNH26oSGXTIQPsvMAP0nCfmdw8IYiygBNXWt5L_PTuEzYM6NeXh22OFhMBVBtecFJwbs20i5zszahXqNKudkwb-MkcjVmYV6sE13pVsEspYZCdEi37tmo2D11M8GciSrSQsbEOsEUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IISK3AL1vEq_m3ynI2TJez0RAJ8GbYevJZDp1O7D1vcEuA-4vC_nAgRKdJL9EyKK7y07Qk63IJPVKEBbJrx5QQX35oR0E9b26zt6xyKNdQZaUS5KKiPxQvywuDdYEQpliWXjzQbfppBLQe0pF1hRGPrpZC6v5tzrR-b-OAGAQpy-IxulnusEiWyr7vFnMHGW68ECxijoxWyqpeUubVw6VleA4Trm1lXDsmhHdjj3vw67EBkkFnHcn3sGZNdiEgx8wFi1WxM7bOTtteWK5es6tJFLv05vvxF3R8CjLqTHMbO0opo5OTMTh0XQY6r8ayXqi8YBNFP2gvjOHkQpXkhqKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
تنها 2 بازیکن در جام جهانی 2026 بیش از 20 دریبل موفق ثبت کردن:
🔺
25 : لیونل مسی
🔺
22 : لامین یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/100552" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100551">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFNHHt71RmAla-b2kc7o5AS3dpsGvuy2VD63ls3u60P0FsWcnDnjEB-C9_q_F7WcsXVx351Z8xyFiL4ceDPL2JJw9EjaNA6py0s8WGBWeYCvZdPumPA-UvmcOgCGAWFr8VxRAbMdRiUy9220fXhej84nb2Uvz4iTcJnQhQxtQHbQjbJuS5RQxL34lv1ieYZxrVPpw-mt6KKeAnSMCW3XAScq_DlmF6IGI03LCQzzp6FKkKtwk_mGXOTjTlg0E-Ok3VzGUJ2EB96YMZIAyNTp5laEg7UErr3KtdC_CwY3wPJQHmmy0L5QQnNykSikGciVwd3EnZdFRtp3qZ8pFRI-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگه آنلاین‌شاپ‌ داری این خبر مخصوص خودته!
اگر فروشگاهت تو تلگرام، اینستاگرام یا بقیه‌ی شبکه‌های اجتماعی فعاله، حالا می‌تونی بدون نیاز به سایت درگاه پرداخت اسنپ‌پی را فعال کنی.
✨
امکان خرید ۴ قسطه برای مشتریات
✅
فعال‌سازی در کمتر از یک هفته
✅
افزایش اعتماد مشتری به پرداخت
✅
بدون نگرانی از فیش‌های واریزی نامعتبر
🔥
همین حالا ثبت‌نام کن ‌و درگاه پرداخت اسنپ‌پی رو به فروشگاهت اضافه کن:
👇🏻
https://l.snpy.ir/i1ekm</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/100551" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100550">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eo7HIzFsCCxFQeRr_y5TRnVVjK_b6_wY4mtNmPCcGZE1bXHr19djJckv3CyK-3nIrEjqdLMg4igNO_DBws0SgR9XvMsm3Tdg9qZrb8LO4S8HJtLUBNOXKpmBe9EER3vX1akHNi6pOqQFduSy8YbHFAWfozSjE77JUrcyWvFMOoZJ7Ek064VuF0bh7WusloM6xydpA18v1ZVGSok4zxpe6YPqbh28QpbK5VAoFWfJc0UXb0BbpsaEIZc4bQHtRafdJURLjtrT6YB8Vw2dEgR1TxdadR3TK5iq-d8S9eybUquLqT0wk2er-1kN_j9a5ACXBW8bAUPGeWSqTqq_JazvcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
فابیان رویز با پاری‌سن‌ژرمن برای تمدید ۲ ساله قراردادش به توافق رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/100550" target="_blank">📅 22:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100549">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGj5895lr25rK21mjYXds9LkYOuWuF05-c9COGBllDyfLif_X4jjWj5djHXFCyWs6Py0Bk3Yw-NthZYz-_yY1BIGGXp7z08oEvw1bw3FHacKqRSuXDUvegliTiRpBzoziUOEMZF-nqxsej6t2zxe4go-Q4e2gBcIlyCucMXh31iPdvt-8zuggj9ecdvv0a988FGY93vzDT4DZbjOnxrXNsWA62eCbvtWhdS7KHeqqCQIYsF0FwqOoOvk86b_L53MpQHiT8FmwGYDrEmBdg3VehjaKOnZ0QGnMry6_-cqTcbiZg0NYkWVtrp2n-PyXelgdap9a5tRhzzUj2QOhUixzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سنتکام: حملات ما به جنوب ایران شروع شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/100549" target="_blank">📅 21:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100544">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dQTiNbsGaK1joQfnMcGhtNUMnhKyDkEnlM35PEtcRE1DmJjMaMTg3krf87S05S8bRJj0Pe82BiKMWkvUTHg3vbbyVuPqpAsI2AbyvBez3YEYFDRxN2smAjEOu02PPrMgtvhP7SkCuOBVt73BuOvQ2P4e5lTzyOJfSoZCIghJ7GZdg3nJreJkU10xPsUEEehSUC9lui9CliNhrjgSXCXousX8SxouVX0vXKX5h9yiOG8CsqImhC2W0X5J7wsgBy-ODxlK6oGRA8qtN0LLNBvjgr5omBAB77KmtDU7QXFRRNEODYq_PyMGIHqPsr3MZ1QVa_jU8YWy8PfVcmge0xJ7mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SYYyOpwxqmD9XmOTvfcO8PibB_iBhR4n65Hes1ewXmry7vxvEsitZrr_Au5-h4PO1_esnJR1Tr3NE68pjj7ZU92X3F8RVg5NuvL-6Hdw6W0qEHQunkOYYWX-dfA5GcarPjFu5RG4nfz_sS8kGT5nWHtDyShYJzq7pZag2r4cpgSMHkNvI7_fZGyzBEexJ9YepXzAT362UjnHT2EpNhMk5soDn4OAUDq3PNXysq9R5wgs0fKjjKfABtqRDLSjx6hAMz0B9Ui6IfPTe4nyJLyWu3PzfqKJYuqMdkSpNk4dEPUJxWYE4CNgoctuBGIAnUrvqi8uTgGvvUeolCZha_32pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AZG1GpIP5yNp1ViB_UOUca9RwUMlexvOHP3d7gv1BUmXAWAfcLnVBT5r3Y2Lzk8HnidaMmmXbt8GMaWALB9L2suZTnPw37-9j19OAAkbI4nJtkQ3uLpuc3k4zaagCR0UmabPeqFrFQ8BKVkkjzuaPW6gketIbefre_-3c11BS-sA6WwB7VNhzNQUM17mUz0TscRhyqYkLKSa6fAuSMhfbAgC9kIsyjt-CZdKPbzzSxRCZ51C0U9qGQFiRU57NbN3yNj6T7t0Su5KEmgngAfJZi4WFAjZY8RWqxaxcGnq4ByLJss7h9kvn4My8DqkQPYzpAsRgbRvVX5i5Zv0d2SNjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KOgaJ9-WJHw1AlOTuvQoGMcj7YLvw3vy0fC7ectqr7xiEaDsJukNYeIjeYHdhoN3vO7K-QL_woI3DsTpjF58FbbMs-goWTB1Rto9PaiWsmpj5aHxtdAoGJw9FMZcbWXzxbquD4mvy1uYgX7vcvaiPjGBt_NJZEKljzsEREdZ6amJvCkdkAVOUk9d4j9ysl5eK6dU_9jxYPqtk21h5IBKU0p_4sJNM6BMzFvTRDj25hqR4yN66wh9NAspxgj7CiryuxvtAzjIUVRphMlOHuVMmjPMgFVRqyYdV8D8p8fmmDBNXEMHwPU2wdtk82fnDDKnCroZIwHcRtM266oWZDXtig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s7z1zp3UeMxFLufHIowzoRHOKuzJsnCM91oHWC4DCUVVffPBSGx7wm-g6TP2e87roqt9ns0ZYgtLn2t_tztJXWjx08B6UP4l0k4w_T1UlgL1mCeoYXRknrVa0H45H1COEQYAK3YSAiqKjQ-cxH_2bS2QAkWjiexLlFKjN285tMElOHwhcjSqnfXopV5YBQpI7YXePJnLSWGNXb8pjeQQFDEULTPOE6B9NqJCL4NUpmvXHHBDSqJhpSiPC8xrJdTt0rcEFgcmPo6U0dQ1WzZidiwUxddehYP9vmXQ7Vhqr8vAYgDmTK4jPAnQ6qA2AF4U7pBd4H6TvjMvF3M299DCCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پدر و پسران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/100544" target="_blank">📅 21:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100543">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQBX7Vs0CFUNWYWGOpxwHXRCeht195jS3UuivhHKvV4y6gKEGh_mkhwuMoVS6lfCLuI6qSDPtSes6skAUwYviXWPOXvzRMQ9sBrIjAXsUcpyruoSV3hJiaV8FRvUo1EpZkG368nfVulAQL6q4Hm3I2AUpikq5xI9ccTD4J1Ot8_jv3-vbxsQptwZZzwMGs7LxRLADjOGd0BdhUCXyj9GUx9alMs9pvyYNs_Zqg8SF3rAyGtIRRBB1Dp31V0GsG9suP0vFF2KjLrsIbQ8doLIp1YNgpzL1-yqCaeCwNaOwFdtXTqBiMoA2rp-D3Su585jtXBBFXIOjuygbAwgAE-Lpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
اولین بازی‌های زین‌الدین زیدان به عنوان سرمربی تیم ملی فرانسه:
😀
ترکیه
🆚
🇫🇷
فرانسه — ۲۵ سپتامبر ۲۰۲۶
😀
بلژیک
🆚
🇫🇷
فرانسه — ۲۸ سپتامبر ۲۰۲۶
🇫🇷
فرانسه
🆚
🇮🇹
ایتالیا — ۲ اکتبر ۲۰۲۶
🇫🇷
فرانسه
🆚
🇧🇪
بلژیک — ۵ اکتبر ۲۰۲۶
🇮🇹
ایتالیا
🆚
🇫🇷
فرانسه — ۱۲ نوامبر ۲۰۲۶
🇫🇷
فرانسه
🆚
🇹🇷
ترکیه — ۱۵ نوامبر ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/100543" target="_blank">📅 21:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100542">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsbaQu-kYKY5BdIBFELfcp9lbZcv1LqejPXzUD-BvbmnKS78eApfLD6NfFpos3ZEn9khi-0dmrzvNvzhE1bGFC7n_3Kk9B0DkzAUIC4VX1hDOxnIXo3Sgm8jB1kcSkh0LPds2BYiWTF6hgoKv7y-_m-4lVTQ6x_Wsb520lCvxdFkAVN4MOpsifUVPhwaa8rQHvec5n1wqwueHV0crS3j97DydrfQk_l7hwpUngDmX7s4T6ETSwRV4MtqvHFgU_E4WiWwjn4cw-u4dWxqRANUPEZZCfIBWOPkkUsD1nnC46Quc92218Nbeg3D3xvL7DF-hP1OTcmPD21-2m3Raxx5nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
خبرنگار: چه تیمی قهرمان جام جهانی خواهد شد؟
🎙
گواردیولا: بنظرم آرژانتین قهرمان جام جهانی میشه چون حضور مسی در بالاترین سطح آمادگی، یک مزیت بزرگ برای اونا به حساب میاد؛ مسی همه چیز رو تغییر میده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100542" target="_blank">📅 21:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100541">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b0ffa0ac5.mp4?token=DBjs-n6yIBclHkYiY1CUDbu_8Qs86q_6pl7g15lhj7Y3nobZ6qNfL6vHS4To05ykohr4Lca0npo7rmoyEbmn54YOUlGj9v0lQPXeWRL4ZhzY4m36kXXg4vWweNBveLnzY3s_uTqfYRIg8CWXfK7EVkvzr8JObLcOejoAnNcYKYHH6SDgarrnqQiKU0Yh2KW8pXuUupt4Yd9XYU6OwqyjTZlEuA0fuOItUovaIy-WtMlaSJA9hF7FYrwiWmg34Pg78asfbTdXoinRX1GqAU-gB4CCr7coxBq_TTKewfYO6mr-JX9admGsJGYAJTMroF4o7pSqGYcgUPTlT8gE_nlRpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b0ffa0ac5.mp4?token=DBjs-n6yIBclHkYiY1CUDbu_8Qs86q_6pl7g15lhj7Y3nobZ6qNfL6vHS4To05ykohr4Lca0npo7rmoyEbmn54YOUlGj9v0lQPXeWRL4ZhzY4m36kXXg4vWweNBveLnzY3s_uTqfYRIg8CWXfK7EVkvzr8JObLcOejoAnNcYKYHH6SDgarrnqQiKU0Yh2KW8pXuUupt4Yd9XYU6OwqyjTZlEuA0fuOItUovaIy-WtMlaSJA9hF7FYrwiWmg34Pg78asfbTdXoinRX1GqAU-gB4CCr7coxBq_TTKewfYO6mr-JX9admGsJGYAJTMroF4o7pSqGYcgUPTlT8gE_nlRpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرد شریف روزگار
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/100541" target="_blank">📅 21:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100540">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">فرم هایی که چنل های دیگه با اسم vip ماهیانه 2-3 میلیون به ممبراشون میفروشن رو شما بصورت کاملا رایگان میتونید تو فاک بت دریافت کنید
💸
🫶
فقط کافیه ۲۰۰ هزارتومن اکانتت رو شارژ کنی و با مدیریت درست فرم های یک روز فاک بت رو استفاده کنی تا نتیجش رو ببینی  @FutballFuckBet…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/100540" target="_blank">📅 21:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100539">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Stg69w2A2y8CH3l6U7O78Zgv0qLWFJkgU-yE0Pkh3WIizoyrIdgWb2mldFVXAlH-ACFIEQC81m9OKI1M25qDlgNPGL9ZiXjbX0DRB9el1vEvOjeaCzg2jE0_0LLEN7MjXZKLz9oPR9bKNFHb_1vX3C8WMATZPU-Trb9foNSoZgHkHAaRlB8fYfZ0AcIk4X9MNFKHflraU9Ox7e-zMIUGEcsFjMf9tBqQdPslxXo_cKGfqV4F3Li6GujNJXZkPdI6zzp5ykRtgH16whRgD7zBNTtWuLNxFV5NTcgBQ1cIqd1k-QgBLIm0bpCAKgU9YsKfOxTA5OAMo4rnBEStGXH1Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرم هایی که چنل های دیگه با اسم vip ماهیانه 2-3 میلیون به ممبراشون میفروشن رو شما بصورت کاملا
رایگان
میتونید تو فاک بت دریافت کنید
💸
🫶
فقط کافیه ۲۰۰ هزارتومن اکانتت رو شارژ کنی و با مدیریت درست فرم های یک روز فاک بت رو استفاده کنی تا نتیجش رو ببینی
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/100539" target="_blank">📅 21:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100538">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkJCsgwdyG5f-Y-ZbHn9HU9-yX0l7nF3ccSxco2jxH633mu8fiEIyh6a5LgL0JBRIhrQkVm-tHhVQzTDjNM8IiX2RGKisLoNYQEQbyhMdCG7aB8-hbgE7H1CNYVtCFJqubuwJ4qPLQDbc5ZM3e06eFHXKhgMoNSSBpey0jW8EDqGgFjAl6-aYPBDXuMvp7aIRmgCQ3YTjUxviCDlztdSZzohLuY9KwcQHHGnzkrYiCCHZn6Ww-hohssdl83dG2e0M_6vcfY-mAHer0e-R71X8-ykiHCz-Fguyrrhhd-vENDbrdMonqP6iT1iZRaJEzvYg50B0k6KZjQBNv19A6jASg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
🇩🇪
#فوری
از اسکای‌اسپورت: اولیسه به بایرن‌مونیخ اطلاع داده که در این باشگاه قراره بمونه به رئال‌مادرید نمیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/100538" target="_blank">📅 21:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100537">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMZSFlhU2IPww48S1q1_xeKN9YqQd3liocKgcsqrcpafj77vENRjr09gZlDq5icqUl02CLbTXZ_P8UhDHHjIK4soKhaCvRzcsjKhA_YvAXswiPSZBB1eR7R1EnZh_Gvv0lXQmSlz7s7WXmQM2Gv2cZnYY-KgeClzA90nl-KPx0GTeRFweWGxFzG6yYGXsC8ofuDnaY6qoVvWAM8GHNBszX6ZdbiBAttnRSPl8qZu8PsVWEeSbMImobWYhPiDANYYVzUCCTnFa_UFkyxNPfwjSxeTNfdEYouoTyQ57TPBDUUJ6DX7gOC-cdz3D_WetWZbM5uVUnj7lkdu5ObPQW94iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
یه‌کم جمع و جور تر بشینید مهمون داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/100537" target="_blank">📅 21:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100536">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🏆
🇺🇸
سخنگوی کاخ‌سفید: دونالد ترامپ در فینال جام‌جهانی حضور دارد و به تیم قهرمان کاپ را اهدا می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/100536" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100535">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/378abba176.mp4?token=HlJiwO4Fy9qIyT17P5wF_Ccwut5MuRxKv6dhE1Yzq-PJvW0J61SoLBS4PGV9HuU5L8gcZ1_gYBCvu7iHSPD7ggIFCYSJH09SKBX1RXcLw9dCPOWQTieU9FNjO7VhR1bwVSJDg1k0pEhUq3sZpMNjhB9iNBpBcQ0Nxm2eqjDGiF6FVkHWxucGFZsHw4c3sWwpiNSfCMU5q1wdOUKzOVwxaZdQgsM27U3AFTWjKZ2o_eg2BLrJ2VlZ5pbSKEzIgsqWA2KE7JQgC3We1eVYORVrld6TEOKRBWdIXBx0TKXs_xrgkkM497HJmjxzpn4k2_uQm11v4aU36yn8C-hI4PFP2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/378abba176.mp4?token=HlJiwO4Fy9qIyT17P5wF_Ccwut5MuRxKv6dhE1Yzq-PJvW0J61SoLBS4PGV9HuU5L8gcZ1_gYBCvu7iHSPD7ggIFCYSJH09SKBX1RXcLw9dCPOWQTieU9FNjO7VhR1bwVSJDg1k0pEhUq3sZpMNjhB9iNBpBcQ0Nxm2eqjDGiF6FVkHWxucGFZsHw4c3sWwpiNSfCMU5q1wdOUKzOVwxaZdQgsM27U3AFTWjKZ2o_eg2BLrJ2VlZ5pbSKEzIgsqWA2KE7JQgC3We1eVYORVrld6TEOKRBWdIXBx0TKXs_xrgkkM497HJmjxzpn4k2_uQm11v4aU36yn8C-hI4PFP2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
فنونی زاده خطاب به جهانبخش: اگر تو ایران بودی یه تیم دسته چهارمی دنبالت میومد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/100535" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100534">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47fe3526bc.mp4?token=TMNgy4oHvA772kO0OdomNT-9Oz0nu7jrrPVfV6-XqrVyBGQ5M4h756jJvp62rnP2lemEe8kM4J6crGKTyAfJ7bHa7FBsUxIFPndnJJ-8-7CErUVbxk1x2y-lKDUMGwvNd6E_SQtc6PMXFyevdtFAyp5DUmJYURlu2PIo2j5NxMpQmyKUfH05IqyCSYg0f1VlDyKJgepdhGO4fTeC6u47qUHVYwu92Tx7pBkYyGf1U8E1ehGiJJoy_WfBS-znMHrqzROPciCMVaeZF7EQ9LRlhrp6EVtcAVzRrAyrfySVvW75F90YiQqlnbzYSC92AYNqAbtPw_sqVtP1oPKpFP20ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47fe3526bc.mp4?token=TMNgy4oHvA772kO0OdomNT-9Oz0nu7jrrPVfV6-XqrVyBGQ5M4h756jJvp62rnP2lemEe8kM4J6crGKTyAfJ7bHa7FBsUxIFPndnJJ-8-7CErUVbxk1x2y-lKDUMGwvNd6E_SQtc6PMXFyevdtFAyp5DUmJYURlu2PIo2j5NxMpQmyKUfH05IqyCSYg0f1VlDyKJgepdhGO4fTeC6u47qUHVYwu92Tx7pBkYyGf1U8E1ehGiJJoy_WfBS-znMHrqzROPciCMVaeZF7EQ9LRlhrp6EVtcAVzRrAyrfySVvW75F90YiQqlnbzYSC92AYNqAbtPw_sqVtP1oPKpFP20ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🏆
حضور تیم‌هایی از قاره‌های آمریکا جنوبی و اروپا، احتمال قضاوت علیرضا فغانی را در فینال افزایش می‌دهد؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/100534" target="_blank">📅 21:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100533">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_v5aRMdESC3yCzVNl9ez2bL4_LNMgIM11IktAzH49akAkec8b2habtnDNtFJ6mbVoWVFB_X2XID1qINEHFSw8qATCGf5y7yBJZko1W8fd3G1Fa8DTUkD9crTetRpIkEz0XCFwJHiw_tKx25uuINHSozBeM5Vt0DDg9img9cr06OTvoSM_WALopZ-13NI7gvRdvYdDvIKauGeMOif1Q57sVe_IKkmUYEQi6pnjRUd3v7nLpRJFS2lWyd4_SsbbvnukvjJ-uTzegRByPltB4dDnepB0kc1NEQb4-79gcJNINnoEkVVbZZN4I2D-aEqpvx6HqgNT9cZDsr-J6ijDzMXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کپی ترید خودکار
— فارکس و کریپتو
⚡
اجرای آنی
— بدون تاخیر، بدون دردسر
💎
رفرال
— با دعوت دوستان درآمد جداگانه داری
💻
پشتیبانی ۲۴/۷
— همیشه در دسترس
🎞
آموزش شارژ حساب</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/100533" target="_blank">📅 21:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100532">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/735694936e.mp4?token=u_490RV4x7nWPzL_Ae-yrQyIZLzeVNou1cF1RR0lNNKSKh2_dEbuf07dlLpBxX34P9aQTqspVo9jDW0-5YdI6n4W9U5E15LnsOoMjugOCDx8HUPaPvLPHq5m-PXQPMrg_1r7DzQLVfY0LdF9p2aVGJNXNz_h6ve820p3vu6e10-U4uAte11FrKnjA0n99iCiwrraoTV5c-SygUP--H3H2Ri6TVmqdwm3g5YB9u93-jlG_gcof81IarjCOWinYuC4i08UwjAK3wrenWRoyAqiUzVwpkCPSCzBA8xesckHLFRZKU6rQKqLPtrqlub3YvFdVQcLoxHZM-ehnzh_u4HtFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/735694936e.mp4?token=u_490RV4x7nWPzL_Ae-yrQyIZLzeVNou1cF1RR0lNNKSKh2_dEbuf07dlLpBxX34P9aQTqspVo9jDW0-5YdI6n4W9U5E15LnsOoMjugOCDx8HUPaPvLPHq5m-PXQPMrg_1r7DzQLVfY0LdF9p2aVGJNXNz_h6ve820p3vu6e10-U4uAte11FrKnjA0n99iCiwrraoTV5c-SygUP--H3H2Ri6TVmqdwm3g5YB9u93-jlG_gcof81IarjCOWinYuC4i08UwjAK3wrenWRoyAqiUzVwpkCPSCzBA8xesckHLFRZKU6rQKqLPtrqlub3YvFdVQcLoxHZM-ehnzh_u4HtFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی وقته دنیا یه خوشحالی از ته دل مثل این صحنه به ما ایرانیا بدهکاره..
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/100532" target="_blank">📅 21:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100531">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QK7zNLxi6p76DWbo90OTvQCLHC4E-xeawdwWlnbcYYxbW_MIe_Nv2kGOwcOSUsl0BvpyHhLe4oiPc_Iu9PJ8esNnMyQSMk8Ae6T65xePfAeaYMnpKSxCaVNIGPNiLOlfa2dwPZKNLVSOptpRJ-7ZzLmtQcvJNIlBmgEJ4JgY560wgH7Eol2DWWltk122yisP9tuoCY5l3hldqABDKfoVerLZVLbu7gBwUd1rFdzrMSWw4_NPDqIDknvPi0KYLEiWKsbVmF8LIrQV5nrAQpq-GOiBLD-mhWBCI-mDVydDvYQXb_jFibhi6lS6L7OSUjylPTnlc1FYGd0Bt8Ly4xU5zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو
🚨
🚨
🚨
🔴
کریستوس تزولیس از کلوب بروژ با مبلغ ۴۰ میلیون یورو به آرسنال پیوست.
𝙃𝙀𝙍𝙀𝙀𝙀𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/100531" target="_blank">📅 20:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100530">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0Sj36gVd0FjZiQyJEf61AlCXTgKEvxcDAmjY67S8SxWvSbjB1GYP08pV0g1GqJrwNsOOicnUpBKcdOaWL1GvvcDakqVkWEUG2XEiYejNHlgk_KSTyqKM198n314nP9dDDKGAriulti52B16o5s2RKL9AXUHz2d8D0Nt7NviYQ0c0xn702K3vvus6TPqndHCbHbUjQ8jjN5acthFCwqqNlsVpWa8QquBiHNug9Pe_TFObvdo2yldzD1IJwE73-1zFFIG9CBIcqfWqkWCLHzpoNVoLknyXxTebwLrI4zkNNJnZE2i6fQjLt44EMb5I-t6cxo-0ay_r6pyaE5lgh5byg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
لیتان، رئیس باشگاه لیل:
🔻
ایوب بوعدی باید برای یک فصل دیگر در تیم بماند چون باشگاه لیل در لیگ قهرمانان اروپا شرکت خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/100530" target="_blank">📅 20:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100529">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">لیگ ملت‌های والیبال
ایران
3⃣
➖
2⃣
آلمان
🇮🇷
25|26|18|25|15
🇩🇪
22|28|25|20|12
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/100529" target="_blank">📅 20:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100528">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec19c4e50.mp4?token=WZ3XT0eZYqWWeyCiCBjw4dUhcKrMhe8VSrMvTae8mNiLVOXzyrW4o2zzgJElDracvgIRIGdtiBI0q5NvORYOOmTnFigBaWCBzqvTcsfR9VCe194B1Otv4_UwkJqz4HtV8ik1lFRp5fkP82kKrxBqOzgUIJDWymak7-jv6AAAf2SjiU5zcliQa_nlcpLTF3S48s2FuwZF5a1HUUwu9MRbC3G9D5irZTnsiX9hbu4Jhds4FnUEC3vwSQEf-w_UY82xbS2L2TcYW2zJd7WzUALespOJYn_iqrOA5bGFu77B97JPDxoNmJ2n32CPTCO4Ke0eiHM8SFclPT6L-Jvs5ybwOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec19c4e50.mp4?token=WZ3XT0eZYqWWeyCiCBjw4dUhcKrMhe8VSrMvTae8mNiLVOXzyrW4o2zzgJElDracvgIRIGdtiBI0q5NvORYOOmTnFigBaWCBzqvTcsfR9VCe194B1Otv4_UwkJqz4HtV8ik1lFRp5fkP82kKrxBqOzgUIJDWymak7-jv6AAAf2SjiU5zcliQa_nlcpLTF3S48s2FuwZF5a1HUUwu9MRbC3G9D5irZTnsiX9hbu4Jhds4FnUEC3vwSQEf-w_UY82xbS2L2TcYW2zJd7WzUALespOJYn_iqrOA5bGFu77B97JPDxoNmJ2n32CPTCO4Ke0eiHM8SFclPT6L-Jvs5ybwOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بلینگام، درباره بحث با مسی:
هیچ مشکلی نبود فقط داشتیم درباره صحنه خطا صحبت میکردیم، خیلی شلوغش کردن! بازی کردن جلوی مسی واقعا افتخاره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/100528" target="_blank">📅 20:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100527">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f42b6ddc.mp4?token=G5zIT3nfk9jtnu6KsXyVLUDLN50jQMNhOprP-CYbadA-4ov4qzWdVBTCSk10u-oRzBkJOk-gDHtObLfJjYOQTL51xicEkc_NAMkLkRtRgKmOyAO9WfHAq4fbxAKA4dPen24FMYxmZFP5w-1aFAluIHuXnN-_uRQXeIp-z26hfou6ClCtITLhx_SCCkGVUHy3yTEE4SpdrUTYMNDcGv2f9Vdocx5l7UFr0msf6jb13B4_abcRLkN7JSEKE-uepAFoV2qWoTOU8yB8LR8AnIXNgzkH0FA-ANsnD2WbjdyothVHBKU4InrUMvov-ffwbAm1IVugK2_Ct7VB0DEFY0RYW6mytht2do-_M2sz8KSxFJNRDDacvwmlE-xX5ln8GITeXvUnB36DaTKHkBVQ_Pb0YTcaeFK6F39FY6pQ2NUitiMZ108kGXl1XRRQuyyMVDN8YeVW49oLipsIFUkvSA8BwxeoMOym_bw3-oPEkUJB2mbulJ1iXj6hAtpSFOgb29bo-y1xlZ0uFwWRQ9NBZ0KZaKCn8Zc-ZtsRsyjPMtI8hF3MelMdBmGGgVuwh32_jTfI-OVq_54pfKRYXWlOCgYMgogYMZEnMHDCVSkBf0lTdH-3frjwW1eC8dBg5CwkpGQHuryf3da_cffzKVniGytGbisuwiFQ0vyoDDkfugHiy9k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f42b6ddc.mp4?token=G5zIT3nfk9jtnu6KsXyVLUDLN50jQMNhOprP-CYbadA-4ov4qzWdVBTCSk10u-oRzBkJOk-gDHtObLfJjYOQTL51xicEkc_NAMkLkRtRgKmOyAO9WfHAq4fbxAKA4dPen24FMYxmZFP5w-1aFAluIHuXnN-_uRQXeIp-z26hfou6ClCtITLhx_SCCkGVUHy3yTEE4SpdrUTYMNDcGv2f9Vdocx5l7UFr0msf6jb13B4_abcRLkN7JSEKE-uepAFoV2qWoTOU8yB8LR8AnIXNgzkH0FA-ANsnD2WbjdyothVHBKU4InrUMvov-ffwbAm1IVugK2_Ct7VB0DEFY0RYW6mytht2do-_M2sz8KSxFJNRDDacvwmlE-xX5ln8GITeXvUnB36DaTKHkBVQ_Pb0YTcaeFK6F39FY6pQ2NUitiMZ108kGXl1XRRQuyyMVDN8YeVW49oLipsIFUkvSA8BwxeoMOym_bw3-oPEkUJB2mbulJ1iXj6hAtpSFOgb29bo-y1xlZ0uFwWRQ9NBZ0KZaKCn8Zc-ZtsRsyjPMtI8hF3MelMdBmGGgVuwh32_jTfI-OVq_54pfKRYXWlOCgYMgogYMZEnMHDCVSkBf0lTdH-3frjwW1eC8dBg5CwkpGQHuryf3da_cffzKVniGytGbisuwiFQ0vyoDDkfugHiy9k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی دایی: «ما شکست خوردیم، به چیزی که می‌خواستیم نرسیدیم.»
کریم باقری: «همه طلبکارانه صحبت می‌کنند، در حالی که هیچ دستاوردی نداشتند.»
عادل فردوسی‌پور: «چرا باید برایشان مجسمه بسازند؟ چرا باید درباره استقبال از تیم ملی، واقعیت را وارونه نشان بدهیم؟ ما هیچ دستاوردی نداشتیم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/100527" target="_blank">📅 20:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100526">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0o6ld4WSEXv6CIpR__BCQHNhrwPf3qgdAQOgrJ-_AyCdT25rUUFfp9hpb8OjqG2nKj9FeHRMECa6Td2fyGRvcTJfzdcdDa9YB9d5HGGaJjGRIvcjLtqswFymFsV0QSxdySBLy9jNRmJD6CmqGzGvHz4pIKuq2eVAZ2uTnnoD12bIFSjC8bghbimGG218qPGEalo8hSi3UWf4dhiCIPgZo8O2Ty84X9eXKQ3aB0CuAmyMDtgf37tyPOgQgWKBb7MV8Y_vH3w0jjvIIlLKztuxd8CnA-5KhkXoxlKKrT412fim5JOh8TXmKg2JMfhLm-xhz1JHfc_iGLh3jlFu7AjoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">�
جدیدترین پیش‌بینی Polymarket برای قهرمان جام جهانی ۲۰۲۶
بعد از برد ارژانتين در برابر انگلستان
🇪🇸
اسپانیا:
۵۸.۱٪
🇦🇷
آرژانتین:
۴۱.۹٪
حالا نوبت توئه؛ از داده‌های بازار ایده بگیر و پیش‌بینی خودت رو در
Betegram
ثبت کن.
🎁
۱۰۰٪ بونوس رایگان اولین واریز
⚡
واریز و برداشت سریع
🏆
بهترین ضرایب بازار
👇
همین حالا ثبت‌نام کن:
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/100526" target="_blank">📅 20:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100525">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yl6enk_XjEMuFaNqJGk3A4DXuP3ko0SMcRAi7E3jz47EceX4ckNFXQ2yEROMRYNwMK4-afHtgXm-E5fiFI-oMipXg0WUrbEiCiInjYfp_N5blWbR6fLruOqzIUtTjtrygIaRmddXgmHIzZHvY2z_5KcJ8ufVeAPO17Lsg6SmrDdaJALedfvAOlekZS8LnlAkJZr6NySHLHexTfZQxhBbvWxcBxyZWj49xKh3QDDQErty41EUVuvG-pmT9N9vUjxzwfTLlTpkV9INf9VaasQHiqTsyirhXqfaWWoULMciHeaXZqiR1jnrGDLviQhtea8te7ZM8Up0uBbWwVlRw8PdKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
عشقتون تو تمرین امروز تیم ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/100525" target="_blank">📅 20:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100524">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d68c789aa9.mp4?token=gxa_6H2QDstlPShpKMrAEBjbn8ikz25uWUBLZxXSsd6xQj-rTS6O3y-n6lufhywiilGuQQVl4qmsMzILw0mYJVH8vPIHP_qt_zLVoyXSKV0mdh5z6Scql2wMSLARiA3z74RddAPrEoEMvsy4VdOASHg8TbAv2C8sKPb4yr92FRIG5_EI3rS6-aoRZn72HTPRLsNPJ2TpoC4fsHCzTiu21jIK9C1SFEG6jhpSsXAAoZhx-NtTVAZx9oI2qyzDMI1e7wgylGchXLaDGpN1QMVHx3Z7R8yqjBH9qP-Ab3j4YxsrwlJgNMNR592Q0H2I1XTikgPPZgqFOVxVzKdp7-12CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d68c789aa9.mp4?token=gxa_6H2QDstlPShpKMrAEBjbn8ikz25uWUBLZxXSsd6xQj-rTS6O3y-n6lufhywiilGuQQVl4qmsMzILw0mYJVH8vPIHP_qt_zLVoyXSKV0mdh5z6Scql2wMSLARiA3z74RddAPrEoEMvsy4VdOASHg8TbAv2C8sKPb4yr92FRIG5_EI3rS6-aoRZn72HTPRLsNPJ2TpoC4fsHCzTiu21jIK9C1SFEG6jhpSsXAAoZhx-NtTVAZx9oI2qyzDMI1e7wgylGchXLaDGpN1QMVHx3Z7R8yqjBH9qP-Ab3j4YxsrwlJgNMNR592Q0H2I1XTikgPPZgqFOVxVzKdp7-12CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
❌
لامین یامال در تمرین گروهی اسپانیا حاضر نشده و روی ران پای چپش بانداژ دیده می‌شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/100524" target="_blank">📅 20:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100523">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJoalgr23y3MGEpmuhyBtoMXUdEKCimRXSo-yIZR7u4wsf0kLOFNz8zNs48a2OXvhiI5v2l8nUcK0xl50znOxlKu-oNW9216SL81XwWG78JM74oQsX6m_Xck-j6vp-cOrLlgJrjSgUHZTOzbp7B7pqxqF57CREGqmMq1H6CIA_iAkcCd8mJROl1oFg3s3hkrWH46Jl9mcwpYDCapluY0VXZiJq1AsSOjTN6KSNB4D8RcfjLEPKKk0d24TH5BOEaQKcElMdZFow_Vszw1Ip-PbxyeNrHOVjqz0MRbqo7mahMbQD9Qfs4E-LCe6LvwgVLBEqUzkp8PNsx-txIUxZcNzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
#فوووووری
– گل
:
رتبه‌بندی ۵ بازیکن برتر برای توپ طلا تا به امروز:
1 - هری کین.
2 - اسطوره مسی.
3 - لامین یامال.
4 - مایکل اولیسه.
5 - کیلیان امباپه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/100523" target="_blank">📅 20:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100522">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aV2uBiS49ZqEW-yeuOVJFnrX2QJdfh4VzzJLY5CHw6PS_QwEbC-8_1QC2OeIoJRiEgABgUg_EYnTRQv6Aik2hxTRGTqPA46MmPi5zhj2wmkUK17GjNDOeRTsLdbuCNDSZ43qtkIGdU8iVYkJE49WXkAj7KWqtItPKoI9mk4Q2ZANrLd0vx2yw3J8YidtaWIc9glOVJatX_niROM1FBHGWC2ZMTOTPpZCO-gZD4s9K5QdPnup2tFBe70RUEfGDu27mYkJh7cDqQNuJgmDun5zUg36iP_ylkmbgUobBNUKt_b2hXJKZ6XnMbGrDoAgajdnILQuaxN3K6CfcVkAfaVA2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📊
🏆
| مقایسه آمار لیونل مسی در جام جهانی 2026 و 2022
غیرقابل توقف
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/100522" target="_blank">📅 19:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100521">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62c9ac7d18.mp4?token=n40QR7uGIzUiI_W-hUM5jVzRxPSLsYCURi7O5T7zz-vF-v24-QtFN3dt1W_yfcZtcwZv6e3suqwaTBt4uQjzm8_3tX7blgEgNNmSCSIwUbTQDoLW4NJoaIOKzvFjrWeQbJN8Tk086SZIa0Opit4-v9YmrVwfPTjcuZQTib4-nj4Ms407TXmWgqmSbVXSsNRDrsj_AvHs2UwiM6VQLyaKlwYMXwVgp43phx0bRP3ALZMSZdXLJWAsULk09fcPpWqiYmjkXqzI56wufygko0iT2bsyWQgBQk_x2vbG7dU-nQ_jz2343t7Le_ipdwffHEUpP-Qmn-nE1boI07WIED8kTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62c9ac7d18.mp4?token=n40QR7uGIzUiI_W-hUM5jVzRxPSLsYCURi7O5T7zz-vF-v24-QtFN3dt1W_yfcZtcwZv6e3suqwaTBt4uQjzm8_3tX7blgEgNNmSCSIwUbTQDoLW4NJoaIOKzvFjrWeQbJN8Tk086SZIa0Opit4-v9YmrVwfPTjcuZQTib4-nj4Ms407TXmWgqmSbVXSsNRDrsj_AvHs2UwiM6VQLyaKlwYMXwVgp43phx0bRP3ALZMSZdXLJWAsULk09fcPpWqiYmjkXqzI56wufygko0iT2bsyWQgBQk_x2vbG7dU-nQ_jz2343t7Le_ipdwffHEUpP-Qmn-nE1boI07WIED8kTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
کل‌کل بامزه دیشب عادل فردوسی‌پور و علی‌آقا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/100521" target="_blank">📅 19:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100520">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBmq_TSKjoPIjU3xwv-DjxPyS8gCHTWVFNGD8IPGaHw82jvZvOpivVjwNN6U9HGM9YFeP6Bpy-M2C7qWMCP0GmC2PjnroTu9lOsk46hM1K6y7HplAWW4dZ7-fDpaJ3KyKAckJDlJw5UN1R6wbkunT93H1oDx0GoW9FVaq2DzMzI6NBCg_VmjAgv0KB52yi-_DWIsNPqb560kCzhwGkp9Mly1V2TEBj7L3ASSnSavHZJKtDIiJxCtbyl3F0eTTYT1dDbXAV1V6lfXPbcspoizhLTYMHtL66aLFDX3B_fSqRO5l6tS8wgYQ1I8egOgzLI4Kf5qpJx7uolxIKk_nAcGUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فابرگاس و خانواده قبل بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/100520" target="_blank">📅 19:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100519">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScyYSLAP5hZugljKPrkqhfBvH9c5Pmxek9j9yq24V52Barq2Z5BR6MsDSR2g_4CKfvCk-DKE6oLoQB2mz8BKWsq5IaCPFdYkXOPsv_XxTW-eYLYjbo_BM-KUbVcoI5sUgDdq9qahbvufZlBolidEPeAdtrZZ4friE_qekMZFtSYm-zcVQCWW_vQpLU6kAw7gwoK5BzrenjNukJ3LETbJ609flXk89Qf1oQrqzbEa_jwYoawZRkg8CbRExltLn8JBFs-e_poq3mTmrSQWx8gObdM9NaI2Z6UhQzLVyQT1_Tmvp6aEiBXWee8njweGMqm1RuaRhQnyXwygKsb2IReBxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیت اول آتالانتا برای فصل بعد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/100519" target="_blank">📅 19:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100518">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kB9Yms2Q7LuSuf5oGqCitjta3DCXBHhaVdXWrJNmCr544Xq0X0wXY85pTp76Aa-g29NF0kzIhe7pYX_Ke4i3oThc_wGe3eAOISZH1LfLJd_C3zIiWCCaHUHk02QrtiSRc8qZW-J7TO8uy87sxq_rLmPcdZpMm7Y3c8sUnzwVIxtxnXddjVAFAf4ZF-H_NGn-McrYTL8Ikas2P5F_lExiFc7cRrHckhD4GniMj2BfKNxytX6rtH2BmKr17ZRgNQSf538VkRl2FU8xXp_L2ko9Qkb9o4PLPWZ9E8kptDums437qPKr5FSSwlCNntWyi5tAm3gVWGwYG170diYnIc79tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سازگار با تمام اپراتور‌ها
✅
لینک ساب اختصاصی
✅
مناسب برای گیم
💵
20 گیگ — 120 تومان
💵
30 گیگ — 150 تومان
💵
نامحدود — 200 تومان
📣
همراه با تست رایگان
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn
چنل رضایت مشتری‌ها
⬇️
@kavianivpn</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/100518" target="_blank">📅 19:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100517">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtHmKQmVyCL66rfTuUYW8x2B8B5lPPIHQg41iDDjAeUlD244XhkMZw-HTSVZ7JwkSYgRRDmJ2OfSiXEyTewqIKbnnnEdT2UzxZGwEjlQwkcrZfg9ZPGEX8ojFE39O-n1tTJYLrCM7J0D9Au9d0ZQhqqEZJWttOLKcRMAeO7HHrYwpABDtQDyKhHn1AxHDS9YZrzBvWjg-UYSJTyq1E_0M5KYxWFBkz_auxACg66xiaCgMOh7MiT09sk6UEUCKooe7Adq8FdE8dsL78laIsPPMm4ORNBg5k27_JfGo0L6d0Sq2F8zwtDsujKq3U5YEJ9lKQufEV4Vt-Oa41Y_mu0j_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
استوری رامین‌رضاییان که بنظر شاهد جدایی این بازیکن از استقلال خواهیم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/100517" target="_blank">📅 19:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100516">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjfD65xnX5hAoyrFKAW6Gow_vksIHVbMlvOpunO5ExwdkQ1B6yvyDLKOBHr-eX1-kdHLybY3fwSDcaoNLX0ZdG1LvOWfqgS0164OsmVYQ_PMwClyRB_YlR05m3gLZo39yBlqdQSpOrHPMNM_72B2bP5p4Xsy4seCFPvUHdHlU7Ldl_amXblLClfE6SH25kw9reM2ocvdMcJGBjZFC0UpHIyGnyRcV6vKHOOauAHAX7B6nsB09OABKGEPdhB9Yvo_UJVTFJnDj18O1QM8hgn5LroeSQhUdvEC25wMpRto01WiDNo5Ll-YgxflFhrMDvcZo834a9GIItvdWuHlpCBQNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
زین الدین زیدان برای یک انقلاب بزرگ در تیم ملی فرانسه آماده میشود.
زیدان قصد دارد یک کادر فنی بزرگ تشکیل دهد که ممکن است شامل بیش از 25 نفر باشد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/100516" target="_blank">📅 19:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100515">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ff7cbd247.mp4?token=NQFHFKUkpvhw2w77QJcsBEdq6o81bsDSq3G7WO9JSJzUIj4CwktferKOP0L8JhwDWxnA9SbbL76sK4h1mIDHaDFN_QKNP9HtWhJ7FdVNHo4iCpHd1f2yjNM-omCNDJ-Jj_41gw8R0onHIXRaFC9nboqc8A_9x4rR_YfNQ74_fOd5GBSAOBOUF78k91mCtolM192-L0PYqpfcIhzPDRhGogKMQql8cLlSgtPNwHmOXzsPIT3PrY8GgWpB2dnuefCC-4Z9VYlLDX3c2E7HRFOrytR0vVrMFMU-zA3G5D0gH-tOyfgISIz7HISQbXKpqf8XoDVyuZHldQeRYmDkVqvIag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ff7cbd247.mp4?token=NQFHFKUkpvhw2w77QJcsBEdq6o81bsDSq3G7WO9JSJzUIj4CwktferKOP0L8JhwDWxnA9SbbL76sK4h1mIDHaDFN_QKNP9HtWhJ7FdVNHo4iCpHd1f2yjNM-omCNDJ-Jj_41gw8R0onHIXRaFC9nboqc8A_9x4rR_YfNQ74_fOd5GBSAOBOUF78k91mCtolM192-L0PYqpfcIhzPDRhGogKMQql8cLlSgtPNwHmOXzsPIT3PrY8GgWpB2dnuefCC-4Z9VYlLDX3c2E7HRFOrytR0vVrMFMU-zA3G5D0gH-tOyfgISIz7HISQbXKpqf8XoDVyuZHldQeRYmDkVqvIag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«قاب رو ببینید... علی دایی و کریم باقری... خیلی سنگینه!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/100515" target="_blank">📅 19:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100514">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QC7Kth06-8nCvEaQYZUruN4ke9h82TmnHMfEkSOjyL8aqQixmG35jtCKZ_BNezTm5NGWYrhr2Q1YjiPuiXIIAinFCSCL2LFBcwuA2MpMjAYLDQZUrhLQvEo6ZbE-wpbBtO0_H_4AASl_IYWtDnsFL1CbUi-BMP9bLsNxwFMfqUnGwaK08pI9iCA1hJnDtMDY5Hj9tp356I-MST2mJY10Q0MsXoADIGbdOgWE474PNN79Vbfp-CfL2GkZGzOOeY-ZfUkZvFBVDDo-tU7gpRQb0_H_8fPL1TcuwwlEMhEuTOWuPyhctTOTe5etCoVoQTGm0KY1mjKTOHxdlVAbYvO9sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمعی از هواداران فرانسوی، طوماری را برای درخواست برگزاری مجدد مسابقه بین فرانسه و اسپانیا منتشر کردند. این اقدام در اعتراض به پنالتی‌ای است که به نفع لامین یامال گرفته شد، به این دلیل که ادعا شده بود قبل از ضربه، دست او به توپ برخورد کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/100514" target="_blank">📅 18:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100513">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/121dde0263.mp4?token=XCBn-FcVhBfV3ji3IaxBM42q5O3lOV8bfOm4PaTKk_lQ30uWYCzGZFRlhSu-CahJsbPDgPtN0YLO94HSSjrQ9WyBm6HeOZUJfmd5kp0TREtAtBUePIsIMei1NVNHYQr8xHlxZAPIS4PFiA8h64g3KDYbIIlrXX-wchal87QfYwUUCXOctZrMJxKCIyIMbT5guLqymDKFgdYyWFIYP2cqFHPP3LyZivCcwPNw97dq8gVQOUTwmJpEGiPB0fbgCnL1C3zVF2e8JuBGsFMPhaK6e-mNTA5slHQ4WyoRtHIexxr96bipzqUT9hd76_5kyIKGpHiVtgil0QxKKGuzHlC5qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/121dde0263.mp4?token=XCBn-FcVhBfV3ji3IaxBM42q5O3lOV8bfOm4PaTKk_lQ30uWYCzGZFRlhSu-CahJsbPDgPtN0YLO94HSSjrQ9WyBm6HeOZUJfmd5kp0TREtAtBUePIsIMei1NVNHYQr8xHlxZAPIS4PFiA8h64g3KDYbIIlrXX-wchal87QfYwUUCXOctZrMJxKCIyIMbT5guLqymDKFgdYyWFIYP2cqFHPP3LyZivCcwPNw97dq8gVQOUTwmJpEGiPB0fbgCnL1C3zVF2e8JuBGsFMPhaK6e-mNTA5slHQ4WyoRtHIexxr96bipzqUT9hd76_5kyIKGpHiVtgil0QxKKGuzHlC5qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
تفریحات کارگردان استادیوم‌های جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/100513" target="_blank">📅 18:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100512">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c73b07447d.mp4?token=JcBk8c_8Q8MickYWsGDmYXlCEv3XEwHhv5M1bDWdDuhW8xUiOG_ELrdnGKG-tXuDTqc4BzU9qrDpUSs7xg1TFPrFU2RGmWQ2Woijn-VHBubQTrtUWqSlcUFDebqeZ66jBA1Rii9otA1ID0iTn5eYTPUlrT864UErc5SuUx4i3EhyRTRpJcut1ZlYjmnHgImZ5Gg8elkYEp6yRMwujSVqvDJbDMgho8dsdF08DPR6yc_Y5lNS4RdPLQI9rkEdJFuS55gCp63gYM8mewVaPEus1qG2YLkokjFfQseOEbcCgxeoI4c69TU448MCOE28Uuv39YAD_zCpIfa6mLtm17TpIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c73b07447d.mp4?token=JcBk8c_8Q8MickYWsGDmYXlCEv3XEwHhv5M1bDWdDuhW8xUiOG_ELrdnGKG-tXuDTqc4BzU9qrDpUSs7xg1TFPrFU2RGmWQ2Woijn-VHBubQTrtUWqSlcUFDebqeZ66jBA1Rii9otA1ID0iTn5eYTPUlrT864UErc5SuUx4i3EhyRTRpJcut1ZlYjmnHgImZ5Gg8elkYEp6yRMwujSVqvDJbDMgho8dsdF08DPR6yc_Y5lNS4RdPLQI9rkEdJFuS55gCp63gYM8mewVaPEus1qG2YLkokjFfQseOEbcCgxeoI4c69TU448MCOE28Uuv39YAD_zCpIfa6mLtm17TpIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتخارات ایرانی‌ها تموم شدنی نیست :))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/100512" target="_blank">📅 18:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100511">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f049197c85.mp4?token=cfnTWgqdzwMj8MaUdiiY0OBA0dbBZiP4MB-ePReraONKQgsXWv4jGJ7T5FKQCZ741wfRGuIux-RAxugyOkJfiVES22LZONzRGSUwP1RrfvcHMgoxC-l-5yn0qY7L5lGodvkZjHiS-mjExKIAFKEm6oTA3JpybkVu-e3ylkd1-LPosXHoUKd7vEECbCtbol6joEtshHMBz59iNlemeNuzBZTi3ErlPOK5MsnGRZ2MUNA7fjmRNR9T02pzBTIZ_PonMlvndxujPuXYe6xZScZ2ksjLDislSti2_OunVLZSt47wzgewiTsFym2fberfA5Qr6X7mrGmxeCzAeY7W53aw8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f049197c85.mp4?token=cfnTWgqdzwMj8MaUdiiY0OBA0dbBZiP4MB-ePReraONKQgsXWv4jGJ7T5FKQCZ741wfRGuIux-RAxugyOkJfiVES22LZONzRGSUwP1RrfvcHMgoxC-l-5yn0qY7L5lGodvkZjHiS-mjExKIAFKEm6oTA3JpybkVu-e3ylkd1-LPosXHoUKd7vEECbCtbol6joEtshHMBz59iNlemeNuzBZTi3ErlPOK5MsnGRZ2MUNA7fjmRNR9T02pzBTIZ_PonMlvndxujPuXYe6xZScZ2ksjLDislSti2_OunVLZSt47wzgewiTsFym2fberfA5Qr6X7mrGmxeCzAeY7W53aw8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرژانتینی‌های دوست داشتنی خوشحال از پیروزی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/100511" target="_blank">📅 18:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100510">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4981bd9a51.mp4?token=v4LEsVls2gx9oGuU9Y5Ye1paRXV1WhQP1xNLqBlXWPMvsBTvPefDmdvnB9tQlZhSlteCELiY-1F8QYkSB4lmYQ3fsvI7Y38UQhGQyAIwR4b5nM7MJS3ovw3z6dOCS9w7PYBHZN7OTNIfSYXrEVXLk38tYJznb9cgIX4CK1NBngbGf8-YoAzZB_iF332FjlbH4cVP0jBcbCAS6mWGfhwZHNPCshvhebZl5E4s8j6bwMSkHnisuKM8s0D00ExSl_yC8_zfm6LlHLNkq4mmDmzXiy_GhWPAZ0EkC5hqiUp-PlOgTrR78sXG1fq7di-DiPSUM2XueuJTe0E5jYCcDzTocQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4981bd9a51.mp4?token=v4LEsVls2gx9oGuU9Y5Ye1paRXV1WhQP1xNLqBlXWPMvsBTvPefDmdvnB9tQlZhSlteCELiY-1F8QYkSB4lmYQ3fsvI7Y38UQhGQyAIwR4b5nM7MJS3ovw3z6dOCS9w7PYBHZN7OTNIfSYXrEVXLk38tYJznb9cgIX4CK1NBngbGf8-YoAzZB_iF332FjlbH4cVP0jBcbCAS6mWGfhwZHNPCshvhebZl5E4s8j6bwMSkHnisuKM8s0D00ExSl_yC8_zfm6LlHLNkq4mmDmzXiy_GhWPAZ0EkC5hqiUp-PlOgTrR78sXG1fq7di-DiPSUM2XueuJTe0E5jYCcDzTocQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
از کجا به کجا رسیدیم واقعا...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/100510" target="_blank">📅 18:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100509">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62564cea43.mp4?token=C0NCOoGe9x2UEXpbvbTRlWN3n4ragUFuiu7jJpomw4gK-fe5NsPsYsdusyyumrWUBB5b-3vNPwrtYZ5TZpxKIy_0N1w0HqV0aD6lHB5ah_Ig2cRMNbA_Vjo91Z7F9bYRPnDQ86c71LyyxTiQ8T1zRUajC0hEJmq52gJTrvDVNHiIOAB9ubwLIww30Qz6r2h-c61DvCkJCTfogSkIEKcoPMb42V2Q3kl5kTdTYbEJ3v-C4DyjGDYt9KItsFzhLkHrzve6Uu2oCDQ_c8bP9oKXFZ7B_kw2N4mSWiAIfyNZhQtiYBphNyLpwFpSfxqywoef961Athacr35EtRZ2Y3LnyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62564cea43.mp4?token=C0NCOoGe9x2UEXpbvbTRlWN3n4ragUFuiu7jJpomw4gK-fe5NsPsYsdusyyumrWUBB5b-3vNPwrtYZ5TZpxKIy_0N1w0HqV0aD6lHB5ah_Ig2cRMNbA_Vjo91Z7F9bYRPnDQ86c71LyyxTiQ8T1zRUajC0hEJmq52gJTrvDVNHiIOAB9ubwLIww30Qz6r2h-c61DvCkJCTfogSkIEKcoPMb42V2Q3kl5kTdTYbEJ3v-C4DyjGDYt9KItsFzhLkHrzve6Uu2oCDQ_c8bP9oKXFZ7B_kw2N4mSWiAIfyNZhQtiYBphNyLpwFpSfxqywoef961Athacr35EtRZ2Y3LnyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارسلو چندسال پیش گفت: ما تو الکلاسیکو مسی رو خیلی عصبانی نمی‌کردیم چون در این صورت عملکردش خیلی بهتر میشد و دیگه نمیتونستیم جلوشو بگیریم! درسی که جود بلینگام یاد نگرفت و باعث درخشش مسی شد!
👑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/100509" target="_blank">📅 17:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100508">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2241a88830.mp4?token=ajqNQoJ0UnSBvmi72HUymJ3NFiUaYsTt__SNV6k1f0JTu1BTcoQ8zrv8_ITTdEifjQGONMDA71onTiwsUNinSNE1GUjm5r_8JvzQNRoosGxzyYGzC0cr8oSNB2tqzrTxlsUZK2ZPPhDchmI7n6K5N-A3G1rO_MIfRiI3NdiQL9IAA2KzuM25pue91cR3Q2gUmpXjAjFGil3zoWweqpcaRtMbGjf65x_YYIZMwlofgkOsbkxiyDQFFPQo9uM6F93Ab8na0vWwHeNfmqQKCnxMOLN9guCGZXyBDrnoD-elVZmVXn8NKrQbtoss2ePBTc6BB03zudhsX_PvYjK1zx_CXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2241a88830.mp4?token=ajqNQoJ0UnSBvmi72HUymJ3NFiUaYsTt__SNV6k1f0JTu1BTcoQ8zrv8_ITTdEifjQGONMDA71onTiwsUNinSNE1GUjm5r_8JvzQNRoosGxzyYGzC0cr8oSNB2tqzrTxlsUZK2ZPPhDchmI7n6K5N-A3G1rO_MIfRiI3NdiQL9IAA2KzuM25pue91cR3Q2gUmpXjAjFGil3zoWweqpcaRtMbGjf65x_YYIZMwlofgkOsbkxiyDQFFPQo9uM6F93Ab8na0vWwHeNfmqQKCnxMOLN9guCGZXyBDrnoD-elVZmVXn8NKrQbtoss2ePBTc6BB03zudhsX_PvYjK1zx_CXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چالش عادل فردوسی‌پور در تلفظ نام وریا
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/100508" target="_blank">📅 17:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100507">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fb09b2935.mp4?token=v3GTqakdpoufWDQJjcopCZ1cvaQ6suXs4UWHMKZsiCEhuXmz17m1KM0jKXJsndvIwqPR8y-hKhggBGGm4t7T41w0HP9HhxXe41NGe6YMcGT6CbhBJSnroIHjSGLYXadvsHD1KnoLIX-zFJv4sqBvc8z2afcGNCRIQs6z_0U3qJdOC8uV4KbwHgF97E5UbNRzeLIMF-YU42EOZ-p9KH9HRZQjiZ0Kvqu7_vqfeTxt7MWRgffKvxwLRzrqKnPZgmOFMlYz5Vk74J_7ZztpL5mTfeKASSFkxqhTbgCZC9DmhHDT8Gh-x9epzJ_Ffja9GVyjBEB8ca5EpShNzEgIjW-YiDU-vzaJUIZkEJYkMblNUcHQvSeTxn2WEq5reRynKyjJfWxXAlW3sX3dqjgjL5S9J9fjHMkzJBUeevpmS8RE6-pCUcdr3z9RNelXRQdXmYMZHZ8qEsIbZ2l0ITjjLgkmNKXRavNnDSZUJjLthoonEBF91413FIybadaNgcNOMS6qlf0T55ReQcGBO2aZg6uprJ4cP8wtMzLbsyaUer_-jBE0s5Oum8nlhZexTH4tJqIuBFzoQWddoP2FKqeHIdv2wlan-yo3sx-D4lA7kuiPBgCc97m0wPmtMhImJvt1Je-nBwVafvRpjA1Zr9vvHvGirkAfxL1dPrt3ovEI4M4MYLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fb09b2935.mp4?token=v3GTqakdpoufWDQJjcopCZ1cvaQ6suXs4UWHMKZsiCEhuXmz17m1KM0jKXJsndvIwqPR8y-hKhggBGGm4t7T41w0HP9HhxXe41NGe6YMcGT6CbhBJSnroIHjSGLYXadvsHD1KnoLIX-zFJv4sqBvc8z2afcGNCRIQs6z_0U3qJdOC8uV4KbwHgF97E5UbNRzeLIMF-YU42EOZ-p9KH9HRZQjiZ0Kvqu7_vqfeTxt7MWRgffKvxwLRzrqKnPZgmOFMlYz5Vk74J_7ZztpL5mTfeKASSFkxqhTbgCZC9DmhHDT8Gh-x9epzJ_Ffja9GVyjBEB8ca5EpShNzEgIjW-YiDU-vzaJUIZkEJYkMblNUcHQvSeTxn2WEq5reRynKyjJfWxXAlW3sX3dqjgjL5S9J9fjHMkzJBUeevpmS8RE6-pCUcdr3z9RNelXRQdXmYMZHZ8qEsIbZ2l0ITjjLgkmNKXRavNnDSZUJjLthoonEBF91413FIybadaNgcNOMS6qlf0T55ReQcGBO2aZg6uprJ4cP8wtMzLbsyaUer_-jBE0s5Oum8nlhZexTH4tJqIuBFzoQWddoP2FKqeHIdv2wlan-yo3sx-D4lA7kuiPBgCc97m0wPmtMhImJvt1Je-nBwVafvRpjA1Zr9vvHvGirkAfxL1dPrt3ovEI4M4MYLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اسپید:
دستم به دامنت یامال، تو رو به هرچی قبول داری قسمت میدم آرژانتین رو ببر و نذار مسی دوباره قهرمان جام جهانی بشه! اگه اون دوباره قهرمان بشه ما هوادارای رونالدو دیگه اصن چی داریم که بگیم؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/100507" target="_blank">📅 17:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100506">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyBnKBzALdZ-568NbHWfGkkuhZZKVB9CDUhutZ-4rBVzykk5TVqP64xt_nSU8NKA4WR7tl0vlT4BYUkqezcSZAsS-duYgHcsGoCef783lOPAbBAPUT6kjYVWi4gImWqhSBkBnL1uT7GPXu6d2tKzlUyf6k3OEtDOK_LSC1Xnf2LHf9vBSWj-zwrLURwRA4qXFbY-06kfpkYACBx_cKTJ20YrHjM1ZF5M9R81EvgklI3I_Ggx6eBFACx1RlY_dR3IO5Ch6B17Q_fNRKv1p5PI-VfSEDpkz92b4TuOeU-TR2vP7qKiCGU6gGuZ01WZOt0zGLSaFLHe28umIIukqc49JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رامون آلواز:
رئال مادرید واسه فروش کاماوینگا مبلغ 80 میلیون یورو تعیین کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/100506" target="_blank">📅 17:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100505">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/901a48c5c7.mp4?token=hql2NXidkZ2eKXok7MgNhL-qewG_z4tsnFTcKhDnJfzBZJVIkMlOqNBFbDPGuvInalnoXMdKKQ52KaiB_QLVCYbiy6Zdi3ueyWwIq0o4nzDPTltzy4BABs-u-OjZ7FSYhYP2qpuoD2CgNoZ3E4r1LNs-WAd6Sh6hh7hrhue6gEkZAg8GYPV6sayLVxgZACG8WkY7SNT1bz6rZu_wRDEA2yWQBkIa-5nG1HmErHjDFJUJGiphyaWG4sghRCZaS5ivAjQBCoPpL7OSXw1ZEC3T2qiwjdvWlezy7yueMXwRzzQcJy7HuwTKbLjyKZFLxeIDwDqbBm7gVwjUyzOlVZrm_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/901a48c5c7.mp4?token=hql2NXidkZ2eKXok7MgNhL-qewG_z4tsnFTcKhDnJfzBZJVIkMlOqNBFbDPGuvInalnoXMdKKQ52KaiB_QLVCYbiy6Zdi3ueyWwIq0o4nzDPTltzy4BABs-u-OjZ7FSYhYP2qpuoD2CgNoZ3E4r1LNs-WAd6Sh6hh7hrhue6gEkZAg8GYPV6sayLVxgZACG8WkY7SNT1bz6rZu_wRDEA2yWQBkIa-5nG1HmErHjDFJUJGiphyaWG4sghRCZaS5ivAjQBCoPpL7OSXw1ZEC3T2qiwjdvWlezy7yueMXwRzzQcJy7HuwTKbLjyKZFLxeIDwDqbBm7gVwjUyzOlVZrm_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
🏆
تصور کنید توی اوج هیجان و استرس فینال جام جهانی بین آرژانتین و اسپانیا؛ نتیجه بازی 2-2 مساویه و بازیکن ها رفتن برای استراحت بین دو نیمه، همون لحظه بیژن مرتضوی وسط زمین:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/100505" target="_blank">📅 17:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100504">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e5386b5fd.mp4?token=HdF2kWqtOWWzzIHIZeGuku8FQ4HcwYZ4IEDVR8Mj7wmiIDAS8bd1WJRb0H_iTcqMpedin93-fhje39g1k0Z9HQJsSusoMawJs9r5c2uS7DXHyDCBAGBZ81G7YcJdiAugVE9mGFNdTacgB0DhpoZum2ef2oF3D0SFKZVBBejLjV5590rAEHc6dEJP-s7wEOuv8qOwkblY5Q9S2HTUwIu_6NOchDFNGD7VfICA5SYj-jxLoR7bPwF8clH_02aN0bIZA72UXfZt2XBTs0V8Bt7e4TLthLhd39wS1CgKM8E-z0I5QcoYGteSQ8YC5kft5MBGKijn0dul8YPwaHWX90r5ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e5386b5fd.mp4?token=HdF2kWqtOWWzzIHIZeGuku8FQ4HcwYZ4IEDVR8Mj7wmiIDAS8bd1WJRb0H_iTcqMpedin93-fhje39g1k0Z9HQJsSusoMawJs9r5c2uS7DXHyDCBAGBZ81G7YcJdiAugVE9mGFNdTacgB0DhpoZum2ef2oF3D0SFKZVBBejLjV5590rAEHc6dEJP-s7wEOuv8qOwkblY5Q9S2HTUwIu_6NOchDFNGD7VfICA5SYj-jxLoR7bPwF8clH_02aN0bIZA72UXfZt2XBTs0V8Bt7e4TLthLhd39wS1CgKM8E-z0I5QcoYGteSQ8YC5kft5MBGKijn0dul8YPwaHWX90r5ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه مخ‌زدن در استادیوم‌های جام‌جهانی
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/100504" target="_blank">📅 17:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100502">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b77728c3bf.mp4?token=RnWewzYZb0BCCUsFToGz1Cuwz38k8Dg721K12OfJB6osHkuSXFVol_Yxg186nUJT7Ool_mesDsvqzl39XdTUoINPfpeFYXSw-YQ-07g6DkcChqJVjjskpr1tPOk6TZD6uQLsUA0OmAzOsma5FECeOIHoGyeDiYNIE5guZONebiDhliombnRlOtKkZpmFlc7jUV4plEep9qdJurBcZryAwpAh-QyUlrG9sLHdL7jjvKBtc7IkDO1FgylUejDXF-zbjMd1pGIMiKdYQm2JvTMm7LAuxq60wOP7vsNZOiYT8phaFQLV1hTlCU76nA49iNcN8aJp4xV_AHzxlFQFDGvg7oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b77728c3bf.mp4?token=RnWewzYZb0BCCUsFToGz1Cuwz38k8Dg721K12OfJB6osHkuSXFVol_Yxg186nUJT7Ool_mesDsvqzl39XdTUoINPfpeFYXSw-YQ-07g6DkcChqJVjjskpr1tPOk6TZD6uQLsUA0OmAzOsma5FECeOIHoGyeDiYNIE5guZONebiDhliombnRlOtKkZpmFlc7jUV4plEep9qdJurBcZryAwpAh-QyUlrG9sLHdL7jjvKBtc7IkDO1FgylUejDXF-zbjMd1pGIMiKdYQm2JvTMm7LAuxq60wOP7vsNZOiYT8phaFQLV1hTlCU76nA49iNcN8aJp4xV_AHzxlFQFDGvg7oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
قیاسی: رگ گردن میذارم که هالند لره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/100502" target="_blank">📅 17:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100500">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uw9yPaC9FnxdTRFidFiber4ofx0eUiKxS-oVFwl0C1hI6lNdU5wbqYBgy_bE0HYbj2u21fZGxVz25-tdpUy1Gl4bXaYvUpaZ3O3tKWLcuLcek-1eBXJICSIpISs86AkS0Wu0rLtotrqWKSZve6wfSFfJutyK23SfpLAS_1GNFYb7ns2VjTSdktofc9gsqP49qQamAp1cswsDLC7cOiV3_QfzqBZh0J4sFI5pN_k8J3iPMd6MWawzYReLH_rye-WNv7iAj8HgjIgp5HlT1WUSvbhfkVaeatvOKYBeuhvd1lNwERmUXwI4DBBYElQ5-4Pp1VcsW3o5MulyOwc9EMZFVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tJJVURmprgrKXvsPB-o9jRrtleEl39bEcRADSE-NSieGrui4M0JnApaRdgI2AWRR4fPfKgv3sap2qJndx8l_zJy7jhvdogRvfds1fWKOfenUT1fezi37Ll_OiyaZf17Yia85Ib6n3yNTe0trHsA8fPcDGI9ziMBTFH2wNoZkeA8eRdpXWgMRLPw7Zv86CBTVL1g5a7ajq2Je0zBG_XlU1H1XLEHE-IVGylJCP6drLD8EJaoyNhafc9maGmI5Xp8-9FpHn7mJU0my_x8m0JQB2DCiHxAYdxjkwSLnb9Amyu_5rbrH41bjZqRxurB1cEFzKj9W31mPglWyueahCA883A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مینی تقابلی که قراره روی سکوها بین داداش یامال و پسر انزو فرناندز داشته باشیم:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/100500" target="_blank">📅 16:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100499">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6mZ19f7CJdpXrhfB0lHpoe1W095kQbXDofBcxrl8w1ld2SF7melqOdOuBykHCWABmCD31cpEqRTCjMbg4rZLzy5wyghRVfrNrRTN3JeoyjagxLs8hslkxTCaBjR6hYlmKv9qH7XzdJHyWKomvR8xZ2BXOqbBd4IkvS5otbwDAAvgJjqMcg1MHZ4vMrizChj_FoCuFmM1cH_SaRhrvofZKh0aKtgxHqhaWgr1p0arXLtciyRFp1JZxKkfypUv-99iCqYr-AQ_mtVpdbk2aNUtpO41mctb2n3-HTDi9xjqsI4QkfC-mYhxL5xi1HoCfzf4_cbNffErom2nTYygx4Fqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
الکسیس مک آلیستر بازیکنی است که بیشترین بازی را در تاریخ جام جهانی بدون باخت انجام داده است
11 برد، 2 تساوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/100499" target="_blank">📅 16:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100498">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DebHDzrI0acyrpHMOanTyeiH1gVgCWL3ymLuu2IagCaOluWO6_hxjcIFeRR09Blb9S2pEIABgenSlF-BcsTQ9_PSCK0LnqNuitCTLERjyIVxn6p-_-kk7cNXfpdesW4szrbPHgqe4aHQJwC-xbXxK9ZYpvavm5R-qZ1sa5mrz0phKQi4zah5NiaVvzi8U88oCrC5Hp0vhb0jE9AnKTfJ8honXxF6kwXZ1semgDm2YTuABiqI13jgwK6s6lUJohtRJU8CfPDoSYzyti4FZ9CebPZGjplp0MveCcHIF6G41BJwEQxns5aNt2J-wGVZBaC2jOvwTfTsZc-djPdVdy7VZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
رومانو: سوبوسلای مجارستانی با لیورپول برای تمدید قرارداد تا ۲۰۳۱ به توافق رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/100498" target="_blank">📅 16:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100497">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef12f755c5.mp4?token=SGwMBf_Xm4m2vgOsy1K1T4IovIfK75U2rNLCriyTOEXKU0TljwTAOFEyzgnF47z-tAyaIseooH82MK1QjEjvwLUQGsClUd1Q42hgs_il0OvZz8A_1x0CkKgOmteYyNRNFqm-Lbq4Zd9_BZbRQMlXfahppljqajNRxuDmqdSeVxPCMKfeXul-Z-OZMCALc8eNhl4R7NTcVH-i0L_NoVpqeiSVHSZ712-pTxJTMp-v8vUzWNokrk1Zk9nR2Ph_bAyaOj-QR5jHyUnWWOa_LuLACPSjivDyBfQHO5lxvJW5B_Mha6jzel35gevbVEF58zv4qVpHzI71piDu1bJtzb41hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef12f755c5.mp4?token=SGwMBf_Xm4m2vgOsy1K1T4IovIfK75U2rNLCriyTOEXKU0TljwTAOFEyzgnF47z-tAyaIseooH82MK1QjEjvwLUQGsClUd1Q42hgs_il0OvZz8A_1x0CkKgOmteYyNRNFqm-Lbq4Zd9_BZbRQMlXfahppljqajNRxuDmqdSeVxPCMKfeXul-Z-OZMCALc8eNhl4R7NTcVH-i0L_NoVpqeiSVHSZ712-pTxJTMp-v8vUzWNokrk1Zk9nR2Ph_bAyaOj-QR5jHyUnWWOa_LuLACPSjivDyBfQHO5lxvJW5B_Mha6jzel35gevbVEF58zv4qVpHzI71piDu1bJtzb41hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این جام که نشد ایشالا جام‌جهانی بعدی بانو
🎈
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/100497" target="_blank">📅 16:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100496">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efcbbbb391.mp4?token=oYjXttAR1dpbpBqhMZcXA3oSCURCeK_VMa__SBpomyLzuv62CCzKIsekE5lD6JrOAnhzu0Pi6f_NQVhY9j9Ags6Ap2hgNE_6s6jvbJNOe83l6GGEEd4dA_SkdsHwepAVDWRmoXQ6QPLGwtll70UxMr_cQTo6N1u5UvRoUWuKZDDii7PSEgvGRHHAduTjCttYP1eMBPRw2yGL9VOuJcgvY3S7WBML0uRIWsyI5ZwQbpdDoiVhm_E68VFbrw4tkClKiPSY2aqUVqo_PgngAeQ5P8q-RPoUY8R-zmWajOOF4beNTuHNaK0RPuVIuMSRCjKLK-WJ8gV-bjzDtyUcj8PVRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efcbbbb391.mp4?token=oYjXttAR1dpbpBqhMZcXA3oSCURCeK_VMa__SBpomyLzuv62CCzKIsekE5lD6JrOAnhzu0Pi6f_NQVhY9j9Ags6Ap2hgNE_6s6jvbJNOe83l6GGEEd4dA_SkdsHwepAVDWRmoXQ6QPLGwtll70UxMr_cQTo6N1u5UvRoUWuKZDDii7PSEgvGRHHAduTjCttYP1eMBPRw2yGL9VOuJcgvY3S7WBML0uRIWsyI5ZwQbpdDoiVhm_E68VFbrw4tkClKiPSY2aqUVqo_PgngAeQ5P8q-RPoUY8R-zmWajOOF4beNTuHNaK0RPuVIuMSRCjKLK-WJ8gV-bjzDtyUcj8PVRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
علی‌آقا دایی که میگه بخاطر مسی آرژانتینی هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/100496" target="_blank">📅 16:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100495">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4X3WZ_6kPok05fIhcZkERSrsjaQkhqw-Il07R0J9UjOglIeZ3AGvJo-Wc9idqnoj1KxA_5fUkwEYomhuzhvt1aQJKM3DOqks2bKZuEN3q6qaReJj9cSADSMCB1FrkCaHDsxPQEDGIqvIudCxLePxeg10PDNux6xxkeiQU7pgt6V5N0vo-ZW6a_0XTVDLyE2p_bP0kmaAuF5s44CxLz_5VjcI5n9FShthDf1XiqtS4L_SrEGE_AGCOsOiIDRV0URX12-Clc3My_gkGoIlDhPD1nXhJW-rYvVX4N91KqMvxg2CFUUEzdk4zQPUTFr0xdTl6xfxPKJuvIIdBYyHORhlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری دی پائول کنار مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/100495" target="_blank">📅 16:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100494">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cb2da8dfa.mp4?token=Bt8gYX8MHRqxo7ZXONIr6ARiSUH3QhQZkEBZozitJoNcTYg4XDKz89TNOSfYseH7umtiu6U1uqpnha3Yto4T_4tD_DZC4EFVxJ40boMMdgV2_mKi_lJmjMSipYE-ysi7KvgtU3YUOGUXEn1VqiZW7wz-Oh1kcNaB9q1PXHrfM1Xdst_La3ENlmlqrf1qArBKrMAN18DTGPtdTnAILC9Lf3V-3RtAiqgeLWTH_1d-8USURs9r31VuviIqqP-gAm6r1hFtc-l69XiX0DdEMZLcrCzXxEjdSKF0PGAcvAUn7-PkEgVzndN2T9YTwNVWhhmk9UA4JfmkLjSVkbXi-8M8Om1GtIvhmBdX3gwiBQUtAax35uW10hgKjHju2DFziDDNaraC0gVUV0ZhVj_hcDRjnPg1lCQVStDWrGO4DHuNZo6bhs7MA_UCB8gP87Fwv_9jiaNkwJiItjWG-ZrhJbg4JzSPKkkd-HX77XUxstmc6QIPkWhovsfa7zj20EXUa1dI2936QaoLaGON7XGssXbxlzJpjbz5m5X9vhX6xCQDE6uT5G5jPx4CXewtV1lxAh51ZHfQHZoPIBTwNASSEzmDloANlO2xanpLAeQZWxn9A9YgdqOw2EWYTbo58zd5eXlbIEDK3L6JsgoohGY7rso9YNVLCh9vRMR2qH8gCC23ixM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cb2da8dfa.mp4?token=Bt8gYX8MHRqxo7ZXONIr6ARiSUH3QhQZkEBZozitJoNcTYg4XDKz89TNOSfYseH7umtiu6U1uqpnha3Yto4T_4tD_DZC4EFVxJ40boMMdgV2_mKi_lJmjMSipYE-ysi7KvgtU3YUOGUXEn1VqiZW7wz-Oh1kcNaB9q1PXHrfM1Xdst_La3ENlmlqrf1qArBKrMAN18DTGPtdTnAILC9Lf3V-3RtAiqgeLWTH_1d-8USURs9r31VuviIqqP-gAm6r1hFtc-l69XiX0DdEMZLcrCzXxEjdSKF0PGAcvAUn7-PkEgVzndN2T9YTwNVWhhmk9UA4JfmkLjSVkbXi-8M8Om1GtIvhmBdX3gwiBQUtAax35uW10hgKjHju2DFziDDNaraC0gVUV0ZhVj_hcDRjnPg1lCQVStDWrGO4DHuNZo6bhs7MA_UCB8gP87Fwv_9jiaNkwJiItjWG-ZrhJbg4JzSPKkkd-HX77XUxstmc6QIPkWhovsfa7zj20EXUa1dI2936QaoLaGON7XGssXbxlzJpjbz5m5X9vhX6xCQDE6uT5G5jPx4CXewtV1lxAh51ZHfQHZoPIBTwNASSEzmDloANlO2xanpLAeQZWxn9A9YgdqOw2EWYTbo58zd5eXlbIEDK3L6JsgoohGY7rso9YNVLCh9vRMR2qH8gCC23ixM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
تسلط کامل فیروز کریمی روی زبان انگلیسی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/100494" target="_blank">📅 16:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100493">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8ceabea2a.mp4?token=g2uzPvxZuM78CvdYv2ixUn2PzE0TXkjCZqpwmb69QPK1wyAJK-cVgP4KUb3nAK-FfGVd4QbgcAV0RRpZfZO1Yt0QMcENM-HTRBpkstIrlMHJsQqyk2cieH8Q4qLvV1cZa3TCSHKwDpVk70QlM3Bmnjfu5IebfclsUaKM4RtJZyrkHqiM4S2-xZbIfgCigB9QIWiYLw51VLEADOllA0eEE9oPs97w8FGeQT2LIsHFKiX1pk_Xna1JEq24L2iczxca3mfQsojIx3zaPvQsXe8iTVZ1mET0vRzRTrO_PovZ-QrfIDfzGV_rX7L8dYSHE5B3B1_IQaVeboaN6zyOu9VVvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8ceabea2a.mp4?token=g2uzPvxZuM78CvdYv2ixUn2PzE0TXkjCZqpwmb69QPK1wyAJK-cVgP4KUb3nAK-FfGVd4QbgcAV0RRpZfZO1Yt0QMcENM-HTRBpkstIrlMHJsQqyk2cieH8Q4qLvV1cZa3TCSHKwDpVk70QlM3Bmnjfu5IebfclsUaKM4RtJZyrkHqiM4S2-xZbIfgCigB9QIWiYLw51VLEADOllA0eEE9oPs97w8FGeQT2LIsHFKiX1pk_Xna1JEq24L2iczxca3mfQsojIx3zaPvQsXe8iTVZ1mET0vRzRTrO_PovZ-QrfIDfzGV_rX7L8dYSHE5B3B1_IQaVeboaN6zyOu9VVvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
آخر عاقبت گنده‌گوزی یه بچه‌سال برا اسطوره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/100493" target="_blank">📅 16:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100492">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0505b98db1.mp4?token=LIbUO7U8q-VyYYcz3amUFhr5XL9R3yzRtsW9qghh8hGWoWo3dbeJ5cpYWCbaoDETeKhwStr0JOSO2C_OsqOkPFMOQKoQ1k35ODuoOeuTwsLgecIX3TH385LygR83HdkTMENfN_E8UvGSAHadMA6CSGfoCeaSMj5ZKPzq97RefhxvCesMpOW2c1hm6INAa9iMehrsYsxwvkU6U7S1napJAFFq71G3RXTU9PIMUvrQQZTsDLjyMcsCvedTNwkyOA2Gb3HmBKCDQ45un8GooX3fWjBBear54wDUa51vpZaw9XurT44dJJZD47-24w4giHoKyGDXmI68Y__qC6XlpGVKAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0505b98db1.mp4?token=LIbUO7U8q-VyYYcz3amUFhr5XL9R3yzRtsW9qghh8hGWoWo3dbeJ5cpYWCbaoDETeKhwStr0JOSO2C_OsqOkPFMOQKoQ1k35ODuoOeuTwsLgecIX3TH385LygR83HdkTMENfN_E8UvGSAHadMA6CSGfoCeaSMj5ZKPzq97RefhxvCesMpOW2c1hm6INAa9iMehrsYsxwvkU6U7S1napJAFFq71G3RXTU9PIMUvrQQZTsDLjyMcsCvedTNwkyOA2Gb3HmBKCDQ45un8GooX3fWjBBear54wDUa51vpZaw9XurT44dJJZD47-24w4giHoKyGDXmI68Y__qC6XlpGVKAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای عمو ها اووعو اووعوو رو بخونید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/100492" target="_blank">📅 15:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100491">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2CoTMmJvjqDSfJaw8cSiKKziWEVTYvBjp1otfBD_dLx-Q5Z52tIeGEZcsVeAs0oXOXhMSySekh7VFY8jvfmR6bp5U-Wyyz81CwIWkGwCTxbKXZGS9kgde-pPJ1UhgdUhwqoCJanhA2-4JtsQjpvRiPpdqH1_uYGtcDN9E2T_Qeqv64LHqLOayR_nxj4fH-V26SqD_RFspfwNFGHdtndkJT43g20VUN-rg1tzz8gDN6D4yrUnkXyyQrJr8dRypkyeqkdNeNoOa42L0stIf3JMye3QBjTKxTgnlUxJmuXW0dkfUiYUM5ZWDwa2eBXzDFIegKmbwLHf9xEhc3eVwrrgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦁
🇦🇷
آرژانتین در مراحل حذفی جام‌جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/100491" target="_blank">📅 15:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100490">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2fa-bu_bbUXR096q8wTP2BZXAKnm1jw8F5_l1nmTaGyiZeKtOFgjoI8x8EUTiv9VhvWGVYeFhq8g3gXP7SasoboykAE7rE0xt6SegrdQn_0eT4xMNd0WvJExTwkL1LCfQ543JzxoM4DjjmXvs-gEzENLFrSgFKNk87g2grulicXNjINnG_OY5yPAVEyaZrNQKlcChfNdLFqkLPZNMtfI-1uRZK15alPiK0knv5T27tm09FETFTC7iEOnYSXmVpsb9Hm3Od2KT6H7VhBYOitsvUTFFjqT0RFFEfN9SpPqQNCtnyeGxoJeMbi_ynPJNCBl0Agidw5FdRi1WO_EEMLSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
🏆
با صعود به فینال جام‌جهانی، آرژانتین با عبور از اسپانیا صدرنشین رنکینگ فیفا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/100490" target="_blank">📅 15:32 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
