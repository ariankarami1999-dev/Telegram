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
<img src="https://cdn4.telesco.pe/file/ETp76c6biJqfO4-WKWsg4UcrPlENKBpSujwTBGKHzVoQrvcAYFqozNcLeLmJbkKEnmR60IOEEASsiuCnAc8ZDjCUz8XBbNoY88rNAQi5IQ3HqW_s0sB7BGlMN30ibF5whCieic5sQ8aDmcVeZAi1tmxqb3Jee3199BPGVmFQqpq4YUq8oPU-g7M92ki-cONUWbnE1eZfqIbnXoioNeRH0bVbIlBxglp9RfYoEkx6zVuLD3hWkEIWRw2WLf9FNGhO0kWv0q0arbS6kPyQdOlyrv8RppdGLfCPQLUAvrU7FkHXWzddfodyZl0sR7vHVBHiDilCLabArTzdLU708NqU0g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 942K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 02:56:07</div>
<hr>

<div class="tg-post" id="msg-134920">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QH11KWik8ACsniQskC57HCkeOl_pJhKpbmSXsi2OTDNGKiaCRUjq9OAXzk8OpNLXvmYf82pyk3SYnP_FYd2VQtnCSlw_chGktEcTw3rpOXgbn_U-KP4s2rpprGD_qCqCWQBrisZfhn6W31nFg-d1eZET3WOb5v-La3Py8E_M3Gs00xVtSOTU70PASH8rhdjFKJr3KJn6wKKrOsuBIZQW1s5_ffY8Uy-no-ccxMClZGMAM-H4tUateYNLvl7vpIgje0AK0WlCfUze7hIB8ygcKVy_MdyeLgrQuN0inGmvHdTDMPb37IW-OBV504WlAZ4eJbDjwlbtPPomfor9a_Yiog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون حمله موشکی سپاه به بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/alonews/134920" target="_blank">📅 02:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134919">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JniQAOebjnVQ33vpQ0FwgLdC_wtCEqpycWkUvnluqT7E5-Bb-_YHL5M8CstxEHSDGGL45awiBQLPKbXK8YAuH4lDF1lxFihwES7P5S-ryS0jxRMP4jHR_dNFERuQKPqCmRjNhSjfKX8IvYXHT80KMtL5rGwRFz6kBaKbtw5jY6su_pOv4QwuxvmKvoyvR3ET0JSKON0BmOsToUU6oQeER6jVGTyCmHdXnKjC977muanuIP-rxjt8_JQiw5nA2AC512neivoFJiEeAoYeY6UXcceBw2_rkd9JLt2KDseS2knJ2D-D2f8gcXqcEZRlYe8Jo1dN2i9Xm6OzgUNY-gFNcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای عراقچی در حال خروج از ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/alonews/134919" target="_blank">📅 02:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134918">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhFSth0sTNguWWJv0Cp-WIY6ag7bl1g62pMtNEz0zATPm5cwkfZFUMDz1q6mljLRA_dfEG2Ut52KEzwDoSHtpJ8SsP-qwgHvtz8FWzXTHTYiE2hgqUVe1cyQCMxPEiGmh0yRdF9eOlp1EzQsI3CRwQFKZJ18IV6QjIFoEsaesgTG8WFLI8lkeVpxYGD3kJYSAvGE_ZUFXEhsNOAoLQR8iYFRCz64D2s8P-qHkzu8ILakWuMEAAZj14raGdV3hN7ZhnpPqtZ136-ozNagE2hvuzp-X64YPTYB10qryW9ELMwG3DTBj95c42aOP37LHXadMa4yqsX-eokJ2iuLsVlR_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستون دود در پایگاه دریایی بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/134918" target="_blank">📅 02:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134917">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/530b6d1ce4.mp4?token=pD9X261JSqsukBsjoRs5ky33ascdDi5KyaGQK_oBIJBZhJZYZtXLLnl5QsfXbbohLPo4fgGJrdwpOIKcMb1sqQHnxV6ZcYUKkwJGwJaqRm7VP__OhCt1GppCK8REcn78IBpU9-87k5lcZ8pEZMGifMmofnXrIFLXFA2B86ZJbDitzLawSmCzLFF4HVS0Ka60C3quD8hYJhq58gDSQ4LB_puILrbatkq7drREGO5zVjNSJEVjPaj1_k-iBeW-pdKZXz95ti0zzpMS3GRbF5oMBL5gawpFwKiCHy-GvnVHEQ179iEBOTc7FJADO9UONeAXpdFD8U19lw8AcR6Nv538IF5N5W9GnEYuJKcwFB0LiUKc9zlfa-E--DiSKDIIjfqiLAJDuf9rX6r9pv-gQVQZhB_dJDKOtyUFqy_YgSmdHoWW5g5LA83RYeeJSllmGOhnguH--4hBkXr2l9OiypBCUTQgpcuY7grd-6ytxsXE2Ab97pbgN_wMtwYdLyHGir7wQRsxe3D6MK_hlwyIW4K2V71lZv-bO6msF0Fix26T2JbBcsB9ThoBuA3Pf6OovzGGCUjYRO0cgSvsUyzvw4RgtXq7r1T5-DbsxWB7An2QEibiidI1g7Ei9x3H6Ed6hWfrm8kSX6Z_yXqH8iKyKGDl7N_fZ_V2QAn13bcQ367YIqU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/530b6d1ce4.mp4?token=pD9X261JSqsukBsjoRs5ky33ascdDi5KyaGQK_oBIJBZhJZYZtXLLnl5QsfXbbohLPo4fgGJrdwpOIKcMb1sqQHnxV6ZcYUKkwJGwJaqRm7VP__OhCt1GppCK8REcn78IBpU9-87k5lcZ8pEZMGifMmofnXrIFLXFA2B86ZJbDitzLawSmCzLFF4HVS0Ka60C3quD8hYJhq58gDSQ4LB_puILrbatkq7drREGO5zVjNSJEVjPaj1_k-iBeW-pdKZXz95ti0zzpMS3GRbF5oMBL5gawpFwKiCHy-GvnVHEQ179iEBOTc7FJADO9UONeAXpdFD8U19lw8AcR6Nv538IF5N5W9GnEYuJKcwFB0LiUKc9zlfa-E--DiSKDIIjfqiLAJDuf9rX6r9pv-gQVQZhB_dJDKOtyUFqy_YgSmdHoWW5g5LA83RYeeJSllmGOhnguH--4hBkXr2l9OiypBCUTQgpcuY7grd-6ytxsXE2Ab97pbgN_wMtwYdLyHGir7wQRsxe3D6MK_hlwyIW4K2V71lZv-bO6msF0Fix26T2JbBcsB9ThoBuA3Pf6OovzGGCUjYRO0cgSvsUyzvw4RgtXq7r1T5-DbsxWB7An2QEibiidI1g7Ei9x3H6Ed6hWfrm8kSX6Z_yXqH8iKyKGDl7N_fZ_V2QAn13bcQ367YIqU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آخرین وضعیت شبکۀ برق شهرهای مورد حمله، از زبان روابط‌عمومی وزارت نیرو
🔴
مردم با مدیریت مصرف برق، به برق‌رسانی پایدار به جنوب کشور کمک کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/134917" target="_blank">📅 02:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134916">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a82adfa6fe.mp4?token=F8IS48cZxMLTVVr752_oREpjR7fLBnWRTN6um6o7ka4U8J-ZYkNk10D7ZB3Ub05_4QUcohsG1VJXwJ7OQxbwJ32DcZxEh8v5pu4NQ_c6RvAKrYHmRto3F4ccbjd8pTQLQtOyYAd1QxQ3RhFIP79Uyz_lIrfMF8ptTMKqabpKABJyhpoOaNn-e6tZCqoUr0RkYKCTNjwWYYBPdtpBQ9M8bFkrdxGzX82XDcKZ6WGYLJ2Y8qNTG9QO2Gkf8TPC_KoLGK1TXSk00gQa5qJc6yAM2tPK_Mt7bMAl34xkejEcmAXD4pVR8BCN2T3UPaLX5TG1mkUYGDlCX91Y7Mx0k5IUcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a82adfa6fe.mp4?token=F8IS48cZxMLTVVr752_oREpjR7fLBnWRTN6um6o7ka4U8J-ZYkNk10D7ZB3Ub05_4QUcohsG1VJXwJ7OQxbwJ32DcZxEh8v5pu4NQ_c6RvAKrYHmRto3F4ccbjd8pTQLQtOyYAd1QxQ3RhFIP79Uyz_lIrfMF8ptTMKqabpKABJyhpoOaNn-e6tZCqoUr0RkYKCTNjwWYYBPdtpBQ9M8bFkrdxGzX82XDcKZ6WGYLJ2Y8qNTG9QO2Gkf8TPC_KoLGK1TXSk00gQa5qJc6yAM2tPK_Mt7bMAl34xkejEcmAXD4pVR8BCN2T3UPaLX5TG1mkUYGDlCX91Y7Mx0k5IUcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی وحشتناک از حمله به اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/134916" target="_blank">📅 02:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134915">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fti9tqdW5TLkmzSM3pwVP382PpG7mk7C0IEzlG4ubPEpO7I6ZwHw-6pAsgUcI8LU1Bfeor91ZwHUwynal3mtFmRwZa7lDf3HjJjcmf1u499ndIfz6joPZP8m6oNKDHAyd6qmkGvNWknlhVKEXX6Kfda9whhdiwJZLK3lV1w19hxr6ptjIK61aKW947lF8k7FESDWwPWvz0ilIqS_ebgvh_GcshvAwxitdmZ-BV_9CgQcDDSEjNqkHyA7bc04Icp0C15GvPBC_YvyIfx_JTvX9F_qfSr7n15NaeB87kLB6pQNyCffLmOjjLBBDmZZhBGFzdEM1gMrO3I95Kjb9DWDZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نقشه حملات امشب آمریکا به ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/134915" target="_blank">📅 02:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134914">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
گزارشات اولیه از کاهش پهنای باند اینترنت در سراسر کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/134914" target="_blank">📅 02:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134913">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
چند دقیقه پیش امریکا به فرودگاه بندرعباس حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/134913" target="_blank">📅 02:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134912">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
انفجار در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/134912" target="_blank">📅 02:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134911">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7aa57774a.mp4?token=aCsG91lqxpevv8sZ_5PiTDQT8k7rw7dd2yTA-HPobUQ4XaRgRb3Bf1fe-pYETzfWp0Lmp4bU8nTsiANxh8HhnjEHkpok1-fgbPqXyLhmCjTJQu94-4zj3PvnQMelsCZOnFH5BfEMvykoIJJjFigVemFvLePdTgieopW1VAXVWOllT9tjLPuMSt5eVLP735MFO45MFeRl7ReaAQOkbgJFSs6vyfoocdKFC8hqg6IbmOtJHjxZP1HMe6puONV6BzYKSG-hX0-det8kHe9ngIDX859QNplEX8MqL3ckTVl7jass2EQUSN2SphQjvTKZhexS246InkcBbk7jn90anpZpUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7aa57774a.mp4?token=aCsG91lqxpevv8sZ_5PiTDQT8k7rw7dd2yTA-HPobUQ4XaRgRb3Bf1fe-pYETzfWp0Lmp4bU8nTsiANxh8HhnjEHkpok1-fgbPqXyLhmCjTJQu94-4zj3PvnQMelsCZOnFH5BfEMvykoIJJjFigVemFvLePdTgieopW1VAXVWOllT9tjLPuMSt5eVLP735MFO45MFeRl7ReaAQOkbgJFSs6vyfoocdKFC8hqg6IbmOtJHjxZP1HMe6puONV6BzYKSG-hX0-det8kHe9ngIDX859QNplEX8MqL3ckTVl7jass2EQUSN2SphQjvTKZhexS246InkcBbk7jn90anpZpUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه‌ی انهدام رادار ارتش آمریکا در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/134911" target="_blank">📅 02:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134910">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZByEMbWGw6hyH0yVn8YQQdbZYbKQD_TR4m5swhyMhEmn1d2UrfuCq7d8LJZs8_2I28Zk_pfbIwVm68BH2ZOytUUUoKR3_z_KV3yRq-cprY3otFTGU3Nr9bbnoRJoidknMBySE7PhY0gJa9puO4Gbbjl6teoQvI_rDs8ERcJLbBC9m4HElzyeHSb3fiIpkQ8fYIXWRpeTWGTg_f2N6zNLi6OS8pctGT5c5XgP5VqydulPziUgJ-sYlgU3pK4-Hq0T1qfnWJbkNrG18-h60dCPakfUDL6uzdsXxBm_IAXeFLviuHpuys_LX6s0CmcGunMEFmGnjbBcAOeZPpv4gdD8VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سایپا از محصول جدیدش برای جنگ زمینی با آمریکا رونمایی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/134910" target="_blank">📅 02:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134909">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">💢
پشماااااااااااااااااااااااااااام
😐
برای اولین بار همزمان 25تا سوخت رسان تو خلیج فارس درحال مروازن
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/134909" target="_blank">📅 02:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134908">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBDLrEtkRwkaAohZ_TRoMN9kRYLKzYYuz4e08Od2en_56gsZaLsI8iw9NGfukkLbBhfgGEji4uFNCPguW87-b7PGkpUU_bOJZQUvImVOsLqnMf6GTJYNeJgAoKhR0QZxRc6KdJiuvm2BbyKQlkS3mWohLaK9JT5YN57JqYNMVjx4dIhgIDVcqtfuf1ELiwAvVuQOzLLHxom0LCVt43hoXyDSWFEtZpIf114C_tdDyKM3eaEfgjwJRegC6l9Ui3InEWI5626_YSFidaAd28dqWtaD90c0aChRlmqqj0VncNQyzQJ9u1DCfQwpluNKP3OftZAeyWG0yZ52yCmHJXujXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هگست، وزیر
جنگ آمریکا :
ایران کنترل تنگه رو در اختیار نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/134908" target="_blank">📅 02:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134907">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
قطعی برق تو کیش برطرف شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/134907" target="_blank">📅 02:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134906">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93c5684acf.mp4?token=OvDT9XJgvdDJTXqLZHrwHP1cqMvXTFVVmVSlaA-_r2XE1vDtLgSC89KH7yISG2u-ygkJL2rJgp5rmu6xvp9TGqOpovPfcW1Gp-41KDfS-u4n6euUb1yWTFuglOEnsLq1M1jajzMnsPh7bUNfejMMxBrJKSVJ36-vi5rZ08C7pV4vk6Grwt595qspX4BFejGDvvimTr7oxWPGd7cz_cdGTloVWj250oyZqsBKDuw3xXbQ2DITez2OC2fQzRMg2wQVR2R-EqDC2nxwBA0HEibeHST1eXp63SATCtjMyTpzLWYpri2vipIPEMzD-MwPZmkdbiQVmMlrBqJ-0CJJoG2JUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93c5684acf.mp4?token=OvDT9XJgvdDJTXqLZHrwHP1cqMvXTFVVmVSlaA-_r2XE1vDtLgSC89KH7yISG2u-ygkJL2rJgp5rmu6xvp9TGqOpovPfcW1Gp-41KDfS-u4n6euUb1yWTFuglOEnsLq1M1jajzMnsPh7bUNfejMMxBrJKSVJ36-vi5rZ08C7pV4vk6Grwt595qspX4BFejGDvvimTr7oxWPGd7cz_cdGTloVWj250oyZqsBKDuw3xXbQ2DITez2OC2fQzRMg2wQVR2R-EqDC2nxwBA0HEibeHST1eXp63SATCtjMyTpzLWYpri2vipIPEMzD-MwPZmkdbiQVmMlrBqJ-0CJJoG2JUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/134906" target="_blank">📅 02:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134905">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tX2NQ3k442wHkCWCWBNDTeNDLj1i_0ZQ1srr2TaKvkdl-rdqA7V-zTAKdtSbSjRQ_NIN9KLqZLxa3E6CEUKvK6sMgbilD6L1G54_rfKX9CcMXW4zGOSi9EdaQw5jOxwFWEAciOdfUVMhO8BNOh9vsNzXO5OdvBUJnq5p-GDk9vPBYMBfrGQxx4gJ_G9vzmpo0gjxy0Rqyzb1KTKAUfFGVxXqwavxu9H5Mnr1AIa7icMpfumxC1Ee7DMcrG_XfKqnDLmHfzvhg1IqOUvpf30RRSs-qv8ye21fC1h28ZUiRF8V-2s__u-X-hCOEjm67Emz7IETxidFlwYuDNRIVZDB5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل
المنصوری
لبنان رو، مورد هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/134905" target="_blank">📅 02:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134904">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f0d99f1e.mp4?token=EPeuml65HdU4DeSB5k60X8xiUdwleVMgaHpr7NiWUqStXewdiao7Pvq89VHihWAMxIwOXgiu3f306f5G2vDXLj5-_vTvBqA7k3rN-C8_yDvaXft4f0x80G3gJerrKqhS8mhmivKCu8331x1hBqrRtpTcZ_izM6l19yxlK2zoluHl-p6Icf59TsbfuWp7CBoOSPALDO-nKsvJKs7WDAU-QW8UEhhaUJu-uHPU6R7Wz2dmYfucwIBwKnDNucYZ938KDmAEe7AFhTtGhIbdNM3yZf8pc0MfRNAQ5RoZwWVLzYlkRjXCPP0Ih-EUyp5AlhIhrSieeGJhEj0BGfXnOb8YXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f0d99f1e.mp4?token=EPeuml65HdU4DeSB5k60X8xiUdwleVMgaHpr7NiWUqStXewdiao7Pvq89VHihWAMxIwOXgiu3f306f5G2vDXLj5-_vTvBqA7k3rN-C8_yDvaXft4f0x80G3gJerrKqhS8mhmivKCu8331x1hBqrRtpTcZ_izM6l19yxlK2zoluHl-p6Icf59TsbfuWp7CBoOSPALDO-nKsvJKs7WDAU-QW8UEhhaUJu-uHPU6R7Wz2dmYfucwIBwKnDNucYZ938KDmAEe7AFhTtGhIbdNM3yZf8pc0MfRNAQ5RoZwWVLzYlkRjXCPP0Ih-EUyp5AlhIhrSieeGJhEj0BGfXnOb8YXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوی فغانی عزیز به حقیقت پیوست
از داوری در زمین‌های خاکی هاشم‌آباد تا رویای قضاوت در فینال جام جهانی/
علیرضا فغانی بارها ثابت کرده که موفقیت، حاصل سال‌ها تلاش و باور به رویاهاست. او می‌گوید در دوران نوجوانی هدفش قضاوت فینال جام جهانی بود، اما بسیاری این آرزو را غیرممکن می‌دانستند و به آن خندیدند.
#نخبه
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/134904" target="_blank">📅 02:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134903">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
دیدن این ویدئو برای همه لازمه
🤔
مخصوصا طرفدارهای حرام زاده حکومت</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/alonews/134903" target="_blank">📅 02:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134901">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agZZoRrNLba39OeHopqPYlgBi5AelC0keth-nUMIGD52KGCLwJw_V1ZDgylyMRuXBctkTmqTuH75No04h-8fnV0iAP7m_AcUgKBE7FZHkEqWcCUpM6H-U1ETL_Vq5Ye6c8helBNL05OpAQ3mrRwoZeUO3E0IJ30sWuxoExW00CSidYiU0EwmsyiXd3I9xOjHcsD-OrPelOaEPTqDrJF_j-KUgUCkMKd7Ww9ELO0slF3ZUDJ8vw-hZ6olIDZM3BCfsm6mf7twMuOcpqvcG2LH4LHwTpSm2HQLbBWSQNT9WAagxBUlJXkKLfa4TPFp9EiKuJO0Wc_soJhGqYGiKNxeeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بدون شرح در صدا و سیما
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/134901" target="_blank">📅 01:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134900">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPXWxUx8DLsArzKiMVjFEx9kZyi9wkjntX-m3AcgLMVfT1W1eaa8g4hxnXqU1UCsvFk_89Ce85Q4lqc9n8mvXI28bXqdi2YA34dsr5LLvI0u8rmJEZFuGqjSdmL_MVAcmvltlznPbnLwRhrgF2qOS-9-BNnc7HiHqt-zZHic9e0uE4puoDxJ1xz9zzoIlqTRrjlyHIDxnJeKbrQOG0qJJdP-wDZY1fR7htJGWBKp8nEWkPWSJ7cEYaSTLUrkr3nV9iw40o0AkLSaAB66SxDftEXHb8TeCRwpl7rQdq-VIBJjoHrsHCZoFpZkDDXj23VDLLqU28HWsJkrDQC6IQDnhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری جدید هادی چوپان
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/134900" target="_blank">📅 01:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134899">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
فارس: حملۀ موشکی به پایگاه‌های هوایی و دریایی بوشهر
معاون استانداری بوشهر:
🔴
در حملۀ دقایقی پیش به بوشهر چند فروند موشک دشمن آمریکایی به پایگاه هوایی و پایگاه دریایی بوشهر اصابت کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/134899" target="_blank">📅 01:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134898">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
کاربران از شنیده شدن صدای حداقل ۲انفجار در کرمانشاه خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/134898" target="_blank">📅 01:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134897">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcGOQDK6UPdJN9-_HDrYtMpGOljWo57kDFmeE2EpKbT0TocijAZ8mcLULyJfiOKhpTgHq_N2ZHz_Hmol11k6-wIMbwYNwp7XdcQ5bFnq53XdKUdM3WXr2O91arP4i-vS8tmc2T2AjRN9Y5K7E1w4iss16iwbO9heMCVpxbT8iqeoYDN8uYna6rpC1qmIb8_wHb5d5xNAvgH1EFs4pGp6WstygRfMSXqypklwK9o_jRyq8y4-BqLqscljT1pvV5-SX3okrH6kx1aKJyJRWFH2ICGbVkAzvnFQgoA_U1TbeA0_ZdOhErgkBd4MzL6UNJMJHg3vT4HvCg6CgL3EPziwdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اربیل عراق پس از حملات ایران در تاریکی فرو رفت
🔴
بر اساس گزارش‌های اولیه، برق در بخش عمده‌ای از شهرستان‌ها و نواحی استان اربیل اقلیم کردستان عراق به‌طور کامل قطع شده و هم‌زمان پرواز جنگنده‌های آمریکایی بر فراز این منطقه ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/134897" target="_blank">📅 01:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134896">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/899752499b.mp4?token=u4v8DYQ4j8YFKiLlBh4wnHOsQU7400psTP7t_NRiyM5wkrupPAzrt-N70jVo4fF6rd-BkBWqr9CAslsjrzOJ91pJoTRjiO1wGrv-oBUDNVAMTBkoPelDWkjClS9WqeiLEcCYH9WUzBPPgmE17PiXrgetIxCjM_9JO-Wfzu-qMEnchJabtoKo7jrYaF9QaZxEriUDLunV02e1hPh0p4pEOy5E-Ph_1g6Huxni-5WsvylavqRr0GOVzgJwJZvcQId6pjB-pAr8LrvYzpIUxa4-13zCQfHGc74ROx2pKrcZfy20MEHOq9b_GA3blYnKRJxGqZtTeKC11mX_KbKvHHWbLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/899752499b.mp4?token=u4v8DYQ4j8YFKiLlBh4wnHOsQU7400psTP7t_NRiyM5wkrupPAzrt-N70jVo4fF6rd-BkBWqr9CAslsjrzOJ91pJoTRjiO1wGrv-oBUDNVAMTBkoPelDWkjClS9WqeiLEcCYH9WUzBPPgmE17PiXrgetIxCjM_9JO-Wfzu-qMEnchJabtoKo7jrYaF9QaZxEriUDLunV02e1hPh0p4pEOy5E-Ph_1g6Huxni-5WsvylavqRr0GOVzgJwJZvcQId6pjB-pAr8LrvYzpIUxa4-13zCQfHGc74ROx2pKrcZfy20MEHOq9b_GA3blYnKRJxGqZtTeKC11mX_KbKvHHWbLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آیسان اسلامی درباره ایران اینترنشنال گفته که از امشب باید بگم دایی مراد بیاد خونه؛ مراد ویسی جوری حرف می‌زنه که آدم فکر می‌کنه فردا باید بلیط بگیره برگرده ایران، ولی باز هیچی نمیشه. کانال رو می‌زنی روی مهدوی‌آزاد، اون که یه مدته داره خار جمهوری اسلامی رو می‌گاد و علنا قاطی کرده. قاضی‌زاده هم مثل مبصرهای مدرسه‌ست و اصلا شوخی موخی نداره. بعدش که فرزاد فرحزاد می‌اد، فکر می‌کنی همین الان دیگه انقلاب شد، ولی بعد می‌بینی بازم هیچی به هیچی نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/134896" target="_blank">📅 01:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134895">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
انفجار در کرمانشاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/134895" target="_blank">📅 01:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134894">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
انفجار در کرمانشاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/134894" target="_blank">📅 01:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134893">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
سامانه‌های پدافند هوایی در کویت فعال شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/134893" target="_blank">📅 01:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134892">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQVkIo-cA5GtdvsIo2Qij0t5kjq5jBMzhAFuT1Sa2EHhNqq_jz6NFb_ydNjwrOC5wD8BQGxw6K9F4FYe94gJS8IYWFeN3bkZzVpiGKHzhMWgjf_T6cggFVc4-xST7SN5ATwLSwOdZtQ7xDnXcvC_TbDSG0IBDivjiaPHygf34M5IQlqvpKySEu_gD7s2toiWmjdy5fEDmO6CEN5OqVbg_FOM9xgTtixo9GkHr0Zq-taghG_67yWW26WXlVkLaU_DzY4XLbA7pKXpeFdTfDN_s2A3gSaOQv5PhPu859lRxpzASqsEhr5bIz0D9oFM0HFDMGt0j1gLGlwYzxjuBOH7gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نگهداشتن سرباز تو پادگان دلیلی غیر از گوشت قربانی بودن دارن؟
🔴
آقا زاده ها و پایدارچی ها اعلام آمادگی کنن برای پاس نگهبانی تو شهرهای جنوبی
🔴
30 میلیون جان فدا بودن که! هرکی نره حرام زاده است.</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/134892" target="_blank">📅 01:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134889">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SSMBABRWBwhW__rwRyF4OUPOw1YYNKLkMyFRNpnKSd-vonkfcPuxdiSLt-17WEM-J1a1ABL3LDkn79VsdgftY-JBFf4l3T-GDEvQfUu429swjypuQB6zxXoDZqLd9jZmLmOk16u1OwC9cmUDIwOPmG12x1lEKWYPfTeq_ayOofiFqhCcYpdrkM324QZfJqzPRbv2_PIMo-VHJQ6rD-aCK7BQmFamfod88J7LbialqmpFmnO8oxwrcxhslteBf44o7HqVbUn9UczZQOWHb0fkfsWCs_W1KiKHRWKan9wETGkNGqk3xMQpS5cKIhC3VpnpsgqHSQyYVxibQS-ojRyQ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lzz3qTSNI4O4v9jB4t6eFI_TKct2us1kOYo54-E7m-EdZMTIcLyviTnL8xmPxF0ccysysQ9V9-L2eZXmmqAOs017hjtdmK1Als8NEjriO-zMyII44g9Kij8Kuu5zmTYgd8jxiTfF2NT0MW7eu2VYiFmZUoHGKS3tRIEj0zvIAu8SUZMZ9P0HUxYbyxNjTAjXgF8LGYqN9Lerkm5f5FCzzy47bFOc11ftNAiB6Hr1jjbaQHB6Y_yEe4OWVjR6Zu2sXo14-I-O_JiICNV30Wqzfqbjhda0c-o-4bbb--Ym0TiIyTqSQ2O67INRNfTFEIxmFxvxfgEMFhG7HzbnOgPjZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3d51fa3abb.mp4?token=T0dzfeExIYHsZE9s8whilU4ngIkV12Qy38UguAczzOoaVQbG0wmtp3RTidhqPL2daIr0oF8iR_vRsdU08xt92iHjpDOKI4aPIYLN6HTtq9U297FFy2dL3HKSliG_5yEIypR-aPsm7IR9cduNw_futBKarNC6BWMgcx2yL-dOfBMZ2s3ZfpZOObaY1JIj_FQ_D_xwAcIHW8aS6KfFCSmK1tEPneVCm6yIAwHyXUqmomiTrdg2GOUxM05otZeVOLA66ABW4MySKG3ZAOQ2Mn_kTOUdLK3fDELAFps1HqzBj9r2FdxjnogqXAx06u50LU02urhy4M8ehdO7v4L1pUtG6w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3d51fa3abb.mp4?token=T0dzfeExIYHsZE9s8whilU4ngIkV12Qy38UguAczzOoaVQbG0wmtp3RTidhqPL2daIr0oF8iR_vRsdU08xt92iHjpDOKI4aPIYLN6HTtq9U297FFy2dL3HKSliG_5yEIypR-aPsm7IR9cduNw_futBKarNC6BWMgcx2yL-dOfBMZ2s3ZfpZOObaY1JIj_FQ_D_xwAcIHW8aS6KfFCSmK1tEPneVCm6yIAwHyXUqmomiTrdg2GOUxM05otZeVOLA66ABW4MySKG3ZAOQ2Mn_kTOUdLK3fDELAFps1HqzBj9r2FdxjnogqXAx06u50LU02urhy4M8ehdO7v4L1pUtG6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این وسط دیشب توی تبریز یه نفر بخاطر اینکه کل پولشو رو برد انگلیس شرط بندی کرده بود و باخت، خودشو از طبقه ششم انداخت پایین و خودکشی کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/134889" target="_blank">📅 01:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134888">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
انفجار در بندر لنگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/134888" target="_blank">📅 01:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134887">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
انفجار مجدد در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/134887" target="_blank">📅 01:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134886">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2492a5baba.mp4?token=NTgKgZOX3i44qLugG4iGnleA708LBYedmyteRzKDpoxzuQI2R0StbeIQki67NOK8-S3cw3dFJqKzwdTlVFddf0HS4U8Wa6c3CMjzS_-bsaa5Q-MfIiDSSJrM8wFJWhxe7sIQggu1Hetnsl_HerJexF8txlnEGZ1A1ztKHNb2K0U-YH93042jIvIcKTI4fMVl6KW7Gxri81jx7rpDEXSjZQsRw87GzJ77ERe_G5kfEj4L3DP5j4DT2MvnqIAx0qYJwkHGU6m8DevTyZJ0EiIYCohrZxubxTDZHg5De9Gu_Q0__aL2M8_1IY1TF7EsiPdCVyoLoHRPY-DYfFPnGpVT2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2492a5baba.mp4?token=NTgKgZOX3i44qLugG4iGnleA708LBYedmyteRzKDpoxzuQI2R0StbeIQki67NOK8-S3cw3dFJqKzwdTlVFddf0HS4U8Wa6c3CMjzS_-bsaa5Q-MfIiDSSJrM8wFJWhxe7sIQggu1Hetnsl_HerJexF8txlnEGZ1A1ztKHNb2K0U-YH93042jIvIcKTI4fMVl6KW7Gxri81jx7rpDEXSjZQsRw87GzJ77ERe_G5kfEj4L3DP5j4DT2MvnqIAx0qYJwkHGU6m8DevTyZJ0EiIYCohrZxubxTDZHg5De9Gu_Q0__aL2M8_1IY1TF7EsiPdCVyoLoHRPY-DYfFPnGpVT2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که از یکی از سرباز های تیپ 388 بمپور به شدت وایرال شده که داره آهنگ میخونه
😀
💔
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/134886" target="_blank">📅 01:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134885">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
نگهداشتن سرباز تو پادگان دلیلی غیر از گوشت قربانی بودن دارن؟
🔴
آقا زاده ها و پایدارچی ها اعلام آمادگی کنن برای پاس نگهبانی تو شهرهای جنوبی
🔴
30 میلیون جان فدا بودن که! هرکی نره حرام زاده است.</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/134885" target="_blank">📅 01:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134884">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
دامنه حملات داره کم کم میاد بالا و به تهران میرسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/134884" target="_blank">📅 01:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134883">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
فوری/حمله آمریکا به شهر ویسیان لرستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/134883" target="_blank">📅 01:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134882">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f3dd4a9c.mp4?token=kv39hoYsWK1s5sfjaBzBcBdHXMB2j3Ycp5DXXdY31zaSZjqrAVDQvpIPM7e4p8oDCMR5st6R67NmjocvgPXYBmIkgw1_XwGU-n17DCfN08cRWctt8e3rZ0NO3E0QEmaCK7QYQLlNjBrs83H5s7zEnIy0pFdO5Jcg075YFthWrLuzcukSEua5jPzl1-ukLT7fOuABdQt9Bja4XIDscxsH3mpKxXJ8FPvZ9_mgEqD1oPWBDWnnwK6SX4o9YfU-_yei4B9AkKTfsTXlHQq2mEcxBvmUU15Xj9aJE-7gka_C6IZSYnnPYaAz4IuFZpCGNEFTPDDvRlWvk1Xyp3VJy_wsFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f3dd4a9c.mp4?token=kv39hoYsWK1s5sfjaBzBcBdHXMB2j3Ycp5DXXdY31zaSZjqrAVDQvpIPM7e4p8oDCMR5st6R67NmjocvgPXYBmIkgw1_XwGU-n17DCfN08cRWctt8e3rZ0NO3E0QEmaCK7QYQLlNjBrs83H5s7zEnIy0pFdO5Jcg075YFthWrLuzcukSEua5jPzl1-ukLT7fOuABdQt9Bja4XIDscxsH3mpKxXJ8FPvZ9_mgEqD1oPWBDWnnwK6SX4o9YfU-_yei4B9AkKTfsTXlHQq2mEcxBvmUU15Xj9aJE-7gka_C6IZSYnnPYaAz4IuFZpCGNEFTPDDvRlWvk1Xyp3VJy_wsFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش زندۀ خبرنگار صداوسیما از فرودگاه ایرانشهر پس از حمله
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/134882" target="_blank">📅 01:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134881">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1faf6563c.mp4?token=JnCGqmEYsskwb5BZo0RcqGKg8dWIEPuJBYWPns8d8Xx1GOwzY_OinkBJhmdZydyFtnfMTnULwdcOqwsPlsB-Ra5H7dtOFl2AhEHnlT0faG4-WrAAy1tzRlQl0io_6WBI9mXLoIw0mWm4LXuyMrRiwhUGwiuMHexBbaaX7hZ6rkkLlp0YcK0n5NYspUYB6mz1Ob-QaSjLQ5XeAlNzalQJbetldzXs9hbH8vQsjqfhE5GcIaE4rPSDb2GlKACO50sjihqm0-1WRKOCX0TSvTHCAyYr3URQvqxao5_qTttbiJNVcA7MlBFrA8o6pQFwdNRCDNfSgnO0Z7TOrxR_LmqYXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1faf6563c.mp4?token=JnCGqmEYsskwb5BZo0RcqGKg8dWIEPuJBYWPns8d8Xx1GOwzY_OinkBJhmdZydyFtnfMTnULwdcOqwsPlsB-Ra5H7dtOFl2AhEHnlT0faG4-WrAAy1tzRlQl0io_6WBI9mXLoIw0mWm4LXuyMrRiwhUGwiuMHexBbaaX7hZ6rkkLlp0YcK0n5NYspUYB6mz1Ob-QaSjLQ5XeAlNzalQJbetldzXs9hbH8vQsjqfhE5GcIaE4rPSDb2GlKACO50sjihqm0-1WRKOCX0TSvTHCAyYr3URQvqxao5_qTttbiJNVcA7MlBFrA8o6pQFwdNRCDNfSgnO0Z7TOrxR_LmqYXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رسانه های عربی ادعا کردند که یک رادار آمریکایی در کویت مورد حمله قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/134881" target="_blank">📅 01:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134880">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
از همون روز که ترامپ گفت اگه حکومت مردم رو بکشه حمله میکنم ، همه چیز شروع شد.</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/134880" target="_blank">📅 01:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134879">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
اینترنت تو برخی نقاط اختلال شدید خورده
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/134879" target="_blank">📅 01:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134877">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7619330353.mp4?token=LRkMyo-7It0EmGm8-UFT96KQZK7OhZYkye_c0ZwCJN17YE7WZe3hs1mPoShVmo1jMQ8oRcuy3sqQhPMWX2cvRV8UWZw9lthJlRR8FnFDLhQ1q20xOA_6KssoJWhILlliYOYDKBr3_RkJzQMiBeWb35Crtg-y9T9gIquZP5ufL3S6ZUiM1HqG1a5dtz8Qia7SfZcCjFX8aVYtlkbuWmS3QZSVrRnLB9bs96MS7yOSHBLSADMXEOygreTd0D__romI76lkQEr-nMus5fJ7zg4h9rWldaDxGa7M__XFQczzvGRRCejCGy1l4E6r_EuIFnNKt8Ym-AyI9T95u1iLv-vXyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7619330353.mp4?token=LRkMyo-7It0EmGm8-UFT96KQZK7OhZYkye_c0ZwCJN17YE7WZe3hs1mPoShVmo1jMQ8oRcuy3sqQhPMWX2cvRV8UWZw9lthJlRR8FnFDLhQ1q20xOA_6KssoJWhILlliYOYDKBr3_RkJzQMiBeWb35Crtg-y9T9gIquZP5ufL3S6ZUiM1HqG1a5dtz8Qia7SfZcCjFX8aVYtlkbuWmS3QZSVrRnLB9bs96MS7yOSHBLSADMXEOygreTd0D__romI76lkQEr-nMus5fJ7zg4h9rWldaDxGa7M__XFQczzvGRRCejCGy1l4E6r_EuIFnNKt8Ym-AyI9T95u1iLv-vXyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امشب، پهپادهای ایرانی به مناطقی در کویت، نزدیک مرز عراق، حمله کردند.
🔴
هنوز مشخص نیست که چه اهدافی مورد هدف قرار گرفتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/134877" target="_blank">📅 01:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134876">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
فوووووری/همه پرواز های کشور بدستور سازمان هواپیمایی ایران کنسل شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/134876" target="_blank">📅 01:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134875">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">💢
فوووووووووری/پرواز جنگنده‌های اسرائیلی به مقصد نامعلوم  @MamelekatDaily | پروکسی</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/134875" target="_blank">📅 01:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134874">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
هم اکنون بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/134874" target="_blank">📅 01:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134873">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
12انفجار تو بوشهر رخ داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/134873" target="_blank">📅 01:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134872">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فوری/انفجارهای مهیب در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/134872" target="_blank">📅 00:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134871">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99b324f9f1.mp4?token=QhbBSADcXTM_flaw3EbTvPg9kzBwjjKFZDXmI6B4pPVssmwHdUXc5w8Gc4JrHuYSVUYCL6qjE1yb4G--NgrfzOzUnLD7noTSSf__a2IcTuqVW84ES7j-IBblxRlYDoYqrYKcv_5vgy0G2A3S77BAe_V2BdSP3U6TDh26XAcbU6gBBxoeCuf5XALdc7c5v-5CAl8hb3-1vB4I4l64Wb3jyW6T4YnHOv7iDzDW98FYzIpxac5Td3BNCSfaZVu2nRDTA4WPMrJ1oJCmu2onpTEDScXXZKz8O7Iy7R8vNDFPDemHv7goAQS6kBq46ZvaKlIBLWzu3Eti25BzNM6aKteGpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99b324f9f1.mp4?token=QhbBSADcXTM_flaw3EbTvPg9kzBwjjKFZDXmI6B4pPVssmwHdUXc5w8Gc4JrHuYSVUYCL6qjE1yb4G--NgrfzOzUnLD7noTSSf__a2IcTuqVW84ES7j-IBblxRlYDoYqrYKcv_5vgy0G2A3S77BAe_V2BdSP3U6TDh26XAcbU6gBBxoeCuf5XALdc7c5v-5CAl8hb3-1vB4I4l64Wb3jyW6T4YnHOv7iDzDW98FYzIpxac5Td3BNCSfaZVu2nRDTA4WPMrJ1oJCmu2onpTEDScXXZKz8O7Iy7R8vNDFPDemHv7goAQS6kBq46ZvaKlIBLWzu3Eti25BzNM6aKteGpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام: تفنگداران دریایی آمریکا از یگان یازدهم اعزامی دریایی، در تاریخ ۱۶ ژوئیه، عملیات بازرسی و بررسی را بر روی نفتکش «ام/تی وین یائو» در خلیج عمان انجام دادند.
🔴
تا به امروز، نیروهای آمریکایی مسیر ۳ کشتی تجاری را که تلاش کردند محاصره را بشکنند تغییر داده، یک کشتی که تمکین نکرد را مختل کرده، و سوار بر یک کشتی شده‌اند تا اطمینان حاصل کنند که محاصره دریایی مداوم آمریکا علیه ایران بهطور کامل رعایت می‌شود.
🔴
تنگه هرمز و آب‌های اطراف آن باز و آزاد باقی می‌مانند، به جز کشتی‌هایی که تلاش کنند محاصره آمریکایی را که دیوار فولادی تحمیل می‌کند نقض کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/134871" target="_blank">📅 00:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134870">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
شرکت ملی گاز: صدای مهیب احتمالی امشب در نوشهر، مربوط به تست و هواگیری گاز خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/134870" target="_blank">📅 00:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134869">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/134869" target="_blank">📅 00:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134868">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
بخاطر جنوب لبنان، جنوب ایران رفت</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/134868" target="_blank">📅 00:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134867">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cn0rmS3Oc1UH1tWlXM21SBgn_AYr8VLTgIk4sDv5geXnuHjPnyqAEPoUwTbEeVi22wTxapgTAk8t3wpLtgI7TcvLshD_oH_toZSRtWDRi1zm5wkklho_lKct71fMBRgRuLuxPLLNTXR9NANplxPgBS0oJ5MvrUZmL8lXX7nj5oh5ydVjtWcfQ8fu3WXZ2HjUrHoNrIyex6uC407a0VVQZ1UFi32_aSd6FDP5UGtEkm4iUV_bNjKey2AafYUFzygjXVMLczMl0k2v66EDqysSPnQ-8IUDbhxuu9EZKmKlyTsqlc70SWoAvspPMYyVf-pcdDWLrV_H_FLmMWjLtf1KXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم‌اکنون / وضعیت آسمان ایران و منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/134867" target="_blank">📅 00:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134866">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGSrVJchkn2C1svHn7q1t57cZmz0ioxQfR453_iSf0Y4F3UvkZMgY5Mvaabxgvet8wpSN7w11FbUrnfdBzYPKTuG2ebszuy7ZzCcsTl5BYhitK-rvZVa6TXAcb-vvUTmRQ9q5kTjvSS762DpyMkWBLYhaM3QrDfV9GWFQCQ46CzBDXNsMrOhkKd1Ged6aZDl0UUwzTQaM3Q9M1rapCVD0CLjqa1hWJml-6zVJ94CXagT0QwwZ7xaxxSh7GE6Tu4b7v_Lc4qaolW3QoO3QnMDLH7uJzvFDDyxajyqD3RXqbHLmP7v7LyYfx-NOVkVzdPHxMvaKLfjfiaLCpC9f_S8Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق داده‌های وبسایت فلایت رادار، یک جنگنده اف۳۵ در آسمان امارات کد اضطراری ۷۷۰۰ اعلام کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/134866" target="_blank">📅 00:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134865">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
سنتکام: ما آماده انجام هر ماموریتی هستیم و در حال حاضر ۵۰ هزار نیرو در خاورمیانه داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/134865" target="_blank">📅 00:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134864">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFfhhAueEI9I8KhNINYj2hdVwFS_jpNCHvmcqriSczFDvzqLgXFUuH9F9XmZFKPvBRdlfobc0vAYJoDke_mvzyzq3UiNymkZqZmU7by1c6_O2ZKTmHbJbDUH1z4syIGCaVaxfdKkMM1FSkA983PhqpO5fukY2UzipiO-5DAaulShkz9fVR8cp2UduPUQptTlBV-qCubFRBbvH3iBtF-hH6wYRAvfIweAVBxWVCDr1gPWPupYR4VU3OcksK2r20rZK2amA2A3H8uMDV6gpcOnsaAE75utlxqna2uhX8w1Urkg8HOwjMmFwDlHS4nS-QnEq88vdWBz6NUTLH1x0UYC1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اینترنت موبایل تو بعضی از نقاط دچار افت کیفیت، کندی و اختلال شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/134864" target="_blank">📅 00:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134863">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⭕️
چند نکته بسیار مهم برای حفظ امنیت شما در تلگرام
🔴
برای تنظیم بیشتر موارد، وارد مسیر
Settings > Privacy and Security
شوید.
۱. مخفی‌کردن شماره تلفن
وارد
Phone Number
شوید و این گزینه‌ها را تنظیم کنید:
Who can see my phone number:
روی
Nobody
Who can find me by my number:
روی
My Contacts
بخش‌های
Always Allow
و
Never Allow
را نیز بررسی کنید تا استثنای ناخواسته‌ای وجود نداشته باشد.
تنظیم دوم مانع می‌شود افراد غریبه فقط با ذخیره‌کردن شماره شما، حساب تلگرامتان را پیدا کنند. البته طبق توضیح تلگرام، کسی که شماره‌تان را از قبل می‌داند و در مخاطبین خود ذخیره کرده است، ممکن است همچنان آن را ببیند.
۲. محدودکردن آخرین بازدید و آنلاین‌بودن
در بخش
Last Seen & Online
، گزینه را روی
My Contacts
یا
Nobody
قرار دهید. بخش استثناها را هم بررسی کنید. توجه کنید که هنگام تایپ‌کردن یا ارسال پیام، ممکن است وضعیت آنلاین شما برای مدت کوتاهی به همان شخص نمایش داده شود.
۳. محدودکردن عکس پروفایل
در
Profile Photos
، نمایش عکس را روی
My Contacts
بگذارید. برای حساب‌های کاری یا عمومی بهتر است از عکسی استفاده کنید که اطلاعاتی مثل محل زندگی، پلاک خودرو، محل کار یا اعضای خانواده را آشکار نکند.
۴. جلوگیری از شناسایی از طریق فوروارد
در بخش
Forwarded Messages
، گزینه را روی
Nobody
قرار دهید. با این تنظیم، وقتی دیگران پیام شما را فوروارد می‌کنند، نام فرستنده به پروفایل شما لینک نمی‌شود.
۵. جلوگیری از اضافه‌شدن به گروه‌های ناشناس
در
Groups & Channels
گزینه را روی
My Contacts
تنظیم کنید. در قسمت استثناها نیز فقط افراد مورداعتماد را قرار دهید تا افراد ناشناس نتوانند شما را مستقیماً وارد گروه یا کانال کنند.
۶. مخفی‌کردن IP در تماس‌ها
در بخش
Calls > Peer-to-Peer
، گزینه را روی
Nobody
بگذارید. در این حالت تماس‌ها از سرورهای تلگرام عبور می‌کنند و IP شما برای طرف مقابل آشکار نمی‌شود؛ ممکن است کیفیت تماس کمی کاهش پیدا کند.
۷. فعال‌کردن رمز دومرحله‌ای
وارد
Two-Step Verification
شوید و یک رمز قوی و متفاوت از رمزهای دیگر انتخاب کنید. ایمیل بازیابی نیز باید رمز قوی و تأیید دومرحله‌ای داشته باشد. با فعال‌کردن این قابلیت، صرفاً داشتن سیم‌کارت یا کد پیامکی برای ورود به حساب کافی نخواهد بود.
۸. بررسی دستگاه‌های متصل
در
Devices
یا
Active Sessions
، همه موبایل‌ها، رایانه‌ها و مرورگرهای متصل را بررسی کنید. هر دستگاه ناشناس یا قدیمی را ببندید؛ در صورت تردید، از گزینه
Terminate All Other Sessions
استفاده کنید.
۹. قفل‌کردن خود برنامه تلگرام
گزینه
Passcode Lock
را فعال کنید و قفل خودکار را روی زمان کوتاه قرار دهید. اثر انگشت یا تشخیص چهره را هم فعال کنید تا در صورت بازبودن قفل گوشی، دیگران نتوانند تلگرام را باز کنند.
۱۰. مدیریت مخاطبین همگام‌شده
اگر نمی‌خواهید فهرست مخاطبین گوشی در تلگرام ذخیره و همگام‌سازی شود،
Sync Contacts
را خاموش و از گزینه
Delete Synced Contacts
استفاده کنید. همچنین می‌توانید
Suggest Frequent Contacts
را غیرفعال کنید.
۱۱. برای گفتگوهای بسیار حساس از Secret Chat استفاده کنید
گفتگوهای عادی تلگرام در فضای ابری ذخیره می‌شوند. برای مطالب حساس از
Secret Chat
استفاده کنید؛ این گفتگوها رمزنگاری سرتاسری، وابستگی به همان دستگاه و امکان حذف خودکار پیام دارند.
۱۲. کد ورود را هرگز برای کسی نفرستید
کد ورود تلگرام، رمز دومرحله‌ای، QR ورود، اطلاعات بانکی و فایل‌های ناشناس را در اختیار کاربران یا ربات‌ها قرار ندهید. تلگرام تأکید می‌کند که با ربات‌ها مانند افراد غریبه رفتار کنید.
برای حریم خصوصی بیشتر، بهتر است نام کاربری تلگرام، عکس پروفایل و نام نمایشی شما با شبکه‌های اجتماعی دیگرتان یکسان نباشد؛ چون حتی با مخفی‌بودن شماره، امکان تطبیق هویت از طریق این اطلاعات وجود دارد.
⭕️
حتما از تلگرام رسمی استفاده کنید و از Google Play یا App Store نصب کنید همچنین اگر تلگرام غیر رسمی دارید حذف کنید.
#حریم_خصوصی
#امنیت
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/134863" target="_blank">📅 00:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134862">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
گویا پل فلزی بندرعباس رو هم زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/134862" target="_blank">📅 00:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134861">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-poll">
<h4>📊 به نظرتون چی میشه؟</h4>
<ul>
<li>✓ تهاجم گسترده زمینی و هوایی آمریکا</li>
<li>✓ توافق میشه</li>
</ul>
</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/134861" target="_blank">📅 00:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134860">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
فارس:
حمله به پل خمیر شش کشته و زخمی داشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/134860" target="_blank">📅 00:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134859">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
برق مناطقی از کیش قطع شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/134859" target="_blank">📅 00:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134857">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GjiDdns_BwCEtuO_bMVDQ8USU-5pRUIVTkMkrArWlric0FofMhNAvOqqK0zursFcmUkTGHUpgPhHVijF4uf3pNZssOacBvXz5PTheQTWocqS_rt2JPLenZDeei9VX5WCUbnJgO81cRJfju7zauJKea8ROWKBUtgm9yKKXi2hsZc-f0Zyjzz-7G2UZeVdVa-hhd6UycYNleZa8Lem-jVyh86wh3eQJ4kWNqA0ESaK8uCSu8-LMKISgHRLHvfsGoa7qn0po9PiuInz6bb9dA4xYInfcI-eFiu1GJMJXTNSdSf0CzVBy2gR4IWs5igsJyucqWc8tDNPVgudRiypPte2Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ukkv3Hpag9uOmHhrRK-19UHz_d2s8shPD6ZF_kyirniMfqS_OS5NJ3bgZxFvoG0H4ylXEkJAbURjGkEdUmZypeZE7czcT0T2T2ERoX1xxpLcmffhvJjH63U9dS8HKfmqTenBFS10KOOt_lDpDvvz3YBd6uLRDORzIcP72eSd4Ui_fim76SugwiFydeO22ZLbhwqFPAgmE3_OwS_GQZ0Wu4qsGsFb-Qi0KUotB-URXfmNvca6MgqOWMof4_vrn5nEoockJof8IMm8ddFIIbaILfEc-WIBWyxRRxNYNh8MT0EtNS8E89rche9Xn-yxMc8qCEn6OgOOsdl8JDtca_BdYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
پلی که حملات شب گذشته آمریکا آن را هدف قرار داد، حامل بزرگراه شماره ۷۶ است؛ جادهای اصلی که بندرعباس را به شهر لار و از آنجا به شیراز متصل میکند.
🔴
این بخش، بخشی حیاتی از زیرساخت حملونقل کالاهای تجاری به مقصد و از مبدأ بندرعباس به شمار میرود و همچنین جابهجایی مسافران میان استانهای هرمزگان، فارس و مرکز ایران را پوشش میدهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/134857" target="_blank">📅 00:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134856">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-3eWT4yXWYWoM1B38lMKRcdfAGCY2Fy0pZFLD4RwbWRTC0C1SX4Xe_2Hb4qRfCjR4_2k-cfZP1bUTVNz-CMWOUwHEbYDIbnC_qix8-Id7eusSslzSMs8P5rGzea8qspuGYMYwkjjsheQefOH1YeccpUgFVJqg1mCjEDcFwKU5GTC2jQ4Pyoi9zkrI523AZ8-TfzL5RbRUrvEffNICrr1vTFotQzgJITd1FZQ9tVMknyCFZEITISLgPkiYm8hMVzhW6gpqjmXLNXQEXUnGz9bpSLytJQHE77AlonKGZeQcP2AaiZ1VGAiDlWTrtBHk355mTRHzTaAygS9RjyAlrZzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تمامی پل هایی که بندر خمیر را به بندرعباس متصل می کرد توسط ارتش آمریکا مورد اصابت قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/134856" target="_blank">📅 00:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134855">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uX6V0itlGpigBlM-Ag6q4tdtV_CXyvBAcYYlv0PfK3XNPyGUPNv3TX5QEsvX5Gl6kyOgO3bgV6Ih6re5lqy9KBUpXoCWdwx0GqBzUUZkiyehq8cy8YQ49guNwWwb1_TvzQ-AjMmwx0u7qPs6wsmQY65lRlv8YQ4tUt3IsiX9VxKhIPgz1pIBeiocmqs9sZovmUQNJaZfetierj8B8D6Uvz30KbM5eTzpkIzAaOt1TAvG6IMl0DjLyzrFPidg103y6_xWb7SeUDQYMaMVEOhRTN09Yq2w5RYwX7GbCuyxcjbm1zwlqCK7-0vPFM-HQZJCshC4ntNh7VTZsWxhR3uTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اولین تصویر واضح از پل‌ِ بندرخمیر که مورد هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/134855" target="_blank">📅 00:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134854">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⭕️
الونیوز فقط در تلگرام
💬
و توییتر
❌
فعال هستش
🔴
سایر شبکه های اجتماعی چه داخلی چه خارجی که با نام الونیوز فعالیت می‌کنند مرتبط به ما نیست و پیشنهاد میکنم که لفت بدید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/134854" target="_blank">📅 00:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134853">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
تمام راه‌های ارتباطی به جنوب، فرودگاه، پل‌ها، راه آهن و... دارن دونه دونه نابود میشن! آمریکا بدون هدف کاریو نمی کنه. یه سناریو بزرگ و احتمالا حمله زمینی پشتشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/134853" target="_blank">📅 00:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134852">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
فوری/صدا و سیما: دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی آمریکا هدف قرار گرفته شده و ۲ نفر مصدوم شدن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/134852" target="_blank">📅 00:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134851">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/134851" target="_blank">📅 00:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134850">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/134850" target="_blank">📅 00:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134849">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
فوری/صدا و سیما: دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی آمریکا هدف قرار گرفته شده و ۲ نفر مصدوم شدن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/134849" target="_blank">📅 00:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134848">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96d13ca129.mp4?token=DY4-qOfgPNH9xaWSI1Kn1uh54qgoQaNaha8hUXEUqZ37Tfa81OY2xJqizabLuhFOvi922Rc97ckMCYSFUNS2esYZEx67-xy7UXsngX_blOLkcplENqZbsPpKRDy_MfJp5Y22PwIq2sxs7lwBzvwX1i5EQnRay3RiFGLb-VrObSt7vVISpsQ20bh1zZm9oQXfAO2jg_9W82cZ6xgOEwlTPLayY2e2tF9QbKtTccvoOWMW2GPMc6iAlRqsxvOG78YILoH7c4Sm6YN_i3R0I_RZ7y_1TFkqJ-4z6Sb2tLTO_F01LCAgrgkrNG7tcW-AN4xRtPzWufnYUEGnNZDQeFWabw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96d13ca129.mp4?token=DY4-qOfgPNH9xaWSI1Kn1uh54qgoQaNaha8hUXEUqZ37Tfa81OY2xJqizabLuhFOvi922Rc97ckMCYSFUNS2esYZEx67-xy7UXsngX_blOLkcplENqZbsPpKRDy_MfJp5Y22PwIq2sxs7lwBzvwX1i5EQnRay3RiFGLb-VrObSt7vVISpsQ20bh1zZm9oQXfAO2jg_9W82cZ6xgOEwlTPLayY2e2tF9QbKtTccvoOWMW2GPMc6iAlRqsxvOG78YILoH7c4Sm6YN_i3R0I_RZ7y_1TFkqJ-4z6Sb2tLTO_F01LCAgrgkrNG7tcW-AN4xRtPzWufnYUEGnNZDQeFWabw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب عزیزم
❤️
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/134848" target="_blank">📅 00:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134847">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
فووووووری/یک مقام آمریکایی به ان بی سی: همانطور که رئیس جمهور گفته بود این هفته حمله به زیرساخت‌ها، پل‌ها و نیروگاه‌ها انجام میشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/134847" target="_blank">📅 00:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134846">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
راه‌های ارتباطی و زیرساخت‌های مهم جنوب ایران رو یکی‌یکی دارن می‌زنن، ولی حکومت ملاها مثل همیشه نه جون مردم براش مهمه، نه امنیت کشور و نه آینده ایران.
🔴
با این اتفاقاتی که داره می‌افته، بعید نیست دارن برای حمله زمینی برنامه ریزی می‌کنن؛ جنگی که باز هم هزینه‌ش رو مردم بی‌دفاع ایران باید بدن، نه اونایی که خودشون و خانواده‌هاشون جای امن نشستن.
🔴
آخرِ همه این ماجراها یه چیز کاملاً روشنه: جمهوری اسلامی رفتنیه و سقوطش حتمیه. فقط معلوم نیست قبل از اینکه به زباله‌دان تاریخ بره، قراره چقدر خون از مردم بگیره، چقدر کشور رو ویران کنه و چقدر هزینه روی دست ملت بذاره، اما جنایت‌ها و ویرانی‌هایی که به جا گذاشته، هیچ‌وقت از حافظه مردم ایران پاک نمی‌شه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/134846" target="_blank">📅 00:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134844">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
فوری / قشم ۴ انفجار
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/134844" target="_blank">📅 00:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134843">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd604b00c.mp4?token=VVGDvKJBn9Gw5uBAxRqVeHEluNN4H-j0l_mGLrkwVj9ufHyyLQwEHLThRQ8sFHFPwv_6THfW1NpZTDs9YE8on9ZHzuVwXjAQNdahCOXg5BLzrz9i6HqxejXnprT92WX_WXHPHN1LUMSsTgq2GgpwLPhppKHYGQdSe15ht_l7JF8T88RXRAUf--BP9jdZmiGL9Dc9AnTp33ML30J_7P0b3j6DGszrLSKf3TWJpkWVUzdccGuc3wd-doA_Am46vcTv7sgAwfvIF3ieOo-iVZ32AVWbnhup3CCuOqzQmmfsdJgA612Jz0K1q0F5yovHksikyKIE8xvlHvX1Y-a5Wjwz9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd604b00c.mp4?token=VVGDvKJBn9Gw5uBAxRqVeHEluNN4H-j0l_mGLrkwVj9ufHyyLQwEHLThRQ8sFHFPwv_6THfW1NpZTDs9YE8on9ZHzuVwXjAQNdahCOXg5BLzrz9i6HqxejXnprT92WX_WXHPHN1LUMSsTgq2GgpwLPhppKHYGQdSe15ht_l7JF8T88RXRAUf--BP9jdZmiGL9Dc9AnTp33ML30J_7P0b3j6DGszrLSKf3TWJpkWVUzdccGuc3wd-doA_Am46vcTv7sgAwfvIF3ieOo-iVZ32AVWbnhup3CCuOqzQmmfsdJgA612Jz0K1q0F5yovHksikyKIE8xvlHvX1Y-a5Wjwz9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پل لار - بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/134843" target="_blank">📅 00:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134842">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
سر فشار رقاصه‌های پرچم ایرانمون داره نابود میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/134842" target="_blank">📅 00:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134841">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
فووووووری/راه آهن بندر عباسو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/134841" target="_blank">📅 00:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134840">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dv2tbnWgJ4gR6kxO4bSLI1BZ9z3IqYY8ooTb0E4DfXoGfSzRvjv2hFyeem09NlzAdiLQ15Tu0VZsQB-7P9qktY-sfWv6dDy52xXPMznroa-U-QRnNvnz2jWbibR-tlhUXVtBX-XVXQwdIlCbR0sdNi-lLX7NamnvSN7zNhEph0YMDQkysby62AW9PcbXdRPB0y7CalAjmvqvnjXpJFhAeS1SC-NaZlWbblw1Oesm1qPglUgUx1I3go0eYs1IbygyzPwq8V2139Nxc8xQhpFtxl-VGse-PSazkjQgMF5hKTkxevYE_aIefDxsbR16W4PKV8NK6HjQR7cvp96dl0085A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: آرزوی شهادت دارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/134840" target="_blank">📅 00:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134839">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
صداوسیما: صدای ۴ انفجار در محدوده ساحل جنوبی قشم شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/134839" target="_blank">📅 00:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134838">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
فوری/سی‌بی‌اس به نقل از مقام آمریکایی: دستورالعمل‌های مربوط به حملات آمریکا به‌روزرسانی شده‌اند تا شامل پل‌ها و اهداف ارتباطی و تدارکاتی شود، با هدف افزایش فشار بر ایران.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/134838" target="_blank">📅 00:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134837">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
مقاومت اسلامی عراق برای کشتن ترامپ ۱۰ میلیون دلار جایزه تعیین کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/134837" target="_blank">📅 00:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134836">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
فعالیت جنگنده ها بر فراز منامه، بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/134836" target="_blank">📅 00:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134835">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
تسنیم: آمریکا شروع به زدن زیرساخت ها و پل ها کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/134835" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134834">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
به لحظات ملکوتی قطع اینترنت داریم نزدیک میشیم.
🔴
خشاب های VPN خودتون رو پر کنید.</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/134834" target="_blank">📅 23:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134833">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
تصاویری از حمله به پل در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/134833" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134832">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
پل کهورستان بندرعباس هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/alonews/134832" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134831">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
تصاویری از حمله به پل در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/134831" target="_blank">📅 23:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134830">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
تصاویری از حمله به پل در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/134830" target="_blank">📅 23:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134829">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
مهر: دقایقی پیش، صدای حدود ۶ انفجار پیاپی در حوالی شهرستان حمیدیه شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/134829" target="_blank">📅 23:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134828">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
انفجار در کهورستان بندرعباس.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/134828" target="_blank">📅 23:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134827">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3efbf07c20.mp4?token=enJBJ-oPFKHOZwhirBGdv4R1QuCP6I1b10GXL1GfYa1Uc9Ct8bJzSguBUaCEinQzaUlbCnsknIT8W8_ueFIW6dABcMGgRaYufAWfLm9Rtq4s4Kvngd3aJhu2_MkMlGKioDETw_2cnyBZC7ZjiQH28fJ9l2dey-662sD6V5k4y68HP50nhNPA6kYDhW-QdM48IawsrtiRXOK-yV_M4EpQ9-p4sLLiNXRArPAps9cAVwTGu7Ax-C0UdOHvYWwHbfWXgut--0AFbG6fq-tlj_m7qySmpGbhJcYUaJ5aN02QesF-Ql1h1JgKdE65JUR_TctAewgwGONDUrZwuNr0ZX18FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3efbf07c20.mp4?token=enJBJ-oPFKHOZwhirBGdv4R1QuCP6I1b10GXL1GfYa1Uc9Ct8bJzSguBUaCEinQzaUlbCnsknIT8W8_ueFIW6dABcMGgRaYufAWfLm9Rtq4s4Kvngd3aJhu2_MkMlGKioDETw_2cnyBZC7ZjiQH28fJ9l2dey-662sD6V5k4y68HP50nhNPA6kYDhW-QdM48IawsrtiRXOK-yV_M4EpQ9-p4sLLiNXRArPAps9cAVwTGu7Ax-C0UdOHvYWwHbfWXgut--0AFbG6fq-tlj_m7qySmpGbhJcYUaJ5aN02QesF-Ql1h1JgKdE65JUR_TctAewgwGONDUrZwuNr0ZX18FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حمله به پل در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/alonews/134827" target="_blank">📅 23:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134826">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
فوری/ طبق گزارشات، یک پل در بندرعباس هدف قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/134826" target="_blank">📅 23:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134825">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
فوری/انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/134825" target="_blank">📅 23:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134824">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
فوری/حملات شدید به قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/alonews/134824" target="_blank">📅 23:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134823">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
فوری/ورودی های پایگاه زیرزمینی عقاب 44 ایران جمهوری اسلامی ایران توسط آمریکا بمباران شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/alonews/134823" target="_blank">📅 23:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134822">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✅
فوووووووووری/حمله زمینی   ️رشیدی کوچی؛ نماینده سابق مجلس: حمله‌ زمینی آمریکا به ایران قطعیه. اگه تا الانم حمله نکرده به خاطر گرمای شدید هواست
✅
@AkhbareFouri</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/134822" target="_blank">📅 23:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134821">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
فوری / حمله به فرودگاه ایرانشهر ، استان سیستان و بلوچستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/134821" target="_blank">📅 23:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134820">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
سنتکام: پس از پاکسازی مین‌ها، گذرگاه‌هایی در تنگه هرمز بازگشایی شده و در حال حاضر دریانوردی در این منطقه ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/alonews/134820" target="_blank">📅 23:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134819">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
سخنگوی سنتکام: ما آماده انجام هر ماموریتی هستیم و در حال حاضر ۵۰ هزار نیرو در خاورمیانه داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/134819" target="_blank">📅 23:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134817">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/507e824d84.mp4?token=AyfrSQl--JyKPc5csiH5_YnbMtygF20lCfsKAFTcc3dZNRm4p2FCjNFSrLWpwwAFjC3EbE5CB6kEP-a4rlomFDvFvGL0K4Zo0M7_BLnjoJEyYHtRkHrTLcW7M9WI9OBE6eh7ccBX9wMZlb-lqaMbVRCUgp3fM2BK_3KnlDhY_6KWfcgVZy0w16V8CKtZ43BujFBHSjNWN8m-D9Qgy4Y5xzo2sc9nJEkgkbpJ7olXyAr5Y6ad_yj_dgYIDh_AcE8sSKSr3iLOWdf78VbfHXlc_2y5K_nxkRaFRYAgnDncKt2X6qtj6vMhqo_lEvP9kzRU-RQNr-cP9FTdG39R0P4Phw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/507e824d84.mp4?token=AyfrSQl--JyKPc5csiH5_YnbMtygF20lCfsKAFTcc3dZNRm4p2FCjNFSrLWpwwAFjC3EbE5CB6kEP-a4rlomFDvFvGL0K4Zo0M7_BLnjoJEyYHtRkHrTLcW7M9WI9OBE6eh7ccBX9wMZlb-lqaMbVRCUgp3fM2BK_3KnlDhY_6KWfcgVZy0w16V8CKtZ43BujFBHSjNWN8m-D9Qgy4Y5xzo2sc9nJEkgkbpJ7olXyAr5Y6ad_yj_dgYIDh_AcE8sSKSr3iLOWdf78VbfHXlc_2y5K_nxkRaFRYAgnDncKt2X6qtj6vMhqo_lEvP9kzRU-RQNr-cP9FTdG39R0P4Phw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده های آمریکایی به طور گسترده در آسمان بحرین پرواز می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/134817" target="_blank">📅 23:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134816">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
صدای ۲ انفجار در شهر بوشهر شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/134816" target="_blank">📅 23:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134815">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b1bc0ea2b.mp4?token=hSplCoue1PWoKbxvphoC02lOR6IBYQclQkC3KLFOGOtqTviJloO8qJmfHP62P54j--lr5YCOzj9ogJ58VkGmboGoFs5YMVYlS3xFB7BGGSyMnnZzLARkwYwAx6tEuoKbcB6i-LXOE5YkaIwQnsRT-gJwTzFz0pelWKU-3VCnb1emJsGPu3gXlbfUxXWpYIMyr-UDEYNCehB5UBDlPW1nZV0pqajejpAExtG3L0bqCGfbw1ykkfEZEesNKi392BPfLsj0LRcJ0UCADbi9Tq0b81YoJ-MtRvyeeDcxJYDzXD0RBj0oUnbPsEFIxfJ4FWZD_PC1eh8US3xVKtcuuB1hgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b1bc0ea2b.mp4?token=hSplCoue1PWoKbxvphoC02lOR6IBYQclQkC3KLFOGOtqTviJloO8qJmfHP62P54j--lr5YCOzj9ogJ58VkGmboGoFs5YMVYlS3xFB7BGGSyMnnZzLARkwYwAx6tEuoKbcB6i-LXOE5YkaIwQnsRT-gJwTzFz0pelWKU-3VCnb1emJsGPu3gXlbfUxXWpYIMyr-UDEYNCehB5UBDlPW1nZV0pqajejpAExtG3L0bqCGfbw1ykkfEZEesNKi392BPfLsj0LRcJ0UCADbi9Tq0b81YoJ-MtRvyeeDcxJYDzXD0RBj0oUnbPsEFIxfJ4FWZD_PC1eh8US3xVKtcuuB1hgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شلیک موشک از کویت به سوی اهواز در ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/134815" target="_blank">📅 22:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134814">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
به اهواز با موشک تاماهاک حمله کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/alonews/134814" target="_blank">📅 22:44 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
