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
<img src="https://cdn5.telesco.pe/file/Bu7VwPAiDe0HgWd9MwAf7bpL7nhVuGYh-q5tuMwakQCqlxQP7OhtJJigRAdxLyw5MWa3mpy17CY4oOPmUJwgjfEmmAt9OX8yHEH2uDmqgiP_fNGWPoKs-o7OFlJ3ZfdmuIEW4vZ33QDHrgpThJ5DoCul3BsXERGfDpMSjDDXGzZFS43PTSJ2j3AqK-WzuyNOaRxo97lQyHBwqT_j92G69z0ejbzYMn57_rqWSJWQBExq10GZ-BnzEe3xF6hbYyltbpNixSgrzpXnsl2Yxra_K1C2Z_LeUlC_wDFVw-FedoZ0PLxMtbqbvycGnnXT3ntatXvpPRLRIpikpZAPf-XiAQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 392K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 20:42:00</div>
<hr>

<div class="tg-post" id="msg-107827">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56554104cf.mp4?token=j2Nb-is624Tml-6i-MQmTMxPZTCMyQTy8Yd3PWb3SS4Yg4By1ak4O1rbFlPzZNC3IlJ7fbyn9LgmZJFDhdb13MTgRyeBfvKn-wlTkcSXb1FRAdnbdiJDX3L6yskrQt9AqbdvCBTJSrQzh9wt0To1z2ZjigP0EUsHRGVwpci1LBkCf3PqM8VN2Fhtox_VbfRVOhkG2tGkg67_w4jQgAyqMsjcDCTYhCRaeQx-OMYa7KiQDR-DzHAVwFFZI-GbVgXNFU5inJozFUGJtmeAMEM8x-Dzyk5Or4ni0-lcqF4DCn71eAlMlMoVLoNqXOLlHIGkzOvqYkoGL8niFTRoO86rznydVgKEH5Yd3zM2TU-T39upVu9fXWrd2Z6wZ-OdGuH5mo2P8NYscK8UVsPVPT34CFOx9TPrmgHeKdi6g82iqKL6kjFCoMqWO-SiWzRIPHsqHSfb_TT9xA6_2kpevRS0CZjtar0AbmlXyt-TMMV0XbG5PWozjW1i1gjAGF5zmxKPKcxtPSypttx5kRVkgAD2ozCyV3TmJmCYCSmnt-o6XUa4M-p4M5HD8beOocJ081BjaTJyozEx5wZ-pvV2P4BW1fbDmEBwVTMauOk7qkYjYjW-RQiNNi8fsXx5R9AV0P3-ONyF5tNFEJLHaQArdGhca2sr14UvPVK6cwmWuVIFu_I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56554104cf.mp4?token=j2Nb-is624Tml-6i-MQmTMxPZTCMyQTy8Yd3PWb3SS4Yg4By1ak4O1rbFlPzZNC3IlJ7fbyn9LgmZJFDhdb13MTgRyeBfvKn-wlTkcSXb1FRAdnbdiJDX3L6yskrQt9AqbdvCBTJSrQzh9wt0To1z2ZjigP0EUsHRGVwpci1LBkCf3PqM8VN2Fhtox_VbfRVOhkG2tGkg67_w4jQgAyqMsjcDCTYhCRaeQx-OMYa7KiQDR-DzHAVwFFZI-GbVgXNFU5inJozFUGJtmeAMEM8x-Dzyk5Or4ni0-lcqF4DCn71eAlMlMoVLoNqXOLlHIGkzOvqYkoGL8niFTRoO86rznydVgKEH5Yd3zM2TU-T39upVu9fXWrd2Z6wZ-OdGuH5mo2P8NYscK8UVsPVPT34CFOx9TPrmgHeKdi6g82iqKL6kjFCoMqWO-SiWzRIPHsqHSfb_TT9xA6_2kpevRS0CZjtar0AbmlXyt-TMMV0XbG5PWozjW1i1gjAGF5zmxKPKcxtPSypttx5kRVkgAD2ozCyV3TmJmCYCSmnt-o6XUa4M-p4M5HD8beOocJ081BjaTJyozEx5wZ-pvV2P4BW1fbDmEBwVTMauOk7qkYjYjW-RQiNNi8fsXx5R9AV0P3-ONyF5tNFEJLHaQArdGhca2sr14UvPVK6cwmWuVIFu_I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
پیمان حدادی مدیرعامل پرسپولیس: ما زور داشتیم و تورنمنت سه‌جانبه برگزار کردیم. اینکه قهرمان فصل‌گذشته معرفی نشد کاملا منطقی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 610 · <a href="https://t.me/Futball180TV/107827" target="_blank">📅 20:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107826">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇷
۸۱ سال گذشت؛ کلیپ ویژه سالروز تاسیس باشگاه استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/Futball180TV/107826" target="_blank">📅 20:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107825">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_YhsFB5hSWR_uKKWIZDsbnKnGE6cZUVigEo6OH-pkWyTl8-nYgfi22NabL-XW612TvYCssT-2a6TMWhIq7hGxTmsg1LBOOeAfKxPcRCwQ3cV9xZqAqcujQQzeGOfvngSblwaVIZgZmebRc1Zu21MQypN2l2qmc-IDJJM_-utggYbgUD6JeIrwJWns9DD24OhW0bwbalPFZ-ppFYKczDAiCsahn1hI6-gH9pTg6wEGnSgDRfwXYTrnd3u386RKS77NVjZ8PorN_DiafZr_kSrA618zilHzjGtbhXGg7T1sXme9DLC5FFYJgmXngkBNWW0uHD7Tp6dyKlHA3o8W5e4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
‼️
پیمان‌حدادی: قرارداد اورونوف را تمدید کرده بودیم که بتوانیم بعد از درخشش احتمالی این بازیکن در جام‌جهانی این بازیکن را بفروشیم ولی برنامه‌ریزی موفقی نداشتیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/Futball180TV/107825" target="_blank">📅 20:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107824">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‼️
حمید مریخ مدیر برنامه یاسر آسانی و نزدیک به باشگاه استقلال قصد داره که شیرزاد آسانوف هافبک میانی 23 ساله تیم ملی ازبکستان رونیم‌فصل به تیم استقلال بیاره و منتظر تاییدیه بختیاری زاده‌ست.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/Futball180TV/107824" target="_blank">📅 20:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107823">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50712b5d4b.mp4?token=gjwi6Xf7k_MreJ_-DDKbKHLuF_D1NmwDrVFNbUqHSivFbXWtQ5rSe9u8t8uMcTfZRDllrGRT7i7BVhUTSar7ZyMnVcAVYN3igftT6O1SSP-vZNz5AssYJCHuo8ySPBzbvtbCGvAVYCvXWYHe1kH7UQIXzdD2e6jTlXB5FmYtXaYn5YDDadXQGIyC8KU27gVuGjU_bSDq0UlamXvWUROskBxwVVTmKpTJZhMblhCAXCsm_Q-gzOV_0S4luk7k6AdKHPQf4dwaXlkBUsv4lzK1eQ7Wk84mfYF7-Pf9dAIUkbdBEqLhhc_cSx_FISnXHzwU5dPbLjOehF8RYv9Hp82yeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50712b5d4b.mp4?token=gjwi6Xf7k_MreJ_-DDKbKHLuF_D1NmwDrVFNbUqHSivFbXWtQ5rSe9u8t8uMcTfZRDllrGRT7i7BVhUTSar7ZyMnVcAVYN3igftT6O1SSP-vZNz5AssYJCHuo8ySPBzbvtbCGvAVYCvXWYHe1kH7UQIXzdD2e6jTlXB5FmYtXaYn5YDDadXQGIyC8KU27gVuGjU_bSDq0UlamXvWUROskBxwVVTmKpTJZhMblhCAXCsm_Q-gzOV_0S4luk7k6AdKHPQf4dwaXlkBUsv4lzK1eQ7Wk84mfYF7-Pf9dAIUkbdBEqLhhc_cSx_FISnXHzwU5dPbLjOehF8RYv9Hp82yeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پیمان
حدادی مدیرعامل پرسپولیس: قرارداد 5 بازیکن خارجی ما 4 میلیون و 80 هزار دلار است
🔴
در نیم فصل و تابستان بعدی بازیکن خارجی نخواهیم گرفت. ابتدای فصل بخاطر همین کادر ایرانی گرفتیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/Futball180TV/107823" target="_blank">📅 20:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107822">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65b6b0e4ee.mp4?token=JP5IHFdy_wN5YZQRSHsGeBWixbyVydKKqb0PeWkryTvychjXuwjoB0b12IDdLvJ6nNQhplsQKUhgNU9dzCVzBY40lpEnq3lhBMDRZKEXIWTUsaBqilHWdUyH1_1TpNevSUizq2x4USs4m3_DtqP4rxXCtBdMJbr4oCGNNiGNGT9lR1tIudfzXMRG4vinVBGCumllJQZXYEfdo3CbtB9Q4wniv1dWOIdc8kKPDHnzsqk1jDkVgS3F2SjTzV8WNxcOHVo7707ResKHVh6z_tzVKBdXeCUpCPS2FR0piv2YlS0QC3xSTF5jviF4YvFlU-Uqb5C5VsAleNZM4EBRCHk3iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65b6b0e4ee.mp4?token=JP5IHFdy_wN5YZQRSHsGeBWixbyVydKKqb0PeWkryTvychjXuwjoB0b12IDdLvJ6nNQhplsQKUhgNU9dzCVzBY40lpEnq3lhBMDRZKEXIWTUsaBqilHWdUyH1_1TpNevSUizq2x4USs4m3_DtqP4rxXCtBdMJbr4oCGNNiGNGT9lR1tIudfzXMRG4vinVBGCumllJQZXYEfdo3CbtB9Q4wniv1dWOIdc8kKPDHnzsqk1jDkVgS3F2SjTzV8WNxcOHVo7707ResKHVh6z_tzVKBdXeCUpCPS2FR0piv2YlS0QC3xSTF5jviF4YvFlU-Uqb5C5VsAleNZM4EBRCHk3iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
‏همسر
بیژن مرتضوی: تو مجازی به آقا بیژن فحش میدید ولی تو واقعیت دنبال عکس و امضا هستید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/Futball180TV/107822" target="_blank">📅 20:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107821">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe589a60ed.mp4?token=VSAFn_Foi4zydxPRyFtdp3eZkJ90Fwdi2JtpdgPIWKdkJhK5FphNAz6OHFMxWfhX9mXcYmObNqOsDNQRPBCm_4cegoh8RbTRmaDp5zQ0mQsIAWotHUOfxbx6l5ZGORO2cAVdccbL8QGGGrW4eKVn4FGOW93l5wQ5JkeFDgvzn33WYPMZV18PpeYEo6Cz4sQEOvIISMcsk_REEtiH5c-05XZFZ2gwKCb81cKdPHev2wDogI1oAhk4NqNxMnazlbIVcDXxj797lLxmimigfYe8cguewx0Y3IGB_5C6fKskGt-zSTjujjIOSdUoHtljRVuw4dBSwDNPZorNiHyjMh0otQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe589a60ed.mp4?token=VSAFn_Foi4zydxPRyFtdp3eZkJ90Fwdi2JtpdgPIWKdkJhK5FphNAz6OHFMxWfhX9mXcYmObNqOsDNQRPBCm_4cegoh8RbTRmaDp5zQ0mQsIAWotHUOfxbx6l5ZGORO2cAVdccbL8QGGGrW4eKVn4FGOW93l5wQ5JkeFDgvzn33WYPMZV18PpeYEo6Cz4sQEOvIISMcsk_REEtiH5c-05XZFZ2gwKCb81cKdPHev2wDogI1oAhk4NqNxMnazlbIVcDXxj797lLxmimigfYe8cguewx0Y3IGB_5C6fKskGt-zSTjujjIOSdUoHtljRVuw4dBSwDNPZorNiHyjMh0otQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
اقدام تلافی‌جویانه امید عالیشاه برابر خداداد
😆
😆
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/Futball180TV/107821" target="_blank">📅 19:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107820">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6340210c7d.mp4?token=gdob-c-dtRO-tAoT21jTK900WIS9kQYVr57X2Kyi_q-BfsgJQqY8QOLP67rDFnczXof7KymNjQcPlifiAmMHCOJG18YUdmtiAJzIpF-IAwovu1iAApvVtAUP7WbEnHA4GteORtRVWt3Og9bmomz-qU76VJzDYnBtgGhCPr2yxaIt5vtZtt3Jd3JoNub53ZO7y-J7e7RvW2-Z8dcz-ccPck6WQiJ3Tj42IpNQY0BwEmF7SntvA0DoFs2FyZvWPOVBVISO7saEChPOPD_gxNb-auYSvWG76PJbY6V_suHsST5MIjpQLX_c21lR2xT1UR95V2ugDAf5fFH4XUCu2zDU7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6340210c7d.mp4?token=gdob-c-dtRO-tAoT21jTK900WIS9kQYVr57X2Kyi_q-BfsgJQqY8QOLP67rDFnczXof7KymNjQcPlifiAmMHCOJG18YUdmtiAJzIpF-IAwovu1iAApvVtAUP7WbEnHA4GteORtRVWt3Og9bmomz-qU76VJzDYnBtgGhCPr2yxaIt5vtZtt3Jd3JoNub53ZO7y-J7e7RvW2-Z8dcz-ccPck6WQiJ3Tj42IpNQY0BwEmF7SntvA0DoFs2FyZvWPOVBVISO7saEChPOPD_gxNb-auYSvWG76PJbY6V_suHsST5MIjpQLX_c21lR2xT1UR95V2ugDAf5fFH4XUCu2zDU7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
مهدی مهدوی‌کیا در واکنش به اتفاقی که برای کریستیانو رونالدو در تیم ملی پرتغال افتاد گفت:
🔹
«وقتی این خبر رو خوندم واقعاً ناراحت شدم؛ یک ابرستاره مثل رونالدو شایسته چنین رفتاری نیست. کسی که سال‌ها برای تیم ملی پرتغال همه‌چیزش رو گذاشت و یکی از مهم‌ترین چهره‌های تاریخ این تیم بود، حالا به جایی رسیده که اردو رو ترک می‌کنه. به نظرم باید احترام بیشتری برای بازیکنی با این سابقه و جایگاه قائل بود.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/Futball180TV/107820" target="_blank">📅 19:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107819">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae14913e57.mp4?token=EXUDrF75gWTTqP_6H-uja-oFrq96dmhtcupf5NjpKVVr7fJELGNVd_eFX95SBFwYUOiTluNuMz46gPTfs0lGtn3w-iwRkdcGxMUd3l-KaxDGu27xo5Z44QSl-2v8bxwjP81gYliItrFtK1RmzfviowHDtmptFAXpcsaXspEzuVC3Dgb0_TArlgcpobNpxOhiDbDQXVvYuhbiEzFENWlmU_AIe7Z8Cg-rfuO5Ru1ek5CjL5lKXLHohX-PQnmfAfaA99oOLM45u4QLUTFOAylOdufb3FfQC4CStjty1m3sahFUzl-mB4KZ_vby89wsIEkU_wBKanzW_P082h1LcN8kVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae14913e57.mp4?token=EXUDrF75gWTTqP_6H-uja-oFrq96dmhtcupf5NjpKVVr7fJELGNVd_eFX95SBFwYUOiTluNuMz46gPTfs0lGtn3w-iwRkdcGxMUd3l-KaxDGu27xo5Z44QSl-2v8bxwjP81gYliItrFtK1RmzfviowHDtmptFAXpcsaXspEzuVC3Dgb0_TArlgcpobNpxOhiDbDQXVvYuhbiEzFENWlmU_AIe7Z8Cg-rfuO5Ru1ek5CjL5lKXLHohX-PQnmfAfaA99oOLM45u4QLUTFOAylOdufb3FfQC4CStjty1m3sahFUzl-mB4KZ_vby89wsIEkU_wBKanzW_P082h1LcN8kVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
💙
فتاحی رئیس سازمان فوتبال باشگاه استقلال: نمی دانم پرسپولیسی‌ها علیه یاسر آسانی چه مستندانی دارند/ وقتی باشگاه السد قطر با آن تیم حقوقی قوی که دارد از باشگاه استقلال شکایت نمی کند یعنی حضور یاسر آسانی هیچ مشکلی نداشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/Futball180TV/107819" target="_blank">📅 19:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107818">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70613f964d.mp4?token=QsiUmW2w-lzq7IdI4SvXr-WG0Afpbvk0K0fADvQy6ozYY4xrJYMJ2S5LIODiIEVHp_Z8tmt_ONSkQBZ813Ii2iNqSzxgi67LSMHRCJ3erknknAANR1jsO36tfjDF9y7VjWhEJE2hRAaJclEUrlGk486ya5WlFBU4gFYA3lZUXbUWJbs-V1vUwQnmE_AQmfu0-H7EoqpLMz6U-MgbVImw6B4RtStzEnaKI1Vjdjer4vMGqxWpyzF2lT3xu1sK7O674HgtF-rBnIyAc92PRQcJ2-OiOJWQ59y8Aab335XfeMYxlUvuzckP_-KUub7jGRg1nJgtPLeurSqph6xNSp7ITTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70613f964d.mp4?token=QsiUmW2w-lzq7IdI4SvXr-WG0Afpbvk0K0fADvQy6ozYY4xrJYMJ2S5LIODiIEVHp_Z8tmt_ONSkQBZ813Ii2iNqSzxgi67LSMHRCJ3erknknAANR1jsO36tfjDF9y7VjWhEJE2hRAaJclEUrlGk486ya5WlFBU4gFYA3lZUXbUWJbs-V1vUwQnmE_AQmfu0-H7EoqpLMz6U-MgbVImw6B4RtStzEnaKI1Vjdjer4vMGqxWpyzF2lT3xu1sK7O674HgtF-rBnIyAc92PRQcJ2-OiOJWQ59y8Aab335XfeMYxlUvuzckP_-KUub7jGRg1nJgtPLeurSqph6xNSp7ITTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های امیرحسین صادقی بازیکن اسبق استقلال و تیم‌ملی درباره وضعیت وخیم اقتصادی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/107818" target="_blank">📅 18:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107817">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf836fb3bd.mp4?token=tXboIadOZBcKdv8E3Cb_UtTLMruNzxS3Q1HGyWTrbZ6rlU7xwfabNfSwoWT0iCGYjh9TuvQ5uSC-ersOkjEYEKg1DjrPgbrgVia0wqas85ioazW8e4lVo2llvc1OpCH25RV7WWAWhdxuckGsTlbay92HWK0SRYW3ZmUCKOAwNcsN70dVr92-C-j31XHdd-0PbAiAon8ve6ktd2oySoqEiO1myNYqHxNCoYkyvKuVsw0D_z_F8G1fTij90Nq8vHRl72Ref3MrrahstusKPiNxwkGiwoFBVEFFX24tHqrPwsFyOLm5WJQGl1vCdrj2uY6lLlO-uK8YqN09uXqnNsQnEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf836fb3bd.mp4?token=tXboIadOZBcKdv8E3Cb_UtTLMruNzxS3Q1HGyWTrbZ6rlU7xwfabNfSwoWT0iCGYjh9TuvQ5uSC-ersOkjEYEKg1DjrPgbrgVia0wqas85ioazW8e4lVo2llvc1OpCH25RV7WWAWhdxuckGsTlbay92HWK0SRYW3ZmUCKOAwNcsN70dVr92-C-j31XHdd-0PbAiAon8ve6ktd2oySoqEiO1myNYqHxNCoYkyvKuVsw0D_z_F8G1fTij90Nq8vHRl72Ref3MrrahstusKPiNxwkGiwoFBVEFFX24tHqrPwsFyOLm5WJQGl1vCdrj2uY6lLlO-uK8YqN09uXqnNsQnEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
فریادهای عجیب یه نماینده مجلس جلو قالیباف به همتی رئیس بانک‌مرکزی: به والله میرم خودمو جلو بانک مرکزی آتیش میزنم
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/107817" target="_blank">📅 18:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107816">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esKZieHQyh9Q3TjnrIceZfEbNjw-_6dayAiuzW4I-8cLf_r6SN3p_y7Yq_M1Sulz65MVVo0r2WCUHtkyY8K7vO9zPBHNdBcfQy2pfjaehVu6AciWI5l2QX4Y2RNb0j6MPulxfsFfr1UOFJXW5xzvKyg08wXmac3xfS3D7AluNQ2UZEzNapxr0WH4fPyOHqR4wlUNABvEbGsCUHHbFzwkPGeTuqbNyyWpdXdBYZCqJ151uOfdB_k2w1ycy1whYpCd5MfU0rezNsgNN2326Nf15lsYpGHIDiYaf6e3fLV1cIH154pZgRo5YUrmVLeSJF45MI0e0Uarnm3PW5PPUFx7Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
فدراسیون فوتبال پرتغال قصد داره برای فیفادی بعدی یک بازی ویژه خداحافظی با اسطوره کریس‌رونالدو مشابه اقدام آرژانتین برای لیونل‌مسی تدارک ببینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/107816" target="_blank">📅 18:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107815">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0576436f6.mp4?token=elqySRzAFlIiwobQXfd1anjqCrMreO_u_FGNsHJCeIzXuY2ONg-fOcVviOK07NYZIwW8ZqWbKvi24anWOvG9zNOa5NjuQFTJM1aUtnvBSutrBbC7Dy-_P1i3qdFxVaT60zebf8YPfHaVAJdoSgDKDGrfI6qFXGBqGjWPFq9stev-K5n_OMFaePkwFh7CPUAQBvSC-Sq92JTEp8fpEOc8SJ5UL-PikE68gEygEMmsjAzLGLbL4OWVW6heBA-KKHhppEsOu6rRckjbkYSMpRloExnS4_be51wqXOj15-P96F6K72TjOYTMteyXovnMvjyeglC2UskC_y0cNr1-XItFIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0576436f6.mp4?token=elqySRzAFlIiwobQXfd1anjqCrMreO_u_FGNsHJCeIzXuY2ONg-fOcVviOK07NYZIwW8ZqWbKvi24anWOvG9zNOa5NjuQFTJM1aUtnvBSutrBbC7Dy-_P1i3qdFxVaT60zebf8YPfHaVAJdoSgDKDGrfI6qFXGBqGjWPFq9stev-K5n_OMFaePkwFh7CPUAQBvSC-Sq92JTEp8fpEOc8SJ5UL-PikE68gEygEMmsjAzLGLbL4OWVW6heBA-KKHhppEsOu6rRckjbkYSMpRloExnS4_be51wqXOj15-P96F6K72TjOYTMteyXovnMvjyeglC2UskC_y0cNr1-XItFIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚽️
مهدی مهدوی‌کیا اسطوره فوتبال ایران در حمایت از مهدی قایدی گفت:
🔹
هر بازیکنی حق داره بگه بهترین مربی‌ای که باهاش کار کرده چه کسی بوده. اینکه به خاطر چنین مسئله‌ای یک بازیکن رو به تیم ملی دعوت نکنیم، واقعاً نمی‌دونم چی بگم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/107815" target="_blank">📅 17:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107814">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107814" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/107814" target="_blank">📅 17:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107813">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tv9hWShUZRN2mD74qiHSNA8xzTewOjjRDlJgK2NXtk111CmS46vItCPYlZRS063umOL7IJ_s7z0AJm12BH01CoNCOjKZGA6et3AYU6MopkQ1j8QcSKSTRSh8__XidM9KU1frIhwufvg0vsvxCVAdOCpHjtA0UrVZ2IRdQnRTAiHfQ0S_g40-9qHhh5WK0bBpdA8k_xd5cbv6hUYcjfX5GOw_OL1sQuQJZLdxF7cURutuXI2mjE-OCT3MPYO5anSDVPE_i1peyUw5ZyUUh2RJ28hUNNjFW6_Dmz0OkX2nY0u6dOQChEBoZDBUQ7UHMZcA51LWYG6bR-J-LPkTQiOGvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز نروژ
🆚
پرتغال را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
نروژ: ۲ برد، ۳ شکست و ۸ گل زده
پرتغال: ۴ برد، ۱ شکست و ۹ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/107813" target="_blank">📅 17:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107812">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_hMnZgumTRBQe5LXm14boVTu63HcWFxAxjnsDDNkgRJ0iGoqu_PFtEvbKb-4ObWwfgqgAksSdLQV2F4nSLjBUwEtq35xcRofOtz41KSn_NcgeyZ0otG5rPvO0EPbFySaYlBWtw6M6FdA07gV35HKbl2e-YcKaFfDsy365LIedXrrzJjXhYVQfIo49ui3SYUfzOAkA1T2G_5sgJAuuIXk8La_XWiJ_SvYGZFPJTvUu5VSMlSEJpYTl9cjQ3tKO_vLA_bPghOy37Nqwmo3ZDRH5aWE4p1vVvnwexXJnkWvP2dvdE1g6iha_Rg4ipjV6pU3D5gJhKNZSKEMEVhhBGj3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
⚽️
براساس گزارش منابع خبری، یحیی گل‌محمدی سرمربی فعلی دهوک عراق قرارداد خود را با این تیم فسخ کرده و در آستانه حضور روی نيمکت تیم‌ملی امید قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/107812" target="_blank">📅 17:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107811">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqIKijK_tYNv8MLewq68fS0PBN6yVnWvveUEZYUzgNbmdxTp2fIqUgfVZ4C8cU4WVRKTc-XKz1hCf74eUBc6nmQ3_1MaSd9HQqTdJYOrKlTEwV7X19wV8QSXq4oC3Oi3_hZf1JlIThAyIRJAdojT6LInQXOkfQF44sLgZKFmPcfWbNC_KFX39vLUdjzsv981ihIcxOQPysb66r_3iEKd9vvMEQbe7wfW7POS0T75ve7E82oscp2jCZaHxgGqYrHEn6j14ywOJb9fckft0wmwagU2wRVERUSt8e0n9c1b6gds5eCIQSJYFy4S0SItMhLxAv_W-_sb50u3Es0eQzvQEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
مارکا: اندریک از نیمکت‌نشینی‌های مداوم توسط مورینیو ناراحته و میخواد ژانویه مجددا به صورت قرضی از رئال‌مادرید جدا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/107811" target="_blank">📅 17:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107810">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‼️
⚽️
لحظات تلخ احسان حاج‌صفی در تیم ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/107810" target="_blank">📅 17:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107809">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0177fa0248.mp4?token=ByqitgXZEE_4iw4CIEtmTj7oj8YKZ5ykLagkI08BkPFDUb2jW8R37XEmIW1YyxIYGvn-l0z6C4lWHlmU5tLpjBo4JMQfS5bwekKrLfD6LkXm_OP4OzGr8gd2eq5iXT-kVt6ar5ribJFipRJlpqrm27tdyHuzkKmDTDN8BoMiYGoN949aq3Krhfbpzz5IMIKf0lf6Gvbiu2fxOzaP3jNRIWZZhSDG2cYD_OnRD_-TLf_w5dEvpgQuUdq4NsVsw9hTeECugrNc8ZskvKbbJn8LrUf55SIdmGnPqbAspR0iXfyRHXUI2WM0DKki6ebAfViXmexcCgkWLVTnEKyxZOgSBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0177fa0248.mp4?token=ByqitgXZEE_4iw4CIEtmTj7oj8YKZ5ykLagkI08BkPFDUb2jW8R37XEmIW1YyxIYGvn-l0z6C4lWHlmU5tLpjBo4JMQfS5bwekKrLfD6LkXm_OP4OzGr8gd2eq5iXT-kVt6ar5ribJFipRJlpqrm27tdyHuzkKmDTDN8BoMiYGoN949aq3Krhfbpzz5IMIKf0lf6Gvbiu2fxOzaP3jNRIWZZhSDG2cYD_OnRD_-TLf_w5dEvpgQuUdq4NsVsw9hTeECugrNc8ZskvKbbJn8LrUf55SIdmGnPqbAspR0iXfyRHXUI2WM0DKki6ebAfViXmexcCgkWLVTnEKyxZOgSBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
⚽️
علی‌فتح‌الله‌زاده مدیرعامل سابق استقلال: قلعه‌نویی نتیجه نمی‌گیره؛ من بودم عوضش می‌کردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/107809" target="_blank">📅 16:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107808">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e1845ed89.mp4?token=K0MpSFZcJJhtVIx5kYQSCwqI-MoKPV687JeTK6SHp7OXHYDKTGZukOBgPVbY0J6anGScwFDxwi7lj4_7h99zN7dXFBxDTjGHD1EjdyD6viX6HuV80SP6_lkGaR6Adx1AforbEbhRjh9owZYAsfNnyJw7haXbTLj-mgMw3h_Y465mGY3jXZBbBjk5SkSlas-TfZoL2amZmREHVXy5VUjfBTw84xja1QrAfIjNrX1MVXHmrb0gCa8r-vK_6qpKSRc1_olo6hLJfF98-DTYaYdiBmLntCBk4I5vMgCJMSQB9KyPokp2Nq0t84w5KMUzn_vu3oV0zsYxcg7mFho4C1rdSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e1845ed89.mp4?token=K0MpSFZcJJhtVIx5kYQSCwqI-MoKPV687JeTK6SHp7OXHYDKTGZukOBgPVbY0J6anGScwFDxwi7lj4_7h99zN7dXFBxDTjGHD1EjdyD6viX6HuV80SP6_lkGaR6Adx1AforbEbhRjh9owZYAsfNnyJw7haXbTLj-mgMw3h_Y465mGY3jXZBbBjk5SkSlas-TfZoL2amZmREHVXy5VUjfBTw84xja1QrAfIjNrX1MVXHmrb0gCa8r-vK_6qpKSRc1_olo6hLJfF98-DTYaYdiBmLntCBk4I5vMgCJMSQB9KyPokp2Nq0t84w5KMUzn_vu3oV0zsYxcg7mFho4C1rdSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
میثاقی: فیفا دی سوم چیشد؟ اگر قرار نبود بازی کنید حداقل لیگ را برگزار می کردید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/107808" target="_blank">📅 16:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107807">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63df69c40a.mp4?token=NOK16TJXzGfz4O4FPRyRib9tjOKWqfxRN_zV4x4wmn-r_DSmKp7raIF7xb4zd45bdAEX-qcrsjSqlm5nZLcH7PFCbLIq2v9xbdsGY8WqwaCJvTlOAI6abbriPFeur5zk6oYo65ayaHuLD7DnxeSJhOknNdslwFMr3nUPINkh_t6f0LdHrSeUmopbhVjj0O4ovQW8EbGIZT4ceuFJDEfO8Zo-NzQ10NwCmUecsdWW67G0hzt0mTwwyq5o0CU0NZwWhONMtSTCN25mfGsVMLUnNeLXyLPWpNI-ND4etf0YvhOiS8Ja5nHZU2M7pa7InwfIDBKR7HOoiadH260cVHektQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63df69c40a.mp4?token=NOK16TJXzGfz4O4FPRyRib9tjOKWqfxRN_zV4x4wmn-r_DSmKp7raIF7xb4zd45bdAEX-qcrsjSqlm5nZLcH7PFCbLIq2v9xbdsGY8WqwaCJvTlOAI6abbriPFeur5zk6oYo65ayaHuLD7DnxeSJhOknNdslwFMr3nUPINkh_t6f0LdHrSeUmopbhVjj0O4ovQW8EbGIZT4ceuFJDEfO8Zo-NzQ10NwCmUecsdWW67G0hzt0mTwwyq5o0CU0NZwWhONMtSTCN25mfGsVMLUnNeLXyLPWpNI-ND4etf0YvhOiS8Ja5nHZU2M7pa7InwfIDBKR7HOoiadH260cVHektQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
رسول‌مهربانی مجری دلقک و گزارشگر صداوسیما که با این الفاظ دیروز جنجالی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/107807" target="_blank">📅 16:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107806">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dc22c75d3.mp4?token=t1vzCNC4zOQU-m0OM5l6B7UFcfIidNzIUNJIe9BLIUMTIkVFGlV_9zSKOeTEcDuO1h3cVDsPAyvuvCVeqddWDpa9MMbRbgCu6QQjY8X-6gE9ijjpQSsWG7r0YY3TlUFZG5wqrDlhmLZc8E95bewxEJ-defVUyCeU4tZZ8Kr2smFmFOThNKH-INrm43s5jPq_1PBIcEAEZ5-n2wLXCDZ20hrpoE5duSTBQsnOBjW91XHvB4keDkc8_vhjwqr4apWLtZmM3bTN5NRvlBaEeekwGSW7iT6bsgT9KVC4fZcgmJUSK8HFj3OAquJfUX3SkES2Twx1NzsaNdPBmuruQb2rNzM7judrEfDzM9mqfuovjBc_jripEsFxdk5NKwpQhR-KsQx6IZT5TFDuzK81FDotE4JLqmR7vhPKpHbBBZYPmGWsGZT-0FYR81nGZ3invbEh_UUG-3lErmMRAkl664_vQnJCM2S7o0SAkDGNl3QzVWaFIVrrjS-Dig4V6k24MpPoBqnEkACFt2zw8HS7ftW_QMULeNgKkkZ-wk72oF4VPpEiZSct_BJB1yZlEhOaOF5Rp8jq5SClGTxf8e1K4e09b-DajP_FlfFZFM3IflE0dQzA2febRDZ9KuNoIQwpeVkw58OqcEKsnDU_O8eAjb-2_zKp7_bcXcoKdBxoAULWVGE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dc22c75d3.mp4?token=t1vzCNC4zOQU-m0OM5l6B7UFcfIidNzIUNJIe9BLIUMTIkVFGlV_9zSKOeTEcDuO1h3cVDsPAyvuvCVeqddWDpa9MMbRbgCu6QQjY8X-6gE9ijjpQSsWG7r0YY3TlUFZG5wqrDlhmLZc8E95bewxEJ-defVUyCeU4tZZ8Kr2smFmFOThNKH-INrm43s5jPq_1PBIcEAEZ5-n2wLXCDZ20hrpoE5duSTBQsnOBjW91XHvB4keDkc8_vhjwqr4apWLtZmM3bTN5NRvlBaEeekwGSW7iT6bsgT9KVC4fZcgmJUSK8HFj3OAquJfUX3SkES2Twx1NzsaNdPBmuruQb2rNzM7judrEfDzM9mqfuovjBc_jripEsFxdk5NKwpQhR-KsQx6IZT5TFDuzK81FDotE4JLqmR7vhPKpHbBBZYPmGWsGZT-0FYR81nGZ3invbEh_UUG-3lErmMRAkl664_vQnJCM2S7o0SAkDGNl3QzVWaFIVrrjS-Dig4V6k24MpPoBqnEkACFt2zw8HS7ftW_QMULeNgKkkZ-wk72oF4VPpEiZSct_BJB1yZlEhOaOF5Rp8jq5SClGTxf8e1K4e09b-DajP_FlfFZFM3IflE0dQzA2febRDZ9KuNoIQwpeVkw58OqcEKsnDU_O8eAjb-2_zKp7_bcXcoKdBxoAULWVGE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🙂
بازگشت سردار آزمون به تیم ملی بعد از مدت‌ها با کمک متن هوش‌مصنوعی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107806" target="_blank">📅 15:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107805">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ab5019276.mp4?token=rF8np1zaqvRnF6HSPcZEWVATiBbeWdmhjEGAiddrbpDyZIFabPTFQLJK4AqxocH4cn44NYT6cce5HpaH8zKcQAH91Rvs9beL3UhKxAOYMOie-rOaj4Y2_HThQjLPTUDzgIN8NwUjplUSlrSnCE-3XKJDGzwqdEHWJCvN29e2azAEKHydOoFqrO-vNy3LpFhFXQJyBDsl0kyVEwc2iwddajE-5uOiiIFwg7Ez_bp9yP2QQFKR07nq5vlEjhFiWrc_f1FdV45-CsnABQHR0KrtcENMYPYYzm2tEIlpUmO1dMKc_231l9HuaAtkXdRWrNGnwI-y-IyDe1EZFK3hv6IwWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ab5019276.mp4?token=rF8np1zaqvRnF6HSPcZEWVATiBbeWdmhjEGAiddrbpDyZIFabPTFQLJK4AqxocH4cn44NYT6cce5HpaH8zKcQAH91Rvs9beL3UhKxAOYMOie-rOaj4Y2_HThQjLPTUDzgIN8NwUjplUSlrSnCE-3XKJDGzwqdEHWJCvN29e2azAEKHydOoFqrO-vNy3LpFhFXQJyBDsl0kyVEwc2iwddajE-5uOiiIFwg7Ez_bp9yP2QQFKR07nq5vlEjhFiWrc_f1FdV45-CsnABQHR0KrtcENMYPYYzm2tEIlpUmO1dMKc_231l9HuaAtkXdRWrNGnwI-y-IyDe1EZFK3hv6IwWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
ویدیو وایرال شده از شادی رتبه ۲ و ۶ کنکور در حین اعلام نتایج کنکور سراسری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/107805" target="_blank">📅 15:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107804">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49b154fa09.mp4?token=cNTApEH363vNjDIqBoRE15fnTQpGdOn0k7JRlllohOo_PFCE-Z8CMU0VfNb9hKVskT5S6dhVeAhupNm2M4wEhgDJezrGb1OV76JnmCLZ0ZL0Gmpwr7ni7fQf8tvPzBKsAsRBlKgUqcmdtC2BoGkU6zlLUlOGRPIXmQEJ_6Di-8SypSrG5LQXK5ofzGnA1W6smaY7Dn9g-Vj6JJXae17TLrrajUZlaijwSJwkJbRr41AZrYMsInh2yruBfeTVC0lwVXZIsyhfvpiBHJGGq8ARG-rAfdUVK7txe20CTRb717Dco1znAlKHxVihJjbGHxohIH2qYuxP8FquVsA6ZzInDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49b154fa09.mp4?token=cNTApEH363vNjDIqBoRE15fnTQpGdOn0k7JRlllohOo_PFCE-Z8CMU0VfNb9hKVskT5S6dhVeAhupNm2M4wEhgDJezrGb1OV76JnmCLZ0ZL0Gmpwr7ni7fQf8tvPzBKsAsRBlKgUqcmdtC2BoGkU6zlLUlOGRPIXmQEJ_6Di-8SypSrG5LQXK5ofzGnA1W6smaY7Dn9g-Vj6JJXae17TLrrajUZlaijwSJwkJbRr41AZrYMsInh2yruBfeTVC0lwVXZIsyhfvpiBHJGGq8ARG-rAfdUVK7txe20CTRb717Dco1znAlKHxVihJjbGHxohIH2qYuxP8FquVsA6ZzInDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
👤
👤
مشاور قالیباف رئیس مجلس:‌ تا به عادل فردوسی‌پور تذکر دادم، مطلب حمایت از علی کریمی را حذف کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107804" target="_blank">📅 14:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107803">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCB6oAviaiNvy4iCQKnCfBjLQKNsGDGud_xF8TZ6Vjb15aPM4pC0LYk7yCHJIcsPTxnys2ey0Jvv_sgocc2LS2eudC8ogzcd3pmkiiY8MkOwtHET1fjiFvO2pSrYp0tdMZHXBIBGPp2fXRCJoDCc_sGp3a_N7AgtkKsRbuikz3Yas1_ceXXDXoGfKe-4mNV4fQsnj-VUKuxlyVTLpUatYAomU-rGS8gbBbjaThRoGfSpuikbcwDQ8AuGyhlB_hTVr5FGJeNIS-od30wIF4muos0b4Ko2fnUWAr5KIimvQrLa1B6KfguJYy097yDBLe8oPQeDjGtHejlFbhlANdByUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇹🇷
وضعیت وخیم ترکیه در لیگ‌ملت‌های اروپا؛ بازی بعدیشون جلو ایتالیا هست که آردا گولر بدلیل دریافت اخطار محرومه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107803" target="_blank">📅 14:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107802">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e464e1d963.mp4?token=t9nFgc7_q1XrrGrbJOrseKZZMkqi22Ave4S5MYGVGNC2MXwQDpOZXReqUAS6_vgjiyebKqaRk89U619fOmX4H6yUcZUXExf_MWrOh5JV4kZaFqIq06VhSk-h9X4W9JvzyFnlx24g8jOMATgMuPNLKN4rALj3eSYzi2taG8OR3ZZi6k35dKrRr9d3L1yiJWr7b-MBxRZiWJrqhSEO7DAa6qA8c895syYiBTQbtfe8ovUZLKpPv0qZu3acQ8c8Xom52ihVlevDU3tgesIoNsRJ-1e9XoTsr7_wtjTXp_Nmhf8U1qVrLYIJdV5qsxG6Gjdl2-2ALF3OaYVUPEzYbvmlImmmKHxYtPp1u7jlsOt7Yt81aLTvJj5IcPkCvj0Au8EQKhK8PlvMsITBaxw9Cmd6RSrzfXnmrUD5iAg_c_A2OgaHAFp5dI_icOeiIsUgJOyD3CAHAZSAYuPX88LtNYD3H_Uw7z4_Mhe3HmutyRI6oCOXjYlbzS-ouMpt5_Rg3pivPriw7ymoIWrUH1fXYifwjVavI2o4qjTQxg59nUhKBP_-OTN6uPG8GA7eye6dES58hTrN5bB6R1YnkTbTMSxRpO_7wBP4WV0t1LgBZOMB2P5qLZ13igyhiC7MRzZJsCYC3OM5lERjdQ998vPUcwd3knt2-V9DDb6huNBdHqlIW00" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e464e1d963.mp4?token=t9nFgc7_q1XrrGrbJOrseKZZMkqi22Ave4S5MYGVGNC2MXwQDpOZXReqUAS6_vgjiyebKqaRk89U619fOmX4H6yUcZUXExf_MWrOh5JV4kZaFqIq06VhSk-h9X4W9JvzyFnlx24g8jOMATgMuPNLKN4rALj3eSYzi2taG8OR3ZZi6k35dKrRr9d3L1yiJWr7b-MBxRZiWJrqhSEO7DAa6qA8c895syYiBTQbtfe8ovUZLKpPv0qZu3acQ8c8Xom52ihVlevDU3tgesIoNsRJ-1e9XoTsr7_wtjTXp_Nmhf8U1qVrLYIJdV5qsxG6Gjdl2-2ALF3OaYVUPEzYbvmlImmmKHxYtPp1u7jlsOt7Yt81aLTvJj5IcPkCvj0Au8EQKhK8PlvMsITBaxw9Cmd6RSrzfXnmrUD5iAg_c_A2OgaHAFp5dI_icOeiIsUgJOyD3CAHAZSAYuPX88LtNYD3H_Uw7z4_Mhe3HmutyRI6oCOXjYlbzS-ouMpt5_Rg3pivPriw7ymoIWrUH1fXYifwjVavI2o4qjTQxg59nUhKBP_-OTN6uPG8GA7eye6dES58hTrN5bB6R1YnkTbTMSxRpO_7wBP4WV0t1LgBZOMB2P5qLZ13igyhiC7MRzZJsCYC3OM5lERjdQ998vPUcwd3knt2-V9DDb6huNBdHqlIW00" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حضور بیژن مرتضوی و همسرش در دربند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107802" target="_blank">📅 14:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107801">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82e592cb76.mp4?token=amGzMs3tnbShRlp_2-3JQ6lf-wUbUxAqBCuzfQ-aZ6nLjR73DjaXMyBikJKLjzQR1GczyWKP-_Cj3ktY25YHgdxzFdEiJZLz8vCTnKS0PAEtkaaI0b73X1dqB8R698M4Iagqz7QgIcDEelAneW3lYsvAn9qf0Z5m61cEXrZScnjiRw8v7nTLUbCp1Ert_9w9kN2smACSLtoLFdp-ITEvGdchOXq25c73MrLytqkcAC_q4LGXiFln4t5sfs-PHjwCBHVm_BTWKokZUSpSMd3p2OSX3Tfp8L50nvMYN0_hBKAVogWk344cRN7LwpaIInV9nK7lNCB34m1InVLplo6Txg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82e592cb76.mp4?token=amGzMs3tnbShRlp_2-3JQ6lf-wUbUxAqBCuzfQ-aZ6nLjR73DjaXMyBikJKLjzQR1GczyWKP-_Cj3ktY25YHgdxzFdEiJZLz8vCTnKS0PAEtkaaI0b73X1dqB8R698M4Iagqz7QgIcDEelAneW3lYsvAn9qf0Z5m61cEXrZScnjiRw8v7nTLUbCp1Ert_9w9kN2smACSLtoLFdp-ITEvGdchOXq25c73MrLytqkcAC_q4LGXiFln4t5sfs-PHjwCBHVm_BTWKokZUSpSMd3p2OSX3Tfp8L50nvMYN0_hBKAVogWk344cRN7LwpaIInV9nK7lNCB34m1InVLplo6Txg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇮🇹
یک‌دقیقه با درخشش دوناروما مقابل فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107801" target="_blank">📅 14:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107800">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5581b57d8f.mp4?token=vjGklso303yKsBVZ4lafsOTAnVVCDeNZaPO5CQAMbkMTYpJhJmZm9L1A5saOGUjkFzwruAH5ZBzpFt-sIwf3FOFp-epJOdOgmljPC2sfB_6Je8AhFlQPf1m_b3PzcZI1np0fa13ECtSniuRmM1SwSVZDPGRivsN_KtCoCZC7Bbb4RBeq2hwHESKA1CWowLoe_s0A7_ERPj9OBIDT9ym_wpL4GKZ7irIZmm66OUOlKiPFRiailR_UqJFX1cpv1EVAshZjDYtdwB11BpcOjR4-oHsKS414uYJXuwsmXLoYqJn-4_s2F06BdxUJ4AqcdFLAbQG0orl1pCmRKm_71DWyrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5581b57d8f.mp4?token=vjGklso303yKsBVZ4lafsOTAnVVCDeNZaPO5CQAMbkMTYpJhJmZm9L1A5saOGUjkFzwruAH5ZBzpFt-sIwf3FOFp-epJOdOgmljPC2sfB_6Je8AhFlQPf1m_b3PzcZI1np0fa13ECtSniuRmM1SwSVZDPGRivsN_KtCoCZC7Bbb4RBeq2hwHESKA1CWowLoe_s0A7_ERPj9OBIDT9ym_wpL4GKZ7irIZmm66OUOlKiPFRiailR_UqJFX1cpv1EVAshZjDYtdwB11BpcOjR4-oHsKS414uYJXuwsmXLoYqJn-4_s2F06BdxUJ4AqcdFLAbQG0orl1pCmRKm_71DWyrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
دزدی مسئولین از بانک‌ها سوژه جالب و وایرال شده مهران مدیری در مرد سه‌هزارچهره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107800" target="_blank">📅 13:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107799">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
‼️
⚠️
درگیری‌شدید و خونین در مسابقه‌ای از لیگ زیر ۱۸ سال کشور که در مشهد برگزار شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107799" target="_blank">📅 13:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107798">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46755fa2d0.mp4?token=rlaSSByo6y5HPfwtVc7TUWNkG58Pa_lXyyEXhCNrhLznH85Z1rUlsfj-0hMWBbiksc-ymLGcpel1tmuHY4vQSAtpEK4TGvoueR7HuJ7o9fqIfqNKN3JmJJHtusCIYD6itJSNMrykgg5k5g7DP0ZgF9J6NvTIhx6FdRXgnrOuD6roQ_cYUAyNmEjh96LJw92NiT4xfvqQIZEFzgUYK1MJrZwZyOMNN7S-7HI4VY1q3W-IAvshYWr7XHP8B2dlTlAmu1qyws71I4KVEGta1hlYMv62sgylgbItkEKn2lcMuzAmiDa4M9zv7-9-VgXZqv9p5cCw1NEDaB23PisZbPqBcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46755fa2d0.mp4?token=rlaSSByo6y5HPfwtVc7TUWNkG58Pa_lXyyEXhCNrhLznH85Z1rUlsfj-0hMWBbiksc-ymLGcpel1tmuHY4vQSAtpEK4TGvoueR7HuJ7o9fqIfqNKN3JmJJHtusCIYD6itJSNMrykgg5k5g7DP0ZgF9J6NvTIhx6FdRXgnrOuD6roQ_cYUAyNmEjh96LJw92NiT4xfvqQIZEFzgUYK1MJrZwZyOMNN7S-7HI4VY1q3W-IAvshYWr7XHP8B2dlTlAmu1qyws71I4KVEGta1hlYMv62sgylgbItkEKn2lcMuzAmiDa4M9zv7-9-VgXZqv9p5cCw1NEDaB23PisZbPqBcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🐐
از توماس مولر پرسیدن: «مسی یا رونالدو؛ بهترین فوتبالیست تاریخ کیه؟»
جوابش؟
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107798" target="_blank">📅 12:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107797">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad1675b1b.mp4?token=e1JzHZQTHg8-rL-00Sk1fQ3zlNkSSAmxg5d8XrQblHSq5PYG-kjl9WJGI9S_w_shL1YBGTbINUKfAxv12jRE9GSaGUrlsUxqJOMmbuKNQswe2tAvasZ8YYgi4zynWWHXDx0UtukcMB9t7IlRasdqTdB4iv4G_1o7ouu2pdx-YwjD3nIacaGU4UJc7nov8ATfoimIJlAPyq9eEYZcI3r2OiKEEkn-74g6cjrtqPAZJuPwrdfTYuedHq-kIIuSHxjssVeqPltGSoakIFa0v9RZ9cjUEdO2oUAXaOWXwcIfbP6-A_FlUK6OMZGUThWv-Jlg5mUQfai-TpozN3fABfhfrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad1675b1b.mp4?token=e1JzHZQTHg8-rL-00Sk1fQ3zlNkSSAmxg5d8XrQblHSq5PYG-kjl9WJGI9S_w_shL1YBGTbINUKfAxv12jRE9GSaGUrlsUxqJOMmbuKNQswe2tAvasZ8YYgi4zynWWHXDx0UtukcMB9t7IlRasdqTdB4iv4G_1o7ouu2pdx-YwjD3nIacaGU4UJc7nov8ATfoimIJlAPyq9eEYZcI3r2OiKEEkn-74g6cjrtqPAZJuPwrdfTYuedHq-kIIuSHxjssVeqPltGSoakIFa0v9RZ9cjUEdO2oUAXaOWXwcIfbP6-A_FlUK6OMZGUThWv-Jlg5mUQfai-TpozN3fABfhfrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇹
عدم‌پاسخگویی سرمربی پرتغال درباره رونالدو در نشست‌خبری پیش از بازی با نروژ!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107797" target="_blank">📅 12:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107796">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a683578dd.mp4?token=EnrwbBnEJqphOPeywbSTqXlW_kn15AAftuk14Z2_3Wtycqf0FWq-x1lyOoSZIAHA3ZV4eyaPf1cGvhSsbWggB02h7TtYlplpff1_JNHPrLG_GdyFey8O3jQaMH23ZNDMjPCey0ii0RmCDELiov9Las2RfKlOPfP936f-pqCKmTYeKHtqIX1CxFObyZLa3LcdJuL2MzZBfcZqdhqJ1U346tHbPtwplF6LDl2WRxapHrjKI-M0u_uedCLgSn1HdCNZ-bfb5cMTPHbQm6PLaE5x6iO_VYHArAkx87p8jYVQguiJfN7E341PynkGhc3Y8j4O4r-TLLeuZTydTj-pToZlBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a683578dd.mp4?token=EnrwbBnEJqphOPeywbSTqXlW_kn15AAftuk14Z2_3Wtycqf0FWq-x1lyOoSZIAHA3ZV4eyaPf1cGvhSsbWggB02h7TtYlplpff1_JNHPrLG_GdyFey8O3jQaMH23ZNDMjPCey0ii0RmCDELiov9Las2RfKlOPfP936f-pqCKmTYeKHtqIX1CxFObyZLa3LcdJuL2MzZBfcZqdhqJ1U346tHbPtwplF6LDl2WRxapHrjKI-M0u_uedCLgSn1HdCNZ-bfb5cMTPHbQm6PLaE5x6iO_VYHArAkx87p8jYVQguiJfN7E341PynkGhc3Y8j4O4r-TLLeuZTydTj-pToZlBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
دهقانی، مسوول مسابقات بین‌المللی فدراسیون فوتبال: باید ورزشگاه آزادی را همانند نیوکمپ بارسلون مسقف کنیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107796" target="_blank">📅 12:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107795">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfa3096b41.mp4?token=mHo7HOMBUOGbl1F5-MEeZsyO95atSYFC_IjhhWCRtjWVrJ7g4RYo63O3keV-3-4rcGaq2vR20A8PM1UZI0ccEtgcoPseO3BPfDl1c8HYiF7gYIrNbc_hydWj8JREz8vCRSU92cVVLlvMaqlhV2iwwm-ulN38LBGBg-359-ZGsjpbqyrUeq9Lg7tbir63ugI92DEIukKoH4vxAICQAkNIlcDY6R7OJX7cABIs7TsOKwrQ-utsVii_HtUwxJ-EzC7xViVNxRkYLVXLLt8znHN3kWoZZEZiNl3kMgpYablhhJmE80Dbf_ZPFxbS3QdO7liQN_mL9VdAfLU5wDN8k-OgXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfa3096b41.mp4?token=mHo7HOMBUOGbl1F5-MEeZsyO95atSYFC_IjhhWCRtjWVrJ7g4RYo63O3keV-3-4rcGaq2vR20A8PM1UZI0ccEtgcoPseO3BPfDl1c8HYiF7gYIrNbc_hydWj8JREz8vCRSU92cVVLlvMaqlhV2iwwm-ulN38LBGBg-359-ZGsjpbqyrUeq9Lg7tbir63ugI92DEIukKoH4vxAICQAkNIlcDY6R7OJX7cABIs7TsOKwrQ-utsVii_HtUwxJ-EzC7xViVNxRkYLVXLLt8znHN3kWoZZEZiNl3kMgpYablhhJmE80Dbf_ZPFxbS3QdO7liQN_mL9VdAfLU5wDN8k-OgXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🎙
ترس عجیب پیمان یوسفی مجری تلویزیون هنگام نام بردن از روحانی؛ یه وقت نیاید بالاسرمون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107795" target="_blank">📅 11:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107794">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6ce37f880.mp4?token=buouViEIHtrG_utmSbjzfJ9IkNddifVC2MxocLIHHkCzcsXcc0DP8hHt_MxvZwbGafBpimMvIY-VCAh1MfQjEyGUnPFGFpUvrTW0DG4Ujai6kgM3-K8hLL1C05yYrJT0HHe2MBShBBBE82KqWta_P10a6VcUs1H0b2T91X_PAjMfYcCWu0qJFsfZWlCrh28Vt44WYrOLVtLZi98IcMjcAv3yvh2v_wWxHtb4DCxqoGEuRQe6nbCGa1zaNy6-jyFTYC6q9EwbruTJ2UIj7X9TVLZS2saYTktG6AXwMm8jd5MogVgyMXHciKPBrFGbLCMBXk5MQlzGODPVm7FW11oYnaPe6m083L-7TS_OCoZ6_BOr2JSva3cuWVFWC5GgGoGtt6RrUedqv976gLSArfDVFRLfZQVYLQVOzl_XDME4-y977X139poAfhfAy4GJqXWh2tpY2dykqktDytTDrGdJuMjS8TV-BJCxuo5mC9jVChQfbrXdbTXYHauRQeLOyiv7owyaVuOgwz36dOtc-E0lZWK4jK-HPyVOt0OxwU_4uPeZC-yNf78Z14XMR3JpLZUEmeq9ChbmhHFiJBbM30T7uqBkWbAsuY4cSqLLFpF7iN0EWKuI0-CFT_47UOLIK4daaEZDCR5WSKAbSUzpYYyzE2Wt7emuBFBO9uzGjuecg_E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6ce37f880.mp4?token=buouViEIHtrG_utmSbjzfJ9IkNddifVC2MxocLIHHkCzcsXcc0DP8hHt_MxvZwbGafBpimMvIY-VCAh1MfQjEyGUnPFGFpUvrTW0DG4Ujai6kgM3-K8hLL1C05yYrJT0HHe2MBShBBBE82KqWta_P10a6VcUs1H0b2T91X_PAjMfYcCWu0qJFsfZWlCrh28Vt44WYrOLVtLZi98IcMjcAv3yvh2v_wWxHtb4DCxqoGEuRQe6nbCGa1zaNy6-jyFTYC6q9EwbruTJ2UIj7X9TVLZS2saYTktG6AXwMm8jd5MogVgyMXHciKPBrFGbLCMBXk5MQlzGODPVm7FW11oYnaPe6m083L-7TS_OCoZ6_BOr2JSva3cuWVFWC5GgGoGtt6RrUedqv976gLSArfDVFRLfZQVYLQVOzl_XDME4-y977X139poAfhfAy4GJqXWh2tpY2dykqktDytTDrGdJuMjS8TV-BJCxuo5mC9jVChQfbrXdbTXYHauRQeLOyiv7owyaVuOgwz36dOtc-E0lZWK4jK-HPyVOt0OxwU_4uPeZC-yNf78Z14XMR3JpLZUEmeq9ChbmhHFiJBbM30T7uqBkWbAsuY4cSqLLFpF7iN0EWKuI0-CFT_47UOLIK4daaEZDCR5WSKAbSUzpYYyzE2Wt7emuBFBO9uzGjuecg_E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
🎙
🇮🇷
بغض محمد عمری ستاره پرسپولیس ترکید: از روستا به تهران آمدم؛ شب‌ها با یک بربری می‌خوابیدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107794" target="_blank">📅 11:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107793">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9581683260.mp4?token=EcprwDP18nMRfdiU6FvE9CtdWe0mqQLMIHvPgCKjNfWxma64FsmKqG1JOIGq2Ts4aIC6Xc5qSYaLgY76uo6T44pzrJSu7DR5i--ssjoJ3HMsMvCrIGB1waDkAOga1lbu0IZzvtgN-VauIPtMQs94A4tD1-hb4kfk2hAA36eu2NVjt7iOU3JZ5PxwAm8FZmzKfk5q808TJYJg_5AnKR3VhpSGeO50Xp2ToXyVKI6kVJw-cAglI1tYJsM-OK94srwRD1i1CHqAHs0FNy9uiyY4w7dZ4scgR9hTiF3cMRZ28_2RbDIsGnfXPSTSW1UfIGIU2RSJdLjziAY0e5OX0_AkQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9581683260.mp4?token=EcprwDP18nMRfdiU6FvE9CtdWe0mqQLMIHvPgCKjNfWxma64FsmKqG1JOIGq2Ts4aIC6Xc5qSYaLgY76uo6T44pzrJSu7DR5i--ssjoJ3HMsMvCrIGB1waDkAOga1lbu0IZzvtgN-VauIPtMQs94A4tD1-hb4kfk2hAA36eu2NVjt7iOU3JZ5PxwAm8FZmzKfk5q808TJYJg_5AnKR3VhpSGeO50Xp2ToXyVKI6kVJw-cAglI1tYJsM-OK94srwRD1i1CHqAHs0FNy9uiyY4w7dZ4scgR9hTiF3cMRZ28_2RbDIsGnfXPSTSW1UfIGIU2RSJdLjziAY0e5OX0_AkQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایش های عجیب وینی مقابل هند هم ادامه داشت!
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107793" target="_blank">📅 11:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107792">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107792" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107792" target="_blank">📅 11:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107791">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxmHNmdf5t6-1D_I5WNzbUgLxkAe3KVCHga_RZGjDQfORG4Kr8l1B_Nk455y4IBec1V9yCc_H4vpbgDa5Fr0fwburm7Q8UDbrwqrW1t_tFXjCGzIXJgMNVWr9bA1Xej1taEOm8KK_rRpcMgRzosK971aH1enQv1vHE7pNHWZABnZDlkT6FtZW8-I_Z44Vkw4KMecmAC3Qa9WpINnsfSwMgtAI59nqmC0j9LCDupoFl-37SltRfzGqbZoNlXyZAv6rci77zPaz_Q1Edw6RAht8GrTSs7E-ClxB7mUa_6oHe7F107NaO9UqYZom-V0H-gNah5hEIBC3BusozepZjgYvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
آلمان
🆚
یونان
صربستان
🆚
هلند
نروژ
🆚
پرتغال
دانمارک
🆚
ولز
آفریقای جنوبی
🆚
مصر
مالی
🆚
مراکش
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107791" target="_blank">📅 11:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107790">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6634bc99dd.mp4?token=Opsyhj9ofXa0I-B7vVOIcz3hbO3IGtJcIGzBaKBcsPBw2KZRdEzbgr2F5Vx33p3L2Awyikgi6BjLNFaR-JEJy1SRTUNzXLe2c2DxLMALUmP2F9Y3YLypPNRoTy_BJGy3890Y-ZlOyxG3NC5BuPBCxgsxviCf16Qk7OrKVwFtxjxDJX5msMQ1l3aBcw9FzocQiwMfdemHDjdTKt527XlV3TMrV7Y4XCQ4bR0gCQbB__hhBg1Krb-DlzYtIdyJ0H1ZCH2_613p_jd8SNEe0dtIE3505_wte5tJyWbz8W53I5PcEW8hHfts40UPf7pvNCti10i3hb9-0E38d-tbvhSyXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6634bc99dd.mp4?token=Opsyhj9ofXa0I-B7vVOIcz3hbO3IGtJcIGzBaKBcsPBw2KZRdEzbgr2F5Vx33p3L2Awyikgi6BjLNFaR-JEJy1SRTUNzXLe2c2DxLMALUmP2F9Y3YLypPNRoTy_BJGy3890Y-ZlOyxG3NC5BuPBCxgsxviCf16Qk7OrKVwFtxjxDJX5msMQ1l3aBcw9FzocQiwMfdemHDjdTKt527XlV3TMrV7Y4XCQ4bR0gCQbB__hhBg1Krb-DlzYtIdyJ0H1ZCH2_613p_jd8SNEe0dtIE3505_wte5tJyWbz8W53I5PcEW8hHfts40UPf7pvNCti10i3hb9-0E38d-tbvhSyXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکت‌جالب لامین‌یامال بعد از بازی دیشب
❤️
👌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/107790" target="_blank">📅 11:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107789">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/321c017aa1.mp4?token=fbrd5ZpTFfgeCnfxY98B0UdeXEOwU8Zu9T0RzlXD_EIlQ0U94DU4zs5Ri9kuoy1eq7ARDTHvuF7NPUBeV0p_BTKA7raQ9RUlCBzEcpxtKzuBtcgKV2cPTdsDb5bcb1ltjQsu-RL9C8NWqXWhTE62isuuFGP9f87unrMGpxCRFoz6euLogoQbyjime3U9tgAxCU_VFmAy2UTOWV_7v6rUFUQCrSZygvr49DW_PuyIp5F4PZ87zK7kvSQe5YWhqX-PXqILoYwLPq6w_RNAmBOc-vdz2P1wkHD71aG1-8bZnpOgAo9cjXgxMGV2I7KDVWRSpb18h74BmuRTYdvpiyvcpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/321c017aa1.mp4?token=fbrd5ZpTFfgeCnfxY98B0UdeXEOwU8Zu9T0RzlXD_EIlQ0U94DU4zs5Ri9kuoy1eq7ARDTHvuF7NPUBeV0p_BTKA7raQ9RUlCBzEcpxtKzuBtcgKV2cPTdsDb5bcb1ltjQsu-RL9C8NWqXWhTE62isuuFGP9f87unrMGpxCRFoz6euLogoQbyjime3U9tgAxCU_VFmAy2UTOWV_7v6rUFUQCrSZygvr49DW_PuyIp5F4PZ87zK7kvSQe5YWhqX-PXqILoYwLPq6w_RNAmBOc-vdz2P1wkHD71aG1-8bZnpOgAo9cjXgxMGV2I7KDVWRSpb18h74BmuRTYdvpiyvcpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
▶️
کنایه مهران مدیری به ماجرای نماینده مجلس و مامور راهور در مرد سه‌هزارچهره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/107789" target="_blank">📅 10:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107788">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c7979edd7.mp4?token=Rf-bwb7-hF5WHWHSghqLc2Bm_sNB1H7CkNVmTr49NUQ5VLQI-W1rO1m2KazM5sfGqiPdnRN5sJ5xVOpf_2wpLDS4jOIRceJezdZdzqGP0qztr3P3ushnGAQ75bPEkQToxHQnPfZk4tdstoVDeL5aYIJjgPt1BhB2kwoCSIJzEE163ZuxVict-QNucixCffZ_KqND0CLIGjXY7RQAQFQK51KGIoJU1mik-bSy_ctxdeiAAoTTOJlgWAab5Soa4y2YV0HxFas4OM8J0rRuKGwD8F7SsF2xXYhicUuVF_P9nqLtvmx-OTATh4noUkaCTrkZ7fXLXClgcUugnCSTPWzNtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c7979edd7.mp4?token=Rf-bwb7-hF5WHWHSghqLc2Bm_sNB1H7CkNVmTr49NUQ5VLQI-W1rO1m2KazM5sfGqiPdnRN5sJ5xVOpf_2wpLDS4jOIRceJezdZdzqGP0qztr3P3ushnGAQ75bPEkQToxHQnPfZk4tdstoVDeL5aYIJjgPt1BhB2kwoCSIJzEE163ZuxVict-QNucixCffZ_KqND0CLIGjXY7RQAQFQK51KGIoJU1mik-bSy_ctxdeiAAoTTOJlgWAab5Soa4y2YV0HxFas4OM8J0rRuKGwD8F7SsF2xXYhicUuVF_P9nqLtvmx-OTATh4noUkaCTrkZ7fXLXClgcUugnCSTPWzNtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
🇮🇹
درخششِ دوناروما اجازه ی گرفتن انتقام رو به زیدان در بازی با ایتالیا نداد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107788" target="_blank">📅 10:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107787">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95502ba1a6.mp4?token=LdbpwsIgvsLN7ybuFjHwq-yrbIKvy9oksNROoIpFuXjoixvvoFT8EFZfx_gRzdBK9Z6__SwEE4QYGtT0vf3gr-_Nh_xFuOESMvsY2ujw9nXAI3-1CSej-f5VI9sTU75x1ZsGT7rnaUfrdBpqZuxQao5yfmzDOmrODMNDEuJGJWwHvXdo8ffBh63HiHVqepFbQIVpEhJQjP37Mv7D9nM7hX0Jl3Imh1ux1AQZ7q2qrqOA-BbEhs2xI50FmXOExGmZ6IVWMhL1j6rKo9foz8cWgTp2bd90SiWAhal1vH44IQX7urztDKwvQOKuzRAzPv7fT7JuRnRHE97JBgeoyISAkLXYG8qcihr1Q7kV2iAzv6c26uClVymuZjzoOUdKRW0FuzfjHVVco7yijo4o1AtnPvrEA2rwbR_Q5O2nOklVa2H62krPfICaP9DVVxDCD9jICvYpMQ1W6eUQOEIvUDaoHmgWWfrjrJbGi3PtCFM2A7MmlTIdwtWsRFFaz57tdtdkHcUdYSqJ486SDrxt94tFwa4Fdn5XqgDNRViv0kUM5ak4dNI8wLtn1HgmjDcQwCMSKdnJgRVjbLfPNCNL2vDGWv4c0ZZuGExhHs9tp--hANTM8txREtpaoQYBD5LUdfUuiTfI4snDAIG4HoxzcNqf0a1tYoAoLEqlCmPZ8GlqipA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95502ba1a6.mp4?token=LdbpwsIgvsLN7ybuFjHwq-yrbIKvy9oksNROoIpFuXjoixvvoFT8EFZfx_gRzdBK9Z6__SwEE4QYGtT0vf3gr-_Nh_xFuOESMvsY2ujw9nXAI3-1CSej-f5VI9sTU75x1ZsGT7rnaUfrdBpqZuxQao5yfmzDOmrODMNDEuJGJWwHvXdo8ffBh63HiHVqepFbQIVpEhJQjP37Mv7D9nM7hX0Jl3Imh1ux1AQZ7q2qrqOA-BbEhs2xI50FmXOExGmZ6IVWMhL1j6rKo9foz8cWgTp2bd90SiWAhal1vH44IQX7urztDKwvQOKuzRAzPv7fT7JuRnRHE97JBgeoyISAkLXYG8qcihr1Q7kV2iAzv6c26uClVymuZjzoOUdKRW0FuzfjHVVco7yijo4o1AtnPvrEA2rwbR_Q5O2nOklVa2H62krPfICaP9DVVxDCD9jICvYpMQ1W6eUQOEIvUDaoHmgWWfrjrJbGi3PtCFM2A7MmlTIdwtWsRFFaz57tdtdkHcUdYSqJ486SDrxt94tFwa4Fdn5XqgDNRViv0kUM5ak4dNI8wLtn1HgmjDcQwCMSKdnJgRVjbLfPNCNL2vDGWv4c0ZZuGExhHs9tp--hANTM8txREtpaoQYBD5LUdfUuiTfI4snDAIG4HoxzcNqf0a1tYoAoLEqlCmPZ8GlqipA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
نمای‌کامل از صحنه‌جنجالی بازی لیگ‌برتر بانوان میان استقلال و گل‌گهر سیرجان؛ فقط جیغ و داد داور و بازیکنان رو ببينيد
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107787" target="_blank">📅 09:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107786">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/363181b8d9.mp4?token=bFTGGkIt8bEAwPxv6HdBn1VPGOaH6FjzOf_BuXChToavy_eJw2qAz1a5hct1kut0sHW5gbC0hjWTtCauTY5cU0Sgw2m_bXXhrC3R5rOXANmFufT8dK_hhCRG5-Ij5ylLbesJJhUI7cHmkhMndPyXRcARLArCcHUg2UksW_O5IeRub4Al0z2i1VizpCz25UK8W40kBirevYrt53ZX8AqXWEsEOfQA0u4YAdu980csWZ-z2c7bn73XW1XGKuChSMZWeP7bLQjBVFH0MdkwBlWZXbZ37Wt0DtQa8BXy0OG9AuPwduVWMI3FrRIP6EOUlWj_9A8bSGPg12Iyla1H0DrUFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/363181b8d9.mp4?token=bFTGGkIt8bEAwPxv6HdBn1VPGOaH6FjzOf_BuXChToavy_eJw2qAz1a5hct1kut0sHW5gbC0hjWTtCauTY5cU0Sgw2m_bXXhrC3R5rOXANmFufT8dK_hhCRG5-Ij5ylLbesJJhUI7cHmkhMndPyXRcARLArCcHUg2UksW_O5IeRub4Al0z2i1VizpCz25UK8W40kBirevYrt53ZX8AqXWEsEOfQA0u4YAdu980csWZ-z2c7bn73XW1XGKuChSMZWeP7bLQjBVFH0MdkwBlWZXbZ37Wt0DtQa8BXy0OG9AuPwduVWMI3FrRIP6EOUlWj_9A8bSGPg12Iyla1H0DrUFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
▶️
‼️
علی فتح‌الله‌زاده:
🔺
فدراسیون با یه قانون من درآوردی سه جانبه برگزار کرد، میتونست با همون منطق بین ۴ تیم اول بازی بزاره قهرمان مشخص کنه.. به استقلال ظلم شد چون به احتمال ۹۰ درصد تو حذفی قهرمان بود و اون جام رو هم از دست داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107786" target="_blank">📅 09:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107785">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/708801c3df.mp4?token=oVzSFrYQkg0AdcdrdDPRuVb21zkbTSBNQ_JdWuE4_qmt0e-gsZrnLPrR48FumELrs7hbUuxDbXnmf2PA54l-SmPC5YxhlH7w7FcsRkQOkpDw8NxHznI_0rJQlvJReZ__m8ysDwG1hJRAPrw-elyui5Nj4ZegIhAfnvirZJDps69ZDvqYnpD81IZ6LlXBg8Jo3uZpOcvZoXGv-ZiulrjsE1EuyUv8Zkh4IRvFx9k-lLJ6OWNvYtVHXFQ7Y-fs4g-_IDRbgUv1MDjFKB7eDc_pDb8V28rEvsHVLY-wYKe4_ArkHa-cIULjuo7fLZg84ysiSkUCLN0LbVg0scOxD-KObA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/708801c3df.mp4?token=oVzSFrYQkg0AdcdrdDPRuVb21zkbTSBNQ_JdWuE4_qmt0e-gsZrnLPrR48FumELrs7hbUuxDbXnmf2PA54l-SmPC5YxhlH7w7FcsRkQOkpDw8NxHznI_0rJQlvJReZ__m8ysDwG1hJRAPrw-elyui5Nj4ZegIhAfnvirZJDps69ZDvqYnpD81IZ6LlXBg8Jo3uZpOcvZoXGv-ZiulrjsE1EuyUv8Zkh4IRvFx9k-lLJ6OWNvYtVHXFQ7Y-fs4g-_IDRbgUv1MDjFKB7eDc_pDb8V28rEvsHVLY-wYKe4_ArkHa-cIULjuo7fLZg84ysiSkUCLN0LbVg0scOxD-KObA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🥈
ایشون کیمیا زارعی ورزشکار رشته روئینگ هستن که تو مسابقان ناگویا یه مدال طلا و یه نقره به دست آوردن
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107785" target="_blank">📅 09:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107784">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a540d193c.mp4?token=V9ZYdYg_m3D_V-NjaR5NJTPG9FmKmcbc2_yzoZIrRmOPNofKJh-lc8iiRizuqEa39EeBPX0LWJkvG1B9cV8Exf-_5Wr1LGoL6eDe9bVBKs6o2UH05Rwdps2G8YChM88B4jpjUFnFS7dPji8Xyoj_7Retm5XU-siMcmayWbjdxoqf9_jAHGXWZnr_05Hy3aTBjjeCGrJUWAaEYuOrnquFCbcDJDd9HovTWFfTDe9UfgFUdLxxj2O-lJ5cTExiQnjRuKLDgyeu7t0MTzl1oCb3_rkhJ_JywPaYO0lD4nvaStXNfR8xNB5mlSOuGQSei4kMDaJ9Y2_K6AmPl-jTxpm8XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a540d193c.mp4?token=V9ZYdYg_m3D_V-NjaR5NJTPG9FmKmcbc2_yzoZIrRmOPNofKJh-lc8iiRizuqEa39EeBPX0LWJkvG1B9cV8Exf-_5Wr1LGoL6eDe9bVBKs6o2UH05Rwdps2G8YChM88B4jpjUFnFS7dPji8Xyoj_7Retm5XU-siMcmayWbjdxoqf9_jAHGXWZnr_05Hy3aTBjjeCGrJUWAaEYuOrnquFCbcDJDd9HovTWFfTDe9UfgFUdLxxj2O-lJ5cTExiQnjRuKLDgyeu7t0MTzl1oCb3_rkhJ_JywPaYO0lD4nvaStXNfR8xNB5mlSOuGQSei4kMDaJ9Y2_K6AmPl-jTxpm8XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
🐐
حمایت فیلیپه ملو از کریستیانو رونالدو:
"یه تفاوت خیلی فاحش بین رفتار بازیکنا با کریستیانو رونالدو و رفتار بازیکنای آرژانتینی با مسی وجود داره.‌ من می‌بینم وقتی بازیکنای حریف مقابل کریستیانو رونالدو بازی می‌کنن، خیلی بیشتر بهش احترام می‌ذارن. تو تیم ملی پرتغال، هیچ‌کس حتی به گرد پای کریستیانو رونالدو هم نمیرسه! تو نمی‌تونی بذاری بهترین بازیکن تاریخ همین‌جوری بذاره بره، انگار نه انگار که اتفاقی افتاده؛ اصلاً راه نداره!"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107784" target="_blank">📅 08:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107783">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d08431eb67.mp4?token=nbGZG8xmCjOV2BDTYWqQj1I67hPGPEyjkho7pt8gFHHBzUNKIxgHT0PRQLTOrVUhu50vbHmAc7m9bH4om-W0Niscc8kPIeUtG_15m0iVACScBybOE_lFDPhs4kjWptEaXWi_nffWkBTgPvnUI_MNoUThA0tdqCuh8JhPwajTf8d6-s9q1ciyv_wO91uC89_iN6TW45ycnpVNtv4aEk1AwYsy_Sb_Ut7SZ0nlBzHrA36wOGsjLu5KQR-0iqg07UEI4yUzEIi5V1MuErFA7wbZbO7Enew7bUGyDBr1WObysZwKhkdjJ_0_d2nGQU0tappgqFmwbEpiO-HLSn_6jdxogQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d08431eb67.mp4?token=nbGZG8xmCjOV2BDTYWqQj1I67hPGPEyjkho7pt8gFHHBzUNKIxgHT0PRQLTOrVUhu50vbHmAc7m9bH4om-W0Niscc8kPIeUtG_15m0iVACScBybOE_lFDPhs4kjWptEaXWi_nffWkBTgPvnUI_MNoUThA0tdqCuh8JhPwajTf8d6-s9q1ciyv_wO91uC89_iN6TW45ycnpVNtv4aEk1AwYsy_Sb_Ut7SZ0nlBzHrA36wOGsjLu5KQR-0iqg07UEI4yUzEIi5V1MuErFA7wbZbO7Enew7bUGyDBr1WObysZwKhkdjJ_0_d2nGQU0tappgqFmwbEpiO-HLSn_6jdxogQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
سوپرگل سکسی یامال در تمرینات اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107783" target="_blank">📅 08:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107780">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df11e10418.mp4?token=n90Fg0YlL4sxcRKs7ySYFVkh507F-yuTllH0TpVcKgdEOYoggViGjdkQHLFfpCxnY8y50NWgBx-7mKStNQOwJkK3ugTG65_eBepw0___fh6PzbDH2hxFhbHsSKpl6EBKSomK6i18S5IDYudB0XpVOpSR2s9uJQULHphVhfzfavxgj2nq4EJ5LXX6l-327I91t_EFkX3mNs13f18CvBGgZ3dhikKgHGopjbG3cD4ddlG8L2Y9Y25BiPcP_Te7McUo6sqbBDVZ5gd0kLQfHmuMdwZXKRV78kG61I3HATWv7GPQDqH0D9pvSO7ZluAnpJqOZ-hmaO_w2S8UoEEl3BUoIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df11e10418.mp4?token=n90Fg0YlL4sxcRKs7ySYFVkh507F-yuTllH0TpVcKgdEOYoggViGjdkQHLFfpCxnY8y50NWgBx-7mKStNQOwJkK3ugTG65_eBepw0___fh6PzbDH2hxFhbHsSKpl6EBKSomK6i18S5IDYudB0XpVOpSR2s9uJQULHphVhfzfavxgj2nq4EJ5LXX6l-327I91t_EFkX3mNs13f18CvBGgZ3dhikKgHGopjbG3cD4ddlG8L2Y9Y25BiPcP_Te7McUo6sqbBDVZ5gd0kLQfHmuMdwZXKRV78kG61I3HATWv7GPQDqH0D9pvSO7ZluAnpJqOZ-hmaO_w2S8UoEEl3BUoIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎁
زلاتان ابراهیموویچ به مناسبت تولد ۴۵ سالگی‌اش، یک خودروی فراری مدل F80 کادو داده. قیمت این فراری، حدود ۳.۶ میلیون یورو تخمین زده می‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107780" target="_blank">📅 00:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107779">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f84ad4f46e.mp4?token=PzJUp1zXq6SJDakQX1Xkqv3vSo1P2WZL-ISmWJtAYLnH0MvR6us_R6psBrc2HuU4WoprYKsyexrsbCM2SBBNwAguTmbzUdX3Rc_vcGU5zkLtAdGdF61IFgT_8ObZOFtPDrEhw132Y-HofnvrRfkRryZGdBFlbpvP8L7_wFP9l3YILkcAmnfALHAIEgO-CoYmByk3G3veIOtpVOQylm9rrV-veyqS3m_24CX18rP8NsNF0gOx4hKqMZExk9IX0IsQWBbmRB2l1lNQivMWH_YHOpNH4Ut88gtL5_AanD-iEthDvWgbFuYi17DdO2IUa-5L6U0vghug8GOMnk7tsEvfAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f84ad4f46e.mp4?token=PzJUp1zXq6SJDakQX1Xkqv3vSo1P2WZL-ISmWJtAYLnH0MvR6us_R6psBrc2HuU4WoprYKsyexrsbCM2SBBNwAguTmbzUdX3Rc_vcGU5zkLtAdGdF61IFgT_8ObZOFtPDrEhw132Y-HofnvrRfkRryZGdBFlbpvP8L7_wFP9l3YILkcAmnfALHAIEgO-CoYmByk3G3veIOtpVOQylm9rrV-veyqS3m_24CX18rP8NsNF0gOx4hKqMZExk9IX0IsQWBbmRB2l1lNQivMWH_YHOpNH4Ut88gtL5_AanD-iEthDvWgbFuYi17DdO2IUa-5L6U0vghug8GOMnk7tsEvfAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
‏لحظه
اصابت صاعقه به برج میلاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107779" target="_blank">📅 00:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107778">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0ule1a9wmoICTsXI-5UB3jir9TkZg3bMYEQBrwh9nIVWRHX_yo-MFo5x2kArzvEP9bMegj1rbivaAq1URGMk50xsJ78uxowWiK9QsdmQ_YvnSrXUACHeM7NPsEe_57yXtGKWqrBjmhy5K5TZmOF0cF1h2WYE953vWVFQH_QcjYVloclkSS3POsGvHe-j2HB8quFP9kOv3nAUebvCEeiq7RyeEz8xmRZ4YqPkH2qX9GAE9aLFm0u_quOHMu_GnnsJ86mXrJbr39RWpvM3D2RXY1trQJcLKOll0j3nyrLyTrWRWeCD4uTJcmZ4BgNDGUzDFixOjYPRjL3So12Q7i8Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
لیگ ملت‌های اروپا| تیم اول و دوم ندارد؛ اسپانیا با هر ترکیبی برنده می‌شود
اسپانیا سه - ‌چک یک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107778" target="_blank">📅 00:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107777">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abea032aaf.mp4?token=P6Q2S6G5wq_Yo8kldepVZeCmHCDlRhUe14fJzqDaJbRCtr3czaG48Q5cBZ3FP1GggczdXLA-cdBR_mcf7pJZ-KyBldUHLhBySGYHtey3gtbNVVIhpgPNYZ2Y5kn0feLq4aDHmCqEvrNDVUgLWsjtGrP9GKGSqbUNHjdy2oogN2p6P6vv71qyb6cF6qUG7Baa2JcHdzBdFI9D1DRFJ_4vUMgewgTQGfJKEBDmMpZVMbD6GhRYa6nELeHr7dXUU5U-81dumiEdp3IMdXmGVO62Ju5OYV0T3vBKgi23pvG55ReY67lqodBnx6br7sr67K-QK83EYa_RQLBiQ0jng83Cag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abea032aaf.mp4?token=P6Q2S6G5wq_Yo8kldepVZeCmHCDlRhUe14fJzqDaJbRCtr3czaG48Q5cBZ3FP1GggczdXLA-cdBR_mcf7pJZ-KyBldUHLhBySGYHtey3gtbNVVIhpgPNYZ2Y5kn0feLq4aDHmCqEvrNDVUgLWsjtGrP9GKGSqbUNHjdy2oogN2p6P6vv71qyb6cF6qUG7Baa2JcHdzBdFI9D1DRFJ_4vUMgewgTQGfJKEBDmMpZVMbD6GhRYa6nELeHr7dXUU5U-81dumiEdp3IMdXmGVO62Ju5OYV0T3vBKgi23pvG55ReY67lqodBnx6br7sr67K-QK83EYa_RQLBiQ0jng83Cag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم اسپانیا به جمهوری چک توسط میکل مرینو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107777" target="_blank">📅 00:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107775">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f7684655.mp4?token=RxhJXXW-6-7UXijb56JcnDoG7N3f0gC9enQ21-dF4nnwj6KqvRMby1It9W1PhGXKxzlNW4uirDWxIe7Vgz6YUuh0zL3VazSReh3LezFBMHGx6rZuTG3nbCW3PjXzndsWl7ml1h8xhVtbvpjGeC9jt_uSeT8ZJMr3d1DFCLKa1n4YV2UcwDjTVNRAfrkUBkKQQKihsfJa0ReOiAYG2AtHNPZtuyer6LrWzmSCzhdK7HcTIQdxZHo2QWjDglGOJPfrF9vxPXoQJRRP9shyYIT5w4aG0l9Eji2I4tq_jLZRBNXxn2lBgxOHe40j0cjd9SpwkLQpBsWHTQ02o6R3zTe6dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f7684655.mp4?token=RxhJXXW-6-7UXijb56JcnDoG7N3f0gC9enQ21-dF4nnwj6KqvRMby1It9W1PhGXKxzlNW4uirDWxIe7Vgz6YUuh0zL3VazSReh3LezFBMHGx6rZuTG3nbCW3PjXzndsWl7ml1h8xhVtbvpjGeC9jt_uSeT8ZJMr3d1DFCLKa1n4YV2UcwDjTVNRAfrkUBkKQQKihsfJa0ReOiAYG2AtHNPZtuyer6LrWzmSCzhdK7HcTIQdxZHo2QWjDglGOJPfrF9vxPXoQJRRP9shyYIT5w4aG0l9Eji2I4tq_jLZRBNXxn2lBgxOHe40j0cjd9SpwkLQpBsWHTQ02o6R3zTe6dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول جمهوری چک به اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107775" target="_blank">📅 23:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107774">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdcc4901e9.mp4?token=B-WUf-g24rvuepHh4Y4fKDcRZIhfdy1FLMB1MT2JGht7e9fpvBF80MQ6rajjTWHe6fsv1leQ5kghtV4p18L9IUgbJ2P0EOfmokpalEd7Oy_DkS688phmNUqutEPmd6IGl46xO0aouNr80ENEJXkaXi7XMRM73MC8ygF-WBSTt5BrLOEqAKdfL_TqT9tORA-LpNNHfPO6IUW2DR41M9T0BXEq870bwh_uP54J1m6089DPSC2LhwIPafB_vlfA50OGJHZnhQTEq2JEwaPmkUtWrkdAFwkY-VAmgnXtfMKFIGaPIEwwHV5ndtmeGQsUncK57Ug1vRszDbWYAO7akU7SlTcbqGtMssmj6fMrlQ8mjfDL80X16RtsLDBn6BBiSjcLte8lPoaEhBXIJmFCAPpd5ZCWK8lMfPI8OCm9HPKpIwe7OAZ5vFSao9nuXWntSPg_-_O5vocKMGLrS3NkNk1O1Im73V2ZvxSUxdlE3AVa9R40iws1g2R_TNkUof8VA9Tdrb91W_ZaqyjnhtE5yeK7NkwcZdP3-13_InhlNmy6Cw4Uv6DzOtEE75XuiNFHVJvwvG2muoUSXQk73sa4gEusfSE2pu2zvW-IdtgdKxnKXZ2SypDiH8VlfPYz4wQL3yWALUeC8Hf4gdbt5t9iQm0IUOF5WVumuCe24xf2cmDJkSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdcc4901e9.mp4?token=B-WUf-g24rvuepHh4Y4fKDcRZIhfdy1FLMB1MT2JGht7e9fpvBF80MQ6rajjTWHe6fsv1leQ5kghtV4p18L9IUgbJ2P0EOfmokpalEd7Oy_DkS688phmNUqutEPmd6IGl46xO0aouNr80ENEJXkaXi7XMRM73MC8ygF-WBSTt5BrLOEqAKdfL_TqT9tORA-LpNNHfPO6IUW2DR41M9T0BXEq870bwh_uP54J1m6089DPSC2LhwIPafB_vlfA50OGJHZnhQTEq2JEwaPmkUtWrkdAFwkY-VAmgnXtfMKFIGaPIEwwHV5ndtmeGQsUncK57Ug1vRszDbWYAO7akU7SlTcbqGtMssmj6fMrlQ8mjfDL80X16RtsLDBn6BBiSjcLte8lPoaEhBXIJmFCAPpd5ZCWK8lMfPI8OCm9HPKpIwe7OAZ5vFSao9nuXWntSPg_-_O5vocKMGLrS3NkNk1O1Im73V2ZvxSUxdlE3AVa9R40iws1g2R_TNkUof8VA9Tdrb91W_ZaqyjnhtE5yeK7NkwcZdP3-13_InhlNmy6Cw4Uv6DzOtEE75XuiNFHVJvwvG2muoUSXQk73sa4gEusfSE2pu2zvW-IdtgdKxnKXZ2SypDiH8VlfPYz4wQL3yWALUeC8Hf4gdbt5t9iQm0IUOF5WVumuCe24xf2cmDJkSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
کارشناس صداوسیما: چین دیگه بهمون تصاویر ماهواره‌ای نمیده و بهمون گفته اول برید مشکلتون با آمریکا رو حل کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107774" target="_blank">📅 23:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107773">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‼️
💵
دلار به 271 تومن رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107773" target="_blank">📅 23:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107772">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a91b6171a6.mp4?token=pAq4Gyxb1yZXULGldq6vMyqi2uCNa9abf37RAXHbeLAAevDi6UaGN5rkhAoOwi3MX7Gz5GQ9bt4LAbl7LmaaPK9hUAPYdjnZNu6VE7vdrznmW9eNIIhWuRIeX91uZ-4foilL7Ypei7a8CwYpxU6St2ds0wjX-d81jkMXyHhFheoKKU80WPWvDgMr_cTTS80UeLtX2utjV4gDhb1j1R9ERU0H4gumCmpm_ohxvlKXeXL442MYsVoxWHgCDmzcEY5TQknLKhQOjX4VxxDMxoWJH8TprqzZawBkjz4-Oz5aFhzjd2HwyQOuyCfxToxFvCJmMbMyb1BolodBe4o6LImFfnUavD83pEdxBDjmGFZuqlj6_AHWDGo0rmwBKZDtwCS_rWLBc83PeegcEdoQ512WZ4ThdHEDLWiTu486edpcuQ_id1pVLzvnDyEEELmefWrWcKtG0svx9EpmtuL0rXfKQK-ytMIB8o1kErRFsZ1Xjf6puibGcT27EFbS8iqc5FCYG2twnA1qP4wqBhTqlcglXGiEPytBRE9OJWggQ3cqM8Vecl1kSx6nF1Q52jMaPhMfVI5HZteto5rPqoTorNJy-V95DCXA31aDgsxmgXk1VWIlBsiRNVeAFVgdT0r9cM_9QfW6ZSAbpS0r7Oiu8sgYk6Zd0eWZccY7v83g_2XOBDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a91b6171a6.mp4?token=pAq4Gyxb1yZXULGldq6vMyqi2uCNa9abf37RAXHbeLAAevDi6UaGN5rkhAoOwi3MX7Gz5GQ9bt4LAbl7LmaaPK9hUAPYdjnZNu6VE7vdrznmW9eNIIhWuRIeX91uZ-4foilL7Ypei7a8CwYpxU6St2ds0wjX-d81jkMXyHhFheoKKU80WPWvDgMr_cTTS80UeLtX2utjV4gDhb1j1R9ERU0H4gumCmpm_ohxvlKXeXL442MYsVoxWHgCDmzcEY5TQknLKhQOjX4VxxDMxoWJH8TprqzZawBkjz4-Oz5aFhzjd2HwyQOuyCfxToxFvCJmMbMyb1BolodBe4o6LImFfnUavD83pEdxBDjmGFZuqlj6_AHWDGo0rmwBKZDtwCS_rWLBc83PeegcEdoQ512WZ4ThdHEDLWiTu486edpcuQ_id1pVLzvnDyEEELmefWrWcKtG0svx9EpmtuL0rXfKQK-ytMIB8o1kErRFsZ1Xjf6puibGcT27EFbS8iqc5FCYG2twnA1qP4wqBhTqlcglXGiEPytBRE9OJWggQ3cqM8Vecl1kSx6nF1Q52jMaPhMfVI5HZteto5rPqoTorNJy-V95DCXA31aDgsxmgXk1VWIlBsiRNVeAFVgdT0r9cM_9QfW6ZSAbpS0r7Oiu8sgYk6Zd0eWZccY7v83g_2XOBDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
جواد خیابانی بعد چند ماه نمایش خداحافظی از تلویزیون امشب دوباره به شبکه‌ورزش برگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107772" target="_blank">📅 23:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107771">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd54269d70.mp4?token=FwHq-_F4WV6SsJZ0bkJdZAKNH4f3QsQoGcyaMuD_3lYSloVK7PQvwtJUUkpnkZj51Ei2B33JHLyP8DoVGhsFHnTTWCKDDDOdrcV338aWonIvtoeChpru4YTr3DdbqePTQWSlIfKTrhIIP6set610CXVICJ9bvHfnlCdj2_4csmGTLMnR50uvbFTOElCi5selxS_BsVBhr-K-qVRmhzxdeyoWjUn8HAU_n5FB69k1lwTCyCe1Wmua_cC1heYGKJueAPA1DZN18iTOtxRZswDlz3E4ov4K1ORM2IogUdDaQBSAMSHV_0zSU4lN8iGeBpE8kEqrePeSMqG-qOgrmx6t9ZvWVtw4vD_6e4VqdBeuHknwtn2DBRk2rLGgjxAT8_rwu8lA5i17tY0LU7qe9lJELtJUxbXp-GCfS9rsUFqkG41vJt4fBq9KMKiz3owAs0qdJatA6nwbBs5SzsE1mA0N5-LmLTblKncDB-0iC3I7zMIUF1WVPgg5RcZAjD2FJuxMsbs8isKrwJCC_X9zTAuxKz7l7Z7hXg6EVCwo5y-2DD5nRZDkN_eUv4GUs5qgNktYpACPbrhKVOx-3xpnwU8aSn4mfbe-Z1uSML1w6GfWs0X3u9wROeEpxjsR2FahTXbVW6rt5Dz_BR114XXJdgUVCvVTYOl4Vwup1GHqWVvG0IY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd54269d70.mp4?token=FwHq-_F4WV6SsJZ0bkJdZAKNH4f3QsQoGcyaMuD_3lYSloVK7PQvwtJUUkpnkZj51Ei2B33JHLyP8DoVGhsFHnTTWCKDDDOdrcV338aWonIvtoeChpru4YTr3DdbqePTQWSlIfKTrhIIP6set610CXVICJ9bvHfnlCdj2_4csmGTLMnR50uvbFTOElCi5selxS_BsVBhr-K-qVRmhzxdeyoWjUn8HAU_n5FB69k1lwTCyCe1Wmua_cC1heYGKJueAPA1DZN18iTOtxRZswDlz3E4ov4K1ORM2IogUdDaQBSAMSHV_0zSU4lN8iGeBpE8kEqrePeSMqG-qOgrmx6t9ZvWVtw4vD_6e4VqdBeuHknwtn2DBRk2rLGgjxAT8_rwu8lA5i17tY0LU7qe9lJELtJUxbXp-GCfS9rsUFqkG41vJt4fBq9KMKiz3owAs0qdJatA6nwbBs5SzsE1mA0N5-LmLTblKncDB-0iC3I7zMIUF1WVPgg5RcZAjD2FJuxMsbs8isKrwJCC_X9zTAuxKz7l7Z7hXg6EVCwo5y-2DD5nRZDkN_eUv4GUs5qgNktYpACPbrhKVOx-3xpnwU8aSn4mfbe-Z1uSML1w6GfWs0X3u9wROeEpxjsR2FahTXbVW6rt5Dz_BR114XXJdgUVCvVTYOl4Vwup1GHqWVvG0IY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
هنوز چند روز مونده تا پدیده ال‌نینو وارد کشور بشه بعد وضعیت امروز عظیمیه کرج:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/107771" target="_blank">📅 23:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107770">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9943a67dd4.mp4?token=AeKhVZludv4OIiapeHLLIIL6lQXYgi51sKjn8HHUiHS5EnfYkPrMDw2ZwIsggJfXk-4kEc3VwAiDzf-KqI9cZXPkrBQrUu_NyJzTEuzVlE68-LvuPNm4ehbWRoCgIeGss9GrzMaIgMO4or6fnuX6hQaMysEwAijxN4xBMZ6DBTw8-URVprsIIkXoZkbbAZPQiknsOg1Tpl5gpSNB92F3xr0GLHbMJC6o1fzeUP3IOr_11I66GROTolUToKikDJqHj0L1y2NQd76OtgNocD-yKsoWOrIq6J6T_9CAkXRDd3GlHDICMoUcC2tpT4XjrmeTWilIUSQ7AOPhJ18IqgNpqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9943a67dd4.mp4?token=AeKhVZludv4OIiapeHLLIIL6lQXYgi51sKjn8HHUiHS5EnfYkPrMDw2ZwIsggJfXk-4kEc3VwAiDzf-KqI9cZXPkrBQrUu_NyJzTEuzVlE68-LvuPNm4ehbWRoCgIeGss9GrzMaIgMO4or6fnuX6hQaMysEwAijxN4xBMZ6DBTw8-URVprsIIkXoZkbbAZPQiknsOg1Tpl5gpSNB92F3xr0GLHbMJC6o1fzeUP3IOr_11I66GROTolUToKikDJqHj0L1y2NQd76OtgNocD-yKsoWOrIq6J6T_9CAkXRDd3GlHDICMoUcC2tpT4XjrmeTWilIUSQ7AOPhJ18IqgNpqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل دوم اسپانیا به جمهوری چک توسط رودری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107770" target="_blank">📅 22:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107769">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a73573624.mp4?token=GuooJGi6M7zhlft5NWdkEHQJOoToQIdAZAvsklOdWmThvehQAYL0SV-bKXI4cWYPe4PpBcTqBt5Yeep94AZH1w4V21-BPs6aTm_AYq1XgceVfss2idoO6OIUFc7e1jYYJP6Nwdf8TlMiTMGYHPoPpPKL9lI9RUMC24icQMDehvQcbvftIYtV5OovI2cETaKIb4zo6XcEODRMoM9HYhZj86jKq_b5VQUcQMaqURJ4HhzsDf7oHymYd29TcH8BcT-j54CdDlc9fEpU4VdsZn3SBSSqXvLN2ByAKRVjX0VhhqHEwAB_XWi0SbcO2N3iLV1WCcgg1-YEhp7JOgFZfbTP6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a73573624.mp4?token=GuooJGi6M7zhlft5NWdkEHQJOoToQIdAZAvsklOdWmThvehQAYL0SV-bKXI4cWYPe4PpBcTqBt5Yeep94AZH1w4V21-BPs6aTm_AYq1XgceVfss2idoO6OIUFc7e1jYYJP6Nwdf8TlMiTMGYHPoPpPKL9lI9RUMC24icQMDehvQcbvftIYtV5OovI2cETaKIb4zo6XcEODRMoM9HYhZj86jKq_b5VQUcQMaqURJ4HhzsDf7oHymYd29TcH8BcT-j54CdDlc9fEpU4VdsZn3SBSSqXvLN2ByAKRVjX0VhhqHEwAB_XWi0SbcO2N3iLV1WCcgg1-YEhp7JOgFZfbTP6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
گل اول اسپانیا به جمهوری چک توسط یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107769" target="_blank">📅 22:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107768">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اشک شوق قهرمانی و معافیت از سربازی
بازیکنان تیم امید کره جنوبی چهارمین قهرمانی متوالی این کشور در بازی‌های آسیایی را رقم زدند و این قهرمانی برای بازیکنان کره به معنای معافیت از خدمت سربازی ۲ ساله بود تا این گونه اشک از چشمانشان جاری شود
البته لازم به ذکر است که همه بازیکنان این تیم همچنان ملزم به گذراندن دوره آموزشی هستند، مسیری که سون هیونگ مین هم قبلا طی کرده بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/107768" target="_blank">📅 21:52 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107767">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انگلیس هفتا به کرواسی زده
😐
😳</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107767" target="_blank">📅 21:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107766">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmSDsu65VkYSin3I5jpDlXUZBhKjqiQPulJktFrYqlTgC7JOuxCxnZKDqfsjSJNiZawEV-Qbyf4kECdZkUKRhx2oB-zW4ff_eF--oU8v2-N5w-kkEW_xs5ptLXl_PT_v0Ve7QleNTI5mjsr48gC4UdC7kHHo-GNmdgJmj_AmrXCi_EoS0GlchhAPWp7rcwDD-a8479tGifZp_EB-Svyn9zNdA-9dIxsHGqYG7rLuEe_c_2cY7hzF-naFZpS3nu8R0mHUjvtnSmFZadFxS4_MBxyLu4ugGOyesIFAMzpbvdiDvqlAdLpqehm4C2Rz_w1Dv_3j0fXNImkbEbItqqeYcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترکیب تیم‌ملی اسپانیا مقابل جمهوری چک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/107766" target="_blank">📅 20:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107765">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSUw-TYMBdnDagL_HNuDYV-Vd5mrcPMSn7phJ_9NrTfoSHOSd_p_h-ZMTsm9noKzH20L7qAleyh1PepTisC59N2D0I37EjENI0KH2XePCCA18iA8nwkwTn5iauYS5EDY8onGI6uKZcqwLdjda5tY08pL8Dha89ZrJKsssleiUdI23qvnnY-VzYA0p2XaN2C_N1f0O6HaMNm2p64NwSYGUIaW3eAY45KH1QG5ga1-D7pXX3dmHPPvFif4exp39rFJ9OQdwr9EugoJciynKUIOIxWB1dO80x-kGF_7jNOvZu01aiGQ7_edKjHUVWwq1sl6D05W9b5NhKZ7QmyMfPD4kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
🇧🇷
در سال ۲۰۲۲ رافینیا از لحاظ تعداد گل های زده شده در مقایسه وینیسیوس بسیار عقب تر بود اما او امروز توانسته دو گل بیشتر از وینیسیوس به ثمر برساند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107765" target="_blank">📅 20:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107764">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObH9oQ_ebLm2BIvGzmvfpWRz6wC2U4UglgO2JttsidG5Ypu5WFx0GZP5v-SJViqLvPjgJYUZGHE1yG3L_gEWBymsh4L8AqRqWDwQtKO75JG9UzD-2tGUvs0BoNcc_YYV2aV3dLbAOIuEIy52cc6AW2iRHjqSpLAG69t9RoXPiOS8o44R12uy1BGqFVHZKV9Talyyh40XlcnN8qPK1aAjsler4kIDjjXR3iZ8LVVdT1Lpf9iypqxHkstllVlWzX4naXTJGTO0r9T6LWREcfsFoGIC_2-Jwk7bTxHHfNCUbyI2asL2Doy3_3Mch7fDbvCnttjDDPVEbRLGrpIw6O_ohQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
ویرجیل فن‌دایک در سال ٢٠٢۶ به اندازه کریستیانو رونالدو گل ملی بثمر رسانده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107764" target="_blank">📅 19:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107763">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iISL_cjliGHT8Mm1lCk-V_rTG2SkXGLl7FEyq5TDe4C1zsv_wp5C9ixUzCWX46j1ItrLe02fEFF9BKJg6ucZX7oIZhDyqoqC0gsR23ejds6QSFsdIR3xn-HlZTw0ZwMPYElOZrN78PtasgPDhLEHv0CQ_w-Edk2jarbazq6LzPmHB4uXet-NEB8guQUSD3EKbGn4vVLUe9JuUnH81uVdTxCttisgenWWlF4bUIuaMUsjDaLwQIP-c6B2i-pGfHwSRkhzLa0HIUv1WZVWA_5dJOE0eosbiQ_O1vkuQKQBonxHZlgYOK84f7sI5qZALQse_K7VXzSYlwG1bL_0NrTMFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
روبرت لواندوفسکی پس از هت‌تریک برای تیم ملی لهستان در بازی امشب، شادی گل معروف لامین یامال کنار پرچم کرنر را تکرار کرد
🥹
🚩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107763" target="_blank">📅 19:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107762">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f408d58b0b.mp4?token=oGgAmy87Lx0y2UayFZpt-1BLv7cemzv0CqnghJHNMsRlzhTzrGr8GlUdrNt5qIlJ3e4x8CZo02PxZtqPNqklYSF0OSB-JqppMXzU3MsQWenpPkvs2qSuHf5aNZi5rp4z8JR4FGqnkdxLAZcxwZhtS30Fw9VaQnNYTlA8PCM9fqvN-p2kiJAuKG7LdlpWnF49a6oR8QSX6JD3xfP8znhL--SI4RI6zog_lwnBmryehpLM4c6tfCyxUIpLceQF8yorquP-11GJo6o7zf9GU_t0WNbbNv4wAnDdazGL1cz-JlXvqhInoP_mDlX8m3UVUK6tutcJueDn7xj-WFHrvnBTgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f408d58b0b.mp4?token=oGgAmy87Lx0y2UayFZpt-1BLv7cemzv0CqnghJHNMsRlzhTzrGr8GlUdrNt5qIlJ3e4x8CZo02PxZtqPNqklYSF0OSB-JqppMXzU3MsQWenpPkvs2qSuHf5aNZi5rp4z8JR4FGqnkdxLAZcxwZhtS30Fw9VaQnNYTlA8PCM9fqvN-p2kiJAuKG7LdlpWnF49a6oR8QSX6JD3xfP8znhL--SI4RI6zog_lwnBmryehpLM4c6tfCyxUIpLceQF8yorquP-11GJo6o7zf9GU_t0WNbbNv4wAnDdazGL1cz-JlXvqhInoP_mDlX8m3UVUK6tutcJueDn7xj-WFHrvnBTgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
ترو خدا هوش مصنوعی رو از ایرانیا جدا کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107762" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107761">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfuMEvoVxslGelgFUGp4fw80gHdDkS7AbtLpkPTugobkbC2mfmhBUtb4N_pzsSseDFUC16iSZwQ_DMV_CuLJqJpjB0Mo896GFWn73r7OsDl_z7fhjc65YoS-16zRYLywL6JA8VbhgaCnvJC42tZFtOsp2hVsQ2Cqh136SZbP0-qJ8I1ke9htHUhI5JjpNDcNTlKeC6ixo9Qado6rbhJmoS7oH_wMhi7GstvRZxp9ZMej8AxqDl6eZTGA9_b6T9NbLInN6O4j-wboW6UaqT8ma7CkgIzTNEftRSpQcWPY6YTgs_p-_EdWZS-XHacBmKUh3wUWaspgc51-sGSFYvyGaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇭🇷
ترکیب انگلیس و کرواسی؛ ساعت ۱۹:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107761" target="_blank">📅 18:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107760">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58fe91d1ea.mp4?token=oxfBpr4RSygilAo-IXPOqyUw0mFDnl9jf5sthn3P3GueHTtan7MwZsTW2U03YHQIroZNSgLl5IQp-duBpBpVKhlv5gyAMPvRtHmkum_Bk-mTMlhFsBdr_2fPbKyCUfsh-_AW25D4HS-beGhx6vKoTB9PXLZV-esnRLJ_mUCyiGrK-_6EjH0yxuEE66AWvBiXe1mpgKTodDcX2-85VCclXTOWoH3sfZClAuZVUjydoSx6siNfiboSrJEW11rlmIW6Q0lUEAqoWk0FBgpnkL2fkC10jQWwWoLdpr5ZLpcQkrqGM-FPlCBMo6ybLKWwvjbPf9z5kXzCDPdTxf3FD_MHng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58fe91d1ea.mp4?token=oxfBpr4RSygilAo-IXPOqyUw0mFDnl9jf5sthn3P3GueHTtan7MwZsTW2U03YHQIroZNSgLl5IQp-duBpBpVKhlv5gyAMPvRtHmkum_Bk-mTMlhFsBdr_2fPbKyCUfsh-_AW25D4HS-beGhx6vKoTB9PXLZV-esnRLJ_mUCyiGrK-_6EjH0yxuEE66AWvBiXe1mpgKTodDcX2-85VCclXTOWoH3sfZClAuZVUjydoSx6siNfiboSrJEW11rlmIW6Q0lUEAqoWk0FBgpnkL2fkC10jQWwWoLdpr5ZLpcQkrqGM-FPlCBMo6ybLKWwvjbPf9z5kXzCDPdTxf3FD_MHng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚪️
احسان حاج‌صفی: سعید الهویی، هومن افاضلی و رحمان رضایی جزو بهترین‌ها هستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107760" target="_blank">📅 18:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107759">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
‼️
کنفدراسیون فوتبال آسیا برای فصل آینده مسابقات تنها ورزشگاه‌هایی را قابل استفاده می‌داند که دارای سقف استاندارد باشند و بدین ترتیب تقریبا هیچکدام از ورزشگاه‌های ایرانی شرایط میزبانی از رقابت‌های آسیایی را ندارند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107759" target="_blank">📅 17:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107758">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuSgr1xIiufaZJPOaHa3s6X03PSP9BQ98Pc4Vkf8J08vLmeWsfahjF3SHbNaCwTgL7V0GoyCDmAkACx_q503YcXaqXocRhOvIdOx64vot9vuHmVwab1Tf8z3UHnt8XElFfvjVJI5CKUnjYaEXVHkky_bFelaNMycN4-zh5b0d3REkfyyIk33Z3HpKomgEFH1St2vkclqd1WJTcQ8O-8FRi7VWyfM1BfDkz2NfCyH1tcXvme_mNjjoCwAB3NNCD4cmEunSq4OAzn-2Hir6emU9dZ4bsYNePuxW70e4iWfpLtjinKrk_Guz0dz71y4R00QA4X7FzuLUdpRn-2Z-U6MUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💵
دلار به 271 تومن رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107758" target="_blank">📅 17:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107757">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfd85597f0.mp4?token=fiIiAs9SQAu-2FTpHqP2Gnh5sBScrgOHl4fMy4h6XqN0tobGWfNrQX6sHKt-XHV5rX3AQmM35di-8_xTTQjFtMNvVS6BHUTKsel2B1DCWj1O1tnFLV-VeIqXRklM6u__-65DCYat7Ma2GalsBPjShm9t7uPdj_P6GdqLJWnuHFCU_K06i9sXgs8PkbcNXirxxLKXPonubQn5SRlcq3z7BEBb0FEOM6vpRwysxy9cYsr2ji-NifKDfW-qZA2n7smFgafq1Oq6wnhs_dvnliHNnDLKmCGEeu2TwpuBqmxd9YRTodk1qVFUk2z23qu_UlhGbeItZopfLfYGeGy99XSx-jH-M4DWdOWJ_zQtsTu98qjFJ8CxVE6xRHsIL08dCefaPur213v430u3WGmic_dOOgOrLma-jtRIkokaBjflRPcEL7vtpTBX-3tAX1_HfQai_ErrOMHmve_kUHkd1L13ka9WRtF_Xj1ZlxTUEUacHl6CvKkLU9rMiqGwoboGXx_aXQE0p_vyAbbTRRLfPYPyLEWNelEWmMsR8d33sRCM2wDFNsxVU_X78B4Ed1CVYmK1-ekvpc1oC_nlvglVYT1zqqHn5gGk-JBbyQEgvdb9ctCgfDrM9ecBTIQSxSSKA8-oRVgeM9EESK7r0E6BZNJK61s8zCifGOApMUrFQpYeiTI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfd85597f0.mp4?token=fiIiAs9SQAu-2FTpHqP2Gnh5sBScrgOHl4fMy4h6XqN0tobGWfNrQX6sHKt-XHV5rX3AQmM35di-8_xTTQjFtMNvVS6BHUTKsel2B1DCWj1O1tnFLV-VeIqXRklM6u__-65DCYat7Ma2GalsBPjShm9t7uPdj_P6GdqLJWnuHFCU_K06i9sXgs8PkbcNXirxxLKXPonubQn5SRlcq3z7BEBb0FEOM6vpRwysxy9cYsr2ji-NifKDfW-qZA2n7smFgafq1Oq6wnhs_dvnliHNnDLKmCGEeu2TwpuBqmxd9YRTodk1qVFUk2z23qu_UlhGbeItZopfLfYGeGy99XSx-jH-M4DWdOWJ_zQtsTu98qjFJ8CxVE6xRHsIL08dCefaPur213v430u3WGmic_dOOgOrLma-jtRIkokaBjflRPcEL7vtpTBX-3tAX1_HfQai_ErrOMHmve_kUHkd1L13ka9WRtF_Xj1ZlxTUEUacHl6CvKkLU9rMiqGwoboGXx_aXQE0p_vyAbbTRRLfPYPyLEWNelEWmMsR8d33sRCM2wDFNsxVU_X78B4Ed1CVYmK1-ekvpc1oC_nlvglVYT1zqqHn5gGk-JBbyQEgvdb9ctCgfDrM9ecBTIQSxSSKA8-oRVgeM9EESK7r0E6BZNJK61s8zCifGOApMUrFQpYeiTI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
گریه‌های بی پایان بازیکن سابق استقلال در شب دستگیری در کلانتری دماوند!
❌
خاطره بامزه بابک مرادی از دستگیری بازیکنان استقلال در شب سالگرد ازدواج مهدی قائدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107757" target="_blank">📅 17:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107754">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967556808b.mp4?token=gUJYN7hjWRNvDPG0GmkZ2eo5leg20TFE7Vlbzke_FeFv5IwKD4IsC4y7MkGINqHDkqxq8I5v_VnC3MNFZ6GqVLWnkcy2rxP6agvpzZ7wCOVLQuy7Cr8f8D9-I1AK8Eh8hEhLuUDJDVc3Q-Fz2C36YwGfNDysrmsCqwW6v2gbwIog0MIMIiDAHZNxPm8F5PnI3HXILBZjnu8XpcppWgMj5Hddwld73oRSctekCPal5-TGkTAcSJV6BvLDcL_RxyCuYlx1qir01wxbTe5vrsCBKNq3ysFW29Q-lTb2uB7CJSX1KXCCNwqB8gTK6zIfTrAqJlaRJluAeGA1gC9YADFE6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967556808b.mp4?token=gUJYN7hjWRNvDPG0GmkZ2eo5leg20TFE7Vlbzke_FeFv5IwKD4IsC4y7MkGINqHDkqxq8I5v_VnC3MNFZ6GqVLWnkcy2rxP6agvpzZ7wCOVLQuy7Cr8f8D9-I1AK8Eh8hEhLuUDJDVc3Q-Fz2C36YwGfNDysrmsCqwW6v2gbwIog0MIMIiDAHZNxPm8F5PnI3HXILBZjnu8XpcppWgMj5Hddwld73oRSctekCPal5-TGkTAcSJV6BvLDcL_RxyCuYlx1qir01wxbTe5vrsCBKNq3ysFW29Q-lTb2uB7CJSX1KXCCNwqB8gTK6zIfTrAqJlaRJluAeGA1gC9YADFE6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇸
و بشنوید از مدل ماشین دروازه‌بان اصلی و معروف تیم‌ملی اسپانیا یعنی اونای سیمون
👀
🚘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107754" target="_blank">📅 16:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107753">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b23bb5ad12.mp4?token=UNRLN4pyOEDX7KKQ7ABQSwExOlZBXXPPHquhHSYRPNOhOPOh2Roz1j7YW91O0gWOtTPOCIlv5umg9WIcV0HHDZp6uiPs8JxEt4J3WKQ-QF1NywzPLKNmi0rgrrqGcmD_XpAFDFSuGVA-LDs71_TVDDtodYbGpAFWwyc3B0snfiW5G-p_IsLo7Kr1IlbIV5wf4rz9vLcnXx9Z2CRDlw5iAqt8gXx6av7Lh5U5Vr2GKS7-H26726ICPqHZYvfx7BoBp5YZym2O7ZxlKDqu_1avUU1CZ3Lp6d3py5KplOW4e4ylJJI3_foqSBghtK7MI86VF5M5HONlnBGJTPpUydxpQYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b23bb5ad12.mp4?token=UNRLN4pyOEDX7KKQ7ABQSwExOlZBXXPPHquhHSYRPNOhOPOh2Roz1j7YW91O0gWOtTPOCIlv5umg9WIcV0HHDZp6uiPs8JxEt4J3WKQ-QF1NywzPLKNmi0rgrrqGcmD_XpAFDFSuGVA-LDs71_TVDDtodYbGpAFWwyc3B0snfiW5G-p_IsLo7Kr1IlbIV5wf4rz9vLcnXx9Z2CRDlw5iAqt8gXx6av7Lh5U5Vr2GKS7-H26726ICPqHZYvfx7BoBp5YZym2O7ZxlKDqu_1avUU1CZ3Lp6d3py5KplOW4e4ylJJI3_foqSBghtK7MI86VF5M5HONlnBGJTPpUydxpQYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✅
ویدیو کاربردی از نحوه جدید سوخت‌گیری که به تدریج در کل کشور اجرا خواهد شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107753" target="_blank">📅 16:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107752">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b48e9e7f4b.mp4?token=Ik9xM0Um1770_b0bGOejO049PD3b3A-DVjLut9WFuHfAULxhQJAG6eFgYpaJbA0p_Z0NAinRF6oqR2UvUGXHbADyqO8b4kwIj4IkinDxrWW0di2dhOlc7ORJeVnf8Zgp2PR5Rl7UaW1vneZB_2IQ_lmqk9Q4Ej0Opw6f9h7HsZmsC8COBK_UYHU60tcsXrFH5XRY67IFtOVl7n80OqqRDxPjCUHUT9Z8GOW_iuDsMF9zbJBfnbNocOve94rwvbg0xdASEQ1-dMX__5KfiizVymgrgNFbX1ZqijqojkrK1ukgs7LXHNIggQu5MkA3AP9v3I-TytfGKbiPpZGhNycUymCM6fR_hPm8Y0zgIvPfVO7qc4tf_iRCdw21XOVFBI_tFpUTF9Gp1vHwpEC6ICi70-S496u0tg1UijJu1u2Wn9Sl0JoBRoZHlhj50o_qb8Gvs67wbx6Qjgu_2jJk3dUuwNINTQ1OO3kmaeNNYihTJg9XoRHvJDDbUEfkE1P0WR6DvTn7_DWxG4dWX7CuNXGvBAQ00eslLBjeyRjiQETUN0KT5axSi1mVS33zWP6Its1tfc39erbh4OvIpZJ9fKe8IMPamY8UFLcp4FFEF5CbQRY4QnZLbfpwvTNuGGIFGPi3cLtiDX_9GZkxI5Ak-3G-_MZumPvKDekEcopdPDboWfI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b48e9e7f4b.mp4?token=Ik9xM0Um1770_b0bGOejO049PD3b3A-DVjLut9WFuHfAULxhQJAG6eFgYpaJbA0p_Z0NAinRF6oqR2UvUGXHbADyqO8b4kwIj4IkinDxrWW0di2dhOlc7ORJeVnf8Zgp2PR5Rl7UaW1vneZB_2IQ_lmqk9Q4Ej0Opw6f9h7HsZmsC8COBK_UYHU60tcsXrFH5XRY67IFtOVl7n80OqqRDxPjCUHUT9Z8GOW_iuDsMF9zbJBfnbNocOve94rwvbg0xdASEQ1-dMX__5KfiizVymgrgNFbX1ZqijqojkrK1ukgs7LXHNIggQu5MkA3AP9v3I-TytfGKbiPpZGhNycUymCM6fR_hPm8Y0zgIvPfVO7qc4tf_iRCdw21XOVFBI_tFpUTF9Gp1vHwpEC6ICi70-S496u0tg1UijJu1u2Wn9Sl0JoBRoZHlhj50o_qb8Gvs67wbx6Qjgu_2jJk3dUuwNINTQ1OO3kmaeNNYihTJg9XoRHvJDDbUEfkE1P0WR6DvTn7_DWxG4dWX7CuNXGvBAQ00eslLBjeyRjiQETUN0KT5axSi1mVS33zWP6Its1tfc39erbh4OvIpZJ9fKe8IMPamY8UFLcp4FFEF5CbQRY4QnZLbfpwvTNuGGIFGPi3cLtiDX_9GZkxI5Ak-3G-_MZumPvKDekEcopdPDboWfI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عجب دوران‌کودکی جذابی رو‌ پشت‌سر گذاشتیم...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107752" target="_blank">📅 16:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107751">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9d2f3d6a6.mp4?token=ZA7Z7MTLk9ZHlhBgBJk79amIUQM59_X4XpRK3V4sH24UI2-mJvZ19becPx0bOa5bEzq8f6VAwXy4ff7OSxWH1jxqzcdsrVixlZkox9RVgP-ektCt7smTQRzy1SDbry70CzBPivCIwGZzIrAx-YwvEti5eUU3yHf0KX7z5wXEs73h-hKiEHqhIfFmZoeS54PwA2wvquVJdjz4FT7-vqdSNaesBbs27LcZfAtza1Qt2OZ_xeuwBGQvQkLN8X6sqGs1TVndVz6lJFXwMo81YbsHipMm0Wsh0cNM8V387JZPcllscMSkU32cn1zKqfiiw7oYj5hxZP-EgzQQNkKoiHC20w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9d2f3d6a6.mp4?token=ZA7Z7MTLk9ZHlhBgBJk79amIUQM59_X4XpRK3V4sH24UI2-mJvZ19becPx0bOa5bEzq8f6VAwXy4ff7OSxWH1jxqzcdsrVixlZkox9RVgP-ektCt7smTQRzy1SDbry70CzBPivCIwGZzIrAx-YwvEti5eUU3yHf0KX7z5wXEs73h-hKiEHqhIfFmZoeS54PwA2wvquVJdjz4FT7-vqdSNaesBbs27LcZfAtza1Qt2OZ_xeuwBGQvQkLN8X6sqGs1TVndVz6lJFXwMo81YbsHipMm0Wsh0cNM8V387JZPcllscMSkU32cn1zKqfiiw7oYj5hxZP-EgzQQNkKoiHC20w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⚪️
بازنده‌های پر سروصدا یعنی اعضای تیم‌ملی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107751" target="_blank">📅 15:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107750">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jw51xB0JqLezkGUsqqanr3lpOiZywLE3clxr_jRFqzVBIRYg28uPNyb8A4T7tqF5cJjibjmEnJ7c32y3CTlQXYIaL9iVRv1TZcYlEKw1S1VzzZfzX3j8TtvqLkq1j6sk61nmzALMP7eCYtSORJJsi6sdlP7idrxwxxs5cEsoSfj1KzU3IRNIF-ZghX5F8IGEl0i50xUTLeeQCDrn1ru_xyX7JudkEtMyQbYInHur_SabTBze33Gz-YV549u8AErsSrx6yLtBopdCgqx1pzYdI4YQ7bCTvPTb0gbQ5LI784XdebXVAvUnWzLjgfG5_1sAilhxAgTxnnGnPcfUbuAZpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇺
میسا رودریگز "تحت تاثیر" قانون "پنالتی به سبک مارک پوبیل" قرار گرفت که اکنون توسط یوفا اعمال می‌شود.
❌
در بازی پاریس و آرسنال در لیگ قهرمانان زنان، یک حرکت مشابه حرکتی که مدافع اتلتیکو و دروازه‌بان موسو در برابر بارسلونا انجام دادند، به عنوان یک خطا (پنالتی) اعلام شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107750" target="_blank">📅 15:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107749">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🇪🇸
رومانو: بارسلونا پس از فیفادی قرارداد سه بازیکن یعنی رافینیا، برنال و ژاوی اسپارت را تمدید میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107749" target="_blank">📅 15:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107748">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86371ca1ee.mp4?token=jCVDt3ACSJkvEIsV3RSmdvaUrkLJvclnVfdZqh83xPTmW-nLseRXWA0ZiIEocUzEe_jglP-0JDOW1FCPpLYEBUfl248Y1hNVNGlpPMtjR4aVz-oyvL52cIlG-GKjv3GH8KHCLRZrgT2Mq0JHkkKm_BDIJBURQPSxMZlp2frB0_PPNmn_VU9kwVWAQRbHLkWTxxnQbHPTNEU6l4DLaReOTsIG99EpgS7ALdz0FgXco6w5ML9NrxrwaK0ViIJRzexW26LgRvPiGnfRwfw8a3imaMs7o1zOCU3rifE8Nl7sTGd0ezfY89PXSDKPVLY3vk8V1guGVgPUm3OXJVmr718bwDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86371ca1ee.mp4?token=jCVDt3ACSJkvEIsV3RSmdvaUrkLJvclnVfdZqh83xPTmW-nLseRXWA0ZiIEocUzEe_jglP-0JDOW1FCPpLYEBUfl248Y1hNVNGlpPMtjR4aVz-oyvL52cIlG-GKjv3GH8KHCLRZrgT2Mq0JHkkKm_BDIJBURQPSxMZlp2frB0_PPNmn_VU9kwVWAQRbHLkWTxxnQbHPTNEU6l4DLaReOTsIG99EpgS7ALdz0FgXco6w5ML9NrxrwaK0ViIJRzexW26LgRvPiGnfRwfw8a3imaMs7o1zOCU3rifE8Nl7sTGd0ezfY89PXSDKPVLY3vk8V1guGVgPUm3OXJVmr718bwDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
مهدوی‌کیا: دوره پرولایسنس در آلمان در یک سال برگزار می‌شود؛ در ایران ٩ روزه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107748" target="_blank">📅 14:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107747">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e10be0d86.mp4?token=Sa5LwWnL-vxXpXsDmWFLTrgLe7YCD2kNEgUBERMmajN305M3YmxZ6r2fwRY1Tk9inMoA-40Lj8ZRF3Vvs17klkeHkgd8172Xhsi07qb_9Wwek6YINTI5gVO5_U1SiS_aXQanCxsvPwj91k-pVkVaXaV3W-19bP0bOLr4oZKPGQU24UNod4zRo2s0NHq11ugmW8a00Lx7-Xz_4ZgYsi6XOPVW5cu7E0i7059_s-T4TcTtZ78wLQvs8ECw8iTLS9e1fQSO5-7soLUanxN1yVQTdu_lAVsscQdHd-iYO70g6mXu6cuL7nAZniKJBnOnaGeGxR3SlLyUlunmkKGiCkqP4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e10be0d86.mp4?token=Sa5LwWnL-vxXpXsDmWFLTrgLe7YCD2kNEgUBERMmajN305M3YmxZ6r2fwRY1Tk9inMoA-40Lj8ZRF3Vvs17klkeHkgd8172Xhsi07qb_9Wwek6YINTI5gVO5_U1SiS_aXQanCxsvPwj91k-pVkVaXaV3W-19bP0bOLr4oZKPGQU24UNod4zRo2s0NHq11ugmW8a00Lx7-Xz_4ZgYsi6XOPVW5cu7E0i7059_s-T4TcTtZ78wLQvs8ECw8iTLS9e1fQSO5-7soLUanxN1yVQTdu_lAVsscQdHd-iYO70g6mXu6cuL7nAZniKJBnOnaGeGxR3SlLyUlunmkKGiCkqP4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
😳
ویدیوی وایرال شده از کلاس تخلیه گریه برای بانوان در تهران! این خانم‌ها برای تخلیه احساسات خود در کلاس‌ها پول پرداخت می‌کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107747" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107746">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd4b89af76.mp4?token=jvOKNdhzc-_lIhjWED93GPArLkAbsGKBvi_NjmdzYOOxDLR4VNGegKELFbT5E6PHtf5S7sMojn1Htrq7ur-Reah91-mrwW6sis8CXIDdASmLEhXc1f2OrQo83jnii_WfnD-Co6V4X-k0VVb6gMSW0oUVWbgumaeMOOyJUIPd--41_CaApiYHWybSdBNwilTLLzIOmjnm3lVYtYvp8vVLWtA-DsNHvhSSJRh0GW8RECRLgVbpuVx9lKFImqWMq_E5lgOdn2LBvc83H77fcnHXYHMIUbMUrjYPUAYdVyTg-c3MDk2TAlpfjNkXYKvje9UGF6GxQwEFsgEs8DhW6yb3jh642JDlxZbSq6Z16y48q_xning28mOh17v1Yu4ntDPW3Vhdh3IGPxwThbZkJX0j94rH7DGO7KLT4UKUL7SwLol3genZNNDXUv4pp7APIvgmCoTOnEMq8CigPjFpkRhTVlnj6G7ph69tDPOwpdeH07_zR9y8BiUEn8pJw7BTQx1yoMAPSCa4nbjy3YkrQrzw9LKrTpUE-DNk4mmKF8bTYj7OC2KsEFsPkK6Y2efFux-WHE_pmAMbWPXWAyX-VaKUhFPiYcD75qmbolkD960UUEON8ZMnVTXScuG10TvMvaxwlLOQo4D6w1Fu8ka5ehy21A7M9BGWbuX4x4mTirvw6w0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd4b89af76.mp4?token=jvOKNdhzc-_lIhjWED93GPArLkAbsGKBvi_NjmdzYOOxDLR4VNGegKELFbT5E6PHtf5S7sMojn1Htrq7ur-Reah91-mrwW6sis8CXIDdASmLEhXc1f2OrQo83jnii_WfnD-Co6V4X-k0VVb6gMSW0oUVWbgumaeMOOyJUIPd--41_CaApiYHWybSdBNwilTLLzIOmjnm3lVYtYvp8vVLWtA-DsNHvhSSJRh0GW8RECRLgVbpuVx9lKFImqWMq_E5lgOdn2LBvc83H77fcnHXYHMIUbMUrjYPUAYdVyTg-c3MDk2TAlpfjNkXYKvje9UGF6GxQwEFsgEs8DhW6yb3jh642JDlxZbSq6Z16y48q_xning28mOh17v1Yu4ntDPW3Vhdh3IGPxwThbZkJX0j94rH7DGO7KLT4UKUL7SwLol3genZNNDXUv4pp7APIvgmCoTOnEMq8CigPjFpkRhTVlnj6G7ph69tDPOwpdeH07_zR9y8BiUEn8pJw7BTQx1yoMAPSCa4nbjy3YkrQrzw9LKrTpUE-DNk4mmKF8bTYj7OC2KsEFsPkK6Y2efFux-WHE_pmAMbWPXWAyX-VaKUhFPiYcD75qmbolkD960UUEON8ZMnVTXScuG10TvMvaxwlLOQo4D6w1Fu8ka5ehy21A7M9BGWbuX4x4mTirvw6w0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇹
یکسال پیش در چنین روزی برتری پرتغال به رهبری رونالدو مقابل اسپانیا در فینال لیگ‌ملت‌های اروپا و قهرمانی در این مسابقات!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107746" target="_blank">📅 14:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107745">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9decbe8c9.mp4?token=C3qasarEDmu8VuxNuAWycu9FNZV6vt-Rs0_m1-9DTvve2tphpgH-hj7EnIyl7Q3qTAgwORx6AOMUVbQiDWlI7qGwOuPSt_O4lQB-NDur6aXGpGZ-N4EZ7lKmGkYGLfZayvboPaKUCQ-Zy6Jux81gRbkViDiIoNXIE9_Ws20bmPc-4GQFDo3NsvmczLHzbBQEvAIiiCgvZVqTNcCpJuljOwJtYjCa2BWQRe6juQWBuqwc9aSJJGVmu9db_Pi7s20GgGy7w-ZOYF23O_rZc-9-pzzHntw1-lrqUn-fgpXQmObmw96Aff3yNJRvujp5b-klW9V5vPJNVpOxMtZV1TPIVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9decbe8c9.mp4?token=C3qasarEDmu8VuxNuAWycu9FNZV6vt-Rs0_m1-9DTvve2tphpgH-hj7EnIyl7Q3qTAgwORx6AOMUVbQiDWlI7qGwOuPSt_O4lQB-NDur6aXGpGZ-N4EZ7lKmGkYGLfZayvboPaKUCQ-Zy6Jux81gRbkViDiIoNXIE9_Ws20bmPc-4GQFDo3NsvmczLHzbBQEvAIiiCgvZVqTNcCpJuljOwJtYjCa2BWQRe6juQWBuqwc9aSJJGVmu9db_Pi7s20GgGy7w-ZOYF23O_rZc-9-pzzHntw1-lrqUn-fgpXQmObmw96Aff3yNJRvujp5b-klW9V5vPJNVpOxMtZV1TPIVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
یک شرکت فرآورده‌های گوشتی به این شکل کاملا منطقی تبلیغ سوسیس‌هاشو کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107745" target="_blank">📅 13:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107744">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c197e3a2a3.mp4?token=Sq7RmTsfqrndQh8OvMu0GdWlNJfM0sJqnrQtPkSuQ6vymgkWMAd9GkTqf_WEtBecqrVe3i9COkW3jt7_pQXrHearCA4xiSSyljnbFeKyY8E0kwJquFdKEqvFFvKTYH7xZ0S_6Jxsbunajn3S38NZvMdlDdR4GkxUnebk2OyVI2vXmtKsbkCEbqpBpW3H8pleZEiMYNWbtSyhZSgfqr3dZpMalc6suMw8F5LH2fZ0syTxp_aE2wmlqAA3AxpKfxOE0SAoAM0OSQTiNV3j2jIRBAQMvN9ihIw8Pegs2P7fofZKtg1zrAlZ1nx0roP4bnVnV-8NPQwNzIu2vxncJPvn3D3HteiiC6slR59-GJ-Ahb8mCO5vfBfwXEbpRTda0wZ8jwutkRA1aGUZU7vpwwE_Pb3UETp4F4Jc4knDRdp-SVcDME1jWF7bgBgkSm3gIBXfB3F8rvD9epDr3ADo55sbKbQSmzfdo9BUbRzoyPLLznsz2hFRxGKIsE_9end5FuVsKyCaZewIRNgw_1xvcychkqkhtfs-sleL43JhJR6rvlWrsTfrPQjwTaDlwLocPq3TFzWG6RLWeFY26UhNfdJXbG9p_6K-o5WLHsHG4anEy4rMuhnFuCWPbTj7Omh5hq7_Lu924rtSb7VfMCZI86MkyG2K4QEIleZalM2OtGZkMSE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c197e3a2a3.mp4?token=Sq7RmTsfqrndQh8OvMu0GdWlNJfM0sJqnrQtPkSuQ6vymgkWMAd9GkTqf_WEtBecqrVe3i9COkW3jt7_pQXrHearCA4xiSSyljnbFeKyY8E0kwJquFdKEqvFFvKTYH7xZ0S_6Jxsbunajn3S38NZvMdlDdR4GkxUnebk2OyVI2vXmtKsbkCEbqpBpW3H8pleZEiMYNWbtSyhZSgfqr3dZpMalc6suMw8F5LH2fZ0syTxp_aE2wmlqAA3AxpKfxOE0SAoAM0OSQTiNV3j2jIRBAQMvN9ihIw8Pegs2P7fofZKtg1zrAlZ1nx0roP4bnVnV-8NPQwNzIu2vxncJPvn3D3HteiiC6slR59-GJ-Ahb8mCO5vfBfwXEbpRTda0wZ8jwutkRA1aGUZU7vpwwE_Pb3UETp4F4Jc4knDRdp-SVcDME1jWF7bgBgkSm3gIBXfB3F8rvD9epDr3ADo55sbKbQSmzfdo9BUbRzoyPLLznsz2hFRxGKIsE_9end5FuVsKyCaZewIRNgw_1xvcychkqkhtfs-sleL43JhJR6rvlWrsTfrPQjwTaDlwLocPq3TFzWG6RLWeFY26UhNfdJXbG9p_6K-o5WLHsHG4anEy4rMuhnFuCWPbTj7Omh5hq7_Lu924rtSb7VfMCZI86MkyG2K4QEIleZalM2OtGZkMSE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🥇
کامبک جانانه یونس امامی در مقابل کشتی گیر ژاپنی و کسب مدال طلا بازی های آسیایی ناگویا با گزارش ابوذر کرمی نیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107744" target="_blank">📅 13:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107743">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-SR64Q_mxVCJuT6eYKeNfFR3uLA7Wt74kFrhebD_jUVmu-61iYPKzkc_aHuTMifPkg-NMRwi5peVRZkKpBUtW78MvMQ9WYAK2ranWB_jBmF2riyx6UtAQugo33z-JisERZJU3NZbAsJ2EMWBo1SkXJIgPXPLp3CjH1vc0x8HNPMjyuIZoEWqwi3SK9MyVcq9aSh1jiFpZOXwAorzU7z2mmQAwe-XT1gv2z3P1f5Hkpf7Z-bSIQ2No8c4qSNB8tBewnNorghvOjNMbmkYc3LvmrAckhKtkt48z_H8HwuFiCUzAjca9Umqn6D95lCPAQEJhbpT44PuPf06KuhsNEv5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
رافینیا در این‌فصل از مسابقات فوتبال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107743" target="_blank">📅 13:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107742">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/096e7cab86.mp4?token=FVsufPNhEFYpGO5lGvi6RTZCO6RBzn6e0CwU4kzpL_6aOl85ULMsgDAc0HRuRYhaBmpxhAMaP6fC9NhY-Eqv0a4RlOA8nY-YLBo7I3TCyPIF5Xnp0Bibqnm-n_HUoM6UXwaEs9jyjrnGYORTnQOL8QIcmLGf8A9QJQFVHUtk3yuoycXhoH8gm05dA9Gr4Z6ktaeRjEVslYp4qmzwW2DPlV8l-eUGXOioJBhic-hma_pk9a1B9O90pzQaWhWQXfe2PMHlcEJ-xA1RtmVXJMkKiZVOVz6PKJDH2I6ITaJQabxgs3KjUnjC6STws4o04zUA-4qZVvKK7rlE2lwkhe7hgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/096e7cab86.mp4?token=FVsufPNhEFYpGO5lGvi6RTZCO6RBzn6e0CwU4kzpL_6aOl85ULMsgDAc0HRuRYhaBmpxhAMaP6fC9NhY-Eqv0a4RlOA8nY-YLBo7I3TCyPIF5Xnp0Bibqnm-n_HUoM6UXwaEs9jyjrnGYORTnQOL8QIcmLGf8A9QJQFVHUtk3yuoycXhoH8gm05dA9Gr4Z6ktaeRjEVslYp4qmzwW2DPlV8l-eUGXOioJBhic-hma_pk9a1B9O90pzQaWhWQXfe2PMHlcEJ-xA1RtmVXJMkKiZVOVz6PKJDH2I6ITaJQabxgs3KjUnjC6STws4o04zUA-4qZVvKK7rlE2lwkhe7hgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
میکروفون باز، کار دست گزارشگر داد؛ جمله جنجالی هادی عامل علیه حسن یزدانی!
🔻
در حالی که پیروزی امیرعلی آذرپیرا مقابل آرش یوشیدا یکی از مهم‌ترین اتفاقات صبح کشتی ایران در بازی‌های آسیایی ناگویا بود، صحبت‌های پشت صحنه و خارج از گزارش روی آنتن زنده، یک حاشیه بزرگ برای کشتی ایران ساخت.
🔹
❌
👀
هادی عامل: صبر کنید ببینید اگه (یوشیدا) تو مسابقات جهانی به حسن (یزدانی) بخوره، ببینید با حسن چیکار می‌کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107742" target="_blank">📅 13:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107741">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35b732453.mp4?token=PEbL6SKkarOSOd1hTHZoHhm2Nj7ehuRLPFiUcG5NiWdRoHKwAqQHqZLTu2ClCGSuVusofuoyCgEfED0FG0fiCB9JVvgIrD-c1JHDd89_vT5qQqKULtZ8Hwvhh_C4VDye_whYsMaLL0VXC8c4-ptIru0gBl7jr5VKq1noQoZnVydSEnVo4cuhZ--sX4usFWIps7aIjhO7dPnAyh9WsZBDIgTOsQa1WllRtKHW19uZdEj4njEVI7mJ8-F5RAHiJnPUrVsnSmdl37t0CDUEkv8tqo-uF2jwHgp7hJyfZ66uXTTo6hdxrpX6UV39Hw9v6MqmIwyn4Zlw69eBI_y20RFdgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35b732453.mp4?token=PEbL6SKkarOSOd1hTHZoHhm2Nj7ehuRLPFiUcG5NiWdRoHKwAqQHqZLTu2ClCGSuVusofuoyCgEfED0FG0fiCB9JVvgIrD-c1JHDd89_vT5qQqKULtZ8Hwvhh_C4VDye_whYsMaLL0VXC8c4-ptIru0gBl7jr5VKq1noQoZnVydSEnVo4cuhZ--sX4usFWIps7aIjhO7dPnAyh9WsZBDIgTOsQa1WllRtKHW19uZdEj4njEVI7mJ8-F5RAHiJnPUrVsnSmdl37t0CDUEkv8tqo-uF2jwHgp7hJyfZ66uXTTo6hdxrpX6UV39Hw9v6MqmIwyn4Zlw69eBI_y20RFdgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
گزارش‌های مستهجن و عجیب گزارشگر تکواندو صداوسیما در بازی‌های آسیایی ناگویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107741" target="_blank">📅 13:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107740">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpxBgy3t-Qk-fUcuwbAxdfFQt-hCwbc4NaifA9ryJwx78G-7Audl-qtasgDoBv0YI1AozafRc2f-GocO2PPcXWpvzua_haOzlD-MEQRDrkma_p4k1jdafareK1GKZ5zEnTiv-ZhZ57tCaJCojYFkd3JV1l8Sraf42CP5aB6EeHloiw2jaZKDtsz6gLRAKe_XDNMea0BMS5fpgpn0e_cRBSJqUa_qoF0hR3doTVu3bZWdNVCj71VRKCmvOA-1fn_C8XGzWQqHmDeOIFkUhJHSmBdR0r-0o9teNhlWRFabcx--f77SeChvyCGm09_biA6zy3_jAEL_syyyZLqCpzvErw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
📊
برترین گلزنان تاریخ‌بازی‌های ملی؛ حضور اسطوره علی‌دایی از ایران در رده سوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107740" target="_blank">📅 12:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107739">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/888405197c.mp4?token=mo-FIeQHR3pxExhm-TQq_VSbk2o_J4jzhGZMf31VKHiy0nShZ-NFaiENxrzDWqR39NqAhKT460lU7-tlW90gXR9WtuNKGT6ueurhsYoeIwEWKwyT-DRE6JxYNjn5YmMGpQpX4_kwEDKrlAPTqYhVDWkg8uSHL9b6jRhcXRjMORnKyW2fBKAtusRmcg4QNwmkvOGbghvM5YqK0HM1nVjP_O95OXRbQOw9mkHSUTHY0hxj1GkLzKX_ruPydydd75RvxxVelEYvBier1p_y0p2aoV8nEvjGtrpsRW0ZSEq3HcCo6OVh2Z3PSg86LaQ48i0Eb4h3xqx_FqrgIApnU0KYgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/888405197c.mp4?token=mo-FIeQHR3pxExhm-TQq_VSbk2o_J4jzhGZMf31VKHiy0nShZ-NFaiENxrzDWqR39NqAhKT460lU7-tlW90gXR9WtuNKGT6ueurhsYoeIwEWKwyT-DRE6JxYNjn5YmMGpQpX4_kwEDKrlAPTqYhVDWkg8uSHL9b6jRhcXRjMORnKyW2fBKAtusRmcg4QNwmkvOGbghvM5YqK0HM1nVjP_O95OXRbQOw9mkHSUTHY0hxj1GkLzKX_ruPydydd75RvxxVelEYvBier1p_y0p2aoV8nEvjGtrpsRW0ZSEq3HcCo6OVh2Z3PSg86LaQ48i0Eb4h3xqx_FqrgIApnU0KYgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
ناراحتی‌ و گریه ناهید‌کیانی بعد حذف شدن از مسابقات آسیایی تکواندو ناگویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107739" target="_blank">📅 12:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107738">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56498866f7.mp4?token=m2-JJzTXWdbKUIosNVMYoYxD3FEFX44PQE3OTbO_0FlxHsNALzBj4Nbovpp9q6Nns5q7b4ppklFjwjZ2xGM6ZA98cFaKtjA1wPPU49sJUjEmAd-4mPOXRWcUBbIjlfibMZrLAE2eVH2uaPPZqv3NgLiRfhAgv_3sxl_E88R6wZGys6MstkfJbU-bm6VKL71DJRCg4GhRPVU5_TOp3nQKijJ42gH3bYsHWl6I5cKKrzqtlYq2UE05Lo7RqUT3bXjK9mkaSAlVkUocJs1lE56Q0iIAvRN8cfykq__7_xK3brkLewBRGJKhlAKkKrJFjqNg8f7hergxRVbD1sHi57q1-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56498866f7.mp4?token=m2-JJzTXWdbKUIosNVMYoYxD3FEFX44PQE3OTbO_0FlxHsNALzBj4Nbovpp9q6Nns5q7b4ppklFjwjZ2xGM6ZA98cFaKtjA1wPPU49sJUjEmAd-4mPOXRWcUBbIjlfibMZrLAE2eVH2uaPPZqv3NgLiRfhAgv_3sxl_E88R6wZGys6MstkfJbU-bm6VKL71DJRCg4GhRPVU5_TOp3nQKijJ42gH3bYsHWl6I5cKKrzqtlYq2UE05Lo7RqUT3bXjK9mkaSAlVkUocJs1lE56Q0iIAvRN8cfykq__7_xK3brkLewBRGJKhlAKkKrJFjqNg8f7hergxRVbD1sHi57q1-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
👀
گزارشگر تکواندو رو مشاهده میکنید این چنین در اوج در حال گزارش است
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107738" target="_blank">📅 12:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107737">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxVgDXbbtg2idrqQ9eNBJLj5NyJqRMIOQcAKrZNhBc78odZccrxOxed-w7acDqp20eVNr7vEXpQ3oWwAqB7wIo-8fIsUUCXOWCrkFhqMT-Ud-lV-yEoXvZAgMEF97FkQaNVuIRXZ05QhnSTiMckNAvn2z7w_IHL0JV9MUzWvKeAQkXfaNVPD7pQB9cToeO5XcQDLw0OIaLJ7q5MzP-4vSssw6mAm6SFcUwOc4G5ladJxyC8pKKdAxGoXPC_jUaWUuovAbobhbRVp_59zq86leVqcqiEnRKvjoFt8KIPjo_fRZR9Z7SJWDwRRKG55vN7JT9o_so88SakGC0ztPvljlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
مسابقات لیگ‌ملت‌های آسیا به شکل اروپا قرار است از شهریور ۱۴۰۶ آغاز شود. ایران در سطح یک این مسابقات قرار خواهد گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107737" target="_blank">📅 12:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107736">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcKuQhBnbd1n0KcH4GtBUWq1y2PkeJfyl2Zd6WIFPKd9fULXE0DSmRWOKtt-cDsvLLI_Kd1UvkivQQLNOg65Gsg9YmpQQ0ItYm7TpZ-9kCw7o_HF4z8mIlG7nZmd8HgP6ateM0cTVcSnIjlZFftZM9oMAWdI1DLSQexfxF6FFA4YgxSDWeCOgqYmxTulBN2FgESlyYeyKwxKZFjgZNlE3pu-SeNL6HOaz9f51ViHyty_EkAnFHKxaoa7SWsaP-LP3MlTjUK7bA_d3JGPFRs_t60EYpeR1V1jbt6jfFkakEXBNhqWadLC7KH8HVemrretDmGAIQAQ0JZdpnXmxwrxrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
اسامی نفرات برتر آزمون کنکور ۱۴۰۵؛ نتایج اولیه برای تمامی داوطلبان تا ساعاتی دیگه اعلام میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107736" target="_blank">📅 11:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107735">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6316faf3f3.mp4?token=fxkxlhanP-ZzpShmxJNf_o-G7jFKh4Jfc3yFkhCR0BlR9YiAKr2b7BL_XVo1rnJSucIumpfYj8ZsBWLRwg2BrlI3nuNTKAdeXn0afkoHOpjWXMXvr2PLmqriCeos_vilAdEc85A8GBSzwixi0oNm2O3xfRxH95-KMPbj1siwQV_VPHFu5UAyv9yrXgP4ygz1g7k3OLjGhNWDC2qNb6NJ7qmvsuCGITIE2eSIbxWYAXyt18HzJkVqhOWWCM1B5DA_Q0CiRQMyRcQxy3B32BF5mWm4h0j5yzi-t_ZzUVIa7PAq5Ll3NO_QMBEbbG-mfPVH2BYdoGy8Hs1sPKcPixyHWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6316faf3f3.mp4?token=fxkxlhanP-ZzpShmxJNf_o-G7jFKh4Jfc3yFkhCR0BlR9YiAKr2b7BL_XVo1rnJSucIumpfYj8ZsBWLRwg2BrlI3nuNTKAdeXn0afkoHOpjWXMXvr2PLmqriCeos_vilAdEc85A8GBSzwixi0oNm2O3xfRxH95-KMPbj1siwQV_VPHFu5UAyv9yrXgP4ygz1g7k3OLjGhNWDC2qNb6NJ7qmvsuCGITIE2eSIbxWYAXyt18HzJkVqhOWWCM1B5DA_Q0CiRQMyRcQxy3B32BF5mWm4h0j5yzi-t_ZzUVIa7PAq5Ll3NO_QMBEbbG-mfPVH2BYdoGy8Hs1sPKcPixyHWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
شبکه سه اومد بازی جودوکار خانم ایران تو مسابقات آسیایی رو پخش کنه که جودکار ایرانی تو ثانیه اول درجا بازیو باخت و حذف شد ...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107735" target="_blank">📅 11:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107732">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68d8475315.mp4?token=UCibz9A7L-ilwBbCSVbVD1GLHBRNvdWxGMQcFpdhXjGaswPQq9A2wnzs7bkfM8PCc45VJxcoSqckXA4dXpND5YW97746Rr9M1aVDwKZDPWxfbhqj8HseEyYuel9bgM_vFnrMrvBN2Zcraq_hEgiseF67cLRyHHeXh20sNkToYELi8x7vL3k9S7FwrKhyRIQmJcG7ZgQlNX-sg71N2AHcy_AgSLfdMgOyOBB3OtbdoL9BVHk85Hh57R24swauGxjATFzEuNs3gdZkR5iWA04KAIcI2Tgv4y5pNCYZA30UovHY0tjZ8YCi7ZgmIngQdX28nObnViZXu6lag7wMMF8Yjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68d8475315.mp4?token=UCibz9A7L-ilwBbCSVbVD1GLHBRNvdWxGMQcFpdhXjGaswPQq9A2wnzs7bkfM8PCc45VJxcoSqckXA4dXpND5YW97746Rr9M1aVDwKZDPWxfbhqj8HseEyYuel9bgM_vFnrMrvBN2Zcraq_hEgiseF67cLRyHHeXh20sNkToYELi8x7vL3k9S7FwrKhyRIQmJcG7ZgQlNX-sg71N2AHcy_AgSLfdMgOyOBB3OtbdoL9BVHk85Hh57R24swauGxjATFzEuNs3gdZkR5iWA04KAIcI2Tgv4y5pNCYZA30UovHY0tjZ8YCi7ZgmIngQdX28nObnViZXu6lag7wMMF8Yjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
⚠️
دو قاب از بيژن‌مرتضوی به فاصله ۴ سال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/107732" target="_blank">📅 11:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107731">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fbb258d04.mp4?token=a3Ugw8lfdqloi4c729ddYJFBRW_H_KvKV8wF98lx4JeOGZ_1iZtghSuHzh6InCZqx2qw5aIY7cgu_aWx3wYK4jwFGyV_euDwpwG-lLnq2ayxak0OAoedvieqMXE13WmrYUJlLxhjoh7Fn6-haOkhsu-wj6YMvq8MMLGG9y_oPv8HtnRfmFkRekQZ04ML2zcU_yqL9LhIkzW5SL_wzWQ8zZDw3Uj2NaSLkrK6lyyYNTNmvppIxGeCUnjs_cwgNqhKlumbpxpx_FqkjOPYhWObIjI1OwvLagakS3QUfN0K9DjHnSWQIOzP55mgK3rAy8cwyhVJYgzXpuyVRf_JAfN42w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fbb258d04.mp4?token=a3Ugw8lfdqloi4c729ddYJFBRW_H_KvKV8wF98lx4JeOGZ_1iZtghSuHzh6InCZqx2qw5aIY7cgu_aWx3wYK4jwFGyV_euDwpwG-lLnq2ayxak0OAoedvieqMXE13WmrYUJlLxhjoh7Fn6-haOkhsu-wj6YMvq8MMLGG9y_oPv8HtnRfmFkRekQZ04ML2zcU_yqL9LhIkzW5SL_wzWQ8zZDw3Uj2NaSLkrK6lyyYNTNmvppIxGeCUnjs_cwgNqhKlumbpxpx_FqkjOPYhWObIjI1OwvLagakS3QUfN0K9DjHnSWQIOzP55mgK3rAy8cwyhVJYgzXpuyVRf_JAfN42w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚪️
نه به تیم‌ملی چیز جدید اضافه کردن و نه تونستن جام خاصی به ارمغان بیارن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107731" target="_blank">📅 11:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107730">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8086af61bd.mp4?token=N24f4SX_RXUaHTwd6Hy7gGXqbq9YJEroNyxBk7TQDTvabBu1qkv-6HejgyM9CjtyHl7fgXvTrEVCvSOFo6ap9xJ2aZHvTBXzzqRfenHVyd6fA2EYxbKGlclMTOEaw-nvso4L1gs5D0g0xOwIUzysNkOd0NAxJ6qs3kBZqFCI5lpuRcaCFg2ejB-7IgZuNKmxFUNFbrXxiDv_SpjSCUEsMUK_eNwKOW1hwfn_cnIimThvJqG2lV9Og2g-NzLfeK5_W-ZbtEtF-TKNKvgDQ1P5LOrBvHcbongBqCo9s7ptwr3s5BbxW5WfuopEuejXvkLgMjLEQLWqGTQOJTi7S473XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8086af61bd.mp4?token=N24f4SX_RXUaHTwd6Hy7gGXqbq9YJEroNyxBk7TQDTvabBu1qkv-6HejgyM9CjtyHl7fgXvTrEVCvSOFo6ap9xJ2aZHvTBXzzqRfenHVyd6fA2EYxbKGlclMTOEaw-nvso4L1gs5D0g0xOwIUzysNkOd0NAxJ6qs3kBZqFCI5lpuRcaCFg2ejB-7IgZuNKmxFUNFbrXxiDv_SpjSCUEsMUK_eNwKOW1hwfn_cnIimThvJqG2lV9Og2g-NzLfeK5_W-ZbtEtF-TKNKvgDQ1P5LOrBvHcbongBqCo9s7ptwr3s5BbxW5WfuopEuejXvkLgMjLEQLWqGTQOJTi7S473XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
▶️
تلخ‌ترین صحبت‌های مالک موبو نیوز در گفتگو با امیرحسین قیاسی...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107730" target="_blank">📅 10:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107729">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdae91c6ba.mp4?token=EkX-SX3jUq3NqPhiYafq5M2vfUqS5gsdTZZu8yn6Y8NF8YKRX-x0jQ-QUGIW-wvNdJBPV-GYe5NrAqUGZTYiETnTZ3xkN90Lb19br9UGyGTgCxa-dokgAovY28LS0HUbRnQ87Xfs9JvfafvfoQ0LNsj-qNPS4YOAVPkofmiXMF0944zbvDBjsdppizZzvwcOjILF-rDNkxa-VHa7VS8kxSd3FClmZqpjnbSfmKjOpnaWxQDS3rHbWXsmhOU24w045QVxOwJ8ptRrF1Hui1L-hhWfPCA0Z-adWdukdzuLCnRs_sXDIUSskvffXxJwoO4c2Six6U94TOBXcKoy-9XHrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdae91c6ba.mp4?token=EkX-SX3jUq3NqPhiYafq5M2vfUqS5gsdTZZu8yn6Y8NF8YKRX-x0jQ-QUGIW-wvNdJBPV-GYe5NrAqUGZTYiETnTZ3xkN90Lb19br9UGyGTgCxa-dokgAovY28LS0HUbRnQ87Xfs9JvfafvfoQ0LNsj-qNPS4YOAVPkofmiXMF0944zbvDBjsdppizZzvwcOjILF-rDNkxa-VHa7VS8kxSd3FClmZqpjnbSfmKjOpnaWxQDS3rHbWXsmhOU24w045QVxOwJ8ptRrF1Hui1L-hhWfPCA0Z-adWdukdzuLCnRs_sXDIUSskvffXxJwoO4c2Six6U94TOBXcKoy-9XHrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
یه راه خوب برای کنترل هزینه‌های اینترنت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107729" target="_blank">📅 10:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107728">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c37b6c6ac.mp4?token=P2nt0k-2kZzeG9GkCdtrWdPqaLd5yc3cWSOc1rb1DQMLRKmd1TilFC_4EykNQPHhfUHqngP4cOnxYonI2jC6ip_awe-5XWEolrKc6QF_LtGGVcizicEQlKeHIncoOk3HqX3Z4tJNS10OEmQ0msPzmVddUTzGOGuxg4wsOSyCiKC60dGMeFWME02Y58yhPKLkRuawx8ddpJyudoJExHtOWSxVSFMCSrjxYYhsD0xmfaHmw3SeSAfapSoWOH4ZBmfVcfy8TK3asYCu7CZriD0pUUxfcuu5XooDOfHQwbf50u1u91UGxkQVxHpzxtl09W99fM9AAmtiDCcF_uIxnCoIXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c37b6c6ac.mp4?token=P2nt0k-2kZzeG9GkCdtrWdPqaLd5yc3cWSOc1rb1DQMLRKmd1TilFC_4EykNQPHhfUHqngP4cOnxYonI2jC6ip_awe-5XWEolrKc6QF_LtGGVcizicEQlKeHIncoOk3HqX3Z4tJNS10OEmQ0msPzmVddUTzGOGuxg4wsOSyCiKC60dGMeFWME02Y58yhPKLkRuawx8ddpJyudoJExHtOWSxVSFMCSrjxYYhsD0xmfaHmw3SeSAfapSoWOH4ZBmfVcfy8TK3asYCu7CZriD0pUUxfcuu5XooDOfHQwbf50u1u91UGxkQVxHpzxtl09W99fM9AAmtiDCcF_uIxnCoIXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
بیخیالی بازیکن های پرتغال از رفتن رونالدو دقیقا یاد این سکانس تاریخی میندازه !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107728" target="_blank">📅 09:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107727">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZXUtNIJTGEMlv4JoyC0O-Lm0dvmawBvFXLrVdrD1HMWj6oLHyp3gHR5KarDSuBSBfbmwC90hxY0sOrS9vrJyKkqQb-ntU3R-QebwSTZg5ubeOEefl0QgFvRiYT3ulCjMveuA40vb7ie47eVK1FJeMXQn0l2HccwcM7nCD19QH1XKVp3JewoB7l2xEHY2gSQbQ3aM2HlKum9d5NqCcJSR0XacBvzganBxVsY_QaWUsQ05W12B4TVFiaRWzRq2SX-PoHSpx2otqpoUx1TVW6Z_mxsiGCgCOgkXJ9-cs0HU0zdin3TM4_vs8Qq4CbVsK-4-k_p8BIs5QncyBvgaWOCRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇶🇦
با اعلام‌رومانو: ریاض‌محرز با عقد قراردادی به الشمال قطر، رقیب استقلال و تراکتور در لیگ‌نخبگان آسیا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107727" target="_blank">📅 09:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107726">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b5c7684c2.mp4?token=RaG_TTtyOa-xIuRDKH5ug93CAk98M_sD5Bob-kMPPOfKtFImR8tECwXXXmL6Oe0ClEMVhsnqYbqjDXSPNKSMn6DyZ0xrFyK2GMHc3Uff_NW8kimYVpD3l9K7sPtf4ateB36ydXa25-xpuJ-M-400u5K9QjhpeRujV9acEKx90Qa17fMg9EtTxpjkU1C8PFbYd7b67t94CGs9hs-6xmPL0twVxmPT1EErEhRzG5BGpOvc6QFZ7YZUPZfWSAQGi0-tHrAQ2jpPOYUvGBpBBlPX2S2o1voeIOl96oPXGpGU3bla9uG6JBpXMJX3Nf34J97kdIFQK65W4pzovOoSnlOVGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b5c7684c2.mp4?token=RaG_TTtyOa-xIuRDKH5ug93CAk98M_sD5Bob-kMPPOfKtFImR8tECwXXXmL6Oe0ClEMVhsnqYbqjDXSPNKSMn6DyZ0xrFyK2GMHc3Uff_NW8kimYVpD3l9K7sPtf4ateB36ydXa25-xpuJ-M-400u5K9QjhpeRujV9acEKx90Qa17fMg9EtTxpjkU1C8PFbYd7b67t94CGs9hs-6xmPL0twVxmPT1EErEhRzG5BGpOvc6QFZ7YZUPZfWSAQGi0-tHrAQ2jpPOYUvGBpBBlPX2S2o1voeIOl96oPXGpGU3bla9uG6JBpXMJX3Nf34J97kdIFQK65W4pzovOoSnlOVGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚪️
سقوط تیم‌ملی به روایت اصغر مازیار!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107726" target="_blank">📅 09:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107725">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d02e44cc.mp4?token=IgjAKOrnEsJHMjEGAI47_Fli33jRxobZRXqfusujA5HIK0ZcbU6H8owT-I8eJ_mh1KWQsbWsdoBagdbJJxj0l9CgdR0z1nzvH6MOt9IutRaHDNC0NuKsH50UTsaoivJTzG1aMj7TeiUr3Jt3Bicir9SVyxkyRUJ_dkDfiNPU96aQJAY5HnyV6wsDO-A0svhctvoUaKrgVthi04809yT2C4MGsO01DWA4XLftR90rop1BhyXl5SgfcyfN2X6skJtDFB4Ju7YfyS1ZtP6SusR2lFtcqkOwn35gJUFJG02x2LlyHLSl5iHOuYudX48UO07KD9tuvKW6hR8LyCbLIzOobQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d02e44cc.mp4?token=IgjAKOrnEsJHMjEGAI47_Fli33jRxobZRXqfusujA5HIK0ZcbU6H8owT-I8eJ_mh1KWQsbWsdoBagdbJJxj0l9CgdR0z1nzvH6MOt9IutRaHDNC0NuKsH50UTsaoivJTzG1aMj7TeiUr3Jt3Bicir9SVyxkyRUJ_dkDfiNPU96aQJAY5HnyV6wsDO-A0svhctvoUaKrgVthi04809yT2C4MGsO01DWA4XLftR90rop1BhyXl5SgfcyfN2X6skJtDFB4Ju7YfyS1ZtP6SusR2lFtcqkOwn35gJUFJG02x2LlyHLSl5iHOuYudX48UO07KD9tuvKW6hR8LyCbLIzOobQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وای این چه سمی بوددددد
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107725" target="_blank">📅 08:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107721">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107721" target="_blank">📅 00:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107720">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/blTKI4mJpd34y1d5NGK_fRE8Qb6wqFww3lotSZIxM3UNSC-XjO9BDB1mjP3cmegf0Dj-DJ_kc227Ze7TgfgZK_q7xJmcg62yEOj2smeeO383Vgg6mU8BymXZrivd-1FsS85xFS3_cG7_zgKfstzLsZ8BA6kDvvypV-PBTzqdfYbijGkZVCI596Pnw1ZNf-2ZScVbxYNnfWqJjHZDH0yRXvjCXd4F8iZ9Nma40O6FxT3pxV4JGf9HWLCTToBVlm-a3Xb1rCGLa0KVCzE4a1zs1fwHtXUZuJyLyuonfiTk9Q1_Glr_02GVerIYn5Es1L-sPyeu3-DjonKGOCMUf29rKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
بنر هواداران عربستانی برای بازی مقابل قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107720" target="_blank">📅 00:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107719">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇹
🇫🇷
هایلایت بازی فرانسه یک - یک ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107719" target="_blank">📅 00:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107718">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
❌
🇮🇷
علوی، سخنگوی فدراسیون فوتبال: استقلال قهرمان فصل گذشته نشده و بحث جدیدی درمورد اهدای جام به این تیم نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107718" target="_blank">📅 00:05 · 11 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
